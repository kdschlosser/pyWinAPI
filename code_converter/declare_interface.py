# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2018 EventGhost Project <http://eventghost.net/>
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

from __future__ import print_function
from comment import parse_comment, equalize_width
from utils import process_param

PARAM_TEMPLATE = '''{indent}        ({data_type}, '{param_name}')'''
IID_TEMPLATE = '''{indent}{cls_name}._iid_ = IID_{cls_name}'''
STDMETHOD_TEMPLATE = '''{indent}    STDMETHOD('{method}')('''


def parse_declare_interface(indent, data):
    skip_until = None

    output = []

    for i, line in enumerate(data):
        if skip_until is not None:
            if i <= skip_until:
                continue
            skip_until = None

        line = line.strip()

        comment_line, comment = parse_comment(line)
        if not comment_line and comment:
            comment = equalize_width(indent, comment)
            output += [comment]
            continue

        if comment_line is None and comment is None:
            skip_until = i
            comments = []
            for j, d in enumerate(data[i:]):
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
            output += [comment]
            continue

        line = comment_line

        if line.startswith('DECLARE_INTERFACE_'):
            cls_name = line.split('(')[-1]
            cls_name = cls_name.split(',', 1)[0]
            cls_name = cls_name.replace(')', '').strip()
            output += [IID_TEMPLATE.format(indent=indent, cls_name=cls_name)]
            line = line.replace('{', '').strip()
            line = line.replace('IUnknown', 'comtypes.IUnknown')
            output += [indent + line + '(']
            if comment:
                comment = equalize_width(indent + '    ', comment)
                output += [comment]
            continue

        elif line.startswith('STDMETHOD'):
            if 'QueryInterface)' in line or 'AddRef)' in line or 'Release)':
                continue

            skip_until = i
            method = line

            next_skip_until = None
            param_comments = []

            while not method.endswith(';'):
                if next_skip_until is not None:
                    if next_skip_until == 0:
                        next_skip_until = None
                    else:
                        next_skip_until -= 1
                        skip_until += 1
                        continue

                comment_line, comment = parse_comment(
                    data[skip_until + 1].strip()
                )

                if not comment_line and comment:
                    comment = equalize_width(indent + '        ', comment)
                    param_comments += [comment + '\n']
                    skip_until += 1
                    continue

                if comment_line is None and comment is None:
                    next_skip_until = 1
                    comments = []
                    for j, d in enumerate(data[i:]):
                        next_skip_until += 1
                        skip_until += 1
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
                    comment = equalize_width(
                        indent + '        ',
                        ' '.join(comments)
                    )
                    param_comments += [comment]
                    continue

                if comment:
                    comment = equalize_width(indent + '        ', comment)
                    param_comments += [comment]
                else:
                    param_comments += ['']

                comment_line = comment_line.strip()

                skip_until += 1

                if (
                    comment_line.endswith(';') or
                    (' ' in comment_line and '(' not in comment_line)
                ):
                    method += ' ' + comment_line

            method_name, method = method.split(')', 1)
            method_name = method_name.split('(')[-1].strip()
            method = method.rsplit(')', 1)[0]
            method = method.split('(', 1)[-1].strip()
            import sys

            sys.stderr.write('DEFINE INTERFACE: ' + method + '\n')

            while '(' in method:
                tmp1, tmp2 = method.split('(', 1)
                tmp1 = tmp1.rsplit(' ', 1)[0]
                tmp2 = tmp2.split(')', 1)[-1]

                method = tmp1 + ' ' + tmp2

            sys.stderr.write('DEFINE INTERFACE: ' + method + '\n')

            params = list(
                itm.strip() for itm in method.split(',')
                if itm.strip()
            )

            sys.stderr.write('DEFINE INTERFACE: ' + str(params) + '\n')

            found_params = []
            for param in params:
                param = param.rsplit(')')[-1]

                try:
                    data_type, param_name = param.rsplit(' ', 1)
                except ValueError:
                    import sys
                    sys.stderr.write('PARAM_ERROR: ' + param + '\n')
                    raise

                param_name = param_name.strip()
                data_type = data_type.replace(' ', '')
                found_params += [process_param(param_name, data_type)]

            sys.stderr.write('DEFINE INTERFACE: ' + str(found_params) + '\n')

            output += [
                STDMETHOD_TEMPLATE.format(indent=indent, method=method_name)
            ]

            for j, param in enumerate(found_params):
                param_name, data_type = param
                data_type = data_type.replace('_Inout_', '')
                try:
                    comment = param_comments[j]
                    if comment:
                        output += [comment]
                except IndexError:
                    pass

                template = PARAM_TEMPLATE.format(
                    indent=indent,
                    data_type=data_type,
                    param_name=param_name
                )

                if j != len(found_params) - 1:
                    template += ','
                output += [template]

            output += [indent + '    ),']

        else:
            if comment:
                comment = equalize_width(indent + '    ', comment)
                output += [comment]

    output = '\n'.join(output)[:-1]
    output += '\n' + indent + ')' + '\n'
    print(output)
