import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD


class tagCATEGORYINFO(ctypes.Structure):
    pass


CATEGORYINFO = tagCATEGORYINFO



def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file

__REQUIRED_RPCNDR_H_VERSION__ = None

if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    __REQUIRED_RPCNDR_H_VERSION__ = 500
# END IF

# verify that the <rpcsal.h> version is high enough to compile this file


__REQUIRED_RPCSAL_H_VERSION__ = None
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    __REQUIRED_RPCSAL_H_VERSION__ = 100
# END IF

from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA

__RPCNDR_H_VERSION__ = None

if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

COM_NO_WINDOWS_H = None
if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

__comcat_h__ = None
if not defined(__comcat_h__):
    __comcat_h__ = 1

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF
    __IEnumGUID_INTERFACE_DEFINED__ = 1
    __IEnumCATEGORYINFO_INTERFACE_DEFINED__ = 1
    __ICatRegister_INTERFACE_DEFINED__ = 1
    __ICatInformation_INTERFACE_DEFINED__ = 1

    # Forward Declarations
    __IEnumGUID_FWD_DEFINED__ = None
    if not defined(__IEnumGUID_FWD_DEFINED__):
        __IEnumGUID_FWD_DEFINED__ = 1
        __IEnumGUID_INTERFACE_DEFINED__ = None

        IID_IEnumGUID = MIDL_INTERFACE(
            "{0002E000-0000-0000-C000-000000000046}"
        )


        class IEnumGUID(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumGUID

    # END IF  __IEnumGUID_FWD_DEFINED__

    __IEnumCATEGORYINFO_FWD_DEFINED__ = None
    if not defined(__IEnumCATEGORYINFO_FWD_DEFINED__):
        __IEnumCATEGORYINFO_FWD_DEFINED__ = 1
        __IEnumCATEGORYINFO_INTERFACE_DEFINED__ = None

        IID_IEnumCATEGORYINFO = MIDL_INTERFACE(
            "{0002E011-0000-0000-C000-000000000046}"
        )


        class IEnumCATEGORYINFO(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumCATEGORYINFO

    # END IF  __IEnumCATEGORYINFO_FWD_DEFINED__

    __ICatRegister_FWD_DEFINED__ = None
    if not defined(__ICatRegister_FWD_DEFINED__):
        __ICatRegister_FWD_DEFINED__ = 1
        __ICatRegister_INTERFACE_DEFINED__ = None

        IID_ICatRegister = MIDL_INTERFACE(
            "{0002E012-0000-0000-C000-000000000046}"
        )


        class ICatRegister(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICatRegister

    # END IF  __ICatRegister_FWD_DEFINED__

    __ICatInformation_FWD_DEFINED__ = None
    if not defined(__ICatInformation_FWD_DEFINED__):
        __ICatInformation_FWD_DEFINED__ = 1
        __ICatInformation_INTERFACE_DEFINED__ = None

        IID_ICatInformation = MIDL_INTERFACE(
            "{0002E013-0000-0000-C000-000000000046}"
        )


        class ICatInformation(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICatInformation

    # END IF  __ICatInformation_FWD_DEFINED__


    # header files for imported files

    from pyWinAPI.um.unknwn_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_comcat_0000_0000
    # [local]
    # = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - =
    # ComCat.h
    # = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - =
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
    # ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
    # THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
    # PARTICULAR PURPOSE.
    # = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - =
    # = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - =
    # OLE Componet Categories Interfaces.
    # = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - =
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # //////////////////////////////////////////////////////////////////////////
        #
        # Types
        CLSID_StdComponentCategoriesMgr = None
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        CATID = GUID
        REFCATID = REFGUID
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        IID_IEnumCLSID = IID_IEnumGUID
        IEnumCLSID = IEnumGUID
        LPENUMCLSID = POINTER(IEnumGUID)
        CATID_NULL = GUID_NULL


        def IsEqualCATID(rcatid1, rcatid2):
            return IsEqualGUID(rcatid1, rcatid2)


        IID_IEnumCATID = IID_IEnumGUID
        IEnumCATID = IEnumGUID

        CATID_Insertable = CATID
        CATID_Control = CATID
        CATID_Programmable = CATID
        CATID_IsShortcut = CATID
        CATID_NeverShowExt = CATID
        CATID_DocObject = CATID
        CATID_Printable = CATID
        CATID_RequiresDataPathHost = CATID
        CATID_PersistsToMoniker = CATID
        CATID_PersistsToStorage = CATID
        CATID_PersistsToStreamInit = CATID
        CATID_PersistsToStream = CATID
        CATID_PersistsToMemory = CATID
        CATID_PersistsToFile = CATID
        CATID_PersistsToPropertyBag = CATID
        CATID_InternetAware = CATID
        CATID_DesignTimeUIActivatableControl = CATID

        # //////////////////////////////////////////////////////////////////////////
        #
        # Category IDs (link to uuid3.lib)
        # //////////////////////////////////////////////////////////////////////////
        #
        # Interface Definitions
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        _LPENUMGUID_DEFINED = None
        if not defined(_LPENUMGUID_DEFINED):
            _LPENUMGUID_DEFINED = 1

            if not defined(__IEnumGUID_INTERFACE_DEFINED__):
                __IEnumGUID_INTERFACE_DEFINED__ = 1

                LPENUMGUID = POINTER(IEnumGUID)

                # interface IEnumGUID
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass

                else:
                    IEnumGUID._methods_ = [
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (
                                ['out', annotation('_Out_writes_to_(celt,*pceltFetched)')],
                                POINTER(GUID),
                               'rgelt'
                            ),
                            (
                                ['out', annotation('_Out_opt_')],
                                POINTER(ULONG),
                               'pceltFetched'
                            ),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteNext',
                            (['in'], ULONG, 'celt'),
                            (['out'], POINTER(GUID), 'rgelt'),
                            (['out'], POINTER(ULONG), 'pceltFetched'),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Skip',
                            (['in'], ULONG, 'celt'),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Reset',
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Clone',
                            (['out'], POINTER(POINTER(IEnumGUID)), 'ppenum'),
                        ),
                    ]
                # END IF  C style interface
            # END IF __IEnumGUID_INTERFACE_DEFINED__
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        _LPENUMCATEGORYINFO_DEFINED = None

        if not defined(_LPENUMCATEGORYINFO_DEFINED):
            _LPENUMCATEGORYINFO_DEFINED = 1

            __MIDL_itf_comcat_0000_0001_v0_0_c_ifspec = RPC_IF_HANDLE
            __MIDL_itf_comcat_0000_0001_v0_0_s_ifspec = RPC_IF_HANDLE

            if not defined(__IEnumCATEGORYINFO_INTERFACE_DEFINED__):
                __IEnumCATEGORYINFO_INTERFACE_DEFINED__ = 1
                # interface IEnumCATEGORYINFO
                # [unique][uuid][object]
                tagCATEGORYINFO._fields_ = [
                    ('catid', CATID),
                    ('lcid', LCID),
                    ('szDescription', OLECHAR * 128),
                ]
                LPCATEGORYINFO = POINTER(tagCATEGORYINFO)

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IEnumCATEGORYINFO._methods_ = [
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (['out'], POINTER(CATEGORYINFO), 'rgelt'),
                            (['out'], POINTER(ULONG), 'pceltFetched'),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Skip',
                            (['in'], ULONG, 'celt'),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Reset',
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Clone',
                            (
                                ['out'],
                                POINTER(POINTER(IEnumCATEGORYINFO)),
                               'ppenum'
                            ),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IEnumCATEGORYINFO_INTERFACE_DEFINED__
            # interface __MIDL_itf_comcat_0000_0002
            # [local]
        # END IF
        _LPCATREGISTER_DEFINED = None
        if not defined(_LPCATREGISTER_DEFINED):
            _LPCATREGISTER_DEFINED = 1

            if not defined(__ICatRegister_INTERFACE_DEFINED__):
                __ICatRegister_INTERFACE_DEFINED__ = 1
                # interface ICatRegister
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    ICatRegister._methods_ = [
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RegisterCategories',
                            (['in'], ULONG, 'cCategories'),
                            (['in'], CATEGORYINFO * 0, 'rgCategoryInfo'),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UnRegisterCategories',
                            (['in'], ULONG, 'cCategories'),
                            (['in'], CATID * 0, 'rgcatid'),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RegisterClassImplCategories',
                            (['in'], REFCLSID, 'rclsid'),
                            (['in'], ULONG, 'cCategories'),
                            (['in'], CATID * 0, 'rgcatid'),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UnRegisterClassImplCategories',
                            (['in'], REFCLSID, 'rclsid'),
                            (['in'], ULONG, 'cCategories'),
                            (['in'], CATID * 0, 'rgcatid'),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RegisterClassReqCategories',
                            (['in'], REFCLSID, 'rclsid'),
                            (['in'], ULONG, 'cCategories'),
                            (['in'], CATID * 0, 'rgcatid'),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UnRegisterClassReqCategories',
                            (['in'], REFCLSID, 'rclsid'),
                            (['in'], ULONG, 'cCategories'),
                            (['in'], CATID * 0, 'rgcatid'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ICatRegister_INTERFACE_DEFINED__
            # interface __MIDL_itf_comcat_0000_0003
            # [local]
        # END IF
        _LPCATINFORMATION_DEFINED = None
        if not defined(_LPCATINFORMATION_DEFINED):
            _LPCATINFORMATION_DEFINED = 1

            if not defined(__ICatInformation_INTERFACE_DEFINED__):
                __ICatInformation_INTERFACE_DEFINED__ = 1

                # interface ICatInformation
                # [unique][uuid][object]


                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    ICatInformation._methods_ = [
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnumCategories',
                            (['in'], LCID, 'lcid'),
                            (
                                ['out'],
                                POINTER(POINTER(IEnumCATEGORYINFO)),
                               'ppenumCategoryInfo'
                            ),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetCategoryDesc',
                            (['in'], REFCATID, 'rcatid'),
                            (['in'], LCID, 'lcid'),
                            (['out'], POINTER(LPWSTR), 'pszDesc'),
                        ),
                        #
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'EnumClassesOfCategories',
                            (['in'], ULONG, 'cImplemented'),
                            (['in'], CATID * 0, 'rgcatidImpl'),
                            (['in'], ULONG, 'cRequired'),
                            (['in'], CATID * 0, 'rgcatidReq'),
                            (
                                ['out'],
                                POINTER(POINTER(IEnumCLSID)),
                               'ppenumClsid'
                            ),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteEnumClassesOfCategories',
                            (['in'], ULONG, 'cImplemented'),
                            (['unique', 'in'], CATID * 0, 'rgcatidImpl'),
                            (['in'], ULONG, 'cRequired'),
                            (['unique', 'in'], CATID * 0, 'rgcatidReq'),
                            (
                                ['out'],
                                POINTER(POINTER(IEnumCLSID)),
                               'ppenumClsid'
                            ),
                        ),
                        #
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'IsClassOfCategories',
                            (['in'], REFCLSID, 'rclsid'),
                            (['in'], ULONG, 'cImplemented'),
                            (['in'], CATID * 0, 'rgcatidImpl'),
                            (['in'], ULONG, 'cRequired'),
                            (['in'], CATID * 0, 'rgcatidReq'),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteIsClassOfCategories',
                            (['in'], REFCLSID, 'rclsid'),
                            (['in'], ULONG, 'cImplemented'),
                            (['unique', 'in'], CATID * 0, 'rgcatidImpl'),
                            (['in'], ULONG, 'cRequired'),
                            (['unique', 'in'], CATID * 0, 'rgcatidReq'),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnumImplCategoriesOfClass',
                            (['in'], REFCLSID, 'rclsid'),
                            (
                                ['out'],
                                POINTER(POINTER(IEnumCATID)),
                               'ppenumCatid'
                            ),
                        ),
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnumReqCategoriesOfClass',
                            (['in'], REFCLSID, 'rclsid'),
                            (
                                ['out'],
                                POINTER(POINTER(IEnumCATID)),
                               'ppenumCatid'
                            ),
                        ),
                    ]
                # END IF  C style interface
            # interface __MIDL_itf_comcat_0000_0004
            # [local]
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF
# END IF
