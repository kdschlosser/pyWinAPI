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


def equalize_width(indent, comment):
    saved_comments = []

    comments = comment.split('\n')

    for comment in comments:
        if not comment:
            continue



        comment = comment.replace('#', '').strip()
        comment = comment.replace('   ', ' ').replace('  ', ' ')
        o_len = len(comment)

        for line_char in ('*', '=', '-', '_', '#'):
            if line_char * o_len == comment:
                break
        else:
            line_char = None

        c_len = len(indent + '# ') + o_len
        if c_len <= 79:
            saved_comments += [indent + '# ' + comment]
        elif line_char is not None:
            saved_comments += [indent + '# ' + comment[:o_len - c_len]]
        else:
            quote_open = False
            brace_count = 0
            par_count = 0

            last_space = 0
            temp_comment = indent + '# '
            for i, char in enumerate(list(comment)):
                if char == '"':
                    quote_open = not quote_open
                elif char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                elif char == '(':
                    par_count += 1
                elif char == ')':
                    par_count -= 1
                elif (
                    char == ' ' and
                    not quote_open and
                    not brace_count and
                    not par_count
                ):
                    last_space = i + len(indent) + 2
                temp_comment += char
                if len(temp_comment) == 79 and last_space:
                    temp_comment = temp_comment[:last_space]
                    break
            comment = comment.replace(
                temp_comment[temp_comment.find('#') + 2:],
                ''
            )

            saved_comments += [(
                indent +
                temp_comment.strip() +
                '\n' +
                equalize_width(indent, '# ' + comment)
            )]

    return '\n'.join(saved_comments)


def parse_comment(line):

    if '//' in line and '/*' not in line and 'http://' not in line:
        try:
            temp_line, comment = line.split('//')
        except ValueError:
            temp_line = ''
            comment = line.strip()[2:].strip()

        temp_line = temp_line.strip()
        if comment:
            return temp_line, '# ' + comment
        else:
            return temp_line, ''

    elif '/*' in line and '*/' not in line:
        return None, None

    elif '*/' in line and '/*' not in line:
        return '', ''

    elif '/*' in line:

        indent_count = 0
        for char in list(line):
            if char != ' ':
                break
            indent_count += 1

        indent_count -= indent_count % 4
        indent = ' ' * indent_count
        line = line.replace('/**', '/*')
        line = line.replace('**/', '*/')
        line = line.replace('/*', '\n/*')
        line = line.replace('*/', '\n')
        lines = line.split('\n')
        new_lines = []
        comments = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith('/*'):
                comments += [line[2:].strip()]
            else:
                new_lines += [line]

        if new_lines:
            line = indent + ' '.join(new_lines)
        else:
            line = ''

        if comments:
            comment = indent + '# ' + ('\n' + indent + '# ').join(comments)
        else:
            comment = ''

        return line, comment

    return line, ''
