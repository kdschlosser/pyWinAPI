from pyWinAPI import *

# /* + + Copyright (c) 2005 Microsoft Corporation Module Name: ipv6prefast.h
# Abstract: Provides control over IPv6 - related PREfast warnings. Revision
# History: - -
_PREFAST_ = 1
IPV6_PREFAST_SAFE = 1
if defined(_PREFAST_) and defined(IPV6_PREFAST_SAFE):
    pass
# END IF   _PREFAST_ ...
