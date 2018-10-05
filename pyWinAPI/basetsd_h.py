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
    INT64,
    KAFFINITY,
    ULONG64,
)

ADDRESS_TAG_BIT = 0x40000000000


def HandleToULong(h):
    try:
        return ULONG(h.value)
    except AttributeError:
        return ULONG(h)


def HandleToLong(h):
    try:
        return LONG(h.value)
    except AttributeError:
        return LONG(h)


def ULongToHandle(h):
    try:
        return HANDLE(h.value)
    except AttributeError:
        return HANDLE(h)


def LongToHandle(h):
    try:
        return HANDLE(h.value)
    except AttributeError:
        return HANDLE(h)


def PtrToUlong(p):
    try:
        return ULONG(p.value)
    except AttributeError:
        return ULONG(p)


def PtrToUint(p):
    try:
        return UINT(p.value)
    except AttributeError:
        return UINT(p)


def PtrToUshort(p):
    try:
        return USHORT(p.value)
    except AttributeError:
        return USHORT(p)


def PtrToLong(p):
    try:
        return LONG(p.value)
    except AttributeError:
        return LONG(p)


def PtrToInt(p):
    try:
        return INT(p.value)
    except AttributeError:
        return INT(p)


def PtrToShort(p):
    try:
        return SHORT(p.value)
    except AttributeError:
        return SHORT(p)


def IntToPtr(p):
    try:
        return INT_PTR(p.value)
    except AttributeError:
        return INT_PTR(p)


def UIntToPtr(p):
    try:
        return INT_PTR(p.value)
    except AttributeError:
        return INT_PTR(p)


def LongToPtr(p):
    try:
        return INT_PTR(p.value)
    except AttributeError:
        return INT_PTR(p)


def ULongToPtr(p):
    try:
        return INT_PTR(p.value)
    except AttributeError:
        return INT_PTR(p)


def PtrToPtr64(p):
    try:
        return POINTER_64(p.value)
    except AttributeError:
        return POINTER_64(p)


def Ptr64ToPtr(p):
    try:
        return INT_PTR(p.value)
    except AttributeError:
        return INT_PTR(p)


def HandleToHandle64(h):
    return PtrToPtr64(h)


def Handle64ToHandle(h):
    return Ptr64ToPtr(h)


def Ptr32ToPtr(p):
    try:
        return ULONG_PTR(p.value)
    except AttributeError:
        return ULONG_PTR(p)


def Handle32ToHandle(h):
    try:
        return PVOID(h.value)
    except AttributeError:
        return PVOID(h)


def PtrToPtr32(p):
    try:
        return POINTER_32(p.value)
    except AttributeError:
        return POINTER_32(p)


def HandleToHandle32(h):
    return PtrToPtr32(h)


MAXUINT_PTR = ~0
MAXINT_PTR = MAXUINT_PTR >> 1
MININT_PTR = ~MAXINT_PTR

MAXULONG_PTR = ~0
MAXLONG_PTR = MAXULONG_PTR >> 1
MINLONG_PTR = ~MAXLONG_PTR

MAXUHALF_PTR = ~0
MAXHALF_PTR = MAXUHALF_PTR >> 1
MINHALF_PTR = ~MAXHALF_PTR

MAXUINT8 = ~0
MAXINT8 = MAXUINT8 >> 1
MININT8 = ~MAXINT8

MAXUINT16 = ~0
MAXINT16 = MAXUINT16 >> 1
MININT16 = ~MAXINT16

MAXUINT32 = ~0
MAXINT32 = MAXUINT32 >> 1
MININT32 = ~MAXINT32

MAXUINT64 = ~0
MAXINT64 = MAXUINT64 >> 1
MININT64 = ~MAXINT64

MAXULONG32 = ~0
MAXLONG32 = MAXULONG32 >> 1
MINLONG32 = ~MAXLONG32

MAXULONG64 = ~0
MAXLONG64 = MAXULONG64 >> 1
MINLONG64 = ~MAXLONG64

MAXULONGLONG = ~0
MAXLONGLONG = MAXULONGLONG >> 1
MINLONGLONG = ~MAXLONGLONG

MAXSIZE_T = ~0
MAXSSIZE_T = MAXSIZE_T >> 1
MINSSIZE_T = ~MAXSSIZE_T

MAXUINT = ~0
MAXINT = MAXUINT >> 1
MININT = ~MAXINT

MAXDWORD32 = ~0
MAXDWORD64 = ~0


from .wtypes_h import (
    INT8,
    PINT8,
    UINT8,
    PUINT8,
    INT16,
    UINT16,
    PUINT16,
    INT32,
    PINT32,
    UINT32,
    PUINT32,
    PINT64,
    UINT64,
    PUINT64,
    POINTER_64,
    POINTER_64_INT,
    POINTER_32,
    UPOINTER_32,
    POINTER_SIGNED,
    POINTER_UNSIGNED,
    SPOINTER_32,
    SIZE_T,
    PSIZE_T,
    SSIZE_T,
    PSSIZE_T,
    LONG32,
    PLONG32,
    ULONG32,
    PULONG32,
    DWORD32,
    PDWORD32,
    INT_PTR,
    PINT_PTR,
    UINT_PTR,
    PUINT_PTR,
    LONG_PTR,
    PLONG_PTR,
    ULONG_PTR,
    PULONG_PTR,
    SHANDLE_PTR,
    HANDLE_PTR,
    UHALF_PTR,
    PUHALF_PTR,
    HALF_PTR,
    PHALF_PTR,
    DWORD_PTR,
    PDWORD_PTR,
    LONG64,
    PLONG64,
    PULONG64,
    DWORD64,
    PDWORD64,
    USHORT,
    LONG,
    HANDLE,
    UINT,
    INT,
    PVOID,
    SHORT
)

import ctypes

ULONG = ctypes.c_ulong


__all__ = [
    'INT8', 'PINT8', 'UINT8', 'PUINT8', 'INT16', 'UINT16', 'PUINT16', 'INT32',
    'PINT32', 'UINT32', 'PUINT32', 'INT64', 'PINT64', 'UINT64', 'PUINT64',
    'POINTER_64', 'POINTER_64_INT', 'POINTER_32', 'UPOINTER_32',
    'POINTER_SIGNED', 'POINTER_UNSIGNED', 'SPOINTER_32', 'SIZE_T', 'PSIZE_T',
    'SSIZE_T', 'PSSIZE_T', 'LONG32', 'PLONG32', 'ULONG32', 'PULONG32',
    'DWORD32', 'PDWORD32', 'INT_PTR', 'PINT_PTR', 'UINT_PTR', 'PUINT_PTR',
    'LONG_PTR', 'PLONG_PTR', 'ULONG_PTR', 'PULONG_PTR', 'SHANDLE_PTR',
    'HANDLE_PTR', 'UHALF_PTR', 'PUHALF_PTR', 'HALF_PTR', 'PHALF_PTR',
    'DWORD_PTR', 'PDWORD_PTR', 'LONG64', 'PLONG64', 'ULONG64', 'PULONG64',
    'DWORD64', 'PDWORD64', 'KAFFINITY', 'MAXUINT_PTR', 'MAXINT_PTR',
    'MININT_PTR', 'MAXULONG_PTR', 'MAXLONG_PTR', 'MINLONG_PTR', 'MAXUHALF_PTR',
    'MAXHALF_PTR', 'MINHALF_PTR', 'MAXUINT8', 'MAXINT8', 'MININT8',
    'MAXUINT16', 'MAXINT16', 'MININT16', 'MAXUINT32', 'MAXINT32', 'MININT32',
    'MAXUINT64', 'MAXINT64', 'MININT64', 'MAXULONG32', 'MAXLONG32',
    'MINLONG32', 'MAXULONG64', 'MAXLONG64', 'MINLONG64', 'MAXULONGLONG',
    'MAXLONGLONG', 'MINLONGLONG', 'MAXSIZE_T', 'MAXSSIZE_T', 'MINSSIZE_T',
    'MAXUINT', 'MAXINT', 'MININT', 'MAXDWORD32', 'MAXDWORD64',
    'ADDRESS_TAG_BIT', 'HandleToULong', 'HandleToLong', 'ULongToHandle',
    'LongToHandle', 'PtrToUlong', 'PtrToUint', 'PtrToUshort', 'PtrToLong',
    'PtrToInt', 'PtrToShort', 'IntToPtr', 'UIntToPtr', 'LongToPtr',
    'ULongToPtr', 'PtrToPtr64', 'Ptr64ToPtr', 'HandleToHandle64',
    'Handle64ToHandle', 'Ptr32ToPtr', 'Handle32ToHandle', 'PtrToPtr32',
    'HandleToHandle32'
]
