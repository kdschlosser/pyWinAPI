# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function, absolute_import
from code_converter.utils import process_param, split_strip
from code_converter.comment import parse_comment, equalize_width

CLS_TEMPLATE = '''
class {cls_name}({parent_cls}):
    _case_insensitive_ = True
    _iid_ = {iid_name}
    _idlflags_ = [{idl_flags}]
'''


CLS_TEMPLATE_EXTENSION = '''    _methods_ = [
{methods}
    ]'''



METHOD_PARAM_EXTENSION = ''',
{method_params}
        ),'''


METHOD_EXTENSION = '''
        ),'''


GUID_TEMPLATE = '''{iid_name} = IID(
    '{iid}'
)

'''


LIBRARY_TEMPLATE = '''class {library_name}(object):
    name = '{library_name}'
    _reg_typelib_ = ({iid_name}, {version}, 0)


'''


CO_CLASS_TEMPLATE = '''class {co_class_name}(comtypes.CoClass):
    _reg_clsid_ = {co_clsid_name}
    _idlflags_ = []
    _reg_typelib_ = ({iid_name}, {version}, 0)
    _com_interfaces_ = [
{com_interfaces}
    ]


'''


'''
class Library(object):
    u'MM Device API 1.0 Type Library'
    name = u'MMDeviceAPILib'
    _reg_typelib_ = ('{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}', 1, 0)

class MMDeviceEnumerator(CoClass):
    _reg_clsid_ = GUID('{BCDE0395-E52F-467C-8E3D-C4579291692E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}', 1, 0)
    
    
class IMMDeviceEnumerator(stdole.IUnknown):
    _case_insensitive_ = True
    u'MMDevice Enumerator Interface'
    _iid_ = GUID('{A95664D2-9614-4F35-A746-DE8DB63617E6}')
    _idlflags_ = ['nonextensible']
    _com_interfaces_ = [IMMDeviceEnumerator]

'''

TEMPLATE_METHOD = '''{indent}{comment}
{indent}    COMMETHOD(
{indent}        {method_options},
{indent}        {method_data_type},
{indent}        '{method_name}',{params}
{indent}    ),
'''

TEMPLATE_INTERFACE = '''{indent}{iid_name} = {iid}
{indent}
{indent}
{indent}class {cls_name}({parent_cls}):{helpstring}
{indent}    _case_insensitive_ = True
{indent}    _idlflags_ = {idl_flags}
{indent}    _iid_ = {iid_name}
'''

TEMPLATE_COCLASS = '''{indent}{iid_name} = {iid}
{indent}
{indent}
{indent}class {cls_name}(comtypes.CoClass):{helpstring}
{indent}    _case_insensitive_ = True
{indent}    _idlflags_ = {idl_flags}
{indent}    _reg_clsid_ = {iid_name}
{indent}    _reg_typelib_ = {reg_typelib}
{indent}    _com_interfaces_ = {com_interfaces}
'''

TEMPLATE_LIBRARY = '''{indent}{iid_name} = {iid}
{indent}
{indent}
{indent}class {cls_name}(object):{helpstring}
{indent}    _case_insensitive_ = True
{indent}    _reg_typelib_ = {reg_typelib}
{indent}    name = '{cls_name}'
'''


TEMPLATE_METHODS = '''{indent}{cls_name}._methods_ = [
{methods}{indent}]
'''


TEMPLATE_PARAM1 = '''
{indent}        ({param_direction}, {param_data_type}, '{param_name}'),'''

TEMPLATE_PARAM2 = '''
{indent}        (
{indent}            {param_direction},
{indent}            {param_data_type},
{indent}           '{param_name}'
{indent}        ),'''

TEMPLATE_HELPSTRING = '''\n{indent}    """{indent}\n    {helpstring}\n{indent}    """'''


interface_declarations = []

class Options(dict):

    def __init__(self, options):
        dict.__init__(self)
        self.options = options.replace('in,', '"in",').replace('in]', '"in"]')
        for item in ('length_is', 'size_is'):
            if item in self.options:
                new_options = ''
                while item + '(' in self.options:

                    pattern = self.options[:self.options.find(item + '(') + len(item) + 1]
                    new_options += pattern
                    self.options = self.options.replace(pattern, '', 1)
                    brace_count = 1
                    for i, char in enumerate(list(self.options)):
                        if char == ')':
                            brace_count -= 1
                        if char == '(':
                            brace_count += 1
                        if brace_count == 0:
                            break
                    else:
                        continue

                    self.options = self.options[i + 1:]
                    new_options += ')'

                self.options = new_options + self.options
        self.found_options = []

    def helpstring(self, value):
        return 'comtypes.helpstring({0})'.format(repr(value))

    def id(self, value):
        return 'comtypes.dispid({0})'.format(repr(value))

    def annotation(self, value):
        values = []

        def check_options(itm):
            if itm + ',' not in self.options and itm + ']' not in self.options:
                values.append(itm)

        if '_Inout' in value:
            check_options('in')
            check_options('out')

        elif '_Out' in value:
            check_options('out')

        elif '_In' in value:
            check_options('in')

        if '_Ret' in value:
            values += ['retval']

        if '_opt_' in values:
            if 'defaultvalue(' not in self.options:
                values += ['defaultvalue(None)']

        values += ['annotation({0}),'.format(repr(value))]
        return values
        # return values

    def defaultvalue(self, value):
        return 'defaultvalue({0})'.format(repr(value))

    def size_is(self):
        return 'size_is'

    def length_is(self):
        return 'length_is'

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if hasattr(self, item):
            return getattr(self, item)

        class Wrapper:
            def __call__(self, _):
                return ''

            def __str__(self):
                if item == 'string':
                    return ''

                return repr(item)

            def __repr__(self):
                if item == 'string':
                    return ''
                return repr(item)


        return Wrapper()

    def __str__(self):

        # namespace = dict(
        #     list((key, value) for key, value in Options.__dict__.items() if not key.startswith('_'))
        # )
        #
        # namespacedict(
        #     helpstring=self.helpstring,
        #     id=id,
        #     annotation=self.annotation,
        #     defaultvalue=self.defaultvalue,
        #     size_is=self.size_is,
        #     length_is=self.length_is,
        # )

        # self.__dict__.update(
        #
        # )
        # #

        # namespace.update(self.__dict__)

        exec('found_options = ' + self.options + '\n', self)
        found_options = []
        for item in self.found_options:
            if isinstance(item, list):
                found_options += item
            else:
                found_options += [item]

        options = dict(
            list((item, 1) for item in found_options)
        )

        size_is = options.pop('size_is', 0)
        length_is = options.pop('length_is', 0)

        options = options.keys()[:]

        if size_is and length_is:
            if "in" not in options:
                options += ["in"]

            if "out" not in options:
                options += ["out"]

        res = repr(list(item for item in options if item))\

        res = res.replace('"a', 'a').replace(',"', '')
        res = res.replace(")'", ')').replace(')"', ')')
        res = res.replace("'comtypes", 'comtypes')
        res = res.replace('"comtypes', 'comtypes')
        res = res.replace(',,', ',')
        res = res.replace('[, ', '[')

        for itm in ('in', 'out', 'retval'):
            while res.count("'{0}'".format(itm)):
                if (
                    res.count("'{0}',".format(itm)) == 1 and
                    res.count("'{0}']".format(itm)) == 0
                ):
                    break
                elif res.count("'{0}',".format(itm)) > 1:
                    res = res.replace("'{0}',".format(itm), '', 1)
                else:
                    break

        return res


def get_help_string(indent, data):
    help_string = data.pop('helpstring')
    if help_string:
        help_string = TEMPLATE_HELPSTRING.format(
            indent=indent,
            helpstring=help_string
        )
    return help_string


def parse_keys(in_data):
    b_count = 0
    res = ''
    for char in list(in_data):
        if char == '[':
            b_count += 1
        elif char == ']':
            b_count -= 1

        res += char

        if b_count == 0:
            return res


def parse_options(line):
    options = parse_keys(line)
    return options, Options(options)


def parse_interface(indent, methods, importer, interface_data, dec):
    if 'declared' in interface_data and dec:
        dec = False

    if dec is True:
        help_string = get_help_string(indent, interface_data)
        interface_data['iid'] = interface_data['iid'].format(indent=indent)
        interface_data['declared'] = True

        if interface_data['co_class']:
            co_class = TEMPLATE_COCLASS.format(
                indent='',
                helpstring=help_string,
                **interface_data
            )
            interface_declarations.append(co_class)

        elif interface_data['library']:
            library = TEMPLATE_LIBRARY.format(
                indent='',
                helpstring=help_string,
                **interface_data
            )

            interface_declarations.append(library)
        else:
            interface = TEMPLATE_INTERFACE.format(
                indent='',
                helpstring=help_string,
                **interface_data
            )

            interface_declarations.append(interface)
        return

    if interface_data['co_class'] or interface_data['library']:
        return

    cls_name = interface_data['cls_name']

    chained_comment = False
    chained_method = False
    found_methods = []
    for line_num, method in enumerate(methods):

        if chained_method:
            if ';' in method:
                chained_method = False
            continue

        if chained_comment:
            if '*/' in method:
                chained_comment = False

            continue

        method, comment = parse_comment(method)

        if method is None and comment is None:
            comment = ''
            chained_comment = True
            for comnt in methods[line_num:]:
                comnt = comnt.strip()

                if (
                    not comnt.startswith('**/') and
                    not comnt.startswith('*/') and
                    comnt.startswith('*')
                ):
                    comnt = comnt[1:].strip()

                comment += ' ' + comnt
                if '*/' in comnt:
                    break
            method, new_comment = parse_comment(comment)

        if method and not method.endswith(';'):
            chained_method = True

            method = ''
            comment = ''
            for meth in methods[line_num:]:
                meth = meth.strip()
                meth, new_comment = parse_comment(meth)
                comment += ' ' + new_comment
                method += ' ' + meth

                if meth.endswith('\\'):
                    method = method[:-1]

                if ';' in meth:
                    break

        comment = equalize_width(indent + '    ', comment)

        if comment:
            if '\n' in comment:
                found_methods += ['\n']
                split_comment = comment.split('\n')
                for comnt in split_comment[:-1]:
                    found_methods += [comnt + '\n']

                found_methods += [split_comment[-1]]
            else:
                try:
                    if found_methods[-1].strip().endswith('\n'):
                        found_methods += [comment.rstrip() + '\n']
                    else:
                        found_methods += ['\n' + comment.rstrip()]
                except IndexError:
                    found_methods += [comment.rstrip() + '\n']

            comment = ''

        if not method:
            continue

        if method.strip().startswith('['):
            pattern, method_options = parse_options(method.strip())
            method = method.replace(pattern, '')
        else:
            method_options = Options('[]')

        # void APOProcess([in, annotation("_In_")] UINT32 u32NumInputConnections, [in, annotation("_In_")] APO_CONNECTION_PROPERTY** ppInputConnections, [in, annotation("_In_")] UINT32 u32NumOutputConnections, [in, out, annotation("_Inout_")] APO_CONNECTION_PROPERTY** ppOutputConnections);',
        try:
            method_name, temp_params = method.split('(', 1)
        except ValueError:
            continue

        method_name = method_name.strip()
        try:
            method_data_type, method_name = method_name.split(' ')
        except ValueError:
            continue

        method_name = method_name.strip()
        method_data_type = method_data_type.strip()
        temp_params = temp_params.strip()[:-2]

        found_params = []
        # [in, annotation("_In_")] UINT32 u32NumInputConnections, [in, annotation("_In_")] APO_CONNECTION_PROPERTY** ppInputConnections, [in, annotation("_In_")] UINT32 u32NumOutputConnections, [in, out, annotation("_Inout_")] APO_CONNECTION_PROPERTY** ppOutputConnections',

        while temp_params:
            if temp_params.startswith('['):
                pattern, param_direction = parse_options(temp_params)
                temp_params = temp_params.replace(pattern, '')
            else:
                param_direction = Options('[]')

            # UINT32 u32NumInputConnections,
            # [in, annotation("_In_")] APO_CONNECTION_PROPERTY** ppInputConnections, [in, annotation("_In_")] UINT32 u32NumOutputConnections, [in, out, annotation("_Inout_")] APO_CONNECTION_PROPERTY** ppOutputConnections'

            if ',' in temp_params:
                param, temp_params = split_strip(temp_params, ',')
            else:
                param = temp_params
                temp_params = ''

            try:
                param_data_type, param_name = split_strip(param, ' ')
            except ValueError:
                continue

            param_name, param_data_type = process_param(
                param_name,
                param_data_type
            )
            template = TEMPLATE_PARAM1.format(
                indent=indent,
                param_direction=param_direction,
                param_data_type=param_data_type,
                param_name=param_name,
                comment=comment
            )
            if len(template) > 79:
                template = TEMPLATE_PARAM2.format(
                    indent=indent,
                    param_direction=param_direction,
                    param_data_type=param_data_type,
                    param_name=param_name,
                    comment=comment
                )

            found_params += [template]

        found_methods += [
            TEMPLATE_METHOD.format(
                indent=indent,
                method_options=method_options,
                method_data_type=method_data_type,
                method_name=method_name,
                params=''.join(found_params) if found_params else '',
                comment=comment
            )
        ]

    template = TEMPLATE_METHODS.format(
        indent=indent,
        cls_name=cls_name,
        methods=''.join(found_methods),
    )
    if not found_methods:
        template = template.split('[')[0]
        template += '[]\n\n'

    print(template)

#
# class Interface(object):
#
#     def __init__(self, importer, guid, data, path, comments):
#         self.comments = comments
#         self.declared_interfaces = DeclareInterface(importer, guid, data, path, comments)
#         self.importer = importer
#         self.guid = guid
#         self.lines = {}
#         self.comtypes = None
#         self.guid_importer = None
#         self._all = set()
#         self.interace_declerations = {}
#         self.libraries = {}
#         self.path = path
#         found_library = None
#         ifndef = 0
#         saved_lines = []
#
#         start = None
#         dec_start = None
#         print "\n\n-- INTERACE -------------------------------------------\n\n"
#         for i, line in enumerate(data[:]):
#             if '_LIBRARY_DEFINED__' in line and 'ifndef' in line:
#                 library = line[:line.find('_LIBRARY_DEFINED__')]
#                 library = library.split('_')[-1]
#                 found_library = dict(
#                     library_name=library,
#                     co_class_iid=None,
#                     iid_name=None,
#                     co_clsid_name=None,
#                 )
#                 ifndef += 1
#                 print '\n\n{0} FOUND LIBRARY {1} {0}\n\n'.format('#' * 10, library)
#                 continue
#             if ifndef > 0:
#                 ifndef += line.count('ifndef')
#                 ifndef -= line.count('endif')
#
#                 if 'DECLSPEC_UUID' in line:
#                     start = i
#
#                 if start > 0:
#                     saved_lines += [line]
#                     if line.strip().endswith(')'):
#                         start = 0
#                         if 'DECLSPEC_UUID' in saved_lines[0]:
#                             found_library['co_class_iid'] = (
#                                 ' '.join(ln.strip() for ln in saved_lines)[:-1]
#                             )
#                         saved_lines = []
#
#                 if line.startswith('EXTERN_C'):
#                     line = line.strip().replace(';', '')
#                     if found_library['library_name'] in line:
#                         iid_name = line.split(' ')[-1]
#                         found_library['iid_name'] = iid_name
#                     elif 'CLSID' in line:
#                         clsid_name = line.split(' ')[-1]
#                         found_library['co_clsid_name'] = clsid_name
#
#                 if ifndef == 0:
#                     self.libraries[i] = found_library
#                     found_library = None
#
#                 continue
#
#             if line.startswith('typedef INTerface'):
#                 dec_start = i
#
#             if dec_start is not None and line.rstrip().endswith(';'):
#                 self.interace_declerations[dec_start] = (
#                     data[dec_start:i + 1]
#                 )
#                 dec_start = None
#
#             if line.strip().startswith('MIDL_INTERFACE'):
#                 start = i
#                 if self.comtypes is None:
#                     self.comtypes = importer.add_importer('comtypes')
#
#             if start is not None and line.rstrip().endswith('};'):
#                 self.lines[start] = data[start - 1:i + 1]
#         for value in sorted(self.interace_declerations.values()):
#             print value
#
#     @property
#     def all(self):
#         new_all = set()
#         for item in self._all:
#             new_all.add(item)
#
#         for item in self.declared_interfaces.all:
#             new_all.add(item)
#
#         return new_all
#
#
#     def process(self):
#         for line_num, line in self.declared_interfaces.process():
#             yield line_num, line
#
#         libraries = {}
#
#         for line_num, data in self.libraries.items():
#             library_name = data['library_name']
#             co_class_iid = data['co_class_iid']
#             iid_name = data['iid_name']
#             co_clsid_name = data['co_clsid_name']
#             library_iid = ''
#             version = '1'
#             cls_name = ''
#             interfaces = []
#
#             if co_class_iid is None:
#                 co_class_iid = ''
#                 co_class_name = ''
#                 co_clsid_name = ''
#             else:
#                 co_class_iid, co_class_name = co_class_iid.replace('   ', ' ').split(' ')[-2:]
#                 print co_class_iid, library_name
#                 co_class_iid = co_class_iid.split('(')
#                 print co_class_iid, library_name
#                 co_class_iid[0] += '('
#                 co_class_iid[1] = "    '{" + co_class_iid[1][:-1].replace('"', '') + "}'"
#                 co_class_iid += [')']
#                 co_class_iid = co_clsid_name + ' = ' + '\n'.join(co_class_iid)
#
#             try:
#                 with open(self.path[:-1] + 'idl') as f:
#                     idl = f.read().split('\n')
#             except IOError:
#                 continue
#
#             meta_data = None
#
#             for i, line in enumerate(idl):
#                 if line.startswith('library') and library_name in line:
#
#                     meta_data_start = i
#                     while not idl[meta_data_start].startswith('['):
#                         meta_data_start -= 1
#
#                     meta_data = idl[meta_data_start:i - 1]
#                     continue
#
#                 if meta_data is not None:
#                     if 'interface' in line and line.strip().endswith(';'):
#                         if not cls_name:
#                             cls_name = line.rstrip().split(' ')[-1][:-1]
#
#                             for ln in meta_data:
#                                 ln = ln.strip()
#                                 if ln.startswith('uuid'):
#                                     ln = ln.replace('uuid(', '').replace(')', '')
#                                     library_iid = GUID_TEMPLATE.format(
#                                         iid_name=iid_name,
#                                         iid='{' + ln.replace(',', '').strip() + '}'
#                                     )
#                                 if ln.startswith('version'):
#                                     version = ln.replace('version(', '')
#                                     version = version.split('.')[0]
#                         interfaces += [line.rstrip().split(' ')[-1][:-1]]
#
#                     if line.startswith('};'):
#
#                         library_template = LIBRARY_TEMPLATE.format(
#                             library_name=library_name,
#                             iid_name=iid_name,
#                             version=version
#                         )
#                         if co_class_name:
#                             co_class_template = CO_CLASS_TEMPLATE.format(
#                                 co_class_name=co_class_name,
#                                 co_clsid_name=co_clsid_name,
#                                 iid_name=iid_name,
#                                 version=version,
#                                 com_interfaces='\n'.join(
#                                     ' ' * 8 + iface + ',' for iface in interfaces
#                                 )
#                             )
#                             self._all.add(co_clsid_name)
#                             self._all.add(co_class_name)
#                         else:
#                             co_class_template = ''
#
#                         output = [
#                             co_class_iid + '\n\n',
#                             library_iid,
#                             library_template,
#                             co_class_template,
#                         ]
#
#                         libraries[cls_name] = output
#                         self._all.add(iid_name)
#                         self._all.add(library_name)
#
#                         meta_data = None
#
#         declerations = []
#
#         for line_num, decleration in list(self.interace_declerations.items())[:]:
#             decleration = ' '.join(d.strip() for d in decleration)
#             decleration = decleration.rsplit(' ', 1)[1].replace(';', '').strip()
#             declerations += [decleration]
#             self.interace_declerations[decleration] = line_num
#
#         if self.lines:
#             line_num = sorted(self.lines.keys())[0] - 1
#             yield line_num, 'COMMETHOD = comtypes.COMMETHOD\n\n'
#
#         for line_num, lines in self.lines.items()[:]:
#             output = ''
#             guid_output = ''
#             guid = None
#             guid_name = None
#             cls_name = 'NO_CLASS_NAME_FOUND'
#             parent_cls = 'NO_PARENT_CLASS_NAME_FOUND'
#             methods = []
#
#             method = []
#
#             for c_ln, line in enumerate(lines[1:]):
#                 line = line.split(':')
#
#                 if len(line) == 2 and 'public' in line[1]:
#                     _, parent_cls = line[1].strip().split(' ')
#                     cls_name = line[0].strip()
#
#                     parent_cls = parent_cls.replace(
#                         'IUnknown',
#                         'comtypes.IUnknown'
#                     )
#
#                     if guid_name is None:
#                         guid_name = 'IID_' + cls_name
#                         guid_output = GUID_TEMPLATE.format(
#                             iid_name=guid_name,
#                             iid=guid
#                         )
#                         self.importer.add_importer('guiddef_h').add('IID')
#                 else:
#                     line = line[0].strip()
#
#                     if line.startswith('MIDL_INTERFACE'):
#                         guid = line.replace('MIDL_INTERFACE(', '')
#                         guid = guid.replace('"', '').replace(')', '')
#                         guid = '{' + guid.strip() + '}'
#
#                         try:
#                             guid_name = self.guid[guid]
#                         except KeyError:
#                             pass
#                         except NameError:
#                             if self.guid_importer is None:
#                                 self.guid_importer = self.importer.add_importer('guiddef_h')
#                                 self.guid_importer.add(guid)
#
#                     if line.startswith('virtual'):
#                         method = [line]
#                     elif method:
#                         method += [line]
#                         if line.endswith(';'):
#                             saved_lines = method[:]
#
#                             if '*/' in method[0]:
#                                 method[0] = method[0][method[0].find('*/') + 3:]
#
#                             method = ' '.join(m.strip() for m in method)
#                             method = method.replace('virtual', '').strip()
#                             ret_data_type, method = method.split('(', 1)
#                             ret_data_type = ret_data_type.split(' ')
#                             method_name = ret_data_type[-1]
#                             ret_data_type = ret_data_type[0].upper()
#                             method = method.rsplit(')', 1)[0].strip()
#                             method_params = []
#
#                             for param in method.split(','):
#                                 param = param.strip()
#                                 param_type = []
#
#                                 if '[in]' in param.lower():
#                                     param_type += ['in']
#                                 if '[out]' in param.lower():
#                                     param_type += ['out']
#                                 if '[retval]' in param.lower():
#                                     param_type += ['retval']
#
#                                 param = param.split('*/')
#                                 if len(param) == 2:
#                                     param = param[1:]
#                                 param = param[0].strip()
#                                 try:
#                                     param = param.split(' ')
#                                     try:
#                                         param_data_type, param_name = param[-2:]
#                                     except ValueError:
#                                         continue
#
#                                     if not param_data_type.strip():
#                                         print '************** ERROR param_data_type', saved_lines, param
#                                         import time
#                                         time.sleep(0.1)
#                                         continue
#
#                                     for rem in (
#                                         '_Outptr_result_maybenull_',
#                                         '_In_',
#                                         '_Out_writes_all_',
#                                         '__RPC__',
#                                         '_Out_'
#                                     ):
#                                         if rem in param_data_type:
#                                             param_data_type.replace(rem, '').strip()
#                                             if not param_data_type:
#                                                 raise ValueError
#
#                                 except ValueError:
#                                     print saved_lines
#                                     import time
#                                     time.sleep(1)
#                                     raise
#
#                                 param_data_type = (
#                                     param_data_type.strip().replace(
#                                         'IUnknown',
#                                         'comtypes.IUnknown'
#                                     )
#                                 )
#
#                                 param_name = param_name.strip()
#
#                                 self.importer.add(param_data_type)
#
#                                 while param_name.startswith('*'):
#                                     param_data_type = (
#                                         'POINTER(' + param_data_type + ')'
#                                     )
#                                     param_name = param_name[1:]
#                                     self.importer.add('POINTER')
#
#                                 method_params += [
#                                     PARAM_TEMPLATE.format(
#                                         param_type=str(param_type),
#                                         param_data_type=param_data_type,
#                                         param_name=param_name
#                                     )
#                                 ]
#
#                             template = METHOD_TEMPLATE[:-1]
#                             self.importer.add(ret_data_type)
#                             if method_params:
#                                 template += METHOD_PARAM_EXTENSION
#                                 method = template.format(
#                                     ret_data_type=ret_data_type,
#                                     method_name=method_name,
#                                     method_params='\n'.join(method_params)
#                                 )
#                             else:
#                                 template += METHOD_EXTENSION
#                                 method = template.format(
#                                     ret_data_type=ret_data_type,
#                                     method_name=method_name
#                                 )
#                             methods += [method]
#                             method = []
#
#             self._all.add(cls_name)
#
#             if cls_name in self.importer.allowed:
#                 self.importer.add(cls_name)
#                 continue
#
#             cls_template = CLS_TEMPLATE
#
#             if cls_name in libraries:
#                 idl_flags = "'nonextensible'"
#             else:
#                 idl_flags = ''
#
#             if cls_name in declerations:
#                 cls_template = cls_template.format(
#                     parent_cls=parent_cls,
#                     cls_name=cls_name,
#                     iid_name=guid_name,
#                     idl_flags=idl_flags
#                 )
#                 yield self.interace_declerations[cls_name], guid_output + cls_template + '\n'
#
#                 if methods:
#                     new_methods = ''
#                     for ln in '\n'.join(methods).split('\n'):
#                         new_methods += ln[4:] + '\n'
#
#                     method_template = DEC_TEMPLATE_EXTENSION.format(
#                         cls_name=cls_name,
#                         methods=new_methods
#                     )
#                     yield line_num, method_template + '\n\n'
#             else:
#                 if methods:
#                     cls_template += CLS_TEMPLATE_EXTENSION
#                     cls_template = cls_template.format(
#                         parent_cls=parent_cls,
#                         cls_name=cls_name,
#                         iid_name=guid_name,
#                         idl_flags=idl_flags,
#                         methods='\n'.join(methods)
#                     )
#                 else:
#                     cls_template = cls_template.format(
#                         parent_cls=parent_cls,
#                         cls_name=cls_name,
#                         idl_flags=idl_flags,
#                         iid_name=guid_name,
#                     )
#
#                 yield line_num, guid_output + output + cls_template + '\n\n'
#
#             if cls_name in libraries:
#                 if cls_name in declerations:
#                     line_num = self.interace_declerations[cls_name]
#                 yield (
#                     line_num + 1,
#                     ''.join(libraries[cls_name])
#                 )
#
#
# class DeclareInterface(object):
#
#     def __init__(self, importer, guid, data, path, comments):
#         self.comments = comments
#         self.lines = {}
#         self.guid = guid
#         self.path = path
#         self.importer = importer
#         self.forward_declerations = {}
#         self.all = set()
#
#         lines = []
#         start = None
#         brace_count = 0
#
#         print "\n\n-- DECLARE INTERACE -----------------------------------\n\n"
#
#         for i, line in enumerate(data[:]):
#             if line.startswith('#define INTERFACE') and line.endswith(';'):
#                 forward = line.split(' ', 2)[2][:-1]
#                 self.forward_declerations[forward] = i
#                 continue
#
#             if line.startswith('DECLARE_INTERFACE_'):
#                 start = i
#             if start is not None:
#                 lines += [line]
#                 brace_count += line.count('{')
#                 brace_count -= line.count('}')
#                 if '};' in line and brace_count == 0:
#                     self.lines[start] = lines[:]
#                     print lines
#                     lines = []
#                     start = None
#
#     def process(self):
#         # DECLARE_INTERFACE_(IMetaDataDispenser, IUnknown)
#         # {
#         #     STDMETHOD(DefineScope)(                 // Return code.
#         #         REFCLSID    rclsid,                 // [in] What version to create.
#         #         DWORD       dwCreateFlags,          // [in] Flags on the create.
#         #         REFIID      riid,                   // [in] The interface desired.
#         #         IUnknown    **ppIUnk) PURE;         // [out] Return interface on success.
#         #
#         #     STDMETHOD(OpenScope)(                   // Return code.
#         #         LPCWSTR     szScope,                // [in] The scope to open.
#         #         DWORD       dwOpenFlags,            // [in] Open mode flags.
#         #         REFIID      riid,                   // [in] The interface desired.
#         #         IUnknown    **ppIUnk) PURE;         // [out] Return interface on success.
#         #
# # STDMETHOD(OpenScopeOnMemory)( LPCVOID     pData, ULONG       cbData, DWORD       dwOpenFlags, REFIID      riid, IUnknown    **ppIUnk) PURE;
#         # };
#         for line_num, lines in self.lines.items():
#             cls_name = None
#             parent_cls = None
#             methods = []
#             method_lines = []
#             start_method = None
#
#             for i, line in enumerate(lines[:]):
#                 if cls_name is None:
#                     cls_name, parent_cls = line.split('(', 1)[1].split(')')[0].split(',', 1)
#                     cls_name = cls_name.strip()
#                     parent_cls = parent_cls.strip().replace('IUnknown', 'comtypes.IUnknown')
#                 else:
#                     if line.strip().startswith('STDMETHOD'):
#                         start_method = i
#                     if start_method is not None:
#
#                         if '//' in line:
#                             comment = line[line.find('//'):]
#                             line = line.replace(comment, '')
#                         else:
#                             comment = ''
#
#                         method_lines += [[line.strip(), comment]]
#                         if line.strip().endswith(';'):
#                             methods += [method_lines[:]]
#                             method_lines = []
#                             start_method = None
#
#             method_output = []
#
#             for method_lines in methods:
#                 print cls_name, method_lines
#                 method_name = None
#                 method_params = []
#                 self.importer.add('HRESULT')
#                 ret_data_type = 'HRESULT'
#
#                 for line, comment in method_lines:
#                     if line.startswith('STDMETHOD_'):
#                         ret_data_type = 'VOID'
#                         line = line.split('_(', 1)
#                         if len(line) == 2:
#                             method_name, line = line[1].split(')', 1)
#                             ret_data_type, method_name = method_name.split(',', 1)
#                             ret_data_type = ret_data_type.strip()
#                             method_name = method_name.strip()
#                             line = line.strip()
#                         else:
#                             line = line[0]
#                             method_name = ''
#
#                     if line.startswith('STDMETHOD'):
#                         line = line.split('(', 1)
#                         if len(line) == 2:
#                             method_name, line = line[1].split(')', 1)
#                             method_name = method_name.strip()
#                             line = line.strip()
#                         else:
#                             line = line[0]
#                             method_name = ''
#
#                     if method_name is not None:
#                         if not method_name:
#                             method_name, line = line.split(')', 1)
#                             if ret_data_type == 'VOID':
#                                 ret_data_type, method_name = method_name.split(',', 1)
#                                 ret_data_type = ret_data_type.strip()
#                             method_name = method_name.strip()
#                             line = line.replace('(', '', 1)
#
#                         if line.endswith(';'):
#                             line = line.rsplit(')', 1)[0].strip()
#
#                         if '_Out_' in line or '_In_' in line:
#                             line = line.split(')', 1)
#                             if len(line) == 1:
#                                 continue
#                             line = line[1]
#
#                         if not line.strip() or line.strip() == '(':
#                             continue
#
#                         params = line.split(',')
#                         for param in params:
#                             param = param.strip()
#                             if not param:
#                                 continue
#                             try:
#                                 param_data_type, param_name = param.rsplit(' ', 1)
#                             except ValueError:
#                                 import time
#                                 print '************* DECLARE INTERFACE PARAM ERROR:', repr(param)
#                                 time.sleep(0.1)
#                                 continue
#
#                             param_data_type = param_data_type.strip().rsplit(' ', 1)
#                             if len(param_data_type) == 1:
#                                 param_data_type = param_data_type[0].strip()
#                             else:
#                                 param_data_type = param_data_type[1].strip()
#
#                             if 'IUnknown' in param_data_type:
#                                 param_data_type = param_data_type.replace('IUnknown', 'comtypes.IUnknown')
#                             else:
#                                 self.importer.add(param_data_type)
#
#                             param_name = param_name.strip().replace(',', '')
#                             if '[' in param_name:
#                                 param_name, array_count = param_name.split('[', 1)
#                                 array_count = array_count.split(']', 1)[0].strip()
#                                 if not array_count:
#                                     array_count = '0'
#                                 param_name = param_name.strip()
#                             else:
#                                 array_count = None
#
#                             if array_count is not None:
#                                 param_data_type += ' * ' + array_count
#
#                             while param_data_type.endswith('*'):
#                                 param_name = '*' + param_name
#                                 param_data_type = param_data_type[:-1]
#
#                             param_data_type = param_data_type.replace('(', '').strip()
#
#                             while param_name.startswith('*'):
#                                 param_data_type = 'POINTER(' + param_data_type + ')'
#                                 self.importer.add('POINTER')
#                                 param_name = param_name[1:]
#
#                             param_type = []
#                             if '[in]' in comment.lower():
#                                 param_type += ['in']
#                             if '[out]' in comment.lower():
#                                 param_type += ['out']
#                             if '[out|in]' in comment.lower():
#                                 param_type += ['out', 'in']
#                             if '[in|out]' in comment.lower():
#                                 param_type += ['in', 'out']
#                             if '[retval]' in comment.lower():
#                                 param_type += ['retval']
#
#                             if not param_type:
#                                 param_type += ['in']
#
#                             param = PARAM_TEMPLATE.format(
#                                 param_type=param_type,
#                                 param_data_type=param_data_type,
#                                 param_name=param_name
#                             )
#                             if comment:
#                                 param += comment.replace('//', ' # ')
#
#                             method_params += [param]
#
#                 template = METHOD_TEMPLATE.format(
#                     ret_data_type=ret_data_type,
#                     method_name=method_name
#                 )
#                 if method_params:
#                     template += METHOD_PARAM_EXTENSION.format(
#                         method_params='\n'.join(method_params)
#                     )
#                 else:
#                     template += METHOD_EXTENSION
#
#                 method_output += [template]
#
#             if cls_name is not None:
#                 iid_name = 'IID_' + cls_name
#                 try:
#                     self.guid[iid_name]
#                 except KeyError:
#                     yield line_num - 1, GUID_TEMPLATE.format(iid_name=iid_name, iid="'{}'")
#
#                 template = CLS_TEMPLATE.format(
#                     cls_name=cls_name,
#                     parent_cls=parent_cls,
#                     iid_name=iid_name,
#                     idl_flags=''
#                 )
#                 if cls_name in self.forward_declerations:
#                     yield self.forward_declerations[cls_name], template
#                     if method_output:
#                         yield line_num, DEC_TEMPLATE_EXTENSION.format(
#                             cls_name=cls_name,
#                             methods='\n'.join(method_output)
#                         )
#                 else:
#                     if method_output:
#                         template += CLS_TEMPLATE_EXTENSION.format(methods='\n'.join(method_output))
#                     yield line_num, template
#                 self.all.add(cls_name)
#
#
#
#
