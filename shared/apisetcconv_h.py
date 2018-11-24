from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

# **********************************************************************
# * apisetcconv.h - - Contains Win32 Calling Conventions for APISETs * that
# were a part of the old legacy APIs * Copyright (c) Microsoft Corp. All
# rights reserved. * *
# *********************************************************************
_APISETCCONV_ = None
if not defined(_APISETCCONV_):
    _APISETCCONV_ = 1

    WINADVAPI = None
    if not defined(WINADVAPI):
        _ADVAPI32_ = None
        if not defined(_ADVAPI32_):
            WINADVAPI = DECLSPEC_IMPORT
        else:
            WINADVAPI = 1
        # END IF
    # END IF
    WINBASEAPI = None
    if not defined(WINBASEAPI):
        _KERNEL32_ = None
        if not defined(_KERNEL32_):
            WINBASEAPI = DECLSPEC_IMPORT
        else:
            WINBASEAPI = 1
        # END IF
    # END IF
    ZAWPROXYAPI = None
    if not defined(ZAWPROXYAPI):
        _ZAWPROXY_ = None
        if not defined(_ZAWPROXY_):
            ZAWPROXYAPI = DECLSPEC_IMPORT
        else:
            ZAWPROXYAPI = 1
        # END IF
    # END IF
    WINUSERAPI = None
    if not defined(WINUSERAPI):
        _USER32_ = None
        if not defined(_USER32_):
            WINUSERAPI = DECLSPEC_IMPORT
            WINABLEAPI = DECLSPEC_IMPORT
        else:
            WINUSERAPI = 1
            WINABLEAPI = 1
        # END IF
    # END IF
    else:
        WINABLEAPI = None

    if not defined(WINABLEAPI):
        _USER32_ = None
        if not defined(_USER32_):
            WINABLEAPI = DECLSPEC_IMPORT
        else:
             WINABLEAPI = 1
        # END IF
    # END IF
    WINCFGMGR32API = None
    if not defined(WINCFGMGR32API):
        _SETUPAPI_ = None
        if not defined(_SETUPAPI_):
            WINCFGMGR32API = DECLSPEC_IMPORT
        else:
            WINCFGMGR32API = 1
        # END IF
    # END IF
    WINDEVQUERYAPI = None
    if not defined(WINDEVQUERYAPI):
        _CFGMGR32_ = None
        if not defined(_CFGMGR32_):
            WINDEVQUERYAPI = DECLSPEC_IMPORT
        else:
            WINDEVQUERYAPI = 1
        # END IF
    # END IF

    WINSWDEVICEAPI = None
    if not defined(WINSWDEVICEAPI):
        _CFGMGR32_ = None
        if not defined(_CFGMGR32_):
            WINSWDEVICEAPI = DECLSPEC_IMPORT
        else:
            WINSWDEVICEAPI = 1
        # END IF
    # END IF

    CMAPI = None
    if not defined(CMAPI):
        _CFGMGR32_ = None
        if not defined(_CFGMGR32_):
            CMAPI = DECLSPEC_IMPORT
        else:
            CMAPI = 1
        # END IF
    # END IF

    WINPATHCCHAPI = None
    if not defined(WINPATHCCHAPI):
        STATIC_PATHCCH = None
        if not defined(STATIC_PATHCCH):
            WINPATHCCHAPI = WINBASEAPI
        else:
            WINPATHCCHAPI = 1
        # END IF
    # END IF
# END IF   _APISETCCONV_
