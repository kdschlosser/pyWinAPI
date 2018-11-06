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

from __future__ import print_function, absolute_import
from code_converter.comment import parse_comment
import os
import atexit
from code_converter import known_defines

new_defines = []

module_name = ''

def save_defines():

    path = os.path.join(os.path.dirname(__file__), 'known_defines.py')
    with open(path, 'w') as f:
        printed_module_name = False
        for key, value in known_defines.__dict__.items():
            if isinstance(value, str) and value == 'NEW':
                if not printed_module_name:
                    printed_module_name = True
                    f.write('# ' + module_name + '\n')
                f.write(key + ' = None\n')


atexit.register(save_defines)


def parse_macro(indent, lne, macro=False):
    global line
    line, comment = parse_comment(lne)
    comment = comment.strip()
    line = line.strip()

    if comment:
        comment = ' ' + comment

    def set_pattern(repl, add):
        global line

        line = line.replace(repl, '').strip()

        if ' or ' in line:
            defines = list(d.strip() for d in line.split(' or '))
        elif ' and ' in line:
            defines = list(d.strip() for d in line.split(' and '))
        else:
            defines = [line]

        for define in defines:
            old_define = define
            open_brackets = ''
            while define.startswith('('):
                open_brackets += define[:1]
                define = define[1:]

            if not hasattr(known_defines, define):
                setattr(known_defines, define, 'NEW')

            define = open_brackets + add + define
            define += ')'
            line = line.replace(old_define, define)

    if line.startswith('#ifndef'):
        set_pattern('#ifndef', 'not defined(')
        if line.startswith('(') and line.endswith(')'):
            line = line[1:-1]

        new_line = 'if ' + line + ':'

        if macro:
            print(indent + new_line)
        else:
            print(indent + '    ' + new_line)
            return '', indent + '    '

    if line.startswith('#ifdef'):
        set_pattern('#ifdef', 'defined(')
        if line.startswith('(') and line.endswith(')'):
            line = line[1:-1]
        line = 'if ' + line + ':' + comment
        if macro:
            print(indent + line)
        else:
            print(indent + '    ' + line)
            return '', indent + '    '

    if (
        line.startswith('#elif') or
        line.startswith('#else') or
        line.startswith('#if')
    ):

        for item in ('#elif', '#if'):
            if line.startswith(item):
                line = line.replace(item, '').strip()

                if line.startswith('(') and line.endswith(')'):
                    line = line[1:-1]

                line = item + ' ' + line
                break

        line = line[1:] + ':' + comment

        if line.startswith('if'):
            if macro:
                print(indent + line)
            else:
                print(indent + '    ' + line)
                return '', indent + '    '
        else:
            if macro:
                print(indent[:-4] + line)
            else:
                print(indent + line)
                return '', indent

    if line.startswith('#endif'):
        if comment:
            print(indent + '# END IF ' + comment[2:])
        else:
            print(indent + '# END IF')
        return '', indent[:-4]

    return line, indent
