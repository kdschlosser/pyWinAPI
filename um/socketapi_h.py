import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


_SOCKETAPI_H = None

# /* Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# socketapi.h Abstract: Prototypes and Definitions for Socket API
if not defined(_SOCKETAPI_H):
    _SOCKETAPI_H = VOID
    if defined(_MSC_VER):
        pass
    # END IF   _MSC_VER

    if defined(__cplusplus):
        networking = ctypes.WinDLL('Windows.Networking')

        # extern "C"
        # {
        # #endif
        #
        # #include <winapifamily.h>
        #
        # #pragma region Application Family
        # #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
        #
        # #if NTDDI_VERSION >= NTDDI_WIN8
        #
        # HRESULT WINAPI SetSocketMediaStreamingMode(_In_ BOOL value);
        SetSocketMediaStreamingMode = (
            networking.SetSocketMediaStreamingMode
        )
        SetSocketMediaStreamingMode.restype = HRESULT
    # END IF   NTDDI_VERSION >= NTDDI_WIN8
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
if defined(__cplusplus):
    pass
# END IF

# END IF   _SOCKETAPI_H


