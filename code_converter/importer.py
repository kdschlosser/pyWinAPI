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

TEMPLATE = '''from {module_name} import (
{imports}
)
'''

IMPORT_TEMPLATE = '''    {imprt},'''

import imp
import sys


base_path = os.path.dirname(__file__)
import_start = os.path.abspath(os.path.join(base_path, '..'))







class Importer(object):

    def __init__(self, module_name='wtypes_h', parent=None, path=None):
        self._allowed = []
        if 'pyWinAPI' not in sys.modules:
            res = imp.find_module('pyWinAPI', [os.path.split(path)[0]])
            mod = imp.load_module('pyWinAPI', *res)
            sys.modules['pyWinAPI'] = mod
        if path is not None:
            try:
                res = imp.find_module(module_name, [path])
                mod = imp.load_module('pyWinAPI.' + module_name, *res)
                sys.modules['pyWinAPI.' + module_name] = mod

                mod_path = os.path.join(path, module_name + '.py')
                if os.path.exists(mod_path):
                    mod = sys.modules['pyWinAPI.' + module_name]
                    namespace = mod.__dict__
                    self._allowed = list(
                        key for key in namespace.keys()
                        if not key.startswith('__')
                    )
            except ImportError:
                mod = __import__(module_name)
                namespace = mod.__dict__
                self._allowed = list(
                    key for key in namespace.keys()
                    if not key.startswith('__')
                )

        self.module_name = module_name
        self.parent = parent
        self.path = path
        self._modules = {}
        self._imports = []

        if module_name == 'wtypes_h':
            importer = self.add_importer('ntdef_h')
            self._allowed += importer.allowed[:]

    def process(self):
        if self._imports:
            imports = list(
                IMPORT_TEMPLATE.format(imprt=imprt) for imprt in self._imports
            )

            yield TEMPLATE.format(
                module_name=self.module_name, imports='\n'.join(imports)
            )

        elif self.module_name != 'wtypes_h':
            yield 'import ' + self.module_name + '\n'

        for importer in self._modules.values():
            for impt in importer.process():
                yield impt

    def add_importer(self, module_name):
        if module_name == self.module_name:
            return self

        if self.parent is not None:
            return self.parent.add_importer(module_name)

        for m_name, importer in self._modules.items():
            if m_name == module_name:
                return importer

        importer = Importer(module_name, self, path=self.path)
        self._modules[module_name] = importer

        return importer

    @property
    def allowed(self):
        return self._allowed

    def add(self, item):

        if item in self._imports:
            return True

        if item in self.allowed:
            self._imports += [item]
            return True

        return False

