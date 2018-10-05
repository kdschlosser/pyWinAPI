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

from .wtypes_h import (
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
    FILETIME,
    PFILETIME,
    LPFILETIME,
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
    ULONG,
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


__all__ = [
    'cdecl', 'pascal', 'far', 'near', 'NULL', 'PSZ', 'CDECL', 'CALLBACK',
    'WINAPI', 'WINAPIV', 'APIENTRY', 'APIPRIVATE', 'PASCAL', 'WINAPI_INLINE',
    'FAR', 'NEAR', 'WPARAM', 'LPARAM', 'LRESULT', 'SPHANDLE', 'LPHANDLE',
    'HGLOBAL', 'HLOCAL', 'GLOBALHANDLE', 'LOCALHANDLE', 'FARPROC', 'NEARPROC',
    'PROC', 'HKEY', 'PHKEY', 'HMETAFILE', 'HINSTANCE', 'HMODULE', 'HRGN',
    'HRSRC', 'HSPRITE', 'HLSURF', 'HSTR', 'HTASK', 'HWINSTA', 'HKL', 'HFILE',
    'FILETIME', 'PFILETIME', 'LPFILETIME', 'DWORD', 'BOOL', 'BYTE', 'WORD',
    'FLOAT', 'PFLOAT', 'PBOOL', 'INT', 'UINT', 'PUINT', 'ULONG', 'PULONG',
    'USHORT', 'PUSHORT', 'UCHAR', 'PUCHAR', 'ATOM', 'FALSE', 'TRUE', 'IN',
    'OUT', 'OPTIONAL', 'MAX_PATH', 'MAKEWORD', 'MAKELONG', 'LOWORD', 'HIWORD',
    'LOBYTE', 'HIBYTE',
]

