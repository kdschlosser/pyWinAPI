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
__mfreadwrite_h__ = None
__IMFReadWriteClassFactory_FWD_DEFINED__ = None
__IMFSourceReader_FWD_DEFINED__ = None
__IMFSourceReaderEx_FWD_DEFINED__ = None
__IMFSourceReaderCallback_FWD_DEFINED__ = None
__IMFSourceReaderCallback2_FWD_DEFINED__ = None
__IMFSinkWriter_FWD_DEFINED__ = None
__IMFSinkWriterEx_FWD_DEFINED__ = None
__IMFSinkWriterEncoderConfig_FWD_DEFINED__ = None
__IMFSinkWriterCallback_FWD_DEFINED__ = None
__IMFSinkWriterCallback2_FWD_DEFINED__ = None
__IMFReadWriteClassFactory_INTERFACE_DEFINED__ = None
__IMFSourceReader_INTERFACE_DEFINED__ = None
__IMFSourceReaderEx_INTERFACE_DEFINED__ = None
__IMFSourceReaderCallback_INTERFACE_DEFINED__ = None
__IMFSourceReaderCallback2_INTERFACE_DEFINED__ = None
__IMFSinkWriter_INTERFACE_DEFINED__ = None
__IMFSinkWriterEx_INTERFACE_DEFINED__ = None
__IMFSinkWriterEncoderConfig_INTERFACE_DEFINED__ = None
__IMFSinkWriterCallback_INTERFACE_DEFINED__ = None
__IMFSinkWriterCallback2_INTERFACE_DEFINED__ = None


class _MF_SINK_WRITER_STATISTICS(ctypes.Structure):
    pass


MF_SINK_WRITER_STATISTICS = _MF_SINK_WRITER_STATISTICS


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


if not defined(__mfreadwrite_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations

    if not defined(__IMFReadWriteClassFactory_FWD_DEFINED__):

        class IMFReadWriteClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IMFReadWriteClassFactory_FWD_DEFINED__

    if not defined(__IMFSourceReader_FWD_DEFINED__):
        class IMFSourceReader(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceReader_FWD_DEFINED__

    if not defined(__IMFSourceReaderEx_FWD_DEFINED__):
        class IMFSourceReaderEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceReaderEx_FWD_DEFINED__

    if not defined(__IMFSourceReaderCallback_FWD_DEFINED__):
        class IMFSourceReaderCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceReaderCallback_FWD_DEFINED__

    if not defined(__IMFSourceReaderCallback2_FWD_DEFINED__):
        class IMFSourceReaderCallback2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceReaderCallback2_FWD_DEFINED__

    if not defined(__IMFSinkWriter_FWD_DEFINED__):
        class IMFSinkWriter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSinkWriter_FWD_DEFINED__

    if not defined(__IMFSinkWriterEx_FWD_DEFINED__):
        class IMFSinkWriterEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSinkWriterEx_FWD_DEFINED__

    if not defined(__IMFSinkWriterEncoderConfig_FWD_DEFINED__):
        class IMFSinkWriterEncoderConfig(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSinkWriterEncoderConfig_FWD_DEFINED__

    if not defined(__IMFSinkWriterCallback_FWD_DEFINED__):
        class IMFSinkWriterCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSinkWriterCallback_FWD_DEFINED__

    if not defined(__IMFSinkWriterCallback2_FWD_DEFINED__):
        class IMFSinkWriterCallback2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSinkWriterCallback2_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.mfobjects_h import * # NOQA
    from pyWinAPI.um.mftransform_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            CLSID_MFReadWriteClassFactory = EXTERN_GUID(
                    0x48E2ED0F,
                    0x98C2,
                    0x4A37,
                    0xBE,
                    0xD5,
                    0x16,
                    0x63,
                    0x12,
                    0xDD,
                    0xD8,
                    0x3F
                )
            if not defined(__IMFReadWriteClassFactory_INTERFACE_DEFINED__):
                # interface IMFReadWriteClassFactory
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFReadWriteClassFactory = MIDL_INTERFACE(
                        "{E7FE2E12-661C-40DA-92F9-4F002AB67627}"
                    )
                    IMFReadWriteClassFactory._iid_ = IID_IMFReadWriteClassFactory

                    IMFReadWriteClassFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateInstanceFromURL')],
                            HRESULT,
                            'CreateInstanceFromURL',
                            (['in'], REFCLSID, 'clsid'),
                            (['in'], LPCWSTR, 'pwszURL'),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(LPVOID), 'ppvObject'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateInstanceFromObject')],
                            HRESULT,
                            'CreateInstanceFromObject',
                            (['in'], REFCLSID, 'clsid'),
                            (['in'], POINTER(comtypes.IUnknown), 'punkObject'),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(LPVOID), 'ppvObject'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFReadWriteClassFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfreadwrite_0000_0001
            # [local]
            CLSID_MFSourceReader = EXTERN_GUID(
                0x1777133C,
                0x0881,
                0x411B,
                0xA5,
                0x77,
                0xAD,
                0x54,
                0x5F,
                0x07,
                0x14,
                0xC4
            )
            mfreadwrite = ctypes.windll.MFREADWRITE

            # STDAPI MFCreateSourceReaderFromURL(
            # _In_ LPCWSTR pwszURL,
            # _In_opt_ IMFAttributes *pAttributes,
            # _Out_ IMFSourceReader **ppSourceReader );
            MFCreateSourceReaderFromURL = mfreadwrite.MFCreateSourceReaderFromURL

            # STDAPI MFCreateSourceReaderFromByteStream(
            # _In_ IMFByteStream *pByteStream,
            # _In_opt_ IMFAttributes *pAttributes,
            # _Out_ IMFSourceReader **ppSourceReader );
            MFCreateSourceReaderFromByteStream = (
                mfreadwrite.MFCreateSourceReaderFromByteStream
            )

            # STDAPI MFCreateSourceReaderFromMediaSource(
            # _In_ IMFMediaSource *pMediaSource,
            # _In_opt_ IMFAttributes *pAttributes,
            # _Out_ IMFSourceReader **ppSourceReader );
            MFCreateSourceReaderFromMediaSource = (
                mfreadwrite.MFCreateSourceReaderFromMediaSource
            )

            MF_SOURCE_READER_ASYNC_CALLBACK = EXTERN_GUID(
                0x1E3DBEAC,
                0xBB43,
                0x4C35,
                0xB5,
                0x07,
                0xCD,
                0x64,
                0x44,
                0x64,
                0xC9,
                0x65
            )
            MF_SOURCE_READER_D3D_MANAGER = EXTERN_GUID(
                0xEC822DA2,
                0xE1E9,
                0x4B29,
                0xA0,
                0xD8,
                0x56,
                0x3C,
                0x71,
                0x9F,
                0x52,
                0x69
            )
            MF_SOURCE_READER_DISABLE_DXVA = EXTERN_GUID(
                0xAA456CFD,
                0x3943,
                0x4A1E,
                0xA7,
                0x7D,
                0x18,
                0x38,
                0xC0,
                0xEA,
                0x2E,
                0x35
            )
            MF_SOURCE_READER_MEDIASOURCE_CONFIG = EXTERN_GUID(
                0x9085ABEB,
                0x0354,
                0x48F9,
                0xAB,
                0xB5,
                0x20,
                0x0D,
                0xF8,
                0x38,
                0xC6,
                0x8E
            )
            MF_SOURCE_READER_MEDIASOURCE_CHARACTERISTICS = EXTERN_GUID(
                0x6D23F5C8,
                0xC5D7,
                0x4A9B,
                0x99,
                0x71,
                0x5D,
                0x11,
                0xF8,
                0xBC,
                0xA8,
                0x80
            )
            MF_SOURCE_READER_ENABLE_VIDEO_PROCESSING = EXTERN_GUID(
                0xFB394F3D,
                0xCCF1,
                0x42EE,
                0xBB,
                0xB3,
                0xF9,
                0xB8,
                0x45,
                0xD5,
                0x68,
                0x1D
            )
            if WINVER >= _WIN32_WINNT_WIN8:
                MF_SOURCE_READER_ENABLE_ADVANCED_VIDEO_PROCESSING = EXTERN_GUID(
                    0xF81DA2C,
                    0xB537,
                    0x4672,
                    0xA8,
                    0xB2,
                    0xA6,
                    0x81,
                    0xB1,
                    0x73,
                    0x7,
                    0xA3
                )
                MF_SOURCE_READER_DISABLE_CAMERA_PLUGINS = EXTERN_GUID(
                    0x9D3365DD,
                    0x58F,
                    0x4CFB,
                    0x9F,
                    0x97,
                    0xB3,
                    0x14,
                    0xCC,
                    0x99,
                    0xC8,
                    0xAD
                )
            # END IF

            MF_SOURCE_READER_DISCONNECT_MEDIASOURCE_ON_SHUTDOWN = EXTERN_GUID(
                0x56B67165,
                0x219E,
                0x456D,
                0xA2,
                0x2E,
                0x2D,
                0x30,
                0x04,
                0xC7,
                0xFE,
                0x56
            )
            MF_SOURCE_READER_ENABLE_TRANSCODE_ONLY_TRANSFORMS = EXTERN_GUID(
                0xDFD4F008,
                0xB5FD,
                0x4E78,
                0xAE,
                0x44,
                0x62,
                0xA1,
                0xE6,
                0x7B,
                0xBE,
                0x27
            )
            MF_SOURCE_READER_D3D11_BIND_FLAGS = EXTERN_GUID(
                0x33F3197B,
                0xF73A,
                0x4E14,
                0x8D,
                0x85,
                0xE,
                0x4C,
                0x43,
                0x68,
                0x78,
                0x8D
            )


            class MF_SOURCE_READER_CONTROL_FLAG(ENUM):
                MF_SOURCE_READER_CONTROLF_DRAIN = 0x1


            class __MIDL___MIDL_itf_mfreadwrite_0000_0001_0001(ENUM):
                MF_SOURCE_READER_INVALID_STREAM_INDEX = 0xFFFFFFFF
                MF_SOURCE_READER_ALL_STREAMS = 0xFFFFFFFE
                MF_SOURCE_READER_ANY_STREAM = 0xFFFFFFFE
                MF_SOURCE_READER_FIRST_AUDIO_STREAM = 0xFFFFFFFD
                MF_SOURCE_READER_FIRST_VIDEO_STREAM = 0xFFFFFFFC
                MF_SOURCE_READER_MEDIASOURCE = 0xFFFFFFFF


            MF_SOURCE_READER_INVALID_STREAM_INDEX = __MIDL___MIDL_itf_mfreadwrite_0000_0001_0001.MF_SOURCE_READER_INVALID_STREAM_INDEX
            MF_SOURCE_READER_ALL_STREAMS = __MIDL___MIDL_itf_mfreadwrite_0000_0001_0001.MF_SOURCE_READER_ALL_STREAMS
            MF_SOURCE_READER_ANY_STREAM = __MIDL___MIDL_itf_mfreadwrite_0000_0001_0001.MF_SOURCE_READER_ANY_STREAM
            MF_SOURCE_READER_FIRST_AUDIO_STREAM = __MIDL___MIDL_itf_mfreadwrite_0000_0001_0001.MF_SOURCE_READER_FIRST_AUDIO_STREAM
            MF_SOURCE_READER_FIRST_VIDEO_STREAM = __MIDL___MIDL_itf_mfreadwrite_0000_0001_0001.MF_SOURCE_READER_FIRST_VIDEO_STREAM
            MF_SOURCE_READER_MEDIASOURCE = __MIDL___MIDL_itf_mfreadwrite_0000_0001_0001.MF_SOURCE_READER_MEDIASOURCE

            if WINVER >= _WIN32_WINNT_WIN8:
                class __MIDL___MIDL_itf_mfreadwrite_0000_0001_0002(ENUM):
                    MF_SOURCE_READER_CURRENT_TYPE_INDEX = 0xFFFFFFFF


                MF_SOURCE_READER_CURRENT_TYPE_INDEX = __MIDL___MIDL_itf_mfreadwrite_0000_0001_0002.MF_SOURCE_READER_CURRENT_TYPE_INDEX
            # END IF   (WINVER >= _WIN32_WINNT_WIN8)

            if not defined(__IMFSourceReader_INTERFACE_DEFINED__):
                # interface IMFSourceReader
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSourceReader = MIDL_INTERFACE(
                        "{70AE66F2-C809-4E4F-8915-BDCB406B7993}"
                    )
                    IMFSourceReader._iid_ = IID_IMFSourceReader

                    IMFSourceReader._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetStreamSelection')],
                            HRESULT,
                            'GetStreamSelection',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['out'], POINTER(BOOL), 'pfSelected'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStreamSelection')],
                            HRESULT,
                            'SetStreamSelection',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], BOOL, 'fSelected'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNativeMediaType')],
                            HRESULT,
                            'GetNativeMediaType',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], DWORD, 'dwMediaTypeIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaType)),
                                'ppMediaType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentMediaType')],
                            HRESULT,
                            'GetCurrentMediaType',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaType)),
                                'ppMediaType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCurrentMediaType')],
                            HRESULT,
                            'SetCurrentMediaType',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], POINTER(DWORD), 'pdwReserved'),
                            (['in'], POINTER(IMFMediaType), 'pMediaType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCurrentPosition')],
                            HRESULT,
                            'SetCurrentPosition',
                            (['in'], REFGUID, 'guidTimeFormat'),
                            (['in'], REFPROPVARIANT, 'varPosition'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ReadSample')],
                            HRESULT,
                            'ReadSample',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], DWORD, 'dwControlFlags'),
                            (['out'], POINTER(DWORD), 'pdwActualStreamIndex'),
                            (['out'], POINTER(DWORD), 'pdwStreamFlags'),
                            (['out'], POINTER(LONGLONG), 'pllTimestamp'),
                            (['out'], POINTER(POINTER(IMFSample)), 'ppSample'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Flush')],
                            HRESULT,
                            'Flush',
                            (['in'], DWORD, 'dwStreamIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetServiceForStream')],
                            HRESULT,
                            'GetServiceForStream',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], REFGUID, 'guidService'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(LPVOID), 'ppvObject'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPresentationAttribute')],
                            HRESULT,
                            'GetPresentationAttribute',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], REFGUID, 'guidAttribute'),
                            (['out'], POINTER(PROPVARIANT), 'pvarAttribute'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSourceReader_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfreadwrite_0000_0002
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
        if WINVER >= _WIN32_WINNT_WIN8:
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
                if not defined(__IMFSourceReaderEx_INTERFACE_DEFINED__):
                    # interface IMFSourceReaderEx
                    # [local][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFSourceReaderEx = MIDL_INTERFACE(
                            "{7B981CF0-560E-4116-9875-B099895F23D7}"
                        )
                        IMFSourceReaderEx._iid_ = IID_IMFSourceReaderEx

                        IMFSourceReaderEx._methods_ = [
                            COMMETHOD(
                                [helpstring('Method SetNativeMediaType')],
                                HRESULT,
                                'SetNativeMediaType',
                                (['in'], DWORD, 'dwStreamIndex'),
                                (['in'], POINTER(IMFMediaType), 'pMediaType'),
                                (['out'], POINTER(DWORD), 'pdwStreamFlags'),
                            ),
                            COMMETHOD(
                                [helpstring('Method AddTransformForStream')],
                                HRESULT,
                                'AddTransformForStream',
                                (['in'], DWORD, 'dwStreamIndex'),
                                (
                                    ['in'],
                                    POINTER(comtypes.IUnknown),
                                    'pTransformOrActivate'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method RemoveAllTransformsForStream')],
                                HRESULT,
                                'RemoveAllTransformsForStream',
                                (['in'], DWORD, 'dwStreamIndex'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTransformForStream')],
                                HRESULT,
                                'GetTransformForStream',
                                (['in'], DWORD, 'dwStreamIndex'),
                                (['in'], DWORD, 'dwTransformIndex'),
                                (['out'], POINTER(GUID), 'pGuidCategory'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTransform)),
                                    'ppTransform'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFSourceReaderEx_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfreadwrite_0000_0003
                # [local]
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
        # END IF

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFSourceReaderCallback_INTERFACE_DEFINED__):
                # interface IMFSourceReaderCallback
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSourceReaderCallback = MIDL_INTERFACE(
                        "{DEEC8D99-FA1D-4D82-84C2-2C8969944867}"
                    )
                    IMFSourceReaderCallback._iid_ = IID_IMFSourceReaderCallback

                    IMFSourceReaderCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnReadSample')],
                            HRESULT,
                            'OnReadSample',
                            (['in'], HRESULT, 'hrStatus'),
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], DWORD, 'dwStreamFlags'),
                            (['in'], LONGLONG, 'llTimestamp'),
                            (['in'], POINTER(IMFSample), 'pSample'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnFlush')],
                            HRESULT,
                            'OnFlush',
                            (['in'], DWORD, 'dwStreamIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnEvent')],
                            HRESULT,
                            'OnEvent',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSourceReaderCallback_INTERFACE_DEFINED__

            if not defined(__IMFSourceReaderCallback2_INTERFACE_DEFINED__):
                # interface IMFSourceReaderCallback2
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSourceReaderCallback2 = MIDL_INTERFACE(
                        "{CF839FE6-8C2A-4DD2-B6EA-C22D6961AF05}"
                    )
                    IMFSourceReaderCallback2._iid_ = IID_IMFSourceReaderCallback2

                    IMFSourceReaderCallback2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnTransformChange')],
                            HRESULT,
                            'OnTransformChange',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnStreamError')],
                            HRESULT,
                            'OnStreamError',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], HRESULT, 'hrStatus'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSourceReaderCallback2_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfreadwrite_0000_0005
            # [local]
            CLSID_MFSinkWriter = EXTERN_GUID(
                0xA3BBFB17,
                0x8273,
                0x4E52,
                0x9E,
                0x0E,
                0x97,
                0x39,
                0xDC,
                0x88,
                0x79,
                0x90
            )
            mfreadwrite = ctypes.windll.MFREADWRITE

            # STDAPI MFCreateSinkWriterFromURL(
            # _In_opt_ LPCWSTR pwszOutputURL,
            # _In_opt_ IMFByteStream *pByteStream,
            # _In_opt_ IMFAttributes *pAttributes,
            # _Out_ IMFSinkWriter **ppSinkWriter );
            MFCreateSinkWriterFromURL = mfreadwrite.MFCreateSinkWriterFromURL

            # STDAPI MFCreateSinkWriterFromMediaSink(
            # _In_ IMFMediaSink *pMediaSink,
            # _In_opt_ IMFAttributes *pAttributes,
            # _Out_ IMFSinkWriter **ppSinkWriter );
            MFCreateSinkWriterFromMediaSink = (
                mfreadwrite.MFCreateSinkWriterFromMediaSink
            )

            MF_SINK_WRITER_ASYNC_CALLBACK = EXTERN_GUID(
                0x48CB183E,
                0x7B0B,
                0x46F4,
                0x82,
                0x2E,
                0x5E,
                0x1D,
                0x2D,
                0xDA,
                0x43,
                0x54
            )
            MF_SINK_WRITER_DISABLE_THROTTLING = EXTERN_GUID(
                0x08B845D8,
                0x2B74,
                0x4AFE,
                0x9D,
                0x53,
                0xBE,
                0x16,
                0xD2,
                0xD5,
                0xAE,
                0x4F
            )
            if WINVER >= _WIN32_WINNT_WIN8:
                MF_SINK_WRITER_D3D_MANAGER = EXTERN_GUID(
                    0xEC822DA2,
                    0xE1E9,
                    0x4B29,
                    0xA0,
                    0xD8,
                    0x56,
                    0x3C,
                    0x71,
                    0x9F,
                    0x52,
                    0x69
                )
                MF_SINK_WRITER_ENCODER_CONFIG = EXTERN_GUID(
                    0xAD91CD04,
                    0xA7CC,
                    0x4AC7,
                    0x99,
                    0xB6,
                    0xA5,
                    0x7B,
                    0x9A,
                    0x4A,
                    0x7C,
                    0x70
                )
            # END IF

            if defined(_MSC_VER) and (_MSC_VER >= 1600):
                pass
            # END IF

            _MF_SINK_WRITER_STATISTICS._fields_ = [
                ('cb', DWORD),
                ('llLastTimestampReceived', LONGLONG),
                ('llLastTimestampEncoded', LONGLONG),
                ('llLastTimestampProcessed', LONGLONG),
                ('llLastStreamTickReceived', LONGLONG),
                ('llLastSinkSampleRequest', LONGLONG),
                ('qwNumSamplesReceived', QWORD),
                ('qwNumSamplesEncoded', QWORD),
                ('qwNumSamplesProcessed', QWORD),
                ('qwNumStreamTicksReceived', QWORD),
                ('dwByteCountQueued', DWORD),
                ('qwByteCountProcessed', QWORD),
                ('dwNumOutstandingSinkSampleRequests', DWORD),
                ('dwAverageSampleRateReceived', DWORD),
                ('dwAverageSampleRateEncoded', DWORD),
                ('dwAverageSampleRateProcessed', DWORD),
            ]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFSinkWriter_INTERFACE_DEFINED__):
                # interface IMFSinkWriter
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSinkWriter = MIDL_INTERFACE(
                        "{3137F1CD-FE5E-4805-A5D8-FB477448CB3D}"
                    )
                    IMFSinkWriter._iid_ = IID_IMFSinkWriter

                    IMFSinkWriter._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddStream')],
                            HRESULT,
                            'AddStream',
                            (['in'], POINTER(IMFMediaType), 'pTargetMediaType'),
                            (['out'], POINTER(DWORD), 'pdwStreamIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetInputMediaType')],
                            HRESULT,
                            'SetInputMediaType',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], POINTER(IMFMediaType), 'pInputMediaType'),
                            (
                                ['in'],
                                POINTER(IMFAttributes),
                                'pEncodingParameters'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method BeginWriting')],
                            HRESULT,
                            'BeginWriting',
                        ),
                        COMMETHOD(
                            [helpstring('Method WriteSample')],
                            HRESULT,
                            'WriteSample',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], POINTER(IMFSample), 'pSample'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SendStreamTick')],
                            HRESULT,
                            'SendStreamTick',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], LONGLONG, 'llTimestamp'),
                        ),
                        COMMETHOD(
                            [helpstring('Method PlaceMarker')],
                            HRESULT,
                            'PlaceMarker',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], LPVOID, 'pvContext'),
                        ),
                        COMMETHOD(
                            [helpstring('Method NotifyEndOfSegment')],
                            HRESULT,
                            'NotifyEndOfSegment',
                            (['in'], DWORD, 'dwStreamIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Flush')],
                            HRESULT,
                            'Flush',
                            (['in'], DWORD, 'dwStreamIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finalize')],
                            HRESULT,
                            'Finalize',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetServiceForStream')],
                            HRESULT,
                            'GetServiceForStream',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], REFGUID, 'guidService'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(LPVOID), 'ppvObject'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStatistics')],
                            HRESULT,
                            'GetStatistics',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (
                                ['out'],
                                POINTER(MF_SINK_WRITER_STATISTICS),
                                'pStats'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSinkWriter_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfreadwrite_0000_0006
            # [local]
            if WINVER >= _WIN32_WINNT_WIN8:
                if not defined(__IMFSinkWriterEx_INTERFACE_DEFINED__):
                    # interface IMFSinkWriterEx
                    # [local][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFSinkWriterEx = MIDL_INTERFACE(
                            "{588D72AB-5BC1-496A-8714-B70617141B25}"
                        )
                        IMFSinkWriterEx._iid_ = IID_IMFSinkWriterEx

                        IMFSinkWriterEx._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetTransformForStream')],
                                HRESULT,
                                'GetTransformForStream',
                                (['in'], DWORD, 'dwStreamIndex'),
                                (['in'], DWORD, 'dwTransformIndex'),
                                (['out'], POINTER(GUID), 'pGuidCategory'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTransform)),
                                    'ppTransform'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFSinkWriterEx_INTERFACE_DEFINED__

                if not defined(__IMFSinkWriterEncoderConfig_INTERFACE_DEFINED__):
                    # interface IMFSinkWriterEncoderConfig
                    # [local][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFSinkWriterEncoderConfig = MIDL_INTERFACE(
                            "{17C3779E-3CDE-4EDE-8C60-3899F5F53AD6}"
                        )
                        IMFSinkWriterEncoderConfig._iid_ = IID_IMFSinkWriterEncoderConfig

                        IMFSinkWriterEncoderConfig._methods_ = [
                            COMMETHOD(
                                [helpstring('Method SetTargetMediaType')],
                                HRESULT,
                                'SetTargetMediaType',
                                (['in'], DWORD, 'dwStreamIndex'),
                                (
                                    ['in'],
                                    POINTER(IMFMediaType),
                                    'pTargetMediaType'
                                ),
                                (
                                    ['in'],
                                    POINTER(IMFAttributes),
                                    'pEncodingParameters'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method PlaceEncodingParameters')],
                                HRESULT,
                                'PlaceEncodingParameters',
                                (['in'], DWORD, 'dwStreamIndex'),
                                (
                                    ['in'],
                                    POINTER(IMFAttributes),
                                    'pEncodingParameters'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFSinkWriterEncoderConfig_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfreadwrite_0000_0008
                # [local]
            # END IF

            if not defined(__IMFSinkWriterCallback_INTERFACE_DEFINED__):
                # interface IMFSinkWriterCallback
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSinkWriterCallback = MIDL_INTERFACE(
                        "{666F76DE-33D2-41B9-A458-29ED0A972C58}"
                    )
                    IMFSinkWriterCallback._iid_ = IID_IMFSinkWriterCallback

                    IMFSinkWriterCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnFinalize')],
                            HRESULT,
                            'OnFinalize',
                            (['in'], HRESULT, 'hrStatus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnMarker')],
                            HRESULT,
                            'OnMarker',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], LPVOID, 'pvContext'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSinkWriterCallback_INTERFACE_DEFINED__

            if not defined(__IMFSinkWriterCallback2_INTERFACE_DEFINED__):
                # interface IMFSinkWriterCallback2
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSinkWriterCallback2 = MIDL_INTERFACE(
                        "{2456BD58-C067-4513-84FE-8D0C88FFDC61}"
                    )
                    IMFSinkWriterCallback2._iid_ = IID_IMFSinkWriterCallback2

                    IMFSinkWriterCallback2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnTransformChange')],
                            HRESULT,
                            'OnTransformChange',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnStreamError')],
                            HRESULT,
                            'OnStreamError',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], HRESULT, 'hrStatus'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSinkWriterCallback2_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfreadwrite_0000_0010
            # [local]
            MF_READWRITE_DISABLE_CONVERTERS = EXTERN_GUID(
                0x98D5B065,
                0x1374,
                0x4847,
                0x8D,
                0x5D,
                0x31,
                0x52,
                0x0F,
                0xEE,
                0x71,
                0x56
            )
            MF_READWRITE_ENABLE_HARDWARE_TRANSFORMS = EXTERN_GUID(
                0xA634A91C,
                0x822B,
                0x41B9,
                0xA4,
                0x94,
                0x4D,
                0xE4,
                0x64,
                0x36,
                0x12,
                0xB0
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINVER >= _WIN32_WINNT_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            MF_READWRITE_MMCSS_CLASS = EXTERN_GUID(
                0x39384300,
                0xD0EB,
                0x40B1,
                0x87,
                0xA0,
                0x33,
                0x18,
                0x87,
                0x1B,
                0x5A,
                0x53
            )
            MF_READWRITE_MMCSS_PRIORITY = EXTERN_GUID(
                0x43AD19CE,
                0xF33F,
                0x4BA9,
                0xA5,
                0x80,
                0xE4,
                0xCD,
                0x12,
                0xF2,
                0xD1,
                0x44
            )
            MF_READWRITE_MMCSS_CLASS_AUDIO = EXTERN_GUID(
                0x430847DA,
                0x0890,
                0x4B0E,
                0x93,
                0x8C,
                0x05,
                0x43,
                0x32,
                0xC5,
                0x47,
                0xE1
            )
            MF_READWRITE_MMCSS_PRIORITY_AUDIO = EXTERN_GUID(
                0x273DB885,
                0x2DE2,
                0x4DB2,
                0xA6,
                0xA7,
                0xFD,
                0xB6,
                0x6F,
                0xB4,
                0x0B,
                0x61
            )
            MF_READWRITE_D3D_OPTIONAL = EXTERN_GUID(
                0x216479D9,
                0x3071,
                0x42CA,
                0xBB,
                0x6C,
                0x4C,
                0x22,
                0x10,
                0x2E,
                0x1D,
                0x18
            )
            MF_MEDIASINK_AUTOFINALIZE_SUPPORTED = EXTERN_GUID(
                0x48C131BE,
                0x135A,
                0x41CB,
                0x82,
                0x90,
                0x3,
                0x65,
                0x25,
                0x9,
                0xC9,
                0x99
            )
            MF_MEDIASINK_ENABLE_AUTOFINALIZE = EXTERN_GUID(
                0x34014265,
                0xCB7E,
                0x4CDE,
                0xAC,
                0x7C,
                0xEF,
                0xFD,
                0x3B,
                0x3C,
                0x25,
                0x30
            )
            MF_READWRITE_ENABLE_AUTOFINALIZE = EXTERN_GUID(
                0xDD7CA129,
                0x8CD1,
                0x4DC5,
                0x9D,
                0xDE,
                0xCE,
                0x16,
                0x86,
                0x75,
                0xDE,
                0x61
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


