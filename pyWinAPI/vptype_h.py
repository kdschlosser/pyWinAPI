from .winapifamily_h import * # NOQA
from .wtypes_h import(
    ENUM,
    POINTER,
    DWORD,
    RECT,
    BOOL,
    LONG
)
import ctypes


class _AMVP_SELECT_FORMAT_BY(ENUM):
    AMVP_DO_NOT_CARE = 0
    AMVP_BEST_BANDWIDTH = 1
    AMVP_INPUT_SAME_AS_OUTPUT = 2


AMVP_SELECT_FORMAT_BY = _AMVP_SELECT_FORMAT_BY


class _AMVP_MODE(ENUM):
    AMVP_MODE_WEAVE = 0
    AMVP_MODE_BOBINTERLEAVED = 1
    AMVP_MODE_BOBNONINTERLEAVED = 2
    AMVP_MODE_SKIPEVEN = 3
    AMVP_MODE_SKIPODD = 4


AMVP_MODE = _AMVP_MODE


class _AMVPSIZE(ctypes.Structure):
    _fields_ = [
        ('dwWidth', DWORD),
        ('dwHeight', DWORD)
    ]


AMVPSIZE = _AMVPSIZE
LPAMVPSIZE = POINTER(_AMVPSIZE)


class _AMVPDIMINFO(ctypes.Structure):
    _fields_ = [
        ('dwFieldWidth', DWORD),
        ('dwFieldHeight', DWORD),
        ('dwVBIWidth', DWORD),
        ('dwVBIHeight', DWORD),
        ('rcValidRegion', RECT),
    ]


AMVPDIMINFO = _AMVPDIMINFO
LPAMVPDIMINFO = POINTER(_AMVPDIMINFO)


class _AMVPDATAINFO(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwMicrosecondsPerField', DWORD),
        ('amvpDimInfo', AMVPDIMINFO),
        ('dwPictAspectRatioX', DWORD),
        ('dwPictAspectRatioY', DWORD),
        ('bEnableDoubleClock', BOOL),
        ('bEnableVACT', BOOL),
        ('bDataIsInterlaced', BOOL),
        ('lHalfLinesOdd', LONG),
        ('bFieldPolarityInverted', BOOL),
        ('dwNumLinesInVREF', DWORD),
        ('lHalfLinesEven', LONG),
        ('dwReserved1', DWORD),
    ]


AMVPDATAINFO = _AMVPDATAINFO
LPAMVPDATAINFO = POINTER(_AMVPDATAINFO)


__all__ = (
    '_AMVP_SELECT_FORMAT_BY', 'AMVP_SELECT_FORMAT_BY', '_AMVP_MODE',
    'AMVP_MODE', '_AMVPSIZE', 'AMVPSIZE', 'LPAMVPSIZE', '_AMVPDIMINFO',
    'AMVPDIMINFO', 'LPAMVPDIMINFO', '_AMVPDATAINFO', 'AMVPDATAINFO',
    'LPAMVPDATAINFO'
)
