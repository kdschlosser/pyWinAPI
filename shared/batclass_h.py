import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


class BATTERY_REPORTING_SCALE(ctypes.Structure):
    pass


PBATTERY_REPORTING_SCALE = POINTER(BATTERY_REPORTING_SCALE)


class BATTERY_NOTIFY(ctypes.Structure):
    pass


PBATTERY_NOTIFY = POINTER(BATTERY_NOTIFY)


class BATTERY_MINIPORT_INFO(ctypes.Structure):
    pass


PBATTERY_MINIPORT_INFO = POINTER(BATTERY_MINIPORT_INFO)


class BATTERY_MINIPORT_INFO_V1_1(ctypes.Structure):
    pass


PBATTERY_MINIPORT_INFO_V1_1 = POINTER(BATTERY_MINIPORT_INFO_V1_1)


class _BATTERY_WMI_STATUS(ctypes.Structure):
    pass


BATTERY_WMI_STATUS = _BATTERY_WMI_STATUS
PBATTERY_WMI_STATUS = POINTER(_BATTERY_WMI_STATUS)


class _BATTERY_WMI_RUNTIME(ctypes.Structure):
    pass


BATTERY_WMI_RUNTIME = _BATTERY_WMI_RUNTIME
PBATTERY_WMI_RUNTIME = POINTER(_BATTERY_WMI_RUNTIME)


class _BATTERY_WMI_TEMPERATURE(ctypes.Structure):
    pass


BATTERY_WMI_TEMPERATURE = _BATTERY_WMI_TEMPERATURE
PBATTERY_WMI_TEMPERATURE = POINTER(_BATTERY_WMI_TEMPERATURE)


class _BATTERY_WMI_FULL_CHARGED_CAPACITY(ctypes.Structure):
    pass


BATTERY_WMI_FULL_CHARGED_CAPACITY = _BATTERY_WMI_FULL_CHARGED_CAPACITY
PBATTERY_WMI_FULL_CHARGED_CAPACITY = POINTER(_BATTERY_WMI_FULL_CHARGED_CAPACITY)


class _BATTERY_WMI_CYCLE_COUNT(ctypes.Structure):
    pass


BATTERY_WMI_CYCLE_COUNT = _BATTERY_WMI_CYCLE_COUNT
PBATTERY_WMI_CYCLE_COUNT = POINTER(_BATTERY_WMI_CYCLE_COUNT)


class _BATTERY_WMI_STATIC_DATA(ctypes.Structure):
    pass


BATTERY_WMI_STATIC_DATA = _BATTERY_WMI_STATIC_DATA
PBATTERY_WMI_STATIC_DATA = POINTER(_BATTERY_WMI_STATIC_DATA)


class _BATTERY_WMI_STATUS_CHANGE(ctypes.Structure):
    pass


BATTERY_WMI_STATUS_CHANGE = _BATTERY_WMI_STATUS_CHANGE
PBATTERY_WMI_STATUS_CHANGE = POINTER(_BATTERY_WMI_STATUS_CHANGE)


class _BATTERY_TAG_CHANGE(ctypes.Structure):
    pass


BATTERY_TAG_CHANGE = _BATTERY_TAG_CHANGE
PBATTERY_TAG_CHANGE = POINTER(_BATTERY_TAG_CHANGE)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# batclass.h Abstract: Defines battery class driver interfaces. - -
from pyWinAPI.shared.poclass_h import * # NOQA


# Battery device GUID
BATTERY_STATUS_WMI_GUID = DEFINE_GUID(
    0xFC4670D1,
    0xEBBF,
    0x416E,
    0x87,
    0xCE,
    0x37,
    0x4A,
    0x4E,
    0xBC,
    0x11,
    0x1A
)
BATTERY_RUNTIME_WMI_GUID = DEFINE_GUID(
    0x535A3767,
    0x1AC2,
    0x49BC,
    0xA0,
    0x77,
    0x3F,
    0x7A,
    0x02,
    0xE4,
    0x0A,
    0xEC
)
BATTERY_TEMPERATURE_WMI_GUID = DEFINE_GUID(
    0x1A52A14D,
    0xADCE,
    0x4A44,
    0x9A,
    0x3E,
    0xC8,
    0xD8,
    0xF1,
    0x5F,
    0xF2,
    0xC2
)
BATTERY_FULL_CHARGED_CAPACITY_WMI_GUID = DEFINE_GUID(
    0x40B40565,
    0x96F7,
    0x4435,
    0x86,
    0x94,
    0x97,
    0xE0,
    0xE4,
    0x39,
    0x59,
    0x05
)
BATTERY_CYCLE_COUNT_WMI_GUID = DEFINE_GUID(
    0xEF98DB24,
    0x0014,
    0x4C25,
    0xA5,
    0x0B,
    0xC7,
    0x24,
    0xAE,
    0x5C,
    0xD3,
    0x71
)
BATTERY_STATIC_DATA_WMI_GUID = DEFINE_GUID(
    0x05E1E463,
    0xE4E2,
    0x4EA9,
    0x80,
    0xCB,
    0x9B,
    0xD4,
    0xB3,
    0xCA,
    0x06,
    0x55
)
BATTERY_STATUS_CHANGE_WMI_GUID = DEFINE_GUID(
    0xCDDFA0C3,
    0x7C5B,
    0x4E43,
    0xA0,
    0x34,
    0x05,
    0x9F,
    0xA5,
    0xB8,
    0x43,
    0x64
)
BATTERY_TAG_CHANGE_WMI_GUID = DEFINE_GUID(
    0x5E1F6E19,
    0x8786,
    0x4D23,
    0x94,
    0xFC,
    0x9E,
    0x74,
    0x6B,
    0xD5,
    0xD8,
    0x88
)

_BATCLASS_ = None
if not defined(_BATCLASS_):
    _BATCLASS_ = 1

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION < NTDDI_WINXP:
            # Format of data returned when
            # BATTERY_INFORMATION_LEVEL = BatteryGranularityInformation
            # is an array of BATTERY_REPORTING_SCALE
            _NTPOAPI_ = None
            if not defined(_NTPOAPI_):
                BATTERY_REPORTING_SCALE._fields_ = [
                    ('Granularity', ULONG),
                    ('Capacity', ULONG),
                ]
            # END IF   _NTPOAPI_
        # END IF   (NTDDI_VERSION < NTDDI_WINXP)

        _WINDOWS_ = None
        if not defined(_WINDOWS_):
            # Battery Class - Miniport device driver interfaces
            # NTSTATUS
            # (BCLASS_QUERY_TAG_CALLBACK)(
            # _In_ PVOID Context,
            # _Out_ PULONG BatteryTag
            # );
            BCLASS_QUERY_TAG_CALLBACK = CALLBACK(
                NTSTATUS,
                PVOID,
                PULONG,
            )

            # NTSTATUS
            # (BCLASS_QUERY_INFORMATION_CALLBACK)(
            # _In_ PVOID Context,
            # _In_ ULONG BatteryTag,
            # _In_ BATTERY_QUERY_INFORMATION_LEVEL Level,
            # _In_ LONG AtRate,
            # _Out_writes_bytes_to_(BufferLength, *ReturnedLength) PVOID Buffer,
            # _In_ ULONG BufferLength,
            # _Out_ PULONG ReturnedLength
            # );
            BCLASS_QUERY_INFORMATION_CALLBACK = CALLBACK(
                NTSTATUS,
                PVOID,
                ULONG,
                BATTERY_QUERY_INFORMATION_LEVEL,
                LONG,
                PVOID,
                ULONG,
                PULONG
            )

            # NTSTATUS
            # (BCLASS_QUERY_STATUS_CALLBACK)(
            # _In_ PVOID Context,
            # _In_ ULONG BatteryTag,
            # _Out_ PBATTERY_STATUS BatteryStatus
            # );
            BCLASS_QUERY_STATUS_CALLBACK = CALLBACK(
                NTSTATUS,
                PVOID,
                ULONG,
                PBATTERY_STATUS,
            )

            BATTERY_NOTIFY._fields_ = [
                ('PowerState', ULONG),
                ('LowCapacity', ULONG),
                ('HighCapacity', ULONG),
            ]

            # NTSTATUS
            # (BCLASS_SET_STATUS_NOTIFY_CALLBACK)(
            # _In_ PVOID Context,
            # _In_ ULONG BatteryTag,
            # _In_ PBATTERY_NOTIFY BatteryNotify
            # );
            BCLASS_SET_STATUS_NOTIFY_CALLBACK = CALLBACK(
                NTSTATUS,
                PVOID,
                ULONG,
                PBATTERY_NOTIFY
            )

            # NTSTATUS
            # (BCLASS_SET_INFORMATION_CALLBACK)(
            # _In_ PVOID Context,
            # _In_ ULONG BatteryTag,
            # _In_ BATTERY_SET_INFORMATION_LEVEL Level,
            # _In_opt_ PVOID Buffer
            # );
            BCLASS_SET_INFORMATION_CALLBACK = CALLBACK(
                NTSTATUS,
                PVOID,
                ULONG,
                BATTERY_SET_INFORMATION_LEVEL,
                PVOID
            )

            # NTSTATUS
            # (BCLASS_DISABLE_STATUS_NOTIFY_CALLBACK)(
            # _In_ PVOID Context
            # );
            BCLASS_DISABLE_STATUS_NOTIFY_CALLBACK = CALLBACK(
                NTSTATUS,
                PVOID
            )

            PBCLASS_QUERY_TAG_CALLBACK = POINTER(BCLASS_QUERY_TAG_CALLBACK)
            BCLASS_QUERY_TAG = PBCLASS_QUERY_TAG_CALLBACK

            PBCLASS_QUERY_INFORMATION_CALLBACK = POINTER(BCLASS_QUERY_INFORMATION_CALLBACK)
            BCLASS_QUERY_INFORMATION = PBCLASS_QUERY_INFORMATION_CALLBACK

            PBCLASS_QUERY_STATUS_CALLBACK = POINTER(BCLASS_QUERY_STATUS_CALLBACK)
            BCLASS_QUERY_STATUS = PBCLASS_QUERY_STATUS_CALLBACK

            PBCLASS_SET_STATUS_NOTIFY_CALLBACK = POINTER(BCLASS_SET_STATUS_NOTIFY_CALLBACK)
            BCLASS_SET_STATUS_NOTIFY = PBCLASS_SET_STATUS_NOTIFY_CALLBACK

            PBCLASS_SET_INFORMATION_CALLBACK = POINTER(BCLASS_SET_INFORMATION_CALLBACK)
            BCLASS_SET_INFORMATION = PBCLASS_SET_INFORMATION_CALLBACK

            PBCLASS_DISABLE_STATUS_NOTIFY_CALLBACK = POINTER(BCLASS_DISABLE_STATUS_NOTIFY_CALLBACK)
            BCLASS_DISABLE_STATUS_NOTIFY = PBCLASS_DISABLE_STATUS_NOTIFY_CALLBACK

            from pyWinAPI.missing_structures_h import * # NOQA

            BATTERY_MINIPORT_INFO._fields_ = [
                ('MajorVersion', USHORT),
                ('MinorVersion', USHORT),
                # Miniport context
                ('Context', PVOID),
                ('QueryTag', BCLASS_QUERY_TAG),
                ('QueryInformation', BCLASS_QUERY_INFORMATION),
                ('SetInformation', BCLASS_SET_INFORMATION),
                ('QueryStatus', BCLASS_QUERY_STATUS),
                ('SetStatusNotify', BCLASS_SET_STATUS_NOTIFY),
                ('DisableStatusNotify', BCLASS_DISABLE_STATUS_NOTIFY),
                ('Pdo', PDEVICE_OBJECT),
                ('DeviceName', PUNICODE_STRING),
            ]

            BATTERY_MINIPORT_INFO_V1_1._fields_ = [
                ('MajorVersion', USHORT),
                ('MinorVersion', USHORT),
                # Miniport context
                ('Context', PVOID),
                ('QueryTag', BCLASS_QUERY_TAG),
                ('QueryInformation', BCLASS_QUERY_INFORMATION),
                ('SetInformation', BCLASS_SET_INFORMATION),
                ('QueryStatus', BCLASS_QUERY_STATUS),
                ('SetStatusNotify', BCLASS_SET_STATUS_NOTIFY),
                ('DisableStatusNotify', BCLASS_DISABLE_STATUS_NOTIFY),
                ('Pdo', PDEVICE_OBJECT),
                ('DeviceName', PUNICODE_STRING),
                ('Fdo', PDEVICE_OBJECT),
            ]
            BATTERY_CLASS_MAJOR_VERSION = 0x0001
            BATTERY_CLASS_MINOR_VERSION = 0x0000
            BATTERY_CLASS_MINOR_VERSION_1 = 0x0001

            if NTDDI_VERSION >= NTDDI_WINXP:
                # WMI data block structures
                _BATTERY_WMI_STATUS._fields_ = [
                    ('Tag', ULONG),
                    ('RemainingCapacity', ULONG),
                    ('ChargeRate', LONG),
                    ('DischargeRate', LONG),
                    ('Voltage', ULONG),
                    ('PowerOnline', BOOLEAN),
                    ('Charging', BOOLEAN),
                    ('Discharging', BOOLEAN),
                    ('Critical', BOOLEAN),
                ]

                _BATTERY_WMI_RUNTIME._fields_ = [
                    ('Tag', ULONG),
                    ('EstimatedRuntime', ULONG),
                ]

                _BATTERY_WMI_TEMPERATURE._fields_ = [
                    ('Tag', ULONG),
                    ('Temperature', ULONG),
                ]

                _BATTERY_WMI_FULL_CHARGED_CAPACITY._fields_ = [
                    ('Tag', ULONG),
                    ('FullChargedCapacity', ULONG),
                ]

                _BATTERY_WMI_CYCLE_COUNT._fields_ = [
                    ('Tag', ULONG),
                    ('CycleCount', ULONG),
                ]

                _BATTERY_WMI_STATIC_DATA._fields_ = [
                    ('Tag', ULONG),
                    ('ManufactureDate', WCHAR * 25),
                    ('Granularity', BATTERY_REPORTING_SCALE * 4),
                    ('Capabilities', ULONG),
                    ('Technology', UCHAR),
                    ('Chemistry', ULONG),
                    ('DesignedCapacity', ULONG),
                    ('DefaultAlert1', ULONG),
                    ('DefaultAlert2', ULONG),
                    ('CriticalBias', ULONG),
                    ('Strings', WCHAR * 1),
                ]

                _BATTERY_WMI_STATUS_CHANGE._fields_ = [
                    ('Tag', ULONG),
                    ('PowerOnline', BOOLEAN),
                    ('Charging', BOOLEAN),
                    ('Discharging', BOOLEAN),
                    ('Critical', BOOLEAN),
                ]

                _BATTERY_TAG_CHANGE._fields_ = [
                    ('Tag', ULONG),
                ]
            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

            # Battery class driver functions
            BATTERYCLASS = None
            if not defined(BATTERYCLASS):
                BATTERYCLASSAPI = DECLSPEC_IMPORT
            else:
                BATTERYCLASSAPI = 1
            # END IF

            battc = ctypes.windll.BATTC

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # _Check_return_
            # NTSTATUS
            # BATTERYCLASSAPI
            # BatteryClassInitializeDevice(
            # _In_ PBATTERY_MINIPORT_INFO MiniportInfo,
            # _Out_ PVOID *ClassData
            # );
            BatteryClassInitializeDevice = battc.BatteryClassInitializeDevice
            BatteryClassInitializeDevice.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # NTSTATUS
            # BATTERYCLASSAPI
            # BatteryClassUnload(
            # _In_ PVOID ClassData
            # );
            BatteryClassUnload = battc.BatteryClassUnload
            BatteryClassUnload.restype = NTSTATUS

            # _IRQL_requires_max_(PASSIVE_LEVEL)
            # _Check_return_
            # NTSTATUS
            # BATTERYCLASSAPI
            # BatteryClassIoctl(
            # _In_ PVOID ClassData,
            # _Inout_ PIRP Irp
            # );
            BatteryClassIoctl = battc.BatteryClassIoctl
            BatteryClassIoctl.restype = NTSTATUS

            if NTDDI_VERSION >= NTDDI_WINXP:
                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # _Check_return_
                # NTSTATUS
                # BATTERYCLASSAPI
                # BatteryClassSystemControl(
                # _In_ PVOID ClassData,
                # _In_ PVOID WmiLibContext, // PWMILIB_CONTEXT
                # _In_ PDEVICE_OBJECT  DeviceObject,
                # _Inout_ PIRP Irp,
                # _Out_ PVOID Disposition // PSYSCTL_IRP_DISPOSITION
                # );
                BatteryClassSystemControl = battc.BatteryClassSystemControl
                BatteryClassSystemControl.restype = NTSTATUS

                # _IRQL_requires_max_(PASSIVE_LEVEL)
                # _Check_return_
                # NTSTATUS
                # BATTERYCLASSAPI
                # BatteryClassQueryWmiDataBlock(
                # _In_ PVOID ClassData,
                # _Inout_ PDEVICE_OBJECT DeviceObject,
                # _Inout_ PIRP Irp,
                # _In_ ULONG GuidIndex,
                # _Out_writes_(1) PULONG InstanceLengthArray,
                # _In_ ULONG OutBufferSize,
                # _Out_writes_bytes_opt_(OutBufferSize) PUCHAR Buffer
                # );
                BatteryClassQueryWmiDataBlock = (
                    battc.BatteryClassQueryWmiDataBlock
                )
                BatteryClassQueryWmiDataBlock.restype = NTSTATUS

            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)
            # _IRQL_requires_max_(DISPATCH_LEVEL)
            # NTSTATUS
            # BATTERYCLASSAPI
            # BatteryClassStatusNotify(
            # _In_ PVOID ClassData
            # );
            BatteryClassStatusNotify = battc.BatteryClassStatusNotify
            BatteryClassStatusNotify.restype = NTSTATUS

        # END IF   _WINDOWS_
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _BATCLASS_
