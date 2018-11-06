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


from code_converter.utils import process_param, process_hex
from code_converter.comment import equalize_width, parse_comment
from code_converter.preprocessor import parse_macro


# ******************* Forward declarations

TEMPLATE_DECLARATION = '''{indent}class {cls_name}({parent_cls}):
{indent}    pass'''

TEMPLATE_DECLARATION_FIELDS_START = '''{indent}{cls_name}._fields_ = ['''
TEMPLATE_DECLARATION_FIELDS_END = '''{indent}]'''
TEMPLATE_DECLARATION_FIELD = '''{indent}    ('{field_name}', {field_data_type}),{comment}'''
TEMPLATE_DECLARATION_FIELD_BIT = '''{indent}    ('{field_name}', {field_data_type}, {bit}),'''

TEMPLATE_DECLARATION_ANONYMOUS_START = '''{indent}{cls_name}._anonymous_ = ('''
TEMPLATE_DECLARATION_ANONYMOUS_END = '''{indent})'''
TEMPLATE_DECLARATION_ANONYMOUS = '''{indent}    '{anonymous}','''


TEMPLATE_DECLARATION_SUBSTRUCTURE = '''{indent}{cls_name}.{child_cls} = {child_cls}'''
#
#
# # *********************** normal struct
#
# TEMPLATE_STRUCT = '''{indent}class {cls_name}({parent_cls}):'''
#
# TEMPLATE_FIELDS_START = '''{indent}    _fields_ = ['''
# TEMPLATE_FIELDS_END = '''{indent}    ]'''
# TEMPLATE_FIELD = '''{indent}        ('{field_name}', {field_data_type}),'''
# TEMPLATE_FIELD_BIT = '''{indent}        ('{field_name}', {field_data_type}, {bit}),'''
#
# TEMPLATE_ANONYMOUS_START = '''{indent}    _anonymous_ = ('''
# TEMPLATE_ANONYMOUS_END = '''{indent}    )'''
# TEMPLATE_ANONYMOUS = '''{indent}        '{anonymous}','''
#
# TEMPLATE_ADDONS_NONE = '''{indent}    pass'''
#
#
#
# TEMPLATE_SUBCLASS_NO_FIELDS = '''
# {indent}class {cls_name}({parent_cls}):
# {indent}    pass
# '''
#
# TEMPLATE_NO_FIELDS = '''
# {indent}class {cls_name}(ctypes.Structure):
# {indent}    pass
#
# '''
#
# TEMPLATE = '''
# {indent}class {cls_name}(ctypes.Structure):
# {indent}    _fields_ = [
# {fields}
# {indent}    ]
#
#
# '''
#
# TEMPLATE_ANONYMOUS = '''
# {indent}class {cls_name}(ctypes.Structure):
# {sub_structures}
# {indent}    _anonymous_ = ({anonymous})
# {indent}    _fields_ = [
# {fields}
# {indent}    ]
#
#
# '''
#
# TEMPLATE_SUBSTRUCTURES = '''
# {indent}class {cls_name}(ctypes.Structure):
# {sub_structures}
# {indent}    _fields_ = [
# {fields}
# {indent}    ]
#
#
# '''
#
# FIELD_TEMPLATE = '''{indent}        ('{field_name}', {field_data_type}),'''

'''
    if forward_dec:
        
        # TEMPLATE_DECLARATION_STRUCT.format(
        #     indent=indent,
        #     cls_name=cls_name,
        #     parent_cls=parent_cls
        # )
        struct_template = TEMPLATE_DECLARATION_STRUCT
            
        # TEMPLATE_DECLARATION_FIELDS_START.format(
        #     indent=indent,
        #     cls_name=cls_name
        # )
        field_start_template = TEMPLATE_DECLARATION_FIELDS_START

        # TEMPLATE_DECLARATION_FIELDS_END.format(
        #     indent=indent
        # )
        field_end_template = TEMPLATE_DECLARATION_FIELDS_END

        # TEMPLATE_DECLARATION_FIELD.format(
        #     indent=indent,
        #     field_name=field_name,
        #     field_data_type=field_data_type
        # )
        field_template = TEMPLATE_DECLARATION_FIELD

        # TEMPLATE_DECLARATION_FIELD_BIT.format(
        #     indent=indent,
        #     field_name=field_name,
        #     field_data_type=field_data_type,
        #     bit=bit
        # )
        field_bit_template = TEMPLATE_DECLARATION_FIELD_BIT

        # TEMPLATE_DECLARATION_ANONYMOUS_START.format(
        #     indent=indent,
        #     cls_name=cls_name
        # )
        anonymous_start_template = TEMPLATE_DECLARATION_ANONYMOUS_START

        # TEMPLATE_DECLARATION_ANONYMOUS_END.format(
        #     indent=indent
        # )
        anonymous_end_template = TEMPLATE_DECLARATION_ANONYMOUS_END

        # TEMPLATE_DECLARATION_ANONYMOUS.format(
        #     indent=indent,
        #     anonymous=anonymous
        # )
        anonymous_template = TEMPLATE_DECLARATION_ANONYMOUS

        # TEMPLATE_DECLARATION_SUBSTRUCTURE.format(
        #     indent=indent,
        #     cls_name=cls_name,
        #     sub_name=sub_name
        # )
    else:

        # TEMPLATE_STRUCT.format(
        #     indent=indent,
        #     cls_name=cls_name,
        #     parent_cls=parent_cls
        # )
        struct_template = TEMPLATE_STRUCT

        # TEMPLATE_FIELDS_START.format(
        #     indent=indent
        # )
        field_start_template = TEMPLATE_FIELDS_START

        # TEMPLATE_FIELDS_END.format(
        #     indent=indent
        # )
        field_end_template = TEMPLATE_FIELDS_END
        
        # TEMPLATE_FIELD.format(
        #     indent=indent,
        #     field_name=field_name,
        #     field_data_type=field_data_type
        # )
        field_template = TEMPLATE_FIELD

        # TEMPLATE_FIELD_BIT.format(
        #     indent=indent,
        #     field_name=field_name,
        #     field_data_type=field_data_type,
        #     bit=bit
        # )
        field_bit_template = TEMPLATE_FIELD_BIT

        # TEMPLATE_ANONYMOUS_START.format(
        #     indent=indent
        # )
        anonymous_start_template = TEMPLATE_ANONYMOUS_START

        # TEMPLATE_ANONYMOUS_END.format(
        #     indent=indent
        # )
        anonymous_end_template = TEMPLATE_ANONYMOUS_END

        # TEMPLATE_ANONYMOUS.format(
        #     indent=indent,
        #     anonymous=anonymous
        # )
        anonymous_template = TEMPLATE_ANONYMOUS


        # TEMPLATE_ADDONS_NONE.format(indent=indent)
'''


def parse_struct_union(
    indent,
    data,
    importer,
    struct_count,
    union_count,
    declarations
):

    lines = data.split('\n')

    for i, line in enumerate(lines):
        if '_Struct_size_bytes_' in line:
            l1, l2 = line.split('_Struct_size_bytes_(', 1)
            l2 = l2.split(')', 1)[1]
            line = l1 + l2
            lines[i] = line

        if '_Union_size_bytes_' in line:
            l1, l2 = line.split('_Union_size_bytes_(', 1)
            l2 = l2.split(')', 1)[1]
            line = l1 + l2
            lines[i] = line

    if len(lines) == 1:
        lines = lines[0].split(' ')
        attr_name = lines[-1].replace(';', '').strip()
        value = lines[-2].strip()

        attr_name, value = process_param(attr_name, value)
        try:
            print(indent + attr_name + ' = ' + value + '\n\n')
        except TypeError:
            return struct_count, union_count
        return struct_count, union_count

    if 'struct' not in lines[0] or 'union' not in lines[0]:
        lines[0] += ' ' + lines.pop(1).lstrip()

    start_data = ''

    while '{' not in start_data:
        try:
            start_data += lines.pop(0)
        except IndexError:
            break

    try:
        start_data, extra = start_data.split('{', 1)
    except ValueError:
        extra = ''

    if extra.strip():
        lines.insert(0, extra)

    parent_cls, cls_name = start_data.rstrip().rsplit(' ', 1)
    parent_cls = parent_cls.replace('typedef', '')
    cls_name = cls_name.replace('typedef', '')

    if 'struct' in parent_cls or 'struct' in cls_name:
        parent_cls = parent_cls.replace('struct', '').strip()
        cls_name = cls_name.replace('struct', '').strip()
        data_type = 'ctypes.Structure'
    else:
        parent_cls = parent_cls.replace('union', '').strip()
        cls_name = cls_name.replace('union', '').strip()
        data_type = 'ctypes.Union'

    if not parent_cls:
        parent_cls = data_type

    cls_name = cls_name.replace('{', '').strip()

    if ';' in cls_name:
        cls_name = cls_name.replace(';', '')
        if parent_cls in ('ctypes.Structure', 'ctypes.Union'):
            print(
                TEMPLATE_DECLARATION.format(
                    indent=indent,
                    cls_name=cls_name.strip(),
                    parent_cls=parent_cls
                )
            )
            return struct_count, union_count
        else:
            if parent_cls == cls_name:
                return struct_count, union_count

            if '*' in cls_name or '*' in parent_cls:
                cls_name, parent_cls = process_param(cls_name, parent_cls)
                print(indent + cls_name + ' = ' + parent_cls)
            else:
                declarations += [cls_name.strip()]
                print(
                    TEMPLATE_DECLARATION.format(
                        indent=indent,
                        cls_name=cls_name.strip(),
                        parent_cls=parent_cls
                    )
                )
            return struct_count, union_count

    if cls_name not in declarations:
        declarations += [cls_name]
        print(
            TEMPLATE_DECLARATION.format(
                indent=indent,
                cls_name=cls_name.strip(),
                parent_cls=parent_cls
            )
        )

    anonymous = []
    fields = []
    sub_structure = []
    sub_structure_type = None
    brace_count = 0
    field = ''
    chained_comment = False
    field_comment = ''
    field_macro = ''

    var_names = data.rsplit('}', 1)[1].replace(';', '')
    var_names = list(n.strip() for n in var_names.split(','))

    if not cls_name and var_names:
        cls_name = var_names.pop(0)

    elif not cls_name:
        print(indent + '#~#~#~', repr(data))
        return struct_count, union_count

    if cls_name in var_names:
        var_names.remove(cls_name)

    data_fields = '~~~~'.join(lines)
    data_fields = data_fields[:data_fields.rfind('}')].split('~~~~')

    for line_num, line in enumerate(data_fields):
        if chained_comment and '*/' not in line:
            continue

        chained_comment = False

        if sub_structure_type is None:
            line, comment = parse_comment(line)
        else:
            comment = ''

        if line is None and comment is None:
            # /*
            # * Aliases for StringPrep
            # */
            comment = ''
            chained_comment = True
            for comnt in data_fields[line_num:]:
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

            line, comment = parse_comment(comment)
            field_comment = equalize_width(indent + '    ', comment)

            if not line:
                continue

        elif comment:
            field_comment = equalize_width(indent + '    ', comment)

        if sub_structure_type is None:
            import sys

            class STDOut(object):
                saved_data = ''
                stdout = sys.stdout

                def write(self, data):
                    STDOut.saved_data = data.rstrip()

                def __getattr__(self, item):
                    if item in self.__dict__:
                        return self.__dict__[item]
                    return getattr(STDOut.stdout, item)

            sys.stdout = STDOut()
            new_line, new_indent = parse_macro(indent, line.strip())
            sys.stdout = STDOut.stdout

            if new_line != line or new_indent != indent:
                field_macro = STDOut.saved_data
                line = new_line
                indent = new_indent
            else:
                field_macro = ''

        if not line:
            continue

        if line.startswith('#'):
            continue

        if '_Field_size_' in line:
            line = line.split(')', 1)[1]

        if 'OPTIONAL' in line:
            line = line[:line.find('OPTIONAL') - 1].rstrip()

        if (
            (
                line.strip().startswith('union') or
                line.strip().startswith('struct')
            ) and
            line.strip().endswith(';')
        ):
            line = line.replace('struct', '').replace('union', '')
        if line.strip().startswith('union'):
            sub_structure_type = 'union'

        elif line.strip().startswith('struct'):
            sub_structure_type = 'struct'

        if sub_structure_type is not None:
            if not sub_structure and line.strip().endswith(';'):
                mult = None
                line = line.replace(sub_structure_type, '').strip()[:-1]
                try:
                    p_cls, c_name = line.split(' ')
                except ValueError:
                    c_name = line
                    if sub_structure_type == 'union':
                        p_cls = 'ctypes.Union'
                    else:
                        p_cls = 'ctypes.Structure'

                if '*' in c_name:
                    f_name, f_data_type = process_param(
                        c_name,
                        c_name.replace('*', '')
                    )

                else:
                    f_name = c_name
                    f_data_type = cls_name + '.' + f_name
                    print(
                        TEMPLATE_DECLARATION.format(
                            indent=indent,
                            cls_name=f_name,
                            parent_cls=p_cls
                        )
                    )

                    print('\n')

                    print(
                        TEMPLATE_DECLARATION_SUBSTRUCTURE.format(
                            indent=indent,
                            cls_name=cls_name,
                            child_cls=f_name
                        )
                    )

            else:
                sub_structure += [line]
                brace_count += line.count('{')
                brace_count -= line.count('}')
                if brace_count == 0 and line.rstrip().endswith(';'):
                    f_name = (
                        line.replace(';', '').replace('}', '').strip()
                    )
                    if not f_name:

                        if sub_structure_type == 'union':
                            sub_count = union_count = union_count + 1
                        else:
                            sub_count = struct_count = struct_count + 1

                        f_name = '_{0}_{1}'.format(
                            sub_structure_type.title(),
                            sub_count
                        )

                        line = line.replace(
                            ';',
                            f_name + ';'
                        )
                        sub_structure[len(sub_structure) - 1] = line
                        anonymous += [f_name]

                    if '[' in f_name:
                        tmp_field_name, mult = f_name.split('[', 1)
                        mult = mult.replace(']', '').strip()

                        for i, ln in enumerate(sub_structure):
                            sub_structure[i] = ln.replace(
                                f_name,
                                tmp_field_name
                            )
                        f_name = tmp_field_name

                    else:
                        mult = None

                        sub_structure[0] = (
                            '{0}typedef {1} '.format(
                                indent,
                                sub_structure_type
                            )
                        )

                    if not sub_structure[1].strip().startswith('{'):
                        sub_structure[0] += '{'

                    parse_struct_union(
                        indent,
                        '\n'.join(sub_structure),
                        importer,
                        struct_count,
                        union_count,
                        declarations
                    )

                    f_data_type = cls_name + '.' + f_name

                else:
                    continue

            sub_structure = []
            sub_structure_type = None

            print(
                TEMPLATE_DECLARATION_SUBSTRUCTURE.format(
                    indent=indent,
                    cls_name=cls_name,
                    child_cls=f_name
                )
            )

            if '\n' in field_comment:
                fields += [[None, '\n' + field_comment]]
                field_comment = ''

            elif field_comment:
                field_comment = ' ' + field_comment[field_comment.find('#'):]

            if mult:
                fields += [
                    [
                        field_macro,
                        TEMPLATE_DECLARATION_FIELD.format(
                            indent=indent,
                            field_name=f_name,
                            field_data_type=f_data_type + ' * ' + mult,
                            comment=field_comment
                        )
                    ]
                ]
            else:
                fields += [
                    [
                        field_macro,
                        TEMPLATE_DECLARATION_FIELD.format(
                            indent=indent,
                            field_name=f_name,
                            field_data_type=f_data_type,
                            comment=field_comment
                        )
                    ]
                ]

            field_macro = ''
            field_comment = ''
            continue

        elif field:
            line = line.strip()
            if line.endswith('\\'):
                line = line[:-1].strip()
            field += ' ' + line
            if not line.endswith(';'):
                continue

        elif line.rstrip().endswith(';'):
            field = line
        else:
            line = line.strip()
            if line.endswith('\\'):
                line = line[:-1].strip()

            field = line
            continue

        try:
            field_data_type, field_name = (
                field[:-1].replace(';', '').strip().split(' ', 1)
            )
        except ValueError:
            print('*******', field)
            raise

        if ',' in field_name:
            field_names = list(
                fn.strip() for fn in field_name.split(',')
            )
            count = []
        elif '[' in field_name:
            count = []
            while '[' in field_name:
                field_name, c = field_name.rsplit('[', 1)
                count.insert(0, c.replace(']', '').strip())
            field_names = [field_name]
        else:
            count = []
            field_names = [field_name.strip()]

        for i, field_name in enumerate(field_names):
            while ' ' in field_name:
                try:
                    field_data_type, field_name = (
                        field_data_type.split(' ', 1)
                    )
                except ValueError:
                    break
            field_names[i] = field_name.strip()

        field_data_type = field_data_type.strip()
        field_data_type = field_data_type.replace(
            'IUnknown',
            'comtypes.IUnknown'
        )

        field_data_types = []
        for i, field_name in enumerate(field_names):

            field_name, fd_type = process_param(
                field_name,
                field_data_type
            )

            field_data_types += [fd_type]
            field_names[i] = field_name

        for i, field_data_type in enumerate(field_data_types):
            fd_type = field_data_type
            for j, cnt in enumerate(count):
                if j == 1:
                    fd_type = '(' + fd_type + ')'
                if j:
                    fd_type += '({0} * {1})'.format(
                        field_data_type,
                        cnt
                    )
                else:
                    fd_type += ' * ' + cnt

            field_data_types[i] = fd_type

        for i, field_name in enumerate(field_names):

            if '\n' in field_comment:
                fields += [[None, '\n' + field_comment]]
                field_comment = ''

            elif field_comment:
                field_comment = ' ' + field_comment[field_comment.find('#'):]

            fields += [
                [
                    field_macro,
                    TEMPLATE_DECLARATION_FIELD.format(
                        indent=indent,
                        field_name=field_name,
                        field_data_type=field_data_types[i],
                        comment=field_comment
                    )
                ]
            ]

        field_macro = ''
        field_comment = ''
        field = ''

    if anonymous:
        print(
            TEMPLATE_DECLARATION_ANONYMOUS_START.format(
                indent=indent,
                cls_name=cls_name
            )
        )

        for anon in anonymous:
            print(
                TEMPLATE_DECLARATION_ANONYMOUS.format(
                    indent=indent,
                    anonymous=anon
                )
            )
        print(
            TEMPLATE_DECLARATION_ANONYMOUS_END.format(
                indent=indent,
            )
        )

    if fields:
        macro_indexes = []

        for j, items in enumerate(fields[:]):
            if items[0]:
                macro_indexes += [[j, items]]
                fields.remove(items)

        if macro_indexes:
            print(indent + '_temp_fields_ = (')

        else:
            print(
                TEMPLATE_DECLARATION_FIELDS_START.format(
                    indent=indent,
                    cls_name=cls_name
                )
            )

        for _, field in fields:
            print(field)

        print(
            TEMPLATE_DECLARATION_FIELDS_END.format(
                indent=indent,
            )
        )

        if macro_indexes:
            for index, items in macro_indexes:
                macro, field = items
                macro = macro[4:]

                print(macro)
                print(
                    '{0}    _temp_fields_.insert({1}, {2})'.format(
                        indent,
                        index,
                        field.strip()[:-1]
                    )
                )
            print(
                '{0}{1}._fields_ = _temp_fields_'.format(indent, cls_name)
            )

    for i, var_name in enumerate(var_names[:]):
        if not var_name:
            var_names.pop(i)
            continue

        var_name, value = process_param(
            var_name,
            cls_name
        )

        if var_name is None:
            continue

        var_names[i] = indent + var_name + ' = ' + value

    if var_names:
        print('\n')

        for var_name in var_names:
            print(var_name)

    print('\n')

    return struct_count, union_count

#
#
# class Structure(object):
#
#     def __init__(self, importer, data, indent=''):
#         self.indent = indent
#         self.importer = importer
#         self.all = set()
#
#         self.lines = {}
#         start = None
#         brace_count = 0
#         if indent:
#             print data
#         else:
#             print "\n\n-- STRUCT ---------------------------------------------\n\n"
#
#         for i, line in enumerate(data[:]):
#             if '_Struct_size_bytes_' in line:
#                 l1, l2 = line.split('_Struct_size_bytes_(', 1)
#                 l2 = l2.split(')', 1)[1]
#                 line = l1 + l2
#
#             if (
#                 line.startswith(indent + 'typedef') or
#                 line.startswith(indent + 'struct')
#             ):
#                 if 'struct' in line:
#                     if line.rstrip().endswith(';'):
#                         self.lines[i] = [line]
#                     else:
#                         start = i
#                 elif indent + 'struct' not in data[i + 1] and 'struct' in data[i + 1]:
#                     if data[i + 1].rstrip().endswith(';'):
#                         self.lines[i] = data[i:i + 2]
#                     else:
#                         start = i
#
#             if start is not None:
#                 if '{' in line:
#                     brace_count += 1
#                 elif '}' in line:
#                     brace_count -= 1
#
#                 if brace_count == 0 and line.rstrip().endswith(';'):
#                     self.lines[start] = data[start:i + 1]
#                     print self.lines[start]
#                     start = None
#
#     def process(self):
#         if self.lines:
#             self.importer.add_importer('ctypes')
#
#         for line_num, lines in self.lines.items()[:]:
#             if len(lines) == 1:
#                 lines = lines[0].split(' ')
#                 attr_name = lines[-1].replace(';', '').strip()
#                 value = lines[-2].strip()
#
#                 while '*' in attr_name:
#                     value = 'POINTER(' + value + ')'
#                     attr_name = attr_name[1:]
#
#                 self.all.add(attr_name)
#
#                 if attr_name in self.importer.allowed:
#                     self.importer.add(attr_name)
#                     continue
#
#                 yield line_num, attr_name + ' = ' + value + '\n\n'
#                 continue
#
#             if 'struct' not in lines[0]:
#                 lines[0] += ' ' + lines.pop(1).lstrip()
#
#             start_data = ''
#
#             while '{' not in start_data:
#                 try:
#                     start_data += lines.pop(0)
#                 except IndexError:
#                     break
#
#             try:
#                 start_data, extra = start_data.split('{', 1)
#             except ValueError:
#                 extra = ''
#
#             if extra.strip():
#                 lines.insert(0, extra)
#
#             parent_cls, cls_name = start_data.rstrip().rsplit(' ', 1)
#             parent_cls = parent_cls.replace('typedef', '').replace('struct', '').strip()
#             cls_name = cls_name.replace('typedef', '').replace('struct', '').strip()
#
#             if not parent_cls:
#                 parent_cls = None
#
#             if ';' in cls_name:
#                 cls_name = cls_name.replace(';', '')
#                 if parent_cls is None:
#                     self.all.add(cls_name)
#                     if cls_name in self.importer.allowed:
#                         self.importer.add(cls_name)
#                         continue
#
#                     yield line_num, TEMPLATE_NO_FIELDS.format(
#                         cls_name=cls_name.strip()
#                     )
#                     continue
#                 else:
#                     if parent_cls == cls_name:
#                         continue
#
#                     while cls_name.startswith('*'):
#                         parent_cls = 'POINTER(' + parent_cls + ')'
#                         cls_name = cls_name[1:]
#
#                     self.all.add(cls_name)
#                     if cls_name in self.importer.allowed:
#                         self.importer.add(cls_name)
#                         continue
#
#                     yield line_num, cls_name + ' = ' + parent_cls
#                     continue
#
#             anonymous = []
#             sub_structures = []
#             fields = []
#             union = []
#             struct = []
#
#             struct_count = 0
#             union_count = 0
#             brace_count = 0
#             field = ''
#
#             var_names = ' '.join(lines)
#             var_names = var_names[var_names.rfind('}') + 1:].replace(
#                 ';',
#                 ''
#             ).replace(' ', '').split(',')
#
#             if not cls_name:
#                 cls_name = var_names.pop(0)
#
#             if cls_name in var_names:
#                 var_names.remove(cls_name)
#
#             data_fields = '~~~~'.join(lines)
#             data_fields = data_fields[:data_fields.rfind('}')].split('~~~~')
#
#             for line in data_fields:
#                 if line.startswith('#'):
#                     continue
#
#                 if '_Field_size_' in line:
#                     line = line.split(')', 1)[1]
#
#                 if 'OPTIONAL' in line:
#                     line = line[:line.find('OPTIONAL') - 1].rstrip()
#
#                 if (
#                     (
#                         line.strip().startswith('union') or
#                         line.strip().startswith('struct')
#                     ) and
#                     line.strip().endswith(';')
#                 ):
#                     line = line.replace('struct', '').replace('union', '')
#
#                 if union or line.strip().startswith('union') and not struct:
#                     if not union and line.strip().endswith(';'):
#                         mult = None
#                         line = line.replace('union', '').strip()[:-1]
#                         p_cls, c_name = line.split(' ')
#                         p_count = c_name.count('*')
#                         c_name = c_name.replace('*', '')
#                         union = TEMPLATE_SUBCLASS_NO_FIELDS.format(
#                             cls_name=c_name,
#                             parent_cls=p_cls
#                         )
#
#                         union = [
#                             '\n'.join(
#                                 self.indent + '    ' + ln for ln in union.split('\n')
#                             )
#                         ]
#
#                         f_data_type = c_name
#                         f_name = c_name
#                         for _ in range(p_count):
#                             f_data_type = (
#                                 'POINTER(' + f_data_type + ')'
#                             )
#
#                     else:
#                         union += [line]
#                         brace_count += line.count('{')
#                         brace_count -= line.count('}')
#                         if brace_count == 0 and line.rstrip().endswith(';'):
#                             f_name = (
#                                 line.replace(';', '').replace('}', '').strip()
#                             )
#                             if not f_name:
#                                 f_name = '_Union_' + str(union_count)
#                                 union_count += 1
#                                 line = line.replace(
#                                     ';',
#                                     f_name + ';'
#                                 )
#                                 union[len(union) - 1] = line
#                                 anonymous += [f_name]
#
#                             if '[' in f_name:
#                                 tmp_field_name, mult = f_name.split('[', 1)
#                                 mult = mult.replace(']', '').strip()
#
#                                 for i, ln in enumerate(union):
#                                     union[i] = ln.replace(
#                                         f_name,
#                                         tmp_field_name
#                                     )
#                                 f_name = tmp_field_name
#
#                             else:
#                                 mult = None
#
#                             union[0] = self.indent + '    typedef union '
#
#                             if not union[1].strip().startswith('{'):
#                                 union[0] += '{'
#
#                             union = Union(
#                                 self.importer,
#                                 union[:],
#                                 self.indent + '    '
#                             ).process()
#
#                             union = list(
#                                 item[1]
#                                 for item in union
#                             )
#
#                             for i, item in enumerate(union):
#                                 union[i] = item.rstrip() + '\n'
#
#                             f_data_type = f_name
#                         else:
#                             continue
#
#                     sub_structures += union[:]
#                     union = []
#
#                     if mult:
#                         fields += [
#                             FIELD_TEMPLATE.format(
#                                 field_name=f_name,
#                                 field_data_type=f_data_type + ' * ' + mult
#                             )
#                         ]
#                     else:
#                         fields += [
#                             FIELD_TEMPLATE.format(
#                                 field_name=f_name,
#                                 field_data_type=f_data_type
#                             )
#                         ]
#
#                     continue
#
#                 elif struct or line.strip().startswith('struct') and not union:
#                     if not struct and line.strip().endswith(';'):
#                         mult = None
#                         line = line.replace('struct', '').strip()[:-1]
#                         try:
#                             p_cls, c_name = line.split(' ', 1)
#                         except ValueError:
#                             import time
#                             print line
#                             time.sleep(1)
#                             raise
#                         p_count = c_name.count('*')
#                         c_name = c_name.replace('*', '').strip()
#                         struct = TEMPLATE_SUBCLASS_NO_FIELDS.format(
#                             cls_name=c_name,
#                             parent_cls=p_cls
#                         )
#
#                         struct = [
#                             '\n'.join(
#                                 self.indent + '    ' + ln for ln in struct.split('\n')
#                             )
#                         ]
#
#                         f_data_type = c_name
#                         f_name = c_name
#                         for _ in range(p_count):
#                             f_data_type = (
#                                 'POINTER(' + f_data_type + ')'
#                             )
#
#                     else:
#                         struct += [line]
#                         brace_count += line.count('{')
#                         brace_count -= line.count('}')
#                         if brace_count == 0 and line.rstrip().endswith(';'):
#                             f_name = (
#                                 line.replace(';', '').replace('}', '').strip()
#                             )
#                             if not f_name:
#                                 f_name = '_Struct_' + str(struct_count)
#                                 struct_count += 1
#                                 line = line.replace(';', f_name + ';')
#                                 struct[len(struct) - 1] = line
#                                 anonymous += [f_name]
#
#                             if '[' in f_name:
#                                 tmp_field_name, mult = f_name.split('[', 1)
#                                 mult = mult.replace(']', '').strip()
#
#                                 for i, ln in enumerate(struct):
#                                     struct[i] = ln.replace(
#                                         f_name,
#                                         tmp_field_name
#                                     )
#
#                                 f_name = tmp_field_name
#                             else:
#                                 mult = None
#
#                             struct[0] = self.indent + '    typedef struct '
#
#                             if not struct[1].strip().startswith('{'):
#                                 struct[0] += '{'
#
#                             struct = Structure(
#                                 self.importer,
#                                 struct[:],
#                                 self.indent + '    '
#                             ).process()
#
#                             struct = list(
#                                 item[1]
#                                 for item in struct
#                             )
#
#                             for i, item in enumerate(struct):
#                                 struct[i] = item.rstrip() + '\n'
#
#                             f_data_type = f_name
#                         else:
#                             continue
#
#                     sub_structures += struct[:]
#
#                     struct = []
#
#                     if mult:
#                         fields += [
#                             FIELD_TEMPLATE.format(
#                                 field_name=f_name,
#                                 field_data_type=f_data_type + ' * ' + mult
#                             )
#                         ]
#                     else:
#                         fields += [
#                             FIELD_TEMPLATE.format(
#                                 field_name=f_name,
#                                 field_data_type=f_data_type
#                             )
#                         ]
#
#                     continue
#
#                 elif field:
#                     line = line.strip()
#                     if line.endswith('\\'):
#                         line = line.rstrip()[:-1]
#                     field += line
#                     if not line.endswith(';'):
#                         continue
#
#                 elif line.rstrip().endswith(';'):
#                     field = line.strip()
#                 else:
#                     line = line.strip()
#                     if line.endswith('\\'):
#                         line = line[1:]
#
#                     field = line
#                     continue
#
#                 field_data_type, field_name = (
#                     field[:-1].replace(';', '').strip().split(' ', 1)
#                 )
#
#                 if ',' in field_name:
#                     field_names = list(
#                         fn.strip() for fn in field_name.split(',')
#                     )
#                     count = []
#                 elif '[' in field_name:
#                     count = []
#                     while '[' in field_name:
#                         field_name, c = field_name.rsplit('[', 1)
#                         count.insert(0, c.replace(']', '').strip())
#                     field_names = [field_name]
#                 else:
#                     count = []
#                     field_names = [field_name.strip()]
#
#                 for i, field_name in enumerate(field_names):
#                     while ' ' in field_name:
#                         try:
#                             field_data_type, field_name = (
#                                 field_data_type.split(' ', 1)
#                             )
#                         except ValueError:
#                             break
#                     field_names[i] = field_name.strip()
#
#                 field_data_type = field_data_type.strip()
#                 field_data_type = field_data_type.replace(
#                     'IUnknown',
#                     'comtypes.IUnknown'
#                 )
#
#                 self.importer.add(field_data_type)
#
#                 field_data_types = []
#                 for i, field_name in enumerate(field_names):
#                     fd_type = field_data_type
#                     while '*' in field_name:
#                         fd_type = 'POINTER(' + fd_type + ')'
#                         field_name = field_name[1:]
#                         self.importer.add('POINTER')
#                     field_data_types += [fd_type]
#                     field_names[i] = field_name
#
#                 for i, field_data_type in enumerate(field_data_types):
#                     fd_type = field_data_type
#                     for j, cnt in enumerate(count):
#                         if j == 1:
#                             fd_type = '(' + fd_type + ')'
#                         if j:
#                             fd_type += '({0} * {1})'.format(
#                                 field_data_type,
#                                 cnt
#                             )
#                         else:
#                             fd_type += ' * ' + cnt
#
#                     field_data_types[i] = fd_type
#
#                 for i, field_name in enumerate(field_names):
#
#                     fields += [
#                         FIELD_TEMPLATE.format(
#                             field_name=field_name,
#                             field_data_type=field_data_types[i]
#                         )
#                     ]
#
#                 field = ''
#             if len(self.indent):
#                 for i, item in enumerate(sub_structures):
#                     sub_structures[i] = '\n'.join(
#                         itm[len(self.indent):] for itm in item.split('\n')
#                     )
#
#             self.all.add(cls_name)
#
#             if cls_name in self.importer.allowed:
#                 self.importer.add(cls_name)
#                 template = ''
#
#             elif anonymous:
#                 template = TEMPLATE_ANONYMOUS.format(
#                     cls_name=cls_name,
#                     fields='\n'.join(fields),
#                     anonymous=''.join("'" + a + "', " for a in anonymous),
#                     sub_structures=''.join(sub_structures)
#                 )
#
#             elif sub_structures:
#                 template = TEMPLATE_SUBSTRUCTURES.format(
#                     cls_name=cls_name,
#                     fields='\n'.join(fields),
#                     sub_structures=''.join(sub_structures)
#                 )
#
#             else:
#                 template = TEMPLATE.format(
#                     cls_name=cls_name,
#                     fields='\n'.join(fields)
#                 )
#
#             for i, var_name in enumerate(var_names[:]):
#                 if not var_name:
#                     var_names.pop(i)
#                     continue
#
#                 value = cls_name
#
#                 if var_name == value:
#                     continue
#
#                 while var_name.startswith('*'):
#                     value = 'POINTER(' + value + ')'
#                     var_name = var_name[1:]
#                     self.importer.add('POINTER')
#
#                 self.all.add(var_name)
#                 if var_name in self.importer.allowed:
#                     self.importer.add(var_name)
#                     continue
#
#                 var_names[i] = var_name + ' = ' + value
#
#             if var_names:
#                 template += '\n'.join(var_names)
#                 yield line_num, '\n'.join(
#                     self.indent + line for line in template.split('\n')
#                 ) + '\n\n'
#             elif template:
#                 yield line_num, '\n'.join(
#                     self.indent + line for line in template.split('\n')
#                 )
#
#
# from union import Union
