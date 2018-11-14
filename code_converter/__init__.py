# from define import Define
# from guid import GUID
# from interface import Interface
# from importer import Importer
# from enum import Enum
# from structure import Structure
# from union import Union
# from comment import Comment
# from includes import Includes
# from typedef import Typedef
from __future__ import print_function, absolute_import

from code_converter.includes import parse_include
from code_converter.enum import parse_enum
from code_converter.define import parse_define
from code_converter.comment import parse_comment, equalize_width
from code_converter.structure import parse_struct_union, u_s_declarations
from code_converter.interface import parse_interface, interface_declarations
from code_converter.dll import parse_dll, write_functions, print_not_found
from code_converter.guid import parse_guid

from code_converter import preprocessor

for key in sorted(preprocessor.__dict__.keys()):
    print(key)


parse_macro = preprocessor.parse_macro

import re


class Allowed:
    def __contains__(self, item):
        return False

    def __iter__(self):
        return iter([])


class Importer:

    allowed = Allowed()

    @staticmethod
    def add(*args, **kwargs):
        pass



FUNDAMENTAL_TYPES = {
    'short': 'SHORT',
    'short int': 'SHORT',
    'signed short': 'SHORT',
    'signed short int': 'SHORT',
    'unsigned short': 'USHORT',
    'unsigned short int': 'USHORT',
    ' int ': ' INT ',
    '(int)': '(INT)',
    '(int ': '(INT ',
    'signed': 'INT',
    'signed int': 'INT',
    'unsigned': 'UINT',
    'unsigned int': 'UINT',
    'long': 'LONG',
    'long int': 'LONG',
    'signed long': 'LONG',
    'signed long int': 'LONG',
    'unsigned long': 'ULONG',
    'unsigned long int': 'ULONG',
    'long long': 'LONGLONG',
    'long long int': 'LONGLONG',
    'signed long long': 'LONGLONG',
    'signed long long int': 'LONGLONG',
    'unsigned long long': 'ULONGLONG',
    'unsigned long long int': 'ULONGLONG',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'long double': 'LONG',
    'void': 'VOID',
    'char': 'CHAR',
    'signed char': 'CHAR',
    'unsigned char': 'UCHAR',
    'boolean': 'BOOL',
    'bool': 'BOOL',
    '__int8': 'INT8',
    '__int16': 'INT16',
    '__int32': 'INT32',
    '__int64': 'INT64',
    'wchar_t': 'WCHAR',
    '__wchar_t': 'WCHAR',
    '||': ' or ',
    '&&': ' and ',
    'sizeof': 'ctypes.sizeof',
    'memmove': 'ctypes.memmove',
    'memset': 'ctypes.memset',
    '__INT64': 'INT64',
    '__export': '',
    '__override': '',
    '__WRAPPED__': '',
    '_Struct_size_bytes_(Size)': '',
    'const ': '',
    '[ ]': '[]',
    '[  ]': '[]',
    '&lt;': '<',
    '&gt;': '>'
}

import os
import re

def convert(data):

    for key, value in FUNDAMENTAL_TYPES.items():
        data = data.replace(key, value)

    data = re.sub("!(?!=)", 'not ', data)
    data = re.sub("(?! )==(?! )", ' == ', data)
    data = re.sub(r"(?! )\+(?! )", ' + ', data)
    data = re.sub(r"(?! )\-(?! )", ' - ', data)
    data = re.sub("(?! )<=(?! )", ' <= ', data)
    data = re.sub("(?! )>=(?! )", ' >= ', data)
    data = re.sub("(?! )!=(?! )", ' != ', data)
    data = re.sub("(?! )<<(?! )", ' << ', data)
    data = re.sub("(?! )>>(?! )", ' >> ', data)
    data = re.sub(r"(?! )\|(?! )", ' | ', data)
    data = re.sub("(?! )(?!>)>(?!>)(?! )", ' > ', data)
    data = re.sub("(?! )(?!<)<(?!<)(?! )", ' < ', data)
    data = re.sub("(?! )&(?! )", ' & ', data)
    data = re.sub("  or  ", ' or ', data)
    data = re.sub("  and  ", ' and ', data)

    return data


TEMPLATE_MIDL = '''MIDL_INTERFACE(
{1}    "{{{{{0}}}}}"
{1})'''
TEMPLATE_IID = '''IID(
{1}    "{{{{{0}}}}}"
{1})'''
TEMPLATE_DECLSPEC = '''DECLSPEC_UUID(
{1}    "{{{{{0}}}}}"
{1})'''


def gen_code(file_path=None, output='', string_data=None, dll=None):
    # output_path = os.path.dirname(output)

    idl_file = os.path.splitext(file_path)[0] + '.idl'

    interfaces = []
    libraries = []
    preprocessor.module_name = file_path

    if os.path.exists(idl_file):
        with open(idl_file, 'r') as f:
            idl = f.read()

        idl = convert(idl)

        idl = list(l.rstrip() for l in idl.split('\n'))
        idl_brace_count = 0
        found_struct = False
        found_enum = False
        found_interface = ''
        interface_capture = None
        found_library = None
        found_coclass = None
        found_data = []
        options = []

        def get_interface_capture():
            res = dict(
                idl_flags=[],
                version=None,
                iid='None{indent}',
                helpstring='',
                cls_name='',
                reg_typelib=None,
                co_class=False,
                library=False,
                methods=[]
            )
            idl_flags = []
            for attr in options:
                for itm in (
                    '[',
                    ']',
                    'uuid',
                    'helpstring',
                    'version',
                    'object',
                    'pointer_default',
                    'local',
                ):
                    if attr.strip().startswith(itm):
                        break
                else:
                    idl_flags += [attr.strip()]
                    continue

                if attr.startswith('uuid'):
                    attr = attr.replace('uuid', '').replace(',', '')
                    res['iid'] = attr.strip()[1:-1].replace(' ', '').upper()

                if attr.startswith('helpstring'):
                    attr = attr.replace('helpstring', '').replace(',', '')
                    res['helpstring'] = attr.strip()[2:-2]

                if attr.startswith('version'):
                    attr = attr.replace('version', '').replace(',', '')
                    res['version'] = attr.strip()[1:-1]

            res['idl_flags'] = idl_flags

            del options[:]
            return res

        for i, line in enumerate(idl[:]):
            if line.strip().startswith('[') and '[default]' not in line:
                interface_capture = []

            if interface_capture is not None:
                interface_capture += [line.strip().replace(',', '')]
                if line.strip().endswith(']'):
                    options = interface_capture[:]
                    interface_capture = None

            # if line.strip().startswith('cpp_quote'):
            #     line = line.replace('cpp_quote', '', 1).strip()[2:-2]
            #     continue
            #
            # if line.strip().startswith('import'):
            #     line = line.replace('import', '#include', 1)[:-1].replace('.idl', '.h')
            #     continue

            if line.strip().startswith('coclass'):
                found_coclass = line.replace('coclass', '').strip()

                interface_data = get_interface_capture()
                if interface_data['iid']:
                    interface_data['iid'] = TEMPLATE_DECLSPEC.format(
                            interface_data['iid'],
                            '{indent}'
                        )

                interface_data.update(
                    dict(
                        iid_name='CLSID_' + found_coclass,
                        cls_name=found_coclass,
                        com_interfaces=[],
                        co_class=True,
                    )
                )

                for library in libraries:
                    if library['cls_name'] == found_library:
                        version = library['version']
                        if version is not None:
                            version = list(int(v) for v in version.split('.'))
                            reg_typelib = (
                                ['LIBID_' + found_library] + version
                            )

                            interface_data['reg_typelib'] = tuple(reg_typelib)
                            library['reg_typelib'] = tuple(reg_typelib)

                        break
                libraries += [interface_data]

            if found_coclass and 'interface' in line:
                co_interface = line.split('interface')[1].replace(';', '')
                co_interface = co_interface.strip()

                for library in libraries:
                    if library['cls_name'] == found_coclass:
                        library['com_interfaces'] = [co_interface]

            #
            # if line.strip().startswith('typedef enum'):
            #     found_enum = True
            #
            # if line.strip().startswith('typedef struct'):
            #     found_struct = True
            #
            # if found_struct or found_enum:
            #     idl_brace_count += line.count('{')
            #     idl_brace_count -= line.count('}')
            #
            #     if ';' in line and idl_brace_count == 0:
            #         found_enum = False
            #         found_struct = False
            #         continue
            #
            # if found_struct and line.strip().startswith('['):
            #     s_indent, line = line.split('[', 1)
            #     line = line.split(']', 1)[1]
            #     line = s_indent + line
            #     idl[i] = line

            if line.startswith('interface'):
                line = line.replace('interface', '')
                try:
                    interface_name, interface_parent = (
                        line.replace('interface', '').split(':')
                    )

                except ValueError:
                    interface_name = line
                    interface_parent = 'IUnknown'

                interface_name = interface_name.replace(';', '').strip()
                interface_parent = interface_parent.replace('{', '').strip()

                interface_parent = interface_parent.replace(
                    'IUnknown',
                    'comtypes.IUnknown'
                )

                interface_data = get_interface_capture()
                if interface_data['iid']:
                    interface_data['iid'] = TEMPLATE_MIDL.format(
                        interface_data['iid'],
                        '{indent}'
                    )

                interface_data.update(
                    dict(
                        iid_name='IID_' + interface_name,
                        cls_name=interface_name,
                        parent_cls=interface_parent
                    )
                )

                for j, interface in enumerate(interfaces):
                    if interface['cls_name'] == interface_name:
                        interfaces[j] = interface_data
                        break
                else:
                    interfaces += [interface_data]

                found_interface = interface_name

            if line.strip().startswith('library'):
                found_library = line.replace('library', '').strip()

                library_data = get_interface_capture()
                if library_data['iid']:
                    library_data['iid'] = TEMPLATE_IID.format(
                        library_data['iid'],
                        '{indent}'
                    )
                    library_data.update(
                        dict(
                            iid_name='LIBID_' + found_library,
                            cls_name=found_library,
                            library=True,

                        )
                    )

                for j, library in enumerate(libraries):
                    if library['cls_name'] == found_library:
                        libraries[j] = library_data
                        break
                else:
                    libraries += [library_data]

            if found_library or found_interface or found_coclass:
                if idl_brace_count != 0:
                    found_data += [line]

                idl_brace_count += line.count('{')
                idl_brace_count -= line.count('}')

                if idl_brace_count == 0 and (';' in line or line.strip() == '}'):
                    if found_coclass:
                        container = libraries
                        name = found_coclass

                    elif found_interface:
                        container = interfaces
                        name = found_interface
                        found_interface = ''
                    else:
                        container = libraries
                        name = found_library
                        found_library = ''

                    for cont in container:
                        if cont['cls_name'] == name:
                            cont['methods'] = found_data[:]
                            if not found_coclass:
                                del found_data[:]
                            else:
                                found_coclass = ''

    with open(file_path, 'r') as f:
        string_data = f.read()

    string_data = convert(string_data)
    string_data = string_data.replace('\t', '    ').split('\n')

    namespace = {}
    steps = [None]
    new_lines = ''
    chained_comment = False
    skip_lines = None
    anon_struct_count = 0
    anon_union_count = 0
    union_struct_fwd_definitions = []
    tdef = False
    COBJMACROS = False
    found_dlls = []

    def check_state_step():
        if steps[-1] is not None:
            step = steps[-1]
            parse_macro('    ' * (len(steps) - 2), step.strip(), True)
            print('    ' * (len(steps) - 1) + 'pass')
            steps[len(steps) - 1] = None

    def handle_preprocessor():

        for j, step in enumerate(steps):

            if step is not None:
                step_indent = '    ' * step.count('    ')

                parse_macro(step_indent, step.strip(), True)
                steps[j] = None

    if interfaces:
        print('''def annotation(value):\n    if '_opt_' in value:\n        return comtypes.defaultvalue(None)\n    else:\n        return None\n''')

    for i, line in enumerate(string_data):

        if 'COBJMACROS' in line and not COBJMACROS:
            COBJMACROS = True
            continue

        if chained_comment and '*/' not in line:
            continue

        if line.strip() == 'typedef':
            tdef = True
            continue

        for item in ('ifndef', 'ifdef', 'elif', 'if', 'else', 'endif', 'define'):
            line = line.replace('# ' + item, '#' + item)

        indent = '    ' * (len(steps) - 1)
        indent_count = len(indent)

        for item in ('ifdef', 'ifndef', 'if'):
            if line.strip().startswith('#' + item):
                COBJMACROS = False
                if new_lines:
                    print()
                    new_lines = ''
                steps += [line]
                break
        else:
            for item in ('elif', 'else'):
                if line.strip().startswith('#' + item):
                    COBJMACROS = False
                    check_state_step()
                    steps[len(steps) - 1] = line
                    break
            else:
                if line.strip().startswith('#endif'):
                    if COBJMACROS:
                        COBJMACROS = False
                        continue
                    check_state_step()
                    if len(steps) > 1:
                        steps = steps[:-1]

                    parse_macro('    ' * (len(steps) - 1), line.strip(), True)
                    continue

        if COBJMACROS:
            continue

        line, _ = parse_comment(line.strip())
        if line is None:
            line = string_data[i].split('/*')[0]

        for interface_data in interfaces[:]:
            pattern1 = 'typedef interface {0} {0};'.format(
                interface_data['cls_name']
            )

            pattern2 = 'typedef struct {0}Vtbl'.format(
                interface_data['cls_name']
            )

            if pattern1 in line:
                handle_preprocessor()
                parse_interface(
                    indent,
                    interface_data['methods'],
                    Importer,
                    interface_data,
                    True
                )
                break

            if pattern2 in line:
                handle_preprocessor()
                parse_interface(
                    indent,
                    interface_data['methods'],
                    Importer,
                    interface_data,
                    False
                )
                interfaces.remove(interface_data)
                break
        else:
            for interface_data in libraries:
                pattern = 'typedef struct {0} {0};'.format(
                    interface_data['cls_name']
                )

                declare = 'defined' not in interface_data
                if pattern in line:
                    handle_preprocessor()
                    parse_interface(
                        indent,
                        interface_data['methods'],
                        Importer,
                        interface_data,
                        declare
                    )
                    break

                for pattern in ('IID', 'CLSID'):
                    pattern = 'EXTERN_C const {0} {1}'.format(
                        pattern,
                        interface_data['iid_name']
                    )

                    if pattern in line:
                        handle_preprocessor()
                        parse_interface(
                            indent,
                            interface_data['methods'],
                            Importer,
                            interface_data,
                            declare
                        )
                        break
                else:
                    continue

                if not declare:
                    libraries.remove(interface_data)
                break
            else:
                if skip_lines is not None:
                    start, stop = skip_lines
                    if start <= i <= stop:
                        continue

                    skip_lines = None

                if line.startswith('DECLARE_HANDLE'):
                    var_name = line.split('(', 1)[1].split(')', 1)[0]
                    print(indent + var_name + ' = DECLARE_HANDLE()')
                    continue

                if line.startswith('#define'):
                    if '/*' in line:
                        line = line.split('/*')[0]

                    if line.endswith('\\'):
                        define = ''
                        start = i
                        stop = i
                        for j, d in enumerate(string_data[i:]):
                            stop = i + j
                            if '/*' in d:
                                d, comment = d.split('/*', 1)
                                d = d.strip()
                                if d.endswith('\\'):
                                    d = d[:-1] + ' /*' + comment
                                    define += d
                                else:
                                    d = d + ' /*' + comment
                                    define += d
                                    break
                            else:
                                define += d

                                if d.endswith('\\'):
                                    define = define[:-1]
                                else:
                                    break
                        skip_lines = [start, stop]
                    else:
                        define = line

                    handle_preprocessor()
                    if parse_define('    ' * (len(steps) - 1), define, Importer):
                        new_lines = '\n'
                    else:
                        skip_lines = None

                new_line, comment = parse_comment(line)

                if new_line:
                    guid_line = parse_guid(indent, [new_line])
                    if guid_line:
                        handle_preprocessor()
                        if comment:
                            print(comment)
                        print(guid_line)
                        continue

                if line.startswith('enum') or line.startswith('typedef enum'):
                    if new_lines:
                        print(new_lines)
                        new_lines = ''

                    brace_count = 0
                    enum = []
                    start = i
                    stop = i
                    for j, enum_line in enumerate(string_data[i:]):
                        if j + i == i:
                            temp_line = enum_line.strip()

                            if temp_line.startswith('enum'):
                                temp_line = string_data[j - 1].strip()
                                if (
                                    'typedef' in temp_line
                                    and ';' not in temp_line
                                ):
                                    enum_line = enum_line.replace(
                                        'enum',
                                        'typedef enum',
                                        1
                                    )
                        stop = j + i
                        brace_count += enum_line.count('{')
                        brace_count -= enum_line.count('}')

                        if not enum_line.startswith(indent):
                            enum_line = indent + enum_line.lstrip()

                        enum += [enum_line[indent_count:]]

                        if ';' in enum_line and brace_count == 0:
                            break

                    if tdef:
                        enum[0] = enum[0].replace('enum', 'typedef enum', 1)
                        tdef = False

                    skip_lines = [start, stop]
                    handle_preprocessor()
                    parse_enum(indent, enum, namespace)

                elif (
                    line.startswith('struct') or
                    line.startswith('union') or
                    line.startswith('typedef struct') or
                    line.startswith('typedef union')
                ):
                    brace_count = 0
                    struct = []
                    start = i
                    stop = i
                    for j, struct_line in enumerate(string_data[i:]):
                        if j + i == i:
                            temp_line = struct_line.strip()

                            if (
                                temp_line.startswith('struct') or
                                temp_line.startswith('union')
                            ):
                                temp_line = string_data[j - 1].strip()
                                if (
                                    'typedef' in temp_line
                                    and ';' not in temp_line
                                ):
                                    struct_line = struct_line.replace(
                                        'struct',
                                        'typedef struct',
                                        1
                                    )
                                    struct_line = struct_line.replace(
                                        'union',
                                        'typedef union',
                                        1
                                    )

                        stop = j + i
                        struct += [struct_line]
                        brace_count += struct_line.count('{')
                        brace_count -= struct_line.count('}')
                        if ';' in struct_line and brace_count == 0:
                            break

                    struct = '\n'.join(struct)
                    if tdef:
                        if struct.strip().startswith('struct'):
                            struct = struct.replace('struct', 'typedef struct', 1)
                        else:
                            struct = struct.replace('union', 'typedef union', 1)

                        tdef = False

                    skip_lines = [start, stop]
                    handle_preprocessor()
                    anon_struct_count, anon_union_count = parse_struct_union(
                        indent,
                        struct,
                        Importer,
                        anon_struct_count,
                        anon_union_count,
                        union_struct_fwd_definitions,
                        True
                    )
                    continue

                else:
                    chained_comment = False

                    if line.strip().startswith('typedef') and ';' in line:
                        handle_preprocessor()
                        line, comment = parse_comment(line)

                        line = line.replace('typedef', '').strip()
                        line = line.replace(';', '').strip()
                        var_names = []
                        hold_over = ''
                        for l in line.split(' '):
                            if not l.strip():
                                continue

                            if hold_over:
                                l = hold_over + l
                                hold_over = ''
                            if l == '*':
                                hold_over = '*'
                                continue
                            if l == '**':
                                hold_over = '**'
                                continue
                            l = l.strip().rstrip(',')
                            for v in l.split(','):
                                v = v.strip()
                                var_names += [v]
                        value = var_names[0]
                        var_names = var_names[1:]
                        from code_converter.utils import process_param

                        if comment:
                            print(indent + comment)
                        for var_name in var_names:
                            new_var_name, new_value = process_param(
                                var_name,
                                value
                            )

                            if new_var_name != new_value:
                                print(indent + new_var_name + ' = ' + new_value)
                        continue

                    if line.strip().startswith('#include'):
                        line, comment = parse_comment(line)
                        line = line.replace('#include', '').strip()
                        line = line.replace('<', '').replace('>', '')
                        line = line.replace('"', '').strip()
                        line = line.replace('.h', '_h')
                        line = line.replace('/', '.').replace('\\', '.')
                        handle_preprocessor()
                        print(indent + 'from {0} import * # NOQA'.format(line))
                        continue

                    tdef = False

                    new_line, comment = parse_comment(string_data[i])

                    if new_line is not None and new_line.strip() and ';' not in new_line:
                        if new_line.strip().startswith('#'):
                            continue
                        start = i
                        stop = i

                        data = []
                        for j, ln in enumerate(string_data[i:]):
                            stop = i + j

                            if ln.endswith('\\'):
                                ln = ln[:-1]
                            data += [ln.strip()]

                            if ln.endswith(';'):
                                break

                        skip_lines = [start, stop]
                        new_line = '\n'.join(data)

                    elif new_line is None and comment is None:
                        # /*
                        # * Aliases for StringPrep
                        # */
                        comment = ''
                        chained_comment = True

                        for comnt in string_data[i:]:
                            comnt = comnt.strip()

                            if not comnt.startswith('**/') and not comnt.startswith('*/') and comnt.startswith('*'):
                                comnt = comnt[1:].strip()

                            comment += ' ' + comnt

                            if '*/' in comnt:
                                break

                        new_line, comment = parse_comment(comment)

                    if new_line:
                        guid_line = parse_guid(indent, new_line.split('\n'))
                        if guid_line:
                            handle_preprocessor()
                            if comment:
                                print('\n' + comment)
                            print(guid_line)
                            continue

                        line = parse_dll(indent, new_line.split('\n'), found_dlls)
                        if line:
                            handle_preprocessor()
                            if comment:
                                comment = equalize_width(indent, comment)
                                print('\n' +comment)
                            print(line)
                            continue

                    if not new_line.strip() and comment:
                        comment = equalize_width(indent, comment)
                        handle_preprocessor()
                        print('\n' + comment)
                        continue

    for interface_data in interfaces:
        indent = ''
        methods = interface_data['methods']
        importer = Importer

        parse_interface(
            indent,
            methods,
            importer,
            interface_data,
            False
        )

    for interface_data in libraries:
        indent = ''
        methods = interface_data['methods']
        importer = Importer

        parse_interface(
            indent,
            methods,
            importer,
            interface_data,
            False
        )
        # elif line.startswith('#include') or line.startswith('# include'):
        #     parse_include(indent, line, os.path.split(file_path)[0])

    # print 'importer'
    # importer = Importer(path=output_path)
    # print 'comment'
    # comment = Comment(string_data, COMMENTS)
    # print 'guid'
    # guid = GUID(importer, string_data)
    # print 'interface'
    # interface = Interface(importer, guid, string_data, file_path, comment)
    # print 'includes'
    # includes = Includes(string_data)
    # print 'define'
    # define = Define(importer, string_data)
    # print 'enum'
    # enum = Enum(importer, string_data)
    # print 'structure'
    # structure = Structure(importer, string_data)
    # print 'union'
    # union = Union(importer, string_data)
    # print 'typedef'
    # typedef = Typedef(importer, string_data)
    #
    # if dll is not None:
    #     dll_string = dll
    #     from dll import Dll
    #     dll = Dll(dll_string, importer, string_data)
    #
    # lines = []
    #
    # print 'process interface'
    # lines += list(interface.process())
    # print 'process comment'
    # lines += list(comment.process(importer))
    # print 'process  includes'
    # lines += list(includes.process())
    # print 'process define'
    # lines += list(define.process())
    # print 'process enum'
    # lines += list(enum.process())
    # print 'process guid'
    # lines += list(guid.process())
    # print 'process structure'
    # lines += list(structure.process())
    # print 'process union'
    # lines += list(union.process())
    # print 'process typedef'
    # lines += list(typedef.process())
    #
    # if dll is not None:
    #     print 'process dll'
    #     lines += list(dll.process())
    #
    # all_set = []
    # allowed = importer.allowed
    # for cls in (interface, define, enum, guid, structure, union, typedef, dll):
    #     if cls is None:
    #         continue
    #
    #     for itm in cls.all:
    #         if not itm:
    #             continue
    #         itm = itm.split('(')[0].split(' ')[0].replace('def ', '').strip()
    #         if itm not in all_set and itm not in allowed:
    #             all_set += [itm]
    #
    # lines = sorted(lines)
    # lines = '\n'.join(line[1] for line in lines)
    #
    # lines += '\n\n__all__ = (\n'
    #
    # output = ['']
    #
    # for item in all_set:
    #     item = "'" + item + "', "
    #     for i, ln in enumerate(output[:]):
    #         if len(ln) + len(item) <= 75:
    #             ln += item
    #             output[i] = ln
    #             break
    #     else:
    #         output += [item]
    #
    # for ln in output:
    #     lines += '    ' + ln + '\n'
    #
    # lines += ')\n'
    #
    # imports = '\n\n'
    # print 'process importer'
    # for impt in importer.process():
    #     imports += impt
    #
    # imports += '\n\n'
    # return imports + lines


# this code converter is by no means complete and without error. it is
# designed to ease the amount of work that needs to be done. The output file
# still needs to be gone over and checked for consistency and accuracy.


# there are 2 files in this code builder that will need to copied over to
# the folder you are saving the API conversions to.data_types.py
# and guiddef_h.py.

# Enter the output path and filename here be sure to keep the filename the
# same and append _h to the filename

# a lot of the microsoft h files do not have a dll they are married to. but
# some do. as an example setupapi.h is what creates setupapi.dll if this is
# the case do not tack on the _h
# output_file = r'C:\Users\Administrator\Desktop\New folder (18)\pyWinAPI'# ks_h.py'

# enter the input filename here
input_file = r'C:\Stackless27\Lib\site-packages\pyWinAPI\km\wdm.h' # ks.h'
# COMMENTS = False
#
# # if there is a specific dll that is created fro an h file the name of that
# # dll needs to be entered here without the .dll extension
# load_dll = None
#
#
import sys
# from StringIO import StringIO
#
# log = StringIO()
#

if __name__ == '__main__':
    _stdout = sys.stdout
    # _stderr = sys.stderr
    #
    import threading

    print_lock = threading.Lock()

    output_file = input_file[:-2] + '_h.py'

    if os.path.exists(output_file):
        if raw_input("delete file " + output_file).lower() == 'n':
            sys.exit(0)


    class STDOut(object):
        line_buffer = []
        out_buffer = []

        def write(self, data):
            with print_lock:
                # _stdout.write(data)
                # _stdout.flush()
                try:
                    self.line_buffer += [data]
                    if len(self.line_buffer) == 3:
                        if (
                            self.line_buffer[0].strip().startswith('#') and
                            self.line_buffer[2].strip().startswith('#') and
                            not self.line_buffer[1].strip()
                        ):
                            self.line_buffer.pop(1)

                        self.out_buffer += [self.line_buffer.pop(0)]

                except ValueError:
                    pass

        def close(self):
            for line in self.line_buffer:
                self.out_buffer += [line]

            if interface_declarations:
                temp_buffer = '\n\n'.join(interface_declarations).split('\n')
                temp_buffer += ['', '']
            else:
                temp_buffer = []

            temp_buffer += '\n\n'.join(u_s_declarations).split('\n')
            if u_s_declarations:
                temp_buffer += ['', '']

            temp_buffer += ''.join(self.out_buffer).split('\n')

            # for item in temp_buffer:
            #     sys.stderr.write(repr(item) + '\n')

            out_buffer = []

            for line in temp_buffer:
                try:
                    back_2 = out_buffer[-2].strip()
                    back_1 = out_buffer[-1].strip()
                except IndexError:
                    out_buffer += [line]
                    continue

                if not line.strip() and not back_1 and not back_2:
                    continue

                if (
                    not line.strip() and
                    (
                        back_1.startswith('if') or
                        back_1.startswith('elif') or
                        back_1.startswith('else') or
                        back_1.startswith('#')
                    )
                ):
                    continue

                if line.strip().startswith('class '):
                    if back_1:
                        if (
                            back_1.startswith('if') or
                            back_1.startswith('elif') or
                            back_1.startswith('else') or
                            back_1.startswith('#')
                        ):
                            out_buffer += [line]
                        else:
                            out_buffer += ['', '', line]

                        continue

                    if back_2:
                        out_buffer += ['', line]
                        continue

                out_buffer += [line]

            with open(output_file, 'w') as f:
                f.write('import ctypes\n')
                f.write('from pyWinAPI import *\n')
                f.write('from pyWinAPI.shared.wtypes_h import *\n')
                f.write('from pyWinAPI.shared.winapifamily_h import *\n')
                f.write('from pyWinAPI.shared.sdkddkver_h import *\n')
                f.write('from pyWinAPI.shared.guiddef_h import *\n')
                f.write('\n'.join(out_buffer) + '\n')

        def __getattr__(self, item):
            if item in self.__dict__:
                return self.__dict__[item]
            with print_lock:
                return getattr(_stdout, item)


    sys.stdout = STDOut()
    gen_code(input_file)
    sys.stdout.close()

    write_functions()
    print_not_found()

#
# class STDErr(object):
#
#     def write(self, data):
#         with print_lock:
#             _stderr.write(data)
#             _stderr.flush()
#             log.write(data)
#
#     def __getattr__(self, item):
#         if item in self.__dict__:
#             return self.__dict__[item]
#         with print_lock:
#             return getattr(_stderr, item)
#


#
#
# if os.path.isdir(input_file):
#     sys.stderr = STDErr()
#     sys.stdout = STDOut()
#     files = os.listdir(input_file)
#     for f in files:
#         if f.endswith('.h'):
#             # if f in ('CertSrv.h', 'CompPkgSup.h', 'contentpartner.h', 'dwrite_3.h', 'icu.h'):
#             #     continue
#             o_file = os.path.join(output_file, f.lower().replace('.h', '_h.py'))
#             if os.path.exists(o_file):
#                 continue
#
#             l_file = o_file + '.log'
#             try:
#                 _stdout.write(f + '\n')
#                 _stdout.flush()
#                 code = gen_code(
#                     os.path.join(input_file, f),
#                     output=o_file,
#                     dll=load_dll
#                 )
#             except:
#                 import traceback
#                 traceback.print_exc()
#             else:
#                 with open(o_file, 'w') as fl:
#                     fl.write(code)
#
#             log.seek(0)
#             with open(l_file, 'w') as fl:
#                 fl.write(log.read())
#
#             log = StringIO()
# else:
#     o_file = os.path.join(output_file, os.path.split(input_file)[1].replace('.h', '_h.py'))
#     l_file = o_file + '.log'
#     _stdout.write(input_file + '\n')
#     _stdout.flush()
#     code = gen_code(
#         input_file,
#         output=o_file,
#         dll=load_dll
#     )
#     with open(o_file, 'w') as fl:
#         fl.write(code)
#
#     log.seek(0)
#
#     with open(l_file, 'w') as fl:
#         fl.write(log.read())
# if output_file is None:
#     print code
#
# else:
#     with open(output_file, 'w') as f:
#         f.write(code)




