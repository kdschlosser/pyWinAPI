__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from rpc_h import *
# from rpcndr_h import *
# from windows_h import *
# from ole2_h import *

from .oaidl_h import *
from .ocidl_h import *
from .propidl_h import *
from .winapifamily_h import *
from .ks_h import *
from .ksmedia_h import *
from .winerror_h import (
    ERROR_NOT_FOUND,
)

from .wtypes_h import (
    ENUM,
    UINT,
    POINTER,
    HRESULT,
    FLOAT,
    LPCGUID,
    ULONG,
    DWORD,
    VARTYPE,
    VOID,
    LONG,
    BOOL,
    LPWSTR,
    REFIID,
    REFGUID,
    WORD,
    UCHAR,
    WCHAR,
    COLORREF,
    LONGLONG,
)
from .guiddef_h import(
    DEFINE_GUID,
    GUID,
    IID,
    DECLSPEC_UUID
)

import ctypes
import comtypes


IID_IKsControl = IID(
    '{28F54685-06FD-11D2-B27A-00A0C9223196}'
)


class IKsControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IKsControl
    _idlflags_ = []


IID_IAudioChannelConfig = IID(
    '{BB11C46F-EC28-493C-B88A-5DB88062CE98}'
)


class IAudioChannelConfig(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioChannelConfig
    _idlflags_ = []


IID_IAudioLoudness = IID(
    '{7D8B1437-DD53-4350-9C1B-1EE2890BD938}'
)


class IAudioLoudness(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioLoudness
    _idlflags_ = []


IID_IAudioInputSelector = IID(
    '{4F03DC02-5E6E-4653-8F72-A030C123D598}'
)


class IAudioInputSelector(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioInputSelector
    _idlflags_ = []


IID_IAudioOutputSelector = IID(
    '{BB515F69-94A7-429e-8B9C-271B3F11A3AB}'
)


class IAudioOutputSelector(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioOutputSelector
    _idlflags_ = []


IID_IAudioMute = IID(
    '{DF45AEEA-B74A-4B6B-AFAD-2366B6AA012E}'
)


class IAudioMute(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioMute
    _idlflags_ = []


IID_IPerChannelDbLevel = IID(
    '{C2F8E001-F205-4BC9-99BC-C13B1E048CCB}'
)


class IPerChannelDbLevel(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPerChannelDbLevel
    _idlflags_ = []


IID_IAudioBass = IID(
    '{A2B1A1D9-4DB3-425D-A2B2-BD335CB3E2E5}'
)


class IAudioBass(IPerChannelDbLevel):
    _case_insensitive_ = True
    _iid_ = IID_IAudioBass
    _idlflags_ = []


IID_IAudioMidrange = IID(
    '{5E54B6D7-B44B-40D9-9A9E-E691D9CE6EDF}'
)


class IAudioMidrange(IPerChannelDbLevel):
    _case_insensitive_ = True
    _iid_ = IID_IAudioMidrange
    _idlflags_ = []


IID_IAudioTreble = IID(
    '{0A717812-694E-4907-B74B-BAFA5CFDCA7B}'
)


class IAudioTreble(IPerChannelDbLevel):
    _case_insensitive_ = True
    _iid_ = IID_IAudioTreble
    _idlflags_ = []


IID_IAudioAutoGainControl = IID(
    '{85401FD4-6DE4-4b9d-9869-2D6753A82F3C}'
)


class IAudioAutoGainControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioAutoGainControl
    _idlflags_ = []


IID_IAudioPeakMeter = IID(
    '{DD79923C-0599-45e0-B8B6-C8DF7DB6E796}'
)


class IAudioPeakMeter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioPeakMeter
    _idlflags_ = []


IID_IKsJackDescription = IID(
    '{4509F757-2D46-4637-8E62-CE7DB944F57B}'
)


class IKsJackDescription(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IKsJackDescription
    _idlflags_ = []


IID_IKsJackDescription2 = IID(
    '{478F3A9B-E0C9-4827-9228-6F5505FFE76A}'
)


class IKsJackDescription2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IKsJackDescription2
    _idlflags_ = []


IID_IKsJackSinkInformation = IID(
    '{D9BD72ED-290F-4581-9FF3-61027A8FE532}'
)


class IKsJackSinkInformation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IKsJackSinkInformation
    _idlflags_ = []


IID_IKsJackContainerId = IID(
    '{C99AF463-D629-4EC4-8C00-E54D68154248}'
)


class IKsJackContainerId(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IKsJackContainerId
    _idlflags_ = []


IID_IPart = IID(
    '{AE2DE0E4-5BCA-4F2D-AA46-5D13F8FDB3A9}'
)


class IPart(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPart
    _idlflags_ = []


IID_IConnector = IID(
    '{9c2c4058-23f5-41de-877a-df3af236a09e}'
)


class IConnector(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IConnector
    _idlflags_ = []


IID_ISubunit = IID(
    '{82149A85-DBA6-4487-86BB-EA8F7FEFCC71}'
)


class ISubunit(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISubunit
    _idlflags_ = []


IID_IControlInterface = IID(
    '{45d37c3f-5140-444a-ae24-400789f3cbf3}'
)


class IControlInterface(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IControlInterface
    _idlflags_ = []


IID_IControlChangeNotify = IID(
    '{A09513ED-C709-4d21-BD7B-5F34C47F3947}'
)


class IControlChangeNotify(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IControlChangeNotify
    _idlflags_ = []


IID_IDeviceTopology = IID(
    '{2A07407E-6497-4A18-9787-32F79BD0D98F}'
)


class IDeviceTopology(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDeviceTopology
    _idlflags_ = ['nonextensible']


CLSID_DeviceTopology = DECLSPEC_UUID(
    '{1DF639D0-5EC1-47AA-9379-828DC1AA8C59}'
)

LIBID_DevTopologyLib = IID(
    '{51B9A01D-8181-4363-B59C-E678F476DD0E}'
)


class DevTopologyLib(object):
    name = 'DevTopologyLib'
    _reg_typelib_ = (LIBID_DevTopologyLib, 1, 0)


IID_IPartsList = IID(
    '{6DAA848C-5EB0-45CC-AEA5-998A2CDA1FFB}'
)


class IPartsList(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPartsList
    _idlflags_ = []


IID_IAudioVolumeLevel = IID(
    '{7FB7B48F-531D-44A2-BCB3-5AD5A134B3DC}'
)


class IAudioVolumeLevel(IPerChannelDbLevel):
    _case_insensitive_ = True
    _iid_ = IID_IAudioVolumeLevel
    _idlflags_ = []


IID_IDeviceSpecificProperty = IID(
    '{3B22BCBF-2586-4af0-8583-205D391B807C}'
)


class IDeviceSpecificProperty(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDeviceSpecificProperty
    _idlflags_ = []


IID_IKsFormatSupport = IID(
    '{3CB4A69D-BB6F-4D2B-95B7-452D2C155DB5}'
)


class IKsFormatSupport(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IKsFormatSupport
    _idlflags_ = []


class DeviceTopology(comtypes.CoClass):
    _reg_clsid_ = CLSID_DeviceTopology
    _idlflags_ = []
    _reg_typelib_ = (LIBID_DevTopologyLib, 1, 0)
    _com_interfaces_ = [IDeviceTopology]
    IPartsList = IPartsList
    IAudioVolumeLevel = IAudioVolumeLevel
    IAudioLoudness = IAudioLoudness
    IAudioInputSelector = IAudioInputSelector
    IAudioMute = IAudioMute
    IAudioBass = IAudioBass
    IAudioMidrange = IAudioMidrange
    IAudioTreble = IAudioTreble
    IAudioAutoGainControl = IAudioAutoGainControl
    IAudioOutputSelector = IAudioOutputSelector
    IAudioPeakMeter = IAudioPeakMeter
    IDeviceSpecificProperty = IDeviceSpecificProperty
    IKsFormatSupport = IKsFormatSupport


E_NOTFOUND = ERROR_NOT_FOUND


DEVTOPO_HARDWARE_INITIATED_EVENTCONTEXT = 'draH'
EVENTCONTEXT_VOLUMESLIDER = DEFINE_GUID(
    0xE2C2E9DE,
    0x09B1,
    0x4B04,
    0x84,
    0xE5,
    0x07,
    0x93,
    0x12,
    0x25,
    0xEE,
    0x04
)


class __MIDL___MIDL_itf_devicetopology_0000_0000_0001(ctypes.Structure):
    _fields_ = [
        ('FormatSize', ULONG),
        ('Flags', ULONG),
        ('SampleSize', ULONG),
        ('Reserved', ULONG),
        ('MajorFormat', GUID),
        ('SubFormat', GUID),
        ('Specifier', GUID),
    ]


KSDATAFORMAT = __MIDL___MIDL_itf_devicetopology_0000_0000_0001
PKSDATAFORMAT = POINTER(__MIDL___MIDL_itf_devicetopology_0000_0000_0001)


class __MIDL___MIDL_itf_devicetopology_0000_0000_0002(ctypes.Structure):

    class _Union_0(ctypes.Union):

        class _Struct_0(ctypes.Structure):
            _fields_ = [
                ('Set', GUID),
                ('Id', ULONG),
                ('Flags', ULONG),
            ]

        _anonymous_ = ('_Struct_0', )
        _fields_ = [
            ('_Struct_0', _Struct_0),
            ('Alignment', LONGLONG),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('_Union_0', _Union_0),
    ]


KSIDENTIFIER = __MIDL___MIDL_itf_devicetopology_0000_0000_0002
PKSIDENTIFIER = POINTER(__MIDL___MIDL_itf_devicetopology_0000_0000_0002)


KSPROPERTY = KSIDENTIFIER
PKSPROPERTY = POINTER(KSIDENTIFIER)
KSMETHOD = KSIDENTIFIER
PKSMETHOD = POINTER(KSIDENTIFIER)
KSEVENT = KSIDENTIFIER
PKSEVENT = POINTER(KSIDENTIFIER)


class __MIDL___MIDL_itf_devicetopology_0000_0000_0005(ENUM):
    eConnTypeUnknown = 0
    eConnType3Point5mm = eConnTypeUnknown + 1
    eConnTypeQuarter = eConnType3Point5mm + 1
    eConnTypeAtapiInternal = eConnTypeQuarter + 1
    eConnTypeRCA = eConnTypeAtapiInternal + 1
    eConnTypeOptical = eConnTypeRCA + 1
    eConnTypeOtherDigital = eConnTypeOptical + 1
    eConnTypeOtherAnalog = eConnTypeOtherDigital + 1
    eConnTypeMultichannelAnalogDIN = eConnTypeOtherAnalog + 1
    eConnTypeXlrProfessional = eConnTypeMultichannelAnalogDIN + 1
    eConnTypeRJ11Modem = eConnTypeXlrProfessional + 1
    eConnTypeCombination = eConnTypeRJ11Modem + 1
    eConnTypeEighth = eConnType3Point5mm

EPcxConnectionType = __MIDL___MIDL_itf_devicetopology_0000_0000_0005


class __MIDL___MIDL_itf_devicetopology_0000_0000_0006(ENUM):
    eGeoLocRear = 0x1
    eGeoLocFront = eGeoLocRear + 1
    eGeoLocLeft = eGeoLocFront + 1
    eGeoLocRight = eGeoLocLeft + 1
    eGeoLocTop = eGeoLocRight + 1
    eGeoLocBottom = eGeoLocTop + 1
    eGeoLocRearPanel = eGeoLocBottom + 1
    eGeoLocRiser = eGeoLocRearPanel + 1
    eGeoLocInsideMobileLid = eGeoLocRiser + 1
    eGeoLocDrivebay = eGeoLocInsideMobileLid + 1
    eGeoLocHDMI = eGeoLocDrivebay + 1
    eGeoLocOutsideMobileLid = eGeoLocHDMI + 1
    eGeoLocATAPI = eGeoLocOutsideMobileLid + 1
    eGeoLocNotApplicable = eGeoLocATAPI + 1
    eGeoLocReserved6 = eGeoLocNotApplicable + 1
    eGeoLocRearOPanel = eGeoLocRearPanel


EPcxGeoLocation = __MIDL___MIDL_itf_devicetopology_0000_0000_0006


class __MIDL___MIDL_itf_devicetopology_0000_0000_0007(ENUM):
    eGenLocPrimaryBox = 0
    eGenLocInternal = eGenLocPrimaryBox + 1
    eGenLocSeparate = eGenLocInternal + 1
    eGenLocOther = eGenLocSeparate + 1


EPcxGenLocation = __MIDL___MIDL_itf_devicetopology_0000_0000_0007


class __MIDL___MIDL_itf_devicetopology_0000_0000_0008(ENUM):
    ePortConnJack = 0
    ePortConnIntegratedDevice = ePortConnJack + 1
    ePortConnBothIntegratedAndJack = ePortConnIntegratedDevice + 1
    ePortConnUnknown = ePortConnBothIntegratedAndJack + 1


EPxcPortConnection = __MIDL___MIDL_itf_devicetopology_0000_0000_0008


class __MIDL___MIDL_itf_devicetopology_0000_0000_0009(ctypes.Structure):
    _fields_ = [
        ('ChannelMapping', DWORD),
        ('Color', COLORREF),
        ('ConnectionType', EPcxConnectionType),
        ('GeoLocation', EPcxGeoLocation),
        ('GenLocation', EPcxGenLocation),
        ('PortConnection', EPxcPortConnection),
        ('IsConnected', BOOL),
    ]


KSJACK_DESCRIPTION = __MIDL___MIDL_itf_devicetopology_0000_0000_0009
PKSJACK_DESCRIPTION = POINTER(__MIDL___MIDL_itf_devicetopology_0000_0000_0009)


class _LUID(ctypes.Structure):
    _fields_ = [
        ('LowPart', DWORD),
        ('HighPart', LONG),
    ]


LUID = _LUID
PLUID = POINTER(_LUID)


class __MIDL___MIDL_itf_devicetopology_0000_0000_0010(ENUM):
    KSJACK_SINK_CONNECTIONTYPE_HDMI = 0
    KSJACK_SINK_CONNECTIONTYPE_DISPLAYPORT = (
        KSJACK_SINK_CONNECTIONTYPE_HDMI + 1
    )


KSJACK_SINK_CONNECTIONTYPE = __MIDL___MIDL_itf_devicetopology_0000_0000_0010


class _tagKSJACK_SINK_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('ConnType', KSJACK_SINK_CONNECTIONTYPE),
        ('ManufacturerId', WORD),
        ('ProductId', WORD),
        ('AudioLatency', WORD),
        ('HDCPCapable', BOOL),
        ('AICapable', BOOL),
        ('SinkDescriptionLength', UCHAR),
        ('SinkDescription', WCHAR * 32),
        ('PortId', LUID),
    ]


KSJACK_SINK_INFORMATION = _tagKSJACK_SINK_INFORMATION


class _tagKSJACK_DESCRIPTION2(ctypes.Structure):
    _fields_ = [
        ('DeviceStateInfo', DWORD),
        ('JackCapabilities', DWORD),
    ]


KSJACK_DESCRIPTION2 = _tagKSJACK_DESCRIPTION2
PKSJACK_DESCRIPTION2 = POINTER(_tagKSJACK_DESCRIPTION2)


class __MIDL___MIDL_itf_devicetopology_0000_0000_0011(ENUM):
    In = 0
    Out = In + 1


DataFlow = __MIDL___MIDL_itf_devicetopology_0000_0000_0011


class __MIDL___MIDL_itf_devicetopology_0000_0000_0012(ENUM):
    Connector = 0
    Subunit = Connector + 1

PartType = __MIDL___MIDL_itf_devicetopology_0000_0000_0012


class __MIDL___MIDL_itf_devicetopology_0000_0000_0013(ENUM):
    Unknown_Connector = 0
    Physical_Internal = Unknown_Connector + 1
    Physical_External = Physical_Internal + 1
    Software_IO = Physical_External + 1
    Software_Fixed = Software_IO + 1
    Network = Software_Fixed + 1


ConnectorType = __MIDL___MIDL_itf_devicetopology_0000_0000_0013


COMMETHOD = comtypes.COMMETHOD


IKsControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'KsProperty',
        (['in'], PKSPROPERTY, 'Property'),
        (['in'], ULONG, 'PropertyLength'),
        (['in', 'out'], POINTER(VOID), 'PropertyData'),
        (['in'], ULONG, 'DataLength'),
        (['out'], POINTER(ULONG), 'BytesReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'KsMethod',
        (['in'], PKSMETHOD, 'Method'),
        (['in'], ULONG, 'MethodLength'),
        (['in', 'out'], POINTER(VOID), 'MethodData'),
        (['in'], ULONG, 'DataLength'),
        (['out'], POINTER(ULONG), 'BytesReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'KsEvent',
        (['in'], PKSEVENT, 'Event'),
        (['in'], ULONG, 'EventLength'),
        (['in', 'out'], POINTER(VOID), 'EventData'),
        (['in'], ULONG, 'DataLength'),
        (['out'], POINTER(ULONG), 'BytesReturned'),
    ),
]


IPerChannelDbLevel._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetChannelCount',
        (['out'], POINTER(UINT), 'pcChannels'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLevelRange',
        (['in'], UINT, 'nChannel'),
        (['out'], POINTER(FLOAT), 'pfMinLevelDB'),
        (['out'], POINTER(FLOAT), 'pfMaxLevelDB'),
        (['out'], POINTER(FLOAT), 'pfStepping'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLevel',
        (['in'], UINT, 'nChannel'),
        (['out'], POINTER(FLOAT), 'pfLevelDB'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLevel',
        (['in'], UINT, 'nChannel'),
        (['in'], FLOAT, 'fLevelDB'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLevelUniform',
        (['in'], FLOAT, 'fLevelDB'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLevelAllChannels',
        (['in'], FLOAT * 1, 'aLevelsDB'),
        (['in'], ULONG, 'cChannels'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
]


IAudioChannelConfig._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetChannelConfig',
        (['in'], DWORD, 'dwConfig'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetChannelConfig',
        (['out', 'retval'], POINTER(DWORD), 'pdwConfig'),
    ),
]


IAudioLoudness._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetEnabled',
        (['out'], POINTER(BOOL), 'pbEnabled'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetEnabled',
        (['in'], BOOL, 'bEnable'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
]


IAudioInputSelector._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSelection',
        (['out'], POINTER(UINT), 'pnIdSelected'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSelection',
        (['in'], UINT, 'nIdSelect'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
]


IAudioOutputSelector._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSelection',
        (['out'], POINTER(UINT), 'pnIdSelected'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSelection',
        (['in'], UINT, 'nIdSelect'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
]


IAudioMute._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetMute',
        (['in'], BOOL, 'bMuted'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMute',
        (['out'], POINTER(BOOL), 'pbMuted'),
    ),
]


IAudioAutoGainControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetEnabled',
        (['out'], POINTER(BOOL), 'pbEnabled'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetEnabled',
        (['in'], BOOL, 'bEnable'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
]


IAudioPeakMeter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetChannelCount',
        (['out'], POINTER(UINT), 'pcChannels'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLevel',
        (['in'], UINT, 'nChannel'),
        (['out'], POINTER(FLOAT), 'pfLevel'),
    ),
]


IDeviceSpecificProperty._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetType',
        (['out'], POINTER(VARTYPE), 'pVType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetValue',
        (['out'], POINTER(VOID), 'pvValue'),
        (['in', 'out'], POINTER(DWORD), 'pcbValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetValue',
        (['in'], POINTER(VOID), 'pvValue'),
        (['in'], DWORD, 'cbValue'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Get4BRange',
        (['out'], POINTER(LONG), 'plMin'),
        (['out'], POINTER(LONG), 'plMax'),
        (['out'], POINTER(LONG), 'plStepping'),
    ),
]


IKsFormatSupport._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'IsFormatSupported',
        (['in'], PKSDATAFORMAT, 'pKsFormat'),
        (['in'], DWORD, 'cbFormat'),
        (['out'], POINTER(BOOL), 'pbSupported'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDevicePreferredFormat',
        (['out'], POINTER(PKSDATAFORMAT), 'ppKsFormat'),
    ),
]


IKsJackDescription._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetJackCount',
        (['out'], POINTER(UINT), 'pcJacks'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetJackDescription',
        (['in'], UINT, 'nJack'),
        (['out'], POINTER(KSJACK_DESCRIPTION), 'pDescription'),
    ),
]


IKsJackDescription2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetJackCount',
        (['out'], POINTER(UINT), 'pcJacks'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetJackDescription2',
        (['in'], UINT, 'nJack'),
        (['out'], POINTER(KSJACK_DESCRIPTION2), 'pDescription2'),
    ),
]


IKsJackSinkInformation._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetJackSinkInformation',
        (['out'], POINTER(KSJACK_SINK_INFORMATION), 'pJackSinkInformation'),
    ),
]


IKsJackContainerId._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetJackContainerId',
        (['out'], POINTER(GUID), 'pJackContainerId'),
    ),
]


IPartsList._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCount',
        (['out'], POINTER(UINT), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPart',
        (['in'], UINT, 'nIndex'),
        (['out'], POINTER(POINTER(IPart)), 'ppPart'),
    ),
]


IPart._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetName',
        (['out'], POINTER(LPWSTR), 'ppwstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLocalId',
        (['out'], POINTER(UINT), 'pnId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetGlobalId',
        (['out'], POINTER(LPWSTR), 'ppwstrGlobalId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPartType',
        (['out'], POINTER(PartType), 'pPartType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSubType',
        (['out'], POINTER(GUID), 'pSubType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetControlInterfaceCount',
        (['out'], POINTER(UINT), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetControlInterface',
        (['in'], UINT, 'nIndex'),
        (['out'], POINTER(POINTER(IControlInterface)), 'ppInterfaceDesc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumPartsIncoming',
        (['out'], POINTER(POINTER(IPartsList)), 'ppParts'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumPartsOutgoing',
        (['out'], POINTER(POINTER(IPartsList)), 'ppParts'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTopologyObject',
        (['out'], POINTER(POINTER(IDeviceTopology)), 'ppTopology'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Activate',
        (['in'], DWORD, 'dwClsContext'),
        (['in'], REFIID, 'refiid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterControlChangeCallback',
        (['in'], REFGUID, 'riid'),
        (['in'], POINTER(IControlChangeNotify), 'pNotify'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterControlChangeCallback',
        (['in'], POINTER(IControlChangeNotify), 'pNotify'),
    ),
]


IConnector._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetType',
        (['out'], POINTER(ConnectorType), 'pType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDataFlow',
        (['out'], POINTER(DataFlow), 'pFlow'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectTo',
        (['in'], POINTER(IConnector), 'pConnectTo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsConnected',
        (['out'], POINTER(BOOL), 'pbConnected'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetConnectedTo',
        (['out'], POINTER(POINTER(IConnector)), 'ppConTo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetConnectorIdConnectedTo',
        (['out'], POINTER(LPWSTR), 'ppwstrConnectorId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDeviceIdConnectedTo',
        (['out'], POINTER(LPWSTR), 'ppwstrDeviceId'),
    ),
]

IControlInterface._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetName',
        (['out'], POINTER(LPWSTR), 'ppwstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIID',
        (['out'], POINTER(GUID), 'pIID'),
    ),
]


IControlChangeNotify._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnNotify',
        (['in'], DWORD, 'dwSenderProcessId'),
        (['in'], LPCGUID, 'pguidEventContext'),
    ),
]

IDeviceTopology._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetConnectorCount',
        (['out'], POINTER(UINT), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetConnector',
        (['in'], UINT, 'nIndex'),
        (['out'], POINTER(POINTER(IConnector)), 'ppConnector'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSubunitCount',
        (['out'], POINTER(UINT), 'pCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSubunit',
        (['in'], UINT, 'nIndex'),
        (['out'], POINTER(POINTER(ISubunit)), 'ppSubunit'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPartById',
        (['in'], UINT, 'nId'),
        (['out'], POINTER(POINTER(IPart)), 'ppPart'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDeviceId',
        (['out'], POINTER(LPWSTR), 'ppwstrDeviceId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSignalPath',
        (['in'], POINTER(IPart), 'pIPartFrom'),
        (['in'], POINTER(IPart), 'pIPartTo'),
        (['in'], BOOL, 'bRejectMixedPaths'),
        (['out'], POINTER(POINTER(IPartsList)), 'ppParts'),
    ),
]


__all__ = (
    'IControlInterface', 'IAudioMidrange', 'IAudioInputSelector', 'IPart',
    'DevTopologyLib', 'IKsJackContainerId', 'CLSID_DeviceTopology', '_LUID',
    'LIBID_DevTopologyLib', 'IAudioBass', 'IControlChangeNotify', 'ISubunit',
    'DeviceTopology', 'IConnector', 'IAudioMute', 'IKsJackSinkInformation',
    'IAudioOutputSelector', 'IAudioVolumeLevel', 'IDeviceSpecificProperty',
    'IKsFormatSupport', 'IAudioLoudness', 'IAudioTreble', 'IPartsList',
    'IAudioAutoGainControl', 'IDeviceTopology', 'IKsJackDescription',
    'IAudioPeakMeter', 'IKsJackDescription2', 'IAudioChannelConfig',
    'IPerChannelDbLevel', 'IKsControl', '__REQUIRED_RPCSAL_H_VERSION__',
    'E_NOTFOUND', '__REQUIRED_RPCNDR_H_VERSION__', 'EPcxConnectionType',
    'DEVTOPO_HARDWARE_INITIATED_EVENTCONTEXT', 'PartType', 'DataFlow',
    'ConnectorType', '__MIDL___MIDL_itf_devicetopology_0000_0000_0012',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0013', 'EPxcPortConnection',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0010', 'EPcxGenLocation',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0011', 'EPcxGeoLocation',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0005', 'KSDATAFORMAT',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0007', 'PKSIDENTIFIER',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0006', 'PKSJACK_DESCRIPTION',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0008', 'PKSJACK_DESCRIPTION2',
    'KSJACK_SINK_CONNECTIONTYPE', 'EVENTCONTEXT_VOLUMESLIDER', 'KSIDENTIFIER',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0001', 'KSJACK_DESCRIPTION2',
    'KSJACK_SINK_INFORMATION', '_tagKSJACK_DESCRIPTION2', 'PKSDATAFORMAT',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0009', 'KSJACK_DESCRIPTION',
    '__MIDL___MIDL_itf_devicetopology_0000_0000_0002', 'PKSMETHOD', 'KSEVENT',
    '_tagKSJACK_SINK_INFORMATION', 'PKSPROPERTY', 'PKSEVENT', 'KSMETHOD',
    'KSPROPERTY',
)
