import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_AVRT_H_ = None


from pyWinAPI.shared.winapifamily_h import * # NOQA

# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# avrt.h Abstract: This module contains the multimedia class scheduler APIs
# and any public data structures needed to call these APIs. --
if not defined(_AVRT_H_):
    _AVRT_H_ = VOID
    if defined(__cplusplus):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # AvRt Priorities
        class _AVRT_PRIORITY(ENUM):
            AVRT_PRIORITY_VERYLOW = - 2
            AVRT_PRIORITY_LOW = - 1
            AVRT_PRIORITY_NORMAL = 0
            AVRT_PRIORITY_HIGH = 1
            AVRT_PRIORITY_CRITICAL = 2

        AVRT_PRIORITY = _AVRT_PRIORITY
        PAVRT_PRIORITY = POINTER(_AVRT_PRIORITY)

        # Infinite timeout for a thread order group.
        THREAD_ORDER_GROUP_INFINITE_TIMEOUT = -1

        # Define API decoration for direct importing of DLL references.
        AVRTAPI = DECLSPEC_IMPORT
        avrt = ctypes.windll.AVRT

        # _Success_(return != NULL)
        # AVRTAPI
        # HANDLE
        # WINAPI
        # AvSetMmThreadCharacteristicsA(
        # _In_ LPCSTR TaskName,
        # _Inout_ LPDWORD TaskIndex
        # );
        AvSetMmThreadCharacteristicsA = avrt.AvSetMmThreadCharacteristicsA
        AvSetMmThreadCharacteristicsA.restype = HANDLE

        # _Success_(return != NULL)
        # AVRTAPI
        # HANDLE
        # WINAPI
        # AvSetMmThreadCharacteristicsW(
        # _In_ LPCWSTR TaskName,
        # _Inout_ LPDWORD TaskIndex
        # );
        AvSetMmThreadCharacteristicsW = avrt.AvSetMmThreadCharacteristicsW
        AvSetMmThreadCharacteristicsW.restype = HANDLE

        if defined(UNICODE):
            AvSetMmThreadCharacteristics = AvSetMmThreadCharacteristicsW
        else:
            AvSetMmThreadCharacteristics = AvSetMmThreadCharacteristicsA
        # END IF   not UNICODE

        # _Success_(return != NULL)
        # AVRTAPI
        # HANDLE
        # WINAPI
        # AvSetMmMaxThreadCharacteristicsA(
        # _In_ LPCSTR FirstTask,
        # _In_ LPCSTR SecondTask,
        # _Inout_ LPDWORD TaskIndex
        # );
        AvSetMmMaxThreadCharacteristicsA = (
            avrt.AvSetMmMaxThreadCharacteristicsA
        )
        AvSetMmMaxThreadCharacteristicsA.restype = HANDLE

        # _Success_(return != NULL)
        # AVRTAPI
        # HANDLE
        # WINAPI
        # AvSetMmMaxThreadCharacteristicsW(
        # _In_ LPCWSTR FirstTask,
        # _In_ LPCWSTR SecondTask,
        # _Inout_ LPDWORD TaskIndex
        # );
        AvSetMmMaxThreadCharacteristicsW = (
            avrt.AvSetMmMaxThreadCharacteristicsW
        )
        AvSetMmMaxThreadCharacteristicsW.restype = HANDLE

        if defined(UNICODE):
            AvSetMmMaxThreadCharacteristics = AvSetMmMaxThreadCharacteristicsW
        else:
            AvSetMmMaxThreadCharacteristics = AvSetMmMaxThreadCharacteristicsA
        # END IF   not UNICODE

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRevertMmThreadCharacteristics(
        # _In_ HANDLE AvrtHandle
        # );
        AvRevertMmThreadCharacteristics = avrt.AvRevertMmThreadCharacteristics
        AvRevertMmThreadCharacteristics.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvSetMmThreadPriority(
        # _In_ HANDLE AvrtHandle,
        # _In_ AVRT_PRIORITY Priority
        # );
        AvSetMmThreadPriority = avrt.AvSetMmThreadPriority
        AvSetMmThreadPriority.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRtCreateThreadOrderingGroup(
        # _Out_ PHANDLE Context,
        # _In_ PLARGE_INTEGER Period,
        # _Inout_ GUID *ThreadOrderingGuid,
        # _In_opt_ PLARGE_INTEGER Timeout
        # );
        AvRtCreateThreadOrderingGroup = avrt.AvRtCreateThreadOrderingGroup
        AvRtCreateThreadOrderingGroup.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRtCreateThreadOrderingGroupExA(
        # _Out_ PHANDLE Context,
        # _In_ PLARGE_INTEGER Period,
        # _Inout_ GUID *ThreadOrderingGuid,
        # _In_opt_ PLARGE_INTEGER Timeout,
        # _In_ LPCSTR TaskName
        # );
        AvRtCreateThreadOrderingGroupExA = (
            avrt.AvRtCreateThreadOrderingGroupExA
        )
        AvRtCreateThreadOrderingGroupExA.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRtCreateThreadOrderingGroupExW(
        # _Out_ PHANDLE Context,
        # _In_ PLARGE_INTEGER Period,
        # _Inout_ GUID *ThreadOrderingGuid,
        # _In_opt_ PLARGE_INTEGER Timeout,
        # _In_ LPCWSTR TaskName
        # );
        AvRtCreateThreadOrderingGroupExW = (
            avrt.AvRtCreateThreadOrderingGroupExW
        )
        AvRtCreateThreadOrderingGroupExW.restype = BOOL

        if defined(UNICODE):
            AvRtCreateThreadOrderingGroupEx = AvRtCreateThreadOrderingGroupExW
        else:
            AvRtCreateThreadOrderingGroupEx = AvRtCreateThreadOrderingGroupExA
        # END IF   not UNICODE

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRtJoinThreadOrderingGroup(
        # _Out_ PHANDLE Context,
        # _In_ GUID *ThreadOrderingGuid,
        # _In_ BOOL Before
        # );
        AvRtJoinThreadOrderingGroup = avrt.AvRtJoinThreadOrderingGroup
        AvRtJoinThreadOrderingGroup.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRtWaitOnThreadOrderingGroup(
        # _In_ HANDLE Context
        # );
        AvRtWaitOnThreadOrderingGroup = avrt.AvRtWaitOnThreadOrderingGroup
        AvRtWaitOnThreadOrderingGroup.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRtLeaveThreadOrderingGroup(
        # _In_ HANDLE Context
        # );
        AvRtLeaveThreadOrderingGroup = avrt.AvRtLeaveThreadOrderingGroup
        AvRtLeaveThreadOrderingGroup.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvRtDeleteThreadOrderingGroup(
        # _In_ HANDLE Context
        # );
        AvRtDeleteThreadOrderingGroup = avrt.AvRtDeleteThreadOrderingGroup
        AvRtDeleteThreadOrderingGroup.restype = BOOL

        # _Success_(return != FALSE)
        # AVRTAPI
        # BOOL
        # WINAPI
        # AvQuerySystemResponsiveness(
        # _In_ HANDLE AvrtHandle,
        # _Out_ PULONG SystemResponsivenessValue
        # );
        AvQuerySystemResponsiveness = avrt.AvQuerySystemResponsiveness
        AvQuerySystemResponsiveness.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   _AVRT_H_


