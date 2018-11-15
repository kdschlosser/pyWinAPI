import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *


class _USBD_VERSION_INFORMATION(ctypes.Structure):
    pass


USBD_VERSION_INFORMATION = _USBD_VERSION_INFORMATION
PUSBD_VERSION_INFORMATION = POINTER(_USBD_VERSION_INFORMATION)


class _USBD_DEVICE_INFORMATION(ctypes.Structure):
    pass


USBD_DEVICE_INFORMATION = _USBD_DEVICE_INFORMATION
PUSBD_DEVICE_INFORMATION = POINTER(_USBD_DEVICE_INFORMATION)


class _USBD_PIPE_INFORMATION(ctypes.Structure):
    pass


USBD_PIPE_INFORMATION = _USBD_PIPE_INFORMATION
PUSBD_PIPE_INFORMATION = POINTER(_USBD_PIPE_INFORMATION)


class _USBD_ENDPOINT_OFFLOAD_INFORMATION(ctypes.Structure):
    pass


USBD_ENDPOINT_OFFLOAD_INFORMATION = _USBD_ENDPOINT_OFFLOAD_INFORMATION
PUSBD_ENDPOINT_OFFLOAD_INFORMATION = POINTER(_USBD_ENDPOINT_OFFLOAD_INFORMATION)


class _USBD_INTERFACE_INFORMATION(ctypes.Structure):
    pass


USBD_INTERFACE_INFORMATION = _USBD_INTERFACE_INFORMATION
PUSBD_INTERFACE_INFORMATION = POINTER(_USBD_INTERFACE_INFORMATION)


class _URB_HCD_AREA(ctypes.Structure):
    pass


class _URB_HEADER(ctypes.Structure):
    pass


class _URB_SELECT_INTERFACE(ctypes.Structure):
    pass


class _URB_SELECT_CONFIGURATION(ctypes.Structure):
    pass


class _URB_PIPE_REQUEST(ctypes.Structure):
    pass


class _URB_FRAME_LENGTH_CONTROL(ctypes.Structure):
    pass


class _URB_GET_FRAME_LENGTH(ctypes.Structure):
    pass


class _URB_SET_FRAME_LENGTH(ctypes.Structure):
    pass


class _URB_GET_CURRENT_FRAME_NUMBER(ctypes.Structure):
    pass


class _URB_CONTROL_DESCRIPTOR_REQUEST(ctypes.Structure):
    pass


class _URB_CONTROL_GET_STATUS_REQUEST(ctypes.Structure):
    pass


class _URB_CONTROL_FEATURE_REQUEST(ctypes.Structure):
    pass


class _URB_CONTROL_VENDOR_OR_CLASS_REQUEST(ctypes.Structure):
    pass


class _URB_CONTROL_GET_INTERFACE_REQUEST(ctypes.Structure):
    pass


class _URB_CONTROL_GET_CONFIGURATION_REQUEST(ctypes.Structure):
    pass


class _OS_STRING(ctypes.Structure):
    pass


OS_STRING = _OS_STRING
POS_STRING = POINTER(_OS_STRING)


class _URB_OS_FEATURE_DESCRIPTOR_REQUEST(ctypes.Structure):
    pass


class _URB_CONTROL_TRANSFER(ctypes.Structure):
    pass


class _URB_CONTROL_TRANSFER_EX(ctypes.Structure):
    pass


class _URB_BULK_OR_INTERRUPT_TRANSFER(ctypes.Structure):
    pass


class _USBD_ISO_PACKET_DESCRIPTOR(ctypes.Structure):
    pass


USBD_ISO_PACKET_DESCRIPTOR = _USBD_ISO_PACKET_DESCRIPTOR
PUSBD_ISO_PACKET_DESCRIPTOR = POINTER(_USBD_ISO_PACKET_DESCRIPTOR)


class _URB_ISOCH_TRANSFER(ctypes.Structure):
    pass


class _USBD_STREAM_INFORMATION(ctypes.Structure):
    pass


USBD_STREAM_INFORMATION = _USBD_STREAM_INFORMATION
PUSBD_STREAM_INFORMATION = POINTER(_USBD_STREAM_INFORMATION)


class _URB_OPEN_STATIC_STREAMS(ctypes.Structure):
    pass


class _URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS(ctypes.Structure):
    pass


class _URB(ctypes.Structure):
    pass


class UrbSelectInterface(_URB_SELECT_INTERFACE):
    pass


class UrbSelectConfiguration(_URB_SELECT_CONFIGURATION):
    pass


class UrbPipeRequest(_URB_PIPE_REQUEST):
    pass


class UrbFrameLengthControl(_URB_FRAME_LENGTH_CONTROL):
    pass


class UrbGetFrameLength(_URB_GET_FRAME_LENGTH):
    pass


class UrbSetFrameLength(_URB_SET_FRAME_LENGTH):
    pass


class UrbGetCurrentFrameNumber(_URB_GET_CURRENT_FRAME_NUMBER):
    pass


class UrbControlTransfer(_URB_CONTROL_TRANSFER):
    pass


class UrbControlTransferEx(_URB_CONTROL_TRANSFER_EX):
    pass


class UrbBulkOrInterruptTransfer(_URB_BULK_OR_INTERRUPT_TRANSFER):
    pass


class UrbIsochronousTransfer(_URB_ISOCH_TRANSFER):
    pass


class UrbControlDescriptorRequest(_URB_CONTROL_DESCRIPTOR_REQUEST):
    pass


class UrbControlGetStatusRequest(_URB_CONTROL_GET_STATUS_REQUEST):
    pass


class UrbControlFeatureRequest(_URB_CONTROL_FEATURE_REQUEST):
    pass


class UrbControlVendorClassRequest(_URB_CONTROL_VENDOR_OR_CLASS_REQUEST):
    pass


class UrbControlGetInterfaceRequest(_URB_CONTROL_GET_INTERFACE_REQUEST):
    pass


class UrbControlGetConfigurationRequest(_URB_CONTROL_GET_CONFIGURATION_REQUEST):
    pass


class UrbOSFeatureDescriptorRequest(_URB_OS_FEATURE_DESCRIPTOR_REQUEST):
    pass


class UrbOpenStaticStreams(_URB_OPEN_STATIC_STREAMS):
    pass


class UrbGetIsochPipeTransferPathDelays(_URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS):
    pass


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# USB.H Abstract: structures and APIs for USB drivers. Environment: Kernel &
# user mode Revision History: 09 - 29 - 95 : created 02 - 10 - 04 : Updated to
# include header versioning - -

__USB_H__ = None

if not defined(__USB_H__):
    __USB_H__ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(PHYSICAL_ADDRESS):
            PHYSICAL_ADDRESS = LARGE_INTEGER
        # END IF

        if not defined(_NTDDK_):
            _WDMDDK_ = None
            if not defined(_WDMDDK_):
                PIRP = PVOID
                PMDL = PVOID
            # END IF
        # END IF

        USBDI_VERSION = 0x00000600
        from pyWinAPI.shared.usbspec_h import * # NOQA


        _WDMDDK_ = None

        if defined(_WDMDDK_):
            pass
        # END IF

        if _MSC_VER >= 1200:
            pass
        # END IF

        USB_PORTATTR_NO_CONNECTOR = 0x00000001
        USB_PORTATTR_SHARED_USB2 = 0x00000002
        USB_PORTATTR_MINI_CONNECTOR = 0x00000004
        USB_PORTATTR_OEM_CONNECTOR = 0x00000008
        USB_PORTATTR_OWNED_BY_CC = 0x01000000
        USB_PORTATTR_NO_OVERCURRENT_UI = 0x02000000


        class _USB_CONTROLLER_FLAVOR(ENUM):
            USB_HcGeneric = 0
            OHCI_Generic = 100
            OHCI_Hydra = 101
            OHCI_NEC = 102
            UHCI_Generic = 200
            UHCI_Piix4 = 201
            UHCI_Piix3 = 202
            UHCI_Ich2 = 203
            UHCI_Reserved204 = 204
            UHCI_Ich1 = 205
            UHCI_Ich3m = 206
            UHCI_Ich4 = 207
            UHCI_Ich5 = 208
            UHCI_Ich6 = 209
            UHCI_Intel = 249
            UHCI_VIA = 250
            UHCI_VIA_x01 = 251
            UHCI_VIA_x02 = 252
            UHCI_VIA_x03 = 253
            UHCI_VIA_x04 = 254
            UHCI_VIA_x0E_FIFO = 264
            EHCI_Generic = 1000
            EHCI_NEC = 2000
            EHCI_Lucent = 3000
            EHCI_NVIDIA_Tegra2 = 4000
            EHCI_NVIDIA_Tegra3 = 4001
            EHCI_Intel_Medfield = 5001


        USB_CONTROLLER_FLAVOR = _USB_CONTROLLER_FLAVOR

        # USB defined structures and constants
        # (see chapter 9 of USB specification)
        USB_DEFAULT_DEVICE_ADDRESS = 0
        USB_DEFAULT_ENDPOINT_ADDRESS = 0

        # max packet size (bytes) for default endpoint
        # until SET_ADDRESS command is received.
        USB_DEFAULT_MAX_PACKET = 64

        # USBD interface structures and constants
        def URB_FROM_IRP(Irp):
            return IoGetCurrentIrpStackLocation(Irp).Parameters.Others.Argument1

        # URB request codes
        URB_FUNCTION_SELECT_CONFIGURATION = 0x0000
        URB_FUNCTION_SELECT_INTERFACE = 0x0001
        URB_FUNCTION_ABORT_PIPE = 0x0002
        URB_FUNCTION_TAKE_FRAME_LENGTH_CONTROL = 0x0003
        URB_FUNCTION_RELEASE_FRAME_LENGTH_CONTROL = 0x0004
        URB_FUNCTION_GET_FRAME_LENGTH = 0x0005
        URB_FUNCTION_SET_FRAME_LENGTH = 0x0006
        URB_FUNCTION_GET_CURRENT_FRAME_NUMBER = 0x0007
        URB_FUNCTION_CONTROL_TRANSFER = 0x0008
        URB_FUNCTION_BULK_OR_INTERRUPT_TRANSFER = 0x0009
        URB_FUNCTION_ISOCH_TRANSFER = 0x000A
        URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE = 0x000B
        URB_FUNCTION_SET_DESCRIPTOR_TO_DEVICE = 0x000C
        URB_FUNCTION_SET_FEATURE_TO_DEVICE = 0x000D
        URB_FUNCTION_SET_FEATURE_TO_INTERFACE = 0x000E
        URB_FUNCTION_SET_FEATURE_TO_ENDPOINT = 0x000F
        URB_FUNCTION_CLEAR_FEATURE_TO_DEVICE = 0x0010
        URB_FUNCTION_CLEAR_FEATURE_TO_INTERFACE = 0x0011
        URB_FUNCTION_CLEAR_FEATURE_TO_ENDPOINT = 0x0012
        URB_FUNCTION_GET_STATUS_FROM_DEVICE = 0x0013
        URB_FUNCTION_GET_STATUS_FROM_INTERFACE = 0x0014
        URB_FUNCTION_GET_STATUS_FROM_ENDPOINT = 0x0015
        URB_FUNCTION_RESERVED_0X0016 = 0x0016
        URB_FUNCTION_VENDOR_DEVICE = 0x0017
        URB_FUNCTION_VENDOR_INTERFACE = 0x0018
        URB_FUNCTION_VENDOR_ENDPOINT = 0x0019
        URB_FUNCTION_CLASS_DEVICE = 0x001A
        URB_FUNCTION_CLASS_INTERFACE = 0x001B
        URB_FUNCTION_CLASS_ENDPOINT = 0x001C
        URB_FUNCTION_RESERVE_0X001D = 0x001D

        # previously URB_FUNCTION_RESET_PIPE
        URB_FUNCTION_SYNC_RESET_PIPE_AND_CLEAR_STALL = 0x001E
        URB_FUNCTION_CLASS_OTHER = 0x001F
        URB_FUNCTION_VENDOR_OTHER = 0x0020
        URB_FUNCTION_GET_STATUS_FROM_OTHER = 0x0021
        URB_FUNCTION_CLEAR_FEATURE_TO_OTHER = 0x0022
        URB_FUNCTION_SET_FEATURE_TO_OTHER = 0x0023
        URB_FUNCTION_GET_DESCRIPTOR_FROM_ENDPOINT = 0x0024
        URB_FUNCTION_SET_DESCRIPTOR_TO_ENDPOINT = 0x0025
        URB_FUNCTION_GET_CONFIGURATION = 0x0026
        URB_FUNCTION_GET_INTERFACE = 0x0027
        URB_FUNCTION_GET_DESCRIPTOR_FROM_INTERFACE = 0x0028
        URB_FUNCTION_SET_DESCRIPTOR_TO_INTERFACE = 0x0029

        # Reserve 0x002B - 0x002F
        URB_FUNCTION_RESERVE_0X002B = 0x002B
        URB_FUNCTION_RESERVE_0X002C = 0x002C
        URB_FUNCTION_RESERVE_0X002D = 0x002D
        URB_FUNCTION_RESERVE_0X002E = 0x002E
        URB_FUNCTION_RESERVE_0X002F = 0x002F

        # USB 2.0 calls start at 0x0030
        if _WIN32_WINNT >= 0x0501:
            URB_FUNCTION_GET_MS_FEATURE_DESCRIPTOR = 0x002A
            URB_FUNCTION_SYNC_RESET_PIPE = 0x0030
            URB_FUNCTION_SYNC_CLEAR_STALL = 0x0031
        # END IF
        if _WIN32_WINNT >= 0x0600:
            URB_FUNCTION_CONTROL_TRANSFER_EX = 0x0032
            URB_FUNCTION_RESERVE_0X0033 = 0x0033
            URB_FUNCTION_RESERVE_0X0034 = 0x0034
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN8:
            URB_FUNCTION_OPEN_STATIC_STREAMS = 0x0035
            URB_FUNCTION_CLOSE_STATIC_STREAMS = 0x0036
            URB_FUNCTION_BULK_OR_INTERRUPT_TRANSFER_USING_CHAINED_MDL = 0x0037
            URB_FUNCTION_ISOCH_TRANSFER_USING_CHAINED_MDL = 0x0038
        # END IF
        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            URB_FUNCTION_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS = 0x003D
        # END IF
        # for backward drivers
        URB_FUNCTION_RESET_PIPE = URB_FUNCTION_SYNC_RESET_PIPE_AND_CLEAR_STALL

        # Values for URB TransferFlags Field
        USBD_SHORT_TRANSFER_OK = 0x00000002
        USBD_START_ISO_TRANSFER_ASAP = 0x00000004
        USBD_DEFAULT_PIPE_TRANSFER = 0x00000008
        USBD_TRANSFER_DIRECTION_OUT = 0
        USBD_TRANSFER_DIRECTION_IN = 1
        USBD_TRANSFER_DIRECTION = USBD_TRANSFER_DIRECTION_IN


        def USBD_TRANSFER_DIRECTION_FLAG(flags):
            return flags & USBD_TRANSFER_DIRECTION


        VALID_TRANSFER_FLAGS_MASK = (
            USBD_SHORT_TRANSFER_OK |
            USBD_TRANSFER_DIRECTION |
            USBD_START_ISO_TRANSFER_ASAP |
            USBD_DEFAULT_PIPE_TRANSFER
        )
        USBD_ISO_START_FRAME_RANGE = 1024
        USBD_STATUS = LONG

        # USBD status codes
        # Status values are 32 bit values layed out as follows:
        # 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
        # 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
        # + - - - + - - - - - - - - - - - - - - - - - - - - - - - - - - - + -
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        # | S |   Status Code      |
        # + - - - + - - - - - - - - - - - - - - - - - - - - - - - - - - - + -
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
        # where
        # S - is the state code
        # 00 - completed with success
        # 01 - request is pending
        # 11, 10 - completed with error
        # Code - is the status code
        # Generic test for success on any status value (non - negative numbers
        # indicate success).
        def USBD_SUCCESS(Status):
            return Status >= 0

        # Generic test for pending status value.
        def USBD_PENDING(Status):
            return Status >> 30 == 1

        # Generic test for error on any status value.
        def USBD_ERROR(Status):
            return Status < 0

        USBD_STATUS_SUCCESS = 0x00000000
        USBD_STATUS_PORT_OPERATION_PENDING = 0x00000001
        USBD_STATUS_PENDING = 0x40000000

        # HC (Hardware) status codes range 0x00000001 - 0x000000FF
        USBD_STATUS_CRC = 0xC0000001
        USBD_STATUS_BTSTUFF = 0xC0000002
        USBD_STATUS_DATA_TOGGLE_MISMATCH = 0xC0000003
        USBD_STATUS_STALL_PID = 0xC0000004
        USBD_STATUS_DEV_NOT_RESPONDING = 0xC0000005
        USBD_STATUS_PID_CHECK_FAILURE = 0xC0000006
        USBD_STATUS_UNEXPECTED_PID = 0xC0000007
        USBD_STATUS_DATA_OVERRUN = 0xC0000008
        USBD_STATUS_DATA_UNDERRUN = 0xC0000009
        USBD_STATUS_RESERVED1 = 0xC000000A
        USBD_STATUS_RESERVED2 = 0xC000000B
        USBD_STATUS_BUFFER_OVERRUN = 0xC000000C
        USBD_STATUS_BUFFER_UNDERRUN = 0xC000000D
        USBD_STATUS_NOT_ACCESSED = 0xC000000F
        USBD_STATUS_FIFO = 0xC0000010
        USBD_STATUS_XACT_ERROR = 0xC0000011
        USBD_STATUS_BABBLE_DETECTED = 0xC0000012
        USBD_STATUS_DATA_BUFFER_ERROR = 0xC0000013
        USBD_STATUS_NO_PING_RESPONSE = 0xC0000014
        USBD_STATUS_INVALID_STREAM_TYPE = 0xC0000015
        USBD_STATUS_INVALID_STREAM_ID = 0xC0000016
        USBD_STATUS_ENDPOINT_HALTED = 0xC0000030

        # Software status codes
        USBD_STATUS_INVALID_URB_FUNCTION = 0x80000200
        USBD_STATUS_INVALID_PARAMETER = 0x80000300
        USBD_STATUS_ERROR_BUSY = 0x80000400
        USBD_STATUS_INVALID_PIPE_HANDLE = 0x80000600
        USBD_STATUS_NO_BANDWIDTH = 0x80000700
        USBD_STATUS_INTERNAL_HC_ERROR = 0x80000800
        USBD_STATUS_ERROR_SHORT_TRANSFER = 0x80000900
        USBD_STATUS_BAD_START_FRAME = 0xC0000A00
        USBD_STATUS_ISOCH_REQUEST_FAILED = 0xC0000B00
        USBD_STATUS_FRAME_CONTROL_OWNED = 0xC0000C00
        USBD_STATUS_FRAME_CONTROL_NOT_OWNED = 0xC0000D00
        USBD_STATUS_NOT_SUPPORTED = 0xC0000E00
        USBD_STATUS_INAVLID_CONFIGURATION_DESCRIPTOR = 0xC0000F00
        USBD_STATUS_INVALID_CONFIGURATION_DESCRIPTOR = 0xC0000F00
        USBD_STATUS_INSUFFICIENT_RESOURCES = 0xC0001000
        USBD_STATUS_SET_CONFIG_FAILED = 0xC0002000
        USBD_STATUS_BUFFER_TOO_SMALL = 0xC0003000
        USBD_STATUS_INTERFACE_NOT_FOUND = 0xC0004000
        USBD_STATUS_INAVLID_PIPE_FLAGS = 0xC0005000
        USBD_STATUS_TIMEOUT = 0xC0006000
        USBD_STATUS_DEVICE_GONE = 0xC0007000
        USBD_STATUS_STATUS_NOT_MAPPED = 0xC0008000
        USBD_STATUS_HUB_INTERNAL_ERROR = 0xC0009000
        USBD_STATUS_CANCELED = 0xC0010000
        USBD_STATUS_ISO_NOT_ACCESSED_BY_HW = 0xC0020000
        USBD_STATUS_ISO_TD_ERROR = 0xC0030000
        USBD_STATUS_ISO_NA_LATE_USBPORT = 0xC0040000
        USBD_STATUS_ISO_NOT_ACCESSED_LATE = 0xC0050000
        USBD_STATUS_BAD_DESCRIPTOR = 0xC0100000
        USBD_STATUS_BAD_DESCRIPTOR_BLEN = 0xC0100001
        USBD_STATUS_BAD_DESCRIPTOR_TYPE = 0xC0100002
        USBD_STATUS_BAD_INTERFACE_DESCRIPTOR = 0xC0100003
        USBD_STATUS_BAD_ENDPOINT_DESCRIPTOR = 0xC0100004
        USBD_STATUS_BAD_INTERFACE_ASSOC_DESCRIPTOR = 0xC0100005
        USBD_STATUS_BAD_CONFIG_DESC_LENGTH = 0xC0100006
        USBD_STATUS_BAD_NUMBER_OF_INTERFACES = 0xC0100007
        USBD_STATUS_BAD_NUMBER_OF_ENDPOINTS = 0xC0100008
        USBD_STATUS_BAD_ENDPOINT_ADDRESS = 0xC0100009
        USBD_PIPE_HANDLE = PVOID
        USBD_CONFIGURATION_HANDLE = PVOID
        USBD_INTERFACE_HANDLE = PVOID

        PAGE_SIZE = 0x1000

        if _WIN32_WINNT >= 0x0501:
            USBD_DEFAULT_MAXIMUM_TRANSFER_SIZE = 0xFFFFFFFF
        else:
            USBD_DEFAULT_MAXIMUM_TRANSFER_SIZE = PAGE_SIZE
        # END IF
        _USBD_VERSION_INFORMATION._fields_ = [
            ('USBDI_Version', ULONG),
            ('Supported_USB_Version', ULONG),
        ]


        class _USBD_PIPE_TYPE(ENUM):
            UsbdPipeTypeControl = 1
            UsbdPipeTypeIsochronous = 2
            UsbdPipeTypeBulk = 3
            UsbdPipeTypeInterrupt = 4


        USBD_PIPE_TYPE = _USBD_PIPE_TYPE


        def USBD_PIPE_DIRECTION_IN(pipeInformation):
            return (
                pipeInformation.EndpointAddress & USB_ENDPOINT_DIRECTION_MASK
            )


        _USBD_DEVICE_INFORMATION._fields_ = [
            ('OffsetNext', ULONG),
            ('UsbdDeviceHandle', PVOID),
            ('DeviceDescriptor', USB_DEVICE_DESCRIPTOR),
        ]
        _USBD_PIPE_INFORMATION._fields_ = [
            ('MaximumPacketSize', USHORT),
            ('EndpointAddress', UCHAR),
            ('Interval', UCHAR),
            ('PipeType', USBD_PIPE_TYPE),
            ('PipeHandle', USBD_PIPE_HANDLE),
            ('MaximumTransferSize', ULONG),
            ('PipeFlags', ULONG),
        ]

        # values for PipeFlags field in USBD_PIPE_INFORMATION struct
        # override the enpoint max_packet size with the value in
        # pipe_information
        # field
        USBD_PF_CHANGE_MAX_PACKET = 0x00000001

        # optimize for SHORT packets 'bulk optimization 1'
        USBD_PF_SHORT_PACKET_OPT = 0x00000002

        # optimize transfers for use with 'real time threads
        USBD_PF_ENABLE_RT_THREAD_ACCESS = 0x00000004

        # causes the driver to allocate map more transfers in the queue.
        USBD_PF_MAP_ADD_TRANSFERS = 0x00000008
        USBD_PF_VIDEO_PRIORITY = 0x00000010
        USBD_PF_VOICE_PRIORITY = 0x00000020
        USBD_PF_INTERACTIVE_PRIORITY = 0x00000030
        USBD_PF_PRIORITY_MASK = 0x000000F0
        USBD_PF_VALID_MASK = (
            USBD_PF_CHANGE_MAX_PACKET |
            USBD_PF_SHORT_PACKET_OPT |
            USBD_PF_ENABLE_RT_THREAD_ACCESS |
            USBD_PF_MAP_ADD_TRANSFERS |
            USBD_PF_VIDEO_PRIORITY |
            USBD_PF_VOICE_PRIORITY |
            USBD_PF_INTERACTIVE_PRIORITY
        )

        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            class _USBD_ENDPOINT_OFFLOAD_MODE(ENUM):
                UsbdEndpointOffloadModeNotSupported = 0
                UsbdEndpointOffloadSoftwareAssisted = 1
                UsbdEndpointOffloadHardwareAssisted = 2


            USBD_ENDPOINT_OFFLOAD_MODE = _USBD_ENDPOINT_OFFLOAD_MODE
            _USBD_ENDPOINT_OFFLOAD_INFORMATION._fields_ = [
                ('Size', ULONG),
                ('EndpointAddress', USHORT), # Input field to be filled in by USB client driver
                ('ResourceId', ULONG),

                # endpoint (in EndpointAddress) was successfully setup for
                # offload mode.
                ('Mode', USBD_ENDPOINT_OFFLOAD_MODE),
                ('RootHubPortNumber', ULONG, 8), # Fields from SLOT_CONTEXT describing the device
                ('RouteString', ULONG, 20),
                ('Speed', ULONG, 4),
                ('UsbDeviceAddress', ULONG, 8),
                ('SlotId', ULONG, 8),
                ('MultiTT', ULONG, 1),
                ('Reserved0', ULONG, 15),
                ('TransferSegmentLA', PHYSICAL_ADDRESS), # Transfer ring information
                ('TransferSegmentVA', PVOID),
                ('TransferRingSize', SIZE_T),
                ('TransferRingInitialCycleBit', ULONG),
                ('MessageNumber', ULONG), # Secondary event ring information
                ('EventRingSegmentLA', PHYSICAL_ADDRESS),
                ('EventRingSegmentVA', PVOID),
                ('EventRingSize', SIZE_T),
                ('EventRingInitialCycleBit', ULONG),
            ]
        # END IF
        _USBD_INTERFACE_INFORMATION._fields_ = [
            ('Length', USHORT),
            ('InterfaceNumber', UCHAR),
            ('AlternateSetting', UCHAR),
            ('Class', UCHAR),
            ('SubClass', UCHAR),
            ('Protocol', UCHAR),
            ('Reserved', UCHAR),
            ('InterfaceHandle', USBD_INTERFACE_HANDLE),
            ('NumberOfPipes', ULONG),
            ('Pipes', USBD_PIPE_INFORMATION * 1),
        ]
        _URB_HCD_AREA._fields_ = [
            ('Reserved8', PVOID * 8),
        ]
        _URB_HEADER._fields_ = [
            ('Length', USHORT),
            ('Function', USHORT),
            ('Status', USBD_STATUS),
            ('UsbdDeviceHandle', PVOID), # Reserved
            ('UsbdFlags', ULONG), # Reserved
        ]
        _URB_SELECT_INTERFACE._fields_ = [
            ('Hdr', _URB_HEADER),
            ('ConfigurationHandle', USBD_CONFIGURATION_HANDLE),
            ('Interface', USBD_INTERFACE_INFORMATION),
        ]
        _URB_SELECT_CONFIGURATION._fields_ = [
            ('Hdr', _URB_HEADER),
            ('ConfigurationDescriptor', PUSB_CONFIGURATION_DESCRIPTOR),
            ('ConfigurationHandle', USBD_CONFIGURATION_HANDLE),
            ('Interface', USBD_INTERFACE_INFORMATION),
        ]
        _URB_PIPE_REQUEST._fields_ = [
            ('Hdr', _URB_HEADER),
            ('PipeHandle', USBD_PIPE_HANDLE),
            ('Reserved', ULONG),
        ]
        _URB_FRAME_LENGTH_CONTROL._fields_ = [
            ('Hdr', _URB_HEADER),
        ]
        _URB_GET_FRAME_LENGTH._fields_ = [
            ('Hdr', _URB_HEADER),
            ('FrameLength', ULONG),
            ('FrameNumber', ULONG),
        ]
        _URB_SET_FRAME_LENGTH._fields_ = [
            ('Hdr', _URB_HEADER),
            ('FrameLengthDelta', LONG),
        ]
        _URB_GET_CURRENT_FRAME_NUMBER._fields_ = [
            ('Hdr', _URB_HEADER),
            ('FrameNumber', ULONG),
        ]
        _URB_CONTROL_DESCRIPTOR_REQUEST._fields_ = [
            ('Hdr', _URB_HEADER),
            ('Reserved', PVOID),
            ('Reserved0', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('Reserved1', USHORT),
            ('Index', UCHAR),
            ('DescriptorType', UCHAR),
            ('LanguageId', USHORT),
            ('Reserved2', USHORT),
        ]
        _URB_CONTROL_GET_STATUS_REQUEST._fields_ = [
            ('Hdr', _URB_HEADER),
            ('Reserved', PVOID),
            ('Reserved0', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('Reserved1', UCHAR * 4),
            ('Index', USHORT),
            ('Reserved2', USHORT),
        ]
        _URB_CONTROL_FEATURE_REQUEST._fields_ = [
            ('Hdr', _URB_HEADER),
            ('Reserved', PVOID),
            ('Reserved2', ULONG),
            ('Reserved3', ULONG),
            ('Reserved4', PVOID),
            ('Reserved5', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('Reserved0', USHORT),
            ('FeatureSelector', USHORT),
            ('Index', USHORT),
            ('Reserved1', USHORT),
        ]
        _URB_CONTROL_VENDOR_OR_CLASS_REQUEST._fields_ = [
            ('Hdr', _URB_HEADER),
            ('Reserved', PVOID),
            ('TransferFlags', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('RequestTypeReservedBits', UCHAR),
            ('Request', UCHAR),
            ('Value', USHORT),
            ('Index', USHORT),
            ('Reserved1', USHORT),
        ]
        _URB_CONTROL_GET_INTERFACE_REQUEST._fields_ = [
            ('Hdr', _URB_HEADER),
            ('Reserved', PVOID),
            ('Reserved0', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('Reserved1', UCHAR * 4),
            ('Interface', USHORT),
            ('Reserved2', USHORT),
        ]
        _URB_CONTROL_GET_CONFIGURATION_REQUEST._fields_ = [
            ('Hdr', _URB_HEADER),
            ('Reserved', PVOID),
            ('Reserved0', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('Reserved1', UCHAR * 8),
        ]
        if _WIN32_WINNT >= 0x0501:
            OS_STRING_DESCRIPTOR_INDEX = 0xEE
            MS_GENRE_DESCRIPTOR_INDEX = 0x0001
            MS_POWER_DESCRIPTOR_INDEX = 0x0002
            MS_OS_STRING_SIGNATURE = "MSFT100"
            MS_OS_FLAGS_CONTAINERID = 0x02


            class _Union_1(ctypes.Union):
                pass


            _Union_1._fields_ = [
                ('bPad', UCHAR),
                ('bFlags', UCHAR),
            ]
            _OS_STRING._Union_1 = _Union_1

            _OS_STRING._anonymous_ = (
                '_Union_1',
            )
            _OS_STRING._fields_ = [
                ('bLength', UCHAR),
                ('bDescriptorType', UCHAR),
                ('MicrosoftString', WCHAR * 7),
                ('bVendorCode', UCHAR),
                ('_Union_1', _OS_STRING._Union_1),
            ]
            _URB_OS_FEATURE_DESCRIPTOR_REQUEST._fields_ = [
                ('Hdr', _URB_HEADER),
                ('Reserved', PVOID),
                ('Reserved0', ULONG),
                ('TransferBufferLength', ULONG),
                ('TransferBuffer', PVOID),
                ('TransferBufferMDL', PMDL),
                ('UrbLink', POINTER(_URB)), # Reserved
                ('hca', _URB_HCD_AREA), # Reserved
                ('Recipient', UCHAR, 5),
                ('Reserved1', UCHAR, 3),
                ('Reserved2', UCHAR),
                ('InterfaceNumber', UCHAR),
                ('MS_PageIndex', UCHAR),
                ('MS_FeatureDescriptorIndex', USHORT),
                ('Reserved3', USHORT),
            ]
        # END IF
        _URB_CONTROL_TRANSFER._fields_ = [
            ('Hdr', _URB_HEADER),
            ('PipeHandle', USBD_PIPE_HANDLE),
            ('TransferFlags', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('SetupPacket', UCHAR * 8),
        ]

        if _WIN32_WINNT >= 0x0600:
            _TEMP__URB_CONTROL_TRANSFER_EX = [
                ('Hdr', _URB_HEADER),
                ('PipeHandle', USBD_PIPE_HANDLE),
                ('TransferFlags', ULONG),
                ('TransferBufferLength', ULONG),
                ('TransferBuffer', PVOID),
                ('TransferBufferMDL', PMDL),
                ('Timeout', ULONG),
            ]

            if defined(WIN64):
                _TEMP__URB_CONTROL_TRANSFER_EX += [
                    ('Pad', ULONG)
                ]

            _TEMP__URB_CONTROL_TRANSFER_EX += [
                ('hca', _URB_HCD_AREA),  # Reserved
                ('SetupPacket', UCHAR * 8)
            ]

            _URB_CONTROL_TRANSFER_EX._fields_ = _TEMP__URB_CONTROL_TRANSFER_EX
            # END IF
        # END IF

        _URB_BULK_OR_INTERRUPT_TRANSFER._fields_ = [
            ('Hdr', _URB_HEADER),
            ('PipeHandle', USBD_PIPE_HANDLE),
            ('TransferFlags', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
        ]
        _USBD_ISO_PACKET_DESCRIPTOR._fields_ = [
            ('Offset', ULONG),
            ('Length', ULONG),
            ('Status', USBD_STATUS),
        ]
        _URB_ISOCH_TRANSFER._fields_ = [
            ('Hdr', _URB_HEADER),
            ('PipeHandle', USBD_PIPE_HANDLE),
            ('TransferFlags', ULONG),
            ('TransferBufferLength', ULONG),
            ('TransferBuffer', PVOID),
            ('TransferBufferMDL', PMDL),
            ('UrbLink', POINTER(_URB)), # Reserved
            ('hca', _URB_HCD_AREA), # Reserved
            ('StartFrame', ULONG),
            ('NumberOfPackets', ULONG),
            ('ErrorCount', ULONG),
            ('IsoPacket', USBD_ISO_PACKET_DESCRIPTOR * 1),
        ]

        if NTDDI_VERSION >= NTDDI_WIN8:
            URB_OPEN_STATIC_STREAMS_VERSION_100 = 0x100
            _USBD_STREAM_INFORMATION._fields_ = [
                ('PipeHandle', USBD_PIPE_HANDLE),
                ('StreamID', ULONG),
                ('MaximumTransferSize', ULONG),
                ('PipeFlags', ULONG),
            ]
            _URB_OPEN_STATIC_STREAMS._fields_ = [
                ('Hdr', _URB_HEADER),
                ('PipeHandle', USBD_PIPE_HANDLE),
                ('NumberOfStreams', ULONG),
                ('StreamInfoVersion', USHORT),
                ('StreamInfoSize', USHORT),
                ('Streams', PUSBD_STREAM_INFORMATION),
            ]
        # END IF

        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            _URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS._fields_ = [
                ('Hdr', _URB_HEADER),
                ('PipeHandle', USBD_PIPE_HANDLE),
                ('MaximumSendPathDelayInMilliSeconds', ULONG),
                ('MaximumCompletionPathDelayInMilliSeconds', ULONG),
            ]
        # END IF

        class _Union_2(ctypes.Union):
            pass



        _TEMP__Union_2 = [
            ('UrbHeader', _URB_HEADER),
            ('UrbSelectInterface', _URB_SELECT_INTERFACE),
            ('UrbSelectConfiguration', _URB_SELECT_CONFIGURATION),
            ('UrbPipeRequest', _URB_PIPE_REQUEST),
            ('UrbFrameLengthControl', _URB_FRAME_LENGTH_CONTROL),
            ('UrbGetFrameLength', _URB_GET_FRAME_LENGTH),
            ('UrbSetFrameLength', _URB_SET_FRAME_LENGTH),
            ('UrbGetCurrentFrameNumber', _URB_GET_CURRENT_FRAME_NUMBER),
            ('UrbControlTransfer', _URB_CONTROL_TRANSFER)
        ]

        if _WIN32_WINNT >= 0x0600:
            _TEMP__Union_2 += [
                ('UrbControlTransferEx', _URB_CONTROL_TRANSFER_EX)
            ]

        # END IF
        _TEMP__Union_2 += [
            ('UrbBulkOrInterruptTransfer', _URB_BULK_OR_INTERRUPT_TRANSFER),
            ('UrbIsochronousTransfer', _URB_ISOCH_TRANSFER),
            ('UrbControlDescriptorRequest', _URB_CONTROL_DESCRIPTOR_REQUEST),
            ('UrbControlGetStatusRequest', _URB_CONTROL_GET_STATUS_REQUEST),
            ('UrbControlFeatureRequest', _URB_CONTROL_FEATURE_REQUEST),
            ('UrbControlVendorClassRequest', _URB_CONTROL_VENDOR_OR_CLASS_REQUEST),
            ('UrbControlGetInterfaceRequest', _URB_CONTROL_GET_INTERFACE_REQUEST),
            ('UrbControlGetConfigurationRequest', _URB_CONTROL_GET_CONFIGURATION_REQUEST)
        ]

        if _WIN32_WINNT >= 0x0501:
            _TEMP__Union_2 += [
                ('UrbOSFeatureDescriptorRequest', _URB_OS_FEATURE_DESCRIPTOR_REQUEST)
            ]
        # END IF

        if NTDDI_VERSION >= NTDDI_WIN8:
            _TEMP__Union_2 += [
                ('UrbOpenStaticStreams', _URB_OPEN_STATIC_STREAMS)
            ]
        # END IF


        if NTDDI_VERSION >= NTDDI_WIN10_RS3:
            _TEMP__Union_2 += [
                ('UrbGetIsochPipeTransferPathDelays', _URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS)
            ]
        # END IF

        _Union_2._fields_ = _TEMP__Union_2
        _URB._Union_2 = _Union_2

        _URB._anonymous_ = (
            '_Union_2',
        )

        _URB._fields_ = [
            ('_Union_2', _URB._Union_2)
        ]

        URB = _URB
        PURB = POINTER(_URB)


        if _MSC_VER >= 1200:
            pass
        # END IF    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)# END IF  __USB_H__
