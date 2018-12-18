import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_INC_VADEFS = None
_W64 = None
_UINTPTR_T_DEFINED = None
_VA_LIST_DEFINED = None
_M_ARM_NT = None
_M_CEE = None



# * vadefs.h - defines helper macros for stdarg.h  Copyright (c) Microsoft
# Corporation. All rights reserved. Purpose: This is a helper file for
# stdarg.h [Public] *
if _MSC_VER > 1000:
    pass
# END IF


if not defined(_INC_VADEFS):
    # DEFINE ERROR:    #define _INC_VADEFS
    if not defined(_WIN32):
        pass
    # END IF


        # /* Currently, all MS C compilers for Win32 platforms default to 8
        # byte alignment.
    if defined(_MSC_VER):
        _CRT_PACKING = 8
    # END IF  _MSC_VER

    # /* Enable mismatch checks if not being included in MIDL/RC
    # (and not explicitly disabled)
    if not defined NO_MIXED_CRT_CHECKS and not defined(__midl) and not defined(RC_INVOKED):
        def _PRAGMA_DETECT_MISMATCH_STRING1(s):
            return #s
        

        def _PRAGMA_DETECT_MISMATCH_STRING0(s):
            return _PRAGMA_DETECT_MISMATCH_STRING1s
        

        def _PRAGMA_DETECT_MISMATCH(name, value):
            return (
                __pragma(,
                    (comment(linker,
                    "/FAILIFMISMATCH:\"" _PRAGMA_DETECT_MISMATCH_STRING0name "=" _PRAGMA_DETECT_MISMATCH_STRING0value "\"")
                ))
            )
    else:
        def _PRAGMA_DETECT_MISMATCH(name, value):
        # DEFINE ERROR:         #define _PRAGMA_DETECT_MISMATCH(name, value)
            pass
    # END IF  NO_MIXED_CRT_CHECKS ...

    if defined(__cplusplus):
        pass
    # END IF


    from specstrings_h import * # NOQA
    if not defined(_W64):
        if not defined(__midl) and (defined(_X86_) or defined(_M_IX86) or defined(_ARM_) or defined(_M_ARM)) and _MSC_VER >= 1300:
            _W64 = __w64
        else:
            # DEFINE ERROR:            #define _W64        # END IF  not defined(__midl) and (defined(_X86_) or defined(_M_IX86) or defined(_ARM_) or defined(_M_ARM)) and _MSC_VER >= 1300
    # END IF  not defined (_W64)

    if not defined(_UINTPTR_T_DEFINED):
        if defined(_WIN64):
            INT64    uintptr_t = UINT
        else:
            UINT   uintptr_t = _W64
        # END IF

        # DEFINE ERROR:        #define _UINTPTR_T_DEFINED    # END IF
    if not defined(_VA_LIST_DEFINED):
        if defined(_M_CEE_PURE):
            va_list = System::ArgIterator
        else:
            # typedef _Writable_bytes_(_Inexpressible_("length varies")) CHAR *  va_list;
            varies" = _Inexpressible_("length(
                _Writable_bytes_,
            )
        # END IF  _M_CEE_PURE
        # DEFINE ERROR:        #define _VA_LIST_DEFINED    # END IF
    if defined(__cplusplus):
        def _ADDRESSOF(v):
            return & reinterpret_cast<const CHAR & >v
    else:
        def _ADDRESSOF(v):
            return & v
    # END IF


    if (defined(_M_ARM_NT) or defined(_M_HYBRID_X86_ARM64)) and not defined(_M_CEE_PURE):
        _VA_ALIGN = 4
        

        def _SLOTSIZEOF(t):
        # DEFINE ERROR:         #define _SLOTSIZEOF(t)   ( ((ctypes.sizeof(t) + _VA_ALIGN - 1) & ~(_VA_ALIGN - 1) )
            pass
        def _APALIGN(t, ap):
            return ((va_list0 - ap) & (__alignoft - 1))
    elif defined(_M_ARM64) and not defined(_M_CEE_PURE):
        _VA_ALIGN = 8
        

        def _SLOTSIZEOF(t):
        # DEFINE ERROR:         #define _SLOTSIZEOF(t)  ( ((ctypes.sizeof(t) + _VA_ALIGN - 1) & ~(_VA_ALIGN - 1) )
            pass
        def _APALIGN(t, ap):
            return ((va_list0 - ap) & (__alignoft - 1))
    else:
        def _SLOTSIZEOF(t):
        # DEFINE ERROR:         #define _SLOTSIZEOF(t)   ((ctypes.sizeof(t))
            pass
        def _APALIGN(t, ap):
            return __alignoft
    # END IF
    if defined(_M_CEE_PURE) or (defined(_M_CEE) and not defined(_M_ARM_NT) and not defined(_M_ARM64)):
        def _crt_va_start(ap, v):
            return (
                (,
                    (__va_start( & ap,
                    _ADDRESSOFv,
                    _SLOTSIZEOFv,
                    __alignofv,
                    _ADDRESSOFv)
                ))
            )
        

        def _crt_va_arg(ap, t):
            return (*t *__va_arg( & ap, _SLOTSIZEOFt, _APALIGNt,ap, t *0))
        

        def _crt_va_end(ap):
            return (__va_end( & ap))
    elif defined(_M_IX86) and not defined(_M_HYBRID_X86_ARM64):
        def _INTSIZEOF(n):
        # DEFINE ERROR:         #define _INTSIZEOF(n)   ( ((ctypes.sizeof(n) + (ctypes.sizeof(INT)- 1) & ~((ctypes.sizeof(INT)- 1) )
            pass
        def _crt_va_start(ap, v):
            return ap = va_list_ADDRESSOFv + _INTSIZEOFv
        def _crt_va_arg(ap, t):
            return (*t *((ap + = _INTSIZEOFt) - _INTSIZEOFt))
        def _crt_va_end(ap):
            return ap = va_list0
    elif defined(_M_ARM_NT):
        if defined(__cplusplus):
            def _crt_va_start(ap, v):
                return (
                    (,
                        (__va_start( & ap,
                        _ADDRESSOFv,
                        _SLOTSIZEOFv,
                        _ADDRESSOFv)
                    ))
                )
        else:
            def _crt_va_start(ap, v):
                return ap = va_list_ADDRESSOFv + _SLOTSIZEOFv
        # END IF


        def _crt_va_arg(ap, t):
            return (*t *((ap + = _SLOTSIZEOFt+ _APALIGNt,ap) -_SLOTSIZEOFt))
        

        def _crt_va_end(ap):
            return ap = va_list0
    elif defined _M_HYBRID_X86_ARM64:
        def _crt_va_start(ap, v):
            return (
                (,
                    (VOID(__va_start( & ap,
                    _ADDRESSOFv,
                    _SLOTSIZEOFv,
                    __alignofv,
                    _ADDRESSOFv)
                )))
            )
        

        def _crt_va_arg(ap, t):
            return (*t*((ap + = _SLOTSIZEOFt) - _SLOTSIZEOFt))
        

        def _crt_va_end(ap):
            return VOID(ap = va_list0)
    elif defined(_M_ARM64):
        def _crt_va_start(ap, v):
            return (
                (,
                    (__va_start( & ap,
                    _ADDRESSOFv,
                    _SLOTSIZEOFv,
                    __alignofv,
                    _ADDRESSOFv)
                ))
            )
        

        def _crt_va_arg(ap, t):
        # DEFINE ERROR: #define _crt_va_arg(ap, t) ( ( (ctypes.sizeof(t) > ( 2*(ctypes.sizeof(INT64) ) ) ? **(t **)( ( ap  + = (ctypes.sizeof(INT64) ) - (ctypes.sizeof(INT64) ) : *(t *)((ap  + = _SLOTSIZEOF(t) + _APALIGN(t,ap)) - _SLOTSIZEOF(t) ) )
            pass
        def _crt_va_end(ap):
            return ap = va_list0
    elif defined(_M_AMD64):
        def _crt_va_start(ap, x):
            return (__va_start( & ap, x))
        

        def _crt_va_arg(ap, t):
        # DEFINE ERROR: #define _crt_va_arg(ap, t) ( ( (ctypes.sizeof(t) > (ctypes.sizeof(INT64) or ( (ctypes.sizeof(t) & ((ctypes.sizeof(t) - 1) ) != 0 ) ? **(t **)( ( ap  + = (ctypes.sizeof(INT64) ) - (ctypes.sizeof(INT64) ) :  *(t  *)( ( ap  + = (ctypes.sizeof(INT64) ) - (ctypes.sizeof(INT64) ) )
            pass
        def _crt_va_end(ap):
            return ap = va_list0
    else:
        # A guess at the proper definitions for other platforms
        def _INTSIZEOF(n):
        # DEFINE ERROR:         #define _INTSIZEOF(n)   ( ((ctypes.sizeof(n) + (ctypes.sizeof(INT)- 1) & ~((ctypes.sizeof(INT)- 1) )
            pass
        def _crt_va_start(ap, v):
            return ap = va_list_ADDRESSOFv + _INTSIZEOFv
        def _crt_va_arg(ap, t):
            return (*t *((ap + = _INTSIZEOFt) - _INTSIZEOFt))
        def _crt_va_end(ap):
            return ap = va_list0
    # END IF
    if defined(__cplusplus):
        pass
    # END IF


    if defined(_MSC_VER):
        pass
    # END IF  _MSC_VER
# END IF  _INC_VADEFS

# 88bf0570-3001-4e78-a5f2-be5765546192
