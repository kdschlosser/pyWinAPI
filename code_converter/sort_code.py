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


# this module iterates over the sdk directory which is shown below in the
# "in_path", The out_path is one folder level down from this module. it will
# make a replica of the SDK folder at this location.
# this module opens up every .h file and indents the file based on the
# preprocessor syntax, #ifndef, #ifdef, #if, #elif and #else.
#
# By doing this it make it far easier to follow the nested
# preprocessor commands. It is with these commands where most of the issue
# arise from so being able to easily read the .h file to be able to fix a
# converted file is extremely important.

from __future__ import print_function, absolute_import
import os

in_path = r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.17134.0'
out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class SortCode(object):

    def __init__(self, data):
        if_count = 0
        lines = []

        for line in data:
            if line.strip().startswith('#'):
                cut_index = 1

                for char in list(line.strip())[1:]:
                    if not char == ' ':
                        break

                    cut_index += 1

                line = '#' + line.strip()[cut_index:]

            for item in ('#if', '#ifdef', '#ifndef'):
                if line.strip().startswith(item):
                    lines += ['    ' * if_count + line]
                    if_count += 1
                    break
            else:
                for item in ('#elif', '#else'):
                    if line.strip().startswith(item):
                        lines += ['    ' * (if_count - 1) + line]
                        break
                else:
                    if line.strip().startswith('#endif'):
                        if_count -= 1

                    lines += ['    ' * if_count + line]
        self.lines = lines

    def __str__(self):
        return '\n'.join(self.lines)


def iter_path(p, indent=''):
    files = os.listdir(p)
    root = p.replace(in_path, out_path)
    if os.path.isdir(p) and not os.path.exists(root):
        os.makedirs(root)
    print(indent + p)

    for f in files:
        in_file = os.path.join(p, f)
        out_file = os.path.join(root, f)

        if os.path.isdir(in_file):
            iter_path(in_file, indent + '    ')
        elif f.endswith('.h'):
            print(indent + '    ' + f)
            with open(in_file, 'r') as f1:
                with open(out_file, 'w') as f2:
                    f2.write(str(SortCode(f1.read().split('\n'))))
        else:
            print(indent + '    ' + f)
            with open(in_file, 'r') as f1:
                with open(out_file, 'w') as f2:
                    f2.write(f1.read())


iter_path(in_path)



