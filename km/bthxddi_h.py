import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _BTHX_VERSION(ctypes.Structure):
    pass


BTHX_VERSION = _BTHX_VERSION
PBTHX_VERSION = POINTER(_BTHX_VERSION)


class _BTHX_CAPABILITIES(ctypes.Structure):
    pass


BTHX_CAPABILITIES = _BTHX_CAPABILITIES
PBTHX_CAPABILITIES = POINTER(_BTHX_CAPABILITIES)


class _BTHX_HCI_READ_WRITE_CONTEXT(ctypes.Structure):
    pass


BTHX_HCI_READ_WRITE_CONTEXT = _BTHX_HCI_READ_WRITE_CONTEXT
PBTHX_HCI_READ_WRITE_CONTEXT = POINTER(_BTHX_HCI_READ_WRITE_CONTEXT)


# **************************************************************************
# Copyright (c) Microsoft Corporation. All Rights Reserved Module Name:
# BthXDDI.h Abstract: Public IOCTL codes and structure common to BTHMINI and
# its Bluetooth extensible transport driver. Environment: Kernel mode only
# Revision History:
# *************************************************************************

__BTHXDDI_H__ = None

if not defined(__BTHXDDI_H__):
    __BTHXDDI_H__ = 1

    if NTDDI_VERSION >= NTDDI_WIN8:
        from pyWinAPI.shared.devioctl_h import * # NOQA
        # DDI Version definition
        BTHX_DDI_VERSION_1 = 0x00000001        # Initial release version

        # HCI packet types
        class _BTHX_HCI_PACKET_TYPE(ENUM):
            HciPacketCommand = 0x01
            HciPacketAclData = 0x02
            HciPacketEvent = 0x04

        BTHX_HCI_PACKET_TYPE = _BTHX_HCI_PACKET_TYPE

        # IOCTL definitions.
        BTHX_IOCTL_BASE = 0


        def BTHX_CTL(id):
            return CTL_CODE(
                FILE_DEVICE_BLUETOOTH,
                id,
                METHOD_NEITHER,
                FILE_ANY_ACCESS
            )


        # kernel - level (internal) IOCTLs
        IOCTL_BTHX_GET_VERSION = BTHX_CTL(BTHX_IOCTL_BASE + 0x100)
        IOCTL_BTHX_SET_VERSION = BTHX_CTL(BTHX_IOCTL_BASE + 0x101)
        IOCTL_BTHX_QUERY_CAPABILITIES = BTHX_CTL(BTHX_IOCTL_BASE + 0x102)
        IOCTL_BTHX_WRITE_HCI = BTHX_CTL(BTHX_IOCTL_BASE + 0x103)
        IOCTL_BTHX_READ_HCI = BTHX_CTL(BTHX_IOCTL_BASE + 0x104)

        # BTH XDDI Interface Version Structure
        _BTHX_VERSION._fields_ = [
            ('Version', ULONG),
        ]

        # Initialize the version data
        # Bluetooth SCO support option.
        class _BTHX_SCO_SUPPORT(ENUM):
            ScoSupportNone = 0
            ScoSupportHCI = 1
            ScoSupportHCIBypass = 2

        BTHX_SCO_SUPPORT = _BTHX_SCO_SUPPORT
        PBTHX_SCO_SUPPORT = POINTER(_BTHX_SCO_SUPPORT)

        # Bluetooth transport driver's capabilities.
        _BTHX_CAPABILITIES._fields_ = [
            # [out] Max ACL IN transfer.
            ('MaxAclTransferInSize', ULONG),
            # [out] Type of SCO support
            ('ScoSupport', BTHX_SCO_SUPPORT),
            # [out] Max SCO channels supported.
            ('MaxScoChannels', ULONG),
            # [out] TRUE if device can support idle/sleep state.
            ('IsDeviceIdleCapable', BOOLEAN),
            # [out] TRUE if device can support remote wake.
            ('IsDeviceWakeCapable', BOOLEAN),
        ]

        # READ/WRITE context
        _BTHX_HCI_READ_WRITE_CONTEXT._fields_ = [
            # Size of Data
            ('DataLen', ULONG),
            # Packet Type
            ('Type', UCHAR),
            # Actual data
            ('Data', UCHAR * 1),
        ]

    # END IF   NTDDI_VERSION
# END IF   __BTHXDDI_H__
