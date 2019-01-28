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
__evr_h__ = None
__IMFVideoPositionMapper_FWD_DEFINED__ = None
__IMFVideoDeviceID_FWD_DEFINED__ = None
__IMFVideoDisplayControl_FWD_DEFINED__ = None
__IMFVideoPresenter_FWD_DEFINED__ = None
__IMFDesiredSample_FWD_DEFINED__ = None
__IMFVideoMixerControl_FWD_DEFINED__ = None
__IMFVideoMixerControl2_FWD_DEFINED__ = None
__IMFVideoRenderer_FWD_DEFINED__ = None
__IEVRFilterConfig_FWD_DEFINED__ = None
__IEVRFilterConfigEx_FWD_DEFINED__ = None
__IMFTopologyServiceLookup_FWD_DEFINED__ = None
__IMFTopologyServiceLookupClient_FWD_DEFINED__ = None
__IEVRTrustedVideoPlugin_FWD_DEFINED__ = None
__IMFVideoPositionMapper_INTERFACE_DEFINED__ = None
__IMFVideoDeviceID_INTERFACE_DEFINED__ = None
_MFVideoNormalizedRect_ = None
__IMFVideoDisplayControl_INTERFACE_DEFINED__ = None
__IMFVideoPresenter_INTERFACE_DEFINED__ = None
__IMFDesiredSample_INTERFACE_DEFINED__ = None
__IMFVideoMixerControl_INTERFACE_DEFINED__ = None
__IMFVideoMixerControl2_INTERFACE_DEFINED__ = None
__IMFVideoRenderer_INTERFACE_DEFINED__ = None
__IEVRFilterConfig_INTERFACE_DEFINED__ = None
__IEVRFilterConfigEx_INTERFACE_DEFINED__ = None
__IMFTopologyServiceLookup_INTERFACE_DEFINED__ = None
__IMFTopologyServiceLookupClient_INTERFACE_DEFINED__ = None
__IEVRTrustedVideoPlugin_INTERFACE_DEFINED__ = None
MFEVRDLL = None


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


if not defined(__evr_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IMFVideoPositionMapper_FWD_DEFINED__):
        class IMFVideoPositionMapper(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoPositionMapper_FWD_DEFINED__

    if not defined(__IMFVideoDeviceID_FWD_DEFINED__):
        class IMFVideoDeviceID(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoDeviceID_FWD_DEFINED__

    if not defined(__IMFVideoDisplayControl_FWD_DEFINED__):
        class IMFVideoDisplayControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoDisplayControl_FWD_DEFINED__

    if not defined(__IMFVideoPresenter_FWD_DEFINED__):
        class IMFVideoPresenter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoPresenter_FWD_DEFINED__

    if not defined(__IMFDesiredSample_FWD_DEFINED__):
        class IMFDesiredSample(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFDesiredSample_FWD_DEFINED__

    if not defined(__IMFVideoMixerControl_FWD_DEFINED__):
        class IMFVideoMixerControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoMixerControl_FWD_DEFINED__

    if not defined(__IMFVideoMixerControl2_FWD_DEFINED__):
        class IMFVideoMixerControl2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoMixerControl2_FWD_DEFINED__

    if not defined(__IMFVideoRenderer_FWD_DEFINED__):
        class IMFVideoRenderer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFVideoRenderer_FWD_DEFINED__

    if not defined(__IEVRFilterConfig_FWD_DEFINED__):
        class IEVRFilterConfig(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEVRFilterConfig_FWD_DEFINED__

    if not defined(__IEVRFilterConfigEx_FWD_DEFINED__):
        class IEVRFilterConfigEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEVRFilterConfigEx_FWD_DEFINED__

    if not defined(__IMFTopologyServiceLookup_FWD_DEFINED__):
        class IMFTopologyServiceLookup(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTopologyServiceLookup_FWD_DEFINED__

    if not defined(__IMFTopologyServiceLookupClient_FWD_DEFINED__):
        class IMFTopologyServiceLookupClient(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFTopologyServiceLookupClient_FWD_DEFINED__

    if not defined(__IEVRTrustedVideoPlugin_FWD_DEFINED__):
        class IEVRTrustedVideoPlugin(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEVRTrustedVideoPlugin_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwn_h import * # NOQA
    from pyWinAPI.um.propidl_h import * # NOQA
    from pyWinAPI.um.mfidl_h import * # NOQA
    from pyWinAPI.um.strmif_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_evr_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__midl):
            class _D3DFORMAT(ENUM):
                D3DFMT_UNKNOWN = 0
                D3DFMT_R8G8B8 = 20
                D3DFMT_A8R8G8B8 = 21
                D3DFMT_X8R8G8B8 = 22
                D3DFMT_R5G6B5 = 23
                D3DFMT_X1R5G5B5 = 24
                D3DFMT_A1R5G5B5 = 25
                D3DFMT_A4R4G4B4 = 26
                D3DFMT_R3G3B2 = 27
                D3DFMT_A8 = 28
                D3DFMT_A8R3G3B2 = 29
                D3DFMT_X4R4G4B4 = 30
                D3DFMT_A2B10G10R10 = 31
                D3DFMT_G16R16 = 34
                D3DFMT_A8P8 = 40
                D3DFMT_P8 = 41
                D3DFMT_L8 = 50
                D3DFMT_A8L8 = 51
                D3DFMT_A4L4 = 52
                D3DFMT_V8U8 = 60
                D3DFMT_L6V5U5 = 61
                D3DFMT_X8L8V8U8 = 62
                D3DFMT_Q8W8V8U8 = 63
                D3DFMT_V16U16 = 64
                D3DFMT_W11V11U10 = 65
                D3DFMT_A2W10V10U10 = 67
                D3DFMT_D16_LOCKABLE = 70
                D3DFMT_D32 = 71
                D3DFMT_D15S1 = 73
                D3DFMT_D24S8 = 75
                D3DFMT_D16 = 80
                D3DFMT_D24X8 = 77
                D3DFMT_D24X4S4 = 79
                D3DFMT_VERTEXDATA = 100
                D3DFMT_INDEX16 = 101
                D3DFMT_INDEX32 = 102
                D3DFMT_FORCE_DWORD = 0x7FFFFFFF

            D3DFORMAT = _D3DFORMAT
        # END IF   __midl

        MR_VIDEO_RENDER_SERVICE = DEFINE_GUID(
            0x1092A86C,
            0xAB1A,
            0x459A,
            0xA3,
            0x36,
            0x83,
            0x1F,
            0xBC,
            0x4D,
            0x11,
            0xFF
        )
        MR_VIDEO_MIXER_SERVICE = DEFINE_GUID(
            0x73CD2FC,
            0x6CF4,
            0x40B7,
            0x88,
            0x59,
            0xE8,
            0x95,
            0x52,
            0xC8,
            0x41,
            0xF8
        )
        MR_VIDEO_ACCELERATION_SERVICE = DEFINE_GUID(
            0xEFEF5175,
            0x5C7D,
            0x4CE2,
            0xBB,
            0xBD,
            0x34,
            0xFF,
            0x8B,
            0xCA,
            0x65,
            0x54
        )
        MR_BUFFER_SERVICE = DEFINE_GUID(
            0xA562248C,
            0x9AC6,
            0x4FFC,
            0x9F,
            0xBA,
            0x3A,
            0xF8,
            0xF8,
            0xAD,
            0x1A,
            0x4D
        )
        VIDEO_ZOOM_RECT = DEFINE_GUID(
            0x7AAA1638,
            0x1B7F,
            0x4C93,
            0xBD,
            0x89,
            0x5B,
            0x9C,
            0x9F,
            0xB6,
            0xFC,
            0xF0
        )
        if not defined(__IMFVideoPositionMapper_INTERFACE_DEFINED__):
            # interface IMFVideoPositionMapper
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoPositionMapper = MIDL_INTERFACE(
                    "{1F6A9F17-E70B-4E24-8AE4-0B2C3BA7A4AE}"
                )
                IMFVideoPositionMapper._iid_ = IID_IMFVideoPositionMapper

                IMFVideoPositionMapper._methods_ = [
                    COMMETHOD(
                        [helpstring('Method MapOutputCoordinateToInputStream')],
                        HRESULT,
                        'MapOutputCoordinateToInputStream',
                        (['in'], FLOAT, 'xOut'),
                        (['in'], FLOAT, 'yOut'),
                        (['in'], DWORD, 'dwOutputStreamIndex'),
                        (['in'], DWORD, 'dwInputStreamIndex'),
                        (['out'], POINTER(FLOAT), 'pxIn'),
                        (['out'], POINTER(FLOAT), 'pyIn'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoPositionMapper_INTERFACE_DEFINED__

        if not defined(__IMFVideoDeviceID_INTERFACE_DEFINED__):
            # interface IMFVideoDeviceID
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoDeviceID = MIDL_INTERFACE(
                    "{A38D9567-5A9C-4F3C-B293-8EB415B279BA}"
                )
                IMFVideoDeviceID._iid_ = IID_IMFVideoDeviceID

                IMFVideoDeviceID._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetDeviceID')],
                        HRESULT,
                        'GetDeviceID',
                        (['out'], POINTER(IID), 'pDeviceID'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoDeviceID_INTERFACE_DEFINED__

        # interface __MIDL_itf_evr_0000_0002
        # [local]
        class MFVideoAspectRatioMode(ENUM):
            MFVideoARMode_None = 0
            MFVideoARMode_PreservePicture = 0x1
            MFVideoARMode_PreservePixel = 0x2
            MFVideoARMode_NonLinearStretch = 0x4
            MFVideoARMode_Mask = 0x7


        class MFVideoRenderPrefs(ENUM):
            MFVideoRenderPrefs_DoNotRenderBorder = 0x1
            MFVideoRenderPrefs_DoNotClipToDevice = 0x2
            MFVideoRenderPrefs_AllowOutputThrottling = 0x4
            MFVideoRenderPrefs_ForceOutputThrottling = 0x8
            MFVideoRenderPrefs_ForceBatching = 0x10
            MFVideoRenderPrefs_AllowBatching = 0x20
            MFVideoRenderPrefs_ForceScaling = 0x40
            MFVideoRenderPrefs_AllowScaling = 0x80
            MFVideoRenderPrefs_DoNotRepaintOnStop = 0x100
            MFVideoRenderPrefs_Mask = 0x1FF

        if not defined(_MFVideoNormalizedRect_):
            MFVideoNormalizedRect._fields_ = [
                ('left', FLOAT),
                ('top', FLOAT),
                ('right', FLOAT),
                ('bottom', FLOAT),
            ]
        # END IF

        if not defined(__IMFVideoDisplayControl_INTERFACE_DEFINED__):
            # interface IMFVideoDisplayControl
            # [helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoDisplayControl = MIDL_INTERFACE(
                    "{A490B1E4-AB84-4D31-A1B2-181E03B1077A}"
                )
                IMFVideoDisplayControl._iid_ = IID_IMFVideoDisplayControl

                IMFVideoDisplayControl._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetNativeVideoSize')],
                        HRESULT,
                        'GetNativeVideoSize',
                        (['in', 'out', 'unique'], POINTER(SIZE), 'pszVideo'),
                        (
                            ['out', 'unique', 'in'],
                            POINTER(SIZE),
                            'pszARVideo'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetIdealVideoSize')],
                        HRESULT,
                        'GetIdealVideoSize',
                        (['unique', 'out', 'in'], POINTER(SIZE), 'pszMin'),
                        (['out', 'in', 'unique'], POINTER(SIZE), 'pszMax'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVideoPosition')],
                        HRESULT,
                        'SetVideoPosition',
                        (
                            ['unique', 'in'],
                            POINTER(MFVideoNormalizedRect),
                            'pnrcSource'
                        ),
                        (['unique', 'in'], LPRECT, 'prcDest'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVideoPosition')],
                        HRESULT,
                        'GetVideoPosition',
                        (
                            ['out'],
                            POINTER(MFVideoNormalizedRect),
                            'pnrcSource'
                        ),
                        (['out'], LPRECT, 'prcDest'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetAspectRatioMode')],
                        HRESULT,
                        'SetAspectRatioMode',
                        (['in'], DWORD, 'dwAspectRatioMode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAspectRatioMode')],
                        HRESULT,
                        'GetAspectRatioMode',
                        (['out'], POINTER(DWORD), 'pdwAspectRatioMode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVideoWindow')],
                        HRESULT,
                        'SetVideoWindow',
                        (['in'], HWND, 'hwndVideo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVideoWindow')],
                        HRESULT,
                        'GetVideoWindow',
                        (['out'], POINTER(HWND), 'phwndVideo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RepaintVideo')],
                        HRESULT,
                        'RepaintVideo',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCurrentImage')],
                        HRESULT,
                        'GetCurrentImage',
                        (['out', 'in'], POINTER(BITMAPINFOHEADER), 'pBih'),
                        (['out'], POINTER(POINTER(BYTE)), 'pDib'),
                        (['out'], POINTER(DWORD), 'pcbDib'),
                        (
                            ['unique', 'in', 'out'],
                            POINTER(LONGLONG),
                            'pTimeStamp'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetBorderColor')],
                        HRESULT,
                        'SetBorderColor',
                        (['in'], COLORREF, 'Clr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetBorderColor')],
                        HRESULT,
                        'GetBorderColor',
                        (['out'], POINTER(COLORREF), 'pClr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetRenderingPrefs')],
                        HRESULT,
                        'SetRenderingPrefs',
                        (['in'], DWORD, 'dwRenderFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRenderingPrefs')],
                        HRESULT,
                        'GetRenderingPrefs',
                        (['out'], POINTER(DWORD), 'pdwRenderFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFullscreen')],
                        HRESULT,
                        'SetFullscreen',
                        (['in'], BOOL, 'fFullscreen'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFullscreen')],
                        HRESULT,
                        'GetFullscreen',
                        (['out'], POINTER(BOOL), 'pfFullscreen'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoDisplayControl_INTERFACE_DEFINED__

        # interface __MIDL_itf_evr_0000_0003
        # [local]
        class MFVP_MESSAGE_TYPE(ENUM):
            MFVP_MESSAGE_FLUSH = 0
            MFVP_MESSAGE_INVALIDATEMEDIATYPE = 0x1
            MFVP_MESSAGE_PROCESSINPUTNOTIFY = 0x2
            MFVP_MESSAGE_BEGINSTREAMING = 0x3
            MFVP_MESSAGE_ENDSTREAMING = 0x4
            MFVP_MESSAGE_ENDOFSTREAM = 0x5
            MFVP_MESSAGE_STEP = 0x6
            MFVP_MESSAGE_CANCELSTEP = 0x7

        if not defined(__IMFVideoPresenter_INTERFACE_DEFINED__):
            # interface IMFVideoPresenter
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoPresenter = MIDL_INTERFACE(
                    "{29AFF080-182A-4A5D-AF3B-448F3A6346CB}"
                )
                IMFVideoPresenter._iid_ = IID_IMFVideoPresenter

                IMFVideoPresenter._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ProcessMessage')],
                        HRESULT,
                        'ProcessMessage',
                        ([], MFVP_MESSAGE_TYPE, 'eMessage'),
                        ([], ULONG_PTR, 'ulParam'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCurrentMediaType')],
                        HRESULT,
                        'GetCurrentMediaType',
                        (
                            ['out'],
                            POINTER(POINTER(IMFVideoMediaType)),
                            'ppMediaType'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoPresenter_INTERFACE_DEFINED__

        if not defined(__IMFDesiredSample_INTERFACE_DEFINED__):
            # interface IMFDesiredSample
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFDesiredSample = MIDL_INTERFACE(
                    "{56C294D0-753E-4260-8D61-A3D8820B1D54}"
                )
                IMFDesiredSample._iid_ = IID_IMFDesiredSample

                IMFDesiredSample._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetDesiredSampleTimeAndDuration')],
                        HRESULT,
                        'GetDesiredSampleTimeAndDuration',
                        (['out'], POINTER(LONGLONG), 'phnsSampleTime'),
                        (['out'], POINTER(LONGLONG), 'phnsSampleDuration'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetDesiredSampleTimeAndDuration')],
                        VOID,
                        'SetDesiredSampleTimeAndDuration',
                        (['in'], LONGLONG, 'hnsSampleTime'),
                        (['in'], LONGLONG, 'hnsSampleDuration'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Clear')],
                        VOID,
                        'Clear',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFDesiredSample_INTERFACE_DEFINED__

        if not defined(__IMFVideoMixerControl_INTERFACE_DEFINED__):
            # interface IMFVideoMixerControl
            # [helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoMixerControl = MIDL_INTERFACE(
                    "{A5C6C53F-C202-4AA5-9695-175BA8C508A5}"
                )
                IMFVideoMixerControl._iid_ = IID_IMFVideoMixerControl

                IMFVideoMixerControl._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetStreamZOrder')],
                        HRESULT,
                        'SetStreamZOrder',
                        (['in'], DWORD, 'dwStreamID'),
                        (['in'], DWORD, 'dwZ'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamZOrder')],
                        HRESULT,
                        'GetStreamZOrder',
                        (['in'], DWORD, 'dwStreamID'),
                        (['out'], POINTER(DWORD), 'pdwZ'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetStreamOutputRect')],
                        HRESULT,
                        'SetStreamOutputRect',
                        (['in'], DWORD, 'dwStreamID'),
                        (
                            ['in'],
                            POINTER(MFVideoNormalizedRect),
                            'pnrcOutput'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetStreamOutputRect')],
                        HRESULT,
                        'GetStreamOutputRect',
                        (['in'], DWORD, 'dwStreamID'),
                        (
                            ['out'],
                            POINTER(MFVideoNormalizedRect),
                            'pnrcOutput'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoMixerControl_INTERFACE_DEFINED__

        # interface __MIDL_itf_evr_0000_0006
        # [local]
        class _MFVideoMixPrefs(ENUM):
            MFVideoMixPrefs_ForceHalfInterlace = 0x1
            MFVideoMixPrefs_AllowDropToHalfInterlace = 0x2
            MFVideoMixPrefs_AllowDropToBob = 0x4
            MFVideoMixPrefs_ForceBob = 0x8
            MFVideoMixPrefs_EnableRotation = 0x10
            MFVideoMixPrefs_Mask = 0x1F

        MFVideoMixPrefs = _MFVideoMixPrefs
        if not defined(__IMFVideoMixerControl2_INTERFACE_DEFINED__):
            # interface IMFVideoMixerControl2
            # [helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoMixerControl2 = MIDL_INTERFACE(
                    "{8459616D-966E-4930-B658-54FA7E5A16D3}"
                )
                IMFVideoMixerControl2._iid_ = IID_IMFVideoMixerControl2

                IMFVideoMixerControl2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetMixingPrefs')],
                        HRESULT,
                        'SetMixingPrefs',
                        (['in'], DWORD, 'dwMixFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMixingPrefs')],
                        HRESULT,
                        'GetMixingPrefs',
                        (['out'], POINTER(DWORD), 'pdwMixFlags'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoMixerControl2_INTERFACE_DEFINED__

        if not defined(__IMFVideoRenderer_INTERFACE_DEFINED__):
            # interface IMFVideoRenderer
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFVideoRenderer = MIDL_INTERFACE(
                    "{DFDFD197-A9CA-43D8-B341-6AF3503792CD}"
                )
                IMFVideoRenderer._iid_ = IID_IMFVideoRenderer

                IMFVideoRenderer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InitializeRenderer')],
                        HRESULT,
                        'InitializeRenderer',
                        (['in'], POINTER(IMFTransform), 'pVideoMixer'),
                        (
                            ['in'],
                            POINTER(IMFVideoPresenter),
                            'pVideoPresenter'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFVideoRenderer_INTERFACE_DEFINED__

        if not defined(__IEVRFilterConfig_INTERFACE_DEFINED__):
            # interface IEVRFilterConfig
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEVRFilterConfig = MIDL_INTERFACE(
                    "{83E91E85-82C1-4EA7-801D-85DC50B75086}"
                )
                IEVRFilterConfig._iid_ = IID_IEVRFilterConfig

                IEVRFilterConfig._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetNumberOfStreams')],
                        HRESULT,
                        'SetNumberOfStreams',
                        (['in'], DWORD, 'dwMaxStreams'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNumberOfStreams')],
                        HRESULT,
                        'GetNumberOfStreams',
                        (['out'], POINTER(DWORD), 'pdwMaxStreams'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEVRFilterConfig_INTERFACE_DEFINED__

        # interface __MIDL_itf_evr_0000_0009
        # [local]
        class _EVRFilterConfig_Prefs(ENUM):
            EVRFilterConfigPrefs_EnableQoS = 0x1
            EVRFilterConfigPrefs_Mask = 0x1

        EVRFilterConfigPrefs = _EVRFilterConfig_Prefs
        if not defined(__IEVRFilterConfigEx_INTERFACE_DEFINED__):
            # interface IEVRFilterConfigEx
            # [helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEVRFilterConfigEx = MIDL_INTERFACE(
                    "{AEA36028-796D-454F-BEEE-B48071E24304}"
                )
                IEVRFilterConfigEx._iid_ = IID_IEVRFilterConfigEx

                IEVRFilterConfigEx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetConfigPrefs')],
                        HRESULT,
                        'SetConfigPrefs',
                        (['in'], DWORD, 'dwConfigFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetConfigPrefs')],
                        HRESULT,
                        'GetConfigPrefs',
                        (['out'], POINTER(DWORD), 'pdwConfigFlags'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEVRFilterConfigEx_INTERFACE_DEFINED__

        # interface __MIDL_itf_evr_0000_0010
        # [local]
        class _MF_SERVICE_LOOKUP_TYPE(ENUM):
            MF_SERVICE_LOOKUP_UPSTREAM = 0
            MF_SERVICE_LOOKUP_UPSTREAM_DIRECT = MF_SERVICE_LOOKUP_UPSTREAM + 1
            MF_SERVICE_LOOKUP_DOWNSTREAM = (
                MF_SERVICE_LOOKUP_UPSTREAM_DIRECT + 1
            )
            MF_SERVICE_LOOKUP_DOWNSTREAM_DIRECT = (
                MF_SERVICE_LOOKUP_DOWNSTREAM + 1
            )
            MF_SERVICE_LOOKUP_ALL = MF_SERVICE_LOOKUP_DOWNSTREAM_DIRECT + 1
            MF_SERVICE_LOOKUP_GLOBAL = MF_SERVICE_LOOKUP_ALL + 1

        MF_SERVICE_LOOKUP_TYPE = _MF_SERVICE_LOOKUP_TYPE
        if not defined(__IMFTopologyServiceLookup_INTERFACE_DEFINED__):
            # interface IMFTopologyServiceLookup
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTopologyServiceLookup = MIDL_INTERFACE(
                    "{FA993889-4383-415A-A930-DD472A8CF6F7}"
                )
                IMFTopologyServiceLookup._iid_ = IID_IMFTopologyServiceLookup

                IMFTopologyServiceLookup._methods_ = [
                    COMMETHOD(
                        [helpstring('Method LookupService')],
                        HRESULT,
                        'LookupService',
                        (['in'], MF_SERVICE_LOOKUP_TYPE, 'Type'),
                        (['in'], DWORD, 'dwIndex'),
                        (['in'], REFGUID, 'guidService'),
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(LPVOID), 'ppvObjects'),
                        (['out', 'in'], POINTER(DWORD), 'pnObjects'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTopologyServiceLookup_INTERFACE_DEFINED__

        if not defined(__IMFTopologyServiceLookupClient_INTERFACE_DEFINED__):
            # interface IMFTopologyServiceLookupClient
            # [uuid][object][local]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFTopologyServiceLookupClient = MIDL_INTERFACE(
                    "{FA99388A-4383-415A-A930-DD472A8CF6F7}"
                )
                IMFTopologyServiceLookupClient._iid_ = IID_IMFTopologyServiceLookupClient

                IMFTopologyServiceLookupClient._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InitServicePointers')],
                        HRESULT,
                        'InitServicePointers',
                        (
                            ['in'],
                            POINTER(IMFTopologyServiceLookup),
                            'pLookup'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseServicePointers')],
                        HRESULT,
                        'ReleaseServicePointers',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFTopologyServiceLookupClient_INTERFACE_DEFINED__

        if not defined(__IEVRTrustedVideoPlugin_INTERFACE_DEFINED__):
            # interface IEVRTrustedVideoPlugin
            # [local][helpstring][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEVRTrustedVideoPlugin = MIDL_INTERFACE(
                    "{83A4CE40-7710-494B-A893-A472049AF630}"
                )
                IEVRTrustedVideoPlugin._iid_ = IID_IEVRTrustedVideoPlugin

                IEVRTrustedVideoPlugin._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsInTrustedVideoMode')],
                        HRESULT,
                        'IsInTrustedVideoMode',
                        (['out'], POINTER(BOOL), 'pYes'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanConstrict')],
                        HRESULT,
                        'CanConstrict',
                        (['out'], POINTER(BOOL), 'pYes'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetConstriction')],
                        HRESULT,
                        'SetConstriction',
                        ([], DWORD, 'dwKPix'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DisableImageExport')],
                        HRESULT,
                        'DisableImageExport',
                        ([], BOOL, 'bDisable'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEVRTrustedVideoPlugin_INTERFACE_DEFINED__

        # interface __MIDL_itf_evr_0000_0013
        # [local]
        if not defined(MFEVRDLL):
            pass
        # END IF

        if MFEVRDLL:
            pass
        else:
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    ole32 = ctypes.windll.OLE32

    # ULONG HWND_UserSize(
    # __RPC__in ULONG *,
    # ULONG,
    # __RPC__in HWND *
    # );
    HWND_UserSize = ole32.HWND_UserSize
    HWND_UserSize.restype = ULONG

    # UCHAR * HWND_UserMarshal(
    # __RPC__in ULONG *,
    # __RPC__inout_xcount(0) UCHAR *,
    # __RPC__in HWND *
    # );
    HWND_UserMarshal = ole32.HWND_UserMarshal
    HWND_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * HWND_UserUnmarshal(
    # __RPC__in ULONG *,
    # __RPC__in_xcount(0) UCHAR *,
    # __RPC__out HWND *
    # );
    HWND_UserUnmarshal = ole32.HWND_UserUnmarshal
    HWND_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID HWND_UserFree(
    # __RPC__in ULONG *,
    # __RPC__in HWND *
    # );
    HWND_UserFree = ole32.HWND_UserFree
    HWND_UserFree.restype = VOID

    # ULONG HWND_UserSize64(
    # __RPC__in ULONG *,
    # ULONG            ,
    # __RPC__in HWND *
    # );
    HWND_UserSize64 = ole32.HWND_UserSize64
    HWND_UserSize64.restype = ULONG

    # UCHAR *HWND_UserMarshal64(
    # __RPC__in ULONG *,
    # __RPC__inout_xcount(0) UCHAR *,
    # __RPC__in HWND *
    #  );
    HWND_UserMarshal64 = ole32.HWND_UserMarshal64
    HWND_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  HWND_UserUnmarshal64(
    # __RPC__in ULONG *,
    # __RPC__in_xcount(0) UCHAR *,
    # __RPC__out HWND *
    # );
    HWND_UserUnmarshal64 = ole32.HWND_UserUnmarshal64
    HWND_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID HWND_UserFree64(
    # __RPC__in ULONG *,
    # __RPC__in HWND *
    # );
    HWND_UserFree64 = ole32.HWND_UserFree64
    HWND_UserFree64.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


