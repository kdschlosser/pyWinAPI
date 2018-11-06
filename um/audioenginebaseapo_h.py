__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
from .ocidl_h import * # NOQA
from .oaidl_h import * # NOQA
from .mmdeviceapi_h import * # NOQA
from .audiomediatype_h import * # NOQA
from .audioapotypes_h import * # NOQA
from .winapifamily_h import * # NOQA
from .mmdeviceapi_h import IPropertyStore

from .wtypes_h import (
    ENUM,
    UINT32,
    POINTER,
    HRESULT,
    HNSTIME,
    BYTE,
    UINT,
    LPWSTR,
    VOID,
    LPGUID,
    HANDLE,
    UINT_PTR,
    LPARAM,
    CLSID,
    WCHAR,
    GUID,
    BOOL,
)
from .guiddef_h import IID
import ctypes
import comtypes


def _HRESULT_TYPEDEF_(_sc):
    return _sc


# The object has already been initialized.
APOERR_ALREADY_INITIALIZED = _HRESULT_TYPEDEF_(0x887D0001)

# Object/structure is not initialized.
APOERR_NOT_INITIALIZED = _HRESULT_TYPEDEF_(0x887D0002)

# a pin supporting the format cannot be found.
APOERR_FORMAT_NOT_SUPPORTED = _HRESULT_TYPEDEF_(0x887D0003)

# Invalid CLSID in an APO Initialization structure
APOERR_INVALID_APO_CLSID = _HRESULT_TYPEDEF_(0x887D0004)

# Buffers overlap on an APO that does not accept in-place buffers.
APOERR_BUFFERS_OVERLAP = _HRESULT_TYPEDEF_(0x887D0005)

# APO is already in an unlocked state
APOERR_ALREADY_UNLOCKED = _HRESULT_TYPEDEF_(0x887D0006)

# number of input or output connections not valid on this APO
APOERR_NUM_CONNECTIONS_INVALID = _HRESULT_TYPEDEF_(0x887D0007)

# Output maxFrameCount not large enough.
APOERR_INVALID_OUTPUT_MAXFRAMECOUNT = _HRESULT_TYPEDEF_(0x887D0008)

# Invalid connection format for this operation
APOERR_INVALID_CONNECTION_FORMAT = _HRESULT_TYPEDEF_(0x887D0009)

# APO is locked ready to process and can not be changed
APOERR_APO_LOCKED = _HRESULT_TYPEDEF_(0x887D000A)

# Invalid coefficient count
APOERR_INVALID_COEFFCOUNT = _HRESULT_TYPEDEF_(0x887D000B)

# Invalid coefficient
APOERR_INVALID_COEFFICIENT = _HRESULT_TYPEDEF_(0x887D000C)

# an invalid curve parameter was specified
APOERR_INVALID_CURVE_PARAM = _HRESULT_TYPEDEF_(0x887D000D)

# Signatures for data structures.
APO_CONNECTION_DESCRIPTOR_SIGNATURE = 'ACDS'
APO_CONNECTION_PROPERTY_SIGNATURE = 'ACPS'

# Min and max framerates for the engine
# Minimum frame rate for APOs
AUDIO_MIN_FRAMERATE = 10.0

# Maximum frame rate for APOs
AUDIO_MAX_FRAMERATE = 384000.0

# Min and max # of channels (samples per frame) for the APOs
# Current minimum number of channels for APOs
AUDIO_MIN_CHANNELS = 0x00000001

# Current maximum number of channels for APOs
AUDIO_MAX_CHANNELS = 0x00001000


class APO_CONNECTION_BUFFER_TYPE(ENUM):
    APO_CONNECTION_BUFFER_TYPE_ALLOCATED = 0
    APO_CONNECTION_BUFFER_TYPE_EXTERNAL = 1
    APO_CONNECTION_BUFFER_TYPE_DEPENDANT = 2


class APO_CONNECTION_DESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('Type', APO_CONNECTION_BUFFER_TYPE),
        ('pBuffer', UINT_PTR),
        ('u32MaxFrameCount', UINT32),
        ('ppFormat', POINTER(POINTER(IAudioMediaType))),
        ('u32Signature', UINT32),
    ]


class APO_FLAG(ENUM):
    APO_FLAG_NONE = 0x00000000
    APO_FLAG_INPLACE = 0x00000001
    APO_FLAG_SAMPLESPERFRAME_MUST_MATCH = 0x00000002
    APO_FLAG_FRAMESPERSECOND_MUST_MATCH = 0x00000004
    APO_FLAG_BITSPERSAMPLE_MUST_MATCH = 0x00000008
    APO_FLAG_MIXER = 0x00000010
    APO_FLAG_DEFAULT = (
        (
            APO_FLAG_SAMPLESPERFRAME_MUST_MATCH |
            APO_FLAG_FRAMESPERSECOND_MUST_MATCH
        ) | APO_FLAG_BITSPERSAMPLE_MUST_MATCH
    )


class APO_REG_PROPERTIES(ctypes.Structure):
    _fields_ = [
        ('clsid', CLSID),
        ('Flags', APO_FLAG),
        ('szFriendlyName', WCHAR * 256),
        ('szCopyrightInfo', WCHAR * 256),
        ('u32MajorVersion', UINT32),
        ('u32MinorVersion', UINT32),
        ('u32MinInputConnections', UINT32),
        ('u32MaxInputConnections', UINT32),
        ('u32MinOutputConnections', UINT32),
        ('u32MaxOutputConnections', UINT32),
        ('u32MaxInstances', UINT32),
        ('u32NumAPOInterfaces', UINT32),
        ('iidAPOInterfaceList', IID * 1),
    ]


PAPO_REG_PROPERTIES = POINTER(APO_REG_PROPERTIES)


class APOInitBaseStruct(ctypes.Structure):
    _fields_ = [
        ('cbSize', UINT32),
        ('clsid', CLSID),
    ]


class AUDIO_FLOW_TYPE(ENUM):
    AUDIO_FLOW_PULL = 0
    AUDIO_FLOW_PUSH = AUDIO_FLOW_PULL + 1


class EAudioConstriction(ENUM):
    eAudioConstrictionOff = 0
    eAudioConstriction48_16 = eAudioConstrictionOff + 1
    eAudioConstriction44_16 = eAudioConstriction48_16 + 1
    eAudioConstriction14_14 = eAudioConstriction44_16 + 1
    eAudioConstrictionMute = eAudioConstriction14_14 + 1


COMMETHOD = comtypes.COMMETHOD


IID_IAudioProcessingObjectRT = IID(
    '{9E1D6A6D-DDBC-4E95-A4C7-AD64BA37846C}'
)


class IAudioProcessingObjectRT(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioProcessingObjectRT
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            VOID,
            'APOProcess',
            (['in'], UINT32, 'u32NumInputConnections'),
            (['in'], POINTER(POINTER(APO_CONNECTION_PROPERTY)), 'ppInputConnections'),
            (['in'], UINT32, 'u32NumOutputConnections'),
            (['in', 'out'], POINTER(POINTER(APO_CONNECTION_PROPERTY)), 'ppOutputConnections'),
        ),
        COMMETHOD(
            [],
            UINT32,
            'CalcInputFrames',
            (['in'], UINT32, 'u32OutputFrameCount'),
        ),
        COMMETHOD(
            [],
            UINT32,
            'CalcOutputFrames',
            (['in'], UINT32, 'u32InputFrameCount'),
        ),
    ]


IID_IAudioProcessingObjectVBR = IID(
    '{7ba1db8f-78ad-49cd-9591-f79d80a17c81}'
)


class IAudioProcessingObjectVBR(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioProcessingObjectVBR
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'CalcMaxInputFrames',
            (['in'], UINT32, 'u32MaxOutputFrameCount'),
            (['out'], POINTER(UINT32), 'pu32InputFrameCount'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CalcMaxOutputFrames',
            (['in'], UINT32, 'u32MaxInputFrameCount'),
            (['out'], POINTER(UINT32), 'pu32OutputFrameCount'),
        ),
    ]


IID_IAudioProcessingObjectConfiguration = IID(
    '{0E5ED805-ABA6-49c3-8F9A-2B8C889C4FA8}'
)


class IAudioProcessingObjectConfiguration(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioProcessingObjectConfiguration
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'LockForProcess',
            (['in'], UINT32, 'u32NumInputConnections'),
            (
                ['in'],
                POINTER(POINTER(APO_CONNECTION_DESCRIPTOR)),
                'ppInputConnections'
            ),
            (['in'], UINT32, 'u32NumOutputConnections'),
            (
                ['in'],
                POINTER(POINTER(APO_CONNECTION_DESCRIPTOR)),
                'ppOutputConnections'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnlockForProcess'
        ),
    ]


IID_IAudioProcessingObject = IID(
    '{FD7F2B29-24D0-4b5c-B177-592C39F9CA10}'
)


class IAudioProcessingObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioProcessingObject
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetLatency',
            (['out'], POINTER(HNSTIME), 'pTime'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetRegistrationProperties',
            (['out'], POINTER(POINTER(APO_REG_PROPERTIES)), 'ppRegProps'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'Initialize',
            (['in'], UINT32, 'cbDataSize'),
            (['in'], POINTER(BYTE), 'pbyData'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsInputFormatSupported',
            (['in'], POINTER(IAudioMediaType), 'pOppositeFormat'),
            (['in'], POINTER(IAudioMediaType), 'pRequestedInputFormat'),
            (
                ['out'],
                POINTER(POINTER(IAudioMediaType)),
                'ppSupportedInputFormat'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'IsOutputFormatSupported',
            (['in'], POINTER(IAudioMediaType), 'pOppositeFormat'),
            (['in'], POINTER(IAudioMediaType), 'pRequestedOutputFormat'),
            (
                ['out'],
                POINTER(POINTER(IAudioMediaType)),
                'ppSupportedOutputFormat'
            ),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetInputChannelCount',
            (['out'], POINTER(UINT32), 'pu32ChannelCount'),
        ),
    ]


IID_IAudioSystemEffects = IID(
    '{5FA00F27-ADD6-499a-8A9D-6B98521FA75B}'
)


class IAudioSystemEffects(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSystemEffects
    _idlflags_ = []


IID_IAudioSystemEffects2 = IID(
    '{BAFE99D2-7436-44CE-9E0E-4D89AFBFFF56}'
)


class IAudioSystemEffects2(IAudioSystemEffects):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSystemEffects2
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetEffectsList',
            (['out'], POINTER(LPGUID), 'ppEffectsIds'),
            (['out'], POINTER(UINT), 'pcEffects'),
            (['in'], HANDLE, 'Event'),
        ),
    ]


IID_IAudioSystemEffectsCustomFormats = IID(
    '{B1176E34-BB7F-4f05-BEBD-1B18A534E097}'
)


class IAudioSystemEffectsCustomFormats(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioSystemEffectsCustomFormats
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'GetFormatCount',
            (['out'], POINTER(UINT), 'pcFormats'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetFormat',
            (['in'], UINT, 'nFormat'),
            (['out'], POINTER(POINTER(IAudioMediaType)), 'ppFormat'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'GetFormatRepresentation',
            (['in'], UINT, 'nFormat'),
            (['out'], POINTER(LPWSTR), 'ppwstrFormatRep'),
        ),
    ]


class APOInitSystemEffects(ctypes.Structure):
    _fields_ = [
        ('APOInit', APOInitBaseStruct),
        ('pAPOEndpoINTProperties', POINTER(IPropertyStore)),
        ('pAPOSystemEffectsProperties', POINTER(IPropertyStore)),
        ('pReserved', POINTER(VOID)),
        ('pDeviceCollection', POINTER(IMMDeviceCollection)),
    ]


class APOInitSystemEffects2(ctypes.Structure):
    _fields_ = [
        ('APOInit', APOInitBaseStruct),
        ('pAPOEndpoINTProperties', POINTER(IPropertyStore)),
        ('pAPOSystemEffectsProperties', POINTER(IPropertyStore)),
        ('pReserved', POINTER(VOID)),
        ('pDeviceCollection', POINTER(IMMDeviceCollection)),
        ('nSoftwareIoDeviceInCollection', UINT),
        ('nSoftwareIoConnectorIndex', UINT),
        ('AudioProcessingMode', GUID),
        ('InitializeForDiscoveryOnly', BOOL),
    ]


class __MIDL___MIDL_itf_audioenginebaseapo_0000_0007_0001(ctypes.Structure):
    _fields_ = [
        ('AddPageParam', LPARAM),
        ('pwstrEndpoINTID', LPWSTR),
        ('pFxProperties', POINTER(IPropertyStore)),
    ]


AudioFXExtensionParams = __MIDL___MIDL_itf_audioenginebaseapo_0000_0007_0001

__all__ = (
    'APO_CONNECTION_BUFFER_TYPE', 'AUDIO_MAX_CHANNELS', 'AUDIO_MIN_CHANNELS',
    'AUDIO_MAX_FRAMERATE', 'APO_CONNECTION_PROPERTY_SIGNATURE',
    'APO_CONNECTION_DESCRIPTOR_SIGNATURE', 'APOERR_INVALID_CURVE_PARAM',
    'APOERR_INVALID_COEFFICIENT', 'APOERR_INVALID_COEFFCOUNT',
    'APOERR_APO_LOCKED', 'APOERR_INVALID_CONNECTION_FORMAT',
    'APOERR_INVALID_OUTPUT_MAXFRAMECOUNT', 'APOERR_NUM_CONNECTIONS_INVALID',
    'APOERR_ALREADY_UNLOCKED', 'APOERR_BUFFERS_OVERLAP',
    'APOERR_INVALID_APO_CLSID', 'APOERR_FORMAT_NOT_SUPPORTED',
    'APOERR_NOT_INITIALIZED', 'APOERR_ALREADY_INITIALIZED',
    'EAudioConstriction', 'AUDIO_FLOW_TYPE', 'APOInitBaseStruct',
    'APO_REG_PROPERTIES', 'PAPO_REG_PROPERTIES', 'APO_FLAG',
    'APO_CONNECTION_DESCRIPTOR', 'IAudioProcessingObjectRT',
    'IAudioProcessingObjectVBR', 'IID_IAudioProcessingObjectVBR',
    'IID_IAudioProcessingObjectRT', 'IID_IAudioProcessingObjectConfiguration',
    'IID_IAudioProcessingObject', 'IAudioProcessingObject',
    'IAudioProcessingObjectConfiguration', 'IID_IAudioSystemEffects',
    'IAudioSystemEffects', 'IID_IAudioSystemEffects2', 'IAudioSystemEffects2',
    'IAudioSystemEffectsCustomFormats', 'IID_IAudioSystemEffectsCustomFormats',
    'AudioFXExtensionParams', 'APOInitSystemEffects2', 'APOInitSystemEffects',
    '__MIDL___MIDL_itf_audioenginebaseapo_0000_0007_0001',
)
