from __future__ import print_function, absolute_import
import os
import re
from code_converter.includes import parse_include
from code_converter.enum import parse_enum
from code_converter.define import parse_define
from code_converter.comment import parse_comment, equalize_width
from code_converter.structure import parse_struct_union, u_s_declarations
from code_converter.interface import parse_interface, interface_declarations
from code_converter.dll import parse_dll, write_functions, print_not_found
from code_converter.guid import parse_guid
from code_converter.utils import process_param
from code_converter import preprocessor

parse_macro = preprocessor.parse_macro


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


def convert(data):
    data = re.sub(r" unsigned short int ", ' USHORT ', data)
    data = re.sub(r"\nunsigned short int ", '\nUSHORT ', data)
    data = re.sub(r" signed short int ", ' SHORT ', data)
    data = re.sub(r"\nsigned short int ", '\nSHORT ', data)
    data = re.sub(r" unsigned short ", ' USHORT ', data)
    data = re.sub(r"\nunsigned short ", '\nUSHORT ', data)
    data = re.sub(r" signed short ", ' SHORT ', data)
    data = re.sub(r"\nsigned short ", '\nSHORT ', data)
    data = re.sub(r" short int ", ' SHORT ', data)
    data = re.sub(r"\nshort int ", '\nSHORT ', data)
    data = re.sub(r" short ", ' SHORT ', data)
    data = re.sub(r"\nshort ", '\nSHORT ', data)
    data = re.sub(r"\(short\) ", '(SHORT)', data)
    data = re.sub(r"\(short\( ", '(SHORT(', data)
    data = re.sub(r" boolean ", ' BOOLEAN ', data)
    data = re.sub(r"\nboolean ", '\nBOOLEAN ', data)
    data = re.sub(r"\(boolean\)", '(BOOLEAN)', data)
    data = re.sub(r"\( boolean \)", '(BOOLEAN)', data)
    data = re.sub(r"\( boolean", '(BOOLEAN', data)
    data = re.sub(r"\(boolean", '(BOOLEAN', data)
    data = re.sub(r" bool ", ' BOOL ', data)
    data = re.sub(r"\nbool ", '\nBOOL ', data)
    data = re.sub(r"\(bool\)", '(BOOL)', data)
    data = re.sub(r"\( bool \)", '(BOOL)', data)
    data = re.sub(r"\( bool", '(BOOL', data)
    data = re.sub(r"\(bool", '(BOOL', data)
    data = re.sub(r" float ", ' FLOAT ', data)
    data = re.sub(r"\nfloat ", '\nFLOAT ', data)
    data = re.sub(r"\(float\)", '(FLOAT)', data)
    data = re.sub(r"\( float \)", '(FLOAT)', data)
    data = re.sub(r"\( float", '(FLOAT', data)
    data = re.sub(r"\(float", '(FLOAT', data)
    data = re.sub(r" long double ", ' LONG ', data)
    data = re.sub(r"\nlong double ", '\nLONG ', data)
    data = re.sub(r"\(long double\)", '(LONG)', data)
    data = re.sub(r"\( long double \)", '(LONG)', data)
    data = re.sub(r"\( long double", '(LONG', data)
    data = re.sub(r"\(long double", '(LONG', data)
    data = re.sub(r" double ", ' DOUBLE ', data)
    data = re.sub(r"\ndouble ", '\nDOUBLE ', data)
    data = re.sub(r"\(double\)", '(DOUBLE)', data)
    data = re.sub(r"\( double \)", '(DOUBLE)', data)
    data = re.sub(r"\( double", '(DOUBLE', data)
    data = re.sub(r"\(double", '(DOUBLE', data)
    data = re.sub(r" unsigned char ", ' UCHAR ', data)
    data = re.sub(r"\nunsigned char ", '\nUCHAR ', data)
    data = re.sub(r"\(unsigned char\)", '(UCHAR)', data)
    data = re.sub(r"\( unsigned char \)", '(UCHAR)', data)
    data = re.sub(r"\( unsigned char", '(UCHAR', data)
    data = re.sub(r"\(unsigned char", '(UCHAR', data)
    data = re.sub(r" signed char ", ' CHAR ', data)
    data = re.sub(r"\nsigned char ", '\nCHAR ', data)
    data = re.sub(r"\(signed char\)", '(CHAR)', data)
    data = re.sub(r"\( signed char \)", '(CHAR)', data)
    data = re.sub(r"\( signed char", '(CHAR', data)
    data = re.sub(r"\(signed char", '(CHAR', data)
    data = re.sub(r" __wchar_t ", ' WCHAR ', data)
    data = re.sub(r"\n__wchar_t ", '\nWCHAR ', data)
    data = re.sub(r"\(__wchar_t\)", '(WCHAR)', data)
    data = re.sub(r"\( __wchar_t \)", '(WCHAR)', data)
    data = re.sub(r"\( __wchar_t", '(WCHAR', data)
    data = re.sub(r"\(__wchar_t", '(WCHAR', data)
    data = re.sub(r" wchar_t ", ' WCHAR ', data)
    data = re.sub(r"\nwchar_t ", '\nWCHAR ', data)
    data = re.sub(r"\(wchar_t\)", '(WCHAR)', data)
    data = re.sub(r"\( wchar_t \)", '(WCHAR)', data)
    data = re.sub(r"\( wchar_t", '(WCHAR', data)
    data = re.sub(r"\(wchar_t", '(WCHAR', data)
    data = re.sub(r" char ", ' CHAR ', data)
    data = re.sub(r"\nchar ", '\nCHAR ', data)
    data = re.sub(r"\(char\)", '(CHAR)', data)
    data = re.sub(r"\( char \)", '(CHAR)', data)
    data = re.sub(r"\( char", '(CHAR', data)
    data = re.sub(r"\(char", '(CHAR', data)
    data = re.sub(r" unsigned long long int ", ' ULONGLONG ', data)
    data = re.sub(r"\nunsigned long long int ", '\nULONGLONG ', data)
    data = re.sub(r" signed long long int ", ' LONGLONG ', data)
    data = re.sub(r"\nsigned long long int ", '\nLONGLONG ', data)
    data = re.sub(r" unsigned long long ", ' ULONGLONG ', data)
    data = re.sub(r"\nunsigned long long ", '\nULONGLONG ', data)
    data = re.sub(r" signed long long ", ' LONGLONG ', data)
    data = re.sub(r"\nsigned long long ", '\nLONGLONG ', data)
    data = re.sub(r" long long int ", ' LONGLONG ', data)
    data = re.sub(r"\nlong long int ", '\nLONGLONG ', data)
    data = re.sub(r" long long ", ' LONGLONG ', data)
    data = re.sub(r"\nlong long ", '\nLONGLONG ', data)
    data = re.sub(r" unsigned long int ", ' ULONG ', data)
    data = re.sub(r"\nunsigned long int ", '\nULONG ', data)
    data = re.sub(r" signed long int ", ' LONG ', data)
    data = re.sub(r"\nsigned long int ", '\nLONG ', data)
    data = re.sub(r" unsigned long ", ' ULONG ', data)
    data = re.sub(r"\nunsigned long ", '\nULONG ', data)
    data = re.sub(r" signed long ", ' LONG ', data)
    data = re.sub(r"\nsigned long ", '\nLONG ', data)
    data = re.sub(r" long int ", ' ULONG ', data)
    data = re.sub(r"\nlong int ", '\nULONG ', data)
    data = re.sub(r" long ", ' LONG ', data)
    data = re.sub(r"\nlong ", '\nLONG ', data)
    data = re.sub(r" unsigned int ", ' UINT ', data)
    data = re.sub(r"\nunsigned int ", '\nUINT ', data)
    data = re.sub(r" signed int ", ' INT ', data)
    data = re.sub(r"\nsigned int ", '\nINT ', data)
    data = re.sub(r" signed ", ' INT ', data)
    data = re.sub(r"\nsigned ", '\nINT ', data)
    data = re.sub(r" unsigned ", ' UINT ', data)
    data = re.sub(r"\nunsigned ", '\nUINT ', data)
    data = re.sub(r" __INT64 ", ' INT64 ', data)
    data = re.sub(r"\n__INT64 ", '\nINT64 ', data)
    data = re.sub(r"\(__INT64\)", '(INT64)', data)
    data = re.sub(r"\( __INT64 \)", '(INT64)', data)
    data = re.sub(r"\( __INT64", '(INT64', data)
    data = re.sub(r"\(__INT64", '(INT64', data)
    data = re.sub(r" __int8 ", ' INT8 ', data)
    data = re.sub(r"\n__int8 ", '\nINT8 ', data)
    data = re.sub(r"\(__int8\)", '(INT8)', data)
    data = re.sub(r"\( __int8 \)", '(INT8)', data)
    data = re.sub(r"\( __int8", '(INT8', data)
    data = re.sub(r"\(__int8", '(INT8', data)
    data = re.sub(r" __int16 ", ' CHAR ', data)
    data = re.sub(r"\n__int16 ", '\nCHAR ', data)
    data = re.sub(r"\(__int16\)", '(CHAR)', data)
    data = re.sub(r"\( __int16 \)", '(CHAR)', data)
    data = re.sub(r"\( __int16", '(CHAR', data)
    data = re.sub(r"\(__int16", '(CHAR', data)
    data = re.sub(r" __int32 ", ' INT32 ', data)
    data = re.sub(r"\n__int32 ", '\nINT32 ', data)
    data = re.sub(r"\(__int32\)", '(INT32)', data)
    data = re.sub(r"\( __int32 \)", '(INT32)', data)
    data = re.sub(r"\( __int32", '(INT32', data)
    data = re.sub(r"\(__int32", '(INT32', data)
    data = re.sub(r" __int64 ", ' INT64 ', data)
    data = re.sub(r"\nchar ", '\nINT64 ', data)
    data = re.sub(r"\(__int64\)", '(INT64)', data)
    data = re.sub(r"\( __int64 \)", '(INT64)', data)
    data = re.sub(r"\( __int64", '(INT64', data)
    data = re.sub(r"\(__int64", '(INT64', data)
    data = re.sub(r" int ", ' INT ', data)
    data = re.sub(r"\nint ", '\nINT ', data)
    data = re.sub(r"\(int\) ", '(INT)', data)
    data = re.sub(r"\(int\( ", '(INT(', data)
    data = re.sub(r" void ", ' VOID ', data)
    data = re.sub(r"\nvoid ", '\nVOID ', data)
    data = re.sub(r"\(void)", '(VOID)', data)
    data = re.sub(r"\( void \)", '(VOID)', data)
    data = re.sub(r"\( void", '(VOID', data)
    data = re.sub(r"\(void", '(VOID', data)
    data = re.sub(r"sizeof", '(ctypes.sizeof', data)
    data = re.sub(r"memmove", '(ctypes.memmove', data)
    data = re.sub(r"memset", '(ctypes.memset', data)
    data = re.sub(r" const ", ' ', data)
    data = re.sub(r"\nconst ", '\n', data)
    data = re.sub(r"\(const", '(', data)
    data = re.sub(r"\( const", '(', data)
    data = re.sub(r"\[const", '[', data)
    data = re.sub(r"\[ const", '[', data)
    data = re.sub(r"__export", '', data)
    data = re.sub(r"__override", '', data)
    data = re.sub(r"__WRAPPED__", '', data)
    data = re.sub(r"_Struct_size_bytes_\(Size\)", '', data)
    data = re.sub(r"_Union_size_bytes_\(Size\)", '', data)
    data = re.sub(r"\[ \]", '[]', data)
    data = re.sub(r"\[  \]", '[]', data)
    data = re.sub(r" \|\| ", ' or ', data)
    data = re.sub(r"(?! )\|\|(?! )", ' or ', data)
    data = re.sub(r" && ", ' and ', data)
    data = re.sub(r"(?! )&&(?! )", ' and ', data)
    data = re.sub(r"!(?!=)", 'not ', data)
    data = re.sub(r"(?! )==(?! )", ' == ', data)
    data = re.sub(r"(?! )\+(?! )", ' + ', data)
    data = re.sub(r"(?! )\-(?! )", ' - ', data)
    data = re.sub(r"(?! )<=(?! )", ' <= ', data)
    data = re.sub(r"(?! )>=(?! )", ' >= ', data)
    data = re.sub(r"(?! )!=(?! )", ' != ', data)
    data = re.sub(r"(?! )<<(?! )", ' << ', data)
    data = re.sub(r"(?! )>>(?! )", ' >> ', data)
    data = re.sub(r"(?! )\|(?! )", ' | ', data)
    data = re.sub(r"(?! )(?!>)>(?!>)(?! )", ' > ', data)
    data = re.sub(r"(?! )(?!<)<(?!<)(?! )", ' < ', data)
    data = re.sub(r"(?! )&(?! )", ' & ', data)
    data = re.sub(r"&lt;", '<', data)
    data = re.sub(r"&gt;", '>', data)

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
        print(
            'def annotation(value):\n'
            '    if \'_opt_\' in value:\n'
            '        return comtypes.defaultvalue(None)\n'
            '    else:\n'
            '        return None\n'
            '\n'
        )

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

        line, comment = parse_comment(line.strip())

        if line is None and comment is None:
            start = i
            stop = i
            comments = []
            for j, d in enumerate(string_data[i:]):
                stop = i + j
                comments += [d.strip()]
                if '*/' in d:
                    break

            skip_lines = [start, stop]
            comment = parse_comment(' '.join(comments))[1]
            comment = equalize_width(indent, comment)
            print('\n' + comment)
            continue

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

                if line.strip() and line.strip().endswith(';'):
                    guid_line = parse_guid(indent, [line])
                    if guid_line:
                        handle_preprocessor()
                        if comment:
                            print(comment)
                        print(guid_line)
                        continue

                if line.strip().startswith('enum') or line.strip().startswith('typedef enum'):
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
                        line = line.replace('typedef', '').strip()
                        line = line.replace(';', '').strip()
                        value, var_names = line.split(' ', 1)

                        var_names = list(
                            v_name.strip() for v_name in var_names.split(',')
                        )

                        while value.endswith('*'):
                            value = value[:-1].strip()
                            var_names[0] = '*' + var_names[0]

                        if comment:
                            comment = equalize_width(indent, comment)
                            print('\n' + comment)

                        for v_name in var_names:
                            v_name, new_val = process_param(v_name, value)
                            print(indent + v_name + ' = ' + new_val)

                        continue

                    if line.strip().startswith('#include'):
                        line = line.replace('#include', '').strip()
                        line = line.replace('<', '').replace('>', '')
                        line = line.replace('"', '').strip()
                        line = line.replace('.h', '_h')
                        line = line.replace('/', '.').replace('\\', '.')
                        handle_preprocessor()
                        if comment:
                            comment = equalize_width(indent, comment)
                            print('\n' + comment)

                        print(indent + 'from {0} import * # NOQA'.format(line))
                        continue

                    tdef = False

                    if line and line.strip() and ';' not in line:
                        if line.strip().startswith('#'):
                            continue
                        start = i
                        stop = i

                        data = []
                        found_guid = False
                        for j, ln in enumerate(string_data[i:]):
                            stop = i + j

                            if ln.endswith('\\'):
                                ln = ln[:-1]
                            data += [ln.strip()]

                            if ln.endswith(';'):
                                break

                            if 'OUR_GUID_ENTRY' in ln or 'DEFINE_CODECAPI_GUID' in ln:
                                found_guid = True

                            if found_guid is True and ')' in ln:
                                break

                        if found_guid:
                            guid_line = parse_guid(indent, data)
                            if guid_line:
                                handle_preprocessor()
                                skip_lines = [start, stop]
                                if comment:
                                    comment = equalize_width(indent, comment)
                                    print('\n' + comment)
                                print(guid_line)
                                continue

                        line = '\n'.join(data)

                    elif line is None and comment is None:
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

                        line, comment = parse_comment(comment)
                        line = line.strip()

                    if line:
                        guid_line = parse_guid(indent, line.split('\n'))
                        if guid_line:
                            handle_preprocessor()
                            if comment:
                                comment = equalize_width(indent, comment)
                                print('\n' + comment)
                            print(guid_line)
                            continue

                        dll_line = parse_dll(indent, line.split('\n'), found_dlls)
                        if dll_line:
                            handle_preprocessor()
                            if comment:
                                comment = equalize_width(indent, comment)
                                print('\n' + comment)
                            print(dll_line)
                            continue

                    if comment:
                        handle_preprocessor()
                        comment = equalize_width(indent, comment)
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

# enter the input filename here
input_file = r'C:\Stackless27\Lib\site-packages\pyWinAPI\um\propvarutil.h' # ks.h'

import sys

if __name__ == '__main__':
    _stdout = sys.stdout

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


