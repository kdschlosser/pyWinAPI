import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

COMMETHOD = comtypes.COMMETHOD


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__mfmediacapture_h__ = None
__IAdvancedMediaCaptureInitializationSettings_FWD_DEFINED__ = None
__IAdvancedMediaCaptureSettings_FWD_DEFINED__ = None
__IAdvancedMediaCapture_FWD_DEFINED__ = None
__IAdvancedMediaCaptureInitializationSettings_INTERFACE_DEFINED__ = None
__IAdvancedMediaCaptureSettings_INTERFACE_DEFINED__ = None
__IAdvancedMediaCapture_INTERFACE_DEFINED__ = None


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

if not defined(__mfmediacapture_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IAdvancedMediaCaptureInitializationSettings_FWD_DEFINED__):
        class IAdvancedMediaCaptureInitializationSettings(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IAdvancedMediaCaptureInitializationSettings_FWD_DEFINED__

    if not defined(__IAdvancedMediaCaptureSettings_FWD_DEFINED__):
        class IAdvancedMediaCaptureSettings(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAdvancedMediaCaptureSettings_FWD_DEFINED__

    if not defined(__IAdvancedMediaCapture_FWD_DEFINED__):
        class IAdvancedMediaCapture(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAdvancedMediaCapture_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.mfobjects_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfmediacapture_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if NTDDI_VERSION >= NTDDI_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IAdvancedMediaCaptureInitializationSettings_INTERFACE_DEFINED__):
                # interface IAdvancedMediaCaptureInitializationSettings
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAdvancedMediaCaptureInitializationSettings = MIDL_INTERFACE(
                        "{3DE21209-8BA6-4F2A-A577-2819B56FF14D}"
                    )
                    IAdvancedMediaCaptureInitializationSettings._iid_ = IID_IAdvancedMediaCaptureInitializationSettings

                    IAdvancedMediaCaptureInitializationSettings._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetDirectxDeviceManager')],
                            HRESULT,
                            'SetDirectxDeviceManager',
                            (['in'], POINTER(IMFDXGIDeviceManager), 'value'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAdvancedMediaCaptureInitializationSettings_INTERFACE_DEFINED__

            if not defined(__IAdvancedMediaCaptureSettings_INTERFACE_DEFINED__):
                # interface IAdvancedMediaCaptureSettings
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAdvancedMediaCaptureSettings = MIDL_INTERFACE(
                        "{24E0485F-A33E-4AA1-B564-6019B1D14F65}"
                    )
                    IAdvancedMediaCaptureSettings._iid_ = IID_IAdvancedMediaCaptureSettings

                    IAdvancedMediaCaptureSettings._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDirectxDeviceManager')],
                            HRESULT,
                            'GetDirectxDeviceManager',
                            (
                                ['out'],
                                POINTER(POINTER(IMFDXGIDeviceManager)),
                                'value'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAdvancedMediaCaptureSettings_INTERFACE_DEFINED__

            if not defined(__IAdvancedMediaCapture_INTERFACE_DEFINED__):
                # interface IAdvancedMediaCapture
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAdvancedMediaCapture = MIDL_INTERFACE(
                        "{D0751585-D216-4344-B5BF-463B68F977BB}"
                    )
                    IAdvancedMediaCapture._iid_ = IID_IAdvancedMediaCapture

                    IAdvancedMediaCapture._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetAdvancedMediaCaptureSettings')],
                            HRESULT,
                            'GetAdvancedMediaCaptureSettings',
                            (
                                ['out'],
                                POINTER(POINTER(IAdvancedMediaCaptureSettings)),
                                'value'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAdvancedMediaCapture_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediacapture_0000_0003
            # [local]
        # END IF   (WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (NTDDI >= NTDDI_WIN8)
    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


