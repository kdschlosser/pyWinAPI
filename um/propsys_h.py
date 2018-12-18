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
__propsys_h__ = None
__IInitializeWithFile_FWD_DEFINED__ = None
__IInitializeWithStream_FWD_DEFINED__ = None
__IPropertyStore_FWD_DEFINED__ = None
__INamedPropertyStore_FWD_DEFINED__ = None
__IObjectWithPropertyKey_FWD_DEFINED__ = None
__IPropertyChange_FWD_DEFINED__ = None
__IPropertyChangeArray_FWD_DEFINED__ = None
__IPropertyStoreCapabilities_FWD_DEFINED__ = None
__IPropertyStoreCache_FWD_DEFINED__ = None
__IPropertyEnumType_FWD_DEFINED__ = None
__IPropertyEnumType2_FWD_DEFINED__ = None
__IPropertyEnumTypeList_FWD_DEFINED__ = None
__IPropertyDescription_FWD_DEFINED__ = None
__IPropertyDescription2_FWD_DEFINED__ = None
__IPropertyDescriptionAliasInfo_FWD_DEFINED__ = None
__IPropertyDescriptionSearchInfo_FWD_DEFINED__ = None
__IPropertyDescriptionRelatedPropertyInfo_FWD_DEFINED__ = None
__IPropertySystem_FWD_DEFINED__ = None
__IPropertyDescriptionList_FWD_DEFINED__ = None
__IPropertyStoreFactory_FWD_DEFINED__ = None
__IDelayedPropertyStoreFactory_FWD_DEFINED__ = None
__IPersistSerializedPropStorage_FWD_DEFINED__ = None
__IPersistSerializedPropStorage2_FWD_DEFINED__ = None
__IPropertySystemChangeNotify_FWD_DEFINED__ = None
__ICreateObject_FWD_DEFINED__ = None
__InMemoryPropertyStore_FWD_DEFINED__ = None
__InMemoryPropertyStoreMarshalByValue_FWD_DEFINED__ = None
__PropertySystem_FWD_DEFINED__ = None
_PROPSYS_ = None
PSSTDAPI = None
_MSC_EXTENSIONS = None
__IInitializeWithFile_INTERFACE_DEFINED__ = None
__IInitializeWithStream_INTERFACE_DEFINED__ = None
__IPropertyStore_INTERFACE_DEFINED__ = None
__INamedPropertyStore_INTERFACE_DEFINED__ = None
__IObjectWithPropertyKey_INTERFACE_DEFINED__ = None
__IPropertyChange_INTERFACE_DEFINED__ = None
__IPropertyChangeArray_INTERFACE_DEFINED__ = None
__IPropertyStoreCapabilities_INTERFACE_DEFINED__ = None
__IPropertyStoreCache_INTERFACE_DEFINED__ = None
__IPropertyEnumType_INTERFACE_DEFINED__ = None
__IPropertyEnumType2_INTERFACE_DEFINED__ = None
__IPropertyEnumTypeList_INTERFACE_DEFINED__ = None
__IPropertyDescription_INTERFACE_DEFINED__ = None
__IPropertyDescription2_INTERFACE_DEFINED__ = None
__IPropertyDescriptionAliasInfo_INTERFACE_DEFINED__ = None
__IPropertyDescriptionSearchInfo_INTERFACE_DEFINED__ = None
__IPropertyDescriptionRelatedPropertyInfo_INTERFACE_DEFINED__ = None
__IPropertySystem_INTERFACE_DEFINED__ = None
__IPropertyDescriptionList_INTERFACE_DEFINED__ = None
__IPropertyStoreFactory_INTERFACE_DEFINED__ = None
__IDelayedPropertyStoreFactory_INTERFACE_DEFINED__ = None
__IPersistSerializedPropStorage_INTERFACE_DEFINED__ = None
__IPersistSerializedPropStorage2_INTERFACE_DEFINED__ = None
__IPropertySystemChangeNotify_INTERFACE_DEFINED__ = None
__ICreateObject_INTERFACE_DEFINED__ = None
__PropSysObjects_LIBRARY_DEFINED__ = None


class tagSERIALIZEDPROPSTORAGE(ctypes.Structure):
    pass


SERIALIZEDPROPSTORAGE = tagSERIALIZEDPROPSTORAGE



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


if not defined(__propsys_h__):

    propsys = ctypes.windll.PROPSYS

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    LIBID_PropSysObjects = IID(
        '{2cda3294-6c4f-4020-b161-27c530c81fa6}'
    )


    class PropSysObjects(object):
        name = 'PropSysObjects'
        _reg_typelib_ = (LIBID_PropSysObjects, 1, 0)


    # Forward Declarations
    if not defined(__IInitializeWithFile_FWD_DEFINED__):
        class IInitializeWithFile(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IInitializeWithFile_FWD_DEFINED__

    if not defined(__IInitializeWithStream_FWD_DEFINED__):
        class IInitializeWithStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IInitializeWithStream_FWD_DEFINED__

    if not defined(__IPropertyStore_FWD_DEFINED__):
        class IPropertyStore(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyStore_FWD_DEFINED__

    if not defined(__INamedPropertyStore_FWD_DEFINED__):
        class INamedPropertyStore(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __INamedPropertyStore_FWD_DEFINED__

    if not defined(__IObjectWithPropertyKey_FWD_DEFINED__):
        class IObjectWithPropertyKey(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IObjectWithPropertyKey_FWD_DEFINED__

    if not defined(__IPropertyChange_FWD_DEFINED__):
        class IPropertyChange(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyChange_FWD_DEFINED__

    if not defined(__IPropertyChangeArray_FWD_DEFINED__):
        class IPropertyChangeArray(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyChangeArray_FWD_DEFINED__

    if not defined(__IPropertyStoreCapabilities_FWD_DEFINED__):
        class IPropertyStoreCapabilities(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyStoreCapabilities_FWD_DEFINED__

    if not defined(__IPropertyStoreCache_FWD_DEFINED__):
        class IPropertyStoreCache(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyStoreCache_FWD_DEFINED__

    if not defined(__IPropertyEnumType_FWD_DEFINED__):
        class IPropertyEnumType(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyEnumType_FWD_DEFINED__

    if not defined(__IPropertyEnumType2_FWD_DEFINED__):
        class IPropertyEnumType2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyEnumType2_FWD_DEFINED__

    if not defined(__IPropertyEnumTypeList_FWD_DEFINED__):
        class IPropertyEnumTypeList(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyEnumTypeList_FWD_DEFINED__

    if not defined(__IPropertyDescription_FWD_DEFINED__):
        class IPropertyDescription(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyDescription_FWD_DEFINED__

    if not defined(__IPropertyDescription2_FWD_DEFINED__):
        class IPropertyDescription2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyDescription2_FWD_DEFINED__

    if not defined(__IPropertyDescriptionAliasInfo_FWD_DEFINED__):
        class IPropertyDescriptionAliasInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyDescriptionAliasInfo_FWD_DEFINED__

    if not defined(__IPropertyDescriptionSearchInfo_FWD_DEFINED__):
        class IPropertyDescriptionSearchInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyDescriptionSearchInfo_FWD_DEFINED__

    if not defined(__IPropertyDescriptionRelatedPropertyInfo_FWD_DEFINED__):
        class IPropertyDescriptionRelatedPropertyInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyDescriptionRelatedPropertyInfo_FWD_DEFINED__

    if not defined(__IPropertySystem_FWD_DEFINED__):
        class IPropertySystem(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertySystem_FWD_DEFINED__

    if not defined(__IPropertyDescriptionList_FWD_DEFINED__):
        class IPropertyDescriptionList(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyDescriptionList_FWD_DEFINED__

    if not defined(__IPropertyStoreFactory_FWD_DEFINED__):
        class IPropertyStoreFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyStoreFactory_FWD_DEFINED__

    if not defined(__IDelayedPropertyStoreFactory_FWD_DEFINED__):
        class IDelayedPropertyStoreFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDelayedPropertyStoreFactory_FWD_DEFINED__

    if not defined(__IPersistSerializedPropStorage_FWD_DEFINED__):
        class IPersistSerializedPropStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistSerializedPropStorage_FWD_DEFINED__

    if not defined(__IPersistSerializedPropStorage2_FWD_DEFINED__):
        class IPersistSerializedPropStorage2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistSerializedPropStorage2_FWD_DEFINED__

    if not defined(__IPropertySystemChangeNotify_FWD_DEFINED__):
        class IPropertySystemChangeNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertySystemChangeNotify_FWD_DEFINED__

    if not defined(__ICreateObject_FWD_DEFINED__):
        class ICreateObject(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICreateObject_FWD_DEFINED__

    if not defined(__InMemoryPropertyStore_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_InMemoryPropertyStore = CLSID(
                '{9a02e012-6303-4e1e-b9a1-630f802592c5}'
            )

            class InMemoryPropertyStore(comtypes.CoClass):
                _reg_clsid_ = CLSID_InMemoryPropertyStore
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PropSysObjects, 1, 0)
                _com_interfaces_ = [IPropertyStore]
        # END IF  __cplusplus
    # END IF  __InMemoryPropertyStore_FWD_DEFINED__

    if not defined(__InMemoryPropertyStoreMarshalByValue_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_InMemoryPropertyStoreMarshalByValue = CLSID(
                '{D4CA0E2D-6DA7-4b75-A97C-5F306F0EAEDC}'
            )


            class InMemoryPropertyStoreMarshalByValue(comtypes.CoClass):
                _reg_clsid_ = CLSID_InMemoryPropertyStoreMarshalByValue
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PropSysObjects, 1, 0)
                _com_interfaces_ = [IPropertyStore]

        # END IF  __cplusplus
    # END IF  __InMemoryPropertyStoreMarshalByValue_FWD_DEFINED__

    if not defined(__PropertySystem_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PropertySystem = CLSID(
                '{b8967f85-58ae-4f46-9fb2-5d7904798f4b}'
            )


            class PropertySystem(comtypes.CoClass):
                _reg_clsid_ = CLSID_PropertySystem
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PropSysObjects, 1, 0)
                _com_interfaces_ = [IPropertyStore]

        # END IF  __cplusplus
    # END IF  __PropertySystem_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.objidl_h import * # NOQA
    from pyWinAPI.um.oleidl_h import * # NOQA
    from pyWinAPI.um.ocidl_h import * # NOQA
    from pyWinAPI.um.shtypes_h import * # NOQA
    from pyWinAPI.um.structuredquerycondition_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    # interface __MIDL_itf_propsys_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if not defined(PSSTDAPI):
        if defined(_PROPSYS_):
            pass
        else:
            pass
        # END IF
    # END IF   PSSTDAPI

    __ZERO__ = 0

    if __ZERO__:
        REFPROPERTYKEY = POINTER(PROPERTYKEY)
    # END IF   0

    from pyWinAPI.shared.propkeydef_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if _MSC_VER >= 1200:
            if not defined(_MSC_EXTENSIONS):
                pass
            # END IF
        # END IF

        if not defined(__IInitializeWithFile_INTERFACE_DEFINED__):
            # interface IInitializeWithFile
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IInitializeWithFile = MIDL_INTERFACE(
                    "{B7D14566-0509-4CCE-A71F-0A554233BD9B}"
                )
                IInitializeWithFile._iid_ = IID_IInitializeWithFile

                IInitializeWithFile._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Initialize')],
                        HRESULT,
                        'Initialize',
                        (['in'], LPCWSTR, 'pszFilePath'),
                        (['in'], DWORD, 'grfMode'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IInitializeWithFile_INTERFACE_DEFINED__

        if not defined(__IInitializeWithStream_INTERFACE_DEFINED__):
            # interface IInitializeWithStream
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IInitializeWithStream = MIDL_INTERFACE(
                    "{B824B49D-22AC-4161-AC8A-9916E8FA3F7F}"
                )
                IInitializeWithStream._iid_ = IID_IInitializeWithStream

                IInitializeWithStream._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Initialize'), 'local'],
                        HRESULT,
                        'Initialize',
                        (['in'], POINTER(IStream), 'pstream'),
                        (['in'], DWORD, 'grfMode'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IInitializeWithStream_INTERFACE_DEFINED__
        # interface __MIDL_itf_propsys_0000_0002
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IPropertyStore_INTERFACE_DEFINED__):
            # interface IPropertyStore
            # [unique][object][helpstring][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyStore = MIDL_INTERFACE(
                    "{886D8EEB-8CF2-4446-8D02-CDBA1DBDCF99}"
                )
                IPropertyStore._iid_ = IID_IPropertyStore

                IPropertyStore._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(DWORD), 'cProps'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAt')],
                        HRESULT,
                        'GetAt',
                        (['in'], DWORD, 'iProp'),
                        (['out'], POINTER(PROPERTYKEY), 'pkey'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetValue')],
                        HRESULT,
                        'GetValue',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(PROPVARIANT), 'pv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetValue')],
                        HRESULT,
                        'SetValue',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['in'], REFPROPVARIANT, 'propvar'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Commit')],
                        HRESULT,
                        'Commit',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyStore_INTERFACE_DEFINED__

        # interface __MIDL_itf_propsys_0000_0003
        # [local]
        # [unique]
        LPPROPERTYSTORE = POINTER(IPropertyStore)

        # PSSTDAPI PropVariantToWinRTPropertyValue(_In_ REFPROPVARIANT propvar, _In_ REFIID riid, _COM_Outptr_result_maybenull_ VOID **ppv);
        PropVariantToWinRTPropertyValue = (
            propsys.PropVariantToWinRTPropertyValue
        )
        PropVariantToWinRTPropertyValue.restype = PSSTDAPI

        # PSSTDAPI WinRTPropertyValueToPropVariant(_In_opt_ IUnknown *punkPropertyValue, _Out_ PROPVARIANT *ppropvar);
        WinRTPropertyValueToPropVariant = (
            propsys.WinRTPropertyValueToPropVariant
        )
        WinRTPropertyValueToPropVariant.restype = PSSTDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__INamedPropertyStore_INTERFACE_DEFINED__):
            # interface INamedPropertyStore
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_INamedPropertyStore = MIDL_INTERFACE(
                    "{71604B0F-97B0-4764-8577-2F13E98A1422}"
                )
                INamedPropertyStore._iid_ = IID_INamedPropertyStore

                INamedPropertyStore._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetNamedValue')],
                        HRESULT,
                        'GetNamedValue',
                        (['in'], LPCWSTR, 'pszName'),
                        (['out'], POINTER(PROPVARIANT), 'ppropvar'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetNamedValue')],
                        HRESULT,
                        'SetNamedValue',
                        (['in'], LPCWSTR, 'pszName'),
                        (['in'], REFPROPVARIANT, 'propvar'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNameCount')],
                        HRESULT,
                        'GetNameCount',
                        (['out'], POINTER(DWORD), 'pdwCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNameAt')],
                        HRESULT,
                        'GetNameAt',
                        (['in'], DWORD, 'iProp'),
                        (['out'], POINTER(BSTR), 'pbstrName'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __INamedPropertyStore_INTERFACE_DEFINED__

        # interface __MIDL_itf_propsys_0000_0004
        # [local]
        class GETPROPERTYSTOREFLAGS(ENUM):
            GPS_DEFAULT = 0
            GPS_HANDLERPROPERTIESONLY = 0x1
            GPS_READWRITE = 0x2
            GPS_TEMPORARY = 0x4
            GPS_FASTPROPERTIESONLY = 0x8
            GPS_OPENSLOWITEM = 0x10
            GPS_DELAYCREATION = 0x20
            GPS_BESTEFFORT = 0x40
            GPS_NO_OPLOCK = 0x80
            GPS_PREFERQUERYPROPERTIES = 0x100
            GPS_EXTRINSICPROPERTIES = 0x200
            GPS_EXTRINSICPROPERTIESONLY = 0x400
            GPS_VOLATILEPROPERTIES = 0x800
            GPS_VOLATILEPROPERTIESONLY = 0x1000
            GPS_MASK_VALID = 0x1FFF

        if not defined(__IObjectWithPropertyKey_INTERFACE_DEFINED__):
            # interface IObjectWithPropertyKey
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IObjectWithPropertyKey = MIDL_INTERFACE(
                    "{FC0CA0A7-C316-4FD2-9031-3E628E6D4F23}"
                )
                IObjectWithPropertyKey._iid_ = IID_IObjectWithPropertyKey

                IObjectWithPropertyKey._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetPropertyKey')],
                        HRESULT,
                        'SetPropertyKey',
                        (['in'], REFPROPERTYKEY, 'key'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyKey')],
                        HRESULT,
                        'GetPropertyKey',
                        (['out'], POINTER(PROPERTYKEY), 'pkey'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IObjectWithPropertyKey_INTERFACE_DEFINED__

        # interface __MIDL_itf_propsys_0000_0005
        # [local]
        class PKA_FLAGS(ENUM):
            PKA_SET = 0
            PKA_APPEND = PKA_SET + 1
            PKA_DELETE = PKA_APPEND + 1
        if not defined(__IPropertyChange_INTERFACE_DEFINED__):
            # interface IPropertyChange
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyChange = MIDL_INTERFACE(
                    "{F917BC8A-1BBA-4478-A245-1BDE03EB9431}"
                )
                IPropertyChange._iid_ = IID_IPropertyChange

                IPropertyChange._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ApplyToPropVariant')],
                        HRESULT,
                        'ApplyToPropVariant',
                        (['in'], REFPROPVARIANT, 'propvarIn'),
                        (['out'], POINTER(PROPVARIANT), 'ppropvarOut'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyChange_INTERFACE_DEFINED__

        if not defined(__IPropertyChangeArray_INTERFACE_DEFINED__):
            # interface IPropertyChangeArray
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyChangeArray = MIDL_INTERFACE(
                    "{380F5CAD-1B5E-42F2-805D-637FD392D31E}"
                )
                IPropertyChangeArray._iid_ = IID_IPropertyChangeArray

                IPropertyChangeArray._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(UINT), 'pcOperations'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAt')],
                        HRESULT,
                        'GetAt',
                        (['in'], UINT, 'iIndex'),
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method InsertAt')],
                        HRESULT,
                        'InsertAt',
                        (['in'], UINT, 'iIndex'),
                        (['in'], POINTER(IPropertyChange), 'ppropChange'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Append')],
                        HRESULT,
                        'Append',
                        (['in'], POINTER(IPropertyChange), 'ppropChange'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AppendOrReplace')],
                        HRESULT,
                        'AppendOrReplace',
                        (['in'], POINTER(IPropertyChange), 'ppropChange'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveAt')],
                        HRESULT,
                        'RemoveAt',
                        (['in'], UINT, 'iIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsKeyInArray')],
                        HRESULT,
                        'IsKeyInArray',
                        (['in'], REFPROPERTYKEY, 'key'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyChangeArray_INTERFACE_DEFINED__

        if not defined(__IPropertyStoreCapabilities_INTERFACE_DEFINED__):
            # interface IPropertyStoreCapabilities
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyStoreCapabilities = MIDL_INTERFACE(
                    "{C8E2D566-186E-4D49-BF41-6909EAD56ACC}"
                )
                IPropertyStoreCapabilities._iid_ = IID_IPropertyStoreCapabilities

                IPropertyStoreCapabilities._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsPropertyWritable')],
                        HRESULT,
                        'IsPropertyWritable',
                        (['in'], REFPROPERTYKEY, 'key'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyStoreCapabilities_INTERFACE_DEFINED__

        if not defined(__IPropertyStoreCache_INTERFACE_DEFINED__):
            # interface IPropertyStoreCache
            # [unique][object][uuid]
            class PSC_STATE(ENUM):
                PSC_NORMAL = 0
                PSC_NOTINSOURCE = 1
                PSC_DIRTY = 2
                PSC_READONLY = 3

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyStoreCache = MIDL_INTERFACE(
                    "{3017056D-9A91-4E90-937D-746C72ABBF4F}"
                )
                IPropertyStoreCache._iid_ = IID_IPropertyStoreCache

                IPropertyStoreCache._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetState')],
                        HRESULT,
                        'GetState',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(PSC_STATE), 'pstate'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetValueAndState')],
                        HRESULT,
                        'GetValueAndState',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(PROPVARIANT), 'ppropvar'),
                        (['out'], POINTER(PSC_STATE), 'pstate'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetState')],
                        HRESULT,
                        'SetState',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['in'], PSC_STATE, 'state'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetValueAndState')],
                        HRESULT,
                        'SetValueAndState',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['unique', 'in'], POINTER(PROPVARIANT), 'ppropvar'),
                        (['in'], PSC_STATE, 'state'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyStoreCache_INTERFACE_DEFINED__

        if not defined(__IPropertyEnumType_INTERFACE_DEFINED__):
            # interface IPropertyEnumType
            # [unique][object][uuid]
            class PROPENUMTYPE(ENUM):
                PET_DISCRETEVALUE = 0
                PET_RANGEDVALUE = 1
                PET_DEFAULTVALUE = 2
                PET_ENDRANGE = 3

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyEnumType = MIDL_INTERFACE(
                    "{11E1FBF9-2D56-4A6B-8DB3-7CD193A471F2}"
                )
                IPropertyEnumType._iid_ = IID_IPropertyEnumType

                IPropertyEnumType._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetEnumType')],
                        HRESULT,
                        'GetEnumType',
                        (['out'], POINTER(PROPENUMTYPE), 'penumtype'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetValue')],
                        HRESULT,
                        'GetValue',
                        (['out'], POINTER(PROPVARIANT), 'ppropvar'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRangeMinValue')],
                        HRESULT,
                        'GetRangeMinValue',
                        (['out'], POINTER(PROPVARIANT), 'ppropvarMin'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRangeSetValue')],
                        HRESULT,
                        'GetRangeSetValue',
                        (['out'], POINTER(PROPVARIANT), 'ppropvarSet'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDisplayText')],
                        HRESULT,
                        'GetDisplayText',
                        (['out'], POINTER(LPWSTR), 'ppszDisplay'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyEnumType_INTERFACE_DEFINED__

        if not defined(__IPropertyEnumType2_INTERFACE_DEFINED__):
            # interface IPropertyEnumType2
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyEnumType2 = MIDL_INTERFACE(
                    "{9B6E051C-5DDD-4321-9070-FE2ACB55E794}"
                )
                IPropertyEnumType2._iid_ = IID_IPropertyEnumType2

                IPropertyEnumType2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetImageReference')],
                        HRESULT,
                        'GetImageReference',
                        (['out'], POINTER(LPWSTR), 'ppszImageRes'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyEnumType2_INTERFACE_DEFINED__

        if not defined(__IPropertyEnumTypeList_INTERFACE_DEFINED__):
            # interface IPropertyEnumTypeList
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyEnumTypeList = MIDL_INTERFACE(
                    "{A99400F4-3D84-4557-94BA-1242FB2CC9A6}"
                )
                IPropertyEnumTypeList._iid_ = IID_IPropertyEnumTypeList

                IPropertyEnumTypeList._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(UINT), 'pctypes'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAt')],
                        HRESULT,
                        'GetAt',
                        (['in'], UINT, 'itype'),
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetConditionAt')],
                        HRESULT,
                        'GetConditionAt',
                        (['in'], UINT, 'nIndex'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FindMatchingIndex')],
                        HRESULT,
                        'FindMatchingIndex',
                        (['in'], REFPROPVARIANT, 'propvarCmp'),
                        (['out'], POINTER(UINT), 'pnIndex'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyEnumTypeList_INTERFACE_DEFINED__

        if not defined(__IPropertyDescription_INTERFACE_DEFINED__):
            # interface IPropertyDescription
            # [unique][object][uuid]
            class PROPDESC_TYPE_FLAGS(ENUM):
                PDTF_DEFAULT = 0
                PDTF_MULTIPLEVALUES = 0x1
                PDTF_ISINNATE = 0x2
                PDTF_ISGROUP = 0x4
                PDTF_CANGROUPBY = 0x8
                PDTF_CANSTACKBY = 0x10
                PDTF_ISTREEPROPERTY = 0x20
                PDTF_INCLUDEINFULLTEXTQUERY = 0x40
                PDTF_ISVIEWABLE = 0x80
                PDTF_ISQUERYABLE = 0x100
                PDTF_CANBEPURGED = 0x200
                PDTF_SEARCHRAWVALUE = 0x400
                PDTF_DONTCOERCEEMPTYSTRINGS = 0x800
                PDTF_ALWAYSINSUPPLEMENTALSTORE = 0x1000
                PDTF_ISSYSTEMPROPERTY = 0x80000000
                PDTF_MASK_ALL = 0x80001FFF


            class PROPDESC_VIEW_FLAGS(ENUM):
                PDVF_DEFAULT = 0
                PDVF_CENTERALIGN = 0x1
                PDVF_RIGHTALIGN = 0x2
                PDVF_BEGINNEWGROUP = 0x4
                PDVF_FILLAREA = 0x8
                PDVF_SORTDESCENDING = 0x10
                PDVF_SHOWONLYIFPRESENT = 0x20
                PDVF_SHOWBYDEFAULT = 0x40
                PDVF_SHOWINPRIMARYLIST = 0x80
                PDVF_SHOWINSECONDARYLIST = 0x100
                PDVF_HIDELABEL = 0x200
                PDVF_HIDDEN = 0x800
                PDVF_CANWRAP = 0x1000
                PDVF_MASK_ALL = 0x1BFF


            class PROPDESC_DISPLAYTYPE(ENUM):
                PDDT_STRING = 0
                PDDT_NUMBER = 1
                PDDT_BOOLEAN = 2
                PDDT_DATETIME = 3
                PDDT_ENUMERATED = 4


            class PROPDESC_GROUPING_RANGE(ENUM):
                PDGR_DISCRETE = 0
                PDGR_ALPHANUMERIC = 1
                PDGR_SIZE = 2
                PDGR_DYNAMIC = 3
                PDGR_DATE = 4
                PDGR_PERCENT = 5
                PDGR_ENUMERATED = 6


            class PROPDESC_FORMAT_FLAGS(ENUM):
                PDFF_DEFAULT = 0
                PDFF_PREFIXNAME = 0x1
                PDFF_FILENAME = 0x2
                PDFF_ALWAYSKB = 0x4
                PDFF_RESERVED_RIGHTTOLEFT = 0x8
                PDFF_SHORTTIME = 0x10
                PDFF_LONGTIME = 0x20
                PDFF_HIDETIME = 0x40
                PDFF_SHORTDATE = 0x80
                PDFF_LONGDATE = 0x100
                PDFF_HIDEDATE = 0x200
                PDFF_RELATIVEDATE = 0x400
                PDFF_USEEDITINVITATION = 0x800
                PDFF_READONLY = 0x1000
                PDFF_NOAUTOREADINGORDER = 0x2000


            class PROPDESC_SORTDESCRIPTION(ENUM):
                PDSD_GENERAL = 0
                PDSD_A_Z = 1
                PDSD_LOWEST_HIGHEST = 2
                PDSD_SMALLEST_BIGGEST = 3
                PDSD_OLDEST_NEWEST = 4


            class PROPDESC_RELATIVEDESCRIPTION_TYPE(ENUM):
                PDRDT_GENERAL = 0
                PDRDT_DATE = 1
                PDRDT_SIZE = 2
                PDRDT_COUNT = 3
                PDRDT_REVISION = 4
                PDRDT_LENGTH = 5
                PDRDT_DURATION = 6
                PDRDT_SPEED = 7
                PDRDT_RATE = 8
                PDRDT_RATING = 9
                PDRDT_PRIORITY = 10


            class PROPDESC_AGGREGATION_TYPE(ENUM):
                PDAT_DEFAULT = 0
                PDAT_FIRST = 1
                PDAT_SUM = 2
                PDAT_AVERAGE = 3
                PDAT_DATERANGE = 4
                PDAT_UNION = 5
                PDAT_MAX = 6
                PDAT_MIN = 7


            class PROPDESC_CONDITION_TYPE(ENUM):
                PDCOT_NONE = 0
                PDCOT_STRING = 1
                PDCOT_SIZE = 2
                PDCOT_DATETIME = 3
                PDCOT_BOOLEAN = 4
                PDCOT_NUMBER = 5

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyDescription = MIDL_INTERFACE(
                    "{6F79D558-3E96-4549-A1D1-7D75D2288814}"
                )
                IPropertyDescription._iid_ = IID_IPropertyDescription

                IPropertyDescription._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetPropertyKey')],
                        HRESULT,
                        'GetPropertyKey',
                        (['out'], POINTER(PROPERTYKEY), 'pkey'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCanonicalName')],
                        HRESULT,
                        'GetCanonicalName',
                        (['out', 'in'], POINTER(LPWSTR), 'ppszName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyType')],
                        HRESULT,
                        'GetPropertyType',
                        (['out'], POINTER(VARTYPE), 'pvartype'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDisplayName')],
                        HRESULT,
                        'GetDisplayName',
                        (['out', 'in'], POINTER(LPWSTR), 'ppszName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetEditInvitation')],
                        HRESULT,
                        'GetEditInvitation',
                        (['out', 'in'], POINTER(LPWSTR), 'ppszInvite'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeFlags')],
                        HRESULT,
                        'GetTypeFlags',
                        (['in'], PROPDESC_TYPE_FLAGS, 'mask'),
                        (['out'], POINTER(PROPDESC_TYPE_FLAGS), 'ppdtFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetViewFlags')],
                        HRESULT,
                        'GetViewFlags',
                        (['out'], POINTER(PROPDESC_VIEW_FLAGS), 'ppdvFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDefaultColumnWidth')],
                        HRESULT,
                        'GetDefaultColumnWidth',
                        (['out'], POINTER(UINT), 'pcxChars'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDisplayType')],
                        HRESULT,
                        'GetDisplayType',
                        (
                            ['out'],
                            POINTER(PROPDESC_DISPLAYTYPE),
                           'pdisplaytype'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetColumnState')],
                        HRESULT,
                        'GetColumnState',
                        (['out'], POINTER(SHCOLSTATEF), 'pcsFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetGroupingRange')],
                        HRESULT,
                        'GetGroupingRange',
                        (['out'], POINTER(PROPDESC_GROUPING_RANGE), 'pgr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRelativeDescriptionType')],
                        HRESULT,
                        'GetRelativeDescriptionType',
                        (
                            ['out'],
                            POINTER(PROPDESC_RELATIVEDESCRIPTION_TYPE),
                           'prdt'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRelativeDescription')],
                        HRESULT,
                        'GetRelativeDescription',
                        (['in'], REFPROPVARIANT, 'propvar1'),
                        (['in'], REFPROPVARIANT, 'propvar2'),
                        (['out', 'in'], POINTER(LPWSTR), 'ppszDesc1'),
                        (['out', 'in'], POINTER(LPWSTR), 'ppszDesc2'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSortDescription')],
                        HRESULT,
                        'GetSortDescription',
                        (['out'], POINTER(PROPDESC_SORTDESCRIPTION), 'psd'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSortDescriptionLabel')],
                        HRESULT,
                        'GetSortDescriptionLabel',
                        (['in'], BOOL, 'fDescending'),
                        (['out', 'in'], POINTER(LPWSTR), 'ppszDescription'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAggregationType')],
                        HRESULT,
                        'GetAggregationType',
                        (
                            ['out'],
                            POINTER(PROPDESC_AGGREGATION_TYPE),
                           'paggtype'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetConditionType')],
                        HRESULT,
                        'GetConditionType',
                        (
                            ['out'],
                            POINTER(PROPDESC_CONDITION_TYPE),
                           'pcontype'
                        ),
                        (['out'], POINTER(CONDITION_OPERATION), 'popDefault'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetEnumTypeList')],
                        HRESULT,
                        'GetEnumTypeList',
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CoerceToCanonicalValue'), 'local'],
                        HRESULT,
                        'CoerceToCanonicalValue',
                        (['out', 'in'], POINTER(PROPVARIANT), 'ppropvar'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FormatForDisplay')],
                        HRESULT,
                        'FormatForDisplay',
                        (['in'], REFPROPVARIANT, 'propvar'),
                        (['in'], PROPDESC_FORMAT_FLAGS, 'pdfFlags'),
                        (['out', 'in'], POINTER(LPWSTR), 'ppszDisplay'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsValueCanonical')],
                        HRESULT,
                        'IsValueCanonical',
                        (['in'], REFPROPVARIANT, 'propvar'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyDescription_INTERFACE_DEFINED__

        if not defined(__IPropertyDescription2_INTERFACE_DEFINED__):
            # interface IPropertyDescription2
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyDescription2 = MIDL_INTERFACE(
                    "{57D2EDED-5062-400E-B107-5DAE79FE57A6}"
                )
                IPropertyDescription2._iid_ = IID_IPropertyDescription2

                IPropertyDescription2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetImageReferenceForValue')],
                        HRESULT,
                        'GetImageReferenceForValue',
                        (['in'], REFPROPVARIANT, 'propvar'),
                        (['out', 'in'], POINTER(LPWSTR), 'ppszImageRes'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyDescription2_INTERFACE_DEFINED__

        if not defined(__IPropertyDescriptionAliasInfo_INTERFACE_DEFINED__):
            # interface IPropertyDescriptionAliasInfo
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyDescriptionAliasInfo = MIDL_INTERFACE(
                    "{F67104FC-2AF9-46FD-B32D-243C1404F3D1}"
                )
                IPropertyDescriptionAliasInfo._iid_ = IID_IPropertyDescriptionAliasInfo

                IPropertyDescriptionAliasInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSortByAlias')],
                        HRESULT,
                        'GetSortByAlias',
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAdditionalSortByAliases')],
                        HRESULT,
                        'GetAdditionalSortByAliases',
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyDescriptionAliasInfo_INTERFACE_DEFINED__

        if not defined(__IPropertyDescriptionSearchInfo_INTERFACE_DEFINED__):
            # interface IPropertyDescriptionSearchInfo
            # [unique][object][uuid]
            class PROPDESC_SEARCHINFO_FLAGS(ENUM):
                PDSIF_DEFAULT = 0
                PDSIF_ININVERTEDINDEX = 0x1
                PDSIF_ISCOLUMN = 0x2
                PDSIF_ISCOLUMNSPARSE = 0x4
                PDSIF_ALWAYSINCLUDE = 0x8
                PDSIF_USEFORTYPEAHEAD = 0x10


            class PROPDESC_COLUMNINDEX_TYPE(ENUM):
                PDCIT_NONE = 0
                PDCIT_ONDISK = 1
                PDCIT_INMEMORY = 2
                PDCIT_ONDEMAND = 3
                PDCIT_ONDISKALL = 4
                PDCIT_ONDISKVECTOR = 5

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyDescriptionSearchInfo = MIDL_INTERFACE(
                    "{078F91BD-29A2-440F-924E-46A291524520}"
                )
                IPropertyDescriptionSearchInfo._iid_ = IID_IPropertyDescriptionSearchInfo

                IPropertyDescriptionSearchInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSearchInfoFlags')],
                        HRESULT,
                        'GetSearchInfoFlags',
                        (
                            ['out'],
                            POINTER(PROPDESC_SEARCHINFO_FLAGS),
                           'ppdsiFlags'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetColumnIndexType')],
                        HRESULT,
                        'GetColumnIndexType',
                        (
                            ['out'],
                            POINTER(PROPDESC_COLUMNINDEX_TYPE),
                           'ppdciType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProjectionString')],
                        HRESULT,
                        'GetProjectionString',
                        (['out'], POINTER(LPWSTR), 'ppszProjection'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMaxSize')],
                        HRESULT,
                        'GetMaxSize',
                        (['out'], POINTER(UINT), 'pcbMaxSize'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyDescriptionSearchInfo_INTERFACE_DEFINED__

        if not defined(__IPropertyDescriptionRelatedPropertyInfo_INTERFACE_DEFINED__):
            # interface IPropertyDescriptionRelatedPropertyInfo
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyDescriptionRelatedPropertyInfo = MIDL_INTERFACE(
                    "{507393F4-2A3D-4A60-B59E-D9C75716C2DD}"
                )
                IPropertyDescriptionRelatedPropertyInfo._iid_ = IID_IPropertyDescriptionRelatedPropertyInfo

                IPropertyDescriptionRelatedPropertyInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetRelatedProperty')],
                        HRESULT,
                        'GetRelatedProperty',
                        (['in'], LPCWSTR, 'pszRelationshipName'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyDescriptionRelatedPropertyInfo_INTERFACE_DEFINED__

        # interface __MIDL_itf_propsys_0000_0017
        # [local]
        class PROPDESC_ENUMFILTER(ENUM):
            PDEF_ALL = 0
            PDEF_SYSTEM = 1
            PDEF_NONSYSTEM = 2
            PDEF_VIEWABLE = 3
            PDEF_QUERYABLE = 4
            PDEF_INFULLTEXTQUERY = 5
            PDEF_COLUMN = 6

        if not defined(__IPropertySystem_INTERFACE_DEFINED__):
            # interface IPropertySystem
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertySystem = MIDL_INTERFACE(
                    "{CA724E8A-C3E6-442B-88A4-6FB0DB8035A3}"
                )
                IPropertySystem._iid_ = IID_IPropertySystem

                IPropertySystem._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetPropertyDescription')],
                        HRESULT,
                        'GetPropertyDescription',
                        (['in'], REFPROPERTYKEY, 'propkey'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyDescriptionByName')],
                        HRESULT,
                        'GetPropertyDescriptionByName',
                        (['in'], LPCWSTR, 'pszCanonicalName'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyDescriptionListFromString')],
                        HRESULT,
                        'GetPropertyDescriptionListFromString',
                        (['in'], LPCWSTR, 'pszPropList'),
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumeratePropertyDescriptions')],
                        HRESULT,
                        'EnumeratePropertyDescriptions',
                        (['in'], PROPDESC_ENUMFILTER, 'filterOn'),
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FormatForDisplay')],
                        HRESULT,
                        'FormatForDisplay',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['in'], REFPROPVARIANT, 'propvar'),
                        (['in'], PROPDESC_FORMAT_FLAGS, 'pdff'),
                        (['out', 'in'], LPWSTR, 'pszText'),
                        (['range', 'in'], DWORD, 'cchText'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FormatForDisplayAlloc')],
                        HRESULT,
                        'FormatForDisplayAlloc',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['in'], REFPROPVARIANT, 'propvar'),
                        (['in'], PROPDESC_FORMAT_FLAGS, 'pdff'),
                        (['out', 'in'], POINTER(LPWSTR), 'ppszDisplay'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RegisterPropertySchema')],
                        HRESULT,
                        'RegisterPropertySchema',
                        (['in'], LPCWSTR, 'pszPath'),
                    ),
                    COMMETHOD(
                        [helpstring('Method UnregisterPropertySchema')],
                        HRESULT,
                        'UnregisterPropertySchema',
                        (['in'], LPCWSTR, 'pszPath'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RefreshPropertySchema')],
                        HRESULT,
                        'RefreshPropertySchema',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertySystem_INTERFACE_DEFINED__

        if not defined(__IPropertyDescriptionList_INTERFACE_DEFINED__):
            # interface IPropertyDescriptionList
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyDescriptionList = MIDL_INTERFACE(
                    "{1F9FC1D0-C39B-4B26-817F-011967D3440E}"
                )
                IPropertyDescriptionList._iid_ = IID_IPropertyDescriptionList

                IPropertyDescriptionList._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(UINT), 'pcElem'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAt')],
                        HRESULT,
                        'GetAt',
                        (['in'], UINT, 'iElem'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyDescriptionList_INTERFACE_DEFINED__

        if not defined(__IPropertyStoreFactory_INTERFACE_DEFINED__):
            # interface IPropertyStoreFactory
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyStoreFactory = MIDL_INTERFACE(
                    "{BC110B6D-57E8-4148-A9C6-91015AB2F3A5}"
                )
                IPropertyStoreFactory._iid_ = IID_IPropertyStoreFactory

                IPropertyStoreFactory._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetPropertyStore')],
                        HRESULT,
                        'GetPropertyStore',
                        (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
                        (
                            ['unique', 'in'],
                            POINTER(comtypes.IUnknown),
                           'pUnkFactory'
                        ),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyStoreForKeys')],
                        HRESULT,
                        'GetPropertyStoreForKeys',
                        (['unique', 'in'], POINTER(PROPERTYKEY), 'rgKeys'),
                        (['in'], UINT, 'cKeys'),
                        (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyStoreFactory_INTERFACE_DEFINED__

        if not defined(__IDelayedPropertyStoreFactory_INTERFACE_DEFINED__):
            # interface IDelayedPropertyStoreFactory
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDelayedPropertyStoreFactory = MIDL_INTERFACE(
                    "{40D4577F-E237-4BDB-BD69-58F089431B6A}"
                )
                IDelayedPropertyStoreFactory._iid_ = IID_IDelayedPropertyStoreFactory

                IDelayedPropertyStoreFactory._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetDelayedPropertyStore')],
                        HRESULT,
                        'GetDelayedPropertyStore',
                        (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
                        (['in'], DWORD, 'dwStoreId'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDelayedPropertyStoreFactory_INTERFACE_DEFINED__

        # interface __MIDL_itf_propsys_0000_0021
        # [local]
        # [v1_enum]
        class _PERSIST_SPROPSTORE_FLAGS(ENUM):
            FPSPS_DEFAULT = 0
            FPSPS_READONLY = 0x1
            FPSPS_TREAT_NEW_VALUES_AS_DIRTY = 0x2

        FPSPS_DEFAULT = _PERSIST_SPROPSTORE_FLAGS.FPSPS_DEFAULT
        FPSPS_READONLY = _PERSIST_SPROPSTORE_FLAGS.FPSPS_READONLY
        FPSPS_TREAT_NEW_VALUES_AS_DIRTY = _PERSIST_SPROPSTORE_FLAGS.FPSPS_TREAT_NEW_VALUES_AS_DIRTY
        PERSIST_SPROPSTORE_FLAGS = INT

        PUSERIALIZEDPROPSTORAGE = POINTER(SERIALIZEDPROPSTORAGE)
        PCUSERIALIZEDPROPSTORAGE = POINTER(SERIALIZEDPROPSTORAGE)

        if not defined(__IPersistSerializedPropStorage_INTERFACE_DEFINED__):
            # interface IPersistSerializedPropStorage
            # [object][local][unique][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistSerializedPropStorage = MIDL_INTERFACE(
                    "{E318AD57-0AA0-450F-ACA5-6FAB7103D917}"
                )
                IPersistSerializedPropStorage._iid_ = IID_IPersistSerializedPropStorage

                IPersistSerializedPropStorage._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetFlags')],
                        HRESULT,
                        'SetFlags',
                        (['in'], PERSIST_SPROPSTORE_FLAGS, 'flags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetPropertyStorage')],
                        HRESULT,
                        'SetPropertyStorage',
                        (['in'], PCUSERIALIZEDPROPSTORAGE, 'psps'),
                        (['in'], DWORD, 'cb'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyStorage')],
                        HRESULT,
                        'GetPropertyStorage',
                        (
                            ['out'],
                            POINTER(POINTER(SERIALIZEDPROPSTORAGE)),
                           'ppsps'
                        ),
                        (['out'], POINTER(DWORD), 'pcb'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistSerializedPropStorage_INTERFACE_DEFINED__

        if not defined(__IPersistSerializedPropStorage2_INTERFACE_DEFINED__):
            # interface IPersistSerializedPropStorage2
            # [object][local][unique][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistSerializedPropStorage2 = MIDL_INTERFACE(
                    "{77EFFA68-4F98-4366-BA72-573B3D880571}"
                )
                IPersistSerializedPropStorage2._iid_ = IID_IPersistSerializedPropStorage2

                IPersistSerializedPropStorage2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetPropertyStorageSize')],
                        HRESULT,
                        'GetPropertyStorageSize',
                        (['out'], POINTER(DWORD), 'pcb'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyStorageBuffer')],
                        HRESULT,
                        'GetPropertyStorageBuffer',
                        (['out'], POINTER(SERIALIZEDPROPSTORAGE), 'psps'),
                        (['in'], DWORD, 'cb'),
                        (['out'], POINTER(DWORD), 'pcbWritten'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistSerializedPropStorage2_INTERFACE_DEFINED__

        if not defined(__IPropertySystemChangeNotify_INTERFACE_DEFINED__):
            # interface IPropertySystemChangeNotify
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertySystemChangeNotify = MIDL_INTERFACE(
                    "{FA955FD9-38BE-4879-A6CE-824CF52D609F}"
                )
                IPropertySystemChangeNotify._iid_ = IID_IPropertySystemChangeNotify

                IPropertySystemChangeNotify._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SchemaRefreshed')],
                        HRESULT,
                        'SchemaRefreshed',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertySystemChangeNotify_INTERFACE_DEFINED__

        if not defined(__ICreateObject_INTERFACE_DEFINED__):
            # interface ICreateObject
            # [object][unique][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICreateObject = MIDL_INTERFACE(
                    "{75121952-E0D0-43E5-9380-1D80483ACF72}"
                )
                ICreateObject._iid_ = IID_ICreateObject

                ICreateObject._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateObject')],
                        HRESULT,
                        'CreateObject',
                        (['in'], REFCLSID, 'clsid'),
                        (
                            ['unique', 'in'],
                            POINTER(comtypes.IUnknown),
                           'pUnkOuter'
                        ),
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ICreateObject_INTERFACE_DEFINED__

        # interface __MIDL_itf_propsys_0000_0025
        # [local]
        # Format a property value for display purposes

        # PSSTDAPI PSFormatForDisplay(
        # _In_ REFPROPERTYKEY propkey,
        # _In_ REFPROPVARIANT propvar,
        # _In_ PROPDESC_FORMAT_FLAGS pdfFlags,
        # _Out_writes_(cchText) LPWSTR pwszText,
        # _In_ DWORD cchText);
        PSFormatForDisplay = propsys.PSFormatForDisplay
        PSFormatForDisplay.restype = PSSTDAPI

        # PSSTDAPI PSFormatForDisplayAlloc(
        # _In_ REFPROPERTYKEY key,
        # _In_ REFPROPVARIANT propvar,
        # _In_ PROPDESC_FORMAT_FLAGS pdff,
        # _Outptr_ PWSTR *ppszDisplay);
        PSFormatForDisplayAlloc = propsys.PSFormatForDisplayAlloc
        PSFormatForDisplayAlloc.restype = PSSTDAPI

        # PSSTDAPI PSFormatPropertyValue(
        # _In_ IPropertyStore *pps,
        # _In_ IPropertyDescription *ppd,
        # _In_ PROPDESC_FORMAT_FLAGS pdff,
        # _Outptr_ LPWSTR *ppszDisplay);
        PSFormatPropertyValue = propsys.PSFormatPropertyValue
        PSFormatPropertyValue.restype = PSSTDAPI

        # Retrieve the image reference associated with a property value
        # (if specified)
        # PSSTDAPI PSGetImageReferenceForValue(
        # _In_ REFPROPERTYKEY propkey,
        # _In_ REFPROPVARIANT propvar,
        # _Outptr_ PWSTR *ppszImageRes);
        PSGetImageReferenceForValue = propsys.PSGetImageReferenceForValue
        PSGetImageReferenceForValue.restype = PSSTDAPI

        # Convert a PROPERTYKEY to and from a PWSTR
        # PSSTDAPI PSStringFromPropertyKey(
        # _In_ REFPROPERTYKEY pkey,
        # _Out_writes_(cch) LPWSTR psz,
        # _In_ UINT cch);
        PSStringFromPropertyKey = propsys.PSStringFromPropertyKey
        PSStringFromPropertyKey.restype = PSSTDAPI

        # PSSTDAPI PSPropertyKeyFromString(
        # _In_ LPCWSTR pszString,
        # _Out_ PROPERTYKEY *pkey);
        PSPropertyKeyFromString = propsys.PSPropertyKeyFromString
        PSPropertyKeyFromString.restype = PSSTDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # Creates an in-memory property store
        # Returns an IPropertyStore, IPersistSerializedPropStorage, and
        # related interfaces interface

        # PSSTDAPI PSCreateMemoryPropertyStore(
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreateMemoryPropertyStore = propsys.PSCreateMemoryPropertyStore
        PSCreateMemoryPropertyStore.restype = PSSTDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Create a read-only, delay-bind multiplexing property store
        # Returns an IPropertyStore interface or related interfaces

        # PSSTDAPI PSCreateDelayedMultiplexPropertyStore(
        # _In_ GETPROPERTYSTOREFLAGS flags,
        # _In_ IDelayedPropertyStoreFactory *pdpsf,
        # _In_reads_(cStores) DWORD *rgStoreIds,
        # _In_ DWORD cStores,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreateDelayedMultiplexPropertyStore = (
            propsys.PSCreateDelayedMultiplexPropertyStore
        )
        PSCreateDelayedMultiplexPropertyStore.restype = PSSTDAPI

        # Create a read-only property store from one or more sources
        # (which each must support either IPropertyStore or IPropertySetStorage)
        #
        # Returns an IPropertyStore interface or related interfaces
        # PSSTDAPI PSCreateMultiplexPropertyStore(
        # _In_reads_(cStores) IUnknown **prgpunkStores,
        # _In_ DWORD cStores,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreateMultiplexPropertyStore = propsys.PSCreateMultiplexPropertyStore
        PSCreateMultiplexPropertyStore.restype = PSSTDAPI

        # Create a container for IPropertyChanges
        # Returns an IPropertyChangeArray interface
        # PSSTDAPI PSCreatePropertyChangeArray(
        # _In_reads_opt_(cChanges) PROPERTYKEY *rgpropkey,
        # _In_reads_opt_(cChanges) PKA_FLAGS *rgflags,
        # _In_reads_opt_(cChanges) PROPVARIANT *rgpropvar,
        # _In_ UINT cChanges,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreatePropertyChangeArray = propsys.PSCreatePropertyChangeArray
        PSCreatePropertyChangeArray.restype = PSSTDAPI

        # Create a simple property change
        # Returns an IPropertyChange interface
        # PSSTDAPI PSCreateSimplePropertyChange(
        # _In_ PKA_FLAGS flags,
        # _In_ REFPROPERTYKEY key,
        # _In_ REFPROPVARIANT propvar,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreateSimplePropertyChange = propsys.PSCreateSimplePropertyChange
        PSCreateSimplePropertyChange.restype = PSSTDAPI

        # Get a property description
        # Returns an IPropertyDescription interface
        # PSSTDAPI PSGetPropertyDescription(
        # _In_ REFPROPERTYKEY propkey,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSGetPropertyDescription = propsys.PSGetPropertyDescription
        PSGetPropertyDescription.restype = PSSTDAPI

        # PSSTDAPI PSGetPropertyDescriptionByName(
        # _In_ LPCWSTR pszCanonicalName,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSGetPropertyDescriptionByName = propsys.PSGetPropertyDescriptionByName
        PSGetPropertyDescriptionByName.restype = PSSTDAPI

        # Lookup a per-machine registered file property handler
        # PSSTDAPI PSLookupPropertyHandlerCLSID(
        # _In_ PCWSTR pszFilePath,
        # _Out_ CLSID *pclsid);
        PSLookupPropertyHandlerCLSID = propsys.PSLookupPropertyHandlerCLSID
        PSLookupPropertyHandlerCLSID.restype = PSSTDAPI

        # Get a property handler, on Vista or downlevel to XP
        # punkItem is a shell item created with an SHCreateItemXXX API
        # Returns an IPropertyStore
        # PSSTDAPI PSGetItemPropertyHandler(
        # _In_ IUnknown *punkItem,
        # _In_ BOOL fReadWrite,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSGetItemPropertyHandler = propsys.PSGetItemPropertyHandler
        PSGetItemPropertyHandler.restype = PSSTDAPI

        # Get a property handler, on Vista or downlevel to XP
        # punkItem is a shell item created with an SHCreateItemXXX API
        # punkCreateObject supports ICreateObject
        # Returns an IPropertyStore
        # PSSTDAPI PSGetItemPropertyHandlerWithCreateObject(
        # _In_ IUnknown *punkItem,
        # _In_ BOOL fReadWrite,
        # _In_ IUnknown *punkCreateObject,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSGetItemPropertyHandlerWithCreateObject = (
            propsys.PSGetItemPropertyHandlerWithCreateObject
        )
        PSGetItemPropertyHandlerWithCreateObject.restype = PSSTDAPI

        # Get or set a property value from a store
        # PSSTDAPI PSGetPropertyValue(
        # _In_ IPropertyStore *pps,
        # _In_ IPropertyDescription *ppd,
        # _Out_ PROPVARIANT *ppropvar);
        PSGetPropertyValue = propsys.PSGetPropertyValue
        PSGetPropertyValue.restype = PSSTDAPI

        # PSSTDAPI PSSetPropertyValue(
        # _In_ IPropertyStore *pps,
        # _In_ IPropertyDescription *ppd,
        # _In_ REFPROPVARIANT propvar);
        PSSetPropertyValue = propsys.PSSetPropertyValue
        PSSetPropertyValue.restype = PSSTDAPI

        # Interact with the set of property descriptions
        # PSSTDAPI PSRegisterPropertySchema(
        # _In_ PCWSTR pszPath);
        PSRegisterPropertySchema = propsys.PSRegisterPropertySchema
        PSRegisterPropertySchema.restype = PSSTDAPI

        # PSSTDAPI PSUnregisterPropertySchema(
        # _In_ PCWSTR pszPath);
        PSUnregisterPropertySchema = propsys.PSUnregisterPropertySchema
        PSUnregisterPropertySchema.restype = PSSTDAPI

        # Returns either: IPropertyDescriptionList or IEnumUnknown interfaces
        # PSSTDAPI PSEnumeratePropertyDescriptions(
        # _In_ PROPDESC_ENUMFILTER filterOn,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSEnumeratePropertyDescriptions = (
            propsys.PSEnumeratePropertyDescriptions
        )
        PSEnumeratePropertyDescriptions.restype = PSSTDAPI

        # Convert between a PROPERTYKEY and its canonical name
        # PSSTDAPI PSGetPropertyKeyFromName(
        # _In_ PCWSTR pszName,
        # _Out_ PROPERTYKEY *ppropkey);
        PSGetPropertyKeyFromName = propsys.PSGetPropertyKeyFromName
        PSGetPropertyKeyFromName.restype = PSSTDAPI

        # PSSTDAPI PSGetNameFromPropertyKey(
        # _In_ REFPROPERTYKEY propkey,
        # _Outptr_ PWSTR *ppszCanonicalName);
        PSGetNameFromPropertyKey = propsys.PSGetNameFromPropertyKey
        PSGetNameFromPropertyKey.restype = PSSTDAPI

        # Coerce and canonicalize a property value
        # PSSTDAPI PSCoerceToCanonicalValue(
        # _In_ REFPROPERTYKEY key,
        # _Inout_ PROPVARIANT *ppropvar);
        PSCoerceToCanonicalValue = propsys.PSCoerceToCanonicalValue
        PSCoerceToCanonicalValue.restype = PSSTDAPI

        # Convert a 'prop:' string into a list of property descriptions
        # Returns an IPropertyDescriptionList interface
        # PSSTDAPI PSGetPropertyDescriptionListFromString(
        # _In_ LPCWSTR pszPropList,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSGetPropertyDescriptionListFromString = (
            propsys.PSGetPropertyDescriptionListFromString
        )
        PSGetPropertyDescriptionListFromString.restype = PSSTDAPI

        # Wrap an IPropertySetStorage interface in an IPropertyStore interface
        # Returns an IPropertyStore or related interface
        # PSSTDAPI PSCreatePropertyStoreFromPropertySetStorage(
        # _In_ IPropertySetStorage *ppss,
        # _In_ DWORD grfMode,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreatePropertyStoreFromPropertySetStorage = (
            propsys.PSCreatePropertyStoreFromPropertySetStorage
        )
        PSCreatePropertyStoreFromPropertySetStorage.restype = PSSTDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # punkSource must support IPropertyStore or IPropertySetStorage
        # On success, the returned ppv is guaranteed to support IPropertyStore.
        # If punkSource already supports IPropertyStore, no wrapper is created.

        # PSSTDAPI PSCreatePropertyStoreFromObject(
        # _In_ IUnknown *punk,
        # _In_ DWORD grfMode,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreatePropertyStoreFromObject = (
            propsys.PSCreatePropertyStoreFromObject
        )
        PSCreatePropertyStoreFromObject.restype = PSSTDAPI

        # punkSource must support IPropertyStore
        # riid may be IPropertyStore, IPropertySetStorage,
        # IPropertyStoreCapabilities, or IObjectProvider
        # PSSTDAPI PSCreateAdapterFromPropertyStore(
        # _In_ IPropertyStore *pps,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSCreateAdapterFromPropertyStore = (
            propsys.PSCreateAdapterFromPropertyStore
        )
        PSCreateAdapterFromPropertyStore.restype = PSSTDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Talk to the property system using an interface
        # Returns an IPropertySystem interface

        # PSSTDAPI PSGetPropertySystem(
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSGetPropertySystem = propsys.PSGetPropertySystem
        PSGetPropertySystem.restype = PSSTDAPI

        # Obtain a value from serialized property storage
        # PSSTDAPI PSGetPropertyFromPropertyStorage(
        # _In_reads_bytes_(cb) PCUSERIALIZEDPROPSTORAGE psps,
        # _In_ DWORD cb,
        # _In_ REFPROPERTYKEY rpkey,
        # _Out_ PROPVARIANT *ppropvar);
        PSGetPropertyFromPropertyStorage = (
            propsys.PSGetPropertyFromPropertyStorage
        )
        PSGetPropertyFromPropertyStorage.restype = PSSTDAPI

        # Obtain a named value from serialized property storage
        # PSSTDAPI PSGetNamedPropertyFromPropertyStorage(
        # _In_reads_bytes_(cb) PCUSERIALIZEDPROPSTORAGE psps,
        # _In_ DWORD cb,
        # _In_ LPCWSTR pszName,
        # _Out_ PROPVARIANT *ppropvar);
        PSGetNamedPropertyFromPropertyStorage = (
            propsys.PSGetNamedPropertyFromPropertyStorage
        )
        PSGetNamedPropertyFromPropertyStorage.restype = PSSTDAPI

        # Helper functions for reading and writing values from IPropertyBag's.
        # PSSTDAPI PSPropertyBag_ReadType(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ VARIANT *var,
        # VARTYPE type);
        PSPropertyBag_ReadType = propsys.PSPropertyBag_ReadType
        PSPropertyBag_ReadType.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadStr(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_writes_(CHARacterCount) LPWSTR value,
        # INT characterCount);
        PSPropertyBag_ReadStr = propsys.PSPropertyBag_ReadStr
        PSPropertyBag_ReadStr.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadStrAlloc(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Outptr_ PWSTR *value);
        PSPropertyBag_ReadStrAlloc = propsys.PSPropertyBag_ReadStrAlloc
        PSPropertyBag_ReadStrAlloc.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadBSTR(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Outptr_ BSTR *value);
        PSPropertyBag_ReadBSTR = propsys.PSPropertyBag_ReadBSTR
        PSPropertyBag_ReadBSTR.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteStr(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ LPCWSTR value);
        PSPropertyBag_WriteStr = propsys.PSPropertyBag_WriteStr
        PSPropertyBag_WriteStr.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteBSTR(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ BSTR value);
        PSPropertyBag_WriteBSTR = propsys.PSPropertyBag_WriteBSTR
        PSPropertyBag_WriteBSTR.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadInt(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ INT *value);
        PSPropertyBag_ReadInt = propsys.PSPropertyBag_ReadInt
        PSPropertyBag_ReadInt.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteInt(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # INT value);
        PSPropertyBag_WriteInt = propsys.PSPropertyBag_WriteInt
        PSPropertyBag_WriteInt.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadSHORT(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ SHORT *value);
        PSPropertyBag_ReadSHORT = propsys.PSPropertyBag_ReadSHORT
        PSPropertyBag_ReadSHORT.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteSHORT(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # SHORT value);
        PSPropertyBag_WriteSHORT = propsys.PSPropertyBag_WriteSHORT
        PSPropertyBag_WriteSHORT.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadLONG(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ LONG *value);
        PSPropertyBag_ReadLONG = propsys.PSPropertyBag_ReadLONG
        PSPropertyBag_ReadLONG.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteLONG(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # LONG value);
        PSPropertyBag_WriteLONG = propsys.PSPropertyBag_WriteLONG
        PSPropertyBag_WriteLONG.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadDWORD(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ DWORD *value);
        PSPropertyBag_ReadDWORD = propsys.PSPropertyBag_ReadDWORD
        PSPropertyBag_ReadDWORD.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteDWORD(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # DWORD value);
        PSPropertyBag_WriteDWORD = propsys.PSPropertyBag_WriteDWORD
        PSPropertyBag_WriteDWORD.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadBOOL(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ BOOL *value);
        PSPropertyBag_ReadBOOL = propsys.PSPropertyBag_ReadBOOL
        PSPropertyBag_ReadBOOL.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteBOOL(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # BOOL value);
        PSPropertyBag_WriteBOOL = propsys.PSPropertyBag_WriteBOOL
        PSPropertyBag_WriteBOOL.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadPOINTL(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ POINTL *value);
        PSPropertyBag_ReadPOINTL = propsys.PSPropertyBag_ReadPOINTL
        PSPropertyBag_ReadPOINTL.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WritePOINTL(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ POINTL *value);
        PSPropertyBag_WritePOINTL = propsys.PSPropertyBag_WritePOINTL
        PSPropertyBag_WritePOINTL.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadPOINTS(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ POINTS *value);
        PSPropertyBag_ReadPOINTS = propsys.PSPropertyBag_ReadPOINTS
        PSPropertyBag_ReadPOINTS.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WritePOINTS(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ POINTS *value);
        PSPropertyBag_WritePOINTS = propsys.PSPropertyBag_WritePOINTS
        PSPropertyBag_WritePOINTS.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadRECTL(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ RECTL *value);
        PSPropertyBag_ReadRECTL = propsys.PSPropertyBag_ReadRECTL
        PSPropertyBag_ReadRECTL.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteRECTL(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ RECTL *value);
        PSPropertyBag_WriteRECTL = propsys.PSPropertyBag_WriteRECTL
        PSPropertyBag_WriteRECTL.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadStream(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Outptr_ IStream **value);
        PSPropertyBag_ReadStream = propsys.PSPropertyBag_ReadStream
        PSPropertyBag_ReadStream.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteStream(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ IStream *value);
        PSPropertyBag_WriteStream = propsys.PSPropertyBag_WriteStream
        PSPropertyBag_WriteStream.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_Delete(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName);
        PSPropertyBag_Delete = propsys.PSPropertyBag_Delete
        PSPropertyBag_Delete.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadULONGLONG(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ ULONGLONG *value);
        PSPropertyBag_ReadULONGLONG = propsys.PSPropertyBag_ReadULONGLONG
        PSPropertyBag_ReadULONGLONG.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteULONGLONG(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # ULONGLONG value);
        PSPropertyBag_WriteULONGLONG = propsys.PSPropertyBag_WriteULONGLONG
        PSPropertyBag_WriteULONGLONG.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadUnknown(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ REFIID riid,
        # _Outptr_ VOID **ppv);
        PSPropertyBag_ReadUnknown = propsys.PSPropertyBag_ReadUnknown
        PSPropertyBag_ReadUnknown.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteUnknown(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ IUnknown *punk);
        PSPropertyBag_WriteUnknown = propsys.PSPropertyBag_WriteUnknown
        PSPropertyBag_WriteUnknown.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadGUID(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ GUID *value);
        PSPropertyBag_ReadGUID = propsys.PSPropertyBag_ReadGUID
        PSPropertyBag_ReadGUID.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WriteGUID(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ GUID *value);
        PSPropertyBag_WriteGUID = propsys.PSPropertyBag_WriteGUID
        PSPropertyBag_WriteGUID.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_ReadPropertyKey(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _Out_ PROPERTYKEY *value);
        PSPropertyBag_ReadPropertyKey = propsys.PSPropertyBag_ReadPropertyKey
        PSPropertyBag_ReadPropertyKey.restype = PSSTDAPI

        # PSSTDAPI PSPropertyBag_WritePropertyKey(
        # _In_ IPropertyBag *propBag,
        # _In_ LPCWSTR propName,
        # _In_ REFPROPERTYKEY value);
        PSPropertyBag_WritePropertyKey = propsys.PSPropertyBag_WritePropertyKey
        PSPropertyBag_WritePropertyKey.restype = PSSTDAPI

        if not defined(__PropSysObjects_LIBRARY_DEFINED__):
            # library PropSysObjects
            # [version][lcid][uuid]
            if defined(__cplusplus):
                pass
            # END IF

            if defined(__cplusplus):
                pass
            # END IF

            if defined(__cplusplus):
                pass
            # END IF

        # END IF  __PropSysObjects_LIBRARY_DEFINED__

        # interface __MIDL_itf_propsys_0000_0026
        # [local]
        if _MSC_VER >= 1200:
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

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


