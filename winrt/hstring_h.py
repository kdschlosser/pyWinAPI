

from wtypes_h import (
    INT,
    PVOID,
    CHAR,
    POINTER,
)
import ctypes


# this ALWAYS GENERATED file contains the definitions for the INTerfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING(  )
# verify that the <rpcndr.h> version is high enough to compile this file
__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
# verify that the <rpcsal.h> version is high enough to compile this file
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# __RPCNDR_H_VERSION__
# Forward Declarations
# header files for imported files
# INTerface __MIDL_itf_hstring_0000_0000
# [local]
# +-------------------------------------------------------------------------

# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.

# --------------------------------------------------------------------------
# Declare the HSTRING handle as wire_marshal for midl only

class HSTRING__(ctypes.Structure):
    _fields_ = [
        ('unused', INT),
    ]


# [unique][wire_marshal]
HSTRING = POINTER(HSTRING__)
# Declaring a handle dummy struct for HSTRING the same way DECLARE_HANDLE does.


class HSTRING_HEADER(ctypes.Structure):

    class Reserved(ctypes.Union):
        _fields_ = [
            ('Reserved1', PVOID),
            ('Reserved2', CHAR * 24),
            ('Reserved2', CHAR * 20),
        ]

    _fields_ = [
        ('Reserved', Reserved),
    ]



# Declare the HSTRING_BUFFER for the HSTRING's two-phase construction
# functions.

# This route eliminates the PCWSTR string copy that happens when passing it to
# the traditional WindowsCreateString().  The caller preallocates a string
# buffer,
# sets the wide CHARacter string values in that buffer, and finally promotes
# the
# buffer to an HSTRING.  If a buffer is never promoted, it can still be
# deleted.
# Additional Prototypes for ALL INTerfaces
# end of Additional Prototypes

__all__ = (
    '__REQUIRED_RPCSAL_H_VERSION__', '__REQUIRED_RPCNDR_H_VERSION__',
    'HSTRING__', 'HSTRING_HEADER', 'HSTRING',
)
