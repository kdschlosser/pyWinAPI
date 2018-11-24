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


u_s_declarations = []


TEMPLATE_DECLARATION = '''{indent}class {cls_name}({parent_cls}):
{indent}    pass
'''

TEMPLATE_DECLARATION_FIELDS_MACRO_START = '''{indent}_TEMP_{cls_name} = ['''
TEMPLATE_DECLARATION_FIELDS_MACRO_CONTINUE = '''{indent}_TEMP_{cls_name} += ['''
TEMPLATE_DECLARATION_FIELDS_MACRO_END = '''{indent}]'''
TEMPLATE_DECLARATION_FIELDS_MACRO_ASSIGN = '''{indent}{cls_name}._fields_ = _TEMP_{cls_name}'''

TEMPLATE_DECLARATION_FIELDS_START = '''{indent}{cls_name}._fields_ = ['''
TEMPLATE_DECLARATION_FIELDS_END = '''{indent}]'''
TEMPLATE_DECLARATION_FIELD = '''{indent}    ('{field_name}', {field_data_type}),{comment}'''
TEMPLATE_DECLARATION_FIELD_BIT = '''{indent}    ('{field_name}', {field_data_type}, {field_bit}),{comment}'''
TEMPLATE_DECLARATION_ANONYMOUS_START = '''{indent}{cls_name}._anonymous_ = ('''
TEMPLATE_DECLARATION_ANONYMOUS_END = '''{indent})'''
TEMPLATE_DECLARATION_ANONYMOUS = '''{indent}    '{anonymous}','''
TEMPLATE_DECLARATION_SUBSTRUCTURE = '''{indent}{cls_name}.{child_cls} = {child_cls}
'''

def parse_struct_union(
    indent,
    data,
    importer,
    struct_count,
    union_count,
    declarations,
    declare=False
):
    import sys

    lines = data.split('\n')
    sys.stderr.write(str(lines) + '\n')

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
            print(indent + attr_name + ' = ' + value + '\n')
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

    if 'public' in start_data:
        import sys
        sys.stderr.write(data)
        brace_count = 0
        start = None
        for i, line in enumerate(lines):
            if line.strip().startswith('typedef '):
                start = i
            if start is not None:
                brace_count += line.count('{')
                brace_count -= line.count('}')

                if ';' in line and brace_count == 0:
                    stop = i
                    break
        else:
            return struct_count, union_count

        res = parse_struct_union(
            indent,
            '\n'.join(lines[start:stop]),
            importer,
            struct_count,
            union_count,
            declarations,
            declare
        )

        return res + (stop,)
    try:
        parent_cls, cls_name = start_data.rstrip().rsplit(' ', 1)
    except ValueError:
        brace_count = 1
        cls_names = ''
        end_index = 0

        for i, line in enumerate(lines):
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count == 0:
                cls_names += line
                end_index = i

            if ';' in line and brace_count == 0:
                break
        else:
            return struct_count, union_count

        cls_names = cls_names.replace(';', '').replace('}', '').strip()
        if not cls_names:
            return struct_count, union_count

        cls_names = cls_names.split(' ')
        cls_name = cls_names[0]
        parent_cls = start_data.strip()
        lines = lines[:end_index]
        lines[end_index] = '} ' + ' '.join(cls_names[1:]) + ';'

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

    if not parent_cls or 'DECLSPEC_ALIGN' in parent_cls:
        parent_cls = data_type

    cls_name = cls_name.replace('{', '').strip()
    if ';' in cls_name:
        cls_name = cls_name.replace(';', '').strip()
        if parent_cls in ('ctypes.Structure', 'ctypes.Union'):
            if declare:
                u_s_declarations.append(
                    TEMPLATE_DECLARATION.format(
                        indent='',
                        cls_name=cls_name,
                        parent_cls=parent_cls
                    )
                )
            else:
                print(
                    TEMPLATE_DECLARATION.format(
                        indent=indent,
                        cls_name=cls_name,
                        parent_cls=parent_cls
                    )
                )
                print('\n')
            return struct_count, union_count
        else:
            if parent_cls == cls_name:
                return struct_count, union_count

            if '*' in cls_name or '*' in parent_cls:
                cls_name, parent_cls = process_param(cls_name, parent_cls)
                print(indent + cls_name + ' = ' + parent_cls)
            else:
                declarations += [cls_name]
                if declare:
                    u_s_declarations.append(
                        TEMPLATE_DECLARATION.format(
                            indent='',
                            cls_name=cls_name,
                            parent_cls=parent_cls
                        )
                    )
                else:
                    print(
                        TEMPLATE_DECLARATION.format(
                            indent=indent,
                            cls_name=cls_name.strip(),
                            parent_cls=parent_cls
                        )
                    )
                    print('\n')

            return struct_count, union_count
    try:
        var_names = data.rsplit('}', 1)[1].replace(';', '')
    except:
        var_names = data.replace(';', '')

    var_names = list(n.strip() for n in var_names.split(','))

    if not cls_name and var_names:
        cls_name = var_names.pop(0)

    elif not cls_name:
        print(indent + '#~#~#~', repr(data))
        return struct_count, union_count

    if cls_name in var_names:
        var_names.remove(cls_name)

    if cls_name not in declarations:
        declarations += [cls_name.strip()]

        if declare:
            for item in u_s_declarations:
                if item.startswith('class ' + cls_name):
                    break
            else:
                u_s_declarations.append(
                    TEMPLATE_DECLARATION.format(
                        indent='',
                        cls_name=cls_name.strip(),
                        parent_cls=parent_cls
                    )
                )
        else:
            print(
                TEMPLATE_DECLARATION.format(
                    indent=indent,
                    cls_name=cls_name.strip(),
                    parent_cls=parent_cls
                )
            )
            print('\n')
    else:
        return struct_count, union_count

    anonymous = []
    fields = []
    sub_structure_type = None
    field = ''
    chained_comment = False
    field_comment = ''
    field_macro = ''
    macro_output = None
    skip_until = None

    data_fields = '~~~~'.join(lines)
    data_fields = data_fields[:data_fields.rfind('}')].split('~~~~')

    found_defines = []
    for line_num, line in enumerate(data_fields):

        if skip_until is not None:
            if line_num <= skip_until:
                continue

            skip_until = None

        if (
            line.strip().startswith('# define') or
            line.strip().startswith('#define')
        ):
            var_name, var_value = line.strip()[1:].replace('define', '', 1).strip().split(' ', 1)
            var_name = var_name.strip()
            var_value = var_value.strip()

            if var_value.startswith('('):
                var_value = var_value[1:].strip()

            def_template = '{0}{1} = {2}'.format(
                indent,
                var_name,
                var_value
            )

            if len(def_template) > 76:
                def_template = '{0}{1} = (\n{0}    {2}\n{0})'.format(
                    indent,
                    var_name,
                    var_value
                )
            print(def_template)
            continue

        if (
            line.strip().startswith('#endif') or
            line.strip().startswith('# endif')
        ):
            field_macro = ''
            fields += [[line, '']]
            indent = indent[:-4]
            macro_output = None
            continue

        for item in ('ifdef', 'idndef', 'if', 'elif', 'else'):
            if (
                line.strip().startswith('#' + item) or
                line.strip().startswith('# ' + item)
            ):
                define = True
                break
        else:
            define = False

        if define:
            macro_output = []
            import sys

            stdout = sys.stdout

            class STDOut(object):
                def write(self, data):
                    sys.stderr.write(data + '\n')
                    macro_output.append(data)

                def __getattr__(self, item):
                    if item in self.__dict__:
                        return self.__dict__[item]
                    return getattr(STDOut.stdout, item)

            sys.stdout = STDOut()
            _, indent = parse_macro(indent, line.strip(), struct=True)
            sys.stdout = stdout
            field_macro = line
            continue

        if ' ' not in line.strip():
            continue

        if chained_comment and '*/' not in line:
            continue

        chained_comment = False

        if sub_structure_type is None:
            line, comment = parse_comment(line)
        else:
            comment = ''

        if line is None and comment is None:
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

        if not line:
            continue

        if line.startswith('#'):
            continue

        if '_Field_' in line:
            chunk_1, chunk_2 = line.split('_Field_', 1)
            chunk_2 = chunk_2.split('(', 1)[1]
            bad_chunk = ''
            b_count = 1
            for char in list(chunk_2):
                b_count += char.count('(')
                b_count -= char.count(')')
                bad_chunk += char
                if not b_count:
                    break
            else:
                continue

            chunk_2 = chunk_2.replace(bad_chunk, '', 1)
            line = chunk_1 + chunk_2

            if not line.strip():
                continue

        if 'OPTIONAL' in line:
            line = line[:line.find('OPTIONAL') - 1].rstrip()

        if sub_structure_type is None:
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
            if line.strip().endswith(';'):
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
                    if macro_output is not None:
                        print(''.join(macro_output))
                        macro_output = None

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
                sub_structure_type = None
            else:
                sub_structure = []
                brace_count = 0
                skip_until = line_num
                for j, sub_line in enumerate(lines[line_num:]):
                    skip_until = line_num + j
                    sub_structure += [sub_line]
                    brace_count += sub_line.count('{')
                    brace_count -= sub_line.count('}')
                    if ';' in sub_line and brace_count == 0:
                        break

                sys.stderr.write(str(sub_structure) + '\n')

                f_name = sub_structure[-1]

                f_name = (
                    f_name.replace(';', '').replace('}', '').strip()
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
                    sub_structure[len(sub_structure) - 1] = (
                        sub_structure[len(sub_structure) - 1].replace(
                            ';',
                            f_name + ';'
                        )
                    )

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
                    sub_structure[0].replace(
                        sub_structure_type,
                        '{0}typedef {1} '.format(
                            indent,
                            sub_structure_type
                        )
                    )
                )

                if macro_output is not None:
                    print(''.join(macro_output))
                    macro_output = None

                parse_struct_union(
                    indent,
                    '\n'.join(sub_structure),
                    importer,
                    struct_count,
                    union_count,
                    []
                )

                f_data_type = cls_name + '.' + f_name
                sub_structure_type = None

                print(
                    TEMPLATE_DECLARATION_SUBSTRUCTURE.format(
                        indent=indent,
                        cls_name=cls_name,
                        child_cls=f_name
                    )
                )

            if '\n' in field_comment:
                fields += [[field_macro, '\n' + field_comment]]
                field_comment = ''

            elif field_comment:
                field_comment = ' ' + field_comment[field_comment.find('#'):]

            if mult:
                if ':' in f_name:
                    f_name,  f_bit = f_name.split(':')
                    f_name = f_name.strip()
                    f_bit = f_bit.strip()
                    template = TEMPLATE_DECLARATION_FIELD_BIT.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type + ' * ' + mult,
                        field_bit=f_bit,
                        comment=''
                    )

                else:
                    template = TEMPLATE_DECLARATION_FIELD.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type + ' * ' + mult,
                        comment=''
                    )

                if field_comment is not None and field_comment.strip():
                    field_comment = equalize_width(indent + '    ',
                        field_comment)
                    template = '\n\n' + field_comment + '\n' + template

                fields += [[field_macro, template]]
            else:
                if ':' in f_name:
                    f_name,  f_bit = f_name.split(':')
                    f_name = f_name.strip()
                    f_bit = f_bit.strip()
                    template = TEMPLATE_DECLARATION_FIELD_BIT.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type,
                        field_bit=f_bit,
                        comment=''
                    )

                else:
                    template = TEMPLATE_DECLARATION_FIELD.format(
                        indent=indent,
                        field_name=f_name,
                        field_data_type=f_data_type,
                        comment=''
                    )

                if field_comment is not None and field_comment.strip():
                    field_comment = equalize_width(indent + '    ', field_comment)
                    template = '\n\n' + field_comment + '\n' + template

                fields += [[field_macro, template]]

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
            if '}' in field:
                continue

            import sys

            parent_cls = line.replace(';', '').strip()
            for i, item in enumerate(u_s_declarations):
                if item.startswith('class ' + cls_name + '('):
                    u_s_declarations[i] = TEMPLATE_DECLARATION.format(
                        indent='',
                        cls_name=cls_name,
                        parent_cls=parent_cls
                    )
                    break
            else:
                sys.stderr.write('******* ' + str(field) + '\n')
                raise

            continue

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
                fields += [[field_macro, '\n' + field_comment]]
                field_comment = ''

            elif field_comment:
                field_comment = ' ' + field_comment[field_comment.find('#'):]

            if field_name is None:
                continue

            if field_data_types[i] in ('_In_', '_Out_', 'IN', 'OUT', '_Inout_'):
                field_data_types[i], field_name = field_name.split(' ', 1)
                field_data_types[i] = field_data_types[i].strip()
                field_name = field_name.strip()

                field_name, field_data_types[i] = process_param(field_name, field_data_types[i])

            if ':' in field_name:
                field_name, field_bit = field_name.split(':')
                field_name = field_name.strip()
                field_bit = field_bit.strip()
                template = TEMPLATE_DECLARATION_FIELD_BIT.format(
                    indent=indent,
                    field_name=field_name,
                    field_data_type=field_data_types[i],
                    field_bit=field_bit,
                    comment=''
                )

            else:
                template = TEMPLATE_DECLARATION_FIELD.format(
                    indent=indent,
                    field_name=field_name,
                    field_data_type=field_data_types[i],
                    comment=''
                )

            if field_comment is not None and field_comment.strip():
                field_comment = equalize_width(indent + '    ', field_comment)
                template = '\n\n' + field_comment + '\n' + template

            fields += [[field_macro, template]]

        field_comment = ''
        field = ''

    if not cls_name:
        return struct_count, union_count

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

    print(('\n'.join(found_defines)))
    if found_defines:
        print()

    if fields:
        for items in fields:
            if items[0]:
                has_macro = True
                break
        else:
            has_macro = False

        last_field = ''
        if has_macro:
            print(
                TEMPLATE_DECLARATION_FIELDS_MACRO_START.format(
                    indent=indent,
                    cls_name=cls_name
                )
            )

            last_macro = ''
            closed_macro = False
            for macro, field in fields:
                if macro and macro != last_macro:
                    last_macro = macro
                    closed_macro = True
                    print(
                        TEMPLATE_DECLARATION_FIELDS_MACRO_END.format(
                            indent=indent)
                    )
                    _, indent = parse_macro(indent + '    ', macro.strip(), struct=True)

                    if 'endif' in macro:
                        print()

                if not field:
                    continue

                if closed_macro:
                    closed_macro = False
                    print(
                        TEMPLATE_DECLARATION_FIELDS_MACRO_CONTINUE.format(
                            indent=indent,
                            cls_name=cls_name
                        )
                    )
                if field.startswith('\n\n') and last_field.endswith('\n'):
                    field = field[2:]

                last_field = field
                print(field)

            if not closed_macro:
                print(
                    TEMPLATE_DECLARATION_FIELDS_MACRO_END.format(
                        indent=indent)
                )

            print(
                TEMPLATE_DECLARATION_FIELDS_MACRO_ASSIGN.format(
                    indent=indent,
                    cls_name=cls_name
                )
            )

        else:
            print(
                TEMPLATE_DECLARATION_FIELDS_START.format(
                    indent=indent,
                    cls_name=cls_name
                )
            )

            for _, field in fields:
                if field.startswith('\n\n') and last_field.endswith('\n'):
                    field = field[2:]

                last_field = field
                print(field)

            print(
                TEMPLATE_DECLARATION_FIELDS_END.format(
                    indent=indent,
                )
            )

    variables = []

    for var_name in var_names:
        if not var_name:
            continue

        var_name, value = process_param(
            var_name,
            cls_name
        )

        if var_name is None:
            continue

        if declare:
            variables += [var_name + ' = ' + value]

        else:
            variables += [indent + var_name + ' = ' + value]

    if variables:
        variables = '\n'.join(variables)
        if declare:
            u_s_declarations.append('\n' + variables + '\n')
        else:
            print(variables)

    return struct_count, union_count
