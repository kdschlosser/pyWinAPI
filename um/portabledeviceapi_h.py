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
__PortableDeviceApi_h__ = None
__IPortableDeviceManager_FWD_DEFINED__ = None
__IPortableDevice_FWD_DEFINED__ = None
__IPortableDeviceContent_FWD_DEFINED__ = None
__IPortableDeviceContent2_FWD_DEFINED__ = None
__IEnumPortableDeviceObjectIDs_FWD_DEFINED__ = None
__IPortableDeviceProperties_FWD_DEFINED__ = None
__IPortableDeviceResources_FWD_DEFINED__ = None
__IPortableDeviceCapabilities_FWD_DEFINED__ = None
__IPortableDeviceEventCallback_FWD_DEFINED__ = None
__IPortableDeviceDataStream_FWD_DEFINED__ = None
__IPortableDeviceUnitsStream_FWD_DEFINED__ = None
__IPortableDevicePropertiesBulk_FWD_DEFINED__ = None
__IPortableDevicePropertiesBulkCallback_FWD_DEFINED__ = None
__IPortableDeviceServiceManager_FWD_DEFINED__ = None
__IPortableDeviceService_FWD_DEFINED__ = None
__IPortableDeviceServiceCapabilities_FWD_DEFINED__ = None
__IPortableDeviceServiceMethods_FWD_DEFINED__ = None
__IPortableDeviceServiceMethodCallback_FWD_DEFINED__ = None
__IPortableDeviceServiceActivation_FWD_DEFINED__ = None
__IPortableDeviceServiceOpenCallback_FWD_DEFINED__ = None
__IPortableDeviceDispatchFactory_FWD_DEFINED__ = None
__IPortableDeviceWebControl_FWD_DEFINED__ = None
__PortableDevice_FWD_DEFINED__ = None
__PortableDeviceManager_FWD_DEFINED__ = None
__PortableDeviceService_FWD_DEFINED__ = None
__PortableDeviceDispatchFactory_FWD_DEFINED__ = None
__PortableDeviceFTM_FWD_DEFINED__ = None
__PortableDeviceServiceFTM_FWD_DEFINED__ = None
__PortableDeviceWebControl_FWD_DEFINED__ = None
__IPortableDeviceManager_INTERFACE_DEFINED__ = None
__IPortableDevice_INTERFACE_DEFINED__ = None
__IPortableDeviceContent_INTERFACE_DEFINED__ = None
__IPortableDeviceContent2_INTERFACE_DEFINED__ = None
__IEnumPortableDeviceObjectIDs_INTERFACE_DEFINED__ = None
__IPortableDeviceProperties_INTERFACE_DEFINED__ = None
__IPortableDeviceResources_INTERFACE_DEFINED__ = None
__IPortableDeviceCapabilities_INTERFACE_DEFINED__ = None
__IPortableDeviceEventCallback_INTERFACE_DEFINED__ = None
__IPortableDeviceDataStream_INTERFACE_DEFINED__ = None
__IPortableDeviceUnitsStream_INTERFACE_DEFINED__ = None
__IPortableDevicePropertiesBulk_INTERFACE_DEFINED__ = None
__IPortableDevicePropertiesBulkCallback_INTERFACE_DEFINED__ = None
__IPortableDeviceServiceManager_INTERFACE_DEFINED__ = None
__IPortableDeviceService_INTERFACE_DEFINED__ = None
__IPortableDeviceServiceCapabilities_INTERFACE_DEFINED__ = None
__IPortableDeviceServiceMethods_INTERFACE_DEFINED__ = None
__IPortableDeviceServiceMethodCallback_INTERFACE_DEFINED__ = None
__IPortableDeviceServiceActivation_INTERFACE_DEFINED__ = None
__IPortableDeviceServiceOpenCallback_INTERFACE_DEFINED__ = None
__IPortableDeviceDispatchFactory_INTERFACE_DEFINED__ = None
__IPortableDeviceWebControl_INTERFACE_DEFINED__ = None
__PortableDeviceApiLib_LIBRARY_DEFINED__ = None


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


if not defined(__PortableDeviceApi_h__):

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IPortableDeviceManager_FWD_DEFINED__):

        class IPortableDeviceManager(comtypes.IUnknown):
            """
            IPortableDeviceManager Interface
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IPortableDeviceManager_FWD_DEFINED__

    if not defined(__IPortableDevice_FWD_DEFINED__):
        class IPortableDevice(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDevice_FWD_DEFINED__

    if not defined(__IPortableDeviceContent_FWD_DEFINED__):
        class IPortableDeviceContent(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceContent_FWD_DEFINED__

    if not defined(__IPortableDeviceContent2_FWD_DEFINED__):
        class IPortableDeviceContent2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceContent2_FWD_DEFINED__

    if not defined(__IEnumPortableDeviceObjectIDs_FWD_DEFINED__):
        class IEnumPortableDeviceObjectIDs(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumPortableDeviceObjectIDs_FWD_DEFINED__

    if not defined(__IPortableDeviceProperties_FWD_DEFINED__):
        class IPortableDeviceProperties(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceProperties_FWD_DEFINED__

    if not defined(__IPortableDeviceResources_FWD_DEFINED__):
        class IPortableDeviceResources(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceResources_FWD_DEFINED__

    if not defined(__IPortableDeviceCapabilities_FWD_DEFINED__):
        class IPortableDeviceCapabilities(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceCapabilities_FWD_DEFINED__

    if not defined(__IPortableDeviceEventCallback_FWD_DEFINED__):
        class IPortableDeviceEventCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceEventCallback_FWD_DEFINED__

    if not defined(__IPortableDeviceDataStream_FWD_DEFINED__):
        class IPortableDeviceDataStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceDataStream_FWD_DEFINED__

    if not defined(__IPortableDeviceUnitsStream_FWD_DEFINED__):
        class IPortableDeviceUnitsStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceUnitsStream_FWD_DEFINED__

    if not defined(__IPortableDevicePropertiesBulk_FWD_DEFINED__):
        class IPortableDevicePropertiesBulk(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDevicePropertiesBulk_FWD_DEFINED__

    if not defined(__IPortableDevicePropertiesBulkCallback_FWD_DEFINED__):
        class IPortableDevicePropertiesBulkCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDevicePropertiesBulkCallback_FWD_DEFINED__

    if not defined(__IPortableDeviceServiceManager_FWD_DEFINED__):
        class IPortableDeviceServiceManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceServiceManager_FWD_DEFINED__

    if not defined(__IPortableDeviceService_FWD_DEFINED__):
        class IPortableDeviceService(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceService_FWD_DEFINED__

    if not defined(__IPortableDeviceServiceCapabilities_FWD_DEFINED__):
        class IPortableDeviceServiceCapabilities(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceServiceCapabilities_FWD_DEFINED__

    if not defined(__IPortableDeviceServiceMethods_FWD_DEFINED__):
        class IPortableDeviceServiceMethods(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceServiceMethods_FWD_DEFINED__

    if not defined(__IPortableDeviceServiceMethodCallback_FWD_DEFINED__):
        class IPortableDeviceServiceMethodCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceServiceMethodCallback_FWD_DEFINED__

    if not defined(__IPortableDeviceServiceActivation_FWD_DEFINED__):
        class IPortableDeviceServiceActivation(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceServiceActivation_FWD_DEFINED__

    if not defined(__IPortableDeviceServiceOpenCallback_FWD_DEFINED__):
        class IPortableDeviceServiceOpenCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceServiceOpenCallback_FWD_DEFINED__

    if not defined(__IPortableDeviceDispatchFactory_FWD_DEFINED__):
        class IPortableDeviceDispatchFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceDispatchFactory_FWD_DEFINED__

    if not defined(__IPortableDeviceWebControl_FWD_DEFINED__):
        class IPortableDeviceWebControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPortableDeviceWebControl_FWD_DEFINED__

    if not defined(__PortableDevice_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            LIBID_PortableDeviceApiLib = IID(
                '{c0ffa723-ff4c-4983-8565-66d78e73036e}'
            )

            CLSID_PortableDevice = DECLSPEC_UUID(
                '{728a21c5-3d9e-48d7-9810-864848f0f404}'
            )


            class PortableDevice(comtypes.CoClass):
                """
                PortableDevice Class
                """
                _reg_clsid_ = CLSID_PortableDevice
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)
                _com_interfaces_ = [IPortableDevice]

        # END IF  __cplusplus
    # END IF  __PortableDevice_FWD_DEFINED__

    if not defined(__PortableDeviceManager_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceManager = DECLSPEC_UUID(
                '{0af10cec-2ecd-4b92-9581-34f6ae0637f3}'
            )


            class PortableDeviceManager(comtypes.CoClass):
                """
                PortableDeviceManager Class
                """
                _reg_clsid_ = CLSID_PortableDeviceManager
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)
                _com_interfaces_ = [IPortableDeviceManager]

        # END IF  __cplusplus
    # END IF  __PortableDeviceManager_FWD_DEFINED__

    if not defined(__PortableDeviceService_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceService = DECLSPEC_UUID(
                '{ef5db4c2-9312-422c-9152-411cd9c4dd84}'
            )


            class PortableDeviceService(comtypes.CoClass):
                """
                PortableDeviceService Class
                """
                _reg_clsid_ = CLSID_PortableDeviceService
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)
                _com_interfaces_ = [IPortableDeviceService]

        # END IF  __cplusplus
    # END IF  __PortableDeviceService_FWD_DEFINED__

    if not defined(__PortableDeviceDispatchFactory_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceDispatchFactory = DECLSPEC_UUID(
                '{43232233-8338-4658-ae01-0b4ae830b6b0}'
            )


            class PortableDeviceDispatchFactory(comtypes.CoClass):
                """
                PortableDeviceDispatchFactory Class
                """
                _reg_clsid_ = CLSID_PortableDeviceDispatchFactory
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)
                _com_interfaces_ = [IPortableDeviceDispatchFactory]

        # END IF  __cplusplus
    # END IF  __PortableDeviceDispatchFactory_FWD_DEFINED__

    if not defined(__PortableDeviceFTM_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceFTM = DECLSPEC_UUID(
                '{f7c0039a-4762-488a-b4b3-760ef9a1ba9b}'
            )


            class PortableDeviceFTM(comtypes.CoClass):
                """
                PortableDeviceFTM Class
                """
                _reg_clsid_ = CLSID_PortableDeviceFTM
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)
                _com_interfaces_ = [IPortableDevice]
        # END IF  __cplusplus
    # END IF  __PortableDeviceFTM_FWD_DEFINED__

    if not defined(__PortableDeviceServiceFTM_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceServiceFTM = DECLSPEC_UUID(
                '{1649b154-c794-497a-9b03-f3f0121302f3}'
            )


            class PortableDeviceServiceFTM(comtypes.CoClass):
                """
                PortableDeviceServiceFTM Class
                """
                _reg_clsid_ = CLSID_PortableDeviceServiceFTM
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)
                _com_interfaces_ = [IPortableDeviceService]

        # END IF  __cplusplus
    # END IF  __PortableDeviceServiceFTM_FWD_DEFINED__

    if not defined(__PortableDeviceWebControl_FWD_DEFINED__):
        if defined(__cplusplus):
            pass
        else:
            CLSID_PortableDeviceWebControl = DECLSPEC_UUID(
                '{186dd02c-2dec-41b5-a7d4-b59056fade51}'
            )


            class PortableDeviceServiceFTM(comtypes.CoClass):
                """
                Dispatch Class for Web Host Applications
                """
                _reg_clsid_ = CLSID_PortableDeviceWebControl
                _idlflags_ = []
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)
                _com_interfaces_ = [IPortableDeviceWebControl]

        # END IF  __cplusplus
    # END IF  __PortableDeviceWebControl_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.propidl_h import * # NOQA
    from pyWinAPI.um.portabledevicetypes_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_PortableDeviceApi_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if _WIN32_WINNT >= 0x0501:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IPortableDeviceManager_INTERFACE_DEFINED__):
                # interface IPortableDeviceManager
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceManager = MIDL_INTERFACE(
                        "{A1567595-4C2F-4574-A6FA-ECEF917B9A40}"
                    )
                    IPortableDeviceManager._iid_ = IID_IPortableDeviceManager

                    IPortableDeviceManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDevices')],
                            HRESULT,
                            'GetDevices',
                            (
                                ['unique', 'out', 'in'],
                                POINTER(LPWSTR),
                               'pPnPDeviceIDs'
                            ),
                            (['out', 'in'], POINTER(DWORD), 'pcPnPDeviceIDs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RefreshDeviceList')],
                            HRESULT,
                            'RefreshDeviceList',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceFriendlyName')],
                            HRESULT,
                            'GetDeviceFriendlyName',
                            (['in'], LPCWSTR, 'pszPnPDeviceID'),
                            (
                                ['unique', 'out', 'in'],
                                POINTER(WCHAR),
                               'pDeviceFriendlyName'
                            ),
                            (
                                ['out', 'in'],
                                POINTER(DWORD),
                               'pcchDeviceFriendlyName'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceDescription')],
                            HRESULT,
                            'GetDeviceDescription',
                            (['in'], LPCWSTR, 'pszPnPDeviceID'),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(WCHAR),
                               'pDeviceDescription'
                            ),
                            (
                                ['out', 'in'],
                                POINTER(DWORD),
                               'pcchDeviceDescription'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceManufacturer')],
                            HRESULT,
                            'GetDeviceManufacturer',
                            (['in'], LPCWSTR, 'pszPnPDeviceID'),
                            (
                                ['unique', 'out', 'in'],
                                POINTER(WCHAR),
                               'pDeviceManufacturer'
                            ),
                            (
                                ['out', 'in'],
                                POINTER(DWORD),
                               'pcchDeviceManufacturer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceProperty')],
                            HRESULT,
                            'GetDeviceProperty',
                            (['in'], LPCWSTR, 'pszPnPDeviceID'),
                            (['in'], LPCWSTR, 'pszDevicePropertyName'),
                            (['out', 'in', 'unique'], POINTER(BYTE), 'pData'),
                            (
                                ['unique', 'out', 'in'],
                                POINTER(DWORD),
                               'pcbData'
                            ),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(DWORD),
                               'pdwType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPrivateDevices')],
                            HRESULT,
                            'GetPrivateDevices',
                            (
                                ['out', 'unique', 'in'],
                                POINTER(LPWSTR),
                               'pPnPDeviceIDs'
                            ),
                            (['out', 'in'], POINTER(DWORD), 'pcPnPDeviceIDs'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceManager_INTERFACE_DEFINED__

            if not defined(__IPortableDevice_INTERFACE_DEFINED__):
                # interface IPortableDevice
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDevice = MIDL_INTERFACE(
                        "{625E2DF8-6392-4CF0-9AD1-3CFA5F17775C}"
                    )
                    IPortableDevice._iid_ = IID_IPortableDevice

                    IPortableDevice._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Open')],
                            HRESULT,
                            'Open',
                            (['in'], LPCWSTR, 'pszPnPDeviceID'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pClientInfo'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SendCommand')],
                            HRESULT,
                            'SendCommand',
                            (['in'], DWORD, 'dwFlags'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pParameters'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppResults'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Content')],
                            HRESULT,
                            'Content',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceContent)),
                               'ppContent'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Capabilities')],
                            HRESULT,
                            'Capabilities',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceCapabilities)),
                               'ppCapabilities'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                        COMMETHOD(
                            [helpstring('Method Close')],
                            HRESULT,
                            'Close',
                        ),
                        COMMETHOD(
                            [helpstring('Method Advise')],
                            HRESULT,
                            'Advise',
                            (['in'], DWORD, 'dwFlags'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceEventCallback),
                               'pCallback'
                            ),
                            (
                                ['in', 'unique'],
                                POINTER(IPortableDeviceValues),
                               'pParameters'
                            ),
                            (['out'], POINTER(LPWSTR), 'ppszCookie'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Unadvise')],
                            HRESULT,
                            'Unadvise',
                            (['in'], LPCWSTR, 'pszCookie'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPnPDeviceID')],
                            HRESULT,
                            'GetPnPDeviceID',
                            (['out'], POINTER(LPWSTR), 'ppszPnPDeviceID'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDevice_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceContent_INTERFACE_DEFINED__):
                # interface IPortableDeviceContent
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceContent = MIDL_INTERFACE(
                        "{6A96ED84-7C73-4480-9938-BF5AF477D426}"
                    )
                    IPortableDeviceContent._iid_ = IID_IPortableDeviceContent

                    IPortableDeviceContent._methods_ = [
                        COMMETHOD(
                            [helpstring('Method EnumObjects')],
                            HRESULT,
                            'EnumObjects',
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], LPCWSTR, 'pszParentObjectID'),
                            (
                                ['unique', 'in'],
                                POINTER(IPortableDeviceValues),
                               'pFilter'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IEnumPortableDeviceObjectIDs)),
                               'ppEnum'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Properties')],
                            HRESULT,
                            'Properties',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceProperties)),
                               'ppProperties'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Transfer')],
                            HRESULT,
                            'Transfer',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceResources)),
                               'ppResources'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateObjectWithPropertiesOnly')],
                            HRESULT,
                            'CreateObjectWithPropertiesOnly',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pValues'
                            ),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(LPWSTR),
                               'ppszObjectID'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateObjectWithPropertiesAndData')],
                            HRESULT,
                            'CreateObjectWithPropertiesAndData',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pValues'
                            ),
                            (['out'], POINTER(POINTER(IStream)), 'ppData'),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(DWORD),
                               'pdwOptimalWriteBufferSize'
                            ),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(LPWSTR),
                               'ppszCookie'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Delete')],
                            HRESULT,
                            'Delete',
                            (['in'], DWORD, 'dwOptions'),
                            (
                                ['in'],
                                POINTER(IPortableDevicePropVariantCollection),
                               'pObjectIDs'
                            ),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppResults'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetObjectIDsFromPersistentUniqueIDs')],
                            HRESULT,
                            'GetObjectIDsFromPersistentUniqueIDs',
                            (
                                ['in'],
                                POINTER(IPortableDevicePropVariantCollection),
                               'pPersistentUniqueIDs'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppObjectIDs'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                        COMMETHOD(
                            [helpstring('Method Move')],
                            HRESULT,
                            'Move',
                            (
                                ['in'],
                                POINTER(IPortableDevicePropVariantCollection),
                               'pObjectIDs'
                            ),
                            (['in'], LPCWSTR, 'pszDestinationFolderObjectID'),
                            (
                                ['in', 'unique', 'out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppResults'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Copy')],
                            HRESULT,
                            'Copy',
                            (
                                ['in'],
                                POINTER(IPortableDevicePropVariantCollection),
                               'pObjectIDs'
                            ),
                            (['in'], LPCWSTR, 'pszDestinationFolderObjectID'),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppResults'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceContent_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceContent2_INTERFACE_DEFINED__):
                # interface IPortableDeviceContent2
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceContent2 = MIDL_INTERFACE(
                        "{9B4ADD96-F6BF-4034-8708-ECA72BF10554}"
                    )
                    IPortableDeviceContent2._iid_ = IID_IPortableDeviceContent2

                    IPortableDeviceContent2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method UpdateObjectWithPropertiesAndData')],
                            HRESULT,
                            'UpdateObjectWithPropertiesAndData',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pProperties'
                            ),
                            (['out'], POINTER(POINTER(IStream)), 'ppData'),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(DWORD),
                               'pdwOptimalWriteBufferSize'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceContent2_INTERFACE_DEFINED__

            if not defined(__IEnumPortableDeviceObjectIDs_INTERFACE_DEFINED__):
                # interface IEnumPortableDeviceObjectIDs
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IEnumPortableDeviceObjectIDs = MIDL_INTERFACE(
                        "{10ECE955-CF41-4728-BFA0-41EEDF1BBF19}"
                    )
                    IEnumPortableDeviceObjectIDs._iid_ = IID_IEnumPortableDeviceObjectIDs

                    IEnumPortableDeviceObjectIDs._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Next')],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'cObjects'),
                            (['out'], POINTER(LPWSTR), 'pObjIDs'),
                            (
                                ['out', 'unique', 'in'],
                                POINTER(ULONG),
                               'pcFetched'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Skip')],
                            HRESULT,
                            'Skip',
                            (['in'], ULONG, 'cObjects'),
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
                                POINTER(POINTER(IEnumPortableDeviceObjectIDs)),
                               'ppEnum'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IEnumPortableDeviceObjectIDs_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceProperties_INTERFACE_DEFINED__):
                # interface IPortableDeviceProperties
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceProperties = MIDL_INTERFACE(
                        "{7F6D695C-03DF-4439-A809-59266BEEE3A6}"
                    )
                    IPortableDeviceProperties._iid_ = IID_IPortableDeviceProperties

                    IPortableDeviceProperties._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetSupportedProperties')],
                            HRESULT,
                            'GetSupportedProperties',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceKeyCollection)),
                               'ppKeys'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPropertyAttributes')],
                            HRESULT,
                            'GetPropertyAttributes',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (['in'], REFPROPERTYKEY, 'Key'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetValues')],
                            HRESULT,
                            'GetValues',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (
                                ['unique', 'in'],
                                POINTER(IPortableDeviceKeyCollection),
                               'pKeys'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppValues'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetValues')],
                            HRESULT,
                            'SetValues',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pValues'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppResults'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Delete')],
                            HRESULT,
                            'Delete',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceKeyCollection),
                               'pKeys'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceProperties_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceResources_INTERFACE_DEFINED__):
                # interface IPortableDeviceResources
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceResources = MIDL_INTERFACE(
                        "{FD8878AC-D841-4D17-891C-E6829CDB6934}"
                    )
                    IPortableDeviceResources._iid_ = IID_IPortableDeviceResources

                    IPortableDeviceResources._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetSupportedResources')],
                            HRESULT,
                            'GetSupportedResources',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceKeyCollection)),
                               'ppKeys'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetResourceAttributes')],
                            HRESULT,
                            'GetResourceAttributes',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (['in'], REFPROPERTYKEY, 'Key'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppResourceAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStream')],
                            HRESULT,
                            'GetStream',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (['in'], REFPROPERTYKEY, 'Key'),
                            (['in'], DWORD, 'dwMode'),
                            (
                                ['unique', 'out', 'in'],
                                POINTER(DWORD),
                               'pdwOptimalBufferSize'
                            ),
                            (['out'], POINTER(POINTER(IStream)), 'ppStream'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Delete')],
                            HRESULT,
                            'Delete',
                            (['in'], LPCWSTR, 'pszObjectID'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceKeyCollection),
                               'pKeys'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateResource')],
                            HRESULT,
                            'CreateResource',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pResourceAttributes'
                            ),
                            (['out'], POINTER(POINTER(IStream)), 'ppData'),
                            (
                                ['unique', 'in', 'out'],
                                POINTER(DWORD),
                               'pdwOptimalWriteBufferSize'
                            ),
                            (
                                ['unique', 'out', 'in'],
                                POINTER(LPWSTR),
                               'ppszCookie'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceResources_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceCapabilities_INTERFACE_DEFINED__):
                # interface IPortableDeviceCapabilities
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceCapabilities = MIDL_INTERFACE(
                        "{2C8C6DBF-E3DC-4061-BECC-8542E810D126}"
                    )
                    IPortableDeviceCapabilities._iid_ = IID_IPortableDeviceCapabilities

                    IPortableDeviceCapabilities._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetSupportedCommands')],
                            HRESULT,
                            'GetSupportedCommands',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceKeyCollection)),
                               'ppCommands'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCommandOptions')],
                            HRESULT,
                            'GetCommandOptions',
                            (['in'], REFPROPERTYKEY, 'Command'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppOptions'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFunctionalCategories')],
                            HRESULT,
                            'GetFunctionalCategories',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppCategories'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFunctionalObjects')],
                            HRESULT,
                            'GetFunctionalObjects',
                            (['in'], REFGUID, 'Category'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppObjectIDs'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedContentTypes')],
                            HRESULT,
                            'GetSupportedContentTypes',
                            (['in'], REFGUID, 'Category'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppContentTypes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedFormats')],
                            HRESULT,
                            'GetSupportedFormats',
                            (['in'], REFGUID, 'ContentType'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppFormats'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedFormatProperties')],
                            HRESULT,
                            'GetSupportedFormatProperties',
                            (['in'], REFGUID, 'Format'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceKeyCollection)),
                               'ppKeys'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFixedPropertyAttributes')],
                            HRESULT,
                            'GetFixedPropertyAttributes',
                            (['in'], REFGUID, 'Format'),
                            (['in'], REFPROPERTYKEY, 'Key'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedEvents')],
                            HRESULT,
                            'GetSupportedEvents',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppEvents'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetEventOptions')],
                            HRESULT,
                            'GetEventOptions',
                            (['in'], REFGUID, 'Event'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppOptions'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceCapabilities_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceEventCallback_INTERFACE_DEFINED__):
                # interface IPortableDeviceEventCallback
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceEventCallback = MIDL_INTERFACE(
                        "{A8792A31-F385-493C-A893-40F64EB45F6E}"
                    )
                    IPortableDeviceEventCallback._iid_ = IID_IPortableDeviceEventCallback

                    IPortableDeviceEventCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnEvent')],
                            HRESULT,
                            'OnEvent',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pEventParameters'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceEventCallback_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceDataStream_INTERFACE_DEFINED__):
                # interface IPortableDeviceDataStream
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceDataStream = MIDL_INTERFACE(
                        "{88E04DB3-1012-4D64-9996-F703A950D3F4}"
                    )
                    IPortableDeviceDataStream._iid_ = IID_IPortableDeviceDataStream

                    IPortableDeviceDataStream._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetObjectID')],
                            HRESULT,
                            'GetObjectID',
                            (['out'], POINTER(LPWSTR), 'ppszObjectID'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceDataStream_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceUnitsStream_INTERFACE_DEFINED__):
                # interface IPortableDeviceUnitsStream
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceUnitsStream = MIDL_INTERFACE(
                        "{5E98025F-BFC4-47A2-9A5F-BC900A507C67}"
                    )
                    IPortableDeviceUnitsStream._iid_ = IID_IPortableDeviceUnitsStream

                    IPortableDeviceUnitsStream._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SeekInUnits'), 'local'],
                            HRESULT,
                            'SeekInUnits',
                            (['in'], LARGE_INTEGER, 'dlibMove'),
                            (['in'], WPD_STREAM_UNITS, 'units'),
                            (['in'], DWORD, 'dwOrigin'),
                            (
                                ['out'],
                                POINTER(ULARGE_INTEGER),
                               'plibNewPosition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceUnitsStream_INTERFACE_DEFINED__

            if not defined(__IPortableDevicePropertiesBulk_INTERFACE_DEFINED__):
                # interface IPortableDevicePropertiesBulk
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDevicePropertiesBulk = MIDL_INTERFACE(
                        "{482B05C0-4056-44ED-9E0F-5E23B009DA93}"
                    )
                    IPortableDevicePropertiesBulk._iid_ = IID_IPortableDevicePropertiesBulk

                    IPortableDevicePropertiesBulk._methods_ = [
                        COMMETHOD(
                            [helpstring('Method QueueGetValuesByObjectList')],
                            HRESULT,
                            'QueueGetValuesByObjectList',
                            (
                                ['in'],
                                POINTER(IPortableDevicePropVariantCollection),
                               'pObjectIDs'
                            ),
                            (
                                ['in'],
                                POINTER(IPortableDeviceKeyCollection),
                               'pKeys'
                            ),
                            (
                                ['in'],
                                POINTER(IPortableDevicePropertiesBulkCallback),
                               'pCallback'
                            ),
                            (['out'], POINTER(GUID), 'pContext'),
                        ),
                        COMMETHOD(
                            [helpstring('Method QueueGetValuesByObjectFormat')],
                            HRESULT,
                            'QueueGetValuesByObjectFormat',
                            (['in'], REFGUID, 'pguidObjectFormat'),
                            (['in'], LPCWSTR, 'pszParentObjectID'),
                            (['in'], DWORD, 'dwDepth'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceKeyCollection),
                               'pKeys'
                            ),
                            (
                                ['in'],
                                POINTER(IPortableDevicePropertiesBulkCallback),
                               'pCallback'
                            ),
                            (['out'], POINTER(GUID), 'pContext'),
                        ),
                        COMMETHOD(
                            [helpstring('Method QueueSetValuesByObjectList')],
                            HRESULT,
                            'QueueSetValuesByObjectList',
                            (
                                ['in'],
                                POINTER(IPortableDeviceValuesCollection),
                               'pObjectValues'
                            ),
                            (
                                ['in'],
                                POINTER(IPortableDevicePropertiesBulkCallback),
                               'pCallback'
                            ),
                            (['out'], POINTER(GUID), 'pContext'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Start')],
                            HRESULT,
                            'Start',
                            (['in'], REFGUID, 'pContext'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                            (['in'], REFGUID, 'pContext'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDevicePropertiesBulk_INTERFACE_DEFINED__

            if not defined(__IPortableDevicePropertiesBulkCallback_INTERFACE_DEFINED__):
                # interface IPortableDevicePropertiesBulkCallback
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDevicePropertiesBulkCallback = MIDL_INTERFACE(
                        "{9DEACB80-11E8-40E3-A9F3-F557986A7845}"
                    )
                    IPortableDevicePropertiesBulkCallback._iid_ = IID_IPortableDevicePropertiesBulkCallback

                    IPortableDevicePropertiesBulkCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnStart')],
                            HRESULT,
                            'OnStart',
                            (['in'], REFGUID, 'pContext'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnProgress')],
                            HRESULT,
                            'OnProgress',
                            (['in'], REFGUID, 'pContext'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValuesCollection),
                               'pResults'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnEnd')],
                            HRESULT,
                            'OnEnd',
                            (['in'], REFGUID, 'pContext'),
                            (['in'], HRESULT, 'hrStatus'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDevicePropertiesBulkCallback_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceServiceManager_INTERFACE_DEFINED__):
                # interface IPortableDeviceServiceManager
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceServiceManager = MIDL_INTERFACE(
                        "{A8ABC4E9-A84A-47A9-80B3-C5D9B172A961}"
                    )
                    IPortableDeviceServiceManager._iid_ = IID_IPortableDeviceServiceManager

                    IPortableDeviceServiceManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDeviceServices')],
                            HRESULT,
                            'GetDeviceServices',
                            (['in'], LPCWSTR, 'pszPnPDeviceID'),
                            (['in'], REFGUID, 'guidServiceCategory'),
                            (
                                ['in', 'out', 'unique'],
                                POINTER(LPWSTR),
                               'pServices'
                            ),
                            (['out', 'in'], POINTER(DWORD), 'pcServices'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceForService')],
                            HRESULT,
                            'GetDeviceForService',
                            (['in'], LPCWSTR, 'pszPnPServiceID'),
                            (['out'], POINTER(LPWSTR), 'ppszPnPDeviceID'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceServiceManager_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceService_INTERFACE_DEFINED__):
                # interface IPortableDeviceService
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceService = MIDL_INTERFACE(
                        "{D3BD3A44-D7B5-40A9-98B7-2FA4D01DEC08}"
                    )
                    IPortableDeviceService._iid_ = IID_IPortableDeviceService

                    IPortableDeviceService._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Open')],
                            HRESULT,
                            'Open',
                            (['in'], LPCWSTR, 'pszPnPServiceID'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pClientInfo'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Capabilities')],
                            HRESULT,
                            'Capabilities',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceServiceCapabilities)),
                               'ppCapabilities'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Content')],
                            HRESULT,
                            'Content',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceContent2)),
                               'ppContent'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Methods')],
                            HRESULT,
                            'Methods',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceServiceMethods)),
                               'ppMethods'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                        COMMETHOD(
                            [helpstring('Method Close')],
                            HRESULT,
                            'Close',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetServiceObjectID')],
                            HRESULT,
                            'GetServiceObjectID',
                            (['out'], POINTER(LPWSTR), 'ppszServiceObjectID'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPnPServiceID')],
                            HRESULT,
                            'GetPnPServiceID',
                            (['out'], POINTER(LPWSTR), 'ppszPnPServiceID'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Advise')],
                            HRESULT,
                            'Advise',
                            (['in'], DWORD, 'dwFlags'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceEventCallback),
                               'pCallback'
                            ),
                            (
                                ['unique', 'in'],
                                POINTER(IPortableDeviceValues),
                               'pParameters'
                            ),
                            (['out'], POINTER(LPWSTR), 'ppszCookie'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Unadvise')],
                            HRESULT,
                            'Unadvise',
                            (['in'], LPCWSTR, 'pszCookie'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SendCommand')],
                            HRESULT,
                            'SendCommand',
                            (['in'], DWORD, 'dwFlags'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pParameters'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppResults'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceService_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceServiceCapabilities_INTERFACE_DEFINED__):
                # interface IPortableDeviceServiceCapabilities
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceServiceCapabilities = MIDL_INTERFACE(
                        "{24DBD89D-413E-43E0-BD5B-197F3C56C886}"
                    )
                    IPortableDeviceServiceCapabilities._iid_ = IID_IPortableDeviceServiceCapabilities

                    IPortableDeviceServiceCapabilities._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetSupportedMethods')],
                            HRESULT,
                            'GetSupportedMethods',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppMethods'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedMethodsByFormat')],
                            HRESULT,
                            'GetSupportedMethodsByFormat',
                            (['in'], REFGUID, 'Format'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppMethods'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMethodAttributes')],
                            HRESULT,
                            'GetMethodAttributes',
                            (['in'], REFGUID, 'Method'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMethodParameterAttributes')],
                            HRESULT,
                            'GetMethodParameterAttributes',
                            (['in'], REFGUID, 'Method'),
                            (['in'], REFPROPERTYKEY, 'Parameter'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedFormats')],
                            HRESULT,
                            'GetSupportedFormats',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppFormats'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFormatAttributes')],
                            HRESULT,
                            'GetFormatAttributes',
                            (['in'], REFGUID, 'Format'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedFormatProperties')],
                            HRESULT,
                            'GetSupportedFormatProperties',
                            (['in'], REFGUID, 'Format'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceKeyCollection)),
                               'ppKeys'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFormatPropertyAttributes')],
                            HRESULT,
                            'GetFormatPropertyAttributes',
                            (['in'], REFGUID, 'Format'),
                            (['in'], REFPROPERTYKEY, 'Property'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedEvents')],
                            HRESULT,
                            'GetSupportedEvents',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppEvents'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetEventAttributes')],
                            HRESULT,
                            'GetEventAttributes',
                            (['in'], REFGUID, 'Event'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetEventParameterAttributes')],
                            HRESULT,
                            'GetEventParameterAttributes',
                            (['in'], REFGUID, 'Event'),
                            (['in'], REFPROPERTYKEY, 'Parameter'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetInheritedServices')],
                            HRESULT,
                            'GetInheritedServices',
                            (['in'], DWORD, 'dwInheritanceType'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDevicePropVariantCollection)),
                               'ppServices'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFormatRenderingProfiles')],
                            HRESULT,
                            'GetFormatRenderingProfiles',
                            (['in'], REFGUID, 'Format'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValuesCollection)),
                               'ppRenderingProfiles'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedCommands')],
                            HRESULT,
                            'GetSupportedCommands',
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceKeyCollection)),
                               'ppCommands'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCommandOptions')],
                            HRESULT,
                            'GetCommandOptions',
                            (['in'], REFPROPERTYKEY, 'Command'),
                            (
                                ['out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppOptions'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceServiceCapabilities_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceServiceMethods_INTERFACE_DEFINED__):
                # interface IPortableDeviceServiceMethods
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceServiceMethods = MIDL_INTERFACE(
                        "{E20333C9-FD34-412D-A381-CC6F2D820DF7}"
                    )
                    IPortableDeviceServiceMethods._iid_ = IID_IPortableDeviceServiceMethods

                    IPortableDeviceServiceMethods._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Invoke')],
                            HRESULT,
                            'Invoke',
                            (['in'], REFGUID, 'Method'),
                            (
                                ['unique', 'in'],
                                POINTER(IPortableDeviceValues),
                               'pParameters'
                            ),
                            (
                                ['in', 'unique', 'out'],
                                POINTER(POINTER(IPortableDeviceValues)),
                               'ppResults'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method InvokeAsync')],
                            HRESULT,
                            'InvokeAsync',
                            (['in'], REFGUID, 'Method'),
                            (
                                ['unique', 'in'],
                                POINTER(IPortableDeviceValues),
                               'pParameters'
                            ),
                            (
                                ['unique', 'in'],
                                POINTER(IPortableDeviceServiceMethodCallback),
                               'pCallback'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                            (
                                ['unique', 'in'],
                                POINTER(IPortableDeviceServiceMethodCallback),
                               'pCallback'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceServiceMethods_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceServiceMethodCallback_INTERFACE_DEFINED__):
                # interface IPortableDeviceServiceMethodCallback
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceServiceMethodCallback = MIDL_INTERFACE(
                        "{C424233C-AFCE-4828-A756-7ED7A2350083}"
                    )
                    IPortableDeviceServiceMethodCallback._iid_ = IID_IPortableDeviceServiceMethodCallback

                    IPortableDeviceServiceMethodCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnComplete')],
                            HRESULT,
                            'OnComplete',
                            (['in'], HRESULT, 'hrStatus'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pResults'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceServiceMethodCallback_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceServiceActivation_INTERFACE_DEFINED__):
                # interface IPortableDeviceServiceActivation
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceServiceActivation = MIDL_INTERFACE(
                        "{E56B0534-D9B9-425C-9B99-75F97CB3D7C8}"
                    )
                    IPortableDeviceServiceActivation._iid_ = IID_IPortableDeviceServiceActivation

                    IPortableDeviceServiceActivation._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OpenAsync')],
                            HRESULT,
                            'OpenAsync',
                            (['in'], LPCWSTR, 'pszPnPServiceID'),
                            (
                                ['in'],
                                POINTER(IPortableDeviceValues),
                               'pClientInfo'
                            ),
                            (
                                ['in'],
                                POINTER(IPortableDeviceServiceOpenCallback),
                               'pCallback'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CancelOpenAsync')],
                            HRESULT,
                            'CancelOpenAsync',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceServiceActivation_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceServiceOpenCallback_INTERFACE_DEFINED__):
                # interface IPortableDeviceServiceOpenCallback
                # [unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceServiceOpenCallback = MIDL_INTERFACE(
                        "{BCED49C8-8EFE-41ED-960B-61313ABD47A9}"
                    )
                    IPortableDeviceServiceOpenCallback._iid_ = IID_IPortableDeviceServiceOpenCallback

                    IPortableDeviceServiceOpenCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnComplete')],
                            HRESULT,
                            'OnComplete',
                            (['in'], HRESULT, 'hrStatus'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceServiceOpenCallback_INTERFACE_DEFINED__

            if not defined(__IPortableDeviceDispatchFactory_INTERFACE_DEFINED__):
                # interface IPortableDeviceDispatchFactory
                # [uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceDispatchFactory = MIDL_INTERFACE(
                        "{5E1EAFC3-E3D7-4132-96FA-759C0F9D1E0F}"
                    )
                    IPortableDeviceDispatchFactory._iid_ = IID_IPortableDeviceDispatchFactory

                    IPortableDeviceDispatchFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDeviceDispatch')],
                            HRESULT,
                            'GetDeviceDispatch',
                            (['in'], LPCWSTR, 'pszPnPDeviceID'),
                            (
                                ['out'],
                                POINTER(POINTER(IDispatch)),
                               'ppDeviceDispatch'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceDispatchFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_PortableDeviceApi_0000_0021
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            if not defined(__IPortableDeviceWebControl_INTERFACE_DEFINED__):
                # interface IPortableDeviceWebControl
                # [uuid][nonextensible][local][dual][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPortableDeviceWebControl = MIDL_INTERFACE(
                        "{94FC7953-5CA1-483A-8AEE-DF52E7747D00}"
                    )
                    IPortableDeviceWebControl._iid_ = IID_IPortableDeviceWebControl

                    IPortableDeviceWebControl._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDeviceFromId')],
                            HRESULT,
                            'GetDeviceFromId',
                            (['in'], BSTR, 'deviceId'),
                            (
                                ['out'],
                                POINTER(POINTER(IDispatch)),
                               'ppDevice'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceFromIdAsync')],
                            HRESULT,
                            'GetDeviceFromIdAsync',
                            (['in'], BSTR, 'deviceId'),
                            (
                                ['in'],
                                POINTER(IDispatch),
                               'pCompletionHandler'
                            ),
                            (['in'], POINTER(IDispatch), 'pErrorHandler'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPortableDeviceWebControl_INTERFACE_DEFINED__

            # interface __MIDL_itf_PortableDeviceApi_0000_0022
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if not defined(__PortableDeviceApiLib_LIBRARY_DEFINED__):
            # library PortableDeviceApiLib
            # [helpstring][version][uuid]
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
                pass
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                pass
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

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

            if defined(__cplusplus):
                pass
            # END IF

            if defined(__cplusplus):
                pass
            # END IF

            class PortableDeviceApiLib(object):
                """
                PortableDeviceApi 1.0 Type Library
                """
                name = 'PortableDeviceClassExtension'
                _reg_typelib_ = (LIBID_PortableDeviceApiLib, 1, 0)

        # END IF  __PortableDeviceApiLib_LIBRARY_DEFINED__

        # interface __MIDL_itf_PortableDeviceApi_0000_0023
        # [local]
    # END IF   (_WIN32_WINNT >= 0x0501)

    # Additional Prototypes for ALL interfaces

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


