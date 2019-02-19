from __future__ import print_function, absolute_import
import os
import re
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


lib_path = os.path.dirname(__file__)

if not lib_path:
    lib_path = os.getcwd()

lib_path = os.path.abspath(os.path.join(lib_path, '..'))


IMPORTS = {}


def enumerate_imports(p):
    mod_path = []

    head = p
    while head != lib_path:
        head, tail = os.path.split(head)
        mod_path.insert(0, tail.replace('.', '_'))

    mod_path.insert(0, 'pyWinAPI')

    files = os.listdir(p)
    for f in files:
        if f.endswith('.h'):
            f = f.lower()
            IMPORTS[f] = '.'.join(mod_path + [f.replace('.', '_')])
        elif os.path.isdir(os.path.join(p, f)):
            enumerate_imports(os.path.join(p, f))


enumerate_imports(lib_path)


from code_converter.includes import parse_include
from code_converter.enum import parse_enum
from code_converter.define import parse_define
from code_converter.comment import parse_comment, equalize_width
from code_converter.structure import parse_struct_union, u_s_declarations
from code_converter.interface import parse_interface, interface_declarations
from code_converter.dll import parse_dll, write_functions, print_not_found
from code_converter.guid import parse_guid
from code_converter.utils import process_param
from code_converter.preprocessor import parse_macro
from code_converter import preprocessor
from code_converter.declare_interface import parse_declare_interface


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
interface_template_1 = '''

{indent}class {cls_name}(comtypes.IUnknown):
{indent}    _case_insensitive_ = True
{indent}    _iid_ = None
{indent}    _idlflags_ = []

'''

interface_template_2 = '''

{indent}class {cls_name}({parent_cls}):
{indent}    _case_insensitive_ = True
{indent}    _iid_ = None
{indent}    _idlflags_ = []

'''

def convert(data):
    data = data.replace('__RPC_FAR ', '')
    data = data.replace('__RPC_unique_pointer ', '')
    data = data.replace('__RPC_USER ', '')
    data = re.sub(r" \-\> ", '.', data)
    data = re.sub(r"\-\> ", '.', data)
    data = re.sub(r" \-\>", '.', data)
    data = re.sub(r"\-\>", '.', data)
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
    data = re.sub(r"\(void\)", '(VOID)', data)
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
    # data = re.sub(r"(?! )\-(?! )", ' - ', data)
    data = re.sub(r"(?! )<=(?! )", ' <= ', data)
    data = re.sub(r"(?! )>=(?! )", ' >= ', data)
    data = re.sub(r"(?! )!=(?! )", ' != ', data)
    data = re.sub(r"(?! )<<(?! )", ' << ', data)
    data = re.sub(r"(?! )>>(?! )", ' >> ', data)
    data = re.sub(r"(?! )\|(?! )", ' | ', data)
    data = re.sub(r"(?!>?! )>(?!>?! )", ' > ', data)
    data = re.sub(r"(?!<?! )<(?!<?! )", ' < ', data)
    data = re.sub(r"> =", '>=', data)
    data = re.sub(r"< =", '<=', data)

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


INTERFACE_START = '''
def INTERFACE(name):
    return type(name, (comtypes.IUnknown,), {})


def STDMETHOD(name):

    def method_wrapper(restype, *args):
        if isinstance(restype, tuple):
            args = (restype,) + args
            restype = HRESULT

        argtypes = tuple(arg[0] for arg in args)
        argnames = list(arg[1] for arg in args)
        res = comtypes.STDMETHOD(restype, name, argtypes)
        return argnames, res

    return method_wrapper


def DECLARE_INTERFACE_(cls, super_cls):
    if super_cls != comtypes.IUnknown:
        bases = super_cls.__bases__
        cls.__bases__ = (
            (super_cls,) +
            tuple(base for base in cls.__bases__ if base not in bases)
        )

    def wrapper(*args):
        argnames = list(arg[0] for arg in args)
        _methods_ = list(arg[1] for arg in args)

        method_names = list(itm[1] for itm in _methods_)

        for i, method_name in enumerate(method_names):
            defaults = argnames[i]

            class MethodWrapper(object):

                def __init__(self, parent, name, keywords):
                    self.__parent = parent
                    self.__name__ = name
                    self.__keywords = keywords

                def __call__(self, *args, **kwargs):
                    args = list(args)
                    for j, keyword in enumerate(self.__keywords):
                        if keyword in kwargs:
                            args.insert(j, kwargs.pop(keyword))

                    getattr(self.__parent, '__com_' + self.__name__)(*args)


            method = MethodWrapper(cls, method_name, defaults)
            setattr(cls, method_name, method)

        cls._methods_ = _methods_

    return wrapper


'''

found_dlls = []
imports_to_follow = []
start_output = []


def gen_code(file_path=None, output='', string_data=None, dll=None):

    idl_file = os.path.splitext(file_path)[0] + '.idl'

    interfaces = []
    built_interfaces = {}
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
    steps = [[]]
    anon_struct_count = 0
    anon_union_count = 0
    union_struct_fwd_definitions = []
    tdef = False

    def check_state_step():
        step = steps[-1]

        if not isinstance(step, list):
            parse_macro('    ' * (len(steps) - 2), step.strip(), True)

            print('    ' * (len(steps) - 1) + 'pass')
            steps[len(steps) - 1] = step[-2]

    def handle_preprocessor(f_dlls=None):
        for j, step in enumerate(steps):
            if isinstance(step, list):
                continue

            if f_dlls is None:
                k_dlls = []
            else:
                k_dlls = f_dlls[:]

            if j:
                step_indent = '    ' * (j - 1)
                k_dlls += steps[j - 1][:]
            else:
                step_indent = ''

            parse_macro(step_indent, step.strip(), True)
            steps[j] = k_dlls[:]

        if f_dlls is not None:
            steps[-1] += list(fd for fd in f_dlls if fd not in steps[-1])

    if interfaces:
        print(
            'def annotation(value):\n'
            '    if \'_opt_\' in value:\n'
            '        return comtypes.defaultvalue(None)\n'
            '    else:\n'
            '        return None\n'
            '\n'
        )

    def combine_extended_lines(start, indt=None, marker=None, braces=None):
        end_index = start
        data = []
        comments = ''

        brace_count = 0
        if indt is None:
            indt = '    ' * (len(steps) - 1)

        cont_line = ''
        cont_comment = ''
        cont_indent = ''

        for data_index, data_line in enumerate(string_data[start:]):
            if not data_line.startswith(indt):
                data_line = indt + data_line.strip()

            data_line = data_line.replace(indt, '', 1)
            data_indent = ''

            for char in list(data_line):
                if char != ' ':
                    break
                data_indent += ' '

            end_index = start + data_index

            data_temp, data_comment = parse_comment(data_line)
            try:
                data_comment = data_comment.replace('#', '', 1).strip()
            except AttributeError:
                sys.stderr.write('COMBINE: ' + repr([data_line, data_temp, data_comment]) + '\n')
                continue

            data_temp = data_indent + data_temp.strip()

            if data_temp.endswith('\\'):
                if cont_line:
                    cont_line += ' ' + data_temp[:-1].strip()
                else:
                    cont_indent = data_indent
                    cont_line += data_temp[:-1].strip()

                if data_comment:
                    cont_comment += ' ' + data_comment.strip()

                continue
            else:
                if cont_line:
                    cont_line += ' ' + data_temp.strip()
                    new_data = cont_line

                    if data_comment:
                        cont_comment += ' ' + data_comment.strip()

                    if cont_comment:
                        data_comment = cont_comment.strip()

                    if marker is not None:
                        new_data = cont_indent + new_data

                    cont_line = ''
                    cont_indent = ''
                    cont_comment = ''

                elif marker is None:
                    new_data = indt + data_temp
                else:
                    new_data = data_indent + data_temp

            if braces is not None:
                brace_count += data_line.count(braces[0])
                brace_count -= data_line.count(braces[1])

            if marker is None and data_comment:
                comments += ' ' + data_comment.strip()

            elif data_comment:
                new_data += ' // ' + data_comment.strip()

            data += [new_data]

            if brace_count == 0:
                if marker is None:
                    break
                if data_temp.strip().endswith(marker):
                    break

        if marker is None and braces is None:
            result = ' '.join(data)
            if comments:
                result += ' // ' + comments.strip()
        else:
            result = '\n'.join(indt + lne for lne in data)

        return result, end_index

    skip_until = None
    print_newline = False
    print_skip = False

    for i, line in enumerate(string_data):
        if skip_until is not None:
            if i <= skip_until:
                continue

            skip_until = None

        if line.strip().startswith('extern "C" {'):
            continue

        if '#ifdef COBJMACROS' in line:
            skip_until = combine_extended_lines(i, marker='#endif')[1]
            continue

        if line.strip() == 'typedef':
            tdef = True
            continue

        indent = '    ' * (len(steps) - 1)

        if line.strip() == '//':
            if print_skip:
                print_skip = False
            else:
                print_skip = True
                print()
            continue

        comment_line, comment = parse_comment(line.strip())
        if not comment_line and comment:
            handle_preprocessor()
            comment = equalize_width(indent, comment)
            print('\n' + comment)
            continue

        if comment_line is None and comment is None:
            skip_until = i
            comments = []
            for j, d in enumerate(string_data[i:]):
                skip_until = i + j
                d = d.strip()
                if d.startswith('/**'):
                    d = d[3:]
                elif d.startswith('**/'):
                    d = d[1:]
                elif d.startswith('*') and not d.startswith('*/'):
                    d = d[1:]

                if '*/' in d:
                    d = d.replace('**/', '').replace('*/', '')
                    comments += [d]
                    break

                comments += [d]
            comment = equalize_width(indent, ' '.join(comments))
            print('\n' + comment)
            continue

        line = comment_line

        for item in ('ifndef', 'ifdef', 'elif', 'if', 'else', 'endif', 'define'):
            line = line.replace('# ' + item, '#' + item)

        for item in ('ifdef', 'ifndef', 'if'):
            if line.strip().startswith('#' + item):
                if line.strip().endswith('\\'):
                    line, skip_until = combine_extended_lines(i, indent)

                steps += [line]
                break
        else:
            for item in ('elif', 'else'):
                if line.strip().startswith('#' + item):
                    check_state_step()
                    if line.strip().endswith('\\'):
                        line, skip_until = combine_extended_lines(i, indent)
                    steps[len(steps) - 1] = line
                    break
            else:
                if line.strip().startswith('#endif'):
                    check_state_step()
                    if len(steps) > 1:
                        steps = steps[:-1]

                    parse_macro(
                        '    ' * (len(steps) - 1),
                        string_data[i].strip(),
                        True
                    )
                    continue

        line = line.replace('typedef _Struct_size_bytes_(Size) struct', 'typedef struct')
        if '__WRAPPED__' in line:
            line = line.replace(' __WRAPPED__', '').strip()
            if not line:
                continue
        line = line.strip()

        if line.startswith('LONG') and '=' in line:
            line = line.replace('LONG', '', 1)
            line = line.replace(';', '').strip()
            line = ' = '.join(item.strip() for item in line.split('=', 1))
            print(indent + line)
            continue

        if line.startswith('MIDL_INTERFACE'):
            handle_preprocessor()

            iface, skip_until = combine_extended_lines(i + 1, indent, ';', '{}')
            iface = iface.split('\n')
            line = line.replace('("', '(\n' + indent + '    "{')
            line = line.replace('")', '}"\n' + indent + ')').upper()

            cls_name = iface[0].split(':')[0].strip()
            interface_iid = indent + 'IID_' + cls_name + ' = ' + line + '\n'
            interface_iid += indent + cls_name + '._iid_ = IID_' + cls_name + '\n\n'

            cls_name, b_interface = parse_interface(indent, iface, Importer, cls_name, False)

            print(indent[:-4] + 'else:')
            print(interface_iid)
            print(b_interface)
            skip_until = combine_extended_lines(i, marker='#endif')[1]
            continue

        for interface_data in interfaces[:]:
            pattern1 = 'typedef interface {0}'.format(
                interface_data['cls_name']
            )

            pattern2 = '{0}Vtbl'.format(
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
                skip_until = i
                break

            if pattern2 in line:
                sys.stderr.write('PATTERN2: ' + pattern2 + ' ' + line + '\n')
                handle_preprocessor()

                if interface_data['cls_name'] in built_interfaces:
                    print(built_interfaces.pop(interface_data['cls_name']))

                else:
                    parse_interface(
                        indent,
                        interface_data['methods'],
                        Importer,
                        interface_data,
                        False
                    )
                interfaces.remove(interface_data)

                skip_until = combine_extended_lines(i, marker='#endif')[1]
            break

        else:
            for interface_cls_name in built_interfaces.keys():
                pattern = '{0}Vtbl'.format(
                    interface_cls_name
                )

                if pattern in line:
                    handle_preprocessor()
                    print(built_interfaces.pop(interface_cls_name))
                    skip_until = combine_extended_lines(i, marker='#endif')[1]
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
                    if line.strip().startswith('DECLARE_HANDLE'):
                        var_name = line.split('(', 1)[1].split(')', 1)[0]
                        print(indent + var_name + ' = DECLARE_HANDLE()')
                        continue

                    if line.strip().startswith('#define INTERFACE'):
                        if INTERFACE_START not in start_output:
                            start_output.append(INTERFACE_START)

                        interface_name = line.replace('#define INTERFACE', '')
                        interface_name = interface_name.strip().split(' ')[0]
                        print(indent + interface_name + " = INTERFACE('" + interface_name + "')")
                        continue

                    if line.strip().startswith('#define'):
                        define_line, skip_until = combine_extended_lines(i, indent)
                        handle_preprocessor()
                        if parse_define('    ' * (len(steps) - 1), define_line, Importer):
                            print_newline = True
                            continue
                        else:
                            skip_until = None
        if skip_until is not None:
            continue

        if line.strip().startswith('DECLARE_INTERFACE_'):
            if print_newline:
                print()
                print_newline = False

            declare_interface, skip_until = combine_extended_lines(i, indent, ';', '{}')
            declare_interface = list(
                di.replace(indent, '', 1) for di in declare_interface.split('\n')
            )
            parse_declare_interface(indent, declare_interface)
            continue

        if (
            (line.strip().startswith('typedef') and string_data[i + 1].strip().startswith('enum')) or
            line.startswith('enum') or
            line.startswith('typedef enum')
        ):
            if print_newline:
                print()
                print_newline = False

            enum, skip_until = combine_extended_lines(i, indent, ';')
            enum = list(
                el.replace(indent, '', 1) for el in enum.split('\n')
            )

            if tdef:
                enum[0] = enum[0].replace('enum', 'typedef enum', 1)
                tdef = False

            if 'typedef enum' not in enum[0] and 'typedef' in enum[0]:
                enum.pop(0)
                enum[0] = enum[0].replace('enum', 'typedef enum')

            if len(enum) > 1:
                if not enum[0].endswith('{'):
                    enum[0] += '{'
                    try:
                        enum[1] = enum[1].replace('{    ', '')
                    except IndexError:
                        sys.stderr.write(str(enum) + '\n')
                        raise

            else:
                enum = enum[0].strip()
                if enum.endswith(';'):
                    enum = enum.replace('typedef enum', '')
                    enum = enum.replace('enum', '').replace(';', '').strip()
                    attr_name, values = enum.split(' ', 1)
                    values = list(v.strip() for v in values.split(','))

                    for v in values:
                        if v == attr_name:
                            continue
                        key, v = process_param(v, attr_name)
                        handle_preprocessor()
                        print(indent + key + ' = ' + v)

                    print()
                    continue
                else:
                    sys.stderr.write(enum + '\n')
                    raise IndexError

            handle_preprocessor()
            parse_enum(indent, enum, namespace)
            continue

        if '_STORAGE_DEVICE_DESCRIPTOR' in line:
            print('# _STORAGE_DEVICE_DESCRIPTOR: ' + line)

        if (
            line.startswith('struct') or
            line.startswith('union') or
            line.startswith('typedef  struct') or
            line.startswith('typedef struct') or
            line.startswith('typedef union')
        ):
            if print_newline:
                print()
                print_newline = False

            struct, skip_until = combine_extended_lines(i, indent, ';', '{}')

            if tdef:
                if struct.strip().startswith('struct'):
                    struct = struct.replace('struct', 'typedef struct', 1)
                else:
                    struct = struct.replace('union', 'typedef union', 1)

                tdef = False

            handle_preprocessor()
            res = parse_struct_union(
                indent,
                struct,
                Importer,
                anon_struct_count,
                anon_union_count,
                union_struct_fwd_definitions,
                True
            )
            anon_struct_count, anon_union_count = res[:2]

            if len(res) == 3:
                skip_until = i + res[2]

            continue

        if line.startswith('typedef') or (tdef and line):
            handle_preprocessor()

            if line.startswith('typedef interface '):
                line = line.replace('typedef interface ', '').strip()
                try:
                    parent_cls, cls_name = line.split(' ')
                except ValueError:
                    line = line.replace(';', '').strip()
                    parent_cls = cls_name = line

                cls_name = cls_name.replace(';', '').strip()
                parent_cls = parent_cls.strip()
                if parent_cls == cls_name:
                    print(interface_template_1.format(indent=indent, cls_name=cls_name))
                else:
                    print(interface_template_2.format(indent=indent, cls_name=cls_name, parent_cls=parent_cls))
                continue

            typedef, skip_until = combine_extended_lines(i, indent, ';')
            cls_name = None
            callback = 'CALLBACK'
            ret_val = None
            params = []

            new_typedef = ''
            for itm in typedef.split('\n'):
                itm = parse_comment(itm)[0]
                if itm and itm.strip():
                    new_typedef += ' ' + itm.strip()

            typedef = new_typedef.replace('typedef', '').strip()

            brace_count = 1

            # # typedef BOOL (CALLBACK* LANGUAGEGROUP_ENUMPROCA)(LGRPID, LPSTR, LPSTR, DWORD, LONG_PTR);
            try:
                ret, func = typedef.split('(', 1)
            except ValueError:
                # typedef DWORD LGRPID;
                try:
                    value, key = typedef.replace(';', '').strip().split(' ')
                    key, value = process_param(key, value)
                    print(indent + key + ' = ' + value)
                    continue
                except ValueError:
                    print(indent + '# ' + 'TYPEDEF ERROR: 1' + typedef)
                    continue

            for i, char in enumerate(list(func)):
                if char == '(':
                    brace_count += 1
                if char == ')':
                    brace_count -= 1
                if not brace_count:
                    try:
                        if func[i + 1] == ';':
                            continue
                    except IndexError:
                        print(indent + '# ' + 'TYPEDEF ERROR 2: ' + typedef)
                    vals = func[i:]
                    func = func[:i]
                    cls_name = func.replace('*', '').strip().split(' ')
                    if len(cls_name) == 1:
                        cls_name = cls_name[0]
                    else:
                        callback = cls_name[-2]
                        cls_name = cls_name[-1]

                    ret_val = ret.strip()
                    break
            else:
                vals = func
                ret, func = ret.rsplit(' ', 1)
                ret_val = ret.strip()

                cls_name = func.strip().replace('*', '').split(' ')

                if len(cls_name) == 1:
                    cls_name = cls_name[0]
                else:
                    callback = cls_name[-2]
                    cls_name = cls_name[-1]

            vals = vals.strip()
            if vals.startswith('('):
                vals = vals[1:]

            vals = vals.replace(');', '')

            for val in vals.split(','):
                val = val.replace(')(', '').strip()
                val = val.split(' ')
                if len(val) == 1:
                    params += [val[0]]
                else:
                    val, key = val[-2:]
                    _, val = process_param(key, val)
                    params += [val]
            #
            # for typed in typedef.split('\n'):
            #     typed = parse_comment(typed)[0]
            #     typed = typed.replace('typedef', '').strip()
            #     typed = list(
            #         t.strip().replace('** ', '**').replace('* ', '*')
            #         for t in typed.split(',') if t.strip()
            #     )
            #     for lne in typed:
            #         if lne.endswith('('):
            #             ret_val, cls_name = lne.split('(', 1)
            #             ret_val = ret_val.split(' ')[-1].strip()
            #
            #             cls_name = list(
            #                 itm for itm in
            #                 cls_name.split(')', 1)[0].strip().replace('*', '').split(' ')
            #                 if itm
            #             )
            #             if not cls_name:
            #                 break
            #             if len(cls_name) == 1:
            #                 cls_name = cls_name[0]
            #             else:
            #                 callback = cls_name[-2]
            #                 cls_name = cls_name[-1]
            #
            #         else:
            #             if cls_name is None:
            #                 lne = list(
            #                     itm.strip() for itm in lne.split('(', 1)
            #                     if itm.strip()
            #                 )
            #
            #                 if len(lne) == 1:
            #                     lne = lne[0]
            #                     if lne.endswith(')'):
            #                         cls_name = list(
            #                             itm.strip() for itm in lne[:-1].split(' ') if itm.strip()
            #                         )
            #                         if len(cls_name) == 1:
            #                             cls_name = cls_name[0]
            #                         else:
            #                             callback = cls_name[-2]
            #                             cls_name = cls_name[-1]
            #
            #                     else:
            #                         ret_val = list(itm for itm in lne.split(' ') if itm)[-1]
            #                     continue
            #                 else:
            #                     ret_val, cls_name = lne[-2:]
            #                     ret_val = list(itm for itm in ret_val.split(' ') if itm)[-1]
            #
            #                     cls_name = list(
            #                         itm for itm in
            #                         cls_name.split(')', 1)[0].strip().replace('*', '').split(' ')
            #                         if itm
            #                     )
            #                     if len(cls_name) == 1:
            #                         cls_name = cls_name[0]
            #                     else:
            #                         callback = cls_name[-2]
            #                         cls_name = cls_name[-1]
            #
            #                     lne = lne[:-2]
            #                     if not lne:
            #                         continue
            #                     lne = ')'.join(lne)
            #             try:
            #                 param_type, param_name = lne.replace(')', '').split(' ')[-2:]
            #                 param_type = process_param(param_name, param_type)[1]
            #                 params += [param_type]
            #             except ValueError:
            #                 if lne.strip() == ');':
            #                     break
            #                 else:
            #                     if lne.count('(') != lne.count(')'):
            #                         continue
            #
            #                     lne = list(itm.strip() for itm in lne.split(',') if itm.strip())
            #                     for itm in lne:
            #                         itm = itm.split(' ')
            #                         if len(itm) == 1:
            #                             params += [itm[0]]
            #                         else:
            #                             value, key = itm[-2:]
            #                             _, value = process_param(key, value)
            #                             params += [value]
            #
            if cls_name is not None:
                tmpl = '{indent}{cls_name} = {callback}(\n'
                tmpl = tmpl.format(
                    indent=indent,
                    cls_name=cls_name,
                    callback=callback
                )

                tmpl += '{indent}    {ret_val},\n'.format(
                    indent=indent,
                    ret_val=ret_val
                )

                for param in params:
                    tmpl += '{indent}    {param},\n'.format(
                        indent=indent,
                        param=param
                    )
                tmpl += '{indent})'.format(indent=indent)
                comment = '\n'.join(indent + '# ' + lne.strip() for lne in typedef.split('\n'))
                print('\n' + comment + '\n')
                print(tmpl + '\n\n')
            else:
                typedef, comment = parse_comment(typedef)
                if comment:
                    print('\n' + indent + '# ' + comment[1:].strip())
                typedef = typedef.replace('typedef', '').replace(';', '').strip()
                try:
                    value, typedefs = typedef.split(' ', 1)
                    typedefs = list(td.strip() for td in typedefs.split(','))

                    for td in typedefs:
                        if td == value:
                            continue

                        td, new_value = process_param(td, value)
                        print(indent + td + ' = ' + new_value)
                except ValueError:

                    # typedef UCHAR ERROR_SEVERITY, *PERROR_SEVERITY;
                    print(indent + '# TYPEDEF ERROR:', typedef.split('\n'))

            #     if '(CALLBACK' in typedef:
            #         restype, callback = typedef.split('(CALLBACK', 1)
            #         call_type = 'CALLBACK'
            #     elif '( CALLBACK' in typedef:
            #         restype, callback = typedef.split('( CALLBACK', 1)
            #         call_type = 'CALLBACK'
            #
            #     elif '(WINAPI' in typedef:
            #         restype, callback = typedef.split('(WINAPI', 1)
            #         call_type = 'WINAPI'
            #
            #     elif '( WINAPI' in typedef:
            #         restype, callback = typedef.split('( WINAPI', 1)
            #         call_type = 'WINAPI'
            #
            #     elif '(NTAPI' in typedef:
            #         restype, callback = typedef.split('(NTAPI', 1)
            #         call_type = 'NTAPI'
            #
            #     elif '( NTAPI' in typedef:
            #         restype, callback = typedef.split('( NTAPI', 1)
            #         call_type = 'NTAPI'
            #     else:
            #         continue
            #
            #     restype = restype.strip()
            #
            #     name, params = callback.split('(', 1)
            #     name = name.replace('*', '').replace(')', '').strip()
            #
            #     params = list(
            #         param.strip() for param in params[:-1].split(',')
            #     )
            #     param_types = [restype]
            #
            #     for param in params:
            #         param = list(p for p in param.split(' ') if p)
            #         if not param:
            #             continue
            #         param_type, param_name = param[-2:]
            #         param = param[:-2]
            #         while param_type in ('*', '**'):
            #             param_name = param_type + param_name
            #             param_type = param[-1]
            #             param = param[:-1]
            #
            #         param_type = process_param(param_name, param_type)[1]
            #         param_types += [param_type]
            #
            #     original_lines = string_data[i: skip_until + 1]
            #     original_lines = list(
            #         indent + '# ' + ol.replace(indent, '', 1)
            #         for ol in original_lines
            #     )
            #
            #     print('\n' + '\n'.join(original_lines))
            #     print(
            #         '{0}{1} = {2}({3})'.format(
            #             indent,
            #             name,
            #             call_type,
            #             ', '.join(param_types)
            #         ) + '\n'
            #     )
            # else:
            #     try:
            #         value, var_names = typedef.split(' ', 1)
            #     except:
            #
            #         raise
            #
            #     var_names = list(
            #         v_name.strip() for v_name in var_names.split(',')
            #     )
            #
            #     while value.endswith('*'):
            #         value = value[:-1].strip()
            #         var_names[0] = '*' + var_names[0]
            #
            #     if comment:
            #         comment = equalize_width(indent, comment)
            #         print('\n' + comment)
            #
            #     for v_name in var_names:
            #         if v_name == value:
            #             continue
            #
            #         v_name, new_val = process_param(v_name, value)
            #         print(indent + v_name + ' = ' + new_val)
            continue

        tdef = False
        if line.startswith('#include') or line.startswith('# include'):
            tdef = False
            mod = line.replace('#include', '').replace('# include', '').strip()
            mod = mod.replace('<', '').replace('>', '').strip()
            mod = mod.replace('"', '').strip()
            mod = mod.split('/')
            mod = mod[-1].split('\\')
            mod = mod[-1].strip().lower()
            if mod in IMPORTS:
                mod = IMPORTS[mod]
            else:
                mod = mod.replace('.', '_')

            handle_preprocessor()
            if comment:
                comment = equalize_width(indent, comment)
                print('\n' + comment)

            print(indent + 'from {0} import * # NOQA'.format(mod))
            imports_to_follow.append(mod)
            continue

        if line.startswith('#'):
            continue

        if line:
            if 'OUR_GUID_ENTRY' in line or 'DEFINE_CODECAPI_GUID' in line:
                guid_line, skip_until = combine_extended_lines(i, indent, ')')
            else:
                guid_line, skip_until = combine_extended_lines(i, indent, ';')

            guid_line = parse_guid(indent, guid_line.split('\n'))
            if guid_line:
                handle_preprocessor()
                print(guid_line)
                continue

            dll_line, skip_until = combine_extended_lines(i, indent, ';')
            if isinstance(steps[-1], list):
                dlls = steps[-1][:]
            else:
                dlls = []

            dll_line = parse_dll(indent, dll_line.split('\n'), dlls)
            if dll_line:
                handle_preprocessor(dlls)
                print(dll_line)
                continue
            else:
                skip_until = None

        if comment:
            handle_preprocessor()
            comment = equalize_width(indent, comment)
            print(comment)
            continue
    #
    # for interface_data in interfaces:
    #     indent = ''
    #     methods = interface_data['methods']
    #     importer = Importer
    #
    #     parse_interface(
    #         indent,
    #         methods,
    #         importer,
    #         interface_data,
    #         False
    #     )
    #
    # for interface_data in libraries:
    #     indent = ''
    #     methods = interface_data['methods']
    #     importer = Importer
    #
    #     parse_interface(
    #         indent,
    #         methods,
    #         importer,
    #         interface_data,
    #         False
    #     )

# enter the input filename here
# input_file = r'C:\Stackless27\Lib\site-packages\pyWinAPI\um\spatialaudiometadata.h'
# input_file = r'C:\Users\Administrator\Desktop\New folder (6)\temp.h'
# input_file = r'C:\Users\Administrator\Desktop\New folder (16)\iTunesCOMInterface.h'
#r'C:\Stackless27\Lib\site-packages\pyWinAPI\shared\apiset.h'


output_folder = r'C:\Users\Administrator\Desktop\New folder (24)'
input_folder = r'C:\Stackless27\Lib\site-packages\pyWinAPI'
import sys


if __name__ == '__main__':
    _stdout = sys.stdout

    def run(input_file):
        import threading

        print_lock = threading.Lock()

        head, input_filename = os.path.split(input_file)

        output_folders = []
        output_file = [input_filename]

        while head != input_folder:
            head, temp_folder = os.path.split(head)
            output_folders.insert(0, temp_folder)

        new_output_folder = os.path.join(output_folder, *output_folders)
        if not os.path.exists(new_output_folder):
            os.makedirs(new_output_folder)

        output_file = os.path.join(new_output_folder, input_filename[:-2] + '_h.py')

        if os.path.exists(output_file):
            return
            if raw_input("delete file " + output_file).lower() == 'n':
                sys.exit(0)

        class STDOut(object):

            def __init__(self):
                self.line_buffer = []
                self.out_buffer = []

            def write(self, data):
                with print_lock:
                    # _stdout.write(data)
                    # _stdout.flush()
                    try:
                        sys.stderr.write(data)
                        sys.stderr.flush()
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

                temp_buffer = ''.join(self.out_buffer).split('\n')
                out_buffer = []

                class_dec_indent = ''

                open_brackets = 0

                for line in temp_buffer:

                    if (
                        not line.strip().startswith('if ') and
                        not line.strip().startswith('elif ') and
                        not line.strip().startswith('else:')
                    ):
                        for item in ('()', '{}', '[]'):
                            open_brackets += line.count(item[0])
                            open_brackets -= line.count(item[1])
                    else:
                        open_brackets = 0

                    if open_brackets and not line.strip():
                        continue

                    if line.strip() and class_dec_indent and not line.startswith(class_dec_indent):
                        class_dec_indent = ''

                    try:
                        back_2 = out_buffer[-2].strip()
                        back_1 = out_buffer[-1].strip()
                    except IndexError:
                        out_buffer += [line]
                        continue

                    if class_dec_indent:
                        if not line.strip() and not back_1:
                            continue
                    else:
                        if not line.strip() and not back_1 and not back_2:
                            continue

                    if back_2 == 'pass' and open_brackets == 1 and '_fields_ =' in line:
                        if line.strip():
                            out_buffer += ['', line]
                            continue

                    if (
                        not line.strip() and not back_1.startswith('# END IF') and
                        (
                            back_1.startswith('if') or
                            back_1.startswith('elif') or
                            back_1.startswith('else') or
                            back_1.startswith('#')
                        )
                    ):
                        continue

                    if not class_dec_indent:
                        if line.strip().endswith('= [') or line.strip().endswith('= ('):
                            class_dec_indent = '    ' * line.count('    ') + '    '

                    if line.strip().startswith('class '):
                        open_brackets = 0
                        class_dec_indent = '    ' * line.count('    ') + '    '

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

                new_defines = preprocessor.new_defines

                for i, macro in enumerate(new_defines):
                    new_defines[i] = macro + ' = None'

                if new_defines:
                    new_defines.append('')

                temp_buffer = new_defines

                if interface_declarations:
                    temp_buffer += '\n\n'.join(interface_declarations).split('\n')
                    temp_buffer += ['', '']

                temp_buffer += '\n\n'.join(u_s_declarations).split('\n')
                if u_s_declarations:
                    temp_buffer += ['', '']

                temp_buffer += out_buffer

                with open(output_file, 'w') as f:
                    f.write('import ctypes\n')
                    f.write('from pyWinAPI import *\n')
                    f.write('from pyWinAPI.shared.wtypes_h import *\n')
                    f.write('from pyWinAPI.shared.winapifamily_h import *\n')
                    f.write('from pyWinAPI.shared.sdkddkver_h import *\n')
                    f.write('from pyWinAPI.shared.guiddef_h import *\n\n\n')
                    f.write(''.join(start_output))
                    f.write('\n'.join(temp_buffer) + '\n')

            def __getattr__(self, item):
                if item in self.__dict__:
                    return self.__dict__[item]
                with print_lock:
                    return getattr(_stdout, item)


        sys.stdout = STDOut()
        try:
            gen_code(input_file)
            tb = ''
        except:
            import traceback
            tb = traceback.format_exc()

        sys.stdout.close()

        if tb:
            with open(output_file, 'a') as f:
                f.write('\n' + tb)

    run(r'C:\Stackless27\Lib\site-packages\pyWinAPI\shared\bdamedia.h')

    for import_to_follow in imports_to_follow:
        while import_to_follow in imports_to_follow:
            imports_to_follow.remove(import_to_follow)

        import_to_follow = import_to_follow.split('.')[1:]
        check_filename = os.path.join(input_folder, *import_to_follow) + '.py'
        if 'pyWinAPI.py' in check_filename:
            continue
        sys.stderr.write('FOLLOW IMPORT: ' + check_filename + '\n')
        if os.path.exists(check_filename):
            continue
        import_to_follow = list(itm.replace('_', '.') for itm in import_to_follow)
        import_to_follow = os.path.join(input_folder, *import_to_follow)

        del preprocessor.new_defines[:]
        del interface_declarations[:]
        del u_s_declarations[:]
        del start_output[:]
        sys.stdout = _stdout

        run(import_to_follow)

    write_functions()
    print_not_found()
