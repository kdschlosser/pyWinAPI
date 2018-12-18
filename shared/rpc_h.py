import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *




# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: rpc.h Abstract: Master include file for RPC applications. - -
    # /* Pull in WINDOWS.H if necessary

RPC_NO_WINDOWS_H = None
MAC = None
_KRPCENV_ = None

if not defined(RPC_NO_WINDOWS_H) and not defined(MAC) and not defined(_MAC) and not defined(_KRPCENV_):

    _INC_WINDOWS = None
    if not defined(_INC_WINDOWS):
        from pyWinAPI.um.windows_h import * # NOQA
    # END IF  _INC_WINDOWS
# END IF   RPC_NO_WINDOWS_H

__RPC_H__ = None
if not defined(__RPC_H__):
    __RPC_H__ = 1

    if _MSC_VER > 1000:
        pass
    # END IF

    if defined(__cplusplus):
        pass
    # END IF
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # platform specific defines
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - MAC - - - - - - - - - - - - - - -
    # - - - - - - - - - - - -
    if defined(MAC) or defined(_MAC):
        __RPC_MAC__ = 1
        # Set the packing level for RPC structures.
        from pyWinAPI.shared.pshpack2_h import * # NOQA
        __RPC_ARM32__ = None
        __RPC_WIN64__ = None
        __RPC_ARM64__ = None
        __RPC_WIN32__ = None

        # - - - - - - - - - - - - - - - - - - - WIN32 - - - - - - - - - - - -
        # - - - - - - - - - - - - - - -
    else:
        __RPC_MAC__ = None
        from pyWinAPI.shared.basetsd_h import * # NOQA
        if defined(_M_ARM64):
            __RPC_ARM64__ = 1
            __RPC_WIN32__ = None
            __RPC_WIN64__ = None
            __RPC_ARM32__ = None
        elif defined(_M_IA64) or defined(_M_AMD64):
            __RPC_WIN64__ = 1
            __RPC_ARM64__ = None
            __RPC_WIN32__ = None
            __RPC_ARM32__ = None
        elif defined(_ARM_):
            __RPC_ARM32__ = 1
            __RPC_WIN64__ = None
            __RPC_ARM64__ = None
            __RPC_WIN32__ = None
        else:
            __RPC_ARM32__ = None
            __RPC_WIN64__ = None
            __RPC_ARM64__ = None
            __RPC_WIN32__ = 1
        # END IF   defined(_M_ARM64)
    # END IF   defined( MAC ) or defined( _MAC )
    if defined(__RPC_WIN64__) or defined(__RPC_ARM64__):
        from pyWinAPI.shared.pshpack8_h import * # NOQA
    # END IF
    __MIDL_USER_DEFINED = None

    if not defined(__MIDL_USER_DEFINED):
        # midl_user_allocate = MIDL_user_allocate
        # midl_user_free = MIDL_user_free
        __MIDL_USER_DEFINED = 1
    # END IF

    # NTSTATUS is also long, so this definition is valid
    # for both user mode and kernel mode
    __specstrings = None
    if defined(__specstrings):
        RPC_STATUS = LONG
    else:
        RPC_STATUS = LONG
    # END IF

    if (
        defined(__RPC_WIN32__) or
        defined(__RPC_WIN64__) or
        defined(__RPC_ARM32__) or
        defined(__RPC_ARM64__)
    ):
        RPC_UNICODE_SUPPORTED = 1
    else:
        RPC_UNICODE_SUPPORTED = None

    # END IF
    if (
        not defined(__RPC_MAC__) and
        (_MSC_VER >= 800 or defined(_STDCALL_SUPPORTED))
    ):
        __RPC_API = ctypes.WINFUNCTYPE
        __RPC_USER = ctypes.WINFUNCTYPE
        __RPC_STUB = ctypes.WINFUNCTYPE
        RPC_ENTRY = ctypes.WINFUNCTYPE
    else:
        def do_nothing_func(item):
            return item

        __RPC_API = do_nothing_func
        __RPC_USER = do_nothing_func
        __RPC_STUB = do_nothing_func
        RPC_ENTRY = do_nothing_func
    # END IF

    __RPC_FAR = 1
    # Some RPC platforms don't define DECLSPEC_IMPORT

    if not defined(DECLSPEC_IMPORT):
        if (
            (
                defined(_M_MRX000) or defined(_M_IX86) or defined(_M_IA64) or
                defined(_M_AMD64) or defined(_M_ARM) or defined(_M_ARM64)
            ) and
            not defined(MIDL_PASS)
        ):
            def DECLSPEC_IMPORT(dllimport):
                return dllimport
        else:
            def DECLSPEC_IMPORT(dllimport):
                return dllimport
        # END IF
    # END IF
    _RPCRT4_ = None
    if not defined(_RPCRT4_) and not defined(_KRPCENV_):
        RPCRTAPI = DECLSPEC_IMPORT
    else:
        def RPCRTAPI(dllimport):
            return dllimport
    # END IF
    _RPCNS4_ = None
    if not defined(_RPCNS4_):
        RPCNSAPI = DECLSPEC_IMPORT
    else:
        def RPCNSAPI(dllimport):
            return dllimport
    # END IF

    if defined(__RPC_MAC__):
        from pyWinAPI.km.crt.setjmp_h import * # NOQA
        RPCXCWORD = ctypes.sizeof(jmp_buf) / ctypes.sizeof(int)

        if _MSC_VER >= 1200:
            pass
        # END IF

        from pyWinAPI.shared.rpcdce_h import * # NOQA
        from pyWinAPI.shared.rpcnsi_h import * # NOQA
        from pyWinAPI.shared.rpcerr_h import * # NOQA
        from pyWinAPI.shared.rpcmac_h import * # NOQA

        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF

        # typedef VOID  (RPC_ENTRY *MACYIELDCALLBACK)( SHORT *) ; // OSErr
        MACYIELDCALLBACK = RPC_ENTRY(VOID, POINTER(SHORT))

        if not defined(UNALIGNED):
            UNALIGNED = 1
        # END IF

        from pyWinAPI.shared.poppack_h import * # NOQA
    else:
        from pyWinAPI.shared.rpcdce_h import * # NOQA

        if not defined(_KRPCENV_):
            from pyWinAPI.shared.rpcnsi_h import * # NOQA
        # END IF   _KRPCENV_

        from pyWinAPI.shared.rpcnterr_h import * # NOQA
        from pyWinAPI.km.crt.excpt_h import * # NOQA

        if not defined(_KRPCENV_):
            from pyWinAPI.shared.winerror_h import * # NOQA
        # END IF   _KRPCENV_

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # END IF   __RPC_MAC__
    # rpcasync.h is now RPC_NO_WINDOWS_H aware, but we can't start including
    # it always
    # as it does still require windef.h which could clash with another header.
    # Parsing of the below test:
    # don't include rpcasync.h if either RPC_NO_WINDOWS_H or __RPC_MAC__ is
    # set, except that setting
    # RPC_NEED_RPCASYNC_H overrides RPC_NO_WINDOWS_H.
    # In any case, if _KRPCENV_ is set, include rpcasync.h regardless of any
    # of the above being set.
    if (
        (
            (not defined( RPC_NO_WINDOWS_H ) or defined(RPC_NEED_RPCASYNC_H))
            and not defined(__RPC_MAC__)
        ) or defined(_KRPCENV_)
    ):
        from pyWinAPI.shared.rpcasync_h import * # NOQA
    # END IF   RPC_NO_WINDOWS_H et al.

    if defined(__RPC_WIN64__) or defined(__RPC_ARM64__):
        from pyWinAPI.shared.poppack_h import * # NOQA
    # END IF

    if defined(__cplusplus):
        pass
    # END IF

# END IF   __RPC_H__
