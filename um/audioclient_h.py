__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
from .unknwn_h import * # NOQA
from .mmreg_h import * # NOQA
from .audiosessiontypes_h import * # NOQA
from .winapifamily_h import * # NOQA
from .ks_h import * # NOQA
from .ksmedia_h import * # NOQA

from .wtypes_h import (
    ENUM,
    HRESULT,
    HANDLE,
    BOOL,
    POINTER,
    FLOAT,
    GUID,
    REFERENCE_TIME,
    LPBYTE,
    UINT32,
    DWORD,
    UINT64,
    VOID,
    BYTE
)
from .guiddef_h import IID, LPCGUID
import ctypes
import comtypes


class AUDCLNT_STREAMOPTIONS(ENUM):
    AUDCLNT_STREAMOPTIONS_NONE = 0
    AUDCLNT_STREAMOPTIONS_RAW = 0x1
    AUDCLNT_STREAMOPTIONS_MATCH_FORMAT = 0x2
    AUDCLNT_STREAMOPTIONS_AMBISONICS = 0x4


class AudioClientProperties(ctypes.Structure):
    _fields_ = [
        ('cbSize', UINT32),
        ('bIsOffload', BOOL),
        ('eCategory', AUDIO_STREAM_CATEGORY),
        ('Options', AUDCLNT_STREAMOPTIONS),
    ]


COMMETHOD = comtypes.COMMETHOD


IID_IAudioClient = IID(
    '{1CB9AD4C-DBFA-4c32-B178-C2F568A703B2}'
)


class IAudioClient(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioClient
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'Initialize',
            (['in'], DWORD, 'ShareMode'),
            (['in'], DWORD, 'StreamFlags'),
            (['in'], REFERENCE_TIME, 'hnsBufferDuration'),
            (['in'], REFERENCE_TIME, 'hnsPeriodicity'),
            (['in'], POINTER(WAVEFORMATEX), 'pFormat'),
            (['in'], LPCGUID, 'AudioSessionGuid')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetBufferSize',
            (['out'], POINTER(UINT32), 'pNumBufferFrames')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetStreamLatency',
            (['out'], POINTER(REFERENCE_TIME), 'phnsLatency')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentPadding',
            (['out'], POINTER(UINT32), 'pNumPaddingFrames')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsFormatSupported',
            (['in'], AUDCLNT_SHAREMODE, 'ShareMode'),
            (['in'], POINTER(WAVEFORMATEX), 'pFormat'),
            (['out'], POINTER(POINTER(WAVEFORMATEX)), 'ppClosestMatch')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMixFormat',
            (['out'], POINTER(POINTER(WAVEFORMATEX)), 'ppDeviceFormat')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetDevicePeriod',
            (['out'], POINTER(REFERENCE_TIME), 'phnsDefaultDevicePeriod'),
            (['out'], POINTER(REFERENCE_TIME), 'phnsMinimumDevicePeriod')
        ),
        COMMETHOD([], HRESULT, 'Start'),
        COMMETHOD([], HRESULT, 'Stop'),
        COMMETHOD([], HRESULT, 'Reset'),
        COMMETHOD(
            [],
            HRESULT,
            'SetEventHandle',
            (['in'], HANDLE, 'eventHandle'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetService',
            (['in'], LPCGUID, 'iid'),
            (['out'], POINTER(POINTER(VOID)), 'ppv')
        ),
    )


IID_IAudioClient2 = IID(
    '{726778CD-F60A-4eda-82DE-E47610CD78AA}'
)


class IAudioClient2(IAudioClient):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioClient2
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'IsOffloadCapable',
            (['in'], AUDIO_STREAM_CATEGORY, 'Category'),
            (['out'], POINTER(BOOL), 'pbOffloadCapable')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetClientProperties',
            (['in'], POINTER(AudioClientProperties), 'pProperties')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetBufferSizeLimits',
            (['in'], POINTER(WAVEFORMATEX), 'pFormat'),
            (['in'], BOOL, 'bEventDriven'),
            (['out'], POINTER(REFERENCE_TIME), 'phnsMinBufferDuration'),
            (['out'], POINTER(REFERENCE_TIME), 'phnsMaxBufferDuration')
        )
    )


class AudioClient3ActivationParams(ctypes.Structure):
    _fields_ = [
        ('tracingContextId', GUID),
    ]


IID_IAudioClient3 = IID(
    '{7ED4EE07-8E67-4CD4-8C1A-2B7A5987AD42}'
)


class IAudioClient3(IAudioClient2):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioClient3
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'GetSharedModeEnginePeriod',
            (['in'], POINTER(WAVEFORMATEX), 'pFormat'),
            (['out'], POINTER(UINT32), 'pDefaultPeriodInFrames'),
            (['out'], POINTER(UINT32), 'pFundamentalPeriodInFrames'),
            (['out'], POINTER(UINT32), 'pMinPeriodInFrames'),
            (['out'], POINTER(UINT32), 'pMaxPeriodInFrames')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCurrentSharedModeEnginePeriod',
            (['out'], POINTER(POINTER(WAVEFORMATEX)), 'ppFormat'),
            (['out'], POINTER(UINT32), 'pCurrentPeriodInFrames'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'InitializeSharedAudioStream',
            (['in'], DWORD, 'StreamFlags'),
            (['in'], UINT32, 'PeriodInFrames'),
            (['in'], POINTER(WAVEFORMATEX), 'pFormat'),
            (['in'], LPCGUID, 'AudioSessionGuid')
        )
    )


IID_IAudioRenderClient = IID(
    '{F294ACFC-3146-4483-A7BF-ADDCA7C260E2}'
)


class IAudioRenderClient(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioRenderClient
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'GetBuffer',
            (['in'], UINT32, 'NumFramesRequested'),
            (['out'], POINTER(LPBYTE), 'ppData')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ReleaseBuffer',
            (['in'], UINT32, 'NumFramesWritten'),
            (['in'], DWORD, 'dwFlags'),
        )
    )


IID_IAudioCaptureClient = IID(
    '{C8ADBD64-E71E-48a0-A4DE-185C395CD317}'
)


class IAudioCaptureClient(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioCaptureClient
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'GetBuffer',
            (['out'], POINTER(POINTER(BYTE)), 'ppData'),
            (['out'], POINTER(UINT32), 'pNumFramesToRead'),
            (['out'], POINTER(DWORD), 'pdwFlags'),
            (['out'], POINTER(UINT64), 'pu64DevicePosition'),
            (['out'], POINTER(UINT64), 'pu64QPCPosition')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'ReleaseBuffer',
            (['in'], UINT32, 'NumFramesRead'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetNextPacketSize',
            (['out'], POINTER(UINT32), 'pNumFramesInNextPacket'),
        )
    )


AUDIOCLOCK_CHARACTERISTIC_FIXED_FREQ = 0x00000001

IID_IAudioClock = IID(
    '{CD63314F-3FBA-4a1b-812C-EF96358728E7}'
)


class IAudioClock(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioClock
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'GetFrequency',
            (['out'], POINTER(UINT64), 'pu64Frequency')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetPosition',
            (['out'], POINTER(UINT64), 'pu64Position'),
            (['out'], POINTER(UINT64), 'pu64QPCPosition'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetCharacteristics',
            (['out'], POINTER(DWORD), 'pdwCharacteristics'),
        )
    )


IID_IAudioClock2 = IID(
    '{6f49ff73-6727-49ac-a008-d98cf5e70048}'
)


class IAudioClock2(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioClock2
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'GetDevicePosition',
            (['out'], POINTER(UINT64), 'DevicePosition'),
            (['out'], POINTER(UINT64), 'QPCPosition'),
        ),
    )


IID_IAudioClockAdjustment = IID(
    '{f6e4c0a0-46d9-4fb8-be21-57a3ef2b626c}'
)


class IAudioClockAdjustment(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioClockAdjustment
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'SetSampleRate',
            (['in'], FLOAT, 'flSampleRate')
        ),
    )


IID_ISimpleAudioVolume = IID(
    '{87CE5498-68D6-44E5-9215-6DA47EF883D8}'
)


class ISimpleAudioVolume(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_ISimpleAudioVolume
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'SetMasterVolume',
            (['in'], FLOAT, 'fLevel'),
            (['in'], LPCGUID, 'EventContext')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMasterVolume',
            (['out'], POINTER(FLOAT), 'pfLevel')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetMute',
            (['in'], BOOL, 'bMute'),
            (['in'], LPCGUID, 'EventContext')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMute',
            (['out'], POINTER(BOOL), 'pbMute')
        )
    )


IID_IAudioStreamVolume = IID(
    '{93014887-242D-4068-8A15-CF5E93B90FE3}'
)


class IAudioStreamVolume(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IAudioStreamVolume
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelCount',
            (['out'], POINTER(UINT32), 'pdwCount')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetChannelVolume',
            (['in'], UINT32, 'dwIndex'),
            (['in'], FLOAT, 'fLevel')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelVolume',
            (['in'], UINT32, 'dwIndex'),
            (['out'], POINTER(FLOAT), 'pfLevel')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetAllVolumes',
            (['in'], UINT32, 'dwCount'),
            (['in'], POINTER(FLOAT), 'pfVolumes')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAllVolumes',
            (['in'], UINT32, 'dwCount'),
            (['out'], POINTER(FLOAT), 'pfVolumes')
        ),
    )


class AMBISONICS_TYPE(ENUM):
    AMBISONICS_TYPE_FULL3D = 0


class AMBISONICS_CHANNEL_ORDERING(ENUM):
    AMBISONICS_CHANNEL_ORDERING_ACN = 0


class AMBISONICS_NORMALIZATION(ENUM):
    AMBISONICS_NORMALIZATION_SN3D = 0
    AMBISONICS_NORMALIZATION_N3D = AMBISONICS_NORMALIZATION_SN3D + 1


AMBISONICS_PARAM_VERSION_1 = 0x00000001


class AMBISONICS_PARAMS(ctypes.Structure):
    _fields_ = [
        ('u32Size', UINT32),
        ('u32Version', UINT32),
        ('u32Type', AMBISONICS_TYPE),
        ('u32ChannelOrdering', AMBISONICS_CHANNEL_ORDERING),
        ('u32Normalization', AMBISONICS_NORMALIZATION),
        ('u32Order', UINT32),
        ('u32NumChannels', UINT32),
        ('pu32ChannelMap', POINTER(UINT32)),
    ]


IID_IAudioAmbisonicsControl = IID(
    '{28724C91-DF35-4856-9F76-D6A26413F3DF}'
)


class IAudioAmbisonicsControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioAmbisonicsControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetData'
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetHeadTracking',
            (['in'], BOOL, 'bEnableHeadTracking'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetHeadTracking',
            (['out'], POINTER(BOOL), 'pbEnableHeadTracking'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetRotation',
            (['in'], FLOAT, 'X'),
            (['in'], FLOAT, 'Y'),
            (['in'], FLOAT, 'Z'),
            (['in'], FLOAT, 'W'),
        ),
    ]


IID_IChannelAudioVolume = IID(
    '{1C158861-B533-4B30-B1CF-E853E51C59B8}'
)


class IChannelAudioVolume(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IChannelAudioVolume
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelCount',
            (['out'], POINTER(UINT32), 'pdwCount')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetChannelVolume',
            (['in'], UINT32, 'dwIndex'),
            (['in'], FLOAT, 'fLevel'),
            (['in'], LPCGUID, 'EventContext')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelVolume',
            (['in'], UINT32, 'dwIndex'),
            (['out'], POINTER(FLOAT), 'pfLevel')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetAllVolumes',
            (['in'], UINT32, 'dwCount'),
            (['in'], POINTER(FLOAT), 'pfVolumes'),
            (['in'], LPCGUID, 'EventContext')
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetAllVolumes',
            (['in'], UINT32, 'dwCount'),
            (['out'], POINTER(FLOAT), 'pfVolumes')
        ),
    )


def AUDCLNT_ERR(n):
    return n


def AUDCLNT_SUCCESS(n):
    return n


AUDCLNT_E_NOT_INITIALIZED = AUDCLNT_ERR(0x00000001)
AUDCLNT_E_ALREADY_INITIALIZED = AUDCLNT_ERR(0x00000002)
AUDCLNT_E_WRONG_ENDPOINT_TYPE = AUDCLNT_ERR(0x00000003)
AUDCLNT_E_DEVICE_INVALIDATED = AUDCLNT_ERR(0x00000004)
AUDCLNT_E_NOT_STOPPED = AUDCLNT_ERR(0x00000005)
AUDCLNT_E_BUFFER_TOO_LARGE = AUDCLNT_ERR(0x00000006)
AUDCLNT_E_OUT_OF_ORDER = AUDCLNT_ERR(0x00000007)
AUDCLNT_E_UNSUPPORTED_FORMAT = AUDCLNT_ERR(0x00000008)
AUDCLNT_E_INVALID_SIZE = AUDCLNT_ERR(0x00000009)
AUDCLNT_E_DEVICE_IN_USE = AUDCLNT_ERR(0x00000000a)
AUDCLNT_E_BUFFER_OPERATION_PENDING = AUDCLNT_ERR(0x00000000b)
AUDCLNT_E_THREAD_NOT_REGISTERED = AUDCLNT_ERR(0x00000000c)
AUDCLNT_E_EXCLUSIVE_MODE_NOT_ALLOWED = AUDCLNT_ERR(0x00000000e)
AUDCLNT_E_ENDPOINT_CREATE_FAILED = AUDCLNT_ERR(0x00000000f)
AUDCLNT_E_SERVICE_NOT_RUNNING = AUDCLNT_ERR(0x00000010)
AUDCLNT_E_EVENTHANDLE_NOT_EXPECTED = AUDCLNT_ERR(0x00000011)
AUDCLNT_E_EXCLUSIVE_MODE_ONLY = AUDCLNT_ERR(0x00000012)
AUDCLNT_E_BUFDURATION_PERIOD_NOT_EQUAL = AUDCLNT_ERR(0x00000013)
AUDCLNT_E_EVENTHANDLE_NOT_SET = AUDCLNT_ERR(0x00000014)
AUDCLNT_E_INCORRECT_BUFFER_SIZE = AUDCLNT_ERR(0x00000015)
AUDCLNT_E_BUFFER_SIZE_ERROR = AUDCLNT_ERR(0x00000016)
AUDCLNT_E_CPUUSAGE_EXCEEDED = AUDCLNT_ERR(0x00000017)
AUDCLNT_E_BUFFER_ERROR = AUDCLNT_ERR(0x00000018)
AUDCLNT_E_BUFFER_SIZE_NOT_ALIGNED = AUDCLNT_ERR(0x00000019)
AUDCLNT_E_INVALID_DEVICE_PERIOD = AUDCLNT_ERR(0x00000020)
AUDCLNT_E_INVALID_STREAM_FLAG = AUDCLNT_ERR(0x00000021)
AUDCLNT_E_ENDPOINT_OFFLOAD_NOT_CAPABLE = AUDCLNT_ERR(0x00000022)
AUDCLNT_E_OUT_OF_OFFLOAD_RESOURCES = AUDCLNT_ERR(0x00000023)
AUDCLNT_E_OFFLOAD_MODE_ONLY = AUDCLNT_ERR(0x00000024)
AUDCLNT_E_NONOFFLOAD_MODE_ONLY = AUDCLNT_ERR(0x00000025)
AUDCLNT_E_RESOURCES_INVALIDATED = AUDCLNT_ERR(0x00000026)
AUDCLNT_E_RAW_MODE_UNSUPPORTED = AUDCLNT_ERR(0x00000027)
AUDCLNT_E_ENGINE_PERIODICITY_LOCKED = AUDCLNT_ERR(0x00000028)
AUDCLNT_E_ENGINE_FORMAT_LOCKED = AUDCLNT_ERR(0x00000029)
AUDCLNT_E_HEADTRACKING_ENABLED = AUDCLNT_ERR(0x00000030)
AUDCLNT_E_HEADTRACKING_UNSUPPORTED = AUDCLNT_ERR(0x00000040)
AUDCLNT_S_BUFFER_EMPTY = AUDCLNT_SUCCESS(0x00000001)
AUDCLNT_S_THREAD_ALREADY_REGISTERED = AUDCLNT_SUCCESS(0x00000002)
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
AUDCLNT_S_POSITION_STALLED = AUDCLNT_SUCCESS(0x00000003)
# Additional Prototypes for ALL INTerfaces
# end of Additional Prototypes

__all__ = (
    'AUDCLNT_STREAMOPTIONS', 'AudioClientProperties', 'IID_IAudioClient',
    'IAudioClient', 'IID_IAudioClient2', 'IAudioClient2',
    'AudioClient3ActivationParams', 'IID_IAudioClient3', 'IAudioClient3',
    'IID_IAudioRenderClient', 'IAudioRenderClient', 'IID_IAudioCaptureClient',
    'IAudioCaptureClient', 'AUDIOCLOCK_CHARACTERISTIC_FIXED_FREQ',
    'IID_IAudioClock', 'IAudioClock', 'IID_IAudioClock2', 'IAudioClock2',
    'IID_IAudioClockAdjustment', 'IAudioClockAdjustment',
    'IID_ISimpleAudioVolume', 'ISimpleAudioVolume', 'IID_IAudioStreamVolume',
    'IAudioStreamVolume', 'AMBISONICS_TYPE', 'AMBISONICS_CHANNEL_ORDERING',
    'AMBISONICS_NORMALIZATION', 'AMBISONICS_PARAM_VERSION_1',
    'AMBISONICS_PARAMS', 'IID_IAudioAmbisonicsControl',
    'IAudioAmbisonicsControl', 'IID_IChannelAudioVolume',
    'IChannelAudioVolume', 'AUDCLNT_ERR', 'AUDCLNT_SUCCESS',
    'AUDCLNT_E_NOT_INITIALIZED', 'AUDCLNT_E_ALREADY_INITIALIZED',
    'AUDCLNT_E_WRONG_ENDPOINT_TYPE', 'AUDCLNT_E_DEVICE_INVALIDATED',
    'AUDCLNT_E_NOT_STOPPED', 'AUDCLNT_E_BUFFER_TOO_LARGE',
    'AUDCLNT_E_OUT_OF_ORDER', 'AUDCLNT_E_UNSUPPORTED_FORMAT',
    'AUDCLNT_E_INVALID_SIZE', 'AUDCLNT_E_DEVICE_IN_USE',
    'AUDCLNT_E_BUFFER_OPERATION_PENDING', 'AUDCLNT_E_THREAD_NOT_REGISTERED',
    'AUDCLNT_E_EXCLUSIVE_MODE_NOT_ALLOWED', 'AUDCLNT_E_ENDPOINT_CREATE_FAILED',
    'AUDCLNT_E_SERVICE_NOT_RUNNING', 'AUDCLNT_E_EVENTHANDLE_NOT_EXPECTED',
    'AUDCLNT_E_EXCLUSIVE_MODE_ONLY', 'AUDCLNT_E_BUFDURATION_PERIOD_NOT_EQUAL',
    'AUDCLNT_E_EVENTHANDLE_NOT_SET', 'AUDCLNT_E_INCORRECT_BUFFER_SIZE',
    'AUDCLNT_E_BUFFER_SIZE_ERROR', 'AUDCLNT_E_CPUUSAGE_EXCEEDED',
    'AUDCLNT_E_BUFFER_ERROR', 'AUDCLNT_E_BUFFER_SIZE_NOT_ALIGNED',
    'AUDCLNT_E_INVALID_DEVICE_PERIOD', 'AUDCLNT_E_INVALID_STREAM_FLAG',
    'AUDCLNT_E_ENDPOINT_OFFLOAD_NOT_CAPABLE',
    'AUDCLNT_E_OUT_OF_OFFLOAD_RESOURCES', 'AUDCLNT_E_OFFLOAD_MODE_ONLY',
    'AUDCLNT_E_NONOFFLOAD_MODE_ONLY', 'AUDCLNT_E_RESOURCES_INVALIDATED',
    'AUDCLNT_E_RAW_MODE_UNSUPPORTED', 'AUDCLNT_E_ENGINE_PERIODICITY_LOCKED',
    'AUDCLNT_E_ENGINE_FORMAT_LOCKED', 'AUDCLNT_E_HEADTRACKING_ENABLED',
    'AUDCLNT_E_HEADTRACKING_UNSUPPORTED', 'AUDCLNT_S_BUFFER_EMPTY',
    'AUDCLNT_S_THREAD_ALREADY_REGISTERED', 'AUDCLNT_S_POSITION_STALLED',
)
