import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class sockaddr_un(ctypes.Structure):
    pass


SOCKADDR_UN = sockaddr_un
PSOCKADDR_UN = POINTER(sockaddr_un)


# /* + + Copyright (c) Microsoft Corporation Module Name: afunix.h Abstract:
# This file contains the definitions for the AF_UNIX socket address family
# that can be used by both user - mode and kernel mode modules. BETA: The
# definitions in this header are subject to change. - -

_AFUNIX_ = 1
if not defined(_AFUNIX_):

    from pyWinAPI.shared.ws2def_h import * # NOQA
    _AFUNIX_ = 1
    UNIX_PATH_MAX = 108

    sockaddr_un._fields_ = [
        # AF_UNIX
        ('sun_family', ADDRESS_FAMILY),
        # pathname
        ('sun_path', CHAR * UNIX_PATH_MAX),
    ]
# END IF  _AFUNIX_
