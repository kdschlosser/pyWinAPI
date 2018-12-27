import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LM_ = None

# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lm.h Abstract:
# This is the top level include file that includes all the files necessary for
# writing Lan Manager Application. [Environment:] User Mode - Win32 --
if not defined(_LM_):
    _LM_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # LAN Manager common definitions
        from pyWinAPI.shared.lmcons_h import * # NOQA

        # LAN Manager network error definitions
        from pyWinAPI.shared.lmerr_h import * # NOQA

        # Access, Domain, Group and User classes
        from pyWinAPI.um.lmaccess_h import * # NOQA

        # Alerter
        from pyWinAPI.um.lmalert_h import * # NOQA

        # Connection, File, Session and Share classes
        from pyWinAPI.um.lmshare_h import * # NOQA

        # Message class
        from pyWinAPI.um.lmmsg_h import * # NOQA

        # Remote Utility class
        from pyWinAPI.um.lmremutl_h import * # NOQA

        # Replicator class
        from pyWinAPI.um.lmrepl_h import * # NOQA

        # Server class
        from pyWinAPI.um.lmserver_h import * # NOQA

        # Service class
        from pyWinAPI.um.lmsvc_h import * # NOQA

        # Use class
        from pyWinAPI.um.lmuse_h import * # NOQA

        # Workstation class
        from pyWinAPI.um.lmwksta_h import * # NOQA

        # NetApiBuffer class
        from pyWinAPI.um.lmapibuf_h import * # NOQA

        # NetErrorLog class
        from pyWinAPI.um.lmerrlog_h import * # NOQA

        # NetConfig class
        from pyWinAPI.um.lmconfig_h import * # NOQA

        # NetStats class
        from pyWinAPI.um.lmstats_h import * # NOQA

        # NetAudit class
        from pyWinAPI.um.lmaudit_h import * # NOQA

        # NetJoinDomain class
        from pyWinAPI.um.lmjoin_h import * # NOQA
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   _LM_


