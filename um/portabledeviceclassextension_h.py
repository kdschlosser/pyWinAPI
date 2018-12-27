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
__PortableDeviceClassExtension_h__ = None
__IPortableDeviceClassExtension_FWD_DEFINED__ = None
__PortableDeviceClassExtension_FWD_DEFINED__ = None
__IPortableDeviceClassExtension_INTERFACE_DEFINED__ = None
__PortableDeviceClassExtension_LIBRARY_DEFINED__ = None


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


if not defined(__PortableDeviceClassExtension_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IPortableDeviceClassExtension_FWD_DEFINED__):

        class IPortableDeviceClassExtension(comtypes.IUnknown):
            """
            IPortableDeviceDriverLibrary Interface
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPortableDeviceClassExtension

    # END IF  __IPortableDeviceClassExtension_FWD_DEFINED__

    if not defined(__PortableDeviceClassExtension_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            LIBID_PortableDeviceClassExtension = IID(
                '{c0ffa723-ff4c-4983-8565-66d78e73036e}'
            )

            CLSID_PortableDeviceClassExtension = DECLSPEC_UUID(
                '{4cadfae1-5512-456a-9d65-5b5e7e9ca9a3}'
            )

            class PortableDeviceClassExtension(comtypes.CoClass):
                """
                PortableDeviceClassExtension Class
                """
                _reg_clsid_ = CLSID_PortableDeviceClassExtension
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceClassExtension, 1, 0)
                _com_interfaces_ = [IPortableDeviceClassExtension]

        # END IF  __cplusplus
    # END IF  __PortableDeviceClassExtension_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.oaidl_h import * # NOQA
    from pyWinAPI.um.ocidl_h import * # NOQA
    from pyWinAPI.um.propidl_h import * # NOQA
    from pyWinAPI.um.portabledevicetypes_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_PortableDeviceClassExtension_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if _WIN32_WINNT >= 0x0501:
            if not defined(__IPortableDeviceClassExtension_INTERFACE_DEFINED__):
                # interface IPortableDeviceClassExtension
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceClassExtension = MIDL_INTERFACE(
                        "{BC08386A-9952-40CD-BA50-9541D64A4B4E}"
                    )
                    IPortableDeviceClassExtension._iid_ = IID_IPortableDeviceClassExtension

                    IPortableDeviceClassExtension._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Initialize')],
                            HRESULT,
                            'Initialize',
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                               'pWdfDeviceUnknown'
                            ),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pOptions'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Uninitialize')],
                            HRESULT,
                            'Uninitialize',
                        ),
                        COMMETHOD(
                            [helpstring('Method ProcessLibraryMessage')],
                            HRESULT,
                            'ProcessLibraryMessage',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pParams'
                            ),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pResults'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceClassExtension_INTERFACE_DEFINED__

            if not defined(__PortableDeviceClassExtension_LIBRARY_DEFINED__):
                # library PortableDeviceClassExtension
                # [helpstring][version][uuid]
                if defined(__cplusplus):
                    pass

                class PortableDeviceClassExtension(object):
                    """
                    PortableDeviceClassExtension 1.0 Type Library
                    """
                    name = 'PortableDeviceClassExtension'
                    _reg_typelib_ = (LIBID_PortableDeviceClassExtension, 1, 0)

                # END IF

            # END IF  __PortableDeviceClassExtension_LIBRARY_DEFINED__

            # interface __MIDL_itf_PortableDeviceClassExtension_0000_0002
            # [local]
        # END IF   (_WIN32_WINNT >= 0x0501)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


