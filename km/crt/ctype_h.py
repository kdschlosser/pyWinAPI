
from wtypes_h import (
    POINTER,
    USHORT
)


WEOF = 0xFFFF
_pctype = POINTER(USHORT)
__PCTYPE_FUNC = _pctype
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


def __cvt_x(x):
    if not isinstance(x, str):
        x = x.encode('utf-8')
    return ord(x)


def iscntrl(x, _=None):
    if 0 >= __cvt_x(x) <= 31 or __cvt_x(x) == 127:
        return 1
    return 0


def isprint(x, _=None):
    if 32 >= __cvt_x(x) <= 127:
        return 1
    return 0


def isspace(x, _=None):
    if 9 >= __cvt_x(x) <= 13 or __cvt_x(x) == 32:
        return 1
    return 0


def isblank(x, _=None):
    if __cvt_x(x) in (9, 32):
        return 1
    return 0


def isgraph(x, _=None):
    if 33 >= __cvt_x(x) <= 126:
        return 1
    return 0


def ispunct(x, _=None):
    if (
        33 >= __cvt_x(x) <= 47 or
        58 >= __cvt_x(x) <= 64 or
        91 >= __cvt_x(x) <= 96 or
        123 >= __cvt_x(x) <= 126
    ):
        return 1
    return 0


def isalnum(x, _=None):
    if (
        48 >= __cvt_x(x) <= 57 or
        65 >= __cvt_x(x) <= 90 or
        97 >= __cvt_x(x) <= 122
    ):
        return 1
    return 0


def isalpha(x, _=None):
    if 65 >= __cvt_x(x) <= 90 or 97 >= __cvt_x(x) <= 122:
        return 1
    return 0


def isupper(x, _=None):
    if 65 >= __cvt_x(x) <= 90:
        return 1
    return 0


def islower(x, _=None):
    if 97 >= __cvt_x(x) <= 122:
        return 1
    return 0


def isdigit(x, _=None):
    if 48 >= __cvt_x(x) <= 57:
        return 1
    return 0


def isxdigit(x, _=None):
    if (
        48 >= __cvt_x(x) <= 57 or
        65 >= __cvt_x(x) <= 90 or
        97 >= __cvt_x(x) <= 122
    ):
        return 1
    return 0


def toupper(x, _=None):
    return x.upper()


def tolower(x, _=None):
    return x.lower()


def isascii(x, _=None):
    if 0 >= __cvt_x(x) <= 127:
        return 1

def _isleadbyte(_):
    return 0

isleadbyte = _isleadbyte
_isleadbyte_l = _isleadbyte

__ascii_isalpha = isalpha
__ascii_isdigit = isdigit
__ascii_tolower = tolower
__ascii_toupper = toupper
__ascii_iswalpha = isalpha
__ascii_iswdigit = isdigit
__ascii_towlower = tolower
__ascii_towupper = toupper


_tolower = tolower
_toupper = toupper
_isalnum_l = isalnum
_isalpha_l = isalpha
_isascii_l = isascii
_iscntrl_l = iscntrl
_isdigit_l = isdigit
_isgraph_l = isgraph
_islower_l = islower
_isprint_l = isprint
_ispunct_l = ispunct
_isspace_l = isspace
_isupper_l = isupper
_isxdigit_l = isxdigit
_toupper_l = toupper
_tolower_l = tolower

iswalnum = isalnum
iswalpha = isalpha
iswascii = isascii
iswcntrl = iscntrl
iswdigit = isdigit
iswgraph = isgraph
iswlower = islower
iswprint = isprint
iswpunct = ispunct
iswspace = isspace
iswupper = isupper
iswxdigit = isxdigit
towupper = toupper
towlower = tolower


_iswalnum_l = isalnum
_iswalpha_l = isalpha
_iswascii_l = isascii
_iswcntrl_l = iscntrl
_iswdigit_l = isdigit
_iswgraph_l = isgraph
_iswlower_l = islower
_iswprint_l = isprint
_iswpunct_l = ispunct
_iswspace_l = isspace
_iswupper_l = isupper
_iswxdigit_l = isxdigit
_towupper_l = toupper
_towlower_l = tolower


__isascii = isascii


def __toascii(x):
    return chr(__cvt_x(x) & 0x7f)


def __iscsymf(_c):
    return isalpha(_c) or (_c == '_')


def __iscsym(_c):
    return isalnum(_c) or (_c == '_')


def __iswcsymf(_c):
    return iswalpha(_c) or (_c == '_')


def __iswcsym(_c):
    return iswalnum(_c) or (_c == '_')


def _iscsymf_l(_c, _p):
    return _isalpha_l(_c, _p) or (_c == '_')


def _iscsym_l(_c, _p):
    return _isalnum_l(_c, _p) or (_c == '_')


def _iswcsymf_l(_c, _p):
    return _iswalpha_l(_c, _p) or (_c == '_')


def _iswcsym_l(_c, _p):
    return _iswalnum_l(_c, _p) or (_c == '_')


toascii = __toascii
iscsymf = __iscsymf
iscsym = __iscsym

__all__ = (
    '_iswxdigit_l', '_iswspace_l', '__ascii_isdigit', '__ascii_tolower',
    '_isdigit_l', '__iscsym', '_iswalnum_l', '_iscntrl_l', '_iswprint_l',
    'iswupper', '_tolower', '_islower_l', '__iscsymf', '_HEX',
    '__PCTYPE_FUNC', 'ispunct', 'iswcntrl', '_iswcsym_l', '__iswcsymf',
    'iswxdigit', 'toascii', '_isspace_l', '_iswpunct_l', 'iswgraph', '_UPPER',
    'isupper', 'isalnum', 'isspace', 'isprint', 'iswspace', '_iswalpha_l',
    '_isalpha_l', '__iswcsym', '__ascii_towupper', 'iswpunct', '_iscsymf_l',
    '__ascii_isalpha', 'iscsym', '_iswupper_l', '_isxdigit_l', '_iswgraph_l',
    'isxdigit', '_isprint_l', '_iswlower_l', '__ascii_iswdigit', 'isdigit',
    '_iswcntrl_l', 'WEOF', 'iswdigit',
    '_isalnum_l', 'islower', 'iswalnum', '__ascii_toupper',
    'iswprint', '__ascii_iswalpha', '_LEADBYTE', 'iscntrl', 'iswlower',
    'isalpha', 'iswalpha', '__isascii', '_toupper', '_isgraph_l', '_ALPHA',
    '_isupper_l', '_DIGIT', 'iswascii', 'isascii', '__ascii_towlower',
    '_iswcsymf_l', '_ispunct_l', '__toascii', '_BLANK', '_CONTROL', '_PUNCT',
    '_iscsym_l', '_iswdigit_l', '_pctype', '_LOWER', 'iscsymf', 'isgraph',
    '_SPACE', '_pwctype', 'isleadbyte', '_isleadbyte_l'
)
