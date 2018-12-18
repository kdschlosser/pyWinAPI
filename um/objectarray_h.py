import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__objectarray_h__ = None
__IObjectArray_FWD_DEFINED__ = None
__IObjectCollection_FWD_DEFINED__ = None
__IObjectArray_INTERFACE_DEFINED__ = None
__IObjectCollection_INTERFACE_DEFINED__ = None


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


if not defined(__objectarray_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IObjectArray_FWD_DEFINED__):

        class IObjectArray(comtypes.IUnknown):
            """
            Unknown Object Array
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IObjectArray_FWD_DEFINED__

    if not defined(__IObjectCollection_FWD_DEFINED__):
        class IObjectCollection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IObjectCollection_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.oaidl_h import * # NOQA
    from pyWinAPI.um.ocidl_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_objectarray_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IObjectArray_INTERFACE_DEFINED__):
            # interface IObjectArray
            # [unique][object][uuid][helpstring]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IObjectArray = MIDL_INTERFACE(
                    "{92CA9DCD-5622-4BBA-A805-5E9F541BD8C9}"
                )
                IObjectArray._iid_ = IID_IObjectArray

                IObjectArray._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(UINT), 'pcObjects'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAt')],
                        HRESULT,
                        'GetAt',
                        (['in'], UINT, 'uiIndex'),
                        (['in'], REFIID, 'riid'),
                        (['out', 'iid_is'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IObjectArray_INTERFACE_DEFINED__

        if not defined(__IObjectCollection_INTERFACE_DEFINED__):
            # interface IObjectCollection
            # [unique][object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IObjectCollection = MIDL_INTERFACE(
                    "{5632B1A4-E38A-400A-928A-D4CD63230295}"
                )
                IObjectCollection._iid_ = IID_IObjectCollection

                IObjectCollection._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AddObject')],
                        HRESULT,
                        'AddObject',
                        (['in'], POINTER(comtypes.IUnknown), 'punk'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddFromArray')],
                        HRESULT,
                        'AddFromArray',
                        (['in'], POINTER(IObjectArray), 'poaSource'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveObjectAt')],
                        HRESULT,
                        'RemoveObjectAt',
                        (['in'], UINT, 'uiIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Clear')],
                        HRESULT,
                        'Clear',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IObjectCollection_INTERFACE_DEFINED__

        # interface __MIDL_itf_objectarray_0000_0002
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # Additional Prototypes for ALL interfaces

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


