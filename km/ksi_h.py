import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class KSIDEFAULTCLOCK(ctypes.Structure):
    pass


PKSIDEFAULTCLOCK = POINTER(KSIDEFAULTCLOCK)


class KSCLOCKINSTANCE(ctypes.Structure):
    pass


PKSCLOCKINSTANCE = POINTER(KSCLOCKINSTANCE)


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: ksi.h Abstract: Windows Driver Model/Connection and Streaming
# Architecture (WDM - CSA) core internal definitions. - -

_KSI_ = None
if not defined(_KSI_):
    _KSI_ = 1

    if defined(__cplusplus):
        pass
    # END IF   defined(__cplusplus)

    from pyWinAPI.shared.ksmedia_h import * # NOQA


    if defined(_NTDDK_):
        KSIDEFAULTCLOCK._fields_ = [
            ('Frequency', LONGLONG),
            ('LastDueTime', LONGLONG),
            ('RunningTimeDelta', LONGLONG),
            ('LastRunningTime', LONGLONG),
            ('TimeAccessLock', KSPIN_LOCK),
            ('EventQueue', LIST_ENTRY),
            ('EventQueueLock', KSPIN_LOCK),
            ('QueueTimer', KTIMER),
            ('QueueDpc', KDPC),
            ('ReferenceCount', LONG),
            ('State', KSSTATE),
            ('SuspendDelta', LONGLONG),
            ('SuspendTime', LONGLONG),
            ('SetTimer', PFNKSSETTIMER),
            ('CancelTimer', PFNKSCANCELTIMER),
            ('CorrelatedTime', PFNKSCLOCK_CORRELATEDTIME),
            ('Context', PVOID),
            ('Resolution', KSRESOLUTION),
            ('FreeEvent', KEVENT),
            ('ExternalTimeReferenceCount', LONG),
            ('ExternalTimeValid', BOOLEAN),
            ('LastStreamTime', LONGLONG),
        ]

        KSCLOCKINSTANCE._fields_ = [
            ('Header', KSOBJECT_HEADER),
            ('DefaultClock', PKSIDEFAULTCLOCK),
            ('Reserved', ULONG),
        ]
        ks = ctypes.windll.KS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiPropertyDefaultClockGetTime(
        # _In_ PIRP Irp,
        # _In_ PKSPROPERTY Property,
        # _Out_ PLONGLONG Time
        # );
        KsiPropertyDefaultClockGetTime = ks.KsiPropertyDefaultClockGetTime
        KsiPropertyDefaultClockGetTime.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiPropertyDefaultClockGetPhysicalTime(
        # _In_ PIRP Irp,
        # _In_ PKSPROPERTY Property,
        # _Out_ PLONGLONG Time
        # );
        KsiPropertyDefaultClockGetPhysicalTime = (
            ks.KsiPropertyDefaultClockGetPhysicalTime
        )
        KsiPropertyDefaultClockGetPhysicalTime.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiPropertyDefaultClockGetCorrelatedTime(
        # _In_ PIRP Irp,
        # _In_ PKSPROPERTY Property,
        # _Out_ PKSCORRELATED_TIME Time
        # );
        KsiPropertyDefaultClockGetCorrelatedTime = (
            ks.KsiPropertyDefaultClockGetCorrelatedTime
        )
        KsiPropertyDefaultClockGetCorrelatedTime.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiPropertyDefaultClockGetCorrelatedPhysicalTime(
        # _In_ PIRP Irp,
        # _In_ PKSPROPERTY Property,
        # _Out_ PKSCORRELATED_TIME Time
        # );
        KsiPropertyDefaultClockGetCorrelatedPhysicalTime = (
            ks.KsiPropertyDefaultClockGetCorrelatedPhysicalTime
        )
        KsiPropertyDefaultClockGetCorrelatedPhysicalTime.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiPropertyDefaultClockGetResolution(
        # _In_ PIRP Irp,
        # _In_ PKSPROPERTY Property,
        # _Out_ PKSRESOLUTION Resolution
        # );
        KsiPropertyDefaultClockGetResolution = (
            ks.KsiPropertyDefaultClockGetResolution
        )
        KsiPropertyDefaultClockGetResolution.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiPropertyDefaultClockGetState(
        # _In_ PIRP Irp,
        # _In_ PKSPROPERTY Property,
        # _Out_ PKSSTATE State
        # );
        KsiPropertyDefaultClockGetState = ks.KsiPropertyDefaultClockGetState
        KsiPropertyDefaultClockGetState.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiPropertyDefaultClockGetFunctionTable(
        # _In_ PIRP Irp,
        # _In_ PKSPROPERTY Property,
        # _Out_ PKSCLOCK_FUNCTIONTABLE FunctionTable
        # );
        KsiPropertyDefaultClockGetFunctionTable = (
            ks.KsiPropertyDefaultClockGetFunctionTable
        )
        KsiPropertyDefaultClockGetFunctionTable.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # _Must_inspect_result_
        # KSDDKAPI
        # NTSTATUS
        # NTAPI
        # KsiDefaultClockAddMarkEvent(
        # _In_ PIRP Irp,
        # _In_ PKSEVENT_TIME_INTERVAL EventTime,
        # _In_ PKSEVENT_ENTRY EventEntry
        # );
        KsiDefaultClockAddMarkEvent = ks.KsiDefaultClockAddMarkEvent
        KsiDefaultClockAddMarkEvent.restype = NTSTATUS

        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # KSDDKAPI
        # BOOLEAN
        # NTAPI
        # KsiQueryObjectCreateItemsPresent(
        # _In_ KSDEVICE_HEADER Header
        # );
        KsiQueryObjectCreateItemsPresent = ks.KsiQueryObjectCreateItemsPresent
        KsiQueryObjectCreateItemsPresent.restype = BOOLEAN

    # END IF   not defined(_NTDDK_)
    STATIC_KSNAME_Server = (
        0x3C0D501A,
        0x140B,
        0x11D1,
        0xB4,
        0x0F,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    KSNAME_Server = DEFINE_GUIDSTRUCT(
        "3C0D501A-140B-11D1-B40F-00A0C9223196"
    )
    KSNAME_Server = DEFINE_GUIDNAMED(KSNAME_Server)
    KSSTRING_Server = "{3C0D501A-140B-11D1-B40F-00A0C9223196}"
    STATIC_KSPROPSETID_Service = (
        0x3C0D501B,
        0x140B,
        0x11D1,
        0xB4,
        0x0F,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )
    KSPROPSETID_Service = DEFINE_GUIDSTRUCT(
        "{3C0D501B-140B-11D1-B40F-00A0C9223196}"
    )
    KSPROPSETID_Service = DEFINE_GUIDNAMED(KSPROPSETID_Service)


    class KSPROPERTY_SERVICE(ENUM):
        KSPROPERTY_SERVICE_BUILDCACHE = 1
        KSPROPERTY_SERVICE_MERIT = 2


    KSPROPERTY_SERVICE_BUILDCACHE = KSPROPERTY_SERVICE.KSPROPERTY_SERVICE_BUILDCACHE
    KSPROPERTY_SERVICE_MERIT = KSPROPERTY_SERVICE.KSPROPERTY_SERVICE_MERIT


    def DEFINE_KSPROPERTY_ITEM_SERVICE_BUILDCACHE(SetHandler):
        return DEFINE_KSPROPERTY_ITEM(
            KSPROPERTY_SERVICE_BUILDCACHE,
            NULL,
            ctypes.sizeof(KSPROPERTY),
            ctypes.sizeof("\\\\?\\"),
            SetHandler,
            NULL,
            0,
            NULL,
            NULL,
            0
        )


    def DEFINE_KSPROPERTY_ITEM_SERVICE_MERIT(SetHandler):
        return DEFINE_KSPROPERTY_ITEM(
            KSPROPERTY_SERVICE_MERIT,
            NULL,
            ctypes.sizeof(KSPROPERTY),
            ctypes.sizeof(ULONG) + ctypes.sizeof("\\\\?\\"),
            SetHandler,
            NULL,
            0,
            NULL,
            NULL,
            0
        )

    if defined(__cplusplus):
        pass

    # END IF   defined(__cplusplus)
# END IF   not _KSI_
