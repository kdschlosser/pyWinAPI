import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _DRV_VERSION(ctypes.Structure):
    pass


DRV_VERSION = _DRV_VERSION
PDRV_VERSION = POINTER(_DRV_VERSION)


class _IO_BLOCK(ctypes.Structure):
    pass


IO_BLOCK = _IO_BLOCK
PIO_BLOCK = POINTER(_IO_BLOCK)


class _IO_BLOCK_EX(ctypes.Structure):
    pass


IO_BLOCK_EX = _IO_BLOCK_EX
PIO_BLOCK_EX = POINTER(_IO_BLOCK_EX)


class _CHANNEL_INFO(ctypes.Structure):
    pass


CHANNEL_INFO = _CHANNEL_INFO
PCHANNEL_INFO = POINTER(_CHANNEL_INFO)


class _USBSCAN_GET_DESCRIPTOR(ctypes.Structure):
    pass


USBSCAN_GET_DESCRIPTOR = _USBSCAN_GET_DESCRIPTOR
PUSBSCAN_GET_DESCRIPTOR = POINTER(_USBSCAN_GET_DESCRIPTOR)


class _DEVICE_DESCRIPTOR(ctypes.Structure):
    pass


DEVICE_DESCRIPTOR = _DEVICE_DESCRIPTOR
PDEVICE_DESCRIPTOR = POINTER(_DEVICE_DESCRIPTOR)


class _USBSCAN_PIPE_INFORMATION(ctypes.Structure):
    pass


USBSCAN_PIPE_INFORMATION = _USBSCAN_PIPE_INFORMATION
PUSBSCAN_PIPE_INFORMATION = POINTER(_USBSCAN_PIPE_INFORMATION)


class _USBSCAN_PIPE_CONFIGURATION(ctypes.Structure):
    pass


USBSCAN_PIPE_CONFIGURATION = _USBSCAN_PIPE_CONFIGURATION
PUSBSCAN_PIPE_CONFIGURATION = POINTER(_USBSCAN_PIPE_CONFIGURATION)


class _USBSCAN_TIMEOUT(ctypes.Structure):
    pass


USBSCAN_TIMEOUT = _USBSCAN_TIMEOUT
PUSBSCAN_TIMEOUT = POINTER(_USBSCAN_TIMEOUT)


# + + Copyright (c) Microsoft Corporation. Module Name: UsbScan.h Abstract:
# Interface with UsbScan kernel driver Environment: User and kernel mode use
# Notes: Interface definition for USB still image driver. - -
if NTDDI_VERSION >= NTDDI_WIN2K:
    _USBSCAN_H_ = None
    if not defined(_USBSCAN_H_):
        _USBSCAN_H_ = 1
        from pyWinAPI.shared.winapifamily_h import * # NOQA

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            MAX_NUM_PIPES = None

            if not defined(MAX_NUM_PIPES):
                MAX_NUM_PIPES = 8
            # END IF

            BULKIN_FLAG = 0x80
            _DRV_VERSION._fields_ = [
                ('major', UINT),
                ('minor', UINT),
                ('internal', UINT),
            ]
            _IO_BLOCK._fields_ = [
                ('uOffset', UINT),
                ('uLength', UINT),
                ('pbyData', PUCHAR),
                ('uIndex', UINT),
            ]
            _IO_BLOCK_EX._fields_ = [
                ('uOffset', UINT),
                ('uLength', UINT),
                ('pbyData', PUCHAR),
                ('uIndex', UINT),
                ('bRequest', UCHAR), # Specific request
                ('bmRequestType', UCHAR), # Bitmap - CHARateristics of request
                ('fTransferDirectionIn', UCHAR), # TRUE - Device - - >Host; FALSE - Host - - >Device
            ]
            _CHANNEL_INFO._fields_ = [
                ('EventChannelSize', UINT),
                ('uReadDataAlignment', UINT),
                ('uWriteDataAlignment', UINT),
            ]


            class PIPE_TYPE(ENUM):
                EVENT_PIPE = 1
                READ_DATA_PIPE = 2
                WRITE_DATA_PIPE = 3
                ALL_PIPE = 4


            EVENT_PIPE = PIPE_TYPE.EVENT_PIPE
            READ_DATA_PIPE = PIPE_TYPE.READ_DATA_PIPE
            WRITE_DATA_PIPE = PIPE_TYPE.WRITE_DATA_PIPE
            ALL_PIPE = PIPE_TYPE.ALL_PIPE
            _USBSCAN_GET_DESCRIPTOR._fields_ = [
                ('DescriptorType', UCHAR), # high byte of wValue field in USB spec.
                ('Index', UCHAR), # low byte of wValue field in USB spec.
                ('LanguageId', USHORT), # wIndex field in USB spec.
            ]

            # The device descriptor structure reports information define in
            # the hardware.
            # If there is enough space to copy the strings, it will be done
            # otherwise
            # only the three first fields:
            # USHORT usVendorId;
            # USHORT usProductId;
            # USHORT usBcdDevice;
            # will contain valid data. Remember: The strings are UNICODE
            # format.
            _DEVICE_DESCRIPTOR._fields_ = [
                ('usVendorId', USHORT),
                ('usProductId', USHORT),
                ('usBcdDevice', USHORT),
                ('usLanguageId', USHORT),
            ]


            class _RAW_PIPE_TYPE(ENUM):
                USBSCAN_PIPE_CONTROL = 1
                USBSCAN_PIPE_ISOCHRONOUS = 2
                USBSCAN_PIPE_BULK = 3
                USBSCAN_PIPE_INTERRUPT = 4


            RAW_PIPE_TYPE = _RAW_PIPE_TYPE
            _USBSCAN_PIPE_INFORMATION._fields_ = [
                ('MaximumPacketSize', USHORT), # Maximum packet size for this pipe
                ('EndpointAddress', UCHAR), # 8 bit USB endpoint address (includes direction)
                ('Interval', UCHAR), # Polling interval in ms if interrupt pipe
                ('PipeType', RAW_PIPE_TYPE), # PipeType identifies type of transfer valid for this pipe
            ]
            _USBSCAN_PIPE_CONFIGURATION._fields_ = [
                ('NumberOfPipes', ULONG),
                ('PipeInfo', USBSCAN_PIPE_INFORMATION * MAX_NUM_PIPES),
            ]
            if NTDDI_VERSION >= NTDDI_WINXP:
                _USBSCAN_TIMEOUT._fields_ = [
                    ('TimeoutRead', ULONG),
                    ('TimeoutWrite', ULONG),
                    ('TimeoutEvent', ULONG),
                ]
            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

            from pyWinAPI.shared.devioctl_h import * # NOQA

            FILE_DEVICE_USB_SCAN = 0x8000
            IOCTL_INDEX = 0x0800
            IOCTL_GET_VERSION = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_CANCEL_IO = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 1,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_WAIT_ON_DEVICE_EVENT = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 2,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_READ_REGISTERS = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 3,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_WRITE_REGISTERS = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 4,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_GET_CHANNEL_ALIGN_RQST = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 5,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_GET_DEVICE_DESCRIPTOR = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 6,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_RESET_PIPE = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 7,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_GET_USB_DESCRIPTOR = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 8,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_SEND_USB_REQUEST = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 9,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )
            IOCTL_GET_PIPE_CONFIGURATION = CTL_CODE(
                FILE_DEVICE_USB_SCAN,
                IOCTL_INDEX + 10,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            if NTDDI_VERSION >= NTDDI_WINXP:
                IOCTL_SET_TIMEOUT = CTL_CODE(
                    FILE_DEVICE_USB_SCAN,
                    IOCTL_INDEX + 11,
                    METHOD_BUFFERED,
                    FILE_ANY_ACCESS,
                )
            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)
            # Temporary to aVOID breaking LOGISCAN code
            ALL = ALL_PIPE
            IOCTL_ABORT_PIPE = IOCTL_CANCEL_IO
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)    # END IF   _USBSCAN_H_# END IF   (NTDDI_VERSION >= NTDDI_WIN2K)
