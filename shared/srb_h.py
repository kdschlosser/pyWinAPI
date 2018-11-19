import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *


if NTDDI_VERSION >= NTDDI_WIN8:
    # Define alignment requirements for variable length components in extended
    # SRB. For Win64, need to ensure all variable length components are 8 bytes
    # align so the pointer fields within the variable length components are 8
    # bytes align. Also define pointer field alignment.
    #
    if defined(_WIN64) or defined(_M_ALPHA):
        SRB_ALIGN = ctypes.Structure
        POINTER_ALIGN = ctypes.Structure
    else:
        SRB_ALIGN = ctypes.Structure
        POINTER_ALIGN = ctypes.Structure
    # END IF

else:
    SRB_ALIGN = ctypes.Structure
    POINTER_ALIGN = ctypes.Structure

# END IF

SCSI_PHYSICAL_ADDRESS = PHYSICAL_ADDRESS
PSCSI_PHYSICAL_ADDRESS = POINTER(PHYSICAL_ADDRESS)


class _ACCESS_RANGE(ctypes.Structure):
    pass


ACCESS_RANGE = _ACCESS_RANGE
PACCESS_RANGE = POINTER(_ACCESS_RANGE)


class _PORT_CONFIGURATION_INFORMATION(ctypes.Structure):
    pass


PORT_CONFIGURATION_INFORMATION = _PORT_CONFIGURATION_INFORMATION
PPORT_CONFIGURATION_INFORMATION = POINTER(_PORT_CONFIGURATION_INFORMATION)


class _SCSI_SUPPORTED_CONTROL_TYPE_LIST(ctypes.Structure):
    pass


SCSI_SUPPORTED_CONTROL_TYPE_LIST = _SCSI_SUPPORTED_CONTROL_TYPE_LIST
PSCSI_SUPPORTED_CONTROL_TYPE_LIST = POINTER(_SCSI_SUPPORTED_CONTROL_TYPE_LIST)


class _SCSI_REQUEST_BLOCK(ctypes.Structure):
    pass


SCSI_REQUEST_BLOCK = _SCSI_REQUEST_BLOCK
PSCSI_REQUEST_BLOCK = POINTER(_SCSI_REQUEST_BLOCK)


class _SCSI_WMI_REQUEST_BLOCK(ctypes.Structure):
    pass


SCSI_WMI_REQUEST_BLOCK = _SCSI_WMI_REQUEST_BLOCK
PSCSI_WMI_REQUEST_BLOCK = POINTER(_SCSI_WMI_REQUEST_BLOCK)


class _SCSI_POWER_REQUEST_BLOCK(ctypes.Structure):
    pass


SCSI_POWER_REQUEST_BLOCK = _SCSI_POWER_REQUEST_BLOCK
PSCSI_POWER_REQUEST_BLOCK = POINTER(_SCSI_POWER_REQUEST_BLOCK)


class _STOR_DEVICE_CAPABILITIES(ctypes.Structure):
    pass


STOR_DEVICE_CAPABILITIES = _STOR_DEVICE_CAPABILITIES
PSTOR_DEVICE_CAPABILITIES = POINTER(_STOR_DEVICE_CAPABILITIES)


class _STOR_DEVICE_CAPABILITIES_EX(ctypes.Structure):
    pass


STOR_DEVICE_CAPABILITIES_EX = _STOR_DEVICE_CAPABILITIES_EX
PSTOR_DEVICE_CAPABILITIES_EX = POINTER(_STOR_DEVICE_CAPABILITIES_EX)


class _SCSI_PNP_REQUEST_BLOCK(ctypes.Structure):
    pass


SCSI_PNP_REQUEST_BLOCK = _SCSI_PNP_REQUEST_BLOCK
PSCSI_PNP_REQUEST_BLOCK = POINTER(_SCSI_PNP_REQUEST_BLOCK)


class _SRBEX_DATA(SRB_ALIGN):
    pass


SRBEX_DATA = _SRBEX_DATA
PSRBEX_DATA = POINTER(_SRBEX_DATA)


class _SRBEX_DATA_BIDIRECTIONAL(SRB_ALIGN):
    pass


SRBEX_DATA_BIDIRECTIONAL = _SRBEX_DATA_BIDIRECTIONAL
PSRBEX_DATA_BIDIRECTIONAL = POINTER(_SRBEX_DATA_BIDIRECTIONAL)


class _SRBEX_DATA_SCSI_CDB16(SRB_ALIGN):
    pass


SRBEX_DATA_SCSI_CDB16 = _SRBEX_DATA_SCSI_CDB16
PSRBEX_DATA_SCSI_CDB16 = POINTER(_SRBEX_DATA_SCSI_CDB16)


class _SRBEX_DATA_SCSI_CDB32(SRB_ALIGN):
    pass


SRBEX_DATA_SCSI_CDB32 = _SRBEX_DATA_SCSI_CDB32
PSRBEX_DATA_SCSI_CDB32 = POINTER(_SRBEX_DATA_SCSI_CDB32)


class _SRBEX_DATA_SCSI_CDB_VAR(SRB_ALIGN):
    pass


SRBEX_DATA_SCSI_CDB_VAR = _SRBEX_DATA_SCSI_CDB_VAR
PSRBEX_DATA_SCSI_CDB_VAR = POINTER(_SRBEX_DATA_SCSI_CDB_VAR)


class _SRBEX_DATA_WMI(SRB_ALIGN):
    pass


SRBEX_DATA_WMI = _SRBEX_DATA_WMI
PSRBEX_DATA_WMI = POINTER(_SRBEX_DATA_WMI)


class _SRBEX_DATA_POWER(SRB_ALIGN):
    pass


SRBEX_DATA_POWER = _SRBEX_DATA_POWER
PSRBEX_DATA_POWER = POINTER(_SRBEX_DATA_POWER)


class _SRBEX_DATA_PNP(SRB_ALIGN):
    pass


SRBEX_DATA_PNP = _SRBEX_DATA_PNP
PSRBEX_DATA_PNP = POINTER(_SRBEX_DATA_PNP)


class _SRBEX_DATA_IO_INFO(SRB_ALIGN):
    pass


SRBEX_DATA_IO_INFO = _SRBEX_DATA_IO_INFO
PSRBEX_DATA_IO_INFO = POINTER(_SRBEX_DATA_IO_INFO)


class _STORAGE_REQUEST_BLOCK_HEADER(SRB_ALIGN):
    pass


STORAGE_REQUEST_BLOCK_HEADER = _STORAGE_REQUEST_BLOCK_HEADER
PSTORAGE_REQUEST_BLOCK_HEADER = POINTER(_STORAGE_REQUEST_BLOCK_HEADER)


class _STORAGE_REQUEST_BLOCK(SRB_ALIGN):
    pass


STORAGE_REQUEST_BLOCK = _STORAGE_REQUEST_BLOCK
PSTORAGE_REQUEST_BLOCK = POINTER(_STORAGE_REQUEST_BLOCK)


class _HW_INITIALIZATION_DATA(ctypes.Structure):
    pass


HW_INITIALIZATION_DATA = _HW_INITIALIZATION_DATA
PHW_INITIALIZATION_DATA = POINTER(_HW_INITIALIZATION_DATA)


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: srb.h Abstract: This file defines the interface between SCSI mini -
# port drivers and the SCSI port driver. It is also used by SCSI class drivers
# to talk to the SCSI port driver. Revision History: - -

_NTSRB_ = None
if not defined(_NTSRB_):
    _NTSRB_ = 1

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.km.wdm_h import *  # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if DBG:
            def DebugPrint(x):
                return ScsiDebugPrint(x)
        else:
            def DebugPrint(x):
                pass
        # END IF

        # begin_storport begin_storportp
        # Define SCSI maximum configuration parameters.
        # NOTE - the current SCSI_MAXIMUM_TARGETS_PER_BUS is applicable only
        # on scsiport miniports. For storport miniports, the max target
        # supported is 255.
        SCSI_MAXIMUM_BUSES_PER_ADAPTER = 255
        SCSI_MAXIMUM_TARGETS_PER_BUS = 128
        SCSI_MAXIMUM_LUNS_PER_TARGET = 255
        SCSI_MINIMUM_PHYSICAL_BREAKS = 16
        SCSI_MAXIMUM_PHYSICAL_BREAKS = 255


        def SCSI_COMBINE_BUS_TARGET(Bus, Target):
            return (
                ((Target & ~(0x20 - 1)) << 8) |
                (Bus << 5) |
                (Target & (0x20 - 1))
            )


        def SCSI_DECODE_BUS_TARGET(Value, Bus, Target):
            Bus = Value >> 5
            Target = ((Value >> 8) & ~(0x20 - 1)) | (Value & (0x20 - 1))


        # This constant is for backward compatibility.
        # This use to be the maximum supported.
        SCSI_MAXIMUM_BUSES = 8
        SCSI_MAXIMUM_TARGETS = 8
        SCSI_MAXIMUM_LOGICAL_UNITS = 8

        # end_storport end_storportp
        _ACCESS_RANGE._fields_ = [
            ('RangeStart', SCSI_PHYSICAL_ADDRESS),
            ('RangeLength', ULONG),
            ('RangeInMemory', BOOLEAN),
        ]

        # Configuration information structure. Contains the information
        # necessary
        # to initialize the adapter. NOTE: This structure's must be a multiple
        # of
        # quadwords.
        _PORT_CONFIGURATION_INFORMATION._fields_ = [
            # Length of port configuation information strucuture.
            ('Length', ULONG),
            # IO bus number (0 for machines that have only 1 IO bus
            ('SystemIoBusNumber', ULONG),
            # EISA, MCA or ISA
            ('AdapterInterfaceType', INTERFACE_TYPE),
            # Interrupt request level for device
            ('BusInterruptLevel', ULONG),
            # well as level, such as internal buses.
            ('BusInterruptVector', ULONG),
            # Interrupt mode (level - sensitive or edge - triggered)
            ('InterruptMode', KINTERRUPT_MODE),
            # Maximum number of bytes that can be transferred in a single SRB
            ('MaximumTransferLength', ULONG),
            # Number of contiguous blocks of physical memory
            ('NumberOfPhysicalBreaks', ULONG),
            # DMA channel for devices using system DMA
            ('DmaChannel', ULONG),
            ('DmaPort', ULONG),
            ('DmaWidth', DMA_WIDTH),
            ('DmaSpeed', DMA_SPEED),
            # Alignment masked required by the adapter for data transfers.
            ('AlignmentMask', ULONG),
            # Number of access range elements which have been allocated.
            ('NumberOfAccessRanges', ULONG),
            # Pointer to array of access range elements.
            ('AccessRanges', POINTER(ACCESS_RANGE)),
            # Reserved field.
            ('Reserved', PVOID),
            # Number of SCSI buses attached to the adapter.
            ('NumberOfBuses', UCHAR),
            # SCSI bus ID for adapter
            ('InitiatorBusId', UCHAR * 8),
            # Indicates that the adapter does scatter/gather
            ('ScatterGather', BOOLEAN),
            # Indicates that the adapter is a bus master
            ('Master', BOOLEAN),
            # Host caches data or state.
            ('CachesData', BOOLEAN),
            # Host adapter scans down for bios devices.
            ('AdapterScansDown', BOOLEAN),
            # Primary at disk address (0x1F0) claimed.
            ('AtdiskPrimaryClaimed', BOOLEAN),
            # Secondary at disk address (0x170) claimed.
            ('AtdiskSecondaryClaimed', BOOLEAN),
            # The master uses 32 - bit DMA addresses.
            ('Dma32BitAddresses', BOOLEAN),
            # Use Demand Mode DMA rather than Single Request.
            ('DemandMode', BOOLEAN),
            # Data buffers must be mapped into virtual address space.
            ('MapBuffers', BOOLEAN),
            # The driver will need to tranlate virtual to physical addresses.
            ('NeedPhysicalAddresses', BOOLEAN),
            # Supports tagged queuing
            ('TaggedQueuing', BOOLEAN),
            # Supports auto request sense.
            ('AutoRequestSense', BOOLEAN),
            # Supports multiple requests per logical unit.
            ('MultipleRequestPerLu', BOOLEAN),
            # Support receive event function.
            ('ReceiveEvent', BOOLEAN),
            # Indicates the real - mode driver has initialized the card.
            ('RealModeInitialized', BOOLEAN),
            # Indicate that the miniport will not touch the data buffers
            # directly.
            ('BufferAccessScsiPortControlled', BOOLEAN),
            # Indicator for wide scsi.
            ('MaximumNumberOfTargets', UCHAR),
            # Ensure quadword alignment.
            ('ReservedUchars', UCHAR * 2),
            # Adapter slot number
            ('SlotNumber', ULONG),
            # Interrupt information for a second IRQ.
            ('BusInterruptLevel2', ULONG),
            ('BusInterruptVector2', ULONG),
            ('InterruptMode2', KINTERRUPT_MODE),
            # DMA information for a second channel.
            ('DmaChannel2', ULONG),
            ('DmaPort2', ULONG),
            ('DmaWidth2', DMA_WIDTH),
            ('DmaSpeed2', DMA_SPEED),
            # for large transfers ( > 64K);
            ('DeviceExtensionSize', ULONG),
            ('SpecificLuExtensionSize', ULONG),
            ('SrbExtensionSize', ULONG),
            # New
            ('Dma64BitAddresses', UCHAR),
            # New
            ('ResetTargetSupported', BOOLEAN),
            # New
            ('MaximumNumberOfLogicalUnits', UCHAR),
            # Supports WMI?
            ('WmiDataProvider', BOOLEAN),
        ]
        # Version control for ConfigInfo structure.
        CONFIG_INFO_VERSION_2 = ctypes.sizeof(PORT_CONFIGURATION_INFORMATION)
        # Flags for controlling 64 - bit DMA use
        # (PORT_CONFIGURATION_INFORMATION field
        # Dma64BitAddresses)
        # Set by scsiport on entering HwFindAdapter if the system can support
        # 64 - bit
        # physical addresses. The miniport can use this information before
        # calling
        # ScsiPortGetUncachedExtension to modify the DeviceExtensionSize,
        # SpecificLuExtensionSize & SrbExtensionSize fields to account for the
        # extra
        # size of the scatter gather list.
        SCSI_DMA64_SYSTEM_SUPPORTED = 0x80
        # Set by the miniport before calling ScsiPortGetUncachedExtension to
        # indicate
        # that scsiport should provide it with 64 - bit physical addresses. If
        # the
        # system does not support 64 - bit PA's then this bit will be ignored.
        SCSI_DMA64_MINIPORT_SUPPORTED = 0x01
        if NTDDI_VERSION > NTDDI_WS03SP1:
            # Set by the miniport before calling ScsiPortGetUncachedExtension
            # to indicate
            # that scsiport should provide it with 64 - bit physical addresses.
            # In addition to I/O requests being handled with > 4GB physical
            # addresses,
            # the uncached extension, SenseInof and Srb Extension may all lie
            # above 4GB.
            # If the system does not support 64 - bit PA's then this bit will
            # be ignored.
            SCSI_DMA64_MINIPORT_FULL64BIT_SUPPORTED = 0x02
        # END IF
        # Command type (and parameter) definition(s) for AdapterControl
        # requests.
        class _SCSI_ADAPTER_CONTROL_TYPE(ENUM):
            ScsiQuerySupportedControlTypes = 0
            ScsiStopAdapter = 1
            ScsiRestartAdapter = 2
            ScsiSetBootConfig = 3
            ScsiSetRunningConfig = 4
            ScsiAdapterControlMax = 5
            MakeAdapterControlTypeSizeOfUlong = 0xFFFFFFFF

        SCSI_ADAPTER_CONTROL_TYPE = _SCSI_ADAPTER_CONTROL_TYPE
        PSCSI_ADAPTER_CONTROL_TYPE = POINTER(_SCSI_ADAPTER_CONTROL_TYPE)

        # Adapter control status values
        class _SCSI_ADAPTER_CONTROL_STATUS(ENUM):
            ScsiAdapterControlSuccess = 0
            ScsiAdapterControlUnsuccessful = 1

        SCSI_ADAPTER_CONTROL_STATUS = _SCSI_ADAPTER_CONTROL_STATUS
        PSCSI_ADAPTER_CONTROL_STATUS = POINTER(_SCSI_ADAPTER_CONTROL_STATUS)

        # Parameters for Adapter Control Functions:
        # ScsiQuerySupportedControlTypes:
        _SCSI_SUPPORTED_CONTROL_TYPE_LIST._fields_ = [
            # Specifies the number of entries in the adapter control type list.
            ('MaxControlType', ULONG),
            # value specified.
            ('SupportedTypeList', BOOLEAN * 0),
        ]

        # begin_storport begin_storportp
        # Uninitialized flag value.
        SP_UNINITIALIZED_VALUE = ~0
        SP_UNTAGGED = ~0

        # Set asynchronous events.
        SRBEV_BUS_RESET = 0x0001
        SRBEV_SCSI_ASYNC_NOTIFICATION = 0x0002

        # begin_ntminitape
        MAXIMUM_CDB_SIZE = 12

        # SCSI I/O Request Block
        _SCSI_REQUEST_BLOCK._fields_ = [
            # offset 0
            ('Length', USHORT),
            # offset 2
            ('Function', UCHAR),
            # offset 3
            ('SrbStatus', UCHAR),
            # offset 4
            ('ScsiStatus', UCHAR),
            # offset 5
            ('PathId', UCHAR),
            # offset 6
            ('TargetId', UCHAR),
            # offset 7
            ('Lun', UCHAR),
            # offset 8
            ('QueueTag', UCHAR),
            # offset 9
            ('QueueAction', UCHAR),
            # offset a
            ('CdbLength', UCHAR),
            # offset b
            ('SenseInfoBufferLength', UCHAR),
            # offset c
            ('SrbFlags', ULONG),
            # offset 10
            ('DataTransferLength', ULONG),
            # offset 14
            ('TimeOutValue', ULONG),
            # offset 18
            ('DataBuffer', PVOID),
            # offset 1c
            ('SenseInfoBuffer', PVOID),
            # offset 20
            ('NextSrb', POINTER(_SCSI_REQUEST_BLOCK)),
            # offset 24
            ('OriginalRequest', PVOID),
            # offset 28
            ('SrbExtension', PVOID),
        ]
        SCSI_REQUEST_BLOCK_SIZE = ctypes.sizeof(SCSI_REQUEST_BLOCK)
        # SCSI I/O Request Block for WMI Requests

        _TEMP__SCSI_WMI_REQUEST_BLOCK = [
            ('Length', USHORT),
            # SRB_FUNCTION_WMI
            ('Function', UCHAR),
            ('SrbStatus', UCHAR),
            ('WMISubFunction', UCHAR),
            # If SRB_WMI_FLAGS_ADAPTER_REQUEST is set in
            ('PathId', UCHAR),
            # WMIFlags then PathId, TargetId and Lun are
            ('TargetId', UCHAR),
            # reserved fields.
            ('Lun', UCHAR),
            ('Reserved1', UCHAR),
            ('WMIFlags', UCHAR),
            ('Reserved2', UCHAR * 2),
            ('SrbFlags', ULONG),
            ('DataTransferLength', ULONG),
            ('TimeOutValue', ULONG),
            ('DataBuffer', PVOID),
            ('DataPath', PVOID),
            ('Reserved3', PVOID),
            ('OriginalRequest', PVOID),
            ('SrbExtension', PVOID),
            ('Reserved4', ULONG),
        ]

        if NTDDI_VERSION >= NTDDI_WS03SP1:
            if defined(_WIN64):
                _TEMP__SCSI_WMI_REQUEST_BLOCK += [
                    # Force PVOID alignment of Cdb
                   ('Reserved6', ULONG),
                ]

            # END IF
        # END IF

        _TEMP__SCSI_WMI_REQUEST_BLOCK += [
            ('Reserved5', UCHAR * 16),
        ]

        _SCSI_WMI_REQUEST_BLOCK._fields_ = _TEMP__SCSI_WMI_REQUEST_BLOCK


        class _STOR_DEVICE_POWER_STATE(ENUM):
            StorPowerDeviceUnspecified = 0
            StorPowerDeviceD0 = 1
            StorPowerDeviceD1 = 2
            StorPowerDeviceD2 = 3
            StorPowerDeviceD3 = 4
            StorPowerDeviceMaximum = 5

        STOR_DEVICE_POWER_STATE = _STOR_DEVICE_POWER_STATE
        PSTOR_DEVICE_POWER_STATE = POINTER(_STOR_DEVICE_POWER_STATE)


        class STOR_POWER_ACTION(ENUM):
            StorPowerActionNone = 0
            StorPowerActionReserved = 1
            StorPowerActionSleep = 2
            StorPowerActionHibernate = 3
            StorPowerActionShutdown = 4
            StorPowerActionShutdownReset = 5
            StorPowerActionShutdownOff = 6
            StorPowerActionWarmEject = 7

        PSTOR_POWER_ACTION = POINTER(STOR_POWER_ACTION)
        StorPowerActionNone = STOR_POWER_ACTION.StorPowerActionNone
        StorPowerActionReserved = STOR_POWER_ACTION.StorPowerActionReserved
        StorPowerActionSleep = STOR_POWER_ACTION.StorPowerActionSleep
        StorPowerActionHibernate = STOR_POWER_ACTION.StorPowerActionHibernate
        StorPowerActionShutdown = STOR_POWER_ACTION.StorPowerActionShutdown
        StorPowerActionShutdownReset = STOR_POWER_ACTION.StorPowerActionShutdownReset
        StorPowerActionShutdownOff = STOR_POWER_ACTION.StorPowerActionShutdownOff
        StorPowerActionWarmEject = STOR_POWER_ACTION.StorPowerActionWarmEject

        _TEMP__SCSI_POWER_REQUEST_BLOCK = [
            # offset 0
            ('Length', USHORT),
            # offset 2
            ('Function', UCHAR),
            # offset 3
            ('SrbStatus', UCHAR),
            # offset 4
            ('SrbPowerFlags', UCHAR),
            # offset 5
            ('PathId', UCHAR),
            # offset 6
            ('TargetId', UCHAR),
            # offset 7
            ('Lun', UCHAR),
            # offset 8
            ('DevicePowerState', STOR_DEVICE_POWER_STATE),
            # offset c
            ('SrbFlags', ULONG),
            # offset 10
            ('DataTransferLength', ULONG),
            # offset 14
            ('TimeOutValue', ULONG),
            # offset 18
            ('DataBuffer', PVOID),
            # offset 1c
            ('SenseInfoBuffer', PVOID),
            # offset 20
            ('NextSrb', POINTER(_SCSI_REQUEST_BLOCK)),
            # offset 24
            ('OriginalRequest', PVOID),
            # offset 28
            ('SrbExtension', PVOID),
            # offset 2c
            ('PowerAction', STOR_POWER_ACTION),
        ]

        if defined(_WIN64):
            _TEMP__SCSI_POWER_REQUEST_BLOCK += [
                # Force PVOID alignment of Cdb
                ('Reserved', ULONG),
            ]


        # END IF
        _TEMP__SCSI_POWER_REQUEST_BLOCK += [
            # offset 30
            ('Reserved5', UCHAR * 16),
        ]

        _SCSI_POWER_REQUEST_BLOCK._fields_ = _TEMP__SCSI_POWER_REQUEST_BLOCK

        # PNP minor function codes.
        class STOR_PNP_ACTION(ENUM):
            StorStartDevice = 0x0
            StorRemoveDevice = 0x2
            StorStopDevice = 0x4
            StorQueryCapabilities = 0x9
            StorQueryResourceRequirements = 0xB
            StorFilterResourceRequirements = 0xD
            StorSurpriseRemoval = 0x17

        PSTOR_PNP_ACTION = POINTER(STOR_PNP_ACTION)
        StorStartDevice = STOR_PNP_ACTION.StorStartDevice
        StorRemoveDevice = STOR_PNP_ACTION.StorRemoveDevice
        StorStopDevice = STOR_PNP_ACTION.StorStopDevice
        StorQueryCapabilities = STOR_PNP_ACTION.StorQueryCapabilities
        StorQueryResourceRequirements = STOR_PNP_ACTION.StorQueryResourceRequirements
        StorFilterResourceRequirements = STOR_PNP_ACTION.StorFilterResourceRequirements
        StorSurpriseRemoval = STOR_PNP_ACTION.StorSurpriseRemoval

        _STOR_DEVICE_CAPABILITIES._fields_ = [
            ('Version', USHORT),
            ('DeviceD1', ULONG, 1),
            ('DeviceD2', ULONG, 1),
            ('LockSupported', ULONG, 1),
            ('EjectSupported', ULONG, 1),
            ('Removable', ULONG, 1),
            ('DockDevice', ULONG, 1),
            ('UniqueID', ULONG, 1),
            ('SilentInstall', ULONG, 1),
            ('SurpriseRemovalOK', ULONG, 1),
            ('NoDisplayInUI', ULONG, 1),
        ]
        STOR_DEVICE_CAPABILITIES_EX_VERSION_1 = 0x1


        _STOR_DEVICE_CAPABILITIES_EX._fields_ = [
            ('Version', USHORT),
            ('Size', USHORT),
            ('DeviceD1', ULONG, 1),
            ('DeviceD2', ULONG, 1),
            ('LockSupported', ULONG, 1),
            ('EjectSupported', ULONG, 1),
            ('Removable', ULONG, 1),
            ('DockDevice', ULONG, 1),
            ('UniqueID', ULONG, 1),
            ('SilentInstall', ULONG, 1),
            ('RawDeviceOK', ULONG, 1),
            ('SurpriseRemovalOK', ULONG, 1),
            ('NoDisplayInUI', ULONG, 1),
            ('DefaultWriteCacheEnabled', ULONG, 1),
            ('Reserved0', ULONG, 20),
            ('Address', ULONG),
            ('UINumber', ULONG),
            ('Reserved1', ULONG * 2),
        ]

        _TEMP__SCSI_PNP_REQUEST_BLOCK = [
            # offset 0
            ('Length', USHORT),
            # offset 2
            ('Function', UCHAR),
            # offset 3
            ('SrbStatus', UCHAR),
            # offset 4
            ('PnPSubFunction', UCHAR),
            # offset 5
            ('PathId', UCHAR),
            # offset 6
            ('TargetId', UCHAR),
            # offset 7
            ('Lun', UCHAR),
            # offset 8
            ('PnPAction', STOR_PNP_ACTION),
            # offset c
            ('SrbFlags', ULONG),
            # offset 10
            ('DataTransferLength', ULONG),
            # offset 14
            ('TimeOutValue', ULONG),
            # offset 18
            ('DataBuffer', PVOID),
            # offset 1c
            ('SenseInfoBuffer', PVOID),
            # offset 20
            ('NextSrb', POINTER(_SCSI_REQUEST_BLOCK)),
            # offset 24
            ('OriginalRequest', PVOID),
            # offset 28
            ('SrbExtension', PVOID),
            # offset 2c
            ('SrbPnPFlags', ULONG),
        ]

        if defined(_WIN64):
            _TEMP__SCSI_PNP_REQUEST_BLOCK += [
                # Force PVOID alignment of Cdb
                ('Reserved', ULONG),
            ]

        # END IF
        _TEMP__SCSI_PNP_REQUEST_BLOCK += [
            # offset 30
            ('Reserved4', UCHAR * 16),
        ]

        _SCSI_PNP_REQUEST_BLOCK._fields_ = _TEMP__SCSI_PNP_REQUEST_BLOCK

        # SRB Functions
        SRB_FUNCTION_EXECUTE_SCSI = 0x00
        SRB_FUNCTION_CLAIM_DEVICE = 0x01
        SRB_FUNCTION_IO_CONTROL = 0x02
        SRB_FUNCTION_RECEIVE_EVENT = 0x03
        SRB_FUNCTION_RELEASE_QUEUE = 0x04
        SRB_FUNCTION_ATTACH_DEVICE = 0x05
        SRB_FUNCTION_RELEASE_DEVICE = 0x06
        SRB_FUNCTION_SHUTDOWN = 0x07
        SRB_FUNCTION_FLUSH = 0x08
        SRB_FUNCTION_PROTOCOL_COMMAND = 0x09
        SRB_FUNCTION_ABORT_COMMAND = 0x10
        SRB_FUNCTION_RELEASE_RECOVERY = 0x11
        SRB_FUNCTION_RESET_BUS = 0x12
        SRB_FUNCTION_RESET_DEVICE = 0x13
        SRB_FUNCTION_TERMINATE_IO = 0x14
        SRB_FUNCTION_FLUSH_QUEUE = 0x15
        SRB_FUNCTION_REMOVE_DEVICE = 0x16
        SRB_FUNCTION_WMI = 0x17
        SRB_FUNCTION_LOCK_QUEUE = 0x18
        SRB_FUNCTION_UNLOCK_QUEUE = 0x19
        SRB_FUNCTION_QUIESCE_DEVICE = 0x1A
        SRB_FUNCTION_RESET_LOGICAL_UNIT = 0x20
        SRB_FUNCTION_SET_LINK_TIMEOUT = 0x21
        SRB_FUNCTION_LINK_TIMEOUT_OCCURRED = 0x22
        SRB_FUNCTION_LINK_TIMEOUT_COMPLETE = 0x23
        SRB_FUNCTION_POWER = 0x24
        SRB_FUNCTION_PNP = 0x25
        SRB_FUNCTION_DUMP_POINTERS = 0x26
        SRB_FUNCTION_FREE_DUMP_POINTERS = 0x27

        # Define extended SRB function that will be used to identify a new
        # type of SRB that is not a SCSI_REQUEST_BLOCK. A
        # SRB_FUNCTION_STORAGE_REQUEST_BLOCK will use a SRB that is of type
        # STORAGE_REQUEST_BLOCK.
        SRB_FUNCTION_STORAGE_REQUEST_BLOCK = 0x28

        # end_storport
        SRB_FUNCTION_GET_DUMP_INFO = 0x2A
        SRB_FUNCTION_FREE_DUMP_INFO = 0x2B

        # begin_storport
        # SRB Status
        SRB_STATUS_PENDING = 0x00
        SRB_STATUS_SUCCESS = 0x01
        SRB_STATUS_ABORTED = 0x02
        SRB_STATUS_ABORT_FAILED = 0x03
        SRB_STATUS_ERROR = 0x04
        SRB_STATUS_BUSY = 0x05
        SRB_STATUS_INVALID_REQUEST = 0x06
        SRB_STATUS_INVALID_PATH_ID = 0x07
        SRB_STATUS_NO_DEVICE = 0x08
        SRB_STATUS_TIMEOUT = 0x09
        SRB_STATUS_SELECTION_TIMEOUT = 0x0A
        SRB_STATUS_COMMAND_TIMEOUT = 0x0B
        SRB_STATUS_MESSAGE_REJECTED = 0x0D
        SRB_STATUS_BUS_RESET = 0x0E
        SRB_STATUS_PARITY_ERROR = 0x0F
        SRB_STATUS_REQUEST_SENSE_FAILED = 0x10
        SRB_STATUS_NO_HBA = 0x11
        SRB_STATUS_DATA_OVERRUN = 0x12
        SRB_STATUS_UNEXPECTED_BUS_FREE = 0x13
        SRB_STATUS_PHASE_SEQUENCE_FAILURE = 0x14
        SRB_STATUS_BAD_SRB_BLOCK_LENGTH = 0x15
        SRB_STATUS_REQUEST_FLUSHED = 0x16
        SRB_STATUS_INVALID_LUN = 0x20
        SRB_STATUS_INVALID_TARGET_ID = 0x21
        SRB_STATUS_BAD_FUNCTION = 0x22
        SRB_STATUS_ERROR_RECOVERY = 0x23
        SRB_STATUS_NOT_POWERED = 0x24
        SRB_STATUS_LINK_DOWN = 0x25

        # This value is used by the port driver to indicate that a non - scsi
        # - related
        # error occured. Miniports must never return this status.
        SRB_STATUS_INTERNAL_ERROR = 0x30

        # Srb status values 0x38 through 0x3f are reserved for internal port
        # driver
        # use.
        # SRB Status Masks
        SRB_STATUS_QUEUE_FROZEN = 0x40
        SRB_STATUS_AUTOSENSE_VALID = 0x80


        def SRB_STATUS(Status):
            return (
                Status &
                ~(SRB_STATUS_AUTOSENSE_VALID | SRB_STATUS_QUEUE_FROZEN)
            )

        # SRB Flag Bits
        SRB_FLAGS_QUEUE_ACTION_ENABLE = 0x00000002
        SRB_FLAGS_DISABLE_DISCONNECT = 0x00000004
        SRB_FLAGS_DISABLE_SYNCH_TRANSFER = 0x00000008
        SRB_FLAGS_BYPASS_FROZEN_QUEUE = 0x00000010
        SRB_FLAGS_DISABLE_AUTOSENSE = 0x00000020
        SRB_FLAGS_DATA_IN = 0x00000040
        SRB_FLAGS_DATA_OUT = 0x00000080
        SRB_FLAGS_NO_DATA_TRANSFER = 0x00000000
        SRB_FLAGS_UNSPECIFIED_DIRECTION = (
            SRB_FLAGS_DATA_IN |
            SRB_FLAGS_DATA_OUT
        )
        SRB_FLAGS_NO_QUEUE_FREEZE = 0x00000100
        SRB_FLAGS_ADAPTER_CACHE_ENABLE = 0x00000200
        SRB_FLAGS_FREE_SENSE_BUFFER = 0x00000400

        # This flag indicates the request is part of the workflow for
        # processing a D3.
        SRB_FLAGS_D3_PROCESSING = 0x00000800

        # This flag indicates that LBA range falls into sequential write
        # required zone
        SRB_FLAGS_SEQUENTIAL_REQUIRED = 0x00001000
        SRB_FLAGS_IS_ACTIVE = 0x00010000
        SRB_FLAGS_ALLOCATED_FROM_ZONE = 0x00020000
        SRB_FLAGS_SGLIST_FROM_POOL = 0x00040000
        SRB_FLAGS_BYPASS_LOCKED_QUEUE = 0x00080000
        SRB_FLAGS_NO_KEEP_AWAKE = 0x00100000
        SRB_FLAGS_PORT_DRIVER_ALLOCSENSE = 0x00200000
        SRB_FLAGS_PORT_DRIVER_SENSEHASPORT = 0x00400000
        SRB_FLAGS_DONT_START_NEXT_PACKET = 0x00800000
        SRB_FLAGS_PORT_DRIVER_RESERVED = 0x0F000000
        SRB_FLAGS_CLASS_DRIVER_RESERVED = 0xF0000000

        if DBG == 1:
            # A signature used to validate the scsi port number
            # at the end of a sense buffer.
            SCSI_PORT_SIGNATURE = 0x54524F50
        # END IF
        # Queue Action
        SRB_SIMPLE_TAG_REQUEST = 0x20
        SRB_HEAD_OF_QUEUE_TAG_REQUEST = 0x21
        SRB_ORDERED_QUEUE_TAG_REQUEST = 0x22
        SRB_WMI_FLAGS_ADAPTER_REQUEST = 0x01
        SRB_POWER_FLAGS_ADAPTER_REQUEST = 0x01
        SRB_PNP_FLAGS_ADAPTER_REQUEST = 0x01
        SRB_IOCTL_FLAGS_ADAPTER_REQUEST = 0x01
        SRB_PROTOCOL_FLAGS_ADAPTER_REQUEST = 0x01

        if NTDDI_VERSION >= NTDDI_WIN8:
            # Define alignment requirements for variable length components in
            # extended
            # SRB. For Win64, need to ensure all variable length components
            # are 8 bytes
            # align so the pointer fields within the variable length
            # components are 8
            # bytes align. Also define pointer field alignment.

            class _SRBEXDATATYPE(ENUM):
                SrbExDataTypeUnknown = 0
                SrbExDataTypeBidirectional = 1
                SrbExDataTypeScsiCdb16 = 0x40
                SrbExDataTypeScsiCdb32 = 65
                SrbExDataTypeScsiCdbVar = 66
                SrbExDataTypeWmi = 0x60
                SrbExDataTypePower = 97
                SrbExDataTypePnP = 98
                SrbExDataTypeIoInfo = 0x80
                SrbExDataTypeMSReservedStart = 0xF0000000
                SrbExDataTypeReserved = 0xFFFFFFFF

            SRBEXDATATYPE = _SRBEXDATATYPE
            PSRBEXDATATYPE = POINTER(_SRBEXDATATYPE)

            # Generic structure definition for accessing any SRB extended
            # data. All SRB
            # extended data must begin with a Type and Length field.
            _SRBEX_DATA._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('Data', UCHAR * ANYSIZE_ARRAY),
            ]

            # SRB extended data for bi - directional commands. For these SRBs,
            # it will have both a
            # SRB extended data (e.g. SRBEX_DATA_SCSI_CDB*) and a
            # SRBEX_DATA_BIDIRECTIONAL.
            SRBEX_DATA_BIDIRECTIONAL_LENGTH = (
                (2 * ctypes.sizeof(ULONG)) + ctypes.sizeof(PVOID)
            )

            _SRBEX_DATA_BIDIRECTIONAL._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('DataInTransferLength', ULONG),
                # Reserved for future to support 64 - bit DataTransferInLength
                ('Reserved1', ULONG),
                ('POINTER_ALIGN DataInBuffer', PVOID),
            ]
            # SRB_FUNCTION_EXECUTE_SCSI for up to 16 byte CDBs
            SRBEX_DATA_SCSI_CDB16_LENGTH = (
                (20 * ctypes.sizeof(UCHAR)) +
                ctypes.sizeof(ULONG) +
                ctypes.sizeof(PVOID)
            )

            _SRBEX_DATA_SCSI_CDB16._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('ScsiStatus', UCHAR),
                ('SenseInfoBufferLength', UCHAR),
                ('CdbLength', UCHAR),
                ('Reserved', UCHAR),
                ('Reserved1', ULONG),
                ('POINTER_ALIGN SenseInfoBuffer', PVOID),
                ('POINTER_ALIGN Cdb', UCHAR * 16),
            ]
            # SRB_FUNCTION_EXECUTE_SCSI for up to 32 byte CDBs
            SRBEX_DATA_SCSI_CDB32_LENGTH = (
                (36 * ctypes.sizeof(UCHAR)) +
                ctypes.sizeof(ULONG) +
                ctypes.sizeof(PVOID)
            )

            _SRBEX_DATA_SCSI_CDB32._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('ScsiStatus', UCHAR),
                ('SenseInfoBufferLength', UCHAR),
                ('CdbLength', UCHAR),
                ('Reserved', UCHAR),
                ('Reserved1', ULONG),
                ('POINTER_ALIGN SenseInfoBuffer', PVOID),
                ('POINTER_ALIGN Cdb', UCHAR * 32),
            ]
            # SRB_FUNCTION_EXECUTE_SCSI for variable length CDBs
            SRBEX_DATA_SCSI_CDB_VAR_LENGTH_MIN = (
                (4 * ctypes.sizeof(UCHAR)) +
                (3 * ctypes.sizeof(ULONG)) +
                ctypes.sizeof(PVOID)
            )

            # NOTE - may want to cap it instead of using ULONG_MAX. Max is 65KB
            # currently (XCDB)
            SRBEX_DATA_SCSI_CDB_VAR_LENGTH_MAX = 0xFFFFFFFF
            _SRBEX_DATA_SCSI_CDB_VAR._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('ScsiStatus', UCHAR),
                ('SenseInfoBufferLength', UCHAR),
                ('Reserved', UCHAR * 2),
                ('CdbLength', ULONG),
                ('Reserved1', ULONG * 2),
                ('POINTER_ALIGN SenseInfoBuffer', PVOID),
                ('POINTER_ALIGN Cdb', UCHAR * ANYSIZE_ARRAY),
            ]
            # Used by SRB_FUNCTION_WMI
            SRBEX_DATA_WMI_LENGTH = (
                (4 * ctypes.sizeof(UCHAR)) +
                ctypes.sizeof(ULONG) +
                ctypes.sizeof(PVOID)
            )

            _SRBEX_DATA_WMI._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('WMISubFunction', UCHAR),
                ('WMIFlags', UCHAR),
                ('Reserved', UCHAR * 2),
                ('Reserved1', ULONG),
                ('POINTER_ALIGN DataPath', PVOID),
            ]
            # Used by SRB_FUNCTION_POWER
            SRBEX_DATA_POWER_LENGTH = (
                (4 * ctypes.sizeof(UCHAR)) +
                ctypes.sizeof(STOR_DEVICE_POWER_STATE) +
                ctypes.sizeof(STOR_POWER_ACTION)
            )

            _SRBEX_DATA_POWER._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('SrbPowerFlags', UCHAR),
                ('Reserved', UCHAR * 3),
                ('DevicePowerState', STOR_DEVICE_POWER_STATE),
                ('PowerAction', STOR_POWER_ACTION),
            ]
            # Used by SRB_FUNCTION_PNP
            SRBEX_DATA_PNP_LENGTH = (
                (4 * ctypes.sizeof(UCHAR)) +
                ctypes.sizeof(STOR_PNP_ACTION) +
                (2 * ctypes.sizeof(ULONG))
            )

            _SRBEX_DATA_PNP._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('PnPSubFunction', UCHAR),
                ('Reserved', UCHAR * 3),
                ('PnPAction', STOR_PNP_ACTION),
                ('SrbPnPFlags', ULONG),
                ('Reserved1', ULONG),
            ]
            # Use in read/write requests to provide additional info about the
            # IO.
            SRBEX_DATA_IO_INFO_LENGTH = (
                (5 * ctypes.sizeof(ULONG)) + (4 * ctypes.sizeof(UCHAR))
            )

            # Define bit flags used in Flags field
            REQUEST_INFO_NO_CACHE_FLAG = 0x00000001
            REQUEST_INFO_PAGING_IO_FLAG = 0x00000002
            REQUEST_INFO_SEQUENTIAL_IO_FLAG = 0x00000004
            REQUEST_INFO_TEMPORARY_FLAG = 0x00000008
            REQUEST_INFO_WRITE_THROUGH_FLAG = 0x00000010
            REQUEST_INFO_HYBRID_WRITE_THROUGH_FLAG = 0x00000020

            if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
                REQUEST_INFO_NO_FILE_OBJECT_FLAG = 0x00000040
                REQUEST_INFO_VOLSNAP_IO_FLAG = 0x00000080
                REQUEST_INFO_STREAM_FLAG = 0x00000100
            # END IF  (NTDDI_VERSION >= NTDDI_WINTHRESHOLD)

            REQUEST_INFO_VALID_CACHEPRIORITY_FLAG = 0x80000000


            _SRBEX_DATA_IO_INFO._fields_ = [
                ('Type', SRBEXDATATYPE),
                ('Length', ULONG),
                ('Flags', ULONG),
                ('Key', ULONG),
                ('RWLength', ULONG),
                ('IsWriteRequest', BOOLEAN),
                ('CachePriority', UCHAR),
                ('Reserved', UCHAR * 2),
                ('Reserved1', ULONG * 2),
            ]

            # SRB signature - "SRBX" in ASCII
            SRB_SIGNATURE = 0x53524258

            # STORAGE_REQUEST_BLOCK structure version.
            STORAGE_REQUEST_BLOCK_VERSION_1 = 0x1

            _STORAGE_REQUEST_BLOCK_HEADER._fields_ = [
                ('Length', USHORT),
                ('Function', UCHAR),
                ('SrbStatus', UCHAR),
            ]

            # STORAGE_REQUEST_BLOCK is the SRB used for
            # SRB_FUNCTION_STORAGE_REQUEST_BLOCK
            _STORAGE_REQUEST_BLOCK._fields_ = [
                # First 8 bytes of this structure is commom between all SRBs
                # and should have the same meaning as SCSI_REQEUST_BLOCK. To
                # avoid compatibility issues, bytes 4 to 7 will not be used
                # and should be set to 0. These bytes corresponds to the
                # ScsiStatus/WMiSubFunction/SrbPowerFlags/PnPSubFunction,
                # PathId, TargetId and Lun fields in the existing SRBs
                # (e.g. SCSI_REQUEST_BLOCK, SCSI_WMI_REQUEST_BLOCK, etc).
                ('Length', USHORT),
                ('Function', UCHAR),
                ('SrbStatus', UCHAR),
                ('ReservedUchar', UCHAR * 4),
                # General SRB fields. The first 6 fields should not changed
                # between versions of this structure.
                # Signature field
                ('Signature',  ULONG),
                # Version field to denote version of STORAGE_REQUEST_BLOCK
                # structure.
                ('Version', ULONG),
                # Size of this structure including address and SRB extended
                # data.
                ('SrbLength', ULONG),
                ('SrbFunction', ULONG),
                ('SrbFlags', ULONG),
                # Reserved for future use to expand SrbStatus to 32-bit
                ('ReservedUlong', ULONG),
                # Equivalent to QueueTag or Task Tag in SCSI
                ('RequestTag', ULONG),
                # Equivalent to Task Priority in SCSI
                ('RequestPriority', USHORT),
                # Equivalent to QueueAction or Task Attributes in SCSI.
                ('RequestAttribute', USHORT),
                # Request timeout value
                ('TimeOutValue', ULONG),
                # Used to store system failure status information in
                # SrbStatus failure conditions (e.g. SRB_STATUS_INTERNAL_ERROR)
                ('SystemStatus', ULONG),
                # Guard page that should always be zero. Use to guard
                # against misbehaving
                # storage filter drivers and to have defined behavior for
                # drivers that misinterpret
                # new SRB format for old on 32-bit platforms.
                ('ZeroGuard1', ULONG),
                # Offset to address from beginning of structure.
                # Address should follow
                # immediately after STORAGE_REQUEST_BLOCK structure and be a
                # STOR_ADDRESS
                # type address.
                ('AddressOffset', ULONG),
                # Number of SRB extended data
                ('NumSrbExData', ULONG),
                # Data transfer length
                ('DataTransferLength', ULONG),
                # Data buffer
                ('DataBuffer', PVOID),
                # Guard page that should always be zero. Use to guard against
                # misbehaving storage filter drivers and to have defined
                # behavior for drivers that misinterpret
                # new SRB format for old on 64-bit platforms.
                ('ZeroGuard2', PVOID),
                # Original IRP containing the request
                ('OriginalRequest', PVOID),
                # Class driver's per-request context
                ('ClassContext', PVOID),
                # Port driver's per-request context
                ('PortContext', PVOID),
                # Miniport's per-request context
                ('MiniportContext', PVOID),
                ('NextSrb', POINTER(_STORAGE_REQUEST_BLOCK)),
                # Offsets to SRB extended data from beginning of structure.
                # Should follow Address field content and be a SRBEX_DATA type
                # extension.
                ('SrbExDataOffset', ULONG * ANYSIZE_ARRAY),
            ]

            # Define SRB types supported
            SRB_TYPE_SCSI_REQUEST_BLOCK = 0
            SRB_TYPE_STORAGE_REQUEST_BLOCK = 1
            # Define address type supported
            STORAGE_ADDRESS_TYPE_BTL8 = 0
        # END IF  (NTDDI_VERSION >= NTDDI_WIN8)
        # end_ntminitape
        # end_storport
        # end_storportp

        # SCSI Adapter Dependent Routines

        # _Must_inspect_result_
        # BOOLEAN
        # (*PHW_INITIALIZE) (
        # _In_ PVOID DeviceExtension
        # );
        PHW_INITIALIZE = CALLBACK(
            BOOLEAN,
            PVOID
        )

        # _Must_inspect_result_
        # BOOLEAN
        # (*PHW_STARTIO) (
        # _In_ PVOID DeviceExtension,
        # _In_ PSCSI_REQUEST_BLOCK Srb
        # );
        PHW_STARTIO = CALLBACK(
            BOOLEAN,
            PVOID,
            PSCSI_REQUEST_BLOCK
        )

        # _Must_inspect_result_
        # BOOLEAN
        # (*PHW_INTERRUPT) (
        # _In_ PVOID DeviceExtension
        # );
        PHW_INTERRUPT = CALLBACK(
            BOOLEAN,
            PVOID
        )

        # VOID
        # (*PHW_TIMER) (
        # _In_ PVOID DeviceExtension
        # );
        PHW_TIMER = CALLBACK(
            VOID,
            PVOID
        )

        # VOID
        # (*PHW_DMA_STARTED) (
        # _In_ PVOID DeviceExtension
        # );
        PHW_DMA_STARTED = CALLBACK(
            VOID,
            PVOID
        )

        # _Must_inspect_result_
        # ULONG
        # (*PHW_FIND_ADAPTER) (
        # _In_ PVOID DeviceExtension,
        # _In_ PVOID HwContext,
        # _In_ PVOID BusInformation,
        # _In_ PCHAR ArgumentString,
        # _Inout_ PPORT_CONFIGURATION_INFORMATION ConfigInfo,
        # _Out_ PBOOLEAN Again
        # );
        PHW_FIND_ADAPTER = CALLBACK(
            ULONG,
            PVOID,
            PVOID,
            PVOID,
            PCHAR,
            PPORT_CONFIGURATION_INFORMATION,
            PBOOLEAN
        )

        # _Must_inspect_result_
        # BOOLEAN
        # (*PHW_RESET_BUS) (
        # _In_ PVOID DeviceExtension,
        # _In_ ULONG PathId
        # );
        PHW_RESET_BUS = CALLBACK(
            BOOLEAN,
            PVOID,
            ULONG
        )

        # _Must_inspect_result_
        # BOOLEAN
        # (*PHW_ADAPTER_STATE) (
        # _In_ PVOID DeviceExtension,
        # _In_ PVOID Context,
        # _In_ BOOLEAN SaveState
        # );
        PHW_ADAPTER_STATE = CALLBACK(
            BOOLEAN,
            PVOID,
            PVOID,
            BOOLEAN
        )

        # _Must_inspect_result_
        # SCSI_ADAPTER_CONTROL_STATUS
        # (*PHW_ADAPTER_CONTROL) (
        # _In_ PVOID DeviceExtension,
        # _In_ SCSI_ADAPTER_CONTROL_TYPE ControlType,
        # _In_ PVOID Parameters
        # );
        PHW_ADAPTER_CONTROL = CALLBACK(
            SCSI_ADAPTER_CONTROL_STATUS,
            PVOID,
            SCSI_ADAPTER_CONTROL_TYPE,
            PVOID
        )
        # Port driver error codes
        SP_BUS_PARITY_ERROR = 0x0001
        SP_UNEXPECTED_DISCONNECT = 0x0002
        SP_INVALID_RESELECTION = 0x0003
        SP_BUS_TIME_OUT = 0x0004
        SP_PROTOCOL_ERROR = 0x0005
        SP_INTERNAL_ADAPTER_ERROR = 0x0006
        SP_REQUEST_TIMEOUT = 0x0007
        SP_IRQ_NOT_RESPONDING = 0x0008
        SP_BAD_FW_WARNING = 0x0009
        SP_BAD_FW_ERROR = 0x000A
        SP_LOST_WMI_MINIPORT_REQUEST = 0x000B
        # Port driver version flags
        SP_VER_TRACE_SUPPORT = 0x0010
        # Return values for SCSI_HW_FIND_ADAPTER.
        SP_RETURN_NOT_FOUND = 0
        SP_RETURN_FOUND = 1
        SP_RETURN_ERROR = 2
        SP_RETURN_BAD_CONFIG = 3
        # Notification Event Types
        class _SCSI_NOTIFICATION_TYPE(ENUM):
            RequestComplete = 1
            NextRequest = 2
            NextLuRequest = 3
            ResetDetected = 4
            CallDisableInterrupts = 5
            CallEnableInterrupts = 6
            RequestTimerCall = 7
            BusChangeDetected = 8
            WMIEvent = 9
            WMIReregister = 10
            LinkUp = 11
            LinkDown = 12
            QueryTickCount = 13
            BufferOverrunDetected = 14
            TraceNotification = 15

        SCSI_NOTIFICATION_TYPE = _SCSI_NOTIFICATION_TYPE
        PSCSI_NOTIFICATION_TYPE = POINTER(_SCSI_NOTIFICATION_TYPE)

        # Structure passed between miniport initialization
        # and SCSI port initialization
        _HW_INITIALIZATION_DATA._fields_ = [
            ('HwInitializationDataSize', ULONG),
            # MPSABus
            ('AdapterInterfaceType', INTERFACE_TYPE),
            # Miniport driver routines
            ('HwInitialize', PHW_INITIALIZE),
            ('HwStartIo', PHW_STARTIO),
            ('HwInterrupt', PHW_INTERRUPT),
            ('HwFindAdapter', PHW_FIND_ADAPTER),
            ('HwResetBus', PHW_RESET_BUS),
            ('HwDmaStarted', PHW_DMA_STARTED),
            ('HwAdapterState', PHW_ADAPTER_STATE),
            # Miniport driver resources
            ('DeviceExtensionSize', ULONG),
            ('SpecificLuExtensionSize', ULONG),
            ('SrbExtensionSize', ULONG),
            ('NumberOfAccessRanges', ULONG),
            ('Reserved', PVOID),
            # Data buffers must be mapped into virtual address space.
            ('MapBuffers', BOOLEAN),
            # The driver will need to tranlate virtual to physical addresses.
            ('NeedPhysicalAddresses', BOOLEAN),
            # Supports tagged queuing
            ('TaggedQueuing', BOOLEAN),
            # Supports auto request sense.
            ('AutoRequestSense', BOOLEAN),
            # Supports multiple requests per logical unit.
            ('MultipleRequestPerLu', BOOLEAN),
            # Support receive event function.
            ('ReceiveEvent', BOOLEAN),
            # Vendor identification length
            ('VendorIdLength', USHORT),
            # Vendor identification
            ('VendorId', PVOID),
        ]

        # begin_ntminitape
        if not defined(_NTDDK_):
            SCSIPORT_API = DECLSPEC_IMPORT
        else:
            SCSIPORT_API = CALLBACK

        # end_ntminitape
        # Port driver routines called by miniport driver
        scsiport = ctypes.windll.SCSIPORT


        # _Must_inspect_result_
        # _IRQL_requires_max_(PASSIVE_LEVEL)
        # SCSIPORT_API
        # ULONG
        # ScsiPortInitialize(
        # _In_ PVOID Argument1,
        # _In_ PVOID Argument2,
        # _In_ struct _HW_INITIALIZATION_DATA *HwInitializationData,
        # _In_ PVOID HwContext
        # );
        ScsiPortInitialize = scsiport.ScsiPortInitialize
        ScsiPortInitialize.restype = ULONG

        # SCSIPORT_API
        # VOID
        # ScsiPortFreeDeviceBase(
        # _In_ PVOID HwDeviceExtension,
        # _In_ PVOID MappedAddress
        # );
        ScsiPortFreeDeviceBase = scsiport.ScsiPortFreeDeviceBase
        ScsiPortFreeDeviceBase.restype = VOID

        # _Must_inspect_result_
        # SCSIPORT_API
        # ULONG
        # ScsiPortGetBusData(
        # _In_ PVOID DeviceExtension,
        # _In_ ULONG BusDataType,
        # _In_ ULONG SystemIoBusNumber,
        # _In_ ULONG SlotNumber,
        # _In_reads_bytes_(Length) PVOID Buffer,
        # _In_ ULONG Length
        # );
        ScsiPortGetBusData = scsiport.ScsiPortGetBusData
        ScsiPortGetBusData.restype = ULONG

        # _Must_inspect_result_
        # SCSIPORT_API
        # ULONG
        # ScsiPortSetBusDataByOffset(
        # _In_ PVOID DeviceExtension,
        # _In_ ULONG BusDataType,
        # _In_ ULONG SystemIoBusNumber,
        # _In_ ULONG SlotNumber,
        # _In_reads_bytes_(Length) PVOID Buffer,
        # _In_ ULONG Offset,
        # _In_ ULONG Length
        # );
        ScsiPortSetBusDataByOffset = scsiport.ScsiPortSetBusDataByOffset
        ScsiPortSetBusDataByOffset.restype = ULONG

        # _Must_inspect_result_
        # SCSIPORT_API
        # PVOID
        # ScsiPortGetDeviceBase(
        # _In_ PVOID HwDeviceExtension,
        # _In_ INTERFACE_TYPE BusType,
        # _In_ ULONG SystemIoBusNumber,
        # _In_ SCSI_PHYSICAL_ADDRESS IoAddress,
        # _In_ ULONG NumberOfBytes,
        # _In_ BOOLEAN InIoSpace
        # );
        ScsiPortGetDeviceBase = scsiport.ScsiPortGetDeviceBase
        ScsiPortGetDeviceBase.restype = PVOID

        # _Must_inspect_result_
        # SCSIPORT_API
        # PVOID
        # ScsiPortGetLogicalUnit(
        # _In_ PVOID HwDeviceExtension,
        # _In_ UCHAR PathId,
        # _In_ UCHAR TargetId,
        # _In_ UCHAR Lun
        # );
        ScsiPortGetLogicalUnit = scsiport.ScsiPortGetLogicalUnit
        ScsiPortGetLogicalUnit.restype = PVOID

        # _Must_inspect_result_
        # SCSIPORT_API
        # PSCSI_REQUEST_BLOCK
        # ScsiPortGetSrb(
        # _In_ PVOID DeviceExtension,
        # _In_ UCHAR PathId,
        # _In_ UCHAR TargetId,
        # _In_ UCHAR Lun,
        # _In_ LONG QueueTag
        # );
        ScsiPortGetSrb = scsiport.ScsiPortGetSrb
        ScsiPortGetSrb.restype = PSCSI_REQUEST_BLOCK

        # _Must_inspect_result_
        # SCSIPORT_API
        # SCSI_PHYSICAL_ADDRESS
        # ScsiPortGetPhysicalAddress(
        # _In_ PVOID HwDeviceExtension,
        # _In_ PSCSI_REQUEST_BLOCK Srb,
        # _In_ PVOID VirtualAddress,
        # _Out_ ULONG *Length
        # );
        ScsiPortGetPhysicalAddress = scsiport.ScsiPortGetPhysicalAddress
        ScsiPortGetPhysicalAddress.restype = SCSI_PHYSICAL_ADDRESS

        # _Must_inspect_result_
        # SCSIPORT_API
        # PVOID
        # ScsiPortGetVirtualAddress(
        # _In_ PVOID HwDeviceExtension,
        # _In_ SCSI_PHYSICAL_ADDRESS PhysicalAddress
        # );
        ScsiPortGetVirtualAddress = scsiport.ScsiPortGetVirtualAddress
        ScsiPortGetVirtualAddress.restype = PVOID

        # _Must_inspect_result_
        # SCSIPORT_API
        # PVOID
        # ScsiPortGetUncachedExtension(
        # _In_ PVOID HwDeviceExtension,
        # _In_ PPORT_CONFIGURATION_INFORMATION ConfigInfo,
        # _In_ ULONG NumberOfBytes
        # );
        ScsiPortGetUncachedExtension = scsiport.ScsiPortGetUncachedExtension
        ScsiPortGetUncachedExtension.restype = PVOID

        # SCSIPORT_API
        # VOID
        # ScsiPortFlushDma(
        # _In_ PVOID DeviceExtension
        # );
        ScsiPortFlushDma = scsiport.ScsiPortFlushDma
        ScsiPortFlushDma.restype = VOID

        # SCSIPORT_API
        # VOID
        # ScsiPortIoMapTransfer(
        # _In_ PVOID HwDeviceExtension,
        # _In_ PSCSI_REQUEST_BLOCK Srb,
        # _In_ PVOID LogicalAddress,
        # _In_ ULONG Length
        # );
        ScsiPortIoMapTransfer = scsiport.ScsiPortIoMapTransfer
        ScsiPortIoMapTransfer.restype = VOID

        # SCSIPORT_API
        # VOID
        # ScsiPortNotification(
        # _In_ SCSI_NOTIFICATION_TYPE NotificationType,
        # _In_ PVOID HwDeviceExtension,
        # ...
        # );
        ScsiPortNotification = scsiport.ScsiPortNotification
        ScsiPortNotification.restype = VOID

        # SCSIPORT_API
        # VOID
        # ScsiPortLogError(
        # _In_ PVOID HwDeviceExtension,
        # _In_ PSCSI_REQUEST_BLOCK Srb OPTIONAL,
        # _In_ UCHAR PathId,
        # _In_ UCHAR TargetId,
        # _In_ UCHAR Lun,
        # _In_ ULONG ErrorCode,
        # _In_ ULONG UniqueId
        # );
        ScsiPortLogError = scsiport.ScsiPortLogError
        ScsiPortLogError.restype = VOID

        # SCSIPORT_API
        # VOID
        # ScsiPortCompleteRequest(
        # _In_ PVOID HwDeviceExtension,
        # _In_ UCHAR PathId,
        # _In_ UCHAR TargetId,
        # _In_ UCHAR Lun,
        # _In_ UCHAR SrbStatus
        # );
        ScsiPortCompleteRequest = scsiport.ScsiPortCompleteRequest
        ScsiPortCompleteRequest.restype = VOID

        # SCSIPORT_API
        # VOID
        # ScsiPortStallExecution(
        # _In_ ULONG Delay
        # );
        ScsiPortStallExecution = scsiport.ScsiPortStallExecution
        ScsiPortStallExecution.restype = VOID

        if defined(_M_AMD64):
            ScsiPortReadPortUchar = READ_PORT_UCHAR
            ScsiPortReadPortUshort = READ_PORT_USHORT
            ScsiPortReadPortUlong = READ_PORT_ULONG
            ScsiPortReadPortBufferUchar = READ_PORT_BUFFER_UCHAR
            ScsiPortReadPortBufferUshort = READ_PORT_BUFFER_USHORT
            ScsiPortReadPortBufferUlong = READ_PORT_BUFFER_ULONG
            ScsiPortReadRegisterUchar = READ_REGISTER_UCHAR
            ScsiPortReadRegisterUshort = READ_REGISTER_USHORT
            ScsiPortReadRegisterUlong = READ_REGISTER_ULONG
            ScsiPortReadRegisterBufferUchar = READ_REGISTER_BUFFER_UCHAR
            ScsiPortReadRegisterBufferUshort = READ_REGISTER_BUFFER_USHORT
            ScsiPortReadRegisterBufferUlong = READ_REGISTER_BUFFER_ULONG
            ScsiPortWritePortUchar = WRITE_PORT_UCHAR
            ScsiPortWritePortUshort = WRITE_PORT_USHORT
            ScsiPortWritePortUlong = WRITE_PORT_ULONG
            ScsiPortWritePortBufferUchar = WRITE_PORT_BUFFER_UCHAR
            ScsiPortWritePortBufferUshort = WRITE_PORT_BUFFER_USHORT
            ScsiPortWritePortBufferUlong = WRITE_PORT_BUFFER_ULONG
            ScsiPortWriteRegisterUchar = WRITE_REGISTER_UCHAR
            ScsiPortWriteRegisterUshort = WRITE_REGISTER_USHORT
            ScsiPortWriteRegisterUlong = WRITE_REGISTER_ULONG
            ScsiPortWriteRegisterBufferUchar = WRITE_REGISTER_BUFFER_UCHAR
            ScsiPortWriteRegisterBufferUshort = WRITE_REGISTER_BUFFER_USHORT
            ScsiPortWriteRegisterBufferUlong = WRITE_REGISTER_BUFFER_ULONG
            ScsiPortMoveMemory = ctypes.memmove
        else:
            # _Must_inspect_result_
            # SCSIPORT_API
            # UCHAR
            # ScsiPortReadPortUchar(
            # _In_ PUCHAR Port
            # );
            ScsiPortReadPortUchar = scsiport.ScsiPortReadPortUchar
            ScsiPortReadPortUchar.restype = UCHAR

            # _Must_inspect_result_
            # SCSIPORT_API
            # USHORT
            # ScsiPortReadPortUshort(
            # _In_ PUSHORT Port
            # );
            ScsiPortReadPortUshort = scsiport.ScsiPortReadPortUshort
            ScsiPortReadPortUshort.restype = USHORT

            # _Must_inspect_result_
            # SCSIPORT_API
            # ULONG
            # ScsiPortReadPortUlong(
            # _In_ PULONG Port
            # );
            ScsiPortReadPortUlong = scsiport.ScsiPortReadPortUlong
            ScsiPortReadPortUlong.restype = ULONG

            # SCSIPORT_API
            # VOID
            # ScsiPortReadPortBufferUchar(
            # _In_ PUCHAR Port,
            # _In_ PUCHAR Buffer,
            # _In_ ULONG  Count
            # );
            ScsiPortReadPortBufferUchar = scsiport.ScsiPortReadPortBufferUchar
            ScsiPortReadPortBufferUchar.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortReadPortBufferUshort(
            # _In_ PUSHORT Port,
            # _In_ PUSHORT Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortReadPortBufferUshort = (
                scsiport.ScsiPortReadPortBufferUshort
            )
            ScsiPortReadPortBufferUshort.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortReadPortBufferUlong(
            # _In_ PULONG Port,
            # _In_ PULONG Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortReadPortBufferUlong = scsiport.ScsiPortReadPortBufferUlong
            ScsiPortReadPortBufferUlong.restype = VOID

            # _Must_inspect_result_
            # SCSIPORT_API
            # UCHAR
            # ScsiPortReadRegisterUchar(
            # _In_ PUCHAR Register
            # );
            ScsiPortReadRegisterUchar = scsiport.ScsiPortReadRegisterUchar
            ScsiPortReadRegisterUchar.restype = UCHAR

            # _Must_inspect_result_
            # SCSIPORT_API
            # USHORT
            # ScsiPortReadRegisterUshort(
            # _In_ PUSHORT Register
            # );
            ScsiPortReadRegisterUshort = scsiport.ScsiPortReadRegisterUshort
            ScsiPortReadRegisterUshort.restype = USHORT

            # _Must_inspect_result_
            # SCSIPORT_API
            # ULONG
            # ScsiPortReadRegisterUlong(
            # _In_ PULONG Register
            # );
            ScsiPortReadRegisterUlong = scsiport.ScsiPortReadRegisterUlong
            ScsiPortReadRegisterUlong.restype = ULONG

            # SCSIPORT_API
            # VOID
            # ScsiPortReadRegisterBufferUchar(
            # _In_ PUCHAR Register,
            # _In_ PUCHAR Buffer,
            # _In_ ULONG  Count
            # );
            ScsiPortReadRegisterBufferUchar = (
                scsiport.ScsiPortReadRegisterBufferUchar
            )
            ScsiPortReadRegisterBufferUchar.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortReadRegisterBufferUshort(
            # _In_ PUSHORT Register,
            # _In_ PUSHORT Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortReadRegisterBufferUshort = (
                scsiport.ScsiPortReadRegisterBufferUshort
            )
            ScsiPortReadRegisterBufferUshort.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortReadRegisterBufferUlong(
            # _In_ PULONG Register,
            # _In_ PULONG Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortReadRegisterBufferUlong = (
                scsiport.ScsiPortReadRegisterBufferUlong
            )
            ScsiPortReadRegisterBufferUlong.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWritePortUchar(
            # _In_ PUCHAR Port,
            # _In_ UCHAR Value
            # );
            ScsiPortWritePortUchar = scsiport.ScsiPortWritePortUchar
            ScsiPortWritePortUchar.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWritePortUshort(
            # _In_ PUSHORT Port,
            # _In_ USHORT Value
            # );
            ScsiPortWritePortUshort = scsiport.ScsiPortWritePortUshort
            ScsiPortWritePortUshort.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWritePortUlong(
            # _In_ PULONG Port,
            # _In_ ULONG Value
            # );
            ScsiPortWritePortUlong = scsiport.ScsiPortWritePortUlong
            ScsiPortWritePortUlong.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWritePortBufferUchar(
            # _In_ PUCHAR Port,
            # _In_ PUCHAR Buffer,
            # _In_ ULONG  Count
            # );
            ScsiPortWritePortBufferUchar = (
                scsiport.ScsiPortWritePortBufferUchar
            )
            ScsiPortWritePortBufferUchar.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWritePortBufferUshort(
            # _In_ PUSHORT Port,
            # _In_ PUSHORT Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortWritePortBufferUshort = (
                scsiport.ScsiPortWritePortBufferUshort
            )
            ScsiPortWritePortBufferUshort.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWritePortBufferUlong(
            # _In_ PULONG Port,
            # _In_ PULONG Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortWritePortBufferUlong = (
                scsiport.ScsiPortWritePortBufferUlong
            )
            ScsiPortWritePortBufferUlong.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWriteRegisterUchar(
            # _In_ PUCHAR Register,
            # _In_ UCHAR Value
            # );
            ScsiPortWriteRegisterUchar = scsiport.ScsiPortWriteRegisterUchar
            ScsiPortWriteRegisterUchar.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWriteRegisterUshort(
            # _In_ PUSHORT Register,
            # _In_ USHORT Value
            # );
            ScsiPortWriteRegisterUshort = scsiport.ScsiPortWriteRegisterUshort
            ScsiPortWriteRegisterUshort.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWriteRegisterUlong(
            # _In_ PULONG Register,
            # _In_ ULONG Value
            # );
            ScsiPortWriteRegisterUlong = scsiport.ScsiPortWriteRegisterUlong
            ScsiPortWriteRegisterUlong.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWriteRegisterBufferUchar(
            # _In_ PUCHAR Register,
            # _In_ PUCHAR Buffer,
            # _In_ ULONG  Count
            # );
            ScsiPortWriteRegisterBufferUchar = (
                scsiport.ScsiPortWriteRegisterBufferUchar
            )
            ScsiPortWriteRegisterBufferUchar.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWriteRegisterBufferUshort(
            # _In_ PUSHORT Register,
            # _In_ PUSHORT Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortWriteRegisterBufferUshort = (
                scsiport.ScsiPortWriteRegisterBufferUshort
            )
            ScsiPortWriteRegisterBufferUshort.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortWriteRegisterBufferUlong(
            # _In_ PULONG Register,
            # _In_ PULONG Buffer,
            # _In_ ULONG Count
            # );
            ScsiPortWriteRegisterBufferUlong = (
                scsiport.ScsiPortWriteRegisterBufferUlong
            )
            ScsiPortWriteRegisterBufferUlong.restype = VOID

            # SCSIPORT_API
            # VOID
            # ScsiPortMoveMemory(
            # _In_ PVOID WriteBuffer,
            # _In_ PVOID ReadBuffer,
            # _In_ ULONG Length
            # );
            ScsiPortMoveMemory = scsiport.ScsiPortMoveMemory
            ScsiPortMoveMemory.restype = VOID

        # END IF

        # _Must_inspect_result_
        # SCSIPORT_API
        # SCSI_PHYSICAL_ADDRESS
        # ScsiPortConvertUlongToPhysicalAddress(
        # _In_ ULONG_PTR UlongAddress
        # );
        ScsiPortConvertUlongToPhysicalAddress = (
            scsiport.ScsiPortConvertUlongToPhysicalAddress
        )
        ScsiPortConvertUlongToPhysicalAddress.restype = SCSI_PHYSICAL_ADDRESS

        # _Must_inspect_result_
        # SCSIPORT_API
        # ULONG
        # ScsiPortConvertPhysicalAddressToUlong(
        # _In_ SCSI_PHYSICAL_ADDRESS Address
        # );
        ScsiPortConvertPhysicalAddressToUlong = (
            scsiport.ScsiPortConvertPhysicalAddressToUlong
        )
        ScsiPortConvertPhysicalAddressToUlong.restype = ULONG

        # SCSIPORT_API
        # VOID
        # ScsiPortQuerySystemTime(
        # _Out_ PLARGE_INTEGER CurrentTime
        # );
        ScsiPortQuerySystemTime = scsiport.ScsiPortQuerySystemTime
        ScsiPortQuerySystemTime.restype = VOID


        def ScsiPortConvertPhysicalAddressToUlong(Address):
            return Address.LowPart

        # Sundown Note:
        # For now, ScsiPortConvertPhysicalAddressToULongPtr() exists only as a
        # macro.
        def ScsiPortConvertPhysicalAddressToULongPtr(Address):
            return Address.QuadPart

        # _Must_inspect_result_
        # SCSIPORT_API
        # BOOLEAN
        # ScsiPortValidateRange(
        # _In_ PVOID HwDeviceExtension,
        # _In_ INTERFACE_TYPE BusType,
        # _In_ ULONG SystemIoBusNumber,
        # _In_ SCSI_PHYSICAL_ADDRESS IoAddress,
        # _In_ ULONG NumberOfBytes,
        # _In_ BOOLEAN InIoSpace
        # );
        ScsiPortValidateRange = scsiport.ScsiPortValidateRange
        ScsiPortValidateRange.restype = BOOLEAN

        # begin_ntminitape
        # SCSIPORT_API
        # VOID
        # ScsiDebugPrint(
        # ULONG DebugPrintLevel,
        # PCCHAR DebugMessage,
        # ...
        # );
        ScsiDebugPrint = scsiport.ScsiDebugPrint
        ScsiDebugPrint.restype = VOID

        # end_ntminitape
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF
