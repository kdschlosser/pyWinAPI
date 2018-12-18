import ctypes
import comtypes
import comtypes.automation
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring
IUnknown = comtypes.IUnknown


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__unknwnbase_h__ = None
__IUnknown_FWD_DEFINED__ = None
__AsyncIUnknown_FWD_DEFINED__ = None
__IClassFactory_FWD_DEFINED__ = None
__IUnknown_INTERFACE_DEFINED__ = None
__AsyncIUnknown_INTERFACE_DEFINED__ = None
__IClassFactory_INTERFACE_DEFINED__ = None


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


if not defined(__unknwnbase_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IUnknown_FWD_DEFINED__):
        pass
    # END IF  __IUnknown_FWD_DEFINED__

    if not defined(__AsyncIUnknown_FWD_DEFINED__):
        class AsyncIUnknown(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __AsyncIUnknown_FWD_DEFINED__

    if not defined(__IClassFactory_FWD_DEFINED__):
        class IClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IClassFactory_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.wtypesbase_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_unknwnbase_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    # +
    # -------------------------------------------------------------------------
    # Microsoft Windows
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # --------------------------------------------------------------------
    if _MSC_VER >= 1020:
        pass
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IUnknown_INTERFACE_DEFINED__):
            # interface IUnknown
            # [unique][uuid][object][local]
            # [unique]
            LPUNKNOWN = POINTER(comtypes.IUnknown)

            # ////////////////////////////////////////////////////////////////
            # IID_IUnknown and all other system IIDs are provided in UUID.LIB
            # Link that library in with your proxies, clients and servers
            # ////////////////////////////////////////////////////////////////
            if _MSC_VER >= 1100 and defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUnknown = MIDL_INTERFACE(
                        "{00000000-0000-0000-C000-000000000046}"
                    )

                # END IF  C style interface
            # END IF  __IUnknown_INTERFACE_DEFINED__
            # interface __MIDL_itf_unknwnbase_0000_0001
            # [local]
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__AsyncIUnknown_INTERFACE_DEFINED__):
            # interface AsyncIUnknown
            # [unique][uuid][object][local]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_AsyncIUnknown = MIDL_INTERFACE(
                    "{000E0000-0000-0000-C000-000000000046}"
                )
                AsyncIUnknown._iid_ = IID_AsyncIUnknown

                AsyncIUnknown._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Begin_QueryInterface')],
                        HRESULT,
                        'Begin_QueryInterface',
                        (['in'], REFIID, 'riid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_QueryInterface')],
                        HRESULT,
                        'Finish_QueryInterface',
                        (['out'], POINTER(POINTER(VOID)), 'ppvObject'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Begin_AddRef')],
                        HRESULT,
                        'Begin_AddRef',
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_AddRef')],
                        ULONG,
                        'Finish_AddRef',
                    ),
                    COMMETHOD(
                        [helpstring('Method Begin_Release')],
                        HRESULT,
                        'Begin_Release',
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_Release')],
                        ULONG,
                        'Finish_Release',
                    ),
                ]

            # END IF  C style interface
        # END IF  __AsyncIUnknown_INTERFACE_DEFINED__

        # interface __MIDL_itf_unknwnbase_0000_0002
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IClassFactory_INTERFACE_DEFINED__):
            # interface IClassFactory
            # [unique][uuid][object]
            # [unique]
            LPCLASSFACTORY = POINTER(IClassFactory)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IClassFactory = MIDL_INTERFACE(
                    "{00000001-0000-0000-C000-000000000046}"
                )
                IClassFactory._iid_ = IID_IClassFactory

                IClassFactory._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateInstance'), 'local'],
                        HRESULT,
                        'CreateInstance',
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppvObject'),
                    ),
                    COMMETHOD(
                        [helpstring('Method LockServer'), 'local'],
                        HRESULT,
                        'LockServer',
                        (['in'], BOOL, 'fLock'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IClassFactory_INTERFACE_DEFINED__
        # interface __MIDL_itf_unknwnbase_0000_0003
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # Additional Prototypes for ALL interfaces    # [local]

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


