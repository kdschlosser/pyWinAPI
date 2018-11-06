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

from shared.wtypes_h import (
    cdecl,
    pascal,
    far,
    near,
    NULL,
    PSZ,
    CDECL,
    CALLBACK,
    WINAPI,
    WINAPIV,
    APIENTRY,
    APIPRIVATE,
    PASCAL,
    WINAPI_INLINE,
    FAR,
    NEAR,
    WPARAM,
    LPARAM,
    LRESULT,
    SPHANDLE,
    LPHANDLE,
    HGLOBAL,
    HLOCAL,
    GLOBALHANDLE,
    LOCALHANDLE,
    FARPROC,
    NEARPROC,
    PROC,
    HKEY,
    PHKEY,
    HMETAFILE,
    HINSTANCE,
    HMODULE,
    HRGN,
    HRSRC,
    HSPRITE,
    HLSURF,
    HSTR,
    HTASK,
    HWINSTA,
    HKL,
    HFILE,
    FILETIME as _FILETIME,
    PFILETIME as _PFILETIME,
    LPFILETIME as _LPFILETIME,
    DWORD,
    BOOL,
    BYTE,
    WORD,
    FLOAT,
    PFLOAT,
    PBOOL,
    INT,
    UINT,
    PUINT,
    ULONG as _ULONG,
    PULONG,
    USHORT,
    PUSHORT,
    UCHAR,
    PUCHAR,
    ATOM,
    LONG
)

FALSE = 0
TRUE = 1
IN = None
OUT = None
OPTIONAL = None
MAX_PATH = 260

FILETIME = _FILETIME
PFILETIME = _PFILETIME
LPFILETIME = _LPFILETIME
ULONG = _ULONG


def MAKEWORD(a, b):
    return WORD(((a & 0xff) | b & 0xff) << 8)


def MAKELONG(a, b):
    return LONG((a & 0xffff) | (b & 0xffff) << 16)


def LOWORD(l):
    return WORD(l & 0xffff)


def HIWORD(l):
    return WORD((l >> 16) & 0xffff)


def LOBYTE(w):
    return BYTE(w & 0xff)


def HIBYTE(w):
    return BYTE((w >> 8) & 0xff)

__all__ = (
    'APIENTRY', 'APIPRIVATE', 'ATOM', 'BOOL', 'BYTE', 'CALLBACK', 'CDECL',
    'DWORD', 'FALSE', 'FAR', 'FARPROC', 'FILETIME', 'FLOAT', 'HFILE',
    'GLOBALHANDLE', 'HGLOBAL', 'HIBYTE', 'HINSTANCE', 'HIWORD', 'HKEY',
    'HKL', 'HLOCAL', 'HLSURF', 'HMETAFILE', 'HMODULE', 'HRGN', 'HRSRC',
    'HSPRITE', 'HSTR', 'HTASK', 'HWINSTA', 'IN', 'INT', 'LOBYTE', 'LONG',
    'LOCALHANDLE', 'LOWORD', 'LPARAM', 'LPFILETIME', 'LPHANDLE', 'NEAR',
    'LRESULT', 'MAKELONG', 'MAKEWORD', 'MAX_PATH', 'NEARPROC', 'NULL',
    'OPTIONAL', 'OUT', 'PASCAL', 'PBOOL', 'PFILETIME', 'PFLOAT', 'PHKEY',
    'PROC', 'PSZ', 'PUCHAR', 'PUINT', 'PULONG', 'PUSHORT', 'SPHANDLE',
    'TRUE', 'UCHAR', 'UINT', 'ULONG', 'USHORT', 'WINAPI', 'WINAPIV',
    'WINAPI_INLINE', 'WORD', 'WPARAM', '_FILETIME', '_LPFILETIME', 'far',
    '_PFILETIME', '_ULONG', 'cdecl', 'near', 'pascal',
)

