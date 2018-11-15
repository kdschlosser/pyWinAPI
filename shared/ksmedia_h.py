from .winapifamily_h import *  # NOQA
from .ks_h import *
from .mmreg_h import *
from .vptype_h import *
from .wtypes_h import (
    ENUM,
    ULONG,
    LONG,
    POINTER,
    SIZE,
    LONGLONG,
    RECT,
    DWORD,
    REFERENCE_TIME,
    BYTE,
    ULONGLONG,
    GUID,
    USHORT,
    SHORT,
    WORD,
    BOOL,
    FLOAT,
    DWORDLONG,
    PVOID,
    UCHAR,
    WCHAR,
    LUID,
    DOUBLE,
    ULARGE_INTEGER,
    UINT,
    INT,
    ULONG_PTR,
    UINT_PTR,
    UINT32,
    TCHAR,
    LARGE_INTEGER,
    CHAR,
    HANDLE,
    UINT64,
    ULONG64,
    NULL,
    COLORREF,
    FIELD_OFFSET,
)
from .guiddef_h import (
    DEFINE_GUIDSTRUCT,
    DEFINE_GUIDNAMED
)
import ctypes
from .devpropdef_h import DEFINE_DEVPROPKEY
from .dciddi_h1 import RGNDATAHEADER
from .strmif_h import COLORKEY

ANYSIZE_ARRAY = 1
MAX_PATH = 256


# ++
# Copyright (c) Microsoft Corporation. All rights reserved.
# Module Name:
# ksmedia.h
# Abstract:
# WDM-CSA Multimedia Definitions.
# --
# !defined(_KS_)
# nameless struct/union
# bit field types other than INT

class KSMULTIPLE_DATA_PROP(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('MultipleItem', KSMULTIPLE_ITEM),
    ]


PKSMULTIPLE_DATA_PROP = POINTER(KSMULTIPLE_DATA_PROP)





# Reserved for system use
# Reserved for system use
class KSINTERFACE_MEDIA(ENUM):
    KSINTERFACE_MEDIA_MUSIC = 0
    KSINTERFACE_MEDIA_WAVE_BUFFERED = 1
    KSINTERFACE_MEDIA_WAVE_QUEUED = 2


# {4e1cecd2-1679-463b-a72f-a5bf64c86eba}


def INIT_USBAUDIO_MID(guid, id):
    guid.Data1 = 0x4e1cecd2 + id
    guid.Data2 = 0x1679
    guid.Data3 = 0x463b
    guid.Data4[0] = 0xa7
    guid.Data4[1] = 0x2f
    guid.Data4[2] = 0xa5
    guid.Data4[3] = 0xbf
    guid.Data4[4] = 0x64
    guid.Data4[5] = 0xc8
    guid.Data4[6] = 0x6e
    guid.Data4[7] = 0xba
    return guid


def EXTRACT_USBAUDIO_MID(guid):
    return guid.Data1 - 0x4e1cecd2


def DEFINE_USBAUDIO_MID_GUID(id):
    return (
        0x4e1cecd2 + id,
        0x1679,
        0x463b,
        0xa7,
        0x2f,
        0xa5,
        0xbf,
        0x64,
        0xc8,
        0x6e,
        0xba
    )


INIT_EXBUS_MANUFACTURER_ID = INIT_USBAUDIO_MID


def IS_COMPATIBLE_USBAUDIO_MID(guid):
    return (
        (guid.Data1 >= 0x4e1cecd2) and
        (guid.Data1 < 0x4e1cecd2 + 0xffff) and
        (guid.Data2 == 0x1679) and
        (guid.Data3 == 0x463b) and
        (guid.Data4[0] == 0xa7) and
        (guid.Data4[1] == 0x2f) and
        (guid.Data4[2] == 0xa5) and
        (guid.Data4[3] == 0xbf) and
        (guid.Data4[4] == 0x64) and
        (guid.Data4[5] == 0xc8) and
        (guid.Data4[6] == 0x6e) and
        (guid.Data4[7] == 0xba)
    )


# !defined(INIT_USBAUDIO_MID)
# {abcc5a5e-c263-463b-a72f-a5bf64c86eba}


def INIT_USBAUDIO_PID(guid, id):
    guid.Data1 = 0xabcc5a5e + id
    guid.Data2 = 0xc263
    guid.Data3 = 0x463b
    guid.Data4[0] = 0xa7
    guid.Data4[1] = 0x2f
    guid.Data4[2] = 0xa5
    guid.Data4[3] = 0xbf
    guid.Data4[4] = 0x64
    guid.Data4[5] = 0xc8
    guid.Data4[6] = 0x6e
    guid.Data4[7] = 0xba
    return guid


def EXTRACT_USBAUDIO_PID(guid):
    return guid.Data1 - 0xabcc5a5e


def DEFINE_USBAUDIO_PID_GUID(id):
    return (
        0xabcc5a5e + id,
        0xc263,
        0x463b,
        0xa7,
        0x2f,
        0xa5,
        0xbf,
        0x64,
        0xc8,
        0x6e,
        0xba
    )


INIT_EXBUS_PRODUCT_ID = INIT_USBAUDIO_PID


def IS_COMPATIBLE_USBAUDIO_PID(guid):
    return (
        (guid.Data1 >= 0xabcc5a5e) and
        (guid.Data1 < 0xabcc5a5e + 0xffff) and
        (guid.Data2 == 0xc263) and
        (guid.Data3 == 0x463b) and
        (guid.Data4[0] == 0xa7) and
        (guid.Data4[1] == 0x2f) and
        (guid.Data4[2] == 0xa5) and
        (guid.Data4[3] == 0xbf) and
        (guid.Data4[4] == 0x64) and
        (guid.Data4[5] == 0xc8) and
        (guid.Data4[6] == 0x6e) and
        (guid.Data4[7] == 0xba)
    )


# !defined(INIT_USBAUDIO_PID)
# {FC575048-2E08-463B-A72F-A5BF64C86EBA}


def INIT_USBAUDIO_PRODUCT_NAME(guid, vid, pid, strIndex):
    guid.Data1 = 0xFC575048 + vid
    guid.Data2 = 0x2E08 + pid
    guid.Data3 = 0x463B + strIndex
    guid.Data4[0] = 0xA7
    guid.Data4[1] = 0x2F
    guid.Data4[2] = 0xA5
    guid.Data4[3] = 0xBF
    guid.Data4[4] = 0x64
    guid.Data4[5] = 0xC8
    guid.Data4[6] = 0x6E
    guid.Data4[7] = 0xBA
    return guid


def DEFINE_USBAUDIO_PRODUCT_NAME(vid, pid, strIndex):
    return (
        0xFC575048 + vid,
        0x2E08 + pid,
        0x463B + strIndex,
        0xA7,
        0x2F,
        0xA5,
        0xBF,
        0x64,
        0xC8,
        0x6E,
        0xBA
    )


# USB Component ID
INIT_EXBUS_PRODUCT_NAME = INIT_USBAUDIO_PRODUCT_NAME


# USB Terminals
def INIT_USB_TERMINAL(guid, id):
    guid.Data1 = 0xDFF219E0 + id
    guid.Data2 = 0xF70F
    guid.Data3 = 0x11D0
    guid.Data4[0] = 0xb9
    guid.Data4[1] = 0x17
    guid.Data4[2] = 0x00
    guid.Data4[3] = 0xa0
    guid.Data4[4] = 0xc9
    guid.Data4[5] = 0x22
    guid.Data4[6] = 0x31
    guid.Data4[7] = 0x96
    return guid


def EXTRACT_USB_TERMINAL(guid):
    return guid.Data1 - 0xDFF219E0


def DEFINE_USB_TERMINAL_GUID(id):
    return (
        0xDFF219E0 + id,
        0xF70F,
        0x11D0,
        0xB9,
        0x17,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )


def DEFINE_WAVEFORMATEX_GUID(x):
    return (
        x,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xaa,
        0x00,
        0x38,
        0x9b,
        0x71
    )


def INIT_WAVEFORMATEX_GUID(Guid, x):
    Guid = KSDATAFORMAT_SUBTYPE_WAVEFORMATEX
    Guid.Data1 = x
    return Guid


def EXTRACT_WAVEFORMATEX_ID(Guid):
    return Guid.Data1


def IS_VALID_WAVEFORMATEX_GUID(Guid):
    pass
    # return (
    #     not ctypes.memcmp(
    #         ctypes.byref(KSDATAFORMAT_SUBTYPE_WAVEFORMATEX) + 1,
    #         Guid + 1,
    #         ctypes.sizeof - ctypes.sizeof
    #     )
    # )
# {d5a47fa7-6d98-11d1-a21a-00a0c9223196}


def INIT_MMREG_MID(guid, id):
    guid.Data1 = 0xd5a47fa7 + id
    guid.Data2 = 0x6d98
    guid.Data3 = 0x11d1
    guid.Data4[0] = 0xa2
    guid.Data4[1] = 0x1a
    guid.Data4[2] = 0x00
    guid.Data4[3] = 0xa0
    guid.Data4[4] = 0xc9
    guid.Data4[5] = 0x22
    guid.Data4[6] = 0x31
    guid.Data4[7] = 0x96
    return guid


def EXTRACT_MMREG_MID(guid):
    return guid.Data1 - 0xd5a47fa7


def DEFINE_MMREG_MID_GUID(id):
    return (
        0xd5a47fa7 + id,
        0x6d98,
        0x11d1,
        0xa2,
        0x1a,
        0x00,
        0xa0,
        0xc9,
        0x22,
        0x31,
        0x96
    )


def IS_COMPATIBLE_MMREG_MID(guid):
    return (
        (guid.Data1 >= 0xd5a47fa7) and
        (guid.Data1 < 0xd5a47fa7 + 0xffff) and
        (guid.Data2 == 0x6d98) and
        (guid.Data3 == 0x11d1) and
        (guid.Data4[0] == 0xa2) and
        (guid.Data4[1] == 0x1a) and
        (guid.Data4[2] == 0x00) and
        (guid.Data4[3] == 0xa0) and
        (guid.Data4[4] == 0xc9) and
        (guid.Data4[5] == 0x22) and
        (guid.Data4[6] == 0x31) and
        (guid.Data4[7] == 0x96)
    )
# !defined(INIT_MMREG_MID)
# {e36dc2ac-6d9a-11d1-a21a-00a0c9223196}


def INIT_MMREG_PID(guid, id):
    guid.Data1 = 0xe36dc2ac + id
    guid.Data2 = 0x6d9a
    guid.Data3 = 0x11d1
    guid.Data4[0] = 0xa2
    guid.Data4[1] = 0x1a
    guid.Data4[2] = 0x00
    guid.Data4[3] = 0xa0
    guid.Data4[4] = 0xc9
    guid.Data4[5] = 0x22
    guid.Data4[6] = 0x31
    guid.Data4[7] = 0x96
    return guid


def EXTRACT_MMREG_PID(guid):
    return guid.Data1 - 0xe36dc2ac


def DEFINE_MMREG_PID_GUID(id):
    return (
        0xe36dc2ac + id,
        0x6d9a,
        0x11d1,
        0xa2,
        0x1a,
        0x00,
        0xa0,
        0xc9,
        0x22,
        0x31,
        0x96
    )


def IS_COMPATIBLE_MMREG_PID(guid):
    return (
        (guid.Data1 >= 0xe36dc2ac) and
        (guid.Data1 < 0xe36dc2ac + 0xffff) and
        (guid.Data2 == 0x6d9a) and
        (guid.Data3 == 0x11d1) and
        (guid.Data4[0] == 0xa2) and
        (guid.Data4[1] == 0x1a) and
        (guid.Data4[2] == 0x00) and
        (guid.Data4[3] == 0xa0) and
        (guid.Data4[4] == 0xc9) and
        (guid.Data4[5] == 0x22) and
        (guid.Data4[6] == 0x31) and
        (guid.Data4[7] == 0x96)
    )
# !defined(INIT_MMREG_PID)












# from pshpack1_h import * # NOQA
# known not to contain extra data.


class KSDATAFORMAT_WAVEFORMATEX(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('WaveFormatEx', WAVEFORMATEX),
    ]


PKSDATAFORMAT_WAVEFORMATEX = POINTER(KSDATAFORMAT_WAVEFORMATEX)


class WAVEFORMATEXTENSIBLE(ctypes.Structure):

    class Samples(ctypes.Union):
        _fields_ = [
            ('wValidBitsPerSample', WORD),
            ('wSamplesPerBlock', WORD),
            ('wReserved', WORD),
        ]

    _fields_ = [
        ('Format', WAVEFORMATEX),
        ('Samples', Samples),
        ('dwChannelMask', DWORD),
        ('SubFormat', GUID),
    ]


PWAVEFORMATEXTENSIBLE = POINTER(WAVEFORMATEXTENSIBLE)


# bits of precision
# valid if wBitsPerSample==0
# If neither applies, set to zero.
# which channels are
# present in stream
# !_WAVEFORMATEXTENSIBLE_
# Format of encoded data as it is

class WAVEFORMATEXTENSIBLE_IEC61937(ctypes.Structure):
    _fields_ = [
        ('FormatExt', WAVEFORMATEXTENSIBLE),
        ('dwEncodedSamplesPerSec', DWORD),
        ('dwEncodedChannelCount', DWORD),
        ('dwAverageBytesPerSec', DWORD),
    ]


PWAVEFORMATEXTENSIBLE_IEC61937 = POINTER(WAVEFORMATEXTENSIBLE_IEC61937)


# INTended to be streamed over the link
# Sampling rate of the post-decode audio.
# Channel count of the post-decode audio.
# Byte rate of the content, can be 0.
# !_WAVEFORMATEXTENSIBLE_IEC61937_
# !defined(WAVE_FORMAT_EXTENSIBLE)
WAVE_FORMAT_EXTENSIBLE = 0xFFFE
# Convenient wrapper structure for the case in which the WaveFormatExt is
# known not to contain extra data.


class KSDATAFORMAT_WAVEFORMATEXTENSIBLE(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('WaveFormatExt', WAVEFORMATEXTENSIBLE),
    ]


PKSDATAFORMAT_WAVEFORMATEXTENSIBLE = POINTER(KSDATAFORMAT_WAVEFORMATEXTENSIBLE)


# DirectSound buffer description

class KSDSOUND_BUFFERDESC(ctypes.Structure):
    _fields_ = [
        ('Flags', ULONG),
        ('Control', ULONG),
        ('WaveFormatEx', WAVEFORMATEX),
    ]


PKSDSOUND_BUFFERDESC = POINTER(KSDSOUND_BUFFERDESC)


# DirectSound format

class KSDATAFORMAT_DSOUND(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('BufferDesc', KSDSOUND_BUFFERDESC),
    ]


PKSDATAFORMAT_DSOUND = POINTER(KSDATAFORMAT_DSOUND)


# defined(_INC_MMSYSTEM) or defined(_INC_MMREG)
# from poppack_h import * # NOQA
# DirectSound buffer flags
KSDSOUND_BUFFER_PRIMARY = 0x00000001
KSDSOUND_BUFFER_STATIC = 0x00000002
KSDSOUND_BUFFER_LOCHARDWARE = 0x00000004
# DirectSound buffer control flags
KSDSOUND_BUFFER_LOCSOFTWARE = 0x00000008
KSDSOUND_BUFFER_CTRL_3D = 0x00000001
KSDSOUND_BUFFER_CTRL_FREQUENCY = 0x00000002
KSDSOUND_BUFFER_CTRL_PAN = 0x00000004
KSDSOUND_BUFFER_CTRL_VOLUME = 0x00000008
KSDSOUND_BUFFER_CTRL_POSITIONNOTIFY = 0x00000010


class KSAUDIO_POSITION(ctypes.Structure):
    _fields_ = [
        ('PlayOffset', ULONGLONG),
        ('WriteOffset', ULONGLONG),
        ('PlayOffset', DWORDLONG),
        ('WriteOffset', DWORDLONG),
    ]


PKSAUDIO_POSITION = POINTER(KSAUDIO_POSITION)


# !_NTDDK_
# !_NTDDK_
# The KSAUDIO_PRESENTATION_POSITION structure specifies the current positions
# of audio data being rendered to the KS pin instance.

class KSAUDIO_PRESENTATION_POSITION(ctypes.Structure):
    _fields_ = [
        ('u64PositionInBlocks', UINT64),
        ('u64QPCPosition', UINT64),
    ]


PKSAUDIO_PRESENTATION_POSITION = POINTER(KSAUDIO_PRESENTATION_POSITION)


# The block offset from the start of the stream to the current post-decoded
# uncompressed
# position in the stream, where a block is the group of channels in the same
# sample; for a PCM stream,
# a block is same as a frame. For compressed formats, a block is a single
# sample within a frame
# (eg. each MP3 frame has 1152 samples or 1152 blocks)
# The value of the performance counter at the time that the audio endpoINT
# device read the device
# position (*pu64Position) in response to the KSAUDIO_PRESENTATION_POSITION
# call.
class CONSTRICTOR_OPTION(ENUM):
    CONSTRICTOR_OPTION_DISABLE = 0
    CONSTRICTOR_OPTION_MUTE = 1


# {13E004D6-B066-43BD-913B-A415CD13DA87},2
# DEVPROP_TYPE_BINARY
DEVPKEY_KsAudio_PacketSize_ConstraINTs = DEFINE_DEVPROPKEY(
    0x13E004D6,
    0xB066,
    0x43BD,
    0x91,
    0x3B,
    0xA4,
    0x15,
    0xCD,
    0x13,
    0xDA,
    0x87,
    2
)


class _KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT(ctypes.Structure):
    _fields_ = [
        ('ProcessingMode', GUID),
        ('SamplesPerProcessingPacket', ULONG),
        ('ProcessingPacketDurationInHns', ULONG),
    ]


KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT = (
    _KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT
)


class _KSAUDIO_PACKETSIZE_CONSTRAINTS(ctypes.Structure):
    _fields_ = [
        ('MinPacketPeriodInHns', ULONG),
        ('PacketSizeFileAlignment', ULONG),
        ('Reserved', ULONG),
        ('NumProcessingModeConstraINTs', ULONG),
        (
            'ProcessingModeConstraINTs',
            KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT * ANYSIZE_ARRAY
        ),
    ]


KSAUDIO_PACKETSIZE_CONSTRAINTS = _KSAUDIO_PACKETSIZE_CONSTRAINTS


# {9404F781-7191-409B-8B0B-80BF6EC229AE},2
# DEVPROP_TYPE_BINARY
DEVPKEY_KsAudio_PacketSize_ConstraINTs2 = DEFINE_DEVPROPKEY(
    0x9404F781,
    0x7191,
    0x409B,
    0x8B,
    0xB,
    0x80,
    0xBF,
    0x6E,
    0xC2,
    0x29,
    0xAE,
    2
)


class _KSAUDIO_PACKETSIZE_CONSTRAINTS2(ctypes.Structure):
    _fields_ = [
        ('MinPacketPeriodInHns', ULONG),
        ('PacketSizeFileAlignment', ULONG),
        ('MaxPacketSizeInBytes', ULONG),
        ('NumProcessingModeConstraINTs', ULONG),
        (
            'ProcessingModeConstraINTs',
            KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT * ANYSIZE_ARRAY
        ),
    ]


KSAUDIO_PACKETSIZE_CONSTRAINTS2 = _KSAUDIO_PACKETSIZE_CONSTRAINTS2


# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# ===========================================================================
# Microphone array pin descriptor
class KSMICARRAY_MICTYPE(ENUM):
    KSMICARRAY_MICTYPE_OMNIDIRECTIONAL = 0
    KSMICARRAY_MICTYPE_SUBCARDIOID = 1
    KSMICARRAY_MICTYPE_CARDIOID = 2
    KSMICARRAY_MICTYPE_SUPERCARDIOID = 3
    KSMICARRAY_MICTYPE_HYPERCARDIOID = 4
    KSMICARRAY_MICTYPE_8SHAPED = 5
    KSMICARRAY_MICTYPE_VENDORDEFINED = 0x0F


# Type of Microphone

class KSAUDIO_MICROPHONE_COORDINATES(ctypes.Structure):
    _fields_ = [
        ('usType', USHORT),
        ('wXCoord', SHORT),
        ('wYCoord', SHORT),
        ('wZCoord', SHORT),
        ('wVerticalAngle', SHORT),
        ('wHorizontalAngle', SHORT),
    ]


PKSAUDIO_MICROPHONE_COORDINATES = POINTER(KSAUDIO_MICROPHONE_COORDINATES)


# X Coordinate of Mic
# Y Coordinate of Mic
# Z Coordinate of Mic
# MRA Vertical Angle
# MRA Horizontal Angle
class KSMICARRAY_MICARRAYTYPE(ENUM):
    KSMICARRAY_MICARRAYTYPE_LINEAR = 0
    KSMICARRAY_MICARRAYTYPE_PLANAR = 1
    KSMICARRAY_MICARRAYTYPE_3D = 2


# Version of Mic array specification (0x0100)

class KSAUDIO_MIC_ARRAY_GEOMETRY(ctypes.Structure):
    _fields_ = [
        ('usVersion', USHORT),
        ('usMicArrayType', USHORT),
        ('wVerticalAngleBegin', SHORT),
        ('wVerticalAngleEnd', SHORT),
        ('wHorizontalAngleBegin', SHORT),
        ('wHorizontalAngleEnd', SHORT),
        ('usFrequencyBandLo', USHORT),
        ('usFrequencyBandHi', USHORT),
        ('usNumberOfMicrophones', USHORT),
        ('KsMicCoord', KSAUDIO_MICROPHONE_COORDINATES * 1),
    ]


PKSAUDIO_MIC_ARRAY_GEOMETRY = POINTER(KSAUDIO_MIC_ARRAY_GEOMETRY)


# Type of Mic Array
# Work Volume Vertical Angle Begin
# Work Volume Vertical Angle End
# Work Volume HorizontalAngle Begin
# Work Volume HorizontalAngle End
# Low end of Freq Range
# High end of Freq Range
# Count of microphone
# coordinate structures
# to follow.
# Array of Microphone
# Coordinate structures
# (NTDDI_VERSION >= NTDDI_VISTA)
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
# ===========================================================================
# DirectSound3D HAL

class _DS3DVECTOR(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('x', FLOAT),
            ('dvX', FLOAT),
        ]

    class _Union_1(ctypes.Union):
        _fields_ = [
            ('y', FLOAT),
            ('dvY', FLOAT),
        ]

    class _Union_2(ctypes.Union):
        _fields_ = [
            ('z', FLOAT),
            ('dvZ', FLOAT),
        ]

    _anonymous_ = ('_Union_0', '_Union_1', '_Union_2', )
    _fields_ = [
        ('_Union_0', _Union_0),
        ('_Union_1', _Union_1),
        ('_Union_2', _Union_2),
    ]


DS3DVECTOR = _DS3DVECTOR
PDS3DVECTOR = POINTER(_DS3DVECTOR)



class KSPROPERTY_DIRECTSOUND3DLISTENER(ENUM):
    KSPROPERTY_DIRECTSOUND3DLISTENER_ALL = 0
    KSPROPERTY_DIRECTSOUND3DLISTENER_POSITION = 1
    KSPROPERTY_DIRECTSOUND3DLISTENER_VELOCITY = 2
    KSPROPERTY_DIRECTSOUND3DLISTENER_ORIENTATION = 3
    KSPROPERTY_DIRECTSOUND3DLISTENER_DISTANCEFACTOR = 4
    KSPROPERTY_DIRECTSOUND3DLISTENER_ROLLOFFFACTOR = 5
    KSPROPERTY_DIRECTSOUND3DLISTENER_DOPPLERFACTOR = 6
    KSPROPERTY_DIRECTSOUND3DLISTENER_BATCH = 7
    KSPROPERTY_DIRECTSOUND3DLISTENER_ALLOCATION = 8


class KSDS3D_LISTENER_ALL(ctypes.Structure):
    _fields_ = [
        ('Position', DS3DVECTOR),
        ('Velocity', DS3DVECTOR),
        ('OrientFront', DS3DVECTOR),
        ('OrientTop', DS3DVECTOR),
        ('DistanceFactor', FLOAT),
        ('RolloffFactor', FLOAT),
        ('DopplerFactor', FLOAT),
    ]


PKSDS3D_LISTENER_ALL = POINTER(KSDS3D_LISTENER_ALL)


class KSDS3D_LISTENER_ORIENTATION(ctypes.Structure):
    _fields_ = [
        ('Front', DS3DVECTOR),
        ('Top', DS3DVECTOR),
    ]


PKSDS3D_LISTENER_ORIENTATION = POINTER(KSDS3D_LISTENER_ORIENTATION)



class KSPROPERTY_DIRECTSOUND3DBUFFER(ENUM):
    KSPROPERTY_DIRECTSOUND3DBUFFER_ALL = 0
    KSPROPERTY_DIRECTSOUND3DBUFFER_POSITION = 1
    KSPROPERTY_DIRECTSOUND3DBUFFER_VELOCITY = 2
    KSPROPERTY_DIRECTSOUND3DBUFFER_CONEANGLES = 3
    KSPROPERTY_DIRECTSOUND3DBUFFER_CONEORIENTATION = 4
    KSPROPERTY_DIRECTSOUND3DBUFFER_CONEOUTSIDEVOLUME = 5
    KSPROPERTY_DIRECTSOUND3DBUFFER_MINDISTANCE = 6
    KSPROPERTY_DIRECTSOUND3DBUFFER_MAXDISTANCE = 7
    KSPROPERTY_DIRECTSOUND3DBUFFER_MODE = 8


class KSDS3D_BUFFER_ALL(ctypes.Structure):
    _fields_ = [
        ('Position', DS3DVECTOR),
        ('Velocity', DS3DVECTOR),
        ('InsideConeAngle', ULONG),
        ('OutsideConeAngle', ULONG),
        ('ConeOrientation', DS3DVECTOR),
        ('ConeOutsideVolume', LONG),
        ('MinDistance', FLOAT),
        ('MaxDistance', FLOAT),
        ('Mode', ULONG),
    ]


PKSDS3D_BUFFER_ALL = POINTER(KSDS3D_BUFFER_ALL)


class KSDS3D_BUFFER_CONE_ANGLES(ctypes.Structure):
    _fields_ = [
        ('InsideConeAngle', ULONG),
        ('OutsideConeAngle', ULONG),
    ]


PKSDS3D_BUFFER_CONE_ANGLES = POINTER(KSDS3D_BUFFER_CONE_ANGLES)


KSAUDIO_STEREO_SPEAKER_GEOMETRY_HEADPHONE = (-1)
KSAUDIO_STEREO_SPEAKER_GEOMETRY_MIN = 5
KSAUDIO_STEREO_SPEAKER_GEOMETRY_NARROW = 10
KSAUDIO_STEREO_SPEAKER_GEOMETRY_WIDE = 20
KSAUDIO_STEREO_SPEAKER_GEOMETRY_MAX = 180
KSDSOUND_3D_MODE_NORMAL = 0x00000000
KSDSOUND_3D_MODE_HEADRELATIVE = 0x00000001
# ===========================================================================
KSDSOUND_3D_MODE_DISABLE = 0x00000002
# Definitions INTended for hardware acceleration of the HRTF 3D algorithm
# ===========================================================================
KSDSOUND_BUFFER_CTRL_HRTF_3D = 0x40000000
# This is the size of the struct in bytes


class KSDS3D_HRTF_PARAMS_MSG(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Enabled', ULONG),
        ('SwapChannels', BOOL),
        ('ZeroAzimuth', BOOL),
        ('CrossFadeOutput', BOOL),
        ('FilterSize', ULONG),
    ]


PKSDS3D_HRTF_PARAMS_MSG = POINTER(KSDS3D_HRTF_PARAMS_MSG)


# This is the additional size of the filter coeff in bytes
# HRTF filter quality levels
class KSDS3D_HRTF_FILTER_QUALITY(ENUM):
    FULL_FILTER = 0
    LIGHT_FILTER = 1
    KSDS3D_FILTER_QUALITY_COUNT = 2


# This is the size of the struct in bytes

class KSDS3D_HRTF_INIT_MSG(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Quality', KSDS3D_HRTF_FILTER_QUALITY),
        ('SampleRate', FLOAT),
        ('MaxFilterSize', ULONG),
        ('FilterTransientMuteLength', ULONG),
        ('FilterOverlapBufferLength', ULONG),
        ('OutputOverlapBufferLength', ULONG),
        ('Reserved', ULONG),
    ]


PKSDS3D_HRTF_INIT_MSG = POINTER(KSDS3D_HRTF_INIT_MSG)


# Coefficient formats
class KSDS3D_HRTF_COEFF_FORMAT(ENUM):
    FLOAT_COEFF = 0
    SHORT_COEFF = 1
    KSDS3D_COEFF_COUNT = 2


# Filter methods
class KSDS3D_HRTF_FILTER_METHOD(ENUM):
    DIRECT_FORM = 0
    CASCADE_FORM = 1
    KSDS3D_FILTER_METHOD_COUNT = 2


# Filter methods
class KSDS3D_HRTF_FILTER_VERSION(ENUM):
    DS3D_HRTF_VERSION_1 = 0


class KSDS3D_HRTF_FILTER_FORMAT_MSG(ctypes.Structure):
    _fields_ = [
        ('FilterMethod', KSDS3D_HRTF_FILTER_METHOD),
        ('CoeffFormat', KSDS3D_HRTF_COEFF_FORMAT),
        ('Version', KSDS3D_HRTF_FILTER_VERSION),
        ('Reserved', ULONG),
    ]


PKSDS3D_HRTF_FILTER_FORMAT_MSG = POINTER(KSDS3D_HRTF_FILTER_FORMAT_MSG)



class KSPROPERTY_HRTF3D(ENUM):
    KSPROPERTY_HRTF3D_PARAMS = 0
    KSPROPERTY_HRTF3D_INITIALIZE = 1
    KSPROPERTY_HRTF3D_FILTER_FORMAT = 2


# ===========================================================================
# Definitions related to the obsolete Interaural Time Delay 3D algorithm
# ===========================================================================
# DirectSound3D FIR context

class KSDS3D_ITD_PARAMS(ctypes.Structure):
    _fields_ = [
        ('Channel', LONG),
        ('VolSmoothScale', FLOAT),
        ('TotalDryAttenuation', FLOAT),
        ('TotalWetAttenuation', FLOAT),
        ('SmoothFrequency', LONG),
        ('Delay', LONG),
    ]


PKSDS3D_ITD_PARAMS = POINTER(KSDS3D_ITD_PARAMS)


class KSDS3D_ITD_PARAMS_MSG(ctypes.Structure):
    _fields_ = [
        ('Enabled', ULONG),
        ('LeftParams', KSDS3D_ITD_PARAMS),
        ('RightParams', KSDS3D_ITD_PARAMS),
        ('Reserved', ULONG),
    ]


PKSDS3D_ITD_PARAMS_MSG = POINTER(KSDS3D_ITD_PARAMS_MSG)



class KSPROPERTY_ITD3D(ENUM):
    KSPROPERTY_ITD3D_PARAMS = 0


class KSDATARANGE_AUDIO(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('MaximumChannels', ULONG),
        ('MinimumBitsPerSample', ULONG),
        ('MaximumBitsPerSample', ULONG),
        ('MinimumSampleFrequency', ULONG),
        ('MaximumSampleFrequency', ULONG),
    ]


PKSDATARANGE_AUDIO = POINTER(KSDATARANGE_AUDIO)

# ===========================================================================
# length


class KSPROPERTY_BIBLIOGRAPHIC(ENUM):
    KSPROPERTY_BIBLIOGRAPHIC_LEADER = 'RDL '
    KSPROPERTY_BIBLIOGRAPHIC_LCCN = '010 '
    KSPROPERTY_BIBLIOGRAPHIC_ISBN = '020 '
    KSPROPERTY_BIBLIOGRAPHIC_ISSN = '220 '
    KSPROPERTY_BIBLIOGRAPHIC_CATALOGINGSOURCE = '040 '
    KSPROPERTY_BIBLIOGRAPHIC_MAINPERSONALNAME = '001 '
    KSPROPERTY_BIBLIOGRAPHIC_MAINCORPORATEBODY = '011 '
    KSPROPERTY_BIBLIOGRAPHIC_MAINMEETINGNAME = '111 '
    KSPROPERTY_BIBLIOGRAPHIC_MAINUNIFORMTITLE = '031 '
    KSPROPERTY_BIBLIOGRAPHIC_UNIFORMTITLE = '042 '
    KSPROPERTY_BIBLIOGRAPHIC_TITLESTATEMENT = '542 '
    KSPROPERTY_BIBLIOGRAPHIC_VARYINGFORMTITLE = '642 '
    KSPROPERTY_BIBLIOGRAPHIC_PUBLICATION = '062 '
    KSPROPERTY_BIBLIOGRAPHIC_PHYSICALDESCRIPTION = '003 '
    KSPROPERTY_BIBLIOGRAPHIC_ADDEDENTRYTITLE = '044 '
    KSPROPERTY_BIBLIOGRAPHIC_SERIESSTATEMENT = '094 '
    KSPROPERTY_BIBLIOGRAPHIC_GENERALNOTE = '005 '
    KSPROPERTY_BIBLIOGRAPHIC_BIBLIOGRAPHYNOTE = '405 '
    KSPROPERTY_BIBLIOGRAPHIC_CONTENTSNOTE = '505 '
    KSPROPERTY_BIBLIOGRAPHIC_CREATIONCREDIT = '805 '
    KSPROPERTY_BIBLIOGRAPHIC_CITATION = '015 '
    KSPROPERTY_BIBLIOGRAPHIC_PARTICIPANT = '115 '
    KSPROPERTY_BIBLIOGRAPHIC_SUMMARY = '025 '
    KSPROPERTY_BIBLIOGRAPHIC_TARGETAUDIENCE = '125 '
    KSPROPERTY_BIBLIOGRAPHIC_ADDEDFORMAVAILABLE = '035 '
    KSPROPERTY_BIBLIOGRAPHIC_SYSTEMDETAILS = '835 '
    KSPROPERTY_BIBLIOGRAPHIC_AWARDS = '685 '
    KSPROPERTY_BIBLIOGRAPHIC_ADDEDENTRYPERSONALNAME = '006 '
    KSPROPERTY_BIBLIOGRAPHIC_ADDEDENTRYTOPICALTERM = '056 '
    KSPROPERTY_BIBLIOGRAPHIC_ADDEDENTRYGEOGRAPHIC = '156 '
    KSPROPERTY_BIBLIOGRAPHIC_INDEXTERMGENRE = '556 '
    KSPROPERTY_BIBLIOGRAPHIC_INDEXTERMCURRICULUM = '856 '
    KSPROPERTY_BIBLIOGRAPHIC_ADDEDENTRYUNIFORMTITLE = '037 '
    KSPROPERTY_BIBLIOGRAPHIC_ADDEDENTRYRELATED = '047 '
    KSPROPERTY_BIBLIOGRAPHIC_SERIESSTATEMENTPERSONALNAME = '008 '
    KSPROPERTY_BIBLIOGRAPHIC_SERIESSTATEMENTUNIFORMTITLE = '038 '



class KSPROPERTY_TOPOLOGYNODE(ENUM):
    KSPROPERTY_TOPOLOGYNODE_ENABLE = 1
    KSPROPERTY_TOPOLOGYNODE_RESET = 2


# (NTDDI_VERSION >= NTDDI_WINXP)
# ===========================================================================
# defined(_NTDDK_)

class KSPROPERTY_RTAUDIO(ENUM):
    KSPROPERTY_RTAUDIO_GETPOSITIONFUNCTION = 0
    KSPROPERTY_RTAUDIO_BUFFER = 1
    KSPROPERTY_RTAUDIO_HWLATENCY = 2
    KSPROPERTY_RTAUDIO_POSITIONREGISTER = 3
    KSPROPERTY_RTAUDIO_CLOCKREGISTER = 4
    KSPROPERTY_RTAUDIO_BUFFER_WITH_NOTIFICATION = 5
    KSPROPERTY_RTAUDIO_REGISTER_NOTIFICATION_EVENT = 6
    KSPROPERTY_RTAUDIO_UNREGISTER_NOTIFICATION_EVENT = 7
    KSPROPERTY_RTAUDIO_QUERY_NOTIFICATION_SUPPORT = 9
    KSPROPERTY_RTAUDIO_PACKETCOUNT = 11
    KSPROPERTY_RTAUDIO_PRESENTATION_POSITION = 12
    KSPROPERTY_RTAUDIO_GETREADPACKET = 13
    KSPROPERTY_RTAUDIO_SETWRITEPACKET = 14


class KSRTAUDIO_BUFFER_PROPERTY(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('BaseAddress', PVOID),
        ('RequestedBufferSize', ULONG),
    ]


PKSRTAUDIO_BUFFER_PROPERTY = POINTER(KSRTAUDIO_BUFFER_PROPERTY)


class KSRTAUDIO_BUFFER_PROPERTY32(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('BaseAddress', ULONG),
        ('RequestedBufferSize', ULONG),
    ]


PKSRTAUDIO_BUFFER_PROPERTY32 = POINTER(KSRTAUDIO_BUFFER_PROPERTY32)


class KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('BaseAddress', PVOID),
        ('RequestedBufferSize', ULONG),
        ('NotificationCount', ULONG),
    ]


PKSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION = POINTER(
    KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION
)


class KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION32(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('BaseAddress', ULONG),
        ('RequestedBufferSize', ULONG),
        ('NotificationCount', ULONG),
    ]


PKSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION32 = POINTER(
    KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION32
)


class KSRTAUDIO_BUFFER(ctypes.Structure):
    _fields_ = [
        ('BufferAddress', PVOID),
        ('ActualBufferSize', ULONG),
        ('CallMemoryBarrier', BOOL),
    ]


PKSRTAUDIO_BUFFER = POINTER(KSRTAUDIO_BUFFER)


class KSRTAUDIO_BUFFER32(ctypes.Structure):
    _fields_ = [
        ('BufferAddress', ULONG),
        ('ActualBufferSize', ULONG),
        ('CallMemoryBarrier', BOOL),
    ]


PKSRTAUDIO_BUFFER32 = POINTER(KSRTAUDIO_BUFFER32)


class KSRTAUDIO_HWLATENCY(ctypes.Structure):
    _fields_ = [
        ('FifoSize', ULONG),
        ('ChipsetDelay', ULONG),
        ('CodecDelay', ULONG),
    ]


PKSRTAUDIO_HWLATENCY = POINTER(KSRTAUDIO_HWLATENCY)


class KSRTAUDIO_HWREGISTER_PROPERTY(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('BaseAddress', PVOID),
    ]


PKSRTAUDIO_HWREGISTER_PROPERTY = POINTER(KSRTAUDIO_HWREGISTER_PROPERTY)


class KSRTAUDIO_HWREGISTER_PROPERTY32(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('BaseAddress', ULONG),
    ]


PKSRTAUDIO_HWREGISTER_PROPERTY32 = POINTER(KSRTAUDIO_HWREGISTER_PROPERTY32)


class KSRTAUDIO_HWREGISTER(ctypes.Structure):
    _fields_ = [
        ('Register', PVOID),
        ('Width', ULONG),
        ('Numerator', ULONGLONG),
        ('Denominator', ULONGLONG),
        ('Accuracy', ULONG),
    ]


PKSRTAUDIO_HWREGISTER = POINTER(KSRTAUDIO_HWREGISTER)


class KSRTAUDIO_HWREGISTER32(ctypes.Structure):
    _fields_ = [
        ('Register', ULONG),
        ('Width', ULONG),
        ('Numerator', ULONGLONG),
        ('Denominator', ULONGLONG),
        ('Accuracy', ULONG),
    ]


PKSRTAUDIO_HWREGISTER32 = POINTER(KSRTAUDIO_HWREGISTER32)


class KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NotificationEvent', HANDLE),
    ]


PKSRTAUDIO_NOTIFICATION_EVENT_PROPERTY = POINTER(
    KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY
)


class KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY32(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NotificationEvent', ULONG),
    ]


PKSRTAUDIO_NOTIFICATION_EVENT_PROPERTY32 = POINTER(
    KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY32
)


class KSRTAUDIO_GETREADPACKET_INFO(ctypes.Structure):
    _fields_ = [
        ('PacketNumber', ULONG),
        ('Flags', DWORD),
        ('PerformanceCounterValue', ULONG64),
        ('MoreData', BOOL),
    ]


PKSRTAUDIO_GETREADPACKET_INFO = POINTER(KSRTAUDIO_GETREADPACKET_INFO)


class KSRTAUDIO_SETWRITEPACKET_INFO(ctypes.Structure):
    _fields_ = [
        ('PacketNumber', ULONG),
        ('Flags', DWORD),
        ('EosPacketLength', ULONG),
    ]


PKSRTAUDIO_SETWRITEPACKET_INFO = POINTER(KSRTAUDIO_SETWRITEPACKET_INFO)


# ===========================================================================

class KSPROPERTY_BTAUDIO(ENUM):
    KSPROPERTY_ONESHOT_RECONNECT = 0
    KSPROPERTY_ONESHOT_DISCONNECT = 1


# ===========================================================================

class KSPROPERTY_DRMAUDIOSTREAM(ENUM):
    KSPROPERTY_DRMAUDIOSTREAM_CONTENTID = 0


# ===========================================================================

class KSPROPERTY_SOUNDDETECTOR(ENUM):
    KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS = 1
    KSPROPERTY_SOUNDDETECTOR_PATTERNS = 2
    KSPROPERTY_SOUNDDETECTOR_ARMED = 3
    KSPROPERTY_SOUNDDETECTOR_MATCHRESULT = 4


class SOUNDDETECTOR_PATTERNHEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('PatternType', GUID),
    ]



class KSEVENT_SOUNDDETECTOR(ENUM):
    KSEVENT_SOUNDDETECTOR_MATCHDETECTED = 1


# ===========================================================================

class KSPROPERTY_AUDIO(ENUM):
    KSPROPERTY_AUDIO_LATENCY = 1
    KSPROPERTY_AUDIO_COPY_PROTECTION = 2
    KSPROPERTY_AUDIO_CHANNEL_CONFIG = 3
    KSPROPERTY_AUDIO_VOLUMELEVEL = 4
    KSPROPERTY_AUDIO_POSITION = 5
    KSPROPERTY_AUDIO_DYNAMIC_RANGE = 6
    KSPROPERTY_AUDIO_QUALITY = 7
    KSPROPERTY_AUDIO_SAMPLING_RATE = 8
    KSPROPERTY_AUDIO_DYNAMIC_SAMPLING_RATE = 9
    KSPROPERTY_AUDIO_MIX_LEVEL_TABLE = 10
    KSPROPERTY_AUDIO_MIX_LEVEL_CAPS = 11
    KSPROPERTY_AUDIO_MUX_SOURCE = 12
    KSPROPERTY_AUDIO_MUTE = 13
    KSPROPERTY_AUDIO_BASS = 14
    KSPROPERTY_AUDIO_MID = 15
    KSPROPERTY_AUDIO_TREBLE = 16
    KSPROPERTY_AUDIO_BASS_BOOST = 17
    KSPROPERTY_AUDIO_EQ_LEVEL = 18
    KSPROPERTY_AUDIO_NUM_EQ_BANDS = 19
    KSPROPERTY_AUDIO_EQ_BANDS = 20
    KSPROPERTY_AUDIO_AGC = 21
    KSPROPERTY_AUDIO_DELAY = 22
    KSPROPERTY_AUDIO_LOUDNESS = 23
    KSPROPERTY_AUDIO_WIDE_MODE = 24
    KSPROPERTY_AUDIO_WIDENESS = 25
    KSPROPERTY_AUDIO_REVERB_LEVEL = 26
    KSPROPERTY_AUDIO_CHORUS_LEVEL = 27
    KSPROPERTY_AUDIO_DEV_SPECIFIC = 28
    KSPROPERTY_AUDIO_DEMUX_DEST = 29
    KSPROPERTY_AUDIO_STEREO_ENHANCE = 30
    KSPROPERTY_AUDIO_MANUFACTURE_GUID = 31
    KSPROPERTY_AUDIO_PRODUCT_GUID = 32
    KSPROPERTY_AUDIO_CPU_RESOURCES = 33
    KSPROPERTY_AUDIO_STEREO_SPEAKER_GEOMETRY = 34
    KSPROPERTY_AUDIO_SURROUND_ENCODE = 35
    KSPROPERTY_AUDIO_3D_INTERFACE = 36
    KSPROPERTY_AUDIO_PEAKMETER = 37
    KSPROPERTY_AUDIO_ALGORITHM_INSTANCE = 38
    KSPROPERTY_AUDIO_FILTER_STATE = 39
    KSPROPERTY_AUDIO_PREFERRED_STATUS = 40
    KSPROPERTY_AUDIO_PEQ_MAX_BANDS = 42
    KSPROPERTY_AUDIO_PEQ_NUM_BANDS = 43
    KSPROPERTY_AUDIO_PEQ_BAND_CENTER_FREQ = 44
    KSPROPERTY_AUDIO_PEQ_BAND_Q_FACTOR = 45
    KSPROPERTY_AUDIO_PEQ_BAND_LEVEL = 46
    KSPROPERTY_AUDIO_CHORUS_MODULATION_RATE = 47
    KSPROPERTY_AUDIO_CHORUS_MODULATION_DEPTH = 48
    KSPROPERTY_AUDIO_REVERB_TIME = 49
    KSPROPERTY_AUDIO_REVERB_DELAY_FEEDBACK = 50
    KSPROPERTY_AUDIO_POSITIONEX = 51
    KSPROPERTY_AUDIO_MIC_ARRAY_GEOMETRY = 52
    KSPROPERTY_AUDIO_PRESENTATION_POSITION = 54
    KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_POSITION = 55
    KSPROPERTY_AUDIO_LINEAR_BUFFER_POSITION = 56
    KSPROPERTY_AUDIO_PEAKMETER2 = 57
    KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_LASTBUFFER_POSITION = 59
    KSPROPERTY_AUDIO_VOLUMELIMIT_ENGAGED = 60
    KSPROPERTY_AUDIO_MIC_SENSITIVITY = 62
    KSPROPERTY_AUDIO_MIC_SNR = 63
    KSPROPERTY_AUDIO_MIC_SENSITIVITY2 = 65


# Audio quality constants
KSAUDIO_QUALITY_WORST = 0x0
KSAUDIO_QUALITY_PC = 0x1
KSAUDIO_QUALITY_BASIC = 0x2
# Audio CPU resource constants
KSAUDIO_QUALITY_ADVANCED = 0x3
KSAUDIO_CPU_RESOURCES_NOT_HOST_CPU = 0x00000000
KSAUDIO_CPU_RESOURCES_HOST_CPU = 0x7FFFFFFF


class KSAUDIO_COPY_PROTECTION(ctypes.Structure):
    _fields_ = [
        ('fCopyrighted', BOOL),
        ('fOriginal', BOOL),
    ]


PKSAUDIO_COPY_PROTECTION = POINTER(KSAUDIO_COPY_PROTECTION)


class KSAUDIO_CHANNEL_CONFIG(ctypes.Structure):
    _fields_ = [
        ('ActiveSpeakerPositions', LONG),
    ]


PKSAUDIO_CHANNEL_CONFIG = POINTER(KSAUDIO_CHANNEL_CONFIG)

# Speaker Positions:
SPEAKER_FRONT_LEFT = 0x1
SPEAKER_FRONT_RIGHT = 0x2
SPEAKER_FRONT_CENTER = 0x4
SPEAKER_LOW_FREQUENCY = 0x8
SPEAKER_BACK_LEFT = 0x10
SPEAKER_BACK_RIGHT = 0x20
SPEAKER_FRONT_LEFT_OF_CENTER = 0x40
SPEAKER_FRONT_RIGHT_OF_CENTER = 0x80
SPEAKER_BACK_CENTER = 0x100
SPEAKER_SIDE_LEFT = 0x200
SPEAKER_SIDE_RIGHT = 0x400
SPEAKER_TOP_CENTER = 0x800
SPEAKER_TOP_FRONT_LEFT = 0x1000
SPEAKER_TOP_FRONT_CENTER = 0x2000
SPEAKER_TOP_FRONT_RIGHT = 0x4000
SPEAKER_TOP_BACK_LEFT = 0x8000
SPEAKER_TOP_BACK_CENTER = 0x10000
# Bit mask locations reserved for future use
SPEAKER_TOP_BACK_RIGHT = 0x20000
# Used to specify that any possible permutation of speaker configurations
SPEAKER_RESERVED = 0x7FFC0000
# DirectSound Speaker Config
SPEAKER_ALL = 0x80000000
KSAUDIO_SPEAKER_DIRECTOUT = 0
KSAUDIO_SPEAKER_MONO = SPEAKER_FRONT_CENTER
KSAUDIO_SPEAKER_1POINT1 = (
    SPEAKER_FRONT_CENTER |
    SPEAKER_LOW_FREQUENCY
)
KSAUDIO_SPEAKER_STEREO = SPEAKER_FRONT_LEFT | SPEAKER_FRONT_RIGHT
KSAUDIO_SPEAKER_2POINT1 = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_LOW_FREQUENCY
)
KSAUDIO_SPEAKER_3POINT0 = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER
)
KSAUDIO_SPEAKER_3POINT1 = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_LOW_FREQUENCY
)
KSAUDIO_SPEAKER_QUAD = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_BACK_LEFT |
    SPEAKER_BACK_RIGHT
)
KSAUDIO_SPEAKER_SURROUND = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_BACK_CENTER
)
KSAUDIO_SPEAKER_5POINT0 = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_SIDE_LEFT |
    SPEAKER_SIDE_RIGHT
)
KSAUDIO_SPEAKER_5POINT1 = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_LOW_FREQUENCY |
    SPEAKER_BACK_LEFT |
    SPEAKER_BACK_RIGHT
)
KSAUDIO_SPEAKER_7POINT0 = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_BACK_LEFT |
    SPEAKER_BACK_RIGHT |
    SPEAKER_SIDE_LEFT |
    SPEAKER_SIDE_RIGHT
)
KSAUDIO_SPEAKER_7POINT1 = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_LOW_FREQUENCY |
    SPEAKER_BACK_LEFT |
    SPEAKER_BACK_RIGHT |
    SPEAKER_FRONT_LEFT_OF_CENTER |
    SPEAKER_FRONT_RIGHT_OF_CENTER
)
KSAUDIO_SPEAKER_5POINT1_SURROUND = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_LOW_FREQUENCY |
    SPEAKER_SIDE_LEFT |
    SPEAKER_SIDE_RIGHT
)
KSAUDIO_SPEAKER_7POINT1_SURROUND = (
    SPEAKER_FRONT_LEFT |
    SPEAKER_FRONT_RIGHT |
    SPEAKER_FRONT_CENTER |
    SPEAKER_LOW_FREQUENCY |
    SPEAKER_BACK_LEFT |
    SPEAKER_BACK_RIGHT |
    SPEAKER_SIDE_LEFT |
    SPEAKER_SIDE_RIGHT
)
# The following are obsolete 5.1 and 7.1 settings (they lack side speakers).
# Note this means
# that the default 5.1 and 7.1 settings (KSAUDIO_SPEAKER_5POINT1 and
# KSAUDIO_SPEAKER_7POINT1 are
# similarly obsolete but are unchanged for compatibility reasons).
KSAUDIO_SPEAKER_5POINT1_BACK = KSAUDIO_SPEAKER_5POINT1
# XP SP2 and later (chronologically)
KSAUDIO_SPEAKER_7POINT1_WIDE = KSAUDIO_SPEAKER_7POINT1
# DVD Speaker Positions
KSAUDIO_SPEAKER_GROUND_FRONT_LEFT = SPEAKER_FRONT_LEFT
KSAUDIO_SPEAKER_GROUND_FRONT_CENTER = SPEAKER_FRONT_CENTER
KSAUDIO_SPEAKER_GROUND_FRONT_RIGHT = SPEAKER_FRONT_RIGHT
KSAUDIO_SPEAKER_GROUND_REAR_LEFT = SPEAKER_BACK_LEFT
KSAUDIO_SPEAKER_GROUND_REAR_RIGHT = SPEAKER_BACK_RIGHT
KSAUDIO_SPEAKER_TOP_MIDDLE = SPEAKER_TOP_CENTER
KSAUDIO_SPEAKER_SUPER_WOOFER = SPEAKER_LOW_FREQUENCY


class KSAUDIO_DYNAMIC_RANGE(ctypes.Structure):
    _fields_ = [
        ('QuietCompression', ULONG),
        ('LoudCompression', ULONG),
    ]


PKSAUDIO_DYNAMIC_RANGE = POINTER(KSAUDIO_DYNAMIC_RANGE)


class KSAUDIO_MIXLEVEL(ctypes.Structure):
    _fields_ = [
        ('Mute', BOOL),
        ('Level', LONG),
    ]


PKSAUDIO_MIXLEVEL = POINTER(KSAUDIO_MIXLEVEL)


class KSAUDIO_MIX_CAPS(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('Reset', LONG),
            ('Resolution', LONG),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('Mute', BOOL),
        ('Minimum', LONG),
        ('Maximum', LONG),
        ('_Union_0', _Union_0),
    ]


PKSAUDIO_MIX_CAPS = POINTER(KSAUDIO_MIX_CAPS)


class KSAUDIO_MIXCAP_TABLE(ctypes.Structure):
    _fields_ = [
        ('InputChannels', ULONG),
        ('OutputChannels', ULONG),
        ('Capabilities', KSAUDIO_MIX_CAPS * 1),
    ]


PKSAUDIO_MIXCAP_TABLE = POINTER(KSAUDIO_MIXCAP_TABLE)


# preferred device index
class KSPROPERTY_SYSAUDIO_DEFAULT_TYPE(ENUM):
    KSPROPERTY_SYSAUDIO_NORMAL_DEFAULT = 0
    KSPROPERTY_SYSAUDIO_PLAYBACK_DEFAULT = 1
    KSPROPERTY_SYSAUDIO_RECORD_DEFAULT = 2
    KSPROPERTY_SYSAUDIO_MIDI_DEFAULT = 3
    KSPROPERTY_SYSAUDIO_MIXER_DEFAULT = 4


# (NTDDI_VERSION < NTDDI_VISTA)

class KSAUDIO_PREFERRED_STATUS(ctypes.Structure):
    _fields_ = [
        ('Enable', BOOL),
        ('DeviceType', KSPROPERTY_SYSAUDIO_DEFAULT_TYPE),
        ('Flags', ULONG),
        ('Reserved', ULONG),
    ]


PKSAUDIO_PREFERRED_STATUS = POINTER(KSAUDIO_PREFERRED_STATUS)


# (NTDDI_VERSION >= NTDDI_WINXP and NTDDI_VERSION < NTDDI_VISTA)

class KSAUDIO_POSITIONEX(ctypes.Structure):
    _fields_ = [
        ('TimerFrequency', LARGE_INTEGER),
        ('TimeStamp1', LARGE_INTEGER),
        ('Position', KSAUDIO_POSITION),
        ('TimeStamp2', LARGE_INTEGER),
    ]


PKSAUDIO_POSITIONEX = POINTER(KSAUDIO_POSITIONEX)


# (NTDDI_VERSION >= NTDDI_VISTA)

class KSPROPERTY_TELEPHONY_CONTROL(ENUM):
    KSPROPERTY_TELEPHONY_PROVIDERID = 0
    KSPROPERTY_TELEPHONY_CALLINFO = 1
    KSPROPERTY_TELEPHONY_CALLCONTROL = 2
    KSPROPERTY_TELEPHONY_PROVIDERCHANGE = 3
    KSPROPERTY_TELEPHONY_CALLHOLD = 4
    KSPROPERTY_TELEPHONY_MUTE_TX = 5


class TELEPHONY_CALLTYPE(ENUM):
    TELEPHONY_CALLTYPE_CIRCUITSWITCHED = 0
    TELEPHONY_CALLTYPE_PACKETSWITCHED_LTE = 1
    TELEPHONY_CALLTYPE_PACKETSWITCHED_WLAN = 2


class TELEPHONY_CALLCONTROLOP(ENUM):
    TELEPHONY_CALLCONTROLOP_DISABLE = 0
    TELEPHONY_CALLCONTROLOP_ENABLE = 1


class _tagKSTELEPHONY_CALLCONTROL(ctypes.Structure):
    _fields_ = [
        ('CallType', TELEPHONY_CALLTYPE),
        ('CallControlOp', TELEPHONY_CALLCONTROLOP),
    ]


KSTELEPHONY_CALLCONTROL = _tagKSTELEPHONY_CALLCONTROL
PKSTELEPHONY_CALLCONTROL = POINTER(_tagKSTELEPHONY_CALLCONTROL)


class TELEPHONY_PROVIDERCHANGEOP(ENUM):
    TELEPHONY_PROVIDERCHANGEOP_END = 0
    TELEPHONY_PROVIDERCHANGEOP_BEGIN = 1
    TELEPHONY_PROVIDERCHANGEOP_CANCEL = 2


class _tagKSTELEPHONY_PROVIDERCHANGE(ctypes.Structure):
    _fields_ = [
        ('CallType', TELEPHONY_CALLTYPE),
        ('ProviderChangeOp', TELEPHONY_PROVIDERCHANGEOP),
    ]


KSTELEPHONY_PROVIDERCHANGE = _tagKSTELEPHONY_PROVIDERCHANGE
PKSTELEPHONY_PROVIDERCHANGE = POINTER(_tagKSTELEPHONY_PROVIDERCHANGE)


class TELEPHONY_CALLSTATE(ENUM):
    TELEPHONY_CALLSTATE_DISABLED = 0
    TELEPHONY_CALLSTATE_ENABLED = 1
    TELEPHONY_CALLSTATE_HOLD = 2
    TELEPHONY_CALLSTATE_PROVIDERTRANSITION = 3


class _tagKSTELEPHONY_CALLINFO(ctypes.Structure):
    _fields_ = [
        ('CallType', TELEPHONY_CALLTYPE),
        ('CallState', TELEPHONY_CALLSTATE),
    ]


KSTELEPHONY_CALLINFO = _tagKSTELEPHONY_CALLINFO
PKSTELEPHONY_CALLINFO = POINTER(_tagKSTELEPHONY_CALLINFO)



class KSPROPERTY_TELEPHONY_TOPOLOGY(ENUM):
    KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR = 0
    KSPROPERTY_TELEPHONY_VOLUME = 1


class _tagKSTOPOLOGY_ENDPOINTID(ctypes.Structure):
    _fields_ = [
        ('TopologyName', WCHAR * MAX_PATH),
        ('PinId', ULONG),
    ]


KSTOPOLOGY_ENDPOINTID = _tagKSTOPOLOGY_ENDPOINTID
PKSTOPOLOGY_ENDPOINTID = POINTER(_tagKSTOPOLOGY_ENDPOINTID)


# Reference string for topology filter of an endpoINT
# Topology filter pin id to which endpoINT is connected

class _tagKSTOPOLOGY_ENDPOINTIDPAIR(ctypes.Structure):
    _fields_ = [
        ('RenderEndpoINT', KSTOPOLOGY_ENDPOINTID),
        ('CaptureEndpoINT', KSTOPOLOGY_ENDPOINTID),
    ]


KSTOPOLOGY_ENDPOINTIDPAIR = _tagKSTOPOLOGY_ENDPOINTIDPAIR
PKSTOPOLOGY_ENDPOINTIDPAIR = POINTER(_tagKSTOPOLOGY_ENDPOINTIDPAIR)


class KSPROPERTY_FMRX_TOPOLOGY(ENUM):
    KSPROPERTY_FMRX_ENDPOINTID = 0
    KSPROPERTY_FMRX_VOLUME = 1
    KSPROPERTY_FMRX_ANTENNAENDPOINTID = 2



class KSPROPERTY_FMRX_CONTROL(ENUM):
    KSPROPERTY_FMRX_STATE = 0


class KSEVENT_TELEPHONY(ENUM):
    KSEVENT_TELEPHONY_ENDPOINTPAIRS_CHANGED = 0


# Internal topology node pin definitions
KSNODEPIN_STANDARD_IN = 1
# can be >= 1
KSNODEPIN_STANDARD_OUT = 0
KSNODEPIN_SUM_MUX_IN = 1
KSNODEPIN_SUM_MUX_OUT = 0
# can be >= 1
KSNODEPIN_DEMUX_IN = 0
KSNODEPIN_DEMUX_OUT = 1
KSNODEPIN_AEC_RENDER_IN = 1
KSNODEPIN_AEC_RENDER_OUT = 0
KSNODEPIN_AEC_CAPTURE_IN = 2
# (NTDDI_VERSION < NTDDI_VISTA)
KSNODEPIN_AEC_CAPTURE_OUT = 3


# ===========================================================================

class KSMETHOD_WAVETABLE(ENUM):
    KSMETHOD_WAVETABLE_WAVE_ALLOC = 0
    KSMETHOD_WAVETABLE_WAVE_FREE = 1
    KSMETHOD_WAVETABLE_WAVE_FIND = 2
    KSMETHOD_WAVETABLE_WAVE_WRITE = 3


# wave identifier

class KSWAVETABLE_WAVE_DESC(ctypes.Structure):
    _fields_ = [
        ('Identifier', KSIDENTIFIER),
        ('Size', ULONG),
        ('Looped', BOOL),
        ('LoopPoINT', ULONG),
        ('InROM', BOOL),
        ('Format', KSDATAFORMAT),
    ]


PKSWAVETABLE_WAVE_DESC = POINTER(KSWAVETABLE_WAVE_DESC)


# wave size
# wave looped flag
# wave loop poINT
# wave InROM flag
# wave format
# ===========================================================================
# ===========================================================================
# Property sets and items
# ===========================================================================
# ===========================================================================

class KSPROPERTY_AEC(ENUM):
    KSPROPERTY_AEC_NOISE_FILL_ENABLE = 0
    KSPROPERTY_AEC_STATUS = 1
    KSPROPERTY_AEC_MODE = 2


AEC_STATUS_FD_HISTORY_UNINITIALIZED = 0x0
AEC_STATUS_FD_HISTORY_CONTINUOUSLY_CONVERGED = 0x1
AEC_STATUS_FD_HISTORY_PREVIOUSLY_DIVERGED = 0x2
AEC_STATUS_FD_CURRENTLY_CONVERGED = 0x8
AEC_MODE_PASS_THROUGH = 0x0
AEC_MODE_HALF_DUPLEX = 0x1
# (NTDDI_VERSION >= NTDDI_WINXP and NTDDI_VERSION < NTDDI_VISTA)
AEC_MODE_FULL_DUPLEX = 0x2


# ===========================================================================

KSPROPERTY_WAVE_QUEUED_POSITION = 0x00000001



KSMETHOD_WAVE_QUEUED_BREAKLOOP = 0x00000001



class KSPROPERTY_WAVE(ENUM):
    KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES = 0
    KSPROPERTY_WAVE_INPUT_CAPABILITIES = 1
    KSPROPERTY_WAVE_OUTPUT_CAPABILITIES = 2
    KSPROPERTY_WAVE_BUFFER = 3
    KSPROPERTY_WAVE_FREQUENCY = 4
    KSPROPERTY_WAVE_VOLUME = 5
    KSPROPERTY_WAVE_PAN = 6


class KSWAVE_COMPATCAPS(ctypes.Structure):
    _fields_ = [
        ('ulDeviceType', ULONG),
    ]


PKSWAVE_COMPATCAPS = POINTER(KSWAVE_COMPATCAPS)


KSWAVE_COMPATCAPS_INPUT = 0x00000000
KSWAVE_COMPATCAPS_OUTPUT = 0x00000001


class KSWAVE_INPUT_CAPABILITIES(ctypes.Structure):
    _fields_ = [
        ('MaximumChannelsPerConnection', ULONG),
        ('MinimumBitsPerSample', ULONG),
        ('MaximumBitsPerSample', ULONG),
        ('MinimumSampleFrequency', ULONG),
        ('MaximumSampleFrequency', ULONG),
        ('TotalConnections', ULONG),
        ('ActiveConnections', ULONG),
    ]


PKSWAVE_INPUT_CAPABILITIES = POINTER(KSWAVE_INPUT_CAPABILITIES)


class KSWAVE_OUTPUT_CAPABILITIES(ctypes.Structure):
    _fields_ = [
        ('MaximumChannelsPerConnection', ULONG),
        ('MinimumBitsPerSample', ULONG),
        ('MaximumBitsPerSample', ULONG),
        ('MinimumSampleFrequency', ULONG),
        ('MaximumSampleFrequency', ULONG),
        ('TotalConnections', ULONG),
        ('StaticConnections', ULONG),
        ('StreamingConnections', ULONG),
        ('ActiveConnections', ULONG),
        ('ActiveStaticConnections', ULONG),
        ('ActiveStreamingConnections', ULONG),
        ('Total3DConnections', ULONG),
        ('Static3DConnections', ULONG),
        ('Streaming3DConnections', ULONG),
        ('Active3DConnections', ULONG),
        ('ActiveStatic3DConnections', ULONG),
        ('ActiveStreaming3DConnections', ULONG),
        ('TotalSampleMemory', ULONG),
        ('FreeSampleMemory', ULONG),
        ('LargestFreeContiguousSampleMemory', ULONG),
    ]


PKSWAVE_OUTPUT_CAPABILITIES = POINTER(KSWAVE_OUTPUT_CAPABILITIES)


class KSWAVE_VOLUME(ctypes.Structure):
    _fields_ = [
        ('LeftAttenuation', LONG),
        ('RightAttenuation', LONG),
    ]


PKSWAVE_VOLUME = POINTER(KSWAVE_VOLUME)


KSWAVE_BUFFER_ATTRIBUTEF_LOOPING = 0x00000001
KSWAVE_BUFFER_ATTRIBUTEF_STATIC = 0x00000002



class KSWAVE_BUFFER(ctypes.Structure):
    _fields_ = [
        ('Attributes', ULONG),
        ('BufferSize', ULONG),
        ('BufferAddress', PVOID),
    ]


PKSWAVE_BUFFER = POINTER(KSWAVE_BUFFER)


# ===========================================================================






class KSPROPERTY_WAVETABLE(ENUM):
    KSPROPERTY_WAVETABLE_LOAD_SAMPLE = 0
    KSPROPERTY_WAVETABLE_UNLOAD_SAMPLE = 1
    KSPROPERTY_WAVETABLE_MEMORY = 2
    KSPROPERTY_WAVETABLE_VERSION = 3


# (NTDDI_VERSION < NTDDI_WS03)

class KSDATARANGE_MUSIC(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('Technology', GUID),
        ('Channels', ULONG),
        ('Notes', ULONG),
        ('ChannelMask', ULONG),
    ]


PKSDATARANGE_MUSIC = POINTER(KSDATARANGE_MUSIC)


# ===========================================================================

class KSEVENT_CYCLIC_TIME(ENUM):
    KSEVENT_CYCLIC_TIME_INTERVAL = 0



class KSPROPERTY_CYCLIC(ENUM):
    KSPROPERTY_CYCLIC_POSITION = 0


# ===========================================================================

class KSEVENT_AUDIO_CONTROL_CHANGE(ENUM):
    KSEVENT_CONTROL_CHANGE = 0


# ===========================================================================

class KSEVENT_LOOPEDSTREAMING(ENUM):
    KSEVENT_LOOPEDSTREAMING_POSITION = 0



class LOOPEDSTREAMING_POSITION_EVENT_DATA(ctypes.Structure):
    _fields_ = [
        ('KsEventData', KSEVENTDATA),
        ('Position', ULONGLONG),
        ('Position', DWORDLONG),
    ]


PLOOPEDSTREAMING_POSITION_EVENT_DATA = POINTER(
    LOOPEDSTREAMING_POSITION_EVENT_DATA
)



class KSEVENT_SYSAUDIO(ENUM):
    KSEVENT_SYSAUDIO_ADDREMOVE_DEVICE = 0
    KSEVENT_SYSAUDIO_CHANGE_DEVICE = 1


# ===========================================================================

class KSPROPERTY_SYSAUDIO(ENUM):
    KSPROPERTY_SYSAUDIO_DEVICE_COUNT = 1
    KSPROPERTY_SYSAUDIO_DEVICE_FRIENDLY_NAME = 2
    KSPROPERTY_SYSAUDIO_DEVICE_INSTANCE = 3
    KSPROPERTY_SYSAUDIO_DEVICE_INTERFACE_NAME = 4
    KSPROPERTY_SYSAUDIO_SELECT_GRAPH = 5
    KSPROPERTY_SYSAUDIO_CREATE_VIRTUAL_SOURCE = 6
    KSPROPERTY_SYSAUDIO_DEVICE_DEFAULT = 7
    KSPROPERTY_SYSAUDIO_ALWAYS_CREATE_VIRTUAL_SOURCE = 8
    KSPROPERTY_SYSAUDIO_ADDREMOVE_LOCK = 9
    KSPROPERTY_SYSAUDIO_ADDREMOVE_UNLOCK = 10
    KSPROPERTY_SYSAUDIO_RENDER_PIN_INSTANCES = 11
    KSPROPERTY_SYSAUDIO_RENDER_CONNECTION_INDEX = 12
    KSPROPERTY_SYSAUDIO_CREATE_VIRTUAL_SOURCE_ONLY = 13
    KSPROPERTY_SYSAUDIO_INSTANCE_INFO = 14
    KSPROPERTY_SYSAUDIO_PREFERRED_DEVICE = 15



class SYSAUDIO_CREATE_VIRTUAL_SOURCE(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('PinCategory', GUID),
        ('PinName', GUID),
    ]


PSYSAUDIO_CREATE_VIRTUAL_SOURCE = POINTER(SYSAUDIO_CREATE_VIRTUAL_SOURCE)


class SYSAUDIO_SELECT_GRAPH(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('PinId', ULONG),
        ('NodeId', ULONG),
        ('Flags', ULONG),
        ('Reserved', ULONG),
    ]


PSYSAUDIO_SELECT_GRAPH = POINTER(SYSAUDIO_SELECT_GRAPH)


class SYSAUDIO_INSTANCE_INFO(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Flags', ULONG),
        ('DeviceNumber', ULONG),
    ]


PSYSAUDIO_INSTANCE_INFO = POINTER(SYSAUDIO_INSTANCE_INFO)


SYSAUDIO_FLAGS_DONT_COMBINE_PINS = 0x00000001


class SYSAUDIO_PREFERRED_DEVICE(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Flags', ULONG),
        ('Index', ULONG),
    ]


PSYSAUDIO_PREFERRED_DEVICE = POINTER(SYSAUDIO_PREFERRED_DEVICE)


# KSPROPERTY_SYSAUDIO_DEFAULT_TYPE
SYSAUDIO_FLAGS_CLEAR_PREFERRED = 0x00000002



class KSPROPERTY_SYSAUDIO_PIN(ENUM):
    KSPROPERTY_SYSAUDIO_TOPOLOGY_CONNECTION_INDEX = 0
    KSPROPERTY_SYSAUDIO_ATTACH_VIRTUAL_SOURCE = 1
    KSPROPERTY_SYSAUDIO_PIN_VOLUME_NODE = 2


class SYSAUDIO_ATTACH_VIRTUAL_SOURCE(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('MixerPinId', ULONG),
        ('Reserved', ULONG),
    ]


PSYSAUDIO_ATTACH_VIRTUAL_SOURCE = POINTER(SYSAUDIO_ATTACH_VIRTUAL_SOURCE)


# ===========================================================================

class KSNODEPROPERTY(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NodeId', ULONG),
        ('Reserved', ULONG),
    ]


PKSNODEPROPERTY = POINTER(KSNODEPROPERTY)


class KSNODEPROPERTY_AUDIO_CHANNEL(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSNODEPROPERTY),
        ('Channel', LONG),
        ('Reserved', ULONG),
    ]


PKSNODEPROPERTY_AUDIO_CHANNEL = POINTER(KSNODEPROPERTY_AUDIO_CHANNEL)


class KSNODEPROPERTY_AUDIO_DEV_SPECIFIC(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSNODEPROPERTY),
        ('DevSpecificId', ULONG),
        ('DeviceInfo', ULONG),
        ('Length', ULONG),
    ]


PKSNODEPROPERTY_AUDIO_DEV_SPECIFIC = POINTER(KSNODEPROPERTY_AUDIO_DEV_SPECIFIC)


class KSNODEPROPERTY_AUDIO_3D_LISTENER(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSNODEPROPERTY),
        ('ListenerId', PVOID),
        ('Reserved', ULONG),
    ]


PKSNODEPROPERTY_AUDIO_3D_LISTENER = POINTER(KSNODEPROPERTY_AUDIO_3D_LISTENER)


class KSNODEPROPERTY_AUDIO_PROPERTY(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSNODEPROPERTY),
        ('AppContext', PVOID),
        ('Length', ULONG),
        ('Reserved', ULONG),
    ]


PKSNODEPROPERTY_AUDIO_PROPERTY = POINTER(KSNODEPROPERTY_AUDIO_PROPERTY)


# ===========================================================================
# {79A9312E-59AE-43b0-A350-8B05284CAB24}

class KSPROPERTY_AUDIOGFX(ENUM):
    KSPROPERTY_AUDIOGFX_RENDERTARGETDEVICEID = 0
    KSPROPERTY_AUDIOGFX_CAPTURETARGETDEVICEID = 1


# ===========================================================================

class KSPROPERTY_LINEAR(ENUM):
    KSPROPERTY_LINEAR_POSITION = 0


# ===========================================================================
# Midi definitions
# see DMusicKS.h
# WARNING! This structure MUST be dword aligned
# regardless of the number of data bytes.
# Delta Milliseconds from the previous midiformat


class KSMUSICFORMAT(ctypes.Structure):
    _fields_ = [
        ('TimeDeltaMs', ULONG),
        ('ByteCount', ULONG),
    ]


PKSMUSICFORMAT = POINTER(KSMUSICFORMAT)


# in the packet. The first midiformat in the packet
# is a delta from the PTS in the KSSTREAM_HEADER.
# Number of bytes of data that follow this struct.

# This entire set of MPEG Standard/Dialect Guids are obsolete. Do not use them.

# =============================================================================
# ============================================================================
# The following official MPEG Formats, Subtypes and Specifiers are listed as
# required or optional
# These official MPEG GUIDs are the preferred method of supporting MPEG/AC-3
# media types in new code.
# Older MPEG GUIDs should also be supported for compatibilty, but these new
# modes are still required.
# ============================================================================
# ============================================================================
# This is a summary of what media types/specifiers will be required for all
# DVD+DSS+DVB+DTV MPEG decoders.
# These media types are what the decoder driver must accept, hardware support
# for all of these media types
# may or may not actually be provided by the decoder natively.  These media
# types are INTended to define
# the "officially" supported MPEG/AC-3 media types that all WHQL certified
# decoders must implement.  This
# specifically includes driver and/or hardware support for all the required
# standards and dialects.
# All MPEG video decoders must support all of the MPEG video modes shown as
# [required] below.
# All MPEG audio decoders must support all of the MPEG audio modes shown as
# [required] below.
# All AC-3 audio decoders must support all of the AC-3 audio modes shown as
# [required] below.
# The line items shown as [optional] need not be implemented, but are possible
# formats that might be implemented.
# Note that the input/output pin formats are defined by 2 or 3 GUIDs: TYPE,
# SUBTYPE, and maybe SPECIFIER.
# The specifiers are included if the data format is a "dialect" that needs to
# be differentiated during decoding.
# The decoder MUST be prepared to deal with ALL requests for _required_
# "Standard" formats OR _required_ "Dialects".
# STATIC_KSDATAFORMAT_TYPE_STANDARD_ELEMENTARY_STREAM         [required]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO           [optional]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO           [optional]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO           [required]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO           [optional]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO              [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO             [optional]
# STATIC_KSDATAFORMAT_TYPE_STANDARD_PES_PACKET                [required]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO            [optional]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO           [optional]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO            [optional]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO           [optional]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO           [required]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO           [required]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO              [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO             [optional]
# STATIC_KSDATAFORMAT_TYPE_STANDARD_PACK_HEADER               [required]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO           [required]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO            [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO           [optional]
# STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO              [required]
# STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO             [optional]
# Note that the SPECIFIER GUIDs normally identify particular versions of MPEG
# such as DSS and DVD.
# This approach was taken to minimize the number of DSS/DVB/DVD/DTV etc. media
# SUBTYPES.
# These specifiers are currently required to disambiguate MPEG syntax
# _parsing_ by the decoder
# using alternate parsing routines or downloadable firmware or hardware decode
# settings.
# In the future these specifiers will be extended to cover new KS MPEG flavors
# such as DVB and DTV.
# Thus, the optional specifiers will be subject to clarification and/or
# definition as they are needed.
# Important note: Per the ITU MPEG specs, MPEG 2 media may contain pure MPEG 1
# syntax and
# any "MPEG 2" PES packets may actually contain MPEG 1 payloads and MPEG 1
# syntax.  Some MPEG
# broadcasts can revert from MPEG2 to MPEG1 format data at their discretion,
# without warning.
# CAUTION: Decoders MUST attempt to process MPEG data AS SOON AS POSSIBLE
# after reception.
# In particular, elementary MPEG or MPEG PES packet streams should not be
# aggregated INTo DVD
# "pack headers" INTernally before submission to the codec hardware if AT ALL
# POSSIBLE.  The
# reason is that mpeg data may need to be processed immediately but there may
# be no additional
# MPEG data forthcoming to fill up the PES packet OR DVD "pack" in a timely
# fashion.  This is
# particularly true of MPEG dialects that utilize "repeat field signally" to
# reuse the last
# decoded MPEG video field.

# End of obsolete MPEG definitions.

# available output modes of decoder
# current mode of the decoder
class KSPROPERTY_MPEG2VID(ENUM):
    KSPROPERTY_MPEG2VID_MODES = 0
    KSPROPERTY_MPEG2VID_CUR_MODE = 1
    KSPROPERTY_MPEG2VID_4_3_RECT = 2
    KSPROPERTY_MPEG2VID_16_9_RECT = 3
    KSPROPERTY_MPEG2VID_16_9_PANSCAN = 4


# output coordinates for 4:3 source
# output coordinates for 16:9 source
# pan and scan vectors

# bit field definitions for MPEG2 VIDEO mode

KSMPEGVIDMODE_PANSCAN = 0x0001
KSMPEGVIDMODE_LTRBOX = 0x0002

KSMPEGVIDMODE_SCALE = 0x0004
# rectangle definitions for the 4/3 and 16/9 cropping properties of
# the MPEG2Video decoder


class _KSMPEGVID_RECT(ctypes.Structure):
    _fields_ = [
        ('StartX', ULONG),
        ('StartY', ULONG),
        ('EndX', ULONG),
        ('EndY', ULONG),
    ]


KSMPEGVID_RECT = _KSMPEGVID_RECT
PKSMPEGVID_RECT = POINTER(_KSMPEGVID_RECT)


class KSPROPERTY_AC3(ENUM):
    KSPROPERTY_AC3_ERROR_CONCEALMENT = 1
    KSPROPERTY_AC3_ALTERNATE_AUDIO = 2
    KSPROPERTY_AC3_DOWNMIX = 3
    KSPROPERTY_AC3_BIT_STREAM_MODE = 4
    KSPROPERTY_AC3_DIALOGUE_LEVEL = 5
    KSPROPERTY_AC3_LANGUAGE_CODE = 6
    KSPROPERTY_AC3_ROOM_TYPE = 7


class KSAC3_ERROR_CONCEALMENT(ctypes.Structure):
    _fields_ = [
        ('fRepeatPreviousBlock', BOOL),
        ('fErrorInCurrentBlock', BOOL),
    ]


PKSAC3_ERROR_CONCEALMENT = POINTER(KSAC3_ERROR_CONCEALMENT)


class KSAC3_ALTERNATE_AUDIO(ctypes.Structure):
    _fields_ = [
        ('fStereo', BOOL),
        ('DualMode', ULONG),
    ]


PKSAC3_ALTERNATE_AUDIO = POINTER(KSAC3_ALTERNATE_AUDIO)


KSAC3_ALTERNATE_AUDIO_1 = 1
KSAC3_ALTERNATE_AUDIO_2 = 2
KSAC3_ALTERNATE_AUDIO_BOTH = 3


class KSAC3_DOWNMIX(ctypes.Structure):
    _fields_ = [
        ('fDownMix', BOOL),
        ('fDolbySurround', BOOL),
    ]


PKSAC3_DOWNMIX = POINTER(KSAC3_DOWNMIX)


class KSAC3_BIT_STREAM_MODE(ctypes.Structure):
    _fields_ = [
        ('BitStreamMode', LONG),
    ]


PKSAC3_BIT_STREAM_MODE = POINTER(KSAC3_BIT_STREAM_MODE)


KSAC3_SERVICE_MAIN_AUDIO = 0
KSAC3_SERVICE_NO_DIALOG = 1
KSAC3_SERVICE_VISUALLY_IMPAIRED = 2
KSAC3_SERVICE_HEARING_IMPAIRED = 3
KSAC3_SERVICE_DIALOG_ONLY = 4
KSAC3_SERVICE_COMMENTARY = 5
KSAC3_SERVICE_EMERGENCY_FLASH = 6
KSAC3_SERVICE_VOICE_OVER = 7


class KSAC3_DIALOGUE_LEVEL(ctypes.Structure):
    _fields_ = [
        ('DialogueLevel', ULONG),
    ]


PKSAC3_DIALOGUE_LEVEL = POINTER(KSAC3_DIALOGUE_LEVEL)


class KSAC3_ROOM_TYPE(ctypes.Structure):
    _fields_ = [
        ('fLargeRoom', BOOL),
    ]


PKSAC3_ROOM_TYPE = POINTER(KSAC3_ROOM_TYPE)


# available output modes of decoder
# current mode of the decoder
class KSPROPERTY_AUDDECOUT(ENUM):
    KSPROPERTY_AUDDECOUT_MODES = 0
    KSPROPERTY_AUDDECOUT_CUR_MODE = 1


KSAUDDECOUTMODE_STEREO_ANALOG = 0x0001
KSAUDDECOUTMODE_PCM_51 = 0x0002
KSAUDDECOUTMODE_SPDIFF = 0x0004


# subpicture definition
class KSPROPERTY_DVDSUBPIC(ENUM):
    KSPROPERTY_DVDSUBPIC_PALETTE = 0
    KSPROPERTY_DVDSUBPIC_HLI = 1
    KSPROPERTY_DVDSUBPIC_COMPOSIT_ON = 2


class _KS_DVD_YCrCb(ctypes.Structure):
    _fields_ = [
        ('Reserved', UCHAR),
        ('Y', UCHAR),
        ('Cr', UCHAR),
        ('Cb', UCHAR),
    ]


KS_DVD_YCrCb = _KS_DVD_YCrCb
PKS_DVD_YCrCb = POINTER(_KS_DVD_YCrCb)


# The KS_DVD_YUV structure is now superseded by KS_DVD_YCrCb above and is
# here for backward compatibility only

class _KS_DVD_YUV(ctypes.Structure):
    _fields_ = [
        ('Reserved', UCHAR),
        ('Y', UCHAR),
        ('V', UCHAR),
        ('U', UCHAR),
    ]


KS_DVD_YUV = _KS_DVD_YUV
PKS_DVD_YUV = POINTER(_KS_DVD_YUV)


class _KSPROPERTY_SPPAL(ctypes.Structure):
    _fields_ = [
        ('sppal', KS_DVD_YUV * 16),
    ]


KSPROPERTY_SPPAL = _KSPROPERTY_SPPAL
PKSPROPERTY_SPPAL = POINTER(_KSPROPERTY_SPPAL)


class _KS_COLCON(ctypes.Structure):
    _fields_ = [
        ('emph1col:4', UCHAR),
        ('emph2col:4', UCHAR),
        ('backcol:4', UCHAR),
        ('patcol:4', UCHAR),
        ('emph1con:4', UCHAR),
        ('emph2con:4', UCHAR),
        ('backcon:4', UCHAR),
        ('patcon:4', UCHAR),
    ]


KS_COLCON = _KS_COLCON
PKS_COLCON = POINTER(_KS_COLCON)


class _KSPROPERTY_SPHLI(ctypes.Structure):
    _fields_ = [
        ('HLISS', USHORT),
        ('Reserved', USHORT),
        ('StartPTM', ULONG),
        ('EndPTM', ULONG),
        ('StartX', USHORT),
        ('StartY', USHORT),
        ('StopX', USHORT),
        ('StopY', USHORT),
        ('ColCon', KS_COLCON),
    ]


KSPROPERTY_SPHLI = _KSPROPERTY_SPHLI
PKSPROPERTY_SPHLI = POINTER(_KSPROPERTY_SPHLI)


# start presentation time in x/90000
# end PTM in x/90000
# color contrast description (4 bytes as given in HLI)
KSPROPERTY_COMPOSIT_ON = BOOL
PKSPROPERTY_COMPOSIT_ON = POINTER(BOOL)


class KSPROPERTY_COPYPROT(ENUM):
    KSPROPERTY_DVDCOPY_CHLG_KEY = 0x01
    KSPROPERTY_DVDCOPY_DVD_KEY1 = 2
    KSPROPERTY_DVDCOPY_DEC_KEY2 = 3
    KSPROPERTY_DVDCOPY_TITLE_KEY = 4
    KSPROPERTY_COPY_MACROVISION = 5
    KSPROPERTY_DVDCOPY_REGION = 6
    KSPROPERTY_DVDCOPY_SET_COPY_STATE = 7
    KSPROPERTY_DVDCOPY_DISC_KEY = 0x80


class _KS_DVDCOPY_CHLGKEY(ctypes.Structure):
    _fields_ = [
        ('ChlgKey', BYTE * 10),
        ('Reserved', BYTE * 2),
    ]


KS_DVDCOPY_CHLGKEY = _KS_DVDCOPY_CHLGKEY
PKS_DVDCOPY_CHLGKEY = POINTER(_KS_DVDCOPY_CHLGKEY)


class _KS_DVDCOPY_BUSKEY(ctypes.Structure):
    _fields_ = [
        ('BusKey', BYTE * 5),
        ('Reserved', BYTE * 1),
    ]


KS_DVDCOPY_BUSKEY = _KS_DVDCOPY_BUSKEY
PKS_DVDCOPY_BUSKEY = POINTER(_KS_DVDCOPY_BUSKEY)


class _KS_DVDCOPY_DISCKEY(ctypes.Structure):
    _fields_ = [
        ('DiscKey', BYTE * 2048),
    ]


KS_DVDCOPY_DISCKEY = _KS_DVDCOPY_DISCKEY
PKS_DVDCOPY_DISCKEY = POINTER(_KS_DVDCOPY_DISCKEY)


class _KS_DVDCOPY_REGION(ctypes.Structure):
    _fields_ = [
        ('Reserved', UCHAR),
        ('RegionData', UCHAR),
        ('Reserved2', UCHAR * 2),
    ]


KS_DVDCOPY_REGION = _KS_DVDCOPY_REGION
PKS_DVDCOPY_REGION = POINTER(_KS_DVDCOPY_REGION)


class _KS_DVDCOPY_TITLEKEY(ctypes.Structure):
    _fields_ = [
        ('KeyFlags', ULONG),
        ('ReservedNT', ULONG * 2),
        ('TitleKey', UCHAR * 6),
        ('Reserved', UCHAR * 2),
    ]


KS_DVDCOPY_TITLEKEY = _KS_DVDCOPY_TITLEKEY
PKS_DVDCOPY_TITLEKEY = POINTER(_KS_DVDCOPY_TITLEKEY)


class _KS_COPY_MACROVISION(ctypes.Structure):
    _fields_ = [
        ('MACROVISIONLevel', ULONG),
    ]


KS_COPY_MACROVISION = _KS_COPY_MACROVISION
PKS_COPY_MACROVISION = POINTER(_KS_COPY_MACROVISION)


class _KS_DVDCOPY_SET_COPY_STATE(ctypes.Structure):
    _fields_ = [
        ('DVDCopyState', ULONG),
    ]


KS_DVDCOPY_SET_COPY_STATE = _KS_DVDCOPY_SET_COPY_STATE
PKS_DVDCOPY_SET_COPY_STATE = POINTER(_KS_DVDCOPY_SET_COPY_STATE)


# indicates we are starting a full
# copy protection sequence.
class KS_DVDCOPYSTATE(ENUM):
    KS_DVDCOPYSTATE_INITIALIZE = 0
    KS_DVDCOPYSTATE_INITIALIZE_TITLE = 1
    KS_DVDCOPYSTATE_AUTHENTICATION_NOT_REQUIRED = 2
    KS_DVDCOPYSTATE_AUTHENTICATION_REQUIRED = 3
    KS_DVDCOPYSTATE_DONE = 4


# indicates we are starting a title
# key copy protection sequence
class KS_COPY_MACROVISION_LEVEL(ENUM):
    KS_MACROVISION_DISABLED = 0
    KS_MACROVISION_LEVEL1 = 1
    KS_MACROVISION_LEVEL2 = 2
    KS_MACROVISION_LEVEL3 = 3


PKS_COPY_MACROVISION_LEVEL = POINTER(KS_COPY_MACROVISION_LEVEL)

# CGMS Copy Protection Flags
KS_DVD_CGMS_RESERVED_MASK = 0x00000078
KS_DVD_CGMS_COPY_PROTECT_MASK = 0x00000018
KS_DVD_CGMS_COPY_PERMITTED = 0x00000000
KS_DVD_CGMS_COPY_ONCE = 0x00000010
KS_DVD_CGMS_NO_COPY = 0x00000018
KS_DVD_COPYRIGHT_MASK = 0x00000040
KS_DVD_NOT_COPYRIGHTED = 0x00000000
KS_DVD_COPYRIGHTED = 0x00000040
KS_DVD_SECTOR_PROTECT_MASK = 0x00000020
KS_DVD_SECTOR_NOT_PROTECTED = 0x00000000
KS_DVD_SECTOR_PROTECTED = 0x00000020

# constants for the biCompression field
KS_BI_RGB = 0
KS_BI_RLE8 = 1
KS_BI_RLE4 = 2
KS_BI_BITFIELDS = 3
KS_BI_JPEG = 4


class tagKS_RGBQUAD(ctypes.Structure):
    _fields_ = [
        ('rgbBlue', BYTE),
        ('rgbGreen', BYTE),
        ('rgbRed', BYTE),
        ('rgbReserved', BYTE),
    ]


KS_RGBQUAD = tagKS_RGBQUAD
PKS_RGBQUAD = POINTER(tagKS_RGBQUAD)


# constants for palettes
# Maximum colours in palette
# Number colours in EGA palette
# Maximum three components
KS_iPALETTE_COLORS = 0x100
# Minimum true colour device
KS_iEGA_COLORS = 0x10
# Index position for RED mask
KS_iMASK_COLORS = 0x3
# Index position for GREEN mask
KS_iTRUECOLOR = 0x10
# Index position for BLUE mask
KS_iRED = 0x0
# Maximum colour depth using a palette
KS_iGREEN = 0x1
# Maximum bits per colour component
KS_iBLUE = 0x2
KS_iPALETTE = 0x8
KS_iMAXBITS = 0x8
KS_SIZE_EGA_PALETTE = KS_iEGA_COLORS * ctypes.sizeof(KS_RGBQUAD)
KS_SIZE_PALETTE = KS_iPALETTE_COLORS * ctypes.sizeof(KS_RGBQUAD)


class tagKS_BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', DWORD),
        ('biWidth', LONG),
        ('biHeight', LONG),
        ('biPlanes', WORD),
        ('biBitCount', WORD),
        ('biCompression', DWORD),
        ('biSizeImage', DWORD),
        ('biXPelsPerMeter', LONG),
        ('biYPelsPerMeter', LONG),
        ('biClrUsed', DWORD),
        ('biClrImportant', DWORD),
    ]


KS_BITMAPINFOHEADER = tagKS_BITMAPINFOHEADER
PKS_BITMAPINFOHEADER = POINTER(tagKS_BITMAPINFOHEADER)


# Used for true colour images that also have a palette
class tag_KS_TRUECOLORINFO(ctypes.Structure):
    _fields_ = [
        ('dwBitMasks', DWORD * KS_iMASK_COLORS),
        ('bmiColors', KS_RGBQUAD * KS_iPALETTE_COLORS),
    ]


KS_TRUECOLORINFO = tag_KS_TRUECOLORINFO
PKS_TRUECOLORINFO = POINTER(tag_KS_TRUECOLORINFO)


def KS_WIDTHBYTES(bits):
    return ((bits + 31) & ~31) / 8


def KS_DIBWIDTHBYTES(bi):
    return KS_WIDTHBYTES(bi.biWidth * bi.biBitCount)


def KS__DIBSIZE(bi):
    return KS_DIBWIDTHBYTES(bi) * bi.biHeight


def KS_DIBSIZE(bi):
    if bi.biHeight < 0:
        return -1 * KS__DIBSIZE(bi)
    else:
        return KS__DIBSIZE(bi)


# The BITMAPINFOHEADER contains all the details about the video stream such
# as the actual image dimensions and their pixel depth. A source filter may
# also request that the sink take only a section of the video by providing a
# clipping rectangle in rcSource. In the worst case where the sink filter
# forgets to check this on connection it will simply render the whole thing
# which isn't a disaster. Ideally a sink filter will check the rcSource and
# if it doesn't support image extraction and the rectangle is not empty then
# it will reject the connection. A filter should use SetRectEmpty to reset a
# rectangle to all zeroes (and IsRectEmpty to later check the rectangle).
# The rcTarget specifies the destination rectangle for the video, for most
# source filters they will set this to all zeroes, a downstream filter may
# request that the video be placed in a particular area of the buffers it
# supplies in which case it will call QueryAccept with a non empty target
class tagKS_VIDEOINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('rcSource', RECT),
        ('rcTarget', RECT),
        ('dwBitRate', DWORD),
        ('dwBitErrorRate', DWORD),
        ('AvgTimePerFrame', REFERENCE_TIME),
        ('bmiHeader', KS_BITMAPINFOHEADER),
    ]


KS_VIDEOINFOHEADER = tagKS_VIDEOINFOHEADER
PKS_VIDEOINFOHEADER = POINTER(tagKS_VIDEOINFOHEADER)


# The bit we really want to use
# Where the video should go
# Approximate bit data rate
# Bit error rate for this stream
# Average time per frame (100ns units)
# !!! WARNING !!!
# DO NOT use the following structure unless you are sure that the
# BITMAPINFOHEADER
# has a normal biSize == ctypes.sizeof(BITMAPINFOHEADER) !
# !!! WARNING !!!
class tagKS_VIDEOINFO(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('bmiColors', KS_RGBQUAD * KS_iPALETTE_COLORS),
            ('dwBitMasks', DWORD * KS_iMASK_COLORS),
            ('TrueColorInfo', KS_TRUECOLORINFO),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('rcSource', RECT),
        ('rcTarget', RECT),
        ('dwBitRate', DWORD),
        ('dwBitErrorRate', DWORD),
        ('AvgTimePerFrame', REFERENCE_TIME),
        ('bmiHeader', KS_BITMAPINFOHEADER),
        ('_Union_0', _Union_0),
    ]


KS_VIDEOINFO = tagKS_VIDEOINFO
PKS_VIDEOINFO = POINTER(tagKS_VIDEOINFO)


# The bit we really want to use
# Where the video should go
# Approximate bit data rate
# Bit error rate for this stream
# Average time per frame (100ns units)
# Colour palette
# True colour masks
# Both of the above
KS_SIZE_MASKS = KS_iMASK_COLORS * ctypes.sizeof(DWORD)
# For normal size
# KS_SIZE_PREHEADER = FIELD_OFFSET(KS_VIDEOINFOHEADER, KS_BITMAPINFOHEADER)
# #define KS_SIZE_VIDEOHEADER (ctypes.sizeof(KS_BITMAPINFOHEADER) +
# KS_SIZE_PREHEADER)
# !!! for abnormal biSizes

KS_SIZE_PREHEADER = 0


def KS_SIZE_VIDEOHEADER(pbmi):
    return pbmi.bmiHeader.biSize + KS_SIZE_PREHEADER
# VBI
# Used for NABTS, CC, Intercast, WST
# inclusive


class tagKS_VBIINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('StartLine', ULONG),
        ('EndLine', ULONG),
        ('SamplingFrequency', ULONG),
        ('MinLineStartTime', ULONG),
        ('MaxLineStartTime', ULONG),
        ('ActualLineStartTime', ULONG),
        ('ActualLineEndTime', ULONG),
        ('VideoStandard', ULONG),
        ('SamplesPerLine', ULONG),
        ('StrideInBytes', ULONG),
        ('BufferSize', ULONG),
    ]


KS_VBIINFOHEADER = tagKS_VBIINFOHEADER
PKS_VBIINFOHEADER = POINTER(tagKS_VBIINFOHEADER)


# inclusive
# Hz.
# microSec * 100 from HSync LE
# microSec * 100 from HSync LE
# microSec * 100 from HSync LE
# microSec * 100 from HSync LE
# KS_AnalogVideoStandard*
# May be > SamplesPerLine
# Bytes
# VBI Sampling Rates
# ~= 1/1.986125e-6
KS_VBIDATARATE_NABTS = 5727272
KS_VBIDATARATE_CC = 503493
KS_VBISAMPLINGRATE_4X_NABTS = 4 * KS_VBIDATARATE_NABTS
KS_VBISAMPLINGRATE_47X_NABTS = 27000000
KS_VBISAMPLINGRATE_5X_NABTS = 5 * KS_VBIDATARATE_NABTS
KS_47NABTS_SCALER = KS_VBISAMPLINGRATE_47X_NABTS / KS_VBIDATARATE_NABTS
# Analog video variant - Use this when the format is FORMAT_AnalogVideo

# rcSource defines the portion of the active video signal to use
# rcTarget defines the destination rectangle
# both of the above are relative to the dwActiveWidth and dwActiveHeight fields
# dwActiveWidth is currently set to 720 for all formats (but could change for
# HDTV)
# dwActiveHeight is 483 for NTSC and 575 for PAL/SECAM  (but could change for
# HDTV)
# Width max is 720, height varies w/ TransmissionStd


class tagKS_AnalogVideoInfo(ctypes.Structure):
    _fields_ = [
        ('rcSource', RECT),
        ('rcTarget', RECT),
        ('dwActiveWidth', DWORD),
        ('dwActiveHeight', DWORD),
        ('AvgTimePerFrame', REFERENCE_TIME),
    ]


KS_ANALOGVIDEOINFO = tagKS_AnalogVideoInfo
PKS_ANALOGVIDEOINFO = POINTER(tagKS_AnalogVideoInfo)


# Where the video should go
# Always 720 (CCIR-601 active samples per line)
# 483 for NTSC, 575 for PAL/SECAM
# Normal ActiveMovie units (100 nS)
# ===========================================================================
# Data packet passed on Analog video stream channel change
# ===========================================================================
# Starting a tuning operation
# Ending a tuning operation
KS_TVTUNER_CHANGE_BEGIN_TUNE = 0x0001
KS_TVTUNER_CHANGE_END_TUNE = 0x0002


class tagKS_TVTUNER_CHANGE_INFO(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('dwCountryCode', DWORD),
        ('dwAnalogVideoStandard', DWORD),
        ('dwChannel', DWORD),
    ]


KS_TVTUNER_CHANGE_INFO = tagKS_TVTUNER_CHANGE_INFO
PKS_TVTUNER_CHANGE_INFO = POINTER(tagKS_TVTUNER_CHANGE_INFO)


# KS_AnalogVideoStandard
# ===========================================================================
# Video format blocks
# ===========================================================================
class KS_MPEG2Level(ENUM):
    KS_MPEG2Level_Low = 0
    KS_MPEG2Level_Main = 1
    KS_MPEG2Level_High1440 = 2
    KS_MPEG2Level_High = 3


class KS_MPEG2Profile(ENUM):
    KS_MPEG2Profile_Simple = 0
    KS_MPEG2Profile_Main = 1
    KS_MPEG2Profile_SNRScalable = 2
    KS_MPEG2Profile_SpatiallyScalable = 3
    KS_MPEG2Profile_High = 4


# if 0, other INTerlace bits are irrelevent
# else 2 fields per media sample
# else Field 2 is first;  top field in PAL is field 1, top field in NTSC is
# field 2?
KS_INTERLACE_IsInterlaced = 0x00000001

KS_INTERLACE_1FieldPerSample = 0x00000002
# use this mask with AMINTERLACE_FieldPat*
KS_INTERLACE_Field1First = 0x00000004
# Data never contains a Field2
KS_INTERLACE_UNUSED = 0x00000008
# Data never contains a Field1
KS_INTERLACE_FieldPatternMask = 0x00000030
# There will be a Field2 for every Field1 (required for Weave?)
KS_INTERLACE_FieldPatField1Only = 0x00000000
# Random pattern of Field1s and Field2s
KS_INTERLACE_FieldPatField2Only = 0x00000010
KS_INTERLACE_FieldPatBothRegular = 0x00000020
KS_INTERLACE_FieldPatBothIrregular = 0x00000030
KS_INTERLACE_DisplayModeMask = 0x000000c0
KS_INTERLACE_DisplayModeBobOnly = 0x00000000
KS_INTERLACE_DisplayModeWeaveOnly = 0x00000040
# duplication of this stream should be restricted
KS_INTERLACE_DisplayModeBobOrWeave = 0x00000080
# if set, the MPEG-2 video decoder should crop output image
KS_COPYPROTECT_RestrictDuplication = 0x00000001
# based on pan-scan vectors in picture_display_extension
# and change the picture aspect ratio accordingly.
KS_MPEG2_DoPanScan = 0x00000001
# if set, the MPEG-2 decoder must be able to produce an output
# pin for DVD style closed caption data found in GOP layer of field 1
# if set, the MPEG-2 decoder must be able to produce an output
KS_MPEG2_DVDLine21Field1 = 0x00000002
# pin for DVD style closed caption data found in GOP layer of field 2
# if set, indicates that black bars have been encoded in the top
KS_MPEG2_DVDLine21Field2 = 0x00000004
# and bottom of the video.
# if set, indicates "film mode" used for 625/50 content.  If cleared,
KS_MPEG2_SourceIsLetterboxed = 0x00000008
# indicates that "camera mode" was used.
# if set and this stream is sent to an analog output, it should
KS_MPEG2_FilmCameraMode = 0x00000010
# be letterboxed.  Streams sent to VGA should be letterboxed only by renderers.
# if set, the MPEG-2 decoder must process DSS style user data
KS_MPEG2_LetterboxAnalogOut = 0x00000020
# if set, the MPEG-2 decoder must process DVB style user data
# if set, the PTS,DTS timestamps advance at 27MHz rather than 90KHz
KS_MPEG2_DSS_UserData = 0x00000040
KS_MPEG2_DVB_UserData = 0x00000080
KS_MPEG2_27MhzTimebase = 0x00000100
# if set and this stream is sent to an analog output, it should
# be in widescreen format (4x3 content should be centered on a 16x9 output).
# Streams sent to VGA should be widescreened only by renderers.
KS_MPEG2_WidescreenAnalogOut = 0x00000200
# Used to test if these flags are supported.  Set and test for AcceptMediaType.
# If rejected, then you cannot use the AMCONTROL flags (send 0 for dwReserved1)
# if set means display the image in a 4x3 area
KS_AMCONTROL_USED = 0x00000001
# if set means display the image in a 16x9 area
# if set, indicates DXVA color info is present in the upper (24) bits of the
# dwControlFlags
KS_AMCONTROL_PAD_TO_4x3 = 0x00000002
KS_AMCONTROL_PAD_TO_16x9 = 0x00000004
# (NTDDI_VERSION >= NTDDI_WINXP)
KS_AMCONTROL_COLORINFO_PRESENT = 0x00000080


class tagKS_VIDEOINFOHEADER2(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('dwControlFlags', DWORD),
            ('dwReserved1', DWORD),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('rcSource', RECT),
        ('rcTarget', RECT),
        ('dwBitRate', DWORD),
        ('dwBitErrorRate', DWORD),
        ('AvgTimePerFrame', REFERENCE_TIME),
        ('dwInterlaceFlags', DWORD),
        ('dwCopyProtectFlags', DWORD),
        ('dwPictAspectRatioX', DWORD),
        ('dwPictAspectRatioY', DWORD),
        ('_Union_0', _Union_0),
        ('dwReserved2', DWORD),
        ('bmiHeader', KS_BITMAPINFOHEADER),
    ]


KS_VIDEOINFOHEADER2 = tagKS_VIDEOINFOHEADER2
PKS_VIDEOINFOHEADER2 = POINTER(tagKS_VIDEOINFOHEADER2)


# use AMINTERLACE_* defines. Reject connection if undefined bits are not 0
# use KS_COPYPROTECT_* defines. Reject connection if undefined bits are not 0
# X dimension of picture aspect ratio, e.g. 16 for 16x9 display
# Y dimension of picture aspect ratio, e.g.  9 for 16x9 display
# use KS_AMCONTROL_* defines, use this from now on
# for backward compatiblity (was "must be 0";  connection rejected otherwise)
# must be 0; reject connection otherwise
# Compatible with VIDEOINFO

class tagKS_MPEG1VIDEOINFO(ctypes.Structure):
    _fields_ = [
        ('hdr', KS_VIDEOINFOHEADER),
        ('dwStartTimeCode', DWORD),
        ('cbSequenceHeader', DWORD),
        ('bSequenceHeader', BYTE * 1),
    ]


KS_MPEG1VIDEOINFO = tagKS_MPEG1VIDEOINFO
PKS_MPEG1VIDEOINFO = POINTER(tagKS_MPEG1VIDEOINFO)


# 25-bit Group of pictures time code at start of data
# Length in bytes of bSequenceHeader
# Sequence header including quantization matrices if any
KS_MAX_SIZE_MPEG1_SEQUENCE_INFO = 0x8C


def KS_SIZE_MPEG1VIDEOINFO(pv):
    return FIELD_OFFSET(
        KS_MPEG1VIDEOINFO.bSequenceHeader[0] + pv.cbSequenceHeader
    )


class tagKS_MPEGVIDEOINFO2(ctypes.Structure):
    _fields_ = [
        ('hdr', KS_VIDEOINFOHEADER2),
        ('dwStartTimeCode', DWORD),
        ('cbSequenceHeader', DWORD),
        ('dwProfile', DWORD),
        ('dwLevel', DWORD),
        ('dwFlags', DWORD),
        ('bSequenceHeader', DWORD * 1),
    ]


KS_MPEGVIDEOINFO2 = tagKS_MPEGVIDEOINFO2
PKS_MPEGVIDEOINFO2 = POINTER(tagKS_MPEGVIDEOINFO2)


# ?? not used for DVD ??
# is 0 for DVD (no sequence header)
# use enum MPEG2Profile
# use enum MPEG2Level
# use AMMPEG2_* defines.  Reject connection if undefined bits are not 0
# DWORD instead of Byte for alignment purposes
# For MPEG-2, if a sequence_header is included, the sequence_extension
# should also be included
# from UVC 1.5 H.264 frame descriptor

class tagKS_H264VIDEOINFO(ctypes.Structure):
    _fields_ = [
        ('wWidth', WORD),
        ('wHeight', WORD),
        ('wSARwidth', WORD),
        ('wSARheight', WORD),
        ('wProfile', WORD),
        ('bLevelIDC', BYTE),
        ('wConstrainedToolset', WORD),
        ('bmSupportedUsages', DWORD),
        ('bmCapabilities', WORD),
        ('bmSVCCapabilities', DWORD),
        ('bmMVCCapabilities', DWORD),
        ('dwFrameInterval', DWORD),
        ('bMaxCodecConfigDelay', BYTE),
        ('bmSupportedSliceModes', BYTE),
        ('bmSupportedSyncFrameTypes', BYTE),
        ('bResolutionScaling', BYTE),
        ('bSimulcastSupport', BYTE),
        ('bmSupportedRateControlModes', BYTE),
        ('wMaxMBperSecOneResolutionNoScalability', WORD),
        ('wMaxMBperSecTwoResolutionsNoScalability', WORD),
        ('wMaxMBperSecThreeResolutionsNoScalability', WORD),
        ('wMaxMBperSecFourResolutionsNoScalability', WORD),
        ('wMaxMBperSecOneResolutionTemporalScalability', WORD),
        ('wMaxMBperSecTwoResolutionsTemporalScalablility', WORD),
        ('wMaxMBperSecThreeResolutionsTemporalScalability', WORD),
        ('wMaxMBperSecFourResolutionsTemporalScalability', WORD),
        ('wMaxMBperSecOneResolutionTemporalQualityScalability', WORD),
        ('wMaxMBperSecTwoResolutionsTemporalQualityScalability', WORD),
        ('wMaxMBperSecThreeResolutionsTemporalQualityScalablity', WORD),
        ('wMaxMBperSecFourResolutionsTemporalQualityScalability', WORD),
        ('wMaxMBperSecOneResolutionTemporalSpatialScalability', WORD),
        ('wMaxMBperSecTwoResolutionsTemporalSpatialScalability', WORD),
        ('wMaxMBperSecThreeResolutionsTemporalSpatialScalablity', WORD),
        ('wMaxMBperSecFourResolutionsTemporalSpatialScalability', WORD),
        ('wMaxMBperSecOneResolutionFullScalability', WORD),
        ('wMaxMBperSecTwoResolutionsFullScalability', WORD),
        ('wMaxMBperSecThreeResolutionsFullScalability', WORD),
        ('wMaxMBperSecFourResolutionsFullScalability', WORD),
    ]


KS_H264VIDEOINFO = tagKS_H264VIDEOINFO
PKS_H264VIDEOINFO = POINTER(tagKS_H264VIDEOINFO)


def KS_SIZE_MPEGVIDEOINFO2(pv):
    return FIELD_OFFSET(
        KS_MPEGVIDEOINFO2.bSequenceHeader[0] + pv.cbSequenceHeader
    )


def KS_MPEG1_SEQUENCE_INFO(pv):
    return BYTE * pv.bSequenceHeader


# ===========================================================================
# Audio format blocks
# ===========================================================================
# if set, the PTS,DTS timestamps advance at 27MHz rather than 90KHz
KS_MPEGAUDIOINFO_27MhzTimebase = 0x00000001
# use KS_MPEGAUDIOINFO_* defines.  Reject connection if undefined bits are not
# 0


class tagKS_MPEAUDIOINFO(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('dwReserved1', DWORD),
        ('dwReserved2', DWORD),
        ('dwReserved3', DWORD),
    ]


KS_MPEGAUDIOINFO = tagKS_MPEAUDIOINFO
PKS_MPEGAUDIOINFO = POINTER(tagKS_MPEAUDIOINFO)

# ===========================================================================
# Video DATAFORMATs
# ===========================================================================

class tagKS_DATAFORMAT_VIDEOINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('VideoInfoHeader', KS_VIDEOINFOHEADER),
    ]


KS_DATAFORMAT_VIDEOINFOHEADER = tagKS_DATAFORMAT_VIDEOINFOHEADER
PKS_DATAFORMAT_VIDEOINFOHEADER = POINTER(tagKS_DATAFORMAT_VIDEOINFOHEADER)


class tagKS_DATAFORMAT_VIDEOINFOHEADER2(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('VideoInfoHeader2', KS_VIDEOINFOHEADER2),
    ]


KS_DATAFORMAT_VIDEOINFOHEADER2 = tagKS_DATAFORMAT_VIDEOINFOHEADER2
PKS_DATAFORMAT_VIDEOINFOHEADER2 = POINTER(tagKS_DATAFORMAT_VIDEOINFOHEADER2)


class tagKS_DATAFORMAT_MPEGVIDEOINFO2(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('MpegVideoInfoHeader2', KS_MPEGVIDEOINFO2),
    ]


KS_DATAFORMAT_MPEGVIDEOINFO2 = tagKS_DATAFORMAT_MPEGVIDEOINFO2
PKS_DATAFORMAT_MPEGVIDEOINFO2 = POINTER(tagKS_DATAFORMAT_MPEGVIDEOINFO2)


class tagKS_DATAFORMAT_H264VIDEOINFO(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('H264VideoInfoHeader', KS_H264VIDEOINFO),
    ]


KS_DATAFORMAT_H264VIDEOINFO = tagKS_DATAFORMAT_H264VIDEOINFO
PKS_DATAFORMAT_H264VIDEOINFO = POINTER(tagKS_DATAFORMAT_H264VIDEOINFO)


class tagKS_DATAFORMAT_IMAGEINFO(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('ImageInfoHeader', KS_BITMAPINFOHEADER),
    ]


KS_DATAFORMAT_IMAGEINFO = tagKS_DATAFORMAT_IMAGEINFO
PKS_DATAFORMAT_IMAGEINFO = POINTER(tagKS_DATAFORMAT_IMAGEINFO)


class tagKS_DATAFORMAT_VIDEOINFO_PALETTE(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('VideoInfo', KS_VIDEOINFO),
    ]


KS_DATAFORMAT_VIDEOINFO_PALETTE = tagKS_DATAFORMAT_VIDEOINFO_PALETTE
PKS_DATAFORMAT_VIDEOINFO_PALETTE = POINTER(tagKS_DATAFORMAT_VIDEOINFO_PALETTE)


class tagKS_DATAFORMAT_VBIINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('DataFormat', KSDATAFORMAT),
        ('VBIInfoHeader', KS_VBIINFOHEADER),
    ]


KS_DATAFORMAT_VBIINFOHEADER = tagKS_DATAFORMAT_VBIINFOHEADER
PKS_DATAFORMAT_VBIINFOHEADER = POINTER(tagKS_DATAFORMAT_VBIINFOHEADER)


# will be MEDIATYPE_Video
class _KS_VIDEO_STREAM_CONFIG_CAPS(ctypes.Structure):
    _fields_ = [
        ('guid', GUID),
        ('VideoStandard', ULONG),
        ('InputSize', SIZE),
        ('MinCroppingSize', SIZE),
        ('MaxCroppingSize', SIZE),
        ('CropGranularityX', INT),
        ('CropGranularityY', INT),
        ('CropAlignX', INT),
        ('CropAlignY', INT),
        ('MinOutputSize', SIZE),
        ('MaxOutputSize', SIZE),
        ('OutputGranularityX', INT),
        ('OutputGranularityY', INT),
        ('StretchTapsX', INT),
        ('StretchTapsY', INT),
        ('ShrinkTapsX', INT),
        ('ShrinkTapsY', INT),
        ('MinFrameInterval', LONGLONG),
        ('MaxFrameInterval', LONGLONG),
        ('MinBitsPerSecond', LONG),
        ('MaxBitsPerSecond', LONG),
    ]


KS_VIDEO_STREAM_CONFIG_CAPS = _KS_VIDEO_STREAM_CONFIG_CAPS
PKS_VIDEO_STREAM_CONFIG_CAPS = POINTER(_KS_VIDEO_STREAM_CONFIG_CAPS)


# logical OR of all AnalogVideoStandards
# supported
# the inherent size of the incoming signal
# (every pixel unique)
# smallest rcSrc cropping rect allowed
# largest rcSrc cropping rect allowed
# granularity of cropping size
# alignment of cropping rect
# smallest bitmap stream can produce
# largest  bitmap stream can produce
# granularity of output bitmap size
# 0, no stretch, 1 pix dup, 2 INTerp, ...
# Describes quality of hardware scaler
# 100 nS units


# ===========================================================================
# Video DATARANGEs
# ===========================================================================
class tagKS_DATARANGE_VIDEO(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('StreamDescriptionFlags', DWORD),
        ('MemoryAllocationFlags', DWORD),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('VideoInfoHeader', KS_VIDEOINFOHEADER),
    ]


KS_DATARANGE_VIDEO = tagKS_DATARANGE_VIDEO
PKS_DATARANGE_VIDEO = POINTER(tagKS_DATARANGE_VIDEO)


class tagKS_DATARANGE_VIDEO2(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('StreamDescriptionFlags', DWORD),
        ('MemoryAllocationFlags', DWORD),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('VideoInfoHeader', KS_VIDEOINFOHEADER2),
    ]


KS_DATARANGE_VIDEO2 = tagKS_DATARANGE_VIDEO2
PKS_DATARANGE_VIDEO2 = POINTER(tagKS_DATARANGE_VIDEO2)


class tagKS_DATARANGE_MPEG1_VIDEO(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('StreamDescriptionFlags', DWORD),
        ('MemoryAllocationFlags', DWORD),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('VideoInfoHeader', KS_MPEG1VIDEOINFO),
    ]


KS_DATARANGE_MPEG1_VIDEO = tagKS_DATARANGE_MPEG1_VIDEO
PKS_DATARANGE_MPEG1_VIDEO = POINTER(tagKS_DATARANGE_MPEG1_VIDEO)


class tagKS_DATARANGE_MPEG2_VIDEO(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('StreamDescriptionFlags', DWORD),
        ('MemoryAllocationFlags', DWORD),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('VideoInfoHeader', KS_MPEGVIDEOINFO2),
    ]


KS_DATARANGE_MPEG2_VIDEO = tagKS_DATARANGE_MPEG2_VIDEO
PKS_DATARANGE_MPEG2_VIDEO = POINTER(tagKS_DATARANGE_MPEG2_VIDEO)


class tagKS_DATARANGE_H264_VIDEO(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('StreamDescriptionFlags', DWORD),
        ('MemoryAllocationFlags', DWORD),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('VideoInfoHeader', KS_H264VIDEOINFO),
    ]


KS_DATARANGE_H264_VIDEO = tagKS_DATARANGE_H264_VIDEO
PKS_DATARANGE_H264_VIDEO = POINTER(tagKS_DATARANGE_H264_VIDEO)


class tagKS_DATARANGE_IMAGE(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('ImageInfoHeader', KS_BITMAPINFOHEADER),
    ]


KS_DATARANGE_IMAGE = tagKS_DATARANGE_IMAGE
PKS_DATARANGE_IMAGE = POINTER(tagKS_DATARANGE_IMAGE)


class tagKS_DATARANGE_VIDEO_PALETTE(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('StreamDescriptionFlags', DWORD),
        ('MemoryAllocationFlags', DWORD),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('VideoInfo', KS_VIDEOINFO),
    ]


KS_DATARANGE_VIDEO_PALETTE = tagKS_DATARANGE_VIDEO_PALETTE
PKS_DATARANGE_VIDEO_PALETTE = POINTER(tagKS_DATARANGE_VIDEO_PALETTE)


class tagKS_DATARANGE_VIDEO_VBI(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('StreamDescriptionFlags', DWORD),
        ('MemoryAllocationFlags', DWORD),
        ('ConfigCaps', KS_VIDEO_STREAM_CONFIG_CAPS),
        ('VBIInfoHeader', KS_VBIINFOHEADER),
    ]


KS_DATARANGE_VIDEO_VBI = tagKS_DATARANGE_VIDEO_VBI
PKS_DATARANGE_VIDEO_VBI = POINTER(tagKS_DATARANGE_VIDEO_VBI)


class tagKS_DATARANGE_ANALOGVIDEO(ctypes.Structure):
    _fields_ = [
        ('DataRange', KSDATARANGE),
        ('AnalogVideoInfo', KS_ANALOGVIDEOINFO),
    ]


KS_DATARANGE_ANALOGVIDEO = tagKS_DATARANGE_ANALOGVIDEO
PKS_DATARANGE_ANALOGVIDEO = POINTER(tagKS_DATARANGE_ANALOGVIDEO)


# ===========================================================================
# StreamDescriptionFlags
# These define the "purpose" of each video stream
# ===========================================================================
# Preview stream
# Capture stream
# Field1 VBI
KS_VIDEOSTREAM_PREVIEW = 0x0001
# Field1 NABTS
KS_VIDEOSTREAM_CAPTURE = 0x0002
# Closed Captioning
KS_VIDEOSTREAM_VBI = 0x0010
# Extended Data Services
KS_VIDEOSTREAM_NABTS = 0x0020
# Field1 Teletext only
KS_VIDEOSTREAM_CC = 0x0100
# Still image input
KS_VIDEOSTREAM_EDS = 0x0200
# Is a VPE based stream?
KS_VIDEOSTREAM_TELETEXT = 0x0400
KS_VIDEOSTREAM_STILL = 0x1000
# MemoryAllocationFlags
KS_VIDEOSTREAM_IS_VPE = 0x8000
# VPE surface in system memory
# VPE surface in display memory
# VPE surface in AGP memory
KS_VIDEO_ALLOC_VPE_SYSTEM = 0x0001
KS_VIDEO_ALLOC_VPE_DISPLAY = 0x0002
KS_VIDEO_ALLOC_VPE_AGP = 0x0004


# Capture driver VBI property sets

class KSPROPERTY_VBICAP(ENUM):
    KSPROPERTY_VBICAP_PROPERTIES_PROTECTION = 0x01


class _VBICAP_PROPERTIES_PROTECTION_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('Status', ULONG),
    ]


VBICAP_PROPERTIES_PROTECTION_S = _VBICAP_PROPERTIES_PROTECTION_S
PVBICAP_PROPERTIES_PROTECTION_S = POINTER(_VBICAP_PROPERTIES_PROTECTION_S)


# Index of stream
KS_VBICAP_PROTECTION_MV_PRESENT = 0x0001
KS_VBICAP_PROTECTION_MV_HARDWARE = 0x0002
KS_VBICAP_PROTECTION_MV_DETECTED = 0x0004
# *************************************************************************
# VBI Related GUIDs, structs and properties for codecs(generic, cc, nabts)
# *************************************************************************
# /
# IP/NABTS Protocol Reserved Group IDs - Overall Range 0x800-0x8FF [Decimal
# 2048-2079]
# Intervening values(0-F) are used if there are multiple providers at a
# particular tier
# /
# Used by individual content creators in show footage/data
KS_NABTS_GROUPID_ORIGINAL_CONTENT_BASE = 0x800
# Used by production company in finished show data
KS_NABTS_GROUPID_ORIGINAL_CONTENT_ADVERTISER_BASE = 0x810
KS_NABTS_GROUPID_PRODUCTION_COMPANY_CONTENT_BASE = 0x820
# Used by broadcast syndicates in syndicated show data
KS_NABTS_GROUPID_PRODUCTION_COMPANY_ADVERTISER_BASE = 0x830
KS_NABTS_GROUPID_SYNDICATED_SHOW_CONTENT_BASE = 0x840
# Used by tv networks in network television data
KS_NABTS_GROUPID_SYNDICATED_SHOW_ADVERTISER_BASE = 0x850
KS_NABTS_GROUPID_NETWORK_WIDE_CONTENT_BASE = 0x860
# Used by telvision stations in local programming data
KS_NABTS_GROUPID_NETWORK_WIDE_ADVERTISER_BASE = 0x870
KS_NABTS_GROUPID_TELEVISION_STATION_CONTENT_BASE = 0x880
# Used by cable system in cable head-end originated data
KS_NABTS_GROUPID_TELEVISION_STATION_ADVERTISER_BASE = 0x890
KS_NABTS_GROUPID_LOCAL_CABLE_SYSTEM_CONTENT_BASE = 0x8A0
# The values between 0x8C0 - 0x8EF are reserved for future expansion
KS_NABTS_GROUPID_LOCAL_CABLE_SYSTEM_ADVERTISER_BASE = 0x8B0
# Used by Microsoft for Testing purposes (0x8F0 - 0x8FF)

KS_NABTS_GROUPID_MICROSOFT_RESERVED_TEST_DATA_BASE = 0x8F0
# Stream Format FEC-corrected NABTS bundles

# NABTS Bundle data structure definition

MAX_NABTS_VBI_LINES_PER_FIELD = 11
NABTS_LINES_PER_BUNDLE = 16
NABTS_PAYLOAD_PER_LINE = 28
NABTS_BYTES_PER_LINE = 36


class _NABTSFEC_BUFFER(ctypes.Structure):
    _fields_ = [
        ('dataSize', ULONG),
        ('groupID', USHORT),
        ('Reserved', USHORT),
        ('data', UCHAR * (NABTS_LINES_PER_BUNDLE * NABTS_PAYLOAD_PER_LINE)),
    ]


NABTSFEC_BUFFER = _NABTSFEC_BUFFER
PNABTSFEC_BUFFER = POINTER(_NABTSFEC_BUFFER)


# vbi codec filtering pin properties
class KSPROPERTY_VBICODECFILTERING(ENUM):
    KSPROPERTY_VBICODECFILTERING_SCANLINES_REQUESTED_BIT_ARRAY = 0x01
    KSPROPERTY_VBICODECFILTERING_SCANLINES_DISCOVERED_BIT_ARRAY = 2
    KSPROPERTY_VBICODECFILTERING_SUBSTREAMS_REQUESTED_BIT_ARRAY = 3
    KSPROPERTY_VBICODECFILTERING_SUBSTREAMS_DISCOVERED_BIT_ARRAY = 4
    KSPROPERTY_VBICODECFILTERING_STATISTICS = 5


# An array of scanline bits 0..1024(32*32)
class _VBICODECFILTERING_SCANLINES(ctypes.Structure):
    _fields_ = [
        ('DwordBitArray', DWORD * 32),
    ]


VBICODECFILTERING_SCANLINES = _VBICODECFILTERING_SCANLINES
PVBICODECFILTERING_SCANLINES = POINTER(_VBICODECFILTERING_SCANLINES)


# An array of 4096 bits (one for each NABTS GroupID)
class _VBICODECFILTERING_NABTS_SUBSTREAMS(ctypes.Structure):
    _fields_ = [
        ('SubstreamMask', DWORD * 128),
    ]


VBICODECFILTERING_NABTS_SUBSTREAMS = _VBICODECFILTERING_NABTS_SUBSTREAMS
PVBICODECFILTERING_NABTS_SUBSTREAMS = POINTER(
    _VBICODECFILTERING_NABTS_SUBSTREAMS
)


# An array of 32 bits (see KS_CC_SUBSTREAM *)
class _VBICODECFILTERING_CC_SUBSTREAMS(ctypes.Structure):
    _fields_ = [
        ('SubstreamMask', DWORD),
    ]


VBICODECFILTERING_CC_SUBSTREAMS = _VBICODECFILTERING_CC_SUBSTREAMS
PVBICODECFILTERING_CC_SUBSTREAMS = POINTER(_VBICODECFILTERING_CC_SUBSTREAMS)


# These KS_CC_SUBSTREAM_* bitmasks are used with
# VBICODECFILTERING_CC_SUBSTREAMS
# Unfiltered Field 1 Data
# Unfiltered Field 2 Data
KS_CC_SUBSTREAM_ODD = 0x0001
KS_CC_SUBSTREAM_EVEN = 0x0002
# The following flags describe CC field 1 substreams: CC1,CC2,TT1,TT2
KS_CC_SUBSTREAM_FIELD1_MASK = 0x00F0
KS_CC_SUBSTREAM_SERVICE_CC1 = 0x0010
KS_CC_SUBSTREAM_SERVICE_CC2 = 0x0020
KS_CC_SUBSTREAM_SERVICE_T1 = 0x0040
# The following flags describe CC field 2 substreams: CC3,CC4,TT3,TT4,XDS
KS_CC_SUBSTREAM_SERVICE_T2 = 0x0080
KS_CC_SUBSTREAM_FIELD2_MASK = 0x1F00
KS_CC_SUBSTREAM_SERVICE_CC3 = 0x0100
KS_CC_SUBSTREAM_SERVICE_CC4 = 0x0200
KS_CC_SUBSTREAM_SERVICE_T3 = 0x0400
KS_CC_SUBSTREAM_SERVICE_T4 = 0x0800
# Special Note: field 1 or 2 substreams are usually on found on field 1 and 2
# respectively
KS_CC_SUBSTREAM_SERVICE_XDS = 0x1000
# If the VBI odd/even polarity is reversed, the correct filtered data will
# still be found.
# /
# Hardware decoded CC stream format
# /
CC_MAX_HW_DECODE_LINES = 0xC


class _CC_BYTE_PAIR(ctypes.Structure):
    _fields_ = [
        ('Decoded', BYTE * 2),
        ('Reserved', USHORT),
    ]


CC_BYTE_PAIR = _CC_BYTE_PAIR
PCC_BYTE_PAIR = POINTER(_CC_BYTE_PAIR)


class _CC_HW_FIELD(ctypes.Structure):
    _fields_ = [
        ('ScanlinesRequested', VBICODECFILTERING_SCANLINES),
        ('fieldFlags', ULONG),
        ('PictureNumber', LONGLONG),
        ('Lines', CC_BYTE_PAIR * CC_MAX_HW_DECODE_LINES),
    ]


CC_HW_FIELD = _CC_HW_FIELD
PCC_HW_FIELD = POINTER(_CC_HW_FIELD)


# KS_VBI_FLAG_FIELD1,2
# (NTDDI_VERSION >= NTDDI_WINXP)
# /
# Raw NABTS stream format (TYPE_NABTS, SUBTYPE_NABTS)
# /
# These low-level structures are byte packed( -Zp1 )
# from pshpack1_h import * # NOQA


class _NABTS_BUFFER_LINE(ctypes.Structure):
    _fields_ = [
        ('Confidence', BYTE),
        ('Bytes', BYTE * NABTS_BYTES_PER_LINE),
    ]


NABTS_BUFFER_LINE = _NABTS_BUFFER_LINE
PNABTS_BUFFER_LINE = POINTER(_NABTS_BUFFER_LINE)


NABTS_BUFFER_PICTURENUMBER_SUPPORT = 0x1


class _NABTS_BUFFER(ctypes.Structure):
    _fields_ = [
        ('ScanlinesRequested', VBICODECFILTERING_SCANLINES),
        ('PictureNumber', LONGLONG),
        ('NabtsLines', NABTS_BUFFER_LINE * MAX_NABTS_VBI_LINES_PER_FIELD),
    ]


NABTS_BUFFER = _NABTS_BUFFER
PNABTS_BUFFER = POINTER(_NABTS_BUFFER)


# from poppack_h import * # NOQA

# WST Codec Teletext Media Sample Format

# Starting a tuning operation
# Ending a tuning operation
WST_TVTUNER_CHANGE_BEGIN_TUNE = 0x1000
WST_TVTUNER_CHANGE_END_TUNE = 0x2000
MAX_WST_VBI_LINES_PER_FIELD = 17
WST_BYTES_PER_LINE = 42


class _WST_BUFFER_LINE(ctypes.Structure):
    _fields_ = [
        ('Confidence', BYTE),
        ('Bytes', BYTE * WST_BYTES_PER_LINE),
    ]


WST_BUFFER_LINE = _WST_BUFFER_LINE
PWST_BUFFER_LINE = POINTER(_WST_BUFFER_LINE)


class _WST_BUFFER(ctypes.Structure):
    _fields_ = [
        ('ScanlinesRequested', VBICODECFILTERING_SCANLINES),
        ('WstLines', WST_BUFFER_LINE * MAX_WST_VBI_LINES_PER_FIELD),
    ]


WST_BUFFER = _WST_BUFFER
PWST_BUFFER = POINTER(_WST_BUFFER)


# Common codec statistics
# upstream SRBs received

class _VBICODECFILTERING_STATISTICS_COMMON(ctypes.Structure):
    _fields_ = [
        ('InputSRBsProcessed', DWORD),
        ('OutputSRBsProcessed', DWORD),
        ('SRBsIgnored', DWORD),
        ('InputSRBsMissing', DWORD),
        ('OutputSRBsMissing', DWORD),
        ('OutputFailures', DWORD),
        ('InternalErrors', DWORD),
        ('ExternalErrors', DWORD),
        ('InputDiscontinuities', DWORD),
        ('DSPFailures', DWORD),
        ('TvTunerChanges', DWORD),
        ('VBIHeaderChanges', DWORD),
        ('LineConfidenceAvg', DWORD),
        ('BytesOutput', DWORD),
    ]


VBICODECFILTERING_STATISTICS_COMMON = _VBICODECFILTERING_STATISTICS_COMMON
PVBICODECFILTERING_STATISTICS_COMMON = POINTER(
    _VBICODECFILTERING_STATISTICS_COMMON
)


# downstream SRBs sent
# SRBs ignored due to no requests
# SRBs dropped upstream
# Output dropped because no SRB pending
# dropped because of other failure
# could not process due to INT. failure
# could not process due to ext. failure
# discontinuities received
# DSP confidence failure
# number of received KS_TVTUNER_CHANGE_BEGIN_TUNE and
# KS_TVTUNER_CHANGE_END_TUNE pairs.
# number of received KS_VBI_FLAG_VBIINFOHEADER_CHANGE
# Average of all DSP confidence results
# Bytes sent downstream
# SRBs sent/received

class _VBICODECFILTERING_STATISTICS_COMMON_PIN(ctypes.Structure):
    _fields_ = [
        ('SRBsProcessed', DWORD),
        ('SRBsIgnored', DWORD),
        ('SRBsMissing', DWORD),
        ('InternalErrors', DWORD),
        ('ExternalErrors', DWORD),
        ('Discontinuities', DWORD),
        ('LineConfidenceAvg', DWORD),
        ('BytesOutput', DWORD),
    ]


VBICODECFILTERING_STATISTICS_COMMON_PIN = (
    _VBICODECFILTERING_STATISTICS_COMMON_PIN
)
PVBICODECFILTERING_STATISTICS_COMMON_PIN = POINTER(
    _VBICODECFILTERING_STATISTICS_COMMON_PIN
)


# SRBs ignored due to filtering
# SRBs not sent/received
# could not send/receive due to INT. failure
# could not send/receive due to ext. failure
# discontinuities received/sent
# Average of all DSP confidence results for this pin
# Bytes sent downstream

# Codec-specific statistics - NABTS

# Generic VBI statistics

class _VBICODECFILTERING_STATISTICS_NABTS(ctypes.Structure):
    _fields_ = [
        ('Common', VBICODECFILTERING_STATISTICS_COMMON),
        ('FECBundleBadLines', DWORD),
        ('FECQueueOverflows', DWORD),
        ('FECCorrectedLines', DWORD),
        ('FECUncorrectableLines', DWORD),
        ('BundlesProcessed', DWORD),
        ('BundlesSent2IP', DWORD),
        ('FilteredLines', DWORD),
    ]


VBICODECFILTERING_STATISTICS_NABTS = _VBICODECFILTERING_STATISTICS_NABTS
PVBICODECFILTERING_STATISTICS_NABTS = POINTER(
    _VBICODECFILTERING_STATISTICS_NABTS
)


# Un-FEC-correctable lines
# Number of times FEC queue overflowed
# Lines CSUM corrected by FEC
# FEC input lines not CSUM correctable
# Bundles received from FEC
# Bundles sent to IP driver
# Lines processed and then dropped
# because no one was INTerested
# Generic VBI pin statistics

class _VBICODECFILTERING_STATISTICS_NABTS_PIN(ctypes.Structure):
    _fields_ = [
        ('Common', VBICODECFILTERING_STATISTICS_COMMON_PIN),
    ]


VBICODECFILTERING_STATISTICS_NABTS_PIN = (
    _VBICODECFILTERING_STATISTICS_NABTS_PIN
)
PVBICODECFILTERING_STATISTICS_NABTS_PIN = POINTER(
    _VBICODECFILTERING_STATISTICS_NABTS_PIN
)


# Codec-specific statistics - Closed Caption

# Generic VBI statistics

class _VBICODECFILTERING_STATISTICS_CC(ctypes.Structure):
    _fields_ = [
        ('Common', VBICODECFILTERING_STATISTICS_COMMON),
    ]


VBICODECFILTERING_STATISTICS_CC = _VBICODECFILTERING_STATISTICS_CC
PVBICODECFILTERING_STATISTICS_CC = POINTER(_VBICODECFILTERING_STATISTICS_CC)


# Generic VBI pin statistics

class _VBICODECFILTERING_STATISTICS_CC_PIN(ctypes.Structure):
    _fields_ = [
        ('Common', VBICODECFILTERING_STATISTICS_COMMON_PIN),
    ]


VBICODECFILTERING_STATISTICS_CC_PIN = _VBICODECFILTERING_STATISTICS_CC_PIN
PVBICODECFILTERING_STATISTICS_CC_PIN = POINTER(
    _VBICODECFILTERING_STATISTICS_CC_PIN
)


# Codec-specific statistics - Teletext

# Generic VBI statistics

class _VBICODECFILTERING_STATISTICS_TELETEXT(ctypes.Structure):
    _fields_ = [
        ('Common', VBICODECFILTERING_STATISTICS_COMMON),
    ]


VBICODECFILTERING_STATISTICS_TELETEXT = _VBICODECFILTERING_STATISTICS_TELETEXT
PVBICODECFILTERING_STATISTICS_TELETEXT = POINTER(
    _VBICODECFILTERING_STATISTICS_TELETEXT
)


# Generic VBI pin statistics

class _VBICODECFILTERING_STATISTICS_TELETEXT_PIN(ctypes.Structure):
    _fields_ = [
        ('Common', VBICODECFILTERING_STATISTICS_COMMON_PIN),
    ]


VBICODECFILTERING_STATISTICS_TELETEXT_PIN = (
    _VBICODECFILTERING_STATISTICS_TELETEXT_PIN
)
PVBICODECFILTERING_STATISTICS_TELETEXT_PIN = POINTER(
    _VBICODECFILTERING_STATISTICS_TELETEXT_PIN
)

# VBI codec property structures(based on KSPROPERTY_VBICODECFILTERING enum)
# *** Most codecs support this property
# KSPROPERTY_VBICODECFILTERING_SCANLINES_REQUESTED_BIT_ARRAY
# KSPROPERTY_VBICODECFILTERING_SCANLINES_DISCOVERED_BIT_ARRAY,

class KSPROPERTY_VBICODECFILTERING_SCANLINES_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Scanlines', VBICODECFILTERING_SCANLINES),
    ]


PKSPROPERTY_VBICODECFILTERING_SCANLINES_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_SCANLINES_S
)


# *** NABTS codecs support this property
# KSPROPERTY_VBICODECFILTERING_SUBSTREAMS_REQUESTED_BIT_ARRAY,
# KSPROPERTY_VBICODECFILTERING_SUBSTREAMS_DISCOVERED_BIT_ARRAY,

class KSPROPERTY_VBICODECFILTERING_NABTS_SUBSTREAMS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Substreams', VBICODECFILTERING_NABTS_SUBSTREAMS),
    ]


PKSPROPERTY_VBICODECFILTERING_NABTS_SUBSTREAMS_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_NABTS_SUBSTREAMS_S
)


# *** Closed captioning codecs support this property
# KSPROPERTY_VBICODECFILTERING_SUBSTREAMS_REQUESTED_BIT_ARRAY,
# KSPROPERTY_VBICODECFILTERING_SUBSTREAMS_DISCOVERED_BIT_ARRAY,

class KSPROPERTY_VBICODECFILTERING_CC_SUBSTREAMS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Substreams', VBICODECFILTERING_CC_SUBSTREAMS),
    ]


PKSPROPERTY_VBICODECFILTERING_CC_SUBSTREAMS_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_CC_SUBSTREAMS_S
)


# *** Most codecs support these versions of the global and pin properties
# KSPROPERTY_VBICODECFILTERING_STATISTICS

class KSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Statistics', VBICODECFILTERING_STATISTICS_COMMON),
    ]


PKSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_S
)


class KSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_PIN_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Statistics', VBICODECFILTERING_STATISTICS_COMMON_PIN),
    ]


PKSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_PIN_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_PIN_S
)


# *** NABTS codecs support this version of the global and pin properties
# KSPROPERTY_VBICODECFILTERING_STATISTICS

class KSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Statistics', VBICODECFILTERING_STATISTICS_NABTS),
    ]


PKSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_S
)


class KSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_PIN_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Statistics', VBICODECFILTERING_STATISTICS_NABTS_PIN),
    ]


PKSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_PIN_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_PIN_S
)


# *** Closed captioning codecs support this version of the global and pin
# properties
# KSPROPERTY_VBICODECFILTERING_STATISTICS

class KSPROPERTY_VBICODECFILTERING_STATISTICS_CC_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Statistics', VBICODECFILTERING_STATISTICS_CC),
    ]


PKSPROPERTY_VBICODECFILTERING_STATISTICS_CC_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_STATISTICS_CC_S
)


class KSPROPERTY_VBICODECFILTERING_STATISTICS_CC_PIN_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Statistics', VBICODECFILTERING_STATISTICS_CC_PIN),
    ]


PKSPROPERTY_VBICODECFILTERING_STATISTICS_CC_PIN_S = POINTER(
    KSPROPERTY_VBICODECFILTERING_STATISTICS_CC_PIN_S
)


# ===========================================================================
# Capture MemoryAllocationFlags
# surface in system memory
class CAPTURE_MEMORY_ALLOCATION_FLAGS(ENUM):
    KS_CAPTURE_ALLOC_INVALID = 0
    KS_CAPTURE_ALLOC_SYSTEM = 0x0001
    KS_CAPTURE_ALLOC_VRAM = 0x0002
    KS_CAPTURE_ALLOC_SYSTEM_AGP = 0x0004
    KS_CAPTURE_ALLOC_VRAM_MAPPED = 0x0008
    KS_CAPTURE_ALLOC_SECURE_BUFFER = 0x0010


PCAPTURE_MEMORY_ALLOCATION_FLAGS = POINTER(CAPTURE_MEMORY_ALLOCATION_FLAGS)


# surface in display memory
# surface in system memory tagged as AGP accessible
# surface in system memory mapped INTo VRAM address space
# secure buffer in VTL1


# Video memory capture KSPROPSETID

# enum value '0' means an invalid KSPROPERTY request.
class KSPROPERTY_VIDMEM_TRANSPORT(ENUM):
    KSPROPERTY_DISPLAY_ADAPTER_GUID = 1
    KSPROPERTY_PREFERRED_CAPTURE_SURFACE = 2
    KSPROPERTY_CURRENT_CAPTURE_SURFACE = 3
    KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS = 4


# Drivers should return an error.

# Returns the Adapter GUID.
# Returns the memory surface preferred by that pin
# Sets/Gets currently selected capture surface
# Maps VRAM surface handle to VRAM physical address


def DEFINE_KSPROPERTY_ITEM_DISPLAY_ADAPTER_GUID(GetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_VIDMEM_TRANSPORT.KSPROPERTY_DISPLAY_ADAPTER_GUID,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(GUID),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_PREFERRED_CAPTURE_SURFACE(GetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_VIDMEM_TRANSPORT.KSPROPERTY_PREFERRED_CAPTURE_SURFACE,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(CAPTURE_MEMORY_ALLOCATION_FLAGS),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_CURRENT_CAPTURE_SURFACE(GetHandler, SetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_VIDMEM_TRANSPORT.KSPROPERTY_CURRENT_CAPTURE_SURFACE,
        GetHandler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(CAPTURE_MEMORY_ALLOCATION_FLAGS),
        SetHandler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS(GetHandler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_VIDMEM_TRANSPORT.KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS,
        GetHandler,
        ctypes.sizeof(VRAM_SURFACE_INFO_PROPERTY_S),
        ctypes.sizeof(DWORD),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )

# Surface info passed on to the mini driver.


class VRAM_SURFACE_INFO(ctypes.Structure):
    _fields_ = [
        ('hSurface', UINT_PTR),
        ('VramPhysicalAddress', LONGLONG),
        ('cbCaptured', DWORD),
        ('dwWidth', DWORD),
        ('dwHeight', DWORD),
        ('dwLinearSize', DWORD),
        ('lPitch', LONG),
        ('ullReserved', ULONGLONG * 16),
    ]


PVRAM_SURFACE_INFO = POINTER(VRAM_SURFACE_INFO)


class VRAM_SURFACE_INFO_PROPERTY_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('pVramSurfaceInfo', PVRAM_SURFACE_INFO),
    ]


PVRAM_SURFACE_INFO_PROPERTY_S = POINTER(VRAM_SURFACE_INFO_PROPERTY_S)

# Secure buffer info passed on to the mini driver.


class SECURE_BUFFER_INFO(ctypes.Structure):
    _fields_ = [
        ('guidBufferIdentifier', GUID),
        ('cbBufferSize', DWORD),
        ('cbCaptured', DWORD),
        ('ullReserved', ULONGLONG * 16),
    ]


PSECURE_BUFFER_INFO = POINTER(SECURE_BUFFER_INFO)


# Sceanrio ID for secure buffer for camera


class KSPROPERTY_MPEG4_MEDIATYPE_ATTRIBUTES(ENUM):
    KSPROPERTY_MPEG4_MEDIATYPE_SD_BOX = 1



class KSEVENT_DYNAMICFORMATCHANGE(ENUM):
    KSEVENT_DYNAMIC_FORMAT_CHANGE = 0


# ===========================================================================
# KSSTREAM_HEADER extensions for digital video
# ===========================================================================
# Frame or Field (default is frame)
# Frame or Field (default is frame)
KS_VIDEO_FLAG_FIELD_MASK = 0x0003
KS_VIDEO_FLAG_FRAME = 0x0000
KS_VIDEO_FLAG_FIELD1 = 0x0001
KS_VIDEO_FLAG_FIELD2 = 0x0002
KS_VIDEO_FLAG_FIELD1FIRST = 0x0004
# I, B, or P (default is I)
KS_VIDEO_FLAG_WEAVE = 0x0008
# I, B, or P (default is I)
KS_VIDEO_FLAG_IPB_MASK = 0x0030
KS_VIDEO_FLAG_I_FRAME = 0x0000
KS_VIDEO_FLAG_P_FRAME = 0x0010
KS_VIDEO_FLAG_B_FRAME = 0x0020
KS_VIDEO_FLAG_REPEAT_FIELD = 0x0040
# Size of this extended header


class tagKS_FRAME_INFO(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('lSurfacePitch', LONG),
            ('Reserved1', DWORD),
        ]

    class _Union_1(ctypes.Union):

        class _Struct_0(ctypes.Structure):
            _fields_ = [
                ('Reserved3', DWORD),
                ('Reserved4', DWORD),
            ]

        _anonymous_ = ('_Struct_0', )
        _fields_ = [
            ('_Struct_0', _Struct_0),
            ('FrameCompletionNumber', ULONGLONG),
        ]

    _anonymous_ = ('_Union_0', '_Union_1', )
    _fields_ = [
        ('ExtendedHeaderSize', ULONG),
        ('dwFrameFlags', DWORD),
        ('PictureNumber', LONGLONG),
        ('DropCount', LONGLONG),
        ('hDirectDraw', HANDLE),
        ('hSurfaceHandle', HANDLE),
        ('DirectDrawRect', RECT),
        ('_Union_0', _Union_0),
        ('Reserved2', DWORD),
        ('_Union_1', _Union_1),
    ]


KS_FRAME_INFO = tagKS_FRAME_INFO
PKS_FRAME_INFO = POINTER(tagKS_FRAME_INFO)


# Field1, Field2, or Frame
# The following are only set when using OverlayMixer
# user mode DDraw handle
# user mode surface handle
# portion of surface locked
# Contains surface pitch a.k.a stride
# ===========================================================================
# KSSTREAM_HEADER extensions for VBI
# ===========================================================================
# Frame or Field (default is frame)
KS_VBI_FLAG_FRAME = 0x0000
KS_VBI_FLAG_FIELD1 = 0x0001
KS_VBI_FLAG_FIELD2 = 0x0002
KS_VBI_FLAG_MV_PRESENT = 0x0100
# (NTDDI_VERSION >= NTDDI_WINXP)
KS_VBI_FLAG_MV_HARDWARE = 0x0200
KS_VBI_FLAG_MV_DETECTED = 0x0400
# TvTunerChangeInfo is valid
# VBIInfoHeader is valid
KS_VBI_FLAG_TVTUNER_CHANGE = 0x0010
KS_VBI_FLAG_VBIINFOHEADER_CHANGE = 0x0020
# Size of this extended header


class tagKS_VBI_FRAME_INFO(ctypes.Structure):
    _fields_ = [
        ('ExtendedHeaderSize', ULONG),
        ('dwFrameFlags', DWORD),
        ('PictureNumber', LONGLONG),
        ('DropCount', LONGLONG),
        ('dwSamplingFrequency', DWORD),
        ('TvTunerChangeInfo', KS_TVTUNER_CHANGE_INFO),
        ('VBIInfoHeader', KS_VBIINFOHEADER),
    ]


KS_VBI_FRAME_INFO = tagKS_VBI_FRAME_INFO
PKS_VBI_FRAME_INFO = POINTER(tagKS_VBI_FRAME_INFO)


# Field1, Field2, or Frame; & etc
# Test only?
# Test only?

# The following are for VRAM surface transport to support LDDM Capture

# VRAM_SURFACE_INFO             VramSurfaceInfo;
# ===========================================================================
# Analog video formats, used with:
# Analog Video Decoders
# TVTuners
# Analog Video Encoders

# XXX_STANDARDS_SUPPORTED returns a bitmask
# ===========================================================================
# This is a digital sensor
class KS_AnalogVideoStandard(ENUM):
    KS_AnalogVideo_None = 0x00000000
    KS_AnalogVideo_NTSC_M = 0x00000001
    KS_AnalogVideo_NTSC_M_J = 0x00000002
    KS_AnalogVideo_NTSC_433 = 0x00000004
    KS_AnalogVideo_PAL_B = 0x00000010
    KS_AnalogVideo_PAL_D = 0x00000020
    KS_AnalogVideo_PAL_G = 0x00000040
    KS_AnalogVideo_PAL_H = 0x00000080
    KS_AnalogVideo_PAL_I = 0x00000100
    KS_AnalogVideo_PAL_M = 0x00000200
    KS_AnalogVideo_PAL_N = 0x00000400
    KS_AnalogVideo_PAL_60 = 0x00000800
    KS_AnalogVideo_SECAM_B = 0x00001000
    KS_AnalogVideo_SECAM_D = 0x00002000
    KS_AnalogVideo_SECAM_G = 0x00004000
    KS_AnalogVideo_SECAM_H = 0x00008000
    KS_AnalogVideo_SECAM_K = 0x00010000
    KS_AnalogVideo_SECAM_K1 = 0x00020000
    KS_AnalogVideo_SECAM_L = 0x00040000
    KS_AnalogVideo_SECAM_L1 = 0x00080000
    KS_AnalogVideo_PAL_N_COMBO = 0x00100000


# 75 IRE Setup
# Japan,  0 IRE Setup
# (NTDDI_VERSION >= NTDDI_WINXP)

KS_AnalogVideo_NTSC_Mask = 0x00000007
KS_AnalogVideo_PAL_Mask = 0x00100FF0
# ===========================================================================
KS_AnalogVideo_SECAM_Mask = 0x000FF000
# Property set definitions
# The comments show whether a given property is:
# R  : READ only
# w  : WRITE only
# RW : READ / WRITE
# O  : Optional (return E_UNSUPPORTED if you don't handle this)
# ===========================================================================



# R O (return 2 DWORDs specifying surface size)
class KSPROPERTY_ALLOCATOR_CONTROL(ENUM):
    KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT = 0
    KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE = 1
    KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS = 2
    KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE = 3


# W I (informn a capture driver whether INTerleave capture is possible or
# not - a value of 1 means that INTerleaved capture is supported)
# R O (if value == 1, then the ovmixer will turn on the DDVP_INTERLEAVE
# flag thus allowing INTerleaved capture of the video)
# (NTDDI_VERSION >= NTDDI_WINXP)
# KSPROPERTY Property;

class KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S(ctypes.Structure):
    _fields_ = [
        ('CX', ULONG),
        ('CY', ULONG),
    ]


PKSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S = POINTER(
    KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S
)


# KSPROPERTY Property;

class KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('InterleavedCapSupported', ULONG),
    ]


PKSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S = POINTER(
    KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S
)


# KSPROPERTY Property;

class KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S(ctypes.Structure):
    _fields_ = [
        ('InterleavedCapPossible', ULONG),
    ]


PKSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S = POINTER(
    KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S
)

# ===========================================================================



# RW O
# RW O
class KSPROPERTY_VIDCAP_VIDEOPROCAMP(ENUM):
    KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS = 0
    KSPROPERTY_VIDEOPROCAMP_CONTRAST = 1
    KSPROPERTY_VIDEOPROCAMP_HUE = 2
    KSPROPERTY_VIDEOPROCAMP_SATURATION = 3
    KSPROPERTY_VIDEOPROCAMP_SHARPNESS = 4
    KSPROPERTY_VIDEOPROCAMP_GAMMA = 5
    KSPROPERTY_VIDEOPROCAMP_COLORENABLE = 6
    KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE = 7
    KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION = 8
    KSPROPERTY_VIDEOPROCAMP_GAIN = 9
    KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER = 10
    KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT = 11
    KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT = 12
    KSPROPERTY_VIDEOPROCAMP_POWERLINE_FREQUENCY = 13


class KSPROPERTY_VIDEOPROCAMP_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_VIDEOPROCAMP_S = POINTER(KSPROPERTY_VIDEOPROCAMP_S)


# Value to set or get
# KSPROPERTY_VIDEOPROCAMP_FLAGS_*
# KSPROPERTY_VIDEOPROCAMP_FLAGS_*

class KSPROPERTY_VIDEOPROCAMP_NODE_S(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSP_NODE),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_VIDEOPROCAMP_NODE_S = POINTER(KSPROPERTY_VIDEOPROCAMP_NODE_S)


# Value to set or get
# KSPROPERTY_VIDEOPROCAMP_FLAGS_*
# KSPROPERTY_VIDEOPROCAMP_FLAGS_*

class KSPROPERTY_VIDEOPROCAMP_S2(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value1', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
        ('Value2', LONG),
    ]


PKSPROPERTY_VIDEOPROCAMP_S2 = POINTER(KSPROPERTY_VIDEOPROCAMP_S2)


class KSPROPERTY_VIDEOPROCAMP_NODE_S2(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSP_NODE),
        ('Value1', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
        ('Value2', LONG),
    ]


PKSPROPERTY_VIDEOPROCAMP_NODE_S2 = POINTER(KSPROPERTY_VIDEOPROCAMP_NODE_S2)

KSPROPERTY_VIDEOPROCAMP_FLAGS_AUTO = 0x0001
KSPROPERTY_VIDEOPROCAMP_FLAGS_MANUAL = 0x0002



# RW
# R
class KSPROPERTY_VIDCAP_SELECTOR(ENUM):
    KSPROPERTY_SELECTOR_SOURCE_NODE_ID = 0
    KSPROPERTY_SELECTOR_NUM_SOURCES = 1


PKSPROPERTY_VIDCAP_SELECTOR = POINTER(KSPROPERTY_VIDCAP_SELECTOR)


class KSPROPERTY_SELECTOR_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_SELECTOR_S = POINTER(KSPROPERTY_SELECTOR_S)


# Value to set or get

class KSPROPERTY_SELECTOR_NODE_S(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSP_NODE),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_SELECTOR_NODE_S = POINTER(KSPROPERTY_SELECTOR_NODE_S)

# ===========================================================================



# R  -overall device capabilities
# R  -capabilities in this mode
class KSPROPERTY_TUNER(ENUM):
    KSPROPERTY_TUNER_CAPS = 0
    KSPROPERTY_TUNER_MODE_CAPS = 1
    KSPROPERTY_TUNER_MODE = 2
    KSPROPERTY_TUNER_STANDARD = 3
    KSPROPERTY_TUNER_FREQUENCY = 4
    KSPROPERTY_TUNER_INPUT = 5
    KSPROPERTY_TUNER_STATUS = 6
    KSPROPERTY_TUNER_IF_MEDIUM = 7
    KSPROPERTY_TUNER_SCAN_CAPS = 8
    KSPROPERTY_TUNER_SCAN_STATUS = 9
    KSPROPERTY_TUNER_STANDARD_MODE = 10
    KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS = 11


# RW -set a mode (TV, FM, AM, DSS)
# R  -get TV standard (only if TV mode)
# RW -set/get frequency
# RW -select an input
# R  -tuning status
# R O-Medium for IF or Transport Pin
# R  -overall device capabilities for scanning
# R  -status of scan
# RW -autodetect mode for signal standard
# R -network type specific tuner capabilities

# Tuning support definitions and INTerfaces

# Definitions
class KSPROPERTY_TUNER_MODES(ENUM):
    KSPROPERTY_TUNER_MODE_TV = 0x0001
    KSPROPERTY_TUNER_MODE_FM_RADIO = 0x0002
    KSPROPERTY_TUNER_MODE_AM_RADIO = 0x0004
    KSPROPERTY_TUNER_MODE_DSS = 0x0008
    KSPROPERTY_TUNER_MODE_ATSC = 0x0010


# also used for DVB-T, DVB-C
# Describes how the device tunes.  Only one of these flags may be set
# in KSPROPERTY_TUNER_MODE_CAPS_S.Strategy
# Describe how the driver should attempt to tune:
# EXACT:   just go to the frequency specified (no fine tuning)
# FINE:    (slow) do an exhaustive search for the best signal
# COARSE:  (fast) use larger frequency jumps to just determine if any signal
# No fine tuning
# Fine grained search

class KS_TUNER_TUNING_FLAGS(ENUM):
    KS_TUNER_TUNING_EXACT = 1
    KS_TUNER_TUNING_FINE = 2
    KS_TUNER_TUNING_COARSE = 3


# Coarse search
# Tune by PLL offset
# Tune by signal strength

class KS_TUNER_STRATEGY(ENUM):
    KS_TUNER_STRATEGY_PLL = 0x01
    KS_TUNER_STRATEGY_SIGNAL_STRENGTH = 0x02
    KS_TUNER_STRATEGY_DRIVER_TUNES = 0x04


# Driver does fine tuning
# Tuning operations

class KSPROPERTY_TUNER_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('ModesSupported', ULONG),
        ('VideoMedium', KSPIN_MEDIUM),
        ('TVAudioMedium', KSPIN_MEDIUM),
        ('RadioAudioMedium', KSPIN_MEDIUM),
    ]


PKSPROPERTY_TUNER_CAPS_S = POINTER(KSPROPERTY_TUNER_CAPS_S)


# KS_PROPERTY_TUNER_MODES_*
# GUID_NULL (no pin), or GUID
# GUID_NULL (no pin), or GUID
# GUID_NULL (no pin), or GUID

class KSPROPERTY_TUNER_IF_MEDIUM_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('IFMedium', KSPIN_MEDIUM),
    ]


PKSPROPERTY_TUNER_IF_MEDIUM_S = POINTER(KSPROPERTY_TUNER_IF_MEDIUM_S)


# GUID_NULL (no pin), or GUID

class KSPROPERTY_TUNER_MODE_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Mode', ULONG),
        ('StandardsSupported', ULONG),
        ('MinFrequency', ULONG),
        ('MaxFrequency', ULONG),
        ('TuningGranularity', ULONG),
        ('NumberOfInputs', ULONG),
        ('SettlingTime', ULONG),
        ('Strategy', ULONG),
    ]


PKSPROPERTY_TUNER_MODE_CAPS_S = POINTER(KSPROPERTY_TUNER_MODE_CAPS_S)


# IN: KSPROPERTY_TUNER_MODE
# KS_AnalogVideo_* (if TV or DSS)
# Hz
# Hz
# Hz
# count of inputs
# milliSeconds
# KS_TUNER_STRATEGY

class KSPROPERTY_TUNER_MODE_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Mode', ULONG),
    ]


PKSPROPERTY_TUNER_MODE_S = POINTER(KSPROPERTY_TUNER_MODE_S)


# IN: KSPROPERTY_TUNER_MODE

class KSPROPERTY_TUNER_FREQUENCY_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Frequency', ULONG),
        ('LastFrequency', ULONG),
        ('TuningFlags', ULONG),
        ('VideoSubChannel', ULONG),
        ('AudioSubChannel', ULONG),
        ('Channel', ULONG),
        ('Country', ULONG),
    ]


PKSPROPERTY_TUNER_FREQUENCY_S = POINTER(KSPROPERTY_TUNER_FREQUENCY_S)


# Hz
# Hz (last known good)
# KS_TUNER_TUNING_FLAGS
# DSS
# DSS
# VBI decoders
# VBI decoders

class KSPROPERTY_TUNER_STANDARD_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Standard', ULONG),
    ]


PKSPROPERTY_TUNER_STANDARD_S = POINTER(KSPROPERTY_TUNER_STANDARD_S)


# KS_AnalogVideo_*

class KSPROPERTY_TUNER_STANDARD_MODE_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('AutoDetect', BOOL),
    ]


PKSPROPERTY_TUNER_STANDARD_MODE_S = POINTER(KSPROPERTY_TUNER_STANDARD_MODE_S)


# RW - specifies whether the driver is in auto-detect mode for the signal
# standard

class KSPROPERTY_TUNER_INPUT_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('InputIndex', ULONG),
    ]


PKSPROPERTY_TUNER_INPUT_S = POINTER(KSPROPERTY_TUNER_INPUT_S)


# 0 to (n-1) inputs

class KSPROPERTY_TUNER_STATUS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('CurrentFrequency', ULONG),
        ('PLLOffset', ULONG),
        ('SignalStrength', ULONG),
        ('Busy', ULONG),
    ]


PKSPROPERTY_TUNER_STATUS_S = POINTER(KSPROPERTY_TUNER_STATUS_S)


# Hz
# if Strategy.KS_TUNER_STRATEGY_PLL
# if Stretegy.KS_TUNER_STRATEGY_SIGNAL_STRENGTH
# TRUE if in the process of tuning

# Exhaustive Scanning tuner support definitions and INTerfaces

# Definitions
# Not locked on a signal. Can be returned at end of scan.
# Signal is near by, not able to report exact frequency. Can be returned at
# end of scan.
class _TunerDecoderLockType(ENUM):
    Tuner_LockType_None = 0x00
    Tuner_LockType_Within_Scan_Sensing_Range = 0x01
    Tuner_LockType_Locked = 0x02


TunerLockType = _TunerDecoderLockType


# Fine tune signal lock established. Can be returned at end of scan.
# Data structures returned for KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S
# operations
# IN -KSPROPERTY_TUNER_MODE

class TUNER_ANALOG_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Mode', ULONG),
        ('StandardsSupported', ULONG),
        ('MinFrequency', ULONG),
        ('MaxFrequency', ULONG),
        ('TuningGranularity', ULONG),
        ('SettlingTime', ULONG),
        ('ScanSensingRange', ULONG),
        ('FineTuneSensingRange', ULONG),
    ]


PTUNER_ANALOG_CAPS_S = POINTER(TUNER_ANALOG_CAPS_S)


# KS_AnalogVideo_* (defined in KS_AnalogVideoStandard)
# R -Hz
# R -Hz
# R -Hz
# R -milliSeconds
# R -max range (Hz) in which tuner can detect presence of a signal
# R -max range (Hz) in which tuner can detect actual frequency of a signal
# ...
# More to come if new structures are needed for different network types.



# initiate frequency scan
class KSEVENT_TUNER(ENUM):
    KSEVENT_TUNER_CHANGED = 0
    KSEVENT_TUNER_INITIATE_SCAN = 1


# Exhaustive Scanning operations
# Determine if ES is possible with device

class KSPROPERTY_TUNER_SCAN_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('fSupportsHardwareAssistedScanning', BOOL),
        ('SupportedBroadcastStandards', ULONG),
        ('GUIDBucket', PVOID),
        ('lengthofBucket', ULONG),
    ]


PKSPROPERTY_TUNER_SCAN_CAPS_S = POINTER(KSPROPERTY_TUNER_SCAN_CAPS_S)


# R
# R
# RW
# R
# Get specific network type capabilities structure (such as
# TUNER_ANALOG_CAPS_S for example)

class KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NetworkType', GUID),
        ('BufferSize', ULONG),
        ('NetworkTunerCapabilities', PVOID),
    ]


PKSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S = POINTER(
    KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S
)


# R  -one of the INTerested GUIDs returned in KSPROPERTY_TUNER_SCAN_CAPS_S
# R  -size of the buffer;
# RW -Buffer
# Obtain current scan operation status

class KSPROPERTY_TUNER_SCAN_STATUS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('LockStatus', TunerLockType),
        ('CurrentFrequency', ULONG),
    ]


PKSPROPERTY_TUNER_SCAN_STATUS_S = POINTER(KSPROPERTY_TUNER_SCAN_STATUS_S)


# R -none, within scan sensing range, or locked
# R -current frequency
# Start a scan

class KSEVENT_TUNER_INITIATE_SCAN_S(ctypes.Structure):
    _fields_ = [
        ('EventData', KSEVENTDATA),
        ('StartFrequency', ULONG),
        ('EndFrequency', ULONG),
    ]


PKSEVENT_TUNER_INITIATE_SCAN_S = POINTER(KSEVENT_TUNER_INITIATE_SCAN_S)


# W -initial frequency for the scan
# W -final frequency for the scan


# Kernel Streaming Video node type definitions

# USB Video Class Definitions









# R
# RW
class KSPROPERTY_VIDCAP_VIDEOENCODER(ENUM):
    KSPROPERTY_VIDEOENCODER_CAPS = 0
    KSPROPERTY_VIDEOENCODER_STANDARD = 1
    KSPROPERTY_VIDEOENCODER_COPYPROTECTION = 2
    KSPROPERTY_VIDEOENCODER_CC_ENABLE = 3


# RW O
# RW O

class KSPROPERTY_VIDEOENCODER_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_VIDEOENCODER_S = POINTER(KSPROPERTY_VIDEOENCODER_S)

# ===========================================================================



# R
# RW
class KSPROPERTY_VIDCAP_VIDEODECODER(ENUM):
    KSPROPERTY_VIDEODECODER_CAPS = 0
    KSPROPERTY_VIDEODECODER_STANDARD = 1
    KSPROPERTY_VIDEODECODER_STATUS = 2
    KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE = 3
    KSPROPERTY_VIDEODECODER_VCR_TIMING = 4
    KSPROPERTY_VIDEODECODER_STATUS2 = 5


# R
# Rw O
# RW O
# R
# VP Output can tri-stae
# VCR PLL timings
class KS_VIDEODECODER_FLAGS(ENUM):
    KS_VIDEODECODER_FLAGS_CAN_DISABLE_OUTPUT = 0x0001
    KS_VIDEODECODER_FLAGS_CAN_USE_VCR_LOCKING = 0x0002
    KS_VIDEODECODER_FLAGS_CAN_INDICATE_LOCKED = 0x0004


# Can indicate valid signal

class KSPROPERTY_VIDEODECODER_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StandardsSupported', ULONG),
        ('Capabilities', ULONG),
        ('SettlingTime', ULONG),
        ('HSyncPerVSync', ULONG),
    ]


PKSPROPERTY_VIDEODECODER_CAPS_S = POINTER(KSPROPERTY_VIDEODECODER_CAPS_S)


# KS_AnalogVideo_*
# KS_VIDEODECODER_FLAGS_*
# milliseconds
# Number of HSync Pulses per VSync

class KSPROPERTY_VIDEODECODER_STATUS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NumberOfLines', ULONG),
        ('SignalLocked', ULONG),
    ]


PKSPROPERTY_VIDEODECODER_STATUS_S = POINTER(KSPROPERTY_VIDEODECODER_STATUS_S)


# 525 or 625 lines detected
# TRUE if signal is locked

class KSPROPERTY_VIDEODECODER_STATUS2_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NumberOfLines', ULONG),
        ('SignalLocked', ULONG),
        ('ChromaLock', ULONG),
    ]


PKSPROPERTY_VIDEODECODER_STATUS2_S = POINTER(KSPROPERTY_VIDEODECODER_STATUS2_S)


# R - 525 or 625 lines detected
# R - TRUE if signal is locked
# R - TRUE if a chroma signal is present

class KSPROPERTY_VIDEODECODER_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value', ULONG),
    ]


PKSPROPERTY_VIDEODECODER_S = POINTER(KSPROPERTY_VIDEODECODER_S)



class KSEVENT_VIDEODECODER(ENUM):
    KSEVENT_VIDEODECODER_CHANGED = 0



class KSEVENT_CAMERACONTROL(ENUM):
    KSEVENT_CAMERACONTROL_FOCUS = 0
    KSEVENT_CAMERACONTROL_ZOOM = 1



# RW O
# RW O
class KSPROPERTY_VIDCAP_CAMERACONTROL(ENUM):
    KSPROPERTY_CAMERACONTROL_PAN = 0
    KSPROPERTY_CAMERACONTROL_TILT = 1
    KSPROPERTY_CAMERACONTROL_ROLL = 2
    KSPROPERTY_CAMERACONTROL_ZOOM = 3
    KSPROPERTY_CAMERACONTROL_EXPOSURE = 4
    KSPROPERTY_CAMERACONTROL_IRIS = 5
    KSPROPERTY_CAMERACONTROL_FOCUS = 6
    KSPROPERTY_CAMERACONTROL_SCANMODE = 7
    KSPROPERTY_CAMERACONTROL_PRIVACY = 8
    KSPROPERTY_CAMERACONTROL_PANTILT = 9
    KSPROPERTY_CAMERACONTROL_PAN_RELATIVE = 10
    KSPROPERTY_CAMERACONTROL_TILT_RELATIVE = 11
    KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE = 12
    KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE = 13
    KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE = 14
    KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE = 15
    KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE = 16
    KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE = 17
    KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH = 18
    KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY = 19


# XP SP2 and later (chronologically)
class KS_CameraControlAsyncOperation(ENUM):
    KS_CAMERACONTROL_ASYNC_START = 0x0001
    KS_CAMERACONTROL_ASYNC_STOP = 0x0002
    KS_CAMERACONTROL_ASYNC_RESET = 0x0003


class KSPROPERTY_CAMERACONTROL_S_EX(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
        ('FocusRect', RECT),
    ]


PKSPROPERTY_CAMERACONTROL_S_EX = POINTER(KSPROPERTY_CAMERACONTROL_S_EX)


# value to get or set
# KSPROPERTY_CAMERACONTROL_FLAGS_*
# KSPROPERTY_CAMERACONTROL_FLAGS_*

class KSPROPERTY_CAMERACONTROL_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_CAMERACONTROL_S = POINTER(KSPROPERTY_CAMERACONTROL_S)


# value to get or set
# KSPROPERTY_CAMERACONTROL_FLAGS_*
# KSPROPERTY_CAMERACONTROL_FLAGS_*
KSPROPERTY_CAMERACONTROL_FLAGS_AUTO = 0x0001
KSPROPERTY_CAMERACONTROL_FLAGS_MANUAL = 0x0002
KSPROPERTY_CAMERACONTROL_FLAGS_ASYNCHRONOUS = 0x0004
KSPROPERTY_CAMERACONTROL_FLAGS_ABSOLUTE = 0x0000
KSPROPERTY_CAMERACONTROL_FLAGS_RELATIVE = 0x0010


class KSPROPERTY_CAMERACONTROL_NODE_S(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSP_NODE),
        ('Value', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_CAMERACONTROL_NODE_S = KSPROPERTY_CAMERACONTROL_NODE_S


# value to get or set
# KSPROPERTY_CAMERACONTROL_FLAGS_*
# KSPROPERTY_CAMERACONTROL_FLAGS_*

class KSPROPERTY_CAMERACONTROL_S2(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Value1', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
        ('Value2', LONG),
    ]


PKSPROPERTY_CAMERACONTROL_S2 = POINTER(KSPROPERTY_CAMERACONTROL_S2)


class KSPROPERTY_CAMERACONTROL_NODE_S2(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSP_NODE),
        ('Value1', LONG),
        ('Flags', ULONG),
        ('Capabilities', ULONG),
        ('Value2', LONG),
    ]


PKSPROPERTY_CAMERACONTROL_NODE_S2 = POINTER(KSPROPERTY_CAMERACONTROL_NODE_S2)


class KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('lOcularFocalLength', LONG),
        ('lObjectiveFocalLengthMin', LONG),
        ('lObjectiveFocalLengthMax', LONG),
    ]


PKSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S = POINTER(
    KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S
)


class KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSNODEPROPERTY),
        ('lOcularFocalLength', LONG),
        ('lObjectiveFocalLengthMin', LONG),
        ('lObjectiveFocalLengthMax', LONG),
    ]


PKSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S = POINTER(
    KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S
)



class KSPROPERTY_CAMERACONTROL_FLASH(ENUM):
    KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY_ID = 0


KSPROPERTY_CAMERACONTROL_FLASH_OFF = 0x00000000
KSPROPERTY_CAMERACONTROL_FLASH_ON = 0x00000001
KSPROPERTY_CAMERACONTROL_FLASH_AUTO = 0x00000002
KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_AUTO = 0x00000001
KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_MANUAL = 0x00000002


class KSPROPERTY_CAMERACONTROL_FLASH_S(ctypes.Structure):
    _fields_ = [
        ('Flash', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_CAMERACONTROL_FLASH_S = POINTER(KSPROPERTY_CAMERACONTROL_FLASH_S)



class KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE(ENUM):
    KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY_ID = 0


KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_OFF = 0x00000000
KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_HIGH = 0x00000001
KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_MEDIUM = 0x00000002
KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_LOW = 0x00000003
KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_AUTO = 0x00000004
KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_AUTO = 0x00000001
KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_MANUAL = 0x00000002


class KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S(ctypes.Structure):
    _fields_ = [
        ('VideoStabilizationMode', ULONG),
        ('Capabilities', ULONG),
    ]


PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S = POINTER(
    KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S
)



class KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST(ENUM):
    KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_PROPERTY_ID = 0


KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_AUTO = 0x00000001
KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_MANUAL = 0x00000002
KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_ASYNC = 0x80000000
KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_FOCUS = 0x00000100
KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_EXPOSURE = 0x00000200
KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_WB = 0x00000400
KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONVERGEMODE = 0x40000000



class KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('Capabilities', ULONG),
            ('Configuration', ULONG),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('FocusRect', RECT),
        ('AutoFocusLock', BOOL),
        ('AutoExposureLock', BOOL),
        ('AutoWhitebalanceLock', BOOL),
        ('_Union_0', _Union_0),
    ]


PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S = POINTER(
    KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S
)



class KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY(ENUM):
    KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_PROPERTY_ID = 0


KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_EXCLUSIVE_WITH_RECORD = (
    0x00000001
)
KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_SEQUENCE_EXCLUSIVE_WITH_RECORD = (
    0x00000002
)


class KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S(ctypes.Structure):
    _fields_ = [
        ('Capabilities', ULONG),
        ('Reserved0', ULONG),
    ]


PKSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S = POINTER(
    KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S
)


# 0
# 1
class KSPROPERTY_CAMERACONTROL_EXTENDED_PROPERTY(ENUM):
    KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE = 0
    KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOFRAMERATE = 1
    KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMAXFRAMERATE = 2
    KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTRIGGERTIME = 3
    KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART = 4
    KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES = 5
    KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL = 6
    KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE = 7
    KSPROPERTY_CAMERACONTROL_EXTENDED_TORCHMODE = 8
    KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE = 9
    KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT = 10
    KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE = 11
    KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE = 12
    KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE = 13
    KSPROPERTY_CAMERACONTROL_EXTENDED_ISO = 14
    KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW = 15
    KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION = 16
    KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET = 17
    KSPROPERTY_CAMERACONTROL_EXTENDED_METADATA = 18
    KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSPRIORITY = 19
    KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSSTATE = 20
    KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_CONFIGCAPS = 21
    KSPROPERTY_CAMERACONTROL_EXTENDED_ROI_ISPCONTROL = 22
    KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION = 23
    KSPROPERTY_CAMERACONTROL_EXTENDED_ZOOM = 24
    KSPROPERTY_CAMERACONTROL_EXTENDED_MCC = 25
    KSPROPERTY_CAMERACONTROL_EXTENDED_ISO_ADVANCED = 26
    KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOSTABILIZATION = 28
    KSPROPERTY_CAMERACONTROL_EXTENDED_VFR = 29
    KSPROPERTY_CAMERACONTROL_EXTENDED_FACEDETECTION = 30
    KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR = 31
    KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM = 32
    KSPROPERTY_CAMERACONTROL_EXTENDED_OIS = 33
    KSPROPERTY_CAMERACONTROL_EXTENDED_ADVANCEDPHOTO = 34
    KSPROPERTY_CAMERACONTROL_EXTENDED_PROFILE = 35
    KSPROPERTY_CAMERACONTROL_EXTENDED_FACEAUTH_MODE = 37
    KSPROPERTY_CAMERACONTROL_EXTENDED_SECURE_MODE = 39
    KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOTEMPORALDENOISING = 40
    KSPROPERTY_CAMERACONTROL_EXTENDED_END = 42
    KSPROPERTY_CAMERACONTROL_EXTENDED_END2 = (
        KSPROPERTY_CAMERACONTROL_EXTENDED_END
    )


KSCAMERA_EXTENDEDPROP_FILTERSCOPE = 0xFFFFFFFF
KSCAMERA_EXTENDEDPROP_CAPS_RESERVED = (
    0xFF00000000000000
)
KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL = (
    0x8000000000000000
)
KSCAMERA_EXTENDEDPROP_CAPS_CANCELLABLE = (
    0x4000000000000000
)
# This mask represents the reserved bits for all capability flags.  All
# EXTENDEDPROP capability
KSCAMERA_EXTENDEDPROP_FLAG_CANCELOPERATION = (
    0x8000000000000000
)
# flags defined below must NOT use the upper 8 bits.
# Same applies to the flags.
KSCAMERA_EXTENDEDPROP_CAPS_MASK = (
    0xFF00000000000000
)
KSCAMERA_EXTENDEDPROP_FLAG_MASK = (
    0xFF00000000000000
)
KSCAMERA_EXTENDEDPROP_PHOTOMODE_NORMAL = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_WARMSTART_MODE_DISABLED = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_WARMSTART_MODE_ENABLED = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_DISABLE = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_2X = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_4X = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_8X = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_16X = (
    0x00000008
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_AUTO = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_MACRO = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_PORTRAIT = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_SPORT = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_SNOW = (
    0x00000008
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_NIGHT = (
    0x00000010
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_BEACH = (
    0x00000020
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_SUNSET = (
    0x00000040
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_CANDLELIGHT = (
    0x00000080
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_LANDSCAPE = (
    0x00000100
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_NIGHTPORTRAIT = (
    0x00000200
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_BACKLIT = (
    0x00000400
)
KSCAMERA_EXTENDEDPROP_SCENEMODE_MANUAL = (
    0x0080000000000000
)
KSCAMERA_EXTENDEDPROP_VIDEOTORCH_OFF = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_VIDEOTORCH_ON = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_VIDEOTORCH_ON_ADJUSTABLEPOWER = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_FLASH_OFF = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_FLASH_ON = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_FLASH_ON_ADJUSTABLEPOWER = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_FLASH_AUTO = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_FLASH_AUTO_ADJUSTABLEPOWER = (
    0x00000008
)
KSCAMERA_EXTENDEDPROP_FLASH_REDEYEREDUCTION = (
    0x00000010
)
KSCAMERA_EXTENDEDPROP_FLASH_SINGLEFLASH = (
    0x00000020
)
KSCAMERA_EXTENDEDPROP_FLASH_MULTIFLASHSUPPORTED = (
    0x00000040
)
KSCAMERA_EXTENDEDPROP_FLASH_MODE_MASK = (
    KSCAMERA_EXTENDEDPROP_FLASH_ON |
    KSCAMERA_EXTENDEDPROP_FLASH_ON_ADJUSTABLEPOWER |
    KSCAMERA_EXTENDEDPROP_FLASH_AUTO |
    KSCAMERA_EXTENDEDPROP_FLASH_AUTO_ADJUSTABLEPOWER
)
KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PHOTO = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_OPTIMIZATION_VIDEO = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_OPTIMIZATION_DEFAULT = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_OPTIMIZATION_QUALITY = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_OPTIMIZATION_LATENCY = (
    0x00000008
)
KSCAMERA_EXTENDEDPROP_OPTIMIZATION_POWER = (
    0x00000010
)
KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PERF_MASK = (
    KSCAMERA_EXTENDEDPROP_OPTIMIZATION_QUALITY |
    KSCAMERA_EXTENDEDPROP_OPTIMIZATION_LATENCY |
    KSCAMERA_EXTENDEDPROP_OPTIMIZATION_POWER
)

KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PRIMARYUSE_MASK = (
    KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PHOTO |
     KSCAMERA_EXTENDEDPROP_OPTIMIZATION_VIDEO
)
KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MANUAL = (
    0x00000002
)
# This combines the generic Video Proc bits shared by all video proc controls.
KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MASK = (
    KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO |
    KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MANUAL |
    KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK
)


class KSCAMERA_EXTENDEDPROP_WHITEBALANCE_MODE(ENUM):
    KSCAMERA_EXTENDEDPROP_WHITEBALANCE_TEMPERATURE = 1
    KSCAMERA_EXTENDEDPROP_WHITEBALANCE_PRESET = 2


class KSCAMERA_EXTENDEDPROP_WBPRESET(ENUM):
    KSCAMERA_EXTENDEDPROP_WBPRESET_CLOUDY = 1
    KSCAMERA_EXTENDEDPROP_WBPRESET_DAYLIGHT = 2
    KSCAMERA_EXTENDEDPROP_WBPRESET_FLASH = 3
    KSCAMERA_EXTENDEDPROP_WBPRESET_FLUORESCENT = 4
    KSCAMERA_EXTENDEDPROP_WBPRESET_TUNGSTEN = 5
    KSCAMERA_EXTENDEDPROP_WBPRESET_CANDLELIGHT = 6


# Focus control extends the generic video proc mask by adding the continous
# flag.
KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUS = (
    0x00000100
)
KSCAMERA_EXTENDEDPROP_FOCUS_MODE_MASK = (
    KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MASK |
    KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUS
)
KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_MACRO = (
    0x00010000
)
KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_NORMAL = (
    0x00020000
)
KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_FULLRANGE = (
    0x00040000
)
KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_INFINITY = (
    0x00080000
)
KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_HYPERFOCAL = (
    0x00100000
)
KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_MASK = (
    KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_MACRO |
    KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_NORMAL |
    KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_FULLRANGE |
    KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_INFINITY |
    KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_HYPERFOCAL
)
# Spare bits 0x200000 - 0x800000 in case of future range expansion
KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_INFINITY = (
    0x01000000
)
KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_HYPERFOCAL = (
    0x02000000
)
KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_NEAREST = (
    0x04000000
)
KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_MASK = (
    KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_INFINITY |
    KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_HYPERFOCAL |
    KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_NEAREST
)
# (NTDDI_VERSION >= NTDDI_WINBLUE)
KSCAMERA_EXTENDEDPROP_ISO_AUTO = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_ISO_50 = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_ISO_80 = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_ISO_100 = (
    0x00000008
)
KSCAMERA_EXTENDEDPROP_ISO_200 = (
    0x00000010
)
KSCAMERA_EXTENDEDPROP_ISO_400 = (
    0x00000020
)
KSCAMERA_EXTENDEDPROP_ISO_800 = (
    0x00000040
)
KSCAMERA_EXTENDEDPROP_ISO_1600 = (
    0x00000080
)
KSCAMERA_EXTENDEDPROP_ISO_3200 = (
    0x00000100
)
KSCAMERA_EXTENDEDPROP_ISO_6400 = (
    0x00000200
)
KSCAMERA_EXTENDEDPROP_ISO_12800 = (
    0x00000400
)
KSCAMERA_EXTENDEDPROP_ISO_25600 = (
    0x00000800
)
KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUSLOCK = (
    0x00000200
)
KSCAMERA_EXTENDEDPROP_FOCUS_UNLOCK = (
    0x00000400
)
KSCAMERA_EXTENDEDPROP_FOCUS_DRIVERFALLBACK_OFF = (
    0x00000800
)
KSCAMERA_EXTENDEDPROP_FOCUS_REGIONBASED = (
    0x00001000
)
KSCAMERA_EXTENDEDPROP_FOCUS_MODE_ADVANCED_MASK = (
    KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUSLOCK |
    KSCAMERA_EXTENDEDPROP_FOCUS_UNLOCK |
    KSCAMERA_EXTENDEDPROP_FOCUS_DRIVERFALLBACK_OFF |
    KSCAMERA_EXTENDEDPROP_FOCUS_REGIONBASED
)
KSCAMERA_EXTENDEDPROP_ISO_MANUAL = (
    0x80000000000000
)
KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_OFF = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_ON = (
    0x00000080
)
KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_AUTO = (
    0x00000100
)
KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_MASK = (
    KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_ON |
    KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_AUTO
)
# (NTDDI_VERSION >= NTDDI_WINBLUE)
KSCAMERA_EXTENDEDPROP_EVCOMP_SIXTHSTEP = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_EVCOMP_QUARTERSTEP = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_EVCOMP_THIRDSTEP = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_EVCOMP_HALFSTEP = (
    0x00000008
)
KSCAMERA_EXTENDEDPROP_EVCOMP_FULLSTEP = (
    0x00000010
)


class KSPROPERTY_CAMERA_PHOTOTRIGGERTIME_FLAGS(ENUM):
    KSPROPERTY_CAMERA_PHOTOTRIGGERTIME_CLEAR = 0
    KSPROPERTY_CAMERA_PHOTOTRIGGERTIME_SET = 1


class tagKSCAMERA_EXTENDEDPROP_HEADER(ctypes.Structure):
    _fields_ = [
        ('Version', ULONG),
        ('PinId', ULONG),
        ('Size', ULONG),
        ('Result', ULONG),
        ('Flags', ULONGLONG),
        ('Capability', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_HEADER = tagKSCAMERA_EXTENDEDPROP_HEADER
PKSCAMERA_EXTENDEDPROP_HEADER = POINTER(tagKSCAMERA_EXTENDEDPROP_HEADER)


class tagKSCAMERA_EXTENDEDPROP_VALUE(ctypes.Structure):

    class Value(ctypes.Union):
        _fields_ = [
            ('dbl', DOUBLE),
            ('ull', ULONGLONG),
            ('ul', ULONG),
            ('ratio', ULARGE_INTEGER),
            ('l', LONG),
            ('ll', LONGLONG),
        ]

    _fields_ = [
        ('Value', Value),
    ]


KSCAMERA_EXTENDEDPROP_VALUE = tagKSCAMERA_EXTENDEDPROP_VALUE
PKSCAMERA_EXTENDEDPROP_VALUE = POINTER(tagKSCAMERA_EXTENDEDPROP_VALUE)


# This is the payload structure fo the Maximum video sensor frame rate possible
# based on the photo resolution being programmed on the sensor.  The PhotoRes
# fields
# are provided by the application, the preview/capture FPS fields are filled in
# by the driver to indicate the maximum sensor frame rate.

class tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES(ctypes.Structure):
    _fields_ = [
        ('PhotoResWidth', ULONG),
        ('PhotoResHeight', ULONG),
        ('PreviewFPSNum', ULONG),
        ('PreviewFPSDenom', ULONG),
        ('CaptureFPSNum', ULONG),
        ('CaptureFPSDenom', ULONG),
    ]


KSCAMERA_MAXVIDEOFPS_FORPHOTORES = tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES
PKSCAMERA_MAXVIDEOFPS_FORPHOTORES = POINTER(
    tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES
)


KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_NONE = 0x00000000
KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_VARIABLE = 0x00000001


class tagKSCAMERA_EXTENDEDPROP_PHOTOMODE(ctypes.Structure):
    _fields_ = [
        ('RequestedHistoryFrames', ULONG),
        ('MaxHistoryFrames', ULONG),
        ('SubMode', ULONG),
        ('Reserved', ULONG),
    ]


KSCAMERA_EXTENDEDPROP_PHOTOMODE = tagKSCAMERA_EXTENDEDPROP_PHOTOMODE
PKSCAMERA_EXTENDEDPROP_PHOTOMODE = POINTER(tagKSCAMERA_EXTENDEDPROP_PHOTOMODE)


class tagKSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING(ctypes.Structure):
    _fields_ = [
        ('Mode', ULONG),
        ('Min', LONG),
        ('Max', LONG),
        ('Step', LONG),
        ('VideoProc', KSCAMERA_EXTENDEDPROP_VALUE),
        ('Reserved', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING = (
    tagKSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING
)
PKSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING = POINTER(
    tagKSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING
)


class tagKSCAMERA_EXTENDEDPROP_EVCOMPENSATION(ctypes.Structure):
    _fields_ = [
        ('Mode', ULONG),
        ('Min', LONG),
        ('Max', LONG),
        ('Value', LONG),
        ('Reserved', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_EVCOMPENSATION = tagKSCAMERA_EXTENDEDPROP_EVCOMPENSATION
PKSCAMERA_EXTENDEDPROP_EVCOMPENSATION = POINTER(
    tagKSCAMERA_EXTENDEDPROP_EVCOMPENSATION
)


class tagKSCAMERA_EXTENDEDPROP_FIELDOFVIEW(ctypes.Structure):
    _fields_ = [
        ('NormalizedFocalLengthX', ULONG),
        ('NormalizedFocalLengthY', ULONG),
        ('Flag', ULONG),
        ('Reserved', ULONG),
    ]


KSCAMERA_EXTENDEDPROP_FIELDOFVIEW = tagKSCAMERA_EXTENDEDPROP_FIELDOFVIEW
PKSCAMERA_EXTENDEDPROP_FIELDOFVIEW = POINTER(
    tagKSCAMERA_EXTENDEDPROP_FIELDOFVIEW
)


class tagKSCAMERA_EXTENDEDPROP_CAMERAOFFSET(ctypes.Structure):
    _fields_ = [
        ('PitchAngle', LONG),
        ('YawAngle', LONG),
        ('Flag', ULONG),
        ('Reserved', ULONG),
    ]


KSCAMERA_EXTENDEDPROP_CAMERAOFFSET = tagKSCAMERA_EXTENDEDPROP_CAMERAOFFSET
PKSCAMERA_EXTENDEDPROP_CAMERAOFFSET = POINTER(
    tagKSCAMERA_EXTENDEDPROP_CAMERAOFFSET
)


# Metadata
# Required alignment for metadata buffer

class tagKSCAMERA_EXTENDEDPROP_METADATAINFO(ctypes.Structure):
    _fields_ = [
        ('BufferAlignment', LONG),
        ('MaxMetadataBufferSize', ULONG),
    ]


KSCAMERA_EXTENDEDPROP_METADATAINFO = tagKSCAMERA_EXTENDEDPROP_METADATAINFO
PKSCAMERA_EXTENDEDPROP_METADATAINFO = POINTER(
    tagKSCAMERA_EXTENDEDPROP_METADATAINFO
)


# Required metadata buffer size
# Aligned at 16 bytes
class KSCAMERA_EXTENDEDPROP_MetadataAlignment(ENUM):
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_16 = 4
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_32 = 5
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_64 = 6
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_128 = 7
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_256 = 8
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_512 = 9
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024 = 10
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048 = 11
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096 = 12
    KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192 = 13


KSCAMERA_EXTENDEDPROP_METADATA_MEMORYTYPE_MASK = (
    0x000000FF
)
KSCAMERA_EXTENDEDPROP_METADATA_SYSTEMMEMORY = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_METADATA_ALIGNMENTREQUIRED = (
    0x00000100
)


class KSCAMERA_MetadataId(ENUM):
    MetadataId_Standard_Start = 1
    MetadataId_PhotoConfirmation = MetadataId_Standard_Start
    MetadataId_UsbVideoHeader = 2
    MetadataId_CaptureStats = 3
    MetadataId_CameraExtrinsics = 4
    MetadataId_CameraIntrinsics = 5
    MetadataId_FrameIllumination = 6
    MetadataId_Standard_End = MetadataId_FrameIllumination
    MetadataId_Custom_Start = 0x80000000


class tagKSCAMERA_METADATA_ITEMHEADER(ctypes.Structure):
    _fields_ = [
        ('MetadataId', ULONG),
        ('Size', ULONG),
    ]


KSCAMERA_METADATA_ITEMHEADER = tagKSCAMERA_METADATA_ITEMHEADER
PKSCAMERA_METADATA_ITEMHEADER = POINTER(tagKSCAMERA_METADATA_ITEMHEADER)


# Size of this header + metadata payload following

class tagKSCAMERA_METADATA_PHOTOCONFIRMATION(ctypes.Structure):
    _fields_ = [
        ('Header', KSCAMERA_METADATA_ITEMHEADER),
        ('PhotoConfirmationIndex', ULONG),
        ('Reserved', ULONG),
    ]


KSCAMERA_METADATA_PHOTOCONFIRMATION = tagKSCAMERA_METADATA_PHOTOCONFIRMATION
PKSCAMERA_METADATA_PHOTOCONFIRMATION = POINTER(
    tagKSCAMERA_METADATA_PHOTOCONFIRMATION
)


class tagKSCAMERA_METADATA_FRAMEILLUMINATION(ctypes.Structure):
    _fields_ = [
        ('Header', KSCAMERA_METADATA_ITEMHEADER),
        ('Flags', ULONG),
        ('Reserved', ULONG),
    ]


KSCAMERA_METADATA_FRAMEILLUMINATION = tagKSCAMERA_METADATA_FRAMEILLUMINATION
PKSCAMERA_METADATA_FRAMEILLUMINATION = POINTER(
    tagKSCAMERA_METADATA_FRAMEILLUMINATION
)


KSCAMERA_METADATA_FRAMEILLUMINATION_FLAG_ON = 0x00000001


class tagKSCAMERA_METADATA_CAPTURESTATS(ctypes.Structure):
    _fields_ = [
        ('Header', KSCAMERA_METADATA_ITEMHEADER),
        ('Flags', ULONG),
        ('Reserved', ULONG),
        ('ExposureTime', ULONGLONG),
        ('ExposureCompensationFlags', ULONGLONG),
        ('ExposureCompensationValue', LONG),
        ('IsoSpeed', ULONG),
        ('FocusState', ULONG),
        ('LensPosition', ULONG),
        ('WhiteBalance', ULONG),
        ('Flash', ULONG),
        ('FlashPower', ULONG),
        ('ZoomFactor', ULONG),
        ('SceneMode', ULONGLONG),
        ('SensorFramerate', ULONGLONG),
    ]


KSCAMERA_METADATA_CAPTURESTATS = tagKSCAMERA_METADATA_CAPTURESTATS
PKSCAMERA_METADATA_CAPTURESTATS = POINTER(tagKSCAMERA_METADATA_CAPTURESTATS)


# a.k.a Focus
KSCAMERA_METADATA_CAPTURESTATS_FLAG_EXPOSURETIME = 0x00000001
KSCAMERA_METADATA_CAPTURESTATS_FLAG_EXPOSURECOMPENSATION = 0x00000002
KSCAMERA_METADATA_CAPTURESTATS_FLAG_ISOSPEED = 0x00000004
KSCAMERA_METADATA_CAPTURESTATS_FLAG_FOCUSSTATE = 0x00000008
KSCAMERA_METADATA_CAPTURESTATS_FLAG_LENSPOSITION = 0x00000010
KSCAMERA_METADATA_CAPTURESTATS_FLAG_WHITEBALANCE = 0x00000020
KSCAMERA_METADATA_CAPTURESTATS_FLAG_FLASH = 0x00000040
KSCAMERA_METADATA_CAPTURESTATS_FLAG_FLASHPOWER = 0x00000080
KSCAMERA_METADATA_CAPTURESTATS_FLAG_ZOOMFACTOR = 0x00000100
KSCAMERA_METADATA_CAPTURESTATS_FLAG_SCENEMODE = 0x00000200
KSCAMERA_METADATA_CAPTURESTATS_FLAG_SENSORFRAMERATE = 0x00000400
# Focus Priority
KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_OFF = (
    0x00000000
)
# Focus State
KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_ON = (
    0x00000001
)


class KSCAMERA_EXTENDEDPROP_FOCUSSTATE(ENUM):
    KSCAMERA_EXTENDEDPROP_FOCUSSTATE_UNINITIALIZED = 0
    KSCAMERA_EXTENDEDPROP_FOCUSSTATE_LOST = 1
    KSCAMERA_EXTENDEDPROP_FOCUSSTATE_SEARCHING = 2
    KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FOCUSED = 3
    KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FAILED = 4


# Extended ROI
# Size of this header + all _CONFIGCAPS structures followed

class tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('ConfigCapCount', ULONG),
        ('Reserved', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER = (
    tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
)
PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER = POINTER(
    tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER
)


# Number of _CONFIGCAPS structures followed
# ISP control ID (focus, exposure, or white balance)

class tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS(ctypes.Structure):
    _fields_ = [
        ('ControlId', ULONG),
        ('MaxNumberOfROIs', ULONG),
        ('Capability', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS = tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS
PKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS = POINTER(
    tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS
)


# Max ROIs supported for this ISP control
# Caps for this ISP control
# Size of this header + all _ ISPCONTROL + all _RECTINFO

class tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('ControlCount', ULONG),
        ('Reserved', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER = (
    tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER
)
PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER = POINTER(
    tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER
)


# Number of ISP controls. 0 indicating clear all ROIs
# ISP control ID (focus, exposure, or white balance)

class tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL(ctypes.Structure):
    _fields_ = [
        ('ControlId', ULONG),
        ('ROICount', ULONG),
        ('Result', ULONG),
        ('Reserved', ULONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL = tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL
PKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL = POINTER(
    tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL
)


# Number of ROIs associated with this ISP control
# Error results of the last SET operation for this ISP control
# Relative coordinates on the frame that face detection is running (Q31 format)

class tagKSCAMERA_EXTENDEDPROP_ROI_INFO(ctypes.Structure):
    _fields_ = [
        ('Region', RECT),
        ('Flags', ULONGLONG),
        ('Weight', LONG),
        ('RegionOfInterestType', LONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_INFO = tagKSCAMERA_EXTENDEDPROP_ROI_INFO
PKSCAMERA_EXTENDEDPROP_ROI_INFO = POINTER(tagKSCAMERA_EXTENDEDPROP_ROI_INFO)


# VIDEOPROCFLAG flags indicating the op mode for the ISP control. Default is 0
# for focus
# Weight of the region   (0 -100)
# KSCAMERA_EXTENDEDPROP_ROITYPE_FACE, if the region is a face; Unknown
# otherwise
class KSCAMERA_EXTENDEDPROP_ROITYPE(ENUM):
    KSCAMERA_EXTENDEDPROP_ROITYPE_UNKNOWN = 0
    KSCAMERA_EXTENDEDPROP_ROITYPE_FACE = 1


# Must be the first field

class tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE(ctypes.Structure):
    _fields_ = [
        ('ROIInfo', KSCAMERA_EXTENDEDPROP_ROI_INFO),
        ('Reserved', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE = (
    tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE
)
PKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE = POINTER(
    tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE
)


# Must be the first field

class tagKSCAMERA_EXTENDEDPROP_ROI_EXPOSURE(ctypes.Structure):
    _fields_ = [
        ('ROIInfo', KSCAMERA_EXTENDEDPROP_ROI_INFO),
        ('Reserved', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_EXPOSURE = tagKSCAMERA_EXTENDEDPROP_ROI_EXPOSURE
PKSCAMERA_EXTENDEDPROP_ROI_EXPOSURE = POINTER(
    tagKSCAMERA_EXTENDEDPROP_ROI_EXPOSURE
)


# Must be the first field

class tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS(ctypes.Structure):
    _fields_ = [
        ('ROIInfo', KSCAMERA_EXTENDEDPROP_ROI_INFO),
        ('Reserved', ULONGLONG),
    ]


KSCAMERA_EXTENDEDPROP_ROI_FOCUS = tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS
PKSCAMERA_EXTENDEDPROP_ROI_FOCUS = POINTER(tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS)


# Photo confirmation (aka still confirmation)
KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_OFF = (
    0x00000000
)
KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_ON = (
    0x00000001
)
# Per Frame Settings



class KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY(ENUM):
    KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CAPABILITY = 0
    KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_SET = 1
    KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR = 2


KSCAMERA_PERFRAMESETTING_AUTO = (
    0x100000000
)
KSCAMERA_PERFRAMESETTING_MANUAL = (
    0x200000000
)


class KSCAMERA_PERFRAMESETTING_ITEM_TYPE(ENUM):
    KSCAMERA_PERFRAMESETTING_ITEM_EXPOSURE_TIME = 1
    KSCAMERA_PERFRAMESETTING_ITEM_FLASH = 2
    KSCAMERA_PERFRAMESETTING_ITEM_EXPOSURE_COMPENSATION = 3
    KSCAMERA_PERFRAMESETTING_ITEM_ISO = 4
    KSCAMERA_PERFRAMESETTING_ITEM_FOCUS = 5
    KSCAMERA_PERFRAMESETTING_ITEM_PHOTOCONFIRMATION = 6
    KSCAMERA_PERFRAMESETTING_ITEM_CUSTOM = 7


class KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Type', ULONG),
        ('Flags', ULONGLONG),
    ]


PKSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER = POINTER(
    KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER
)


# KSCAMERA_PERFRAMESETTING_ITEM_TYPE
# Supported Flags

class KSCAMERA_PERFRAMESETTING_CAP_HEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('ItemCount', ULONG),
        ('Flags', ULONGLONG),
    ]


PKSCAMERA_PERFRAMESETTING_CAP_HEADER = POINTER(
    KSCAMERA_PERFRAMESETTING_CAP_HEADER
)


class KSCAMERA_PERFRAMESETTING_CUSTOM_ITEM(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Reserved', ULONG),
        ('Id', GUID),
    ]


PKSCAMERA_PERFRAMESETTING_CUSTOM_ITEM = POINTER(
    KSCAMERA_PERFRAMESETTING_CUSTOM_ITEM
)


class KSCAMERA_PERFRAMESETTING_ITEM_HEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Type', ULONG),
        ('Flags', ULONGLONG),
    ]


PKSCAMERA_PERFRAMESETTING_ITEM_HEADER = POINTER(
    KSCAMERA_PERFRAMESETTING_ITEM_HEADER
)


# KSCAMERA_PERFRAMESETTING_ITEM_TYPE

class KSCAMERA_PERFRAMESETTING_FRAME_HEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('Id', ULONG),
        ('ItemCount', ULONG),
        ('Reserved', ULONG),
    ]


PKSCAMERA_PERFRAMESETTING_FRAME_HEADER = POINTER(
    KSCAMERA_PERFRAMESETTING_FRAME_HEADER
)


class KSCAMERA_PERFRAMESETTING_HEADER(ctypes.Structure):
    _fields_ = [
        ('Size', ULONG),
        ('FrameCount', ULONG),
        ('Id', GUID),
        ('Flags', ULONGLONG),
        ('LoopCount', ULONG),
        ('Reserved', ULONG),
    ]


PKSCAMERA_PERFRAMESETTING_HEADER = POINTER(KSCAMERA_PERFRAMESETTING_HEADER)


# (NTDDI_VERSION >= NTDDI_WINBLUE)
KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_OFF = 0x00000000
KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_ON = 0x00000001
KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_AUTO = 0x00000002
KSCAMERA_EXTENDEDPROP_VFR_OFF = 0x00000000
KSCAMERA_EXTENDEDPROP_VFR_ON = 0x00000001
KSCAMERA_EXTENDEDPROP_FACEDETECTION_OFF = 0x00000000
KSCAMERA_EXTENDEDPROP_FACEDETECTION_ON = 0x00000001
KSCAMERA_EXTENDEDPROP_FACEDETECTION_PREVIEW = 0x00000001
KSCAMERA_EXTENDEDPROP_FACEDETECTION_VIDEO = 0x00000002
KSCAMERA_EXTENDEDPROP_FACEDETECTION_PHOTO = 0x00000004
KSCAMERA_EXTENDEDPROP_FACEDETECTION_BLINK = 0x00000008
KSCAMERA_EXTENDEDPROP_FACEDETECTION_SMILE = 0x00000010
KSCAMERA_EXTENDEDPROP_FACEDETECTION_MASK = (
    KSCAMERA_EXTENDEDPROP_FACEDETECTION_PREVIEW |
    KSCAMERA_EXTENDEDPROP_FACEDETECTION_VIDEO |
    KSCAMERA_EXTENDEDPROP_FACEDETECTION_PHOTO
)
KSCAMERA_EXTENDEDPROP_FACEDETECTION_ADVANCED_MASK = (
    KSCAMERA_EXTENDEDPROP_FACEDETECTION_BLINK |
    KSCAMERA_EXTENDEDPROP_FACEDETECTION_SMILE
)
KSCAMERA_EXTENDEDPROP_VIDEOHDR_OFF = 0x00000000
KSCAMERA_EXTENDEDPROP_VIDEOHDR_ON = 0x00000001
KSCAMERA_EXTENDEDPROP_VIDEOHDR_AUTO = 0x00000002
KSCAMERA_EXTENDEDPROP_HISTOGRAM_OFF = 0x00000000
KSCAMERA_EXTENDEDPROP_HISTOGRAM_ON = 0x00000001
KSCAMERA_EXTENDEDPROP_OIS_OFF = 0x00000000
KSCAMERA_EXTENDEDPROP_OIS_ON = 0x00000001
KSCAMERA_EXTENDEDPROP_OIS_AUTO = 0x00000002
KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_OFF = 0x00000000
KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_AUTO = 0x00000001
KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_HDR = 0x00000002
KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_FNF = 0x00000004
KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_ULTRALOWLIGHT = 0x00000008
KSCAMERA_EXTENDEDPROP_ZOOM_DEFAULT = 0x00000000
KSCAMERA_EXTENDEDPROP_ZOOM_DIRECT = 0x00000001
KSCAMERA_EXTENDEDPROP_ZOOM_SMOOTH = 0x00000002
KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_DISABLED = (
    0x00000001
)
KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION = (
    0x00000002
)
KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION = (
    0x00000004
)
KSCAMERA_EXTENDEDPROP_SECUREMODE_DISABLED = 0x00000001
KSCAMERA_EXTENDEDPROP_SECUREMODE_ENABLED = 0x00000002
KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_AUTO = 0x00000001
KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_OFF = 0x00000002
KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_ON = 0x00000004


class _KSCAMERA_EXTENDEDPROP_PROFILE(ctypes.Structure):
    _fields_ = [
        ('ProfileId', GUID),
        ('Index', UINT32),
        ('Reserved', UINT32),
    ]


KSCAMERA_EXTENDEDPROP_PROFILE = _KSCAMERA_EXTENDEDPROP_PROFILE
PKSCAMERA_EXTENDEDPROP_PROFILE = POINTER(_KSCAMERA_EXTENDEDPROP_PROFILE)

KSCAMERAPROFILE_FLAGS_VIDEOSTABLIZATION = 0x00000001
KSCAMERAPROFILE_FLAGS_VIDEOHDR = 0x00000002
KSCAMERAPROFILE_FLAGS_PHOTOHDR = 0x00000004
KSCAMERAPROFILE_FLAGS_FACEDETECTION = 0x00000008
KSCAMERAPROFILE_FLAGS_VARIABLEPHOTOSEQUENCE = 0x00000010
KSCAMERAPROFILE_FLAGS_PREVIEW_RES_MUSTMATCH = 0x00000020
KSDEVICE_PROFILE_TYPE_UNKNOWN = 0x00000000
KSDEVICE_PROFILE_TYPE_CAMERA = 0x00000001
# Camera Pin Sensor output type should be in sync with MFFrameSourceTypes

KSCameraProfileSensorType_RGB = 0x0001
KSCameraProfileSensorType_Infrared = 0x0002
KSCameraProfileSensorType_Depth = 0x0004
KSCameraProfileSensorType_PoseTracking = 0x0008
KSCameraProfileSensorType_ImageSegmentation = 0x0010
KSCameraProfileSensorType_Custom = 0x0080


class _KSCAMERA_PROFILE_MEDIAINFO(ctypes.Structure):

    class Resolution(ctypes.Structure):
        _fields_ = [
            ('X', UINT32),
            ('Y', UINT32),
        ]

    class MaxFrameRate(ctypes.Structure):
        _fields_ = [
            ('Numerator', UINT32),
            ('Denominator', UINT32),
        ]

    _fields_ = [
        ('Resolution', Resolution),
        ('MaxFrameRate', MaxFrameRate),
        ('Flags', ULONGLONG),
        ('Data0', UINT32),
        ('Data1', UINT32),
        ('Data2', UINT32),
        ('Data3', UINT32),
    ]


KSCAMERA_PROFILE_MEDIAINFO = _KSCAMERA_PROFILE_MEDIAINFO
PKSCAMERA_PROFILE_MEDIAINFO = POINTER(_KSCAMERA_PROFILE_MEDIAINFO)


class _KSCAMERA_PROFILE_PININFO(ctypes.Structure):

    class _Union_0(ctypes.Union):

        class _Struct_0(ctypes.Structure):
            _fields_ = [
                ('PinIndex', USHORT),
                ('ProfileSensorType', USHORT),
            ]

        _anonymous_ = ('_Struct_0', )
        _fields_ = [
            ('_Struct_0', _Struct_0),
            ('Reserved', UINT32),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('PinCategory', GUID),
        ('_Union_0', _Union_0),
        ('MediaInfoCount', UINT32),
        ('MediaInfos', PKSCAMERA_PROFILE_MEDIAINFO),
    ]


KSCAMERA_PROFILE_PININFO = _KSCAMERA_PROFILE_PININFO
PKSCAMERA_PROFILE_PININFO = POINTER(_KSCAMERA_PROFILE_PININFO)


class _KSCAMERA_PROFILE_INFO(ctypes.Structure):
    _fields_ = [
        ('ProfileId', GUID),
        ('Index', UINT32),
        ('PinCount', UINT32),
        ('Pins', PKSCAMERA_PROFILE_PININFO),
    ]


KSCAMERA_PROFILE_INFO = _KSCAMERA_PROFILE_INFO
PKSCAMERA_PROFILE_INFO = POINTER(_KSCAMERA_PROFILE_INFO)


class _KSCAMERA_PROFILE_CONCURRENCYINFO(ctypes.Structure):
    _fields_ = [
        ('ReferenceGuid', GUID),
        ('Reserved', UINT32),
        ('ProfileCount', UINT32),
        ('Profiles', PKSCAMERA_PROFILE_INFO),
    ]


KSCAMERA_PROFILE_CONCURRENCYINFO = _KSCAMERA_PROFILE_CONCURRENCYINFO
PKSCAMERA_PROFILE_CONCURRENCYINFO = POINTER(_KSCAMERA_PROFILE_CONCURRENCYINFO)


class _KSDEVICE_PROFILE_INFO(ctypes.Structure):

    class _Union_0(ctypes.Union):

        class Camera(ctypes.Structure):
            _fields_ = [
                ('Info', KSCAMERA_PROFILE_INFO),
                ('Reserved', UINT32),
                ('ConcurrencyCount', UINT32),
                ('Concurrency', PKSCAMERA_PROFILE_CONCURRENCYINFO),
            ]

        _fields_ = [
            ('Camera', Camera),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('Type', UINT32),
        ('Size', UINT32),
        ('_Union_0', _Union_0),
    ]


KSDEVICE_PROFILE_INFO = _KSDEVICE_PROFILE_INFO
PKSDEVICE_PROFILE_INFO = POINTER(_KSDEVICE_PROFILE_INFO)

# Add other device type specific "profiles" here.

class _WNF_KSCAMERA_STREAMSTATE_INFO(ctypes.Structure):
    _fields_ = [
        ('ProcessId', ULONG),
        ('SessionId', ULONG),
        ('StreamState', ULONG),
        ('Reserved', ULONG),
    ]


WNF_KSCAMERA_STREAMSTATE_INFO = _WNF_KSCAMERA_STREAMSTATE_INFO
PWNF_KSCAMERA_STREAMSTATE_INFO = POINTER(_WNF_KSCAMERA_STREAMSTATE_INFO)


# ===========================================================================
class KSPROPERTY_EXTDEVICE(ENUM):
    KSPROPERTY_EXTDEVICE_ID = 0
    KSPROPERTY_EXTDEVICE_VERSION = 1
    KSPROPERTY_EXTDEVICE_POWER_STATE = 2
    KSPROPERTY_EXTDEVICE_PORT = 3
    KSPROPERTY_EXTDEVICE_CAPABILITIES = 4


class tagDEVCAPS(ctypes.Structure):
    _fields_ = [
        ('CanRecord', LONG),
        ('CanRecordStrobe', LONG),
        ('HasAudio', LONG),
        ('HasVideo', LONG),
        ('UsesFiles', LONG),
        ('CanSave', LONG),
        ('DeviceType', LONG),
        ('TCRead', LONG),
        ('TCWrite', LONG),
        ('CTLRead', LONG),
        ('IndexRead', LONG),
        ('Preroll', LONG),
        ('Postroll', LONG),
        ('SyncAcc', LONG),
        ('NormRate', LONG),
        ('CanPreview', LONG),
        ('CanMonitorSrc', LONG),
        ('CanTest', LONG),
        ('VideoIn', LONG),
        ('AudioIn', LONG),
        ('Calibrate', LONG),
        ('SeekType', LONG),
        ('SimulatedHardware', LONG),
    ]


DEVCAPS = tagDEVCAPS
PDEVCAPS = POINTER(tagDEVCAPS)


class KSPROPERTY_EXTDEVICE_S(ctypes.Structure):

    class u(ctypes.Union):
        _fields_ = [
            ('Capabilities', DEVCAPS),
            ('DevPort', ULONG),
            ('PowerState', ULONG),
            ('pawchString', WCHAR * MAX_PATH),
            ('NodeUniqueID', DWORD * 2),
        ]

    _fields_ = [
        ('Property', KSPROPERTY),
        ('u', u),
    ]


PKSPROPERTY_EXTDEVICE_S = POINTER(KSPROPERTY_EXTDEVICE_S)


# (R)  Transport specific capability
# (RW) Input signal: e.g. dvsd/NTSC/PAL, dvsl/NTSC/PAL, MPEG2-TS etc
class KSPROPERTY_EXTXPORT(ENUM):
    KSPROPERTY_EXTXPORT_CAPABILITIES = 0
    KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE = 1
    KSPROPERTY_EXTXPORT_OUTPUT_SIGNAL_MODE = 2
    KSPROPERTY_EXTXPORT_LOAD_MEDIUM = 3
    KSPROPERTY_EXTXPORT_MEDIUM_INFO = 4
    KSPROPERTY_EXTXPORT_STATE = 5
    KSPROPERTY_EXTXPORT_STATE_NOTIFY = 6
    KSPROPERTY_EXTXPORT_TIMECODE_SEARCH = 7
    KSPROPERTY_EXTXPORT_ATN_SEARCH = 8
    KSPROPERTY_EXTXPORT_RTC_SEARCH = 9
    KSPROPERTY_RAW_AVC_CMD = 10


# (RW) Output signal: e.g. dvsd/NTSC/PAL, dvsl/NTSC/PAL, MPEG2-TS etc
# (RW) Eject, open tray, close tray
# (R)  Cassettte type, tape grade and write protection
# (RW) Current transport mode and state
# (RW) Notify of transport mode and state change
# (W)  Search to a specific timecode on a tape
# (W)  Search to a specific absolute track number (ATN) on a tape
# (W)  Search to a specific relative time counter (RTC) on a tape
# (RW) Issue a raw AVC commnad

class tagTRANSPORTSTATUS(ctypes.Structure):
    _fields_ = [
        ('Mode', LONG),
        ('LastError', LONG),
        ('RecordInhibit', LONG),
        ('ServoLock', LONG),
        ('MediaPresent', LONG),
        ('MediaLength', LONG),
        ('MediaSize', LONG),
        ('MediaTrackCount', LONG),
        ('MediaTrackLength', LONG),
        ('MediaTrackSide', LONG),
        ('MediaType', LONG),
        ('LinkMode', LONG),
        ('NotifyOn', LONG),
    ]


TRANSPORTSTATUS = tagTRANSPORTSTATUS
PTRANSPORTSTATUS = POINTER(tagTRANSPORTSTATUS)


class tagTRANSPORTBASICPARMS(ctypes.Structure):
    _fields_ = [
        ('TimeFormat', LONG),
        ('TimeReference', LONG),
        ('Superimpose', LONG),
        ('EndStopAction', LONG),
        ('RecordFormat', LONG),
        ('StepFrames', LONG),
        ('SetpField', LONG),
        ('Preroll', LONG),
        ('RecPreroll', LONG),
        ('Postroll', LONG),
        ('EditDelay', LONG),
        ('PlayTCDelay', LONG),
        ('RecTCDelay', LONG),
        ('EditField', LONG),
        ('FrameServo', LONG),
        ('ColorFrameServo', LONG),
        ('ServoRef', LONG),
        ('WarnGenlock', LONG),
        ('SetTracking', LONG),
        ('VolumeName', TCHAR * 40),
        ('Ballistic', LONG * 20),
        ('Speed', LONG),
        ('CounterFormat', LONG),
        ('TunerChannel', LONG),
        ('TunerNumber', LONG),
        ('TimerEvent', LONG),
        ('TimerStartDay', LONG),
        ('TimerStartTime', LONG),
        ('TimerStopDay', LONG),
        ('TimerStopTime', LONG),
    ]


TRANSPORTBASICPARMS = tagTRANSPORTBASICPARMS
PTRANSPORTBASICPARMS = POINTER(tagTRANSPORTBASICPARMS)


class tagTRANSPORTVIDEOPARMS(ctypes.Structure):
    _fields_ = [
        ('OutputMode', LONG),
        ('Input', LONG),
    ]


TRANSPORTVIDEOPARMS = tagTRANSPORTVIDEOPARMS
PTRANSPORTVIDEOPARMS = POINTER(tagTRANSPORTVIDEOPARMS)


class tagTRANSPORTAUDIOPARMS(ctypes.Structure):
    _fields_ = [
        ('EnableOutput', LONG),
        ('EnableRecord', LONG),
        ('EnableSelsync', LONG),
        ('Input', LONG),
        ('MonitorSource', LONG),
    ]


TRANSPORTAUDIOPARMS = tagTRANSPORTAUDIOPARMS
PTRANSPORTAUDIOPARMS = POINTER(tagTRANSPORTAUDIOPARMS)


class MEDIUM_INFO(ctypes.Structure):
    _fields_ = [
        ('MediaPresent', BOOL),
        ('MediaType', ULONG),
        ('RecordInhibit', BOOL),
    ]


PMEDIUM_INFO = POINTER(MEDIUM_INFO)


class TRANSPORT_STATE(ctypes.Structure):
    _fields_ = [
        ('Mode', ULONG),
        ('State', ULONG),
    ]


PTRANSPORT_STATE = POINTER(TRANSPORT_STATE)


class KSPROPERTY_EXTXPORT_S(ctypes.Structure):

    class u(ctypes.Union):

        class Timecode(ctypes.Structure):
            _fields_ = [
                ('frame', BYTE),
                ('second', BYTE),
                ('minute', BYTE),
                ('hour', BYTE),
            ]

        class RawAVC(ctypes.Structure):
            _fields_ = [
                ('PayloadSize', ULONG),
                ('Payload', BYTE * 512),
            ]

        _fields_ = [
            ('Capabilities', ULONG),
            ('SignalMode', ULONG),
            ('LoadMedium', ULONG),
            ('MediumInfo', MEDIUM_INFO),
            ('XPrtState', TRANSPORT_STATE),
            ('Timecode', Timecode),
            ('dwTimecode', DWORD),
            ('dwAbsTrackNumber', DWORD),
            ('RawAVC', RawAVC),
        ]

    _fields_ = [
        ('Property', KSPROPERTY),
        ('u', u),
    ]


PKSPROPERTY_EXTXPORT_S = POINTER(KSPROPERTY_EXTXPORT_S)


class KSPROPERTY_EXTXPORT_NODE_S(ctypes.Structure):

    class u(ctypes.Union):

        class Timecode(ctypes.Structure):
            _fields_ = [
                ('frame', BYTE),
                ('second', BYTE),
                ('minute', BYTE),
                ('hour', BYTE),
            ]

        class RawAVC(ctypes.Structure):
            _fields_ = [
                ('PayloadSize', ULONG),
                ('Payload', BYTE * 512),
            ]

        _fields_ = [
            ('Capabilities', ULONG),
            ('SignalMode', ULONG),
            ('LoadMedium', ULONG),
            ('MediumInfo', MEDIUM_INFO),
            ('XPrtState', TRANSPORT_STATE),
            ('Timecode', Timecode),
            ('dwTimecode', DWORD),
            ('dwAbsTrackNumber', DWORD),
            ('RawAVC', RawAVC),
        ]

    _fields_ = [
        ('NodeProperty', KSP_NODE),
        ('u', u),
    ]


PKSPROPERTY_EXTXPORT_NODE_S = POINTER(KSPROPERTY_EXTXPORT_NODE_S)


# (R) Timecode for the current tape position
# (R) Absolute track number for the current tape position
class KSPROPERTY_TIMECODE(ENUM):
    KSPROPERTY_TIMECODE_READER = 0
    KSPROPERTY_ATN_READER = 1
    KSPROPERTY_RTC_READER = 2


# (R) Relative time counter for the current tape position

class _timecode(ctypes.Union):

    class _Struct_0(ctypes.Structure):
        _fields_ = [
            ('wFrameRate', WORD),
            ('wFrameFract', WORD),
            ('dwFrames', DWORD),
        ]

    _anonymous_ = ('_Struct_0', )
    _fields_ = [
        ('_Struct_0', _Struct_0),
        ('qw', DWORDLONG),
    ]


TIMECODE = _timecode


PTIMECODE = POINTER(TIMECODE)


class tagTIMECODE_SAMPLE(ctypes.Structure):
    _fields_ = [
        ('qwTick', LONGLONG),
        ('timecode', TIMECODE),
        ('dwUser', DWORD),
        ('dwFlags', DWORD),
    ]


TIMECODE_SAMPLE = tagTIMECODE_SAMPLE


# TIMECODE_DEFINED
PTIMECODE_SAMPLE = POINTER(TIMECODE_SAMPLE)


class KSPROPERTY_TIMECODE_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('TimecodeSamp', TIMECODE_SAMPLE),
    ]


PKSPROPERTY_TIMECODE_S = POINTER(KSPROPERTY_TIMECODE_S)


class KSPROPERTY_TIMECODE_NODE_S(ctypes.Structure):
    _fields_ = [
        ('NodeProperty', KSP_NODE),
        ('TimecodeSamp', TIMECODE_SAMPLE),
    ]


PKSPROPERTY_TIMECODE_NODE_S = POINTER(KSPROPERTY_TIMECODE_NODE_S)


# Final response is ready for notify command
# Final response is ready for control command.
class KSEVENT_DEVCMD(ENUM):
    KSEVENT_EXTDEV_COMMAND_NOTIFY_INTERIM_READY = 0
    KSEVENT_EXTDEV_COMMAND_CONTROL_INTERIM_READY = 1
    KSEVENT_EXTDEV_COMMAND_BUSRESET = 2
    KSEVENT_EXTDEV_TIMECODE_UPDATE = 3
    KSEVENT_EXTDEV_OPERATION_MODE_UPDATE = 4
    KSEVENT_EXTDEV_TRANSPORT_STATE_UPDATE = 5
    KSEVENT_EXTDEV_NOTIFY_REMOVAL = 6
    KSEVENT_EXTDEV_NOTIFY_MEDIUM_CHANGE = 7


# A bus reset has occured.
# Timecode has changed.
# Operting mode (VCR,Camera, etc.) has changed.
# Transport state has changed.
# Device was surprise removal.
# Tape medium is removed or added.
# __EDevCtrl__
# XP SP2 and later (chronologically)
# ===========================================================================

# R
# R
class KSPROPERTY_VIDCAP_CROSSBAR(ENUM):
    KSPROPERTY_CROSSBAR_CAPS = 0
    KSPROPERTY_CROSSBAR_PININFO = 1
    KSPROPERTY_CROSSBAR_CAN_ROUTE = 2
    KSPROPERTY_CROSSBAR_ROUTE = 3
    KSPROPERTY_CROSSBAR_INPUT_ACTIVE = 4


# R
# RW
# R

class KSPROPERTY_CROSSBAR_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('NumberOfInputs', ULONG),
        ('NumberOfOutputs', ULONG),
    ]


PKSPROPERTY_CROSSBAR_CAPS_S = POINTER(KSPROPERTY_CROSSBAR_CAPS_S)


# the number of audio and video input pins
# the number of audio and video output pins

class KSPROPERTY_CROSSBAR_PININFO_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Direction', KSPIN_DATAFLOW),
        ('Index', ULONG),
        ('PinType', ULONG),
        ('RelatedPinIndex', ULONG),
        ('Medium', KSPIN_MEDIUM),
    ]


PKSPROPERTY_CROSSBAR_PININFO_S = POINTER(KSPROPERTY_CROSSBAR_PININFO_S)


# KSPIN_DATAFLOW_IN or KSPIN_DATAFLOW_OUT?
# Which pin to return data for?
# KS_PhysConn_Video_* or KS_PhysConn_Audio_*
# For video pins, this is the related audio pin
# Identifies the hardware connection

class KSPROPERTY_CROSSBAR_ROUTE_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('IndexInputPin', ULONG),
        ('IndexOutputPin', ULONG),
        ('CanRoute', ULONG),
    ]


PKSPROPERTY_CROSSBAR_ROUTE_S = POINTER(KSPROPERTY_CROSSBAR_ROUTE_S)


# Zero based index of the input pin
# Zero based index of the output pin
# returns non-zero on CAN_ROUTE if routing is possible

class KSPROPERTY_CROSSBAR_ACTIVE_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('IndexInputPin', ULONG),
        ('Active', ULONG),
    ]


PKSPROPERTY_CROSSBAR_ACTIVE_S = POINTER(KSPROPERTY_CROSSBAR_ACTIVE_S)



class KSEVENT_CROSSBAR(ENUM):
    KSEVENT_CROSSBAR_CHANGED = 0


# The following IDs should match the AM equivalents
class KS_PhysicalConnectorType(ENUM):
    KS_PhysConn_Video_Tuner = 1
    KS_PhysConn_Video_Composite = 2
    KS_PhysConn_Video_SVideo = 3
    KS_PhysConn_Video_RGB = 4
    KS_PhysConn_Video_YRYBY = 5
    KS_PhysConn_Video_SerialDigital = 6
    KS_PhysConn_Video_ParallelDigital = 7
    KS_PhysConn_Video_SCSI = 8
    KS_PhysConn_Video_AUX = 9
    KS_PhysConn_Video_1394 = 10
    KS_PhysConn_Video_USB = 11
    KS_PhysConn_Video_VideoDecoder = 12
    KS_PhysConn_Video_VideoEncoder = 13
    KS_PhysConn_Video_SCART = 14
    KS_PhysConn_Audio_Tuner = 4096
    KS_PhysConn_Audio_Line = 4097
    KS_PhysConn_Audio_Mic = 4098
    KS_PhysConn_Audio_AESDigital = 4099
    KS_PhysConn_Audio_SPDIFDigital = 4100
    KS_PhysConn_Audio_SCSI = 4101
    KS_PhysConn_Audio_AUX = 4102
    KS_PhysConn_Audio_1394 = 4103
    KS_PhysConn_Audio_USB = 4104
    KS_PhysConn_Audio_AudioDecoder = 4105



# R
# RW
class KSPROPERTY_VIDCAP_TVAUDIO(ENUM):
    KSPROPERTY_TVAUDIO_CAPS = 0
    KSPROPERTY_TVAUDIO_MODE = 1
    KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES = 2


# R
# Mono
# Stereo
# Primary language
KS_TVAUDIO_MODE_MONO = 0x0001
# 2nd avail language
KS_TVAUDIO_MODE_STEREO = 0x0002
# 3rd avail language
KS_TVAUDIO_MODE_LANG_A = 0x0010
KS_TVAUDIO_MODE_LANG_B = 0x0020
# if present, stereo
KS_TVAUDIO_MODE_LANG_C = 0x0040
# if present, Language A
# if present, Language B
KS_TVAUDIO_PRESET_STEREO = 0x0200
# if present, Language C
KS_TVAUDIO_PRESET_LANG_A = 0x1000
# (NTDDI_VERSION >= NTDDI_VISTA
KS_TVAUDIO_PRESET_LANG_B = 0x2000
KS_TVAUDIO_PRESET_LANG_C = 0x4000


class KSPROPERTY_TVAUDIO_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Capabilities', ULONG),
        ('InputMedium', KSPIN_MEDIUM),
        ('OutputMedium', KSPIN_MEDIUM),
    ]


PKSPROPERTY_TVAUDIO_CAPS_S = POINTER(KSPROPERTY_TVAUDIO_CAPS_S)


# Bitmask of KS_TVAUDIO_MODE_*

class KSPROPERTY_TVAUDIO_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Mode', ULONG),
    ]


PKSPROPERTY_TVAUDIO_S = POINTER(KSPROPERTY_TVAUDIO_S)



class KSEVENT_TVAUDIO(ENUM):
    KSEVENT_TVAUDIO_CHANGED = 0


# ===========================================================================

# R
# RW
class KSPROPERTY_VIDCAP_VIDEOCOMPRESSION(ENUM):
    KSPROPERTY_VIDEOCOMPRESSION_GETINFO = 0
    KSPROPERTY_VIDEOCOMPRESSION_KEYFRAME_RATE = 1
    KSPROPERTY_VIDEOCOMPRESSION_PFRAMES_PER_KEYFRAME = 2
    KSPROPERTY_VIDEOCOMPRESSION_QUALITY = 3
    KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_KEYFRAME = 4
    KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_FRAME_SIZE = 5
    KSPROPERTY_VIDEOCOMPRESSION_WINDOWSIZE = 6


# RW
# RW
# W
# W
# RW
class KS_CompressionCaps(ENUM):
    KS_CompressionCaps_CanQuality = 1
    KS_CompressionCaps_CanCrunch = 2
    KS_CompressionCaps_CanKeyFrame = 4
    KS_CompressionCaps_CanBFrame = 8
    KS_CompressionCaps_CanWindow = 0x10


class KS_VideoStreamingHINTs(ENUM):
    KS_StreamingHINT_FrameInterval = 0x0100
    KS_StreamingHINT_KeyFrameRate = 0x0200
    KS_StreamingHINT_PFrameRate = 0x0400
    KS_StreamingHINT_CompQuality = 0x0800
    KS_StreamingHINT_CompWindowSize = 0x1000


# XP SP2 and later (chronologically)

class KSPROPERTY_VIDEOCOMPRESSION_GETINFO_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('DefaultKeyFrameRate', LONG),
        ('DefaultPFrameRate', LONG),
        ('DefaultQuality', LONG),
        ('NumberOfQualitySettings', LONG),
        ('Capabilities', LONG),
    ]


PKSPROPERTY_VIDEOCOMPRESSION_GETINFO_S = POINTER(
    KSPROPERTY_VIDEOCOMPRESSION_GETINFO_S
)


# Note, no VersionString!
# Note, no DescriptionString!
# zero based index of stream
# Key frame rate
# Predeicted frames per Key frame
# 0 to 10000
# How many discreet quality settings?
# KS_CompressionCaps_*

class KSPROPERTY_VIDEOCOMPRESSION_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('Value', LONG),
    ]


PKSPROPERTY_VIDEOCOMPRESSION_S = POINTER(KSPROPERTY_VIDEOCOMPRESSION_S)


# zero based index of stream
# value to get or set

class KSPROPERTY_VIDEOCOMPRESSION_S1(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('Value', LONG),
        ('Flags', ULONG),
    ]


PKSPROPERTY_VIDEOCOMPRESSION_S1 = POINTER(KSPROPERTY_VIDEOCOMPRESSION_S1)


class KSPROPERTY_OVERLAYUPDATE(ENUM):
    KSPROPERTY_OVERLAYUPDATE_INTERESTS = 0
    KSPROPERTY_OVERLAYUPDATE_CLIPLIST = 0x1
    KSPROPERTY_OVERLAYUPDATE_PALETTE = 0x2
    KSPROPERTY_OVERLAYUPDATE_COLORKEY = 0x4
    KSPROPERTY_OVERLAYUPDATE_VIDEOPOSITION = 0x8
    KSPROPERTY_OVERLAYUPDATE_DISPLAYCHANGE = 0x10
    KSPROPERTY_OVERLAYUPDATE_COLORREF = 0x10000000


class KSDISPLAYCHANGE(ctypes.Structure):
    _fields_ = [
        ('PelsWidth', ULONG),
        ('PelsHeight', ULONG),
        ('BitsPerPel', ULONG),
        ('DeviceID', WCHAR * 1),
    ]


PKSDISPLAYCHANGE = POINTER(KSDISPLAYCHANGE)


def DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_INTERESTS(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_OVERLAYUPDATE.KSPROPERTY_OVERLAYUPDATE_INTERESTS,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(ULONG),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_PALETTE(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_OVERLAYUPDATE.KSPROPERTY_OVERLAYUPDATE_PALETTE,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        0,
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_COLORKEY(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_OVERLAYUPDATE.KSPROPERTY_OVERLAYUPDATE_COLORKEY,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(COLORKEY),
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_CLIPLIST(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_OVERLAYUPDATE.KSPROPERTY_OVERLAYUPDATE_CLIPLIST,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        2 * ctypes.sizeof(RECT) + ctypes.sizeof(RGNDATAHEADER),
        Handler,
        NULL, 0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_VIDEOPOSITION(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_OVERLAYUPDATE.KSPROPERTY_OVERLAYUPDATE_VIDEOPOSITION,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        2 * ctypes.sizeof(RECT),
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_DISPLAYCHANGE(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_OVERLAYUPDATE.KSPROPERTY_OVERLAYUPDATE_DISPLAYCHANGE,
        NULL,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(KSDISPLAYCHANGE),
        Handler,
        NULL,
        0,
        NULL,
        NULL,
        0
    )


def DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_COLORREF(Handler):
    return DEFINE_KSPROPERTY_ITEM(
        KSPROPERTY_OVERLAYUPDATE.KSPROPERTY_OVERLAYUPDATE_COLORREF,
        Handler,
        ctypes.sizeof(KSPROPERTY),
        ctypes.sizeof(COLORREF),
        NULL,
        NULL,
        0,
        NULL,
        NULL,
        0
    )



# R
# R O
class KSPROPERTY_VIDCAP_VIDEOCONTROL(ENUM):
    KSPROPERTY_VIDEOCONTROL_CAPS = 0
    KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE = 1
    KSPROPERTY_VIDEOCONTROL_FRAME_RATES = 2
    KSPROPERTY_VIDEOCONTROL_MODE = 3


# R O
# RWO
class KS_VideoControlFlags(ENUM):
    KS_VideoControlFlag_FlipHorizontal = 0x0001
    KS_VideoControlFlag_FlipVertical = 0x0002
    KS_Obsolete_VideoControlFlag_ExternalTriggerEnable = 0x0010
    KS_Obsolete_VideoControlFlag_Trigger = 0x0020
    KS_VideoControlFlag_ExternalTriggerEnable = 0x0004
    KS_VideoControlFlag_Trigger = 0x0008
    KS_VideoControlFlag_IndependentImagePin = 0x0040
    KS_VideoControlFlag_StillCapturePreviewFrame = 0x0080
    KS_VideoControlFlag_StartPhotoSequenceCapture = 0x0100
    KS_VideoControlFlag_StopPhotoSequenceCapture = 0x0200


class KSPROPERTY_VIDEOCONTROL_CAPS_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('VideoControlCaps', ULONG),
    ]


PKSPROPERTY_VIDEOCONTROL_CAPS_S = POINTER(KSPROPERTY_VIDEOCONTROL_CAPS_S)


# KS_VideoControlFlags_*

class KSPROPERTY_VIDEOCONTROL_MODE_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('Mode', LONG),
    ]


PKSPROPERTY_VIDEOCONTROL_MODE_S = POINTER(KSPROPERTY_VIDEOCONTROL_MODE_S)


# KS_VideoControlFlags_*

class KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('RangeIndex', ULONG),
        ('Dimensions', SIZE),
        ('CurrentActualFrameRate', LONGLONG),
        ('CurrentMaxAvailableFrameRate', LONGLONG),
    ]


PKSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE_S = POINTER(
    KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE_S
)


# Index of stream
# Index of range
# Size of image
# Only correct if pin is open
# Max Rate temporarily limited on USB or 1394?
# KSPROPERTY_VIDEOCONTROL_FRAME_RATES returns a list of available frame rates
# in 100 nS units

class KSPROPERTY_VIDEOCONTROL_FRAME_RATES_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('StreamIndex', ULONG),
        ('RangeIndex', ULONG),
        ('Dimensions', SIZE),
    ]


PKSPROPERTY_VIDEOCONTROL_FRAME_RATES_S = POINTER(KSPROPERTY_VIDEOCONTROL_FRAME_RATES_S)


# R
class KSPROPERTY_VIDCAP_DROPPEDFRAMES(ENUM):
    KSPROPERTY_DROPPEDFRAMES_CURRENT = 0


class KSPROPERTY_DROPPEDFRAMES_CURRENT_S(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('PictureNumber', LONGLONG),
        ('DropCount', LONGLONG),
        ('AverageFrameSize', ULONG),
    ]


PKSPROPERTY_DROPPEDFRAMES_CURRENT_S = POINTER(KSPROPERTY_DROPPEDFRAMES_CURRENT_S)


class KSPROPERTY_VPCONFIG(ENUM):
    KSPROPERTY_VPCONFIG_NUMCONNECTINFO = 0
    KSPROPERTY_VPCONFIG_GETCONNECTINFO = 1
    KSPROPERTY_VPCONFIG_SETCONNECTINFO = 2
    KSPROPERTY_VPCONFIG_VPDATAINFO = 3
    KSPROPERTY_VPCONFIG_MAXPIXELRATE = 4
    KSPROPERTY_VPCONFIG_INFORMVPINPUT = 5
    KSPROPERTY_VPCONFIG_NUMVIDEOFORMAT = 6
    KSPROPERTY_VPCONFIG_GETVIDEOFORMAT = 7
    KSPROPERTY_VPCONFIG_SETVIDEOFORMAT = 8
    KSPROPERTY_VPCONFIG_INVERTPOLARITY = 9
    KSPROPERTY_VPCONFIG_DECIMATIONCAPABILITY = 10
    KSPROPERTY_VPCONFIG_SCALEFACTOR = 11
    KSPROPERTY_VPCONFIG_DDRAWHANDLE = 12
    KSPROPERTY_VPCONFIG_VIDEOPORTID = 13
    KSPROPERTY_VPCONFIG_DDRAWSURFACEHANDLE = 14
    KSPROPERTY_VPCONFIG_SURFACEPARAMS = 15


class KSVPMAXPIXELRATE(ctypes.Structure):
    _fields_ = [
        ('Size', AMVPSIZE),
        ('MaxPixelsPerSecond', DWORD),
        ('Reserved', DWORD),
    ]


PKSVPMAXPIXELRATE = POINTER(KSVPMAXPIXELRATE)


class KSVPSIZE_PROP(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('Size', AMVPSIZE),
    ]


PKSVPSIZE_PROP = POINTER(KSVPSIZE_PROP)


class KSVPSURFACEPARAMS(ctypes.Structure):
    _fields_ = [
        ('dwPitch', DWORD),
        ('dwXOrigin', DWORD),
        ('dwYOrigin', DWORD),
    ]


PKSVPSURFACEPARAMS = POINTER(KSVPSURFACEPARAMS)


# !defined(__IVPType__)
# ==========================================================================
# The following definitions must be in sync with DDraw.h in DirectX SDK
# ==========================================================================
# * The FourCC code is valid.
DDPF_FOURCC = 0x00000004


class _DDPIXELFORMAT(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('dwRGBBitCount', DWORD),
            ('dwYUVBitCount', DWORD),
            ('dwZBufferBitDepth', DWORD),
            ('dwAlphaBitDepth', DWORD),
        ]

    class _Union_1(ctypes.Union):
        _fields_ = [
            ('dwRBitMask', DWORD),
            ('dwYBitMask', DWORD),
        ]

    class _Union_2(ctypes.Union):
        _fields_ = [
            ('dwGBitMask', DWORD),
            ('dwUBitMask', DWORD),
        ]

    class _Union_3(ctypes.Union):
        _fields_ = [
            ('dwBBitMask', DWORD),
            ('dwVBitMask', DWORD),
        ]

    class _Union_4(ctypes.Union):
        _fields_ = [
            ('dwRGBAlphaBitMask', DWORD),
            ('dwYUVAlphaBitMask', DWORD),
            ('dwRGBZBitMask', DWORD),
            ('dwYUVZBitMask', DWORD),
        ]

    _anonymous_ = ('_Union_0', '_Union_1', '_Union_2', '_Union_3', '_Union_4')
    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('dwFourCC', DWORD),
        ('_Union_0', _Union_0),
        ('_Union_1', _Union_1),
        ('_Union_2', _Union_2),
        ('_Union_3', _Union_3),
        ('_Union_4', _Union_4),
    ]


DDPIXELFORMAT = _DDPIXELFORMAT
LPDDPIXELFORMAT = POINTER(_DDPIXELFORMAT)


# size of structure
# pixel format flags
# (FOURCC code)
# how many bits per pixel (BD_1,2,4,8,16,24,32)
# how many bits per pixel (BD_4,8,16,24,32)
# how many bits for z buffers (BD_8,16,24,32)
# how many bits for alpha channels (BD_1,2,4,8)
# mask for red bit
# mask for Y bits
# mask for green bits
# mask for U bits
# mask for blue bits
# mask for V bits
# mask for alpha channel
# mask for alpha channel
# mask for Z channel
# mask for Z channel
# _DDPIXELFORMAT_DEFINED
# !defined(__DDRAW_INCLUDED__)
# ==========================================================================
# End of DDraw.h header info
# ==========================================================================
# ==========================================================================
# The following definitions must be in sync with DVP.h in DirectX SDK
# ==========================================================================
# size of the DDVIDEOPORTCONNECT structure

class _DDVIDEOPORTCONNECT(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwPortWidth', DWORD),
        ('guidTypeID', GUID),
        ('dwFlags', DWORD),
        ('dwReserved1', ULONG_PTR),
    ]


DDVIDEOPORTCONNECT = _DDVIDEOPORTCONNECT
LPDDVIDEOPORTCONNECT = POINTER(_DDVIDEOPORTCONNECT)


# Width of the video port
# Description of video port connection
# Connection flags
# Reserved, set to zero.
DDVPTYPE_E_HREFH_VREFH = (
    0x54F39980,
    0xDA60,
    0x11CF,
    0x9B,
    0x06,
    0x00,
    0xA0,
    0xC9,
    0x03,
    0xA3,
    0xB8,
)
DDVPTYPE_E_HREFL_VREFL = (
    0xE09C77E0,
    0xDA60,
    0x11CF,
    0x9B,
    0x06,
    0x00,
    0xA0,
    0xC9,
    0x03,
    0xA3,
    0xB8,
)


# !defined(__DVP_INCLUDED__)
# ==========================================================================
# End of DVP.h header info
# ==========================================================================
# ==========================================================================
# The following definitions must be in sync with VPType.h in AM 2.0 SDK
# ==========================================================================
# pixel aspect ratios corresponding to a 720x480 NTSC image or a 720x576 image
# AMPixAspectRatio
class KS_AMPixAspectRatio(ENUM):
    KS_PixAspectRatio_NTSC4x3 = 0
    KS_PixAspectRatio_NTSC16x9 = 1
    KS_PixAspectRatio_PAL4x3 = 2
    KS_PixAspectRatio_PAL16x9 = 3


# AMVP_SELECTFORMATBY
class KS_AMVP_SELECTFORMATBY(ENUM):
    KS_AMVP_DO_NOT_CARE = 0
    KS_AMVP_BEST_BANDWIDTH = 1
    KS_AMVP_INPUT_SAME_AS_OUTPUT = 2


# AMVP_MODE
class KS_AMVP_MODE(ENUM):
    KS_AMVP_MODE_WEAVE = 0
    KS_AMVP_MODE_BOBINTERLEAVED = 1
    KS_AMVP_MODE_BOBNONINTERLEAVED = 2
    KS_AMVP_MODE_SKIPEVEN = 3
    KS_AMVP_MODE_SKIPODD = 4


# AMVPDIMINFO

class tagKS_AMVPDIMINFO(ctypes.Structure):
    _fields_ = [
        ('dwFieldWidth', DWORD),
        ('dwFieldHeight', DWORD),
        ('dwVBIWidth', DWORD),
        ('dwVBIHeight', DWORD),
        ('rcValidRegion', RECT),
    ]


KS_AMVPDIMINFO = tagKS_AMVPDIMINFO
PKS_AMVPDIMINFO = POINTER(tagKS_AMVPDIMINFO)


# [out] field width
# [out] field height
# [out] VBI data width
# [out] VBI data height
# [out] valid rect for data cropping
# AMVPDATAINFO

class tagKS_AMVPDATAINFO(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwMicrosecondsPerField', DWORD),
        ('amvpDimInfo', KS_AMVPDIMINFO),
        ('dwPictAspectRatioX', DWORD),
        ('dwPictAspectRatioY', DWORD),
        ('bEnableDoubleClock', BOOL),
        ('bEnableVACT', BOOL),
        ('bDataIsInterlaced', BOOL),
        ('lHalfLinesOdd', LONG),
        ('bFieldPolarityInverted', BOOL),
        ('dwNumLinesInVREF', DWORD),
        ('lHalfLinesEven', LONG),
        ('dwReserved1', DWORD),
    ]


KS_AMVPDATAINFO = tagKS_AMVPDATAINFO
PKS_AMVPDATAINFO = POINTER(tagKS_AMVPDATAINFO)


# Size of the struct
# Time taken by each field
# Dimensional Information
# Pict aspect ratio in X dimn
# Pict aspect ratio in Y dimn
# Videoport should enable DOUBLE clocking
# Videoport should use an external VACT signal
# Indicates that the signal is INTerlaced
# number of halflines in the odd field
# Device inverts the polarity by default
# Number of lines of data in VREF
# number of halflines in the even field
# Reserved for future use
# AMVPSIZE

class tagKS_AMVPSIZE(ctypes.Structure):
    _fields_ = [
        ('dwWidth', DWORD),
        ('dwHeight', DWORD),
    ]


KS_AMVPSIZE = tagKS_AMVPSIZE
PKS_AMVPSIZE = POINTER(tagKS_AMVPSIZE)


# [in] width in pixels
# [in] height in pixels
# ==========================================================================
# End of VPType.h header info
# ==========================================================================



class KSEVENT_VPNOTIFY(ENUM):
    KSEVENT_VPNOTIFY_FORMATCHANGE = 0


class KSEVENT_VIDCAPTOSTI(ENUM):
    KSEVENT_VIDCAPTOSTI_EXT_TRIGGER = 0
    KSEVENT_VIDCAP_AUTO_UPDATE = 1
    KSEVENT_VIDCAP_SEARCH = 2


# XP SP2 and later (chronologically)
# Extension Unit Properties
class KSPROPERTY_EXTENSION_UNIT(ENUM):
    KSPROPERTY_EXTENSION_UNIT_INFO = 0
    KSPROPERTY_EXTENSION_UNIT_CONTROL = 1
    KSPROPERTY_EXTENSION_UNIT_PASS_THROUGH = 0xFFFF


PKSPROPERTY_EXTENSION_UNIT = POINTER(KSPROPERTY_EXTENSION_UNIT)



class KSEVENT_VPVBINOTIFY(ENUM):
    KSEVENT_VPVBINOTIFY_FORMATCHANGE = 0





class _KSGOP_USERDATA(ctypes.Structure):
    _fields_ = [
        ('sc', ULONG),
        ('reserved1', ULONG),
        ('cFields', BYTE),
        ('l21Data', CHAR * 3),
    ]


KSGOP_USERDATA = _KSGOP_USERDATA
PKSGOP_USERDATA = POINTER(_KSGOP_USERDATA)



# -----------------------------------------------------------------------
# KS_AM_KSPROPSETID_TSRateChange property set definitions for time stamp
KS_AM_UseNewCSSKey = 0x0001



# rw, use KS_AM_ExactRateChange
class KS_AM_PROPERTY_TS_RATE_CHANGE(ENUM):
    KS_AM_RATE_SimpleRateChange = 1
    KS_AM_RATE_ExactRateChange = 2
    KS_AM_RATE_MaxFullDataRate = 3
    KS_AM_RATE_Step = 4


# r, use KS_AM_MaxFullDataRate
# w, use KS_AM_Step
# this is the simplest mechanism to set a time stamp rate change on

class KS_AM_SimpleRateChange(ctypes.Structure):
    _fields_ = [
        ('StartTime', REFERENCE_TIME),
        ('Rate', LONG),
    ]


PKS_AM_SimpleRateChange = POINTER(KS_AM_SimpleRateChange)


# a filter (simplest for the person setting the rate change, harder
# for the filter doing the rate change).
# stream time at which to start this rate
# new rate * 10000 (decimal)
# input TS that maps to zero output TS

class KS_AM_ExactRateChange(ctypes.Structure):
    _fields_ = [
        ('OutputZeroTime', REFERENCE_TIME),
        ('Rate', LONG),
    ]


PKS_AM_ExactRateChange = POINTER(KS_AM_ExactRateChange)


# new rate * 10000 (decimal)
# rate * 10000 (decimal)
# number of frame to step
KS_AM_MaxFullDataRate = LONG
KS_AM_Step = DWORD


# ===========================================================================
# ENCODER API DEFINITIONS
# ===========================================================================

class VIDEOENCODER_BITRATE_MODE(ENUM):
    ConstantBitRate = 0
    VariableBitRateAverage = 1
    VariableBitRatePeak = 2


# Bit rate used for encoding is constant


# Bit rate used for encoding is variable with the specified bitrate used
# as a guaranteed average over a specified window.  The default window
# size is considered to be 5 minutes.


# Bit rate used for encoding is variable with the specified bitrate used
# as an average with a peak not to exceed the specified peak bitrate over
# a specified window.  The default window size is considered to be 500ms
# (classically one GOP).


# __ENCODER_API_DEFINES__
# ===========================================================================
# JACK DESCRIPTION DEFINITIONS
# ===========================================================================

class KSPROPERTY_JACK(ENUM):
    KSPROPERTY_JACK_DESCRIPTION = 1
    KSPROPERTY_JACK_DESCRIPTION2 = 2
    KSPROPERTY_JACK_SINK_INFO = 3
    KSPROPERTY_JACK_CONTAINERID = 4


# Enums used in KSPROPERTY_JACK_INFO_STRUCT
class EPcxConnectionType(ENUM):
    eConnTypeUnknown = 0
    eConnType3PoINT5mm = 1
    eConnTypeQuarter = 2
    eConnTypeAtapiInternal = 3
    eConnTypeRCA = 4
    eConnTypeOptical = 5
    eConnTypeOtherDigital = 6
    eConnTypeOtherAnalog = 7
    eConnTypeMultichannelAnalogDIN = 8
    eConnTypeXlrProfessional = 9
    eConnTypeRJ11Modem = 10
    eConnTypeCombination = 11


class EPcxGeoLocation(ENUM):
    eGeoLocRear = 0x1
    eGeoLocFront = 2
    eGeoLocLeft = 3
    eGeoLocRight = 4
    eGeoLocTop = 5
    eGeoLocBottom = 6
    eGeoLocRearPanel = 7
    eGeoLocRiser = 8
    eGeoLocInsideMobileLid = 9
    eGeoLocDrivebay = 10
    eGeoLocHDMI = 11
    eGeoLocOutsideMobileLid = 12
    eGeoLocATAPI = 13
    eGeoLocNotApplicable = 14
    eGeoLocReserved6 = 15
    EPcxGeoLocation_enum_count = 16
    eGeoLocReserved5 = eGeoLocNotApplicable


class EPcxGenLocation(ENUM):
    eGenLocPrimaryBox = 0
    eGenLocInternal = 1
    eGenLocSeparate = 2
    eGenLocOther = 3
    EPcxGenLocation_enum_count = 4


class EPxcPortConnection(ENUM):
    ePortConnJack = 0
    ePortConnIntegratedDevice = 1
    ePortConnBothIntegratedAndJack = 2
    ePortConnUnknown = 3


# structure for KSPROPERTY_JACK_DESCRIPTION pin property
class KSJACK_DESCRIPTION(ctypes.Structure):
    _fields_ = [
        ('ChannelMapping', DWORD),
        ('Color', DWORD),
        ('ConnectionType', EPcxConnectionType),
        ('GeoLocation', EPcxGeoLocation),
        ('GenLocation', EPcxGenLocation),
        ('PortConnection', EPxcPortConnection),
        ('IsConnected', BOOL),
    ]


PKSJACK_DESCRIPTION = POINTER(KSJACK_DESCRIPTION)


# 0x00rrggbb; (NOT a COLORREF)
# HDMI
class KSJACK_SINK_CONNECTIONTYPE(ENUM):
    KSJACK_SINK_CONNECTIONTYPE_HDMI = 0
    KSJACK_SINK_CONNECTIONTYPE_DISPLAYPORT = 1


# DisplayPort
MAX_SINK_DESCRIPTION_NAME_LENGTH = 0x20


class _tagKSJACK_SINK_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('ConnType', KSJACK_SINK_CONNECTIONTYPE),
        ('ManufacturerId', WORD),
        ('ProductId', WORD),
        ('AudioLatency', WORD),
        ('HDCPCapable', BOOL),
        ('AICapable', BOOL),
        ('SinkDescriptionLength', UCHAR),
        ('SinkDescription', WCHAR * MAX_SINK_DESCRIPTION_NAME_LENGTH),
        ('PortId', LUID),
    ]


KSJACK_SINK_INFORMATION = _tagKSJACK_SINK_INFORMATION
PKSJACK_SINK_INFORMATION = POINTER(_tagKSJACK_SINK_INFORMATION)


# Connection Type
# Sink manufacturer ID
# Sink product ID
# Sink audio latency
# HDCP Support
# ACP Packet, ISRC1, and ISRC2 Support
# Monitor/Sink name length
# Monitor/Sink name
# Video port identifier
JACKDESC2_PRESENCE_DETECT_CAPABILITY = 0x00000001
JACKDESC2_DYNAMIC_FORMAT_CHANGE_CAPABILITY = 0x00000002


class _tagKSJACK_DESCRIPTION2(ctypes.Structure):
    _fields_ = [
        ('DeviceStateInfo', DWORD),
        ('JackCapabilities', DWORD),
    ]


KSJACK_DESCRIPTION2 = _tagKSJACK_DESCRIPTION2
PKSJACK_DESCRIPTION2 = POINTER(_tagKSJACK_DESCRIPTION2)


# Top 16 bits: Report current device state, active, streaming, idle, or
# hardware not ready
# Bottom 16 bits: detailed reason to further explain state in top 16 bits
# Report jack capabilities such as jack presence detection capability
# or dynamic format changing capability



KSPROPERTY_AUDIO_BUFFER_DURATION = 0x1


# ===========================================================================
# HARDWARE AUDIO ENGINE DEFINITIONS
# ===========================================================================



class KSPROPERTY_AUDIOENGINE(ENUM):
    KSPROPERTY_AUDIOENGINE_LFXENABLE = 0
    KSPROPERTY_AUDIOENGINE_GFXENABLE = 1
    KSPROPERTY_AUDIOENGINE_MIXFORMAT = 2
    KSPROPERTY_AUDIOENGINE_DEVICEFORMAT = 4
    KSPROPERTY_AUDIOENGINE_SUPPORTEDDEVICEFORMATS = 5
    KSPROPERTY_AUDIOENGINE_DESCRIPTOR = 6
    KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE = 7
    KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION = 8
    KSPROPERTY_AUDIOENGINE_VOLUMELEVEL = 9


# constant "3" was skipped on purpose for backward compatibility
# from the removal of unused KSPROPERTY_AUDIOENGINE_PROCESSINGPERIOD
class _tagKSAUDIOENGINE_DESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('nHostPinId', UINT),
        ('nOffloadPinId', UINT),
        ('nLoopbackPinId', UINT),
    ]


KSAUDIOENGINE_DESCRIPTOR = _tagKSAUDIOENGINE_DESCRIPTOR
PKSAUDIOENGINE_DESCRIPTOR = POINTER(_tagKSAUDIOENGINE_DESCRIPTOR)


class _tagKSAUDIOENGINE_BUFFER_SIZE_RANGE(ctypes.Structure):
    _fields_ = [
        ('MinBufferBytes', ULONG),
        ('MaxBufferBytes', ULONG),
    ]


KSAUDIOENGINE_BUFFER_SIZE_RANGE = _tagKSAUDIOENGINE_BUFFER_SIZE_RANGE
PKSAUDIOENGINE_BUFFER_SIZE_RANGE = POINTER(_tagKSAUDIOENGINE_BUFFER_SIZE_RANGE)


class AUDIO_CURVE_TYPE(ENUM):
    AUDIO_CURVE_TYPE_NONE = 0
    AUDIO_CURVE_TYPE_WINDOWS_FADE = 1


class _tagKSAUDIOENGINE_VOLUMELEVEL(ctypes.Structure):
    _fields_ = [
        ('TargetVolume', LONG),
        ('CurveType', AUDIO_CURVE_TYPE),
        ('CurveDuration', ULONGLONG),
    ]


KSAUDIOENGINE_VOLUMELEVEL = _tagKSAUDIOENGINE_VOLUMELEVEL
PKSAUDIOENGINE_VOLUMELEVEL = POINTER(_tagKSAUDIOENGINE_VOLUMELEVEL)


# ===========================================================================
# AUDIO SIGNAL PROCESSING DEFINITIONS
# ===========================================================================



class KSPROPERTY_AUDIOSIGNALPROCESSING(ENUM):
    KSPROPERTY_AUDIOSIGNALPROCESSING_MODES = 0



class tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE(ctypes.Structure):
    _fields_ = [
        ('AttributeHeader', KSATTRIBUTE),
        ('SignalProcessingMode', GUID),
    ]


KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE = (
    tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE
)
PKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE = POINTER(
    tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE
)


class KSPROPERTY_AUDIOMODULE(ENUM):
    KSPROPERTY_AUDIOMODULE_DESCRIPTORS = 1
    KSPROPERTY_AUDIOMODULE_COMMAND = 2
    KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID = 3


AUDIOMODULE_MAX_DATA_SIZE = 0xFA00
AUDIOMODULE_MAX_NAME_CCH_SIZE = 0x80


class _KSAUDIOMODULE_DESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('ClassId', GUID),
        ('InstanceId', ULONG),
        ('VersionMajor', ULONG),
        ('VersionMinor', ULONG),
        ('Name', WCHAR * AUDIOMODULE_MAX_NAME_CCH_SIZE),
    ]


KSAUDIOMODULE_DESCRIPTOR = _KSAUDIOMODULE_DESCRIPTOR
PKSAUDIOMODULE_DESCRIPTOR = POINTER(_KSAUDIOMODULE_DESCRIPTOR)


class _KSAUDIOMODULE_PROPERTY(ctypes.Structure):
    _fields_ = [
        ('Property', KSPROPERTY),
        ('ClassId', GUID),
        ('InstanceId', ULONG),
    ]


KSAUDIOMODULE_PROPERTY = _KSAUDIOMODULE_PROPERTY
PKSAUDIOMODULE_PROPERTY = POINTER(_KSAUDIOMODULE_PROPERTY)



class _KSAUDIOMODULE_NOTIFICATION(ctypes.Structure):

    class _Union_0(ctypes.Union):

        class ProviderId(ctypes.Structure):
            _fields_ = [
                ('DeviceId', GUID),
                ('ClassId', GUID),
                ('InstanceId', ULONG),
                ('Reserved', ULONG),
            ]

        _fields_ = [
            ('ProviderId', ProviderId),
            ('Alignment', LONGLONG),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('_Union_0', _Union_0),
    ]


KSAUDIOMODULE_NOTIFICATION = _KSAUDIOMODULE_NOTIFICATION
PKSAUDIOMODULE_NOTIFICATION = POINTER(_KSAUDIOMODULE_NOTIFICATION)

# CLSID

STATIC_CLSID_KsIBasicAudioInterfaceHandler = (
    0xB9F8AC3E,
    0x0F71,
    0x11D2,
    0xB7,
    0x2C,
    0x00,
    0xC0,
    0x4F,
    0xB6,
    0xBD,
    0x3D,
)
CLSID_KsIBasicAudioInterfaceHandler = DEFINE_GUIDSTRUCT(
    "b9f8ac3e-0f71-11d2-b72c-00c04fb6bd3d"
)
CLSID_KsIBasicAudioInterfaceHandler = DEFINE_GUIDNAMED(
    CLSID_KsIBasicAudioInterfaceHandler
)


# PROPSETID

STATIC_PROPSETID_ALLOCATOR_CONTROL = (
    0x53171960,
    0x148E,
    0x11D2,
    0x99,
    0x79,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PROPSETID_ALLOCATOR_CONTROL = DEFINE_GUIDSTRUCT(
    "53171960-148E-11d2-9979-0000C0CC16BA"
)
PROPSETID_ALLOCATOR_CONTROL = DEFINE_GUIDNAMED(
    PROPSETID_ALLOCATOR_CONTROL
)


STATIC_PROPSETID_VIDCAP_VIDEOPROCAMP = (
    0xC6E13360,
    0x30AC,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_VIDEOPROCAMP = DEFINE_GUIDSTRUCT(
    "C6E13360-30AC-11d0-A18C-00A0C9118956"
)
PROPSETID_VIDCAP_VIDEOPROCAMP = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_VIDEOPROCAMP
)


STATIC_PROPSETID_VIDCAP_SELECTOR = (
    0x1ABDAECA,
    0x68B6,
    0x4F83,
    0x93,
    0x71,
    0xB4,
    0x13,
    0x90,
    0x7C,
    0x7B,
    0x9F,
)
PROPSETID_VIDCAP_SELECTOR = DEFINE_GUIDSTRUCT(
    "1ABDAECA-68B6-4F83-9371-B413907C7B9F"
)
PROPSETID_VIDCAP_SELECTOR = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_SELECTOR
)


STATIC_PROPSETID_TUNER = (
    0x6A2E0605,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_TUNER = DEFINE_GUIDSTRUCT(
    "6a2e0605-28e4-11d0-a18c-00a0c9118956"
)
PROPSETID_TUNER = DEFINE_GUIDNAMED(
    PROPSETID_TUNER
)


STATIC_PROPSETID_VIDCAP_VIDEOENCODER = (
    0x6A2E0610,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_VIDEOENCODER = DEFINE_GUIDSTRUCT(
    "6a2e0610-28e4-11d0-a18c-00a0c9118956"
)
PROPSETID_VIDCAP_VIDEOENCODER = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_VIDEOENCODER
)


STATIC_PROPSETID_VIDCAP_VIDEODECODER = (
    0xC6E13350,
    0x30AC,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_VIDEODECODER = DEFINE_GUIDSTRUCT(
    "C6E13350-30AC-11d0-A18C-00A0C9118956"
)
PROPSETID_VIDCAP_VIDEODECODER = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_VIDEODECODER
)


STATIC_PROPSETID_VIDCAP_CAMERACONTROL = (
    0xC6E13370,
    0x30AC,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_CAMERACONTROL = DEFINE_GUIDSTRUCT(
    "C6E13370-30AC-11d0-A18C-00A0C9118956"
)
PROPSETID_VIDCAP_CAMERACONTROL = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_CAMERACONTROL
)


STATIC_PROPSETID_VIDCAP_CAMERACONTROL_FLASH = (
    0x785E8F49,
    0x63A2,
    0x4144,
    0xAB,
    0x70,
    0xFF,
    0xB2,
    0x78,
    0xFA,
    0x26,
    0xCE,
)
PROPSETID_VIDCAP_CAMERACONTROL_FLASH = DEFINE_GUIDSTRUCT(
    "785E8F49-63A2-4144-AB70-FFB278FA26CE"
)
PROPSETID_VIDCAP_CAMERACONTROL_FLASH = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_CAMERACONTROL_FLASH
)


STATIC_PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION = (
    0x43964BD3,
    0x7716,
    0x404E,
    0x8B,
    0xE1,
    0xD2,
    0x99,
    0xB2,
    0xE,
    0x50,
    0xFD,
)
PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION = DEFINE_GUIDSTRUCT(
    "43964BD3-7716-404e-8BE1-D299B20E50FD"
)
PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION
)


STATIC_PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST = (
    0x9D12D198,
    0xF86C,
    0x4FED,
    0xB0,
    0x23,
    0x5D,
    0x87,
    0x65,
    0x3D,
    0xA7,
    0x93,
)
PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST = DEFINE_GUIDSTRUCT(
    "9D12D198-F86C-4fed-B023-5D87653DA793"
)
PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST
)


STATIC_PROPSETID_VIDCAP_CAMERACONTROL_IMAGE_PIN_CAPABILITY = (
    0x9D3D7BBF,
    0x5C6D,
    0x4138,
    0xBB,
    0x0,
    0x58,
    0x4E,
    0xDD,
    0x20,
    0xF7,
    0xC5,
)
PROPSETID_VIDCAP_CAMERACONTROL_IMAGE_PIN_CAPABILITY = DEFINE_GUIDSTRUCT(
    "9D3D7BBF-5C6D-4138-BB00-584EDD20F7C5"
)
PROPSETID_VIDCAP_CAMERACONTROL_IMAGE_PIN_CAPABILITY = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_CAMERACONTROL_IMAGE_PIN_CAPABILITY
)


STATIC_PROPSETID_EXT_DEVICE = (
    0xB5730A90,
    0x1A2C,
    0x11CF,
    0x8C,
    0x23,
    0x00,
    0xAA,
    0x00,
    0x6B,
    0x68,
    0x14,
)
PROPSETID_EXT_DEVICE = DEFINE_GUIDSTRUCT(
    "B5730A90-1A2C-11cf-8C23-00AA006B6814"
)
PROPSETID_EXT_DEVICE = DEFINE_GUIDNAMED(
    PROPSETID_EXT_DEVICE
)


STATIC_PROPSETID_EXT_TRANSPORT = (
    0xA03CD5F0,
    0x3045,
    0x11CF,
    0x8C,
    0x44,
    0x00,
    0xAA,
    0x00,
    0x6B,
    0x68,
    0x14,
)
PROPSETID_EXT_TRANSPORT = DEFINE_GUIDSTRUCT(
    "A03CD5F0-3045-11cf-8C44-00AA006B6814"
)
PROPSETID_EXT_TRANSPORT = DEFINE_GUIDNAMED(
    PROPSETID_EXT_TRANSPORT
)


STATIC_PROPSETID_TIMECODE_READER = (
    0x9B496CE1,
    0x811B,
    0x11CF,
    0x8C,
    0x77,
    0x00,
    0xAA,
    0x00,
    0x6B,
    0x68,
    0x14,
)
PROPSETID_TIMECODE_READER = DEFINE_GUIDSTRUCT(
    "9B496CE1-811B-11cf-8C77-00AA006B6814"
)
PROPSETID_TIMECODE_READER = DEFINE_GUIDNAMED(
    PROPSETID_TIMECODE_READER
)


STATIC_PROPSETID_VIDCAP_CROSSBAR = (
    0x6A2E0640,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_CROSSBAR = DEFINE_GUIDSTRUCT(
    "6a2e0640-28e4-11d0-a18c-00a0c9118956"
)
PROPSETID_VIDCAP_CROSSBAR = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_CROSSBAR
)


STATIC_PROPSETID_VIDCAP_TVAUDIO = (
    0x6A2E0650,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_TVAUDIO = DEFINE_GUIDSTRUCT(
    "6a2e0650-28e4-11d0-a18c-00a0c9118956"
)
PROPSETID_VIDCAP_TVAUDIO = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_TVAUDIO
)


STATIC_PROPSETID_VIDCAP_VIDEOCOMPRESSION = (
    0xC6E13343,
    0x30AC,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_VIDEOCOMPRESSION = DEFINE_GUIDSTRUCT(
    "C6E13343-30AC-11d0-A18C-00A0C9118956"
)
PROPSETID_VIDCAP_VIDEOCOMPRESSION = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_VIDEOCOMPRESSION
)


STATIC_PROPSETID_VIDCAP_VIDEOCONTROL = (
    0x6A2E0670,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_VIDEOCONTROL = DEFINE_GUIDSTRUCT(
    "6a2e0670-28e4-11d0-a18c-00a0c9118956"
)
PROPSETID_VIDCAP_VIDEOCONTROL = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_VIDEOCONTROL
)


STATIC_PROPSETID_VIDCAP_DROPPEDFRAMES = (
    0xC6E13344,
    0x30AC,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
PROPSETID_VIDCAP_DROPPEDFRAMES = DEFINE_GUIDSTRUCT(
    "C6E13344-30AC-11d0-A18C-00A0C9118956"
)
PROPSETID_VIDCAP_DROPPEDFRAMES = DEFINE_GUIDNAMED(
    PROPSETID_VIDCAP_DROPPEDFRAMES
)


# BLUETOOTHLE

STATIC_BLUETOOTHLE_MIDI_SERVICE_UUID = (
    0x03B80E5A,
    0xEDE8,
    0x4B33,
    0xA7,
    0x51,
    0x6C,
    0xE3,
    0x4E,
    0xC4,
    0xC7,
    0x00,
)
BLUETOOTHLE_MIDI_SERVICE_UUID = DEFINE_GUIDSTRUCT(
    "03B80E5A-EDE8-4B33-A751-6CE34EC4C700"
)
BLUETOOTHLE_MIDI_SERVICE_UUID = DEFINE_GUIDNAMED(
    BLUETOOTHLE_MIDI_SERVICE_UUID
)


# AUDIO

STATIC_AUDIO_SIGNALPROCESSINGMODE_DEFAULT = (
    0xC18E2F7E,
    0x933D,
    0x4965,
    0xB7,
    0xD1,
    0x1E,
    0xEF,
    0x22,
    0x8D,
    0x2A,
    0xF3,
)
AUDIO_SIGNALPROCESSINGMODE_DEFAULT = DEFINE_GUIDSTRUCT(
    "C18E2F7E-933D-4965-B7D1-1EEF228D2AF3"
)
AUDIO_SIGNALPROCESSINGMODE_DEFAULT = DEFINE_GUIDNAMED(
    AUDIO_SIGNALPROCESSINGMODE_DEFAULT
)


STATIC_AUDIO_SIGNALPROCESSINGMODE_RAW = (
    0x9E90EA20,
    0xB493,
    0x4FD1,
    0xA1,
    0xA8,
    0x7E,
    0x13,
    0x61,
    0xA9,
    0x56,
    0xCF,
)
AUDIO_SIGNALPROCESSINGMODE_RAW = DEFINE_GUIDSTRUCT(
    "9E90EA20-B493-4FD1-A1A8-7E1361A956CF"
)
AUDIO_SIGNALPROCESSINGMODE_RAW = DEFINE_GUIDNAMED(
    AUDIO_SIGNALPROCESSINGMODE_RAW
)


STATIC_AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS = (
    0x98951333,
    0xB9CD,
    0x48B1,
    0xA0,
    0xA3,
    0xFF,
    0x40,
    0x68,
    0x2D,
    0x73,
    0xF7,
)
AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS = DEFINE_GUIDSTRUCT(
    "98951333-B9CD-48B1-A0A3-FF40682D73F7"
)
AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS = DEFINE_GUIDNAMED(
    AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS
)


STATIC_AUDIO_SIGNALPROCESSINGMODE_SPEECH = (
    0xFC1CFC9B,
    0xB9D6,
    0x4CFA,
    0xB5,
    0xE0,
    0x4B,
    0xB2,
    0x16,
    0x68,
    0x78,
    0xB2,
)
AUDIO_SIGNALPROCESSINGMODE_SPEECH = DEFINE_GUIDSTRUCT(
    "FC1CFC9B-B9D6-4CFA-B5E0-4BB2166878B2"
)
AUDIO_SIGNALPROCESSINGMODE_SPEECH = DEFINE_GUIDNAMED(
    AUDIO_SIGNALPROCESSINGMODE_SPEECH
)


STATIC_AUDIO_SIGNALPROCESSINGMODE_NOTIFICATION = (
    0x9CF2A70B,
    0xF377,
    0x403B,
    0xBD,
    0x6B,
    0x36,
    0x8,
    0x63,
    0xE0,
    0x35,
    0x5C,
)
AUDIO_SIGNALPROCESSINGMODE_NOTIFICATION = DEFINE_GUIDSTRUCT(
    "9CF2A70B-F377-403B-BD6B-360863E0355C"
)
AUDIO_SIGNALPROCESSINGMODE_NOTIFICATION = DEFINE_GUIDNAMED(
    AUDIO_SIGNALPROCESSINGMODE_NOTIFICATION
)


STATIC_AUDIO_SIGNALPROCESSINGMODE_MEDIA = (
    0x4780004E,
    0x7133,
    0x41D8,
    0x8C,
    0x74,
    0x66,
    0x0D,
    0xAD,
    0xD2,
    0xC0,
    0xEE,
)
AUDIO_SIGNALPROCESSINGMODE_MEDIA = DEFINE_GUIDSTRUCT(
    "4780004E-7133-41D8-8C74-660DADD2C0EE"
)
AUDIO_SIGNALPROCESSINGMODE_MEDIA = DEFINE_GUIDNAMED(
    AUDIO_SIGNALPROCESSINGMODE_MEDIA
)


STATIC_AUDIO_SIGNALPROCESSINGMODE_MOVIE = (
    0xB26FEB0D,
    0xEC94,
    0x477C,
    0x94,
    0x94,
    0xD1,
    0xAB,
    0x8E,
    0x75,
    0x3F,
    0x6E,
)
AUDIO_SIGNALPROCESSINGMODE_MOVIE = DEFINE_GUIDSTRUCT(
    "B26FEB0D-EC94-477C-9494-D1AB8E753F6E"
)
AUDIO_SIGNALPROCESSINGMODE_MOVIE = DEFINE_GUIDNAMED(
    AUDIO_SIGNALPROCESSINGMODE_MOVIE
)


STATIC_AUDIO_EFFECT_TYPE_ACOUSTIC_ECHO_CANCELLATION = (
    0x6F64ADBE,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_ACOUSTIC_ECHO_CANCELLATION = DEFINE_GUIDSTRUCT(
    "6f64adbe-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_ACOUSTIC_ECHO_CANCELLATION = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_ACOUSTIC_ECHO_CANCELLATION
)


STATIC_AUDIO_EFFECT_TYPE_NOISE_SUPPRESSION = (
    0x6F64ADBF,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_NOISE_SUPPRESSION = DEFINE_GUIDSTRUCT(
    "6f64adbf-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_NOISE_SUPPRESSION = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_NOISE_SUPPRESSION
)


STATIC_AUDIO_EFFECT_TYPE_AUTOMATIC_GAIN_CONTROL = (
    0x6F64ADC0,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_AUTOMATIC_GAIN_CONTROL = DEFINE_GUIDSTRUCT(
    "6f64adc0-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_AUTOMATIC_GAIN_CONTROL = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_AUTOMATIC_GAIN_CONTROL
)


STATIC_AUDIO_EFFECT_TYPE_BEAMFORMING = (
    0x6F64ADC1,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_BEAMFORMING = DEFINE_GUIDSTRUCT(
    "6f64adc1-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_BEAMFORMING = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_BEAMFORMING
)


STATIC_AUDIO_EFFECT_TYPE_CONSTANT_TONE_REMOVAL = (
    0x6F64ADC2,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_CONSTANT_TONE_REMOVAL = DEFINE_GUIDSTRUCT(
    "6f64adc2-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_CONSTANT_TONE_REMOVAL = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_CONSTANT_TONE_REMOVAL
)



STATIC_AUDIO_EFFECT_TYPE_EQUALIZER = (
    0x6F64ADC3,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_EQUALIZER = DEFINE_GUIDSTRUCT(
    "6f64adc3-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_EQUALIZER = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_EQUALIZER
)


STATIC_AUDIO_EFFECT_TYPE_LOUDNESS_EQUALIZER = (
    0x6F64ADC4,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_LOUDNESS_EQUALIZER = DEFINE_GUIDSTRUCT(
    "6f64adc4-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_LOUDNESS_EQUALIZER = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_LOUDNESS_EQUALIZER
)


STATIC_AUDIO_EFFECT_TYPE_BASS_BOOST = (
    0x6F64ADC5,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_BASS_BOOST = DEFINE_GUIDSTRUCT(
    "6f64adc5-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_BASS_BOOST = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_BASS_BOOST
)


STATIC_AUDIO_EFFECT_TYPE_VIRTUAL_SURROUND = (
    0x6F64ADC6,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_VIRTUAL_SURROUND = DEFINE_GUIDSTRUCT(
    "6f64adc6-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_VIRTUAL_SURROUND = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_VIRTUAL_SURROUND
)


STATIC_AUDIO_EFFECT_TYPE_VIRTUAL_HEADPHONES = (
    0x6F64ADC7,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_VIRTUAL_HEADPHONES = DEFINE_GUIDSTRUCT(
    "6f64adc7-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_VIRTUAL_HEADPHONES = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_VIRTUAL_HEADPHONES
)


STATIC_AUDIO_EFFECT_TYPE_SPEAKER_FILL = (
    0x6F64ADC8,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_SPEAKER_FILL = DEFINE_GUIDSTRUCT(
    "6f64adc8-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_SPEAKER_FILL = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_SPEAKER_FILL
)


STATIC_AUDIO_EFFECT_TYPE_ROOM_CORRECTION = (
    0x6F64ADC9,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_ROOM_CORRECTION = DEFINE_GUIDSTRUCT(
    "6f64adc9-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_ROOM_CORRECTION = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_ROOM_CORRECTION
)


STATIC_AUDIO_EFFECT_TYPE_BASS_MANAGEMENT = (
    0x6F64ADCA,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_BASS_MANAGEMENT = DEFINE_GUIDSTRUCT(
    "6f64adca-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_BASS_MANAGEMENT = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_BASS_MANAGEMENT
)


STATIC_AUDIO_EFFECT_TYPE_ENVIRONMENTAL_EFFECTS = (
    0x6F64ADCB,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_ENVIRONMENTAL_EFFECTS = DEFINE_GUIDSTRUCT(
    "6f64adcb-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_ENVIRONMENTAL_EFFECTS = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_ENVIRONMENTAL_EFFECTS
)


STATIC_AUDIO_EFFECT_TYPE_SPEAKER_PROTECTION = (
    0x6F64ADCC,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_SPEAKER_PROTECTION = DEFINE_GUIDSTRUCT(
    "6f64adcc-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_SPEAKER_PROTECTION = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_SPEAKER_PROTECTION
)


STATIC_AUDIO_EFFECT_TYPE_SPEAKER_COMPENSATION = (
    0x6F64ADCD,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_SPEAKER_COMPENSATION = DEFINE_GUIDSTRUCT(
    "6f64adcd-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_SPEAKER_COMPENSATION = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_SPEAKER_COMPENSATION
)


STATIC_AUDIO_EFFECT_TYPE_DYNAMIC_RANGE_COMPRESSION = (
    0x6F64ADCE,
    0x8211,
    0x11E2,
    0x8C,
    0x70,
    0x2C,
    0x27,
    0xD7,
    0xF0,
    0x01,
    0xFA,
)
AUDIO_EFFECT_TYPE_DYNAMIC_RANGE_COMPRESSION = DEFINE_GUIDSTRUCT(
    "6f64adce-8211-11e2-8c70-2c27d7f001fa"
)
AUDIO_EFFECT_TYPE_DYNAMIC_RANGE_COMPRESSION = DEFINE_GUIDNAMED(
    AUDIO_EFFECT_TYPE_DYNAMIC_RANGE_COMPRESSION
)


# KSMUSIC

STATIC_KSMUSIC_TECHNOLOGY_PORT = (
    0x86C92E60,
    0x62E8,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSMUSIC_TECHNOLOGY_PORT = DEFINE_GUIDSTRUCT(
    "86C92E60-62E8-11CF-A5D6-28DB04C10000"
)
KSMUSIC_TECHNOLOGY_PORT = DEFINE_GUIDNAMED(
    KSMUSIC_TECHNOLOGY_PORT
)


STATIC_KSMUSIC_TECHNOLOGY_SQSYNTH = (
    0x0ECF4380,
    0x62E9,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSMUSIC_TECHNOLOGY_SQSYNTH = DEFINE_GUIDSTRUCT(
    "0ECF4380-62E9-11CF-A5D6-28DB04C10000"
)
KSMUSIC_TECHNOLOGY_SQSYNTH = DEFINE_GUIDNAMED(
    KSMUSIC_TECHNOLOGY_SQSYNTH
)


STATIC_KSMUSIC_TECHNOLOGY_FMSYNTH = (
    0x252C5C80,
    0x62E9,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSMUSIC_TECHNOLOGY_FMSYNTH = DEFINE_GUIDSTRUCT(
    "252C5C80-62E9-11CF-A5D6-28DB04C10000"
)
KSMUSIC_TECHNOLOGY_FMSYNTH = DEFINE_GUIDNAMED(
    KSMUSIC_TECHNOLOGY_FMSYNTH
)


STATIC_KSMUSIC_TECHNOLOGY_WAVETABLE = (
    0x394EC7C0,
    0x62E9,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSMUSIC_TECHNOLOGY_WAVETABLE = DEFINE_GUIDSTRUCT(
    "394EC7C0-62E9-11CF-A5D6-28DB04C10000"
)
KSMUSIC_TECHNOLOGY_WAVETABLE = DEFINE_GUIDNAMED(
    KSMUSIC_TECHNOLOGY_WAVETABLE
)


STATIC_KSMUSIC_TECHNOLOGY_SWSYNTH = (
    0x37407736,
    0x3620,
    0x11D1,
    0x85,
    0xD3,
    0x00,
    0x00,
    0xF8,
    0x75,
    0x43,
    0x80,
)
KSMUSIC_TECHNOLOGY_SWSYNTH = DEFINE_GUIDSTRUCT(
    "37407736-3620-11D1-85D3-0000F8754380"
)
KSMUSIC_TECHNOLOGY_SWSYNTH = DEFINE_GUIDNAMED(
    KSMUSIC_TECHNOLOGY_SWSYNTH
)


# KSDATAFORMAT

STATIC_KSDATAFORMAT_TYPE_VIDEO = (
    0x73646976,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_TYPE_VIDEO = DEFINE_GUIDSTRUCT(
    "73646976-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_TYPE_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_VIDEO
)


STATIC_KSDATAFORMAT_TYPE_AUDIO = (
    0x73647561,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_TYPE_AUDIO = DEFINE_GUIDSTRUCT(
    "73647561-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_TYPE_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_AUDIO
)


STATIC_KSDATAFORMAT_TYPE_TEXT = (
    0x73747874,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_TYPE_TEXT = DEFINE_GUIDSTRUCT(
    "73747874-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_TYPE_TEXT = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_TEXT
)


STATIC_KSDATAFORMAT_SUBTYPE_WAVEFORMATEX = (
    0x00000000,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_WAVEFORMATEX = DEFINE_GUIDSTRUCT(
    "00000000-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_WAVEFORMATEX = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_WAVEFORMATEX
)


STATIC_KSDATAFORMAT_SUBTYPE_ANALOG = (
    0x6DBA3190,
    0x67BD,
    0x11CF,
    0xA0,
    0xF7,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSDATAFORMAT_SUBTYPE_ANALOG = DEFINE_GUIDSTRUCT(
    "6dba3190-67bd-11cf-a0f7-0020afd156e4"
)
KSDATAFORMAT_SUBTYPE_ANALOG = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_ANALOG
)


STATIC_KSDATAFORMAT_SUBTYPE_PCM = DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_PCM)
KSDATAFORMAT_SUBTYPE_PCM = DEFINE_GUIDSTRUCT(
    "00000001-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_PCM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_PCM
)


STATIC_KSDATAFORMAT_SUBTYPE_IEEE_FLOAT = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_IEEE_FLOAT)
)
KSDATAFORMAT_SUBTYPE_IEEE_FLOAT = DEFINE_GUIDSTRUCT(
    "00000003-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEEE_FLOAT = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEEE_FLOAT
)


STATIC_KSDATAFORMAT_SUBTYPE_DRM = DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_DRM)
KSDATAFORMAT_SUBTYPE_DRM = DEFINE_GUIDSTRUCT(
    "00000009-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_DRM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_DRM
)


STATIC_KSDATAFORMAT_SUBTYPE_ALAW = DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_ALAW)
KSDATAFORMAT_SUBTYPE_ALAW = DEFINE_GUIDSTRUCT(
    "00000006-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_ALAW = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_ALAW
)


STATIC_KSDATAFORMAT_SUBTYPE_MULAW = DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_MULAW)
KSDATAFORMAT_SUBTYPE_MULAW = DEFINE_GUIDSTRUCT(
    "00000007-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_MULAW = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MULAW
)


STATIC_KSDATAFORMAT_SUBTYPE_ADPCM = DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_ADPCM)
KSDATAFORMAT_SUBTYPE_ADPCM = DEFINE_GUIDSTRUCT(
    "00000002-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_ADPCM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_ADPCM
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEG = DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_MPEG)
KSDATAFORMAT_SUBTYPE_MPEG = DEFINE_GUIDSTRUCT(
    "00000050-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_MPEG = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEG
)


STATIC_KSDATAFORMAT_SPECIFIER_VC_ID = (
    0xAD98D184,
    0xAAC3,
    0x11D0,
    0xA4,
    0x1C,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSDATAFORMAT_SPECIFIER_VC_ID = DEFINE_GUIDSTRUCT(
    "AD98D184-AAC3-11D0-A41C-00A0C9223196"
)
KSDATAFORMAT_SPECIFIER_VC_ID = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_VC_ID
)


STATIC_KSDATAFORMAT_SPECIFIER_WAVEFORMATEX = (
    0x05589F81,
    0xC356,
    0x11CE,
    0xBF,
    0x01,
    0x00,
    0xAA,
    0x00,
    0x55,
    0x59,
    0x5A,
)
KSDATAFORMAT_SPECIFIER_WAVEFORMATEX = DEFINE_GUIDSTRUCT(
    "05589f81-c356-11ce-bf01-00aa0055595a"
)
KSDATAFORMAT_SPECIFIER_WAVEFORMATEX = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_WAVEFORMATEX
)


STATIC_KSDATAFORMAT_SPECIFIER_DSOUND = (
    0x518590A2,
    0xA184,
    0x11D0,
    0x85,
    0x22,
    0x00,
    0xC0,
    0x4F,
    0xD9,
    0xBA,
    0xF3,
)
KSDATAFORMAT_SPECIFIER_DSOUND = DEFINE_GUIDSTRUCT(
    "518590a2-a184-11d0-8522-00c04fd9baf3"
)
KSDATAFORMAT_SPECIFIER_DSOUND = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_DSOUND
)


STATIC_KSDATAFORMAT_SUBTYPE_RIFF = (
    0x4995DAEE,
    0x9EE6,
    0x11D0,
    0xA4,
    0x0E,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSDATAFORMAT_SUBTYPE_RIFF = DEFINE_GUIDSTRUCT(
    "4995DAEE-9EE6-11D0-A40E-00A0C9223196"
)
KSDATAFORMAT_SUBTYPE_RIFF = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_RIFF
)


STATIC_KSDATAFORMAT_SUBTYPE_RIFFWAVE = (
    0xE436EB8B,
    0x524F,
    0x11CE,
    0x9F,
    0x53,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70,
)
KSDATAFORMAT_SUBTYPE_RIFFWAVE = DEFINE_GUIDSTRUCT(
    "e436eb8b-524f-11ce-9f53-0020af0ba770"
)
KSDATAFORMAT_SUBTYPE_RIFFWAVE = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_RIFFWAVE
)


STATIC_KSDATAFORMAT_TYPE_MUSIC = (
    0xE725D360,
    0x62CC,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSDATAFORMAT_TYPE_MUSIC = DEFINE_GUIDSTRUCT(
    "E725D360-62CC-11CF-A5D6-28DB04C10000"
)
KSDATAFORMAT_TYPE_MUSIC = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_MUSIC
)



STATIC_KSDATAFORMAT_TYPE_MIDI = (
    0x7364696D,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_TYPE_MIDI = DEFINE_GUIDSTRUCT(
    "7364696D-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_TYPE_MIDI = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_MIDI
)


STATIC_KSDATAFORMAT_SUBTYPE_MIDI = (
    0x1D262760,
    0xE957,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSDATAFORMAT_SUBTYPE_MIDI = DEFINE_GUIDSTRUCT(
    "1D262760-E957-11CF-A5D6-28DB04C10000"
)
KSDATAFORMAT_SUBTYPE_MIDI = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MIDI
)


STATIC_KSDATAFORMAT_SUBTYPE_MIDI_BUS = (
    0x2CA15FA0,
    0x6CFE,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSDATAFORMAT_SUBTYPE_MIDI_BUS = DEFINE_GUIDSTRUCT(
    "2CA15FA0-6CFE-11CF-A5D6-28DB04C10000"
)
KSDATAFORMAT_SUBTYPE_MIDI_BUS = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MIDI_BUS
)


STATIC_KSDATAFORMAT_SUBTYPE_RIFFMIDI = (
    0x4995DAF0,
    0x9EE6,
    0x11D0,
    0xA4,
    0x0E,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSDATAFORMAT_SUBTYPE_RIFFMIDI = DEFINE_GUIDSTRUCT(
    "4995DAF0-9EE6-11D0-A40E-00A0C9223196"
)
KSDATAFORMAT_SUBTYPE_RIFFMIDI = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_RIFFMIDI
)


STATIC_KSDATAFORMAT_TYPE_STANDARD_ELEMENTARY_STREAM = (
    0x36523B11,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_TYPE_STANDARD_ELEMENTARY_STREAM = DEFINE_GUIDSTRUCT(
    "36523B11-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_TYPE_STANDARD_ELEMENTARY_STREAM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_STANDARD_ELEMENTARY_STREAM
)


STATIC_KSDATAFORMAT_TYPE_STANDARD_PES_PACKET = (
    0x36523B12,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_TYPE_STANDARD_PES_PACKET = DEFINE_GUIDSTRUCT(
    "36523B12-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_TYPE_STANDARD_PES_PACKET = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_STANDARD_PES_PACKET
)


STATIC_KSDATAFORMAT_TYPE_STANDARD_PACK_HEADER = (
    0x36523B13,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_TYPE_STANDARD_PACK_HEADER = DEFINE_GUIDSTRUCT(
    "36523B13-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_TYPE_STANDARD_PACK_HEADER = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_STANDARD_PACK_HEADER
)


STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO = (
    0x36523B21,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO = DEFINE_GUIDSTRUCT(
    "36523B21-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO
)


STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO = (
    0x36523B22,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO = DEFINE_GUIDSTRUCT(
    "36523B22-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO = (
    0x36523B23,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO = DEFINE_GUIDSTRUCT(
    "36523B23-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO
)


STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO = (
    0x36523B24,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO = DEFINE_GUIDSTRUCT(
    "36523B24-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO = (
    0x36523B25,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO = DEFINE_GUIDSTRUCT(
    "36523B25-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO
)


STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO = (
    0x36523B31,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO = DEFINE_GUIDSTRUCT(
    "36523B31-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO
)


STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO = (
    0x36523B32,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO = DEFINE_GUIDSTRUCT(
    "36523B32-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO
)


STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO = (
    0x36523B33,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO = DEFINE_GUIDSTRUCT(
    "36523B33-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO
)


STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO = (
    0x36523B34,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO = DEFINE_GUIDSTRUCT(
    "36523B34-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO
)


STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO = (
    0x36523B35,
    0x8EE5,
    0x11D1,
    0x8C,
    0xA3,
    0x00,
    0x60,
    0xB0,
    0x57,
    0x66,
    0x4A,
)
KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO = DEFINE_GUIDSTRUCT(
    "36523B35-8EE5-11d1-8CA3-0060B057664A"
)
KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_DSS_VIDEO = (
    0xA0AF4F81,
    0xE163,
    0x11D0,
    0xBA,
    0xD9,
    0x00,
    0x60,
    0x97,
    0x44,
    0x11,
    0x1A,
)
KSDATAFORMAT_SUBTYPE_DSS_VIDEO = DEFINE_GUIDSTRUCT(
    "a0af4f81-e163-11d0-bad9-00609744111a"
)
KSDATAFORMAT_SUBTYPE_DSS_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_DSS_VIDEO
)


STATIC_KSDATAFORMAT_SUBTYPE_DSS_AUDIO = (
    0xA0AF4F82,
    0xE163,
    0x11D0,
    0xBA,
    0xD9,
    0x00,
    0x60,
    0x97,
    0x44,
    0x11,
    0x1A,
)
KSDATAFORMAT_SUBTYPE_DSS_AUDIO = DEFINE_GUIDSTRUCT(
    "a0af4f82-e163-11d0-bad9-00609744111a"
)
KSDATAFORMAT_SUBTYPE_DSS_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_DSS_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEG1Packet = (
    0xE436EB80,
    0x524F,
    0x11CE,
    0x9F,
    0x53,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70,
)
KSDATAFORMAT_SUBTYPE_MPEG1Packet = DEFINE_GUIDSTRUCT(
    "e436eb80-524f-11ce-9F53-0020af0ba770"
)
KSDATAFORMAT_SUBTYPE_MPEG1Packet = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEG1Packet
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEG1Payload = (
    0xE436EB81,
    0x524F,
    0x11CE,
    0x9F,
    0x53,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70,
)
KSDATAFORMAT_SUBTYPE_MPEG1Payload = DEFINE_GUIDSTRUCT(
    "e436eb81-524f-11ce-9F53-0020af0ba770"
)
KSDATAFORMAT_SUBTYPE_MPEG1Payload = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEG1Payload
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEG1Video = (
    0xE436EB86,
    0x524F,
    0x11CE,
    0x9F,
    0x53,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70,
)
KSDATAFORMAT_SUBTYPE_MPEG1Video = DEFINE_GUIDSTRUCT(
    "e436eb86-524f-11ce-9f53-0020af0ba770"
)
KSDATAFORMAT_SUBTYPE_MPEG1Video = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEG1Video
)


STATIC_KSDATAFORMAT_SPECIFIER_MPEG1_VIDEO = (
    0x05589F82,
    0xC356,
    0x11CE,
    0xBF,
    0x01,
    0x00,
    0xAA,
    0x00,
    0x55,
    0x59,
    0x5A,
)
KSDATAFORMAT_SPECIFIER_MPEG1_VIDEO = DEFINE_GUIDSTRUCT(
    "05589f82-c356-11ce-bf01-00aa0055595a"
)
KSDATAFORMAT_SPECIFIER_MPEG1_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_MPEG1_VIDEO
)


STATIC_KSDATAFORMAT_TYPE_MPEG2_PES = (
    0xE06D8020,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_TYPE_MPEG2_PES = DEFINE_GUIDSTRUCT(
    "e06d8020-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_TYPE_MPEG2_PES = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_MPEG2_PES
)


STATIC_KSDATAFORMAT_TYPE_MPEG2_PROGRAM = (
    0xE06D8022,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_TYPE_MPEG2_PROGRAM = DEFINE_GUIDSTRUCT(
    "e06d8022-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_TYPE_MPEG2_PROGRAM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_MPEG2_PROGRAM
)


STATIC_KSDATAFORMAT_TYPE_MPEG2_TRANSPORT = (
    0xE06D8023,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_TYPE_MPEG2_TRANSPORT = DEFINE_GUIDSTRUCT(
    "e06d8023-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_TYPE_MPEG2_TRANSPORT = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_MPEG2_TRANSPORT
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEG2_VIDEO = (
    0xE06D8026,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SUBTYPE_MPEG2_VIDEO = DEFINE_GUIDSTRUCT(
    "e06d8026-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SUBTYPE_MPEG2_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEG2_VIDEO
)


STATIC_KSDATAFORMAT_SPECIFIER_MPEG2_VIDEO = (
    0xE06D80E3,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SPECIFIER_MPEG2_VIDEO = DEFINE_GUIDSTRUCT(
    "e06d80e3-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SPECIFIER_MPEG2_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_MPEG2_VIDEO
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEG2_AUDIO = (
    0xE06D802B,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SUBTYPE_MPEG2_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d802b-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SUBTYPE_MPEG2_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEG2_AUDIO
)


STATIC_KSDATAFORMAT_SPECIFIER_MPEG2_AUDIO = (
    0xE06D80E5,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SPECIFIER_MPEG2_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d80e5-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SPECIFIER_MPEG2_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_MPEG2_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_LPCM_AUDIO = (
    0xE06D8032,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SUBTYPE_LPCM_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d8032-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SUBTYPE_LPCM_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_LPCM_AUDIO
)


STATIC_KSDATAFORMAT_SPECIFIER_LPCM_AUDIO = (
    0xE06D80E6,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SPECIFIER_LPCM_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d80e6-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SPECIFIER_LPCM_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_LPCM_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_AC3_AUDIO = (
    0xE06D802C,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SUBTYPE_AC3_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d802c-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SUBTYPE_AC3_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_AC3_AUDIO
)


STATIC_KSDATAFORMAT_SPECIFIER_AC3_AUDIO = (
    0xE06D80E4,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SPECIFIER_AC3_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d80e4-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SPECIFIER_AC3_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_AC3_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_DOLBY_AC3_SPDIF)
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL = DEFINE_GUIDSTRUCT(
    "00000092-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_WMASPDIF)
)
KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO = DEFINE_GUIDSTRUCT(
    "00000164-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DTS = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_DTS)
)
KSDATAFORMAT_SUBTYPE_IEC61937_DTS = DEFINE_GUIDSTRUCT(
    "00000008-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DTS = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DTS
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_MPEG1 = (
    0x00000003,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_MPEG1 = DEFINE_GUIDSTRUCT(
    "00000003-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_MPEG1 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_MPEG1
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_MPEG2 = (
    0x00000004,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_MPEG2 = DEFINE_GUIDSTRUCT(
    "00000004-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_MPEG2 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_MPEG2
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_MPEG3 = (
    0x00000005,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_MPEG3 = DEFINE_GUIDSTRUCT(
    "00000005-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_MPEG3 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_MPEG3
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_AAC = (
    0x00000006,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_AAC = DEFINE_GUIDSTRUCT(
    "00000006-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_AAC = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_AAC
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_ATRAC = (
    0x00000008,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_ATRAC = DEFINE_GUIDSTRUCT(
    "00000008-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_ATRAC = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_ATRAC
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_ONE_BIT_AUDIO = (
    0x00000009,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_ONE_BIT_AUDIO = DEFINE_GUIDSTRUCT(
    "00000009-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_ONE_BIT_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_ONE_BIT_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS = (
    0x0000000A,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS = DEFINE_GUIDSTRUCT(
    "0000000a-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS_ATMOS = (
    0x0000010A,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS_ATMOS = DEFINE_GUIDSTRUCT(
    "0000010a-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS_ATMOS = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS_ATMOS
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD = (
    0x0000000B,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD = DEFINE_GUIDSTRUCT(
    "0000000b-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP = (
    0x0000000C,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP = DEFINE_GUIDSTRUCT(
    "0000000c-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT20 = (
    0x0000010C,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT20 = DEFINE_GUIDSTRUCT(
    "0000010c-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT20 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT20
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT21 = (
    0x0000030C,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT21 = DEFINE_GUIDSTRUCT(
    "0000030c-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT21 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT21
)


STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DST = (
    0x0000000D,
    0x0CEA,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IEC61937_DST = DEFINE_GUIDSTRUCT(
    "0000000d-0cea-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IEC61937_DST = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IEC61937_DST
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEGLAYER3 = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_MPEGLAYER3)
)
KSDATAFORMAT_SUBTYPE_MPEGLAYER3 = DEFINE_GUIDSTRUCT(
    "00000055-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_MPEGLAYER3 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEGLAYER3
)


STATIC_KSDATAFORMAT_SUBTYPE_MPEG_HEAAC = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_MPEG_HEAAC)
)
KSDATAFORMAT_SUBTYPE_MPEG_HEAAC = DEFINE_GUIDSTRUCT(
    "00001610-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_MPEG_HEAAC = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MPEG_HEAAC
)


STATIC_KSDATAFORMAT_SUBTYPE_WMAUDIO2 = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_WMAUDIO2)
)
KSDATAFORMAT_SUBTYPE_WMAUDIO2 = DEFINE_GUIDSTRUCT(
    "00000161-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_WMAUDIO2 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_WMAUDIO2
)


STATIC_KSDATAFORMAT_SUBTYPE_WMAUDIO3 = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_WMAUDIO3)
)
KSDATAFORMAT_SUBTYPE_WMAUDIO3 = DEFINE_GUIDSTRUCT(
    "00000162-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_WMAUDIO3 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_WMAUDIO3
)


STATIC_KSDATAFORMAT_SUBTYPE_WMAUDIO_LOSSLESS = (
    DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_WMAUDIO_LOSSLESS)
)
KSDATAFORMAT_SUBTYPE_WMAUDIO_LOSSLESS = DEFINE_GUIDSTRUCT(
    "00000163-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_WMAUDIO_LOSSLESS = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_WMAUDIO_LOSSLESS
)


STATIC_KSDATAFORMAT_SUBTYPE_DTS_AUDIO = (
    0xE06D8033,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SUBTYPE_DTS_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d8033-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SUBTYPE_DTS_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_DTS_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_SDDS_AUDIO = (
    0xE06D8034,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SUBTYPE_SDDS_AUDIO = DEFINE_GUIDSTRUCT(
    "e06d8034-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SUBTYPE_SDDS_AUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_SDDS_AUDIO
)


STATIC_KSDATAFORMAT_SUBTYPE_SUBPICTURE = (
    0xE06D802D,
    0xDB46,
    0x11CF,
    0xB4,
    0xD1,
    0x00,
    0x80,
    0x5F,
    0x6C,
    0xBB,
    0xEA,
)
KSDATAFORMAT_SUBTYPE_SUBPICTURE = DEFINE_GUIDSTRUCT(
    "e06d802d-db46-11cf-b4d1-00805f6cbbea"
)
KSDATAFORMAT_SUBTYPE_SUBPICTURE = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_SUBPICTURE
)


STATIC_KSDATAFORMAT_SUBTYPE_VPVideo = (
    0x5A9B6A40,
    0x1A22,
    0x11D1,
    0xBA,
    0xD9,
    0x0,
    0x60,
    0x97,
    0x44,
    0x11,
    0x1A,
)
KSDATAFORMAT_SUBTYPE_VPVideo = DEFINE_GUIDSTRUCT(
    "5a9b6a40-1a22-11d1-bad9-00609744111a"
)
KSDATAFORMAT_SUBTYPE_VPVideo = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_VPVideo
)


STATIC_KSDATAFORMAT_SUBTYPE_VPVBI = (
    0x5A9B6A41,
    0x1A22,
    0x11D1,
    0xBA,
    0xD9,
    0x0,
    0x60,
    0x97,
    0x44,
    0x11,
    0x1A,
)
KSDATAFORMAT_SUBTYPE_VPVBI = DEFINE_GUIDSTRUCT(
    "5a9b6a41-1a22-11d1-bad9-00609744111a"
)
KSDATAFORMAT_SUBTYPE_VPVBI = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_VPVBI
)


STATIC_KSDATAFORMAT_SPECIFIER_VIDEOINFO = (
    0x05589F80,
    0xC356,
    0x11CE,
    0xBF,
    0x01,
    0x00,
    0xAA,
    0x00,
    0x55,
    0x59,
    0x5A,
)
KSDATAFORMAT_SPECIFIER_VIDEOINFO = DEFINE_GUIDSTRUCT(
    "05589f80-c356-11ce-bf01-00aa0055595a"
)
KSDATAFORMAT_SPECIFIER_VIDEOINFO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_VIDEOINFO
)


STATIC_KSDATAFORMAT_SPECIFIER_VIDEOINFO2 = (
    0xF72A76A0,
    0xEB0A,
    0x11D0,
    0xAC,
    0xE4,
    0x00,
    0x00,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
KSDATAFORMAT_SPECIFIER_VIDEOINFO2 = DEFINE_GUIDSTRUCT(
    "f72a76A0-eb0a-11d0-ace4-0000c0cc16ba"
)
KSDATAFORMAT_SPECIFIER_VIDEOINFO2 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_VIDEOINFO2
)


STATIC_KSDATAFORMAT_SPECIFIER_H264_VIDEO = (
    0x2017BE05,
    0x6629,
    0x4248,
    0xAA,
    0xED,
    0x7E,
    0x1A,
    0x47,
    0xBC,
    0x9B,
    0x9C,
)
KSDATAFORMAT_SPECIFIER_H264_VIDEO = DEFINE_GUIDSTRUCT(
    "2017be05-6629-4248-aaed-7e1a47bc9b9c"
)
KSDATAFORMAT_SPECIFIER_H264_VIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_H264_VIDEO
)


STATIC_KSDATAFORMAT_SPECIFIER_JPEG_IMAGE = (
    0x692FA379,
    0xD3E8,
    0x4651,
    0xB5,
    0xB4,
    0xB,
    0x94,
    0xB0,
    0x13,
    0xEE,
    0xAF,
)
KSDATAFORMAT_SPECIFIER_JPEG_IMAGE = DEFINE_GUIDSTRUCT(
    "692fa379-d3e8-4651-b5b4-0b94b013eeaf"
)
KSDATAFORMAT_SPECIFIER_JPEG_IMAGE = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_JPEG_IMAGE
)


STATIC_KSDATAFORMAT_SPECIFIER_IMAGE = (
    0x692FA379,
    0xD3E8,
    0x4651,
    0xB5,
    0xB4,
    0xB,
    0x94,
    0xB0,
    0x13,
    0xEE,
    0xAF,
)
KSDATAFORMAT_SPECIFIER_IMAGE = DEFINE_GUIDSTRUCT(
    "692fa379-d3e8-4651-b5b4-0b94b013eeaf"
)
KSDATAFORMAT_SPECIFIER_IMAGE = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_IMAGE
)


STATIC_KSDATAFORMAT_TYPE_IMAGE = (
    0x72178C23,
    0xE45B,
    0x11D5,
    0xBC,
    0x2A,
    0x00,
    0xB0,
    0xD0,
    0xF3,
    0xF4,
    0xAB,
)
KSDATAFORMAT_TYPE_IMAGE = DEFINE_GUIDSTRUCT(
    "72178c23-e45b-11d5-bc2a-00b0d0f3f4ab"
)
KSDATAFORMAT_TYPE_IMAGE = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_IMAGE
)


STATIC_KSDATAFORMAT_SUBTYPE_JPEG = (
    0x19E4A5AA,
    0x5662,
    0x4FC5,
    0xA0,
    0xC0,
    0x17,
    0x58,
    0x2,
    0x8E,
    0x10,
    0x57,
)
KSDATAFORMAT_SUBTYPE_JPEG = DEFINE_GUIDSTRUCT(
    "19e4a5aa-5662-4fc5-a0c0-1758028e1057"
)
KSDATAFORMAT_SUBTYPE_JPEG = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_JPEG
)


STATIC_KSDATAFORMAT_SUBTYPE_IMAGE_RGB32 = (
    0x00000016,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_IMAGE_RGB32 = DEFINE_GUIDSTRUCT(
    "00000016-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_IMAGE_RGB32 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_IMAGE_RGB32
)


STATIC_KSDATAFORMAT_SUBTYPE_L8 = (
    0x00000032,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_L8 = DEFINE_GUIDSTRUCT(
    "00000032-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_L8 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_L8
)


STATIC_KSDATAFORMAT_SUBTYPE_L8_IR = (
    0x00000032,
    0x0002,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_L8_IR = DEFINE_GUIDSTRUCT(
    "00000032-0002-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_L8_IR = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_L8_IR
)


STATIC_KSDATAFORMAT_SUBTYPE_L8_CUSTOM = (
    0x00000032,
    0x8000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_L8_CUSTOM = DEFINE_GUIDSTRUCT(
    "00000032-8000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_L8_CUSTOM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_L8_CUSTOM
)


STATIC_KSDATAFORMAT_SUBTYPE_L16 = (
    0x00000051,
    0x0000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_L16 = DEFINE_GUIDSTRUCT(
    "00000051-0000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_L16 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_L16
)


STATIC_KSDATAFORMAT_SUBTYPE_L16_IR = (
    0x00000051,
    0x0002,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_L16_IR = DEFINE_GUIDSTRUCT(
    "00000051-0002-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_L16_IR = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_L16_IR
)


STATIC_KSDATAFORMAT_SUBTYPE_D16 = (
    0x00000050,
    0x0004,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_D16 = DEFINE_GUIDSTRUCT(
    "00000050-0004-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_D16 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_D16
)


STATIC_KSDATAFORMAT_SUBTYPE_L16_CUSTOM = (
    0x00000051,
    0x8000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_L16_CUSTOM = DEFINE_GUIDSTRUCT(
    "00000051-8000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_L16_CUSTOM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_L16_CUSTOM
)


STATIC_KSDATAFORMAT_SUBTYPE_MJPG_IR = (
    0x47504A4D,
    0x0002,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_MJPG_IR = DEFINE_GUIDSTRUCT(
    "47504a4d-0002-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_MJPG_IR = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MJPG_IR
)


STATIC_KSDATAFORMAT_SUBTYPE_MJPG_DEPTH = (
    0x47504A4D,
    0x0004,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_MJPG_DEPTH = DEFINE_GUIDSTRUCT(
    "47504a4d-0004-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_MJPG_DEPTH = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MJPG_DEPTH
)


STATIC_KSDATAFORMAT_SUBTYPE_MJPG_CUSTOM = (
    0x47504A4D,
    0x8000,
    0x0010,
    0x80,
    0x00,
    0x00,
    0xAA,
    0x00,
    0x38,
    0x9B,
    0x71,
)
KSDATAFORMAT_SUBTYPE_MJPG_CUSTOM = DEFINE_GUIDSTRUCT(
    "47504a4d-8000-0010-8000-00aa00389b71"
)
KSDATAFORMAT_SUBTYPE_MJPG_CUSTOM = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_MJPG_CUSTOM
)


STATIC_KSDATAFORMAT_TYPE_ANALOGVIDEO = (
    0x0482DDE1,
    0x7817,
    0x11CF,
    0x8A,
    0x03,
    0x00,
    0xAA,
    0x00,
    0x6E,
    0xCB,
    0x65,
)
KSDATAFORMAT_TYPE_ANALOGVIDEO = DEFINE_GUIDSTRUCT(
    "0482dde1-7817-11cf-8a03-00aa006ecb65"
)
KSDATAFORMAT_TYPE_ANALOGVIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_ANALOGVIDEO
)


STATIC_KSDATAFORMAT_SPECIFIER_ANALOGVIDEO = (
    0x0482DDE0,
    0x7817,
    0x11CF,
    0x8A,
    0x03,
    0x00,
    0xAA,
    0x00,
    0x6E,
    0xCB,
    0x65,
)
KSDATAFORMAT_SPECIFIER_ANALOGVIDEO = DEFINE_GUIDSTRUCT(
    "0482dde0-7817-11cf-8a03-00aa006ecb65"
)
KSDATAFORMAT_SPECIFIER_ANALOGVIDEO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_ANALOGVIDEO
)


STATIC_KSDATAFORMAT_TYPE_ANALOGAUDIO = (
    0x0482DEE1,
    0x7817,
    0x11CF,
    0x8A,
    0x03,
    0x00,
    0xAA,
    0x00,
    0x6E,
    0xCB,
    0x65,
)
KSDATAFORMAT_TYPE_ANALOGAUDIO = DEFINE_GUIDSTRUCT(
    "0482DEE1-7817-11cf-8a03-00aa006ecb65"
)
KSDATAFORMAT_TYPE_ANALOGAUDIO = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_ANALOGAUDIO
)


STATIC_KSDATAFORMAT_SPECIFIER_VBI = (
    0xF72A76E0,
    0xEB0A,
    0x11D0,
    0xAC,
    0xE4,
    0x00,
    0x00,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
KSDATAFORMAT_SPECIFIER_VBI = DEFINE_GUIDSTRUCT(
    "f72a76e0-eb0a-11d0-ace4-0000c0cc16ba"
)
KSDATAFORMAT_SPECIFIER_VBI = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SPECIFIER_VBI
)


STATIC_KSDATAFORMAT_TYPE_VBI = (
    0xF72A76E1,
    0xEB0A,
    0x11D0,
    0xAC,
    0xE4,
    0x00,
    0x00,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
KSDATAFORMAT_TYPE_VBI = DEFINE_GUIDSTRUCT(
    "f72a76e1-eb0a-11d0-ace4-0000c0cc16ba"
)
KSDATAFORMAT_TYPE_VBI = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_VBI
)


STATIC_KSDATAFORMAT_SUBTYPE_RAW8 = (
    0xCA20D9A0,
    0x3E3E,
    0x11D1,
    0x9B,
    0xF9,
    0x0,
    0xC0,
    0x4F,
    0xBB,
    0xDE,
    0xBF,
)
KSDATAFORMAT_SUBTYPE_RAW8 = DEFINE_GUIDSTRUCT(
    "ca20d9a0-3e3e-11d1-9bf9-00c04fbbdebf"
)
KSDATAFORMAT_SUBTYPE_RAW8 = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_RAW8
)


STATIC_KSDATAFORMAT_SUBTYPE_CC = (
    0x33214CC1,
    0x11F,
    0x11D2,
    0xB4,
    0xB1,
    0x0,
    0xA0,
    0xD1,
    0x2,
    0xCF,
    0xBE,
)
KSDATAFORMAT_SUBTYPE_CC = DEFINE_GUIDSTRUCT(
    "33214CC1-011F-11D2-B4B1-00A0D102CFBE"
)
KSDATAFORMAT_SUBTYPE_CC = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_CC
)


STATIC_KSDATAFORMAT_SUBTYPE_NABTS = (
    0xF72A76E2,
    0xEB0A,
    0x11D0,
    0xAC,
    0xE4,
    0x00,
    0x00,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
KSDATAFORMAT_SUBTYPE_NABTS = DEFINE_GUIDSTRUCT(
    "f72a76e2-eb0a-11d0-ace4-0000c0cc16ba"
)
KSDATAFORMAT_SUBTYPE_NABTS = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_NABTS
)


STATIC_KSDATAFORMAT_SUBTYPE_TELETEXT = (
    0xF72A76E3,
    0xEB0A,
    0x11D0,
    0xAC,
    0xE4,
    0x00,
    0x00,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
KSDATAFORMAT_SUBTYPE_TELETEXT = DEFINE_GUIDSTRUCT(
    "f72a76e3-eb0a-11d0-ace4-0000c0cc16ba"
)
KSDATAFORMAT_SUBTYPE_TELETEXT = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_TELETEXT
)


STATIC_KSDATAFORMAT_TYPE_NABTS = (
    0xE757BCA0,
    0x39AC,
    0x11D1,
    0xA9,
    0xF5,
    0x0,
    0xC0,
    0x4F,
    0xBB,
    0xDE,
    0x8F,
)
KSDATAFORMAT_TYPE_NABTS = DEFINE_GUIDSTRUCT(
    "E757BCA0-39AC-11d1-A9F5-00C04FBBDE8F"
)
KSDATAFORMAT_TYPE_NABTS = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_NABTS
)


STATIC_KSDATAFORMAT_SUBTYPE_NABTS_FEC = (
    0xE757BCA1,
    0x39AC,
    0x11D1,
    0xA9,
    0xF5,
    0x0,
    0xC0,
    0x4F,
    0xBB,
    0xDE,
    0x8F,
)
KSDATAFORMAT_SUBTYPE_NABTS_FEC = DEFINE_GUIDSTRUCT(
    "E757BCA1-39AC-11d1-A9F5-00C04FBBDE8F"
)
KSDATAFORMAT_SUBTYPE_NABTS_FEC = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_NABTS_FEC
)


STATIC_KSDATAFORMAT_SUBTYPE_OVERLAY = (
    0xE436EB7F,
    0x524F,
    0x11CE,
    0x9F,
    0x53,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70,
)
KSDATAFORMAT_SUBTYPE_OVERLAY = DEFINE_GUIDSTRUCT(
    "e436eb7f-524f-11ce-9f53-0020af0ba770"
)
KSDATAFORMAT_SUBTYPE_OVERLAY = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_OVERLAY
)


STATIC_KSDATAFORMAT_TYPE_AUXLine21Data = (
    0x670AEA80,
    0x3A82,
    0x11D0,
    0xB7,
    0x9B,
    0x00,
    0xAA,
    0x00,
    0x37,
    0x67,
    0xA7,
)
KSDATAFORMAT_TYPE_AUXLine21Data = DEFINE_GUIDSTRUCT(
    "670aea80-3a82-11d0-b79b-00aa003767a7"
)
KSDATAFORMAT_TYPE_AUXLine21Data = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_AUXLine21Data
)


STATIC_KSDATAFORMAT_SUBTYPE_Line21_BytePair = (
    0x6E8D4A22,
    0x310C,
    0x11D0,
    0xB7,
    0x9A,
    0x00,
    0xAA,
    0x00,
    0x37,
    0x67,
    0xA7,
)
KSDATAFORMAT_SUBTYPE_Line21_BytePair = DEFINE_GUIDSTRUCT(
    "6e8d4a22-310c-11d0-b79a-00aa003767a7"
)
KSDATAFORMAT_SUBTYPE_Line21_BytePair = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_Line21_BytePair
)


STATIC_KSDATAFORMAT_SUBTYPE_Line21_GOPPacket = (
    0x6E8D4A23,
    0x310C,
    0x11D0,
    0xB7,
    0x9A,
    0x00,
    0xAA,
    0x00,
    0x37,
    0x67,
    0xA7,
)
KSDATAFORMAT_SUBTYPE_Line21_GOPPacket = DEFINE_GUIDSTRUCT(
    "6e8d4a23-310c-11d0-b79a-00aa003767a7"
)
KSDATAFORMAT_SUBTYPE_Line21_GOPPacket = DEFINE_GUIDNAMED(
    KSDATAFORMAT_SUBTYPE_Line21_GOPPacket
)


STATIC_KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK = (
    0xED0B916A,
    0x044D,
    0x11D1,
    0xAA,
    0x78,
    0x00,
    0xC0,
    0x4F,
    0xC3,
    0x1D,
    0x60,
)
KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK = DEFINE_GUIDSTRUCT(
    "ed0b916a-044d-11d1-aa78-00c04fc31d60"
)
KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK = DEFINE_GUIDNAMED(
    KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK
)


# KSPROPSETID

STATIC_KSPROPSETID_DirectSound3DListener = (
    0x437B3414,
    0xD060,
    0x11D0,
    0x85,
    0x83,
    0x00,
    0xC0,
    0x4F,
    0xD9,
    0xBA,
    0xF3,
)
KSPROPSETID_DirectSound3DListener = DEFINE_GUIDSTRUCT(
    "437b3414-d060-11d0-8583-00c04fd9baf3"
)
KSPROPSETID_DirectSound3DListener = DEFINE_GUIDNAMED(
    KSPROPSETID_DirectSound3DListener
)


STATIC_KSPROPSETID_DirectSound3DBuffer = (
    0x437B3411,
    0xD060,
    0x11D0,
    0x85,
    0x83,
    0x00,
    0xC0,
    0x4F,
    0xD9,
    0xBA,
    0xF3,
)
KSPROPSETID_DirectSound3DBuffer = DEFINE_GUIDSTRUCT(
    "437b3411-d060-11d0-8583-00c04fd9baf3"
)
KSPROPSETID_DirectSound3DBuffer = DEFINE_GUIDNAMED(
    KSPROPSETID_DirectSound3DBuffer
)


STATIC_KSPROPSETID_Hrtf3d = (
    0xB66DECB0,
    0xA083,
    0x11D0,
    0x85,
    0x1E,
    0x00,
    0xC0,
    0x4F,
    0xD9,
    0xBA,
    0xF3,
)
KSPROPSETID_Hrtf3d = DEFINE_GUIDSTRUCT(
    "b66decb0-a083-11d0-851e-00c04fd9baf3"
)
KSPROPSETID_Hrtf3d = DEFINE_GUIDNAMED(
    KSPROPSETID_Hrtf3d
)


STATIC_KSPROPSETID_Itd3d = (
    0x6429F090,
    0x9FD9,
    0x11D0,
    0xA7,
    0x5B,
    0x00,
    0xA0,
    0xC9,
    0x03,
    0x65,
    0xE3,
)
KSPROPSETID_Itd3d = DEFINE_GUIDSTRUCT(
    "6429f090-9fd9-11d0-a75b-00a0c90365e3"
)
KSPROPSETID_Itd3d = DEFINE_GUIDNAMED(
    KSPROPSETID_Itd3d
)


STATIC_KSPROPSETID_Bibliographic = (
    0x07BA150E,
    0xE2B1,
    0x11D0,
    0xAC,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSPROPSETID_Bibliographic = DEFINE_GUIDSTRUCT(
    "07BA150E-E2B1-11D0-AC17-00A0C9223196"
)
KSPROPSETID_Bibliographic = DEFINE_GUIDNAMED(
    KSPROPSETID_Bibliographic
)



STATIC_KSPROPSETID_TopologyNode = (
    0x45FFAAA1,
    0x6E1B,
    0x11D0,
    0xBC,
    0xF2,
    0x44,
    0x45,
    0x53,
    0x54,
    0x00,
    0x00,
)
KSPROPSETID_TopologyNode = DEFINE_GUIDSTRUCT(
    "45FFAAA1-6E1B-11D0-BCF2-444553540000"
)
KSPROPSETID_TopologyNode = DEFINE_GUIDNAMED(
    KSPROPSETID_TopologyNode
)


STATIC_KSPROPSETID_RtAudio = (
    0xA855A48C,
    0x2F78,
    0x4729,
    0x90,
    0x51,
    0x19,
    0x68,
    0x74,
    0x6B,
    0x9E,
    0xEF,
)
KSPROPSETID_RtAudio = DEFINE_GUIDSTRUCT(
    "A855A48C-2F78-4729-9051-1968746B9EEF"
)
KSPROPSETID_RtAudio = DEFINE_GUIDNAMED(
    KSPROPSETID_RtAudio
)


STATIC_KSPROPSETID_BtAudio = (
    0x7FA06C40,
    0xB8F6,
    0x4C7E,
    0x85,
    0x56,
    0xE8,
    0xC3,
    0x3A,
    0x12,
    0xE5,
    0x4D,
)
KSPROPSETID_BtAudio = DEFINE_GUIDSTRUCT(
    "7FA06C40-B8F6-4C7E-8556-E8C33A12E54D"
)
KSPROPSETID_BtAudio = DEFINE_GUIDNAMED(
    KSPROPSETID_BtAudio
)


STATIC_KSPROPSETID_DrmAudioStream = (
    0x2F2C8DDD,
    0x4198,
    0x4FAC,
    0xBA,
    0x29,
    0x61,
    0xBB,
    0x5,
    0xB7,
    0xDE,
    0x6,
)
KSPROPSETID_DrmAudioStream = DEFINE_GUIDSTRUCT(
    "2F2C8DDD-4198-4fac-BA29-61BB05B7DE06"
)
KSPROPSETID_DrmAudioStream = DEFINE_GUIDNAMED(
    KSPROPSETID_DrmAudioStream
)


STATIC_KSPROPSETID_SoundDetector = (
    0x113C425E,
    0xFD17,
    0x4057,
    0xB4,
    0x22,
    0xED,
    0x40,
    0x74,
    0xF1,
    0xAF,
    0xDF,
)
KSPROPSETID_SoundDetector = DEFINE_GUIDSTRUCT(
    "113C425E-FD17-4057-B422-ED4074F1AFDF"
)
KSPROPSETID_SoundDetector = DEFINE_GUIDNAMED(
    KSPROPSETID_SoundDetector
)


STATIC_KSPROPSETID_Audio = (
    0x45FFAAA0,
    0x6E1B,
    0x11D0,
    0xBC,
    0xF2,
    0x44,
    0x45,
    0x53,
    0x54,
    0x00,
    0x00,
)
KSPROPSETID_Audio = DEFINE_GUIDSTRUCT(
    "45FFAAA0-6E1B-11D0-BCF2-444553540000"
)
KSPROPSETID_Audio = DEFINE_GUIDNAMED(
    KSPROPSETID_Audio
)


STATIC_KSPROPSETID_TelephonyControl = (
    0xB6DF7EB1,
    0xD099,
    0x489F,
    0xA6,
    0xA0,
    0xC0,
    0x10,
    0x6F,
    0x8,
    0x87,
    0xA7,
)
KSPROPSETID_TelephonyControl = DEFINE_GUIDSTRUCT(
    "B6DF7EB1-D099-489F-A6A0-C0106F0887A7"
)
KSPROPSETID_TelephonyControl = DEFINE_GUIDNAMED(
    KSPROPSETID_TelephonyControl
)


STATIC_KSPROPSETID_TelephonyTopology = (
    0xABF25C7E,
    0x0E64,
    0x4E32,
    0xB1,
    0x90,
    0xD0,
    0xF6,
    0xD7,
    0xC5,
    0x3E,
    0x97,
)
KSPROPSETID_TelephonyTopology = DEFINE_GUIDSTRUCT(
    "ABF25C7E-0E64-4E32-B190-D0F6D7C53E97"
)
KSPROPSETID_TelephonyTopology = DEFINE_GUIDNAMED(
    KSPROPSETID_TelephonyTopology
)


STATIC_KSPROPSETID_FMRXTopology = (
    0xC46CE8F,
    0xDC2D,
    0x4204,
    0x9D,
    0xC9,
    0xF5,
    0x89,
    0x63,
    0x36,
    0x65,
    0x63,
)
KSPROPSETID_FMRXTopology = DEFINE_GUIDSTRUCT(
    "0C46CE8F-DC2D-4204-9DC9-F58963366563"
)
KSPROPSETID_FMRXTopology = DEFINE_GUIDNAMED(
    KSPROPSETID_FMRXTopology
)


STATIC_KSPROPSETID_FMRXControl = (
    0x947BBA3A,
    0xE8EE,
    0x4786,
    0x90,
    0xC4,
    0x84,
    0x28,
    0x18,
    0x5F,
    0x05,
    0xBE,
)
KSPROPSETID_FMRXControl = DEFINE_GUIDSTRUCT(
    "947BBA3A-E8EE-4786-90C4-8428185F05BE"
)
KSPROPSETID_FMRXControl = DEFINE_GUIDNAMED(
    KSPROPSETID_FMRXControl
)


STATIC_KSPROPSETID_Acoustic_Echo_Cancel = (
    0xD7A4AF8B,
    0x3DC1,
    0x4902,
    0x91,
    0xEA,
    0x8A,
    0x15,
    0xC9,
    0x0E,
    0x05,
    0xB2,
)
KSPROPSETID_Acoustic_Echo_Cancel = DEFINE_GUIDSTRUCT(
    "D7A4AF8B-3DC1-4902-91EA-8A15C90E05B2"
)
KSPROPSETID_Acoustic_Echo_Cancel = DEFINE_GUIDNAMED(
    KSPROPSETID_Acoustic_Echo_Cancel
)


STATIC_KSPROPSETID_Wave_Queued = (
    0x16A15B10,
    0x16F0,
    0x11D0,
    0xA1,
    0x95,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSPROPSETID_Wave_Queued = DEFINE_GUIDSTRUCT(
    "16a15b10-16f0-11d0-a195-0020afd156e4"
)
KSPROPSETID_Wave_Queued = DEFINE_GUIDNAMED(
    KSPROPSETID_Wave_Queued
)


STATIC_KSPROPSETID_Wave = (
    0x924E54B0,
    0x630F,
    0x11CF,
    0xAD,
    0xA7,
    0x08,
    0x00,
    0x3E,
    0x30,
    0x49,
    0x4A,
)
KSPROPSETID_Wave = DEFINE_GUIDSTRUCT(
    "924e54b0-630f-11cf-ada7-08003e30494a"
)
KSPROPSETID_Wave = DEFINE_GUIDNAMED(
    KSPROPSETID_Wave
)


STATIC_KSPROPSETID_WaveTable = (
    0x8539E660,
    0x62E9,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_WaveTable = DEFINE_GUIDSTRUCT(
    "8539E660-62E9-11CF-A5D6-28DB04C10000"
)
KSPROPSETID_WaveTable = DEFINE_GUIDNAMED(
    KSPROPSETID_WaveTable
)


STATIC_KSPROPSETID_Cyclic = (
    0x3FFEAEA0,
    0x2BEE,
    0x11CF,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_Cyclic = DEFINE_GUIDSTRUCT(
    "3FFEAEA0-2BEE-11CF-A5D6-28DB04C10000"
)
KSPROPSETID_Cyclic = DEFINE_GUIDNAMED(
    KSPROPSETID_Cyclic
)


STATIC_KSPROPSETID_Sysaudio = (
    0xCBE3FAA0,
    0xCC75,
    0x11D0,
    0xB4,
    0x65,
    0x00,
    0x00,
    0x1A,
    0x18,
    0x18,
    0xE6,
)
KSPROPSETID_Sysaudio = DEFINE_GUIDSTRUCT(
    "CBE3FAA0-CC75-11D0-B465-00001A1818E6"
)
KSPROPSETID_Sysaudio = DEFINE_GUIDNAMED(
    KSPROPSETID_Sysaudio
)


STATIC_KSPROPSETID_Sysaudio_Pin = (
    0xA3A53220,
    0xC6E4,
    0x11D0,
    0xB4,
    0x65,
    0x00,
    0x00,
    0x1A,
    0x18,
    0x18,
    0xE6,
)
KSPROPSETID_Sysaudio_Pin = DEFINE_GUIDSTRUCT(
    "A3A53220-C6E4-11D0-B465-00001A1818E6"
)
KSPROPSETID_Sysaudio_Pin = DEFINE_GUIDNAMED(
    KSPROPSETID_Sysaudio_Pin
)


STATIC_KSPROPSETID_AudioGfx = (
    0x79A9312E,
    0x59AE,
    0x43B0,
    0xA3,
    0x50,
    0x8B,
    0x5,
    0x28,
    0x4C,
    0xAB,
    0x24,
)
KSPROPSETID_AudioGfx = DEFINE_GUIDSTRUCT(
    "79A9312E-59AE-43b0-A350-8B05284CAB24"
)
KSPROPSETID_AudioGfx = DEFINE_GUIDNAMED(
    KSPROPSETID_AudioGfx
)


STATIC_KSPROPSETID_Linear = (
    0x5A2FFE80,
    0x16B9,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSPROPSETID_Linear = DEFINE_GUIDSTRUCT(
    "5A2FFE80-16B9-11D0-A5D6-28DB04C10000"
)
KSPROPSETID_Linear = DEFINE_GUIDNAMED(
    KSPROPSETID_Linear
)


STATIC_KSPROPSETID_Mpeg2Vid = (
    0xC8E11B60,
    0x0CC9,
    0x11D0,
    0xBD,
    0x69,
    0x00,
    0x35,
    0x05,
    0xC1,
    0x03,
    0xA9,
)
KSPROPSETID_Mpeg2Vid = DEFINE_GUIDSTRUCT(
    "C8E11B60-0CC9-11D0-BD69-003505C103A9"
)
KSPROPSETID_Mpeg2Vid = DEFINE_GUIDNAMED(
    KSPROPSETID_Mpeg2Vid
)


STATIC_KSPROPSETID_AC3 = (
    0xBFABE720,
    0x6E1F,
    0x11D0,
    0xBC,
    0xF2,
    0x44,
    0x45,
    0x53,
    0x54,
    0x00,
    0x00,
)
KSPROPSETID_AC3 = DEFINE_GUIDSTRUCT(
    "BFABE720-6E1F-11D0-BCF2-444553540000"
)
KSPROPSETID_AC3 = DEFINE_GUIDNAMED(
    KSPROPSETID_AC3
)


STATIC_KSPROPSETID_AudioDecoderOut = (
    0x6CA6E020,
    0x43BD,
    0x11D0,
    0xBD,
    0x6A,
    0x00,
    0x35,
    0x05,
    0xC1,
    0x03,
    0xA9,
)
KSPROPSETID_AudioDecoderOut = DEFINE_GUIDSTRUCT(
    "6ca6e020-43bd-11d0-bd6a-003505c103a9"
)
KSPROPSETID_AudioDecoderOut = DEFINE_GUIDNAMED(
    KSPROPSETID_AudioDecoderOut
)


STATIC_KSPROPSETID_DvdSubPic = (
    0xAC390460,
    0x43AF,
    0x11D0,
    0xBD,
    0x6A,
    0x00,
    0x35,
    0x05,
    0xC1,
    0x03,
    0xA9,
)
KSPROPSETID_DvdSubPic = DEFINE_GUIDSTRUCT(
    "ac390460-43af-11d0-bd6a-003505c103a9"
)
KSPROPSETID_DvdSubPic = DEFINE_GUIDNAMED(
    KSPROPSETID_DvdSubPic
)


STATIC_KSPROPSETID_CopyProt = (
    0x0E8A0A40,
    0x6AEF,
    0x11D0,
    0x9E,
    0xD0,
    0x00,
    0xA0,
    0x24,
    0xCA,
    0x19,
    0xB3,
)
KSPROPSETID_CopyProt = DEFINE_GUIDSTRUCT(
    "0E8A0A40-6AEF-11D0-9ED0-00A024CA19B3"
)
KSPROPSETID_CopyProt = DEFINE_GUIDNAMED(
    KSPROPSETID_CopyProt
)


STATIC_KSPROPSETID_VBICAP_PROPERTIES = (
    0xF162C607,
    0x7B35,
    0x496F,
    0xAD,
    0x7F,
    0x2D,
    0xCA,
    0x3B,
    0x46,
    0xB7,
    0x18,
)
KSPROPSETID_VBICAP_PROPERTIES = DEFINE_GUIDSTRUCT(
    "F162C607-7B35-496f-AD7F-2DCA3B46B718"
)
KSPROPSETID_VBICAP_PROPERTIES = DEFINE_GUIDNAMED(
    KSPROPSETID_VBICAP_PROPERTIES
)


STATIC_KSPROPSETID_VBICodecFiltering = (
    0xCAFEB0CA,
    0x8715,
    0x11D0,
    0xBD,
    0x6A,
    0x00,
    0x35,
    0xC0,
    0xED,
    0xBA,
    0xBE,
)
KSPROPSETID_VBICodecFiltering = DEFINE_GUIDSTRUCT(
    "cafeb0ca-8715-11d0-bd6a-0035c0edbabe"
)
KSPROPSETID_VBICodecFiltering = DEFINE_GUIDNAMED(
    KSPROPSETID_VBICodecFiltering
)


STATIC_KSPROPSETID_VramCapture = (
    0xE73FACE3,
    0x2880,
    0x4902,
    0xB7,
    0x99,
    0x88,
    0xD0,
    0xCD,
    0x63,
    0x4E,
    0xF,
)
KSPROPSETID_VramCapture = DEFINE_GUIDSTRUCT(
    "E73FACE3-2880-4902-B799-88D0CD634E0F"
)
KSPROPSETID_VramCapture = DEFINE_GUIDNAMED(
    KSPROPSETID_VramCapture
)


STATIC_KSPROPSETID_MPEG4_MediaType_Attributes = (
    0xFF6C4BFA,
    0x7A9,
    0x4C7B,
    0xA2,
    0x37,
    0x67,
    0x2F,
    0x9D,
    0x68,
    0x6,
    0x5F,
)
KSPROPSETID_MPEG4_MediaType_Attributes = DEFINE_GUIDSTRUCT(
    "FF6C4BFA-07A9-4c7b-A237-672F9D68065F"
)
KSPROPSETID_MPEG4_MediaType_Attributes = DEFINE_GUIDNAMED(
    KSPROPSETID_MPEG4_MediaType_Attributes
)


STATIC_KSPROPSETID_OverlayUpdate = (
    0x490EA5CF,
    0x7681,
    0x11D1,
    0xA2,
    0x1C,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSPROPSETID_OverlayUpdate = DEFINE_GUIDSTRUCT(
    "490EA5CF-7681-11D1-A21C-00A0C9223196"
)
KSPROPSETID_OverlayUpdate = DEFINE_GUIDNAMED(
    KSPROPSETID_OverlayUpdate
)


STATIC_KSPROPSETID_VPConfig = (
    0xBC29A660,
    0x30E3,
    0x11D0,
    0x9E,
    0x69,
    0x00,
    0xC0,
    0x4F,
    0xD7,
    0xC1,
    0x5B,
)
KSPROPSETID_VPConfig = DEFINE_GUIDSTRUCT(
    "bc29a660-30e3-11d0-9e69-00c04fd7c15b"
)
KSPROPSETID_VPConfig = DEFINE_GUIDNAMED(
    KSPROPSETID_VPConfig
)


STATIC_KSPROPSETID_VPVBIConfig = (
    0xEC529B00,
    0x1A1F,
    0x11D1,
    0xBA,
    0xD9,
    0x0,
    0x60,
    0x97,
    0x44,
    0x11,
    0x1A,
)
KSPROPSETID_VPVBIConfig = DEFINE_GUIDSTRUCT(
    "ec529b00-1a1f-11d1-bad9-00609744111a"
)
KSPROPSETID_VPVBIConfig = DEFINE_GUIDNAMED(
    KSPROPSETID_VPVBIConfig
)


STATIC_KSPROPSETID_TSRateChange = (
    0xA503C5C0,
    0x1D1D,
    0x11D1,
    0xAD,
    0x80,
    0x44,
    0x45,
    0x53,
    0x54,
    0x0,
    0x0,
)
KSPROPSETID_TSRateChange = DEFINE_GUIDSTRUCT(
    "A503C5C0-1D1D-11D1-AD80-444553540000"
)
KSPROPSETID_TSRateChange = DEFINE_GUIDNAMED(
    KSPROPSETID_TSRateChange
)


STATIC_KSPROPSETID_Jack = (
    0x4509F757,
    0x2D46,
    0x4637,
    0x8E,
    0x62,
    0xCE,
    0x7D,
    0xB9,
    0x44,
    0xF5,
    0x7B,
)
KSPROPSETID_Jack = DEFINE_GUIDSTRUCT(
    "4509F757-2D46-4637-8E62-CE7DB944F57B"
)
KSPROPSETID_Jack = DEFINE_GUIDNAMED(
    KSPROPSETID_Jack
)


STATIC_KSPROPSETID_AudioBufferDuration = (
    0x4E73C07F,
    0x23CC,
    0x4955,
    0xA7,
    0xEA,
    0x3D,
    0xA5,
    0x2,
    0x49,
    0x62,
    0x90,
)
KSPROPSETID_AudioBufferDuration = DEFINE_GUIDSTRUCT(
    "4E73C07F-23CC-4955-A7EA-3DA502496290"
)
KSPROPSETID_AudioBufferDuration = DEFINE_GUIDNAMED(
    KSPROPSETID_AudioBufferDuration
)


STATIC_KSPROPSETID_AudioEngine = (
    0x3A2F82DC,
    0x886F,
    0x4BAA,
    0x9E,
    0xB4,
    0x8,
    0x2B,
    0x90,
    0x25,
    0xC5,
    0x36,
)
KSPROPSETID_AudioEngine = DEFINE_GUIDSTRUCT(
    "3A2F82DC-886F-4BAA-9EB4-082B9025C536"
)
KSPROPSETID_AudioEngine = DEFINE_GUIDNAMED(
    KSPROPSETID_AudioEngine
)


STATIC_KSPROPSETID_AudioSignalProcessing = (
    0x4F67B528,
    0x30C9,
    0x40DE,
    0xB2,
    0xFB,
    0x85,
    0x9D,
    0xDD,
    0x1F,
    0x34,
    0x70,
)
KSPROPSETID_AudioSignalProcessing = DEFINE_GUIDSTRUCT(
    "4F67B528-30C9-40DE-B2FB-859DDD1F3470"
)
KSPROPSETID_AudioSignalProcessing = DEFINE_GUIDNAMED(
    KSPROPSETID_AudioSignalProcessing
)


STATIC_KSPROPSETID_AudioModule = (
    0xC034FDB0,
    0xFF75,
    0x47C8,
    0xAA,
    0x3C,
    0xEE,
    0x46,
    0x71,
    0x6B,
    0x50,
    0xC6,
)
KSPROPSETID_AudioModule = DEFINE_GUIDSTRUCT(
    "C034FDB0-FF75-47C8-AA3C-EE46716B50C6"
)
KSPROPSETID_AudioModule = DEFINE_GUIDNAMED(
    KSPROPSETID_AudioModule
)


# KSMEDIUMSETID

STATIC_KSMEDIUMSETID_MidiBus = (
    0x05908040,
    0x3246,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSMEDIUMSETID_MidiBus = DEFINE_GUIDSTRUCT(
    "05908040-3246-11D0-A5D6-28DB04C10000"
)
KSMEDIUMSETID_MidiBus = DEFINE_GUIDNAMED(
    KSMEDIUMSETID_MidiBus
)


STATIC_KSMEDIUMSETID_VPBus = (
    0xA18C15EC,
    0xCE43,
    0x11D0,
    0xAB,
    0xE7,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSMEDIUMSETID_VPBus = DEFINE_GUIDSTRUCT(
    "A18C15EC-CE43-11D0-ABE7-00A0C9223196"
)
KSMEDIUMSETID_VPBus = DEFINE_GUIDNAMED(
    KSMEDIUMSETID_VPBus
)


# EVENTSETID

STATIC_EVENTSETID_TUNER = (
    0x6A2E0606,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
EVENTSETID_TUNER = DEFINE_GUIDSTRUCT(
    "6a2e0606-28e4-11d0-a18c-00a0c9118956"
)
EVENTSETID_TUNER = DEFINE_GUIDNAMED(
    EVENTSETID_TUNER
)


STATIC_EVENTSETID_VIDEODECODER = (
    0x6A2E0621,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
EVENTSETID_VIDEODECODER = DEFINE_GUIDSTRUCT(
    "6a2e0621-28e4-11d0-a18c-00a0c9118956"
)
EVENTSETID_VIDEODECODER = DEFINE_GUIDNAMED(
    EVENTSETID_VIDEODECODER
)


STATIC_EVENTSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST = (
    0x2FDFFC5D,
    0xC732,
    0x4BA6,
    0xB5,
    0xDF,
    0x6B,
    0x4D,
    0x7F,
    0xC8,
    0x8B,
    0x8B,
)
EVENTSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST = DEFINE_GUIDSTRUCT(
    "2FDFFC5D-C732-4BA6-B5DF-6B4D7FC88B8B"
)
EVENTSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST = DEFINE_GUIDNAMED(
    EVENTSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST
)


STATIC_EVENTSETID_CROSSBAR = (
    0x6A2E0641,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
EVENTSETID_CROSSBAR = DEFINE_GUIDSTRUCT(
    "6a2e0641-28e4-11d0-a18c-00a0c9118956"
)
EVENTSETID_CROSSBAR = DEFINE_GUIDNAMED(
    EVENTSETID_CROSSBAR
)


# KSEVENTSETID

STATIC_KSEVENTSETID_SoundDetector = (
    0x69785C9B,
    0xFC2D,
    0x49D6,
    0xAC,
    0x32,
    0x47,
    0x99,
    0xF8,
    0x7D,
    0xE9,
    0xF6,
)
KSEVENTSETID_SoundDetector = DEFINE_GUIDSTRUCT(
    "69785C9B-FC2D-49D6-AC32-4799F87DE9F6"
)
KSEVENTSETID_SoundDetector = DEFINE_GUIDNAMED(
    KSEVENTSETID_SoundDetector
)


STATIC_KSEVENTSETID_Telephony = (
    0xB77F12B4,
    0xCEB4,
    0x4484,
    0x8D,
    0x5E,
    0x52,
    0xC1,
    0xE7,
    0xD8,
    0x76,
    0x2D,
)
KSEVENTSETID_Telephony = DEFINE_GUIDSTRUCT(
    "B77F12B4-CEB4-4484-8D5E-52C1E7D8762D"
)
KSEVENTSETID_Telephony = DEFINE_GUIDNAMED(
    KSEVENTSETID_Telephony
)


STATIC_KSEVENTSETID_Cyclic = (
    0x142C1AC0,
    0x072A,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSEVENTSETID_Cyclic = DEFINE_GUIDSTRUCT(
    "142C1AC0-072A-11D0-A5D6-28DB04C10000"
)
KSEVENTSETID_Cyclic = DEFINE_GUIDNAMED(
    KSEVENTSETID_Cyclic
)


STATIC_KSEVENTSETID_AudioControlChange = (
    0xE85E9698,
    0xFA2F,
    0x11D1,
    0x95,
    0xBD,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSEVENTSETID_AudioControlChange = DEFINE_GUIDSTRUCT(
    "E85E9698-FA2F-11D1-95BD-00C04FB925D3"
)
KSEVENTSETID_AudioControlChange = DEFINE_GUIDNAMED(
    KSEVENTSETID_AudioControlChange
)


STATIC_KSEVENTSETID_LoopedStreaming = (
    0x4682B940,
    0xC6EF,
    0x11D0,
    0x96,
    0xD8,
    0x00,
    0xAA,
    0x00,
    0x51,
    0xE5,
    0x1D,
)
KSEVENTSETID_LoopedStreaming = DEFINE_GUIDSTRUCT(
    "4682B940-C6EF-11D0-96D8-00AA0051E51D"
)
KSEVENTSETID_LoopedStreaming = DEFINE_GUIDNAMED(
    KSEVENTSETID_LoopedStreaming
)


STATIC_KSEVENTSETID_Sysaudio = (
    0x04800320,
    0x4491,
    0x11D1,
    0xA0,
    0x50,
    0x40,
    0x57,
    0x05,
    0xC1,
    0x00,
    0x00,
)
KSEVENTSETID_Sysaudio = DEFINE_GUIDSTRUCT(
    "04800320-4491-11D1-A050-405705C10000"
)
KSEVENTSETID_Sysaudio = DEFINE_GUIDNAMED(
    KSEVENTSETID_Sysaudio
)


STATIC_KSEVENTSETID_DynamicFormatChange = (
    0x162AC456,
    0x83D7,
    0x4239,
    0x96,
    0xDF,
    0xC7,
    0x5F,
    0xFA,
    0x13,
    0x8B,
    0xC6,
)
KSEVENTSETID_DynamicFormatChange = DEFINE_GUIDSTRUCT(
    "162AC456-83D7-4239-96DF-C75FFA138BC6"
)
KSEVENTSETID_DynamicFormatChange = DEFINE_GUIDNAMED(
    KSEVENTSETID_DynamicFormatChange
)


STATIC_KSEVENTSETID_CameraAsyncControl = (
    0x22A11754,
    0x9701,
    0x4088,
    0xB3,
    0x3F,
    0x6B,
    0x9C,
    0xBC,
    0x52,
    0xDF,
    0x5E,
)
KSEVENTSETID_CameraAsyncControl = DEFINE_GUIDSTRUCT(
    "22A11754-9701-4088-B33F-6B9CBC52DF5E"
)
KSEVENTSETID_CameraAsyncControl = DEFINE_GUIDNAMED(
    KSEVENTSETID_CameraAsyncControl
)


STATIC_KSEVENTSETID_ExtendedCameraControl = (
    0x571C92C9,
    0x13A2,
    0x47E3,
    0xA6,
    0x49,
    0xD2,
    0xA7,
    0x78,
    0x16,
    0x63,
    0x84,
)
KSEVENTSETID_ExtendedCameraControl = DEFINE_GUIDSTRUCT(
    "571C92C9-13A2-47E3-A649-D2A778166384"
)
KSEVENTSETID_ExtendedCameraControl = DEFINE_GUIDNAMED(
    KSEVENTSETID_ExtendedCameraControl
)


STATIC_KSEVENTSETID_CameraEvent = (
    0x7899B2E0,
    0x6B43,
    0x4964,
    0x9D,
    0x2A,
    0xA2,
    0x1F,
    0x40,
    0x61,
    0xF5,
    0x76,
)
KSEVENTSETID_CameraEvent = DEFINE_GUIDSTRUCT(
    "7899B2E0-6B43-4964-9D2A-A21F4061F576"
)
KSEVENTSETID_CameraEvent = DEFINE_GUIDNAMED(
    KSEVENTSETID_CameraEvent
)


STATIC_KSEVENTSETID_EXTDEV_Command = (
    0x109C7988,
    0xB3CB,
    0x11D2,
    0xB4,
    0x8E,
    0x00,
    0x60,
    0x97,
    0xB3,
    0x39,
    0x1B,
)
KSEVENTSETID_EXTDEV_Command = DEFINE_GUIDSTRUCT(
    "109c7988-b3cb-11d2-b48e-006097b3391b"
)
KSEVENTSETID_EXTDEV_Command = DEFINE_GUIDNAMED(
    KSEVENTSETID_EXTDEV_Command
)


STATIC_KSEVENTSETID_VIDCAP_TVAUDIO = (
    0x6A2E0651,
    0x28E4,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0x89,
    0x56,
)
KSEVENTSETID_VIDCAP_TVAUDIO = DEFINE_GUIDSTRUCT(
    "6a2e0651-28e4-11d0-a18c-00a0c9118956"
)
KSEVENTSETID_VIDCAP_TVAUDIO = DEFINE_GUIDNAMED(
    KSEVENTSETID_VIDCAP_TVAUDIO
)


STATIC_KSEVENTSETID_VPNotify = (
    0x20C5598E,
    0xD3C8,
    0x11D0,
    0x8D,
    0xFC,
    0x00,
    0xC0,
    0x4F,
    0xD7,
    0xC0,
    0x8B,
)
KSEVENTSETID_VPNotify = DEFINE_GUIDSTRUCT(
    "20c5598e-d3c8-11d0-8dfc-00c04fd7c08b"
)
KSEVENTSETID_VPNotify = DEFINE_GUIDNAMED(
    KSEVENTSETID_VPNotify
)


STATIC_KSEVENTSETID_VIDCAPTOSTI = (
    0xDB47DE20,
    0xF628,
    0x11D1,
    0xBA,
    0x41,
    0x0,
    0xA0,
    0xC9,
    0xD,
    0x2B,
    0x5,
)

KSEVENTSETID_VIDCAPTOSTI = DEFINE_GUIDSTRUCT(
    "DB47DE20-F628-11d1-BA41-00A0C90D2B05"
)
KSEVENTSETID_VIDCAPNotify = DEFINE_GUIDNAMED(
    KSEVENTSETID_VIDCAPTOSTI
)
KSEVENTSETID_VIDCAPTOSTI = DEFINE_GUIDNAMED(
    KSEVENTSETID_VIDCAPTOSTI
)


STATIC_KSEVENTSETID_VPVBINotify = (
    0xEC529B01,
    0x1A1F,
    0x11D1,
    0xBA,
    0xD9,
    0x0,
    0x60,
    0x97,
    0x44,
    0x11,
    0x1A,
)
KSEVENTSETID_VPVBINotify = DEFINE_GUIDSTRUCT(
    "ec529b01-1a1f-11d1-bad9-00609744111a"
)
KSEVENTSETID_VPVBINotify = DEFINE_GUIDNAMED(
    KSEVENTSETID_VPVBINotify
)


# KSINTERFACESETID

STATIC_KSINTERFACESETID_Media = (
    0x3A13EB40,
    0x30A7,
    0x11D0,
    0xA5,
    0xD6,
    0x28,
    0xDB,
    0x04,
    0xC1,
    0x00,
    0x00,
)
KSINTERFACESETID_Media = DEFINE_GUIDSTRUCT(
    "3A13EB40-30A7-11D0-A5D6-28DB04C10000"
)
KSINTERFACESETID_Media = DEFINE_GUIDNAMED(
    KSINTERFACESETID_Media
)


# KSCOMPONENTID

STATIC_KSCOMPONENTID_USBAUDIO = (
    0x8F1275F0,
    0x26E9,
    0x4264,
    0xBA,
    0x4D,
    0x39,
    0xFF,
    0xF0,
    0x1D,
    0x94,
    0xAA,
)
KSCOMPONENTID_USBAUDIO = DEFINE_GUIDSTRUCT(
    "8F1275F0-26E9-4264-BA4D-39FFF01D94AA"
)
KSCOMPONENTID_USBAUDIO = DEFINE_GUIDNAMED(
    KSCOMPONENTID_USBAUDIO
)


# CODECAPI

STATIC_CODECAPI_CHANGELISTS = (
    0x62B12ACF,
    0xF6B0,
    0x47D9,
    0x94,
    0x56,
    0x96,
    0xF2,
    0x2C,
    0x4E,
    0x0B,
    0x9D,
)
CODECAPI_CHANGELISTS = DEFINE_GUIDSTRUCT(
    "62B12ACF-F6B0-47D9-9456-96F22C4E0B9D"
)
CODECAPI_CHANGELISTS = DEFINE_GUIDNAMED(
    CODECAPI_CHANGELISTS
)


STATIC_CODECAPI_VIDEO_ENCODER = (
    0x7112E8E1,
    0x3D03,
    0x47EF,
    0x8E,
    0x60,
    0x03,
    0xF1,
    0xCF,
    0x53,
    0x73,
    0x01,
)
CODECAPI_VIDEO_ENCODER = DEFINE_GUIDSTRUCT(
    "7112E8E1-3D03-47EF-8E60-03F1CF537301"
)
CODECAPI_VIDEO_ENCODER = DEFINE_GUIDNAMED(
    CODECAPI_VIDEO_ENCODER
)


STATIC_CODECAPI_AUDIO_ENCODER = (
    0xB9D19A3E,
    0xF897,
    0x429C,
    0xBC,
    0x46,
    0x81,
    0x38,
    0xB7,
    0x27,
    0x2B,
    0x2D,
)
CODECAPI_AUDIO_ENCODER = DEFINE_GUIDSTRUCT(
    "B9D19A3E-F897-429C-BC46-8138B7272B2D"
)
CODECAPI_AUDIO_ENCODER = DEFINE_GUIDNAMED(
    CODECAPI_AUDIO_ENCODER
)


STATIC_CODECAPI_SETALLDEFAULTS = (
    0x6C5E6A7C,
    0xACF8,
    0x4F55,
    0xA9,
    0x99,
    0x1A,
    0x62,
    0x81,
    0x09,
    0x05,
    0x1B,
)
CODECAPI_SETALLDEFAULTS = DEFINE_GUIDSTRUCT(
    "6C5E6A7C-ACF8-4F55-A999-1A628109051B"
)
CODECAPI_SETALLDEFAULTS = DEFINE_GUIDNAMED(
    CODECAPI_SETALLDEFAULTS
)


STATIC_CODECAPI_ALLSETTINGS = (
    0x6A577E92,
    0x83E1,
    0x4113,
    0xAD,
    0xC2,
    0x4F,
    0xCE,
    0xC3,
    0x2F,
    0x83,
    0xA1,
)
CODECAPI_ALLSETTINGS = DEFINE_GUIDSTRUCT(
    "6A577E92-83E1-4113-ADC2-4FCEC32F83A1"
)
CODECAPI_ALLSETTINGS = DEFINE_GUIDNAMED(
    CODECAPI_ALLSETTINGS
)


STATIC_CODECAPI_SUPPORTSEVENTS = (
    0x0581AF97,
    0x7693,
    0x4DBD,
    0x9D,
    0xCA,
    0x3F,
    0x9E,
    0xBD,
    0x65,
    0x85,
    0xA1,
)
CODECAPI_SUPPORTSEVENTS = DEFINE_GUIDSTRUCT(
    "0581AF97-7693-4DBD-9DCA-3F9EBD6585A1"
)
CODECAPI_SUPPORTSEVENTS = DEFINE_GUIDNAMED(
    CODECAPI_SUPPORTSEVENTS
)


STATIC_CODECAPI_CURRENTCHANGELIST = (
    0x1CB14E83,
    0x7D72,
    0x4657,
    0x83,
    0xFD,
    0x47,
    0xA2,
    0xC5,
    0xB9,
    0xD1,
    0x3D,
)
CODECAPI_CURRENTCHANGELIST = DEFINE_GUIDSTRUCT(
    "1CB14E83-7D72-4657-83FD-47A2C5B9D13D"
)
CODECAPI_CURRENTCHANGELIST = DEFINE_GUIDNAMED(
    CODECAPI_CURRENTCHANGELIST
)


# KSNOTIFICATIONID

STATIC_KSNOTIFICATIONID_AudioModule = (
    0x9C2220F0,
    0xD9A6,
    0x4D5C,
    0xA0,
    0x36,
    0x57,
    0x38,
    0x57,
    0xFD,
    0x50,
    0xD2,
)
KSNOTIFICATIONID_AudioModule = DEFINE_GUIDSTRUCT(
    "9C2220F0-D9A6-4D5C-A036-573857FD50D2"
)
KSNOTIFICATIONID_AudioModule = DEFINE_GUIDNAMED(
    KSNOTIFICATIONID_AudioModule
)


# KSCAMERAPROFILE

STATIC_KSCAMERAPROFILE_Legacy = (
    0xB4894D81,
    0x62B7,
    0x4EEC,
    0x87,
    0x40,
    0x80,
    0x65,
    0x8C,
    0x4A,
    0x9D,
    0x3E,
)
KSCAMERAPROFILE_Legacy = DEFINE_GUIDSTRUCT(
    "B4894D81-62B7-4EEC-8740-80658C4A9D3E"
)
KSCAMERAPROFILE_Legacy = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_Legacy
)


STATIC_KSCAMERAPROFILE_VideoRecording = (
    0xA0E517E8,
    0x8F8C,
    0x4F6F,
    0x9A,
    0x57,
    0x46,
    0xFC,
    0x2F,
    0x64,
    0x7E,
    0xC0,
)
KSCAMERAPROFILE_VideoRecording = DEFINE_GUIDSTRUCT(
    "A0E517E8-8F8C-4F6F-9A57-46FC2F647EC0"
)
KSCAMERAPROFILE_VideoRecording = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_VideoRecording
)


STATIC_KSCAMERAPROFILE_HighQualityPhoto = (
    0x32440725,
    0x961B,
    0x4CA3,
    0xB5,
    0xB2,
    0x85,
    0x4E,
    0x71,
    0x9D,
    0x9E,
    0x1B,
)
KSCAMERAPROFILE_HighQualityPhoto = DEFINE_GUIDSTRUCT(
    "32440725-961B-4CA3-B5B2-854E719D9E1B"
)
KSCAMERAPROFILE_HighQualityPhoto = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_HighQualityPhoto
)


STATIC_KSCAMERAPROFILE_BalancedVideoAndPhoto = (
    0x6B52B017,
    0x42C7,
    0x4A21,
    0xBF,
    0xE3,
    0x23,
    0xF0,
    0x09,
    0x14,
    0x98,
    0x87,
)
KSCAMERAPROFILE_BalancedVideoAndPhoto = DEFINE_GUIDSTRUCT(
    "6B52B017-42C7-4A21-BFE3-23F009149887"
)
KSCAMERAPROFILE_BalancedVideoAndPhoto = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_BalancedVideoAndPhoto
)


STATIC_KSCAMERAPROFILE_VideoConferencing = (
    0xC5444A88,
    0xE1BF,
    0x4597,
    0xB2,
    0xDD,
    0x9E,
    0x1E,
    0xAD,
    0x86,
    0x4B,
    0xB8,
)
KSCAMERAPROFILE_VideoConferencing = DEFINE_GUIDSTRUCT(
    "C5444A88-E1BF-4597-B2DD-9E1EAD864BB8"
)
KSCAMERAPROFILE_VideoConferencing = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_VideoConferencing
)


STATIC_KSCAMERAPROFILE_PhotoSequence = (
    0x02399D9D,
    0x4EE8,
    0x49BA,
    0xBC,
    0x07,
    0x5F,
    0xF1,
    0x56,
    0x53,
    0x14,
    0x13,
)
KSCAMERAPROFILE_PhotoSequence = DEFINE_GUIDSTRUCT(
    "02399D9D-4EE8-49BA-BC07-5FF156531413"
)
KSCAMERAPROFILE_PhotoSequence = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_PhotoSequence
)


STATIC_KSCAMERAPROFILE_FaceAuth_Mode = (
    0x81361B22,
    0x700B,
    0x4546,
    0xA2,
    0xD4,
    0xC5,
    0x2E,
    0x90,
    0x7B,
    0xFC,
    0x27,
)
KSCAMERAPROFILE_FaceAuth_Mode = DEFINE_GUIDSTRUCT(
    "81361B22-700B-4546-A2D4-C52E907BFC27"
)
KSCAMERAPROFILE_FaceAuth_Mode = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_FaceAuth_Mode
)


STATIC_KSCAMERAPROFILE_HighFrameRate = (
    0x566E6113,
    0x8C35,
    0x48E7,
    0xB8,
    0x9F,
    0xD2,
    0x3F,
    0xDC,
    0x12,
    0x19,
    0xDC,
)
KSCAMERAPROFILE_HighFrameRate = DEFINE_GUIDSTRUCT(
    "566E6113-8C35-48E7-B89F-D23FDC1219DC"
)
KSCAMERAPROFILE_HighFrameRate = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_HighFrameRate
)


STATIC_KSCAMERAPROFILE_HDRWithWCGVideo = (
    0x4B27C336,
    0x4924,
    0x4989,
    0xB9,
    0x94,
    0xFD,
    0xAF,
    0x1D,
    0xC7,
    0xCD,
    0x85,
)
KSCAMERAPROFILE_HDRWithWCGVideo = DEFINE_GUIDSTRUCT(
    "4B27C336-4924-4989-B994-FDAF1DC7CD85"
)
KSCAMERAPROFILE_HDRWithWCGVideo = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_HDRWithWCGVideo
)


STATIC_KSCAMERAPROFILE_HDRWithWCGPhoto = (
    0x9BF6F1FF,
    0xB555,
    0x4625,
    0xB3,
    0x26,
    0xA4,
    0x6D,
    0xEF,
    0x31,
    0x8F,
    0xB7,
)
KSCAMERAPROFILE_HDRWithWCGPhoto = DEFINE_GUIDSTRUCT(
    "9BF6F1FF-B555-4625-B326-A46DEF318FB7"
)
KSCAMERAPROFILE_HDRWithWCGPhoto = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_HDRWithWCGPhoto
)


STATIC_KSCAMERAPROFILE_VariablePhotoSequence = (
    0x9FF2CB56,
    0xE75A,
    0x49B1,
    0xA9,
    0x28,
    0x99,
    0x85,
    0xD5,
    0x94,
    0x6F,
    0x87,
)
KSCAMERAPROFILE_VariablePhotoSequence = DEFINE_GUIDSTRUCT(
    "9FF2CB56-E75A-49B1-A928-9985D5946F87"
)
KSCAMERAPROFILE_VariablePhotoSequence = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_VariablePhotoSequence
)


STATIC_KSCAMERAPROFILE_VideoHDR8 = (
    0xD4F3F4EC,
    0xBDFF,
    0x4314,
    0xB1,
    0xD4,
    0x00,
    0x8E,
    0x28,
    0x1F,
    0x74,
    0xE7,
)
KSCAMERAPROFILE_VideoHDR8 = DEFINE_GUIDSTRUCT(
    "D4F3F4EC-BDFF-4314-B1D4-008E281F74E7"
)
KSCAMERAPROFILE_VideoHDR8 = DEFINE_GUIDNAMED(
    KSCAMERAPROFILE_VideoHDR8
)


# KSAUDFNAME

STATIC_KSAUDFNAME_BASS = (
    0x185FEDE0,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_BASS = DEFINE_GUIDSTRUCT(
    "185FEDE0-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_BASS = DEFINE_GUIDNAMED(
    KSAUDFNAME_BASS
)


STATIC_KSAUDFNAME_TREBLE = (
    0x185FEDE1,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_TREBLE = DEFINE_GUIDSTRUCT(
    "185FEDE1-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_TREBLE = DEFINE_GUIDNAMED(
    KSAUDFNAME_TREBLE
)


STATIC_KSAUDFNAME_MIDRANGE = (
    0xA2CBE478,
    0xAE84,
    0x49A1,
    0x8B,
    0x72,
    0x4A,
    0xD0,
    0x9B,
    0x78,
    0xED,
    0x34,
)
KSAUDFNAME_MIDRANGE = DEFINE_GUIDSTRUCT(
    "A2CBE478-AE84-49A1-8B72-4AD09B78ED34"
)
KSAUDFNAME_MIDRANGE = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIDRANGE
)


STATIC_KSAUDFNAME_3D_STEREO = (
    0x185FEDE2,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_3D_STEREO = DEFINE_GUIDSTRUCT(
    "185FEDE2-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_3D_STEREO = DEFINE_GUIDNAMED(
    KSAUDFNAME_3D_STEREO
)


STATIC_KSAUDFNAME_MASTER_VOLUME = (
    0x185FEDE3,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MASTER_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDE3-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MASTER_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_MASTER_VOLUME
)


STATIC_KSAUDFNAME_MASTER_MUTE = (
    0x185FEDE4,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MASTER_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDE4-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MASTER_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_MASTER_MUTE
)


STATIC_KSAUDFNAME_WAVE_VOLUME = (
    0x185FEDE5,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_WAVE_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDE5-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_WAVE_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_WAVE_VOLUME
)


STATIC_KSAUDFNAME_WAVE_MUTE = (
    0x185FEDE6,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_WAVE_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDE6-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_WAVE_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_WAVE_MUTE
)


STATIC_KSAUDFNAME_MIDI_VOLUME = (
    0x185FEDE7,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MIDI_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDE7-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MIDI_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIDI_VOLUME
)


STATIC_KSAUDFNAME_MIDI_MUTE = (
    0x185FEDE8,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MIDI_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDE8-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MIDI_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIDI_MUTE
)


STATIC_KSAUDFNAME_CD_VOLUME = (
    0x185FEDE9,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_CD_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDE9-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_CD_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_CD_VOLUME
)


STATIC_KSAUDFNAME_CD_MUTE = (
    0x185FEDEA,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_CD_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDEA-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_CD_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_CD_MUTE
)


STATIC_KSAUDFNAME_LINE_VOLUME = (
    0x185FEDEB,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_LINE_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDEB-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_LINE_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_LINE_VOLUME
)


STATIC_KSAUDFNAME_LINE_MUTE = (
    0x185FEDEC,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_LINE_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDEC-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_LINE_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_LINE_MUTE
)


STATIC_KSAUDFNAME_MIC_VOLUME = (
    0x185FEDED,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MIC_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDED-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MIC_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIC_VOLUME
)


STATIC_KSAUDFNAME_MIC_MUTE = (
    0x185FEDEE,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MIC_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDEE-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MIC_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIC_MUTE
)


STATIC_KSAUDFNAME_RECORDING_SOURCE = (
    0x185FEDEF,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_RECORDING_SOURCE = DEFINE_GUIDSTRUCT(
    "185FEDEF-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_RECORDING_SOURCE = DEFINE_GUIDNAMED(
    KSAUDFNAME_RECORDING_SOURCE
)


STATIC_KSAUDFNAME_PC_SPEAKER_VOLUME = (
    0x185FEDF0,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_PC_SPEAKER_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDF0-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_PC_SPEAKER_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_PC_SPEAKER_VOLUME
)


STATIC_KSAUDFNAME_PC_SPEAKER_MUTE = (
    0x185FEDF1,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_PC_SPEAKER_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDF1-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_PC_SPEAKER_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_PC_SPEAKER_MUTE
)


STATIC_KSAUDFNAME_MIDI_IN_VOLUME = (
    0x185FEDF2,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MIDI_IN_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDF2-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MIDI_IN_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIDI_IN_VOLUME
)


STATIC_KSAUDFNAME_CD_IN_VOLUME = (
    0x185FEDF3,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_CD_IN_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDF3-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_CD_IN_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_CD_IN_VOLUME
)


STATIC_KSAUDFNAME_LINE_IN_VOLUME = (
    0x185FEDF4,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_LINE_IN_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDF4-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_LINE_IN_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_LINE_IN_VOLUME
)


STATIC_KSAUDFNAME_MIC_IN_VOLUME = (
    0x185FEDF5,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MIC_IN_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDF5-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MIC_IN_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIC_IN_VOLUME
)


STATIC_KSAUDFNAME_WAVE_IN_VOLUME = (
    0x185FEDF6,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_WAVE_IN_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDF6-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_WAVE_IN_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_WAVE_IN_VOLUME
)


STATIC_KSAUDFNAME_VOLUME_CONTROL = (
    0x185FEDF7,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_VOLUME_CONTROL = DEFINE_GUIDSTRUCT(
    "185FEDF7-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_VOLUME_CONTROL = DEFINE_GUIDNAMED(
    KSAUDFNAME_VOLUME_CONTROL
)


STATIC_KSAUDFNAME_MIDI = (
    0x185FEDF8,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_MIDI = DEFINE_GUIDSTRUCT(
    "185FEDF8-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_MIDI = DEFINE_GUIDNAMED(
    KSAUDFNAME_MIDI
)


STATIC_KSAUDFNAME_LINE_IN = (
    0x185FEDF9,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_LINE_IN = DEFINE_GUIDSTRUCT(
    "185FEDF9-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_LINE_IN = DEFINE_GUIDNAMED(
    KSAUDFNAME_LINE_IN
)


STATIC_KSAUDFNAME_RECORDING_CONTROL = (
    0x185FEDFA,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_RECORDING_CONTROL = DEFINE_GUIDSTRUCT(
    "185FEDFA-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_RECORDING_CONTROL = DEFINE_GUIDNAMED(
    KSAUDFNAME_RECORDING_CONTROL
)


STATIC_KSAUDFNAME_CD_AUDIO = (
    0x185FEDFB,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_CD_AUDIO = DEFINE_GUIDSTRUCT(
    "185FEDFB-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_CD_AUDIO = DEFINE_GUIDNAMED(
    KSAUDFNAME_CD_AUDIO
)


STATIC_KSAUDFNAME_AUX_VOLUME = (
    0x185FEDFC,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_AUX_VOLUME = DEFINE_GUIDSTRUCT(
    "185FEDFC-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_AUX_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_AUX_VOLUME
)


STATIC_KSAUDFNAME_AUX_MUTE = (
    0x185FEDFD,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_AUX_MUTE = DEFINE_GUIDSTRUCT(
    "185FEDFD-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_AUX_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_AUX_MUTE
)


STATIC_KSAUDFNAME_AUX = (
    0x185FEDFE,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_AUX = DEFINE_GUIDSTRUCT(
    "185FEDFE-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_AUX = DEFINE_GUIDNAMED(
    KSAUDFNAME_AUX
)


STATIC_KSAUDFNAME_PC_SPEAKER = (
    0x185FEDFF,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_PC_SPEAKER = DEFINE_GUIDSTRUCT(
    "185FEDFF-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_PC_SPEAKER = DEFINE_GUIDNAMED(
    KSAUDFNAME_PC_SPEAKER
)


STATIC_KSAUDFNAME_WAVE_OUT_MIX = (
    0x185FEE00,
    0x9905,
    0x11D1,
    0x95,
    0xA9,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSAUDFNAME_WAVE_OUT_MIX = DEFINE_GUIDSTRUCT(
    "185FEE00-9905-11D1-95A9-00C04FB925D3"
)
KSAUDFNAME_WAVE_OUT_MIX = DEFINE_GUIDNAMED(
    KSAUDFNAME_WAVE_OUT_MIX
)


STATIC_KSAUDFNAME_MONO_OUT = (
    0xF9B41DC3,
    0x96E2,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_MONO_OUT = DEFINE_GUIDSTRUCT(
    "F9B41DC3-96E2-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_MONO_OUT = DEFINE_GUIDNAMED(
    KSAUDFNAME_MONO_OUT
)


STATIC_KSAUDFNAME_STEREO_MIX = (
    0xDFF077,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_STEREO_MIX = DEFINE_GUIDSTRUCT(
    "00DFF077-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_STEREO_MIX = DEFINE_GUIDNAMED(
    KSAUDFNAME_STEREO_MIX
)


STATIC_KSAUDFNAME_MONO_MIX = (
    0xDFF078,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_MONO_MIX = DEFINE_GUIDSTRUCT(
    "00DFF078-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_MONO_MIX = DEFINE_GUIDNAMED(
    KSAUDFNAME_MONO_MIX
)


STATIC_KSAUDFNAME_MONO_OUT_VOLUME = (
    0x1AD247EB,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_MONO_OUT_VOLUME = DEFINE_GUIDSTRUCT(
    "1AD247EB-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_MONO_OUT_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_MONO_OUT_VOLUME
)


STATIC_KSAUDFNAME_MONO_OUT_MUTE = (
    0x1AD247EC,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_MONO_OUT_MUTE = DEFINE_GUIDSTRUCT(
    "1AD247EC-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_MONO_OUT_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_MONO_OUT_MUTE
)


STATIC_KSAUDFNAME_STEREO_MIX_VOLUME = (
    0x1AD247ED,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_STEREO_MIX_VOLUME = DEFINE_GUIDSTRUCT(
    "1AD247ED-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_STEREO_MIX_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_STEREO_MIX_VOLUME
)


STATIC_KSAUDFNAME_STEREO_MIX_MUTE = (
    0x22B0EAFD,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_STEREO_MIX_MUTE = DEFINE_GUIDSTRUCT(
    "22B0EAFD-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_STEREO_MIX_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_STEREO_MIX_MUTE
)


STATIC_KSAUDFNAME_MONO_MIX_VOLUME = (
    0x22B0EAFE,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_MONO_MIX_VOLUME = DEFINE_GUIDSTRUCT(
    "22B0EAFE-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_MONO_MIX_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_MONO_MIX_VOLUME
)


STATIC_KSAUDFNAME_MONO_MIX_MUTE = (
    0x2BC31D69,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_MONO_MIX_MUTE = DEFINE_GUIDSTRUCT(
    "2BC31D69-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_MONO_MIX_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_MONO_MIX_MUTE
)


STATIC_KSAUDFNAME_MICROPHONE_BOOST = (
    0x2BC31D6A,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_MICROPHONE_BOOST = DEFINE_GUIDSTRUCT(
    "2BC31D6A-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_MICROPHONE_BOOST = DEFINE_GUIDNAMED(
    KSAUDFNAME_MICROPHONE_BOOST
)


STATIC_KSAUDFNAME_ALTERNATE_MICROPHONE = (
    0x2BC31D6B,
    0x96E3,
    0x11D2,
    0xAC,
    0x4C,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_ALTERNATE_MICROPHONE = DEFINE_GUIDSTRUCT(
    "2BC31D6B-96E3-11d2-AC4C-00C04F8EFB68"
)
KSAUDFNAME_ALTERNATE_MICROPHONE = DEFINE_GUIDNAMED(
    KSAUDFNAME_ALTERNATE_MICROPHONE
)


STATIC_KSAUDFNAME_3D_DEPTH = (
    0x63FF5747,
    0x991F,
    0x11D2,
    0xAC,
    0x4D,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_3D_DEPTH = DEFINE_GUIDSTRUCT(
    "63FF5747-991F-11d2-AC4D-00C04F8EFB68"
)
KSAUDFNAME_3D_DEPTH = DEFINE_GUIDNAMED(
    KSAUDFNAME_3D_DEPTH
)


STATIC_KSAUDFNAME_3D_CENTER = (
    0x9F0670B4,
    0x991F,
    0x11D2,
    0xAC,
    0x4D,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_3D_CENTER = DEFINE_GUIDSTRUCT(
    "9F0670B4-991F-11d2-AC4D-00C04F8EFB68"
)
KSAUDFNAME_3D_CENTER = DEFINE_GUIDNAMED(
    KSAUDFNAME_3D_CENTER
)


STATIC_KSAUDFNAME_VIDEO_VOLUME = (
    0x9B46E708,
    0x992A,
    0x11D2,
    0xAC,
    0x4D,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_VIDEO_VOLUME = DEFINE_GUIDSTRUCT(
    "9B46E708-992A-11d2-AC4D-00C04F8EFB68"
)
KSAUDFNAME_VIDEO_VOLUME = DEFINE_GUIDNAMED(
    KSAUDFNAME_VIDEO_VOLUME
)


STATIC_KSAUDFNAME_VIDEO_MUTE = (
    0x9B46E709,
    0x992A,
    0x11D2,
    0xAC,
    0x4D,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_VIDEO_MUTE = DEFINE_GUIDSTRUCT(
    "9B46E709-992A-11d2-AC4D-00C04F8EFB68"
)
KSAUDFNAME_VIDEO_MUTE = DEFINE_GUIDNAMED(
    KSAUDFNAME_VIDEO_MUTE
)


STATIC_KSAUDFNAME_VIDEO = (
    0x915DAEC4,
    0xA434,
    0x11D2,
    0xAC,
    0x52,
    0x0,
    0xC0,
    0x4F,
    0x8E,
    0xFB,
    0x68,
)
KSAUDFNAME_VIDEO = DEFINE_GUIDSTRUCT(
    "915DAEC4-A434-11d2-AC52-00C04F8EFB68"
)
KSAUDFNAME_VIDEO = DEFINE_GUIDNAMED(
    KSAUDFNAME_VIDEO
)


STATIC_KSAUDFNAME_PEAKMETER = (
    0x57E24340,
    0xFC5B,
    0x4612,
    0xA5,
    0x62,
    0x72,
    0xB1,
    0x1A,
    0x29,
    0xDF,
    0xAE,
)
KSAUDFNAME_PEAKMETER = DEFINE_GUIDSTRUCT(
    "57E24340-FC5B-4612-A562-72B11A29DFAE"
)
KSAUDFNAME_PEAKMETER = DEFINE_GUIDNAMED(
    KSAUDFNAME_PEAKMETER
)


# KSMETHODSETID

STATIC_KSMETHODSETID_Wavetable = (
    0xDCEF31EB,
    0xD907,
    0x11D0,
    0x95,
    0x83,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSMETHODSETID_Wavetable = DEFINE_GUIDSTRUCT(
    "DCEF31EB-D907-11D0-9583-00C04FB925D3"
)
KSMETHODSETID_Wavetable = DEFINE_GUIDNAMED(
    KSMETHODSETID_Wavetable
)


STATIC_KSMETHODSETID_Wave_Queued = (
    0x7432C160,
    0x8827,
    0x11CF,
    0xA1,
    0x02,
    0x00,
    0x20,
    0xAF,
    0xD1,
    0x56,
    0xE4,
)
KSMETHODSETID_Wave_Queued = DEFINE_GUIDSTRUCT(
    "7432c160-8827-11cf-a102-0020afd156e4"
)
KSMETHODSETID_Wave_Queued = DEFINE_GUIDNAMED(
    KSMETHODSETID_Wave_Queued
)


# KSPROPERTYSETID

STATIC_KSPROPERTYSETID_ExtendedCameraControl = (
    0x1CB79112,
    0xC0D2,
    0x4213,
    0x9C,
    0xA6,
    0xCD,
    0x4F,
    0xDB,
    0x92,
    0x79,
    0x72,
)
KSPROPERTYSETID_ExtendedCameraControl = DEFINE_GUIDSTRUCT(
    "1CB79112-C0D2-4213-9CA6-CD4FDB927972"
)
KSPROPERTYSETID_ExtendedCameraControl = DEFINE_GUIDNAMED(
    KSPROPERTYSETID_ExtendedCameraControl
)


STATIC_KSPROPERTYSETID_PerFrameSettingControl = (
    0xF1F3E261,
    0xDEE6,
    0x4537,
    0xBF,
    0xF5,
    0xEE,
    0x20,
    0x6D,
    0xB5,
    0x4A,
    0xAC,
)
KSPROPERTYSETID_PerFrameSettingControl = DEFINE_GUIDSTRUCT(
    "F1F3E261-DEE6-4537-BFF5-EE206DB54AAC"
)
KSPROPERTYSETID_PerFrameSettingControl = DEFINE_GUIDNAMED(
    KSPROPERTYSETID_PerFrameSettingControl
)


# KSALGORITHMINSTANCE

STATIC_KSALGORITHMINSTANCE_SYSTEM_ACOUSTIC_ECHO_CANCEL = (
    0x1C22C56D,
    0x9879,
    0x4F5B,
    0xA3,
    0x89,
    0x27,
    0x99,
    0x6D,
    0xDC,
    0x28,
    0x10,
)
KSALGORITHMINSTANCE_SYSTEM_ACOUSTIC_ECHO_CANCEL = DEFINE_GUIDSTRUCT(
    "1C22C56D-9879-4f5b-A389-27996DDC2810"
)
KSALGORITHMINSTANCE_SYSTEM_ACOUSTIC_ECHO_CANCEL = DEFINE_GUIDNAMED(
    KSALGORITHMINSTANCE_SYSTEM_ACOUSTIC_ECHO_CANCEL
)


STATIC_KSALGORITHMINSTANCE_SYSTEM_NOISE_SUPPRESS = (
    0x5AB0882E,
    0x7274,
    0x4516,
    0x87,
    0x7D,
    0x4E,
    0xEE,
    0x99,
    0xBA,
    0x4F,
    0xD0,
)
KSALGORITHMINSTANCE_SYSTEM_NOISE_SUPPRESS = DEFINE_GUIDSTRUCT(
    "5AB0882E-7274-4516-877D-4EEE99BA4FD0"
)
KSALGORITHMINSTANCE_SYSTEM_NOISE_SUPPRESS = DEFINE_GUIDNAMED(
    KSALGORITHMINSTANCE_SYSTEM_NOISE_SUPPRESS
)


STATIC_KSALGORITHMINSTANCE_SYSTEM_AGC = (
    0x950E55B9,
    0x877C,
    0x4C67,
    0xBE,
    0x8,
    0xE4,
    0x7B,
    0x56,
    0x11,
    0x13,
    0xA,
)
KSALGORITHMINSTANCE_SYSTEM_AGC = DEFINE_GUIDSTRUCT(
    "950E55B9-877C-4c67-BE08-E47B5611130A"
)
KSALGORITHMINSTANCE_SYSTEM_AGC = DEFINE_GUIDNAMED(
    KSALGORITHMINSTANCE_SYSTEM_AGC
)


STATIC_KSALGORITHMINSTANCE_SYSTEM_MICROPHONE_ARRAY_PROCESSOR = (
    0xB6F5A0A0,
    0x9E61,
    0x4F8C,
    0x91,
    0xE3,
    0x76,
    0xCF,
    0xF,
    0x3C,
    0x47,
    0x1F,
)
KSALGORITHMINSTANCE_SYSTEM_MICROPHONE_ARRAY_PROCESSOR = DEFINE_GUIDSTRUCT(
    "B6F5A0A0-9E61-4f8c-91E3-76CF0F3C471F"
)
KSALGORITHMINSTANCE_SYSTEM_MICROPHONE_ARRAY_PROCESSOR = DEFINE_GUIDNAMED(
    KSALGORITHMINSTANCE_SYSTEM_MICROPHONE_ARRAY_PROCESSOR
)


# KSATTRIBUTEID

STATIC_KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE = (
    0xE1F89EB5,
    0x5F46,
    0x419B,
    0x96,
    0x7B,
    0xFF,
    0x67,
    0x70,
    0xB9,
    0x84,
    0x1,
)
KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE = DEFINE_GUIDSTRUCT(
    "E1F89EB5-5F46-419B-967B-FF6770B98401"
)
KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE = DEFINE_GUIDNAMED(
    KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE
)


# AUDIOENDPOINT

STATIC_AUDIOENDPOINT_CLASS_UUID = (
    0xC166523C,
    0xFE0C,
    0x4A94,
    0xA5,
    0x86,
    0xF1,
    0xA8,
    0x0C,
    0xFB,
    0xBF,
    0x3E,
)
AUDIOENDPOINT_CLASS_UUID = DEFINE_GUIDSTRUCT(
    "C166523C-FE0C-4A94-A586-F1A80CFBBF3E"
)
AUDIOENDPOINT_CLASS_UUID = DEFINE_GUIDNAMED(
    AUDIOENDPOINT_CLASS_UUID
)


# KS_SECURE

STATIC_KS_SECURE_CAMERA_SCENARIO_ID = (
    0xAE53FC6E,
    0x8D89,
    0x4488,
    0x9D,
    0x2E,
    0x4D,
    0x00,
    0x87,
    0x31,
    0xC5,
    0xFD,
)
KS_SECURE_CAMERA_SCENARIO_ID = DEFINE_GUIDSTRUCT(
    "AE53FC6E-8D89-4488-9D2E-4D008731C5FD"
)
KS_SECURE_CAMERA_SCENARIO_ID = DEFINE_GUIDNAMED(
    KS_SECURE_CAMERA_SCENARIO_ID
)


# ENCAPIPARAM

STATIC_ENCAPIPARAM_BITRATE = (
    0x49CC4C43,
    0xCA83,
    0x4AD4,
    0xA9,
    0xAF,
    0xF3,
    0x69,
    0x6A,
    0xF6,
    0x66,
    0xDF,
)
ENCAPIPARAM_BITRATE = DEFINE_GUIDSTRUCT(
    "49CC4C43-CA83-4ad4-A9AF-F3696AF666DF"
)
ENCAPIPARAM_BITRATE = DEFINE_GUIDNAMED(
    ENCAPIPARAM_BITRATE
)


STATIC_ENCAPIPARAM_PEAK_BITRATE = (
    0x703F16A9,
    0x3D48,
    0x44A1,
    0xB0,
    0x77,
    0x1,
    0x8D,
    0xFF,
    0x91,
    0x5D,
    0x19,
)
ENCAPIPARAM_PEAK_BITRATE = DEFINE_GUIDSTRUCT(
    "703F16A9-3D48-44a1-B077-018DFF915D19"
)
ENCAPIPARAM_PEAK_BITRATE = DEFINE_GUIDNAMED(
    ENCAPIPARAM_PEAK_BITRATE
)


STATIC_ENCAPIPARAM_BITRATE_MODE = (
    0xEE5FB25C,
    0xC713,
    0x40D1,
    0x9D,
    0x58,
    0xC0,
    0xD7,
    0x24,
    0x1E,
    0x25,
    0xF,
)
ENCAPIPARAM_BITRATE_MODE = DEFINE_GUIDSTRUCT(
    "EE5FB25C-C713-40d1-9D58-C0D7241E250F"
)
ENCAPIPARAM_BITRATE_MODE = DEFINE_GUIDNAMED(
    ENCAPIPARAM_BITRATE_MODE
)


# KSCATEGORY

STATIC_KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR = (
    0x830A44F2,
    0xA32D,
    0x476B,
    0xBE,
    0x97,
    0x42,
    0x84,
    0x56,
    0x73,
    0xB3,
    0x5A,
)
KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR = DEFINE_GUIDSTRUCT(
    "830a44f2-a32d-476b-be97-42845673b35a"
)

KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR = DEFINE_GUIDNAMED(
    KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR
)


STATIC_KSCATEGORY_AUDIO = (
    0x6994AD04,
    0x93EF,
    0x11D0,
    0xA3,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_AUDIO = DEFINE_GUIDSTRUCT(
    "6994AD04-93EF-11D0-A3CC-00A0C9223196"
)
KSCATEGORY_AUDIO = DEFINE_GUIDNAMED(
    KSCATEGORY_AUDIO
)


STATIC_KSCATEGORY_VIDEO = (
    0x6994AD05,
    0x93EF,
    0x11D0,
    0xA3,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_VIDEO = DEFINE_GUIDSTRUCT(
    "6994AD05-93EF-11D0-A3CC-00A0C9223196"
)
KSCATEGORY_VIDEO = DEFINE_GUIDNAMED(
    KSCATEGORY_VIDEO
)


STATIC_KSCATEGORY_REALTIME = (
    0xEB115FFC,
    0x10C8,
    0x4964,
    0x83,
    0x1D,
    0x6D,
    0xCB,
    0x02,
    0xE6,
    0xF2,
    0x3F,
)
KSCATEGORY_REALTIME = DEFINE_GUIDSTRUCT(
    "EB115FFC-10C8-4964-831D-6DCB02E6F23F"
)
KSCATEGORY_REALTIME = DEFINE_GUIDNAMED(
    KSCATEGORY_REALTIME
)


STATIC_KSCATEGORY_TEXT = (
    0x6994AD06,
    0x93EF,
    0x11D0,
    0xA3,
    0xCC,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_TEXT = DEFINE_GUIDSTRUCT(
    "6994AD06-93EF-11D0-A3CC-00A0C9223196"
)
KSCATEGORY_TEXT = DEFINE_GUIDNAMED(
    KSCATEGORY_TEXT
)


STATIC_KSCATEGORY_NETWORK = (
    0x67C9CC3C,
    0x69C4,
    0x11D2,
    0x87,
    0x59,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_NETWORK = DEFINE_GUIDSTRUCT(
    "67C9CC3C-69C4-11D2-8759-00A0C9223196"
)
KSCATEGORY_NETWORK = DEFINE_GUIDNAMED(
    KSCATEGORY_NETWORK
)


STATIC_KSCATEGORY_TOPOLOGY = (
    0xDDA54A40,
    0x1E4C,
    0x11D1,
    0xA0,
    0x50,
    0x40,
    0x57,
    0x05,
    0xC1,
    0x00,
    0x00,
)
KSCATEGORY_TOPOLOGY = DEFINE_GUIDSTRUCT(
    "DDA54A40-1E4C-11D1-A050-405705C10000"
)
KSCATEGORY_TOPOLOGY = DEFINE_GUIDNAMED(
    KSCATEGORY_TOPOLOGY
)


STATIC_KSCATEGORY_VIRTUAL = (
    0x3503EAC4,
    0x1F26,
    0x11D1,
    0x8A,
    0xB0,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSCATEGORY_VIRTUAL = DEFINE_GUIDSTRUCT(
    "3503EAC4-1F26-11D1-8AB0-00A0C9223196"
)
KSCATEGORY_VIRTUAL = DEFINE_GUIDNAMED(
    KSCATEGORY_VIRTUAL
)


STATIC_KSCATEGORY_ACOUSTIC_ECHO_CANCEL = (
    0xBF963D80,
    0xC559,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSCATEGORY_ACOUSTIC_ECHO_CANCEL = DEFINE_GUIDSTRUCT(
    "BF963D80-C559-11D0-8A2B-00A0C9255AC1"
)
KSCATEGORY_ACOUSTIC_ECHO_CANCEL = DEFINE_GUIDNAMED(
    KSCATEGORY_ACOUSTIC_ECHO_CANCEL
)


STATIC_KSCATEGORY_SYSAUDIO = (
    0xA7C7A5B1,
    0x5AF3,
    0x11D1,
    0x9C,
    0xED,
    0x00,
    0xA0,
    0x24,
    0xBF,
    0x04,
    0x07,
)
KSCATEGORY_SYSAUDIO = DEFINE_GUIDSTRUCT(
    "A7C7A5B1-5AF3-11D1-9CED-00A024BF0407"
)
KSCATEGORY_SYSAUDIO = DEFINE_GUIDNAMED(
    KSCATEGORY_SYSAUDIO
)


STATIC_KSCATEGORY_WDMAUD = (
    0x3E227E76,
    0x690D,
    0x11D2,
    0x81,
    0x61,
    0x00,
    0x00,
    0xF8,
    0x77,
    0x5B,
    0xF1,
)
KSCATEGORY_WDMAUD = DEFINE_GUIDSTRUCT(
    "3E227E76-690D-11D2-8161-0000F8775BF1"
)
KSCATEGORY_WDMAUD = DEFINE_GUIDNAMED(
    KSCATEGORY_WDMAUD
)


STATIC_KSCATEGORY_AUDIO_GFX = (
    0x9BAF9572,
    0x340C,
    0x11D3,
    0xAB,
    0xDC,
    0x00,
    0xA0,
    0xC9,
    0x0A,
    0xB1,
    0x6F,
)
KSCATEGORY_AUDIO_GFX = DEFINE_GUIDSTRUCT(
    "9BAF9572-340C-11D3-ABDC-00A0C90AB16F"
)
KSCATEGORY_AUDIO_GFX = DEFINE_GUIDNAMED(
    KSCATEGORY_AUDIO_GFX
)


STATIC_KSCATEGORY_AUDIO_SPLITTER = (
    0x9EA331FA,
    0xB91B,
    0x45F8,
    0x92,
    0x85,
    0xBD,
    0x2B,
    0xC7,
    0x7A,
    0xFC,
    0xDE,
)
KSCATEGORY_AUDIO_SPLITTER = DEFINE_GUIDSTRUCT(
    "9EA331FA-B91B-45F8-9285-BD2BC77AFCDE"
)
KSCATEGORY_AUDIO_SPLITTER = DEFINE_GUIDNAMED(
    KSCATEGORY_AUDIO_SPLITTER
)


STATIC_KSCATEGORY_AUDIO_DEVICE = (
    0xFBF6F530,
    0x07B9,
    0x11D2,
    0xA7,
    0x1E,
    0x00,
    0x00,
    0xF8,
    0x00,
    0x47,
    0x88,
)
KSCATEGORY_AUDIO_DEVICE = DEFINE_GUIDSTRUCT(
    "FBF6F530-07B9-11D2-A71E-0000F8004788"
)
KSCATEGORY_AUDIO_DEVICE = DEFINE_GUIDNAMED(
    KSCATEGORY_AUDIO_DEVICE
)


STATIC_KSCATEGORY_PREFERRED_WAVEOUT_DEVICE = (
    0xD6C5066E,
    0x72C1,
    0x11D2,
    0x97,
    0x55,
    0x00,
    0x00,
    0xF8,
    0x00,
    0x47,
    0x88,
)
KSCATEGORY_PREFERRED_WAVEOUT_DEVICE = DEFINE_GUIDSTRUCT(
    "D6C5066E-72C1-11D2-9755-0000F8004788"
)
KSCATEGORY_PREFERRED_WAVEOUT_DEVICE = DEFINE_GUIDNAMED(
    KSCATEGORY_PREFERRED_WAVEOUT_DEVICE
)


STATIC_KSCATEGORY_PREFERRED_WAVEIN_DEVICE = (
    0xD6C50671,
    0x72C1,
    0x11D2,
    0x97,
    0x55,
    0x00,
    0x00,
    0xF8,
    0x00,
    0x47,
    0x88,
)
KSCATEGORY_PREFERRED_WAVEIN_DEVICE = DEFINE_GUIDSTRUCT(
    "D6C50671-72C1-11D2-9755-0000F8004788"
)
KSCATEGORY_PREFERRED_WAVEIN_DEVICE = DEFINE_GUIDNAMED(
    KSCATEGORY_PREFERRED_WAVEIN_DEVICE
)


STATIC_KSCATEGORY_PREFERRED_MIDIOUT_DEVICE = (
    0xD6C50674,
    0x72C1,
    0x11D2,
    0x97,
    0x55,
    0x00,
    0x00,
    0xF8,
    0x00,
    0x47,
    0x88,
)
KSCATEGORY_PREFERRED_MIDIOUT_DEVICE = DEFINE_GUIDSTRUCT(
    "D6C50674-72C1-11D2-9755-0000F8004788"
)
KSCATEGORY_PREFERRED_MIDIOUT_DEVICE = DEFINE_GUIDNAMED(
    KSCATEGORY_PREFERRED_MIDIOUT_DEVICE
)


STATIC_KSCATEGORY_WDMAUD_USE_PIN_NAME = (
    0x47A4FA20,
    0xA251,
    0x11D1,
    0xA0,
    0x50,
    0x00,
    0x00,
    0xF8,
    0x00,
    0x47,
    0x88,
)
KSCATEGORY_WDMAUD_USE_PIN_NAME = DEFINE_GUIDSTRUCT(
    "47A4FA20-A251-11D1-A050-0000F8004788"
)
KSCATEGORY_WDMAUD_USE_PIN_NAME = DEFINE_GUIDNAMED(
    KSCATEGORY_WDMAUD_USE_PIN_NAME
)


STATIC_KSCATEGORY_ESCALANTE_PLATFORM_DRIVER = (
    0x74F3AEA8,
    0x9768,
    0x11D1,
    0x8E,
    0x07,
    0x00,
    0xA0,
    0xC9,
    0x5E,
    0xC2,
    0x2E,
)
KSCATEGORY_ESCALANTE_PLATFORM_DRIVER = DEFINE_GUIDSTRUCT(
    "74f3aea8-9768-11d1-8e07-00a0c95ec22e"
)
KSCATEGORY_ESCALANTE_PLATFORM_DRIVER = DEFINE_GUIDNAMED(
    KSCATEGORY_ESCALANTE_PLATFORM_DRIVER
)


STATIC_KSCATEGORY_TVTUNER = (
    0xA799A800,
    0xA46D,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0x24,
    0x01,
    0xDC,
    0xD4,
)
KSCATEGORY_TVTUNER = DEFINE_GUIDSTRUCT(
    "a799a800-a46d-11d0-a18c-00a02401dcd4"
)
KSCATEGORY_TVTUNER = DEFINE_GUIDNAMED(
    KSCATEGORY_TVTUNER
)


STATIC_KSCATEGORY_CROSSBAR = (
    0xA799A801,
    0xA46D,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0x24,
    0x01,
    0xDC,
    0xD4,
)
KSCATEGORY_CROSSBAR = DEFINE_GUIDSTRUCT(
    "a799a801-a46d-11d0-a18c-00a02401dcd4"
)
KSCATEGORY_CROSSBAR = DEFINE_GUIDNAMED(
    KSCATEGORY_CROSSBAR
)


STATIC_KSCATEGORY_TVAUDIO = (
    0xA799A802,
    0xA46D,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0x24,
    0x01,
    0xDC,
    0xD4,
)
KSCATEGORY_TVAUDIO = DEFINE_GUIDSTRUCT(
    "a799a802-a46d-11d0-a18c-00a02401dcd4"
)
KSCATEGORY_TVAUDIO = DEFINE_GUIDNAMED(
    KSCATEGORY_TVAUDIO
)


STATIC_KSCATEGORY_VPMUX = (
    0xA799A803,
    0xA46D,
    0x11D0,
    0xA1,
    0x8C,
    0x00,
    0xA0,
    0x24,
    0x01,
    0xDC,
    0xD4,
)
KSCATEGORY_VPMUX = DEFINE_GUIDSTRUCT(
    "a799a803-a46d-11d0-a18c-00a02401dcd4"
)
KSCATEGORY_VPMUX = DEFINE_GUIDNAMED(
    KSCATEGORY_VPMUX
)


STATIC_KSCATEGORY_VBICODEC = (
    0x07DAD660,
    0x22F1,
    0x11D1,
    0xA9,
    0xF4,
    0x00,
    0xC0,
    0x4F,
    0xBB,
    0xDE,
    0x8F,
)
KSCATEGORY_VBICODEC = DEFINE_GUIDSTRUCT(
    "07dad660-22f1-11d1-a9f4-00c04fbbde8f"
)
KSCATEGORY_VBICODEC = DEFINE_GUIDNAMED(
    KSCATEGORY_VBICODEC
)


STATIC_KSCATEGORY_ENCODER = (
    0x19689BF6,
    0xC384,
    0x48FD,
    0xAD,
    0x51,
    0x90,
    0xE5,
    0x8C,
    0x79,
    0xF7,
    0xB,
)
KSCATEGORY_ENCODER = DEFINE_GUIDSTRUCT(
    "19689BF6-C384-48fd-AD51-90E58C79F70B"
)
KSCATEGORY_ENCODER = DEFINE_GUIDNAMED(
    KSCATEGORY_ENCODER
)


STATIC_KSCATEGORY_MULTIPLEXER = (
    0x7A5DE1D3,
    0x1A1,
    0x452C,
    0xB4,
    0x81,
    0x4F,
    0xA2,
    0xB9,
    0x62,
    0x71,
    0xE8,
)
KSCATEGORY_MULTIPLEXER = DEFINE_GUIDSTRUCT(
    "7A5DE1D3-01A1-452c-B481-4FA2B96271E8"
)
KSCATEGORY_MULTIPLEXER = DEFINE_GUIDNAMED(
    KSCATEGORY_MULTIPLEXER
)


# BLUETOOTH

STATIC_BLUETOOTH_MIDI_DATAIO_CHARACTERISTIC = (
    0x7772E5DB,
    0x3868,
    0x4112,
    0xA1,
    0xA9,
    0xF2,
    0x66,
    0x9D,
    0x10,
    0x6B,
    0xF3,
)
BLUETOOTH_MIDI_DATAIO_CHARACTERISTIC = DEFINE_GUIDSTRUCT(
    "7772E5DB-3868-4112-A1A9-F2669D106BF3"
)
BLUETOOTH_MIDI_DATAIO_CHARACTERISTIC = DEFINE_GUIDNAMED(
    BLUETOOTH_MIDI_DATAIO_CHARACTERISTIC
)


# APO

STATIC_APO_CLASS_UUID = (
    0x5989FCE8,
    0x9CD0,
    0x467D,
    0x8A,
    0x6A,
    0x54,
    0x19,
    0xE3,
    0x15,
    0x29,
    0xD4,
)
APO_CLASS_UUID = DEFINE_GUIDSTRUCT(
    "5989fce8-9cd0-467d-8a6a-5419e31529d4"
)
APO_CLASS_UUID = DEFINE_GUIDNAMED(
    APO_CLASS_UUID
)


# PINNAME

STATIC_PINNAME_SPDIF_OUT = (
    0x3A264481,
    0xE52C,
    0x4B82,
    0x8E,
    0x7A,
    0xC8,
    0xE2,
    0xF9,
    0x1D,
    0xC3,
    0x80,
)
PINNAME_SPDIF_OUT = DEFINE_GUIDSTRUCT(
    "3A264481-E52C-4b82-8E7A-C8E2F91DC380"
)
PINNAME_SPDIF_OUT = DEFINE_GUIDNAMED(
    PINNAME_SPDIF_OUT
)


STATIC_PINNAME_SPDIF_IN = (
    0x15DC9025,
    0x22AD,
    0x41B3,
    0x88,
    0x75,
    0xF4,
    0xCE,
    0xB0,
    0x29,
    0x9E,
    0x20,
)
PINNAME_SPDIF_IN = DEFINE_GUIDSTRUCT(
    "15DC9025-22AD-41b3-8875-F4CEB0299E20"
)
PINNAME_SPDIF_IN = DEFINE_GUIDNAMED(
    PINNAME_SPDIF_IN
)


STATIC_PINNAME_HDMI_OUT = (
    0x387BFC03,
    0xE7EF,
    0x4901,
    0x86,
    0xE0,
    0x35,
    0xB7,
    0xC3,
    0x2B,
    0x0,
    0xEF,
)
PINNAME_HDMI_OUT = DEFINE_GUIDSTRUCT(
    "387BFC03-E7EF-4901-86E0-35B7C32B00EF"
)
PINNAME_HDMI_OUT = DEFINE_GUIDNAMED(
    PINNAME_HDMI_OUT
)


STATIC_PINNAME_DISPLAYPORT_OUT = (
    0x21FBB329,
    0x1A4A,
    0x48DA,
    0xA0,
    0x76,
    0x23,
    0x18,
    0xA3,
    0xC5,
    0x9B,
    0x26,
)
PINNAME_DISPLAYPORT_OUT = DEFINE_GUIDSTRUCT(
    "21FBB329-1A4A-48da-A076-2318A3C59B26"
)
PINNAME_DISPLAYPORT_OUT = DEFINE_GUIDNAMED(
    PINNAME_DISPLAYPORT_OUT
)


STATIC_PINNAME_VIDEO_CAPTURE = (
    0xFB6C4281,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
STATIC_PINNAME_CAPTURE = STATIC_PINNAME_VIDEO_CAPTURE
PINNAME_VIDEO_CAPTURE = DEFINE_GUIDSTRUCT(
    "FB6C4281-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_CAPTURE = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_CAPTURE
)
PINNAME_CAPTURE = PINNAME_VIDEO_CAPTURE


STATIC_PINNAME_VIDEO_CC_CAPTURE = (
    0x1AAD8061,
    0x12D,
    0x11D2,
    0xB4,
    0xB1,
    0x0,
    0xA0,
    0xD1,
    0x2,
    0xCF,
    0xBE,
)
STATIC_PINNAME_CC_CAPTURE = STATIC_PINNAME_VIDEO_CC_CAPTURE
PINNAME_VIDEO_CC_CAPTURE = DEFINE_GUIDSTRUCT(
    "1AAD8061-012D-11d2-B4B1-00A0D102CFBE"
)
PINNAME_VIDEO_CC_CAPTURE = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_CC_CAPTURE
)


STATIC_PINNAME_VIDEO_NABTS_CAPTURE = (
    0x29703660,
    0x498A,
    0x11D2,
    0xB4,
    0xB1,
    0x0,
    0xA0,
    0xD1,
    0x2,
    0xCF,
    0xBE,
)
STATIC_PINNAME_NABTS_CAPTURE = STATIC_PINNAME_VIDEO_NABTS_CAPTURE
PINNAME_VIDEO_NABTS_CAPTURE = DEFINE_GUIDSTRUCT(
    "29703660-498A-11d2-B4B1-00A0D102CFBE"
)
PINNAME_VIDEO_NABTS_CAPTURE = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_NABTS_CAPTURE
)


STATIC_PINNAME_VIDEO_PREVIEW = (
    0xFB6C4282,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
STATIC_PINNAME_PREVIEW = STATIC_PINNAME_VIDEO_PREVIEW
PINNAME_VIDEO_PREVIEW = DEFINE_GUIDSTRUCT(
    "FB6C4282-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_PREVIEW = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_PREVIEW
)
PINNAME_PREVIEW = PINNAME_VIDEO_PREVIEW


STATIC_PINNAME_VIDEO_ANALOGVIDEOIN = (
    0xFB6C4283,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_ANALOGVIDEOIN = DEFINE_GUIDSTRUCT(
    "FB6C4283-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_ANALOGVIDEOIN = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_ANALOGVIDEOIN
)


STATIC_PINNAME_VIDEO_VBI = (
    0xFB6C4284,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_VBI = DEFINE_GUIDSTRUCT(
    "FB6C4284-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_VBI = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_VBI
)


STATIC_PINNAME_VIDEO_VIDEOPORT = (
    0xFB6C4285,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_VIDEOPORT = DEFINE_GUIDSTRUCT(
    "FB6C4285-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_VIDEOPORT = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_VIDEOPORT
)


STATIC_PINNAME_VIDEO_NABTS = (
    0xFB6C4286,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_NABTS = DEFINE_GUIDSTRUCT(
    "FB6C4286-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_NABTS = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_NABTS
)


STATIC_PINNAME_VIDEO_EDS = (
    0xFB6C4287,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_EDS = DEFINE_GUIDSTRUCT(
    "FB6C4287-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_EDS = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_EDS
)


STATIC_PINNAME_VIDEO_TELETEXT = (
    0xFB6C4288,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_TELETEXT = DEFINE_GUIDSTRUCT(
    "FB6C4288-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_TELETEXT = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_TELETEXT
)


STATIC_PINNAME_VIDEO_CC = (
    0xFB6C4289,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_CC = DEFINE_GUIDSTRUCT(
    "FB6C4289-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_CC = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_CC
)


STATIC_PINNAME_VIDEO_STILL = (
    0xFB6C428A,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_STILL = DEFINE_GUIDSTRUCT(
    "FB6C428A-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_STILL = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_STILL
)


STATIC_PINNAME_IMAGE = (
    0x38A0CD98,
    0xD49B,
    0x4CE8,
    0xB4,
    0x8A,
    0x34,
    0x46,
    0x67,
    0xA1,
    0x78,
    0x30,
)
PINNAME_IMAGE = DEFINE_GUIDSTRUCT(
    "38A0CD98-D49B-4ce8-B48A-344667A17830"
)
PINNAME_IMAGE = DEFINE_GUIDNAMED(
    PINNAME_IMAGE
)


STATIC_PINNAME_VIDEO_TIMECODE = (
    0xFB6C428B,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_TIMECODE = DEFINE_GUIDSTRUCT(
    "FB6C428B-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_TIMECODE = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_TIMECODE
)


STATIC_PINNAME_VIDEO_VIDEOPORT_VBI = (
    0xFB6C428C,
    0x353,
    0x11D1,
    0x90,
    0x5F,
    0x0,
    0x0,
    0xC0,
    0xCC,
    0x16,
    0xBA,
)
PINNAME_VIDEO_VIDEOPORT_VBI = DEFINE_GUIDSTRUCT(
    "FB6C428C-0353-11d1-905F-0000C0CC16BA"
)
PINNAME_VIDEO_VIDEOPORT_VBI = DEFINE_GUIDNAMED(
    PINNAME_VIDEO_VIDEOPORT_VBI
)


# KSNODETYPE

STATIC_KSNODETYPE_INPUT_UNDEFINED = DEFINE_USB_TERMINAL_GUID(0x0200)
KSNODETYPE_INPUT_UNDEFINED = DEFINE_GUIDSTRUCT(
    "DFF21BE0-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_INPUT_UNDEFINED = DEFINE_GUIDNAMED(
    KSNODETYPE_INPUT_UNDEFINED
)


STATIC_KSNODETYPE_MICROPHONE = DEFINE_USB_TERMINAL_GUID(0x0201)
KSNODETYPE_MICROPHONE = DEFINE_GUIDSTRUCT(
    "DFF21BE1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_MICROPHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_MICROPHONE
)


STATIC_KSNODETYPE_DESKTOP_MICROPHONE = DEFINE_USB_TERMINAL_GUID(0x0202)
KSNODETYPE_DESKTOP_MICROPHONE = DEFINE_GUIDSTRUCT(
    "DFF21BE2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DESKTOP_MICROPHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_DESKTOP_MICROPHONE
)


STATIC_KSNODETYPE_PERSONAL_MICROPHONE = DEFINE_USB_TERMINAL_GUID(0x0203)
KSNODETYPE_PERSONAL_MICROPHONE = DEFINE_GUIDSTRUCT(
    "DFF21BE3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_PERSONAL_MICROPHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_PERSONAL_MICROPHONE
)
KSNODETYPE_HEADSET_MICROPHONE = KSNODETYPE_PERSONAL_MICROPHONE


STATIC_KSNODETYPE_OMNI_DIRECTIONAL_MICROPHONE = (
    DEFINE_USB_TERMINAL_GUID(0x0204)
)
KSNODETYPE_OMNI_DIRECTIONAL_MICROPHONE = DEFINE_GUIDSTRUCT(
    "DFF21BE4-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_OMNI_DIRECTIONAL_MICROPHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_OMNI_DIRECTIONAL_MICROPHONE
)


STATIC_KSNODETYPE_MICROPHONE_ARRAY = DEFINE_USB_TERMINAL_GUID(0x0205)
KSNODETYPE_MICROPHONE_ARRAY = DEFINE_GUIDSTRUCT(
    "DFF21BE5-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_MICROPHONE_ARRAY = DEFINE_GUIDNAMED(
    KSNODETYPE_MICROPHONE_ARRAY
)


STATIC_KSNODETYPE_PROCESSING_MICROPHONE_ARRAY = (
    DEFINE_USB_TERMINAL_GUID(0x0206)
)
KSNODETYPE_PROCESSING_MICROPHONE_ARRAY = DEFINE_GUIDSTRUCT(
    "DFF21BE6-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_PROCESSING_MICROPHONE_ARRAY = DEFINE_GUIDNAMED(
    KSNODETYPE_PROCESSING_MICROPHONE_ARRAY
)


STATIC_KSNODETYPE_OUTPUT_UNDEFINED = DEFINE_USB_TERMINAL_GUID(0x0300)
KSNODETYPE_OUTPUT_UNDEFINED = DEFINE_GUIDSTRUCT(
    "DFF21CE0-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_OUTPUT_UNDEFINED = DEFINE_GUIDNAMED(
    KSNODETYPE_OUTPUT_UNDEFINED
)


STATIC_KSNODETYPE_SPEAKER = DEFINE_USB_TERMINAL_GUID(0x0301)
KSNODETYPE_SPEAKER = DEFINE_GUIDSTRUCT(
    "DFF21CE1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_SPEAKER = DEFINE_GUIDNAMED(
    KSNODETYPE_SPEAKER
)


STATIC_KSNODETYPE_HEADPHONES = DEFINE_USB_TERMINAL_GUID(0x0302)
KSNODETYPE_HEADPHONES = DEFINE_GUIDSTRUCT(
    "DFF21CE2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_HEADPHONES = DEFINE_GUIDNAMED(
    KSNODETYPE_HEADPHONES
)


STATIC_KSNODETYPE_HEAD_MOUNTED_DISPLAY_AUDIO = DEFINE_USB_TERMINAL_GUID(0x0303)
KSNODETYPE_HEAD_MOUNTED_DISPLAY_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF21CE3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_HEAD_MOUNTED_DISPLAY_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_HEAD_MOUNTED_DISPLAY_AUDIO
)


STATIC_KSNODETYPE_DESKTOP_SPEAKER = DEFINE_USB_TERMINAL_GUID(0x0304)
KSNODETYPE_DESKTOP_SPEAKER = DEFINE_GUIDSTRUCT(
    "DFF21CE4-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DESKTOP_SPEAKER = DEFINE_GUIDNAMED(
    KSNODETYPE_DESKTOP_SPEAKER
)


STATIC_KSNODETYPE_ROOM_SPEAKER = DEFINE_USB_TERMINAL_GUID(0x0305)
KSNODETYPE_ROOM_SPEAKER = DEFINE_GUIDSTRUCT(
    "DFF21CE5-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_ROOM_SPEAKER = DEFINE_GUIDNAMED(
    KSNODETYPE_ROOM_SPEAKER
)


STATIC_KSNODETYPE_COMMUNICATION_SPEAKER = DEFINE_USB_TERMINAL_GUID(0x0306)
KSNODETYPE_COMMUNICATION_SPEAKER = DEFINE_GUIDSTRUCT(
    "DFF21CE6-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_COMMUNICATION_SPEAKER = DEFINE_GUIDNAMED(
    KSNODETYPE_COMMUNICATION_SPEAKER
)
KSNODETYPE_HEADSET_SPEAKERS = KSNODETYPE_COMMUNICATION_SPEAKER


STATIC_KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER = (
    DEFINE_USB_TERMINAL_GUID(0x0307)
)
KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER = DEFINE_GUIDSTRUCT(
    "DFF21CE7-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER = DEFINE_GUIDNAMED(
    KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER
)


STATIC_KSNODETYPE_BIDIRECTIONAL_UNDEFINED = DEFINE_USB_TERMINAL_GUID(0x0400)
KSNODETYPE_BIDIRECTIONAL_UNDEFINED = DEFINE_GUIDSTRUCT(
    "DFF21DE0-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_BIDIRECTIONAL_UNDEFINED = DEFINE_GUIDNAMED(
    KSNODETYPE_BIDIRECTIONAL_UNDEFINED
)


STATIC_KSNODETYPE_HANDSET = DEFINE_USB_TERMINAL_GUID(0x0401)
KSNODETYPE_HANDSET = DEFINE_GUIDSTRUCT(
    "DFF21DE1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_HANDSET = DEFINE_GUIDNAMED(
    KSNODETYPE_HANDSET
)


STATIC_KSNODETYPE_HEADSET = DEFINE_USB_TERMINAL_GUID(0x0402)
KSNODETYPE_HEADSET = DEFINE_GUIDSTRUCT(
    "DFF21DE2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_HEADSET = DEFINE_GUIDNAMED(
    KSNODETYPE_HEADSET
)


STATIC_KSNODETYPE_SPEAKERPHONE_NO_ECHO_REDUCTION = (
    DEFINE_USB_TERMINAL_GUID(0x0403)
)
KSNODETYPE_SPEAKERPHONE_NO_ECHO_REDUCTION = DEFINE_GUIDSTRUCT(
    "DFF21DE3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_SPEAKERPHONE_NO_ECHO_REDUCTION = DEFINE_GUIDNAMED(
    KSNODETYPE_SPEAKERPHONE_NO_ECHO_REDUCTION
)


STATIC_KSNODETYPE_ECHO_SUPPRESSING_SPEAKERPHONE = (
    DEFINE_USB_TERMINAL_GUID(0x0404)
)
KSNODETYPE_ECHO_SUPPRESSING_SPEAKERPHONE = DEFINE_GUIDSTRUCT(
    "DFF21DE4-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_ECHO_SUPPRESSING_SPEAKERPHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_ECHO_SUPPRESSING_SPEAKERPHONE
)


STATIC_KSNODETYPE_ECHO_CANCELING_SPEAKERPHONE = (
    DEFINE_USB_TERMINAL_GUID(0x0405)
)
KSNODETYPE_ECHO_CANCELING_SPEAKERPHONE = DEFINE_GUIDSTRUCT(
    "DFF21DE5-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_ECHO_CANCELING_SPEAKERPHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_ECHO_CANCELING_SPEAKERPHONE
)


STATIC_KSNODETYPE_TELEPHONY_UNDEFINED = DEFINE_USB_TERMINAL_GUID(0x0500)
KSNODETYPE_TELEPHONY_UNDEFINED = DEFINE_GUIDSTRUCT(
    "DFF21EE0-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_TELEPHONY_UNDEFINED = DEFINE_GUIDNAMED(
    KSNODETYPE_TELEPHONY_UNDEFINED
)


STATIC_KSNODETYPE_PHONE_LINE = DEFINE_USB_TERMINAL_GUID(0x0501)
KSNODETYPE_PHONE_LINE = DEFINE_GUIDSTRUCT(
    "DFF21EE1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_PHONE_LINE = DEFINE_GUIDNAMED(
    KSNODETYPE_PHONE_LINE
)


STATIC_KSNODETYPE_TELEPHONE = DEFINE_USB_TERMINAL_GUID(0x0502)
KSNODETYPE_TELEPHONE = DEFINE_GUIDSTRUCT(
    "DFF21EE2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_TELEPHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_TELEPHONE
)


STATIC_KSNODETYPE_DOWN_LINE_PHONE = DEFINE_USB_TERMINAL_GUID(0x0503)
KSNODETYPE_DOWN_LINE_PHONE = DEFINE_GUIDSTRUCT(
    "DFF21EE3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DOWN_LINE_PHONE = DEFINE_GUIDNAMED(
    KSNODETYPE_DOWN_LINE_PHONE
)


STATIC_KSNODETYPE_EXTERNAL_UNDEFINED = DEFINE_USB_TERMINAL_GUID(0x0600)
KSNODETYPE_EXTERNAL_UNDEFINED = DEFINE_GUIDSTRUCT(
    "DFF21FE0-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_EXTERNAL_UNDEFINED = DEFINE_GUIDNAMED(
    KSNODETYPE_EXTERNAL_UNDEFINED
)


STATIC_KSNODETYPE_ANALOG_CONNECTOR = DEFINE_USB_TERMINAL_GUID(0x601)
KSNODETYPE_ANALOG_CONNECTOR = DEFINE_GUIDSTRUCT(
    "DFF21FE1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_ANALOG_CONNECTOR = DEFINE_GUIDNAMED(
    KSNODETYPE_ANALOG_CONNECTOR
)


STATIC_KSNODETYPE_DIGITAL_AUDIO_INTERFACE = DEFINE_USB_TERMINAL_GUID(0x0602)
KSNODETYPE_DIGITAL_AUDIO_INTERFACE = DEFINE_GUIDSTRUCT(
    "DFF21FE2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DIGITAL_AUDIO_INTERFACE = DEFINE_GUIDNAMED(
    KSNODETYPE_DIGITAL_AUDIO_INTERFACE
)


STATIC_KSNODETYPE_LINE_CONNECTOR = DEFINE_USB_TERMINAL_GUID(0x0603)
KSNODETYPE_LINE_CONNECTOR = DEFINE_GUIDSTRUCT(
    "DFF21FE3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_LINE_CONNECTOR = DEFINE_GUIDNAMED(
    KSNODETYPE_LINE_CONNECTOR
)


STATIC_KSNODETYPE_LEGACY_AUDIO_CONNECTOR = DEFINE_USB_TERMINAL_GUID(0x0604)
KSNODETYPE_LEGACY_AUDIO_CONNECTOR = DEFINE_GUIDSTRUCT(
    "DFF21FE4-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_LEGACY_AUDIO_CONNECTOR = DEFINE_GUIDNAMED(
    KSNODETYPE_LEGACY_AUDIO_CONNECTOR
)


STATIC_KSNODETYPE_SPDIF_INTERFACE = DEFINE_USB_TERMINAL_GUID(0x0605)
KSNODETYPE_SPDIF_INTERFACE = DEFINE_GUIDSTRUCT(
    "DFF21FE5-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_SPDIF_INTERFACE = DEFINE_GUIDNAMED(
    KSNODETYPE_SPDIF_INTERFACE
)


STATIC_KSNODETYPE_1394_DA_STREAM = DEFINE_USB_TERMINAL_GUID(0x0606)
KSNODETYPE_1394_DA_STREAM = DEFINE_GUIDSTRUCT(
    "DFF21FE6-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_1394_DA_STREAM = DEFINE_GUIDNAMED(
    KSNODETYPE_1394_DA_STREAM
)


STATIC_KSNODETYPE_1394_DV_STREAM_SOUNDTRACK = DEFINE_USB_TERMINAL_GUID(0x0607)
KSNODETYPE_1394_DV_STREAM_SOUNDTRACK = DEFINE_GUIDSTRUCT(
    "DFF21FE7-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_1394_DV_STREAM_SOUNDTRACK = DEFINE_GUIDNAMED(
    KSNODETYPE_1394_DV_STREAM_SOUNDTRACK
)


STATIC_KSNODETYPE_EMBEDDED_UNDEFINED = DEFINE_USB_TERMINAL_GUID(0x0700)
KSNODETYPE_EMBEDDED_UNDEFINED = DEFINE_GUIDSTRUCT(
    "DFF220E0-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_EMBEDDED_UNDEFINED = DEFINE_GUIDNAMED(
    KSNODETYPE_EMBEDDED_UNDEFINED
)


STATIC_KSNODETYPE_LEVEL_CALIBRATION_NOISE_SOURCE = (
    DEFINE_USB_TERMINAL_GUID(0x0701)
)
KSNODETYPE_LEVEL_CALIBRATION_NOISE_SOURCE = DEFINE_GUIDSTRUCT(
    "DFF220E1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_LEVEL_CALIBRATION_NOISE_SOURCE = DEFINE_GUIDNAMED(
    KSNODETYPE_LEVEL_CALIBRATION_NOISE_SOURCE
)


STATIC_KSNODETYPE_EQUALIZATION_NOISE = DEFINE_USB_TERMINAL_GUID(0x0702)
KSNODETYPE_EQUALIZATION_NOISE = DEFINE_GUIDSTRUCT(
    "DFF220E2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_EQUALIZATION_NOISE = DEFINE_GUIDNAMED(
    KSNODETYPE_EQUALIZATION_NOISE
)


STATIC_KSNODETYPE_CD_PLAYER = DEFINE_USB_TERMINAL_GUID(0x0703)
KSNODETYPE_CD_PLAYER = DEFINE_GUIDSTRUCT(
    "DFF220E3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_CD_PLAYER = DEFINE_GUIDNAMED(
    KSNODETYPE_CD_PLAYER
)


STATIC_KSNODETYPE_DAT_IO_DIGITAL_AUDIO_TAPE = DEFINE_USB_TERMINAL_GUID(0x0704)
KSNODETYPE_DAT_IO_DIGITAL_AUDIO_TAPE = DEFINE_GUIDSTRUCT(
    "DFF220E4-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DAT_IO_DIGITAL_AUDIO_TAPE = DEFINE_GUIDNAMED(
    KSNODETYPE_DAT_IO_DIGITAL_AUDIO_TAPE
)


STATIC_KSNODETYPE_DCC_IO_DIGITAL_COMPACT_CASSETTE = (
    DEFINE_USB_TERMINAL_GUID(0x0705)
)
KSNODETYPE_DCC_IO_DIGITAL_COMPACT_CASSETTE = DEFINE_GUIDSTRUCT(
    "DFF220E5-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DCC_IO_DIGITAL_COMPACT_CASSETTE = DEFINE_GUIDNAMED(
    KSNODETYPE_DCC_IO_DIGITAL_COMPACT_CASSETTE
)


STATIC_KSNODETYPE_MINIDISK = DEFINE_USB_TERMINAL_GUID(0x0706)
KSNODETYPE_MINIDISK = DEFINE_GUIDSTRUCT(
    "DFF220E6-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_MINIDISK = DEFINE_GUIDNAMED(
    KSNODETYPE_MINIDISK
)


STATIC_KSNODETYPE_ANALOG_TAPE = DEFINE_USB_TERMINAL_GUID(0x0707)
KSNODETYPE_ANALOG_TAPE = DEFINE_GUIDSTRUCT(
    "DFF220E7-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_ANALOG_TAPE = DEFINE_GUIDNAMED(
    KSNODETYPE_ANALOG_TAPE
)


STATIC_KSNODETYPE_PHONOGRAPH = DEFINE_USB_TERMINAL_GUID(0x0708)
KSNODETYPE_PHONOGRAPH = DEFINE_GUIDSTRUCT(
    "DFF220E8-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_PHONOGRAPH = DEFINE_GUIDNAMED(
    KSNODETYPE_PHONOGRAPH
)


STATIC_KSNODETYPE_VCR_AUDIO = DEFINE_USB_TERMINAL_GUID(0x0708)
KSNODETYPE_VCR_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF220E9-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VCR_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_VCR_AUDIO
)


STATIC_KSNODETYPE_VIDEO_DISC_AUDIO = DEFINE_USB_TERMINAL_GUID(0x070A)
KSNODETYPE_VIDEO_DISC_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF220EA-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_DISC_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_DISC_AUDIO
)


STATIC_KSNODETYPE_DVD_AUDIO = DEFINE_USB_TERMINAL_GUID(0x070B)
KSNODETYPE_DVD_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF220EB-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DVD_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_DVD_AUDIO
)


STATIC_KSNODETYPE_TV_TUNER_AUDIO = DEFINE_USB_TERMINAL_GUID(0x070C)
KSNODETYPE_TV_TUNER_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF220EC-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_TV_TUNER_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_TV_TUNER_AUDIO
)


STATIC_KSNODETYPE_SATELLITE_RECEIVER_AUDIO = DEFINE_USB_TERMINAL_GUID(0x070D)
KSNODETYPE_SATELLITE_RECEIVER_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF220ED-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_SATELLITE_RECEIVER_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_SATELLITE_RECEIVER_AUDIO
)


STATIC_KSNODETYPE_CABLE_TUNER_AUDIO = DEFINE_USB_TERMINAL_GUID(0x070E)
KSNODETYPE_CABLE_TUNER_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF220EE-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_CABLE_TUNER_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_CABLE_TUNER_AUDIO
)


STATIC_KSNODETYPE_DSS_AUDIO = DEFINE_USB_TERMINAL_GUID(0x070F)
KSNODETYPE_DSS_AUDIO = DEFINE_GUIDSTRUCT(
    "DFF220EF-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_DSS_AUDIO = DEFINE_GUIDNAMED(
    KSNODETYPE_DSS_AUDIO
)


STATIC_KSNODETYPE_RADIO_RECEIVER = DEFINE_USB_TERMINAL_GUID(0x0710)
KSNODETYPE_RADIO_RECEIVER = DEFINE_GUIDSTRUCT(
    "DFF220F0-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_RADIO_RECEIVER = DEFINE_GUIDNAMED(
    KSNODETYPE_RADIO_RECEIVER
)


STATIC_KSNODETYPE_RADIO_TRANSMITTER = DEFINE_USB_TERMINAL_GUID(0x0711)
KSNODETYPE_RADIO_TRANSMITTER = DEFINE_GUIDSTRUCT(
    "DFF220F1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_RADIO_TRANSMITTER = DEFINE_GUIDNAMED(
    KSNODETYPE_RADIO_TRANSMITTER
)


STATIC_KSNODETYPE_MULTITRACK_RECORDER = DEFINE_USB_TERMINAL_GUID(0x0712)
KSNODETYPE_MULTITRACK_RECORDER = DEFINE_GUIDSTRUCT(
    "DFF220F2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_MULTITRACK_RECORDER = DEFINE_GUIDNAMED(
    KSNODETYPE_MULTITRACK_RECORDER
)


STATIC_KSNODETYPE_SYNTHESIZER = DEFINE_USB_TERMINAL_GUID(0x0713)
KSNODETYPE_SYNTHESIZER = DEFINE_GUIDSTRUCT(
    "DFF220F3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_SYNTHESIZER = DEFINE_GUIDNAMED(
    KSNODETYPE_SYNTHESIZER
)


STATIC_KSNODETYPE_HDMI_INTERFACE = (
    0xD1B9CC2A,
    0xF519,
    0x417F,
    0x91,
    0xC9,
    0x55,
    0xFA,
    0x65,
    0x48,
    0x10,
    0x01,
)
KSNODETYPE_HDMI_INTERFACE = DEFINE_GUIDSTRUCT(
    "D1B9CC2A-F519-417f-91C9-55FA65481001"
)
KSNODETYPE_HDMI_INTERFACE = DEFINE_GUIDNAMED(
    KSNODETYPE_HDMI_INTERFACE
)


STATIC_KSNODETYPE_DISPLAYPORT_INTERFACE = (
    0xE47E4031,
    0x3EA6,
    0x418D,
    0x8F,
    0x9B,
    0xB7,
    0x38,
    0x43,
    0xCC,
    0xBA,
    0x97,
)
KSNODETYPE_DISPLAYPORT_INTERFACE = DEFINE_GUIDSTRUCT(
    "E47E4031-3EA6-418d-8F9B-B73843CCBA97"
)
KSNODETYPE_DISPLAYPORT_INTERFACE = DEFINE_GUIDNAMED(
    KSNODETYPE_DISPLAYPORT_INTERFACE
)


STATIC_KSNODETYPE_AUDIO_LOOPBACK = (
    0x8F42C0B2,
    0x91CE,
    0x4BCF,
    0x9C,
    0xCD,
    0xE,
    0x59,
    0x90,
    0x37,
    0xAB,
    0x35,
)
KSNODETYPE_AUDIO_LOOPBACK = DEFINE_GUIDSTRUCT(
    "8F42C0B2-91CE-4BCF-9CCD-0E599037AB35"
)
KSNODETYPE_AUDIO_LOOPBACK = DEFINE_GUIDNAMED(
    KSNODETYPE_AUDIO_LOOPBACK
)


STATIC_KSNODETYPE_AUDIO_KEYWORDDETECTOR = (
    0x3817E0B8,
    0xDF58,
    0x4375,
    0xB6,
    0x69,
    0xC4,
    0x96,
    0x34,
    0x33,
    0x1F,
    0x9D,
)
KSNODETYPE_AUDIO_KEYWORDDETECTOR = DEFINE_GUIDSTRUCT(
    "3817E0B8-DF58-4375-B669-C49634331F9D"
)
KSNODETYPE_AUDIO_KEYWORDDETECTOR = DEFINE_GUIDNAMED(
    KSNODETYPE_AUDIO_KEYWORDDETECTOR
)


STATIC_KSNODETYPE_MIDI_JACK = (
    0x265E0C3F,
    0xFA39,
    0x4DF3,
    0xAB,
    0x04,
    0xBE,
    0x01,
    0xB9,
    0x1E,
    0x29,
    0x9A,
)
KSNODETYPE_MIDI_JACK = DEFINE_GUIDSTRUCT(
    "265E0C3F-FA39-4df3-AB04-BE01B91E299A"
)
KSNODETYPE_MIDI_JACK = DEFINE_GUIDNAMED(
    KSNODETYPE_MIDI_JACK
)


STATIC_KSNODETYPE_MIDI_ELEMENT = (
    0x01C6FE66,
    0x6E48,
    0x4C65,
    0xAC,
    0x9B,
    0x52,
    0xDB,
    0x5D,
    0x65,
    0x6C,
    0x7E,
)
KSNODETYPE_MIDI_ELEMENT = DEFINE_GUIDSTRUCT(
    "01C6FE66-6E48-4c65-AC9B-52DB5D656C7E"
)
KSNODETYPE_MIDI_ELEMENT = DEFINE_GUIDNAMED(
    KSNODETYPE_MIDI_ELEMENT
)


STATIC_KSNODETYPE_AUDIO_ENGINE = (
    0x35CAF6E4,
    0xF3B3,
    0x4168,
    0xBB,
    0x4B,
    0x55,
    0xE7,
    0x7A,
    0x46,
    0x1C,
    0x7E,
)
KSNODETYPE_AUDIO_ENGINE = DEFINE_GUIDSTRUCT(
    "35CAF6E4-F3B3-4168-BB4B-55E77A461C7E"
)
KSNODETYPE_AUDIO_ENGINE = DEFINE_GUIDNAMED(
    KSNODETYPE_AUDIO_ENGINE
)


STATIC_KSNODETYPE_SPEAKERS_STATIC_JACK = (
    0x28E04F87,
    0x4DBE,
    0x4F8D,
    0x85,
    0x89,
    0x2,
    0x5D,
    0x20,
    0x9D,
    0xFB,
    0x4A,
)
KSNODETYPE_SPEAKERS_STATIC_JACK = DEFINE_GUIDSTRUCT(
    "28E04F87-4DBE-4f8d-8589-025D209DFB4A"
)
KSNODETYPE_SPEAKERS_STATIC_JACK = DEFINE_GUIDNAMED(
    KSNODETYPE_SPEAKERS_STATIC_JACK
)


STATIC_KSNODETYPE_SWSYNTH = (
    0x423274A0,
    0x8B81,
    0x11D1,
    0xA0,
    0x50,
    0x00,
    0x00,
    0xF8,
    0x00,
    0x47,
    0x88,
)
KSNODETYPE_SWSYNTH = DEFINE_GUIDSTRUCT(
    "423274A0-8B81-11D1-A050-0000F8004788"
)
KSNODETYPE_SWSYNTH = DEFINE_GUIDNAMED(
    KSNODETYPE_SWSYNTH
)


STATIC_KSNODETYPE_SWMIDI = (
    0xCB9BEFA0,
    0xA251,
    0x11D1,
    0xA0,
    0x50,
    0x00,
    0x00,
    0xF8,
    0x00,
    0x47,
    0x88,
)
KSNODETYPE_SWMIDI = DEFINE_GUIDSTRUCT(
    "CB9BEFA0-A251-11D1-A050-0000F8004788"
)
KSNODETYPE_SWMIDI = DEFINE_GUIDNAMED(
    KSNODETYPE_SWMIDI
)


STATIC_KSNODETYPE_DRM_DESCRAMBLE = (
    0xFFBB6E3F,
    0xCCFE,
    0x4D84,
    0x90,
    0xD9,
    0x42,
    0x14,
    0x18,
    0xB0,
    0x3A,
    0x8E,
)
KSNODETYPE_DRM_DESCRAMBLE = DEFINE_GUIDSTRUCT(
    "FFBB6E3F-CCFE-4D84-90D9-421418B03A8E"
)
KSNODETYPE_DRM_DESCRAMBLE = DEFINE_GUIDNAMED(
    KSNODETYPE_DRM_DESCRAMBLE
)


STATIC_KSNODETYPE_TELEPHONY_BIDI = (
    0x686D7CC0,
    0xD903,
    0x4258,
    0xB4,
    0x43,
    0x3A,
    0x3D,
    0x35,
    0x80,
    0x74,
    0x1C,
)
KSNODETYPE_TELEPHONY_BIDI = DEFINE_GUIDSTRUCT(
    "686D7CC0-D903-4258-B443-3A3D3580741C"
)
KSNODETYPE_TELEPHONY_BIDI = DEFINE_GUIDNAMED(
    KSNODETYPE_TELEPHONY_BIDI
)


STATIC_KSNODETYPE_FM_RX = (
    0x834A733C,
    0xF485,
    0x41C0,
    0xA6,
    0x2B,
    0x51,
    0x30,
    0x25,
    0x1,
    0x4E,
    0x40,
)
KSNODETYPE_FM_RX = DEFINE_GUIDSTRUCT(
    "834A733C-F485-41C0-A62B-513025014E40"
)
KSNODETYPE_FM_RX = DEFINE_GUIDNAMED(
    KSNODETYPE_FM_RX
)


STATIC_KSNODETYPE_DAC = (
    0x507AE360,
    0xC554,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_DAC = DEFINE_GUIDSTRUCT(
    "507AE360-C554-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_DAC = DEFINE_GUIDNAMED(
    KSNODETYPE_DAC
)


STATIC_KSNODETYPE_ADC = (
    0x4D837FE0,
    0xC555,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_ADC = DEFINE_GUIDSTRUCT(
    "4D837FE0-C555-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_ADC = DEFINE_GUIDNAMED(
    KSNODETYPE_ADC
)


STATIC_KSNODETYPE_SRC = (
    0x9DB7B9E0,
    0xC555,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_SRC = DEFINE_GUIDSTRUCT(
    "9DB7B9E0-C555-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_SRC = DEFINE_GUIDNAMED(
    KSNODETYPE_SRC
)


STATIC_KSNODETYPE_SUPERMIX = (
    0xE573ADC0,
    0xC555,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_SUPERMIX = DEFINE_GUIDSTRUCT(
    "E573ADC0-C555-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_SUPERMIX = DEFINE_GUIDNAMED(
    KSNODETYPE_SUPERMIX
)


STATIC_KSNODETYPE_MUX = (
    0x2CEAF780,
    0xC556,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_MUX = DEFINE_GUIDSTRUCT(
    "2CEAF780-C556-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_MUX = DEFINE_GUIDNAMED(
    KSNODETYPE_MUX
)


STATIC_KSNODETYPE_DEMUX = (
    0xC0EB67D4,
    0xE807,
    0x11D0,
    0x95,
    0x8A,
    0x00,
    0xC0,
    0x4F,
    0xB9,
    0x25,
    0xD3,
)
KSNODETYPE_DEMUX = DEFINE_GUIDSTRUCT(
    "C0EB67D4-E807-11D0-958A-00C04FB925D3"
)
KSNODETYPE_DEMUX = DEFINE_GUIDNAMED(
    KSNODETYPE_DEMUX
)


STATIC_KSNODETYPE_SUM = (
    0xDA441A60,
    0xC556,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_SUM = DEFINE_GUIDSTRUCT(
    "DA441A60-C556-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_SUM = DEFINE_GUIDNAMED(
    KSNODETYPE_SUM
)


STATIC_KSNODETYPE_MUTE = (
    0x02B223C0,
    0xC557,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_MUTE = DEFINE_GUIDSTRUCT(
    "02B223C0-C557-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_MUTE = DEFINE_GUIDNAMED(
    KSNODETYPE_MUTE
)


STATIC_KSNODETYPE_VOLUME = (
    0x3A5ACC00,
    0xC557,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_VOLUME = DEFINE_GUIDSTRUCT(
    "3A5ACC00-C557-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_VOLUME = DEFINE_GUIDNAMED(
    KSNODETYPE_VOLUME
)


STATIC_KSNODETYPE_TONE = (
    0x7607E580,
    0xC557,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_TONE = DEFINE_GUIDSTRUCT(
    "7607E580-C557-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_TONE = DEFINE_GUIDNAMED(
    KSNODETYPE_TONE
)


STATIC_KSNODETYPE_EQUALIZER = (
    0x9D41B4A0,
    0xC557,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_EQUALIZER = DEFINE_GUIDSTRUCT(
    "9D41B4A0-C557-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_EQUALIZER = DEFINE_GUIDNAMED(
    KSNODETYPE_EQUALIZER
)


STATIC_KSNODETYPE_AGC = (
    0xE88C9BA0,
    0xC557,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_AGC = DEFINE_GUIDSTRUCT(
    "E88C9BA0-C557-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_AGC = DEFINE_GUIDNAMED(
    KSNODETYPE_AGC
)


STATIC_KSNODETYPE_NOISE_SUPPRESS = (
    0xE07F903F,
    0x62FD,
    0x4E60,
    0x8C,
    0xDD,
    0xDE,
    0xA7,
    0x23,
    0x66,
    0x65,
    0xB5,
)
KSNODETYPE_NOISE_SUPPRESS = DEFINE_GUIDSTRUCT(
    "E07F903F-62FD-4e60-8CDD-DEA7236665B5"
)
KSNODETYPE_NOISE_SUPPRESS = DEFINE_GUIDNAMED(
    KSNODETYPE_NOISE_SUPPRESS
)


STATIC_KSNODETYPE_DELAY = (
    0x144981E0,
    0xC558,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_DELAY = DEFINE_GUIDSTRUCT(
    "144981E0-C558-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_DELAY = DEFINE_GUIDNAMED(
    KSNODETYPE_DELAY
)


STATIC_KSNODETYPE_LOUDNESS = (
    0x41887440,
    0xC558,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_LOUDNESS = DEFINE_GUIDSTRUCT(
    "41887440-C558-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_LOUDNESS = DEFINE_GUIDNAMED(
    KSNODETYPE_LOUDNESS
)


STATIC_KSNODETYPE_PROLOGIC_DECODER = (
    0x831C2C80,
    0xC558,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_PROLOGIC_DECODER = DEFINE_GUIDSTRUCT(
    "831C2C80-C558-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_PROLOGIC_DECODER = DEFINE_GUIDNAMED(
    KSNODETYPE_PROLOGIC_DECODER
)


STATIC_KSNODETYPE_STEREO_WIDE = (
    0xA9E69800,
    0xC558,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_STEREO_WIDE = DEFINE_GUIDSTRUCT(
    "A9E69800-C558-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_STEREO_WIDE = DEFINE_GUIDNAMED(
    KSNODETYPE_STEREO_WIDE
)


STATIC_KSNODETYPE_REVERB = (
    0xEF0328E0,
    0xC558,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_REVERB = DEFINE_GUIDSTRUCT(
    "EF0328E0-C558-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_REVERB = DEFINE_GUIDNAMED(
    KSNODETYPE_REVERB
)


STATIC_KSNODETYPE_CHORUS = (
    0x20173F20,
    0xC559,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_CHORUS = DEFINE_GUIDSTRUCT(
    "20173F20-C559-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_CHORUS = DEFINE_GUIDNAMED(
    KSNODETYPE_CHORUS
)


STATIC_KSNODETYPE_3D_EFFECTS = (
    0x55515860,
    0xC559,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_3D_EFFECTS = DEFINE_GUIDSTRUCT(
    "55515860-C559-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_3D_EFFECTS = DEFINE_GUIDNAMED(
    KSNODETYPE_3D_EFFECTS
)


STATIC_KSNODETYPE_PARAMETRIC_EQUALIZER = (
    0x19BB3A6A,
    0xCE2B,
    0x4442,
    0x87,
    0xEC,
    0x67,
    0x27,
    0xC3,
    0xCA,
    0xB4,
    0x77,
)
KSNODETYPE_PARAMETRIC_EQUALIZER = DEFINE_GUIDSTRUCT(
    "19BB3A6A-CE2B-4442-87EC-6727C3CAB477"
)
KSNODETYPE_PARAMETRIC_EQUALIZER = DEFINE_GUIDNAMED(
    KSNODETYPE_PARAMETRIC_EQUALIZER
)


STATIC_KSNODETYPE_UPDOWN_MIX = (
    0xB7EDC5CF,
    0x7B63,
    0x4EE2,
    0xA1,
    0x0,
    0x29,
    0xEE,
    0x2C,
    0xB6,
    0xB2,
    0xDE,
)
KSNODETYPE_UPDOWN_MIX = DEFINE_GUIDSTRUCT(
    "B7EDC5CF-7B63-4ee2-A100-29EE2CB6B2DE"
)
KSNODETYPE_UPDOWN_MIX = DEFINE_GUIDNAMED(
    KSNODETYPE_UPDOWN_MIX
)


STATIC_KSNODETYPE_DYN_RANGE_COMPRESSOR = (
    0x8C8A6A8,
    0x601F,
    0x4AF8,
    0x87,
    0x93,
    0xD9,
    0x5,
    0xFF,
    0x4C,
    0xA9,
    0x7D,
)
KSNODETYPE_DYN_RANGE_COMPRESSOR = DEFINE_GUIDSTRUCT(
    "08C8A6A8-601F-4af8-8793-D905FF4CA97D"
)
KSNODETYPE_DYN_RANGE_COMPRESSOR = DEFINE_GUIDNAMED(
    KSNODETYPE_DYN_RANGE_COMPRESSOR
)


STATIC_KSNODETYPE_ACOUSTIC_ECHO_CANCEL = STATIC_KSCATEGORY_ACOUSTIC_ECHO_CANCEL
KSNODETYPE_ACOUSTIC_ECHO_CANCEL = KSCATEGORY_ACOUSTIC_ECHO_CANCEL


STATIC_KSNODETYPE_MICROPHONE_ARRAY_PROCESSOR = (
    STATIC_KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR
)
KSNODETYPE_MICROPHONE_ARRAY_PROCESSOR = KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR


STATIC_KSNODETYPE_DEV_SPECIFIC = (
    0x941C7AC0,
    0xC559,
    0x11D0,
    0x8A,
    0x2B,
    0x00,
    0xA0,
    0xC9,
    0x25,
    0x5A,
    0xC1,
)
KSNODETYPE_DEV_SPECIFIC = DEFINE_GUIDSTRUCT(
    "941C7AC0-C559-11D0-8A2B-00A0C9255AC1"
)
KSNODETYPE_DEV_SPECIFIC = DEFINE_GUIDNAMED(
    KSNODETYPE_DEV_SPECIFIC
)


STATIC_KSNODETYPE_PROLOGIC_ENCODER = (
    0x8074C5B2,
    0x3C66,
    0x11D2,
    0xB4,
    0x5A,
    0x30,
    0x78,
    0x30,
    0x2C,
    0x20,
    0x30,
)
KSNODETYPE_PROLOGIC_ENCODER = DEFINE_GUIDSTRUCT(
    "8074C5B2-3C66-11D2-B45A-3078302C2030"
)
KSNODETYPE_PROLOGIC_ENCODER = DEFINE_GUIDNAMED(
    KSNODETYPE_PROLOGIC_ENCODER
)


STATIC_KSNODETYPE_PEAKMETER = (
    0xA085651E,
    0x5F0D,
    0x4B36,
    0xA8,
    0x69,
    0xD1,
    0x95,
    0xD6,
    0xAB,
    0x4B,
    0x9E,
)
KSNODETYPE_PEAKMETER = DEFINE_GUIDSTRUCT(
    "A085651E-5F0D-4b36-A869-D195D6AB4B9E"
)
KSNODETYPE_PEAKMETER = DEFINE_GUIDNAMED(
    KSNODETYPE_PEAKMETER
)


STATIC_KSNODETYPE_SURROUND_ENCODER = (
    0x8074C5B2,
    0x3C66,
    0x11D2,
    0xB4,
    0x5A,
    0x30,
    0x78,
    0x30,
    0x2C,
    0x20,
    0x30,
)
KSNODETYPE_SURROUND_ENCODER = DEFINE_GUIDSTRUCT(
    "8074C5B2-3C66-11D2-B45A-3078302C2030"
)
KSNODETYPE_SURROUND_ENCODER = DEFINE_GUIDNAMED(
    KSNODETYPE_SURROUND_ENCODER
)


STATIC_KSNODETYPE_VIDEO_STREAMING = (
    0xDFF229E1,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_STREAMING = DEFINE_GUIDSTRUCT(
    "DFF229E1-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_STREAMING = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_STREAMING
)


STATIC_KSNODETYPE_VIDEO_INPUT_TERMINAL = (
    0xDFF229E2,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_INPUT_TERMINAL = DEFINE_GUIDSTRUCT(
    "DFF229E2-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_INPUT_TERMINAL = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_INPUT_TERMINAL
)


STATIC_KSNODETYPE_VIDEO_OUTPUT_TERMINAL = (
    0xDFF229E3,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_OUTPUT_TERMINAL = DEFINE_GUIDSTRUCT(
    "DFF229E3-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_OUTPUT_TERMINAL = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_OUTPUT_TERMINAL
)


STATIC_KSNODETYPE_VIDEO_SELECTOR = (
    0xDFF229E4,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_SELECTOR = DEFINE_GUIDSTRUCT(
    "DFF229E4-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_SELECTOR = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_SELECTOR
)


STATIC_KSNODETYPE_VIDEO_PROCESSING = (
    0xDFF229E5,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_PROCESSING = DEFINE_GUIDSTRUCT(
    "DFF229E5-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_PROCESSING = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_PROCESSING
)


STATIC_KSNODETYPE_VIDEO_CAMERA_TERMINAL = (
    0xDFF229E6,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_CAMERA_TERMINAL = DEFINE_GUIDSTRUCT(
    "DFF229E6-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_CAMERA_TERMINAL = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_CAMERA_TERMINAL
)


STATIC_KSNODETYPE_VIDEO_INPUT_MTT = (
    0xDFF229E7,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_INPUT_MTT = DEFINE_GUIDSTRUCT(
    "DFF229E7-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_INPUT_MTT = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_INPUT_MTT
)


STATIC_KSNODETYPE_VIDEO_OUTPUT_MTT = (
    0xDFF229E8,
    0xF70F,
    0x11D0,
    0xB9,
    0x17,
    0x00,
    0xA0,
    0xC9,
    0x22,
    0x31,
    0x96,
)
KSNODETYPE_VIDEO_OUTPUT_MTT = DEFINE_GUIDSTRUCT(
    "DFF229E8-F70F-11D0-B917-00A0C9223196"
)
KSNODETYPE_VIDEO_OUTPUT_MTT = DEFINE_GUIDNAMED(
    KSNODETYPE_VIDEO_OUTPUT_MTT
)


STATIC_KSCATEGORY_SYNTHESIZER = STATIC_KSNODETYPE_SYNTHESIZER
KSCATEGORY_SYNTHESIZER = KSNODETYPE_SYNTHESIZER


STATIC_KSCATEGORY_DRM_DESCRAMBLE = STATIC_KSNODETYPE_DRM_DESCRAMBLE
KSCATEGORY_DRM_DESCRAMBLE = KSNODETYPE_DRM_DESCRAMBLE


__all__ = (
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_MPEG3',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_MPEG2',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_MPEG1',
    'STATIC_KSNODETYPE_AUDIO_KEYWORDDETECTOR','KSMICARRAY_MICARRAYTYPE',
    'KSEVENTSETID_EXTDEV_Command','KS_VBISAMPLINGRATE_47X_NABTS',
    'KS_VBI_FLAG_VBIINFOHEADER_CHANGE',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_SPORT','KSAC3_ALTERNATE_AUDIO_1',
    'KSCAMERA_EXTENDEDPROP_FLASH_AUTO_ADJUSTABLEPOWER',
    'STATIC_KSPROPSETID_TSRateChange','STATIC_KSAUDFNAME_MIDI_VOLUME',
    'KSDS3D_ITD_PARAMS_MSG','KS_iRED','KSNODETYPE_SUPERMIX',
    'KSPROPERTY_SELECTOR_S','KSDATAFORMAT_SPECIFIER_VIDEOINFO',
    'KSRTAUDIO_BUFFER_PROPERTY32','KSPROPERTY_TUNER_STANDARD_MODE_S',
    'KSPROPERTY_VIDCAP_TVAUDIO',
    'STATIC_PROPSETID_VIDCAP_CAMERACONTROL_IMAGE_PIN_CAPABILITY',
    'STATIC_KSPROPSETID_VPVBIConfig',
    'KSCAMERA_EXTENDEDPROP_VIDEOTORCH_OFF','KSWAVE_COMPATCAPS_OUTPUT',
    'STATIC_KSCATEGORY_WDMAUD','_VBICODECFILTERING_STATISTICS_NABTS_PIN',
    'KSNODETYPE_1394_DA_STREAM',
    'STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO','KS_VIDEO_FLAG_FRAME',
    'STATIC_KSDATAFORMAT_SUBTYPE_Line21_BytePair','_KSCAMERA_PROFILE_INFO',
    'tagKSCAMERA_EXTENDEDPROP_ROI_INFO','ANYSIZE_ARRAY',
    'STATIC_KSNODETYPE_SWMIDI','STATIC_KSNODETYPE_VIDEO_CAMERA_TERMINAL',
    'STATIC_KSDATAFORMAT_SUBTYPE_MULAW','KSAC3_BIT_STREAM_MODE',
    'KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_8X',
    'KS_NABTS_GROUPID_TELEVISION_STATION_ADVERTISER_BASE',
    'KS_TUNER_STRATEGY',
    'KSCAMERA_EXTENDEDPROP_VIDEOTORCH_ON_ADJUSTABLEPOWER',
    'KSCAMERA_EXTENDEDPROP_VFR_ON',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_ONE_BIT_AUDIO',
    'KS_AM_UseNewCSSKey','KSNODETYPE_MULTITRACK_RECORDER',
    'KSAUDIO_STEREO_SPEAKER_GEOMETRY_MIN','STATIC_EVENTSETID_VIDEODECODER',
    'STATIC_KSEVENTSETID_VIDCAPTOSTI',
    'KSCAMERA_EXTENDEDPROP_FOCUS_DRIVERFALLBACK_OFF',
    'KSALGORITHMINSTANCE_SYSTEM_AGC','KSPROPERTY_AUDDECOUT',
    'SPEAKER_FRONT_LEFT','KSNODETYPE_SWSYNTH',
    'JACKDESC2_DYNAMIC_FORMAT_CHANGE_CAPABILITY',
    'STATIC_KSPROPSETID_TelephonyControl',
    'KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE',
    'KSCAMERA_EXTENDEDPROP_FACEDETECTION_BLINK','KSMULTIPLE_DATA_PROP',
    'KSPROPERTY_VBICODECFILTERING_STATISTICS_CC_PIN_S',
    'KSNODETYPE_ACOUSTIC_ECHO_CANCEL',
    'KSNODETYPE_MICROPHONE_ARRAY_PROCESSOR','KSPROPERTY_LINEAR',
    'KSNOTIFICATIONID_AudioModule','STATIC_KSCAMERAPROFILE_Legacy',
    'KSDATAFORMAT_TYPE_MUSIC','KSDATAFORMAT_TYPE_MPEG2_PROGRAM',
    'STATIC_PINNAME_VIDEO_CAPTURE',
    'KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUSLOCK',
    'STATIC_KSNODETYPE_EMBEDDED_UNDEFINED','KSCATEGORY_SYNTHESIZER',
    'ENCAPIPARAM_PEAK_BITRATE','KSPROPSETID_AC3',
    'KSNODETYPE_ECHO_SUPPRESSING_SPEAKERPHONE',
    'STATIC_KSDATAFORMAT_SUBTYPE_MPEGLAYER3','KSNODETYPE_INPUT_UNDEFINED',
    'KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO','KSVPMAXPIXELRATE',
    'KSDATAFORMAT_SPECIFIER_WAVEFORMATEX',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_SNOW',
    'KSNODETYPE_SPEAKERS_STATIC_JACK',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT21',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT20',
    'STATIC_KSDATAFORMAT_TYPE_MPEG2_PROGRAM','KSPROPSETID_FMRXTopology',
    'KSPROPERTY_AUDIOENGINE','STATIC_PROPSETID_VIDCAP_VIDEODECODER',
    'STATIC_EVENTSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST',
    'KSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_PIN_S','_KS_DVD_YCrCb',
    'KSPROPERTY_VIDCAP_VIDEOCOMPRESSION','STATIC_KSEVENTSETID_Telephony',
    'STATIC_KSNODETYPE_HEAD_MOUNTED_DISPLAY_AUDIO',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONVERGEMODE',
    'STATIC_KSNODETYPE_VIDEO_DISC_AUDIO','KSDATAFORMAT_SUBTYPE_ALAW',
    'STATIC_KSPROPSETID_Mpeg2Vid','KSAUDFNAME_WAVE_MUTE',
    'KSAUDFNAME_MIC_IN_VOLUME','tagKSCAMERA_METADATA_PHOTOCONFIRMATION',
    'KSAUDIO_SPEAKER_GROUND_REAR_LEFT','PINNAME_VIDEO_CC',
    'KS_AnalogVideoStandard','STATIC_KSNODETYPE_SURROUND_ENCODER',
    'KSEVENT_DYNAMICFORMATCHANGE','STATIC_KSPROPSETID_RtAudio',
    'KSDATAFORMAT_SUBTYPE_STANDARD_AC3_AUDIO',
    'STATIC_KSNODETYPE_AUDIO_ENGINE',
    'KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO','KSAUDIO_SPEAKER_5POINT0',
    'STATIC_KSEVENTSETID_AudioControlChange','tagKS_AMVPDATAINFO',
    'KSCAMERA_EXTENDEDPROP_FOCUS_UNLOCK',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS',
    'STATIC_KSEVENTSETID_VPNotify',
    'KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO',
    'KSCAMERA_EXTENDEDPROP_FACEDETECTION_SMILE','KSEVENT_DEVCMD',
    '_KS_DVDCOPY_REGION','KSPROPERTY_HRTF3D','_WST_BUFFER_LINE',
    '_tagKSTOPOLOGY_ENDPOINTIDPAIR','STATIC_KSNODETYPE_PHONOGRAPH',
    'KSPROPERTY_MPEG4_MEDIATYPE_ATTRIBUTES','DDVPTYPE_E_HREFL_VREFL',
    'KSCATEGORY_TVTUNER','CLSID_KsIBasicAudioInterfaceHandler',
    'KSNODETYPE_AUDIO_LOOPBACK','KSNODEPIN_DEMUX_OUT',
    'KS_TVAUDIO_MODE_MONO','KSPROPERTY_VIDCAP_VIDEOCONTROL',
    'KSCAMERA_EXTENDEDPROP_OIS_ON','KSDATAFORMAT_SUBTYPE_CC',
    'KSWAVE_BUFFER','KSAUDFNAME_CD_AUDIO','KSDSOUND_3D_MODE_HEADRELATIVE',
    'KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_EXCLUSIVE_WITH_RECORD',
    'KSCAMERA_PERFRAMESETTING_CAP_HEADER','tagKS_VBI_FRAME_INFO',
    'TELEPHONY_CALLCONTROLOP','STATIC_KSDATAFORMAT_SPECIFIER_MPEG2_VIDEO',
    'STATIC_KSEVENTSETID_ExtendedCameraControl',
    'STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_VIDEO',
    'KSAUDIO_SPEAKER_7POINT1','KSAUDIO_SPEAKER_7POINT0','KSNODEPROPERTY',
    'KSDATAFORMAT_SUBTYPE_WMAUDIO2','KSDATAFORMAT_SUBTYPE_WMAUDIO3',
    'KSDSOUND_BUFFER_LOCSOFTWARE',
    'STATIC_AUDIO_SIGNALPROCESSINGMODE_SPEECH','KSPROPERTY_VPCONFIG',
    'INIT_USBAUDIO_PRODUCT_NAME','KSNODETYPE_VIDEO_STREAMING',
    'STATIC_KSPROPSETID_TopologyNode','KS_AnalogVideo_PAL_Mask',
    'KSDATAFORMAT_SUBTYPE_IEC61937_ONE_BIT_AUDIO',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_LENSPOSITION',
    'KSNODETYPE_VIDEO_OUTPUT_TERMINAL','KSDATAFORMAT_SUBTYPE_RIFFWAVE',
    'tagKS_AnalogVideoInfo','KSCAMERA_EXTENDEDPROP_FACEDETECTION_PREVIEW',
    'KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION',
    'PROPSETID_VIDCAP_SELECTOR','KSPROPSETID_VramCapture',
    'KSPROPSETID_Bibliographic','STATIC_KSAUDFNAME_AUX_MUTE',
    'KSCameraProfileSensorType_Infrared','PROPSETID_VIDCAP_TVAUDIO',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S',
    'KSAUDFNAME_CD_MUTE','KSMETHOD_WAVETABLE','KSPROPERTY_JACK',
    'PINNAME_VIDEO_ANALOGVIDEOIN','AEC_STATUS_FD_CURRENTLY_CONVERGED',
    'KSAUDIO_CPU_RESOURCES_NOT_HOST_CPU','KS_INTERLACE_UNUSED',
    'KSCAMERAPROFILE_FLAGS_PHOTOHDR','KSDATAFORMAT_TYPE_VBI',
    'KSEVENTSETID_Sysaudio','DEFINE_MMREG_MID_GUID',
    'KSCAMERAPROFILE_FaceAuth_Mode','STATIC_KSPROPSETID_VramCapture',
    'KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S',
    'KSPROPERTY_CAMERACONTROL_EXTENDED_PROPERTY',
    'STATIC_KSDATAFORMAT_SUBTYPE_MIDI_BUS','KSPROPERTY_SELECTOR_NODE_S',
    'KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_OFF','KSCATEGORY_WDMAUD',
    'SECURE_BUFFER_INFO','KSAC3_ALTERNATE_AUDIO_BOTH',
    'KS_INTERLACE_DisplayModeBobOrWeave',
    'AUDIO_EFFECT_TYPE_CONSTANT_TONE_REMOVAL','KSDS3D_HRTF_FILTER_QUALITY',
    'KSPROPSETID_Audio','tagKS_DATAFORMAT_VIDEOINFOHEADER',
    'KSPROPERTY_CAMERACONTROL_FLASH_S','STATIC_PINNAME_VIDEO_CC',
    'KS_INTERLACE_Field1First','KSAC3_ERROR_CONCEALMENT',
    'STATIC_KSDATAFORMAT_TYPE_VIDEO','KSAUDIO_COPY_PROTECTION',
    'STATIC_KSNODETYPE_DELAY','KS_AnalogVideo_NTSC_Mask',
    'STATIC_PROPSETID_VIDCAP_VIDEOCOMPRESSION',
    'KSEVENTSETID_DynamicFormatChange','KSRTAUDIO_HWREGISTER_PROPERTY',
    'KSAC3_ALTERNATE_AUDIO','KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_INFINITY',
    'STATIC_KSPROPSETID_AudioGfx','KSDATAFORMAT_SUBTYPE_IEC61937_MPEG1',
    'KSPROPSETID_VBICodecFiltering','KSDATAFORMAT_SUBTYPE_IEC61937_MPEG3',
    'KSDATAFORMAT_SUBTYPE_IEC61937_MPEG2','KSCATEGORY_TOPOLOGY',
    'WST_TVTUNER_CHANGE_BEGIN_TUNE','KSPROPSETID_TopologyNode',
    'KSPROPSETID_Wave','KSCATEGORY_VIDEO','PKSPROPERTY_COMPOSIT_ON',
    'KSPROPERTY_TIMECODE_S','MAX_SINK_DESCRIPTION_NAME_LENGTH',
    'SPEAKER_TOP_FRONT_LEFT','KSDS3D_BUFFER_ALL',
    'STATIC_KSNODETYPE_LOUDNESS','STATIC_KSAUDFNAME_MASTER_MUTE',
    'KSPROPERTY_VIDCAP_SELECTOR','STATIC_KSAUDFNAME_AUX_VOLUME',
    'STATIC_KSDATAFORMAT_SPECIFIER_VIDEOINFO2',
    'STATIC_KSDATAFORMAT_TYPE_AUDIO',
    'KSPROPERTY_VBICODECFILTERING_STATISTICS_NABTS_S',
    'KSPROPERTY_CAMERACONTROL_S','STATIC_KSAUDFNAME_MIDI_IN_VOLUME',
    'KS_CC_SUBSTREAM_FIELD1_MASK',
    'KSPROPERTY_VBICODECFILTERING_NABTS_SUBSTREAMS_S',
    'KSNODETYPE_STEREO_WIDE','KS_INTERLACE_FieldPatBothRegular',
    'STATIC_KSNODETYPE_VOLUME','KSCATEGORY_AUDIO',
    'STATIC_KSPROPERTYSETID_PerFrameSettingControl',
    'KSNODETYPE_COMMUNICATION_SPEAKER','KSAUDFNAME_LINE_IN_VOLUME',
    'KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MASK',
    'STATIC_KSDATAFORMAT_SUBTYPE_VPVideo',
    'KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_MACRO',
    'KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S',
    'KSEVENTSETID_Cyclic','STATIC_PROPSETID_TUNER',
    'KSPROPERTY_VBICODECFILTERING_SCANLINES_S','KS_VBIDATARATE_NABTS',
    'tagDEVCAPS','KSPROPSETID_WaveTable','KSWAVE_COMPATCAPS_INPUT',
    'KSNODETYPE_VIDEO_OUTPUT_MTT',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_EXPOSURECOMPENSATION',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEEE_FLOAT',
    'KSCAMERAPROFILE_BalancedVideoAndPhoto','STATIC_KSNODETYPE_PHONE_LINE',
    'tagKSCAMERA_EXTENDEDPROP_EVCOMPENSATION','KSAUDFNAME_VIDEO_MUTE',
    '_KSGOP_USERDATA','KSDATAFORMAT_SUBTYPE_WAVEFORMATEX',
    'KSPROPERTY_WAVETABLE',
    'STATIC_AUDIO_EFFECT_TYPE_DYNAMIC_RANGE_COMPRESSION',
    'KSAUDFNAME_STEREO_MIX_VOLUME','KSDATAFORMAT_TYPE_AUDIO',
    'STATIC_KSPROPSETID_AC3','STATIC_KSNODETYPE_HDMI_INTERFACE',
    'KSAUDIO_MIXCAP_TABLE','KS_DVD_COPYRIGHTED',
    'KSNODETYPE_SPEAKERPHONE_NO_ECHO_REDUCTION',
    'KSAUDIO_SPEAKER_TOP_MIDDLE','STATIC_KSNODETYPE_VIDEO_PROCESSING',
    'KS_MPEGAUDIOINFO_27MhzTimebase','STATIC_KSAUDFNAME_AUX',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_ZOOMFACTOR',
    'KS_NABTS_GROUPID_ORIGINAL_CONTENT_ADVERTISER_BASE',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_EXPOSURE',
    '_DS3DVECTOR','KS_MPEG1_SEQUENCE_INFO',
    'KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_MASK',
    'KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_ON',
    'STATIC_AUDIO_EFFECT_TYPE_BEAMFORMING',
    'STATIC_KSDATAFORMAT_SUBTYPE_MPEG_HEAAC',
    'STATIC_KSCAMERAPROFILE_VariablePhotoSequence',
    'KSMUSIC_TECHNOLOGY_SQSYNTH','KSAUDDECOUTMODE_PCM_51',
    'STATIC_KSNODETYPE_1394_DA_STREAM',
    'KSCAMERA_EXTENDEDPROP_FOCUS_CONTINUOUS',
    'KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE_S',
    'KSPROPERTY_FMRX_TOPOLOGY','STATIC_KSNODETYPE_PROLOGIC_ENCODER',
    'tagKSCAMERA_EXTENDEDPROP_ROI_FOCUS','tagTRANSPORTAUDIOPARMS',
    'STATIC_KSNOTIFICATIONID_AudioModule',
    'STATIC_KSDATAFORMAT_SUBTYPE_L16_CUSTOM',
    'STATIC_KSNODETYPE_ECHO_SUPPRESSING_SPEAKERPHONE',
    'KSCAMERA_EXTENDEDPROP_WBPRESET','KSNODETYPE_MICROPHONE',
    'KS_VIDEOSTREAM_PREVIEW','KSRTAUDIO_HWREGISTER_PROPERTY32',
    'STATIC_KSNODETYPE_LEGACY_AUDIO_CONNECTOR',
    'STATIC_KSPROPSETID_AudioModule','tagKS_MPEGVIDEOINFO2',
    'STATIC_KSPROPSETID_DrmAudioStream',
    'KSALGORITHMINSTANCE_SYSTEM_MICROPHONE_ARRAY_PROCESSOR',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_MEDIUM',
    'KSAUDFNAME_AUX','KSCAMERAPROFILE_VideoHDR8',
    'STATIC_KSAUDFNAME_WAVE_OUT_MIX','tagTRANSPORTVIDEOPARMS',
    'STATIC_KSNODETYPE_FM_RX','INIT_EXBUS_MANUFACTURER_ID',
    'KSNODETYPE_FM_RX','STATIC_KSDATAFORMAT_SUBTYPE_RIFFMIDI',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_HIGH',
    'STATIC_KSPROPSETID_VPConfig','STATIC_KSPROPSETID_Hrtf3d',
    'INIT_WAVEFORMATEX_GUID','SPEAKER_ALL',
    'STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO',
    'KS_VBI_FLAG_TVTUNER_CHANGE','_KSCAMERA_PROFILE_MEDIAINFO',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_WB',
    'KSAUDFNAME_RECORDING_CONTROL','KSCAMERA_EXTENDEDPROP_ISO_12800',
    'KSDATAFORMAT_TYPE_MPEG2_TRANSPORT','KSPROPERTY_VIDEODECODER_STATUS_S',
    'KSNODETYPE_CD_PLAYER','IS_COMPATIBLE_MMREG_MID',
    'STATIC_KSNODETYPE_SWSYNTH','KS_COPY_MACROVISION_LEVEL',
    'STATIC_KSNODETYPE_VIDEO_INPUT_TERMINAL',
    'KSDATAFORMAT_SUBTYPE_MPEGLAYER3','KS_VBISAMPLINGRATE_5X_NABTS',
    'KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_2X',
    'PROPSETID_VIDCAP_CAMERACONTROL','KS_DVD_CGMS_NO_COPY',
    'KSNODETYPE_SATELLITE_RECEIVER_AUDIO','STATIC_KSCATEGORY_MULTIPLEXER',
    'KSNODETYPE_HEAD_MOUNTED_DISPLAY_AUDIO','SPEAKER_SIDE_RIGHT',
    'KSNODETYPE_VIDEO_SELECTOR','KS_AMCONTROL_PAD_TO_16x9',
    'STATIC_KSNODETYPE_PEAKMETER','AEC_MODE_FULL_DUPLEX',
    'KS_AMVP_SELECTFORMATBY','KSAUDIO_CHANNEL_CONFIG',
    'KSCAMERA_EXTENDEDPROP_OPTIMIZATION_POWER',
    'AUDIO_EFFECT_TYPE_BASS_BOOST','IS_COMPATIBLE_USBAUDIO_MID',
    'KS_AM_ExactRateChange','KSCATEGORY_AUDIO_DEVICE',
    'STATIC_KSAUDFNAME_LINE_IN_VOLUME',
    'KSNODETYPE_DIGITAL_AUDIO_INTERFACE',
    'KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_ON','KSPROPERTY_VIDEODECODER_S',
    'STATIC_KSDATAFORMAT_SUBTYPE_D16','KSAUDFNAME_MIDI_IN_VOLUME',
    'KSDATAFORMAT_SPECIFIER_VBI','KSNODETYPE_RADIO_RECEIVER',
    'KSDATAFORMAT_SUBTYPE_RAW8','WAVE_FORMAT_EXTENSIBLE',
    'KSPROPERTY_TVAUDIO_S','KSPROPERTY_CAMERACONTROL_FLASH',
    'KSNODEPIN_AEC_CAPTURE_IN','tagKSCAMERA_EXTENDEDPROP_FIELDOFVIEW',
    'STATIC_KSCAMERAPROFILE_HighFrameRate','STATIC_KSAUDFNAME_STEREO_MIX',
    'KSNODETYPE_HEADPHONES','STATIC_KSNODETYPE_EQUALIZER',
    'STATIC_AUDIO_SIGNALPROCESSINGMODE_DEFAULT','KSPROPSETID_Cyclic',
    'INIT_MMREG_MID','KS_VIDEO_FLAG_IPB_MASK','KSPROPERTY_OVERLAYUPDATE',
    'AEC_STATUS_FD_HISTORY_CONTINUOUSLY_CONVERGED',
    'KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE',
    '_tagKSAUDIOENGINE_DESCRIPTOR',
    'STATIC_KSDATAFORMAT_SPECIFIER_H264_VIDEO',
    'DEVPKEY_KsAudio_PacketSize_ConstraINTs2','KS_AMCONTROL_PAD_TO_4x3',
    'KS_iTRUECOLOR','KSDATAFORMAT_SUBTYPE_ANALOG','KS_VIDEOSTREAM_STILL',
    'EXTRACT_MMREG_PID','STATIC_KSDATAFORMAT_SUBTYPE_MPEG2_VIDEO',
    'STATIC_KSAUDFNAME_VIDEO_VOLUME','PINNAME_SPDIF_IN','KS_AMVP_MODE',
    'SOUNDDETECTOR_PATTERNHEADER','KSAUDFNAME_WAVE_OUT_MIX',
    'KS_DVD_SECTOR_PROTECTED','KSDATAFORMAT_SUBTYPE_JPEG',
    'KSPROPSETID_DirectSound3DBuffer','STATIC_KSPROPSETID_CopyProt',
    'STATIC_KSDATAFORMAT_TYPE_MIDI',
    'KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO',
    'STATIC_KSNODETYPE_LEVEL_CALIBRATION_NOISE_SOURCE','KSNODETYPE_SUM',
    'KSCAMERA_EXTENDEDPROP_FLASH_ON','KS_VIDEOSTREAM_CC',
    'PINNAME_VIDEO_CC_CAPTURE','KSNODETYPE_PERSONAL_MICROPHONE',
    'KSPROPERTY_VIDEOCONTROL_MODE_S','KSAUDFNAME_MIDI',
    'KSDATAFORMAT_SUBTYPE_AC3_AUDIO',
    'STATIC_KSCAMERAPROFILE_PhotoSequence','KS_VBI_FLAG_MV_DETECTED',
    'STATIC_KSPROPSETID_Jack','KSPROPERTY_TUNER_SCAN_CAPS_S',
    'KSCAMERA_EXTENDEDPROP_FACEDETECTION_OFF',
    'KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_OFF',
    'STATIC_KSPROPSETID_DvdSubPic','STATIC_APO_CLASS_UUID',
    'KSEVENTSETID_VPVBINotify','STATIC_KSNODETYPE_DVD_AUDIO',
    'STATIC_KSAUDFNAME_MONO_MIX_VOLUME','KSDATAFORMAT_SUBTYPE_MPEG2_AUDIO',
    'KSNODETYPE_DSS_AUDIO','KS_CC_SUBSTREAM_EVEN',
    'KSMUSIC_TECHNOLOGY_WAVETABLE','KSDATAFORMAT_SUBTYPE_DRM',
    'KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PHOTO',
    'WAVEFORMATEXTENSIBLE_IEC61937',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_MACRO','KSAUDIO_SPEAKER_DIRECTOUT',
    'KSPROPERTY_CYCLIC','KSCAMERA_METADATA_FRAMEILLUMINATION_FLAG_ON',
    'KSPROPERTY_BIBLIOGRAPHIC','KS_TVAUDIO_MODE_STEREO',
    'STATIC_KSEVENTSETID_CameraEvent','KSPROPSETID_Jack',
    'tagKS_VIDEOINFOHEADER2','STATIC_KSNODETYPE_MULTITRACK_RECORDER',
    'KSDATAFORMAT_SPECIFIER_ANALOGVIDEO','KSAUDIO_SPEAKER_3POINT1',
    'KSAUDIO_SPEAKER_3POINT0','PINNAME_VIDEO_EDS',
    'STATIC_KSCATEGORY_PREFERRED_WAVEOUT_DEVICE',
    'AEC_STATUS_FD_HISTORY_UNINITIALIZED','KSDATAFORMAT_SUBTYPE_DSS_AUDIO',
    'SYSAUDIO_PREFERRED_DEVICE','KSCAMERAPROFILE_FLAGS_VIDEOSTABLIZATION',
    'STATIC_KSNODETYPE_DCC_IO_DIGITAL_COMPACT_CASSETTE',
    '_VBICODECFILTERING_STATISTICS_CC_PIN','KSEVENT_CAMERACONTROL',
    'KSDATAFORMAT_WAVEFORMATEXTENSIBLE','KSPROPSETID_Wave_Queued',
    '_TunerDecoderLockType','KSAUDFNAME_MICROPHONE_BOOST',
    'KSPROPERTY_DROPPEDFRAMES_CURRENT_S',
    'KSCAMERA_EXTENDEDPROP_OPTIMIZATION_QUALITY',
    'KS_CC_SUBSTREAM_SERVICE_CC4','KSCameraProfileSensorType_RGB',
    'STATIC_BLUETOOTHLE_MIDI_SERVICE_UUID','KS_CC_SUBSTREAM_SERVICE_CC1',
    'STATIC_KSDATAFORMAT_SUBTYPE_VPVBI','KS_CC_SUBSTREAM_SERVICE_CC3',
    'STATIC_KSCAMERAPROFILE_VideoConferencing',
    'KSPROPERTY_CAMERACONTROL_S_EX','KSDATAFORMAT_SUBTYPE_RIFFMIDI',
    'AUDIOMODULE_MAX_DATA_SIZE','_CC_HW_FIELD','STATIC_KSCATEGORY_ENCODER',
    'STATIC_KSDATAFORMAT_SUBTYPE_SDDS_AUDIO',
    'PROPSETID_VIDCAP_VIDEOCONTROL','KSAUDIO_STEREO_SPEAKER_GEOMETRY_WIDE',
    'KSPROPERTY_DRMAUDIOSTREAM','STATIC_PROPSETID_VIDCAP_CROSSBAR',
    'KS_SECURE_CAMERA_SCENARIO_ID',
    'KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_16X','KSAUDFNAME_MONO_OUT',
    'KSCAMERA_EXTENDEDPROP_CAPS_RESERVED',
    'AUDIO_EFFECT_TYPE_ENVIRONMENTAL_EFFECTS',
    'KSDATAFORMAT_SUBTYPE_WMAUDIO_LOSSLESS',
    'KS_INTERLACE_FieldPatBothIrregular','KSPROPSETID_SoundDetector',
    'KSCAMERA_EXTENDEDPROP_WHITEBALANCE_MODE',
    'STATIC_AUDIO_SIGNALPROCESSINGMODE_MEDIA','KSDATAFORMAT_TYPE_VIDEO',
    'DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_CLIPLIST',
    'STATIC_PINNAME_SPDIF_IN','KSPROPSETID_VPVBIConfig',
    'STATIC_KSNODETYPE_MUTE','AUDIO_EFFECT_TYPE_BEAMFORMING',
    'STATIC_KSMETHODSETID_Wave_Queued','KSDSOUND_BUFFERDESC',
    'KSDATAFORMAT_SUBTYPE_MJPG_DEPTH','EXTRACT_USBAUDIO_PID',
    'KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S',
    'STATIC_KSNODETYPE_NOISE_SUPPRESS','KSEVENTSETID_VIDCAPTOSTI',
    'KSNODETYPE_DESKTOP_SPEAKER','KSDS3D_ITD_PARAMS',
    'KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO',
    'KSNODETYPE_BIDIRECTIONAL_UNDEFINED','KS_VIDEO_FLAG_B_FRAME',
    'KSCAMERA_EXTENDEDPROP_FLASH_OFF','KS_AM_PROPERTY_TS_RATE_CHANGE',
    'STATIC_PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST',
    '_WST_BUFFER','STATIC_PROPSETID_EXT_TRANSPORT',
    'STATIC_KSNODETYPE_DSS_AUDIO',
    'STATIC_KSNODETYPE_BIDIRECTIONAL_UNDEFINED',
    'KSCAMERA_PERFRAMESETTING_MANUAL','_KS_VIDEO_STREAM_CONFIG_CAPS',
    'tag_KS_TRUECOLORINFO',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_MANUAL',
    'PROPSETID_TIMECODE_READER','KSNODETYPE_VIDEO_CAMERA_TERMINAL',
    'KSCAMERA_EXTENDEDPROP_ISO_400','SPEAKER_FRONT_LEFT_OF_CENTER',
    'SYSAUDIO_FLAGS_DONT_COMBINE_PINS','KS_INTERLACE_FieldPatternMask',
    'KSPROPERTY_VIDEOPROCAMP_S','KSPROPERTY_CROSSBAR_CAPS_S',
    'STATIC_KSCAMERAPROFILE_HighQualityPhoto',
    'STATIC_KSDATAFORMAT_SPECIFIER_WAVEFORMATEX','IS_COMPATIBLE_MMREG_PID',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL',
    'KSNODETYPE_OMNI_DIRECTIONAL_MICROPHONE','STATIC_PINNAME_HDMI_OUT',
    'KSPROPERTY_VIDCAP_VIDEOPROCAMP','STATIC_KSAUDFNAME_VIDEO_MUTE',
    'KS_VIDEOSTREAM_NABTS','KSNODETYPE_ANALOG_TAPE','_KS_DVDCOPY_CHLGKEY',
    'KSDATAFORMAT_TYPE_TEXT','STATIC_PINNAME_VIDEO_VBI',
    'KSRTAUDIO_BUFFER32','STATIC_KSDATAFORMAT_SUBTYPE_TELETEXT',
    'STATIC_EVENTSETID_TUNER','KSCAMERAPROFILE_HDRWithWCGPhoto',
    'EVENTSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST',
    'KSNODETYPE_PHONE_LINE','STATIC_KSNODETYPE_DISPLAYPORT_INTERFACE',
    'KSCAMERAPROFILE_HighFrameRate','STATIC_KSAUDFNAME_3D_STEREO',
    'KSCATEGORY_VBICODEC','KSPROPSETID_AudioGfx',
    'KSNODETYPE_DOWN_LINE_PHONE','KSJACK_DESCRIPTION','KSEVENT_TUNER',
    'STATIC_KSDATAFORMAT_SUBTYPE_WMAUDIO_LOSSLESS',
    'KSPROPERTY_DIRECTSOUND3DLISTENER','STATIC_KSCATEGORY_AUDIO_SPLITTER',
    'KSNODETYPE_SYNTHESIZER','SPEAKER_TOP_BACK_LEFT',
    'tagKSCAMERA_EXTENDEDPROP_METADATAINFO',
    'KSCAMERA_EXTENDEDPROP_EVCOMP_QUARTERSTEP','EXTRACT_MMREG_MID',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD',
    'KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_BACKGROUND_SUBTRACTION',
    'SPEAKER_LOW_FREQUENCY','DEFINE_USBAUDIO_PID_GUID',
    'KSAUDIO_QUALITY_WORST','KSRTAUDIO_HWLATENCY',
    'STATIC_KSNODETYPE_TV_TUNER_AUDIO','KSEVENT_VPNOTIFY',
    'KSCAMERA_EXTENDEDPROP_VIDEOTORCH_ON','KSAC3_SERVICE_DIALOG_ONLY',
    'KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_VARIABLE',
    'KSDS3D_LISTENER_ORIENTATION',
    'KSAUDIO_STEREO_SPEAKER_GEOMETRY_HEADPHONE',
    'STATIC_AUDIO_EFFECT_TYPE_AUTOMATIC_GAIN_CONTROL',
    'STATIC_KSAUDFNAME_RECORDING_CONTROL',
    'KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_OFF',
    'STATIC_KSNODETYPE_REVERB','KSRTAUDIO_SETWRITEPACKET_INFO',
    'KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MANUAL','PROPSETID_EXT_DEVICE',
    'KSNODETYPE_DAT_IO_DIGITAL_AUDIO_TAPE','KSPROPERTY_TELEPHONY_TOPOLOGY',
    'PINNAME_PREVIEW','KSPROPSETID_OverlayUpdate',
    'KSCATEGORY_AUDIO_SPLITTER','KSPROPERTY_SOUNDDETECTOR',
    'KSCAMERA_EXTENDEDPROP_FOCUS_REGIONBASED',
    'KSPROPSETID_MPEG4_MediaType_Attributes',
    'KSPROPERTY_SYSAUDIO_DEFAULT_TYPE','KSNODETYPE_SURROUND_ENCODER',
    'STATIC_KSNODETYPE_CHORUS','_VBICODECFILTERING_STATISTICS_TELETEXT',
    'STATIC_KSDATAFORMAT_SUBTYPE_RIFFWAVE',
    'STATIC_KSDATAFORMAT_SPECIFIER_VC_ID',
    'STATIC_KSDATAFORMAT_SUBTYPE_L8_IR','STATIC_PINNAME_VIDEO_TELETEXT',
    'KSCAMERA_EXTENDEDPROP_ISO_3200',
    'KS_NABTS_GROUPID_MICROSOFT_RESERVED_TEST_DATA_BASE',
    'STATIC_KSAUDFNAME_RECORDING_SOURCE','STATIC_KSNODETYPE_HEADSET',
    'STATIC_KSDATAFORMAT_SUBTYPE_RAW8',
    'tagKSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE',
    'KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK','KSNODETYPE_VCR_AUDIO',
    'KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_OFF','KSMETHODSETID_Wave_Queued',
    'STATIC_KSNODETYPE_ROOM_SPEAKER','KS_MPEG2_DVDLine21Field2',
    'KS_MPEG2_DVDLine21Field1','KSNODETYPE_MINIDISK',
    'tagKS_TVTUNER_CHANGE_INFO','KSEVENTSETID_ExtendedCameraControl',
    'KS_NABTS_GROUPID_PRODUCTION_COMPANY_ADVERTISER_BASE',
    'KSPROPSETID_AudioEngine','KS_BI_JPEG','AUDIOENDPOINT_CLASS_UUID',
    'MEDIUM_INFO','STATIC_KSCATEGORY_VPMUX',
    'KSCAMERA_EXTENDEDPROP_OPTIMIZATION_VIDEO',
    'KSCAMERA_EXTENDEDPROP_ZOOM_DEFAULT',
    'KSCAMERA_EXTENDEDPROP_OPTIMIZATION_DEFAULT',
    'STATIC_KSEVENTSETID_SoundDetector',
    'KSDATAFORMAT_TYPE_STANDARD_PACK_HEADER','STATIC_KSAUDFNAME_TREBLE',
    'KS_DVD_CGMS_COPY_PERMITTED','KSDATAFORMAT_SUBTYPE_L16_IR',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_FLASHPOWER',
    'STATIC_KSNODETYPE_DAC','STATIC_KSCATEGORY_DRM_DESCRAMBLE',
    'STATIC_KSNODETYPE_ADC','KSCAMERA_EXTENDEDPROP_SCENEMODE_BEACH',
    'PINNAME_DISPLAYPORT_OUT','KSCAMERA_EXTENDEDPROP_OPTIMIZATION_LATENCY',
    'KSAUDDECOUTMODE_STEREO_ANALOG','STATIC_KSDATAFORMAT_SUBTYPE_MJPG_IR',
    'KSDATAFORMAT_SUBTYPE_L8_CUSTOM','KSPROPERTY_VIDEOPROCAMP_FLAGS_AUTO',
    'AUDIO_SIGNALPROCESSINGMODE_DEFAULT','_tagKSJACK_SINK_INFORMATION',
    'STATIC_KSDATAFORMAT_TYPE_VBI','KSPROPERTY_AUDIO_BUFFER_DURATION',
    'KSDATAFORMAT_WAVEFORMATEX','STATIC_AUDIO_SIGNALPROCESSINGMODE_RAW',
    'KSAUDIO_SPEAKER_STEREO','STATIC_KSDATAFORMAT_SUBTYPE_IMAGE_RGB32',
    'KSPROPERTY_VIDEOENCODER_S','KSCAMERA_EXTENDEDPROP_OIS_OFF',
    'STATIC_KSPROPSETID_Wave_Queued','STATIC_CODECAPI_CURRENTCHANGELIST',
    '_DDVIDEOPORTCONNECT','STATIC_KSAUDFNAME_MICROPHONE_BOOST',
    'KS_VBIDATARATE_CC','KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY',
    'KSPROPERTY_ALLOCATOR_CONTROL',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_AAC',
    'KSALGORITHMINSTANCE_SYSTEM_NOISE_SUPPRESS',
    'KSPROPERTY_VIDEOCOMPRESSION_S','STATIC_KSNODETYPE_TELEPHONY_BIDI',
    'STATIC_KSAUDFNAME_3D_DEPTH','KSDATAFORMAT_SUBTYPE_IEC61937_DST',
    'KSCATEGORY_AUDIO_GFX','KSEVENTSETID_AudioControlChange',
    'KSMETHOD_WAVE_QUEUED_BREAKLOOP','DEFINE_MMREG_PID_GUID',
    'STATIC_KSAUDFNAME_PEAKMETER','ENCAPIPARAM_BITRATE',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS',
    'KSCAMERAPROFILE_VideoConferencing',
    'KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE','AEC_MODE_PASS_THROUGH',
    'STATIC_PINNAME_CAPTURE','KSNODETYPE_MIDI_JACK',
    'KSDATAFORMAT_SUBTYPE_L16_CUSTOM','KSDATAFORMAT_SUBTYPE_PCM',
    'STATIC_KSNODETYPE_VIDEO_STREAMING',
    '_VBICODECFILTERING_STATISTICS_NABTS','KSPROPERTY_DIRECTSOUND3DBUFFER',
    'tagKS_DATAFORMAT_VIDEOINFO_PALETTE','_tagKSAUDIOENGINE_VOLUMELEVEL',
    'CODECAPI_SUPPORTSEVENTS','STATIC_KSDATAFORMAT_SPECIFIER_VBI',
    'SPEAKER_FRONT_RIGHT','STATIC_KSDATAFORMAT_SUBTYPE_ADPCM',
    'AUDIO_EFFECT_TYPE_ACOUSTIC_ECHO_CANCELLATION',
    'KS_VIDEO_FLAG_FIELD1FIRST','STATIC_KSDATAFORMAT_SUBTYPE_MJPG_CUSTOM',
    'KSAUDIO_SPEAKER_GROUND_FRONT_LEFT',
    'AUDIO_EFFECT_TYPE_ROOM_CORRECTION','STATIC_KSPROPSETID_Wave',
    'KSAUDFNAME_MIDRANGE','STATIC_KSMUSIC_TECHNOLOGY_FMSYNTH',
    'KSDATAFORMAT_SUBTYPE_Line21_BytePair',
    'KSDATAFORMAT_TYPE_STANDARD_ELEMENTARY_STREAM',
    'STATIC_CODECAPI_SUPPORTSEVENTS','KSMEDIUMSETID_MidiBus',
    'KSPROPERTYSETID_PerFrameSettingControl',
    'STATIC_KSAUDFNAME_MASTER_VOLUME','KSNODETYPE_MICROPHONE_ARRAY',
    'KSPROPSETID_FMRXControl','KSDATAFORMAT_TYPE_IMAGE',
    'KSDATAFORMAT_SUBTYPE_OVERLAY','KSDATAFORMAT_SUBTYPE_NABTS_FEC',
    'STATIC_KSPROPSETID_Sysaudio_Pin','KS_CC_SUBSTREAM_ODD',
    'KSCAMERAPROFILE_FLAGS_VIDEOHDR','KSPROPERTY_DVDSUBPIC',
    'KSEVENTSETID_LoopedStreaming','KS_DVD_NOT_COPYRIGHTED',
    'KSCAMERA_EXTENDEDPROP_EVCOMP_FULLSTEP','KSNODETYPE_VIDEO_DISC_AUDIO',
    'KSAUDFNAME_CD_IN_VOLUME','KSWAVE_BUFFER_ATTRIBUTEF_LOOPING',
    'KSCAMERA_EXTENDEDPROP_ISO_80',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_SENSORFRAMERATE',
    'STATIC_KSDATAFORMAT_SUBTYPE_MPEG1Payload',
    'STATIC_KSCAMERAPROFILE_VideoRecording','STATIC_KSAUDFNAME_WAVE_MUTE',
    'KSNODETYPE_ANALOG_CONNECTOR','tagKS_VIDEOINFO',
    'KS_NABTS_GROUPID_LOCAL_CABLE_SYSTEM_CONTENT_BASE',
    'KSCAMERA_EXTENDEDPROP_FACEDETECTION_ADVANCED_MASK',
    'STATIC_CLSID_KsIBasicAudioInterfaceHandler',
    'KS_INTERLACE_FieldPatField1Only','KSPROPERTY_AUDIO',
    'KS_NABTS_GROUPID_PRODUCTION_COMPANY_CONTENT_BASE',
    'KSNODETYPE_TELEPHONY_UNDEFINED','KSPROPERTY_TUNER_IF_MEDIUM_S',
    'KSCAMERA_EXTENDEDPROP_ISO_800','KSCAMERA_EXTENDEDPROP_ISO_200',
    '_VBICODECFILTERING_STATISTICS_CC',
    'STATIC_KSAUDFNAME_PC_SPEAKER_VOLUME','STATIC_KSEVENTSETID_Sysaudio',
    'STATIC_KSAUDFNAME_VOLUME_CONTROL','KSCAMERA_EXTENDEDPROP_ISO_25600',
    'SPEAKER_SIDE_LEFT','KSCAMERA_EXTENDEDPROP_FLAG_CANCELOPERATION',
    'SYSAUDIO_SELECT_GRAPH','tagKS_MPEG1VIDEOINFO',
    'STATIC_AUDIO_EFFECT_TYPE_SPEAKER_PROTECTION',
    'KSDATAFORMAT_SUBTYPE_ADPCM',
    'KSDATAFORMAT_SPECIFIER_DIALECT_AC3_AUDIO',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP',
    'STATIC_KSCATEGORY_SYNTHESIZER',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_AUTO',
    'STATIC_AUDIO_EFFECT_TYPE_ROOM_CORRECTION',
    'STATIC_KSNODETYPE_DESKTOP_SPEAKER','TELEPHONY_CALLSTATE',
    'KSDATAFORMAT_TYPE_ANALOGVIDEO',
    '_VBICODECFILTERING_STATISTICS_TELETEXT_PIN',
    'STATIC_KSPROPERTYSETID_ExtendedCameraControl',
    'STATIC_PROPSETID_VIDCAP_SELECTOR','tagTRANSPORTSTATUS',
    'KSCAMERA_EXTENDEDPROP_EVCOMP_SIXTHSTEP',
    'STATIC_KSPROPSETID_Acoustic_Echo_Cancel','KSAUDFNAME_3D_DEPTH',
    'STATIC_KSDATAFORMAT_SUBTYPE_PCM',
    'STATIC_KS_SECURE_CAMERA_SCENARIO_ID',
    'STATIC_KSDATAFORMAT_SUBTYPE_NABTS_FEC',
    'KSCAMERA_EXTENDEDPROP_OIS_AUTO','_KS_DVDCOPY_TITLEKEY',
    'STATIC_PROPSETID_ALLOCATOR_CONTROL','KSCAMERAPROFILE_VideoRecording',
    'KSAUDFNAME_PEAKMETER','KSDATAFORMAT_SUBTYPE_DTS_AUDIO',
    'KSPROPERTY_COMPOSIT_ON','TELEPHONY_CALLTYPE',
    'AUDIO_SIGNALPROCESSINGMODE_MOVIE','KSAUDIO_SPEAKER_5POINT1_SURROUND',
    'KSPROPERTY_CROSSBAR_ACTIVE_S','EPxcPortConnection',
    'KSPROPERTY_VIDEOPROCAMP_S2','KSMUSIC_TECHNOLOGY_FMSYNTH',
    'STATIC_KSAUDFNAME_BASS','PROPSETID_VIDCAP_CAMERACONTROL_FLASH',
    'DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_VIDEOPOSITION',
    'KSAUDFNAME_ALTERNATE_MICROPHONE','KS_CC_SUBSTREAM_SERVICE_XDS',
    'CC_MAX_HW_DECODE_LINES','KSNODETYPE_AUDIO_KEYWORDDETECTOR',
    'KSCAMERA_EXTENDEDPROP_FLASH_REDEYEREDUCTION','KSEVENT_SYSAUDIO',
    'KSNODETYPE_EMBEDDED_UNDEFINED','STATIC_KSNODETYPE_DRM_DESCRAMBLE',
    '_timecode','_KSCAMERA_EXTENDEDPROP_PROFILE',
    'KSDATAFORMAT_SUBTYPE_MPEG',
    'KSCAMERA_EXTENDEDPROP_WARMSTART_MODE_DISABLED',
    'KSPROPERTY_CAMERACONTROL_FLAGS_AUTO',
    'STATIC_KSDATAFORMAT_TYPE_STANDARD_ELEMENTARY_STREAM',
    'KS_VBI_FLAG_MV_HARDWARE','KSAUDIO_POSITIONEX',
    'STATIC_KSCOMPONENTID_USBAUDIO','KSDSOUND_BUFFER_CTRL_3D',
    'INIT_USB_TERMINAL','KSPROPERTY_VIDEOCOMPRESSION_GETINFO_S',
    'STATIC_PROPSETID_VIDCAP_VIDEOCONTROL','KSAUDFNAME_PC_SPEAKER_MUTE',
    'KSPROPERTY_VIDEOPROCAMP_FLAGS_MANUAL','MAX_NABTS_VBI_LINES_PER_FIELD',
    'WST_TVTUNER_CHANGE_END_TUNE','KS_TVAUDIO_PRESET_LANG_B',
    'KS_TVAUDIO_PRESET_LANG_A','KSPROPSETID_Itd3d','KSAC3_DOWNMIX',
    'KS_MPEG2Level','KSDS3D_HRTF_PARAMS_MSG',
    'KSPROPERTY_TELEPHONY_CONTROL','KSWAVE_BUFFER_ATTRIBUTEF_STATIC',
    'KSAUDIO_STEREO_SPEAKER_GEOMETRY_MAX','KSDATAFORMAT_SUBTYPE_TELETEXT',
    'STATIC_KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR',
    'STATIC_KSDATAFORMAT_SUBTYPE_SUBPICTURE','EPcxConnectionType',
    'KSAUDFNAME_STEREO_MIX','KSAUDFNAME_MASTER_MUTE',
    'KS_VIDEO_FLAG_I_FRAME','KSPROPERTY_VIDEODECODER_CAPS_S',
    'DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_INTERESTS',
    'STATIC_KSALGORITHMINSTANCE_SYSTEM_NOISE_SUPPRESS',
    'KSNODETYPE_LOUDNESS','KSDATAFORMAT_SUBTYPE_MULAW',
    'KSCAMERAPROFILE_HDRWithWCGVideo','APO_CLASS_UUID',
    'KSNODETYPE_TELEPHONY_BIDI','KSINTERFACESETID_Media',
    'STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO','KS_iPALETTE',
    'STATIC_PROPSETID_VIDCAP_CAMERACONTROL_FLASH',
    'KSPROPERTY_TUNER_FREQUENCY_S','KS_MPEG2_27MhzTimebase',
    'KSAUDFNAME_LINE_MUTE','STATIC_KSPROPSETID_OverlayUpdate',
    'KSNODETYPE_DCC_IO_DIGITAL_COMPACT_CASSETTE',
    'KSDSOUND_BUFFER_CTRL_HRTF_3D','KS_DVD_SECTOR_NOT_PROTECTED',
    'KSNODETYPE_DAC','STATIC_KSDATAFORMAT_SUBTYPE_MPEG2_AUDIO',
    'STATIC_KSNODETYPE_DEMUX','STATIC_KSNODETYPE_SUM',
    'KS_CC_SUBSTREAM_SERVICE_T4','KS_CC_SUBSTREAM_SERVICE_T1',
    'STATIC_KSDATAFORMAT_SUBTYPE_LPCM_AUDIO',
    'STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO',
    'KS_CC_SUBSTREAM_SERVICE_T2','KSDATAFORMAT_TYPE_STANDARD_PES_PACKET',
    'STATIC_KSNODETYPE_AGC','KSDATAFORMAT_SPECIFIER_MPEG1_VIDEO',
    'STATIC_AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS','KSNODETYPE_AGC',
    'KS_VIDEOSTREAM_IS_VPE','KSAUDIO_PREFERRED_STATUS',
    'KSPROPSETID_DvdSubPic','KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO',
    'KSNODEPIN_STANDARD_OUT','tagKS_DATAFORMAT_IMAGEINFO',
    'STATIC_KSCATEGORY_ACOUSTIC_ECHO_CANCEL','STATIC_KSNODETYPE_CD_PLAYER',
    'STATIC_KSALGORITHMINSTANCE_SYSTEM_ACOUSTIC_ECHO_CANCEL',
    'KSDATAFORMAT_SUBTYPE_MIDI','STATIC_KSNODETYPE_UPDOWN_MIX',
    'KSDATAFORMAT_TYPE_AUXLine21Data',
    'STATIC_KSPROPSETID_MPEG4_MediaType_Attributes','KSAUDFNAME_CD_VOLUME',
    'KSCATEGORY_PREFERRED_WAVEOUT_DEVICE','KSINTERFACE_MEDIA',
    'KS_COPYPROTECT_RestrictDuplication','KSMUSICFORMAT',
    'KSCAMERAPROFILE_VariablePhotoSequence',
    'KSCAMERA_PERFRAMESETTING_FRAME_HEADER',
    'tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS','KSMETHODSETID_Wavetable',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD',
    'STATIC_CODECAPI_SETALLDEFAULTS',
    'STATIC_KSCATEGORY_WDMAUD_USE_PIN_NAME',
    'KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_4X','STATIC_KSCATEGORY_TOPOLOGY',
    'SPEAKER_FRONT_CENTER','KSPROPERTY_VIDEOCOMPRESSION_S1',
    'KSDATAFORMAT_SUBTYPE_NABTS','KSPROPERTY_TUNER_STATUS_S',
    'KSNODETYPE_AUDIO_ENGINE','KSNODETYPE_HANDSET',
    'KSNODETYPE_VIDEO_INPUT_MTT','AUDIO_SIGNALPROCESSINGMODE_RAW',
    'STATIC_PINNAME_NABTS_CAPTURE','STATIC_KSAUDFNAME_MIDI_MUTE',
    'STATIC_KSNODETYPE_PARAMETRIC_EQUALIZER',
    'KSDATAFORMAT_SPECIFIER_MPEG2_AUDIO',
    'STATIC_KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK',
    'DEFINE_WAVEFORMATEX_GUID','KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_AUTO',
    'KS_MPEG2_DSS_UserData','STATIC_KSAUDFNAME_MIC_VOLUME',
    'KSEVENT_SOUNDDETECTOR','KS_DVD_COPYRIGHT_MASK',
    '_WNF_KSCAMERA_STREAMSTATE_INFO',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS_ATMOS',
    'KS_SIZE_PALETTE','STATIC_KSDATAFORMAT_SUBTYPE_OVERLAY',
    'KSPROPERTY_VIDEOCONTROL_FRAME_RATES_S',
    'KSCAMERA_EXTENDEDPROP_PHOTOMODE_SEQUENCE_SUB_NONE',
    'KSCAMERA_EXTENDEDPROP_ROITYPE','KS_AnalogVideo_SECAM_Mask',
    'KSCAMERA_EXTENDEDPROP_FLASH_SINGLEFLASH',
    'STATIC_KSDATAFORMAT_SUBTYPE_JPEG','KS_AMCONTROL_USED',
    'STATIC_KSNODETYPE_HEADPHONES','STATIC_KSCATEGORY_VIDEO',
    'KS_VIDEO_FLAG_P_FRAME','SPEAKER_BACK_RIGHT',
    'AUDIO_EFFECT_TYPE_SPEAKER_PROTECTION',
    'STATIC_KSDATAFORMAT_SUBTYPE_L16',
    'tagKSCAMERA_MAXVIDEOFPS_FORPHOTORES','KS_CC_SUBSTREAM_FIELD2_MASK',
    '_VBICODECFILTERING_NABTS_SUBSTREAMS','KSEVENT_VIDEODECODER',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_NIGHTPORTRAIT',
    'STATIC_KSNODETYPE_VCR_AUDIO','KSAUDFNAME_MIDI_MUTE','KS_MPEG2Profile',
    'KSDISPLAYCHANGE','KSAUDIO_SPEAKER_QUAD','KS_CC_SUBSTREAM_SERVICE_CC2',
    'KSAUDIO_SPEAKER_5POINT1',
    'KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_INFINITY',
    'KSDATAFORMAT_SUBTYPE_IEEE_FLOAT','KSAUDFNAME_BASS',
    'KS_NABTS_GROUPID_ORIGINAL_CONTENT_BASE','KSNODETYPE_ROOM_SPEAKER',
    'INIT_EXBUS_PRODUCT_NAME','KSDATAFORMAT_TYPE_NABTS',
    'STATIC_KSAUDFNAME_LINE_MUTE','STATIC_KSCATEGORY_NETWORK',
    'STATIC_KSAUDFNAME_MONO_MIX',
    'KSPROPERTY_VIDEOPROCAMP_NODE_S','PTIMECODE_SAMPLE',
    'KSAUDFNAME_LINE_VOLUME','STATIC_KSEVENTSETID_Cyclic',
    'KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_PROPERTY',
    'SPEAKER_BACK_LEFT','STATIC_KSEVENTSETID_VPVBINotify',
    'KSAUDFNAME_MONO_MIX_MUTE','STATIC_CODECAPI_CHANGELISTS',
    'KSAC3_SERVICE_COMMENTARY','KSAUDIO_QUALITY_BASIC',
    'PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION',
    'KSEVENT_VPVBINOTIFY','KS_NABTS_GROUPID_NETWORK_WIDE_CONTENT_BASE',
    'KSAUDIO_QUALITY_ADVANCED','STATIC_CODECAPI_VIDEO_ENCODER',
    'KSAC3_ALTERNATE_AUDIO_2','STATIC_KSNODETYPE_OUTPUT_UNDEFINED',
    'STATIC_KSDATAFORMAT_TYPE_ANALOGAUDIO',
    'KSCAMERAPROFILE_HighQualityPhoto',
    'STATIC_KSNODETYPE_MICROPHONE_ARRAY_PROCESSOR',
    'STATIC_PINNAME_VIDEO_STILL','AUDIO_EFFECT_TYPE_VIRTUAL_HEADPHONES',
    'STATIC_KSAUDFNAME_PC_SPEAKER_MUTE','IS_COMPATIBLE_USBAUDIO_PID',
    'KSDATAFORMAT_SUBTYPE_MPEG1Video','KSPROPERTY_VIDMEM_TRANSPORT',
    'KSNODETYPE_HEADSET','STATIC_AUDIO_SIGNALPROCESSINGMODE_NOTIFICATION',
    'tagKSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE','KS_iGREEN',
    'KSPROPSETID_AudioDecoderOut','LOOPEDSTREAMING_POSITION_EVENT_DATA',
    'STATIC_KSDATAFORMAT_SUBTYPE_WAVEFORMATEX','STATIC_PINNAME_VIDEO_EDS',
    'CODECAPI_SETALLDEFAULTS','STATIC_KSDATAFORMAT_SPECIFIER_MPEG2_AUDIO',
    'STATIC_KSNODETYPE_ECHO_CANCELING_SPEAKERPHONE',
    'KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_FNF','KSWAVE_OUTPUT_CAPABILITIES',
    'tagKSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING','INIT_EXBUS_PRODUCT_ID',
    'KSPROPERTY_RTAUDIO','KSDATARANGE_MUSIC',
    'STATIC_KSNODETYPE_INPUT_UNDEFINED','KS_VIDEO_FLAG_FIELD2',
    'KS_VIDEO_FLAG_FIELD1','BLUETOOTHLE_MIDI_SERVICE_UUID',
    'tagKS_DATARANGE_IMAGE','_KS_COLCON','STATIC_KSNODETYPE_STEREO_WIDE',
    '_KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT',
    'MAX_WST_VBI_LINES_PER_FIELD','STATIC_PINNAME_VIDEO_CC_CAPTURE',
    'STATIC_KSNODETYPE_SATELLITE_RECEIVER_AUDIO',
    'TELEPHONY_PROVIDERCHANGEOP',
    'KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION',
    'KSEVENT_CYCLIC_TIME',
    'STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_VIDEO',
    'KSAUDFNAME_MONO_MIX_VOLUME',
    'KSCAMERA_EXTENDEDPROP_FLASH_ON_ADJUSTABLEPOWER','KSNODETYPE_VOLUME',
    'KSEVENTSETID_Telephony',
    'KS_NABTS_GROUPID_TELEVISION_STATION_CONTENT_BASE',
    'KS_VBISAMPLINGRATE_4X_NABTS','STATIC_KSNODETYPE_SRC',
    'KSCAMERAPROFILE_FLAGS_FACEDETECTION','STATIC_KSPROPSETID_Cyclic',
    'KSCAMERAPROFILE_FLAGS_VARIABLEPHOTOSEQUENCE',
    'tagKS_DATAFORMAT_MPEGVIDEOINFO2','KSNODETYPE_MIDI_ELEMENT',
    'STATIC_AUDIO_EFFECT_TYPE_ACOUSTIC_ECHO_CANCELLATION',
    'AUDIO_EFFECT_TYPE_AUTOMATIC_GAIN_CONTROL',
    'KSPROPERTY_CAMERACONTROL_FLAGS_ASYNCHRONOUS',
    'PINNAME_VIDEO_VIDEOPORT','KSNODETYPE_RADIO_TRANSMITTER',
    'KSCATEGORY_VPMUX','tagKSCAMERA_METADATA_FRAMEILLUMINATION',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_AUTO',
    'STATIC_KSEVENTSETID_VIDCAP_TVAUDIO',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_CANDLELIGHT',
    'AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS',
    'KS_INTERLACE_DisplayModeBobOnly','KSPROPERTY_AEC',
    'STATIC_KSPROPSETID_AudioEngine','KSEVENT_TUNER_INITIATE_SCAN_S',
    'WST_BYTES_PER_LINE','KS_TVAUDIO_PRESET_LANG_C',
    'AEC_STATUS_FD_HISTORY_PREVIOUSLY_DIVERGED','KSAC3_SERVICE_VOICE_OVER',
    'KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_NEAREST','KS_SIZE_MASKS',
    '_KSPROPERTY_SPHLI','KSCAMERAPROFILE_Legacy','KSAUDFNAME_VIDEO_VOLUME',
    'STATIC_KSDATAFORMAT_TYPE_TEXT',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_LOW',
    'STATIC_KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER','_KSMPEGVID_RECT',
    'KSDATAFORMAT_SPECIFIER_JPEG_IMAGE',
    'KSCAMERA_PERFRAMESETTING_ITEM_HEADER',
    'KSCAMERA_EXTENDEDPROP_ISO_6400',
    'STATIC_KSCATEGORY_PREFERRED_WAVEIN_DEVICE',
    'STATIC_KSDATAFORMAT_SUBTYPE_L8_CUSTOM','KS_VIDEO_FLAG_WEAVE',
    'KS_SIZE_MPEG1VIDEOINFO','KSPROPERTY_AUDIOMODULE',
    'KSNODETYPE_VIDEO_PROCESSING','KSNODETYPE_SWMIDI',
    'STATIC_KSALGORITHMINSTANCE_SYSTEM_AGC','KS_DIBWIDTHBYTES',
    'tagKS_FRAME_INFO','KSJACK_SINK_CONNECTIONTYPE',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DST','tagKS_BITMAPINFOHEADER',
    'STATIC_KSNODETYPE_SPEAKER','KSCATEGORY_PREFERRED_MIDIOUT_DEVICE',
    'KSCAMERA_EXTENDEDPROP_EVCOMP_THIRDSTEP',
    'KSPROPERTY_VIDEODECODER_STATUS2_S','DDVPTYPE_E_HREFH_VREFH',
    'KSEVENTSETID_CameraAsyncControl',
    'STATIC_KSNODETYPE_1394_DV_STREAM_SOUNDTRACK',
    'KS_CameraControlAsyncOperation','KSCATEGORY_NETWORK',
    'KSCAMERA_EXTENDEDPROP_ISO_50','STATIC_KSNODETYPE_VIDEO_SELECTOR',
    'KSCAMERA_EXTENDEDPROP_WARMSTART_MODE_ENABLED',
    'STATIC_PINNAME_VIDEO_TIMECODE','STATIC_KSPROPSETID_Bibliographic',
    'KS_iMASK_COLORS','KSNODETYPE_LEVEL_CALIBRATION_NOISE_SOURCE',
    'tagKS_DATAFORMAT_VBIINFOHEADER',
    'DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_COLORKEY',
    'KS_MPEG2_SourceIsLetterboxed','DEFINE_USBAUDIO_MID_GUID',
    'KSNODETYPE_UPDOWN_MIX','STATIC_KSNODETYPE_EQUALIZATION_NOISE',
    'KSPROPERTY_TVAUDIO_CAPS_S','STATIC_KSCATEGORY_SYSAUDIO',
    'STATIC_KSDATAFORMAT_TYPE_STANDARD_PES_PACKET','KSAUDFNAME_3D_STEREO',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_AUTO',
    'KSNODETYPE_PROCESSING_MICROPHONE_ARRAY','KS_INTERLACE_IsInterlaced',
    'KS_VIDEOSTREAM_VBI','KSAUDFNAME_AUX_VOLUME',
    '_tagKSTELEPHONY_PROVIDERCHANGE','STATIC_PINNAME_CC_CAPTURE',
    'KSAUDFNAME_STEREO_MIX_MUTE','KSAUDFNAME_3D_CENTER',
    'STATIC_KSPROPSETID_Audio','KSEVENTSETID_VIDCAPNotify',
    'KSWAVE_INPUT_CAPABILITIES','KS_VBI_FLAG_FIELD2',
    'KSAUDIO_PRESENTATION_POSITION','STATIC_ENCAPIPARAM_PEAK_BITRATE',
    'STATIC_PINNAME_PREVIEW','KSPROPERTY_CAMERACONTROL_NODE_S',
    'CODECAPI_ALLSETTINGS','KSPROPERTY_TUNER','SPEAKER_TOP_CENTER',
    'KSAUDIO_SPEAKER_GROUND_FRONT_CENTER',
    'KS_NABTS_GROUPID_SYNDICATED_SHOW_ADVERTISER_BASE',
    '_KSAUDIO_PACKETSIZE_CONSTRAINTS','KS_SIZE_EGA_PALETTE',
    'KSPROPERTY_SYSAUDIO','STATIC_KSMEDIUMSETID_MidiBus',
    'KSNODETYPE_SPDIF_INTERFACE',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_FOCUSSTATE',
    'STATIC_KSNODETYPE_COMMUNICATION_SPEAKER','KSNODETYPE_MUTE',
    'PINNAME_VIDEO_TIMECODE','KSPROPERTY_VIDCAP_DROPPEDFRAMES',
    'STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_VIDEO',
    'KSAUDFNAME_TREBLE','_KSCAMERA_PROFILE_CONCURRENCYINFO',
    'STATIC_KSAUDFNAME_STEREO_MIX_VOLUME',
    'STATIC_KSNODETYPE_SPEAKERPHONE_NO_ECHO_REDUCTION',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT21',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MAT20',
    'KS_VIDEO_ALLOC_VPE_DISPLAY','KSAUDIO_SPEAKER_SUPER_WOOFER',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_MANUAL',
    'KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_HYPERFOCAL',
    'KS_DVD_CGMS_COPY_PROTECT_MASK','KS_INTERLACE_DisplayModeMask',
    'STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO',
    'STATIC_PINNAME_VIDEO_VIDEOPORT','KSPROPERTY_WAVE',
    'BLUETOOTH_MIDI_DATAIO_CHARACTERISTIC',
    'AUDIO_EFFECT_TYPE_SPEAKER_FILL','KSEVENTSETID_VPNotify',
    'KSCATEGORY_SYSAUDIO','STATIC_KSNODETYPE_VIDEO_INPUT_MTT',
    'STATIC_KSNODETYPE_PERSONAL_MICROPHONE','KS_DVD_SECTOR_PROTECT_MASK',
    'tagKS_MPEAUDIOINFO','KSRTAUDIO_BUFFER','KSDS3D_HRTF_COEFF_FORMAT',
    'SPEAKER_TOP_BACK_RIGHT','KS_VBICAP_PROTECTION_MV_DETECTED',
    'STATIC_EVENTSETID_CROSSBAR','KSNODETYPE_HEADSET_SPEAKERS',
    'KSEVENTSETID_CameraEvent','KSPROPERTY_VIDCAP_CAMERACONTROL',
    'KSNODEPROPERTY_AUDIO_3D_LISTENER','KSEVENT_CROSSBAR','KSNODETYPE_ADC',
    'KSCATEGORY_VIRTUAL','KSRTAUDIO_HWREGISTER32',
    'STATIC_KSPROPSETID_Itd3d','KSPROPERTY_VIDCAP_CROSSBAR',
    'KSCAMERA_EXTENDEDPROP_PHOTOTHUMBNAIL_DISABLE',
    'KSDATAFORMAT_SUBTYPE_MPEG1Packet',
    'STATIC_AUDIO_EFFECT_TYPE_BASS_MANAGEMENT','KS_DVDCOPYSTATE',
    'PROPSETID_VIDCAP_VIDEOPROCAMP',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_ASYNC',
    'PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST',
    'STATIC_KSDATAFORMAT_SUBTYPE_Line21_GOPPacket',
    'tagKS_DATARANGE_VIDEO_PALETTE','KSCATEGORY_REALTIME',
    'KSWAVE_COMPATCAPS','KS_DVD_CGMS_RESERVED_MASK',
    'KS_MPEG2_FilmCameraMode','KSPROPERTY_VBICAP',
    'STATIC_KSDATAFORMAT_SPECIFIER_JPEG_IMAGE','KSAUDFNAME_VIDEO',
    'KSNODETYPE_EQUALIZATION_NOISE','KSPROPERTY_CAMERACONTROL_NODE_S2',
    'KS_iBLUE','STATIC_KSDATAFORMAT_SUBTYPE_WMAUDIO2',
    'STATIC_KSDATAFORMAT_SUBTYPE_WMAUDIO3','KSNODETYPE_DEV_SPECIFIC',
    'KSVPSIZE_PROP','KSDATAFORMAT_SUBTYPE_L8',
    'STATIC_KSNODETYPE_OMNI_DIRECTIONAL_MICROPHONE',
    'KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S','KSAUDIO_MIX_CAPS',
    'KS_INTERLACE_1FieldPerSample','KSDATAFORMAT_SUBTYPE_MPEG1Payload',
    'STATIC_KSNODETYPE_HANDSET','AUDIO_EFFECT_TYPE_VIRTUAL_SURROUND',
    'KSAUDFNAME_RECORDING_SOURCE','KS_VIDEO_ALLOC_VPE_SYSTEM',
    'STATIC_KSCATEGORY_TVTUNER','KS_VBI_FLAG_FIELD1',
    'STATIC_AUDIO_EFFECT_TYPE_ENVIRONMENTAL_EFFECTS',
    'tagKSCAMERA_METADATA_ITEMHEADER','KSNODEPIN_AEC_CAPTURE_OUT',
    'KSEVENT_TVAUDIO','KSAUDFNAME_MIC_MUTE',
    'STATIC_KSCAMERAPROFILE_HDRWithWCGPhoto','KS_VideoControlFlags',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S',
    'KSAUDFNAME_MIC_VOLUME','tagKS_DATAFORMAT_H264VIDEOINFO',
    'STATIC_KSNODETYPE_VIDEO_OUTPUT_TERMINAL',
    'STATIC_KSNODETYPE_DYN_RANGE_COMPRESSOR',
    'tagKS_DATAFORMAT_VIDEOINFOHEADER2','KS_VIDEOSTREAM_TELETEXT',
    'STATIC_KSDATAFORMAT_TYPE_MPEG2_TRANSPORT',
    'tagKS_DATARANGE_MPEG2_VIDEO',
    'KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO',
    'KSCAMERA_EXTENDEDPROP_FOCUS_DISTANCE_MASK',
    'STATIC_KSPROPSETID_TelephonyTopology',
    'STATIC_KSNODETYPE_DESKTOP_MICROPHONE',
    'STATIC_AUDIO_SIGNALPROCESSINGMODE_MOVIE',
    'KSPROPERTY_WAVE_QUEUED_POSITION',
    'KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S',
    'STATIC_KSCATEGORY_AUDIO_GFX','KSAUDIO_POSITION','tagKS_H264VIDEOINFO',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_LANDSCAPE',
    'STATIC_PINNAME_VIDEO_NABTS_CAPTURE','KSDSOUND_3D_MODE_NORMAL',
    'KSCAMERA_PERFRAMESETTING_HEADER','SYSAUDIO_INSTANCE_INFO',
    'tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL',
    'KSRTAUDIO_GETREADPACKET_INFO','KSPROPERTY_VIDEOPROCAMP_NODE_S2',
    'KS_DIBSIZE','KSCATEGORY_ESCALANTE_PLATFORM_DRIVER',
    'KSEVENT_VIDCAPTOSTI','KSDATAFORMAT_SUBTYPE_LPCM_AUDIO',
    'EXTRACT_WAVEFORMATEX_ID','_KSPROPERTY_SPPAL',
    'KSNODETYPE_TV_TUNER_AUDIO',
    'KSALGORITHMINSTANCE_SYSTEM_ACOUSTIC_ECHO_CANCEL',
    'KSMUSIC_TECHNOLOGY_SWSYNTH','KSCAMERAPROFILE_PhotoSequence',
    'STATIC_KSALGORITHMINSTANCE_SYSTEM_MICROPHONE_ARRAY_PROCESSOR',
    'KS_VBI_FLAG_MV_PRESENT','KSNODETYPE_LINE_CONNECTOR',
    'KSCAMERA_EXTENDEDPROP_FACEDETECTION_PHOTO',
    'PROPSETID_VIDCAP_VIDEODECODER','KSDATAFORMAT_SUBTYPE_VPVBI',
    'KSNODETYPE_HEADSET_MICROPHONE','KSDATAFORMAT_SPECIFIER_VC_ID',
    'KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_FULLRANGE','EXTRACT_USBAUDIO_MID',
    'STATIC_KSPROPSETID_AudioBufferDuration','VRAM_SURFACE_INFO',
    'KSPROPERTYSETID_ExtendedCameraControl',
    'AUDIO_SIGNALPROCESSINGMODE_NOTIFICATION','EPcxGeoLocation',
    'KSCAMERA_EXTENDEDPROP_HISTOGRAM_ON',
    'STATIC_KSDATAFORMAT_SPECIFIER_ANALOGVIDEO',
    'KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_MANUAL',
    'KSPROPERTY_TUNER_MODE_CAPS_S',
    'STATIC_KSEVENTSETID_DynamicFormatChange',
    'KSCAMERA_EXTENDEDPROP_FOCUS_MODE_ADVANCED_MASK',
    'tagKSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER',
    'KS_VideoStreamingHINTs','KSDATAFORMAT_DSOUND','PINNAME_CAPTURE',
    'STATIC_KSAUDFNAME_STEREO_MIX_MUTE',
    'STATIC_KSCAMERAPROFILE_BalancedVideoAndPhoto','KSNODETYPE_DVD_AUDIO',
    'DEFINE_USB_TERMINAL_GUID','AUDIO_CURVE_TYPE',
    'KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_AUTO',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DTS',
    'STATIC_KSNODETYPE_DEV_SPECIFIC',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_FLASH','KS_AM_SimpleRateChange',
    'STATIC_PROPSETID_EXT_DEVICE','tagKSCAMERA_METADATA_CAPTURESTATS',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_MANUAL',
    'KSDATAFORMAT_SUBTYPE_IEC61937_ATRAC','STATIC_KSCATEGORY_VBICODEC',
    'tagKS_DATARANGE_H264_VIDEO',
    'STATIC_KSCATEGORY_ESCALANTE_PLATFORM_DRIVER',
    'STATIC_KSAUDFNAME_LINE_VOLUME','STATIC_KSAUDFNAME_MIC_MUTE',
    'STATIC_AUDIO_EFFECT_TYPE_EQUALIZER','WAVEFORMATEXTENSIBLE',
    'DEVPKEY_KsAudio_PacketSize_ConstraINTs','KSCATEGORY_CROSSBAR',
    'KSNODETYPE_NOISE_SUPPRESS','KSPROPERTY_MPEG2VID',
    'KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_SEQUENCE_EXCLUSIVE_WITH_RECORD',
    'KSCAMERA_EXTENDEDPROP_FILTERSCOPE','KSAUDIO_DYNAMIC_RANGE',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_WHITEBALANCE','KSNODETYPE_CHORUS',
    'KSPROPSETID_AudioModule','KSCAMERA_EXTENDEDPROP_FACEDETECTION_ON',
    'DEFINE_USBAUDIO_PRODUCT_NAME','KSCAMERA_EXTENDEDPROP_EVCOMP_HALFSTEP',
    'KSDATAFORMAT_SPECIFIER_AC3_AUDIO','KSAUDFNAME_MONO_MIX',
    'VIDEOENCODER_BITRATE_MODE','tagKSCAMERA_EXTENDEDPROP_HEADER',
    'PINNAME_VIDEO_CAPTURE','KSDATAFORMAT_TYPE_ANALOGAUDIO',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_SCENEMODE',
    'KSCameraProfileSensorType_ImageSegmentation',
    'KS_CC_SUBSTREAM_SERVICE_T3','STATIC_KSNODETYPE_ANALOG_CONNECTOR',
    'STATIC_PINNAME_IMAGE','KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_ON',
    'STATIC_PROPSETID_VIDCAP_VIDEOENCODER',
    'KSPROPERTY_CAMERACONTROL_FLASH_ON','KSDSOUND_BUFFER_STATIC',
    'INIT_USBAUDIO_MID','KS_47NABTS_SCALER',
    'STATIC_KSDATAFORMAT_SPECIFIER_LPCM_AUDIO','KSMPEGVIDMODE_SCALE',
    'KSDATAFORMAT_SUBTYPE_L16','SYSAUDIO_FLAGS_CLEAR_PREFERRED',
    'KSDATAFORMAT_TYPE_MPEG2_PES','KSDATAFORMAT_SUBTYPE_L8_IR',
    'KSDS3D_LISTENER_ALL','STATIC_KSAUDFNAME_CD_MUTE',
    'tagTRANSPORTBASICPARMS','STATIC_KSINTERFACESETID_Media',
    'STATIC_KSAUDFNAME_ALTERNATE_MICROPHONE',
    'STATIC_AUDIO_EFFECT_TYPE_NOISE_SUPPRESSION',
    'KSPROPSETID_Sysaudio_Pin','KSNODETYPE_3D_EFFECTS',
    'KSAUDIO_SPEAKER_GROUND_FRONT_RIGHT','KSVPSURFACEPARAMS',
    'KSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_S',
    'STATIC_AUDIO_EFFECT_TYPE_LOUDNESS_EQUALIZER',
    'KSNODEPIN_AEC_RENDER_IN','tagKSCAMERA_EXTENDEDPROP_PHOTOMODE',
    'KSMICARRAY_MICTYPE','KSPROPERTY_CAMERA_PHOTOTRIGGERTIME_FLAGS',
    'STATIC_KSNODETYPE_RADIO_RECEIVER','STATIC_KSCAMERAPROFILE_VideoHDR8',
    'KSMEDIUMSETID_VPBus','PROPSETID_ALLOCATOR_CONTROL',
    'KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_OFF',
    'KSDEVICE_PROFILE_TYPE_CAMERA','STATIC_PROPSETID_VIDCAP_VIDEOPROCAMP',
    'KS_AMPixAspectRatio','KS_MAX_SIZE_MPEG1_SEQUENCE_INFO',
    'KSPROPSETID_VPConfig','tagKS_VBIINFOHEADER',
    'KSCAMERA_EXTENDEDPROP_ISO_MANUAL','STATIC_CODECAPI_AUDIO_ENCODER',
    'KSPROPSETID_BtAudio','KSCAMERA_EXTENDEDPROP_VIDEOHDR_AUTO',
    'KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY32',
    'KSDSOUND_BUFFER_CTRL_FREQUENCY','KSDSOUND_BUFFER_CTRL_VOLUME',
    'STATIC_PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION',
    'STATIC_KSNODETYPE_CABLE_TUNER_AUDIO','CONSTRICTOR_OPTION',
    'KS_WIDTHBYTES','KSDS3D_HRTF_FILTER_METHOD','KSDATAFORMAT_TYPE_MIDI',
    'KS_AM_Step','PINNAME_VIDEO_VIDEOPORT_VBI','KS_AM_MaxFullDataRate',
    'KS_VBICAP_PROTECTION_MV_PRESENT',
    'STATIC_KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_VIDEO',
    'KS_VIDEODECODER_FLAGS','VRAM_SURFACE_INFO_PROPERTY_S',
    'STATIC_KSNODETYPE_SUPERMIX','STATIC_KSPROPSETID_Linear',
    'STATIC_PROPSETID_VIDCAP_CAMERACONTROL',
    'STATIC_PINNAME_DISPLAYPORT_OUT','KSAUDIO_QUALITY_PC',
    'KS_SIZE_MPEGVIDEOINFO2','STATIC_KSDATAFORMAT_SUBTYPE_CC',
    'STATIC_KSNODETYPE_PROCESSING_MICROPHONE_ARRAY',
    'tagKSCAMERA_EXTENDEDPROP_VALUE','STATIC_CODECAPI_ALLSETTINGS',
    'KSDS3D_HRTF_INIT_MSG','PINNAME_VIDEO_VBI',
    'STATIC_KSDATAFORMAT_SUBTYPE_L8','KSAUDIO_SPEAKER_SURROUND',
    'KSCAMERA_EXTENDEDPROP_ISO_AUTO','STATIC_PINNAME_VIDEO_ANALOGVIDEOIN',
    'STATIC_KSDATAFORMAT_SUBTYPE_ALAW','PINNAME_VIDEO_NABTS',
    'STATIC_KSNODETYPE_MIDI_JACK','STATIC_KSDATAFORMAT_TYPE_ANALOGVIDEO',
    'SPEAKER_FRONT_RIGHT_OF_CENTER','PINNAME_VIDEO_NABTS_CAPTURE',
    'KSCATEGORY_PREFERRED_WAVEIN_DEVICE','_tagKSJACK_DESCRIPTION2',
    'KSCAMERA_EXTENDEDPROP_VIDEOHDR_OFF',
    'KSDATAFORMAT_SUBTYPE_IEC61937_AAC','KSPROPERTY_EXTXPORT',
    'KSWAVE_VOLUME','INIT_USBAUDIO_PID','KSPROPERTY_AUDIOSIGNALPROCESSING',
    'KSPROPERTY_VBICODECFILTERING_STATISTICS_COMMON_PIN_S',
    'KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_ON',
    'KSCameraProfileSensorType_Depth','KSNODETYPE_SPEAKER',
    'EVENTSETID_CROSSBAR','KS_iEGA_COLORS','KSRTAUDIO_BUFFER_PROPERTY',
    'KSNODETYPE_MUX','STATIC_KSNODETYPE_PROLOGIC_DECODER',
    'KS_NABTS_GROUPID_SYNDICATED_SHOW_CONTENT_BASE',
    'KSPROPERTY_EXTXPORT_NODE_S','KSDATAFORMAT_SUBTYPE_SDDS_AUDIO',
    'STATIC_KSDATAFORMAT_SUBTYPE_DSS_AUDIO','STATIC_KSCATEGORY_VIRTUAL',
    'STATIC_AUDIO_EFFECT_TYPE_BASS_BOOST',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_FOCUS',
    'KSCAMERA_EXTENDEDPROP_SECUREMODE_ENABLED',
    'STATIC_KSCATEGORY_AUDIO_DEVICE','KSAC3_SERVICE_MAIN_AUDIO',
    'KSEVENTSETID_VIDCAP_TVAUDIO','SPEAKER_BACK_CENTER',
    'KSAUDIO_SPEAKER_2POINT1',
    'DEFINE_KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS',
    'KSCATEGORY_TVAUDIO','KSDSOUND_BUFFER_LOCHARDWARE',
    'KSNODETYPE_PARAMETRIC_EQUALIZER',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_OFF',
    'AUDIO_SIGNALPROCESSINGMODE_MEDIA',
    'STATIC_KSDATAFORMAT_SPECIFIER_IMAGE',
    'STATIC_KSEVENTSETID_CameraAsyncControl',
    'KSDATAFORMAT_SUBTYPE_STANDARD_MPEG2_AUDIO',
    'STATIC_KSAUDFNAME_CD_VOLUME','STATIC_KSNODETYPE_MINIDISK',
    'KSCAMERA_EXTENDEDPROP_FOCUS_MODE_MASK','tagKS_DATARANGE_VIDEO2',
    'STATIC_KSNODETYPE_TONE','STATIC_KSNODETYPE_DIGITAL_AUDIO_INTERFACE',
    'PROPSETID_VIDCAP_VIDEOCOMPRESSION',
    'KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_OFF',
    'KSNODETYPE_CABLE_TUNER_AUDIO','KSNODEPROPERTY_AUDIO_CHANNEL',
    'KSDATAFORMAT_SPECIFIER_DSOUND',
    'KSDATAFORMAT_SPECIFIER_DIALECT_MPEG2_AUDIO',
    'KSAUDIO_SPEAKER_7POINT1_WIDE','STATIC_KSNODETYPE_ANALOG_TAPE',
    'KSCAMERA_EXTENDEDPROP_PHOTOMODE_NORMAL','KSDSOUND_BUFFER_CTRL_PAN',
    'STATIC_KSAUDFNAME_MIC_IN_VOLUME','PROPSETID_VIDCAP_VIDEOENCODER',
    'KSDSOUND_BUFFER_PRIMARY','KS_INTERLACE_DisplayModeWeaveOnly',
    'tagKSCAMERA_EXTENDEDPROP_CAMERAOFFSET',
    'AUDIO_EFFECT_TYPE_LOUDNESS_EQUALIZER','EVENTSETID_VIDEODECODER',
    'STATIC_KSDATAFORMAT_TYPE_NABTS','KSDATAFORMAT_SPECIFIER_VIDEOINFO2',
    'KSAUDIO_SPEAKER_1POINT1',
    'KSCAMERAPROFILE_FLAGS_PREVIEW_RES_MUSTMATCH',
    'STATIC_KSDATAFORMAT_SPECIFIER_VIDEOINFO',
    '_VBICODECFILTERING_SCANLINES','KSAUDFNAME_LINE_IN',
    'KSAC3_SERVICE_EMERGENCY_FLASH','STATIC_KSNODETYPE_VIDEO_OUTPUT_MTT',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL_PLUS_ATMOS',
    'KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_AUTO',
    'KSNODEPROPERTY_AUDIO_PROPERTY',
    'KSPROPERTY_VBICODECFILTERING_STATISTICS_CC_S',
    'STATIC_KSNODETYPE_MICROPHONE_ARRAY','KSCATEGORY_TEXT',
    'KSAUDFNAME_MIDI_VOLUME','AUDIO_EFFECT_TYPE_EQUALIZER',
    'KSAC3_ROOM_TYPE','SYSAUDIO_CREATE_VIRTUAL_SOURCE',
    '_tagKSTOPOLOGY_ENDPOINTID','STATIC_KSMUSIC_TECHNOLOGY_SQSYNTH',
    'KSAUDIO_SPEAKER_MONO',
    'DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_DISPLAYCHANGE',
    'KSAUDFNAME_MASTER_VOLUME',
    'KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_MASK',
    'STATIC_KSDATAFORMAT_SUBTYPE_MPEG','KSPROPERTY_VIDEOCONTROL_CAPS_S',
    'KS_SIZE_VIDEOHEADER','KSAUDFNAME_PC_SPEAKER',
    'KSCAMERA_EXTENDEDPROP_MetadataAlignment',
    'STATIC_KSNODETYPE_SYNTHESIZER','STATIC_KSEVENTSETID_EXTDEV_Command',
    'KSDS3D_HRTF_FILTER_FORMAT_MSG',
    'KSCAMERA_EXTENDEDPROP_VIDEOTEMPORALDENOISING_AUTO','_DDPIXELFORMAT',
    'KSCAMERA_EXTENDEDPROP_VIDEOSTABILIZATION_AUTO',
    'KSCAMERA_EXTENDEDPROP_FLASH_MODE_MASK','SPEAKER_TOP_BACK_CENTER',
    'STATIC_KSMUSIC_TECHNOLOGY_PORT',
    'STATIC_AUDIO_EFFECT_TYPE_VIRTUAL_SURROUND',
    'STATIC_KSDATAFORMAT_SUBTYPE_MPEG1Video','_KS_DVDCOPY_BUSKEY',
    'KSWAVETABLE_WAVE_DESC','_KSAUDIOMODULE_DESCRIPTOR',
    'KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PERF_MASK',
    'KSDATAFORMAT_SUBTYPE_SUBPICTURE',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_ATRAC',
    'KSDEVICE_PROFILE_TYPE_UNKNOWN',
    'KSCAMERA_EXTENDEDPROP_FLASH_MULTIFLASHSUPPORTED',
    'NABTS_PAYLOAD_PER_LINE','KSCAMERA_PERFRAMESETTING_ITEM_TYPE',
    'KSDATAFORMAT_SUBTYPE_RIFF','KSNODETYPE_LEGACY_AUDIO_CONNECTOR',
    'STATIC_KSAUDFNAME_MONO_OUT_MUTE','KSMPEGVIDMODE_LTRBOX',
    'KS_TVAUDIO_PRESET_STEREO','EPcxGenLocation',
    'STATIC_KSDATAFORMAT_SUBTYPE_DRM','KSCAMERA_EXTENDEDPROP_ZOOM_SMOOTH',
    'KSPROPERTY_BTAUDIO','_KSCAMERA_PROFILE_PININFO',
    'KSPROPERTY_TUNER_MODES','IS_VALID_WAVEFORMATEX_GUID',
    'KSEVENT_LOOPEDSTREAMING','KSCAMERA_EXTENDEDPROP_ISO_1600',
    '_VBICODECFILTERING_STATISTICS_COMMON_PIN',
    'KSCAMERA_EXTENDEDPROP_METADATA_ALIGNMENTREQUIRED',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_MLP',
    'KSDSOUND_3D_MODE_DISABLE','KSAUDFNAME_VOLUME_CONTROL','PINNAME_IMAGE',
    'KSCAMERA_EXTENDEDPROP_FLASH_AUTO','KS_TVTUNER_CHANGE_END_TUNE',
    'KSPROPERTY_VIDCAP_VIDEOENCODER','tagKS_DATARANGE_VIDEO_VBI',
    'KSNODETYPE_TONE','PINNAME_HDMI_OUT','KSCAMERA_EXTENDEDPROP_ISO_100',
    'KSAUDIO_MIC_ARRAY_GEOMETRY','STATIC_KSNODETYPE_TELEPHONY_UNDEFINED',
    'STATIC_KSDATAFORMAT_TYPE_AUXLine21Data',
    'KSDSOUND_BUFFER_CTRL_POSITIONNOTIFY',
    'STATIC_AUDIO_EFFECT_TYPE_SPEAKER_COMPENSATION',
    'STATIC_KSNODETYPE_SPDIF_INTERFACE',
    'STATIC_KSNODETYPE_EXTERNAL_UNDEFINED','KSPROPERTY_TUNER_STANDARD_S',
    'KSCATEGORY_DRM_DESCRAMBLE','KSPROPERTY_TUNER_INPUT_S',
    'INIT_MMREG_PID','AUDIO_EFFECT_TYPE_SPEAKER_COMPENSATION',
    'PINNAME_VIDEO_TELETEXT','STATIC_KSNODETYPE_DAT_IO_DIGITAL_AUDIO_TAPE',
    'KSPROPSETID_Acoustic_Echo_Cancel',
    'STATIC_KSDATAFORMAT_SUBTYPE_AC3_AUDIO',
    'KSCAMERA_EXTENDEDPROP_SECUREMODE_DISABLED','STATIC_KSCATEGORY_AUDIO',
    'KSCAMERA_MetadataId','KSCAMERA_EXTENDEDPROP_CAPS_MASK',
    'KSPROPERTY_CAMERACONTROL_FLAGS_MANUAL','STATIC_PINNAME_VIDEO_PREVIEW',
    'KSDATAFORMAT_SUBTYPE_DSS_VIDEO',
    'KS_NABTS_GROUPID_NETWORK_WIDE_ADVERTISER_BASE',
    'KSPROPERTY_TIMECODE_NODE_S','KSPROPERTY_TIMECODE',
    'KSCATEGORY_ENCODER','STATIC_ENCAPIPARAM_BITRATE_MODE',
    'KS_INTERLACE_FieldPatField2Only',
    'KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S','KSNODETYPE_HDMI_INTERFACE',
    'KSNODETYPE_EQUALIZER','STATIC_KSAUDFNAME_LINE_IN',
    'DEFINE_KSPROPERTY_PREFERRED_CAPTURE_SURFACE',
    'DEFINE_KSPROPERTY_ITEM_DISPLAY_ADAPTER_GUID',
    'KSAC3_SERVICE_NO_DIALOG','STATIC_KSDATAFORMAT_SUBTYPE_MPEG1Packet',
    'KSPROPERTY_EXTENSION_UNIT','PROPSETID_VIDCAP_DROPPEDFRAMES',
    'STATIC_KSPROPSETID_AudioDecoderOut',
    'AUDIO_EFFECT_TYPE_NOISE_SUPPRESSION','PINNAME_SPDIF_OUT',
    'STATIC_KSNODETYPE_ACOUSTIC_ECHO_CANCEL','KSPROPSETID_Linear',
    'CODECAPI_CHANGELISTS','KSDS3D_BUFFER_CONE_ANGLES','KSPROPERTY_AC3',
    'KSDATAFORMAT_SPECIFIER_MPEG2_VIDEO','KSNODEPIN_STANDARD_IN',
    'STATIC_KSDATAFORMAT_SUBTYPE_IEC61937_WMA_PRO',
    'KSCAMERA_EXTENDEDPROP_METADATA_MEMORYTYPE_MASK',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL',
    'KS_PhysicalConnectorType','STATIC_KSNODETYPE_MICROPHONE',
    'KSNODETYPE_TELEPHONE','STATIC_KSMUSIC_TECHNOLOGY_SWSYNTH',
    'KSCAMERA_EXTENDEDPROP_VIDEOHDR_ON','tagKS_DATARANGE_ANALOGVIDEO',
    'KSAUDFNAME_PC_SPEAKER_VOLUME','NABTS_BYTES_PER_LINE',
    'STATIC_KSNODETYPE_AUDIO_LOOPBACK','ENCAPIPARAM_BITRATE_MODE',
    'STATIC_KSPROPSETID_Sysaudio','STATIC_KSPROPSETID_WaveTable',
    'KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S',
    'STATIC_PROPSETID_VIDCAP_TVAUDIO','_KS_DVDCOPY_DISCKEY',
    'KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_HYPERFOCAL',
    '_tagKSAUDIOENGINE_BUFFER_SIZE_RANGE',
    'DEFINE_KSPROPERTY_CURRENT_CAPTURE_SURFACE','tagKS_VIDEOINFOHEADER',
    'KSEVENTSETID_SoundDetector','STATIC_KSCATEGORY_REALTIME',
    'KSPROPERTY_CAMERACONTROL_FLAGS_RELATIVE',
    'STATIC_KSCAMERAPROFILE_HDRWithWCGVideo','KS_BI_RGB',
    'KS_iPALETTE_COLORS','_VBICODECFILTERING_CC_SUBSTREAMS',
    'STATIC_KSAUDFNAME_3D_CENTER','KSCATEGORY_WDMAUD_USE_PIN_NAME',
    'CODECAPI_CURRENTCHANGELIST','KSCAMERA_EXTENDEDPROP_SCENEMODE_BACKLIT',
    'tagKSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER',
    'KSNODETYPE_DRM_DESCRAMBLE','KSNODETYPE_DYN_RANGE_COMPRESSOR',
    'STATIC_KSPROPSETID_SoundDetector','KSPROPSETID_TelephonyTopology',
    'STATIC_PROPSETID_TIMECODE_READER','KSPROPERTY_TUNER_SCAN_STATUS_S',
    'STATIC_PINNAME_VIDEO_NABTS','KSNODETYPE_PHONOGRAPH','_NABTS_BUFFER',
    'STATIC_KSAUDFNAME_WAVE_VOLUME',
    'KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_AUTO',
    'STATIC_KSDATAFORMAT_SUBTYPE_L16_IR','KSPROPERTY_TOPOLOGYNODE',
    'KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_HDR',
    'KSNODETYPE_1394_DV_STREAM_SOUNDTRACK','KSPROPERTY_SYSAUDIO_PIN',
    'STATIC_KSNODETYPE_MUX','TRANSPORT_STATE',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_NIGHT','STATIC_KSCATEGORY_TVAUDIO',
    'KSPROPERTY_CAMERACONTROL_FLASH_AUTO','AEC_MODE_HALF_DUPLEX',
    'STATIC_KSPROPSETID_DirectSound3DListener',
    'KSDATAFORMAT_SUBTYPE_MIDI_BUS','STATIC_KSAUDFNAME_MIDI',
    'KSPROPERTY_EXTDEVICE_S','KSMPEGVIDMODE_PANSCAN',
    'STATIC_KSDATAFORMAT_SUBTYPE_DTS_AUDIO',
    'KSCAMERA_EXTENDEDPROP_FACEAUTH_MODE_DISABLED',
    'KSAUDIO_SPEAKER_GROUND_REAR_RIGHT','KSEVENT_AUDIO_CONTROL_CHANGE',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_PORTRAIT',
    'KSDATAFORMAT_SPECIFIER_LPCM_AUDIO','_KSAUDIOMODULE_NOTIFICATION',
    'KSDATAFORMAT_SUBTYPE_MPEG2_VIDEO','KSDS3D_HRTF_FILTER_VERSION',
    'KSNODETYPE_DEMUX','KSAUDIO_CPU_RESOURCES_HOST_CPU',
    'KSCAMERA_EXTENDEDPROP_ADVANCEDPHOTO_ULTRALOWLIGHT',
    'STATIC_KSAUDFNAME_MONO_OUT_VOLUME','KS_MPEG2_DoPanScan',
    'STATIC_KSAUDFNAME_VIDEO','KSAC3_SERVICE_HEARING_IMPAIRED',
    '_KS_DVD_YUV','KSNODEPIN_SUM_MUX_OUT','KSPROPERTY_FMRX_CONTROL',
    'KSCAMERA_EXTENDEDPROP_METADATA_SYSTEMMEMORY',
    'STATIC_KSDATAFORMAT_SUBTYPE_DSS_VIDEO',
    'STATIC_KSAUDFNAME_CD_IN_VOLUME','KSPROPERTY_VIDCAP_VIDEODECODER',
    '_NABTS_BUFFER_LINE','_CC_BYTE_PAIR','KSPROPSETID_AudioBufferDuration',
    '_KSAUDIOMODULE_PROPERTY','KSPROPSETID_TSRateChange',
    'KSAUDFNAME_MONO_OUT_MUTE','_KS_DVDCOPY_SET_COPY_STATE',
    'KSPROPERTY_AUDIOGFX','JACKDESC2_PRESENCE_DETECT_CAPABILITY',
    'STATIC_KSDATAFORMAT_SPECIFIER_AC3_AUDIO','KS_VIDEOSTREAM_EDS',
    'KSAUDIO_SPEAKER_7POINT1_SURROUND','KSNODETYPE_DISPLAYPORT_INTERFACE',
    'KSNODETYPE_PROLOGIC_DECODER','STATIC_KSDATAFORMAT_TYPE_IMAGE',
    'STATIC_KSDATAFORMAT_TYPE_MPEG2_PES',
    'tagKSCAMERA_EXTENDEDPROP_ROI_EXPOSURE','KSPROPSETID_Mpeg2Vid',
    'KSCAMERA_EXTENDEDPROP_FACEDETECTION_MASK',
    'KSPROPSETID_DrmAudioStream',
    'STATIC_AUDIO_EFFECT_TYPE_VIRTUAL_HEADPHONES',
    'tagKS_DATARANGE_MPEG1_VIDEO','KSCAMERA_PERFRAMESETTING_CUSTOM_ITEM',
    'KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST','PINNAME_VIDEO_STILL',
    'KSNODETYPE_PROLOGIC_ENCODER','KSDATARANGE_AUDIO','KSEVENT_TELEPHONY',
    'PROPSETID_VIDCAP_CAMERACONTROL_IMAGE_PIN_CAPABILITY',
    'STATIC_KSAUDFNAME_MONO_MIX_MUTE','KS_iMAXBITS',
    'AUDIO_EFFECT_TYPE_DYNAMIC_RANGE_COMPRESSION','STATIC_KSCATEGORY_TEXT',
    'STATIC_PROPSETID_VIDCAP_DROPPEDFRAMES','KSAUDDECOUTMODE_SPDIFF',
    'NABTS_LINES_PER_BUNDLE','STATIC_KSAUDFNAME_WAVE_IN_VOLUME',
    'STATIC_KSDATAFORMAT_SUBTYPE_ANALOG',
    'DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_PALETTE',
    'KS_VIDEO_ALLOC_VPE_AGP','KSNODETYPE_EXTERNAL_UNDEFINED',
    'KSCATEGORY_ACOUSTIC_ECHO_CANCEL','_tagKSTELEPHONY_CALLINFO',
    'KS_VBI_FLAG_FRAME','STATIC_PINNAME_SPDIF_OUT','KSNODETYPE_PEAKMETER',
    'KSAC3_SERVICE_VISUALLY_IMPAIRED','STATIC_KSDATAFORMAT_TYPE_MUSIC',
    'tagKS_DATARANGE_VIDEO','KSCameraProfileSensorType_Custom',
    'KSPROPSETID_AudioSignalProcessing','KSNODETYPE_OUTPUT_UNDEFINED',
    'KSNODEPROPERTY_AUDIO_DEV_SPECIFIC','STATIC_KSAUDFNAME_PC_SPEAKER',
    'KSAUDFNAME_MONO_OUT_VOLUME','KS_MPEG2_WidescreenAnalogOut',
    'KSPROPERTY_CAMERACONTROL_S2','KSNODETYPE_DELAY',
    'KSPROPERTY_TUNER_MODE_S','KS_MPEG2_LetterboxAnalogOut',
    'STATIC_KSCATEGORY_CROSSBAR','STATIC_KSNODETYPE_SPEAKERS_STATIC_JACK',
    'KSPROPERTY_CROSSBAR_PININFO_S','SPEAKER_TOP_FRONT_CENTER',
    'CODECAPI_AUDIO_ENCODER','STATIC_KSMETHODSETID_Wavetable',
    'KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK',
    'STATIC_KSAUDFNAME_MIDRANGE','KS_DVD_CGMS_COPY_ONCE','DDPF_FOURCC',
    'KSPROPERTY_VBICODECFILTERING',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_EXPOSURETIME',
    'KSPROPSETID_Sysaudio','tagKS_RGBQUAD','KSNODETYPE_SRC',
    'CAPTURE_MEMORY_ALLOCATION_FLAGS',
    'KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER',
    'KSDATAFORMAT_SUBTYPE_IEC61937_DTS',
    'STATIC_KSDATAFORMAT_SPECIFIER_MPEG1_VIDEO',
    'KSCAMERA_PERFRAMESETTING_AUTO','KSRTAUDIO_HWREGISTER',
    'KSAUDFNAME_WAVE_IN_VOLUME','KSDATAFORMAT_SUBTYPE_VPVideo',
    'KSPROPSETID_CopyProt','KS_AMCONTROL_COLORINFO_PRESENT',
    'KSCAMERA_EXTENDEDPROP_FOCUSSTATE',
    'STATIC_KSPROPSETID_VBICodecFiltering',
    'STATIC_KSPROPSETID_AudioSignalProcessing','_NABTSFEC_BUFFER',
    'KSAUDIO_MIXLEVEL','KSNODETYPE_REVERB','KS_BI_BITFIELDS',
    'KSPROPERTY_EXTXPORT_S','KS_VIDEO_FLAG_REPEAT_FIELD',
    'SPEAKER_RESERVED','KSPROPSETID_Hrtf3d',
    'STATIC_KSNODETYPE_RADIO_TRANSMITTER','KSCOMPONENTID_USBAUDIO',
    'NABTS_BUFFER_PICTURENUMBER_SUPPORT',
    'STATIC_KSEVENTSETID_LoopedStreaming','KSDATAFORMAT_SPECIFIER_IMAGE',
    'KS__DIBSIZE','KS_BI_RLE8','PROPSETID_TUNER',
    'AUDIOMODULE_MAX_NAME_CCH_SIZE','KSAC3_DIALOGUE_LEVEL',
    'STATIC_KSNODETYPE_3D_EFFECTS',
    'KSCAMERA_EXTENDEDPROP_FOCUS_RANGE_NORMAL','KS_BI_RLE4',
    'STATIC_KSDATAFORMAT_SUBTYPE_RIFF',
    'KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_ON',
    'KSCAMERA_EXTENDEDPROP_OPTIMIZATION_PRIMARYUSE_MASK',
    'KSAUDFNAME_WAVE_VOLUME','STATIC_KSCAMERAPROFILE_FaceAuth_Mode',
    'STATIC_KSMUSIC_TECHNOLOGY_WAVETABLE','PROPSETID_VIDCAP_CROSSBAR',
    'STATIC_AUDIO_EFFECT_TYPE_SPEAKER_FILL',
    'STATIC_KSPROPSETID_VBICAP_PROPERTIES',
    'KSCAMERA_EXTENDEDPROP_SCENEMODE_SUNSET',
    'KSCAMERA_METADATA_CAPTURESTATS_FLAG_ISOSPEED',
    'KSDATAFORMAT_SUBTYPE_IMAGE_RGB32',
    'STATIC_KSDATAFORMAT_SUBTYPE_MJPG_DEPTH','KSCATEGORY_MULTIPLEXER',
    'KSAUDIO_MICROPHONE_COORDINATES','STATIC_KSPROPSETID_FMRXControl',
    'tagTIMECODE_SAMPLE','STATIC_KSDATAFORMAT_SUBTYPE_MIDI',
    'KSPROPERTY_VBICODECFILTERING_CC_SUBSTREAMS_S','KSPROPERTY_COPYPROT',
    'KSPROPERTY_TUNER_CAPS_S','STATIC_ENCAPIPARAM_BITRATE','PTIMECODE',
    'KSNODEPIN_AEC_RENDER_OUT',
    'KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION32',
    'KSCAMERA_EXTENDEDPROP_FLAG_MASK','KS_TVAUDIO_MODE_LANG_A',
    'KS_TVAUDIO_MODE_LANG_C','KS_TVAUDIO_MODE_LANG_B',
    'AUDIO_SIGNALPROCESSINGMODE_SPEECH','_KSDEVICE_PROFILE_INFO',
    'AUDIO_EFFECT_TYPE_BASS_MANAGEMENT','KSNODETYPE_VIDEO_INPUT_TERMINAL',
    'KS_CompressionCaps','STATIC_PINNAME_VIDEO_VIDEOPORT_VBI',
    'KSNODEPIN_DEMUX_IN','STATIC_KSNODETYPE_DOWN_LINE_PHONE',
    'KSDATAFORMAT_SUBTYPE_D16',
    'STATIC_BLUETOOTH_MIDI_DATAIO_CHARACTERISTIC',
    'KSCAMERA_EXTENDEDPROP_VFR_OFF','KSPROPERTY_CAMERACONTROL_FLASH_OFF',
    'KSCAMERA_EXTENDEDPROP_ZOOM_DIRECT','EVENTSETID_TUNER',
    'KSDATAFORMAT_SUBTYPE_MPEG_HEAAC',
    'KS_NABTS_GROUPID_LOCAL_CABLE_SYSTEM_ADVERTISER_BASE',
    'KSDATAFORMAT_SPECIFIER_H264_VIDEO','STATIC_KSNODETYPE_LINE_CONNECTOR',
    'KSPROPERTY_EXTDEVICE','KS_MPEG2_DVB_UserData',
    'STATIC_KSAUDFNAME_CD_AUDIO','_KS_COPY_MACROVISION',
    'STATIC_KSPROPSETID_DirectSound3DBuffer',
    '_KSAUDIO_PACKETSIZE_CONSTRAINTS2','EXTRACT_USB_TERMINAL',
    'KSCATEGORY_MICROPHONE_ARRAY_PROCESSOR','STATIC_KSPROPSETID_BtAudio',
    'KSCameraProfileSensorType_PoseTracking',
    'KSPROPERTY_CAMERACONTROL_FLAGS_ABSOLUTE','KSPROPSETID_RtAudio',
    'KS_VIDEO_FLAG_FIELD_MASK','PINNAME_VIDEO_PREVIEW',
    'KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL',
    'KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY','tagKS_AMVPDIMINFO',
    'tagKS_AMVPSIZE','STATIC_KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE',
    'STATIC_KSPROPSETID_FMRXTopology',
    'STATIC_KSCATEGORY_PREFERRED_MIDIOUT_DEVICE',
    'KSCAMERA_EXTENDEDPROP_CAPS_CANCELLABLE',
    'KSDATAFORMAT_SUBTYPE_MJPG_CUSTOM',
    'STATIC_KSDATAFORMAT_TYPE_STANDARD_PACK_HEADER',
    'KSPROPSETID_TelephonyControl','KSNODEPIN_SUM_MUX_IN',
    'STATIC_AUDIO_EFFECT_TYPE_CONSTANT_TONE_REMOVAL',
    'KSNODETYPE_LOW_FREQUENCY_EFFECTS_SPEAKER',
    'KSCAMERA_EXTENDEDPROP_FACEDETECTION_VIDEO',
    'KSDATAFORMAT_SUBTYPE_Line21_GOPPacket',
    'STATIC_KSDATAFORMAT_SUBTYPE_STANDARD_MPEG1_AUDIO',
    '_tagKSTELEPHONY_CALLCONTROL','CODECAPI_VIDEO_ENCODER',
    'KS_VBICAP_PROTECTION_MV_HARDWARE',
    'KSCAMERA_EXTENDEDPROP_HISTOGRAM_OFF','STATIC_KSMEDIUMSETID_VPBus',
    'KSNODETYPE_DESKTOP_MICROPHONE','KSAUDIO_SPEAKER_5POINT1_BACK',
    'KSPROPSETID_VBICAP_PROPERTIES',
    'KSNODETYPE_ECHO_CANCELING_SPEAKERPHONE','KSPROPERTY_CROSSBAR_ROUTE_S',
    'STATIC_KSDATAFORMAT_SUBTYPE_NABTS',
    'KSDATAFORMAT_SPECIFIER_DIALECT_MPEG1_AUDIO','TUNER_ANALOG_CAPS_S',
    'SYSAUDIO_ATTACH_VIRTUAL_SOURCE','KSAUDFNAME_AUX_MUTE',
    'DEFINE_KSPROPERTY_ITEM_OVERLAYUPDATE_COLORREF',
    'STATIC_KSNODETYPE_TELEPHONE','STATIC_AUDIOENDPOINT_CLASS_UUID',
    'KS_TUNER_TUNING_FLAGS','_VBICODECFILTERING_STATISTICS_COMMON',
    'PROPSETID_EXT_TRANSPORT','STATIC_KSDATAFORMAT_SPECIFIER_DSOUND',
    'KSAUDIO_STEREO_SPEAKER_GEOMETRY_NARROW',
    'KSDATAFORMAT_SUBTYPE_MJPG_IR','KS_VIDEOSTREAM_CAPTURE',
    'STATIC_KSAUDFNAME_MONO_OUT','KSPROPSETID_DirectSound3DListener',
    'SPEAKER_TOP_FRONT_RIGHT','KSPROPERTY_ITD3D','KSMUSIC_TECHNOLOGY_PORT',
    'STATIC_KSNODETYPE_MIDI_ELEMENT','KS_TVTUNER_CHANGE_BEGIN_TUNE',
    '_VBICAP_PROPERTIES_PROTECTION_S',
)
