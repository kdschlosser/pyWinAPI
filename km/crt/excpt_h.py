import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_INC_EXCPT = None



# * excpt.h - defines exception values, types and routines  Copyright (c)
# Microsoft Corporation. All rights reserved. Purpose: This file contains the
# definitions and prototypes for the compiler- dependent intrinsics, support
# functions and keywords which implement the structured exception handling
# extensions. [Public] *
if _MSC_VER > 1000:
    pass
# END IF


if not defined(_INC_EXCPT):
    _INC_EXCPT = 1
    from pyWinAPI.km.crt.crtdefs_h import * # NOQA

        # /* Currently, all MS C compilers for Win32 platforms default to 8
        # byte alignment.
    if defined(_MSC_VER):
        pass
    # END IF  _MSC_VER

    if defined(__cplusplus):
        pass
    # END IF


    # /* Exception disposition return values.
    class _EXCEPTION_DISPOSITION(ENUM):
        ExceptionContinueExecution = 1
        ExceptionContinueSearch = 2
        ExceptionNestedException = 3
        ExceptionCollidedUnwind = 4

    EXCEPTION_DISPOSITION = _EXCEPTION_DISPOSITION

    # /* Prototype for SEH support function.
        # /* Declarations to keep MS C 8 (386/486) compiler happy
    if defined(_M_IX86):

        class _EXCEPTION_RECORD(ctypes.Structure):
            pass

        class _CONTEXT(ctypes.Structure):
            pass

    # END IF


        # /* Declarations to keep AMD64 compiler happy
    if defined(_M_AMD64) or defined(_M_ARM) or defined(_M_ARM64) or defined(_M_HYBRID):
        class _EXCEPTION_RECORD(ctypes.Structure):
            pass

        class _CONTEXT(ctypes.Structure):
            pass

        class _DISPATCHER_CONTEXT(ctypes.Structure):
            pass

        if not defined(_M_CEE_PURE):
            ntdll = ctypes.windll.NTDLL


            # _CRTIMP EXCEPTION_DISPOSITION __cdecl __C_specific_handler(
            # _In_ struct _EXCEPTION_RECORD * ExceptionRecord,
            # _In_ VOID * EstablisherFrame,
            # _Inout_ struct _CONTEXT * ContextRecord,
            # _Inout_ struct _DISPATCHER_CONTEXT * DispatcherContext
            # );
            __C_specific_handler = ntdll.__C_specific_handler
            __C_specific_handler.restype = EXCEPTION_DISPOSITION
        # END IF

    # END IF

    # /* Keywords and intrinsics for SEH
    if defined(_MSC_VER):
        # GetExceptionCode = _exception_code
        # exception_code = _exception_code
        # GetExceptionInformation = (struct _EXCEPTION_POINTERS *)_exception_info
        # exception_info = (struct _EXCEPTION_POINTERS *)_exception_info
        # AbnormalTermination = _abnormal_termination
        # abnormal_termination = _abnormal_termination
        pass
    # END IF

    # /* Legal values for expression in except().
    EXCEPTION_EXECUTE_HANDLER = 1
    EXCEPTION_CONTINUE_SEARCH = 0
    EXCEPTION_CONTINUE_EXECUTION = -1
    if defined(__cplusplus):
        pass
    # END IF

    if defined(_MSC_VER):
        pass
    # END IF  _MSC_VER
# END IF  _INC_EXCPT

# 88bf0570-3001-4e78-a5f2-be5765546192
