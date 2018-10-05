from .wtypes_h import (
    UINT,
    POINTER,
    CHAR,
    ULONG,
    USHORT,
)
from .d4iface_h import (
    CHANNEL_HANDLE
)
import ctypes


# ++
# Copyright (c) Microsoft Corporation. All rights reserved.
# Module Name:
# D4drvif.h
# Abstract:
# DOT4 Driver Interface
# --

# Includes


# Defines

MAX_SERVICE_LENGTH = 0x00000028

# Macro definition for defining IOCTL and FSCTL function control codes.  Note
# that function codes 0-2047 are reserved for Microsoft Corporation, and
# 2048-4095 are reserved for customers.


def CTL_CODE(DeviceType, Function, Method, Access):
    return (DeviceType << 16) | (Access << 14) | (Function << 2) | Method


# Define the method codes for how buffers are passed for I/O and FS controls

METHOD_BUFFERED = 0x00000000
METHOD_IN_DIRECT = 0x00000001
METHOD_OUT_DIRECT = 0x00000002
METHOD_NEITHER = 0x00000003

# Define the access check value for any access


# The FILE_READ_ACCESS and FILE_WRITE_ACCESS constants are also defined in
# ntioapi.h as FILE_READ_DATA and FILE_WRITE_DATA. The values for these
# constants *MUST* always be in sync.

# file & pipe
FILE_ANY_ACCESS = 0x00000000
# file & pipe
FILE_READ_ACCESS = 0x00000001
FILE_WRITE_ACCESS = 0x00000002
FILE_DEVICE_DOT4 = 0x00000003a
IOCTL_DOT4_USER_BASE = 0x00000801
IOCTL_DOT4_LAST = IOCTL_DOT4_USER_BASE + 9
IOCTL_DOT4_CREATE_SOCKET = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 7,
    METHOD_OUT_DIRECT,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_DESTROY_SOCKET = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 9,
    METHOD_OUT_DIRECT,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_WAIT_FOR_CHANNEL = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 8,
    METHOD_OUT_DIRECT,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_OPEN_CHANNEL = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 0,
    METHOD_OUT_DIRECT,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_CLOSE_CHANNEL = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 1,
    METHOD_BUFFERED,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_READ = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 2,
    METHOD_OUT_DIRECT,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_WRITE = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 3,
    METHOD_IN_DIRECT,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_ADD_ACTIVITY_BROADCAST = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 4,
    METHOD_BUFFERED,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_REMOVE_ACTIVITY_BROADCAST = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 5,
    METHOD_BUFFERED,
    FILE_ANY_ACCESS,
)
IOCTL_DOT4_WAIT_ACTIVITY_BROADCAST = CTL_CODE(
    FILE_DEVICE_DOT4,
    IOCTL_DOT4_USER_BASE + 6,
    METHOD_OUT_DIRECT,
    FILE_ANY_ACCESS,
)

# Types


class _DOT4_DRIVER_CMD(ctypes.Structure):
    _fields_ = [
        ('hChannelHandle', CHANNEL_HANDLE),
        ('ulSize', ULONG),
        ('ulOffset', ULONG),
        ('ulTimeout', ULONG),
    ]


DOT4_DRIVER_CMD = _DOT4_DRIVER_CMD
PDOT4_DRIVER_CMD = POINTER(_DOT4_DRIVER_CMD)


# Handle to channel
# Length of request
# Offset INTo buffer
# Timeout of operation. Can be INFINITE.

class _DOT4_DC_OPEN_DATA(ctypes.Structure):
    _fields_ = [
        ('CHAR bHsid', UINT),
        ('CHAR fAddActivity', UINT),
        ('hChannelHandle', CHANNEL_HANDLE),
    ]


DOT4_DC_OPEN_DATA = _DOT4_DC_OPEN_DATA
PDOT4_DC_OPEN_DATA = POINTER(_DOT4_DC_OPEN_DATA)


# Host socket created by CREATE_SOCKET
# TRUE to immediately add activity broadcast upon creation
# Handle to channel returned

class _DOT4_DC_CREATE_DATA(ctypes.Structure):
    _fields_ = [
        ('CHAR bPsid', UINT),
        ('pServiceName', CHAR * (MAX_SERVICE_LENGTH + 1)),
        ('CHAR bType', UINT),
        ('ulBufferSize', ULONG),
        ('usMaxHtoPPacketSize', USHORT),
        ('usMaxPtoHPacketSize', USHORT),
        ('CHAR bHsid', UINT),
    ]


DOT4_DC_CREATE_DATA = _DOT4_DC_CREATE_DATA
PDOT4_DC_CREATE_DATA = POINTER(_DOT4_DC_CREATE_DATA)


# This or service name sent
# Type (stream or packet) of channels on socket
# Size of read buffer for channels on socket
# Host socket id returned

class _DOT4_DC_DESTROY_DATA(ctypes.Structure):
    _fields_ = [
        ('CHAR bHsid', UINT),
    ]


DOT4_DC_DESTROY_DATA = _DOT4_DC_DESTROY_DATA
PDOT4_DC_DESTROY_DATA = POINTER(_DOT4_DC_DESTROY_DATA)


# Host socket created by CREATE_SOCKET

# Prototypes

__all__ = (
    'FILE_WRITE_ACCESS', 'CTL_CODE', 'METHOD_OUT_DIRECT', 'IOCTL_DOT4_WRITE',
    'IOCTL_DOT4_WAIT_ACTIVITY_BROADCAST', 'METHOD_NEITHER', 'METHOD_BUFFERED',
    'IOCTL_DOT4_REMOVE_ACTIVITY_BROADCAST', 'IOCTL_DOT4_DESTROY_SOCKET',
    'IOCTL_DOT4_ADD_ACTIVITY_BROADCAST', 'IOCTL_DOT4_USER_BASE',
    'FILE_DEVICE_DOT4', 'IOCTL_DOT4_CREATE_SOCKET', 'METHOD_IN_DIRECT',
    'IOCTL_DOT4_WAIT_FOR_CHANNEL', 'IOCTL_DOT4_OPEN_CHANNEL',
    'IOCTL_DOT4_LAST', 'FILE_READ_ACCESS', 'IOCTL_DOT4_READ',
    'FILE_ANY_ACCESS', 'MAX_SERVICE_LENGTH', 'IOCTL_DOT4_CLOSE_CHANNEL',
    'PDOT4_DC_DESTROY_DATA', '_DOT4_DRIVER_CMD', 'PDOT4_DC_CREATE_DATA',
    '_DOT4_DC_OPEN_DATA', 'DOT4_DC_OPEN_DATA', 'DOT4_DRIVER_CMD',
    '_DOT4_DC_DESTROY_DATA', 'DOT4_DC_DESTROY_DATA', 'PDOT4_DC_OPEN_DATA',
    '_DOT4_DC_CREATE_DATA', 'DOT4_DC_CREATE_DATA', 'PDOT4_DRIVER_CMD',
)
