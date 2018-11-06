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

from shared.minwindef_h import (
    cdecl,
    pascal,
    far,
    near,
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
    FARPROC,
    NEARPROC,
    PROC,
    HLSURF,
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
    ATOM,
    MAX_PATH,
    FALSE,
    TRUE,
    IN,
    OUT,
    OPTIONAL,
    MAKEWORD,
    MAKELONG,
    LOWORD,
    HIWORD,
    LOBYTE,
    HIBYTE,
)

from shared.wtypes_h import (
    HWND,
    HHOOK,
    HEVENT,
    SPHANDLE,
    LPHANDLE,
    HGLOBAL,
    HLOCAL,
    GLOBALHANDLE,
    LOCALHANDLE,
    HGDIOBJ,
    HKEY,
    PHKEY,
    HACCEL,
    HBITMAP,
    HBRUSH,
    HCOLORSPACE,
    HDC,
    HGLRC,
    HDESK,
    HENHMETAFILE,
    HFONT,
    HICON,
    HMENU,
    HMETAFILE,
    HINSTANCE,
    HMODULE,
    HPALETTE,
    HPEN,
    HRGN,
    HRSRC,
    HSPRITE,
    HSTR,
    HTASK,
    HWINSTA,
    HKL,
    HWINEVENTHOOK,
    HMONITOR,
    HUMPD,
    HFILE,
    HCURSOR,
    COLORREF,
    LPCOLORREF,
    RECT,
    PRECT,
    NPRECT,
    LPRECT,
    LPCRECT,
    RECTL,
    PRECTL,
    LPRECTL,
    LPCRECTL,
    POINT,
    PPOINT,
    NPPOINT,
    LPPOINT,
    POINTL,
    PPOINTL,
    SIZE,
    PSIZE,
    LPSIZE,
    SIZEL,
    PSIZEL,
    LPSIZEL,
    POINTS,
    PPOINTS,
    LPPOINTS,
    NULL,
    PSZ,
    PULONG,
    USHORT,
    PUSHORT,
    UCHAR,
    PUCHAR,
    FILETIME,
    PFILETIME,
    LPFILETIME,
)

WINVER = 0x00000500

HFILE_ERROR = HFILE(-1)

DM_UPDATE = 0x00000001
DM_COPY = 0x00000002
DM_PROMPT = 0x00000004
DM_MODIFY = 0x00000008
DM_IN_BUFFER = DM_MODIFY
DM_IN_PROMPT = DM_PROMPT
DM_OUT_BUFFER = DM_COPY
DM_OUT_DEFAULT = DM_UPDATE
DC_FIELDS = 0x00000001
DC_PAPERS = 0x00000002
DC_PAPERSIZE = 0x00000003
DC_MINEXTENT = 0x00000004
DC_MAXEXTENT = 0x00000005
DC_BINS = 0x00000006
DC_DUPLEX = 0x00000007
DC_SIZE = 0x00000008
DC_EXTRA = 0x00000009
DC_VERSION = 0x0000000A
DC_DRIVER = 0x0000000B
DC_BINNAMES = 0x0000000C
DC_ENUMRESOLUTIONS = 0x0000000D
DC_FILEDEPENDENCIES = 0x0000000E
DC_TRUETYPE = 0x0000000F
DC_PAPERNAMES = 0x00000010
DC_ORIENTATION = 0x00000011
DC_COPIES = 0x00000012

__all__ = [
    'cdecl', 'pascal', 'far', 'near', 'NULL', 'PSZ', 'CDECL', 'CALLBACK',
    'WINAPI', 'WINAPIV', 'APIENTRY', 'APIPRIVATE', 'PASCAL', 'WINAPI_INLINE',
    'FAR', 'NEAR', 'WPARAM', 'LPARAM', 'LRESULT', 'FARPROC', 'NEARPROC',
    'PROC', 'HLSURF', 'DWORD', 'BOOL', 'BYTE', 'WORD', 'FLOAT', 'PFLOAT',
    'PBOOL', 'INT', 'UINT', 'PUINT', 'ULONG', 'PULONG', 'USHORT', 'PUSHORT',
    'UCHAR', 'PUCHAR', 'ATOM', 'MAX_PATH', 'FALSE', 'TRUE', 'IN',
    'OUT', 'OPTIONAL', 'MAKEWORD', 'MAKELONG', 'LOWORD', 'HIWORD', 'LOBYTE',
    'HIBYTE', 'HWND', 'HHOOK', 'HEVENT', 'SPHANDLE', 'LPHANDLE', 'HGLOBAL',
    'HLOCAL', 'GLOBALHANDLE', 'LOCALHANDLE', 'HGDIOBJ', 'HKEY', 'PHKEY',
    'HACCEL', 'HBITMAP', 'HBRUSH', 'HCOLORSPACE', 'HDC', 'HGLRC', 'HDESK',
    'HENHMETAFILE', 'HFONT', 'HICON', 'HMENU', 'HMETAFILE', 'HINSTANCE',
    'HMODULE', 'HPALETTE', 'HPEN', 'HRGN', 'HRSRC', 'HSPRITE', 'HSTR', 'HTASK',
    'HWINSTA', 'HKL', 'HWINEVENTHOOK', 'HMONITOR', 'HUMPD', 'HFILE', 'HCURSOR',
    'COLORREF', 'LPCOLORREF', 'RECT', 'PRECT', 'NPRECT', 'LPRECT', 'LPCRECT',
    'RECTL', 'PRECTL', 'LPRECTL', 'LPCRECTL', 'POINT', 'PPOINT', 'NPPOINT',
    'LPPOINT', 'POINTL', 'PPOINTL', 'SIZE', 'PSIZE', 'LPSIZE', 'SIZEL',
    'PSIZEL', 'LPSIZEL', 'POINTS', 'PPOINTS', 'LPPOINTS', 'FILETIME',
    'PFILETIME', 'LPFILETIME', 'WINVER', 'HFILE_ERROR', 'DM_UPDATE', 'DM_COPY',
    'DM_PROMPT', 'DM_MODIFY', 'DM_IN_BUFFER', 'DM_IN_PROMPT', 'DM_OUT_BUFFER',
    'DM_OUT_DEFAULT', 'DC_FIELDS', 'DC_PAPERS', 'DC_PAPERSIZE', 'DC_MINEXTENT',
    'DC_MAXEXTENT', 'DC_BINS', 'DC_DUPLEX', 'DC_SIZE', 'DC_EXTRA',
    'DC_VERSION', 'DC_DRIVER', 'DC_BINNAMES', 'DC_ENUMRESOLUTIONS',
    'DC_FILEDEPENDENCIES', 'DC_TRUETYPE', 'DC_PAPERNAMES', 'DC_ORIENTATION',
    'DC_COPIES',
]

