import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

COMMETHOD = comtypes.COMMETHOD

__REQUIRED_RPCNDR_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__corpub_h__ = None
__CorpubPublish_FWD_DEFINED__ = None
__ICorPublish_FWD_DEFINED__ = None
__ICorPublishEnum_FWD_DEFINED__ = None
__ICorPublishProcess_FWD_DEFINED__ = None
__ICorPublishAppDomain_FWD_DEFINED__ = None
__ICorPublishProcessEnum_FWD_DEFINED__ = None
__ICorPublishAppDomainEnum_FWD_DEFINED__ = None
__CorpubProcessLib_LIBRARY_DEFINED__ = None
__ICorPublish_INTERFACE_DEFINED__ = None
__ICorPublishEnum_INTERFACE_DEFINED__ = None
__ICorPublishProcess_INTERFACE_DEFINED__ = None
__ICorPublishAppDomain_INTERFACE_DEFINED__ = None
__ICorPublishProcessEnum_INTERFACE_DEFINED__ = None
__ICorPublishAppDomainEnum_INTERFACE_DEFINED__ = None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 6.00.0366
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    __REQUIRED_RPCNDR_H_VERSION__ = 475
# END IF

from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF   __RPCNDR_H_VERSION__

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

if not defined(__corpub_h__):
    __corpub_h__ = VOID
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__CorpubPublish_FWD_DEFINED__):
        __CorpubPublish_FWD_DEFINED__ = VOID

        if defined(__cplusplus):
            pass
        else:

            class CorpubPublish(comtypes.CoClass):
                pass
        # END IF  __cplusplus
    # END IF  __CorpubPublish_FWD_DEFINED__

    if not defined(__ICorPublish_FWD_DEFINED__):
        __ICorPublish_FWD_DEFINED__ = VOID


        class ICorPublish(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorPublish_FWD_DEFINED__

    if not defined(__ICorPublishEnum_FWD_DEFINED__):
        __ICorPublishEnum_FWD_DEFINED__ = VOID


        class ICorPublishEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorPublishEnum_FWD_DEFINED__

    if not defined(__ICorPublishProcess_FWD_DEFINED__):
        __ICorPublishProcess_FWD_DEFINED__ = VOID


        class ICorPublishProcess(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorPublishProcess_FWD_DEFINED__

    if not defined(__ICorPublishAppDomain_FWD_DEFINED__):
        __ICorPublishAppDomain_FWD_DEFINED__ = VOID


        class ICorPublishAppDomain(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorPublishAppDomain_FWD_DEFINED__

    if not defined(__ICorPublishProcessEnum_FWD_DEFINED__):
        __ICorPublishProcessEnum_FWD_DEFINED__ = VOID


        class ICorPublishProcessEnum(ICorPublishEnum):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorPublishProcessEnum_FWD_DEFINED__

    if not defined(__ICorPublishAppDomainEnum_FWD_DEFINED__):
        __ICorPublishAppDomainEnum_FWD_DEFINED__ = VOID


        class ICorPublishAppDomainEnum(ICorPublishEnum):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorPublishAppDomainEnum_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwn_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_corpub_0000
    # [local]
    _ZERO_ = 0
    if _ZERO_:
        pass
    # END IF

    class __MIDL___MIDL_itf_corpub_0000_0001(ENUM):
        COR_PUB_MANAGEDONLY = 0x1

    COR_PUB_ENUMPROCESS = __MIDL___MIDL_itf_corpub_0000_0001
    if not defined(__CorpubProcessLib_LIBRARY_DEFINED__):
        __CorpubProcessLib_LIBRARY_DEFINED__ = VOID

        LIBID_CorpubProcessLib = DECLSPEC_UUID(
            "047a9a40-657e-11d3-8d5b-00104b35e7ef"
        )

        CLSID_CorpubPublish = CLSID(
            "047a9a40-657e-11d3-8d5b-00104b35e7ef"
        )

        class CorpubProcessLib(object):
            name = 'CorpubProcessLib'
            _reg_typelib_ = (LIBID_CorpubProcessLib, 1, 0)


        CorpubPublish._reg_clsid_ = CLSID_CorpubPublish
        CorpubPublish._idlflags_ = []
        CorpubPublish._reg_typelib_ = (LIBID_CorpubProcessLib, 1, 0)
        CorpubPublish._com_interfaces_ = [ICorpubPublish]

        # library CorpubProcessLib
        # [helpstring][version][uuid]
        if defined(__cplusplus):
            pass
        # END IF

    # END IF  __CorpubProcessLib_LIBRARY_DEFINED__

    if not defined(__ICorPublish_INTERFACE_DEFINED__):
        __ICorPublish_INTERFACE_DEFINED__ = VOID

        # interface ICorPublish
        # [local][unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorPublish = MIDL_INTERFACE(
                "{9613A0E7-5A68-11D3-8F84-00A0C9B4D50C}"
            )
            ICorPublish._iid_ = IID_ICorPublish

            ICorPublish._methods_ = [
                COMMETHOD(
                    [helpstring('Method EnumProcesses')],
                    HRESULT,
                    'EnumProcesses',
                    (['in'], COR_PUB_ENUMPROCESS, 'Type'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorPublishProcessEnum)),
                        'ppIEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetProcess')],
                    HRESULT,
                    'GetProcess',
                    (['in'], UINT, 'pid'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorPublishProcess)),
                        'ppProcess'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorPublish_INTERFACE_DEFINED__

    if not defined(__ICorPublishEnum_INTERFACE_DEFINED__):
        __ICorPublishEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorPublishEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorPublishEnum = MIDL_INTERFACE(
                "{C0B22967-5A69-11D3-8F84-00A0C9B4D50C}"
            )
            ICorPublishEnum._iid_ = IID_ICorPublishEnum

            ICorPublishEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Skip')],
                    HRESULT,
                    'Skip',
                    (['in'], ULONG, 'celt'),
                ),
                COMMETHOD(
                    [helpstring('Method Reset')],
                    HRESULT,
                    'Reset',
                ),
                COMMETHOD(
                    [helpstring('Method Clone')],
                    HRESULT,
                    'Clone',
                    (['out'], POINTER(POINTER(ICorPublishEnum)), 'ppEnum'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCount')],
                    HRESULT,
                    'GetCount',
                    (['out'], POINTER(ULONG), 'pcelt'),
                ),
            ]

        # END IF  C style interface
    # END IF ICorPublishEnum_INTERFACE_DEFINED__

    if not defined(__ICorPublishProcess_INTERFACE_DEFINED__):
        __ICorPublishProcess_INTERFACE_DEFINED__ = VOID

        # interface ICorPublishProcess
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorPublishProcess = MIDL_INTERFACE(
                "{18D87AF1-5A6A-11D3-8F84-00A0C9B4D50C}"
            )
            ICorPublishProcess._iid_ = IID_ICorPublishProcess

            ICorPublishProcess._methods_ = [
                COMMETHOD(
                    [helpstring('Method IsManaged')],
                    HRESULT,
                    'IsManaged',
                    (['out'], POINTER(BOOL), 'pbManaged'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumAppDomains')],
                    HRESULT,
                    'EnumAppDomains',
                    (
                        ['out'],
                        POINTER(POINTER(ICorPublishAppDomainEnum)),
                        'ppEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetProcessID')],
                    HRESULT,
                    'GetProcessID',
                    (['out'], POINTER(UINT), 'pid'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDisplayName')],
                    HRESULT,
                    'GetDisplayName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], POINTER(WCHAR), 'szName'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorPublishProcess_INTERFACE_DEFINED__

    if not defined(__ICorPublishAppDomain_INTERFACE_DEFINED__):
        __ICorPublishAppDomain_INTERFACE_DEFINED__ = VOID

        # interface ICorPublishAppDomain
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorPublishAppDomain = MIDL_INTERFACE(
                "{D6315C8F-5A6A-11D3-8F84-00A0C9B4D50C}"
            )
            ICorPublishAppDomain._iid_ = IID_ICorPublishAppDomain

            ICorPublishAppDomain._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetID')],
                    HRESULT,
                    'GetID',
                    (['out'], POINTER(ULONG32), 'puId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], POINTER(WCHAR), 'szName'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorPublishAppDomain_INTERFACE_DEFINED__

    if not defined(__ICorPublishProcessEnum_INTERFACE_DEFINED__):
        __ICorPublishProcessEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorPublishProcessEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorPublishProcessEnum = MIDL_INTERFACE(
                "{A37FBD41-5A69-11D3-8F84-00A0C9B4D50C}"
            )
            ICorPublishProcessEnum._iid_ = IID_ICorPublishProcessEnum

            ICorPublishProcessEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorPublishProcess)),
                        'objects'
                    ),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorPublishProcessEnum_INTERFACE_DEFINED__

    if not defined(__ICorPublishAppDomainEnum_INTERFACE_DEFINED__):
        __ICorPublishAppDomainEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorPublishAppDomainEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorPublishAppDomainEnum = MIDL_INTERFACE(
                "{9F0C98F5-5A6A-11D3-8F84-00A0C9B4D50C}"
            )
            ICorPublishAppDomainEnum._iid_ = IID_ICorPublishAppDomainEnum

            ICorPublishAppDomainEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorPublishAppDomain)),
                        'objects'
                    ),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorPublishAppDomainEnum_INTERFACE_DEFINED__

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF
