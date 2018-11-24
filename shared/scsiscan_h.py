import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _SCSISCAN_CMD(ctypes.Structure):
    pass


SCSISCAN_CMD = _SCSISCAN_CMD
PSCSISCAN_CMD = POINTER(_SCSISCAN_CMD)


class _SCSISCAN_INFO(ctypes.Structure):
    pass


SCSISCAN_INFO = _SCSISCAN_INFO
PSCSISCAN_INFO = POINTER(_SCSISCAN_INFO)


# **************************************************************************
# (C) COPYRIGHT 1996 - 2000, MICROSOFT CORP. FILE: scsiscan.h VERSION: 1.0
# DATE: 2/11/1997 DESCRIPTION: IOCTL definitions for the SCSI scanner device
# driver.
# Turns off []
_SCSISCAN_H_ = None

if not defined(_SCSISCAN_H_):
    _SCSISCAN_H_ = 1

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.devioctl_h import *  # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # SCSISCAN_CMD.SrbFlags
        SRB_FLAGS_DISABLE_SYNCH_TRANSFER = 0x00000008
        SRB_FLAGS_DISABLE_AUTOSENSE = 0x00000020
        SRB_FLAGS_DATA_IN = 0x00000040
        SRB_FLAGS_DATA_OUT = 0x00000080
        SRB_FLAGS_NO_DATA_TRANSFER = 0x00000000

        # SCSISCAN_CMD.SrbStatus definitions
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
        SRB_STATUS_QUEUE_FROZEN = 0x40
        SRB_STATUS_AUTOSENSE_VALID = 0x80


        def SRB_STATUS(Status):
            return (
                Status &
                ~(SRB_STATUS_AUTOSENSE_VALID | SRB_STATUS_QUEUE_FROZEN)
            )


        _SCSISCAN_CMD._fields_ = [
            ('Reserved1', ULONG),
            ('Size', ULONG),
            ('SrbFlags', ULONG),
            ('CdbLength', UCHAR),
            ('SenseLength', UCHAR),
            ('Reserved2', UCHAR),
            ('Reserved3', UCHAR),
            ('TransferLength', ULONG),
            ('Cdb', UCHAR * 16),
            ('pSrbStatus', PUCHAR),
            ('pSenseBuffer', PUCHAR),
        ]

        # Temporarily set to 128. Should be determined by other definition.
        MAX_STRING = 128

        _SCSISCAN_INFO._fields_ = [
            ('Size', ULONG),
            ('Flags', ULONG),
            ('PortNumber', UCHAR),
            ('PathId', UCHAR),
            ('TargetId', UCHAR),
            ('Lun', UCHAR),
            ('AdapterName', UCHAR * MAX_STRING),
            ('Reserved', ULONG),
        ]
        SCSISCAN_RESERVED = 0x000
        SCSISCAN_CMD_CODE = 0x004
        SCSISCAN_LOCKDEVICE = 0x005
        SCSISCAN_UNLOCKDEVICE = 0x006
        SCSISCAN_SET_TIMEOUT = 0x007
        SCSISCAN_GET_INFO = 0x008

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # - - - - - - -
        # IOCTL definitions.
        # Use these definitions when calling DeviceIoControl
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # - - - - - - -
        IOCTL_SCSISCAN_CMD = CTL_CODE(
            FILE_DEVICE_SCANNER,
            SCSISCAN_CMD_CODE,
            METHOD_OUT_DIRECT,
            FILE_ANY_ACCESS,
        )
        IOCTL_SCSISCAN_LOCKDEVICE = CTL_CODE(
            FILE_DEVICE_SCANNER,
            SCSISCAN_LOCKDEVICE,
            METHOD_OUT_DIRECT,
            FILE_ANY_ACCESS,
        )
        IOCTL_SCSISCAN_UNLOCKDEVICE = CTL_CODE(
            FILE_DEVICE_SCANNER,
            SCSISCAN_UNLOCKDEVICE,
            METHOD_OUT_DIRECT,
            FILE_ANY_ACCESS,
        )
        IOCTL_SCSISCAN_SET_TIMEOUT = CTL_CODE(
            FILE_DEVICE_SCANNER,
            SCSISCAN_SET_TIMEOUT,
            METHOD_BUFFERED,
            FILE_ANY_ACCESS,
        )
        IOCTL_SCSISCAN_GET_INFO = CTL_CODE(
            FILE_DEVICE_SCANNER,
            SCSISCAN_GET_INFO,
            METHOD_OUT_DIRECT,
            FILE_ANY_ACCESS,
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF
