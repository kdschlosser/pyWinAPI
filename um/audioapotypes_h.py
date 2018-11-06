
from .winapifamily_h import * # NOQA

import ctypes
from .wtypes_h import (
    ENUM,
    UINT_PTR,
    UINT32,
    POINTER,
)


class APO_BUFFER_FLAGS(ENUM):
    BUFFER_INVALID = 0
    BUFFER_VALID = 1
    BUFFER_SILENT = 2


class APO_CONNECTION_PROPERTY(ctypes.Structure):
    _fields_ = [
        ('pBuffer', UINT_PTR),
        ('u32ValidFrameCount', UINT32),
        ('u32BufferFlags', APO_BUFFER_FLAGS),
        ('u32Signature', UINT32),
    ]


PAPO_CONNECTION_PROPERTY = POINTER(APO_CONNECTION_PROPERTY)


class AUDIO_CURVE_TYPE(ENUM):
    AUDIO_CURVE_TYPE_NONE = 0
    AUDIO_CURVE_TYPE_WINDOWS_FADE = 1


__all__ = (
    'AUDIO_CURVE_TYPE', 'PAPO_CONNECTION_PROPERTY', 'APO_CONNECTION_PROPERTY',
    'APO_BUFFER_FLAGS'
)
