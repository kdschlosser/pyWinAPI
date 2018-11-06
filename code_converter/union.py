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


TEMPLATE_NO_FIELDS = '''
class {cls_name}(ctypes.Structure):
    pass


'''

TEMPLATE = '''
class {cls_name}(ctypes.Union):
    _fields_ = [
{fields}
    ]


'''

TEMPLATE_ANONYMOUS = '''
class {cls_name}(ctypes.Union):
{sub_structures}
    _anonymous_ = ({anonymous}) 
    _fields_ = [
{fields}
    ]


'''

TEMPLATE_SUBSTRUCTURES = '''
class {cls_name}(ctypes.Union):
{sub_structures}
    _fields_ = [
{fields}
    ]


'''

FIELD_TEMPLATE = '''        ('{field_name}', {field_data_type}),'''



class Union(object):

    def __init__(self, importer, data, indent=''):
        self.indent = indent
        self.importer = importer
        self.all = set()

        self.lines = {}
        start = None
        brace_count = 0
        if indent:
            print data
        else:
            print "\n\n-- UNION ----------------------------------------------\n\n"
        for i, line in enumerate(data[:]):
            if '_Union_size_bytes_' in line:
                l1, l2 = line.split('_Union_size_bytes_(', 1)
                l2 = l2.split(')', 1)[1]
                line = l1 + l2

            if (
                line.startswith(indent + 'typedef') or
                line.startswith(indent + 'union')
            ):
                if 'union' in line:
                    if line.rstrip().endswith(';'):
                        self.lines[i] = [line]
                    else:
                        start = i
                elif indent + 'union' not in data[i + 1] and 'union' in data[i + 1]:
                    if data[i + 1].rstrip().endswith(';'):
                        self.lines[i] = data[i:i + 2]
                    else:
                        start = i

            if start is not None:
                if '{' in line:
                    brace_count += 1
                elif '}' in line:
                    brace_count -= 1

                if brace_count == 0 and line.rstrip().endswith(';'):
                    self.lines[start] = data[start:i + 1]
                    print self.lines[start]
                    start = None

    def process(self):
        if self.lines:
            self.importer.add_importer('ctypes')

        for line_num, lines in self.lines.items()[:]:
            'typedef union tagBINDPTR *LPBINDPTR;'
            if len(lines) == 1:
                lines = lines[0].split(' ')
                attr_name = lines[-1].replace(';', '').strip()
                value = lines[-2].strip()

                while '*' in attr_name:
                    value = 'POINTER(' + value + ')'
                    attr_name = attr_name[1:]

                self.all.add(attr_name)
                if attr_name in self.importer.allowed:
                    self.importer.add(attr_name)
                    continue

                yield line_num, attr_name + ' = ' + value + '\n\n'
                continue

            if 'union' not in lines[0]:
                lines[0] += ' ' + lines.pop(1).lstrip()

            start_data = ''

            while '{' not in start_data:
                try:
                    start_data += lines.pop(0)
                except IndexError:
                    import time
                    print self.lines[line_num]
                    time.sleep(0.1)
                    raise

            try:
                start_data, extra = start_data.split('{', 1)
            except ValueError:
                print repr(start_data)
                import time
                time.sleep(1)
                raise
            if extra.strip():
                lines.insert(0, extra)

            parent_cls, cls_name = start_data.rstrip().rsplit(' ', 1)
            parent_cls = parent_cls.replace('typedef', '').replace('union', '').strip()
            cls_name = cls_name.replace('typedef', '').replace('union', '').strip()

            if not parent_cls:
                parent_cls = None

            if ';' in cls_name:
                cls_name = cls_name.replace(';', '')
                if parent_cls is None:

                    self.all.add(cls_name)
                    if cls_name in self.importer.allowed:
                        self.importer.add(cls_name)
                        continue

                    yield line_num, TEMPLATE_NO_FIELDS.format(
                        cls_name=cls_name.strip()
                    )
                    continue
                else:
                    if parent_cls == cls_name:
                        continue

                    while cls_name.startswith('*'):
                        parent_cls = 'POINTER(' + parent_cls + ')'
                        cls_name = cls_name[1:]

                    self.all.add(cls_name)
                    if cls_name in self.importer.allowed:
                        self.importer.add(cls_name)
                        continue

                    yield line_num, cls_name + ' = ' + parent_cls
                    continue

            anonymous = []
            sub_structures = []
            fields = []
            union = []
            struct = []

            struct_count = 0
            union_count = 0
            brace_count = 0
            field = ''

            var_names = ' '.join(lines)
            var_names = var_names[var_names.rfind('}') + 1:].replace(
                ';',
                ''
            ).replace(' ', '').split(',')

            if not cls_name:
                cls_name = var_names.pop(0)

            if cls_name in var_names:
                var_names.remove(cls_name)

            data_fields = '~~~~'.join(lines)
            data_fields = data_fields[:data_fields.rfind('}')].split('~~~~')

            for line in data_fields:
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

                if union or line.strip().startswith('union') and not struct:
                    union += [line]
                    brace_count += line.count('{')
                    brace_count -= line.count('}')
                    if brace_count == 0 and line.rstrip().endswith(';'):
                        field_name = (
                            line.replace(';', '').replace('}', '').strip()
                        )
                        if not field_name:
                            field_name = '_Union_' + str(union_count)
                            union_count += 1
                            line = line.replace(
                                ';',
                                field_name + ';'
                            )
                            union[len(union) - 1] = line
                            anonymous += [field_name]

                        if '[' in field_name:
                            tmp_field_name, mult = field_name.split('[', 1)
                            mult = mult.replace(']', '').strip()

                            for i, ln in enumerate(union):
                                union[i] = ln.replace(
                                    field_name,
                                    tmp_field_name
                                )
                            field_name = tmp_field_name
                        else:
                            mult = None

                        union[0] = self.indent + '    typedef union '

                        if not union[1].strip().startswith('{'):
                            union[0] += '{'

                        union = Union(
                            self.importer,
                            union[:],
                            self.indent + '    '
                        ).process()

                        union = list(
                            item[1]
                            for item in union
                        )

                        for i, item in enumerate(union):
                            union[i] = item.rstrip() + '\n'

                        sub_structures += union[:]
                        union = []

                        if mult:
                            fields += [
                                FIELD_TEMPLATE.format(
                                    field_name=field_name,
                                    field_data_type=field_name + ' * ' + mult
                                )
                            ]
                        else:
                            fields += [
                                FIELD_TEMPLATE.format(
                                    field_name=field_name,
                                    field_data_type=field_name
                                )
                            ]

                    continue

                elif struct or line.strip().startswith('struct') and not union:
                    struct += [line]
                    brace_count += line.count('{')
                    brace_count -= line.count('}')
                    if brace_count == 0 and line.rstrip().endswith(';'):
                        field_name = (
                            line.replace(';', '').replace('}', '').strip()
                        )
                        if not field_name:
                            field_name = '_Struct_' + str(struct_count)
                            struct_count += 1
                            line = line.replace(';', field_name + ';')
                            struct[len(struct) - 1] = line
                            anonymous += [field_name]

                        if '[' in field_name:
                            tmp_field_name, mult = field_name.split('[', 1)
                            mult = mult.replace(']', '').strip()

                            for i, ln in enumerate(struct):
                                struct[i] = ln.replace(
                                    field_name,
                                    tmp_field_name
                                )

                            field_name = tmp_field_name
                        else:
                            mult = None

                        struct[0] = self.indent + '    typedef struct '
                        try:
                            if not struct[1].strip().startswith('{'):
                                struct[0] += '{'
                        except IndexError:
                            import time
                            print struct
                            print data_fields
                            time.sleep(0.1)
                            raise

                        struct = Structure(
                            self.importer,
                            struct[:],
                            self.indent + '    '
                        ).process()

                        struct = list(
                            item[1]
                            for item in struct
                        )

                        for i, item in enumerate(struct):
                            struct[i] = item.rstrip() + '\n'

                        sub_structures += struct[:]

                        struct = []

                        if mult:
                            fields += [
                                FIELD_TEMPLATE.format(
                                    field_name=field_name,
                                    field_data_type=field_name + ' * ' + mult
                                )
                            ]
                        else:
                            fields += [
                                FIELD_TEMPLATE.format(
                                    field_name=field_name,
                                    field_data_type=field_name
                                )
                            ]

                    continue

                elif field:
                    line = line.strip()
                    if line.endswith('\\'):
                        line = line.rstrip()[:-1]
                    field += line
                    if not line.endswith(';'):
                        continue

                elif line.rstrip().endswith(';'):
                    field = line.strip()
                else:
                    line = line.strip()
                    if line.endswith('\\'):
                        line = line[1:]

                    field = line
                    continue

                try:

                    field_data_type, field_name = (
                        field[:-1].replace(';', '').strip().split(' ', 1)
                    )
                except ValueError:
                    import time
                    print '**********************ERROR:', field
                    print '**********************ERROR:', lines
                    time.sleep(0.1)
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
                self.importer.add(field_data_type)

                field_data_types = []
                for i, field_name in enumerate(field_names):
                    fd_type = field_data_type
                    while '*' in field_name:
                        fd_type = 'POINTER(' + fd_type + ')'
                        field_name = field_name[1:]
                        self.importer.add('POINTER')
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
                    fields += [
                        FIELD_TEMPLATE.format(
                            field_name=field_name,
                            field_data_type=field_data_types[i]
                        )
                    ]
                field = ''

            if len(self.indent):
                for i, item in enumerate(sub_structures):
                    sub_structures[i] = '\n'.join(
                        itm[len(self.indent):] for itm in item.split('\n')
                    )

            self.all.add(cls_name)

            if cls_name in self.importer.allowed:
                self.importer.add(cls_name)
                template = ''

            elif anonymous:
                template = TEMPLATE_ANONYMOUS.format(
                    cls_name=cls_name,
                    fields='\n'.join(fields),
                    anonymous=''.join("'" + a + "', " for a in anonymous),
                    sub_structures=''.join(sub_structures)
                )

            elif sub_structures:
                template = TEMPLATE_SUBSTRUCTURES.format(
                    cls_name=cls_name,
                    fields='\n'.join(fields),
                    sub_structures=''.join(sub_structures)
                )

            else:
                template = TEMPLATE.format(
                    cls_name=cls_name,
                    fields='\n'.join(fields)
                )

            for i, var_name in enumerate(var_names[:]):
                if not var_name:
                    var_names.pop(i)
                    continue

                value = cls_name

                if var_name == value:
                    continue

                while var_name.startswith('*'):
                    value = 'POINTER(' + value + ')'
                    var_name = var_name[1:]
                    self.importer.add('POINTER')

                self.all.add(var_name)
                if var_name in self.importer.allowed:
                    self.importer.add(var_name)
                    continue

                var_names[i] = var_name + ' = ' + value

            if var_names:
                template += '\n'.join(var_names)
                yield line_num, '\n'.join(
                    self.indent + line for line in template.split('\n')
                ) + '\n\n'
            elif template:
                yield line_num, '\n'.join(
                    self.indent + line for line in template.split('\n')
                )


from structure import Structure
