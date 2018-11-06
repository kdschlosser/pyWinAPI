__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
# from .windows_h import * # NOQA
# from .ole2_h import * # NOQA

from .wtypes_h import (
    ENUM,
    REFERENCE_TIME,
    HRESULT,
    DWORD,
    POINTER,
    LONG,
    LPRECT,
    HWND,
    HDC,
    BYTE,
    COLORREF,
    LPCOLESTR,
    LPOLESTR,
    ULONG,
    LPCWSTR,
    BOOL,
    PVOID,
    LPDWORD,
    LPGUID,
    DOUBLE,
    GUID,
    REFCLSID,
    REFIID,
    VOID,
    WORD,
    DWORDLONG,
    INT,
    ULONGLONG,
    UINT,
    REFGUID,
    LPVOID,
    HKEY,
    HMONITOR,
    DWORD_PTR,
    HANDLE,
    LPWSTR,
    LONGLONG,
    POINT,
    LCID,
    LPSTR,
    PALETTEENTRY,
    RECT,
    CLSID,
    HEVENT,
    LONG_PTR,
    FLOAT,
    WCHAR,
    SIZE,
    CHAR,
    LARGE_INTEGER,
)
from . guiddef_h import (
    IID,
    EXTERN_GUID
)
import ctypes
import comtypes

from .unknwn_h import * # NOQA
from .objidl_h import * # NOQA
from .oaidl_h import * # NOQA
from .ocidl_h import * # NOQA
from .winapifamily_h import * # NOQA

IID_ICreateDevEnum = IID(
    '{29840822-5B84-11D0-BD3B-00A0C911CE86}'
)


class ICreateDevEnum(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICreateDevEnum
    _idlflags_ = []


IID_IPin = IID(
    '{56a86891-0ad4-11ce-b03a-0020af0ba770}'
)


class IPin(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPin
    _idlflags_ = []


IID_IEnumPins = IID(
    '{56a86892-0ad4-11ce-b03a-0020af0ba770}'
)


class IEnumPins(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumPins
    _idlflags_ = []


IID_IEnumMediaTypes = IID(
    '{89c31040-846b-11ce-97d3-00aa0055595a}'
)


class IEnumMediaTypes(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumMediaTypes
    _idlflags_ = []


IID_IFilterGraph = IID(
    '{56a8689f-0ad4-11ce-b03a-0020af0ba770}'
)


class IFilterGraph(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFilterGraph
    _idlflags_ = []


IID_IEnumFilters = IID(
    '{56a86893-0ad4-11ce-b03a-0020af0ba770}'
)


class IEnumFilters(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumFilters
    _idlflags_ = []


IID_IMediaFilter = IID(
    '{56a86899-0ad4-11ce-b03a-0020af0ba770}'
)


class IMediaFilter(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IMediaFilter
    _idlflags_ = []


IID_IBaseFilter = IID(
    '{56a86895-0ad4-11ce-b03a-0020af0ba770}'
)


class IBaseFilter(IMediaFilter):
    _case_insensitive_ = True
    _iid_ = IID_IBaseFilter
    _idlflags_ = []


IID_IReferenceClock = IID(
    '{56a86897-0ad4-11ce-b03a-0020af0ba770}'
)


class IReferenceClock(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IReferenceClock
    _idlflags_ = []


IID_IReferenceClockTimerControl = IID(
    '{ebec459c-2eca-4d42-a8af-30df557614b8}'
)


class IReferenceClockTimerControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IReferenceClockTimerControl
    _idlflags_ = []


IID_IReferenceClock2 = IID(
    '{36b73885-c2c8-11cf-8b46-00805f6cef60}'
)


class IReferenceClock2(IReferenceClock):
    _case_insensitive_ = True
    _iid_ = IID_IReferenceClock2
    _idlflags_ = []


IID_IMediaSample = IID(
    '{56a8689a-0ad4-11ce-b03a-0020af0ba770}'
)


class IMediaSample(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMediaSample
    _idlflags_ = []


IID_IMediaSample2 = IID(
    '{36b73884-c2c8-11cf-8b46-00805f6cef60}'
)


class IMediaSample2(IMediaSample):
    _case_insensitive_ = True
    _iid_ = IID_IMediaSample2
    _idlflags_ = []


IID_IMediaSample2Config = IID(
    '{68961E68-832B-41ea-BC91-63593F3E70E3}'
)


class IMediaSample2Config(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMediaSample2Config
    _idlflags_ = []


IID_IMemAllocator = IID(
    '{56a8689c-0ad4-11ce-b03a-0020af0ba770}'
)


class IMemAllocator(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMemAllocator
    _idlflags_ = []


IID_IMemAllocatorCallbackTemp = IID(
    '{379a0cf0-c1de-11d2-abf5-00a0c905f375}'
)


class IMemAllocatorCallbackTemp(IMemAllocator):
    _case_insensitive_ = True
    _iid_ = IID_IMemAllocatorCallbackTemp
    _idlflags_ = []


IID_IMemAllocatorNotifyCallbackTemp = IID(
    '{92980b30-c1de-11d2-abf5-00a0c905f375}'
)


class IMemAllocatorNotifyCallbackTemp(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMemAllocatorNotifyCallbackTemp
    _idlflags_ = []


IID_IMemInputPin = IID(
    '{56a8689d-0ad4-11ce-b03a-0020af0ba770}'
)


class IMemInputPin(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMemInputPin
    _idlflags_ = []


IID_IAMovieSetup = IID(
    '{a3d8cec0-7e5a-11cf-bbc5-00805f6cef20}'
)


class IAMovieSetup(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMovieSetup
    _idlflags_ = []


IID_IMediaSeeking = IID(
    '{36b73880-c2c8-11cf-8b46-00805f6cef60}'
)


class IMediaSeeking(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMediaSeeking
    _idlflags_ = []


IID_ICodecAPI = IID(
    '{901db4c7-31ce-41a2-85dc-8fa0bf41b8da}'
)


class ICodecAPI(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICodecAPI
    _idlflags_ = []


IID_IEnumRegFilters = IID(
    '{56a868a4-0ad4-11ce-b03a-0020af0ba770}'
)


class IEnumRegFilters(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumRegFilters
    _idlflags_ = []


IID_IFilterMapper = IID(
    '{56a868a3-0ad4-11ce-b03a-0020af0ba770}'
)


class IFilterMapper(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFilterMapper
    _idlflags_ = []


IID_IFilterMapper2 = IID(
    '{b79bb0b0-33c1-11d1-abe1-00a0c905f375}'
)


class IFilterMapper2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFilterMapper2
    _idlflags_ = []


IID_IFilterMapper3 = IID(
    '{b79bb0b1-33c1-11d1-abe1-00a0c905f375}'
)


class IFilterMapper3(IFilterMapper2):
    _case_insensitive_ = True
    _iid_ = IID_IFilterMapper3
    _idlflags_ = []


IID_IQualityControl = IID(
    '{56a868a5-0ad4-11ce-b03a-0020af0ba770}'
)


class IQualityControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IQualityControl
    _idlflags_ = []


IID_IOverlayNotify = IID(
    '{56a868a0-0ad4-11ce-b03a-0020af0ba770}'
)


class IOverlayNotify(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOverlayNotify
    _idlflags_ = []


IID_IOverlayNotify2 = IID(
    '{680EFA10-D535-11D1-87C8-00A0C9223196}'
)


class IOverlayNotify2(IOverlayNotify):
    _case_insensitive_ = True
    _iid_ = IID_IOverlayNotify2
    _idlflags_ = []


IID_IOverlay = IID(
    '{56a868a1-0ad4-11ce-b03a-0020af0ba770}'
)


class IOverlay(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOverlay
    _idlflags_ = []


IID_IMediaEventSink = IID(
    '{56a868a2-0ad4-11ce-b03a-0020af0ba770}'
)


class IMediaEventSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMediaEventSink
    _idlflags_ = []


IID_IFileSourceFilter = IID(
    '{56a868a6-0ad4-11ce-b03a-0020af0ba770}'
)


class IFileSourceFilter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFileSourceFilter
    _idlflags_ = []


IID_IFileSinkFilter = IID(
    '{a2104830-7c70-11cf-8bce-00aa00a3f1a6}'
)


class IFileSinkFilter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFileSinkFilter
    _idlflags_ = []


IID_IFileSinkFilter2 = IID(
    '{00855B90-CE1B-11d0-BD4F-00A0C911CE86}'
)


class IFileSinkFilter2(IFileSinkFilter):
    _case_insensitive_ = True
    _iid_ = IID_IFileSinkFilter2
    _idlflags_ = []


IID_IGraphBuilder = IID(
    '{56a868a9-0ad4-11ce-b03a-0020af0ba770}'
)


class IGraphBuilder(IFilterGraph):
    _case_insensitive_ = True
    _iid_ = IID_IGraphBuilder
    _idlflags_ = []


IID_ICaptureGraphBuilder = IID(
    '{bf87b6e0-8c27-11d0-b3f0-00aa003761c5}'
)


class ICaptureGraphBuilder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICaptureGraphBuilder
    _idlflags_ = []


IID_IAMCopyCaptureFileProgress = IID(
    '{670d1d20-a068-11d0-b3f0-00aa003761c5}'
)


class IAMCopyCaptureFileProgress(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMCopyCaptureFileProgress
    _idlflags_ = []


IID_ICaptureGraphBuilder2 = IID(
    '{93E5A4E0-2D50-11d2-ABFA-00A0C9C6E38D}'
)


class ICaptureGraphBuilder2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICaptureGraphBuilder2
    _idlflags_ = []


IID_IFilterGraph2 = IID(
    '{36b73882-c2c8-11cf-8b46-00805f6cef60}'
)


class IFilterGraph2(IGraphBuilder):
    _case_insensitive_ = True
    _iid_ = IID_IFilterGraph2
    _idlflags_ = []


IID_IFilterGraph3 = IID(
    '{aaf38154-b80b-422f-91e6-b66467509a07}'
)


class IFilterGraph3(IFilterGraph2):
    _case_insensitive_ = True
    _iid_ = IID_IFilterGraph3
    _idlflags_ = []


IID_IStreamBuilder = IID(
    '{56a868bf-0ad4-11ce-b03a-0020af0ba770}'
)


class IStreamBuilder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IStreamBuilder
    _idlflags_ = []


IID_IAsyncReader = IID(
    '{56a868aa-0ad4-11ce-b03a-0020af0ba770}'
)


class IAsyncReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAsyncReader
    _idlflags_ = []


IID_IGraphVersion = IID(
    '{56a868ab-0ad4-11ce-b03a-0020af0ba770}'
)


class IGraphVersion(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IGraphVersion
    _idlflags_ = []


IID_IResourceConsumer = IID(
    '{56a868ad-0ad4-11ce-b03a-0020af0ba770}'
)


class IResourceConsumer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IResourceConsumer
    _idlflags_ = []


IID_IResourceManager = IID(
    '{56a868ac-0ad4-11ce-b03a-0020af0ba770}'
)


class IResourceManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IResourceManager
    _idlflags_ = []


IID_IDistributorNotify = IID(
    '{56a868af-0ad4-11ce-b03a-0020af0ba770}'
)


class IDistributorNotify(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDistributorNotify
    _idlflags_ = []


IID_IAMStreamControl = IID(
    '{36b73881-c2c8-11cf-8b46-00805f6cef60}'
)


class IAMStreamControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMStreamControl
    _idlflags_ = []


IID_ISeekingPassThru = IID(
    '{36b73883-c2c8-11cf-8b46-00805f6cef60}'
)


class ISeekingPassThru(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISeekingPassThru
    _idlflags_ = []


IID_IAMStreamConfig = IID(
    '{C6E13340-30AC-11d0-A18C-00A0C9118956}'
)


class IAMStreamConfig(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMStreamConfig
    _idlflags_ = []


IID_IConfigInterleaving = IID(
    '{BEE3D220-157B-11d0-BD23-00A0C911CE86}'
)


class IConfigInterleaving(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IConfigInterleaving
    _idlflags_ = []


IID_IConfigAviMux = IID(
    '{5ACD6AA0-F482-11ce-8B67-00AA00A3F1A6}'
)


class IConfigAviMux(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IConfigAviMux
    _idlflags_ = []


IID_IAMVideoCompression = IID(
    '{C6E13343-30AC-11d0-A18C-00A0C9118956}'
)


class IAMVideoCompression(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMVideoCompression
    _idlflags_ = []


IID_IAMVfwCaptureDialogs = IID(
    '{D8D715A0-6E5E-11D0-B3F0-00AA003761C5}'
)


class IAMVfwCaptureDialogs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMVfwCaptureDialogs
    _idlflags_ = []


IID_IAMVfwCompressDialogs = IID(
    '{D8D715A3-6E5E-11D0-B3F0-00AA003761C5}'
)


class IAMVfwCompressDialogs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMVfwCompressDialogs
    _idlflags_ = []


IID_IAMDroppedFrames = IID(
    '{C6E13344-30AC-11d0-A18C-00A0C9118956}'
)


class IAMDroppedFrames(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMDroppedFrames
    _idlflags_ = []


IID_IAMAudioInputMixer = IID(
    '{54C39221-8380-11d0-B3F0-00AA003761C5}'
)


class IAMAudioInputMixer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMAudioInputMixer
    _idlflags_ = []


IID_IAMBufferNegotiation = IID(
    '{56ED71A0-AF5F-11D0-B3F0-00AA003761C5}'
)


class IAMBufferNegotiation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMBufferNegotiation
    _idlflags_ = []


IID_IAMAnalogVideoDecoder = IID(
    '{C6E13350-30AC-11d0-A18C-00A0C9118956}'
)


class IAMAnalogVideoDecoder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMAnalogVideoDecoder
    _idlflags_ = []


IID_IAMVideoProcAmp = IID(
    '{C6E13360-30AC-11d0-A18C-00A0C9118956}'
)


class IAMVideoProcAmp(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMVideoProcAmp
    _idlflags_ = []


IID_IAMCameraControl = IID(
    '{C6E13370-30AC-11d0-A18C-00A0C9118956}'
)


class IAMCameraControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMCameraControl
    _idlflags_ = []


IID_IAMVideoControl = IID(
    '{6a2e0670-28e4-11d0-a18c-00a0c9118956}'
)


class IAMVideoControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMVideoControl
    _idlflags_ = []


IID_IAMCrossbar = IID(
    '{C6E13380-30AC-11d0-A18C-00A0C9118956}'
)


class IAMCrossbar(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMCrossbar
    _idlflags_ = []


IID_IAMTuner = IID(
    '{211A8761-03AC-11d1-8D13-00AA00BD8339}'
)


class IAMTuner(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMTuner
    _idlflags_ = []


IID_IAMTunerNotification = IID(
    '{211A8760-03AC-11d1-8D13-00AA00BD8339}'
)


class IAMTunerNotification(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMTunerNotification
    _idlflags_ = []


IID_IAMTVTuner = IID(
    '{211A8766-03AC-11d1-8D13-00AA00BD8339}'
)


class IAMTVTuner(IAMTuner):
    _case_insensitive_ = True
    _iid_ = IID_IAMTVTuner
    _idlflags_ = []


IID_IBPCSatelliteTuner = IID(
    '{211A8765-03AC-11d1-8D13-00AA00BD8339}'
)


class IBPCSatelliteTuner(IAMTuner):
    _case_insensitive_ = True
    _iid_ = IID_IBPCSatelliteTuner
    _idlflags_ = []


IID_IAMTVAudio = IID(
    '{83EC1C30-23D1-11d1-99E6-00A0C9560266}'
)


class IAMTVAudio(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMTVAudio
    _idlflags_ = []


IID_IAMTVAudioNotification = IID(
    '{83EC1C33-23D1-11d1-99E6-00A0C9560266}'
)


class IAMTVAudioNotification(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMTVAudioNotification
    _idlflags_ = []


IID_IAMAnalogVideoEncoder = IID(
    '{C6E133B0-30AC-11d0-A18C-00A0C9118956}'
)


class IAMAnalogVideoEncoder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMAnalogVideoEncoder
    _idlflags_ = []


IID_IKsPropertySet = IID(
    '{31EFAC30-515C-11d0-A9AA-00AA0061BE93}'
)


class IKsPropertySet(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IKsPropertySet
    _idlflags_ = []


IID_IMediaPropertyBag = IID(
    '{6025A880-C0D5-11d0-BD4E-00A0C911CE86}'
)


class IMediaPropertyBag(IPropertyBag):
    _case_insensitive_ = True
    _iid_ = IID_IMediaPropertyBag
    _idlflags_ = []


IID_IPersistMediaPropertyBag = IID(
    '{5738E040-B67F-11d0-BD4D-00A0C911CE86}'
)


class IPersistMediaPropertyBag(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistMediaPropertyBag
    _idlflags_ = []


IID_IAMPhysicalPinInfo = IID(
    '{F938C991-3029-11cf-8C44-00AA006B6814}'
)


class IAMPhysicalPinInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMPhysicalPinInfo
    _idlflags_ = []


IID_IAMExtDevice = IID(
    '{B5730A90-1A2C-11cf-8C23-00AA006B6814}'
)


class IAMExtDevice(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMExtDevice
    _idlflags_ = []


IID_IAMExtTransport = IID(
    '{A03CD5F0-3045-11cf-8C44-00AA006B6814}'
)


class IAMExtTransport(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMExtTransport
    _idlflags_ = []


IID_IAMTimecodeReader = IID(
    '{9B496CE1-811B-11cf-8C77-00AA006B6814}'
)


class IAMTimecodeReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMTimecodeReader
    _idlflags_ = []


IID_IAMTimecodeGenerator = IID(
    '{9B496CE0-811B-11cf-8C77-00AA006B6814}'
)


class IAMTimecodeGenerator(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMTimecodeGenerator
    _idlflags_ = []


IID_IAMTimecodeDisplay = IID(
    '{9B496CE2-811B-11cf-8C77-00AA006B6814}'
)


class IAMTimecodeDisplay(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMTimecodeDisplay
    _idlflags_ = []


IID_IAMDevMemoryAllocator = IID(
    '{c6545bf0-e76b-11d0-bd52-00a0c911ce86}'
)


class IAMDevMemoryAllocator(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMDevMemoryAllocator
    _idlflags_ = []


IID_IAMDevMemoryControl = IID(
    '{c6545bf1-e76b-11d0-bd52-00a0c911ce86}'
)


class IAMDevMemoryControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMDevMemoryControl
    _idlflags_ = []


IID_IAMStreamSelect = IID(
    '{c1960960-17f5-11d1-abe1-00a0c905f375}'
)


class IAMStreamSelect(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMStreamSelect
    _idlflags_ = []


IID_IAMResourceControl = IID(
    '{8389d2d0-77d7-11d1-abe6-00a0c905f375}'
)


class IAMResourceControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMResourceControl
    _idlflags_ = []


IID_IAMClockAdjust = IID(
    '{4d5466b0-a49c-11d1-abe8-00a0c905f375}'
)


class IAMClockAdjust(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMClockAdjust
    _idlflags_ = []


IID_IAMFilterMiscFlags = IID(
    '{2dd74950-a890-11d1-abe8-00a0c905f375}'
)


class IAMFilterMiscFlags(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMFilterMiscFlags
    _idlflags_ = []


IID_IDrawVideoImage = IID(
    '{48efb120-ab49-11d2-aed2-00a0c995e8d5}'
)


class IDrawVideoImage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDrawVideoImage
    _idlflags_ = []


IID_IDecimateVideoImage = IID(
    '{2e5ea3e0-e924-11d2-b6da-00a0c995e8df}'
)


class IDecimateVideoImage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDecimateVideoImage
    _idlflags_ = []


IID_IAMVideoDecimationProperties = IID(
    '{60d32930-13da-11d3-9ec6-c4fcaef5c7be}'
)


class IAMVideoDecimationProperties(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMVideoDecimationProperties
    _idlflags_ = []


IID_IVideoFrameStep = IID(
    '{e46a9787-2b71-444d-a4b5-1fab7b708d6a}'
)


class IVideoFrameStep(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVideoFrameStep
    _idlflags_ = []


IID_IAMLatency = IID(
    '{62EA93BA-EC62-11d2-B770-00C04FB6BD3D}'
)


class IAMLatency(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMLatency
    _idlflags_ = []


IID_IAMPushSource = IID(
    '{F185FE76-E64E-11d2-B76E-00C04FB6BD3D}'
)


class IAMPushSource(IAMLatency):
    _case_insensitive_ = True
    _iid_ = IID_IAMPushSource
    _idlflags_ = []


IID_IAMDeviceRemoval = IID(
    '{f90a6130-b658-11d2-ae49-0000f8754b99}'
)


class IAMDeviceRemoval(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMDeviceRemoval
    _idlflags_ = []


IID_IDVEnc = IID(
    '{d18e17a0-aacb-11d0-afb0-00aa00b67a42}'
)


class IDVEnc(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDVEnc
    _idlflags_ = []


IID_IIPDVDec = IID(
    '{b8e8bd60-0bfe-11d0-af91-00aa00b67a42}'
)


class IIPDVDec(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IIPDVDec
    _idlflags_ = []


IID_IDVRGB219 = IID(
    '{58473A19-2BC8-4663-8012-25F81BABDDD1}'
)


class IDVRGB219(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDVRGB219
    _idlflags_ = []


IID_IDVSplitter = IID(
    '{92a3a302-da7c-4a1f-ba7e-1802bb5d2d02}'
)


class IDVSplitter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDVSplitter
    _idlflags_ = []


IID_IAMAudioRendererStats = IID(
    '{22320CB2-D41A-11d2-BF7C-D7CB9DF0BF93}'
)


class IAMAudioRendererStats(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMAudioRendererStats
    _idlflags_ = []


IID_IAMGraphStreams = IID(
    '{632105FA-072E-11d3-8AF9-00C04FB6BD3D}'
)


class IAMGraphStreams(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMGraphStreams
    _idlflags_ = []


IID_IAMOverlayFX = IID(
    '{62fae250-7e65-4460-bfc9-6398b322073c}'
)


class IAMOverlayFX(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMOverlayFX
    _idlflags_ = []


IID_IAMOpenProgress = IID(
    '{8E1C39A1-DE53-11cf-AA63-0080C744528D}'
)


class IAMOpenProgress(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMOpenProgress
    _idlflags_ = []


IID_IMpeg2Demultiplexer = IID(
    '{436eee9c-264f-4242-90e1-4e330c107512}'
)


class IMpeg2Demultiplexer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMpeg2Demultiplexer
    _idlflags_ = []


IID_IEnumStreamIdMap = IID(
    '{945C1566-6202-46fc-96C7-D87F289C6534}'
)


class IEnumStreamIdMap(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumStreamIdMap
    _idlflags_ = []


IID_IMPEG2StreamIdMap = IID(
    '{D0E04C47-25B8-4369-925A-362A01D95444}'
)


class IMPEG2StreamIdMap(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMPEG2StreamIdMap
    _idlflags_ = []


IID_IRegisterServiceProvider = IID(
    '{7B3A2F01-0751-48DD-B556-004785171C54}'
)


class IRegisterServiceProvider(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRegisterServiceProvider
    _idlflags_ = []


IID_IAMClockSlave = IID(
    '{9FD52741-176D-4b36-8F51-CA8F933223BE}'
)


class IAMClockSlave(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMClockSlave
    _idlflags_ = []


IID_IGetCapabilitiesKey = IID(
    '{a8809222-07bb-48ea-951c-33158100625b}'
)


class IGetCapabilitiesKey(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IGetCapabilitiesKey
    _idlflags_ = []


IID_IEncoderAPI = IID(
    '{70423839-6ACC-4b23-B079-21DBF08156A5}'
)


class IEncoderAPI(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEncoderAPI
    _idlflags_ = []


IID_IVideoEncoder = IID(
    '{02997C3B-8E1B-460e-9270-545E0DE9563E}'
)


class IVideoEncoder(IEncoderAPI):
    _case_insensitive_ = True
    _iid_ = IID_IVideoEncoder
    _idlflags_ = []


IID_IAMDecoderCaps = IID(
    '{c0dff467-d499-4986-972b-e1d9090fa941}'
)


class IAMDecoderCaps(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMDecoderCaps
    _idlflags_ = []


IID_IAMCertifiedOutputProtection = IID(
    '{6feded3e-0ff1-4901-a2f1-43f7012c8515}'
)


class IAMCertifiedOutputProtection(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMCertifiedOutputProtection
    _idlflags_ = []


IID_IAMAsyncReaderTimestampScaling = IID(
    '{cf7b26fc-9a00-485b-8147-3e789d5e8f67}'
)


class IAMAsyncReaderTimestampScaling(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMAsyncReaderTimestampScaling
    _idlflags_ = []


IID_IAMPluginControl = IID(
    '{0e26a181-f40c-4635-8786-976284b52981}'
)


class IAMPluginControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMPluginControl
    _idlflags_ = []


IID_IPinConnection = IID(
    '{4a9a62d3-27d4-403d-91e9-89f540e55534}'
)


class IPinConnection(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPinConnection
    _idlflags_ = []


IID_IPinFlowControl = IID(
    '{c56e9858-dbf3-4f6b-8119-384af2060deb}'
)


class IPinFlowControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPinFlowControl
    _idlflags_ = []


IID_IGraphConfig = IID(
    '{03A1EB8E-32BF-4245-8502-114D08A9CB88}'
)


class IGraphConfig(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IGraphConfig
    _idlflags_ = []


IID_IGraphConfigCallback = IID(
    '{ade0fd60-d19d-11d2-abf6-00a0c905f375}'
)


class IGraphConfigCallback(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IGraphConfigCallback
    _idlflags_ = []


IID_IFilterChain = IID(
    '{DCFBDCF6-0DC2-45f5-9AB2-7C330EA09C29}'
)


class IFilterChain(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFilterChain
    _idlflags_ = []


IID_IVMRImagePresenter = IID(
    '{CE704FE7-E71E-41fb-BAA2-C4403E1182F5}'
)


class IVMRImagePresenter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRImagePresenter
    _idlflags_ = []


IID_IVMRSurfaceAllocator = IID(
    '{31ce832e-4484-458b-8cca-f4d7e3db0b52}'
)


class IVMRSurfaceAllocator(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRSurfaceAllocator
    _idlflags_ = []


IID_IVMRSurfaceAllocatorNotify = IID(
    '{aada05a8-5a4e-4729-af0b-cea27aed51e2}'
)


class IVMRSurfaceAllocatorNotify(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRSurfaceAllocatorNotify
    _idlflags_ = []


IID_IVMRWindowlessControl = IID(
    '{0eb1088c-4dcd-46f0-878f-39dae86a51b7}'
)


class IVMRWindowlessControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRWindowlessControl
    _idlflags_ = []


IID_IVMRMixerControl = IID(
    '{1c1a17b0-bed0-415d-974b-dc6696131599}'
)


class IVMRMixerControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRMixerControl
    _idlflags_ = []


IID_IVMRMonitorConfig = IID(
    '{9cf0b1b6-fbaa-4b7f-88cf-cf1f130a0dce}'
)


class IVMRMonitorConfig(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRMonitorConfig
    _idlflags_ = []


IID_IVMRFilterConfig = IID(
    '{9e5530c5-7034-48b4-bb46-0b8a6efc8e36}'
)


class IVMRFilterConfig(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRFilterConfig
    _idlflags_ = []


IID_IVMRAspectRatioControl = IID(
    '{ede80b5c-bad6-4623-b537-65586c9f8dfd}'
)


class IVMRAspectRatioControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRAspectRatioControl
    _idlflags_ = []


IID_IVMRDeINTerlaceControl = IID(
    '{bb057577-0db8-4e6a-87a7-1a8c9a505a0f}'
)


class IVMRDeINTerlaceControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRDeINTerlaceControl
    _idlflags_ = []


IID_IVMRMixerBitmap = IID(
    '{1E673275-0257-40aa-AF20-7C608D4A0428}'
)


class IVMRMixerBitmap(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRMixerBitmap
    _idlflags_ = []


IID_IVMRImageCompositor = IID(
    '{7a4fb5af-479f-4074-bb40-ce6722e43c82}'
)


class IVMRImageCompositor(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRImageCompositor
    _idlflags_ = []


IID_IVMRVideoStreamControl = IID(
    '{058d1f11-2a54-4bef-bd54-df706626b727}'
)


class IVMRVideoStreamControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRVideoStreamControl
    _idlflags_ = []


IID_IVMRSurface = IID(
    '{a9849bbe-9ec8-4263-b764-62730f0d15d0}'
)


class IVMRSurface(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRSurface
    _idlflags_ = []


IID_IVMRImagePresenterConfig = IID(
    '{9f3a1c85-8555-49ba-935f-be5b5b29d178}'
)


class IVMRImagePresenterConfig(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVMRImagePresenterConfig
    _idlflags_ = []


IID_IVMRImagePresenterExclModeConfig = IID(
    '{e6f7ce40-4673-44f1-8f77-5499d68cb4ea}'
)


class IVMRImagePresenterExclModeConfig(IVMRImagePresenterConfig):
    _case_insensitive_ = True
    _iid_ = IID_IVMRImagePresenterExclModeConfig
    _idlflags_ = []


IID_IVPManager = IID(
    '{aac18c18-e186-46d2-825d-a1f8dc8e395a}'
)


class IVPManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IVPManager
    _idlflags_ = []


IID_IDvdControl = IID(
    '{A70EFE61-E2A3-11d0-A9BE-00AA0061BE93}'
)


class IDvdControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDvdControl
    _idlflags_ = []


IID_IDvdInfo = IID(
    '{A70EFE60-E2A3-11d0-A9BE-00AA0061BE93}'
)


class IDvdInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDvdInfo
    _idlflags_ = []


IID_IDvdCmd = IID(
    '{5a4a97e4-94ee-4a55-9751-74b5643aa27d}'
)


class IDvdCmd(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDvdCmd
    _idlflags_ = []


IID_IDvdState = IID(
    '{86303d6d-1c4a-4087-ab42-f711167048ef}'
)


class IDvdState(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDvdState
    _idlflags_ = []


IID_IDvdControl2 = IID(
    '{33BC7430-EEC0-11D2-8201-00A0C9D74842}'
)


class IDvdControl2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDvdControl2
    _idlflags_ = []


IID_IDvdInfo2 = IID(
    '{34151510-EEC0-11D2-8201-00A0C9D74842}'
)


class IDvdInfo2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDvdInfo2
    _idlflags_ = []


IID_IDvdGraphBuilder = IID(
    '{FCC152B6-F372-11d0-8E00-00C04FD7C08B}'
)


class IDvdGraphBuilder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDvdGraphBuilder
    _idlflags_ = []


IID_IDDrawExclModeVideo = IID(
    '{153ACC21-D83B-11d1-82BF-00A0C9696C8F}'
)


class IDDrawExclModeVideo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDDrawExclModeVideo
    _idlflags_ = []


IID_IDDrawExclModeVideoCallback = IID(
    '{913c24a0-20ab-11d2-9038-00a0c9697298}'
)


class IDDrawExclModeVideoCallback(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDDrawExclModeVideoCallback
    _idlflags_ = []



CDEF_CLASS_DEFAULT = 0x0001
CDEF_BYPASS_CLASS_MANAGER = 0x0002
CDEF_MERIT_ABOVE_DO_NOT_USE = 0x0008
CDEF_DEVMON_CMGR_DEVICE = 0x0010
CDEF_DEVMON_DMO = 0x0020
CDEF_DEVMON_PNP_DEVICE = 0x0040
CDEF_DEVMON_FILTER = 0x0080
CDEF_DEVMON_SELECTIVE_MASK = 0x00f0
COMMETHOD = comtypes.COMMETHOD


ICreateDevEnum._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateClassEnumerator',
        (['in'], REFCLSID, 'clsidDeviceClass'),
        (['out'], POINTER(POINTER(IEnumMoniker)), 'ppEnumMoniker'),
        (['in'], DWORD, 'dwFlags'),
    ),
]


CHARS_IN_GUID = 0x27

class _AMMediaType(ctypes.Structure):
    _fields_ = [
        ('majortype', GUID),
        ('subtype', GUID),
        ('bFixedSizeSamples', BOOL),
        ('bTemporalCompression', BOOL),
        ('lSampleSize', ULONG),
        ('formattype', GUID),
        ('pUnk', POINTER(comtypes.IUnknown)),
        ('cbFormat', ULONG),
        ('pbFormat', POINTER(BYTE)),
    ]


AM_MEDIA_TYPE = _AMMediaType


class _PinDirection(ENUM):
    PINDIR_INPUT = 0
    PINDIR_OUTPUT = PINDIR_INPUT + 1


PIN_DIRECTION = _PinDirection


MAX_PIN_NAME = 0x80
MAX_FILTER_NAME = 0x80
REFTIME = DOUBLE
HSEMAPHORE = DWORD_PTR

class _AllocatorProperties(ctypes.Structure):
    _fields_ = [
        ('cBuffers', LONG),
        ('cbBuffer', LONG),
        ('cbAlign', LONG),
        ('cbPrefix', LONG),
    ]


ALLOCATOR_PROPERTIES = _AllocatorProperties



class _PinInfo(ctypes.Structure):
    _fields_ = [
        ('pFilter', POINTER(IBaseFilter)),
        ('dir', PIN_DIRECTION),
        ('achName', WCHAR * 128),
    ]


PIN_INFO = _PinInfo


IPin._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Connect',
        (['in'], POINTER(IPin), 'pReceivePin'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReceiveConnection',
        (['in'], POINTER(IPin), 'pConnector'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectedTo',
        (['out'], POINTER(POINTER(IPin)), 'pPin'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectionMediaType',
        (['out'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryPinInfo',
        (['out'], POINTER(PIN_INFO), 'pInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryDirection',
        (['out'], POINTER(PIN_DIRECTION), 'pPinDir'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryId',
        (['out'], POINTER(LPWSTR), 'Id'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryAccept',
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumMediaTypes',
        (['out'], POINTER(POINTER(IEnumMediaTypes)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryInternalConnections',
        ([], POINTER(POINTER(IPin)), 'apPin'),
        (['in', 'out'], POINTER(ULONG), 'nPin'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NewSegment',
        (['in'], REFERENCE_TIME, 'tStart'),
        (['in'], REFERENCE_TIME, 'tStop'),
        (['in'], DOUBLE, 'dRate'),
    ),
]


PPIN = POINTER(IPin)
IEnumPins._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cPins'),
        ([], POINTER(POINTER(IPin)), 'ppPins'),
        (['out'], POINTER(ULONG), 'pcFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cPins'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumPins)), 'ppEnum'),
    ),
]


PENUMPINS = POINTER(IEnumPins)
IEnumMediaTypes._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cMediaTypes'),
        ([], POINTER(POINTER(AM_MEDIA_TYPE)), 'ppMediaTypes'),
        (['out'], POINTER(ULONG), 'pcFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cMediaTypes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumMediaTypes)), 'ppEnum'),
    ),
]


PENUMMEDIATYPES = POINTER(IEnumMediaTypes)
IFilterGraph._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddFilter',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
        (['in'], LPCWSTR, 'pName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveFilter',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumFilters',
        (['out'], POINTER(POINTER(IEnumFilters)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindFilterByName',
        (['in'], LPCWSTR, 'pName'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectDirect',
        (['in'], POINTER(IPin), 'ppinOut'),
        (['in'], POINTER(IPin), 'ppinIn'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Reconnect',
        (['in'], POINTER(IPin), 'ppin'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Disconnect',
        (['in'], POINTER(IPin), 'ppin'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultSyncSource'
    ),
]


PFILTERGRAPH = POINTER(IFilterGraph)
IEnumFilters._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cFilters'),
        ([], POINTER(POINTER(IBaseFilter)), 'ppFilter'),
        (['out'], POINTER(ULONG), 'pcFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cFilters'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumFilters)), 'ppEnum'),
    ),
]


PENUMFILTERS = POINTER(IEnumFilters)
class _FilterState(ENUM):
    State_Stopped = 0
    State_Paused = State_Stopped + 1
    State_Running = State_Paused + 1


FILTER_STATE = _FilterState


IMediaFilter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Run',
        ([], REFERENCE_TIME, 'tStart'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        (['in'], DWORD, 'dwMilliSecsTimeout'),
        (['out'], POINTER(FILTER_STATE), 'State'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSyncSource',
        (['in'], POINTER(IReferenceClock), 'pClock'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSyncSource',
        (['out'], POINTER(POINTER(IReferenceClock)), 'pClock'),
    ),
]


PMEDIAFILTER = POINTER(IMediaFilter)

class _FilterInfo(ctypes.Structure):
    _fields_ = [
        ('achName', WCHAR * 128),
        ('pGraph', POINTER(IFilterGraph)),
    ]


FILTER_INFO = _FilterInfo


IBaseFilter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumPins',
        (['out'], POINTER(POINTER(IEnumPins)), 'ppEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindPin',
        (['in'], LPCWSTR, 'Id'),
        (['out'], POINTER(POINTER(IPin)), 'ppPin'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryFilterInfo',
        (['out'], POINTER(FILTER_INFO), 'pInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'JoinFilterGraph',
        (['in'], POINTER(IFilterGraph), 'pGraph'),
        (['in'], LPCWSTR, 'pName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryVendorInfo',
        (['out'], POINTER(LPWSTR), 'pVendorInfo'),
    ),
]


PFILTER = POINTER(IBaseFilter)
IReferenceClock._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTime',
        (['out'], POINTER(REFERENCE_TIME), 'pTime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AdviseTime',
        (['in'], REFERENCE_TIME, 'baseTime'),
        (['in'], REFERENCE_TIME, 'streamTime'),
        (['in'], HEVENT, 'hEvent'),
        (['out'], POINTER(DWORD_PTR), 'pdwAdviseCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AdvisePeriodic',
        (['in'], REFERENCE_TIME, 'startTime'),
        (['in'], REFERENCE_TIME, 'periodTime'),
        (['in'], HSEMAPHORE, 'hSemaphore'),
        (['out'], POINTER(DWORD_PTR), 'pdwAdviseCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise',
        (['in'], DWORD_PTR, 'dwAdviseCookie'),
    ),
]


PREFERENCECLOCK = POINTER(IReferenceClock)
IReferenceClockTimerControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultTimerResolution',
        ([], REFERENCE_TIME, 'timerResolution'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultTimerResolution',
        ([], POINTER(REFERENCE_TIME), 'pTimerResolution'),
    ),
]


PREFERENCECLOCK2 = POINTER(IReferenceClock2)
IMediaSample._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPoINTer',
        ([], POINTER(POINTER(BYTE)), 'ppBuffer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTime',
        (['out'], POINTER(REFERENCE_TIME), 'pTimeStart'),
        (['out'], POINTER(REFERENCE_TIME), 'pTimeEnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTime',
        (['in'], POINTER(REFERENCE_TIME), 'pTimeStart'),
        (['in'], POINTER(REFERENCE_TIME), 'pTimeEnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSyncPoINT',
        ([], BOOL, 'bIsSyncPoINT'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPreroll',
        ([], BOOL, 'bIsPreroll'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetActualDataLength',
        ([], LONG, '__MIDL__IMediaSample0000'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMediaType',
        (['out'], POINTER(POINTER(AM_MEDIA_TYPE)), 'ppMediaType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMediaType',
        (['in'], POINTER(AM_MEDIA_TYPE), 'pMediaType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDiscontinuity',
        ([], BOOL, 'bDiscontinuity'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMediaTime',
        (['out'], POINTER(LONGLONG), 'pTimeStart'),
        (['out'], POINTER(LONGLONG), 'pTimeEnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMediaTime',
        (['in'], POINTER(LONGLONG), 'pTimeStart'),
        (['in'], POINTER(LONGLONG), 'pTimeEnd'),
    ),
]


PMEDIASAMPLE = POINTER(IMediaSample)

class tagAM_SAMPLE2_PROPERTIES(ctypes.Structure):
    _fields_ = [
        ('cbData', DWORD),
        ('dwTypeSpecificFlags', DWORD),
        ('dwSampleFlags', DWORD),
        ('lActual', LONG),
        ('tStart', REFERENCE_TIME),
        ('tStop', REFERENCE_TIME),
        ('dwStreamId', DWORD),
        ('pMediaType', POINTER(AM_MEDIA_TYPE)),
        ('pbBuffer', POINTER(BYTE)),
        ('cbBuffer', LONG),
    ]


AM_SAMPLE2_PROPERTIES = tagAM_SAMPLE2_PROPERTIES


IMediaSample2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetProperties',
        (['in'], DWORD, 'cbProperties'),
        (['out'], POINTER(BYTE), 'pbProperties'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetProperties',
        (['in'], DWORD, 'cbProperties'),
        (['in'], POINTER(BYTE), 'pbProperties'),
    ),
]


PMEDIASAMPLE2 = POINTER(IMediaSample2)
IMediaSample2Config._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSurface',
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppDirect3DSurface9'),
    ),
]


AM_GBF_PREVFRAMESKIPPED = 0x1
AM_GBF_NOTASYNCPOINT = 0x2
AM_GBF_NOWAIT = 0x4
AM_GBF_NODDSURFACELOCK = 0x8
IMemAllocator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetProperties',
        (['in'], POINTER(ALLOCATOR_PROPERTIES), 'pRequest'),
        (['out'], POINTER(ALLOCATOR_PROPERTIES), 'pActual'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetProperties',
        (['out'], POINTER(ALLOCATOR_PROPERTIES), 'pProps'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBuffer',
        (['out'], POINTER(POINTER(IMediaSample)), 'ppBuffer'),
        (['in'], POINTER(REFERENCE_TIME), 'pStartTime'),
        (['in'], POINTER(REFERENCE_TIME), 'pEndTime'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseBuffer',
        (['in'], POINTER(IMediaSample), 'pBuffer'),
    ),
]


PMEMALLOCATOR = POINTER(IMemAllocator)
IMemAllocatorCallbackTemp._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetNotify',
        (['in'], POINTER(IMemAllocatorNotifyCallbackTemp), 'pNotify'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFreeCount',
        (['out'], POINTER(LONG), 'plBuffersFree'),
    ),
]


IMemAllocatorNotifyCallbackTemp._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'NotifyRelease'
    ),
]


IMemInputPin._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetAllocator',
        (['out'], POINTER(POINTER(IMemAllocator)), 'ppAllocator'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyAllocator',
        (['in'], POINTER(IMemAllocator), 'pAllocator'),
        (['in'], BOOL, 'bReadOnly'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllocatorRequirements',
        (['out'], POINTER(ALLOCATOR_PROPERTIES), 'pProps'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Receive',
        (['in'], POINTER(IMediaSample), 'pSample'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReceiveMultiple',
        (['in'], POINTER(POINTER(IMediaSample)), 'pSamples'),
        (['in'], LONG, 'nSamples'),
        (['out'], POINTER(LONG), 'nSamplesProcessed'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReceiveCanBlock'
    ),
]


PMEMINPUTPIN = POINTER(IMemInputPin)
IAMovieSetup._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Unregister'
    ),
]


PAMOVIESETUP = POINTER(IAMovieSetup)
class AM_SEEKING_SeekingFlags(ENUM):
    AM_SEEKING_NoPositioning = 0
    AM_SEEKING_AbsolutePositioning = 0x1
    AM_SEEKING_RelativePositioning = 0x2
    AM_SEEKING_IncrementalPositioning = 0x3
    AM_SEEKING_PositioningBitsMask = 0x3
    AM_SEEKING_SeekToKeyFrame = 0x4
    AM_SEEKING_ReturnTime = 0x8
    AM_SEEKING_Segment = 0x10
    AM_SEEKING_NoFlush = 0x20


AM_SEEKING_SEEKING_FLAGS = AM_SEEKING_SeekingFlags


class AM_SEEKING_SeekingCapabilities(ENUM):
    AM_SEEKING_CanSeekAbsolute = 0x1
    AM_SEEKING_CanSeekForwards = 0x2
    AM_SEEKING_CanSeekBackwards = 0x4
    AM_SEEKING_CanGetCurrentPos = 0x8
    AM_SEEKING_CanGetStopPos = 0x10
    AM_SEEKING_CanGetDuration = 0x20
    AM_SEEKING_CanPlayBackwards = 0x40
    AM_SEEKING_CanDoSegments = 0x80
    AM_SEEKING_Source = 0x100


AM_SEEKING_SEEKING_CAPABILITIES = AM_SEEKING_SeekingCapabilities


IMediaSeeking._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCapabilities',
        (['out'], POINTER(DWORD), 'pCapabilities'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CheckCapabilities',
        (['in', 'out'], POINTER(DWORD), 'pCapabilities'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsFormatSupported',
        (['in'], POINTER(GUID), 'pFormat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryPreferredFormat',
        (['out'], POINTER(GUID), 'pFormat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTimeFormat',
        (['out'], POINTER(GUID), 'pFormat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsUsingTimeFormat',
        (['in'], POINTER(GUID), 'pFormat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTimeFormat',
        (['in'], POINTER(GUID), 'pFormat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDuration',
        (['out'], POINTER(LONGLONG), 'pDuration'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStopPosition',
        (['out'], POINTER(LONGLONG), 'pStop'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentPosition',
        (['out'], POINTER(LONGLONG), 'pCurrent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConvertTimeFormat',
        (['out'], POINTER(LONGLONG), 'pTarget'),
        (['in'], POINTER(GUID), 'pTargetFormat'),
        (['in'], LONGLONG, 'Source'),
        (['in'], POINTER(GUID), 'pSourceFormat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPositions',
        (['in', 'out'], POINTER(LONGLONG), 'pCurrent'),
        (['in'], DWORD, 'dwCurrentFlags'),
        (['in', 'out'], POINTER(LONGLONG), 'pStop'),
        (['in'], DWORD, 'dwStopFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPositions',
        (['out'], POINTER(LONGLONG), 'pCurrent'),
        (['out'], POINTER(LONGLONG), 'pStop'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAvailable',
        (['out'], POINTER(LONGLONG), 'pEarliest'),
        (['out'], POINTER(LONGLONG), 'pLatest'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetRate',
        (['in'], DOUBLE, 'dRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRate',
        (['out'], POINTER(DOUBLE), 'pdRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPreroll',
        (['out'], POINTER(LONGLONG), 'pllPreroll'),
    ),
]


PMEDIASEEKING = POINTER(IMediaSeeking)
from .winapifamily_h import * # NOQA
from .winapifamily_h import * # NOQA

class CodecAPIEventData(ctypes.Structure):
    _fields_ = [
        ('guid', GUID),
        ('dataLength', DWORD),
        ('reserved', DWORD * 3),
    ]



ICodecAPI._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'IsSupported',
        (['in'], POINTER(GUID), 'Api'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsModifiable',
        (['in'], POINTER(GUID), 'Api'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParameterRange',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(VARIANT), 'ValueMin'),
        (['out'], POINTER(VARIANT), 'ValueMax'),
        (['out'], POINTER(VARIANT), 'SteppingDelta'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParameterValues',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(POINTER(VARIANT)), 'Values'),
        (['out'], POINTER(ULONG), 'ValuesCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultValue',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(VARIANT), 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetValue',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(VARIANT), 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetValue',
        (['in'], POINTER(GUID), 'Api'),
        (['in'], POINTER(VARIANT), 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterForEvent',
        (['in'], POINTER(GUID), 'Api'),
        (['in'], LONG_PTR, 'userData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterForEvent',
        (['in'], POINTER(GUID), 'Api'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetValueWithNotify',
        (['in'], POINTER(GUID), 'Api'),
        (['in'], POINTER(VARIANT), 'Value'),
        (['out'], POINTER(POINTER(GUID)), 'ChangedParam'),
        (['out'], POINTER(ULONG), 'ChangedParamCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAllDefaultsWithNotify',
        (['out'], POINTER(POINTER(GUID)), 'ChangedParam'),
        (['out'], POINTER(ULONG), 'ChangedParamCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllSettings',
        (['in'], POINTER(IStream), '__MIDL__ICodecAPI0000'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAllSettings',
        (['in'], POINTER(IStream), '__MIDL__ICodecAPI0001'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAllSettingsWithNotify',
        ([], POINTER(IStream), '__MIDL__ICodecAPI0002'),
        (['out'], POINTER(POINTER(GUID)), 'ChangedParam'),
        (['out'], POINTER(ULONG), 'ChangedParamCount'),
    ),
]



class REGFILTER(ctypes.Structure):
    _fields_ = [
        ('Clsid', CLSID),
        ('Name', LPWSTR),
    ]



IEnumRegFilters._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cFilters'),
        ([], POINTER(POINTER(REGFILTER)), 'apRegFilter'),
        (['out'], POINTER(ULONG), 'pcFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cFilters'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumRegFilters)), 'ppEnum'),
    ),
]


PENUMREGFILTERS = POINTER(IEnumRegFilters)

class __MIDL_IFilterMapper_0001(ENUM):
    MERIT_PREFERRED = 0x800000
    MERIT_NORMAL = 0x600000
    MERIT_UNLIKELY = 0x400000
    MERIT_DO_NOT_USE = 0x200000
    MERIT_SW_COMPRESSOR = 0x100000
    MERIT_HW_COMPRESSOR = 0x100050


IFilterMapper._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RegisterFilter',
        (['in'], CLSID, 'clsid'),
        (['in'], LPCWSTR, 'Name'),
        (['in'], DWORD, 'dwMerit'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterFilterInstance',
        (['in'], CLSID, 'clsid'),
        (['in'], LPCWSTR, 'Name'),
        (['out'], POINTER(CLSID), 'MRId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterPin',
        (['in'], CLSID, 'Filter'),
        (['in'], LPCWSTR, 'Name'),
        (['in'], BOOL, 'bRendered'),
        (['in'], BOOL, 'bOutput'),
        (['in'], BOOL, 'bZero'),
        (['in'], BOOL, 'bMany'),
        (['in'], CLSID, 'ConnectsToFilter'),
        (['in'], LPCWSTR, 'ConnectsToPin'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterPinType',
        (['in'], CLSID, 'clsFilter'),
        (['in'], LPCWSTR, 'strName'),
        (['in'], CLSID, 'clsMajorType'),
        (['in'], CLSID, 'clsSubType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterFilter',
        (['in'], CLSID, 'Filter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterFilterInstance',
        (['in'], CLSID, 'MRId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterPin',
        (['in'], CLSID, 'Filter'),
        (['in'], LPCWSTR, 'Name'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumMatchingFilters',
        (['out'], POINTER(POINTER(IEnumRegFilters)), 'ppEnum'),
        (['in'], DWORD, 'dwMerit'),
        (['in'], BOOL, 'bInputNeeded'),
        (['in'], CLSID, 'clsInMaj'),
        (['in'], CLSID, 'clsInSub'),
        (['in'], BOOL, 'bRender'),
        (['in'], BOOL, 'bOututNeeded'),
        (['in'], CLSID, 'clsOutMaj'),
        (['in'], CLSID, 'clsOutSub'),
    ),
]


class REGPINTYPES(ctypes.Structure):
    _fields_ = [
        ('clsMajorType', POINTER(CLSID)),
        ('clsMinorType', POINTER(CLSID)),
    ]


class REGFILTERPINS(ctypes.Structure):
    _fields_ = [
        ('strName', LPWSTR),
        ('bRendered', BOOL),
        ('bOutput', BOOL),
        ('bZero', BOOL),
        ('bMany', BOOL),
        ('clsConnectsToFilter', POINTER(CLSID)),
        ('strConnectsToPin', POINTER(WCHAR)),
        ('nMediaTypes', UINT),
        ('lpMediaType', POINTER(REGPINTYPES)),
    ]


class REGPINMEDIUM(ctypes.Structure):
    _fields_ = [
        ('clsMedium', CLSID),
        ('dw1', DWORD),
        ('dw2', DWORD),
    ]


class __MIDL___MIDL_itf_strmif_0000_0023_0001(ENUM):
    REG_PINFLAG_B_ZERO = 0x1
    REG_PINFLAG_B_RENDERER = 0x2
    REG_PINFLAG_B_MANY = 0x4
    REG_PINFLAG_B_OUTPUT = 0x8


class REGFILTERPINS2(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('cInstances', UINT),
        ('nMediaTypes', UINT),
        ('lpMediaType', POINTER(REGPINTYPES)),
        ('nMediums', UINT),
        ('lpMedium', POINTER(REGPINMEDIUM)),
        ('clsPinCategory', POINTER(CLSID)),
    ]


class REGFILTER2(ctypes.Structure):

    class _Union_0(ctypes.Union):

        class _Struct_0(ctypes.Structure):
            _fields_ = [
                ('cPins', ULONG),
                ('rgPins', POINTER(REGFILTERPINS)),
            ]

        class _Struct_1(ctypes.Structure):
            _fields_ = [
                ('cPins2', ULONG),
                ('rgPins2', POINTER(REGFILTERPINS2)),
            ]

        _anonymous_ = ('_Struct_0', '_Struct_1', )
        _fields_ = [
            ('_Struct_0', _Struct_0),
            ('_Struct_1', _Struct_1),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('dwVersion', DWORD),
        ('dwMerit', DWORD),
        ('_Union_0', _Union_0),
    ]


IFilterMapper2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateCategory',
        (['in'], REFCLSID, 'clsidCategory'),
        (['in'], DWORD, 'dwCategoryMerit'),
        (['in'], LPCWSTR, 'Description'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnregisterFilter',
        (['in'], POINTER(CLSID), 'pclsidCategory'),
        (['in'], LPCOLESTR, 'szInstance'),
        (['in'], REFCLSID, 'Filter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterFilter',
        (['in'], REFCLSID, 'clsidFilter'),
        (['in'], LPCWSTR, 'Name'),
        (['in', 'out'], POINTER(POINTER(IMoniker)), 'ppMoniker'),
        (['in'], POINTER(CLSID), 'pclsidCategory'),
        (['in'], LPCOLESTR, 'szInstance'),
        (['in'], POINTER(REGFILTER2), 'prf2'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumMatchingFilters',
        (['out'], POINTER(POINTER(IEnumMoniker)), 'ppEnum'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], BOOL, 'bExactMatch'),
        (['in'], DWORD, 'dwMerit'),
        (['in'], BOOL, 'bInputNeeded'),
        (['in'], DWORD, 'cInputTypes'),
        ([], POINTER(GUID), 'pInputTypes'),
        (['in'], POINTER(REGPINMEDIUM), 'pMedIn'),
        (['in'], POINTER(CLSID), 'pPinCategoryIn'),
        (['in'], BOOL, 'bRender'),
        (['in'], BOOL, 'bOutputNeeded'),
        (['in'], DWORD, 'cOutputTypes'),
        ([], POINTER(GUID), 'pOutputTypes'),
        (['in'], POINTER(REGPINMEDIUM), 'pMedOut'),
        (['in'], POINTER(CLSID), 'pPinCategoryOut'),
    ),
]


IFilterMapper3._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetICreateDevEnum',
        (['out'], POINTER(POINTER(ICreateDevEnum)), 'ppEnum'),
    ),
]


class tagQualityMessageType(ENUM):
    Famine = 0
    Flood = Famine + 1


QualityMessageType = tagQualityMessageType


class tagQuality(ctypes.Structure):
    _fields_ = [
        ('Type', QualityMessageType),
        ('Proportion', LONG),
        ('Late', REFERENCE_TIME),
        ('TimeStamp', REFERENCE_TIME),
    ]


Quality = tagQuality


PQUALITYCONTROL = POINTER(IQualityControl)
IQualityControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Notify',
        (['in'], POINTER(IBaseFilter), 'pSelf'),
        (['in'], Quality, 'q'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSink',
        (['in'], POINTER(IQualityControl), 'piqc'),
    ),
]


class __MIDL___MIDL_itf_strmif_0000_0026_0001(ENUM):
    CK_NOCOLORKEY = 0
    CK_INDEX = 0x1
    CK_RGB = 0x2


class tagCOLORKEY(ctypes.Structure):
    _fields_ = [
        ('KeyType', DWORD),
        ('PaletteIndex', DWORD),
        ('LowColorValue', COLORREF),
        ('HighColorValue', COLORREF),
    ]


COLORKEY = tagCOLORKEY


class __MIDL___MIDL_itf_strmif_0000_0026_0002(ENUM):
    ADVISE_NONE = 0
    ADVISE_CLIPPING = 0x1
    ADVISE_PALETTE = 0x2
    ADVISE_COLORKEY = 0x4
    ADVISE_POSITION = 0x8
    ADVISE_DISPLAY_CHANGE = 0x10

ADVISE_ALL = (
    (
        (
            __MIDL___MIDL_itf_strmif_0000_0026_0002.ADVISE_CLIPPING |
            __MIDL___MIDL_itf_strmif_0000_0026_0002.ADVISE_PALETTE
        ) |
        __MIDL___MIDL_itf_strmif_0000_0026_0002.ADVISE_COLORKEY
    ) |
    __MIDL___MIDL_itf_strmif_0000_0026_0002.ADVISE_POSITION
)

ADVISE_ALL2 = (
    ADVISE_ALL |
    __MIDL___MIDL_itf_strmif_0000_0026_0002.ADVISE_DISPLAY_CHANGE
)

class _RGNDATAHEADER(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('iType', DWORD),
        ('nCount', DWORD),
        ('nRgnSize', DWORD),
        ('rcBound', RECT),
    ]


RGNDATAHEADER = _RGNDATAHEADER



class _RGNDATA(ctypes.Structure):
    _fields_ = [
        ('rdh', RGNDATAHEADER),
        ('Buffer', CHAR * 1),
    ]


RGNDATA = _RGNDATA


IOverlayNotify._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnPaletteChange',
        (['in'], DWORD, 'dwColors'),
        (['in'], POINTER(PALETTEENTRY), 'pPalette'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnClipChange',
        (['in'], POINTER(RECT), 'pSourceRect'),
        (['in'], POINTER(RECT), 'pDestinationRect'),
        (['in'], POINTER(RGNDATA), 'pRgnData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnColorKeyChange',
        (['in'], POINTER(COLORKEY), 'pColorKey'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnPositionChange',
        (['in'], POINTER(RECT), 'pSourceRect'),
        (['in'], POINTER(RECT), 'pDestinationRect'),
    ),
]


POVERLAYNOTIFY = POINTER(IOverlayNotify)
IOverlayNotify2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnDisplayChange',
        ([], HMONITOR, 'hMonitor'),
    ),
]


POVERLAYNOTIFY2 = POINTER(IOverlayNotify2)
IOverlay._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPalette',
        (['out'], POINTER(DWORD), 'pdwColors'),
        ([], POINTER(POINTER(PALETTEENTRY)), 'ppPalette'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPalette',
        (['in'], DWORD, 'dwColors'),
        (['in'], POINTER(PALETTEENTRY), 'pPalette'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultColorKey',
        (['out'], POINTER(COLORKEY), 'pColorKey'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetColorKey',
        (['out'], POINTER(COLORKEY), 'pColorKey'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetColorKey',
        (['in', 'out'], POINTER(COLORKEY), 'pColorKey'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetWindowHandle',
        (['out'], POINTER(HWND), 'pHwnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetClipList',
        (['out'], POINTER(RECT), 'pSourceRect'),
        (['out'], POINTER(RECT), 'pDestinationRect'),
        (['out'], POINTER(POINTER(RGNDATA)), 'ppRgnData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVideoPosition',
        (['out'], POINTER(RECT), 'pSourceRect'),
        (['out'], POINTER(RECT), 'pDestinationRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Advise',
        (['in'], POINTER(IOverlayNotify), 'pOverlayNotify'),
        (['in'], DWORD, 'dwInterests'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise'
    ),
]


POVERLAY = POINTER(IOverlay)
IMediaEventSink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Notify',
        (['in'], LONG, 'EventCode'),
        (['in'], LONG_PTR, 'EventParam1'),
        (['in'], LONG_PTR, 'EventParam2'),
    ),
]


PMEDIAEVENTSINK = POINTER(IMediaEventSink)
IFileSourceFilter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], LPCOLESTR, 'pszFileName'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurFile',
        (['out'], POINTER(LPOLESTR), 'ppszFileName'),
        (['out'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
]


PFILTERFILESOURCE = POINTER(IFileSourceFilter)
IFileSinkFilter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetFileName',
        (['in'], LPCOLESTR, 'pszFileName'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurFile',
        (['out'], POINTER(LPOLESTR), 'ppszFileName'),
        (['out'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
]


PFILTERFILESINK = POINTER(IFileSinkFilter)
IFileSinkFilter2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetMode',
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMode',
        (['out'], POINTER(DWORD), 'pdwFlags'),
    ),
]


PFILESINKFILTER2 = POINTER(IFileSinkFilter2)
class AM_FILESINK_FLAGS(ENUM):
    AM_FILE_OVERWRITE = 0x1



IGraphBuilder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Connect',
        (['in'], POINTER(IPin), 'ppinOut'),
        (['in'], POINTER(IPin), 'ppinIn'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Render',
        (['in'], POINTER(IPin), 'ppinOut'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenderFile',
        (['in'], LPCWSTR, 'lpcwstrFile'),
        (['in'], LPCWSTR, 'lpcwstrPlayList'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddSourceFilter',
        (['in'], LPCWSTR, 'lpcwstrFileName'),
        (['in'], LPCWSTR, 'lpcwstrFilterName'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLogFile',
        (['in'], DWORD_PTR, 'hFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ShouldOperationContinue'
    ),
]


ICaptureGraphBuilder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetFiltergraph',
        (['in'], POINTER(IGraphBuilder), 'pfg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFiltergraph',
        (['out'], POINTER(POINTER(IGraphBuilder)), 'ppfg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetOutputFileName',
        (['in'], POINTER(GUID), 'pType'),
        (['in'], LPCOLESTR, 'lpstrFile'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppf'),
        (['out'], POINTER(POINTER(IFileSinkFilter)), 'ppSink'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindInterface',
        (['in'], POINTER(GUID), 'pCategory'),
        (['in'], POINTER(IBaseFilter), 'pf'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppINT'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenderStream',
        (['in'], POINTER(GUID), 'pCategory'),
        (['in'], POINTER(comtypes.IUnknown), 'pSource'),
        (['in'], POINTER(IBaseFilter), 'pfCompressor'),
        (['in'], POINTER(IBaseFilter), 'pfRenderer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ControlStream',
        (['in'], POINTER(GUID), 'pCategory'),
        (['in'], POINTER(IBaseFilter), 'pFilter'),
        (['in'], POINTER(REFERENCE_TIME), 'pstart'),
        (['in'], POINTER(REFERENCE_TIME), 'pstop'),
        (['in'], WORD, 'wStartCookie'),
        (['in'], WORD, 'wStopCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AllocCapFile',
        (['in'], LPCOLESTR, 'lpstr'),
        (['in'], DWORDLONG, 'dwlSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CopyCaptureFile',
        (['in'], LPOLESTR, 'lpwstrOld'),
        (['in'], LPOLESTR, 'lpwstrNew'),
        (['in'], INT, 'fAllowEscAbort'),
        (['in'], POINTER(IAMCopyCaptureFileProgress), 'pCallback'),
    ),
]


IAMCopyCaptureFileProgress._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Progress',
        (['in'], INT, 'iProgress'),
    ),
]


ICaptureGraphBuilder2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetFiltergraph',
        (['in'], POINTER(IGraphBuilder), 'pfg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFiltergraph',
        (['out'], POINTER(POINTER(IGraphBuilder)), 'ppfg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetOutputFileName',
        (['in'], POINTER(GUID), 'pType'),
        (['in'], LPCOLESTR, 'lpstrFile'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppf'),
        (['out'], POINTER(POINTER(IFileSinkFilter)), 'ppSink'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindInterface',
        (['in'], POINTER(GUID), 'pCategory'),
        (['in'], POINTER(GUID), 'pType'),
        (['in'], POINTER(IBaseFilter), 'pf'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppINT'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenderStream',
        (['in'], POINTER(GUID), 'pCategory'),
        (['in'], POINTER(GUID), 'pType'),
        (['in'], POINTER(comtypes.IUnknown), 'pSource'),
        (['in'], POINTER(IBaseFilter), 'pfCompressor'),
        (['in'], POINTER(IBaseFilter), 'pfRenderer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ControlStream',
        (['in'], POINTER(GUID), 'pCategory'),
        (['in'], POINTER(GUID), 'pType'),
        (['in'], POINTER(IBaseFilter), 'pFilter'),
        (['in'], POINTER(REFERENCE_TIME), 'pstart'),
        (['in'], POINTER(REFERENCE_TIME), 'pstop'),
        (['in'], WORD, 'wStartCookie'),
        (['in'], WORD, 'wStopCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AllocCapFile',
        (['in'], LPCOLESTR, 'lpstr'),
        (['in'], DWORDLONG, 'dwlSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CopyCaptureFile',
        (['in'], LPOLESTR, 'lpwstrOld'),
        (['in'], LPOLESTR, 'lpwstrNew'),
        (['in'], INT, 'fAllowEscAbort'),
        (['in'], POINTER(IAMCopyCaptureFileProgress), 'pCallback'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FindPin',
        (['in'], POINTER(comtypes.IUnknown), 'pSource'),
        (['in'], PIN_DIRECTION, 'pindir'),
        (['in'], POINTER(GUID), 'pCategory'),
        (['in'], POINTER(GUID), 'pType'),
        (['in'], BOOL, 'fUnconnected'),
        (['in'], INT, 'num'),
        (['out'], POINTER(POINTER(IPin)), 'ppPin'),
    ),
]


IFilterGraph2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddSourceFilterForMoniker',
        (['in'], POINTER(IMoniker), 'pMoniker'),
        (['in'], POINTER(IBindCtx), 'pCtx'),
        (['in'], LPCWSTR, 'lpcwstrFilterName'),
        (['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReconnectEx',
        (['in'], POINTER(IPin), 'ppin'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenderEx',
        (['in'], POINTER(IPin), 'pPinOut'),
        (['in'], DWORD, 'dwFlags'),
        (['in', 'out'], POINTER(DWORD), 'pvContext'),
    ),
]


IFilterGraph3._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetSyncSourceEx',
        (['in'], POINTER(IReferenceClock), 'pClockForMostOfFilterGraph'),
        (['in'], POINTER(IReferenceClock), 'pClockForFilter'),
        (['in'], POINTER(IBaseFilter), 'pFilter'),
    ),
]


IStreamBuilder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Render',
        (['in'], POINTER(IPin), 'ppinOut'),
        (['in'], POINTER(IGraphBuilder), 'pGraph'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Backout',
        (['in'], POINTER(IPin), 'ppinOut'),
        (['in'], POINTER(IGraphBuilder), 'pGraph'),
    ),
]


IAsyncReader._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RequestAllocator',
        (['in'], POINTER(IMemAllocator), 'pPreferred'),
        (['in'], POINTER(ALLOCATOR_PROPERTIES), 'pProps'),
        (['out'], POINTER(POINTER(IMemAllocator)), 'ppActual'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Request',
        (['in'], POINTER(IMediaSample), 'pSample'),
        (['in'], DWORD_PTR, 'dwUser'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'WaitForNext',
        (['in'], DWORD, 'dwTimeout'),
        (['out'], POINTER(POINTER(IMediaSample)), 'ppSample'),
        (['out'], POINTER(DWORD_PTR), 'pdwUser'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SyncReadAligned',
        (['in'], POINTER(IMediaSample), 'pSample'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SyncRead',
        (['in'], LONGLONG, 'llPosition'),
        (['in'], LONG, 'lLength'),
        (['out'], POINTER(BYTE), 'pBuffer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Length',
        (['out'], POINTER(LONGLONG), 'pTotal'),
        (['out'], POINTER(LONGLONG), 'pAvailable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EndFlush'
    ),
]


IGraphVersion._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryVersion',
        ([], POINTER(LONG), 'pVersion'),
    ),
]


IResourceConsumer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AcquireResource',
        (['in'], LONG, 'idResource'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseResource',
        (['in'], LONG, 'idResource'),
    ),
]


IResourceManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Register',
        (['in'], LPCWSTR, 'pName'),
        (['in'], LONG, 'cResource'),
        (['out'], POINTER(LONG), 'plToken'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterGroup',
        (['in'], LPCWSTR, 'pName'),
        (['in'], LONG, 'cResource'),
        (['in'], POINTER(LONG), 'palTokens'),
        (['out'], POINTER(LONG), 'plToken'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RequestResource',
        (['in'], LONG, 'idResource'),
        (['in'], POINTER(comtypes.IUnknown), 'pFocusObject'),
        (['in'], POINTER(IResourceConsumer), 'pConsumer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyAcquire',
        (['in'], LONG, 'idResource'),
        (['in'], POINTER(IResourceConsumer), 'pConsumer'),
        (['in'], HRESULT, 'hr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyRelease',
        (['in'], LONG, 'idResource'),
        (['in'], POINTER(IResourceConsumer), 'pConsumer'),
        (['in'], BOOL, 'bStillWant'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CancelRequest',
        (['in'], LONG, 'idResource'),
        (['in'], POINTER(IResourceConsumer), 'pConsumer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFocus',
        (['in'], POINTER(comtypes.IUnknown), 'pFocusObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseFocus',
        (['in'], POINTER(comtypes.IUnknown), 'pFocusObject'),
    ),
]


IDistributorNotify._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Run',
        ([], REFERENCE_TIME, 'tStart'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSyncSource',
        (['in'], POINTER(IReferenceClock), 'pClock'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyGraphChange'
    ),
]


class AM_STREAM_INFO_FLAGS(ENUM):
    AM_STREAM_INFO_START_DEFINED = 0x1
    AM_STREAM_INFO_STOP_DEFINED = 0x2
    AM_STREAM_INFO_DISCARDING = 0x4
    AM_STREAM_INFO_STOP_SEND_EXTRA = 0x10




class AM_STREAM_INFO(ctypes.Structure):
    _fields_ = [
        ('tStart', REFERENCE_TIME),
        ('tStop', REFERENCE_TIME),
        ('dwStartCookie', DWORD),
        ('dwStopCookie', DWORD),
        ('dwFlags', DWORD),
    ]



IAMStreamControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StartAt',
        (['in'], POINTER(REFERENCE_TIME), 'ptStart'),
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'StopAt',
        (['in'], POINTER(REFERENCE_TIME), 'ptStop'),
        (['in'], BOOL, 'bSendExtra'),
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetInfo',
        (['out'], POINTER(AM_STREAM_INFO), 'pInfo'),
    ),
]


ISeekingPassThru._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Init',
        (['in'], BOOL, 'bSupportRendering'),
        (['in'], POINTER(IPin), 'pPin'),
    ),
]



class _VIDEO_STREAM_CONFIG_CAPS(ctypes.Structure):
    _fields_ = [
        ('guid', GUID),
        ('VideoStandard', ULONG),
        ('InputSize', SIZE),
        ('MinCroppingSize', SIZE),
        ('MaxCroppingSize', SIZE),
        ('CropGranularityX', INT),
        ('CropGranularityY', INT),
        ('CropAlignX', INT),
        ('CropAlignY', INT),
        ('MinOutputSize', SIZE),
        ('MaxOutputSize', SIZE),
        ('OutputGranularityX', INT),
        ('OutputGranularityY', INT),
        ('StretchTapsX', INT),
        ('StretchTapsY', INT),
        ('ShrinkTapsX', INT),
        ('ShrinkTapsY', INT),
        ('MinFrameInterval', LONGLONG),
        ('MaxFrameInterval', LONGLONG),
        ('MinBitsPerSecond', LONG),
        ('MaxBitsPerSecond', LONG),
    ]


VIDEO_STREAM_CONFIG_CAPS = _VIDEO_STREAM_CONFIG_CAPS



class _AUDIO_STREAM_CONFIG_CAPS(ctypes.Structure):
    _fields_ = [
        ('guid', GUID),
        ('MinimumChannels', ULONG),
        ('MaximumChannels', ULONG),
        ('ChannelsGranularity', ULONG),
        ('MinimumBitsPerSample', ULONG),
        ('MaximumBitsPerSample', ULONG),
        ('BitsPerSampleGranularity', ULONG),
        ('MinimumSampleFrequency', ULONG),
        ('MaximumSampleFrequency', ULONG),
        ('SampleFrequencyGranularity', ULONG),
    ]


AUDIO_STREAM_CONFIG_CAPS = _AUDIO_STREAM_CONFIG_CAPS


IAMStreamConfig._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetFormat',
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFormat',
        (['out'], POINTER(POINTER(AM_MEDIA_TYPE)), 'ppmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNumberOfCapabilities',
        (['out'], POINTER(INT), 'piCount'),
        (['out'], POINTER(INT), 'piSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStreamCaps',
        (['in'], INT, 'iIndex'),
        (['out'], POINTER(POINTER(AM_MEDIA_TYPE)), 'ppmt'),
        (['out'], POINTER(BYTE), 'pSCC'),
    ),
]


class InterleavingMode(ENUM):
    INTERLEAVE_NONE = 0
    INTERLEAVE_CAPTURE = INTERLEAVE_NONE + 1
    INTERLEAVE_FULL = INTERLEAVE_CAPTURE + 1
    INTERLEAVE_NONE_BUFFERED = INTERLEAVE_FULL + 1



IConfigInterleaving._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'put_Mode',
        (['in'], InterleavingMode, 'mode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Mode',
        (['out'], POINTER(InterleavingMode), 'pMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Interleaving',
        (['in'], POINTER(REFERENCE_TIME), 'prtInterleave'),
        (['in'], POINTER(REFERENCE_TIME), 'prtPreroll'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Interleaving',
        (['out'], POINTER(REFERENCE_TIME), 'prtInterleave'),
        (['out'], POINTER(REFERENCE_TIME), 'prtPreroll'),
    ),
]


IConfigAviMux._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetMasterStream',
        (['in'], LONG, 'iStream'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMasterStream',
        (['out'], POINTER(LONG), 'pStream'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetOutputCompatibilityIndex',
        (['in'], BOOL, 'fOldIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetOutputCompatibilityIndex',
        (['out'], POINTER(BOOL), 'pfOldIndex'),
    ),
]


class CompressionCaps(ENUM):
    CompressionCaps_CanQuality = 0x1
    CompressionCaps_CanCrunch = 0x2
    CompressionCaps_CanKeyFrame = 0x4
    CompressionCaps_CanBFrame = 0x8
    CompressionCaps_CanWindow = 0x10



IAMVideoCompression._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'put_KeyFrameRate',
        (['in'], LONG, 'KeyFrameRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_KeyFrameRate',
        (['out'], POINTER(LONG), 'pKeyFrameRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_PFramesPerKeyFrame',
        (['in'], LONG, 'PFramesPerKeyFrame'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_PFramesPerKeyFrame',
        (['out'], POINTER(LONG), 'pPFramesPerKeyFrame'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Quality',
        (['in'], DOUBLE, 'Quality'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Quality',
        (['out'], POINTER(DOUBLE), 'pQuality'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_WindowSize',
        (['in'], DWORDLONG, 'WindowSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_WindowSize',
        (['out'], POINTER(DWORDLONG), 'pWindowSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetInfo',
        (['out'], LPWSTR, 'pszVersion'),
        (['in', 'out'], POINTER(INT), 'pcbVersion'),
        (['out'], LPWSTR, 'pszDescription'),
        (['in', 'out'], POINTER(INT), 'pcbDescription'),
        (['out'], POINTER(LONG), 'pDefaultKeyFrameRate'),
        (['out'], POINTER(LONG), 'pDefaultPFramesPerKey'),
        (['out'], POINTER(DOUBLE), 'pDefaultQuality'),
        (['out'], POINTER(LONG), 'pCapabilities'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OverrideKeyFrame',
        (['in'], LONG, 'FrameNumber'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OverrideFrameSize',
        (['in'], LONG, 'FrameNumber'),
        (['in'], LONG, 'Size'),
    ),
]


class VfwCaptureDialogs(ENUM):
    VfwCaptureDialog_Source = 0x1
    VfwCaptureDialog_Format = 0x2
    VfwCaptureDialog_Display = 0x4



class VfwCompressDialogs(ENUM):
    VfwCompressDialog_Config = 0x1
    VfwCompressDialog_About = 0x2
    VfwCompressDialog_QueryConfig = 0x4
    VfwCompressDialog_QueryAbout = 0x8



IAMVfwCaptureDialogs._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'HasDialog',
        (['in'], INT, 'iDialog'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ShowDialog',
        (['in'], INT, 'iDialog'),
        (['in'], HWND, 'hwnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SendDriverMessage',
        (['in'], INT, 'iDialog'),
        (['in'], INT, 'uMsg'),
        (['in'], LONG, 'dw1'),
        (['in'], LONG, 'dw2'),
    ),
]


IAMVfwCompressDialogs._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ShowDialog',
        (['in'], INT, 'iDialog'),
        (['in'], HWND, 'hwnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        ([], LPVOID, 'pState'),
        (['in', 'out'], POINTER(INT), 'pcbState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetState',
        (['in'], LPVOID, 'pState'),
        (['in'], INT, 'cbState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SendDriverMessage',
        (['in'], INT, 'uMsg'),
        (['in'], LONG, 'dw1'),
        (['in'], LONG, 'dw2'),
    ),
]


IAMDroppedFrames._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetNumDropped',
        (['out'], POINTER(LONG), 'plDropped'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNumNotDropped',
        (['out'], POINTER(LONG), 'plNotDropped'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDroppedInfo',
        (['in'], LONG, 'lSize'),
        (['out'], POINTER(LONG), 'plArray'),
        (['out'], POINTER(LONG), 'plNumCopied'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAverageFrameSize',
        (['out'], POINTER(LONG), 'plAverageSize'),
    ),
]


AMF_AUTOMATICGAIN = -1.0
IAMAudioInputMixer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'put_Enable',
        (['in'], BOOL, 'fEnable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Enable',
        (['out'], POINTER(BOOL), 'pfEnable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Mono',
        (['in'], BOOL, 'fMono'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Mono',
        (['out'], POINTER(BOOL), 'pfMono'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_MixLevel',
        (['in'], DOUBLE, 'Level'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_MixLevel',
        (['out'], POINTER(DOUBLE), 'pLevel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Pan',
        (['in'], DOUBLE, 'Pan'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Pan',
        (['out'], POINTER(DOUBLE), 'pPan'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Loudness',
        (['in'], BOOL, 'fLoudness'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Loudness',
        (['out'], POINTER(BOOL), 'pfLoudness'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Treble',
        (['in'], DOUBLE, 'Treble'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Treble',
        (['out'], POINTER(DOUBLE), 'pTreble'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_TrebleRange',
        (['out'], POINTER(DOUBLE), 'pRange'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Bass',
        (['in'], DOUBLE, 'Bass'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Bass',
        (['out'], POINTER(DOUBLE), 'pBass'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_BassRange',
        (['out'], POINTER(DOUBLE), 'pRange'),
    ),
]


IAMBufferNegotiation._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SuggestAllocatorProperties',
        (['in'], POINTER(ALLOCATOR_PROPERTIES), 'pprop'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllocatorProperties',
        (['out'], POINTER(ALLOCATOR_PROPERTIES), 'pprop'),
    ),
]


class tagAnalogVideoStandard(ENUM):
    AnalogVideo_None = 0
    AnalogVideo_NTSC_M = 0x1
    AnalogVideo_NTSC_M_J = 0x2
    AnalogVideo_NTSC_433 = 0x4
    AnalogVideo_PAL_B = 0x10
    AnalogVideo_PAL_D = 0x20
    AnalogVideo_PAL_G = 0x40
    AnalogVideo_PAL_H = 0x80
    AnalogVideo_PAL_I = 0x100
    AnalogVideo_PAL_M = 0x200
    AnalogVideo_PAL_N = 0x400
    AnalogVideo_PAL_60 = 0x800
    AnalogVideo_SECAM_B = 0x1000
    AnalogVideo_SECAM_D = 0x2000
    AnalogVideo_SECAM_G = 0x4000
    AnalogVideo_SECAM_H = 0x8000
    AnalogVideo_SECAM_K = 0x10000
    AnalogVideo_SECAM_K1 = 0x20000
    AnalogVideo_SECAM_L = 0x40000
    AnalogVideo_SECAM_L1 = 0x80000
    AnalogVideo_PAL_N_COMBO = 0x100000
    AnalogVideoMask_MCE_NTSC = (
        ( ( ( ( ( AnalogVideo_NTSC_M |
AnalogVideo_NTSC_M_J ) |
AnalogVideo_NTSC_433 ) |
AnalogVideo_PAL_M ) |
AnalogVideo_PAL_N ) |
AnalogVideo_PAL_60 ) |
AnalogVideo_PAL_N_COMBO
    )
    AnalogVideoMask_MCE_PAL = (
        ( ( ( AnalogVideo_PAL_B |
AnalogVideo_PAL_D ) |
AnalogVideo_PAL_G ) |
AnalogVideo_PAL_H ) |
AnalogVideo_PAL_I
    )
    AnalogVideoMask_MCE_SECAM = (
        ( ( ( ( ( ( AnalogVideo_SECAM_B |
AnalogVideo_SECAM_D ) |
AnalogVideo_SECAM_G ) |
AnalogVideo_SECAM_H ) |
AnalogVideo_SECAM_K ) |
AnalogVideo_SECAM_K1 ) |
AnalogVideo_SECAM_L ) |
AnalogVideo_SECAM_L1
    )


AnalogVideoStandard = tagAnalogVideoStandard


class tagTunerInputType(ENUM):
    TunerInputCable = 0
    TunerInputAntenna = TunerInputCable + 1


TunerInputType = tagTunerInputType


AnalogVideo_NTSC_Mask = 0x00000007
AnalogVideo_PAL_Mask = 0x00100FF0
AnalogVideo_SECAM_Mask = 0x000FF000
class VideoCopyProtectionType(ENUM):
    VideoCopyProtectionMacrovisionBasic = 0
    VideoCopyProtectionMacrovisionCBI = VideoCopyProtectionMacrovisionBasic + 1



class tagPhysicalConnectorType(ENUM):
    PhysConn_Video_Tuner = 1
    PhysConn_Video_Composite = PhysConn_Video_Tuner + 1
    PhysConn_Video_SVideo = PhysConn_Video_Composite + 1
    PhysConn_Video_RGB = PhysConn_Video_SVideo + 1
    PhysConn_Video_YRYBY = PhysConn_Video_RGB + 1
    PhysConn_Video_SerialDigital = PhysConn_Video_YRYBY + 1
    PhysConn_Video_ParallelDigital = PhysConn_Video_SerialDigital + 1
    PhysConn_Video_SCSI = PhysConn_Video_ParallelDigital + 1
    PhysConn_Video_AUX = PhysConn_Video_SCSI + 1
    PhysConn_Video_1394 = PhysConn_Video_AUX + 1
    PhysConn_Video_USB = PhysConn_Video_1394 + 1
    PhysConn_Video_VideoDecoder = PhysConn_Video_USB + 1
    PhysConn_Video_VideoEncoder = PhysConn_Video_VideoDecoder + 1
    PhysConn_Video_SCART = PhysConn_Video_VideoEncoder + 1
    PhysConn_Video_Black = PhysConn_Video_SCART + 1
    PhysConn_Audio_Tuner = 0x1000
    PhysConn_Audio_Line = PhysConn_Audio_Tuner + 1
    PhysConn_Audio_Mic = PhysConn_Audio_Line + 1
    PhysConn_Audio_AESDigital = PhysConn_Audio_Mic + 1
    PhysConn_Audio_SPDIFDigital = PhysConn_Audio_AESDigital + 1
    PhysConn_Audio_SCSI = PhysConn_Audio_SPDIFDigital + 1
    PhysConn_Audio_AUX = PhysConn_Audio_SCSI + 1
    PhysConn_Audio_1394 = PhysConn_Audio_AUX + 1
    PhysConn_Audio_USB = PhysConn_Audio_1394 + 1
    PhysConn_Audio_AudioDecoder = PhysConn_Audio_USB + 1


PhysicalConnectorType = tagPhysicalConnectorType


IAMAnalogVideoDecoder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_AvailableTVFormats',
        (['out'], POINTER(LONG), 'lAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_TVFormat',
        (['in'], LONG, 'lAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_TVFormat',
        (['out'], POINTER(LONG), 'plAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_HorizontalLocked',
        (['out'], POINTER(LONG), 'plLocked'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_VCRHorizontalLocking',
        (['in'], LONG, 'lVCRHorizontalLocking'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_VCRHorizontalLocking',
        (['out'], POINTER(LONG), 'plVCRHorizontalLocking'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_NumberOfLines',
        (['out'], POINTER(LONG), 'plNumberOfLines'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_OutputEnable',
        (['in'], LONG, 'lOutputEnable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_OutputEnable',
        (['out'], POINTER(LONG), 'plOutputEnable'),
    ),
]


class tagVideoProcAmpProperty(ENUM):
    VideoProcAmp_Brightness = 0
    VideoProcAmp_Contrast = VideoProcAmp_Brightness + 1
    VideoProcAmp_Hue = VideoProcAmp_Contrast + 1
    VideoProcAmp_Saturation = VideoProcAmp_Hue + 1
    VideoProcAmp_Sharpness = VideoProcAmp_Saturation + 1
    VideoProcAmp_Gamma = VideoProcAmp_Sharpness + 1
    VideoProcAmp_ColorEnable = VideoProcAmp_Gamma + 1
    VideoProcAmp_WhiteBalance = VideoProcAmp_ColorEnable + 1
    VideoProcAmp_BacklightCompensation = VideoProcAmp_WhiteBalance + 1
    VideoProcAmp_Gain = VideoProcAmp_BacklightCompensation + 1


VideoProcAmpProperty = tagVideoProcAmpProperty


class tagVideoProcAmpFlags(ENUM):
    VideoProcAmp_Flags_Auto = 0x1
    VideoProcAmp_Flags_Manual = 0x2


VideoProcAmpFlags = tagVideoProcAmpFlags


IAMVideoProcAmp._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetRange',
        (['in'], LONG, 'Property'),
        (['out'], POINTER(LONG), 'pMin'),
        (['out'], POINTER(LONG), 'pMax'),
        (['out'], POINTER(LONG), 'pSteppingDelta'),
        (['out'], POINTER(LONG), 'pDefault'),
        (['out'], POINTER(LONG), 'pCapsFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Set',
        (['in'], LONG, 'Property'),
        (['in'], LONG, 'lValue'),
        (['in'], LONG, 'Flags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Get',
        (['in'], LONG, 'Property'),
        (['out'], POINTER(LONG), 'lValue'),
        (['out'], POINTER(LONG), 'Flags'),
    ),
]


class tagCameraControlProperty(ENUM):
    CameraControl_Pan = 0
    CameraControl_Tilt = CameraControl_Pan + 1
    CameraControl_Roll = CameraControl_Tilt + 1
    CameraControl_Zoom = CameraControl_Roll + 1
    CameraControl_Exposure = CameraControl_Zoom + 1
    CameraControl_Iris = CameraControl_Exposure + 1
    CameraControl_Focus = CameraControl_Iris + 1


CameraControlProperty = tagCameraControlProperty


class tagCameraControlFlags(ENUM):
    CameraControl_Flags_Auto = 0x1
    CameraControl_Flags_Manual = 0x2


CameraControlFlags = tagCameraControlFlags


IAMCameraControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetRange',
        (['in'], LONG, 'Property'),
        (['out'], POINTER(LONG), 'pMin'),
        (['out'], POINTER(LONG), 'pMax'),
        (['out'], POINTER(LONG), 'pSteppingDelta'),
        (['out'], POINTER(LONG), 'pDefault'),
        (['out'], POINTER(LONG), 'pCapsFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Set',
        (['in'], LONG, 'Property'),
        (['in'], LONG, 'lValue'),
        (['in'], LONG, 'Flags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Get',
        (['in'], LONG, 'Property'),
        (['out'], POINTER(LONG), 'lValue'),
        (['out'], POINTER(LONG), 'Flags'),
    ),
]


class tagVideoControlFlags(ENUM):
    VideoControlFlag_FlipHorizontal = 0x1
    VideoControlFlag_FlipVertical = 0x2
    VideoControlFlag_ExternalTriggerEnable = 0x4
    VideoControlFlag_Trigger = 0x8


VideoControlFlags = tagVideoControlFlags


IAMVideoControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCaps',
        (['in'], POINTER(IPin), 'pPin'),
        (['out'], POINTER(LONG), 'pCapsFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMode',
        (['in'], POINTER(IPin), 'pPin'),
        (['in'], LONG, 'Mode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMode',
        (['in'], POINTER(IPin), 'pPin'),
        (['out'], POINTER(LONG), 'Mode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentActualFrameRate',
        (['in'], POINTER(IPin), 'pPin'),
        (['out'], POINTER(LONGLONG), 'ActualFrameRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMaxAvailableFrameRate',
        (['in'], POINTER(IPin), 'pPin'),
        (['in'], LONG, 'iIndex'),
        (['in'], SIZE, 'Dimensions'),
        (['out'], POINTER(LONGLONG), 'MaxAvailableFrameRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFrameRateList',
        (['in'], POINTER(IPin), 'pPin'),
        (['in'], LONG, 'iIndex'),
        (['in'], SIZE, 'Dimensions'),
        (['out'], POINTER(LONG), 'ListSize'),
        (['out'], POINTER(POINTER(LONGLONG)), 'FrameRates'),
    ),
]


IAMCrossbar._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_PinCounts',
        (['out'], POINTER(LONG), 'OutputPinCount'),
        (['out'], POINTER(LONG), 'InputPinCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CanRoute',
        (['in'], LONG, 'OutputPinIndex'),
        (['in'], LONG, 'InputPinIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Route',
        (['in'], LONG, 'OutputPinIndex'),
        (['in'], LONG, 'InputPinIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_IsRoutedTo',
        (['in'], LONG, 'OutputPinIndex'),
        (['out'], POINTER(LONG), 'InputPinIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_CrossbarPinInfo',
        (['in'], BOOL, 'IsInputPin'),
        (['in'], LONG, 'PinIndex'),
        (['out'], POINTER(LONG), 'PinIndexRelated'),
        (['out'], POINTER(LONG), 'PhysicalType'),
    ),
]


class tagAMTunerSubChannel(ENUM):
    AMTUNER_SUBCHAN_NO_TUNE = - 2
    AMTUNER_SUBCHAN_DEFAULT = - 1


AMTunerSubChannel = tagAMTunerSubChannel


class tagAMTunerSignalStrength(ENUM):
    AMTUNER_HASNOSIGNALSTRENGTH = - 1
    AMTUNER_NOSIGNAL = 0
    AMTUNER_SIGNALPRESENT = 1


AMTunerSignalStrength = tagAMTunerSignalStrength


class tagAMTunerModeType(ENUM):
    AMTUNER_MODE_DEFAULT = 0
    AMTUNER_MODE_TV = 0x1
    AMTUNER_MODE_FM_RADIO = 0x2
    AMTUNER_MODE_AM_RADIO = 0x4
    AMTUNER_MODE_DSS = 0x8


AMTunerModeType = tagAMTunerModeType


class tagAMTunerEventType(ENUM):
    AMTUNER_EVENT_CHANGED = 0x1


AMTunerEventType = tagAMTunerEventType


IAMTuner._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'put_Channel',
        (['in'], LONG, 'lChannel'),
        (['in'], LONG, 'lVideoSubChannel'),
        (['in'], LONG, 'lAudioSubChannel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Channel',
        (['out'], POINTER(LONG), 'plChannel'),
        (['out'], POINTER(LONG), 'plVideoSubChannel'),
        (['out'], POINTER(LONG), 'plAudioSubChannel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ChannelMinMax',
        (['out'], POINTER(LONG), 'lChannelMin'),
        (['out'], POINTER(LONG), 'lChannelMax'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_CountryCode',
        (['in'], LONG, 'lCountryCode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_CountryCode',
        (['out'], POINTER(LONG), 'plCountryCode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_TuningSpace',
        (['in'], LONG, 'lTuningSpace'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_TuningSpace',
        (['out'], POINTER(LONG), 'plTuningSpace'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Logon',
        (['in'], HANDLE, 'hCurrentUser'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SignalPresent',
        (['out'], POINTER(LONG), 'plSignalStrength'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Mode',
        (['in'], AMTunerModeType, 'lMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Mode',
        (['out'], POINTER(AMTunerModeType), 'plMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAvailableModes',
        (['out'], POINTER(LONG), 'plModes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterNotificationCallBack',
        (['in'], POINTER(IAMTunerNotification), 'pNotify'),
        (['in'], LONG, 'lEvents'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnRegisterNotificationCallBack',
        (['in'], POINTER(IAMTunerNotification), 'pNotify'),
    ),
]


IAMTunerNotification._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnEvent',
        (['in'], AMTunerEventType, 'Event'),
    ),
]


IAMTVTuner._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_AvailableTVFormats',
        (['out'], POINTER(LONG), 'lAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_TVFormat',
        (['out'], POINTER(LONG), 'plAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AutoTune',
        (['in'], LONG, 'lChannel'),
        (['out'], POINTER(LONG), 'plFoundSignal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_NumInputConnections',
        (['out'], POINTER(LONG), 'plNumInputConnections'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_InputType',
        (['in'], LONG, 'lIndex'),
        (['in'], TunerInputType, 'InputType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_InputType',
        (['in'], LONG, 'lIndex'),
        (['out'], POINTER(TunerInputType), 'pInputType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_ConnectInput',
        (['in'], LONG, 'lIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_ConnectInput',
        (['out'], POINTER(LONG), 'plIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_VideoFrequency',
        (['out'], POINTER(LONG), 'lFreq'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_AudioFrequency',
        (['out'], POINTER(LONG), 'lFreq'),
    ),
]


IBPCSatelliteTuner._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_DefaultSubChannelTypes',
        (['out'], POINTER(LONG), 'plDefaultVideoType'),
        (['out'], POINTER(LONG), 'plDefaultAudioType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_DefaultSubChannelTypes',
        (['in'], LONG, 'lDefaultVideoType'),
        (['in'], LONG, 'lDefaultAudioType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsTapingPermitted'
    ),
]


class tagTVAudioMode(ENUM):
    AMTVAUDIO_MODE_MONO = 0x1
    AMTVAUDIO_MODE_STEREO = 0x2
    AMTVAUDIO_MODE_LANG_A = 0x10
    AMTVAUDIO_MODE_LANG_B = 0x20
    AMTVAUDIO_MODE_LANG_C = 0x40
    AMTVAUDIO_PRESET_STEREO = 0x200
    AMTVAUDIO_PRESET_LANG_A = 0x1000
    AMTVAUDIO_PRESET_LANG_B = 0x2000
    AMTVAUDIO_PRESET_LANG_C = 0x4000


TVAudioMode = tagTVAudioMode


class tagAMTVAudioEventType(ENUM):
    AMTVAUDIO_EVENT_CHANGED = 0x1


AMTVAudioEventType = tagAMTVAudioEventType


IAMTVAudio._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetHardwareSupportedTVAudioModes',
        (['out'], POINTER(LONG), 'plModes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAvailableTVAudioModes',
        (['out'], POINTER(LONG), 'plModes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_TVAudioMode',
        (['out'], POINTER(LONG), 'plMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_TVAudioMode',
        (['in'], LONG, 'lMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterNotificationCallBack',
        (['in'], POINTER(IAMTunerNotification), 'pNotify'),
        (['in'], LONG, 'lEvents'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnRegisterNotificationCallBack',
        ([], POINTER(IAMTunerNotification), 'pNotify'),
    ),
]


IAMTVAudioNotification._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnEvent',
        (['in'], AMTVAudioEventType, 'Event'),
    ),
]


IAMAnalogVideoEncoder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_AvailableTVFormats',
        (['out'], POINTER(LONG), 'lAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_TVFormat',
        (['in'], LONG, 'lAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_TVFormat',
        (['out'], POINTER(LONG), 'plAnalogVideoStandard'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_CopyProtection',
        (['in'], LONG, 'lVideoCopyProtection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_CopyProtection',
        (['out'], POINTER(LONG), 'lVideoCopyProtection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_CCEnable',
        (['in'], LONG, 'lCCEnable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_CCEnable',
        (['out'], POINTER(LONG), 'lCCEnable'),
    ),
]


class AMPROPERTY_PIN(ENUM):
    AMPROPERTY_PIN_CATEGORY = 0
    AMPROPERTY_PIN_MEDIUM = AMPROPERTY_PIN_CATEGORY + 1



KSPROPERTY_SUPPORT_GET = 0x1
KSPROPERTY_SUPPORT_SET = 0x2
IKsPropertySet._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Set',
        (['in'], REFGUID, 'guidPropSet'),
        (['in'], DWORD, 'dwPropID'),
        (['in'], LPVOID, 'pInstanceData'),
        (['in'], DWORD, 'cbInstanceData'),
        (['in'], LPVOID, 'pPropData'),
        (['in'], DWORD, 'cbPropData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Get',
        (['in'], REFGUID, 'guidPropSet'),
        (['in'], DWORD, 'dwPropID'),
        (['in'], LPVOID, 'pInstanceData'),
        (['in'], DWORD, 'cbInstanceData'),
        ([], LPVOID, 'pPropData'),
        (['in'], DWORD, 'cbPropData'),
        (['out'], POINTER(DWORD), 'pcbReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QuerySupported',
        (['in'], REFGUID, 'guidPropSet'),
        (['in'], DWORD, 'dwPropID'),
        (['out'], POINTER(DWORD), 'pTypeSupport'),
    ),
]


LPMEDIAPROPERTYBAG = POINTER(IMediaPropertyBag)
IMediaPropertyBag._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumProperty',
        (['in'], ULONG, 'iProperty'),
        (['in', 'out'], POINTER(VARIANT), 'pvarPropertyName'),
        (['in', 'out'], POINTER(VARIANT), 'pvarPropertyValue'),
    ),
]


LPPERSISTMEDIAPROPERTYBAG = POINTER(IPersistMediaPropertyBag)
IPersistMediaPropertyBag._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], POINTER(IMediaPropertyBag), 'pPropBag'),
        (['in'], POINTER(IErrorLog), 'pErrorLog'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], POINTER(IMediaPropertyBag), 'pPropBag'),
        (['in'], BOOL, 'fClearDirty'),
        (['in'], BOOL, 'fSaveAllProperties'),
    ),
]


IAMPhysicalPinInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPhysicalType',
        (['out'], POINTER(LONG), 'pType'),
        (['out'], POINTER(LPOLESTR), 'ppszType'),
    ),
]


PAMPHYSICALPININFO = POINTER(IAMPhysicalPinInfo)
IAMExtDevice._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCapability',
        (['in'], LONG, 'Capability'),
        (['out'], POINTER(LONG), 'pValue'),
        (['out'], POINTER(DOUBLE), 'pdblValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_ExternalDeviceID',
        (['out'], POINTER(LPOLESTR), 'ppszData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_ExternalDeviceVersion',
        (['out'], POINTER(LPOLESTR), 'ppszData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_DevicePower',
        (['in'], LONG, 'PowerMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_DevicePower',
        (['out'], POINTER(LONG), 'pPowerMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Calibrate',
        (['in'], HEVENT, 'hEvent'),
        (['in'], LONG, 'Mode'),
        (['out'], POINTER(LONG), 'pStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_DevicePort',
        (['in'], LONG, 'DevicePort'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_DevicePort',
        (['out'], POINTER(LONG), 'pDevicePort'),
    ),
]


PEXTDEVICE = POINTER(IAMExtDevice)
IAMExtTransport._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCapability',
        (['in'], LONG, 'Capability'),
        (['out'], POINTER(LONG), 'pValue'),
        (['out'], POINTER(DOUBLE), 'pdblValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_MediaState',
        (['in'], LONG, 'State'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_MediaState',
        (['out'], POINTER(LONG), 'pState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_LocalControl',
        (['in'], LONG, 'State'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_LocalControl',
        (['out'], POINTER(LONG), 'pState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStatus',
        (['in'], LONG, 'StatusItem'),
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTransportBasicParameters',
        (['in'], LONG, 'Param'),
        (['in', 'out'], POINTER(LONG), 'pValue'),
        (['in', 'out'], POINTER(LPOLESTR), 'ppszData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTransportBasicParameters',
        (['in'], LONG, 'Param'),
        (['in'], LONG, 'Value'),
        (['in'], LPCOLESTR, 'pszData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTransportVideoParameters',
        (['in'], LONG, 'Param'),
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTransportVideoParameters',
        (['in'], LONG, 'Param'),
        (['in'], LONG, 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTransportAudioParameters',
        (['in'], LONG, 'Param'),
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTransportAudioParameters',
        (['in'], LONG, 'Param'),
        (['in'], LONG, 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Mode',
        (['in'], LONG, 'Mode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Mode',
        (['out'], POINTER(LONG), 'pMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_Rate',
        (['in'], DOUBLE, 'dblRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_Rate',
        (['out'], POINTER(DOUBLE), 'pdblRate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetChase',
        (['out'], POINTER(LONG), 'pEnabled'),
        (['out'], POINTER(LONG), 'pOffset'),
        (['out'], POINTER(HEVENT), 'phEvent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetChase',
        (['in'], LONG, 'Enable'),
        (['in'], LONG, 'Offset'),
        (['in'], HEVENT, 'hEvent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBump',
        (['out'], POINTER(LONG), 'pSpeed'),
        (['out'], POINTER(LONG), 'pDuration'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBump',
        (['in'], LONG, 'Speed'),
        (['in'], LONG, 'Duration'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_AntiClogControl',
        (['out'], POINTER(LONG), 'pEnabled'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_AntiClogControl',
        (['in'], LONG, 'Enable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetEditPropertySet',
        (['in'], LONG, 'EditID'),
        (['out'], POINTER(LONG), 'pState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetEditPropertySet',
        (['in', 'out'], POINTER(LONG), 'pEditID'),
        (['in'], LONG, 'State'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetEditProperty',
        (['in'], LONG, 'EditID'),
        (['in'], LONG, 'Param'),
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetEditProperty',
        (['in'], LONG, 'EditID'),
        (['in'], LONG, 'Param'),
        (['in'], LONG, 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_EditStart',
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_EditStart',
        (['in'], LONG, 'Value'),
    ),
]


PIAMEXTTRANSPORT = POINTER(IAMExtTransport)

class tagTIMECODE(ctypes.Structure):
    _fields_ = [
        ('wFrameRate', WORD),
        ('wFrameFract', WORD),
        ('dwFrames', DWORD),
    ]


TIMECODE = tagTIMECODE


class tagTIMECODE_SAMPLE(ctypes.Structure):
    _fields_ = [
        ('qwTick', LONGLONG),
        ('timecode', TIMECODE),
        ('dwUser', DWORD),
        ('dwFlags', DWORD),
    ]


TIMECODE_SAMPLE = tagTIMECODE_SAMPLE


PTIMECODE = POINTER(TIMECODE)
PTIMECODE_SAMPLE = POINTER(TIMECODE_SAMPLE)
IAMTimecodeReader._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTCRMode',
        (['in'], LONG, 'Param'),
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTCRMode',
        (['in'], LONG, 'Param'),
        (['in'], LONG, 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_VITCLine',
        (['in'], LONG, 'Line'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_VITCLine',
        (['out'], POINTER(LONG), 'pLine'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTimecode',
        (['out'], PTIMECODE_SAMPLE, 'pTimecodeSample'),
    ),
]


PIAMTIMECODEREADER = POINTER(IAMTimecodeReader)
IAMTimecodeGenerator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTCGMode',
        (['in'], LONG, 'Param'),
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTCGMode',
        (['in'], LONG, 'Param'),
        (['in'], LONG, 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_VITCLine',
        (['in'], LONG, 'Line'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'get_VITCLine',
        (['out'], POINTER(LONG), 'pLine'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTimecode',
        (['in'], PTIMECODE_SAMPLE, 'pTimecodeSample'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTimecode',
        (['out'], PTIMECODE_SAMPLE, 'pTimecodeSample'),
    ),
]


PIAMTIMECODEGENERATOR = POINTER(IAMTimecodeGenerator)
IAMTimecodeDisplay._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTCDisplayEnable',
        (['out'], POINTER(LONG), 'pState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTCDisplayEnable',
        (['in'], LONG, 'State'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTCDisplay',
        (['in'], LONG, 'Param'),
        (['out'], POINTER(LONG), 'pValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTCDisplay',
        (['in'], LONG, 'Param'),
        (['in'], LONG, 'Value'),
    ),
]


PIAMTIMECODEDISPLAY = POINTER(IAMTimecodeDisplay)
IAMDevMemoryAllocator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetInfo',
        (['out'], POINTER(DWORD), 'pdwcbTotalFree'),
        (['out'], POINTER(DWORD), 'pdwcbLargestFree'),
        (['out'], POINTER(DWORD), 'pdwcbTotalMemory'),
        (['out'], POINTER(DWORD), 'pdwcbMinimumChunk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CheckMemory',
        (['in'], POINTER(BYTE), 'pBuffer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Alloc',
        (['out'], POINTER(POINTER(BYTE)), 'ppBuffer'),
        (['in', 'out'], POINTER(DWORD), 'pdwcbBuffer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Free',
        (['in'], POINTER(BYTE), 'pBuffer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDevMemoryObject',
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppUnkInnner'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
    ),
]


PAMDEVMEMORYALLOCATOR = POINTER(IAMDevMemoryAllocator)
IAMDevMemoryControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDevId',
        (['out'], POINTER(DWORD), 'pdwDevId'),
    ),
]


PAMDEVMEMORYCONTROL = POINTER(IAMDevMemoryControl)
IAMStreamSelect._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Count',
        (['out'], POINTER(DWORD), 'pcStreams'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Info',
        (['in'], LONG, 'lIndex'),
        (['out'], POINTER(POINTER(AM_MEDIA_TYPE)), 'ppmt'),
        (['out'], POINTER(DWORD), 'pdwFlags'),
        (['out'], POINTER(LCID), 'plcid'),
        (['out'], POINTER(DWORD), 'pdwGroup'),
        (['out'], POINTER(LPWSTR), 'ppszName'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppObject'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppUnk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Enable',
        (['in'], LONG, 'lIndex'),
        (['in'], DWORD, 'dwFlags'),
    ),
]


PAMSTREAMSELECT = POINTER(IAMStreamSelect)
IAMResourceControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Reserve',
        (['in'], DWORD, 'dwFlags'),
        (['in'], PVOID, 'pvReserved'),
    ),
]


IAMClockAdjust._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetClockDelta',
        (['in'], REFERENCE_TIME, 'rtDelta'),
    ),
]


IAMFilterMiscFlags._methods_ = [
    COMMETHOD(
        [],
        ULONG,
        'GetMiscFlags'
    ),
]


IDrawVideoImage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DrawVideoImageDraw',
        (['in'], HDC, 'hdc'),
        (['in'], LPRECT, 'lprcSrc'),
        (['in'], LPRECT, 'lprcDst'),
    ),
]


IDecimateVideoImage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetDecimationImageSize',
        (['in'], LONG, 'lWidth'),
        (['in'], LONG, 'lHeight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ResetDecimationImageSize'
    ),
]


class _DECIMATION_USAGE(ENUM):
    DECIMATION_LEGACY = 0
    DECIMATION_USE_DECODER_ONLY = DECIMATION_LEGACY + 1
    DECIMATION_USE_VIDEOPORT_ONLY = DECIMATION_USE_DECODER_ONLY + 1
    DECIMATION_USE_OVERLAY_ONLY = DECIMATION_USE_VIDEOPORT_ONLY + 1
    DECIMATION_DEFAULT = DECIMATION_USE_OVERLAY_ONLY + 1


DECIMATION_USAGE = _DECIMATION_USAGE


IAMVideoDecimationProperties._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryDecimationUsage',
        (['out'], POINTER(DECIMATION_USAGE), 'lpUsage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDecimationUsage',
        (['in'], DECIMATION_USAGE, 'Usage'),
    ),
]


IVideoFrameStep._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Step',
        ([], DWORD, 'dwFrames'),
        ([], POINTER(comtypes.IUnknown), 'pStepObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CanStep',
        ([], LONG, 'bMultiple'),
        ([], POINTER(comtypes.IUnknown), 'pStepObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CancelStep'
    ),
]


IAMLatency._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetLatency',
        (['in'], POINTER(REFERENCE_TIME), 'prtLatency'),
    ),
]


IAMPushSource._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPushSourceFlags',
        (['out'], POINTER(ULONG), 'pFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPushSourceFlags',
        (['in'], ULONG, 'Flags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetStreamOffset',
        (['in'], REFERENCE_TIME, 'rtOffset'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStreamOffset',
        (['out'], POINTER(REFERENCE_TIME), 'prtOffset'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMaxStreamOffset',
        (['out'], POINTER(REFERENCE_TIME), 'prtMaxOffset'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMaxStreamOffset',
        (['in'], REFERENCE_TIME, 'rtMaxOffset'),
    ),
]


IAMDeviceRemoval._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DeviceInfo',
        (['out'], POINTER(CLSID), 'pclsidInterfaceClass'),
        (['out'], POINTER(LPWSTR), 'pwszSymbolicLink'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Disassociate'
    ),
]



class DVINFO(ctypes.Structure):
    _fields_ = [
        ('dwDVAAuxSrc', DWORD),
        ('dwDVAAuxCtl', DWORD),
        ('dwDVAAuxSrc1', DWORD),
        ('dwDVAAuxCtl1', DWORD),
        ('dwDVVAuxSrc', DWORD),
        ('dwDVVAuxCtl', DWORD),
        ('dwDVReserved', DWORD * 2),
    ]



PDVINFO = POINTER(DVINFO)


IDVEnc._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_IFormatResolution',
        (['out'], POINTER(INT), 'VideoFormat'),
        (['out'], POINTER(INT), 'DVFormat'),
        (['out'], POINTER(INT), 'Resolution'),
        (['in'], BYTE, 'fDVInfo'),
        (['out'], POINTER(DVINFO), 'sDVInfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_IFormatResolution',
        (['in'], INT, 'VideoFormat'),
        (['in'], INT, 'DVFormat'),
        (['in'], INT, 'Resolution'),
        (['in'], BYTE, 'fDVInfo'),
        (['in'], POINTER(DVINFO), 'sDVInfo'),
    ),
]


IIPDVDec._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'get_IPDisplay',
        (['out'], POINTER(INT), 'displayPix'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'put_IPDisplay',
        (['in'], INT, 'displayPix'),
    ),
]


IDVRGB219._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetRGB219',
        (['in'], BOOL, 'bState'),
    ),
]


IDVSplitter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DiscardAlternateVideoFrames',
        (['in'], INT, 'nDiscard'),
    ),
]


IAMAudioRendererStats._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetStatParam',
        (['in'], DWORD, 'dwParam'),
        (['out'], POINTER(DWORD), 'pdwParam1'),
        (['out'], POINTER(DWORD), 'pdwParam2'),
    ),
]


IAMGraphStreams._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'FindUpstreamInterface',
        (['in'], POINTER(IPin), 'pPin'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvInterface'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SyncUsingStreamOffset',
        (['in'], BOOL, 'bUseStreamOffset'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMaxGraphLatency',
        (['in'], REFERENCE_TIME, 'rtMaxGraphLatency'),
    ),
]


IAMOverlayFX._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryOverlayFXCaps',
        (['out'], POINTER(DWORD), 'lpdwOverlayFXCaps'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetOverlayFX',
        (['in'], DWORD, 'dwOverlayFX'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetOverlayFX',
        (['out'], POINTER(DWORD), 'lpdwOverlayFX'),
    ),
]


IAMOpenProgress._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryProgress',
        (['out'], POINTER(LONGLONG), 'pllTotal'),
        (['out'], POINTER(LONGLONG), 'pllCurrent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AbortOperation'
    ),
]


IMpeg2Demultiplexer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateOutputPin',
        (['in'], POINTER(AM_MEDIA_TYPE), 'pMediaType'),
        (['in'], LPWSTR, 'pszPinName'),
        (['out'], POINTER(POINTER(IPin)), 'ppIPin'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetOutputPinMediaType',
        (['in'], LPWSTR, 'pszPinName'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pMediaType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DeleteOutputPin',
        (['in'], LPWSTR, 'pszPinName'),
    ),
]


MPEG2_PROGRAM_STREAM_MAP = 0x00000000
MPEG2_PROGRAM_ELEMENTARY_STREAM = 0x00000001
MPEG2_PROGRAM_DIRECTORY_PES_PACKET = 0x00000002
MPEG2_PROGRAM_PACK_HEADER = 0x00000003
MPEG2_PROGRAM_PES_STREAM = 0x00000004
MPEG2_PROGRAM_SYSTEM_HEADER = 0x00000005
SUBSTREAM_FILTER_VAL_NONE = 0x10000000

class STREAM_ID_MAP(ctypes.Structure):
    _fields_ = [
        ('stream_id', ULONG),
        ('dwMediaSampleContent', DWORD),
        ('ulSubstreamFilterValue', ULONG),
        ('iDataOffset', INT),
    ]



IEnumStreamIdMap._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'cRequest'),
        ([], POINTER(STREAM_ID_MAP), 'pStreamIdMap'),
        (['out'], POINTER(ULONG), 'pcReceived'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'cRecords'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumStreamIdMap)), 'ppIEnumStreamIdMap'),
    ),
]


IMPEG2StreamIdMap._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'MapStreamId',
        (['in'], ULONG, 'ulStreamId'),
        (['in'], DWORD, 'MediaSampleContent'),
        (['in'], ULONG, 'ulSubstreamFilterValue'),
        (['in'], INT, 'iDataOffset'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnmapStreamId',
        (['in'], ULONG, 'culStreamId'),
        (['in'], POINTER(ULONG), 'pulStreamId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumStreamIdMap',
        (['out'], POINTER(POINTER(IEnumStreamIdMap)), 'ppIEnumStreamIdMap'),
    ),
]


IRegisterServiceProvider._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RegisterService',
        (['in'], REFGUID, 'guidService'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkObject'),
    ),
]


IAMClockSlave._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetErrorTolerance',
        (['in'], DWORD, 'dwTolerance'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetErrorTolerance',
        (['out'], POINTER(DWORD), 'pdwTolerance'),
    ),
]


IID_IAMGraphBuilderCallback = IID(
    '{4995f511-9ddb-4f12-bd3b-f04611807b79}'
)


class IAMFilterGraphBuilderCallback(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMGraphBuilderCallback
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            HRESULT,
            'SelectedFilter',
            (['in'], POINTER(IMoniker), 'pMon'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'CreatedFilter',
            (['in'], POINTER(IBaseFilter), 'pFil'),
        ),
        COMMETHOD(
            [],
            HRESULT,
            'UnableToRender',
            ([], POINTER(IPin), 'pPin'),
        ),
    ]


IID_IAMFilterGraphCallback = EXTERN_GUID(
    0x56A868FD,
    0x0AD4,
    0x11CE,
    0xB0,
    0xA3,
    0x0,
    0x20,
    0xAF,
    0x0B,
    0xA7,
    0x70
)


class IAMFilterGraphCallback(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAMFilterGraphCallback
    _idlflags_ = []
    _methods_ = [

        COMMETHOD(
            [],
            HRESULT,
            'UnableToRender',
            ([], POINTER(IPin), 'pPin'),
        ),
    ]


IGetCapabilitiesKey._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCapabilitiesKey',
        (['out'], POINTER(HKEY), 'pHKey'),
    ),
]


IEncoderAPI._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'IsSupported',
        (['in'], POINTER(GUID), 'Api'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsAvailable',
        (['in'], POINTER(GUID), 'Api'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParameterRange',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(VARIANT), 'ValueMin'),
        (['out'], POINTER(VARIANT), 'ValueMax'),
        (['out'], POINTER(VARIANT), 'SteppingDelta'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParameterValues',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(POINTER(VARIANT)), 'Values'),
        (['out'], POINTER(ULONG), 'ValuesCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultValue',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(VARIANT), 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetValue',
        (['in'], POINTER(GUID), 'Api'),
        (['out'], POINTER(VARIANT), 'Value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetValue',
        (['in'], POINTER(GUID), 'Api'),
        (['in'], POINTER(VARIANT), 'Value'),
    ),
]


class VIDEOENCODER_BITRATE_MODE(ENUM):
    ConstantBitRate = 0
    VariableBitRateAverage = ConstantBitRate + 1
    VariableBitRatePeak = VariableBitRateAverage + 1



AM_GETDECODERCAP_QUERY_VMR_SUPPORT = 0x00000001
VMR_NOTSUPPORTED = 0x00000000
VMR_SUPPORTED = 0x00000001
AM_QUERY_DECODER_VMR_SUPPORT = 0x00000001
AM_QUERY_DECODER_DXVA_1_SUPPORT = 0x00000002
AM_QUERY_DECODER_DVD_SUPPORT = 0x00000003
AM_QUERY_DECODER_ATSC_SD_SUPPORT = 0x00000004
AM_QUERY_DECODER_ATSC_HD_SUPPORT = 0x00000005
AM_GETDECODERCAP_QUERY_VMR9_SUPPORT = 0x00000006
AM_GETDECODERCAP_QUERY_EVR_SUPPORT = 0x00000007
DECODER_CAP_NOTSUPPORTED = 0x00000000
DECODER_CAP_SUPPORTED = 0x00000001
IAMDecoderCaps._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDecoderCaps',
        (['in'], DWORD, 'dwCapIndex'),
        (['out'], POINTER(DWORD), 'lpdwCap'),
    ),
]



class _AMCOPPSignature(ctypes.Structure):
    _fields_ = [
        ('Signature', BYTE * 256),
    ]


AMCOPPSignature = _AMCOPPSignature



class _AMCOPPCommand(ctypes.Structure):
    _fields_ = [
        ('macKDI', GUID),
        ('guidCommandID', GUID),
        ('dwSequence', DWORD),
        ('cbSizeData', DWORD),
        ('CommandData', BYTE * 4056),
    ]


AMCOPPCommand = _AMCOPPCommand


LPAMCOPPCommand = POINTER(_AMCOPPCommand)



class _AMCOPPStatusInput(ctypes.Structure):
    _fields_ = [
        ('rApp', GUID),
        ('guidStatusRequestID', GUID),
        ('dwSequence', DWORD),
        ('cbSizeData', DWORD),
        ('StatusData', BYTE * 4056),
    ]


AMCOPPStatusInput = _AMCOPPStatusInput


LPAMCOPPStatusInput = POINTER(_AMCOPPStatusInput)



class _AMCOPPStatusOutput(ctypes.Structure):
    _fields_ = [
        ('macKDI', GUID),
        ('cbSizeData', DWORD),
        ('COPPStatus', BYTE * 4076),
    ]


AMCOPPStatusOutput = _AMCOPPStatusOutput


LPAMCOPPStatusOutput = POINTER(_AMCOPPStatusOutput)


IAMCertifiedOutputProtection._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'KeyExchange',
        (['out'], POINTER(GUID), 'pRandom'),
        (['out'], POINTER(POINTER(BYTE)), 'VarLenCertGH'),
        (['out'], POINTER(DWORD), 'pdwLengthCertGH'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SessionSequenceStart',
        (['in'], POINTER(AMCOPPSignature), 'pSig'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ProtectionCommand',
        (['in'], POINTER(AMCOPPCommand), 'cmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ProtectionStatus',
        (['in'], POINTER(AMCOPPStatusInput), 'pStatusInput'),
        (['out'], POINTER(AMCOPPStatusOutput), 'pStatusOutput'),
    ),
]


IAMAsyncReaderTimestampScaling._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTimestampMode',
        ([], POINTER(BOOL), 'pfRaw'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTimestampMode',
        ([], BOOL, 'fRaw'),
    ),
]


IAMPluginControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPreferredClsid',
        ([], REFGUID, 'subType'),
        ([], POINTER(CLSID), 'clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPreferredClsidByIndex',
        ([], DWORD, 'index'),
        ([], POINTER(GUID), 'subType'),
        ([], POINTER(CLSID), 'clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetPreferredClsid',
        ([], REFGUID, 'subType'),
        ([], POINTER(CLSID), 'clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsDisabled',
        ([], REFCLSID, 'clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDisabledByIndex',
        ([], DWORD, 'index'),
        ([], POINTER(CLSID), 'clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDisabled',
        ([], REFCLSID, 'clsid'),
        ([], BOOL, 'disabled'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsLegacyDisabled',
        ([], LPCWSTR, 'dllName'),
    ),
]


from .winapifamily_h import * # NOQA
IPinConnection._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DynamicQueryAccept',
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyEndOfStream',
        (['in'], HANDLE, 'hNotifyEvent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DynamicDisconnect'
    ),
]


IPinFlowControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Block',
        (['in'], DWORD, 'dwBlockFlags'),
        (['in'], HANDLE, 'hEvent'),
    ),
]


class _AM_GRAPH_CONFIG_RECONNECT_FLAGS(ENUM):
    AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT = 0x1
    AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS = 0x2
    AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS = 0x4


AM_GRAPH_CONFIG_RECONNECT_FLAGS = _AM_GRAPH_CONFIG_RECONNECT_FLAGS


class _AM_FILTER_FLAGS(ENUM):
    AM_FILTER_FLAGS_REMOVABLE = 0x1


AM_FILTER_FLAGS = _AM_FILTER_FLAGS


IGraphConfig._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Reconnect',
        (['in'], POINTER(IPin), 'pOutputPin'),
        (['in'], POINTER(IPin), 'pInputPin'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmtFirstConnection'),
        (['in'], POINTER(IBaseFilter), 'pUsingFilter'),
        (['in'], HANDLE, 'hAbortEvent'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Reconfigure',
        (['in'], POINTER(IGraphConfigCallback), 'pCallback'),
        (['in'], PVOID, 'pvContext'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], HANDLE, 'hAbortEvent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddFilterToCache',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumCacheFilter',
        (['out'], POINTER(POINTER(IEnumFilters)), 'pEnum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveFilterFromCache',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStartTime',
        (['out'], POINTER(REFERENCE_TIME), 'prtStart'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PushThroughData',
        (['in'], POINTER(IPin), 'pOutputPin'),
        (['in'], POINTER(IPinConnection), 'pConnection'),
        (['in'], HANDLE, 'hEventAbort'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFilterFlags',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
        (['in'], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFilterFlags',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
        (['out'], POINTER(DWORD), 'pdwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveFilterEx',
        (['in'], POINTER(IBaseFilter), 'pFilter'),
        ([], DWORD, 'Flags'),
    ),
]


IGraphConfigCallback._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Reconfigure',
        ([], PVOID, 'pvContext'),
        ([], DWORD, 'dwFlags'),
    ),
]


IFilterChain._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StartChain',
        (['in'], POINTER(IBaseFilter), 'pStartFilter'),
        (['in'], POINTER(IBaseFilter), 'pEndFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PauseChain',
        (['in'], POINTER(IBaseFilter), 'pStartFilter'),
        (['in'], POINTER(IBaseFilter), 'pEndFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'StopChain',
        (['in'], POINTER(IBaseFilter), 'pStartFilter'),
        (['in'], POINTER(IBaseFilter), 'pEndFilter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveChain',
        (['in'], POINTER(IBaseFilter), 'pStartFilter'),
        (['in'], POINTER(IBaseFilter), 'pEndFilter'),
    ),
]


LPDIRECTDRAW7 = POINTER(DWORD)
LPDIRECTDRAWSURFACE7 = POINTER(DWORD)
LPDDPIXELFORMAT = POINTER(DWORD)
LPBITMAPINFOHEADER = POINTER(DWORD)

class DDCOLORKEY(ctypes.Structure):
    _fields_ = [
        ('dw1', DWORD),
        ('dw2', DWORD),
    ]


LPDDCOLORKEY = POINTER(DDCOLORKEY)

from .ddraw_h import * # NOQA


class VMRPresentationFlags(ENUM):
    VMRSample_SyncPoINT = 0x1
    VMRSample_Preroll = 0x2
    VMRSample_Discontinuity = 0x4
    VMRSample_TimeValid = 0x8
    VMRSample_SrcDstRectsValid = 0x10


class tagVMRPRESENTATIONINFO(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('lpSurf', LPDIRECTDRAWSURFACE7),
        ('rtStart', REFERENCE_TIME),
        ('rtEnd', REFERENCE_TIME),
        ('szAspectRatio', SIZE),
        ('rcSrc', RECT),
        ('rcDst', RECT),
        ('dwTypeSpecificFlags', DWORD),
        ('dwInterlaceFlags', DWORD),
    ]


VMRPRESENTATIONINFO = tagVMRPRESENTATIONINFO


IVMRImagePresenter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StartPresenting',
        (['in'], DWORD_PTR, 'dwUserID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'StopPresenting',
        (['in'], DWORD_PTR, 'dwUserID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PresentImage',
        (['in'], DWORD_PTR, 'dwUserID'),
        (['in'], POINTER(VMRPRESENTATIONINFO), 'lpPresInfo'),
    ),
]


class VMRSurfaceAllocationFlags(ENUM):
    AMAP_PIXELFORMAT_VALID = 0x1
    AMAP_3D_TARGET = 0x2
    AMAP_ALLOW_SYSMEM = 0x4
    AMAP_FORCE_SYSMEM = 0x8
    AMAP_DIRECTED_FLIP = 0x10
    AMAP_DXVA_TARGET = 0x20


class tagVMRALLOCATIONINFO(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('lpHdr', LPBITMAPINFOHEADER),
        ('lpPixFmt', LPDDPIXELFORMAT),
        ('szAspectRatio', SIZE),
        ('dwMinBuffers', DWORD),
        ('dwMaxBuffers', DWORD),
        ('dwInterlaceFlags', DWORD),
        ('szNativeSize', SIZE),
    ]


VMRALLOCATIONINFO = tagVMRALLOCATIONINFO


IVMRSurfaceAllocator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AllocateSurface',
        (['in'], DWORD_PTR, 'dwUserID'),
        (['in'], POINTER(VMRALLOCATIONINFO), 'lpAllocInfo'),
        (['in', 'out'], POINTER(DWORD), 'lpdwActualBuffers'),
        (['out'], POINTER(LPDIRECTDRAWSURFACE7), 'lplpSurface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FreeSurface',
        (['in'], DWORD_PTR, 'dwID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PrepareSurface',
        (['in'], DWORD_PTR, 'dwUserID'),
        (['in'], LPDIRECTDRAWSURFACE7, 'lpSurface'),
        (['in'], DWORD, 'dwSurfaceFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AdviseNotify',
        (['in'], POINTER(IVMRSurfaceAllocatorNotify), 'lpIVMRSurfAllocNotify'),
    ),
]


IVMRSurfaceAllocatorNotify._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AdviseSurfaceAllocator',
        (['in'], DWORD_PTR, 'dwUserID'),
        (['in'], POINTER(IVMRSurfaceAllocator), 'lpIVRMSurfaceAllocator'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDDrawDevice',
        (['in'], LPDIRECTDRAW7, 'lpDDrawDevice'),
        (['in'], HMONITOR, 'hMonitor'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ChangeDDrawDevice',
        (['in'], LPDIRECTDRAW7, 'lpDDrawDevice'),
        (['in'], HMONITOR, 'hMonitor'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyEvent',
        (['in'], LONG, 'EventCode'),
        (['in'], LONG_PTR, 'Param1'),
        (['in'], LONG_PTR, 'Param2'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBorderColor',
        (['in'], COLORREF, 'clrBorder'),
    ),
]


class VMR_ASPECT_RATIO_MODE(ENUM):
    VMR_ARMODE_NONE = 0
    VMR_ARMODE_LETTER_BOX = VMR_ARMODE_NONE + 1


IVMRWindowlessControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetNativeVideoSize',
        (['out'], POINTER(LONG), 'lpWidth'),
        (['out'], POINTER(LONG), 'lpHeight'),
        (['out'], POINTER(LONG), 'lpARWidth'),
        (['out'], POINTER(LONG), 'lpARHeight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMinIdealVideoSize',
        (['out'], POINTER(LONG), 'lpWidth'),
        (['out'], POINTER(LONG), 'lpHeight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMaxIdealVideoSize',
        (['out'], POINTER(LONG), 'lpWidth'),
        (['out'], POINTER(LONG), 'lpHeight'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVideoPosition',
        (['in'], LPRECT, 'lpSRCRect'),
        (['in'], LPRECT, 'lpDSTRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVideoPosition',
        (['out'], LPRECT, 'lpSRCRect'),
        (['out'], LPRECT, 'lpDSTRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAspectRatioMode',
        (['out'], POINTER(DWORD), 'lpAspectRatioMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAspectRatioMode',
        (['in'], DWORD, 'AspectRatioMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetVideoClippingWindow',
        (['in'], HWND, 'hwnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RepaINTVideo',
        (['in'], HWND, 'hwnd'),
        (['in'], HDC, 'hdc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentImage',
        (['out'], POINTER(POINTER(BYTE)), 'lpDib'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBorderColor',
        (['in'], COLORREF, 'Clr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBorderColor',
        (['out'], POINTER(COLORREF), 'lpClr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetColorKey',
        (['in'], COLORREF, 'Clr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetColorKey',
        (['out'], POINTER(COLORREF), 'lpClr'),
    ),
]


class VMRMixerPrefs(ENUM):
    MixerPref_NoDecimation = 0x1
    MixerPref_DecimateOutput = 0x2
    MixerPref_ARAdjustXorY = 0x4
    MixerPref_DecimationReserved = 0x8
    MixerPref_DecimateMask = 0xF
    MixerPref_BiLinearFiltering = 0x10
    MixerPref_PoINTFiltering = 0x20
    MixerPref_FilteringMask = 0xF0
    MixerPref_RenderTargetRGB = 0x100
    MixerPref_RenderTargetYUV = 0x1000
    MixerPref_RenderTargetYUV420 = 0x200
    MixerPref_RenderTargetYUV422 = 0x400
    MixerPref_RenderTargetYUV444 = 0x800
    MixerPref_RenderTargetReserved = 0xE000
    MixerPref_RenderTargetMask = 0xFF00
    MixerPref_DynamicSwitchToBOB = 0x10000
    MixerPref_DynamicDecimateBy2 = 0x20000
    MixerPref_DynamicReserved = 0xC0000
    MixerPref_DynamicMask = 0xF0000


class _NORMALIZEDRECT(ctypes.Structure):
    _fields_ = [
        ('left', FLOAT),
        ('top', FLOAT),
        ('right', FLOAT),
        ('bottom', FLOAT),
    ]


NORMALIZEDRECT = _NORMALIZEDRECT


PNORMALIZEDRECT = POINTER(_NORMALIZEDRECT)


IVMRMixerControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetAlpha',
        (['in'], DWORD, 'dwStreamID'),
        (['in'], FLOAT, 'Alpha'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAlpha',
        (['in'], DWORD, 'dwStreamID'),
        (['out'], POINTER(FLOAT), 'pAlpha'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetZOrder',
        (['in'], DWORD, 'dwStreamID'),
        (['in'], DWORD, 'dwZ'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetZOrder',
        (['in'], DWORD, 'dwStreamID'),
        (['out'], POINTER(DWORD), 'pZ'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetOutputRect',
        (['in'], DWORD, 'dwStreamID'),
        (['in'], POINTER(NORMALIZEDRECT), 'pRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetOutputRect',
        (['in'], DWORD, 'dwStreamID'),
        (['out'], POINTER(NORMALIZEDRECT), 'pRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBackgroundClr',
        (['in'], COLORREF, 'ClrBkg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBackgroundClr',
        (['in'], POINTER(COLORREF), 'lpClrBkg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetMixingPrefs',
        (['in'], DWORD, 'dwMixerPrefs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMixingPrefs',
        (['out'], POINTER(DWORD), 'pdwMixerPrefs'),
    ),
]



class tagVMRGUID(ctypes.Structure):
    _fields_ = [
        ('pGUID', POINTER(GUID)),
        ('GUID', GUID),
    ]


VMRGUID = tagVMRGUID



class tagVMRMONITORINFO(ctypes.Structure):
    _fields_ = [
        ('guid', VMRGUID),
        ('rcMonitor', RECT),
        ('hMon', HMONITOR),
        ('dwFlags', DWORD),
        ('szDevice', WCHAR * 32),
        ('szDescription', WCHAR * 256),
        ('liDriverVersion', LARGE_INTEGER),
        ('dwVendorId', DWORD),
        ('dwDeviceId', DWORD),
        ('dwSubSysId', DWORD),
        ('dwRevision', DWORD),
    ]


VMRMONITORINFO = tagVMRMONITORINFO


IVMRMonitorConfig._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetMonitor',
        (['in'], POINTER(VMRGUID), 'pGUID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMonitor',
        (['out'], POINTER(VMRGUID), 'pGUID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultMonitor',
        (['in'], POINTER(VMRGUID), 'pGUID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultMonitor',
        (['out'], POINTER(VMRGUID), 'pGUID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAvailableMonitors',
        (['out'], POINTER(VMRMONITORINFO), 'pInfo'),
        (['in'], DWORD, 'dwMaxInfoArraySize'),
        (['out'], POINTER(DWORD), 'pdwNumDevices'),
    ),
]


class VMRRenderPrefs(ENUM):
    RenderPrefs_RestrictToInitialMonitor = 0
    RenderPrefs_ForceOffscreen = 0x1
    RenderPrefs_ForceOverlays = 0x2
    RenderPrefs_AllowOverlays = 0
    RenderPrefs_AllowOffscreen = 0
    RenderPrefs_DoNotRenderColorKeyAndBorder = 0x8
    RenderPrefs_Reserved = 0x10
    RenderPrefs_PreferAGPMemWhenMixing = 0x20
    RenderPrefs_Mask = 0x3F



class VMRMode(ENUM):
    VMRMode_Windowed = 0x1
    VMRMode_Windowless = 0x2
    VMRMode_Renderless = 0x4
    VMRMode_Mask = 0x7


class __MIDL___MIDL_itf_strmif_0000_0122_0001(ENUM):
    MAX_NUMBER_OF_STREAMS = 16


IVMRFilterConfig._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetImageCompositor',
        (['in'], POINTER(IVMRImageCompositor), 'lpVMRImgCompositor'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetNumberOfStreams',
        (['in'], DWORD, 'dwMaxStreams'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNumberOfStreams',
        (['out'], POINTER(DWORD), 'pdwMaxStreams'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetRenderingPrefs',
        (['in'], DWORD, 'dwRenderFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRenderingPrefs',
        (['out'], POINTER(DWORD), 'pdwRenderFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetRenderingMode',
        (['in'], DWORD, 'Mode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRenderingMode',
        (['out'], POINTER(DWORD), 'pMode'),
    ),
]


IVMRAspectRatioControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetAspectRatioMode',
        (['out'], LPDWORD, 'lpdwARMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetAspectRatioMode',
        (['in'], DWORD, 'dwARMode'),
    ),
]


class VMRDeINTerlacePrefs(ENUM):
    DeINTerlacePref_NextBest = 0x1
    DeINTerlacePref_BOB = 0x2
    DeINTerlacePref_Weave = 0x4
    DeINTerlacePref_Mask = 0x7



class VMRDeINTerlaceTech(ENUM):
    DeINTerlaceTech_Unknown = 0
    DeINTerlaceTech_BOBLineReplicate = 0x1
    DeINTerlaceTech_BOBVerticalStretch = 0x2
    DeINTerlaceTech_MedianFiltering = 0x4
    DeINTerlaceTech_EdgeFiltering = 0x10
    DeINTerlaceTech_FieldAdaptive = 0x20
    DeINTerlaceTech_PixelAdaptive = 0x40
    DeINTerlaceTech_MotionVectorSteered = 0x80




class _VMRFrequency(ctypes.Structure):
    _fields_ = [
        ('dwNumerator', DWORD),
        ('dwDenominator', DWORD),
    ]


VMRFrequency = _VMRFrequency



class _VMRVideoDesc(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwSampleWidth', DWORD),
        ('dwSampleHeight', DWORD),
        ('SingleFieldPerSample', BOOL),
        ('dwFourCC', DWORD),
        ('InputSampleFreq', VMRFrequency),
        ('OutputFrameFreq', VMRFrequency),
    ]


VMRVideoDesc = _VMRVideoDesc



class _VMRDeINTerlaceCaps(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwNumPreviousOutputFrames', DWORD),
        ('dwNumForwardRefSamples', DWORD),
        ('dwNumBackwardRefSamples', DWORD),
        ('DeINTerlaceTechnology', VMRDeINTerlaceTech),
    ]


VMRDeINTerlaceCaps = _VMRDeINTerlaceCaps


IVMRDeINTerlaceControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetNumberOfDeINTerlaceModes',
        (['in'], POINTER(VMRVideoDesc), 'lpVideoDescription'),
        (['in', 'out'], LPDWORD, 'lpdwNumDeINTerlaceModes'),
        (['out'], LPGUID, 'lpDeINTerlaceModes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDeINTerlaceModeCaps',
        (['in'], LPGUID, 'lpDeINTerlaceMode'),
        (['in'], POINTER(VMRVideoDesc), 'lpVideoDescription'),
        (['in', 'out'], POINTER(VMRDeINTerlaceCaps), 'lpDeINTerlaceCaps'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDeINTerlaceMode',
        (['in'], DWORD, 'dwStreamID'),
        (['out'], LPGUID, 'lpDeINTerlaceMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDeINTerlaceMode',
        (['in'], DWORD, 'dwStreamID'),
        (['in'], LPGUID, 'lpDeINTerlaceMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDeINTerlacePrefs',
        (['out'], LPDWORD, 'lpdwDeINTerlacePrefs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDeINTerlacePrefs',
        (['in'], DWORD, 'dwDeINTerlacePrefs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetActualDeINTerlaceMode',
        (['in'], DWORD, 'dwStreamID'),
        (['out'], LPGUID, 'lpDeINTerlaceMode'),
    ),
]



class _VMRALPHABITMAP(ctypes.Structure):
    _fields_ = [
        ('dwFlags', DWORD),
        ('hdc', HDC),
        ('pDDS', LPDIRECTDRAWSURFACE7),
        ('rSrc', RECT),
        ('rDest', NORMALIZEDRECT),
        ('fAlpha', FLOAT),
        ('clrSrcKey', COLORREF),
    ]


VMRALPHABITMAP = _VMRALPHABITMAP


PVMRALPHABITMAP = POINTER(_VMRALPHABITMAP)


VMRBITMAP_DISABLE = 0x00000001
VMRBITMAP_HDC = 0x00000002
VMRBITMAP_ENTIREDDS = 0x00000004
VMRBITMAP_SRCCOLORKEY = 0x00000008
VMRBITMAP_SRCRECT = 0x00000010
IVMRMixerBitmap._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetAlphaBitmap',
        (['in'], POINTER(VMRALPHABITMAP), 'pBmpParms'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UpdateAlphaBitmapParameters',
        (['in'], PVMRALPHABITMAP, 'pBmpParms'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAlphaBitmapParameters',
        (['out'], PVMRALPHABITMAP, 'pBmpParms'),
    ),
]



class _VMRVIDEOSTREAMINFO(ctypes.Structure):
    _fields_ = [
        ('pddsVideoSurface', LPDIRECTDRAWSURFACE7),
        ('dwWidth', DWORD),
        ('dwHeight', DWORD),
        ('dwStrmID', DWORD),
        ('fAlpha', FLOAT),
        ('ddClrKey', DDCOLORKEY),
        ('rNormal', NORMALIZEDRECT),
    ]


VMRVIDEOSTREAMINFO = _VMRVIDEOSTREAMINFO


IVMRImageCompositor._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'InitCompositionTarget',
        (['in'], POINTER(comtypes.IUnknown), 'pD3DDevice'),
        (['in'], LPDIRECTDRAWSURFACE7, 'pddsRenderTarget'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TermCompositionTarget',
        (['in'], POINTER(comtypes.IUnknown), 'pD3DDevice'),
        (['in'], LPDIRECTDRAWSURFACE7, 'pddsRenderTarget'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetStreamMediaType',
        (['in'], DWORD, 'dwStrmID'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmt'),
        (['in'], BOOL, 'fTexture'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CompositeImage',
        (['in'], POINTER(comtypes.IUnknown), 'pD3DDevice'),
        (['in'], LPDIRECTDRAWSURFACE7, 'pddsRenderTarget'),
        (['in'], POINTER(AM_MEDIA_TYPE), 'pmtRenderTarget'),
        (['in'], REFERENCE_TIME, 'rtStart'),
        (['in'], REFERENCE_TIME, 'rtEnd'),
        (['in'], DWORD, 'dwClrBkGnd'),
        (['in'], POINTER(VMRVIDEOSTREAMINFO), 'pVideoStreamInfo'),
        (['in'], UINT, 'cStreams'),
    ),
]


IVMRVideoStreamControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetColorKey',
        (['in'], LPDDCOLORKEY, 'lpClrKey'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetColorKey',
        (['out'], VOID, 'lpClrKey'),  # LPDDCOLORKEY
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetStreamActiveState',
        (['in'], BOOL, 'fActive'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStreamActiveState',
        (['out'], POINTER(BOOL), 'lpfActive'),
    ),
]


IVMRSurface._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'LockSurface',
        (['out'], POINTER(POINTER(BYTE)), 'lpSurface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSurface',
        (['out'], POINTER(LPDIRECTDRAWSURFACE7), 'lplpSurface'),
    ),
]


IVMRImagePresenterConfig._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetRenderingPrefs',
        (['in'], DWORD, 'dwRenderFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRenderingPrefs',
        (['out'], POINTER(DWORD), 'dwRenderFlags'),
    ),
]


IVMRImagePresenterExclModeConfig._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetXlcModeDDObjAndPrimarySurface',
        (['in'], LPDIRECTDRAW7, 'lpDDObj'),
        (['in'], LPDIRECTDRAWSURFACE7, 'lpPrimarySurf'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetXlcModeDDObjAndPrimarySurface',
        (['out'], POINTER(LPDIRECTDRAW7), 'lpDDObj'),
        (['out'], POINTER(LPDIRECTDRAWSURFACE7), 'lpPrimarySurf'),
    ),
]


IVPManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetVideoPortIndex',
        (['in'], DWORD, 'dwVideoPortIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVideoPortIndex',
        (['out'], POINTER(DWORD), 'pdwVideoPortIndex'),
    ),
]


from .winapifamily_h import * # NOQA
from .ddraw_h import * # NOQA
class tagDVD_DOMAIN(ENUM):
    DVD_DOMAIN_FirstPlay = 1
    DVD_DOMAIN_VideoManagerMenu = DVD_DOMAIN_FirstPlay + 1
    DVD_DOMAIN_VideoTitleSetMenu = DVD_DOMAIN_VideoManagerMenu + 1
    DVD_DOMAIN_Title = DVD_DOMAIN_VideoTitleSetMenu + 1
    DVD_DOMAIN_Stop = DVD_DOMAIN_Title + 1


DVD_DOMAIN = tagDVD_DOMAIN


class tagDVD_MENU_ID(ENUM):
    DVD_MENU_Title = 2
    DVD_MENU_Root = 3
    DVD_MENU_Subpicture = 4
    DVD_MENU_Audio = 5
    DVD_MENU_Angle = 6
    DVD_MENU_Chapter = 7


DVD_MENU_ID = tagDVD_MENU_ID


class tagDVD_DISC_SIDE(ENUM):
    DVD_SIDE_A = 1
    DVD_SIDE_B = 2


DVD_DISC_SIDE = tagDVD_DISC_SIDE


class tagDVD_PREFERRED_DISPLAY_MODE(ENUM):
    DISPLAY_CONTENT_DEFAULT = 0
    DISPLAY_16x9 = 1
    DISPLAY_4x3_PANSCAN_PREFERRED = 2
    DISPLAY_4x3_LETTERBOX_PREFERRED = 3


DVD_PREFERRED_DISPLAY_MODE = tagDVD_PREFERRED_DISPLAY_MODE


DVD_REGISTER = WORD
GPRMARRAY = DVD_REGISTER * 16
SPRMARRAY = DVD_REGISTER * 24


class tagDVD_ATR(ctypes.Structure):
    _fields_ = [
        ('ulCAT', ULONG),
        ('pbATRI', BYTE * 768),
    ]


DVD_ATR = tagDVD_ATR

DVD_VideoATR = BYTE * 2
DVD_AudioATR = BYTE * 8
DVD_SubpictureATR = BYTE * 6


class tagDVD_FRAMERATE(ENUM):
    DVD_FPS_25 = 1
    DVD_FPS_30NonDrop = 3


DVD_FRAMERATE = tagDVD_FRAMERATE



class tagDVD_TIMECODE(ctypes.Structure):
    _fields_ = [
        ('Hours1    :4', ULONG),
        ('Hours10  :4', ULONG),
        ('Minutes1  :4', ULONG),
        ('Minutes10:4', ULONG),
        ('Seconds1  :4', ULONG),
        ('Seconds10:4', ULONG),
        ('Frames1   :4', ULONG),
        ('Frames10 :2', ULONG),
        ('FrameRateCode: 2', ULONG),
    ]


DVD_TIMECODE = tagDVD_TIMECODE


class tagDVD_NavCmdType(ENUM):
    DVD_NavCmdType_Pre = 1
    DVD_NavCmdType_Post = 2
    DVD_NavCmdType_Cell = 3
    DVD_NavCmdType_Button = 4


DVD_NavCmdType = tagDVD_NavCmdType


class tagDVD_TIMECODE_FLAGS(ENUM):
    DVD_TC_FLAG_25fps = 0x1
    DVD_TC_FLAG_30fps = 0x2
    DVD_TC_FLAG_DropFrame = 0x4
    DVD_TC_FLAG_Interpolated = 0x8


DVD_TIMECODE_FLAGS = tagDVD_TIMECODE_FLAGS



class tagDVD_HMSF_TIMECODE(ctypes.Structure):
    _fields_ = [
        ('bHours', BYTE),
        ('bMinutes', BYTE),
        ('bSeconds', BYTE),
        ('bFrames', BYTE),
    ]


DVD_HMSF_TIMECODE = tagDVD_HMSF_TIMECODE



class tagDVD_PLAYBACK_LOCATION2(ctypes.Structure):
    _fields_ = [
        ('TitleNum', ULONG),
        ('ChapterNum', ULONG),
        ('TimeCode', DVD_HMSF_TIMECODE),
        ('TimeCodeFlags', ULONG),
    ]


DVD_PLAYBACK_LOCATION2 = tagDVD_PLAYBACK_LOCATION2



class tagDVD_PLAYBACK_LOCATION(ctypes.Structure):
    _fields_ = [
        ('TitleNum', ULONG),
        ('ChapterNum', ULONG),
        ('TimeCode', ULONG),
    ]


DVD_PLAYBACK_LOCATION = tagDVD_PLAYBACK_LOCATION


VALID_UOP_SOMTHING_OR_OTHER = DWORD


class __MIDL___MIDL_itf_strmif_0000_0132_0001(ENUM):
    UOP_FLAG_Play_Title_Or_AtTime = 0x1
    UOP_FLAG_Play_Chapter = 0x2
    UOP_FLAG_Play_Title = 0x4
    UOP_FLAG_Stop = 0x8
    UOP_FLAG_ReturnFromSubMenu = 0x10
    UOP_FLAG_Play_Chapter_Or_AtTime = 0x20
    UOP_FLAG_PlayPrev_Or_Replay_Chapter = 0x40
    UOP_FLAG_PlayNext_Chapter = 0x80
    UOP_FLAG_Play_Forwards = 0x100
    UOP_FLAG_Play_Backwards = 0x200
    UOP_FLAG_ShowMenu_Title = 0x400
    UOP_FLAG_ShowMenu_Root = 0x800
    UOP_FLAG_ShowMenu_SubPic = 0x1000
    UOP_FLAG_ShowMenu_Audio = 0x2000
    UOP_FLAG_ShowMenu_Angle = 0x4000
    UOP_FLAG_ShowMenu_Chapter = 0x8000
    UOP_FLAG_Resume = 0x10000
    UOP_FLAG_Select_Or_Activate_Button = 0x20000
    UOP_FLAG_Still_Off = 0x40000
    UOP_FLAG_Pause_On = 0x80000
    UOP_FLAG_Select_Audio_Stream = 0x100000
    UOP_FLAG_Select_SubPic_Stream = 0x200000
    UOP_FLAG_Select_Angle = 0x400000
    UOP_FLAG_Select_Karaoke_Audio_Presentation_Mode = 0x800000
    UOP_FLAG_Select_Video_Mode_Preference = 0x1000000


VALID_UOP_FLAG = __MIDL___MIDL_itf_strmif_0000_0132_0001


class __MIDL___MIDL_itf_strmif_0000_0132_0002(ENUM):
    DVD_CMD_FLAG_None = 0
    DVD_CMD_FLAG_Flush = 0x1
    DVD_CMD_FLAG_SendEvents = 0x2
    DVD_CMD_FLAG_Block = 0x4
    DVD_CMD_FLAG_StartWhenRendered = 0x8
    DVD_CMD_FLAG_EndAfterRendered = 0x10


DVD_CMD_FLAGS = __MIDL___MIDL_itf_strmif_0000_0132_0002


class __MIDL___MIDL_itf_strmif_0000_0132_0003(ENUM):
    DVD_ResetOnStop = 1
    DVD_NotifyParentalLevelChange = 2
    DVD_HMSF_TimeCodeEvents = 3
    DVD_AudioDuringFFwdRew = 4
    DVD_EnableNonblockingAPIs = 5
    DVD_CacheSizeInMB = 6
    DVD_EnablePortableBookmarks = 7
    DVD_EnableExtendedCopyProtectErrors = 8
    DVD_NotifyPositionChange = 9
    DVD_IncreaseOutputControl = 10
    DVD_EnableStreaming = 11
    DVD_EnableESOutput = 12
    DVD_EnableTitleLength = 13
    DVD_DisableStillThrottle = 14
    DVD_EnableLoggingEvents = 15
    DVD_MaxReadBurstInKB = 16
    DVD_ReadBurstPeriodInMS = 17
    DVD_RestartDisc = 18
    DVD_EnableCC = 19


DVD_OPTION_FLAG = __MIDL___MIDL_itf_strmif_0000_0132_0003


class __MIDL___MIDL_itf_strmif_0000_0132_0004(ENUM):
    DVD_Relative_Upper = 1
    DVD_Relative_Lower = 2
    DVD_Relative_Left = 3
    DVD_Relative_Right = 4


DVD_RELATIVE_BUTTON = __MIDL___MIDL_itf_strmif_0000_0132_0004


class tagDVD_PARENTAL_LEVEL(ENUM):
    DVD_PARENTAL_LEVEL_8 = 0x8000
    DVD_PARENTAL_LEVEL_7 = 0x4000
    DVD_PARENTAL_LEVEL_6 = 0x2000
    DVD_PARENTAL_LEVEL_5 = 0x1000
    DVD_PARENTAL_LEVEL_4 = 0x800
    DVD_PARENTAL_LEVEL_3 = 0x400
    DVD_PARENTAL_LEVEL_2 = 0x200
    DVD_PARENTAL_LEVEL_1 = 0x100


DVD_PARENTAL_LEVEL = tagDVD_PARENTAL_LEVEL


class tagDVD_AUDIO_LANG_EXT(ENUM):
    DVD_AUD_EXT_NotSpecified = 0
    DVD_AUD_EXT_Captions = 1
    DVD_AUD_EXT_VisuallyImpaired = 2
    DVD_AUD_EXT_DirectorComments1 = 3
    DVD_AUD_EXT_DirectorComments2 = 4


DVD_AUDIO_LANG_EXT = tagDVD_AUDIO_LANG_EXT


class tagDVD_SUBPICTURE_LANG_EXT(ENUM):
    DVD_SP_EXT_NotSpecified = 0
    DVD_SP_EXT_Caption_Normal = 1
    DVD_SP_EXT_Caption_Big = 2
    DVD_SP_EXT_Caption_Children = 3
    DVD_SP_EXT_CC_Normal = 5
    DVD_SP_EXT_CC_Big = 6
    DVD_SP_EXT_CC_Children = 7
    DVD_SP_EXT_Forced = 9
    DVD_SP_EXT_DirectorComments_Normal = 13
    DVD_SP_EXT_DirectorComments_Big = 14
    DVD_SP_EXT_DirectorComments_Children = 15


DVD_SUBPICTURE_LANG_EXT = tagDVD_SUBPICTURE_LANG_EXT


class tagDVD_AUDIO_APPMODE(ENUM):
    DVD_AudioMode_None = 0
    DVD_AudioMode_Karaoke = 1
    DVD_AudioMode_Surround = 2
    DVD_AudioMode_Other = 3


DVD_AUDIO_APPMODE = tagDVD_AUDIO_APPMODE


class tagDVD_AUDIO_FORMAT(ENUM):
    DVD_AudioFormat_AC3 = 0
    DVD_AudioFormat_MPEG1 = 1
    DVD_AudioFormat_MPEG1_DRC = 2
    DVD_AudioFormat_MPEG2 = 3
    DVD_AudioFormat_MPEG2_DRC = 4
    DVD_AudioFormat_LPCM = 5
    DVD_AudioFormat_DTS = 6
    DVD_AudioFormat_SDDS = 7
    DVD_AudioFormat_Other = 8


DVD_AUDIO_FORMAT = tagDVD_AUDIO_FORMAT


class tagDVD_KARAOKE_DOWNMIX(ENUM):
    DVD_Mix_0to0 = 0x1
    DVD_Mix_1to0 = 0x2
    DVD_Mix_2to0 = 0x4
    DVD_Mix_3to0 = 0x8
    DVD_Mix_4to0 = 0x10
    DVD_Mix_Lto0 = 0x20
    DVD_Mix_Rto0 = 0x40
    DVD_Mix_0to1 = 0x100
    DVD_Mix_1to1 = 0x200
    DVD_Mix_2to1 = 0x400
    DVD_Mix_3to1 = 0x800
    DVD_Mix_4to1 = 0x1000
    DVD_Mix_Lto1 = 0x2000
    DVD_Mix_Rto1 = 0x4000


DVD_KARAOKE_DOWNMIX = tagDVD_KARAOKE_DOWNMIX



class tagDVD_AudioAttributes(ctypes.Structure):
    _fields_ = [
        ('AppMode', DVD_AUDIO_APPMODE),
        ('AppModeData', BYTE),
        ('AudioFormat', DVD_AUDIO_FORMAT),
        ('Language', LCID),
        ('LanguageExtension', DVD_AUDIO_LANG_EXT),
        ('fHasMultichannelInfo', BOOL),
        ('dwFrequency', DWORD),
        ('bQuantization', BYTE),
        ('bNumberOfChannels', BYTE),
        ('dwReserved', DWORD * 2),
    ]


DVD_AudioAttributes = tagDVD_AudioAttributes



class tagDVD_MUA_MixingInfo(ctypes.Structure):
    _fields_ = [
        ('fMixTo0', BOOL),
        ('fMixTo1', BOOL),
        ('fMix0InPhase', BOOL),
        ('fMix1InPhase', BOOL),
        ('dwSpeakerPosition', DWORD),
    ]


DVD_MUA_MixingInfo = tagDVD_MUA_MixingInfo



class tagDVD_MUA_Coeff(ctypes.Structure):
    _fields_ = [
        ('log2_alpha', DOUBLE),
        ('log2_beta', DOUBLE),
    ]


DVD_MUA_Coeff = tagDVD_MUA_Coeff



class tagDVD_MultichannelAudioAttributes(ctypes.Structure):
    _fields_ = [
        ('Info', DVD_MUA_MixingInfo * 8),
        ('Coeff', DVD_MUA_Coeff * 8),
    ]


DVD_MultichannelAudioAttributes = tagDVD_MultichannelAudioAttributes


class tagDVD_KARAOKE_CONTENTS(ENUM):
    DVD_Karaoke_GuideVocal1 = 0x1
    DVD_Karaoke_GuideVocal2 = 0x2
    DVD_Karaoke_GuideMelody1 = 0x4
    DVD_Karaoke_GuideMelody2 = 0x8
    DVD_Karaoke_GuideMelodyA = 0x10
    DVD_Karaoke_GuideMelodyB = 0x20
    DVD_Karaoke_SoundEffectA = 0x40
    DVD_Karaoke_SoundEffectB = 0x80


DVD_KARAOKE_CONTENTS = tagDVD_KARAOKE_CONTENTS


class tagDVD_KARAOKE_ASSIGNMENT(ENUM):
    DVD_Assignment_reserved0 = 0
    DVD_Assignment_reserved1 = 1
    DVD_Assignment_LR = 2
    DVD_Assignment_LRM = 3
    DVD_Assignment_LR1 = 4
    DVD_Assignment_LRM1 = 5
    DVD_Assignment_LR12 = 6
    DVD_Assignment_LRM12 = 7


DVD_KARAOKE_ASSIGNMENT = tagDVD_KARAOKE_ASSIGNMENT



class tagDVD_KaraokeAttributes(ctypes.Structure):
    _fields_ = [
        ('bVersion', BYTE),
        ('fMasterOfCeremoniesInGuideVocal1', BOOL),
        ('fDuet', BOOL),
        ('ChannelAssignment', DVD_KARAOKE_ASSIGNMENT),
        ('wChannelContents', WORD * 8),
    ]


DVD_KaraokeAttributes = tagDVD_KaraokeAttributes


class tagDVD_VIDEO_COMPRESSION(ENUM):
    DVD_VideoCompression_Other = 0
    DVD_VideoCompression_MPEG1 = 1
    DVD_VideoCompression_MPEG2 = 2


DVD_VIDEO_COMPRESSION = tagDVD_VIDEO_COMPRESSION



class tagDVD_VideoAttributes(ctypes.Structure):
    _fields_ = [
        ('fPanscanPermitted', BOOL),
        ('fLetterboxPermitted', BOOL),
        ('ulAspectX', ULONG),
        ('ulAspectY', ULONG),
        ('ulFrameRate', ULONG),
        ('ulFrameHeight', ULONG),
        ('Compression', DVD_VIDEO_COMPRESSION),
        ('fLine21Field1InGOP', BOOL),
        ('fLine21Field2InGOP', BOOL),
        ('ulSourceResolutionX', ULONG),
        ('ulSourceResolutionY', ULONG),
        ('fIsSourceLetterboxed', BOOL),
        ('fIsFilmMode', BOOL),
    ]


DVD_VideoAttributes = tagDVD_VideoAttributes


class tagDVD_SUBPICTURE_TYPE(ENUM):
    DVD_SPType_NotSpecified = 0
    DVD_SPType_Language = 1
    DVD_SPType_Other = 2


DVD_SUBPICTURE_TYPE = tagDVD_SUBPICTURE_TYPE


class tagDVD_SUBPICTURE_CODING(ENUM):
    DVD_SPCoding_RunLength = 0
    DVD_SPCoding_Extended = 1
    DVD_SPCoding_Other = 2


DVD_SUBPICTURE_CODING = tagDVD_SUBPICTURE_CODING



class tagDVD_SubpictureAttributes(ctypes.Structure):
    _fields_ = [
        ('Type', DVD_SUBPICTURE_TYPE),
        ('CodingMode', DVD_SUBPICTURE_CODING),
        ('Language', LCID),
        ('LanguageExtension', DVD_SUBPICTURE_LANG_EXT),
    ]


DVD_SubpictureAttributes = tagDVD_SubpictureAttributes


class tagDVD_TITLE_APPMODE(ENUM):
    DVD_AppMode_Not_Specified = 0
    DVD_AppMode_Karaoke = 1
    DVD_AppMode_Other = 3


DVD_TITLE_APPMODE = tagDVD_TITLE_APPMODE



class tagDVD_TitleMainAttributes(ctypes.Structure):

    class _Union_0(ctypes.Union):
        _fields_ = [
            ('AppMode', DVD_TITLE_APPMODE),
            ('TitleLength', DVD_HMSF_TIMECODE),
        ]

    _anonymous_ = ('_Union_0', )
    _fields_ = [
        ('_Union_0', _Union_0),
        ('VideoAttributes', DVD_VideoAttributes),
        ('ulNumberOfAudioStreams', ULONG),
        ('AudioAttributes', DVD_AudioAttributes * 8),
        ('MultichannelAudioAttributes', DVD_MultichannelAudioAttributes * 8),
        ('ulNumberOfSubpictureStreams', ULONG),
        ('SubpictureAttributes', DVD_SubpictureAttributes * 32),
    ]


DVD_TitleAttributes = tagDVD_TitleMainAttributes



class tagDVD_MenuAttributes(ctypes.Structure):
    _fields_ = [
        ('fCompatibleRegion', BOOL * 8),
        ('VideoAttributes', DVD_VideoAttributes),
        ('fAudioPresent', BOOL),
        ('AudioAttributes', DVD_AudioAttributes),
        ('fSubpicturePresent', BOOL),
        ('SubpictureAttributes', DVD_SubpictureAttributes),
    ]


DVD_MenuAttributes = tagDVD_MenuAttributes


IDvdControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'TitlePlay',
        (['in'], ULONG, 'ulTitle'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ChapterPlay',
        (['in'], ULONG, 'ulTitle'),
        (['in'], ULONG, 'ulChapter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TimePlay',
        (['in'], ULONG, 'ulTitle'),
        (['in'], ULONG, 'bcdTime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TimeSearch',
        (['in'], ULONG, 'bcdTime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ChapterSearch',
        (['in'], ULONG, 'ulChapter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ForwardScan',
        (['in'], DOUBLE, 'dwSpeed'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BackwardScan',
        (['in'], DOUBLE, 'dwSpeed'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MenuCall',
        (['in'], DVD_MENU_ID, 'MenuID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ButtonSelectAndActivate',
        (['in'], ULONG, 'ulButton'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MenuLanguageSelect',
        (['in'], LCID, 'Language'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AudioStreamChange',
        (['in'], ULONG, 'ulAudio'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SubpictureStreamChange',
        (['in'], ULONG, 'ulSubPicture'),
        (['in'], BOOL, 'bDisplay'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AngleChange',
        (['in'], ULONG, 'ulAngle'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ParentalLevelSelect',
        (['in'], ULONG, 'ulParentalLevel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ParentalCountrySelect',
        (['in'], WORD, 'wCountry'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'KaraokeAudioPresentationModeChange',
        (['in'], ULONG, 'ulMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'VideoModePreferrence',
        (['in'], ULONG, 'ulPreferredDisplayMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetRoot',
        (['in'], LPCWSTR, 'pszPath'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MouseActivate',
        (['in'], POINT, 'poINT'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MouseSelect',
        (['in'], POINT, 'poINT'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ChapterPlayAutoStop',
        (['in'], ULONG, 'ulTitle'),
        (['in'], ULONG, 'ulChapter'),
        (['in'], ULONG, 'ulChaptersToPlay'),
    ),
]


IDvdInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentDomain',
        (['out'], POINTER(DVD_DOMAIN), 'pDomain'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentLocation',
        (['out'], POINTER(DVD_PLAYBACK_LOCATION), 'pLocation'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTotalTitleTime',
        (['out'], POINTER(ULONG), 'pulTotalTime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentButton',
        (['out'], POINTER(ULONG), 'pulButtonsAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentButton'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentAngle',
        (['out'], POINTER(ULONG), 'pulAnglesAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentAngle'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentAudio',
        (['out'], POINTER(ULONG), 'pulStreamsAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentStream'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentSubpicture',
        (['out'], POINTER(ULONG), 'pulStreamsAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentStream'),
        (['out'], POINTER(BOOL), 'pIsDisabled'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentUOPS',
        (['out'], POINTER(VALID_UOP_SOMTHING_OR_OTHER), 'pUOP'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllSPRMs',
        (['out'], POINTER(SPRMARRAY), 'pRegisterArray'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllGPRMs',
        (['out'], POINTER(GPRMARRAY), 'pRegisterArray'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAudioLanguage',
        (['in'], ULONG, 'ulStream'),
        (['out'], POINTER(LCID), 'pLanguage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSubpictureLanguage',
        (['in'], ULONG, 'ulStream'),
        (['out'], POINTER(LCID), 'pLanguage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTitleAttributes',
        (['in'], ULONG, 'ulTitle'),
        (['out'], POINTER(DVD_ATR), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVMGAttributes',
        (['out'], POINTER(DVD_ATR), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentVideoAttributes',
        (['out'], POINTER(DVD_VideoATR), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentAudioAttributes',
        (['out'], POINTER(DVD_AudioATR), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentSubpictureAttributes',
        (['out'], POINTER(DVD_SubpictureATR), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentVolumeInfo',
        (['out'], POINTER(ULONG), 'pulNumOfVol'),
        (['out'], POINTER(ULONG), 'pulThisVolNum'),
        (['out'], POINTER(DVD_DISC_SIDE), 'pSide'),
        (['out'], POINTER(ULONG), 'pulNumOfTitles'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDVDTextInfo',
        ([], POINTER(BYTE), 'pTextManager'),
        (['in'], ULONG, 'ulBufSize'),
        (['out'], POINTER(ULONG), 'pulActualSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPlayerParentalLevel',
        (['out'], POINTER(ULONG), 'pulParentalLevel'),
        (['out'], POINTER(ULONG), 'pulCountryCode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNumberOfChapters',
        (['in'], ULONG, 'ulTitle'),
        (['out'], POINTER(ULONG), 'pulNumberOfChapters'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTitleParentalLevels',
        (['in'], ULONG, 'ulTitle'),
        (['out'], POINTER(ULONG), 'pulParentalLevels'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRoot',
        ([], LPSTR, 'pRoot'),
        (['in'], ULONG, 'ulBufSize'),
        (['out'], POINTER(ULONG), 'pulActualSize'),
    ),
]


IDvdCmd._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'WaitForEnd'
    ),
]


IDvdState._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDiscID',
        (['out'], POINTER(ULONGLONG), 'pullUniqueID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParentalLevel',
        (['out'], POINTER(ULONG), 'pulParentalLevel'),
    ),
]


IDvdControl2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'PlayTitle',
        (['in'], ULONG, 'ulTitle'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayChapterInTitle',
        (['in'], ULONG, 'ulTitle'),
        (['in'], ULONG, 'ulChapter'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayAtTimeInTitle',
        (['in'], ULONG, 'ulTitle'),
        (['in'], POINTER(DVD_HMSF_TIMECODE), 'pStartTime'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReturnFromSubmenu',
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayAtTime',
        (['in'], POINTER(DVD_HMSF_TIMECODE), 'pTime'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayChapter',
        (['in'], ULONG, 'ulChapter'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayPrevChapter',
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReplayChapter',
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayNextChapter',
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayForwards',
        (['in'], DOUBLE, 'dSpeed'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayBackwards',
        (['in'], DOUBLE, 'dSpeed'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ShowMenu',
        (['in'], DVD_MENU_ID, 'MenuID'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Resume',
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectRelativeButton',
        ([], DVD_RELATIVE_BUTTON, 'buttonDir'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectButton',
        (['in'], ULONG, 'ulButton'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectAndActivateButton',
        (['in'], ULONG, 'ulButton'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Pause',
        (['in'], BOOL, 'bState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectAudioStream',
        (['in'], ULONG, 'ulAudio'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectSubpictureStream',
        (['in'], ULONG, 'ulSubPicture'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSubpictureState',
        (['in'], BOOL, 'bState'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectAngle',
        (['in'], ULONG, 'ulAngle'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectParentalLevel',
        (['in'], ULONG, 'ulParentalLevel'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectParentalCountry',
        (['in'], BYTE * 2, 'bCountry'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectKaraokeAudioPresentationMode',
        (['in'], ULONG, 'ulMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectVideoModePreference',
        (['in'], ULONG, 'ulPreferredDisplayMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDVDDirectory',
        (['in'], LPCWSTR, 'pszwPath'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ActivateAtPosition',
        (['in'], POINT, 'poINT'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectAtPosition',
        (['in'], POINT, 'poINT'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayChaptersAutoStop',
        (['in'], ULONG, 'ulTitle'),
        (['in'], ULONG, 'ulChapter'),
        (['in'], ULONG, 'ulChaptersToPlay'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AcceptParentalLevelChange',
        (['in'], BOOL, 'bAccept'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetOption',
        (['in'], DVD_OPTION_FLAG, 'flag'),
        (['in'], BOOL, 'fState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetState',
        (['in'], POINTER(IDvdState), 'pState'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PlayPeriodInTitleAutoStop',
        (['in'], ULONG, 'ulTitle'),
        (['in'], POINTER(DVD_HMSF_TIMECODE), 'pStartTime'),
        (['in'], POINTER(DVD_HMSF_TIMECODE), 'pEndTime'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetGPRM',
        (['in'], ULONG, 'ulIndex'),
        (['in'], WORD, 'wValue'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'ppCmd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectDefaultMenuLanguage',
        (['in'], LCID, 'Language'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectDefaultAudioLanguage',
        (['in'], LCID, 'Language'),
        (['in'], DVD_AUDIO_LANG_EXT, 'audioExtension'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SelectDefaultSubpictureLanguage',
        (['in'], LCID, 'Language'),
        (['in'], DVD_SUBPICTURE_LANG_EXT, 'subpictureExtension'),
    ),
]


class DVD_TextStringType(ENUM):
    DVD_Struct_Volume = 0x1
    DVD_Struct_Title = 0x2
    DVD_Struct_ParentalID = 0x3
    DVD_Struct_PartOfTitle = 0x4
    DVD_Struct_Cell = 0x5
    DVD_Stream_Audio = 0x10
    DVD_Stream_Subpicture = 0x11
    DVD_Stream_Angle = 0x12
    DVD_Channel_Audio = 0x20
    DVD_General_Name = 0x30
    DVD_General_Comments = 0x31
    DVD_Title_Series = 0x38
    DVD_Title_Movie = 0x39
    DVD_Title_Video = 0x3a
    DVD_Title_Album = 0x3b
    DVD_Title_Song = 0x3c
    DVD_Title_Other = 0x3f
    DVD_Title_Sub_Series = 0x40
    DVD_Title_Sub_Movie = 0x41
    DVD_Title_Sub_Video = 0x42
    DVD_Title_Sub_Album = 0x43
    DVD_Title_Sub_Song = 0x44
    DVD_Title_Sub_Other = 0x47
    DVD_Title_Orig_Series = 0x48
    DVD_Title_Orig_Movie = 0x49
    DVD_Title_Orig_Video = 0x4a
    DVD_Title_Orig_Album = 0x4b
    DVD_Title_Orig_Song = 0x4c
    DVD_Title_Orig_Other = 0x4f
    DVD_Other_Scene = 0x50
    DVD_Other_Cut = 0x51
    DVD_Other_Take = 0x52


class DVD_TextCharSet(ENUM):
    DVD_CharSet_Unicode = 0
    DVD_CharSet_ISO646 = 1
    DVD_CharSet_JIS_Roman_Kanji = 2
    DVD_CharSet_ISO8859_1 = 3
    DVD_CharSet_ShiftJIS_Kanji_Roman_Katakana = 4


DVD_TITLE_MENU = 0x000
DVD_STREAM_DATA_CURRENT = 0x800
DVD_STREAM_DATA_VMGM = 0x400
DVD_STREAM_DATA_VTSM = 0x401
DVD_DEFAULT_AUDIO_STREAM = 0x0f


class tagDVD_DECODER_CAPS(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwAudioCaps', DWORD),
        ('dFwdMaxRateVideo', DOUBLE),
        ('dFwdMaxRateAudio', DOUBLE),
        ('dFwdMaxRateSP', DOUBLE),
        ('dBwdMaxRateVideo', DOUBLE),
        ('dBwdMaxRateAudio', DOUBLE),
        ('dBwdMaxRateSP', DOUBLE),
        ('dwRes1', DWORD),
        ('dwRes2', DWORD),
        ('dwRes3', DWORD),
        ('dwRes4', DWORD),
    ]


DVD_DECODER_CAPS = tagDVD_DECODER_CAPS


DVD_AUDIO_CAPS_AC3 = 0x00000001
DVD_AUDIO_CAPS_MPEG2 = 0x00000002
DVD_AUDIO_CAPS_LPCM = 0x00000004
DVD_AUDIO_CAPS_DTS = 0x00000008
DVD_AUDIO_CAPS_SDDS = 0x00000010
IDvdInfo2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentDomain',
        (['out'], POINTER(DVD_DOMAIN), 'pDomain'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentLocation',
        (['out'], POINTER(DVD_PLAYBACK_LOCATION2), 'pLocation'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTotalTitleTime',
        (['out'], POINTER(DVD_HMSF_TIMECODE), 'pTotalTime'),
        (['out'], POINTER(ULONG), 'ulTimeCodeFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentButton',
        (['out'], POINTER(ULONG), 'pulButtonsAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentButton'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentAngle',
        (['out'], POINTER(ULONG), 'pulAnglesAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentAngle'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentAudio',
        (['out'], POINTER(ULONG), 'pulStreamsAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentStream'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentSubpicture',
        (['out'], POINTER(ULONG), 'pulStreamsAvailable'),
        (['out'], POINTER(ULONG), 'pulCurrentStream'),
        (['out'], POINTER(BOOL), 'pbIsDisabled'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentUOPS',
        (['out'], POINTER(ULONG), 'pulUOPs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllSPRMs',
        (['out'], POINTER(SPRMARRAY), 'pRegisterArray'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAllGPRMs',
        (['out'], POINTER(GPRMARRAY), 'pRegisterArray'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAudioLanguage',
        (['in'], ULONG, 'ulStream'),
        (['out'], POINTER(LCID), 'pLanguage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSubpictureLanguage',
        (['in'], ULONG, 'ulStream'),
        (['out'], POINTER(LCID), 'pLanguage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTitleAttributes',
        (['in'], ULONG, 'ulTitle'),
        (['out'], POINTER(DVD_MenuAttributes), 'pMenu'),
        (['out'], POINTER(DVD_TitleAttributes), 'pTitle'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVMGAttributes',
        (['out'], POINTER(DVD_MenuAttributes), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentVideoAttributes',
        (['out'], POINTER(DVD_VideoAttributes), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetAudioAttributes',
        (['in'], ULONG, 'ulStream'),
        (['out'], POINTER(DVD_AudioAttributes), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetKaraokeAttributes',
        (['in'], ULONG, 'ulStream'),
        (['out'], POINTER(DVD_KaraokeAttributes), 'pAttributes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSubpictureAttributes',
        (['in'], ULONG, 'ulStream'),
        (['out'], POINTER(DVD_SubpictureAttributes), 'pATR'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDVDVolumeInfo',
        (['out'], POINTER(ULONG), 'pulNumOfVolumes'),
        (['out'], POINTER(ULONG), 'pulVolume'),
        (['out'], POINTER(DVD_DISC_SIDE), 'pSide'),
        (['out'], POINTER(ULONG), 'pulNumOfTitles'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDVDTextNumberOfLanguages',
        (['out'], POINTER(ULONG), 'pulNumOfLangs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDVDTextLanguageInfo',
        (['in'], ULONG, 'ulLangIndex'),
        (['out'], POINTER(ULONG), 'pulNumOfStrings'),
        (['out'], POINTER(LCID), 'pLangCode'),
        (['out'], POINTER(DVD_TextCharSet), 'pbCharacterSet'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDVDTextStringAsNative',
        (['in'], ULONG, 'ulLangIndex'),
        (['in'], ULONG, 'ulStringIndex'),
        (['out'], POINTER(BYTE), 'pbBuffer'),
        (['in'], ULONG, 'ulMaxBufferSize'),
        (['out'], POINTER(ULONG), 'pulActualSize'),
        (['out'], POINTER(DVD_TextStringType), 'pType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDVDTextStringAsUnicode',
        (['in'], ULONG, 'ulLangIndex'),
        (['in'], ULONG, 'ulStringIndex'),
        (['out'], POINTER(WCHAR), 'pchwBuffer'),
        (['in'], ULONG, 'ulMaxBufferSize'),
        (['out'], POINTER(ULONG), 'pulActualSize'),
        (['out'], POINTER(DVD_TextStringType), 'pType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPlayerParentalLevel',
        (['out'], POINTER(ULONG), 'pulParentalLevel'),
        (['out'], BYTE * 2, 'pbCountryCode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNumberOfChapters',
        (['in'], ULONG, 'ulTitle'),
        (['out'], POINTER(ULONG), 'pulNumOfChapters'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTitleParentalLevels',
        (['in'], ULONG, 'ulTitle'),
        (['out'], POINTER(ULONG), 'pulParentalLevels'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDVDDirectory',
        ([], LPWSTR, 'pszwPath'),
        (['in'], ULONG, 'ulMaxSize'),
        (['out'], POINTER(ULONG), 'pulActualSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsAudioStreamEnabled',
        (['in'], ULONG, 'ulStreamNum'),
        (['out'], POINTER(BOOL), 'pbEnabled'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDiscID',
        (['in'], LPCWSTR, 'pszwPath'),
        (['out'], POINTER(ULONGLONG), 'pullDiscID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        (['out'], POINTER(POINTER(IDvdState)), 'pStateData'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMenuLanguages',
        (['out'], POINTER(LCID), 'pLanguages'),
        (['in'], ULONG, 'ulMaxLanguages'),
        (['out'], POINTER(ULONG), 'pulActualLanguages'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetButtonAtPosition',
        (['in'], POINT, 'point'),
        (['out'], POINTER(ULONG), 'pulButtonIndex'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCmdFromEvent',
        (['in'], LONG_PTR, 'lParam1'),
        (['out'], POINTER(POINTER(IDvdCmd)), 'pCmdObj'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultMenuLanguage',
        (['out'], POINTER(LCID), 'pLanguage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultAudioLanguage',
        (['out'], POINTER(LCID), 'pLanguage'),
        (['out'], POINTER(DVD_AUDIO_LANG_EXT), 'pAudioExtension'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultSubpictureLanguage',
        (['out'], POINTER(LCID), 'pLanguage'),
        (['out'], POINTER(DVD_SUBPICTURE_LANG_EXT), 'pSubpictureExtension'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDecoderCaps',
        (['out'], POINTER(DVD_DECODER_CAPS), 'pCaps'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetButtonRect',
        (['in'], ULONG, 'ulButton'),
        (['out'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsSubpictureStreamEnabled',
        (['in'], ULONG, 'ulStreamNum'),
        (['out'], POINTER(BOOL), 'pbEnabled'),
    ),
]


class _AM_DVD_GRAPH_FLAGS(ENUM):
    AM_DVD_HWDEC_PREFER = 0x1
    AM_DVD_HWDEC_ONLY = 0x2
    AM_DVD_SWDEC_PREFER = 0x4
    AM_DVD_SWDEC_ONLY = 0x8
    AM_DVD_NOVPE = 0x100
    AM_DVD_DO_NOT_CLEAR = 0x200
    AM_DVD_VMR9_ONLY = 0x800
    AM_DVD_EVR_ONLY = 0x1000
    AM_DVD_EVR_QOS = 0x2000
    AM_DVD_ADAPT_GRAPH = 0x4000
    AM_DVD_MASK = 0xFFFF


AM_DVD_GRAPH_FLAGS = _AM_DVD_GRAPH_FLAGS


class _AM_DVD_STREAM_FLAGS(ENUM):
    AM_DVD_STREAM_VIDEO = 0x1
    AM_DVD_STREAM_AUDIO = 0x2
    AM_DVD_STREAM_SUBPIC = 0x4


AM_DVD_STREAM_FLAGS = _AM_DVD_STREAM_FLAGS



class __MIDL___MIDL_itf_strmif_0000_0138_0001(ctypes.Structure):
    _fields_ = [
        ('hrVPEStatus', HRESULT),
        ('bDvdVolInvalid', BOOL),
        ('bDvdVolUnknown', BOOL),
        ('bNoLine21In', BOOL),
        ('bNoLine21Out', BOOL),
        ('iNumStreams', INT),
        ('iNumStreamsFailed', INT),
        ('dwFailedStreamsFlag', DWORD),
    ]


AM_DVD_RENDERSTATUS = __MIDL___MIDL_itf_strmif_0000_0138_0001


IDvdGraphBuilder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetFiltergraph',
        (['out'], POINTER(POINTER(IGraphBuilder)), 'ppGB'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDvdInterface',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvIF'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenderDvdVideoVolume',
        (['in'], LPCWSTR, 'lpcwszPathName'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(AM_DVD_RENDERSTATUS), 'pStatus'),
    ),
]


IDDrawExclModeVideo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetDDrawObject',
        (['in'], POINTER(IDirectDraw), 'pDDrawObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDDrawObject',
        (['out'], POINTER(POINTER(IDirectDraw)), 'ppDDrawObject'),
        (['out'], POINTER(BOOL), 'pbUsingExternal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDDrawSurface',
        (['in'], POINTER(IDirectDrawSurface), 'pDDrawSurface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDDrawSurface',
        (['out'], POINTER(POINTER(IDirectDrawSurface)), 'ppDDrawSurface'),
        (['out'], POINTER(BOOL), 'pbUsingExternal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDrawParameters',
        (['in'], POINTER(RECT), 'prcSource'),
        (['in'], POINTER(RECT), 'prcTarget'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetNativeVideoProps',
        (['out'], POINTER(DWORD), 'pdwVideoWidth'),
        (['out'], POINTER(DWORD), 'pdwVideoHeight'),
        (['out'], POINTER(DWORD), 'pdwPictAspectRatioX'),
        (['out'], POINTER(DWORD), 'pdwPictAspectRatioY'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetCallbackInterface',
        (['in'], POINTER(IDDrawExclModeVideoCallback), 'pCallback'),
        (['in'], DWORD, 'dwFlags'),
    ),
]


IDDrawExclModeVideoCallback._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnUpdateOverlay',
        (['in'], BOOL, 'bBefore'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], BOOL, 'bOldVisible'),
        (['in'], POINTER(RECT), 'prcOldSrc'),
        (['in'], POINTER(RECT), 'prcOldDest'),
        (['in'], BOOL, 'bNewVisible'),
        (['in'], POINTER(RECT), 'prcNewSrc'),
        (['in'], POINTER(RECT), 'prcNewDest'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnUpdateColorKey',
        (['in'], POINTER(COLORKEY), 'pKey'),
        (['in'], DWORD, 'dwColor'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnUpdateSize',
        (['in'], DWORD, 'dwWidth'),
        (['in'], DWORD, 'dwHeight'),
        (['in'], DWORD, 'dwARWidth'),
        (['in'], DWORD, 'dwARHeight'),
    ),
]



__all__ = (
    'IAMPushSource', 'IOverlayNotify2', 'IAMStreamControl', 'IMemInputPin',
    'IAMDevMemoryAllocator', 'IEnumRegFilters', 'IOverlayNotify',
    'IVMRImagePresenterConfig', 'IBPCSatelliteTuner', 'IGetCapabilitiesKey',
    'IVMRDeINTerlaceControl', 'IKsPropertySet', 'IAMCrossbar', 'IDVSplitter',
    'IMpeg2Demultiplexer', 'IVMRMixerControl', 'IDistributorNotify', 'IPin',
    'IFilterGraph2', 'IFilterGraph3', 'IAMDecoderCaps', 'IPinFlowControl',
    'IAMVideoControl', 'IAMVfwCompressDialogs', 'IAMTVAudioNotification',
    'IAMVfwCaptureDialogs', 'IVMRSurfaceAllocator', 'IAMClockAdjust', 'PPIN',
    'IEncoderAPI', 'ICaptureGraphBuilder2', 'IDvdCmd', 'IAMPluginControl',
    'IEnumPins', 'IAMClockSlave', 'ICaptureGraphBuilder', 'IMediaFilter',
    'IRegisterServiceProvider', 'IVMRImagePresenter', 'IEnumFilters',
    'IPersistMediaPropertyBag', 'IDvdControl2', 'IAMTimecodeReader', 'IDVEnc',
    'IAMVideoProcAmp', 'IAMPhysicalPinInfo', 'IAMCopyCaptureFileProgress',
    'IAMExtDevice', 'IReferenceClockTimerControl', 'IAMAnalogVideoEncoder',
    'IMPEG2StreamIdMap', 'IAMStreamConfig', 'IAMFilterMiscFlags', 'IDvdInfo',
    'IResourceConsumer', 'IAMVideoCompression', 'IMediaEventSink', 'IAMTuner',
    'ISeekingPassThru', 'IDvdControl', 'IVMRWindowlessControl', 'IAMLatency',
    'IMemAllocator', 'IMemAllocatorNotifyCallbackTemp', 'IAMTimecodeDisplay',
    'IFilterGraph', 'IMediaSample', 'IReferenceClock', 'IVMRSurface',
    'IAMGraphStreams', 'IAMBufferNegotiation', 'IVPManager', 'IStreamBuilder',
    'IReferenceClock2', 'IAMAsyncReaderTimestampScaling', 'IAMCameraControl',
    'ICodecAPI', 'IOverlay', 'IAMTVTuner', 'IQualityControl', 'IAMovieSetup',
    'IPinConnection', 'IMemAllocatorCallbackTemp', 'IMediaSample2Config',
    'IVMRAspectRatioControl', 'ICreateDevEnum', 'IAMTunerNotification',
    'IAMDevMemoryControl', 'IAMAnalogVideoDecoder', 'IAMResourceControl',
    'IFilterMapper2', 'IFilterMapper3', 'IDvdGraphBuilder', 'IGraphBuilder',
    'IVMRVideoStreamControl', 'IGraphConfigCallback', 'IVMRMonitorConfig',
    'IFileSourceFilter', 'IMediaSeeking', 'IAMExtTransport', 'IDVRGB219',
    'IAMDeviceRemoval', 'IVideoEncoder', 'IConfigInterleaving', 'IDvdState',
    'IVideoFrameStep', 'IAMAudioRendererStats', 'IAMOverlayFX', 'IAMTVAudio',
    'IVMRFilterConfig', 'IDDrawExclModeVideoCallback', 'IFileSinkFilter',
    'IAMOpenProgress', 'IAMAudioInputMixer', 'IGraphConfig', 'IIPDVDec',
    'IDDrawExclModeVideo', 'IVMRImageCompositor', 'IMediaPropertyBag',
    'IEnumStreamIdMap', 'IFileSinkFilter2', 'IAMTimecodeGenerator', 'VMRMode',
    'IFilterChain', 'IResourceManager', 'IConfigAviMux', 'IVMRMixerBitmap',
    'IAMStreamSelect', 'IMediaSample2', 'IDecimateVideoImage', 'IBaseFilter',
    'IAMCertifiedOutputProtection', 'IFilterMapper', 'IDvdInfo2', 'DVINFO',
    'IAMVideoDecimationProperties', 'IAMDroppedFrames', 'IGraphVersion',
    'IEnumMediaTypes', 'IVMRSurfaceAllocatorNotify', 'IAsyncReader',
    'IVMRImagePresenterExclModeConfig', 'IDrawVideoImage', 'ADVISE_ALL2',
    'VMRBITMAP_SRCCOLORKEY', 'CDEF_DEVMON_FILTER', 'VMRBITMAP_HDC', 'DVD_ATR',
    'AM_GETDECODERCAP_QUERY_VMR9_SUPPORT', 'MAX_PIN_NAME', 'CDEF_DEVMON_DMO',
    'AnalogVideo_PAL_Mask', 'MPEG2_PROGRAM_PACK_HEADER', 'VMRBITMAP_DISABLE',
    'MPEG2_PROGRAM_SYSTEM_HEADER', 'DECODER_CAP_NOTSUPPORTED', 'ADVISE_ALL',
    'MPEG2_PROGRAM_PES_STREAM', 'DVD_STREAM_DATA_CURRENT', 'DVD_TITLE_MENU',
    'AM_GETDECODERCAP_QUERY_EVR_SUPPORT', 'AnalogVideo_SECAM_Mask', 'VMRGUID',
    'MPEG2_PROGRAM_STREAM_MAP', 'DVD_STREAM_DATA_VTSM', 'DVD_AUDIO_CAPS_SDDS',
    'CDEF_BYPASS_CLASS_MANAGER', 'CDEF_DEVMON_PNP_DEVICE', 'AM_GBF_NOWAIT',
    'MPEG2_PROGRAM_ELEMENTARY_STREAM', 'VMR_SUPPORTED', 'CDEF_CLASS_DEFAULT',
    'KSPROPERTY_SUPPORT_SET', 'MPEG2_PROGRAM_DIRECTORY_PES_PACKET', 'RGNDATA',
    'DVD_AUDIO_CAPS_MPEG2', 'KSPROPERTY_SUPPORT_GET', 'DVD_AUDIO_CAPS_DTS',
    'AM_QUERY_DECODER_DXVA_1_SUPPORT', 'CDEF_MERIT_ABOVE_DO_NOT_USE',
    'AM_QUERY_DECODER_VMR_SUPPORT', 'SUBSTREAM_FILTER_VAL_NONE', 'DVD_DOMAIN',
    '__REQUIRED_RPCNDR_H_VERSION__', 'AM_GETDECODERCAP_QUERY_VMR_SUPPORT',
    'DVD_AUDIO_CAPS_AC3', 'MAX_FILTER_NAME', 'CDEF_DEVMON_SELECTIVE_MASK',
    'CDEF_DEVMON_CMGR_DEVICE', 'AM_QUERY_DECODER_DVD_SUPPORT', 'FILTER_STATE',
    'AM_GBF_NODDSURFACELOCK', 'VMRBITMAP_SRCRECT', 'AMF_AUTOMATICGAIN',
    'DVD_AUDIO_CAPS_LPCM', 'AM_QUERY_DECODER_ATSC_SD_SUPPORT', '_FilterState',
    'AM_GBF_NOTASYNCPOINT', 'AnalogVideo_NTSC_Mask', 'CHARS_IN_GUID',
    'AM_GBF_PREVFRAMESKIPPED', 'DVD_DEFAULT_AUDIO_STREAM', 'VMR_NOTSUPPORTED',
    'DVD_STREAM_DATA_VMGM', 'AM_QUERY_DECODER_ATSC_HD_SUPPORT', 'TVAudioMode',
    '__REQUIRED_RPCSAL_H_VERSION__', 'VMRBITMAP_ENTIREDDS', '_PinDirection',
    'DECODER_CAP_SUPPORTED', 'InterleavingMode', 'VMRSurfaceAllocationFlags',
    'tagAMTunerModeType', 'DVD_RELATIVE_BUTTON', 'AM_STREAM_INFO_FLAGS',
    'AM_SEEKING_SEEKING_FLAGS', 'AMTunerModeType', 'tagCameraControlProperty',
    '_AM_FILTER_FLAGS', 'VALID_UOP_FLAG', 'CameraControlFlags', 'DVD_MENU_ID',
    'tagDVD_TITLE_APPMODE', 'DVD_KARAOKE_CONTENTS', 'DVD_TIMECODE_FLAGS',
    'AnalogVideoStandard', 'AM_SEEKING_SEEKING_CAPABILITIES', 'DVD_CMD_FLAGS',
    'AMTunerSubChannel', 'tagDVD_VIDEO_COMPRESSION', 'tagDVD_DISC_SIDE',
    'DVD_PREFERRED_DISPLAY_MODE', 'AM_SEEKING_SeekingCapabilities', 'PDVINFO',
    'tagPhysicalConnectorType', 'AMTunerSignalStrength', 'AM_FILESINK_FLAGS',
    'AMTVAudioEventType', 'DVD_OPTION_FLAG', 'DVD_VIDEO_COMPRESSION',
    '__MIDL___MIDL_itf_strmif_0000_0132_0002', 'tagAMTunerSubChannel',
    'tagVideoProcAmpFlags', 'VfwCaptureDialogs', 'tagQualityMessageType',
    'tagDVD_SUBPICTURE_LANG_EXT', 'DVD_KARAOKE_DOWNMIX', 'tagDVD_FRAMERATE',
    'tagCameraControlFlags', 'VideoProcAmpFlags', 'PhysicalConnectorType',
    'tagDVD_AUDIO_LANG_EXT', 'AM_DVD_GRAPH_FLAGS', 'VMRMixerPrefs', 'Quality',
    'AMTunerEventType', 'VideoControlFlags', 'tagDVD_NavCmdType', 'REGFILTER',
    '_AM_DVD_STREAM_FLAGS', 'tagTVAudioMode', 'VIDEOENCODER_BITRATE_MODE',
    'tagVideoProcAmpProperty', 'tagDVD_AUDIO_APPMODE', '_DECIMATION_USAGE',
    'DVD_KARAOKE_ASSIGNMENT', 'DVD_FRAMERATE', 'CameraControlProperty',
    'DECIMATION_USAGE', 'tagVideoControlFlags', 'DVD_NavCmdType', 'PIN_INFO',
    'AM_FILTER_FLAGS', 'AM_SEEKING_SeekingFlags', 'DVD_AUDIO_APPMODE',
    'tagDVD_SUBPICTURE_TYPE', 'tagDVD_MENU_ID', 'tagAMTunerEventType',
    'VideoCopyProtectionType', 'VMRDeINTerlacePrefs', 'tagDVD_DOMAIN',
    'AM_GRAPH_CONFIG_RECONNECT_FLAGS', 'tagDVD_AUDIO_FORMAT', 'PIN_DIRECTION',
    'AM_DVD_STREAM_FLAGS', 'CompressionCaps', '_AM_DVD_GRAPH_FLAGS',
    'tagAMTunerSignalStrength', 'VMRPresentationFlags', 'TunerInputType',
    'DVD_AUDIO_FORMAT', 'tagTunerInputType', 'VMR_ASPECT_RATIO_MODE',
    'tagDVD_KARAOKE_ASSIGNMENT', 'VMRRenderPrefs', 'VMRDeINTerlaceTech',
    'DVD_SUBPICTURE_CODING', 'QualityMessageType', 'DVD_PARENTAL_LEVEL',
    '__MIDL___MIDL_itf_strmif_0000_0132_0001', 'VfwCompressDialogs',
    '__MIDL___MIDL_itf_strmif_0000_0132_0003', 'tagDVD_KARAOKE_CONTENTS',
    '__MIDL___MIDL_itf_strmif_0000_0132_0004', 'tagDVD_PARENTAL_LEVEL',
    'DVD_AUDIO_LANG_EXT', 'tagDVD_KARAOKE_DOWNMIX', 'VideoProcAmpProperty',
    'AMPROPERTY_PIN', '_AM_GRAPH_CONFIG_RECONNECT_FLAGS', 'DVD_TITLE_APPMODE',
    'DVD_SUBPICTURE_LANG_EXT', 'DVD_SUBPICTURE_TYPE', 'tagDVD_TIMECODE_FLAGS',
    'tagDVD_SUBPICTURE_CODING', 'tagAnalogVideoStandard', 'DVD_DISC_SIDE',
    'tagDVD_PREFERRED_DISPLAY_MODE', 'tagAMTVAudioEventType', 'VMRVideoDesc',
    'IID_IAMFilterGraphCallback', 'AM_SAMPLE2_PROPERTIES', 'tagDVD_MUA_Coeff',
    '_AMCOPPStatusInput', 'AM_DVD_RENDERSTATUS', 'LPAMCOPPStatusOutput',
    'DVD_PLAYBACK_LOCATION2', 'AMCOPPStatusOutput', 'DVD_MUA_MixingInfo',
    '_RGNDATAHEADER', 'AM_MEDIA_TYPE', 'tagVMRPRESENTATIONINFO', 'DDCOLORKEY',
    'tagTIMECODE_SAMPLE', 'RGNDATAHEADER', 'VMRPRESENTATIONINFO', 'COLORKEY',
    'REGPINMEDIUM', 'TIMECODE_SAMPLE', 'DVD_SubpictureAttributes', 'TIMECODE',
    'tagDVD_MultichannelAudioAttributes', 'tagDVD_HMSF_TIMECODE', '_RGNDATA',
    'tagVMRALLOCATIONINFO', '_NORMALIZEDRECT', '_AMMediaType', 'tagCOLORKEY',
    'tagDVD_AudioAttributes', 'VIDEO_STREAM_CONFIG_CAPS', 'PNORMALIZEDRECT',
    'tagDVD_VideoAttributes', 'NORMALIZEDRECT', 'DVD_AudioAttributes',
    '__MIDL___MIDL_itf_strmif_0000_0138_0001', '_VMRDeINTerlaceCaps',
    'DVD_KaraokeAttributes', 'DVD_HMSF_TIMECODE', 'DVD_MenuAttributes',
    'tagVMRGUID', 'tagAM_SAMPLE2_PROPERTIES', '_VMRVideoDesc', 'FILTER_INFO',
    'tagDVD_TitleMainAttributes', 'VMRDeINTerlaceCaps', 'tagDVD_DECODER_CAPS',
    'ALLOCATOR_PROPERTIES', 'LPAMCOPPCommand', 'DVD_DECODER_CAPS', '_PinInfo',
    '_AMCOPPStatusOutput', '_VMRALPHABITMAP', 'tagDVD_SubpictureAttributes',
    'tagDVD_MenuAttributes', '_VMRVIDEOSTREAMINFO', 'VMRVIDEOSTREAMINFO',
    'VMRALPHABITMAP', 'DVD_MUA_Coeff', 'DVD_MultichannelAudioAttributes',
    'STREAM_ID_MAP', 'LPAMCOPPStatusInput', 'AM_STREAM_INFO', '_FilterInfo',
    'PVMRALPHABITMAP', '_VIDEO_STREAM_CONFIG_CAPS', 'CodecAPIEventData',
    'tagDVD_KaraokeAttributes', 'VMRFrequency', 'VMRALLOCATIONINFO',
    'REGFILTERPINS2', 'DVD_TitleAttributes', 'DVD_VideoAttributes', 'REFTIME',
    'tagTIMECODE', 'AMCOPPStatusInput', 'REGPINTYPES', 'tagVMRMONITORINFO',
    'tagDVD_PLAYBACK_LOCATION', '_AMCOPPCommand', 'tagQuality', 'REGFILTER2',
    'tagDVD_TIMECODE', 'tagDVD_PLAYBACK_LOCATION2', 'tagDVD_MUA_MixingInfo',
    'AMCOPPCommand', 'VMRMONITORINFO', 'DVD_PLAYBACK_LOCATION', 'tagDVD_ATR',
    '_AMCOPPSignature', '_AUDIO_STREAM_CONFIG_CAPS', 'REGFILTERPINS',
    '_VMRFrequency', '_AllocatorProperties', 'DVD_TIMECODE', '_timecode',
    'AUDIO_STREAM_CONFIG_CAPS', 'AMCOPPSignature', 'PMEDIASAMPLE2', 'PFILTER',
    'LPDDPIXELFORMAT', 'PENUMREGFILTERS', 'PAMDEVMEMORYALLOCATOR', 'POVERLAY',
    'PAMPHYSICALPININFO', 'PREFERENCECLOCK2', 'HSEMAPHORE', 'PFILTERGRAPH',
    'PFILESINKFILTER2', 'POVERLAYNOTIFY2', 'LPMEDIAPROPERTYBAG', 'PEXTDEVICE',
    'PIAMEXTTRANSPORT', 'PMEDIASEEKING', 'PFILTERFILESOURCE', 'PENUMFILTERS',
    'PQUALITYCONTROL', 'PAMDEVMEMORYCONTROL', 'PMEMINPUTPIN', 'PAMOVIESETUP',
    'PAMSTREAMSELECT', 'PREFERENCECLOCK', 'POVERLAYNOTIFY', 'DVD_REGISTER',
    'PIAMTIMECODEGENERATOR', 'LPPERSISTMEDIAPROPERTYBAG', 'PTIMECODE',
    'LPDIRECTDRAWSURFACE7', 'PMEDIAFILTER', 'LPDIRECTDRAW7', 'PMEDIASAMPLE',
    'PENUMMEDIATYPES', 'PIAMTIMECODEDISPLAY', 'PTIMECODE_SAMPLE', 'PENUMPINS',
    'LPDDCOLORKEY', 'PIAMTIMECODEREADER', 'PMEDIAEVENTSINK', 'PMEMALLOCATOR',
    'LPBITMAPINFOHEADER', 'VALID_UOP_SOMTHING_OR_OTHER', 'PFILTERFILESINK',
)
