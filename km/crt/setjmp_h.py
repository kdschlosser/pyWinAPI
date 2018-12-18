import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class __JUMP_BUFFER(ctypes.Structure):
    pass


_JUMP_BUFFER = __JUMP_BUFFER


class _SETJMP_FLOAT128(ctypes.Structure):
    pass

SETJMP_FLOAT128 = _SETJMP_FLOAT128


# * setjmp.h - definitions/declarations for setjmp/longjmp routines  Copyright
# (c) Microsoft Corporation. All rights reserved. Purpose: This file defines
# the machine - dependent buffer used by setjmp/longjmp to save and restore
# the program state, and declarations for those routines. [ANSI/System V]
# [Public] *

if _MSC_VER > 1000:
    pass
# END IF

_INC_SETJMP = None
_INC_SETJMPEX = None
_JMP_BUF_DEFINED = None

if not defined(_INC_SETJMP):
    _INC_SETJMP = 1

    ucrtbase = ctypes.windll.UCRTBASE

    from pyWinAPI.km.crt.crtdefs_h import * # NOQA

        # /* The reason why simple setjmp won't work here is that there may be
        # case when CLR stubs are on the stack e.g. function call just after
        # jitting, and not unwinding CLR will result in bad state of CLR which
        # then can AV or do something very bad.

    if defined(_M_CEE):
        from pyWinAPI.km.crt.setjmpex_h import * # NOQA
    # END IF  defined(_M_CEE)

    if defined(_MSC_VER):
        # /* Currently, all MS C compilers for Win32 platforms default to 8
        # byte alignment.
        pass
    # END IF  _MSC_VER

    if defined(__cplusplus):
        pass
    # END IF

    # /* Definitions specific to particular setjmp implementations.
        # /* MS compiler for x86
    if defined(_M_IX86):
        if not defined(_INC_SETJMPEX):
            setjmp = ucrtbase.setjmp
        # END IF

        _JBLEN = 16
        _JBTYPE = INT

        # /* Define jump buffer layout for x86 setjmp/longjmp.
        __JUMP_BUFFER._fields_ = [
            ('Ebp', ULONG),
            ('Ebx', ULONG),
            ('Edi', ULONG),
            ('Esi', ULONG),
            ('Esp', ULONG),
            ('Eip', ULONG),
            ('Registration', ULONG),
            ('TryLevel', ULONG),
            ('Cookie', ULONG),
            ('UnwindFunc', ULONG),
            ('UnwindData', ULONG * 6),
        ]

    elif defined(_M_AMD64):
        _SETJMP_FLOAT128._fields_ = [
            ('INT64 Part', UINT * 2),
        ]
        _JBLEN = 16
        _JBTYPE = _SETJMP_FLOAT128

        if not defined(_INC_SETJMPEX):
            setjmp = ucrtbase.setjmp
        # END IF

        _JUMP_BUFFER._fields_ = [
            ('INT64 Frame', UINT),
            ('INT64 Rbx', UINT),
            ('INT64 Rsp', UINT),
            ('INT64 Rbp', UINT),
            ('INT64 Rsi', UINT),
            ('INT64 Rdi', UINT),
            ('INT64 R12', UINT),
            ('INT64 R13', UINT),
            ('INT64 R14', UINT),
            ('INT64 R15', UINT),
            ('INT64 Rip', UINT),
            ('MxCsr', ULONG),
            ('FpCsr', USHORT),
            ('Spare', USHORT),
            ('Xmm6', SETJMP_FLOAT128),
            ('Xmm7', SETJMP_FLOAT128),
            ('Xmm8', SETJMP_FLOAT128),
            ('Xmm9', SETJMP_FLOAT128),
            ('Xmm10', SETJMP_FLOAT128),
            ('Xmm11', SETJMP_FLOAT128),
            ('Xmm12', SETJMP_FLOAT128),
            ('Xmm13', SETJMP_FLOAT128),
            ('Xmm14', SETJMP_FLOAT128),
            ('Xmm15', SETJMP_FLOAT128),
        ]
    elif defined(_M_ARM):
        if not defined(_INC_SETJMPEX):
            setjmp = ucrtbase.setjmp
        # END IF

        # /* ARM setjmp definitions.
        _JBLEN = 28
        _JBTYPE = INT

    elif defined(_M_ARM64):
        _JBLEN = 24
        _JBTYPE = UINT64

        if not defined(_INC_SETJMPEX):
            setjmp = VOID
        # END IF
    # END IF

    if not defined(_JMP_BUF_DEFINED):
        _JMP_BUF_DEFINED = 1
        jmp_buf = _JBTYPE * _JBLEN
    # END IF

    # Function prototypes

    # INT __cdecl setjmp(_Out_ jmp_buf _Buf);

        ntdll = ctypes.windll.NTDLL

    if defined(__cplusplus):
        if _MSC_VER >= 1200:
            pass

    # END IF
    if defined(_MSC_VER):
        pass
    # END IF  _MSC_VER
# END IF  _INC_SETJMP
