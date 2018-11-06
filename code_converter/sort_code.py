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


in_path = r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.17134.0'
out_path = r'C:\Users\Administrator\Desktop\New folder (30)'

import os


def iter_path(p, indent=''):
    files = os.listdir(p)
    root = p.replace(in_path, out_path)
    if os.path.isdir(p) and not os.path.exists(root):
        os.makedirs(root)
    print indent + p

    for f in files:
        in_file = os.path.join(p, f)
        out_file = os.path.join(root, f)

        if os.path.isdir(in_file):
            iter_path(in_file, indent + '    ')
        elif f.endswith('.h'):
            print indent + '    ' + f
            with open(in_file, 'r') as f1:
                with open(out_file, 'w') as f2:
                    f2.write(str(SortCode(f1.read().split('\n'))))
        else:
            print indent + '    ' + f
            with open(in_file, 'r') as f1:
                with open(out_file, 'w') as f2:
                    f2.write(f1.read())


iter_path(in_path)



