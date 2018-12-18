from pyWinAPI import *

# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: poppack.h Abstract: This file turns packing of structures off.
# (That is, it enables automatic alignment of structure fields.) An include
# file is needed because various compilers do this in different ways.
# poppack.h is the complement to pshpack?.h. An inclusion of poppack.h MUST
# ALWAYS be preceded by an inclusion of one of pshpack?.h, in one - to - one
# correspondence. For Microsoft compatible compilers, this file uses the pop
# option to the pack pragma so that it can restore the previous saved by the
# pshpack?.h include file. - -

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
