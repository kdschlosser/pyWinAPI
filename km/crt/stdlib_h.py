

from wtypes_h import (
    LONG,
    DOUBLE,
    FLOAT,
    UINT,
    INT,
)
import ctypes

from crtdefs_h import * # NOQA
from limits_h import * # NOQA

MB_LEN_MAX = 0x00000005
EXIT_SUCCESS = 0x00000000
EXIT_FAILURE = 0x00000001
_onexit_t = INT
_onexit_m_t = _onexit_t
onexit_t = _onexit_t


class _div_t(ctypes.Structure):
    _fields_ = [
        ('quot', INT),
        ('rem', INT),
    ]


div_t = _div_t


class _ldiv_t(ctypes.Structure):
    _fields_ = [
        ('quot', LONG),
        ('rem', LONG),
    ]


ldiv_t = _ldiv_t


class _LDOUBLE(ctypes.Structure):
    _fields_ = [
        ('CHAR ld', UINT * 10),
    ]


def _PTR_LD(x):
    return x


class _CRT_DOUBLE(ctypes.Structure):
    _fields_ = [
        ('x', DOUBLE),
    ]


class _CRT_FLOAT(ctypes.Structure):
    _fields_ = [
        ('f', FLOAT),
    ]


class _LONGDOUBLE(ctypes.Structure):
    _fields_ = [
        ('x', LONG),
    ]


class _LDBL12(ctypes.Structure):
    _fields_ = [
        ('CHAR ld12', UINT * 12),
    ]


RAND_MAX = 0x00007FFF


def __max(a, b):
    if a > b:
        return a
    else:
        return b


def __min(a, b):
    if a < b:
        return a
    else:
        return b


_MAX_PATH = 0x00000104
_MAX_DRIVE = 0x00000003
_MAX_DIR = 0x00000100
_MAX_FNAME = 0x00000100
_MAX_EXT = 0x00000100
_OUT_TO_DEFAULT = 0x00000000
_OUT_TO_STDERR = 0x00000001
_OUT_TO_MSGBOX = 0x00000002
_REPORT_ERRMODE = 0x00000003
_WRITE_ABORT_MSG = 0x00000001
_CALL_REPORTFAULT = 0x00000002
_MAX_ENV = 0x00007FFF


def _countof(_Array):
    return ctypes.sizeof(_Array) / ctypes.sizeof(_Array[0])


_CVTBUFSIZE = 309 + 40
max = __max
min = __min

__all__ = (
    '_CVTBUFSIZE', '_OUT_TO_STDERR', '_MAX_ENV', '_REPORT_ERRMODE',
    '_WRITE_ABORT_MSG', '_OUT_TO_DEFAULT',  '_PTR_LD', 'RAND_MAX', '_MAX_EXT',
    '_countof', '_MAX_DRIVE', '_MAX_DIR', 'MB_LEN_MAX', '_CALL_REPORTFAULT',
    '_OUT_TO_MSGBOX', '_MAX_FNAME', 'EXIT_SUCCESS', 'EXIT_FAILURE',
    '_MAX_PATH', 'onexit_t', '_LDOUBLE', '_ldiv_t', '_CRT_FLOAT', 'div_t',
    '_CRT_DOUBLE', '_LONGDOUBLE', 'ldiv_t', '_LDBL12', '_div_t', '_onexit_m_t',
    'min', 'max'
)
