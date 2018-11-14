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

import sys
import platform
from collections import OrderedDict

WINDOWS_VERSIONS = OrderedDict()
WINDOWS_VERSIONS["XP"] = [[5, 1], [5, 2]]
WINDOWS_VERSIONS["XP32"] = [5, 1]
WINDOWS_VERSIONS["XP64"] = [5, 2]
WINDOWS_VERSIONS["VISTA"] = [6, 0]
WINDOWS_VERSIONS["7"] = [6, 1]
WINDOWS_VERSIONS["8"] = [[6, 2], [6, 3]]
WINDOWS_VERSIONS["80"] = [6, 2]
WINDOWS_VERSIONS["81"] = [6, 3]
WINDOWS_VERSIONS["10"] = [10, 0]


def _compare(opp, other):
    if isinstance(other, int):
        other = str(other)
    else:
        other = other.upper()

    if other not in WINDOWS_VERSIONS.keys():
        raise WindowsVersionError(other)

    ver = platform.version().split('.')
    this = [int(ver[0]), int(ver[1])]

    versions = WINDOWS_VERSIONS[other]
    if other not in ("8", "XP"):
        versions = [versions]

    if opp == '>':
        return any(this > version for version in versions)
    elif opp == '<':
        return any(this < version for version in versions)
    elif opp == '<=':
        return any(this <= version for version in versions)
    elif opp == '>=':
        return any(this >= version for version in versions)
    elif opp == '==':
        return any(this == version for version in versions)
    elif opp == '!=':
        return any(this != version for version in versions)


class WindowsVersionError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return (
            "'{0}' is not in the list of supported values:\n"
            "\t{1}\n".format(self.msg, ", ".join(WINDOWS_VERSIONS.keys()))
        )


class WindowsVersion(object):
    """
    A convenience module for checking the windows version.

    In addition to the *IsXY()* methods, you can use comparison like this:

    ``eg.WindowsVersion OPERATOR "KEY"``

    ``OPERATOR`` is one of ``<``, ``<=``, ``==``, ``!=``, ``>=``, ``>``

    +-----------+--------------------------------------+
    | ``KEY``   | Windows version(s)                   |
    +===========+======================================+
    | ``XP``    | *all of XP32 and XP64*               |
    +-----------+--------------------------------------+
    | ``XP32``  | Windows XP,                          |
    |           | Windows XP 64-Bit Edition,           |
    |           | Windows Tablet PC,                   |
    |           | Windows Media Center Edition 2002,   |
    |           | Windows Media Center Edition 2004,   |
    |           | Windows Media Center Edition 2005    |
    +-----------+--------------------------------------+
    | ``XP64``  | Windows XP Professional x64 Edition, |
    |           | Windows Server 2003,                 |
    |           | Windows Server 2003 R2               |
    +-----------+--------------------------------------+
    | ``Vista`` | Windows Vista,                       |
    |           | Windows Server 2008                  |
    +-----------+--------------------------------------+
    | ``7``     | Windows 7,                           |
    |           | Windows Server 2008 R2               |
    +-----------+--------------------------------------+
    | ``8``     | *all of 80 and 81*                   |
    +-----------+--------------------------------------+
    | ``80``    | Windows 8,                           |
    |           | Windows Server 2012,                 |
    |           | Windows RT                           |
    +-----------+--------------------------------------+
    | ``81``    | Windows 8.1,                         |
    |           | Windows 2012 R2,                     |
    |           | Windows RT 8.1                       |
    +-----------+--------------------------------------+
    | ``10``    | Windows 10,                          |
    |           | Windows Server 2016                  |
    +-----------+--------------------------------------+

    |

    .. The above line gives some extra space after the table in the helpfile.
       References:
           https://msdn.microsoft.com/en-us/library/windows/desktop/ms724832(v=vs.85).aspx
           https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions
           http://www.gaijin.at/lstwinver.php
    """

    def __eq__(self, other):
        # type: (str) -> bool
        """
        Checks if the installed Windows version is equal
        to *other* windows version.

        :type other: str
        :rtype: bool
        """
        return _compare('==', other)

    def __ne__(self, other):
        # type: (str) -> bool
        """
        Checks if the installed Windows version is not equal
        to *other* windows version.

        :type other: str
        :rtype: bool
        """
        return _compare('!=', other)

    def __gt__(self, other):
        # type: (str) -> bool
        """
        Checks if the installed Windows version is newer
        than *other* windows version.

        :type other: str
        :rtype: bool
        """
        return _compare('>', other)

    def __ge__(self, other):
        # type: (str) -> bool
        """
        Checks if the installed Windows version is newer or equal
        than *other* windows version.

        :type other: str
        :rtype: bool
        """
        return _compare('>=', other)

    def __lt__(self, other):
        # type: (str) -> bool
        """
        Checks if the installed Windows version is older
        than *other* windows version.

        :type other: str
        :rtype: bool
        """
        return _compare('<', other)

    def __le__(self, other):
        # type: (str) -> bool
        """
        Checks if the installed Windows version is older or equal
        than *other* windows version.

        :type other: str
        :rtype: bool
        """
        return _compare('<=', other)

    def __str__(self):
        # type: () -> str
        """
        Gives a string with the word 'Windows' followed by the (full)
        version number for the installed Windows.

        :rtype: str
        """
        return "{0} {1}".format(
            platform.system(),
            platform.version()
        )

    @property
    def version(self):
        # type: () -> list
        """
        Return the major and minor version number of the installed Windows.

        :rtype: list
        :return: [major, minor]

        """
        return platform.version().split('.')[:2]

    @property
    def is_xp(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows XP x86
        * Windows XP x64
        * Windows Server 2003
        * Windows 2003 R2
        * Windows Tablet PC
        * Windows Media Center Edition 2002
        * Windows Media Center Edition 2004
        * Windows Media Center Edition 2005

        :rtype: bool
        """
        return _compare('==', "XP")

    @property
    def is_xp32(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows XP x86
        * Windows Tablet PC
        * Windows Media Center Edition 2002
        * Windows Media Center Edition 2004
        * Windows Media Center Edition 2005

        :rtype: bool
        """
        return _compare('==', "XP32")

    @property
    def is_xp64(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows XP x64
        * Windows Server 2003
        * Windows 2003 R2

        :rtype: bool
        """
        return _compare('==', "XP64")

    @property
    def is_vista(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows Vista
        * Windows Server 2008

        :rtype: bool
        """
        return _compare('==', "Vista")

    @property
    def is_7(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows 7
        * Windows Server 2008 R2

        :rtype: bool
        """
        return _compare('==', "7")

    @property
    def is_8(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows 8
        * Windows 8.1
        * Windows Server 2012
        * Windows 2012 R2
        * Windows RT
        * Windows RT 8.1

        :rtype: bool
        """
        return _compare('==', "8")

    @property
    def is_80(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows 8
        * Windows Server 2012
        * Windows RT

        :rtype: bool
        """
        return _compare('==', "80")

    @property
    def is_81(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows 8.1
        * Windows 2012 R2
        * Windows RT 8.1

        :rtype: bool
        """
        return _compare('==', "81")

    @property
    def is_10(self):
        # type: () -> bool
        """
        Checks if installed Windows version is one of:

        * Windows 10
        * Windows Server 2016

        :rtype: bool
        """
        return _compare('==', "10")


windows_version = WindowsVersion()

_WIN32_WINNT_NT4 = 0x0400 # Windows NT 4.0
_WIN32_WINNT_WIN2K = 0x0500 # Windows 2000
_WIN32_WINNT_WINXP = 0x0501 # Windows XP
_WIN32_WINNT_WS03 = 0x0502 # Windows Server 2003
_WIN32_WINNT_WIN6 = 0x0600 # Windows Vista
_WIN32_WINNT_VISTA = 0x0600 # Windows Vista
_WIN32_WINNT_WS08 = 0x0600 # Windows Server 2008
_WIN32_WINNT_LONGHORN = 0x0600 # Windows Vista
_WIN32_WINNT_WIN7 = 0x0601 # Windows 7
_WIN32_WINNT_WIN8 = 0x0602 # Windows 8
_WIN32_WINNT_WINBLUE = 0x0603 # Windows 8.1
_WIN32_WINNT_WINTHRESHOLD = 0x0A00 # Windows 10
_WIN32_WINNT_WIN10 = 0x0A00 # Windows 10
_WIN32_WINNT_WIN10_RS2 = _WIN32_WINNT_WIN10
_WIN32_WINNT_WIN10_RS3 = _WIN32_WINNT_WIN10

if windows_version.is_xp:
    _WIN32_WINNT = _WIN32_WINNT_WINXP

elif windows_version.is_vista:
    _WIN32_WINNT = _WIN32_WINNT_VISTA

elif windows_version.is_7:
    _WIN32_WINNT = _WIN32_WINNT_WIN7

elif windows_version.is_8:
    _WIN32_WINNT = _WIN32_WINNT_WIN8

elif windows_version.is_10:
    _WIN32_WINNT = _WIN32_WINNT_WIN10

else:
    _WIN32_WINNT = None


if sys.maxsize > 2**32:
    _M_AMD64 = 1
    _M_X64 = 1
    __64BIT__ = 1
    _WIN64 = 1
    _AMD64_ = 1
    _X86_ = None
else:
    _M_AMD64 = None
    _M_X64 = None
    __64BIT__ = None
    _WIN64 = None
    _AMD64_ = None
    _X86_ = 1


_WIN32 = True
_WINRT_DLL = True
__AVX__ = True
__AVX2__ = True
_MSC_VER = 1915
MAX_PATH = 255

_M_IX86_FP = not sys.maxsize > 2**32

DECLSPEC_DEPRECATED_DDK = None
MIDL_PASS = None
RC_INVOKED = None
NTDDI_VERSION = None
WINVER = None
_WIN32_IE = None
MOFCOMP_PASS = None
_INC_WINAPIFAMILY = None
_WIN32_WINDOWS = None
__LPGUID_DEFINED__ = None

WINAPI_FAMILY = None
WINAPI_PARTITION_DESKTOP = None
WINAPI_PARTITION_APP = None
WINAPI_PARTITION_PC_APP = None
WINAPI_PARTITION_PHONE_APP = None
WINAPI_PARTITION_SYSTEM = None
WINAPI_PARTITION_SERVER = None
_INC_WINPACKAGEFAMILY = None
__cplusplus = None
CINTERFACE = 1
_NTDDK_ = None
_NTHAL_ = None
_MINWINBASE_ = None
GUID_DEFS_ONLY = None
NO_GUID_DEFS = None
__WINDOWS_DONT_DISABLE_PRAGMA_PACK_WARNING__ = None
DUMMYUNIONNAME = 0
_DEBUG = None
_HRESULT_DEFINED = None

_FILETIME_ = None
_MAC = None
UNICODE = 1


def defined(macro):
    return macro is not None


if __name__ == '__main__':
    pyWinAPI_module = sys.modules['__main__']
    pyWinAPI_module.__name__ = 'pyWinAPI'
    pyWinAPI_module.__package__ = ''
    sys.modules['pyWinAPI'] = pyWinAPI_module
else:
    pyWinAPI_module = sys.modules[__name__]

del OrderedDict
del platform
del sys
del _compare
del WindowsVersionError
del WindowsVersion
del windows_version
del WINDOWS_VERSIONS


__all__ = (
    'DECLSPEC_DEPRECATED_DDK', 'MIDL_PASS', 'RC_INVOKED', '_MSC_VER',
    '_M_AMD64', '_M_IX86_FP', '_M_X64', '_WIN32', '_WIN32_WINNT', 'defined',
    '_WIN32_WINNT_LONGHORN', '_WIN32_WINNT_NT4',  '__AVX__', '__64BIT__',
    '_WIN32_WINNT_VISTA', '_WIN32_WINNT_WIN10', '_WIN32_WINNT_WIN2K', 'WINVER',
    '_WIN32_WINNT_WIN6', '_WIN32_WINNT_WIN7', '_WIN32_WINNT_WIN8', '__AVX2__',
    '_WIN32_WINNT_WINBLUE', '_WIN32_WINNT_WINTHRESHOLD', '_WINRT_DLL',
    '_WIN32_WINNT_WINXP', '_WIN32_WINNT_WS03', '_WIN32_WINNT_WS08', '_WIN64',
    'NTDDI_VERSION', '_WIN32_IE', 'MOFCOMP_PASS', '_INC_WINAPIFAMILY',
    'WINAPI_FAMILY', 'WINAPI_PARTITION_DESKTOP', 'WINAPI_PARTITION_APP',
    'WINAPI_PARTITION_PC_APP', 'WINAPI_PARTITION_PHONE_APP', 'CINTERFACE',
    'WINAPI_PARTITION_SYSTEM', 'WINAPI_PARTITION_SERVER', '__cplusplus',
    '_INC_WINPACKAGEFAMILY', '_NTDDK_', '_NTHAL_', '_MINWINBASE_',
    '__WINDOWS_DONT_DISABLE_PRAGMA_PACK_WARNING__', '_FILETIME_', '_MAC',
    'UNICODE', 'GUID_DEFS_ONLY', 'NO_GUID_DEFS', 'MAX_PATH', '_WIN32_WINDOWS',
    '__LPGUID_DEFINED__', 'DUMMYUNIONNAME', '_DEBUG', '_HRESULT_DEFINED',
    '_AMD64_', '_X86_', '_WIN32_WINNT_WIN10_RS2', '_WIN32_WINNT_WIN10_RS3'
)

from shared.sdkddkver_h import * # NOQA
#
