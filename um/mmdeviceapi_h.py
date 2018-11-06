__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from rpc_h import *
# from rpcndr_h import *
# from windows_h import *
# from ole2_h import *

from .wtypes_h import (
    ENUM,
    REFIID,
    DWORD,
    POINTER,
    VOID,
    HRESULT,
    LPWSTR,
    UINT,
    LPCWSTR,
    PROPERTYKEY,
    LPARAM
)

from .propidl_h import (
    PROPVARIANT,
)

from .guiddef_h import (
    DECLSPEC_UUID,
    GUID,
    DEFINE_GUID,
    IID,
)

from .propkeydef_h import DEFINE_PROPERTYKEY

import ctypes
import comtypes

from .unknwn_h import *
from .propsys_h import *
from .winapifamily_h import *

from .winerror_h import (
    ERROR_NOT_FOUND,
    ERROR_UNSUPPORTED_TYPE
)


E_NOTFOUND = ERROR_NOT_FOUND
E_UNSUPPORTED_TYPE = ERROR_UNSUPPORTED_TYPE
DEVICE_STATE_ACTIVE = 0x00000001
DEVICE_STATE_DISABLED = 0x00000002
DEVICE_STATE_NOTPRESENT = 0x00000004
DEVICE_STATE_UNPLUGGED = 0x00000008
DEVICE_STATEMASK_ALL = 0x0000000f

S_OK = 0x00000000

STGM_READ = 0x00000000
STGM_WRITE = 0x00000001
STGM_READWRITE = 0x00000002

IID_IMMNotificationClient = IID(
    '{7991EEC9-7E89-4D85-8390-6C703CEC60C0}'
)


class IMMNotificationClient(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMMNotificationClient
    _idlflags_ = []


IID_IMMDevice = IID(
    '{D666063F-1587-4E43-81F1-B948E807363F}'
)


class IMMDevice(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMMDevice
    _idlflags_ = []


IID_IMMDeviceCollection = IID(
    '{0BD7A1BE-7A1A-44DB-8397-CC5392387B5E}'
)


class IMMDeviceCollection(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMMDeviceCollection
    _idlflags_ = []


IID_IMMEndpoint = IID(
    '{1BE09788-6894-4089-8586-9A2A6C265AC5}'
)


class IMMEndpoint(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMMEndpoint
    _idlflags_ = []


IID_IMMDeviceEnumerator = IID(
    '{A95664D2-9614-4F35-A746-DE8DB63617E6}'
)


class IMMDeviceEnumerator(comtypes.IUnknown):
    _instance = None
    _case_insensitive_ = True
    _iid_ = IID_IMMDeviceEnumerator
    _idlflags_ = []


CLSID_MMDeviceEnumerator = DECLSPEC_UUID(
    '{BCDE0395-E52F-467C-8E3D-C4579291692E}'
)

LIBID_MMDeviceAPILib = IID(
    '{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}'
)


class MMDeviceAPILib(object):
    name = 'MMDeviceAPILib'
    _reg_typelib_ = (LIBID_MMDeviceAPILib, 1, 0)


class MMDeviceEnumerator(comtypes.CoClass):
    _reg_clsid_ = CLSID_MMDeviceEnumerator
    _idlflags_ = []
    _reg_typelib_ = (LIBID_MMDeviceAPILib, 1, 0)
    _com_interfaces_ = [IMMDeviceEnumerator]


IID_IMMDeviceActivator = IID(
    '{3B0D0EA4-D0A9-4B0E-935B-09516746FAC0}'
)


class IMMDeviceActivator(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMMDeviceActivator
    _idlflags_ = []


IID_IActivateAudioInterfaceCompletionHandler = IID(
    '{41D949AB-9862-444A-80F6-C261334DA5EB}'
)


class IActivateAudioInterfaceCompletionHandler(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActivateAudioInterfaceCompletionHandler
    _idlflags_ = []


IID_IActivateAudioInterfaceAsyncOperation = IID(
    '{72A22D78-CDE4-431D-B8CC-843A71199B6D}'
)


class IActivateAudioInterfaceAsyncOperation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActivateAudioInterfaceAsyncOperation
    _idlflags_ = []


PKEY_AudioEndpoint_FormFactor = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    0
)
PKEY_AudioEndpoint_ControlPanelPageProvider = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    1
)
PKEY_AudioEndpoint_Association = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    2
)
PKEY_AudioEndpoint_PhysicalSpeakers = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    3
)
PKEY_AudioEndpoint_GUID = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    4
)
PKEY_AudioEndpoint_Disable_SysFx = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    5
)


# System Effects are enabled.
ENDPOINT_SYSFX_ENABLED = 0x00000000

# System Effects are disabled.
ENDPOINT_SYSFX_DISABLED = 0x00000001


PKEY_AudioEndpoint_FullRangeSpeakers = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    6
)
PKEY_AudioEndpoint_Supports_EventDriven_Mode = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    7
)
PKEY_AudioEndpoint_JackSubType = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    8
)
PKEY_AudioEndpoint_Default_VolumeInDb = DEFINE_PROPERTYKEY(
    0x1da5d803,
    0xd492,
    0x4edd,
    0x8c,
    0x23,
    0xe0,
    0xc0,
    0xff,
    0xee,
    0x7f,
    0x0e,
    9
)
PKEY_AudioEngine_DeviceFormat = DEFINE_PROPERTYKEY(
    0xf19f064d,
    0x82c,
    0x4e27,
    0xbc,
    0x73,
    0x68,
    0x82,
    0xa1,
    0xbb,
    0x8e,
    0x4c,
    0
)
PKEY_AudioEngine_OEMFormat = DEFINE_PROPERTYKEY(
    0xe4870e26,
    0x3cc5,
    0x4cd2,
    0xba,
    0x46,
    0xca,
    0xa,
    0x9a,
    0x70,
    0xed,
    0x4,
    3
)
PKEY_AudioEndpointLogo_IconEffects = DEFINE_PROPERTYKEY(
    0xf1ab780d,
    0x2010,
    0x4ed3,
    0xa3,
    0xa6,
    0x8b,
    0x87,
    0xf0,
    0xf0,
    0xc4,
    0x76,
    0
)

PKEY_AudioEndpointLogo_IconPath = DEFINE_PROPERTYKEY(
    0xf1ab780d,
    0x2010,
    0x4ed3,
    0xa3,
    0xa6,
    0x8b,
    0x87,
    0xf0,
    0xf0,
    0xc4,
    0x76,
    1
)
PKEY_AudioEndpointSettings_MenuText = DEFINE_PROPERTYKEY(
    0x14242002,
    0x0320,
    0x4de4,
    0x95,
    0x55,
    0xa7,
    0xd8,
    0x2b,
    0x73,
    0xc2,
    0x86,
    0
)
PKEY_AudioEndpointSettings_LaunchContract = DEFINE_PROPERTYKEY(
    0x14242002,
    0x0320,
    0x4de4,
    0x95,
    0x55,
    0xa7,
    0xd8,
    0x2b,
    0x73,
    0xc2,
    0x86,
    1
)


class tagDIRECTX_AUDIO_ACTIVATION_PARAMS(ctypes.Structure):
    _fields_ = [
        ('cbDirectXAudioActivationParams', DWORD),
        ('guidAudioSession', GUID),
        ('dwAudioStreamFlags', DWORD),
    ]


DIRECTX_AUDIO_ACTIVATION_PARAMS = tagDIRECTX_AUDIO_ACTIVATION_PARAMS
PDIRECTX_AUDIO_ACTIVATION_PARAMS = POINTER(tagDIRECTX_AUDIO_ACTIVATION_PARAMS)


class __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001(ENUM):
    eRender = 0
    eCapture = eRender + 1
    eAll = eCapture + 1
    EDataFlow_enum_count = eAll + 1


EDataFlow = __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001


class __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002(ENUM):
    eConsole = 0
    eMultimedia = eConsole + 1
    eCommunications = eMultimedia + 1
    ERole_enum_count = eCommunications + 1


ERole = __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002


class __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0003(ENUM):
    RemoteNetworkDevice = 0
    Speakers = RemoteNetworkDevice + 1
    LineLevel = Speakers + 1
    Headphones = LineLevel + 1
    Microphone = Headphones + 1
    Headset = Microphone + 1
    Handset = Headset + 1
    UnknownDigitalPassthrough = Handset + 1
    SPDIF = UnknownDigitalPassthrough + 1
    DigitalAudioDisplayDevice = SPDIF + 1
    UnknownFormFactor = DigitalAudioDisplayDevice + 1
    EndpointFormFactor_enum_count = UnknownFormFactor + 1


EndpointFormFactor = __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0003
HDMI = EndpointFormFactor.DigitalAudioDisplayDevice


DEVINTERFACE_AUDIO_RENDER = DEFINE_GUID(
    0xE6327CAD,
    0xDCEC,
    0x4949,
    0xAE,
    0x8A,
    0x99,
    0x1E,
    0x97,
    0x6A,
    0x79,
    0xD2
)
DEVINTERFACE_AUDIO_CAPTURE = DEFINE_GUID(
    0x2EEF81BE,
    0x33FA,
    0x4800,
    0x96,
    0x70,
    0x1C,
    0xD4,
    0x74,
    0x97,
    0x2C,
    0x3F
)
DEVINTERFACE_MIDI_OUTPUT = DEFINE_GUID(
    0x6DC23320,
    0xAB33,
    0x4CE4,
    0x80,
    0xD4,
    0xBB,
    0xB3,
    0xEB,
    0xBF,
    0x28,
    0x14
)
DEVINTERFACE_MIDI_INPUT = DEFINE_GUID(
    0x504BE32C,
    0xCCF6,
    0x4D2C,
    0xB7,
    0x3F,
    0x6F,
    0x8B,
    0x37,
    0x47,
    0xE2,
    0x2B
)
COMMETHOD = comtypes.COMMETHOD


IMMNotificationClient._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnDeviceStateChanged',
        (['in'], LPCWSTR, 'pwstrDeviceId'),
        (['in'], DWORD, 'dwNewState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDeviceAdded',
        (['in'], LPCWSTR, 'pwstrDeviceId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDeviceRemoved',
        (['in'], LPCWSTR, 'pwstrDeviceId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDefaultDeviceChanged',
        (['in'], EDataFlow, 'flow'),
        (['in'], ERole, 'role'),
        (['in'], LPCWSTR, 'pwstrDefaultDeviceId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnPropertyValueChanged',
        (['in'], LPCWSTR, 'pwstrDeviceId'),
        (['in'], PROPERTYKEY, 'key'),
    ),
]


IMMDevice._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Activate',
        (['in'], REFIID, 'iid'),
        (['in'], DWORD, 'dwClsCtx'),
        (['in'], POINTER(PROPVARIANT), 'pActivationParams', None),
        (['out'], POINTER(POINTER(VOID)), 'ppInterface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OpenPropertyStore',
        (['in'], DWORD, 'stgmAccess'),
        (['out'], POINTER(POINTER(IPropertyStore)), 'ppProperties'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetId',
        (['out'], POINTER(LPWSTR), 'ppstrId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        (['out'], POINTER(DWORD), 'pdwState'),
    ),
]


IMMDeviceCollection._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCount',
        (['out'], POINTER(UINT), 'pcDevices'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Item',
        (['in'], UINT, 'nDevice'),
        (['out'], POINTER(POINTER(IMMDevice)), 'ppDevice'),
    ),
]


IMMEndpoint._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDataFlow',
        (['out'], POINTER(EDataFlow), 'pDataFlow'),
    ),
]


IMMDeviceEnumerator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumAudioEndpoints',
        (['in'], EDataFlow, 'dataFlow'),
        (['in'], DWORD, 'dwStateMask'),
        (['out'], POINTER(POINTER(IMMDeviceCollection)), 'ppDevices'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultAudioEndpoint',
        (['in'], EDataFlow, 'dataFlow'),
        (['in'], ERole, 'role'),
        (['out'], POINTER(POINTER(IMMDevice)), 'ppEndpoint'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDevice',
        (['in'], LPCWSTR, 'pwstrId'),
        (['out'], POINTER(POINTER(IMMDevice)), 'ppDevice'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterEndpointNotificationCallback',
        (['in'], POINTER(IMMNotificationClient), 'pClient'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterEndpointNotificationCallback',
        (['in'], POINTER(IMMNotificationClient), 'pClient'),
    ),
]


IMMDeviceActivator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Activate',
        (['in'], REFIID, 'iid'),
        (['in'], POINTER(IMMDevice), 'pDevice'),
        (['in'], POINTER(PROPVARIANT), 'pActivationParams'),
        (['out'], POINTER(POINTER(VOID)), 'ppInterface'),
    ),
]


IActivateAudioInterfaceCompletionHandler._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ActivateCompleted',
        (
            ['in'],
            POINTER(IActivateAudioInterfaceAsyncOperation),
            'activateOperation'
        ),
    ),
]


IActivateAudioInterfaceAsyncOperation._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetActivateResult',
        (['out'], POINTER(HRESULT), 'activateResult'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'activatedInterface'),
    ),
]


class __MIDL___MIDL_itf_mmdeviceapi_0000_0008_0001(ctypes.Structure):
    _fields_ = [
        ('AddPageParam', LPARAM),
        ('pEndpoint', POINTER(IMMDevice)),
        ('pPnpInterface', POINTER(IMMDevice)),
        ('pPnpDevnode', POINTER(IMMDevice)),
    ]


AudioExtensionParams = __MIDL___MIDL_itf_mmdeviceapi_0000_0008_0001


__all__ = (
    'IMMDevice', 'IMMDeviceEnumerator', 'MMDeviceEnumerator', 'IMMEndpoint',
    'IActivateAudioInterfaceAsyncOperation', 'IMMNotificationClient', 'HDMI',
    'MMDeviceAPILib', 'CLSID_MMDeviceEnumerator', 'IMMDeviceCollection',
    'IActivateAudioInterfaceCompletionHandler', 'LIBID_MMDeviceAPILib',
    'IMMDeviceActivator', 'ENDPOINT_SYSFX_ENABLED', 'DEVICE_STATE_NOTPRESENT',
    'DEVICE_STATE_UNPLUGGED', 'E_UNSUPPORTED_TYPE', 'DEVICE_STATEMASK_ALL',
    '__REQUIRED_RPCNDR_H_VERSION__', 'E_NOTFOUND',
    'DEVICE_STATE_ACTIVE', '__REQUIRED_RPCSAL_H_VERSION__', 'EDataFlow',
    'ENDPOINT_SYSFX_DISABLED', 'DEVICE_STATE_DISABLED', 'ERole',
    '__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001', 'EndpointFormFactor',
    '__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0003', 'DEVINTERFACE_MIDI_INPUT',
    '__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002', 'AudioExtensionParams',
    'DEVINTERFACE_AUDIO_RENDER', 'DEVINTERFACE_AUDIO_CAPTURE',
    'DEVINTERFACE_MIDI_OUTPUT', 'tagDIRECTX_AUDIO_ACTIVATION_PARAMS',
    'PDIRECTX_AUDIO_ACTIVATION_PARAMS', 'DIRECTX_AUDIO_ACTIVATION_PARAMS',
    '__MIDL___MIDL_itf_mmdeviceapi_0000_0008_0001',
)
