

from wtypes_h import (
    POINTER,
    CHAR,
    UINT,
    SHORT,
    INT64,
    WCHAR,
    INT,
    LONG,
    VOID
)

import ctypes
from ctype_h import *

from crtdefs_h import * # NOQA
from time_h import *


class _iobuf(ctypes.Structure):
    _fields_ = [
        ('_ptr', POINTER(CHAR)),
        ('_cnt', INT),
        ('_base', POINTER(CHAR)),
        ('_flag', INT),
        ('_file', INT),
        ('_charbuf', INT),
        ('_bufsiz', INT),
        ('_tmpfname', POINTER(CHAR))
    ]

WCHAR_MIN = 0x00000000
WCHAR_MAX = 0x0000FFFF
WEOF = 0xFFFF
FILE = _iobuf



import sys

stdin = sys.stdin
stdout = sys.stdout
stderr = sys.stderr

_fsize_t = UINT

class _wfinddata_t(ctypes.Structure):
    _fields_ = [
        ('attrib', UINT),
        ('time_create', time_t),
        ('time_access', time_t),
        ('time_write', time_t),
        ('size', _fsize_t),
        ('name', WCHAR * 260),
    ]




class _wfinddatai64_t(ctypes.Structure):
    _fields_ = [
        ('attrib', UINT),
        ('time_create', time_t),
        ('time_access', time_t),
        ('time_write', time_t),
        ('size', INT64),
        ('name', WCHAR * 260),
    ]




class _wfinddata32_t(ctypes.Structure):
    _fields_ = [
        ('attrib', UINT),
        ('time_create', _time32_t),
        ('time_access', _time32_t),
        ('time_write', _time32_t),
        ('size', _fsize_t),
        ('name', WCHAR * 260),
    ]




class _wfinddata32i64_t(ctypes.Structure):
    _fields_ = [
        ('attrib', UINT),
        ('time_create', _time32_t),
        ('time_access', _time32_t),
        ('time_write', _time32_t),
        ('size', INT64),
        ('name', WCHAR * 260),
    ]




class _wfinddata64i32_t(ctypes.Structure):
    _fields_ = [
        ('attrib', UINT),
        ('time_create', _time64_t),
        ('time_access', _time64_t),
        ('time_write', _time64_t),
        ('size', _fsize_t),
        ('name', WCHAR * 260),
    ]




class _wfinddata64_t(ctypes.Structure):
    _fields_ = [
        ('attrib', UINT),
        ('time_create', _time64_t),
        ('time_access', _time64_t),
        ('time_write', _time64_t),
        ('size', INT64),
        ('name', WCHAR * 260),
    ]



__PCTYPE_FUNC = _pctype
_pctype = _pctype
_pwctype = _pctype

_UPPER = 0x00000001
_LOWER = 0x00000002
_DIGIT = 0x00000004
_SPACE = 0x00000008
_PUNCT = 0x00000010
_CONTROL = 0x00000020
_BLANK = 0x00000040
_HEX = 0x00000080
_LEADBYTE = 0x00008000
_ALPHA = 0x0100 | _UPPER | _LOWER

_ino_t = UINT
ino_t = UINT
_dev_t = UINT
dev_t = UINT
_off_t = LONG
off_t = LONG

class _stat32(ctypes.Structure):
    _fields_ = [
        ('st_dev', _dev_t),
        ('st_ino', _ino_t),
        ('SHORT st_mode', UINT),
        ('st_nlink', SHORT),
        ('st_uid', SHORT),
        ('st_gid', SHORT),
        ('st_rdev', _dev_t),
        ('st_size', _off_t),
        ('st_atime', _time32_t),
        ('st_mtime', _time32_t),
        ('st_ctime', _time32_t),
    ]




class stat(ctypes.Structure):
    _fields_ = [
        ('st_dev', _dev_t),
        ('st_ino', _ino_t),
        ('SHORT st_mode', UINT),
        ('st_nlink', SHORT),
        ('st_uid', SHORT),
        ('st_gid', SHORT),
        ('st_rdev', _dev_t),
        ('st_size', _off_t),
        ('st_atime', time_t),
        ('st_mtime', time_t),
        ('st_ctime', time_t),
    ]




class _stat32i64(ctypes.Structure):
    _fields_ = [
        ('st_dev', _dev_t),
        ('st_ino', _ino_t),
        ('SHORT st_mode', UINT),
        ('st_nlink', SHORT),
        ('st_uid', SHORT),
        ('st_gid', SHORT),
        ('st_rdev', _dev_t),
        ('st_size', INT64),
        ('st_atime', _time32_t),
        ('st_mtime', _time32_t),
        ('st_ctime', _time32_t),
    ]




class _stat64i32(ctypes.Structure):
    _fields_ = [
        ('st_dev', _dev_t),
        ('st_ino', _ino_t),
        ('SHORT st_mode', UINT),
        ('st_nlink', SHORT),
        ('st_uid', SHORT),
        ('st_gid', SHORT),
        ('st_rdev', _dev_t),
        ('st_size', _off_t),
        ('st_atime', _time64_t),
        ('st_mtime', _time64_t),
        ('st_ctime', _time64_t),
    ]




class _stat64(ctypes.Structure):
    _fields_ = [
        ('st_dev', _dev_t),
        ('st_ino', _ino_t),
        ('SHORT st_mode', UINT),
        ('st_nlink', SHORT),
        ('st_uid', SHORT),
        ('st_gid', SHORT),
        ('st_rdev', _dev_t),
        ('st_size', INT64),
        ('st_atime', _time64_t),
        ('st_mtime', _time64_t),
        ('st_ctime', _time64_t),
    ]


class _stat(ctypes.Structure):
    _fields_ = [
        ('st_dev', _dev_t),
        ('st_ino', _ino_t),
        ('SHORT st_mode', UINT),
        ('st_nlink', SHORT),
        ('st_uid', SHORT),
        ('st_gid', SHORT),
        ('st_rdev', _dev_t),
        ('st_size', _off_t),
        ('st_atime', time_t),
        ('st_mtime', time_t),
        ('st_ctime', time_t),
    ]


class _stati64(ctypes.Structure):
    _fields_ = [
        ('st_dev', _dev_t),
        ('st_ino', _ino_t),
        ('SHORT st_mode', UINT),
        ('st_nlink', SHORT),
        ('st_uid', SHORT),
        ('st_gid', SHORT),
        ('st_rdev', _dev_t),
        ('st_size', INT64),
        ('st_atime', time_t),
        ('st_mtime', time_t),
        ('st_ctime', time_t),
    ]


__stat64 = _stat64


_SWPRINTFS_DEPRECATED = (
    _CRT_DEPRECATE_TEXT("swprINTf has been changed to conform with the ISO C standard, adding an extra CHARacter count parameter. To use traditional Microsoft swprINTf, set _CRT_NON_CONFORMING_SWPRINTFS.")
)


def getwCHAR():
    return fgetwc(stdin)


def putwCHAR(_c):
    return fputwc(_c, stdout)


def getwc(_stm):
    return fgetwc(_stm)


def putwc(_c, _stm):
    return fputwc(_c,_stm)


def _putwc_nolock(_c, _stm):
    return _fputwc_nolock(_c,_stm)


def _getwc_nolock(_c):
    return _fgetwc_nolock(_c)


def fgetwc(_stm):
    return _getwc_nolock(_stm)


def fputwc(_c, _stm):
    return _putwc_nolock(_c,_stm)


def ungetwc(_c, _stm):
    return _ungetwc_nolock(_c,_stm)

_putwch = VOID # _putwch_nolock
_getwch = VOID # _getwch_nolock
_getwche = VOID # _getwche_nolock
_ungetwch = VOID # _ungetwch_nolock

wcswcs = wcsstr

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


mbstate_t = INT
_WINT_t = WCHAR

__all__ = (
    '_iswxdigit_l', '_iswspace_l', '_getwc_nolock', '_iswgraph_l', '_getwch',
    'fgetwc', 'iswupper', 'isleadbyte', '__PCTYPE_FUNC', '_ungetwch', 'getwc',
    'iswcntrl', 'iswxdigit', '_iswpunct_l', 'iswgraph', '_iswprint_l', '_HEX',
    'iswpunct', 'stderr', 'iswspace', '_iswalpha_l', '_putwch', '_UPPER',
    'getwCHAR', 'putwc', '_iswupper_l', '_iswalnum_l', 'ungetwc', '__stat64',
    '_iswcntrl_l', '_getwche', 'WEOF', 'iswdigit', '_PUNCT', 'fputwc', 'stat',
    '_iswdigit_l', 'iswalnum', 'iswprint', '_LEADBYTE', 'putwCHAR', '_BLANK',
    '_iswlower_l', 'iswlower', 'iswalpha', '_putwc_nolock', '_ALPHA', 'stdin',
    '_pctype', '_DIGIT', 'iswascii', '_SWPRINTFS_DEPRECATED', 'stdout', 'tm',
    '_CONTROL', 'WCHAR_MAX', 'WCHAR_MIN', '_LOWER', 'wcswcs', '_SPACE',
    '_pwctype', '_stat', '_stat32', '_stat32i64', '_wfinddata64_t', 'FILE',
    '_wfinddata_t', '_wfinddata32_t', '_wfinddata64i32_t', '_stati64',
    '_stat64i32', '_stat64', '_wfinddata32i64_t', '_wfinddatai64_t', '_off_t',
    'mbstate_t', '_fsize_t', '_WINT_t', '_ino_t', 'off_t', '_dev_t', 'dev_t',
    'ino_t', '_iobuf'
)
