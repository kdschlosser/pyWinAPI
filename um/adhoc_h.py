

from wtypes_h import (
    ENUM,
    ULONG,
    POINTER,
    HRESULT,
    LPWSTR,
    BOOLEAN,
    GUID,
    LPCWSTR,
    LONG,
)
from guiddef_h import (
    IID,
    DECLSPEC_UUID
)
import ctypes
import ntdef_h
import comtypes


__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
IID_IDot11AdHocManager = IID(
    '{8F10CC26-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IDot11AdHocManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDot11AdHocManager
    _idlflags_ = ['nonextensible']


CLSID_Dot11AdHocManager = DECLSPEC_UUID(
    '{DD06A84F-83BD-4d01-8AB9-2389FEA0869E}'
)

LIBID_ADHOCLib = IID(
    '{45357166-FF38-4302-8F5C-DF5B703A6E3D}'
)

class ADHOCLib(object):
    name = 'ADHOCLib'
    _reg_typelib_ = (LIBID_ADHOCLib, 1, 0)


class Dot11AdHocManager(comtypes.CoClass):
    _reg_clsid_ = CLSID_Dot11AdHocManager
    _idlflags_ = []
    _reg_typelib_ = (LIBID_ADHOCLib, 1, 0)
    _com_interfaces_ = [
        IDot11AdHocManager,
    ]



IID_IDot11AdHocManagerNotificationSink = IID(
    '{8F10CC27-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IDot11AdHocManagerNotificationSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDot11AdHocManagerNotificationSink
    _idlflags_ = []


IID_IEnumDot11AdHocNetworks = IID(
    '{8F10CC28-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IEnumDot11AdHocNetworks(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDot11AdHocNetworks
    _idlflags_ = []


IID_IDot11AdHocNetwork = IID(
    '{8F10CC29-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IDot11AdHocNetwork(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDot11AdHocNetwork
    _idlflags_ = []


IID_IDot11AdHocNetworkNotificationSink = IID(
    '{8F10CC2A-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IDot11AdHocNetworkNotificationSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDot11AdHocNetworkNotificationSink
    _idlflags_ = []


IID_IDot11AdHocInterface = IID(
    '{8F10CC2B-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IDot11AdHocInterface(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDot11AdHocInterface
    _idlflags_ = []


IID_IEnumDot11AdHocInterfaces = IID(
    '{8F10CC2C-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IEnumDot11AdHocInterfaces(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDot11AdHocInterfaces
    _idlflags_ = []


IID_IEnumDot11AdHocSecuritySettings = IID(
    '{8F10CC2D-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IEnumDot11AdHocSecuritySettings(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDot11AdHocSecuritySettings
    _idlflags_ = []


IID_IDot11AdHocSecuritySettings = IID(
    '{8F10CC2E-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IDot11AdHocSecuritySettings(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDot11AdHocSecuritySettings
    _idlflags_ = []


IID_IDot11AdHocInterfaceNotificationSink = IID(
    '{8F10CC2F-CF0D-42a0-ACBE-E2DE7007384D}'
)


class IDot11AdHocInterfaceNotificationSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDot11AdHocInterfaceNotificationSink
    _idlflags_ = []


Dot11AdHocManager = Dot11AdHocManager


from oaidl_h import * # NOQA
from winapifamily_h import * # NOQA
class tagDOT11_ADHOC_CIPHER_ALGORITHM(ENUM):
    DOT11_ADHOC_CIPHER_ALGO_INVALID = - 1
    DOT11_ADHOC_CIPHER_ALGO_NONE = 0
    DOT11_ADHOC_CIPHER_ALGO_CCMP = 0x4
    DOT11_ADHOC_CIPHER_ALGO_WEP = 0x101


DOT11_ADHOC_CIPHER_ALGORITHM = tagDOT11_ADHOC_CIPHER_ALGORITHM


class tagDOT11_ADHOC_AUTH_ALGORITHM(ENUM):
    DOT11_ADHOC_AUTH_ALGO_INVALID = - 1
    DOT11_ADHOC_AUTH_ALGO_80211_OPEN = 1
    DOT11_ADHOC_AUTH_ALGO_RSNA_PSK = 7


DOT11_ADHOC_AUTH_ALGORITHM = tagDOT11_ADHOC_AUTH_ALGORITHM


class tagDOT11_ADHOC_NETWORK_CONNECTION_STATUS(ENUM):
    DOT11_ADHOC_NETWORK_CONNECTION_STATUS_INVALID = 0
    DOT11_ADHOC_NETWORK_CONNECTION_STATUS_DISCONNECTED = 11
    DOT11_ADHOC_NETWORK_CONNECTION_STATUS_CONNECTING = 12
    DOT11_ADHOC_NETWORK_CONNECTION_STATUS_CONNECTED = 13
    DOT11_ADHOC_NETWORK_CONNECTION_STATUS_FORMED = 14


DOT11_ADHOC_NETWORK_CONNECTION_STATUS = tagDOT11_ADHOC_NETWORK_CONNECTION_STATUS


class tagDOT11_ADHOC_CONNECT_FAIL_REASON(ENUM):
    DOT11_ADHOC_CONNECT_FAIL_DOMAIN_MISMATCH = 0
    DOT11_ADHOC_CONNECT_FAIL_PASSPHRASE_MISMATCH = 1
    DOT11_ADHOC_CONNECT_FAIL_OTHER = 2


DOT11_ADHOC_CONNECT_FAIL_REASON = tagDOT11_ADHOC_CONNECT_FAIL_REASON


COMMETHOD = comtypes.COMMETHOD


IDot11AdHocManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateNetwork',
        (['in'], LPCWSTR, 'Name'),
        (['in'], LPCWSTR, 'Password'),
        (['in'], LONG, 'GeographicalId'),
        (['in'], POINTER(IDot11AdHocInterface), 'pInterface'),
        (['in'], POINTER(IDot11AdHocSecuritySettings), 'pSecurity'),
        (['in'], POINTER(GUID), 'pContextGuid'),
        (['out'], POINTER(POINTER(IDot11AdHocNetwork)), 'pIAdHoc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CommitCreatedNetwork',
        (['in'], POINTER(IDot11AdHocNetwork), 'pIAdHoc'),
        (['in'], BOOLEAN, 'fSaveProfile'),
        (['in'], BOOLEAN, 'fMakeSavedProfileUserSpecific'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIEnumDot11AdHocNetworks',
        (['in'], POINTER(GUID), 'pContextGuid'),
        (['out'], POINTER(POINTER(IEnumDot11AdHocNetworks)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIEnumDot11AdHocInterfaces',
        (['out'], POINTER(POINTER(IEnumDot11AdHocInterfaces)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNetwork',
        (['in'], POINTER(GUID), 'NetworkSignature'),
        (['out'], POINTER(POINTER(IDot11AdHocNetwork)), 'pNetwork'),
    ),
]


IDot11AdHocManagerNotificationSink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnNetworkAdd',
        (['in'], POINTER(IDot11AdHocNetwork), 'pIAdHocNetwork'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnNetworkRemove',
        (['in'], POINTER(GUID), 'Signature'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnInterfaceAdd',
        (['in'], POINTER(IDot11AdHocInterface), 'pIAdHocInterface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnInterfaceRemove',
        (['in'], POINTER(GUID), 'Signature'),
    ),
]


IEnumDot11AdHocNetworks._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cElt'),
        (['out'], POINTER(POINTER(IDot11AdHocNetwork)), 'rgElt'),
        (['out'], POINTER(ULONG), 'pcEltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cElt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumDot11AdHocNetworks)), 'ppEnum'),
    ),
]


IDot11AdHocNetwork._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetStatus',
        (['in', 'out'], POINTER(DOT11_ADHOC_NETWORK_CONNECTION_STATUS), 'eStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSSID',
        (['out'], POINTER(LPWSTR), 'ppszwSSID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HasProfile',
        (['in', 'out'], POINTER(BOOLEAN), 'pf11d'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetProfileName',
        (['out'], POINTER(LPWSTR), 'ppszwProfileName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSignalQuality',
        (['out'], POINTER(ULONG), 'puStrengthValue'),
        (['out'], POINTER(ULONG), 'puStrengthMax'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSecuritySetting',
        (['out'], POINTER(POINTER(IDot11AdHocSecuritySettings)), 'pAdHocSecuritySetting'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetContextGuid',
        (['in', 'out'], POINTER(GUID), 'pContextGuid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSignature',
        (['in', 'out'], POINTER(GUID), 'pSignature'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetInterface',
        (['out'], POINTER(POINTER(IDot11AdHocInterface)), 'pAdHocInterface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Connect',
        (['in'], LPCWSTR, 'Passphrase'),
        (['in'], LONG, 'GeographicalId'),
        (['in'], BOOLEAN, 'fSaveProfile'),
        (['in'], BOOLEAN, 'fMakeSavedProfileUserSpecific'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Disconnect'
    ),
]


IDot11AdHocNetworkNotificationSink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnStatusChange',
        ([], DOT11_ADHOC_NETWORK_CONNECTION_STATUS, 'eStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnConnectFail',
        ([], DOT11_ADHOC_CONNECT_FAIL_REASON, 'eFailReason'),
    ),
]


IDot11AdHocInterface._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDeviceSignature',
        (['in', 'out'], POINTER(GUID), 'pSignature'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFriendlyName',
        (['out'], POINTER(LPWSTR), 'ppszName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsDot11d',
        (['in', 'out'], POINTER(BOOLEAN), 'pf11d'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsAdHocCapable',
        (['in', 'out'], POINTER(BOOLEAN), 'pfAdHocCapable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsRadioOn',
        (['in', 'out'], POINTER(BOOLEAN), 'pfIsRadioOn'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetActiveNetwork',
        (['out'], POINTER(POINTER(IDot11AdHocNetwork)), 'ppNetwork'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIEnumSecuritySettings',
        (['out'], POINTER(POINTER(IEnumDot11AdHocSecuritySettings)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIEnumDot11AdHocNetworks',
        (['in'], POINTER(GUID), 'pFilterGuid'),
        (['out'], POINTER(POINTER(IEnumDot11AdHocNetworks)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStatus',
        (['in', 'out'], POINTER(DOT11_ADHOC_NETWORK_CONNECTION_STATUS), 'pState'),
    ),
]


IEnumDot11AdHocInterfaces._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cElt'),
        (['out'], POINTER(POINTER(IDot11AdHocInterface)), 'rgElt'),
        (['out'], POINTER(ULONG), 'pcEltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cElt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumDot11AdHocInterfaces)), 'ppEnum'),
    ),
]


IEnumDot11AdHocSecuritySettings._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cElt'),
        (['out'], POINTER(POINTER(IDot11AdHocSecuritySettings)), 'rgElt'),
        (['out'], POINTER(ULONG), 'pcEltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cElt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumDot11AdHocSecuritySettings)), 'ppEnum'),
    ),
]


IDot11AdHocSecuritySettings._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDot11AuthAlgorithm',
        (['in', 'out'], POINTER(DOT11_ADHOC_AUTH_ALGORITHM), 'pAuth'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDot11CipherAlgorithm',
        (['in', 'out'], POINTER(DOT11_ADHOC_CIPHER_ALGORITHM), 'pCipher'),
    ),
]


IDot11AdHocInterfaceNotificationSink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnConnectionStatusChange',
        ([], DOT11_ADHOC_NETWORK_CONNECTION_STATUS, 'eStatus'),
    ),
]



__all__ = (
    'ADHOCLib', 'IDot11AdHocInterface', 'IDot11AdHocManager',
    'CLSID_Dot11AdHocManager', 'IEnumDot11AdHocSecuritySettings',
    'LIBID_ADHOCLib', 'IDot11AdHocNetworkNotificationSink',
    'IDot11AdHocManagerNotificationSink', 'IDot11AdHocNetwork',
    'IDot11AdHocInterfaceNotificationSink', 'Dot11AdHocManager',
    'IDot11AdHocSecuritySettings', 'IEnumDot11AdHocNetworks',
    'IEnumDot11AdHocInterfaces', '__REQUIRED_RPCSAL_H_VERSION__',
    '__REQUIRED_RPCNDR_H_VERSION__', 'DOT11_ADHOC_CIPHER_ALGORITHM',
    'DOT11_ADHOC_NETWORK_CONNECTION_STATUS', 'DOT11_ADHOC_AUTH_ALGORITHM',
    'tagDOT11_ADHOC_CONNECT_FAIL_REASON', 'tagDOT11_ADHOC_CIPHER_ALGORITHM',
    'DOT11_ADHOC_CONNECT_FAIL_REASON', 'tagDOT11_ADHOC_AUTH_ALGORITHM',
    'tagDOT11_ADHOC_NETWORK_CONNECTION_STATUS',
)
