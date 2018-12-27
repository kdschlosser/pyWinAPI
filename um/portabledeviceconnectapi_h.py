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
__PortableDeviceConnectApi_h__ = None
__IEnumPortableDeviceConnectors_FWD_DEFINED__ = None
__IPortableDeviceConnector_FWD_DEFINED__ = None
__IConnectionRequestCallback_FWD_DEFINED__ = None
__EnumBthMtpConnectors_FWD_DEFINED__ = None
__IEnumPortableDeviceConnectors_INTERFACE_DEFINED__ = None
__IPortableDeviceConnector_INTERFACE_DEFINED__ = None
__IConnectionRequestCallback_INTERFACE_DEFINED__ = None
__PortableDeviceConnectApiLib_LIBRARY_DEFINED__ = None


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


if not defined(__PortableDeviceConnectApi_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IEnumPortableDeviceConnectors_FWD_DEFINED__):

        class IEnumPortableDeviceConnectors(comtypes.IUnknown):
            """
            IEnumPortableDeviceConnectors Interface
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IEnumPortableDeviceConnectors_FWD_DEFINED__

    if not defined(__IPortableDeviceConnector_FWD_DEFINED__):
        class IPortableDeviceConnector(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceConnector_FWD_DEFINED__

    if not defined(__IConnectionRequestCallback_FWD_DEFINED__):
        class IConnectionRequestCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IConnectionRequestCallback_FWD_DEFINED__

    if not defined(__EnumBthMtpConnectors_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            pass
        # END IF  __cplusplus
    # END IF  __EnumBthMtpConnectors_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.propsys_h import * # NOQA

    from pyWinAPI.um.portabledeviceconnectimports_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_PortableDeviceConnectApi_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Property set by the MTP Bluetooth Enumerator indicate whether the
        # device is connected
        # {EA1237FA-589D-4472-84E4-0ABE36FD62EF}.2

        DEVPKEY_MTPBTH_IsConnected = DEFINE_DEVPROPKEY(
            0xEA1237FA,
            0x589D,
            0x4472,
            0x84,
            0xE4,
            0x0A,
            0xBE,
            0x36,
            0xFD,
            0x62,
            0x2,
            2
        )

        if not defined(__IEnumPortableDeviceConnectors_INTERFACE_DEFINED__):
            # interface IEnumPortableDeviceConnectors
            # [unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumPortableDeviceConnectors = MIDL_INTERFACE(
                    "{BFDEF549-9247-454F-BD82-06FE80853FAA}"
                )
                IEnumPortableDeviceConnectors._iid_ = IID_IEnumPortableDeviceConnectors

                IEnumPortableDeviceConnectors._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next')],
                        HRESULT,
                        'Next',
                        (['in'], UINT32, 'cRequested'),
                        (
                            ['out'],
                            POINTER(POINTER(IPortableDeviceConnector)),
                           'pConnectors'
                        ),
                        (
                            ['unique', 'out', 'in'],
                            POINTER(UINT32),
                           'pcFetched'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Skip')],
                        HRESULT,
                        'Skip',
                        (['in'], UINT32, 'cConnectors'),
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
                        (
                            ['out'],
                            POINTER(POINTER(IEnumPortableDeviceConnectors)),
                           'ppEnum'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumPortableDeviceConnectors_INTERFACE_DEFINED__

        if not defined(__IPortableDeviceConnector_INTERFACE_DEFINED__):
            # interface IPortableDeviceConnector
            # [unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPortableDeviceConnector = MIDL_INTERFACE(
                    "{625E2DF8-6392-4CF0-9AD1-3CFA5F17775C}"
                )
                IPortableDeviceConnector._iid_ = IID_IPortableDeviceConnector

                IPortableDeviceConnector._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Connect')],
                        HRESULT,
                        'Connect',
                        (
                            ['in'],
                            POINTER(IConnectionRequestCallback),
                           'pCallback'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Disconnect')],
                        HRESULT,
                        'Disconnect',
                        (
                            ['in'],
                            POINTER(IConnectionRequestCallback),
                           'pCallback'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Cancel')],
                        HRESULT,
                        'Cancel',
                        (
                            ['in'],
                            POINTER(IConnectionRequestCallback),
                           'pCallback'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProperty')],
                        HRESULT,
                        'GetProperty',
                        (['in'], POINTER(DEVPROPKEY), 'pPropertyKey'),
                        (['out'], POINTER(DEVPROPTYPE), 'pPropertyType'),
                        (['out'], POINTER(POINTER(BYTE)), 'ppData'),
                        (['out'], POINTER(UINT32), 'pcbData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetProperty')],
                        HRESULT,
                        'SetProperty',
                        (['in'], POINTER(DEVPROPKEY), 'pPropertyKey'),
                        (['in'], DEVPROPTYPE, 'PropertyType'),
                        (['in'], POINTER(BYTE), 'pData'),
                        (['in'], UINT32, 'cbData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPnPID')],
                        HRESULT,
                        'GetPnPID',
                        (['out'], POINTER(LPWSTR), 'ppwszPnPID'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPortableDeviceConnector_INTERFACE_DEFINED__

        if not defined(__IConnectionRequestCallback_INTERFACE_DEFINED__):
            # interface IConnectionRequestCallback
            # [unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IConnectionRequestCallback = MIDL_INTERFACE(
                    "{272C9AE0-7161-4AE0-91BD-9F448EE9C427}"
                )
                IConnectionRequestCallback._iid_ = IID_IConnectionRequestCallback

                IConnectionRequestCallback._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnComplete')],
                        HRESULT,
                        'OnComplete',
                        (['in'], HRESULT, 'hrStatus'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IConnectionRequestCallback_INTERFACE_DEFINED__

        if not defined(__PortableDeviceConnectApiLib_LIBRARY_DEFINED__):
            # library PortableDeviceConnectApiLib
            # [helpstring][version][uuid]
            if defined(__cplusplus):
                pass
            # END IF

        # END IF  __PortableDeviceConnectApiLib_LIBRARY_DEFINED__

        # interface __MIDL_itf_PortableDeviceConnectApi_0000_0004
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


