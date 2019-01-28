import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__MFAPI_H__ = None
AVRT_DATA = None
AVRT_BSS = None
MF_VERSION = None
MF_INIT_GUIDS = None
FCC = None
DEFINE_MEDIATYPE_GUID = None
DIRECT3D_VERSION = None
LOCAL_D3DFMT_DEFINES = None
DEFINE_BINARY_MEDIATYPE_GUID = None
_MFVideoRotationFormat_ = None
_KSMEDIA_ = None
_INTSAFE_H_INCLUDED_ = None


class tagMFASYNCRESULT(ctypes.Structure):
    pass


MFASYNCRESULT = tagMFASYNCRESULT


class _MOVE_RECT(ctypes.Structure):
    pass


MOVE_RECT = _MOVE_RECT


class _DIRTYRECT_INFO(ctypes.Structure):
    pass


DIRTYRECT_INFO = _DIRTYRECT_INFO


class _MOVEREGION_INFO(ctypes.Structure):
    pass


MOVEREGION_INFO = _MOVEREGION_INFO


class _ROI_AREA(ctypes.Structure):
    pass


ROI_AREA = _ROI_AREA
PROI_AREA = POINTER(_ROI_AREA)


class _MACROBLOCK_DATA(ctypes.Structure):
    pass


MACROBLOCK_DATA = _MACROBLOCK_DATA


class tagFaceRectInfoBlobHeader(ctypes.Structure):
    pass


FaceRectInfoBlobHeader = tagFaceRectInfoBlobHeader


class tagFaceRectInfo(ctypes.Structure):
    pass


FaceRectInfo = tagFaceRectInfo


class tagFaceCharacterizationBlobHeader(ctypes.Structure):
    pass


FaceCharacterizationBlobHeader = tagFaceCharacterizationBlobHeader


class tagFaceCharacterization(ctypes.Structure):
    pass


FaceCharacterization = tagFaceCharacterization


class tagCapturedMetadataExposureCompensation(ctypes.Structure):
    pass


CapturedMetadataExposureCompensation = tagCapturedMetadataExposureCompensation


class tagCapturedMetadataISOGains(ctypes.Structure):
    pass


CapturedMetadataISOGains = tagCapturedMetadataISOGains


class tagCapturedMetadataWhiteBalanceGains(ctypes.Structure):
    pass


CapturedMetadataWhiteBalanceGains = tagCapturedMetadataWhiteBalanceGains


class tagMetadataTimeStamps(ctypes.Structure):
    pass


MetadataTimeStamps = tagMetadataTimeStamps


class tagHistogramGrid(ctypes.Structure):
    pass


HistogramGrid = tagHistogramGrid


class tagHistogramBlobHeader(ctypes.Structure):
    pass


HistogramBlobHeader = tagHistogramBlobHeader


class tagHistogramHeader(ctypes.Structure):
    pass


HistogramHeader = tagHistogramHeader


class tagHistogramDataHeader(ctypes.Structure):
    pass


HistogramDataHeader = tagHistogramDataHeader


class _MFFOLDDOWN_MATRIX(ctypes.Structure):
    pass


MFFOLDDOWN_MATRIX = _MFFOLDDOWN_MATRIX


class _MT_CUSTOM_VIDEO_PRIMARIES(ctypes.Structure):
    pass


MT_CUSTOM_VIDEO_PRIMARIES = _MT_CUSTOM_VIDEO_PRIMARIES


class _MT_ARBITRARY_HEADER(ctypes.Structure):
    pass


MT_ARBITRARY_HEADER = _MT_ARBITRARY_HEADER


class _MF_FLOAT2(ctypes.Structure):
    pass


MF_FLOAT2 = _MF_FLOAT2


class _MF_FLOAT3(ctypes.Structure):
    pass


MF_FLOAT3 = _MF_FLOAT3


class _MF_QUATERNION(ctypes.Structure):
    pass


MF_QUATERNION = _MF_QUATERNION


class _MFCameraExtrinsic_CalibratedTransform(ctypes.Structure):
    pass


MFCameraExtrinsic_CalibratedTransform = _MFCameraExtrinsic_CalibratedTransform


class _MFCameraExtrinsics(ctypes.Structure):
    pass


MFCameraExtrinsics = _MFCameraExtrinsics


class _MFCameraIntrinsic_PinholeCameraModel(ctypes.Structure):
    pass


MFCameraIntrinsic_PinholeCameraModel = _MFCameraIntrinsic_PinholeCameraModel


class _MFCameraIntrinsic_DistortionModel(ctypes.Structure):
    pass


MFCameraIntrinsic_DistortionModel = _MFCameraIntrinsic_DistortionModel


class _MFPinholeCameraIntrinsic_IntrinsicModel(ctypes.Structure):
    pass


MFPinholeCameraIntrinsic_IntrinsicModel = _MFPinholeCameraIntrinsic_IntrinsicModel


class _MFPinholeCameraIntrinsics(ctypes.Structure):
    pass


MFPinholeCameraIntrinsics = _MFPinholeCameraIntrinsics

from pyWinAPI.shared.winapifamily_h import * # NOQA

# @@@ + + +
# @@@@******************************************************************
# Microsoft Windows Media Foundation
# Copyright (C) Microsoft Corporation. All rights reserved.
# @@@---@@@@******************************************************************
# MFAPI.h is the header containing the APIs for using the MF platform.
if not defined(__MFAPI_H__):
    __MFAPI_H__ = VOID
    from pyWinAPI.um.mfobjects_h import * # NOQA
    from pyWinAPI.shared.mmreg_h import * # NOQA
    from pyWinAPI.um.avrt_h import * # NOQA
    from pyWinAPI.um.minwinbase_h import * # NOQA

    if not defined(AVRT_DATA):
        AVRT_DATA = VOID
    # END IF

    if not defined(AVRT_BSS):
        AVRT_BSS = VOID
    # END IF

    if not defined(MF_VERSION):
        if WINVER >= _WIN32_WINNT_WIN7:
            MF_SDK_VERSION = 0x0002
        else:
            MF_SDK_VERSION = 0x0001
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        MF_API_VERSION = 0x0070
        MF_VERSION = MF_SDK_VERSION << 16 | MF_API_VERSION
    # END IF  not defined(MF_VERSION)

    MFSTARTUP_NOSOCKET = 0x1
    MFSTARTUP_LITE = MFSTARTUP_NOSOCKET
    MFSTARTUP_FULL = 0
    if defined(__cplusplus):
        pass
    # END IF

    # /////////////////////////////////////////////////////////////////////////
    # ///////////////////////////// Startup/Shutdown //////////////////////////
    # /////////////////////////////////////////////////////////////////////////
    #
    # Initializes the platform object.
    # Must be called before using Media Foundation.
    # A matching MFShutdown call must be made when the application is done
    # using
    # Media Foundation.
    # The "Version" parameter should be set to MF_API_VERSION.
    # Application should not call MFStartup / MFShutdown from workqueue threads

    mfplat = ctypes.windll.MFPLAT
    if defined(__cplusplus):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):

            # STDAPI MFStartup( ULONG Version, DWORD dwFlags = MFSTARTUP_FULL );
            MFStartup = mfplat.MFStartup
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    else:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            # STDAPI MFStartup( ULONG Version, DWORD dwFlags );
            MFStartup = mfplat.MFStartup

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # Shuts down the platform object.
        # Releases all resources including threads.
        # Application should call MFShutdown the same number of times as
        # MFStartup
        # Application should not call MFStartup / MFShutdown from workqueue
        # threads
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////// Platform ////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        #
        # These functions can be used to keep the MF platform object in place.
        # Every call to MFLockPlatform should have a matching call to
        # MFUnlockPlatform
        # /////////////////////////////////////////////////////////////////////
        #
        # MF workitem functions
        MFShutdown = mfplat.MFShutdown
        MFLockPlatform = mfplat.MFLockPlatform
        MFUnlockPlatform = mfplat.MFUnlockPlatform

        MFWORKITEM_KEY = UINT64
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # STDAPI MFPutWorkItem(
        # DWORD dwQueue,
        # IMFAsyncCallback * pCallback,
        # IUnknown * pState);
        MFPutWorkItem = mfplat.MFPutWorkItem
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFPutWorkItem2(
        # DWORD dwQueue,
        # LONG Priority,
        # _In_ IMFAsyncCallback * pCallback,
        # _In_opt_ IUnknown * pState);
        MFPutWorkItem2 = mfplat.MFPutWorkItem2
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        mfplat = ctypes.windll.MFPLAT
        # STDAPI MFPutWorkItemEx(
        # DWORD dwQueue,
        # IMFAsyncResult * pResult);
        MFPutWorkItemEx = mfplat.MFPutWorkItemEx
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFPutWorkItemEx2(
        # DWORD dwQueue,
        # LONG Priority,
        # _In_ IMFAsyncResult * pResult);
        MFPutWorkItemEx2 = mfplat.MFPutWorkItemEx2

        # STDAPI MFPutWaitingWorkItem(
        # HANDLE hEvent,
        # LONG Priority,
        # _In_ IMFAsyncResult * pResult,
        # _Out_opt_ MFWORKITEM_KEY * pKey
        # );
        MFPutWaitingWorkItem = mfplat.MFPutWaitingWorkItem

        # STDAPI MFAllocateSerialWorkQueue(
        # _In_ DWORD dwWorkQueue,
        # _Out_ OUT DWORD * pdwWorkQueue);
        MFAllocateSerialWorkQueue = mfplat.MFAllocateSerialWorkQueue

        # STDAPI MFScheduleWorkItemEx(
        # IMFAsyncResult * pResult,
        # INT64 Timeout,
        # _Out_opt_ MFWORKITEM_KEY * pKey);
        MFScheduleWorkItemEx = mfplat.MFScheduleWorkItemEx
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # STDAPI MFScheduleWorkItem(
        # IMFAsyncCallback * pCallback,
        # IUnknown * pState,
        # INT64 Timeout,
        # _Out_opt_ MFWORKITEM_KEY * pKey);
        MFScheduleWorkItem = mfplat.MFScheduleWorkItem

        # The CancelWorkItem method is used by objects to cancel scheduled
        # operation
        # Due to asynchronous nature of timers, application might still get a
        # timer callback after MFCancelWorkItem has returned.
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFCancelWorkItem(
        # MFWORKITEM_KEY Key);
        MFCancelWorkItem = mfplat.MFCancelWorkItem

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # /////////////////////////////////////////////////////////////////////
        # MF periodic callbacks
        # STDAPI MFGetTimerPeriodicity(
        # _Out_ DWORD * Periodicity);
        MFGetTimerPeriodicity = mfplat.MFGetTimerPeriodicity

        # typedef VOID (*MFPERIODICCALLBACK)(IUnknown* pContext);
        MFPERIODICCALLBACK = CALLBACK(
            VOID,
            POINTER(comtypes.IUnknown)
        )

        # STDAPI MFAddPeriodicCallback(
        # MFPERIODICCALLBACK Callback,
        # IUnknown * pContext,
        # _Out_opt_ DWORD * pdwKey);
        MFAddPeriodicCallback = mfplat.MFAddPeriodicCallback

        # STDAPI MFRemovePeriodicCallback(
        # DWORD dwKey);
        MFRemovePeriodicCallback = mfplat.MFRemovePeriodicCallback

        # /////////////////////////////////////////////////////////////////////
        # MF work queues

        if WINVER >= _WIN32_WINNT_WIN7:
            # MFASYNC_WORKQUEUE_TYPE: types of work queue used by
            # MFAllocateWorkQueueEx
            class MFASYNC_WORKQUEUE_TYPE(ENUM):
                MF_STANDARD_WORKQUEUE = 0
                MF_WINDOW_WORKQUEUE = 1
                MF_MULTITHREADED_WORKQUEUE = 2

            MF_STANDARD_WORKQUEUE = MFASYNC_WORKQUEUE_TYPE.MF_STANDARD_WORKQUEUE
            MF_WINDOW_WORKQUEUE = MFASYNC_WORKQUEUE_TYPE.MF_WINDOW_WORKQUEUE
            MF_MULTITHREADED_WORKQUEUE = MFASYNC_WORKQUEUE_TYPE.MF_MULTITHREADED_WORKQUEUE

            # STDAPI MFAllocateWorkQueueEx(
            # _In_ MFASYNC_WORKQUEUE_TYPE WorkQueueType,
            # _Out_ OUT DWORD * pdwWorkQueue);
            MFAllocateWorkQueueEx = mfplat.MFAllocateWorkQueueEx
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        # Allocate a standard work queue. the behaviour is the same with:
        # MFAllocateWorkQueueEx( MF_STANDARD_WORKQUEUE, pdwWorkQueue )
        # STDAPI MFAllocateWorkQueue(
        # _Out_ OUT DWORD * pdwWorkQueue);
        MFAllocateWorkQueue = mfplat.MFAllocateWorkQueue
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFLockWorkQueue(
        # _In_ DWORD dwWorkQueue);
        MFLockWorkQueue = mfplat.MFLockWorkQueue

        # STDAPI MFUnlockWorkQueue(
        # _In_ DWORD dwWorkQueue);
        MFUnlockWorkQueue = mfplat.MFUnlockWorkQueue
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # STDAPI MFBeginRegisterWorkQueueWithMMCSS(
        # DWORD dwWorkQueueId,
        # _In_ LPCWSTR wszClass,
        # DWORD dwTaskId,
        # _In_ IMFAsyncCallback * pDoneCallback,
        # _In_ IUnknown * pDoneState );
        MFBeginRegisterWorkQueueWithMMCSS = (
            mfplat.MFBeginRegisterWorkQueueWithMMCSS
        )

        # STDAPI MFBeginRegisterWorkQueueWithMMCSSEx(
        # DWORD dwWorkQueueId,
        # _In_ LPCWSTR wszClass,
        # DWORD dwTaskId,
        # LONG lPriority,
        # _In_ IMFAsyncCallback * pDoneCallback,
        # _In_ IUnknown * pDoneState );
        MFBeginRegisterWorkQueueWithMMCSSEx = (
            mfplat.MFBeginRegisterWorkQueueWithMMCSSEx
        )
        # STDAPI MFEndRegisterWorkQueueWithMMCSS(
        # _In_ IMFAsyncResult * pResult,
        # _Out_ DWORD * pdwTaskId );
        MFEndRegisterWorkQueueWithMMCSS = (
            mfplat.MFEndRegisterWorkQueueWithMMCSS
        )

        # STDAPI MFBeginUnregisterWorkQueueWithMMCSS(
        # DWORD dwWorkQueueId,
        # _In_ IMFAsyncCallback * pDoneCallback,
        # _In_ IUnknown * pDoneState );
        MFBeginUnregisterWorkQueueWithMMCSS = (
            mfplat.MFBeginUnregisterWorkQueueWithMMCSS
        )

        # STDAPI MFEndUnregisterWorkQueueWithMMCSS(
        # _In_ IMFAsyncResult * pResult );
        MFEndUnregisterWorkQueueWithMMCSS = (
            mfplat.MFEndUnregisterWorkQueueWithMMCSS
        )

        # STDAPI MFGetWorkQueueMMCSSClass(
        # DWORD dwWorkQueueId,
        # _Out_writes_to_opt_(*pcchClass,*pcchClass)  LPWSTR pwszClass,
        # _Inout_  DWORD *pcchClass );
        MFGetWorkQueueMMCSSClass = mfplat.MFGetWorkQueueMMCSSClass

        # STDAPI MFGetWorkQueueMMCSSTaskId(
        # DWORD dwWorkQueueId,
        # _Out_ LPDWORD pdwTaskId );
        MFGetWorkQueueMMCSSTaskId = mfplat.MFGetWorkQueueMMCSSTaskId

        # STDAPI MFRegisterPlatformWithMMCSS(
        # _In_ PCWSTR wszClass,
        # _Inout_ DWORD* pdwTaskId,
        # _In_ LONG lPriority );
        MFRegisterPlatformWithMMCSS = mfplat.MFRegisterPlatformWithMMCSS
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):

        # STDAPI MFLockSharedWorkQueue(
        # _In_ PCWSTR wszClass,
        # _In_ LONG BasePriority,
        # _Inout_ DWORD* pdwTaskId,
        # _Out_ DWORD* pID );
        MFLockSharedWorkQueue = mfplat.MFLockSharedWorkQueue
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        # STDAPI MFGetWorkQueueMMCSSPriority(
        # DWORD dwWorkQueueId,
        # _Out_ LONG* lPriority );
        MFGetWorkQueueMMCSSPriority = mfplat.MFGetWorkQueueMMCSSPriority
        # /////////////////////////////////////////////////////////////////////////////
        #
        # /////////////////////////////// Async Model
        # //////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////
        #
        # Instantiates the MF-provided Async Result implementation
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFCreateAsyncResult(
        # IUnknown * punkObject,
        # IMFAsyncCallback * pCallback,
        # IUnknown * punkState,
        # _Out_ IMFAsyncResult ** ppAsyncResult );
        MFCreateAsyncResult = mfplat.MFCreateAsyncResult

        # Helper for calling IMFAsyncCallback::Invoke
        # STDAPI MFInvokeCallback(
        # IMFAsyncResult * pAsyncResult );
        MFInvokeCallback = mfplat.MFInvokeCallback

        # MFASYNCRESULT struct.
        # Any implementation of IMFAsyncResult must inherit from this struct;
        # the Media Foundation workqueue implementation depends on this.
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            tagMFASYNCRESULT._fields_ = [
                ('AsyncResult', IMFAsyncResult),
                ('overlapped', OVERLAPPED),
                ('pCallback', POINTER(IMFAsyncCallback)),
                ('hrStatusResult', HRESULT),
                ('dwBytesTransferred', DWORD),
                ('hEvent', HANDLE),
            ]
        # END IF  C style interface
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////// Files  //////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        #
        # Regardless of the access mode with which the file is opened, the
        # sharing
        # permissions will allow shared reading and deleting.

        # STDAPI MFCreateFile(
        # MF_FILE_ACCESSMODE  AccessMode,
        # MF_FILE_OPENMODE    OpenMode,
        # MF_FILE_FLAGS       fFlags,
        # LPCWSTR             pwszFileURL,
        # _Out_ IMFByteStream       **ppIByteStream );
        MFCreateFile = mfplat.MFCreateFile

        # STDAPI MFCreateTempFile(
        # MF_FILE_ACCESSMODE  AccessMode,
        # MF_FILE_OPENMODE    OpenMode,
        # MF_FILE_FLAGS       fFlags,
        # _Out_ IMFByteStream       **ppIByteStream );
        MFCreateTempFile = mfplat.MFCreateTempFile

        # STDAPI MFBeginCreateFile(
        # MF_FILE_ACCESSMODE  AccessMode,
        # MF_FILE_OPENMODE    OpenMode,
        # MF_FILE_FLAGS       fFlags,
        # LPCWSTR             pwszFilePath,
        # IMFAsyncCallback *  pCallback,
        # IUnknown *          pState,
        # _Out_ IUnknown ** ppCancelCookie);
        MFBeginCreateFile = mfplat.MFBeginCreateFile

        # STDAPI MFEndCreateFile(
        # IMFAsyncResult * pResult,
        # _Out_ IMFByteStream **ppFile );
        MFEndCreateFile = mfplat.MFEndCreateFile

        # STDAPI MFCancelCreateFile(
        # IUnknown * pCancelCookie);
        MFCancelCreateFile = mfplat.MFCancelCreateFile

        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////// Buffers /////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # Creates an IMFMediaBuffer in memory
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFCreateMemoryBuffer(
        # _In_ DWORD                      cbMaxLength,
        # _Out_ IMFMediaBuffer **         ppBuffer );
        MFCreateMemoryBuffer = mfplat.MFCreateMemoryBuffer

        # Creates an IMFMediaBuffer wrapper at the given offset and length
        # within an existing IMFMediaBuffer
        # STDAPI MFCreateMediaBufferWrapper(
        # _In_ IMFMediaBuffer *           pBuffer,
        # _In_ DWORD                      cbOffset,
        # _In_ DWORD                      dwLength,
        # _Out_ IMFMediaBuffer **         ppBuffer );
        MFCreateMediaBufferWrapper = mfplat.MFCreateMediaBufferWrapper
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Creates a legacy buffer (IMediaBuffer) wrapper at the given offset
        # within
        # an existing IMFMediaBuffer.
        # pSample is optional. It can point to the original IMFSample from
        # which this
        # IMFMediaBuffer came. If provided, then *ppMediaBuffer will succeed
        # QueryInterface for IID_IMFSample, from which the original sample's
        # attributes
        # can be obtained

        # STDAPI MFCreateLegacyMediaBufferOnMFMediaBuffer(
        # _In_opt_ IMFSample *            pSample,
        # _In_ IMFMediaBuffer *           pMFMediaBuffer,
        # _In_ DWORD                      cbOffset,
        # _Outptr_ IMediaBuffer **     ppMediaBuffer );
        MFCreateLegacyMediaBufferOnMFMediaBuffer = (
            mfplat.MFCreateLegacyMediaBufferOnMFMediaBuffer
        )

        # Create a DirectX surface buffer
        from pyWinAPI.shared.dxgiformat_h import * # NOQA

        # STDAPI_(DXGI_FORMAT) MFMapDX9FormatToDXGIFormat( _In_ DWORD dx9 );
        MFMapDX9FormatToDXGIFormat = mfplat.MFMapDX9FormatToDXGIFormat
        MFMapDX9FormatToDXGIFormat.restype = DXGI_FORMAT

        # STDAPI_(DWORD) MFMapDXGIFormatToDX9Format( _In_ DXGI_FORMAT dx11 );
        MFMapDXGIFormatToDX9Format = mfplat.MFMapDXGIFormatToDX9Format
        MFMapDXGIFormatToDX9Format.restype = DWORD

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFLockDXGIDeviceManager(
        # _Out_opt_ UINT* pResetToken,
        # _Outptr_ IMFDXGIDeviceManager** ppManager
        # );
        MFLockDXGIDeviceManager = mfplat.MFLockDXGIDeviceManager
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        evr = ctypes.windll.EVR
        # STDAPI MFCreateDXSurfaceBuffer(
        # _In_ REFIID                     riid,
        # _In_ IUnknown *                 punkSurface,
        # _In_ BOOL                       fBottomUpWhenLinear,
        # _Outptr_ IMFMediaBuffer **   ppBuffer );
        MFCreateDXSurfaceBuffer = evr.MFCreateDXSurfaceBuffer

        # STDAPI MFCreateWICBitmapBuffer(
        # _In_ REFIID                     riid,
        # _In_ IUnknown *                 punkSurface,
        # _Outptr_ IMFMediaBuffer **   ppBuffer
        # );
        MFCreateWICBitmapBuffer = mfplat.MFCreateWICBitmapBuffer
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):

        # STDAPI
        # MFCreateDXGISurfaceBuffer(
        # _In_ REFIID riid,
        # _In_ IUnknown* punkSurface,
        # _In_ UINT uSubresourceIndex,
        # _In_ BOOL fBottomUpWhenLinear,
        # _Outptr_ IMFMediaBuffer** ppBuffer
        # );
        MFCreateDXGISurfaceBuffer = mfplat.MFCreateDXGISurfaceBuffer

        # STDAPI MFCreateVideoSampleAllocatorEx(
        # _In_   REFIID riid,
        # _Outptr_  void** ppSampleAllocator
        # );
        MFCreateVideoSampleAllocatorEx = mfplat.MFCreateVideoSampleAllocatorEx

        # STDAPI
        # MFCreateDXGIDeviceManager(
        # _Out_ UINT* resetToken,
        # _Outptr_ IMFDXGIDeviceManager** ppDeviceManager
        # );
        MFCreateDXGIDeviceManager = mfplat.MFCreateDXGIDeviceManager
        MF_E_DXGI_DEVICE_NOT_INITIALIZED = 0x80041000        # DXVA2_E_NOT_INITIALIZED
        MF_E_DXGI_NEW_VIDEO_DEVICE = 0x80041001        # DXVA2_E_NEW_VIDEO_DEVICE
        MF_E_DXGI_VIDEO_DEVICE_LOCKED = 0x80041002        # DXVA2_E_VIDEO_DEVICE_LOCKED

        # Create an aligned memory buffer.
        # The following constants were chosen for parity with the alignment
        # constants
        # in ntioapi.h
        MF_1_BYTE_ALIGNMENT = 0x00000000
        MF_2_BYTE_ALIGNMENT = 0x00000001
        MF_4_BYTE_ALIGNMENT = 0x00000003
        MF_8_BYTE_ALIGNMENT = 0x00000007
        MF_16_BYTE_ALIGNMENT = 0x0000000F
        MF_32_BYTE_ALIGNMENT = 0x0000001F
        MF_64_BYTE_ALIGNMENT = 0x0000003F
        MF_128_BYTE_ALIGNMENT = 0x0000007F
        MF_256_BYTE_ALIGNMENT = 0x000000FF
        MF_512_BYTE_ALIGNMENT = 0x000001FF
        MF_1024_BYTE_ALIGNMENT = 0x000003FF
        MF_2048_BYTE_ALIGNMENT = 0x000007FF
        MF_4096_BYTE_ALIGNMENT = 0x00000FFF
        MF_8192_BYTE_ALIGNMENT = 0x00001FFF

        # STDAPI MFCreateAlignedMemoryBuffer(
        # _In_ DWORD                      cbMaxLength,
        # _In_ DWORD                      cbAligment,
        # _Out_ IMFMediaBuffer **         ppBuffer );
        MFCreateAlignedMemoryBuffer = mfplat.MFCreateAlignedMemoryBuffer
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # This GUID is used in IMFGetService::GetService calls to retrieve
        # interfaces from the buffer. Its value is defined in evr.h
        # /////////////////////////////////////////////////////////////////////
        # /////////////////////////////// Events //////////////////////////////
        # /////////////////////////////////////////////////////////////////////
        # Instantiates the MF-provided Media Event implementation.
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFCreateMediaEvent(
        # _In_ MediaEventType met,
        # _In_ REFGUID guidExtendedType,
        # _In_ HRESULT hrStatus,
        # _In_opt_ PROPVARIANT * pvValue,
        # _Out_ IMFMediaEvent ** ppEvent );

        MFCreateMediaEvent = mfplat.MFCreateMediaEvent
        # Instantiates an object that implements IMFMediaEventQueue.
        # Components that provide an IMFMediaEventGenerator can use this object
        # internally to do their Media Event Generator work for them.
        # IMFMediaEventGenerator calls should be forwarded to the similar call
        # on this object's IMFMediaEventQueue interface (e.g. BeginGetEvent,
        # EndGetEvent), and the various IMFMediaEventQueue::QueueEventXXX methods
        #
        # can be used to queue events that the caller will consume.
        # STDAPI MFCreateEventQueue(
        # _Out_ IMFMediaEventQueue **ppMediaEventQueue );
        MFCreateEventQueue = mfplat.MFCreateEventQueue
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Event attributes
        # Some of the common Media Foundation events have associated attributes
        # that go in their IMFAttributes stores
        # MESessionCapabilitiesChanged attributes
        # MF_EVENT_SESSIONCAPS {7E5EBCD0-11B8-4abe-AFAD-10F6599A7F42}
        # Type: UINT32
        MF_EVENT_SESSIONCAPS = DEFINE_GUID(
            0x7E5EBCD0,
            0x11B8,
            0x4ABE,
            0xAF,
            0xAD,
            0x10,
            0xF6,
            0x59,
            0x9A,
            0x7F,
            0x42
        )

        # MF_EVENT_SESSIONCAPS_DELTA {7E5EBCD1-11B8-4abe-AFAD-10F6599A7F42}
        # Type: UINT32
        MF_EVENT_SESSIONCAPS_DELTA = DEFINE_GUID(
            0x7E5EBCD1,
            0x11B8,
            0x4ABE,
            0xAF,
            0xAD,
            0x10,
            0xF6,
            0x59,
            0x9A,
            0x7F,
            0x42
        )

        # Session capabilities bitflags
        MFSESSIONCAP_START = 0x00000001
        MFSESSIONCAP_SEEK = 0x00000002
        MFSESSIONCAP_PAUSE = 0x00000004
        MFSESSIONCAP_RATE_FORWARD = 0x00000010
        MFSESSIONCAP_RATE_REVERSE = 0x00000020
        MFSESSIONCAP_DOES_NOT_USE_NETWORK = 0x00000040

        # MESessionTopologyStatus attributes
        # Possible values for MF_EVENT_TOPOLOGY_STATUS attribute.
        # For a given topology, these status values will arrive via
        # MESessionTopologyStatus in the order below.
        # However, there are no guarantees about how these status values will
        # be
        # ordered between two consecutive topologies. For example,
        # MF_TOPOSTATUS_READY could arrive for topology n + 1 before
        # MF_TOPOSTATUS_ENDED arrives for topology n if the application called
        # IMFMediaSession::SetTopology for topology n + 1 well enough in
        # advance of the
        # end of topology n. Conversely, if topology n ends before the
        # application
        # calls IMFMediaSession::SetTopology for topology n + 1, then
        # MF_TOPOSTATUS_ENDED will arrive for topology n before
        # MF_TOPOSTATUS_READY
        # arrives for topology n + 1.
        class MF_TOPOSTATUS(ENUM):
            MF_TOPOSTATUS_INVALID = 0
            MF_TOPOSTATUS_READY = 100
            MF_TOPOSTATUS_STARTED_SOURCE = 200
            if WINVER >= _WIN32_WINNT_WIN7:
                MF_TOPOSTATUS_DYNAMIC_CHANGED = 210
            # END IF

            MF_TOPOSTATUS_SINK_SWITCHED = 300
            MF_TOPOSTATUS_ENDED = 400

        MF_TOPOSTATUS_INVALID = MF_TOPOSTATUS.MF_TOPOSTATUS_INVALID
        MF_TOPOSTATUS_READY = MF_TOPOSTATUS.MF_TOPOSTATUS_READY
        MF_TOPOSTATUS_STARTED_SOURCE = MF_TOPOSTATUS.MF_TOPOSTATUS_STARTED_SOURCE

        if WINVER >= _WIN32_WINNT_WIN7:
            MF_TOPOSTATUS_DYNAMIC_CHANGED = MF_TOPOSTATUS.MF_TOPOSTATUS_DYNAMIC_CHANGED
        # END IF

        MF_TOPOSTATUS_SINK_SWITCHED = MF_TOPOSTATUS.MF_TOPOSTATUS_SINK_SWITCHED
        MF_TOPOSTATUS_ENDED = MF_TOPOSTATUS.MF_TOPOSTATUS_ENDED

        # MF_EVENT_TOPOLOGY_STATUS {30C5018D-9A53-454b-AD9E-6D5F8FA7C43B}
        # Type: UINT32 {MF_TOPOLOGY_STATUS}
        MF_EVENT_TOPOLOGY_STATUS = DEFINE_GUID(
            0x30C5018D,
            0x9A53,
            0x454B,
            0xAD,
            0x9E,
            0x6D,
            0x5F,
            0x8F,
            0xA7,
            0xC4,
            0x3B
        )

        # MESessionNotifyPresentationTime attributes
        # MF_EVENT_START_PRESENTATION_TIME
        # {5AD914D0-9B45-4a8d-A2C0-81D1E50BFB07}
        # Type: UINT64
        MF_EVENT_START_PRESENTATION_TIME = DEFINE_GUID(
            0x5AD914D0,
            0x9B45,
            0x4A8D,
            0xA2,
            0xC0,
            0x81,
            0xD1,
            0xE5,
            0xB,
            0xFB,
            0x7
        )

        # MF_EVENT_PRESENTATION_TIME_OFFSET
        # {5AD914D1-9B45-4a8d-A2C0-81D1E50BFB07}
        # Type: UINT64
        MF_EVENT_PRESENTATION_TIME_OFFSET = DEFINE_GUID(
            0x5AD914D1,
            0x9B45,
            0x4A8D,
            0xA2,
            0xC0,
            0x81,
            0xD1,
            0xE5,
            0xB,
            0xFB,
            0x7
        )

        # MF_EVENT_START_PRESENTATION_TIME_AT_OUTPUT
        # {5AD914D2-9B45-4a8d-A2C0-81D1E50BFB07}
        # Type: UINT64
        MF_EVENT_START_PRESENTATION_TIME_AT_OUTPUT = DEFINE_GUID(
            0x5AD914D2,
            0x9B45,
            0x4A8D,
            0xA2,
            0xC0,
            0x81,
            0xD1,
            0xE5,
            0xB,
            0xFB,
            0x7
        )

        # MESourceStarted attributes
        # MF_EVENT_SOURCE_FAKE_START {a8cc55a7-6b31-419f-845d-ffb351a2434b}
        # Type: UINT32
        MF_EVENT_SOURCE_FAKE_START = DEFINE_GUID(
            0xA8CC55A7,
            0x6B31,
            0x419F,
            0x84,
            0x5D,
            0xFF,
            0xB3,
            0x51,
            0xA2,
            0x43,
            0x4B
        )

        # MF_EVENT_SOURCE_PROJECTSTART {a8cc55a8-6b31-419f-845d-ffb351a2434b}
        # Type: UINT64
        MF_EVENT_SOURCE_PROJECTSTART = DEFINE_GUID(
            0xA8CC55A8,
            0x6B31,
            0x419F,
            0x84,
            0x5D,
            0xFF,
            0xB3,
            0x51,
            0xA2,
            0x43,
            0x4B
        )

        # MF_EVENT_SOURCE_ACTUAL_START {a8cc55a9-6b31-419f-845d-ffb351a2434b}
        # Type: UINT64
        MF_EVENT_SOURCE_ACTUAL_START = DEFINE_GUID(
            0xA8CC55A9,
            0x6B31,
            0x419F,
            0x84,
            0x5D,
            0xFF,
            0xB3,
            0x51,
            0xA2,
            0x43,
            0x4B
        )

        # MEEndOfPresentationSegment attributes
        # MF_EVENT_SOURCE_TOPOLOGY_CANCELED
        # {DB62F650-9A5E-4704-ACF3-563BC6A73364}
        # Type: UINT32
        MF_EVENT_SOURCE_TOPOLOGY_CANCELED = DEFINE_GUID(
            0xDB62F650,
            0x9A5E,
            0x4704,
            0xAC,
            0xF3,
            0x56,
            0x3B,
            0xC6,
            0xA7,
            0x33,
            0x64
        )

        # MESourceCharacteristicsChanged attributes
        # MF_EVENT_SOURCE_CHARACTERISTICS
        # {47DB8490-8B22-4f52-AFDA-9CE1B2D3CFA8}
        # Type: UINT32
        MF_EVENT_SOURCE_CHARACTERISTICS = DEFINE_GUID(
            0x47DB8490,
            0x8B22,
            0x4F52,
            0xAF,
            0xDA,
            0x9C,
            0xE1,
            0xB2,
            0xD3,
            0xCF,
            0xA8
        )

        # MF_EVENT_SOURCE_CHARACTERISTICS_OLD
        # {47DB8491-8B22-4f52-AFDA-9CE1B2D3CFA8}
        # Type: UINT32
        MF_EVENT_SOURCE_CHARACTERISTICS_OLD = DEFINE_GUID(
            0x47DB8491,
            0x8B22,
            0x4F52,
            0xAF,
            0xDA,
            0x9C,
            0xE1,
            0xB2,
            0xD3,
            0xCF,
            0xA8
        )

        # MESourceRateChangeRequested attributes
        # MF_EVENT_DO_THINNING {321EA6FB-DAD9-46e4-B31D-D2EAE7090E30}
        # Type: UINT32
        MF_EVENT_DO_THINNING = DEFINE_GUID(
            0x321EA6FB,
            0xDAD9,
            0x46E4,
            0xB3,
            0x1D,
            0xD2,
            0xEA,
            0xE7,
            0x9,
            0xE,
            0x30
        )

        # MEStreamSinkScrubSampleComplete attributes
        # MF_EVENT_SCRUBSAMPLE_TIME {9AC712B3-DCB8-44d5-8D0C-37455A2782E3}
        # Type: UINT64
        MF_EVENT_SCRUBSAMPLE_TIME = DEFINE_GUID(
            0x9AC712B3,
            0xDCB8,
            0x44D5,
            0x8D,
            0xC,
            0x37,
            0x45,
            0x5A,
            0x27,
            0x82,
            0xE3
        )

        # MESinkInvalidated and MESessionStreamSinkFormatChanged attributes
        # MF_EVENT_OUTPUT_NODE {830f1a8b-c060-46dd-a801-1c95dec9b107}
        # Type: UINT64
        MF_EVENT_OUTPUT_NODE = DEFINE_GUID(
            0x830F1A8B,
            0xC060,
            0x46DD,
            0xA8,
            0x01,
            0x1C,
            0x95,
            0xDE,
            0xC9,
            0xB1,
            0x07
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if WINVER >= _WIN32_WINNT_WIN7:
            # METransformNeedInput attributes
            # MF_EVENT_MFT_INPUT_STREAM_ID
            # {F29C2CCA-7AE6-42d2-B284-BF837CC874E2}
            # Type: UINT32
            MF_EVENT_MFT_INPUT_STREAM_ID = DEFINE_GUID(
                0xF29C2CCA,
                0x7AE6,
                0x42D2,
                0xB2,
                0x84,
                0xBF,
                0x83,
                0x7C,
                0xC8,
                0x74,
                0xE2
            )

            # METransformDrainComplete and METransformMarker attributes
            # MF_EVENT_MFT_CONTEXT {B7CD31F1-899E-4b41-80C9-26A896D32977}
            # Type: UINT64
            MF_EVENT_MFT_CONTEXT = DEFINE_GUID(
                0xB7CD31F1,
                0x899E,
                0x4B41,
                0x80,
                0xC9,
                0x26,
                0xA8,
                0x96,
                0xD3,
                0x29,
                0x77
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINVER >= _WIN32_WINNT_WINBLUE:
            # MEContentProtectionMetadata attributes
            # MF_EVENT_STREAM_METADATA_KEYDATA
            # {CD59A4A1-4A3B-4BBD-8665-72A40FBEA776}
            # Type: BLOB
            MF_EVENT_STREAM_METADATA_KEYDATA = DEFINE_GUID(
                0xCD59A4A1,
                0x4A3B,
                0x4BBD,
                0x86,
                0x65,
                0x72,
                0xA4,
                0xF,
                0xBE,
                0xA7,
                0x76
            )

            # MF_EVENT_STREAM_METADATA_CONTENT_KEYIDS
            # {5063449D-CC29-4FC6-A75A-D247B35AF85C}
            # Type: BLOB
            MF_EVENT_STREAM_METADATA_CONTENT_KEYIDS = DEFINE_GUID(
                0x5063449D,
                0xCC29,
                0x4FC6,
                0xA7,
                0x5A,
                0xD2,
                0x47,
                0xB3,
                0x5A,
                0xF8,
                0x5C
            )

            # MF_EVENT_STREAM_METADATA_SYSTEMID
            # {1EA2EF64-BA16-4A36-8719-FE7560BA32AD}
            # Type: BLOB
            MF_EVENT_STREAM_METADATA_SYSTEMID = DEFINE_GUID(
                0x1EA2EF64,
                0xBA16,
                0x4A36,
                0x87,
                0x19,
                0xFE,
                0x75,
                0x60,
                0xBA,
                0x32,
                0xAD
            )
        # END IF   (WINVER >= _WIN32_WINNT_WINBLUE)

        # //////////////////////////////////////////////////////////////////////////////
        #
        # ///////////////////////////// Samples
        # //////////////////////////////////////
        # //////////////////////////////////////////////////////////////////////////////
        #
        # Creates an instance of the Media Foundation implementation of
        # IMFSample

        # STDAPI MFCreateSample( _Out_ IMFSample **ppIMFSample );
        MFCreateSample = mfplat.MFCreateSample
        # Sample attributes
        # These are the well-known attributes that can be present on an MF
        # Sample's
        # IMFAttributes store
        # @@MFSampleExtension_MaxDecodeFrameSize
        # / <summary>
        # {D3CC654F-F9F3-4A13-889F-F04EB2B5B957}
        # MFSampleExtension_MaxDecodeFrameSize
        # {UINT64 (HI32(Width),LO32(Height))}
        # specify the maxiumum resolution of compressed input bitstream,
        # the decoder shall decode any comressed pictures below the specified
        # maximum resolution
        # any input compressed pictures beyond the maximum resolution shall
        # not be decoded and dropped by the decoder
        # the attribute shall be set on input sample
        # / </summary>
        MFSampleExtension_MaxDecodeFrameSize = DEFINE_GUID(
            0xD3CC654F,
            0xF9F3,
            0x4A13,
            0x88,
            0x9F,
            0xF0,
            0x4E,
            0xB2,
            0xB5,
            0xB9,
            0x57
        )

        # @@MFSampleExtension_AccumulatedNonRefPicPercent
        # / <summary>
        # {79EA74DF-A740-445B-BC98-C9ED1F260EEE}
        # MFSampleExtension_AccumulatedNonRefPicPercent
        # Type: UINT32
        # specify the percentage of accumulated non-reference pictures up to
        # this output sample in decoding order
        # The most common examples are,
        # 1. if the sequence has the GOP structure of IPPPP......, the value
        # will be 0
        # 2. if the sequence has the GOP structure of IPBPB......, the
        # percentage will be around 40%~50%. The value is 40~50.
        # 3. if the sequence has the GOP structure of IPBBPBB......, the
        # percentage will be around 50%~66%. The value is 50~60.
        # where B frames are not used for reference.
        # This is some statistic to application or pipeline whether decoder
        # alone can have graceful degradation on quality management
        # In the above example,
        # 1. Decoder alone can't have graceful quality management. Because it
        # can only have full frame rate or 1/15 of full frame rate when GOP
        # size is 15 frames or 1/30 when GOP size is 30 frames
        # 2. Decoder alone can have quality management. Because it can have
        # full frame rate or 1/2 of full frame rate or 1/GOPSize
        # 2. Decoder alone can have quality management. Because it can have
        # full frame rate, or down to 1/3 of full frame rate or 1/GOPSize
        # the attribute could be set on output sample from decoders
        # / </summary>
        # {79EA74DF-A740-445B-BC98-C9ED1F260EEE}
        MFSampleExtension_AccumulatedNonRefPicPercent = DEFINE_GUID(
            0x79EA74DF,
            0xA740,
            0x445B,
            0xBC,
            0x98,
            0xC9,
            0xED,
            0x1F,
            0x26,
            0xE,
            0xEE
        )

        # //////////////////////////////////////////////////////////////////////////////
        #
        # Sample extensions for SAMPLE-AES encryption
        # MFSampleExtension_Encryption_ProtectionScheme
        # {D054D096-28BB-45DA-87EC-74F351871406}
        # Type: UINT32
        # Specifies the cipher and mode used to encrypt the content
        MFSampleExtension_Encryption_ProtectionScheme = DEFINE_GUID(
            0xD054D096,
            0x28BB,
            0x45DA,
            0x87,
            0xEC,
            0x74,
            0xF3,
            0x51,
            0x87,
            0x14,
            0x6
        )


        class _MFSampleEncryptionProtectionScheme(ENUM):
            MF_SAMPLE_ENCRYPTION_PROTECTION_SCHEME_NONE = 0
            MF_SAMPLE_ENCRYPTION_PROTECTION_SCHEME_AES_CTR = 1
            MF_SAMPLE_ENCRYPTION_PROTECTION_SCHEME_AES_CBC = 2

        MFSampleEncryptionProtectionScheme = _MFSampleEncryptionProtectionScheme

        # MFSampleExtension_Encryption_CryptByteBlock
        # {9D84289B-0C7F-4713-AB95-108AB42AD801}
        # Type: UINT32
        # Represents the number of encrypted blocks in the protection pattern,
        # where each block is 16 bytes.
        MFSampleExtension_Encryption_CryptByteBlock = DEFINE_GUID(
            0x9D84289B,
            0xC7F,
            0x4713,
            0xAB,
            0x95,
            0x10,
            0x8A,
            0xB4,
            0x2A,
            0xD8,
            0x1
        )

        # MFSampleExtension_Encryption_SkipByteBlock
        # {0D550548-8317-4AB1-845F-D06306E293E3}
        # Type: UINT32
        # Represents the number of unencrypted blocks in the protection
        # pattern, where each block is 16 bytes.
        MFSampleExtension_Encryption_SkipByteBlock = DEFINE_GUID(
            0xD550548,
            0x8317,
            0x4AB1,
            0x84,
            0x5F,
            0xD0,
            0x63,
            0x6,
            0xE2,
            0x93,
            0xE3
        )

        # //////////////////////////////////////////////////////////////////////////////
        #
        # Attributes for HW-DRM support
        # @@MFSampleExtension_Encryption_SubSample_Mapping
        # / <summary>
        # / The data blob associated with this attribute should contain an
        # array of byte
        # / ranges as DWORDs where every two DWORDs make a set. The first
        # DWORD in each set
        # / is the number of clear bytes and the second DWORD of the set is
        # the number of
        # / encrypted bytes.
        # / Note that a pair of 0s is not a valid set
        # (either value can be 0, but not both).
        # / The array of byte ranges that indicate which ranges to decrypt,
        # including the
        # / possibility that the entire sample should NOT be decrypted.
        # / It must be set on an IMFSample using SetBlob
        # / </summary>
        MFSampleExtension_Encryption_SubSample_Mapping = DEFINE_GUID(
            0x8444F27A,
            0x69A1,
            0x48DA,
            0xBD,
            0x08,
            0x11,
            0xCE,
            0xF3,
            0x68,
            0x30,
            0xD2
        )

        # MFSampleExtension_Encryption_ClearSliceHeaderData
        # {5509A4F4-320D-4E6C-8D1A-94C66DD20CB0}
        # /* The MF blob should be parsed in the way below defined in
        # SliceHeaderSet, with proper verifications == == == == == == == == ==
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == == == == == == == == == =
        # Note the slice header data here DO NOT have all bits for all the
        # syntaxes. Some bits are removed on purpose to send out a lossy
        # compressed slice header in order to be 100% secure The partial slice
        # header data here SHALL not include any bits for emulation prevention
        # byte 0x03 == == == == == == == == = typedef struct SliceHeader_tag
        # { WORD dSliceHeaderLen; // indicate the length of the following slice header in byte, it shall not be more than 1024 BYTE SliceHeaderBytes[0]; // slice header data, the last byte might contain some bits not used, leave them random } SliceHeader; With dSliceHeaderLen bytes serialized after the SliceHeader struct. And then use an array of these serialized consecutively, typedef struct SliceHeaderSet_tag { WORD dNumHeaders; // indicate the number of slice headers in the input sample SliceHeader rgstSliceheader[0]; // cNumHeaders slice header data } SliceHeaderSet;
        #
        # Type: BLOB
        MFSampleExtension_Encryption_ClearSliceHeaderData = DEFINE_GUID(
            0x5509A4F4,
            0x320D,
            0x4E6C,
            0x8D,
            0x1A,
            0x94,
            0xC6,
            0x6D,
            0xD2,
            0xC,
            0xB0
        )

        # MFSampleExtension_Encryption_HardwareProtection_KeyInfoID
        # {8CBFCCEB-94A5-4DE1-8231-A85E47CF81E7}
        # Type: GUID
        # This attribute applies to media samples. The GUID associated with
        # this
        # attribute indicates an identifier (KID/LID) for the hardware
        # protection to be
        # used for the given sample. All hardware protected samples flowing
        # out of the
        # MFT decryptor should have this attribute set with the proper GUID.
        MFSampleExtension_Encryption_HardwareProtection_KeyInfoID = DEFINE_GUID(
            0x8CBFCCEB,
            0x94A5,
            0x4DE1,
            0x82,
            0x31,
            0xA8,
            0x5E,
            0x47,
            0xCF,
            0x81,
            0xE7
        )

        # MFSampleExtension_Encryption_HardwareProtection_KeyInfo
        # {B2372080-455B-4DD7-9989-1A955784B754}
        # Type: BLOB
        # This attribute applies to media samples. The data blob associated
        # with this
        # sample has all the information relative to the slot/ID for the
        # hardware
        # protection to be used for the given sample. All hardware protected
        # samples
        # flowing out of the MFT decryptor should have this attribute set with
        # the
        # proper blob.
        MFSampleExtension_Encryption_HardwareProtection_KeyInfo = DEFINE_GUID(
            0xB2372080,
            0x455B,
            0x4DD7,
            0x99,
            0x89,
            0x1A,
            0x95,
            0x57,
            0x84,
            0xB7,
            0x54
        )

        # MFSampleExtension_Encryption_HardwareProtection_VideoDecryptorContext {693470C8-E837-47A0-88CB-535B905E3582}
        #
        # Data type: IUnknown * (IMFContentDecryptorContext)
        # This attribute applies to media samples. It associates a sample with
        # a
        # given IMFContentDecryptorContext which is needed to be able to to
        # decrypt/decode the sample properly when using hardware protection.
        MFSampleExtension_Encryption_HardwareProtection_VideoDecryptorContext = DEFINE_GUID(
            0x693470C8,
            0xE837,
            0x47A0,
            0x88,
            0xCB,
            0x53,
            0x5B,
            0x90,
            0x5E,
            0x35,
            0x82
        )

        # MFSampleExtension_Encryption_Opaque_Data
        # {224D77E5-1391-4FFB-9F41-B432F68C611D}
        # Data type : BLOB
        # This attribute applies to media samples.The data blob associated
        # with this sample has some private information
        # set by OEM secure environment to be used for the given sample.The
        # hardware protected samples flowing out of the
        # MFT decryptor might have this attribute set with the proper blob.
        # When present, this attribute is set by the decryptor MFT with data
        # that originates from the OEM secure environment.
        # The host decoder may extract this and provide the data to the D3D11
        # device for VLD decoding
        # through(UINT PrivateDataSize, void* pPrivateData)
        # of D3D11_VIDEO_DECODER_BEGIN_FRAME_CRYPTO_SESSION data structure in
        # the DecoderBeginFrame() call, when present.
        MFSampleExtension_Encryption_Opaque_Data = DEFINE_GUID(
            0x224D77E5,
            0x1391,
            0x4FFB,
            0x9F,
            0x41,
            0xB4,
            0x32,
            0xF6,
            0x8C,
            0x61,
            0x1D
        )

        # MFSampleExtension_NALULengthInfo. This is an alias of
        # MF_NALU_LENGTH_INFORMATION
        # Type: BLOB
        # Set MFSampleExtension_NALULengthInfo as a BLOB on the input sample,
        # with one DWORD for each NALU including start code and NALU type in
        # the sample. For example, if
        # there are AUD (9 bytes), SPS (25 bytes), PPS (10 bytes), IDR slice1
        # (50 k), IDR slice 2 (60 k),
        # then there should be 5 DWORDs with values 9, 25, 10, 50 k, 60 k in
        # the BLOB.
        MFSampleExtension_NALULengthInfo = DEFINE_GUID(
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

        # MFSampleExtension_Encryption_ResumeVideoOutput.
        # {A435ABA5-AFDE-4CF5-BC1C-F6ACAF13949D}
        # Type: UINT32
        # This attribute shall be used in hardware DRM scenario only
        # it is set on input compressed sample to (H.264/HEVC) video decoder
        # when present, it indicates video output in video render should
        # resume on the first output (uncompressed) sample
        # with the attribute MFSampleExtension_Encryption_ResumeVideoOutput
        # set to true
        # note: (H.264/HEVC) video decoder should buffer the attribute when
        # video decoder
        # detects the attribute set to true on some input sample, which might
        # be dropped since
        # those input sample might not be decode-able because of missing
        # references,
        # and set the attribute to true on the first output sample not dropped
        # in video decoder
        MFSampleExtension_Encryption_ResumeVideoOutput = DEFINE_GUID(
            0xA435ABA5,
            0xAFDE,
            0x4CF5,
            0xBC,
            0x1C,
            0xF6,
            0xAC,
            0xAF,
            0x13,
            0x94,
            0x9D
        )

        # MFSampleExtension_Encryption_NALUTypes.
        # {B0F067C7-714C-416C-8D59-5F4DDF8913B6}
        # Type: BLOB
        # The MF blob contains all the NALU type byte for different NALUs in
        # the MF sample.One NALU type is one byte, including the syntaxes
        # forbidden_zero_bit, nal_ref_idc, and nal_unit_type.
        MFSampleExtension_Encryption_NALUTypes = DEFINE_GUID(
            0xB0F067C7,
            0x714C,
            0x416C,
            0x8D,
            0x59,
            0x5F,
            0x4D,
            0xDF,
            0x89,
            0x13,
            0xB6
        )

        # MFSampleExtension_Encryption_SPSPPSData
        # {AEDE0FA2-0E0C-453C-B7F3-DE8693364D11}
        # Type : BLOB
        # When present, the MF blob contains all SPS(s) and / or PPS(s) NALUs
        # inside the MF sample.
        # SPSs and PPSs shall be present in the same order as that in the MF
        # sample and in the format of AvcC,
        # which is DWORD, four - byte length inforamtion for the bytes
        # followed, and NALU data of SPS or PPS, for each NALU.
        # For example, the layout could be 10 in DWORD, 10 bytes data for SPS,
        # 5 in DWORD, and 5 bytes data for PPS.In total, it has 4 + 10 + 4 + 5
        # = 23 bytes.
        MFSampleExtension_Encryption_SPSPPSData = DEFINE_GUID(
            0xAEDE0FA2,
            0xE0C,
            0x453C,
            0xB7,
            0xF3,
            0xDE,
            0x86,
            0x93,
            0x36,
            0x4D,
            0x11
        )

        # MFSampleExtension_Encryption_SEIData
        # {3CF0E972-4542-4687-9999-585F565FBA7D}
        # Type : BLOB
        # When present, the MF blob contains all SEI NALUs inside the MF
        # sample.
        # (If there are multiple SEIs in the protected MF sample, all the SEIs shall be present in the blob.)
        #
        # SEIs shall be present in the same order as that in the MF sample and
        # in the format of AvcC,
        # which is DWORD, four - byte length inforamtion for the bytes
        # followed, and NALU data of SEI.
        # For example, the layout could be 10 in DWORD, 10 bytes data for the
        # first SEI, 5 in DWORD, and 5 bytes data for the second SEI.In total,
        # it has 4 + 10 + 4 + 5 = 23 bytes.
        # Some note about how to process the SEI NALUs in the blob of
        # MFSampleExtension_Encryption_SEIData
        # Decoder should verify every byte of an SEI NALU is clear, not
        # protected, before parsing the SEI NALU
        # otherwise, decoder should treat the SEI NALU as corrupted by
        # encryption and skip the parsing of the SEI NALU
        MFSampleExtension_Encryption_SEIData = DEFINE_GUID(
            0x3CF0E972,
            0x4542,
            0x4687,
            0x99,
            0x99,
            0x58,
            0x5F,
            0x56,
            0x5F,
            0xBA,
            0x7D
        )

        # MFSampleExtension_Encryption_HardwareProtection
        # {9A2B2D2B-8270-43E3-8448-994F426E8886}
        # Type: UINT32
        # When present, this UINT32 attribute indicates whether the sample is
        # hardware protected.
        # 0 = not hardware protected, nonzero = hardware protected
        MFSampleExtension_Encryption_HardwareProtection = DEFINE_GUID(
            0x9A2B2D2B,
            0x8270,
            0x43E3,
            0x84,
            0x48,
            0x99,
            0x4F,
            0x42,
            0x6E,
            0x88,
            0x86
        )

        # MFSampleExtension_CleanPoint {9cdf01d8-a0f0-43ba-b077-eaa06cbd728a}
        # Type: UINT32
        # If present and nonzero, indicates that the sample is a clean point
        # (key
        # frame), and decoding can begin at this sample.
        MFSampleExtension_CleanPoint = DEFINE_GUID(
            0x9CDF01D8,
            0xA0F0,
            0x43BA,
            0xB0,
            0x77,
            0xEA,
            0xA0,
            0x6C,
            0xBD,
            0x72,
            0x8A
        )

        # MFSampleExtension_Discontinuity
        # {9cdf01d9-a0f0-43ba-b077-eaa06cbd728a}
        # Type: UINT32
        # If present and nonzero, indicates that the sample data represents
        # the first
        # sample following a discontinuity (gap) in the stream of samples.
        # This can happen, for instance, if the previous sample was lost in
        # transmission.
        MFSampleExtension_Discontinuity = DEFINE_GUID(
            0x9CDF01D9,
            0xA0F0,
            0x43BA,
            0xB0,
            0x77,
            0xEA,
            0xA0,
            0x6C,
            0xBD,
            0x72,
            0x8A
        )

        # MFSampleExtension_Token {8294da66-f328-4805-b551-00deb4c57a61}
        # Type: IUNKNOWN
        # When an IMFMediaStream delivers a sample via MEMediaStream, this
        # attribute
        # should be set to the IUnknown *pToken argument that was passed with
        # the
        # IMFMediaStream::RequestSample call to which this sample corresponds.
        MFSampleExtension_Token = DEFINE_GUID(
            0x8294DA66,
            0xF328,
            0x4805,
            0xB5,
            0x51,
            0x00,
            0xDE,
            0xB4,
            0xC5,
            0x7A,
            0x61
        )

        # MFSampleExtension_ClosedCaption_CEA708
        # {26f09068-e744-47dc-aa03-dbf20403bde6}
        # Type: BLOB
        # MF sample attribute contained the closed caption data in CEA-708
        # format.
        MFSampleExtension_ClosedCaption_CEA708 = DEFINE_GUID(
            0x26F09068,
            0xE744,
            0x47DC,
            0xAA,
            0x03,
            0xDB,
            0xF2,
            0x04,
            0x03,
            0xBD,
            0xE6
        )
        MFSampleExtension_ClosedCaption_CEA708_MAX_SIZE = 256

        # MFSampleExtension_DecodeTimestamp
        # {73A954D4-09E2-4861-BEFC-94BD97C08E6E}
        # Type : UINT64
        # If present, contains the DTS (Decoding Time Stamp) of the sample.
        MFSampleExtension_DecodeTimestamp = DEFINE_GUID(
            0x73A954D4,
            0x9E2,
            0x4861,
            0xBE,
            0xFC,
            0x94,
            0xBD,
            0x97,
            0xC0,
            0x8E,
            0x6E
        )

        # MFSampleExtension_VideoEncodeQP
        # {B2EFE478-F979-4C66-B95E-EE2B82C82F36}
        # Type: UINT64
        # Used by video encoders to specify the QP used to encode the output
        # sample.
        MFSampleExtension_VideoEncodeQP = DEFINE_GUID(
            0xB2EFE478,
            0xF979,
            0x4C66,
            0xB9,
            0x5E,
            0xEE,
            0x2B,
            0x82,
            0xC8,
            0x2F,
            0x36
        )

        # MFSampleExtension_VideoEncPictureType
        # {973704E6-CD14-483C-8F20-C9FC0928BAD5}
        # Type: UINT32
        # Used by video encoders to specify the output sample's picture type.
        MFSampleExtension_VideoEncodePictureType = DEFINE_GUID(
            0x973704E6,
            0xCD14,
            0x483C,
            0x8F,
            0x20,
            0xC9,
            0xFC,
            0x9,
            0x28,
            0xBA,
            0xD5
        )

        # MFSampleExtension_FrameCorruption
        # {B4DD4A8C-0BEB-44C4-8B75-B02B913B04F0}
        # Type: UINT32
        # Indicates whether the frame in the sample has corruption or not
        # value 0 indicates that there is no corruption, or it is unknown
        # Value 1 indicates that some corruption was detected e.g, during
        # decoding
        MFSampleExtension_FrameCorruption = DEFINE_GUID(
            0xB4DD4A8C,
            0xBEB,
            0x44C4,
            0x8B,
            0x75,
            0xB0,
            0x2B,
            0x91,
            0x3B,
            0x4,
            0xF0
        )
        if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
            # MFSampleExtension_DirtyRects
            # {9BA70225-B342-4E97-9126-0B566AB7EA7E}
            # Type: BLOB
            # This is a blob containing information about the dirty rectangles
            # within
            # a frame. The blob is a struct of type DIRTYRECT_INFO containing
            # an array
            # of NumDirtyRects number of DirtyRects elements.
            MFSampleExtension_DirtyRects = DEFINE_GUID(
                0x9BA70225,
                0xB342,
                0x4E97,
                0x91,
                0x26,
                0x0B,
                0x56,
                0x6A,
                0xB7,
                0xEA,
                0x7E
            )

            # MFSampleExtension_MoveRegions
            # {E2A6C693-3A8B-4B8D-95D0-F60281A12FB7}
            # Type: BLOB
            # This is a blob containing information about the moved regions
            # within
            # a frame. The blob is a struct of type MOVEREGION_INFO containing
            # an array
            # of NumMoveRegions number of MoveRegions elements.
            MFSampleExtension_MoveRegions = DEFINE_GUID(
                0xE2A6C693,
                0x3A8B,
                0x4B8D,
                0x95,
                0xD0,
                0xF6,
                0x02,
                0x81,
                0xA1,
                0x2F,
                0xB7
            )

            _MOVE_RECT._fields_ = [
                ('SourcePoint', POINT),
                ('DestRect', RECT),
            ]

            _DIRTYRECT_INFO._fields_ = [
                ('FrameNumber', UINT),
                ('NumDirtyRects', UINT),
                ('DirtyRects', RECT * 1),
            ]

            _MOVEREGION_INFO._fields_ = [
                ('FrameNumber', UINT),
                ('NumMoveRegions', UINT),
                ('MoveRegions', MOVE_RECT * 1),
            ]

            # MFSampleExtension_HDCP_OptionalHeader
            # Type: BLOB
            # This blob contains LPCM header in front of LPCM sample in a PES
            # packet. It is
            # encrypted when HDCP 2.x frames are sent, and is needed for
            # decryption.
            MFSampleExtension_HDCP_OptionalHeader = DEFINE_GUID(
                0x9A2E7390,
                0x121F,
                0x455F,
                0x83,
                0x76,
                0xC9,
                0x74,
                0x28,
                0xE0,
                0xB5,
                0x40
            )

            # MFSampleExtension_HDCP_FrameCounter
            # Type: BLOB
            # This blob contains the PES_private_data section of a PES packet
            # according to the
            # HDCP 2.2/2.1 specification. This blob should contain the stream
            # counter and
            # input counter.
            MFSampleExtension_HDCP_FrameCounter = DEFINE_GUID(
                0x9D389C60,
                0xF507,
                0x4AA6,
                0xA4,
                0xA,
                0x71,
                0x2,
                0x7A,
                0x2,
                0xF3,
                0xDE
            )

            # MFSampleExtension_HDCP_StreamID
            # {177E5D74-C370-4A7A-95A2-36833C01D0AF}
            # Type: UINT32
            # This UINT32 value is provided to the HDCP Encryptor MFT on each
            # input sample.
            # The Stream ID value allows the HDCP Encryptor MFT to support
            # time-multiplexed
            # encryption of multiple independent streams. An example is using
            # 0 for first
            # display video stream, 1 for second display video stream, 2 for
            # first display audio
            # stream, 3 for second display audio stream.
            # Per the HDCP 2.2 specification, this value is referred to as
            # streamCtr. It is called
            # StreamID here to be more intuitive.
            MFSampleExtension_HDCP_StreamID = DEFINE_GUID(
                0x177E5D74,
                0xC370,
                0x4A7A,
                0x95,
                0xA2,
                0x36,
                0x83,
                0x3C,
                0x01,
                0xD0,
                0xAF
            )

            # MFSampleExtension_Timestamp
            # Type: int64
            # { 1e436999-69be-4c7a-9369-70068c0260cb }
            # MFSampleExtension_Timestamp {INT64 }
            # The timestamp of a sample
            MFSampleExtension_Timestamp = DEFINE_GUID(
                0x1E436999,
                0x69BE,
                0x4C7A,
                0x93,
                0x69,
                0x70,
                0x06,
                0x8C,
                0x02,
                0x60,
                0xCB
            )

            # MFSampleExtension_RepeatFrame
            # {88BE738F-0711-4F42-B458-344AED42EC2F}
            # Type: UINT32
            # This UINT32 when set to 1 indicates that the frame is a repeat
            # of the previous frame
            MFSampleExtension_RepeatFrame = DEFINE_GUID(
                0x88BE738F,
                0x711,
                0x4F42,
                0xB4,
                0x58,
                0x34,
                0x4A,
                0xED,
                0x42,
                0xEC,
                0x2F
            )

            # MFT_ENCODER_ERROR {C8D1EDA4-98E4-41D5-9297-44F53852F90E}
            # Type: GUID
            # This is the GUID of a property that caused the encoder MFT to
            # fail initialization
            MFT_ENCODER_ERROR = DEFINE_GUID(
                0xC8D1EDA4,
                0x98E4,
                0x41D5,
                0x92,
                0x97,
                0x44,
                0xF5,
                0x38,
                0x52,
                0xF9,
                0x0E
            )

            # MFT_GFX_DRIVER_VERSION_ID_Attribute
            # {F34B9093-05E0-4B16-993D-3E2A2CDE6AD3}
            # Type: WSTR
            # For hardware MFTs, this attribute allows the HMFT to report the
            # graphics driver version.
            MFT_GFX_DRIVER_VERSION_ID_Attribute = DEFINE_GUID(
                0xF34B9093,
                0x05E0,
                0x4B16,
                0x99,
                0x3D,
                0x3E,
                0x2A,
                0x2C,
                0xDE,
                0x6A,
                0xD3
            )
        # END IF

        # ///////////////////////////////////////////////////////////////////////////
        #
        # The following sample attributes are used for encrypted samples
        # ///////////////////////////////////////////////////////////////////////////
        #
        # MFSampleExtension_DescrambleData
        # {43483BE6-4903-4314-B032-2951365936FC}
        # Type: UINT64
        MFSampleExtension_DescrambleData = DEFINE_GUID(
            0x43483BE6,
            0x4903,
            0x4314,
            0xB0,
            0x32,
            0x29,
            0x51,
            0x36,
            0x59,
            0x36,
            0xFC
        )

        # MFSampleExtension_SampleKeyID {9ED713C8-9B87-4B26-8297-A93B0C5A8ACC}
        # Type: UINT32
        MFSampleExtension_SampleKeyID = DEFINE_GUID(
            0x9ED713C8,
            0x9B87,
            0x4B26,
            0x82,
            0x97,
            0xA9,
            0x3B,
            0x0C,
            0x5A,
            0x8A,
            0xCC
        )

        # MFSampleExtension_GenKeyFunc {441CA1EE-6B1F-4501-903A-DE87DF42F6ED}
        # Type: UINT64
        MFSampleExtension_GenKeyFunc = DEFINE_GUID(
            0x441CA1EE,
            0x6B1F,
            0x4501,
            0x90,
            0x3A,
            0xDE,
            0x87,
            0xDF,
            0x42,
            0xF6,
            0xED
        )

        # MFSampleExtension_GenKeyCtx {188120CB-D7DA-4B59-9B3E-9252FD37301C}
        # Type: UINT64
        MFSampleExtension_GenKeyCtx = DEFINE_GUID(
            0x188120CB,
            0xD7DA,
            0x4B59,
            0x9B,
            0x3E,
            0x92,
            0x52,
            0xFD,
            0x37,
            0x30,
            0x1C
        )

        # MFSampleExtension_PacketCrossOffsets
        # {2789671D-389F-40BB-90D9-C282F77F9ABD}
        # Type: BLOB
        MFSampleExtension_PacketCrossOffsets = DEFINE_GUID(
            0x2789671D,
            0x389F,
            0x40BB,
            0x90,
            0xD9,
            0xC2,
            0x82,
            0xF7,
            0x7F,
            0x9A,
            0xBD
        )

        # MFSampleExtension_Encryption_SampleID
        # {6698B84E-0AFA-4330-AEB2-1C0A98D7A44D}
        # Type: BLOB
        MFSampleExtension_Encryption_SampleID = DEFINE_GUID(
            0x6698B84E,
            0x0AFA,
            0x4330,
            0xAE,
            0xB2,
            0x1C,
            0x0A,
            0x98,
            0xD7,
            0xA4,
            0x4D
        )

        # MFSampleExtension_Encryption_KeyID
        # {76376591-795F-4DA1-86ED-9D46ECA109A9}
        # Type: BLOB
        MFSampleExtension_Encryption_KeyID = DEFINE_GUID(
            0x76376591,
            0x795F,
            0x4DA1,
            0x86,
            0xED,
            0x9D,
            0x46,
            0xEC,
            0xA1,
            0x09,
            0xA9
        )

        # MFSampleExtension_Content_KeyID
        # {C6C7F5B0-ACCA-415B-87D9-10441469EFC6}
        # Type: GUID
        MFSampleExtension_Content_KeyID = DEFINE_GUID(
            0xC6C7F5B0,
            0xACCA,
            0x415B,
            0x87,
            0xD9,
            0x10,
            0x44,
            0x14,
            0x69,
            0xEF,
            0xC6
        )

        # MFSampleExtension_Encryption_SubSampleMappingSplit
        # {FE0254B9-2AA5-4EDC-99F7-17E89DBF9174}
        # Type: BLOB
        # Specifies the regions of clear and encrypted bytes in the sample
        MFSampleExtension_Encryption_SubSampleMappingSplit = DEFINE_GUID(
            0xFE0254B9,
            0x2AA5,
            0x4EDC,
            0x99,
            0xF7,
            0x17,
            0xE8,
            0x9D,
            0xBF,
            0x91,
            0x74
        )

        # ///////////////////////////////////////////////////////////////////////////
        #
        # MFSample STANDARD EXTENSION ATTRIBUTE GUIDs
        # ///////////////////////////////////////////////////////////////////////////
        #
        # {b1d5830a-deb8-40e3-90fa-389943716461} MFSampleExtension_Interlaced
        # {UINT32 (BOOL)}
        MFSampleExtension_Interlaced = DEFINE_GUID(
            0xB1D5830A,
            0xDEB8,
            0x40E3,
            0x90,
            0xFA,
            0x38,
            0x99,
            0x43,
            0x71,
            0x64,
            0x61
        )

        # {941ce0a3-6ae3-4dda-9a08-a64298340617}
        # MFSampleExtension_BottomFieldFirst {UINT32 (BOOL)}
        MFSampleExtension_BottomFieldFirst = DEFINE_GUID(
            0x941CE0A3,
            0x6AE3,
            0x4DDA,
            0x9A,
            0x08,
            0xA6,
            0x42,
            0x98,
            0x34,
            0x06,
            0x17
        )

        # {304d257c-7493-4fbd-b149-9228de8d9a99}
        # MFSampleExtension_RepeatFirstField {UINT32 (BOOL)}
        MFSampleExtension_RepeatFirstField = DEFINE_GUID(
            0x304D257C,
            0x7493,
            0x4FBD,
            0xB1,
            0x49,
            0x92,
            0x28,
            0xDE,
            0x8D,
            0x9A,
            0x99
        )

        # {9d85f816-658b-455a-bde0-9fa7e15ab8f9} MFSampleExtension_SingleField
        # {UINT32 (BOOL)}
        MFSampleExtension_SingleField = DEFINE_GUID(
            0x9D85F816,
            0x658B,
            0x455A,
            0xBD,
            0xE0,
            0x9F,
            0xA7,
            0xE1,
            0x5A,
            0xB8,
            0xF9
        )

        # {6852465a-ae1c-4553-8e9b-c3420fcb1637}
        # MFSampleExtension_DerivedFromTopField {UINT32 (BOOL)}
        MFSampleExtension_DerivedFromTopField = DEFINE_GUID(
            0x6852465A,
            0xAE1C,
            0x4553,
            0x8E,
            0x9B,
            0xC3,
            0x42,
            0x0F,
            0xCB,
            0x16,
            0x37
        )

        # MFSampleExtension_MeanAbsoluteDifference
        # {1cdbde11-08b4-4311-a6dd-0f9f371907aa}
        # Type: UINT32
        MFSampleExtension_MeanAbsoluteDifference = DEFINE_GUID(
            0x1CDBDE11,
            0x08B4,
            0x4311,
            0xA6,
            0xDD,
            0x0F,
            0x9F,
            0x37,
            0x19,
            0x07,
            0xAA
        )

        # MFSampleExtension_LongTermReferenceFrameInfo
        # {9154733f-e1bd-41bf-81d3-fcd918f71332}
        # Type: UINT32
        MFSampleExtension_LongTermReferenceFrameInfo = DEFINE_GUID(
            0x9154733F,
            0xE1BD,
            0x41BF,
            0x81,
            0xD3,
            0xFC,
            0xD9,
            0x18,
            0xF7,
            0x13,
            0x32
        )

        _ROI_AREA._fields_ = [
            ('rect', RECT),
            ('QPDelta', INT32),
        ]

        # MFSampleExtension_ROIRectangle {3414a438-4998-4d2c-be82-be3ca0b24d43}
        # Type: BLOB
        MFSampleExtension_ROIRectangle = DEFINE_GUID(
            0x3414A438,
            0x4998,
            0x4D2C,
            0xBE,
            0x82,
            0xBE,
            0x3C,
            0xA0,
            0xB2,
            0x4D,
            0x43
        )

        # MFSampleExtension_LastSlice {2b5d5457-5547-4f07-b8c8-b4a3a9a1daac}
        # Type: UINT32
        MFSampleExtension_LastSlice = DEFINE_GUID(
            0x2B5D5457,
            0x5547,
            0x4F07,
            0xB8,
            0xC8,
            0xB4,
            0xA3,
            0xA9,
            0xA1,
            0xDA,
            0xAC
        )

        # Indicates macroblock is not needed for output and can be skipped
        MACROBLOCK_FLAG_SKIP = 0x00000001

        # Indicates macroblock is changed from the previous frame
        MACROBLOCK_FLAG_DIRTY = 0x00000002

        # Indicates macroblock from the previous frame has moved to a new
        # position
        MACROBLOCK_FLAG_MOTION = 0x00000004

        # Indicates macroblock contains video playback or other continuous
        # motion, rather than a slower moving screen capture
        MACROBLOCK_FLAG_VIDEO = 0x00000008

        # Indicates that the motion vector values of MACROBLOCK_DATA are
        # valid, and should be used in preference to
        # the encoder's calculated motion vector values
        MACROBLOCK_FLAG_HAS_MOTION_VECTOR = 0x00000010

        # Indicates that the QPDelta value of MACROBLOCK_DATA is valid, and
        # specifies the QP of this macroblock relative
        # to the rest of the frame
        MACROBLOCK_FLAG_HAS_QP = 0x00000020

        _MACROBLOCK_DATA._fields_ = [
            ('flags', UINT32),
            ('motionVectorX', INT16),
            ('motionVectorY', INT16),
            ('QPDelta', INT32),
        ]

        # MFSampleExtension_FeatureMap {a032d165-46fc-400a-b449-49de53e62a6e}
        # Type: BLOB
        # Blob should contain one MACROBLOCK_DATA structure for each
        # macroblock in the
        # input frame.
        MFSampleExtension_FeatureMap = DEFINE_GUID(
            0xA032D165,
            0x46FC,
            0x400A,
            0xB4,
            0x49,
            0x49,
            0xDE,
            0x53,
            0xE6,
            0x2A,
            0x6E
        )

        # MFSampleExtension_ChromaOnly {1eb9179c-a01f-4845-8c04-0e65a26eb04f}
        # Type: BOOL (UINT32)
        # Set to 1 if the input sample is a chroma-only frame
        MFSampleExtension_ChromaOnly = DEFINE_GUID(
            0x1EB9179C,
            0xA01F,
            0x4845,
            0x8C,
            0x04,
            0x0E,
            0x65,
            0xA2,
            0x6E,
            0xB0,
            0x4F
        )

        # /////////////////////////////////////////////////////////////////////////////
        #
        # / These are the attribute GUIDs that need to be used by MFT0 to
        # provide
        # / thumbnail support. We are declaring these in our internal idl
        # first and
        # / once we pass API spec review, we can move it to the public header.
        # /////////////////////////////////////////////////////////////////////////////
        #
        # MFSampleExtension_PhotoThumbnail
        # {74BBC85C-C8BB-42DC-B586DA17FFD35DCC}
        # Type: IUnknown
        # If this attribute is set on the IMFSample provided by the MFT0, this
        # will contain the IMFMediaBuffer which contains
        # the Photo Thumbnail as configured using the
        # KSPROPERTYSETID_ExtendedCameraControl.
        MFSampleExtension_PhotoThumbnail = DEFINE_GUID(
            0x74BBC85C,
            0xC8BB,
            0x42DC,
            0xB5,
            0x86,
            0xDA,
            0x17,
            0xFF,
            0xD3,
            0x5D,
            0xCC
        )

        # MFSampleExtension_PhotoThumbnailMediaType
        # {61AD5420-EBF8-4143-89AF6BF25F672DEF}
        # Type: IUnknown
        # This attribute will contain the IMFMediaType which describes the
        # image format type contained in the
        # MFSampleExtension_PhotoThumbnail attribute. If the
        # MFSampleExtension_PhotoThumbnail attribute
        # is present on the photo sample, the
        # MFSampleExtension_PhotoThumbnailMediaType is required.
        MFSampleExtension_PhotoThumbnailMediaType = DEFINE_GUID(
            0x61AD5420,
            0xEBF8,
            0x4143,
            0x89,
            0xAF,
            0x6B,
            0xF2,
            0x5F,
            0x67,
            0x2D,
            0xEF
        )

        # MFSampleExtension_CaptureMetadata
        # Type: IUnknown (IMFAttributes)
        # This is the IMFAttributes store for all the metadata related to the
        # capture
        # pipeline. It can be potentially present on any IMFSample.
        MFSampleExtension_CaptureMetadata = DEFINE_GUID(
            0x2EBE23A8,
            0xFAF5,
            0x444A,
            0xA6,
            0xA2,
            0xEB,
            0x81,
            0x08,
            0x80,
            0xAB,
            0x5D
        )

        # MFSampleExtension_MDLCacheCookie
        # Type: IUnknown (IMFAttributes)
        # This is the IMFAttributes stored in the sample if the mini driver
        # desires to cache MDL's. This is used internally by the pipeline.
        # {5F002AF9-D8F9-41A3-B6C3-A2AD43F647AD}
        MFSampleExtension_MDLCacheCookie = DEFINE_GUID(
            0x5F002AF9,
            0xD8F9,
            0x41A3,
            0xB6,
            0xC3,
            0xA2,
            0xAD,
            0x43,
            0xF6,
            0x47,
            0xAD
        )

        # Put all MF_CAPTURE_METADATA_* here.
        # {0F9DD6C6-6003-45D8-BD59-F1F53E3D04E8}
        # MF_CAPTURE_METADATA_PHOTO_FRAME_FLASH {UINT32}
        # 0 - No flash triggered on this frame.
        # non-0 - Flash triggered on this frame.
        # Do not explicitly check for a value of 1 here, we may overload this
        # to
        # indicate special types of flash going forward
        # (applications should only
        # check for != 0 to indicate flash took place).
        MF_CAPTURE_METADATA_PHOTO_FRAME_FLASH = DEFINE_GUID(
            0x0F9DD6C6,
            0x6003,
            0x45D8,
            0xBD,
            0x59,
            0xF1,
            0xF5,
            0x3E,
            0x3D,
            0x04,
            0xE8
        )

        # The raw IUnknown corresponding to the IMFMediaBuffer that contains
        # the metadata
        # stream as written by the camera driver. This may be a mix of
        # pre-defined metadata
        # such as photo confirmation, focus notification, or custom metadata
        # that only
        # the MFT0 can parse.
        MF_CAPTURE_METADATA_FRAME_RAWSTREAM = DEFINE_GUID(
            0x9252077B,
            0x2680,
            0x49B9,
            0xAE,
            0x02,
            0xB1,
            0x90,
            0x75,
            0x97,
            0x3B,
            0x70
        )

        # {A87EE154-997F-465D-B91F-29D53B982B88}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_FOCUSSTATE = DEFINE_GUID(
            0xA87EE154,
            0x997F,
            0x465D,
            0xB9,
            0x1F,
            0x29,
            0xD5,
            0x3B,
            0x98,
            0x2B,
            0x88
        )

        # {BB3716D9-8A61-47A4-8197-459C7FF174D5}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_REQUESTED_FRAME_SETTING_ID = DEFINE_GUID(
            0xBB3716D9,
            0x8A61,
            0x47A4,
            0x81,
            0x97,
            0x45,
            0x9C,
            0x7F,
            0xF1,
            0x74,
            0xD5
        )

        # {16B9AE99-CD84-4063-879D-A28C7633729E}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_EXPOSURE_TIME = DEFINE_GUID(
            0x16B9AE99,
            0xCD84,
            0x4063,
            0x87,
            0x9D,
            0xA2,
            0x8C,
            0x76,
            0x33,
            0x72,
            0x9E
        )

        # {D198AA75-4B62-4345-ABF3-3C31FA12C299}
        MF_CAPTURE_METADATA_EXPOSURE_COMPENSATION = DEFINE_GUID(
            0xD198AA75,
            0x4B62,
            0x4345,
            0xAB,
            0xF3,
            0x3C,
            0x31,
            0xFA,
            0x12,
            0xC2,
            0x99
        )

        # {E528A68F-B2E3-44FE-8B65-07BF4B5A13FF}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_ISO_SPEED = DEFINE_GUID(
            0xE528A68F,
            0xB2E3,
            0x44FE,
            0x8B,
            0x65,
            0x7,
            0xBF,
            0x4B,
            0x5A,
            0x13,
            0xFF
        )

        # {B5FC8E86-11D1-4E70-819B-723A89FA4520}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_LENS_POSITION = DEFINE_GUID(
            0xB5FC8E86,
            0x11D1,
            0x4E70,
            0x81,
            0x9B,
            0x72,
            0x3A,
            0x89,
            0xFA,
            0x45,
            0x20
        )

        # {9CC3B54D-5ED3-4BAE-B388-7670AEF59E13}
        # TYPE: UINT64
        MF_CAPTURE_METADATA_SCENE_MODE = DEFINE_GUID(
            0x9CC3B54D,
            0x5ED3,
            0x4BAE,
            0xB3,
            0x88,
            0x76,
            0x70,
            0xAE,
            0xF5,
            0x9E,
            0x13
        )

        # {4A51520B-FB36-446C-9DF2-68171B9A0389}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_FLASH = DEFINE_GUID(
            0x4A51520B,
            0xFB36,
            0x446C,
            0x9D,
            0xF2,
            0x68,
            0x17,
            0x1B,
            0x9A,
            0x3,
            0x89
        )

        # {9C0E0D49-0205-491A-BC9D-2D6E1F4D5684}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_FLASH_POWER = DEFINE_GUID(
            0x9C0E0D49,
            0x205,
            0x491A,
            0xBC,
            0x9D,
            0x2D,
            0x6E,
            0x1F,
            0x4D,
            0x56,
            0x84
        )

        # {C736FD77-0FB9-4E2E-97A2-FCD490739EE9}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_WHITEBALANCE = DEFINE_GUID(
            0xC736FD77,
            0xFB9,
            0x4E2E,
            0x97,
            0xA2,
            0xFC,
            0xD4,
            0x90,
            0x73,
            0x9E,
            0xE9
        )

        # {E50B0B81-E501-42C2-ABF2-857ECB13FA5C}
        # TYPE: UINT32
        MF_CAPTURE_METADATA_ZOOMFACTOR = DEFINE_GUID(
            0xE50B0B81,
            0xE501,
            0x42C2,
            0xAB,
            0xF2,
            0x85,
            0x7E,
            0xCB,
            0x13,
            0xFA,
            0x5C
        )

        # {864F25A6-349F-46B1-A30E-54CC22928A47}
        # TYPE: BLOB
        MF_CAPTURE_METADATA_FACEROIS = DEFINE_GUID(
            0x864F25A6,
            0x349F,
            0x46B1,
            0xA3,
            0xE,
            0x54,
            0xCC,
            0x22,
            0x92,
            0x8A,
            0x47
        )

        # {E94D50CC-3DA0-44d4-BB34-83198A741868}
        # TYPE: BLOB
        MF_CAPTURE_METADATA_FACEROITIMESTAMPS = DEFINE_GUID(
            0xE94D50CC,
            0x3DA0,
            0x44D4,
            0xBB,
            0x34,
            0x83,
            0x19,
            0x8A,
            0x74,
            0x18,
            0x68
        )

        # {B927A1A8-18EF-46d3-B3AF-69372F94D9B2}
        # TYPE: BLOB
        MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS = DEFINE_GUID(
            0xB927A1A8,
            0x18EF,
            0x46D3,
            0xB3,
            0xAF,
            0x69,
            0x37,
            0x2F,
            0x94,
            0xD9,
            0xB2
        )

        # {05802AC9-0E1D-41c7-A8C8-7E7369F84E1E}
        # TYPE: BLOB
        MF_CAPTURE_METADATA_ISO_GAINS = DEFINE_GUID(
            0x5802AC9,
            0xE1D,
            0x41C7,
            0xA8,
            0xC8,
            0x7E,
            0x73,
            0x69,
            0xF8,
            0x4E,
            0x1E
        )

        # {DB51357E-9D3D-4962-B06D-07CE650D9A0A}
        # TYPE: UINT64
        MF_CAPTURE_METADATA_SENSORFRAMERATE = DEFINE_GUID(
            0xDB51357E,
            0x9D3D,
            0x4962,
            0xB0,
            0x6D,
            0x7,
            0xCE,
            0x65,
            0xD,
            0x9A,
            0xA
        )

        # {E7570C8F-2DCB-4c7c-AACE-22ECE7CCE647}
        # TYPE: BLOB
        MF_CAPTURE_METADATA_WHITEBALANCE_GAINS = DEFINE_GUID(
            0xE7570C8F,
            0x2DCB,
            0x4C7C,
            0xAA,
            0xCE,
            0x22,
            0xEC,
            0xE7,
            0xCC,
            0xE6,
            0x47
        )

        # {85358432-2EF6-4ba9-A3FB-06D82974B895}
        # TYPE: BLOB
        MF_CAPTURE_METADATA_HISTOGRAM = DEFINE_GUID(
            0x85358432,
            0x2EF6,
            0x4BA9,
            0xA3,
            0xFB,
            0x6,
            0xD8,
            0x29,
            0x74,
            0xB8,
            0x95
        )

        # {2e9575b8-8c31-4a02-8575-42b197b71592}
        # TYPE: BLOB
        MF_CAPTURE_METADATA_EXIF = DEFINE_GUID(
            0x2E9575B8,
            0x8C31,
            0x4A02,
            0x85,
            0x75,
            0x42,
            0xB1,
            0x97,
            0xB7,
            0x15,
            0x92
        )

        # {6D688FFC-63D3-46FE-BADA-5B947DB0D080}
        # TYPE: UINT64
        MF_CAPTURE_METADATA_FRAME_ILLUMINATION = DEFINE_GUID(
            0x6D688FFC,
            0x63D3,
            0x46FE,
            0xBA,
            0xDA,
            0x5B,
            0x94,
            0x7D,
            0xB0,
            0xD0,
            0x80
        )

        # MF_CAPTURE_METADATA_UVC_PAYLOADHEADER
        # {F9F88A87-E1DD-441E-95CB-42E21A64F1D9}
        # Value type: Blob
        # Stores USB Video Class Camera's payload header for user mode
        # components to
        # get the camera timestamps and other header information.
        MF_CAPTURE_METADATA_UVC_PAYLOADHEADER = DEFINE_GUID(
            0xF9F88A87,
            0xE1DD,
            0x441E,
            0x95,
            0xCB,
            0x42,
            0xE2,
            0x1A,
            0x64,
            0xF1,
            0xD9
        )

        # MFSampleExtension_Depth_MinReliableDepth
        # Type: UINT32, minimum reliable depth value in a D16 format depth
        # frame.
        # Default value if the attribute is absent is 1, because 0 represent
        # invalid depth
        # {5F8582B2-E36B-47C8-9B87-FEE1CA72C5B0}
        MFSampleExtension_Depth_MinReliableDepth = DEFINE_GUID(
            0x5F8582B2,
            0xE36B,
            0x47C8,
            0x9B,
            0x87,
            0xFE,
            0xE1,
            0xCA,
            0x72,
            0xC5,
            0xB0
        )

        # MFSampleExtension_Depth_MaxReliableDepth
        # Type: UINT32, maximum reliable depth value in a D16 format depth
        # frame
        # Default value if the attribute is absent is 65535
        # {E45545D1-1F0F-4A32-A8A7-6101A24EA8BE}
        MFSampleExtension_Depth_MaxReliableDepth = DEFINE_GUID(
            0xE45545D1,
            0x1F0F,
            0x4A32,
            0xA8,
            0xA7,
            0x61,
            0x1,
            0xA2,
            0x4E,
            0xA8,
            0xBE
        )

        # MF_CAPTURE_METADATA_FIRST_SCANLINE_START_TIME_QPC
        # {F9F88A87-E1DD-441E-95CB-42E21A64F1D9}
        # Value type: UINT64
        # Stores value of the start of scan in QPC time
        MF_CAPTURE_METADATA_FIRST_SCANLINE_START_TIME_QPC = DEFINE_GUID(
            0x6A2C49F1,
            0xE052,
            0x46B6,
            0xB2,
            0xD9,
            0x73,
            0xC1,
            0x55,
            0x87,
            0x09,
            0xAF
        )

        # MF_CAPTURE_METADATA_LAST_SCANLINE_END_TIME_QPC
        # {F9F88A87-E1DD-441E-95CB-42E21A64F1D9}
        # Value type: UINT64
        # Stores value of the end of scan in QPC time
        MF_CAPTURE_METADATA_LAST_SCANLINE_END_TIME_QPC = DEFINE_GUID(
            0xDCCADECB,
            0xC4D4,
            0x400D,
            0xB4,
            0x18,
            0x10,
            0xE8,
            0x85,
            0x25,
            0xE1,
            0xF6
        )

        # MF_CAPTURE_METADATA_SCANLINE_TIME_QPC_ACCURACY
        # {F9F88A87-E1DD-441E-95CB-42E21A64F1D9}
        # Value type: UINT64
        # Stores value of timestamp accuracy in QPC time absolute value
        MF_CAPTURE_METADATA_SCANLINE_TIME_QPC_ACCURACY = DEFINE_GUID(
            0x4CD79C51,
            0xF765,
            0x4B09,
            0xB1,
            0xE1,
            0x27,
            0xD1,
            0xF7,
            0xEB,
            0xEA,
            0x09
        )

        # MF_CAPTURE_METADATA_SCAN_DIRECTION
        # {F9F88A87-E1DD-441E-95CB-42E21A64F1D9}
        # Value type: UINT32
        # Bitfield of the way the scan is read. If value is 0x00, scan is Left
        # to Right, Top to Bottom
        # 0x0 - Left.Right
        # 0x1 - Right.Left
        # 0x2 Bottom.Top
        # 0x0 - Horizontal Scanline
        # 0x4 - Vertical Scanline
        MF_CAPTURE_METADATA_SCANLINE_DIRECTION = DEFINE_GUID(
            0x6496A3BA,
            0x1907,
            0x49E6,
            0xB0,
            0xC3,
            0x12,
            0x37,
            0x95,
            0xF3,
            0x80,
            0xA9
        )
        MFCAPTURE_METADATA_SCAN_RIGHT_LEFT = 0x00000001
        MFCAPTURE_METADATA_SCAN_BOTTOM_TOP = 0x00000002
        MFCAPTURE_METADATA_SCANLINE_VERTICAL = 0x00000004

        tagFaceRectInfoBlobHeader._fields_ = [
            # Size of this header + all FaceRectInfo following
            ('Size', ULONG),
            # Number of FaceRectInfo's in the blob
            ('Count', ULONG),
        ]

        tagFaceRectInfo._fields_ = [
            # Relative coordinates on the frame (Q31 format)
            ('Region', RECT),
            # Confidence Level of the region being a face
            ('confidenceLevel', LONG),
        ]

        tagFaceCharacterizationBlobHeader._fields_ = [
            # Size of this header + all FaceCharacterization following
            ('Size', ULONG),
            # Number of FaceCharacterization's in the blob. Must match the
            # number of FaceRectInfo's in FaceRectInfoBlobHeader
            ('Count', ULONG),
        ]

        tagFaceCharacterization._fields_ = [
            # [0, 100]. 0 indicates no blink for the left eye. 100 indicates
            # definite blink for the left eye
            ('BlinkScoreLeft', ULONG),
            # [0, 100]. 0 indicates no blink for the right eye. 100 indicates
            # definite blink for the right eye
            ('BlinkScoreRight', ULONG),
            # Any one of the MF_METADATAFACIALEXPRESSION_XXX defined
            ('FacialExpression', ULONG),
            # [0, 100]. 0 indicates no such facial expression as identified.
            # 100 indicates definite such facial expression as defined
            ('FacialExpressionScore', ULONG),
        ]
        MF_METADATAFACIALEXPRESSION_SMILE = 0x00000001

        tagCapturedMetadataExposureCompensation._fields_ = [
            # KSCAMERA_EXTENDEDPROP_EVCOMP_XXX step flag
            ('Flags', UINT64),
            # EV Compensation value in units of the step
            ('Value', INT32),
        ]

        tagCapturedMetadataISOGains._fields_ = [
            ('AnalogGain', FLOAT),
            ('DigitalGain', FLOAT),
        ]

        tagCapturedMetadataWhiteBalanceGains._fields_ = [
            ('R', FLOAT),
            ('G', FLOAT),
            ('B', FLOAT),
        ]

        tagMetadataTimeStamps._fields_ = [
            # Bitwise OR of MF_METADATATIMESTAMPS_XXX flags
            ('Flags', ULONG),
            # QPC time for the sample where the metadata is derived from
            # (in 100ns)
            ('Device', LONGLONG),
            # PTS for the sample where the metadata is derived from (in 100ns)
            ('Presentation', LONGLONG),
        ]
        MF_METADATATIMESTAMPS_DEVICE = 0x00000001
        MF_METADATATIMESTAMPS_PRESENTATION = 0x00000002

        tagHistogramGrid._fields_ = [
            # Width of the sensor output that histogram is collected from
            ('Width', ULONG),
            # Height of the sensor output that histogram is collected from
            ('Height', ULONG),
            # Absolute coordinates of the region on the sensor output that the
            # histogram is collected for
            ('Region', RECT),
        ]

        tagHistogramBlobHeader._fields_ = [
            # Size of the entire histogram blob in bytes
            ('Size', ULONG),
            # Number of histograms in the blob. Each histogram is identified
            # by a HistogramHeader
            ('Histograms', ULONG),
        ]

        tagHistogramHeader._fields_ = [
            # Size in bytes of this header +
            # (HistogramDataHeader + histogram data following)*number of
            # channels available
            ('Size', ULONG),
            # Number of bins in the histogram
            ('Bins', ULONG),
            # Color space that the histogram is collected from
            ('FourCC', ULONG),
            # Masks of the color channels that the histogram is collected for
            ('ChannelMasks', ULONG),
            # Grid that the histogram is collected from
            ('Grid', HistogramGrid),
        ]

        tagHistogramDataHeader._fields_ = [
            # Size in bytes of this header + histogram data following
            ('Size', ULONG),
            # Mask of the color channel for the histogram data
            ('ChannelMask', ULONG),
            # 1, if linear; 0 nonlinear
            ('Linear', ULONG),
        ]
        MF_HISTOGRAM_CHANNEL_Y = 0x00000001
        MF_HISTOGRAM_CHANNEL_R = 0x00000002
        MF_HISTOGRAM_CHANNEL_G = 0x00000004
        MF_HISTOGRAM_CHANNEL_B = 0x00000008
        MF_HISTOGRAM_CHANNEL_Cb = 0x00000010
        MF_HISTOGRAM_CHANNEL_Cr = 0x00000020

        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////// Attributes ////////////////////////////////////
        #
        # //////////////////////////////////////////////////////////////////////////////
        #
        # STDAPI
        # MFCreateAttributes(
        # _Out_   IMFAttributes** ppMFAttributes,
        # _In_    UINT32          cInitialSize
        # );
        MFCreateAttributes = mfplat.MFCreateAttributes
        # STDAPI
        # MFInitAttributesFromBlob(
        # _In_                    IMFAttributes*  pAttributes,
        # _In_reads_bytes_(cbBufSize)  UINT8*    pBuf,
        # _In_                    UINT            cbBufSize
        # );
        MFInitAttributesFromBlob = mfplat.MFInitAttributesFromBlob
        # STDAPI
        # MFGetAttributesAsBlobSize(
        # _In_    IMFAttributes*  pAttributes,
        # _Out_   UINT32*         pcbBufSize
        # );
        MFGetAttributesAsBlobSize = mfplat.MFGetAttributesAsBlobSize
        # STDAPI
        # MFGetAttributesAsBlob(
        # _In_                    IMFAttributes*  pAttributes,
        # _Out_writes_bytes_(cbBufSize) UINT8*          pBuf,
        # _In_                    UINT            cbBufSize
        # );
        MFGetAttributesAsBlob = mfplat.MFGetAttributesAsBlob
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////// MFT Register & Enum ////////////////////////////
        #
        # //////////////////////////////////////////////////////////////////////////////
        #
        # MFT Registry categories
        if defined(MF_INIT_GUIDS):
            from pyWinAPI.shared.initguid_h import * # NOQA
        # END IF

        # {d6c02d4b-6833-45b4-971a-05a4b04bab91} MFT_CATEGORY_VIDEO_DECODER
        MFT_CATEGORY_VIDEO_DECODER = DEFINE_GUID(
            0xD6C02D4B,
            0x6833,
            0x45B4,
            0x97,
            0x1A,
            0x05,
            0xA4,
            0xB0,
            0x4B,
            0xAB,
            0x91
        )

        # {f79eac7d-e545-4387-bdee-d647d7bde42a} MFT_CATEGORY_VIDEO_ENCODER
        MFT_CATEGORY_VIDEO_ENCODER = DEFINE_GUID(
            0xF79EAC7D,
            0xE545,
            0x4387,
            0xBD,
            0xEE,
            0xD6,
            0x47,
            0xD7,
            0xBD,
            0xE4,
            0x2A
        )

        # {12e17c21-532c-4a6e-8a1c-40825a736397} MFT_CATEGORY_VIDEO_EFFECT
        MFT_CATEGORY_VIDEO_EFFECT = DEFINE_GUID(
            0x12E17C21,
            0x532C,
            0x4A6E,
            0x8A,
            0x1C,
            0x40,
            0x82,
            0x5A,
            0x73,
            0x63,
            0x97
        )

        # {059c561e-05ae-4b61-b69d-55b61ee54a7b} MFT_CATEGORY_MULTIPLEXER
        MFT_CATEGORY_MULTIPLEXER = DEFINE_GUID(
            0x059C561E,
            0x05AE,
            0x4B61,
            0xB6,
            0x9D,
            0x55,
            0xB6,
            0x1E,
            0xE5,
            0x4A,
            0x7B
        )

        # {a8700a7a-939b-44c5-99d7-76226b23b3f1} MFT_CATEGORY_DEMULTIPLEXER
        MFT_CATEGORY_DEMULTIPLEXER = DEFINE_GUID(
            0xA8700A7A,
            0x939B,
            0x44C5,
            0x99,
            0xD7,
            0x76,
            0x22,
            0x6B,
            0x23,
            0xB3,
            0xF1
        )

        # {9ea73fb4-ef7a-4559-8d5d-719d8f0426c7} MFT_CATEGORY_AUDIO_DECODER
        MFT_CATEGORY_AUDIO_DECODER = DEFINE_GUID(
            0x9EA73FB4,
            0xEF7A,
            0x4559,
            0x8D,
            0x5D,
            0x71,
            0x9D,
            0x8F,
            0x04,
            0x26,
            0xC7
        )

        # {91c64bd0-f91e-4d8c-9276-db248279d975} MFT_CATEGORY_AUDIO_ENCODER
        MFT_CATEGORY_AUDIO_ENCODER = DEFINE_GUID(
            0x91C64BD0,
            0xF91E,
            0x4D8C,
            0x92,
            0x76,
            0xDB,
            0x24,
            0x82,
            0x79,
            0xD9,
            0x75
        )

        # {11064c48-3648-4ed0-932e-05ce8ac811b7} MFT_CATEGORY_AUDIO_EFFECT
        MFT_CATEGORY_AUDIO_EFFECT = DEFINE_GUID(
            0x11064C48,
            0x3648,
            0x4ED0,
            0x93,
            0x2E,
            0x05,
            0xCE,
            0x8A,
            0xC8,
            0x11,
            0xB7
        )
        if WINVER >= _WIN32_WINNT_WIN7:
            # {302EA3FC-AA5F-47f9-9F7A-C2188BB163021}...MFT_CATEGORY_VIDEO_PROCESSOR
            #
            MFT_CATEGORY_VIDEO_PROCESSOR = DEFINE_GUID(
                0x302EA3FC,
                0xAA5F,
                0x47F9,
                0x9F,
                0x7A,
                0xC2,
                0x18,
                0x8B,
                0xB1,
                0x63,
                0x2
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        # {90175d57-b7ea-4901-aeb3-933a8747756f} MFT_CATEGORY_OTHER
        MFT_CATEGORY_OTHER = DEFINE_GUID(
            0x90175D57,
            0xB7EA,
            0x4901,
            0xAE,
            0xB3,
            0x93,
            0x3A,
            0x87,
            0x47,
            0x75,
            0x6F
        )
        if NTDDI_VERSION >= NTDDI_WIN10_RS1:
            MFT_CATEGORY_ENCRYPTOR = DEFINE_GUID(
                0xB0C687BE,
                0x01CD,
                0x44B5,
                0xB8,
                0xB2,
                0x7C,
                0x1D,
                0x7E,
                0x05,
                0x8B,
                0x1F
            )
        # END IF

        # TODO: switch to NTDDI_WIN10_RS3 when _NT_TARGET_VERSION is updated
        # to support RS3
        if NTDDI_VERSION >= NTDDI_WIN10_RS2:
            # {145CD8B4-92F4-4b23-8AE7-E0DF06C2DA95}
            # MFT_CATEGORY_VIDEO_RENDERER_EFFECT
            MFT_CATEGORY_VIDEO_RENDERER_EFFECT = DEFINE_GUID(
                0x145CD8B4,
                0x92F4,
                0x4B23,
                0x8A,
                0xE7,
                0xE0,
                0xDF,
                0x6,
                0xC2,
                0xDA,
                0x95
            )
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # "Flags" is for future expansion - for now must be 0
        # STDAPI
        # MFTRegister(
        # _In_                            CLSID                   clsidMFT,
        # _In_                            GUID                    guidCategory,
        # _In_                            LPWSTR                  pszName,
        # _In_                            UINT32                  Flags,
        # _In_                            UINT32                  cInputTypes,
        # _In_reads_opt_(cInputTypes)    MFT_REGISTER_TYPE_INFO* pInputTypes,
        # _In_                            UINT32                  cOutputTypes,
        # _In_reads_opt_(cOutputTypes)   MFT_REGISTER_TYPE_INFO* pOutputTypes,
        # _In_opt_                        IMFAttributes*          pAttributes
        # );
        MFTRegister = mfplat.MFTRegister
        # STDAPI
        # MFTUnregister(
        # _In_    CLSID   clsidMFT
        # );
        MFTUnregister = mfplat.MFTUnregister

        if WINVER >= _WIN32_WINNT_WIN7:
            # Register an MFT class in-process
            # STDAPI
            # MFTRegisterLocal(
            # _In_                        IClassFactory*          pClassFactory,
            # _In_                        REFGUID                 guidCategory,
            # _In_                        LPCWSTR                 pszName,
            # _In_                        UINT32                  Flags,
            # _In_                        UINT32                  cInputTypes,
            # _In_reads_opt_(cInputTypes)const MFT_REGISTER_TYPE_INFO* pInputTypes,
            # _In_                        UINT32                  cOutputTypes,
            # _In_reads_opt_(cOutputTypes)const MFT_REGISTER_TYPE_INFO* pOutputTypes
            # );
            MFTRegisterLocal = mfplat.MFTRegisterLocal

            # Unregister locally registered MFT
            # If pClassFactory is NULL all local MFTs are unregistered
            # STDAPI
            # MFTUnregisterLocal(
            # _In_opt_    IClassFactory *   pClassFactory
            # );
            MFTUnregisterLocal = mfplat.MFTUnregisterLocal

            # Register an MFT class in-process, by CLSID
            # STDAPI
            # MFTRegisterLocalByCLSID(
            # _In_                        REFCLSID                clisdMFT,
            # _In_                        REFGUID                 guidCategory,
            # _In_                        LPCWSTR                 pszName,
            # _In_                        UINT32                  Flags,
            # _In_                        UINT32                  cInputTypes,
            # _In_reads_opt_(cInputTypes)const MFT_REGISTER_TYPE_INFO* pInputTypes,
            # _In_                        UINT32                  cOutputTypes,
            # _In_reads_opt_(cOutputTypes)const MFT_REGISTER_TYPE_INFO* pOutputTypes
            # );
            MFTRegisterLocalByCLSID = mfplat.MFTRegisterLocalByCLSID

            # Unregister locally registered MFT by CLSID
            # STDAPI
            # MFTUnregisterLocalByCLSID(
            # _In_    CLSID   clsidMFT
            # );
            MFTUnregisterLocalByCLSID = mfplat.MFTUnregisterLocalByCLSID
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        # result *ppclsidMFT must be freed with CoTaskMemFree.
        # STDAPI
        # MFTEnum(
        # _In_                    GUID                    guidCategory,
        # _In_                    UINT32                  Flags,
        # _In_opt_                MFT_REGISTER_TYPE_INFO* pInputType,
        # _In_opt_                MFT_REGISTER_TYPE_INFO* pOutputType,
        # _In_opt_                IMFAttributes*          pAttributes,
        # _Outptr_result_buffer_(*pcMFTs)   CLSID**           ppclsidMFT, // must be freed with CoTaskMemFree
        # _Out_                   UINT32*                 pcMFTs
        # );
        MFTEnum = mfplat.MFTEnum
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if WINVER >= _WIN32_WINNT_WIN7:
            class _MFT_ENUM_FLAG(ENUM):
                MFT_ENUM_FLAG_SYNCMFT = 0x00000001
                MFT_ENUM_FLAG_ASYNCMFT = 0x00000002
                MFT_ENUM_FLAG_HARDWARE = 0x00000004
                MFT_ENUM_FLAG_FIELDOFUSE = 0x00000008
                MFT_ENUM_FLAG_LOCALMFT = 0x00000010
                MFT_ENUM_FLAG_TRANSCODE_ONLY = 0x00000020

                # Apply system local, do not use and preferred sorting and
                # filtering
                MFT_ENUM_FLAG_SORTANDFILTER = 0x00000040

                # Similar to MFT_ENUM_FLAG_SORTANDFILTER, but apply a local
                # policy of: MF_PLUGIN_CONTROL_POLICY_USE_APPROVED_PLUGINS
                MFT_ENUM_FLAG_SORTANDFILTER_APPROVED_ONLY = 0x000000C0

                # Similar to MFT_ENUM_FLAG_SORTANDFILTER, but apply a local
                # policy of: MF_PLUGIN_CONTROL_POLICY_USE_WEB_PLUGINS
                MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY = 0x00000140

                # Similar to MFT_ENUM_FLAG_SORTANDFILTER, but apply a local
                # policy of: MF_PLUGIN_CONTROL_POLICY_USE_WEB_PLUGINS_EDGEMODE
                MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY_EDGEMODE = 0x00000240
                MFT_ENUM_FLAG_UNTRUSTED_STOREMFT = 0x00000400

                # Enumerates all MFTs including SW and HW MFTs and applies
                # filtering
                MFT_ENUM_FLAG_ALL = 0x0000003F

            MFT_ENUM_FLAG_SYNCMFT = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_SYNCMFT
            MFT_ENUM_FLAG_ASYNCMFT = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_ASYNCMFT
            MFT_ENUM_FLAG_HARDWARE = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_HARDWARE
            MFT_ENUM_FLAG_FIELDOFUSE = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_FIELDOFUSE
            MFT_ENUM_FLAG_LOCALMFT = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_LOCALMFT
            MFT_ENUM_FLAG_TRANSCODE_ONLY = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_TRANSCODE_ONLY
            MFT_ENUM_FLAG_SORTANDFILTER = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_SORTANDFILTER
            MFT_ENUM_FLAG_SORTANDFILTER_APPROVED_ONLY = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_SORTANDFILTER_APPROVED_ONLY
            MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY
            MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY_EDGEMODE = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_SORTANDFILTER_WEB_ONLY_EDGEMODE
            MFT_ENUM_FLAG_UNTRUSTED_STOREMFT = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_UNTRUSTED_STOREMFT
            MFT_ENUM_FLAG_ALL = _MFT_ENUM_FLAG.MFT_ENUM_FLAG_ALL

            # result *pppMFTActivate must be freed with CoTaskMemFree. Each
            # IMFActivate pointer inside this
            # buffer should be released.

            # STDAPI
            # MFTEnumEx(
            # _In_                                GUID                            guidCategory,
            # _In_                                UINT32                          Flags,
            # _In_opt_                            MFT_REGISTER_TYPE_INFO*   pInputType,
            # _In_opt_                            MFT_REGISTER_TYPE_INFO*   pOutputType,
            # _Outptr_result_buffer_(*pnumMFTActivate) IMFActivate***                 pppMFTActivate,
            # _Out_                               UINT32*                         pnumMFTActivate
            # );
            MFTEnumEx = mfplat.MFTEnumEx
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        # TODO: switch to NTDDI_WIN10_RS3 when _NT_TARGET_VERSION is updated
        # to support RS3
        if NTDDI_VERSION >= NTDDI_WIN10_RS2:
            # MFT_ENUM_VIDEO_RENDERER_EXTENSION_PROFILE
            # {62C56928-9A4E-443b-B9DC-CAC830C24100}
            # Type: VT_VECTOR | VT_LPWSTR
            # MFTEnumEx stores this on the attribute store of the IMFActivate
            # object that
            # MFTEnumEx creates for MFTs that have an associated UWP Manifest
            # containing the tag
            # VideoRendererExtensionProfiles. This contains a list of all
            # VideoRendererExtensionProfile
            # entries in the VideoRendererExtensionProfiles tag.
            MFT_ENUM_VIDEO_RENDERER_EXTENSION_PROFILE = DEFINE_GUID(
                0x62C56928,
                0x9A4E,
                0x443B,
                0xB9,
                0xDC,
                0xCA,
                0xC8,
                0x30,
                0xC2,
                0x41,
                0x0
            )
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WIN10_RS1:
            # {1D39518C-E220-4DA8-A07F-BA172552D6B1} MFT_ENUM_ADAPTER_LUID
            MFT_ENUM_ADAPTER_LUID = DEFINE_GUID(
                0x1D39518C,
                0xE220,
                0x4DA8,
                0xA0,
                0x7F,
                0xBA,
                0x17,
                0x25,
                0x52,
                0xD6,
                0xB1
            )
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS1)

        # results *pszName, *ppInputTypes, and *ppOutputTypes must be freed
        # with CoTaskMemFree.
        # *ppAttributes must be released.

        # STDAPI
        # MFTGetInfo(
        # _In_                                   CLSID                       clsidMFT,
        # _Out_opt_                              LPWSTR*                     pszName,
        # _Outptr_opt_result_buffer_(*pcInputTypes)  MFT_REGISTER_TYPE_INFO**    ppInputTypes,
        # _Out_opt_                              UINT32*                     pcInputTypes,
        # _Outptr_opt_result_buffer_(*pcOutputTypes) MFT_REGISTER_TYPE_INFO**    ppOutputTypes,
        # _Out_opt_                              UINT32*                     pcOutputTypes,
        # _Outptr_opt_result_maybenull_                    IMFAttributes**             ppAttributes
        # );
        MFTGetInfo = mfplat.MFTGetInfo
        if WINVER >= _WIN32_WINNT_WIN7:
            # Get the plugin control API
            # STDAPI
            # MFGetPluginControl(
            # _Out_ IMFPluginControl **ppPluginControl
            # );
            MFGetPluginControl = mfplat.MFGetPluginControl
            # Get MFT's merit - checking that is has a valid certificate
            # STDAPI
            # MFGetMFTMerit(
            # _Inout_ IUnknown *pMFT,
            # _In_    UINT32   cbVerifier,
            # _In_reads_bytes_(cbVerifier) BYTE * verifier,
            # _Out_   DWORD   *merit
            # );
            MFGetMFTMerit = mfplat.MFGetMFTMerit        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINVER >= _WIN32_WINNT_WIN8:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

            # STDAPI
            # MFRegisterLocalSchemeHandler(
            # _In_        PCWSTR          szScheme,
            # _In_        IMFActivate*    pActivate
            # );
            MFRegisterLocalSchemeHandler = mfplat.MFRegisterLocalSchemeHandler
            # STDAPI
            # MFRegisterLocalByteStreamHandler(
            # _In_        PCWSTR          szFileExtension,
            # _In_        PCWSTR          szMimeType,
            # _In_        IMFActivate*    pActivate
            # );
            MFRegisterLocalByteStreamHandler = (
                mfplat.MFRegisterLocalByteStreamHandler
            )
            # Wrap a bytestream so that calling Close() on the wrapper
            # closes the wrapper but not the original bytestream. The
            # original bytestream can then be passed to another
            # media source for instance.
            # STDAPI
            # MFCreateMFByteStreamWrapper(
            # _In_        IMFByteStream*  pStream,
            # _Out_       IMFByteStream** ppStreamWrapper
            # );
            MFCreateMFByteStreamWrapper = mfplat.MFCreateMFByteStreamWrapper        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            # Create a MF activate object that can instantiate media extension
            # objects.
            # The activate object supports both IMFActivate and IClassFactory.
            # STDAPI
            # MFCreateMediaExtensionActivate(
            # _In_        PCWSTR          szActivatableClassId,
            # _In_opt_    IUnknown*       pConfiguration,
            # _In_        REFIID          riid,
            # _Outptr_    LPVOID*         ppvObject
            # );
            MFCreateMediaExtensionActivate = (
                mfplat.MFCreateMediaExtensionActivate
            )        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN8)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////// MFT Attributes GUIDs ////////////////////////////
        #
        # {53476A11-3F13-49fb-AC42-EE2733C96741}
        # MFT_SUPPORT_DYNAMIC_FORMAT_CHANGE {UINT32 (BOOL)}
        MFT_SUPPORT_DYNAMIC_FORMAT_CHANGE = DEFINE_GUID(
            0x53476A11,
            0x3F13,
            0x49FB,
            0xAC,
            0x42,
            0xEE,
            0x27,
            0x33,
            0xC9,
            0x67,
            0x41
        )

        # ///////////////////////////////////////////////////////////////////////////////////////////////////////////// Media Type GUIDs ////////////////////////////
        #
        # //////////////////////////////////////////////////////////////////////////////
        #
        # GUIDs for media types
        # In MF, media types for uncompressed video formats MUST be composed
        # from a FourCC or D3DFORMAT combined with
        # the "base GUID" {00000000-0000-0010-8000-00AA00389B71} by replacing
        # the initial 32 bits with the FourCC/D3DFORMAT
        # Audio media types for types which already have a defined wFormatTag
        # value can be constructed similarly, by
        # putting the wFormatTag (zero-extended to 32 bits) into the first 32
        # bits of the base GUID.
        # Compressed video or audio can also use any well-known GUID that
        # exists, or can create a new GUID.
        # GUIDs for common media types are defined below.
        # needed for the GUID definition macros below
        if not defined(FCC):
            def FCC(ch4):
                return (
                    ((ch4 & 0xFF) << 24) |
                    ((ch4 & 0xFF00) << 8) |
                    ((ch4 & 0xFF0000) >> 8) |
                    ((ch4 & 0xFF000000) >> 24)
                )
        # END IF

        # this macro creates a media type GUID from a FourCC, D3DFMT, or
        # WAVE_FORMAT
        if not defined(DEFINE_MEDIATYPE_GUID):
            def DEFINE_MEDIATYPE_GUID(_, format):
                return DEFINE_GUID(
                    format,
                    0x0000,
                    0x0010,
                    0x80,
                    0x00,
                    0x00,
                    0xAA,
                    0x00,
                    0x38,
                    0x9B,
                    0x71
                )
        # END IF

        # video media types
        # If no D3D headers have been included yet, define local versions of
        # D3DFMT constants we use.
        # We can't include D3D headers from this header because we need it to
        # be compatible with all versions
        # of D3D.
        if not defined(DIRECT3D_VERSION):
            D3DFMT_R8G8B8 = 20
            D3DFMT_A8R8G8B8 = 21
            D3DFMT_X8R8G8B8 = 22
            D3DFMT_R5G6B5 = 23
            D3DFMT_X1R5G5B5 = 24
            D3DFMT_A2B10G10R10 = 31
            D3DFMT_P8 = 41
            D3DFMT_L8 = 50
            D3DFMT_D16 = 80
            D3DFMT_L16 = 81
            D3DFMT_A16B16G16R16F = 113
            LOCAL_D3DFMT_DEFINES = 1
        # END IF

        # assume MFVideoFormat_H264 is frame aligned. that is, each input
        # sample has one complete compressed frame
        # (one frame picture, two field pictures or a single unpaired field picture)
        #
        if WINVER >= _WIN32_WINNT_WIN8:
            pass
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        if WDK_NTDDI_VERSION >= NTDDI_WIN10:
            pass
        # END IF

        if WDK_NTDDI_VERSION >= NTDDI_WIN10_RS3:
            pass
        # END IF

        if WDK_NTDDI_VERSION >= NTDDI_WIN10:
            # MFSample Perception Date Type-specific attribute GUIDs should be
            # in sync with KSCameraProfileSensorType
            class _MFFrameSourceTypes(ENUM):
                MFFrameSourceTypes_Color = 0x0001
                MFFrameSourceTypes_Infrared = 0x0002
                MFFrameSourceTypes_Depth = 0x0004
                MFFrameSourceTypes_Image = 0x0008
                MFFrameSourceTypes_Custom = 0x0080

            MFFrameSourceTypes = _MFFrameSourceTypes
        # END IF   (WINVER > _WIN32_WINNT_WIN10)

        # undef the local D3DFMT definitions to avoid later clashes with D3D
        # headers
        if defined(LOCAL_D3DFMT_DEFINES):
            pass
        # END IF

        # assume MFVideoFormat_H264_ES may not be frame aligned. that is, each
        # input sample may have one partial frame,
        # multiple frames, some frames plus some partial frame
        # or more general, N.M frames, N is the integer part and M is the
        # fractional part.
        # {3F40F4F0-5622-4FF8-B6D8-A17A584BEE5E}  MFVideoFormat_H264_ES
        MFVideoFormat_H264_ES = DEFINE_GUID(
            0x3F40F4F0,
            0x5622,
            0x4FF8,
            0xB6,
            0xD8,
            0xA1,
            0x7A,
            0x58,
            0x4B,
            0xEE,
            0x5E
        )

        # some legacy formats that don't fit the common pattern
        # {e06d8026-db46-11cf-b4d1-00805f6cbbea}  MFVideoFormat_MPEG2
        MFVideoFormat_MPEG2 = DEFINE_GUID(
            0xE06D8026,
            0xDB46,
            0x11CF,
            0xB4,
            0xD1,
            0x00,
            0x80,
            0x5F,
            0x6C,
            0xBB,
            0xEA
        )
        MFVideoFormat_MPG2 = MFVideoFormat_MPEG2

        # audio media types
        # MFAudioFormat_DTS is for S/PDIF-encapsulated DTS core streams. It is
        # the same as KSDATAFORMAT_SUBTYPE_IEC61937_DTS in ksmedia.h.
        # Use MEDIASUBTYPE_DTS2 (defined in wmcodecdsp.h) for raw DTS core
        # streams.
        # If DTS extension substreams may be present, use MEDIASUBTYPE_DTS_HD
        # instead for Master Audio, and MEDIASUBTYPE_DTS_HD_HRA for
        # High Resolution Audio and other extension substream variants.
        # (KSDATAFORMAT_SUBTYPE_IEC61937_DTS_HD is the
        # S/PDIF media subtype for MEDIASUBTYPE_DTS_HD and
        # MEDIASUBTYPE_DTS_HD_HRA.)
        #
        # MFAudioFormat_Dolby_AC3_SPDIF is for S/PDIF-encapsulated AC-3. It is
        # the same as KSDATAFORMAT_SUBTYPE_IEC61937_DOLBY_DIGITAL in ksmedia.h.
        # Use MFAudioFormat_Dolby_AC3 (MEDIASUBTYPE_DOLBY_AC3 in wmcodecdsp.h)
        # for raw AC-3 streams.
        if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
            pass
        # END IF

        # These audio types are not derived from an existing wFormatTag
        # MEDIASUBTYPE_DOBY_AC3 DEFINED IN KSUUIDS.H
        MFAudioFormat_Dolby_AC3 = DEFINE_GUID(
            0xE06D802C,
            0xDB46,
            0x11CF,
            0xB4,
            0xD1,
            0x00,
            0x80,
            0x05F,
            0x6C,
            0xBB,
            0xEA
        )
        # MEDIASUBTYPE_DOBY_DDPUS DEFINED IN WMCODECDSP.H
        MFAudioFormat_Dolby_DDPlus = DEFINE_GUID(
            0xA7FB87AF,
            0x2D02,
            0x42FB,
            0xA4,
            0xD4,
            0x5,
            0xCD,
            0x93,
            0x84,
            0x3B,
            0xDD
        )
        # {8D2FD10B-5841-4A6B-8905-588FEC1ADED9}
        MFAudioFormat_Vorbis = DEFINE_GUID(
            0x8D2FD10B,
            0x5841,
            0x4A6B,
            0x89,
            0x05,
            0x58,
            0x8F,
            0xEC,
            0x1A,
            0xDE,
            0xD9
        )
        if NTDDI_VERSION >= NTDDI_WIN10_RS2:
            MFAudioFormat_Float_SpatialObjects = DEFINE_GUID(
                0xFA39CD94,
                0xBC64,
                0x4AB1,
                0x9B,
                0x71,
                0xDC,
                0xD0,
                0x9D,
                0x5A,
                0x7E,
                0x7A
            )
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

        if WINVER >= _WIN32_WINNT_THRESHOLD:
            # LPCM audio with headers for encapsulation in an MPEG2 bitstream
            MFAudioFormat_LPCM = DEFINE_GUID(
                0xE06D8032,
                0xDB46,
                0x11CF,
                0xB4,
                0xD1,
                0x00,
                0x80,
                0x5F,
                0x6C,
                0xBB,
                0xEA
            )
            MFAudioFormat_PCM_HDCP = DEFINE_GUID(
                0xA5E7FF01,
                0x8411,
                0x4ACC,
                0xA8,
                0x65,
                0x5F,
                0x49,
                0x41,
                0x28,
                0x8D,
                0x80
            )
            MFAudioFormat_Dolby_AC3_HDCP = DEFINE_GUID(
                0x97663A80,
                0x8FFB,
                0x4445,
                0xA6,
                0xBA,
                0x79,
                0x2D,
                0x90,
                0x8F,
                0x49,
                0x7F
            )
            MFAudioFormat_AAC_HDCP = DEFINE_GUID(
                0x419BCE76,
                0x8B72,
                0x400F,
                0xAD,
                0xEB,
                0x84,
                0xB5,
                0x7D,
                0x63,
                0x48,
                0x4D
            )
            MFAudioFormat_ADTS_HDCP = DEFINE_GUID(
                0xDA4963A3,
                0x14D8,
                0x4DCF,
                0x92,
                0xB7,
                0x19,
                0x3E,
                0xB8,
                0x43,
                0x63,
                0xDB
            )
            MFAudioFormat_Base_HDCP = DEFINE_GUID(
                0x3884B5BC,
                0xE277,
                0x43FD,
                0x98,
                0x3D,
                0x03,
                0x8A,
                0xA8,
                0xD9,
                0xB6,
                0x05
            )
            MFVideoFormat_H264_HDCP = DEFINE_GUID(
                0x5D0CE9DD,
                0x9817,
                0x49DA,
                0xBD,
                0xFD,
                0xF5,
                0xF5,
                0xB9,
                0x8F,
                0x18,
                0xA6
            )
            MFVideoFormat_HEVC_HDCP = DEFINE_GUID(
                0x3CFE0FE6,
                0x05C4,
                0x47DC,
                0x9D,
                0x70,
                0x4B,
                0xDB,
                0x29,
                0x59,
                0x72,
                0x0F
            )
            MFVideoFormat_Base_HDCP = DEFINE_GUID(
                0xEAC3B9D5,
                0xBD14,
                0x4237,
                0x8F,
                0x1F,
                0xBA,
                0xB4,
                0x28,
                0xE4,
                0x93,
                0x12
            )
        # END IF

        # MPEG-4 media types
        # {00000000-767a-494d-b478-f29d25dc9037}  MFMPEG4Format_Base
        MFMPEG4Format_Base = DEFINE_GUID(
            0x00000000,
            0x767A,
            0x494D,
            0xB4,
            0x78,
            0xF2,
            0x9D,
            0x25,
            0xDC,
            0x90,
            0x37
        )

        # Subtitle media types
        # {2006F94F-29CA-4195-B8DB-00DED8FF0C97} MFSubtitleFormat_XML
        MFSubtitleFormat_XML = DEFINE_GUID(
            0x2006F94F,
            0x29CA,
            0x4195,
            0xB8,
            0xDB,
            0x00,
            0xDE,
            0xD8,
            0xFF,
            0x0C,
            0x97
        )

        # {73E73992-9a10-4356-9557-7194E91E3E54} MFSubtitleFormat_TTML
        MFSubtitleFormat_TTML = DEFINE_GUID(
            0x73E73992,
            0x9A10,
            0x4356,
            0x95,
            0x57,
            0x71,
            0x94,
            0xE9,
            0x1E,
            0x3E,
            0x54
        )

        # {7FA7FAA3-FEAE-4E16-AEDF-36B9ACFBB099} MFSubtitleFormat_ATSC
        MFSubtitleFormat_ATSC = DEFINE_GUID(
            0x7FA7FAA3,
            0xFEAE,
            0x4E16,
            0xAE,
            0xDF,
            0x36,
            0xB9,
            0xAC,
            0xFB,
            0xB0,
            0x99
        )

        # {C886D215-F485-40BB-8DB6-FADBC619A45D} MFSubtitleFormat_WebVTT
        MFSubtitleFormat_WebVTT = DEFINE_GUID(
            0xC886D215,
            0xF485,
            0x40BB,
            0x8D,
            0xB6,
            0xFA,
            0xDB,
            0xC6,
            0x19,
            0xA4,
            0x5D
        )

        # {5E467F2E-77CA-4CA5-8391-D142ED4B76C8} MFSubtitleFormat_SRT
        MFSubtitleFormat_SRT = DEFINE_GUID(
            0x5E467F2E,
            0x77CA,
            0x4CA5,
            0x83,
            0x91,
            0xD1,
            0x42,
            0xED,
            0x4B,
            0x76,
            0xC8
        )

        # {57176A1B-1A9E-4EEA-ABEF-C61760198AC4} MFSubtitleFormat_SSA
        MFSubtitleFormat_SSA = DEFINE_GUID(
            0x57176A1B,
            0x1A9E,
            0x4EEA,
            0xAB,
            0xEF,
            0xC6,
            0x17,
            0x60,
            0x19,
            0x8A,
            0xC4
        )

        # {1BB3D849-6614-4D80-8882-ED24AA82DA92}
        # MFSubtitleFormat_CustomUserData
        MFSubtitleFormat_CustomUserData = DEFINE_GUID(
            0x1BB3D849,
            0x6614,
            0x4D80,
            0x88,
            0x82,
            0xED,
            0x24,
            0xAA,
            0x82,
            0xDA,
            0x92
        )

        # Binary Data MediaTypes
        if not defined(DEFINE_BINARY_MEDIATYPE_GUID):
            def DEFINE_BINARY_MEDIATYPE_GUID(_, format):
                return DEFINE_GUID(
                    format,
                    0xBF10,
                    0x48B4,
                    0xBC,
                    0x18,
                    0x59,
                    0x3D,
                    0xC1,
                    0xDB,
                    0x95,
                    0xF
                )
        # END IF

        # /////////////////////////////////////////////////////////////////////
        # ////////////////// Media Type Attributes GUIDs //////////////////////
        # /////////////////////////////////////////////////////////////////////
        # GUIDs for IMFMediaType properties - prefix 'MF_MT_' - basic prop
        # type in {},
        # with type to cast to in ().
        # core info for all types
        # {48eba18e-f8c9-4687-bf11-0a74c9f96a8f} MF_MT_MAJOR_TYPE   {GUID}
        MF_MT_MAJOR_TYPE = DEFINE_GUID(
            0x48EBA18E,
            0xF8C9,
            0x4687,
            0xBF,
            0x11,
            0x0A,
            0x74,
            0xC9,
            0xF9,
            0x6A,
            0x8F
        )

        # {f7e34c9a-42e8-4714-b74b-cb29d72c35e5} MF_MT_SUBTYPE    {GUID}
        MF_MT_SUBTYPE = DEFINE_GUID(
            0xF7E34C9A,
            0x42E8,
            0x4714,
            0xB7,
            0x4B,
            0xCB,
            0x29,
            0xD7,
            0x2C,
            0x35,
            0xE5
        )

        # {c9173739-5e56-461c-b713-46fb995cb95f} MF_MT_ALL_SAMPLES_INDEPENDENT
        # {UINT32 (BOOL)}
        MF_MT_ALL_SAMPLES_INDEPENDENT = DEFINE_GUID(
            0xC9173739,
            0x5E56,
            0x461C,
            0xB7,
            0x13,
            0x46,
            0xFB,
            0x99,
            0x5C,
            0xB9,
            0x5F
        )

        # {b8ebefaf-b718-4e04-b0a9-116775e3321b} MF_MT_FIXED_SIZE_SAMPLES
        # {UINT32 (BOOL)}
        MF_MT_FIXED_SIZE_SAMPLES = DEFINE_GUID(
            0xB8EBEFAF,
            0xB718,
            0x4E04,
            0xB0,
            0xA9,
            0x11,
            0x67,
            0x75,
            0xE3,
            0x32,
            0x1B
        )

        # {3afd0cee-18f2-4ba5-a110-8bea502e1f92} MF_MT_COMPRESSED
        # {UINT32 (BOOL)}
        MF_MT_COMPRESSED = DEFINE_GUID(
            0x3AFD0CEE,
            0x18F2,
            0x4BA5,
            0xA1,
            0x10,
            0x8B,
            0xEA,
            0x50,
            0x2E,
            0x1F,
            0x92
        )

        # MF_MT_SAMPLE_SIZE is only valid if MF_MT_FIXED_SIZED_SAMPLES is TRUE
        # {dad3ab78-1990-408b-bce2-eba673dacc10} MF_MT_SAMPLE_SIZE   {UINT32}
        MF_MT_SAMPLE_SIZE = DEFINE_GUID(
            0xDAD3AB78,
            0x1990,
            0x408B,
            0xBC,
            0xE2,
            0xEB,
            0xA6,
            0x73,
            0xDA,
            0xCC,
            0x10
        )

        # 4d3f7b23-d02f-4e6c-9bee-e4bf2c6c695d  MF_MT_WRAPPED_TYPE   {Blob}
        MF_MT_WRAPPED_TYPE = DEFINE_GUID(
            0x4D3F7B23,
            0xD02F,
            0x4E6C,
            0x9B,
            0xEE,
            0xE4,
            0xBF,
            0x2C,
            0x6C,
            0x69,
            0x5D
        )
        if WINVER >= _WIN32_WINNT_WIN8:
            # Media Type & Sample attributes for 3D Video
            # {CB5E88CF-7B5B-476b-85AA-1CA5AE187555}  MF_MT_VIDEO_3D
            # {UINT32 (BOOL)}
            MF_MT_VIDEO_3D = DEFINE_GUID(
                0xCB5E88CF,
                0x7B5B,
                0x476B,
                0x85,
                0xAA,
                0x1C,
                0xA5,
                0xAE,
                0x18,
                0x75,
                0x55
            )

            # Enum describing the packing for 3D video frames
            class _MFVideo3DFormat(ENUM):
                MFVideo3DSampleFormat_BaseView = 0
                MFVideo3DSampleFormat_MultiView = 1
                MFVideo3DSampleFormat_Packed_LeftRight = 2
                MFVideo3DSampleFormat_Packed_TopBottom = 3

            MFVideo3DFormat = _MFVideo3DFormat

            # {5315d8a0-87c5-4697-b793-666c67c49b}  MF_MT_VIDEO_3D_FORMAT
            # {UINT32 (anyof MFVideo3DFormat)}
            MF_MT_VIDEO_3D_FORMAT = DEFINE_GUID(
                0x5315D8A0,
                0x87C5,
                0x4697,
                0xB7,
                0x93,
                0x66,
                0x6,
                0xC6,
                0x7C,
                0x4,
                0x9B
            )

            # {BB077E8A-DCBF-42eb-AF60-418DF98AA495}  MF_MT_VIDEO_3D_NUM_VIEW
            # {UINT32}
            MF_MT_VIDEO_3D_NUM_VIEWS = DEFINE_GUID(
                0xBB077E8A,
                0xDCBF,
                0x42EB,
                0xAF,
                0x60,
                0x41,
                0x8D,
                0xF9,
                0x8A,
                0xA4,
                0x95
            )

            # {6D4B7BFF-5629-4404-948C-C634F4CE26D4}
            # MF_MT_VIDEO_3D_LEFT_IS_BASE {UINT32}
            MF_MT_VIDEO_3D_LEFT_IS_BASE = DEFINE_GUID(
                0x6D4B7BFF,
                0x5629,
                0x4404,
                0x94,
                0x8C,
                0xC6,
                0x34,
                0xF4,
                0xCE,
                0x26,
                0xD4
            )

            # {EC298493-0ADA-4ea1-A4FE-CBBD36CE9331}
            # MF_MT_VIDEO_3D_FIRST_IS_LEFT {UINT32 (BOOL)}
            MF_MT_VIDEO_3D_FIRST_IS_LEFT = DEFINE_GUID(
                0xEC298493,
                0xADA,
                0x4EA1,
                0xA4,
                0xFE,
                0xCB,
                0xBD,
                0x36,
                0xCE,
                0x93,
                0x31
            )

            # MFSampleExtension_3DVideo
            # {F86F97A4-DD54-4e2e-9A5E-55FC2D74A005}
            # Type: UINT32
            # If present and nonzero, indicates that the sample contains 3D
            # Video data
            MFSampleExtension_3DVideo = DEFINE_GUID(
                0xF86F97A4,
                0xDD54,
                0x4E2E,
                0x9A,
                0x5E,
                0x55,
                0xFC,
                0x2D,
                0x74,
                0xA0,
                0x05
            )

            # Enum describing the packing for 3D video frames in a sample
            class _MFVideo3DSampleFormat(ENUM):
                MFSampleExtension_3DVideo_MultiView = 1
                MFSampleExtension_3DVideo_Packed = 0

            MFVideo3DSampleFormat = _MFVideo3DSampleFormat

            # MFSampleExtension_3DVideo_SampleFormat
            # {08671772-E36F-4cff-97B3-D72E20987A48}
            # Type: UINT32
            # The value of this attribute is a member of the
            # MFVideo3DSampleFormat enumeration.
            # MFVideo3DSampleFormat enumeration identifies how 3D views are
            # stored in the sample
            # - in a packed representation, all views are stored in a single
            # buffer
            # - in a multiview representation, each view is stored in its own
            # buffer
            MFSampleExtension_3DVideo_SampleFormat = DEFINE_GUID(
                0x8671772,
                0xE36F,
                0x4CFF,
                0x97,
                0xB3,
                0xD7,
                0x2E,
                0x20,
                0x98,
                0x7A,
                0x48
            )

            # Enum describing the video rotation formats
            # Only the values of 0, 90, 180, and 270 are valid.
            if not defined(_MFVideoRotationFormat_):
                _MFVideoRotationFormat_ = VOID


                class _MFVideoRotationFormat(ENUM):
                    MFVideoRotationFormat_0 = 0
                    MFVideoRotationFormat_90 = 90
                    MFVideoRotationFormat_180 = 180
                    MFVideoRotationFormat_270 = 270

                MFVideoRotationFormat = _MFVideoRotationFormat
            # END IF

            # MF_MT_VIDEO_ROTATION {C380465D-2271-428C-9B83-ECEA3B4A85C1}
            # Type: UINT32
            # Description: MF_MT_VIDEO_ROTATION attribute means the degree
            # that the content
            # has already been rotated in the counter clockwise direction.
            # Currently, only the values of 0, 90, 180, and 270 are valid for
            # MF_MT_VIDEO_ROTATION.
            # For convenience, these currently supported values are enumerated
            # in MFVideoRotationFormat.
            # Example: if the media type has MF_MT_VIDEO_ROTATION set as
            # MFVideoRotationFormat_90,
            # it means the content has been rotated 90 degree in the counter
            # clockwise direction.
            # If the content was actually rotated 90 degree in the clockwise
            # direction, 90 degree in
            # clockwise should be converted into 270 degree in the counter
            # clockwise direction and set
            # the attribute MF_MT_VIDEO_ROTATION as MFVideoRotationFormat_270
            # accordingly.
            MF_MT_VIDEO_ROTATION = DEFINE_GUID(
                0xC380465D,
                0x2271,
                0x428C,
                0x9B,
                0x83,
                0xEC,
                0xEA,
                0x3B,
                0x4A,
                0x85,
                0xC1
            )
            if NTDDI_VERSION >= NTDDI_WIN10_RS2:
                MF_DEVICESTREAM_MULTIPLEXED_MANAGER = DEFINE_GUID(
                    0x6EA542B0,
                    0x281F,
                    0x4231,
                    0xA4,
                    0x64,
                    0xFE,
                    0x2F,
                    0x50,
                    0x22,
                    0x50,
                    0x1C
                )
                MF_MEDIATYPE_MULTIPLEXED_MANAGER = DEFINE_GUID(
                    0x13C78FB5,
                    0xF275,
                    0x4EA0,
                    0xBB,
                    0x5F,
                    0x2,
                    0x49,
                    0x83,
                    0x2B,
                    0xD,
                    0x6E
                )
                MFSampleExtension_MULTIPLEXED_MANAGER = DEFINE_GUID(
                    0x8DCDEE79,
                    0x6B5A,
                    0x4C45,
                    0x8D,
                    0xB9,
                    0x20,
                    0xB3,
                    0x95,
                    0xF0,
                    0x2F,
                    0xCF
                )

                # STDAPI MFCreateMuxStreamAttributes(
                # _In_ IMFCollection *pAttributesToMux,
                # _COM_Outptr_ IMFAttributes**ppMuxAttribs
                # );
                MFCreateMuxStreamAttributes = (
                    mfplat.MFCreateMuxStreamAttributes
                )

                # STDAPI MFCreateMuxStreamMediaType(
                # _In_ IMFCollection *pMediaTypesToMux,
                # _COM_Outptr_ IMFMediaType**ppMuxMediaType
                # );
                MFCreateMuxStreamMediaType = mfplat.MFCreateMuxStreamMediaType

                # STDAPI MFCreateMuxStreamSample(
                # _In_ IMFCollection *pSamplesToMux,
                # _COM_Outptr_ IMFSample**ppMuxSample
                # );
                MFCreateMuxStreamSample = mfplat.MFCreateMuxStreamSample
            # END IF

            if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
                # MF_MT_SECURE  {c5acc4fd-0304-4ecf-809f-47bc97ff63bd }
                # Type: UINT32 (BOOL)
                # Description: MF_MT_SECURE attribute indicates that the
                # content will be using
                # secure D3D surfaces. These surfaces can only be accessed by
                # trusted hardware.
                MF_MT_SECURE = DEFINE_GUID(
                    0xC5ACC4FD,
                    0x0304,
                    0x4ECF,
                    0x80,
                    0x9F,
                    0x47,
                    0xBC,
                    0x97,
                    0xFF,
                    0x63,
                    0xBD
                )

                # MF_DEVICESTREAM_ATTRIBUTE_FRAMESOURCE_TYPES
                # {17145FD1-1B2B-423C-8001-2B6833ED3588}
                # Type: UINT32 (enum type defined in MFFrameSourceTypes)
                # Description: The value of this attribute is a enum value,
                # describing the sensor types.
                # For backward compatibility, when this attribute was not
                # defined on in a media type, it is assumed to be
                # MFFrameSourceTypes::Color.
                MF_DEVICESTREAM_ATTRIBUTE_FRAMESOURCE_TYPES = DEFINE_GUID(
                    0x17145FD1,
                    0x1B2B,
                    0x423C,
                    0x80,
                    0x1,
                    0x2B,
                    0x68,
                    0x33,
                    0xED,
                    0x35,
                    0x88
                )

                # MF_MT_ALPHA_MODE {5D959B0D-4CBF-4D04-919F-3F5F7F284211}
                # Type: UINT32
                # Description: To differentiate the usage of alpha channel in
                # such video formats, a new attribute MF_MT_ALPHA_MODE is
                # designed to describe this information.
                # The value of this attribute can be cast to DXGI_ALPHA_MODE.
                # If this attribute is not present, for backward
                # compatibility, the value is DXGI_ALPHA_MODE_STRAIGHT for
                # video format supporting alpha channel,
                # such as ARGB32, or DXGI_ALPHA_MODE_IGNORE for video format
                # without alpha channel, such as RGB32.
                MF_MT_ALPHA_MODE = DEFINE_GUID(
                    0x5D959B0D,
                    0x4CBF,
                    0x4D04,
                    0x91,
                    0x9F,
                    0x3F,
                    0x5F,
                    0x7F,
                    0x28,
                    0x42,
                    0x11
                )


                class _MFDepthMeasurement(ENUM):
                    DistanceToFocalPlane = 0
                    DistanceToOpticalCenter = 1

                MFDepthMeasurement = _MFDepthMeasurement

                # MF_MT_DEPTH_MEASUREMENT
                # {FD5AC489-0917-4BB6-9D54-3122BF70144B}
                # Type : UINT32 (MFDepthMeasurement)
                # Description: If this attribute is not present, by default it
                # is DistanceToFocalPlane, illustrated by following diagram.
                MF_MT_DEPTH_MEASUREMENT = DEFINE_GUID(
                    0xFD5AC489,
                    0x917,
                    0x4BB6,
                    0x9D,
                    0x54,
                    0x31,
                    0x22,
                    0xBF,
                    0x70,
                    0x14,
                    0x4B
                )

                # MF_MT_DEPTH_VALUE_UNIT {21a800f5-3189-4797-beba-f13cd9a31a5e}
                # Type : UINT64
                # Description: MF_MT_DEPTH_VALUE_UNIT attribute indicates
                # scale of the depth value in nanometers.
                # For each pixel in depth frame, the actual depth measured in
                # nanometers is the pixel value multiplied by this attribute.
                MF_MT_DEPTH_VALUE_UNIT = DEFINE_GUID(
                    0x21A800F5,
                    0x3189,
                    0x4797,
                    0xBE,
                    0xBA,
                    0xF1,
                    0x3C,
                    0xD9,
                    0xA3,
                    0x1A,
                    0x5E
                )
            # END IF

            # MF_MT_VIDEO_NO_FRAME_ORDERING
            # {3F5B106F-6BC2-4EE3-B7ED-8902C18F5351}
            # Type: UINT32
            # Description: MF_MT_VIDEO_NO_FRAME_ORDERING set to non-zero
            # (true) means external users/apps know
            # that input video bitstream has no frame rerodering,
            # that is, the output and display order is the same as the input
            # and decoding order
            # it will overwrite bitstream syntaxes even if bitstream syntaxes
            # do not indicate
            # that the output and display order is the same as the input and
            # decoding order
            # it is an attribute set on input media type
            MF_MT_VIDEO_NO_FRAME_ORDERING = DEFINE_GUID(
                0x3F5B106F,
                0x6BC2,
                0x4EE3,
                0xB7,
                0xED,
                0x89,
                0x2,
                0xC1,
                0x8F,
                0x53,
                0x51
            )

            # MF_MT_VIDEO_H264_NO_FMOASO {ED461CD6-EC9F-416A-A8A3-26D7D31018D7}
            # Type: UINT32
            # Description: MF_MT_VIDEO_H264_NO_FMOASO set to non-zero (true)
            # means external users/apps know
            # that H.264 input video bitstream has no FMO/ASO enabled,
            # that is, even if the bitstream has baseline profile and
            # constraint_set1_flag equal to 0,
            # the bitstream shall not have FMO/ASO
            # then H.264 decoder uses DXVA decoding and doesn't fall back to
            # software decoding
            # it improves power consumption, memory usage, performance and
            # user experiences
            # (without unnecessary glitches on low end devices)
            # it is an attribute set on input media type
            MF_MT_VIDEO_H264_NO_FMOASO = DEFINE_GUID(
                0xED461CD6,
                0xEC9F,
                0x416A,
                0xA8,
                0xA3,
                0x26,
                0xD7,
                0xD3,
                0x10,
                0x18,
                0xD7
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        # TODO: switch to NTDDI_WIN10_RS3 when _NT_TARGET_VERSION is updated
        # to support RS3
        if NTDDI_VERSION >= NTDDI_WIN10_RS2:
            # Renderer Extensions
            # MFSampleExtension_ForwardedDecodeUnits
            # {424C754C-97C8-48d6-8777-FC41F7B60879}
            # Type: IUnknown
            # This is an object of type IMFCollection containing IMFSample
            # objects
            # which contain NALU/SEI forwarded by a decoder.
            # Contains all custom NALU/SEI since previous frame with emulation
            # prevention bytes removed.
            # see: MF_MT_FORWARD_CUSTOM_NALU, MF_MT_FORWARD_CUSTOM_SEI
            MFSampleExtension_ForwardedDecodeUnits = DEFINE_GUID(
                0x424C754C,
                0x97C8,
                0x48D6,
                0x87,
                0x77,
                0xFC,
                0x41,
                0xF7,
                0xB6,
                0x8,
                0x79
            )

            # MFSampleExtension_TargetGlobalLuminance
            # {3F60EF36-31EF-4daf-8360-940397E41EF3}
            # Type: UINT32
            # Value in Nits that specifies the targeted global backlight
            # luminance for
            # the associated video frame.
            MFSampleExtension_TargetGlobalLuminance = DEFINE_GUID(
                0x3F60EF36,
                0x31EF,
                0x4DAF,
                0x83,
                0x60,
                0x94,
                0x3,
                0x97,
                0xE4,
                0x1E,
                0xF3
            )


            class _MF_CUSTOM_DECODE_UNIT_TYPE(ENUM):
                MF_DECODE_UNIT_NAL = 0
                MF_DECODE_UNIT_SEI = 1

            MF_CUSTOM_DECODE_UNIT_TYPE = _MF_CUSTOM_DECODE_UNIT_TYPE

            # MFSampleExtension_ForwardedDecodeUnitType
            # {089E57C7-47D3-4a26-BF9C-4B64FAFB5D1E}
            # Type: UINT32 (oneof MF_CUSTOM_DECODE_UNIT_TYPE)
            # Attached to IMFSample objects in
            # MFSampleExtension_ForwardedDecodeUnits, specifies
            # what type of unit is attached: SEI or NAL
            MFSampleExtension_ForwardedDecodeUnitType = DEFINE_GUID(
                0x89E57C7,
                0x47D3,
                0x4A26,
                0xBF,
                0x9C,
                0x4B,
                0x64,
                0xFA,
                0xFB,
                0x5D,
                0x1E
            )

            # MF_MT_FORWARD_CUSTOM_NALU {ED336EFD-244F-428d-9153-28F399458890}
            # Type: UINT32
            # Specifies the NAL unit type to forward on output samples of the
            # decoder.
            # If the decoder parses the specified NALU then it will not
            # forwarded.
            # See: MFSampleExtension_ForwardedDecodeUnits
            MF_MT_FORWARD_CUSTOM_NALU = DEFINE_GUID(
                0xED336EFD,
                0x244F,
                0x428D,
                0x91,
                0x53,
                0x28,
                0xF3,
                0x99,
                0x45,
                0x88,
                0x90
            )

            # MF_MT_FORWARD_CUSTOM_SEI {E27362F1-B136-41d1-9594-3A7E4FEBF2D1}
            # Type: UINT32
            # Specifies the SEI type to forward on output samples of the
            # decoder
            # If the decoder parses the specified SEI then it will not be
            # forwarded.
            # See: MFSampleExtension_ForwardedDecodeUnits
            MF_MT_FORWARD_CUSTOM_SEI = DEFINE_GUID(
                0xE27362F1,
                0xB136,
                0x41D1,
                0x95,
                0x94,
                0x3A,
                0x7E,
                0x4F,
                0xEB,
                0xF2,
                0xD1
            )

            # MF_MT_VIDEO_RENDERER_EXTENSION_PROFILE
            # {8437D4B9-D448-4fcd-9B6B-839BF96C7798}
            # Type: LPCWSTR
            # Contains a string that matches an entry in a MediaRendererEffect
            # Manifest's
            # VideoRendererExtensionProfiles list to select which effect to
            # load
            MF_MT_VIDEO_RENDERER_EXTENSION_PROFILE = DEFINE_GUID(
                0x8437D4B9,
                0xD448,
                0x4FCD,
                0x9B,
                0x6B,
                0x83,
                0x9B,
                0xF9,
                0x6C,
                0x77,
                0x98
            )
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

        if NTDDI_VERSION >= NTDDI_WIN10_RS4:
            # MF_DECODER_FWD_CUSTOM_SEI_DECODE_ORDER
            # {f13bbe3c-36d4-410a-b985-7a951a1e6294}
            # Type: UINT32
            # Specifies that the SEI unit type to forward on output samples of
            # the decoder
            # shall be sent out in decode order (i.e. ahead of time)
            # This is required for downstream apps to process the SEI in
            # advance of receiving
            # the frame it is meant to be attached to
            MF_DECODER_FWD_CUSTOM_SEI_DECODE_ORDER = DEFINE_GUID(
                0xF13BBE3C,
                0x36D4,
                0x410A,
                0xB9,
                0x85,
                0x7A,
                0x95,
                0x1A,
                0x1E,
                0x62,
                0x94
            )
        # END IF  (NTDDI_VERSION >= NTDDI_WIN10_RS4)

        # AUDIO data
        # {37e48bf5-645e-4c5b-89de-ada9e29b696a} MF_MT_AUDIO_NUM_CHANNELS
        # {UINT32}
        MF_MT_AUDIO_NUM_CHANNELS = DEFINE_GUID(
            0x37E48BF5,
            0x645E,
            0x4C5B,
            0x89,
            0xDE,
            0xAD,
            0xA9,
            0xE2,
            0x9B,
            0x69,
            0x6A
        )

        # {5faeeae7-0290-4c31-9e8a-c534f68d9dba}
        # MF_MT_AUDIO_SAMPLES_PER_SECOND {UINT32}
        MF_MT_AUDIO_SAMPLES_PER_SECOND = DEFINE_GUID(
            0x5FAEEAE7,
            0x0290,
            0x4C31,
            0x9E,
            0x8A,
            0xC5,
            0x34,
            0xF6,
            0x8D,
            0x9D,
            0xBA
        )

        # {fb3b724a-cfb5-4319-aefe-6e42b2406132}
        # MF_MT_AUDIO_FLOAT_SAMPLES_PER_SECOND {double}
        MF_MT_AUDIO_FLOAT_SAMPLES_PER_SECOND = DEFINE_GUID(
            0xFB3B724A,
            0xCFB5,
            0x4319,
            0xAE,
            0xFE,
            0x6E,
            0x42,
            0xB2,
            0x40,
            0x61,
            0x32
        )

        # {1aab75c8-cfef-451c-ab95-ac034b8e1731}
        # MF_MT_AUDIO_AVG_BYTES_PER_SECOND {UINT32}
        MF_MT_AUDIO_AVG_BYTES_PER_SECOND = DEFINE_GUID(
            0x1AAB75C8,
            0xCFEF,
            0x451C,
            0xAB,
            0x95,
            0xAC,
            0x03,
            0x4B,
            0x8E,
            0x17,
            0x31
        )

        # {322de230-9eeb-43bd-ab7a-ff412251541d} MF_MT_AUDIO_BLOCK_ALIGNMENT
        # {UINT32}
        MF_MT_AUDIO_BLOCK_ALIGNMENT = DEFINE_GUID(
            0x322DE230,
            0x9EEB,
            0x43BD,
            0xAB,
            0x7A,
            0xFF,
            0x41,
            0x22,
            0x51,
            0x54,
            0x1D
        )

        # {f2deb57f-40fa-4764-aa33-ed4f2d1ff669} MF_MT_AUDIO_BITS_PER_SAMPLE
        # {UINT32}
        MF_MT_AUDIO_BITS_PER_SAMPLE = DEFINE_GUID(
            0xF2DEB57F,
            0x40FA,
            0x4764,
            0xAA,
            0x33,
            0xED,
            0x4F,
            0x2D,
            0x1F,
            0xF6,
            0x69
        )

        # {d9bf8d6a-9530-4b7c-9ddf-ff6fd58bbd06}
        # MF_MT_AUDIO_VALID_BITS_PER_SAMPLE {UINT32}
        MF_MT_AUDIO_VALID_BITS_PER_SAMPLE = DEFINE_GUID(
            0xD9BF8D6A,
            0x9530,
            0x4B7C,
            0x9D,
            0xDF,
            0xFF,
            0x6F,
            0xD5,
            0x8B,
            0xBD,
            0x06
        )

        # {aab15aac-e13a-4995-9222-501ea15c6877} MF_MT_AUDIO_SAMPLES_PER_BLOCK
        # {UINT32}
        MF_MT_AUDIO_SAMPLES_PER_BLOCK = DEFINE_GUID(
            0xAAB15AAC,
            0xE13A,
            0x4995,
            0x92,
            0x22,
            0x50,
            0x1E,
            0xA1,
            0x5C,
            0x68,
            0x77
        )

        # {55fb5765-644a-4caf-8479-938983bb1588}` MF_MT_AUDIO_CHANNEL_MASK
        # {UINT32}
        MF_MT_AUDIO_CHANNEL_MASK = DEFINE_GUID(
            0x55FB5765,
            0x644A,
            0x4CAF,
            0x84,
            0x79,
            0x93,
            0x89,
            0x83,
            0xBB,
            0x15,
            0x88
        )

        # MF_MT_AUDIO_FOLDDOWN_MATRIX stores folddown structure from
        # multichannel to stereo
        _MFFOLDDOWN_MATRIX._fields_ = [
            ('cbSize', UINT32),
            # number of source channels
            ('cSrcChannels', UINT32),
            # number of destination channels
            ('cDstChannels', UINT32),
            # mask
            ('dwChannelMask', UINT32),
            ('Coeff', LONG * 64),
        ]

        # {9d62927c-36be-4cf2-b5c4-a3926e3e8711}` MF_MT_AUDIO_FOLDDOWN_MATRIX
        # {BLOB, MFFOLDDOWN_MATRIX}
        MF_MT_AUDIO_FOLDDOWN_MATRIX = DEFINE_GUID(
            0x9D62927C,
            0x36BE,
            0x4CF2,
            0xB5,
            0xC4,
            0xA3,
            0x92,
            0x6E,
            0x3E,
            0x87,
            0x11
        )

        # {0x9d62927d-36be-4cf2-b5c4-a3926e3e8711}` MF_MT_AUDIO_WMADRC_PEAKREF
        # {UINT32}
        MF_MT_AUDIO_WMADRC_PEAKREF = DEFINE_GUID(
            0x9D62927D,
            0x36BE,
            0x4CF2,
            0xB5,
            0xC4,
            0xA3,
            0x92,
            0x6E,
            0x3E,
            0x87,
            0x11
        )

        # {0x9d62927e-36be-4cf2-b5c4-a3926e3e8711}`
        # MF_MT_AUDIO_WMADRC_PEAKTARGET {UINT32}
        MF_MT_AUDIO_WMADRC_PEAKTARGET = DEFINE_GUID(
            0x9D62927E,
            0x36BE,
            0x4CF2,
            0xB5,
            0xC4,
            0xA3,
            0x92,
            0x6E,
            0x3E,
            0x87,
            0x11
        )

        # {0x9d62927f-36be-4cf2-b5c4-a3926e3e8711}` MF_MT_AUDIO_WMADRC_AVGREF
        # {UINT32}
        MF_MT_AUDIO_WMADRC_AVGREF = DEFINE_GUID(
            0x9D62927F,
            0x36BE,
            0x4CF2,
            0xB5,
            0xC4,
            0xA3,
            0x92,
            0x6E,
            0x3E,
            0x87,
            0x11
        )

        # {0x9d629280-36be-4cf2-b5c4-a3926e3e8711}`
        # MF_MT_AUDIO_WMADRC_AVGTARGET {UINT32}
        MF_MT_AUDIO_WMADRC_AVGTARGET = DEFINE_GUID(
            0x9D629280,
            0x36BE,
            0x4CF2,
            0xB5,
            0xC4,
            0xA3,
            0x92,
            0x6E,
            0x3E,
            0x87,
            0x11
        )

        # MF_MT_AUDIO_PREFER_WAVEFORMATEX tells the converter to prefer a
        # plain WAVEFORMATEX rather than
        # a WAVEFORMATEXTENSIBLE when converting to a legacy type. It is set
        # by the WAVEFORMATEX.IMFMediaType
        # conversion routines when the original format block is a
        # non-extensible WAVEFORMATEX.
        # This preference can be overridden and does not guarantee that the
        # type can be correctly expressed
        # by a non-extensible type.
        # {a901aaba-e037-458a-bdf6-545be2074042}
        # MF_MT_AUDIO_PREFER_WAVEFORMATEX {UINT32 (BOOL)}
        MF_MT_AUDIO_PREFER_WAVEFORMATEX = DEFINE_GUID(
            0xA901AABA,
            0xE037,
            0x458A,
            0xBD,
            0xF6,
            0x54,
            0x5B,
            0xE2,
            0x07,
            0x40,
            0x42
        )

        if WINVER >= _WIN32_WINNT_WIN7:
            # AUDIO - AAC extra data
            # {BFBABE79-7434-4d1c-94F0-72A3B9E17188} MF_MT_AAC_PAYLOAD_TYPE
            # {UINT32}
            MF_MT_AAC_PAYLOAD_TYPE = DEFINE_GUID(
                0xBFBABE79,
                0x7434,
                0x4D1C,
                0x94,
                0xF0,
                0x72,
                0xA3,
                0xB9,
                0xE1,
                0x71,
                0x88
            )

            # {7632F0E6-9538-4d61-ACDA-EA29C8C14456}
            # MF_MT_AAC_AUDIO_PROFILE_LEVEL_INDICATION {UINT32}
            MF_MT_AAC_AUDIO_PROFILE_LEVEL_INDICATION = DEFINE_GUID(
                0x7632F0E6,
                0x9538,
                0x4D61,
                0xAC,
                0xDA,
                0xEA,
                0x29,
                0xC8,
                0xC1,
                0x44,
                0x56
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        if WINVER >= _WIN32_WINNT_WIN10:
            # AUDIO - FLAC extra data
            # {8B81ADAE-4B5A-4D40-8022-F38D09CA3C5C}
            # MF_MT_AUDIO_FLAC_MAX_BLOCK_SIZE {UINT32}
            MF_MT_AUDIO_FLAC_MAX_BLOCK_SIZE = DEFINE_GUID(
                0x8B81ADAE,
                0x4B5A,
                0x4D40,
                0x80,
                0x22,
                0xF3,
                0x8D,
                0x9,
                0xCA,
                0x3C,
                0x5C
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN10)

        if NTDDI_VERSION >= NTDDI_WIN10_RS2:
            # AUDIO - Spatial Audio Sample extra data
            # {DCFBA24A-2609-4240-A721-3FAEA76A4DF9}
            # MF_MT_SPATIAL_AUDIO_MAX_DYNAMIC_OBJECTS {UINT32}
            MF_MT_SPATIAL_AUDIO_MAX_DYNAMIC_OBJECTS = DEFINE_GUID(
                0xDCFBA24A,
                0x2609,
                0x4240,
                0xA7,
                0x21,
                0x3F,
                0xAE,
                0xA7,
                0x6A,
                0x4D,
                0xF9
            )

            # {2AB71BC0-6223-4BA7-AD64-7B94B47AE792}
            # MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_FORMAT_ID {GUID}
            MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_FORMAT_ID = DEFINE_GUID(
                0x2AB71BC0,
                0x6223,
                0x4BA7,
                0xAD,
                0x64,
                0x7B,
                0x94,
                0xB4,
                0x7A,
                0xE7,
                0x92
            )

            # {094BA8BE-D723-489F-92FA-766777B34726}
            # MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_LENGTH {UINT32}
            MF_MT_SPATIAL_AUDIO_OBJECT_METADATA_LENGTH = DEFINE_GUID(
                0x94BA8BE,
                0xD723,
                0x489F,
                0x92,
                0xFA,
                0x76,
                0x67,
                0x77,
                0xB3,
                0x47,
                0x26
            )

            # {11AA80B4-E0DA-47C6-8060-96C1259AE50D}
            # MF_MT_SPATIAL_AUDIO_MAX_METADATA_ITEMS {UINT32}
            MF_MT_SPATIAL_AUDIO_MAX_METADATA_ITEMS = DEFINE_GUID(
                0x11AA80B4,
                0xE0DA,
                0x47C6,
                0x80,
                0x60,
                0x96,
                0xC1,
                0x25,
                0x9A,
                0xE5,
                0xD
            )

            # {83E96EC9-1184-417E-8254-9F269158FC06}
            # MF_MT_SPATIAL_AUDIO_MIN_METADATA_ITEM_OFFSET_SPACING {UINT32}
            MF_MT_SPATIAL_AUDIO_MIN_METADATA_ITEM_OFFSET_SPACING = DEFINE_GUID(
                0x83E96EC9,
                0x1184,
                0x417E,
                0x82,
                0x54,
                0x9F,
                0x26,
                0x91,
                0x58,
                0xFC,
                0x6
            )

            # {6842F6E7-D43E-4EBB-9C9C-C96F41784863}
            # MF_MT_SPATIAL_AUDIO_DATA_PRESENT {UINT32 (BOOL)}
            MF_MT_SPATIAL_AUDIO_DATA_PRESENT = DEFINE_GUID(
                0x6842F6E7,
                0xD43E,
                0x4EBB,
                0x9C,
                0x9C,
                0xC9,
                0x6F,
                0x41,
                0x78,
                0x48,
                0x63
            )
        # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS2)

        # VIDEO core data
        # {1652c33d-d6b2-4012-b834-72030849a37d} MF_MT_FRAME_SIZE
        # {UINT64 (HI32(Width),LO32(Height))}
        MF_MT_FRAME_SIZE = DEFINE_GUID(
            0x1652C33D,
            0xD6B2,
            0x4012,
            0xB8,
            0x34,
            0x72,
            0x03,
            0x08,
            0x49,
            0xA3,
            0x7D
        )

        # {c459a2e8-3d2c-4e44-b132-fee5156c7bb0} MF_MT_FRAME_RATE
        # {UINT64 (HI32(Numerator),LO32(Denominator))}
        MF_MT_FRAME_RATE = DEFINE_GUID(
            0xC459A2E8,
            0x3D2C,
            0x4E44,
            0xB1,
            0x32,
            0xFE,
            0xE5,
            0x15,
            0x6C,
            0x7B,
            0xB0
        )

        # {c6376a1e-8d0a-4027-be45-6d9a0ad39bb6} MF_MT_PIXEL_ASPECT_RATIO
        # {UINT64 (HI32(Numerator),LO32(Denominator))}
        MF_MT_PIXEL_ASPECT_RATIO = DEFINE_GUID(
            0xC6376A1E,
            0x8D0A,
            0x4027,
            0xBE,
            0x45,
            0x6D,
            0x9A,
            0x0A,
            0xD3,
            0x9B,
            0xB6
        )

        # {8772f323-355a-4cc7-bb78-6d61a048ae82} MF_MT_DRM_FLAGS
        # {UINT32 (anyof MFVideoDRMFlags)}
        MF_MT_DRM_FLAGS = DEFINE_GUID(
            0x8772F323,
            0x355A,
            0x4CC7,
            0xBB,
            0x78,
            0x6D,
            0x61,
            0xA0,
            0x48,
            0xAE,
            0x82
        )
        if WINVER >= _WIN32_WINNT_WIN8:
            # {24974215-1B7B-41e4-8625-AC469F2DEDAA}
            # MF_MT_TIMESTAMP_CAN_BE_DTS {UINT32 (BOOL)}
            MF_MT_TIMESTAMP_CAN_BE_DTS = DEFINE_GUID(
                0x24974215,
                0x1B7B,
                0x41E4,
                0x86,
                0x25,
                0xAC,
                0x46,
                0x9F,
                0x2D,
                0xED,
                0xAA
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)


        class _MFVideoDRMFlags(ENUM):
            MFVideoDRMFlag_None = 0
            MFVideoDRMFlag_AnalogProtected = 1
            MFVideoDRMFlag_DigitallyProtected = 2

        MFVideoDRMFlags = _MFVideoDRMFlags

        # {4d0e73e5-80ea-4354-a9d0-1176ceb028ea} MF_MT_PAD_CONTROL_FLAGS
        # {UINT32 (oneof MFVideoPadFlags)}
        MF_MT_PAD_CONTROL_FLAGS = DEFINE_GUID(
            0x4D0E73E5,
            0x80EA,
            0x4354,
            0xA9,
            0xD0,
            0x11,
            0x76,
            0xCE,
            0xB0,
            0x28,
            0xEA
        )


        class _MFVideoPadFlags(ENUM):
            MFVideoPadFlag_PAD_TO_None = 0
            MFVideoPadFlag_PAD_TO_4x3 = 1
            MFVideoPadFlag_PAD_TO_16x9 = 2

        MFVideoPadFlags = _MFVideoPadFlags

        # {68aca3cc-22d0-44e6-85f8-28167197fa38} MF_MT_SOURCE_CONTENT_HINT
        # {UINT32 (oneof MFVideoSrcContentHintFlags)}
        MF_MT_SOURCE_CONTENT_HINT = DEFINE_GUID(
            0x68ACA3CC,
            0x22D0,
            0x44E6,
            0x85,
            0xF8,
            0x28,
            0x16,
            0x71,
            0x97,
            0xFA,
            0x38
        )


        class _MFVideoSrcContentHintFlags(ENUM):
            MFVideoSrcContentHintFlag_None = 0
            MFVideoSrcContentHintFlag_16x9 = 1
            MFVideoSrcContentHintFlag_235_1 = 2

        MFVideoSrcContentHintFlags = _MFVideoSrcContentHintFlags

        # {65df2370-c773-4c33-aa64-843e068efb0c} MF_MT_CHROMA_SITING
        # {UINT32 (anyof MFVideoChromaSubsampling)}
        MF_MT_VIDEO_CHROMA_SITING = DEFINE_GUID(
            0x65DF2370,
            0xC773,
            0x4C33,
            0xAA,
            0x64,
            0x84,
            0x3E,
            0x06,
            0x8E,
            0xFB,
            0x0C
        )

        # {e2724bb8-e676-4806-b4b2-a8d6efb44ccd} MF_MT_INTERLACE_MODE
        # {UINT32 (oneof MFVideoInterlaceMode)}
        MF_MT_INTERLACE_MODE = DEFINE_GUID(
            0xE2724BB8,
            0xE676,
            0x4806,
            0xB4,
            0xB2,
            0xA8,
            0xD6,
            0xEF,
            0xB4,
            0x4C,
            0xCD
        )

        # {5fb0fce9-be5c-4935-a811-ec838f8eed93} MF_MT_TRANSFER_FUNCTION
        # {UINT32 (oneof MFVideoTransferFunction)}
        MF_MT_TRANSFER_FUNCTION = DEFINE_GUID(
            0x5FB0FCE9,
            0xBE5C,
            0x4935,
            0xA8,
            0x11,
            0xEC,
            0x83,
            0x8F,
            0x8E,
            0xED,
            0x93
        )

        # {dbfbe4d7-0740-4ee0-8192-850ab0e21935} MF_MT_VIDEO_PRIMARIES
        # {UINT32 (oneof MFVideoPrimaries)}
        MF_MT_VIDEO_PRIMARIES = DEFINE_GUID(
            0xDBFBE4D7,
            0x0740,
            0x4EE0,
            0x81,
            0x92,
            0x85,
            0x0A,
            0xB0,
            0xE2,
            0x19,
            0x35
        )

        # TODO: switch to RS define once it exists (see: 5312604)
        if WINVER >= _WIN32_WINNT_WIN10:
            # MF_MT_MAX_LUMINANCE_LEVEL specifies the maximum luminance level
            # of the content in Nits.
            # Has the same semantics as MaxCLL as defined in CEA-861.3
            # {50253128-C110-4de4-98AE-46A324FAE6DA} MF_MT_MAX_LUMINANCE_LEVEL
            # {UINT32}
            MF_MT_MAX_LUMINANCE_LEVEL = DEFINE_GUID(
                0x50253128,
                0xC110,
                0x4DE4,
                0x98,
                0xAE,
                0x46,
                0xA3,
                0x24,
                0xFA,
                0xE6,
                0xDA
            )

            # MF_MT_MAX_FRAME_AVERAGE_LUMINANCE_LEVEL specifies the maximum
            # average per-frame
            # luminance level of the content in Nits.
            # Has the same semantics as MaxFALL as defined in CEA-861.3
            # {58D4BF57-6F52-4733-A195-A9E29ECF9E27}
            # MF_MT_MAX_FRAME_AVERAGE_LUMINANCE_LEVEL {UINT32}
            MF_MT_MAX_FRAME_AVERAGE_LUMINANCE_LEVEL = DEFINE_GUID(
                0x58D4BF57,
                0x6F52,
                0x4733,
                0xA1,
                0x95,
                0xA9,
                0xE2,
                0x9E,
                0xCF,
                0x9E,
                0x27
            )

            # MF_MT_MAX_MASTERING_LUMINANCE specifies the maximum luminance of
            # the display
            # the content was authored on in Nits.
            # Has the same semantics as max_display_mastering_luminance as
            # defined in ST.2086
            # {D6C6B997-272F-4ca1-8D00-8042111A0FF6}
            # MF_MT_MAX_MASTERING_LUMINANCE {UINT32}
            MF_MT_MAX_MASTERING_LUMINANCE = DEFINE_GUID(
                0xD6C6B997,
                0x272F,
                0x4CA1,
                0x8D,
                0x0,
                0x80,
                0x42,
                0x11,
                0x1A,
                0xF,
                0xF6
            )

            # MF_MT_MIN_MASTERING_LUMINANCE specifies the maximum luminance of
            # the display
            # the content was authored on in 0.0001 Nits.
            # Has the same semantics as min_display_mastering_luminance as
            # defined in ST.2086
            # {839A4460-4E7E-4b4f-AE79-CC08905C7B27}
            # MF_MT_MIN_MASTERING_LUMINANCE {UINT32}
            MF_MT_MIN_MASTERING_LUMINANCE = DEFINE_GUID(
                0x839A4460,
                0x4E7E,
                0x4B4F,
                0xAE,
                0x79,
                0xCC,
                0x8,
                0x90,
                0x5C,
                0x7B,
                0x27
            )

            # MF_MT_DECODER_USE_MAX_RESOLUTION hints the decoder should
            # allocate worst
            # case supported resolution whenever possible
            # {4c547c24-af9a-4f38-96ad-978773cf53e7}
            # MF_MT_DECODER_USE_MAX_RESOLUTION {UINT32 (BOOL)}
            MF_MT_DECODER_USE_MAX_RESOLUTION = DEFINE_GUID(
                0x4C547C24,
                0xAF9A,
                0x4F38,
                0x96,
                0xAD,
                0x97,
                0x87,
                0x73,
                0xCF,
                0x53,
                0xE7
            )

            # MF_MT_DECODER_MAX_DPB_COUNT is a value that hints to the decoder
            # that the current
            # decoding session will never require more than the specified
            # number of decode surfaces
            # {67BE144C-88B7-4CA9-9628-C808D5262217}
            # MF_MT_DECODER_MAX_DPB_COUNT {UINT32}
            MF_MT_DECODER_MAX_DPB_COUNT = DEFINE_GUID(
                0x67BE144C,
                0x88B7,
                0x4CA9,
                0x96,
                0x28,
                0xC8,
                0x8,
                0xD5,
                0x26,
                0x22,
                0x17
            )
        # END IF   (WINVER > _WIN32_WINNT_WIN10)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # {47537213-8cfb-4722-aa34-fbc9e24d77b8} MF_MT_CUSTOM_VIDEO_PRIMARIES
        # {BLOB (MT_CUSTOM_VIDEO_PRIMARIES)}
        MF_MT_CUSTOM_VIDEO_PRIMARIES = DEFINE_GUID(
            0x47537213,
            0x8CFB,
            0x4722,
            0xAA,
            0x34,
            0xFB,
            0xC9,
            0xE2,
            0x4D,
            0x77,
            0xB8
        )

        _MT_CUSTOM_VIDEO_PRIMARIES._fields_ = [
            ('fRx', FLOAT),
            ('fRy', FLOAT),
            ('fGx', FLOAT),
            ('fGy', FLOAT),
            ('fBx', FLOAT),
            ('fBy', FLOAT),
            ('fWx', FLOAT),
            ('fWy', FLOAT),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # {3e23d450-2c75-4d25-a00e-b91670d12327} MF_MT_YUV_MATRIX
        # {UINT32 (oneof MFVideoTransferMatrix)}
        MF_MT_YUV_MATRIX = DEFINE_GUID(
            0x3E23D450,
            0x2C75,
            0x4D25,
            0xA0,
            0x0E,
            0xB9,
            0x16,
            0x70,
            0xD1,
            0x23,
            0x27
        )

        # {53a0529c-890b-4216-8bf9-599367ad6d20} MF_MT_VIDEO_LIGHTING
        # {UINT32 (oneof MFVideoLighting)}
        MF_MT_VIDEO_LIGHTING = DEFINE_GUID(
            0x53A0529C,
            0x890B,
            0x4216,
            0x8B,
            0xF9,
            0x59,
            0x93,
            0x67,
            0xAD,
            0x6D,
            0x20
        )

        # {c21b8ee5-b956-4071-8daf-325edf5cab11} MF_MT_VIDEO_NOMINAL_RANGE
        # {UINT32 (oneof MFNominalRange)}
        MF_MT_VIDEO_NOMINAL_RANGE = DEFINE_GUID(
            0xC21B8EE5,
            0xB956,
            0x4071,
            0x8D,
            0xAF,
            0x32,
            0x5E,
            0xDF,
            0x5C,
            0xAB,
            0x11
        )

        # {66758743-7e5f-400d-980a-aa8596c85696} MF_MT_GEOMETRIC_APERTURE
        # {BLOB (MFVideoArea)}
        MF_MT_GEOMETRIC_APERTURE = DEFINE_GUID(
            0x66758743,
            0x7E5F,
            0x400D,
            0x98,
            0x0A,
            0xAA,
            0x85,
            0x96,
            0xC8,
            0x56,
            0x96
        )

        # {d7388766-18fe-48c6-a177-ee894867c8c4}
        # MF_MT_MINIMUM_DISPLAY_APERTURE {BLOB (MFVideoArea)}
        MF_MT_MINIMUM_DISPLAY_APERTURE = DEFINE_GUID(
            0xD7388766,
            0x18FE,
            0x48C6,
            0xA1,
            0x77,
            0xEE,
            0x89,
            0x48,
            0x67,
            0xC8,
            0xC4
        )

        # {79614dde-9187-48fb-b8c7-4d52689de649} MF_MT_PAN_SCAN_APERTURE
        # {BLOB (MFVideoArea)}
        MF_MT_PAN_SCAN_APERTURE = DEFINE_GUID(
            0x79614DDE,
            0x9187,
            0x48FB,
            0xB8,
            0xC7,
            0x4D,
            0x52,
            0x68,
            0x9D,
            0xE6,
            0x49
        )

        # {4b7f6bc3-8b13-40b2-a993-abf630b8204e} MF_MT_PAN_SCAN_ENABLED
        # {UINT32 (BOOL)}
        MF_MT_PAN_SCAN_ENABLED = DEFINE_GUID(
            0x4B7F6BC3,
            0x8B13,
            0x40B2,
            0xA9,
            0x93,
            0xAB,
            0xF6,
            0x30,
            0xB8,
            0x20,
            0x4E
        )

        # {20332624-fb0d-4d9e-bd0d-cbf6786c102e} MF_MT_AVG_BITRATE   {UINT32}
        MF_MT_AVG_BITRATE = DEFINE_GUID(
            0x20332624,
            0xFB0D,
            0x4D9E,
            0xBD,
            0x0D,
            0xCB,
            0xF6,
            0x78,
            0x6C,
            0x10,
            0x2E
        )

        # {799cabd6-3508-4db4-a3c7-569cd533deb1} MF_MT_AVG_BIT_ERROR_RATE
        # {UINT32}
        MF_MT_AVG_BIT_ERROR_RATE = DEFINE_GUID(
            0x799CABD6,
            0x3508,
            0x4DB4,
            0xA3,
            0xC7,
            0x56,
            0x9C,
            0xD5,
            0x33,
            0xDE,
            0xB1
        )

        # {c16eb52b-73a1-476f-8d62-839d6a020652} MF_MT_MAX_KEYFRAME_SPACING
        # {UINT32}
        MF_MT_MAX_KEYFRAME_SPACING = DEFINE_GUID(
            0xC16EB52B,
            0x73A1,
            0x476F,
            0x8D,
            0x62,
            0x83,
            0x9D,
            0x6A,
            0x02,
            0x06,
            0x52
        )

        # {b6bc765f-4c3b-40a4-bd51-2535b66fe09d} MF_MT_USER_DATA    {BLOB}
        MF_MT_USER_DATA = DEFINE_GUID(
            0xB6BC765F,
            0x4C3B,
            0x40A4,
            0xBD,
            0x51,
            0x25,
            0x35,
            0xB6,
            0x6F,
            0xE0,
            0x9D
        )

        # {a505d3ac-f930-436e-8ede-93a509ce23b2} MF_MT_OUTPUT_BUFFER_NUM
        # {UINT32}
        MF_MT_OUTPUT_BUFFER_NUM = DEFINE_GUID(
            0xA505D3AC,
            0xF930,
            0x436E,
            0x8E,
            0xDE,
            0x93,
            0xA5,
            0x09,
            0xCE,
            0x23,
            0xB2
        )

        # TODO: Fix when GovM has the right ifdef check
        if WINVER >= _WIN32_WINNT_WIN10:
            # /
            # {0xbb12d222,0x2bdb,0x425e,0x91,0xec,0x23,0x08,0xe1,0x89,0xa5,0x8f} MF_MT_REALTIME_CONTENT UINT32 (0 or 1)
            #
            MF_MT_REALTIME_CONTENT = DEFINE_GUID(
                0xBB12D222,
                0x2BDB,
                0x425E,
                0x91,
                0xEC,
                0x23,
                0x08,
                0xE1,
                0x89,
                0xA5,
                0x8F
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN10
        # VIDEO - uncompressed format data
        # {644b4e48-1e02-4516-b0eb-c01ca9d49ac6} MF_MT_DEFAULT_STRIDE
        # {UINT32 (INT32)} // in bytes
        MF_MT_DEFAULT_STRIDE = DEFINE_GUID(
            0x644B4E48,
            0x1E02,
            0x4516,
            0xB0,
            0xEB,
            0xC0,
            0x1C,
            0xA9,
            0xD4,
            0x9A,
            0xC6
        )
        # {6d283f42-9846-4410-afd9-654d503b1a54} MF_MT_PALETTE
        # {BLOB (array of MFPaletteEntry - usually 256)}
        MF_MT_PALETTE = DEFINE_GUID(
            0x6D283F42,
            0x9846,
            0x4410,
            0xAF,
            0xD9,
            0x65,
            0x4D,
            0x50,
            0x3B,
            0x1A,
            0x54
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # the following is only used for legacy data that was stuck at the end
        # of the format block when the type
        # was converted from a VIDEOINFOHEADER or VIDEOINFOHEADER2 block in an
        # AM_MEDIA_TYPE.
        # {73d1072d-1870-4174-a063-29ff4ff6c11e}
        MF_MT_AM_FORMAT_TYPE = DEFINE_GUID(
            0x73D1072D,
            0x1870,
            0x4174,
            0xA0,
            0x63,
            0x29,
            0xFF,
            0x4F,
            0xF6,
            0xC1,
            0x1E
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # VIDEO - Generic compressed video extra data
        # {ad76a80b-2d5c-4e0b-b375-64e520137036} MF_MT_VIDEO_PROFILE
        # {UINT32} This is an alias of MF_MT_MPEG2_PROFILE
        MF_MT_VIDEO_PROFILE = DEFINE_GUID(
            0xAD76A80B,
            0x2D5C,
            0x4E0B,
            0xB3,
            0x75,
            0x64,
            0xE5,
            0x20,
            0x13,
            0x70,
            0x36
        )

        # {96f66574-11c5-4015-8666-bff516436da7} MF_MT_VIDEO_LEVEL   {UINT32}
        # This is an alias of MF_MT_MPEG2_LEVEL
        MF_MT_VIDEO_LEVEL = DEFINE_GUID(
            0x96F66574,
            0x11C5,
            0x4015,
            0x86,
            0x66,
            0xBF,
            0xF5,
            0x16,
            0x43,
            0x6D,
            0xA7
        )

        # VIDEO - MPEG1/2 extra data
        # {91f67885-4333-4280-97cd-bd5a6c03a06e} MF_MT_MPEG_START_TIME_CODE
        # {UINT32}
        MF_MT_MPEG_START_TIME_CODE = DEFINE_GUID(
            0x91F67885,
            0x4333,
            0x4280,
            0x97,
            0xCD,
            0xBD,
            0x5A,
            0x6C,
            0x03,
            0xA0,
            0x6E
        )

        # {ad76a80b-2d5c-4e0b-b375-64e520137036} MF_MT_MPEG2_PROFILE
        # {UINT32 (oneof AM_MPEG2Profile)}
        MF_MT_MPEG2_PROFILE = DEFINE_GUID(
            0xAD76A80B,
            0x2D5C,
            0x4E0B,
            0xB3,
            0x75,
            0x64,
            0xE5,
            0x20,
            0x13,
            0x70,
            0x36
        )

        # {96f66574-11c5-4015-8666-bff516436da7} MF_MT_MPEG2_LEVEL
        # {UINT32 (oneof AM_MPEG2Level)}
        MF_MT_MPEG2_LEVEL = DEFINE_GUID(
            0x96F66574,
            0x11C5,
            0x4015,
            0x86,
            0x66,
            0xBF,
            0xF5,
            0x16,
            0x43,
            0x6D,
            0xA7
        )

        # {31e3991d-f701-4b2f-b426-8ae3bda9e04b} MF_MT_MPEG2_FLAGS
        # {UINT32 (anyof AMMPEG2_xxx flags)}
        MF_MT_MPEG2_FLAGS = DEFINE_GUID(
            0x31E3991D,
            0xF701,
            0x4B2F,
            0xB4,
            0x26,
            0x8A,
            0xE3,
            0xBD,
            0xA9,
            0xE0,
            0x4B
        )

        # {3c036de7-3ad0-4c9e-9216-ee6d6ac21cb3} MF_MT_MPEG_SEQUENCE_HEADER
        # {BLOB}
        MF_MT_MPEG_SEQUENCE_HEADER = DEFINE_GUID(
            0x3C036DE7,
            0x3AD0,
            0x4C9E,
            0x92,
            0x16,
            0xEE,
            0x6D,
            0x6A,
            0xC2,
            0x1C,
            0xB3
        )

        # {A20AF9E8-928A-4B26-AAA9-F05C74CAC47C} MF_MT_MPEG2_STANDARD
        # {UINT32 (0 for default MPEG2, 1 to use ATSC standard, 2 to use DVB standard, 3 to use ARIB standard)}
        #
        MF_MT_MPEG2_STANDARD = DEFINE_GUID(
            0xA20AF9E8,
            0x928A,
            0x4B26,
            0xAA,
            0xA9,
            0xF0,
            0x5C,
            0x74,
            0xCA,
            0xC4,
            0x7C
        )

        # {5229BA10-E29D-4F80-A59C-DF4F180207D2} MF_MT_MPEG2_TIMECODE
        # {UINT32 (0 for no timecode, 1 to append an 4 byte timecode to the front of each transport packet)}
        #
        MF_MT_MPEG2_TIMECODE = DEFINE_GUID(
            0x5229BA10,
            0xE29D,
            0x4F80,
            0xA5,
            0x9C,
            0xDF,
            0x4F,
            0x18,
            0x2,
            0x7,
            0xD2
        )

        # {825D55E4-4F12-4197-9EB3-59B6E4710F06} MF_MT_MPEG2_CONTENT_PACKET
        # {UINT32 (0 for no content packet, 1 to append a 14 byte Content Packet header according to the ARIB specification to the beginning a transport packet at 200-1000 ms intervals.)}
        #
        MF_MT_MPEG2_CONTENT_PACKET = DEFINE_GUID(
            0x825D55E4,
            0x4F12,
            0x4197,
            0x9E,
            0xB3,
            0x59,
            0xB6,
            0xE4,
            0x71,
            0xF,
            0x6
        )

        # {91a49eb5-1d20-4b42-ace8-804269bf95ed}
        # MF_MT_MPEG2_ONE_FRAME_PER_PACKET
        # {UINT32 (BOOL) -- 0 for default behavior of splitting large video frames into multiple PES packets, 1 for always putting a full frame inside a PES packet, even if that requires setting the PES packet size to undefined (0)}
        #
        MF_MT_MPEG2_ONE_FRAME_PER_PACKET = DEFINE_GUID(
            0x91A49EB5,
            0x1D20,
            0x4B42,
            0xAC,
            0xE8,
            0x80,
            0x42,
            0x69,
            0xBF,
            0x95,
            0xED
        )

        # {168f1b4a-3e91-450f-aea7-e4baeadae5ba} MF_MT_MPEG2_HDCP
        # {UINT32 (BOOL) -- 0 for default behavior of clear MPEG2 stream, 1 for adding the HDCP descriptor to the PMT
        #
        MF_MT_MPEG2_HDCP = DEFINE_GUID(
            0x168F1B4A,
            0x3E91,
            0x450F,
            0xAE,
            0xA7,
            0xE4,
            0xBA,
            0xEA,
            0xDA,
            0xE5,
            0xBA
        )
        # VIDEO - H264 extra data
        # {F5929986-4C45-4FBB-BB49-6CC534D05B9B}
        # {UINT32, UVC 1.5 H.264 format descriptor: bMaxCodecConfigDelay}
        MF_MT_H264_MAX_CODEC_CONFIG_DELAY = DEFINE_GUID(
            0xF5929986,
            0x4C45,
            0x4FBB,
            0xBB,
            0x49,
            0x6C,
            0xC5,
            0x34,
            0xD0,
            0x5B,
            0x9B
        )
        # {C8BE1937-4D64-4549-8343-A8086C0BFDA5}
        # {UINT32, UVC 1.5 H.264 format descriptor: bmSupportedSliceModes}
        MF_MT_H264_SUPPORTED_SLICE_MODES = DEFINE_GUID(
            0xC8BE1937,
            0x4D64,
            0x4549,
            0x83,
            0x43,
            0xA8,
            0x8,
            0x6C,
            0xB,
            0xFD,
            0xA5
        )
        # {89A52C01-F282-48D2-B522-22E6AE633199}
        # {UINT32, UVC 1.5 H.264 format descriptor: bmSupportedSyncFrameTypes}
        MF_MT_H264_SUPPORTED_SYNC_FRAME_TYPES = DEFINE_GUID(
            0x89A52C01,
            0xF282,
            0x48D2,
            0xB5,
            0x22,
            0x22,
            0xE6,
            0xAE,
            0x63,
            0x31,
            0x99
        )
        # {E3854272-F715-4757-BA90-1B696C773457}
        # {UINT32, UVC 1.5 H.264 format descriptor: bResolutionScaling}
        MF_MT_H264_RESOLUTION_SCALING = DEFINE_GUID(
            0xE3854272,
            0xF715,
            0x4757,
            0xBA,
            0x90,
            0x1B,
            0x69,
            0x6C,
            0x77,
            0x34,
            0x57
        )
        # {9EA2D63D-53F0-4A34-B94E-9DE49A078CB3}
        # {UINT32, UVC 1.5 H.264 format descriptor: bSimulcastSupport}
        MF_MT_H264_SIMULCAST_SUPPORT = DEFINE_GUID(
            0x9EA2D63D,
            0x53F0,
            0x4A34,
            0xB9,
            0x4E,
            0x9D,
            0xE4,
            0x9A,
            0x7,
            0x8C,
            0xB3
        )
        # {6A8AC47E-519C-4F18-9BB3-7EEAAEA5594D}
        # {UINT32, UVC 1.5 H.264 format descriptor: bmSupportedRateControlModes}
        #
        MF_MT_H264_SUPPORTED_RATE_CONTROL_MODES = DEFINE_GUID(
            0x6A8AC47E,
            0x519C,
            0x4F18,
            0x9B,
            0xB3,
            0x7E,
            0xEA,
            0xAE,
            0xA5,
            0x59,
            0x4D
        )
        # {45256D30-7215-4576-9336-B0F1BCD59BB2}
        # {Blob of size 20 * (ctypes.sizeof(WORD), UVC 1.5 H.264 format descriptor: wMaxMBperSec*}
        #
        MF_MT_H264_MAX_MB_PER_SEC = DEFINE_GUID(
            0x45256D30,
            0x7215,
            0x4576,
            0x93,
            0x36,
            0xB0,
            0xF1,
            0xBC,
            0xD5,
            0x9B,
            0xB2
        )
        # {60B1A998-DC01-40CE-9736-ABA845A2DBDC}
        # {UINT32, UVC 1.5 H.264 frame descriptor: bmSupportedUsages}
        MF_MT_H264_SUPPORTED_USAGES = DEFINE_GUID(
            0x60B1A998,
            0xDC01,
            0x40CE,
            0x97,
            0x36,
            0xAB,
            0xA8,
            0x45,
            0xA2,
            0xDB,
            0xDC
        )
        # {BB3BD508-490A-11E0-99E4-1316DFD72085}
        # {UINT32, UVC 1.5 H.264 frame descriptor: bmCapabilities}
        MF_MT_H264_CAPABILITIES = DEFINE_GUID(
            0xBB3BD508,
            0x490A,
            0x11E0,
            0x99,
            0xE4,
            0x13,
            0x16,
            0xDF,
            0xD7,
            0x20,
            0x85
        )
        # {F8993ABE-D937-4A8F-BBCA-6966FE9E1152}
        # {UINT32, UVC 1.5 H.264 frame descriptor: bmSVCCapabilities}
        MF_MT_H264_SVC_CAPABILITIES = DEFINE_GUID(
            0xF8993ABE,
            0xD937,
            0x4A8F,
            0xBB,
            0xCA,
            0x69,
            0x66,
            0xFE,
            0x9E,
            0x11,
            0x52
        )
        # {359CE3A5-AF00-49CA-A2F4-2AC94CA82B61}
        # {UINT32, UVC 1.5 H.264 Probe/Commit Control: bUsage}
        MF_MT_H264_USAGE = DEFINE_GUID(
            0x359CE3A5,
            0xAF00,
            0x49CA,
            0xA2,
            0xF4,
            0x2A,
            0xC9,
            0x4C,
            0xA8,
            0x2B,
            0x61
        )
        # {705177D8-45CB-11E0-AC7D-B91CE0D72085}
        # {UINT32, UVC 1.5 H.264 Probe/Commit Control: bmRateControlModes}
        MF_MT_H264_RATE_CONTROL_MODES = DEFINE_GUID(
            0x705177D8,
            0x45CB,
            0x11E0,
            0xAC,
            0x7D,
            0xB9,
            0x1C,
            0xE0,
            0xD7,
            0x20,
            0x85
        )
        # {85E299B2-90E3-4FE8-B2F5-C067E0BFE57A}
        # {UINT64, UVC 1.5 H.264 Probe/Commit Control: bmLayoutPerStream}
        MF_MT_H264_LAYOUT_PER_STREAM = DEFINE_GUID(
            0x85E299B2,
            0x90E3,
            0x4FE8,
            0xB2,
            0xF5,
            0xC0,
            0x67,
            0xE0,
            0xBF,
            0xE5,
            0x7A
        )
        # According to Mpeg4 spec, SPS and PPS of H.264/HEVC codec could
        # appear in sample data.
        # description box. Mpeg4 sink filters out the SPS and PPS NALU and do
        # not support in band SPS and PPS NALU.
        # This attribute enables support for in band SPS and PPS to appear in
        # the elementary stream.
        # HEVC will have in-band parameter set by default with MP4 recording
        # for broad support. H.264 will have out - of - band parameter set by
        # default for historical reason.
        # {75DA5090-910B-4A03-896C-7B898FEEA5AF}
        MF_MT_IN_BAND_PARAMETER_SET = DEFINE_GUID(
            0x75DA5090,
            0x910B,
            0x4A03,
            0x89,
            0x6C,
            0x7B,
            0x89,
            0x8F,
            0xEE,
            0xA5,
            0xAF
        )
        # {54F486DD-9327-4F6D-80AB-6F709EBB4CCE}
        # {UINT32, FourCC of the track type in MPEG-4 used for binary streams}
        MF_MT_MPEG4_TRACK_TYPE = DEFINE_GUID(
            0x54F486DD,
            0x9327,
            0x4F6D,
            0x80,
            0xAB,
            0x6F,
            0x70,
            0x9E,
            0xBB,
            0x4C,
            0xCE
        )
        # INTERLEAVED - DV extra data
        # {84bd5d88-0fb8-4ac8-be4b-a8848bef98f3} MF_MT_DV_AAUX_SRC_PACK_0
        # {UINT32}
        MF_MT_DV_AAUX_SRC_PACK_0 = DEFINE_GUID(
            0x84BD5D88,
            0x0FB8,
            0x4AC8,
            0xBE,
            0x4B,
            0xA8,
            0x84,
            0x8B,
            0xEF,
            0x98,
            0xF3
        )
        # {f731004e-1dd1-4515-aabe-f0c06aa536ac} MF_MT_DV_AAUX_CTRL_PACK_0
        # {UINT32}
        MF_MT_DV_AAUX_CTRL_PACK_0 = DEFINE_GUID(
            0xF731004E,
            0x1DD1,
            0x4515,
            0xAA,
            0xBE,
            0xF0,
            0xC0,
            0x6A,
            0xA5,
            0x36,
            0xAC
        )
        # {720e6544-0225-4003-a651-0196563a958e} MF_MT_DV_AAUX_SRC_PACK_1
        # {UINT32}
        MF_MT_DV_AAUX_SRC_PACK_1 = DEFINE_GUID(
            0x720E6544,
            0x0225,
            0x4003,
            0xA6,
            0x51,
            0x01,
            0x96,
            0x56,
            0x3A,
            0x95,
            0x8E
        )
        # {cd1f470d-1f04-4fe0-bfb9-d07ae0386ad8} MF_MT_DV_AAUX_CTRL_PACK_1
        # {UINT32}
        MF_MT_DV_AAUX_CTRL_PACK_1 = DEFINE_GUID(
            0xCD1F470D,
            0x1F04,
            0x4FE0,
            0xBF,
            0xB9,
            0xD0,
            0x7A,
            0xE0,
            0x38,
            0x6A,
            0xD8
        )
        # {41402d9d-7b57-43c6-b129-2cb997f15009} MF_MT_DV_VAUX_SRC_PACK
        # {UINT32}
        MF_MT_DV_VAUX_SRC_PACK = DEFINE_GUID(
            0x41402D9D,
            0x7B57,
            0x43C6,
            0xB1,
            0x29,
            0x2C,
            0xB9,
            0x97,
            0xF1,
            0x50,
            0x09
        )
        # {2f84e1c4-0da1-4788-938e-0dfbfbb34b48} MF_MT_DV_VAUX_CTRL_PACK
        # {UINT32}
        MF_MT_DV_VAUX_CTRL_PACK = DEFINE_GUID(
            0x2F84E1C4,
            0x0DA1,
            0x4788,
            0x93,
            0x8E,
            0x0D,
            0xFB,
            0xFB,
            0xB3,
            0x4B,
            0x48
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    if WINVER >= _WIN32_WINNT_WIN7:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            # ARBITRARY
            # MT_ARBITRARY_HEADER stores information about the format of an
            # arbitrary media type
            _MT_ARBITRARY_HEADER._fields_ = [
                ('majortype', GUID),
                ('subtype', GUID),
                ('bFixedSizeSamples', BOOL),
                ('bTemporalCompression', BOOL),
                ('lSampleSize', ULONG),
                ('formattype', GUID),
            ]

            # {9E6BD6F5-0109-4f95-84AC-9309153A19FC} MF_MT_ARBITRARY_HEADER
            # {MT_ARBITRARY_HEADER}
            MF_MT_ARBITRARY_HEADER = DEFINE_GUID(
                0x9E6BD6F5,
                0x109,
                0x4F95,
                0x84,
                0xAC,
                0x93,
                0x9,
                0x15,
                0x3A,
                0x19,
                0xFC
            )

            # {5A75B249-0D7D-49a1-A1C3-E0D87F0CADE5} MF_MT_ARBITRARY_FORMAT
            # {Blob}
            MF_MT_ARBITRARY_FORMAT = DEFINE_GUID(
                0x5A75B249,
                0xD7D,
                0x49A1,
                0xA1,
                0xC3,
                0xE0,
                0xD8,
                0x7F,
                0xC,
                0xAD,
                0xE5
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            # IMAGE
            # {ED062CF4-E34E-4922-BE99-934032133D7C} MF_MT_IMAGE_LOSS_TOLERANT
            # {UINT32 (BOOL)}
            MF_MT_IMAGE_LOSS_TOLERANT = DEFINE_GUID(
                0xED062CF4,
                0xE34E,
                0x4922,
                0xBE,
                0x99,
                0x93,
                0x40,
                0x32,
                0x13,
                0x3D,
                0x7C
            )

            # MPEG-4 Media Type Attributes
            # {261E9D83-9529-4B8F-A111-8B9C950A81A9}
            # MF_MT_MPEG4_SAMPLE_DESCRIPTION {BLOB}
            MF_MT_MPEG4_SAMPLE_DESCRIPTION = DEFINE_GUID(
                0x261E9D83,
                0x9529,
                0x4B8F,
                0xA1,
                0x11,
                0x8B,
                0x9C,
                0x95,
                0x0A,
                0x81,
                0xA9
            )

            # {9aa7e155-b64a-4c1d-a500-455d600b6560}
            # MF_MT_MPEG4_CURRENT_SAMPLE_ENTRY {UINT32}
            MF_MT_MPEG4_CURRENT_SAMPLE_ENTRY = DEFINE_GUID(
                0x9AA7E155,
                0xB64A,
                0x4C1D,
                0xA5,
                0x00,
                0x45,
                0x5D,
                0x60,
                0x0B,
                0x65,
                0x60
            )

            if NTDDI_VERSION >= NTDDI_WIN10_RS4:
                # Ambisonics Stream Attribute
                # The value of this blob must be AMBISONICS_PARAMS structure
                # defined in AudioClient.h
                # {F715CF3E-A964-4C3F-94AE-9D6BA7264641}
                # MF_SD_AMBISONICS_SAMPLE3D_DESCRIPTION {BLOB}
                MF_SD_AMBISONICS_SAMPLE3D_DESCRIPTION = DEFINE_GUID(
                    0xF715CF3E,
                    0xA964,
                    0x4C3F,
                    0x94,
                    0xAE,
                    0x9D,
                    0x6B,
                    0xA7,
                    0x26,
                    0x46,
                    0x41
                )
            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            # Save original format information for AVI and WAV files
            # {d7be3fe0-2bc7-492d-b843-61a1919b70c3} MF_MT_ORIGINAL_4CC
            # (UINT32)
            MF_MT_ORIGINAL_4CC = DEFINE_GUID(
                0xD7BE3FE0,
                0x2BC7,
                0x492D,
                0xB8,
                0x43,
                0x61,
                0xA1,
                0x91,
                0x9B,
                0x70,
                0xC3
            )

            # {8cbbc843-9fd9-49c2-882f-a72586c408ad}
            # MF_MT_ORIGINAL_WAVE_FORMAT_TAG (UINT32)
            MF_MT_ORIGINAL_WAVE_FORMAT_TAG = DEFINE_GUID(
                0x8CBBC843,
                0x9FD9,
                0x49C2,
                0x88,
                0x2F,
                0xA7,
                0x25,
                0x86,
                0xC4,
                0x08,
                0xAD
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            # Video Capture Media Type Attributes
            # {D2E7558C-DC1F-403f-9A72-D28BB1EB3B5E}
            # MF_MT_FRAME_RATE_RANGE_MIN
            # {UINT64 (HI32(Numerator),LO32(Denominator))}
            MF_MT_FRAME_RATE_RANGE_MIN = DEFINE_GUID(
                0xD2E7558C,
                0xDC1F,
                0x403F,
                0x9A,
                0x72,
                0xD2,
                0x8B,
                0xB1,
                0xEB,
                0x3B,
                0x5E
            )

            # {E3371D41-B4CF-4a05-BD4E-20B88BB2C4D6}
            # MF_MT_FRAME_RATE_RANGE_MAX
            # {UINT64 (HI32(Numerator),LO32(Denominator))}
            MF_MT_FRAME_RATE_RANGE_MAX = DEFINE_GUID(
                0xE3371D41,
                0xB4CF,
                0x4A05,
                0xBD,
                0x4E,
                0x20,
                0xB8,
                0x8B,
                0xB2,
                0xC4,
                0xD6
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF   (WINVER >= _WIN32_WINNT_WIN7)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if WINVER >= _WIN32_WINNT_WIN8:
            # {9C27891A-ED7A-40e1-88E8-B22727A024EE} MF_LOW_LATENCY
            # {UINT32 (BOOL)}
            # Same GUID as CODECAPI_AVLowLatencyMode
            MF_LOW_LATENCY = DEFINE_GUID(
                0x9C27891A,
                0xED7A,
                0x40E1,
                0x88,
                0xE8,
                0xB2,
                0x27,
                0x27,
                0xA0,
                0x24,
                0xEE
            )

            # {E3F2E203-D445-4B8C-9211-AE390D3BA017} {UINT32} Maximum
            # macroblocks per second that can be handled by MFT
            MF_VIDEO_MAX_MB_PER_SEC = DEFINE_GUID(
                0xE3F2E203,
                0xD445,
                0x4B8C,
                0x92,
                0x11,
                0xAE,
                0x39,
                0xD,
                0x3B,
                0xA0,
                0x17
            )

            # {7086E16C-49C5-4201-882A-8538F38CF13A} {UINT32 (BOOL)}
            # Enables(0, default)/disables(1) the DXVA decode status queries
            # in decoders. When disabled decoder won't provide
            # MFSampleExtension_FrameCorruption
            MF_DISABLE_FRAME_CORRUPTION_INFO = DEFINE_GUID(
                0x7086E16C,
                0x49C5,
                0x4201,
                0x88,
                0x2A,
                0x85,
                0x38,
                0xF3,
                0x8C,
                0xF1,
                0x3A
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN8)

        # //////////////////////////////////////////////////////////////////////////////
        #
        # Camera Extrinsics
        # //////////////////////////////////////////////////////////////////////////////
        #
        _MF_FLOAT2._fields_ = [
            ('x', FLOAT),
            ('y', FLOAT),
        ]

        _MF_FLOAT3._fields_ = [
            ('x', FLOAT),
            ('y', FLOAT),
            ('z', FLOAT),
        ]

        _MF_QUATERNION._fields_ = [
            ('x', FLOAT),
            ('y', FLOAT),
            ('z', FLOAT),
            ('w', FLOAT),
        ]

        _MFCameraExtrinsic_CalibratedTransform._fields_ = [
            ('CalibrationId', GUID),
            ('Position', MF_FLOAT3),
            ('Orientation', MF_QUATERNION),
        ]

        _MFCameraExtrinsics._fields_ = [
            ('TransformCount', UINT32),
            ('CalibratedTransforms', MFCameraExtrinsic_CalibratedTransform * 1),
        ]

        # MFStreamExtension_CameraExtrinsics
        # {686196D0-13E2-41D9-9638-EF032C272A52}
        # Value type: Blob (MFCameraExtrinsics)
        # Stores camera extrinsics data on the stream's attribute store
        MFStreamExtension_CameraExtrinsics = DEFINE_GUID(
            0x686196D0,
            0x13E2,
            0x41D9,
            0x96,
            0x38,
            0xEF,
            0x3,
            0x2C,
            0x27,
            0x2A,
            0x52
        )

        # MFSampleExtension_CameraExtrinsics
        # {6B761658-B7EC-4C3B-8225-8623CABEC31D}
        # Value type: Blob (MFCameraExtrinsics)
        # Stores camera extrinsics data on the sample's (a.k.a frame)
        # attribute store
        MFSampleExtension_CameraExtrinsics = DEFINE_GUID(
            0x6B761658,
            0xB7EC,
            0x4C3B,
            0x82,
            0x25,
            0x86,
            0x23,
            0xCA,
            0xBE,
            0xC3,
            0x1D
        )

        # //////////////////////////////////////////////////////////////////////////////
        #
        # Camera Intrinsics
        # //////////////////////////////////////////////////////////////////////////////
        #
        _MFCameraIntrinsic_PinholeCameraModel._fields_ = [
            ('FocalLength', MF_FLOAT2),
            ('PrincipalPoint', MF_FLOAT2),
        ]

        _MFCameraIntrinsic_DistortionModel._fields_ = [
            ('Radial_k1', FLOAT),
            ('Radial_k2', FLOAT),
            ('Radial_k3', FLOAT),
            ('Tangential_p1', FLOAT),
            ('Tangential_p2', FLOAT),
        ]

        _MFPinholeCameraIntrinsic_IntrinsicModel._fields_ = [
            ('Width', UINT32),
            ('Height', UINT32),
            ('CameraModel', MFCameraIntrinsic_PinholeCameraModel),
            ('DistortionModel', MFCameraIntrinsic_DistortionModel),
        ]

        _MFPinholeCameraIntrinsics._fields_ = [
            ('IntrinsicModelCount', UINT32),
            ('IntrinsicModels', MFPinholeCameraIntrinsic_IntrinsicModel * 1),
        ]

        # MFStreamExtension_PinholeCameraIntrinsics
        # {DBAC0455-0EC8-4AEF-9C32-7A3EE3456F53}
        # Value type: Blob (MFPinholeCameraIntrinsics)
        # Stores camera intrinsics data on stream attribute store
        MFStreamExtension_PinholeCameraIntrinsics = DEFINE_GUID(
            0xDBAC0455,
            0xEC8,
            0x4AEF,
            0x9C,
            0x32,
            0x7A,
            0x3E,
            0xE3,
            0x45,
            0x6F,
            0x53
        )

        # MFSampleExtension_PinholeCameraIntrinsics
        # {4EE3B6C5-6A15-4E72-9761-70C1DB8B9FE3}
        # Value type: Blob (MFPinholeCameraIntrinsics)
        # Stores camera intrinsics data on the sample's (a.k.a frame)
        # attribute store
        MFSampleExtension_PinholeCameraIntrinsics = DEFINE_GUID(
            0x4EE3B6C5,
            0x6A15,
            0x4E72,
            0x97,
            0x61,
            0x70,
            0xC1,
            0xDB,
            0x8B,
            0x9F,
            0xE3
        )

        # //////////////////////////////////////////////////////////////////////////////
        #
        # ///////////////////////////// Media Type GUIDs
        # //////////////////////////////
        # //////////////////////////////////////////////////////////////////////////////
        #
        # Major types
        MFMediaType_Default = DEFINE_GUID(
            0x81A412E6,
            0x8103,
            0x4B06,
            0x85,
            0x7F,
            0x18,
            0x62,
            0x78,
            0x10,
            0x24,
            0xAC
        )
        MFMediaType_Audio = DEFINE_GUID(
            0x73647561,
            0x0000,
            0x0010,
            0x80,
            0x00,
            0x00,
            0xAA,
            0x00,
            0x38,
            0x9B,
            0x71
        )
        MFMediaType_Video = DEFINE_GUID(
            0x73646976,
            0x0000,
            0x0010,
            0x80,
            0x00,
            0x00,
            0xAA,
            0x00,
            0x38,
            0x9B,
            0x71
        )
        MFMediaType_Protected = DEFINE_GUID(
            0x7B4B6FE6,
            0x9D04,
            0x4494,
            0xBE,
            0x14,
            0x7E,
            0x0B,
            0xD0,
            0x76,
            0xC8,
            0xE4
        )
        MFMediaType_SAMI = DEFINE_GUID(
            0xE69669A0,
            0x3DCD,
            0x40CB,
            0x9E,
            0x2E,
            0x37,
            0x08,
            0x38,
            0x7C,
            0x06,
            0x16
        )
        MFMediaType_Script = DEFINE_GUID(
            0x72178C22,
            0xE45B,
            0x11D5,
            0xBC,
            0x2A,
            0x00,
            0xB0,
            0xD0,
            0xF3,
            0xF4,
            0xAB
        )
        MFMediaType_Image = DEFINE_GUID(
            0x72178C23,
            0xE45B,
            0x11D5,
            0xBC,
            0x2A,
            0x00,
            0xB0,
            0xD0,
            0xF3,
            0xF4,
            0xAB
        )
        MFMediaType_HTML = DEFINE_GUID(
            0x72178C24,
            0xE45B,
            0x11D5,
            0xBC,
            0x2A,
            0x00,
            0xB0,
            0xD0,
            0xF3,
            0xF4,
            0xAB
        )
        MFMediaType_Binary = DEFINE_GUID(
            0x72178C25,
            0xE45B,
            0x11D5,
            0xBC,
            0x2A,
            0x00,
            0xB0,
            0xD0,
            0xF3,
            0xF4,
            0xAB
        )
        MFMediaType_FileTransfer = DEFINE_GUID(
            0x72178C26,
            0xE45B,
            0x11D5,
            0xBC,
            0x2A,
            0x00,
            0xB0,
            0xD0,
            0xF3,
            0xF4,
            0xAB
        )
        MFMediaType_Stream = DEFINE_GUID(
            0xE436EB83,
            0x524F,
            0x11CE,
            0x9F,
            0x53,
            0x00,
            0x20,
            0xAF,
            0x0B,
            0xA7,
            0x70
        )
        MFMediaType_MultiplexedFrames = DEFINE_GUID(
            0x6EA542B0,
            0x281F,
            0x4231,
            0xA4,
            0x64,
            0xFE,
            0x2F,
            0x50,
            0x22,
            0x50,
            0x1C
        )
        MFMediaType_Subtitle = DEFINE_GUID(
            0xA6D13581,
            0xED50,
            0x4E65,
            0xAE,
            0x08,
            0x26,
            0x06,
            0x55,
            0x76,
            0xAA,
            0xCC
        )

        # TODO: switch to RS define once it exists (see: 5312604)
        if WINVER >= _WIN32_WINNT_WIN10:
            MFMediaType_Perception = DEFINE_GUID(
                0x597FF6F9,
                0x6EA2,
                0x4670,
                0x85,
                0xB4,
                0xEA,
                0x84,
                0x7,
                0x3F,
                0xE9,
                0x40
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN10)

        # Image subtypes (MFMediaType_Image major type)
        # JPEG subtype: same as GUID_ContainerFormatJpeg
        MFImageFormat_JPEG = DEFINE_GUID(
            0x19E4A5AA,
            0x5662,
            0x4FC5,
            0xA0,
            0xC0,
            0x17,
            0x58,
            0x02,
            0x8E,
            0x10,
            0x57
        )

        # RGB32 subtype: same as MFVideoFormat_RGB32
        MFImageFormat_RGB32 = DEFINE_GUID(
            0x00000016,
            0x0000,
            0x0010,
            0x80,
            0x00,
            0x00,
            0xAA,
            0x00,
            0x38,
            0x9B,
            0x71
        )

        # MPEG2 Stream subtypes (MFMediaType_Stream major type)
        MFStreamFormat_MPEG2Transport = DEFINE_GUID(
            0xE06D8023,
            0xDB46,
            0x11CF,
            0xB4,
            0xD1,
            0x00,
            0x80,
            0x5F,
            0x6C,
            0xBB,
            0xEA
        )
        MFStreamFormat_MPEG2Program = DEFINE_GUID(
            0x263067D1,
            0xD330,
            0x45DC,
            0xB6,
            0x69,
            0x34,
            0xD9,
            0x86,
            0xE4,
            0xE3,
            0xE1
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Representations
        AM_MEDIA_TYPE_REPRESENTATION = DEFINE_GUID(
            0xE2E42AD2,
            0x132C,
            0x491E,
            0xA2,
            0x68,
            0x3C,
            0x7C,
            0x2D,
            0xCA,
            0x18,
            0x1F
        )
        FORMAT_MFVideoFormat = DEFINE_GUID(
            0xAED4AB2D,
            0x7326,
            0x43CB,
            0x94,
            0x64,
            0xC8,
            0x79,
            0xCA,
            0xB9,
            0xC4,
            0x3D
        )

        # /////////////////////////////////////////////////////////////////////
        # //////////////////////// Media Type functions ///////////////////////
        # /////////////////////////////////////////////////////////////////////
        # Forward declaration

        class tagVIDEOINFOHEADER(ctypes.Structure):
            pass


        VIDEOINFOHEADER = tagVIDEOINFOHEADER


        class tagVIDEOINFOHEADER2(ctypes.Structure):
            pass


        VIDEOINFOHEADER2 = tagVIDEOINFOHEADER2


        class tagMPEG1VIDEOINFO(ctypes.Structure):
            pass


        MPEG1VIDEOINFO = tagMPEG1VIDEOINFO


        class tagMPEG2VIDEOINFO(ctypes.Structure):
            pass


        MPEG2VIDEOINFO = tagMPEG2VIDEOINFO


        class _AMMediaType(ctypes.Structure):
            pass


        AM_MEDIA_TYPE = _AMMediaType

        # STDAPI
        # MFValidateMediaTypeSize(
        # _In_                    GUID    FormatType,
        # _In_reads_bytes_opt_(cbSize) UINT8*  pBlock,
        # _In_                    UINT32  cbSize
        # );
        MFValidateMediaTypeSize = mfplat.MFValidateMediaTypeSize
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI
        # MFCreateMediaType(
        # _Outptr_ IMFMediaType**  ppMFType
        # );
        MFCreateMediaType = mfplat.MFCreateMediaType
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # STDAPI
        # MFCreateMFVideoFormatFromMFMediaType(
        # _In_        IMFMediaType*           pMFType,
        # _Out_       MFVIDEOFORMAT**         ppMFVF, // must be deleted with CoTaskMemFree
        # _Out_opt_   UINT32*                 pcbSize
        # );
        MFCreateMFVideoFormatFromMFMediaType = (
            mfplat.MFCreateMFVideoFormatFromMFMediaType
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        class _MFWaveFormatExConvertFlags(ENUM):
            MFWaveFormatExConvertFlag_Normal = 0
            MFWaveFormatExConvertFlag_ForceExtensible = 1

        MFWaveFormatExConvertFlags = _MFWaveFormatExConvertFlags
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if defined(__cplusplus):
        # declarations with default parameters
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            # STDAPI
            # MFCreateWaveFormatExFromMFMediaType(
            # _In_        IMFMediaType*   pMFType,
            # _Out_       WAVEFORMATEX**  ppWF,
            # _Out_opt_   UINT32*         pcbSize,
            # _In_        UINT32          Flags = MFWaveFormatExConvertFlag_Normal
            # );
            MFCreateWaveFormatExFromMFMediaType = (
                mfplat.MFCreateWaveFormatExFromMFMediaType
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            # STDAPI
            # MFInitMediaTypeFromVideoInfoHeader(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  VIDEOINFOHEADER*  pVIH,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype = NULL
            # );
            MFInitMediaTypeFromVideoInfoHeader = (
                mfplat.MFInitMediaTypeFromVideoInfoHeader
            )

            # STDAPI
            # MFInitMediaTypeFromVideoInfoHeader2(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  VIDEOINFOHEADER2* pVIH2,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype = NULL
            # );
            MFInitMediaTypeFromVideoInfoHeader2 = (
                mfplat.MFInitMediaTypeFromVideoInfoHeader2
            )

            # STDAPI
            # MFInitMediaTypeFromMPEG1VideoInfo(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  MPEG1VIDEOINFO*   pMP1VI,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype = NULL
            # );
            MFInitMediaTypeFromMPEG1VideoInfo = (
                mfplat.MFInitMediaTypeFromMPEG1VideoInfo
            )

            # STDAPI
            # MFInitMediaTypeFromMPEG2VideoInfo(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  MPEG2VIDEOINFO*   pMP2VI,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype = NULL
            # );
            MFInitMediaTypeFromMPEG2VideoInfo = (
                mfplat.MFInitMediaTypeFromMPEG2VideoInfo
            )

            # STDAPI
            # MFCalculateBitmapImageSize(
            # _In_reads_bytes_(cbBufSize)  BITMAPINFOHEADER* pBMIH,
            # _In_                    UINT32                  cbBufSize,
            # _Out_                   UINT32*                 pcbImageSize,
            # _Out_opt_               BOOL*                   pbKnown = NULL
            # );
            MFCalculateBitmapImageSize = mfplat.MFCalculateBitmapImageSize
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    else:
        # same declarations without default parameters
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            # STDAPI
            # MFCreateWaveFormatExFromMFMediaType(
            # _In_        IMFMediaType*   pMFType,
            # _Out_       WAVEFORMATEX**  ppWF,
            # _Out_opt_   UINT32*         pcbSize,
            # _In_        UINT32          Flags
            # );
            MFCreateWaveFormatExFromMFMediaType = (
                mfplat.MFCreateWaveFormatExFromMFMediaType
            )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            # STDAPI
            # MFInitMediaTypeFromVideoInfoHeader(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  VIDEOINFOHEADER*  pVIH,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype
            # );
            MFInitMediaTypeFromVideoInfoHeader = (
                mfplat.MFInitMediaTypeFromVideoInfoHeader
            )

            # STDAPI
            # MFInitMediaTypeFromVideoInfoHeader2(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  VIDEOINFOHEADER2* pVIH2,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype
            # );
            MFInitMediaTypeFromVideoInfoHeader2 = (
                mfplat.MFInitMediaTypeFromVideoInfoHeader2
            )

            # STDAPI
            # MFInitMediaTypeFromMPEG1VideoInfo(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  MPEG1VIDEOINFO*   pMP1VI,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype
            # );
            MFInitMediaTypeFromMPEG1VideoInfo = (
                mfplat.MFInitMediaTypeFromMPEG1VideoInfo
            )

            # STDAPI
            # MFInitMediaTypeFromMPEG2VideoInfo(
            # _In_                    IMFMediaType*           pMFType,
            # _In_reads_bytes_(cbBufSize)  MPEG2VIDEOINFO*   pMP2VI,
            # _In_                    UINT32                  cbBufSize,
            # _In_opt_                GUID*             pSubtype
            # );
            MFInitMediaTypeFromMPEG2VideoInfo = (
                mfplat.MFInitMediaTypeFromMPEG2VideoInfo
            )

            # STDAPI
            # MFCalculateBitmapImageSize(
            # _In_reads_bytes_(cbBufSize)  BITMAPINFOHEADER* pBMIH,
            # _In_                    UINT32                  cbBufSize,
            # _Out_                   UINT32*                 pcbImageSize,
            # _Out_opt_               BOOL*                   pbKnown
            # );
            MFCalculateBitmapImageSize = mfplat.MFCalculateBitmapImageSize
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF  cplusplus

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # STDAPI
        # MFCalculateImageSize(
        # _In_                    REFGUID                 guidSubtype,
        # _In_                    UINT32                  unWidth,
        # _In_                    UINT32                  unHeight,
        # _Out_                   UINT32*                 pcbImageSize
        # );
        MFCalculateImageSize = mfplat.MFCalculateImageSize

        # STDAPI
        # MFFrameRateToAverageTimePerFrame(
        # _In_                    UINT32                  unNumerator,
        # _In_                    UINT32                  unDenominator,
        # _Out_                   UINT64*                 punAverageTimePerFrame
        # );
        MFFrameRateToAverageTimePerFrame = (
            mfplat.MFFrameRateToAverageTimePerFrame
        )

        # STDAPI
        # MFAverageTimePerFrameToFrameRate(
        # _In_                    UINT64                  unAverageTimePerFrame,
        # _Out_                   UINT32*                 punNumerator,
        # _Out_                   UINT32*                 punDenominator
        # );
        MFAverageTimePerFrameToFrameRate = (
            mfplat.MFAverageTimePerFrameToFrameRate
        )

        # STDAPI
        # MFInitMediaTypeFromMFVideoFormat(
        # _In_                    IMFMediaType*           pMFType,
        # _In_reads_bytes_(cbBufSize)  MFVIDEOFORMAT*    pMFVF,
        # _In_                    UINT32                  cbBufSize
        # );
        MFInitMediaTypeFromMFVideoFormat = (
            mfplat.MFInitMediaTypeFromMFVideoFormat
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI
        # MFInitMediaTypeFromWaveFormatEx(
        # _In_                    IMFMediaType*           pMFType,
        # _In_reads_bytes_(cbBufSize)  WAVEFORMATEX*     pWaveFormat,
        # _In_                    UINT32                  cbBufSize
        # );
        MFInitMediaTypeFromWaveFormatEx = (
            mfplat.MFInitMediaTypeFromWaveFormatEx
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # STDAPI
        # MFInitMediaTypeFromAMMediaType(
        # _In_    IMFMediaType*           pMFType,
        # _In_    AM_MEDIA_TYPE*    pAMType
        # );
        MFInitMediaTypeFromAMMediaType = mfplat.MFInitMediaTypeFromAMMediaType

        # STDAPI
        # MFInitAMMediaTypeFromMFMediaType(
        # _In_    IMFMediaType*           pMFType,
        # _In_    GUID                    guidFormatBlockType,
        # _Inout_ AM_MEDIA_TYPE*          pAMType
        # );
        MFInitAMMediaTypeFromMFMediaType = (
            mfplat.MFInitAMMediaTypeFromMFMediaType
        )

        # STDAPI
        # MFCreateAMMediaTypeFromMFMediaType(
        # _In_    IMFMediaType*           pMFType,
        # _In_    GUID                    guidFormatBlockType,
        # _Inout_ AM_MEDIA_TYPE**         ppAMType // delete with DeleteMediaType
        # );
        MFCreateAMMediaTypeFromMFMediaType = (
            mfplat.MFCreateAMMediaTypeFromMFMediaType
        )

        # This function compares a full media type to a partial media type.
        # A "partial" media type is one that is given out by a component as a
        # possible
        # media type it could accept. Many attributes may be unset, which
        # represents
        # a "don't care" status for that attribute.
        # For example, a video effect may report that it supports YV12,
        # but not want to specify a particular size. It simply creates a media
        # type and sets
        # the major type to MFMediaType_Video and the subtype to
        # MEDIASUBTYPE_YV12.
        # The comparison function succeeds if the partial type contains at
        # least a major type,
        # and all of the attributes in the partial type exist in the full type
        # and are set to
        # the same value.
        # STDAPI_(BOOL)
        # MFCompareFullToPartialMediaType(
        # _In_    IMFMediaType*   pMFTypeFull,
        # _In_    IMFMediaType*   pMFTypePartial
        # );
        MFCompareFullToPartialMediaType = (
            mfplat.MFCompareFullToPartialMediaType
        )
        MFCompareFullToPartialMediaType.restype = BOOL
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI
        # MFWrapMediaType(
        # _In_    IMFMediaType*    pOrig,
        # _In_    REFGUID          MajorType,
        # _In_    REFGUID          SubType,
        # _Out_   IMFMediaType **  ppWrap
        # );
        MFWrapMediaType = mfplat.MFWrapMediaType

        # STDAPI
        # MFUnwrapMediaType(
        # _In_    IMFMediaType*    pWrap,
        # _Out_   IMFMediaType **  ppOrig
        # );
        MFUnwrapMediaType = mfplat.MFUnwrapMediaType
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # MFCreateVideoMediaType
        if defined(_KSMEDIA_):
            evr = ctypes.windll.EVR

            # STDAPI MFCreateVideoMediaTypeFromVideoInfoHeader(
            # _In_ KS_VIDEOINFOHEADER* pVideoInfoHeader,
            # DWORD cbVideoInfoHeader,
            # DWORD dwPixelAspectRatioX,
            # DWORD dwPixelAspectRatioY,
            # MFVideoInterlaceMode InterlaceMode,
            # QWORD VideoFlags,
            # _In_opt_ GUID * pSubtype,
            # _Out_ IMFVideoMediaType** ppIVideoMediaType
            # );
            MFCreateVideoMediaTypeFromVideoInfoHeader = (
                evr.MFCreateVideoMediaTypeFromVideoInfoHeader
            )

            # STDAPI MFCreateVideoMediaTypeFromVideoInfoHeader2(
            # _In_ KS_VIDEOINFOHEADER2* pVideoInfoHeader,
            # DWORD cbVideoInfoHeader,
            # QWORD AdditionalVideoFlags,
            # _In_opt_ GUID * pSubtype,
            # _Out_ IMFVideoMediaType** ppIVideoMediaType
            # );
            MFCreateVideoMediaTypeFromVideoInfoHeader2 = (
                evr.MFCreateVideoMediaTypeFromVideoInfoHeader2
            )
        # END IF

        evr = ctypes.windll.EVR

        # STDAPI MFCreateVideoMediaType(
        # _In_ MFVIDEOFORMAT* pVideoFormat,
        # _Out_ IMFVideoMediaType** ppIVideoMediaType
        # );
        MFCreateVideoMediaType = evr.MFCreateVideoMediaType

        # STDAPI MFCreateVideoMediaTypeFromSubtype(
        # _In_ GUID * pAMSubtype,
        # _Out_ IMFVideoMediaType  **ppIVideoMediaType
        # );
        MFCreateVideoMediaTypeFromSubtype = (
            evr.MFCreateVideoMediaTypeFromSubtype
        )

        # STDAPI_(BOOL)
        # MFIsFormatYUV(
        # DWORD Format
        # );
        MFIsFormatYUV = evr.MFIsFormatYUV
        MFIsFormatYUV.restype = BOOL

        # These depend on BITMAPINFOHEADER being defined
        # STDAPI MFCreateVideoMediaTypeFromBitMapInfoHeader(
        # _In_ BITMAPINFOHEADER* pbmihBitMapInfoHeader,
        # DWORD dwPixelAspectRatioX,
        # DWORD dwPixelAspectRatioY,
        # MFVideoInterlaceMode InterlaceMode,
        # QWORD VideoFlags,
        # QWORD qwFramesPerSecondNumerator,
        # QWORD qwFramesPerSecondDenominator,
        # DWORD dwMaxBitRate,
        # _Out_ IMFVideoMediaType** ppIVideoMediaType
        # );
        MFCreateVideoMediaTypeFromBitMapInfoHeader = (
            evr.MFCreateVideoMediaTypeFromBitMapInfoHeader
        )

        # STDAPI MFGetStrideForBitmapInfoHeader(
        # DWORD format,
        # DWORD dwWidth,
        # _Out_ LONG* pStride
        # );
        MFGetStrideForBitmapInfoHeader = evr.MFGetStrideForBitmapInfoHeader

        # STDAPI MFGetPlaneSize(
        # DWORD format,
        # DWORD dwWidth,
        # DWORD dwHeight,
        # _Out_ DWORD* pdwPlaneSize
        # );
        MFGetPlaneSize = evr.MFGetPlaneSize

        if WINVER >= _WIN32_WINNT_WIN7:
            # MFCreateVideoMediaTypeFromBitMapInfoHeaderEx

            # STDAPI MFCreateVideoMediaTypeFromBitMapInfoHeaderEx(
            # _In_reads_bytes_(cbBitMapInfoHeader) BITMAPINFOHEADER* pbmihBitMapInfoHeader,
            # _In_    UINT32                  cbBitMapInfoHeader,
            # DWORD dwPixelAspectRatioX,
            # DWORD dwPixelAspectRatioY,
            # MFVideoInterlaceMode InterlaceMode,
            # QWORD VideoFlags,
            # DWORD dwFramesPerSecondNumerator,
            # DWORD dwFramesPerSecondDenominator,
            # DWORD dwMaxBitRate,
            # _Out_ IMFVideoMediaType** ppIVideoMediaType
            # );
            MFCreateVideoMediaTypeFromBitMapInfoHeaderEx = (
                mfplat.MFCreateVideoMediaTypeFromBitMapInfoHeaderEx
            )
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        # MFCreateMediaTypeFromRepresentation

        # STDAPI MFCreateMediaTypeFromRepresentation(
        # GUID guidRepresentation,
        # _In_ LPVOID pvRepresentation,
        # _Out_ IMFMediaType** ppIMediaType
        # );
        MFCreateMediaTypeFromRepresentation = (
            mfplat.MFCreateMediaTypeFromRepresentation
        )

        # MFCreateAudioMediaType
        # STDAPI
        # MFCreateAudioMediaType(
        # _In_    WAVEFORMATEX* pAudioFormat,
        # _Out_   IMFAudioMediaType** ppIAudioMediaType
        # );
        MFCreateAudioMediaType = mfplat.MFCreateAudioMediaType

        # DWORD
        # STDMETHODCALLTYPE
        # MFGetUncompressedVideoFormat(
        # _In_    MFVIDEOFORMAT* pVideoFormat
        # );
        MFGetUncompressedVideoFormat = evr.MFGetUncompressedVideoFormat
        MFGetUncompressedVideoFormat.restype = DWORD

        # STDAPI
        # MFInitVideoFormat(
        # _In_    MFVIDEOFORMAT*          pVideoFormat,
        # _In_    MFStandardVideoFormat   type
        # );
        MFInitVideoFormat = evr.MFInitVideoFormat

        # STDAPI
        # MFInitVideoFormat_RGB(
        # _In_    MFVIDEOFORMAT*  pVideoFormat,
        # _In_    DWORD           dwWidth,
        # _In_    DWORD           dwHeight,
        # _In_    DWORD           D3Dfmt // 0 indicates sRGB
        # );
        MFInitVideoFormat_RGB = evr.MFInitVideoFormat_RGB

        # STDAPI
        # MFConvertColorInfoToDXVA(
        # _Out_ DWORD* pdwToDXVA,
        # _In_  MFVIDEOFORMAT* pFromFormat
        # );
        MFConvertColorInfoToDXVA = evr.MFConvertColorInfoToDXVA

        # STDAPI
        # MFConvertColorInfoFromDXVA(
        # _Inout_ MFVIDEOFORMAT* pToFormat,
        # _In_    DWORD dwFromDXVA
        # );
        MFConvertColorInfoFromDXVA = evr.MFConvertColorInfoFromDXVA
        # Optimized stride copy function
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        evr = ctypes.windll.EVR
        # STDAPI MFCopyImage(
        # _Out_writes_bytes_(_Inexpressible_(abs(lDestStride) *  dwLines)) BYTE* pDest,
        # LONG    lDestStride,
        # _In_reads_bytes_(_Inexpressible_(abs(lSrcStride) * dwLines)) BYTE* pSrc,
        # LONG    lSrcStride,
        # _Out_range_( <= , _Inexpressible_(min(abs(lSrcStride), abs(lDestStride))))  DWORD dwWidthInBytes,
        # DWORD   dwLines
        # );
        MFCopyImage = evr.MFCopyImage
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        evr = ctypes.windll.EVR

        # STDAPI MFConvertFromFP16Array(
        # _Out_writes_(dwCount) float* pDest,
        # _In_reads_(dwCount) WORD* pSrc,
        # DWORD dwCount
        # );
        MFConvertFromFP16Array = evr.MFConvertFromFP16Array

        # STDAPI MFConvertToFP16Array(
        # _Out_writes_(dwCount) WORD* pDest,
        # _In_reads_(dwCount) float* pSrc,
        # DWORD dwCount
        # );
        MFConvertToFP16Array = evr.MFConvertToFP16Array
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # STDAPI MFCreate2DMediaBuffer(
        # _In_ DWORD dwWidth,
        # _In_ DWORD dwHeight,
        # _In_ DWORD dwFourCC,
        # _In_ BOOL fBottomUp,
        # _Out_ IMFMediaBuffer**    ppBuffer
        # );
        MFCreate2DMediaBuffer = mfplat.MFCreate2DMediaBuffer

        # Creates an optimal system memory media buffer from a media type
        # STDAPI MFCreateMediaBufferFromMediaType(
        # _In_ IMFMediaType* pMediaType,
        # _In_ LONGLONG llDuration, // Sample Duration, needed for audio
        # _In_ DWORD dwMinLength, // 0 means optimized default
        # _In_ DWORD dwMinAlignment, // 0 means optimized default
        # _Outptr_ IMFMediaBuffer** ppBuffer
        # );
        MFCreateMediaBufferFromMediaType = (
            mfplat.MFCreateMediaBufferFromMediaType
        )    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    # /////////////////////////////////////////////////////////////////////////
    # ///////////////////// Attributes Utility functions //////////////////////
    # /////////////////////////////////////////////////////////////////////////

    if defined(__cplusplus):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
            # IMFAttributes inline UTILITY FUNCTIONS - used for IMFMediaType
            # as well
            # "failsafe" inline get methods - return the stored value or
            # return a default
            # helpers for getting/setting ratios and sizes
            if defined(_INTSAFE_H_INCLUDED_):
                MFGetAttributeString = mfplat.MFGetAttributeString
                MFGetAttributeString.restype = HRESULT

            # END IF _INTSAFE_H_INCLUDED_
            #
            # ////////////////////////////  Collection ////////////////////
            # /////////////////////////////////////////////////////////////
            #
            #
            # // Instantiates the MF-provided IMFCollection implementation
            #
            # STDAPI MFCreateCollection(
            # _Out_ IMFCollection **ppIMFCollection );
            MFCreateCollection = mfplat.MFCreateCollection
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # END IF

    # /////////////////////////////////////////////////////////////////////
    # ////////////////////////////// Memory Management ////////////////////
    # /////////////////////////////////////////////////////////////////////

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Heap alloc/free
        class _EAllocationType(ENUM):
            eAllocationTypeDynamic = 1
            eAllocationTypeRT = 2
            eAllocationTypePageable = 3
            eAllocationTypeIgnore = 4

        EAllocationType = _EAllocationType

        # EXTERN_C void* WINAPI MFHeapAlloc( size_t nSize,
        # ULONG dwFlags,
        # _In_opt_ CHAR *pszFile,
        # INT line,
        # EAllocationType eat);
        MFHeapAlloc = mfplat.MFHeapAlloc
        MFHeapAlloc.restype = POINTER(VOID)

        # EXTERN_C VOID WINAPI MFHeapFree( VOID * pv );
        MFHeapFree = mfplat.MFHeapFree
        MFHeapFree.restype = VOID

        # ////////////////////////  SourceResolver ////////////////////////
        # /////////////////////////////////////////////////////////////////

        CLSID_MFSourceResolver = DEFINE_GUID(
            0x90EAB60F,
            0xE43A,
            0x4188,
            0xBC,
            0xC4,
            0xE4,
            0x7F,
            0xDF,
            0x04,
            0x86,
            0x8C
        )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINVER >= _WIN32_WINNT_WIN7:
        # Return (a * b + d) / c
        # Returns _I64_MAX or LLONG_MIN on failure or _I64_MAX if
        # mplat.dll is not available
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):

            # LONGLONG WINAPI MFllMulDiv(LONGLONG a, LONGLONG b, LONGLONG c, LONGLONG d);
            MFllMulDiv = mfplat.MFllMulDiv
            MFllMulDiv.restype = LONGLONG

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)

        # //////////////////////// Content Protection /////////////////////////
        # /////////////////////////////////////////////////////////////////////
        #
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        # STDAPI MFGetContentProtectionSystemCLSID(
        # _In_ REFGUID guidProtectionSystemID,
        # _Out_ CLSID *pclsid );
        MFGetContentProtectionSystemCLSID = (
            mfplat.MFGetContentProtectionSystemCLSID
        )
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF

# END IF  #if not defined(__MFAPI_H__)


