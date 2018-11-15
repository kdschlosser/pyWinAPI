import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _WINUSB_PIPE_INFORMATION(ctypes.Structure):
    pass


WINUSB_PIPE_INFORMATION = _WINUSB_PIPE_INFORMATION
PWINUSB_PIPE_INFORMATION = POINTER(_WINUSB_PIPE_INFORMATION)


class _WINUSB_PIPE_INFORMATION_EX(ctypes.Structure):
    pass


WINUSB_PIPE_INFORMATION_EX = _WINUSB_PIPE_INFORMATION_EX
PWINUSB_PIPE_INFORMATION_EX = POINTER(_WINUSB_PIPE_INFORMATION_EX)


# *************************************************************************
# Copyright (c) 2002 Microsoft Corporation Module Name: wusbio.h Abstract:
# Public header for WINUSB Environment: User and Kernel Mode Notes: THIS CODE
# AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER
# EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. Copyright (c) 2001
# Microsoft Corporation. All Rights Reserved. Revision History: 11/12/2002 :
# created *

__WUSBIO_H__ = None

if not defined(__WUSBIO_H__):
    __WUSBIO_H__ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WINXP:
            from pyWinAPI.shared.usb_h import * # NOQA

            # Pipe policy types
            SHORT_PACKET_TERMINATE = 0x01
            AUTO_CLEAR_STALL = 0x02
            PIPE_TRANSFER_TIMEOUT = 0x03
            IGNORE_SHORT_PACKETS = 0x04
            ALLOW_PARTIAL_READS = 0x05
            AUTO_FLUSH = 0x06
            RAW_IO = 0x07
            MAXIMUM_TRANSFER_SIZE = 0x08
            RESET_PIPE_ON_RESUME = 0x09

            # Power policy types
            # Add 0x80 for Power policy types in order to prevent overlap with
            # Pipe policy types to prevent "accidentally" setting the wrong
            # value for the
            # wrong type.
            AUTO_SUSPEND = 0x81
            SUSPEND_DELAY = 0x83

            # Device Information types
            DEVICE_SPEED = 0x01

            # Device Speeds
            LowSpeed = 0x01
            FullSpeed = 0x02
            HighSpeed = 0x03

            # {DA812BFF - 12C3 - 46a2 - 8E2B - DBD3B7834C43}
            from pyWinAPI.shared.initguid_h import * # NOQA
            WinUSB_TestGuid = DEFINE_GUID(
                0xDA812BFF,
                0x12C3,
                0x46A2,
                0x8E,
                0x2B,
                0xDB,
                0xD3,
                0xB7,
                0x83,
                0x4C,
                0x43
            )
            _WINUSB_PIPE_INFORMATION._fields_ = [
                ('PipeType', USBD_PIPE_TYPE),
                ('PipeId', UCHAR),
                ('MaximumPacketSize', USHORT),
                ('Interval', UCHAR),
            ]
            _WINUSB_PIPE_INFORMATION_EX._fields_ = [
                ('PipeType', USBD_PIPE_TYPE),
                ('PipeId', UCHAR),
                ('MaximumPacketSize', USHORT),
                ('Interval', UCHAR),
                ('MaximumBytesPerInterval', ULONG),
            ]
        # END IF   (NTDDI_VERSION >= NTDDI_WINXP)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __WUSBIO_H__
