# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.


import ctypes
from .minwindef_h import MAX_PATH, LOBYTE
from .windef_h import RECTL, POINTS
from .wtypes_h import (
    POINTER,
    BOOL,
    LPVOID,
    HGDIOBJ,
    HMETAFILE,
    ULONG_PTR,
    CHAR,
    PSTR,
    RECT,
    POINT,
    LPSTR,
    LPWSTR,
    USHORT,
    WCHAR,
    HANDLE,
    SHORT,
    LPCSTR,
    LPCWSTR,
    SIZEL,
    POINTL,
    INT,
    ULONG,
    LONG,
    FLOAT,
    WORD,
    DWORD,
    BYTE,
    COLORREF,
    HDC,
    UINT,
    HRESULT,
)


# version 5.0
WINVER = 0x00000500

# 0
R2_BLACK = 0x00000001

# DPon
R2_NOTMERGEPEN = 0x00000002

# DPna
R2_MASKNOTPEN = 0x00000003

# PN
R2_NOTCOPYPEN = 0x00000004

# PDna
R2_MASKPENNOT = 0x00000005

# Dn
R2_NOT = 0x00000006

# DPx
R2_XORPEN = 0x00000007

# DPan
R2_NOTMASKPEN = 0x00000008

# DPa
R2_MASKPEN = 0x00000009

# DPxn
R2_NOTXORPEN = 0x0000000A

# D
R2_NOP = 0x0000000B

# DPno
R2_MERGENOTPEN = 0x0000000C

# P
R2_COPYPEN = 0x0000000D

# PDno
R2_MERGEPENNOT = 0x0000000E

# DPo
R2_MERGEPEN = 0x0000000F

# 1
R2_WHITE = 0x00000010
R2_LAST = 0x00000010

# dest = source
SRCCOPY = 0x00CC0020

# dest = source OR dest
SRCPAINT = 0x00EE0086

# dest = source AND dest
SRCAND = 0x008800C6

# dest = source XOR dest
SRCINVERT = 0x00660046

# dest = source AND (NOT dest )
SRCERASE = 0x00440328

# dest = (NOT source)
NOTSRCCOPY = 0x00330008

# dest = (NOT src) AND (NOT dest)
NOTSRCERASE = 0x001100A6

# dest = (source AND pattern)
MERGECOPY = 0x00C000CA

# dest = (NOT source) OR dest
MERGEPAINT = 0x00BB0226

# dest = pattern
PATCOPY = 0x00F00021

# dest = DPSnoo
PATPAINT = 0x00FB0A09

# dest = pattern XOR dest
PATINVERT = 0x005A0049

# dest = (NOT dest)
DSTINVERT = 0x00550009

# dest = BLACK
BLACKNESS = 0x00000042

# dest = WHITE
WHITENESS = 0x00FF0062

# Do not Mirror the bitmap in this call
NOMIRRORBITMAP = 0x80000000

# Include layered windows
CAPTUREBLT = 0x40000000


def MAKEROP4(fore, back):
    return DWORD(((back << 8) & 0xFF000000) | fore)


from .basetsd_h import LongToHandle # NOQA


GDI_ERROR = 0xFFFFFFFF
HGDI_ERROR = LongToHandle(0xFFFFFFFF)
ERROR = 0x00000000
NULLREGION = 0x00000001
SIMPLEREGION = 0x00000002
COMPLEXREGION = 0x00000003
RGN_ERROR = ERROR
RGN_AND = 0x00000001
RGN_OR = 0x00000002
RGN_XOR = 0x00000003
RGN_DIFF = 0x00000004
RGN_COPY = 0x00000005
RGN_MIN = RGN_AND
RGN_MAX = RGN_COPY
BLACKONWHITE = 0x00000001
WHITEONBLACK = 0x00000002
COLORONCOLOR = 0x00000003
HALFTONE = 0x00000004
MAXSTRETCHBLTMODE = 0x00000004
STRETCH_ANDSCANS = BLACKONWHITE
STRETCH_ORSCANS = WHITEONBLACK
STRETCH_DELETESCANS = COLORONCOLOR
STRETCH_HALFTONE = HALFTONE
ALTERNATE = 0x00000001
WINDING = 0x00000002
POLYFILL_LAST = 0x00000002

# Right to left
LAYOUT_RTL = 0x00000001

# Bottom to top
LAYOUT_BTT = 0x00000002

# Vertical before horizontal
LAYOUT_VBH = 0x00000004
LAYOUT_ORIENTATIONMASK = LAYOUT_RTL | LAYOUT_BTT | LAYOUT_VBH
LAYOUT_BITMAPORIENTATIONPRESERVED = 0x00000008
TA_NOUPDATECP = 0x00000000
TA_UPDATECP = 0x00000001
TA_LEFT = 0x00000000
TA_RIGHT = 0x00000002
TA_CENTER = 0x00000006
TA_TOP = 0x00000000
TA_BOTTOM = 0x00000008
TA_BASELINE = 0x00000018
TA_RTLREADING = 0x00000100
TA_MASK = (TA_BASELINE+TA_CENTER+TA_UPDATECP+TA_RTLREADING)
VTA_BASELINE = TA_BASELINE
VTA_LEFT = TA_BOTTOM
VTA_RIGHT = TA_TOP
VTA_CENTER = TA_CENTER
VTA_BOTTOM = TA_RIGHT
VTA_TOP = TA_LEFT
ETO_OPAQUE = 0x00000002
ETO_CLIPPED = 0x00000004
ETO_GLYPH_INDEX = 0x00000010
ETO_RTLREADING = 0x00000080
ETO_NUMERICSLOCAL = 0x00000400
ETO_NUMERICSLATIN = 0x00000800
ETO_IGNORELANGUAGE = 0x00001000
ETO_PDY = 0x00002000
ETO_REVERSE_INDEX_MAP = 0x00010000
ASPECT_FILTERING = 0x00000001
DCB_RESET = 0x00000001
DCB_ACCUMULATE = 0x00000002
DCB_DIRTY = DCB_ACCUMULATE
DCB_SET = DCB_RESET | DCB_ACCUMULATE
DCB_ENABLE = 0x00000004
DCB_DISABLE = 0x00000008
META_SETBKCOLOR = 0x00000201
META_SETBKMODE = 0x00000102
META_SETMAPMODE = 0x00000103
META_SETROP2 = 0x00000104
META_SETRELABS = 0x00000105
META_SETPOLYFILLMODE = 0x00000106
META_SETSTRETCHBLTMODE = 0x00000107
META_SETTEXTCHAREXTRA = 0x00000108
META_SETTEXTCOLOR = 0x00000209
META_SETTEXTJUSTIFICATION = 0x0000020A
META_SETWINDOWORG = 0x0000020B
META_SETWINDOWEXT = 0x0000020C
META_SETVIEWPORTORG = 0x0000020D
META_SETVIEWPORTEXT = 0x0000020E
META_OFFSETWINDOWORG = 0x0000020F
META_SCALEWINDOWEXT = 0x00000410
META_OFFSETVIEWPORTORG = 0x00000211
META_SCALEVIEWPORTEXT = 0x00000412
META_LINETO = 0x00000213
META_MOVETO = 0x00000214
META_EXCLUDECLIPRECT = 0x00000415
META_INTERSECTCLIPRECT = 0x00000416
META_ARC = 0x00000817
META_ELLIPSE = 0x00000418
META_FLOODFILL = 0x00000419
META_PIE = 0x0000081A
META_RECTANGLE = 0x0000041B
META_ROUNDRECT = 0x0000061C
META_PATBLT = 0x0000061D
META_SAVEDC = 0x0000001E
META_SETPIXEL = 0x0000041F
META_OFFSETCLIPRGN = 0x00000220
META_TEXTOUT = 0x00000521
META_BITBLT = 0x00000922
META_STRETCHBLT = 0x00000B23
META_POLYGON = 0x00000324
META_POLYLINE = 0x00000325
META_ESCAPE = 0x00000626
META_RESTOREDC = 0x00000127
META_FILLREGION = 0x00000228
META_FRAMEREGION = 0x00000429
META_INVERTREGION = 0x0000012A
META_PAINTREGION = 0x0000012B
META_SELECTCLIPREGION = 0x0000012C
META_SELECTOBJECT = 0x0000012D
META_SETTEXTALIGN = 0x0000012E
META_CHORD = 0x00000830
META_SETMAPPERFLAGS = 0x00000231
META_EXTTEXTOUT = 0x00000A32
META_SETDIBTODEV = 0x00000D33
META_SELECTPALETTE = 0x00000234
META_REALIZEPALETTE = 0x00000035
META_ANIMATEPALETTE = 0x00000436
META_SETPALENTRIES = 0x00000037
META_POLYPOLYGON = 0x00000538
META_RESIZEPALETTE = 0x00000139
META_DIBBITBLT = 0x00000940
META_DIBSTRETCHBLT = 0x00000B41
META_DIBCREATEPATTERNBRUSH = 0x00000142
META_STRETCHDIB = 0x00000F43
META_EXTFLOODFILL = 0x00000548
META_SETLAYOUT = 0x00000149
META_DELETEOBJECT = 0x000001F0
META_CREATEPALETTE = 0x000000F7
META_CREATEPATTERNBRUSH = 0x000001F9
META_CREATEPENINDIRECT = 0x000002FA
META_CREATEFONTINDIRECT = 0x000002FB
META_CREATEBRUSHINDIRECT = 0x000002FC
META_CREATEREGION = 0x000006FF


class _DRAWPATRECT(ctypes.Structure):
    _fields_ = [
        ('ptPosition', POINT),
        ('ptSize', POINT),
        ('wStyle', WORD),
        ('wPattern', WORD),
    ]


DRAWPATRECT = _DRAWPATRECT
PDRAWPATRECT = POINTER(_DRAWPATRECT)


NEWFRAME = 0x00000001
ABORTDOC = 0x00000002
NEXTBAND = 0x00000003
SETCOLORTABLE = 0x00000004
GETCOLORTABLE = 0x00000005
FLUSHOUTPUT = 0x00000006
DRAFTMODE = 0x00000007
QUERYESCSUPPORT = 0x00000008
SETABORTPROC = 0x00000009
STARTDOC = 0x0000000A
ENDDOC = 0x0000000B
GETPHYSPAGESIZE = 0x0000000C
GETPRINTINGOFFSET = 0x0000000D
GETSCALINGFACTOR = 0x0000000E
MFCOMMENT = 0x0000000F
GETPENWIDTH = 0x00000010
SETCOPYCOUNT = 0x00000011
SELECTPAPERSOURCE = 0x00000012
DEVICEDATA = 0x00000013
PASSTHROUGH = 0x00000013
GETTECHNOLGY = 0x00000014
GETTECHNOLOGY = 0x00000014
SETLINECAP = 0x00000015
SETLINEJOIN = 0x00000016
SETMITERLIMIT = 0x00000017
BANDINFO = 0x00000018
DRAWPATTERNRECT = 0x00000019
GETVECTORPENSIZE = 0x0000001A
GETVECTORBRUSHSIZE = 0x0000001B
ENABLEDUPLEX = 0x0000001C
GETSETPAPERBINS = 0x0000001D
GETSETPRINTORIENT = 0x0000001E
ENUMPAPERBINS = 0x0000001F
SETDIBSCALING = 0x00000020
EPSPRINTING = 0x00000021
ENUMPAPERMETRICS = 0x00000022
GETSETPAPERMETRICS = 0x00000023
POSTSCRIPT_DATA = 0x00000025
POSTSCRIPT_IGNORE = 0x00000026
MOUSETRAILS = 0x00000027
GETDEVICEUNITS = 0x0000002A
GETEXTENDEDTEXTMETRICS = 0x00000100
GETEXTENTTABLE = 0x00000101
GETPAIRKERNTABLE = 0x00000102
GETTRACKKERNTABLE = 0x00000103
EXTTEXTOUT = 0x00000200
GETFACENAME = 0x00000201
DOWNLOADFACE = 0x00000202
ENABLERELATIVEWIDTHS = 0x00000300
ENABLEPAIRKERNING = 0x00000301
SETKERNTRACK = 0x00000302
SETALLJUSTVALUES = 0x00000303
SETCHARSET = 0x00000304
STRETCHBLT = 0x00000800
METAFILE_DRIVER = 0x00000801
GETSETSCREENPARAMS = 0x00000C00
QUERYDIBSUPPORT = 0x00000C01
BEGIN_PATH = 0x00001000
CLIP_TO_PATH = 0x00001001
END_PATH = 0x00001002
EXT_DEVICE_CAPS = 0x00001003
RESTORE_CTM = 0x00001004
SAVE_CTM = 0x00001005
SET_ARC_DIRECTION = 0x00001006
SET_BACKGROUND_COLOR = 0x00001007
SET_POLY_MODE = 0x00001008
SET_SCREEN_ANGLE = 0x00001009
SET_SPREAD = 0x0000100A
TRANSFORM_CTM = 0x0000100B
SET_CLIP_BOX = 0x0000100C
SET_BOUNDS = 0x0000100D
SET_MIRROR_MODE = 0x0000100E
OPENCHANNEL = 0x0000100E
DOWNLOADHEADER = 0x0000100F
CLOSECHANNEL = 0x00001010
POSTSCRIPT_PASSTHROUGH = 0x00001013
ENCAPSULATED_POSTSCRIPT = 0x00001014

# new escape for NT5 pscript driver
POSTSCRIPT_IDENTIFY = 0x00001015

# new escape for NT5 pscript driver
POSTSCRIPT_INJECTION = 0x00001016
CHECKJPEGFORMAT = 0x00001017
CHECKPNGFORMAT = 0x00001018

# new escape for NT5 pscript driver
GET_PS_FEATURESETTING = 0x00001019

# private escape
GDIPLUS_TS_QUERYVER = 0x0000101A

# private escape
GDIPLUS_TS_RECORD = 0x0000101B
MILCORE_TS_QUERYVER_RESULT_FALSE = 0x00000000
MILCORE_TS_QUERYVER_RESULT_TRUE = 0x7FFFFFFF

# new escape for NT5 pscript driver
SPCLPASSTHROUGH2 = 0x000011D8
PSIDENT_GDICENTRIC = 0x00000000
PSIDENT_PSCENTRIC = 0x00000001


class _PSINJECTDATA(ctypes.Structure):
    _fields_ = [
        # number of raw data bytes (NOT including this header)
        ('DataBytes', DWORD),
        # injection point
        ('InjectionPoint', WORD),
        # page number to apply the injection
        ('PageNumber', WORD),
        # Followed by raw data to be injected
    ]


PSINJECTDATA = _PSINJECTDATA
PPSINJECTDATA = POINTER(_PSINJECTDATA)


PSINJECT_BEGINSTREAM = 0x00000001
PSINJECT_PSADOBE = 0x00000002
PSINJECT_PAGESATEND = 0x00000003
PSINJECT_PAGES = 0x00000004
PSINJECT_DOCNEEDEDRES = 0x00000005
PSINJECT_DOCSUPPLIEDRES = 0x00000006
PSINJECT_PAGEORDER = 0x00000007
PSINJECT_ORIENTATION = 0x00000008
PSINJECT_BOUNDINGBOX = 0x00000009
PSINJECT_DOCUMENTPROCESSCOLORS = 0x0000000A
PSINJECT_COMMENTS = 0x0000000B
PSINJECT_BEGINDEFAULTS = 0x0000000C
PSINJECT_ENDDEFAULTS = 0x0000000D
PSINJECT_BEGINPROLOG = 0x0000000E
PSINJECT_ENDPROLOG = 0x0000000F
PSINJECT_BEGINSETUP = 0x00000010
PSINJECT_ENDSETUP = 0x00000011
PSINJECT_TRAILER = 0x00000012
PSINJECT_EOF = 0x00000013
PSINJECT_ENDSTREAM = 0x00000014
PSINJECT_DOCUMENTPROCESSCOLORSATEND = 0x00000015
PSINJECT_PAGENUMBER = 0x00000064
PSINJECT_BEGINPAGESETUP = 0x00000065
PSINJECT_ENDPAGESETUP = 0x00000066
PSINJECT_PAGETRAILER = 0x00000067
PSINJECT_PLATECOLOR = 0x00000068
PSINJECT_SHOWPAGE = 0x00000069
PSINJECT_PAGEBBOX = 0x0000006A
PSINJECT_ENDPAGECOMMENTS = 0x0000006B
PSINJECT_VMSAVE = 0x000000C8
PSINJECT_VMRESTORE = 0x000000C9
FEATURESETTING_NUP = 0x00000000
FEATURESETTING_OUTPUT = 0x00000001
FEATURESETTING_PSLEVEL = 0x00000002
FEATURESETTING_CUSTPAPER = 0x00000003
FEATURESETTING_MIRROR = 0x00000004
FEATURESETTING_NEGATIVE = 0x00000005
FEATURESETTING_PROTOCOL = 0x00000006
FEATURESETTING_PRIVATE_BEGIN = 0x00001000
FEATURESETTING_PRIVATE_END = 0x00001FFF


class _PSFEATURE_OUTPUT(ctypes.Structure):
    _fields_ = [
        ('bPageIndependent', BOOL),
        ('bSetPageDevice', BOOL),
    ]


PSFEATURE_OUTPUT = _PSFEATURE_OUTPUT
PPSFEATURE_OUTPUT = POINTER(_PSFEATURE_OUTPUT)


class _PSFEATURE_CUSTPAPER(ctypes.Structure):
    _fields_ = [
        ('lOrientation', LONG),
        ('lWidth', LONG),
        ('lHeight', LONG),
        ('lWidthOffset', LONG),
        ('lHeightOffset', LONG),
    ]


PSFEATURE_CUSTPAPER = _PSFEATURE_CUSTPAPER
PPSFEATURE_CUSTPAPER = POINTER(_PSFEATURE_CUSTPAPER)


PSPROTOCOL_ASCII = 0x00000000
PSPROTOCOL_BCP = 0x00000001
PSPROTOCOL_TBCP = 0x00000002
PSPROTOCOL_BINARY = 0x00000003
QDI_SETDIBITS = 0x00000001
QDI_GETDIBITS = 0x00000002
QDI_DIBTOSCREEN = 0x00000004
QDI_STRETCHDIB = 0x00000008
SP_NOTREPORTED = 0x00004000
SP_ERROR = -1
SP_APPABORT = -2
SP_USERABORT = -3
SP_OUTOFDISK = -4
SP_OUTOFMEMORY = -5
PR_JOBSTATUS = 0x00000000
OBJ_PEN = 0x00000001
OBJ_BRUSH = 0x00000002
OBJ_DC = 0x00000003
OBJ_METADC = 0x00000004
OBJ_PAL = 0x00000005
OBJ_FONT = 0x00000006
OBJ_BITMAP = 0x00000007
OBJ_REGION = 0x00000008
OBJ_METAFILE = 0x00000009
OBJ_MEMDC = 0x0000000A
OBJ_EXTPEN = 0x0000000B
OBJ_ENHMETADC = 0x0000000C
OBJ_ENHMETAFILE = 0x0000000D
OBJ_COLORSPACE = 0x0000000E
GDI_OBJ_LAST = OBJ_COLORSPACE
MWT_IDENTITY = 0x00000001
MWT_LEFTMULTIPLY = 0x00000002
MWT_RIGHTMULTIPLY = 0x00000003
MWT_MIN = MWT_IDENTITY
MWT_MAX = MWT_RIGHTMULTIPLY


class tagXFORM(ctypes.Structure):
    _fields_ = [
        ('eM11', FLOAT),
        ('eM12', FLOAT),
        ('eM21', FLOAT),
        ('eM22', FLOAT),
        ('eDx', FLOAT),
        ('eDy', FLOAT),
    ]


XFORM = tagXFORM
PXFORM = POINTER(tagXFORM)


class tagBITMAP(ctypes.Structure):
    _fields_ = [
        ('bmType', LONG),
        ('bmWidth', LONG),
        ('bmHeight', LONG),
        ('bmWidthBytes', LONG),
        ('bmPlanes', WORD),
        ('bmBitsPixel', WORD),
        ('bmBits', LPVOID),
    ]


BITMAP = tagBITMAP
PBITMAP = POINTER(tagBITMAP)


class tagRGBTRIPLE(ctypes.Structure):
    _fields_ = [
        ('rgbtBlue', BYTE),
        ('rgbtGreen', BYTE),
        ('rgbtRed', BYTE),
    ]


RGBTRIPLE = tagRGBTRIPLE
PRGBTRIPLE = POINTER(tagRGBTRIPLE)


class tagRGBQUAD(ctypes.Structure):
    _fields_ = [
        ('rgbBlue', BYTE),
        ('rgbGreen', BYTE),
        ('rgbRed', BYTE),
        ('rgbReserved', BYTE),
    ]


RGBQUAD = tagRGBQUAD


CS_ENABLE = 0x00000001
CS_DISABLE = 0x00000002
CS_DELETE_TRANSFORM = 0x00000003
LCS_SIGNATURE = 'PSOC'
LCS_sRGB = 'sRGB'

# Windows default color space
LCS_WINDOWS_COLOR_SPACE = 'Win '
LCSCSTYPE = LONG
LCS_CALIBRATED_RGB = 0x00000000
LCSGAMUTMATCH = LONG
LCS_GM_BUSINESS = 0x00000001
LCS_GM_GRAPHICS = 0x00000002
LCS_GM_IMAGES = 0x00000004
LCS_GM_ABS_COLORIMETRIC = 0x00000008
CM_OUT_OF_GAMUT = 0x000000FF
CM_IN_GAMUT = 0x00000000
ICM_ADDPROFILE = 0x00000001
ICM_DELETEPROFILE = 0x00000002
ICM_QUERYPROFILE = 0x00000003
ICM_SETDEFAULTPROFILE = 0x00000004
ICM_REGISTERICMATCHER = 0x00000005
ICM_UNREGISTERICMATCHER = 0x00000006
ICM_QUERYMATCH = 0x00000007


def GetKValue(cmyk):
    return BYTE(cmyk)


def GetYValue(cmyk):
    return BYTE(cmyk >> 8)


def GetMValue(cmyk):
    return BYTE(cmyk >> 16)


def GetCValue(cmyk):
    return BYTE(cmyk >> 24)


def CMYK(c, m, y, k):
    return COLORREF(k | (y << 8) | (m << 16) | (c << 24))


FXPT16DOT16 = LONG
FXPT2DOT30 = LONG


class tagCIEXYZ(ctypes.Structure):
    _fields_ = [
        ('ciexyzX', FXPT2DOT30),
        ('ciexyzY', FXPT2DOT30),
        ('ciexyzZ', FXPT2DOT30),
    ]


CIEXYZ = tagCIEXYZ


class tagICEXYZTRIPLE(ctypes.Structure):
    _fields_ = [
        ('ciexyzRed', CIEXYZ),
        ('ciexyzGreen', CIEXYZ),
        ('ciexyzBlue', CIEXYZ),
    ]


CIEXYZTRIPLE = tagICEXYZTRIPLE


class tagLOGCOLORSPACEA(ctypes.Structure):
    _fields_ = [
        ('lcsSignature', DWORD),
        ('lcsVersion', DWORD),
        ('lcsSize', DWORD),
        ('lcsCSType', LCSCSTYPE),
        ('lcsIntent', LCSGAMUTMATCH),
        ('lcsEndpoints', CIEXYZTRIPLE),
        ('lcsGammaRed', DWORD),
        ('lcsGammaGreen', DWORD),
        ('lcsGammaBlue', DWORD),
        ('lcsFilename', CHAR * MAX_PATH),
    ]


LOGCOLORSPACEA = tagLOGCOLORSPACEA
LPLOGCOLORSPACEA = POINTER(tagLOGCOLORSPACEA)


class tagLOGCOLORSPACEW(ctypes.Structure):
    _fields_ = [
        ('lcsSignature', DWORD),
        ('lcsVersion', DWORD),
        ('lcsSize', DWORD),
        ('lcsCSType', LCSCSTYPE),
        ('lcsIntent', LCSGAMUTMATCH),
        ('lcsEndpoints', CIEXYZTRIPLE),
        ('lcsGammaRed', DWORD),
        ('lcsGammaGreen', DWORD),
        ('lcsGammaBlue', DWORD),
        ('lcsFilename', WCHAR * MAX_PATH),
    ]


LOGCOLORSPACEW = tagLOGCOLORSPACEW
LPLOGCOLORSPACEW = POINTER(tagLOGCOLORSPACEW)


class tagBITMAPCOREHEADER(ctypes.Structure):
    _fields_ = [
        # used to get to color table
        ('bcSize', DWORD),
        ('bcWidth', WORD),
        ('bcHeight', WORD),
        ('bcPlanes', WORD),
        ('bcBitCount', WORD),
    ]


BITMAPCOREHEADER = tagBITMAPCOREHEADER
PBITMAPCOREHEADER = POINTER(tagBITMAPCOREHEADER)


class tagBITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ('biSize', DWORD),
        ('biWidth', LONG),
        ('biHeight', LONG),
        ('biPlanes', WORD),
        ('biBitCount', WORD),
        ('biCompression', DWORD),
        ('biSizeImage', DWORD),
        ('biXPelsPerMeter', LONG),
        ('biYPelsPerMeter', LONG),
        ('biClrUsed', DWORD),
        ('biClrImportant', DWORD),
    ]


BITMAPINFOHEADER = tagBITMAPINFOHEADER
PBITMAPINFOHEADER = POINTER(tagBITMAPINFOHEADER)


class BITMAPV4HEADER(ctypes.Structure):
    _fields_ = [
        ('bV4Size', DWORD),
        ('bV4Width', LONG),
        ('bV4Height', LONG),
        ('bV4Planes', WORD),
        ('bV4BitCount', WORD),
        ('bV4V4Compression', DWORD),
        ('bV4SizeImage', DWORD),
        ('bV4XPelsPerMeter', LONG),
        ('bV4YPelsPerMeter', LONG),
        ('bV4ClrUsed', DWORD),
        ('bV4ClrImportant', DWORD),
        ('bV4RedMask', DWORD),
        ('bV4GreenMask', DWORD),
        ('bV4BlueMask', DWORD),
        ('bV4AlphaMask', DWORD),
        ('bV4CSType', DWORD),
        ('bV4Endpoints', CIEXYZTRIPLE),
        ('bV4GammaRed', DWORD),
        ('bV4GammaGreen', DWORD),
        ('bV4GammaBlue', DWORD),
    ]


PBITMAPV4HEADER = POINTER(BITMAPV4HEADER)


class BITMAPV5HEADER(ctypes.Structure):
    _fields_ = [
        ('bV5Size', DWORD),
        ('bV5Width', LONG),
        ('bV5Height', LONG),
        ('bV5Planes', WORD),
        ('bV5BitCount', WORD),
        ('bV5Compression', DWORD),
        ('bV5SizeImage', DWORD),
        ('bV5XPelsPerMeter', LONG),
        ('bV5YPelsPerMeter', LONG),
        ('bV5ClrUsed', DWORD),
        ('bV5ClrImportant', DWORD),
        ('bV5RedMask', DWORD),
        ('bV5GreenMask', DWORD),
        ('bV5BlueMask', DWORD),
        ('bV5AlphaMask', DWORD),
        ('bV5CSType', DWORD),
        ('bV5Endpoints', CIEXYZTRIPLE),
        ('bV5GammaRed', DWORD),
        ('bV5GammaGreen', DWORD),
        ('bV5GammaBlue', DWORD),
        ('bV5Intent', DWORD),
        ('bV5ProfileData', DWORD),
        ('bV5ProfileSize', DWORD),
        ('bV5Reserved', DWORD),
    ]


PBITMAPV5HEADER = POINTER(BITMAPV5HEADER)


PROFILE_LINKED = 'LINK'
PROFILE_EMBEDDED = 'MBED'
BI_RGB = 0x00000000
BI_RLE8 = 0x00000001
BI_RLE4 = 0x00000002
BI_BITFIELDS = 0x00000003
BI_JPEG = 0x00000004
BI_PNG = 0x00000005


# noinspection PyTypeChecker
class tagBITMAPINFO(ctypes.Structure):
    _fields_ = [
        ('bmiHeader', BITMAPINFOHEADER),
        ('bmiColors', RGBQUAD * 1),
    ]


BITMAPINFO = tagBITMAPINFO
PBITMAPINFO = POINTER(tagBITMAPINFO)


# noinspection PyTypeChecker
class tagBITMAPCOREINFO(ctypes.Structure):
    _fields_ = [
        ('bmciHeader', BITMAPCOREHEADER),
        ('bmciColors', RGBTRIPLE * 1),
    ]


BITMAPCOREINFO = tagBITMAPCOREINFO
PBITMAPCOREINFO = POINTER(tagBITMAPCOREINFO)


class tagBITMAPFILEHEADER(ctypes.Structure):
    _fields_ = [
        ('bfType', WORD),
        ('bfSize', DWORD),
        ('bfReserved1', WORD),
        ('bfReserved2', WORD),
        ('bfOffBits', DWORD),
    ]


BITMAPFILEHEADER = tagBITMAPFILEHEADER
PBITMAPFILEHEADER = POINTER(tagBITMAPFILEHEADER)


def MAKEPOINTS(l):
    return l


# noinspection PyTypeChecker
class tagFONTSIGNATURE(ctypes.Structure):
    _fields_ = [
        ('fsUsb', DWORD * 4),
        ('fsCsb', DWORD * 2),
    ]


FONTSIGNATURE = tagFONTSIGNATURE
PFONTSIGNATURE = POINTER(tagFONTSIGNATURE)


class tagCHARSETINFO(ctypes.Structure):
    _fields_ = [
        ('ciCharset', UINT),
        ('ciACP', UINT),
        ('fs', FONTSIGNATURE),
    ]


CHARSETINFO = tagCHARSETINFO
PCHARSETINFO = POINTER(tagCHARSETINFO)


TCI_SRCCHARSET = 0x00000001
TCI_SRCCODEPAGE = 0x00000002
TCI_SRCFONTSIG = 0x00000003
TCI_SRCLOCALE = 0x00001000


# noinspection PyTypeChecker
class tagLOCALESIGNATURE(ctypes.Structure):
    _fields_ = [
        ('lsUsb', DWORD * 4),
        ('lsCsbDefault', DWORD * 2),
        ('lsCsbSupported', DWORD * 2),
    ]


LOCALESIGNATURE = tagLOCALESIGNATURE
PLOCALESIGNATURE = POINTER(tagLOCALESIGNATURE)


# noinspection PyTypeChecker
class tagHANDLETABLE(ctypes.Structure):
    _fields_ = [
        ('objectHandle', HGDIOBJ * 1),
    ]


HANDLETABLE = tagHANDLETABLE
PHANDLETABLE = POINTER(tagHANDLETABLE)


# noinspection PyTypeChecker
class tagMETARECORD(ctypes.Structure):
    _fields_ = [
        ('rdSize', DWORD),
        ('rdFunction', WORD),
        ('rdParm', WORD * 1),
    ]


METARECORD = tagMETARECORD


class tagMETAFILEPICT(ctypes.Structure):
    _fields_ = [
        ('mm', LONG),
        ('xExt', LONG),
        ('yExt', LONG),
        ('hMF', HMETAFILE),
    ]


METAFILEPICT = tagMETAFILEPICT


class tagMETAHEADER(ctypes.Structure):
    _fields_ = [
        ('mtType', WORD),
        ('mtHeaderSize', WORD),
        ('mtVersion', WORD),
        ('mtSize', DWORD),
        ('mtNoObjects', WORD),
        ('mtMaxRecord', DWORD),
        ('mtNoParameters', WORD),
    ]


METAHEADER = tagMETAHEADER


# noinspection PyTypeChecker
class tagENHMETARECORD(ctypes.Structure):
    _fields_ = [
        # Record type EMR_XXX
        ('iType', DWORD),
        # Record size in bytes
        ('nSize', DWORD),
        # Parameters
        ('dParm', DWORD * 1),
    ]


ENHMETARECORD = tagENHMETARECORD
PENHMETARECORD = POINTER(tagENHMETARECORD)
LPENHMETARECORD = POINTER(tagENHMETARECORD)


class tagENHMETAHEADER(ctypes.Structure):
    _fields_ = [
        # Record typeEMR_HEADER
        ('iType', DWORD),
        # Record size in bytes.  This may be greater
        ('nSize', DWORD),
        # than the sizeof(ENHMETAHEADER).
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Inclusive-inclusive Picture Frame of metafile in .01 mm units
        ('rclFrame', RECTL),
        # Signature.  Must be ENHMETA_SIGNATURE.
        ('dSignature', DWORD),
        # Version number
        ('nVersion', DWORD),
        # Size of the metafile in bytes
        ('nBytes', DWORD),
        # Number of records in the metafile
        ('nRecords', DWORD),
        # Number of handles in the handle table
        ('nHandles', WORD),
        # Handle index zero is reserved.
        # Reserved.  Must be zero.
        ('sReserved', WORD),
        # Number of chars in the unicode description string
        ('nDescription', DWORD),
        # This is 0 if there is no description string
        # Offset to the metafile description record.
        ('offDescription', DWORD),
        # This is 0 if there is no description string
        # Number of entries in the metafile palette.
        ('nPalEntries', DWORD),
        # Size of the reference device in pels
        ('szlDevice', SIZEL),
        # Size of the reference device in millimeters
        ('szlMillimeters', SIZEL),
        # Size of PIXELFORMATDESCRIPTOR information
        ('cbPixelFormat', DWORD),
        # This is 0 if no pixel format is set
        # Offset to PIXELFORMATDESCRIPTOR
        ('offPixelFormat', DWORD),
        # This is 0 if no pixel format is set
        # TRUE if OpenGL commands are present in
        ('bOpenGL', DWORD),
        # the metafile, otherwise FALSE
        # Size of the reference device in micrometers
        ('szlMicrometers', SIZEL),
    ]


ENHMETAHEADER = tagENHMETAHEADER
PENHMETAHEADER = POINTER(tagENHMETAHEADER)
LPENHMETAHEADER = POINTER(tagENHMETAHEADER)


TMPF_FIXED_PITCH = 0x00000001
TMPF_VECTOR = 0x00000002
TMPF_DEVICE = 0x00000008
TMPF_TRUETYPE = 0x00000004


class tagTEXTMETRICA(ctypes.Structure):
    _fields_ = [
        ('tmHeight', LONG),
        ('tmAscent', LONG),
        ('tmDescent', LONG),
        ('tmInternalLeading', LONG),
        ('tmExternalLeading', LONG),
        ('tmAveCharWidth', LONG),
        ('tmMaxCharWidth', LONG),
        ('tmWeight', LONG),
        ('tmOverhang', LONG),
        ('tmDigitizedAspectX', LONG),
        ('tmDigitizedAspectY', LONG),
        ('tmFirstChar', BYTE),
        ('tmLastChar', BYTE),
        ('tmDefaultChar', BYTE),
        ('tmBreakChar', BYTE),
        ('tmItalic', BYTE),
        ('tmUnderlined', BYTE),
        ('tmStruckOut', BYTE),
        ('tmPitchAndFamily', BYTE),
        ('tmCharSet', BYTE),
    ]


TEXTMETRICA = tagTEXTMETRICA
PTEXTMETRICA = POINTER(tagTEXTMETRICA)


class tagTEXTMETRICW(ctypes.Structure):
    _fields_ = [
        ('tmHeight', LONG),
        ('tmAscent', LONG),
        ('tmDescent', LONG),
        ('tmInternalLeading', LONG),
        ('tmExternalLeading', LONG),
        ('tmAveCharWidth', LONG),
        ('tmMaxCharWidth', LONG),
        ('tmWeight', LONG),
        ('tmOverhang', LONG),
        ('tmDigitizedAspectX', LONG),
        ('tmDigitizedAspectY', LONG),
        ('tmFirstChar', WCHAR),
        ('tmLastChar', WCHAR),
        ('tmDefaultChar', WCHAR),
        ('tmBreakChar', WCHAR),
        ('tmItalic', BYTE),
        ('tmUnderlined', BYTE),
        ('tmStruckOut', BYTE),
        ('tmPitchAndFamily', BYTE),
        ('tmCharSet', BYTE),
    ]


TEXTMETRICW = tagTEXTMETRICW
PTEXTMETRICW = POINTER(tagTEXTMETRICW)


NTM_REGULAR = 0x00000040
NTM_BOLD = 0x00000020
NTM_ITALIC = 0x00000001
NTM_NONNEGATIVE_AC = 0x00010000
NTM_PS_OPENTYPE = 0x00020000
NTM_TT_OPENTYPE = 0x00040000
NTM_MULTIPLEMASTER = 0x00080000
NTM_TYPE1 = 0x00100000
NTM_DSIG = 0x00200000


class tagNEWTEXTMETRICA(ctypes.Structure):
    _fields_ = [
        ('tmHeight', LONG),
        ('tmAscent', LONG),
        ('tmDescent', LONG),
        ('tmInternalLeading', LONG),
        ('tmExternalLeading', LONG),
        ('tmAveCharWidth', LONG),
        ('tmMaxCharWidth', LONG),
        ('tmWeight', LONG),
        ('tmOverhang', LONG),
        ('tmDigitizedAspectX', LONG),
        ('tmDigitizedAspectY', LONG),
        ('tmFirstChar', BYTE),
        ('tmLastChar', BYTE),
        ('tmDefaultChar', BYTE),
        ('tmBreakChar', BYTE),
        ('tmItalic', BYTE),
        ('tmUnderlined', BYTE),
        ('tmStruckOut', BYTE),
        ('tmPitchAndFamily', BYTE),
        ('tmCharSet', BYTE),
        ('ntmFlags', DWORD),
        ('ntmSizeEM', UINT),
        ('ntmCellHeight', UINT),
        ('ntmAvgWidth', UINT),
    ]


NEWTEXTMETRICA = tagNEWTEXTMETRICA
PNEWTEXTMETRICA = POINTER(tagNEWTEXTMETRICA)


class tagNEWTEXTMETRICW(ctypes.Structure):
    _fields_ = [
        ('tmHeight', LONG),
        ('tmAscent', LONG),
        ('tmDescent', LONG),
        ('tmInternalLeading', LONG),
        ('tmExternalLeading', LONG),
        ('tmAveCharWidth', LONG),
        ('tmMaxCharWidth', LONG),
        ('tmWeight', LONG),
        ('tmOverhang', LONG),
        ('tmDigitizedAspectX', LONG),
        ('tmDigitizedAspectY', LONG),
        ('tmFirstChar', WCHAR),
        ('tmLastChar', WCHAR),
        ('tmDefaultChar', WCHAR),
        ('tmBreakChar', WCHAR),
        ('tmItalic', BYTE),
        ('tmUnderlined', BYTE),
        ('tmStruckOut', BYTE),
        ('tmPitchAndFamily', BYTE),
        ('tmCharSet', BYTE),
        ('ntmFlags', DWORD),
        ('ntmSizeEM', UINT),
        ('ntmCellHeight', UINT),
        ('ntmAvgWidth', UINT),
    ]


NEWTEXTMETRICW = tagNEWTEXTMETRICW
PNEWTEXTMETRICW = POINTER(tagNEWTEXTMETRICW)


class tagNEWTEXTMETRICEXA(ctypes.Structure):
    _fields_ = [
        ('ntmTm', NEWTEXTMETRICA),
        ('ntmFontSig', FONTSIGNATURE),
    ]


NEWTEXTMETRICEXA = tagNEWTEXTMETRICEXA


class tagNEWTEXTMETRICEXW(ctypes.Structure):
    _fields_ = [
        ('ntmTm', NEWTEXTMETRICW),
        ('ntmFontSig', FONTSIGNATURE),
    ]


NEWTEXTMETRICEXW = tagNEWTEXTMETRICEXW


class tagPELARRAY(ctypes.Structure):
    _fields_ = [
        ('paXCount', LONG),
        ('paYCount', LONG),
        ('paXExt', LONG),
        ('paYExt', LONG),
        ('paRGBs', BYTE),
    ]


PELARRAY = tagPELARRAY
PPELARRAY = POINTER(tagPELARRAY)


class tagLOGBRUSH(ctypes.Structure):
    _fields_ = [
        ('lbStyle', UINT),
        ('lbColor', COLORREF),
        # Sundown: lbHatch could hold a HANDLE
        ('lbHatch', ULONG_PTR),
    ]


LOGBRUSH = tagLOGBRUSH
PLOGBRUSH = POINTER(tagLOGBRUSH)


class tagLOGBRUSH32(ctypes.Structure):
    _fields_ = [
        ('lbStyle', UINT),
        ('lbColor', COLORREF),
        ('lbHatch', ULONG),
    ]


LOGBRUSH32 = tagLOGBRUSH32
PLOGBRUSH32 = POINTER(tagLOGBRUSH32)


class tagLOGPEN(ctypes.Structure):
    _fields_ = [
        ('lopnStyle', UINT),
        ('lopnWidth', POINT),
        ('lopnColor', COLORREF),
    ]


LOGPEN = tagLOGPEN
PLOGPEN = POINTER(tagLOGPEN)


# noinspection PyTypeChecker
class tagEXTLOGPEN(ctypes.Structure):
    _fields_ = [
        ('elpPenStyle', DWORD),
        ('elpWidth', DWORD),
        ('elpBrushStyle', UINT),
        ('elpColor', COLORREF),
        # Sundown: elpHatch could take a HANDLE
        ('elpHatch', ULONG_PTR),
        ('elpNumEntries', DWORD),
        ('elpStyleEntry', DWORD * 1),
    ]


EXTLOGPEN = tagEXTLOGPEN
PEXTLOGPEN = POINTER(tagEXTLOGPEN)


class tagPALETTEENTRY(ctypes.Structure):
    _fields_ = [
        ('peRed', BYTE),
        ('peGreen', BYTE),
        ('peBlue', BYTE),
        ('peFlags', BYTE),
    ]


PALETTEENTRY = tagPALETTEENTRY
PPALETTEENTRY = POINTER(tagPALETTEENTRY)


# ERROR - #define _LOGPALETTE_DEFINED


# noinspection PyTypeChecker
class tagLOGPALETTE(ctypes.Structure):
    _fields_ = [
        ('palVersion', WORD),
        ('palNumEntries', WORD),
        ('palPalEntry', PALETTEENTRY * 1),
    ]


LOGPALETTE = tagLOGPALETTE
PLOGPALETTE = POINTER(tagLOGPALETTE)


LF_FACESIZE = 0x00000020


# noinspection PyTypeChecker
class tagLOGFONTA(ctypes.Structure):
    _fields_ = [
        ('lfHeight', LONG),
        ('lfWidth', LONG),
        ('lfEscapement', LONG),
        ('lfOrientation', LONG),
        ('lfWeight', LONG),
        ('lfItalic', BYTE),
        ('lfUnderline', BYTE),
        ('lfStrikeOut', BYTE),
        ('lfCharSet', BYTE),
        ('lfOutPrecision', BYTE),
        ('lfClipPrecision', BYTE),
        ('lfQuality', BYTE),
        ('lfPitchAndFamily', BYTE),
        ('lfFaceName', CHAR * LF_FACESIZE),
    ]


LOGFONTA = tagLOGFONTA
PLOGFONTA = POINTER(tagLOGFONTA)


# noinspection PyTypeChecker
class tagLOGFONTW(ctypes.Structure):
    _fields_ = [
        ('lfHeight', LONG),
        ('lfWidth', LONG),
        ('lfEscapement', LONG),
        ('lfOrientation', LONG),
        ('lfWeight', LONG),
        ('lfItalic', BYTE),
        ('lfUnderline', BYTE),
        ('lfStrikeOut', BYTE),
        ('lfCharSet', BYTE),
        ('lfOutPrecision', BYTE),
        ('lfClipPrecision', BYTE),
        ('lfQuality', BYTE),
        ('lfPitchAndFamily', BYTE),
        ('lfFaceName', WCHAR * LF_FACESIZE),
    ]


LOGFONTW = tagLOGFONTW
PLOGFONTW = POINTER(tagLOGFONTW)


LF_FULLFACESIZE = 0x00000040


# noinspection PyTypeChecker
class tagENUMLOGFONTA(ctypes.Structure):
    _fields_ = [
        ('elfLogFont', LOGFONTA),
        ('elfFullName', BYTE * LF_FULLFACESIZE),
        ('elfStyle', BYTE * LF_FACESIZE),
    ]


ENUMLOGFONTA = tagENUMLOGFONTA


# noinspection PyTypeChecker
class tagENUMLOGFONTW(ctypes.Structure):
    _fields_ = [
        ('elfLogFont', LOGFONTW),
        ('elfFullName', WCHAR * LF_FULLFACESIZE),
        ('elfStyle', WCHAR * LF_FACESIZE),
    ]


ENUMLOGFONTW = tagENUMLOGFONTW


# noinspection PyTypeChecker
class tagENUMLOGFONTEXA(ctypes.Structure):
    _fields_ = [
        ('elfLogFont', LOGFONTA),
        ('elfFullName', BYTE * LF_FULLFACESIZE),
        ('elfStyle', BYTE * LF_FACESIZE),
        ('elfScript', BYTE * LF_FACESIZE),
    ]


ENUMLOGFONTEXA = tagENUMLOGFONTEXA


# noinspection PyTypeChecker
class tagENUMLOGFONTEXW(ctypes.Structure):
    _fields_ = [
        ('elfLogFont', LOGFONTW),
        ('elfFullName', WCHAR * LF_FULLFACESIZE),
        ('elfStyle', WCHAR * LF_FACESIZE),
        ('elfScript', WCHAR * LF_FACESIZE),
    ]


ENUMLOGFONTEXW = tagENUMLOGFONTEXW


OUT_DEFAULT_PRECIS = 0x00000000
OUT_STRING_PRECIS = 0x00000001
OUT_CHARACTER_PRECIS = 0x00000002
OUT_STROKE_PRECIS = 0x00000003
OUT_TT_PRECIS = 0x00000004
OUT_DEVICE_PRECIS = 0x00000005
OUT_RASTER_PRECIS = 0x00000006
OUT_TT_ONLY_PRECIS = 0x00000007
OUT_OUTLINE_PRECIS = 0x00000008
OUT_SCREEN_OUTLINE_PRECIS = 0x00000009
OUT_PS_ONLY_PRECIS = 0x0000000A
CLIP_DEFAULT_PRECIS = 0x00000000
CLIP_CHARACTER_PRECIS = 0x00000001
CLIP_STROKE_PRECIS = 0x00000002
CLIP_MASK = 0x0000000F
CLIP_LH_ANGLES = 1 << 4
CLIP_TT_ALWAYS = 2 << 4
CLIP_DFA_DISABLE = 4 << 4
CLIP_EMBEDDED = 8 << 4
DEFAULT_QUALITY = 0x00000000
DRAFT_QUALITY = 0x00000001
PROOF_QUALITY = 0x00000002
NONANTIALIASED_QUALITY = 0x00000003
ANTIALIASED_QUALITY = 0x00000004
CLEARTYPE_QUALITY = 0x00000005
CLEARTYPE_NATURAL_QUALITY = 0x00000006
DEFAULT_PITCH = 0x00000000
FIXED_PITCH = 0x00000001
VARIABLE_PITCH = 0x00000002
MONO_FONT = 0x00000008
ANSI_CHARSET = 0x00000000
DEFAULT_CHARSET = 0x00000001
SYMBOL_CHARSET = 0x00000002
SHIFTJIS_CHARSET = 0x00000080
HANGEUL_CHARSET = 0x00000081
HANGUL_CHARSET = 0x00000081
GB2312_CHARSET = 0x00000086
CHINESEBIG5_CHARSET = 0x00000088
OEM_CHARSET = 0x000000FF
JOHAB_CHARSET = 0x00000082
HEBREW_CHARSET = 0x000000B1
ARABIC_CHARSET = 0x000000B2
GREEK_CHARSET = 0x000000A1
TURKISH_CHARSET = 0x000000A2
VIETNAMESE_CHARSET = 0x000000A3
THAI_CHARSET = 0x000000DE
EASTEUROPE_CHARSET = 0x000000EE
RUSSIAN_CHARSET = 0x000000CC
MAC_CHARSET = 0x0000004D
BALTIC_CHARSET = 0x000000BA
FS_LATIN1 = 0x00000001
FS_LATIN2 = 0x00000002
FS_CYRILLIC = 0x00000004
FS_GREEK = 0x00000008
FS_TURKISH = 0x00000010
FS_HEBREW = 0x00000020
FS_ARABIC = 0x00000040
FS_BALTIC = 0x00000080
FS_VIETNAMESE = 0x00000100
FS_THAI = 0x00010000
FS_JISJAPAN = 0x00020000
FS_CHINESESIMP = 0x00040000
FS_WANSUNG = 0x00080000
FS_CHINESETRAD = 0x00100000
FS_JOHAB = 0x00200000
FS_SYMBOL = 0x80000000

# Don't care or don't know.
FF_DONTCARE = 0 << 4

# Variable stroke width, serifed.
FF_ROMAN = 1 << 4

# Variable stroke width, sans-serifed.
FF_SWISS = 2 << 4

# Constant stroke width, serifed or sans-serifed.
FF_MODERN = 3 << 4

# Cursive, etc.
FF_SCRIPT = 4 << 4

# Old English, etc.
FF_DECORATIVE = 5 << 4

FW_DONTCARE = 0x00000000
FW_THIN = 0x00000064
FW_EXTRALIGHT = 0x000000C8
FW_LIGHT = 0x0000012C
FW_NORMAL = 0x00000190
FW_MEDIUM = 0x000001F4
FW_SEMIBOLD = 0x00000258
FW_BOLD = 0x000002BC
FW_EXTRABOLD = 0x00000320
FW_HEAVY = 0x00000384
FW_ULTRALIGHT = FW_EXTRALIGHT
FW_REGULAR = FW_NORMAL
FW_DEMIBOLD = FW_SEMIBOLD
FW_ULTRABOLD = FW_EXTRABOLD
FW_BLACK = FW_HEAVY
PANOSE_COUNT = 0x0000000A
PAN_FAMILYTYPE_INDEX = 0x00000000
PAN_SERIFSTYLE_INDEX = 0x00000001
PAN_WEIGHT_INDEX = 0x00000002
PAN_PROPORTION_INDEX = 0x00000003
PAN_CONTRAST_INDEX = 0x00000004
PAN_STROKEVARIATION_INDEX = 0x00000005
PAN_ARMSTYLE_INDEX = 0x00000006
PAN_LETTERFORM_INDEX = 0x00000007
PAN_MIDLINE_INDEX = 0x00000008
PAN_XHEIGHT_INDEX = 0x00000009
PAN_CULTURE_LATIN = 0x00000000


class tagPANOSE(ctypes.Structure):
    _fields_ = [
        ('bFamilyType', BYTE),
        ('bSerifStyle', BYTE),
        ('bWeight', BYTE),
        ('bProportion', BYTE),
        ('bContrast', BYTE),
        ('bStrokeVariation', BYTE),
        ('bArmStyle', BYTE),
        ('bLetterform', BYTE),
        ('bMidline', BYTE),
        ('bXHeight', BYTE),
    ]


PANOSE = tagPANOSE
LPPANOSE = POINTER(tagPANOSE)


# Any
PAN_ANY = 0x00000000

# No Fit
PAN_NO_FIT = 0x00000001

# Text and Display
PAN_FAMILY_TEXT_DISPLAY = 0x00000002

# Script
PAN_FAMILY_SCRIPT = 0x00000003

# Decorative
PAN_FAMILY_DECORATIVE = 0x00000004

# Pictorial
PAN_FAMILY_PICTORIAL = 0x00000005

# Cove
PAN_SERIF_COVE = 0x00000002

# Obtuse Cove
PAN_SERIF_OBTUSE_COVE = 0x00000003

# Square Cove
PAN_SERIF_SQUARE_COVE = 0x00000004

# Obtuse Square Cove
PAN_SERIF_OBTUSE_SQUARE_COVE = 0x00000005

# Square
PAN_SERIF_SQUARE = 0x00000006

# Thin
PAN_SERIF_THIN = 0x00000007

# Bone
PAN_SERIF_BONE = 0x00000008

# Exaggerated
PAN_SERIF_EXAGGERATED = 0x00000009

# Triangle
PAN_SERIF_TRIANGLE = 0x0000000A

# Normal Sans
PAN_SERIF_NORMAL_SANS = 0x0000000B

# Obtuse Sans
PAN_SERIF_OBTUSE_SANS = 0x0000000C

# Prep Sans
PAN_SERIF_PERP_SANS = 0x0000000D

# Flared
PAN_SERIF_FLARED = 0x0000000E

# Rounded
PAN_SERIF_ROUNDED = 0x0000000F

# Very Light
PAN_WEIGHT_VERY_LIGHT = 0x00000002

# Light
PAN_WEIGHT_LIGHT = 0x00000003

# Thin
PAN_WEIGHT_THIN = 0x00000004

# Book
PAN_WEIGHT_BOOK = 0x00000005

# Medium
PAN_WEIGHT_MEDIUM = 0x00000006

# Demi
PAN_WEIGHT_DEMI = 0x00000007

# Bold
PAN_WEIGHT_BOLD = 0x00000008

# Heavy
PAN_WEIGHT_HEAVY = 0x00000009

# Black
PAN_WEIGHT_BLACK = 0x0000000A

# Nord
PAN_WEIGHT_NORD = 0x0000000B

# Old Style
PAN_PROP_OLD_STYLE = 0x00000002

# Modern
PAN_PROP_MODERN = 0x00000003

# Even Width
PAN_PROP_EVEN_WIDTH = 0x00000004

# Expanded
PAN_PROP_EXPANDED = 0x00000005

# Condensed
PAN_PROP_CONDENSED = 0x00000006

# Very Expanded
PAN_PROP_VERY_EXPANDED = 0x00000007

# Very Condensed
PAN_PROP_VERY_CONDENSED = 0x00000008

# Monospaced
PAN_PROP_MONOSPACED = 0x00000009

# None
PAN_CONTRAST_NONE = 0x00000002

# Very Low
PAN_CONTRAST_VERY_LOW = 0x00000003

# Low
PAN_CONTRAST_LOW = 0x00000004

# Medium Low
PAN_CONTRAST_MEDIUM_LOW = 0x00000005

# Medium
PAN_CONTRAST_MEDIUM = 0x00000006

# Mediim High
PAN_CONTRAST_MEDIUM_HIGH = 0x00000007

# High
PAN_CONTRAST_HIGH = 0x00000008

# Very High
PAN_CONTRAST_VERY_HIGH = 0x00000009

# Gradual/Diagonal
PAN_STROKE_GRADUAL_DIAG = 0x00000002

# Gradual/Transitional
PAN_STROKE_GRADUAL_TRAN = 0x00000003

# Gradual/Vertical
PAN_STROKE_GRADUAL_VERT = 0x00000004

# Gradual/Horizontal
PAN_STROKE_GRADUAL_HORZ = 0x00000005

# Rapid/Vertical
PAN_STROKE_RAPID_VERT = 0x00000006

# Rapid/Horizontal
PAN_STROKE_RAPID_HORZ = 0x00000007

# Instant/Vertical
PAN_STROKE_INSTANT_VERT = 0x00000008

# Straight Arms/Horizontal
PAN_STRAIGHT_ARMS_HORZ = 0x00000002

# Straight Arms/Wedge
PAN_STRAIGHT_ARMS_WEDGE = 0x00000003

# Straight Arms/Vertical
PAN_STRAIGHT_ARMS_VERT = 0x00000004

# Straight Arms/Single-Serif
PAN_STRAIGHT_ARMS_SINGLE_SERIF = 0x00000005

# Straight Arms/Double-Serif
PAN_STRAIGHT_ARMS_DOUBLE_SERIF = 0x00000006

# Non-Straight Arms/Horizontal
PAN_BENT_ARMS_HORZ = 0x00000007

# Non-Straight Arms/Wedge
PAN_BENT_ARMS_WEDGE = 0x00000008

# Non-Straight Arms/Vertical
PAN_BENT_ARMS_VERT = 0x00000009

# Non-Straight Arms/Single-Serif
PAN_BENT_ARMS_SINGLE_SERIF = 0x0000000A

# Non-Straight Arms/Double-Serif
PAN_BENT_ARMS_DOUBLE_SERIF = 0x0000000B

# Normal/Contact
PAN_LETT_NORMAL_CONTACT = 0x00000002

# Normal/Weighted
PAN_LETT_NORMAL_WEIGHTED = 0x00000003

# Normal/Boxed
PAN_LETT_NORMAL_BOXED = 0x00000004

# Normal/Flattened
PAN_LETT_NORMAL_FLATTENED = 0x00000005

# Normal/Rounded
PAN_LETT_NORMAL_ROUNDED = 0x00000006

# Normal/Off Center
PAN_LETT_NORMAL_OFF_CENTER = 0x00000007

# Normal/Square
PAN_LETT_NORMAL_SQUARE = 0x00000008

# Oblique/Contact
PAN_LETT_OBLIQUE_CONTACT = 0x00000009

# Oblique/Weighted
PAN_LETT_OBLIQUE_WEIGHTED = 0x0000000A

# Oblique/Boxed
PAN_LETT_OBLIQUE_BOXED = 0x0000000B

# Oblique/Flattened
PAN_LETT_OBLIQUE_FLATTENED = 0x0000000C

# Oblique/Rounded
PAN_LETT_OBLIQUE_ROUNDED = 0x0000000D

# Oblique/Off Center
PAN_LETT_OBLIQUE_OFF_CENTER = 0x0000000E

# Oblique/Square
PAN_LETT_OBLIQUE_SQUARE = 0x0000000F

# Standard/Trimmed
PAN_MIDLINE_STANDARD_TRIMMED = 0x00000002

# Standard/Pointed
PAN_MIDLINE_STANDARD_POINTED = 0x00000003

# Standard/Serifed
PAN_MIDLINE_STANDARD_SERIFED = 0x00000004

# High/Trimmed
PAN_MIDLINE_HIGH_TRIMMED = 0x00000005

# High/Pointed
PAN_MIDLINE_HIGH_POINTED = 0x00000006

# High/Serifed
PAN_MIDLINE_HIGH_SERIFED = 0x00000007

# Constant/Trimmed
PAN_MIDLINE_CONSTANT_TRIMMED = 0x00000008

# Constant/Pointed
PAN_MIDLINE_CONSTANT_POINTED = 0x00000009

# Constant/Serifed
PAN_MIDLINE_CONSTANT_SERIFED = 0x0000000A

# Low/Trimmed
PAN_MIDLINE_LOW_TRIMMED = 0x0000000B

# Low/Pointed
PAN_MIDLINE_LOW_POINTED = 0x0000000C

# Low/Serifed
PAN_MIDLINE_LOW_SERIFED = 0x0000000D

# Constant/Small
PAN_XHEIGHT_CONSTANT_SMALL = 0x00000002

# Constant/Standard
PAN_XHEIGHT_CONSTANT_STD = 0x00000003

# Constant/Large
PAN_XHEIGHT_CONSTANT_LARGE = 0x00000004

# Ducking/Small
PAN_XHEIGHT_DUCKING_SMALL = 0x00000005

# Ducking/Standard
PAN_XHEIGHT_DUCKING_STD = 0x00000006

# Ducking/Large
PAN_XHEIGHT_DUCKING_LARGE = 0x00000007
ELF_VENDOR_SIZE = 0x00000004


# noinspection PyTypeChecker
class tagEXTLOGFONTA(ctypes.Structure):
    _fields_ = [
        ('elfLogFont', LOGFONTA),
        ('elfFullName', BYTE * LF_FULLFACESIZE),
        ('elfStyle', BYTE * LF_FACESIZE),
        # 0 for the first release of NT
        ('elfVersion', DWORD),
        ('elfStyleSize', DWORD),
        ('elfMatch', DWORD),
        ('elfReserved', DWORD),
        ('elfVendorId', BYTE * ELF_VENDOR_SIZE),
        # 0 for Latin
        ('elfCulture', DWORD),
        ('elfPanose', PANOSE),
    ]


EXTLOGFONTA = tagEXTLOGFONTA
PEXTLOGFONTA = POINTER(tagEXTLOGFONTA)


# noinspection PyTypeChecker
class tagEXTLOGFONTW(ctypes.Structure):
    _fields_ = [
        ('elfLogFont', LOGFONTW),
        ('elfFullName', WCHAR * LF_FULLFACESIZE),
        ('elfStyle', WCHAR * LF_FACESIZE),
        # 0 for the first release of NT
        ('elfVersion', DWORD),
        ('elfStyleSize', DWORD),
        ('elfMatch', DWORD),
        ('elfReserved', DWORD),
        ('elfVendorId', BYTE * ELF_VENDOR_SIZE),
        # 0 for Latin
        ('elfCulture', DWORD),
        ('elfPanose', PANOSE),
    ]


EXTLOGFONTW = tagEXTLOGFONTW
PEXTLOGFONTW = POINTER(tagEXTLOGFONTW)


ELF_VERSION = 0x00000000
ELF_CULTURE_LATIN = 0x00000000
RASTER_FONTTYPE = 0x00000001
DEVICE_FONTTYPE = 0x00000002
TRUETYPE_FONTTYPE = 0x00000004


def RGB(r, g, b):
    return COLORREF(r | (g << 8) | (b << 16))


def PALETTERGB(r, g, b):
    return 0x02000000 | RGB(r, g, b)


def PALETTEINDEX(i):
    return COLORREF(0x01000000 | i)


# palette index used for animation
PC_RESERVED = 0x00000001

# palette index is explicit to device
PC_EXPLICIT = 0x00000002

# do not match color to system palette
PC_NOCOLLAPSE = 0x00000004


def GetRValue(rgb):
    return LOBYTE(rgb)


def GetGValue(rgb):
    return LOBYTE(rgb >> 8)


def GetBValue(rgb):
    return LOBYTE(rgb >> 16)


TRANSPARENT = 0x00000001
OPAQUE = 0x00000002
BKMODE_LAST = 0x00000002
GM_COMPATIBLE = 0x00000001
GM_ADVANCED = 0x00000002
GM_LAST = 0x00000002
PT_CLOSEFIGURE = 0x00000001
PT_LINETO = 0x00000002
PT_BEZIERTO = 0x00000004
PT_MOVETO = 0x00000006
MM_TEXT = 0x00000001
MM_LOMETRIC = 0x00000002
MM_HIMETRIC = 0x00000003
MM_LOENGLISH = 0x00000004
MM_HIENGLISH = 0x00000005
MM_TWIPS = 0x00000006
MM_ISOTROPIC = 0x00000007
MM_ANISOTROPIC = 0x00000008
MM_MIN = MM_TEXT
MM_MAX = MM_ANISOTROPIC
MM_MAX_FIXEDSCALE = MM_TWIPS
ABSOLUTE = 0x00000001
RELATIVE = 0x00000002
WHITE_BRUSH = 0x00000000
LTGRAY_BRUSH = 0x00000001
GRAY_BRUSH = 0x00000002
DKGRAY_BRUSH = 0x00000003
BLACK_BRUSH = 0x00000004
NULL_BRUSH = 0x00000005
HOLLOW_BRUSH = NULL_BRUSH
WHITE_PEN = 0x00000006
BLACK_PEN = 0x00000007
NULL_PEN = 0x00000008
OEM_FIXED_FONT = 0x0000000A
ANSI_FIXED_FONT = 0x0000000B
ANSI_VAR_FONT = 0x0000000C
SYSTEM_FONT = 0x0000000D
DEVICE_DEFAULT_FONT = 0x0000000E
DEFAULT_PALETTE = 0x0000000F
SYSTEM_FIXED_FONT = 0x00000010
DEFAULT_GUI_FONT = 0x00000011
DC_BRUSH = 0x00000012
DC_PEN = 0x00000013
STOCK_LAST = 0x00000013
CLR_INVALID = 0xFFFFFFFF
BS_SOLID = 0x00000000
BS_NULL = 0x00000001
BS_HOLLOW = BS_NULL
BS_HATCHED = 0x00000002
BS_PATTERN = 0x00000003
BS_INDEXED = 0x00000004
BS_DIBPATTERN = 0x00000005
BS_DIBPATTERNPT = 0x00000006
BS_PATTERN8X8 = 0x00000007
BS_DIBPATTERN8X8 = 0x00000008
BS_MONOPATTERN = 0x00000009

# -----
HS_HORIZONTAL = 0x00000000

# |||||
HS_VERTICAL = 0x00000001

# \\\
HS_FDIAGONAL = 0x00000002
# ///
HS_BDIAGONAL = 0x00000003

# +++++
HS_CROSS = 0x00000004

# xxxxx
HS_DIAGCROSS = 0x00000005
PS_SOLID = 0x00000000

# -------
PS_DASH = 0x00000001

# .......
PS_DOT = 0x00000002

# _._._._
PS_DASHDOT = 0x00000003

# _.._.._
PS_DASHDOTDOT = 0x00000004
PS_NULL = 0x00000005
PS_INSIDEFRAME = 0x00000006
PS_USERSTYLE = 0x00000007
PS_ALTERNATE = 0x00000008
PS_STYLE_MASK = 0x0000000F
PS_ENDCAP_ROUND = 0x00000000
PS_ENDCAP_SQUARE = 0x00000100
PS_ENDCAP_FLAT = 0x00000200
PS_ENDCAP_MASK = 0x00000F00
PS_JOIN_ROUND = 0x00000000
PS_JOIN_BEVEL = 0x00001000
PS_JOIN_MITER = 0x00002000
PS_JOIN_MASK = 0x0000F000
PS_COSMETIC = 0x00000000
PS_GEOMETRIC = 0x00010000
PS_TYPE_MASK = 0x000F0000
AD_COUNTERCLOCKWISE = 0x00000001
AD_CLOCKWISE = 0x00000002

# Device driver version
DRIVERVERSION = 0x00000000

# Device classification
TECHNOLOGY = 0x00000002

# Horizontal size in millimeters
HORZSIZE = 0x00000004

# Vertical size in millimeters
VERTSIZE = 0x00000006

# Horizontal width in pixels
HORZRES = 0x00000008

# Vertical height in pixels
VERTRES = 0x0000000A

# Number of bits per pixel
BITSPIXEL = 0x0000000C

# Number of planes
PLANES = 0x0000000E

# Number of brushes the device has
NUMBRUSHES = 0x00000010

# Number of pens the device has
NUMPENS = 0x00000012

# Number of markers the device has
NUMMARKERS = 0x00000014

# Number of fonts the device has
NUMFONTS = 0x00000016

# Number of colors the device supports
NUMCOLORS = 0x00000018

# Size required for device descriptor
PDEVICESIZE = 0x0000001A

# Curve capabilities
CURVECAPS = 0x0000001C

# Line capabilities
LINECAPS = 0x0000001E

# Polygonal capabilities
POLYGONALCAPS = 0x00000020

# Text capabilities
TEXTCAPS = 0x00000022

# Clipping capabilities
CLIPCAPS = 0x00000024

# Bitblt capabilities
RASTERCAPS = 0x00000026

# Length of the X leg
ASPECTX = 0x00000028

# Length of the Y leg
ASPECTY = 0x0000002A

# Length of the hypotenuse
ASPECTXY = 0x0000002C

# Logical pixels/inch in X
LOGPIXELSX = 0x00000058

# Logical pixels/inch in Y
LOGPIXELSY = 0x0000005A

# Number of entries in physical palette
SIZEPALETTE = 0x00000068

# Number of reserved entries in palette
NUMRESERVED = 0x0000006A

# Actual color resolution
COLORRES = 0x0000006C

# Physical Width in device units
PHYSICALWIDTH = 0x0000006E

# Physical Height in device units
PHYSICALHEIGHT = 0x0000006F

# Physical Printable Area x margin
PHYSICALOFFSETX = 0x00000070

# Physical Printable Area y margin
PHYSICALOFFSETY = 0x00000071

# Scaling factor x
SCALINGFACTORX = 0x00000072

# Scaling factor y
SCALINGFACTORY = 0x00000073

# Current vertical refresh rate of the
VREFRESH = 0x00000074

# Horizontal width of entire desktop in
DESKTOPVERTRES = 0x00000075

# Vertical height of entire desktop in
DESKTOPHORZRES = 0x00000076

# Preferred blt alignment
BLTALIGNMENT = 0x00000077

# Shading and blending caps
SHADEBLENDCAPS = 0x00000078

# Color Management caps
COLORMGMTCAPS = 0x00000079

# Vector plotter
DT_PLOTTER = 0x00000000

# Raster display
DT_RASDISPLAY = 0x00000001

# Raster printer
DT_RASPRINTER = 0x00000002

# Raster camera
DT_RASCAMERA = 0x00000003

# Character-stream, PLP
DT_CHARSTREAM = 0x00000004

# Metafile, VDM
DT_METAFILE = 0x00000005

# Display-file
DT_DISPFILE = 0x00000006

# Curves not supported
CC_NONE = 0x00000000

# Can do circles
CC_CIRCLES = 0x00000001

# Can do pie wedges
CC_PIE = 0x00000002

# Can do chord arcs
CC_CHORD = 0x00000004

# Can do ellipese
CC_ELLIPSES = 0x00000008

# Can do wide lines
CC_WIDE = 0x00000010

# Can do styled lines
CC_STYLED = 0x00000020

# Can do wide styled lines
CC_WIDESTYLED = 0x00000040

# Can do interiors
CC_INTERIORS = 0x00000080

#
CC_ROUNDRECT = 0x00000100

# Lines not supported
LC_NONE = 0x00000000

# Can do polylines
LC_POLYLINE = 0x00000002

# Can do markers
LC_MARKER = 0x00000004

# Can do polymarkers
LC_POLYMARKER = 0x00000008

# Can do wide lines
LC_WIDE = 0x00000010

# Can do styled lines
LC_STYLED = 0x00000020

# Can do wide styled lines
LC_WIDESTYLED = 0x00000040

# Can do interiors
LC_INTERIORS = 0x00000080

# Polygonals not supported
PC_NONE = 0x00000000

# Can do polygons
PC_POLYGON = 0x00000001

# Can do rectangles
PC_RECTANGLE = 0x00000002

# Can do winding polygons
PC_WINDPOLYGON = 0x00000004

# Can do trapezoids
PC_TRAPEZOID = 0x00000004

# Can do scanlines
PC_SCANLINE = 0x00000008

# Can do wide borders
PC_WIDE = 0x00000010

# Can do styled borders
PC_STYLED = 0x00000020

# Can do wide styled borders
PC_WIDESTYLED = 0x00000040

# Can do interiors
PC_INTERIORS = 0x00000080

# Can do polypolygons
PC_POLYPOLYGON = 0x00000100

# Can do paths
PC_PATHS = 0x00000200

# No clipping of output
CP_NONE = 0x00000000

# Output clipped to rects
CP_RECTANGLE = 0x00000001

# obsolete
CP_REGION = 0x00000002

# Can do OutputPrecision   CHARACTER
TC_OP_CHARACTER = 0x00000001

# Can do OutputPrecision   STROKE
TC_OP_STROKE = 0x00000002

# Can do ClipPrecision     STROKE
TC_CP_STROKE = 0x00000004

# Can do CharRotAbility    90
TC_CR_90 = 0x00000008

# Can do CharRotAbility    ANY
TC_CR_ANY = 0x00000010

# Can do ScaleFreedom      X_YINDEPENDENT
TC_SF_X_YINDEP = 0x00000020

# Can do ScaleAbility      DOUBLE
TC_SA_DOUBLE = 0x00000040

# Can do ScaleAbility      INTEGER
TC_SA_INTEGER = 0x00000080

# Can do ScaleAbility      CONTINUOUS
TC_SA_CONTIN = 0x00000100

# Can do EmboldenAbility   DOUBLE
TC_EA_DOUBLE = 0x00000200

# Can do ItalisizeAbility  ABLE
TC_IA_ABLE = 0x00000400

# Can do UnderlineAbility  ABLE
TC_UA_ABLE = 0x00000800

# Can do StrikeOutAbility  ABLE
TC_SO_ABLE = 0x00001000

# Can do RasterFontAble    ABLE
TC_RA_ABLE = 0x00002000

# Can do VectorFontAble    ABLE
TC_VA_ABLE = 0x00004000
TC_RESERVED = 0x00008000

# Don't do text scroll with blt
TC_SCROLLBLT = 0x00010000
# ERROR - #define RC_NONE

# Can do standard BLT.
RC_BITBLT = 0x00000001

# Device requires banding support
RC_BANDING = 0x00000002

# Device requires scaling support
RC_SCALING = 0x00000004

# Device can support >64K bitmap
RC_BITMAP64 = 0x00000008

# has 2.0 output calls
RC_GDI20_OUTPUT = 0x00000010
RC_GDI20_STATE = 0x00000020
RC_SAVEBITMAP = 0x00000040

# supports DIB to memory
RC_DI_BITMAP = 0x00000080

# supports a palette
RC_PALETTE = 0x00000100

# supports DIBitsToDevice
RC_DIBTODEV = 0x00000200

# supports >64K fonts
RC_BIGFONT = 0x00000400

# supports StretchBlt
RC_STRETCHBLT = 0x00000800

# supports FloodFill
RC_FLOODFILL = 0x00001000

# supports StretchDIBits
RC_STRETCHDIB = 0x00002000
RC_OP_DX_OUTPUT = 0x00004000
RC_DEVBITS = 0x00008000
SB_NONE = 0x00000000
SB_CONST_ALPHA = 0x00000001
SB_PIXEL_ALPHA = 0x00000002
SB_PREMULT_ALPHA = 0x00000004
SB_GRAD_RECT = 0x00000010
SB_GRAD_TRI = 0x00000020
CM_NONE = 0x00000000
CM_DEVICE_ICM = 0x00000001
CM_GAMMA_RAMP = 0x00000002
CM_CMYK_COLOR = 0x00000004

# color table in RGBs
DIB_RGB_COLORS = 0x00000000

# color table in palette indices
DIB_PAL_COLORS = 0x00000001
SYSPAL_ERROR = 0x00000000
SYSPAL_STATIC = 0x00000001
SYSPAL_NOSTATIC = 0x00000002
SYSPAL_NOSTATIC256 = 0x00000003

# initialize bitmap
CBM_INIT = 0x0000004
FLOODFILLBORDER = 0x00000000
FLOODFILLSURFACE = 0x00000001
CCHDEVICENAME = 0x00000020
CCHFORMNAME = 0x00000020


# noinspection PyTypeChecker
class _devicemodeA(ctypes.Structure):
    class _Union_0(ctypes.Union):
        _fields_ = [

        ]

    class _Union_1(ctypes.Union):
        _fields_ = [
            ('dmDisplayFlags', DWORD),
            ('dmNup', DWORD),
        ]

    _anonymous_ = ('_Union_0', '_Union_1')
    _fields_ = [
        ('dmDeviceName', BYTE * CCHDEVICENAME),
        ('dmSpecVersion', WORD),
        ('dmDriverVersion', WORD),
        ('dmSize', WORD),
        ('dmDriverExtra', WORD),
        ('dmFields', DWORD),
        ('_Union_0', _Union_0),
        ('dmScale', SHORT),
        ('dmCopies', SHORT),
        ('dmDefaultSource', SHORT),
        ('dmPrintQuality', SHORT),
        ('dmColor', SHORT),
        ('dmDuplex', SHORT),
        ('dmYResolution', SHORT),
        ('dmTTOption', SHORT),
        ('dmCollate', SHORT),
        ('dmFormName', BYTE * CCHFORMNAME),
        ('dmLogPixels', WORD),
        ('dmBitsPerPel', DWORD),
        ('dmPelsWidth', DWORD),
        ('dmPelsHeight', DWORD),
        ('_Union_1', _Union_1),
        ('dmDisplayFrequency', DWORD),
        ('dmICMMethod', DWORD),
        ('dmICMIntent', DWORD),
        ('dmMediaType', DWORD),
        ('dmDitherType', DWORD),
        ('dmReserved1', DWORD),
        ('dmReserved2', DWORD),
        ('dmPanningWidth', DWORD),
        ('dmPanningHeight', DWORD),
    ]


DEVMODEA = _devicemodeA
PDEVMODEA = POINTER(_devicemodeA)
NPDEVMODEA = POINTER(_devicemodeA)
LPDEVMODEA = POINTER(_devicemodeA)


# noinspection PyTypeChecker
class _devicemodeW(ctypes.Structure):
    class _Union_0(ctypes.Union):
        _fields_ = [

        ]

    class _Union_1(ctypes.Union):
        _fields_ = [
            ('dmDisplayFlags', DWORD),
            ('dmNup', DWORD),
        ]

    _anonymous_ = ('_Union_0', '_Union_1')
    _fields_ = [
        ('dmDeviceName', WCHAR * CCHDEVICENAME),
        ('dmSpecVersion', WORD),
        ('dmDriverVersion', WORD),
        ('dmSize', WORD),
        ('dmDriverExtra', WORD),
        ('dmFields', DWORD),
        ('_Union_0', _Union_0),
        ('dmScale', SHORT),
        ('dmCopies', SHORT),
        ('dmDefaultSource', SHORT),
        ('dmPrintQuality', SHORT),
        ('dmColor', SHORT),
        ('dmDuplex', SHORT),
        ('dmYResolution', SHORT),
        ('dmTTOption', SHORT),
        ('dmCollate', SHORT),
        ('dmFormName', WCHAR * CCHFORMNAME),
        ('dmLogPixels', WORD),
        ('dmBitsPerPel', DWORD),
        ('dmPelsWidth', DWORD),
        ('dmPelsHeight', DWORD),
        ('_Union_1', _Union_1),
        ('dmDisplayFrequency', DWORD),
        ('dmICMMethod', DWORD),
        ('dmICMIntent', DWORD),
        ('dmMediaType', DWORD),
        ('dmDitherType', DWORD),
        ('dmReserved1', DWORD),
        ('dmReserved2', DWORD),
        ('dmPanningWidth', DWORD),
        ('dmPanningHeight', DWORD),
    ]


DEVMODEW = _devicemodeW
PDEVMODEW = POINTER(_devicemodeW)
NPDEVMODEW = POINTER(_devicemodeW)
LPDEVMODEW = POINTER(_devicemodeW)


DM_SPECVERSION = 0x00000401
DM_ORIENTATION = 0x00000001
DM_PAPERSIZE = 0x00000002
DM_PAPERLENGTH = 0x00000004
DM_PAPERWIDTH = 0x00000008
DM_SCALE = 0x00000010
DM_POSITION = 0x00000020
DM_NUP = 0x00000040
DM_DISPLAYORIENTATION = 0x00000080
DM_COPIES = 0x00000100
DM_DEFAULTSOURCE = 0x00000200
DM_PRINTQUALITY = 0x00000400
DM_COLOR = 0x00000800
DM_DUPLEX = 0x00001000
DM_YRESOLUTION = 0x00002000
DM_TTOPTION = 0x00004000
DM_COLLATE = 0x00008000
DM_FORMNAME = 0x00010000
DM_LOGPIXELS = 0x00020000
DM_BITSPERPEL = 0x00040000
DM_PELSWIDTH = 0x00080000
DM_PELSHEIGHT = 0x00100000
DM_DISPLAYFLAGS = 0x00200000
DM_DISPLAYFREQUENCY = 0x00400000
DM_ICMMETHOD = 0x00800000
DM_ICMINTENT = 0x01000000
DM_MEDIATYPE = 0x02000000
DM_DITHERTYPE = 0x04000000
DM_PANNINGWIDTH = 0x08000000
DM_PANNINGHEIGHT = 0x10000000
DM_DISPLAYFIXEDOUTPUT = 0x20000000
DMORIENT_PORTRAIT = 0x00000001
DMORIENT_LANDSCAPE = 0x00000002

# Letter 8 1/2 x 11 in
DMPAPER_LETTER = 0x00000001
DMPAPER_FIRST = DMPAPER_LETTER

# Letter Small 8 1/2 x 11 in
DMPAPER_LETTERSMALL = 0x00000002

# Tabloid 11 x 17 in
DMPAPER_TABLOID = 0x00000003

# Ledger 17 x 11 in
DMPAPER_LEDGER = 0x00000004

# Legal 8 1/2 x 14 in
DMPAPER_LEGAL = 0x00000005

# Statement 5 1/2 x 8 1/2 in
DMPAPER_STATEMENT = 0x00000006

# Executive 7 1/4 x 10 1/2 in
DMPAPER_EXECUTIVE = 0x00000007

# A3 297 x 420 mm
DMPAPER_A3 = 0x00000008

# A4 210 x 297 mm
DMPAPER_A4 = 0x00000009

# A4 Small 210 x 297 mm
DMPAPER_A4SMALL = 0x0000000A

# A5 148 x 210 mm
DMPAPER_A5 = 0x0000000B

# B4 (JIS) 250 x 354
DMPAPER_B4 = 0x0000000C

# B5 (JIS) 182 x 257 mm
DMPAPER_B5 = 0x0000000D

# Folio 8 1/2 x 13 in
DMPAPER_FOLIO = 0x0000000E

# Quarto 215 x 275 mm
DMPAPER_QUARTO = 0x0000000F

# 10x14 in
DMPAPER_10X14 = 0x00000010

# 11x17 in
DMPAPER_11X17 = 0x00000011

# Note 8 1/2 x 11 in
DMPAPER_NOTE = 0x00000012

# Envelope #9 3 7/8 x 8 7/8
DMPAPER_ENV_9 = 0x00000013

# Envelope #10 4 1/8 x 9 1/2
DMPAPER_ENV_10 = 0x00000014

# Envelope #11 4 1/2 x 10 3/8
DMPAPER_ENV_11 = 0x00000015

# Envelope #12 4 x 11
DMPAPER_ENV_12 = 0x00000016

# Envelope #14 5 x 11 1/2
DMPAPER_ENV_14 = 0x00000017

# C size sheet
DMPAPER_CSHEET = 0x00000018

# D size sheet
DMPAPER_DSHEET = 0x00000019

# E size sheet
DMPAPER_ESHEET = 0x0000001A

# Envelope DL 110 x 220mm
DMPAPER_ENV_DL = 0x0000001B

# Envelope C5 162 x 229 mm
DMPAPER_ENV_C5 = 0x0000001C

# Envelope C3  324 x 458 mm
DMPAPER_ENV_C3 = 0x0000001D

# Envelope C4  229 x 324 mm
DMPAPER_ENV_C4 = 0x0000001E

# Envelope C6  114 x 162 mm
DMPAPER_ENV_C6 = 0x0000001F

# Envelope C65 114 x 229 mm
DMPAPER_ENV_C65 = 0x00000020

# Envelope B4  250 x 353 mm
DMPAPER_ENV_B4 = 0x00000021

# Envelope B5  176 x 250 mm
DMPAPER_ENV_B5 = 0x00000022

# Envelope B6  176 x 125 mm
DMPAPER_ENV_B6 = 0x00000023

# Envelope 110 x 230 mm
DMPAPER_ENV_ITALY = 0x00000024

# Envelope Monarch 3.875 x 7.5 in
DMPAPER_ENV_MONARCH = 0x00000025

# 6 3/4 Envelope 3 5/8 x 6 1/2 in
DMPAPER_ENV_PERSONAL = 0x00000026

# US Std Fanfold 14 7/8 x 11 in
DMPAPER_FANFOLD_US = 0x00000027

# German Std Fanfold 8 1/2 x 12 in
DMPAPER_FANFOLD_STD_GERMAN = 0x00000028

# German Legal Fanfold 8 1/2 x 13 in
DMPAPER_FANFOLD_LGL_GERMAN = 0x00000029

# B4 (ISO) 250 x 353 mm
DMPAPER_ISO_B4 = 0x0000002A

# Japanese Postcard 100 x 148 mm
DMPAPER_JAPANESE_POSTCARD = 0x0000002B

# 9 x 11 in
DMPAPER_9X11 = 0x0000002C

# 10 x 11 in
DMPAPER_10X11 = 0x0000002D

# 15 x 11 in
DMPAPER_15X11 = 0x0000002E

# Envelope Invite 220 x 220 mm
DMPAPER_ENV_INVITE = 0x0000002F

# RESERVED--DO NOT USE
DMPAPER_RESERVED_48 = 0x00000030

# RESERVED--DO NOT USE
DMPAPER_RESERVED_49 = 0x00000031

# Letter Extra 9 x 12 in
DMPAPER_LETTER_EXTRA = 0x00000032

# Legal Extra 9 x 15 in
DMPAPER_LEGAL_EXTRA = 0x00000033

# Tabloid Extra 11.69 x 18 in
DMPAPER_TABLOID_EXTRA = 0x00000034

# A4 Extra 9.27 x 12.69 in
DMPAPER_A4_EXTRA = 0x00000035

# Letter Transverse 8 x 11 in
DMPAPER_LETTER_TRANSVERSE = 0x00000036

# A4 Transverse 210 x 297 mm
DMPAPER_A4_TRANSVERSE = 0x00000037

# Letter Extra Transverse 9 x 12 in
DMPAPER_LETTER_EXTRA_TRANSVERSE = 0x00000038

# SuperA/SuperA/A4 227 x 356 mm
DMPAPER_A_PLUS = 0x00000039

# SuperB/SuperB/A3 305 x 487 mm
DMPAPER_B_PLUS = 0x0000003A

# Letter Plus 8.5 x 12.69 in
DMPAPER_LETTER_PLUS = 0x0000003B

# A4 Plus 210 x 330 mm
DMPAPER_A4_PLUS = 0x0000003C

# A5 Transverse 148 x 210 mm
DMPAPER_A5_TRANSVERSE = 0x0000003D

# B5 (JIS) Transverse 182 x 257 mm
DMPAPER_B5_TRANSVERSE = 0x0000003E

# A3 Extra 322 x 445 mm
DMPAPER_A3_EXTRA = 0x0000003F

# A5 Extra 174 x 235 mm
DMPAPER_A5_EXTRA = 0x00000040

# B5 (ISO) Extra 201 x 276 mm
DMPAPER_B5_EXTRA = 0x00000041

# A2 420 x 594 mm
DMPAPER_A2 = 0x00000042

# A3 Transverse 297 x 420 mm
DMPAPER_A3_TRANSVERSE = 0x00000043

# A3 Extra Transverse 322 x 445 mm
DMPAPER_A3_EXTRA_TRANSVERSE = 0x00000044

# Japanese Double Postcard 200 x 148 mm
DMPAPER_DBL_JAPANESE_POSTCARD = 0x00000045

# A6 105 x 148 mm
DMPAPER_A6 = 0x00000046

# Japanese Envelope Kaku #2
DMPAPER_JENV_KAKU2 = 0x00000047

# Japanese Envelope Kaku #3
DMPAPER_JENV_KAKU3 = 0x00000048

# Japanese Envelope Chou #3
DMPAPER_JENV_CHOU3 = 0x00000049

# Japanese Envelope Chou #4
DMPAPER_JENV_CHOU4 = 0x0000004A

# Letter Rotated 11 x 8 1/2 11 in
DMPAPER_LETTER_ROTATED = 0x0000004B

# A3 Rotated 420 x 297 mm
DMPAPER_A3_ROTATED = 0x0000004C

# A4 Rotated 297 x 210 mm
DMPAPER_A4_ROTATED = 0x0000004D

# A5 Rotated 210 x 148 mm
DMPAPER_A5_ROTATED = 0x0000004E

# B4 (JIS) Rotated 364 x 257 mm
DMPAPER_B4_JIS_ROTATED = 0x0000004F

# B5 (JIS) Rotated 257 x 182 mm
DMPAPER_B5_JIS_ROTATED = 0x00000050

# Japanese Postcard Rotated 148 x 100 mm
DMPAPER_JAPANESE_POSTCARD_ROTATED = 0x00000051

# Double Japanese Postcard Rotated 148 x 200 mm
DMPAPER_DBL_JAPANESE_POSTCARD_ROTATED = 0x00000052

# A6 Rotated 148 x 105 mm
DMPAPER_A6_ROTATED = 0x00000053

# Japanese Envelope Kaku #2 Rotated
DMPAPER_JENV_KAKU2_ROTATED = 0x00000054

# Japanese Envelope Kaku #3 Rotated
DMPAPER_JENV_KAKU3_ROTATED = 0x00000055

# Japanese Envelope Chou #3 Rotated
DMPAPER_JENV_CHOU3_ROTATED = 0x00000056

# Japanese Envelope Chou #4 Rotated
DMPAPER_JENV_CHOU4_ROTATED = 0x00000057

# B6 (JIS) 128 x 182 mm
DMPAPER_B6_JIS = 0x00000058

# B6 (JIS) Rotated 182 x 128 mm
DMPAPER_B6_JIS_ROTATED = 0x00000059

# 12 x 11 in
DMPAPER_12X11 = 0x0000005A

# Japanese Envelope You #4
DMPAPER_JENV_YOU4 = 0x0000005B

# Japanese Envelope You #4 Rotated
DMPAPER_JENV_YOU4_ROTATED = 0x0000005C

# PRC 16K 146 x 215 mm
DMPAPER_P16K = 0x0000005D

# PRC 32K 97 x 151 mm
DMPAPER_P32K = 0x0000005E

# PRC 32K(Big) 97 x 151 mm
DMPAPER_P32KBIG = 0x0000005F

# PRC Envelope #1 102 x 165 mm
DMPAPER_PENV_1 = 0x00000060

# PRC Envelope #2 102 x 176 mm
DMPAPER_PENV_2 = 0x00000061

# PRC Envelope #3 125 x 176 mm
DMPAPER_PENV_3 = 0x00000062

# PRC Envelope #4 110 x 208 mm
DMPAPER_PENV_4 = 0x00000063

# PRC Envelope #5 110 x 220 mm
DMPAPER_PENV_5 = 0x00000064

# PRC Envelope #6 120 x 230 mm
DMPAPER_PENV_6 = 0x00000065

# PRC Envelope #7 160 x 230 mm
DMPAPER_PENV_7 = 0x00000066

# PRC Envelope #8 120 x 309 mm
DMPAPER_PENV_8 = 0x00000067

# PRC Envelope #9 229 x 324 mm
DMPAPER_PENV_9 = 0x00000068

# PRC Envelope #10 324 x 458 mm
DMPAPER_PENV_10 = 0x00000069

# PRC 16K Rotated
DMPAPER_P16K_ROTATED = 0x0000006A

# PRC 32K Rotated
DMPAPER_P32K_ROTATED = 0x0000006B

# PRC 32K(Big) Rotated
DMPAPER_P32KBIG_ROTATED = 0x0000006C

# PRC Envelope #1 Rotated 165 x 102 mm
DMPAPER_PENV_1_ROTATED = 0x0000006D

# PRC Envelope #2 Rotated 176 x 102 mm
DMPAPER_PENV_2_ROTATED = 0x0000006E

# PRC Envelope #3 Rotated 176 x 125 mm
DMPAPER_PENV_3_ROTATED = 0x0000006F

# PRC Envelope #4 Rotated 208 x 110 mm
DMPAPER_PENV_4_ROTATED = 0x00000070

# PRC Envelope #5 Rotated 220 x 110 mm
DMPAPER_PENV_5_ROTATED = 0x00000071

# PRC Envelope #6 Rotated 230 x 120 mm
DMPAPER_PENV_6_ROTATED = 0x00000072

# PRC Envelope #7 Rotated 230 x 160 mm
DMPAPER_PENV_7_ROTATED = 0x00000073

# PRC Envelope #8 Rotated 309 x 120 mm
DMPAPER_PENV_8_ROTATED = 0x00000074

# PRC Envelope #9 Rotated 324 x 229 mm
DMPAPER_PENV_9_ROTATED = 0x00000075

# PRC Envelope #10 Rotated 458 x 324 mm
DMPAPER_PENV_10_ROTATED = 0x00000076
DMPAPER_LAST = DMPAPER_PENV_10_ROTATED
DMPAPER_USER = 0x00000100
DMBIN_UPPER = 0x00000001
DMBIN_FIRST = DMBIN_UPPER
DMBIN_ONLYONE = 0x00000001
DMBIN_LOWER = 0x00000002
DMBIN_MIDDLE = 0x00000003
DMBIN_MANUAL = 0x00000004
DMBIN_ENVELOPE = 0x00000005
DMBIN_ENVMANUAL = 0x00000006
DMBIN_AUTO = 0x00000007
DMBIN_TRACTOR = 0x00000008
DMBIN_SMALLFMT = 0x00000009
DMBIN_LARGEFMT = 0x0000000A
DMBIN_LARGECAPACITY = 0x0000000B
DMBIN_CASSETTE = 0x0000000E
DMBIN_FORMSOURCE = 0x0000000F
DMBIN_LAST = DMBIN_FORMSOURCE

# device specific bins start here
DMBIN_USER = 0x00000100
DMRES_DRAFT = -1
DMRES_LOW = -2
DMRES_MEDIUM = -3
DMRES_HIGH = -4
DMCOLOR_MONOCHROME = 0x00000001
DMCOLOR_COLOR = 0x00000002
DMDUP_SIMPLEX = 0x00000001
DMDUP_VERTICAL = 0x00000002
DMDUP_HORIZONTAL = 0x00000003

# print TT fonts as graphics
DMTT_BITMAP = 0x00000001

# download TT fonts as soft fonts
DMTT_DOWNLOAD = 0x00000002

# substitute device fonts for TT fonts
DMTT_SUBDEV = 0x00000003

# download TT fonts as outline soft fonts
DMTT_DOWNLOAD_OUTLINE = 0x00000004
DMCOLLATE_FALSE = 0x00000000
DMCOLLATE_TRUE = 0x00000001
DMDO_DEFAULT = 0x00000000
DMDO_90 = 0x00000001
DMDO_180 = 0x00000002
DMDO_270 = 0x00000003
DMDFO_DEFAULT = 0x00000000
DMDFO_STRETCH = 0x00000001
DMDFO_CENTER = 0x00000002
DM_INTERLACED = 0x00000002
DMDISPLAYFLAGS_TEXTMODE = 0x00000004
DMNUP_SYSTEM = 0x00000001
DMNUP_ONEUP = 0x00000002

# ICM disabled
DMICMMETHOD_NONE = 0x00000001

# ICM handled by system
DMICMMETHOD_SYSTEM = 0x00000002

# ICM handled by driver
DMICMMETHOD_DRIVER = 0x00000003

# ICM handled by device
DMICMMETHOD_DEVICE = 0x00000004

# Device-specific methods start here
DMICMMETHOD_USER = 0x00000100

# Maximize color saturation
DMICM_SATURATE = 0x00000001

# Maximize color contrast
DMICM_CONTRAST = 0x00000002

# Use specific color metric
DMICM_COLORIMETRIC = 0x00000003

# Use specific color metric
DMICM_ABS_COLORIMETRIC = 0x00000004

# Device-specific intents start here
DMICM_USER = 0x00000100

# Standard paper
DMMEDIA_STANDARD = 0x00000001

# Transparency
DMMEDIA_TRANSPARENCY = 0x00000002

# Glossy paper
DMMEDIA_GLOSSY = 0x00000003

# Device-specific media start here
DMMEDIA_USER = 0x00000100

# No dithering
DMDITHER_NONE = 0x00000001

# Dither with a coarse brush
DMDITHER_COARSE = 0x00000002

# Dither with a fine brush
DMDITHER_FINE = 0x00000003

# LineArt dithering
DMDITHER_LINEART = 0x00000004

# LineArt dithering
DMDITHER_ERRORDIFFUSION = 0x00000005

# LineArt dithering
DMDITHER_RESERVED6 = 0x00000006

# LineArt dithering
DMDITHER_RESERVED7 = 0x00000007

# LineArt dithering
DMDITHER_RESERVED8 = 0x00000008

# LineArt dithering
DMDITHER_RESERVED9 = 0x00000009

# Device does grayscaling
DMDITHER_GRAYSCALE = 0x0000000A

# Device-specific dithers start here
DMDITHER_USER = 0x00000100


# noinspection PyTypeChecker
class _DISPLAY_DEVICEA(ctypes.Structure):
    _fields_ = [
        ('cb', DWORD),
        ('DeviceName', CHAR * 32),
        ('DeviceString', CHAR * 128),
        ('StateFlags', DWORD),
        ('DeviceID', CHAR * 128),
        ('DeviceKey', CHAR * 128),
    ]


DISPLAY_DEVICEA = _DISPLAY_DEVICEA
PDISPLAY_DEVICEA = POINTER(_DISPLAY_DEVICEA)
LPDISPLAY_DEVICEA = POINTER(_DISPLAY_DEVICEA)


# noinspection PyTypeChecker
class _DISPLAY_DEVICEW(ctypes.Structure):
    _fields_ = [
        ('cb', DWORD),
        ('DeviceName', WCHAR * 32),
        ('DeviceString', WCHAR * 128),
        ('StateFlags', DWORD),
        ('DeviceID', WCHAR * 128),
        ('DeviceKey', WCHAR * 128),
    ]


DISPLAY_DEVICEW = _DISPLAY_DEVICEW
PDISPLAY_DEVICEW = POINTER(_DISPLAY_DEVICEW)
LPDISPLAY_DEVICEW = POINTER(_DISPLAY_DEVICEW)


DISPLAY_DEVICE_ATTACHED_TO_DESKTOP = 0x00000001
DISPLAY_DEVICE_MULTI_DRIVER = 0x00000002
DISPLAY_DEVICE_PRIMARY_DEVICE = 0x00000004
DISPLAY_DEVICE_MIRRORING_DRIVER = 0x00000008
DISPLAY_DEVICE_VGA_COMPATIBLE = 0x00000010
DISPLAY_DEVICE_REMOVABLE = 0x00000020
DISPLAY_DEVICE_MODESPRUNED = 0x08000000
DISPLAY_DEVICE_REMOTE = 0x04000000
DISPLAY_DEVICE_DISCONNECT = 0x02000000
DISPLAY_DEVICE_TS_COMPATIBLE = 0x00200000
DISPLAY_DEVICE_UNSAFE_MODES_ON = 0x00080000
DISPLAY_DEVICE_ACTIVE = 0x00000001
DISPLAY_DEVICE_ATTACHED = 0x00000002
RDH_RECTANGLES = 0x00000001


class _RGNDATAHEADER(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('iType', DWORD),
        ('nCount', DWORD),
        ('nRgnSize', DWORD),
        ('rcBound', RECT),
    ]


RGNDATAHEADER = _RGNDATAHEADER
PRGNDATAHEADER = POINTER(_RGNDATAHEADER)


# noinspection PyTypeChecker
class _RGNDATA(ctypes.Structure):
    _fields_ = [
        ('rdh', RGNDATAHEADER),
        ('Buffer', CHAR * 1),
    ]


RGNDATA = _RGNDATA
PRGNDATA = POINTER(_RGNDATA)


SYSRGN = 0x00000004


class _ABC(ctypes.Structure):
    _fields_ = [
        ('abcA', INT),
        ('abcB', UINT),
        ('abcC', INT),
    ]


ABC = _ABC
PABC = POINTER(_ABC)


class _ABCFLOAT(ctypes.Structure):
    _fields_ = [
        ('abcfA', FLOAT),
        ('abcfB', FLOAT),
        ('abcfC', FLOAT),
    ]


ABCFLOAT = _ABCFLOAT
PABCFLOAT = POINTER(_ABCFLOAT)


class _OUTLINETEXTMETRICA(ctypes.Structure):
    _fields_ = [
        ('otmSize', UINT),
        ('otmTextMetrics', TEXTMETRICA),
        ('otmFiller', BYTE),
        ('otmPanoseNumber', PANOSE),
        ('otmfsSelection', UINT),
        ('otmfsType', UINT),
        ('otmsCharSlopeRise', INT),
        ('otmsCharSlopeRun', INT),
        ('otmItalicAngle', INT),
        ('otmEMSquare', UINT),
        ('otmAscent', INT),
        ('otmDescent', INT),
        ('otmLineGap', UINT),
        ('otmsCapEmHeight', UINT),
        ('otmsXHeight', UINT),
        ('otmrcFontBox', RECT),
        ('otmMacAscent', INT),
        ('otmMacDescent', INT),
        ('otmMacLineGap', UINT),
        ('otmusMinimumPPEM', UINT),
        ('otmptSubscriptSize', POINT),
        ('otmptSubscriptOffset', POINT),
        ('otmptSuperscriptSize', POINT),
        ('otmptSuperscriptOffset', POINT),
        ('otmsStrikeoutSize', UINT),
        ('otmsStrikeoutPosition', INT),
        ('otmsUnderscoreSize', INT),
        ('otmsUnderscorePosition', INT),
        ('otmpFamilyName', PSTR),
        ('otmpFaceName', PSTR),
        ('otmpStyleName', PSTR),
        ('otmpFullName', PSTR),
    ]


OUTLINETEXTMETRICA = _OUTLINETEXTMETRICA
POUTLINETEXTMETRICA = POINTER(_OUTLINETEXTMETRICA)


class _OUTLINETEXTMETRICW(ctypes.Structure):
    _fields_ = [
        ('otmSize', UINT),
        ('otmTextMetrics', TEXTMETRICW),
        ('otmFiller', BYTE),
        ('otmPanoseNumber', PANOSE),
        ('otmfsSelection', UINT),
        ('otmfsType', UINT),
        ('otmsCharSlopeRise', INT),
        ('otmsCharSlopeRun', INT),
        ('otmItalicAngle', INT),
        ('otmEMSquare', UINT),
        ('otmAscent', INT),
        ('otmDescent', INT),
        ('otmLineGap', UINT),
        ('otmsCapEmHeight', UINT),
        ('otmsXHeight', UINT),
        ('otmrcFontBox', RECT),
        ('otmMacAscent', INT),
        ('otmMacDescent', INT),
        ('otmMacLineGap', UINT),
        ('otmusMinimumPPEM', UINT),
        ('otmptSubscriptSize', POINT),
        ('otmptSubscriptOffset', POINT),
        ('otmptSuperscriptSize', POINT),
        ('otmptSuperscriptOffset', POINT),
        ('otmsStrikeoutSize', UINT),
        ('otmsStrikeoutPosition', INT),
        ('otmsUnderscoreSize', INT),
        ('otmsUnderscorePosition', INT),
        ('otmpFamilyName', PSTR),
        ('otmpFaceName', PSTR),
        ('otmpStyleName', PSTR),
        ('otmpFullName', PSTR),
    ]


OUTLINETEXTMETRICW = _OUTLINETEXTMETRICW
POUTLINETEXTMETRICW = POINTER(_OUTLINETEXTMETRICW)


class tagPOLYTEXTA(ctypes.Structure):
    _fields_ = [
        ('x', INT),
        ('y', INT),
        ('n', UINT),
        ('lpstr', LPCSTR),
        ('uiFlags', UINT),
        ('rcl', RECT),
        ('*pdx', INT),
    ]


POLYTEXTA = tagPOLYTEXTA
PPOLYTEXTA = POINTER(tagPOLYTEXTA)


class tagPOLYTEXTW(ctypes.Structure):
    _fields_ = [
        ('x', INT),
        ('y', INT),
        ('n', UINT),
        ('lpstr', LPCWSTR),
        ('uiFlags', UINT),
        ('rcl', RECT),
        ('*pdx', INT),
    ]


POLYTEXTW = tagPOLYTEXTW
PPOLYTEXTW = POINTER(tagPOLYTEXTW)


class _FIXED(ctypes.Structure):
    _fields_ = [
        ('fract', WORD),
        ('value', SHORT),
        ('value', SHORT),
        ('fract', WORD),
    ]


FIXED = _FIXED


class _MAT2(ctypes.Structure):
    _fields_ = [
        ('eM11', FIXED),
        ('eM12', FIXED),
        ('eM21', FIXED),
        ('eM22', FIXED),
    ]


MAT2 = _MAT2


class _GLYPHMETRICS(ctypes.Structure):
    _fields_ = [
        ('gmBlackBoxX', UINT),
        ('gmBlackBoxY', UINT),
        ('gmptGlyphOrigin', POINT),
        ('gmCellIncX', SHORT),
        ('gmCellIncY', SHORT),
    ]


GLYPHMETRICS = _GLYPHMETRICS


GGO_METRICS = 0x00000000
GGO_BITMAP = 0x00000001
GGO_NATIVE = 0x00000002
GGO_BEZIER = 0x00000003
GGO_GRAY2_BITMAP = 0x00000004
GGO_GRAY4_BITMAP = 0x00000005
GGO_GRAY8_BITMAP = 0x00000006
GGO_GLYPH_INDEX = 0x00000080
GGO_UNHINTED = 0x00000100
TT_POLYGON_TYPE = 0x00000018
TT_PRIM_LINE = 0x00000001
TT_PRIM_QSPLINE = 0x00000002
TT_PRIM_CSPLINE = 0x00000003


class tagPOINTFX(ctypes.Structure):
    _fields_ = [
        ('x', FIXED),
        ('y', FIXED),
    ]


POINTFX = tagPOINTFX


# noinspection PyTypeChecker
class tagTTPOLYCURVE(ctypes.Structure):
    _fields_ = [
        ('wType', WORD),
        ('cpfx', WORD),
        ('apfx', POINTFX * 1),
    ]


TTPOLYCURVE = tagTTPOLYCURVE


class tagTTPOLYGONHEADER(ctypes.Structure):
    _fields_ = [
        ('cb', DWORD),
        ('dwType', DWORD),
        ('pfxStart', POINTFX),
    ]


TTPOLYGONHEADER = tagTTPOLYGONHEADER


GCP_DBCS = 0x00000001
GCP_REORDER = 0x00000002
GCP_USEKERNING = 0x00000008
GCP_GLYPHSHAPE = 0x00000010
GCP_LIGATE = 0x00000020
GCP_DIACRITIC = 0x00000100
GCP_KASHIDA = 0x00000400
GCP_ERROR = 0x00008000
FLI_MASK = 0x0000103B
GCP_JUSTIFY = 0x00010000
FLI_GLYPHS = 0x00040000
GCP_CLASSIN = 0x00080000
GCP_MAXEXTENT = 0x00100000
GCP_JUSTIFYIN = 0x00200000
GCP_DISPLAYZWG = 0x00400000
GCP_SYMSWAPOFF = 0x00800000
GCP_NUMERICOVERRIDE = 0x01000000
GCP_NEUTRALOVERRIDE = 0x02000000
GCP_NUMERICSLATIN = 0x04000000
GCP_NUMERICSLOCAL = 0x08000000
GCPCLASS_LATIN = 0x00000001
GCPCLASS_HEBREW = 0x00000002
GCPCLASS_ARABIC = 0x00000002
GCPCLASS_NEUTRAL = 0x00000003
GCPCLASS_LOCALNUMBER = 0x00000004
GCPCLASS_LATINNUMBER = 0x00000005
GCPCLASS_LATINNUMERICTERMINATOR = 0x00000006
GCPCLASS_LATINNUMERICSEPARATOR = 0x00000007
GCPCLASS_NUMERICSEPARATOR = 0x00000008
GCPCLASS_PREBOUNDLTR = 0x00000080
GCPCLASS_PREBOUNDRTL = 0x00000040
GCPCLASS_POSTBOUNDLTR = 0x00000020
GCPCLASS_POSTBOUNDRTL = 0x00000010
GCPGLYPH_LINKBEFORE = 0x00008000
GCPGLYPH_LINKAFTER = 0x00004000


class tagGCP_RESULTSA(ctypes.Structure):
    _fields_ = [
        ('lStructSize', DWORD),
        ('lpOutString', LPSTR),
        ('lpOrder', UINT),
        ('lpDx', INT),
        ('lpCaretPos', INT),
        ('lpClass', LPSTR),
        ('lpGlyphs', LPWSTR),
        ('nGlyphs', UINT),
        ('nMaxFit', INT),
    ]


GCP_RESULTSA = tagGCP_RESULTSA


class tagGCP_RESULTSW(ctypes.Structure):
    _fields_ = [
        ('lStructSize', DWORD),
        ('lpOutString', LPWSTR),
        ('lpOrder', UINT),
        ('lpDx', INT),
        ('lpCaretPos', INT),
        ('lpClass', LPSTR),
        ('lpGlyphs', LPWSTR),
        ('nGlyphs', UINT),
        ('nMaxFit', INT),
    ]


GCP_RESULTSW = tagGCP_RESULTSW


class _RASTERIZER_STATUS(ctypes.Structure):
    _fields_ = [
        ('nSize', SHORT),
        ('wFlags', SHORT),
        ('nLanguageID', SHORT),
    ]


RASTERIZER_STATUS = _RASTERIZER_STATUS


TT_AVAILABLE = 0x00000001
TT_ENABLED = 0x00000002


class tagPIXELFORMATDESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('nSize', WORD),
        ('nVersion', WORD),
        ('dwFlags', DWORD),
        ('iPixelType', BYTE),
        ('cColorBits', BYTE),
        ('cRedBits', BYTE),
        ('cRedShift', BYTE),
        ('cGreenBits', BYTE),
        ('cGreenShift', BYTE),
        ('cBlueBits', BYTE),
        ('cBlueShift', BYTE),
        ('cAlphaBits', BYTE),
        ('cAlphaShift', BYTE),
        ('cAccumBits', BYTE),
        ('cAccumRedBits', BYTE),
        ('cAccumGreenBits', BYTE),
        ('cAccumBlueBits', BYTE),
        ('cAccumAlphaBits', BYTE),
        ('cDepthBits', BYTE),
        ('cStencilBits', BYTE),
        ('cAuxBuffers', BYTE),
        ('iLayerType', BYTE),
        ('bReserved', BYTE),
        ('dwLayerMask', DWORD),
        ('dwVisibleMask', DWORD),
        ('dwDamageMask', DWORD),
    ]


PIXELFORMATDESCRIPTOR = tagPIXELFORMATDESCRIPTOR
PPIXELFORMATDESCRIPTOR = POINTER(tagPIXELFORMATDESCRIPTOR)


PFD_TYPE_RGBA = 0x00000000
PFD_TYPE_COLORINDEX = 0x00000001
PFD_MAIN_PLANE = 0x00000000
PFD_OVERLAY_PLANE = 0x00000001
PFD_UNDERLAY_PLANE = -1
PFD_DOUBLEBUFFER = 0x00000001
PFD_STEREO = 0x00000002
PFD_DRAW_TO_WINDOW = 0x00000004
PFD_DRAW_TO_BITMAP = 0x00000008
PFD_SUPPORT_GDI = 0x00000010
PFD_SUPPORT_OPENGL = 0x00000020
PFD_GENERIC_FORMAT = 0x00000040
PFD_NEED_PALETTE = 0x00000080
PFD_NEED_SYSTEM_PALETTE = 0x00000100
PFD_SWAP_EXCHANGE = 0x00000200
PFD_SWAP_COPY = 0x00000400
PFD_SWAP_LAYER_BUFFERS = 0x00000800
PFD_GENERIC_ACCELERATED = 0x00001000
PFD_SUPPORT_DIRECTDRAW = 0x00002000
PFD_DIRECT3D_ACCELERATED = 0x00004000
PFD_SUPPORT_COMPOSITION = 0x00008000
PFD_DEPTH_DONTCARE = 0x20000000
PFD_DOUBLEBUFFER_DONTCARE = 0x40000000
PFD_STEREO_DONTCARE = 0x80000000
DM_UPDATE = 0x00000001
DM_COPY = 0x00000002
DM_PROMPT = 0x00000004
DM_MODIFY = 0x00000008
DM_IN_BUFFER = DM_MODIFY
DM_IN_PROMPT = DM_PROMPT
DM_OUT_BUFFER = DM_COPY
DM_OUT_DEFAULT = DM_UPDATE
DC_FIELDS = 0x00000001
DC_PAPERS = 0x00000002
DC_PAPERSIZE = 0x00000003
DC_MINEXTENT = 0x00000004
DC_MAXEXTENT = 0x00000005
DC_BINS = 0x00000006
DC_DUPLEX = 0x00000007
DC_SIZE = 0x00000008
DC_EXTRA = 0x00000009
DC_VERSION = 0x0000000A
DC_DRIVER = 0x0000000B
DC_BINNAMES = 0x0000000C
DC_ENUMRESOLUTIONS = 0x0000000D
DC_FILEDEPENDENCIES = 0x0000000E
DC_TRUETYPE = 0x0000000F
DC_PAPERNAMES = 0x00000010
DC_ORIENTATION = 0x00000011
DC_COPIES = 0x00000012
DC_BINADJUST = 0x00000013
DC_EMF_COMPLIANT = 0x00000014
DC_DATATYPE_PRODUCED = 0x00000015
DC_COLLATE = 0x00000016
DC_MANUFACTURER = 0x00000017
DC_MODEL = 0x00000018
DC_PERSONALITY = 0x00000019
DC_PRINTRATE = 0x0000001A
DC_PRINTRATEUNIT = 0x0000001B
PRINTRATEUNIT_PPM = 0x00000001
PRINTRATEUNIT_CPS = 0x00000002
PRINTRATEUNIT_LPM = 0x00000003
PRINTRATEUNIT_IPM = 0x00000004
DC_PRINTERMEM = 0x0000001C
DC_MEDIAREADY = 0x0000001D
DC_STAPLE = 0x0000001E
DC_PRINTRATEPPM = 0x0000001F
DC_COLORDEVICE = 0x00000020
DC_NUP = 0x00000021
DC_MEDIATYPENAMES = 0x00000022
DC_MEDIATYPES = 0x00000023
DCTT_BITMAP = 0x0000001
DCTT_DOWNLOAD = 0x0000002
DCTT_SUBDEV = 0x0000004
DCTT_DOWNLOAD_OUTLINE = 0x0000008
DCBA_FACEUPNONE = 0x00000000
DCBA_FACEUPCENTER = 0x00000001
DCBA_FACEUPLEFT = 0x00000002
DCBA_FACEUPRIGHT = 0x00000003
DCBA_FACEDOWNNONE = 0x00000100
DCBA_FACEDOWNCENTER = 0x00000101
DCBA_FACEDOWNLEFT = 0x00000102
DCBA_FACEDOWNRIGHT = 0x00000103


class tagWCRANGE(ctypes.Structure):
    _fields_ = [
        ('wcLow', WCHAR),
        ('cGlyphs', USHORT),
    ]


WCRANGE = tagWCRANGE
PWCRANGE = POINTER(tagWCRANGE)


# noinspection PyTypeChecker
class tagGLYPHSET(ctypes.Structure):
    _fields_ = [
        ('cbThis', DWORD),
        ('flAccel', DWORD),
        ('cGlyphsSupported', DWORD),
        ('cRanges', DWORD),
        ('ranges', WCRANGE * 1),
    ]


GLYPHSET = tagGLYPHSET
PGLYPHSET = POINTER(tagGLYPHSET)


GS_8BIT_INDICES = 0x00000001
GGI_MARK_NONEXISTING_GLYPHS = 0x00000001
STAMP_DESIGNVECTOR = 0x8000000 + ord('D') + (ord('V') << 8)
STAMP_AXESLIST = 0x8000000 + ord('A') + (ord('L') << 8)
MM_MAX_NUMAXES = 0x00000010


# noinspection PyTypeChecker
class tagDESIGNVECTOR(ctypes.Structure):
    _fields_ = [
        ('dvReserved', DWORD),
        ('dvNumAxes', DWORD),
        ('dvValues', LONG * MM_MAX_NUMAXES),
    ]


DESIGNVECTOR = tagDESIGNVECTOR
PDESIGNVECTOR = POINTER(tagDESIGNVECTOR)


FR_PRIVATE = 0x00000010
FR_NOT_ENUM = 0x00000020
MM_MAX_AXES_NAMELEN = 0x00000010


# noinspection PyTypeChecker
class tagAXISINFOA(ctypes.Structure):
    _fields_ = [
        ('axMinValue', LONG),
        ('axMaxValue', LONG),
        ('axAxisName', BYTE * MM_MAX_AXES_NAMELEN),
    ]


AXISINFOA = tagAXISINFOA
PAXISINFOA = POINTER(tagAXISINFOA)


# noinspection PyTypeChecker
class tagAXISINFOW(ctypes.Structure):
    _fields_ = [
        ('axMinValue', LONG),
        ('axMaxValue', LONG),
        ('axAxisName', WCHAR * MM_MAX_AXES_NAMELEN),
    ]


AXISINFOW = tagAXISINFOW
PAXISINFOW = POINTER(tagAXISINFOW)


# noinspection PyTypeChecker
class tagAXESLISTA(ctypes.Structure):
    _fields_ = [
        ('axlReserved', DWORD),
        ('axlNumAxes', DWORD),
        ('axlAxisInfo', AXISINFOA * MM_MAX_NUMAXES),
    ]


AXESLISTA = tagAXESLISTA
PAXESLISTA = POINTER(tagAXESLISTA)


# noinspection PyTypeChecker
class tagAXESLISTW(ctypes.Structure):
    _fields_ = [
        ('axlReserved', DWORD),
        ('axlNumAxes', DWORD),
        ('axlAxisInfo', AXISINFOW * MM_MAX_NUMAXES),
    ]


AXESLISTW = tagAXESLISTW
PAXESLISTW = POINTER(tagAXESLISTW)


class tagENUMLOGFONTEXDVA(ctypes.Structure):
    _fields_ = [
        ('elfEnumLogfontEx', ENUMLOGFONTEXA),
        ('elfDesignVector', DESIGNVECTOR),
    ]


ENUMLOGFONTEXDVA = tagENUMLOGFONTEXDVA
PENUMLOGFONTEXDVA = POINTER(tagENUMLOGFONTEXDVA)


class tagENUMLOGFONTEXDVW(ctypes.Structure):
    _fields_ = [
        ('elfEnumLogfontEx', ENUMLOGFONTEXW),
        ('elfDesignVector', DESIGNVECTOR),
    ]


ENUMLOGFONTEXDVW = tagENUMLOGFONTEXDVW
PENUMLOGFONTEXDVW = POINTER(tagENUMLOGFONTEXDVW)


class tagENUMTEXTMETRICA(ctypes.Structure):
    _fields_ = [
        ('etmNewTextMetricEx', NEWTEXTMETRICEXA),
        ('etmAxesList', AXESLISTA),
    ]


ENUMTEXTMETRICA = tagENUMTEXTMETRICA
PENUMTEXTMETRICA = POINTER(tagENUMTEXTMETRICA)


class tagENUMTEXTMETRICW(ctypes.Structure):
    _fields_ = [
        ('etmNewTextMetricEx', NEWTEXTMETRICEXW),
        ('etmAxesList', AXESLISTW),
    ]


ENUMTEXTMETRICW = tagENUMTEXTMETRICW
PENUMTEXTMETRICW = POINTER(tagENUMTEXTMETRICW)


GDIREGISTERDDRAWPACKETVERSION = 0x00000001


DDRAWMARSHCALLBACKMARSHAL = HRESULT
DDRAWMARSHCALLBACKUNMARSHAL = HRESULT
DDRAWMARSHCALLBACKRELEASE = HRESULT


class GDIREGISTERDDRAWPACKET(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwVersion', DWORD),
        ('pfnDdMarshal', DDRAWMARSHCALLBACKMARSHAL),
        ('pfnDdUnmarshal', DDRAWMARSHCALLBACKUNMARSHAL),
        ('pfnDdRelease', DDRAWMARSHCALLBACKRELEASE),
    ]


PGDIREGISTERDDRAWPACKET = POINTER(GDIREGISTERDDRAWPACKET)


COLOR16 = USHORT


class _TRIVERTEX(ctypes.Structure):
    _fields_ = [
        ('x', LONG),
        ('y', LONG),
        ('Red', COLOR16),
        ('Green', COLOR16),
        ('Blue', COLOR16),
        ('Alpha', COLOR16),
    ]


TRIVERTEX = _TRIVERTEX
PTRIVERTEX = POINTER(_TRIVERTEX)
LPTRIVERTEX = POINTER(_TRIVERTEX)


class _GRADIENT_TRIANGLE(ctypes.Structure):
    _fields_ = [
        ('Vertex1', ULONG),
        ('Vertex2', ULONG),
        ('Vertex3', ULONG),
    ]


GRADIENT_TRIANGLE = _GRADIENT_TRIANGLE
PGRADIENT_TRIANGLE = POINTER(_GRADIENT_TRIANGLE)
LPGRADIENT_TRIANGLE = POINTER(_GRADIENT_TRIANGLE)


class _GRADIENT_RECT(ctypes.Structure):
    _fields_ = [
        ('UpperLeft', ULONG),
        ('LowerRight', ULONG),
    ]


GRADIENT_RECT = _GRADIENT_RECT
PGRADIENT_RECT = POINTER(_GRADIENT_RECT)
LPGRADIENT_RECT = POINTER(_GRADIENT_RECT)


class _BLENDFUNCTION(ctypes.Structure):
    _fields_ = [
        ('BlendOp', BYTE),
        ('BlendFlags', BYTE),
        ('SourceConstantAlpha', BYTE),
        ('AlphaFormat', BYTE),
    ]


BLENDFUNCTION = _BLENDFUNCTION
PBLENDFUNCTION = POINTER(_BLENDFUNCTION)


AC_SRC_OVER = 0x00000000
AC_SRC_ALPHA = 0x00000001
GRADIENT_FILL_RECT_H = 0x00000000
GRADIENT_FILL_RECT_V = 0x00000001
GRADIENT_FILL_TRIANGLE = 0x00000002
GRADIENT_FILL_OP_FLAG = 0x000000FF


# noinspection PyTypeChecker
class tagDIBSECTION(ctypes.Structure):
    _fields_ = [
        ('dsBm', BITMAP),
        ('dsBmih', BITMAPINFOHEADER),
        ('dsBitfields', DWORD * 3),
        ('dshSection', HANDLE),
        ('dsOffset', DWORD),
    ]


DIBSECTION = tagDIBSECTION
PDIBSECTION = POINTER(tagDIBSECTION)


CA_NEGATIVE = 0x00000001
CA_LOG_FILTER = 0x00000002
ILLUMINANT_DEVICE_DEFAULT = 0x00000000
ILLUMINANT_A = 0x00000001
ILLUMINANT_B = 0x00000002
ILLUMINANT_C = 0x00000003
ILLUMINANT_D50 = 0x00000004
ILLUMINANT_D55 = 0x00000005
ILLUMINANT_D65 = 0x00000006
ILLUMINANT_D75 = 0x00000007
ILLUMINANT_F2 = 0x00000008
ILLUMINANT_MAX_INDEX = ILLUMINANT_F2
ILLUMINANT_TUNGSTEN = ILLUMINANT_A
ILLUMINANT_DAYLIGHT = ILLUMINANT_C
ILLUMINANT_FLUORESCENT = ILLUMINANT_F2
ILLUMINANT_NTSC = ILLUMINANT_C
RGB_GAMMA_MIN = 0x00000540
RGB_GAMMA_MAX = 0x0000FDE8
REFERENCE_WHITE_MIN = 0x00001770
REFERENCE_WHITE_MAX = 0x00002710
REFERENCE_BLACK_MIN = 0x00000000
REFERENCE_BLACK_MAX = 0x00000FA0
COLOR_ADJ_MIN = -100
COLOR_ADJ_MAX = 0x00000064


class tagCOLORADJUSTMENT(ctypes.Structure):
    _fields_ = [
        ('caSize', WORD),
        ('caFlags', WORD),
        ('caIlluminantIndex', WORD),
        ('caRedGamma', WORD),
        ('caGreenGamma', WORD),
        ('caBlueGamma', WORD),
        ('caReferenceBlack', WORD),
        ('caReferenceWhite', WORD),
        ('caContrast', SHORT),
        ('caBrightness', SHORT),
        ('caColorfulness', SHORT),
        ('caRedGreenTint', SHORT),
    ]


COLORADJUSTMENT = tagCOLORADJUSTMENT
PCOLORADJUSTMENT = POINTER(tagCOLORADJUSTMENT)


class _DOCINFOA(ctypes.Structure):
    _fields_ = [
        ('cbSize', INT),
        ('lpszDocName', LPCSTR),
        ('lpszOutput', LPCSTR),
        ('lpszDatatype', LPCSTR),
        ('fwType', DWORD),
    ]


DOCINFOA = _DOCINFOA
LPDOCINFOA = POINTER(_DOCINFOA)


class _DOCINFOW(ctypes.Structure):
    _fields_ = [
        ('cbSize', INT),
        ('lpszDocName', LPCWSTR),
        ('lpszOutput', LPCWSTR),
        ('lpszDatatype', LPCWSTR),
        ('fwType', DWORD),
    ]


DOCINFOW = _DOCINFOW
LPDOCINFOW = POINTER(_DOCINFOW)


DI_APPBANDING = 0x00000001
DI_ROPS_READ_DESTINATION = 0x00000002
FONTMAPPER_MAX = 0x0000000A


class tagKERNINGPAIR(ctypes.Structure):
    _fields_ = [
        ('wFirst', WORD),
        ('wSecond', WORD),
        ('iKernAmount', INT),
    ]


KERNINGPAIR = tagKERNINGPAIR
LPKERNINGPAIR = POINTER(tagKERNINGPAIR)


ICM_OFF = 0x00000001
ICM_ON = 0x00000002
ICM_QUERY = 0x00000003
ICM_DONE_OUTSIDEDC = 0x00000004
ENHMETA_SIGNATURE = 0x20454D46
ENHMETA_STOCK_OBJECT = 0x80000000
EMR_HEADER = 0x00000001
EMR_POLYBEZIER = 0x00000002
EMR_POLYGON = 0x00000003
EMR_POLYLINE = 0x00000004
EMR_POLYBEZIERTO = 0x00000005
EMR_POLYLINETO = 0x00000006
EMR_POLYPOLYLINE = 0x00000007
EMR_POLYPOLYGON = 0x00000008
EMR_SETWINDOWEXTEX = 0x00000009
EMR_SETWINDOWORGEX = 0x0000000A
EMR_SETVIEWPORTEXTEX = 0x0000000B
EMR_SETVIEWPORTORGEX = 0x0000000C
EMR_SETBRUSHORGEX = 0x0000000D
EMR_EOF = 0x0000000E
EMR_SETPIXELV = 0x0000000F
EMR_SETMAPPERFLAGS = 0x00000010
EMR_SETMAPMODE = 0x00000011
EMR_SETBKMODE = 0x00000012
EMR_SETPOLYFILLMODE = 0x00000013
EMR_SETROP2 = 0x00000014
EMR_SETSTRETCHBLTMODE = 0x00000015
EMR_SETTEXTALIGN = 0x00000016
EMR_SETCOLORADJUSTMENT = 0x00000017
EMR_SETTEXTCOLOR = 0x00000018
EMR_SETBKCOLOR = 0x00000019
EMR_OFFSETCLIPRGN = 0x0000001A
EMR_MOVETOEX = 0x0000001B
EMR_SETMETARGN = 0x0000001C
EMR_EXCLUDECLIPRECT = 0x0000001D
EMR_INTERSECTCLIPRECT = 0x0000001E
EMR_SCALEVIEWPORTEXTEX = 0x0000001F
EMR_SCALEWINDOWEXTEX = 0x00000020
EMR_SAVEDC = 0x00000021
EMR_RESTOREDC = 0x00000022
EMR_SETWORLDTRANSFORM = 0x00000023
EMR_MODIFYWORLDTRANSFORM = 0x00000024
EMR_SELECTOBJECT = 0x00000025
EMR_CREATEPEN = 0x00000026
EMR_CREATEBRUSHINDIRECT = 0x00000027
EMR_DELETEOBJECT = 0x00000028
EMR_ANGLEARC = 0x00000029
EMR_ELLIPSE = 0x0000002A
EMR_RECTANGLE = 0x0000002B
EMR_ROUNDRECT = 0x0000002C
EMR_ARC = 0x0000002D
EMR_CHORD = 0x0000002E
EMR_PIE = 0x0000002F
EMR_SELECTPALETTE = 0x00000030
EMR_CREATEPALETTE = 0x00000031
EMR_SETPALETTEENTRIES = 0x00000032
EMR_RESIZEPALETTE = 0x00000033
EMR_REALIZEPALETTE = 0x00000034
EMR_EXTFLOODFILL = 0x00000035
EMR_LINETO = 0x00000036
EMR_ARCTO = 0x00000037
EMR_POLYDRAW = 0x00000038
EMR_SETARCDIRECTION = 0x00000039
EMR_SETMITERLIMIT = 0x0000003A
EMR_BEGINPATH = 0x0000003B
EMR_ENDPATH = 0x0000003C
EMR_CLOSEFIGURE = 0x0000003D
EMR_FILLPATH = 0x0000003E
EMR_STROKEANDFILLPATH = 0x0000003F
EMR_STROKEPATH = 0x00000040
EMR_FLATTENPATH = 0x00000041
EMR_WIDENPATH = 0x00000042
EMR_SELECTCLIPPATH = 0x00000043
EMR_ABORTPATH = 0x00000044
EMR_GDICOMMENT = 0x00000046
EMR_FILLRGN = 0x00000047
EMR_FRAMERGN = 0x00000048
EMR_INVERTRGN = 0x00000049
EMR_PAINTRGN = 0x0000004A
EMR_EXTSELECTCLIPRGN = 0x0000004B
EMR_BITBLT = 0x0000004C
EMR_STRETCHBLT = 0x0000004D
EMR_MASKBLT = 0x0000004E
EMR_PLGBLT = 0x0000004F
EMR_SETDIBITSTODEVICE = 0x00000050
EMR_STRETCHDIBITS = 0x00000051
EMR_EXTCREATEFONTINDIRECTW = 0x00000052
EMR_EXTTEXTOUTA = 0x00000053
EMR_EXTTEXTOUTW = 0x00000054
EMR_POLYBEZIER16 = 0x00000055
EMR_POLYGON16 = 0x00000056
EMR_POLYLINE16 = 0x00000057
EMR_POLYBEZIERTO16 = 0x00000058
EMR_POLYLINETO16 = 0x00000059
EMR_POLYPOLYLINE16 = 0x0000005A
EMR_POLYPOLYGON16 = 0x0000005B
EMR_POLYDRAW16 = 0x0000005C
EMR_CREATEMONOBRUSH = 0x0000005D
EMR_CREATEDIBPATTERNBRUSHPT = 0x0000005E
EMR_EXTCREATEPEN = 0x0000005F
EMR_POLYTEXTOUTA = 0x00000060
EMR_POLYTEXTOUTW = 0x00000061
EMR_SETICMMODE = 0x00000062
EMR_CREATECOLORSPACE = 0x00000063
EMR_SETCOLORSPACE = 0x00000064
EMR_DELETECOLORSPACE = 0x00000065
EMR_GLSRECORD = 0x00000066
EMR_GLSBOUNDEDRECORD = 0x00000067
EMR_PIXELFORMAT = 0x00000068
EMR_RESERVED_105 = 0x00000069
EMR_RESERVED_106 = 0x0000006A
EMR_RESERVED_107 = 0x0000006B
EMR_RESERVED_108 = 0x0000006C
EMR_RESERVED_109 = 0x0000006D
EMR_RESERVED_110 = 0x0000006E
EMR_COLORCORRECTPALETTE = 0x0000006F
EMR_SETICMPROFILEA = 0x00000070
EMR_SETICMPROFILEW = 0x00000071
EMR_ALPHABLEND = 0x00000072
EMR_SETLAYOUT = 0x00000073
EMR_TRANSPARENTBLT = 0x00000074
EMR_RESERVED_117 = 0x00000075
EMR_GRADIENTFILL = 0x00000076
EMR_RESERVED_119 = 0x00000077
EMR_RESERVED_120 = 0x00000078
EMR_COLORMATCHTOTARGETW = 0x00000079
EMR_CREATECOLORSPACEW = 0x0000007A
EMR_MIN = 0x00000001
EMR_MAX = 0x0000007A


class tagEMR(ctypes.Structure):
    _fields_ = [
        # Enhanced metafile record type
        ('iType', DWORD),
        # Length of the record in bytes.
        ('nSize', DWORD),
        # This must be a multiple of 4.
    ]


EMR = tagEMR
PEMR = POINTER(tagEMR)


class tagEMRTEXT(ctypes.Structure):
    _fields_ = [
        ('ptlReference', POINTL),
        ('nChars', DWORD),
        # Offset to the string
        ('offString', DWORD),
        ('fOptions', DWORD),
        ('rcl', RECTL),
        # Offset to the inter-character spacing array.
        ('offDx', DWORD),
        # This is always given.
    ]


EMRTEXT = tagEMRTEXT
PEMRTEXT = POINTER(tagEMRTEXT)


class tagABORTPATH(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
    ]


EMRABORTPATH = tagABORTPATH
PEMRABORTPATH = POINTER(tagABORTPATH)
EMRBEGINPATH = tagABORTPATH
PEMRBEGINPATH = POINTER(tagABORTPATH)
EMRENDPATH = tagABORTPATH
PEMRENDPATH = POINTER(tagABORTPATH)
EMRCLOSEFIGURE = tagABORTPATH
PEMRCLOSEFIGURE = POINTER(tagABORTPATH)
EMRFLATTENPATH = tagABORTPATH
PEMRFLATTENPATH = POINTER(tagABORTPATH)
EMRWIDENPATH = tagABORTPATH
PEMRWIDENPATH = POINTER(tagABORTPATH)
EMRSETMETARGN = tagABORTPATH
PEMRSETMETARGN = POINTER(tagABORTPATH)
EMRSAVEDC = tagABORTPATH
PEMRSAVEDC = POINTER(tagABORTPATH)
EMRREALIZEPALETTE = tagABORTPATH
PEMRREALIZEPALETTE = POINTER(tagABORTPATH)


class tagEMRSELECTCLIPPATH(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('iMode', DWORD),
    ]


EMRSELECTCLIPPATH = tagEMRSELECTCLIPPATH
PEMRSELECTCLIPPATH = POINTER(tagEMRSELECTCLIPPATH)
EMRSETBKMODE = tagEMRSELECTCLIPPATH
PEMRSETBKMODE = POINTER(tagEMRSELECTCLIPPATH)
EMRSETMAPMODE = tagEMRSELECTCLIPPATH
PEMRSETMAPMODE = POINTER(tagEMRSELECTCLIPPATH)
EMRSETLAYOUT = tagEMRSELECTCLIPPATH
PEMRSETLAYOUT = POINTER(tagEMRSELECTCLIPPATH)
EMRSETPOLYFILLMODE = tagEMRSELECTCLIPPATH
PEMRSETPOLYFILLMODE = POINTER(tagEMRSELECTCLIPPATH)
EMRSETROP2 = tagEMRSELECTCLIPPATH
PEMRSETROP2 = POINTER(tagEMRSELECTCLIPPATH)
EMRSETSTRETCHBLTMODE = tagEMRSELECTCLIPPATH
PEMRSETSTRETCHBLTMODE = POINTER(tagEMRSELECTCLIPPATH)
EMRSETICMMODE = tagEMRSELECTCLIPPATH
PEMRSETICMMODE = POINTER(tagEMRSELECTCLIPPATH)
EMRSETTEXTALIGN = tagEMRSELECTCLIPPATH
PEMRSETTEXTALIGN = POINTER(tagEMRSELECTCLIPPATH)


class tagEMRSETMITERLIMIT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('eMiterLimit', FLOAT),
    ]


EMRSETMITERLIMIT = tagEMRSETMITERLIMIT
PEMRSETMITERLIMIT = POINTER(tagEMRSETMITERLIMIT)


class tagEMRRESTOREDC(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Specifies a relative instance
        ('iRelative', LONG),
    ]


EMRRESTOREDC = tagEMRRESTOREDC
PEMRRESTOREDC = POINTER(tagEMRRESTOREDC)


class tagEMRSETARCDIRECTION(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Specifies the arc direction in the
        ('iArcDirection', DWORD),
        # advanced graphics mode.
    ]


EMRSETARCDIRECTION = tagEMRSETARCDIRECTION
PEMRSETARCDIRECTION = POINTER(tagEMRSETARCDIRECTION)


class tagEMRSETMAPPERFLAGS(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('dwFlags', DWORD),
    ]


EMRSETMAPPERFLAGS = tagEMRSETMAPPERFLAGS
PEMRSETMAPPERFLAGS = POINTER(tagEMRSETMAPPERFLAGS)


class tagEMRSETTEXTCOLOR(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('crColor', COLORREF),
    ]


EMRSETBKCOLOR = tagEMRSETTEXTCOLOR
PEMRSETBKCOLOR = POINTER(tagEMRSETTEXTCOLOR)
EMRSETTEXTCOLOR = tagEMRSETTEXTCOLOR
PEMRSETTEXTCOLOR = POINTER(tagEMRSETTEXTCOLOR)


class tagEMRSELECTOBJECT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Object handle index
        ('ihObject', DWORD),
    ]


EMRSELECTOBJECT = tagEMRSELECTOBJECT
PEMRSELECTOBJECT = POINTER(tagEMRSELECTOBJECT)
EMRDELETEOBJECT = tagEMRSELECTOBJECT
PEMRDELETEOBJECT = POINTER(tagEMRSELECTOBJECT)


class tagEMRSELECTPALETTE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Palette handle index, background mode only
        ('ihPal', DWORD),
    ]


EMRSELECTPALETTE = tagEMRSELECTPALETTE
PEMRSELECTPALETTE = POINTER(tagEMRSELECTPALETTE)


class tagEMRRESIZEPALETTE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Palette handle index
        ('ihPal', DWORD),
        ('cEntries', DWORD),
    ]


EMRRESIZEPALETTE = tagEMRRESIZEPALETTE
PEMRRESIZEPALETTE = POINTER(tagEMRRESIZEPALETTE)


# noinspection PyTypeChecker
class tagEMRSETPALETTEENTRIES(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Palette handle index
        ('ihPal', DWORD),
        ('iStart', DWORD),
        ('cEntries', DWORD),
        # The peFlags fields do not contain any flags
        ('aPalEntries', PALETTEENTRY * 1),
    ]


EMRSETPALETTEENTRIES = tagEMRSETPALETTEENTRIES
PEMRSETPALETTEENTRIES = POINTER(tagEMRSETPALETTEENTRIES)


class tagEMRSETCOLORADJUSTMENT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('ColorAdjustment', COLORADJUSTMENT),
    ]


EMRSETCOLORADJUSTMENT = tagEMRSETCOLORADJUSTMENT
PEMRSETCOLORADJUSTMENT = POINTER(tagEMRSETCOLORADJUSTMENT)


# noinspection PyTypeChecker
class tagEMRGDICOMMENT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Size of data in bytes
        ('cbData', DWORD),
        ('Data', BYTE * 1),
    ]


EMRGDICOMMENT = tagEMRGDICOMMENT
PEMRGDICOMMENT = POINTER(tagEMRGDICOMMENT)


class tagEMREOF(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Number of palette entries
        ('nPalEntries', DWORD),
        # Offset to the palette entries
        ('offPalEntries', DWORD),
        # Same as nSize and must be the last DWORD
        ('nSizeLast', DWORD),
        # of the record.  The palette entries,
        # if exist, precede this field.
    ]


EMREOF = tagEMREOF
PEMREOF = POINTER(tagEMREOF)


class tagEMRLINETO(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('ptl', POINTL),
    ]


EMRLINETO = tagEMRLINETO
PEMRLINETO = POINTER(tagEMRLINETO)
EMRMOVETOEX = tagEMRLINETO
PEMRMOVETOEX = POINTER(tagEMRLINETO)


class tagEMROFFSETCLIPRGN(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('ptlOffset', POINTL),
    ]


EMROFFSETCLIPRGN = tagEMROFFSETCLIPRGN
PEMROFFSETCLIPRGN = POINTER(tagEMROFFSETCLIPRGN)


class tagEMRFILLPATH(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
    ]


EMRFILLPATH = tagEMRFILLPATH
PEMRFILLPATH = POINTER(tagEMRFILLPATH)
EMRSTROKEANDFILLPATH = tagEMRFILLPATH
PEMRSTROKEANDFILLPATH = POINTER(tagEMRFILLPATH)
EMRSTROKEPATH = tagEMRFILLPATH
PEMRSTROKEPATH = POINTER(tagEMRFILLPATH)


class tagEMREXCLUDECLIPRECT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('rclClip', RECTL),
    ]


EMREXCLUDECLIPRECT = tagEMREXCLUDECLIPRECT
PEMREXCLUDECLIPRECT = POINTER(tagEMREXCLUDECLIPRECT)
EMRINTERSECTCLIPRECT = tagEMREXCLUDECLIPRECT
PEMRINTERSECTCLIPRECT = POINTER(tagEMREXCLUDECLIPRECT)


class tagEMRSETVIEWPORTORGEX(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('ptlOrigin', POINTL),
    ]


EMRSETVIEWPORTORGEX = tagEMRSETVIEWPORTORGEX
PEMRSETVIEWPORTORGEX = POINTER(tagEMRSETVIEWPORTORGEX)
EMRSETWINDOWORGEX = tagEMRSETVIEWPORTORGEX
PEMRSETWINDOWORGEX = POINTER(tagEMRSETVIEWPORTORGEX)
EMRSETBRUSHORGEX = tagEMRSETVIEWPORTORGEX
PEMRSETBRUSHORGEX = POINTER(tagEMRSETVIEWPORTORGEX)


class tagEMRSETVIEWPORTEXTEX(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('szlExtent', SIZEL),
    ]


EMRSETVIEWPORTEXTEX = tagEMRSETVIEWPORTEXTEX
PEMRSETVIEWPORTEXTEX = POINTER(tagEMRSETVIEWPORTEXTEX)
EMRSETWINDOWEXTEX = tagEMRSETVIEWPORTEXTEX
PEMRSETWINDOWEXTEX = POINTER(tagEMRSETVIEWPORTEXTEX)


class tagEMRSCALEVIEWPORTEXTEX(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('xNum', LONG),
        ('xDenom', LONG),
        ('yNum', LONG),
        ('yDenom', LONG),
    ]


EMRSCALEVIEWPORTEXTEX = tagEMRSCALEVIEWPORTEXTEX
PEMRSCALEVIEWPORTEXTEX = POINTER(tagEMRSCALEVIEWPORTEXTEX)
EMRSCALEWINDOWEXTEX = tagEMRSCALEVIEWPORTEXTEX
PEMRSCALEWINDOWEXTEX = POINTER(tagEMRSCALEVIEWPORTEXTEX)


class tagEMRSETWORLDTRANSFORM(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('xform', XFORM),
    ]


EMRSETWORLDTRANSFORM = tagEMRSETWORLDTRANSFORM
PEMRSETWORLDTRANSFORM = POINTER(tagEMRSETWORLDTRANSFORM)


class tagEMRMODIFYWORLDTRANSFORM(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('xform', XFORM),
        ('iMode', DWORD),
    ]


EMRMODIFYWORLDTRANSFORM = tagEMRMODIFYWORLDTRANSFORM
PEMRMODIFYWORLDTRANSFORM = POINTER(tagEMRMODIFYWORLDTRANSFORM)


class tagEMRSETPIXELV(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('ptlPixel', POINTL),
        ('crColor', COLORREF),
    ]


EMRSETPIXELV = tagEMRSETPIXELV
PEMRSETPIXELV = POINTER(tagEMRSETPIXELV)


class tagEMREXTFLOODFILL(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('ptlStart', POINTL),
        ('crColor', COLORREF),
        ('iMode', DWORD),
    ]


EMREXTFLOODFILL = tagEMREXTFLOODFILL
PEMREXTFLOODFILL = POINTER(tagEMREXTFLOODFILL)


class tagEMRELLIPSE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounding rectangle
        ('rclBox', RECTL),
    ]


EMRELLIPSE = tagEMRELLIPSE
PEMRELLIPSE = POINTER(tagEMRELLIPSE)
EMRRECTANGLE = tagEMRELLIPSE
PEMRRECTANGLE = POINTER(tagEMRELLIPSE)


class tagEMRROUNDRECT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounding rectangle
        ('rclBox', RECTL),
        ('szlCorner', SIZEL),
    ]


EMRROUNDRECT = tagEMRROUNDRECT
PEMRROUNDRECT = POINTER(tagEMRROUNDRECT)


class tagEMRARC(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounding rectangle
        ('rclBox', RECTL),
        ('ptlStart', POINTL),
        ('ptlEnd', POINTL),
    ]


EMRARC = tagEMRARC
PEMRARC = POINTER(tagEMRARC)
EMRARCTO = tagEMRARC
PEMRARCTO = POINTER(tagEMRARC)
EMRCHORD = tagEMRARC
PEMRCHORD = POINTER(tagEMRARC)
EMRPIE = tagEMRARC
PEMRPIE = POINTER(tagEMRARC)


class tagEMRANGLEARC(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('ptlCenter', POINTL),
        ('nRadius', DWORD),
        ('eStartAngle', FLOAT),
        ('eSweepAngle', FLOAT),
    ]


EMRANGLEARC = tagEMRANGLEARC
PEMRANGLEARC = POINTER(tagEMRANGLEARC)


# noinspection PyTypeChecker
class tagEMRPOLYLINE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('cptl', DWORD),
        ('aptl', POINTL * 1),
    ]


EMRPOLYLINE = tagEMRPOLYLINE
PEMRPOLYLINE = POINTER(tagEMRPOLYLINE)
EMRPOLYBEZIER = tagEMRPOLYLINE
PEMRPOLYBEZIER = POINTER(tagEMRPOLYLINE)
EMRPOLYGON = tagEMRPOLYLINE
PEMRPOLYGON = POINTER(tagEMRPOLYLINE)
EMRPOLYBEZIERTO = tagEMRPOLYLINE
PEMRPOLYBEZIERTO = POINTER(tagEMRPOLYLINE)
EMRPOLYLINETO = tagEMRPOLYLINE
PEMRPOLYLINETO = POINTER(tagEMRPOLYLINE)


# noinspection PyTypeChecker
class tagEMRPOLYLINE16(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('cpts', DWORD),
        ('apts', POINTS * 1),
    ]


EMRPOLYLINE16 = tagEMRPOLYLINE16
PEMRPOLYLINE16 = POINTER(tagEMRPOLYLINE16)
EMRPOLYBEZIER16 = tagEMRPOLYLINE16
PEMRPOLYBEZIER16 = POINTER(tagEMRPOLYLINE16)
EMRPOLYGON16 = tagEMRPOLYLINE16
PEMRPOLYGON16 = POINTER(tagEMRPOLYLINE16)
EMRPOLYBEZIERTO16 = tagEMRPOLYLINE16
PEMRPOLYBEZIERTO16 = POINTER(tagEMRPOLYLINE16)
EMRPOLYLINETO16 = tagEMRPOLYLINE16
PEMRPOLYLINETO16 = POINTER(tagEMRPOLYLINE16)


# noinspection PyTypeChecker
class tagEMRPOLYDRAW(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Number of points
        ('cptl', DWORD),
        # Array of points
        ('aptl', POINTL * 1),
        # Array of point types
        ('abTypes', BYTE * 1),
    ]


EMRPOLYDRAW = tagEMRPOLYDRAW
PEMRPOLYDRAW = POINTER(tagEMRPOLYDRAW)


# noinspection PyTypeChecker
class tagEMRPOLYDRAW16(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Number of points
        ('cpts', DWORD),
        # Array of points
        ('apts', POINTS * 1),
        # Array of point types
        ('abTypes', BYTE * 1),
    ]


EMRPOLYDRAW16 = tagEMRPOLYDRAW16
PEMRPOLYDRAW16 = POINTER(tagEMRPOLYDRAW16)


# noinspection PyTypeChecker
class tagEMRPOLYPOLYLINE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Number of polys
        ('nPolys', DWORD),
        # Total number of points in all polys
        ('cptl', DWORD),
        # Array of point counts for each poly
        ('aPolyCounts', DWORD * 1),
        # Array of points
        ('aptl', POINTL * 1),
    ]


EMRPOLYPOLYLINE = tagEMRPOLYPOLYLINE
PEMRPOLYPOLYLINE = POINTER(tagEMRPOLYPOLYLINE)
EMRPOLYPOLYGON = tagEMRPOLYPOLYLINE
PEMRPOLYPOLYGON = POINTER(tagEMRPOLYPOLYLINE)


# noinspection PyTypeChecker
class tagEMRPOLYPOLYLINE16(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Number of polys
        ('nPolys', DWORD),
        # Total number of points in all polys
        ('cpts', DWORD),
        # Array of point counts for each poly
        ('aPolyCounts', DWORD * 1),
        # Array of points
        ('apts', POINTS * 1),
    ]


EMRPOLYPOLYLINE16 = tagEMRPOLYPOLYLINE16
PEMRPOLYPOLYLINE16 = POINTER(tagEMRPOLYPOLYLINE16)
EMRPOLYPOLYGON16 = tagEMRPOLYPOLYLINE16
PEMRPOLYPOLYGON16 = POINTER(tagEMRPOLYPOLYLINE16)


# noinspection PyTypeChecker
class tagEMRINVERTRGN(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Size of region data in bytes
        ('cbRgnData', DWORD),
        ('RgnData', BYTE * 1),
    ]


EMRINVERTRGN = tagEMRINVERTRGN
PEMRINVERTRGN = POINTER(tagEMRINVERTRGN)
EMRPAINTRGN = tagEMRINVERTRGN
PEMRPAINTRGN = POINTER(tagEMRINVERTRGN)


# noinspection PyTypeChecker
class tagEMRFILLRGN(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Size of region data in bytes
        ('cbRgnData', DWORD),
        # Brush handle index
        ('ihBrush', DWORD),
        ('RgnData', BYTE * 1),
    ]


EMRFILLRGN = tagEMRFILLRGN
PEMRFILLRGN = POINTER(tagEMRFILLRGN)


# noinspection PyTypeChecker
class tagEMRFRAMERGN(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Size of region data in bytes
        ('cbRgnData', DWORD),
        # Brush handle index
        ('ihBrush', DWORD),
        ('szlStroke', SIZEL),
        ('RgnData', BYTE * 1),
    ]


EMRFRAMERGN = tagEMRFRAMERGN
PEMRFRAMERGN = POINTER(tagEMRFRAMERGN)


# noinspection PyTypeChecker
class tagEMREXTSELECTCLIPRGN(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Size of region data in bytes
        ('cbRgnData', DWORD),
        ('iMode', DWORD),
        ('RgnData', BYTE * 1),
    ]


EMREXTSELECTCLIPRGN = tagEMREXTSELECTCLIPRGN
PEMREXTSELECTCLIPRGN = POINTER(tagEMREXTSELECTCLIPRGN)


class tagEMREXTTEXTOUTA(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Current graphics mode
        ('iGraphicsMode', DWORD),
        # X and Y scales from Page units to .01mm units
        ('exScale', FLOAT),
        # if graphics mode is GM_COMPATIBLE.
        ('eyScale', FLOAT),
        # This is followed by the string and spacing
        ('emrtext', EMRTEXT),
        # array
    ]


EMREXTTEXTOUTA = tagEMREXTTEXTOUTA
PEMREXTTEXTOUTA = POINTER(tagEMREXTTEXTOUTA)
EMREXTTEXTOUTW = tagEMREXTTEXTOUTA
PEMREXTTEXTOUTW = POINTER(tagEMREXTTEXTOUTA)


# noinspection PyTypeChecker
class tagEMRPOLYTEXTOUTA(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        # Current graphics mode
        ('iGraphicsMode', DWORD),
        # X and Y scales from Page units to .01mm units
        ('exScale', FLOAT),
        # if graphics mode is GM_COMPATIBLE.
        ('eyScale', FLOAT),
        ('cStrings', LONG),
        # Array of EMRTEXT structures.  This is
        ('aemrtext', EMRTEXT * 1),
        # followed by the strings and spacing arrays.
    ]


EMRPOLYTEXTOUTA = tagEMRPOLYTEXTOUTA
PEMRPOLYTEXTOUTA = POINTER(tagEMRPOLYTEXTOUTA)
EMRPOLYTEXTOUTW = tagEMRPOLYTEXTOUTA
PEMRPOLYTEXTOUTW = POINTER(tagEMRPOLYTEXTOUTA)


class tagEMRBITBLT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('xDest', LONG),
        ('yDest', LONG),
        ('cxDest', LONG),
        ('cyDest', LONG),
        ('dwRop', DWORD),
        ('xSrc', LONG),
        ('ySrc', LONG),
        # Source DC transform
        ('xformSrc', XFORM),
        # Source DC BkColor in RGB
        ('crBkColorSrc', COLORREF),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        # (DIB_RGB_COLORS)
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
    ]


EMRBITBLT = tagEMRBITBLT
PEMRBITBLT = POINTER(tagEMRBITBLT)


class tagEMRSTRETCHBLT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('xDest', LONG),
        ('yDest', LONG),
        ('cxDest', LONG),
        ('cyDest', LONG),
        ('dwRop', DWORD),
        ('xSrc', LONG),
        ('ySrc', LONG),
        # Source DC transform
        ('xformSrc', XFORM),
        # Source DC BkColor in RGB
        ('crBkColorSrc', COLORREF),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        # (DIB_RGB_COLORS)
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
        ('cxSrc', LONG),
        ('cySrc', LONG),
    ]


EMRSTRETCHBLT = tagEMRSTRETCHBLT
PEMRSTRETCHBLT = POINTER(tagEMRSTRETCHBLT)


class tagEMRMASKBLT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('xDest', LONG),
        ('yDest', LONG),
        ('cxDest', LONG),
        ('cyDest', LONG),
        ('dwRop', DWORD),
        ('xSrc', LONG),
        ('ySrc', LONG),
        # Source DC transform
        ('xformSrc', XFORM),
        # Source DC BkColor in RGB
        ('crBkColorSrc', COLORREF),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        # (DIB_RGB_COLORS)
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
        ('xMask', LONG),
        ('yMask', LONG),
        # Mask bitmap info color table usage
        ('iUsageMask', DWORD),
        # Offset to the mask BITMAPINFO structure if any
        ('offBmiMask', DWORD),
        # Size of the mask BITMAPINFO structure if any
        ('cbBmiMask', DWORD),
        # Offset to the mask bitmap bits if any
        ('offBitsMask', DWORD),
        # Size of the mask bitmap bits if any
        ('cbBitsMask', DWORD),
    ]


EMRMASKBLT = tagEMRMASKBLT
PEMRMASKBLT = POINTER(tagEMRMASKBLT)


# noinspection PyTypeChecker
class tagEMRPLGBLT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('aptlDest', POINTL * 3),
        ('xSrc', LONG),
        ('ySrc', LONG),
        ('cxSrc', LONG),
        ('cySrc', LONG),
        # Source DC transform
        ('xformSrc', XFORM),
        # Source DC BkColor in RGB
        ('crBkColorSrc', COLORREF),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        # (DIB_RGB_COLORS)
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
        ('xMask', LONG),
        ('yMask', LONG),
        # Mask bitmap info color table usage
        ('iUsageMask', DWORD),
        # Offset to the mask BITMAPINFO structure if any
        ('offBmiMask', DWORD),
        # Size of the mask BITMAPINFO structure if any
        ('cbBmiMask', DWORD),
        # Offset to the mask bitmap bits if any
        ('offBitsMask', DWORD),
        # Size of the mask bitmap bits if any
        ('cbBitsMask', DWORD),
    ]


EMRPLGBLT = tagEMRPLGBLT
PEMRPLGBLT = POINTER(tagEMRPLGBLT)


class tagEMRSETDIBITSTODEVICE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('xDest', LONG),
        ('yDest', LONG),
        ('xSrc', LONG),
        ('ySrc', LONG),
        ('cxSrc', LONG),
        ('cySrc', LONG),
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        ('iStartScan', DWORD),
        ('cScans', DWORD),
    ]


EMRSETDIBITSTODEVICE = tagEMRSETDIBITSTODEVICE
PEMRSETDIBITSTODEVICE = POINTER(tagEMRSETDIBITSTODEVICE)


class tagEMRSTRETCHDIBITS(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('xDest', LONG),
        ('yDest', LONG),
        ('xSrc', LONG),
        ('ySrc', LONG),
        ('cxSrc', LONG),
        ('cySrc', LONG),
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        ('dwRop', DWORD),
        ('cxDest', LONG),
        ('cyDest', LONG),
    ]


EMRSTRETCHDIBITS = tagEMRSTRETCHDIBITS
PEMRSTRETCHDIBITS = POINTER(tagEMRSTRETCHDIBITS)


class tagEMREXTCREATEFONTINDIRECTW(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Font handle index
        ('ihFont', DWORD),
        ('elfw', EXTLOGFONTW),
    ]


EMREXTCREATEFONTINDIRECTW = tagEMREXTCREATEFONTINDIRECTW
PEMREXTCREATEFONTINDIRECTW = POINTER(tagEMREXTCREATEFONTINDIRECTW)


class tagEMRCREATEPALETTE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Palette handle index
        ('ihPal', DWORD),
        # The peFlags fields in the palette entries
        ('lgpl', LOGPALETTE),
        # do not contain any flags
    ]


EMRCREATEPALETTE = tagEMRCREATEPALETTE
PEMRCREATEPALETTE = POINTER(tagEMRCREATEPALETTE)


class tagEMRCREATEPEN(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Pen handle index
        ('ihPen', DWORD),
        ('lopn', LOGPEN),
    ]


EMRCREATEPEN = tagEMRCREATEPEN
PEMRCREATEPEN = POINTER(tagEMRCREATEPEN)


class tagEMREXTCREATEPEN(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Pen handle index
        ('ihPen', DWORD),
        # Offset to the BITMAPINFO structure if any
        ('offBmi', DWORD),
        # Size of the BITMAPINFO structure if any
        ('cbBmi', DWORD),
        # The bitmap info is followed by the bitmap
        # bits to form a packed DIB.
        # Offset to the brush bitmap bits if any
        ('offBits', DWORD),
        # Size of the brush bitmap bits if any
        ('cbBits', DWORD),
        # The extended pen with the style array.
        ('elp', EXTLOGPEN),
    ]


EMREXTCREATEPEN = tagEMREXTCREATEPEN
PEMREXTCREATEPEN = POINTER(tagEMREXTCREATEPEN)


class tagEMRCREATEBRUSHINDIRECT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Brush handle index
        ('ihBrush', DWORD),
        # The style must be BS_SOLID, BS_HOLLOW,
        ('lb', LOGBRUSH32),
        # BS_NULL or BS_HATCHED.
    ]


EMRCREATEBRUSHINDIRECT = tagEMRCREATEBRUSHINDIRECT
PEMRCREATEBRUSHINDIRECT = POINTER(tagEMRCREATEBRUSHINDIRECT)


class tagEMRCREATEMONOBRUSH(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Brush handle index
        ('ihBrush', DWORD),
        # Bitmap info color table usage
        ('iUsage', DWORD),
        # Offset to the BITMAPINFO structure
        ('offBmi', DWORD),
        # Size of the BITMAPINFO structure
        ('cbBmi', DWORD),
        # Offset to the bitmap bits
        ('offBits', DWORD),
        # Size of the bitmap bits
        ('cbBits', DWORD),
    ]


EMRCREATEMONOBRUSH = tagEMRCREATEMONOBRUSH
PEMRCREATEMONOBRUSH = POINTER(tagEMRCREATEMONOBRUSH)


class tagEMRCREATEDIBPATTERNBRUSHPT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Brush handle index
        ('ihBrush', DWORD),
        # Bitmap info color table usage
        ('iUsage', DWORD),
        # Offset to the BITMAPINFO structure
        ('offBmi', DWORD),
        # Size of the BITMAPINFO structure
        ('cbBmi', DWORD),
        # The bitmap info is followed by the bitmap
        # bits to form a packed DIB.
        # Offset to the bitmap bits
        ('offBits', DWORD),
        # Size of the bitmap bits
        ('cbBits', DWORD),
    ]


EMRCREATEDIBPATTERNBRUSHPT = tagEMRCREATEDIBPATTERNBRUSHPT
PEMRCREATEDIBPATTERNBRUSHPT = POINTER(tagEMRCREATEDIBPATTERNBRUSHPT)


class tagEMRFORMAT(ctypes.Structure):
    _fields_ = [
        # Format signature, e.g. ENHMETA_SIGNATURE.
        ('dSignature', DWORD),
        # Format version number.
        ('nVersion', DWORD),
        # Size of data in bytes.
        ('cbData', DWORD),
        # Offset to data from GDICOMMENT_IDENTIFIER.
        ('offData', DWORD),
        # It must begin at a DWORD offset.
    ]


EMRFORMAT = tagEMRFORMAT
PEMRFORMAT = POINTER(tagEMRFORMAT)


# noinspection PyTypeChecker
class tagEMRGLSRECORD(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Size of data in bytes
        ('cbData', DWORD),
        ('Data', BYTE * 1),
    ]


EMRGLSRECORD = tagEMRGLSRECORD
PEMRGLSRECORD = POINTER(tagEMRGLSRECORD)


# noinspection PyTypeChecker
class tagEMRGLSBOUNDEDRECORD(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Bounds in recording coordinates
        ('rclBounds', RECTL),
        # Size of data in bytes
        ('cbData', DWORD),
        ('Data', BYTE * 1),
    ]


EMRGLSBOUNDEDRECORD = tagEMRGLSBOUNDEDRECORD
PEMRGLSBOUNDEDRECORD = POINTER(tagEMRGLSBOUNDEDRECORD)


class tagEMRPIXELFORMAT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        ('pfd', PIXELFORMATDESCRIPTOR),
    ]


EMRPIXELFORMAT = tagEMRPIXELFORMAT
PEMRPIXELFORMAT = POINTER(tagEMRPIXELFORMAT)


class tagEMRCREATECOLORSPACE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # ColorSpace handle index
        ('ihCS', DWORD),
        # Ansi version of LOGCOLORSPACE
        ('lcs', LOGCOLORSPACEA),
    ]


EMRCREATECOLORSPACE = tagEMRCREATECOLORSPACE
PEMRCREATECOLORSPACE = POINTER(tagEMRCREATECOLORSPACE)


class tagEMRSETCOLORSPACE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # ColorSpace handle index
        ('ihCS', DWORD),
    ]


EMRSETCOLORSPACE = tagEMRSETCOLORSPACE
PEMRSETCOLORSPACE = POINTER(tagEMRSETCOLORSPACE)
EMRSELECTCOLORSPACE = tagEMRSETCOLORSPACE
PEMRSELECTCOLORSPACE = POINTER(tagEMRSETCOLORSPACE)
EMRDELETECOLORSPACE = tagEMRSETCOLORSPACE
PEMRDELETECOLORSPACE = POINTER(tagEMRSETCOLORSPACE)


# noinspection PyTypeChecker
class tagEMREXTESCAPE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Escape code
        ('iEscape', INT),
        # Size of escape data
        ('cbEscData', INT),
        # Escape data
        ('EscData', BYTE * 1),
    ]


EMREXTESCAPE = tagEMREXTESCAPE
PEMREXTESCAPE = POINTER(tagEMREXTESCAPE)
EMRDRAWESCAPE = tagEMREXTESCAPE
PEMRDRAWESCAPE = POINTER(tagEMREXTESCAPE)


# noinspection PyTypeChecker
class tagEMRNAMEDESCAPE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Escape code
        ('iEscape', INT),
        # Size of driver name
        ('cbDriver', INT),
        # Size of escape data
        ('cbEscData', INT),
        # Driver name and Escape data
        ('EscData', BYTE * 1),
    ]


EMRNAMEDESCAPE = tagEMRNAMEDESCAPE
PEMRNAMEDESCAPE = POINTER(tagEMRNAMEDESCAPE)


SETICMPROFILE_EMBEDED = 0x00000001


# noinspection PyTypeChecker
class tagEMRSETICMPROFILE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # flags
        ('dwFlags', DWORD),
        # Size of desired profile name
        ('cbName', DWORD),
        # Size of raw profile data if attached
        ('cbData', DWORD),
        # Array size is cbName + cbData
        ('Data', BYTE * 1),
    ]


EMRSETICMPROFILE = tagEMRSETICMPROFILE
PEMRSETICMPROFILE = POINTER(tagEMRSETICMPROFILE)
EMRSETICMPROFILEA = tagEMRSETICMPROFILE
PEMRSETICMPROFILEA = POINTER(tagEMRSETICMPROFILE)
EMRSETICMPROFILEW = tagEMRSETICMPROFILE
PEMRSETICMPROFILEW = POINTER(tagEMRSETICMPROFILE)


CREATECOLORSPACE_EMBEDED = 0x00000001


# noinspection PyTypeChecker
class tagEMRCREATECOLORSPACEW(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # ColorSpace handle index
        ('ihCS', DWORD),
        # Unicode version of logical color space structure
        ('lcs', LOGCOLORSPACEW),
        # flags
        ('dwFlags', DWORD),
        # size of raw source profile data if attached
        ('cbData', DWORD),
        # Array size is cbData
        ('Data', BYTE * 1),
    ]


EMRCREATECOLORSPACEW = tagEMRCREATECOLORSPACEW
PEMRCREATECOLORSPACEW = POINTER(tagEMRCREATECOLORSPACEW)


COLORMATCHTOTARGET_EMBEDED = 0x00000001


# noinspection PyTypeChecker
class tagCOLORMATCHTOTARGET(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # CS_ENABLE, CS_DISABLE or CS_DELETE_TRANSFORM
        ('dwAction', DWORD),
        # flags
        ('dwFlags', DWORD),
        # Size of desired target profile name
        ('cbName', DWORD),
        # Size of raw target profile data if attached
        ('cbData', DWORD),
        # Array size is cbName + cbData
        ('Data', BYTE * 1),
    ]


EMRCOLORMATCHTOTARGET = tagCOLORMATCHTOTARGET
PEMRCOLORMATCHTOTARGET = POINTER(tagCOLORMATCHTOTARGET)


class tagCOLORCORRECTPALETTE(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Palette handle index
        ('ihPalette', DWORD),
        # Index of first entry to correct
        ('nFirstEntry', DWORD),
        # Number of palette entries to correct
        ('nPalEntries', DWORD),
        # Reserved
        ('nReserved', DWORD),
    ]


EMRCOLORCORRECTPALETTE = tagCOLORCORRECTPALETTE
PEMRCOLORCORRECTPALETTE = POINTER(tagCOLORCORRECTPALETTE)


class tagEMRALPHABLEND(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('xDest', LONG),
        ('yDest', LONG),
        ('cxDest', LONG),
        ('cyDest', LONG),
        ('dwRop', DWORD),
        ('xSrc', LONG),
        ('ySrc', LONG),
        # Source DC transform
        ('xformSrc', XFORM),
        # Source DC BkColor in RGB
        ('crBkColorSrc', COLORREF),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        # (DIB_RGB_COLORS)
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
        ('cxSrc', LONG),
        ('cySrc', LONG),
    ]


EMRALPHABLEND = tagEMRALPHABLEND
PEMRALPHABLEND = POINTER(tagEMRALPHABLEND)


# noinspection PyTypeChecker
class tagEMRGRADIENTFILL(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('nVer', DWORD),
        ('nTri', DWORD),
        ('ulMode', ULONG),
        ('Ver', TRIVERTEX * 1),
    ]


EMRGRADIENTFILL = tagEMRGRADIENTFILL
PEMRGRADIENTFILL = POINTER(tagEMRGRADIENTFILL)


class tagEMRTRANSPARENTBLT(ctypes.Structure):
    _fields_ = [
        ('emr', EMR),
        # Inclusive-inclusive bounds in device units
        ('rclBounds', RECTL),
        ('xDest', LONG),
        ('yDest', LONG),
        ('cxDest', LONG),
        ('cyDest', LONG),
        ('dwRop', DWORD),
        ('xSrc', LONG),
        ('ySrc', LONG),
        # Source DC transform
        ('xformSrc', XFORM),
        # Source DC BkColor in RGB
        ('crBkColorSrc', COLORREF),
        # Source bitmap info color table usage
        ('iUsageSrc', DWORD),
        # (DIB_RGB_COLORS)
        # Offset to the source BITMAPINFO structure
        ('offBmiSrc', DWORD),
        # Size of the source BITMAPINFO structure
        ('cbBmiSrc', DWORD),
        # Offset to the source bitmap bits
        ('offBitsSrc', DWORD),
        # Size of the source bitmap bits
        ('cbBitsSrc', DWORD),
        ('cxSrc', LONG),
        ('cySrc', LONG),
    ]


EMRTRANSPARENTBLT = tagEMRTRANSPARENTBLT
PEMRTRANSPARENTBLT = POINTER(tagEMRTRANSPARENTBLT)


GDICOMMENT_IDENTIFIER = 0x43494447
GDICOMMENT_WINDOWS_METAFILE = 0x80000001
GDICOMMENT_BEGINGROUP = 0x00000002
GDICOMMENT_ENDGROUP = 0x00000003
GDICOMMENT_MULTIFORMATS = 0x40000004
EPS_SIGNATURE = 0x46535045
GDICOMMENT_UNICODE_STRING = 0x00000040
GDICOMMENT_UNICODE_END = 0x00000080


class _POINTFLOAT(ctypes.Structure):
    _fields_ = [
        ('x', FLOAT),
        ('y', FLOAT),
    ]


POINTFLOAT = _POINTFLOAT
PPOINTFLOAT = POINTER(_POINTFLOAT)


class _GLYPHMETRICSFLOAT(ctypes.Structure):
    _fields_ = [
        ('gmfBlackBoxX', FLOAT),
        ('gmfBlackBoxY', FLOAT),
        ('gmfptGlyphOrigin', POINTFLOAT),
        ('gmfCellIncX', FLOAT),
        ('gmfCellIncY', FLOAT),
    ]


GLYPHMETRICSFLOAT = _GLYPHMETRICSFLOAT
PGLYPHMETRICSFLOAT = POINTER(_GLYPHMETRICSFLOAT)


WGL_FONT_LINES = 0x00000000
WGL_FONT_POLYGONS = 0x00000001


# lpd
class tagLAYERPLANEDESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('nSize', WORD),
        ('nVersion', WORD),
        ('dwFlags', DWORD),
        ('iPixelType', BYTE),
        ('cColorBits', BYTE),
        ('cRedBits', BYTE),
        ('cRedShift', BYTE),
        ('cGreenBits', BYTE),
        ('cGreenShift', BYTE),
        ('cBlueBits', BYTE),
        ('cBlueShift', BYTE),
        ('cAlphaBits', BYTE),
        ('cAlphaShift', BYTE),
        ('cAccumBits', BYTE),
        ('cAccumRedBits', BYTE),
        ('cAccumGreenBits', BYTE),
        ('cAccumBlueBits', BYTE),
        ('cAccumAlphaBits', BYTE),
        ('cDepthBits', BYTE),
        ('cStencilBits', BYTE),
        ('cAuxBuffers', BYTE),
        ('iLayerPlane', BYTE),
        ('bReserved', BYTE),
        ('crTransparent', COLORREF),
    ]


LAYERPLANEDESCRIPTOR = tagLAYERPLANEDESCRIPTOR
PLAYERPLANEDESCRIPTOR = POINTER(tagLAYERPLANEDESCRIPTOR)


LPD_DOUBLEBUFFER = 0x00000001
LPD_STEREO = 0x00000002
LPD_SUPPORT_GDI = 0x00000010
LPD_SUPPORT_OPENGL = 0x00000020
LPD_SHARE_DEPTH = 0x00000040
LPD_SHARE_STENCIL = 0x00000080
LPD_SHARE_ACCUM = 0x00000100
LPD_SWAP_EXCHANGE = 0x00000200
LPD_SWAP_COPY = 0x00000400
LPD_TRANSPARENT = 0x00001000
LPD_TYPE_RGBA = 0x00000000
LPD_TYPE_COLORINDEX = 0x00000001
WGL_SWAP_MAIN_PLANE = 0x00000001
WGL_SWAP_OVERLAY1 = 0x00000002
WGL_SWAP_OVERLAY2 = 0x00000004
WGL_SWAP_OVERLAY3 = 0x00000008
WGL_SWAP_OVERLAY4 = 0x00000010
WGL_SWAP_OVERLAY5 = 0x00000020
WGL_SWAP_OVERLAY6 = 0x00000040
WGL_SWAP_OVERLAY7 = 0x00000080
WGL_SWAP_OVERLAY8 = 0x00000100
WGL_SWAP_OVERLAY9 = 0x00000200
WGL_SWAP_OVERLAY10 = 0x00000400
WGL_SWAP_OVERLAY11 = 0x00000800
WGL_SWAP_OVERLAY12 = 0x00001000
WGL_SWAP_OVERLAY13 = 0x00002000
WGL_SWAP_OVERLAY14 = 0x00004000
WGL_SWAP_OVERLAY15 = 0x00008000
WGL_SWAP_UNDERLAY1 = 0x00010000
WGL_SWAP_UNDERLAY2 = 0x00020000
WGL_SWAP_UNDERLAY3 = 0x00040000
WGL_SWAP_UNDERLAY4 = 0x00080000
WGL_SWAP_UNDERLAY5 = 0x00100000
WGL_SWAP_UNDERLAY6 = 0x00200000
WGL_SWAP_UNDERLAY7 = 0x00400000
WGL_SWAP_UNDERLAY8 = 0x00800000
WGL_SWAP_UNDERLAY9 = 0x01000000
WGL_SWAP_UNDERLAY10 = 0x02000000
WGL_SWAP_UNDERLAY11 = 0x04000000
WGL_SWAP_UNDERLAY12 = 0x08000000
WGL_SWAP_UNDERLAY13 = 0x10000000
WGL_SWAP_UNDERLAY14 = 0x20000000
WGL_SWAP_UNDERLAY15 = 0x40000000


class _WGLSWAP(ctypes.Structure):
    _fields_ = [
        ('hdc', HDC),
        ('uiFlags', UINT),
    ]


WGLSWAP = _WGLSWAP
PWGLSWAP = POINTER(_WGLSWAP)


WGL_SWAPMULTIPLE_MAX = 0x00000010
