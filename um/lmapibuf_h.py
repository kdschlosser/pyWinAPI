import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMAPIBUF_ = None


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmapibuf.h
# Abstract: This file contains information about NetApiBuffer APIs.
# Environment: User Mode - Win32 Notes: You must include LMCONS.H before this
# file, since this file depends on values defined in LMCONS.H. --
if not defined(_LMAPIBUF_):
    _LMAPIBUF_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF


    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    netapi32 = ctypes.windll.NETAPI32
    from pyWinAPI.shared.lmcons_h import *  # NOQA


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # // Function Prototypes
        #
        #
        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetApiBufferAllocate(
        # _In_ DWORD ByteCount,
        # _Outptr_result_bytebuffer_(ByteCount) LPVOID * Buffer
        # );
        NetApiBufferAllocate = netapi32.NetApiBufferAllocate
        NetApiBufferAllocate.restype = NET_API_STATUS

        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetApiBufferFree(
        # _Frees_ptr_opt_ LPVOID Buffer
        # );
        NetApiBufferFree = netapi32.NetApiBufferFree
        NetApiBufferFree.restype = NET_API_STATUS

        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetApiBufferReallocate(
        # _Frees_ptr_opt_ LPVOID OldBuffer,
        # _In_ DWORD NewByteCount,
        # _Outptr_result_bytebuffer_(NewByteCount) LPVOID * NewBuffer
        # );
        NetApiBufferReallocate = netapi32.NetApiBufferReallocate
        NetApiBufferReallocate.restype = NET_API_STATUS

        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetApiBufferSize(
        # _In_ LPVOID Buffer,
        # _Out_ LPDWORD ByteCount
        # );
        NetApiBufferSize = netapi32.NetApiBufferSize
        NetApiBufferSize.restype = NET_API_STATUS

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # The following private function will go away eventually.
        # Call NetApiBufferAllocate instead.
        # Internal Function
        pass

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_APP):
        # _Success_( return == 0 )
        # NET_API_STATUS NET_API_FUNCTION
        # NetApiBufferFree(
        # _Frees_ptr_opt_ LPVOID Buffer
        # );
        NetApiBufferFree = netapi32.NetApiBufferFree
        NetApiBufferFree.restype = NET_API_STATUS

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_APP)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   _LMAPIBUF_


