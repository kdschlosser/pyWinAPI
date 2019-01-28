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
__mfcaptureengine_h__ = None
__IMFCaptureEngineOnEventCallback_FWD_DEFINED__ = None
__IMFCaptureEngineOnSampleCallback_FWD_DEFINED__ = None
__IMFCaptureSink_FWD_DEFINED__ = None
__IMFCaptureRecordSink_FWD_DEFINED__ = None
__IMFCapturePreviewSink_FWD_DEFINED__ = None
__IMFCapturePhotoSink_FWD_DEFINED__ = None
__IMFCaptureSource_FWD_DEFINED__ = None
__IMFCaptureEngine_FWD_DEFINED__ = None
__IMFCaptureEngineClassFactory_FWD_DEFINED__ = None
__IMFCaptureEngineOnSampleCallback2_FWD_DEFINED__ = None
__IMFCaptureSink2_FWD_DEFINED__ = None
_MFVideoNormalizedRect_ = None
__IMFCaptureEngineOnEventCallback_INTERFACE_DEFINED__ = None
__IMFCaptureEngineOnSampleCallback_INTERFACE_DEFINED__ = None
__IMFCaptureSink_INTERFACE_DEFINED__ = None
__IMFCaptureRecordSink_INTERFACE_DEFINED__ = None
__IMFCapturePreviewSink_INTERFACE_DEFINED__ = None
__IMFCapturePhotoSink_INTERFACE_DEFINED__ = None
__IMFCaptureSource_INTERFACE_DEFINED__ = None
__IMFCaptureEngine_INTERFACE_DEFINED__ = None
__IMFCaptureEngineClassFactory_INTERFACE_DEFINED__ = None
__IMFCaptureEngineOnSampleCallback2_INTERFACE_DEFINED__ = None
__IMFCaptureSink2_INTERFACE_DEFINED__ = None


class MFVideoNormalizedRect(ctypes.Structure):
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


if not defined(__mfcaptureengine_h__):
    # Forward Declarations
    if not defined(__IMFCaptureEngineOnEventCallback_FWD_DEFINED__):
        class IMFCaptureEngineOnEventCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IMFCaptureEngineOnEventCallback_FWD_DEFINED__

    if not defined(__IMFCaptureEngineOnSampleCallback_FWD_DEFINED__):
        class IMFCaptureEngineOnSampleCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureEngineOnSampleCallback_FWD_DEFINED__

    if not defined(__IMFCaptureSink_FWD_DEFINED__):
        class IMFCaptureSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureSink_FWD_DEFINED__

    if not defined(__IMFCaptureRecordSink_FWD_DEFINED__):
        class IMFCaptureRecordSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureRecordSink_FWD_DEFINED__

    if not defined(__IMFCapturePreviewSink_FWD_DEFINED__):
        class IMFCapturePreviewSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCapturePreviewSink_FWD_DEFINED__

    if not defined(__IMFCapturePhotoSink_FWD_DEFINED__):
        class IMFCapturePhotoSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCapturePhotoSink_FWD_DEFINED__

    if not defined(__IMFCaptureSource_FWD_DEFINED__):
        class IMFCaptureSource(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureSource_FWD_DEFINED__

    if not defined(__IMFCaptureEngine_FWD_DEFINED__):
        class IMFCaptureEngine(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureEngine_FWD_DEFINED__

    if not defined(__IMFCaptureEngineClassFactory_FWD_DEFINED__):
        class IMFCaptureEngineClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureEngineClassFactory_FWD_DEFINED__

    if not defined(__IMFCaptureEngineOnSampleCallback2_FWD_DEFINED__):
        class IMFCaptureEngineOnSampleCallback2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureEngineOnSampleCallback2_FWD_DEFINED__

    if not defined(__IMFCaptureSink2_FWD_DEFINED__):
        class IMFCaptureSink2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCaptureSink2_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.mfobjects_h import * # NOQA
    from pyWinAPI.um.mfidl_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfcaptureengine_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            if not defined(_MFVideoNormalizedRect_):
                MFVideoNormalizedRect._fields_ = [
                    ('left', FLOAT),
                    ('top', FLOAT),
                    ('right', FLOAT),
                    ('bottom', FLOAT),
                ]
            # END IF

            class MF_CAPTURE_ENGINE_DEVICE_TYPE(ENUM):
                MF_CAPTURE_ENGINE_DEVICE_TYPE_AUDIO = 0
                MF_CAPTURE_ENGINE_DEVICE_TYPE_VIDEO = 0x1


            class MF_CAPTURE_ENGINE_SINK_TYPE(ENUM):
                MF_CAPTURE_ENGINE_SINK_TYPE_RECORD = 0
                MF_CAPTURE_ENGINE_SINK_TYPE_PREVIEW = 0x1
                MF_CAPTURE_ENGINE_SINK_TYPE_PHOTO = 0x2


            class __MIDL___MIDL_itf_mfcaptureengine_0000_0000_0001(ENUM):
                MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_PREVIEW = (
                    0xFFFFFFFA
                )
                MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_RECORD = (
                    0xFFFFFFF9
                )
                MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_PHOTO = (
                    0xFFFFFFF8
                )
                MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_AUDIO = (
                    0xFFFFFFF7
                )
                MF_CAPTURE_ENGINE_MEDIASOURCE = 0xFFFFFFFF

            MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_PREVIEW = __MIDL___MIDL_itf_mfcaptureengine_0000_0000_0001.MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_PREVIEW
            MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_RECORD = __MIDL___MIDL_itf_mfcaptureengine_0000_0000_0001.MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_VIDEO_RECORD
            MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_PHOTO = __MIDL___MIDL_itf_mfcaptureengine_0000_0000_0001.MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_PHOTO
            MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_AUDIO = __MIDL___MIDL_itf_mfcaptureengine_0000_0000_0001.MF_CAPTURE_ENGINE_PREFERRED_SOURCE_STREAM_FOR_AUDIO
            MF_CAPTURE_ENGINE_MEDIASOURCE = __MIDL___MIDL_itf_mfcaptureengine_0000_0000_0001.MF_CAPTURE_ENGINE_MEDIASOURCE


            class MF_CAPTURE_ENGINE_STREAM_CATEGORY(ENUM):
                MF_CAPTURE_ENGINE_STREAM_CATEGORY_VIDEO_PREVIEW = 0
                MF_CAPTURE_ENGINE_STREAM_CATEGORY_VIDEO_CAPTURE = 0x1
                MF_CAPTURE_ENGINE_STREAM_CATEGORY_PHOTO_INDEPENDENT = 0x2
                MF_CAPTURE_ENGINE_STREAM_CATEGORY_PHOTO_DEPENDENT = 0x3
                MF_CAPTURE_ENGINE_STREAM_CATEGORY_AUDIO = 0x4
                MF_CAPTURE_ENGINE_STREAM_CATEGORY_UNSUPPORTED = 0x5


            class MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE(ENUM):
                MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_OTHER = 0
                MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_COMMUNICATIONS = 1
                MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_MEDIA = 2
                MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_GAMECHAT = 3
                MF_CAPTURE_ENGINE_MEDIA_CATEGORY_TYPE_SPEECH = 4


            class MF_CAPTURE_ENGINE_AUDIO_PROCESSING_MODE(ENUM):
                MF_CAPTURE_ENGINE_AUDIO_PROCESSING_DEFAULT = 0
                MF_CAPTURE_ENGINE_AUDIO_PROCESSING_RAW = 1

            MF_CAPTURE_ENGINE_INITIALIZED = EXTERN_GUID(
                0x219992BC,
                0xCF92,
                0x4531,
                0xA1,
                0xAE,
                0x96,
                0xE1,
                0xE8,
                0x86,
                0xC8,
                0xF1
            )
            MF_CAPTURE_ENGINE_PREVIEW_STARTED = EXTERN_GUID(
                0xA416DF21,
                0xF9D3,
                0x4A74,
                0x99,
                0x1B,
                0xB8,
                0x17,
                0x29,
                0x89,
                0x52,
                0xC4
            )
            MF_CAPTURE_ENGINE_PREVIEW_STOPPED = EXTERN_GUID(
                0x13D5143C,
                0x1EDD,
                0x4E50,
                0xA2,
                0xEF,
                0x35,
                0x0A,
                0x47,
                0x67,
                0x80,
                0x60
            )
            MF_CAPTURE_ENGINE_RECORD_STARTED = EXTERN_GUID(
                0xAC2B027B,
                0xDDF9,
                0x48A0,
                0x89,
                0xBE,
                0x38,
                0xAB,
                0x35,
                0xEF,
                0x45,
                0xC0
            )
            MF_CAPTURE_ENGINE_RECORD_STOPPED = EXTERN_GUID(
                0x55E5200A,
                0xF98F,
                0x4C0D,
                0xA9,
                0xEC,
                0x9E,
                0xB2,
                0x5E,
                0xD3,
                0xD7,
                0x73
            )
            MF_CAPTURE_ENGINE_PHOTO_TAKEN = EXTERN_GUID(
                0x3C50C445,
                0x7304,
                0x48EB,
                0x86,
                0x5D,
                0xBB,
                0xA1,
                0x9B,
                0xA3,
                0xAF,
                0x5C
            )
            MF_CAPTURE_SOURCE_CURRENT_DEVICE_MEDIA_TYPE_SET = EXTERN_GUID(
                0xE7E75E4C,
                0x039C,
                0x4410,
                0x81,
                0x5B,
                0x87,
                0x41,
                0x30,
                0x7B,
                0x63,
                0xAA
            )
            MF_CAPTURE_ENGINE_ERROR = EXTERN_GUID(
                0x46B89FC6,
                0x33CC,
                0x4399,
                0x9D,
                0xAD,
                0x78,
                0x4D,
                0xE7,
                0x7D,
                0x58,
                0x7C
            )
            MF_CAPTURE_ENGINE_EFFECT_ADDED = EXTERN_GUID(
                0xAA8DC7B5,
                0xA048,
                0x4E13,
                0x8E,
                0xBE,
                0xF2,
                0x3C,
                0x46,
                0xC8,
                0x30,
                0xC1
            )
            MF_CAPTURE_ENGINE_EFFECT_REMOVED = EXTERN_GUID(
                0xC6E8DB07,
                0xFB09,
                0x4A48,
                0x89,
                0xC6,
                0xBF,
                0x92,
                0xA0,
                0x42,
                0x22,
                0xC9
            )
            MF_CAPTURE_ENGINE_ALL_EFFECTS_REMOVED = EXTERN_GUID(
                0xFDED7521,
                0x8ED8,
                0x431A,
                0xA9,
                0x6B,
                0xF3,
                0xE2,
                0x56,
                0x5E,
                0x98,
                0x1C
            )
            MF_CAPTURE_SINK_PREPARED = EXTERN_GUID(
                0x7BFCE257,
                0x12B1,
                0x4409,
                0x8C,
                0x34,
                0xD4,
                0x45,
                0xDA,
                0xAB,
                0x75,
                0x78
            )
            MF_CAPTURE_ENGINE_OUTPUT_MEDIA_TYPE_SET = EXTERN_GUID(
                0xCAAAD994,
                0x83EC,
                0x45E9,
                0xA3,
                0x0A,
                0x1F,
                0x20,
                0xAA,
                0xDB,
                0x98,
                0x31
            )
            MF_CAPTURE_ENGINE_CAMERA_STREAM_BLOCKED = EXTERN_GUID(
                0xA4209417,
                0x8D39,
                0x46F3,
                0xB7,
                0x59,
                0x59,
                0x12,
                0x52,
                0x8F,
                0x42,
                0x07
            )
            MF_CAPTURE_ENGINE_CAMERA_STREAM_UNBLOCKED = EXTERN_GUID(
                0x9BE9EEF0,
                0xCDAF,
                0x4717,
                0x85,
                0x64,
                0x83,
                0x4A,
                0xAE,
                0x66,
                0x41,
                0x5C
            )
            MF_CAPTURE_ENGINE_D3D_MANAGER = EXTERN_GUID(
                0x76E25E7B,
                0xD595,
                0x4283,
                0x96,
                0x2C,
                0xC5,
                0x94,
                0xAF,
                0xD7,
                0x8D,
                0xDF
            )
            MF_CAPTURE_ENGINE_RECORD_SINK_VIDEO_MAX_UNPROCESSED_SAMPLES = EXTERN_GUID(
                0xB467F705,
                0x7913,
                0x4894,
                0x9D,
                0x42,
                0xA2,
                0x15,
                0xFE,
                0xA2,
                0x3D,
                0xA9
            )
            MF_CAPTURE_ENGINE_RECORD_SINK_AUDIO_MAX_UNPROCESSED_SAMPLES = EXTERN_GUID(
                0x1CDDB141,
                0xA7F4,
                0x4D58,
                0x98,
                0x96,
                0x4D,
                0x15,
                0xA5,
                0x3C,
                0x4E,
                0xFE
            )
            MF_CAPTURE_ENGINE_RECORD_SINK_VIDEO_MAX_PROCESSED_SAMPLES = EXTERN_GUID(
                0xE7B4A49E,
                0x382C,
                0x4AEF,
                0xA9,
                0x46,
                0xAE,
                0xD5,
                0x49,
                0xB,
                0x71,
                0x11
            )
            MF_CAPTURE_ENGINE_RECORD_SINK_AUDIO_MAX_PROCESSED_SAMPLES = EXTERN_GUID(
                0x9896E12A,
                0xF707,
                0x4500,
                0xB6,
                0xBD,
                0xDB,
                0x8E,
                0xB8,
                0x10,
                0xB5,
                0xF
            )
            MF_CAPTURE_ENGINE_USE_AUDIO_DEVICE_ONLY = EXTERN_GUID(
                0x1C8077DA,
                0x8466,
                0x4DC4,
                0x8B,
                0x8E,
                0x27,
                0x6B,
                0x3F,
                0x85,
                0x92,
                0x3B
            )
            MF_CAPTURE_ENGINE_USE_VIDEO_DEVICE_ONLY = EXTERN_GUID(
                0x7E025171,
                0xCF32,
                0x4F2E,
                0x8F,
                0x19,
                0x41,
                0x5,
                0x77,
                0xB7,
                0x3A,
                0x66
            )
            MF_CAPTURE_ENGINE_DISABLE_HARDWARE_TRANSFORMS = EXTERN_GUID(
                0xB7C42A6B,
                0x3207,
                0x4495,
                0xB4,
                0xE7,
                0x81,
                0xF9,
                0xC3,
                0x5D,
                0x59,
                0x91
            )
            MF_CAPTURE_ENGINE_DISABLE_DXVA = EXTERN_GUID(
                0xF9818862,
                0x179D,
                0x433F,
                0xA3,
                0x2F,
                0x74,
                0xCB,
                0xCF,
                0x74,
                0x46,
                0x6D
            )
            MF_CAPTURE_ENGINE_MEDIASOURCE_CONFIG = EXTERN_GUID(
                0xBC6989D2,
                0x0FC1,
                0x46E1,
                0xA7,
                0x4F,
                0xEF,
                0xD3,
                0x6B,
                0xC7,
                0x88,
                0xDE
            )
            MF_CAPTURE_ENGINE_DECODER_MFT_FIELDOFUSE_UNLOCK_Attribute = EXTERN_GUID(
                0x2B8AD2E8,
                0x7ACB,
                0x4321,
                0xA6,
                0x06,
                0x32,
                0x5C,
                0x42,
                0x49,
                0xF4,
                0xFC
            )
            MF_CAPTURE_ENGINE_ENCODER_MFT_FIELDOFUSE_UNLOCK_Attribute = EXTERN_GUID(
                0x54C63A00,
                0x78D5,
                0x422F,
                0xAA,
                0x3E,
                0x5E,
                0x99,
                0xAC,
                0x64,
                0x92,
                0x69
            )
            MF_CAPTURE_ENGINE_ENABLE_CAMERA_STREAMSTATE_NOTIFICATION = EXTERN_GUID(
                0x4C808E9D,
                0xAAED,
                0x4713,
                0x90,
                0xFB,
                0xCB,
                0x24,
                0x06,
                0x4A,
                0xB8,
                0xDA
            )
            MF_CAPTURE_ENGINE_MEDIA_CATEGORY = EXTERN_GUID(
                0x8E3F5BD5,
                0xDBBF,
                0x42F0,
                0x85,
                0x42,
                0xD0,
                0x7A,
                0x39,
                0x71,
                0x76,
                0x2A
            )
            MF_CAPTURE_ENGINE_AUDIO_PROCESSING = EXTERN_GUID(
                0x10F1BE5E,
                0x7E11,
                0x410B,
                0x97,
                0x3D,
                0xF4,
                0xB6,
                0x10,
                0x90,
                0x0,
                0xFE
            )
            MF_CAPTURE_ENGINE_EVENT_GENERATOR_GUID = EXTERN_GUID(
                0xABFA8AD5,
                0xFC6D,
                0x4911,
                0x87,
                0xE0,
                0x96,
                0x19,
                0x45,
                0xF8,
                0xF7,
                0xCE
            )
            MF_CAPTURE_ENGINE_EVENT_STREAM_INDEX = EXTERN_GUID(
                0x82697F44,
                0xB1CF,
                0x42EB,
                0x97,
                0x53,
                0xF8,
                0x6D,
                0x64,
                0x9C,
                0x88,
                0x65
            )
            MF_CAPTURE_ENGINE_SELECTEDCAMERAPROFILE = EXTERN_GUID(
                0x03160B7E,
                0x1C6F,
                0x4DB2,
                0xAD,
                0x56,
                0xA7,
                0xC4,
                0x30,
                0xF8,
                0x23,
                0x92
            )
            MF_CAPTURE_ENGINE_SELECTEDCAMERAPROFILE_INDEX = EXTERN_GUID(
                0x3CE88613,
                0x2214,
                0x46C3,
                0xB4,
                0x17,
                0x82,
                0xF8,
                0xA3,
                0x13,
                0xC9,
                0xC3
            )
            if not defined(__IMFCaptureEngineOnEventCallback_INTERFACE_DEFINED__):
                # interface IMFCaptureEngineOnEventCallback
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureEngineOnEventCallback = MIDL_INTERFACE(
                        "{AEDA51C0-9025-4983-9012-DE597B88B089}"
                    )
                    IMFCaptureEngineOnEventCallback._iid_ = IID_IMFCaptureEngineOnEventCallback

                    IMFCaptureEngineOnEventCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnEvent')],
                            HRESULT,
                            'OnEvent',
                            (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureEngineOnEventCallback_INTERFACE_DEFINED__

            if not defined(__IMFCaptureEngineOnSampleCallback_INTERFACE_DEFINED__):
                # interface IMFCaptureEngineOnSampleCallback
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureEngineOnSampleCallback = MIDL_INTERFACE(
                        "{52150B82-AB39-4467-980F-E48BF0822ECD}"
                    )
                    IMFCaptureEngineOnSampleCallback._iid_ = IID_IMFCaptureEngineOnSampleCallback

                    IMFCaptureEngineOnSampleCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnSample')],
                            HRESULT,
                            'OnSample',
                            (['in'], POINTER(IMFSample), 'pSample'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureEngineOnSampleCallback_INTERFACE_DEFINED__

            if not defined(__IMFCaptureSink_INTERFACE_DEFINED__):
                # interface IMFCaptureSink
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureSink = MIDL_INTERFACE(
                        "{72D6135B-35E9-412C-B926-FD5265F2A885}"
                    )
                    IMFCaptureSink._iid_ = IID_IMFCaptureSink

                    IMFCaptureSink._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetOutputMediaType')],
                            HRESULT,
                            'GetOutputMediaType',
                            (['in'], DWORD, 'dwSinkStreamIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaType)),
                                'ppMediaType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetService')],
                            HRESULT,
                            'GetService',
                            (['in'], DWORD, 'dwSinkStreamIndex'),
                            (['in'], REFGUID, 'rguidService'),
                            (['in'], REFIID, 'riid'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'ppUnknown'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddStream')],
                            HRESULT,
                            'AddStream',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                            (['in'], POINTER(IMFMediaType), 'pMediaType'),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                            (['out'], POINTER(DWORD), 'pdwSinkStreamIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Prepare')],
                            HRESULT,
                            'Prepare',
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAllStreams')],
                            HRESULT,
                            'RemoveAllStreams',
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureSink_INTERFACE_DEFINED__

            if not defined(__IMFCaptureRecordSink_INTERFACE_DEFINED__):
                # interface IMFCaptureRecordSink
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureRecordSink = MIDL_INTERFACE(
                        "{3323B55A-F92A-4FE2-8EDC-E9BFC0634D77}"
                    )
                    IMFCaptureRecordSink._iid_ = IID_IMFCaptureRecordSink

                    IMFCaptureRecordSink._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetOutputByteStream')],
                            HRESULT,
                            'SetOutputByteStream',
                            (['in'], POINTER(IMFByteStream), 'pByteStream'),
                            (['in'], REFGUID, 'guidContainerType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetOutputFileName')],
                            HRESULT,
                            'SetOutputFileName',
                            (['in'], LPCWSTR, 'fileName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSampleCallback')],
                            HRESULT,
                            'SetSampleCallback',
                            (['in'], DWORD, 'dwStreamSinkIndex'),
                            (
                                ['in'],
                                POINTER(IMFCaptureEngineOnSampleCallback),
                                'pCallback'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCustomSink')],
                            HRESULT,
                            'SetCustomSink',
                            (['in'], POINTER(IMFMediaSink), 'pMediaSink'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRotation')],
                            HRESULT,
                            'GetRotation',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['out'], POINTER(DWORD), 'pdwRotationValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetRotation')],
                            HRESULT,
                            'SetRotation',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], DWORD, 'dwRotationValue'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureRecordSink_INTERFACE_DEFINED__

            if not defined(__IMFCapturePreviewSink_INTERFACE_DEFINED__):
                # interface IMFCapturePreviewSink
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCapturePreviewSink = MIDL_INTERFACE(
                        "{77346CFD-5B49-4D73-ACE0-5B52A859F2E0}"
                    )
                    IMFCapturePreviewSink._iid_ = IID_IMFCapturePreviewSink

                    IMFCapturePreviewSink._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetRenderHandle')],
                            HRESULT,
                            'SetRenderHandle',
                            (['in'], HANDLE, 'handle'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetRenderSurface')],
                            HRESULT,
                            'SetRenderSurface',
                            (['in'], POINTER(comtypes.IUnknown), 'pSurface'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UpdateVideo')],
                            HRESULT,
                            'UpdateVideo',
                            (['in'], POINTER(MFVideoNormalizedRect), 'pSrc'),
                            (['in'], POINTER(RECT), 'pDst'),
                            (['in'], POINTER(COLORREF), 'pBorderClr'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSampleCallback')],
                            HRESULT,
                            'SetSampleCallback',
                            (['in'], DWORD, 'dwStreamSinkIndex'),
                            (
                                ['in'],
                                POINTER(IMFCaptureEngineOnSampleCallback),
                                'pCallback'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMirrorState')],
                            HRESULT,
                            'GetMirrorState',
                            (['out'], POINTER(BOOL), 'pfMirrorState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetMirrorState')],
                            HRESULT,
                            'SetMirrorState',
                            (['in'], BOOL, 'fMirrorState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRotation')],
                            HRESULT,
                            'GetRotation',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['out'], POINTER(DWORD), 'pdwRotationValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetRotation')],
                            HRESULT,
                            'SetRotation',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], DWORD, 'dwRotationValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCustomSink')],
                            HRESULT,
                            'SetCustomSink',
                            (['in'], POINTER(IMFMediaSink), 'pMediaSink'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCapturePreviewSink_INTERFACE_DEFINED__

            if not defined(__IMFCapturePhotoSink_INTERFACE_DEFINED__):
                # interface IMFCapturePhotoSink
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCapturePhotoSink = MIDL_INTERFACE(
                        "{D2D43CC8-48BB-4AA7-95DB-10C06977E777}"
                    )
                    IMFCapturePhotoSink._iid_ = IID_IMFCapturePhotoSink

                    IMFCapturePhotoSink._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetOutputFileName')],
                            HRESULT,
                            'SetOutputFileName',
                            (['in'], LPCWSTR, 'fileName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSampleCallback')],
                            HRESULT,
                            'SetSampleCallback',
                            (
                                ['in'],
                                POINTER(IMFCaptureEngineOnSampleCallback),
                                'pCallback'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetOutputByteStream')],
                            HRESULT,
                            'SetOutputByteStream',
                            (['in'], POINTER(IMFByteStream), 'pByteStream'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCapturePhotoSink_INTERFACE_DEFINED__

            if not defined(__IMFCaptureSource_INTERFACE_DEFINED__):
                # interface IMFCaptureSource
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureSource = MIDL_INTERFACE(
                        "{439A42A8-0D2C-4505-BE83-F79B2A05D5C4}"
                    )
                    IMFCaptureSource._iid_ = IID_IMFCaptureSource

                    IMFCaptureSource._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCaptureDeviceSource')],
                            HRESULT,
                            'GetCaptureDeviceSource',
                            (
                                ['in'],
                                MF_CAPTURE_ENGINE_DEVICE_TYPE,
                                'mfCaptureEngineDeviceType'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaSource)),
                                'ppMediaSource'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCaptureDeviceActivate')],
                            HRESULT,
                            'GetCaptureDeviceActivate',
                            (
                                ['in'],
                                MF_CAPTURE_ENGINE_DEVICE_TYPE,
                                'mfCaptureEngineDeviceType'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFActivate)),
                                'ppActivate'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetService')],
                            HRESULT,
                            'GetService',
                            (['in'], REFIID, 'rguidService'),
                            (['in'], REFIID, 'riid'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'ppUnknown'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddEffect')],
                            HRESULT,
                            'AddEffect',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                            (['in'], POINTER(comtypes.IUnknown), 'pUnknown'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveEffect')],
                            HRESULT,
                            'RemoveEffect',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                            (['in'], POINTER(comtypes.IUnknown), 'pUnknown'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAllEffects')],
                            HRESULT,
                            'RemoveAllEffects',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAvailableDeviceMediaType')],
                            HRESULT,
                            'GetAvailableDeviceMediaType',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                            (['in'], DWORD, 'dwMediaTypeIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaType)),
                                'ppMediaType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCurrentDeviceMediaType')],
                            HRESULT,
                            'SetCurrentDeviceMediaType',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                            (['in'], POINTER(IMFMediaType), 'pMediaType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentDeviceMediaType')],
                            HRESULT,
                            'GetCurrentDeviceMediaType',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaType)),
                                'ppMediaType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceStreamCount')],
                            HRESULT,
                            'GetDeviceStreamCount',
                            (['out'], POINTER(DWORD), 'pdwStreamCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceStreamCategory')],
                            HRESULT,
                            'GetDeviceStreamCategory',
                            (['in'], DWORD, 'dwSourceStreamIndex'),
                            (
                                ['out'],
                                POINTER(MF_CAPTURE_ENGINE_STREAM_CATEGORY),
                                'pStreamCategory'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMirrorState')],
                            HRESULT,
                            'GetMirrorState',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['out'], POINTER(BOOL), 'pfMirrorState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetMirrorState')],
                            HRESULT,
                            'SetMirrorState',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], BOOL, 'fMirrorState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamIndexFromFriendlyName')],
                            HRESULT,
                            'GetStreamIndexFromFriendlyName',
                            (['in'], UINT32, 'uifriendlyName'),
                            (['out'], POINTER(DWORD), 'pdwActualStreamIndex'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureSource_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfcaptureengine_0000_0007
            # [local]
            CLSID_MFCaptureEngine = EXTERN_GUID(
                0xEFCE38D3,
                0x8914,
                0x4674,
                0xA7,
                0xDF,
                0xAE,
                0x1B,
                0x3D,
                0x65,
                0x4B,
                0x8A
            )
            if not defined(__IMFCaptureEngine_INTERFACE_DEFINED__):
                # interface IMFCaptureEngine
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureEngine = MIDL_INTERFACE(
                        "{A6BBA433-176B-48B2-B375-53AA03473207}"
                    )
                    IMFCaptureEngine._iid_ = IID_IMFCaptureEngine

                    IMFCaptureEngine._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Initialize')],
                            HRESULT,
                            'Initialize',
                            (
                                ['in'],
                                POINTER(IMFCaptureEngineOnEventCallback),
                                'pEventCallback'
                            ),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                                'pAudioSource'
                            ),
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                                'pVideoSource'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method StartPreview')],
                            HRESULT,
                            'StartPreview',
                        ),
                        COMMETHOD(
                            [helpstring('Method StopPreview')],
                            HRESULT,
                            'StopPreview',
                        ),
                        COMMETHOD(
                            [helpstring('Method StartRecord')],
                            HRESULT,
                            'StartRecord',
                        ),
                        COMMETHOD(
                            [helpstring('Method StopRecord')],
                            HRESULT,
                            'StopRecord',
                            (['in'], BOOL, 'bFinalize'),
                            (['in'], BOOL, 'bFlushUnprocessedSamples'),
                        ),
                        COMMETHOD(
                            [helpstring('Method TakePhoto')],
                            HRESULT,
                            'TakePhoto',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSink')],
                            HRESULT,
                            'GetSink',
                            (
                                ['in'],
                                MF_CAPTURE_ENGINE_SINK_TYPE,
                                'mfCaptureEngineSinkType'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFCaptureSink)),
                                'ppSink'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSource')],
                            HRESULT,
                            'GetSource',
                            (
                                ['out'],
                                POINTER(POINTER(IMFCaptureSource)),
                                'ppSource'
                            ),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureEngine_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfcaptureengine_0000_0008
            # [local]
            CLSID_MFCaptureEngineClassFactory = EXTERN_GUID(
                0xEFCE38D3,
                0x8914,
                0x4674,
                0xA7,
                0xDF,
                0xAE,
                0x1B,
                0x3D,
                0x65,
                0x4B,
                0x8A
            )
            if not defined(__IMFCaptureEngineClassFactory_INTERFACE_DEFINED__):
                # interface IMFCaptureEngineClassFactory
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureEngineClassFactory = MIDL_INTERFACE(
                        "{8F02D140-56FC-4302-A705-3A97C78BE779}"
                    )
                    IMFCaptureEngineClassFactory._iid_ = IID_IMFCaptureEngineClassFactory

                    IMFCaptureEngineClassFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateInstance')],
                            HRESULT,
                            'CreateInstance',
                            (['in'], REFCLSID, 'clsid'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(LPVOID), 'ppvObject'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureEngineClassFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfcaptureengine_0000_0009
            # [local]
            MFSampleExtension_DeviceReferenceSystemTime = EXTERN_GUID(
                0x6523775A,
                0xBA2D,
                0x405F,
                0xB2,
                0xC5,
                0x01,
                0xFF,
                0x88,
                0xE2,
                0xE8,
                0xF6
            )
            if not defined(__IMFCaptureEngineOnSampleCallback2_INTERFACE_DEFINED__):
                # interface IMFCaptureEngineOnSampleCallback2
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureEngineOnSampleCallback2 = MIDL_INTERFACE(
                        "{E37CEED7-340F-4514-9F4D-9C2AE026100B}"
                    )
                    IMFCaptureEngineOnSampleCallback2._iid_ = IID_IMFCaptureEngineOnSampleCallback2

                    IMFCaptureEngineOnSampleCallback2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnSynchronizedEvent')],
                            HRESULT,
                            'OnSynchronizedEvent',
                            (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureEngineOnSampleCallback2_INTERFACE_DEFINED__

            if not defined(__IMFCaptureSink2_INTERFACE_DEFINED__):
                # interface IMFCaptureSink2
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCaptureSink2 = MIDL_INTERFACE(
                        "{F9E4219E-6197-4B5E-B888-BEE310AB2C59}"
                    )
                    IMFCaptureSink2._iid_ = IID_IMFCaptureSink2

                    IMFCaptureSink2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetOutputMediaType')],
                            HRESULT,
                            'SetOutputMediaType',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], POINTER(IMFMediaType), 'pMediaType'),
                            (
                                ['in'],
                                POINTER(IMFAttributes),
                                'pEncodingAttributes'
                            ),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IMFCaptureSink2_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfcaptureengine_0000_0011
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


