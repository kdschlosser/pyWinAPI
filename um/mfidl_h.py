import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__mfidl_h__ = None
__IMFMediaSession_FWD_DEFINED__ = None
__IMFSourceResolver_FWD_DEFINED__ = None
__IMFMediaSource_FWD_DEFINED__ = None
__IMFMediaSourceEx_FWD_DEFINED__ = None
__IMFClockConsumer_FWD_DEFINED__ = None
__IMFMediaStream_FWD_DEFINED__ = None
__IMFMediaSink_FWD_DEFINED__ = None
__IMFStreamSink_FWD_DEFINED__ = None
__IMFVideoSampleAllocator_FWD_DEFINED__ = None
__IMFVideoSampleAllocatorNotify_FWD_DEFINED__ = None
__IMFVideoSampleAllocatorNotifyEx_FWD_DEFINED__ = None
__IMFVideoSampleAllocatorCallback_FWD_DEFINED__ = None
__IMFVideoSampleAllocatorEx_FWD_DEFINED__ = None
__IMFDXGIDeviceManagerSource_FWD_DEFINED__ = None
__IMFVideoProcessorControl_FWD_DEFINED__ = None
__IMFVideoProcessorControl2_FWD_DEFINED__ = None
__IMFVideoProcessorControl3_FWD_DEFINED__ = None
__IMFTopology_FWD_DEFINED__ = None
__IMFTopologyNode_FWD_DEFINED__ = None
__IMFGetService_FWD_DEFINED__ = None
__IMFClock_FWD_DEFINED__ = None
__IMFPresentationClock_FWD_DEFINED__ = None
__IMFPresentationTimeSource_FWD_DEFINED__ = None
__IMFClockStateSink_FWD_DEFINED__ = None
__IMFPresentationDescriptor_FWD_DEFINED__ = None
__IMFStreamDescriptor_FWD_DEFINED__ = None
__IMFMediaTypeHandler_FWD_DEFINED__ = None
__IMFTimer_FWD_DEFINED__ = None
__IMFShutdown_FWD_DEFINED__ = None
__IMFTopoLoader_FWD_DEFINED__ = None
__IMFContentProtectionManager_FWD_DEFINED__ = None
__IMFContentEnabler_FWD_DEFINED__ = None
__IMFMetadata_FWD_DEFINED__ = None
__IMFMetadataProvider_FWD_DEFINED__ = None
__IMFRateSupport_FWD_DEFINED__ = None
__IMFRateControl_FWD_DEFINED__ = None
__IMFTimecodeTranslate_FWD_DEFINED__ = None
__IMFSeekInfo_FWD_DEFINED__ = None
__IMFSimpleAudioVolume_FWD_DEFINED__ = None
__IMFAudioStreamVolume_FWD_DEFINED__ = None
__IMFAudioPolicy_FWD_DEFINED__ = None
__IMFSampleGrabberSinkCallback_FWD_DEFINED__ = None
__IMFSampleGrabberSinkCallback2_FWD_DEFINED__ = None
__IMFWorkQueueServices_FWD_DEFINED__ = None
__IMFWorkQueueServicesEx_FWD_DEFINED__ = None
__IMFQualityManager_FWD_DEFINED__ = None
__IMFQualityAdvise_FWD_DEFINED__ = None
__IMFQualityAdvise2_FWD_DEFINED__ = None
__IMFQualityAdviseLimits_FWD_DEFINED__ = None
__IMFRealTimeClient_FWD_DEFINED__ = None
__IMFRealTimeClientEx_FWD_DEFINED__ = None
__IMFSequencerSource_FWD_DEFINED__ = None
__IMFMediaSourceTopologyProvider_FWD_DEFINED__ = None
__IMFMediaSourcePresentationProvider_FWD_DEFINED__ = None
__IMFTopologyNodeAttributeEditor_FWD_DEFINED__ = None
__IMFByteStreamBuffering_FWD_DEFINED__ = None
__IMFByteStreamCacheControl_FWD_DEFINED__ = None
__IMFByteStreamTimeSeek_FWD_DEFINED__ = None
__IMFByteStreamCacheControl2_FWD_DEFINED__ = None
__IMFNetCredential_FWD_DEFINED__ = None
__IMFNetCredentialManager_FWD_DEFINED__ = None
__IMFNetCredentialCache_FWD_DEFINED__ = None
__IMFSSLCertificateManager_FWD_DEFINED__ = None
__IMFNetResourceFilter_FWD_DEFINED__ = None
__IMFSourceOpenMonitor_FWD_DEFINED__ = None
__IMFNetProxyLocator_FWD_DEFINED__ = None
__IMFNetProxyLocatorFactory_FWD_DEFINED__ = None
__IMFSaveJob_FWD_DEFINED__ = None
__IMFNetSchemeHandlerConfig_FWD_DEFINED__ = None
__IMFSchemeHandler_FWD_DEFINED__ = None
__IMFByteStreamHandler_FWD_DEFINED__ = None
__IMFTrustedInput_FWD_DEFINED__ = None
__IMFInputTrustAuthority_FWD_DEFINED__ = None
__IMFTrustedOutput_FWD_DEFINED__ = None
__IMFOutputTrustAuthority_FWD_DEFINED__ = None
__IMFOutputPolicy_FWD_DEFINED__ = None
__IMFOutputSchema_FWD_DEFINED__ = None
__IMFSecureChannel_FWD_DEFINED__ = None
__IMFSampleProtection_FWD_DEFINED__ = None
__IMFMediaSinkPreroll_FWD_DEFINED__ = None
__IMFFinalizableMediaSink_FWD_DEFINED__ = None
__IMFStreamingSinkConfig_FWD_DEFINED__ = None
__IMFRemoteProxy_FWD_DEFINED__ = None
__IMFObjectReferenceStream_FWD_DEFINED__ = None
__IMFPMPHost_FWD_DEFINED__ = None
__IMFPMPClient_FWD_DEFINED__ = None
__IMFPMPServer_FWD_DEFINED__ = None
__IMFRemoteDesktopPlugin_FWD_DEFINED__ = None
__IMFSAMIStyle_FWD_DEFINED__ = None
__IMFTranscodeProfile_FWD_DEFINED__ = None
__IMFTranscodeSinkInfoProvider_FWD_DEFINED__ = None
__IMFFieldOfUseMFTUnlock_FWD_DEFINED__ = None
__IMFLocalMFTRegistration_FWD_DEFINED__ = None
__IMFCapturePhotoConfirmation_FWD_DEFINED__ = None
__IMFPMPHostApp_FWD_DEFINED__ = None
__IMFPMPClientApp_FWD_DEFINED__ = None
__IMFMediaStreamSourceSampleRequest_FWD_DEFINED__ = None
__IMFTrackedSample_FWD_DEFINED__ = None
__IMFProtectedEnvironmentAccess_FWD_DEFINED__ = None
__IMFSignedLibrary_FWD_DEFINED__ = None
__IMFSystemId_FWD_DEFINED__ = None
__IMFContentProtectionDevice_FWD_DEFINED__ = None
__IMFContentDecryptorContext_FWD_DEFINED__ = None
__IMFNetCrossOriginSupport_FWD_DEFINED__ = None
__IMFHttpDownloadRequest_FWD_DEFINED__ = None
__IMFHttpDownloadSession_FWD_DEFINED__ = None
__IMFHttpDownloadSessionProvider_FWD_DEFINED__ = None
__IMFMediaSource2_FWD_DEFINED__ = None
__IMFMediaStream2_FWD_DEFINED__ = None
__IMFSensorDevice_FWD_DEFINED__ = None
__IMFSensorGroup_FWD_DEFINED__ = None
__IMFSensorStream_FWD_DEFINED__ = None
__IMFSensorTransformFactory_FWD_DEFINED__ = None
__IMFSensorProfile_FWD_DEFINED__ = None
__IMFSensorProfileCollection_FWD_DEFINED__ = None
__IMFSensorProcessActivity_FWD_DEFINED__ = None
__IMFSensorActivityReport_FWD_DEFINED__ = None
__IMFSensorActivitiesReport_FWD_DEFINED__ = None
__IMFSensorActivitiesReportCallback_FWD_DEFINED__ = None
__IMFSensorActivityMonitor_FWD_DEFINED__ = None
__IMFMediaSession_INTERFACE_DEFINED__ = None
__IMFSourceResolver_INTERFACE_DEFINED__ = None
__IMFMediaSource_INTERFACE_DEFINED__ = None
__IMFMediaSourceEx_INTERFACE_DEFINED__ = None
__IMFClockConsumer_INTERFACE_DEFINED__ = None
__IMFMediaStream_INTERFACE_DEFINED__ = None
__IMFMediaSink_INTERFACE_DEFINED__ = None
__IMFStreamSink_INTERFACE_DEFINED__ = None
__IMFVideoSampleAllocator_INTERFACE_DEFINED__ = None
__IMFVideoSampleAllocatorNotify_INTERFACE_DEFINED__ = None
__IMFVideoSampleAllocatorNotifyEx_INTERFACE_DEFINED__ = None
__IMFVideoSampleAllocatorCallback_INTERFACE_DEFINED__ = None
__IMFVideoSampleAllocatorEx_INTERFACE_DEFINED__ = None
__IMFDXGIDeviceManagerSource_INTERFACE_DEFINED__ = None
__IMFVideoProcessorControl_INTERFACE_DEFINED__ = None
__IMFVideoProcessorControl2_INTERFACE_DEFINED__ = None
__IMFVideoProcessorControl3_INTERFACE_DEFINED__ = None
__IMFTopology_INTERFACE_DEFINED__ = None
__IMFTopologyNode_INTERFACE_DEFINED__ = None
__IMFGetService_INTERFACE_DEFINED__ = None
__IMFClock_INTERFACE_DEFINED__ = None
__IMFPresentationClock_INTERFACE_DEFINED__ = None
__IMFPresentationTimeSource_INTERFACE_DEFINED__ = None
__IMFClockStateSink_INTERFACE_DEFINED__ = None
__IMFPresentationDescriptor_INTERFACE_DEFINED__ = None
__IMFStreamDescriptor_INTERFACE_DEFINED__ = None
__IMFMediaTypeHandler_INTERFACE_DEFINED__ = None
__IMFTimer_INTERFACE_DEFINED__ = None
__IMFShutdown_INTERFACE_DEFINED__ = None
__IMFTopoLoader_INTERFACE_DEFINED__ = None
__IMFContentProtectionManager_INTERFACE_DEFINED__ = None
__IMFContentEnabler_INTERFACE_DEFINED__ = None
MFRR_INFO_VERSION = None
__IMFMetadata_INTERFACE_DEFINED__ = None
__IMFMetadataProvider_INTERFACE_DEFINED__ = None
__IMFRateSupport_INTERFACE_DEFINED__ = None
__IMFRateControl_INTERFACE_DEFINED__ = None
__IMFTimecodeTranslate_INTERFACE_DEFINED__ = None
__IMFSeekInfo_INTERFACE_DEFINED__ = None
__IMFSimpleAudioVolume_INTERFACE_DEFINED__ = None
__IMFAudioStreamVolume_INTERFACE_DEFINED__ = None
__IMFAudioPolicy_INTERFACE_DEFINED__ = None
__IMFSampleGrabberSinkCallback_INTERFACE_DEFINED__ = None
__IMFSampleGrabberSinkCallback2_INTERFACE_DEFINED__ = None
__IMFWorkQueueServices_INTERFACE_DEFINED__ = None
__IMFWorkQueueServicesEx_INTERFACE_DEFINED__ = None
__IMFQualityManager_INTERFACE_DEFINED__ = None
__IMFQualityAdvise_INTERFACE_DEFINED__ = None
__IMFQualityAdvise2_INTERFACE_DEFINED__ = None
__IMFQualityAdviseLimits_INTERFACE_DEFINED__ = None
__IMFRealTimeClient_INTERFACE_DEFINED__ = None
__IMFRealTimeClientEx_INTERFACE_DEFINED__ = None
__IMFSequencerSource_INTERFACE_DEFINED__ = None
__IMFMediaSourceTopologyProvider_INTERFACE_DEFINED__ = None
__IMFMediaSourcePresentationProvider_INTERFACE_DEFINED__ = None
__IMFTopologyNodeAttributeEditor_INTERFACE_DEFINED__ = None
__IMFByteStreamBuffering_INTERFACE_DEFINED__ = None
__IMFByteStreamCacheControl_INTERFACE_DEFINED__ = None
__IMFByteStreamTimeSeek_INTERFACE_DEFINED__ = None
__IMFByteStreamCacheControl2_INTERFACE_DEFINED__ = None
__IMFNetCredential_INTERFACE_DEFINED__ = None
__IMFNetCredentialManager_INTERFACE_DEFINED__ = None
__IMFNetCredentialCache_INTERFACE_DEFINED__ = None
__IMFSSLCertificateManager_INTERFACE_DEFINED__ = None
__IMFNetResourceFilter_INTERFACE_DEFINED__ = None
__IMFSourceOpenMonitor_INTERFACE_DEFINED__ = None
__IMFNetProxyLocator_INTERFACE_DEFINED__ = None
__IMFNetProxyLocatorFactory_INTERFACE_DEFINED__ = None
__IMFSaveJob_INTERFACE_DEFINED__ = None
__IMFNetSchemeHandlerConfig_INTERFACE_DEFINED__ = None
__IMFSchemeHandler_INTERFACE_DEFINED__ = None
__IMFByteStreamHandler_INTERFACE_DEFINED__ = None
__IMFTrustedInput_INTERFACE_DEFINED__ = None
__IMFInputTrustAuthority_INTERFACE_DEFINED__ = None
__IMFTrustedOutput_INTERFACE_DEFINED__ = None
__IMFOutputTrustAuthority_INTERFACE_DEFINED__ = None
__IMFOutputPolicy_INTERFACE_DEFINED__ = None
__IMFOutputSchema_INTERFACE_DEFINED__ = None
__IMFSecureChannel_INTERFACE_DEFINED__ = None
__IMFSampleProtection_INTERFACE_DEFINED__ = None
__IMFMediaSinkPreroll_INTERFACE_DEFINED__ = None
__IMFFinalizableMediaSink_INTERFACE_DEFINED__ = None
__IMFStreamingSinkConfig_INTERFACE_DEFINED__ = None
__IMFRemoteProxy_INTERFACE_DEFINED__ = None
__IMFObjectReferenceStream_INTERFACE_DEFINED__ = None
__IMFPMPHost_INTERFACE_DEFINED__ = None
__IMFPMPClient_INTERFACE_DEFINED__ = None
__IMFPMPServer_INTERFACE_DEFINED__ = None
__IMFRemoteDesktopPlugin_INTERFACE_DEFINED__ = None
__IMFSAMIStyle_INTERFACE_DEFINED__ = None
__IMFTranscodeProfile_INTERFACE_DEFINED__ = None
__IMFTranscodeSinkInfoProvider_INTERFACE_DEFINED__ = None
__IMFFieldOfUseMFTUnlock_INTERFACE_DEFINED__ = None
__IMFLocalMFTRegistration_INTERFACE_DEFINED__ = None
__IMFCapturePhotoConfirmation_INTERFACE_DEFINED__ = None
__IMFPMPHostApp_INTERFACE_DEFINED__ = None
__IMFPMPClientApp_INTERFACE_DEFINED__ = None
__IMFMediaStreamSourceSampleRequest_INTERFACE_DEFINED__ = None
__IMFTrackedSample_INTERFACE_DEFINED__ = None
__IMFProtectedEnvironmentAccess_INTERFACE_DEFINED__ = None
__IMFSignedLibrary_INTERFACE_DEFINED__ = None
__IMFSystemId_INTERFACE_DEFINED__ = None
__IMFContentProtectionDevice_INTERFACE_DEFINED__ = None
__IMFContentDecryptorContext_INTERFACE_DEFINED__ = None
__IMFNetCrossOriginSupport_INTERFACE_DEFINED__ = None
__IMFHttpDownloadRequest_INTERFACE_DEFINED__ = None
__IMFHttpDownloadSession_INTERFACE_DEFINED__ = None
__IMFHttpDownloadSessionProvider_INTERFACE_DEFINED__ = None
__IMFMediaSource2_INTERFACE_DEFINED__ = None
__IMFMediaStream2_INTERFACE_DEFINED__ = None
__IMFSensorDevice_INTERFACE_DEFINED__ = None
__IMFSensorGroup_INTERFACE_DEFINED__ = None
__IMFSensorStream_INTERFACE_DEFINED__ = None
__IMFSensorTransformFactory_INTERFACE_DEFINED__ = None
__IMFSensorProfile_INTERFACE_DEFINED__ = None
__IMFSensorProfileCollection_INTERFACE_DEFINED__ = None
__IMFSensorProcessActivity_INTERFACE_DEFINED__ = None
__IMFSensorActivityReport_INTERFACE_DEFINED__ = None
__IMFSensorActivitiesReport_INTERFACE_DEFINED__ = None
__IMFSensorActivitiesReportCallback_INTERFACE_DEFINED__ = None
__IMFSensorActivityMonitor_INTERFACE_DEFINED__ = None

IID_IMFTopology = MIDL_INTERFACE(
            "{83CF873A-F6DA-4BC8-823F-BACFD55DC433}"
        )


class IMFTopology(IMFAttributes):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IMFTopology



class _MFCLOCK_PROPERTIES(ctypes.Structure):
    pass


MFCLOCK_PROPERTIES = _MFCLOCK_PROPERTIES


class _MFRR_COMPONENT_HASH_INFO(ctypes.Structure):
    pass


MFRR_COMPONENT_HASH_INFO = _MFRR_COMPONENT_HASH_INFO
PMFRR_COMPONENT_HASH_INFO = POINTER(_MFRR_COMPONENT_HASH_INFO)


class _MFRR_COMPONENTS(ctypes.Structure):
    pass


MFRR_COMPONENTS = _MFRR_COMPONENTS
PMFRR_COMPONENTS = POINTER(_MFRR_COMPONENTS)


class _ASFFlatPicture(ctypes.Structure):
    pass


ASF_FLAT_PICTURE = _ASFFlatPicture


class _ASFFlatSynchronisedLyrics(ctypes.Structure):
    pass


ASF_FLAT_SYNCHRONISED_LYRICS = _ASFFlatSynchronisedLyrics


class _MFTOPONODE_ATTRIBUTE_UPDATE(ctypes.Structure):
    pass


MFTOPONODE_ATTRIBUTE_UPDATE = _MFTOPONODE_ATTRIBUTE_UPDATE


class _MF_LEAKY_BUCKET_PAIR(ctypes.Structure):
    pass


MF_LEAKY_BUCKET_PAIR = _MF_LEAKY_BUCKET_PAIR


class _MFBYTESTREAM_BUFFERING_PARAMS(ctypes.Structure):
    pass


MFBYTESTREAM_BUFFERING_PARAMS = _MFBYTESTREAM_BUFFERING_PARAMS


class __MIDL___MIDL_itf_mfidl_0000_0058_0001(ctypes.Structure):
    pass


MF_BYTE_STREAM_CACHE_RANGE = __MIDL___MIDL_itf_mfidl_0000_0058_0001


class _MFNetCredentialManagerGetParam(ctypes.Structure):
    pass


MFNetCredentialManagerGetParam = _MFNetCredentialManagerGetParam


class _MFINPUTTRUSTAUTHORITY_ACTION(ctypes.Structure):
    pass


MFINPUTTRUSTAUTHORITY_ACCESS_ACTION = _MFINPUTTRUSTAUTHORITY_ACTION


class _MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS(ctypes.Structure):
    pass


MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS = _MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS


class _MF_TRANSCODE_SINK_INFO(ctypes.Structure):
    pass


MF_TRANSCODE_SINK_INFO = _MF_TRANSCODE_SINK_INFO


class _MFT_REGISTRATION_INFO(ctypes.Structure):
    pass


MFT_REGISTRATION_INFO = _MFT_REGISTRATION_INFO


class _MFCONTENTPROTECTIONDEVICE_INPUT_DATA(ctypes.Structure):
    pass


MFCONTENTPROTECTIONDEVICE_INPUT_DATA = _MFCONTENTPROTECTIONDEVICE_INPUT_DATA


class _MFCONTENTPROTECTIONDEVICE_OUTPUT_DATA(ctypes.Structure):
    pass


MFCONTENTPROTECTIONDEVICE_OUTPUT_DATA = _MFCONTENTPROTECTIONDEVICE_OUTPUT_DATA


class _MFCONTENTPROTECTIONDEVICE_REALTIMECLIENT_DATA(ctypes.Structure):
    pass


MFCONTENTPROTECTIONDEVICE_REALTIMECLIENT_DATA = _MFCONTENTPROTECTIONDEVICE_REALTIMECLIENT_DATA


class MFMediaKeyStatus(ctypes.Structure):
    pass





class _MF_VIDEO_SPHERICAL_VIEWDIRECTION(ctypes.Structure):
    pass


MF_VIDEO_SPHERICAL_VIEWDIRECTION = _MF_VIDEO_SPHERICAL_VIEWDIRECTION


class __MIDL___MIDL_itf_mfidl_0000_0113_0001(ctypes.Structure):
    pass


SENSORPROFILEID = __MIDL___MIDL_itf_mfidl_0000_0113_0001



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


if not defined(__mfidl_h__):
    # Forward Declarations
    if not defined(__IMFMediaSession_FWD_DEFINED__):
        class IMFMediaSession(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSession_FWD_DEFINED__

    if not defined(__IMFSourceResolver_FWD_DEFINED__):
        class IMFSourceResolver(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceResolver_FWD_DEFINED__

    if not defined(__IMFMediaSource_FWD_DEFINED__):
        class IMFMediaSource(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSource_FWD_DEFINED__

    if not defined(__IMFMediaSourceEx_FWD_DEFINED__):
        class IMFMediaSourceEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSourceEx_FWD_DEFINED__

    if not defined(__IMFClockConsumer_FWD_DEFINED__):
        class IMFClockConsumer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFClockConsumer_FWD_DEFINED__

    if not defined(__IMFMediaStream_FWD_DEFINED__):
        class IMFMediaStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaStream_FWD_DEFINED__

    if not defined(__IMFMediaSink_FWD_DEFINED__):
        class IMFMediaSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSink_FWD_DEFINED__

    if not defined(__IMFStreamSink_FWD_DEFINED__):
        class IMFStreamSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFStreamSink_FWD_DEFINED__

    if not defined(__IMFVideoSampleAllocator_FWD_DEFINED__):
        class IMFVideoSampleAllocator(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoSampleAllocator_FWD_DEFINED__

    if not defined(__IMFVideoSampleAllocatorNotify_FWD_DEFINED__):
        class IMFVideoSampleAllocatorNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoSampleAllocatorNotify_FWD_DEFINED__

    if not defined(__IMFVideoSampleAllocatorNotifyEx_FWD_DEFINED__):
        class IMFVideoSampleAllocatorNotifyEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoSampleAllocatorNotifyEx_FWD_DEFINED__

    if not defined(__IMFVideoSampleAllocatorCallback_FWD_DEFINED__):
        class IMFVideoSampleAllocatorCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoSampleAllocatorCallback_FWD_DEFINED__

    if not defined(__IMFVideoSampleAllocatorEx_FWD_DEFINED__):
        class IMFVideoSampleAllocatorEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoSampleAllocatorEx_FWD_DEFINED__

    if not defined(__IMFDXGIDeviceManagerSource_FWD_DEFINED__):
        class IMFDXGIDeviceManagerSource(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFDXGIDeviceManagerSource_FWD_DEFINED__

    if not defined(__IMFVideoProcessorControl_FWD_DEFINED__):
        class IMFVideoProcessorControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoProcessorControl_FWD_DEFINED__

    if not defined(__IMFVideoProcessorControl2_FWD_DEFINED__):
        class IMFVideoProcessorControl2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoProcessorControl2_FWD_DEFINED__

    if not defined(__IMFVideoProcessorControl3_FWD_DEFINED__):
        class IMFVideoProcessorControl3(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoProcessorControl3_FWD_DEFINED__

    if not defined(__IMFTopology_FWD_DEFINED__):
    # END IF  __IMFTopology_FWD_DEFINED__

    if not defined(__IMFTopologyNode_FWD_DEFINED__):
        IMFTopology._methods_ = [
            # / <summary>
            # / It returns the identifier for the whole topology.
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pID">Pointer to a variable where the identifier
            # of the topology is returned</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>        
            COMMETHOD(
                [],
                HRESULT,
                'GetTopologyID',
                (['out'], POINTER(TOPOID), 'pID'),
            ),
            # / <summary>
            # / Add a node to the topology
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pNode">The pointer to the topology node to be
            # added</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                ['local'],
                HRESULT,
                'AddNode',
                (['in'], POINTER(IMFTopologyNode), 'pNode'),
            ),
            # / <summary>
            # / Remove a node from the topology
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pNode">the pointer to the topology node to be
            # removed</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                ['local'],
                HRESULT,
                'RemoveNode',
                (['in'], POINTER(IMFTopologyNode), 'pNode'),
            ),
            # / <summary>
            # / Return the count of nodes in the topology
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pwNodes">The pointer of a WORD variable where the
            # node count will be returned.</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>        
            COMMETHOD(
                [],
                HRESULT,
                'GetNodeCount',
                (['out'], POINTER(WORD), 'pwNodes'),
            ),
            # / <summary>
            # / Retreives the node at position wIndex
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="wIndex">the index of the node to return</param>
            # / <param name="ppNode">the node to return</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetNode',
                (['in'], WORD, 'wIndex'),
                (['out'], POINTER(POINTER(IMFTopologyNode)), 'ppNode'),
            ),
            # / <summary>
            # / Removes all nodes
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                ['local'],
                HRESULT,
                'Clear',
            ),
            # / <summary>
            # / Makes the current topology a copy of the topology passed in as
            # pTopology
            # / </summary>
            # / <remarks>
            # / It simplies calls IMFTopologyNode::CloneFrom on each topology
            # node in the topology
            # / </remarks>
            # / <param name="pTopology">The topology to clone from</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>        
            COMMETHOD(
                [],
                HRESULT,
                'CloneFrom',
                (['in'], POINTER(IMFTopology), 'pTopology'),
            ),
            # / <summary>
            # / Finds topology node by ID
            # / </summary>
            # / <returns>
            # /  <para>
            # /  MF_E_NOT_FOUND:
            # /   No node with the specific node ID exist in the topology.
            # /  </para>
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetNodeByID',
                (['in'], TOPOID, 'qwTopoNodeID'),
                (['out'], POINTER(POINTER(IMFTopologyNode)), 'ppNode'),
            ),
            # / <summary>
            # /  Used by MF components or application to discover all the
            # source
            # /  nodes in current topology.
            # /  This is a helper function to save caller from having to
            # enumerate
            # /  through the whole topology.
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="ppCollection">
            # /  The collection of the topology source nodes
            # / </param>
            # / <returns>
            # /  If the method succeeds, the return value is S_OK.
            # /  If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetSourceNodeCollection',
                (['out'], POINTER(POINTER(IMFCollection)), 'ppCollection'),
            ),
            # / <summary>
            # /  Used by MF components or application to discover all the
            # output
            # /  nodes.
            # /  This is a helper function to save caller from having to
            # enumerate
            # /  through the whole topology.
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="ppCollection">
            # /  The collection of the topology output nodes
            # / </param>
            # / <returns>
            # /  If the method succeeds, the return value is S_OK.
            # /  If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetOutputNodeCollection',
                (['out'], POINTER(POINTER(IMFCollection)), 'ppCollection'),
            ),
        ]

    # END IF  __IMFTopologyNode_FWD_DEFINED__

    if not defined(__IMFGetService_FWD_DEFINED__):
        class IMFGetService(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFGetService_FWD_DEFINED__

    if not defined(__IMFClock_FWD_DEFINED__):
        class IMFClock(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFClock_FWD_DEFINED__

    if not defined(__IMFPresentationClock_FWD_DEFINED__):
        class IMFPresentationClock(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPresentationClock_FWD_DEFINED__

    if not defined(__IMFPresentationTimeSource_FWD_DEFINED__):
        class IMFPresentationTimeSource(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPresentationTimeSource_FWD_DEFINED__

    if not defined(__IMFClockStateSink_FWD_DEFINED__):
        class IMFClockStateSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFClockStateSink_FWD_DEFINED__

    if not defined(__IMFPresentationDescriptor_FWD_DEFINED__):
        class IMFPresentationDescriptor(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPresentationDescriptor_FWD_DEFINED__

    if not defined(__IMFStreamDescriptor_FWD_DEFINED__):
        class IMFStreamDescriptor(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFStreamDescriptor_FWD_DEFINED__

    if not defined(__IMFMediaTypeHandler_FWD_DEFINED__):
        class IMFMediaTypeHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaTypeHandler_FWD_DEFINED__

    if not defined(__IMFTimer_FWD_DEFINED__):
        class IMFTimer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimer_FWD_DEFINED__

    if not defined(__IMFShutdown_FWD_DEFINED__):
        class IMFShutdown(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFShutdown_FWD_DEFINED__

    if not defined(__IMFTopoLoader_FWD_DEFINED__):
        class IMFTopoLoader(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTopoLoader_FWD_DEFINED__

    if not defined(__IMFContentProtectionManager_FWD_DEFINED__):
        class IMFContentProtectionManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFContentProtectionManager_FWD_DEFINED__

    if not defined(__IMFContentEnabler_FWD_DEFINED__):
        class IMFContentEnabler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFContentEnabler_FWD_DEFINED__

    if not defined(__IMFMetadata_FWD_DEFINED__):
        class IMFMetadata(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMetadata_FWD_DEFINED__

    if not defined(__IMFMetadataProvider_FWD_DEFINED__):
        class IMFMetadataProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMetadataProvider_FWD_DEFINED__

    if not defined(__IMFRateSupport_FWD_DEFINED__):
        class IMFRateSupport(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFRateSupport_FWD_DEFINED__

    if not defined(__IMFRateControl_FWD_DEFINED__):
        class IMFRateControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFRateControl_FWD_DEFINED__

    if not defined(__IMFTimecodeTranslate_FWD_DEFINED__):
        class IMFTimecodeTranslate(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTimecodeTranslate_FWD_DEFINED__

    if not defined(__IMFSeekInfo_FWD_DEFINED__):
        class IMFSeekInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSeekInfo_FWD_DEFINED__

    if not defined(__IMFSimpleAudioVolume_FWD_DEFINED__):
        class IMFSimpleAudioVolume(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSimpleAudioVolume_FWD_DEFINED__

    if not defined(__IMFAudioStreamVolume_FWD_DEFINED__):
        class IMFAudioStreamVolume(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFAudioStreamVolume_FWD_DEFINED__

    if not defined(__IMFAudioPolicy_FWD_DEFINED__):
        class IMFAudioPolicy(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFAudioPolicy_FWD_DEFINED__

    if not defined(__IMFSampleGrabberSinkCallback_FWD_DEFINED__):
        class IMFSampleGrabberSinkCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSampleGrabberSinkCallback_FWD_DEFINED__

    if not defined(__IMFSampleGrabberSinkCallback2_FWD_DEFINED__):
        class IMFSampleGrabberSinkCallback2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSampleGrabberSinkCallback2_FWD_DEFINED__

    if not defined(__IMFWorkQueueServices_FWD_DEFINED__):
        class IMFWorkQueueServices(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFWorkQueueServices_FWD_DEFINED__

    if not defined(__IMFWorkQueueServicesEx_FWD_DEFINED__):
        class IMFWorkQueueServicesEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFWorkQueueServicesEx_FWD_DEFINED__

    if not defined(__IMFQualityManager_FWD_DEFINED__):
        class IMFQualityManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFQualityManager_FWD_DEFINED__

    if not defined(__IMFQualityAdvise_FWD_DEFINED__):
        class IMFQualityAdvise(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFQualityAdvise_FWD_DEFINED__

    if not defined(__IMFQualityAdvise2_FWD_DEFINED__):
        class IMFQualityAdvise2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFQualityAdvise2_FWD_DEFINED__

    if not defined(__IMFQualityAdviseLimits_FWD_DEFINED__):
        class IMFQualityAdviseLimits(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFQualityAdviseLimits_FWD_DEFINED__

    if not defined(__IMFRealTimeClient_FWD_DEFINED__):
        class IMFRealTimeClient(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFRealTimeClient_FWD_DEFINED__

    if not defined(__IMFRealTimeClientEx_FWD_DEFINED__):
        class IMFRealTimeClientEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFRealTimeClientEx_FWD_DEFINED__

    if not defined(__IMFSequencerSource_FWD_DEFINED__):
        class IMFSequencerSource(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSequencerSource_FWD_DEFINED__

    if not defined(__IMFMediaSourceTopologyProvider_FWD_DEFINED__):
        class IMFMediaSourceTopologyProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSourceTopologyProvider_FWD_DEFINED__

    if not defined(__IMFMediaSourcePresentationProvider_FWD_DEFINED__):
        class IMFMediaSourcePresentationProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSourcePresentationProvider_FWD_DEFINED__

    if not defined(__IMFTopologyNodeAttributeEditor_FWD_DEFINED__):
        IMFTopology._methods_ = [
            # / <summary>
            # / It returns the identifier for the whole topology.
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pID">Pointer to a variable where the identifier
            # of the topology is returned</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>        
            COMMETHOD(
                [],
                HRESULT,
                'GetTopologyID',
                (['out'], POINTER(TOPOID), 'pID'),
            ),
            # / <summary>
            # / Add a node to the topology
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pNode">The pointer to the topology node to be
            # added</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                ['local'],
                HRESULT,
                'AddNode',
                (['in'], POINTER(IMFTopologyNode), 'pNode'),
            ),
            # / <summary>
            # / Remove a node from the topology
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pNode">the pointer to the topology node to be
            # removed</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                ['local'],
                HRESULT,
                'RemoveNode',
                (['in'], POINTER(IMFTopologyNode), 'pNode'),
            ),
            # / <summary>
            # / Return the count of nodes in the topology
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="pwNodes">The pointer of a WORD variable where the
            # node count will be returned.</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>        
            COMMETHOD(
                [],
                HRESULT,
                'GetNodeCount',
                (['out'], POINTER(WORD), 'pwNodes'),
            ),
            # / <summary>
            # / Retreives the node at position wIndex
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="wIndex">the index of the node to return</param>
            # / <param name="ppNode">the node to return</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetNode',
                (['in'], WORD, 'wIndex'),
                (['out'], POINTER(POINTER(IMFTopologyNode)), 'ppNode'),
            ),
            # / <summary>
            # / Removes all nodes
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                ['local'],
                HRESULT,
                'Clear',
            ),
            # / <summary>
            # / Makes the current topology a copy of the topology passed in as
            # pTopology
            # / </summary>
            # / <remarks>
            # / It simplies calls IMFTopologyNode::CloneFrom on each topology
            # node in the topology
            # / </remarks>
            # / <param name="pTopology">The topology to clone from</param>
            # / <returns>
            # / If the method succeeds, the return value is S_OK.
            # / If the method fails, the return value will be some failure
            # code.
            # / </returns>        
            COMMETHOD(
                [],
                HRESULT,
                'CloneFrom',
                (['in'], POINTER(IMFTopology), 'pTopology'),
            ),
            # / <summary>
            # / Finds topology node by ID
            # / </summary>
            # / <returns>
            # /  <para>
            # /  MF_E_NOT_FOUND:
            # /   No node with the specific node ID exist in the topology.
            # /  </para>
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetNodeByID',
                (['in'], TOPOID, 'qwTopoNodeID'),
                (['out'], POINTER(POINTER(IMFTopologyNode)), 'ppNode'),
            ),
            # / <summary>
            # /  Used by MF components or application to discover all the
            # source
            # /  nodes in current topology.
            # /  This is a helper function to save caller from having to
            # enumerate
            # /  through the whole topology.
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="ppCollection">
            # /  The collection of the topology source nodes
            # / </param>
            # / <returns>
            # /  If the method succeeds, the return value is S_OK.
            # /  If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetSourceNodeCollection',
                (['out'], POINTER(POINTER(IMFCollection)), 'ppCollection'),
            ),
            # / <summary>
            # /  Used by MF components or application to discover all the
            # output
            # /  nodes.
            # /  This is a helper function to save caller from having to
            # enumerate
            # /  through the whole topology.
            # / </summary>
            # / <remarks>
            # / </remarks>
            # / <param name="ppCollection">
            # /  The collection of the topology output nodes
            # / </param>
            # / <returns>
            # /  If the method succeeds, the return value is S_OK.
            # /  If the method fails, the return value will be some failure
            # code.
            # / </returns>
            #        
            COMMETHOD(
                [],
                HRESULT,
                'GetOutputNodeCollection',
                (['out'], POINTER(POINTER(IMFCollection)), 'ppCollection'),
            ),
        ]

    # END IF  __IMFTopologyNodeAttributeEditor_FWD_DEFINED__

    if not defined(__IMFByteStreamBuffering_FWD_DEFINED__):
        class IMFByteStreamBuffering(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFByteStreamBuffering_FWD_DEFINED__

    if not defined(__IMFByteStreamCacheControl_FWD_DEFINED__):
        class IMFByteStreamCacheControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFByteStreamCacheControl_FWD_DEFINED__

    if not defined(__IMFByteStreamTimeSeek_FWD_DEFINED__):
        class IMFByteStreamTimeSeek(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFByteStreamTimeSeek_FWD_DEFINED__

    if not defined(__IMFByteStreamCacheControl2_FWD_DEFINED__):
        class IMFByteStreamCacheControl2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFByteStreamCacheControl2_FWD_DEFINED__

    if not defined(__IMFNetCredential_FWD_DEFINED__):
        class IMFNetCredential(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetCredential_FWD_DEFINED__

    if not defined(__IMFNetCredentialManager_FWD_DEFINED__):
        class IMFNetCredentialManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetCredentialManager_FWD_DEFINED__

    if not defined(__IMFNetCredentialCache_FWD_DEFINED__):
        class IMFNetCredentialCache(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetCredentialCache_FWD_DEFINED__

    if not defined(__IMFSSLCertificateManager_FWD_DEFINED__):
        class IMFSSLCertificateManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSSLCertificateManager_FWD_DEFINED__

    if not defined(__IMFNetResourceFilter_FWD_DEFINED__):
        class IMFNetResourceFilter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetResourceFilter_FWD_DEFINED__

    if not defined(__IMFSourceOpenMonitor_FWD_DEFINED__):
        class IMFSourceOpenMonitor(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSourceOpenMonitor_FWD_DEFINED__

    if not defined(__IMFNetProxyLocator_FWD_DEFINED__):
        class IMFNetProxyLocator(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetProxyLocator_FWD_DEFINED__

    if not defined(__IMFNetProxyLocatorFactory_FWD_DEFINED__):
        class IMFNetProxyLocatorFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetProxyLocatorFactory_FWD_DEFINED__

    if not defined(__IMFSaveJob_FWD_DEFINED__):
        class IMFSaveJob(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSaveJob_FWD_DEFINED__

    if not defined(__IMFNetSchemeHandlerConfig_FWD_DEFINED__):
        class IMFNetSchemeHandlerConfig(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetSchemeHandlerConfig_FWD_DEFINED__

    if not defined(__IMFSchemeHandler_FWD_DEFINED__):
        class IMFSchemeHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSchemeHandler_FWD_DEFINED__

    if not defined(__IMFByteStreamHandler_FWD_DEFINED__):
        class IMFByteStreamHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFByteStreamHandler_FWD_DEFINED__

    if not defined(__IMFTrustedInput_FWD_DEFINED__):
        class IMFTrustedInput(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTrustedInput_FWD_DEFINED__

    if not defined(__IMFInputTrustAuthority_FWD_DEFINED__):
        class IMFInputTrustAuthority(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFInputTrustAuthority_FWD_DEFINED__

    if not defined(__IMFTrustedOutput_FWD_DEFINED__):
        class IMFTrustedOutput(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTrustedOutput_FWD_DEFINED__

    if not defined(__IMFOutputTrustAuthority_FWD_DEFINED__):
        class IMFOutputTrustAuthority(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFOutputTrustAuthority_FWD_DEFINED__

    if not defined(__IMFOutputPolicy_FWD_DEFINED__):
        class IMFOutputPolicy(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFOutputPolicy_FWD_DEFINED__

    if not defined(__IMFOutputSchema_FWD_DEFINED__):
        class IMFOutputSchema(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFOutputSchema_FWD_DEFINED__

    if not defined(__IMFSecureChannel_FWD_DEFINED__):
        class IMFSecureChannel(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSecureChannel_FWD_DEFINED__

    if not defined(__IMFSampleProtection_FWD_DEFINED__):
        class IMFSampleProtection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSampleProtection_FWD_DEFINED__

    if not defined(__IMFMediaSinkPreroll_FWD_DEFINED__):
        class IMFMediaSinkPreroll(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSinkPreroll_FWD_DEFINED__

    if not defined(__IMFFinalizableMediaSink_FWD_DEFINED__):
        class IMFFinalizableMediaSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFFinalizableMediaSink_FWD_DEFINED__

    if not defined(__IMFStreamingSinkConfig_FWD_DEFINED__):
        class IMFStreamingSinkConfig(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFStreamingSinkConfig_FWD_DEFINED__

    if not defined(__IMFRemoteProxy_FWD_DEFINED__):
        class IMFRemoteProxy(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFRemoteProxy_FWD_DEFINED__

    if not defined(__IMFObjectReferenceStream_FWD_DEFINED__):
        class IMFObjectReferenceStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFObjectReferenceStream_FWD_DEFINED__

    if not defined(__IMFPMPHost_FWD_DEFINED__):
        class IMFPMPHost(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPMPHost_FWD_DEFINED__

    if not defined(__IMFPMPClient_FWD_DEFINED__):
        class IMFPMPClient(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPMPClient_FWD_DEFINED__

    if not defined(__IMFPMPServer_FWD_DEFINED__):
        class IMFPMPServer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPMPServer_FWD_DEFINED__

    if not defined(__IMFRemoteDesktopPlugin_FWD_DEFINED__):
        class IMFRemoteDesktopPlugin(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFRemoteDesktopPlugin_FWD_DEFINED__

    if not defined(__IMFSAMIStyle_FWD_DEFINED__):
        class IMFSAMIStyle(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSAMIStyle_FWD_DEFINED__

    if not defined(__IMFTranscodeProfile_FWD_DEFINED__):
        class IMFTranscodeProfile(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTranscodeProfile_FWD_DEFINED__

    if not defined(__IMFTranscodeSinkInfoProvider_FWD_DEFINED__):
        class IMFTranscodeSinkInfoProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTranscodeSinkInfoProvider_FWD_DEFINED__

    if not defined(__IMFFieldOfUseMFTUnlock_FWD_DEFINED__):
        class IMFFieldOfUseMFTUnlock(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFFieldOfUseMFTUnlock_FWD_DEFINED__

    if not defined(__IMFLocalMFTRegistration_FWD_DEFINED__):
        class IMFLocalMFTRegistration(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFLocalMFTRegistration_FWD_DEFINED__

    if not defined(__IMFCapturePhotoConfirmation_FWD_DEFINED__):
        class IMFCapturePhotoConfirmation(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFCapturePhotoConfirmation_FWD_DEFINED__

    if not defined(__IMFPMPHostApp_FWD_DEFINED__):
        class IMFPMPHostApp(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPMPHostApp_FWD_DEFINED__

    if not defined(__IMFPMPClientApp_FWD_DEFINED__):
        class IMFPMPClientApp(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPMPClientApp_FWD_DEFINED__

    if not defined(__IMFMediaStreamSourceSampleRequest_FWD_DEFINED__):
        class IMFMediaStreamSourceSampleRequest(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaStreamSourceSampleRequest_FWD_DEFINED__

    if not defined(__IMFTrackedSample_FWD_DEFINED__):
        class IMFTrackedSample(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTrackedSample_FWD_DEFINED__

    if not defined(__IMFProtectedEnvironmentAccess_FWD_DEFINED__):
        class IMFProtectedEnvironmentAccess(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFProtectedEnvironmentAccess_FWD_DEFINED__

    if not defined(__IMFSignedLibrary_FWD_DEFINED__):
        class IMFSignedLibrary(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSignedLibrary_FWD_DEFINED__

    if not defined(__IMFSystemId_FWD_DEFINED__):
        class IMFSystemId(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSystemId_FWD_DEFINED__

    if not defined(__IMFContentProtectionDevice_FWD_DEFINED__):
        class IMFContentProtectionDevice(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFContentProtectionDevice_FWD_DEFINED__

    if not defined(__IMFContentDecryptorContext_FWD_DEFINED__):
        class IMFContentDecryptorContext(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFContentDecryptorContext_FWD_DEFINED__

    if not defined(__IMFNetCrossOriginSupport_FWD_DEFINED__):
        class IMFNetCrossOriginSupport(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFNetCrossOriginSupport_FWD_DEFINED__

    if not defined(__IMFHttpDownloadRequest_FWD_DEFINED__):
        class IMFHttpDownloadRequest(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFHttpDownloadRequest_FWD_DEFINED__

    if not defined(__IMFHttpDownloadSession_FWD_DEFINED__):
        class IMFHttpDownloadSession(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFHttpDownloadSession_FWD_DEFINED__

    if not defined(__IMFHttpDownloadSessionProvider_FWD_DEFINED__):
        class IMFHttpDownloadSessionProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFHttpDownloadSessionProvider_FWD_DEFINED__

    if not defined(__IMFMediaSource2_FWD_DEFINED__):
        class IMFMediaSource2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaSource2_FWD_DEFINED__

    if not defined(__IMFMediaStream2_FWD_DEFINED__):
        class IMFMediaStream2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFMediaStream2_FWD_DEFINED__

    if not defined(__IMFSensorDevice_FWD_DEFINED__):
        class IMFSensorDevice(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorDevice_FWD_DEFINED__

    if not defined(__IMFSensorGroup_FWD_DEFINED__):
        class IMFSensorGroup(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorGroup_FWD_DEFINED__

    if not defined(__IMFSensorStream_FWD_DEFINED__):
        class IMFSensorStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorStream_FWD_DEFINED__

    if not defined(__IMFSensorTransformFactory_FWD_DEFINED__):
        class IMFSensorTransformFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorTransformFactory_FWD_DEFINED__

    if not defined(__IMFSensorProfile_FWD_DEFINED__):
        class IMFSensorProfile(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorProfile_FWD_DEFINED__

    if not defined(__IMFSensorProfileCollection_FWD_DEFINED__):
        class IMFSensorProfileCollection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorProfileCollection_FWD_DEFINED__

    if not defined(__IMFSensorProcessActivity_FWD_DEFINED__):
        class IMFSensorProcessActivity(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorProcessActivity_FWD_DEFINED__

    if not defined(__IMFSensorActivityReport_FWD_DEFINED__):
        class IMFSensorActivityReport(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorActivityReport_FWD_DEFINED__

    if not defined(__IMFSensorActivitiesReport_FWD_DEFINED__):
        class IMFSensorActivitiesReport(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorActivitiesReport_FWD_DEFINED__

    if not defined(__IMFSensorActivitiesReportCallback_FWD_DEFINED__):
        class IMFSensorActivitiesReportCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorActivitiesReportCallback_FWD_DEFINED__

    if not defined(__IMFSensorActivityMonitor_FWD_DEFINED__):
        class IMFSensorActivityMonitor(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSensorActivityMonitor_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.mfobjects_h import * # NOQA
    from pyWinAPI.um.mftransform_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    # interface __MIDL_itf_mfidl_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.shared.windef_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        class MFSESSION_SETTOPOLOGY_FLAGS(ENUM):
            MFSESSION_SETTOPOLOGY_IMMEDIATE = 0x1
            MFSESSION_SETTOPOLOGY_NORESOLUTION = 0x2
            MFSESSION_SETTOPOLOGY_CLEAR_CURRENT = 0x4


        class MFSESSION_GETFULLTOPOLOGY_FLAGS(ENUM):
            MFSESSION_GETFULLTOPOLOGY_CURRENT = 0x1


        class MFPMPSESSION_CREATION_FLAGS(ENUM):
            MFPMPSESSION_UNPROTECTED_PROCESS = 0x1
            MFPMPSESSION_IN_PROCESS = 0x2

        INT64 TOPOID = UINT
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        MF_WVC1_PROG_SINGLE_SLICE_CONTENT = EXTERN_GUID(
            0x67EC2559,
            0x0F2F,
            0x4420,
            0xA4,
            0xDD,
            0x2F,
            0x8E,
            0xE7,
            0xA5,
            0x73,
            0x8B
        )
        MF_PROGRESSIVE_CODING_CONTENT = EXTERN_GUID(
            0x8F020EEA,
            0x1508,
            0x471F,
            0x9D,
            0xA6,
            0x50,
            0x7D,
            0x7C,
            0xFA,
            0x40,
            0xDB
        )
        MF_NALU_LENGTH_SET = EXTERN_GUID(
            0xA7911D53,
            0x12A4,
            0x4965,
            0xAE,
            0x70,
            0x6E,
            0xAD,
            0xD6,
            0xFF,
            0x05,
            0x51
        )
        MF_NALU_LENGTH_INFORMATION = EXTERN_GUID(
            0x19124E7C,
            0xAD4B,
            0x465F,
            0xBB,
            0x18,
            0x20,
            0x18,
            0x62,
            0x87,
            0xB6,
            0xAF
        )
        MF_USER_DATA_PAYLOAD = EXTERN_GUID(
            0xD1D4985D,
            0xDC92,
            0x457A,
            0xB3,
            0xA0,
            0x65,
            0x1A,
            0x33,
            0xA3,
            0x10,
            0x47
        )
        MF_MPEG4SINK_SPSPPS_PASSTHROUGH = EXTERN_GUID(
            0x5601A134,
            0x2005,
            0x4AD2,
            0xB3,
            0x7D,
            0x22,
            0xA6,
            0xC5,
            0x54,
            0xDE,
            0xB2
        )
        MF_MPEG4SINK_MOOV_BEFORE_MDAT = EXTERN_GUID(
            0xF672E3AC,
            0xE1E6,
            0x4F10,
            0xB5,
            0xEC,
            0x5F,
            0x3B,
            0x30,
            0x82,
            0x88,
            0x16
        )
        MF_MPEG4SINK_MINIMUM_PROPERTIES_SIZE = EXTERN_GUID(
            0xDCA1ED52,
            0x450E,
            0x4A22,
            0x8C,
            0x62,
            0x4E,
            0xD4,
            0x52,
            0xF7,
            0xA1,
            0x87
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFMediaSession_INTERFACE_DEFINED__):
            # interface IMFMediaSession
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaSession = MIDL_INTERFACE(
                    "{90377834-21D0-4DEE-8214-BA2E3E6C1127}"
                )
                IMFMediaSession._iid_ = IID_IMFMediaSession


                IMFMediaSession._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetTopology')],
                        HRESULT,
                        'SetTopology',
                        (['in'], DWORD, 'dwSetTopologyFlags'),
                        (['in'], POINTER(IMFTopology), 'pTopology'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ClearTopologies')],
                        HRESULT,
                        'ClearTopologies',
                    ),
                    COMMETHOD(
                        [helpstring('Method Start')],
                        HRESULT,
                        'Start',
                        (['unique', 'in'], POINTER(GUID), 'pguidTimeFormat'),
                        (
                            ['unique', 'in'],
                            POINTER(PROPVARIANT),
                           'pvarStartPosition'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Pause')],
                        HRESULT,
                        'Pause',
                    ),
                    COMMETHOD(
                        [helpstring('Method Stop')],
                        HRESULT,
                        'Stop',
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                    COMMETHOD(
                        [helpstring('Method Shutdown')],
                        HRESULT,
                        'Shutdown',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetClock')],
                        HRESULT,
                        'GetClock',
                        (['out'], POINTER(POINTER(IMFClock)), 'ppClock'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSessionCapabilities')],
                        HRESULT,
                        'GetSessionCapabilities',
                        (['out'], POINTER(DWORD), 'pdwCaps'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFullTopology')],
                        HRESULT,
                        'GetFullTopology',
                        (['in'], DWORD, 'dwGetFullTopologyFlags'),
                        (['in'], TOPOID, 'TopoId'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopology)),
                           'ppFullTopology'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaSession_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0001
        # [local]
        MF_SESSION_TOPOLOADER = EXTERN_GUID(
            0x1E83D482,
            0x1F1C,
            0x4571,
            0x84,
            0x5,
            0x88,
            0xF4,
            0xB2,
            0x18,
            0x1F,
            0x71
        )
        MF_SESSION_GLOBAL_TIME = EXTERN_GUID(
            0x1E83D482,
            0x1F1C,
            0x4571,
            0x84,
            0x5,
            0x88,
            0xF4,
            0xB2,
            0x18,
            0x1F,
            0x72
        )
        MF_SESSION_QUALITY_MANAGER = EXTERN_GUID(
            0x1E83D482,
            0x1F1C,
            0x4571,
            0x84,
            0x5,
            0x88,
            0xF4,
            0xB2,
            0x18,
            0x1F,
            0x73
        )
        MF_SESSION_CONTENT_PROTECTION_MANAGER = EXTERN_GUID(
            0x1E83D482,
            0x1F1C,
            0x4571,
            0x84,
            0x5,
            0x88,
            0xF4,
            0xB2,
            0x18,
            0x1F,
            0x74
        )
        MF_SESSION_SERVER_CONTEXT = EXTERN_GUID(
            0xAFE5B291,
            0x50FA,
            0x46E8,
            0xB9,
            0xBE,
            0xC,
            0xC,
            0x3C,
            0xE4,
            0xB3,
            0xA5
        )
        MF_SESSION_REMOTE_SOURCE_MODE = EXTERN_GUID(
            0xF4033EF4,
            0x9BB3,
            0x4378,
            0x94,
            0x1F,
            0x85,
            0xA0,
            0x85,
            0x6B,
            0xC2,
            0x44
        )
        MF_SESSION_APPROX_EVENT_OCCURRENCE_TIME = EXTERN_GUID(
            0x190E852F,
            0x6238,
            0x42D1,
            0xB5,
            0xAF,
            0x69,
            0xEA,
            0x33,
            0x8E,
            0xF8,
            0x50
        )
        MF_PMP_SERVER_CONTEXT = EXTERN_GUID(
            0x2F00C910,
            0xD2CF,
            0x4278,
            0x8B,
            0x6A,
            0xD0,
            0x77,
            0xFA,
            0xC3,
            0xA2,
            0x5F
        )
        mf = ctypes.windll.MF


        # STDAPI MFCreateMediaSession(
        # IMFAttributes* pConfiguration,
        # _Outptr_ IMFMediaSession** ppMediaSession
        # );
        MFCreateMediaSession = mf.MFCreateMediaSession
        MFCreateMediaSession.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP):
        mf = ctypes.windll.MF


        # STDAPI MFCreatePMPMediaSession(
        # DWORD dwCreationFlags,
        # IMFAttributes *pConfiguration,
        # _Outptr_ IMFMediaSession** ppMediaSession,
        # _Outptr_opt_ IMFActivate **ppEnablerActivate
        # );
        MFCreatePMPMediaSession = mf.MFCreatePMPMediaSession
        MFCreatePMPMediaSession.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class MF_OBJECT_TYPE(ENUM):
            MF_OBJECT_MEDIASOURCE = 0
            MF_OBJECT_BYTESTREAM = MF_OBJECT_MEDIASOURCE + 1 )
            MF_OBJECT_INVALID = MF_OBJECT_BYTESTREAM + 1 )


        class __MIDL___MIDL_itf_mfidl_0000_0001_0001(ENUM):
            MF_RESOLUTION_MEDIASOURCE = 0x1
            MF_RESOLUTION_BYTESTREAM = 0x2
            MF_RESOLUTION_CONTENT_DOES_NOT_HAVE_TO_MATCH_EXTENSION_OR_MIME_TYPE = (
                0x10
            )
            MF_RESOLUTION_KEEP_BYTE_STREAM_ALIVE_ON_FAIL = 0x20
            MF_RESOLUTION_DISABLE_LOCAL_PLUGINS = 0x40
            MF_RESOLUTION_PLUGIN_CONTROL_POLICY_APPROVED_ONLY = 0x80
            MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY = 0x100
            MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY_EDGEMODE = 0x200
            MF_RESOLUTION_ENABLE_STORE_PLUGINS = 0x400
            MF_RESOLUTION_READ = 0x10000
            MF_RESOLUTION_WRITE = 0x20000

        MF_RESOLUTION_MEDIASOURCE = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_MEDIASOURCE
        MF_RESOLUTION_BYTESTREAM = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_BYTESTREAM
        MF_RESOLUTION_CONTENT_DOES_NOT_HAVE_TO_MATCH_EXTENSION_OR_MIME_TYPE = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_CONTENT_DOES_NOT_HAVE_TO_MATCH_EXTENSION_OR_MIME_TYPE
        MF_RESOLUTION_KEEP_BYTE_STREAM_ALIVE_ON_FAIL = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_KEEP_BYTE_STREAM_ALIVE_ON_FAIL
        MF_RESOLUTION_DISABLE_LOCAL_PLUGINS = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_DISABLE_LOCAL_PLUGINS
        MF_RESOLUTION_PLUGIN_CONTROL_POLICY_APPROVED_ONLY = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_PLUGIN_CONTROL_POLICY_APPROVED_ONLY
        MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY
        MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY_EDGEMODE = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_PLUGIN_CONTROL_POLICY_WEB_ONLY_EDGEMODE
        MF_RESOLUTION_ENABLE_STORE_PLUGINS = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_ENABLE_STORE_PLUGINS
        MF_RESOLUTION_READ = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_READ
        MF_RESOLUTION_WRITE = __MIDL___MIDL_itf_mfidl_0000_0001_0001.MF_RESOLUTION_WRITE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        class _MF_CONNECT_METHOD(ENUM):
            MF_CONNECT_DIRECT = 0
            MF_CONNECT_ALLOW_CONVERTER = 0x1
            MF_CONNECT_ALLOW_DECODER = 0x3
            MF_CONNECT_RESOLVE_INDEPENDENT_OUTPUTTYPES = 0x4
            MF_CONNECT_AS_OPTIONAL = 0x10000
            MF_CONNECT_AS_OPTIONAL_BRANCH = 0x20000

        MF_CONNECT_METHOD = _MF_CONNECT_METHOD


        class _MF_TOPOLOGY_RESOLUTION_STATUS_FLAGS(ENUM):
            MF_TOPOLOGY_RESOLUTION_SUCCEEDED = 0
            MF_OPTIONAL_NODE_REJECTED_MEDIA_TYPE = 0x1
            MF_OPTIONAL_NODE_REJECTED_PROTECTED_PROCESS = 0x2

        MF_TOPOLOGY_RESOLUTION_STATUS_FLAGS = _MF_TOPOLOGY_RESOLUTION_STATUS_FLAGS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFSourceResolver_INTERFACE_DEFINED__):
            # interface IMFSourceResolver
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSourceResolver = MIDL_INTERFACE(
                    "{FBE5A32D-A497-4B61-BB85-97B1A848A6E3}"
                )
                IMFSourceResolver._iid_ = IID_IMFSourceResolver


                IMFSourceResolver._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateObjectFromURL'), 'local'],
                        HRESULT,
                        'CreateObjectFromURL',
                        (['in'], LPCWSTR, 'pwszURL'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], POINTER(IPropertyStore), 'pProps'),
                        (['out'], POINTER(MF_OBJECT_TYPE), 'pObjectType'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method CreateObjectFromByteStream'), 'local'],
                        HRESULT,
                        'CreateObjectFromByteStream',
                        (['in'], POINTER(IMFByteStream), 'pByteStream'),
                        (['in'], LPCWSTR, 'pwszURL'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], POINTER(IPropertyStore), 'pProps'),
                        (['out'], POINTER(MF_OBJECT_TYPE), 'pObjectType'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginCreateObjectFromURL'), 'local'],
                        HRESULT,
                        'BeginCreateObjectFromURL',
                        (['in'], LPCWSTR, 'pwszURL'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], POINTER(IPropertyStore), 'pProps'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppIUnknownCancelCookie'
                        ),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndCreateObjectFromURL'), 'local'],
                        HRESULT,
                        'EndCreateObjectFromURL',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(MF_OBJECT_TYPE), 'pObjectType'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginCreateObjectFromByteStream'), 'local'],
                        HRESULT,
                        'BeginCreateObjectFromByteStream',
                        (['in'], POINTER(IMFByteStream), 'pByteStream'),
                        (['in'], LPCWSTR, 'pwszURL'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], POINTER(IPropertyStore), 'pProps'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppIUnknownCancelCookie'
                        ),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndCreateObjectFromByteStream'), 'local'],
                        HRESULT,
                        'EndCreateObjectFromByteStream',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(MF_OBJECT_TYPE), 'pObjectType'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method CancelObjectCreation'), 'local'],
                        HRESULT,
                        'CancelObjectCreation',
                        (
                            ['in'],
                            POINTER(comtypes.IUnknown),
                           'pIUnknownCancelCookie'
                        ),
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [string][in]            # [in]            # [in]            # [in]            # [call_as]            # [in]            # [out]            # [out]            # [call_as]            # [in]            # [unique][in]            # [in]            # [unique][in]            # [in]            # [call_as]            # [in]            # [out]            # [out]        # END IF  __IMFSourceResolver_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0002
        # [local]
        mf = ctypes.windll.MF


        # STDAPI MFCreateSourceResolver(
        # _Outptr_ IMFSourceResolver     **ppISourceResolver); // out
        MFCreateSourceResolver = mf.MFCreateSourceResolver
        MFCreateSourceResolver.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        mfplat = ctypes.windll.MFPLAT


        # STDAPI CreatePropertyStore(
        # _Outptr_ IPropertyStore        **ppStore); // out
        CreatePropertyStore = mfplat.CreatePropertyStore
        CreatePropertyStore.restype = STDAPI


        mf = ctypes.windll.MF


        # STDAPI MFGetSupportedSchemes(
        # _Out_ PROPVARIANT* pPropVarSchemeArray  );
        MFGetSupportedSchemes = mf.MFGetSupportedSchemes
        MFGetSupportedSchemes.restype = STDAPI


        # STDAPI MFGetSupportedMimeTypes(
        # _Out_ PROPVARIANT* pPropVarMimeTypeArray  );
        MFGetSupportedMimeTypes = mf.MFGetSupportedMimeTypes
        MFGetSupportedMimeTypes.restype = STDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINVER >= _WIN32_WINNT_WIN7:
        pass
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINVER >= _WIN32_WINNT_WIN8:
        pass
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        pass
    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MFMEDIASOURCE_CHARACTERISTICS(ENUM):
            MFMEDIASOURCE_IS_LIVE = 0x1
            MFMEDIASOURCE_CAN_SEEK = 0x2
            MFMEDIASOURCE_CAN_PAUSE = 0x4
            MFMEDIASOURCE_HAS_SLOW_SEEK = 0x8
            MFMEDIASOURCE_HAS_MULTIPLE_PRESENTATIONS = 0x10
            MFMEDIASOURCE_CAN_SKIPFORWARD = 0x20
            MFMEDIASOURCE_CAN_SKIPBACKWARD = 0x40
            MFMEDIASOURCE_DOES_NOT_USE_NETWORK = 0x80

        MFMEDIASOURCE_CHARACTERISTICS = _MFMEDIASOURCE_CHARACTERISTICS
        if WINVER >= _WIN32_WINNT_WIN7:
            MF_TIME_FORMAT_ENTRY_RELATIVE = EXTERN_GUID(
                0x4399F178,
                0x46D3,
                0x4504,
                0xAF,
                0xDA,
                0x20,
                0xD3,
                0x2E,
                0x9B,
                0xA3,
                0x60
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if not defined(__IMFMediaSource_INTERFACE_DEFINED__):
            # interface IMFMediaSource
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaSource = MIDL_INTERFACE(
                    "{279A808D-AEC7-40C8-9C6B-A6B492C78A66}"
                )
                IMFMediaSource._iid_ = IID_IMFMediaSource


                IMFMediaSource._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCharacteristics')],
                        HRESULT,
                        'GetCharacteristics',
                        (['out'], POINTER(DWORD), 'pdwCharacteristics'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CreatePresentationDescriptor'), 'local'],
                        HRESULT,
                        'CreatePresentationDescriptor',
                        (
                            ['out'],
                            POINTER(POINTER(IMFPresentationDescriptor)),
                           'ppPresentationDescriptor'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Start')],
                        HRESULT,
                        'Start',
                        (
                            ['in'],
                            POINTER(IMFPresentationDescriptor),
                           'pPresentationDescriptor'
                        ),
                        (['unique', 'in'], POINTER(GUID), 'pguidTimeFormat'),
                        (
                            ['unique', 'in'],
                            POINTER(PROPVARIANT),
                           'pvarStartPosition'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Stop')],
                        HRESULT,
                        'Stop',
                    ),
                    COMMETHOD(
                        [helpstring('Method Pause')],
                        HRESULT,
                        'Pause',
                    ),
                    COMMETHOD(
                        [helpstring('Method Shutdown')],
                        HRESULT,
                        'Shutdown',
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [out]            # [size_is][size_is][out]            # [out]        # END IF  __IMFMediaSource_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0003
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINVER >= _WIN32_WINNT_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFMediaSourceEx_INTERFACE_DEFINED__):
                # interface IMFMediaSourceEx
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFMediaSourceEx = MIDL_INTERFACE(
                        "{3C9B2EB9-86D5-4514-A394-F56664F9F0D8}"
                    )
                    IMFMediaSourceEx._iid_ = IID_IMFMediaSourceEx


                    IMFMediaSourceEx._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetSourceAttributes')],
                            HRESULT,
                            'GetSourceAttributes',
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamAttributes')],
                            HRESULT,
                            'GetStreamAttributes',
                            (['in'], DWORD, 'dwStreamIdentifier'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetD3DManager')],
                            HRESULT,
                            'SetD3DManager',
                            (['in'], POINTER(comtypes.IUnknown), 'pManager'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFMediaSourceEx_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0004
            # [local]
            MF_SOURCE_STREAM_SUPPORTS_HW_CONNECTION = EXTERN_GUID(
                0xA38253AA,
                0x6314,
                0x42FD,
                0xA3,
                0xCE,
                0xBB,
                0x27,
                0xB6,
                0x85,
                0x99,
                0x46
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFClockConsumer_INTERFACE_DEFINED__):
                # interface IMFClockConsumer
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFClockConsumer = MIDL_INTERFACE(
                        "{6EF2A662-47C0-4666-B13D-CBB717F2FA2C}"
                    )
                    IMFClockConsumer._iid_ = IID_IMFClockConsumer


                    IMFClockConsumer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetPresentationClock')],
                            HRESULT,
                            'SetPresentationClock',
                            (
                                ['in'],
                                POINTER(IMFPresentationClock),
                               'pPresentationClock'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPresentationClock')],
                            HRESULT,
                            'GetPresentationClock',
                            (
                                ['out'],
                                POINTER(POINTER(IMFPresentationClock)),
                               'ppPresentationClock'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFClockConsumer_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0005
            # [local]        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFMediaStream_INTERFACE_DEFINED__):
            # interface IMFMediaStream
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaStream = MIDL_INTERFACE(
                    "{D182108F-4EC6-443F-AA42-A71106EC825F}"
                )
                IMFMediaStream._iid_ = IID_IMFMediaStream


                IMFMediaStream._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetMediaSource')],
                        HRESULT,
                        'GetMediaSource',
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaSource)),
                           'ppMediaSource'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamDescriptor')],
                        HRESULT,
                        'GetStreamDescriptor',
                        (
                            ['out'],
                            POINTER(POINTER(IMFStreamDescriptor)),
                           'ppStreamDescriptor'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method RequestSample'), 'local'],
                        HRESULT,
                        'RequestSample',
                        (['in'], POINTER(comtypes.IUnknown), 'pToken'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]        # END IF  __IMFMediaStream_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0006
        # [local]
        if WINVER >= _WIN32_WINNT_WIN8:
            MF_STREAM_SINK_SUPPORTS_HW_CONNECTION = EXTERN_GUID(
                0x9B465CBF,
                0x597,
                0x4F9E,
                0x9F,
                0x3C,
                0xB9,
                0x7E,
                0xEE,
                0xF9,
                0x3,
                0x59
            )
            MF_STREAM_SINK_SUPPORTS_ROTATION = EXTERN_GUID(
                0xB3E96280,
                0xBD05,
                0x41A5,
                0x97,
                0xAD,
                0x8A,
                0x7F,
                0xEE,
                0x24,
                0xB9,
                0x12
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)


        class MF_TRANSFER_VIDEO_FRAME_FLAGS(ENUM):
            MF_TRANSFER_VIDEO_FRAME_DEFAULT = 0
            MF_TRANSFER_VIDEO_FRAME_STRETCH = 1
            MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR = 2

        MF_SINK_VIDEO_PTS = EXTERN_GUID(
            0x2162BDE7,
            0x421E,
            0x4B90,
            0x9B,
            0x33,
            0xE5,
            0x8F,
            0xBF,
            0x1D,
            0x58,
            0xB6
        )
        MF_SINK_VIDEO_NATIVE_WIDTH = EXTERN_GUID(
            0xE6D6A707,
            0x1505,
            0x4747,
            0x9B,
            0x10,
            0x72,
            0xD2,
            0xD1,
            0x58,
            0xCB,
            0x3A
        )
        MF_SINK_VIDEO_NATIVE_HEIGHT = EXTERN_GUID(
            0xF0CA6705,
            0x490C,
            0x43E8,
            0x94,
            0x1C,
            0xC0,
            0xB3,
            0x20,
            0x6B,
            0x9A,
            0x65
        )
        MF_SINK_VIDEO_DISPLAY_ASPECT_RATIO_NUMERATOR = EXTERN_GUID(
            0xD0F33B22,
            0xB78A,
            0x4879,
            0xB4,
            0x55,
            0xF0,
            0x3E,
            0xF3,
            0xFA,
            0x82,
            0xCD
        )
        MF_SINK_VIDEO_DISPLAY_ASPECT_RATIO_DENOMINATOR = EXTERN_GUID(
            0x6EA1EB97,
            0x1FE0,
            0x4F10,
            0xA6,
            0xE4,
            0x1F,
            0x4F,
            0x66,
            0x15,
            0x64,
            0xE0
        )
        MF_BD_MVC_PLANE_OFFSET_METADATA = EXTERN_GUID(
            0x62A654E4,
            0xB76C,
            0x4901,
            0x98,
            0x23,
            0x2C,
            0xB6,
            0x15,
            0xD4,
            0x73,
            0x18
        )
        MF_LUMA_KEY_ENABLE = EXTERN_GUID(
            0x7369820F,
            0x76DE,
            0x43CA,
            0x92,
            0x84,
            0x47,
            0xB8,
            0xF3,
            0x7E,
            0x06,
            0x49
        )
        MF_LUMA_KEY_LOWER = EXTERN_GUID(
            0x93D7B8D5,
            0x0B81,
            0x4715,
            0xAE,
            0xA0,
            0x87,
            0x25,
            0x87,
            0x16,
            0x21,
            0xE9
        )
        MF_LUMA_KEY_UPPER = EXTERN_GUID(
            0xD09F39BB,
            0x4602,
            0x4C31,
            0xA7,
            0x06,
            0xA1,
            0x21,
            0x71,
            0xA5,
            0x11,
            0x0A
        )
        MF_USER_EXTENDED_ATTRIBUTES = EXTERN_GUID(
            0xC02ABAC6,
            0xFEB2,
            0x4541,
            0x92,
            0x2F,
            0x92,
            0x0B,
            0x43,
            0x70,
            0x27,
            0x22
        )
        MF_INDEPENDENT_STILL_IMAGE = EXTERN_GUID(
            0xEA12AF41,
            0x0710,
            0x42C9,
            0xA1,
            0x27,
            0xDA,
            0xA3,
            0xE7,
            0x84,
            0x83,
            0xA5
        )
        if not defined(__IMFMediaSink_INTERFACE_DEFINED__):
            # interface IMFMediaSink
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaSink = MIDL_INTERFACE(
                    "{6EF2A660-47C0-4666-B13D-CBB717F2FA2C}"
                )
                IMFMediaSink._iid_ = IID_IMFMediaSink


                IMFMediaSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCharacteristics')],
                        HRESULT,
                        'GetCharacteristics',
                        (['out'], POINTER(DWORD), 'pdwCharacteristics'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddStreamSink')],
                        HRESULT,
                        'AddStreamSink',
                        (['in'], DWORD, 'dwStreamSinkIdentifier'),
                        (['in'], POINTER(IMFMediaType), 'pMediaType'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFStreamSink)),
                           'ppStreamSink'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveStreamSink')],
                        HRESULT,
                        'RemoveStreamSink',
                        (['in'], DWORD, 'dwStreamSinkIdentifier'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamSinkCount')],
                        HRESULT,
                        'GetStreamSinkCount',
                        (['out'], POINTER(DWORD), 'pcStreamSinkCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamSinkByIndex')],
                        HRESULT,
                        'GetStreamSinkByIndex',
                        (['in'], DWORD, 'dwIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFStreamSink)),
                           'ppStreamSink'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamSinkById')],
                        HRESULT,
                        'GetStreamSinkById',
                        (['in'], DWORD, 'dwStreamSinkIdentifier'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFStreamSink)),
                           'ppStreamSink'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetPresentationClock')],
                        HRESULT,
                        'SetPresentationClock',
                        (
                            ['in'],
                            POINTER(IMFPresentationClock),
                           'pPresentationClock'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPresentationClock')],
                        HRESULT,
                        'GetPresentationClock',
                        (
                            ['out'],
                            POINTER(POINTER(IMFPresentationClock)),
                           'ppPresentationClock'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Shutdown')],
                        HRESULT,
                        'Shutdown',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaSink_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0007
        # [local]
        class _MFSTREAMSINK_MARKER_TYPE(ENUM):
            MFSTREAMSINK_MARKER_DEFAULT = 0
            MFSTREAMSINK_MARKER_ENDOFSEGMENT = (
                MFSTREAMSINK_MARKER_DEFAULT + 1 )
            )
            MFSTREAMSINK_MARKER_TICK = MFSTREAMSINK_MARKER_ENDOFSEGMENT + 1 )
            MFSTREAMSINK_MARKER_EVENT = MFSTREAMSINK_MARKER_TICK + 1 )
        MFSTREAMSINK_MARKER_TYPE = _MFSTREAMSINK_MARKER_TYPE
        if not defined(__IMFStreamSink_INTERFACE_DEFINED__):
            # interface IMFStreamSink
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFStreamSink = MIDL_INTERFACE(
                    "{0A97B3CF-8E7C-4A3D-8F8C-0C843DC247FB}"
                )
                IMFStreamSink._iid_ = IID_IMFStreamSink


                IMFStreamSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetMediaSink')],
                        HRESULT,
                        'GetMediaSink',
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaSink)),
                           'ppMediaSink'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetIdentifier')],
                        HRESULT,
                        'GetIdentifier',
                        (['out'], POINTER(DWORD), 'pdwIdentifier'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMediaTypeHandler')],
                        HRESULT,
                        'GetMediaTypeHandler',
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaTypeHandler)),
                           'ppHandler'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessSample')],
                        HRESULT,
                        'ProcessSample',
                        (['in'], POINTER(IMFSample), 'pSample'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PlaceMarker')],
                        HRESULT,
                        'PlaceMarker',
                        (['in'], MFSTREAMSINK_MARKER_TYPE, 'eMarkerType'),
                        (['in'], POINTER(PROPVARIANT), 'pvarMarkerValue'),
                        (['in'], POINTER(PROPVARIANT), 'pvarContextValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Flush')],
                        HRESULT,
                        'Flush',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFStreamSink_INTERFACE_DEFINED__

        if not defined(__IMFVideoSampleAllocator_INTERFACE_DEFINED__):
            # interface IMFVideoSampleAllocator
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoSampleAllocator = MIDL_INTERFACE(
                    "{86CBC910-E533-4751-8E3B-F19B5B806A03}"
                )
                IMFVideoSampleAllocator._iid_ = IID_IMFVideoSampleAllocator


                IMFVideoSampleAllocator._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetDirectXManager')],
                        HRESULT,
                        'SetDirectXManager',
                        (
                            ['unique', 'in'],
                            POINTER(comtypes.IUnknown),
                           'pManager'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method UninitializeSampleAllocator')],
                        HRESULT,
                        'UninitializeSampleAllocator',
                    ),
                    COMMETHOD(
                        [helpstring('Method InitializeSampleAllocator')],
                        HRESULT,
                        'InitializeSampleAllocator',
                        (['in'], DWORD, 'cRequestedFrames'),
                        (['in'], POINTER(IMFMediaType), 'pMediaType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AllocateSample')],
                        HRESULT,
                        'AllocateSample',
                        (['out'], POINTER(POINTER(IMFSample)), 'ppSample'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoSampleAllocator_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0009
        # [local]
        if WINVER >= _WIN32_WINNT_WIN7:
            if not defined(__IMFVideoSampleAllocatorNotify_INTERFACE_DEFINED__):
                # interface IMFVideoSampleAllocatorNotify
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFVideoSampleAllocatorNotify = MIDL_INTERFACE(
                        "{A792CDBE-C374-4E89-8335-278E7B9956A4}"
                    )
                    IMFVideoSampleAllocatorNotify._iid_ = IID_IMFVideoSampleAllocatorNotify


                    IMFVideoSampleAllocatorNotify._methods_ = [
                        COMMETHOD(
                            [helpstring('Method NotifyRelease')],
                            HRESULT,
                            'NotifyRelease',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFVideoSampleAllocatorNotify_INTERFACE_DEFINED__

            if not defined(__IMFVideoSampleAllocatorNotifyEx_INTERFACE_DEFINED__):
                # interface IMFVideoSampleAllocatorNotifyEx
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFVideoSampleAllocatorNotifyEx = MIDL_INTERFACE(
                        "{3978AA1A-6D5B-4B7F-A340-90899189AE34}"
                    )
                    IMFVideoSampleAllocatorNotifyEx._iid_ = IID_IMFVideoSampleAllocatorNotifyEx


                    IMFVideoSampleAllocatorNotifyEx._methods_ = [
                        COMMETHOD(
                            [helpstring('Method NotifyPrune')],
                            HRESULT,
                            'NotifyPrune',
                            (
                                [],
                                POINTER(IMFSample),
                               '__MIDL__IMFVideoSampleAllocatorNotifyEx0000'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFVideoSampleAllocatorNotifyEx_INTERFACE_DEFINED__

            if not defined(__IMFVideoSampleAllocatorCallback_INTERFACE_DEFINED__):
                # interface IMFVideoSampleAllocatorCallback
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFVideoSampleAllocatorCallback = MIDL_INTERFACE(
                        "{992388B4-3372-4F67-8B6F-C84C071F4751}"
                    )
                    IMFVideoSampleAllocatorCallback._iid_ = IID_IMFVideoSampleAllocatorCallback


                    IMFVideoSampleAllocatorCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetCallback')],
                            HRESULT,
                            'SetCallback',
                            (
                                ['unique', 'in'],
                                POINTER(IMFVideoSampleAllocatorNotify),
                               'pNotify'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFreeSampleCount')],
                            HRESULT,
                            'GetFreeSampleCount',
                            (['out'], POINTER(LONG), 'plSamples'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFVideoSampleAllocatorCallback_INTERFACE_DEFINED__

            if not defined(__IMFVideoSampleAllocatorEx_INTERFACE_DEFINED__):
                # interface IMFVideoSampleAllocatorEx
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFVideoSampleAllocatorEx = MIDL_INTERFACE(
                        "{545B3A48-3283-4F62-866F-A62D8F598F9F}"
                    )
                    IMFVideoSampleAllocatorEx._iid_ = IID_IMFVideoSampleAllocatorEx


                    IMFVideoSampleAllocatorEx._methods_ = [
                        COMMETHOD(
                            [helpstring('Method InitializeSampleAllocatorEx')],
                            HRESULT,
                            'InitializeSampleAllocatorEx',
                            (['in'], DWORD, 'cInitialSamples'),
                            (['in'], DWORD, 'cMaximumSamples'),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                            (['in'], POINTER(IMFMediaType), 'pMediaType'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFVideoSampleAllocatorEx_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0013
            # [local]        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
        if WINVER >= _WIN32_WINNT_WINBLUE:
            if not defined(__IMFDXGIDeviceManagerSource_INTERFACE_DEFINED__):
                # interface IMFDXGIDeviceManagerSource
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFDXGIDeviceManagerSource = MIDL_INTERFACE(
                        "{20BC074B-7A8D-4609-8C3B-64A0A3B5D7CE}"
                    )
                    IMFDXGIDeviceManagerSource._iid_ = IID_IMFDXGIDeviceManagerSource


                    IMFDXGIDeviceManagerSource._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetManager')],
                            HRESULT,
                            'GetManager',
                            (
                                ['out'],
                                POINTER(POINTER(IMFDXGIDeviceManager)),
                               'ppManager'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFDXGIDeviceManagerSource_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0014
            # [local]        # END IF   (WINVER >= _WIN32_WINNT_WINBLUE)
        if WINVER >= _WIN32_WINNT_WIN8:
            class _MF_VIDEO_PROCESSOR_ROTATION(ENUM):
                ROTATION_NONE = 0
                ROTATION_NORMAL = 1

            MF_VIDEO_PROCESSOR_ROTATION = _MF_VIDEO_PROCESSOR_ROTATION


            class _MF_VIDEO_PROCESSOR_MIRROR(ENUM):
                MIRROR_NONE = 0
                MIRROR_HORIZONTAL = 1
                MIRROR_VERTICAL = 2

            MF_VIDEO_PROCESSOR_MIRROR = _MF_VIDEO_PROCESSOR_MIRROR
            if not defined(__IMFVideoProcessorControl_INTERFACE_DEFINED__):
                # interface IMFVideoProcessorControl
                # [unique][helpstring][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFVideoProcessorControl = MIDL_INTERFACE(
                        "{A3F675D5-6119-4F7F-A100-1D8B280F0EFB}"
                    )
                    IMFVideoProcessorControl._iid_ = IID_IMFVideoProcessorControl


                    IMFVideoProcessorControl._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetBorderColor')],
                            HRESULT,
                            'SetBorderColor',
                            (['in'], POINTER(MFARGB), 'pBorderColor'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSourceRectangle')],
                            HRESULT,
                            'SetSourceRectangle',
                            (['in'], POINTER(RECT), 'pSrcRect'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetDestinationRectangle')],
                            HRESULT,
                            'SetDestinationRectangle',
                            (['in'], POINTER(RECT), 'pDstRect'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetMirror')],
                            HRESULT,
                            'SetMirror',
                            (['in'], MF_VIDEO_PROCESSOR_MIRROR, 'eMirror'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetRotation')],
                            HRESULT,
                            'SetRotation',
                            (
                                ['in'],
                                MF_VIDEO_PROCESSOR_ROTATION,
                               'eRotation'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetConstrictionSize')],
                            HRESULT,
                            'SetConstrictionSize',
                            (['in'], POINTER(SIZE), 'pConstrictionSize'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFVideoProcessorControl_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0015
            # [local]
            if WINVER >= _WIN32_WINNT_WINBLUE:
                if not defined(__IMFVideoProcessorControl2_INTERFACE_DEFINED__):
                    # interface IMFVideoProcessorControl2
                    # [unique][uuid][local][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFVideoProcessorControl2 = MIDL_INTERFACE(
                            "{BDE633D3-E1DC-4A7F-A693-BBAE399C4A20}"
                        )
                        IMFVideoProcessorControl2._iid_ = IID_IMFVideoProcessorControl2


                        IMFVideoProcessorControl2._methods_ = [
                            COMMETHOD(
                                [helpstring('Method SetRotationOverride')],
                                HRESULT,
                                'SetRotationOverride',
                                (['in'], UINT, 'uiRotation'),
                            ),
                            COMMETHOD(
                                [helpstring('Method EnableHardwareEffects')],
                                HRESULT,
                                'EnableHardwareEffects',
                                (['in'], BOOL, 'fEnabled'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetSupportedHardwareEffects')],
                                HRESULT,
                                'GetSupportedHardwareEffects',
                                (['out'], POINTER(UINT), 'puiSupport'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFVideoProcessorControl2_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfidl_0000_0016
                # [local]
                if WINVER >= _WIN32_WINNT_WIN10:
                    class _MFVideoSphericalFormat(ENUM):
                        MFVideoSphericalFormat_Unsupported = 0
                        MFVideoSphericalFormat_Equirectangular = 1

                    MFVideoSphericalFormat = _MFVideoSphericalFormat
                # END IF  (WINVER >= _WIN32_WINNT_WIN10)

                if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                    MF_XVP_SAMPLE_LOCK_TIMEOUT = EXTERN_GUID(
                        0xAA4DDB29,
                        0x5134,
                        0x4363,
                        0xAC,
                        0x72,
                        0x83,
                        0xEC,
                        0x4B,
                        0xC1,
                        0x4,
                        0x26
                    )


                    class MFVideoSphericalProjectionMode(ENUM):
                        MFVideoSphericalProjectionMode_Spherical = 0
                        MFVideoSphericalProjectionMode_Flat = (
                            MFVideoSphericalProjectionMode_Spherical + 1 )
                        )
                    if not defined(__IMFVideoProcessorControl3_INTERFACE_DEFINED__):
                        # interface IMFVideoProcessorControl3
                        # [uuid][local][object]
                        if defined(__cplusplus) and not defined(CINTERFACE):
                            pass
                        else:
                            IID_IMFVideoProcessorControl3 = MIDL_INTERFACE(
                                "{2424B3F2-EB23-40F1-91AA-74BDDEEA0883}"
                            )
                            IMFVideoProcessorControl3._iid_ = IID_IMFVideoProcessorControl3


                            IMFVideoProcessorControl3._methods_ = [
                                COMMETHOD(
                                    [helpstring('Method GetNaturalOutputType')],
                                    HRESULT,
                                    'GetNaturalOutputType',
                                    (
                                        ['out'],
                                        POINTER(POINTER(IMFMediaType)),
                                       'ppType'
                                    ),
                                ),
                                COMMETHOD(
                                    [helpstring('Method EnableSphericalVideoProcessing')],
                                    HRESULT,
                                    'EnableSphericalVideoProcessing',
                                    (['in'], BOOL, 'fEnable'),
                                    (
                                        ['in'],
                                        MFVideoSphericalFormat,
                                       'eFormat'
                                    ),
                                    (
                                        ['in'],
                                        MFVideoSphericalProjectionMode,
                                       'eProjectionMode'
                                    ),
                                ),
                                COMMETHOD(
                                    [helpstring('Method SetSphericalVideoProperties')],
                                    HRESULT,
                                    'SetSphericalVideoProperties',
                                    (['in'], FLOAT, 'X'),
                                    (['in'], FLOAT, 'Y'),
                                    (['in'], FLOAT, 'Z'),
                                    (['in'], FLOAT, 'W'),
                                    (['in'], FLOAT, 'fieldOfView'),
                                ),
                                COMMETHOD(
                                    [helpstring('Method SetOutputDevice')],
                                    HRESULT,
                                    'SetOutputDevice',
                                    (
                                        ['in'],
                                        POINTER(comtypes.IUnknown),
                                       'pOutputDevice'
                                    ),
                                ),
                            ]

                        # END IF  C style interface
                    # END IF  __IMFVideoProcessorControl3_INTERFACE_DEFINED__

                    # interface __MIDL_itf_mfidl_0000_0017
                    # [local]                # END IF  (NTDDI_VERSION >= NTDDI_WIN10_RS3)
            # END IF   (WINVER >= _WIN32_WINNT_WINBLUE)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFTopology_INTERFACE_DEFINED__):
            # interface IMFTopology
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTopology = MIDL_INTERFACE(
                    "{83CF873A-F6DA-4BC8-823F-BACFD55DC433}"
                )
                IMFTopology._iid_ = IID_IMFTopology


                IMFTopology._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetTopologyID')],
                        HRESULT,
                        'GetTopologyID',
                        (['out'], POINTER(TOPOID), 'pID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddNode'), 'local'],
                        HRESULT,
                        'AddNode',
                        (['in'], POINTER(IMFTopologyNode), 'pNode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveNode'), 'local'],
                        HRESULT,
                        'RemoveNode',
                        (['in'], POINTER(IMFTopologyNode), 'pNode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNodeCount')],
                        HRESULT,
                        'GetNodeCount',
                        (['out'], POINTER(WORD), 'pwNodes'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNode')],
                        HRESULT,
                        'GetNode',
                        (['in'], WORD, 'wIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopologyNode)),
                           'ppNode'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Clear'), 'local'],
                        HRESULT,
                        'Clear',
                    ),
                    COMMETHOD(
                        [helpstring('Method CloneFrom')],
                        HRESULT,
                        'CloneFrom',
                        (['in'], POINTER(IMFTopology), 'pTopology'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNodeByID')],
                        HRESULT,
                        'GetNodeByID',
                        (['in'], TOPOID, 'qwTopoNodeID'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopologyNode)),
                           'ppNode'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSourceNodeCollection')],
                        HRESULT,
                        'GetSourceNodeCollection',
                        (
                            ['out'],
                            POINTER(POINTER(IMFCollection)),
                           'ppCollection'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputNodeCollection')],
                        HRESULT,
                        'GetOutputNodeCollection',
                        (
                            ['out'],
                            POINTER(POINTER(IMFCollection)),
                           'ppCollection'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTopology_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0018
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    MF_TOPOLOGY_PROJECTSTART = EXTERN_GUID(
        0x7ED3F802,
        0x86BB,
        0x4B3F,
        0xB7,
        0xE4,
        0x7C,
        0xB4,
        0x3A,
        0xFD,
        0x4B,
        0x80
    )
    MF_TOPOLOGY_PROJECTSTOP = EXTERN_GUID(
        0x7ED3F803,
        0x86BB,
        0x4B3F,
        0xB7,
        0xE4,
        0x7C,
        0xB4,
        0x3A,
        0xFD,
        0x4B,
        0x80
    )
    MF_TOPOLOGY_NO_MARKIN_MARKOUT = EXTERN_GUID(
        0x7ED3F804,
        0x86BB,
        0x4B3F,
        0xB7,
        0xE4,
        0x7C,
        0xB4,
        0x3A,
        0xFD,
        0x4B,
        0x80
    )
    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            class MFTOPOLOGY_DXVA_MODE(ENUM):
                MFTOPOLOGY_DXVA_DEFAULT = 0
                MFTOPOLOGY_DXVA_NONE = 1
                MFTOPOLOGY_DXVA_FULL = 2

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        MF_TOPOLOGY_DXVA_MODE = EXTERN_GUID(
            0x1E8D34F6,
            0xF5AB,
            0x4E23,
            0xBB,
            0x88,
            0x87,
            0x4A,
            0xA3,
            0xA1,
            0xA7,
            0x4D
        )
        MF_TOPOLOGY_ENABLE_XVP_FOR_PLAYBACK = EXTERN_GUID(
            0x1967731F,
            0xCD78,
            0x42FC,
            0xB0,
            0x26,
            0x9,
            0x92,
            0xA5,
            0x6E,
            0x56,
            0x93
        )
        MF_TOPOLOGY_STATIC_PLAYBACK_OPTIMIZATIONS = EXTERN_GUID(
            0xB86CAC42,
            0x41A6,
            0x4B79,
            0x89,
            0x7A,
            0x1A,
            0xB0,
            0xE5,
            0x2B,
            0x4A,
            0x1B
        )
        MF_TOPOLOGY_PLAYBACK_MAX_DIMS = EXTERN_GUID(
            0x5715CF19,
            0x5768,
            0x44AA,
            0xAD,
            0x6E,
            0x87,
            0x21,
            0xF1,
            0xB0,
            0xF9,
            0xBB
        )
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            class MFTOPOLOGY_HARDWARE_MODE(ENUM):
                MFTOPOLOGY_HWMODE_SOFTWARE_ONLY = 0
                MFTOPOLOGY_HWMODE_USE_HARDWARE = 1
                MFTOPOLOGY_HWMODE_USE_ONLY_HARDWARE = 2

            MF_TOPOLOGY_HARDWARE_MODE = EXTERN_GUID(
                0xD2D362FD,
                0x4E4F,
                0x4191,
                0xA5,
                0x79,
                0xC6,
                0x18,
                0xB6,
                0x67,
                0x6,
                0xAF
            )
            MF_TOPOLOGY_PLAYBACK_FRAMERATE = EXTERN_GUID(
                0xC164737A,
                0xC2B1,
                0x4553,
                0x83,
                0xBB,
                0x5A,
                0x52,
                0x60,
                0x72,
                0x44,
                0x8F
            )
            MF_TOPOLOGY_DYNAMIC_CHANGE_NOT_ALLOWED = EXTERN_GUID(
                0xD529950B,
                0xD484,
                0x4527,
                0xA9,
                0xCD,
                0xB1,
                0x90,
                0x95,
                0x32,
                0xB5,
                0xB0
            )
            MF_TOPOLOGY_ENUMERATE_SOURCE_TYPES = EXTERN_GUID(
                0x6248C36D,
                0x5D0B,
                0x4F40,
                0xA0,
                0xBB,
                0xB0,
                0xB3,
                0x05,
                0xF7,
                0x76,
                0x98
            )
            MF_TOPOLOGY_START_TIME_ON_PRESENTATION_SWITCH = EXTERN_GUID(
                0xC8CC113F,
                0x7951,
                0x4548,
                0xAA,
                0xD6,
                0x9E,
                0xD6,
                0x20,
                0x2E,
                0x62,
                0xB3
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINVER >= _WIN32_WINNT_WIN8:
        MF_DISABLE_LOCALLY_REGISTERED_PLUGINS = EXTERN_GUID(
            0x66B16DA9,
            0xADD4,
            0x47E0,
            0xA1,
            0x6B,
            0x5A,
            0xF1,
            0xFB,
            0x48,
            0x36,
            0x34
        )
        MF_LOCAL_PLUGIN_CONTROL_POLICY = EXTERN_GUID(
            0xD91B0085,
            0xC86D,
            0x4F81,
            0x88,
            0x22,
            0x8C,
            0x68,
            0xE1,
            0xD7,
            0xFA,
            0x04
        )
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP):
        mf = ctypes.windll.MF


        # STDAPI MFCreateTopology(
        # _Outptr_ IMFTopology ** ppTopo );
        MFCreateTopology = mf.MFCreateTopology
        MFCreateTopology.restype = STDAPI


        class MF_TOPOLOGY_TYPE(ENUM):
            MF_TOPOLOGY_OUTPUT_NODE = 0
            MF_TOPOLOGY_SOURCESTREAM_NODE = MF_TOPOLOGY_OUTPUT_NODE + 1 )
            MF_TOPOLOGY_TRANSFORM_NODE = MF_TOPOLOGY_SOURCESTREAM_NODE + 1 )
            MF_TOPOLOGY_TEE_NODE = MF_TOPOLOGY_TRANSFORM_NODE + 1 )
            MF_TOPOLOGY_MAX = 0xFFFFFFFF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFTopologyNode_INTERFACE_DEFINED__):
            # interface IMFTopologyNode
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTopologyNode = MIDL_INTERFACE(
                    "{83CF873A-F6DA-4BC8-823F-BACFD55DC430}"
                )
                IMFTopologyNode._iid_ = IID_IMFTopologyNode


                IMFTopologyNode._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetObject')],
                        HRESULT,
                        'SetObject',
                        (['in'], POINTER(comtypes.IUnknown), 'pObject'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetObject')],
                        HRESULT,
                        'GetObject',
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNodeType')],
                        HRESULT,
                        'GetNodeType',
                        (['out'], POINTER(MF_TOPOLOGY_TYPE), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTopoNodeID')],
                        HRESULT,
                        'GetTopoNodeID',
                        (['out'], POINTER(TOPOID), 'pID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetTopoNodeID')],
                        HRESULT,
                        'SetTopoNodeID',
                        (['in'], TOPOID, 'ullTopoID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputCount')],
                        HRESULT,
                        'GetInputCount',
                        (['out'], POINTER(DWORD), 'pcInputs'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputCount')],
                        HRESULT,
                        'GetOutputCount',
                        (['out'], POINTER(DWORD), 'pcOutputs'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ConnectOutput'), 'local'],
                        HRESULT,
                        'ConnectOutput',
                        (['in'], DWORD, 'dwOutputIndex'),
                        (['in'], POINTER(IMFTopologyNode), 'pDownstreamNode'),
                        (['in'], DWORD, 'dwInputIndexOnDownstreamNode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DisconnectOutput'), 'local'],
                        HRESULT,
                        'DisconnectOutput',
                        (['in'], DWORD, 'dwOutputIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInput')],
                        HRESULT,
                        'GetInput',
                        (['in'], DWORD, 'dwInputIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopologyNode)),
                           'ppUpstreamNode'
                        ),
                        (
                            ['out'],
                            POINTER(DWORD),
                           'pdwOutputIndexOnUpstreamNode'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutput')],
                        HRESULT,
                        'GetOutput',
                        (['in'], DWORD, 'dwOutputIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopologyNode)),
                           'ppDownstreamNode'
                        ),
                        (
                            ['out'],
                            POINTER(DWORD),
                           'pdwInputIndexOnDownstreamNode'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetOutputPrefType'), 'local'],
                        HRESULT,
                        'SetOutputPrefType',
                        (['in'], DWORD, 'dwOutputIndex'),
                        (['in'], POINTER(IMFMediaType), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputPrefType'), 'local'],
                        HRESULT,
                        'GetOutputPrefType',
                        (['in'], DWORD, 'dwOutputIndex'),
                        (['out'], POINTER(POINTER(IMFMediaType)), 'ppType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetInputPrefType'), 'local'],
                        HRESULT,
                        'SetInputPrefType',
                        (['in'], DWORD, 'dwInputIndex'),
                        (['in'], POINTER(IMFMediaType), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInputPrefType'), 'local'],
                        HRESULT,
                        'GetInputPrefType',
                        (['in'], DWORD, 'dwInputIndex'),
                        (['out'], POINTER(POINTER(IMFMediaType)), 'ppType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CloneFrom')],
                        HRESULT,
                        'CloneFrom',
                        (['in'], POINTER(IMFTopologyNode), 'pNode'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [in]            # [out]            # [size_is][size_is][out]            # [call_as]            # [in]            # [out]            # [size_is][size_is][out]        # END IF  __IMFTopologyNode_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0019
        # [local]
        class _MF_TOPONODE_FLUSH_MODE(ENUM):
            MF_TOPONODE_FLUSH_ALWAYS = 0
            MF_TOPONODE_FLUSH_SEEK = MF_TOPONODE_FLUSH_ALWAYS + 1 )
            MF_TOPONODE_FLUSH_NEVER = MF_TOPONODE_FLUSH_SEEK + 1 )
        MF_TOPONODE_FLUSH_MODE = _MF_TOPONODE_FLUSH_MODE
        MF_TOPONODE_FLUSH = EXTERN_GUID(
            0x494BBCE8,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )


        class _MF_TOPONODE_DRAIN_MODE(ENUM):
            MF_TOPONODE_DRAIN_DEFAULT = 0
            MF_TOPONODE_DRAIN_ALWAYS = MF_TOPONODE_DRAIN_DEFAULT + 1 )
            MF_TOPONODE_DRAIN_NEVER = MF_TOPONODE_DRAIN_ALWAYS + 1 )
        MF_TOPONODE_DRAIN_MODE = _MF_TOPONODE_DRAIN_MODE
        MF_TOPONODE_DRAIN = EXTERN_GUID(
            0x494BBCE9,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_D3DAWARE = EXTERN_GUID(
            0x494BBCED,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPOLOGY_RESOLUTION_STATUS = EXTERN_GUID(
            0x494BBCDE,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_ERRORCODE = EXTERN_GUID(
            0x494BBCEE,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_CONNECT_METHOD = EXTERN_GUID(
            0x494BBCF1,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_LOCKED = EXTERN_GUID(
            0x494BBCF7,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_WORKQUEUE_ID = EXTERN_GUID(
            0x494BBCF8,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_WORKQUEUE_MMCSS_CLASS = EXTERN_GUID(
            0x494BBCF9,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_DECRYPTOR = EXTERN_GUID(
            0x494BBCFA,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_DISCARDABLE = EXTERN_GUID(
            0x494BBCFB,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_ERROR_MAJORTYPE = EXTERN_GUID(
            0x494BBCFD,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_ERROR_SUBTYPE = EXTERN_GUID(
            0x494BBCFE,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_WORKQUEUE_MMCSS_TASKID = EXTERN_GUID(
            0x494BBCFF,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_WORKQUEUE_MMCSS_PRIORITY = EXTERN_GUID(
            0x5001F840,
            0x2816,
            0x48F4,
            0x93,
            0x64,
            0xAD,
            0x1E,
            0xF6,
            0x61,
            0xA1,
            0x23
        )
        MF_TOPONODE_WORKQUEUE_ITEM_PRIORITY = EXTERN_GUID(
            0xA1FF99BE,
            0x5E97,
            0x4A53,
            0xB4,
            0x94,
            0x56,
            0x8C,
            0x64,
            0x2C,
            0x0F,
            0xF3
        )
        MF_TOPONODE_MARKIN_HERE = EXTERN_GUID(
            0x494BBD00,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_MARKOUT_HERE = EXTERN_GUID(
            0x494BBD01,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_DECODER = EXTERN_GUID(
            0x494BBD02,
            0xB031,
            0x4E38,
            0x97,
            0xC4,
            0xD5,
            0x42,
            0x2D,
            0xD6,
            0x18,
            0xDC
        )
        MF_TOPONODE_MEDIASTART = EXTERN_GUID(
            0x835C58EA,
            0xE075,
            0x4BC7,
            0xBC,
            0xBA,
            0x4D,
            0xE0,
            0x00,
            0xDF,
            0x9A,
            0xE6
        )
        MF_TOPONODE_MEDIASTOP = EXTERN_GUID(
            0x835C58EB,
            0xE075,
            0x4BC7,
            0xBC,
            0xBA,
            0x4D,
            0xE0,
            0x00,
            0xDF,
            0x9A,
            0xE6
        )
        MF_TOPONODE_SOURCE = EXTERN_GUID(
            0x835C58EC,
            0xE075,
            0x4BC7,
            0xBC,
            0xBA,
            0x4D,
            0xE0,
            0x00,
            0xDF,
            0x9A,
            0xE6
        )
        MF_TOPONODE_PRESENTATION_DESCRIPTOR = EXTERN_GUID(
            0x835C58ED,
            0xE075,
            0x4BC7,
            0xBC,
            0xBA,
            0x4D,
            0xE0,
            0x00,
            0xDF,
            0x9A,
            0xE6
        )
        MF_TOPONODE_STREAM_DESCRIPTOR = EXTERN_GUID(
            0x835C58EE,
            0xE075,
            0x4BC7,
            0xBC,
            0xBA,
            0x4D,
            0xE0,
            0x00,
            0xDF,
            0x9A,
            0xE6
        )
        MF_TOPONODE_SEQUENCE_ELEMENTID = EXTERN_GUID(
            0x835C58EF,
            0xE075,
            0x4BC7,
            0xBC,
            0xBA,
            0x4D,
            0xE0,
            0x00,
            0xDF,
            0x9A,
            0xE6
        )
        MF_TOPONODE_TRANSFORM_OBJECTID = EXTERN_GUID(
            0x88DCC0C9,
            0x293E,
            0x4E8B,
            0x9A,
            0xEB,
            0xA,
            0xD6,
            0x4C,
            0xC0,
            0x16,
            0xB0
        )
        MF_TOPONODE_STREAMID = EXTERN_GUID(
            0x14932F9B,
            0x9087,
            0x4BB4,
            0x84,
            0x12,
            0x51,
            0x67,
            0x14,
            0x5C,
            0xBE,
            0x04
        )
        MF_TOPONODE_NOSHUTDOWN_ON_REMOVE = EXTERN_GUID(
            0x14932F9C,
            0x9087,
            0x4BB4,
            0x84,
            0x12,
            0x51,
            0x67,
            0x14,
            0x5C,
            0xBE,
            0x04
        )
        MF_TOPONODE_RATELESS = EXTERN_GUID(
            0x14932F9D,
            0x9087,
            0x4BB4,
            0x84,
            0x12,
            0x51,
            0x67,
            0x14,
            0x5C,
            0xBE,
            0x04
        )
        MF_TOPONODE_DISABLE_PREROLL = EXTERN_GUID(
            0x14932F9E,
            0x9087,
            0x4BB4,
            0x84,
            0x12,
            0x51,
            0x67,
            0x14,
            0x5C,
            0xBE,
            0x04
        )
        MF_TOPONODE_PRIMARYOUTPUT = EXTERN_GUID(
            0x6304EF99,
            0x16B2,
            0x4EBE,
            0x9D,
            0x67,
            0xE4,
            0xC5,
            0x39,
            0xB3,
            0xA2,
            0x59
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP):
        mf = ctypes.windll.MF


        # STDAPI MFCreateTopologyNode(
        # MF_TOPOLOGY_TYPE NodeType,
        # _Outptr_ IMFTopologyNode ** ppNode );
        MFCreateTopologyNode = mf.MFCreateTopologyNode
        MFCreateTopologyNode.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if WINVER >= _WIN32_WINNT_WIN7:
            mf = ctypes.windll.MF


            # STDAPI MFGetTopoNodeCurrentType(
            # IMFTopologyNode* pNode,
            # DWORD dwStreamIndex,
            # BOOL fOutput,
            # _Outptr_ IMFMediaType** ppType);
            MFGetTopoNodeCurrentType = mf.MFGetTopoNodeCurrentType
            MFGetTopoNodeCurrentType.restype = STDAPI


        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFGetService_INTERFACE_DEFINED__):
            # interface IMFGetService
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFGetService = MIDL_INTERFACE(
                    "{FA993888-4383-415A-A930-DD472A8CF6F7}"
                )
                IMFGetService._iid_ = IID_IMFGetService


                IMFGetService._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetService')],
                        HRESULT,
                        'GetService',
                        (['in'], REFGUID, 'guidService'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(LPVOID), 'ppvObject'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFGetService_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0020
        # [local]
        mf = ctypes.windll.MF


        # STDAPI MFGetService(
        # IUnknown* punkObject,
        # REFGUID guidService,
        # REFIID riid,
        # _Outptr_ LPVOID* ppvObject
        # );
        MFGetService = mf.MFGetService
        MFGetService.restype = STDAPI


        MFTIME = LONGLONG


        class _MFCLOCK_CHARACTERISTICS_FLAGS(ENUM):
            MFCLOCK_CHARACTERISTICS_FLAG_FREQUENCY_10MHZ = 0x2
            MFCLOCK_CHARACTERISTICS_FLAG_ALWAYS_RUNNING = 0x4
            MFCLOCK_CHARACTERISTICS_FLAG_IS_SYSTEM_CLOCK = 0x8

        MFCLOCK_CHARACTERISTICS_FLAGS = _MFCLOCK_CHARACTERISTICS_FLAGS


        class _MFCLOCK_STATE(ENUM):
            MFCLOCK_STATE_INVALID = 0
            MFCLOCK_STATE_RUNNING = MFCLOCK_STATE_INVALID + 1 )
            MFCLOCK_STATE_STOPPED = MFCLOCK_STATE_RUNNING + 1 )
            MFCLOCK_STATE_PAUSED = MFCLOCK_STATE_STOPPED + 1 )
        MFCLOCK_STATE = _MFCLOCK_STATE


        class _MFCLOCK_RELATIONAL_FLAGS(ENUM):
            MFCLOCK_RELATIONAL_FLAG_JITTER_NEVER_AHEAD = 0x1

        MFCLOCK_RELATIONAL_FLAGS = _MFCLOCK_RELATIONAL_FLAGS
        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF


        _MFCLOCK_PROPERTIES._fields_ = [
            ('INT64 qwCorrelationRate', UINT),
            ('guidClockId', GUID),
            ('dwClockFlags', DWORD),
            ('INT64 qwClockFrequency', UINT),
            ('dwClockTolerance', DWORD),
            ('dwClockJitter', DWORD),
        ]
        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF


        if not defined(__IMFClock_INTERFACE_DEFINED__):
            # interface IMFClock
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFClock = MIDL_INTERFACE(
                    "{2EB1E945-18B8-4139-9B1A-D5D584818530}"
                )
                IMFClock._iid_ = IID_IMFClock


                IMFClock._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetClockCharacteristics')],
                        HRESULT,
                        'GetClockCharacteristics',
                        (['out'], POINTER(DWORD), 'pdwCharacteristics'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCorrelatedTime')],
                        HRESULT,
                        'GetCorrelatedTime',
                        (['in'], DWORD, 'dwReserved'),
                        (['out'], POINTER(LONGLONG), 'pllClockTime'),
                        (['out'], POINTER(MFTIME), 'phnsSystemTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetContinuityKey')],
                        HRESULT,
                        'GetContinuityKey',
                        (['out'], POINTER(DWORD), 'pdwContinuityKey'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetState')],
                        HRESULT,
                        'GetState',
                        (['in'], DWORD, 'dwReserved'),
                        (['out'], POINTER(MFCLOCK_STATE), 'peClockState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProperties')],
                        HRESULT,
                        'GetProperties',
                        (
                            ['out'],
                            POINTER(MFCLOCK_PROPERTIES),
                           'pClockProperties'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFClock_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0021
        # [local]
        mfplat = ctypes.windll.MFPLAT


        # STDAPI_(MFTIME)
        # MFGetSystemTime(
        # );
        MFGetSystemTime = mfplat.MFGetSystemTime
        MFGetSystemTime.restype = STDAPI_(MFTIME)


        if not defined(__IMFPresentationClock_INTERFACE_DEFINED__):
            # interface IMFPresentationClock
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFPresentationClock = MIDL_INTERFACE(
                    "{868CE85C-8EA9-4F55-AB82-B009A910A805}"
                )
                IMFPresentationClock._iid_ = IID_IMFPresentationClock


                IMFPresentationClock._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetTimeSource')],
                        HRESULT,
                        'SetTimeSource',
                        (
                            ['in'],
                            POINTER(IMFPresentationTimeSource),
                           'pTimeSource'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTimeSource')],
                        HRESULT,
                        'GetTimeSource',
                        (
                            ['out'],
                            POINTER(POINTER(IMFPresentationTimeSource)),
                           'ppTimeSource'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTime')],
                        HRESULT,
                        'GetTime',
                        (['out'], POINTER(MFTIME), 'phnsClockTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddClockStateSink')],
                        HRESULT,
                        'AddClockStateSink',
                        (['in'], POINTER(IMFClockStateSink), 'pStateSink'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveClockStateSink')],
                        HRESULT,
                        'RemoveClockStateSink',
                        (['in'], POINTER(IMFClockStateSink), 'pStateSink'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Start')],
                        HRESULT,
                        'Start',
                        (['in'], LONGLONG, 'llClockStartOffset'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Stop')],
                        HRESULT,
                        'Stop',
                    ),
                    COMMETHOD(
                        [helpstring('Method Pause')],
                        HRESULT,
                        'Pause',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFPresentationClock_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0022
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP):
        mf = ctypes.windll.MF


        # STDAPI MFCreatePresentationClock(
        # _Outptr_ IMFPresentationClock** ppPresentationClock
        # );
        MFCreatePresentationClock = mf.MFCreatePresentationClock
        MFCreatePresentationClock.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFPresentationTimeSource_INTERFACE_DEFINED__):
            # interface IMFPresentationTimeSource
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFPresentationTimeSource = MIDL_INTERFACE(
                    "{7FF12CCE-F76F-41C2-863B-1666C8E5E139}"
                )
                IMFPresentationTimeSource._iid_ = IID_IMFPresentationTimeSource


                IMFPresentationTimeSource._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetUnderlyingClock')],
                        HRESULT,
                        'GetUnderlyingClock',
                        (['out'], POINTER(POINTER(IMFClock)), 'ppClock'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFPresentationTimeSource_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0023
        # [local]
        mfplat = ctypes.windll.MFPLAT


        # STDAPI
        # MFCreateSystemTimeSource(
        # _Outptr_ IMFPresentationTimeSource** ppSystemTimeSource
        # );
        MFCreateSystemTimeSource = mfplat.MFCreateSystemTimeSource
        MFCreateSystemTimeSource.restype = STDAPI


        if not defined(__IMFClockStateSink_INTERFACE_DEFINED__):
            # interface IMFClockStateSink
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFClockStateSink = MIDL_INTERFACE(
                    "{F6696E82-74F7-4F3D-A178-8A5E09C3659F}"
                )
                IMFClockStateSink._iid_ = IID_IMFClockStateSink


                IMFClockStateSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnClockStart')],
                        HRESULT,
                        'OnClockStart',
                        (['in'], MFTIME, 'hnsSystemTime'),
                        (['in'], LONGLONG, 'llClockStartOffset'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnClockStop')],
                        HRESULT,
                        'OnClockStop',
                        (['in'], MFTIME, 'hnsSystemTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnClockPause')],
                        HRESULT,
                        'OnClockPause',
                        (['in'], MFTIME, 'hnsSystemTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnClockRestart')],
                        HRESULT,
                        'OnClockRestart',
                        (['in'], MFTIME, 'hnsSystemTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnClockSetRate')],
                        HRESULT,
                        'OnClockSetRate',
                        (['in'], MFTIME, 'hnsSystemTime'),
                        (['in'], FLOAT, 'flRate'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFClockStateSink_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0024
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        MF_PD_PMPHOST_CONTEXT = EXTERN_GUID(
            0x6C990D31,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
        MF_PD_APP_CONTEXT = EXTERN_GUID(
            0x6C990D32,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        MF_PD_DURATION = EXTERN_GUID(
            0x6C990D33,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
        MF_PD_TOTAL_FILE_SIZE = EXTERN_GUID(
            0x6C990D34,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
        MF_PD_AUDIO_ENCODING_BITRATE = EXTERN_GUID(
            0x6C990D35,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
        MF_PD_VIDEO_ENCODING_BITRATE = EXTERN_GUID(
            0x6C990D36,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
        MF_PD_MIME_TYPE = EXTERN_GUID(
            0x6C990D37,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
        MF_PD_LAST_MODIFIED_TIME = EXTERN_GUID(
            0x6C990D38,
            0xBB8E,
            0x477A,
            0x85,
            0x98,
            0xD,
            0x5D,
            0x96,
            0xFC,
            0xD8,
            0x8A
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            MF_PD_PLAYBACK_ELEMENT_ID = EXTERN_GUID(
                0x6C990D39,
                0xBB8E,
                0x477A,
                0x85,
                0x98,
                0xD,
                0x5D,
                0x96,
                0xFC,
                0xD8,
                0x8A
            )
            MF_PD_PREFERRED_LANGUAGE = EXTERN_GUID(
                0x6C990D3A,
                0xBB8E,
                0x477A,
                0x85,
                0x98,
                0xD,
                0x5D,
                0x96,
                0xFC,
                0xD8,
                0x8A
            )
            MF_PD_PLAYBACK_BOUNDARY_TIME = EXTERN_GUID(
                0x6C990D3B,
                0xBB8E,
                0x477A,
                0x85,
                0x98,
                0xD,
                0x5D,
                0x96,
                0xFC,
                0xD8,
                0x8A
            )
            MF_PD_AUDIO_ISVARIABLEBITRATE = EXTERN_GUID(
                0x33026EE0,
                0xE387,
                0x4582,
                0xAE,
                0x0A,
                0x34,
                0xA2,
                0xAD,
                0x3B,
                0xAA,
                0x18
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
            MF_PD_ADAPTIVE_STREAMING = DEFINE_GUID(
                0xEA0D5D97,
                0x29F9,
                0x488B,
                0xAE,
                0x6B,
                0x7D,
                0x6B,
                0x41,
                0x36,
                0x11,
                0x2B
            )
        # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

        if not defined(__IMFPresentationDescriptor_INTERFACE_DEFINED__):
            # interface IMFPresentationDescriptor
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFPresentationDescriptor = MIDL_INTERFACE(
                    "{03CB2711-24D7-4DB6-A17F-F3A7A479A536}"
                )
                IMFPresentationDescriptor._iid_ = IID_IMFPresentationDescriptor


                IMFPresentationDescriptor._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetStreamDescriptorCount')],
                        HRESULT,
                        'GetStreamDescriptorCount',
                        (['out'], POINTER(DWORD), 'pdwDescriptorCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamDescriptorByIndex')],
                        HRESULT,
                        'GetStreamDescriptorByIndex',
                        (['in'], DWORD, 'dwIndex'),
                        (['out'], POINTER(BOOL), 'pfSelected'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFStreamDescriptor)),
                           'ppDescriptor'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SelectStream')],
                        HRESULT,
                        'SelectStream',
                        (['in'], DWORD, 'dwDescriptorIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeselectStream')],
                        HRESULT,
                        'DeselectStream',
                        (['in'], DWORD, 'dwDescriptorIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Clone')],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IMFPresentationDescriptor)),
                           'ppPresentationDescriptor'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFPresentationDescriptor_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0025
        # [local]
        mfplat = ctypes.windll.MFPLAT


        # STDAPI MFCreatePresentationDescriptor(
        # DWORD cStreamDescriptors,
        # _In_reads_opt_( cStreamDescriptors ) IMFStreamDescriptor** apStreamDescriptors,
        # _Outptr_ IMFPresentationDescriptor** ppPresentationDescriptor
        # );
        MFCreatePresentationDescriptor = mfplat.MFCreatePresentationDescriptor
        MFCreatePresentationDescriptor.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        mf = ctypes.windll.MF


        # STDAPI MFRequireProtectedEnvironment(
        # _In_ IMFPresentationDescriptor* pPresentationDescriptor
        # );
        MFRequireProtectedEnvironment = mf.MFRequireProtectedEnvironment
        MFRequireProtectedEnvironment.restype = STDAPI


        mfplat = ctypes.windll.MFPLAT


        # STDAPI MFSerializePresentationDescriptor(
        # _In_ IMFPresentationDescriptor * pPD,
        # _Out_ DWORD * pcbData,
        # _Outptr_result_bytebuffer_to_(*pcbData, *pcbData) BYTE ** ppbData);
        MFSerializePresentationDescriptor = (
            mfplat.MFSerializePresentationDescriptor
        )
        MFSerializePresentationDescriptor.restype = STDAPI


        # STDAPI MFDeserializePresentationDescriptor(
        # _In_ DWORD cbData,
        # _In_reads_( cbData ) BYTE * pbData,
        # _Outptr_ IMFPresentationDescriptor ** ppPD);
        MFDeserializePresentationDescriptor = (
            mfplat.MFDeserializePresentationDescriptor
        )
        MFDeserializePresentationDescriptor.restype = STDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        MF_SD_LANGUAGE = EXTERN_GUID(
            0xAF2180,
            0xBDC2,
            0x423C,
            0xAB,
            0xCA,
            0xF5,
            0x3,
            0x59,
            0x3B,
            0xC1,
            0x21
        )
        MF_SD_PROTECTED = EXTERN_GUID(
            0xAF2181,
            0xBDC2,
            0x423C,
            0xAB,
            0xCA,
            0xF5,
            0x3,
            0x59,
            0x3B,
            0xC1,
            0x21
        )
        MF_SD_STREAM_NAME = EXTERN_GUID(
            0x4F1B099D,
            0xD314,
            0x41E5,
            0xA7,
            0x81,
            0x7F,
            0xEF,
            0xAA,
            0x4C,
            0x50,
            0x1F
        )
        MF_SD_MUTUALLY_EXCLUSIVE = EXTERN_GUID(
            0x23EF79C,
            0x388D,
            0x487F,
            0xAC,
            0x17,
            0x69,
            0x6C,
            0xD6,
            0xE3,
            0xC6,
            0xF5
        )
        if not defined(__IMFStreamDescriptor_INTERFACE_DEFINED__):
            # interface IMFStreamDescriptor
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFStreamDescriptor = MIDL_INTERFACE(
                    "{56C03D9C-9DBB-45F5-AB4B-D80F47C05938}"
                )
                IMFStreamDescriptor._iid_ = IID_IMFStreamDescriptor


                IMFStreamDescriptor._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetStreamIdentifier')],
                        HRESULT,
                        'GetStreamIdentifier',
                        (['out'], POINTER(DWORD), 'pdwStreamIdentifier'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMediaTypeHandler')],
                        HRESULT,
                        'GetMediaTypeHandler',
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaTypeHandler)),
                           'ppMediaTypeHandler'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFStreamDescriptor_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0026
        # [local]
        mfplat = ctypes.windll.MFPLAT


        # STDAPI MFCreateStreamDescriptor(
        # DWORD dwStreamIdentifier,
        # DWORD cMediaTypes,
        # _In_reads_(cMediaTypes) IMFMediaType** apMediaTypes,
        # _Outptr_ IMFStreamDescriptor** ppDescriptor
        # );
        MFCreateStreamDescriptor = mfplat.MFCreateStreamDescriptor
        MFCreateStreamDescriptor.restype = STDAPI


        if not defined(__IMFMediaTypeHandler_INTERFACE_DEFINED__):
            # interface IMFMediaTypeHandler
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaTypeHandler = MIDL_INTERFACE(
                    "{E93DCF6C-4B07-4E1E-8123-AA16ED6EADF5}"
                )
                IMFMediaTypeHandler._iid_ = IID_IMFMediaTypeHandler


                IMFMediaTypeHandler._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsMediaTypeSupported'), 'local'],
                        HRESULT,
                        'IsMediaTypeSupported',
                        (['in'], POINTER(IMFMediaType), 'pMediaType'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaType)),
                           'ppMediaType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMediaTypeCount')],
                        HRESULT,
                        'GetMediaTypeCount',
                        (['out'], POINTER(DWORD), 'pdwTypeCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMediaTypeByIndex'), 'local'],
                        HRESULT,
                        'GetMediaTypeByIndex',
                        (['in'], DWORD, 'dwIndex'),
                        (['out'], POINTER(POINTER(IMFMediaType)), 'ppType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetCurrentMediaType'), 'local'],
                        HRESULT,
                        'SetCurrentMediaType',
                        (['in'], POINTER(IMFMediaType), 'pMediaType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCurrentMediaType'), 'local'],
                        HRESULT,
                        'GetCurrentMediaType',
                        (
                            ['out'],
                            POINTER(POINTER(IMFMediaType)),
                           'ppMediaType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMajorType')],
                        HRESULT,
                        'GetMajorType',
                        (['out'], POINTER(GUID), 'pguidMajorType'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [size_is][in]            # [in]            # [size_is][size_is][out]            # [out]            # [call_as]            # [in]            # [size_is][size_is][out]            # [out]            # [call_as]            # [size_is][in]            # [in]            # [call_as]            # [size_is][size_is][out]            # [out]        # END IF  __IMFMediaTypeHandler_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0027
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        mf = ctypes.windll.MF


        # STDAPI MFCreateSimpleTypeHandler(
        # _Outptr_ IMFMediaTypeHandler ** ppHandler );
        MFCreateSimpleTypeHandler = mf.MFCreateSimpleTypeHandler
        MFCreateSimpleTypeHandler.restype = STDAPI


        class MFTIMER_FLAGS(ENUM):
            MFTIMER_RELATIVE = 0x1

        if not defined(__IMFTimer_INTERFACE_DEFINED__):
            # interface IMFTimer
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTimer = MIDL_INTERFACE(
                    "{E56E4CBD-8F70-49D8-A0F8-EDB3D6AB9BF2}"
                )
                IMFTimer._iid_ = IID_IMFTimer


                IMFTimer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetTimer')],
                        HRESULT,
                        'SetTimer',
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], LONGLONG, 'llClockTime'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppunkKey'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method CancelTimer')],
                        HRESULT,
                        'CancelTimer',
                        (['in'], POINTER(comtypes.IUnknown), 'punkKey'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTimer_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0028
        # [local]
        MF_ACTIVATE_CUSTOM_VIDEO_MIXER_CLSID = EXTERN_GUID(
            0xBA491360,
            0xBE50,
            0x451E,
            0x95,
            0xAB,
            0x6D,
            0x4A,
            0xCC,
            0xC7,
            0xDA,
            0xD8
        )
        MF_ACTIVATE_CUSTOM_VIDEO_MIXER_ACTIVATE = EXTERN_GUID(
            0xBA491361,
            0xBE50,
            0x451E,
            0x95,
            0xAB,
            0x6D,
            0x4A,
            0xCC,
            0xC7,
            0xDA,
            0xD8
        )
        MF_ACTIVATE_CUSTOM_VIDEO_MIXER_FLAGS = EXTERN_GUID(
            0xBA491362,
            0xBE50,
            0x451E,
            0x95,
            0xAB,
            0x6D,
            0x4A,
            0xCC,
            0xC7,
            0xDA,
            0xD8
        )
        MF_ACTIVATE_CUSTOM_VIDEO_PRESENTER_CLSID = EXTERN_GUID(
            0xBA491364,
            0xBE50,
            0x451E,
            0x95,
            0xAB,
            0x6D,
            0x4A,
            0xCC,
            0xC7,
            0xDA,
            0xD8
        )
        MF_ACTIVATE_CUSTOM_VIDEO_PRESENTER_ACTIVATE = EXTERN_GUID(
            0xBA491365,
            0xBE50,
            0x451E,
            0x95,
            0xAB,
            0x6D,
            0x4A,
            0xCC,
            0xC7,
            0xDA,
            0xD8
        )
        MF_ACTIVATE_CUSTOM_VIDEO_PRESENTER_FLAGS = EXTERN_GUID(
            0xBA491366,
            0xBE50,
            0x451E,
            0x95,
            0xAB,
            0x6D,
            0x4A,
            0xCC,
            0xC7,
            0xDA,
            0xD8
        )


        class __MIDL___MIDL_itf_mfidl_0000_0028_0001(ENUM):
            MF_ACTIVATE_CUSTOM_MIXER_ALLOWFAIL = 0x1

        MF_ACTIVATE_CUSTOM_MIXER_ALLOWFAIL = __MIDL___MIDL_itf_mfidl_0000_0028_0001.MF_ACTIVATE_CUSTOM_MIXER_ALLOWFAIL


        class __MIDL___MIDL_itf_mfidl_0000_0028_0002(ENUM):
            MF_ACTIVATE_CUSTOM_PRESENTER_ALLOWFAIL = 0x1

        MF_ACTIVATE_CUSTOM_PRESENTER_ALLOWFAIL = __MIDL___MIDL_itf_mfidl_0000_0028_0002.MF_ACTIVATE_CUSTOM_PRESENTER_ALLOWFAIL
        MF_ACTIVATE_MFT_LOCKED = EXTERN_GUID(
            0xC1F6093C,
            0x7F65,
            0x4FBD,
            0x9E,
            0x39,
            0x5F,
            0xAE,
            0xC3,
            0xC4,
            0xFB,
            0xD7
        )
        MF_ACTIVATE_VIDEO_WINDOW = EXTERN_GUID(
            0x9A2DBBDD,
            0xF57E,
            0x4162,
            0x82,
            0xB9,
            0x68,
            0x31,
            0x37,
            0x76,
            0x82,
            0xD3
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MFSHUTDOWN_STATUS(ENUM):
            MFSHUTDOWN_INITIATED = 0
            MFSHUTDOWN_COMPLETED = MFSHUTDOWN_INITIATED + 1 )
        MFSHUTDOWN_STATUS = _MFSHUTDOWN_STATUS
        if not defined(__IMFShutdown_INTERFACE_DEFINED__):
            # interface IMFShutdown
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFShutdown = MIDL_INTERFACE(
                    "{97EC2EA4-0E42-4937-97AC-9D6D328824E1}"
                )
                IMFShutdown._iid_ = IID_IMFShutdown


                IMFShutdown._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Shutdown')],
                        HRESULT,
                        'Shutdown',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetShutdownStatus')],
                        HRESULT,
                        'GetShutdownStatus',
                        (['out'], POINTER(MFSHUTDOWN_STATUS), 'pStatus'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFShutdown_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0029
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        mf = ctypes.windll.MF


        # STDAPI
        # MFShutdownObject(
        # IUnknown * pUnk );
        MFShutdownObject = mf.MFShutdownObject
        MFShutdownObject.restype = STDAPI


        # STDAPI
        # MFCreateAudioRenderer(
        # IMFAttributes* pAudioAttributes,
        # _Outptr_ IMFMediaSink** ppSink
        # );
        MFCreateAudioRenderer = mf.MFCreateAudioRenderer
        MFCreateAudioRenderer.restype = STDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP):
        mf = ctypes.windll.MF


        # STDAPI
        # MFCreateAudioRendererActivate(
        # _Outptr_ IMFActivate ** ppActivate
        # );
        MFCreateAudioRendererActivate = mf.MFCreateAudioRendererActivate
        MFCreateAudioRendererActivate.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_PC_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        MF_AUDIO_RENDERER_ATTRIBUTE_FLAGS = EXTERN_GUID(
            0xEDE4B5E0,
            0xF805,
            0x4D6C,
            0x99,
            0xB3,
            0xDB,
            0x01,
            0xBF,
            0x95,
            0xDF,
            0xAB
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        MF_AUDIO_RENDERER_ATTRIBUTE_SESSION_ID = EXTERN_GUID(
            0xEDE4B5E3,
            0xF805,
            0x4D6C,
            0x99,
            0xB3,
            0xDB,
            0x01,
            0xBF,
            0x95,
            0xDF,
            0xAB
        )
        MF_AUDIO_RENDERER_ATTRIBUTE_ENDPOINT_ID = EXTERN_GUID(
            0xB10AAEC3,
            0xEF71,
            0x4CC3,
            0xB8,
            0x73,
            0x5,
            0xA9,
            0xA0,
            0x8B,
            0x9F,
            0x8E
        )
        MF_AUDIO_RENDERER_ATTRIBUTE_ENDPOINT_ROLE = EXTERN_GUID(
            0x6BA644FF,
            0x27C5,
            0x4D02,
            0x98,
            0x87,
            0xC2,
            0x86,
            0x19,
            0xFD,
            0xB9,
            0x1B
        )
        MF_AUDIO_RENDERER_ATTRIBUTE_STREAM_CATEGORY = EXTERN_GUID(
            0xA9770471,
            0x92EC,
            0x4DF4,
            0x94,
            0xFE,
            0x81,
            0xC3,
            0x6F,
            0xC,
            0x3A,
            0x7A
        )
        mf = ctypes.windll.MF


        # STDAPI
        # MFCreateVideoRendererActivate(
        # _In_ HWND hwndVideo,
        # _Outptr_ IMFActivate ** ppActivate
        # );
        MFCreateVideoRendererActivate = mf.MFCreateVideoRendererActivate
        MFCreateVideoRendererActivate.restype = STDAPI


        if WINVER >= _WIN32_WINNT_WIN7:
            mf = ctypes.windll.MF


            # STDAPI
            # MFCreateMPEG4MediaSink(
            # _In_ IMFByteStream* pIByteStream,
            # _In_opt_ IMFMediaType* pVideoMediaType,
            # _In_opt_ IMFMediaType* pAudioMediaType,
            # _Outptr_ IMFMediaSink** ppIMediaSink
            # );
            MFCreateMPEG4MediaSink = mf.MFCreateMPEG4MediaSink
            MFCreateMPEG4MediaSink.restype = STDAPI


            # STDAPI
            # MFCreate3GPMediaSink(
            # _In_ IMFByteStream* pIByteStream,
            # _In_opt_ IMFMediaType* pVideoMediaType,
            # _In_opt_ IMFMediaType* pAudioMediaType,
            # _Outptr_ IMFMediaSink** ppIMediaSink
            # );
            MFCreate3GPMediaSink = mf.MFCreate3GPMediaSink
            MFCreate3GPMediaSink.restype = STDAPI


            # STDAPI
            # MFCreateMP3MediaSink(
            # _In_ IMFByteStream* pTargetByteStream,
            # _Outptr_ IMFMediaSink** ppMediaSink
            # );
            MFCreateMP3MediaSink = mf.MFCreateMP3MediaSink
            MFCreateMP3MediaSink.restype = STDAPI

        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINVER >= _WIN32_WINNT_WIN8:
            mf = ctypes.windll.MF


            # STDAPI
            # MFCreateAC3MediaSink(
            # _In_ IMFByteStream* pTargetByteStream,
            # _In_ IMFMediaType* pAudioMediaType,
            # _Outptr_ IMFMediaSink** ppMediaSink
            # );
            MFCreateAC3MediaSink = mf.MFCreateAC3MediaSink
            MFCreateAC3MediaSink.restype = STDAPI


            # STDAPI
            # MFCreateADTSMediaSink(
            # _In_ IMFByteStream* pTargetByteStream,
            # _In_ IMFMediaType* pAudioMediaType,
            # _Outptr_ IMFMediaSink** ppMediaSink
            # );
            MFCreateADTSMediaSink = mf.MFCreateADTSMediaSink
            MFCreateADTSMediaSink.restype = STDAPI


            # STDAPI
            # MFCreateMuxSink(
            # _In_ GUID guidOutputSubType,
            # _In_opt_ IMFAttributes* pOutputAttributes,
            # _In_opt_ IMFByteStream* pOutputByteStream,
            # _Outptr_ IMFMediaSink** ppMuxSink
            # );
            MFCreateMuxSink = mf.MFCreateMuxSink
            MFCreateMuxSink.restype = STDAPI


            # STDAPI
            # MFCreateFMPEG4MediaSink(
            # _In_ IMFByteStream* pIByteStream,
            # _In_opt_ IMFMediaType* pVideoMediaType,
            # _In_opt_ IMFMediaType* pAudioMediaType,
            # _Outptr_ IMFMediaSink** ppIMediaSink
            # );
            MFCreateFMPEG4MediaSink = mf.MFCreateFMPEG4MediaSink
            MFCreateFMPEG4MediaSink.restype = STDAPI

        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        if WINVER >= _WIN32_WINNT_WINBLUE:
            mf = ctypes.windll.MF


            # STDAPI
            # MFCreateAVIMediaSink(
            # _In_ IMFByteStream* pIByteStream,
            # _In_ IMFMediaType* pVideoMediaType,
            # _In_opt_ IMFMediaType* pAudioMediaType,
            # _Outptr_ IMFMediaSink** ppIMediaSink
            # );
            MFCreateAVIMediaSink = mf.MFCreateAVIMediaSink
            MFCreateAVIMediaSink.restype = STDAPI


        # END IF   (WINVER >= _WIN32_WINNT_WINBLUE)

        if WINVER >= _WIN32_WINNT_WINBLUE:
            mf = ctypes.windll.MF


            # STDAPI
            # MFCreateWAVEMediaSink(
            # _In_ IMFByteStream* pTargetByteStream,
            # _In_ IMFMediaType* pAudioMediaType,
            # _Outptr_ IMFMediaSink** ppMediaSink
            # );
            MFCreateWAVEMediaSink = mf.MFCreateWAVEMediaSink
            MFCreateWAVEMediaSink.restype = STDAPI


        # END IF   (WINVER >= _WIN32_WINNT_WINBLUE)

        if not defined(__IMFTopoLoader_INTERFACE_DEFINED__):
            # interface IMFTopoLoader
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTopoLoader = MIDL_INTERFACE(
                    "{DE9A6157-F660-4643-B56A-DF9F7998C7CD}"
                )
                IMFTopoLoader._iid_ = IID_IMFTopoLoader


                IMFTopoLoader._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Load')],
                        HRESULT,
                        'Load',
                        (['in'], POINTER(IMFTopology), 'pInputTopo'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopology)),
                           'ppOutputTopo'
                        ),
                        (['in'], POINTER(IMFTopology), 'pCurrentTopo'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTopoLoader_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0030
        # [local]
        mf = ctypes.windll.MF


        # STDAPI MFCreateTopoLoader(
        # _Outptr_ IMFTopoLoader ** ppObj );
        MFCreateTopoLoader = mf.MFCreateTopoLoader
        MFCreateTopoLoader.restype = STDAPI


        if not defined(__IMFContentProtectionManager_INTERFACE_DEFINED__):
            # interface IMFContentProtectionManager
            # [unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFContentProtectionManager = MIDL_INTERFACE(
                    "{ACF92459-6A61-42BD-B57C-B43E51203CB0}"
                )
                IMFContentProtectionManager._iid_ = IID_IMFContentProtectionManager


                IMFContentProtectionManager._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginEnableContent'), 'local'],
                        HRESULT,
                        'BeginEnableContent',
                        (['in'], POINTER(IMFActivate), 'pEnablerActivate'),
                        (['in'], POINTER(IMFTopology), 'pTopo'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndEnableContent'), 'local'],
                        HRESULT,
                        'EndEnableContent',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [in]            # [size_is][in]            # [in]            # [in]            # [call_as]            # [in]        # END IF  __IMFContentProtectionManager_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0031
        # [local]
        class __MIDL___MIDL_itf_mfidl_0000_0031_0001(ENUM):
            MF_LICENSE_URL_UNTRUSTED = 0
            MF_LICENSE_URL_TRUSTED = MF_LICENSE_URL_UNTRUSTED + 1 )
            MF_LICENSE_URL_TAMPERED = MF_LICENSE_URL_TRUSTED + 1 )
        MF_URL_TRUST_STATUS = __MIDL___MIDL_itf_mfidl_0000_0031_0001
        if not defined(__IMFContentEnabler_INTERFACE_DEFINED__):
            # interface IMFContentEnabler
            # [unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFContentEnabler = MIDL_INTERFACE(
                    "{D3C4EF59-49CE-4381-9071-D5BCD044C770}"
                )
                IMFContentEnabler._iid_ = IID_IMFContentEnabler


                IMFContentEnabler._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetEnableType')],
                        HRESULT,
                        'GetEnableType',
                        (['out'], POINTER(GUID), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetEnableURL')],
                        HRESULT,
                        'GetEnableURL',
                        (['out'], POINTER(LPWSTR), 'ppwszURL'),
                        (['out'], POINTER(DWORD), 'pcchURL'),
                        (
                            ['unique', 'in', 'out'],
                            POINTER(MF_URL_TRUST_STATUS),
                           'pTrustStatus'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetEnableData')],
                        HRESULT,
                        'GetEnableData',
                        (['out'], POINTER(POINTER(BYTE)), 'ppbData'),
                        (['out'], POINTER(DWORD), 'pcbData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsAutomaticSupported')],
                        HRESULT,
                        'IsAutomaticSupported',
                        (['out'], POINTER(BOOL), 'pfAutomatic'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AutomaticEnable')],
                        HRESULT,
                        'AutomaticEnable',
                    ),
                    COMMETHOD(
                        [helpstring('Method MonitorEnable')],
                        HRESULT,
                        'MonitorEnable',
                    ),
                    COMMETHOD(
                        [helpstring('Method Cancel')],
                        HRESULT,
                        'Cancel',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFContentEnabler_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0032
        # [local]
        MFENABLETYPE_WMDRMV1_LicenseAcquisition = EXTERN_GUID(
            0x4FF6EEAF,
            0xB43,
            0x4797,
            0x9B,
            0x85,
            0xAB,
            0xF3,
            0x18,
            0x15,
            0xE7,
            0xB0
        )
        MFENABLETYPE_WMDRMV7_LicenseAcquisition = EXTERN_GUID(
            0x3306DF,
            0x4A06,
            0x4884,
            0xA0,
            0x97,
            0xEF,
            0x6D,
            0x22,
            0xEC,
            0x84,
            0xA3
        )
        MFENABLETYPE_WMDRMV7_Individualization = EXTERN_GUID(
            0xACD2C84A,
            0xB303,
            0x4F65,
            0xBC,
            0x2C,
            0x2C,
            0x84,
            0x8D,
            0x1,
            0xA9,
            0x89
        )
        MFENABLETYPE_MF_UpdateRevocationInformation = EXTERN_GUID(
            0xE558B0B5,
            0xB3C4,
            0x44A0,
            0x92,
            0x4C,
            0x50,
            0xD1,
            0x78,
            0x93,
            0x23,
            0x85
        )
        MFENABLETYPE_MF_UpdateUntrustedComponent = EXTERN_GUID(
            0x9879F3D6,
            0xCEE2,
            0x48E6,
            0xB5,
            0x73,
            0x97,
            0x67,
            0xAB,
            0x17,
            0x2F,
            0x16
        )
        MFENABLETYPE_MF_RebootRequired = EXTERN_GUID(
            0x6D4D3D4B,
            0x0ECE,
            0x4652,
            0x8B,
            0x3A,
            0xF2,
            0xD2,
            0x42,
            0x60,
            0xD8,
            0x87
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # Structs that contain information about revoked or UINT binaries,
        # returned by the IMFContentEnabler::GetEnableData() method of
        # the Revocation content enabler
        if not defined(MFRR_INFO_VERSION):
            pass
        # END IF


        # The values for MFRR_COMPONENT_HASH_INFO.ulReason    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # STR_HASH_LEN: Number of characters required to represent a SHA-1 hash
        # (RTL_MAX_HASH_LEN_V1) as a string of the form "0x5a3b53463b672a4f..."
        # Each byte of a SHA-1 hash takes two characters to represent, and
        # we add in two leading characters "0x" as well as the NULL terminator
        _MFRR_COMPONENT_HASH_INFO._fields_ = [
            # Reason for failure (revoked or UINT or badly signed).
            ('ulReason', DWORD),
            # Header hash of the component
            ('rgHeaderHash', WCHAR * STR_HASH_LEN),
            # in the signing certificate chain is revoked
            ('rgPublicKeyHash', WCHAR * STR_HASH_LEN),
            # Component name (full path name)
            ('wszName', WCHAR * MAX_PATH),
        ]

        _MFRR_COMPONENTS._fields_ = [
            # Version number
            ('dwRRInfoVersion', DWORD),
            # Number of components in list
            ('dwRRComponents', DWORD),
            # allocated memory for the array of component info structures
            ('pRRComponents', PMFRR_COMPONENT_HASH_INFO),
        ]

        _ASFFlatPicture._fields_ = [
            # Direct mapped fields
            ('bPictureType', BYTE),
            ('dwDataLen', DWORD),
        ]

        _ASFFlatSynchronisedLyrics._fields_ = [
            # Direct mapped fields
            ('bTimeStampFormat', BYTE),
            ('bContentType', BYTE),
            ('dwLyricsLen', DWORD),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFMetadata_INTERFACE_DEFINED__):
            # interface IMFMetadata
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMetadata = MIDL_INTERFACE(
                    "{F88CFB8C-EF16-4991-B450-CB8C69E51704}"
                )
                IMFMetadata._iid_ = IID_IMFMetadata


                IMFMetadata._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetLanguage')],
                        HRESULT,
                        'SetLanguage',
                        (['in'], LPCWSTR, 'pwszRFC1766'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLanguage')],
                        HRESULT,
                        'GetLanguage',
                        (['out'], POINTER(LPWSTR), 'ppwszRFC1766'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllLanguages')],
                        HRESULT,
                        'GetAllLanguages',
                        (['out'], POINTER(PROPVARIANT), 'ppvLanguages'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetProperty')],
                        HRESULT,
                        'SetProperty',
                        (['in'], LPCWSTR, 'pwszName'),
                        (['in'], POINTER(PROPVARIANT), 'ppvValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProperty')],
                        HRESULT,
                        'GetProperty',
                        (['in'], LPCWSTR, 'pwszName'),
                        (['out'], POINTER(PROPVARIANT), 'ppvValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteProperty')],
                        HRESULT,
                        'DeleteProperty',
                        (['in'], LPCWSTR, 'pwszName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllPropertyNames')],
                        HRESULT,
                        'GetAllPropertyNames',
                        (['out'], POINTER(PROPVARIANT), 'ppvNames'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMetadata_INTERFACE_DEFINED__

        if not defined(__IMFMetadataProvider_INTERFACE_DEFINED__):
            # interface IMFMetadataProvider
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMetadataProvider = MIDL_INTERFACE(
                    "{56181D2D-E221-4ADB-B1C8-3CEE6A53F76F}"
                )
                IMFMetadataProvider._iid_ = IID_IMFMetadataProvider


                IMFMetadataProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetMFMetadata')],
                        HRESULT,
                        'GetMFMetadata',
                        (
                            ['in'],
                            POINTER(IMFPresentationDescriptor),
                           'pPresentationDescriptor'
                        ),
                        (['in'], DWORD, 'dwStreamIdentifier'),
                        (['in'], DWORD, 'dwFlags'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFMetadata)),
                           'ppMFMetadata'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMetadataProvider_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0034
        # [local]
        MF_METADATA_PROVIDER_SERVICE = EXTERN_GUID(
            0xDB214084,
            0x58A4,
            0x4D2E,
            0xB8,
            0x4F,
            0x6F,
            0x75,
            0x5B,
            0x2F,
            0x7A,
            0xD
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if WINVER >= _WIN32_WINNT_WIN7:
            MF_PROPERTY_HANDLER_SERVICE = EXTERN_GUID(
                0xA3FACE02,
                0x32B8,
                0x41DD,
                0x90,
                0xE7,
                0x5F,
                0xEF,
                0x7C,
                0x89,
                0x91,
                0xB5
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MFRATE_DIRECTION(ENUM):
            MFRATE_FORWARD = 0
            MFRATE_REVERSE = MFRATE_FORWARD + 1 )
        MFRATE_DIRECTION = _MFRATE_DIRECTION
        if not defined(__IMFRateSupport_INTERFACE_DEFINED__):
            # interface IMFRateSupport
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFRateSupport = MIDL_INTERFACE(
                    "{0A9CCDBC-D797-4563-9667-94EC5D79292D}"
                )
                IMFRateSupport._iid_ = IID_IMFRateSupport


                IMFRateSupport._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSlowestRate')],
                        HRESULT,
                        'GetSlowestRate',
                        (['in'], MFRATE_DIRECTION, 'eDirection'),
                        (['in'], BOOL, 'fThin'),
                        (['out'], POINTER(FLOAT), 'pflRate'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFastestRate')],
                        HRESULT,
                        'GetFastestRate',
                        (['in'], MFRATE_DIRECTION, 'eDirection'),
                        (['in'], BOOL, 'fThin'),
                        (['out'], POINTER(FLOAT), 'pflRate'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsRateSupported')],
                        HRESULT,
                        'IsRateSupported',
                        (['in'], BOOL, 'fThin'),
                        (['in'], FLOAT, 'flRate'),
                        (
                            ['out', 'unique', 'in'],
                            POINTER(FLOAT),
                           'pflNearestSupportedRate'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFRateSupport_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0035
        # [local]
        MF_RATE_CONTROL_SERVICE = EXTERN_GUID(
            0x866FA297,
            0xB802,
            0x4BF8,
            0x9D,
            0xC9,
            0x5E,
            0x3B,
            0x6A,
            0x9F,
            0x53,
            0xC9
        )
        if not defined(__IMFRateControl_INTERFACE_DEFINED__):
            # interface IMFRateControl
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFRateControl = MIDL_INTERFACE(
                    "{88DDCD21-03C3-4275-91ED-55EE3929328F}"
                )
                IMFRateControl._iid_ = IID_IMFRateControl


                IMFRateControl._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetRate')],
                        HRESULT,
                        'SetRate',
                        (['in'], BOOL, 'fThin'),
                        (['in'], FLOAT, 'flRate'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRate')],
                        HRESULT,
                        'GetRate',
                        (['out', 'in', 'unique'], POINTER(BOOL), 'pfThin'),
                        (['out', 'unique', 'in'], POINTER(FLOAT), 'pflRate'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFRateControl_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0036
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if WINVER >= _WIN32_WINNT_WIN7:
            if not defined(__IMFTimecodeTranslate_INTERFACE_DEFINED__):
                # interface IMFTimecodeTranslate
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFTimecodeTranslate = MIDL_INTERFACE(
                        "{AB9D8661-F7E8-4EF4-9861-89F334F94E74}"
                    )
                    IMFTimecodeTranslate._iid_ = IID_IMFTimecodeTranslate


                    IMFTimecodeTranslate._methods_ = [
                        COMMETHOD(
                            [helpstring('Method BeginConvertTimecodeToHNS')],
                            HRESULT,
                            'BeginConvertTimecodeToHNS',
                            (
                                ['in'],
                                POINTER(PROPVARIANT),
                               'pPropVarTimecode'
                            ),
                            (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                            (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method EndConvertTimecodeToHNS')],
                            HRESULT,
                            'EndConvertTimecodeToHNS',
                            (['in'], POINTER(IMFAsyncResult), 'pResult'),
                            (['out'], POINTER(MFTIME), 'phnsTime'),
                        ),
                        COMMETHOD(
                            [helpstring('Method BeginConvertHNSToTimecode')],
                            HRESULT,
                            'BeginConvertHNSToTimecode',
                            (['in'], MFTIME, 'hnsTime'),
                            (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                            (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method EndConvertHNSToTimecode')],
                            HRESULT,
                            'EndConvertHNSToTimecode',
                            (['in'], POINTER(IMFAsyncResult), 'pResult'),
                            (
                                ['out'],
                                POINTER(PROPVARIANT),
                               'pPropVarTimecode'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFTimecodeTranslate_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0037
            # [local]
            MF_TIMECODE_SERVICE = EXTERN_GUID(
                0xA0D502A7,
                0x0EB3,
                0x4885,
                0xB1,
                0xB9,
                0x9F,
                0xEB,
                0x0D,
                0x08,
                0x34,
                0x54
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if WINVER >= _WIN32_WINNT_WIN8:
            if not defined(__IMFSeekInfo_INTERFACE_DEFINED__):
                # interface IMFSeekInfo
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSeekInfo = MIDL_INTERFACE(
                        "{26AFEA53-D9ED-42B5-AB80-E64F9EE34779}"
                    )
                    IMFSeekInfo._iid_ = IID_IMFSeekInfo


                    IMFSeekInfo._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetNearestKeyFrames')],
                            HRESULT,
                            'GetNearestKeyFrames',
                            (['in'], POINTER(GUID), 'pguidTimeFormat'),
                            (
                                ['in'],
                                POINTER(PROPVARIANT),
                               'pvarStartPosition'
                            ),
                            (
                                ['out'],
                                POINTER(PROPVARIANT),
                               'pvarPreviousKeyFrame'
                            ),
                            (
                                ['out'],
                                POINTER(PROPVARIANT),
                               'pvarNextKeyFrame'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSeekInfo_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0038
            # [local]        # END IF   (WINVER >= _WIN32_WINNT_WIN8)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINVER >= _WIN32_WINNT_WIN8:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFSimpleAudioVolume_INTERFACE_DEFINED__):
            # interface IMFSimpleAudioVolume
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSimpleAudioVolume = MIDL_INTERFACE(
                    "{089EDF13-CF71-4338-8D13-9E569DBDC319}"
                )
                IMFSimpleAudioVolume._iid_ = IID_IMFSimpleAudioVolume


                IMFSimpleAudioVolume._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetMasterVolume')],
                        HRESULT,
                        'SetMasterVolume',
                        (['in'], FLOAT, 'fLevel'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMasterVolume')],
                        HRESULT,
                        'GetMasterVolume',
                        (['out'], POINTER(FLOAT), 'pfLevel'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetMute')],
                        HRESULT,
                        'SetMute',
                        (['in'], BOOL, 'bMute'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMute')],
                        HRESULT,
                        'GetMute',
                        (['out'], POINTER(BOOL), 'pbMute'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSimpleAudioVolume_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0039
        # [local]
        MR_POLICY_VOLUME_SERVICE = EXTERN_GUID(
            0x1ABAA2AC,
            0x9D3B,
            0x47C6,
            0xAB,
            0x48,
            0xC5,
            0x95,
            0x6,
            0xDE,
            0x78,
            0x4D
        )
        if WINVER >= _WIN32_WINNT_WIN8:
            MR_CAPTURE_POLICY_VOLUME_SERVICE = EXTERN_GUID(
                0x24030ACD,
                0x107A,
                0x4265,
                0x97,
                0x5C,
                0x41,
                0x4E,
                0x33,
                0xE6,
                0x5F,
                0x2A
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        if not defined(__IMFAudioStreamVolume_INTERFACE_DEFINED__):
            # interface IMFAudioStreamVolume
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFAudioStreamVolume = MIDL_INTERFACE(
                    "{76B1BBDB-4EC8-4F36-B106-70A9316DF593}"
                )
                IMFAudioStreamVolume._iid_ = IID_IMFAudioStreamVolume


                IMFAudioStreamVolume._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetChannelCount')],
                        HRESULT,
                        'GetChannelCount',
                        (['out'], POINTER(UINT32), 'pdwCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetChannelVolume')],
                        HRESULT,
                        'SetChannelVolume',
                        (['in'], UINT32, 'dwIndex'),
                        (['in'], FLOAT, 'fLevel'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetChannelVolume')],
                        HRESULT,
                        'GetChannelVolume',
                        (['in'], UINT32, 'dwIndex'),
                        (['out'], POINTER(FLOAT), 'pfLevel'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetAllVolumes')],
                        HRESULT,
                        'SetAllVolumes',
                        (['in'], UINT32, 'dwCount'),
                        (['in'], POINTER(FLOAT), 'pfVolumes'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllVolumes')],
                        HRESULT,
                        'GetAllVolumes',
                        (['in'], UINT32, 'dwCount'),
                        (['out'], POINTER(FLOAT), 'pfVolumes'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFAudioStreamVolume_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0040
        # [local]
        MR_STREAM_VOLUME_SERVICE = EXTERN_GUID(
            0xF8B5FA2F,
            0x32EF,
            0x46F5,
            0xB1,
            0x72,
            0x13,
            0x21,
            0x21,
            0x2F,
            0xB2,
            0xC4
        )
        if not defined(__IMFAudioPolicy_INTERFACE_DEFINED__):
            # interface IMFAudioPolicy
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFAudioPolicy = MIDL_INTERFACE(
                    "{A0638C2B-6465-4395-9AE7-A321A9FD2856}"
                )
                IMFAudioPolicy._iid_ = IID_IMFAudioPolicy


                IMFAudioPolicy._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetGroupingParam')],
                        HRESULT,
                        'SetGroupingParam',
                        (['in'], REFGUID, 'rguidClass'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetGroupingParam')],
                        HRESULT,
                        'GetGroupingParam',
                        (['out'], POINTER(GUID), 'pguidClass'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetDisplayName')],
                        HRESULT,
                        'SetDisplayName',
                        (['in'], LPCWSTR, 'pszName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDisplayName')],
                        HRESULT,
                        'GetDisplayName',
                        (['out'], POINTER(LPWSTR), 'pszName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetIconPath')],
                        HRESULT,
                        'SetIconPath',
                        (['in'], LPCWSTR, 'pszPath'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetIconPath')],
                        HRESULT,
                        'GetIconPath',
                        (['out'], POINTER(LPWSTR), 'pszPath'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFAudioPolicy_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0041
        # [local]
        MR_AUDIO_POLICY_SERVICE = EXTERN_GUID(
            0x911FD737,
            0x6775,
            0x4AB0,
            0xA6,
            0x14,
            0x29,
            0x78,
            0x62,
            0xFD,
            0xAC,
            0x88
        )
        if not defined(__IMFSampleGrabberSinkCallback_INTERFACE_DEFINED__):
            # interface IMFSampleGrabberSinkCallback
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSampleGrabberSinkCallback = MIDL_INTERFACE(
                    "{8C7B80BF-EE42-4B59-B1DF-55668E1BDCA8}"
                )
                IMFSampleGrabberSinkCallback._iid_ = IID_IMFSampleGrabberSinkCallback


                IMFSampleGrabberSinkCallback._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnSetPresentationClock')],
                        HRESULT,
                        'OnSetPresentationClock',
                        (
                            ['in'],
                            POINTER(IMFPresentationClock),
                           'pPresentationClock'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnProcessSample')],
                        HRESULT,
                        'OnProcessSample',
                        (['in'], REFGUID, 'guidMajorMediaType'),
                        (['in'], DWORD, 'dwSampleFlags'),
                        (['in'], LONGLONG, 'llSampleTime'),
                        (['in'], LONGLONG, 'llSampleDuration'),
                        (['in'], POINTER(BYTE), 'pSampleBuffer'),
                        (['in'], DWORD, 'dwSampleSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnShutdown')],
                        HRESULT,
                        'OnShutdown',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSampleGrabberSinkCallback_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0042
        # [local]
        mf = ctypes.windll.MF


        # STDAPI
        # MFCreateSampleGrabberSinkActivate(
        # IMFMediaType *pIMFMediaType,
        # IMFSampleGrabberSinkCallback* pIMFSampleGrabberSinkCallback,
        # _Outptr_ IMFActivate** ppIActivate
        # );
        MFCreateSampleGrabberSinkActivate = (
            mf.MFCreateSampleGrabberSinkActivate
        )
        MFCreateSampleGrabberSinkActivate.restype = STDAPI


        MF_SAMPLEGRABBERSINK_SAMPLE_TIME_OFFSET = EXTERN_GUID(
            0x62E3D776,
            0x8100,
            0x4E03,
            0xA6,
            0xE8,
            0xBD,
            0x38,
            0x57,
            0xAC,
            0x9C,
            0x47
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            MF_SAMPLEGRABBERSINK_IGNORE_CLOCK = EXTERN_GUID(
                0x0EFDA2C0,
                0x2B69,
                0x4E2E,
                0xAB,
                0x8D,
                0x46,
                0xDC,
                0xBF,
                0xF7,
                0xD2,
                0x5D
            )
            if not defined(__IMFSampleGrabberSinkCallback2_INTERFACE_DEFINED__):
                # interface IMFSampleGrabberSinkCallback2
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSampleGrabberSinkCallback2 = MIDL_INTERFACE(
                        "{CA86AA50-C46E-429E-AB27-16D6AC6844CB}"
                    )
                    IMFSampleGrabberSinkCallback2._iid_ = IID_IMFSampleGrabberSinkCallback2


                    IMFSampleGrabberSinkCallback2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnProcessSampleEx')],
                            HRESULT,
                            'OnProcessSampleEx',
                            (['in'], REFGUID, 'guidMajorMediaType'),
                            (['in'], DWORD, 'dwSampleFlags'),
                            (['in'], LONGLONG, 'llSampleTime'),
                            (['in'], LONGLONG, 'llSampleDuration'),
                            (['in'], POINTER(BYTE), 'pSampleBuffer'),
                            (['in'], DWORD, 'dwSampleSize'),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSampleGrabberSinkCallback2_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0043
            # [local]        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        MF_QUALITY_SERVICES = EXTERN_GUID(
            0xB7E2BE11,
            0x2F96,
            0x4640,
            0xB5,
            0x2C,
            0x28,
            0x23,
            0x65,
            0xBD,
            0xF1,
            0x6C
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFWorkQueueServices_INTERFACE_DEFINED__):
            # interface IMFWorkQueueServices
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFWorkQueueServices = MIDL_INTERFACE(
                    "{35FE1BB8-A3A9-40FE-BBEC-EB569C9CCCA3}"
                )
                IMFWorkQueueServices._iid_ = IID_IMFWorkQueueServices


                IMFWorkQueueServices._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginRegisterTopologyWorkQueuesWithMMCSS'), 'local'],
                        HRESULT,
                        'BeginRegisterTopologyWorkQueuesWithMMCSS',
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'pState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndRegisterTopologyWorkQueuesWithMMCSS'), 'local'],
                        HRESULT,
                        'EndRegisterTopologyWorkQueuesWithMMCSS',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginUnregisterTopologyWorkQueuesWithMMCSS'), 'local'],
                        HRESULT,
                        'BeginUnregisterTopologyWorkQueuesWithMMCSS',
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'pState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndUnregisterTopologyWorkQueuesWithMMCSS'), 'local'],
                        HRESULT,
                        'EndUnregisterTopologyWorkQueuesWithMMCSS',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTopologyWorkQueueMMCSSClass')],
                        HRESULT,
                        'GetTopologyWorkQueueMMCSSClass',
                        (['in'], DWORD, 'dwTopologyWorkQueueId'),
                        (['out'], LPWSTR, 'pwszClass'),
                        (['out', 'in'], POINTER(DWORD), 'pcchClass'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTopologyWorkQueueMMCSSTaskId')],
                        HRESULT,
                        'GetTopologyWorkQueueMMCSSTaskId',
                        (['in'], DWORD, 'dwTopologyWorkQueueId'),
                        (['out'], POINTER(DWORD), 'pdwTaskId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginRegisterPlatformWorkQueueWithMMCSS'), 'local'],
                        HRESULT,
                        'BeginRegisterPlatformWorkQueueWithMMCSS',
                        (['in'], DWORD, 'dwPlatformWorkQueue'),
                        (['in'], LPCWSTR, 'wszClass'),
                        (['in'], DWORD, 'dwTaskId'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'pState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndRegisterPlatformWorkQueueWithMMCSS'), 'local'],
                        HRESULT,
                        'EndRegisterPlatformWorkQueueWithMMCSS',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(DWORD), 'pdwTaskId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginUnregisterPlatformWorkQueueWithMMCSS'), 'local'],
                        HRESULT,
                        'BeginUnregisterPlatformWorkQueueWithMMCSS',
                        (['in'], DWORD, 'dwPlatformWorkQueue'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'pState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndUnregisterPlatformWorkQueueWithMMCSS'), 'local'],
                        HRESULT,
                        'EndUnregisterPlatformWorkQueueWithMMCSS',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPlaftormWorkQueueMMCSSClass')],
                        HRESULT,
                        'GetPlaftormWorkQueueMMCSSClass',
                        (['in'], DWORD, 'dwPlatformWorkQueueId'),
                        (['out'], LPWSTR, 'pwszClass'),
                        (['out', 'in'], POINTER(DWORD), 'pcchClass'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPlatformWorkQueueMMCSSTaskId')],
                        HRESULT,
                        'GetPlatformWorkQueueMMCSSTaskId',
                        (['in'], DWORD, 'dwPlatformWorkQueueId'),
                        (['out'], POINTER(DWORD), 'pdwTaskId'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [in]            # [call_as]            # [in]            # [call_as]            # [in]            # [call_as]            # [in]            # [call_as]            # [in]            # [in]            # [in]            # [in]            # [call_as]            # [in]            # [out]            # [call_as]            # [in]            # [in]            # [call_as]            # [in]        # END IF  __IMFWorkQueueServices_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0044
        # [local]
        MF_WORKQUEUE_SERVICES = EXTERN_GUID(
            0x8E37D489,
            0x41E0,
            0x413A,
            0x90,
            0x68,
            0x28,
            0x7C,
            0x88,
            0x6D,
            0x8D,
            0xDA
        )
        if not defined(__IMFWorkQueueServicesEx_INTERFACE_DEFINED__):
            # interface IMFWorkQueueServicesEx
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFWorkQueueServicesEx = MIDL_INTERFACE(
                    "{96BF961B-40FE-42F1-BA9D-320238B49700}"
                )
                IMFWorkQueueServicesEx._iid_ = IID_IMFWorkQueueServicesEx


                IMFWorkQueueServicesEx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetTopologyWorkQueueMMCSSPriority')],
                        HRESULT,
                        'GetTopologyWorkQueueMMCSSPriority',
                        (['in'], DWORD, 'dwTopologyWorkQueueId'),
                        (['out'], POINTER(LONG), 'plPriority'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginRegisterPlatformWorkQueueWithMMCSSEx'), 'local'],
                        HRESULT,
                        'BeginRegisterPlatformWorkQueueWithMMCSSEx',
                        (['in'], DWORD, 'dwPlatformWorkQueue'),
                        (['in'], LPCWSTR, 'wszClass'),
                        (['in'], DWORD, 'dwTaskId'),
                        (['in'], LONG, 'lPriority'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'pState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPlatformWorkQueueMMCSSPriority')],
                        HRESULT,
                        'GetPlatformWorkQueueMMCSSPriority',
                        (['in'], DWORD, 'dwPlatformWorkQueueId'),
                        (['out'], POINTER(LONG), 'plPriority'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [in]            # [in]            # [in]            # [in]            # [in]        # END IF  __IMFWorkQueueServicesEx_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0045
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MF_QUALITY_DROP_MODE(ENUM):
            MF_DROP_MODE_NONE = 0
            MF_DROP_MODE_1 = 0x1
            MF_DROP_MODE_2 = 0x2
            MF_DROP_MODE_3 = 0x3
            MF_DROP_MODE_4 = 0x4
            MF_DROP_MODE_5 = 0x5
            MF_NUM_DROP_MODES = 0x6

        MF_QUALITY_DROP_MODE = _MF_QUALITY_DROP_MODE


        class _MF_QUALITY_LEVEL(ENUM):
            MF_QUALITY_NORMAL = 0
            MF_QUALITY_NORMAL_MINUS_1 = 0x1
            MF_QUALITY_NORMAL_MINUS_2 = 0x2
            MF_QUALITY_NORMAL_MINUS_3 = 0x3
            MF_QUALITY_NORMAL_MINUS_4 = 0x4
            MF_QUALITY_NORMAL_MINUS_5 = 0x5
            MF_NUM_QUALITY_LEVELS = 0x6

        MF_QUALITY_LEVEL = _MF_QUALITY_LEVEL
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            class _MF_QUALITY_ADVISE_FLAGS(ENUM):
                MF_QUALITY_CANNOT_KEEP_UP = 0x1

            MF_QUALITY_ADVISE_FLAGS = _MF_QUALITY_ADVISE_FLAGS
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFQualityManager_INTERFACE_DEFINED__):
            # interface IMFQualityManager
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFQualityManager = MIDL_INTERFACE(
                    "{8D009D86-5B9F-4115-B1FC-9F80D52AB8AB}"
                )
                IMFQualityManager._iid_ = IID_IMFQualityManager


                IMFQualityManager._methods_ = [
                    COMMETHOD(
                        [helpstring('Method NotifyTopology')],
                        HRESULT,
                        'NotifyTopology',
                        (['in'], POINTER(IMFTopology), 'pTopology'),
                    ),
                    COMMETHOD(
                        [helpstring('Method NotifyPresentationClock')],
                        HRESULT,
                        'NotifyPresentationClock',
                        (['in'], POINTER(IMFPresentationClock), 'pClock'),
                    ),
                    COMMETHOD(
                        [helpstring('Method NotifyProcessInput')],
                        HRESULT,
                        'NotifyProcessInput',
                        (['in'], POINTER(IMFTopologyNode), 'pNode'),
                        (['in'], LONG, 'lInputIndex'),
                        (['in'], POINTER(IMFSample), 'pSample'),
                    ),
                    COMMETHOD(
                        [helpstring('Method NotifyProcessOutput')],
                        HRESULT,
                        'NotifyProcessOutput',
                        (['in'], POINTER(IMFTopologyNode), 'pNode'),
                        (['in'], LONG, 'lOutputIndex'),
                        (['in'], POINTER(IMFSample), 'pSample'),
                    ),
                    COMMETHOD(
                        [helpstring('Method NotifyQualityEvent')],
                        HRESULT,
                        'NotifyQualityEvent',
                        (['in'], POINTER(comtypes.IUnknown), 'pObject'),
                        (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Shutdown')],
                        HRESULT,
                        'Shutdown',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFQualityManager_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0046
        # [local]
        mf = ctypes.windll.MF


        # STDAPI MFCreateStandardQualityManager(
        # _Outptr_ IMFQualityManager **ppQualityManager );
        MFCreateStandardQualityManager = mf.MFCreateStandardQualityManager
        MFCreateStandardQualityManager.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        MF_QUALITY_NOTIFY_PROCESSING_LATENCY = EXTERN_GUID(
            0xF6B44AF8,
            0x604D,
            0x46FE,
            0xA9,
            0x5D,
            0x45,
            0x47,
            0x9B,
            0x10,
            0xC9,
            0xBC
        )
        MF_QUALITY_NOTIFY_SAMPLE_LAG = EXTERN_GUID(
            0x30D15206,
            0xED2A,
            0x4760,
            0xBE,
            0x17,
            0xEB,
            0x4A,
            0x9F,
            0x12,
            0x29,
            0x5C
        )
        if not defined(__IMFQualityAdvise_INTERFACE_DEFINED__):
            # interface IMFQualityAdvise
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFQualityAdvise = MIDL_INTERFACE(
                    "{EC15E2E9-E36B-4F7C-8758-77D452EF4CE7}"
                )
                IMFQualityAdvise._iid_ = IID_IMFQualityAdvise


                IMFQualityAdvise._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetDropMode')],
                        HRESULT,
                        'SetDropMode',
                        (['in'], MF_QUALITY_DROP_MODE, 'eDropMode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetQualityLevel')],
                        HRESULT,
                        'SetQualityLevel',
                        (['in'], MF_QUALITY_LEVEL, 'eQualityLevel'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDropMode')],
                        HRESULT,
                        'GetDropMode',
                        (
                            ['out'],
                            POINTER(MF_QUALITY_DROP_MODE),
                           'peDropMode'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetQualityLevel')],
                        HRESULT,
                        'GetQualityLevel',
                        (
                            ['out'],
                            POINTER(MF_QUALITY_LEVEL),
                           'peQualityLevel'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method DropTime')],
                        HRESULT,
                        'DropTime',
                        (['in'], LONGLONG, 'hnsAmountToDrop'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFQualityAdvise_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0047
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFQualityAdvise2_INTERFACE_DEFINED__):
                # interface IMFQualityAdvise2
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFQualityAdvise2 = MIDL_INTERFACE(
                        "{F3706F0D-8EA2-4886-8000-7155E9EC2EAE}"
                    )
                    IMFQualityAdvise2._iid_ = IID_IMFQualityAdvise2


                    IMFQualityAdvise2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method NotifyQualityEvent')],
                            HRESULT,
                            'NotifyQualityEvent',
                            (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                            (['out'], POINTER(DWORD), 'pdwFlags'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFQualityAdvise2_INTERFACE_DEFINED__

            if not defined(__IMFQualityAdviseLimits_INTERFACE_DEFINED__):
                # interface IMFQualityAdviseLimits
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFQualityAdviseLimits = MIDL_INTERFACE(
                        "{DFCD8E4D-30B5-4567-ACAA-8EB5B7853DC9}"
                    )
                    IMFQualityAdviseLimits._iid_ = IID_IMFQualityAdviseLimits


                    IMFQualityAdviseLimits._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetMaximumDropMode')],
                            HRESULT,
                            'GetMaximumDropMode',
                            (
                                ['out'],
                                POINTER(MF_QUALITY_DROP_MODE),
                               'peDropMode'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMinimumQualityLevel')],
                            HRESULT,
                            'GetMinimumQualityLevel',
                            (
                                ['out'],
                                POINTER(MF_QUALITY_LEVEL),
                               'peQualityLevel'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFQualityAdviseLimits_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0049
            # [local]        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFRealTimeClient_INTERFACE_DEFINED__):
            # interface IMFRealTimeClient
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFRealTimeClient = MIDL_INTERFACE(
                    "{2347D60B-3FB5-480C-8803-8DF3ADCD3EF0}"
                )
                IMFRealTimeClient._iid_ = IID_IMFRealTimeClient


                IMFRealTimeClient._methods_ = [
                    COMMETHOD(
                        [helpstring('Method RegisterThreads')],
                        HRESULT,
                        'RegisterThreads',
                        (['in'], DWORD, 'dwTaskIndex'),
                        (['in'], LPCWSTR, 'wszClass'),
                    ),
                    COMMETHOD(
                        [helpstring('Method UnregisterThreads')],
                        HRESULT,
                        'UnregisterThreads',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetWorkQueue')],
                        HRESULT,
                        'SetWorkQueue',
                        (['in'], DWORD, 'dwWorkQueueId'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFRealTimeClient_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0050
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINVER >= _WIN32_WINNT_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFRealTimeClientEx_INTERFACE_DEFINED__):
                # interface IMFRealTimeClientEx
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFRealTimeClientEx = MIDL_INTERFACE(
                        "{03910848-AB16-4611-B100-17B88AE2F248}"
                    )
                    IMFRealTimeClientEx._iid_ = IID_IMFRealTimeClientEx


                    IMFRealTimeClientEx._methods_ = [
                        COMMETHOD(
                            [helpstring('Method RegisterThreadsEx')],
                            HRESULT,
                            'RegisterThreadsEx',
                            (['out', 'in'], POINTER(DWORD), 'pdwTaskIndex'),
                            (['in'], LPCWSTR, 'wszClassName'),
                            (['in'], LONG, 'lBasePriority'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UnregisterThreads')],
                            HRESULT,
                            'UnregisterThreads',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetWorkQueueEx')],
                            HRESULT,
                            'SetWorkQueueEx',
                            (['in'], DWORD, 'dwMultithreadedWorkQueueId'),
                            (['in'], LONG, 'lWorkItemBasePriority'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFRealTimeClientEx_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0051
            # [local]        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        MFSequencerElementId = DWORD


        class _MFSequencerTopologyFlags(ENUM):
            SequencerTopologyFlags_Last = 0x1

        MFSequencerTopologyFlags = _MFSequencerTopologyFlags
        if not defined(__IMFSequencerSource_INTERFACE_DEFINED__):
            # interface IMFSequencerSource
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSequencerSource = MIDL_INTERFACE(
                    "{197CD219-19CB-4DE1-A64C-ACF2EDCBE59E}"
                )
                IMFSequencerSource._iid_ = IID_IMFSequencerSource


                IMFSequencerSource._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AppendTopology')],
                        HRESULT,
                        'AppendTopology',
                        (['in'], POINTER(IMFTopology), 'pTopology'),
                        (['in'], DWORD, 'dwFlags'),
                        (['out'], POINTER(MFSequencerElementId), 'pdwId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteTopology')],
                        HRESULT,
                        'DeleteTopology',
                        (['in'], MFSequencerElementId, 'dwId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPresentationContext')],
                        HRESULT,
                        'GetPresentationContext',
                        (['in'], POINTER(IMFPresentationDescriptor), 'pPD'),
                        (['out'], POINTER(MFSequencerElementId), 'pId'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopology)),
                           'ppTopology'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method UpdateTopology')],
                        HRESULT,
                        'UpdateTopology',
                        (['in'], MFSequencerElementId, 'dwId'),
                        (['in'], POINTER(IMFTopology), 'pTopology'),
                    ),
                    COMMETHOD(
                        [helpstring('Method UpdateTopologyFlags')],
                        HRESULT,
                        'UpdateTopologyFlags',
                        (['in'], MFSequencerElementId, 'dwId'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSequencerSource_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0052
        # [local]
        MF_TIME_FORMAT_SEGMENT_OFFSET = EXTERN_GUID(
            0xC8B8BE77,
            0x869C,
            0x431D,
            0x81,
            0x2E,
            0x16,
            0x96,
            0x93,
            0xF6,
            0x5A,
            0x39
        )
        mf = ctypes.windll.MF


        # STDAPI MFCreateSequencerSource(
        # IUnknown *pReserved,
        # _Outptr_ IMFSequencerSource **ppSequencerSource
        # );
        MFCreateSequencerSource = mf.MFCreateSequencerSource
        MFCreateSequencerSource.restype = STDAPI


        # STDAPI MFCreateSequencerSegmentOffset(
        # MFSequencerElementId dwId,
        # MFTIME hnsOffset,
        # _Out_ PROPVARIANT *pvarSegmentOffset
        # );
        MFCreateSequencerSegmentOffset = mf.MFCreateSequencerSegmentOffset
        MFCreateSequencerSegmentOffset.restype = STDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if WINVER >= _WIN32_WINNT_WIN7:
            mf = ctypes.windll.MF


            # STDAPI MFCreateAggregateSource(
            # _In_ IMFCollection *pSourceCollection,
            # _Outptr_ IMFMediaSource **ppAggSource
            # );
            MFCreateAggregateSource = mf.MFCreateAggregateSource
            MFCreateAggregateSource.restype = STDAPI


        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFMediaSourceTopologyProvider_INTERFACE_DEFINED__):
            # interface IMFMediaSourceTopologyProvider
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaSourceTopologyProvider = MIDL_INTERFACE(
                    "{0E1D6009-C9F3-442D-8C51-A42D2D49452F}"
                )
                IMFMediaSourceTopologyProvider._iid_ = IID_IMFMediaSourceTopologyProvider


                IMFMediaSourceTopologyProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetMediaSourceTopology')],
                        HRESULT,
                        'GetMediaSourceTopology',
                        (
                            ['in'],
                            POINTER(IMFPresentationDescriptor),
                           'pPresentationDescriptor'
                        ),
                        (
                            ['out'],
                            POINTER(POINTER(IMFTopology)),
                           'ppTopology'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaSourceTopologyProvider_INTERFACE_DEFINED__

        if not defined(__IMFMediaSourcePresentationProvider_INTERFACE_DEFINED__):
            # interface IMFMediaSourcePresentationProvider
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaSourcePresentationProvider = MIDL_INTERFACE(
                    "{0E1D600A-C9F3-442D-8C51-A42D2D49452F}"
                )
                IMFMediaSourcePresentationProvider._iid_ = IID_IMFMediaSourcePresentationProvider


                IMFMediaSourcePresentationProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ForceEndOfPresentation')],
                        HRESULT,
                        'ForceEndOfPresentation',
                        (
                            ['in'],
                            POINTER(IMFPresentationDescriptor),
                           'pPresentationDescriptor'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaSourcePresentationProvider_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0054
        # [local]
        MF_SOURCE_PRESENTATION_PROVIDER_SERVICE = EXTERN_GUID(
            0xE002AADC,
            0xF4AF,
            0x4EE5,
            0x98,
            0x47,
            0x05,
            0x3E,
            0xDF,
            0x84,
            0x04,
            0x26
        )
        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF


        class _Union_1(ctypes.Union):
            pass


        _Union_1._fields_ = [
            # [case()]
            ('u32', UINT32),
            # [case()]
            ('u64', UINT64),
            # [case()]
            ('d', DOUBLE),
        ]
        _MFTOPONODE_ATTRIBUTE_UPDATE._Union_1 = _Union_1

        _MFTOPONODE_ATTRIBUTE_UPDATE._anonymous_ = (
            '_Union_1',
        )

        _MFTOPONODE_ATTRIBUTE_UPDATE._fields_ = [
            ('NodeId', TOPOID),
            ('guidAttributeKey', GUID),
            ('attrType', MF_ATTRIBUTE_TYPE),
            # [switch_type][switch_is]
            ('_Union_1', _MFTOPONODE_ATTRIBUTE_UPDATE._Union_1),
        ]
        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF


        if not defined(__IMFTopologyNodeAttributeEditor_INTERFACE_DEFINED__):
            # interface IMFTopologyNodeAttributeEditor
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTopologyNodeAttributeEditor = MIDL_INTERFACE(
                    "{676AA6DD-238A-410D-BB99-65668D01605A}"
                )
                IMFTopologyNodeAttributeEditor._iid_ = IID_IMFTopologyNodeAttributeEditor


                IMFTopologyNodeAttributeEditor._methods_ = [
                    COMMETHOD(
                        [helpstring('Method UpdateNodeAttributes')],
                        HRESULT,
                        'UpdateNodeAttributes',
                        (['in'], TOPOID, 'TopoId'),
                        (['in'], DWORD, 'cUpdates'),
                        (
                            ['in'],
                            POINTER(MFTOPONODE_ATTRIBUTE_UPDATE),
                           'pUpdates'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTopologyNodeAttributeEditor_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0055
        # [local]
        MF_TOPONODE_ATTRIBUTE_EDITOR_SERVICE = EXTERN_GUID(
            0x65656E1A,
            0x077F,
            0x4472,
            0x83,
            0xEF,
            0x31,
            0x6F,
            0x11,
            0xD5,
            0x08,
            0x7A
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        _MF_LEAKY_BUCKET_PAIR._fields_ = [
            ('dwBitrate', DWORD),
            ('msBufferWindow', DWORD),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        _MFBYTESTREAM_BUFFERING_PARAMS._fields_ = [
            ('cbTotalFileSize', QWORD),
            ('cbPlayableDataSize', QWORD),
            ('prgBuckets', POINTER(MF_LEAKY_BUCKET_PAIR)),
            ('cBuckets', DWORD),
            ('qwNetBufferingTime', QWORD),
            ('qwExtraBufferingTimeDuringSeek', QWORD),
            ('qwPlayDuration', QWORD),
            ('dRate', FLOAT),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if defined(_MSC_VER) and (_MSC_VER >= 1600):
            pass
        # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFByteStreamBuffering_INTERFACE_DEFINED__):
            # interface IMFByteStreamBuffering
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFByteStreamBuffering = MIDL_INTERFACE(
                    "{6D66D782-1D4F-4DB7-8C63-CB8C77F1EF5E}"
                )
                IMFByteStreamBuffering._iid_ = IID_IMFByteStreamBuffering


                IMFByteStreamBuffering._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetBufferingParams')],
                        HRESULT,
                        'SetBufferingParams',
                        (
                            ['in'],
                            POINTER(MFBYTESTREAM_BUFFERING_PARAMS),
                           'pParams'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnableBuffering')],
                        HRESULT,
                        'EnableBuffering',
                        (['in'], BOOL, 'fEnable'),
                    ),
                    COMMETHOD(
                        [helpstring('Method StopBuffering')],
                        HRESULT,
                        'StopBuffering',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFByteStreamBuffering_INTERFACE_DEFINED__

        if not defined(__IMFByteStreamCacheControl_INTERFACE_DEFINED__):
            # interface IMFByteStreamCacheControl
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFByteStreamCacheControl = MIDL_INTERFACE(
                    "{F5042EA4-7A96-4A75-AA7B-2BE1EF7F88D5}"
                )
                IMFByteStreamCacheControl._iid_ = IID_IMFByteStreamCacheControl


                IMFByteStreamCacheControl._methods_ = [
                    COMMETHOD(
                        [helpstring('Method StopBackgroundTransfer')],
                        HRESULT,
                        'StopBackgroundTransfer',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFByteStreamCacheControl_INTERFACE_DEFINED__

        if not defined(__IMFByteStreamTimeSeek_INTERFACE_DEFINED__):
            # interface IMFByteStreamTimeSeek
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFByteStreamTimeSeek = MIDL_INTERFACE(
                    "{64976BFA-FB61-4041-9069-8C9A5F659BEB}"
                )
                IMFByteStreamTimeSeek._iid_ = IID_IMFByteStreamTimeSeek


                IMFByteStreamTimeSeek._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsTimeSeekSupported')],
                        HRESULT,
                        'IsTimeSeekSupported',
                        (['out'], POINTER(BOOL), 'pfTimeSeekIsSupported'),
                    ),
                    COMMETHOD(
                        [helpstring('Method TimeSeek')],
                        HRESULT,
                        'TimeSeek',
                        (['in'], QWORD, 'qwTimePosition'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTimeSeekResult')],
                        HRESULT,
                        'GetTimeSeekResult',
                        (['out'], POINTER(QWORD), 'pqwStartTime'),
                        (['out'], POINTER(QWORD), 'pqwStopTime'),
                        (['out'], POINTER(QWORD), 'pqwDuration'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFByteStreamTimeSeek_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0058
        # [local]
        if WINVER >= _WIN32_WINNT_WIN8:
            __MIDL___MIDL_itf_mfidl_0000_0058_0001._fields_ = [
                ('qwStartOffset', QWORD),
                ('qwEndOffset', QWORD),
            ]
            if not defined(__IMFByteStreamCacheControl2_INTERFACE_DEFINED__):
                # interface IMFByteStreamCacheControl2
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFByteStreamCacheControl2 = MIDL_INTERFACE(
                        "{71CE469C-F34B-49EA-A56B-2D2A10E51149}"
                    )
                    IMFByteStreamCacheControl2._iid_ = IID_IMFByteStreamCacheControl2


                    IMFByteStreamCacheControl2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetByteRanges')],
                            HRESULT,
                            'GetByteRanges',
                            (['out'], POINTER(DWORD), 'pcRanges'),
                            (
                                ['out'],
                                POINTER(POINTER(MF_BYTE_STREAM_CACHE_RANGE)),
                               'ppRanges'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCacheLimit')],
                            HRESULT,
                            'SetCacheLimit',
                            (['in'], QWORD, 'qwBytes'),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsBackgroundTransferActive')],
                            HRESULT,
                            'IsBackgroundTransferActive',
                            (['out'], POINTER(BOOL), 'pfActive'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFByteStreamCacheControl2_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0059
            # [local]        # END IF   (WINVER >= _WIN32_WINNT_WIN8)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFNetCredential_INTERFACE_DEFINED__):
            # interface IMFNetCredential
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFNetCredential = MIDL_INTERFACE(
                    "{5B87EF6A-7ED8-434F-BA0E-184FAC1628D1}"
                )
                IMFNetCredential._iid_ = IID_IMFNetCredential


                IMFNetCredential._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetUser')],
                        HRESULT,
                        'SetUser',
                        (['in'], POINTER(BYTE), 'pbData'),
                        (['in'], DWORD, 'cbData'),
                        (['in'], BOOL, 'fDataIsEncrypted'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetPassword')],
                        HRESULT,
                        'SetPassword',
                        (['in'], POINTER(BYTE), 'pbData'),
                        (['in'], DWORD, 'cbData'),
                        (['in'], BOOL, 'fDataIsEncrypted'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetUser')],
                        HRESULT,
                        'GetUser',
                        (['out'], POINTER(BYTE), 'pbData'),
                        (['out', 'in'], POINTER(DWORD), 'pcbData'),
                        (['in'], BOOL, 'fEncryptData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPassword')],
                        HRESULT,
                        'GetPassword',
                        (['out'], POINTER(BYTE), 'pbData'),
                        (['out', 'in'], POINTER(DWORD), 'pcbData'),
                        (['in'], BOOL, 'fEncryptData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method LoggedOnUser')],
                        HRESULT,
                        'LoggedOnUser',
                        (['out'], POINTER(BOOL), 'pfLoggedOnUser'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFNetCredential_INTERFACE_DEFINED__

        if not defined(__IMFNetCredentialManager_INTERFACE_DEFINED__):
            # interface IMFNetCredentialManager
            # [local][uuid][object]
            _MFNetCredentialManagerGetParam._fields_ = [
                ('hrOp', HRESULT),
                ('fAllowLoggedOnUser', BOOL),
                ('fClearTextPackage', BOOL),
                ('pszUrl', LPCWSTR),
                ('pszSite', LPCWSTR),
                ('pszRealm', LPCWSTR),
                ('pszPackage', LPCWSTR),
                ('nRetries', LONG),
            ]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFNetCredentialManager = MIDL_INTERFACE(
                    "{5B87EF6B-7ED8-434F-BA0E-184FAC1628D1}"
                )
                IMFNetCredentialManager._iid_ = IID_IMFNetCredentialManager


                IMFNetCredentialManager._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginGetCredentials')],
                        HRESULT,
                        'BeginGetCredentials',
                        (
                            ['in'],
                            POINTER(MFNetCredentialManagerGetParam),
                           'pParam'
                        ),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'pState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndGetCredentials')],
                        HRESULT,
                        'EndGetCredentials',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFNetCredential)),
                           'ppCred'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetGood')],
                        HRESULT,
                        'SetGood',
                        (['in'], POINTER(IMFNetCredential), 'pCred'),
                        (['in'], BOOL, 'fGood'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFNetCredentialManager_INTERFACE_DEFINED__

        if not defined(__IMFNetCredentialCache_INTERFACE_DEFINED__):
            # interface IMFNetCredentialCache
            # [local][uuid][object]
            class _MFNetCredentialRequirements(ENUM):
                REQUIRE_PROMPT = 0x1
                REQUIRE_SAVE_SELECTED = 0x2

            MFNetCredentialRequirements = _MFNetCredentialRequirements


            class _MFNetCredentialOptions(ENUM):
                MFNET_CREDENTIAL_SAVE = 0x1
                MFNET_CREDENTIAL_DONT_CACHE = 0x2
                MFNET_CREDENTIAL_ALLOW_CLEAR_TEXT = 0x4

            MFNetCredentialOptions = _MFNetCredentialOptions


            class _MFNetAuthenticationFlags(ENUM):
                MFNET_AUTHENTICATION_PROXY = 0x1
                MFNET_AUTHENTICATION_CLEAR_TEXT = 0x2
                MFNET_AUTHENTICATION_LOGGED_ON_USER = 0x4

            MFNetAuthenticationFlags = _MFNetAuthenticationFlags
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFNetCredentialCache = MIDL_INTERFACE(
                    "{5B87EF6C-7ED8-434F-BA0E-184FAC1628D1}"
                )
                IMFNetCredentialCache._iid_ = IID_IMFNetCredentialCache


                IMFNetCredentialCache._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCredential')],
                        HRESULT,
                        'GetCredential',
                        (['in'], LPCWSTR, 'pszUrl'),
                        (['in'], LPCWSTR, 'pszRealm'),
                        (['in'], DWORD, 'dwAuthenticationFlags'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFNetCredential)),
                           'ppCred'
                        ),
                        (['out'], POINTER(DWORD), 'pdwRequirementsFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetGood')],
                        HRESULT,
                        'SetGood',
                        (['in'], POINTER(IMFNetCredential), 'pCred'),
                        (['in'], BOOL, 'fGood'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetUserOptions')],
                        HRESULT,
                        'SetUserOptions',
                        (['in'], POINTER(IMFNetCredential), 'pCred'),
                        (['in'], DWORD, 'dwOptionsFlags'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFNetCredentialCache_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0062
        # [local]
        mf = ctypes.windll.MF


        # STDAPI
        # MFCreateCredentialCache(
        # _Outptr_ IMFNetCredentialCache ** ppCache);
        MFCreateCredentialCache = mf.MFCreateCredentialCache
        MFCreateCredentialCache.restype = STDAPI


    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            if not defined(__IMFSSLCertificateManager_INTERFACE_DEFINED__):
                # interface IMFSSLCertificateManager
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSSLCertificateManager = MIDL_INTERFACE(
                        "{61F7D887-1230-4A8B-AEBA-8AD434D1A64D}"
                    )
                    IMFSSLCertificateManager._iid_ = IID_IMFSSLCertificateManager


                    IMFSSLCertificateManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetClientCertificate')],
                            HRESULT,
                            'GetClientCertificate',
                            (['in'], LPCWSTR, 'pszURL'),
                            (['out'], POINTER(POINTER(BYTE)), 'ppbData'),
                            (['out'], POINTER(DWORD), 'pcbData'),
                        ),
                        COMMETHOD(
                            [helpstring('Method BeginGetClientCertificate')],
                            HRESULT,
                            'BeginGetClientCertificate',
                            (['in'], LPCWSTR, 'pszURL'),
                            (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                            (['in'], POINTER(comtypes.IUnknown), 'pState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method EndGetClientCertificate')],
                            HRESULT,
                            'EndGetClientCertificate',
                            (['in'], POINTER(IMFAsyncResult), 'pResult'),
                            (['out'], POINTER(POINTER(BYTE)), 'ppbData'),
                            (['out'], POINTER(DWORD), 'pcbData'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCertificatePolicy')],
                            HRESULT,
                            'GetCertificatePolicy',
                            (['in'], LPCWSTR, 'pszURL'),
                            (
                                ['out'],
                                POINTER(BOOL),
                               'pfOverrideAutomaticCheck'
                            ),
                            (
                                ['out'],
                                POINTER(BOOL),
                               'pfClientCertificateAvailable'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnServerCertificate')],
                            HRESULT,
                            'OnServerCertificate',
                            (['in'], LPCWSTR, 'pszURL'),
                            (['in'], POINTER(BYTE), 'pbData'),
                            (['in'], DWORD, 'cbData'),
                            (['out'], POINTER(BOOL), 'pfIsGood'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSSLCertificateManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0063
            # [local]
            MFNETSOURCE_SSLCERTIFICATE_MANAGER = EXTERN_GUID(
                0x55E6CB27,
                0xE69B,
                0x4267,
                0x94,
                0x0C,
                0x2D,
                0x7E,
                0xC5,
                0xBB,
                0x8A,
                0x0F
            )
            if not defined(__IMFNetResourceFilter_INTERFACE_DEFINED__):
                # interface IMFNetResourceFilter
                # [local][unique][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFNetResourceFilter = MIDL_INTERFACE(
                        "{091878A3-BF11-4A5C-BC9F-33995B06EF2D}"
                    )
                    IMFNetResourceFilter._iid_ = IID_IMFNetResourceFilter


                    IMFNetResourceFilter._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnRedirect')],
                            HRESULT,
                            'OnRedirect',
                            (['in'], LPCWSTR, 'pszUrl'),
                            (['out'], POINTER(VARIANT_BOOL), 'pvbCancel'),
                        ),
                        COMMETHOD(
                            [helpstring('Method OnSendingRequest')],
                            HRESULT,
                            'OnSendingRequest',
                            (['in'], LPCWSTR, 'pszUrl'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFNetResourceFilter_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0064
            # [local]
            MFNETSOURCE_RESOURCE_FILTER = EXTERN_GUID(
                0x815D0FF6,
                0x265A,
                0x4477,
                0x9E,
                0x46,
                0x7B,
                0x80,
                0xAD,
                0x80,
                0xB5,
                0xFB
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFSourceOpenMonitor_INTERFACE_DEFINED__):
            # interface IMFSourceOpenMonitor
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSourceOpenMonitor = MIDL_INTERFACE(
                    "{059054B3-027C-494C-A27D-9113291CF87F}"
                )
                IMFSourceOpenMonitor._iid_ = IID_IMFSourceOpenMonitor


                IMFSourceOpenMonitor._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnSourceEvent')],
                        HRESULT,
                        'OnSourceEvent',
                        (['in'], POINTER(IMFMediaEvent), 'pEvent'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSourceOpenMonitor_INTERFACE_DEFINED__

        if not defined(__IMFNetProxyLocator_INTERFACE_DEFINED__):
            # interface IMFNetProxyLocator
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFNetProxyLocator = MIDL_INTERFACE(
                    "{E9CD0383-A268-4BB4-82DE-658D53574D41}"
                )
                IMFNetProxyLocator._iid_ = IID_IMFNetProxyLocator


                IMFNetProxyLocator._methods_ = [
                    COMMETHOD(
                        [helpstring('Method FindFirstProxy')],
                        HRESULT,
                        'FindFirstProxy',
                        (['in'], LPCWSTR, 'pszHost'),
                        (['in'], LPCWSTR, 'pszUrl'),
                        (['in'], BOOL, 'fReserved'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FindNextProxy')],
                        HRESULT,
                        'FindNextProxy',
                    ),
                    COMMETHOD(
                        [helpstring('Method RegisterProxyResult')],
                        HRESULT,
                        'RegisterProxyResult',
                        (['in'], HRESULT, 'hrOp'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCurrentProxy')],
                        HRESULT,
                        'GetCurrentProxy',
                        (['out'], LPWSTR, 'pszStr'),
                        (['out', 'in'], POINTER(DWORD), 'pcchStr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Clone')],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IMFNetProxyLocator)),
                           'ppProxyLocator'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFNetProxyLocator_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0066
        # [local]
        mf = ctypes.windll.MF


        # STDAPI MFCreateProxyLocator(
        # LPCWSTR pszProtocol,
        # IPropertyStore* pProxyConfig,
        # _Outptr_ IMFNetProxyLocator** ppProxyLocator );
        MFCreateProxyLocator = mf.MFCreateProxyLocator
        MFCreateProxyLocator.restype = STDAPI


        if not defined(__IMFNetProxyLocatorFactory_INTERFACE_DEFINED__):
            # interface IMFNetProxyLocatorFactory
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFNetProxyLocatorFactory = MIDL_INTERFACE(
                    "{E9CD0384-A268-4BB4-82DE-658D53574D41}"
                )
                IMFNetProxyLocatorFactory._iid_ = IID_IMFNetProxyLocatorFactory


                IMFNetProxyLocatorFactory._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateProxyLocator')],
                        HRESULT,
                        'CreateProxyLocator',
                        (['in'], LPCWSTR, 'pszProtocol'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFNetProxyLocator)),
                           'ppProxyLocator'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFNetProxyLocatorFactory_INTERFACE_DEFINED__

        if not defined(__IMFSaveJob_INTERFACE_DEFINED__):
            # interface IMFSaveJob
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSaveJob = MIDL_INTERFACE(
                    "{E9931663-80BF-4C6E-98AF-5DCF58747D1F}"
                )
                IMFSaveJob._iid_ = IID_IMFSaveJob


                IMFSaveJob._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginSave')],
                        HRESULT,
                        'BeginSave',
                        (['in'], POINTER(IMFByteStream), 'pStream'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'pState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndSave')],
                        HRESULT,
                        'EndSave',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CancelSave')],
                        HRESULT,
                        'CancelSave',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProgress')],
                        HRESULT,
                        'GetProgress',
                        (['out'], POINTER(DWORD), 'pdwPercentComplete'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSaveJob_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0068
        # [local]
        MFNET_SAVEJOB_SERVICE = EXTERN_GUID(
            0xB85A587F,
            0x3D02,
            0x4E52,
            0x95,
            0x65,
            0x55,
            0xD3,
            0xEC,
            0x1E,
            0x7F,
            0xF7
        )


        class _MFNETSOURCE_PROTOCOL_TYPE(ENUM):
            MFNETSOURCE_UNDEFINED = 0
            MFNETSOURCE_HTTP = 0x1
            MFNETSOURCE_RTSP = 0x2
            MFNETSOURCE_FILE = 0x3
            MFNETSOURCE_MULTICAST = 0x4

        MFNETSOURCE_PROTOCOL_TYPE = _MFNETSOURCE_PROTOCOL_TYPE
        if not defined(__IMFNetSchemeHandlerConfig_INTERFACE_DEFINED__):
            # interface IMFNetSchemeHandlerConfig
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFNetSchemeHandlerConfig = MIDL_INTERFACE(
                    "{7BE19E73-C9BF-468A-AC5A-A5E8653BEC87}"
                )
                IMFNetSchemeHandlerConfig._iid_ = IID_IMFNetSchemeHandlerConfig


                IMFNetSchemeHandlerConfig._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetNumberOfSupportedProtocols')],
                        HRESULT,
                        'GetNumberOfSupportedProtocols',
                        (['out'], POINTER(ULONG), 'pcProtocols'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSupportedProtocolType')],
                        HRESULT,
                        'GetSupportedProtocolType',
                        (['in'], ULONG, 'nProtocolIndex'),
                        (
                            ['out'],
                            POINTER(MFNETSOURCE_PROTOCOL_TYPE),
                           'pnProtocolType'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ResetProtocolRolloverSettings')],
                        HRESULT,
                        'ResetProtocolRolloverSettings',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFNetSchemeHandlerConfig_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0069
        # [local]
        # STDAPI MFCreateNetSchemePlugin(
        # REFIID riid,
        # LPVOID *ppvHandler );
        MFCreateNetSchemePlugin = mf.MFCreateNetSchemePlugin
        MFCreateNetSchemePlugin.restype = STDAPI


        class _MFNETSOURCE_TRANSPORT_TYPE(ENUM):
            MFNETSOURCE_UDP = 0
            MFNETSOURCE_TCP = MFNETSOURCE_UDP + 1 )
        MFNETSOURCE_TRANSPORT_TYPE = _MFNETSOURCE_TRANSPORT_TYPE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MFNETSOURCE_CACHE_STATE(ENUM):
            MFNETSOURCE_CACHE_UNAVAILABLE = 0
            MFNETSOURCE_CACHE_ACTIVE_WRITING = (
                MFNETSOURCE_CACHE_UNAVAILABLE + 1 )
            )
            MFNETSOURCE_CACHE_ACTIVE_COMPLETE = (
                MFNETSOURCE_CACHE_ACTIVE_WRITING + 1 )
            )
        MFNETSOURCE_CACHE_STATE = _MFNETSOURCE_CACHE_STATE


        class _MFNETSOURCE_STATISTICS_IDS(ENUM):
            MFNETSOURCE_RECVPACKETS_ID = 0
            MFNETSOURCE_LOSTPACKETS_ID = MFNETSOURCE_RECVPACKETS_ID + 1 )
            MFNETSOURCE_RESENDSREQUESTED_ID = MFNETSOURCE_LOSTPACKETS_ID + 1 )
            MFNETSOURCE_RESENDSRECEIVED_ID = (
                MFNETSOURCE_RESENDSREQUESTED_ID + 1 )
            )
            MFNETSOURCE_RECOVEREDBYECCPACKETS_ID = (
                MFNETSOURCE_RESENDSRECEIVED_ID + 1 )
            )
            MFNETSOURCE_RECOVEREDBYRTXPACKETS_ID = (
                MFNETSOURCE_RECOVEREDBYECCPACKETS_ID + 1 )
            )
            MFNETSOURCE_OUTPACKETS_ID = (
                MFNETSOURCE_RECOVEREDBYRTXPACKETS_ID + 1 )
            )
            MFNETSOURCE_RECVRATE_ID = MFNETSOURCE_OUTPACKETS_ID + 1 )
            MFNETSOURCE_AVGBANDWIDTHBPS_ID = MFNETSOURCE_RECVRATE_ID + 1 )
            MFNETSOURCE_BYTESRECEIVED_ID = MFNETSOURCE_AVGBANDWIDTHBPS_ID + 1 )
            MFNETSOURCE_PROTOCOL_ID = MFNETSOURCE_BYTESRECEIVED_ID + 1 )
            MFNETSOURCE_TRANSPORT_ID = MFNETSOURCE_PROTOCOL_ID + 1 )
            MFNETSOURCE_CACHE_STATE_ID = MFNETSOURCE_TRANSPORT_ID + 1 )
            MFNETSOURCE_LINKBANDWIDTH_ID = MFNETSOURCE_CACHE_STATE_ID + 1 )
            MFNETSOURCE_CONTENTBITRATE_ID = MFNETSOURCE_LINKBANDWIDTH_ID + 1 )
            MFNETSOURCE_SPEEDFACTOR_ID = MFNETSOURCE_CONTENTBITRATE_ID + 1 )
            MFNETSOURCE_BUFFERSIZE_ID = MFNETSOURCE_SPEEDFACTOR_ID + 1 )
            MFNETSOURCE_BUFFERPROGRESS_ID = MFNETSOURCE_BUFFERSIZE_ID + 1 )
            MFNETSOURCE_LASTBWSWITCHTS_ID = MFNETSOURCE_BUFFERPROGRESS_ID + 1 )
            MFNETSOURCE_SEEKRANGESTART_ID = MFNETSOURCE_LASTBWSWITCHTS_ID + 1 )
            MFNETSOURCE_SEEKRANGEEND_ID = MFNETSOURCE_SEEKRANGESTART_ID + 1 )
            MFNETSOURCE_BUFFERINGCOUNT_ID = MFNETSOURCE_SEEKRANGEEND_ID + 1 )
            MFNETSOURCE_INCORRECTLYSIGNEDPACKETS_ID = (
                MFNETSOURCE_BUFFERINGCOUNT_ID + 1 )
            )
            MFNETSOURCE_SIGNEDSESSION_ID = (
                MFNETSOURCE_INCORRECTLYSIGNEDPACKETS_ID + 1 )
            )
            MFNETSOURCE_MAXBITRATE_ID = MFNETSOURCE_SIGNEDSESSION_ID + 1 )
            MFNETSOURCE_RECEPTION_QUALITY_ID = MFNETSOURCE_MAXBITRATE_ID + 1 )
            MFNETSOURCE_RECOVEREDPACKETS_ID = (
                MFNETSOURCE_RECEPTION_QUALITY_ID + 1 )
            )
            MFNETSOURCE_VBR_ID = MFNETSOURCE_RECOVEREDPACKETS_ID + 1 )
            MFNETSOURCE_DOWNLOADPROGRESS_ID = MFNETSOURCE_VBR_ID + 1 )
            MFNETSOURCE_UNPREDEFINEDPROTOCOLNAME_ID = (
                MFNETSOURCE_DOWNLOADPROGRESS_ID + 1 )
            )
        MFNETSOURCE_STATISTICS_IDS = _MFNETSOURCE_STATISTICS_IDS
        MFNETSOURCE_STATISTICS_SERVICE = EXTERN_GUID(
            0x3CB1F275,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_STATISTICS = EXTERN_GUID(
            0x3CB1F274,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        MFNETSOURCE_BUFFERINGTIME = EXTERN_GUID(
            0x3CB1F276,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ACCELERATEDSTREAMINGDURATION = EXTERN_GUID(
            0x3CB1F277,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_MAXUDPACCELERATEDSTREAMINGDURATION = EXTERN_GUID(
            0x4AAB2879,
            0xBBE1,
            0x4994,
            0x9F,
            0xF0,
            0x54,
            0x95,
            0xBD,
            0x25,
            0x1,
            0x29
        )
        MFNETSOURCE_MAXBUFFERTIMEMS = EXTERN_GUID(
            0x408B24E6,
            0x4038,
            0x4401,
            0xB5,
            0xB2,
            0xFE,
            0x70,
            0x1A,
            0x9E,
            0xBF,
            0x10
        )
        MFNETSOURCE_CONNECTIONBANDWIDTH = EXTERN_GUID(
            0x3CB1F278,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_CACHEENABLED = EXTERN_GUID(
            0x3CB1F279,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_AUTORECONNECTLIMIT = EXTERN_GUID(
            0x3CB1F27A,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_RESENDSENABLED = EXTERN_GUID(
            0x3CB1F27B,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_THINNINGENABLED = EXTERN_GUID(
            0x3CB1F27C,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROTOCOL = EXTERN_GUID(
            0x3CB1F27D,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_TRANSPORT = EXTERN_GUID(
            0x3CB1F27E,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            MFNETSOURCE_PREVIEWMODEENABLED = EXTERN_GUID(
                0x3CB1F27F,
                0x0505,
                0x4C5D,
                0xAE,
                0x71,
                0x0A,
                0x55,
                0x63,
                0x44,
                0xEF,
                0xA1
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        MFNETSOURCE_CREDENTIAL_MANAGER = EXTERN_GUID(
            0x3CB1F280,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PPBANDWIDTH = EXTERN_GUID(
            0x3CB1F281,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_AUTORECONNECTPROGRESS = EXTERN_GUID(
            0x3CB1F282,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROXYLOCATORFACTORY = EXTERN_GUID(
            0x3CB1F283,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_BROWSERUSERAGENT = EXTERN_GUID(
            0x3CB1F28B,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_BROWSERWEBPAGE = EXTERN_GUID(
            0x3CB1F28C,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PLAYERVERSION = EXTERN_GUID(
            0x3CB1F28D,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PLAYERID = EXTERN_GUID(
            0x3CB1F28E,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_HOSTEXE = EXTERN_GUID(
            0x3CB1F28F,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_HOSTVERSION = EXTERN_GUID(
            0x3CB1F291,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PLAYERUSERAGENT = EXTERN_GUID(
            0x3CB1F292,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            MFNETSOURCE_CLIENTGUID = EXTERN_GUID(
                0x60A2C4A6,
                0xF197,
                0x4C14,
                0xA5,
                0xBF,
                0x88,
                0x83,
                0xD,
                0x24,
                0x58,
                0xAF
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        MFNETSOURCE_LOGURL = EXTERN_GUID(
            0x3CB1F293,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_UDP = EXTERN_GUID(
            0x3CB1F294,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_TCP = EXTERN_GUID(
            0x3CB1F295,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_MSB = EXTERN_GUID(
            0x3CB1F296,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_RTSP = EXTERN_GUID(
            0x3CB1F298,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_HTTP = EXTERN_GUID(
            0x3CB1F299,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_STREAMING = EXTERN_GUID(
            0x3CB1F29C,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_DOWNLOAD = EXTERN_GUID(
            0x3CB1F29D,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_ENABLE_PRIVATEMODE = EXTERN_GUID(
            0x824779D8,
            0xF18B,
            0x4405,
            0x8C,
            0xF1,
            0x46,
            0x4F,
            0xB5,
            0xAA,
            0x8F,
            0x71
        )
        MFNETSOURCE_UDP_PORT_RANGE = EXTERN_GUID(
            0x3CB1F29A,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROXYINFO = EXTERN_GUID(
            0x3CB1F29B,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_DRMNET_LICENSE_REPRESENTATION = EXTERN_GUID(
            0x47EAE1BD,
            0xBDFE,
            0x42E2,
            0x82,
            0xF3,
            0x54,
            0xA4,
            0x8C,
            0x17,
            0x96,
            0x2D
        )
        MFNETSOURCE_PROXYSETTINGS = EXTERN_GUID(
            0x3CB1F287,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROXYHOSTNAME = EXTERN_GUID(
            0x3CB1F284,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROXYPORT = EXTERN_GUID(
            0x3CB1F288,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROXYEXCEPTIONLIST = EXTERN_GUID(
            0x3CB1F285,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROXYBYPASSFORLOCAL = EXTERN_GUID(
            0x3CB1F286,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        MFNETSOURCE_PROXYRERUNAUTODETECTION = EXTERN_GUID(
            0x3CB1F289,
            0x0505,
            0x4C5D,
            0xAE,
            0x71,
            0x0A,
            0x55,
            0x63,
            0x44,
            0xEF,
            0xA1
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            MFNETSOURCE_STREAM_LANGUAGE = EXTERN_GUID(
                0x9AB44318,
                0xF7CD,
                0x4F2D,
                0x8D,
                0x6D,
                0xFA,
                0x35,
                0xB4,
                0x92,
                0xCE,
                0xCB
            )
            MFNETSOURCE_LOGPARAMS = EXTERN_GUID(
                0x64936AE8,
                0x9418,
                0x453A,
                0x8C,
                0xDA,
                0x3E,
                0xA,
                0x66,
                0x8B,
                0x35,
                0x3B
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINVER >= _WIN32_WINNT_WIN8:
            MFNETSOURCE_PEERMANAGER = EXTERN_GUID(
                0x48B29ADB,
                0xFEBF,
                0x45EE,
                0xA9,
                0xBF,
                0xEF,
                0xB8,
                0x1C,
                0x49,
                0x2E,
                0xFC
            )
            MFNETSOURCE_FRIENDLYNAME = EXTERN_GUID(
                0x5B2A7757,
                0xBC6B,
                0x447E,
                0xAA,
                0x06,
                0x0D,
                0xDA,
                0x1C,
                0x64,
                0x6E,
                0x2F
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)


        class _MFNET_PROXYSETTINGS(ENUM):
            MFNET_PROXYSETTING_NONE = 0
            MFNET_PROXYSETTING_MANUAL = 1
            MFNET_PROXYSETTING_AUTO = 2
            MFNET_PROXYSETTING_BROWSER = 3

        MFNET_PROXYSETTINGS = _MFNET_PROXYSETTINGS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFSchemeHandler_INTERFACE_DEFINED__):
            # interface IMFSchemeHandler
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSchemeHandler = MIDL_INTERFACE(
                    "{6D4C7B74-52A0-4BB7-B0DB-55F29F47A668}"
                )
                IMFSchemeHandler._iid_ = IID_IMFSchemeHandler


                IMFSchemeHandler._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginCreateObject')],
                        HRESULT,
                        'BeginCreateObject',
                        (['in'], LPCWSTR, 'pwszURL'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], POINTER(IPropertyStore), 'pProps'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppIUnknownCancelCookie'
                        ),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndCreateObject')],
                        HRESULT,
                        'EndCreateObject',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(MF_OBJECT_TYPE), 'pObjectType'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppObject'
                        ),
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
                ]

            # END IF  C style interface
        # END IF  __IMFSchemeHandler_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0070
        # [local]
        if WINVER >= _WIN32_WINNT_WIN7:
            MF_BYTESTREAMHANDLER_ACCEPTS_SHARE_WRITE = EXTERN_GUID(
                0xA6E1F733,
                0x3001,
                0x4915,
                0x81,
                0x50,
                0x15,
                0x58,
                0xA2,
                0x18,
                0xE,
                0xC8
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if not defined(__IMFByteStreamHandler_INTERFACE_DEFINED__):
            # interface IMFByteStreamHandler
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFByteStreamHandler = MIDL_INTERFACE(
                    "{BB420AA4-765B-4A1F-91FE-D6A8A143924C}"
                )
                IMFByteStreamHandler._iid_ = IID_IMFByteStreamHandler


                IMFByteStreamHandler._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginCreateObject')],
                        HRESULT,
                        'BeginCreateObject',
                        (['in'], POINTER(IMFByteStream), 'pByteStream'),
                        (['in'], LPCWSTR, 'pwszURL'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], POINTER(IPropertyStore), 'pProps'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppIUnknownCancelCookie'
                        ),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndCreateObject')],
                        HRESULT,
                        'EndCreateObject',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(MF_OBJECT_TYPE), 'pObjectType'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppObject'
                        ),
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
                        [helpstring('Method GetMaxNumberOfBytesRequiredForResolution')],
                        HRESULT,
                        'GetMaxNumberOfBytesRequiredForResolution',
                        (['out'], POINTER(QWORD), 'pqwBytes'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFByteStreamHandler_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0071
        # [local]
        MF_BYTESTREAM_SERVICE = EXTERN_GUID(
            0xAB025E2B,
            0x16D9,
            0x4180,
            0xA1,
            0x27,
            0xBA,
            0x6C,
            0x70,
            0x15,
            0x61,
            0x61
        )
        if not defined(__IMFTrustedInput_INTERFACE_DEFINED__):
            # interface IMFTrustedInput
            # [helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTrustedInput = MIDL_INTERFACE(
                    "{542612C4-A1B8-4632-B521-DE11EA64A0B0}"
                )
                IMFTrustedInput._iid_ = IID_IMFTrustedInput


                IMFTrustedInput._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetInputTrustAuthority')],
                        HRESULT,
                        'GetInputTrustAuthority',
                        (['in'], DWORD, 'dwStreamID'),
                        (['in'], REFIID, 'riid'),
                        (
                            ['out', 'iid_is'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppunkObject'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTrustedInput_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0072
        # [local]
        class _MFPOLICYMANAGER_ACTION(ENUM):
            PEACTION_NO = 0
            PEACTION_PLAY = 1
            PEACTION_COPY = 2
            PEACTION_EXPORT = 3
            PEACTION_EXTRACT = 4
            PEACTION_RESERVED1 = 5
            PEACTION_RESERVED2 = 6
            PEACTION_RESERVED3 = 7
            PEACTION_LAST = 7

        MFPOLICYMANAGER_ACTION = _MFPOLICYMANAGER_ACTION

        _MFINPUTTRUSTAUTHORITY_ACTION._fields_ = [
            ('Action', MFPOLICYMANAGER_ACTION),
            ('pbTicket', POINTER(BYTE)),
            ('cbTicket', DWORD),
        ]

        _MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS._fields_ = [
            ('dwSize', DWORD),
            ('dwVer', DWORD),
            ('cbSignatureOffset', DWORD),
            ('cbSignatureSize', DWORD),
            ('cbExtensionOffset', DWORD),
            ('cbExtensionSize', DWORD),
            ('cActions', DWORD),
            ('rgOutputActions', MFINPUTTRUSTAUTHORITY_ACCESS_ACTION * 1),
        ]
        MF_MEDIA_PROTECTION_MANAGER_PROPERTIES = EXTERN_GUID(
            0x38BD81A9,
            0xACEA,
            0x4C73,
            0x89,
            0xB2,
            0x55,
            0x32,
            0xC0,
            0xAE,
            0xCA,
            0x79
        )
        if not defined(__IMFInputTrustAuthority_INTERFACE_DEFINED__):
            # interface IMFInputTrustAuthority
            # [helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFInputTrustAuthority = MIDL_INTERFACE(
                    "{D19F8E98-B126-4446-890C-5DCB7AD71453}"
                )
                IMFInputTrustAuthority._iid_ = IID_IMFInputTrustAuthority


                IMFInputTrustAuthority._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetDecrypter'), 'local'],
                        HRESULT,
                        'GetDecrypter',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RequestAccess'), 'local'],
                        HRESULT,
                        'RequestAccess',
                        (['in'], MFPOLICYMANAGER_ACTION, 'Action'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFActivate)),
                           'ppContentEnablerActivate'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPolicy'), 'local'],
                        HRESULT,
                        'GetPolicy',
                        (['in'], MFPOLICYMANAGER_ACTION, 'Action'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFOutputPolicy)),
                           'ppPolicy'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method BindAccess'), 'local'],
                        HRESULT,
                        'BindAccess',
                        (
                            ['in'],
                            POINTER(MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS),
                           'pParam'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method UpdateAccess'), 'local'],
                        HRESULT,
                        'UpdateAccess',
                        (
                            ['in'],
                            POINTER(MFINPUTTRUSTAUTHORITY_ACCESS_PARAMS),
                           'pParam'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Reset')],
                        HRESULT,
                        'Reset',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFInputTrustAuthority_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0073
        # [local]
        if not defined(__IMFTrustedOutput_INTERFACE_DEFINED__):
            # interface IMFTrustedOutput
            # [local][unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTrustedOutput = MIDL_INTERFACE(
                    "{D19F8E95-B126-4446-890C-5DCB7AD71453}"
                )
                IMFTrustedOutput._iid_ = IID_IMFTrustedOutput


                IMFTrustedOutput._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetOutputTrustAuthorityCount')],
                        HRESULT,
                        'GetOutputTrustAuthorityCount',
                        (['out'], POINTER(DWORD), 'pcOutputTrustAuthorities'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputTrustAuthorityByIndex')],
                        HRESULT,
                        'GetOutputTrustAuthorityByIndex',
                        (['in'], DWORD, 'dwIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFOutputTrustAuthority)),
                           'ppauthority'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsFinal')],
                        HRESULT,
                        'IsFinal',
                        (['out'], POINTER(BOOL), 'pfIsFinal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTrustedOutput_INTERFACE_DEFINED__

        if not defined(__IMFOutputTrustAuthority_INTERFACE_DEFINED__):
            # interface IMFOutputTrustAuthority
            # [local][unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFOutputTrustAuthority = MIDL_INTERFACE(
                    "{D19F8E94-B126-4446-890C-5DCB7AD71453}"
                )
                IMFOutputTrustAuthority._iid_ = IID_IMFOutputTrustAuthority


                IMFOutputTrustAuthority._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetAction')],
                        HRESULT,
                        'GetAction',
                        (['out'], POINTER(MFPOLICYMANAGER_ACTION), 'pAction'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetPolicy')],
                        HRESULT,
                        'SetPolicy',
                        (
                            ['in'],
                            POINTER(POINTER(IMFOutputPolicy)),
                           'ppPolicy'
                        ),
                        (['in'], DWORD, 'nPolicy'),
                        (['out'], POINTER(POINTER(BYTE)), 'ppbTicket'),
                        (['out'], POINTER(DWORD), 'pcbTicket'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFOutputTrustAuthority_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0075
        # [local]
        if not defined(__IMFOutputPolicy_INTERFACE_DEFINED__):
            # interface IMFOutputPolicy
            # [local][unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFOutputPolicy = MIDL_INTERFACE(
                    "{7F00F10A-DAED-41AF-AB26-5FDFA4DFBA3C}"
                )
                IMFOutputPolicy._iid_ = IID_IMFOutputPolicy


                IMFOutputPolicy._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GenerateRequiredSchemas')],
                        HRESULT,
                        'GenerateRequiredSchemas',
                        (['in'], DWORD, 'dwAttributes'),
                        (['in'], GUID, 'guidOutputSubType'),
                        (
                            ['in'],
                            POINTER(GUID),
                           'rgGuidProtectionSchemasSupported'
                        ),
                        (['in'], DWORD, 'cProtectionSchemasSupported'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFCollection)),
                           'ppRequiredProtectionSchemas'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOriginatorID')],
                        HRESULT,
                        'GetOriginatorID',
                        (['out'], POINTER(GUID), 'pguidOriginatorID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMinimumGRLVersion')],
                        HRESULT,
                        'GetMinimumGRLVersion',
                        (['out'], POINTER(DWORD), 'pdwMinimumGRLVersion'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFOutputPolicy_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0076
        # [local]
        MFCONNECTOR_SPDIF = EXTERN_GUID(
            0xB94A712,
            0xAD3E,
            0x4CEE,
            0x83,
            0xCE,
            0xCE,
            0x32,
            0xE3,
            0xDB,
            0x65,
            0x22
        )
        MFCONNECTOR_UNKNOWN = EXTERN_GUID(
            0xAC3AEF5C,
            0xCE43,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_PCI = EXTERN_GUID(
            0xAC3AEF5D,
            0xCE43,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_PCIX = EXTERN_GUID(
            0xAC3AEF5E,
            0xCE43,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_PCI_Express = EXTERN_GUID(
            0xAC3AEF5F,
            0xCE43,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_AGP = EXTERN_GUID(
            0xAC3AEF60,
            0xCE43,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_VGA = EXTERN_GUID(
            0x57CD5968,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_SVIDEO = EXTERN_GUID(
            0x57CD5969,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_COMPOSITE = EXTERN_GUID(
            0x57CD596A,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_COMPONENT = EXTERN_GUID(
            0x57CD596B,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_DVI = EXTERN_GUID(
            0x57CD596C,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_HDMI = EXTERN_GUID(
            0x57CD596D,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_LVDS = EXTERN_GUID(
            0x57CD596E,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_D_JPN = EXTERN_GUID(
            0x57CD5970,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_SDI = EXTERN_GUID(
            0x57CD5971,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_DISPLAYPORT_EXTERNAL = EXTERN_GUID(
            0x57CD5972,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_DISPLAYPORT_EMBEDDED = EXTERN_GUID(
            0x57CD5973,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_UDI_EXTERNAL = EXTERN_GUID(
            0x57CD5974,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_UDI_EMBEDDED = EXTERN_GUID(
            0x57CD5975,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_MIRACAST = EXTERN_GUID(
            0x57CD5977,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_TRANSPORT_AGNOSTIC_DIGITAL_MODE_A = EXTERN_GUID(
            0x57CD5978,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        MFCONNECTOR_TRANSPORT_AGNOSTIC_DIGITAL_MODE_B = EXTERN_GUID(
            0x57CD5979,
            0xCE47,
            0x11D9,
            0x92,
            0xDB,
            0x00,
            0x0B,
            0xDB,
            0x28,
            0xFF,
            0x98
        )
        if not defined(__IMFOutputSchema_INTERFACE_DEFINED__):
            # interface IMFOutputSchema
            # [local][unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFOutputSchema = MIDL_INTERFACE(
                    "{7BE0FC5B-ABD9-44FB-A5C8-F50136E71599}"
                )
                IMFOutputSchema._iid_ = IID_IMFOutputSchema


                IMFOutputSchema._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSchemaType')],
                        HRESULT,
                        'GetSchemaType',
                        (['out'], POINTER(GUID), 'pguidSchemaType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetConfigurationData')],
                        HRESULT,
                        'GetConfigurationData',
                        (['out'], POINTER(DWORD), 'pdwVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOriginatorID')],
                        HRESULT,
                        'GetOriginatorID',
                        (['out'], POINTER(GUID), 'pguidOriginatorID'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFOutputSchema_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0077
        # [local]
        MFPROTECTION_DISABLE = EXTERN_GUID(
            0x8CC6D81B,
            0xFEC6,
            0x4D8F,
            0x96,
            0x4B,
            0xCF,
            0xBA,
            0x0B,
            0x0D,
            0xAD,
            0x0D
        )
        MFPROTECTION_CONSTRICTVIDEO = EXTERN_GUID(
            0x193370CE,
            0xC5E4,
            0x4C3A,
            0x8A,
            0x66,
            0x69,
            0x59,
            0xB4,
            0xDA,
            0x44,
            0x42
        )
        MFPROTECTION_CONSTRICTVIDEO_NOOPM = EXTERN_GUID(
            0xA580E8CD,
            0xC247,
            0x4957,
            0xB9,
            0x83,
            0x3C,
            0x2E,
            0xEB,
            0xD1,
            0xFF,
            0x59
        )
        MFPROTECTION_CONSTRICTAUDIO = EXTERN_GUID(
            0xFFC99B44,
            0xDF48,
            0x4E16,
            0x8E,
            0x66,
            0x09,
            0x68,
            0x92,
            0xC1,
            0x57,
            0x8A
        )
        MFPROTECTION_TRUSTEDAUDIODRIVERS = EXTERN_GUID(
            0x65BDF3D2,
            0x0168,
            0x4816,
            0xA5,
            0x33,
            0x55,
            0xD4,
            0x7B,
            0x02,
            0x71,
            0x01
        )
        MFPROTECTION_HDCP = EXTERN_GUID(
            0xAE7CC03D,
            0xC828,
            0x4021,
            0xAC,
            0xB7,
            0xD5,
            0x78,
            0xD2,
            0x7A,
            0xAF,
            0x13
        )
        MFPROTECTION_CGMSA = EXTERN_GUID(
            0xE57E69E9,
            0x226B,
            0x4D31,
            0xB4,
            0xE3,
            0xD3,
            0xDB,
            0x00,
            0x87,
            0x36,
            0xDD
        )
        MFPROTECTION_ACP = EXTERN_GUID(
            0xC3FD11C6,
            0xF8B7,
            0x4D20,
            0xB0,
            0x08,
            0x1D,
            0xB1,
            0x7D,
            0x61,
            0xF2,
            0xDA
        )
        MFPROTECTION_WMDRMOTA = EXTERN_GUID(
            0xA267A6A1,
            0x362E,
            0x47D0,
            0x88,
            0x05,
            0x46,
            0x28,
            0x59,
            0x8A,
            0x23,
            0xE4
        )
        MFPROTECTION_FFT = EXTERN_GUID(
            0x462A56B2,
            0x2866,
            0x4BB6,
            0x98,
            0x0D,
            0x6D,
            0x8D,
            0x9E,
            0xDB,
            0x1A,
            0x8C
        )
        MFPROTECTION_PROTECTED_SURFACE = EXTERN_GUID(
            0x4F5D9566,
            0xE742,
            0x4A25,
            0x8D,
            0x1F,
            0xD2,
            0x87,
            0xB5,
            0xFA,
            0x0A,
            0xDE
        )
        MFPROTECTION_DISABLE_SCREEN_SCRAPE = EXTERN_GUID(
            0xA21179A4,
            0xB7CD,
            0x40D8,
            0x96,
            0x14,
            0x8E,
            0xF2,
            0x37,
            0x1B,
            0xA7,
            0x8D
        )
        MFPROTECTION_VIDEO_FRAMES = EXTERN_GUID(
            0x36A59CBC,
            0x7401,
            0x4A8C,
            0xBC,
            0x20,
            0x46,
            0xA7,
            0xC9,
            0xE5,
            0x97,
            0xF0
        )
        MFPROTECTION_HARDWARE = EXTERN_GUID(
            0x4EE7F0C1,
            0x9ED7,
            0x424F,
            0xB6,
            0xBE,
            0x99,
            0x6B,
            0x33,
            0x52,
            0x88,
            0x56
        )
        MFPROTECTION_HDCP_WITH_TYPE_ENFORCEMENT = EXTERN_GUID(
            0xA4A585E8,
            0xED60,
            0x442D,
            0x81,
            0x4D,
            0xDB,
            0x4D,
            0x42,
            0x20,
            0xA0,
            0x6D
        )


        class _MF_OPM_CGMSA_PROTECTION_LEVEL(ENUM):
            MF_OPM_CGMSA_OFF = 0
            MF_OPM_CGMSA_COPY_FREELY = 0x1
            MF_OPM_CGMSA_COPY_NO_MORE = 0x2
            MF_OPM_CGMSA_COPY_ONE_GENERATION = 0x3
            MF_OPM_CGMSA_COPY_NEVER = 0x4
            MF_OPM_CGMSA_REDISTRIBUTION_CONTROL_REQUIRED = 0x8

        MF_OPM_CGMSA_PROTECTION_LEVEL = _MF_OPM_CGMSA_PROTECTION_LEVEL


        class _MF_OPM_ACP_PROTECTION_LEVEL(ENUM):
            MF_OPM_ACP_OFF = 0
            MF_OPM_ACP_LEVEL_ONE = 1
            MF_OPM_ACP_LEVEL_TWO = 2
            MF_OPM_ACP_LEVEL_THREE = 3
            MF_OPM_ACP_FORCE_ULONG = 0x7FFFFFFF

        MF_OPM_ACP_PROTECTION_LEVEL = _MF_OPM_ACP_PROTECTION_LEVEL
        MFPROTECTIONATTRIBUTE_BEST_EFFORT = EXTERN_GUID(
            0xC8E06331,
            0x75F0,
            0x4EC1,
            0x8E,
            0x77,
            0x17,
            0x57,
            0x8F,
            0x77,
            0x3B,
            0x46
        )
        MFPROTECTIONATTRIBUTE_FAIL_OVER = EXTERN_GUID(
            0x8536ABC5,
            0x38F1,
            0x4151,
            0x9C,
            0xCE,
            0xF5,
            0x5D,
            0x94,
            0x12,
            0x29,
            0xAC
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINVER >= _WIN32_WINNT_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            MFPROTECTION_GRAPHICS_TRANSFER_AES_ENCRYPTION = EXTERN_GUID(
                0xC873DE64,
                0xD8A5,
                0x49E6,
                0x88,
                0xBB,
                0xFB,
                0x96,
                0x3F,
                0xD3,
                0xD4,
                0xCE
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        MFPROTECTIONATTRIBUTE_CONSTRICTVIDEO_IMAGESIZE = EXTERN_GUID(
            0x8476FC,
            0x4B58,
            0x4D80,
            0xA7,
            0x90,
            0xE7,
            0x29,
            0x76,
            0x73,
            0x16,
            0x1D
        )
        MFPROTECTIONATTRIBUTE_HDCP_SRM = EXTERN_GUID(
            0x6F302107,
            0x3477,
            0x4468,
            0x8A,
            0x8,
            0xEE,
            0xF9,
            0xDB,
            0x10,
            0xE2,
            0xF
        )


        class _MFAudioConstriction(ENUM):
            MFaudioConstrictionOff = 0
            MFaudioConstriction48_16 = MFaudioConstrictionOff + 1 )
            MFaudioConstriction44_16 = MFaudioConstriction48_16 + 1 )
            MFaudioConstriction14_14 = MFaudioConstriction44_16 + 1 )
            MFaudioConstrictionMute = MFaudioConstriction14_14 + 1 )
        MFAudioConstriction = _MFAudioConstriction
        if WINVER >= _WIN32_WINNT_WIN7:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINVER >= _WIN32_WINNT_WIN7:
            pass
        else:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFSecureChannel_INTERFACE_DEFINED__):
            # interface IMFSecureChannel
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSecureChannel = MIDL_INTERFACE(
                    "{D0AE555D-3B12-4D97-B060-0990BC5AEB67}"
                )
                IMFSecureChannel._iid_ = IID_IMFSecureChannel


                IMFSecureChannel._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCertificate')],
                        HRESULT,
                        'GetCertificate',
                        (['out'], POINTER(POINTER(BYTE)), 'ppCert'),
                        (['out'], POINTER(DWORD), 'pcbCert'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetupSession')],
                        HRESULT,
                        'SetupSession',
                        (['in'], POINTER(BYTE), 'pbEncryptedSessionKey'),
                        (['in'], DWORD, 'cbSessionKey'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSecureChannel_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0078
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class SAMPLE_PROTECTION_VERSION(ENUM):
            SAMPLE_PROTECTION_VERSION_NO = 0
            SAMPLE_PROTECTION_VERSION_BASIC_LOKI = 1
            SAMPLE_PROTECTION_VERSION_SCATTER = 2
            SAMPLE_PROTECTION_VERSION_RC4 = 3
            SAMPLE_PROTECTION_VERSION_AES128CTR = 4

        MF_SampleProtectionSalt = EXTERN_GUID(
            0x5403DEEE,
            0xB9EE,
            0x438F,
            0xAA,
            0x83,
            0x38,
            0x4,
            0x99,
            0x7E,
            0x56,
            0x9D
        )
        if not defined(__IMFSampleProtection_INTERFACE_DEFINED__):
            # interface IMFSampleProtection
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSampleProtection = MIDL_INTERFACE(
                    "{8E36395F-C7B9-43C4-A54D-512B4AF63C95}"
                )
                IMFSampleProtection._iid_ = IID_IMFSampleProtection


                IMFSampleProtection._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetInputProtectionVersion')],
                        HRESULT,
                        'GetInputProtectionVersion',
                        (['out'], POINTER(DWORD), 'pdwVersion'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOutputProtectionVersion')],
                        HRESULT,
                        'GetOutputProtectionVersion',
                        (['out'], POINTER(DWORD), 'pdwVersion'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProtectionCertificate')],
                        HRESULT,
                        'GetProtectionCertificate',
                        (['in'], DWORD, 'dwVersion'),
                        (['out'], POINTER(POINTER(BYTE)), 'ppCert'),
                        (['out'], POINTER(DWORD), 'pcbCert'),
                    ),
                    COMMETHOD(
                        [helpstring('Method InitOutputProtection')],
                        HRESULT,
                        'InitOutputProtection',
                        (['in'], DWORD, 'dwVersion'),
                        (['in'], DWORD, 'dwOutputId'),
                        (['in'], POINTER(BYTE), 'pbCert'),
                        (['in'], DWORD, 'cbCert'),
                        (['out'], POINTER(POINTER(BYTE)), 'ppbSeed'),
                        (['out'], POINTER(DWORD), 'pcbSeed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method InitInputProtection')],
                        HRESULT,
                        'InitInputProtection',
                        (['in'], DWORD, 'dwVersion'),
                        (['in'], DWORD, 'dwInputId'),
                        (['in'], POINTER(BYTE), 'pbSeed'),
                        (['in'], DWORD, 'cbSeed'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSampleProtection_INTERFACE_DEFINED__

        if not defined(__IMFMediaSinkPreroll_INTERFACE_DEFINED__):
            # interface IMFMediaSinkPreroll
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaSinkPreroll = MIDL_INTERFACE(
                    "{5DFD4B2A-7674-4110-A4E6-8A68FD5F3688}"
                )
                IMFMediaSinkPreroll._iid_ = IID_IMFMediaSinkPreroll


                IMFMediaSinkPreroll._methods_ = [
                    COMMETHOD(
                        [helpstring('Method NotifyPreroll')],
                        HRESULT,
                        'NotifyPreroll',
                        (['in'], MFTIME, 'hnsUpcomingStartTime'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaSinkPreroll_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0080
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFFinalizableMediaSink_INTERFACE_DEFINED__):
            # interface IMFFinalizableMediaSink
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFFinalizableMediaSink = MIDL_INTERFACE(
                    "{EAECB74A-9A50-42CE-9541-6A7F57AA4AD7}"
                )
                IMFFinalizableMediaSink._iid_ = IID_IMFFinalizableMediaSink


                IMFFinalizableMediaSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BeginFinalize')],
                        HRESULT,
                        'BeginFinalize',
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndFinalize')],
                        HRESULT,
                        'EndFinalize',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFFinalizableMediaSink_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0081
        # [local]    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if not defined(__IMFStreamingSinkConfig_INTERFACE_DEFINED__):
                # interface IMFStreamingSinkConfig
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFStreamingSinkConfig = MIDL_INTERFACE(
                        "{9DB7AA41-3CC5-40D4-8509-555804AD34CC}"
                    )
                    IMFStreamingSinkConfig._iid_ = IID_IMFStreamingSinkConfig


                    IMFStreamingSinkConfig._methods_ = [
                        COMMETHOD(
                            [helpstring('Method StartStreaming')],
                            HRESULT,
                            'StartStreaming',
                            (['in'], BOOL, 'fSeekOffsetIsByteOffset'),
                            (['in'], QWORD, 'qwSeekOffset'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFStreamingSinkConfig_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0082
            # [local]        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__IMFRemoteProxy_INTERFACE_DEFINED__):
            # interface IMFRemoteProxy
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFRemoteProxy = MIDL_INTERFACE(
                    "{994E23AD-1CC2-493C-B9FA-46F1CB040FA4}"
                )
                IMFRemoteProxy._iid_ = IID_IMFRemoteProxy


                IMFRemoteProxy._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetRemoteObject')],
                        HRESULT,
                        'GetRemoteObject',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRemoteHost')],
                        HRESULT,
                        'GetRemoteHost',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFRemoteProxy_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0083
        # [local]
        MF_REMOTE_PROXY = EXTERN_GUID(
            0x2F00C90E,
            0xD2CF,
            0x4278,
            0x8B,
            0x6A,
            0xD0,
            0x77,
            0xFA,
            0xC3,
            0xA2,
            0x5F
        )
        if not defined(__IMFObjectReferenceStream_INTERFACE_DEFINED__):
            # interface IMFObjectReferenceStream
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFObjectReferenceStream = MIDL_INTERFACE(
                    "{09EF5BE3-C8A7-469E-8B70-73BF25BB193F}"
                )
                IMFObjectReferenceStream._iid_ = IID_IMFObjectReferenceStream


                IMFObjectReferenceStream._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SaveReference')],
                        HRESULT,
                        'SaveReference',
                        (['in'], REFIID, 'riid'),
                        (['in'], POINTER(comtypes.IUnknown), 'pUnk'),
                    ),
                    COMMETHOD(
                        [helpstring('Method LoadReference')],
                        HRESULT,
                        'LoadReference',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFObjectReferenceStream_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0084
        # [local]
        CLSID_CreateMediaExtensionObject = EXTERN_GUID(
            0xEF65A54D,
            0x0788,
            0x45B8,
            0x8B,
            0x14,
            0xBC,
            0x0F,
            0x6A,
            0x6B,
            0x51,
            0x37
        )
        if not defined(__IMFPMPHost_INTERFACE_DEFINED__):
            # interface IMFPMPHost
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFPMPHost = MIDL_INTERFACE(
                    "{F70CA1A9-FDC7-4782-B994-ADFFB1C98606}"
                )
                IMFPMPHost._iid_ = IID_IMFPMPHost


                IMFPMPHost._methods_ = [
                    COMMETHOD(
                        [helpstring('Method LockProcess')],
                        HRESULT,
                        'LockProcess',
                    ),
                    COMMETHOD(
                        [helpstring('Method UnlockProcess')],
                        HRESULT,
                        'UnlockProcess',
                    ),
                    COMMETHOD(
                        [helpstring('Method CreateObjectByCLSID'), 'local'],
                        HRESULT,
                        'CreateObjectByCLSID',
                        (['in'], REFCLSID, 'clsid'),
                        (['unique', 'in'], POINTER(IStream), 'pStream'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]            # [in]            # [size_is][unique][in]            # [in]            # [in]            # [iid_is][out]        # END IF  __IMFPMPHost_INTERFACE_DEFINED__
        # interface __MIDL_itf_mfidl_0000_0085
        # [local]
        if WINVER >= _WIN32_WINNT_WIN7:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if not defined(__IMFPMPClient_INTERFACE_DEFINED__):
            # interface IMFPMPClient
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFPMPClient = MIDL_INTERFACE(
                    "{6C4E655D-EAD8-4421-B6B9-54DCDBBDF820}"
                )
                IMFPMPClient._iid_ = IID_IMFPMPClient


                IMFPMPClient._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetPMPHost')],
                        HRESULT,
                        'SetPMPHost',
                        (['in'], POINTER(IMFPMPHost), 'pPMPHost'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFPMPClient_INTERFACE_DEFINED__

        if not defined(__IMFPMPServer_INTERFACE_DEFINED__):
            # interface IMFPMPServer
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFPMPServer = MIDL_INTERFACE(
                    "{994E23AF-1CC2-493C-B9FA-46F1CB040FA4}"
                )
                IMFPMPServer._iid_ = IID_IMFPMPServer


                IMFPMPServer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method LockProcess')],
                        HRESULT,
                        'LockProcess',
                    ),
                    COMMETHOD(
                        [helpstring('Method UnlockProcess')],
                        HRESULT,
                        'UnlockProcess',
                    ),
                    COMMETHOD(
                        [helpstring('Method CreateObjectByCLSID')],
                        HRESULT,
                        'CreateObjectByCLSID',
                        (['in'], REFCLSID, 'clsid'),
                        (['in'], REFIID, 'riid'),
                        (
                            ['out', 'iid_is'],
                            POINTER(POINTER(VOID)),
                           'ppObject'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFPMPServer_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0087
        # [local]
        mf = ctypes.windll.MF


        # STDAPI MFCreatePMPServer(
        # DWORD dwCreationFlags,
        # _Outptr_ IMFPMPServer** ppPMPServer
        # );
        MFCreatePMPServer = mf.MFCreatePMPServer
        MFCreatePMPServer.restype = STDAPI


        if not defined(__IMFRemoteDesktopPlugin_INTERFACE_DEFINED__):
            # interface IMFRemoteDesktopPlugin
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFRemoteDesktopPlugin = MIDL_INTERFACE(
                    "{1CDE6309-CAE0-4940-907E-C1EC9C3D1D4A}"
                )
                IMFRemoteDesktopPlugin._iid_ = IID_IMFRemoteDesktopPlugin


                IMFRemoteDesktopPlugin._methods_ = [
                    COMMETHOD(
                        [helpstring('Method UpdateTopology')],
                        HRESULT,
                        'UpdateTopology',
                        (['out', 'in'], POINTER(IMFTopology), 'pTopology'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFRemoteDesktopPlugin_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0088
        # [local]
        # STDAPI MFCreateRemoteDesktopPlugin(
        # _Outptr_ IMFRemoteDesktopPlugin** ppPlugin );
        MFCreateRemoteDesktopPlugin = mf.MFCreateRemoteDesktopPlugin
        MFCreateRemoteDesktopPlugin.restype = STDAPI


        # EXTERN_C HRESULT STDAPICALLTYPE CreateNamedPropertyStore(
        # _Outptr_ INamedPropertyStore **ppStore
        # );
        CreateNamedPropertyStore = mf.CreateNamedPropertyStore
        CreateNamedPropertyStore.restype = HRESULT


        if not defined(__IMFSAMIStyle_INTERFACE_DEFINED__):
            # interface IMFSAMIStyle
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSAMIStyle = MIDL_INTERFACE(
                    "{A7E025DD-5303-4A62-89D6-E747E1EFAC73}"
                )
                IMFSAMIStyle._iid_ = IID_IMFSAMIStyle


                IMFSAMIStyle._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetStyleCount')],
                        HRESULT,
                        'GetStyleCount',
                        (['out'], POINTER(DWORD), 'pdwCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStyles')],
                        HRESULT,
                        'GetStyles',
                        (['out'], POINTER(PROPVARIANT), 'pPropVarStyleArray'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetSelectedStyle')],
                        HRESULT,
                        'SetSelectedStyle',
                        (['in'], LPCWSTR, 'pwszStyle'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSelectedStyle')],
                        HRESULT,
                        'GetSelectedStyle',
                        (['out'], POINTER(LPWSTR), 'ppwszStyle'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSAMIStyle_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0089
        # [local]
        MF_SAMI_SERVICE = EXTERN_GUID(
            0x49A89AE7,
            0xB4D9,
            0x4EF2,
            0xAA,
            0x5C,
            0xF6,
            0x5A,
            0x3E,
            0x5,
            0xAE,
            0x4E
        )
        MF_PD_SAMI_STYLELIST = EXTERN_GUID(
            0xE0B73C7F,
            0x486D,
            0x484E,
            0x98,
            0x72,
            0x4D,
            0xE5,
            0x19,
            0x2A,
            0x7B,
            0xF8
        )
        MF_SD_SAMI_LANGUAGE = EXTERN_GUID(
            0x36FCB98A,
            0x6CD0,
            0x44CB,
            0xAC,
            0xB9,
            0xA8,
            0xF5,
            0x60,
            0xD,
            0xD0,
            0xBB
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            mf = ctypes.windll.MF


            # STDAPI MFCreateSampleCopierMFT(_Outptr_ IMFTransform** ppCopierMFT);
            MFCreateSampleCopierMFT = mf.MFCreateSampleCopierMFT
            MFCreateSampleCopierMFT.restype = STDAPI


            if not defined(__IMFTranscodeProfile_INTERFACE_DEFINED__):
                # interface IMFTranscodeProfile
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFTranscodeProfile = MIDL_INTERFACE(
                        "{4ADFDBA3-7AB0-4953-A62B-461E7FF3DA1E}"
                    )
                    IMFTranscodeProfile._iid_ = IID_IMFTranscodeProfile


                    IMFTranscodeProfile._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetAudioAttributes')],
                            HRESULT,
                            'SetAudioAttributes',
                            (['in'], POINTER(IMFAttributes), 'pAttrs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAudioAttributes')],
                            HRESULT,
                            'GetAudioAttributes',
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttrs'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetVideoAttributes')],
                            HRESULT,
                            'SetVideoAttributes',
                            (['in'], POINTER(IMFAttributes), 'pAttrs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVideoAttributes')],
                            HRESULT,
                            'GetVideoAttributes',
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttrs'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetContainerAttributes')],
                            HRESULT,
                            'SetContainerAttributes',
                            (['in'], POINTER(IMFAttributes), 'pAttrs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetContainerAttributes')],
                            HRESULT,
                            'GetContainerAttributes',
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttrs'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFTranscodeProfile_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0090
            # [local]        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            MF_TRANSCODE_CONTAINERTYPE = EXTERN_GUID(
                0x150FF23F,
                0x4ABC,
                0x478B,
                0xAC,
                0x4F,
                0xE1,
                0x91,
                0x6F,
                0xBA,
                0x1C,
                0xCA
            )
            MFTranscodeContainerType_ASF = EXTERN_GUID(
                0x430F6F6E,
                0xB6BF,
                0x4FC1,
                0xA0,
                0xBD,
                0x9E,
                0xE4,
                0x6E,
                0xEE,
                0x2A,
                0xFB
            )
            MFTranscodeContainerType_MPEG4 = EXTERN_GUID(
                0xDC6CD05D,
                0xB9D0,
                0x40EF,
                0xBD,
                0x35,
                0xFA,
                0x62,
                0x2C,
                0x1A,
                0xB2,
                0x8A
            )
            MFTranscodeContainerType_MP3 = EXTERN_GUID(
                0xE438B912,
                0x83F1,
                0x4DE6,
                0x9E,
                0x3A,
                0x9F,
                0xFB,
                0xC6,
                0xDD,
                0x24,
                0xD1
            )
            MFTranscodeContainerType_FLAC = EXTERN_GUID(
                0x31344AA3,
                0x05A9,
                0x42B5,
                0x90,
                0x1B,
                0x8E,
                0x9D,
                0x42,
                0x57,
                0xF7,
                0x5E
            )
            MFTranscodeContainerType_3GP = EXTERN_GUID(
                0x34C50167,
                0x4472,
                0x4F34,
                0x9E,
                0xA0,
                0xC4,
                0x9F,
                0xBA,
                0xCF,
                0x03,
                0x7D
            )
            MFTranscodeContainerType_AC3 = EXTERN_GUID(
                0x6D8D91C3,
                0x8C91,
                0x4ED1,
                0x87,
                0x42,
                0x8C,
                0x34,
                0x7D,
                0x5B,
                0x44,
                0xD0
            )
            MFTranscodeContainerType_ADTS = EXTERN_GUID(
                0x132FD27D,
                0x0F02,
                0x43DE,
                0xA3,
                0x01,
                0x38,
                0xFB,
                0xBB,
                0xB3,
                0x83,
                0x4E
            )
            MFTranscodeContainerType_MPEG2 = EXTERN_GUID(
                0xBFC2DBF9,
                0x7BB4,
                0x4F8F,
                0xAF,
                0xDE,
                0xE1,
                0x12,
                0xC4,
                0x4B,
                0xA8,
                0x82
            )
            MFTranscodeContainerType_WAVE = EXTERN_GUID(
                0x64C3453C,
                0x0F26,
                0x4741,
                0xBE,
                0x63,
                0x87,
                0xBD,
                0xF8,
                0xBB,
                0x93,
                0x5B
            )
            MFTranscodeContainerType_AVI = EXTERN_GUID(
                0x7EDFE8AF,
                0x402F,
                0x4D76,
                0xA3,
                0x3C,
                0x61,
                0x9F,
                0xD1,
                0x57,
                0xD0,
                0xF1
            )
            if WINVER >= _WIN32_WINNT_WIN8:
                MFTranscodeContainerType_FMPEG4 = EXTERN_GUID(
                    0x9BA876F1,
                    0x419F,
                    0x4B77,
                    0xA1,
                    0xE0,
                    0x35,
                    0x95,
                    0x9D,
                    0x9D,
                    0x40,
                    0x4
                )
            # END IF   (WINVER >= _WIN32_WINNT_WIN8)

            MFTranscodeContainerType_AMR = EXTERN_GUID(
                0x25D5AD3,
                0x621A,
                0x475B,
                0x96,
                0x4D,
                0x66,
                0xB1,
                0xC8,
                0x24,
                0xF0,
                0x79
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            MF_TRANSCODE_SKIP_METADATA_TRANSFER = EXTERN_GUID(
                0x4E4469EF,
                0xB571,
                0x4959,
                0x8F,
                0x83,
                0x3D,
                0xCF,
                0xBA,
                0x33,
                0xA3,
                0x93
            )
            MF_TRANSCODE_TOPOLOGYMODE = EXTERN_GUID(
                0x3E3DF610,
                0x394A,
                0x40B2,
                0x9D,
                0xEA,
                0x3B,
                0xAB,
                0x65,
                0xB,
                0xEB,
                0xF2
            )


            class _MF_TRANSCODE_TOPOLOGYMODE_FLAGS(ENUM):
                MF_TRANSCODE_TOPOLOGYMODE_SOFTWARE_ONLY = 0
                MF_TRANSCODE_TOPOLOGYMODE_HARDWARE_ALLOWED = 1

            MF_TRANSCODE_TOPOLOGYMODE_FLAGS = _MF_TRANSCODE_TOPOLOGYMODE_FLAGS
            MF_TRANSCODE_ADJUST_PROFILE = EXTERN_GUID(
                0x9C37C21B,
                0x60F,
                0x487C,
                0xA6,
                0x90,
                0x80,
                0xD7,
                0xF5,
                0xD,
                0x1C,
                0x72
            )


            class _MF_TRANSCODE_ADJUST_PROFILE_FLAGS(ENUM):
                MF_TRANSCODE_ADJUST_PROFILE_DEFAULT = 0
                MF_TRANSCODE_ADJUST_PROFILE_USE_SOURCE_ATTRIBUTES = 1

            MF_TRANSCODE_ADJUST_PROFILE_FLAGS = _MF_TRANSCODE_ADJUST_PROFILE_FLAGS
            MF_TRANSCODE_ENCODINGPROFILE = EXTERN_GUID(
                0x6947787C,
                0xF508,
                0x4EA9,
                0xB1,
                0xE9,
                0xA1,
                0xFE,
                0x3A,
                0x49,
                0xFB,
                0xC9
            )
            MF_TRANSCODE_QUALITYVSSPEED = EXTERN_GUID(
                0x98332DF8,
                0x03CD,
                0x476B,
                0x89,
                0xFA,
                0x3F,
                0x9E,
                0x44,
                0x2D,
                0xEC,
                0x9F
            )
            MF_TRANSCODE_DONOT_INSERT_ENCODER = EXTERN_GUID(
                0xF45AA7CE,
                0xAB24,
                0x4012,
                0xA1,
                0x1B,
                0xDC,
                0x82,
                0x20,
                0x20,
                0x14,
                0x10
            )


            class _MF_VIDEO_PROCESSOR_ALGORITHM_TYPE(ENUM):
                MF_VIDEO_PROCESSOR_ALGORITHM_DEFAULT = 0
                MF_VIDEO_PROCESSOR_ALGORITHM_MRF_CRF_444 = 1

            MF_VIDEO_PROCESSOR_ALGORITHM_TYPE = _MF_VIDEO_PROCESSOR_ALGORITHM_TYPE
            MF_VIDEO_PROCESSOR_ALGORITHM = EXTERN_GUID(
                0x4A0A1E1F,
                0x272C,
                0x4FB6,
                0x9E,
                0xB1,
                0xDB,
                0x33,
                0xC,
                0xBC,
                0x97,
                0xCA
            )
            MF_XVP_DISABLE_FRC = EXTERN_GUID(
                0x2C0AFA19,
                0x7A97,
                0x4D5A,
                0x9E,
                0xE8,
                0x16,
                0xD4,
                0xFC,
                0x51,
                0x8D,
                0x8C
            )
            if WINVER >= _WIN32_WINNT_WINBLUE:
                MF_XVP_CALLER_ALLOCATES_OUTPUT = EXTERN_GUID(
                    0x4A2CABC,
                    0xCAB,
                    0x40B1,
                    0xA1,
                    0xB9,
                    0x75,
                    0xBC,
                    0x36,
                    0x58,
                    0xF0,
                    0x0
                )
                if WINVER < _WIN32_WINNT_WINTHRESHOLD:
                    CLSID_VideoProcessorMFT = EXTERN_GUID(
                        0x88753B26,
                        0x5B24,
                        0x49BD,
                        0xB2,
                        0xE7,
                        0xC,
                        0x44,
                        0x5C,
                        0x78,
                        0xC9,
                        0x82
                    )
                # END IF   (WINVER < _WIN32_WINNT_WINTHRESHOLD)
            # END IF   (WINVER >= _WIN32_WINNT_WINBLUE)


            # STDAPI MFCreateTranscodeProfile(
            # _Outptr_ IMFTranscodeProfile** ppTranscodeProfile
            # );
            MFCreateTranscodeProfile = mf.MFCreateTranscodeProfile
            MFCreateTranscodeProfile.restype = STDAPI


            # STDAPI MFCreateTranscodeTopology(
            # _In_ IMFMediaSource* pSrc,
            # _In_ LPCWSTR pwszOutputFilePath,
            # _In_ IMFTranscodeProfile* pProfile,
            # _Outptr_ IMFTopology** ppTranscodeTopo
            # );
            MFCreateTranscodeTopology = mf.MFCreateTranscodeTopology
            MFCreateTranscodeTopology.restype = STDAPI

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINVER >= _WIN32_WINNT_WIN8:
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                mf = ctypes.windll.MF


                # STDAPI MFCreateTranscodeTopologyFromByteStream(
                # _In_ IMFMediaSource* pSrc,
                # _In_ IMFByteStream* pOutputStream,
                # _In_ IMFTranscodeProfile* pProfile,
                # _Out_ IMFTopology** ppTranscodeTopo
                # );
                MFCreateTranscodeTopologyFromByteStream = (
                    mf.MFCreateTranscodeTopologyFromByteStream
                )
                MFCreateTranscodeTopologyFromByteStream.restype = STDAPI


            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            mf = ctypes.windll.MF


            # STDAPI MFTranscodeGetAudioOutputAvailableTypes(
            # _In_ REFGUID guidSubType,
            # _In_ DWORD dwMFTFlags,
            # _In_opt_ IMFAttributes* pCodecConfig,
            # _Outptr_ IMFCollection** ppAvailableTypes );
            MFTranscodeGetAudioOutputAvailableTypes = (
                mf.MFTranscodeGetAudioOutputAvailableTypes
            )
            MFTranscodeGetAudioOutputAvailableTypes.restype = STDAPI


            _MF_TRANSCODE_SINK_INFO._fields_ = [
                ('dwVideoStreamID', DWORD),
                ('pVideoMediaType', POINTER(IMFMediaType)),
                ('dwAudioStreamID', DWORD),
                ('pAudioMediaType', POINTER(IMFMediaType)),
            ]
            if not defined(__IMFTranscodeSinkInfoProvider_INTERFACE_DEFINED__):
                # interface IMFTranscodeSinkInfoProvider
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFTranscodeSinkInfoProvider = MIDL_INTERFACE(
                        "{8CFFCD2E-5A03-4A3A-AFF7-EDCD107C620E}"
                    )
                    IMFTranscodeSinkInfoProvider._iid_ = IID_IMFTranscodeSinkInfoProvider


                    IMFTranscodeSinkInfoProvider._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetOutputFile')],
                            HRESULT,
                            'SetOutputFile',
                            (['in'], LPCWSTR, 'pwszFileName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetOutputByteStream')],
                            HRESULT,
                            'SetOutputByteStream',
                            (
                                ['in'],
                                POINTER(IMFActivate),
                               'pByteStreamActivate'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetProfile')],
                            HRESULT,
                            'SetProfile',
                            (
                                ['in'],
                                POINTER(IMFTranscodeProfile),
                               'pProfile'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSinkInfo')],
                            HRESULT,
                            'GetSinkInfo',
                            (
                                ['out'],
                                POINTER(MF_TRANSCODE_SINK_INFO),
                               'pSinkInfo'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFTranscodeSinkInfoProvider_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0091
            # [local]
            # STDAPI MFCreateTranscodeSinkActivate(
            # _Outptr_ IMFActivate** ppActivate );
            MFCreateTranscodeSinkActivate = mf.MFCreateTranscodeSinkActivate
            MFCreateTranscodeSinkActivate.restype = STDAPI


            if not defined(__IMFFieldOfUseMFTUnlock_INTERFACE_DEFINED__):
                # interface IMFFieldOfUseMFTUnlock
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFFieldOfUseMFTUnlock = MIDL_INTERFACE(
                        "{508E71D3-EC66-4FC3-8775-B4B9ED6BA847}"
                    )
                    IMFFieldOfUseMFTUnlock._iid_ = IID_IMFFieldOfUseMFTUnlock


                    IMFFieldOfUseMFTUnlock._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Unlock')],
                            HRESULT,
                            'Unlock',
                            (['in'], POINTER(comtypes.IUnknown), 'pUnkMFT'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFFieldOfUseMFTUnlock_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0092
            # [local]
            _MFT_REGISTRATION_INFO._fields_ = [
                ('clsid', CLSID),
                ('guidCategory', GUID),
                ('uiFlags', UINT32),
                ('pszName', LPCWSTR),
                ('cInTypes', DWORD),
                # [size_is]
                ('pInTypes', POINTER(MFT_REGISTER_TYPE_INFO)),
                ('cOutTypes', DWORD),
                # [size_is]
                ('pOutTypes', POINTER(MFT_REGISTER_TYPE_INFO)),
            ]
            MF_LOCAL_MFT_REGISTRATION_SERVICE = EXTERN_GUID(
                0xDDF5CF9C,
                0x4506,
                0x45AA,
                0xAB,
                0xF0,
                0x6D,
                0x5D,
                0x94,
                0xDD,
                0x1B,
                0x4A
            )
            if not defined(__IMFLocalMFTRegistration_INTERFACE_DEFINED__):
                # interface IMFLocalMFTRegistration
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFLocalMFTRegistration = MIDL_INTERFACE(
                        "{149C4D73-B4BE-4F8D-8B87-079E926B6ADD}"
                    )
                    IMFLocalMFTRegistration._iid_ = IID_IMFLocalMFTRegistration


                    IMFLocalMFTRegistration._methods_ = [
                        COMMETHOD(
                            [helpstring('Method RegisterMFTs')],
                            HRESULT,
                            'RegisterMFTs',
                            (['in'], POINTER(MFT_REGISTRATION_INFO), 'pMFTs'),
                            ([], DWORD, 'cMFTs'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFLocalMFTRegistration_INTERFACE_DEFINED__

            if not defined(__IMFCapturePhotoConfirmation_INTERFACE_DEFINED__):
                # interface IMFCapturePhotoConfirmation
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFCapturePhotoConfirmation = MIDL_INTERFACE(
                        "{19F68549-CA8A-4706-A4EF-481DBC95E12C}"
                    )
                    IMFCapturePhotoConfirmation._iid_ = IID_IMFCapturePhotoConfirmation


                    IMFCapturePhotoConfirmation._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetPhotoConfirmationCallback')],
                            HRESULT,
                            'SetPhotoConfirmationCallback',
                            (
                                ['in'],
                                POINTER(IMFAsyncCallback),
                               'pNotificationCallback'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetPixelFormat')],
                            HRESULT,
                            'SetPixelFormat',
                            (['in'], GUID, 'subtype'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPixelFormat')],
                            HRESULT,
                            'GetPixelFormat',
                            (['out'], POINTER(GUID), 'subtype'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFCapturePhotoConfirmation_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0094
            # [local]        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            if WINVER >= _WIN32_WINNT_WIN8:
                if not defined(__IMFPMPHostApp_INTERFACE_DEFINED__):
                    # interface IMFPMPHostApp
                    # [uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFPMPHostApp = MIDL_INTERFACE(
                            "{84D2054A-3AA1-4728-A3B0-440A418CF49C}"
                        )
                        IMFPMPHostApp._iid_ = IID_IMFPMPHostApp


                        IMFPMPHostApp._methods_ = [
                            COMMETHOD(
                                [helpstring('Method LockProcess')],
                                HRESULT,
                                'LockProcess',
                            ),
                            COMMETHOD(
                                [helpstring('Method UnlockProcess')],
                                HRESULT,
                                'UnlockProcess',
                            ),
                            COMMETHOD(
                                [helpstring('Method ActivateClassById')],
                                HRESULT,
                                'ActivateClassById',
                                (['in'], LPCWSTR, 'id'),
                                (
                                    ['unique', 'in'],
                                    POINTER(IStream),
                                   'pStream'
                                ),
                                (['in'], REFIID, 'riid'),
                                (
                                    ['iid_is', 'out'],
                                    POINTER(POINTER(VOID)),
                                   'ppv'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFPMPHostApp_INTERFACE_DEFINED__

                if not defined(__IMFPMPClientApp_INTERFACE_DEFINED__):
                    # interface IMFPMPClientApp
                    # [local][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFPMPClientApp = MIDL_INTERFACE(
                            "{C004F646-BE2C-48F3-93A2-A0983EBA1108}"
                        )
                        IMFPMPClientApp._iid_ = IID_IMFPMPClientApp


                        IMFPMPClientApp._methods_ = [
                            COMMETHOD(
                                [helpstring('Method SetPMPHost')],
                                HRESULT,
                                'SetPMPHost',
                                (['in'], POINTER(IMFPMPHostApp), 'pPMPHost'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFPMPClientApp_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfidl_0000_0096
                # [local]            # END IF
            if WINVER >= _WIN32_WINNT_WINBLUE:
                if not defined(__IMFMediaStreamSourceSampleRequest_INTERFACE_DEFINED__):
                    # interface IMFMediaStreamSourceSampleRequest
                    # [unique][uuid][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IMFMediaStreamSourceSampleRequest = MIDL_INTERFACE(
                            "{380B9AF9-A85B-4E78-A2AF-EA5CE645C6B4}"
                        )
                        IMFMediaStreamSourceSampleRequest._iid_ = IID_IMFMediaStreamSourceSampleRequest


                        IMFMediaStreamSourceSampleRequest._methods_ = [
                            COMMETHOD(
                                [helpstring('Method SetSample')],
                                HRESULT,
                                'SetSample',
                                (['in'], POINTER(IMFSample), 'value'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IMFMediaStreamSourceSampleRequest_INTERFACE_DEFINED__

                # interface __MIDL_itf_mfidl_0000_0097
                # [local]            # END IF
            if not defined(__IMFTrackedSample_INTERFACE_DEFINED__):
                # interface IMFTrackedSample
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFTrackedSample = MIDL_INTERFACE(
                        "{245BF8E9-0755-40F7-88A5-AE0F18D55E17}"
                    )
                    IMFTrackedSample._iid_ = IID_IMFTrackedSample


                    IMFTrackedSample._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetAllocator')],
                            HRESULT,
                            'SetAllocator',
                            (
                                ['in'],
                                POINTER(IMFAsyncCallback),
                               'pSampleAllocator'
                            ),
                            (
                                ['unique', 'in'],
                                POINTER(comtypes.IUnknown),
                               'pUnkState'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFTrackedSample_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0098
            # [local]
            mfplat = ctypes.windll.MFPLAT


            # STDAPI MFCreateTrackedSample(
            # _Outptr_ IMFTrackedSample** ppMFSample);
            MFCreateTrackedSample = mfplat.MFCreateTrackedSample
            MFCreateTrackedSample.restype = STDAPI


        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            mfplat = ctypes.windll.MFPLAT


            # STDAPI MFCreateMFByteStreamOnStream(
            # IStream*        pStream,
            # _Outptr_ IMFByteStream** ppByteStream);
            MFCreateMFByteStreamOnStream = mfplat.MFCreateMFByteStreamOnStream
            MFCreateMFByteStreamOnStream.restype = STDAPI


            # STDAPI MFCreateStreamOnMFByteStream(
            # _In_ IMFByteStream* pByteStream,
            # _Outptr_ IStream** ppStream);
            MFCreateStreamOnMFByteStream = mfplat.MFCreateStreamOnMFByteStream
            MFCreateStreamOnMFByteStream.restype = STDAPI

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            mfplat = ctypes.windll.MFPLAT


            # STDAPI MFCreateMFByteStreamOnStreamEx(
            # _In_ IUnknown* punkStream,
            # _Outptr_ IMFByteStream** ppByteStream );
            MFCreateMFByteStreamOnStreamEx = (
                mfplat.MFCreateMFByteStreamOnStreamEx
            )
            MFCreateMFByteStreamOnStreamEx.restype = STDAPI


            # STDAPI MFCreateStreamOnMFByteStreamEx(
            # _In_ IMFByteStream* pByteStream,
            # _In_ REFIID riid,
            # _Outptr_ VOID **ppv );
            MFCreateStreamOnMFByteStreamEx = (
                mfplat.MFCreateStreamOnMFByteStreamEx
            )
            MFCreateStreamOnMFByteStreamEx.restype = STDAPI


            # STDAPI MFCreateMediaTypeFromProperties(
            # _In_ IUnknown* punkStream,
            # _Outptr_ IMFMediaType** ppMediaType );
            MFCreateMediaTypeFromProperties = (
                mfplat.MFCreateMediaTypeFromProperties
            )
            MFCreateMediaTypeFromProperties.restype = STDAPI


            # STDAPI MFCreatePropertiesFromMediaType(
            # _In_ IMFMediaType* pMediaType,
            # _In_ REFIID riid,
            # _Outptr_ VOID **ppv );
            MFCreatePropertiesFromMediaType = (
                mfplat.MFCreatePropertiesFromMediaType
            )
            MFCreatePropertiesFromMediaType.restype = STDAPI


            if WINVER >= _WIN32_WINNT_WINBLUE:
                MF_WRAPPED_BUFFER_SERVICE = DEFINE_GUID(
                    0xAB544072,
                    0xC269,
                    0x4EBC,
                    0xA5,
                    0x52,
                    0x1C,
                    0x3B,
                    0x32,
                    0xBE,
                    0xD5,
                    0xCA
                )
                MF_WRAPPED_SAMPLE_SERVICE = EXTERN_GUID(
                    0x31F52BF2,
                    0xD03E,
                    0x4048,
                    0x80,
                    0xD0,
                    0x9C,
                    0x10,
                    0x46,
                    0xD8,
                    0x7C,
                    0x61
                )
            # END IF   (WINVER >= _WIN32_WINNT_WINBLUE)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            MF_WRAPPED_OBJECT = EXTERN_GUID(
                0x2B182C4C,
                0xD6AC,
                0x49F4,
                0x89,
                0x15,
                0xF7,
                0x18,
                0x87,
                0xDB,
                0x70,
                0xCD
            )
            CLSID_HttpSchemePlugin = EXTERN_GUID(
                0x44CB442B,
                0x9DA9,
                0x49DF,
                0xB3,
                0xFD,
                0x2,
                0x37,
                0x77,
                0xB1,
                0x6E,
                0x50
            )
            CLSID_UrlmonSchemePlugin = EXTERN_GUID(
                0x9EC4B4F9,
                0x3029,
                0x45AD,
                0x94,
                0x7B,
                0x34,
                0x4D,
                0xE2,
                0xA2,
                0x49,
                0xE2
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            CLSID_NetSchemePlugin = EXTERN_GUID(
                0xE9F4EBAB,
                0xD97B,
                0x463E,
                0xA2,
                0xB1,
                0xC5,
                0x4E,
                0xE3,
                0xF9,
                0x41,
                0x4D
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            mf = ctypes.windll.MF


            # STDAPI MFEnumDeviceSources(
            # _In_                IMFAttributes*                      pAttributes,
            # _Outptr_result_buffer_(*pcSourceActivate) IMFActivate***    pppSourceActivate,
            # _Out_               UINT32*                             pcSourceActivate
            # );
            MFEnumDeviceSources = mf.MFEnumDeviceSources
            MFEnumDeviceSources.restype = STDAPI


            # STDAPI MFCreateDeviceSource(
            # _In_  IMFAttributes*   pAttributes,
            # _Outptr_ IMFMediaSource** ppSource
            # );
            MFCreateDeviceSource = mf.MFCreateDeviceSource
            MFCreateDeviceSource.restype = STDAPI


            # STDAPI MFCreateDeviceSourceActivate(
            # _In_  IMFAttributes*   pAttributes,
            # _Outptr_ IMFActivate**   ppActivate
            # );
            MFCreateDeviceSourceActivate = mf.MFCreateDeviceSourceActivate
            MFCreateDeviceSourceActivate.restype = STDAPI


            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE = EXTERN_GUID(
                0xC60AC5FE,
                0x252A,
                0x478F,
                0xA0,
                0xEF,
                0xBC,
                0x8F,
                0xA5,
                0xF7,
                0xCA,
                0xD3
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_HW_SOURCE = EXTERN_GUID(
                0xDE7046BA,
                0x54D6,
                0x4487,
                0xA2,
                0xA4,
                0xEC,
                0x7C,
                0xD,
                0x1B,
                0xD1,
                0x63
            )
            MF_DEVSOURCE_ATTRIBUTE_FRIENDLY_NAME = EXTERN_GUID(
                0x60D0E559,
                0x52F8,
                0x4FA2,
                0xBB,
                0xCE,
                0xAC,
                0xDB,
                0x34,
                0xA8,
                0xEC,
                0x1
            )
            MF_DEVSOURCE_ATTRIBUTE_MEDIA_TYPE = EXTERN_GUID(
                0x56A819CA,
                0xC78,
                0x4DE4,
                0xA0,
                0xA7,
                0x3D,
                0xDA,
                0xBA,
                0xF,
                0x24,
                0xD4
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_CATEGORY = EXTERN_GUID(
                0x77F0AE69,
                0xC3BD,
                0x4509,
                0x94,
                0x1D,
                0x46,
                0x7E,
                0x4D,
                0x24,
                0x89,
                0x9E
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_SYMBOLIC_LINK = EXTERN_GUID(
                0x58F0AAD8,
                0x22BF,
                0x4F8A,
                0xBB,
                0x3D,
                0xD2,
                0xC4,
                0x97,
                0x8C,
                0x6E,
                0x2F
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_SYMBOLIC_LINK = EXTERN_GUID(
                0x98D24B5E,
                0x5930,
                0x4614,
                0xB5,
                0xA1,
                0xF6,
                0x0,
                0xF9,
                0x35,
                0x5A,
                0x78
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_MAX_BUFFERS = EXTERN_GUID(
                0x7DD9B730,
                0x4F2D,
                0x41D5,
                0x8F,
                0x95,
                0xC,
                0xC9,
                0xA9,
                0x12,
                0xBA,
                0x26
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_ENDPOINT_ID = EXTERN_GUID(
                0x30DA9258,
                0xFEB9,
                0x47A7,
                0xA4,
                0x53,
                0x76,
                0x3A,
                0x7A,
                0x8E,
                0x1C,
                0x5F
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_ROLE = EXTERN_GUID(
                0xBC9D118E,
                0x8C67,
                0x4A18,
                0x85,
                0xD4,
                0x12,
                0xD3,
                0x0,
                0x40,
                0x5,
                0x52
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_PROVIDER_DEVICE_ID = EXTERN_GUID(
                0x36689D42,
                0xA06C,
                0x40AE,
                0x84,
                0xCF,
                0xF5,
                0xA0,
                0x34,
                0x6,
                0x7C,
                0xC4
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_AUDCAP_GUID = EXTERN_GUID(
                0x14DD9A1C,
                0x7CFF,
                0x41BE,
                0xB1,
                0xB9,
                0xBA,
                0x1A,
                0xC6,
                0xEC,
                0xB5,
                0x71
            )
            MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_GUID = EXTERN_GUID(
                0x8AC3587A,
                0x4AE7,
                0x42D8,
                0x99,
                0xE0,
                0x0A,
                0x60,
                0x13,
                0xEE,
                0xF9,
                0x0F
            )
            MF_DEVICESTREAM_IMAGE_STREAM = EXTERN_GUID(
                0xA7FFB865,
                0xE7B2,
                0x43B0,
                0x9F,
                0x6F,
                0x9A,
                0xF2,
                0xA0,
                0xE5,
                0xF,
                0xC0
            )
            MF_DEVICESTREAM_INDEPENDENT_IMAGE_STREAM = EXTERN_GUID(
                0x3EEEC7E,
                0xD605,
                0x4576,
                0x8B,
                0x29,
                0x65,
                0x80,
                0xB4,
                0x90,
                0xD7,
                0xD3
            )
            MF_DEVICESTREAM_STREAM_ID = EXTERN_GUID(
                0x11BD5120,
                0xD124,
                0x446B,
                0x88,
                0xE6,
                0x17,
                0x6,
                0x2,
                0x57,
                0xFF,
                0xF9
            )
            MF_DEVICESTREAM_STREAM_CATEGORY = EXTERN_GUID(
                0x2939E7B8,
                0xA62E,
                0x4579,
                0xB6,
                0x74,
                0xD4,
                0x7,
                0x3D,
                0xFA,
                0xBB,
                0xBA
            )
            MF_DEVICESTREAM_FRAMESERVER_SHARED = EXTERN_GUID(
                0x1CB378E9,
                0xB279,
                0x41D4,
                0xAF,
                0x97,
                0x34,
                0xA2,
                0x43,
                0xE6,
                0x83,
                0x20
            )
            MF_DEVICESTREAM_TRANSFORM_STREAM_ID = EXTERN_GUID(
                0xE63937B7,
                0xDAAF,
                0x4D49,
                0x81,
                0x5F,
                0xD8,
                0x26,
                0xF8,
                0xAD,
                0x31,
                0xE7
            )
            MF_DEVICESTREAM_EXTENSION_PLUGIN_CLSID = EXTERN_GUID(
                0x048E6558,
                0x60C4,
                0x4173,
                0xBD,
                0x5B,
                0x6A,
                0x3C,
                0xA2,
                0x89,
                0x6A,
                0xEE
            )
            MF_DEVICEMFT_EXTENSION_PLUGIN_CLSID = EXTERN_GUID(
                0x844DBAE,
                0x34FA,
                0x48A0,
                0xA7,
                0x83,
                0x8E,
                0x69,
                0x6F,
                0xB1,
                0xC9,
                0xA8
            )
            MF_DEVICESTREAM_EXTENSION_PLUGIN_CONNECTION_POINT = EXTERN_GUID(
                0x37F9375C,
                0xE664,
                0x4EA4,
                0xAA,
                0xE4,
                0xCB,
                0x6D,
                0x1D,
                0xAC,
                0xA1,
                0xF4
            )
            MF_DEVICESTREAM_TAKEPHOTO_TRIGGER = EXTERN_GUID(
                0x1D180E34,
                0x538C,
                0x4FBB,
                0xA7,
                0x5A,
                0x85,
                0x9A,
                0xF7,
                0xD2,
                0x61,
                0xA6
            )
            MF_DEVICESTREAM_MAX_FRAME_BUFFERS = EXTERN_GUID(
                0x1684CEBE,
                0x3175,
                0x4985,
                0x88,
                0x2C,
                0x0E,
                0xFD,
                0x3E,
                0x8A,
                0xC1,
                0x1E
            )
            MF_DEVICEMFT_CONNECTED_FILTER_KSCONTROL = EXTERN_GUID(
                0x6A2C4FA6,
                0xD179,
                0x41CD,
                0x95,
                0x23,
                0x82,
                0x23,
                0x71,
                0xEA,
                0x40,
                0xE5
            )
            MF_DEVICEMFT_CONNECTED_PIN_KSCONTROL = EXTERN_GUID(
                0xE63310F7,
                0xB244,
                0x4EF8,
                0x9A,
                0x7D,
                0x24,
                0xC7,
                0x4E,
                0x32,
                0xEB,
                0xD0
            )
            MF_DEVICE_THERMAL_STATE_CHANGED = EXTERN_GUID(
                0x70CCD0AF,
                0xFC9F,
                0x4DEB,
                0xA8,
                0x75,
                0x9F,
                0xEC,
                0xD1,
                0x6C,
                0x5B,
                0xD4
            )
            MFSampleExtension_DeviceTimestamp = EXTERN_GUID(
                0x8F3E35E7,
                0x2DCD,
                0x4887,
                0x86,
                0x22,
                0x2A,
                0x58,
                0xBA,
                0xA6,
                0x52,
                0xB0
            )
            MFSampleExtension_Spatial_CameraViewTransform = EXTERN_GUID(
                0x4E251FA4,
                0x830F,
                0x4770,
                0x85,
                0x9A,
                0x4B,
                0x8D,
                0x99,
                0xAA,
                0x80,
                0x9B
            )
            MFSampleExtension_Spatial_CameraCoordinateSystem = EXTERN_GUID(
                0x9D13C82F,
                0x2199,
                0x4E67,
                0x91,
                0xCD,
                0xD1,
                0xA4,
                0x18,
                0x1F,
                0x25,
                0x34
            )
            MFSampleExtension_Spatial_CameraProjectionTransform = EXTERN_GUID(
                0x47F9FCB5,
                0x2A02,
                0x4F26,
                0xA4,
                0x77,
                0x79,
                0x2F,
                0xDF,
                0x95,
                0x88,
                0x6A
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFProtectedEnvironmentAccess_INTERFACE_DEFINED__):
            # interface IMFProtectedEnvironmentAccess
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFProtectedEnvironmentAccess = MIDL_INTERFACE(
                    "{EF5DC845-F0D9-4EC9-B00C-CB5183D38434}"
                )
                IMFProtectedEnvironmentAccess._iid_ = IID_IMFProtectedEnvironmentAccess


                IMFProtectedEnvironmentAccess._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Call')],
                        HRESULT,
                        'Call',
                        (['in'], UINT32, 'inputLength'),
                        (['in'], POINTER(BYTE), 'input'),
                        (['in'], UINT32, 'outputLength'),
                        (['out'], POINTER(BYTE), 'output'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReadGRL')],
                        HRESULT,
                        'ReadGRL',
                        (['out'], POINTER(UINT32), 'outputLength'),
                        (['out'], POINTER(POINTER(BYTE)), 'output'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFProtectedEnvironmentAccess_INTERFACE_DEFINED__

        if not defined(__IMFSignedLibrary_INTERFACE_DEFINED__):
            # interface IMFSignedLibrary
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSignedLibrary = MIDL_INTERFACE(
                    "{4A724BCA-FF6A-4C07-8E0D-7A358421CF06}"
                )
                IMFSignedLibrary._iid_ = IID_IMFSignedLibrary


                IMFSignedLibrary._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetProcedureAddress')],
                        HRESULT,
                        'GetProcedureAddress',
                        (['in'], LPCSTR, 'name'),
                        (['out'], POINTER(PVOID), 'address'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSignedLibrary_INTERFACE_DEFINED__

        if not defined(__IMFSystemId_INTERFACE_DEFINED__):
            # interface IMFSystemId
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSystemId = MIDL_INTERFACE(
                    "{FFF4AF3A-1FC1-4EF9-A29B-D26C49E2F31A}"
                )
                IMFSystemId._iid_ = IID_IMFSystemId


                IMFSystemId._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetData')],
                        HRESULT,
                        'GetData',
                        (['out'], POINTER(UINT32), 'size'),
                        (['out'], POINTER(POINTER(BYTE)), 'data'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Setup')],
                        HRESULT,
                        'Setup',
                        ([], UINT32, 'stage'),
                        ([], UINT32, 'cbIn'),
                        (['in'], POINTER(BYTE), 'pbIn'),
                        (['out'], POINTER(UINT32), 'pcbOut'),
                        (['out'], POINTER(POINTER(BYTE)), 'ppbOut'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSystemId_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0101
        # [local]
        mf = ctypes.windll.MF


        # STDAPI MFCreateProtectedEnvironmentAccess(
        # _Outptr_ IMFProtectedEnvironmentAccess**   ppAccess
        # );
        MFCreateProtectedEnvironmentAccess = (
            mf.MFCreateProtectedEnvironmentAccess
        )
        MFCreateProtectedEnvironmentAccess.restype = STDAPI


        # STDAPI MFLoadSignedLibrary(
        # _In_ LPCWSTR pszName,
        # _Outptr_ IMFSignedLibrary**   ppLib
        # );
        MFLoadSignedLibrary = mf.MFLoadSignedLibrary
        MFLoadSignedLibrary.restype = STDAPI


        # STDAPI MFGetSystemId(
        # _Outptr_ IMFSystemId** ppId
        # );
        MFGetSystemId = mf.MFGetSystemId
        MFGetSystemId.restype = STDAPI


        # STDAPI MFGetLocalId(
        # _In_reads_bytes_(size) BYTE *verifier,
        # _In_ UINT32 size,
        # _Outptr_ LPWSTR *id
        # );
        MFGetLocalId = mf.MFGetLocalId
        MFGetLocalId.restype = STDAPI


        # {40871C59-AB40-471F-8DC3-1F259D862479}
        CLSID_MPEG2ByteStreamPlugin = DEFINE_GUID(
            0x40871C59,
            0xAB40,
            0x471F,
            0x8D,
            0xC3,
            0x1F,
            0x25,
            0x9D,
            0x86,
            0x24,
            0x79
        )

        # {f09992f7-9fba-4c4a-a37f-8c47b4e1dfe7}
        MF_MEDIASOURCE_SERVICE = EXTERN_GUID(
            0xF09992F7,
            0x9FBA,
            0x4C4A,
            0xA3,
            0x7F,
            0x8C,
            0x47,
            0xB4,
            0xE1,
            0xDF,
            0xE7
        )

        # {014A5031-2F05-4C6A-9F9C-7D0DC4EDA5F4}
        MF_ACCESS_CONTROLLED_MEDIASOURCE_SERVICE = EXTERN_GUID(
            0x14A5031,
            0x2F05,
            0x4C6A,
            0x9F,
            0x9C,
            0x7D,
            0xD,
            0xC4,
            0xED,
            0xA5,
            0xF4
        )

        _MFCONTENTPROTECTIONDEVICE_INPUT_DATA._fields_ = [
            ('HWProtectionFunctionID', DWORD),
            ('PrivateDataByteCount', DWORD),
            ('HWProtectionDataByteCount', DWORD),
            ('Reserved', DWORD),
            ('InputData', BYTE * 4),
        ]

        _MFCONTENTPROTECTIONDEVICE_OUTPUT_DATA._fields_ = [
            ('PrivateDataByteCount', DWORD),
            ('MaxHWProtectionDataByteCount', DWORD),
            ('HWProtectionDataByteCount', DWORD),
            ('Status', HRESULT),
            ('TransportTimeInHundredsOfNanoseconds', LONGLONG),
            ('ExecutionTimeInHundredsOfNanoseconds', LONGLONG),
            ('OutputData', BYTE * 4),
        ]

        _MFCONTENTPROTECTIONDEVICE_REALTIMECLIENT_DATA._fields_ = [
            ('TaskIndex', DWORD),
            ('ClassName', WCHAR * MAX_PATH),
            ('BasePriority', LONG),
        ]
        if not defined(__IMFContentProtectionDevice_INTERFACE_DEFINED__):
            # interface IMFContentProtectionDevice
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFContentProtectionDevice = MIDL_INTERFACE(
                    "{E6257174-A060-4C9A-A088-3B1B471CAD28}"
                )
                IMFContentProtectionDevice._iid_ = IID_IMFContentProtectionDevice


                IMFContentProtectionDevice._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InvokeFunction')],
                        HRESULT,
                        'InvokeFunction',
                        (['in'], DWORD, 'FunctionId'),
                        (['in'], DWORD, 'InputBufferByteCount'),
                        (['in'], POINTER(BYTE), 'InputBuffer'),
                        (
                            ['out', 'in'],
                            POINTER(DWORD),
                           'OutputBufferByteCount'
                        ),
                        (['out'], POINTER(BYTE), 'OutputBuffer'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPrivateDataByteCount')],
                        HRESULT,
                        'GetPrivateDataByteCount',
                        (['out'], POINTER(DWORD), 'PrivateInputByteCount'),
                        (['out'], POINTER(DWORD), 'PrivateOutputByteCount'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFContentProtectionDevice_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0102
        # [local]
        mfplat = ctypes.windll.MFPLAT


        # STDAPI MFCreateContentProtectionDevice(
        # _In_ REFGUID ProtectionSystemId,
        # _Outptr_ IMFContentProtectionDevice **ContentProtectionDevice);
        MFCreateContentProtectionDevice = (
            mfplat.MFCreateContentProtectionDevice
        )
        MFCreateContentProtectionDevice.restype = STDAPI


        # STDAPI MFIsContentProtectionDeviceSupported(
        # _In_ REFGUID ProtectionSystemId,
        # _Out_ BOOL *isSupported);
        MFIsContentProtectionDeviceSupported = (
            mfplat.MFIsContentProtectionDeviceSupported
        )
        MFIsContentProtectionDeviceSupported.restype = STDAPI


        if not defined(__IMFContentDecryptorContext_INTERFACE_DEFINED__):
            # interface IMFContentDecryptorContext
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFContentDecryptorContext = MIDL_INTERFACE(
                    "{7EC4B1BD-43FB-4763-85D2-64FCB5C5F4CB}"
                )
                IMFContentDecryptorContext._iid_ = IID_IMFContentDecryptorContext


                IMFContentDecryptorContext._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InitializeHardwareKey')],
                        HRESULT,
                        'InitializeHardwareKey',
                        (['in'], UINT, 'InputPrivateDataByteCount'),
                        (['in'], POINTER(VOID), 'InputPrivateData'),
                        (['out'], POINTER(UINT64), 'OutputPrivateData'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFContentDecryptorContext_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0103
        # [local]
        MF_CONTENT_DECRYPTOR_SERVICE = EXTERN_GUID(
            0x68A72927,
            0xFC7B,
            0x44EE,
            0x85,
            0xF4,
            0x7C,
            0x51,
            0xBD,
            0x55,
            0xA6,
            0x59
        )
        MF_CONTENT_PROTECTION_DEVICE_SERVICE = EXTERN_GUID(
            0xFF58436F,
            0x76A0,
            0x41FE,
            0xB5,
            0x66,
            0x10,
            0xCC,
            0x53,
            0x96,
            0x2E,
            0xDD
        )


        # STDAPI MFCreateContentDecryptorContext(
        # _In_ REFGUID guidMediaProtectionSystemId,
        # _In_opt_ IMFDXGIDeviceManager *pD3DManager,
        # _In_ IMFContentProtectionDevice *pContentProtectionDevice,
        # _Outptr_ IMFContentDecryptorContext **ppContentDecryptorContext);
        MFCreateContentDecryptorContext = (
            mfplat.MFCreateContentDecryptorContext
        )
        MFCreateContentDecryptorContext.restype = STDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            MF_SD_AUDIO_ENCODER_DELAY = EXTERN_GUID(
                0x8E85422C,
                0x73DE,
                0x403F,
                0x9A,
                0x35,
                0x55,
                0x0A,
                0xD6,
                0xE8,
                0xB9,
                0x51
            )
            MF_SD_AUDIO_ENCODER_PADDING = EXTERN_GUID(
                0x529C7F2C,
                0xAC4B,
                0x4E3F,
                0xBF,
                0xC3,
                0x09,
                0x02,
                0x19,
                0x49,
                0x82,
                0xCB
            )
            CLSID_MSH264DecoderMFT = EXTERN_GUID(
                0x62CE7E72,
                0x4C71,
                0x4D20,
                0xB1,
                0x5D,
                0x45,
                0x28,
                0x31,
                0xA8,
                0x7D,
                0x9D
            )
            CLSID_MSH264EncoderMFT = EXTERN_GUID(
                0x6CA50344,
                0x051A,
                0x4DED,
                0x97,
                0x79,
                0xA4,
                0x33,
                0x05,
                0x16,
                0x5E,
                0x35
            )
            CLSID_MSDDPlusDecMFT = EXTERN_GUID(
                0x177C0AFE,
                0x900B,
                0x48D4,
                0x9E,
                0x4C,
                0x57,
                0xAD,
                0xD2,
                0x50,
                0xB3,
                0xD4
            )
            CLSID_MP3DecMediaObject = EXTERN_GUID(
                0xBBEEA841,
                0x0A63,
                0x4F52,
                0xA7,
                0xAB,
                0xA9,
                0xB3,
                0xA8,
                0x4E,
                0xD3,
                0x8A
            )
            CLSID_MSAACDecMFT = EXTERN_GUID(
                0x32D186A7,
                0x218F,
                0x4C75,
                0x88,
                0x76,
                0xDD,
                0x77,
                0x27,
                0x3A,
                0x89,
                0x99
            )
            CLSID_MSH265DecoderMFT = EXTERN_GUID(
                0x420A51A3,
                0xD605,
                0x430C,
                0xB4,
                0xFC,
                0x45,
                0x27,
                0x4F,
                0xA6,
                0xC5,
                0x62
            )
            CLSID_WMVDecoderMFT = EXTERN_GUID(
                0x82D353DF,
                0x90BD,
                0x4382,
                0x8B,
                0xC2,
                0x3F,
                0x61,
                0x92,
                0xB7,
                0x6E,
                0x34
            )
            CLSID_WMADecMediaObject = EXTERN_GUID(
                0x2EEB4ADF,
                0x4578,
                0x4D10,
                0xBC,
                0xA7,
                0xBB,
                0x95,
                0x5F,
                0x56,
                0x32,
                0x0A
            )
            CLSID_MSMPEGAudDecMFT = EXTERN_GUID(
                0x70707B39,
                0xB2CA,
                0x4015,
                0xAB,
                0xEA,
                0xF8,
                0x44,
                0x7D,
                0x22,
                0xD8,
                0x8B
            )
            CLSID_MSMPEGDecoderMFT = EXTERN_GUID(
                0x2D709E52,
                0x123F,
                0x49B5,
                0x9C,
                0xBC,
                0x9A,
                0xF5,
                0xCD,
                0xE2,
                0x8F,
                0xB9
            )
            CLSID_AudioResamplerMediaObject = EXTERN_GUID(
                0xF447B69E,
                0x1884,
                0x4A7E,
                0x80,
                0x55,
                0x34,
                0x6F,
                0x74,
                0xD6,
                0xED,
                0xB3
            )
            CLSID_MSVPxDecoder = EXTERN_GUID(
                0xE3AAF548,
                0xC9A4,
                0x4C6E,
                0x23,
                0x4D,
                0x5A,
                0xDA,
                0x37,
                0x4B,
                0x00,
                0x00
            )
            CLSID_MSOpusDecoder = EXTERN_GUID(
                0x63E17C10,
                0x2D43,
                0x4C42,
                0x8F,
                0xE3,
                0x8D,
                0x8B,
                0x63,
                0xE4,
                0x6A,
                0x6A
            )
            CLSID_VideoProcessorMFT = EXTERN_GUID(
                0x88753B26,
                0x5B24,
                0x49BD,
                0xB2,
                0xE7,
                0xC,
                0x44,
                0x5C,
                0x78,
                0xC9,
                0x82
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        class MF_MEDIAKEYSESSION_TYPE(ENUM):
            MF_MEDIAKEYSESSION_TYPE_TEMPORARY = 0
            MF_MEDIAKEYSESSION_TYPE_PERSISTENT_LICENSE = (
                MF_MEDIAKEYSESSION_TYPE_TEMPORARY + 1 )
            )
            MF_MEDIAKEYSESSION_TYPE_PERSISTENT_RELEASE_MESSAGE = (
                MF_MEDIAKEYSESSION_TYPE_PERSISTENT_LICENSE + 1 )
            )
            MF_MEDIAKEYSESSION_TYPE_PERSISTENT_USAGE_RECORD = (
                MF_MEDIAKEYSESSION_TYPE_PERSISTENT_RELEASE_MESSAGE + 1 )
            )


        class MF_MEDIAKEY_STATUS(ENUM):
            MF_MEDIAKEY_STATUS_USABLE = 0
            MF_MEDIAKEY_STATUS_EXPIRED = MF_MEDIAKEY_STATUS_USABLE + 1 )
            MF_MEDIAKEY_STATUS_OUTPUT_DOWNSCALED = (
                MF_MEDIAKEY_STATUS_EXPIRED + 1 )
            )
            MF_MEDIAKEY_STATUS_OUTPUT_NOT_ALLOWED = (
                MF_MEDIAKEY_STATUS_OUTPUT_DOWNSCALED + 1 )
            )
            MF_MEDIAKEY_STATUS_STATUS_PENDING = (
                MF_MEDIAKEY_STATUS_OUTPUT_NOT_ALLOWED + 1 )
            )
            MF_MEDIAKEY_STATUS_INTERNAL_ERROR = (
                MF_MEDIAKEY_STATUS_STATUS_PENDING + 1 )
            )
            MF_MEDIAKEY_STATUS_RELEASED = (
                MF_MEDIAKEY_STATUS_INTERNAL_ERROR + 1 )
            )
            MF_MEDIAKEY_STATUS_OUTPUT_RESTRICTED = (
                MF_MEDIAKEY_STATUS_RELEASED + 1 )
            )
        MFMediaKeyStatus._fields_ = [
            ('pbKeyId', POINTER(BYTE)),
            ('cbKeyId', UINT),
            ('eMediaKeyStatus', MF_MEDIAKEY_STATUS),
        ]


        class MF_MEDIAKEYSESSION_MESSAGETYPE(ENUM):
            MF_MEDIAKEYSESSION_MESSAGETYPE_LICENSE_REQUEST = 0
            MF_MEDIAKEYSESSION_MESSAGETYPE_LICENSE_RENEWAL = 1
            MF_MEDIAKEYSESSION_MESSAGETYPE_LICENSE_RELEASE = 2
            MF_MEDIAKEYSESSION_MESSAGETYPE_INDIVIDUALIZATION_REQUEST = 3


        class _MF_CROSS_ORIGIN_POLICY(ENUM):
            MF_CROSS_ORIGIN_POLICY_NONE = 0
            MF_CROSS_ORIGIN_POLICY_ANONYMOUS = 1
            MF_CROSS_ORIGIN_POLICY_USE_CREDENTIALS = 2

        MF_CROSS_ORIGIN_POLICY = _MF_CROSS_ORIGIN_POLICY
        if not defined(__IMFNetCrossOriginSupport_INTERFACE_DEFINED__):
            # interface IMFNetCrossOriginSupport
            # [local][unique][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFNetCrossOriginSupport = MIDL_INTERFACE(
                    "{BC2B7D44-A72D-49D5-8376-1480DEE58B22}"
                )
                IMFNetCrossOriginSupport._iid_ = IID_IMFNetCrossOriginSupport


                IMFNetCrossOriginSupport._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCrossOriginPolicy')],
                        HRESULT,
                        'GetCrossOriginPolicy',
                        (['out'], POINTER(MF_CROSS_ORIGIN_POLICY), 'pPolicy'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSourceOrigin')],
                        HRESULT,
                        'GetSourceOrigin',
                        (['out'], POINTER(LPWSTR), 'wszSourceOrigin'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsSameOrigin')],
                        HRESULT,
                        'IsSameOrigin',
                        (['in'], LPCWSTR, 'wszURL'),
                        (['out'], POINTER(BOOL), 'pfIsSameOrigin'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFNetCrossOriginSupport_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0104
        # [local]
        MFNETSOURCE_CROSS_ORIGIN_SUPPORT = EXTERN_GUID(
            0x9842207C,
            0xB02C,
            0x4271,
            0xA2,
            0xFC,
            0x72,
            0xE4,
            0x93,
            0x8,
            0xE5,
            0xC2
        )
        if not defined(__IMFHttpDownloadRequest_INTERFACE_DEFINED__):
            # interface IMFHttpDownloadRequest
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFHttpDownloadRequest = MIDL_INTERFACE(
                    "{F779FDDF-26E7-4270-8A8B-B983D1859DE0}"
                )
                IMFHttpDownloadRequest._iid_ = IID_IMFHttpDownloadRequest


                IMFHttpDownloadRequest._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AddHeader')],
                        HRESULT,
                        'AddHeader',
                        (['in'], LPCWSTR, 'szHeader'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginSendRequest')],
                        HRESULT,
                        'BeginSendRequest',
                        (['in'], POINTER(BYTE), 'pbPayload'),
                        (['in'], ULONG, 'cbPayload'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndSendRequest')],
                        HRESULT,
                        'EndSendRequest',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginReceiveResponse')],
                        HRESULT,
                        'BeginReceiveResponse',
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndReceiveResponse')],
                        HRESULT,
                        'EndReceiveResponse',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginReadPayload')],
                        HRESULT,
                        'BeginReadPayload',
                        (['out'], POINTER(BYTE), 'pb'),
                        (['in'], ULONG, 'cb'),
                        (['in'], POINTER(IMFAsyncCallback), 'pCallback'),
                        (['in'], POINTER(comtypes.IUnknown), 'punkState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EndReadPayload')],
                        HRESULT,
                        'EndReadPayload',
                        (['in'], POINTER(IMFAsyncResult), 'pResult'),
                        (['out'], POINTER(QWORD), 'pqwOffset'),
                        (['out'], POINTER(ULONG), 'pcbRead'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueryHeader')],
                        HRESULT,
                        'QueryHeader',
                        (['in'], LPCWSTR, 'szHeaderName'),
                        (['in'], DWORD, 'dwIndex'),
                        (['out'], POINTER(LPWSTR), 'ppszHeaderValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetURL')],
                        HRESULT,
                        'GetURL',
                        (['out'], POINTER(LPWSTR), 'ppszURL'),
                    ),
                    COMMETHOD(
                        [helpstring('Method HasNullSourceOrigin')],
                        HRESULT,
                        'HasNullSourceOrigin',
                        (['out'], POINTER(BOOL), 'pfNullSourceOrigin'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTimeSeekResult')],
                        HRESULT,
                        'GetTimeSeekResult',
                        (['out'], POINTER(QWORD), 'pqwStartTime'),
                        (['out'], POINTER(QWORD), 'pqwStopTime'),
                        (['out'], POINTER(QWORD), 'pqwDuration'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetHttpStatus')],
                        HRESULT,
                        'GetHttpStatus',
                        (['out'], POINTER(DWORD), 'pdwHttpStatus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAtEndOfPayload')],
                        HRESULT,
                        'GetAtEndOfPayload',
                        (['out'], POINTER(BOOL), 'pfAtEndOfPayload'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTotalLength')],
                        HRESULT,
                        'GetTotalLength',
                        (['out'], POINTER(QWORD), 'pqwTotalLength'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRangeEndOffset')],
                        HRESULT,
                        'GetRangeEndOffset',
                        (['out'], POINTER(QWORD), 'pqwRangeEnd'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFHttpDownloadRequest_INTERFACE_DEFINED__

        if not defined(__IMFHttpDownloadSession_INTERFACE_DEFINED__):
            # interface IMFHttpDownloadSession
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFHttpDownloadSession = MIDL_INTERFACE(
                    "{71FA9A2C-53CE-4662-A132-1A7E8CBF62DB}"
                )
                IMFHttpDownloadSession._iid_ = IID_IMFHttpDownloadSession


                IMFHttpDownloadSession._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetServer')],
                        HRESULT,
                        'SetServer',
                        (['in'], LPCWSTR, 'szServerName'),
                        (['in'], DWORD, 'nPort'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CreateRequest')],
                        HRESULT,
                        'CreateRequest',
                        (['in'], LPCWSTR, 'szObjectName'),
                        (['in'], BOOL, 'fBypassProxyCache'),
                        (['in'], BOOL, 'fSecure'),
                        (['in'], LPCWSTR, 'szVerb'),
                        (['in'], LPCWSTR, 'szReferrer'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFHttpDownloadRequest)),
                           'ppRequest'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFHttpDownloadSession_INTERFACE_DEFINED__

        if not defined(__IMFHttpDownloadSessionProvider_INTERFACE_DEFINED__):
            # interface IMFHttpDownloadSessionProvider
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFHttpDownloadSessionProvider = MIDL_INTERFACE(
                    "{1B4CF4B9-3A16-4115-839D-03CC5C99DF01}"
                )
                IMFHttpDownloadSessionProvider._iid_ = IID_IMFHttpDownloadSessionProvider


                IMFHttpDownloadSessionProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateHttpDownloadSession')],
                        HRESULT,
                        'CreateHttpDownloadSession',
                        (['in'], LPCWSTR, 'wszScheme'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFHttpDownloadSession)),
                           'ppDownloadSession'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFHttpDownloadSessionProvider_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0107
        # [local]
        MFNETSOURCE_HTTP_DOWNLOAD_SESSION_PROVIDER = EXTERN_GUID(
            0x7D55081E,
            0x307D,
            0x4D6D,
            0xA6,
            0x63,
            0xA9,
            0x3B,
            0xE9,
            0x7C,
            0x4B,
            0x5C
        )
    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

    if WINVER >= _WIN32_WINNT_WIN10:
        class MF_MEDIASOURCE_STATUS_INFO(ENUM):
            MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED = 0
            MF_MEDIASOURCE_STATUS_INFO_UNKNOWN = 1

        MF_SD_MEDIASOURCE_STATUS = EXTERN_GUID(
            0x1913678B,
            0xFC0F,
            0x44DA,
            0x8F,
            0x43,
            0x1B,
            0xA3,
            0xB5,
            0x26,
            0xF4,
            0xAE
        )

        _MF_VIDEO_SPHERICAL_VIEWDIRECTION._fields_ = [
            ('iHeading', INT),
            ('iPitch', INT),
            ('iRoll', INT),
        ]
        MF_SD_VIDEO_SPHERICAL = EXTERN_GUID(
            0xA51DA449,
            0x3FDC,
            0x478C,
            0xBC,
            0xB5,
            0x30,
            0xBE,
            0x76,
            0x59,
            0x5F,
            0x55
        )
        MF_SD_VIDEO_SPHERICAL_FORMAT = EXTERN_GUID(
            0x4A8FC407,
            0x6EA1,
            0x46C8,
            0xB5,
            0x67,
            0x69,
            0x71,
            0xD4,
            0xA1,
            0x39,
            0xC3
        )
        MF_SD_VIDEO_SPHERICAL_INITIAL_VIEWDIRECTION = EXTERN_GUID(
            0x11D25A49,
            0xBB62,
            0x467F,
            0x9D,
            0xB1,
            0xC1,
            0x71,
            0x65,
            0x71,
            0x6C,
            0x49
        )
        MF_MEDIASOURCE_EXPOSE_ALL_STREAMS = EXTERN_GUID(
            0xE7F250B8,
            0x8FD9,
            0x4A09,
            0xB6,
            0xC1,
            0x6A,
            0x31,
            0x5C,
            0x7C,
            0x72,
            0xE
        )
        if not defined(__IMFMediaSource2_INTERFACE_DEFINED__):
            # interface IMFMediaSource2
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaSource2 = MIDL_INTERFACE(
                    "{FBB03414-D13B-4786-8319-5AC51FC0A136}"
                )
                IMFMediaSource2._iid_ = IID_IMFMediaSource2


                IMFMediaSource2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetMediaType')],
                        HRESULT,
                        'SetMediaType',
                        (['in'], DWORD, 'dwStreamID'),
                        (['in'], POINTER(IMFMediaType), 'pMediaType'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaSource2_INTERFACE_DEFINED__

        if not defined(__IMFMediaStream2_INTERFACE_DEFINED__):
            # interface IMFMediaStream2
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFMediaStream2 = MIDL_INTERFACE(
                    "{C5BC37D6-75C7-46A1-A132-81B5F723C20F}"
                )
                IMFMediaStream2._iid_ = IID_IMFMediaStream2


                IMFMediaStream2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetStreamState')],
                        HRESULT,
                        'SetStreamState',
                        (['in'], MF_STREAM_STATE, 'value'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamState')],
                        HRESULT,
                        'GetStreamState',
                        (['out'], POINTER(MF_STREAM_STATE), 'value'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFMediaStream2_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0109
        # [local]    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)
    if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            MF_ST_MEDIASOURCE_COLLECTION = EXTERN_GUID(
                0x616DE972,
                0x83AD,
                0x4950,
                0x81,
                0x70,
                0x63,
                0x0D,
                0x19,
                0xCB,
                0xE3,
                0x07
            )
            MF_DEVICESTREAM_FILTER_KSCONTROL = EXTERN_GUID(
                0x46783CCA,
                0x3DF5,
                0x4923,
                0xA9,
                0xEF,
                0x36,
                0xB7,
                0x22,
                0x3E,
                0xDD,
                0xE0
            )
            MF_DEVICESTREAM_PIN_KSCONTROL = EXTERN_GUID(
                0xEF3EF9A7,
                0x87F2,
                0x48CA,
                0xBE,
                0x02,
                0x67,
                0x48,
                0x78,
                0x91,
                0x8E,
                0x98
            )
            MF_DEVICESTREAM_SOURCE_ATTRIBUTES = EXTERN_GUID(
                0x2F8CB617,
                0x361B,
                0x434F,
                0x85,
                0xEA,
                0x99,
                0xA0,
                0x3E,
                0x1C,
                0xE4,
                0xE0
            )
            MF_DEVICESTREAM_FRAMESERVER_HIDDEN = EXTERN_GUID(
                0xF402567B,
                0x4D91,
                0x4179,
                0x96,
                0xD1,
                0x74,
                0xC8,
                0x48,
                0x0C,
                0x20,
                0x34
            )
            MF_STF_VERSION_INFO = EXTERN_GUID(
                0x6770BD39,
                0xEF82,
                0x44EE,
                0xA4,
                0x9B,
                0x93,
                0x4B,
                0xEB,
                0x24,
                0xAE,
                0xF7
            )
            MF_STF_VERSION_DATE = EXTERN_GUID(
                0x31A165D5,
                0xDF67,
                0x4095,
                0x8E,
                0x44,
                0x88,
                0x68,
                0xFC,
                0x20,
                0xDB,
                0xFD
            )
            MF_DEVICESTREAM_REQUIRED_CAPABILITIES = EXTERN_GUID(
                0x6D8B957E,
                0x7CF6,
                0x43F4,
                0xAF,
                0x56,
                0x9C,
                0x0E,
                0x1E,
                0x4F,
                0xCB,
                0xE1
            )
            MF_DEVICESTREAM_REQUIRED_SDDL = EXTERN_GUID(
                0x331AE85D,
                0xC0D3,
                0x49BA,
                0x83,
                0xBA,
                0x82,
                0xA1,
                0x2D,
                0x63,
                0xCD,
                0xD6
            )
            MF_DEVICEMFT_SENSORPROFILE_COLLECTION = EXTERN_GUID(
                0x36EBDC44,
                0xB12C,
                0x441B,
                0x89,
                0xF4,
                0x08,
                0xB2,
                0xF4,
                0x1A,
                0x9C,
                0xFC
            )
            MF_DEVICESTREAM_SENSORSTREAM_ID = EXTERN_GUID(
                0xE35B9FE4,
                0x0659,
                0x4CAD,
                0xBB,
                0x51,
                0x33,
                0x16,
                0x0B,
                0xE7,
                0xE4,
                0x13
            )


            class __MIDL___MIDL_itf_mfidl_0000_0109_0001(ENUM):
                MFSensorDeviceType_Unknown = 0
                MFSensorDeviceType_Device = MFSensorDeviceType_Unknown + 1 )
                MFSensorDeviceType_MediaSource = (
                    MFSensorDeviceType_Device + 1 )
                )
                MFSensorDeviceType_FrameProvider = (
                    MFSensorDeviceType_MediaSource + 1 )
                )
                MFSensorDeviceType_SensorTransform = (
                    MFSensorDeviceType_FrameProvider + 1 )
                )
            MFSensorDeviceType = __MIDL___MIDL_itf_mfidl_0000_0109_0001


            class __MIDL___MIDL_itf_mfidl_0000_0109_0002(ENUM):
                MFSensorStreamType_Unknown = 0
                MFSensorStreamType_Input = MFSensorStreamType_Unknown + 1 )
                MFSensorStreamType_Output = MFSensorStreamType_Input + 1 )
            MFSensorStreamType = __MIDL___MIDL_itf_mfidl_0000_0109_0002


            class __MIDL___MIDL_itf_mfidl_0000_0109_0003(ENUM):
                MFSensorDeviceMode_Controller = 0
                MFSensorDeviceMode_Shared = MFSensorDeviceMode_Controller + 1 )
            MFSensorDeviceMode = __MIDL___MIDL_itf_mfidl_0000_0109_0003
            if not defined(__IMFSensorDevice_INTERFACE_DEFINED__):
                # interface IMFSensorDevice
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSensorDevice = MIDL_INTERFACE(
                        "{FB9F48F2-2A18-4E28-9730-786F30F04DC4}"
                    )
                    IMFSensorDevice._iid_ = IID_IMFSensorDevice


                    IMFSensorDevice._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDeviceId')],
                            HRESULT,
                            'GetDeviceId',
                            (['out'], POINTER(ULONGLONG), 'pDeviceId'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceType')],
                            HRESULT,
                            'GetDeviceType',
                            (['out'], POINTER(MFSensorDeviceType), 'pType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFlags')],
                            HRESULT,
                            'GetFlags',
                            (['out'], POINTER(ULONGLONG), 'pFlags'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSymbolicLink')],
                            HRESULT,
                            'GetSymbolicLink',
                            (['out', 'in'], LPWSTR, 'SymbolicLink'),
                            (['in'], LONG, 'cchSymbolicLink'),
                            (['out'], POINTER(LONG), 'pcchWritten'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDeviceAttributes')],
                            HRESULT,
                            'GetDeviceAttributes',
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamAttributesCount')],
                            HRESULT,
                            'GetStreamAttributesCount',
                            (['in'], MFSensorStreamType, 'eType'),
                            (['out'], POINTER(DWORD), 'pdwCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamAttributes')],
                            HRESULT,
                            'GetStreamAttributes',
                            (['in'], MFSensorStreamType, 'eType'),
                            (['in'], DWORD, 'dwIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSensorDeviceMode')],
                            HRESULT,
                            'SetSensorDeviceMode',
                            (['in'], MFSensorDeviceMode, 'eMode'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSensorDeviceMode')],
                            HRESULT,
                            'GetSensorDeviceMode',
                            (['out'], POINTER(MFSensorDeviceMode), 'peMode'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSensorDevice_INTERFACE_DEFINED__

            if not defined(__IMFSensorGroup_INTERFACE_DEFINED__):
                # interface IMFSensorGroup
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSensorGroup = MIDL_INTERFACE(
                        "{4110243A-9757-461F-89F1-F22345BCAB4E}"
                    )
                    IMFSensorGroup._iid_ = IID_IMFSensorGroup


                    IMFSensorGroup._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetSymbolicLink')],
                            HRESULT,
                            'GetSymbolicLink',
                            (['out', 'in'], LPWSTR, 'SymbolicLink'),
                            (['in'], LONG, 'cchSymbolicLink'),
                            (['out'], POINTER(LONG), 'pcchWritten'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFlags')],
                            HRESULT,
                            'GetFlags',
                            (['out'], POINTER(ULONGLONG), 'pFlags'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSensorGroupAttributes')],
                            HRESULT,
                            'GetSensorGroupAttributes',
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSensorDeviceCount')],
                            HRESULT,
                            'GetSensorDeviceCount',
                            (['out'], POINTER(DWORD), 'pdwCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSensorDevice')],
                            HRESULT,
                            'GetSensorDevice',
                            (['in'], DWORD, 'dwIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFSensorDevice)),
                               'ppDevice'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetDefaultSensorDeviceIndex')],
                            HRESULT,
                            'SetDefaultSensorDeviceIndex',
                            (['in'], DWORD, 'dwIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDefaultSensorDeviceIndex')],
                            HRESULT,
                            'GetDefaultSensorDeviceIndex',
                            (['out'], POINTER(DWORD), 'pdwIndex'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateMediaSource')],
                            HRESULT,
                            'CreateMediaSource',
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaSource)),
                               'ppSource'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSensorGroup_INTERFACE_DEFINED__

            if not defined(__IMFSensorStream_INTERFACE_DEFINED__):
                # interface IMFSensorStream
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSensorStream = MIDL_INTERFACE(
                        "{E9A42171-C56E-498A-8B39-EDA5A070B7FC}"
                    )
                    IMFSensorStream._iid_ = IID_IMFSensorStream


                    IMFSensorStream._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetMediaTypeCount')],
                            HRESULT,
                            'GetMediaTypeCount',
                            (['out'], POINTER(DWORD), 'pdwCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMediaType')],
                            HRESULT,
                            'GetMediaType',
                            (['in'], DWORD, 'dwIndex'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFMediaType)),
                               'ppMediaType'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CloneSensorStream')],
                            HRESULT,
                            'CloneSensorStream',
                            (
                                ['out'],
                                POINTER(POINTER(IMFSensorStream)),
                               'ppStream'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSensorStream_INTERFACE_DEFINED__

            if not defined(__IMFSensorTransformFactory_INTERFACE_DEFINED__):
                # interface IMFSensorTransformFactory
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSensorTransformFactory = MIDL_INTERFACE(
                        "{EED9C2EE-66B4-4F18-A697-AC7D3960215C}"
                    )
                    IMFSensorTransformFactory._iid_ = IID_IMFSensorTransformFactory


                    IMFSensorTransformFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetFactoryAttributes')],
                            HRESULT,
                            'GetFactoryAttributes',
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttributes'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method InitializeFactory')],
                            HRESULT,
                            'InitializeFactory',
                            (['in'], DWORD, 'dwMaxTransformCount'),
                            (
                                ['in'],
                                POINTER(IMFCollection),
                               'pSensorDevices'
                            ),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetTransformCount')],
                            HRESULT,
                            'GetTransformCount',
                            (['out'], POINTER(DWORD), 'pdwCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetTransformInformation')],
                            HRESULT,
                            'GetTransformInformation',
                            (['in'], DWORD, 'TransformIndex'),
                            (['out'], POINTER(GUID), 'pguidTransformId'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFAttributes)),
                               'ppAttributes'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IMFCollection)),
                               'ppStreamInformation'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateTransform')],
                            HRESULT,
                            'CreateTransform',
                            (['in'], REFGUID, 'guidSensorTransformID'),
                            (['in'], POINTER(IMFAttributes), 'pAttributes'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFDeviceTransform)),
                               'ppDeviceMFT'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSensorTransformFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0113
            # [local]
            __MIDL___MIDL_itf_mfidl_0000_0113_0001._fields_ = [
                ('Type', GUID),
                ('Index', UINT32),
                ('Unused', UINT32),
            ]
            if not defined(__IMFSensorProfile_INTERFACE_DEFINED__):
                # interface IMFSensorProfile
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSensorProfile = MIDL_INTERFACE(
                        "{22F765D1-8DAB-4107-846D-56BAF72215E7}"
                    )
                    IMFSensorProfile._iid_ = IID_IMFSensorProfile


                    IMFSensorProfile._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetProfileId')],
                            HRESULT,
                            'GetProfileId',
                            (['out'], POINTER(SENSORPROFILEID), 'pId'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddProfileFilter')],
                            HRESULT,
                            'AddProfileFilter',
                            (['in'], UINT32, 'StreamId'),
                            (['in'], LPCWSTR, 'wzFilterSetString'),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsMediaTypeSupported')],
                            HRESULT,
                            'IsMediaTypeSupported',
                            (['in'], UINT32, 'StreamId'),
                            (['in'], POINTER(IMFMediaType), 'pMediaType'),
                            (['out'], POINTER(BOOL), 'pfSupported'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddBlockedControl')],
                            HRESULT,
                            'AddBlockedControl',
                            (['in'], LPCWSTR, 'wzBlockedControl'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSensorProfile_INTERFACE_DEFINED__

            if not defined(__IMFSensorProfileCollection_INTERFACE_DEFINED__):
                # interface IMFSensorProfileCollection
                # [local][helpstring][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFSensorProfileCollection = MIDL_INTERFACE(
                        "{C95EA55B-0187-48BE-9353-8D2507662351}"
                    )
                    IMFSensorProfileCollection._iid_ = IID_IMFSensorProfileCollection


                    IMFSensorProfileCollection._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetProfileCount')],
                            DWORD,
                            'GetProfileCount',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetProfile')],
                            HRESULT,
                            'GetProfile',
                            (['in'], DWORD, 'Index'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFSensorProfile)),
                               'ppProfile'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddProfile')],
                            HRESULT,
                            'AddProfile',
                            (['in'], POINTER(IMFSensorProfile), 'pProfile'),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindProfile')],
                            HRESULT,
                            'FindProfile',
                            (['in'], POINTER(SENSORPROFILEID), 'ProfileId'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFSensorProfile)),
                               'ppProfile'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveProfileByIndex')],
                            VOID,
                            'RemoveProfileByIndex',
                            (['in'], DWORD, 'Index'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveProfile')],
                            VOID,
                            'RemoveProfile',
                            (['in'], POINTER(SENSORPROFILEID), 'ProfileId'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFSensorProfileCollection_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfidl_0000_0115
            # [local]
            mfsensorgroup = ctypes.windll.MFSENSORGROUP


            # STDAPI
            # MFCreateSensorProfile(
            # _In_ REFGUID ProfileType,
            # _In_ UINT32 ProfileIndex,
            # _In_opt_z_ LPCWSTR Constraints,
            # _COM_Outptr_ IMFSensorProfile** ppProfile
            # );
            MFCreateSensorProfile = mfsensorgroup.MFCreateSensorProfile
            MFCreateSensorProfile.restype = STDAPI


            # STDAPI
            # MFCreateSensorProfileCollection(
            # _COM_Outptr_ IMFSensorProfileCollection** ppSensorProfile
            # );
            MFCreateSensorProfileCollection = (
                mfsensorgroup.MFCreateSensorProfileCollection
            )
            MFCreateSensorProfileCollection.restype = STDAPI

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if not defined(__IMFSensorProcessActivity_INTERFACE_DEFINED__):
            # interface IMFSensorProcessActivity
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSensorProcessActivity = MIDL_INTERFACE(
                    "{39DC7F4A-B141-4719-813C-A7F46162A2B8}"
                )
                IMFSensorProcessActivity._iid_ = IID_IMFSensorProcessActivity


                IMFSensorProcessActivity._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetProcessId')],
                        HRESULT,
                        'GetProcessId',
                        (['out'], POINTER(ULONG), 'pPID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamingState')],
                        HRESULT,
                        'GetStreamingState',
                        (['out'], POINTER(BOOL), 'pfStreaming'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamingMode')],
                        HRESULT,
                        'GetStreamingMode',
                        (['out'], POINTER(MFSensorDeviceMode), 'pMode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetReportTime')],
                        HRESULT,
                        'GetReportTime',
                        (['out'], POINTER(FILETIME), 'pft'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSensorProcessActivity_INTERFACE_DEFINED__

        if not defined(__IMFSensorActivityReport_INTERFACE_DEFINED__):
            # interface IMFSensorActivityReport
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSensorActivityReport = MIDL_INTERFACE(
                    "{3E8C4BE1-A8C2-4528-90DE-2851BDE5FEAD}"
                )
                IMFSensorActivityReport._iid_ = IID_IMFSensorActivityReport


                IMFSensorActivityReport._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetFriendlyName')],
                        HRESULT,
                        'GetFriendlyName',
                        (['out'], LPWSTR, 'FriendlyName'),
                        (['in'], ULONG, 'cchFriendlyName'),
                        (['out'], POINTER(ULONG), 'pcchWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSymbolicLink')],
                        HRESULT,
                        'GetSymbolicLink',
                        (['out', 'in'], LPWSTR, 'SymbolicLink'),
                        (['in'], ULONG, 'cchSymbolicLink'),
                        (['out'], POINTER(ULONG), 'pcchWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProcessCount')],
                        HRESULT,
                        'GetProcessCount',
                        (['out'], POINTER(ULONG), 'pcCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetProcessActivity')],
                        HRESULT,
                        'GetProcessActivity',
                        (['in'], ULONG, 'Index'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFSensorProcessActivity)),
                           'ppProcessActivity'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSensorActivityReport_INTERFACE_DEFINED__

        if not defined(__IMFSensorActivitiesReport_INTERFACE_DEFINED__):
            # interface IMFSensorActivitiesReport
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSensorActivitiesReport = MIDL_INTERFACE(
                    "{683F7A5E-4A19-43CD-B1A9-DBF4AB3F7777}"
                )
                IMFSensorActivitiesReport._iid_ = IID_IMFSensorActivitiesReport


                IMFSensorActivitiesReport._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCount')],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(ULONG), 'pcCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetActivityReport')],
                        HRESULT,
                        'GetActivityReport',
                        (['in'], ULONG, 'Index'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFSensorActivityReport)),
                           'sensorActivityReport'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetActivityReportByDeviceName')],
                        HRESULT,
                        'GetActivityReportByDeviceName',
                        (['in'], LPCWSTR, 'SymbolicName'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFSensorActivityReport)),
                           'sensorActivityReport'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSensorActivitiesReport_INTERFACE_DEFINED__

        if not defined(__IMFSensorActivitiesReportCallback_INTERFACE_DEFINED__):
            # interface IMFSensorActivitiesReportCallback
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSensorActivitiesReportCallback = MIDL_INTERFACE(
                    "{DE5072EE-DBE3-46DC-8A87-B6F631194751}"
                )
                IMFSensorActivitiesReportCallback._iid_ = IID_IMFSensorActivitiesReportCallback


                IMFSensorActivitiesReportCallback._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnActivitiesReport')],
                        HRESULT,
                        'OnActivitiesReport',
                        (
                            ['in'],
                            POINTER(IMFSensorActivitiesReport),
                           'sensorActivitiesReport'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSensorActivitiesReportCallback_INTERFACE_DEFINED__

        if not defined(__IMFSensorActivityMonitor_INTERFACE_DEFINED__):
            # interface IMFSensorActivityMonitor
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSensorActivityMonitor = MIDL_INTERFACE(
                    "{D0CEF145-B3F4-4340-A2E5-7A5080CA05CB}"
                )
                IMFSensorActivityMonitor._iid_ = IID_IMFSensorActivityMonitor


                IMFSensorActivityMonitor._methods_ = [
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
                ]

            # END IF  C style interface
        # END IF  __IMFSensorActivityMonitor_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfidl_0000_0120
        # [local]
        mfsensorgroup = ctypes.windll.MFSENSORGROUP


        # STDAPI
        # MFCreateSensorActivityMonitor(
        # _In_ IMFSensorActivitiesReportCallback* pCallback,
        # _COM_Outptr_ IMFSensorActivityMonitor** ppActivityMonitor
        # );
        MFCreateSensorActivityMonitor = (
            mfsensorgroup.MFCreateSensorActivityMonitor
        )
        MFCreateSensorActivityMonitor.restype = STDAPI


    # END IF   (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32


    # ULONG              BSTR_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG


    # UCHAR *  BSTR_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = POINTER(UCHAR)


    # UCHAR *  BSTR_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = POINTER(UCHAR)


    # VOID                       BSTR_UserFree(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID


    # ULONG              LPSAFEARRAY_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize = oleaut32.LPSAFEARRAY_UserSize
    LPSAFEARRAY_UserSize.restype = ULONG


    # UCHAR *  LPSAFEARRAY_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal = oleaut32.LPSAFEARRAY_UserMarshal
    LPSAFEARRAY_UserMarshal.restype = POINTER(UCHAR)


    # UCHAR *  LPSAFEARRAY_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal = oleaut32.LPSAFEARRAY_UserUnmarshal
    LPSAFEARRAY_UserUnmarshal.restype = POINTER(UCHAR)


    # VOID                       LPSAFEARRAY_UserFree(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree = oleaut32.LPSAFEARRAY_UserFree
    LPSAFEARRAY_UserFree.restype = VOID


    # ULONG              BSTR_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG


    # UCHAR *  BSTR_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = POINTER(UCHAR)


    # UCHAR *  BSTR_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = POINTER(UCHAR)


    # VOID                       BSTR_UserFree64(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID


    # ULONG              LPSAFEARRAY_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize64 = oleaut32.LPSAFEARRAY_UserSize64
    LPSAFEARRAY_UserSize64.restype = ULONG


    # UCHAR *  LPSAFEARRAY_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal64 = oleaut32.LPSAFEARRAY_UserMarshal64
    LPSAFEARRAY_UserMarshal64.restype = POINTER(UCHAR)


    # UCHAR *  LPSAFEARRAY_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal64 = oleaut32.LPSAFEARRAY_UserUnmarshal64
    LPSAFEARRAY_UserUnmarshal64.restype = POINTER(UCHAR)


    # VOID                       LPSAFEARRAY_UserFree64(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree64 = oleaut32.LPSAFEARRAY_UserFree64
    LPSAFEARRAY_UserFree64.restype = VOID

    # [local]    # [in]    # [in]    # [in]
    # [annotation][out]    # [in]    # [in]    # [call_as]    # [string][in]    # [in]    # [in]    # [in]    # [local]    # [in]
    # [annotation][out]
    # [annotation][out]    # [call_as]    # [in]    # [out]    # [out]    # [local]    # [in]    # [in]    # [in]    # [in]
    # [annotation][out]    # [in]    # [in]    # [call_as]    # [in]    # [unique][in]    # [in]    # [unique][in]    # [in]    # [local]    # [in]
    # [annotation][out]
    # [annotation][out]    # [call_as]    # [in]    # [out]    # [out]    # [local]
    # [annotation][out]    # [call_as]    # [out]    # [size_is][size_is][out]    # [out]    # [local]    # [in]    # [call_as]    # [local]    # [in]
    # [annotation][out]    # [call_as]    # [in]    # [out]    # [size_is][size_is][out]    # [local]    # [in]
    # [annotation][out]    # [call_as]    # [in]    # [out]    # [size_is][size_is][out]    # [local]    # [in]
    # [annotation][out]    # [call_as]    # [size_is][in]    # [in]    # [size_is][size_is][out]    # [out]    # [local]    # [in]
    # [annotation][out]    # [call_as]    # [in]    # [size_is][size_is][out]    # [out]    # [local]    # [in]    # [call_as]    # [size_is][in]    # [in]    # [local]
    # [annotation][out]    # [call_as]    # [size_is][size_is][out]    # [out]    # [local]    # [in]    # [in]    # [in]    # [in]    # [call_as]    # [in]    # [size_is][in]    # [in]    # [in]    # [local]    # [in]    # [call_as]    # [in]    # [local]    # [in]    # [in]    # [call_as]    # [in]    # [local]    # [in]    # [call_as]    # [in]    # [local]    # [in]    # [in]    # [call_as]    # [in]    # [local]    # [in]    # [call_as]    # [in]    # [local]    # [in]    # [in]    # [in]    # [in]    # [in]    # [call_as]    # [in]    # [in]    # [in]    # [in]    # [local]    # [in]
    # [annotation][out]    # [call_as]    # [in]    # [out]    # [local]    # [in]    # [in]    # [in]    # [call_as]    # [in]    # [in]    # [local]    # [in]    # [call_as]    # [in]    # [local]    # [in]    # [in]    # [in]    # [in]    # [in]    # [in]    # [call_as]    # [in]    # [in]    # [in]    # [in]    # [in]    # [local]    # [in]    # [unique][in]    # [in]    # [iid_is][out]    # [call_as]    # [in]    # [size_is][unique][in]    # [in]    # [in]    # [iid_is][out]
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


