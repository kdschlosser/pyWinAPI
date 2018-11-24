from pyWinAPI import *
from pyWinAPI.shared.guiddef_h import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -
# File: ATSMedia.h
# Desc: Broadcast Driver Architecture Media Definitions for ATSC
# Copyright (c) 1996 - 2001, Microsoft Corporation. All rights reserved.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -
from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

    _KSMEDIA_ = 1
    if not defined(_KSMEDIA_):
        pass
    # END IF   not defined(_KSMEDIA_)
    _BDAMEDIA_ = 1
    if not defined(_BDAMEDIA_):
        pass
    # END IF   not defined(_KSMEDIA_)
    _ATSCMEDIA_ = None
    if not defined(_ATSCMEDIA_):
        _ATSCMEDIA_ = 1
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # ATSC Network Type
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_BDANETWORKTYPE_ATSC = (
            0x71985F51,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        BDANETWORKTYPE_ATSC = DEFINE_GUIDSTRUCT(
            "71985F51-1CA1-11d3-9CC8-00C04F7971E0"
        )
        BDANETWORKTYPE_ATSC = DEFINE_GUIDNAMED(BDANETWORKTYPE_ATSC)
    # END IF   _ATSCMEDIA_
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
