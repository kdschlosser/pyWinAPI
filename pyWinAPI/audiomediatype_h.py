__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
from .oaidl_h import * # NOQA
from .ocidl_h import * # NOQA
from .mmreg_h import * # NOQA
from .winapifamily_h import * # NOQA

import ctypes
import comtypes
from .wtypes_h import (
    BOOL,
    POINTER,
    HRESULT,
    DWORD,
    GUID,
    FLOAT,
)
from .guiddef_h import IID


class _UNCOMPRESSEDAUDIOFORMAT(ctypes.Structure):
    _fields_ = [
        ('guidFormatType', GUID),
        ('dwSamplesPerFrame', DWORD),
        ('dwBytesPerSampleContainer', DWORD),
        ('dwValidBitsPerSample', DWORD),
        ('fFramesPerSecond', FLOAT),
        ('dwChannelMask', DWORD),
    ]

UNCOMPRESSEDAUDIOFORMAT = _UNCOMPRESSEDAUDIOFORMAT

COMMETHOD = comtypes.COMMETHOD

IID_IAudioMediaType = IID(
    '{4E997F73-B71F-4798-873B-ED7DFCF15B4D}'
)


class IAudioMediaType(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioMediaType
    _idlflags_ = []


IAudioMediaType._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'IsCompressedFormat',
        (['out'], POINTER(BOOL), 'pfCompressed'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsEqual',
        (['in'], POINTER(IAudioMediaType), 'pIAudioType'),
        (['out'], POINTER(DWORD), 'pdwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetUncompressedAudioFormat',
        (['out'], POINTER(UNCOMPRESSEDAUDIOFORMAT), 'pUncompressedAudioFormat'),
    ),
]


AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES = 0x00000002
AUDIOMEDIATYPE_EQUAL_FORMAT_DATA = 0x00000004
AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA = 0x00000008


__all__ = (
    '_UNCOMPRESSEDAUDIOFORMAT', 'UNCOMPRESSEDAUDIOFORMAT', 'IAudioMediaType',
    'IID_IAudioMediaType', 'AUDIOMEDIATYPE_EQUAL_FORMAT_TYPES',
    'AUDIOMEDIATYPE_EQUAL_FORMAT_DATA', 'AUDIOMEDIATYPE_EQUAL_FORMAT_USER_DATA'
)
