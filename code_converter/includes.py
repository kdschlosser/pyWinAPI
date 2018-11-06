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

import os
from code_converter.comment import parse_comment

base_path = os.path.dirname(__file__)
module_path = os.path.abspath(os.path.join(base_path, '..'))


def locate_module(include, module_name, mods, path):

    module_name += '_h.py'

    files = os.listdir(path)

    if module_name in files or include in files:
        return mods + '.' + module_name[:-3]

    for f in files:
        new_path = os.path.join(path, f)
        if os.path.isdir(new_path):
            res = locate_module(
                include,
                module_name[:-3],
                mods + '.' + f,
                new_path
            )

            if res is not None:
                if res == mods + '.':
                    if path == base_path:
                        return None

                    return locate_module(
                        include,
                        module_name[:-3],
                        res,
                        os.path.split(path)[1]
                    )
                else:
                    return res

    if path == base_path:
        return None

    for i in range(1, 10):
        if mods == '.' * i:
            return mods + '.'


def parse_include(indent, include, path):
    if 'pack' in include:
        return

    include, comment = parse_comment(include)

    module_name = include.replace('#include', '').replace('# include', '')
    module_name = module_name.replace('<', '').replace('>', '').strip()
    if module_name.endswith('.h'):
        module_name = module_name[:-2]

    module_name = module_name.replace('.', '_').replace('"', '').lower()

    if module_name.isdigit():
        module_name = '_' + module_name

    print(module_name)
    res = locate_module(include, module_name, '.', path)

    if res is not None:
        print('{0}from .{1} import *{2}'.format(indent, res, comment))

