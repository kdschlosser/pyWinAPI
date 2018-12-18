import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _BATTERY_QUERY_INFORMATION(ctypes.Structure):
    pass


BATTERY_QUERY_INFORMATION = _BATTERY_QUERY_INFORMATION
PBATTERY_QUERY_INFORMATION = POINTER(_BATTERY_QUERY_INFORMATION)


class _BATTERY_INFORMATION(ctypes.Structure):
    pass


BATTERY_INFORMATION = _BATTERY_INFORMATION
PBATTERY_INFORMATION = POINTER(_BATTERY_INFORMATION)


class _BATTERY_CHARGING_SOURCE(ctypes.Structure):
    pass


BATTERY_CHARGING_SOURCE = _BATTERY_CHARGING_SOURCE
PBATTERY_CHARGING_SOURCE = POINTER(_BATTERY_CHARGING_SOURCE)


class _BATTERY_CHARGING_SOURCE_INFORMATION(ctypes.Structure):
    pass


BATTERY_CHARGING_SOURCE_INFORMATION = _BATTERY_CHARGING_SOURCE_INFORMATION
PBATTERY_CHARGING_SOURCE_INFORMATION = POINTER(_BATTERY_CHARGING_SOURCE_INFORMATION)


class _BATTERY_SET_INFORMATION(ctypes.Structure):
    pass


BATTERY_SET_INFORMATION = _BATTERY_SET_INFORMATION
PBATTERY_SET_INFORMATION = POINTER(_BATTERY_SET_INFORMATION)


class _BATTERY_CHARGER_STATUS(ctypes.Structure):
    pass


BATTERY_CHARGER_STATUS = _BATTERY_CHARGER_STATUS
PBATTERY_CHARGER_STATUS = POINTER(_BATTERY_CHARGER_STATUS)


class _BATTERY_USB_CHARGER_STATUS(ctypes.Structure):
    pass


BATTERY_USB_CHARGER_STATUS = _BATTERY_USB_CHARGER_STATUS
PBATTERY_USB_CHARGER_STATUS = POINTER(_BATTERY_USB_CHARGER_STATUS)


class _BATTERY_WAIT_STATUS(ctypes.Structure):
    pass


BATTERY_WAIT_STATUS = _BATTERY_WAIT_STATUS
PBATTERY_WAIT_STATUS = POINTER(_BATTERY_WAIT_STATUS)


class _BATTERY_STATUS(ctypes.Structure):
    pass


BATTERY_STATUS = _BATTERY_STATUS
PBATTERY_STATUS = POINTER(_BATTERY_STATUS)


class _BATTERY_MANUFACTURE_DATE(ctypes.Structure):
    pass


BATTERY_MANUFACTURE_DATE = _BATTERY_MANUFACTURE_DATE
PBATTERY_MANUFACTURE_DATE = POINTER(_BATTERY_MANUFACTURE_DATE)


class _THERMAL_INFORMATION(ctypes.Structure):
    pass


THERMAL_INFORMATION = _THERMAL_INFORMATION
PTHERMAL_INFORMATION = POINTER(_THERMAL_INFORMATION)


class _THERMAL_WAIT_READ(ctypes.Structure):
    pass


THERMAL_WAIT_READ = _THERMAL_WAIT_READ
PTHERMAL_WAIT_READ = POINTER(_THERMAL_WAIT_READ)


class _THERMAL_POLICY(ctypes.Structure):
    pass


THERMAL_POLICY = _THERMAL_POLICY
PTHERMAL_POLICY = POINTER(_THERMAL_POLICY)


class PROCESSOR_OBJECT_INFO(ctypes.Structure):
    pass


PPROCESSOR_OBJECT_INFO = POINTER(PROCESSOR_OBJECT_INFO)


class PROCESSOR_OBJECT_INFO_EX(ctypes.Structure):
    pass


PPROCESSOR_OBJECT_INFO_EX = POINTER(PROCESSOR_OBJECT_INFO_EX)


class _PCC_HEADER(ctypes.Structure):
    pass


PCC_HEADER = _PCC_HEADER
PPCC_HEADER = POINTER(_PCC_HEADER)


class _PCC_INPUT_BUFFER(ctypes.Structure):
    pass


PCC_INPUT_BUFFER = _PCC_INPUT_BUFFER
PPCC_INPUT_BUFFER = POINTER(_PCC_INPUT_BUFFER)


class _PCC_OUTPUT_BUFFER(ctypes.Union):
    pass


PCC_OUTPUT_BUFFER = _PCC_OUTPUT_BUFFER
PPCC_OUTPUT_BUFFER = POINTER(_PCC_OUTPUT_BUFFER)


class _PROCESSOR_PCC_INTERFACE_STANDARD(ctypes.Structure):
    pass


PROCESSOR_PCC_INTERFACE_STANDARD = _PROCESSOR_PCC_INTERFACE_STANDARD
PPROCESSOR_PCC_INTERFACE_STANDARD = POINTER(_PROCESSOR_PCC_INTERFACE_STANDARD)


class _THERMAL_COOLING_INTERFACE(ctypes.Structure):
    pass


THERMAL_COOLING_INTERFACE = _THERMAL_COOLING_INTERFACE
PTHERMAL_COOLING_INTERFACE = POINTER(_THERMAL_COOLING_INTERFACE)


class _WAKE_ALARM_INFORMATION(ctypes.Structure):
    pass


WAKE_ALARM_INFORMATION = _WAKE_ALARM_INFORMATION
PWAKE_ALARM_INFORMATION = POINTER(_WAKE_ALARM_INFORMATION)


class _ACPI_REAL_TIME(ctypes.Structure):
    pass


ACPI_REAL_TIME = _ACPI_REAL_TIME
PACPI_REAL_TIME = POINTER(_ACPI_REAL_TIME)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# poclass.h Abstract: Defines power policy device driver interfaces. Revision
# History: - -
# GUIDs are defined outside ifdef __POCLASS_ so that they can be instantiated
# easily using <initguid.h>.
# Custom device properties...
from pyWinAPI.shared.devpropdef_h import * # NOQA
from pyWinAPI.shared.winapifamily_h import * # NOQA


# This is of type DEVPROP_TYPE_UINT32 and represents the NT processor
# number.
PROCESSOR_NUMBER_PKEY = DEFINE_DEVPROPKEY(
    0x5724C81D,
    0xD5AF,
    0x4C1F,
    0xA1,
    0x03,
    0xA0,
    0x6E,
    0x28,
    0xF2,
    0x04,
    0xC6,
    0x1
)


# Power management policy device GUIDs
GUID_DEVICE_BATTERY = DEFINE_GUID(
    0x72631E54,
    0x78A4,
    0x11D0,
    0xBC,
    0xF7,
    0x00,
    0xAA,
    0x00,
    0xB7,
    0xB3,
    0x2A
)
GUID_DEVICE_APPLICATIONLAUNCH_BUTTON = DEFINE_GUID(
    0x629758EE,
    0x986E,
    0x4D9E,
    0x8E,
    0x47,
    0xDE,
    0x27,
    0xF8,
    0xAB,
    0x05,
    0x4D
)
GUID_DEVICE_SYS_BUTTON = DEFINE_GUID(
    0x4AFA3D53,
    0x74A7,
    0x11D0,
    0xBE,
    0x5E,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x57
)
GUID_DEVICE_LID = DEFINE_GUID(
    0x4AFA3D52,
    0x74A7,
    0x11D0,
    0xBE,
    0x5E,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x57
)
GUID_DEVICE_THERMAL_ZONE = DEFINE_GUID(
    0x4AFA3D51,
    0x74A7,
    0x11D0,
    0xBE,
    0x5E,
    0x00,
    0xA0,
    0xC9,
    0x06,
    0x28,
    0x57
)
GUID_DEVICE_FAN = DEFINE_GUID(
    0x05ECD13D,
    0x81DA,
    0x4A2A,
    0x8A,
    0x4C,
    0x52,
    0x4F,
    0x23,
    0xDD,
    0x4D,
    0xC9
)
GUID_DEVICE_PROCESSOR = DEFINE_GUID(
    0x97FADB10,
    0x4E33,
    0x40AE,
    0x35,
    0x9C,
    0x8B,
    0xEF,
    0x02,
    0x9D,
    0xBD,
    0xD0
)
GUID_DEVICE_MEMORY = DEFINE_GUID(
    0x3FD0F03D,
    0x92E0,
    0x45FB,
    0xB7,
    0x5C,
    0x5E,
    0xD8,
    0xFF,
    0xB0,
    0x10,
    0x21
)
GUID_DEVICE_ACPI_TIME = DEFINE_GUID(
    0x97F99BF6,
    0x4497,
    0x4F18,
    0xBB,
    0x22,
    0x4B,
    0x9F,
    0xB2,
    0xFB,
    0xEF,
    0x9C
)
GUID_DEVICE_MESSAGE_INDICATOR = DEFINE_GUID(
    0xCD48A365,
    0xFA94,
    0x4CE2,
    0xA2,
    0x32,
    0xA1,
    0xB7,
    0x64,
    0xE5,
    0xD8,
    0xB4
)

# copied from hidclass.h
GUID_CLASS_INPUT = DEFINE_GUID(
    0x4D1E55B2,
    0xF16F,
    0x11CF,
    0x88,
    0xCB,
    0x00,
    0x11,
    0x11,
    0x00,
    0x00,
    0x30
)

# {DBE4373D - 3C81 - 40cb - ACE4 - E0E5D05F0C9F}
GUID_DEVINTERFACE_THERMAL_COOLING = DEFINE_GUID(
    0xDBE4373D,
    0x3C81,
    0x40CB,
    0xAC,
    0xE4,
    0xE0,
    0xE5,
    0xD0,
    0x5F,
    0xC,
    0x9F
)

_POCLASS_ = None
if not defined(_POCLASS_):
    _POCLASS_ = 1

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Battery driver interface
        # (devices of registrying as GUID_DEVICE_BATTERY)
        class BATTERY_QUERY_INFORMATION_LEVEL(ENUM):
            BatteryInformation = 1
            BatteryGranularityInformation = 2
            BatteryTemperature = 3
            BatteryEstimatedTime = 4
            BatteryDeviceName = 5
            BatteryManufactureDate = 6
            BatteryManufactureName = 7
            BatteryUniqueID = 8
            BatterySerialNumber = 9

        BatteryInformation = BATTERY_QUERY_INFORMATION_LEVEL.BatteryInformation
        BatteryGranularityInformation = BATTERY_QUERY_INFORMATION_LEVEL.BatteryGranularityInformation
        BatteryTemperature = BATTERY_QUERY_INFORMATION_LEVEL.BatteryTemperature
        BatteryEstimatedTime = BATTERY_QUERY_INFORMATION_LEVEL.BatteryEstimatedTime
        BatteryDeviceName = BATTERY_QUERY_INFORMATION_LEVEL.BatteryDeviceName
        BatteryManufactureDate = BATTERY_QUERY_INFORMATION_LEVEL.BatteryManufactureDate
        BatteryManufactureName = BATTERY_QUERY_INFORMATION_LEVEL.BatteryManufactureName
        BatteryUniqueID = BATTERY_QUERY_INFORMATION_LEVEL.BatteryUniqueID
        BatterySerialNumber = BATTERY_QUERY_INFORMATION_LEVEL.BatterySerialNumber

        _BATTERY_QUERY_INFORMATION._fields_ = [
            ('BatteryTag', ULONG),
            ('InformationLevel', BATTERY_QUERY_INFORMATION_LEVEL),
            ('AtRate', ULONG),
        ]

        _BATTERY_INFORMATION._fields_ = [
            ('Capabilities', ULONG),
            ('Technology', UCHAR),
            ('Reserved', UCHAR * 3),
            ('Chemistry', UCHAR * 4),
            ('DesignedCapacity', ULONG),
            ('FullChargedCapacity', ULONG),
            ('DefaultAlert1', ULONG),
            ('DefaultAlert2', ULONG),
            ('CriticalBias', ULONG),
            ('CycleCount', ULONG),
        ]

        # BATTERY_INFORMATION.*Capacity constants
        BATTERY_UNKNOWN_CAPACITY = 0xFFFFFFFF
        UNKNOWN_CAPACITY = BATTERY_UNKNOWN_CAPACITY

        # BATTERY_INFORMATION.Capabilities flags
        BATTERY_SYSTEM_BATTERY = 0x80000000
        BATTERY_CAPACITY_RELATIVE = 0x40000000
        BATTERY_IS_SHORT_TERM = 0x20000000
        BATTERY_SEALED = 0x10000000
        BATTERY_SET_CHARGE_SUPPORTED = 0x00000001
        BATTERY_SET_DISCHARGE_SUPPORTED = 0x00000002
        BATTERY_SET_CHARGINGSOURCE_SUPPORTED = 0x00000004
        BATTERY_SET_CHARGER_ID_SUPPORTED = 0x00000008


        # BatteryEstimatedTime constant
        BATTERY_UNKNOWN_TIME = 0xFFFFFFFF
        BATTERY_UNKNOWN_CURRENT = 0xFFFFFFFF
        UNKNOWN_CURRENT = BATTERY_UNKNOWN_CURRENT

        # AC type explicitly set to maintain backwards compatibility
        # (the previous enum member BatteryChargingSourceType_None was removed).
        #
        class _BATTERY_CHARGING_SOURCE_TYPE(ENUM):
            BatteryChargingSourceType_AC = 1
            BatteryChargingSourceType_USB = 2
            BatteryChargingSourceType_Wireless = 3
            BatteryChargingSourceType_Max = 4

        BATTERY_CHARGING_SOURCE_TYPE = _BATTERY_CHARGING_SOURCE_TYPE
        PBATTERY_CHARGING_SOURCE_TYPE = POINTER(_BATTERY_CHARGING_SOURCE_TYPE)

        _BATTERY_CHARGING_SOURCE._fields_ = [
            ('Type', BATTERY_CHARGING_SOURCE_TYPE),
            ('MaxCurrent', ULONG),
        ]

        BATTERY_CHARGER_ID = GUID
        PBATTERY_CHARGER_ID = POINTER(GUID)

        # New structure for Windows Phone specific feature: Source Change
        # Notification.
        _BATTERY_CHARGING_SOURCE_INFORMATION._fields_ = [
            ('Type', BATTERY_CHARGING_SOURCE_TYPE),
            ('SourceOnline', BOOLEAN),
        ]


        # Physical USB port types.
        class _USB_CHARGER_PORT(ENUM):
            UsbChargerPort_Legacy = 1
            UsbChargerPort_TypeC = 2
            UsbChargerPort_Max = 3

        USB_CHARGER_PORT = _USB_CHARGER_PORT
        PUSB_CHARGER_PORT = POINTER(_USB_CHARGER_PORT)


        # IOCTL_BATTERY_SET_INFORMATION information levels
        class BATTERY_SET_INFORMATION_LEVEL(ENUM):
            BatteryCriticalBias = 1
            BatteryCharge = 2
            BatteryDischarge = 3
            BatteryChargingSource = 4
            BatteryChargerId = 5
            BatteryChargerStatus = 6

        BatteryCriticalBias = BATTERY_SET_INFORMATION_LEVEL.BatteryCriticalBias
        BatteryCharge = BATTERY_SET_INFORMATION_LEVEL.BatteryCharge
        BatteryDischarge = BATTERY_SET_INFORMATION_LEVEL.BatteryDischarge
        BatteryChargingSource = BATTERY_SET_INFORMATION_LEVEL.BatteryChargingSource
        BatteryChargerId = BATTERY_SET_INFORMATION_LEVEL.BatteryChargerId
        BatteryChargerStatus = BATTERY_SET_INFORMATION_LEVEL.BatteryChargerStatus


        # Generic Payload for IOCTL_BATTERY_SET_INFORMATION.
        _BATTERY_SET_INFORMATION._fields_ = [
            ('BatteryTag', ULONG),
            ('InformationLevel', BATTERY_SET_INFORMATION_LEVEL),
            ('Buffer', UCHAR * 1),
        ]


        # Payload for IOCTL_BATTERY_SET_INFORMATION information level
        # BatteryChargerStatus.
        # CAD uses this structure to identify charger source properties to the
        # Battery.
        _BATTERY_CHARGER_STATUS._fields_ = [
            # Identifies the charger type.
            ('Type', BATTERY_CHARGING_SOURCE_TYPE),
            # charging source type identified by Type.
            ('VaData', ULONG * 1),
        ]

        # Payload for IOCTL_BATTERY_SET_INFORMATION/BatteryChargerStatus
        # (CAD - >Battery)
        # when Type is set to BatteryChargingSourceType_USB.
        # CAD uses this structure to identify charger source properties to the
        # Battery.
        _BATTERY_USB_CHARGER_STATUS._fields_ = [
            # This value will be set to BatteryChargingSourceType_USB.
            ('Type', BATTERY_CHARGING_SOURCE_TYPE),
            # Should not be interpreted by BM.
            ('Reserved', ULONG),
            # Flags.
            ('Flags', ULONG),
            # in such case zero should be interpreted as unknown value.
            ('MaxCurrent', ULONG),
            # in such case zero should be interpreted as unknown value.
            ('Voltage', ULONG),
            # USB Port Type.
            ('PortType', USB_CHARGER_PORT),
            # When set to 0 indicates that port information is unavailable.
            ('PortId', ULONGLONG),
            # 64 - bit systems.
            ('PowerSourceInformation', PVOID),
            # passed from charging port uninterpreted by CAD.
            ('OemCharger', BATTERY_CHARGER_ID),
        ]


        # BATTERY_USB_CHARGER_STATUS.Flags field.
        # Indicates Type - C port running in the Default USB mode.
        BATTERY_USB_CHARGER_STATUS_FN_DEFAULT_USB = 0x00000001


        _BATTERY_WAIT_STATUS._fields_ = [
            ('BatteryTag', ULONG),
            ('Timeout', ULONG),
            ('PowerState', ULONG),
            ('LowCapacity', ULONG),
            ('HighCapacity', ULONG),
        ]

        _BATTERY_STATUS._fields_ = [
            ('PowerState', ULONG),
            ('Capacity', ULONG),
            ('Voltage', ULONG),
            ('Rate', LONG),
        ]

        # Battery Status Constants
        BATTERY_UNKNOWN_VOLTAGE = 0xFFFFFFFF
        BATTERY_UNKNOWN_RATE = 0x80000000
        UNKNOWN_RATE = BATTERY_UNKNOWN_RATE
        UNKNOWN_VOLTAGE = BATTERY_UNKNOWN_VOLTAGE

        # PowerState flags
        BATTERY_POWER_ON_LINE = 0x00000001
        BATTERY_DISCHARGING = 0x00000002
        BATTERY_CHARGING = 0x00000004
        BATTERY_CRITICAL = 0x00000008

        # Max battery driver BATTERY_QUERY_INFORMATION_LEVEL string storage
        # size in bytes.
        MAX_BATTERY_STRING_SIZE = 128

        # Struct for accessing the packed date format in
        # BatteryManufactureDate.
        _BATTERY_MANUFACTURE_DATE._fields_ = [
            ('Day', UCHAR),
            ('Month', UCHAR),
            ('Year', USHORT),
        ]

        from pyWinAPI.shared.devioctl_h import * # NOQA
        from pyWinAPI.km.wdm_h import * # NOQA
        from pyWinAPI.um.winnt_h import * # NOQA

        # battery
        IOCTL_BATTERY_QUERY_TAG = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x10,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        IOCTL_BATTERY_QUERY_INFORMATION = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x11,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        IOCTL_BATTERY_SET_INFORMATION = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x12,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_BATTERY_QUERY_STATUS = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x13,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )

        # New ioctl for Windows Phone specific feature: Source Change
        # Notificaton.
        IOCTL_BATTERY_CHARGING_SOURCE_CHANGE = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x14,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        BATTERY_TAG_INVALID = 0

        # Thermal Zone driver interface
        # (devices of registrying as GUID_DEVICE_THERMAL_ZONE)
        MAX_ACTIVE_COOLING_LEVELS = 10

        # This structure has been depricated and the THERMAL_INFORMATION_EX
        # structure should be used. THERMAL_INFORMATION has been left here for
        # backward compatibility with the thermal WMI interface.
        _THERMAL_INFORMATION._fields_ = [
            ('ThermalStamp', ULONG),
            ('ThermalConstant1', ULONG),
            ('ThermalConstant2', ULONG),
            ('Processors', KAFFINITY),
            ('SamplingPeriod', ULONG),
            ('CurrentTemperature', ULONG),
            ('PassiveTripPoint', ULONG),
            ('CriticalTripPoint', ULONG),
            ('ActiveTripPointCount', UCHAR),
            ('ActiveTripPoint', ULONG * MAX_ACTIVE_COOLING_LEVELS),
        ]
        ACTIVE_COOLING = 0x0
        PASSIVE_COOLING = 0x1

        _THERMAL_WAIT_READ._fields_ = [
            ('Timeout', ULONG),
            ('LowTemperature', ULONG),
            ('HighTemperature', ULONG),
        ]
        TZ_ACTIVATION_REASON_THERMAL = 0x00000001
        TZ_ACTIVATION_REASON_CURRENT = 0x00000002

        _THERMAL_POLICY._fields_ = [
            ('Version', ULONG),
            ('WaitForUpdate', BOOLEAN),
            ('Hibernate', BOOLEAN),
            ('Critical', BOOLEAN),
            ('ThermalStandby', BOOLEAN),
            ('ActivationReasons', ULONG),
            ('PassiveLimit', ULONG),
            ('ActiveLevel', ULONG),
            ('OverThrottled', BOOLEAN),
        ]
        THERMAL_POLICY_VERSION_1 = 1
        THERMAL_POLICY_VERSION_2 = 2

        # thermal
        IOCTL_THERMAL_QUERY_INFORMATION = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x20,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        IOCTL_THERMAL_SET_COOLING_POLICY = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x21,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_RUN_ACTIVE_COOLING_METHOD = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x22,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_THERMAL_SET_PASSIVE_LIMIT = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x23,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_THERMAL_READ_TEMPERATURE = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x24,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        IOCTL_THERMAL_READ_POLICY = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x25,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )

        # Lid class driver functions
        IOCTL_QUERY_LID = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x30,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )

        # Switch class driver functions
        IOCTL_NOTIFY_SWITCH_EVENT = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x40,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )

        # System button class driver functions
        IOCTL_GET_SYS_BUTTON_CAPS = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x50,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        IOCTL_GET_SYS_BUTTON_EVENT = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x51,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )
        SYS_BUTTON_POWER = 0x00000001
        SYS_BUTTON_SLEEP = 0x00000002
        SYS_BUTTON_LID = 0x00000004
        SYS_BUTTON_WAKE = 0x80000000

        # Lid - specific state embedded in the button event irp.
        SYS_BUTTON_LID_STATE_MASK = 0x00030000
        SYS_BUTTON_LID_OPEN = 0x00010000
        SYS_BUTTON_LID_CLOSED = 0x00020000
        SYS_BUTTON_LID_INITIAL = 0x00040000
        SYS_BUTTON_LID_CHANGED = 0x00080000

        # Processor object class driver functions
        PROCESSOR_OBJECT_INFO._fields_ = [
            ('PhysicalID', ULONG),
            ('PBlkAddress', ULONG),
            ('PBlkLength', UCHAR),
        ]

        PROCESSOR_OBJECT_INFO_EX._fields_ = [
            ('PhysicalID', ULONG),
            ('PBlkAddress', ULONG),
            ('PBlkLength', UCHAR),
            ('InitialApicId', ULONG),
        ]
        IOCTL_GET_PROCESSOR_OBJ_INFO = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x60,
            METHOD_BUFFERED,
            FILE_READ_ACCESS,
        )

        _WINDOWS_ = None
        if not defined(_WINDOWS_):
            # PCC processor power management interface
            class SupportedFeatures(ctypes.Union):
                pass


            class _Struct_1(ctypes.Structure):
                pass


            _Struct_1._fields_ = [
                # 0
                ('SciDoorbell', ULONG, 1),
                # 31:1
                ('Reserved', ULONG, 31),
            ]
            SupportedFeatures._Struct_1 = _Struct_1

            SupportedFeatures._anonymous_ = (
                '_Struct_1',
            )

            SupportedFeatures._fields_ = [
                ('_Struct_1', SupportedFeatures._Struct_1),
                ('AsULong', ULONG),
            ]
            _PCC_HEADER.SupportedFeatures = SupportedFeatures


            class Command(ctypes.Union):
                pass


            class _Struct_1(ctypes.Structure):
                pass


            _Struct_1._fields_ = [
                # 7:0
                ('CommandCode', USHORT, 8),
                # 14:8
                ('ReservedZ', USHORT, 7),
                # 15
                ('SciDoorbell', USHORT, 1),
            ]
            Command._Struct_1 = _Struct_1

            Command._anonymous_ = (
                '_Struct_1',
            )

            Command._fields_ = [
                ('_Struct_1', Command._Struct_1),
                ('AsUShort', USHORT),
            ]
            _PCC_HEADER.Command = Command


            class Status(ctypes.Union):
                pass


            class _Struct_1(ctypes.Structure):
                pass


            _Struct_1._fields_ = [
                # 0
                ('CommandComplete', USHORT, 1),
                # 1
                ('SciReceived', USHORT, 1),
                # 2
                ('Error', USHORT, 1),
                # 15:3
                ('Reserved', USHORT, 13),
            ]
            Status._Struct_1 = _Struct_1

            Status._anonymous_ = (
                '_Struct_1',
            )

            Status._fields_ = [
                ('_Struct_1', Status._Struct_1),
                ('AsUShort', USHORT),
            ]
            _PCC_HEADER.Status = Status

            _PCC_HEADER._fields_ = [
                ('Signature', ULONG),
                ('HeaderLength', USHORT),
                ('MajorVersion', UCHAR),
                ('MinorVersion', UCHAR),
                ('SupportedFeatures', _PCC_HEADER.SupportedFeatures),
                ('Command', _PCC_HEADER.Command),
                ('Status', _PCC_HEADER.Status),
                ('Latency', ULONG),
                ('MinimumCommandInterval', ULONG),
                ('MaximumCommandInterval', ULONG),
                ('NominalFrequency', ULONG),
                ('MinimumFrequency', ULONG),
                ('MinimumUnthrottledFrequency', ULONG),
            ]


            class _Union_1(ctypes.Union):
                pass


            class GetAverageFrequency(ctypes.Structure):
                pass


            GetAverageFrequency._fields_ = [
                ('ReservedZ', UCHAR * 3),
            ]
            _Union_1.GetAverageFrequency = GetAverageFrequency


            class SetDesiredFrequency(ctypes.Structure):
                pass


            SetDesiredFrequency._fields_ = [
                ('DesiredFrequency', UCHAR),
                ('ReservedZ', UCHAR * 2),
            ]
            _Union_1.SetDesiredFrequency = SetDesiredFrequency

            _Union_1._fields_ = [
                ('GetAverageFrequency', _Union_1.GetAverageFrequency),
                ('SetDesiredFrequency', _Union_1.SetDesiredFrequency),
            ]
            _PCC_INPUT_BUFFER._Union_1 = _Union_1

            _PCC_INPUT_BUFFER._anonymous_ = (
                '_Union_1',
            )

            _PCC_INPUT_BUFFER._fields_ = [
                ('ControlEnabled', UCHAR),
                ('_Union_1', _PCC_INPUT_BUFFER._Union_1),
            ]


            class GetAverageFrequency(ctypes.Structure):
                pass


            GetAverageFrequency._fields_ = [
                ('AverageFrequency', UCHAR),
                ('FrequencyLimit', UCHAR),
                ('Reserved', UCHAR * 2),
            ]
            _PCC_OUTPUT_BUFFER.GetAverageFrequency = GetAverageFrequency


            class SetDesiredFrequency(ctypes.Structure):
                pass


            SetDesiredFrequency._fields_ = [
                ('Reserved', UCHAR * 4),
            ]
            _PCC_OUTPUT_BUFFER.SetDesiredFrequency = SetDesiredFrequency

            _PCC_OUTPUT_BUFFER._fields_ = [
                ('GetAverageFrequency', _PCC_OUTPUT_BUFFER.GetAverageFrequency),
                ('SetDesiredFrequency', _PCC_OUTPUT_BUFFER.SetDesiredFrequency),
            ]

            # VOID
            # (PROCESSOR_PCC_DOORBELL_CALLBACK)(
            # _In_ ULONG Status,
            # _In_ ULONG_PTR Context
            # );
            PROCESSOR_PCC_DOORBELL_CALLBACK = CALLBACK(
                VOID,
                ULONG,
                ULONG_PTR
            )

            PPROCESSOR_PCC_DOORBELL_CALLBACK = POINTER(PROCESSOR_PCC_DOORBELL_CALLBACK)
            PROCESSOR_PCC_COMMAND_GET_AVERAGE_FREQUENCY = 0x00
            PROCESSOR_PCC_COMMAND_SET_DESIRED_FREQUENCY = 0x01

            # NTSTATUS
            # (PROCESSOR_PCC_RING_DOORBELL)(
            # _In_ UCHAR Command,
            # _In_ PPROCESSOR_PCC_DOORBELL_CALLBACK Callback,
            # _In_ ULONG_PTR Context
            # );
            PROCESSOR_PCC_RING_DOORBELL = CALLBACK(
                NTSTATUS,
                UCHAR,
                PPROCESSOR_PCC_DOORBELL_CALLBACK,
                ULONG_PTR
            )

            PPROCESSOR_PCC_RING_DOORBELL = POINTER(PROCESSOR_PCC_RING_DOORBELL)

            _PROCESSOR_PCC_INTERFACE_STANDARD._fields_ = [
                # Generic interface header
                ('Size', USHORT),
                ('Version', USHORT),
                ('Context', PVOID),
                ('InterfaceReference', PINTERFACE_REFERENCE),
                ('InterfaceDereference', PINTERFACE_DEREFERENCE),
                # PCC interfaces
                ('PccRingDoorbell', PPROCESSOR_PCC_RING_DOORBELL),
                ('PccHeader', PPCC_HEADER),
                ('PccHeaderLength', ULONG),
            ]
            PROCESSOR_PCC_INTERFACE_STANDARD_VERSION = 1

            # Thermal client interface (devices implementing
            # GUID_THERMAL_COOLING_INTERFACE)
            # _Function_class_(DEVICE_ACTIVE_COOLING)
            # VOID
            # DEVICE_ACTIVE_COOLING (
            # _Inout_opt_ PVOID Context,
            # _In_ BOOLEAN Engaged
            # );
            DEVICE_ACTIVE_COOLING = CALLBACK(
                VOID,
                PVOID,
                BOOLEAN
            )

            PDEVICE_ACTIVE_COOLING = POINTER(DEVICE_ACTIVE_COOLING)

            # _Function_class_(DEVICE_PASSIVE_COOLING)
            # VOID
            # DEVICE_PASSIVE_COOLING (
            # _Inout_opt_ PVOID Context,
            # _In_ ULONG Percentage
            # );
            DEVICE_PASSIVE_COOLING = CALLBACK(
                VOID,
                PVOID,
                ULONG
            )

            PDEVICE_PASSIVE_COOLING = POINTER(DEVICE_PASSIVE_COOLING)

            _THERMAL_COOLING_INTERFACE._fields_ = [
                # generic interface header
                ('Size', USHORT),
                ('Version', USHORT),
                ('Context', PVOID),
                ('InterfaceReference', PINTERFACE_REFERENCE),
                ('InterfaceDereference', PINTERFACE_DEREFERENCE),
                # Thermal cooling interface
                ('Flags', ULONG),
                ('ActiveCooling', PDEVICE_ACTIVE_COOLING),
                ('PassiveCooling', PDEVICE_PASSIVE_COOLING),
            ]
            THERMAL_COOLING_INTERFACE_VERSION = 1

            # The following THERMAL_DEVICE_* definitions are deprecated and
            # should not be
            # used. Use THERMAL_COOLING_* instead.
            THERMAL_DEVICE_INTERFACE_VERSION = 1


            class _THERMAL_DEVICE_INTERFACE_FLAGS(ENUM):
                ThermalDeviceFlagActiveCooling = 1
                ThermalDeviceFlagPassiveCooling = 2

            THERMAL_DEVICE_INTERFACE_FLAGS = _THERMAL_DEVICE_INTERFACE_FLAGS
            PTHERMAL_DEVICE_INTERFACE_FLAGS = POINTER(_THERMAL_DEVICE_INTERFACE_FLAGS)
        # END IF   _WINDOWS_

        # Message indicator class driver functions
        IOCTL_SET_SYS_MESSAGE_INDICATOR = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x70,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )

        # ACPI Time device functions
        IOCTL_SET_WAKE_ALARM_VALUE = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x80,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_SET_WAKE_ALARM_POLICY = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x81,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_GET_WAKE_ALARM_VALUE = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x82,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )
        IOCTL_GET_WAKE_ALARM_POLICY = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x83,
            METHOD_BUFFERED,
            FILE_READ_ACCESS | FILE_WRITE_ACCESS,
        )

        _WAKE_ALARM_INFORMATION._fields_ = [
            # 0x00000001 - DC Timer
            ('TimerIdentifier', ULONG),
            # 0xffffffff disables a timer or indicates a timer countdown
            # completion.
            ('Timeout', ULONG),
        ]

        # ACPI Real Time Clock functions
        ACPI_TIME_ADJUST_DAYLIGHT = 0x01
        ACPI_TIME_IN_DAYLIGHT = 0x02
        ACPI_TIME_ZONE_UNKNOWN = 0x7FF
        IOCTL_ACPI_GET_REAL_TIME = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x84,
            METHOD_BUFFERED,
            FILE_READ_DATA,
        )
        IOCTL_ACPI_SET_REAL_TIME = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x85,
            METHOD_BUFFERED,
            FILE_WRITE_ACCESS,
        )
        IOCTL_GET_WAKE_ALARM_SYSTEM_POWERSTATE = CTL_CODE(
            FILE_DEVICE_BATTERY,
            0x86,
            METHOD_BUFFERED,
            FILE_READ_DATA,
        )

        _ACPI_REAL_TIME._fields_ = [
            # Year : 2010 - 9999
            ('Year', UINT16),
            # Month : 1 - 12
            ('Month', UINT8),
            # Day : 1 - 31
            ('Day', UINT8),
            # Hour : 0 - 23
            ('Hour', UINT8),
            # Minute : 0 - 59
            ('Minute', UINT8),
            # Second : 0 - 59
            ('Second', UINT8),
            # 0 - Time is not valid (request failed); 1 - Time is valid
            ('Valid', UINT8),
            # Milliseconds : 1 - 1000
            ('Milliseconds', UINT16),
            # TimeZone : - 1440 to 1440 or 2047
            ('TimeZone', INT16),
            # DayLight : 0 - 1
            ('DayLight', UINT8),
            # Reserved: Must be 0
            ('Reserved1', UINT8 * 3),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _POCLASS_
