

from shared.wtypes_h import (
    ENUM,
    NULL,
    POINTER,
    CHAR,
    VOID,
    INT,
    UINT,
    INT64,
    UINT64,
)
from pyWinAPI import *

import ctypes

from shared.ntdef_h import *

from shared.sdkddkver_h import *

if NTDDI_VERSION >= NTDDI_WIN10_RS3:
    __UCONFIG_H__ = 0

    U_DISABLE_RENAMING = 0x00000001
    U_SHOW_CPLUSPLUS_API = 0x00000000
    U_DEFAULT_SHOW_DRAFT = 0x00000000
    U_HIDE_DRAFT_API = 0x00000001
    U_HIDE_DEPRECATED_API = 0x00000001
    U_HIDE_OBSOLETE_API = 0x00000001
    U_HIDE_INTERNAL_API = 0x00000001
    U_HAVE_STD_STRING = 0x00000000
    U_NO_DEFAULT_INCLUDE_UTF_HEADERS = 0x00000001

    # from uconfig_local_h import * # NOQA

    U_DEBUG = 0x00000000
    UCLN_NO_AUTO_CLEANUP = 0x00000001
    U_OVERRIDE_CXX_ALLOCATION = 0x00000001
    U_ENABLE_TRACING = 0x00000000
    UCONFIG_ENABLE_PLUGINS = 0x00000000
    U_ENABLE_DYLOAD = 0x00000001
    U_CHECK_DYLOAD = 0x00000001
    U_HAVE_LIB_SUFFIX = 0x00000001


    def CONVERT_TO_STRING(s):
        return str(s)


    U_LIB_SUFFIX_C_NAME_STRING = ""
    UCONFIG_ONLY_COLLATION = 0x00000000
    UCONFIG_NO_FILE_IO = 0x00000000
    UCONFIG_NO_CONVERSION = 0x00000000
    UCONFIG_ONLY_HTML_CONVERSION = 0x00000000
    UCONFIG_NO_LEGACY_CONVERSION = 0x00000000
    UCONFIG_NO_NORMALIZATION = 0x00000000


    UCONFIG_NO_BREAK_ITERATION = 0x00000000
    UCONFIG_NO_IDNA = 0x00000000
    # UCONFIG_MSGPAT_DEFAULT_APOSTROPHE_MODE = UMessagePatternApostropheMode.UMSGPAT_APOS_DOUBLE_OPTIONAL
    UCONFIG_NO_COLLATION = 0x00000000
    UCONFIG_NO_FORMATTING = 0x00000000
    UCONFIG_NO_TRANSLITERATION = 0x00000000
    UCONFIG_NO_REGULAR_EXPRESSIONS = 0x00000000
    UCONFIG_NO_SERVICE = 0x00000000
    UCONFIG_HAVE_PARSEALLINPUT = 0x00000001
    UCONFIG_FORMAT_FASTPATHS_49 = 0x00000001
    UCONFIG_NO_FILTERED_BREAK_ITERATION = 0x00000000

    _PLATFORM_H = 0

    U_PF_UNKNOWN = 0x00000000
    U_PF_WINDOWS = 0x000003E8
    U_PF_MINGW = 0x00000708
    U_PF_CYGWIN = 0x0000076C
    U_PF_HPUX = 0x00000834
    U_PF_SOLARIS = 0x00000A28
    U_PF_BSD = 0x00000BB8
    U_PF_AIX = 0x00000C1C
    U_PF_IRIX = 0x00000C80
    U_PF_DARWIN = 0x00000DAC
    U_PF_IPHONE = 0x00000DDE
    U_PF_QNX = 0x00000E74
    U_PF_LINUX = 0x00000FA0
    U_PF_BROWSER_NATIVE_CLIENT = 0x00000FB4
    U_PF_ANDROID = 0x00000FD2
    U_PF_OS390 = 0x00002328
    U_PF_OS400 = 0x000024B8

    U_PLATFORM = U_PF_WINDOWS
    U_PLATFORM_USES_ONLY_WIN32_API = 0x00000001
    U_PLATFORM_HAS_WIN32_API = 0x00000001
    U_PLATFORM_IMPLEMENTS_POSIX = 0x00000000
    U_PLATFORM_IS_LINUX_BASED = 0x00000000
    U_PLATFORM_IS_DARWIN_BASED = 0x00000000

    U_HAVE_STDINT_H = 0x00000000
    U_HAVE_INTTYPES_H = U_HAVE_STDINT_H

    U_IOSTREAM_SOURCE = 0x00030C1F
    U_GCC_MAJOR_MINOR = 0x00000000
    U_IS_BIG_ENDIAN = 0x00000000
    U_HAVE_PLACEMENT_NEW = 0x00000001
    U_HAVE_DEBUG_LOCATION_NEW = 0x00000001


    def __has_attribute(x):
        return 0


    def __has_cpp_attribute(x):
        return 0


    def __has_builtin(x):
        return 0


    def __has_feature(x):
        return 0


    def __has_extension(x):
        return 0


    def __has_warning(x):
        return 0


    U_MALLOC_ATTR = None


    def U_ALLOC_SIZE_ATTR(X):
        pass


    def _ALLOC_SIZE_ATTR2(X, Y):
        pass


    U_CPLUSPLUS_VERSION = 0x00000000
    U_HAVE_RVALUE_REFERENCES = 0x00000000
    U_NOEXCEPT = None

    U_FALLTHROUGH = None
    U_ASCII_FAMILY = 0x00000000
    U_EBCDIC_FAMILY = 0x00000001
    U_CHARSET_FAMILY = U_ASCII_FAMILY

    U_CHARSET_IS_UTF8 = 0x00000000
    U_HAVE_WCHAR_H = 0x00000001
    U_SIZEOF_WCHAR_T = 0x00000002

    U_HAVE_WCSCPY = U_HAVE_WCHAR_H
    U_HAVE_CHAR16_T = 0x00000001

    def U_DECLARE_UTF16(string):
        return string


    def U_EXPORT(dllexport):
        return dllexport


    def U_EXPORT2(dllexport):
        return dllexport


    def U_IMPORT(dllimport):
        return dllimport


    U_CALLCONV = U_EXPORT2
    _PTYPES_H = 0

    __STDC_LIMIT_MACROS = 0


    # from features_h import * # NOQA


    uint8_t = UINT
    int8_t = INT
    short16_t = INT
    int16_t = SHORT
    uint16_t = UINT
    int32_t = INT
    uint32_t = UINT
    int64_t = INT64
    uint64_t = UINT64

    __UMACHINE_H__ = 0

    from km.crt.stddef_h import * # NOQA

    U_CFUNC = VOID
    U_CDECL_BEGIN = 0
    U_CDECL_END = 0

    def U_ATTRIBUTE_DEPRECATED(deprecated):
        pass

    U_CAPI = U_EXPORT
    U_STABLE = U_CAPI
    U_DRAFT = U_CAPI
    U_DEPRECATED = U_ATTRIBUTE_DEPRECATED
    U_OBSOLETE = U_CAPI
    U_INTERNAL = U_CAPI


    def U_OVERRIDE(override):
        pass


    def U_FINAL(final):
        pass

    INT8_MIN = int8_t(-128)
    INT16_MIN = int16_t(-32767 - 1)
    INT32_MIN = int32_t(-2147483647 - 1)
    INT8_MAX = int8_t(127)
    INT16_MAX = int16_t(32767)
    INT32_MAX = int32_t(2147483647)
    UINT8_MAX = uint8_t(255)
    UINT16_MAX = uint16_t(65535)
    UINT32_MAX = uint32_t(4294967295)


    def INT64_C(c):
        return c


    def UINT64_C(c):
        return c


    U_INT64_MIN = int64_t(INT64_C(-9223372036854775807) - 1)
    U_INT64_MAX = int64_t(INT64_C(9223372036854775807))
    U_UINT64_MAX = uint64_t(UINT64_C(18446744073709551615))
    UBool = int8_t
    TRUE = 1
    FALSE = 0

    U_WCHAR_IS_UTF16 = 0
    U_WCHAR_IS_UTF32 = None

    U_SIZEOF_UCHAR = 0x00000002
    UCHAR_TYPE = None
    UChar = uint16_t
    OldUChar = ctypes.c_wchar
    UChar32 = int32_t
    U_SENTINEL = -1

    __UTF_H__ = 0


    def U_IS_UNICODE_NONCHAR(c):
        return (
            c >= 0xfdd0 and
            (uint32_t(c).value <= 0xfdef or c & 0xfffe == 0xfffe) and
            uint32_t(c).value <= 0x10ffff
        )


    def U_IS_UNICODE_CHAR(c):
        return (
            uint32_t(c).value < 0xd800 or
            (
                uint32_t(c).value > 0xdfff and
                uint32_t(c).value <= 0x10ffff and
                not U_IS_UNICODE_NONCHAR(c)
            )
        )


    def U_IS_BMP(c):
        return uint32_t(c).value <= 0xffff


    def U_IS_SUPPLEMENTARY(c):
        return uint32_t(c - 0x10000).value <= 0xfffff


    def U_IS_LEAD(c):
        return c & 0xfffffc00 == 0xd800


    def U_IS_TRAIL(c):
        return c & 0xfffffc00 == 0xdc00


    def U_IS_SURROGATE(c):
        return c & 0xfffff800 == 0xd800


    def U_IS_SURROGATE_LEAD(c):
        return c & 0x400 == 0


    def U_IS_SURROGATE_TRAIL(c):
        return c & 0x400 != 0


    __UTF8_H__ = 0



    def U8_COUNT_TRAIL_BYTES(leadByte):
        if uint8_t(leadByte).value < 0xf0:
            return (
                int(uint8_t(leadByte).value >= 0xc0) +
                int(uint8_t(leadByte).value >= 0xe0)
            )
        elif uint8_t(leadByte).value < 0xfe:
            return (
                3 +
                int(uint8_t(leadByte).value >= 0xf8) +
                int(uint8_t(leadByte).value >= 0xfc)
            )
        else:
            return 0


    def U8_COUNT_TRAIL_BYTES_UNSAFE(leadByte):
        return (
            int(leadByte >= 0xc0) +
            int(leadByte >= 0xe0) +
            int(leadByte >= 0xf0)
        )


    def U8_MASK_LEAD_BYTE(leadByte, countTrailBytes):
        leadByte &= (1 << (6 - countTrailBytes)) -1
        return leadByte


    def U8_IS_SINGLE(c):
        return c & 0x80 == 0


    def U8_IS_LEAD(c):
        return uint8_t(c - 0xc0).value < 0x3e


    def U8_IS_TRAIL(c):
        return c & 0xc0 == 0x80


    def U8_LENGTH(c):
        if uint32_t(c).value <= 0x7f:
            return 1
        elif uint32_t(c).value <= 0x7ff:
            return 2
        elif uint32_t(c).value <= 0xd7ff:
            return 3
        elif uint32_t(c).value <= 0xdfff or uint32_t(c).value > 0x10ffff:
            return 0
        elif uint32_t(c).value <= 0xffff:
            return 3
        else:
            return 4


    U8_MAX_LENGTH = 0x00000004


    def U8_GET_UNSAFE(s, i, c):
        _u8_get_unsafe_index = int32_t(i).value
        _u8_get_unsafe_index = U8_SET_CP_START_UNSAFE(s, _u8_get_unsafe_index)
        return U8_NEXT_UNSAFE(s, _u8_get_unsafe_index, c)


    def U8_GET(s, start, i, length, c):
        _u8_get_index = uint32_t(i).value
        _u8_get_index = U8_SET_CP_START(s, start, _u8_get_index)
        return U8_NEXT(s, _u8_get_index, length, c)


    def U8_GET_OR_FFFD(s, start, i, length, c):
        _u8_get_index = uint8_t(i).value
        _u8_get_index = U8_SET_CP_START(s, start, _u8_get_index)
        return U8_NEXT_OR_FFFD(s, _u8_get_index, length, c)


    def U8_NEXT_UNSAFE(s, i, c):
        c= uint8_t(s).value[i + 1]
        if c >= 0x80:
            if c < 0xe0:
                c = (
                    ((c & 0x1f) << 6) |
                    (s[i + 1] & 0x3f)
                )
            elif c < 0xf0:
                c = UChar(
                    (c << 12) |
                    ((s[i] & 0x3f) << 6) |
                    (s[i + 1] & 0x3f)
                ).value
                i += 2
            else:
                c = (
                    ((c & 7) << 18) |
                    ((s[i] & 0x3f) << 12) |
                    ((s[i + 1] & 0x3f) << 6) |
                    (s[i + 2] & 0x3f)
                )
                i += 3
        return s, i, c



    def U8_NEXT(s, i, length, c):
        c = uint8_t(s).value[i + 1]
        if c >= 0x80:
            __t1 = uint8_t(s[i] - 0x80).value
            __t2 = uint8_t(s[i + 1] - 0x80).value
            if (
                0xe0 < c <= 0xec and
                ((i + 1) < length or length < 0) and
                __t1 <= 0x3f and
                __t2 <= 0x3f
            ):
                c = UChar((c << 12) | (__t1 << 6) | __t2).value
                i += 2
            elif (
                0xc2 <= c < 0xe0 and
                i != length and
                uint8_t(s[i] - 0x80).value <= 0x3f
            ):
                __t1 = uint8_t(s[i] - 0x80).value
                c = ((c & 0x1f) << 6) | __t1
                i = i + i
            else:
                c = utf8_nextCharSafeBody(
                    ctypes.byref(uint8_t(s)),
                    i,
                    length,
                    c,
                    -1
                )
        return i, c


    # def U8_NEXT_OR_FFFD(s, i, length, c):
    #     return { c=uint8_ts[i++]; if(c>=0x80) { uint8_t __t1, __t2; if( (0xe0<c and c<=0xec) and ((i+1)<length or length<0) and (__t1=uint8_t(s[i]-0x80))<=0x3f and (__t2=uint8_t(s[i+1]-0x80))<= 0x3f ) {
    #
    #
    # def U8_APPEND_UNSAFE(s, i, c):
    #     return { if(uint32_tc<=0x7f) { s[i++]=uint8_tc; } else { if(uint32_tc<=0x7ff) { s[i++]=uint8_t((c>>6)|0xc0); } else { if(uint32_tc<=0xffff) { s[i++]=uint8_t((c>>12)|0xe0); } else { s[i++]=uint8_t((c>>18)|0xf0); s[i++]=uint8_t(((c>>12)&0x3f)|0x80); } s[i++]=uint8_t(((c>>6)&0x3f)|0x80); } s[i++]=uint8_t((c&0x3f)|0x80); } }
    #
    #
    # def U8_APPEND(s, i, capacity, c, isError):
    #     return { ifuint32_tc<=0x7f) { s[i++]=uint8_tc; } else if(uint32_tc<=0x7ff and i+1<capacity { s[i++]=uint8_t((c>>6)|0xc0); s[i++]=uint8_t((c&0x3f)|0x80); } else if(uint32_tc<=0xd7ff and i+2<capacity) { s[i++]=uint8_t((c>>12)|0xe0); s[i++]=uint8_t(((c>>6)&0x3f)|0x80); s[i++]=uint8_t((c&0x3f)|0x80); } else { i=utf8_appendCharSafeBody(s, i, capacity, c, &isError); } }
    #
    #
    # def U8_FWD_1_UNSAFE(s, i):
    #     return { i+=1+U8_COUNT_TRAIL_BYTES_UNSAFE(uint8_ts[i]); }
    #
    #
    # def U8_FWD_1(s, i, length):
    #     return { uint8_t __b=uint8_ts[i++]; if(U8_IS_LEAD__b { uint8_t __count=U8_COUNT_TRAIL_BYTES__b; ifi+__count>length and length>=0) { __count=uint8_t(length-i); } while(__count>0 and U8_IS_TRAIL(s[i])) { ++i; --__count; } } }
    #
    #
    # def U8_FWD_N_UNSAFE(s, i, n):
    #     return { int32_t __N=n; while(__N>0) { U8_FWD_1_UNSAFEs, i; --__N; } }
    #
    #
    # def U8_FWD_N(s, i, length, n):
    #     return { int32_t __N=n; while(__N>0 and i<length or (length<0 and s[i]!=0)) { U8_FWD_1s, i, length; --__N; } }
    #
    #
    # def U8_SET_CP_START_UNSAFE(s, i):
    #     return { while(U8_IS_TRAIL(s[i])) { --i; } }
    #
    #
    # def U8_SET_CP_START(s, start, i):
    #     return { if(U8_IS_TRAIL(s[i])) { i=utf8_back1SafeBody(s, start, i); } }
    #
    #
    # def U8_PREV_UNSAFE(s, i, c):
    #     return { c=uint8_ts[--i]; if(U8_IS_TRAILc) { uint8_t __b, __count=1, __shift=6;
    #
    #
    # def U8_PREV(s, start, i, c):
    #     return { c=uint8_ts[--i]; if(c>=0x80) { c=utf8_prevCharSafeBody(uint8_t *s, start, &i, c, -1); } }
    #
    #
    # def U8_PREV_OR_FFFD(s, start, i, c):
    #     return { c=uint8_ts[--i]; if(c>=0x80) { c=utf8_prevCharSafeBody(uint8_t *s, start, &i, c, -3); } }
    #
    #
    # def U8_BACK_1_UNSAFE(s, i):
    #     return { while(U8_IS_TRAIL(s[--i])) {} }
    #
    #
    # def U8_BACK_1(s, start, i):
    #     return { if(U8_IS_TRAIL(s[--i])) { i=utf8_back1SafeBody(s, start, i); } }
    #
    #
    # def U8_BACK_N_UNSAFE(s, i, n):
    #     return { int32_t __N=n; while(__N>0) { U8_BACK_1_UNSAFEs, i; --__N; } }
    #
    #
    # def U8_BACK_N(s, start, i, n):
    #     return { int32_t __N=n; while(__N>0 and i>start) { U8_BACK_1s, start, i; --__N; } }
    #
    #
    # def U8_SET_CP_LIMIT_UNSAFE(s, i):
    #     return { U8_BACK_1_UNSAFEs, i; U8_FWD_1_UNSAFEs, i; }
    #
    #
    # def U8_SET_CP_LIMIT(s, start, i, length):
    #     return { ifstart<i and (i<length or length<0) { U8_BACK_1s, start, i; U8_FWD_1s, i, length; } }
    #
    #
    # def U16_IS_SINGLE(c):
    #     return !U_IS_SURROGATEc
    #
    #
    # def U16_IS_LEAD(c):
    #     return ((c&0xfffffc00)==0xd800)
    #
    #
    # def U16_IS_TRAIL(c):
    #     return ((c&0xfffffc00)==0xdc00)
    #
    #
    # def U16_IS_SURROGATE(c):
    #     return U_IS_SURROGATEc
    #
    #
    # def U16_IS_SURROGATE_LEAD(c):
    #     return ((c&0x400)==0)
    #
    #
    # def U16_IS_SURROGATE_TRAIL(c):
    #     return ((c&0x400)!=0)
    # U16_SURROGATE_OFFSET = (0xd800<<10UL)+0xdc00-0x10000
    #
    #
    # def U16_GET_SUPPLEMENTARY(lead, trail):
    #     return ((UChar32lead<<10UL)+UChar32trail-U16_SURROGATE_OFFSET)
    #
    #
    # def U16_LEAD(supplementary):
    #     return UChar((supplementary>>10)+0xd7c0)
    #
    #
    # def U16_TRAIL(supplementary):
    #     return UChar((supplementary&0x3ff)|0xdc00)
    #
    #
    # def U16_LENGTH(c):
    #     return (uint32_tc<=0xffff ? 1 : 2)
    # U16_MAX_LENGTH = 0x00000002
    #
    #
    # def U16_GET_UNSAFE(s, i, c):
    #     return { c=s[i]; if(U16_IS_SURROGATEc { if(U16_IS_SURROGATE_LEADc) { c=U16_GET_SUPPLEMENTARYc, s[i+1]); } else { c=U16_GET_SUPPLEMENTARY(s[i-1], c); } } }
    #
    #
    # def U16_GET(s, start, i, length, c):
    #     return { c=s[i]; if(U16_IS_SURROGATEc { uint16_t __c2; if(U16_IS_SURROGATE_LEADc) { ifi+1!=length and U16_IS_TRAIL(__c2=s[i+1])) { c=U16_GET_SUPPLEMENTARY(c, __c2); } } else { if(i>start and U16_IS_LEAD(__c2=s[i-1])) { c=U16_GET_SUPPLEMENTARY(__c2, c); } } } }
    #
    #
    # def U16_NEXT_UNSAFE(s, i, c):
    #     return { c=s[i++]; if(U16_IS_LEADc { c=U16_GET_SUPPLEMENTARYc, s[i++]); } }
    #
    #
    # def U16_NEXT(s, i, length, c):
    #     return { c=s[i++]; if(U16_IS_LEADc { uint16_t __c2; ifi!=length and U16_IS_TRAIL(__c2=s[i])) { ++i; c=U16_GET_SUPPLEMENTARY(c, __c2); } } }
    #
    #
    # def U16_APPEND_UNSAFE(s, i, c):
    #     return { if(uint32_tc<=0xffff) { s[i++]=uint16_tc; } else { s[i++]=uint16_t((c>>10)+0xd7c0); s[i++]=uint16_t((c&0x3ff)|0xdc00); } }
    #
    #
    # def U16_APPEND(s, i, capacity, c, isError):
    #     return { ifuint32_tc<=0xffff) { s[i++]=uint16_tc; } else if(uint32_tc<=0x10ffff and i+1<capacity { s[i++]=uint16_t((c>>10)+0xd7c0); s[i++]=uint16_t((c&0x3ff)|0xdc00); } else { isError=TRUE; } }
    #
    #
    # def U16_FWD_1_UNSAFE(s, i):
    #     return { if(U16_IS_LEAD(s[i++])) { ++i; } }
    #
    #
    # def U16_FWD_1(s, i, length):
    #     return { if(U16_IS_LEAD(s[i++]) and i!=length and U16_IS_TRAIL(s[i])) { ++i; } }
    #
    #
    # def U16_FWD_N_UNSAFE(s, i, n):
    #     return { int32_t __N=n; while(__N>0) { U16_FWD_1_UNSAFEs, i; --__N; } }
    #
    #
    # def U16_FWD_N(s, i, length, n):
    #     return { int32_t __N=n; while(__N>0 and i<length or (length<0 and s[i]!=0)) { U16_FWD_1s, i, length; --__N; } }
    #
    #
    # def U16_SET_CP_START_UNSAFE(s, i):
    #     return { if(U16_IS_TRAIL(s[i])) { --i; } }
    #
    #
    # def U16_SET_CP_START(s, start, i):
    #     return { if(U16_IS_TRAIL(s[i]) and i>start and U16_IS_LEAD(s[i-1])) { --i; } }
    #
    #
    # def U16_PREV_UNSAFE(s, i, c):
    #     return { c=s[--i]; if(U16_IS_TRAILc { c=U16_GET_SUPPLEMENTARYs[--i], c); } }
    #
    #
    # def U16_PREV(s, start, i, c):
    #     return { c=s[--i]; if(U16_IS_TRAILc { uint16_t __c2; ifi>start and U16_IS_LEAD(__c2=s[i-1])) { --i; c=U16_GET_SUPPLEMENTARY(__c2, c); } } }
    #
    #
    # def U16_BACK_1_UNSAFE(s, i):
    #     return { if(U16_IS_TRAIL(s[--i])) { --i; } }
    #
    #
    # def U16_BACK_1(s, start, i):
    #     return { if(U16_IS_TRAIL(s[--i]) and i>start and U16_IS_LEAD(s[i-1])) { --i; } }
    #
    #
    # def U16_BACK_N_UNSAFE(s, i, n):
    #     return { int32_t __N=n; while(__N>0) { U16_BACK_1_UNSAFEs, i; --__N; } }
    #
    #
    # def U16_BACK_N(s, start, i, n):
    #     return { int32_t __N=n; while(__N>0 and i>start) { U16_BACK_1s, start, i; --__N; } }
    #
    #
    # def U16_SET_CP_LIMIT_UNSAFE(s, i):
    #     return { if(U16_IS_LEAD(s[i-1])) { ++i; } }
    #
    #
    # def U16_SET_CP_LIMIT(s, start, i, length):
    #     return { ifstart<i and (i<length or length<0) and U16_IS_LEAD(s[i-1]) and U16_IS_TRAIL(s[i]) { ++i; } }


U_COPYRIGHT_STRING_LENGTH = 0x00000080
U_MAX_VERSION_LENGTH = 0x00000004
U_VERSION_DELIMITER = '.'
U_MAX_VERSION_STRING_LENGTH = 0x00000014
# UVersionInfo[U_MAX_VERSION_LENGTH] = uint8_t


# from float_h import * # NOQA

#
# U_ICUDATA_TYPE_LETTER = "e"
# U_ICUDATA_TYPE_LITLETTER = e
# U_ICUDATA_TYPE_LETTER = "x"
# U_ICUDATA_TYPE_LITLETTER = x
# U_ICUDATA_TYPE_LETTER = "b"
# U_ICUDATA_TYPE_LITLETTER = b
# U_ICUDATA_TYPE_LETTER = "l"
# U_ICUDATA_TYPE_LITLETTER = l
# U_ICUDATA_NAME = "icudt" U_ICU_VERSION_SHORT U_ICUDATA_TYPE_LETTER\n"
# U_ICUDATA_ENTRY_POINT = U_DEF2_ICUDATA_ENTRY_POINT(
#     U_ICU_VERSION_MAJOR_NUM,
#     U_LIB_SUFFIX_C_NAME,
# )
# UDate = DOUBLE
# U_MILLIS_PER_SECOND = 0x000003E8
# U_MILLIS_PER_MINUTE = 0x0000EA60
# U_MILLIS_PER_HOUR = 0x0036EE80
# U_MILLIS_PER_DAY = 0x05265C00
# U_DATE_MAX = DBL_MAX
# U_DATE_MIN = -U_DATE_MAX
# U_DATA_API = U_EXPORT
# U_COMMON_API = U_EXPORT
# U_I18N_API = U_EXPORT
# U_LAYOUT_API = U_EXPORT
# U_LAYOUTEX_API = U_EXPORT
# U_IO_API = U_EXPORT
# U_TOOLUTIL_API = U_EXPORT
# U_DATA_API = U_IMPORT
# U_COMMON_API = U_EXPORT
# U_I18N_API = U_IMPORT
# U_LAYOUT_API = U_IMPORT
# U_LAYOUTEX_API = U_IMPORT
# U_IO_API = U_IMPORT
# U_TOOLUTIL_API = U_IMPORT
# U_DATA_API = U_IMPORT
# U_COMMON_API = U_IMPORT
# U_I18N_API = U_EXPORT
# U_LAYOUT_API = U_IMPORT
# U_LAYOUTEX_API = U_IMPORT
# U_IO_API = U_IMPORT
# U_TOOLUTIL_API = U_IMPORT
# U_DATA_API = U_IMPORT
# U_COMMON_API = U_IMPORT
# U_I18N_API = U_IMPORT
# U_LAYOUT_API = U_EXPORT
# U_LAYOUTEX_API = U_IMPORT
# U_IO_API = U_IMPORT
# U_TOOLUTIL_API = U_IMPORT
# U_DATA_API = U_IMPORT
# U_COMMON_API = U_IMPORT
# U_I18N_API = U_IMPORT
# U_LAYOUT_API = U_IMPORT
# U_LAYOUTEX_API = U_EXPORT
# U_IO_API = U_IMPORT
# U_TOOLUTIL_API = U_IMPORT
# U_DATA_API = U_IMPORT
# U_COMMON_API = U_IMPORT
# U_I18N_API = U_IMPORT
# U_LAYOUT_API = U_IMPORT
# U_LAYOUTEX_API = U_IMPORT
# U_IO_API = U_EXPORT
# U_TOOLUTIL_API = U_IMPORT
# U_DATA_API = U_IMPORT
# U_COMMON_API = U_IMPORT
# U_I18N_API = U_IMPORT
# U_LAYOUT_API = U_IMPORT
# U_LAYOUTEX_API = U_IMPORT
# U_IO_API = U_IMPORT
# U_TOOLUTIL_API = U_EXPORT
# U_DATA_API = U_IMPORT
# U_COMMON_API = U_IMPORT
# U_I18N_API = U_IMPORT
# U_LAYOUT_API = U_IMPORT
# U_LAYOUTEX_API = U_IMPORT
# U_IO_API = U_IMPORT
# U_TOOLUTIL_API = U_IMPORT
# U_STANDARD_CPP_NAMESPACE = ::
# class UErrorCode(ENUM):
#     U_USING_FALLBACK_WARNING = - 128
#     U_ERROR_WARNING_START = - 128
#     U_USING_DEFAULT_WARNING = - 127
#     U_SAFECLONE_ALLOCATED_WARNING = - 126
#     U_STATE_OLD_WARNING = - 125
#     U_STRING_NOT_TERMINATED_WARNING = - 124
#     U_SORT_KEY_TOO_SHORT_WARNING = - 123
#     U_AMBIGUOUS_ALIAS_WARNING = - 122
#     U_DIFFERENT_UCA_VERSION = - 121
#     U_PLUGIN_CHANGED_LEVEL_WARNING = - 120
#     U_ZERO_ERROR = 0
#     U_ILLEGAL_ARGUMENT_ERROR = 1
#     U_MISSING_RESOURCE_ERROR = 2
#     U_INVALID_FORMAT_ERROR = 3
#     U_FILE_ACCESS_ERROR = 4
#     U_INTERNAL_PROGRAM_ERROR = 5
#     U_MESSAGE_PARSE_ERROR = 6
#     U_MEMORY_ALLOCATION_ERROR = 7
#     U_INDEX_OUTOFBOUNDS_ERROR = 8
#     U_PARSE_ERROR = 9
#     U_INVALID_CHAR_FOUND = 10
#     U_TRUNCATED_CHAR_FOUND = 11
#     U_ILLEGAL_CHAR_FOUND = 12
#     U_INVALID_TABLE_FORMAT = 13
#     U_INVALID_TABLE_FILE = 14
#     U_BUFFER_OVERFLOW_ERROR = 15
#     U_UNSUPPORTED_ERROR = 16
#     U_RESOURCE_TYPE_MISMATCH = 17
#     U_ILLEGAL_ESCAPE_SEQUENCE = 18
#     U_UNSUPPORTED_ESCAPE_SEQUENCE = 19
#     U_NO_SPACE_AVAILABLE = 20
#     U_CE_NOT_FOUND_ERROR = 21
#     U_PRIMARY_TOO_LONG_ERROR = 22
#     U_STATE_TOO_OLD_ERROR = 23
#     U_TOO_MANY_ALIASES_ERROR = (
#         24     /**< There are too many aliases in the path to the requested resource.
#     )
#     It is very possible that a circular alias definition has occured */ = 24
#     U_ENUM_OUT_OF_SYNC_ERROR = 25
#     U_INVARIANT_CONVERSION_ERROR = 26
#     U_INVALID_STATE_ERROR = 27
#     U_COLLATOR_VERSION_MISMATCH = 28
#     U_USELESS_COLLATOR_ERROR = 29
#     U_NO_WRITE_PERMISSION = 30
#     U_BAD_VARIABLE_DEFINITION = 0x10000
#     U_PARSE_ERROR_START = 0x10000
#     U_MALFORMED_RULE = 65537
#     U_MALFORMED_SET = 65538
#     U_MALFORMED_SYMBOL_REFERENCE = 65539
#     U_MALFORMED_UNICODE_ESCAPE = 65540
#     U_MALFORMED_VARIABLE_DEFINITION = 65541
#     U_MALFORMED_VARIABLE_REFERENCE = 65542
#     U_MISMATCHED_SEGMENT_DELIMITERS = 65543
#     U_MISPLACED_ANCHOR_START = 65544
#     U_MISPLACED_CURSOR_OFFSET = 65545
#     U_MISPLACED_QUANTIFIER = 65546
#     U_MISSING_OPERATOR = 65547
#     U_MISSING_SEGMENT_CLOSE = 65548
#     U_MULTIPLE_ANTE_CONTEXTS = 65549
#     U_MULTIPLE_CURSORS = 65550
#     U_MULTIPLE_POST_CONTEXTS = 65551
#     U_TRAILING_BACKSLASH = 65552
#     U_UNDEFINED_SEGMENT_REFERENCE = 65553
#     U_UNDEFINED_VARIABLE = 65554
#     U_UNQUOTED_SPECIAL = 65555
#     U_UNTERMINATED_QUOTE = 65556
#     U_RULE_MASK_ERROR = 65557
#     U_MISPLACED_COMPOUND_FILTER = 65558
#     U_MULTIPLE_COMPOUND_FILTERS = 65559
#     U_INVALID_RBT_SYNTAX = 65560
#     U_INVALID_PROPERTY_PATTERN = 65561
#     U_MALFORMED_PRAGMA = 65562
#     U_UNCLOSED_SEGMENT = 65563
#     U_ILLEGAL_CHAR_IN_SEGMENT = 65564
#     U_VARIABLE_RANGE_EXHAUSTED = 65565
#     U_VARIABLE_RANGE_OVERLAP = 65566
#     U_ILLEGAL_CHARACTER = 65567
#     U_INTERNAL_TRANSLITERATOR_ERROR = 65568
#     U_INVALID_ID = 65569
#     U_INVALID_FUNCTION = 65570
#     U_UNEXPECTED_TOKEN = 0x10100
#     U_FMT_PARSE_ERROR_START = 0x10100
#     U_MULTIPLE_DECIMAL_SEPARATORS = 65793
#     U_MULTIPLE_DECIMAL_SEPERATORS = U_MULTIPLE_DECIMAL_SEPARATORS
#     U_MULTIPLE_EXPONENTIAL_SYMBOLS = 65794
#     U_MALFORMED_EXPONENTIAL_PATTERN = 65795
#     U_MULTIPLE_PERCENT_SYMBOLS = 65796
#     U_MULTIPLE_PERMILL_SYMBOLS = 65797
#     U_MULTIPLE_PAD_SPECIFIERS = 65798
#     U_PATTERN_SYNTAX_ERROR = 65799
#     U_ILLEGAL_PAD_POSITION = 65800
#     U_UNMATCHED_BRACES = 65801
#     U_UNSUPPORTED_PROPERTY = 65802
#     U_UNSUPPORTED_ATTRIBUTE = 65803
#     U_ARGUMENT_TYPE_MISMATCH = 65804
#     U_DUPLICATE_KEYWORD = 65805
#     U_UNDEFINED_KEYWORD = 65806
#     U_DEFAULT_KEYWORD_MISSING = 65807
#     U_DECIMAL_NUMBER_SYNTAX_ERROR = 65808
#     U_FORMAT_INEXACT_ERROR = 65809
#     U_BRK_INTERNAL_ERROR = 0x10200
#     U_BRK_ERROR_START = 0x10200
#     U_BRK_HEX_DIGITS_EXPECTED = 66049
#     U_BRK_SEMICOLON_EXPECTED = 66050
#     U_BRK_RULE_SYNTAX = 66051
#     U_BRK_UNCLOSED_SET = 66052
#     U_BRK_ASSIGN_ERROR = 66053
#     U_BRK_VARIABLE_REDFINITION = 66054
#     U_BRK_MISMATCHED_PAREN = 66055
#     U_BRK_NEW_LINE_IN_QUOTED_STRING = 66056
#     U_BRK_UNDEFINED_VARIABLE = 66057
#     U_BRK_INIT_ERROR = 66058
#     U_BRK_RULE_EMPTY_SET = 66059
#     U_BRK_UNRECOGNIZED_OPTION = 66060
#     U_BRK_MALFORMED_RULE_TAG = 66061
#     U_REGEX_INTERNAL_ERROR = 0x10300
#     U_REGEX_ERROR_START = 0x10300
#     U_REGEX_RULE_SYNTAX = 66305
#     U_REGEX_INVALID_STATE = 66306
#     U_REGEX_BAD_ESCAPE_SEQUENCE = 66307
#     U_REGEX_PROPERTY_SYNTAX = 66308
#     U_REGEX_UNIMPLEMENTED = 66309
#     U_REGEX_MISMATCHED_PAREN = 66310
#     U_REGEX_NUMBER_TOO_BIG = 66311
#     U_REGEX_BAD_INTERVAL = 66312
#     U_REGEX_MAX_LT_MIN = 66313
#     U_REGEX_INVALID_BACK_REF = 66314
#     U_REGEX_INVALID_FLAG = 66315
#     U_REGEX_LOOK_BEHIND_LIMIT = 66316
#     U_REGEX_SET_CONTAINS_STRING = 66317
#     U_REGEX_MISSING_CLOSE_BRACKET = U_REGEX_SET_CONTAINS_STRING + 2
#     U_REGEX_INVALID_RANGE = 66318
#     U_REGEX_STACK_OVERFLOW = 66319
#     U_REGEX_TIME_OUT = 66320
#     U_REGEX_STOPPED_BY_CALLER = 66321
#     U_REGEX_PATTERN_TOO_BIG = 66322
#     U_REGEX_INVALID_CAPTURE_GROUP_NAME = 66323
#     U_IDNA_PROHIBITED_ERROR = 0x10400
#     U_IDNA_ERROR_START = 0x10400
#     U_IDNA_UNASSIGNED_ERROR = 66561
#     U_IDNA_CHECK_BIDI_ERROR = 66562
#     U_IDNA_STD3_ASCII_RULES_ERROR = 66563
#     U_IDNA_ACE_PREFIX_ERROR = 66564
#     U_IDNA_VERIFICATION_ERROR = 66565
#     U_IDNA_LABEL_TOO_LONG_ERROR = 66566
#     U_IDNA_ZERO_LENGTH_LABEL_ERROR = 66567
#     U_IDNA_DOMAIN_NAME_TOO_LONG_ERROR = 66568
#     U_STRINGPREP_PROHIBITED_ERROR = U_IDNA_PROHIBITED_ERROR
#     U_STRINGPREP_UNASSIGNED_ERROR = U_IDNA_UNASSIGNED_ERROR
#     U_STRINGPREP_CHECK_BIDI_ERROR = U_IDNA_CHECK_BIDI_ERROR
#     U_PLUGIN_ERROR_START = 0x10500
#     U_PLUGIN_TOO_HIGH = 0x10500
#     U_PLUGIN_DIDNT_SET_LEVEL = 66817
#
#
#
#
#
# def U_SUCCESS(x):
#     return (x<=U_ZERO_ERROR)
#
#
# def U_FAILURE(x):
#     return (x>U_ZERO_ERROR)
# from stdarg_h import * # NOQA
# class UTraceLevel(ENUM):
#     UTRACE_OFF = - 1
#     UTRACE_ERROR = 0
#     UTRACE_WARNING = 3
#     UTRACE_OPEN_CLOSE = 5
#     UTRACE_INFO = 7
#     UTRACE_VERBOSE = 9
#
#
#
# class UTraceFunctionNumber(ENUM):
#     UTRACE_FUNCTION_START = 0
#     UTRACE_U_INIT = UTRACE_FUNCTION_START
#     UTRACE_U_CLEANUP = 1
#     UTRACE_CONVERSION_START = 0x1000
#     UTRACE_UCNV_OPEN = UTRACE_CONVERSION_START
#     UTRACE_UCNV_OPEN_PACKAGE = 4097
#     UTRACE_UCNV_OPEN_ALGORITHMIC = 4098
#     UTRACE_UCNV_CLONE = 4099
#     UTRACE_UCNV_CLOSE = 4100
#     UTRACE_UCNV_FLUSH_CACHE = 4101
#     UTRACE_UCNV_LOAD = 4102
#     UTRACE_UCNV_UNLOAD = 4103
#     UTRACE_COLLATION_START = 0x2000
#     UTRACE_UCOL_OPEN = UTRACE_COLLATION_START
#     UTRACE_UCOL_CLOSE = 8193
#     UTRACE_UCOL_STRCOLL = 8194
#     UTRACE_UCOL_GET_SORTKEY = 8195
#     UTRACE_UCOL_GETLOCALE = 8196
#     UTRACE_UCOL_NEXTSORTKEYPART = 8197
#     UTRACE_UCOL_STRCOLLITER = 8198
#     UTRACE_UCOL_OPEN_FROM_SHORT_STRING = 8199
#     UTRACE_UCOL_STRCOLLUTF8 = 8200
#
#
#
# class UStringTrieResult(ENUM):
#     USTRINGTRIE_NO_MATCH = 0
#     USTRINGTRIE_NO_VALUE = 1
#     USTRINGTRIE_FINAL_VALUE = 2
#     USTRINGTRIE_INTERMEDIATE_VALUE = 3
#
#
#  = UStringTrieResult
#
#
#
#
# def USTRINGTRIE_MATCHES(result):
#     return (result!=USTRINGTRIE_NO_MATCH)
#
#
# def USTRINGTRIE_HAS_VALUE(result):
#     return (result>=USTRINGTRIE_FINAL_VALUE)
#
#
# def USTRINGTRIE_HAS_NEXT(result):
#     return (result&1)
# U_SHAPE_LENGTH_GROW_SHRINK = 0x00000000
# U_SHAPE_LAMALEF_RESIZE = 0x00000000
# U_SHAPE_LENGTH_FIXED_SPACES_NEAR = 0x00000001
# U_SHAPE_LAMALEF_NEAR = 0x00000001
# U_SHAPE_LENGTH_FIXED_SPACES_AT_END = 0x00000002
# U_SHAPE_LAMALEF_END = 0x00000002
# U_SHAPE_LENGTH_FIXED_SPACES_AT_BEGINNING = 0x00000003
# U_SHAPE_LAMALEF_BEGIN = 0x00000003
# U_SHAPE_LAMALEF_AUTO = 0x00010000
# U_SHAPE_LENGTH_MASK = 0x00010003
# U_SHAPE_LAMALEF_MASK = 0x00010003
# U_SHAPE_TEXT_DIRECTION_LOGICAL = 0x00000000
# U_SHAPE_TEXT_DIRECTION_VISUAL_RTL = 0x00000000
# U_SHAPE_TEXT_DIRECTION_VISUAL_LTR = 0x00000004
# U_SHAPE_TEXT_DIRECTION_MASK = 0x00000004
# U_SHAPE_LETTERS_NOOP = 0x00000000
# U_SHAPE_LETTERS_SHAPE = 0x00000008
# U_SHAPE_LETTERS_UNSHAPE = 0x00000010
# U_SHAPE_LETTERS_SHAPE_TASHKEEL_ISOLATED = 0x00000018
# U_SHAPE_LETTERS_MASK = 0x00000018
# U_SHAPE_DIGITS_NOOP = 0x00000000
# U_SHAPE_DIGITS_EN2AN = 0x00000020
# U_SHAPE_DIGITS_AN2EN = 0x00000040
# U_SHAPE_DIGITS_ALEN2AN_INIT_LR = 0x00000060
# U_SHAPE_DIGITS_ALEN2AN_INIT_AL = 0x00000080
# U_SHAPE_DIGITS_RESERVED = 0x000000A0
# U_SHAPE_DIGITS_MASK = 0x000000E0
# U_SHAPE_DIGIT_TYPE_AN = 0x00000000
# U_SHAPE_DIGIT_TYPE_AN_EXTENDED = 0x00000100
# U_SHAPE_DIGIT_TYPE_RESERVED = 0x00000200
# U_SHAPE_DIGIT_TYPE_MASK = 0x00000300
# U_SHAPE_AGGREGATE_TASHKEEL = 0x00004000
# U_SHAPE_AGGREGATE_TASHKEEL_NOOP = 0x00000000
# U_SHAPE_AGGREGATE_TASHKEEL_MASK = 0x00004000
# U_SHAPE_PRESERVE_PRESENTATION = 0x00008000
# U_SHAPE_PRESERVE_PRESENTATION_NOOP = 0x00000000
# U_SHAPE_PRESERVE_PRESENTATION_MASK = 0x00008000
# U_SHAPE_SEEN_TWOCELL_NEAR = 0x00200000
# U_SHAPE_SEEN_MASK = 0x00700000
# U_SHAPE_YEHHAMZA_TWOCELL_NEAR = 0x01000000
# U_SHAPE_YEHHAMZA_MASK = 0x03800000
# U_SHAPE_TASHKEEL_BEGIN = 0x00040000
# U_SHAPE_TASHKEEL_END = 0x00060000
# U_SHAPE_TASHKEEL_RESIZE = 0x00080000
# U_SHAPE_TASHKEEL_REPLACE_BY_TATWEEL = 0x000C0000
# U_SHAPE_TASHKEEL_MASK = 0x000E0000
# U_SHAPE_SPACES_RELATIVE_TO_TEXT_BEGIN_END = 0x04000000
# U_SHAPE_SPACES_RELATIVE_TO_TEXT_MASK = 0x04000000
# U_SHAPE_TAIL_NEW_UNICODE = 0x08000000
# U_SHAPE_TAIL_TYPE_MASK = 0x08000000
# class UScriptCode(ENUM):
#     USCRIPT_INVALID_CODE = - 1
#     USCRIPT_COMMON = 0
#     USCRIPT_INHERITED = (
#         1   /* "Code for inherited script" for non - spacing combining marks; also Qaai */
#     )
#     USCRIPT_ARABIC = 2
#     USCRIPT_ARMENIAN = 3
#     USCRIPT_BENGALI = 4
#     USCRIPT_BOPOMOFO = 5
#     USCRIPT_CHEROKEE = 6
#     USCRIPT_COPTIC = 7
#     USCRIPT_CYRILLIC = 8
#     USCRIPT_DESERET = 9
#     USCRIPT_DEVANAGARI = 10
#     USCRIPT_ETHIOPIC = 11
#     USCRIPT_GEORGIAN = 12
#     USCRIPT_GOTHIC = 13
#     USCRIPT_GREEK = 14
#     USCRIPT_GUJARATI = 15
#     USCRIPT_GURMUKHI = 16
#     USCRIPT_HAN = 17
#     USCRIPT_HANGUL = 18
#     USCRIPT_HEBREW = 19
#     USCRIPT_HIRAGANA = 20
#     USCRIPT_KANNADA = 21
#     USCRIPT_KATAKANA = 22
#     USCRIPT_KHMER = 23
#     USCRIPT_LAO = 24
#     USCRIPT_LATIN = 25
#     USCRIPT_MALAYALAM = 26
#     USCRIPT_MONGOLIAN = 27
#     USCRIPT_MYANMAR = 28
#     USCRIPT_OGHAM = 29
#     USCRIPT_OLD_ITALIC = 30
#     USCRIPT_ORIYA = 31
#     USCRIPT_RUNIC = 32
#     USCRIPT_SINHALA = 33
#     USCRIPT_SYRIAC = 34
#     USCRIPT_TAMIL = 35
#     USCRIPT_TELUGU = 36
#     USCRIPT_THAANA = 37
#     USCRIPT_THAI = 38
#     USCRIPT_TIBETAN = 39
#     USCRIPT_CANADIAN_ABORIGINAL = 40
#     USCRIPT_UCAS = USCRIPT_CANADIAN_ABORIGINAL
#     USCRIPT_YI = 41
#     USCRIPT_TAGALOG = 42
#     USCRIPT_HANUNOO = 43
#     USCRIPT_BUHID = 44
#     USCRIPT_TAGBANWA = 45
#     USCRIPT_BRAILLE = 46
#     USCRIPT_CYPRIOT = 47
#     USCRIPT_LIMBU = 48
#     USCRIPT_LINEAR_B = 49
#     USCRIPT_OSMANYA = 50
#     USCRIPT_SHAVIAN = 51
#     USCRIPT_TAI_LE = 52
#     USCRIPT_UGARITIC = 53
#     USCRIPT_KATAKANA_OR_HIRAGANA = 54
#     USCRIPT_BUGINESE = 55
#     USCRIPT_GLAGOLITIC = 56
#     USCRIPT_KHAROSHTHI = 57
#     USCRIPT_SYLOTI_NAGRI = 58
#     USCRIPT_NEW_TAI_LUE = 59
#     USCRIPT_TIFINAGH = 60
#     USCRIPT_OLD_PERSIAN = 61
#     USCRIPT_BALINESE = 62
#     USCRIPT_BATAK = 63
#     USCRIPT_BLISSYMBOLS = 64
#     USCRIPT_BRAHMI = 65
#     USCRIPT_CHAM = 66
#     USCRIPT_CIRTH = 67
#     USCRIPT_OLD_CHURCH_SLAVONIC_CYRILLIC = 68
#     USCRIPT_DEMOTIC_EGYPTIAN = 69
#     USCRIPT_HIERATIC_EGYPTIAN = 70
#     USCRIPT_EGYPTIAN_HIEROGLYPHS = 71
#     USCRIPT_KHUTSURI = 72
#     USCRIPT_SIMPLIFIED_HAN = 73
#     USCRIPT_TRADITIONAL_HAN = 74
#     USCRIPT_PAHAWH_HMONG = 75
#     USCRIPT_OLD_HUNGARIAN = 76
#     USCRIPT_HARAPPAN_INDUS = 77
#     USCRIPT_JAVANESE = 78
#     USCRIPT_KAYAH_LI = 79
#     USCRIPT_LATIN_FRAKTUR = 80
#     USCRIPT_LATIN_GAELIC = 81
#     USCRIPT_LEPCHA = 82
#     USCRIPT_LINEAR_A = 83
#     USCRIPT_MANDAIC = 84
#     USCRIPT_MANDAEAN = USCRIPT_MANDAIC
#     USCRIPT_MAYAN_HIEROGLYPHS = 85
#     USCRIPT_MEROITIC_HIEROGLYPHS = 86
#     USCRIPT_MEROITIC = USCRIPT_MEROITIC_HIEROGLYPHS
#     USCRIPT_NKO = 87
#     USCRIPT_ORKHON = 88
#     USCRIPT_OLD_PERMIC = 89
#     USCRIPT_PHAGS_PA = 90
#     USCRIPT_PHOENICIAN = 91
#     USCRIPT_MIAO = 92
#     USCRIPT_PHONETIC_POLLARD = USCRIPT_MIAO
#     USCRIPT_RONGORONGO = 93
#     USCRIPT_SARATI = 94
#     USCRIPT_ESTRANGELO_SYRIAC = 95
#     USCRIPT_WESTERN_SYRIAC = 96
#     USCRIPT_EASTERN_SYRIAC = 97
#     USCRIPT_TENGWAR = 98
#     USCRIPT_VAI = 99
#     USCRIPT_VISIBLE_SPEECH = 100
#     USCRIPT_CUNEIFORM = 101
#     USCRIPT_UNWRITTEN_LANGUAGES = 102
#     USCRIPT_UNKNOWN = (
#         103 /* Unknown="Code for uncoded script" for unasINT code poINTs */
#     )
#     USCRIPT_CARIAN = 104
#     USCRIPT_JAPANESE = 105
#     USCRIPT_LANNA = 106
#     USCRIPT_LYCIAN = 107
#     USCRIPT_LYDIAN = 108
#     USCRIPT_OL_CHIKI = 109
#     USCRIPT_REJANG = 110
#     USCRIPT_SAURASHTRA = 111
#     USCRIPT_SIGN_WRITING = 112
#     USCRIPT_SUNDANESE = 113
#     USCRIPT_MOON = 114
#     USCRIPT_MEITEI_MAYEK = 115
#     USCRIPT_IMPERIAL_ARAMAIC = 116
#     USCRIPT_AVESTAN = 117
#     USCRIPT_CHAKMA = 118
#     USCRIPT_KOREAN = 119
#     USCRIPT_KAITHI = 120
#     USCRIPT_MANICHAEAN = 121
#     USCRIPT_INSCRIPTIONAL_PAHLAVI = 122
#     USCRIPT_PSALTER_PAHLAVI = 123
#     USCRIPT_BOOK_PAHLAVI = 124
#     USCRIPT_INSCRIPTIONAL_PARTHIAN = 125
#     USCRIPT_SAMARITAN = 126
#     USCRIPT_TAI_VIET = 127
#     USCRIPT_MATHEMATICAL_NOTATION = 128
#     USCRIPT_SYMBOLS = 129
#     USCRIPT_BAMUM = 130
#     USCRIPT_LISU = 131
#     USCRIPT_NAKHI_GEBA = 132
#     USCRIPT_OLD_SOUTH_ARABIAN = 133
#     USCRIPT_BASSA_VAH = 134
#     USCRIPT_DUPLOYAN = 135
#     USCRIPT_ELBASAN = 136
#     USCRIPT_GRANTHA = 137
#     USCRIPT_KPELLE = 138
#     USCRIPT_LOMA = 139
#     USCRIPT_MENDE = 140
#     USCRIPT_MEROITIC_CURSIVE = 141
#     USCRIPT_OLD_NORTH_ARABIAN = 142
#     USCRIPT_NABATAEAN = 143
#     USCRIPT_PALMYRENE = 144
#     USCRIPT_KHUDAWADI = 145
#     USCRIPT_SINDHI = USCRIPT_KHUDAWADI
#     USCRIPT_WARANG_CITI = 146
#     USCRIPT_AFAKA = 147
#     USCRIPT_JURCHEN = 148
#     USCRIPT_MRO = 149
#     USCRIPT_NUSHU = 150
#     USCRIPT_SHARADA = 151
#     USCRIPT_SORA_SOMPENG = 152
#     USCRIPT_TAKRI = 153
#     USCRIPT_TANGUT = 154
#     USCRIPT_WOLEAI = 155
#     USCRIPT_ANATOLIAN_HIEROGLYPHS = 156
#     USCRIPT_KHOJKI = 157
#     USCRIPT_TIRHUTA = 158
#     USCRIPT_CAUCASIAN_ALBANIAN = 159
#     USCRIPT_MAHAJANI = 160
#     USCRIPT_AHOM = 161
#     USCRIPT_HATRAN = 162
#     USCRIPT_MODI = 163
#     USCRIPT_MULTANI = 164
#     USCRIPT_PAU_CIN_HAU = 165
#     USCRIPT_SIDDHAM = 166
#     USCRIPT_ADLAM = 167
#     USCRIPT_BHAIKSUKI = 168
#     USCRIPT_MARCHEN = 169
#     USCRIPT_NEWA = 170
#     USCRIPT_OSAGE = 171
#     USCRIPT_HAN_WITH_BOPOMOFO = 172
#     USCRIPT_JAMO = 173
#     USCRIPT_SYMBOLS_EMOJI = 174
#
#
#
# class UScriptUsage(ENUM):
#     USCRIPT_USAGE_NOT_ENCODED = 0
#     USCRIPT_USAGE_UNKNOWN = 1
#     USCRIPT_USAGE_EXCLUDED = 2
#     USCRIPT_USAGE_LIMITED_USE = 3
#     USCRIPT_USAGE_ASPIRATIONAL = 4
#     USCRIPT_USAGE_RECOMMENDED = 5
#
#
#
# UReplaceable = VOID*
#
# class UReplaceableCallbacks(ctypes.Structure):
#     _fields_ = [
#         (' rep)', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(int32_t)))))))))))))))))))))))),
#         (' rep', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(UChar)))))))))))))))))))))))),
#         ('int32_t offset)', UChar),
#         (' rep', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(UChar32)))))))))))))))))))))))))),
#         ('int32_t offset)', UChar32),
#         (' rep', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(VOID))))))))))))))))))))))))),
#         ('int32_t start', VOID),
#         ('int32_t limit', VOID),
#         (' text', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(VOID))))))),
#         ('int32_t textLength)', VOID),
#         (' rep', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(VOID))))))))))))))))))))))))),
#         ('int32_t start', VOID),
#         ('int32_t limit', VOID),
#         (' dst)', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(VOID))))))),
#         (' rep', POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(VOID)))))))))))))))))))))),
#         ('int32_t start', VOID),
#         ('int32_t limit', VOID),
#         ('int32_t dest)', VOID),
#     ]
#
#
#
# U_NO_THROW = throw()
# UClassID = VOID*
# from cstddef import * # NOQA
#  =
#
#
# U_COMPARE_CODE_POINT_ORDER = 0x00008000
#
# class UFieldPosition(ctypes.Structure):
#     _fields_ = [
#         ('field', int32_t),
#         ('beginIndex', int32_t),
#         ('endIndex', int32_t),
#     ]
#
#
#
# URegistryKey = VOID*
# UListFormatter = struct
#
#
#  =
#
#
# UCharIterator = struct
#
#
#  = UCharIterator;
#
#
# class UCharIteratorOrigin(ENUM):
#     UITER_START UITER_CURRENT UITER_LIMIT UITER_ZERO UITER_LENGTH = 0
#
#
#
# class (ENUM):
#     UITER_UNKNOWN_INDEX = - 2
#
#
#
# UITER_NO_STATE = (uint32_t)0xffffffff
#
# class UCharIterator(ctypes.Structure):
#     _fields_ = [
#         ('context', POINTER(VOID)),
#         ('length', int32_t),
#         ('start', int32_t),
#         ('index', int32_t),
#         ('limit', int32_t),
#         ('reservedField', int32_t),
#         ('getIndex', POINTER(UCharIteratorGetIndex)),
#         ('move', POINTER(UCharIteratorMove)),
#         ('hasNext', POINTER(UCharIteratorHasNext)),
#         ('hasPrevious', POINTER(UCharIteratorHasPrevious)),
#         ('current', POINTER(UCharIteratorCurrent)),
#         ('next', POINTER(UCharIteratorNext)),
#         ('previous', POINTER(UCharIteratorPrevious)),
#         ('reservedFn', POINTER(UCharIteratorReserved)),
#         ('getState', POINTER(UCharIteratorGetState)),
#         ('setState', POINTER(UCharIteratorSetState)),
#     ]
#
#
#
# UEnumeration = struct
#
#
# UEnumeration = UEnumeration
#
#
# ULOC_CHINESE = "zh"
# ULOC_ENGLISH = "en"
# ULOC_FRENCH = "fr"
# ULOC_GERMAN = "de"
# ULOC_ITALIAN = "it"
# ULOC_JAPANESE = "ja"
# ULOC_KOREAN = "ko"
# ULOC_SIMPLIFIED_CHINESE = "zh_CN"
# ULOC_TRADITIONAL_CHINESE = "zh_TW"
# ULOC_CANADA = "en_CA"
# ULOC_CANADA_FRENCH = "fr_CA"
# ULOC_CHINA = "zh_CN"
# ULOC_PRC = "zh_CN"
# ULOC_FRANCE = "fr_FR"
# ULOC_GERMANY = "de_DE"
# ULOC_ITALY = "it_IT"
# ULOC_JAPAN = "ja_JP"
# ULOC_KOREA = "ko_KR"
# ULOC_TAIWAN = "zh_TW"
# ULOC_UK = "en_GB"
# ULOC_US = "en_US"
# ULOC_LANG_CAPACITY = 0x0000000C
# ULOC_COUNTRY_CAPACITY = 0x00000004
# ULOC_FULLNAME_CAPACITY = 0x0000009D
# ULOC_SCRIPT_CAPACITY = 0x00000006
# ULOC_KEYWORDS_CAPACITY = 0x00000060
# ULOC_KEYWORD_AND_VALUES_CAPACITY = 0x00000064
# ULOC_KEYWORD_SEPARATOR = '@'
# ULOC_KEYWORD_SEPARATOR_UNICODE = 0x00000040
# ULOC_KEYWORD_ASSIGN = '='
# ULOC_KEYWORD_ASSIGN_UNICODE = 0x0000003D
# ULOC_KEYWORD_ITEM_SEPARATOR = ';'
# ULOC_KEYWORD_ITEM_SEPARATOR_UNICODE = 0x0000003B
# class ULocDataLocaleType(ENUM):
#     ULOC_ACTUAL_LOCALE = 0
#     ULOC_VALID_LOCALE = 1
#
#
#
# class ULayoutType(ENUM):
#     ULOC_LAYOUT_LTR = 0
#     ULOC_LAYOUT_RTL = 1
#     ULOC_LAYOUT_TTB = 2
#     ULOC_LAYOUT_BTT = 3
#     ULOC_LAYOUT_UNKNOWN = 4
#
#
#
# class UAcceptResult(ENUM):
#     ULOC_ACCEPT_FAILED = 0
#     ULOC_ACCEPT_VALID = 1
#     ULOC_ACCEPT_FALLBACK = 2   /* A fallback was found for example
#     Accept list contained 'ja_JP' = 2
#     which matched available locale 'ja'. */ = 3
#
#
#
# UResourceBundle = struct
#
#
# UResourceBundle = UResourceBundle
#
#
# class UResType(ENUM):
#     URES_NONE = - 1
#     URES_STRING = 0
#     URES_BINARY = 1
#     URES_TABLE = 2
#     URES_ALIAS = 3
#     URES_INT = 7
#     URES_ARRAY = 8
#     URES_INT_VECTOR = 14
#
#
#
# class UDisplayContextType(ENUM):
#     UDISPCTX_TYPE_DIALECT_HANDLING = 0
#     UDISPCTX_TYPE_CAPITALIZATION = 1
#     UDISPCTX_TYPE_DISPLAY_LENGTH = 2
#
#
#  = UDisplayContextType
#
#
# UDisplayContextType = UDisplayContextType
# class UDisplayContext(ENUM):
#     UDISPCTX_STANDARD_NAMES = (UDISPCTX_TYPE_DIALECT_HANDLING << 8) + 0
#     UDISPCTX_DIALECT_NAMES = (UDISPCTX_TYPE_DIALECT_HANDLING << 8) + 1
#     UDISPCTX_CAPITALIZATION_NONE = (UDISPCTX_TYPE_CAPITALIZATION << 8) + 0
#     UDISPCTX_CAPITALIZATION_FOR_MIDDLE_OF_SENTENCE = (
#         (UDISPCTX_TYPE_CAPITALIZATION << 8) + 1
#     )
#     UDISPCTX_CAPITALIZATION_FOR_BEGINNING_OF_SENTENCE = (
#         (UDISPCTX_TYPE_CAPITALIZATION << 8) + 2
#     )
#     UDISPCTX_CAPITALIZATION_FOR_UI_LIST_OR_MENU = (
#         (UDISPCTX_TYPE_CAPITALIZATION << 8) + 3
#     )
#     UDISPCTX_CAPITALIZATION_FOR_STANDALONE = (
#         (UDISPCTX_TYPE_CAPITALIZATION << 8) + 4
#     )
#     UDISPCTX_LENGTH_FULL = (UDISPCTX_TYPE_DISPLAY_LENGTH << 8) + 0
#     UDISPCTX_LENGTH_SHORT = (UDISPCTX_TYPE_DISPLAY_LENGTH << 8) + 1
#
#
#  = UDisplayContext
#
#
# UDisplayContext = UDisplayContext
# class UDialectHandling(ENUM):
#     ULDN_STANDARD_NAMES = 0
#     ULDN_DIALECT_NAMES = 1
#
#
#
# ULocaleDisplayNames = struct
#
#
#  =
#
#
# class UCurrencyUsage(ENUM):
#     UCURR_USAGE_STANDARD = 0
#     UCURR_USAGE_CASH = 1
#
#
#  = UCurrencyUsage
#
#
# UCurrencyUsage = UCurrencyUsage
# class UCurrNameStyle(ENUM):
#     UCURR_SYMBOL_NAME = 0
#     UCURR_LONG_NAME = 1
#
#
#
# UCurrRegistryKey = VOID*
# class UCurrCurrencyType(ENUM):
#     UCURR_ALL = INT32_MAX
#     UCURR_COMMON = 1
#     UCURR_UNCOMMON = 2
#     UCURR_DEPRECATED = 4
#     UCURR_NON_DEPRECATED = 8
#
#
#
# UConverter = struct
#
#
# UConverter = UConverter
#
#
# UCNV_SUB_STOP_ON_ILLEGAL = "i"
# UCNV_SKIP_STOP_ON_ILLEGAL = "i"
# UCNV_ESCAPE_ICU = NULL
# UCNV_ESCAPE_JAVA = "J"
# UCNV_ESCAPE_C = "C"
# UCNV_ESCAPE_XML_DEC = "D"
# UCNV_ESCAPE_XML_HEX = "X"
# UCNV_ESCAPE_UNICODE = "U"
# UCNV_ESCAPE_CSS2 = "S"
# class UConverterCallbackReason(ENUM):
#     UCNV_UNASSIGNED = 0  /**< The code poINT is unasINT.
#     The error code U_INVALID_CHAR_FOUND will be set. */ = 0
#     UCNV_ILLEGAL = 1     /**< The code poINT is illegal. For example
#     \\x81\\x2E is illegal in SJIS because \\x2E = 1
#     is not a valid trail byte for the \\x81 = 2
#     lead byte. = 3
#     Also starting with Unicode 3.0.1 non-SHORTest byte sequences = 4
#     in UTF-8 (like \\xC1\\xA1 instead of \\x61 for U+0061) = 5
#     are also illegal not just irregular. = 6
#     The error code U_ILLEGAL_CHAR_FOUND will be set. */ = 7
#     UCNV_IRREGULAR = 2   /**< The codepoINT is not a regular sequence in
#     the encoding. For example \\xED\\xA0\\x80..\\xED\\xBF\\xBF = 8
#     are irregular UTF-8 byte sequences for single surrogate = 9
#     code poINTs. = 10
#     The error code U_INVALID_CHAR_FOUND will be set. */ = 11
#     UCNV_RESET = 3       /**< The callback is called with this reason when a
#     'reset' has occured. Callback should reset all = 12
#     state. */ = 13
#     UCNV_CLOSE = 4        /**< Called when the converter is closed. The
#     callback should release any allocated memory.*/ = 14
#     UCNV_CLONE = 5         /**< Called when ucnv_safeClone() is called on the
#     converter. the poINTer available as the = 15
#     'context' is an alias to the original converters' = 16
#     context poINTer. If the context must be owned = 17
#     by the new converter the callback must clone = 18
#     the data and call ucnv_setFromUCallback = 19
#     (or setToUCallback) with the correct poINTer. = 20
#     @stable ICU 2.2 = 21
#     */ = 22
#
#
#
#
# class UConverterFromUnicodeArgs(ctypes.Structure):
#     _fields_ = [
#         ('size', uint16_t),
#         ('flush', UBool),
#         ('converter', POINTER(UConverter)),
#         ('source', POINTER(UChar)),
#         ('sourceLimit', POINTER(UChar)),
#         ('target', POINTER(CHAR)),
#         ('targetLimit', POINTER(CHAR)),
#         ('offsets', POINTER(int32_t)),
#     ]
#
#
#
#
# class UConverterToUnicodeArgs(ctypes.Structure):
#     _fields_ = [
#         ('size', uint16_t),
#         ('flush', UBool),
#         ('converter', POINTER(UConverter)),
#         ('source', POINTER(CHAR)),
#         ('sourceLimit', POINTER(CHAR)),
#         ('target', POINTER(UChar)),
#         ('targetLimit', POINTER(UChar)),
#         ('offsets', POINTER(int32_t)),
#     ]
#
#
#
# USet = struct
#
#
# USet = USet
#
#
# UCNV_MAX_CONVERTER_NAME_LENGTH = 0x0000003C
# UCNV_MAX_FULL_FILE_NAME_LENGTH = 600+UCNV_MAX_CONVERTER_NAME_LENGTH
# UCNV_SI = 0x0000000F
# UCNV_SO = 0x0000000E
# class UConverterType(ENUM):
#     UCNV_UNSUPPORTED_CONVERTER = - 1
#     UCNV_SBCS = 0
#     UCNV_DBCS = 1
#     UCNV_MBCS = 2
#     UCNV_LATIN_1 = 3
#     UCNV_UTF8 = 4
#     UCNV_UTF16_BigEndian = 5
#     UCNV_UTF16_LittleEndian = 6
#     UCNV_UTF32_BigEndian = 7
#     UCNV_UTF32_LittleEndian = 8
#     UCNV_EBCDIC_STATEFUL = 9
#     UCNV_ISO_2022 = 10
#     UCNV_LMBCS_1 = 11
#     UCNV_LMBCS_2 = 12
#     UCNV_LMBCS_3 = 13
#     UCNV_LMBCS_4 = 14
#     UCNV_LMBCS_5 = 15
#     UCNV_LMBCS_6 = 16
#     UCNV_LMBCS_8 = 17
#     UCNV_LMBCS_11 = 18
#     UCNV_LMBCS_16 = 19
#     UCNV_LMBCS_17 = 20
#     UCNV_LMBCS_18 = 21
#     UCNV_LMBCS_19 = 22
#     UCNV_LMBCS_LAST = UCNV_LMBCS_19
#     UCNV_HZ = 23
#     UCNV_SCSU = 24
#     UCNV_ISCII = 25
#     UCNV_US_ASCII = 26
#     UCNV_UTF7 = 27
#     UCNV_BOCU1 = 28
#     UCNV_UTF16 = 29
#     UCNV_UTF32 = 30
#     UCNV_CESU8 = 31
#     UCNV_IMAP_MAILBOX = 32
#     UCNV_COMPOUND_TEXT = 33
#     UCNV_NUMBER_OF_SUPPORTED_CONVERTER_TYPES = 34
#
#
#
# class UConverterPlatform(ENUM):
#     UCNV_UNKNOWN = - 1
#     UCNV_IBM = 0
#
#
#
# UCNV_OPTION_SEP_CHAR = ','
# UCNV_OPTION_SEP_STRING = ","
# UCNV_VALUE_SEP_CHAR = '='
# UCNV_VALUE_SEP_STRING = "="
# UCNV_LOCALE_OPTION_STRING = ",locale="
# UCNV_VERSION_OPTION_STRING = ",version="
# UCNV_SWAP_LFNL_OPTION_STRING = ",swaplfnl"
#
#
# def UCNV_GET_MAX_BYTES_FOR_STRING(length, maxCharSize):
#     return (int32_tlength+10)*int32_tmaxCharSize
# class UConverterUnicodeSet(ENUM):
#     UCNV_ROUNDTRIP_SET = 0
#     UCNV_ROUNDTRIP_AND_FALLBACK_SET = 1
#
#
#
# context = POINTER(VOID)
# size_t size) = VOID
# context = POINTER(VOID)
# VOID mem = VOID
# size_t size) = VOID
# context = POINTER(VOID)
# VOID mem) = VOID
# U_UNICODE_VERSION = "9.0"
# UCHAR_MIN_VALUE = 0x00000000
# UCHAR_MAX_VALUE = 0x0010FFFF
#
#
# def U_MASK(x):
#     return uint32_t1<<x
# class UProperty(ENUM):
#     UCHAR_ALPHABETIC = 0
#     UCHAR_BINARY_START = UCHAR_ALPHABETIC
#     UCHAR_ASCII_HEX_DIGIT = 1
#     UCHAR_BIDI_CONTROL = 2
#     UCHAR_BIDI_MIRRORED = 3
#     UCHAR_DASH = 4
#     UCHAR_DEFAULT_IGNORABLE_CODE_POINT = 5
#     UCHAR_DEPRECATED = 6
#     UCHAR_DIACRITIC = 7
#     UCHAR_EXTENDER = 8
#     UCHAR_FULL_COMPOSITION_EXCLUSION = 9
#     UCHAR_GRAPHEME_BASE = 10
#     UCHAR_GRAPHEME_EXTEND = 11
#     UCHAR_GRAPHEME_LINK = 12
#     UCHAR_HEX_DIGIT = 13
#     UCHAR_HYPHEN = 14
#     UCHAR_ID_CONTINUE = 15
#     UCHAR_ID_START = 16
#     UCHAR_IDEOGRAPHIC = 17
#     UCHAR_IDS_BINARY_OPERATOR = 18
#     UCHAR_IDS_TRINARY_OPERATOR = 19
#     UCHAR_JOIN_CONTROL = 20
#     UCHAR_LOGICAL_ORDER_EXCEPTION = 21
#     UCHAR_LOWERCASE = 22
#     UCHAR_MATH = 23
#     UCHAR_NONCHARACTER_CODE_POINT = 24
#     UCHAR_QUOTATION_MARK = 25
#     UCHAR_RADICAL = 26
#     UCHAR_SOFT_DOTTED = 27
#     UCHAR_TERMINAL_PUNCTUATION = 28
#     UCHAR_UNIFIED_IDEOGRAPH = 29
#     UCHAR_UPPERCASE = 30
#     UCHAR_WHITE_SPACE = 31
#     UCHAR_XID_CONTINUE = 32
#     UCHAR_XID_START = 33
#     UCHAR_CASE_SENSITIVE = 34
#     UCHAR_S_TERM = 35
#     UCHAR_VARIATION_SELECTOR = 36
#     UCHAR_NFD_INERT = 37
#     UCHAR_NFKD_INERT = 38
#     UCHAR_NFC_INERT = 39
#     UCHAR_NFKC_INERT = 40
#     UCHAR_SEGMENT_STARTER = 41
#     UCHAR_PATTERN_SYNTAX = 42
#     UCHAR_PATTERN_WHITE_SPACE = 43
#     UCHAR_POSIX_ALNUM = 44
#     UCHAR_POSIX_BLANK = 45
#     UCHAR_POSIX_GRAPH = 46
#     UCHAR_POSIX_PRINT = 47
#     UCHAR_POSIX_XDIGIT = 48
#     UCHAR_CASED = 49
#     UCHAR_CASE_IGNORABLE = 50
#     UCHAR_CHANGES_WHEN_LOWERCASED = 51
#     UCHAR_CHANGES_WHEN_UPPERCASED = 52
#     UCHAR_CHANGES_WHEN_TITLECASED = 53
#     UCHAR_CHANGES_WHEN_CASEFOLDED = 54
#     UCHAR_CHANGES_WHEN_CASEMAPPED = 55
#     UCHAR_CHANGES_WHEN_NFKC_CASEFOLDED = 56
#     UCHAR_EMOJI = 57
#     UCHAR_EMOJI_PRESENTATION = 58
#     UCHAR_EMOJI_MODIFIER = 59
#     UCHAR_EMOJI_MODIFIER_BASE = 60
#     UCHAR_BIDI_CLASS = 0x1000
#     UCHAR_INT_START = UCHAR_BIDI_CLASS
#     UCHAR_BLOCK = 0x1001
#     UCHAR_CANONICAL_COMBINING_CLASS = 0x1002
#     UCHAR_DECOMPOSITION_TYPE = 0x1003
#     UCHAR_EAST_ASIAN_WIDTH = 0x1004
#     UCHAR_GENERAL_CATEGORY = 0x1005
#     UCHAR_JOINING_GROUP = 0x1006
#     UCHAR_JOINING_TYPE = 0x1007
#     UCHAR_LINE_BREAK = 0x1008
#     UCHAR_NUMERIC_TYPE = 0x1009
#     UCHAR_SCRIPT = 0x100A
#     UCHAR_HANGUL_SYLLABLE_TYPE = 0x100B
#     UCHAR_NFD_QUICK_CHECK = 0x100C
#     UCHAR_NFKD_QUICK_CHECK = 0x100D
#     UCHAR_NFC_QUICK_CHECK = 0x100E
#     UCHAR_NFKC_QUICK_CHECK = 0x100F
#     UCHAR_LEAD_CANONICAL_COMBINING_CLASS = 0x1010
#     UCHAR_TRAIL_CANONICAL_COMBINING_CLASS = 0x1011
#     UCHAR_GRAPHEME_CLUSTER_BREAK = 0x1012
#     UCHAR_SENTENCE_BREAK = 0x1013
#     UCHAR_WORD_BREAK = 0x1014
#     UCHAR_BIDI_PAIRED_BRACKET_TYPE = 0x1015
#     UCHAR_GENERAL_CATEGORY_MASK = 0x2000
#     UCHAR_MASK_START = UCHAR_GENERAL_CATEGORY_MASK
#     UCHAR_NUMERIC_VALUE = 0x3000
#     UCHAR_DOUBLE_START = UCHAR_NUMERIC_VALUE
#     UCHAR_AGE = 0x4000
#     UCHAR_STRING_START = UCHAR_AGE
#     UCHAR_BIDI_MIRRORING_GLYPH = 0x4001
#     UCHAR_CASE_FOLDING = 0x4002
#     UCHAR_LOWERCASE_MAPPING = 0x4004
#     UCHAR_NAME = 0x4005
#     UCHAR_SIMPLE_CASE_FOLDING = 0x4006
#     UCHAR_SIMPLE_LOWERCASE_MAPPING = 0x4007
#     UCHAR_SIMPLE_TITLECASE_MAPPING = 0x4008
#     UCHAR_SIMPLE_UPPERCASE_MAPPING = 0x4009
#     UCHAR_TITLECASE_MAPPING = 0x400A
#     UCHAR_UPPERCASE_MAPPING = 0x400C
#     UCHAR_BIDI_PAIRED_BRACKET = 0x400D
#     UCHAR_SCRIPT_EXTENSIONS = 0x7000
#     UCHAR_OTHER_PROPERTY_START = UCHAR_SCRIPT_EXTENSIONS
#     UCHAR_INVALID_CODE = - 1
#
#
#
# class UCharCategory(ENUM):
#     U_UNASSIGNED = 0
#     U_GENERAL_OTHER_TYPES = 0
#     U_UPPERCASE_LETTER = 1
#     U_LOWERCASE_LETTER = 2
#     U_TITLECASE_LETTER = 3
#     U_MODIFIER_LETTER = 4
#     U_OTHER_LETTER = 5
#     U_NON_SPACING_MARK = 6
#     U_ENCLOSING_MARK = 7
#     U_COMBINING_SPACING_MARK = 8
#     U_DECIMAL_DIGIT_NUMBER = 9
#     U_LETTER_NUMBER = 10
#     U_OTHER_NUMBER = 11
#     U_SPACE_SEPARATOR = 12
#     U_LINE_SEPARATOR = 13
#     U_PARAGRAPH_SEPARATOR = 14
#     U_CONTROL_CHAR = 15
#     U_FORMAT_CHAR = 16
#     U_PRIVATE_USE_CHAR = 17
#     U_SURROGATE = 18
#     U_DASH_PUNCTUATION = 19
#     U_START_PUNCTUATION = 20
#     U_END_PUNCTUATION = 21
#     U_CONNECTOR_PUNCTUATION = 22
#     U_OTHER_PUNCTUATION = 23
#     U_MATH_SYMBOL = 24
#     U_CURRENCY_SYMBOL = 25
#     U_MODIFIER_SYMBOL = 26
#     U_OTHER_SYMBOL = 27
#     U_INITIAL_PUNCTUATION = 28
#     U_FINAL_PUNCTUATION = 29
#     U_CHAR_CATEGORY_COUNT = 30
#
#
#
# U_GC_CN_MASK = U_MASK(U_GENERAL_OTHER_TYPES)
# U_GC_LU_MASK = U_MASK(U_UPPERCASE_LETTER)
# U_GC_LL_MASK = U_MASK(U_LOWERCASE_LETTER)
# U_GC_LT_MASK = U_MASK(U_TITLECASE_LETTER)
# U_GC_LM_MASK = U_MASK(U_MODIFIER_LETTER)
# U_GC_LO_MASK = U_MASK(U_OTHER_LETTER)
# U_GC_MN_MASK = U_MASK(U_NON_SPACING_MARK)
# U_GC_ME_MASK = U_MASK(U_ENCLOSING_MARK)
# U_GC_MC_MASK = U_MASK(U_COMBINING_SPACING_MARK)
# U_GC_ND_MASK = U_MASK(U_DECIMAL_DIGIT_NUMBER)
# U_GC_NL_MASK = U_MASK(U_LETTER_NUMBER)
# U_GC_NO_MASK = U_MASK(U_OTHER_NUMBER)
# U_GC_ZS_MASK = U_MASK(U_SPACE_SEPARATOR)
# U_GC_ZL_MASK = U_MASK(U_LINE_SEPARATOR)
# U_GC_ZP_MASK = U_MASK(U_PARAGRAPH_SEPARATOR)
# U_GC_CC_MASK = U_MASK(U_CONTROL_CHAR)
# U_GC_CF_MASK = U_MASK(U_FORMAT_CHAR)
# U_GC_CO_MASK = U_MASK(U_PRIVATE_USE_CHAR)
# U_GC_CS_MASK = U_MASK(U_SURROGATE)
# U_GC_PD_MASK = U_MASK(U_DASH_PUNCTUATION)
# U_GC_PS_MASK = U_MASK(U_START_PUNCTUATION)
# U_GC_PE_MASK = U_MASK(U_END_PUNCTUATION)
# U_GC_PC_MASK = U_MASK(U_CONNECTOR_PUNCTUATION)
# U_GC_PO_MASK = U_MASK(U_OTHER_PUNCTUATION)
# U_GC_SM_MASK = U_MASK(U_MATH_SYMBOL)
# U_GC_SC_MASK = U_MASK(U_CURRENCY_SYMBOL)
# U_GC_SK_MASK = U_MASK(U_MODIFIER_SYMBOL)
# U_GC_SO_MASK = U_MASK(U_OTHER_SYMBOL)
# U_GC_PI_MASK = U_MASK(U_INITIAL_PUNCTUATION)
# U_GC_PF_MASK = U_MASK(U_FINAL_PUNCTUATION)
# U_GC_L_MASK = (
#     U_GC_LU_MASK  |
#      U_GC_LL_MASK  |
#      U_GC_LT_MASK  |
#      U_GC_LM_MASK  |
#      U_GC_LO_MASK
# )
# U_GC_LC_MASK = U_GC_LU_MASK | U_GC_LL_MASK | U_GC_LT_MASK
# U_GC_M_MASK = U_GC_MN_MASK | U_GC_ME_MASK | U_GC_MC_MASK
# U_GC_N_MASK = U_GC_ND_MASK | U_GC_NL_MASK | U_GC_NO_MASK
# U_GC_Z_MASK = U_GC_ZS_MASK | U_GC_ZL_MASK | U_GC_ZP_MASK
# U_GC_C_MASK = (
#     U_GC_CN_MASK  |
#      U_GC_CC_MASK  |
#      U_GC_CF_MASK  |
#      U_GC_CO_MASK  |
#      U_GC_CS_MASK
# )
# U_GC_P_MASK = (
#     U_GC_PD_MASK  |
#      U_GC_PS_MASK  |
#      U_GC_PE_MASK  |
#      U_GC_PC_MASK  |
#      U_GC_PO_MASK  |
#      U_GC_PI_MASK  |
#      U_GC_PF_MASK
# )
# U_GC_S_MASK = U_GC_SM_MASK | U_GC_SC_MASK | U_GC_SK_MASK | U_GC_SO_MASK
# class UCharDirection(ENUM):
#     U_LEFT_TO_RIGHT = 0
#     U_RIGHT_TO_LEFT = 1
#     U_EUROPEAN_NUMBER = 2
#     U_EUROPEAN_NUMBER_SEPARATOR = 3
#     U_EUROPEAN_NUMBER_TERMINATOR = 4
#     U_ARABIC_NUMBER = 5
#     U_COMMON_NUMBER_SEPARATOR = 6
#     U_BLOCK_SEPARATOR = 7
#     U_SEGMENT_SEPARATOR = 8
#     U_WHITE_SPACE_NEUTRAL = 9
#     U_OTHER_NEUTRAL = 10
#     U_LEFT_TO_RIGHT_EMBEDDING = 11
#     U_LEFT_TO_RIGHT_OVERRIDE = 12
#     U_RIGHT_TO_LEFT_ARABIC = 13
#     U_RIGHT_TO_LEFT_EMBEDDING = 14
#     U_RIGHT_TO_LEFT_OVERRIDE = 15
#     U_POP_DIRECTIONAL_FORMAT = 16
#     U_DIR_NON_SPACING_MARK = 17
#     U_BOUNDARY_NEUTRAL = 18
#     U_FIRST_STRONG_ISOLATE = 19
#     U_LEFT_TO_RIGHT_ISOLATE = 20
#     U_RIGHT_TO_LEFT_ISOLATE = 21
#     U_POP_DIRECTIONAL_ISOLATE = 22
#
#
#
# class UBidiPairedBracketType(ENUM):
#     U_BPT_NONE = 0
#     U_BPT_OPEN = 1
#     U_BPT_CLOSE = 2
#
#
#
# class UBlockCode(ENUM):
#     UBLOCK_NO_BLOCK = 0  /* Special range indicating No_Block */
#     UBLOCK_BASIC_LATIN = 1
#     UBLOCK_LATIN_1_SUPPLEMENT = 2
#     UBLOCK_LATIN_EXTENDED_A = 3
#     UBLOCK_LATIN_EXTENDED_B = 4
#     UBLOCK_IPA_EXTENSIONS = 5
#     UBLOCK_SPACING_MODIFIER_LETTERS = 6
#     UBLOCK_COMBINING_DIACRITICAL_MARKS = 7
#     UBLOCK_GREEK = 8
#     UBLOCK_CYRILLIC = 9
#     UBLOCK_ARMENIAN = 10
#     UBLOCK_HEBREW = 11
#     UBLOCK_ARABIC = 12
#     UBLOCK_SYRIAC = 13
#     UBLOCK_THAANA = 14
#     UBLOCK_DEVANAGARI = 15
#     UBLOCK_BENGALI = 16
#     UBLOCK_GURMUKHI = 17
#     UBLOCK_GUJARATI = 18
#     UBLOCK_ORIYA = 19
#     UBLOCK_TAMIL = 20
#     UBLOCK_TELUGU = 21
#     UBLOCK_KANNADA = 22
#     UBLOCK_MALAYALAM = 23
#     UBLOCK_SINHALA = 24
#     UBLOCK_THAI = 25
#     UBLOCK_LAO = 26
#     UBLOCK_TIBETAN = 27
#     UBLOCK_MYANMAR = 28
#     UBLOCK_GEORGIAN = 29
#     UBLOCK_HANGUL_JAMO = 30
#     UBLOCK_ETHIOPIC = 31
#     UBLOCK_CHEROKEE = 32
#     UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS = 33
#     UBLOCK_OGHAM = 34
#     UBLOCK_RUNIC = 35
#     UBLOCK_KHMER = 36
#     UBLOCK_MONGOLIAN = 37
#     UBLOCK_LATIN_EXTENDED_ADDITIONAL = 38
#     UBLOCK_GREEK_EXTENDED = 39
#     UBLOCK_GENERAL_PUNCTUATION = 40
#     UBLOCK_SUPERSCRIPTS_AND_SUBSCRIPTS = 41
#     UBLOCK_CURRENCY_SYMBOLS = 42
#     UBLOCK_COMBINING_MARKS_FOR_SYMBOLS = 43
#     UBLOCK_LETTERLIKE_SYMBOLS = 44
#     UBLOCK_NUMBER_FORMS = 45
#     UBLOCK_ARROWS = 46
#     UBLOCK_MATHEMATICAL_OPERATORS = 47
#     UBLOCK_MISCELLANEOUS_TECHNICAL = 48
#     UBLOCK_CONTROL_PICTURES = 49
#     UBLOCK_OPTICAL_CHARACTER_RECOGNITION = 50
#     UBLOCK_ENCLOSED_ALPHANUMERICS = 51
#     UBLOCK_BOX_DRAWING = 52
#     UBLOCK_BLOCK_ELEMENTS = 53
#     UBLOCK_GEOMETRIC_SHAPES = 54
#     UBLOCK_MISCELLANEOUS_SYMBOLS = 55
#     UBLOCK_DINGBATS = 56
#     UBLOCK_BRAILLE_PATTERNS = 57
#     UBLOCK_CJK_RADICALS_SUPPLEMENT = 58
#     UBLOCK_KANGXI_RADICALS = 59
#     UBLOCK_IDEOGRAPHIC_DESCRIPTION_CHARACTERS = 60
#     UBLOCK_CJK_SYMBOLS_AND_PUNCTUATION = 61
#     UBLOCK_HIRAGANA = 62
#     UBLOCK_KATAKANA = 63
#     UBLOCK_BOPOMOFO = 64
#     UBLOCK_HANGUL_COMPATIBILITY_JAMO = 65
#     UBLOCK_KANBUN = 66
#     UBLOCK_BOPOMOFO_EXTENDED = 67
#     UBLOCK_ENCLOSED_CJK_LETTERS_AND_MONTHS = 68
#     UBLOCK_CJK_COMPATIBILITY = 69
#     UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A = 70
#     UBLOCK_CJK_UNIFIED_IDEOGRAPHS = 71
#     UBLOCK_YI_SYLLABLES = 72
#     UBLOCK_YI_RADICALS = 73
#     UBLOCK_HANGUL_SYLLABLES = 74
#     UBLOCK_HIGH_SURROGATES = 75
#     UBLOCK_HIGH_PRIVATE_USE_SURROGATES = 76
#     UBLOCK_LOW_SURROGATES = 77
#     UBLOCK_PRIVATE_USE_AREA = 78
#     UBLOCK_PRIVATE_USE = UBLOCK_PRIVATE_USE_AREA
#     UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS = 79
#     UBLOCK_ALPHABETIC_PRESENTATION_FORMS = 80
#     UBLOCK_ARABIC_PRESENTATION_FORMS_A = 81
#     UBLOCK_COMBINING_HALF_MARKS = 82
#     UBLOCK_CJK_COMPATIBILITY_FORMS = 83
#     UBLOCK_SMALL_FORM_VARIANTS = 84
#     UBLOCK_ARABIC_PRESENTATION_FORMS_B = 85
#     UBLOCK_SPECIALS = 86
#     UBLOCK_HALFWIDTH_AND_FULLWIDTH_FORMS = 87
#     UBLOCK_OLD_ITALIC = 88
#     UBLOCK_GOTHIC = 89
#     UBLOCK_DESERET = 90
#     UBLOCK_BYZANTINE_MUSICAL_SYMBOLS = 91
#     UBLOCK_MUSICAL_SYMBOLS = 92
#     UBLOCK_MATHEMATICAL_ALPHANUMERIC_SYMBOLS = 93
#     UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B = 94
#     UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT = 95
#     UBLOCK_TAGS = 96
#     UBLOCK_CYRILLIC_SUPPLEMENT = 97
#     UBLOCK_CYRILLIC_SUPPLEMENTARY = UBLOCK_CYRILLIC_SUPPLEMENT
#     UBLOCK_TAGALOG = 98
#     UBLOCK_HANUNOO = 99
#     UBLOCK_BUHID = 100
#     UBLOCK_TAGBANWA = 101
#     UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A = 102
#     UBLOCK_SUPPLEMENTAL_ARROWS_A = 103
#     UBLOCK_SUPPLEMENTAL_ARROWS_B = 104
#     UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B = 105
#     UBLOCK_SUPPLEMENTAL_MATHEMATICAL_OPERATORS = 106
#     UBLOCK_KATAKANA_PHONETIC_EXTENSIONS = 107
#     UBLOCK_VARIATION_SELECTORS = 108
#     UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_A = 109
#     UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_B = 110
#     UBLOCK_LIMBU = 111
#     UBLOCK_TAI_LE = 112
#     UBLOCK_KHMER_SYMBOLS = 113
#     UBLOCK_PHONETIC_EXTENSIONS = 114
#     UBLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS = 115
#     UBLOCK_YIJING_HEXAGRAM_SYMBOLS = 116
#     UBLOCK_LINEAR_B_SYLLABARY = 117
#     UBLOCK_LINEAR_B_IDEOGRAMS = 118
#     UBLOCK_AEGEAN_NUMBERS = 119
#     UBLOCK_UGARITIC = 120
#     UBLOCK_SHAVIAN = 121
#     UBLOCK_OSMANYA = 122
#     UBLOCK_CYPRIOT_SYLLABARY = 123
#     UBLOCK_TAI_XUAN_JING_SYMBOLS = 124
#     UBLOCK_VARIATION_SELECTORS_SUPPLEMENT = 125
#     UBLOCK_ANCIENT_GREEK_MUSICAL_NOTATION = 126
#     UBLOCK_ANCIENT_GREEK_NUMBERS = 127
#     UBLOCK_ARABIC_SUPPLEMENT = 128
#     UBLOCK_BUGINESE = 129
#     UBLOCK_CJK_STROKES = 130
#     UBLOCK_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT = 131
#     UBLOCK_COPTIC = 132
#     UBLOCK_ETHIOPIC_EXTENDED = 133
#     UBLOCK_ETHIOPIC_SUPPLEMENT = 134
#     UBLOCK_GEORGIAN_SUPPLEMENT = 135
#     UBLOCK_GLAGOLITIC = 136
#     UBLOCK_KHAROSHTHI = 137
#     UBLOCK_MODIFIER_TONE_LETTERS = 138
#     UBLOCK_NEW_TAI_LUE = 139
#     UBLOCK_OLD_PERSIAN = 140
#     UBLOCK_PHONETIC_EXTENSIONS_SUPPLEMENT = 141
#     UBLOCK_SUPPLEMENTAL_PUNCTUATION = 142
#     UBLOCK_SYLOTI_NAGRI = 143
#     UBLOCK_TIFINAGH = 144
#     UBLOCK_VERTICAL_FORMS = 145
#     UBLOCK_NKO = 146
#     UBLOCK_BALINESE = 147
#     UBLOCK_LATIN_EXTENDED_C = 148
#     UBLOCK_LATIN_EXTENDED_D = 149
#     UBLOCK_PHAGS_PA = 150
#     UBLOCK_PHOENICIAN = 151
#     UBLOCK_CUNEIFORM = 152
#     UBLOCK_CUNEIFORM_NUMBERS_AND_PUNCTUATION = 153
#     UBLOCK_COUNTING_ROD_NUMERALS = 154
#     UBLOCK_SUNDANESE = 155
#     UBLOCK_LEPCHA = 156
#     UBLOCK_OL_CHIKI = 157
#     UBLOCK_CYRILLIC_EXTENDED_A = 158
#     UBLOCK_VAI = 159
#     UBLOCK_CYRILLIC_EXTENDED_B = 160
#     UBLOCK_SAURASHTRA = 161
#     UBLOCK_KAYAH_LI = 162
#     UBLOCK_REJANG = 163
#     UBLOCK_CHAM = 164
#     UBLOCK_ANCIENT_SYMBOLS = 165
#     UBLOCK_PHAISTOS_DISC = 166
#     UBLOCK_LYCIAN = 167
#     UBLOCK_CARIAN = 168
#     UBLOCK_LYDIAN = 169
#     UBLOCK_MAHJONG_TILES = 170
#     UBLOCK_DOMINO_TILES = 171
#     UBLOCK_SAMARITAN = 172
#     UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED = 173
#     UBLOCK_TAI_THAM = 174
#     UBLOCK_VEDIC_EXTENSIONS = 175
#     UBLOCK_LISU = 176
#     UBLOCK_BAMUM = 177
#     UBLOCK_COMMON_INDIC_NUMBER_FORMS = 178
#     UBLOCK_DEVANAGARI_EXTENDED = 179
#     UBLOCK_HANGUL_JAMO_EXTENDED_A = 180
#     UBLOCK_JAVANESE = 181
#     UBLOCK_MYANMAR_EXTENDED_A = 182
#     UBLOCK_TAI_VIET = 183
#     UBLOCK_MEETEI_MAYEK = 184
#     UBLOCK_HANGUL_JAMO_EXTENDED_B = 185
#     UBLOCK_IMPERIAL_ARAMAIC = 186
#     UBLOCK_OLD_SOUTH_ARABIAN = 187
#     UBLOCK_AVESTAN = 188
#     UBLOCK_INSCRIPTIONAL_PARTHIAN = 189
#     UBLOCK_INSCRIPTIONAL_PAHLAVI = 190
#     UBLOCK_OLD_TURKIC = 191
#     UBLOCK_RUMI_NUMERAL_SYMBOLS = 192
#     UBLOCK_KAITHI = 193
#     UBLOCK_EGYPTIAN_HIEROGLYPHS = 194
#     UBLOCK_ENCLOSED_ALPHANUMERIC_SUPPLEMENT = 195
#     UBLOCK_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT = 196
#     UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C = 197
#     UBLOCK_MANDAIC = 198
#     UBLOCK_BATAK = 199
#     UBLOCK_ETHIOPIC_EXTENDED_A = 200
#     UBLOCK_BRAHMI = 201
#     UBLOCK_BAMUM_SUPPLEMENT = 202
#     UBLOCK_KANA_SUPPLEMENT = 203
#     UBLOCK_PLAYING_CARDS = 204
#     UBLOCK_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS = 205
#     UBLOCK_EMOTICONS = 206
#     UBLOCK_TRANSPORT_AND_MAP_SYMBOLS = 207
#     UBLOCK_ALCHEMICAL_SYMBOLS = 208
#     UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D = 209
#     UBLOCK_ARABIC_EXTENDED_A = 210
#     UBLOCK_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS = 211
#     UBLOCK_CHAKMA = 212
#     UBLOCK_MEETEI_MAYEK_EXTENSIONS = 213
#     UBLOCK_MEROITIC_CURSIVE = 214
#     UBLOCK_MEROITIC_HIEROGLYPHS = 215
#     UBLOCK_MIAO = 216
#     UBLOCK_SHARADA = 217
#     UBLOCK_SORA_SOMPENG = 218
#     UBLOCK_SUNDANESE_SUPPLEMENT = 219
#     UBLOCK_TAKRI = 220
#     UBLOCK_BASSA_VAH = 221
#     UBLOCK_CAUCASIAN_ALBANIAN = 222
#     UBLOCK_COPTIC_EPACT_NUMBERS = 223
#     UBLOCK_COMBINING_DIACRITICAL_MARKS_EXTENDED = 224
#     UBLOCK_DUPLOYAN = 225
#     UBLOCK_ELBASAN = 226
#     UBLOCK_GEOMETRIC_SHAPES_EXTENDED = 227
#     UBLOCK_GRANTHA = 228
#     UBLOCK_KHOJKI = 229
#     UBLOCK_KHUDAWADI = 230
#     UBLOCK_LATIN_EXTENDED_E = 231
#     UBLOCK_LINEAR_A = 232
#     UBLOCK_MAHAJANI = 233
#     UBLOCK_MANICHAEAN = 234
#     UBLOCK_MENDE_KIKAKUI = 235
#     UBLOCK_MODI = 236
#     UBLOCK_MRO = 237
#     UBLOCK_MYANMAR_EXTENDED_B = 238
#     UBLOCK_NABATAEAN = 239
#     UBLOCK_OLD_NORTH_ARABIAN = 240
#     UBLOCK_OLD_PERMIC = 241
#     UBLOCK_ORNAMENTAL_DINGBATS = 242
#     UBLOCK_PAHAWH_HMONG = 243
#     UBLOCK_PALMYRENE = 244
#     UBLOCK_PAU_CIN_HAU = 245
#     UBLOCK_PSALTER_PAHLAVI = 246
#     UBLOCK_SHORTHAND_FORMAT_CONTROLS = 247
#     UBLOCK_SIDDHAM = 248
#     UBLOCK_SINHALA_ARCHAIC_NUMBERS = 249
#     UBLOCK_SUPPLEMENTAL_ARROWS_C = 250
#     UBLOCK_TIRHUTA = 251
#     UBLOCK_WARANG_CITI = 252
#     UBLOCK_AHOM = 253
#     UBLOCK_ANATOLIAN_HIEROGLYPHS = 254
#     UBLOCK_CHEROKEE_SUPPLEMENT = 255
#     UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E = 256
#     UBLOCK_EARLY_DYNASTIC_CUNEIFORM = 257
#     UBLOCK_HATRAN = 258
#     UBLOCK_MULTANI = 259
#     UBLOCK_OLD_HUNGARIAN = 260
#     UBLOCK_SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS = 261
#     UBLOCK_SUTTON_SIGNWRITING = 262
#     UBLOCK_ADLAM = 263
#     UBLOCK_BHAIKSUKI = 264
#     UBLOCK_CYRILLIC_EXTENDED_C = 265
#     UBLOCK_GLAGOLITIC_SUPPLEMENT = 266
#     UBLOCK_IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION = 267
#     UBLOCK_MARCHEN = 268
#     UBLOCK_MONGOLIAN_SUPPLEMENT = 269
#     UBLOCK_NEWA = 270
#     UBLOCK_OSAGE = 271
#     UBLOCK_TANGUT = 272
#     UBLOCK_TANGUT_COMPONENTS = 273
#     UBLOCK_INVALID_CODE = - 1
#
#
#  = UBlockCode
#
#
# UBlockCode = UBlockCode
# class UEastAsianWidth(ENUM):
#     U_EA_NEUTRAL = 0
#     U_EA_AMBIGUOUS = 1
#     U_EA_HALFWIDTH = 2
#     U_EA_FULLWIDTH = 3
#     U_EA_NARROW = 4
#     U_EA_WIDE = 5
#
#
#
# class UCharNameChoice(ENUM):
#     U_UNICODE_CHAR_NAME = 0
#     U_EXTENDED_CHAR_NAME = U_UNICODE_CHAR_NAME + 2
#     U_CHAR_NAME_ALIAS = 1
#
#
#
# class UPropertyNameChoice(ENUM):
#     U_SHORT_PROPERTY_NAME = 0
#     U_LONG_PROPERTY_NAME = 1
#
#
#
# class UDecompositionType(ENUM):
#     U_DT_NONE = 0
#     U_DT_CANONICAL = 1
#     U_DT_COMPAT = 2
#     U_DT_CIRCLE = 3
#     U_DT_FINAL = 4
#     U_DT_FONT = 5
#     U_DT_FRACTION = 6
#     U_DT_INITIAL = 7
#     U_DT_ISOLATED = 8
#     U_DT_MEDIAL = 9
#     U_DT_NARROW = 10
#     U_DT_NOBREAK = 11
#     U_DT_SMALL = 12
#     U_DT_SQUARE = 13
#     U_DT_SUB = 14
#     U_DT_SUPER = 15
#     U_DT_VERTICAL = 16
#     U_DT_WIDE = 17
#
#
#
# class UJoiningType(ENUM):
#     U_JT_NON_JOINING = 0
#     U_JT_JOIN_CAUSING = 1
#     U_JT_DUAL_JOINING = 2
#     U_JT_LEFT_JOINING = 3
#     U_JT_RIGHT_JOINING = 4
#     U_JT_TRANSPARENT = 5
#
#
#
# class UJoiningGroup(ENUM):
#     U_JG_NO_JOINING_GROUP = 0
#     U_JG_AIN = 1
#     U_JG_ALAPH = 2
#     U_JG_ALEF = 3
#     U_JG_BEH = 4
#     U_JG_BETH = 5
#     U_JG_DAL = 6
#     U_JG_DALATH_RISH = 7
#     U_JG_E = 8
#     U_JG_FEH = 9
#     U_JG_FINAL_SEMKATH = 10
#     U_JG_GAF = 11
#     U_JG_GAMAL = 12
#     U_JG_HAH = 13
#     U_JG_TEH_MARBUTA_GOAL = 14
#     U_JG_HAMZA_ON_HEH_GOAL = U_JG_TEH_MARBUTA_GOAL
#     U_JG_HE = 15
#     U_JG_HEH = 16
#     U_JG_HEH_GOAL = 17
#     U_JG_HETH = 18
#     U_JG_KAF = 19
#     U_JG_KAPH = 20
#     U_JG_KNOTTED_HEH = 21
#     U_JG_LAM = 22
#     U_JG_LAMADH = 23
#     U_JG_MEEM = 24
#     U_JG_MIM = 25
#     U_JG_NOON = 26
#     U_JG_NUN = 27
#     U_JG_PE = 28
#     U_JG_QAF = 29
#     U_JG_QAPH = 30
#     U_JG_REH = 31
#     U_JG_REVERSED_PE = 32
#     U_JG_SAD = 33
#     U_JG_SADHE = 34
#     U_JG_SEEN = 35
#     U_JG_SEMKATH = 36
#     U_JG_SHIN = 37
#     U_JG_SWASH_KAF = 38
#     U_JG_SYRIAC_WAW = 39
#     U_JG_TAH = 40
#     U_JG_TAW = 41
#     U_JG_TEH_MARBUTA = 42
#     U_JG_TETH = 43
#     U_JG_WAW = 44
#     U_JG_YEH = 45
#     U_JG_YEH_BARREE = 46
#     U_JG_YEH_WITH_TAIL = 47
#     U_JG_YUDH = 48
#     U_JG_YUDH_HE = 49
#     U_JG_ZAIN = 50
#     U_JG_FE = 51
#     U_JG_KHAPH = 52
#     U_JG_ZHAIN = 53
#     U_JG_BURUSHASKI_YEH_BARREE = 54
#     U_JG_FARSI_YEH = 55
#     U_JG_NYA = 56
#     U_JG_ROHINGYA_YEH = 57
#     U_JG_MANICHAEAN_ALEPH = 58
#     U_JG_MANICHAEAN_AYIN = 59
#     U_JG_MANICHAEAN_BETH = 60
#     U_JG_MANICHAEAN_DALETH = 61
#     U_JG_MANICHAEAN_DHAMEDH = 62
#     U_JG_MANICHAEAN_FIVE = 63
#     U_JG_MANICHAEAN_GIMEL = 64
#     U_JG_MANICHAEAN_HETH = 65
#     U_JG_MANICHAEAN_HUNDRED = 66
#     U_JG_MANICHAEAN_KAPH = 67
#     U_JG_MANICHAEAN_LAMEDH = 68
#     U_JG_MANICHAEAN_MEM = 69
#     U_JG_MANICHAEAN_NUN = 70
#     U_JG_MANICHAEAN_ONE = 71
#     U_JG_MANICHAEAN_PE = 72
#     U_JG_MANICHAEAN_QOPH = 73
#     U_JG_MANICHAEAN_RESH = 74
#     U_JG_MANICHAEAN_SADHE = 75
#     U_JG_MANICHAEAN_SAMEKH = 76
#     U_JG_MANICHAEAN_TAW = 77
#     U_JG_MANICHAEAN_TEN = 78
#     U_JG_MANICHAEAN_TETH = 79
#     U_JG_MANICHAEAN_THAMEDH = 80
#     U_JG_MANICHAEAN_TWENTY = 81
#     U_JG_MANICHAEAN_WAW = 82
#     U_JG_MANICHAEAN_YODH = 83
#     U_JG_MANICHAEAN_ZAYIN = 84
#     U_JG_STRAIGHT_WAW = 85
#     U_JG_AFRICAN_FEH = 86
#     U_JG_AFRICAN_NOON = 87
#     U_JG_AFRICAN_QAF = 88
#
#
#
# class UGraphemeClusterBreak(ENUM):
#     U_GCB_OTHER = 0
#     U_GCB_CONTROL = 1
#     U_GCB_CR = 2
#     U_GCB_EXTEND = 3
#     U_GCB_L = 4
#     U_GCB_LF = 5
#     U_GCB_LV = 6
#     U_GCB_LVT = 7
#     U_GCB_T = 8
#     U_GCB_V = 9
#     U_GCB_SPACING_MARK = 10     /* from here on: new in Unicode 5.1/ICU 4.0 */
#     U_GCB_PREPEND = 11
#     U_GCB_REGIONAL_INDICATOR = 12   /* new in Unicode 6.2/ICU 50 */
#     U_GCB_E_BASE = 13           /* from here on: new in Unicode 9.0/ICU 58 */
#     U_GCB_E_BASE_GAZ = 14
#     U_GCB_E_MODIFIER = 15
#     U_GCB_GLUE_AFTER_ZWJ = 16
#     U_GCB_ZWJ = 17
#
#
#
# class UWordBreakValues(ENUM):
#     U_WB_OTHER = 0
#     U_WB_ALETTER = 1
#     U_WB_FORMAT = 2
#     U_WB_KATAKANA = 3
#     U_WB_MIDLETTER = 4
#     U_WB_MIDNUM = 5
#     U_WB_NUMERIC = 6
#     U_WB_EXTENDNUMLET = 7
#     U_WB_CR = 8                 /* from here on: new in Unicode 5.1/ICU 4.0 */
#     U_WB_EXTEND = 9
#     U_WB_LF = 10
#     U_WB_MIDNUMLET = 11
#     U_WB_NEWLINE = 12
#     U_WB_REGIONAL_INDICATOR = 13    /* new in Unicode 6.2/ICU 50 */
#     U_WB_HEBREW_LETTER = 14     /* from here on: new in Unicode 6.3/ICU 52 */
#     U_WB_SINGLE_QUOTE = 15
#     U_WB_DOUBLE_QUOTE = 16
#     U_WB_E_BASE = 17            /* from here on: new in Unicode 9.0/ICU 58 */
#     U_WB_E_BASE_GAZ = 18
#     U_WB_E_MODIFIER = 19
#     U_WB_GLUE_AFTER_ZWJ = 20
#     U_WB_ZWJ = 21
#
#
#
# class USentenceBreak(ENUM):
#     U_SB_OTHER = 0
#     U_SB_ATERM = 1
#     U_SB_CLOSE = 2
#     U_SB_FORMAT = 3
#     U_SB_LOWER = 4
#     U_SB_NUMERIC = 5
#     U_SB_OLETTER = 6
#     U_SB_SEP = 7
#     U_SB_SP = 8
#     U_SB_STERM = 9
#     U_SB_UPPER = 10
#     U_SB_CR = 11                /* from here on: new in Unicode 5.1/ICU 4.0 */
#     U_SB_EXTEND = 12
#     U_SB_LF = 13
#     U_SB_SCONTINUE = 14
#
#
#
# class ULineBreak(ENUM):
#     U_LB_UNKNOWN = 0
#     U_LB_AMBIGUOUS = 1
#     U_LB_ALPHABETIC = 2
#     U_LB_BREAK_BOTH = 3
#     U_LB_BREAK_AFTER = 4
#     U_LB_BREAK_BEFORE = 5
#     U_LB_MANDATORY_BREAK = 6
#     U_LB_CONTINGENT_BREAK = 7
#     U_LB_CLOSE_PUNCTUATION = 8
#     U_LB_COMBINING_MARK = 9
#     U_LB_CARRIAGE_RETURN = 10
#     U_LB_EXCLAMATION = 11
#     U_LB_GLUE = 12
#     U_LB_HYPHEN = 13
#     U_LB_IDEOGRAPHIC = 14
#     U_LB_INSEPARABLE = 15
#     U_LB_INSEPERABLE = U_LB_INSEPARABLE
#     U_LB_INFIX_NUMERIC = 16
#     U_LB_LINE_FEED = 17
#     U_LB_NONSTARTER = 18
#     U_LB_NUMERIC = 19
#     U_LB_OPEN_PUNCTUATION = 20
#     U_LB_POSTFIX_NUMERIC = 21
#     U_LB_PREFIX_NUMERIC = 22
#     U_LB_QUOTATION = 23
#     U_LB_COMPLEX_CONTEXT = 24
#     U_LB_SURROGATE = 25
#     U_LB_SPACE = 26
#     U_LB_BREAK_SYMBOLS = 27
#     U_LB_ZWSPACE = 28
#     U_LB_NEXT_LINE = 29          /* from here on: new in Unicode 4/ICU 2.6 */
#     U_LB_WORD_JOINER = 30
#     U_LB_H2 = 31                 /* from here on: new in Unicode 4.1/ICU 3.4 */
#     U_LB_H3 = 32
#     U_LB_JL = 33
#     U_LB_JT = 34
#     U_LB_JV = 35
#     U_LB_CLOSE_PARENTHESIS = 36  /* new in Unicode 5.2/ICU 4.4 */
#     U_LB_CONDITIONAL_JAPANESE_STARTER = 37 /* new in Unicode 6.1/ICU 49 */
#     U_LB_HEBREW_LETTER = 38      /* new in Unicode 6.1/ICU 49 */
#     U_LB_REGIONAL_INDICATOR = 39 /* new in Unicode 6.2/ICU 50 */
#     U_LB_E_BASE = 40             /* from here on: new in Unicode 9.0/ICU 58 */
#     U_LB_E_MODIFIER = 41
#     U_LB_ZWJ = 42
#
#
#
# class UNumericType(ENUM):
#     U_NT_NONE = 0
#     U_NT_DECIMAL = 1
#     U_NT_DIGIT = 2
#     U_NT_NUMERIC = 3
#
#
#
# class UHangulSyllableType(ENUM):
#     U_HST_NOT_APPLICABLE = 0
#     U_HST_LEADING_JAMO = 1
#     U_HST_VOWEL_JAMO = 2
#     U_HST_TRAILING_JAMO = 3
#     U_HST_LV_SYLLABLE = 4
#     U_HST_LVT_SYLLABLE = 5
#
#
#
# U_NO_NUMERIC_VALUE = (DOUBLE)-123456789.
#
#
# def U_GET_GC_MASK(c):
#     return U_MASK(u_CHARTypec)
# U_FOLD_CASE_DEFAULT = 0x00000000
# U_FOLD_CASE_EXCLUDE_SPECIAL_I = 0x00000001
# UText = struct
#
#
#  = UText;
#
#
#
#
# def UTEXT_NEXT32(ut):
#     return ut.chunkOffset < ut.chunkLength and (ut.chunkContents)[ut.chunkOffset]<0xd800 ? (ut.chunkContents)[(ut.chunkOffset)++] : utext_next32ut
#
#
# def UTEXT_PREVIOUS32(ut):
#     return ut.chunkOffset > 0 and ut.chunkContents[ut.chunkOffset-1] < 0xd800 ? ut.chunkContents[--(ut.chunkOffset)] : utext_previous32ut
#
#
# def UTEXT_GETNATIVEINDEX(ut):
#     return ut.chunkOffset <= ut.nativeIndexingLimit? ut.chunkNativeStart+ut.chunkOffset : ut.pFuncs.mapOffsetToNativeut
#
#
# def UTEXT_SETNATIVEINDEX(ut, ix):
#     return { int64_t __offset = ix - ut.chunkNativeStart; if (__offset>=0 and __offset<=int64_tut.nativeIndexingLimit) { ut.chunkOffset=int32_t__offset; } else { utext_setNativeIndexut, ix; } }
# class (ENUM):
#     UTEXT_PROVIDER_LENGTH_IS_EXPENSIVE = 1
#     UTEXT_PROVIDER_STABLE_CHUNKS = 2
#     UTEXT_PROVIDER_WRITABLE = 3
#     UTEXT_PROVIDER_HAS_META_DATA = 4
#     UTEXT_PROVIDER_OWNS_TEXT = 5
#
#
#
#
# class UTextFuncs(ctypes.Structure):
#     _fields_ = [
#         ('tableSize', int32_t),
#         ('reserved1', int32_t),
#         ('reserved2', int32_t),
#         ('reserved3', int32_t),
#         ('clone', POINTER(UTextClone)),
#         ('nativeLength', POINTER(UTextNativeLength)),
#         ('access', POINTER(UTextAccess)),
#         ('extract', POINTER(UTextExtract)),
#         ('replace', POINTER(UTextReplace)),
#         ('copy', POINTER(UTextCopy)),
#         ('mapOffsetToNative', POINTER(UTextMapOffsetToNative)),
#         ('mapNativeIndexToUTF16', POINTER(UTextMapNativeIndexToUTF16)),
#         ('close', POINTER(UTextClose)),
#         ('spare1', POINTER(UTextClose)),
#         ('spare2', POINTER(UTextClose)),
#         ('spare3', POINTER(UTextClose)),
#     ]
#
#
#
# UTextFuncs = UTextFuncs
#
#
#
# class UText(ctypes.Structure):
#     _fields_ = [
#         ('magic', uint32_t),
#         ('flags', int32_t),
#         ('providerProperties', int32_t),
#         ('sizeOfStruct', int32_t),
#         ('chunkNativeLimit', int64_t),
#         ('extraSize', int32_t),
#         ('nativeIndexingLimit', int32_t),
#         ('chunkNativeStart', int64_t),
#         ('chunkOffset', int32_t),
#         ('chunkLength', int32_t),
#         ('chunkContents', POINTER(UChar)),
#         ('pFuncs', POINTER(UTextFuncs)),
#         ('pExtra', POINTER(VOID)),
#         ('context', POINTER(VOID)),
#         ('p', POINTER(VOID)),
#         ('q', POINTER(VOID)),
#         ('r', POINTER(VOID)),
#         ('privP', POINTER(VOID)),
#         ('a', int64_t),
#         ('b', int32_t),
#         ('c', int32_t),
#         ('privA', int64_t),
#         ('privB', int32_t),
#         ('privC', int32_t),
#     ]
#
#
#
# UTEXT_INITIALIZER = [
#     UTEXT_MAGIC,
#     0,
#     0,
#     ctypes.sizeof(UText),
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     NULL,
#     0,
#     0,
#     0,
#     0,
#     0,
#     0,
# ]
# USet = struct
#
#
# USet = USet
#
#
# class (ENUM):
#     USET_IGNORE_SPACE = 1
#     USET_CASE_INSENSITIVE = 2
#     USET_ADD_CASE_MAPPINGS = 4
#
#
#
# class USetSpanCondition(ENUM):
#     USET_SPAN_NOT_CONTAINED = 0
#     USET_SPAN_CONTAINED = 1
#     USET_SPAN_SIMPLE = 2
#
#
#
# class (ENUM):
#     USET_SERIALIZED_STATIC_ARRAY_CAPACITY = 8
#
#
#
#
# class USerializedSet(ctypes.Structure):
#     _fields_ = [
#         ('array', POINTER(uint16_t)),
#         ('bmpLength', int32_t),
#         ('length', int32_t),
#         ('staticArray', uint16_t * USET_SERIALIZED_STATIC_ARRAY_CAPACITY),
#     ]
#
#
#
# class UNormalization2Mode(ENUM):
#     UNORM2_COMPOSE = 0
#     UNORM2_DECOMPOSE = 1
#     UNORM2_FCD = 2
#     UNORM2_COMPOSE_CONTIGUOUS = 3
#
#
#
# class UNormalizationCheckResult(ENUM):
#     UNORM_NO = 0
#     UNORM_YES = 1
#     UNORM_MAYBE = 2
#
#
#
# UNormalizer2 = struct
#
#
#  =
#
#
# UNORM_INPUT_IS_FCD = 0x00020000
# U_COMPARE_IGNORE_CASE = 0x00010000
# U_COMPARE_CODE_POINT_ORDER = 0x00008000
# class UNormalizationMode(ENUM):
#     UNORM_NONE = 1
#     UNORM_NFD = 2
#     UNORM_NFKD = 3
#     UNORM_NFC = 4
#     UNORM_DEFAULT = UNORM_NFC
#     UNORM_NFKC = 5
#     UNORM_FCD = 6
#     UNORM_MODE_COUNT = 7
#
#
#
# UConverterSelector = struct
#
#
# UConverterSelector = UConverterSelector
#
#
# u_nl_catd = UResourceBundle*
# UBiDiLevel = uint8_t
# UBIDI_DEFAULT_LTR = 0x000000FE
# UBIDI_DEFAULT_RTL = 0x000000FF
# UBIDI_MAX_EXPLICIT_LEVEL = 0x0000007D
# UBIDI_LEVEL_OVERRIDE = 0x00000080
# UBIDI_MAP_NOWHERE = -1
# class UBiDiDirection(ENUM):
#     UBIDI_LTR = 0
#     UBIDI_RTL = 1
#     UBIDI_MIXED = 2
#     UBIDI_NEUTRAL = 3
#
#
#  = UBiDiDirection
#
#
# UBiDiDirection = UBiDiDirection
# UBiDi = struct
#
#
# UBiDi = UBiDi
#
#
# class UBiDiReorderingMode(ENUM):
#     UBIDI_REORDER_DEFAULT = 0
#     UBIDI_REORDER_NUMBERS_SPECIAL = 1
#     UBIDI_REORDER_GROUP_NUMBERS_WITH_R = 2
#     UBIDI_REORDER_RUNS_ONLY = 3
#     UBIDI_REORDER_INVERSE_NUMBERS_AS_L = 4
#     UBIDI_REORDER_INVERSE_LIKE_DIRECT = 5
#     UBIDI_REORDER_INVERSE_FOR_NUMBERS_SPECIAL = 6
#
#
#
# class UBiDiReorderingOption(ENUM):
#     UBIDI_OPTION_DEFAULT = 0
#     UBIDI_OPTION_INSERT_MARKS = 1
#     UBIDI_OPTION_REMOVE_CONTROLS = 2
#     UBIDI_OPTION_STREAMING = 4
#
#
#
# UBIDI_KEEP_BASE_COMBINING = 0x00000001
# UBIDI_DO_MIRRORING = 0x00000002
# UBIDI_INSERT_LRM_FOR_NUMERIC = 0x00000004
# UBIDI_REMOVE_BIDI_CONTROLS = 0x00000008
# UBIDI_OUTPUT_REVERSE = 0x00000010
# UHashtable = struct
#
#
# UHashtable = UHashtable
#
#
# class UStringTrieBuildOption(ENUM):
#     USTRINGTRIE_BUILD_FAST = 0
#     USTRINGTRIE_BUILD_SMALL = 1
#
#
#  = UStringTrieBuildOption
#
#
# U_COMPARE_CODE_POINT_ORDER = 0x00008000
#
#
# def U_STRING_DECL(var, cs, length):
#     return static UChar *var=UChar *U_DECLARE_UTF16cs
#
#
#
# def U_STRING_DECL(var, cs, length):
#     return static UChar var[length+1]=L ## cs
#
#
#
# def U_STRING_DECL(var, cs, length):
#     return static UChar var[length+1]=cs
#
#
#
# def U_STRING_DECL(var, cs, length):
#     return static UChar var[length+1]
#
#
# def U_STRING_INIT(var, cs, length):
#     return u_CHARsToUChars(cs, var, length+1)
# offset = UChar
# VOID context) = UChar
# UCaseMap = struct
#
#
#  = UCaseMap;
#
#
# U_TITLECASE_NO_LOWERCASE = 0x00000100
# U_TITLECASE_NO_BREAK_ADJUSTMENT = 0x00000200
# UCASEMAP_OMIT_UNCHANGED_TEXT = 0x00004000
# U_PARSE_CONTEXT_LEN = 16 } = {
#
#
# class UParseError(ctypes.Structure):
#     _fields_ = [
#         ('line', int32_t),
#         ('offset', int32_t),
#         ('preContext', UChar * U_PARSE_CONTEXT_LEN),
#         ('postContext', UChar * U_PARSE_CONTEXT_LEN),
#     ]
#
#
# UStringPrepProfile = UStringPrepProfile
#
#
# USPREP_DEFAULT = 0x00000000
# USPREP_ALLOW_UNASSIGNED = 0x00000001
#
#
# class UStringPrepProfileType(ENUM):
#     USPREP_RFC3491_NAMEPREP = 0
#     USPREP_RFC3530_NFS4_CS_PREP = 1
#     USPREP_RFC3530_NFS4_CS_PREP_CI = 2
#     USPREP_RFC3530_NFS4_CIS_PREP = 3
#     USPREP_RFC3530_NFS4_MIXED_PREP_PREFIX = 4
#     USPREP_RFC3530_NFS4_MIXED_PREP_SUFFIX = 5
#     USPREP_RFC3722_ISCSI = 6
#     USPREP_RFC3920_NODEPREP = 7
#     USPREP_RFC3920_RESOURCEPREP = 8
#     USPREP_RFC4011_MIB = 9
#     USPREP_RFC4013_SASLPREP = 10
#     USPREP_RFC4505_TRACE = 11
#     USPREP_RFC4518_LDAP = 12
#     USPREP_RFC4518_LDAP_CI = 13
#
#
# UIDNA_DEFAULT = 0
# UIDNA_USE_STD3_RULES = 2
# UIDNA_CHECK_BIDI = 4
# UIDNA_CHECK_CONTEXTJ = 8
# UIDNA_NONTRANSITIONAL_TO_ASCII = 0x10
# UIDNA_NONTRANSITIONAL_TO_UNICODE = 0x20
# UIDNA_CHECK_CONTEXTO = 0x40
#
#
#
# class UIDNA(ctypes.Structure):
#     pass
#
#
# class UIDNAInfo(ctypes.Structure):
#     _fields_ = [
#         ('size', int16_t),
#         ('isTransitionalDifferent', UBool),
#         ('reservedB3', UBool),
#         ('errors', uint32_t),
#         ('reservedI2', int32_t),
#         ('reservedI3', int32_t),
#     ]
#
#
#
# UIDNA_INFO_INITIALIZER = [
#     ctypes.sizeof(UIDNAInfo),
#     FALSE,
#     FALSE,
#     0,
#     0,
#     0,
# ]
#
#
#
# UIDNA_ERROR_EMPTY_LABEL = 1
# UIDNA_ERROR_LABEL_TOO_LONG = 2
# UIDNA_ERROR_DOMAIN_NAME_TOO_LONG = 4
# UIDNA_ERROR_LEADING_HYPHEN = 8
# UIDNA_ERROR_TRAILING_HYPHEN = 0x10
# UIDNA_ERROR_HYPHEN_3_4 = 0x20
# UIDNA_ERROR_LEADING_COMBINING_MARK = 0x40
# UIDNA_ERROR_DISALLOWED = 0x80
# UIDNA_ERROR_PUNYCODE = 0x100
# UIDNA_ERROR_LABEL_HAS_DOT = 0x200
# UIDNA_ERROR_INVALID_ACE_LABEL = 0x400
# UIDNA_ERROR_BIDI = 0x800
# UIDNA_ERROR_CONTEXTJ = 0x1000
# UIDNA_ERROR_CONTEXTO_PUNCTUATION = 0x2000
# UIDNA_ERROR_CONTEXTO_DIGITS = 0x4000
#
#
#
# class UBreakIteratorType(ENUM):
#     UBRK_CHARACTER = 0
#     UBRK_WORD = 1
#     UBRK_LINE = 2
#     UBRK_SENTENCE = 3
#
#
#
# UBRK_DONE = int32_t(-1)
#
#
# class UWordBreak(ENUM):
#     UBRK_WORD_NONE = 0
#     UBRK_WORD_NONE_LIMIT = 100
#     UBRK_WORD_NUMBER = 100
#     UBRK_WORD_NUMBER_LIMIT = 200
#     UBRK_WORD_LETTER = 200
#     UBRK_WORD_LETTER_LIMIT = 300
#     UBRK_WORD_KANA = 300
#     UBRK_WORD_KANA_LIMIT = 400
#     UBRK_WORD_IDEO = 400
#     UBRK_WORD_IDEO_LIMIT = 500
#
#
#
# class ULineBreakTag(ENUM):
#     UBRK_LINE_SOFT = 0
#     UBRK_LINE_SOFT_LIMIT = 100
#     UBRK_LINE_HARD = 100
#     UBRK_LINE_HARD_LIMIT = 200
#
#
#
# class USentenceBreakTag(ENUM):
#     UBRK_SENTENCE_TERM = 0
#     UBRK_SENTENCE_TERM_LIMIT = 100
#     UBRK_SENTENCE_SEP = 100
#     UBRK_SENTENCE_SEP_LIMIT = 200
#
#
#
# class UMessagePatternApostropheMode(ENUM):
#     UMSGPAT_APOS_DOUBLE_OPTIONAL = 0
#     UMSGPAT_APOS_DOUBLE_REQUIRED = 1
#
#
#
# class UMessagePatternPartType(ENUM):
#     UMSGPAT_PART_TYPE_MSG_START = 0
#     UMSGPAT_PART_TYPE_MSG_LIMIT = 1
#     UMSGPAT_PART_TYPE_SKIP_SYNTAX = 2
#     UMSGPAT_PART_TYPE_INSERT_CHAR = 3
#     UMSGPAT_PART_TYPE_REPLACE_NUMBER = 4
#     UMSGPAT_PART_TYPE_ARG_START = 5
#     UMSGPAT_PART_TYPE_ARG_LIMIT = 6
#     UMSGPAT_PART_TYPE_ARG_NUMBER = 7
#     UMSGPAT_PART_TYPE_ARG_NAME = 8
#     UMSGPAT_PART_TYPE_ARG_TYPE = 9
#     UMSGPAT_PART_TYPE_ARG_STYLE = 10
#     UMSGPAT_PART_TYPE_ARG_SELECTOR = 11
#     UMSGPAT_PART_TYPE_ARG_INT = 12
#     UMSGPAT_PART_TYPE_ARG_DOUBLE = 13
#
#
# class UMessagePatternArgType(ENUM):
#     UMSGPAT_ARG_TYPE_NONE = 0
#     UMSGPAT_ARG_TYPE_SIMPLE = 1
#     UMSGPAT_ARG_TYPE_CHOICE = 2
#     UMSGPAT_ARG_TYPE_PLURAL = 3
#     UMSGPAT_ARG_TYPE_SELECT = 4
#     UMSGPAT_ARG_TYPE_SELECTORDINAL = 5
#
#
# def UMSGPAT_ARG_TYPE_HAS_PLURAL_STYLE(argType):
#     return (argType==UMSGPAT_ARG_TYPE_PLURAL or argType==UMSGPAT_ARG_TYPE_SELECTORDINAL)
# class (ENUM):
#     UMSGPAT_ARG_NAME_NOT_NUMBER = - 1
#     UMSGPAT_ARG_NAME_NOT_VALID = - 2
#
#
#
# UMSGPAT_NO_NUMERIC_VALUE = (DOUBLE)(-123456789)
# U_ICU_VERSION_BUNDLE = "icuver"
# U_ICU_DATA_KEY = "DataVersion"
# CANITER_SKIP_ZEROES = TRUE
# class UAlphabeticIndexLabelType(ENUM):
#     U_ALPHAINDEX_NORMAL = 0
#     U_ALPHAINDEX_UNDERFLOW = 1
#     U_ALPHAINDEX_INFLOW = 2
#     U_ALPHAINDEX_OVERFLOW = 3
#
#
#
# UHashtable = struct
#
#
# NUMSYS_NAME_CAPACITY = 0x00000008
# class UTimeZoneNameType(ENUM):
#     UTZNM_UNKNOWN = 0x00
#     UTZNM_LONG_GENERIC = 0x01
#     UTZNM_LONG_STANDARD = 0x02
#     UTZNM_LONG_DAYLIGHT = 0x04
#     UTZNM_SHORT_GENERIC = 0x08
#     UTZNM_SHORT_STANDARD = 0x10
#     UTZNM_SHORT_DAYLIGHT = 0x20
#     UTZNM_EXEMPLAR_LOCATION = 0x40
#
#
#
# class UTimeZoneFormatStyle(ENUM):
#     UTZFMT_STYLE_GENERIC_LOCATION = 0
#     UTZFMT_STYLE_GENERIC_LONG = 1
#     UTZFMT_STYLE_GENERIC_SHORT = 2
#     UTZFMT_STYLE_SPECIFIC_LONG = 3
#     UTZFMT_STYLE_SPECIFIC_SHORT = 4
#     UTZFMT_STYLE_LOCALIZED_GMT = 5
#     UTZFMT_STYLE_LOCALIZED_GMT_SHORT = 6
#     UTZFMT_STYLE_ISO_BASIC_SHORT = 7
#     UTZFMT_STYLE_ISO_BASIC_LOCAL_SHORT = 8
#     UTZFMT_STYLE_ISO_BASIC_FIXED = 9
#     UTZFMT_STYLE_ISO_BASIC_LOCAL_FIXED = 10
#     UTZFMT_STYLE_ISO_BASIC_FULL = 11
#     UTZFMT_STYLE_ISO_BASIC_LOCAL_FULL = 12
#     UTZFMT_STYLE_ISO_EXTENDED_FIXED = 13
#     UTZFMT_STYLE_ISO_EXTENDED_LOCAL_FIXED = 14
#     UTZFMT_STYLE_ISO_EXTENDED_FULL = 15
#     UTZFMT_STYLE_ISO_EXTENDED_LOCAL_FULL = 16
#     UTZFMT_STYLE_ZONE_ID = 17
#     UTZFMT_STYLE_ZONE_ID_SHORT = 18
#     UTZFMT_STYLE_EXEMPLAR_LOCATION = 19
#
#
#
# class UTimeZoneFormatGMTOffsetPatternType(ENUM):
#     UTZFMT_PAT_POSITIVE_HM = 0
#     UTZFMT_PAT_POSITIVE_HMS = 1
#     UTZFMT_PAT_NEGATIVE_HM = 2
#     UTZFMT_PAT_NEGATIVE_HMS = 3
#     UTZFMT_PAT_POSITIVE_H = 4
#     UTZFMT_PAT_NEGATIVE_H = 5
#     UTZFMT_PAT_COUNT = 6
#
#
#
# class UTimeZoneFormatTimeType(ENUM):
#     UTZFMT_TIME_TYPE_UNKNOWN = 0
#     UTZFMT_TIME_TYPE_STANDARD = 1
#     UTZFMT_TIME_TYPE_DAYLIGHT = 2
#
#
#
# class UTimeZoneFormatParseOption(ENUM):
#     UTZFMT_PARSE_OPTION_NONE = 0x00
#     UTZFMT_PARSE_OPTION_ALL_STYLES = 0x01
#     UTZFMT_PARSE_OPTION_TZ_DATABASE_ABBREVIATIONS = 0x02
#
#
#
# UCAL_UNKNOWN_ZONE_ID = "Etc/Unknown"
# UCalendar = VOID*
# class UCalendarType(ENUM):
#     UCAL_TRADITIONAL = 0
#     UCAL_DEFAULT = UCAL_TRADITIONAL
#     UCAL_GREGORIAN = 1
#
#
#  = UCalendarType
#
#
# UCalendarType = UCalendarType
# class UCalendarDateFields(ENUM):
#     UCAL_ERA = 0
#     UCAL_YEAR = 1
#     UCAL_MONTH = 2
#     UCAL_WEEK_OF_YEAR = 3
#     UCAL_WEEK_OF_MONTH = 4
#     UCAL_DATE = 5
#     UCAL_DAY_OF_YEAR = 6
#     UCAL_DAY_OF_WEEK = 7
#     UCAL_DAY_OF_WEEK_IN_MONTH = 8
#     UCAL_AM_PM = 9
#     UCAL_HOUR = 10
#     UCAL_HOUR_OF_DAY = 11
#     UCAL_MINUTE = 12
#     UCAL_SECOND = 13
#     UCAL_MILLISECOND = 14
#     UCAL_ZONE_OFFSET = 15
#     UCAL_DST_OFFSET = 16
#     UCAL_YEAR_WOY = 17
#     UCAL_DOW_LOCAL = 18
#     UCAL_EXTENDED_YEAR = 19
#     UCAL_JULIAN_DAY = 20
#     UCAL_MILLISECONDS_IN_DAY = 21
#     UCAL_IS_LEAP_MONTH = 22
#     UCAL_FIELD_COUNT = 23
#     UCAL_DAY_OF_MONTH = UCAL_DATE
#
#
#  = UCalendarDateFields
#
#
# UCalendarDateFields = UCalendarDateFields
# class UCalendarDaysOfWeek(ENUM):
#     UCAL_SUNDAY = 1
#     UCAL_MONDAY = 2
#     UCAL_TUESDAY = 3
#     UCAL_WEDNESDAY = 4
#     UCAL_THURSDAY = 5
#     UCAL_FRIDAY = 6
#     UCAL_SATURDAY = 7
#
#
#  = UCalendarDaysOfWeek
#
#
# UCalendarDaysOfWeek = UCalendarDaysOfWeek
# class UCalendarMonths(ENUM):
#     UCAL_JANUARY = 0
#     UCAL_FEBRUARY = 1
#     UCAL_MARCH = 2
#     UCAL_APRIL = 3
#     UCAL_MAY = 4
#     UCAL_JUNE = 5
#     UCAL_JULY = 6
#     UCAL_AUGUST = 7
#     UCAL_SEPTEMBER = 8
#     UCAL_OCTOBER = 9
#     UCAL_NOVEMBER = 10
#     UCAL_DECEMBER = 11
#     UCAL_UNDECIMBER = 12
#
#
#  = UCalendarMonths
#
#
# UCalendarMonths = UCalendarMonths
# class UCalendarAMPMs(ENUM):
#     UCAL_AM = 0
#     UCAL_PM = 1
#
#
#  = UCalendarAMPMs
#
#
# UCalendarAMPMs = UCalendarAMPMs
# class USystemTimeZoneType(ENUM):
#     UCAL_ZONE_TYPE_ANY = 0
#     UCAL_ZONE_TYPE_CANONICAL = 1
#     UCAL_ZONE_TYPE_CANONICAL_LOCATION = 2
#
#
#  = USystemTimeZoneType
#
#
# USystemTimeZoneType = USystemTimeZoneType
# class UCalendarDisplayNameType(ENUM):
#     UCAL_STANDARD = 0
#     UCAL_SHORT_STANDARD = 1
#     UCAL_DST = 2
#     UCAL_SHORT_DST = 3
#
#
#  = UCalendarDisplayNameType
#
#
# UCalendarDisplayNameType = UCalendarDisplayNameType
# class UCalendarAttribute(ENUM):
#     UCAL_LENIENT = 0
#     UCAL_FIRST_DAY_OF_WEEK = 1
#     UCAL_MINIMAL_DAYS_IN_FIRST_WEEK = 2
#     UCAL_REPEATED_WALL_TIME = 3
#     UCAL_SKIPPED_WALL_TIME = 4
#
#
#  = UCalendarAttribute
#
#
# UCalendarAttribute = UCalendarAttribute
# class UCalendarWallTimeOption(ENUM):
#     UCAL_WALLTIME_LAST = 0
#     UCAL_WALLTIME_FIRST = 1
#     UCAL_WALLTIME_NEXT_VALID = 2
#
#
#  = UCalendarWallTimeOption
#
#
# UCalendarWallTimeOption = UCalendarWallTimeOption
# class UCalendarLimitType(ENUM):
#     UCAL_MINIMUM = 0
#     UCAL_MAXIMUM = 1
#     UCAL_GREATEST_MINIMUM = 2
#     UCAL_LEAST_MAXIMUM = 3
#     UCAL_ACTUAL_MINIMUM = 4
#     UCAL_ACTUAL_MAXIMUM = 5
#
#
#  = UCalendarLimitType
#
#
# UCalendarLimitType = UCalendarLimitType
# class UCalendarWeekdayType(ENUM):
#     UCAL_WEEKDAY = 0
#     UCAL_WEEKEND = 1
#     UCAL_WEEKEND_ONSET = 2
#     UCAL_WEEKEND_CEASE = 3
#
#
#  = UCalendarWeekdayType
#
#
# UCalendarWeekdayType = UCalendarWeekdayType
# class UTimeZoneTransitionType(ENUM):
#     UCAL_TZ_TRANSITION_NEXT = 0
#     UCAL_TZ_TRANSITION_NEXT_INCLUSIVE = 1
#     UCAL_TZ_TRANSITION_PREVIOUS = 2
#     UCAL_TZ_TRANSITION_PREVIOUS_INCLUSIVE = 3
#
#
#  = UTimeZoneTransitionType
#
#
# UTimeZoneTransitionType = UTimeZoneTransitionType
# UCollator = struct
#
#
# UCollator = UCollator
#
#
# class UCollationResult(ENUM):
#     UCOL_EQUAL = 0
#     UCOL_GREATER = 1
#     UCOL_LESS = - 1
#
#
#
# class UColAttributeValue(ENUM):
#     UCOL_DEFAULT = - 1
#     UCOL_PRIMARY = 0
#     UCOL_SECONDARY = 1
#     UCOL_TERTIARY = 2
#     UCOL_DEFAULT_STRENGTH = UCOL_TERTIARY
#     UCOL_CE_STRENGTH_LIMIT = 3
#     UCOL_QUATERNARY = 3
#     UCOL_IDENTICAL = 15
#     UCOL_STRENGTH_LIMIT = 16
#     UCOL_OFF = 16
#     UCOL_ON = 17
#     UCOL_SHIFTED = 20
#     UCOL_NON_IGNORABLE = 21
#     UCOL_LOWER_FIRST = 24
#     UCOL_UPPER_FIRST = 25
#
#
#
# UCollationStrength = UColAttributeValue
# class UColAttribute(ENUM):
#     UCOL_FRENCH_COLLATION = 0
#     UCOL_ALTERNATE_HANDLING = 1
#     UCOL_CASE_FIRST = 2
#     UCOL_CASE_LEVEL = 3
#     UCOL_NORMALIZATION_MODE = 4
#     UCOL_DECOMPOSITION_MODE = UCOL_NORMALIZATION_MODE
#     UCOL_STRENGTH = 5
#     UCOL_NUMERIC_COLLATION = UCOL_STRENGTH + 2
#     UCOL_ATTRIBUTE_COUNT = 6
#
#
#
# class UColRuleOption(ENUM):
#     UCOL_TAILORING_ONLY = 0
#     UCOL_FULL_RULES = 1
#
#
#
# class UColBoundMode(ENUM):
#     UCOL_BOUND_LOWER = 0
#     UCOL_BOUND_UPPER = 1
#     UCOL_BOUND_UPPER_LONG = 2
#
#
#
# UCOL_NULLORDER = (int32_t)0xFFFFFFFF
# UCollationElements = UCollationElements
#
#
# UCharsetDetector = struct
#
#
# UCharsetDetector = UCharsetDetector
#
#
# UCharsetMatch = struct
#
#
# UCharsetMatch = UCharsetMatch
#
#
# UDateIntervalFormat = struct
#
#
#  =
#
#
# UDateTimePatternGenerator = POINTER(VOID)
# class UDateTimePatternField(ENUM):
#     UDATPG_ERA_FIELD = 0
#     UDATPG_YEAR_FIELD = 1
#     UDATPG_QUARTER_FIELD = 2
#     UDATPG_MONTH_FIELD = 3
#     UDATPG_WEEK_OF_YEAR_FIELD = 4
#     UDATPG_WEEK_OF_MONTH_FIELD = 5
#     UDATPG_WEEKDAY_FIELD = 6
#     UDATPG_DAY_OF_YEAR_FIELD = 7
#     UDATPG_DAY_OF_WEEK_IN_MONTH_FIELD = 8
#     UDATPG_DAY_FIELD = 9
#     UDATPG_DAYPERIOD_FIELD = 10
#     UDATPG_HOUR_FIELD = 11
#     UDATPG_MINUTE_FIELD = 12
#     UDATPG_SECOND_FIELD = 13
#     UDATPG_FRACTIONAL_SECOND_FIELD = 14
#     UDATPG_ZONE_FIELD = 15
#     UDATPG_FIELD_COUNT = 16
#
#
#
# class UDateTimePatternMatchOptions(ENUM):
#     UDATPG_MATCH_NO_OPTIONS = 0
#     UDATPG_MATCH_HOUR_FIELD_LENGTH = 1 << UDATPG_HOUR_FIELD
#     UDATPG_MATCH_ALL_FIELDS_LENGTH = (1 << UDATPG_FIELD_COUNT) - 1
#
#
#
# class UDateTimePatternConflict(ENUM):
#     UDATPG_NO_CONFLICT = 0
#     UDATPG_BASE_CONFLICT = 1
#     UDATPG_CONFLICT = 2
#
#
#
# UFieldPositionIterator = struct
#
#
#  =
#
#
# class UFormattableType(ENUM):
#     UFMT_DATE = 0
#     UFMT_DOUBLE = 1
#     UFMT_LONG = 2
#     UFMT_STRING = 3
#     UFMT_ARRAY = 4
#     UFMT_INT64 = 5
#     UFMT_OBJECT = 6
#
#
#
# UFormattable = POINTER(VOID)
# class UGender(ENUM):
#     UGENDER_MALE = 0
#     UGENDER_FEMALE = 1
#     UGENDER_OTHER = 2
#
#
#  = UGender
#
#
# UGender = UGender
# UGenderInfo = struct
#
#
# UGenderInfo = UGenderInfo
#
#
# ULocaleData = struct
#
#
# ULocaleData = ULocaleData
#
#
# class ULocaleDataExemplarSetType(ENUM):
#     ULOCDATA_ES_STANDARD = 0
#     ULOCDATA_ES_AUXILIARY = 1
#     ULOCDATA_ES_INDEX = 2
#     ULOCDATA_ES_PUNCTUATION = 3
#
#
#
# class ULocaleDataDelimiterType(ENUM):
#     ULOCDATA_QUOTATION_START = 0
#     ULOCDATA_QUOTATION_END = 1
#     ULOCDATA_ALT_QUOTATION_START = 2
#     ULOCDATA_ALT_QUOTATION_END = 3
#
#
#
# class UMeasurementSystem(ENUM):
#     UMS_SI = 0
#     UMS_US = 1
#     UMS_UK = 2
#
#
#
# from stdarg_h import * # NOQA
# UMessageFormat = VOID*
# UNumberFormat = VOID*
# class UNumberFormatStyle(ENUM):
#     UNUM_PATTERN_DECIMAL = 0
#     UNUM_DECIMAL = 1
#     UNUM_CURRENCY = 2
#     UNUM_PERCENT = 3
#     UNUM_SCIENTIFIC = 4
#     UNUM_SPELLOUT = 5
#     UNUM_ORDINAL = 6
#     UNUM_DURATION = 7
#     UNUM_NUMBERING_SYSTEM = 8
#     UNUM_PATTERN_RULEBASED = 9
#     UNUM_CURRENCY_ISO = 10
#     UNUM_CURRENCY_PLURAL = 11
#     UNUM_CURRENCY_ACCOUNTING = 12
#     UNUM_CASH_CURRENCY = 13
#     UNUM_DECIMAL_COMPACT_SHORT = 14
#     UNUM_DECIMAL_COMPACT_LONG = 15
#     UNUM_CURRENCY_STANDARD = 16
#     UNUM_DEFAULT = UNUM_DECIMAL
#     UNUM_IGNORE = UNUM_PATTERN_DECIMAL
#
#
#
# class UNumberFormatRoundingMode(ENUM):
#     UNUM_ROUND_CEILING = 0
#     UNUM_ROUND_FLOOR = 1
#     UNUM_ROUND_DOWN = 2
#     UNUM_ROUND_UP = 3
#     UNUM_ROUND_HALFEVEN = 4
#     UNUM_ROUND_HALFDOWN = UNUM_ROUND_HALFEVEN + 1
#     UNUM_ROUND_HALFUP = 5
#     UNUM_ROUND_UNNECESSARY = 6
#
#
#
# class UNumberFormatPadPosition(ENUM):
#     UNUM_PAD_BEFORE_PREFIX = 0
#     UNUM_PAD_AFTER_PREFIX = 1
#     UNUM_PAD_BEFORE_SUFFIX = 2
#     UNUM_PAD_AFTER_SUFFIX = 3
#
#
#
# class UNumberCompactStyle(ENUM):
#     UNUM_SHORT = 0
#     UNUM_LONG = 1
#
#
#
# class UCurrencySpacing(ENUM):
#     UNUM_CURRENCY_MATCH = 0
#     UNUM_CURRENCY_SURROUNDING_MATCH = 1
#     UNUM_CURRENCY_INSERT = 2
#     UNUM_CURRENCY_SPACING_COUNT = 3
#
#
#  = UCurrencySpacing
#
#
# class UNumberFormatFields(ENUM):
#     UNUM_INTEGER_FIELD = 0
#     UNUM_FRACTION_FIELD = 1
#     UNUM_DECIMAL_SEPARATOR_FIELD = 2
#     UNUM_EXPONENT_SYMBOL_FIELD = 3
#     UNUM_EXPONENT_SIGN_FIELD = 4
#     UNUM_EXPONENT_FIELD = 5
#     UNUM_GROUPING_SEPARATOR_FIELD = 6
#     UNUM_CURRENCY_FIELD = 7
#     UNUM_PERCENT_FIELD = 8
#     UNUM_PERMILL_FIELD = 9
#     UNUM_SIGN_FIELD = 10
#
#
#
# class UNumberFormatAttributeValue(ENUM):
#     UNUM_FORMAT_ATTRIBUTE_VALUE_HIDDEN = 0
#
#
#
# class UNumberFormatAttribute(ENUM):
#     UNUM_PARSE_INT_ONLY = 0
#     UNUM_GROUPING_USED = 1
#     UNUM_DECIMAL_ALWAYS_SHOWN = 2
#     UNUM_MAX_INTEGER_DIGITS = 3
#     UNUM_MIN_INTEGER_DIGITS = 4
#     UNUM_INTEGER_DIGITS = 5
#     UNUM_MAX_FRACTION_DIGITS = 6
#     UNUM_MIN_FRACTION_DIGITS = 7
#     UNUM_FRACTION_DIGITS = 8
#     UNUM_MULTIPLIER = 9
#     UNUM_GROUPING_SIZE = 10
#     UNUM_ROUNDING_MODE = 11
#     UNUM_ROUNDING_INCREMENT = 12
#     UNUM_FORMAT_WIDTH = 13
#     UNUM_PADDING_POSITION = 14
#     UNUM_SECONDARY_GROUPING_SIZE = 15
#     UNUM_SIGNIFICANT_DIGITS_USED = 16
#     UNUM_MIN_SIGNIFICANT_DIGITS = 17
#     UNUM_MAX_SIGNIFICANT_DIGITS = 18
#     UNUM_LENIENT_PARSE = 19
#     #if UCONFIG_HAVE_PARSEALLINPUT = 20
#     UNUM_PARSE_ALL_INPUT = 20
#     #endif = 21
#     UNUM_SCALE = 21
#     UNUM_CURRENCY_USAGE = 23
#     UNUM_MAX_NONBOOLEAN_ATTRIBUTE = 0x0FFF
#     UNUM_FORMAT_FAIL_IF_MORE_THAN_MAX_DIGITS = 0x1000
#     UNUM_PARSE_NO_EXPONENT = 4097
#     UNUM_PARSE_DECIMAL_MARK_REQUIRED = 0x1002
#     UNUM_LIMIT_BOOLEAN_ATTRIBUTE = 0x1003
#
#
#
# class UNumberFormatTextAttribute(ENUM):
#     UNUM_POSITIVE_PREFIX = 0
#     UNUM_POSITIVE_SUFFIX = 1
#     UNUM_NEGATIVE_PREFIX = 2
#     UNUM_NEGATIVE_SUFFIX = 3
#     UNUM_PADDING_CHARACTER = 4
#     UNUM_CURRENCY_CODE = 5
#     UNUM_DEFAULT_RULESET = 6
#     UNUM_PUBLIC_RULESETS = 7
#
#
#
# class UNumberFormatSymbol(ENUM):
#     UNUM_DECIMAL_SEPARATOR_SYMBOL = 0
#     UNUM_GROUPING_SEPARATOR_SYMBOL = 1
#     UNUM_PATTERN_SEPARATOR_SYMBOL = 2
#     UNUM_PERCENT_SYMBOL = 3
#     UNUM_ZERO_DIGIT_SYMBOL = 4
#     UNUM_DIGIT_SYMBOL = 5
#     UNUM_MINUS_SIGN_SYMBOL = 6
#     UNUM_PLUS_SIGN_SYMBOL = 7
#     UNUM_CURRENCY_SYMBOL = 8
#     UNUM_INTL_CURRENCY_SYMBOL = 9
#     UNUM_MONETARY_SEPARATOR_SYMBOL = 10
#     UNUM_EXPONENTIAL_SYMBOL = 11
#     UNUM_PERMILL_SYMBOL = 12
#     UNUM_PAD_ESCAPE_SYMBOL = 13
#     UNUM_INFINITY_SYMBOL = 14
#     UNUM_NAN_SYMBOL = 15
#     UNUM_SIGNIFICANT_DIGIT_SYMBOL = 16
#     UNUM_MONETARY_GROUPING_SEPARATOR_SYMBOL = 17
#     UNUM_ONE_DIGIT_SYMBOL = 18
#     UNUM_TWO_DIGIT_SYMBOL = 19
#     UNUM_THREE_DIGIT_SYMBOL = 20
#     UNUM_FOUR_DIGIT_SYMBOL = 21
#     UNUM_FIVE_DIGIT_SYMBOL = 22
#     UNUM_SIX_DIGIT_SYMBOL = 23
#     UNUM_SEVEN_DIGIT_SYMBOL = 24
#     UNUM_EIGHT_DIGIT_SYMBOL = 25
#     UNUM_NINE_DIGIT_SYMBOL = 26
#     UNUM_EXPONENT_MULTIPLICATION_SYMBOL = 27
#
#
#
# UDateFormat = VOID*
# class UDateFormatStyle(ENUM):
#     UDAT_FULL = 0
#     UDAT_LONG = 1
#     UDAT_MEDIUM = 2
#     UDAT_SHORT = 3
#     UDAT_DEFAULT = UDAT_MEDIUM
#     UDAT_RELATIVE = 1 << 7
#     UDAT_FULL_RELATIVE = UDAT_FULL | UDAT_RELATIVE
#     UDAT_LONG_RELATIVE = UDAT_LONG | UDAT_RELATIVE
#     UDAT_MEDIUM_RELATIVE = UDAT_MEDIUM | UDAT_RELATIVE
#     UDAT_SHORT_RELATIVE = UDAT_SHORT | UDAT_RELATIVE
#     UDAT_NONE = - 1
#     UDAT_PATTERN = - 2
#
#
#
# UDAT_YEAR = "y"
# UDAT_QUARTER = "QQQQ"
# UDAT_ABBR_QUARTER = "QQQ"
# UDAT_YEAR_QUARTER = "yQQQQ"
# UDAT_YEAR_ABBR_QUARTER = "yQQQ"
# UDAT_MONTH = "MMMM"
# UDAT_ABBR_MONTH = "MMM"
# UDAT_NUM_MONTH = "M"
# UDAT_YEAR_MONTH = "yMMMM"
# UDAT_YEAR_ABBR_MONTH = "yMMM"
# UDAT_YEAR_NUM_MONTH = "yM"
# UDAT_DAY = "d"
# UDAT_YEAR_MONTH_DAY = "yMMMMd"
# UDAT_YEAR_ABBR_MONTH_DAY = "yMMMd"
# UDAT_YEAR_NUM_MONTH_DAY = "yMd"
# UDAT_WEEKDAY = "EEEE"
# UDAT_ABBR_WEEKDAY = "E"
# UDAT_YEAR_MONTH_WEEKDAY_DAY = "yMMMMEEEEd"
# UDAT_YEAR_ABBR_MONTH_WEEKDAY_DAY = "yMMMEd"
# UDAT_YEAR_NUM_MONTH_WEEKDAY_DAY = "yMEd"
# UDAT_MONTH_DAY = "MMMMd"
# UDAT_ABBR_MONTH_DAY = "MMMd"
# UDAT_NUM_MONTH_DAY = "Md"
# UDAT_MONTH_WEEKDAY_DAY = "MMMMEEEEd"
# UDAT_ABBR_MONTH_WEEKDAY_DAY = "MMMEd"
# UDAT_NUM_MONTH_WEEKDAY_DAY = "MEd"
# UDAT_HOUR = "j"
# UDAT_HOUR24 = "H"
# UDAT_MINUTE = "m"
# UDAT_HOUR_MINUTE = "jm"
# UDAT_HOUR24_MINUTE = "Hm"
# UDAT_SECOND = "s"
# UDAT_HOUR_MINUTE_SECOND = "jms"
# UDAT_HOUR24_MINUTE_SECOND = "Hms"
# UDAT_MINUTE_SECOND = "ms"
# UDAT_LOCATION_TZ = "VVVV"
# UDAT_GENERIC_TZ = "vvvv"
# UDAT_ABBR_GENERIC_TZ = "v"
# UDAT_SPECIFIC_TZ = "zzzz"
# UDAT_ABBR_SPECIFIC_TZ = "z"
# UDAT_ABBR_UTC_TZ = "ZZZZ"
# class UDateFormatField(ENUM):
#     UDAT_ERA_FIELD = 0
#     UDAT_YEAR_FIELD = 1
#     UDAT_MONTH_FIELD = 2
#     UDAT_DATE_FIELD = 3
#     UDAT_HOUR_OF_DAY1_FIELD = 4
#     UDAT_HOUR_OF_DAY0_FIELD = 5
#     UDAT_MINUTE_FIELD = 6
#     UDAT_SECOND_FIELD = 7
#     UDAT_FRACTIONAL_SECOND_FIELD = 8
#     UDAT_DAY_OF_WEEK_FIELD = 9
#     UDAT_DAY_OF_YEAR_FIELD = 10
#     UDAT_DAY_OF_WEEK_IN_MONTH_FIELD = 11
#     UDAT_WEEK_OF_YEAR_FIELD = 12
#     UDAT_WEEK_OF_MONTH_FIELD = 13
#     UDAT_AM_PM_FIELD = 14
#     UDAT_HOUR1_FIELD = 15
#     UDAT_HOUR0_FIELD = 16
#     UDAT_TIMEZONE_FIELD = 17
#     UDAT_YEAR_WOY_FIELD = 18
#     UDAT_DOW_LOCAL_FIELD = 19
#     UDAT_EXTENDED_YEAR_FIELD = 20
#     UDAT_JULIAN_DAY_FIELD = 21
#     UDAT_MILLISECONDS_IN_DAY_FIELD = 22
#     UDAT_TIMEZONE_RFC_FIELD = 23
#     UDAT_TIMEZONE_GENERIC_FIELD = 24
#     UDAT_STANDALONE_DAY_FIELD = 25
#     UDAT_STANDALONE_MONTH_FIELD = 26
#     UDAT_QUARTER_FIELD = 27
#     UDAT_STANDALONE_QUARTER_FIELD = 28
#     UDAT_TIMEZONE_SPECIAL_FIELD = 29
#     UDAT_YEAR_NAME_FIELD = 30
#     UDAT_TIMEZONE_LOCALIZED_GMT_OFFSET_FIELD = 31
#     UDAT_TIMEZONE_ISO_FIELD = 32
#     UDAT_TIMEZONE_ISO_LOCAL_FIELD = 33
#     UDAT_AM_PM_MIDNIGHT_NOON_FIELD = 35
#     UDAT_FLEXIBLE_DAY_PERIOD_FIELD = 36
#
#
#
# class UDateFormatBooleanAttribute(ENUM):
#     UDAT_PARSE_ALLOW_WHITESPACE = 0
#     UDAT_PARSE_ALLOW_NUMERIC = 1
#     UDAT_PARSE_PARTIAL_LITERAL_MATCH = 2
#     UDAT_PARSE_MULTIPLE_PATTERNS_FOR_MATCH = 3
#     UDAT_BOOLEAN_ATTRIBUTE_COUNT = 4
#
#
#
# class UDateFormatSymbolType(ENUM):
#     UDAT_ERAS = 0
#     UDAT_MONTHS = 1
#     UDAT_SHORT_MONTHS = 2
#     UDAT_WEEKDAYS = 3
#     UDAT_SHORT_WEEKDAYS = 4
#     UDAT_AM_PMS = 5
#     UDAT_LOCALIZED_CHARS = 6
#     UDAT_ERA_NAMES = 7
#     UDAT_NARROW_MONTHS = 8
#     UDAT_NARROW_WEEKDAYS = 9
#     UDAT_STANDALONE_MONTHS = 10
#     UDAT_STANDALONE_SHORT_MONTHS = 11
#     UDAT_STANDALONE_NARROW_MONTHS = 12
#     UDAT_STANDALONE_WEEKDAYS = 13
#     UDAT_STANDALONE_SHORT_WEEKDAYS = 14
#     UDAT_STANDALONE_NARROW_WEEKDAYS = 15
#     UDAT_QUARTERS = 16
#     UDAT_SHORT_QUARTERS = 17
#     UDAT_STANDALONE_QUARTERS = 18
#     UDAT_STANDALONE_SHORT_QUARTERS = 19
#     UDAT_SHORTER_WEEKDAYS = 20
#     UDAT_STANDALONE_SHORTER_WEEKDAYS = 21
#     UDAT_CYCLIC_YEARS_WIDE = 22
#     UDAT_CYCLIC_YEARS_ABBREVIATED = 23
#     UDAT_CYCLIC_YEARS_NARROW = 24
#     UDAT_ZODIAC_NAMES_WIDE = 25
#     UDAT_ZODIAC_NAMES_ABBREVIATED = 26
#     UDAT_ZODIAC_NAMES_NARROW = 27
#
#
#
# UDateFormatSymbols = struct
#
#
# UDateFormatSymbols = UDateFormatSymbols
#
#
# class UMeasureFormatWidth(ENUM):
#     UMEASFMT_WIDTH_WIDE = 0
#     UMEASFMT_WIDTH_SHORT = 1
#     UMEASFMT_WIDTH_NARROW = 2
#     UMEASFMT_WIDTH_NUMERIC = 3
#
#
#  = UMeasureFormatWidth
#
#
# UMeasureFormatWidth = UMeasureFormatWidth
# UNumberingSystem = struct
#
#
#  =
#
#
# class UPluralType(ENUM):
#     UPLURAL_TYPE_CARDINAL = 0
#     UPLURAL_TYPE_ORDINAL = 1
#
#
#  = UPluralType
#
#
# UPluralType = UPluralType
# UPluralRules = struct
#
#
#  =
#
#
# U_HAVE_RBNF = 0x00000000
# U_HAVE_RBNF = 0x00000001
# UPLRULES_NO_UNIQUE_VALUE = (DOUBLE)-0.00123456777
# UHashtable = struct
#
#
#  = UHashtable;
#
#
# URegularExpression = struct
#
#
# URegularExpression = URegularExpression
#
#
# class URegexpFlag(ENUM):
#     UREGEX_CASE_INSENSITIVE = 2
#     UREGEX_COMMENTS = 4
#     UREGEX_DOTALL = 32
#     UREGEX_LITERAL = 16
#     UREGEX_MULTILINE = 8
#     UREGEX_UNIX_LINES = 1
#     UREGEX_UWORD = 256
#     UREGEX_ERROR_ON_UNKNOWN_ESCAPES = 512
#
#
#
# class URegionType(ENUM):
#     URGN_UNKNOWN = 0
#     URGN_TERRITORY = 1
#     URGN_WORLD = 2
#     URGN_CONTINENT = 3
#     URGN_SUBCONTINENT = 4
#     URGN_GROUPING = 5
#     URGN_DEPRECATED = 6
#
#
#
# URegion = struct
#
#
#  = URegion;
#
#
# class UDateRelativeDateTimeFormatterStyle(ENUM):
#     UDAT_STYLE_LONG = 0
#     UDAT_STYLE_SHORT = 1
#     UDAT_STYLE_NARROW = 2
#
#
#
# class URelativeDateTimeUnit(ENUM):
#     UDAT_REL_UNIT_YEAR = 0
#     UDAT_REL_UNIT_QUARTER = 1
#     UDAT_REL_UNIT_MONTH = 2
#     UDAT_REL_UNIT_WEEK = 3
#     UDAT_REL_UNIT_DAY = 4
#     UDAT_REL_UNIT_HOUR = 5
#     UDAT_REL_UNIT_MINUTE = 6
#     UDAT_REL_UNIT_SECOND = 7
#     UDAT_REL_UNIT_SUNDAY = 8
#     UDAT_REL_UNIT_MONDAY = 9
#     UDAT_REL_UNIT_TUESDAY = 10
#     UDAT_REL_UNIT_WEDNESDAY = 11
#     UDAT_REL_UNIT_THURSDAY = 12
#     UDAT_REL_UNIT_FRIDAY = 13
#     UDAT_REL_UNIT_SATURDAY = 14
#
#
#
# URelativeDateTimeFormatter = struct
#
#
#  =
#
#
# class UDateRelativeUnit(ENUM):
#     UDAT_RELATIVE_SECONDS = 0
#     UDAT_RELATIVE_MINUTES = 1
#     UDAT_RELATIVE_HOURS = 2
#     UDAT_RELATIVE_DAYS = 3
#     UDAT_RELATIVE_WEEKS = 4
#     UDAT_RELATIVE_MONTHS = 5
#     UDAT_RELATIVE_YEARS = 6
#
#
#
# class UDateAbsoluteUnit(ENUM):
#     UDAT_ABSOLUTE_SUNDAY = 0
#     UDAT_ABSOLUTE_MONDAY = 1
#     UDAT_ABSOLUTE_TUESDAY = 2
#     UDAT_ABSOLUTE_WEDNESDAY = 3
#     UDAT_ABSOLUTE_THURSDAY = 4
#     UDAT_ABSOLUTE_FRIDAY = 5
#     UDAT_ABSOLUTE_SATURDAY = 6
#     UDAT_ABSOLUTE_DAY = 7
#     UDAT_ABSOLUTE_WEEK = 8
#     UDAT_ABSOLUTE_MONTH = 9
#     UDAT_ABSOLUTE_YEAR = 10
#     UDAT_ABSOLUTE_NOW = 11
#
#
#
# class UDateDirection(ENUM):
#     UDAT_DIRECTION_LAST_2 = 0
#     UDAT_DIRECTION_LAST = 1
#     UDAT_DIRECTION_THIS = 2
#     UDAT_DIRECTION_NEXT = 3
#     UDAT_DIRECTION_NEXT_2 = 4
#     UDAT_DIRECTION_PLAIN = 5
#
#
#
# USEARCH_DONE = -1
# UStringSearch = struct
#
#
# UStringSearch = UStringSearch
#
#
# class USearchAttribute(ENUM):
#     USEARCH_OVERLAP = 0
#     USEARCH_ELEMENT_COMPARISON = 2
#
#
#
# class USearchAttributeValue(ENUM):
#     USEARCH_DEFAULT = - 1
#     USEARCH_OFF = 0
#     USEARCH_ON = 1
#     USEARCH_STANDARD_ELEMENT_COMPARISON = 2
#     USEARCH_PATTERN_BASE_WEIGHT_IS_WILDCARD = 3
#     USEARCH_ANY_BASE_WEIGHT_IS_WILDCARD = 4
#
#
#
# USearch = struct
#
#
# USearch = USearch
#
#
# USpoofChecker = struct
#
#
#  = USpoofChecker;
#
#
# class USpoofChecks(ENUM):
#     USPOOF_SINGLE_SCRIPT_CONFUSABLE = 1
#     USPOOF_MIXED_SCRIPT_CONFUSABLE = 2
#     USPOOF_WHOLE_SCRIPT_CONFUSABLE = 4
#     USPOOF_RESTRICTION_LEVEL = 16
#     USPOOF_INVISIBLE = 32
#     USPOOF_CHAR_LIMIT = 64
#     USPOOF_MIXED_NUMBERS = 128
#     USPOOF_ALL_CHECKS = 0xFFFF
#     USPOOF_AUX_INFO = 0x40000000
#
#
#
# class UDateTimeScale(ENUM):
#     UDTS_JAVA_TIME = 0
#     UDTS_UNIX_TIME = 1
#     UDTS_ICU4C_TIME = 2
#     UDTS_WINDOWS_FILE_TIME = 3
#     UDTS_DOTNET_DATE_TIME = 4
#     UDTS_MAC_OLD_TIME = 5
#     UDTS_MAC_TIME = 6
#     UDTS_EXCEL_TIME = 7
#     UDTS_DB2_TIME = 8
#     UDTS_UNIX_MICROSECONDS_TIME = 9
#
#
#
# class UTimeScaleValue(ENUM):
#     UTSV_UNITS_VALUE = 0
#     UTSV_EPOCH_OFFSET_VALUE = 1
#     UTSV_FROM_MIN_VALUE = 2
#     UTSV_FROM_MAX_VALUE = 3
#     UTSV_TO_MIN_VALUE = 4
#     UTSV_TO_MAX_VALUE = 5
#
#
#
# UTransliterator = VOID*
# class UTransDirection(ENUM):
#     UTRANS_FORWARD = 0
#     UTRANS_REVERSE = 1
#
#
#
#
# class UTransPosition(ctypes.Structure):
#     _fields_ = [
#         ('contextStart', int32_t),
#         ('contextLimit', int32_t),
#         ('start', int32_t),
#         ('limit', int32_t),
#     ]
#
#
#
#
# __all__ = (
#     'U_NO_THROW', 'UCONFIG_NO_BREAK_ITERATION', 'ULOC_KEYWORD_ITEM_SEPARATOR',
#     'U8_PREV_OR_FFFD', 'U16_GET_SUPPLEMENTARY', 'U_MASK', 'UBIDI_DEFAULT_LTR',
#     'UCNV_GET_MAX_BYTES_FOR_STRING', 'ULOC_ITALIAN', 'UDAT_MINUTE', 'U_CFUNC',
#     '__uint8_t', 'UDAT_HOUR', 'U_SHAPE_YEHHAMZA_TWOCELL_NEAR', 'U_GC_LO_MASK',
#     'UBIDI_MAX_EXPLICIT_LEVEL', 'U_SHAPE_TEXT_DIRECTION_VISUAL_LTR', 'U8_GET',
#     'UTEXT_GETNATIVEINDEX', 'UDAT_ABBR_MONTH_DAY', 'U_INT64_MAX', 'U8_APPEND',
#     'U_HAVE_DEBUG_LOCATION_NEW', 'U8_NEXT_OR_FFFD', 'U_INTERNAL', 'U_IMPORT',
#     'USTRINGTRIE_HAS_NEXT', 'U_ICUDATA_TYPE_LITLETTER', 'U_IS_SUPPLEMENTARY',
#     'U_SHAPE_SEEN_TWOCELL_NEAR', 'U16_IS_SURROGATE', 'U_GC_ZP_MASK', 'U_CAPI',
#     '__has_extension', 'ULOC_KEYWORD_ASSIGN', 'U_LAYOUT_API', 'U16_IS_LEAD',
#     'U8_SET_CP_LIMIT', 'UCNV_MAX_CONVERTER_NAME_LENGTH', 'UBIDI_MAP_NOWHERE',
#     'U_CPLUSPLUS_VERSION', 'U_HIDE_DRAFT_API', 'U8_SET_CP_START', 'U8_FWD_1',
#     'U_IS_SURROGATE_TRAIL', 'U_IS_TRAIL', 'U16_NEXT_UNSAFE', 'U16_IS_TRAIL',
#     'U_IS_SURROGATE_LEAD', 'U_SHAPE_SPACES_RELATIVE_TO_TEXT_BEGIN_END',
#     'U_OBSOLETE', 'U_SHAPE_LETTERS_SHAPE_TASHKEEL_ISOLATED', 'U16_APPEND',
#     'U_IS_UNICODE_NONCHAR', 'U_GC_S_MASK', 'UTEXT_SETNATIVEINDEX', 'U16_PREV',
#     'U_GC_CO_MASK', 'U_SHAPE_PRESERVE_PRESENTATION_NOOP', 'U8_NEXT_UNSAFE',
#     'U_PF_UNKNOWN', 'U_ICUDATA_TYPE_LETTER', 'U_SHAPE_DIGITS_ALEN2AN_INIT_AL',
#     'UDAT_SECOND', 'U_PLATFORM_IS_LINUX_BASED', 'CONVERT_TO_STRING', 'UText',
#     'U16_IS_SURROGATE_TRAIL', 'U_GC_SC_MASK', 'UDAT_YEAR_ABBR_MONTH_DAY',
#     'UDAT_YEAR_MONTH_DAY', 'UCNV_ESCAPE_JAVA', 'U16_BACK_1', 'U_CDECL_BEGIN',
#     'U_PLATFORM_IMPLEMENTS_POSIX', 'U_SHAPE_TEXT_DIRECTION_LOGICAL', 'USet',
#     'UCASEMAP_OMIT_UNCHANGED_TEXT', 'U8_NEXT', 'U_COMPARE_IGNORE_CASE',
#     'UTEXT_PREVIOUS32', 'U_GCC_MAJOR_MINOR', 'U_SHAPE_TASHKEEL_BEGIN',
#     'U_ENABLE_DYLOAD', 'U8_MASK_LEAD_BYTE', 'U_SHAPE_LENGTH_MASK', 'U16_GET',
#     'U_GC_CC_MASK', 'U_ICU_DATA_KEY', 'U_IS_LEAD', 'U8_PREV_UNSAFE', 'UIDNA',
#     'ULOC_KOREA', 'U16_SET_CP_START_UNSAFE', 'U_LIB_SUFFIX_C_NAME_STRING',
#     'UCNV_ESCAPE_XML_DEC', 'ULOC_GERMANY', 'ULOC_UK', 'U_MILLIS_PER_MINUTE',
#     'UCNV_OPTION_SEP_STRING', 'U8_COUNT_TRAIL_BYTES_UNSAFE', 'UDAT_YEAR',
#     'U_SHAPE_LETTERS_NOOP', 'U_GC_NL_MASK', 'ULOC_US', 'INT32_MIN', 'UCNV_SO',
#     'U_SHAPE_DIGIT_TYPE_MASK', 'U_EXPORT2', 'U_SHAPE_LENGTH_GROW_SHRINK',
#     'UDAT_NUM_MONTH_DAY', 'U_PF_QNX', 'U_COPYRIGHT_STRING_LENGTH', 'U8_FWD_N',
#     'ULOC_KEYWORD_SEPARATOR_UNICODE', 'UDAT_NUM_MONTH_WEEKDAY_DAY', 'UCNV_SI',
#     'UDAT_ABBR_QUARTER', 'U8_BACK_N', 'U_LAYOUTEX_API', 'U_PF_MINGW', 'UBiDi',
#     'U_SHAPE_AGGREGATE_TASHKEEL', 'U_ALLOC_SIZE_ATTR2', 'U_PF_OS390', 'UBool',
#     'U_PF_LINUX', 'U_TOOLUTIL_API', 'UCAL_UNKNOWN_ZONE_ID', 'U_HAVE_RBNF',
#     'U16_SET_CP_LIMIT', 'U_SIZEOF_UCHAR', 'U16_IS_SURROGATE_LEAD', 'U_PF_AIX',
#     'ULOC_TAIWAN', 'UDAT_HOUR24_MINUTE', 'U_IOSTREAM_SOURCE', 'U_SENTINEL',
#     'U_ICUDATA_NAME', 'U_SHAPE_TAIL_NEW_UNICODE', 'U8_FWD_N_UNSAFE', 'size_t',
#     'U_HIDE_OBSOLETE_API', 'UDAT_ABBR_GENERIC_TZ', 'U_GC_LU_MASK', 'ULOC_PRC',
#     'U_GC_M_MASK', 'ULOC_CHINA', 'UINT8_MAX', 'U_MILLIS_PER_SECOND', 'offset',
#     'U_DEPRECATED', 'UDAT_GENERIC_TZ', 'UMSGPAT_NO_NUMERIC_VALUE', 'U_IS_BMP',
#     'UCNV_ESCAPE_XML_HEX', 'U_CDECL_END', 'U8_GET_UNSAFE', 'U16_GET_UNSAFE',
#     'UDAT_NUM_MONTH', 'U_SHAPE_TASHKEEL_END', 'U_STRING_INIT', 'U_GC_PF_MASK',
#     'U_SHAPE_TEXT_DIRECTION_VISUAL_RTL', 'U_SHAPE_DIGIT_TYPE_AN_EXTENDED',
#     'U_DEFAULT_SHOW_DRAFT', 'UDAT_ABBR_UTC_TZ', 'U_GET_GC_MASK', 'U_EXPORT',
#     'U16_APPEND_UNSAFE', 'U_ASCII_FAMILY', 'UBIDI_KEEP_BASE_COMBINING',
#     'U_MALLOC_ATTR', 'UCONFIG_NO_NORMALIZATION', 'U_SHAPE_LAMALEF_BEGIN',
#     'UDAT_MINUTE_SECOND', 'U16_IS_SINGLE', 'U8_SET_CP_START_UNSAFE', 'UDate',
#     'ULOC_KEYWORDS_CAPACITY', 'U_GC_PC_MASK', 'UCLN_NO_AUTO_CLEANUP',
#     'U_CHECK_DYLOAD', 'U_STANDARD_CPP_NAMESPACE', 'U_HIDE_INTERNAL_API',
#     'ULOC_LANG_CAPACITY', 'U8_GET_OR_FFFD', 'U_GC_SK_MASK', 'U_GC_PE_MASK',
#     'U_PF_WINDOWS', 'U_SHAPE_TASHKEEL_MASK', 'U_HAVE_RVALUE_REFERENCES',
#     'U_IS_BIG_ENDIAN', 'U8_IS_TRAIL', 'UBIDI_REMOVE_BIDI_CONTROLS', 'INT64_C',
#     'U_SHAPE_TASHKEEL_RESIZE', 'UDAT_HOUR_MINUTE', '__has_feature', 'U8_PREV',
#     'U_DISABLE_RENAMING', 'ULOC_CANADA_FRENCH', 'U8_IS_SINGLE', 'UINT64_C',
#     'U_OVERRIDE', 'U16_BACK_1_UNSAFE', 'UMSGPAT_ARG_TYPE_HAS_PLURAL_STYLE',
#     'UCNV_ESCAPE_CSS2', 'INT8_MIN', 'U8_COUNT_TRAIL_BYTES', 'U_PF_IPHONE',
#     'U8_APPEND_UNSAFE', 'U_SHAPE_DIGIT_TYPE_RESERVED', '__has_attribute',
#     'U_DATE_MIN', 'UDAT_YEAR_NUM_MONTH_WEEKDAY_DAY', '__has_warning',
#     'U_HAVE_INTTYPES_H', 'ULOC_CANADA', 'UDAT_YEAR_ABBR_MONTH', 'U_PF_DARWIN',
#     'U_GC_ME_MASK', 'INT32_MAX', 'UCHAR_MAX_VALUE', 'USTRINGTRIE_MATCHES',
#     'U_SHAPE_DIGITS_MASK', 'U_SHAPE_LAMALEF_RESIZE', 'U16_TRAIL', 'U16_NEXT',
#     'U_MAX_VERSION_STRING_LENGTH', 'U8_BACK_N_UNSAFE', 'ULOC_CHINESE',
#     'U_GC_MN_MASK', 'U16_BACK_N', 'U8_FWD_1_UNSAFE', 'UCOL_NULLORDER',
#     'UCNV_MAX_FULL_FILE_NAME_LENGTH', 'USPREP_DEFAULT', 'U_IS_SURROGATE',
#     'U_SHAPE_DIGITS_EN2AN', 'U_HAVE_PLACEMENT_NEW', 'U_GC_PI_MASK', 'U_DEBUG',
#     'UCONFIG_NO_TRANSLITERATION', 'U_HAVE_STDINT_H', 'U_FALLTHROUGH',
#     'UDAT_YEAR_NUM_MONTH_DAY', 'UDAT_YEAR_MONTH_WEEKDAY_DAY', '__has_builtin',
#     'USTRINGTRIE_HAS_VALUE', 'U_MILLIS_PER_HOUR', '__has_cpp_attribute',
#     'U_GC_PS_MASK', 'UCONFIG_NO_LEGACY_CONVERSION', 'U_FAILURE', 'U16_FWD_1',
#     'U_SHAPE_LENGTH_FIXED_SPACES_NEAR', 'U_EBCDIC_FAMILY', 'U_STABLE',
#     'U_HAVE_LIB_SUFFIX', 'ULOC_FULLNAME_CAPACITY', 'U_HAVE_WCSCPY', 'U_DRAFT',
#     'UCONFIG_NO_REGULAR_EXPRESSIONS', 'UCNV_SWAP_LFNL_OPTION_STRING',
#     'U_TITLECASE_NO_BREAK_ADJUSTMENT', 'U16_MAX_LENGTH', 'UCONFIG_NO_SERVICE',
#     'U_GC_NO_MASK', 'UCHAR_TYPE', 'U16_SET_CP_LIMIT_UNSAFE', 'U_PF_HPUX',
#     'U_SHOW_CPLUSPLUS_API', 'U_PF_ANDROID', 'U_COMPARE_CODE_POINT_ORDER',
#     'UCNV_VALUE_SEP_CHAR', 'ULOC_FRENCH', 'U_IO_API', 'U_DECLARE_UTF16',
#     'UDAT_ABBR_MONTH_WEEKDAY_DAY', 'U8_MAX_LENGTH', 'U16_FWD_N', 'U_DATE_MAX',
#     'U_GC_PD_MASK', 'U_MAX_VERSION_LENGTH', 'U8_LENGTH', 'U_GC_SM_MASK',
#     'U_ICU_VERSION_BUNDLE', 'U_PF_BSD', 'UTEXT_NEXT32', 'UDAT_YEAR_MONTH',
#     'UDAT_LOCATION_TZ', 'U_SHAPE_TASHKEEL_REPLACE_BY_TATWEEL', 'UBRK_DONE',
#     'U16_SET_CP_START', 'U8_BACK_1_UNSAFE', 'UCONFIG_HAVE_PARSEALLINPUT',
#     'U_UINT64_MAX', 'U_HAVE_WCHAR_H', 'U_SHAPE_DIGITS_NOOP', 'UINT32_MAX',
#     'UDAT_YEAR_ABBR_MONTH_WEEKDAY_DAY', 'U_GC_C_MASK', 'U_GC_L_MASK',
#     'U_PLATFORM_IS_DARWIN_BASED', 'ULOC_KEYWORD_SEPARATOR', 'U_GC_CF_MASK',
#     'UDAT_YEAR_NUM_MONTH', 'UDAT_HOUR24_MINUTE_SECOND', 'U_VERSION_DELIMITER',
#     'UCONFIG_NO_FILTERED_BREAK_ITERATION', 'U_CALLCONV', 'INT16_MIN',
#     'UIDNA_INFO_INITIALIZER', 'U8_SET_CP_LIMIT_UNSAFE', 'U_NOEXCEPT',
#     'ULOC_KEYWORD_ITEM_SEPARATOR_UNICODE', 'UCNV_ESCAPE_ICU', 'UCNV_ESCAPE_C',
#     'UDAT_SPECIFIC_TZ', 'U_SHAPE_AGGREGATE_TASHKEEL_NOOP', 'U16_LEAD',
#     'UCNV_SUB_STOP_ON_ILLEGAL', 'U_SHAPE_LAMALEF_NEAR', 'U16_FWD_1_UNSAFE',
#     'UBIDI_OUTPUT_REVERSE', 'UBIDI_LEVEL_OVERRIDE', 'U_SHAPE_LETTERS_SHAPE',
#     'U_PLATFORM_HAS_WIN32_API', 'U8_BACK_1', 'UINT16_MAX', 'U_SUCCESS',
#     'UDAT_HOUR_MINUTE_SECOND', 'UBIDI_DEFAULT_RTL', 'U_SHAPE_YEHHAMZA_MASK',
#     'U_SHAPE_LENGTH_FIXED_SPACES_AT_BEGINNING', 'UCNV_LOCALE_OPTION_STRING',
#     'U_OVERRIDE_CXX_ALLOCATION', 'ULOC_FRANCE', 'ULOC_ENGLISH', 'ULOC_GERMAN',
#     'U_GC_LC_MASK', 'UDAT_YEAR_ABBR_QUARTER', 'USEARCH_DONE', 'U_COMMON_API',
#     'U16_FWD_N_UNSAFE', 'U_SHAPE_LAMALEF_END', 'ULOC_COUNTRY_CAPACITY',
#     'U_SHAPE_LETTERS_UNSHAPE', 'U_NO_NUMERIC_VALUE', 'UCONFIG_NO_IDNA',
#     'U_SHAPE_SPACES_RELATIVE_TO_TEXT_MASK', 'U_GC_SO_MASK', 'U_GC_P_MASK',
#     'UCONFIG_FORMAT_FASTPATHS_49', 'U_SIZEOF_WCHAR_T', 'U_PF_OS400', 'int8_t',
#     'UTEXT_INITIALIZER', 'U_ICUDATA_ENTRY_POINT', 'UCNV_VALUE_SEP_STRING',
#     'U_SHAPE_AGGREGATE_TASHKEEL_MASK', 'UCNV_ESCAPE_UNICODE', 'UDAT_HOUR24',
#     'UCONFIG_NO_COLLATION', 'U_GC_Z_MASK', 'U_IS_UNICODE_CHAR', 'U_INT64_MIN',
#     'U_SHAPE_TAIL_TYPE_MASK', 'U_HAVE_STD_STRING', 'U16_PREV_UNSAFE',
#     'INT8_MAX', 'UCNV_VERSION_OPTION_STRING', 'U_GC_CS_MASK', 'ULOC_ITALY',
#     'UDAT_DAY', 'U8_IS_LEAD', 'U_SHAPE_SEEN_MASK', 'U16_LENGTH', 'U_DATA_API',
#     'ULOC_KEYWORD_AND_VALUES_CAPACITY', 'U_GC_ZS_MASK', 'ULOC_KOREAN',
#     'ULOC_KEYWORD_ASSIGN_UNICODE', 'U_GC_LM_MASK', 'U16_SURROGATE_OFFSET',
#     'U_MILLIS_PER_DAY', 'UCNV_SKIP_STOP_ON_ILLEGAL', 'U_UNICODE_VERSION',
#     'U_NO_DEFAULT_INCLUDE_UTF_HEADERS', 'U_SHAPE_PRESERVE_PRESENTATION',
#     'U_STRING_DECL', 'U_GC_LT_MASK', 'UDAT_QUARTER', 'U_SHAPE_LAMALEF_AUTO',
#     'U_FOLD_CASE_EXCLUDE_SPECIAL_I', 'U_CHARSET_FAMILY', 'UCONFIG_NO_FILE_IO',
#     'UBIDI_INSERT_LRM_FOR_NUMERIC', 'UBIDI_DO_MIRRORING', 'UDAT_ABBR_MONTH',
#     'U_SHAPE_LAMALEF_MASK', 'U_SHAPE_DIGIT_TYPE_AN', 'UCNV_OPTION_SEP_CHAR',
#     'UDAT_ABBR_WEEKDAY', 'U_HAVE_CHAR16_T', 'U_FOLD_CASE_DEFAULT', 'U_FINAL',
#     'ULOC_JAPANESE', 'U_SHAPE_DIGITS_RESERVED', 'U_PF_CYGWIN', 'UDAT_MONTH',
#     'UCONFIG_NO_FORMATTING', 'UCONFIG_ONLY_HTML_CONVERSION', 'U_GC_PO_MASK',
#     'USPREP_ALLOW_UNASSIGNED', 'U_ENABLE_TRACING', 'UCONFIG_ONLY_COLLATION',
#     'U_ATTRIBUTE_DEPRECATED', 'U_SHAPE_PRESERVE_PRESENTATION_MASK', 'UGender',
#     'U_TITLECASE_NO_LOWERCASE', 'ULOC_SCRIPT_CAPACITY', 'UNORM_INPUT_IS_FCD',
#     'U_HIDE_DEPRECATED_API', 'U_ALLOC_SIZE_ATTR', 'U_GC_ND_MASK', 'U_PF_IRIX',
#     'U_SHAPE_TEXT_DIRECTION_MASK', 'U16_BACK_N_UNSAFE', 'UDAT_WEEKDAY',
#     'UCONFIG_MSGPAT_DEFAULT_APOSTROPHE_MODE', 'U_GC_LL_MASK', 'U_GC_N_MASK',
#     'ULOC_SIMPLIFIED_CHINESE', 'UDAT_YEAR_QUARTER', 'UCHAR_MIN_VALUE',
#     'NUMSYS_NAME_CAPACITY', 'U_GC_ZL_MASK', 'UCONFIG_ENABLE_PLUGINS',
#     'CANITER_SKIP_ZEROES', 'U_PLATFORM', 'UPLRULES_NO_UNIQUE_VALUE',
#     'U_CHARSET_IS_UTF8', 'ULOC_TRADITIONAL_CHINESE', 'U_SHAPE_DIGITS_AN2EN',
#     'U_I18N_API', 'UITER_NO_STATE', 'U_SHAPE_LENGTH_FIXED_SPACES_AT_END',
#     'ULOC_JAPAN', 'UDAT_ABBR_SPECIFIC_TZ', 'U_PF_BROWSER_NATIVE_CLIENT',
#     'UCONFIG_NO_CONVERSION', 'U_PLATFORM_USES_ONLY_WIN32_API', 'INT16_MAX',
#     'UDAT_MONTH_WEEKDAY_DAY', 'U_SHAPE_LETTERS_MASK', 'U_GC_CN_MASK',
#     'U_GC_MC_MASK', 'U_SHAPE_DIGITS_ALEN2AN_INIT_LR', 'UDAT_MONTH_DAY',
#     'U_PF_SOLARIS', 'USystemTimeZoneType', 'UDateDirection', 'UJoiningType',
#     'UPropertyNameChoice', 'UProperty', 'UConverterCallbackReason', 'USearch',
#     'UCalendarDateFields', 'UBreakIteratorType', 'ULocDataLocaleType',
#     'UNumberFormatRoundingMode', 'UScriptUsage', 'ULayoutType', 'URegionType',
#     'UDateAbsoluteUnit', 'ULineBreakTag', 'UCalendarWallTimeOption',
#     'UCalendarMonths', 'ULocaleDataDelimiterType', 'UWordBreak', 'UResType',
#     'UConverterType', 'UMessagePatternPartType', 'UTimeZoneFormatStyle',
#     'UColAttribute', 'UMeasurementSystem', 'UColBoundMode', 'UCurrencyUsage',
#     'UColAttributeValue', 'UDisplayContextType', 'UNumberFormatTextAttribute',
#     'UHangulSyllableType', 'UDialectHandling', 'UDateTimePatternConflict',
#     'UTimeZoneTransitionType', 'UTraceFunctionNumber', 'UMeasureFormatWidth',
#     'UDateRelativeDateTimeFormatterStyle', 'UCalendarDaysOfWeek', 'UIDNAInfo',
#     'UNormalizationMode', 'UCalendarType', 'UNumberFormatAttribute',
#     'UCalendarWeekdayType', 'USentenceBreakTag', 'UBiDiReorderingMode',
#     'UDateFormatBooleanAttribute', 'UCharCategory', 'UTimeZoneFormatTimeType',
#     'UFormattableType', 'UTimeScaleValue', 'UWordBreakValues', 'ULineBreak',
#     'UTransDirection', 'UCharIteratorOrigin', 'UCollationResult', 'UCaseMap',
#     'UDateRelativeUnit', 'UNumberCompactStyle', 'USetSpanCondition',
#     'UTimeZoneNameType', 'UConverterUnicodeSet', 'UNumberFormatSymbol',
#     'UTimeZoneFormatParseOption', 'UDateTimePatternMatchOptions', 'UCollator',
#     'UCharNameChoice', 'UNumberFormatFields', 'UColRuleOption', 'URegexpFlag',
#     'UNumberFormatPadPosition', 'UNumberFormatStyle', 'USearchAttributeValue',
#     'UCalendarLimitType', 'ULocaleDataExemplarSetType', 'UPluralType',
#     'USpoofChecks', 'UAlphabeticIndexLabelType', 'USentenceBreak', 'URegion',
#     'UDecompositionType', 'UGraphemeClusterBreak', 'UBiDiReorderingOption',
#     'UTraceLevel', 'UEastAsianWidth', 'UMessagePatternArgType', 'UErrorCode',
#     'UCurrCurrencyType', 'UDateFormatSymbolType', 'UCurrencySpacing',
#     'USearchAttribute', 'UDisplayContext', 'UMessagePatternApostropheMode',
#     'UCalendarAttribute', 'UCalendarDisplayNameType', 'UDateFormatStyle',
#     'UScriptCode', 'UDateFormatField', 'UNumericType', 'UConverterPlatform',
#     'UJoiningGroup', 'UBidiPairedBracketType', 'UDateTimePatternField',
#     'UCalendarAMPMs', 'UCurrNameStyle', 'UDateTimeScale', 'UBlockCode',
#     'UCharDirection', 'UStringTrieResult', 'UNormalizationCheckResult',
#     'UBiDiDirection', 'URelativeDateTimeUnit', 'UNormalization2Mode',
#     'UAcceptResult', 'UTimeZoneFormatGMTOffsetPatternType', 'UPluralRules',
#     'UStringPrepProfileType', 'UStringTrieBuildOption', 'U_PARSE_CONTEXT_LEN',
#     'UNumberFormatAttributeValue', 'UCharsetMatch', 'UEnumeration', 'int32_t',
#     'UConverter', 'UListFormatter', 'UCharIterator', 'UDateFormatSymbols',
#     'URelativeDateTimeFormatter', 'UCharsetDetector', 'UHashtable', 'uint8_t',
#     'UNormalizer2', 'URegularExpression', 'UDateIntervalFormat', 'UTextFuncs',
#     'ULocaleData', 'UGenderInfo', 'UResourceBundle', 'UNumberingSystem',
#     'UStringSearch', 'USpoofChecker', 'UTransPosition', 'UConverterSelector',
#     'UParseError', 'USerializedSet', 'UReplaceableCallbacks', 'UBiDiLevel',
#     'UConverterToUnicodeArgs', 'UFieldPositionIterator', 'UCollationElements',
#     'ULocaleDisplayNames', 'UStringPrepProfile', 'UFieldPosition', 'uint32_t',
#     'UConverterFromUnicodeArgs', 'UCalendar', 'UDateTimePatternGenerator',
#     'UReplaceable', 'UMessageFormat', 'UTransliterator', 'UFormattable',
#     'UCurrRegistryKey', 'uint16_t', 'URegistryKey', 'short16_t', 'UClassID',
#     'UDateFormat', 'UVersionInfo[U_MAX_VERSION_LENGTH]', 'UNumberFormat',
#     'UChar32', 'UCollationStrength', 'context', 'u_nl_catd',
# )
