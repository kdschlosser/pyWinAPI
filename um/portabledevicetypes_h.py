import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__PortableDeviceTypes_h__ = None
__IWpdSerializer_FWD_DEFINED__ = None
__IPortableDeviceValues_FWD_DEFINED__ = None
__IPortableDeviceKeyCollection_FWD_DEFINED__ = None
__IPortableDevicePropVariantCollection_FWD_DEFINED__ = None
__IPortableDeviceValuesCollection_FWD_DEFINED__ = None
__WpdSerializer_FWD_DEFINED__ = None
__PortableDeviceValues_FWD_DEFINED__ = None
__PortableDeviceKeyCollection_FWD_DEFINED__ = None
__PortableDevicePropVariantCollection_FWD_DEFINED__ = None
__PortableDeviceValuesCollection_FWD_DEFINED__ = None
__IWpdSerializer_INTERFACE_DEFINED__ = None
__IPortableDeviceValues_INTERFACE_DEFINED__ = None
__IPortableDeviceKeyCollection_INTERFACE_DEFINED__ = None
__IPortableDevicePropVariantCollection_INTERFACE_DEFINED__ = None
__IPortableDeviceValuesCollection_INTERFACE_DEFINED__ = None
__PortableDeviceTypesLib_LIBRARY_DEFINED__ = None


def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    pass
# END IF


# verify that the <rpcsal.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    pass
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H


if not defined(__PortableDeviceTypes_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IWpdSerializer_FWD_DEFINED__):
        class IWpdSerializer(comtypes.IUnknown):
            """
            IWpdSerializer Interface
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IWpdSerializer

    # END IF  __IWpdSerializer_FWD_DEFINED__

    if not defined(__IPortableDeviceValues_FWD_DEFINED__):
        class IPortableDeviceValues(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceValues_FWD_DEFINED__

    if not defined(__IPortableDeviceKeyCollection_FWD_DEFINED__):
        class IPortableDeviceKeyCollection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceKeyCollection_FWD_DEFINED__

    if not defined(__IPortableDevicePropVariantCollection_FWD_DEFINED__):
        class IPortableDevicePropVariantCollection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDevicePropVariantCollection_FWD_DEFINED__

    if not defined(__IPortableDeviceValuesCollection_FWD_DEFINED__):
        class IPortableDeviceValuesCollection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceValuesCollection_FWD_DEFINED__

    if not defined(__WpdSerializer_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:

            CLSID_WpdSerializer = CLSID(
                '{0b91a74b-ad7c-4a9d-b563-29eef9167172}'
            )

            class WpdSerializer(comtypes.CoClass):
                """
                WpdSerializer Class
                """
                _reg_clsid_ = CLSID_WpdSerializer
                _idlflags_ = []
                _com_interfaces_ = [IWpdSerializer]

        # END IF  __cplusplus
    # END IF  __WpdSerializer_FWD_DEFINED__

    if not defined(__PortableDeviceValues_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceValues = CLSID(
                '{0c15d503-d017-47ce-9016-7b3f978721cc}'
            )


            class PortableDeviceValues(comtypes.CoClass):
                """
                Portable Device Values Class
                """
                _reg_clsid_ = CLSID_PortableDeviceValues
                _idlflags_ = []
                _com_interfaces_ = [IPortableDeviceValues]

        # END IF  __cplusplus
    # END IF  __PortableDeviceValues_FWD_DEFINED__

    if not defined(__PortableDeviceKeyCollection_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceKeyCollection = CLSID(
                '{de2d022d-2480-43be-97f0-d1fa2cf98f4f}'
            )


            class PortableDeviceKeyCollection(comtypes.CoClass):
                """
                Portable Device PROPERTYKEY collection
                """
                _reg_clsid_ = CLSID_PortableDeviceKeyCollection
                _idlflags_ = []
                _com_interfaces_ = [IPortableDeviceKeyCollection]

        # END IF  __cplusplus
    # END IF  __PortableDeviceKeyCollection_FWD_DEFINED__

    if not defined(__PortableDevicePropVariantCollection_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDevicePropVariantCollection = CLSID(
                '{de2d022d-2480-43be-97f0-d1fa2cf98f4f}'
            )


            class PortableDevicePropVariantCollection(comtypes.CoClass):
                """
                Portable Device PROPVARIANT collection
                """
                _reg_clsid_ = CLSID_PortableDevicePropVariantCollection
                _idlflags_ = []
                _com_interfaces_ = [IPortableDevicePropVariantCollection]

        # END IF  __cplusplus
    # END IF  __PortableDevicePropVariantCollection_FWD_DEFINED__

    if not defined(__PortableDeviceValuesCollection_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceValuesCollection = CLSID(
                '{3882134d-14cf-4220-9cb4-435f86d83f60}'
            )


            class PortableDeviceValuesCollection(comtypes.CoClass):
                """
                Portable Device Values collection
                """
                _reg_clsid_ = CLSID_PortableDeviceValuesCollection
                _idlflags_ = []
                _com_interfaces_ = [IPortableDeviceValuesCollection]

        # END IF  __cplusplus
    # END IF  __PortableDeviceValuesCollection_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.oaidl_h import * # NOQA
    from pyWinAPI.um.ocidl_h import * # NOQA
    from pyWinAPI.um.propsys_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_PortableDeviceTypes_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if _WIN32_WINNT >= 0x0501:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            class tagWPD_STREAM_UNITS(ENUM):
                WPD_STREAM_UNITS_BYTES = 0L
                WPD_STREAM_UNITS_FRAMES = 0x1
                WPD_STREAM_UNITS_ROWS = 0x2
                WPD_STREAM_UNITS_MILLISECONDS = 0x4
                WPD_STREAM_UNITS_MICROSECONDS = 0x8

            WPD_STREAM_UNITS = tagWPD_STREAM_UNITS
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            if not defined(__IWpdSerializer_INTERFACE_DEFINED__):
                # interface IWpdSerializer
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IWpdSerializer = MIDL_INTERFACE(
                        "{B32F4002-BB27-45FF-AF4F-06631C1E8DAD}"
                    )
                    IWpdSerializer._iid_ = IID_IWpdSerializer

                    IWpdSerializer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetIPortableDeviceValuesFromBuffer')],
                            HRESULT,
                            'GetIPortableDeviceValuesFromBuffer',
                            (['in'], POINTER(BYTE), 'pBuffer'),
                            (['in'], DWORD, 'dwInputBufferLength'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppParams'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method WriteIPortableDeviceValuesToBuffer')],
                            HRESULT,
                            'WriteIPortableDeviceValuesToBuffer',
                            (['in'], DWORD, 'dwOutputBufferLength'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pResults'
                            ),
                            (['out'], POINTER(BYTE), 'pBuffer'),
                            (['out'], POINTER(DWORD), 'pdwBytesWritten'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBufferFromIPortableDeviceValues')],
                            HRESULT,
                            'GetBufferFromIPortableDeviceValues',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pSource'
                            ),
                            (['out'], POINTER(POINTER(BYTE)), 'ppBuffer'),
                            (['out'], POINTER(DWORD), 'pdwBufferSize'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSerializedSize')],
                            HRESULT,
                            'GetSerializedSize',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pSource'
                            ),
                            (['out'], POINTER(DWORD), 'pdwSize'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IWpdSerializer_INTERFACE_DEFINED__

            # interface __MIDL_itf_PortableDeviceTypes_0000_0001
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IPortableDeviceValues_INTERFACE_DEFINED__):
                # interface IPortableDeviceValues
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceValues = MIDL_INTERFACE(
                        "{6848F6F2-3155-4F86-B6F5-263EEEAB3143}"
                    )
                    IPortableDeviceValues._iid_ = IID_IPortableDeviceValues

                    IPortableDeviceValues._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCount')],
                            HRESULT,
                            'GetCount',
                            (['in'], POINTER(DWORD), 'pcelt'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAt')],
                            HRESULT,
                            'GetAt',
                            (['in'], DWORD, 'index'),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(PROPERTYKEY),
                               'pKey'
                            ),
                            (
                                ['unique', 'out', 'in'],
                                POINTER(PROPVARIANT),
                               'pValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetValue')],
                            HRESULT,
                            'SetValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], POINTER(PROPVARIANT), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetValue')],
                            HRESULT,
                            'GetValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(PROPVARIANT), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStringValue')],
                            HRESULT,
                            'SetStringValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], LPCWSTR, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStringValue')],
                            HRESULT,
                            'GetStringValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(LPWSTR), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetUnsignedIntegerValue')],
                            HRESULT,
                            'SetUnsignedIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], ULONG, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetUnsignedIntegerValue')],
                            HRESULT,
                            'GetUnsignedIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(ULONG), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSignedIntegerValue')],
                            HRESULT,
                            'SetSignedIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], LONG, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSignedIntegerValue')],
                            HRESULT,
                            'GetSignedIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(LONG), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetUnsignedLargeIntegerValue')],
                            HRESULT,
                            'SetUnsignedLargeIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], ULONGLONG, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetUnsignedLargeIntegerValue')],
                            HRESULT,
                            'GetUnsignedLargeIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(ULONGLONG), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSignedLargeIntegerValue')],
                            HRESULT,
                            'SetSignedLargeIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], LONGLONG, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSignedLargeIntegerValue')],
                            HRESULT,
                            'GetSignedLargeIntegerValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(LONGLONG), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetFloatValue')],
                            HRESULT,
                            'SetFloatValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], FLOAT, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFloatValue')],
                            HRESULT,
                            'GetFloatValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(FLOAT), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetErrorValue')],
                            HRESULT,
                            'SetErrorValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], HRESULT, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetErrorValue')],
                            HRESULT,
                            'GetErrorValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(HRESULT), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetKeyValue')],
                            HRESULT,
                            'SetKeyValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], REFPROPERTYKEY, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetKeyValue')],
                            HRESULT,
                            'GetKeyValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(PROPERTYKEY), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetBoolValue')],
                            HRESULT,
                            'SetBoolValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], BOOL, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBoolValue')],
                            HRESULT,
                            'GetBoolValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(BOOL), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetIUnknownValue')],
                            HRESULT,
                            'SetIUnknownValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], POINTER(comtypes.IUnknown), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetIUnknownValue')],
                            HRESULT,
                            'GetIUnknownValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                               'ppValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetGuidValue')],
                            HRESULT,
                            'SetGuidValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], REFGUID, 'Value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetGuidValue')],
                            HRESULT,
                            'GetGuidValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(GUID), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetBufferValue')],
                            HRESULT,
                            'SetBufferValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['in'], POINTER(BYTE), 'pValue'),
                            (['in'], DWORD, 'cbValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBufferValue')],
                            HRESULT,
                            'GetBufferValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (['out'], POINTER(POINTER(BYTE)), 'ppValue'),
                            (['out'], POINTER(DWORD), 'pcbValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetIPortableDeviceValuesValue')],
                            HRESULT,
                            'SetIPortableDeviceValuesValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetIPortableDeviceValuesValue')],
                            HRESULT,
                            'GetIPortableDeviceValuesValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetIPortableDevicePropVariantCollectionValue')],
                            HRESULT,
                            'SetIPortableDevicePropVariantCollectionValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['in'],
                                POINTER(IPortableDevicePropVariantCollection),
                               'pValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetIPortableDevicePropVariantCollectionValue')],
                            HRESULT,
                            'GetIPortableDevicePropVariantCollectionValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetIPortableDeviceKeyCollectionValue')],
                            HRESULT,
                            'SetIPortableDeviceKeyCollectionValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceKeyCollection),
                               'pValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetIPortableDeviceKeyCollectionValue')],
                            HRESULT,
                            'GetIPortableDeviceKeyCollectionValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceKeyCollection)),
                               'ppValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetIPortableDeviceValuesCollectionValue')],
                            HRESULT,
                            'SetIPortableDeviceValuesCollectionValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValuesCollection),
                               'pValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetIPortableDeviceValuesCollectionValue')],
                            HRESULT,
                            'GetIPortableDeviceValuesCollectionValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValuesCollection)),
                               'ppValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveValue')],
                            HRESULT,
                            'RemoveValue',
                            (['in'], REFPROPERTYKEY, 'key'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CopyValuesFromPropertyStore')],
                            HRESULT,
                            'CopyValuesFromPropertyStore',
                            (['in'], POINTER(IPropertyStore), 'pStore'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CopyValuesToPropertyStore')],
                            HRESULT,
                            'CopyValuesToPropertyStore',
                            (['in'], POINTER(IPropertyStore), 'pStore'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Clear')],
                            HRESULT,
                            'Clear',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceValues_INTERFACE_DEFINED__

            # interface __MIDL_itf_PortableDeviceTypes_0000_0002
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP) and not WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IPortableDeviceKeyCollection_INTERFACE_DEFINED__):
                # interface IPortableDeviceKeyCollection
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceKeyCollection = MIDL_INTERFACE(
                        "{DADA2357-E0AD-492E-98DB-DD61C53BA353}"
                    )
                    IPortableDeviceKeyCollection._iid_ = IID_IPortableDeviceKeyCollection

                    IPortableDeviceKeyCollection._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCount')],
                            HRESULT,
                            'GetCount',
                            (['in'], POINTER(DWORD), 'pcElems'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAt')],
                            HRESULT,
                            'GetAt',
                            (['in'], DWORD, 'dwIndex'),
                            (['in'], POINTER(PROPERTYKEY), 'pKey'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Add')],
                            HRESULT,
                            'Add',
                            (['in'], REFPROPERTYKEY, 'Key'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Clear')],
                            HRESULT,
                            'Clear',
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAt')],
                            HRESULT,
                            'RemoveAt',
                            (['in'], DWORD, 'dwIndex'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceKeyCollection_INTERFACE_DEFINED__

            if not defined(__IPortableDevicePropVariantCollection_INTERFACE_DEFINED__):
                # interface IPortableDevicePropVariantCollection
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDevicePropVariantCollection = MIDL_INTERFACE(
                        "{89B2E422-4F1B-4316-BCEF-A44AFEA83EB3}"
                    )
                    IPortableDevicePropVariantCollection._iid_ = IID_IPortableDevicePropVariantCollection

                    IPortableDevicePropVariantCollection._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCount')],
                            HRESULT,
                            'GetCount',
                            (['in'], POINTER(DWORD), 'pcElems'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAt')],
                            HRESULT,
                            'GetAt',
                            (['in'], DWORD, 'dwIndex'),
                            (['in'], POINTER(PROPVARIANT), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Add')],
                            HRESULT,
                            'Add',
                            (['in'], POINTER(PROPVARIANT), 'pValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetType')],
                            HRESULT,
                            'GetType',
                            (['out'], POINTER(VARTYPE), 'pvt'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ChangeType')],
                            HRESULT,
                            'ChangeType',
                            (['in'], VARTYPE, 'vt'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Clear')],
                            HRESULT,
                            'Clear',
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAt')],
                            HRESULT,
                            'RemoveAt',
                            (['in'], DWORD, 'dwIndex'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDevicePropVariantCollection_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceValuesCollection_INTERFACE_DEFINED__):
                # interface IPortableDeviceValuesCollection
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceValuesCollection = MIDL_INTERFACE(
                        "{6E3F2D79-4E07-48C4-8208-D8C2E5AF4A99}"
                    )
                    IPortableDeviceValuesCollection._iid_ = IID_IPortableDeviceValuesCollection

                    IPortableDeviceValuesCollection._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCount')],
                            HRESULT,
                            'GetCount',
                            (['in'], POINTER(DWORD), 'pcElems'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAt')],
                            HRESULT,
                            'GetAt',
                            (['in'], DWORD, 'dwIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppValues'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Add')],
                            HRESULT,
                            'Add',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pValues'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Clear')],
                            HRESULT,
                            'Clear',
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAt')],
                            HRESULT,
                            'RemoveAt',
                            (['in'], DWORD, 'dwIndex'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceValuesCollection_INTERFACE_DEFINED__

            # interface __MIDL_itf_PortableDeviceTypes_0000_0005
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if not defined(__PortableDeviceTypesLib_LIBRARY_DEFINED__):
            # library PortableDeviceTypesLib
            # [helpstring][version][uuid]

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                pass
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
                pass
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

            if defined(__cplusplus):
                pass
            # END IF

            if defined(__cplusplus):
                pass
            # END IF

            if defined(__cplusplus):
                pass
            # END IF

            if defined(__cplusplus):
                pass
            # END IF

            if defined(__cplusplus):
                pass
            # END IF

        # END IF  __PortableDeviceTypesLib_LIBRARY_DEFINED__

        # interface __MIDL_itf_PortableDeviceTypes_0000_0006
        # [local]
    # END IF   (_WIN32_WINNT >= 0x0501)
    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG              BSTR_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG

    # UCHAR *  BSTR_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  BSTR_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       BSTR_UserFree(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID

    # ULONG              LPSAFEARRAY_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize = oleaut32.LPSAFEARRAY_UserSize
    LPSAFEARRAY_UserSize.restype = ULONG

    # UCHAR *  LPSAFEARRAY_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal = oleaut32.LPSAFEARRAY_UserMarshal
    LPSAFEARRAY_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  LPSAFEARRAY_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal = oleaut32.LPSAFEARRAY_UserUnmarshal
    LPSAFEARRAY_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       LPSAFEARRAY_UserFree(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree = oleaut32.LPSAFEARRAY_UserFree
    LPSAFEARRAY_UserFree.restype = VOID

    # ULONG              BSTR_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG

    # UCHAR *  BSTR_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  BSTR_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       BSTR_UserFree64(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID

    # ULONG              LPSAFEARRAY_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize64 = oleaut32.LPSAFEARRAY_UserSize64
    LPSAFEARRAY_UserSize64.restype = ULONG

    # UCHAR *  LPSAFEARRAY_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal64 = oleaut32.LPSAFEARRAY_UserMarshal64
    LPSAFEARRAY_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  LPSAFEARRAY_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal64 = oleaut32.LPSAFEARRAY_UserUnmarshal64
    LPSAFEARRAY_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       LPSAFEARRAY_UserFree64(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree64 = oleaut32.LPSAFEARRAY_UserFree64
    LPSAFEARRAY_UserFree64.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


