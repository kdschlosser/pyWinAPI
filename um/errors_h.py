import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -
# File: Errors.h
# Desc: ActiveMovie error defines.
# Copyright (c) 1992 - 2001, Microsoft Corporation. All rights reserved.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -

__ERRORS__ = None
if not defined(__ERRORS__):
    __ERRORS__ = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        _AMOVIE_ = 0

        if defined(__cplusplus):
            pass
        # END IF   __cplusplus

        if not defined(_AMOVIE_):
            AMOVIEAPI = DECLSPEC_IMPORT
        else:
            AMOVIEAPI = 1
        # END IF
        # codes 0 - 01ff are reserved for OLE
        VFW_FIRST_CODE = 0x200
        MAX_ERROR_TEXT_LEN = 160

        # includes all message definitions
        from pyWinAPI.um.vfwmsgs_h import * # NOQA

        AMGETERRORTEXTPROCA = CALLBACK(BOOL, HRESULT, CHAR, DWORD)
        AMGETERRORTEXTPROCW = CALLBACK(BOOL, HRESULT, WCHAR, DWORD)

        quartz = ctypes.windll.quartz

        # AMOVIEAPI DWORD WINAPI AMGetErrorTextA( HRESULT hr , _Out_writes_(MaxLen) LPSTR pbuffer , DWORD MaxLen);
        AMGetErrorTextA = quartz.AMGetErrorTextA
        AMGetErrorTextA.restype = DWORD

        # AMOVIEAPI DWORD WINAPI AMGetErrorTextW( HRESULT hr , _Out_writes_(MaxLen) LPWSTR pbuffer , DWORD MaxLen);
        AMGetErrorTextW = quartz.AMGetErrorTextW
        AMGetErrorTextW.restype = DWORD


        if defined(UNICODE):
            AMGetErrorText = AMGetErrorTextW
            AMGETERRORTEXTPROC = AMGETERRORTEXTPROCW
        else:
            AMGetErrorText = AMGetErrorTextA
            AMGETERRORTEXTPROC = AMGETERRORTEXTPROCA
        # END IF
        if defined(__cplusplus):
            pass
        # END IF   __cplusplus
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __ERRORS__
