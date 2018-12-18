import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_CRTIMP = None
_DLL = None
_INC_CRTDEFS = None
_STR2WSTR = None
__FILEW__ = None
__FUNCTIONW__ = None
_CRT_NOFORCE_MANIFEST = None
_M_CEE = None
_STATIC_CPPLIB = None
_CRT_APPEND = None
_W64 = None
_CRTIMP_NOIA64 = None
_CRTIMP2 = None
_CRTIMP_ALT = None
_CRT_ALTERNATIVE_INLINES = None
_STATIC_MGDLIB = None
_MANAGED = None
_MRTIMP = None
_MRTIMP2 = None
_MCRTIMP = None
__clrcall = None
_CRTDATA = None
_CRTIMP2_PURE = None
__cplusplus_cli = None
__STDC_WANT_SECURE_LIB__ = None
_CRT_SECURE_NO_WARNINGS = None
_CRT_SECURE_FORCE_DEPRECATE_CORE = None
_CRT_INSECURE_DEPRECATE_CORE = None
_CRT_SECURE_NO_DEPRECATE_CORE = None
_CRT_SECURE_FORCE_DEPRECATE = None
_CRT_SECURE_NO_DEPRECATE = None
_CRT_INSECURE_DEPRECATE = None
_CRT_SECURE_DEPRECATE_MEMORY = None
_CRT_SECURE_WARNINGS_MEMORY = None
_CRT_INSECURE_DEPRECATE_MEMORY = None
_CRT_SECURE_NO_DEPRECATE_GLOBALS = None
_CRT_SECURE_NO_WARNINGS_GLOBALS = None
_CRT_INSECURE_DEPRECATE_GLOBALS = None
_CRT_MANAGED_HEAP_NO_DEPRECATE = None
_CRT_MANAGED_HEAP_NO_WARNINGS = None
_CRT_MANAGED_HEAP_DEPRECATE = None
_CRT_OBSOLETE_NO_DEPRECATE = None
_CRT_OBSOLETE_NO_WARNINGS = None
_CRT_OBSOLETE = None
_CRT_JIT_INTRINSIC = None
_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES = None
_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT = None
_CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES = None
_CRT_NONSTDC_FORCE_DEPRECATE = None
_CRT_NONSTDC_NO_DEPRECATE = None
_CRT_NONSTDC_NO_WARNINGS = None
_CRT_NONSTDC_DEPRECATE = None
_POSIX_ = None
_SIZE_T_DEFINED = None
_RSIZE_T_DEFINED = None
_INTPTR_T_DEFINED = None
_UINTPTR_T_DEFINED = None
_PTRDIFF_T_DEFINED = None
_WCHAR_T_DEFINED = None
_VA_LIST_DEFINED = None
_ERRCODE_DEFINED = None
_USE_32BIT_TIME_T = None
UNALIGNED = None
_CRT_ALIGN = None
_MSC_VER_GREATER_THEN_13102050 = None
__cdecl = None
_TAGLC_ID_DEFINED = None
_THREADLOCALEINFO = None
_ARM64_ = None
_PREFAST_ = None
_PFT_SHOULD_CHECK_RETURN = None
_PFT_SHOULD_CHECK_RETURN_WAT = None
_NO_INLINING = None
_CRT_UNUSED = None
CRTDLL2 = None
_CRT_STDIO_IMP = None
_CRT_STDIO_IMP_ALT = None

class localeinfo_(ctypes.Structure):
    pass


_locale_tstruct = localeinfo_
_locale_t = POINTER(localeinfo_)


class tagLC_ID(ctypes.Structure):
    pass


LC_ID = tagLC_ID
LPLC_ID = POINTER(tagLC_ID)


class threadlocaleinfo(ctypes.Structure):
    pass


threadlocinfo = threadlocaleinfo




# * crtdefs.h - definitions/declarations common to all CRT  Copyright (c)
# Microsoft Corporation. All rights reserved. Purpose: This file has mostly
# defines used by the entire CRT. [Public] *
# Lack of pragma once is deliberate
# Define _CRTIMP
if not defined(_CRTIMP):
    if defined(_DLL):
        _CRTIMP = VOID
    else:
        _CRTIMP = VOID
    # END IF  _DLL
# END IF  _CRTIMP

if not defined(_INC_CRTDEFS):
    _INC_CRTDEFS = VOID

    # Define __FUNCTIONW__ and __FILEW__ if not already defined
    if not defined(_STR2WSTR):
        def __STR2WSTR(str):
            return L##str


        def _STR2WSTR(str):
            return __STR2WSTRstr
    # END IF


    if not defined(__FILEW__):
        __FILEW__ = _STR2WSTR(__FILE__)
    # END IF


    if not defined(__FUNCTIONW__):
        __FUNCTIONW__ = _STR2WSTR(__FUNCTION__)
    # END IF


    if defined (__midl):
        # MIDL does not want to see this stuff
        _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES = 0
        _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT = 0
        _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES = 0
    # END IF  defined (__midl)

    if not defined (_WIN32):
        pass
    # END IF  not defined (_WIN32)

    if not defined(_CRT_NOFORCE_MANIFEST):
        _CRT_NOFORCE_MANIFEST = VOID
    # END IF


    # Remove this once stdhpp\yvals.h integrates from VS
    if defined(_M_CEE) and not defined(_STATIC_CPPLIB):
        _STATIC_CPPLIB = VOID
    # END IF


    _CRTEXP = VOID
    from specstrings_h import * # NOQA
    if defined(_MSC_VER):
        _CRT_PACKING = 8
    # END IF  _MSC_VER

    from vadefs_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF  __cplusplus

    # preprocessor string helpers
    def __CRT_STRINGIZE(_Value):
        return #_Value


    def _CRT_STRINGIZE(_Value):
        return __CRT_STRINGIZE_Value


    def __CRT_WIDE(_String):
        return L(##(_String))


    def _CRT_WIDE(_String):
        return __CRT_WIDE_String
    if not defined(_CRT_APPEND):
        def __CRT_APPEND(_Value1, _Value2):
            return _Value1(##(_Value2))


        def _CRT_APPEND(_Value1, _Value2):
            return __CRT_APPEND_Value1, _Value2
    # END IF


    if not defined(_W64):
        if not defined(__midl) and (defined(_X86_) or defined(_M_IX86) or defined(_ARM_) or defined(_M_ARM)) and _MSC_VER >= 1300:
            _W64 = __w64
        else:
            _W64 = VOID
        # END IF  not defined(__midl) and (defined(_X86_) or defined(_M_IX86) or defined(_ARM_) or defined(_M_ARM)) and _MSC_VER >= 1300
    # END IF  not defined (_W64)

    # Define _CRTIMP_NOIA64
    if not defined(_CRTIMP_NOIA64):
        if defined (_M_IA64):
            _CRTIMP_NOIA64 = VOID
        else:
            _CRTIMP_NOIA64 = _CRTIMP
        # END IF  defined (_M_IA64)
    # END IF  _CRTIMP_NOIA64

    # Define _CRTIMP2
    if not defined(_CRTIMP2):
        if defined(_DLL) and not defined(_STATIC_CPPLIB):
            _CRTIMP2 = VOID
        else:
            _CRTIMP2 = VOID
        # END IF  defined (_DLL) and not defined (_STATIC_CPPLIB)
    # END IF  _CRTIMP2

    # Define _CRTIMP_ALT
    _CRT_ALTERNATIVE_INLINES = VOID
    if not defined(_CRTIMP_ALT):
        if defined(_DLL):
            if defined(_CRT_ALTERNATIVE_INLINES):
                _CRTIMP_ALT = VOID
            else:
                _CRTIMP_ALT = _CRTIMP
                _CRT_ALTERNATIVE_IMPORTED = VOID
            # END IF  _CRT_ALTERNATIVE_INLINES

        else:
            _CRTIMP_ALT = VOID
        # END IF  _DLL
    # END IF  _CRTIMP_ALT

    # /* defined(__cplusplus) is due to some code that sets MANAGED_CXX but
    # builds .c files. For example:
    # testsrc\basetest\kernel\ps\modm\*\_build_clr
    if defined(_STATIC_MGDLIB) and not defined(_MANAGED) and defined(__cplusplus):
        pass
    # END IF


    if defined(_M_CEE_PURE) and defined(_STATIC_MGDLIB):
        _STATIC_MGDLIB_PURE = VOID
    # END IF


    # Define _MRTIMP
    if not defined(_MRTIMP):
        if not defined(_STATIC_MGDLIB):
            _MRTIMP = VOID
        else:
            _MRTIMP = VOID
        # END IF

    # END IF


    # Define _MRTIMP2
    if not defined(_MRTIMP2):
        if defined(_DLL) and not defined(_STATIC_CPPLIB):
            _MRTIMP2 = VOID
        else:
            _MRTIMP2 = VOID
        # END IF  _DLL and not STATIC_CPPLIB
    # END IF  _MRTIMP2

    if not defined(_MCRTIMP):
        if defined(_DLL) and (not defined(_MANAGED) or not defined(_STATIC_MGDLIB)):
            _MCRTIMP = VOID
        else:
            _MCRTIMP = VOID
        # END IF  _DLL
    # END IF  _CRTIMP

    if (_MSC_VER < 1400) and (not defined(__clrcall)):
        __clrcall = __cdecl
    # END IF


    if defined (_M_CEE_PURE):
        __CLR_OR_THIS_CALL = __clrcall
        __CLRCALL_OR_CDECL = __clrcall
    else:
        __CLR_OR_THIS_CALL = VOID
        __CLRCALL_OR_CDECL = __cdecl
    # END IF


    if defined(_M_CEE_PURE) or (defined(_STATIC_CPPLIB) and not defined(_DLL)):
        _CRTIMP_PURE = VOID
        _CRTEXP_PURE = VOID
    else:
        _CRTIMP_PURE = _CRTIMP
        _CRTEXP_PURE = _CRTEXP
    # END IF


    # Define _MRTIMP2_NPURE
    if (defined(_DLL) and defined(_M_CEE_PURE)) and not defined(_STATIC_MGDLIB):
        _MRTIMP2_NPURE = VOID
    else:
        _MRTIMP2_NPURE = VOID
    # END IF  _DLL and not STATIC_CPPLIB

    if defined(_STATIC_MGDLIB) and defined(_M_CEE_PURE):
        _CRTIMP2_CALLING_CONVENTION = __clrcall
        _CRTIMP2_PURE_CALLING_CONVENTION = __clrcall
        _CRTIMP2_MEMBER_FUNCTION_CALLING_CONVENTION = VOID
        _CRTIMP2_PURE_MEMBER_FUNCTION_CALLING_CONVENTION = VOID
        _MRTIMP_CALLING_CONVENTION = __clrcall
        _MRTIMP2_CALLING_CONVENTION = __clrcall
        _MRTIMP2_NPURE_CALLING_CONVENTION = __clrcall
    else:
        _CRTIMP2_CALLING_CONVENTION = __cdecl
        _CRTIMP2_PURE_CALLING_CONVENTION = __cdecl
        _CRTIMP2_MEMBER_FUNCTION_CALLING_CONVENTION = VOID
        _CRTIMP2_PURE_MEMBER_FUNCTION_CALLING_CONVENTION = VOID
        _MRTIMP_CALLING_CONVENTION = __cdecl
        _MRTIMP2_CALLING_CONVENTION = __cdecl
        _MRTIMP2_NPURE_CALLING_CONVENTION = __cdecl
    # END IF


            # /* Always declare the data in a legal way. Sometimes it will be
            # accessed via imported functions, sometimes directly as declared
            # here.
    if not defined(_CRTDATA):
        if defined(_M_CEE_PURE):
            def _CRTDATA(x):
                return x
        else:
            def _CRTDATA(x):
                return _CRTIMP(x)
        # END IF  _M_CEE_PURE
    # END IF  _CRTDATA

    if not defined(_CRTIMP2_PURE):
        if defined(_M_CEE_PURE):
            _CRTIMP2_PURE = VOID
        else:
            _CRTIMP2_PURE = _CRTIMP2
        # END IF

    # END IF


    def _CRTIMP2_FUNCTION(type):
        return _CRTIMP2(type(_CRTIMP2_CALLING_CONVENTION))


    def _CRTIMP2_PURE_FUNCTION(type):
        return _CRTIMP2_PURE(type(_CRTIMP2_PURE_CALLING_CONVENTION))
    _CRTIMP2_PURE_CONSTRUCTOR = (
        _CRTIMP2_PURE(_CRTIMP2_MEMBER_FUNCTION_CALLING_CONVENTION)
    )
    _CRTIMP2_PURE_DESTRUCTOR = (
        _CRTIMP2_PURE(_CRTIMP2_MEMBER_FUNCTION_CALLING_CONVENTION)
    )


    def _CRTIMP2_MEMBER_FUNCTION(type):
        return _CRTIMP2(type(_CRTIMP2_MEMBER_FUNCTION_CALLING_CONVENTION))


    def _CRTIMP2_PURE_MEMBER_FUNCTION(type):
        return _CRTIMP2_PURE(type(_CRTIMP2_PURE_MEMBER_FUNCTION_CALLING_CONVENTION))


    def _MRTIMP_FUNCTION(type):
        return _MRTIMP(type(_MRTIMP_CALLING_CONVENTION))


    def _MRTIMP2_FUNCTION(type):
        return _MRTIMP2(type(_MRTIMP2_CALLING_CONVENTION))


    def _MRTIMP2_NPURE_FUNCTION(type):
        return _MRTIMP2_NPURE(type(_MRTIMP2_NPURE_CALLING_CONVENTION))
    if not defined(_MANAGED):
        def _MSVCR80_FUNCTION(type):
            return type(__cdecl)


        def _MSVCR80_FUNCTION_2(sal, type):
            return sal(type(__cdecl))
    elif not defined(_STATIC_MGDLIB):
        def _MSVCR80_FUNCTION(type):
            return _CRTIMP(type(__cdecl))


        def _MSVCR80_FUNCTION_2(sal, type):
            return _CRTIMP(sal(type(__cdecl)))
    else:
        def _MSVCR80_FUNCTION(type):
            return type(__ALTDECL)


        def _MSVCR80_FUNCTION_2(sal, type):
            return sal(type(__ALTDECL))
    # END IF


    if defined(_STATIC_MGDLIB) and defined(_M_CEE_PURE):
        _CRTIMP_TYPEINFO = VOID
    else:
        _CRTIMP_TYPEINFO = _CRTIMP
    # END IF


    if defined(_STATIC_MGDLIB) and defined(_M_CEE_PURE):
        _CRTIMP_PURE_TYPEINFO = VOID
    else:
        _CRTIMP_PURE_TYPEINFO = _CRTIMP_PURE
    # END IF


    if defined(_M_CEE):
        if defined(__cplusplus_cli):
            _PGLOBAL = VOID
        else:
            _PGLOBAL = VOID
        # END IF  defined (__cplusplus_cli)

    else:
        _PGLOBAL = VOID
    # END IF  _M_CEE

    if defined(_M_CEE) and (_MSC_VER >= 1400):
        _AGLOBAL = VOID
    else:
        _AGLOBAL = VOID
    # END IF  _M_CEE

    # define a specific constant for mixed mode
    if defined(_M_CEE):
        if not defined(_M_CEE_PURE):
            _M_CEE_MIXED = VOID
        # END IF  _M_CEE_PURE
    # END IF  _M_CEE

    # Define __STDC_SECURE_LIB__
    __STDC_SECURE_LIB__ = 200411L

    # Retain__GOT_SECURE_LIB__ for back-compat
    __GOT_SECURE_LIB__ = __STDC_SECURE_LIB__

    # Default value for __STDC_WANT_SECURE_LIB__ is 1
    if not defined(__STDC_WANT_SECURE_LIB__):
        __STDC_WANT_SECURE_LIB__ = 1
    # END IF  __STDC_WANT_SECURE_LIB__

    # Turn off warnings if __STDC_WANT_SECURE_LIB__ is 0
    if not __STDC_WANT_SECURE_LIB__ and not defined(_CRT_SECURE_NO_WARNINGS):
        _CRT_SECURE_NO_WARNINGS = VOID
    # END IF  not __STDC_WANT_SECURE_LIB__ and not defined (_CRT_SECURE_NO_WARNINGS)

    # See note on use of deprecate at the top of this file
    if _MSC_FULL_VER >= 140050320:
        def _CRT_DEPRECATE_TEXT(_Text):
            return _TEXT
    else:
        def _CRT_DEPRECATE_TEXT(_Text):
            return _Text
    # END IF  _MSC_FULL_VER >= 140050320

    if not defined(_CRT_SECURE_FORCE_DEPRECATE_CORE):
        _CRT_SECURE_NO_DEPRECATE_CORE = VOID
    # END IF


    # Define _CRT_INSECURE_DEPRECATE
    if not defined(_CRT_INSECURE_DEPRECATE_CORE):
        if defined(_CRT_SECURE_NO_DEPRECATE_CORE):
            _CRT_INSECURE_DEPRECATE_CORE = VOID
        else:
            pass
    # END IF

    # END IF


    if not defined(_CRT_SECURE_FORCE_DEPRECATE):
        _CRT_SECURE_NO_DEPRECATE = VOID
    # END IF


    # Define _CRT_INSECURE_DEPRECATE
    # See note on use of deprecate at the top of this file
    if defined(_CRT_SECURE_NO_DEPRECATE) and not defined(_CRT_SECURE_NO_WARNINGS):
        _CRT_SECURE_NO_WARNINGS = VOID
    # END IF


    if not defined(_CRT_INSECURE_DEPRECATE):
        if defined(_CRT_SECURE_NO_WARNINGS):
            _CRT_INSECURE_DEPRECATE = VOID
        else:
            pass
        # END IF  _CRT_SECURE_NO_DEPRECATE
    # END IF  _CRT_INSECURE_DEPRECATE

    # Define _CRT_INSECURE_DEPRECATE_MEMORY
    # See note on use of deprecate at the top of this file
    if defined(_CRT_SECURE_DEPRECATE_MEMORY) and not defined(_CRT_SECURE_WARNINGS_MEMORY):
        _CRT_SECURE_WARNINGS_MEMORY = VOID
    # END IF


    if not defined(_CRT_INSECURE_DEPRECATE_MEMORY):
        if not defined (_CRT_SECURE_WARNINGS_MEMORY):
            _CRT_INSECURE_DEPRECATE_MEMORY = VOID
        else:
            def _CRT_INSECURE_DEPRECATE_MEMORY(_Replacement):
                return _CRT_INSECURE_DEPRECATE(_Replacement)
        # END IF  not defined (_CRT_SECURE_DEPRECATE_MEMORY)
    # END IF  _CRT_INSECURE_DEPRECATE_MEMORY

    # Define _CRT_INSECURE_DEPRECATE_GLOBALS
    # See note on use of deprecate at the top of this file
    if not defined (RC_INVOKED):
        if defined(_CRT_SECURE_NO_DEPRECATE_GLOBALS) and not defined(_CRT_SECURE_NO_WARNINGS_GLOBALS):
            _CRT_SECURE_NO_WARNINGS_GLOBALS = VOID
        # END IF

    # END IF


    if not defined(_CRT_INSECURE_DEPRECATE_GLOBALS):
        if defined (RC_INVOKED):
            _CRT_INSECURE_DEPRECATE_GLOBALS = VOID
        else:
            if defined(_CRT_SECURE_NO_WARNINGS_GLOBALS):
                _CRT_INSECURE_DEPRECATE_GLOBALS = VOID
            else:
                def _CRT_INSECURE_DEPRECATE_GLOBALS(_Replacement):
                    return _CRT_INSECURE_DEPRECATE(_Replacement)
            # END IF  defined (_CRT_SECURE_NO_DEPRECATE_GLOBALS)
        # END IF  defined (RC_INVOKED)
    # END IF  _CRT_INSECURE_DEPRECATE_GLOBALS

    # Define _CRT_MANAGED_HEAP_DEPRECATE
    # See note on use of deprecate at the top of this file
    if defined(_CRT_MANAGED_HEAP_NO_DEPRECATE) and not defined(_CRT_MANAGED_HEAP_NO_WARNINGS):
        _CRT_MANAGED_HEAP_NO_WARNINGS = VOID
    # END IF


    if not defined(_CRT_MANAGED_HEAP_DEPRECATE):
        if defined(_CRT_MANAGED_HEAP_NO_WARNINGS):
            _CRT_MANAGED_HEAP_DEPRECATE = VOID
        else:
            if defined(_M_CEE):
                _CRT_MANAGED_HEAP_DEPRECATE = VOID

                # /* Disabled to allow QA tests to get fixed
                # _CRT_DEPRECATE_TEXT("Direct heap access is not safely possible from managed code.")
                #
            else:
                _CRT_MANAGED_HEAP_DEPRECATE = VOID
            # END IF  defined (_M_CEE)
        # END IF  _CRT_MANAGED_HEAP_NO_DEPRECATE
    # END IF  _CRT_MANAGED_HEAP_DEPRECATE

    # Change the __FILL_BUFFER_PATTERN to 0xFE to fix security function buffer
    # overrun detection bug
    _SECURECRT_FILL_BUFFER_PATTERN = 0xFE

    # obsolete stuff
    # Define _CRT_OBSOLETE
    # See note on use of deprecate at the top of this file
    if defined(_CRT_OBSOLETE_NO_DEPRECATE) and not defined(_CRT_OBSOLETE_NO_WARNINGS):
        _CRT_OBSOLETE_NO_WARNINGS = VOID
    # END IF


    if not defined(_CRT_OBSOLETE):
        if defined(_CRT_OBSOLETE_NO_WARNINGS):
            _CRT_OBSOLETE = VOID
        else:
            pass
        # END IF  _CRT_OBSOLETE_NO_WARNINGS
    # END IF  _CRT_OBSOLETE

    # jit64 instrinsic stuff
    if not defined(_CRT_JIT_INTRINSIC):
        if defined(_M_CEE) and (defined(_M_AMD64) or defined(_M_IA64)):
            # This is only needed when managed code is calling the native
            # APIs, targeting the 64-bit runtime
            _CRT_JIT_INTRINSIC = VOID
        else:
            _CRT_JIT_INTRINSIC = VOID
        # END IF  defined (_M_CEE) and (defined (_M_AMD64) or defined (_M_IA64))
    # END IF  _CRT_JIT_INTRINSIC

    # Define overload switches
    if not defined (RC_INVOKED):
        if not defined(_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES):
            _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES = 0
            if not __STDC_WANT_SECURE_LIB__ and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES:
                pass
            # END IF  not __STDC_WANT_SECURE_LIB__ and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES

        else:
            pass
        # END IF  not defined (_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES)
    # END IF  not defined (RC_INVOKED)

    if not defined (RC_INVOKED):
        if not defined(_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT):
            # _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT is ignored if
            # _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES is set to 0
            _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT = 0
            if not __STDC_WANT_SECURE_LIB__ and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT:
                pass
            # END IF  not __STDC_WANT_SECURE_LIB__ and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT

        else:
            pass
        # END IF  not defined (_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT)
    # END IF  not defined (RC_INVOKED)

    if not defined (RC_INVOKED):
        if not defined(_CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES):
            if __STDC_WANT_SECURE_LIB__:
                _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES = 1
            else:
                _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES = 0
            # END IF  __STDC_WANT_SECURE_LIB__

            if not __STDC_WANT_SECURE_LIB__ and _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES:
                pass
            # END IF  not __STDC_WANT_SECURE_LIB__ and _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES

        else:
            pass
        # END IF  not defined (_CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES)
    # END IF  not defined (RC_INVOKED)

    if not defined(_CRT_NONSTDC_FORCE_DEPRECATE):
        _CRT_NONSTDC_NO_DEPRECATE = VOID
    # END IF


    # Define _CRT_NONSTDC_DEPRECATE
    # See note on use of deprecate at the top of this file
    if defined(_CRT_NONSTDC_NO_DEPRECATE) and not defined(_CRT_NONSTDC_NO_WARNINGS):
        _CRT_NONSTDC_NO_WARNINGS = VOID
    # END IF


    if not defined(_CRT_NONSTDC_DEPRECATE):
        if defined(_CRT_NONSTDC_NO_WARNINGS) or defined(_POSIX_):
            _CRT_NONSTDC_DEPRECATE = VOID
        else:
            def _CRT_NONSTDC_DEPRECATE(_NewName):
                return _CRT_DEPRECATE_TEXT(_NewName)
        # END IF  defined (_CRT_NONSTDC_NO_DEPRECATE)
    # END IF  not defined (_CRT_NONSTDC_DEPRECATE)

    if not defined(_SIZE_T_DEFINED):
        if defined(_WIN64):
            size_t = INT64
        else:
            size_t = UINT
        # END IF
        _SIZE_T_DEFINED = VOID
    # END IF


    if __STDC_WANT_SECURE_LIB__:
        if not defined(_RSIZE_T_DEFINED):
            rsize_t = size_t
            _RSIZE_T_DEFINED = VOID
        # END IF

    # END IF


    if not defined(_INTPTR_T_DEFINED):
        if defined(_WIN64):
            intptr_t = INT64
        else:
            intptr_t = INT
        # END IF
        _INTPTR_T_DEFINED = VOID
    # END IF


    if not defined(_UINTPTR_T_DEFINED):
        if defined(_WIN64):
            uintptr_t = INT64
        else:
            uintptr_t = UINT
        # END IF
        _UINTPTR_T_DEFINED = VOID
    # END IF


    if not defined(_PTRDIFF_T_DEFINED):
        if defined(_WIN64):
            ptrdiff_t = INT64
        else:
            ptrdiff_t = INT
        # END IF

        _PTRDIFF_T_DEFINED = VOID
    # END IF


    if not defined(_WCHAR_T_DEFINED):
        wchar_t = USHORT
        _WCHAR_T_DEFINED = VOID
    # END IF  _WCHAR_T_DEFINED

    wint_t = USHORT
    wctype_t = USHORT
    _WCTYPE_T_DEFINED = VOID
    if not defined(_VA_LIST_DEFINED):
        if defined(_M_CEE_PURE):
            va_list = POINTER(CHAR)
        else:
            va_list = POINTER(CHAR)
        # END IF  _M_CEE_PURE
        _VA_LIST_DEFINED = VOID
    # END IF
    if not defined(_ERRCODE_DEFINED):
        _ERRCODE_DEFINED = VOID
        errcode = INT
        errno_t = INT
    # END IF


    # 32-bit time value
    __time32_t = LONG
    _TIME32_T_DEFINED = VOID

    # 64-bit time value
    __time64_t = LONGLONG
    _TIME64_T_DEFINED = VOID
    if not defined(_WIN64):
        _USE_32BIT_TIME_T = VOID
    # END IF


    if defined(_USE_32BIT_TIME_T):
        # time value
        time_t = LONG
    else:
        # time value
        time_t = LONGLONG
    # END IF


    _TIME_T_DEFINED = 1    # avoid multiple def's of time_t
    _NO_CPP_INLINES = VOID
    _CONST_RETURN = VOID

    # For backwards compatibility
    _WConst_return = _CONST_RETURN
    if not defined(UNALIGNED):
        if defined(_M_IA64) or defined(_M_AMD64) or defined(_M_ARM) or defined(_M_ARM64):
            UNALIGNED = VOID
        else:
            UNALIGNED = VOID
        # END IF  defined (_M_IA64) or defined (_M_AMD64) or defined (_M_ARM) or defined (_M_ARM64)
    # END IF  not defined (UNALIGNED)

    if not defined (_CRT_ALIGN):
        if defined (__midl):
            _CRT_ALIGN = VOID
        else:
            def _CRT_ALIGN(x):
                return x
        # END IF  defined (__midl)
    # END IF  not defined (_CRT_ALIGN)

    # Define _CRTNOALIAS, _CRTRESTRICT
    if _MSC_FULL_VER >= 13102050:
        if not defined(_MSC_VER_GREATER_THEN_13102050):
            _MSC_VER_GREATER_THEN_13102050 = VOID
        # END IF  not defined (_MSC_VER_GREATER_THEN_13102050)
    # END IF  _MSC_FULL_VER >= 13102050

    if (defined(_M_IA64) and defined(_MSC_VER_GREATER_THEN_13102050)) or _MSC_VER >= 1400:
        _CRTNOALIAS = VOID
        _CRTRESTRICT = VOID
    else:
        _CRTNOALIAS = VOID
        _CRTRESTRICT = VOID
    # END IF  ( defined(_M_IA64) and defined(_MSC_VER_GREATER_THEN_13102050) ) or _MSC_VER >= 1400

    # Define __cdecl for non-Microsoft compilers
    if (not defined(_MSC_VER) and not defined(__cdecl)):
        __cdecl = VOID
    # END IF  (not defined (_MSC_VER) and not defined (__cdecl))

    if defined(_M_CEE_PURE):
        __CRTDECL = __clrcall
        __CRTDECL_STDCALL = __clrcall
    else:
        __CRTDECL = __cdecl
        __CRTDECL_STDCALL = __cdecl
    # END IF


    if defined(_M_CEE_PURE):
        __ALTDECL = __clrcall
    else:
        __ALTDECL = __cdecl
    # END IF


    _ARGMAX = 100

    # _TRUNCATE
    _TRUNCATE = -1

    # helper macros for cpp overloads
    if not defined (RC_INVOKED):
        if defined (__cplusplus) and _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES and not defined(__midl):
            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_0(_ReturnType, _FuncName, _DstType, _Dst):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_1(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_2(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_3(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_4(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_1_1(_ReturnType, _FuncName, _HType1, _HArg1, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_1_2(_ReturnType, _FuncName, _HType1, _HArg1, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_1_3(_ReturnType, _FuncName, _HType1, _HArg1, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_2_0(_ReturnType, _FuncName, _HType1, _HArg1, _HType2, _HArg2, _DstType, _Dst):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_1_ARGLIST(_ReturnType, _FuncName, _VFuncName, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_2_ARGLIST(_ReturnType, _FuncName, _VFuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_SPLITPATH(_ReturnType, _FuncName, _DstType, _Src):
                pass
        else:
            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_0(_ReturnType, _FuncName, _DstType, _Dst):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_1(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_2(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_3(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_4(_ReturnType, _FuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_1_1(_ReturnType, _FuncName, _HType1, _HArg1, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_1_2(_ReturnType, _FuncName, _HType1, _HArg1, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_1_3(_ReturnType, _FuncName, _HType1, _HArg1, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_2_0(_ReturnType, _FuncName, _HType1, _HArg1, _HType2, _HArg2, _DstType, _Dst):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_1_ARGLIST(_ReturnType, _FuncName, _VFuncName, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_0_2_ARGLIST(_ReturnType, _FuncName, _VFuncName, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_SECURE_FUNC_SPLITPATH(_ReturnType, _FuncName, _DstType, _Src):
                pass
        # END IF  defined (__cplusplus) and _CRT_SECURE_CPP_OVERLOAD_SECURE_NAMES
    # END IF  not defined (RC_INVOKED)


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_0(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_1(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_3(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_4(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_1_1(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _HType1, _HArg1, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_2_0(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _HType1, _HArg1, _HType2, _HArg2, _SalAttributeDst, _DstType, _Dst):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_1_ARGLIST(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_ARGLIST(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_SIZE(_DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_3_SIZE(_DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_0(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_4(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_1_1(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _HType1, _HArg1, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_2_0(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _HType1, _HArg1, _HType2, _HArg2, _SalAttributeDst, _DstType, _Dst):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1_ARGLIST(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_SIZE(_DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
        pass


    def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3_SIZE(_DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
        pass
    if not defined (RC_INVOKED):
        if defined (__cplusplus) and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES and not defined(__midl):
            def __RETURN_POLICY_SAME(_FunctionCall, _Dst):
                pass


            def __RETURN_POLICY_DST(_FunctionCall, _Dst):
                pass

            def __RETURN_POLICY_VOID(_FunctionCall, _Dst):
                pass

            __EMPTY_DECLSPEC = VOID

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_0_CGETS(_ReturnType, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_3_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_4_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_1_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_2_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _HType2, _HArg2, _SalAttributeDst, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_1_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _VFuncName, _SecureVFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SecureVFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_3_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass

            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                pass

            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                pass

            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                pass

            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass

            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass

            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass

            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass

            if not defined (RC_INVOKED) and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT:
                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_0_CGETS(_ReturnType, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_4_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_1_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_2_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _HType2, _HArg2, _SalAttributeDst, _DstType, _Dst):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _VFuncName, _SecureVFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_ARGLIST(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                    pass


                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass


                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass
            else:
                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst):
                    pass

                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_0_GETS(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _DstType, _Dst):
                    pass

                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_4_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_1_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_2_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _HType2, _HArg2, _SalAttributeDst, _DstType, _Dst):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _VFuncName, _SecureVFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_ARGLIST(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                    pass

                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                    pass

                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                    pass


                def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass


                def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                    pass
            # END IF  not defined (RC_INVOKED) and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_COUNT

        else:
            __RETURN_POLICY_SAME = VOID
            __RETURN_POLICY_DST = VOID
            __RETURN_POLICY_VOID = VOID
            __EMPTY_DECLSPEC = VOID


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_0_CGETS(_ReturnType, _DeclSpec, _FuncName, _SalAttributeDst, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_3_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_4_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_1_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_2_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _HType2, _HArg2, _SalAttributeDst, _DstType, _Dst):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_1_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _VFuncName, _SecureVFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SecureVFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_2_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_FUNC_0_3_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_0_GETS(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass

            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_4_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3, _TType4, _TArg4):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_1_1_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_2_0_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _HType1, _HArg1, _HType2, _HArg2, _SalAttributeDst, _DstType, _Dst):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_1_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _SecureFuncName, _VFuncName, _SecureVFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_ARGLIST(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_ARGLIST_EX(_ReturnType, _ReturnPolicy, _DeclSpec, _FuncName, _VFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_2_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_STANDARD_NFUNC_0_3_SIZE_EX(_DeclSpec, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_FUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_INLINE_FUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                pass

            def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_0_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_1_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_2_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2):
                pass


            def __DECLARE_CPP_OVERLOAD_INLINE_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass


            def __DEFINE_CPP_OVERLOAD_INLINE_NFUNC_0_3_EX(_ReturnType, _ReturnPolicy, _FuncName, _SecureFuncName, _SecureDstType, _SalAttributeDst, _DstType, _Dst, _TType1, _TArg1, _TType2, _TArg2, _TType3, _TArg3):
                pass
        # END IF  defined (__cplusplus) and _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES
    # END IF  not defined (RC_INVOKED)


    threadlocaleinfostruct = struct

    threadmbcinfostruct = struct

    pthreadlocinfo = POINTER()

    pthreadmbcinfo = POINTER()

    __lc_time_data = struct


    localeinfo_._fields_ = [
        ('locinfo', pthreadlocinfo),
        ('mbcinfo', pthreadmbcinfo),
    ]
    if not defined(_TAGLC_ID_DEFINED):
        tagLC_ID._fields_ = [
            ('wLanguage', USHORT),
            ('wCountry', USHORT),
            ('wCodePage', USHORT),
        ]
        _TAGLC_ID_DEFINED = VOID
    # END IF  _TAGLC_ID_DEFINED


    if not defined(_THREADLOCALEINFO):
        class lc_category(ctypes.Structure):
            pass


        lc_category._fields_ = [
            ('locale', POINTER(CHAR)),
            ('wlocale', POINTER(WCHAR)),
            ('refcount', POINTER(INT)),
            ('wrefcount', POINTER(INT)),
        ]
        threadlocaleinfo.lc_category = lc_category


        threadlocaleinfo._fields_ = [
            ('refcount', INT),
            ('lc_codepage', UINT),
            ('lc_collate_cp', UINT),
            # LCID
            ('lc_handle', ULONG * 6),
            ('lc_id', LC_ID * 6),
            ('lc_category', threadlocaleinfo.lc_category * 6),
            ('lc_clike', INT),
            ('mb_cur_max', INT),
            ('lconv_intl_refcount', POINTER(INT)),
            ('lconv_num_refcount', POINTER(INT)),
            ('lconv_mon_refcount', POINTER(INT)),
            ('lconv', POINTER(lconv)),
            ('ctype1_refcount', POINTER(INT)),
            ('ctype1', POINTER(USHORT)),
            ('pctype', POINTER(USHORT)),
            ('pclmap', POINTER(UCHAR)),
            ('pcumap', POINTER(UCHAR)),
            ('lc_time_curr', POINTER(__lc_time_data)),
        ]
        _THREADLOCALEINFO = VOID
    # END IF  _THREADLOCALEINFO


    if not defined(__midl) and not defined(MIDL_PASS):
        # Define Control Flow Guard instrumentation and support functions.
        if defined(_ARM64_):
            _guard_check_icall = __guard_check_icall_thunk
        # END IF


        if not defined(_M_CEE):
            pass
        # END IF


        if defined(_M_AMD64):
            pass
        # END IF

    # END IF


    if defined(__cplusplus):
        pass
    # END IF  __cplusplus

    if defined(_PREFAST_) and defined(_PFT_SHOULD_CHECK_RETURN):
        _Check_return_opt_ = _Check_return_
    else:
        _Check_return_opt_ = VOID
    # END IF


    if defined(_PREFAST_) and defined(_PFT_SHOULD_CHECK_RETURN_WAT):
        _Check_return_wat_ = _Check_return_
    else:
        _Check_return_wat_ = VOID
    # END IF


    if not defined(__midl) and not defined(MIDL_PASS) and defined(_PREFAST_):
        def __crt_typefix(ctype):
            return VOID
    else:
        __crt_typefix = VOID
    # END IF


    if (defined(__midl)):
        # suppress tchar inlines
        if not defined(_NO_INLINING):
            _NO_INLINING = VOID
        # END IF  _NO_INLINING
    # END IF  (defined (__midl))

    if not defined(_CRT_UNUSED):
        def _CRT_UNUSED(x):
            return VOIDx
    # END IF  _CRT_UNUSED

    if (_MSC_VER > 1400) and defined(CRTDLL2):
        # VC9 (15) does not like extern VOID; change it to
        # just VOID.
        __FORCE_INSTANCE_CRTIMP2 = _CRTIMP2
        __FORCE_INSTANCE_EXTERN = 1        # nothing
    else:
        __FORCE_INSTANCE_CRTIMP2 = _CRTIMP2
        __FORCE_INSTANCE_EXTERN = extern
    # END IF


    if ((not defined(_PREFAST_) or (_MSC_FULL_VER >= 160021202))):
        pass
    else:
        # PLACEHOLDER CODE:
        __nullptr = 0
    # END IF  BUG ESP:849 - disabling under prefast

    if not defined(_CRT_STDIO_IMP):
        _CRT_STDIO_IMP = _CRTIMP
    # END IF


    if not defined(_CRT_STDIO_IMP_ALT):
        _CRT_STDIO_IMP_ALT = _CRTIMP_ALT
    # END IF


    if defined(_MSC_VER):
        pass
    # END IF  _MSC_VER
# END IF  _INC_CRTDEFS

# 88bf0570-3001-4e78-a5f2-be5765546192
