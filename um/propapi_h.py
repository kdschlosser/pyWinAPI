import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_PROPAPI_H_ = None

# + -------------------------------------------------------------------------
# Microsoft Windows
# Copyright (C) Microsoft Corporation, 1992-2006.
# File:  propapi.h
# Contents: Structured storage properties APIs
# --------------------------------------------------------------------------
if not defined(_PROPAPI_H_):
    _PROPAPI_H_ = VOID

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__cplusplus):
            pass
        # END IF

        NTPROP = POINTER(VOID)
        from pyWinAPI.um.propidl_h import * # NOQA
        ole32 = ctypes.windll.OLE32

        # EXTERN_C
        # _Success_(TRUE) // Raises status on failure
        # ULONG __stdcall
        # StgPropertyLengthAsVariant(
        # _In_reads_bytes_(cbProp) SERIALIZEDPROPERTYVALUE* pProp,
        # _In_ ULONG cbProp,
        # _In_ USHORT CodePage,
        # _Reserved_ BYTE bReserved);
        StgPropertyLengthAsVariant = ole32.StgPropertyLengthAsVariant
        StgPropertyLengthAsVariant.restype = ULONG

        if defined(__cplusplus):
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   ifndef _PROPAPI_H_


