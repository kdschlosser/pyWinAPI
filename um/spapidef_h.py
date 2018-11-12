import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

_INC_SPAPIDEF = None
SP_LOG_TOKEN = None

# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# spapidef.h Abstract: Public header file for Windows NT Setup and Device
# Installer services Dll. - -
if not defined(_INC_SPAPIDEF):
    _INC_SPAPIDEF = 1

    from pyWinAPI.shared.winapifamily_h import *
    from pyWinAPI.shared.guiddef_h import *

    if _MSC_VER > 1000:
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(SP_LOG_TOKEN):
            SP_LOG_TOKEN = DWORDLONG
            PSP_LOG_TOKEN = POINTER(DWORDLONG)
        # END IF

        # Special txtlog token values
        LOGTOKEN_TYPE_MASK = 3
        LOGTOKEN_UNSPECIFIED = 0
        LOGTOKEN_NO_LOG = 1
        LOGTOKEN_SETUPAPI_APPLOG = 2
        LOGTOKEN_SETUPAPI_DEVLOG = 3

        # Flags for SetupCreateTextLogSection
        TXTLOG_SETUPAPI_DEVLOG = 0x00000001
        TXTLOG_SETUPAPI_CMDLINE = 0x00000002
        TXTLOG_SETUPAPI_BITS = 0x00000003

        # Flags for SetupWriteTextLog

        # Event Levels (bits 0 - 3)
        TXTLOG_ERROR = 0x1
        TXTLOG_WARNING = 0x2
        TXTLOG_SYSTEM_STATE_CHANGE = 0x3
        TXTLOG_SUMMARY = 0x4
        TXTLOG_DETAILS = 0x5
        TXTLOG_VERBOSE = 0x6
        TXTLOG_VERY_VERBOSE = 0x7

        # Bits reserved for internal use
        TXTLOG_RESERVED_FLAGS = 0x0000FFF0

        # Basic flags (bits 4 - 31)
        TXTLOG_TIMESTAMP = 0x00010000
        TXTLOG_DEPTH_INCR = 0x00020000
        TXTLOG_DEPTH_DECR = 0x00040000
        TXTLOG_TAB_1 = 0x00080000
        TXTLOG_FLUSH_FILE = 0x00100000


        def TXTLOG_LEVEL(flags):
            return flags & 0xF


        # Setupapi, Setupdi event categories
        TXTLOG_DEVINST = 0x00000001
        TXTLOG_INF = 0x00000002
        TXTLOG_FILEQ = 0x00000004
        TXTLOG_COPYFILES = 0x00000008
        TXTLOG_SIGVERIF = 0x00000020
        TXTLOG_BACKUP = 0x00000080
        TXTLOG_UI = 0x00000100
        TXTLOG_UTIL = 0x00000200
        TXTLOG_INFDB = 0x00000400
        TXTLOG_POLICY = 0x00800000
        TXTLOG_NEWDEV = 0x01000000
        TXTLOG_UMPNPMGR = 0x02000000
        TXTLOG_DRIVER_STORE = 0x04000000
        TXTLOG_SETUP = 0x08000000
        TXTLOG_CMI = 0x10000000
        TXTLOG_DEVMGR = 0x20000000
        TXTLOG_INSTALLER = 0x40000000
        TXTLOG_VENDOR = 0x80000000
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _INC_SPAPIDEF
