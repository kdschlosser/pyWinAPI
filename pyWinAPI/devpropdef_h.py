
from .winapifamily_h import * # NOQA
from .wtypes_h import (
    POINTER,
    ULONG,
    CHAR,
    GUID,
    PCWSTR,
    ENUM,
    NULL,
    PVOID,
    _wcsicmp
)
import ctypes


# ++
# Copyright (c) Microsoft Corporation.  All rights reserved.
# Module Name:
# devpropdef.h
# Abstract:
# Defines property types and keys for the Plug and Play Device Property API.
# Environment:
# User and Kernel modes.
# --

# Type definition for property data types.  Valid DEVPROPTYPE values are
# constructed from base DEVPROP_TYPE_ values, which may be modified by a
# logical OR with DEVPROP_TYPEMOD_ values, as appropriate.

DEVPROPTYPE = ULONG
PDEVPROPTYPE = POINTER(ULONG)

# Property type modifiers.  Used to modify base DEVPROP_TYPE_ values, as
# appropriate.  Not valid as standalone DEVPROPTYPE values.

# array of fixed-sized data elements
# list of variable-sized data elements
DEVPROP_TYPEMOD_ARRAY = 0x0000000000001000
DEVPROP_TYPEMOD_LIST = 0x0000000000002000

# Property data types.

# nothing, no property data
# null property data
DEVPROP_TYPE_EMPTY = 0x0000000000000000
# 8-bit INT (SBYTE)
DEVPROP_TYPE_NULL = 0x0000000000000001
# 8-bit unINT (BYTE)
DEVPROP_TYPE_SBYTE = 0x0000000000000002
# 16-bit INT (SHORT)
DEVPROP_TYPE_BYTE = 0x0000000000000003
# 16-bit unINT (USHORT)
DEVPROP_TYPE_INT16 = 0x0000000000000004
# 32-bit INT (LONG)
DEVPROP_TYPE_UINT16 = 0x0000000000000005
# 32-bit unINT (ULONG)
DEVPROP_TYPE_INT32 = 0x0000000000000006
# 64-bit INT (LONG64)
DEVPROP_TYPE_UINT32 = 0x0000000000000007
# 64-bit unINT (ULONG64)
DEVPROP_TYPE_INT64 = 0x0000000000000008
# 32-bit FLOATing-poINT (FLOAT)
DEVPROP_TYPE_UINT64 = 0x0000000000000009
# 64-bit FLOATing-poINT (DOUBLE)
DEVPROP_TYPE_FLOAT = 0x00000000A
# 128-bit data (DECIMAL)
DEVPROP_TYPE_DOUBLE = 0x00000000B
# 128-bit unique identifier (GUID)
DEVPROP_TYPE_DECIMAL = 0x00000000C
# 64 bit INT currency value (CURRENCY)
DEVPROP_TYPE_GUID = 0x00000000D
# date (DATE)
DEVPROP_TYPE_CURRENCY = 0x00000000E
# file time (FILETIME)
DEVPROP_TYPE_DATE = 0x00000000F
# 8-bit BOOLean (DEVPROP_BOOLEAN)
DEVPROP_TYPE_FILETIME = 0x0000000000000010
# null-terminated string
DEVPROP_TYPE_BOOLEAN = 0x0000000000000011
# multi-sz string list
DEVPROP_TYPE_STRING = 0x0000000000000012
# self-relative binary SECURITY_DESCRIPTOR
DEVPROP_TYPE_STRING_LIST = DEVPROP_TYPE_STRING | DEVPROP_TYPEMOD_LIST
# security descriptor string (SDDL format)
DEVPROP_TYPE_SECURITY_DESCRIPTOR = 0x0000000000000013
# device property key (DEVPROPKEY)
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING = 0x0000000000000014
# device property type (DEVPROPTYPE)
DEVPROP_TYPE_DEVPROPKEY = 0x0000000000000015
# custom binary data
DEVPROP_TYPE_DEVPROPTYPE = 0x0000000000000016
# 32-bit Win32 system error code
DEVPROP_TYPE_BINARY = DEVPROP_TYPE_BYTE | DEVPROP_TYPEMOD_ARRAY
# 32-bit NTSTATUS code
DEVPROP_TYPE_ERROR = 0x0000000000000017
# string resource (@[path\]<dllname>,-<strId>)
DEVPROP_TYPE_NTSTATUS = 0x0000000000000018
DEVPROP_TYPE_STRING_INDIRECT = 0x0000000000000019

# Max base DEVPROP_TYPE_ and DEVPROP_TYPEMOD_ values.

# max valid DEVPROP_TYPE_ value
# max valid DEVPROP_TYPEMOD_ value
MAX_DEVPROP_TYPE = 0x0000000000000019
MAX_DEVPROP_TYPEMOD = 0x0000000000002000

# Bitmasks for extracting DEVPROP_TYPE_ and DEVPROP_TYPEMOD_ values.

# range for base DEVPROP_TYPE_ values
# mask for DEVPROP_TYPEMOD_ type modifiers
DEVPROP_MASK_TYPE = 0x00000000FFF
DEVPROP_MASK_TYPEMOD = 0x00000000F000

# Property type specific data types.

# 8-bit BOOLean type definition for DEVPROP_TYPE_BOOLEAN (True=-1, False=0)
DEVPROP_BOOLEAN = CHAR
PDEVPROP_BOOLEAN = POINTER(CHAR)
DEVPROP_TRUE = -1
DEVPROP_FALSE = 0

# DEVPROPKEY structure

DEVPROPGUID = GUID
PDEVPROPGUID = POINTER(GUID)
DEVPROPID = ULONG
PDEVPROPID = POINTER(ULONG)

class DEVPROPKEY(ctypes.Structure):
    _fields_= [
        ('fmtid', DEVPROPGUID),
        ('pid', ULONG),
    ]


PDEVPROPKEY = POINTER(DEVPROPKEY)

from .guiddef_h import IsEqualGUID
# DEVPROPKEY_DEFINED


def IsEqualDevPropKey(a, b):
    return (a.pid == b.pid) and IsEqualGUID(a.fmtid, b.fmtid)

# _SYS_GUID_OPERATOR_EQ_

# DEVPROPSTORE Enumeration


# This enumeration describes where a property is stored.
class _DEVPROPSTORE(ENUM):
    DEVPROP_STORE_SYSTEM = 0
    DEVPROP_STORE_USER = 1


DEVPROPSTORE = _DEVPROPSTORE
PDEVPROPSTORE = POINTER(_DEVPROPSTORE)

# DEVPROPCOMPKEY structure

# This structure represents a compound key for a property.


class DEVPROPCOMPKEY(ctypes.Structure):
    _fields_= [
        ('Key', DEVPROPKEY),
        ('Store', DEVPROPSTORE),
        ('LocaleName', PCWSTR),
    ]


PDEVPROPCOMPKEY = POINTER(DEVPROPCOMPKEY)


def IsEqualLocaleName(a, b):
    return((a == b) or ((a != NULL and b != NULL) and _wcsicmp(a, b) == 0)
)


def IsEqualDevPropCompKey(a, b):
    return (
        IsEqualDevPropKey(a.Key, b.Key) and
        (a.Store == b.Store) and
        IsEqualLocaleName(a.LocaleName, b.LocaleName)
    )

# _SYS_GUID_OPERATOR_EQ_
# __cplusplus
# !IsEqualDevPropCompKey

# DEVPROPERTY structure


class DEVPROPERTY(ctypes.Structure):
    _fields_= [
        ('CompKey', DEVPROPCOMPKEY),
        ('Type', DEVPROPTYPE),
        ('BufferSize', ULONG),
        ('Buffer', PVOID)
    ]


PDEVPROPERTY = POINTER(DEVPROPERTY)


# All valid DEVPROPKEY definitions must use a PROPID that is equal to or
# greater
# than DEVPROPID_FIRST_USABLE.

DEVPROPID_FIRST_USABLE = 0x00000002
# _DEVPROPDEF_H_


def DEFINE_DEVPROPKEY(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8, pid):
    return DEVPROPKEY(
        GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8),
        pid
    )

_all_ = (
'DEFINE_DEVPROPKEY', 'DEVPROPCOMPKEY', 'DEVPROPERTY', 'DEVPROPGUID',
    'DEVPROPID', 'DEVPROPID_FIRST_USABLE', 'DEVPROPKEY', 'DEVPROPSTORE',
    'DEVPROPTYPE', 'DEVPROP_BOOLEAN', 'DEVPROP_FALSE', 'DEVPROP_MASK_TYPE',
    'DEVPROP_MASK_TYPEMOD', 'DEVPROP_TRUE', 'DEVPROP_TYPEMOD_ARRAY',
    'DEVPROP_TYPEMOD_LIST', 'DEVPROP_TYPE_BINARY', 'DEVPROP_TYPE_BOOLEAN',
    'DEVPROP_TYPE_BYTE', 'DEVPROP_TYPE_CURRENCY', 'DEVPROP_TYPE_DATE',
    'DEVPROP_TYPE_DECIMAL', 'DEVPROP_TYPE_DEVPROPKEY', 'DEVPROP_TYPE_DOUBLE',
    'DEVPROP_TYPE_DEVPROPTYPE', 'DEVPROP_TYPE_EMPTY', 'DEVPROP_TYPE_ERROR',
    'DEVPROP_TYPE_FILETIME', 'DEVPROP_TYPE_FLOAT', 'DEVPROP_TYPE_GUID',
    'DEVPROP_TYPE_INT16', 'DEVPROP_TYPE_INT32', 'DEVPROP_TYPE_INT64',
    'DEVPROP_TYPE_NTSTATUS', 'DEVPROP_TYPE_NULL', 'DEVPROP_TYPE_SBYTE',
    'DEVPROP_TYPE_SECURITY_DESCRIPTOR', 'DEVPROP_TYPE_STRING', 'PDEVPROPERTY',
    'DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING', 'DEVPROP_TYPE_STRING_INDIRECT',
    'DEVPROP_TYPE_STRING_LIST', 'DEVPROP_TYPE_UINT16', 'DEVPROP_TYPE_UINT32',
    'DEVPROP_TYPE_UINT64', 'MAX_DEVPROP_TYPE', 'MAX_DEVPROP_TYPEMOD',
    'PDEVPROPCOMPKEY', 'PDEVPROPGUID', 'PDEVPROPID', 'PDEVPROPKEY',
    'PDEVPROPSTORE', 'PDEVPROPTYPE', 'PDEVPROP_BOOLEAN', '_DEVPROPSTORE',
    'IsEqualDevPropCompKey', 'IsEqualLocaleName', 'IsEqualDevPropKey'
)
