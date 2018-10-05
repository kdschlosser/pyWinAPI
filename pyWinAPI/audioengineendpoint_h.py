
__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
# from oaidl_h import * # NOQA
# from ocidl_h import * # NOQA
# from propidl_h import * # NOQA
from .mmreg_h import * # NOQA
from .audioapotypes_h import * # NOQA
from .mmdeviceapi_h import * # NOQA
from .winapifamily_h import * # NOQA

from .wtypes_h import (
    ENUM,
    HNSTIME,
    POINTER,
    VOID,
    HRESULT,
    UINT32,
    DWORD,
    HANDLE,
    UINT_PTR,
    FLOAT32,
    BOOL,
    UINT64,
)
from .propkeydef_h import DEFINE_PROPERTYKEY

from .guiddef_h import (
    DEFINE_GUID,
    IID,
    DEFINE_GUIDSTRUCT,
    DEFINE_GUIDNAMED,
)
import ctypes
import comtypes


class __MIDL___MIDL_itf_audioengineendpoint_0000_0000_0001(ENUM):
    eHostProcessConnector = 0
    eOffloadConnector = eHostProcessConnector + 1
    eLoopbackConnector = eOffloadConnector + 1
    eKeywordDetectorConnector = eLoopbackConnector + 1
    eConnectorCount = eKeywordDetectorConnector + 1


EndpointConnectorType = __MIDL___MIDL_itf_audioengineendpoint_0000_0000_0001


class AUDIO_ENDPOINT_SHARED_CREATE_PARAMS(ctypes.Structure):
    _fields_ = [
        ('u32Size', UINT32),
        ('u32TSSessionId', UINT32),
        ('targetEndpointConnectorType', EndpointConnectorType),
        ('wfxDeviceFormat', WAVEFORMATEX),
    ]


PAUDIO_ENDPOINT_SHARED_CREATE_PARAMS = POINTER(AUDIO_ENDPOINT_SHARED_CREATE_PARAMS)


class AE_POSITION_FLAGS(ENUM):
    POSITION_INVALID = 0
    POSITION_DISCONTINUOUS = 1
    POSITION_CONTINUOUS = 2
    POSITION_QPC_ERROR = 4


class AE_CURRENT_POSITION(ctypes.Structure):
    _fields_ = [
        ('u64DevicePosition', UINT64),
        ('u64StreamPosition', UINT64),
        ('u64PaddingFrames', UINT64),
        ('hnsQPCPosition', HNSTIME),
        ('f32FramesPerSecond', FLOAT32),
        ('Flag', AE_POSITION_FLAGS),
    ]


PAE_CURRENT_POSITION = POINTER(AE_CURRENT_POSITION)

COMMETHOD = comtypes.COMMETHOD

IID_IAudioEndpoint = IID(
    '{30A99515-1527-4451-AF9F-00C5F0234DAF}'
)


class IAudioEndpoint(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpoint
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetFrameFormat',
            (['out'], POINTER(POINTER(WAVEFORMATEX)), 'ppFormat'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetFramesPerPacket',
            (['out'], POINTER(UINT32), 'pFramesPerPacket'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetLatency',
            (['out'], POINTER(HNSTIME), 'pLatency'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetStreamFlags',
            (['in'], DWORD, 'streamFlags'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetEventHandle',
            (['in'], HANDLE, 'eventHandle'),
        ),
    ]


IID_IAudioEndpointRT = IID(
    '{DFD2005F-A6E5-4d39-A265-939ADA9FBB4D}'
)


class IAudioEndpointRT(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointRT
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            VOID,
            'GetCurrentPadding',
            (['out'], POINTER(HNSTIME), 'pPadding'),
            (['out'], POINTER(AE_CURRENT_POSITION), 'pAeCurrentPosition'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetPinActive'
        ),
    ]


IID_IAudioInputEndpointRT = IID(
    '{8026AB61-92B2-43c1-A1DF-5C37EBD08D82}'
)


class IAudioInputEndpointRT(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioInputEndpointRT
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            VOID,
            'GetInputDataPointer',
            (['in', 'out'], POINTER(APO_CONNECTION_PROPERTY), 'pConnectionProperty'),
            (['in', 'out'], POINTER(AE_CURRENT_POSITION), 'pAeTimeStamp'),
        ),
        COMMETHOD(
            [],
            VOID,
            'ReleaseInputDataPointer',
            (['in'], UINT32, 'u32FrameCount'),
            (['in'], UINT_PTR, 'pDataPointer'),
        ),
        COMMETHOD(
            [],
            VOID,
            'PulseEndpoint'
        ),
    ]


IID_IAudioOutputEndpointRT = IID(
    '{8FA906E4-C31C-4e31-932E-19A66385E9AA}'
)


class IAudioOutputEndpointRT(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioOutputEndpointRT
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            UINT_PTR,
            'GetOutputDataPointer',
            (['in'], UINT32, 'u32FrameCount'),
            (['in'], POINTER(AE_CURRENT_POSITION), 'pAeTimeStamp'),
        ),
        COMMETHOD(
            [],
            VOID,
            'ReleaseOutputDataPointer',
            (['in'], POINTER(APO_CONNECTION_PROPERTY), 'pConnectionProperty'),
        ),
        COMMETHOD(
            [],
            VOID,
            'PulseEndpoint'
        ),
    ]


IID_IAudioDeviceEndpoint = IID(
    '{D4952F5A-A0B2-4cc4-8B82-9358488DD8AC}'
)


class IAudioDeviceEndpoint(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioDeviceEndpoint
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetBuffer',
            (['in'], HNSTIME, 'MaxPeriod'),
            (['in'], UINT32, 'u32LatencyCoefficient'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetRTCaps',
            (['out'], POINTER(BOOL), 'pbIsRTCapable'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetEventDrivenCapable',
            (['out'], POINTER(BOOL), 'pbisEventCapable'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'WriteExclusiveModeParametersToSharedMemory',
            (['in'], UINT_PTR, 'hTargetProcess'),
            (['in'], HNSTIME, 'hnsPeriod'),
            (['in'], HNSTIME, 'hnsBufferDuration'),
            (['in'], UINT32, 'u32LatencyCoefficient'),
            (['out'], POINTER(UINT32), 'pu32SharedMemorySize'),
            (['out'], POINTER(UINT_PTR), 'phSharedMemory'),
        ),
    ]


IID_IAudioEndpointOffloadStreamVolume = IID(
    '{64F1DD49-71CA-4281-8672-3A9EDDD1D0B6}'
)


class IAudioEndpointOffloadStreamVolume(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointOffloadStreamVolume
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetVolumeChannelCount',
            (['out'], POINTER(UINT32), 'pu32ChannelCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetChannelVolumes',
            (['in'], UINT32, 'u32ChannelCount'),
            (['in'], POINTER(FLOAT32), 'pf32Volumes'),
            (['in'], AUDIO_CURVE_TYPE, 'u32CurveType'),
            (['in'], POINTER(HNSTIME), 'pCurveDuration'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetChannelVolumes',
            (['in'], UINT32, 'u32ChannelCount'),
            (['out'], POINTER(FLOAT32), 'pf32Volumes'),
        ),
    ]


IID_IAudioEndpointOffloadStreamMute = IID(
    '{DFE21355-5EC2-40E0-8D6B-710AC3C00249}'
)


class IAudioEndpointOffloadStreamMute(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointOffloadStreamMute
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetMute',
            (['in'], BOOL, 'bMuted'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMute',
            (['out'], POINTER(BOOL), 'pbMuted'),
        ),
    ]


IID_IAudioEndpointOffloadStreamMeter = IID(
    '{E1546DCE-9DD1-418B-9AB2-348CED161C86}'
)


class IAudioEndpointOffloadStreamMeter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointOffloadStreamMeter
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetMeterChannelCount',
            (['out'], POINTER(UINT32), 'pu32ChannelCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetMeteringData',
            (['in'], UINT32, 'u32ChannelCount'),
            (['out'], POINTER(FLOAT32), 'pf32PeakValues'),
        ),
    ]


IID_IAudioEndpointLastBufferControl = IID(
    '{F8520DD3-8F9D-4437-9861-62F584C33DD6}'
)


class IAudioEndpointLastBufferControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointLastBufferControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            VOID,
            'ReleaseOutputDataPointerForLastBuffer',
            (['in'], POINTER(APO_CONNECTION_PROPERTY), 'pConnectionProperty'),
        ),
    ]


IID_IAudioLfxControl = IID(
    '{076A6922-D802-4F83-BAF6-409D9CA11BFE}'
)


class IAudioLfxControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioLfxControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SetLocalEffectsState',
            (['in'], BOOL, 'bEnabled'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetLocalEffectsState',
            (['out'], POINTER(BOOL), 'pbEnabled'),
        ),
    ]


IID_IHardwareAudioEngineBase = IID(
    '{EDDCE3E4-F3C1-453a-B461-223563CBD886}'
)


class IHardwareAudioEngineBase(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IHardwareAudioEngineBase
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetAvailableOffloadConnectorCount'
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetEngineFormat'
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetEngineDeviceFormat'
        ),
        COMMETHOD(
            [],
            HRESULT,
            'SetGfxState'
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetGfxState'
        ),
    ]


IID_IAudioEndpointControl = IID(
    '{C684B72A-6DF4-4774-BDF9-76B77509B653}'
)


class IAudioEndpointControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointControl
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'Stop'
        ),
    ]


STATIC_DEVINTERFACE_AUDIOENDPOINTPLUGIN = DEFINE_GUID(
    0x9F2F7B66,
    0x65AC,
    0x4FA6,
    0x8A,
    0xE4,
    0x12,
    0x3C,
    0x78,
    0xB8,
    0x93,
    0x13
)

DEVINTERFACE_AUDIOENDPOINTPLUGIN = DEFINE_GUIDSTRUCT(
    "9F2F7B66-65AC-4FA6-8AE4-123C78B89313"
)
DEVINTERFACE_AUDIOENDPOINTPLUGIN = DEFINE_GUIDNAMED(
    DEVINTERFACE_AUDIOENDPOINTPLUGIN
)
DEVPKEY_AudioEndpointPlugin_FactoryCLSID = DEFINE_PROPERTYKEY(
    0x12d83bd7,
    0xcf12,
    0x46be,
    0x85,
    0x40,
    0x81,
    0x27,
    0x10,
    0xd3,
    0x2,
    0x1c,
    1
)
DEVPKEY_AudioEndpointPlugin_DataFlow = DEFINE_PROPERTYKEY(
    0x12d83bd7,
    0xcf12,
    0x46be,
    0x85,
    0x40,
    0x81,
    0x27,
    0x10,
    0xd3,
    0x2,
    0x1c,
    2
)
DEVPKEY_AudioEndpointPlugin_PnPInterface = DEFINE_PROPERTYKEY(
    0x12d83bd7,
    0xcf12,
    0x46be,
    0x85,
    0x40,
    0x81,
    0x27,
    0x10,
    0xd3,
    0x2,
    0x1c,
    3
)

__all__ = (
    'IAudioEndpoint', 'IID_IAudioEndpoint', 'PAE_CURRENT_POSITION',
    'AE_CURRENT_POSITION', 'AE_POSITION_FLAGS',
    'PAUDIO_ENDPOINT_SHARED_CREATE_PARAMS',
    'AUDIO_ENDPOINT_SHARED_CREATE_PARAMS', 'EndpointConnectorType',
    '__MIDL___MIDL_itf_audioengineendpoint_0000_0000_0001',
    'IAudioInputEndpointRT', 'IID_IAudioInputEndpointRT',
    'IID_IAudioEndpointRT', 'IAudioEndpointRT', 'IAudioDeviceEndpoint',
    'IID_IAudioDeviceEndpoint', 'IID_IAudioOutputEndpointRT',
    'IAudioOutputEndpointRT', 'IAudioEndpointOffloadStreamMute',
    'IID_IAudioEndpointOffloadStreamMute', 'IAudioEndpointOffloadStreamVolume',
    'IID_IAudioEndpointOffloadStreamVolume', 'IAudioEndpointLastBufferControl',
    'IID_IAudioEndpointLastBufferControl', 'IAudioEndpointOffloadStreamMeter',
    'IID_IAudioEndpointOffloadStreamMeter', 'IHardwareAudioEngineBase',
    'IID_IHardwareAudioEngineBase', 'IAudioLfxControl',
    'IID_IAudioLfxControl', 'STATIC_DEVINTERFACE_AUDIOENDPOINTPLUGIN',
    'IAudioEndpointControl', 'IID_IAudioEndpointControl',
    'DEVPKEY_AudioEndpointPlugin_PnPInterface',
    'DEVPKEY_AudioEndpointPlugin_DataFlow',
    'DEVPKEY_AudioEndpointPlugin_FactoryCLSID',
    'DEVINTERFACE_AUDIOENDPOINTPLUGIN',
)
