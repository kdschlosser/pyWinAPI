from .wtypes_h import (
    RECT,
    VOID,
    POINTER,
    LPVOID,
    CHAR,
    DWORD,
    LONG,
    INT,
    RECTL,
    LPRECT,
    PRECTL,
    LPRECTL,
    LPCRECTL,
    CALLBACK,
    ULONG_PTR,
    WORD
)
from .mmreg_h import mmioFOURCC
import ctypes


# ******************************************************************
# *
# *      FILE:           dciddi.h
# *
# *      DESCRIPTION:    definitions for MS/Intel-defined DCI INTerface
# *
# *      Copyright (C) 1994-1999 Intel/Microsoft Corporation.  All Rights
# Reserved.
# *
# ******************************************************************
from .winapifamily_h import * # NOQA
# DCI Command Escapes
DCICOMMAND = 0x00000C03
DCI_VERSION = 0x00000100
DCICREATEPRIMARYSURFACE = 0x00000001
DCICREATEOFFSCREENSURFACE = 0x00000002
DCICREATEOVERLAYSURFACE = 0x00000003
DCIENUMSURFACE = 0x00000004
DCIESCAPE = 0x00000005
# DCI-Defined error codes
# success
DCI_OK = 0x00000000
# Hard errors -- DCI will be unavailable
DCI_FAIL_GENERIC = -1
DCI_FAIL_UNSUPPORTEDVERSION = -2
DCI_FAIL_INVALIDSURFACE = -3
DCI_FAIL_UNSUPPORTED = -4
# Soft errors -- DCI may be available later
DCI_ERR_CURRENTLYNOTAVAIL = -5
DCI_ERR_INVALIDRECT = -6
DCI_ERR_UNSUPPORTEDFORMAT = -7
DCI_ERR_UNSUPPORTEDMASK = -8
DCI_ERR_TOOBIGHEIGHT = -9
DCI_ERR_TOOBIGWIDTH = -10
DCI_ERR_TOOBIGSIZE = -11
DCI_ERR_OUTOFMEMORY = -12
DCI_ERR_INVALIDPOSITION = -13
DCI_ERR_INVALIDSTRETCH = -14
DCI_ERR_INVALIDCLIPLIST = -15
DCI_ERR_SURFACEISOBSCURED = -16
DCI_ERR_XALIGN = -17
DCI_ERR_YALIGN = -18
DCI_ERR_XYALIGN = -19
DCI_ERR_WIDTHALIGN = -20
DCI_ERR_HEIGHTALIGN = -21
# success messages -- DCI call succeeded, but specified item changed
DCI_STATUS_POINTERCHANGED = 0x00000001
DCI_STATUS_STRIDECHANGED = 0x00000002
DCI_STATUS_FORMATCHANGED = 0x00000004
DCI_STATUS_SURFACEINFOCHANGED = 0x00000008
DCI_STATUS_CHROMAKEYCHANGED = 0x00000010
DCI_STATUS_WASSTILLDRAWING = 0x00000020


def DCI_SUCCESS(error):
    return DCIRVAL(error) >= 0


# DCI Capability Flags
DCI_SURFACE_TYPE = 0x0000000F
DCI_PRIMARY = 0x00000000
DCI_OFFSCREEN = 0x00000001
DCI_OVERLAY = 0x00000002
DCI_VISIBLE = 0x00000010
DCI_CHROMAKEY = 0x00000020
DCI_1632_ACCESS = 0x00000040
DCI_DWORDSIZE = 0x00000080
DCI_DWORDALIGN = 0x00000100
DCI_WRITEONLY = 0x00000200
DCI_ASYNC = 0x00000400
DCI_CAN_STRETCHX = 0x00001000
DCI_CAN_STRETCHY = 0x00002000
DCI_CAN_STRETCHXY = DCI_CAN_STRETCHX | DCI_CAN_STRETCHY
DCI_CAN_STRETCHXN = 0x00004000
DCI_CAN_STRETCHYN = 0x00008000
DCI_CAN_STRETCHXYN = DCI_CAN_STRETCHXN | DCI_CAN_STRETCHYN
DCI_CANOVERLAY = 0x00010000

# * Win32 RGNDATA structure.  This will be used for  cliplist info. passing.


NPRECTL = RECTL
RDH_RECTANGLES = 0x00000000

class tagRGNDATAHEADER(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('iType', DWORD),
        ('nCount', DWORD),
        ('nRgnSize', DWORD),
        ('rcBound', RECTL),
    ]


RGNDATAHEADER = tagRGNDATAHEADER


# size of structure
# Will be RDH_RECTANGLES
# # of clipping rectangles
# size of buffer -- can be zero
# bounding  rectangle for region
PRGNDATAHEADER = POINTER(RGNDATAHEADER)
NPRGNDATAHEADER = RGNDATAHEADER
LPRGNDATAHEADER = POINTER(RGNDATAHEADER)
LPCRGNDATAHEADER = POINTER(RGNDATAHEADER)

class tagRGNDATA(ctypes.Structure):
    _fields_ = [
        ('rdh', RGNDATAHEADER),
        ('Buffer', CHAR * 1),
    ]


RGNDATA = tagRGNDATA
PRGNDATA = POINTER(RGNDATA)
LPRGNDATA = POINTER(RGNDATA)
# return for callbacks
DCIRVAL = INT
# *************************************************************************
# *      input structures
# *************************************************************************

# * Used by a DCI client to provide input parameters for the
# * DCICREATEPRIMARYSURFACE escape.


class _DCICMD(ctypes.Structure):
    _fields_ = [
        ('dwCommand', DWORD),
        ('dwParam1', DWORD),
        ('dwParam2', DWORD),
        ('dwVersion', DWORD),
        ('dwReserved', DWORD),
    ]


DCICMD = _DCICMD



# * This structure is used by a DCI client to provide input parameters for
# * the DCICREATE... calls.  The fields that are actually relevant differ for
# * each of the three calls.  Details are in the DCI Spec chapter providing
# * the function specifications.


class _DCICREATEINPUT(ctypes.Structure):
    _fields_ = [
        ('cmd', DCICMD),
        ('dwCompression', DWORD),
        ('dwMask', DWORD * 3),
        ('dwWidth', DWORD),
        ('dwHeight', DWORD),
        ('dwDCICaps', DWORD),
        ('dwBitCount', DWORD),
        ('lpSurface', LPVOID),
    ]


DCICREATEINPUT = _DCICREATEINPUT
LPDCICREATEINPUT = POINTER(_DCICREATEINPUT)

class _DCISURFACEINFO(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwDCICaps', DWORD),
        ('dwCompression', DWORD),
        ('dwMask', DWORD * 3),
        ('dwWidth', DWORD),
        ('dwHeight', DWORD),
        ('lStride', LONG),
        ('dwBitCount', DWORD),
        ('dwOffSurface', ULONG_PTR),
        ('wSelSurface', WORD),
        ('wReserved', WORD),
        ('dwReserved1', DWORD),
        ('dwReserved2', DWORD),
        ('dwReserved3', DWORD),
        ('BeginAccess', CALLBACK(DCIRVAL, LPVOID, LPRECT)),
        ('EndAccess', CALLBACK(VOID, LPVOID)),
        ('DestroySurface', CALLBACK(VOID, LPVOID)),
    ]

DCISURFACEINFO = _DCISURFACEINFO
LPDCISURFACEINFO = POINTER(_DCISURFACEINFO)

# common header structure
# format of surface to be created
# for  nonstandard RGB (e.g. 5-6-5, RGB32)
# height of the surface to be created
# width of input surfaces
# capabilities of surface wanted
# bit depth of format to be created
# poINTer to an associated surface
# *************************************************************************
# *      surface info. structures
# *************************************************************************

# * This structure is used to return information about available support
# * during a DCIEnumSurface call.  It is also used to create a primary
# * surface, and as a member of the larger structures returned by the
# * offscreen and overlay calls.

# size of structure
# capability flags (stretch, etc.)
# format of surface to be created
# for BI_BITMASK surfaces
# width of surface
# height of surface
# distance in bytes betw. one pixel
# and the pixel directly below it
# Bits per pixel for this dwCompression
# offset of surface poINTer
# selector of surface poINTer
# reserved for provider
# reserved for DCIMAN
# reserved for future
# BeginAccess callback
# EndAcess callback
# Destroy surface callback

# * This structure is used by a DCI client to provide input parameters for the
# * DCIEnumSurface call.


class _DCIENUMINPUT(ctypes.Structure):
    _fields_ = [
        ('cmd', DCICMD),
        ('rSrc', RECT),
        ('rDst', RECT),
        ('EnumCallback', CALLBACK(VOID, LPDCISURFACEINFO, LPVOID)),
        ('lpContext', LPVOID),
    ]


DCIENUMINPUT = _DCIENUMINPUT
LPDCIENUMINPUT = POINTER(_DCIENUMINPUT)


class _DCIOFFSCREEN(ctypes.Structure):
    _fields_ = [
        ('dciInfo', DCISURFACEINFO),
        ('Draw', CALLBACK(DCIRVAL, LPVOID)),
        ('SetClipList', CALLBACK(DCIRVAL, LPVOID, LPRGNDATA)),
        ('SetDestination', CALLBACK(DCIRVAL, LPVOID, LPRECT, LPRECT)),

    ]
#
#         DCISURFACEINFO  dciInfo;                                                           /* surface info                  */
#         DCIRVAL (CALLBACK *Draw) (LPVOID);                                            /* copy to onscreen buffer   */
#         DCIRVAL (CALLBACK *SetClipList) (LPVOID, LPRGNDATA);          /* SetCliplist callback              */
#         DCIRVAL (CALLBACK *SetDestination) (LPVOID, LPRECT, LPRECT);  /* SetDestination callback       */
# } DCIOFFSCREEN, FAR *LPDCIOFFSCREEN;


# common header structure
# source rect. for stretch
# dest. rect. for stretch
# callback for supported formats

# * This structure must be allocated and returned by the DCI provider in
# * response to a DCICREATEPRIMARYSURFACE call.


# * This structure must be allocated and returned by the DCI provider in
# * response to a DCICREATEOFFSCREENSURFACE call.

# surface info
# copy to onscreen buffer
# SetCliplist callback
# SetDestination callback

# * This structure must be allocated and returned by the DCI provider in
# response
# * to a DCICREATEOVERLAYSURFACE call.

# surface info
# chromakey color value
# specifies valid bits of value
# DCI FOURCC def.s for extended DIB formats
YVU9 = mmioFOURCC('Y', 'V', 'U', '9')
Y411 = mmioFOURCC('Y', '4', '1', '1')
YUY2 = mmioFOURCC('Y', 'U', 'Y', '2')
YVYU = mmioFOURCC('Y', 'V', 'Y', 'U')
UYVY = mmioFOURCC('U', 'Y', 'V', 'Y')
Y211 = mmioFOURCC('Y', '2', '1', '1')
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# _INC_DCIDDI

__all__ = (
    'DCI_FAIL_GENERIC', 'DCI_1632_ACCESS', 'DCI_DWORDALIGN', 'DCI_VISIBLE',
    'DCI_ERR_INVALIDSTRETCH', 'DCICOMMAND', 'DCI_ERR_SURFACEISOBSCURED',
    'DCI_OK', 'Y411', 'DCI_SURFACE_TYPE', 'DCI_CAN_STRETCHXN', 'DCI_SUCCESS',
    'DCI_ERR_YALIGN', 'DCI_ERR_TOOBIGSIZE', 'DCI_STATUS_POINTERCHANGED',
    'DCI_STATUS_SURFACEINFOCHANGED', 'DCI_DWORDSIZE', 'DCI_ERR_OUTOFMEMORY',
    'DCI_STATUS_STRIDECHANGED', 'DCI_STATUS_FORMATCHANGED', 'DCI_VERSION',
    'DCI_ERR_INVALIDCLIPLIST', 'DCI_OFFSCREEN', 'DCI_STATUS_WASSTILLDRAWING',
    'DCI_ERR_CURRENTLYNOTAVAIL', 'DCI_ASYNC', 'DCI_ERR_INVALIDPOSITION',
    'DCICREATEOVERLAYSURFACE', 'DCI_ERR_HEIGHTALIGN', 'YVYU', 'DCIESCAPE',
    'DCI_ERR_XYALIGN', 'DCI_ERR_WIDTHALIGN', 'DCI_CAN_STRETCHX', 'Y211',
    'DCICREATEOFFSCREENSURFACE', 'DCI_ERR_TOOBIGHEIGHT', 'RDH_RECTANGLES',
    'DCI_FAIL_UNSUPPORTEDVERSION', 'DCI_FAIL_INVALIDSURFACE', 'DCI_CHROMAKEY',
    'DCI_ERR_UNSUPPORTEDFORMAT', 'DCI_ERR_INVALIDRECT', 'DCI_CAN_STRETCHXYN',
    'DCI_PRIMARY', 'DCI_ERR_TOOBIGWIDTH', 'DCI_CAN_STRETCHXY', 'DCI_OVERLAY',
    'DCI_WRITEONLY', 'DCI_CAN_STRETCHYN', 'DCICREATEPRIMARYSURFACE', 'UYVY',
    'DCI_ERR_XALIGN', 'DCI_FAIL_UNSUPPORTED', 'DCI_CANOVERLAY', 'YVU9',
    'DCI_ERR_UNSUPPORTEDMASK', 'DCIENUMSURFACE', 'DCI_CAN_STRETCHY', 'YUY2',
    'DCI_STATUS_CHROMAKEYCHANGED', 'LPDCIENUMINPUT', 'tagRGNDATAHEADER',
    '_DCICREATEINPUT', '_DCIENUMINPUT', 'LPDCICREATEINPUT', 'DCICMD',
    'tagRGNDATA', 'RGNDATA', '_DCICMD', 'DCIENUMINPUT', 'DCICREATEINPUT',
    'RGNDATAHEADER', 'RECTL', 'DCIRVAL', 'NPRECTL', 'PRGNDATA',
    'LPRGNDATAHEADER', 'NPRGNDATAHEADER', 'PRGNDATAHEADER',
    'LPCRGNDATAHEADER', 'PRECTL', 'LPRECTL', 'LPCRECTL'
)
