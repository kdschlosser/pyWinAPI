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

class Typedef(object):
    def __init__(self, importer, data):
        self.importer = importer
        self.lines = {}
        self.all = set()
        print "\n\n-- TYPDEF ---------------------------------------------\n\n"

        for i, line in enumerate(data[:]):
            if (
                line.startswith('typedef') and
                'union' not in line and
                'struct' not in line and
                'enum' not in line and
                not line.startswith('typedef INTerface') and
                line.rstrip().endswith(';')
            ):
                self.lines[i] = line
                print self.lines[i]

    def process(self):

        loaded = []

        for line_num, line in self.lines.items()[:]:
            line = line.replace('typedef', '').replace(';', '').strip()
            line = line.split(',')

            value, attrs = line[0].rsplit(' ', 1)

            attrs = [attrs] + line[1:]

            value = value.strip()
            value = value.split(' ')

            for i, val in enumerate(value[:]):

                if '__RPC_' in val:
                    value.pop(i)

            if len(value) > 1:
                for val in value:
                    if val not in loaded and not self.importer.add(val):
                        continue
                    else:
                        break
                else:
                    val = value[0]
            else:
                val = value[0]

            output = []
            if not val.endswith('A'):
                for attr in attrs:
                    attr = attr.strip()
                    if not attr:
                        continue

                    tmp_attr = attr
                    tmp_val = val
                    attr = attr.replace('*', '')

                    while tmp_attr.startswith('*'):
                        self.importer.add('POINTER')
                        tmp_attr = tmp_attr[1:]
                        tmp_val = 'POINTER(' + tmp_val + ')'

                    if attr == tmp_val:
                        continue

                    self.all.add(attr)
                    if attr in self.importer.allowed:
                        self.importer.add(attr)
                        continue

                    output += [attr + ' = ' + tmp_val]

                if output:
                    yield line_num, '\n'.join(output)
