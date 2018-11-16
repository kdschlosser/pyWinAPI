import ctypes
from pyWinAPI.shared.devioctl_h import *

from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _BTHHFP_DESCRIPTOR(ctypes.Structure):
    pass


BTHHFP_DESCRIPTOR = _BTHHFP_DESCRIPTOR
PBTHHFP_DESCRIPTOR = POINTER(_BTHHFP_DESCRIPTOR)


class _BTHHFP_DESCRIPTOR2(ctypes.Structure):
    pass


BTHHFP_DESCRIPTOR2 = _BTHHFP_DESCRIPTOR2
PBTHHFP_DESCRIPTOR2 = POINTER(_BTHHFP_DESCRIPTOR2)


class _BTHHFP_AUDIO_DEVICE_CAPABILTIES(ctypes.Structure):
    pass


BTHHFP_AUDIO_DEVICE_CAPABILTIES = _BTHHFP_AUDIO_DEVICE_CAPABILTIES
PBTHHFP_AUDIO_DEVICE_CAPABILTIES = POINTER(_BTHHFP_AUDIO_DEVICE_CAPABILTIES)


class _HFP_BYPASS_CODEC_ID_V1(ctypes.Structure):
    pass


HFP_BYPASS_CODEC_ID_V1 = _HFP_BYPASS_CODEC_ID_V1
PHFP_BYPASS_CODEC_ID_V1 = POINTER(_HFP_BYPASS_CODEC_ID_V1)


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: bthhfpddi.h Abstract: This module defines the types, constants, and
# functions that are exposed to device drivers that interact with the Windows
# Bluetooth Handsfree profile driver. - -
# The interface class GUID for HFP SCO HCI bypass
# {BE446647 - F655 - 4919 - 8BD0 - 125BA5D4CE65}
GUID_DEVINTERFACE_BLUETOOTH_HFP_SCO_HCIBYPASS = DEFINE_GUID(
    0xBE446647,
    0xF655,
    0x4919,
    0x8B,
    0xD0,
    0x12,
    0x5B,
    0xA5,
    0xD4,
    0xCE,
    0x65
)
# BTHHFP_DESCRIPTOR
# Describes the characteristics of the Bluetooth HFP device for an audio
# driver. This information does not change while the interface is enabled
# but can change while disabled.
_BTHHFP_DESCRIPTOR._fields_ = [
    ('InputPinCategory', GUID),
    ('OutputPinCategory', GUID),
    ('ContainerId', GUID),
    ('SupportsVolume', BOOL),
    ('VolumePropertyValuesSize', ULONG),
    ('FriendlyName', UNICODE_STRING),
]
_BTHHFP_DESCRIPTOR2._fields_ = [
    ('InputPinCategory', GUID),
    ('OutputPinCategory', GUID),
    ('ContainerId', GUID),
    ('SupportsVolume', BOOL),
    ('VolumePropertyValuesSize', ULONG),
    ('FriendlyName', UNICODE_STRING),
    ('SupportsNREC', BOOL),
]
_BTHHFP_AUDIO_DEVICE_CAPABILTIES._fields_ = [
    ('Version', DWORD),
    ('Supports16kHzSampling', BOOL),
]
AUDIO_DEVICE_CAPABILITIES_VERSION = 1

ntoskrnl = ctypes.windll.NTOSKRNL

# VOID
# FORCEINLINE
# BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT(
# _Out_ PBTHHFP_AUDIO_DEVICE_CAPABILTIES caps
# )
# {
# RtlZeroMemory(caps, (ctypes.sizeof(BTHHFP_AUDIO_DEVICE_CAPABILTIES));
RtlZeroMemory = ntoskrnl.RtlZeroMemory
RtlZeroMemory.restype = VOID


class _HFP_BYPASS_CODEC_ID_VERSION(ENUM):
    REQ_HFP_BYPASS_CODEC_ID_V1 = 1


HFP_BYPASS_CODEC_ID_VERSION = _HFP_BYPASS_CODEC_ID_VERSION
PHFP_BYPASS_CODEC_ID_VERSION = POINTER(_HFP_BYPASS_CODEC_ID_VERSION)

_HFP_BYPASS_CODEC_ID_V1._fields_ = [
    ('CodecId', UCHAR),
]


# The control codes used by an audio driver when cooperating with the
# HF profile class driver to operate a SCO HCI bypass connection.
def BTHHFP_IOCTL(_index_):
    return CTL_CODE(
        FILE_DEVICE_UNKNOWN,
        _index_,
        METHOD_NEITHER,
        FILE_ANY_ACCESS
    )


IOCTL_BTHHFP_GET_DEVICEOBJECT = BTHHFP_IOCTL(0)
IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR = BTHHFP_IOCTL(100)
IOCTL_BTHHFP_DEVICE_GET_VOLUMEPROPERTYVALUES = BTHHFP_IOCTL(101)
IOCTL_BTHHFP_DEVICE_GET_KSNODETYPES = BTHHFP_IOCTL(1) # will be deprecated
IOCTL_BTHHFP_DEVICE_GET_CONTAINERID = BTHHFP_IOCTL(2) # will be deprecated
IOCTL_BTHHFP_DEVICE_REQUEST_CONNECT = BTHHFP_IOCTL(3)
IOCTL_BTHHFP_DEVICE_REQUEST_DISCONNECT = BTHHFP_IOCTL(4)
IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE = BTHHFP_IOCTL(5)
IOCTL_BTHHFP_SPEAKER_SET_VOLUME = BTHHFP_IOCTL(6)
IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE = BTHHFP_IOCTL(7)
IOCTL_BTHHFP_MIC_SET_VOLUME = BTHHFP_IOCTL(8)
IOCTL_BTHHFP_MIC_GET_VOLUME_STATUS_UPDATE = BTHHFP_IOCTL(9)
IOCTL_BTHHFP_STREAM_OPEN = BTHHFP_IOCTL(10)
IOCTL_BTHHFP_STREAM_CLOSE = BTHHFP_IOCTL(11)
IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE = BTHHFP_IOCTL(12)

if NTDDI_VERSION >= NTDDI_WINBLUE:
    IOCTL_BTHHFP_DEVICE_GET_DESCRIPTOR2 = BTHHFP_IOCTL(13)
    IOCTL_BTHHFP_DEVICE_GET_NRECDISABLE_STATUS_UPDATE = BTHHFP_IOCTL(14)
    IOCTL_BTHHFP_DEVICE_GET_CODEC_ID = BTHHFP_IOCTL(15)
# END IF

if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
    IOCTL_BTHHFP_DEVICE_INDICATE_AUDIO_DEVICE_CAPABILITIES = BTHHFP_IOCTL(16)
# END IF
