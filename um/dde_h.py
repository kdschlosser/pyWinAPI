

from wtypes_h import (
    UINT,
    SHORT,
    BYTE,
)
import ctypes
import ntdef_h


# ****************************************************************************\
# *                                                                           
#  *
# * dde.h -       Dynamic Data Exchange structures and definitions            
#  *
# *                                                                           
#  *
# * Copyright (c) 1993-1999, Microsoft Corp.    All rights reserved          *
# *                                                                           
#  *
# \****************************************************************************
from windef_h import * # NOQA
from winapifamily_h import * # NOQA
# padding added after data member
# begin_r_dde
# DDE window messages
WM_DDE_FIRST = 0x000003E0
WM_DDE_INITIATE = WM_DDE_FIRST
WM_DDE_TERMINATE = WM_DDE_FIRST+1
WM_DDE_ADVISE = WM_DDE_FIRST+2
WM_DDE_UNADVISE = WM_DDE_FIRST+3
WM_DDE_ACK = WM_DDE_FIRST+4
WM_DDE_DATA = WM_DDE_FIRST+5
WM_DDE_REQUEST = WM_DDE_FIRST+6
WM_DDE_POKE = WM_DDE_FIRST+7
WM_DDE_EXECUTE = WM_DDE_FIRST+8
WM_DDE_LAST = WM_DDE_FIRST+8
# end_r_dde
# ----------------------------------------------------------------------------
# |       DDEACK structure
# |
# |    Structure of wStatus (LOWORD(lParam)) in WM_DDE_ACK message
# |       sent in response to a WM_DDE_DATA, WM_DDE_REQUEST, WM_DDE_POKE,
# |       WM_DDE_ADVISE, or WM_DDE_UNADVISE message.
# |
# ----------------------------------------------------------------------------

class DDEACK(ctypes.Structure):
    _fields_ = [
        ('SHORT bAppReturnCode:8', UINT),
        ('reserved:6', UINT),
        ('fBusy:1', UINT),
        ('fAck:1', UINT),
        ('SHORT usFlags', UINT),
    ]



# ----------------------------------------------------------------------------
# |       DDEADVISE structure
# |
# |    WM_DDE_ADVISE parameter structure for hOptions (LOWORD(lParam))
# |
# ----------------------------------------------------------------------------

class DDEADVISE(ctypes.Structure):
    _fields_ = [
        ('SHORT reserved:14', UINT),
        ('fDeferUpd:1', UINT),
        ('fAckReq:1', UINT),
        ('SHORT usFlags', UINT),
        ('cfFormat', SHORT),
    ]



# ----------------------------------------------------------------------------
# |       DDEDATA structure
# |
# |       WM_DDE_DATA parameter structure for hData (LOWORD(lParam)).
# |       The actual size of this structure depends on the size of
# |       the Value array.
# |
# ----------------------------------------------------------------------------

class DDEDATA(ctypes.Structure):
    _fields_ = [
        ('SHORT unused:12', UINT),
        ('fResponse:1', UINT),
        ('fRelease:1', UINT),
        ('reserved:1', UINT),
        ('fAckReq:1', UINT),
        ('SHORT usFlags', UINT),
        ('cfFormat', SHORT),
        ('Value', BYTE * 1),
    ]



# ----------------------------------------------------------------------------
# |    DDEPOKE structure
# |
# |    WM_DDE_POKE parameter structure for hData (LOWORD(lParam)).
# |       The actual size of this structure depends on the size of
# |       the Value array.
# |
# ----------------------------------------------------------------------------

class DDEPOKE(ctypes.Structure):
    _fields_ = [
        ('SHORT unused:13', UINT),
        ('fRelease:1', UINT),
        ('fReserved:2', UINT),
        ('SHORT usFlags', UINT),
        ('cfFormat', SHORT),
        ('Value', BYTE * 1),
    ]



# Earlier versions of DDE.H incorrectly
# 12 unused bits.
# This member was named rgb[1] in previous
# versions of DDE.H
# ----------------------------------------------------------------------------
# The following typedef's were used in previous versions of the Windows SDK.
# They are still valid.  The above typedef's define exactly the same structures
# as those below.  The above typedef names are recommended, however, as they
# are more meaningful.
# Note that the DDEPOKE structure typedef'ed in earlier versions of DDE.H did
# not correctly define the bit positions.
# ----------------------------------------------------------------------------

class DDELN(ctypes.Structure):
    _fields_ = [
        ('SHORT unused:13', UINT),
        ('fRelease:1', UINT),
        ('fDeferUpd:1', UINT),
        ('fAckReq:1', UINT),
        ('SHORT usFlags', UINT),
        ('cfFormat', SHORT),
    ]




class DDEUP(ctypes.Structure):
    _fields_ = [
        ('SHORT unused:12', UINT),
        ('fAck:1', UINT),
        ('fRelease:1', UINT),
        ('fReserved:1', UINT),
        ('fAckReq:1', UINT),
        ('SHORT usFlags', UINT),
        ('cfFormat', SHORT),
        ('rgb', BYTE * 1),
    ]




# * DDE SECURITY


# * DDE message packing APIs

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# _DDEHEADER_INCLUDED_

__all__ = (
    'WM_DDE_REQUEST', 'WM_DDE_ACK', 'WM_DDE_ADVISE', 'WM_DDE_FIRST', 'DDEACK', 
    'WM_DDE_LAST', 'WM_DDE_EXECUTE', 'WM_DDE_DATA', 'WM_DDE_TERMINATE', 
    'WM_DDE_POKE', 'WM_DDE_INITIATE', 'WM_DDE_UNADVISE', 'DDEPOKE', 'DDEDATA', 
    'DDEUP', 'DDEADVISE', 'DDELN', 
)
