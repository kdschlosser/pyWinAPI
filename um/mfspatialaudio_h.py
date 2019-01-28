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
__mfspatialaudio_h__ = None
__IMFSpatialAudioObjectBuffer_FWD_DEFINED__ = None
__IMFSpatialAudioSample_FWD_DEFINED__ = None
__IMFSpatialAudioObjectBuffer_INTERFACE_DEFINED__ = None
__IMFSpatialAudioSample_INTERFACE_DEFINED__ = None


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


if not defined(__mfspatialaudio_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # header files for imported files
    from pyWinAPI.um.mfobjects_h import *  # NOQA
    from pyWinAPI.um.spatialaudioclient_h import *  # NOQA
    from pyWinAPI.um.spatialaudiometadata_h import *  # NOQA

    # Forward Declarations
    if not defined(__IMFSpatialAudioObjectBuffer_FWD_DEFINED__):
        class IMFSpatialAudioObjectBuffer(IMFMediaBuffer):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IMFSpatialAudioObjectBuffer_FWD_DEFINED__

    if not defined(__IMFSpatialAudioSample_FWD_DEFINED__):
        class IMFSpatialAudioSample(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMFSpatialAudioSample_FWD_DEFINED__

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_mfspatialaudio_0000_0000
    # [local]
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        if not defined(__IMFSpatialAudioObjectBuffer_INTERFACE_DEFINED__):
            # interface IMFSpatialAudioObjectBuffer
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSpatialAudioObjectBuffer = MIDL_INTERFACE(
                    "{D396EC8C-605E-4249-978D-72AD1C312872}"
                )
                IMFSpatialAudioObjectBuffer._iid_ = IID_IMFSpatialAudioObjectBuffer

                IMFSpatialAudioObjectBuffer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetID')],
                        HRESULT,
                        'SetID',
                        (['in'], UINT32, 'u32ID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetID')],
                        HRESULT,
                        'GetID',
                        (['out'], POINTER(UINT32), 'pu32ID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetType')],
                        HRESULT,
                        'SetType',
                        (['in'], AudioObjectType, 'type'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetType')],
                        HRESULT,
                        'GetType',
                        (['out'], POINTER(AudioObjectType), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMetadataItems')],
                        HRESULT,
                        'GetMetadataItems',
                        (
                            ['out'],
                            POINTER(POINTER(ISpatialAudioMetadataItems)),
                            'ppMetadataItems'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSpatialAudioObjectBuffer_INTERFACE_DEFINED__

        if not defined(__IMFSpatialAudioSample_INTERFACE_DEFINED__):
            # interface IMFSpatialAudioSample
            # [local][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMFSpatialAudioSample = MIDL_INTERFACE(
                    "{ABF28A9B-3393-4290-BA79-5FFC46D986B2}"
                )
                IMFSpatialAudioSample._iid_ = IID_IMFSpatialAudioSample

                IMFSpatialAudioSample._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetObjectCount')],
                        HRESULT,
                        'GetObjectCount',
                        (['out'], POINTER(DWORD), 'pdwObjectCount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddSpatialAudioObject')],
                        HRESULT,
                        'AddSpatialAudioObject',
                        (
                            ['in'],
                            POINTER(IMFSpatialAudioObjectBuffer),
                            'pAudioObjBuffer'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSpatialAudioObjectByIndex')],
                        HRESULT,
                        'GetSpatialAudioObjectByIndex',
                        (['in'], DWORD, 'dwIndex'),
                        (
                            ['out'],
                            POINTER(POINTER(IMFSpatialAudioObjectBuffer)),
                            'ppAudioObjBuffer'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMFSpatialAudioSample_INTERFACE_DEFINED__

        # interface __MIDL_itf_mfspatialaudio_0000_0002
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


