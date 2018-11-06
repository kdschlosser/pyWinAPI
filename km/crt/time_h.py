

from wtypes_h import (
    NULL,
    INT,
    UINT,
    LONG,
    INT64,
    SIZE_T
)
import ctypes


from crtdefs_h import * # NOQA
from crtdefs_h import * # NOQA
_time32_t = LONG
_time64_t = INT64
time_t = INT64
clock_t = LONG
size_t = SIZE_T

class tm(ctypes.Structure):
    _fields_ = [
        ('tm_sec', INT),
        ('tm_min', INT),
        ('tm_hour', INT),
        ('tm_mday', INT),
        ('tm_mon', INT),
        ('tm_year', INT),
        ('tm_wday', INT),
        ('tm_yday', INT),
        ('tm_isdst', INT),
    ]

CLOCKS_PER_SEC = 0x000003E8

CLK_TCK = CLOCKS_PER_SEC

__all__ = (
    'CLK_TCK', 'CLOCKS_PER_SEC', 'tm', 'size_t', '_time32_t', 'clock_t',
    'time_t', '_time64_t',
)
