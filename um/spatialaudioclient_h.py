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
__spatialaudioclient_h__ = None
__IAudioFormatEnumerator_FWD_DEFINED__ = None
__ISpatialAudioObjectBase_FWD_DEFINED__ = None
__ISpatialAudioObject_FWD_DEFINED__ = None
__ISpatialAudioObjectRenderStreamBase_FWD_DEFINED__ = None
__ISpatialAudioObjectRenderStream_FWD_DEFINED__ = None
__ISpatialAudioObjectRenderStreamNotify_FWD_DEFINED__ = None
__ISpatialAudioClient_FWD_DEFINED__ = None
__IAudioFormatEnumerator_INTERFACE_DEFINED__ = None
__ISpatialAudioObjectBase_INTERFACE_DEFINED__ = None
__ISpatialAudioObject_INTERFACE_DEFINED__ = None
__ISpatialAudioObjectRenderStreamBase_INTERFACE_DEFINED__ = None
__ISpatialAudioObjectRenderStream_INTERFACE_DEFINED__ = None
__ISpatialAudioObjectRenderStreamNotify_INTERFACE_DEFINED__ = None
__ISpatialAudioClient_INTERFACE_DEFINED__ = None


class SpatialAudioObjectRenderStreamActivationParams(ctypes.Structure):
    pass


class SpatialAudioClientActivationParams(ctypes.Structure):
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

if not defined(__spatialaudioclient_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IAudioFormatEnumerator_FWD_DEFINED__):
        class IAudioFormatEnumerator(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAudioFormatEnumerator_FWD_DEFINED__

    if not defined(__ISpatialAudioObjectBase_FWD_DEFINED__):
        class ISpatialAudioObjectBase(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioObjectBase_FWD_DEFINED__

    if not defined(__ISpatialAudioObject_FWD_DEFINED__):
        class ISpatialAudioObject(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioObject_FWD_DEFINED__

    if not defined(__ISpatialAudioObjectRenderStreamBase_FWD_DEFINED__):
        class ISpatialAudioObjectRenderStreamBase(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioObjectRenderStreamBase_FWD_DEFINED__

    if not defined(__ISpatialAudioObjectRenderStream_FWD_DEFINED__):
        class ISpatialAudioObjectRenderStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioObjectRenderStream_FWD_DEFINED__

    if not defined(__ISpatialAudioObjectRenderStreamNotify_FWD_DEFINED__):
        class ISpatialAudioObjectRenderStreamNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __ISpatialAudioObjectRenderStreamNotify_FWD_DEFINED__

    if not defined(__ISpatialAudioClient_FWD_DEFINED__):
        class ISpatialAudioClient(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpatialAudioClient_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.shared.wtypes_h import * # NOQA
    from pyWinAPI.um.unknwn_h import * # NOQA
    from pyWinAPI.winrt.hstring_h import * # NOQA
    from pyWinAPI.um.audioclient_h import * # NOQA
    from pyWinAPI.shared.mmreg_h import * # NOQA
    from pyWinAPI.um.propsys_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_spatialaudioclient_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class AudioObjectType(ENUM):
            AudioObjectType_None = 0
            AudioObjectType_Dynamic = 1 << 0
            AudioObjectType_FrontLeft = 1 << 1
            AudioObjectType_FrontRight = 1 << 2
            AudioObjectType_FrontCenter = 1 << 3
            AudioObjectType_LowFrequency = 1 << 4
            AudioObjectType_SideLeft = 1 << 5
            AudioObjectType_SideRight = 1 << 6
            AudioObjectType_BackLeft = 1 << 7
            AudioObjectType_BackRight = 1 << 8
            AudioObjectType_TopFrontLeft = 1 << 9
            AudioObjectType_TopFrontRight = 1 << 10
            AudioObjectType_TopBackLeft = 1 << 11
            AudioObjectType_TopBackRight = 1 << 12
            AudioObjectType_BottomFrontLeft = 1 << 13
            AudioObjectType_BottomFrontRight = 1 << 14
            AudioObjectType_BottomBackLeft = 1 << 15
            AudioObjectType_BottomBackRight = 1 << 16
            AudioObjectType_BackCenter = 1 << 17

        SpatialAudioObjectRenderStreamActivationParams._fields_ = [
            ('ObjectFormat', POINTER(WAVEFORMATEX)),
            ('StaticObjectTypeMask', AudioObjectType),
            ('MinDynamicObjectCount', UINT32),
            ('MaxDynamicObjectCount', UINT32),
            ('Category', AUDIO_STREAM_CATEGORY),
            ('EventHandle', HANDLE),
            ('NotifyObject', POINTER(ISpatialAudioObjectRenderStreamNotify)),
        ]
        if not defined(__IAudioFormatEnumerator_INTERFACE_DEFINED__):
            # interface IAudioFormatEnumerator
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IAudioFormatEnumerator = MIDL_INTERFACE(
                    "{DCDAA858-895A-4A22-A5EB-67BDA506096D}"
                )
                IAudioFormatEnumerator._iid_ = IID_IAudioFormatEnumerator

                IAudioFormatEnumerator._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(UINT32), 'count'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFormat')],
                        HRESULT,
                        'GetFormat',
                        (['in'], UINT32, 'index'),
                        (['out'], POINTER(POINTER(WAVEFORMATEX)), 'format'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IAudioFormatEnumerator_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObjectBase_INTERFACE_DEFINED__):
            # interface ISpatialAudioObjectBase
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObjectBase = MIDL_INTERFACE(
                    "{CCE0B8F2-8D4D-4EFB-A8CF-3D6ECF1C30E0}"
                )
                ISpatialAudioObjectBase._iid_ = IID_ISpatialAudioObjectBase

                ISpatialAudioObjectBase._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetBuffer')],
                        HRESULT,
                        'GetBuffer',
                        (['out'], POINTER(POINTER(BYTE)), 'buffer'),
                        (['out'], POINTER(UINT32), 'bufferLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetEndOfStream')],
                        HRESULT,
                        'SetEndOfStream',
                        (['in'], UINT32, 'frameCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsActive')],
                        HRESULT,
                        'IsActive',
                        (['out'], POINTER(BOOL), 'isActive'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAudioObjectType')],
                        HRESULT,
                        'GetAudioObjectType',
                        (
                            ['out'],
                            POINTER(AudioObjectType),
                            'audioObjectType'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObjectBase_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObject_INTERFACE_DEFINED__):
            # interface ISpatialAudioObject
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObject = MIDL_INTERFACE(
                    "{DDE28967-521B-46E5-8F00-BD6F2BC8AB1D}"
                )
                ISpatialAudioObject._iid_ = IID_ISpatialAudioObject

                ISpatialAudioObject._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetPosition')],
                        HRESULT,
                        'SetPosition',
                        (['in'], FLOAT, 'x'),
                        (['in'], FLOAT, 'y'),
                        (['in'], FLOAT, 'z'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVolume')],
                        HRESULT,
                        'SetVolume',
                        (['in'], FLOAT, 'volume'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObject_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObjectRenderStreamBase_INTERFACE_DEFINED__):
            # interface ISpatialAudioObjectRenderStreamBase
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObjectRenderStreamBase = MIDL_INTERFACE(
                    "{FEAAF403-C1D8-450D-AA05-E0CCEE7502A8}"
                )
                ISpatialAudioObjectRenderStreamBase._iid_ = IID_ISpatialAudioObjectRenderStreamBase

                ISpatialAudioObjectRenderStreamBase._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetAvailableDynamicObjectCount')],
                        HRESULT,
                        'GetAvailableDynamicObjectCount',
                        (['out'], POINTER(UINT32), 'value'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetService')],
                        HRESULT,
                        'GetService',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'service'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Start')],
                        HRESULT,
                        'Start',
                    ),
                    COMMETHOD(
                        [helpstring('Method Stop')],
                        HRESULT,
                        'Stop',
                    ),
                    COMMETHOD(
                        [helpstring('Method Reset')],
                        HRESULT,
                        'Reset',
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginUpdatingAudioObjects')],
                        HRESULT,
                        'BeginUpdatingAudioObjects',
                        (
                            ['out'],
                            POINTER(UINT32),
                            'availableDynamicObjectCount'
                        ),
                        (['out'], POINTER(UINT32), 'frameCountPerBuffer'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndUpdatingAudioObjects')],
                        HRESULT,
                        'EndUpdatingAudioObjects',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObjectRenderStreamBase_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObjectRenderStream_INTERFACE_DEFINED__):
            # interface ISpatialAudioObjectRenderStream
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObjectRenderStream = MIDL_INTERFACE(
                    "{BAB5F473-B423-477B-85F5-B5A332A04153}"
                )
                ISpatialAudioObjectRenderStream._iid_ = IID_ISpatialAudioObjectRenderStream

                ISpatialAudioObjectRenderStream._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioObject')],
                        HRESULT,
                        'ActivateSpatialAudioObject',
                        (['in'], AudioObjectType, 'type'),
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioObject)),
                            'audioObject'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObjectRenderStream_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioObjectRenderStreamNotify_INTERFACE_DEFINED__):
            # interface ISpatialAudioObjectRenderStreamNotify
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioObjectRenderStreamNotify = MIDL_INTERFACE(
                    "{DDDF83E6-68D7-4C70-883F-A1836AFB4A50}"
                )
                ISpatialAudioObjectRenderStreamNotify._iid_ = IID_ISpatialAudioObjectRenderStreamNotify

                ISpatialAudioObjectRenderStreamNotify._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnAvailableDynamicObjectCountChange')],
                        HRESULT,
                        'OnAvailableDynamicObjectCountChange',
                        (
                            ['in'],
                            POINTER(ISpatialAudioObjectRenderStreamBase),
                            'sender'
                        ),
                        (['in'], LONGLONG, 'hnsComplianceDeadlineTime'),
                        (['in'], UINT32, 'availableDynamicObjectCountChange'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioObjectRenderStreamNotify_INTERFACE_DEFINED__

        if not defined(__ISpatialAudioClient_INTERFACE_DEFINED__):
            # interface ISpatialAudioClient
            # [local][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpatialAudioClient = MIDL_INTERFACE(
                    "{BBF8E066-AAAA-49BE-9A4D-FD2A858EA27F}"
                )
                ISpatialAudioClient._iid_ = IID_ISpatialAudioClient

                ISpatialAudioClient._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetStaticObjectPosition')],
                        HRESULT,
                        'GetStaticObjectPosition',
                        (['in'], AudioObjectType, 'type'),
                        (['out'], POINTER(FLOAT), 'x'),
                        (['out'], POINTER(FLOAT), 'y'),
                        (['out'], POINTER(FLOAT), 'z'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNativeStaticObjectTypeMask')],
                        HRESULT,
                        'GetNativeStaticObjectTypeMask',
                        (['out'], POINTER(AudioObjectType), 'mask'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMaxDynamicObjectCount')],
                        HRESULT,
                        'GetMaxDynamicObjectCount',
                        (['out'], POINTER(UINT32), 'value'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSupportedAudioObjectFormatEnumerator')],
                        HRESULT,
                        'GetSupportedAudioObjectFormatEnumerator',
                        (
                            ['out'],
                            POINTER(POINTER(IAudioFormatEnumerator)),
                            'enumerator'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMaxFrameCount')],
                        HRESULT,
                        'GetMaxFrameCount',
                        (['in'], POINTER(WAVEFORMATEX), 'objectFormat'),
                        (['out'], POINTER(UINT32), 'frameCountPerBuffer'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsAudioObjectFormatSupported')],
                        HRESULT,
                        'IsAudioObjectFormatSupported',
                        (['in'], POINTER(WAVEFORMATEX), 'objectFormat'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsSpatialAudioStreamAvailable')],
                        HRESULT,
                        'IsSpatialAudioStreamAvailable',
                        (['in'], REFIID, 'streamUuid'),
                        (['in'], POINTER(PROPVARIANT), 'auxiliaryInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ActivateSpatialAudioStream')],
                        HRESULT,
                        'ActivateSpatialAudioStream',
                        (['in'], POINTER(PROPVARIANT), 'activationParams'),
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'stream'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpatialAudioClient_INTERFACE_DEFINED__

        # interface __MIDL_itf_spatialaudioclient_0000_0007
        # [local]
        # SpatialAudioClientActivationParams is an optional activation
        # parameter for ISpatialAudioClient
        # ISpatialAudioClient implementations log various things via ETW
        # tracing
        # including a "context" identifier and version information.
        # The "tracing context" identifier helps with correlation of which
        # audio client instance belongs to which application context
        # Sample app code:
        # PROPVARIANT var;
        # PropVariantInit( & var);
        # auto p = reinterpret_cast<SpatialAudioClientActivationParams
        # *>(CoTaskMemAlloc((ctypes.sizeof(SpatialAudioClientActivationParams)));
        #
        # if (nullptr == p) { ... }
        #  context identifier
        #  app identifier
        #  app version info
        #  app version info
        # var.vt = VT_BLOB;
        # var.blob.cbSize = (ctypes.sizeof(*p);
        # var.blob.pBlobData = reinterpret_cast<BYTE *>(p);
        # hr =
        # ActivateAudioInterfaceAsync(device, __
        # uuidof(ISpatialAudioClient), & var, ...);
        #
        # ...
        # PropVariantClear( & var);
        SpatialAudioClientActivationParams._fields_ = [
            ('tracingContextId', GUID),
            ('appId', GUID),
            ('majorVersion', INT),
            ('minorVersion1', INT),
            ('minorVersion2', INT),
            ('minorVersion3', INT),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


