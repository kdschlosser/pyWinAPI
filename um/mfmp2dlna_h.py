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
__mfmp2dlna_h__ = None
__IMFDLNASinkInit_FWD_DEFINED__ = None
__IMFDLNASinkInit_INTERFACE_DEFINED__ = None


class _MFMPEG2DLNASINKSTATS(ctypes.Structure):
    pass


MFMPEG2DLNASINKSTATS = _MFMPEG2DLNASINKSTATS


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


if not defined(__mfmp2dlna_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IMFDLNASinkInit_FWD_DEFINED__):
        class IMFDLNASinkInit(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IMFDLNASinkInit_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.mfobjects_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfmp2dlna_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if WINVER >= _WIN32_WINNT_WIN7:
            if not defined(__IMFDLNASinkInit_INTERFACE_DEFINED__):
                # interface IMFDLNASinkInit
                # [local][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMFDLNASinkInit = MIDL_INTERFACE(
                        "{0C012799-1B61-4C10-BDA9-04445BE5F561}"
                    )
                    IMFDLNASinkInit._iid_ = IID_IMFDLNASinkInit

                    IMFDLNASinkInit._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Initialize')],
                            HRESULT,
                            'Initialize',
                            ([], POINTER(IMFByteStream), 'pByteStream'),
                            ([], BOOL, 'fPal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMFDLNASinkInit_INTERFACE_DEFINED__

            # interface __MIDL_itf_mfmp2dlna_0000_0001
            # [local]
            CLSID_MPEG2DLNASink = EXTERN_GUID(
                0xFA5FE7C5,
                0x6A1D,
                0x4B11,
                0xB4,
                0x1F,
                0xF9,
                0x59,
                0xD6,
                0xC7,
                0x65,
                0x00
            )
            MF_MP2DLNA_USE_MMCSS = EXTERN_GUID(
                0x54F3E2EE,
                0xA2A2,
                0x497D,
                0x98,
                0x34,
                0x97,
                0x3A,
                0xFD,
                0xE5,
                0x21,
                0xEB
            )
            MF_MP2DLNA_VIDEO_BIT_RATE = EXTERN_GUID(
                0xE88548DE,
                0x73B4,
                0x42D7,
                0x9C,
                0x75,
                0xAD,
                0xFA,
                0xA,
                0x2A,
                0x6E,
                0x4C
            )
            MF_MP2DLNA_AUDIO_BIT_RATE = EXTERN_GUID(
                0x2D1C070E,
                0x2B5F,
                0x4AB3,
                0xA7,
                0xE6,
                0x8D,
                0x94,
                0x3B,
                0xA8,
                0xD0,
                0x0A
            )
            MF_MP2DLNA_ENCODE_QUALITY = EXTERN_GUID(
                0xB52379D7,
                0x1D46,
                0x4FB6,
                0xA3,
                0x17,
                0xA4,
                0xA5,
                0xF6,
                0x09,
                0x59,
                0xF8
            )
            MF_MP2DLNA_STATISTICS = EXTERN_GUID(
                0x75E488A3,
                0xD5AD,
                0x4898,
                0x85,
                0xE0,
                0xBC,
                0xCE,
                0x24,
                0xA7,
                0x22,
                0xD7
            )

            _MFMPEG2DLNASINKSTATS._fields_ = [
                ('cBytesWritten', DWORDLONG),
                ('fPAL', BOOL),
                ('fccVideo', DWORD),
                ('dwVideoWidth', DWORD),
                ('dwVideoHeight', DWORD),
                ('cVideoFramesReceived', DWORDLONG),
                ('cVideoFramesEncoded', DWORDLONG),
                ('cVideoFramesSkipped', DWORDLONG),
                ('cBlackVideoFramesEncoded', DWORDLONG),
                ('cVideoFramesDuplicated', DWORDLONG),
                ('cAudioSamplesPerSec', DWORD),
                ('cAudioChannels', DWORD),
                ('cAudioBytesReceived', DWORDLONG),
                ('cAudioFramesEncoded', DWORDLONG),
            ]
        # END IF   (WINVER >= _WIN32_WINNT_WIN7)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


