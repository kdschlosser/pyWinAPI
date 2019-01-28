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
__mfmediaengine_h__ = None
__IMFMediaError_FWD_DEFINED__ = None
__IMFMediaTimeRange_FWD_DEFINED__ = None
__IMFMediaEngineNotify_FWD_DEFINED__ = None
__IMFMediaEngineSrcElements_FWD_DEFINED__ = None
__IMFMediaEngine_FWD_DEFINED__ = None
__IMFMediaEngineEx_FWD_DEFINED__ = None
__IMFMediaEngineAudioEndpointId_FWD_DEFINED__ = None
__IMFMediaEngineExtension_FWD_DEFINED__ = None
__IMFMediaEngineProtectedContent_FWD_DEFINED__ = None
__IAudioSourceProvider_FWD_DEFINED__ = None
__IMFMediaEngineWebSupport_FWD_DEFINED__ = None
__IMFMediaSourceExtensionNotify_FWD_DEFINED__ = None
__IMFBufferListNotify_FWD_DEFINED__ = None
__IMFSourceBufferNotify_FWD_DEFINED__ = None
__IMFSourceBuffer_FWD_DEFINED__ = None
__IMFSourceBufferAppendMode_FWD_DEFINED__ = None
__IMFSourceBufferList_FWD_DEFINED__ = None
__IMFMediaSourceExtension_FWD_DEFINED__ = None
__IMFMediaSourceExtensionLiveSeekableRange_FWD_DEFINED__ = None
__IMFMediaEngineEME_FWD_DEFINED__ = None
__IMFMediaEngineSrcElementsEx_FWD_DEFINED__ = None
__IMFMediaEngineNeedKeyNotify_FWD_DEFINED__ = None
__IMFMediaKeys_FWD_DEFINED__ = None
__IMFMediaKeySession_FWD_DEFINED__ = None
__IMFMediaKeySessionNotify_FWD_DEFINED__ = None
__IMFCdmSuspendNotify_FWD_DEFINED__ = None
__IMFHDCPStatus_FWD_DEFINED__ = None
__IMFMediaEngineOPMInfo_FWD_DEFINED__ = None
__IMFMediaEngineClassFactory_FWD_DEFINED__ = None
__IMFMediaEngineClassFactoryEx_FWD_DEFINED__ = None
__IMFMediaEngineClassFactory2_FWD_DEFINED__ = None
__IMFExtendedDRMTypeSupport_FWD_DEFINED__ = None
__IMFMediaEngineSupportsSourceTransfer_FWD_DEFINED__ = None
__IMFMediaEngineTransferSource_FWD_DEFINED__ = None
__IMFTimedText_FWD_DEFINED__ = None
__IMFTimedTextNotify_FWD_DEFINED__ = None
__IMFTimedTextTrack_FWD_DEFINED__ = None
__IMFTimedTextTrackList_FWD_DEFINED__ = None
__IMFTimedTextCue_FWD_DEFINED__ = None
__IMFTimedTextFormattedText_FWD_DEFINED__ = None
__IMFTimedTextStyle_FWD_DEFINED__ = None
__IMFTimedTextRegion_FWD_DEFINED__ = None
__IMFTimedTextBinary_FWD_DEFINED__ = None
__IMFTimedTextCueList_FWD_DEFINED__ = None
__IMFMediaEngineEMENotify_FWD_DEFINED__ = None
__IMFMediaKeySessionNotify2_FWD_DEFINED__ = None
__IMFMediaKeySystemAccess_FWD_DEFINED__ = None
__IMFMediaEngineClassFactory3_FWD_DEFINED__ = None
__IMFMediaKeys2_FWD_DEFINED__ = None
__IMFMediaKeySession2_FWD_DEFINED__ = None
__IMFMediaError_INTERFACE_DEFINED__ = None
__IMFMediaTimeRange_INTERFACE_DEFINED__ = None
__IMFMediaEngineNotify_INTERFACE_DEFINED__ = None
__IMFMediaEngineSrcElements_INTERFACE_DEFINED__ = None
_MFVideoNormalizedRect_ = None
__IMFMediaEngine_INTERFACE_DEFINED__ = None
__IMFMediaEngineEx_INTERFACE_DEFINED__ = None
__IMFMediaEngineAudioEndpointId_INTERFACE_DEFINED__ = None
__IMFMediaEngineExtension_INTERFACE_DEFINED__ = None
__IMFMediaEngineProtectedContent_INTERFACE_DEFINED__ = None
__IAudioSourceProvider_INTERFACE_DEFINED__ = None
__IMFMediaEngineWebSupport_INTERFACE_DEFINED__ = None
__IMFMediaSourceExtensionNotify_INTERFACE_DEFINED__ = None
__IMFBufferListNotify_INTERFACE_DEFINED__ = None
__IMFSourceBufferNotify_INTERFACE_DEFINED__ = None
__IMFSourceBuffer_INTERFACE_DEFINED__ = None
__IMFSourceBufferAppendMode_INTERFACE_DEFINED__ = None
__IMFSourceBufferList_INTERFACE_DEFINED__ = None
__IMFMediaSourceExtension_INTERFACE_DEFINED__ = None
__IMFMediaSourceExtensionLiveSeekableRange_INTERFACE_DEFINED__ = None
__IMFMediaEngineEME_INTERFACE_DEFINED__ = None
__IMFMediaEngineSrcElementsEx_INTERFACE_DEFINED__ = None
__IMFMediaEngineNeedKeyNotify_INTERFACE_DEFINED__ = None
__IMFMediaKeys_INTERFACE_DEFINED__ = None
__IMFMediaKeySession_INTERFACE_DEFINED__ = None
__IMFMediaKeySessionNotify_INTERFACE_DEFINED__ = None
__IMFCdmSuspendNotify_INTERFACE_DEFINED__ = None
__IMFHDCPStatus_INTERFACE_DEFINED__ = None
__IMFMediaEngineOPMInfo_INTERFACE_DEFINED__ = None
NO_MEDIA_ENGINE_FACTORY = None
__IMFMediaEngineClassFactory_INTERFACE_DEFINED__ = None
__IMFMediaEngineClassFactoryEx_INTERFACE_DEFINED__ = None
__IMFMediaEngineClassFactory2_INTERFACE_DEFINED__ = None
__IMFExtendedDRMTypeSupport_INTERFACE_DEFINED__ = None
__IMFMediaEngineSupportsSourceTransfer_INTERFACE_DEFINED__ = None
__IMFMediaEngineTransferSource_INTERFACE_DEFINED__ = None
__IMFTimedText_INTERFACE_DEFINED__ = None
__IMFTimedTextNotify_INTERFACE_DEFINED__ = None
__IMFTimedTextTrack_INTERFACE_DEFINED__ = None
__IMFTimedTextTrackList_INTERFACE_DEFINED__ = None
__IMFTimedTextCue_INTERFACE_DEFINED__ = None
__IMFTimedTextFormattedText_INTERFACE_DEFINED__ = None
__IMFTimedTextStyle_INTERFACE_DEFINED__ = None
__IMFTimedTextRegion_INTERFACE_DEFINED__ = None
__IMFTimedTextBinary_INTERFACE_DEFINED__ = None
__IMFTimedTextCueList_INTERFACE_DEFINED__ = None
__IMFMediaEngineEMENotify_INTERFACE_DEFINED__ = None
__IMFMediaKeySessionNotify2_INTERFACE_DEFINED__ = None
__IMFMediaKeySystemAccess_INTERFACE_DEFINED__ = None
__IMFMediaEngineClassFactory3_INTERFACE_DEFINED__ = None
__IMFMediaKeys2_INTERFACE_DEFINED__ = None
__IMFMediaKeySession2_INTERFACE_DEFINED__ = None


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


if not defined(__mfmediaengine_h__):
    # Forward Declarations
    if not defined(__IMFMediaError_FWD_DEFINED__):
        class IMFMediaError(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IMFMediaError_FWD_DEFINED__

    if not defined(__IMFMediaTimeRange_FWD_DEFINED__):
        class IMFMediaTimeRange(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaTimeRange_FWD_DEFINED__

    if not defined(__IMFMediaEngineNotify_FWD_DEFINED__):
        class IMFMediaEngineNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineNotify_FWD_DEFINED__

    if not defined(__IMFMediaEngineSrcElements_FWD_DEFINED__):
        class IMFMediaEngineSrcElements(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineSrcElements_FWD_DEFINED__

    if not defined(__IMFMediaEngine_FWD_DEFINED__):
        class IMFMediaEngine(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngine_FWD_DEFINED__

    if not defined(__IMFMediaEngineEx_FWD_DEFINED__):
        class IMFMediaEngineEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineEx_FWD_DEFINED__

    if not defined(__IMFMediaEngineAudioEndpointId_FWD_DEFINED__):
        class IMFMediaEngineAudioEndpointId(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineAudioEndpointId_FWD_DEFINED__

    if not defined(__IMFMediaEngineExtension_FWD_DEFINED__):
        class IMFMediaEngineExtension(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineExtension_FWD_DEFINED__

    if not defined(__IMFMediaEngineProtectedContent_FWD_DEFINED__):
        class IMFMediaEngineProtectedContent(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineProtectedContent_FWD_DEFINED__

    if not defined(__IAudioSourceProvider_FWD_DEFINED__):
        class IAudioSourceProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAudioSourceProvider_FWD_DEFINED__

    if not defined(__IMFMediaEngineWebSupport_FWD_DEFINED__):
        class IMFMediaEngineWebSupport(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineWebSupport_FWD_DEFINED__

    if not defined(__IMFMediaSourceExtensionNotify_FWD_DEFINED__):
        class IMFMediaSourceExtensionNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSourceExtensionNotify_FWD_DEFINED__

    if not defined(__IMFBufferListNotify_FWD_DEFINED__):
        class IMFBufferListNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFBufferListNotify_FWD_DEFINED__

    if not defined(__IMFSourceBufferNotify_FWD_DEFINED__):
        class IMFSourceBufferNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceBufferNotify_FWD_DEFINED__

    if not defined(__IMFSourceBuffer_FWD_DEFINED__):
        class IMFSourceBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceBuffer_FWD_DEFINED__

    if not defined(__IMFSourceBufferAppendMode_FWD_DEFINED__):
        class IMFSourceBufferAppendMode(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceBufferAppendMode_FWD_DEFINED__

    if not defined(__IMFSourceBufferList_FWD_DEFINED__):
        class IMFSourceBufferList(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceBufferList_FWD_DEFINED__

    if not defined(__IMFMediaSourceExtension_FWD_DEFINED__):
        class IMFMediaSourceExtension(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSourceExtension_FWD_DEFINED__

    if not defined(__IMFMediaSourceExtensionLiveSeekableRange_FWD_DEFINED__):
        class IMFMediaSourceExtensionLiveSeekableRange(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSourceExtensionLiveSeekableRange_FWD_DEFINED__

    if not defined(__IMFMediaEngineEME_FWD_DEFINED__):
        class IMFMediaEngineEME(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineEME_FWD_DEFINED__

    if not defined(__IMFMediaEngineSrcElementsEx_FWD_DEFINED__):
        class IMFMediaEngineSrcElementsEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineSrcElementsEx_FWD_DEFINED__

    if not defined(__IMFMediaEngineNeedKeyNotify_FWD_DEFINED__):
        class IMFMediaEngineNeedKeyNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineNeedKeyNotify_FWD_DEFINED__

    if not defined(__IMFMediaKeys_FWD_DEFINED__):
        class IMFMediaKeys(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaKeys_FWD_DEFINED__

    if not defined(__IMFMediaKeySession_FWD_DEFINED__):
        class IMFMediaKeySession(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaKeySession_FWD_DEFINED__

    if not defined(__IMFMediaKeySessionNotify_FWD_DEFINED__):
        class IMFMediaKeySessionNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaKeySessionNotify_FWD_DEFINED__

    if not defined(__IMFCdmSuspendNotify_FWD_DEFINED__):
        class IMFCdmSuspendNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCdmSuspendNotify_FWD_DEFINED__

    if not defined(__IMFHDCPStatus_FWD_DEFINED__):
        class IMFHDCPStatus(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFHDCPStatus_FWD_DEFINED__

    if not defined(__IMFMediaEngineOPMInfo_FWD_DEFINED__):
        class IMFMediaEngineOPMInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineOPMInfo_FWD_DEFINED__

    if not defined(__IMFMediaEngineClassFactory_FWD_DEFINED__):
        class IMFMediaEngineClassFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineClassFactory_FWD_DEFINED__

    if not defined(__IMFMediaEngineClassFactoryEx_FWD_DEFINED__):
        class IMFMediaEngineClassFactoryEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineClassFactoryEx_FWD_DEFINED__

    if not defined(__IMFMediaEngineClassFactory2_FWD_DEFINED__):
        class IMFMediaEngineClassFactory2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineClassFactory2_FWD_DEFINED__

    if not defined(__IMFExtendedDRMTypeSupport_FWD_DEFINED__):
        class IMFExtendedDRMTypeSupport(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFExtendedDRMTypeSupport_FWD_DEFINED__

    if not defined(__IMFMediaEngineSupportsSourceTransfer_FWD_DEFINED__):
        class IMFMediaEngineSupportsSourceTransfer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineSupportsSourceTransfer_FWD_DEFINED__

    if not defined(__IMFMediaEngineTransferSource_FWD_DEFINED__):
        class IMFMediaEngineTransferSource(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineTransferSource_FWD_DEFINED__

    if not defined(__IMFTimedText_FWD_DEFINED__):
        class IMFTimedText(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedText_FWD_DEFINED__

    if not defined(__IMFTimedTextNotify_FWD_DEFINED__):
        class IMFTimedTextNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextNotify_FWD_DEFINED__

    if not defined(__IMFTimedTextTrack_FWD_DEFINED__):
        class IMFTimedTextTrack(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextTrack_FWD_DEFINED__

    if not defined(__IMFTimedTextTrackList_FWD_DEFINED__):
        class IMFTimedTextTrackList(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextTrackList_FWD_DEFINED__

    if not defined(__IMFTimedTextCue_FWD_DEFINED__):
        class IMFTimedTextCue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextCue_FWD_DEFINED__

    if not defined(__IMFTimedTextFormattedText_FWD_DEFINED__):
        class IMFTimedTextFormattedText(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextFormattedText_FWD_DEFINED__

    if not defined(__IMFTimedTextStyle_FWD_DEFINED__):
        class IMFTimedTextStyle(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextStyle_FWD_DEFINED__

    if not defined(__IMFTimedTextRegion_FWD_DEFINED__):
        class IMFTimedTextRegion(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextRegion_FWD_DEFINED__

    if not defined(__IMFTimedTextBinary_FWD_DEFINED__):
        class IMFTimedTextBinary(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextBinary_FWD_DEFINED__

    if not defined(__IMFTimedTextCueList_FWD_DEFINED__):
        class IMFTimedTextCueList(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimedTextCueList_FWD_DEFINED__

    if not defined(__IMFMediaEngineEMENotify_FWD_DEFINED__):
        class IMFMediaEngineEMENotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineEMENotify_FWD_DEFINED__

    if not defined(__IMFMediaKeySessionNotify2_FWD_DEFINED__):
        class IMFMediaKeySessionNotify2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaKeySessionNotify2_FWD_DEFINED__

    if not defined(__IMFMediaKeySystemAccess_FWD_DEFINED__):
        class IMFMediaKeySystemAccess(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaKeySystemAccess_FWD_DEFINED__

    if not defined(__IMFMediaEngineClassFactory3_FWD_DEFINED__):
        class IMFMediaEngineClassFactory3(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaEngineClassFactory3_FWD_DEFINED__

    if not defined(__IMFMediaKeys2_FWD_DEFINED__):
        class IMFMediaKeys2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaKeys2_FWD_DEFINED__

    if not defined(__IMFMediaKeySession2_FWD_DEFINED__):
        class IMFMediaKeySession2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaKeySession2_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwn_h import * # NOQA
    from pyWinAPI.um.mfidl_h import * # NOQA
    from pyWinAPI.um.mfobjects_h import * # NOQA
    from pyWinAPI.um.mftransform_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfmediaengine_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINVER >= _WIN32_WINNT_WIN8:
        # Prevent a name collision
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            class MF_MEDIA_ENGINE_ERR(ENUM):
                MF_MEDIA_ENGINE_ERR_NOERROR = 0
                MF_MEDIA_ENGINE_ERR_ABORTED = 1
                MF_MEDIA_ENGINE_ERR_NETWORK = 2
                MF_MEDIA_ENGINE_ERR_DECODE = 3
                MF_MEDIA_ENGINE_ERR_SRC_NOT_SUPPORTED = 4
                MF_MEDIA_ENGINE_ERR_ENCRYPTED = 5

            if not defined(__IMFMediaError_INTERFACE_DEFINED__):
                # interface IMFMediaError
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaError = MIDL_INTERFACE(
                        "{FC0E10D2-AB2A-4501-A951-06BB1075184C}"
                    )
                    IMFMediaError._iid_ = IID_IMFMediaError

                    IMFMediaError._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetErrorCode')],
                            USHORT,
                            'GetErrorCode',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetExtendedErrorCode')],
                            HRESULT,
                            'GetExtendedErrorCode',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetErrorCode')],
                            HRESULT,
                            'SetErrorCode',
                            (['in'], MF_MEDIA_ENGINE_ERR, 'error'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetExtendedErrorCode')],
                            HRESULT,
                            'SetExtendedErrorCode',
                            (['in'], HRESULT, 'error'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaError_INTERFACE_DEFINED__

            if not defined(__IMFMediaTimeRange_INTERFACE_DEFINED__):
                # interface IMFMediaTimeRange
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaTimeRange = MIDL_INTERFACE(
                        "{DB71A2FC-078A-414E-9DF9-8C2531B0AA6C}"
                    )
                    IMFMediaTimeRange._iid_ = IID_IMFMediaTimeRange

                    IMFMediaTimeRange._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetLength')],
                            DWORD,
                            'GetLength',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStart')],
                            HRESULT,
                            'GetStart',
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(DOUBLE), 'pStart'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetEnd')],
                            HRESULT,
                            'GetEnd',
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(DOUBLE), 'pEnd'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ContainsTime')],
                            BOOL,
                            'ContainsTime',
                            (['in'], DOUBLE, 'time'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddRange')],
                            HRESULT,
                            'AddRange',
                            (['in'], DOUBLE, 'startTime'),
                            (['in'], DOUBLE, 'endTime'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Clear')],
                            HRESULT,
                            'Clear',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaTimeRange_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0002
            # [local]
            class MF_MEDIA_ENGINE_EVENT(ENUM):
                MF_MEDIA_ENGINE_EVENT_LOADSTART = 1
                MF_MEDIA_ENGINE_EVENT_PROGRESS = 2
                MF_MEDIA_ENGINE_EVENT_SUSPEND = 3
                MF_MEDIA_ENGINE_EVENT_ABORT = 4
                MF_MEDIA_ENGINE_EVENT_ERROR = 5
                MF_MEDIA_ENGINE_EVENT_EMPTIED = 6
                MF_MEDIA_ENGINE_EVENT_STALLED = 7
                MF_MEDIA_ENGINE_EVENT_PLAY = 8
                MF_MEDIA_ENGINE_EVENT_PAUSE = 9
                MF_MEDIA_ENGINE_EVENT_LOADEDMETADATA = 10
                MF_MEDIA_ENGINE_EVENT_LOADEDDATA = 11
                MF_MEDIA_ENGINE_EVENT_WAITING = 12
                MF_MEDIA_ENGINE_EVENT_PLAYING = 13
                MF_MEDIA_ENGINE_EVENT_CANPLAY = 14
                MF_MEDIA_ENGINE_EVENT_CANPLAYTHROUGH = 15
                MF_MEDIA_ENGINE_EVENT_SEEKING = 16
                MF_MEDIA_ENGINE_EVENT_SEEKED = 17
                MF_MEDIA_ENGINE_EVENT_TIMEUPDATE = 18
                MF_MEDIA_ENGINE_EVENT_ENDED = 19
                MF_MEDIA_ENGINE_EVENT_RATECHANGE = 20
                MF_MEDIA_ENGINE_EVENT_DURATIONCHANGE = 21
                MF_MEDIA_ENGINE_EVENT_VOLUMECHANGE = 22
                MF_MEDIA_ENGINE_EVENT_FORMATCHANGE = 1000
                MF_MEDIA_ENGINE_EVENT_PURGEQUEUEDEVENTS = 1001
                MF_MEDIA_ENGINE_EVENT_TIMELINE_MARKER = 1002
                MF_MEDIA_ENGINE_EVENT_BALANCECHANGE = 1003
                MF_MEDIA_ENGINE_EVENT_DOWNLOADCOMPLETE = 1004
                MF_MEDIA_ENGINE_EVENT_BUFFERINGSTARTED = 1005
                MF_MEDIA_ENGINE_EVENT_BUFFERINGENDED = 1006
                MF_MEDIA_ENGINE_EVENT_FRAMESTEPCOMPLETED = 1007
                MF_MEDIA_ENGINE_EVENT_NOTIFYSTABLESTATE = 1008
                MF_MEDIA_ENGINE_EVENT_FIRSTFRAMEREADY = 1009
                MF_MEDIA_ENGINE_EVENT_TRACKSCHANGE = 1010
                MF_MEDIA_ENGINE_EVENT_OPMINFO = 1011
                MF_MEDIA_ENGINE_EVENT_RESOURCELOST = 1012
                MF_MEDIA_ENGINE_EVENT_DELAYLOADEVENT_CHANGED = 1013
                MF_MEDIA_ENGINE_EVENT_STREAMRENDERINGERROR = 1014
                MF_MEDIA_ENGINE_EVENT_SUPPORTEDRATES_CHANGED = 1015
                MF_MEDIA_ENGINE_EVENT_AUDIOENDPOINTCHANGE = 1016

            if not defined(__IMFMediaEngineNotify_INTERFACE_DEFINED__):
                # interface IMFMediaEngineNotify
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineNotify = MIDL_INTERFACE(
                        "{FEE7C112-E776-42B5-9BBF-0048524E2BD5}"
                    )
                    IMFMediaEngineNotify._iid_ = IID_IMFMediaEngineNotify

                    IMFMediaEngineNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method EventNotify')],
                            HRESULT,
                            'EventNotify',
                            (['in'], DWORD, 'event'),
                            (['in'], DWORD_PTR, 'param1'),
                            (['in'], DWORD, 'param2'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineNotify_INTERFACE_DEFINED__

            if not defined(__IMFMediaEngineSrcElements_INTERFACE_DEFINED__):
                # interface IMFMediaEngineSrcElements
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineSrcElements = MIDL_INTERFACE(
                        "{7A5E5354-B114-4C72-B991-3131D75032EA}"
                    )
                    IMFMediaEngineSrcElements._iid_ = IID_IMFMediaEngineSrcElements

                    IMFMediaEngineSrcElements._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetLength')],
                            DWORD,
                            'GetLength',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetURL')],
                            HRESULT,
                            'GetURL',
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(BSTR), 'pURL'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetType')],
                            HRESULT,
                            'GetType',
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(BSTR), 'pType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMedia')],
                            HRESULT,
                            'GetMedia',
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(BSTR), 'pMedia'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddElement')],
                            HRESULT,
                            'AddElement',
                            (['in'], BSTR, 'pURL'),
                            (['in'], BSTR, 'pType'),
                            (['in'], BSTR, 'pMedia'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAllElements')],
                            HRESULT,
                            'RemoveAllElements',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineSrcElements_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0004
            # [local]
            class MF_MEDIA_ENGINE_NETWORK(ENUM):
                MF_MEDIA_ENGINE_NETWORK_EMPTY = 0
                MF_MEDIA_ENGINE_NETWORK_IDLE = 1
                MF_MEDIA_ENGINE_NETWORK_LOADING = 2
                MF_MEDIA_ENGINE_NETWORK_NO_SOURCE = 3


            class MF_MEDIA_ENGINE_READY(ENUM):
                MF_MEDIA_ENGINE_READY_HAVE_NOTHING = 0
                MF_MEDIA_ENGINE_READY_HAVE_METADATA = 1
                MF_MEDIA_ENGINE_READY_HAVE_CURRENT_DATA = 2
                MF_MEDIA_ENGINE_READY_HAVE_FUTURE_DATA = 3
                MF_MEDIA_ENGINE_READY_HAVE_ENOUGH_DATA = 4


            class MF_MEDIA_ENGINE_CANPLAY(ENUM):
                MF_MEDIA_ENGINE_CANPLAY_NOT_SUPPORTED = 0
                MF_MEDIA_ENGINE_CANPLAY_MAYBE = 1
                MF_MEDIA_ENGINE_CANPLAY_PROBABLY = 2


            class MF_MEDIA_ENGINE_PRELOAD(ENUM):
                MF_MEDIA_ENGINE_PRELOAD_MISSING = 0
                MF_MEDIA_ENGINE_PRELOAD_EMPTY = 1
                MF_MEDIA_ENGINE_PRELOAD_NONE = 2
                MF_MEDIA_ENGINE_PRELOAD_METADATA = 3
                MF_MEDIA_ENGINE_PRELOAD_AUTOMATIC = 4

            if not defined(_MFVideoNormalizedRect_):
                MFVideoNormalizedRect._fields_ = [
                    ('left', FLOAT),
                    ('top', FLOAT),
                    ('right', FLOAT),
                    ('bottom', FLOAT),
                ]
            # END IF

            if not defined(__IMFMediaEngine_INTERFACE_DEFINED__):
                # interface IMFMediaEngine
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngine = MIDL_INTERFACE(
                        "{98A1B0BB-03EB-4935-AE7C-93C1FA0E1C93}"
                    )
                    IMFMediaEngine._iid_ = IID_IMFMediaEngine

                    IMFMediaEngine._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetError')],
                            HRESULT,
                            'GetError',
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaError)),
                                'ppError'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetErrorCode')],
                            HRESULT,
                            'SetErrorCode',
                            (['in'], MF_MEDIA_ENGINE_ERR, 'error'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSourceElements')],
                            HRESULT,
                            'SetSourceElements',
                            (
                                ['in'],
                                POINTER(IMFMediaEngineSrcElements),
                                'pSrcElements'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSource')],
                            HRESULT,
                            'SetSource',
                            (['in'], BSTR, 'pUrl'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentSource')],
                            HRESULT,
                            'GetCurrentSource',
                            (['out'], POINTER(BSTR), 'ppUrl'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNetworkState')],
                            USHORT,
                            'GetNetworkState',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPreload')],
                            MF_MEDIA_ENGINE_PRELOAD,
                            'GetPreload',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetPreload')],
                            HRESULT,
                            'SetPreload',
                            (['in'], MF_MEDIA_ENGINE_PRELOAD, 'Preload'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBuffered')],
                            HRESULT,
                            'GetBuffered',
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaTimeRange)),
                                'ppBuffered'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Load')],
                            HRESULT,
                            'Load',
                        ),
                        COMMETHOD(
                            [helpstring('Method CanPlayType')],
                            HRESULT,
                            'CanPlayType',
                            (['in'], BSTR, 'type'),
                            (
                                ['out'],
                                POINTER(MF_MEDIA_ENGINE_CANPLAY),
                                'pAnswer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetReadyState')],
                            USHORT,
                            'GetReadyState',
                        ),
                        COMMETHOD(
                            [helpstring('Method IsSeeking')],
                            BOOL,
                            'IsSeeking',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentTime')],
                            DOUBLE,
                            'GetCurrentTime',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCurrentTime')],
                            HRESULT,
                            'SetCurrentTime',
                            (['in'], DOUBLE, 'seekTime'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStartTime')],
                            DOUBLE,
                            'GetStartTime',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDuration')],
                            DOUBLE,
                            'GetDuration',
                        ),
                        COMMETHOD(
                            [helpstring('Method IsPaused')],
                            BOOL,
                            'IsPaused',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDefaultPlaybackRate')],
                            DOUBLE,
                            'GetDefaultPlaybackRate',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetDefaultPlaybackRate')],
                            HRESULT,
                            'SetDefaultPlaybackRate',
                            (['in'], DOUBLE, 'Rate'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPlaybackRate')],
                            DOUBLE,
                            'GetPlaybackRate',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetPlaybackRate')],
                            HRESULT,
                            'SetPlaybackRate',
                            (['in'], DOUBLE, 'Rate'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPlayed')],
                            HRESULT,
                            'GetPlayed',
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaTimeRange)),
                                'ppPlayed'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSeekable')],
                            HRESULT,
                            'GetSeekable',
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaTimeRange)),
                                'ppSeekable'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsEnded')],
                            BOOL,
                            'IsEnded',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAutoPlay')],
                            BOOL,
                            'GetAutoPlay',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetAutoPlay')],
                            HRESULT,
                            'SetAutoPlay',
                            (['in'], BOOL, 'AutoPlay'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetLoop')],
                            BOOL,
                            'GetLoop',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetLoop')],
                            HRESULT,
                            'SetLoop',
                            (['in'], BOOL, 'Loop'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Play')],
                            HRESULT,
                            'Play',
                        ),
                        COMMETHOD(
                            [helpstring('Method Pause')],
                            HRESULT,
                            'Pause',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMuted')],
                            BOOL,
                            'GetMuted',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetMuted')],
                            HRESULT,
                            'SetMuted',
                            (['in'], BOOL, 'Muted'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVolume')],
                            DOUBLE,
                            'GetVolume',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetVolume')],
                            HRESULT,
                            'SetVolume',
                            (['in'], DOUBLE, 'Volume'),
                        ),
                        COMMETHOD(
                            [helpstring('Method HasVideo')],
                            BOOL,
                            'HasVideo',
                        ),
                        COMMETHOD(
                            [helpstring('Method HasAudio')],
                            BOOL,
                            'HasAudio',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNativeVideoSize')],
                            HRESULT,
                            'GetNativeVideoSize',
                            (['out'], POINTER(DWORD), 'cx'),
                            (['out'], POINTER(DWORD), 'cy'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVideoAspectRatio')],
                            HRESULT,
                            'GetVideoAspectRatio',
                            (['out'], POINTER(DWORD), 'cx'),
                            (['out'], POINTER(DWORD), 'cy'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Shutdown')],
                            HRESULT,
                            'Shutdown',
                        ),
                        COMMETHOD(
                            [helpstring('Method TransferVideoFrame')],
                            HRESULT,
                            'TransferVideoFrame',
                            (['in'], POINTER(comtypes.IUnknown), 'pDstSurf'),
                            (['in'], POINTER(MFVideoNormalizedRect), 'pSrc'),
                            (['in'], POINTER(RECT), 'pDst'),
                            (['in'], POINTER(MFARGB), 'pBorderClr'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnVideoStreamTick')],
                            HRESULT,
                            'OnVideoStreamTick',
                            (['out'], POINTER(LONGLONG), 'pPts'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngine_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0005
            # [local]
            class MF_MEDIA_ENGINE_S3D_PACKING_MODE(ENUM):
                MF_MEDIA_ENGINE_S3D_PACKING_MODE_NONE = 0
                MF_MEDIA_ENGINE_S3D_PACKING_MODE_SIDE_BY_SIDE = 1
                MF_MEDIA_ENGINE_S3D_PACKING_MODE_TOP_BOTTOM = 2


            class MF_MEDIA_ENGINE_STATISTIC(ENUM):
                MF_MEDIA_ENGINE_STATISTIC_FRAMES_RENDERED = 0
                MF_MEDIA_ENGINE_STATISTIC_FRAMES_DROPPED = 1
                MF_MEDIA_ENGINE_STATISTIC_BYTES_DOWNLOADED = 2
                MF_MEDIA_ENGINE_STATISTIC_BUFFER_PROGRESS = 3
                MF_MEDIA_ENGINE_STATISTIC_FRAMES_PER_SECOND = 4
                MF_MEDIA_ENGINE_STATISTIC_PLAYBACK_JITTER = 5
                MF_MEDIA_ENGINE_STATISTIC_FRAMES_CORRUPTED = 6
                MF_MEDIA_ENGINE_STATISTIC_TOTAL_FRAME_DELAY = 7


            class MF_MEDIA_ENGINE_SEEK_MODE(ENUM):
                MF_MEDIA_ENGINE_SEEK_MODE_NORMAL = 0
                MF_MEDIA_ENGINE_SEEK_MODE_APPROXIMATE = 1

            if not defined(__IMFMediaEngineEx_INTERFACE_DEFINED__):
                # interface IMFMediaEngineEx
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineEx = MIDL_INTERFACE(
                        "{83015EAD-B1E6-40D0-A98A-37145FFE1AD1}"
                    )
                    IMFMediaEngineEx._iid_ = IID_IMFMediaEngineEx

                    IMFMediaEngineEx._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetSourceFromByteStream')],
                            HRESULT,
                            'SetSourceFromByteStream',
                            (['in'], POINTER(IMFByteStream), 'pByteStream'),
                            (['in'], BSTR, 'pURL'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStatistics')],
                            HRESULT,
                            'GetStatistics',
                            (
                                ['in'],
                                MF_MEDIA_ENGINE_STATISTIC,
                                'StatisticID'
                            ),
                            (['out'], POINTER(PROPVARIANT), 'pStatistic'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UpdateVideoStream')],
                            HRESULT,
                            'UpdateVideoStream',
                            (['in'], POINTER(MFVideoNormalizedRect), 'pSrc'),
                            (['in'], POINTER(RECT), 'pDst'),
                            (['in'], POINTER(MFARGB), 'pBorderClr'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBalance')],
                            DOUBLE,
                            'GetBalance',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetBalance')],
                            HRESULT,
                            'SetBalance',
                            (['in'], DOUBLE, 'balance'),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsPlaybackRateSupported')],
                            BOOL,
                            'IsPlaybackRateSupported',
                            (['in'], DOUBLE, 'rate'),
                        ),
                        COMMETHOD(
                            [helpstring('Method FrameStep')],
                            HRESULT,
                            'FrameStep',
                            (['in'], BOOL, 'Forward'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetResourceCharacteristics')],
                            HRESULT,
                            'GetResourceCharacteristics',
                            (['out'], POINTER(DWORD), 'pCharacteristics'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPresentationAttribute')],
                            HRESULT,
                            'GetPresentationAttribute',
                            (['in'], REFGUID, 'guidMFAttribute'),
                            (['out'], POINTER(PROPVARIANT), 'pvValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNumberOfStreams')],
                            HRESULT,
                            'GetNumberOfStreams',
                            (['out'], POINTER(DWORD), 'pdwStreamCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamAttribute')],
                            HRESULT,
                            'GetStreamAttribute',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], REFGUID, 'guidMFAttribute'),
                            (['out'], POINTER(PROPVARIANT), 'pvValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamSelection')],
                            HRESULT,
                            'GetStreamSelection',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['out'], POINTER(BOOL), 'pEnabled'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStreamSelection')],
                            HRESULT,
                            'SetStreamSelection',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], BOOL, 'Enabled'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ApplyStreamSelections')],
                            HRESULT,
                            'ApplyStreamSelections',
                        ),
                        COMMETHOD(
                            [helpstring('Method IsProtected')],
                            HRESULT,
                            'IsProtected',
                            (['out'], POINTER(BOOL), 'pProtected'),
                        ),
                        COMMETHOD(
                            [helpstring('Method InsertVideoEffect')],
                            HRESULT,
                            'InsertVideoEffect',
                            (['in'], POINTER(comtypes.IUnknown), 'pEffect'),
                            (['in'], BOOL, 'fOptional'),
                        ),
                        COMMETHOD(
                            [helpstring('Method InsertAudioEffect')],
                            HRESULT,
                            'InsertAudioEffect',
                            (['in'], POINTER(comtypes.IUnknown), 'pEffect'),
                            (['in'], BOOL, 'fOptional'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAllEffects')],
                            HRESULT,
                            'RemoveAllEffects',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetTimelineMarkerTimer')],
                            HRESULT,
                            'SetTimelineMarkerTimer',
                            (['in'], DOUBLE, 'timeToFire'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetTimelineMarkerTimer')],
                            HRESULT,
                            'GetTimelineMarkerTimer',
                            (['out'], POINTER(DOUBLE), 'pTimeToFire'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CancelTimelineMarkerTimer')],
                            HRESULT,
                            'CancelTimelineMarkerTimer',
                        ),
                        COMMETHOD(
                            [helpstring('Method IsStereo3D')],
                            BOOL,
                            'IsStereo3D',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStereo3DFramePackingMode')],
                            HRESULT,
                            'GetStereo3DFramePackingMode',
                            (
                                ['out'],
                                POINTER(MF_MEDIA_ENGINE_S3D_PACKING_MODE),
                                'packMode'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStereo3DFramePackingMode')],
                            HRESULT,
                            'SetStereo3DFramePackingMode',
                            (
                                ['in'],
                                MF_MEDIA_ENGINE_S3D_PACKING_MODE,
                                'packMode'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStereo3DRenderMode')],
                            HRESULT,
                            'GetStereo3DRenderMode',
                            (
                                ['out'],
                                POINTER(MF3DVideoOutputType),
                                'outputType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStereo3DRenderMode')],
                            HRESULT,
                            'SetStereo3DRenderMode',
                            (['in'], MF3DVideoOutputType, 'outputType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method EnableWindowlessSwapchainMode')],
                            HRESULT,
                            'EnableWindowlessSwapchainMode',
                            (['in'], BOOL, 'fEnable'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVideoSwapchainHandle')],
                            HRESULT,
                            'GetVideoSwapchainHandle',
                            (['out'], POINTER(HANDLE), 'phSwapchain'),
                        ),
                        COMMETHOD(
                            [helpstring('Method EnableHorizontalMirrorMode')],
                            HRESULT,
                            'EnableHorizontalMirrorMode',
                            (['in'], BOOL, 'fEnable'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAudioStreamCategory')],
                            HRESULT,
                            'GetAudioStreamCategory',
                            (['out'], POINTER(UINT32), 'pCategory'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetAudioStreamCategory')],
                            HRESULT,
                            'SetAudioStreamCategory',
                            (['in'], UINT32, 'category'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAudioEndpointRole')],
                            HRESULT,
                            'GetAudioEndpointRole',
                            (['out'], POINTER(UINT32), 'pRole'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetAudioEndpointRole')],
                            HRESULT,
                            'SetAudioEndpointRole',
                            (['in'], UINT32, 'role'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRealTimeMode')],
                            HRESULT,
                            'GetRealTimeMode',
                            (['out'], POINTER(BOOL), 'pfEnabled'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetRealTimeMode')],
                            HRESULT,
                            'SetRealTimeMode',
                            (['in'], BOOL, 'fEnable'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCurrentTimeEx')],
                            HRESULT,
                            'SetCurrentTimeEx',
                            (['in'], DOUBLE, 'seekTime'),
                            (['in'], MF_MEDIA_ENGINE_SEEK_MODE, 'seekMode'),
                        ),
                        COMMETHOD(
                            [helpstring('Method EnableTimeUpdateTimer')],
                            HRESULT,
                            'EnableTimeUpdateTimer',
                            (['in'], BOOL, 'fEnableTimer'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineEx_INTERFACE_DEFINED__

            if not defined(__IMFMediaEngineAudioEndpointId_INTERFACE_DEFINED__):
                # interface IMFMediaEngineAudioEndpointId
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineAudioEndpointId = MIDL_INTERFACE(
                        "{7A3BAC98-0E76-49FB-8C20-8A86FD98EAF2}"
                    )
                    IMFMediaEngineAudioEndpointId._iid_ = IID_IMFMediaEngineAudioEndpointId

                    IMFMediaEngineAudioEndpointId._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetAudioEndpointId')],
                            HRESULT,
                            'SetAudioEndpointId',
                            (['in'], LPCWSTR, 'pszEndpointId'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAudioEndpointId')],
                            HRESULT,
                            'GetAudioEndpointId',
                            (['out'], POINTER(LPWSTR), 'ppszEndpointId'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineAudioEndpointId_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0007
            # [local]
            class MF_MEDIA_ENGINE_EXTENSION_TYPE(ENUM):
                MF_MEDIA_ENGINE_EXTENSION_TYPE_MEDIASOURCE = 0
                MF_MEDIA_ENGINE_EXTENSION_TYPE_BYTESTREAM = 1

            if not defined(__IMFMediaEngineExtension_INTERFACE_DEFINED__):
                # interface IMFMediaEngineExtension
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineExtension = MIDL_INTERFACE(
                        "{2F69D622-20B5-41E9-AFDF-89CED1DDA04E}"
                    )
                    IMFMediaEngineExtension._iid_ = IID_IMFMediaEngineExtension

                    IMFMediaEngineExtension._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CanPlayType')],
                            HRESULT,
                            'CanPlayType',
                            (['in'], BOOL, 'AudioOnly'),
                            (['in'], BSTR, 'MimeType'),
                            (
                                ['out'],
                                POINTER(MF_MEDIA_ENGINE_CANPLAY),
                               'pAnswer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method BeginCreateObject')],
                            HRESULT,
                            'BeginCreateObject',
                            (['in'], BSTR, 'bstrURL'),
                            (['in'], POINTER(IMFByteStream), 'pByteStream'),
                            (['in'], MF_OBJECT_TYPE, 'type'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'ppIUnknownCancelCookie'
                            ),
                            (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                            (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CancelObjectCreation')],
                            HRESULT,
                            'CancelObjectCreation',
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                                'pIUnknownCancelCookie'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method EndCreateObject')],
                            HRESULT,
                            'EndCreateObject',
                            (['in'], POINTER(IMFAsyncResult), 'pResult'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'ppObject'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineExtension_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0008
            # [local]
            class MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS(ENUM):
                MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_PROTECTED = 0x1
                MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_SURFACE_PROTECTION = (
                    0x2
                )
                MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_ANTI_SCREEN_SCRAPE_PROTECTION = (
                    0x4
                )

            MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_PROTECTED = MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS.MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_PROTECTED
            MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_SURFACE_PROTECTION = MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS.MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_SURFACE_PROTECTION
            MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_ANTI_SCREEN_SCRAPE_PROTECTION = MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAGS.MF_MEDIA_ENGINE_FRAME_PROTECTION_FLAG_REQUIRES_ANTI_SCREEN_SCRAPE_PROTECTION
            if not defined(__IMFMediaEngineProtectedContent_INTERFACE_DEFINED__):
                # interface IMFMediaEngineProtectedContent
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineProtectedContent = MIDL_INTERFACE(
                        "{9F8021E8-9C8C-487E-BB5C-79AA4779938C}"
                    )
                    IMFMediaEngineProtectedContent._iid_ = IID_IMFMediaEngineProtectedContent

                    IMFMediaEngineProtectedContent._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ShareResources')],
                            HRESULT,
                            'ShareResources',
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                                'pUnkDeviceContext'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRequiredProtections')],
                            HRESULT,
                            'GetRequiredProtections',
                            (
                                ['out'],
                                POINTER(DWORD),
                                'pFrameProtectionFlags'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetOPMWindow')],
                            HRESULT,
                            'SetOPMWindow',
                            (['in'], HWND, 'hwnd'),
                        ),
                        COMMETHOD(
                            [helpstring('Method TransferVideoFrame')],
                            HRESULT,
                            'TransferVideoFrame',
                            (['in'], POINTER(comtypes.IUnknown), 'pDstSurf'),
                            (['in'], POINTER(MFVideoNormalizedRect), 'pSrc'),
                            (['in'], POINTER(RECT), 'pDst'),
                            (['in'], POINTER(MFARGB), 'pBorderClr'),
                            (
                                ['out'],
                                POINTER(DWORD),
                                'pFrameProtectionFlags'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetContentProtectionManager')],
                            HRESULT,
                            'SetContentProtectionManager',
                            (
                                ['in'],
                                POINTER(IMFContentProtectionManager),
                                'pCPM'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetApplicationCertificate')],
                            HRESULT,
                            'SetApplicationCertificate',
                            (['in'], POINTER(BYTE), 'pbBlob'),
                            (['in'], DWORD, 'cbBlob'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineProtectedContent_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0009
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            if not defined(__IAudioSourceProvider_INTERFACE_DEFINED__):
                # interface IAudioSourceProvider
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAudioSourceProvider = MIDL_INTERFACE(
                        "{EBBAF249-AFC2-4582-91C6-B60DF2E84954}"
                    )
                    IAudioSourceProvider._iid_ = IID_IAudioSourceProvider

                    IAudioSourceProvider._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ProvideInput')],
                            HRESULT,
                            'ProvideInput',
                            (['in'], DWORD, 'dwSampleCount'),
                            (
                                ['out', 'in'],
                                POINTER(DWORD),
                                'pdwChannelCount'
                            ),
                            (
                                ['out'],
                                POINTER(FLOAT),
                                'pInterleavedAudioData'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAudioSourceProvider_INTERFACE_DEFINED__

            if not defined(__IMFMediaEngineWebSupport_INTERFACE_DEFINED__):
                # interface IMFMediaEngineWebSupport
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineWebSupport = MIDL_INTERFACE(
                        "{BA2743A1-07E0-48EF-84B6-9A2ED023CA6C}"
                    )
                    IMFMediaEngineWebSupport._iid_ = IID_IMFMediaEngineWebSupport

                    IMFMediaEngineWebSupport._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ShouldDelayTheLoadEvent')],
                            BOOL,
                            'ShouldDelayTheLoadEvent',
                        ),
                        COMMETHOD(
                            [helpstring('Method ConnectWebAudio')],
                            HRESULT,
                            'ConnectWebAudio',
                            (['in'], DWORD, 'dwSampleRate'),
                            (
                                ['out'],
                                POINTER(POINTER(IAudioSourceProvider)),
                                'ppSourceProvider'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method DisconnectWebAudio')],
                            HRESULT,
                            'DisconnectWebAudio',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineWebSupport_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0011
            # [local]
            MF_MSE_CALLBACK = EXTERN_GUID(
                0x9063A7C0,
                0x42C5,
                0x4FFD,
                0xA8,
                0xA8,
                0x6F,
                0xCF,
                0x9E,
                0xA3,
                0xD0,
                0x0C
            )
            MF_MSE_ACTIVELIST_CALLBACK = EXTERN_GUID(
                0x949BDA0F,
                0x4549,
                0x46D5,
                0xAD,
                0x7F,
                0xB8,
                0x46,
                0xE1,
                0xAB,
                0x16,
                0x52
            )
            MF_MSE_BUFFERLIST_CALLBACK = EXTERN_GUID(
                0x42E669B0,
                0xD60E,
                0x4AFB,
                0xA8,
                0x5B,
                0xD8,
                0xE5,
                0xFE,
                0x6B,
                0xDA,
                0xB5
            )
            MF_MSE_VP9_SUPPORT = EXTERN_GUID(
                0x92D78429,
                0xD88B,
                0x4FF0,
                0x83,
                0x22,
                0x80,
                0x3E,
                0xFA,
                0x6E,
                0x96,
                0x26
            )
            MF_MSE_OPUS_SUPPORT = EXTERN_GUID(
                0x4D224CC1,
                0x8CC4,
                0x48A3,
                0xA7,
                0xA7,
                0xE4,
                0xC1,
                0x6C,
                0xE6,
                0x38,
                0x8A
            )


            class MF_MSE_VP9_SUPPORT_TYPE(ENUM):
                MF_MSE_VP9_SUPPORT_DEFAULT = 0
                MF_MSE_VP9_SUPPORT_ON = 1
                MF_MSE_VP9_SUPPORT_OFF = 2


            class MF_MSE_OPUS_SUPPORT_TYPE(ENUM):
                MF_MSE_OPUS_SUPPORT_ON = 0
                MF_MSE_OPUS_SUPPORT_OFF = 1

            if not defined(__IMFMediaSourceExtensionNotify_INTERFACE_DEFINED__):
                # interface IMFMediaSourceExtensionNotify
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaSourceExtensionNotify = MIDL_INTERFACE(
                        "{A7901327-05DD-4469-A7B7-0E01979E361D}"
                    )
                    IMFMediaSourceExtensionNotify._iid_ = IID_IMFMediaSourceExtensionNotify

                    IMFMediaSourceExtensionNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnSourceOpen')],
                            VOID,
                            'OnSourceOpen',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnSourceEnded')],
                            VOID,
                            'OnSourceEnded',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnSourceClose')],
                            VOID,
                            'OnSourceClose',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaSourceExtensionNotify_INTERFACE_DEFINED__

            if not defined(__IMFBufferListNotify_INTERFACE_DEFINED__):
                # interface IMFBufferListNotify
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFBufferListNotify = MIDL_INTERFACE(
                        "{24CD47F7-81D8-4785-ADB2-AF697A963CD2}"
                    )
                    IMFBufferListNotify._iid_ = IID_IMFBufferListNotify

                    IMFBufferListNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnAddSourceBuffer')],
                            VOID,
                            'OnAddSourceBuffer',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnRemoveSourceBuffer')],
                            VOID,
                            'OnRemoveSourceBuffer',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFBufferListNotify_INTERFACE_DEFINED__

            if not defined(__IMFSourceBufferNotify_INTERFACE_DEFINED__):
                # interface IMFSourceBufferNotify
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSourceBufferNotify = MIDL_INTERFACE(
                        "{87E47623-2CEB-45D6-9B88-D8520C4DCBBC}"
                    )
                    IMFSourceBufferNotify._iid_ = IID_IMFSourceBufferNotify

                    IMFSourceBufferNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnUpdateStart')],
                            VOID,
                            'OnUpdateStart',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnAbort')],
                            VOID,
                            'OnAbort',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnError')],
                            VOID,
                            'OnError',
                            (['in'], HRESULT, 'hr'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnUpdate')],
                            VOID,
                            'OnUpdate',
                        ),
                        COMMETHOD(
                            [helpstring('Method OnUpdateEnd')],
                            VOID,
                            'OnUpdateEnd',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSourceBufferNotify_INTERFACE_DEFINED__

            if not defined(__IMFSourceBuffer_INTERFACE_DEFINED__):
                # interface IMFSourceBuffer
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSourceBuffer = MIDL_INTERFACE(
                        "{E2CD3A4B-AF25-4D3D-9110-DA0E6F8EE877}"
                    )
                    IMFSourceBuffer._iid_ = IID_IMFSourceBuffer

                    IMFSourceBuffer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetUpdating')],
                            BOOL,
                            'GetUpdating',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBuffered')],
                            HRESULT,
                            'GetBuffered',
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaTimeRange)),
                               'ppBuffered'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetTimeStampOffset')],
                            DOUBLE,
                            'GetTimeStampOffset',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetTimeStampOffset')],
                            HRESULT,
                            'SetTimeStampOffset',
                            (['in'], DOUBLE, 'offset'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAppendWindowStart')],
                            DOUBLE,
                            'GetAppendWindowStart',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetAppendWindowStart')],
                            HRESULT,
                            'SetAppendWindowStart',
                            (['in'], DOUBLE, 'time'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAppendWindowEnd')],
                            DOUBLE,
                            'GetAppendWindowEnd',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetAppendWindowEnd')],
                            HRESULT,
                            'SetAppendWindowEnd',
                            (['in'], DOUBLE, 'time'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Append')],
                            HRESULT,
                            'Append',
                            (['in'], POINTER(BYTE), 'pData'),
                            (['in'], DWORD, 'len'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AppendByteStream')],
                            HRESULT,
                            'AppendByteStream',
                            (['in'], POINTER(IMFByteStream), 'pStream'),
                            (['in'], POINTER(DWORDLONG), 'pMaxLen'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Abort')],
                            HRESULT,
                            'Abort',
                        ),
                        COMMETHOD(
                            [helpstring('Method Remove')],
                            HRESULT,
                            'Remove',
                            (['in'], DOUBLE, 'start'),
                            (['in'], DOUBLE, 'end'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSourceBuffer_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0015
            # [local]
            if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
                class MF_MSE_APPEND_MODE(ENUM):
                    MF_MSE_APPEND_MODE_SEGMENTS = 0
                    MF_MSE_APPEND_MODE_SEQUENCE = 1

                if not defined(__IMFSourceBufferAppendMode_INTERFACE_DEFINED__):
                    # interface IMFSourceBufferAppendMode
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFSourceBufferAppendMode = MIDL_INTERFACE(
                            "{19666FB4-BABE-4C55-BC03-0A074DA37E2A}"
                        )
                        IMFSourceBufferAppendMode._iid_ = IID_IMFSourceBufferAppendMode

                        IMFSourceBufferAppendMode._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetAppendMode')],
                                MF_MSE_APPEND_MODE,
                                'GetAppendMode',
                            ),
                            COMMETHOD(
                                [helpstring('Method SetAppendMode')],
                                HRESULT,
                                'SetAppendMode',
                                (['in'], MF_MSE_APPEND_MODE, 'mode'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFSourceBufferAppendMode_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfmediaengine_0000_0016
                # [local]
            # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

            if not defined(__IMFSourceBufferList_INTERFACE_DEFINED__):
                # interface IMFSourceBufferList
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSourceBufferList = MIDL_INTERFACE(
                        "{249981F8-8325-41F3-B80C-3B9E3AAD0CBE}"
                    )
                    IMFSourceBufferList._iid_ = IID_IMFSourceBufferList

                    IMFSourceBufferList._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetLength')],
                            DWORD,
                            'GetLength',
                        ),
                        COMMETHOD(
                            [helpstring('Method *GetSourceBuffer')],
                            IMFSourceBuffer,
                            '*GetSourceBuffer',
                            (['in'], DWORD, 'index'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSourceBufferList_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0017
            # [local]
            class MF_MSE_READY(ENUM):
                MF_MSE_READY_CLOSED = 1
                MF_MSE_READY_OPEN = 2
                MF_MSE_READY_ENDED = 3


            class MF_MSE_ERROR(ENUM):
                MF_MSE_ERROR_NOERROR = 0
                MF_MSE_ERROR_NETWORK = 1
                MF_MSE_ERROR_DECODE = 2
                MF_MSE_ERROR_UNKNOWN_ERROR = 3

            if not defined(__IMFMediaSourceExtension_INTERFACE_DEFINED__):
                # interface IMFMediaSourceExtension
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaSourceExtension = MIDL_INTERFACE(
                        "{E467B94E-A713-4562-A802-816A42E9008A}"
                    )
                    IMFMediaSourceExtension._iid_ = IID_IMFMediaSourceExtension

                    IMFMediaSourceExtension._methods_ = [
                        COMMETHOD(
                            [helpstring('Method *GetSourceBuffers')],
                            IMFSourceBufferList,
                            '*GetSourceBuffers',
                        ),
                        COMMETHOD(
                            [helpstring('Method *GetActiveSourceBuffers')],
                            IMFSourceBufferList,
                            '*GetActiveSourceBuffers',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetReadyState')],
                            MF_MSE_READY,
                            'GetReadyState',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDuration')],
                            DOUBLE,
                            'GetDuration',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetDuration')],
                            HRESULT,
                            'SetDuration',
                            (['in'], DOUBLE, 'duration'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddSourceBuffer')],
                            HRESULT,
                            'AddSourceBuffer',
                            (['in'], BSTR, 'type'),
                            (
                                ['in'],
                                POINTER(IMFSourceBufferNotify),
                                'pNotify'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFSourceBuffer)),
                                'ppSourceBuffer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveSourceBuffer')],
                            HRESULT,
                            'RemoveSourceBuffer',
                            (
                                ['in'],
                                POINTER(IMFSourceBuffer),
                                'pSourceBuffer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetEndOfStream')],
                            HRESULT,
                            'SetEndOfStream',
                            (['in'], MF_MSE_ERROR, 'error'),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsTypeSupported')],
                            BOOL,
                            'IsTypeSupported',
                            (['in'], BSTR, 'type'),
                        ),
                        COMMETHOD(
                            [helpstring('Method *GetSourceBuffer')],
                            IMFSourceBuffer,
                            '*GetSourceBuffer',
                            (['in'], DWORD, 'dwStreamIndex'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaSourceExtension_INTERFACE_DEFINED__

            if not defined(__IMFMediaSourceExtensionLiveSeekableRange_INTERFACE_DEFINED__):
                # interface IMFMediaSourceExtensionLiveSeekableRange
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaSourceExtensionLiveSeekableRange = MIDL_INTERFACE(
                        "{5D1ABFD6-450A-4D92-9EFC-D6B6CBC1F4DA}"
                    )
                    IMFMediaSourceExtensionLiveSeekableRange._iid_ = IID_IMFMediaSourceExtensionLiveSeekableRange

                    IMFMediaSourceExtensionLiveSeekableRange._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetLiveSeekableRange')],
                            HRESULT,
                            'SetLiveSeekableRange',
                            (['in'], DOUBLE, 'start'),
                            (['in'], DOUBLE, 'end'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ClearLiveSeekableRange')],
                            HRESULT,
                            'ClearLiveSeekableRange',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaSourceExtensionLiveSeekableRange_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0019
            # [local]
            if not defined(__IMFMediaEngineEME_INTERFACE_DEFINED__):
                # interface IMFMediaEngineEME
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineEME = MIDL_INTERFACE(
                        "{50DC93E4-BA4F-4275-AE66-83E836E57469}"
                    )
                    IMFMediaEngineEME._iid_ = IID_IMFMediaEngineEME

                    IMFMediaEngineEME._methods_ = [
                        COMMETHOD(
                            [helpstring('Method get_Keys')],
                            HRESULT,
                            'get_Keys',
                            (['out'], POINTER(POINTER(IMFMediaKeys)), 'keys'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetMediaKeys')],
                            HRESULT,
                            'SetMediaKeys',
                            (['in'], POINTER(IMFMediaKeys), 'keys'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineEME_INTERFACE_DEFINED__

            if not defined(__IMFMediaEngineSrcElementsEx_INTERFACE_DEFINED__):
                # interface IMFMediaEngineSrcElementsEx
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineSrcElementsEx = MIDL_INTERFACE(
                        "{654A6BB3-E1A3-424A-9908-53A43A0DFDA0}"
                    )
                    IMFMediaEngineSrcElementsEx._iid_ = IID_IMFMediaEngineSrcElementsEx

                    IMFMediaEngineSrcElementsEx._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddElementEx')],
                            HRESULT,
                            'AddElementEx',
                            (['in'], BSTR, 'pURL'),
                            (['in'], BSTR, 'pType'),
                            (['in'], BSTR, 'pMedia'),
                            (['in'], BSTR, 'keySystem'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetKeySystem')],
                            HRESULT,
                            'GetKeySystem',
                            (['in'], DWORD, 'index'),
                            (['out'], POINTER(BSTR), 'pType'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineSrcElementsEx_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0021
            # [local]
            MF_MEDIA_ENGINE_NEEDKEY_CALLBACK = EXTERN_GUID(
                0x7EA80843,
                0xB6E4,
                0x432C,
                0x8E,
                0xA4,
                0x78,
                0x48,
                0xFF,
                0xE4,
                0x22,
                0x0E
            )
            if not defined(__IMFMediaEngineNeedKeyNotify_INTERFACE_DEFINED__):
                # interface IMFMediaEngineNeedKeyNotify
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineNeedKeyNotify = MIDL_INTERFACE(
                        "{46A30204-A696-4B18-8804-246B8F031BB1}"
                    )
                    IMFMediaEngineNeedKeyNotify._iid_ = IID_IMFMediaEngineNeedKeyNotify

                    IMFMediaEngineNeedKeyNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method NeedKey')],
                            VOID,
                            'NeedKey',
                            (['in'], POINTER(BYTE), 'initData'),
                            (['in'], DWORD, 'cb'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineNeedKeyNotify_INTERFACE_DEFINED__

            if not defined(__IMFMediaKeys_INTERFACE_DEFINED__):
                # interface IMFMediaKeys
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaKeys = MIDL_INTERFACE(
                        "{5CB31C05-61FF-418F-AFDA-CAAF41421A38}"
                    )
                    IMFMediaKeys._iid_ = IID_IMFMediaKeys

                    IMFMediaKeys._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateSession')],
                            HRESULT,
                            'CreateSession',
                            (['in'], BSTR, 'mimeType'),
                            (['in'], POINTER(BYTE), 'initData'),
                            (['in'], DWORD, 'cb'),
                            (['in'], POINTER(BYTE), 'customData'),
                            (['in'], DWORD, 'cbCustomData'),
                            (
                                ['in'],
                                POINTER(IMFMediaKeySessionNotify),
                                'notify'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaKeySession)),
                                'ppSession'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method get_KeySystem')],
                            HRESULT,
                            'get_KeySystem',
                            (['out'], POINTER(BSTR), 'keySystem'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Shutdown')],
                            HRESULT,
                            'Shutdown',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSuspendNotify')],
                            HRESULT,
                            'GetSuspendNotify',
                            (
                                ['out'],
                                POINTER(POINTER(IMFCdmSuspendNotify)),
                                'notify'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaKeys_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0023
            # [local]
            class _MF_MEDIA_ENGINE_KEYERR(ENUM):
                MF_MEDIAENGINE_KEYERR_UNKNOWN = 1
                MF_MEDIAENGINE_KEYERR_CLIENT = 2
                MF_MEDIAENGINE_KEYERR_SERVICE = 3
                MF_MEDIAENGINE_KEYERR_OUTPUT = 4
                MF_MEDIAENGINE_KEYERR_HARDWARECHANGE = 5
                MF_MEDIAENGINE_KEYERR_DOMAIN = 6

            MF_MEDIA_ENGINE_KEYERR = _MF_MEDIA_ENGINE_KEYERR
            if not defined(__IMFMediaKeySession_INTERFACE_DEFINED__):
                # interface IMFMediaKeySession
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaKeySession = MIDL_INTERFACE(
                        "{24FA67D5-D1D0-4DC5-995C-C0EFDC191FB5}"
                    )
                    IMFMediaKeySession._iid_ = IID_IMFMediaKeySession

                    IMFMediaKeySession._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetError')],
                            HRESULT,
                            'GetError',
                            (['out'], POINTER(USHORT), 'code'),
                            (['out'], POINTER(DWORD), 'systemCode'),
                        ),
                        COMMETHOD(
                            [helpstring('Method get_KeySystem')],
                            HRESULT,
                            'get_KeySystem',
                            (['out'], POINTER(BSTR), 'keySystem'),
                        ),
                        COMMETHOD(
                            [helpstring('Method get_SessionId')],
                            HRESULT,
                            'get_SessionId',
                            (['out'], POINTER(BSTR), 'sessionId'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Update')],
                            HRESULT,
                            'Update',
                            (['in'], POINTER(BYTE), 'key'),
                            (['in'], DWORD, 'cb'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Close')],
                            HRESULT,
                            'Close',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaKeySession_INTERFACE_DEFINED__

            if not defined(__IMFMediaKeySessionNotify_INTERFACE_DEFINED__):
                # interface IMFMediaKeySessionNotify
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaKeySessionNotify = MIDL_INTERFACE(
                        "{6A0083F9-8947-4C1D-9CE0-CDEE22B23135}"
                    )
                    IMFMediaKeySessionNotify._iid_ = IID_IMFMediaKeySessionNotify

                    IMFMediaKeySessionNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method KeyMessage')],
                            VOID,
                            'KeyMessage',
                            (['in'], BSTR, 'destinationURL'),
                            (['in'], POINTER(BYTE), 'message'),
                            (['in'], DWORD, 'cb'),
                        ),
                        COMMETHOD(
                            [helpstring('Method KeyAdded')],
                            VOID,
                            'KeyAdded',
                        ),
                        COMMETHOD(
                            [helpstring('Method KeyError')],
                            VOID,
                            'KeyError',
                            (['in'], USHORT, 'code'),
                            (['in'], DWORD, 'systemCode'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaKeySessionNotify_INTERFACE_DEFINED__

            if not defined(__IMFCdmSuspendNotify_INTERFACE_DEFINED__):
                # interface IMFCdmSuspendNotify
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCdmSuspendNotify = MIDL_INTERFACE(
                        "{7A5645D2-43BD-47FD-87B7-DCD24CC7D692}"
                    )
                    IMFCdmSuspendNotify._iid_ = IID_IMFCdmSuspendNotify

                    IMFCdmSuspendNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Begin')],
                            HRESULT,
                            'Begin',
                        ),
                        COMMETHOD(
                            [helpstring('Method End')],
                            HRESULT,
                            'End',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFCdmSuspendNotify_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0026
            # [local]
            class _MF_HDCP_STATUS(ENUM):
                MF_HDCP_STATUS_ON = 0
                MF_HDCP_STATUS_OFF = 1
                MF_HDCP_STATUS_ON_WITH_TYPE_ENFORCEMENT = 2

            MF_HDCP_STATUS = _MF_HDCP_STATUS
            if not defined(__IMFHDCPStatus_INTERFACE_DEFINED__):
                # interface IMFHDCPStatus
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFHDCPStatus = MIDL_INTERFACE(
                        "{DE400F54-5BF1-40CF-8964-0BEA136B1E3D}"
                    )
                    IMFHDCPStatus._iid_ = IID_IMFHDCPStatus

                    IMFHDCPStatus._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Query')],
                            HRESULT,
                            'Query',
                            (
                                ['out', 'in'],
                                POINTER(MF_HDCP_STATUS),
                                'pStatus'
                            ),
                            (['out', 'in'], POINTER(BOOL), 'pfStatus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Set')],
                            HRESULT,
                            'Set',
                            (['in'], MF_HDCP_STATUS, 'status'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFHDCPStatus_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0027
            # [local]
            class MF_MEDIA_ENGINE_OPM_STATUS(ENUM):
                MF_MEDIA_ENGINE_OPM_NOT_REQUESTED = 0
                MF_MEDIA_ENGINE_OPM_ESTABLISHED = 1
                MF_MEDIA_ENGINE_OPM_FAILED_VM = 2
                MF_MEDIA_ENGINE_OPM_FAILED_BDA = 3
                MF_MEDIA_ENGINE_OPM_FAILED_UNSIGNED_DRIVER = 4
                MF_MEDIA_ENGINE_OPM_FAILED = 5

            if not defined(__IMFMediaEngineOPMInfo_INTERFACE_DEFINED__):
                # interface IMFMediaEngineOPMInfo
                # [local][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineOPMInfo = MIDL_INTERFACE(
                        "{765763E6-6C01-4B01-BB0F-B829F60ED28C}"
                    )
                    IMFMediaEngineOPMInfo._iid_ = IID_IMFMediaEngineOPMInfo

                    IMFMediaEngineOPMInfo._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetOPMInfo')],
                            HRESULT,
                            'GetOPMInfo',
                            (
                                ['out'],
                                POINTER(MF_MEDIA_ENGINE_OPM_STATUS),
                                'pStatus'
                            ),
                            (['out'], POINTER(BOOL), 'pConstricted'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineOPMInfo_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0028
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if not defined(NO_MEDIA_ENGINE_FACTORY):
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
                MF_MEDIA_ENGINE_CALLBACK = EXTERN_GUID(
                    0xC60381B8,
                    0x83A4,
                    0x41F8,
                    0xA3,
                    0xD0,
                    0xDE,
                    0x05,
                    0x07,
                    0x68,
                    0x49,
                    0xA9
                )
                MF_MEDIA_ENGINE_DXGI_MANAGER = EXTERN_GUID(
                    0x065702DA,
                    0x1094,
                    0x486D,
                    0x86,
                    0x17,
                    0xEE,
                    0x7C,
                    0xC4,
                    0xEE,
                    0x46,
                    0x48
                )
                MF_MEDIA_ENGINE_EXTENSION = EXTERN_GUID(
                    0x3109FD46,
                    0x060D,
                    0x4B62,
                    0x8D,
                    0xCF,
                    0xFA,
                    0xFF,
                    0x81,
                    0x13,
                    0x18,
                    0xD2
                )
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                MF_MEDIA_ENGINE_PLAYBACK_HWND = EXTERN_GUID(
                    0xD988879B,
                    0x67C9,
                    0x4D92,
                    0xBA,
                    0xA7,
                    0x6E,
                    0xAD,
                    0xD4,
                    0x46,
                    0x03,
                    0x9D
                )
                MF_MEDIA_ENGINE_OPM_HWND = EXTERN_GUID(
                    0xA0BE8EE7,
                    0x0572,
                    0x4F2C,
                    0xA8,
                    0x01,
                    0x2A,
                    0x15,
                    0x1B,
                    0xD3,
                    0xE7,
                    0x26
                )
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
                MF_MEDIA_ENGINE_PLAYBACK_VISUAL = EXTERN_GUID(
                    0x6DEBD26F,
                    0x6AB9,
                    0x4D7E,
                    0xB0,
                    0xEE,
                    0xC6,
                    0x1A,
                    0x73,
                    0xFF,
                    0xAD,
                    0x15
                )
                MF_MEDIA_ENGINE_COREWINDOW = EXTERN_GUID(
                    0xFCCAE4DC,
                    0x0B7F,
                    0x41C2,
                    0x9F,
                    0x96,
                    0x46,
                    0x59,
                    0x94,
                    0x8A,
                    0xCD,
                    0xDC
                )
                MF_MEDIA_ENGINE_VIDEO_OUTPUT_FORMAT = EXTERN_GUID(
                    0x5066893C,
                    0x8CF9,
                    0x42BC,
                    0x8B,
                    0x8A,
                    0x47,
                    0x22,
                    0x12,
                    0xE5,
                    0x27,
                    0x26
                )
                MF_MEDIA_ENGINE_CONTENT_PROTECTION_FLAGS = EXTERN_GUID(
                    0xE0350223,
                    0x5AAF,
                    0x4D76,
                    0xA7,
                    0xC3,
                    0x06,
                    0xDE,
                    0x70,
                    0x89,
                    0x4D,
                    0xB4
                )
                MF_MEDIA_ENGINE_CONTENT_PROTECTION_MANAGER = EXTERN_GUID(
                    0xFDD6DFAA,
                    0xBD85,
                    0x4AF3,
                    0x9E,
                    0x0F,
                    0xA0,
                    0x1D,
                    0x53,
                    0x9D,
                    0x87,
                    0x6A
                )
                MF_MEDIA_ENGINE_AUDIO_ENDPOINT_ROLE = EXTERN_GUID(
                    0xD2CB93D1,
                    0x116A,
                    0x44F2,
                    0x93,
                    0x85,
                    0xF7,
                    0xD0,
                    0xFD,
                    0xA2,
                    0xFB,
                    0x46
                )
                MF_MEDIA_ENGINE_AUDIO_CATEGORY = EXTERN_GUID(
                    0xC8D4C51D,
                    0x350E,
                    0x41F2,
                    0xBA,
                    0x46,
                    0xFA,
                    0xEB,
                    0xBB,
                    0x08,
                    0x57,
                    0xF6
                )
                MF_MEDIA_ENGINE_STREAM_CONTAINS_ALPHA_CHANNEL = EXTERN_GUID(
                    0x5CBFAF44,
                    0xD2B2,
                    0x4CFB,
                    0x80,
                    0xA7,
                    0xD4,
                    0x29,
                    0xC7,
                    0x4C,
                    0x78,
                    0x9D
                )
                MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE = EXTERN_GUID(
                    0x4E0212E2,
                    0xE18F,
                    0x41E1,
                    0x95,
                    0xE5,
                    0xC0,
                    0xE7,
                    0xE9,
                    0x23,
                    0x5B,
                    0xC3
                )
                MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE9 = EXTERN_GUID(
                    0x052C2D39,
                    0x40C0,
                    0x4188,
                    0xAB,
                    0x86,
                    0xF8,
                    0x28,
                    0x27,
                    0x3B,
                    0x75,
                    0x22
                )
                MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE10 = EXTERN_GUID(
                    0x11A47AFD,
                    0x6589,
                    0x4124,
                    0xB3,
                    0x12,
                    0x61,
                    0x58,
                    0xEC,
                    0x51,
                    0x7F,
                    0xC3
                )
                MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE11 = EXTERN_GUID(
                    0x1CF1315F,
                    0xCE3F,
                    0x4035,
                    0x93,
                    0x91,
                    0x16,
                    0x14,
                    0x2F,
                    0x77,
                    0x51,
                    0x89
                )
                if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
                    MF_MEDIA_ENGINE_BROWSER_COMPATIBILITY_MODE_IE_EDGE = EXTERN_GUID(
                        0xA6F3E465,
                        0x3ACA,
                        0x442C,
                        0xA3,
                        0xF0,
                        0xAD,
                        0x6D,
                        0xDA,
                        0xD8,
                        0x39,
                        0xAE
                    )
                    MF_MEDIA_ENGINE_COMPATIBILITY_MODE = EXTERN_GUID(
                        0x3EF26AD4,
                        0xDC54,
                        0x45DE,
                        0xB9,
                        0xAF,
                        0x76,
                        0xC8,
                        0xC6,
                        0x6B,
                        0xFA,
                        0x8E
                    )
                    MF_MEDIA_ENGINE_COMPATIBILITY_MODE_WWA_EDGE = EXTERN_GUID(
                        0x15B29098,
                        0x9F01,
                        0x4E4D,
                        0xB6,
                        0x5A,
                        0xC0,
                        0x6C,
                        0x6C,
                        0x89,
                        0xDA,
                        0x2A
                    )
                    MF_MEDIA_ENGINE_COMPATIBILITY_MODE_WIN10 = EXTERN_GUID(
                        0x5B25E089,
                        0x6CA7,
                        0x4139,
                        0xA2,
                        0xCB,
                        0xFC,
                        0xAA,
                        0xB3,
                        0x95,
                        0x52,
                        0xA3
                    )
                # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

                MF_MEDIA_ENGINE_SOURCE_RESOLVER_CONFIG_STORE = EXTERN_GUID(
                    0x0AC0C497,
                    0xB3C4,
                    0x48C9,
                    0x9C,
                    0xDE,
                    0xBB,
                    0x8C,
                    0xA2,
                    0x44,
                    0x2C,
                    0xA3
                )
                MF_MEDIA_ENGINE_TRACK_ID = EXTERN_GUID(
                    0x65BEA312,
                    0x4043,
                    0x4815,
                    0x8E,
                    0xAB,
                    0x44,
                    0xDC,
                    0xE2,
                    0xEF,
                    0x8F,
                    0x2A
                )
                MF_MEDIA_ENGINE_TELEMETRY_APPLICATION_ID = EXTERN_GUID(
                    0x1E7B273B,
                    0xA7E4,
                    0x402A,
                    0x8F,
                    0x51,
                    0xC4,
                    0x8E,
                    0x88,
                    0xA2,
                    0xCA,
                    0xBC
                )
                MF_MEDIA_ENGINE_SYNCHRONOUS_CLOSE = EXTERN_GUID(
                    0xC3C2E12F,
                    0x7E0E,
                    0x4E43,
                    0xB9,
                    0x1C,
                    0xDC,
                    0x99,
                    0x2C,
                    0xCD,
                    0xFA,
                    0x5E
                )
                MF_MEDIA_ENGINE_MEDIA_PLAYER_MODE = EXTERN_GUID(
                    0x3DDD8D45,
                    0x5AA1,
                    0x4112,
                    0x82,
                    0xE5,
                    0x36,
                    0xF6,
                    0xA2,
                    0x19,
                    0x7E,
                    0x6E
                )


                class MF_MEDIA_ENGINE_CREATEFLAGS(ENUM):
                    MF_MEDIA_ENGINE_AUDIOONLY = 0x1
                    MF_MEDIA_ENGINE_WAITFORSTABLE_STATE = 0x2
                    MF_MEDIA_ENGINE_FORCEMUTE = 0x4
                    MF_MEDIA_ENGINE_REAL_TIME_MODE = 0x8
                    MF_MEDIA_ENGINE_DISABLE_LOCAL_PLUGINS = 0x10
                    MF_MEDIA_ENGINE_CREATEFLAGS_MASK = 0x1F


                class MF_MEDIA_ENGINE_PROTECTION_FLAGS(ENUM):
                    MF_MEDIA_ENGINE_ENABLE_PROTECTED_CONTENT = 1
                    MF_MEDIA_ENGINE_USE_PMP_FOR_ALL_CONTENT = 2
                    MF_MEDIA_ENGINE_USE_UNPROTECTED_PMP = 4

                if not defined(__IMFMediaEngineClassFactory_INTERFACE_DEFINED__):
                    # interface IMFMediaEngineClassFactory
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFMediaEngineClassFactory = MIDL_INTERFACE(
                            "{4D645ACE-26AA-4688-9BE1-DF3516990B93}"
                        )
                        IMFMediaEngineClassFactory._iid_ = IID_IMFMediaEngineClassFactory

                        IMFMediaEngineClassFactory._methods_ = [
                            COMMETHOD(
                                [helpstring('Method CreateInstance')],
                                HRESULT,
                                'CreateInstance',
                                (['in'], DWORD, 'dwFlags'),
                                (['in'], POINTER(IMFAttributes), 'pAttr'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaEngine)),
                                    'ppPlayer'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method CreateTimeRange')],
                                HRESULT,
                                'CreateTimeRange',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaTimeRange)),
                                    'ppTimeRange'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method CreateError')],
                                HRESULT,
                                'CreateError',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaError)),
                                    'ppError'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFMediaEngineClassFactory_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfmediaengine_0000_0029
                # [local]
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                if not defined(__IMFMediaEngineClassFactoryEx_INTERFACE_DEFINED__):
                    # interface IMFMediaEngineClassFactoryEx
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFMediaEngineClassFactoryEx = MIDL_INTERFACE(
                            "{C56156C6-EA5B-48A5-9DF8-FBE035D0929E}"
                        )
                        IMFMediaEngineClassFactoryEx._iid_ = IID_IMFMediaEngineClassFactoryEx

                        IMFMediaEngineClassFactoryEx._methods_ = [
                            COMMETHOD(
                                [helpstring('Method CreateMediaSourceExtension')],
                                HRESULT,
                                'CreateMediaSourceExtension',
                                (['in'], DWORD, 'dwFlags'),
                                (['in'], POINTER(IMFAttributes), 'pAttr'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaSourceExtension)),
                                    'ppMSE'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method CreateMediaKeys')],
                                HRESULT,
                                'CreateMediaKeys',
                                (['in'], BSTR, 'keySystem'),
                                (['in'], BSTR, 'cdmStorePath'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaKeys)),
                                    'ppKeys'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method IsTypeSupported')],
                                HRESULT,
                                'IsTypeSupported',
                                (['in'], BSTR, 'type'),
                                (['in'], BSTR, 'keySystem'),
                                (['out'], POINTER(BOOL), 'isSupported'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFMediaEngineClassFactoryEx_INTERFACE_DEFINED__

                if not defined(__IMFMediaEngineClassFactory2_INTERFACE_DEFINED__):
                    # interface IMFMediaEngineClassFactory2
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFMediaEngineClassFactory2 = MIDL_INTERFACE(
                            "{09083CEF-867F-4BF6-8776-DEE3A7B42FCA}"
                        )
                        IMFMediaEngineClassFactory2._iid_ = IID_IMFMediaEngineClassFactory2

                        IMFMediaEngineClassFactory2._methods_ = [
                            COMMETHOD(
                                [helpstring('Method CreateMediaKeys2')],
                                HRESULT,
                                'CreateMediaKeys2',
                                (['in'], BSTR, 'keySystem'),
                                (['in'], BSTR, 'defaultCdmStorePath'),
                                (['in'], BSTR, 'inprivateCdmStorePath'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaKeys)),
                                    'ppKeys'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFMediaEngineClassFactory2_INTERFACE_DEFINED__

                if not defined(__IMFExtendedDRMTypeSupport_INTERFACE_DEFINED__):
                    # interface IMFExtendedDRMTypeSupport
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFExtendedDRMTypeSupport = MIDL_INTERFACE(
                            "{332EC562-3758-468D-A784-E38F23552128}"
                        )
                        IMFExtendedDRMTypeSupport._iid_ = IID_IMFExtendedDRMTypeSupport

                        IMFExtendedDRMTypeSupport._methods_ = [
                            COMMETHOD(
                                [helpstring('Method IsTypeSupportedEx')],
                                HRESULT,
                                'IsTypeSupportedEx',
                                (['in'], BSTR, 'type'),
                                (['in'], BSTR, 'keySystem'),
                                (
                                    ['out'],
                                    POINTER(MF_MEDIA_ENGINE_CANPLAY),
                                    'pAnswer'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFExtendedDRMTypeSupport_INTERFACE_DEFINED__

                if not defined(__IMFMediaEngineSupportsSourceTransfer_INTERFACE_DEFINED__):
                    # interface IMFMediaEngineSupportsSourceTransfer
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFMediaEngineSupportsSourceTransfer = MIDL_INTERFACE(
                            "{A724B056-1B2E-4642-A6F3-DB9420C52908}"
                        )
                        IMFMediaEngineSupportsSourceTransfer._iid_ = IID_IMFMediaEngineSupportsSourceTransfer

                        IMFMediaEngineSupportsSourceTransfer._methods_ = [
                            COMMETHOD(
                                [helpstring('Method ShouldTransferSource')],
                                HRESULT,
                                'ShouldTransferSource',
                                (['out'], POINTER(BOOL), 'pfShouldTransfer'),
                            ),
                            COMMETHOD(
                                [helpstring('Method DetachMediaSource')],
                                HRESULT,
                                'DetachMediaSource',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFByteStream)),
                                    'ppByteStream'
                                ),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaSource)),
                                    'ppMediaSource'
                                ),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFMediaSourceExtension)),
                                    'ppMSE'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method AttachMediaSource')],
                                HRESULT,
                                'AttachMediaSource',
                                (
                                    ['in'],
                                    POINTER(IMFByteStream),
                                    'pByteStream'
                                ),
                                (
                                    ['in'],
                                    POINTER(IMFMediaSource),
                                    'pMediaSource'
                                ),
                                (
                                    ['in'],
                                    POINTER(IMFMediaSourceExtension),
                                    'pMSE'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFMediaEngineSupportsSourceTransfer_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfmediaengine_0000_0033
                # [local]
                if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
                    if not defined(__IMFMediaEngineTransferSource_INTERFACE_DEFINED__):
                        # interface IMFMediaEngineTransferSource
                        # [local][unique][uuid][object]
                        if defined(__cplusplus) and not defined(CINTERFACE):
                            pass
                        else:
                            IID_IMFMediaEngineTransferSource = MIDL_INTERFACE(
                                "{24230452-FE54-40CC-94F3-FCC394C340D6}"
                            )
                            IMFMediaEngineTransferSource._iid_ = IID_IMFMediaEngineTransferSource

                            IMFMediaEngineTransferSource._methods_ = [
                                COMMETHOD(
                                    [helpstring('Method TransferSourceToMediaEngine')],
                                    HRESULT,
                                    'TransferSourceToMediaEngine',
                                    (
                                        ['in'],
                                        POINTER(IMFMediaEngine),
                                        'destination'
                                    ),
                                ),
                            ]

                        # END IF  C style interface
                    # END IF  __IMFMediaEngineTransferSource_INTERFACE_DEFINED__

                    # interface __MIDL_itf_mfmediaengine_0000_0034
                    # [local]
                # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
                CLSID_MFMediaEngineClassFactory = EXTERN_GUID(
                    0xB44392DA,
                    0x499B,
                    0x446B,
                    0xA4,
                    0xCB,
                    0x0,
                    0x5F,
                    0xEA,
                    0xD0,
                    0xE6,
                    0xD5
                )
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
        # END IF   (NO_MEDIA_ENGINE_FACTORY)

        if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                MF_MEDIA_ENGINE_TIMEDTEXT = EXTERN_GUID(
                    0x805EA411,
                    0x92E0,
                    0x4E59,
                    0x9B,
                    0x6E,
                    0x5C,
                    0x7D,
                    0x79,
                    0x15,
                    0xE6,
                    0x4F
                )


                class MF_TIMED_TEXT_TRACK_KIND(ENUM):
                    MF_TIMED_TEXT_TRACK_KIND_UNKNOWN = 0
                    MF_TIMED_TEXT_TRACK_KIND_SUBTITLES = 1
                    MF_TIMED_TEXT_TRACK_KIND_CAPTIONS = 2
                    MF_TIMED_TEXT_TRACK_KIND_METADATA = 3


                class MF_TIMED_TEXT_UNIT_TYPE(ENUM):
                    MF_TIMED_TEXT_UNIT_TYPE_PIXELS = 0
                    MF_TIMED_TEXT_UNIT_TYPE_PERCENTAGE = 1


                class MF_TIMED_TEXT_FONT_STYLE(ENUM):
                    MF_TIMED_TEXT_FONT_STYLE_NORMAL = 0
                    MF_TIMED_TEXT_FONT_STYLE_OBLIQUE = 1
                    MF_TIMED_TEXT_FONT_STYLE_ITALIC = 2


                class MF_TIMED_TEXT_ALIGNMENT(ENUM):
                    MF_TIMED_TEXT_ALIGNMENT_START = 0
                    MF_TIMED_TEXT_ALIGNMENT_END = 1
                    MF_TIMED_TEXT_ALIGNMENT_CENTER = 2


                class MF_TIMED_TEXT_DISPLAY_ALIGNMENT(ENUM):
                    MF_TIMED_TEXT_DISPLAY_ALIGNMENT_BEFORE = 0
                    MF_TIMED_TEXT_DISPLAY_ALIGNMENT_AFTER = 1
                    MF_TIMED_TEXT_DISPLAY_ALIGNMENT_CENTER = 2


                class MF_TIMED_TEXT_DECORATION(ENUM):
                    MF_TIMED_TEXT_DECORATION_NONE = 0
                    MF_TIMED_TEXT_DECORATION_UNDERLINE = 1
                    MF_TIMED_TEXT_DECORATION_LINE_THROUGH = 2
                    MF_TIMED_TEXT_DECORATION_OVERLINE = 4


                class MF_TIMED_TEXT_WRITING_MODE(ENUM):
                    MF_TIMED_TEXT_WRITING_MODE_LRTB = 0
                    MF_TIMED_TEXT_WRITING_MODE_RLTB = 1
                    MF_TIMED_TEXT_WRITING_MODE_TBRL = 2
                    MF_TIMED_TEXT_WRITING_MODE_TBLR = 3
                    MF_TIMED_TEXT_WRITING_MODE_LR = 4
                    MF_TIMED_TEXT_WRITING_MODE_RL = 5
                    MF_TIMED_TEXT_WRITING_MODE_TB = 6


                class MF_TIMED_TEXT_SCROLL_MODE(ENUM):
                    MF_TIMED_TEXT_SCROLL_MODE_POP_ON = 0
                    MF_TIMED_TEXT_SCROLL_MODE_ROLL_UP = 1


                class MF_TIMED_TEXT_ERROR_CODE(ENUM):
                    MF_TIMED_TEXT_ERROR_CODE_NOERROR = 0
                    MF_TIMED_TEXT_ERROR_CODE_FATAL = 1
                    MF_TIMED_TEXT_ERROR_CODE_DATA_FORMAT = 2
                    MF_TIMED_TEXT_ERROR_CODE_NETWORK = 3
                    MF_TIMED_TEXT_ERROR_CODE_INTERNAL = 4


                class MF_TIMED_TEXT_CUE_EVENT(ENUM):
                    MF_TIMED_TEXT_CUE_EVENT_ACTIVE = 0
                    MF_TIMED_TEXT_CUE_EVENT_INACTIVE = (
                        MF_TIMED_TEXT_CUE_EVENT_ACTIVE + 1
                    )
                    MF_TIMED_TEXT_CUE_EVENT_CLEAR = (
                        MF_TIMED_TEXT_CUE_EVENT_INACTIVE + 1
                    )


                class MF_TIMED_TEXT_TRACK_READY_STATE(ENUM):
                    MF_TIMED_TEXT_TRACK_READY_STATE_NONE = 0
                    MF_TIMED_TEXT_TRACK_READY_STATE_LOADING = (
                        MF_TIMED_TEXT_TRACK_READY_STATE_NONE + 1
                    )
                    MF_TIMED_TEXT_TRACK_READY_STATE_LOADED = (
                        MF_TIMED_TEXT_TRACK_READY_STATE_LOADING + 1
                    )
                    MF_TIMED_TEXT_TRACK_READY_STATE_ERROR = (
                        MF_TIMED_TEXT_TRACK_READY_STATE_LOADED + 1
                    )
                if not defined(__IMFTimedText_INTERFACE_DEFINED__):
                    # interface IMFTimedText
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedText = MIDL_INTERFACE(
                            "{1F2A94C9-A3DF-430D-9D0F-ACD85DDC29AF}"
                        )
                        IMFTimedText._iid_ = IID_IMFTimedText

                        IMFTimedText._methods_ = [
                            COMMETHOD(
                                [helpstring('Method RegisterNotifications')],
                                HRESULT,
                                'RegisterNotifications',
                                (
                                    ['in'],
                                    POINTER(IMFTimedTextNotify),
                                    'notify'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method SelectTrack')],
                                HRESULT,
                                'SelectTrack',
                                (['in'], DWORD, 'trackId'),
                                (['in'], BOOL, 'selected'),
                            ),
                            COMMETHOD(
                                [helpstring('Method AddDataSource')],
                                HRESULT,
                                'AddDataSource',
                                (
                                    ['in'],
                                    POINTER(IMFByteStream),
                                    'byteStream'
                                ),
                                (['in'], LPCWSTR, 'label'),
                                (['in'], LPCWSTR, 'language'),
                                (['in'], MF_TIMED_TEXT_TRACK_KIND, 'kind'),
                                (['in'], BOOL, 'isDefault'),
                                (['out'], POINTER(DWORD), 'trackId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method AddDataSourceFromUrl')],
                                HRESULT,
                                'AddDataSourceFromUrl',
                                (['in'], LPCWSTR, 'url'),
                                (['in'], LPCWSTR, 'label'),
                                (['in'], LPCWSTR, 'language'),
                                (['in'], MF_TIMED_TEXT_TRACK_KIND, 'kind'),
                                (['in'], BOOL, 'isDefault'),
                                (['out'], POINTER(DWORD), 'trackId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method AddTrack')],
                                HRESULT,
                                'AddTrack',
                                (['in'], LPCWSTR, 'label'),
                                (['in'], LPCWSTR, 'language'),
                                (['in'], MF_TIMED_TEXT_TRACK_KIND, 'kind'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextTrack)),
                                    'track'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method RemoveTrack')],
                                HRESULT,
                                'RemoveTrack',
                                (['in'], POINTER(IMFTimedTextTrack), 'track'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetCueTimeOffset')],
                                HRESULT,
                                'GetCueTimeOffset',
                                (['out'], POINTER(DOUBLE), 'offset'),
                            ),
                            COMMETHOD(
                                [helpstring('Method SetCueTimeOffset')],
                                HRESULT,
                                'SetCueTimeOffset',
                                (['in'], DOUBLE, 'offset'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTracks')],
                                HRESULT,
                                'GetTracks',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextTrackList)),
                                    'tracks'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetActiveTracks')],
                                HRESULT,
                                'GetActiveTracks',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextTrackList)),
                                    'activeTracks'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTextTracks')],
                                HRESULT,
                                'GetTextTracks',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextTrackList)),
                                    'textTracks'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetMetadataTracks')],
                                HRESULT,
                                'GetMetadataTracks',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextTrackList)),
                                    'metadataTracks'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method SetInBandEnabled')],
                                HRESULT,
                                'SetInBandEnabled',
                                (['in'], BOOL, 'enabled'),
                            ),
                            COMMETHOD(
                                [helpstring('Method IsInBandEnabled')],
                                BOOL,
                                'IsInBandEnabled',
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedText_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextNotify_INTERFACE_DEFINED__):
                    # interface IMFTimedTextNotify
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextNotify = MIDL_INTERFACE(
                            "{DF6B87B6-CE12-45DB-ABA7-432FE054E57D}"
                        )
                        IMFTimedTextNotify._iid_ = IID_IMFTimedTextNotify

                        IMFTimedTextNotify._methods_ = [
                            COMMETHOD(
                                [helpstring('Method TrackAdded')],
                                VOID,
                                'TrackAdded',
                                (['in'], DWORD, 'trackId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method TrackRemoved')],
                                VOID,
                                'TrackRemoved',
                                (['in'], DWORD, 'trackId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method TrackSelected')],
                                VOID,
                                'TrackSelected',
                                (['in'], DWORD, 'trackId'),
                                (['in'], BOOL, 'selected'),
                            ),
                            COMMETHOD(
                                [helpstring('Method TrackReadyStateChanged')],
                                VOID,
                                'TrackReadyStateChanged',
                                (['in'], DWORD, 'trackId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method Error')],
                                VOID,
                                'Error',
                                (
                                    ['in'],
                                    MF_TIMED_TEXT_ERROR_CODE,
                                    'errorCode'
                                ),
                                (['in'], HRESULT, 'extendedErrorCode'),
                                (['in'], DWORD, 'sourceTrackId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method Cue')],
                                VOID,
                                'Cue',
                                (['in'], MF_TIMED_TEXT_CUE_EVENT, 'cueEvent'),
                                (['in'], DOUBLE, 'currentTime'),
                                (['in'], POINTER(IMFTimedTextCue), 'cue'),
                            ),
                            COMMETHOD(
                                [helpstring('Method Reset')],
                                VOID,
                                'Reset',
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextNotify_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextTrack_INTERFACE_DEFINED__):
                    # interface IMFTimedTextTrack
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextTrack = MIDL_INTERFACE(
                            "{8822C32D-654E-4233-BF21-D7F2E67D30D4}"
                        )
                        IMFTimedTextTrack._iid_ = IID_IMFTimedTextTrack

                        IMFTimedTextTrack._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetId')],
                                DWORD,
                                'GetId',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetLabel')],
                                HRESULT,
                                'GetLabel',
                                (['out'], POINTER(LPWSTR), 'label'),
                            ),
                            COMMETHOD(
                                [helpstring('Method SetLabel')],
                                HRESULT,
                                'SetLabel',
                                (['in'], LPCWSTR, 'label'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetLanguage')],
                                HRESULT,
                                'GetLanguage',
                                (['out'], POINTER(LPWSTR), 'language'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTrackKind')],
                                MF_TIMED_TEXT_TRACK_KIND,
                                'GetTrackKind',
                            ),
                            COMMETHOD(
                                [helpstring('Method IsInBand')],
                                BOOL,
                                'IsInBand',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetInBandMetadataTrackDispatchType')],
                                HRESULT,
                                'GetInBandMetadataTrackDispatchType',
                                (['out'], POINTER(LPWSTR), 'dispatchType'),
                            ),
                            COMMETHOD(
                                [helpstring('Method IsActive')],
                                BOOL,
                                'IsActive',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetErrorCode')],
                                MF_TIMED_TEXT_ERROR_CODE,
                                'GetErrorCode',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetExtendedErrorCode')],
                                HRESULT,
                                'GetExtendedErrorCode',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetDataFormat')],
                                HRESULT,
                                'GetDataFormat',
                                (['out'], POINTER(GUID), 'format'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetReadyState')],
                                MF_TIMED_TEXT_TRACK_READY_STATE,
                                'GetReadyState',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetCueList')],
                                HRESULT,
                                'GetCueList',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextCueList)),
                                    'cues'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextTrack_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextTrackList_INTERFACE_DEFINED__):
                    # interface IMFTimedTextTrackList
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextTrackList = MIDL_INTERFACE(
                            "{23FF334C-442C-445F-BCCC-EDC438AA11E2}"
                        )
                        IMFTimedTextTrackList._iid_ = IID_IMFTimedTextTrackList

                        IMFTimedTextTrackList._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetLength')],
                                DWORD,
                                'GetLength',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTrack')],
                                HRESULT,
                                'GetTrack',
                                (['in'], DWORD, 'index'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextTrack)),
                                   'track'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTrackById')],
                                HRESULT,
                                'GetTrackById',
                                (['in'], DWORD, 'trackId'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextTrack)),
                                    'track'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextTrackList_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextCue_INTERFACE_DEFINED__):
                    # interface IMFTimedTextCue
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextCue = MIDL_INTERFACE(
                            "{1E560447-9A2B-43E1-A94C-B0AAABFBFBC9}"
                        )
                        IMFTimedTextCue._iid_ = IID_IMFTimedTextCue

                        IMFTimedTextCue._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetId')],
                                DWORD,
                                'GetId',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetOriginalId')],
                                HRESULT,
                                'GetOriginalId',
                                (['out'], POINTER(LPWSTR), 'originalId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetCueKind')],
                                MF_TIMED_TEXT_TRACK_KIND,
                                'GetCueKind',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetStartTime')],
                                DOUBLE,
                                'GetStartTime',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetDuration')],
                                DOUBLE,
                                'GetDuration',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTrackId')],
                                DWORD,
                                'GetTrackId',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetData')],
                                HRESULT,
                                'GetData',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextBinary)),
                                    'data'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetRegion')],
                                HRESULT,
                                'GetRegion',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextRegion)),
                                    'region'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetStyle')],
                                HRESULT,
                                'GetStyle',
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextStyle)),
                                    'style'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetLineCount')],
                                DWORD,
                                'GetLineCount',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetLine')],
                                HRESULT,
                                'GetLine',
                                (['in'], DWORD, 'index'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextFormattedText)),
                                    'line'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextCue_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextFormattedText_INTERFACE_DEFINED__):
                    # interface IMFTimedTextFormattedText
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextFormattedText = MIDL_INTERFACE(
                            "{E13AF3C1-4D47-4354-B1F5-E83AE0ECAE60}"
                        )
                        IMFTimedTextFormattedText._iid_ = IID_IMFTimedTextFormattedText

                        IMFTimedTextFormattedText._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetText')],
                                HRESULT,
                                'GetText',
                                (['out'], POINTER(LPWSTR), 'text'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetSubformattingCount')],
                                DWORD,
                                'GetSubformattingCount',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetSubformatting')],
                                HRESULT,
                                'GetSubformatting',
                                (['in'], DWORD, 'index'),
                                (['out'], POINTER(DWORD), 'firstChar'),
                                (['out'], POINTER(DWORD), 'charLength'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextStyle)),
                                    'style'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextFormattedText_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextStyle_INTERFACE_DEFINED__):
                    # interface IMFTimedTextStyle
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextStyle = MIDL_INTERFACE(
                            "{09B2455D-B834-4F01-A347-9052E21C450E}"
                        )
                        IMFTimedTextStyle._iid_ = IID_IMFTimedTextStyle

                        IMFTimedTextStyle._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetName')],
                                HRESULT,
                                'GetName',
                                (['out'], POINTER(LPWSTR), 'name'),
                            ),
                            COMMETHOD(
                                [helpstring('Method IsExternal')],
                                BOOL,
                                'IsExternal',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetFontFamily')],
                                HRESULT,
                                'GetFontFamily',
                                (['out'], POINTER(LPWSTR), 'fontFamily'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetFontSize')],
                                HRESULT,
                                'GetFontSize',
                                (['out'], POINTER(DOUBLE), 'fontSize'),
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_UNIT_TYPE),
                                    'unitType'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetColor')],
                                HRESULT,
                                'GetColor',
                                (['out'], POINTER(MFARGB), 'color'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetBackgroundColor')],
                                HRESULT,
                                'GetBackgroundColor',
                                (['out'], POINTER(MFARGB), 'bgColor'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetShowBackgroundAlways')],
                                HRESULT,
                                'GetShowBackgroundAlways',
                                (
                                    ['out'],
                                    POINTER(BOOL),
                                    'showBackgroundAlways'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetFontStyle')],
                                HRESULT,
                                'GetFontStyle',
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_FONT_STYLE),
                                    'fontStyle'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetBold')],
                                HRESULT,
                                'GetBold',
                                (['out'], POINTER(BOOL), 'bold'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetRightToLeft')],
                                HRESULT,
                                'GetRightToLeft',
                                (['out'], POINTER(BOOL), 'rightToLeft'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTextAlignment')],
                                HRESULT,
                                'GetTextAlignment',
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_ALIGNMENT),
                                    'textAlign'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTextDecoration')],
                                HRESULT,
                                'GetTextDecoration',
                                (['out'], POINTER(DWORD), 'textDecoration'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetTextOutline')],
                                HRESULT,
                                'GetTextOutline',
                                (['out'], POINTER(MFARGB), 'color'),
                                (['out'], POINTER(DOUBLE), 'thickness'),
                                (['out'], POINTER(DOUBLE), 'blurRadius'),
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_UNIT_TYPE),
                                    'unitType'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextStyle_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextRegion_INTERFACE_DEFINED__):
                    # interface IMFTimedTextRegion
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextRegion = MIDL_INTERFACE(
                            "{C8D22AFC-BC47-4BDF-9B04-787E49CE3F58}"
                        )
                        IMFTimedTextRegion._iid_ = IID_IMFTimedTextRegion

                        IMFTimedTextRegion._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetName')],
                                HRESULT,
                                'GetName',
                                (['out'], POINTER(LPWSTR), 'name'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetPosition')],
                                HRESULT,
                                'GetPosition',
                                (['out'], POINTER(DOUBLE), 'pX'),
                                (['out'], POINTER(DOUBLE), 'pY'),
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_UNIT_TYPE),
                                    'unitType'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetExtent')],
                                HRESULT,
                                'GetExtent',
                                (['out'], POINTER(DOUBLE), 'pWidth'),
                                (['out'], POINTER(DOUBLE), 'pHeight'),
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_UNIT_TYPE),
                                    'unitType'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetBackgroundColor')],
                                HRESULT,
                                'GetBackgroundColor',
                                (['out'], POINTER(MFARGB), 'bgColor'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetWritingMode')],
                                HRESULT,
                                'GetWritingMode',
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_WRITING_MODE),
                                    'writingMode'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetDisplayAlignment')],
                                HRESULT,
                                'GetDisplayAlignment',
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_DISPLAY_ALIGNMENT),
                                    'displayAlign'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetLineHeight')],
                                HRESULT,
                                'GetLineHeight',
                                (['out'], POINTER(DOUBLE), 'pLineHeight'),
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_UNIT_TYPE),
                                    'unitType'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetClipOverflow')],
                                HRESULT,
                                'GetClipOverflow',
                                (['out'], POINTER(BOOL), 'clipOverflow'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetPadding')],
                                HRESULT,
                                'GetPadding',
                                (['out'], POINTER(DOUBLE), 'before'),
                                (['out'], POINTER(DOUBLE), 'start'),
                                (['out'], POINTER(DOUBLE), 'after'),
                                (['out'], POINTER(DOUBLE), 'end'),
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_UNIT_TYPE),
                                    'unitType'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetWrap')],
                                HRESULT,
                                'GetWrap',
                                (['out'], POINTER(BOOL), 'wrap'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetZIndex')],
                                HRESULT,
                                'GetZIndex',
                                (['out'], POINTER(INT32), 'zIndex'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetScrollMode')],
                                HRESULT,
                                'GetScrollMode',
                                (
                                    ['out'],
                                    POINTER(MF_TIMED_TEXT_SCROLL_MODE),
                                    'scrollMode'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextRegion_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextBinary_INTERFACE_DEFINED__):
                    # interface IMFTimedTextBinary
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextBinary = MIDL_INTERFACE(
                            "{4AE3A412-0545-43C4-BF6F-6B97A5C6C432}"
                        )
                        IMFTimedTextBinary._iid_ = IID_IMFTimedTextBinary

                        IMFTimedTextBinary._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetData')],
                                HRESULT,
                                'GetData',
                                (['out'], POINTER(POINTER(BYTE)), 'data'),
                                (['out'], POINTER(DWORD), 'length'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextBinary_INTERFACE_DEFINED__

                if not defined(__IMFTimedTextCueList_INTERFACE_DEFINED__):
                    # interface IMFTimedTextCueList
                    # [local][unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFTimedTextCueList = MIDL_INTERFACE(
                            "{AD128745-211B-40A0-9981-FE65F166D0FD}"
                        )
                        IMFTimedTextCueList._iid_ = IID_IMFTimedTextCueList

                        IMFTimedTextCueList._methods_ = [
                            COMMETHOD(
                                [helpstring('Method GetLength')],
                                DWORD,
                                'GetLength',
                            ),
                            COMMETHOD(
                                [helpstring('Method GetCueByIndex')],
                                HRESULT,
                                'GetCueByIndex',
                                (['in'], DWORD, 'index'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextCue)),
                                    'cue'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetCueById')],
                                HRESULT,
                                'GetCueById',
                                (['in'], DWORD, 'id'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextCue)),
                                    'cue'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetCueByOriginalId')],
                                HRESULT,
                                'GetCueByOriginalId',
                                (['in'], LPCWSTR, 'originalId'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextCue)),
                                    'cue'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method AddTextCue')],
                                HRESULT,
                                'AddTextCue',
                                (['in'], DOUBLE, 'start'),
                                (['in'], DOUBLE, 'duration'),
                                (['in'], LPCWSTR, 'text'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextCue)),
                                    'cue'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method AddDataCue')],
                                HRESULT,
                                'AddDataCue',
                                (['in'], DOUBLE, 'start'),
                                (['in'], DOUBLE, 'duration'),
                                (['in'], POINTER(BYTE), 'data'),
                                (['in'], DWORD, 'dataSize'),
                                (
                                    ['out'],
                                    POINTER(POINTER(IMFTimedTextCue)),
                                    'cue'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method RemoveCue')],
                                HRESULT,
                                'RemoveCue',
                                (['in'], POINTER(IMFTimedTextCue), 'cue'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFTimedTextCueList_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfmediaengine_0000_0044
                # [local]
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
        # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        MF_MEDIA_ENGINE_CONTINUE_ON_CODEC_ERROR = EXTERN_GUID(
            0xDBCDB7F9,
            0x48E4,
            0x4295,
            0xB7,
            0x0D,
            0xD5,
            0x18,
            0x23,
            0x4E,
            0xEB,
            0x38
        )


        class MF_MEDIA_ENGINE_STREAMTYPE_FAILED(ENUM):
            MF_MEDIA_ENGINE_STREAMTYPE_FAILED_UNKNOWN = 0
            MF_MEDIA_ENGINE_STREAMTYPE_FAILED_AUDIO = 1
            MF_MEDIA_ENGINE_STREAMTYPE_FAILED_VIDEO = 2

    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
            MF_MEDIA_ENGINE_EME_CALLBACK = EXTERN_GUID(
                0x494553A7,
                0xA481,
                0x4CB7,
                0xBE,
                0xC5,
                0x38,
                0x09,
                0x03,
                0x51,
                0x37,
                0x31
            )
            if not defined(__IMFMediaEngineEMENotify_INTERFACE_DEFINED__):
                # interface IMFMediaEngineEMENotify
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineEMENotify = MIDL_INTERFACE(
                        "{9E184D15-CDB7-4F86-B49E-566689F4A601}"
                    )
                    IMFMediaEngineEMENotify._iid_ = IID_IMFMediaEngineEMENotify

                    IMFMediaEngineEMENotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Encrypted')],
                            VOID,
                            'Encrypted',
                            (['in'], POINTER(BYTE), 'pbInitData'),
                            (['in'], DWORD, 'cb'),
                            (['in'], BSTR, 'bstrInitDataType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method WaitingForKey')],
                            VOID,
                            'WaitingForKey',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineEMENotify_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0045
            # [local]
            class MF_MEDIAKEYS_REQUIREMENT(ENUM):
                MF_MEDIAKEYS_REQUIREMENT_REQUIRED = 1
                MF_MEDIAKEYS_REQUIREMENT_OPTIONAL = 2
                MF_MEDIAKEYS_REQUIREMENT_NOT_ALLOWED = 3

            if not defined(__IMFMediaKeySessionNotify2_INTERFACE_DEFINED__):
                # interface IMFMediaKeySessionNotify2
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaKeySessionNotify2 = MIDL_INTERFACE(
                        "{C3A9E92A-DA88-46B0-A110-6CF953026CB9}"
                    )
                    IMFMediaKeySessionNotify2._iid_ = IID_IMFMediaKeySessionNotify2

                    IMFMediaKeySessionNotify2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method KeyMessage2')],
                            VOID,
                            'KeyMessage2',
                            (
                                ['in'],
                                MF_MEDIAKEYSESSION_MESSAGETYPE,
                                'eMessageType'
                            ),
                            (['in'], BSTR, 'destinationURL'),
                            (['in'], POINTER(BYTE), 'pbMessage'),
                            (['in'], DWORD, 'cbMessage'),
                        ),
                        COMMETHOD(
                            [helpstring('Method KeyStatusChange')],
                            VOID,
                            'KeyStatusChange',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaKeySessionNotify2_INTERFACE_DEFINED__

            if not defined(__IMFMediaKeySystemAccess_INTERFACE_DEFINED__):
                # interface IMFMediaKeySystemAccess
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaKeySystemAccess = MIDL_INTERFACE(
                        "{AEC63FDA-7A97-4944-B35C-6C6DF8085CC3}"
                    )
                    IMFMediaKeySystemAccess._iid_ = IID_IMFMediaKeySystemAccess

                    IMFMediaKeySystemAccess._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateMediaKeys')],
                            HRESULT,
                            'CreateMediaKeys',
                            (
                                ['in'],
                                POINTER(IPropertyStore),
                                'pCdmCustomConfig'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaKeys2)),
                                'ppKeys'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method get_SupportedConfiguration')],
                            HRESULT,
                            'get_SupportedConfiguration',
                            (
                                ['out'],
                                POINTER(POINTER(IPropertyStore)),
                                'ppSupportedConfiguration'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method get_KeySystem')],
                            HRESULT,
                            'get_KeySystem',
                            (['out'], POINTER(BSTR), 'pKeySystem'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaKeySystemAccess_INTERFACE_DEFINED__

            if not defined(__IMFMediaEngineClassFactory3_INTERFACE_DEFINED__):
                # interface IMFMediaEngineClassFactory3
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaEngineClassFactory3 = MIDL_INTERFACE(
                        "{3787614F-65F7-4003-B673-EAD8293A0E60}"
                    )
                    IMFMediaEngineClassFactory3._iid_ = IID_IMFMediaEngineClassFactory3

                    IMFMediaEngineClassFactory3._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateMediaKeySystemAccess')],
                            HRESULT,
                            'CreateMediaKeySystemAccess',
                            (['in'], BSTR, 'keySystem'),
                            (
                                ['in'],
                                POINTER(POINTER(IPropertyStore)),
                                'ppSupportedConfigurationsArray'
                            ),
                            (['in'], UINT, 'uSize'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaKeySystemAccess)),
                                'ppKeyAccess'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaEngineClassFactory3_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0048
            # [local]
            if not defined(__IMFMediaKeys2_INTERFACE_DEFINED__):
                # interface IMFMediaKeys2
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaKeys2 = MIDL_INTERFACE(
                        "{45892507-AD66-4DE2-83A2-ACBB13CD8D43}"
                    )
                    IMFMediaKeys2._iid_ = IID_IMFMediaKeys2

                    IMFMediaKeys2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateSession2')],
                            HRESULT,
                            'CreateSession2',
                            (['in'], MF_MEDIAKEYSESSION_TYPE, 'eSessionType'),
                            (
                                ['in'],
                                POINTER(IMFMediaKeySessionNotify2),
                                'pMFMediaKeySessionNotify2'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaKeySession2)),
                                'ppSession'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetServerCertificate')],
                            HRESULT,
                            'SetServerCertificate',
                            (['in'], POINTER(BYTE), 'pbServerCertificate'),
                            (['in'], DWORD, 'cb'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDOMException')],
                            HRESULT,
                            'GetDOMException',
                            (['in'], HRESULT, 'systemCode'),
                            (['out'], POINTER(HRESULT), 'code'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaKeys2_INTERFACE_DEFINED__

            if not defined(__IMFMediaKeySession2_INTERFACE_DEFINED__):
                # interface IMFMediaKeySession2
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaKeySession2 = MIDL_INTERFACE(
                        "{E9707E05-6D55-4636-B185-3DE21210BD75}"
                    )
                    IMFMediaKeySession2._iid_ = IID_IMFMediaKeySession2

                    IMFMediaKeySession2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method get_KeyStatuses')],
                            HRESULT,
                            'get_KeyStatuses',
                            (
                                ['out'],
                                POINTER(POINTER(MFMediaKeyStatus)),
                                'pKeyStatusesArray'
                            ),
                            (['out'], POINTER(UINT), 'puSize'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Load')],
                            HRESULT,
                            'Load',
                            (['in'], BSTR, 'bstrSessionId'),
                            (['out'], POINTER(BOOL), 'pfLoaded'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GenerateRequest')],
                            HRESULT,
                            'GenerateRequest',
                            (['in'], BSTR, 'initDataType'),
                            (['in'], POINTER(BYTE), 'pbInitData'),
                            (['in'], DWORD, 'cb'),
                        ),
                        COMMETHOD(
                            [helpstring('Method get_Expiration')],
                            HRESULT,
                            'get_Expiration',
                            (['out'], POINTER(DOUBLE), 'dblExpiration'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Remove')],
                            HRESULT,
                            'Remove',
                        ),
                        COMMETHOD(
                            [helpstring('Method Shutdown')],
                            HRESULT,
                            'Shutdown',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaKeySession2_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmediaengine_0000_0050
            # [local]
        # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


