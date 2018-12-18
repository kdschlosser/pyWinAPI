import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__objsafe_h__ = None
__IObjectSafety_FWD_DEFINED__ = None
__IObjectSafety_INTERFACE_DEFINED__ = None

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

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF


if not defined(__objsafe_h__):
    # Forward Declarations
    if not defined(__IObjectSafety_FWD_DEFINED__):
        class IObjectSafety(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IObjectSafety_FWD_DEFINED__

    # header files for imported files
    from unknwn_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        if not defined(_LPSAFEOBJECT_DEFINED):
            _LPSAFEOBJECT_DEFINED = VOID
            INTERFACESAFE_FOR_UNTRUSTED_CALLER = 0x00000001 # Caller of interface may be untrusted
            INTERFACESAFE_FOR_UNTRUSTED_DATA = 0x00000002 # Data passed into interface may be untrusted
            INTERFACE_USES_DISPEX = 0x00000004 # Object knows to use IDispatchEx
            INTERFACE_USES_SECURITY_MANAGER = 0x00000008 # Object knows to use IInternetHostSecurityManager

            # {CB5BDC81-93C1-11cf-8F20-00805F2CD064}
            IID_IObjectSafety = DEFINE_GUID(
                0xcb5bdc81,
                0x93c1,
                0x11cf,
                0x8f,
                0x20,
                0x0,
                0x80,
                0x5f,
                0x2c,
                0xd0,
                0x64
            )

            if not defined(__IObjectSafety_INTERFACE_DEFINED__):
                # interface IObjectSafety
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IObjectSafety = MIDL_INTERFACE(
                        "{CB5BDC81-93C1-11CF-8F20-00805F2CD064}"
                    )
                    IObjectSafety._iid_ = IID_IObjectSafety

                    IObjectSafety._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetInterfaceSafetyOptions')],
                            HRESULT,
                            'GetInterfaceSafetyOptions',
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(DWORD), 'pdwSupportedOptions'),
                            (['out'], POINTER(DWORD), 'pdwEnabledOptions'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetInterfaceSafetyOptions')],
                            HRESULT,
                            'SetInterfaceSafetyOptions',
                            (['in'], REFIID, 'riid'),
                            (['in'], DWORD, 'dwOptionSetMask'),
                            (['in'], DWORD, 'dwEnabledOptions'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IObjectSafety_INTERFACE_DEFINED__

            # interface __MIDL_itf_objsafe_0000_0001
            # [local]
            # [unique]
            LPOBJECTSAFETY = POINTER(IObjectSafety)
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


