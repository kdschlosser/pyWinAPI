import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__CGUID_H__ = None


from pyWinAPI.shared.winapifamily_h import * # NOQA

# /* +
# -------------------------------------------------------------------------
# Microsoft Windows Copyright (c) Microsoft Corporation. All rights reserved.
# File: cguid.h -
if not defined(__CGUID_H__):
    __CGUID_H__ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    if _MSC_VER >= 800:
        if _MSC_VER >= 1200:
            pass
        # END IF
    # END IF


    if defined(__cplusplus):
        pass
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WINXP:
            pass
        # END IF

        if NTDDI_VERSION >= NTDDI_VISTA:
            pass
        # END IF

        # --------------------------------------------
        # CD Forms CLSIDs
        # --------------------------------------------
        # Form Kernel objects
        # Control objects
        # Property Pages    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Enumerations
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if defined(__cplusplus):
        pass
    # END IF

    if _MSC_VER >= 800:
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF

    # END IF

# END IF  __CGUID_H__


