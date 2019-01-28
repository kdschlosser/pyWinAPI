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
__mfsharingengine_h__ = None
__IMFSharingEngineClassFactory_FWD_DEFINED__ = None
__IMFMediaSharingEngine_FWD_DEFINED__ = None
__IMFMediaSharingEngineClassFactory_FWD_DEFINED__ = None
__IMFImageSharingEngine_FWD_DEFINED__ = None
__IMFImageSharingEngineClassFactory_FWD_DEFINED__ = None
__IPlayToControl_FWD_DEFINED__ = None
__IPlayToControlWithCapabilities_FWD_DEFINED__ = None
__IPlayToSourceClassFactory_FWD_DEFINED__ = None
__IMFSharingEngineClassFactory_INTERFACE_DEFINED__ = None
__IMFMediaSharingEngine_INTERFACE_DEFINED__ = None
__IMFMediaSharingEngineClassFactory_INTERFACE_DEFINED__ = None
__IMFImageSharingEngine_INTERFACE_DEFINED__ = None
__IMFImageSharingEngineClassFactory_INTERFACE_DEFINED__ = None
__IPlayToControl_INTERFACE_DEFINED__ = None
__IPlayToControlWithCapabilities_INTERFACE_DEFINED__ = None
__IPlayToSourceClassFactory_INTERFACE_DEFINED__ = None


class DEVICE_INFO(ctypes.Structure):
    pass


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


if not defined(__mfsharingengine_h__):
    # Forward Declarations
    if not defined(__IMFSharingEngineClassFactory_FWD_DEFINED__):
        class IMFSharingEngineClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IMFSharingEngineClassFactory_FWD_DEFINED__

    if not defined(__IMFMediaSharingEngine_FWD_DEFINED__):
        class IMFMediaSharingEngine(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSharingEngine_FWD_DEFINED__

    if not defined(__IMFMediaSharingEngineClassFactory_FWD_DEFINED__):
        class IMFMediaSharingEngineClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSharingEngineClassFactory_FWD_DEFINED__

    if not defined(__IMFImageSharingEngine_FWD_DEFINED__):
        class IMFImageSharingEngine(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFImageSharingEngine_FWD_DEFINED__

    if not defined(__IMFImageSharingEngineClassFactory_FWD_DEFINED__):
        class IMFImageSharingEngineClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFImageSharingEngineClassFactory_FWD_DEFINED__

    if not defined(__IPlayToControl_FWD_DEFINED__):
        class IPlayToControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPlayToControl_FWD_DEFINED__

    if not defined(__IPlayToControlWithCapabilities_FWD_DEFINED__):
        class IPlayToControlWithCapabilities(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPlayToControlWithCapabilities_FWD_DEFINED__

    if not defined(__IPlayToSourceClassFactory_FWD_DEFINED__):
        class IPlayToSourceClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPlayToSourceClassFactory_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.mfmediaengine_h import * # NOQA
    from pyWinAPI.winrt.inspectable_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfsharingengine_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINVER >= _WIN32_WINNT_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            DEVICE_INFO._fields_ = [
                ('pFriendlyDeviceName', BSTR),
                ('pUniqueDeviceName', BSTR),
                ('pManufacturerName', BSTR),
                ('pModelName', BSTR),
                ('pIconURL', BSTR),
            ]


            class MF_SHARING_ENGINE_EVENT(ENUM):
                MF_SHARING_ENGINE_EVENT_DISCONNECT = 2000
                MF_SHARING_ENGINE_EVENT_LOCALRENDERINGSTARTED = 2001
                MF_SHARING_ENGINE_EVENT_LOCALRENDERINGENDED = 2002
                MF_SHARING_ENGINE_EVENT_STOPPED = 2003
                MF_SHARING_ENGINE_EVENT_ERROR = 2501


            class MF_MEDIA_SHARING_ENGINE_EVENT(ENUM):
                MF_MEDIA_SHARING_ENGINE_EVENT_DISCONNECT = 2000

            if not defined(__IMFSharingEngineClassFactory_INTERFACE_DEFINED__):
                # interface IMFSharingEngineClassFactory
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSharingEngineClassFactory = MIDL_INTERFACE(
                        "{2BA61F92-8305-413B-9733-FAF15F259384}"
                    )
                    IMFSharingEngineClassFactory._iid_ = IID_IMFSharingEngineClassFactory

                    IMFSharingEngineClassFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateInstance')],
                            HRESULT,
                            'CreateInstance',
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], POINTER(IMFAttributes), 'pAttr'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                               'ppEngine'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSharingEngineClassFactory_INTERFACE_DEFINED__

            if not defined(__IMFMediaSharingEngine_INTERFACE_DEFINED__):
                # interface IMFMediaSharingEngine
                # [local][unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaSharingEngine = MIDL_INTERFACE(
                        "{8D3CE1BF-2367-40E0-9EEE-40D377CC1B46}"
                    )
                    IMFMediaSharingEngine._iid_ = IID_IMFMediaSharingEngine

                    IMFMediaSharingEngine._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDevice')],
                            HRESULT,
                            'GetDevice',
                            (['out'], POINTER(DEVICE_INFO), 'pDevice'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaSharingEngine_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfsharingengine_0000_0002
            # [local]
            MF_MEDIA_SHARING_ENGINE_DEVICE_NAME = EXTERN_GUID(
                0x771E05D1,
                0x862F,
                0x4299,
                0x95,
                0xAC,
                0xAE,
                0x81,
                0xFD,
                0x14,
                0xF3,
                0xE7
            )
            MF_MEDIA_SHARING_ENGINE_DEVICE = EXTERN_GUID(
                0xB461C58A,
                0x7A08,
                0x4B98,
                0x99,
                0xA8,
                0x70,
                0xFD,
                0x5F,
                0x3B,
                0xAD,
                0xFD
            )
            MF_MEDIA_SHARING_ENGINE_INITIAL_SEEK_TIME = DEFINE_GUID(
                0x6F3497F5,
                0xD528,
                0x4A4F,
                0x8D,
                0xD7,
                0xDB,
                0x36,
                0x65,
                0x7E,
                0xC4,
                0xC9
            )
            MF_SHUTDOWN_RENDERER_ON_ENGINE_SHUTDOWN = DEFINE_GUID(
                0xC112D94D,
                0x6B9C,
                0x48F8,
                0xB6,
                0xF9,
                0x79,
                0x50,
                0xFF,
                0x9A,
                0xB7,
                0x1E
            )
            MF_PREFERRED_SOURCE_URI = DEFINE_GUID(
                0x5FC85488,
                0x436A,
                0x4DB8,
                0x90,
                0xAF,
                0x4D,
                0xB4,
                0x2,
                0xAE,
                0x5C,
                0x57
            )
            MF_SHARING_ENGINE_SHAREDRENDERER = DEFINE_GUID(
                0xEFA446A0,
                0x73E7,
                0x404E,
                0x8A,
                0xE2,
                0xFE,
                0xF6,
                0x0A,
                0xF5,
                0xA3,
                0x2B
            )
            MF_SHARING_ENGINE_CALLBACK = DEFINE_GUID(
                0x57DC1E95,
                0xD252,
                0x43FA,
                0x9B,
                0xBC,
                0x18,
                0x0,
                0x70,
                0xEE,
                0xFE,
                0x6D
            )
            if not defined(__IMFMediaSharingEngineClassFactory_INTERFACE_DEFINED__):
                # interface IMFMediaSharingEngineClassFactory
                # [local][unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaSharingEngineClassFactory = MIDL_INTERFACE(
                        "{524D2BC4-B2B1-4FE5-8FAC-FA4E4512B4E0}"
                    )
                    IMFMediaSharingEngineClassFactory._iid_ = IID_IMFMediaSharingEngineClassFactory

                    IMFMediaSharingEngineClassFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateInstance')],
                            HRESULT,
                            'CreateInstance',
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], POINTER(IMFAttributes), 'pAttr'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaSharingEngine)),
                               'ppEngine'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaSharingEngineClassFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfsharingengine_0000_0003
            # [local]
            CLSID_MFMediaSharingEngineClassFactory = EXTERN_GUID(
                0xF8E307FB,
                0x6D45,
                0x4AD3,
                0x99,
                0x93,
                0x66,
                0xCD,
                0x5A,
                0x52,
                0x96,
                0x59
            )
            if not defined(__IMFImageSharingEngine_INTERFACE_DEFINED__):
                # interface IMFImageSharingEngine
                # [local][unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFImageSharingEngine = MIDL_INTERFACE(
                        "{CFA0AE8E-7E1C-44D2-AE68-FC4C148A6354}"
                    )
                    IMFImageSharingEngine._iid_ = IID_IMFImageSharingEngine

                    IMFImageSharingEngine._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetSource')],
                            HRESULT,
                            'SetSource',
                            (['in'], POINTER(comtypes.IUnknown), 'pStream'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDevice')],
                            HRESULT,
                            'GetDevice',
                            (['out'], POINTER(DEVICE_INFO), 'pDevice'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Shutdown')],
                            HRESULT,
                            'Shutdown',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFImageSharingEngine_INTERFACE_DEFINED__

            if not defined(__IMFImageSharingEngineClassFactory_INTERFACE_DEFINED__):
                # interface IMFImageSharingEngineClassFactory
                # [local][unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFImageSharingEngineClassFactory = MIDL_INTERFACE(
                        "{1FC55727-A7FB-4FC8-83AE-8AF024990AF1}"
                    )
                    IMFImageSharingEngineClassFactory._iid_ = IID_IMFImageSharingEngineClassFactory

                    IMFImageSharingEngineClassFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateInstanceFromUDN')],
                            HRESULT,
                            'CreateInstanceFromUDN',
                            (['in'], BSTR, 'pUniqueDeviceName'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFImageSharingEngine)),
                               'ppEngine'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFImageSharingEngineClassFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfsharingengine_0000_0005
            # [local]
            CLSID_MFImageSharingEngineClassFactory = EXTERN_GUID(
                0xB22C3339,
                0x87F3,
                0x4059,
                0xA0,
                0xC5,
                0x3,
                0x7A,
                0xA9,
                0x70,
                0x7E,
                0xAF
            )


            class PLAYTO_SOURCE_CREATEFLAGS(ENUM):
                PLAYTO_SOURCE_NONE = 0
                PLAYTO_SOURCE_IMAGE = 0x1
                PLAYTO_SOURCE_AUDIO = 0x2
                PLAYTO_SOURCE_VIDEO = 0x4
                PLAYTO_SOURCE_PROTECTED = 0x8

            if not defined(__IPlayToControl_INTERFACE_DEFINED__):
                # interface IPlayToControl
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPlayToControl = MIDL_INTERFACE(
                        "{607574EB-F4B6-45C1-B08C-CB715122901D}"
                    )
                    IPlayToControl._iid_ = IID_IPlayToControl

                    IPlayToControl._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Connect')],
                            HRESULT,
                            'Connect',
                            (
                                ['in'],
                                POINTER(IMFSharingEngineClassFactory),
                               'pFactory'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Disconnect')],
                            HRESULT,
                            'Disconnect',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPlayToControl_INTERFACE_DEFINED__

            if not defined(__IPlayToControlWithCapabilities_INTERFACE_DEFINED__):
                # interface IPlayToControlWithCapabilities
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPlayToControlWithCapabilities = MIDL_INTERFACE(
                        "{AA9DD80F-C50A-4220-91C1-332287F82A34}"
                    )
                    IPlayToControlWithCapabilities._iid_ = IID_IPlayToControlWithCapabilities

                    IPlayToControlWithCapabilities._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCapabilities')],
                            HRESULT,
                            'GetCapabilities',
                            (
                                ['out'],
                                POINTER(PLAYTO_SOURCE_CREATEFLAGS),
                               'pCapabilities'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPlayToControlWithCapabilities_INTERFACE_DEFINED__

            if not defined(__IPlayToSourceClassFactory_INTERFACE_DEFINED__):
                # interface IPlayToSourceClassFactory
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPlayToSourceClassFactory = MIDL_INTERFACE(
                        "{842B32A3-9B9B-4D1C-B3F3-49193248A554}"
                    )
                    IPlayToSourceClassFactory._iid_ = IID_IPlayToSourceClassFactory

                    IPlayToSourceClassFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateInstance')],
                            HRESULT,
                            'CreateInstance',
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], POINTER(IPlayToControl), 'pControl'),
                            (
                                ['out'],
                                POINTER(POINTER(IInspectable)),
                               'ppSource'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPlayToSourceClassFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfsharingengine_0000_0008
            # [local]
            CLSID_PlayToSourceClassFactory = EXTERN_GUID(
                0xDA17539A,
                0x3DC3,
                0x42C1,
                0xA7,
                0x49,
                0xA1,
                0x83,
                0xB5,
                0x1F,
                0x08,
                0x5E
            )
            GUID_PlayToService = EXTERN_GUID(
                0xF6A8FF9D,
                0x9E14,
                0x41C9,
                0xBF,
                0x0F,
                0x12,
                0x0A,
                0x2B,
                0x3C,
                0xE1,
                0x20
            )
            GUID_NativeDeviceService = EXTERN_GUID(
                0xEF71E53C,
                0x52F4,
                0x43C5,
                0xB8,
                0x6A,
                0xAD,
                0x6C,
                0xB2,
                0x16,
                0xA6,
                0x1E
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


