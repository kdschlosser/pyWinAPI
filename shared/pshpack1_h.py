from pyWinAPI import *

# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: pshpack1.h Abstract: This file turns 1 byte packing of structures on.
# (That is, it disables automatic alignment of structure fields.) An include
# file is needed because various compilers do this in different ways. For
# Microsoft compatible compilers, this files uses the push option to the pack
# pragma so that the poppack.h include file can restore the previous packing
# reliably. The file poppack.h is the complement to this file. - -
lint = None
_PUSHPOP_SUPPORTED = None
if not (defined(lint) or defined(RC_INVOKED)):
    if (
        (_MSC_VER >= 800 and not defined(_M_I86)) or
        defined(_PUSHPOP_SUPPORTED)
    ):
        if not defined(MIDL_PASS) or defined(__midl):
            pass
        else:
            pass
        # END IF
    else:
        pass
    # END IF
    pass
# END IF  not  (defined(lint) or defined(RC_INVOKED))
