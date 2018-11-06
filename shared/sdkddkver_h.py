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

from pyWinAPI import *


# from pyWinAPI.um.icucommon_h import *

_INC_SDKDDKVER = True

_WIN32_WINNT_NT4 = 0x0400
_WIN32_WINNT_WIN2K = 0x0500
_WIN32_WINNT_WINXP = 0x0501
_WIN32_WINNT_WS03 = 0x0502
_WIN32_WINNT_WIN6 = 0x0600
_WIN32_WINNT_VISTA = 0x0600
_WIN32_WINNT_WS08 = 0x0600
_WIN32_WINNT_LONGHORN = 0x0600
_WIN32_WINNT_WIN7 = 0x0601
_WIN32_WINNT_WIN8 = 0x0602
_WIN32_WINNT_WINBLUE = 0x0603
_WIN32_WINNT_WINTHRESHOLD = 0x0A00 # ABRACADABRA_THRESHOLD
_WIN32_WINNT_WIN10 = 0x0A00 # ABRACADABRA_THRESHOLD
_WIN32_WINNT_WIN10_TH2 = _WIN32_WINNT_WIN10
_WIN32_WINNT_WIN10_RS1 = _WIN32_WINNT_WIN10

# //
# // _WIN32_IE_ version constants
# //
_WIN32_IE_IE20 = 0x0200
_WIN32_IE_IE30 = 0x0300
_WIN32_IE_IE302 = 0x0302
_WIN32_IE_IE40 = 0x0400
_WIN32_IE_IE401 = 0x0401
_WIN32_IE_IE50 = 0x0500
_WIN32_IE_IE501 = 0x0501
_WIN32_IE_IE55 = 0x0550
_WIN32_IE_IE60 = 0x0600
_WIN32_IE_IE60SP1 = 0x0601
_WIN32_IE_IE60SP2 = 0x0603
_WIN32_IE_IE70 = 0x0700
_WIN32_IE_IE80 = 0x0800
_WIN32_IE_IE90 = 0x0900
_WIN32_IE_IE100 = 0x0A00
_WIN32_IE_IE110 = 0x0A00  # ABRACADABRA_THRESHOLD #

# //
# // IE <-> OS version mapping
# //
# // NT4 supports IE versions 2.0 -> 6.0 SP1
_WIN32_IE_NT4 = _WIN32_IE_IE20
_WIN32_IE_NT4SP1 = _WIN32_IE_IE20
_WIN32_IE_NT4SP2 = _WIN32_IE_IE20
_WIN32_IE_NT4SP3 = _WIN32_IE_IE302
_WIN32_IE_NT4SP4 = _WIN32_IE_IE401
_WIN32_IE_NT4SP5 = _WIN32_IE_IE401
_WIN32_IE_NT4SP6 = _WIN32_IE_IE50

# // Win98 supports IE versions 4.01 -> 6.0 SP1
_WIN32_IE_WIN98 = _WIN32_IE_IE401

# // Win98SE supports IE versions 5.0 -> 6.0 SP1
_WIN32_IE_WIN98SE = _WIN32_IE_IE50

# // WinME supports IE versions 5.5 -> 6.0 SP1
_WIN32_IE_WINME = _WIN32_IE_IE55

# // Win2k supports IE versions 5.01 -> 6.0 SP1
_WIN32_IE_WIN2K = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP1 = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP2 = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP3 = _WIN32_IE_IE501
_WIN32_IE_WIN2KSP4 = _WIN32_IE_IE501
_WIN32_IE_XP = _WIN32_IE_IE60
_WIN32_IE_XPSP1 = _WIN32_IE_IE60SP1
_WIN32_IE_XPSP2 = _WIN32_IE_IE60SP2
_WIN32_IE_WS03 = 0x0602
_WIN32_IE_WS03SP1 = _WIN32_IE_IE60SP2
_WIN32_IE_WIN6 = _WIN32_IE_IE70
_WIN32_IE_LONGHORN = _WIN32_IE_IE70
_WIN32_IE_WIN7 = _WIN32_IE_IE80
_WIN32_IE_WIN8 = _WIN32_IE_IE100
_WIN32_IE_WINBLUE = _WIN32_IE_IE100
_WIN32_IE_WINTHRESHOLD = _WIN32_IE_IE110 # ABRACADABRA_THRESHOLD
_WIN32_IE_WIN10 = _WIN32_IE_IE110 # ABRACADABRA_THRESHOLD

# //
# // NTDDI version constants
# //
NTDDI_WIN2K = 0x05000000
NTDDI_WIN2KSP1 = 0x05000100
NTDDI_WIN2KSP2 = 0x05000200
NTDDI_WIN2KSP3 = 0x05000300
NTDDI_WIN2KSP4 = 0x05000400
#
NTDDI_WINXP = 0x05010000
NTDDI_WINXPSP1 = 0x05010100
NTDDI_WINXPSP2 = 0x05010200
NTDDI_WINXPSP3 = 0x05010300
NTDDI_WINXPSP4 = 0x05010400

NTDDI_WS03 = 0x05020000
NTDDI_WS03SP1 = 0x05020100
NTDDI_WS03SP2 = 0x05020200
NTDDI_WS03SP3 = 0x05020300
NTDDI_WS03SP4 = 0x05020400

NTDDI_WIN6 = 0x06000000
NTDDI_WIN6SP1 = 0x06000100
NTDDI_WIN6SP2 = 0x06000200
NTDDI_WIN6SP3 = 0x06000300
NTDDI_WIN6SP4 = 0x06000400

NTDDI_VISTA = NTDDI_WIN6
NTDDI_VISTASP1 = NTDDI_WIN6SP1
NTDDI_VISTASP2 = NTDDI_WIN6SP2
NTDDI_VISTASP3 = NTDDI_WIN6SP3
NTDDI_VISTASP4 = NTDDI_WIN6SP4

#
# #define NTDDI_LONGHORN  NTDDI_VISTA
#
NTDDI_WS08 = NTDDI_WIN6SP1
NTDDI_WS08SP2 = NTDDI_WIN6SP2
NTDDI_WS08SP3 = NTDDI_WIN6SP3
NTDDI_WS08SP4 = NTDDI_WIN6SP4
NTDDI_WIN7 = 0x06010000
NTDDI_WIN8 = 0x06020000
NTDDI_WINBLUE = 0x06030000
NTDDI_WINTHRESHOLD = 0x0A000000 # ABRACADABRA_THRESHOLD
NTDDI_WIN10 = 0x0A000000 # ABRACADABRA_THRESHOLD
NTDDI_WIN10_TH2 = 0x0A000001 # ABRACADABRA_WIN10_TH2
NTDDI_WIN10_RS1 = 0x0A000002 # ABRACADABRA_WIN10_RS1
NTDDI_WIN10_RS2 = 0x0A000003 # ABRACADABRA_WIN10_RS2
NTDDI_WIN10_RS3 = 0x0A000004 # ABRACADABRA_WIN10_RS3
NTDDI_WIN10_RS4 = 0x0A000005 # ABRACADABRA_WIN10_RS4
WDK_NTDDI_VERSION = NTDDI_WIN10_RS4 # ABRACADABRA_WIN10_RS4
# //
# // masks for version macros
# //
OSVERSION_MASK = 0xFFFF0000
SPVERSION_MASK = 0x0000FF00
SUBVERSION_MASK = 0x000000FF

# //
# // macros to extract various version fields from the NTDDI version
# //


def OSVER(Version):
    return Version & OSVERSION_MASK


def SPVER(Version):
    return (Version & SPVERSION_MASK) >> 8


def UBVER(Version):
    return Version & SUBVERSION_MASK


if defined(DECLSPEC_DEPRECATED_DDK):
    DECLSPEC_DEPRECATED_DDK_WIN6 = None

    # // deprecate in 2k or later
    if NTDDI_VERSION >= NTDDI_WIN2K:
        DECLSPEC_DEPRECATED_DDK_WIN2K = DECLSPEC_DEPRECATED_DDK

    # // deprecate in XP or later
    if NTDDI_VERSION >= NTDDI_WINXP:
        DECLSPEC_DEPRECATED_DDK_WINXP = DECLSPEC_DEPRECATED_DDK

    # // deprecate in WS03 or later
    if NTDDI_VERSION >= NTDDI_WS03:
        DECLSPEC_DEPRECATED_DDK_WIN2003 = DECLSPEC_DEPRECATED_DDK

    # // deprecate in WIN6 or later
    if NTDDI_VERSION >= NTDDI_WIN6:
        DECLSPEC_DEPRECATED_DDK_WIN6 = DECLSPEC_DEPRECATED_DDK

    DECLSPEC_DEPRECATED_DDK_LONGHORN = (
        DECLSPEC_DEPRECATED_DDK_WIN6
    )


# //
# // if versions aren't already defined, default to most current
# //
def NTDDI_VERSION_FROM_WIN32_WINNT2(ver):
    return ver


def NTDDI_VERSION_FROM_WIN32_WINNT(ver):
    return NTDDI_VERSION_FROM_WIN32_WINNT2(ver)


if not defined(_WIN32_WINNT):
    _WIN32_WINNT = 0x0A00


if not defined(NTDDI_VERSION):
    if defined(_WIN32_WINNT):
        if _WIN32_WINNT <= _WIN32_WINNT_WINBLUE:
            # // set NTDDI_VERSION based on _WIN32_WINNT
            NTDDI_VERSION = NTDDI_VERSION_FROM_WIN32_WINNT(
                _WIN32_WINNT
            )
        elif _WIN32_WINNT >= _WIN32_WINNT_WIN10:
            # // set NTDDI_VERSION to default to WDK_NTDDI_VERSION
            NTDDI_VERSION = WDK_NTDDI_VERSION
    else:
        # // set NTDDI_VERSION to default to latest if _WIN32_WINNT isn't set
        NTDDI_VERSION = 0x0A000005


if not defined(WINVER):
    if defined(_WIN32_WINNT):
        # // set WINVER based on _WIN32_WINNT
        WINVER = _WIN32_WINNT
    else:
        WINVER = 0x0A00


if not defined(_WIN32_IE):
    if defined(_WIN32_WINNT):
        # // set _WIN32_IE based on _WIN32_WINNT
        if _WIN32_WINNT <= _WIN32_WINNT_NT4:
            _WIN32_IE = _WIN32_IE_IE50
        elif _WIN32_WINNT <= _WIN32_WINNT_WIN2K:
            _WIN32_IE = _WIN32_IE_IE501
        elif _WIN32_WINNT <= _WIN32_WINNT_WINXP:
            _WIN32_IE = _WIN32_IE_IE60
        elif _WIN32_WINNT <= _WIN32_WINNT_WS03:
            _WIN32_IE = _WIN32_IE_WS03
        elif _WIN32_WINNT <= _WIN32_WINNT_VISTA:
            _WIN32_IE = _WIN32_IE_LONGHORN
        elif _WIN32_WINNT <= _WIN32_WINNT_WIN7:
            _WIN32_IE = _WIN32_IE_WIN7
        elif _WIN32_WINNT <= _WIN32_WINNT_WIN8:
            _WIN32_IE = _WIN32_IE_WIN8
        else:
            _WIN32_IE = 0x0A00
    else:
        _WIN32_IE = 0x0A00

# //
# // Sanity check for compatible versions
# //
if (
    defined(_WIN32_WINNT) and
    not defined(MIDL_PASS) and
    not defined(RC_INVOKED)
):

    if defined(WINVER) and (WINVER < 0x0400) and (_WIN32_WINNT > 0x0400):
        raise RuntimeError(
            "WINVER setting conflicts with _WIN32_WINNT setting"
        )

    if (
        (OSVERSION_MASK & NTDDI_VERSION) == NTDDI_WIN2K and
        _WIN32_WINNT != _WIN32_WINNT_WIN2K
    ):
        raise RuntimeError(
            'NTDDI_VERSION setting conflicts with _WIN32_WINNT setting'
        )

    if (
        (OSVERSION_MASK & NTDDI_VERSION) == NTDDI_WINXP and
        _WIN32_WINNT != _WIN32_WINNT_WINXP
    ):
        raise RuntimeError(
            'NTDDI_VERSION setting conflicts with _WIN32_WINNT setting'
        )

    if (
        (OSVERSION_MASK & NTDDI_VERSION) == NTDDI_WS03 and
        _WIN32_WINNT != _WIN32_WINNT_WS03
    ):
        raise RuntimeError(
            'NTDDI_VERSION setting conflicts with _WIN32_WINNT setting'
        )

    if (
        (OSVERSION_MASK & NTDDI_VERSION) == NTDDI_VISTA and
        _WIN32_WINNT != _WIN32_WINNT_VISTA
    ):
        raise RuntimeError(
            'NTDDI_VERSION setting conflicts with _WIN32_WINNT setting'
        )

    if (
        _WIN32_WINNT < _WIN32_WINNT_WIN2K and
        _WIN32_IE > _WIN32_IE_IE60SP1
    ):
        raise RuntimeError(
            '_WIN32_WINNT settings conflicts with _WIN32_IE setting'
        )

__all__ = (
    'NTDDI_VERSION_FROM_WIN32_WINNT', 'NTDDI_VERSION_FROM_WIN32_WINNT2',
    'NTDDI_VISTA', 'NTDDI_VISTASP1', 'NTDDI_VISTASP2', 'NTDDI_VISTASP3',
    'NTDDI_VISTASP4', 'NTDDI_WIN10', 'NTDDI_WIN10_RS1', 'NTDDI_WIN10_RS2',
    'NTDDI_WIN10_RS3', 'NTDDI_WIN10_RS4', 'NTDDI_WIN10_TH2', 'NTDDI_WIN6',
    'NTDDI_WIN2K', 'NTDDI_WIN2KSP1', 'NTDDI_WIN2KSP2', 'NTDDI_WIN2KSP3',
    'NTDDI_WIN2KSP4', 'NTDDI_WIN6SP1', 'NTDDI_WIN6SP2', 'NTDDI_WIN6SP3',
    'NTDDI_WIN6SP4', 'NTDDI_WIN7', 'NTDDI_WIN8', 'NTDDI_WINBLUE', 'OSVER',
    'NTDDI_WINTHRESHOLD', 'NTDDI_WINXP', 'NTDDI_WINXPSP1', 'NTDDI_WS03',
    'NTDDI_WINXPSP2', 'NTDDI_WINXPSP3', 'NTDDI_WINXPSP4', 'NTDDI_WS03SP1',
    'NTDDI_WS03SP2', 'NTDDI_WS03SP3', 'NTDDI_WS03SP4', 'NTDDI_WS08',
    'NTDDI_WS08SP2', 'NTDDI_WS08SP3', 'NTDDI_WS08SP4', 'OSVERSION_MASK',
    'SPVER', 'SPVERSION_MASK', 'SUBVERSION_MASK', 'UBVER', '_WIN32_IE_XP',
    'WDK_NTDDI_VERSION', '_INC_SDKDDKVER', '_WIN32_IE_IE100',
    '_WIN32_IE_IE110', '_WIN32_IE_IE20', '_WIN32_IE_IE30',
    '_WIN32_IE_IE302', '_WIN32_IE_IE40', '_WIN32_IE_IE401',
    '_WIN32_IE_IE50', '_WIN32_IE_IE501', '_WIN32_IE_IE55',
    '_WIN32_IE_IE60', '_WIN32_IE_IE60SP1', '_WIN32_IE_IE60SP2',
    '_WIN32_IE_IE70', '_WIN32_IE_IE80', '_WIN32_IE_IE90', '_WIN32_IE_NT4',
    '_WIN32_IE_LONGHORN', '_WIN32_IE_NT4SP1', '_WIN32_IE_NT4SP2',
    '_WIN32_IE_NT4SP3', '_WIN32_IE_NT4SP4', '_WIN32_IE_NT4SP5',
    '_WIN32_IE_NT4SP6', '_WIN32_IE_WIN10', '_WIN32_IE_WIN2K',
    '_WIN32_IE_WIN2KSP1', '_WIN32_IE_WIN2KSP2', '_WIN32_IE_WIN2KSP3',
    '_WIN32_IE_WIN2KSP4', '_WIN32_IE_WIN6', '_WIN32_IE_WIN7',
    '_WIN32_IE_WIN8', '_WIN32_IE_WIN98', '_WIN32_IE_WIN98SE',
    '_WIN32_IE_WINBLUE', '_WIN32_IE_WINME', '_WIN32_IE_WINTHRESHOLD',
    '_WIN32_IE_WS03', '_WIN32_IE_WS03SP1', '_WIN32_IE_XPSP1',
    '_WIN32_IE_XPSP2', '_WIN32_WINNT_WIN10_RS1', '_WIN32_WINNT_WIN10_TH2',
)

from um.icu_h import *