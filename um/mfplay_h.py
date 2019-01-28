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
__mfplay_h__ = None
__IMFPMediaPlayer_FWD_DEFINED__ = None
__IMFPMediaItem_FWD_DEFINED__ = None
__IMFPMediaPlayerCallback_FWD_DEFINED__ = None
__IMFPMediaPlayer_INTERFACE_DEFINED__ = None
__IMFPMediaItem_INTERFACE_DEFINED__ = None
__IMFPMediaPlayerCallback_INTERFACE_DEFINED__ = None


class MFP_EVENT_HEADER(ctypes.Structure):
    pass


class MFP_PLAY_EVENT(ctypes.Structure):
    pass


class MFP_PAUSE_EVENT(ctypes.Structure):
    pass


class MFP_STOP_EVENT(ctypes.Structure):
    pass


class MFP_POSITION_SET_EVENT(ctypes.Structure):
    pass


class MFP_RATE_SET_EVENT(ctypes.Structure):
    pass


class MFP_MEDIAITEM_CREATED_EVENT(ctypes.Structure):
    pass


class MFP_MEDIAITEM_SET_EVENT(ctypes.Structure):
    pass


class MFP_FRAME_STEP_EVENT(ctypes.Structure):
    pass


class MFP_MEDIAITEM_CLEARED_EVENT(ctypes.Structure):
    pass


class MFP_MF_EVENT(ctypes.Structure):
    pass


class MFP_ERROR_EVENT(ctypes.Structure):
    pass


class MFP_PLAYBACK_ENDED_EVENT(ctypes.Structure):
    pass


class MFP_ACQUIRE_USER_CREDENTIAL_EVENT(ctypes.Structure):
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

if not defined(__mfplay_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IMFPMediaPlayer_FWD_DEFINED__):
        class IMFPMediaPlayer(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IMFPMediaPlayer_FWD_DEFINED__

    if not defined(__IMFPMediaItem_FWD_DEFINED__):
        class IMFPMediaItem(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFPMediaItem_FWD_DEFINED__

    if not defined(__IMFPMediaPlayerCallback_FWD_DEFINED__):
        IMFPMediaPlayer._methods_ = [
            COMMETHOD([], HRESULT, 'Play'),
            COMMETHOD([], HRESULT, 'Pause'),
            COMMETHOD([], HRESULT, 'Stop'),
            COMMETHOD([], HRESULT, 'FrameStep'),
            # Position controls
            COMMETHOD(
                [],
                HRESULT,
                'SetPosition',
                ([annotation('_In_'), 'in'], REFGUID, 'guidPositionType'),
                (['in'], POINTER(PROPVARIANT), 'pvPositionValue'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetPosition',
                ([annotation('_In_'), 'in'], REFGUID, 'guidPositionType'),
                (
                    [annotation('_Out_'), 'out'],
                    POINTER(PROPVARIANT),
                    'pvPositionValue'
                ),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetDuration',
                ([annotation('_In_'), 'in'], REFGUID, 'guidPositionType'),
                (
                    [annotation('_Out_'), 'out'],
                    POINTER(PROPVARIANT),
                    'pvDurationValue'
                ),
            ),
            # Rate Control
            COMMETHOD(
                [],
                HRESULT,
                'SetRate',
                ([annotation('_In_'), 'in'], FLOAT, 'flRate'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetRate',
                ([annotation('_Out_'), 'out'], POINTER(FLOAT), 'pflRate'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetSupportedRates',
                ([annotation('_In_'), 'in'], BOOL, 'fForwardDirection'),
                (
                    ['out', annotation('_Out_')],
                    POINTER(FLOAT),
                    'pflSlowestRate'
                ),
                (['in'], POINTER(FLOAT), 'pflFastestRate'),
            ),
            # State
            COMMETHOD(
                [],
                HRESULT,
                'GetState',
                (
                    ['out', annotation('_Out_')],
                    POINTER(MFP_MEDIAPLAYER_STATE),
                    'peState'
                ),
            ),
            # Media Item Management
            COMMETHOD(
                [],
                HRESULT,
                'CreateMediaItemFromURL',
                ([annotation('_In_'), 'in'], LPCWSTR, 'pwszURL'),
                (['in'], BOOL, 'fSync'),
                (['in'], DWORD_PTR, 'dwUserData'),
                (
                    ['out', annotation('_Out_opt_')],
                    POINTER(POINTER(IMFPMediaItem)),
                    'ppMediaItem'
                ),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'CreateMediaItemFromObject',
                (
                    [annotation('_In_'), 'in'],
                    POINTER(comtypes.IUnknown),
                    'pIUnknownObj'
                ),
                (['in'], BOOL, 'fSync'),
                (['in'], DWORD_PTR, 'dwUserData'),
                (
                    ['out', annotation('_Out_opt_')],
                    POINTER(POINTER(IMFPMediaItem)),
                    'ppMediaItem'
                ),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'SetMediaItem',
                (
                    [annotation('_In_'), 'in'],
                    POINTER(IMFPMediaItem),
                    'pIMFPMediaItem'
                ),
            ),
            # Clears the media item from the player and goes to the empty state
            COMMETHOD(
                [],
                HRESULT,
                'ClearMediaItem',
            ),
            # / Fails if no media item is present
            COMMETHOD(
                [],
                HRESULT,
                'GetMediaItem',
                (
                    ['out', annotation('_Out_')],
                    POINTER(POINTER(IMFPMediaItem)),
                    'ppIMFPMediaItem'
                ),
            ),
            # Audio controls
            COMMETHOD(
                [],
                HRESULT,
                'GetVolume',
                (['out', annotation('_Out_')], POINTER(FLOAT), 'pflVolume'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'SetVolume',
                ([annotation('_In_'), 'in'], FLOAT, 'flVolume'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetBalance',
                (['out', annotation('_Out_')], POINTER(FLOAT), 'pflBalance'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'SetBalance',
                ([annotation('_In_'), 'in'], FLOAT, 'flBalance'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetMute',
                ([annotation('_Out_'), 'out'], POINTER(BOOL), 'pfMute'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'SetMute',
                ([annotation('_In_'), 'in'], BOOL, 'fMute'),
            ),
            # Video controls
            # / </summary>
            #
            COMMETHOD(
                [],
                HRESULT,
                'GetNativeVideoSize',
                (['out', annotation('_Out_opt_')], POINTER(SIZE), 'pszVideo'),
                (['in'], POINTER(SIZE), 'pszARVideo'),
            ),
            # / </summary>
            #
            COMMETHOD(
                [],
                HRESULT,
                'GetIdealVideoSize',
                (['out', annotation('_Out_opt_')], POINTER(SIZE), 'pszMin'),
                (['in'], POINTER(SIZE), 'pszMax'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'SetVideoSourceRect',
                (
                    [annotation('_In_'), 'in'],
                    POINTER(MFVideoNormalizedRect),
                    'pnrcSource'
                ),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetVideoSourceRect',
                (
                    ['out', annotation('_Out_')],
                    POINTER(MFVideoNormalizedRect),
                    'pnrcSource'
                ),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'SetAspectRatioMode',
                ([annotation('_In_'), 'in'], DWORD, 'dwAspectRatioMode'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetAspectRatioMode',
                (
                    [annotation('_Out_'), 'out'],
                    POINTER(DWORD),
                    'pdwAspectRatioMode'
                ),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetVideoWindow',
                (['out', annotation('_Out_')], POINTER(HWND), 'phwndVideo'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'UpdateVideo',
            ),
            COMMETHOD(
                [],
                HRESULT,
                'SetBorderColor',
                ([annotation('_In_'), 'in'], COLORREF, 'Clr'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'GetBorderColor',
                (['out', annotation('_Out_')], POINTER(COLORREF), 'pClr'),
            ),
            # Effect Management
            COMMETHOD(
                [],
                HRESULT,
                'InsertEffect',
                (
                    [annotation('_In_'), 'in'],
                    POINTER(comtypes.IUnknown),
                    'pEffect'
                ),
                (['in'], BOOL, 'fOptional'),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'RemoveEffect',
                (
                    [annotation('_In_'), 'in'],
                    POINTER(comtypes.IUnknown),
                    'pEffect'
                ),
            ),
            COMMETHOD(
                [],
                HRESULT,
                'RemoveAllEffects',
            ),
            # Shutdown
            COMMETHOD(
                [],
                HRESULT,
                'Shutdown',
            ),
        ]

    # END IF  __IMFPMediaPlayerCallback_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwn_h import * # NOQA
    from pyWinAPI.um.propsys_h import * # NOQA
    from pyWinAPI.um.mfidl_h import * # NOQA
    from pyWinAPI.um.evr_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfplay_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    mfplay = ctypes.windll.MFPLAY

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if WINVER >= _WIN32_WINNT_WIN7:
            MFP_CREATION_OPTIONS = UINT32


            class _MFP_CREATION_OPTIONS(ENUM):
                MFP_OPTION_NONE = 0
                MFP_OPTION_FREE_THREADED_CALLBACK = 0x1
                MFP_OPTION_NO_MMCSS = 0x2
                MFP_OPTION_NO_REMOTE_DESKTOP_OPTIMIZATION = 0x4


            class MFP_MEDIAPLAYER_STATE(ENUM):
                MFP_MEDIAPLAYER_STATE_EMPTY = 0
                MFP_MEDIAPLAYER_STATE_STOPPED = 0x1
                MFP_MEDIAPLAYER_STATE_PLAYING = 0x2
                MFP_MEDIAPLAYER_STATE_PAUSED = 0x3
                MFP_MEDIAPLAYER_STATE_SHUTDOWN = 0x4

            MFP_MEDIAITEM_CHARACTERISTICS = UINT32


            class _MFP_MEDIAITEM_CHARACTERISTICS(ENUM):
                MFP_MEDIAITEM_IS_LIVE = 0x1
                MFP_MEDIAITEM_CAN_SEEK = 0x2
                MFP_MEDIAITEM_CAN_PAUSE = 0x4
                MFP_MEDIAITEM_HAS_SLOW_SEEK = 0x8

            MFP_CREDENTIAL_FLAGS = UINT32


            class _MFP_CREDENTIAL_FLAGS(ENUM):
                MFP_CREDENTIAL_PROMPT = 0x1
                MFP_CREDENTIAL_SAVE = 0x2
                MFP_CREDENTIAL_DO_NOT_CACHE = 0x4
                MFP_CREDENTIAL_CLEAR_TEXT = 0x8
                MFP_CREDENTIAL_PROXY = 0x10
                MFP_CREDENTIAL_LOGGED_ON_USER = 0x20

            # STDAPI MFPCreateMediaPlayer(
            # _In_opt_  LPCWSTR pwszURL,
            # _In_      BOOL fStartPlayback,
            # _In_opt_  MFP_CREATION_OPTIONS creationOptions,
            # _In_opt_  IMFPMediaPlayerCallback * pCallback,
            # _In_opt_  HWND hWnd,
            # _Out_opt_ IMFPMediaPlayer ** ppMediaPlayer );
            MFPCreateMediaPlayer = mfplay.MFPCreateMediaPlayer

            if not defined(__IMFPMediaPlayer_INTERFACE_DEFINED__):
                # interface IMFPMediaPlayer
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFPMediaPlayer = MIDL_INTERFACE(
                        "{A714590A-58AF-430A-85BF-44F5EC838D85}"
                    )
                    IMFPMediaPlayer._iid_ = IID_IMFPMediaPlayer

                    IMFPMediaPlayer._methods_ = [
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
                            [helpstring('Method Stop')],
                            HRESULT,
                            'Stop',
                        ),
                        COMMETHOD(
                            [helpstring('Method FrameStep')],
                            HRESULT,
                            'FrameStep',
                        ),
                        COMMETHOD(
                            [helpstring('Method SetPosition')],
                            HRESULT,
                            'SetPosition',
                            (['in'], REFGUID, 'guidPositionType'),
                            (['in'], POINTER(PROPVARIANT), 'pvPositionValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPosition')],
                            HRESULT,
                            'GetPosition',
                            (['in'], REFGUID, 'guidPositionType'),
                            (
                                ['out'],
                                POINTER(PROPVARIANT),
                                'pvPositionValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDuration')],
                            HRESULT,
                            'GetDuration',
                            (['in'], REFGUID, 'guidPositionType'),
                            (
                                ['out'],
                                POINTER(PROPVARIANT),
                                'pvDurationValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetRate')],
                            HRESULT,
                            'SetRate',
                            (['in'], FLOAT, 'flRate'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRate')],
                            HRESULT,
                            'GetRate',
                            (['out'], POINTER(FLOAT), 'pflRate'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSupportedRates')],
                            HRESULT,
                            'GetSupportedRates',
                            (['in'], BOOL, 'fForwardDirection'),
                            (['out'], POINTER(FLOAT), 'pflSlowestRate'),
                            (['out'], POINTER(FLOAT), 'pflFastestRate'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetState')],
                            HRESULT,
                            'GetState',
                            (
                                ['out'],
                                POINTER(MFP_MEDIAPLAYER_STATE),
                                'peState'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateMediaItemFromURL')],
                            HRESULT,
                            'CreateMediaItemFromURL',
                            (['in'], LPCWSTR, 'pwszURL'),
                            (['in'], BOOL, 'fSync'),
                            (['in'], DWORD_PTR, 'dwUserData'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFPMediaItem)),
                                'ppMediaItem'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateMediaItemFromObject')],
                            HRESULT,
                            'CreateMediaItemFromObject',
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                                'pIUnknownObj'
                            ),
                            (['in'], BOOL, 'fSync'),
                            (['in'], DWORD_PTR, 'dwUserData'),
                            (
                                ['out'],
                                POINTER(POINTER(IMFPMediaItem)),
                                'ppMediaItem'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetMediaItem')],
                            HRESULT,
                            'SetMediaItem',
                            (
                                ['in'],
                                POINTER(IMFPMediaItem),
                                'pIMFPMediaItem'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ClearMediaItem')],
                            HRESULT,
                            'ClearMediaItem',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMediaItem')],
                            HRESULT,
                            'GetMediaItem',
                            (
                                ['out'],
                                POINTER(POINTER(IMFPMediaItem)),
                                'ppIMFPMediaItem'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVolume')],
                            HRESULT,
                            'GetVolume',
                            (['out'], POINTER(FLOAT), 'pflVolume'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetVolume')],
                            HRESULT,
                            'SetVolume',
                            (['in'], FLOAT, 'flVolume'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBalance')],
                            HRESULT,
                            'GetBalance',
                            (['out'], POINTER(FLOAT), 'pflBalance'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetBalance')],
                            HRESULT,
                            'SetBalance',
                            (['in'], FLOAT, 'flBalance'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMute')],
                            HRESULT,
                            'GetMute',
                            (['out'], POINTER(BOOL), 'pfMute'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetMute')],
                            HRESULT,
                            'SetMute',
                            (['in'], BOOL, 'fMute'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNativeVideoSize')],
                            HRESULT,
                            'GetNativeVideoSize',
                            (['out'], POINTER(SIZE), 'pszVideo'),
                            (['out'], POINTER(SIZE), 'pszARVideo'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetIdealVideoSize')],
                            HRESULT,
                            'GetIdealVideoSize',
                            (['out'], POINTER(SIZE), 'pszMin'),
                            (['out'], POINTER(SIZE), 'pszMax'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetVideoSourceRect')],
                            HRESULT,
                            'SetVideoSourceRect',
                            (
                                ['in'],
                                POINTER(MFVideoNormalizedRect),
                                'pnrcSource'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVideoSourceRect')],
                            HRESULT,
                            'GetVideoSourceRect',
                            (
                                ['out'],
                                POINTER(MFVideoNormalizedRect),
                                'pnrcSource'
                            ),
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
                            [helpstring('Method GetVideoWindow')],
                            HRESULT,
                            'GetVideoWindow',
                            (['out'], POINTER(HWND), 'phwndVideo'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UpdateVideo')],
                            HRESULT,
                            'UpdateVideo',
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
                            [helpstring('Method InsertEffect')],
                            HRESULT,
                            'InsertEffect',
                            (['in'], POINTER(comtypes.IUnknown), 'pEffect'),
                            (['in'], BOOL, 'fOptional'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveEffect')],
                            HRESULT,
                            'RemoveEffect',
                            (['in'], POINTER(comtypes.IUnknown), 'pEffect'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAllEffects')],
                            HRESULT,
                            'RemoveAllEffects',
                        ),
                        COMMETHOD(
                            [helpstring('Method Shutdown')],
                            HRESULT,
                            'Shutdown',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFPMediaPlayer_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfplay_0000_0001
            # [local]
            MFP_POSITIONTYPE_100NS = EXTERN_GUID(
                0x0,
                0x0,
                0x0,
                0x0,
                0x0,
                0x0,
                0x0,
                0x0,
                0x0,
                0x0,
                0x0
            )
            if not defined(__IMFPMediaItem_INTERFACE_DEFINED__):
                # interface IMFPMediaItem
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFPMediaItem = MIDL_INTERFACE(
                        "{90EB3E6B-ECBF-45CC-B1DA-C6FE3EA70D57}"
                    )
                    IMFPMediaItem._iid_ = IID_IMFPMediaItem

                    IMFPMediaItem._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetMediaPlayer')],
                            HRESULT,
                            'GetMediaPlayer',
                            (
                                ['out'],
                                POINTER(POINTER(IMFPMediaPlayer)),
                                'ppMediaPlayer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetURL')],
                            HRESULT,
                            'GetURL',
                            (['out'], POINTER(LPWSTR), 'ppwszURL'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetObject')],
                            HRESULT,
                            'GetObject',
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'ppIUnknown'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetUserData')],
                            HRESULT,
                            'GetUserData',
                            (['out'], POINTER(DWORD_PTR), 'pdwUserData'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetUserData')],
                            HRESULT,
                            'SetUserData',
                            (['in'], DWORD_PTR, 'dwUserData'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStartStopPosition')],
                            HRESULT,
                            'GetStartStopPosition',
                            (
                                ['out'],
                                POINTER(GUID),
                                'pguidStartPositionType'
                            ),
                            (['out'], POINTER(PROPVARIANT), 'pvStartValue'),
                            (['out'], POINTER(GUID), 'pguidStopPositionType'),
                            (['out'], POINTER(PROPVARIANT), 'pvStopValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStartStopPosition')],
                            HRESULT,
                            'SetStartStopPosition',
                            (['in'], POINTER(GUID), 'pguidStartPositionType'),
                            (['in'], POINTER(PROPVARIANT), 'pvStartValue'),
                            (['in'], POINTER(GUID), 'pguidStopPositionType'),
                            (['in'], POINTER(PROPVARIANT), 'pvStopValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method HasVideo')],
                            HRESULT,
                            'HasVideo',
                            (['out'], POINTER(BOOL), 'pfHasVideo'),
                            (['out'], POINTER(BOOL), 'pfSelected'),
                        ),
                        COMMETHOD(
                            [helpstring('Method HasAudio')],
                            HRESULT,
                            'HasAudio',
                            (['out'], POINTER(BOOL), 'pfHasAudio'),
                            (['out'], POINTER(BOOL), 'pfSelected'),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsProtected')],
                            HRESULT,
                            'IsProtected',
                            (['out'], POINTER(BOOL), 'pfProtected'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDuration')],
                            HRESULT,
                            'GetDuration',
                            (['in'], REFGUID, 'guidPositionType'),
                            (
                                ['out'],
                                POINTER(PROPVARIANT),
                                'pvDurationValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNumberOfStreams')],
                            HRESULT,
                            'GetNumberOfStreams',
                            (['out'], POINTER(DWORD), 'pdwStreamCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetStreamSelection')],
                            HRESULT,
                            'GetStreamSelection',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['out'], POINTER(BOOL), 'pfEnabled'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStreamSelection')],
                            HRESULT,
                            'SetStreamSelection',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (['in'], BOOL, 'fEnabled'),
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
                            [helpstring('Method GetPresentationAttribute')],
                            HRESULT,
                            'GetPresentationAttribute',
                            (['in'], REFGUID, 'guidMFAttribute'),
                            (['out'], POINTER(PROPVARIANT), 'pvValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCharacteristics')],
                            HRESULT,
                            'GetCharacteristics',
                            (
                                ['out'],
                                POINTER(MFP_MEDIAITEM_CHARACTERISTICS),
                                'pCharacteristics'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetStreamSink')],
                            HRESULT,
                            'SetStreamSink',
                            (['in'], DWORD, 'dwStreamIndex'),
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                                'pMediaSink'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMetadata')],
                            HRESULT,
                            'GetMetadata',
                            (
                                ['out'],
                                POINTER(POINTER(IPropertyStore)),
                                'ppMetadataStore'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFPMediaItem_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfplay_0000_0002
            # [local]
            class MFP_EVENT_TYPE(ENUM):
                MFP_EVENT_TYPE_PLAY = 0
                MFP_EVENT_TYPE_PAUSE = 1
                MFP_EVENT_TYPE_STOP = 2
                MFP_EVENT_TYPE_POSITION_SET = 3
                MFP_EVENT_TYPE_RATE_SET = 4
                MFP_EVENT_TYPE_MEDIAITEM_CREATED = 5
                MFP_EVENT_TYPE_MEDIAITEM_SET = 6
                MFP_EVENT_TYPE_FRAME_STEP = 7
                MFP_EVENT_TYPE_MEDIAITEM_CLEARED = 8
                MFP_EVENT_TYPE_MF = 9
                MFP_EVENT_TYPE_ERROR = 10
                MFP_EVENT_TYPE_PLAYBACK_ENDED = 11
                MFP_EVENT_TYPE_ACQUIRE_USER_CREDENTIAL = 12

            MFP_EVENT_HEADER._fields_ = [
                ('eEventType', MFP_EVENT_TYPE),
                ('hrEvent', HRESULT),
                ('pMediaPlayer', POINTER(IMFPMediaPlayer)),
                ('eState', MFP_MEDIAPLAYER_STATE),
                ('pPropertyStore', POINTER(IPropertyStore)),
            ]

            MFP_PLAY_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_PAUSE_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_STOP_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_POSITION_SET_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_RATE_SET_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
                ('flRate', FLOAT),
            ]

            MFP_MEDIAITEM_CREATED_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
                ('dwUserData', DWORD_PTR),
            ]

            MFP_MEDIAITEM_SET_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_FRAME_STEP_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_MEDIAITEM_CLEARED_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_MF_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('MFEventType', MediaEventType),
                ('pMFMediaEvent', POINTER(IMFMediaEvent)),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_ERROR_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
            ]

            MFP_PLAYBACK_ENDED_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('pMediaItem', POINTER(IMFPMediaItem)),
            ]

            MFP_ACQUIRE_USER_CREDENTIAL_EVENT._fields_ = [
                ('header', MFP_EVENT_HEADER),
                ('dwUserData', DWORD_PTR),
                ('fProceedWithAuthentication', BOOL),
                ('hrAuthenticationStatus', HRESULT),
                ('pwszURL', LPCWSTR),
                ('pwszSite', LPCWSTR),
                ('pwszRealm', LPCWSTR),
                ('pwszPackage', LPCWSTR),
                ('nRetries', LONG),
                ('flags', MFP_CREDENTIAL_FLAGS),
                ('pCredential', POINTER(IMFNetCredential)),
            ]
            if not defined(__IMFPMediaPlayerCallback_INTERFACE_DEFINED__):
                # interface IMFPMediaPlayerCallback
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFPMediaPlayerCallback = MIDL_INTERFACE(
                        "{766C8FFB-5FDB-4FEA-A28D-B912996F51BD}"
                    )
                    IMFPMediaPlayerCallback._iid_ = IID_IMFPMediaPlayerCallback

                    IMFPMediaPlayerCallback._methods_ = [
                        COMMETHOD(
                            [helpstring('Method OnMediaPlayerEvent')],
                            VOID,
                            'OnMediaPlayerEvent',
                            (
                                ['in'],
                                POINTER(MFP_EVENT_HEADER),
                                'pEventHeader'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFPMediaPlayerCallback_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfplay_0000_0003
            # [local]        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


