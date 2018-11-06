

from .wtypes_h import (
    DWORD,
    LPRECT,
    WORD,
    LONG,
    LPVOID,
    CHAR,
    LARGE_INTEGER,
    GUID,
    POINTER,
    BYTE,
    FAR,
    HRESULT,
    CALLBACK,
    HWND,
    VOID,
    HANDLE,
    LPBOOL,
    LPDWORD,
    LPPALETTEENTRY,
    REFGUID,
    HDC,
    LPLONG,
    BOOL,
    LPSIZE
)
from .winerror_h import (
    S_OK,
    S_FALSE,
    E_FAIL,
    E_NOTIMPL,
    E_OUTOFMEMORY,
    CO_E_NOTINITIALIZED,
    E_INVALIDARG
)
from .dciddi_h import LPRGNDATA
from .guiddef_h import DEFINE_GUID
from .mmreg_h import MAKEFOURCC
from .dmerror_h import MAKE_HRESULT
import ctypes
import comtypes


ddraw = ctypes.windll.Ddraw
from .winapifamily_h import * # NOQA

DIRECTDRAW_VERSION = 0x0700
from .objbase_h import * # NOQA


_FACDD = 0x876


def MAKE_DDHRESULT(code):
    return MAKE_HRESULT(1, _FACDD, code)


FOURCC_DXT1 = MAKEFOURCC('D', 'X', 'T', '1')
FOURCC_DXT2 = MAKEFOURCC('D', 'X', 'T', '2')
FOURCC_DXT3 = MAKEFOURCC('D', 'X', 'T', '3')
FOURCC_DXT4 = MAKEFOURCC('D', 'X', 'T', '4')
FOURCC_DXT5 = MAKEFOURCC('D', 'X', 'T', '5')

CLSID_DirectDraw = DEFINE_GUID(
    0xD7B70EE0,
    0x4340,
    0x11CF,
    0xB0,
    0x63,
    0x00,
    0x20,
    0xAF,
    0xC2,
    0xCD,
    0x35
)
CLSID_DirectDraw7 = DEFINE_GUID(
    0x3C305196,
    0x50DB,
    0x11D3,
    0x9C,
    0xFE,
    0x00,
    0xC0,
    0x4F,
    0xD9,
    0x30,
    0xC5
)
CLSID_DirectDrawClipper = DEFINE_GUID(
    0x593817A0,
    0x7DB3,
    0x11CF,
    0xA2,
    0xDE,
    0x00,
    0xAA,
    0x00,
    0xB9,
    0x33,
    0x56
)
IID_IDirectDraw = DEFINE_GUID(
    0x6C14DB80,
    0xA733,
    0x11CE,
    0xA5,
    0x21,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xE5,
    0x60
)
IID_IDirectDraw2 = DEFINE_GUID(
    0xB3A6F3E0,
    0x2B43,
    0x11CF,
    0xA2,
    0xDE,
    0x00,
    0xAA,
    0x00,
    0xB9,
    0x33,
    0x56
)
IID_IDirectDraw4 = DEFINE_GUID(
    0x9C59509A,
    0x39BD,
    0x11D1,
    0x8C,
    0x4A,
    0x00,
    0xC0,
    0x4F,
    0xD9,
    0x30,
    0xC5
)
IID_IDirectDraw7 = DEFINE_GUID(
    0x15E65EC0,
    0x3B9C,
    0x11D2,
    0xB9,
    0x2F,
    0x00,
    0x60,
    0x97,
    0x97,
    0xEA,
    0x5B
)
IID_IDirectDrawSurface = DEFINE_GUID(
    0x6C14DB81,
    0xA733,
    0x11CE,
    0xA5,
    0x21,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xE5,
    0x60
)
IID_IDirectDrawSurface2 = DEFINE_GUID(
    0x57805885,
    0x6EEC,
    0x11CF,
    0x94,
    0x41,
    0xA8,
    0x23,
    0x03,
    0xC1,
    0x0E,
    0x27
)
IID_IDirectDrawSurface3 = DEFINE_GUID(
    0xDA044E00,
    0x69B2,
    0x11D0,
    0xA1,
    0xD5,
    0x00,
    0xAA,
    0x00,
    0xB8,
    0xDF,
    0xBB
)
IID_IDirectDrawSurface4 = DEFINE_GUID(
    0x0B2B8630,
    0xAD35,
    0x11D0,
    0x8E,
    0xA6,
    0x00,
    0x60,
    0x97,
    0x97,
    0xEA,
    0x5B
)
IID_IDirectDrawSurface7 = DEFINE_GUID(
    0x06675A80,
    0x3B9B,
    0x11D2,
    0xB9,
    0x2F,
    0x00,
    0x60,
    0x97,
    0x97,
    0xEA,
    0x5B
)
IID_IDirectDrawPalette = DEFINE_GUID(
    0x6C14DB84,
    0xA733,
    0x11CE,
    0xA5,
    0x21,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xE5,
    0x60
)
IID_IDirectDrawClipper = DEFINE_GUID(
    0x6C14DB85,
    0xA733,
    0x11CE,
    0xA5,
    0x21,
    0x00,
    0x20,
    0xAF,
    0x0B,
    0xE5,
    0x60
)
IID_IDirectDrawColorControl = DEFINE_GUID(
    0x4B9F0EE0,
    0x0D7E,
    0x11D0,
    0x9B,
    0x06,
    0x00,
    0xA0,
    0xC9,
    0x03,
    0xA3,
    0xB8
)
IID_IDirectDrawGammaControl = DEFINE_GUID(
    0x69C11C3E,
    0xB46B,
    0x11D1,
    0xAD,
    0x7A,
    0x00,
    0xC0,
    0x4F,
    0xC2,
    0x9B,
    0x4E
)

STDMETHOD = comtypes.STDMETHOD


class IDirectDraw(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDraw
    _idlflags_ = []


LPDIRECTDRAW = POINTER(IDirectDraw)


class IDirectDraw2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDraw2
    _idlflags_ = []


LPDIRECTDRAW2 = POINTER(IDirectDraw2)


class IDirectDraw4(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDraw4
    _idlflags_ = []


LPDIRECTDRAW4 = POINTER(IDirectDraw4)


class IDirectDraw7(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDraw7
    _idlflags_ = []


LPDIRECTDRAW7 = POINTER(IDirectDraw7)


class IDirectDrawSurface(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawSurface
    _idlflags_ = []



LPDIRECTDRAWSURFACE = POINTER(IDirectDrawSurface)


class IDirectDrawSurface2(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawSurface2
    _idlflags_ = []


LPDIRECTDRAWSURFACE2 = POINTER(IDirectDrawSurface2)


class IDirectDrawSurface3(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawSurface3
    _idlflags_ = []


LPDIRECTDRAWSURFACE3 = POINTER(IDirectDrawSurface3)


class IDirectDrawSurface4(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawSurface4
    _idlflags_ = []


LPDIRECTDRAWSURFACE4 = POINTER(IDirectDrawSurface4)


class IDirectDrawSurface7(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawSurface7
    _idlflags_ = []


LPDIRECTDRAWSURFACE7 = POINTER(IDirectDrawSurface7)


class IDirectDrawPalette(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawPalette
    _idlflags_ = []


LPDIRECTDRAWPALETTE = POINTER(IDirectDrawPalette)


class IDirectDrawClipper(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawClipper
    _idlflags_ = []


LPDIRECTDRAWCLIPPER = POINTER(IDirectDrawClipper)


class IDirectDrawColorControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawColorControl
    _idlflags_ = []


LPDIRECTDRAWCOLORCONTROL = POINTER(IDirectDrawColorControl)


class IDirectDrawGammaControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectDrawGammaControl
    _idlflags_ = []


LPDIRECTDRAWGAMMACONTROL = POINTER(IDirectDrawGammaControl)


class _DDFXROP(ctypes.Structure):
    _fields_ = []


LPDDFXROP = POINTER(_DDFXROP)


class _DDSURFACEDESC(ctypes.Structure):
    _fields_ = []


LPDDSURFACEDESC = POINTER(_DDSURFACEDESC)


class _DDSURFACEDESC2(ctypes.Structure):
    _fields_ = []


LPDDSURFACEDESC2 = POINTER(_DDSURFACEDESC2)


class _DDCOLORCONTROL(ctypes.Structure):
    _fields_ = []


LPDDCOLORCONTROL = POINTER(_DDCOLORCONTROL)


#     extern _Check_return_ HRESULT WINAPI DirectDrawEnumerateW( LPDDENUMCALLBACKW lpCallback, LPVOID lpContext );
DirectDrawEnumerateW = ddraw.DirectDrawEnumerateW
DirectDrawEnumerateW.restype = HRESULT


#     extern _Check_return_ HRESULT WINAPI DirectDrawEnumerateA( LPDDENUMCALLBACKA lpCallback, LPVOID lpContext );
DirectDrawEnumerateA = ddraw.DirectDrawEnumerateA
DirectDrawEnumerateA.restype = HRESULT


#     extern HRESULT WINAPI DirectDrawEnumerateExW( LPDDENUMCALLBACKEXW lpCallback, LPVOID lpContext, DWORD dwFlags);
DirectDrawEnumerateExW = ddraw.DirectDrawEnumerateExW
DirectDrawEnumerateExW.restype = HRESULT


#     extern HRESULT WINAPI DirectDrawEnumerateExA( LPDDENUMCALLBACKEXA lpCallback, LPVOID lpContext, DWORD dwFlags);
DirectDrawEnumerateExA = ddraw.DirectDrawEnumerateExA
DirectDrawEnumerateExA.restype = HRESULT


#     extern _Check_return_ HRESULT WINAPI DirectDrawCreate( GUID FAR *lpGUID, LPDIRECTDRAW FAR *lplpDD, IUnknown FAR *pUnkOuter );
DirectDrawCreate = ddraw.DirectDrawCreate
DirectDrawCreate.restype = HRESULT


#     extern HRESULT WINAPI DirectDrawCreateEx( GUID FAR * lpGuid, LPVOID  *lplpDD, REFIID  iid,IUnknown FAR *pUnkOuter );
DirectDrawCreateEx = ddraw.DirectDrawCreateEx
DirectDrawCreateEx.restype = HRESULT


#     extern _Check_return_ HRESULT WINAPI DirectDrawCreateClipper( DWORD dwFlags, LPDIRECTDRAWCLIPPER FAR *lplpDDClipper, IUnknown FAR *pUnkOuter );
DirectDrawCreateClipper = ddraw.DirectDrawCreateClipper
DirectDrawCreateClipper.restype = HRESULT

DDENUM_ATTACHEDSECONDARYDEVICES = 0x00000001
DDENUM_DETACHEDSECONDARYDEVICES = 0x00000002
DDENUM_NONDISPLAYDEVICES = 0x00000004
REGSTR_KEY_DDHW_DESCRIPTION = "Description"
REGSTR_KEY_DDHW_DRIVERNAME = "DriverName"
REGSTR_PATH_DDHW = "Hardware\\DirectDrawDrivers"
DDCREATE_HARDWAREONLY = 0x00000001
DDCREATE_EMULATIONONLY = 0x00000002

LPDDENUMMODESCALLBACK = CALLBACK(HRESULT, LPDDSURFACEDESC, LPVOID)
LPDDENUMMODESCALLBACK2 = CALLBACK(HRESULT, LPDDSURFACEDESC2, LPVOID)
LPDDENUMSURFACESCALLBACK = CALLBACK(HRESULT, LPDIRECTDRAWSURFACE, LPDDSURFACEDESC, LPVOID)
LPDDENUMSURFACESCALLBACK2 = CALLBACK(HRESULT, LPDIRECTDRAWSURFACE4, LPDDSURFACEDESC2, LPVOID)
LPDDENUMSURFACESCALLBACK7 = CALLBACK(HRESULT, LPDIRECTDRAWSURFACE7, LPDDSURFACEDESC2, LPVOID)

class _DDARGB(ctypes.Structure):
    _fields_ = [
        ('blue', BYTE),
        ('green', BYTE),
        ('red', BYTE),
        ('alpha', BYTE),
    ]


DDARGB = _DDARGB


LPDDARGB = POINTER(FAR)

class _DDRGBA(ctypes.Structure):
    _fields_ = [
        ('red', BYTE),
        ('green', BYTE),
        ('blue', BYTE),
        ('alpha', BYTE),
    ]


DDRGBA = _DDRGBA


LPDDRGBA = POINTER(FAR)

class _DDCOLORKEY(ctypes.Structure):
    _fields_ = [
        ('dwColorSpaceLowValue', DWORD),
        ('dwColorSpaceHighValue', DWORD),
    ]


DDCOLORKEY = _DDCOLORKEY


LPDDCOLORKEY = DDCOLORKEY

class _DDBLTFX(ctypes.Structure):

    class DUMMYUNIONNAME1(ctypes.Union):
        _fields_ = [
            ('dwZDestConst', DWORD),
            ('lpDDSZBufferDest', LPDIRECTDRAWSURFACE),
        ]

    class DUMMYUNIONNAME2(ctypes.Union):
        _fields_ = [
            ('dwZSrcConst', DWORD),
            ('lpDDSZBufferSrc', LPDIRECTDRAWSURFACE),
        ]

    class DUMMYUNIONNAME3(ctypes.Union):
        _fields_ = [
            ('dwAlphaDestConst', DWORD),
            ('lpDDSAlphaDest', LPDIRECTDRAWSURFACE),
        ]

    class DUMMYUNIONNAME4(ctypes.Union):
        _fields_ = [
            ('dwAlphaSrcConst', DWORD),
            ('lpDDSAlphaSrc', LPDIRECTDRAWSURFACE),
        ]

    class DUMMYUNIONNAME5(ctypes.Union):
        _fields_ = [
            ('dwFillColor', DWORD),
            ('dwFillDepth', DWORD),
            ('dwFillPixel', DWORD),
            ('lpDDSPattern', LPDIRECTDRAWSURFACE),
        ]

    _fields_ = [
        ('dwSize', DWORD),
        ('dwDDFX', DWORD),
        ('dwROP', DWORD),
        ('dwDDROP', DWORD),
        ('dwRotationAngle', DWORD),
        ('dwZBufferOpCode', DWORD),
        ('dwZBufferLow', DWORD),
        ('dwZBufferHigh', DWORD),
        ('dwZBufferBaseDest', DWORD),
        ('dwZDestConstBitDepth', DWORD),
        ('DUMMYUNIONNAME1', DUMMYUNIONNAME1),
        ('dwZSrcConstBitDepth', DWORD),
        ('DUMMYUNIONNAME2', DUMMYUNIONNAME2),
        ('dwAlphaEdgeBlendBitDepth', DWORD),
        ('dwAlphaEdgeBlend', DWORD),
        ('dwReserved', DWORD),
        ('dwAlphaDestConstBitDepth', DWORD),
        ('DUMMYUNIONNAME3', DUMMYUNIONNAME3),
        ('dwAlphaSrcConstBitDepth', DWORD),
        ('DUMMYUNIONNAME4', DUMMYUNIONNAME4),
        ('DUMMYUNIONNAME5', DUMMYUNIONNAME5),
        ('ddckDestColorkey', DDCOLORKEY),
        ('ddckSrcColorkey', DDCOLORKEY),
    ]


DDBLTFX = _DDBLTFX


LPDDBLTFX = DDBLTFX

class _DDSCAPS(ctypes.Structure):
    _fields_ = [
        ('dwCaps', DWORD),
    ]


DDSCAPS = _DDSCAPS


LPDDSCAPS = DDSCAPS

class _DDOSCAPS(ctypes.Structure):
    _fields_ = [
        ('dwCaps', DWORD),
    ]


DDOSCAPS = _DDOSCAPS


LPDDOSCAPS = DDOSCAPS

class _DDSCAPSEX(ctypes.Structure):

    class DUMMYUNIONNAME1(ctypes.Union):
        _fields_ = [
            ('dwCaps4', DWORD),
            ('dwVolumeDepth', DWORD),
        ]

    _fields_ = [
        ('dwCaps2', DWORD),
        ('dwCaps3', DWORD),
        ('DUMMYUNIONNAME1', DUMMYUNIONNAME1),
    ]


DDSCAPSEX = _DDSCAPSEX
LPDDSCAPSEX = POINTER(_DDSCAPSEX)



class _DDSCAPS2(ctypes.Structure):

    class DUMMYUNIONNAME1(ctypes.Union):
        _fields_ = [
            ('dwCaps4', DWORD),
            ('dwVolumeDepth', DWORD),
        ]

    _fields_ = [
        ('dwCaps', DWORD),
        ('dwCaps2', DWORD),
        ('dwCaps3', DWORD),
        ('DUMMYUNIONNAME1', DUMMYUNIONNAME1),
    ]


DDSCAPS2 = _DDSCAPS2


LPDDSCAPS2 = DDSCAPS2
DD_ROP_SPACE = int(256 / 32)

class _DDCAPS_DX1(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwCaps', DWORD),
        ('dwCaps2', DWORD),
        ('dwCKeyCaps', DWORD),
        ('dwFXCaps', DWORD),
        ('dwFXAlphaCaps', DWORD),
        ('dwPalCaps', DWORD),
        ('dwSVCaps', DWORD),
        ('dwAlphaBltConstBitDepths', DWORD),
        ('dwAlphaBltPixelBitDepths', DWORD),
        ('dwAlphaBltSurfaceBitDepths', DWORD),
        ('dwAlphaOverlayConstBitDepths', DWORD),
        ('dwAlphaOverlayPixelBitDepths', DWORD),
        ('dwAlphaOverlaySurfaceBitDepths', DWORD),
        ('dwZBufferBitDepths', DWORD),
        ('dwVidMemTotal', DWORD),
        ('dwVidMemFree', DWORD),
        ('dwMaxVisibleOverlays', DWORD),
        ('dwCurrVisibleOverlays', DWORD),
        ('dwNumFourCCCodes', DWORD),
        ('dwAlignBoundarySrc', DWORD),
        ('dwAlignSizeSrc', DWORD),
        ('dwAlignBoundaryDest', DWORD),
        ('dwAlignSizeDest', DWORD),
        ('dwAlignStrideAlign', DWORD),
        ('dwRops', DWORD * DD_ROP_SPACE),
        ('ddsCaps', DDSCAPS),
        ('dwMinOverlayStretch', DWORD),
        ('dwMaxOverlayStretch', DWORD),
        ('dwMinLiveVideoStretch', DWORD),
        ('dwMaxLiveVideoStretch', DWORD),
        ('dwMinHwCodecStretch', DWORD),
        ('dwMaxHwCodecStretch', DWORD),
        ('dwReserved1', DWORD),
        ('dwReserved2', DWORD),
        ('dwReserved3', DWORD),
    ]


DDCAPS_DX1 = _DDCAPS_DX1


LPDDCAPS_DX1 = DDCAPS_DX1

class _DDCAPS_DX3(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwCaps', DWORD),
        ('dwCaps2', DWORD),
        ('dwCKeyCaps', DWORD),
        ('dwFXCaps', DWORD),
        ('dwFXAlphaCaps', DWORD),
        ('dwPalCaps', DWORD),
        ('dwSVCaps', DWORD),
        ('dwAlphaBltConstBitDepths', DWORD),
        ('dwAlphaBltPixelBitDepths', DWORD),
        ('dwAlphaBltSurfaceBitDepths', DWORD),
        ('dwAlphaOverlayConstBitDepths', DWORD),
        ('dwAlphaOverlayPixelBitDepths', DWORD),
        ('dwAlphaOverlaySurfaceBitDepths', DWORD),
        ('dwZBufferBitDepths', DWORD),
        ('dwVidMemTotal', DWORD),
        ('dwVidMemFree', DWORD),
        ('dwMaxVisibleOverlays', DWORD),
        ('dwCurrVisibleOverlays', DWORD),
        ('dwNumFourCCCodes', DWORD),
        ('dwAlignBoundarySrc', DWORD),
        ('dwAlignSizeSrc', DWORD),
        ('dwAlignBoundaryDest', DWORD),
        ('dwAlignSizeDest', DWORD),
        ('dwAlignStrideAlign', DWORD),
        ('dwRops', DWORD * DD_ROP_SPACE),
        ('ddsCaps', DDSCAPS),
        ('dwMinOverlayStretch', DWORD),
        ('dwMaxOverlayStretch', DWORD),
        ('dwMinLiveVideoStretch', DWORD),
        ('dwMaxLiveVideoStretch', DWORD),
        ('dwMinHwCodecStretch', DWORD),
        ('dwMaxHwCodecStretch', DWORD),
        ('dwReserved1', DWORD),
        ('dwReserved2', DWORD),
        ('dwReserved3', DWORD),
        ('dwSVBCaps', DWORD),
        ('dwSVBCKeyCaps', DWORD),
        ('dwSVBFXCaps', DWORD),
        ('dwSVBRops', DWORD * DD_ROP_SPACE),
        ('dwVSBCaps', DWORD),
        ('dwVSBCKeyCaps', DWORD),
        ('dwVSBFXCaps', DWORD),
        ('dwVSBRops', DWORD * DD_ROP_SPACE),
        ('dwSSBCaps', DWORD),
        ('dwSSBCKeyCaps', DWORD),
        ('dwSSBFXCaps', DWORD),
        ('dwSSBRops', DWORD * DD_ROP_SPACE),
        ('dwReserved4', DWORD),
        ('dwReserved5', DWORD),
        ('dwReserved6', DWORD),
    ]


DDCAPS_DX3 = _DDCAPS_DX3


LPDDCAPS_DX3 = DDCAPS_DX3

class _DDCAPS_DX5(ctypes.Structure):
    _fields_ = [

    ]


DDCAPS_DX5 = _DDCAPS_DX5


LPDDCAPS_DX5 = DDCAPS_DX5

class _DDCAPS_DX6(ctypes.Structure):
    _fields_ = [

    ]


DDCAPS_DX6 = _DDCAPS_DX6


LPDDCAPS_DX6 = DDCAPS_DX6

class _DDCAPS_DX7(ctypes.Structure):
    _fields_ = [

    ]


DDCAPS_DX7 = _DDCAPS_DX7
LPDDCAPS_DX7 = DDCAPS_DX7

DDCAPS = DDCAPS_DX7
LPDDCAPS = POINTER(DDCAPS)

class _DDPIXELFORMAT(ctypes.Structure):

    class DUMMYUNIONNAME1(ctypes.Union):
        _fields_ = [
            ('dwRGBBitCount', DWORD),
            ('dwYUVBitCount', DWORD),
            ('dwZBufferBitDepth', DWORD),
            ('dwAlphaBitDepth', DWORD),
            ('dwLuminanceBitCount', DWORD),
            ('dwBumpBitCount', DWORD),
            ('dwPrivateFormatBitCount', DWORD),
        ]

    class DUMMYUNIONNAME2(ctypes.Union):
        _fields_ = [
            ('dwRBitMask', DWORD),
            ('dwYBitMask', DWORD),
            ('dwStencilBitDepth', DWORD),
            ('dwLuminanceBitMask', DWORD),
            ('dwBumpDuBitMask', DWORD),
            ('dwOperations', DWORD),
        ]

    class DUMMYUNIONNAME3(ctypes.Union):

        class MultiSampleCaps(ctypes.Structure):
            _fields_ = [
                ('wFlipMSTypes', WORD),
                ('wBltMSTypes', WORD),
            ]

        _fields_ = [
            ('dwGBitMask', DWORD),
            ('dwUBitMask', DWORD),
            ('dwZBitMask', DWORD),
            ('dwBumpDvBitMask', DWORD),
            ('MultiSampleCaps', MultiSampleCaps),
        ]

    class DUMMYUNIONNAME4(ctypes.Union):
        _fields_ = [
            ('dwBBitMask', DWORD),
            ('dwVBitMask', DWORD),
            ('dwStencilBitMask', DWORD),
            ('dwBumpLuminanceBitMask', DWORD),
        ]

    class DUMMYUNIONNAME5(ctypes.Union):
        _fields_ = [
            ('dwRGBAlphaBitMask', DWORD),
            ('dwYUVAlphaBitMask', DWORD),
            ('dwLuminanceAlphaBitMask', DWORD),
            ('dwRGBZBitMask', DWORD),
            ('dwYUVZBitMask', DWORD),
        ]

    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('dwFourCC', DWORD),
        ('DUMMYUNIONNAME1', DUMMYUNIONNAME1),
        ('DUMMYUNIONNAME2', DUMMYUNIONNAME2),
        ('DUMMYUNIONNAME3', DUMMYUNIONNAME3),
        ('DUMMYUNIONNAME4', DUMMYUNIONNAME4),
        ('DUMMYUNIONNAME5', DUMMYUNIONNAME5),
    ]


DDPIXELFORMAT = _DDPIXELFORMAT


LPDDPIXELFORMAT = DDPIXELFORMAT

class _DDOVERLAYFX(ctypes.Structure):

    class DUMMYUNIONNAME1(ctypes.Union):
        _fields_ = [
            ('dwAlphaDestConst', DWORD),
            ('lpDDSAlphaDest', LPDIRECTDRAWSURFACE),
        ]

    class DUMMYUNIONNAME2(ctypes.Union):
        _fields_ = [
            ('dwAlphaSrcConst', DWORD),
            ('lpDDSAlphaSrc', LPDIRECTDRAWSURFACE),
        ]

    _fields_ = [
        ('dwSize', DWORD),
        ('dwAlphaEdgeBlendBitDepth', DWORD),
        ('dwAlphaEdgeBlend', DWORD),
        ('dwReserved', DWORD),
        ('dwAlphaDestConstBitDepth', DWORD),
        ('DUMMYUNIONNAME1', DUMMYUNIONNAME1),
        ('dwAlphaSrcConstBitDepth', DWORD),
        ('DUMMYUNIONNAME2', DUMMYUNIONNAME2),
        ('dckDestColorkey', DDCOLORKEY),
        ('dckSrcColorkey', DDCOLORKEY),
        ('dwDDFX', DWORD),
        ('dwFlags', DWORD),
    ]


DDOVERLAYFX = _DDOVERLAYFX


LPDDOVERLAYFX = POINTER(FAR)

class _DDBLTBATCH(ctypes.Structure):
    _fields_ = [
        ('lprDest', LPRECT),
        ('lpDDSSrc', LPDIRECTDRAWSURFACE),
        ('lprSrc', LPRECT),
        ('dwFlags', DWORD),
        ('lpDDBltFx', LPDDBLTFX),
    ]


DDBLTBATCH = _DDBLTBATCH


LPDDBLTBATCH = FAR

class _DDGAMMARAMP(ctypes.Structure):
    _fields_ = [
        ('red', WORD * 256),
        ('green', WORD * 256),
        ('blue', WORD * 256),
    ]


DDGAMMARAMP = _DDGAMMARAMP


LPDDGAMMARAMP = FAR
MAX_DDDEVICEID_STRING = 0x200

class tagDDDEVICEIDENTIFIER(ctypes.Structure):
    _fields_ = [
        ('szDriver', CHAR * MAX_DDDEVICEID_STRING),
        ('szDescription', CHAR * MAX_DDDEVICEID_STRING),
        ('liDriverVersion', LARGE_INTEGER),
        ('dwDriverVersionLowPart', DWORD),
        ('dwDriverVersionHighPart', DWORD),
        ('dwVendorId', DWORD),
        ('dwDeviceId', DWORD),
        ('dwSubSysId', DWORD),
        ('dwRevision', DWORD),
        ('guidDeviceIdentifier', GUID),
    ]


DDDEVICEIDENTIFIER = tagDDDEVICEIDENTIFIER
LPDDDEVICEIDENTIFIER = POINTER(tagDDDEVICEIDENTIFIER)



class tagDDDEVICEIDENTIFIER2(ctypes.Structure):
    _fields_ = [
        ('szDriver', CHAR * MAX_DDDEVICEID_STRING),
        ('szDescription', CHAR * MAX_DDDEVICEID_STRING),
        ('liDriverVersion', LARGE_INTEGER),
        ('dwDriverVersionLowPart', DWORD),
        ('dwDriverVersionHighPart', DWORD),
        ('dwVendorId', DWORD),
        ('dwDeviceId', DWORD),
        ('dwSubSysId', DWORD),
        ('dwRevision', DWORD),
        ('guidDeviceIdentifier', GUID),
        ('dwWHQLLevel', DWORD),
    ]


DDDEVICEIDENTIFIER2 = tagDDDEVICEIDENTIFIER2
LPDDDEVICEIDENTIFIER2 = POINTER(tagDDDEVICEIDENTIFIER2)


DDGDI_GETHOSTIDENTIFIER = 0x00000001


def GET_WHQL_YEAR(dwWHQLLevel):
    return dwWHQLLevel / 0x10000


def GET_WHQL_MONTH(dwWHQLLevel):
    return (dwWHQLLevel / 0x100) & 0x00ff


def GET_WHQL_DAY(dwWHQLLevel):
    return dwWHQLLevel & 0xff



LPCLIPPERCALLBACK = CALLBACK(DWORD, LPDIRECTDRAWCLIPPER, HWND, DWORD, LPVOID)
#ifdef STREAMING
LPSURFACESTREAMINGCALLBACK = CALLBACK(DWORD, DWORD)
#endif


def IDirectDraw_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p, a, b)


def IDirectDraw_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDraw_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDraw_Compact(p):
    return p.lpVtbl.Compact(p)


def IDirectDraw_CreateClipper(p, a, b, c):
    return p.lpVtbl.CreateClipper(p, a, b, c)


def IDirectDraw_CreatePalette(p, a, b, c, d):
    return p.lpVtbl.CreatePalette(p, a, b, c, d)


def IDirectDraw_CreateSurface(p, a, b, c):
    return p.lpVtbl.CreateSurface(p, a, b, c)


def IDirectDraw_DuplicateSurface(p, a, b):
    return p.lpVtbl.DuplicateSurface(p, a, b)


def IDirectDraw_EnumDisplayModes(p, a, b, c, d):
    return p.lpVtbl.EnumDisplayModes(p, a, b, c, d)


def IDirectDraw_EnumSurfaces(p, a, b, c, d):
    return p.lpVtbl.EnumSurfaces(p, a, b, c, d)


def IDirectDraw_FlipToGDISurface(p):
    return p.lpVtbl.FlipToGDISurface(p)


def IDirectDraw_GetCaps(p, a, b):
    return p.lpVtbl.GetCaps(p, a, b)


def IDirectDraw_GetDisplayMode(p, a):
    return p.lpVtbl.GetDisplayMode(p, a)


def IDirectDraw_GetFourCCCodes(p, a, b):
    return p.lpVtbl.GetFourCCCodes(p, a, b)


def IDirectDraw_GetGDISurface(p, a):
    return p.lpVtbl.GetGDISurface(p, a)


def IDirectDraw_GetMonitorFrequency(p, a):
    return p.lpVtbl.GetMonitorFrequency(p, a)


def IDirectDraw_GetScanLine(p, a):
    return p.lpVtbl.GetScanLine(p, a)


def IDirectDraw_GetVerticalBlankStatus(p, a):
    return p.lpVtbl.GetVerticalBlankStatus(p, a)


def IDirectDraw_Initialize(p, a):
    return p.lpVtbl.Initialize(p, a)


def IDirectDraw_RestoreDisplayMode(p):
    return p.lpVtbl.RestoreDisplayMode(p)


def IDirectDraw_SetCooperativeLevel(p, a, b):
    return p.lpVtbl.SetCooperativeLevel(p, a, b)


def IDirectDraw_SetDisplayMode(p, a, b, c):
    return p.lpVtbl.SetDisplayMode(p, a, b, c)


def IDirectDraw_WaitForVerticalBlank(p, a, b):
    return p.lpVtbl.WaitForVerticalBlank(p, a, b)


def IDirectDraw2_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p, a, b)


def IDirectDraw2_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDraw2_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDraw2_Compact(p):
    return p.lpVtbl.Compact(p)


def IDirectDraw2_CreateClipper(p, a, b, c):
    return p.lpVtbl.CreateClipper(p, a, b, c)


def IDirectDraw2_CreatePalette(p, a, b, c, d):
    return p.lpVtbl.CreatePalette(p, a, b, c, d)


def IDirectDraw2_CreateSurface(p, a, b, c):
    return p.lpVtbl.CreateSurface(p, a, b, c)


def IDirectDraw2_DuplicateSurface(p, a, b):
    return p.lpVtbl.DuplicateSurface(p, a, b)


def IDirectDraw2_EnumDisplayModes(p, a, b, c, d):
    return p.lpVtbl.EnumDisplayModes(p, a, b, c, d)


def IDirectDraw2_EnumSurfaces(p, a, b, c, d):
    return p.lpVtbl.EnumSurfaces(p, a, b, c, d)


def IDirectDraw2_FlipToGDISurface(p):
    return p.lpVtbl.FlipToGDISurface(p)


def IDirectDraw2_GetCaps(p, a, b):
    return p.lpVtbl.GetCaps(p, a, b)


def IDirectDraw2_GetDisplayMode(p, a):
    return p.lpVtbl.GetDisplayMode(p, a)


def IDirectDraw2_GetFourCCCodes(p, a, b):
    return p.lpVtbl.GetFourCCCodes(p, a, b)


def IDirectDraw2_GetGDISurface(p, a):
    return p.lpVtbl.GetGDISurface(p, a)


def IDirectDraw2_GetMonitorFrequency(p, a):
    return p.lpVtbl.GetMonitorFrequency(p, a)


def IDirectDraw2_GetScanLine(p, a):
    return p.lpVtbl.GetScanLine(p, a)


def IDirectDraw2_GetVerticalBlankStatus(p, a):
    return p.lpVtbl.GetVerticalBlankStatus(p, a)


def IDirectDraw2_Initialize(p, a):
    return p.lpVtbl.Initialize(p, a)


def IDirectDraw2_RestoreDisplayMode(p):
    return p.lpVtbl.RestoreDisplayMode(p)


def IDirectDraw2_SetCooperativeLevel(p, a, b):
    return p.lpVtbl.SetCooperativeLevel(p, a, b)


def IDirectDraw2_SetDisplayMode(p, a, b, c, d, e):
    return p.lpVtbl.SetDisplayMode(p, a, b, c, d, e)


def IDirectDraw2_WaitForVerticalBlank(p, a, b):
    return p.lpVtbl.WaitForVerticalBlank(p, a, b)


def IDirectDraw2_GetAvailableVidMem(p, a, b, c):
    return p.lpVtbl.GetAvailableVidMem(p, a, b, c)



def IDirectDraw4_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p, a, b)


def IDirectDraw4_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDraw4_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDraw4_Compact(p):
    return p.lpVtbl.Compact(p)


def IDirectDraw4_CreateClipper(p, a, b, c):
    return p.lpVtbl.CreateClipper(p, a, b, c)


def IDirectDraw4_CreatePalette(p, a, b, c, d):
    return p.lpVtbl.CreatePalette(p, a, b, c, d)


def IDirectDraw4_CreateSurface(p, a, b, c):
    return p.lpVtbl.CreateSurface(p, a, b, c)


def IDirectDraw4_DuplicateSurface(p, a, b):
    return p.lpVtbl.DuplicateSurface(p, a, b)


def IDirectDraw4_EnumDisplayModes(p, a, b, c, d):
    return p.lpVtbl.EnumDisplayModes(p, a, b, c, d)


def IDirectDraw4_EnumSurfaces(p, a, b, c, d):
    return p.lpVtbl.EnumSurfaces(p, a, b, c, d)


def IDirectDraw4_FlipToGDISurface(p):
    return p.lpVtbl.FlipToGDISurface(p)


def IDirectDraw4_GetCaps(p, a, b):
    return p.lpVtbl.GetCaps(p, a, b)


def IDirectDraw4_GetDisplayMode(p, a):
    return p.lpVtbl.GetDisplayMode(p, a)


def IDirectDraw4_GetFourCCCodes(p, a, b):
    return p.lpVtbl.GetFourCCCodes(p, a, b)


def IDirectDraw4_GetGDISurface(p, a):
    return p.lpVtbl.GetGDISurface(p, a)


def IDirectDraw4_GetMonitorFrequency(p, a):
    return p.lpVtbl.GetMonitorFrequency(p, a)


def IDirectDraw4_GetScanLine(p, a):
    return p.lpVtbl.GetScanLine(p, a)


def IDirectDraw4_GetVerticalBlankStatus(p, a):
    return p.lpVtbl.GetVerticalBlankStatus(p, a)


def IDirectDraw4_Initialize(p, a):
    return p.lpVtbl.Initialize(p, a)


def IDirectDraw4_RestoreDisplayMode(p):
    return p.lpVtbl.RestoreDisplayMode(p)


def IDirectDraw4_SetCooperativeLevel(p, a, b):
    return p.lpVtbl.SetCooperativeLevel(p, a, b)


def IDirectDraw4_SetDisplayMode(p, a, b, c, d, e):
    return p.lpVtbl.SetDisplayMode(p, a, b, c, d, e)


def IDirectDraw4_WaitForVerticalBlank(p, a, b):
    return p.lpVtbl.WaitForVerticalBlank(p, a, b)


def IDirectDraw4_GetAvailableVidMem(p, a, b, c):
    return p.lpVtbl.GetAvailableVidMem(p, a, b, c)




def IDirectDraw4_GetSurfaceFromDC(p, a, b):
    return p.lpVtbl.GetSurfaceFromDC(p, a, b)


def IDirectDraw4_RestoreAllSurfaces(p):
    return p.lpVtbl.RestoreAllSurfaces(p)


def IDirectDraw4_TestCooperativeLevel(p):
    return p.lpVtbl.TestCooperativeLevel(p)


def IDirectDraw4_GetDeviceIdentifier(p, a, b):
    return p.lpVtbl.GetDeviceIdentifier(p,a,b)


def IDirectDraw7_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterfacep, a, b


def IDirectDraw7_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDraw7_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDraw7_Compact(p):
    return p.lpVtbl.Compact(p)


def IDirectDraw7_CreateClipper(p, a, b, c):
    return p.lpVtbl.CreateClipper(p, a, b, c)


def IDirectDraw7_CreatePalette(p, a, b, c, d):
    return p.lpVtbl.CreatePalette(p, a, b, c, d)


def IDirectDraw7_CreateSurface(p, a, b, c):
    return p.lpVtbl.CreateSurface(p, a, b, c)


def IDirectDraw7_DuplicateSurface(p, a, b):
    return p.lpVtbl.DuplicateSurface(p, a, b)


def IDirectDraw7_EnumDisplayModes(p, a, b, c, d):
    return p.lpVtbl.EnumDisplayModes(p, a, b, c, d)


def IDirectDraw7_EnumSurfaces(p, a, b, c, d):
    return p.lpVtbl.EnumSurfaces(p, a, b, c, d)


def IDirectDraw7_FlipToGDISurface(p):
    return p.lpVtbl.FlipToGDISurface(p)


def IDirectDraw7_GetCaps(p, a, b):
    return p.lpVtbl.GetCaps(p, a, b)


def IDirectDraw7_GetDisplayMode(p, a):
    return p.lpVtbl.GetDisplayMode(p, a)


def IDirectDraw7_GetFourCCCodes(p, a, b):
    return p.lpVtbl.GetFourCCCodes(p, a, b)


def IDirectDraw7_GetGDISurface(p, a):
    return p.lpVtbl.GetGDISurface(p, a)


def IDirectDraw7_GetMonitorFrequency(p, a):
    return p.lpVtbl.GetMonitorFrequency(p, a)


def IDirectDraw7_GetScanLine(p, a):
    return p.lpVtbl.GetScanLine(p, a)


def IDirectDraw7_GetVerticalBlankStatus(p, a):
    return p.lpVtbl.GetVerticalBlankStatus(p, a)


def IDirectDraw7_Initialize(p, a):
    return p.lpVtbl.Initialize(p, a)


def IDirectDraw7_RestoreDisplayMode(p):
    return p.lpVtbl.RestoreDisplayMode(p)


def IDirectDraw7_SetCooperativeLevel(p, a, b):
    return p.lpVtbl.SetCooperativeLevel(p, a, b)


def IDirectDraw7_SetDisplayMode(p, a, b, c, d, e):
    return p.lpVtbl.SetDisplayMode(p, a, b, c, d, e)


def IDirectDraw7_WaitForVerticalBlank(p, a, b):
    return p.lpVtbl.WaitForVerticalBlank(p, a, b)


def IDirectDraw7_GetAvailableVidMem(p, a, b, c):
    return p.lpVtbl.GetAvailableVidMem(p, a, b, c)


def IDirectDraw7_GetSurfaceFromDC(p, a, b):
    return p.lpVtbl.GetSurfaceFromDC(p, a, b)


def IDirectDraw7_RestoreAllSurfaces(p):
    return p.lpVtbl.RestoreAllSurfaces(p)


def IDirectDraw7_TestCooperativeLevel(p):
    return p.lpVtbl.TestCooperativeLevel(p)


def IDirectDraw7_GetDeviceIdentifier(p, a, b):
    return p.lpVtbl.GetDeviceIdentifier(p,a,b)


def IDirectDraw7_StartModeTest(p, a, b, c):
    return p.lpVtbl.StartModeTest(p,a,b,c)


def IDirectDraw7_EvaluateMode(p, a, b):
    return p.lpVtbl.EvaluateMode(p,a,b)

def IDirectDrawPalette_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p, a, b)


def IDirectDrawPalette_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawPalette_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawPalette_GetCaps(p, a):
    return p.lpVtbl.GetCaps(p, a)


def IDirectDrawPalette_GetEntries(p, a, b, c, d):
    return p.lpVtbl.GetEntries(p, a, b, c, d)


def IDirectDrawPalette_Initialize(p, a, b, c):
    return p.lpVtbl.Initialize(p, a, b, c)


def IDirectDrawPalette_SetEntries(p, a, b, c, d):
    return p.lpVtbl.SetEntries(p, a, b, c, d)


def IDirectDrawClipper_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p, a, b)


def IDirectDrawClipper_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawClipper_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawClipper_GetClipList(p, a, b, c):
    return p.lpVtbl.GetClipList(p, a, b, c)


def IDirectDrawClipper_GetHWnd(p, a):
    return p.lpVtbl.GetHWnd(p, a)


def IDirectDrawClipper_Initialize(p, a, b):
    return p.lpVtbl.Initialize(p, a, b)


def IDirectDrawClipper_IsClipListChanged(p, a):
    return p.lpVtbl.IsClipListChanged(p, a)


def IDirectDrawClipper_SetClipList(p, a, b):
    return p.lpVtbl.SetClipList(p, a, b)


def IDirectDrawClipper_SetHWnd(p, a, b):
    return p.lpVtbl.SetHWnd(p, a, b)


def IDirectDrawSurface_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p,a,b)


def IDirectDrawSurface_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawSurface_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawSurface_AddAttachedSurface(p, a):
    return p.lpVtbl.AddAttachedSurface(p,a)


def IDirectDrawSurface_AddOverlayDirtyRect(p, a):
    return p.lpVtbl.AddOverlayDirtyRect(p,a)


def IDirectDrawSurface_Blt(p, a, b, c, d, e):
    return p.lpVtbl.Blt(p,a,b,c,d,e)


def IDirectDrawSurface_BltBatch(p, a, b, c):
    return p.lpVtbl.BltBatch(p,a,b,c)


def IDirectDrawSurface_BltFast(p, a, b, c, d, e):
    return p.lpVtbl.BltFast(p,a,b,c,d,e)


def IDirectDrawSurface_DeleteAttachedSurface(p, a, b):
    return p.lpVtbl.DeleteAttachedSurface(p,a,b)


def IDirectDrawSurface_EnumAttachedSurfaces(p, a, b):
    return p.lpVtbl.EnumAttachedSurfaces(p,a,b)


def IDirectDrawSurface_EnumOverlayZOrders(p, a, b, c):
    return p.lpVtbl.EnumOverlayZOrders(p,a,b,c)


def IDirectDrawSurface_Flip(p, a, b):
    return p.lpVtbl.Flip(p,a,b)


def IDirectDrawSurface_GetAttachedSurface(p, a, b):
    return p.lpVtbl.GetAttachedSurface(p,a,b)


def IDirectDrawSurface_GetBltStatus(p, a):
    return p.lpVtbl.GetBltStatus(p,a)


def IDirectDrawSurface_GetCaps(p, b):
    return p.lpVtbl.GetCaps(p,b)


def IDirectDrawSurface_GetClipper(p, a):
    return p.lpVtbl.GetClipper(p,a)


def IDirectDrawSurface_GetColorKey(p, a, b):
    return p.lpVtbl.GetColorKey(p,a,b)


def IDirectDrawSurface_GetDC(p, a):
    return p.lpVtbl.GetDC(p,a)


def IDirectDrawSurface_GetFlipStatus(p, a):
    return p.lpVtbl.GetFlipStatus(p,a)


def IDirectDrawSurface_GetOverlayPosition(p, a, b):
    return p.lpVtbl.GetOverlayPosition(p,a,b)


def IDirectDrawSurface_GetPalette(p, a):
    return p.lpVtbl.GetPalette(p,a)


def IDirectDrawSurface_GetPixelFormat(p, a):
    return p.lpVtbl.GetPixelFormat(p,a)


def IDirectDrawSurface_GetSurfaceDesc(p, a):
    return p.lpVtbl.GetSurfaceDesc(p,a)


def IDirectDrawSurface_Initialize(p, a, b):
    return p.lpVtbl.Initialize(p,a,b)


def IDirectDrawSurface_IsLost(p):
    return p.lpVtbl.IsLost(p)


def IDirectDrawSurface_Lock(p, a, b, c, d):
    return p.lpVtbl.Lock(p,a,b,c,d)


def IDirectDrawSurface_ReleaseDC(p, a):
    return p.lpVtbl.ReleaseDC(p,a)


def IDirectDrawSurface_Restore(p):
    return p.lpVtbl.Restore(p)


def IDirectDrawSurface_SetClipper(p, a):
    return p.lpVtbl.SetClipper(p,a)


def IDirectDrawSurface_SetColorKey(p, a, b):
    return p.lpVtbl.SetColorKey(p,a,b)


def IDirectDrawSurface_SetOverlayPosition(p, a, b):
    return p.lpVtbl.SetOverlayPosition(p,a,b)


def IDirectDrawSurface_SetPalette(p, a):
    return p.lpVtbl.SetPalette(p,a)


def IDirectDrawSurface_Unlock(p, b):
    return p.lpVtbl.Unlock(p,b)


def IDirectDrawSurface_UpdateOverlay(p, a, b, c, d, e):
    return p.lpVtbl.UpdateOverlay(p,a,b,c,d,e)


def IDirectDrawSurface_UpdateOverlayDisplay(p, a):
    return p.lpVtbl.UpdateOverlayDisplay(p,a)


def IDirectDrawSurface_UpdateOverlayZOrder(p, a, b):
    return p.lpVtbl.UpdateOverlayZOrder(p,a,b)


def IDirectDrawSurface2_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p,a,b)


def IDirectDrawSurface2_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawSurface2_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawSurface2_AddAttachedSurface(p, a):
    return p.lpVtbl.AddAttachedSurface(p,a)


def IDirectDrawSurface2_AddOverlayDirtyRect(p, a):
    return p.lpVtbl.AddOverlayDirtyRect(p,a)


def IDirectDrawSurface2_Blt(p, a, b, c, d, e):
    return p.lpVtbl.Blt(p,a,b,c,d,e)


def IDirectDrawSurface2_BltBatch(p, a, b, c):
    return p.lpVtbl.BltBatch(p,a,b,c)


def IDirectDrawSurface2_BltFast(p, a, b, c, d, e):
    return p.lpVtbl.BltFast(p,a,b,c,d,e)


def IDirectDrawSurface2_DeleteAttachedSurface(p, a, b):
    return p.lpVtbl.DeleteAttachedSurface(p,a,b)


def IDirectDrawSurface2_EnumAttachedSurfaces(p, a, b):
    return p.lpVtbl.EnumAttachedSurfaces(p,a,b)


def IDirectDrawSurface2_EnumOverlayZOrders(p, a, b, c):
    return p.lpVtbl.EnumOverlayZOrders(p,a,b,c)


def IDirectDrawSurface2_Flip(p, a, b):
    return p.lpVtbl.Flip(p,a,b)


def IDirectDrawSurface2_GetAttachedSurface(p, a, b):
    return p.lpVtbl.GetAttachedSurface(p,a,b)


def IDirectDrawSurface2_GetBltStatus(p, a):
    return p.lpVtbl.GetBltStatus(p,a)


def IDirectDrawSurface2_GetCaps(p, b):
    return p.lpVtbl.GetCaps(p,b)


def IDirectDrawSurface2_GetClipper(p, a):
    return p.lpVtbl.GetClipper(p,a)


def IDirectDrawSurface2_GetColorKey(p, a, b):
    return p.lpVtbl.GetColorKey(p,a,b)


def IDirectDrawSurface2_GetDC(p, a):
    return p.lpVtbl.GetDC(p,a)


def IDirectDrawSurface2_GetFlipStatus(p, a):
    return p.lpVtbl.GetFlipStatus(p,a)


def IDirectDrawSurface2_GetOverlayPosition(p, a, b):
    return p.lpVtbl.GetOverlayPosition(p,a,b)


def IDirectDrawSurface2_GetPalette(p, a):
    return p.lpVtbl.GetPalette(p,a)


def IDirectDrawSurface2_GetPixelFormat(p, a):
    return p.lpVtbl.GetPixelFormat(p,a)


def IDirectDrawSurface2_GetSurfaceDesc(p, a):
    return p.lpVtbl.GetSurfaceDesc(p,a)


def IDirectDrawSurface2_Initialize(p, a, b):
    return p.lpVtbl.Initialize(p,a,b)


def IDirectDrawSurface2_IsLost(p):
    return p.lpVtbl.IsLost(p)


def IDirectDrawSurface2_Lock(p, a, b, c, d):
    return p.lpVtbl.Lock(p,a,b,c,d)


def IDirectDrawSurface2_ReleaseDC(p, a):
    return p.lpVtbl.ReleaseDC(p,a)


def IDirectDrawSurface2_Restore(p):
    return p.lpVtbl.Restore(p)


def IDirectDrawSurface2_SetClipper(p, a):
    return p.lpVtbl.SetClipper(p,a)


def IDirectDrawSurface2_SetColorKey(p, a, b):
    return p.lpVtbl.SetColorKey(p,a,b)


def IDirectDrawSurface2_SetOverlayPosition(p, a, b):
    return p.lpVtbl.SetOverlayPosition(p,a,b)


def IDirectDrawSurface2_SetPalette(p, a):
    return p.lpVtbl.SetPalette(p,a)


def IDirectDrawSurface2_Unlock(p, b):
    return p.lpVtbl.Unlock(p,b)


def IDirectDrawSurface2_UpdateOverlay(p, a, b, c, d, e):
    return p.lpVtbl.UpdateOverlay(p,a,b,c,d,e)


def IDirectDrawSurface2_UpdateOverlayDisplay(p, a):
    return p.lpVtbl.UpdateOverlayDisplay(p,a)


def IDirectDrawSurface2_UpdateOverlayZOrder(p, a, b):
    return p.lpVtbl.UpdateOverlayZOrder(p,a,b)


def IDirectDrawSurface2_GetDDInterface(p, a):
    return p.lpVtbl.GetDDInterface(p,a)


def IDirectDrawSurface2_PageLock(p, a):
    return p.lpVtbl.PageLock(p,a)


def IDirectDrawSurface2_PageUnlock(p, a):
    return p.lpVtbl.PageUnlock(p,a)


def IDirectDrawSurface3_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface((p,a,b))


def IDirectDrawSurface3_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawSurface3_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawSurface3_AddAttachedSurface(p, a):
    return p.lpVtbl.AddAttachedSurface(p,a)


def IDirectDrawSurface3_AddOverlayDirtyRect(p, a):
    return p.lpVtbl.AddOverlayDirtyRect(p,a)


def IDirectDrawSurface3_Blt(p, a, b, c, d, e):
    return p.lpVtbl.Blt(p,a,b,c,d,e)


def IDirectDrawSurface3_BltBatch(p, a, b, c):
    return p.lpVtbl.BltBatch(p,a,b,c)


def IDirectDrawSurface3_BltFast(p, a, b, c, d, e):
    return p.lpVtbl.BltFast(p,a,b,c,d,e)


def IDirectDrawSurface3_DeleteAttachedSurface(p, a, b):
    return p.lpVtbl.DeleteAttachedSurface(p,a,b)


def IDirectDrawSurface3_EnumAttachedSurfaces(p, a, b):
    return p.lpVtbl.EnumAttachedSurfaces(p,a,b)


def IDirectDrawSurface3_EnumOverlayZOrders(p, a, b, c):
    return p.lpVtbl.EnumOverlayZOrders(p,a,b,c)


def IDirectDrawSurface3_Flip(p, a, b):
    return p.lpVtbl.Flip(p,a,b)


def IDirectDrawSurface3_GetAttachedSurface(p, a, b):
    return p.lpVtbl.GetAttachedSurface(p,a,b)


def IDirectDrawSurface3_GetBltStatus(p, a):
    return p.lpVtbl.GetBltStatus(p,a)


def IDirectDrawSurface3_GetCaps(p, b):
    return p.lpVtbl.GetCaps(p,b)


def IDirectDrawSurface3_GetClipper(p, a):
    return p.lpVtbl.GetClipper(p,a)


def IDirectDrawSurface3_GetColorKey(p, a, b):
    return p.lpVtbl.GetColorKey(p,a,b)


def IDirectDrawSurface3_GetDC(p, a):
    return p.lpVtbl.GetDC(p,a)


def IDirectDrawSurface3_GetFlipStatus(p, a):
    return p.lpVtbl.GetFlipStatus(p,a)


def IDirectDrawSurface3_GetOverlayPosition(p, a, b):
    return p.lpVtbl.GetOverlayPosition(p,a,b)


def IDirectDrawSurface3_GetPalette(p, a):
    return p.lpVtbl.GetPalette(p,a)


def IDirectDrawSurface3_GetPixelFormat(p, a):
    return p.lpVtbl.GetPixelFormat(p,a)


def IDirectDrawSurface3_GetSurfaceDesc(p, a):
    return p.lpVtbl.GetSurfaceDesc(p,a)


def IDirectDrawSurface3_Initialize(p, a, b):
    return p.lpVtbl.Initialize(p,a,b)


def IDirectDrawSurface3_IsLost(p):
    return p.lpVtbl.IsLost(p)


def IDirectDrawSurface3_Lock(p, a, b, c, d):
    return p.lpVtbl.Lock(p,a,b,c,d)


def IDirectDrawSurface3_ReleaseDC(p, a):
    return p.lpVtbl.ReleaseDC(p,a)


def IDirectDrawSurface3_Restore(p):
    return p.lpVtbl.Restore(p)


def IDirectDrawSurface3_SetClipper(p, a):
    return p.lpVtbl.SetClipper(p,a)


def IDirectDrawSurface3_SetColorKey(p, a, b):
    return p.lpVtbl.SetColorKey(p,a,b)


def IDirectDrawSurface3_SetOverlayPosition(p, a, b):
    return p.lpVtbl.SetOverlayPosition(p,a,b)


def IDirectDrawSurface3_SetPalette(p, a):
    return p.lpVtbl.SetPalette(p,a)


def IDirectDrawSurface3_Unlock(p, b):
    return p.lpVtbl.Unlock(p,b)


def IDirectDrawSurface3_UpdateOverlay(p, a, b, c, d, e):
    return p.lpVtbl.UpdateOverlay(p,a,b,c,d,e)


def IDirectDrawSurface3_UpdateOverlayDisplay(p, a):
    return p.lpVtbl.UpdateOverlayDisplay(p,a)


def IDirectDrawSurface3_UpdateOverlayZOrder(p, a, b):
    return p.lpVtbl.UpdateOverlayZOrder(p,a,b)


def IDirectDrawSurface3_GetDDInterface(p, a):
    return p.lpVtbl.GetDDInterface(p,a)


def IDirectDrawSurface3_PageLock(p, a):
    return p.lpVtbl.PageLock(p,a)


def IDirectDrawSurface3_PageUnlock(p, a):
    return p.lpVtbl.PageUnlock(p,a)


def IDirectDrawSurface3_SetSurfaceDesc(p, a, b):
    return p.lpVtbl.SetSurfaceDesc(p,a,b)


def IDirectDrawSurface4_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p,a,b)


def IDirectDrawSurface4_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawSurface4_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawSurface4_AddAttachedSurface(p, a):
    return p.lpVtbl.AddAttachedSurface(p,a)


def IDirectDrawSurface4_AddOverlayDirtyRect(p, a):
    return p.lpVtbl.AddOverlayDirtyRect(p,a)


def IDirectDrawSurface4_Blt(p, a, b, c, d, e):
    return p.lpVtbl.Blt(p,a,b,c,d,e)


def IDirectDrawSurface4_BltBatch(p, a, b, c):
    return p.lpVtbl.BltBatch(p,a,b,c)


def IDirectDrawSurface4_BltFast(p, a, b, c, d, e):
    return p.lpVtbl.BltFast(p,a,b,c,d,e)


def IDirectDrawSurface4_DeleteAttachedSurface(p, a, b):
    return p.lpVtbl.DeleteAttachedSurface(p,a,b)


def IDirectDrawSurface4_EnumAttachedSurfaces(p, a, b):
    return p.lpVtbl.EnumAttachedSurfaces(p,a,b)


def IDirectDrawSurface4_EnumOverlayZOrders(p, a, b, c):
    return p.lpVtbl.EnumOverlayZOrders(p,a,b,c)


def IDirectDrawSurface4_Flip(p, a, b):
    return p.lpVtbl.Flip(p,a,b)


def IDirectDrawSurface4_GetAttachedSurface(p, a, b):
    return p.lpVtbl.GetAttachedSurface(p,a,b)


def IDirectDrawSurface4_GetBltStatus(p, a):
    return p.lpVtbl.GetBltStatus(p,a)


def IDirectDrawSurface4_GetCaps(p, b):
    return p.lpVtbl.GetCaps(p,b)


def IDirectDrawSurface4_GetClipper(p, a):
    return p.lpVtbl.GetClipper(p,a)


def IDirectDrawSurface4_GetColorKey(p, a, b):
    return p.lpVtbl.GetColorKey(p,a,b)


def IDirectDrawSurface4_GetDC(p, a):
    return p.lpVtbl.GetDC(p,a)


def IDirectDrawSurface4_GetFlipStatus(p, a):
    return p.lpVtbl.GetFlipStatus(p,a)


def IDirectDrawSurface4_GetOverlayPosition(p, a, b):
    return p.lpVtbl.GetOverlayPosition(p,a,b)


def IDirectDrawSurface4_GetPalette(p, a):
    return p.lpVtbl.GetPalette(p,a)


def IDirectDrawSurface4_GetPixelFormat(p, a):
    return p.lpVtbl.GetPixelFormat(p,a)


def IDirectDrawSurface4_GetSurfaceDesc(p, a):
    return p.lpVtbl.GetSurfaceDesc(p,a)


def IDirectDrawSurface4_Initialize(p, a, b):
    return p.lpVtbl.Initialize(p,a,b)


def IDirectDrawSurface4_IsLost(p):
    return p.lpVtbl.IsLost(p)


def IDirectDrawSurface4_Lock(p, a, b, c, d):
    return p.lpVtbl.Lock(p,a,b,c,d)


def IDirectDrawSurface4_ReleaseDC(p, a):
    return p.lpVtbl.ReleaseDC(p,a)


def IDirectDrawSurface4_Restore(p):
    return p.lpVtbl.Restore(p)


def IDirectDrawSurface4_SetClipper(p, a):
    return p.lpVtbl.SetClipper(p,a)


def IDirectDrawSurface4_SetColorKey(p, a, b):
    return p.lpVtbl.SetColorKey(p,a,b)


def IDirectDrawSurface4_SetOverlayPosition(p, a, b):
    return p.lpVtbl.SetOverlayPosition(p,a,b)


def IDirectDrawSurface4_SetPalette(p, a):
    return p.lpVtbl.SetPalette(p,a)


def IDirectDrawSurface4_Unlock(p, b):
    return p.lpVtbl.Unlock(p,b)


def IDirectDrawSurface4_UpdateOverlay(p, a, b, c, d, e):
    return p.lpVtbl.UpdateOverlay(p,a,b,c,d,e)


def IDirectDrawSurface4_UpdateOverlayDisplay(p, a):
    return p.lpVtbl.UpdateOverlayDisplay(p,a)


def IDirectDrawSurface4_UpdateOverlayZOrder(p, a, b):
    return p.lpVtbl.UpdateOverlayZOrder(p,a,b)


def IDirectDrawSurface4_GetDDInterface(p, a):
    return p.lpVtbl.GetDDInterface(p,a)


def IDirectDrawSurface4_PageLock(p, a):
    return p.lpVtbl.PageLock(p,a)


def IDirectDrawSurface4_PageUnlock(p, a):
    return p.lpVtbl.PageUnlock(p,a)


def IDirectDrawSurface4_SetSurfaceDesc(p, a, b):
    return p.lpVtbl.SetSurfaceDesc(p,a,b)


def IDirectDrawSurface4_SetPrivateData(p, a, b, c, d):
    return p.lpVtbl.SetPrivateData(p,a,b,c,d)


def IDirectDrawSurface4_GetPrivateData(p, a, b, c):
    return p.lpVtbl.GetPrivateData(p,a,b,c)


def IDirectDrawSurface4_FreePrivateData(p, a):
    return p.lpVtbl.FreePrivateData(p,a)


def IDirectDrawSurface4_GetUniquenessValue(p, a):
    return p.lpVtbl.GetUniquenessValue(p, a)


def IDirectDrawSurface4_ChangeUniquenessValue(p):
    return p.lpVtbl.ChangeUniquenessValue(p)


def IDirectDrawSurface7_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p,a,b)


def IDirectDrawSurface7_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawSurface7_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawSurface7_AddAttachedSurface(p, a):
    return p.lpVtbl.AddAttachedSurface(p,a)


def IDirectDrawSurface7_AddOverlayDirtyRect(p, a):
    return p.lpVtbl.AddOverlayDirtyRect(p,a)


def IDirectDrawSurface7_Blt(p, a, b, c, d, e):
    return p.lpVtbl.Blt(p,a,b,c,d,e)


def IDirectDrawSurface7_BltBatch(p, a, b, c):
    return p.lpVtbl.BltBatch(p,a,b,c)


def IDirectDrawSurface7_BltFast(p, a, b, c, d, e):
    return p.lpVtbl.BltFast(p,a,b,c,d,e)


def IDirectDrawSurface7_DeleteAttachedSurface(p, a, b):
    return p.lpVtbl.DeleteAttachedSurface(p,a,b)


def IDirectDrawSurface7_EnumAttachedSurfaces(p, a, b):
    return p.lpVtbl.EnumAttachedSurfaces(p,a,b)


def IDirectDrawSurface7_EnumOverlayZOrders(p, a, b, c):
    return p.lpVtbl.EnumOverlayZOrders(p,a,b,c)


def IDirectDrawSurface7_Flip(p, a, b):
    return p.lpVtbl.Flip(p,a,b)


def IDirectDrawSurface7_GetAttachedSurface(p, a, b):
    return p.lpVtbl.GetAttachedSurface(p,a,b)


def IDirectDrawSurface7_GetBltStatus(p, a):
    return p.lpVtbl.GetBltStatus(p,a)


def IDirectDrawSurface7_GetCaps(p, b):
    return p.lpVtbl.GetCaps(p,b)


def IDirectDrawSurface7_GetClipper(p, a):
    return p.lpVtbl.GetClipper(p,a)


def IDirectDrawSurface7_GetColorKey(p, a, b):
    return p.lpVtbl.GetColorKey(p,a,b)


def IDirectDrawSurface7_GetDC(p, a):
    return p.lpVtbl.GetDC(p,a)


def IDirectDrawSurface7_GetFlipStatus(p, a):
    return p.lpVtbl.GetFlipStatus(p,a)


def IDirectDrawSurface7_GetOverlayPosition(p, a, b):
    return p.lpVtbl.GetOverlayPosition(p,a,b)


def IDirectDrawSurface7_GetPalette(p, a):
    return p.lpVtbl.GetPalette(p,a)


def IDirectDrawSurface7_GetPixelFormat(p, a):
    return p.lpVtbl.GetPixelFormat(p,a)


def IDirectDrawSurface7_GetSurfaceDesc(p, a):
    return p.lpVtbl.GetSurfaceDesc(p,a)


def IDirectDrawSurface7_Initialize(p, a, b):
    return p.lpVtbl.Initialize(p,a,b)


def IDirectDrawSurface7_IsLost(p):
    return p.lpVtbl.IsLost(p)


def IDirectDrawSurface7_Lock(p, a, b, c, d):
    return p.lpVtbl.Lock(p,a,b,c,d)


def IDirectDrawSurface7_ReleaseDC(p, a):
    return p.lpVtbl.ReleaseDC(p,a)


def IDirectDrawSurface7_Restore(p):
    return p.lpVtbl.Restore(p)


def IDirectDrawSurface7_SetClipper(p, a):
    return p.lpVtbl.SetClipper(p,a)


def IDirectDrawSurface7_SetColorKey(p, a, b):
    return p.lpVtbl.SetColorKey(p,a,b)


def IDirectDrawSurface7_SetOverlayPosition(p, a, b):
    return p.lpVtbl.SetOverlayPosition(p,a,b)


def IDirectDrawSurface7_SetPalette(p, a):
    return p.lpVtbl.SetPalette(p,a)


def IDirectDrawSurface7_Unlock(p, b):
    return p.lpVtbl.Unlock(p,b)


def IDirectDrawSurface7_UpdateOverlay(p, a, b, c, d, e):
    return p.lpVtbl.UpdateOverlay(p,a,b,c,d,e)


def IDirectDrawSurface7_UpdateOverlayDisplay(p, a):
    return p.lpVtbl.UpdateOverlayDisplay(p,a)


def IDirectDrawSurface7_UpdateOverlayZOrder(p, a, b):
    return p.lpVtbl.UpdateOverlayZOrder(p,a,b)


def IDirectDrawSurface7_GetDDInterface(p, a):
    return p.lpVtbl.GetDDInterface(p,a)


def IDirectDrawSurface7_PageLock(p, a):
    return p.lpVtbl.PageLock(p,a)


def IDirectDrawSurface7_PageUnlock(p, a):
    return p.lpVtbl.PageUnlock(p,a)


def IDirectDrawSurface7_SetSurfaceDesc(p, a, b):
    return p.lpVtbl.SetSurfaceDesc(p,a,b)


def IDirectDrawSurface7_SetPrivateData(p, a, b, c, d):
    return p.lpVtbl.SetPrivateData(p,a,b,c,d)


def IDirectDrawSurface7_GetPrivateData(p, a, b, c):
    return p.lpVtbl.GetPrivateData(p,a,b,c)


def IDirectDrawSurface7_FreePrivateData(p, a):
    return p.lpVtbl.FreePrivateData(p,a)


def IDirectDrawSurface7_GetUniquenessValue(p, a):
    return p.lpVtbl.GetUniquenessValue(p, a)


def IDirectDrawSurface7_ChangeUniquenessValue(p):
    return p.lpVtbl.ChangeUniquenessValue(p)


def IDirectDrawSurface7_SetPriority(p, a):
    return p.lpVtbl.SetPriority(p,a)


def IDirectDrawSurface7_GetPriority(p, a):
    return p.lpVtbl.GetPriority(p,a)


def IDirectDrawSurface7_SetLOD(p, a):
    return p.lpVtbl.SetLOD(p,a)


def IDirectDrawSurface7_GetLOD(p, a):
    return p.lpVtbl.GetLOD(p,a)


def IDirectDrawColorControl_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p, a, b)


def IDirectDrawColorControl_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawColorControl_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawColorControl_GetColorControls(p, a):
    return p.lpVtbl.GetColorControls(p, a)


def IDirectDrawColorControl_SetColorControls(p, a):
    return p.lpVtbl.SetColorControls(p, a)


def IDirectDrawGammaControl_QueryInterface(p, a, b):
    return p.lpVtbl.QueryInterface(p, a, b)


def IDirectDrawGammaControl_AddRef(p):
    return p.lpVtbl.AddRef(p)


def IDirectDrawGammaControl_Release(p):
    return p.lpVtbl.Release(p)


def IDirectDrawGammaControl_GetGammaRamp(p, a, b):
    return p.lpVtbl.GetGammaRamp(p, a, b)


def IDirectDrawGammaControl_SetGammaRamp(p, a, b):
    return p.lpVtbl.SetGammaRamp(p, a, b)


class _DDSURFACEDESC(ctypes.Structure):

    class DUMMYUNIONNAME1(ctypes.Union):
        _fields_ = [
            ('lPitch', LONG),
            ('dwLinearSize', DWORD),
        ]

    class DUMMYUNIONNAME2(ctypes.Union):
        _fields_ = [
            ('dwMipMapCount', DWORD),
            ('dwZBufferBitDepth', DWORD),
            ('dwRefreshRate', DWORD),
        ]

    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('dwHeight', DWORD),
        ('dwWidth', DWORD),
        ('DUMMYUNIONNAME1', DUMMYUNIONNAME1),
        ('dwBackBufferCount', DWORD),
        ('DUMMYUNIONNAME2', DUMMYUNIONNAME2),
        ('dwAlphaBitDepth', DWORD),
        ('dwReserved', DWORD),
        ('lpSurface', LPVOID),
        ('ddckCKDestOverlay', DDCOLORKEY),
        ('ddckCKDestBlt', DDCOLORKEY),
        ('ddckCKSrcOverlay', DDCOLORKEY),
        ('ddckCKSrcBlt', DDCOLORKEY),
        ('ddpfPixelFormat', DDPIXELFORMAT),
        ('ddsCaps', DDSCAPS),
    ]


DDSURFACEDESC = _DDSURFACEDESC



class _DDSURFACEDESC2(ctypes.Structure):

    class DUMMYUNIONNAME1(ctypes.Union):
        _fields_ = [
            ('lPitch', LONG),
            ('dwLinearSize', DWORD),
        ]

    class DUMMYUNIONNAME5(ctypes.Union):
        _fields_ = [
            ('dwBackBufferCount', DWORD),
            ('dwDepth', DWORD),
        ]

    class DUMMYUNIONNAME2(ctypes.Union):
        _fields_ = [
            ('dwMipMapCount', DWORD),
            ('dwRefreshRate', DWORD),
            ('dwSrcVBHandle', DWORD),
        ]

    class DUMMYUNIONNAME3(ctypes.Union):
        _fields_ = [
            ('ddckCKDestOverlay', DDCOLORKEY),
            ('dwEmptyFaceColor', DWORD),
        ]

    class DUMMYUNIONNAME4(ctypes.Union):
        _fields_ = [
            ('ddpfPixelFormat', DDPIXELFORMAT),
            ('dwFVF', DWORD),
        ]

    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('dwHeight', DWORD),
        ('dwWidth', DWORD),
        ('DUMMYUNIONNAME1', DUMMYUNIONNAME1),
        ('DUMMYUNIONNAME5', DUMMYUNIONNAME5),
        ('DUMMYUNIONNAME2', DUMMYUNIONNAME2),
        ('dwAlphaBitDepth', DWORD),
        ('dwReserved', DWORD),
        ('lpSurface', LPVOID),
        ('DUMMYUNIONNAME3', DUMMYUNIONNAME3),
        ('ddckCKDestBlt', DDCOLORKEY),
        ('ddckCKSrcOverlay', DDCOLORKEY),
        ('ddckCKSrcBlt', DDCOLORKEY),
        ('DUMMYUNIONNAME4', DUMMYUNIONNAME4),
        ('ddsCaps', DDSCAPS2),
        ('dwTextureStage', DWORD),
    ]


DDSURFACEDESC2 = _DDSURFACEDESC2


DDSD_CAPS = 0x00000001
DDSD_HEIGHT = 0x00000002
DDSD_WIDTH = 0x00000004
DDSD_PITCH = 0x00000008
DDSD_BACKBUFFERCOUNT = 0x00000020
DDSD_ZBUFFERBITDEPTH = 0x00000040
DDSD_ALPHABITDEPTH = 0x00000080
DDSD_LPSURFACE = 0x00000800
DDSD_PIXELFORMAT = 0x00001000
DDSD_CKDESTOVERLAY = 0x00002000
DDSD_CKDESTBLT = 0x00004000
DDSD_CKSRCOVERLAY = 0x00008000
DDSD_CKSRCBLT = 0x00010000
DDSD_MIPMAPCOUNT = 0x00020000
DDSD_REFRESHRATE = 0x00040000
DDSD_LINEARSIZE = 0x00080000
DDSD_TEXTURESTAGE = 0x00100000
DDSD_FVF = 0x00200000
DDSD_SRCVBHANDLE = 0x00400000
DDSD_DEPTH = 0x00800000
DDSD_ALL = 0x00fff9ee

class _DDOPTSURFACEDESC(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('ddSCaps', DDSCAPS2),
        ('ddOSCaps', DDOSCAPS),
        ('guid', GUID),
        ('dwCompressionRatio', DWORD),
    ]


DDOPTSURFACEDESC = _DDOPTSURFACEDESC


DDOSD_GUID = 0x00000001
DDOSD_COMPRESSION_RATIO = 0x00000002
DDOSD_SCAPS = 0x00000004
DDOSD_OSCAPS = 0x00000008
DDOSD_ALL = 0x0000000f
DDOSDCAPS_OPTCOMPRESSED = 0x00000001
DDOSDCAPS_OPTREORDERED = 0x00000002
DDOSDCAPS_MONOLITHICMIPMAP = 0x00000004
DDOSDCAPS_VALIDSCAPS = 0x30004800
DDOSDCAPS_VALIDOSCAPS = 0x00000007

class _DDCOLORCONTROL(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('lBrightness', LONG),
        ('lContrast', LONG),
        ('lHue', LONG),
        ('lSaturation', LONG),
        ('lSharpness', LONG),
        ('lGamma', LONG),
        ('lColorEnable', LONG),
        ('dwReserved1', DWORD),
    ]


DDCOLORCONTROL = _DDCOLORCONTROL


DDCOLOR_BRIGHTNESS = 0x00000001
DDCOLOR_CONTRAST = 0x00000002
DDCOLOR_HUE = 0x00000004
DDCOLOR_SATURATION = 0x00000008
DDCOLOR_SHARPNESS = 0x00000010
DDCOLOR_GAMMA = 0x00000020
DDCOLOR_COLORENABLE = 0x00000040
DDSCAPS_RESERVED1 = 0x00000001
DDSCAPS_ALPHA = 0x00000002
DDSCAPS_BACKBUFFER = 0x00000004
DDSCAPS_COMPLEX = 0x00000008
DDSCAPS_FLIP = 0x00000010
DDSCAPS_FRONTBUFFER = 0x00000020
DDSCAPS_OFFSCREENPLAIN = 0x00000040
DDSCAPS_OVERLAY = 0x00000080
DDSCAPS_PALETTE = 0x00000100
DDSCAPS_PRIMARYSURFACE = 0x00000200
DDSCAPS_RESERVED3 = 0x00000400
DDSCAPS_PRIMARYSURFACELEFT = 0x00000000
DDSCAPS_SYSTEMMEMORY = 0x00000800
DDSCAPS_TEXTURE = 0x00001000
DDSCAPS_3DDEVICE = 0x00002000
DDSCAPS_VIDEOMEMORY = 0x00004000
DDSCAPS_VISIBLE = 0x00008000
DDSCAPS_WRITEONLY = 0x00010000
DDSCAPS_ZBUFFER = 0x00020000
DDSCAPS_OWNDC = 0x00040000
DDSCAPS_LIVEVIDEO = 0x00080000
DDSCAPS_HWCODEC = 0x00100000
DDSCAPS_MODEX = 0x00200000
DDSCAPS_MIPMAP = 0x00400000
DDSCAPS_RESERVED2 = 0x00800000
DDSCAPS_ALLOCONLOAD = 0x04000000
DDSCAPS_VIDEOPORT = 0x08000000
DDSCAPS_LOCALVIDMEM = 0x10000000
DDSCAPS_NONLOCALVIDMEM = 0x20000000
DDSCAPS_STANDARDVGAMODE = 0x40000000
DDSCAPS_OPTIMIZED = 0x80000000
DDSCAPS2_RESERVED4 = 0x00000002
DDSCAPS2_HARDWAREDEINTERLACE = 0x00000000
DDSCAPS2_HINTDYNAMIC = 0x00000004
DDSCAPS2_HINTSTATIC = 0x00000008
DDSCAPS2_TEXTUREMANAGE = 0x00000010
DDSCAPS2_RESERVED1 = 0x00000020
DDSCAPS2_RESERVED2 = 0x00000040
DDSCAPS2_OPAQUE = 0x00000080
DDSCAPS2_HINTANTIALIASING = 0x00000100
DDSCAPS2_CUBEMAP = 0x00000200
DDSCAPS2_CUBEMAP_POSITIVEX = 0x00000400
DDSCAPS2_CUBEMAP_NEGATIVEX = 0x00000800
DDSCAPS2_CUBEMAP_POSITIVEY = 0x00001000
DDSCAPS2_CUBEMAP_NEGATIVEY = 0x00002000
DDSCAPS2_CUBEMAP_POSITIVEZ = 0x00004000
DDSCAPS2_CUBEMAP_NEGATIVEZ = 0x00008000
DDSCAPS2_CUBEMAP_ALLFACES = (
    DDSCAPS2_CUBEMAP_POSITIVEX  |
     DDSCAPS2_CUBEMAP_NEGATIVEX  |
     DDSCAPS2_CUBEMAP_POSITIVEY  |
     DDSCAPS2_CUBEMAP_NEGATIVEY  |
     DDSCAPS2_CUBEMAP_POSITIVEZ  |
     DDSCAPS2_CUBEMAP_NEGATIVEZ
)
DDSCAPS2_MIPMAPSUBLEVEL = 0x00010000
DDSCAPS2_D3DTEXTUREMANAGE = 0x00020000
DDSCAPS2_DONOTPERSIST = 0x00040000
DDSCAPS2_STEREOSURFACELEFT = 0x00080000
DDSCAPS2_VOLUME = 0x00200000
DDSCAPS2_NOTUSERLOCKABLE = 0x00400000
DDSCAPS2_POINTS = 0x00800000
DDSCAPS2_RTPATCHES = 0x01000000
DDSCAPS2_NPATCHES = 0x02000000
DDSCAPS2_RESERVED3 = 0x04000000
DDSCAPS2_DISCARDBACKBUFFER = 0x10000000
DDSCAPS2_ENABLEALPHACHANNEL = 0x20000000
DDSCAPS2_EXTENDEDFORMATPRIMARY = 0x40000000
DDSCAPS2_ADDITIONALPRIMARY = 0x80000000
DDSCAPS3_MULTISAMPLE_MASK = 0x0000001F
DDSCAPS3_MULTISAMPLE_QUALITY_MASK = 0x000000E0
DDSCAPS3_MULTISAMPLE_QUALITY_SHIFT = 0x5
DDSCAPS3_RESERVED1 = 0x00000100
DDSCAPS3_RESERVED2 = 0x00000200
DDSCAPS3_LIGHTWEIGHTMIPMAP = 0x00000400
DDSCAPS3_AUTOGENMIPMAP = 0x00000800
DDSCAPS3_DMAP = 0x00001000
DDSCAPS3_CREATESHAREDRESOURCE = 0x00002000
DDSCAPS3_READONLYRESOURCE = 0x00004000
DDSCAPS3_OPENSHAREDRESOURCE = 0x00008000
DDCAPS_3D = 0x00000001
DDCAPS_ALIGNBOUNDARYDEST = 0x00000002
DDCAPS_ALIGNSIZEDEST = 0x00000004
DDCAPS_ALIGNBOUNDARYSRC = 0x00000008
DDCAPS_ALIGNSIZESRC = 0x00000010
DDCAPS_ALIGNSTRIDE = 0x00000020
DDCAPS_BLT = 0x00000040
DDCAPS_BLTQUEUE = 0x00000080
DDCAPS_BLTFOURCC = 0x00000100
DDCAPS_BLTSTRETCH = 0x00000200
DDCAPS_GDI = 0x00000400
DDCAPS_OVERLAY = 0x00000800
DDCAPS_OVERLAYCANTCLIP = 0x00001000
DDCAPS_OVERLAYFOURCC = 0x00002000
DDCAPS_OVERLAYSTRETCH = 0x00004000
DDCAPS_PALETTE = 0x00008000
DDCAPS_PALETTEVSYNC = 0x00010000
DDCAPS_READSCANLINE = 0x00020000
DDCAPS_RESERVED1 = 0x00040000
DDCAPS_VBI = 0x00080000
DDCAPS_ZBLTS = 0x00100000
DDCAPS_ZOVERLAYS = 0x00200000
DDCAPS_COLORKEY = 0x00400000
DDCAPS_ALPHA = 0x00800000
DDCAPS_COLORKEYHWASSIST = 0x01000000
DDCAPS_NOHARDWARE = 0x02000000
DDCAPS_BLTCOLORFILL = 0x04000000
DDCAPS_BANKSWITCHED = 0x08000000
DDCAPS_BLTDEPTHFILL = 0x10000000
DDCAPS_CANCLIP = 0x20000000
DDCAPS_CANCLIPSTRETCHED = 0x40000000
DDCAPS_CANBLTSYSMEM = 0x80000000
DDCAPS2_CERTIFIED = 0x00000001
DDCAPS2_NO2DDURING3DSCENE = 0x00000002
DDCAPS2_VIDEOPORT = 0x00000004
DDCAPS2_AUTOFLIPOVERLAY = 0x00000008
DDCAPS2_CANBOBINTERLEAVED = 0x00000010
DDCAPS2_CANBOBNONINTERLEAVED = 0x00000020
DDCAPS2_COLORCONTROLOVERLAY = 0x00000040
DDCAPS2_COLORCONTROLPRIMARY = 0x00000080
DDCAPS2_CANDROPZ16BIT = 0x00000100
DDCAPS2_NONLOCALVIDMEM = 0x00000200
DDCAPS2_NONLOCALVIDMEMCAPS = 0x00000400
DDCAPS2_NOPAGELOCKREQUIRED = 0x00000800
DDCAPS2_WIDESURFACES = 0x00001000
DDCAPS2_CANFLIPODDEVEN = 0x00002000
DDCAPS2_CANBOBHARDWARE = 0x00004000
DDCAPS2_COPYFOURCC = 0x00008000
DDCAPS2_PRIMARYGAMMA = 0x00020000
DDCAPS2_CANRENDERWINDOWED = 0x00080000
DDCAPS2_CANCALIBRATEGAMMA = 0x00100000
DDCAPS2_FLIPINTERVAL = 0x00200000
DDCAPS2_FLIPNOVSYNC = 0x00400000
DDCAPS2_CANMANAGETEXTURE = 0x00800000
DDCAPS2_TEXMANINNONLOCALVIDMEM = 0x01000000
DDCAPS2_STEREO = 0x02000000
DDCAPS2_SYSTONONLOCAL_AS_SYSTOLOCAL = 0x04000000
DDCAPS2_RESERVED1 = 0x08000000
DDCAPS2_CANMANAGERESOURCE = 0x10000000
DDCAPS2_DYNAMICTEXTURES = 0x20000000
DDCAPS2_CANAUTOGENMIPMAP = 0x40000000
DDCAPS2_CANSHARERESOURCE = 0x80000000
DDFXALPHACAPS_BLTALPHAEDGEBLEND = 0x00000001
DDFXALPHACAPS_BLTALPHAPIXELS = 0x00000002
DDFXALPHACAPS_BLTALPHAPIXELSNEG = 0x00000004
DDFXALPHACAPS_BLTALPHASURFACES = 0x00000008
DDFXALPHACAPS_BLTALPHASURFACESNEG = 0x00000010
DDFXALPHACAPS_OVERLAYALPHAEDGEBLEND = 0x00000020
DDFXALPHACAPS_OVERLAYALPHAPIXELS = 0x00000040
DDFXALPHACAPS_OVERLAYALPHAPIXELSNEG = 0x00000080
DDFXALPHACAPS_OVERLAYALPHASURFACES = 0x00000100
DDFXALPHACAPS_OVERLAYALPHASURFACESNEG = 0x00000200
DDFXCAPS_BLTARITHSTRETCHY = 0x00000020
DDFXCAPS_BLTARITHSTRETCHYN = 0x00000010
DDFXCAPS_BLTMIRRORLEFTRIGHT = 0x00000040
DDFXCAPS_BLTMIRRORUPDOWN = 0x00000080
DDFXCAPS_BLTROTATION = 0x00000100
DDFXCAPS_BLTROTATION90 = 0x00000200
DDFXCAPS_BLTSHRINKX = 0x00000400
DDFXCAPS_BLTSHRINKXN = 0x00000800
DDFXCAPS_BLTSHRINKY = 0x00001000
DDFXCAPS_BLTSHRINKYN = 0x00002000
DDFXCAPS_BLTSTRETCHX = 0x00004000
DDFXCAPS_BLTSTRETCHXN = 0x00008000
DDFXCAPS_BLTSTRETCHY = 0x00010000
DDFXCAPS_BLTSTRETCHYN = 0x00020000
DDFXCAPS_OVERLAYARITHSTRETCHY = 0x00040000
DDFXCAPS_OVERLAYARITHSTRETCHYN = 0x00000008
DDFXCAPS_OVERLAYSHRINKX = 0x00080000
DDFXCAPS_OVERLAYSHRINKXN = 0x00100000
DDFXCAPS_OVERLAYSHRINKY = 0x00200000
DDFXCAPS_OVERLAYSHRINKYN = 0x00400000
DDFXCAPS_OVERLAYSTRETCHX = 0x00800000
DDFXCAPS_OVERLAYSTRETCHXN = 0x01000000
DDFXCAPS_OVERLAYSTRETCHY = 0x02000000
DDFXCAPS_OVERLAYSTRETCHYN = 0x04000000
DDFXCAPS_OVERLAYMIRRORLEFTRIGHT = 0x08000000
DDFXCAPS_OVERLAYMIRRORUPDOWN = 0x10000000
DDFXCAPS_OVERLAYDEINTERLACE = 0x20000000
DDFXCAPS_BLTALPHA = 0x00000001
DDFXCAPS_BLTFILTER = DDFXCAPS_BLTARITHSTRETCHY
DDFXCAPS_OVERLAYALPHA = 0x00000004
DDFXCAPS_OVERLAYFILTER = DDFXCAPS_OVERLAYARITHSTRETCHY
DDSVCAPS_RESERVED1 = 0x00000001
DDSVCAPS_RESERVED2 = 0x00000002
DDSVCAPS_RESERVED3 = 0x00000004
DDSVCAPS_RESERVED4 = 0x00000008
DDSVCAPS_STEREOSEQUENTIAL = 0x00000010
DDPCAPS_4BIT = 0x00000001
DDPCAPS_8BITENTRIES = 0x00000002
DDPCAPS_8BIT = 0x00000004
DDPCAPS_INITIALIZE = 0x00000000
DDPCAPS_PRIMARYSURFACE = 0x00000010
DDPCAPS_PRIMARYSURFACELEFT = 0x00000020
DDPCAPS_ALLOW256 = 0x00000040
DDPCAPS_VSYNC = 0x00000080
DDPCAPS_1BIT = 0x00000100
DDPCAPS_2BIT = 0x00000200
DDPCAPS_ALPHA = 0x00000400
DDSPD_IUNKNOWNPOINTER = 0x00000001
DDSPD_VOLATILE = 0x00000002
DDBD_1 = 0x00004000
DDBD_2 = 0x00002000
DDBD_4 = 0x00001000
DDBD_8 = 0x00000800
DDBD_16 = 0x00000400
DDBD_24 = 0x00000200
DDBD_32 = 0x00000100
DDCKEY_COLORSPACE = 0x00000001
DDCKEY_DESTBLT = 0x00000002
DDCKEY_DESTOVERLAY = 0x00000004
DDCKEY_SRCBLT = 0x00000008
DDCKEY_SRCOVERLAY = 0x00000010
DDCKEYCAPS_DESTBLT = 0x00000001
DDCKEYCAPS_DESTBLTCLRSPACE = 0x00000002
DDCKEYCAPS_DESTBLTCLRSPACEYUV = 0x00000004
DDCKEYCAPS_DESTBLTYUV = 0x00000008
DDCKEYCAPS_DESTOVERLAY = 0x00000010
DDCKEYCAPS_DESTOVERLAYCLRSPACE = 0x00000020
DDCKEYCAPS_DESTOVERLAYCLRSPACEYUV = 0x00000040
DDCKEYCAPS_DESTOVERLAYONEACTIVE = 0x00000080
DDCKEYCAPS_DESTOVERLAYYUV = 0x00000100
DDCKEYCAPS_SRCBLT = 0x00000200
DDCKEYCAPS_SRCBLTCLRSPACE = 0x00000400
DDCKEYCAPS_SRCBLTCLRSPACEYUV = 0x00000800
DDCKEYCAPS_SRCBLTYUV = 0x00001000
DDCKEYCAPS_SRCOVERLAY = 0x00002000
DDCKEYCAPS_SRCOVERLAYCLRSPACE = 0x00004000
DDCKEYCAPS_SRCOVERLAYCLRSPACEYUV = 0x00008000
DDCKEYCAPS_SRCOVERLAYONEACTIVE = 0x00010000
DDCKEYCAPS_SRCOVERLAYYUV = 0x00020000
DDCKEYCAPS_NOCOSTOVERLAY = 0x00040000
DDPF_ALPHAPIXELS = 0x00000001
DDPF_ALPHA = 0x00000002
DDPF_FOURCC = 0x00000004
DDPF_PALETTEINDEXED4 = 0x00000008
DDPF_PALETTEINDEXEDTO8 = 0x00000010
DDPF_PALETTEINDEXED8 = 0x00000020
DDPF_RGB = 0x00000040
DDPF_COMPRESSED = 0x00000080
DDPF_RGBTOYUV = 0x00000100
DDPF_YUV = 0x00000200
DDPF_ZBUFFER = 0x00000400
DDPF_PALETTEINDEXED1 = 0x00000800
DDPF_PALETTEINDEXED2 = 0x00001000
DDPF_ZPIXELS = 0x00002000
DDPF_STENCILBUFFER = 0x00004000
DDPF_ALPHAPREMULT = 0x00008000
DDPF_LUMINANCE = 0x00020000
DDPF_BUMPLUMINANCE = 0x00040000
DDPF_BUMPDUDV = 0x00080000
DDENUMSURFACES_ALL = 0x00000001
DDENUMSURFACES_MATCH = 0x00000002
DDENUMSURFACES_NOMATCH = 0x00000004
DDENUMSURFACES_CANBECREATED = 0x00000008
DDENUMSURFACES_DOESEXIST = 0x00000010
DDSDM_STANDARDVGAMODE = 0x00000001
DDEDM_REFRESHRATES = 0x00000001
DDEDM_STANDARDVGAMODES = 0x00000002
DDSCL_FULLSCREEN = 0x00000001
DDSCL_ALLOWREBOOT = 0x00000002
DDSCL_NOWINDOWCHANGES = 0x00000004
DDSCL_NORMAL = 0x00000008
DDSCL_EXCLUSIVE = 0x00000010
DDSCL_ALLOWMODEX = 0x00000040
DDSCL_SETFOCUSWINDOW = 0x00000080
DDSCL_SETDEVICEWINDOW = 0x00000100
DDSCL_CREATEDEVICEWINDOW = 0x00000200
DDSCL_MULTITHREADED = 0x00000400
DDSCL_FPUSETUP = 0x00000800
DDSCL_FPUPRESERVE = 0x00001000
DDBLT_ALPHADEST = 0x00000001
DDBLT_ALPHADESTCONSTOVERRIDE = 0x00000002
DDBLT_ALPHADESTNEG = 0x00000004
DDBLT_ALPHADESTSURFACEOVERRIDE = 0x00000008
DDBLT_ALPHAEDGEBLEND = 0x00000010
DDBLT_ALPHASRC = 0x00000020
DDBLT_ALPHASRCCONSTOVERRIDE = 0x00000040
DDBLT_ALPHASRCNEG = 0x00000080
DDBLT_ALPHASRCSURFACEOVERRIDE = 0x00000100
DDBLT_ASYNC = 0x00000200
DDBLT_COLORFILL = 0x00000400
DDBLT_DDFX = 0x00000800
DDBLT_DDROPS = 0x00001000
DDBLT_KEYDEST = 0x00002000
DDBLT_KEYDESTOVERRIDE = 0x00004000
DDBLT_KEYSRC = 0x00008000
DDBLT_KEYSRCOVERRIDE = 0x00010000
DDBLT_ROP = 0x00020000
DDBLT_ROTATIONANGLE = 0x00040000
DDBLT_ZBUFFER = 0x00080000
DDBLT_ZBUFFERDESTCONSTOVERRIDE = 0x00100000
DDBLT_ZBUFFERDESTOVERRIDE = 0x00200000
DDBLT_ZBUFFERSRCCONSTOVERRIDE = 0x00400000
DDBLT_ZBUFFERSRCOVERRIDE = 0x00800000
DDBLT_WAIT = 0x01000000
DDBLT_DEPTHFILL = 0x02000000
DDBLT_DONOTWAIT = 0x08000000
DDBLT_PRESENTATION = 0x10000000
DDBLT_LAST_PRESENTATION = 0x20000000
DDBLT_EXTENDED_FLAGS = 0x40000000
DDBLT_EXTENDED_LINEAR_CONTENT = 0x00000004
DDBLTFAST_NOCOLORKEY = 0x00000000
DDBLTFAST_SRCCOLORKEY = 0x00000001
DDBLTFAST_DESTCOLORKEY = 0x00000002
DDBLTFAST_WAIT = 0x00000010
DDBLTFAST_DONOTWAIT = 0x00000020
DDFLIP_WAIT = 0x00000001
DDFLIP_EVEN = 0x00000002
DDFLIP_ODD = 0x00000004
DDFLIP_NOVSYNC = 0x00000008
DDFLIP_INTERVAL2 = 0x02000000
DDFLIP_INTERVAL3 = 0x03000000
DDFLIP_INTERVAL4 = 0x04000000
DDFLIP_STEREO = 0x00000010
DDFLIP_DONOTWAIT = 0x00000020
DDOVER_ALPHADEST = 0x00000001
DDOVER_ALPHADESTCONSTOVERRIDE = 0x00000002
DDOVER_ALPHADESTNEG = 0x00000004
DDOVER_ALPHADESTSURFACEOVERRIDE = 0x00000008
DDOVER_ALPHAEDGEBLEND = 0x00000010
DDOVER_ALPHASRC = 0x00000020
DDOVER_ALPHASRCCONSTOVERRIDE = 0x00000040
DDOVER_ALPHASRCNEG = 0x00000080
DDOVER_ALPHASRCSURFACEOVERRIDE = 0x00000100
DDOVER_HIDE = 0x00000200
DDOVER_KEYDEST = 0x00000400
DDOVER_KEYDESTOVERRIDE = 0x00000800
DDOVER_KEYSRC = 0x00001000
DDOVER_KEYSRCOVERRIDE = 0x00002000
DDOVER_SHOW = 0x00004000
DDOVER_ADDDIRTYRECT = 0x00008000
DDOVER_REFRESHDIRTYRECTS = 0x00010000
DDOVER_REFRESHALL = 0x00020000
DDOVER_DDFX = 0x00080000
DDOVER_AUTOFLIP = 0x00100000
DDOVER_BOB = 0x00200000
DDOVER_OVERRIDEBOBWEAVE = 0x00400000
DDOVER_INTERLEAVED = 0x00800000
DDOVER_BOBHARDWARE = 0x01000000
DDOVER_ARGBSCALEFACTORS = 0x02000000
DDOVER_DEGRADEARGBSCALING = 0x04000000
DDSETSURFACEDESC_RECREATEDC = 0x00000000
DDSETSURFACEDESC_PRESERVEDC = 0x00000001
DDLOCK_SURFACEMEMORYPTR = 0x00000000
DDLOCK_WAIT = 0x00000001
DDLOCK_EVENT = 0x00000002
DDLOCK_READONLY = 0x00000010
DDLOCK_WRITEONLY = 0x00000020
DDLOCK_NOSYSLOCK = 0x00000800
DDLOCK_NOOVERWRITE = 0x00001000
DDLOCK_DISCARDCONTENTS = 0x00002000
DDLOCK_OKTOSWAP = 0x00002000
DDLOCK_DONOTWAIT = 0x00004000
DDLOCK_HASVOLUMETEXTUREBOXRECT = 0x00008000
DDLOCK_NODIRTYUPDATE = 0x00010000
DDBLTFX_ARITHSTRETCHY = 0x00000001
DDBLTFX_MIRRORLEFTRIGHT = 0x00000002
DDBLTFX_MIRRORUPDOWN = 0x00000004
DDBLTFX_NOTEARING = 0x00000008
DDBLTFX_ROTATE180 = 0x00000010
DDBLTFX_ROTATE270 = 0x00000020
DDBLTFX_ROTATE90 = 0x00000040
DDBLTFX_ZBUFFERRANGE = 0x00000080
DDBLTFX_ZBUFFERBASEDEST = 0x00000100
DDOVERFX_ARITHSTRETCHY = 0x00000001
DDOVERFX_MIRRORLEFTRIGHT = 0x00000002
DDOVERFX_MIRRORUPDOWN = 0x00000004
DDOVERFX_DEINTERLACE = 0x00000008
DDWAITVB_BLOCKBEGIN = 0x00000001
DDWAITVB_BLOCKBEGINEVENT = 0x00000002
DDWAITVB_BLOCKEND = 0x00000004
DDGFS_CANFLIP = 0x00000001
DDGFS_ISFLIPDONE = 0x00000002
DDGBS_CANBLT = 0x00000001
DDGBS_ISBLTDONE = 0x00000002
DDENUMOVERLAYZ_BACKTOFRONT = 0x00000000
DDENUMOVERLAYZ_FRONTTOBACK = 0x00000001
DDOVERZ_SENDTOFRONT = 0x00000000
DDOVERZ_SENDTOBACK = 0x00000001
DDOVERZ_MOVEFORWARD = 0x00000002
DDOVERZ_MOVEBACKWARD = 0x00000003
DDOVERZ_INSERTINFRONTOF = 0x00000004
DDOVERZ_INSERTINBACKOF = 0x00000005
DDSGR_CALIBRATE = 0x00000001
DDSMT_ISTESTREQUIRED = 0x00000001
DDEM_MODEPASSED = 0x00000001
DDEM_MODEFAILED = 0x00000002

DD_OK = S_OK
DD_FALSE = S_FALSE
DDENUMRET_CANCEL = 0x0
DDENUMRET_OK = 0x1
DDERR_ALREADYINITIALIZED = MAKE_DDHRESULT( 5 )
DDERR_CANNOTATTACHSURFACE = MAKE_DDHRESULT( 10 )
DDERR_CANNOTDETACHSURFACE = MAKE_DDHRESULT( 20 )
DDERR_CURRENTLYNOTAVAIL = MAKE_DDHRESULT( 40 )
DDERR_EXCEPTION = MAKE_DDHRESULT( 55 )
DDERR_GENERIC = E_FAIL
DDERR_HEIGHTALIGN = MAKE_DDHRESULT( 90 )
DDERR_INCOMPATIBLEPRIMARY = MAKE_DDHRESULT( 95 )
DDERR_INVALIDCAPS = MAKE_DDHRESULT( 100 )
DDERR_INVALIDCLIPLIST = MAKE_DDHRESULT( 110 )
DDERR_INVALIDMODE = MAKE_DDHRESULT( 120 )
DDERR_INVALIDOBJECT = MAKE_DDHRESULT( 130 )
DDERR_INVALIDPARAMS = E_INVALIDARG
DDERR_INVALIDPIXELFORMAT = MAKE_DDHRESULT( 145 )
DDERR_INVALIDRECT = MAKE_DDHRESULT( 150 )
DDERR_LOCKEDSURFACES = MAKE_DDHRESULT( 160 )
DDERR_NO3D = MAKE_DDHRESULT( 170 )
DDERR_NOALPHAHW = MAKE_DDHRESULT( 180 )
DDERR_NOSTEREOHARDWARE = MAKE_DDHRESULT( 181 )
DDERR_NOSURFACELEFT = MAKE_DDHRESULT( 182 )
DDERR_NOCLIPLIST = MAKE_DDHRESULT( 205 )
DDERR_NOCOLORCONVHW = MAKE_DDHRESULT( 210 )
DDERR_NOCOOPERATIVELEVELSET = MAKE_DDHRESULT( 212 )
DDERR_NOCOLORKEY = MAKE_DDHRESULT( 215 )
DDERR_NOCOLORKEYHW = MAKE_DDHRESULT( 220 )
DDERR_NODIRECTDRAWSUPPORT = MAKE_DDHRESULT( 222 )
DDERR_NOEXCLUSIVEMODE = MAKE_DDHRESULT( 225 )
DDERR_NOFLIPHW = MAKE_DDHRESULT( 230 )
DDERR_NOGDI = MAKE_DDHRESULT( 240 )
DDERR_NOMIRRORHW = MAKE_DDHRESULT( 250 )
DDERR_NOTFOUND = MAKE_DDHRESULT( 255 )
DDERR_NOOVERLAYHW = MAKE_DDHRESULT( 260 )
DDERR_OVERLAPPINGRECTS = MAKE_DDHRESULT( 270 )
DDERR_NORASTEROPHW = MAKE_DDHRESULT( 280 )
DDERR_NOROTATIONHW = MAKE_DDHRESULT( 290 )
DDERR_NOSTRETCHHW = MAKE_DDHRESULT( 310 )
DDERR_NOT4BITCOLOR = MAKE_DDHRESULT( 316 )
DDERR_NOT4BITCOLORINDEX = MAKE_DDHRESULT( 317 )
DDERR_NOT8BITCOLOR = MAKE_DDHRESULT( 320 )
DDERR_NOTEXTUREHW = MAKE_DDHRESULT( 330 )
DDERR_NOVSYNCHW = MAKE_DDHRESULT( 335 )
DDERR_NOZBUFFERHW = MAKE_DDHRESULT( 340 )
DDERR_NOZOVERLAYHW = MAKE_DDHRESULT( 350 )
DDERR_OUTOFCAPS = MAKE_DDHRESULT( 360 )
DDERR_OUTOFMEMORY = E_OUTOFMEMORY
DDERR_OUTOFVIDEOMEMORY = MAKE_DDHRESULT( 380 )
DDERR_OVERLAYCANTCLIP = MAKE_DDHRESULT( 382 )
DDERR_OVERLAYCOLORKEYONLYONEACTIVE = MAKE_DDHRESULT( 384 )
DDERR_PALETTEBUSY = MAKE_DDHRESULT( 387 )
DDERR_COLORKEYNOTSET = MAKE_DDHRESULT( 400 )
DDERR_SURFACEALREADYATTACHED = MAKE_DDHRESULT( 410 )
DDERR_SURFACEALREADYDEPENDENT = MAKE_DDHRESULT( 420 )
DDERR_SURFACEBUSY = MAKE_DDHRESULT( 430 )
DDERR_CANTLOCKSURFACE = MAKE_DDHRESULT( 435 )
DDERR_SURFACEISOBSCURED = MAKE_DDHRESULT( 440 )
DDERR_SURFACELOST = MAKE_DDHRESULT( 450 )
DDERR_SURFACENOTATTACHED = MAKE_DDHRESULT( 460 )
DDERR_TOOBIGHEIGHT = MAKE_DDHRESULT( 470 )
DDERR_TOOBIGSIZE = MAKE_DDHRESULT( 480 )
DDERR_TOOBIGWIDTH = MAKE_DDHRESULT( 490 )
DDERR_UNSUPPORTED = E_NOTIMPL
DDERR_UNSUPPORTEDFORMAT = MAKE_DDHRESULT( 510 )
DDERR_UNSUPPORTEDMASK = MAKE_DDHRESULT( 520 )
DDERR_INVALIDSTREAM = MAKE_DDHRESULT( 521 )
DDERR_VERTICALBLANKINPROGRESS = MAKE_DDHRESULT( 537 )
DDERR_WASSTILLDRAWING = MAKE_DDHRESULT( 540 )
DDERR_DDSCAPSCOMPLEXREQUIRED = MAKE_DDHRESULT( 542 )
DDERR_XALIGN = MAKE_DDHRESULT( 560 )
DDERR_INVALIDDIRECTDRAWGUID = MAKE_DDHRESULT( 561 )
DDERR_DIRECTDRAWALREADYCREATED = MAKE_DDHRESULT( 562 )
DDERR_NODIRECTDRAWHW = MAKE_DDHRESULT( 563 )
DDERR_PRIMARYSURFACEALREADYEXISTS = MAKE_DDHRESULT( 564 )
DDERR_NOEMULATION = MAKE_DDHRESULT( 565 )
DDERR_REGIONTOOSMALL = MAKE_DDHRESULT( 566 )
DDERR_CLIPPERISUSINGHWND = MAKE_DDHRESULT( 567 )
DDERR_NOCLIPPERATTACHED = MAKE_DDHRESULT( 568 )
DDERR_NOHWND = MAKE_DDHRESULT( 569 )
DDERR_HWNDSUBCLASSED = MAKE_DDHRESULT( 570 )
DDERR_HWNDALREADYSET = MAKE_DDHRESULT( 571 )
DDERR_NOPALETTEATTACHED = MAKE_DDHRESULT( 572 )
DDERR_NOPALETTEHW = MAKE_DDHRESULT( 573 )
DDERR_BLTFASTCANTCLIP = MAKE_DDHRESULT( 574 )
DDERR_NOBLTHW = MAKE_DDHRESULT( 575 )
DDERR_NODDROPSHW = MAKE_DDHRESULT( 576 )
DDERR_OVERLAYNOTVISIBLE = MAKE_DDHRESULT( 577 )
DDERR_NOOVERLAYDEST = MAKE_DDHRESULT( 578 )
DDERR_INVALIDPOSITION = MAKE_DDHRESULT( 579 )
DDERR_NOTAOVERLAYSURFACE = MAKE_DDHRESULT( 580 )
DDERR_EXCLUSIVEMODEALREADYSET = MAKE_DDHRESULT( 581 )
DDERR_NOTFLIPPABLE = MAKE_DDHRESULT( 582 )
DDERR_CANTDUPLICATE = MAKE_DDHRESULT( 583 )
DDERR_NOTLOCKED = MAKE_DDHRESULT( 584 )
DDERR_CANTCREATEDC = MAKE_DDHRESULT( 585 )
DDERR_NODC = MAKE_DDHRESULT( 586 )
DDERR_WRONGMODE = MAKE_DDHRESULT( 587 )
DDERR_IMPLICITLYCREATED = MAKE_DDHRESULT( 588 )
DDERR_NOTPALETTIZED = MAKE_DDHRESULT( 589 )
DDERR_UNSUPPORTEDMODE = MAKE_DDHRESULT( 590 )
DDERR_NOMIPMAPHW = MAKE_DDHRESULT( 591 )
DDERR_INVALIDSURFACETYPE = MAKE_DDHRESULT( 592 )
DDERR_NOOPTIMIZEHW = MAKE_DDHRESULT( 600 )
DDERR_NOTLOADED = MAKE_DDHRESULT( 601 )
DDERR_NOFOCUSWINDOW = MAKE_DDHRESULT( 602 )
DDERR_NOTONMIPMAPSUBLEVEL = MAKE_DDHRESULT( 603 )
DDERR_DCALREADYCREATED = MAKE_DDHRESULT( 620 )
DDERR_NONONLOCALVIDMEM = MAKE_DDHRESULT( 630 )
DDERR_CANTPAGELOCK = MAKE_DDHRESULT( 640 )
DDERR_CANTPAGEUNLOCK = MAKE_DDHRESULT( 660 )
DDERR_NOTPAGELOCKED = MAKE_DDHRESULT( 680 )
DDERR_MOREDATA = MAKE_DDHRESULT( 690 )
DDERR_EXPIRED = MAKE_DDHRESULT( 691 )
DDERR_TESTFINISHED = MAKE_DDHRESULT( 692 )
DDERR_NEWMODE = MAKE_DDHRESULT( 693 )
DDERR_D3DNOTINITIALIZED = MAKE_DDHRESULT( 694 )
DDERR_VIDEONOTACTIVE = MAKE_DDHRESULT( 695 )
DDERR_NOMONITORINFORMATION = MAKE_DDHRESULT( 696 )
DDERR_NODRIVERSUPPORT = MAKE_DDHRESULT( 697 )
DDERR_DEVICEDOESNTOWNSURFACE = MAKE_DDHRESULT( 699 )
DDERR_NOTINITIALIZED = CO_E_NOTINITIALIZED


IDirectDraw._methods_ = [
    STDMETHOD(
        VOID,
        'Compact',
        (),
    ),
    STDMETHOD(
        VOID,
        'CreateClipper',
        (DWORD, POINTER(LPDIRECTDRAWCLIPPER), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreatePalette',
        (DWORD, LPPALETTEENTRY, POINTER(LPDIRECTDRAWPALETTE), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreateSurface',
        (LPDDSURFACEDESC, POINTER(LPDIRECTDRAWSURFACE), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'DuplicateSurface',
        (LPDIRECTDRAWSURFACE, POINTER(LPDIRECTDRAWSURFACE))
    ),
    STDMETHOD(
        VOID,
        'EnumDisplayModes',
        (DWORD, LPDDSURFACEDESC, LPVOID, LPDDENUMMODESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'EnumSurfaces',
        (DWORD, LPDDSURFACEDESC, LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'FlipToGDISurface',
        (),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDCAPS, LPDDCAPS),
    ),
    STDMETHOD(
        VOID,
        'GetDisplayMode',
        (LPDDSURFACEDESC,),
    ),
    STDMETHOD(
        VOID,
        'GetFourCCCodes',
        (LPDWORD, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'GetGDISurface',
        (POINTER(LPDIRECTDRAWSURFACE),),
    ),
    STDMETHOD(
        VOID,
        'GetMonitorFrequency',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetScanLine',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetVerticalBlankStatus',
        (LPBOOL,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (POINTER(GUID),),
    ),
    STDMETHOD(
        VOID,
        'RestoreDisplayMode',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetCooperativeLevel',
        (HWND, DWORD),
    ),
    STDMETHOD(
        VOID,
        'SetDisplayMode',
        (DWORD, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'WaitForVerticalBlank',
        (DWORD, HANDLE),
    ),
]

IDirectDraw2._methods_ = [
    STDMETHOD(
        VOID,
        'Compact',
        (),
    ),
    STDMETHOD(
        VOID,
        'CreateClipper',
        (DWORD, POINTER(LPDIRECTDRAWCLIPPER), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreatePalette',
        (DWORD, LPPALETTEENTRY, POINTER(LPDIRECTDRAWPALETTE), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreateSurface',
        (LPDDSURFACEDESC2, POINTER(LPDIRECTDRAWSURFACE2), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'DuplicateSurface',
        (LPDIRECTDRAWSURFACE2, POINTER(LPDIRECTDRAWSURFACE2))
    ),
    STDMETHOD(
        VOID,
        'EnumDisplayModes',
        (DWORD, LPDDSURFACEDESC2, LPVOID, LPDDENUMMODESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'EnumSurfaces',
        (DWORD, LPDDSURFACEDESC2, LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'FlipToGDISurface',
        (),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDCAPS, LPDDCAPS),
    ),
    STDMETHOD(
        VOID,
        'GetDisplayMode',
        (LPDDSURFACEDESC2,),
    ),
    STDMETHOD(
        VOID,
        'GetFourCCCodes',
        (LPDWORD, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'GetGDISurface',
        (POINTER(LPDIRECTDRAWSURFACE2),),
    ),
    STDMETHOD(
        VOID,
        'GetMonitorFrequency',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetScanLine',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetVerticalBlankStatus',
        (LPBOOL,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (POINTER(GUID),),
    ),
    STDMETHOD(
        VOID,
        'RestoreDisplayMode',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetCooperativeLevel',
        (HWND, DWORD),
    ),
    STDMETHOD(
        VOID,
        'SetDisplayMode',
        (DWORD, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'WaitForVerticalBlank',
        (DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'GetAvailableVidMem',
        (LPDDSCAPS, LPDWORD, LPDWORD),
    ),
]

IDirectDraw4._methods_ = [
    STDMETHOD(
        VOID,
        'Compact',
        (),
    ),
    STDMETHOD(
        VOID,
        'CreateClipper',
        (DWORD, POINTER(LPDIRECTDRAWCLIPPER), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreatePalette',
        (DWORD, LPPALETTEENTRY, POINTER(LPDIRECTDRAWPALETTE), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreateSurface',
        (LPDDSURFACEDESC2, POINTER(LPDIRECTDRAWSURFACE4), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'DuplicateSurface',
        (LPDIRECTDRAWSURFACE4, POINTER(LPDIRECTDRAWSURFACE4))
    ),
    STDMETHOD(
        VOID,
        'EnumDisplayModes',
        (DWORD, LPDDSURFACEDESC2, LPVOID, LPDDENUMMODESCALLBACK2),
    ),
    STDMETHOD(
        VOID,
        'EnumSurfaces',
        (DWORD, LPDDSURFACEDESC2, LPVOID, LPDDENUMSURFACESCALLBACK2),
    ),
    STDMETHOD(
        VOID,
        'FlipToGDISurface',
        (),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDCAPS, LPDDCAPS),
    ),
    STDMETHOD(
        VOID,
        'GetDisplayMode',
        (LPDDSURFACEDESC2,),
    ),
    STDMETHOD(
        VOID,
        'GetFourCCCodes',
        (LPDWORD, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'GetGDISurface',
        (POINTER(LPDIRECTDRAWSURFACE4),),
    ),
    STDMETHOD(
        VOID,
        'GetMonitorFrequency',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetScanLine',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetVerticalBlankStatus',
        (LPBOOL,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (POINTER(GUID),),
    ),
    STDMETHOD(
        VOID,
        'RestoreDisplayMode',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetCooperativeLevel',
        (HWND, DWORD),
    ),
    STDMETHOD(
        VOID,
        'SetDisplayMode',
        (DWORD, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'WaitForVerticalBlank',
        (DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'GetAvailableVidMem',
        (LPDDSCAPS2, LPDWORD, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'GetSurfaceFromDC',
        (HDC, POINTER(LPDIRECTDRAWSURFACE4)),
    ),
    STDMETHOD(
        VOID,
        'RestoreAllSurfaces',
        (),
    ),
    STDMETHOD(
        VOID,
        'TestCooperativeLevel',
        (),
    ),
    STDMETHOD(
        VOID,
        'GetDeviceIdentifier',
        (LPDDDEVICEIDENTIFIER, DWORD),
    ),
]


IDirectDraw7._methods_ = [
    STDMETHOD(
        VOID,
        'Compact',
        (),
    ),
    STDMETHOD(
        VOID,
        'CreateClipper',
        (DWORD, POINTER(LPDIRECTDRAWCLIPPER), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreatePalette',
        (DWORD, LPPALETTEENTRY, POINTER(LPDIRECTDRAWPALETTE), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'CreateSurface',
        (LPDDSURFACEDESC2, POINTER(LPDIRECTDRAWSURFACE7), POINTER(comtypes.IUnknown)),
    ),
    STDMETHOD(
        VOID,
        'DuplicateSurface',
        (LPDIRECTDRAWSURFACE7, POINTER(LPDIRECTDRAWSURFACE7))
    ),
    STDMETHOD(
        VOID,
        'EnumDisplayModes',
        (DWORD, LPDDSURFACEDESC2, LPVOID, LPDDENUMMODESCALLBACK2),
    ),
    STDMETHOD(
        VOID,
        'EnumSurfaces',
        (DWORD, LPDDSURFACEDESC2, LPVOID, LPDDENUMSURFACESCALLBACK7),
    ),
    STDMETHOD(
        VOID,
        'FlipToGDISurface',
        (),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDCAPS, LPDDCAPS),
    ),
    STDMETHOD(
        VOID,
        'GetDisplayMode',
        (LPDDSURFACEDESC2,),
    ),
    STDMETHOD(
        VOID,
        'GetFourCCCodes',
        (LPDWORD, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'GetGDISurface',
        (POINTER(LPDIRECTDRAWSURFACE7),),
    ),
    STDMETHOD(
        VOID,
        'GetMonitorFrequency',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetScanLine',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetVerticalBlankStatus',
        (LPBOOL,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (POINTER(GUID),),
    ),
    STDMETHOD(
        VOID,
        'RestoreDisplayMode',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetCooperativeLevel',
        (HWND, DWORD),
    ),
    STDMETHOD(
        VOID,
        'SetDisplayMode',
        (DWORD, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'WaitForVerticalBlank',
        (DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'GetAvailableVidMem',
        (LPDDSCAPS2, LPDWORD, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'GetSurfaceFromDC',
        (HDC, POINTER(LPDIRECTDRAWSURFACE7)),
    ),
    STDMETHOD(
        VOID,
        'RestoreAllSurfaces',
        (),
    ),
    STDMETHOD(
        VOID,
        'TestCooperativeLevel',
        (),
    ),
    STDMETHOD(
        VOID,
        'GetDeviceIdentifier',
        (LPDDDEVICEIDENTIFIER2, DWORD),
    ),
    STDMETHOD(
        VOID,
        'StartModeTest',
        (LPSIZE, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'EvaluateMode',
        (DWORD, POINTER(DWORD)),
    ),
]

IDirectDrawPalette._methods_ = [
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetEntries',
        (DWORD, DWORD, DWORD, LPPALETTEENTRY),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (LPDIRECTDRAW, DWORD, LPPALETTEENTRY),
    ),
    STDMETHOD(
        VOID,
        'SetEntries',
        (DWORD, DWORD, DWORD ,LPPALETTEENTRY),
    ),
]



IDirectDrawClipper._methods_ = [
    STDMETHOD(
        VOID,
        'GetClipList',
        (LPRECT, LPRGNDATA, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'GetHWnd',
        (POINTER(HWND),),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (LPDIRECTDRAW, DWORD),
    ),
    STDMETHOD(
        VOID,
        'IsClipListChanged',
        (POINTER(BOOL),),
    ),
    STDMETHOD(
        VOID,
        'SetClipList',
        (LPRGNDATA, DWORD),
    ),
    STDMETHOD(
        VOID,
        'SetHWnd',
        (DWORD, HWND),
    ),
]


IDirectDrawSurface._methods_ = [
    STDMETHOD(
        VOID,
        'AddAttachedSurface',
        (LPDIRECTDRAWSURFACE,),
    ),
    STDMETHOD(
        VOID,
        'AddOverlayDirtyRect',
        (LPRECT,),
    ),
    STDMETHOD(
        VOID,
        'Blt',
        (LPRECT, LPDIRECTDRAWSURFACE, LPRECT, DWORD, LPDDBLTFX),
    ),
    STDMETHOD(
        VOID,
        'BltBatch',
        (LPDDBLTBATCH, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'BltFast',
        (DWORD, DWORD, LPDIRECTDRAWSURFACE, LPRECT, DWORD),
    ),
    STDMETHOD(
        VOID,
        'DeleteAttachedSurface',
        (DWORD,LPDIRECTDRAWSURFACE),
    ),
    STDMETHOD(
        VOID,
        'EnumAttachedSurfaces',
        (LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'EnumOverlayZOrders',
        (DWORD, LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'Flip',
        (LPDIRECTDRAWSURFACE, DWORD),
    ),
    STDMETHOD(
        VOID,
        'GetAttachedSurface',
        (LPDDSCAPS, POINTER(LPDIRECTDRAWSURFACE)),
    ),
    STDMETHOD(
        VOID,
        'GetBltStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDSCAPS,),
    ),
    STDMETHOD(
        VOID,
        'GetClipper',
        (POINTER(LPDIRECTDRAWCLIPPER),),
    ),
    STDMETHOD(
        VOID,
        'GetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'GetDC',
        (POINTER(HDC),),
    ),
    STDMETHOD(
        VOID,
        'GetFlipStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetOverlayPosition',
        (LPLONG, LPLONG),
    ),
    STDMETHOD(
        VOID,
        'GetPalette',
        (POINTER(LPDIRECTDRAWPALETTE),),
    ),
    STDMETHOD(
        VOID,
        'GetPixelFormat',
        (LPDDPIXELFORMAT,),
    ),
    STDMETHOD(
        VOID,
        'GetSurfaceDesc',
        (LPDDSURFACEDESC,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (LPDIRECTDRAW, LPDDSURFACEDESC),
    ),
    STDMETHOD(
        VOID,
        'IsLost',
        (),
    ),
    STDMETHOD(
        VOID,
        'Lock',
        (LPRECT, LPDDSURFACEDESC, DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'ReleaseDC',
        (HDC,),
    ),
    STDMETHOD(
        VOID,
        'Restore',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetClipper',
        (LPDIRECTDRAWCLIPPER,),
    ),
    STDMETHOD(
        VOID,
        'SetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'SetOverlayPosition',
        (LONG, LONG),
    ),
    STDMETHOD(
        VOID,
        'SetPalette',
        (LPDIRECTDRAWPALETTE,),
    ),
    STDMETHOD(
        VOID,
        'Unlock',
        (LPVOID,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlay',
        (LPRECT, LPDIRECTDRAWSURFACE, LPRECT, DWORD, LPDDOVERLAYFX),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayDisplay',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayZOrder',
        (DWORD, LPDIRECTDRAWSURFACE),
    ),
]


IDirectDrawSurface2._methods_ = [
    STDMETHOD(
        VOID,
        'AddAttachedSurface',
        (LPDIRECTDRAWSURFACE2,),
    ),
    STDMETHOD(
        VOID,
        'AddOverlayDirtyRect',
        (LPRECT,),
    ),
    STDMETHOD(
        VOID,
        'Blt',
        (LPRECT, LPDIRECTDRAWSURFACE2, LPRECT, DWORD, LPDDBLTFX),
    ),
    STDMETHOD(
        VOID,
        'BltBatch',
        (LPDDBLTBATCH, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'BltFast',
        (DWORD, DWORD, LPDIRECTDRAWSURFACE2, LPRECT, DWORD),
    ),
    STDMETHOD(
        VOID,
        'DeleteAttachedSurface',
        (DWORD, LPDIRECTDRAWSURFACE2),
    ),
    STDMETHOD(
        VOID,
        'EnumAttachedSurfaces',
        (LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'EnumOverlayZOrders',
        (DWORD, LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'Flip',
        (LPDIRECTDRAWSURFACE2, DWORD),
    ),
    STDMETHOD(
        VOID,
        'GetAttachedSurface',
        (LPDDSCAPS, POINTER(LPDIRECTDRAWSURFACE2)),
    ),
    STDMETHOD(
        VOID,
        'GetBltStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDSCAPS,),
    ),
    STDMETHOD(
        VOID,
        'GetClipper',
        (POINTER(LPDIRECTDRAWCLIPPER),),
    ),
    STDMETHOD(
        VOID,
        'GetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'GetDC',
        (POINTER(HDC),),
    ),
    STDMETHOD(
        VOID,
        'GetFlipStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetOverlayPosition',
        (LPLONG, LPLONG),
    ),
    STDMETHOD(
        VOID,
        'GetPalette',
        (POINTER(LPDIRECTDRAWPALETTE),),
    ),
    STDMETHOD(
        VOID,
        'GetPixelFormat',
        (LPDDPIXELFORMAT,),
    ),
    STDMETHOD(
        VOID,
        'GetSurfaceDesc',
        (LPDDSURFACEDESC,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (LPDIRECTDRAW, LPDDSURFACEDESC),
    ),
    STDMETHOD(
        VOID,
        'IsLost',
        (),
    ),
    STDMETHOD(
        VOID,
        'Lock',
        (LPRECT, LPDDSURFACEDESC, DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'ReleaseDC',
        (HDC,),
    ),
    STDMETHOD(
        VOID,
        'Restore',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetClipper',
        (LPDIRECTDRAWCLIPPER,),
    ),
    STDMETHOD(
        VOID,
        'SetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'SetOverlayPosition',
        (LONG, LONG),
    ),
    STDMETHOD(
        VOID,
        'SetPalette',
        (LPDIRECTDRAWPALETTE,),
    ),
    STDMETHOD(
        VOID,
        'Unlock',
        (LPVOID,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlay',
        (LPRECT, LPDIRECTDRAWSURFACE2, LPRECT, DWORD, LPDDOVERLAYFX),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayDisplay',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayZOrder',
        (DWORD, LPDIRECTDRAWSURFACE2),
    ),
    STDMETHOD(
        VOID,
        'GetDDInterface',
        (POINTER(LPVOID),),
    ),
    STDMETHOD(
        VOID,
        'PageLock',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'PageUnlock',
        (DWORD,),
    ),
]

IDirectDrawSurface3._methods_ = [
    STDMETHOD(
        VOID,
        'AddAttachedSurface',
        (LPDIRECTDRAWSURFACE3,),
    ),
    STDMETHOD(
        VOID,
        'AddOverlayDirtyRect',
        (LPRECT,),
    ),
    STDMETHOD(
        VOID,
        'Blt',
        (LPRECT, LPDIRECTDRAWSURFACE3, LPRECT, DWORD, LPDDBLTFX),
    ),
    STDMETHOD(
        VOID,
        'BltBatch',
        (LPDDBLTBATCH, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'BltFast',
        (DWORD, DWORD, LPDIRECTDRAWSURFACE3, LPRECT, DWORD),
    ),
    STDMETHOD(
        VOID,
        'DeleteAttachedSurface',
        (DWORD, LPDIRECTDRAWSURFACE3),
    ),
    STDMETHOD(
        VOID,
        'EnumAttachedSurfaces',
        (LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'EnumOverlayZOrders',
        (DWORD, LPVOID, LPDDENUMSURFACESCALLBACK),
    ),
    STDMETHOD(
        VOID,
        'Flip',
        (LPDIRECTDRAWSURFACE2, DWORD),
    ),
    STDMETHOD(
        VOID,
        'GetAttachedSurface',
        (LPDDSCAPS, POINTER(LPDIRECTDRAWSURFACE3)),
    ),
    STDMETHOD(
        VOID,
        'GetBltStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDSCAPS,),
    ),
    STDMETHOD(
        VOID,
        'GetClipper',
        (POINTER(LPDIRECTDRAWCLIPPER),),
    ),
    STDMETHOD(
        VOID,
        'GetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'GetDC',
        (POINTER(HDC),),
    ),
    STDMETHOD(
        VOID,
        'GetFlipStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetOverlayPosition',
        (LPLONG, LPLONG),
    ),
    STDMETHOD(
        VOID,
        'GetPalette',
        (POINTER(LPDIRECTDRAWPALETTE),),
    ),
    STDMETHOD(
        VOID,
        'GetPixelFormat',
        (LPDDPIXELFORMAT,),
    ),
    STDMETHOD(
        VOID,
        'GetSurfaceDesc',
        (LPDDSURFACEDESC,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (LPDIRECTDRAW, LPDDSURFACEDESC),
    ),
    STDMETHOD(
        VOID,
        'IsLost',
        (),
    ),
    STDMETHOD(
        VOID,
        'Lock',
        (LPRECT, LPDDSURFACEDESC, DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'ReleaseDC',
        (HDC,),
    ),
    STDMETHOD(
        VOID,
        'Restore',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetClipper',
        (LPDIRECTDRAWCLIPPER,),
    ),
    STDMETHOD(
        VOID,
        'SetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'SetOverlayPosition',
        (LONG, LONG),
    ),
    STDMETHOD(
        VOID,
        'SetPalette',
        (LPDIRECTDRAWPALETTE,),
    ),
    STDMETHOD(
        VOID,
        'Unlock',
        (LPVOID,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlay',
        (LPRECT, LPDIRECTDRAWSURFACE3, LPRECT, DWORD, LPDDOVERLAYFX),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayDisplay',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayZOrder',
        (DWORD, LPDIRECTDRAWSURFACE3),
    ),
    STDMETHOD(
        VOID,
        'GetDDInterface',
        (POINTER(LPVOID),),
    ),
    STDMETHOD(
        VOID,
        'PageLock',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'PageUnlock',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'SetSurfaceDesc',
        (LPDDSURFACEDESC, DWORD),
    ),
]

IDirectDrawSurface4._methods_ = [
    STDMETHOD(
        VOID,
        'AddAttachedSurface',
        (LPDIRECTDRAWSURFACE4,),
    ),
    STDMETHOD(
        VOID,
        'AddOverlayDirtyRect',
        (LPRECT,),
    ),
    STDMETHOD(
        VOID,
        'Blt',
        (LPRECT, LPDIRECTDRAWSURFACE4, LPRECT, DWORD, LPDDBLTFX),
    ),
    STDMETHOD(
        VOID,
        'BltBatch',
        (LPDDBLTBATCH, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'BltFast',
        (DWORD, DWORD, LPDIRECTDRAWSURFACE4, LPRECT, DWORD),
    ),
    STDMETHOD(
        VOID,
        'DeleteAttachedSurface',
        (DWORD, LPDIRECTDRAWSURFACE4),
    ),
    STDMETHOD(
        VOID,
        'EnumAttachedSurfaces',
        (LPVOID, LPDDENUMSURFACESCALLBACK2),
    ),
    STDMETHOD(
        VOID,
        'EnumOverlayZOrders',
        (DWORD, LPVOID, LPDDENUMSURFACESCALLBACK2),
    ),
    STDMETHOD(
        VOID,
        'Flip',
        (LPDIRECTDRAWSURFACE4, DWORD),
    ),
    STDMETHOD(
        VOID,
        'GetAttachedSurface',
        (LPDDSCAPS, POINTER(LPDIRECTDRAWSURFACE4)),
    ),
    STDMETHOD(
        VOID,
        'GetBltStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDSCAPS2,),
    ),
    STDMETHOD(
        VOID,
        'GetClipper',
        (POINTER(LPDIRECTDRAWCLIPPER),),
    ),
    STDMETHOD(
        VOID,
        'GetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'GetDC',
        (POINTER(HDC),),
    ),
    STDMETHOD(
        VOID,
        'GetFlipStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetOverlayPosition',
        (LPLONG, LPLONG),
    ),
    STDMETHOD(
        VOID,
        'GetPalette',
        (POINTER(LPDIRECTDRAWPALETTE),),
    ),
    STDMETHOD(
        VOID,
        'GetPixelFormat',
        (LPDDPIXELFORMAT,),
    ),
    STDMETHOD(
        VOID,
        'GetSurfaceDesc',
        (LPDDSURFACEDESC2,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (LPDIRECTDRAW, LPDDSURFACEDESC2),
    ),
    STDMETHOD(
        VOID,
        'IsLost',
        (),
    ),
    STDMETHOD(
        VOID,
        'Lock',
        (LPRECT, LPDDSURFACEDESC2, DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'ReleaseDC',
        (HDC,),
    ),
    STDMETHOD(
        VOID,
        'Restore',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetClipper',
        (LPDIRECTDRAWCLIPPER,),
    ),
    STDMETHOD(
        VOID,
        'SetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'SetOverlayPosition',
        (LONG, LONG),
    ),
    STDMETHOD(
        VOID,
        'SetPalette',
        (LPDIRECTDRAWPALETTE,),
    ),
    STDMETHOD(
        VOID,
        'Unlock',
        (LPVOID,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlay',
        (LPRECT, LPDIRECTDRAWSURFACE4, LPRECT, DWORD, LPDDOVERLAYFX),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayDisplay',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayZOrder',
        (DWORD, LPDIRECTDRAWSURFACE4),
    ),
    STDMETHOD(
        VOID,
        'GetDDInterface',
        (POINTER(LPVOID),),
    ),
    STDMETHOD(
        VOID,
        'PageLock',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'PageUnlock',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'SetSurfaceDesc',
        (LPDDSURFACEDESC2, DWORD),
    ),
    STDMETHOD(
        VOID,
        'SetPrivateData',
        (REFGUID, LPVOID, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'GetPrivateData',
        (REFGUID, LPVOID, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'FreePrivateData',
        (REFGUID,),
    ),
    STDMETHOD(
        VOID,
        'GetUniquenessValue',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'ChangeUniquenessValue',
        (),
    ),
]



IDirectDrawSurface7._methods_ = [
    STDMETHOD(
        VOID,
        'AddAttachedSurface',
        (LPDIRECTDRAWSURFACE7,),
    ),
    STDMETHOD(
        VOID,
        'AddOverlayDirtyRect',
        (LPRECT,),
    ),
    STDMETHOD(
        VOID,
        'Blt',
        (LPRECT, LPDIRECTDRAWSURFACE7, LPRECT, DWORD, LPDDBLTFX),
    ),
    STDMETHOD(
        VOID,
        'BltBatch',
        (LPDDBLTBATCH, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'BltFast',
        (DWORD, DWORD, LPDIRECTDRAWSURFACE7, LPRECT, DWORD),
    ),
    STDMETHOD(
        VOID,
        'DeleteAttachedSurface',
        (DWORD, LPDIRECTDRAWSURFACE7),
    ),
    STDMETHOD(
        VOID,
        'EnumAttachedSurfaces',
        (LPVOID, LPDDENUMSURFACESCALLBACK7),
    ),
    STDMETHOD(
        VOID,
        'EnumOverlayZOrders',
        (DWORD, LPVOID, LPDDENUMSURFACESCALLBACK7),
    ),
    STDMETHOD(
        VOID,
        'Flip',
        (LPDIRECTDRAWSURFACE7, DWORD),
    ),
    STDMETHOD(
        VOID,
        'GetAttachedSurface',
        (LPDDSCAPS, POINTER(LPDIRECTDRAWSURFACE7)),
    ),
    STDMETHOD(
        VOID,
        'GetBltStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetCaps',
        (LPDDSCAPS2,),
    ),
    STDMETHOD(
        VOID,
        'GetClipper',
        (POINTER(LPDIRECTDRAWCLIPPER),),
    ),
    STDMETHOD(
        VOID,
        'GetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'GetDC',
        (POINTER(HDC),),
    ),
    STDMETHOD(
        VOID,
        'GetFlipStatus',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetOverlayPosition',
        (LPLONG, LPLONG),
    ),
    STDMETHOD(
        VOID,
        'GetPalette',
        (POINTER(LPDIRECTDRAWPALETTE),),
    ),
    STDMETHOD(
        VOID,
        'GetPixelFormat',
        (LPDDPIXELFORMAT,),
    ),
    STDMETHOD(
        VOID,
        'GetSurfaceDesc',
        (LPDDSURFACEDESC2,),
    ),
    STDMETHOD(
        VOID,
        'Initialize',
        (LPDIRECTDRAW, LPDDSURFACEDESC2),
    ),
    STDMETHOD(
        VOID,
        'IsLost',
        (),
    ),
    STDMETHOD(
        VOID,
        'Lock',
        (LPRECT, LPDDSURFACEDESC2, DWORD, HANDLE),
    ),
    STDMETHOD(
        VOID,
        'ReleaseDC',
        (HDC,),
    ),
    STDMETHOD(
        VOID,
        'Restore',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetClipper',
        (LPDIRECTDRAWCLIPPER,),
    ),
    STDMETHOD(
        VOID,
        'SetColorKey',
        (DWORD, LPDDCOLORKEY),
    ),
    STDMETHOD(
        VOID,
        'SetOverlayPosition',
        (LONG, LONG),
    ),
    STDMETHOD(
        VOID,
        'SetPalette',
        (LPDIRECTDRAWPALETTE,),
    ),
    STDMETHOD(
        VOID,
        'Unlock',
        (LPVOID,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlay',
        (LPRECT, LPDIRECTDRAWSURFACE7, LPRECT, DWORD, LPDDOVERLAYFX),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayDisplay',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'UpdateOverlayZOrder',
        (DWORD, LPDIRECTDRAWSURFACE7),
    ),
    STDMETHOD(
        VOID,
        'GetDDInterface',
        (POINTER(LPVOID),),
    ),
    STDMETHOD(
        VOID,
        'PageLock',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'PageUnlock',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'SetSurfaceDesc',
        (LPDDSURFACEDESC2, DWORD),
    ),
    STDMETHOD(
        VOID,
        'SetPrivateData',
        (REFGUID, LPVOID, DWORD, DWORD),
    ),
    STDMETHOD(
        VOID,
        'GetPrivateData',
        (REFGUID, LPVOID, LPDWORD),
    ),
    STDMETHOD(
        VOID,
        'FreePrivateData',
        (REFGUID,),
    ),
    STDMETHOD(
        VOID,
        'GetUniquenessValue',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'ChangeUniquenessValue',
        (),
    ),
    STDMETHOD(
        VOID,
        'SetPriority',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetPriority',
        (LPDWORD,),
    ),
    STDMETHOD(
        VOID,
        'SetLOD',
        (DWORD,),
    ),
    STDMETHOD(
        VOID,
        'GetLOD',
        (LPDWORD,),
    ),
]

IDirectDrawColorControl._methods_ = [
    STDMETHOD(
        VOID,
        'GetColorControls',
        (LPDDCOLORCONTROL,),
    ),
    STDMETHOD(
        VOID,
        'SetColorControls',
        (LPDDCOLORCONTROL,),
    ),
]


IDirectDrawGammaControl._methods_ = [
    STDMETHOD(
        VOID,
        'GetGammaRamp',
        (LPDDGAMMARAMP,),
    ),
    STDMETHOD(
        VOID,
        'SetGammaRamp',
        (LPDDGAMMARAMP,),
    ),
]


__all__ = (
    'IDirectDraw', 'IDirectDraw2', 'IDirectDraw4', 'IDirectDraw7',
    'IDirectDrawColorControl', 'IDirectDrawGammaControl', 'IDirectDrawSurface',
    'IDirectDrawSurface2', 'IDirectDrawSurface3', 'IDirectDrawSurface4',
    'IDirectDrawSurface7', 'IDirectDrawClipper', 'DDSCAPS2_DISCARDBACKBUFFER',
    'IDirectDrawClipper_Release', 'DDPF_RGB',
    'IDirectDrawSurface7_GetPrivateData', 'IDirectDrawSurface4_Initialize',
    'IDirectDraw4_RestoreAllSurfaces', 'IDirectDrawSurface2_GetColorKey',
    'DDERR_OVERLAPPINGRECTS', 'IDirectDraw4_GetDeviceIdentifier', 'DDBD_4',
    'IDirectDrawSurface3_AddAttachedSurface', 'DDSCAPS3_AUTOGENMIPMAP',
    'IDirectDrawColorControl_QueryInterface', 'IDirectDrawSurface3_Lock',
    'IDirectDrawGammaControl_QueryInterface', 'DDSCAPS_ZBUFFER', 'DDBD_2',
    'IDirectDraw2_EnumDisplayModes', 'DDERR_VERTICALBLANKINPROGRESS', 'DD_OK',
    'IDirectDrawSurface7_SetPriority', 'IDirectDrawSurface3_GetSurfaceDesc',
    'DDBLT_ALPHADESTNEG', 'DDBLT_ZBUFFERDESTOVERRIDE', 'IDirectDraw7_GetCaps',
    'DDBLT_ALPHASRCCONSTOVERRIDE', 'DDFXCAPS_OVERLAYSHRINKXN', 'DDBD_8',
    'IDirectDrawSurface4_PageLock', 'IDirectDraw4_GetGDISurface', 'DDSD_FVF',
    'DDENUMSURFACES_CANBECREATED', 'IDirectDrawSurface3_Flip', 'DDBLT_ASYNC',
    'IDirectDraw7_EvaluateMode', 'IDirectDrawSurface4_SetClipper', 'DDBD_16',
    'DDLOCK_NOSYSLOCK', 'IDirectDrawPalette_QueryInterface', 'MAKE_DDHRESULT',
    'DDCAPS_ALIGNSIZEDEST', 'DDCAPS2_CERTIFIED', 'DDSCL_FPUPRESERVE',
    'IDirectDraw_RestoreDisplayMode', 'IDirectDrawSurface4_BltBatch',
    'DDBLT_ZBUFFERDESTCONSTOVERRIDE', 'IDirectDraw2_RestoreDisplayMode',
    'IDirectDrawSurface4_GetPixelFormat', 'DDERR_LOCKEDSURFACES', 'DDCAPS_3D',
    'IDirectDrawSurface7_FreePrivateData', 'IDirectDrawSurface4_GetClipper',
    'IDirectDrawSurface_AddOverlayDirtyRect', 'DDERR_NOSTRETCHHW', 'DDPF_YUV',
    'IDirectDraw_GetDisplayMode', 'IDirectDrawSurface4_DeleteAttachedSurface',
    'IDirectDraw_Compact', 'DDOVERFX_ARITHSTRETCHY', 'DDSCAPS_OPTIMIZED',
    'IDirectDraw_GetFourCCCodes', 'IDirectDrawSurface_GetPalette', 'DDBD_1',
    'IDirectDraw2_CreateSurface', 'IDirectDrawSurface7_BltBatch', 'DDOSD_ALL',
    'IDirectDrawSurface3_EnumOverlayZOrders', 'IDirectDraw_GetScanLine',
    'IDirectDrawSurface7_EnumOverlayZOrders', 'DDERR_GENERIC', 'DDSCL_NORMAL',
    'IDirectDraw2_Initialize', 'DDOVERZ_INSERTINBACKOF', 'DDERR_NOROTATIONHW',
    'IDirectDrawSurface4_SetSurfaceDesc', 'DDENUMSURFACES_NOMATCH', '_FACDD',
    'IDirectDrawSurface_EnumOverlayZOrders', 'IDirectDrawSurface4_BltFast',
    'IDirectDraw7_RestoreDisplayMode', 'DDBLT_LAST_PRESENTATION', 'DD_FALSE',
    'DDSCAPS2_D3DTEXTUREMANAGE', 'IDirectDrawSurface4_SetPrivateData',
    'DDSCAPS_PRIMARYSURFACE', 'DDSD_REFRESHRATE', 'DDCAPS_ALIGNBOUNDARYSRC',
    'IDirectDrawSurface7_ChangeUniquenessValue', 'DDOVERZ_SENDTOFRONT',
    'IDirectDrawSurface4_ChangeUniquenessValue', 'IDirectDrawSurface_Release',
    'IDirectDrawSurface3_ReleaseDC', 'IDirectDrawSurface2_GetPixelFormat',
    'IDirectDrawSurface7_GetClipper', 'IDirectDrawSurface2_GetClipper',
    'IDirectDraw2_GetVerticalBlankStatus', 'DDCKEYCAPS_SRCOVERLAYYUV',
    'IDirectDrawSurface7_GetSurfaceDesc', 'IDirectDraw7_GetFourCCCodes',
    'DDSCL_FULLSCREEN', 'IDirectDrawSurface_SetPalette', 'DDERR_NOVSYNCHW',
    'IDirectDraw2_AddRef', 'REGSTR_KEY_DDHW_DESCRIPTION', 'DDCAPS_ZOVERLAYS',
    'IDirectDraw4_GetVerticalBlankStatus', 'IDirectDraw7_GetAvailableVidMem',
    'IDirectDrawSurface3_SetSurfaceDesc', 'DDCAPS2_CANDROPZ16BIT', 'DDBD_32',
    'IDirectDraw_DuplicateSurface', 'DDOVER_ALPHASRCCONSTOVERRIDE', 'DDBD_24',
    'IDirectDrawSurface2_Lock', 'IDirectDraw4_GetScanLine', 'GET_WHQL_MONTH',
    'IDirectDrawClipper_GetClipList', 'IDirectDrawSurface7_Release', 'DDARGB',
    'IDirectDrawSurface2_SetPalette', 'IDirectDraw4_SetDisplayMode', 'DDRGBA',
    'IDirectDrawColorControl_Release', 'IDirectDrawSurface4_AddRef',
    'IDirectDrawSurface_Blt', 'IDirectDrawSurface3_AddOverlayDirtyRect',
    'DDSD_CKDESTOVERLAY', 'IDirectDrawSurface4_GetOverlayPosition', '_DDARGB',
    'IDirectDrawSurface3_BltBatch', 'IDirectDrawSurface7_GetPriority',
    'IDirectDrawSurface3_PageUnlock', 'IDirectDrawSurface4_FreePrivateData',
    'DDFXCAPS_BLTROTATION', 'IDirectDrawSurface7_AddOverlayDirtyRect',
    'DDCAPS2_SYSTONONLOCAL_AS_SYSTOLOCAL', 'DDOVER_HIDE',
    'IDirectDrawSurface7_BltFast', 'DDPCAPS_PRIMARYSURFACELEFT', 'DDBLT_WAIT',
    'IDirectDrawSurface4_Flip', 'DDSCAPS3_OPENSHAREDRESOURCE', 'DDCOLOR_HUE',
    'IDirectDrawSurface2_AddAttachedSurface', 'DDERR_CANTLOCKSURFACE',
    'DDFXCAPS_OVERLAYARITHSTRETCHY', 'IDirectDrawSurface_GetPixelFormat',
    'DDERR_INCOMPATIBLEPRIMARY', 'IDirectDraw_GetGDISurface', 'DDSCAPS_OWNDC',
    'DDERR_SURFACEISOBSCURED', 'IDirectDrawSurface4_EnumOverlayZOrders',
    'IDirectDrawGammaControl_AddRef', 'IDirectDrawSurface3_GetPalette',
    'DDSCL_SETFOCUSWINDOW', 'IDirectDraw7_SetDisplayMode', 'DDSCAPS_HWCODEC',
    'IDirectDrawSurface3_GetDC', 'IDirectDrawSurface_ReleaseDC', 'DDFLIP_ODD',
    'IDirectDraw7_AddRef', 'IDirectDrawSurface_UpdateOverlayZOrder',
    'DDSD_ALPHABITDEPTH', 'IDirectDrawSurface4_GetColorKey', 'DDSCAPS3_DMAP',
    'IDirectDrawSurface2_GetSurfaceDesc', 'DDCAPS2_CANBOBHARDWARE', 'DDBLTFX',
    'DDERR_CANNOTATTACHSURFACE', 'DDERR_NODIRECTDRAWHW', 'DDSCL_ALLOWREBOOT',
    'DDSCAPS2_CUBEMAP_NEGATIVEX', 'DDSCAPS2_CUBEMAP_NEGATIVEY', 'DDOVER_DDFX',
    'DDSCAPS2_RESERVED1', 'IDirectDraw2_GetMonitorFrequency', 'GET_WHQL_DAY',
    'IDirectDrawSurface_GetCaps', 'DDOSDCAPS_MONOLITHICMIPMAP', 'DDFLIP_EVEN',
    'DDSCL_EXCLUSIVE', 'IDirectDrawSurface2_Blt', 'DDENUMSURFACES_DOESEXIST',
    'IDirectDrawSurface2_DeleteAttachedSurface', 'DDSCAPS3_LIGHTWEIGHTMIPMAP',
    'IDirectDraw4_SetCooperativeLevel', 'IDirectDraw4_WaitForVerticalBlank',
    'IDirectDraw_GetVerticalBlankStatus', 'DDERR_TOOBIGHEIGHT', 'DDERR_NOGDI',
    'IDirectDraw7_GetMonitorFrequency', 'DDFXCAPS_BLTALPHA', 'DDCAPS_ALPHA',
    'IDirectDrawSurface2_GetBltStatus', 'IDirectDraw7_Release', 'DDOSD_GUID',
    'IDirectDrawSurface2_Release', 'DDERR_NOCOOPERATIVELEVELSET', 'DDSD_CAPS',
    'IDirectDrawSurface3_DeleteAttachedSurface', 'IDirectDraw7_CreateClipper',
    'DDCKEYCAPS_DESTOVERLAYONEACTIVE', 'IDirectDrawSurface2_GetCaps',
    'IDirectDrawSurface_BltBatch', 'IDirectDrawSurface_BltFast', 'DDSD_DEPTH',
    'IDirectDrawSurface2_SetClipper', 'IDirectDrawSurface4_GetBltStatus',
    'IDirectDrawSurface7_GetDDInterface', 'IDirectDraw7_GetSurfaceFromDC',
    'IDirectDrawSurface3_GetFlipStatus', 'IDirectDraw4_QueryInterface',
    'DDFXALPHACAPS_BLTALPHAEDGEBLEND', 'DDERR_INVALIDCLIPLIST', 'DDPF_ALPHA',
    'IDirectDrawSurface3_GetPixelFormat', 'DDERR_OUTOFMEMORY', 'DDBLT_KEYSRC',
    'IDirectDrawGammaControl_GetGammaRamp', 'DDERR_CANTPAGELOCK', 'DDBLT_ROP',
    'IDirectDrawSurface7_GetFlipStatus', 'DDERR_NODIRECTDRAWSUPPORT',
    'IDirectDraw4_GetMonitorFrequency', 'IDirectDrawClipper_GetHWnd',
    'IDirectDrawSurface4_Lock', 'DDCOLOR_CONTRAST', 'DDCAPS_COLORKEY',
    'IDirectDrawSurface7_Initialize', 'IDirectDrawSurface_QueryInterface',
    'DDCKEYCAPS_SRCBLTCLRSPACE', 'IDirectDrawSurface4_QueryInterface',
    'IDirectDrawSurface3_GetBltStatus', 'DDERR_OVERLAYNOTVISIBLE',
    'DDCAPS2_COLORCONTROLOVERLAY', 'DDERR_SURFACEALREADYATTACHED', 'DDSD_ALL',
    'DDFXCAPS_BLTARITHSTRETCHY', 'DDERR_WASSTILLDRAWING', 'DDSCAPS_3DDEVICE',
    'IDirectDrawSurface2_GetFlipStatus', 'IDirectDrawSurface3_BltFast',
    'DDENUMOVERLAYZ_FRONTTOBACK', 'IDirectDraw7_GetDisplayMode', 'DDSD_WIDTH',
    'IDirectDraw2_GetAvailableVidMem', 'IDirectDrawSurface_UpdateOverlay',
    'IDirectDraw7_EnumDisplayModes', 'IDirectDrawGammaControl_Release',
    'IDirectDrawSurface3_GetDDInterface', 'IDirectDraw7_GetDeviceIdentifier',
    'DDSCAPS_BACKBUFFER', 'IDirectDrawSurface4_UpdateOverlayDisplay',
    'DDERR_TESTFINISHED', 'DDENUMOVERLAYZ_BACKTOFRONT', 'DDSVCAPS_RESERVED3',
    'IDirectDraw_EnumDisplayModes', 'IDirectDrawSurface2_AddRef',
    'IDirectDraw2_FlipToGDISurface', 'DDERR_CANTPAGEUNLOCK', 'DDERR_NOTFOUND',
    'IDirectDrawSurface4_GetAttachedSurface', 'DDSCL_SETDEVICEWINDOW',
    'IDirectDrawSurface2_GetPalette', 'DDPF_STENCILBUFFER', 'DDLOCK_READONLY',
    'IDirectDrawSurface4_SetPalette', 'DDENUM_DETACHEDSECONDARYDEVICES',
    'DDOSDCAPS_VALIDSCAPS', 'IDirectDrawSurface_GetSurfaceDesc', 'DDERR_NO3D',
    'IDirectDrawSurface7_PageUnlock', 'DDFXCAPS_BLTFILTER', 'DDOVER_ALPHASRC',
    'IDirectDraw7_EnumSurfaces', 'DDCKEYCAPS_SRCBLT', 'DDCKEY_SRCOVERLAY',
    'DDOSDCAPS_OPTREORDERED', 'DDFXCAPS_BLTROTATION90', 'DDSCL_MULTITHREADED',
    'DDERR_REGIONTOOSMALL', 'DDERR_INVALIDSTREAM', 'DDERR_INVALIDPARAMS',
    'IDirectDrawSurface3_SetClipper', 'DDERR_UNSUPPORTED', 'DDERR_NOCLIPLIST',
    'IDirectDraw4_GetCaps', 'IDirectDraw2_WaitForVerticalBlank', 'DDCAPS_GDI',
    'IDirectDrawSurface2_Restore', 'DDCAPS_OVERLAYSTRETCH', 'DDBLT_ZBUFFER',
    'IDirectDraw4_TestCooperativeLevel', 'DDERR_NOTPAGELOCKED', 'DDOSD_SCAPS',
    'DDCAPS_BLTDEPTHFILL', 'DDSD_TEXTURESTAGE', 'DDOVER_OVERRIDEBOBWEAVE',
    'IDirectDrawSurface4_GetDDInterface', 'DDERR_HWNDALREADYSET', 'DDSCAPSEX',
    'IDirectDrawSurface2_GetDC', 'DDCAPS2_CANMANAGERESOURCE', 'DD_ROP_SPACE',
    'IDirectDrawSurface7_Flip', 'IDirectDrawSurface4_GetUniquenessValue',
    'DDERR_NOOPTIMIZEHW', 'IDirectDrawSurface2_GetDDInterface', 'FOURCC_DXT4',
    'DDCAPS2_FLIPINTERVAL', 'DDCAPS2_NONLOCALVIDMEM', 'DDSMT_ISTESTREQUIRED',
    'IDirectDrawSurface7_UpdateOverlayDisplay', 'DDERR_NOCLIPPERATTACHED',
    'IDirectDrawSurface7_SetOverlayPosition', 'DDERR_UNSUPPORTEDMODE',
    'DDBLT_ALPHAEDGEBLEND', 'IDirectDrawSurface2_IsLost', 'DDSCL_ALLOWMODEX',
    'IDirectDrawSurface7_QueryInterface', 'IDirectDrawSurface3_SetPalette',
    'DDCOLOR_SATURATION', 'IDirectDrawSurface7_SetPrivateData', 'FOURCC_DXT5',
    'IDirectDrawSurface3_QueryInterface', 'DDSCAPS2_POINTS', 'DDPCAPS_1BIT',
    'IDirectDrawSurface3_UpdateOverlayZOrder', 'DDERR_NODDROPSHW', '_DDBLTFX',
    'IDirectDraw4_FlipToGDISurface', 'IDirectDrawSurface_AddAttachedSurface',
    'IDirectDrawSurface4_EnumAttachedSurfaces', 'IDirectDraw7_CreateSurface',
    'IDirectDrawSurface3_AddRef', 'DDBLT_DEPTHFILL', 'DDERR_CANTDUPLICATE',
    'IDirectDraw_SetCooperativeLevel', 'DDSD_LINEARSIZE', 'DDSD_PIXELFORMAT',
    'DDSD_CKSRCBLT', 'IDirectDrawSurface7_DeleteAttachedSurface', '_DDRGBA',
    'DDCAPS2_COLORCONTROLPRIMARY', 'DDSCAPS2_VOLUME', 'DDBLT_ALPHASRC',
    'REGSTR_PATH_DDHW', 'IDirectDrawSurface4_SetColorKey', 'DDERR_NOFLIPHW',
    'IDirectDrawSurface_GetFlipStatus', 'IDirectDrawSurface7_UpdateOverlay',
    'IDirectDrawSurface2_PageUnlock', 'DDFXCAPS_BLTSTRETCHY', 'DDCKEY_SRCBLT',
    'DDFXCAPS_BLTSTRETCHX', 'DDOVERZ_MOVEFORWARD', 'DDBLT_DONOTWAIT',
    'DDCKEYCAPS_DESTOVERLAYCLRSPACE', 'DDCAPS2_CANSHARERESOURCE', 'DDSCAPS2',
    'IDirectDrawSurface2_GetOverlayPosition', 'IDirectDrawSurface7_Unlock',
    'IDirectDrawSurface3_GetColorKey', 'DDFXALPHACAPS_BLTALPHAPIXELSNEG',
    'DDERR_SURFACENOTATTACHED', 'IDirectDraw_Initialize', 'DDSCAPS_WRITEONLY',
    'IDirectDrawClipper_IsClipListChanged', 'IDirectDrawColorControl_AddRef',
    'DDPF_PALETTEINDEXED8', 'DDERR_NOCOLORKEYHW', 'DDBLT_ROTATIONANGLE',
    'IDirectDrawClipper_SetHWnd', 'DDSGR_CALIBRATE', 'DDERR_TOOBIGSIZE',
    'IDirectDraw7_QueryInterface', 'DDSCAPS2_CUBEMAP_POSITIVEX', 'DDBLT_DDFX',
    'DDSCAPS2_CUBEMAP_POSITIVEY', 'DDSCAPS2_CUBEMAP_POSITIVEZ', 'FOURCC_DXT2',
    'IDirectDrawSurface7_AddRef', 'IDirectDrawSurface7_Blt', 'DDPCAPS_8BIT',
    'DDFXALPHACAPS_BLTALPHAPIXELS', 'IDirectDrawSurface_GetColorKey',
    'IDirectDrawSurface4_ReleaseDC', 'DDERR_NOOVERLAYDEST', 'DDBLT_COLORFILL',
    'DDSD_MIPMAPCOUNT', 'DDOSD_COMPRESSION_RATIO', 'DDSCAPS_LIVEVIDEO',
    'IDirectDrawSurface2_BltBatch', 'DDCKEYCAPS_SRCOVERLAYCLRSPACE',
    'DDLOCK_SURFACEMEMORYPTR', 'DDERR_IMPLICITLYCREATED', 'DDSCAPS_PALETTE',
    'IDirectDrawSurface2_BltFast', 'DDCAPS_ALIGNSIZESRC', 'DDERR_SURFACEBUSY',
    'DDCAPS2_WIDESURFACES', 'IDirectDrawSurface4_GetPrivateData', '_DDSCAPS',
    'DDCKEYCAPS_DESTBLTYUV', 'DDCKEYCAPS_DESTBLTCLRSPACEYUV', 'DDPCAPS_4BIT',
    'DDSCAPS2_HINTSTATIC', 'DDOVERFX_DEINTERLACE', 'DDFXCAPS_OVERLAYSTRETCHX',
    'IDirectDrawColorControl_SetColorControls', 'IDirectDrawSurface3_GetCaps',
    'IDirectDrawSurface_GetClipper', 'DDSCAPS2_ENABLEALPHACHANNEL', 'DDSCAPS',
    'IDirectDrawSurface7_ReleaseDC', 'IDirectDraw2_Release', 'DDFLIP_NOVSYNC',
    'IDirectDrawSurface4_AddAttachedSurface', 'DDPCAPS_PRIMARYSURFACE',
    'DDENUMSURFACES_ALL', 'IDirectDrawSurface_GetBltStatus', 'DDGBS_CANBLT',
    'IDirectDrawSurface3_SetOverlayPosition', 'DDSCAPS_LOCALVIDMEM',
    'DDFXCAPS_BLTSHRINKXN', 'DDBLTFX_ZBUFFERBASEDEST', 'IDirectDraw2_Compact',
    'IDirectDraw2_GetDisplayMode', 'DDCAPS_CANCLIPSTRETCHED', 'DDERR_EXPIRED',
    'IDirectDraw2_SetCooperativeLevel', 'IDirectDraw7_FlipToGDISurface',
    'IDirectDraw7_Initialize', 'DDOVER_KEYDESTOVERRIDE', 'DDERR_NOOVERLAYHW',
    'IDirectDrawGammaControl_SetGammaRamp', 'DDOVER_ALPHADESTSURFACEOVERRIDE',
    'IDirectDrawPalette_GetCaps', 'IDirectDrawSurface7_GetOverlayPosition',
    'IDirectDraw2_CreateClipper', 'DDCREATE_HARDWAREONLY', 'DDFLIP_DONOTWAIT',
    'IDirectDrawSurface2_Initialize', 'DDBLTFAST_NOCOLORKEY', 'DDPF_ZPIXELS',
    'IDirectDrawSurface4_GetDC', 'IDirectDrawSurface_Lock', 'DDCAPS_CANCLIP',
    'DDOVER_ADDDIRTYRECT', 'IDirectDrawSurface7_GetAttachedSurface',
    'IDirectDrawSurface4_AddOverlayDirtyRect', 'IDirectDraw2_GetCaps',
    'DDCAPS2_CANBOBNONINTERLEAVED', 'IDirectDrawSurface7_GetCaps', 'DDOSCAPS',
    'DDERR_SURFACELOST', 'DDERR_INVALIDPOSITION', 'DDERR_CANTCREATEDC',
    'IDirectDrawPalette_GetEntries', 'IDirectDraw_SetDisplayMode', 'LPVOID',
    'IDirectDrawSurface2_UpdateOverlayDisplay', 'DDCAPS_PALETTEVSYNC',
    'IDirectDraw_CreateClipper', 'REGSTR_KEY_DDHW_DRIVERNAME', 'FOURCC_DXT3',
    'DDFXALPHACAPS_OVERLAYALPHAEDGEBLEND', 'DDPF_PALETTEINDEXEDTO8',
    'DDERR_ALREADYINITIALIZED', 'DDPF_ALPHAPREMULT', 'DDBLTFX_MIRRORUPDOWN',
    'DDERR_D3DNOTINITIALIZED', 'IDirectDraw4_GetAvailableVidMem', '_DDOSCAPS',
    'IDirectDrawSurface2_Unlock', 'IDirectDraw4_Release', 'DDERR_INVALIDMODE',
    'IDirectDrawSurface_UpdateOverlayDisplay', 'IDirectDraw_AddRef',
    'DDERR_NOT8BITCOLOR', 'IDirectDraw7_TestCooperativeLevel', 'DDFLIP_WAIT',
    'DDBLT_ZBUFFERSRCOVERRIDE', 'DDOVER_ALPHASRCSURFACEOVERRIDE', '_DDSCAPS2',
    'DDBLTFAST_DESTCOLORKEY', 'DDCREATE_EMULATIONONLY', 'DDCKEYCAPS_DESTBLT',
    'DDSCAPS2_DONOTPERSIST', 'IDirectDraw4_EnumDisplayModes', 'DDPCAPS_VSYNC',
    'DDSD_BACKBUFFERCOUNT', 'DDSVCAPS_RESERVED4', 'DDCAPS_BLTFOURCC',
    'IDirectDrawSurface4_UpdateOverlay', 'DDSPD_VOLATILE', 'DDSCAPS_MIPMAP',
    'IDirectDrawSurface4_SetOverlayPosition', 'IDirectDraw7_GetScanLine',
    'IDirectDrawSurface3_GetAttachedSurface', 'IDirectDrawSurface3_IsLost',
    'IDirectDrawSurface7_GetPixelFormat', 'IDirectDraw4_CreateSurface',
    'DDSCAPS2_MIPMAPSUBLEVEL', 'IDirectDrawSurface7_PageLock', 'DDCAPS_BLT',
    'IDirectDrawSurface_Unlock', 'DDOVERZ_MOVEBACKWARD', 'DDOVER_ALPHASRCNEG',
    'IDirectDrawClipper_SetClipList', 'DDERR_NOTONMIPMAPSUBLEVEL', 'LPDDARGB',
    'IDirectDrawSurface_EnumAttachedSurfaces', 'IDirectDraw2_SetDisplayMode',
    'IDirectDraw2_EnumSurfaces', 'IDirectDrawSurface7_Lock', 'DDCAPS_OVERLAY',
    'DDBLT_ALPHADESTSURFACEOVERRIDE', 'IDirectDrawSurface_GetOverlayPosition',
    'DDENUMRET_CANCEL', 'IDirectDraw7_SetCooperativeLevel', 'DDEM_MODEPASSED',
    'DDERR_INVALIDDIRECTDRAWGUID', 'IDirectDrawSurface7_SetSurfaceDesc',
    'IDirectDrawSurface7_GetUniquenessValue', 'IDirectDraw4_DuplicateSurface',
    'DDFXALPHACAPS_BLTALPHASURFACES', 'IDirectDrawSurface_SetClipper',
    'DDFXCAPS_OVERLAYDEINTERLACE', 'DDSCAPS3_MULTISAMPLE_QUALITY_MASK',
    'IDirectDrawSurface7_UpdateOverlayZOrder', 'IDirectDraw7_StartModeTest',
    'DDLOCK_WRITEONLY', 'IDirectDrawSurface2_EnumAttachedSurfaces',
    'DDERR_PALETTEBUSY', 'IDirectDrawSurface2_PageLock', 'DDBLTFX_ROTATE270',
    'IDirectDraw_GetMonitorFrequency', 'IDirectDrawSurface_AddRef',
    'IDirectDrawPalette_Release', 'IDirectDrawSurface4_GetCaps', 'DDERR_NODC',
    'DDBLTFX_ARITHSTRETCHY', 'DDCAPS_BANKSWITCHED', 'IDirectDraw_Release',
    'IDirectDraw4_CreateClipper', 'IDirectDrawSurface4_GetPalette',
    'DDFXCAPS_OVERLAYALPHA', 'IDirectDrawSurface_Initialize', 'DDFLIP_STEREO',
    'DDEM_MODEFAILED', 'IDirectDraw4_EnumSurfaces', 'DDCAPS_BLTCOLORFILL',
    'IDirectDrawSurface3_GetOverlayPosition', 'DDCAPS2_NONLOCALVIDMEMCAPS',
    'DDCAPS2_TEXMANINNONLOCALVIDMEM', 'DDCKEYCAPS_SRCOVERLAYCLRSPACEYUV',
    'DDFXCAPS_BLTMIRRORLEFTRIGHT', 'DDSCAPS2_ADDITIONALPRIMARY', 'DDSD_PITCH',
    'DDSCAPS3_READONLYRESOURCE', 'IDirectDrawSurface7_GetDC', 'DDBLT_KEYDEST',
    'DDCAPS_OVERLAYFOURCC', 'IDirectDrawSurface_GetDC', 'DDCKEY_DESTBLT',
    'IDirectDrawSurface_Restore', 'DDSETSURFACEDESC_RECREATEDC', 'DDCAPS_VBI',
    'DDERR_NOPALETTEATTACHED', 'DDFXCAPS_OVERLAYSHRINKX', 'DDBLTFX_ROTATE90',
    'IDirectDrawSurface4_IsLost', 'DDSCAPS2_RESERVED4', 'DDSCAPS2_RESERVED3',
    'DDSDM_STANDARDVGAMODE', 'IDirectDraw_CreatePalette', 'DDCAPS_PALETTE',
    'DDSCAPS2_RESERVED2', 'DDSCAPS_NONLOCALVIDMEM', 'DDPF_PALETTEINDEXED2',
    'IDirectDraw7_GetGDISurface', 'DDERR_NOSTEREOHARDWARE', 'DDERR_EXCEPTION',
    'DDOVER_ALPHAEDGEBLEND', 'IDirectDrawPalette_SetEntries', 'DDSD_HEIGHT',
    'DDPF_PALETTEINDEXED4', 'IDirectDrawSurface3_UpdateOverlay', 'DDOVER_BOB',
    'DDPF_PALETTEINDEXED1', 'DDSCAPS3_RESERVED1', 'DDSCAPS3_RESERVED2',
    'IDirectDrawSurface4_Unlock', 'IDirectDrawSurface3_GetClipper',
    'DDOVER_ALPHADEST', 'DDOVERFX_MIRRORLEFTRIGHT', 'DDSCAPS2_RTPATCHES',
    'DDSCAPS_VIDEOPORT', 'IDirectDrawSurface2_SetOverlayPosition', 'LPDDRGBA',
    'IDirectDrawSurface2_SetColorKey', 'DDBLT_ALPHADESTCONSTOVERRIDE',
    'DDCOLOR_SHARPNESS', 'IDirectDrawSurface3_Initialize', 'DDGFS_ISFLIPDONE',
    'IDirectDraw7_GetVerticalBlankStatus', 'DDBLTFAST_SRCCOLORKEY',
    'DDSCAPS2_OPAQUE', 'IDirectDrawSurface3_Unlock', 'DDERR_NOMIPMAPHW',
    'IDirectDrawSurface2_QueryInterface', 'DDCAPS2_NOPAGELOCKREQUIRED',
    'DDCAPS2_AUTOFLIPOVERLAY', 'IDirectDraw4_GetFourCCCodes', 'DDPF_BUMPDUDV',
    'IDirectDrawSurface2_UpdateOverlay', 'DDBLTFAST_WAIT', 'DDOVER_KEYDEST',
    'IDirectDrawSurface_GetAttachedSurface', 'IDirectDrawSurface7_SetLOD',
    'DDCKEYCAPS_DESTOVERLAY', 'DDCAPS2_NO2DDURING3DSCENE', 'DDSCAPS2_CUBEMAP',
    'IDirectDraw4_RestoreDisplayMode', 'DDOVERZ_SENDTOBACK', 'DDPF_FOURCC',
    'IDirectDraw4_GetSurfaceFromDC', 'IDirectDrawClipper_AddRef', 'LPDDFXROP',
    'IDirectDrawSurface3_Release', 'DDWAITVB_BLOCKBEGIN', 'DDSCAPS_OVERLAY',
    'IDirectDrawSurface7_GetColorKey', 'IDirectDrawSurface4_GetFlipStatus',
    'IDirectDraw4_Initialize', 'IDirectDrawSurface_SetOverlayPosition',
    'DDBLT_KEYSRCOVERRIDE', 'DDERR_NOZOVERLAYHW', 'DDBLT_PRESENTATION',
    'IDirectDraw2_DuplicateSurface', 'IDirectDraw4_CreatePalette', 'LPDDCAPS',
    'DDSCAPS2_HINTANTIALIASING', 'DDPCAPS_8BITENTRIES', 'IDirectDraw4_AddRef',
    'MAX_DDDEVICEID_STRING', 'IDirectDraw7_WaitForVerticalBlank', 'LPDDSCAPS',
    'DDSPD_IUNKNOWNPOINTER', 'IDirectDrawSurface4_GetSurfaceDesc',
    'DDERR_NOSURFACELEFT', 'DDERR_HEIGHTALIGN', 'DDPCAPS_INITIALIZE',
    'DDENUM_ATTACHEDSECONDARYDEVICES', 'DDSCAPS_PRIMARYSURFACELEFT',
    'IDirectDrawPalette_Initialize', 'DDFXCAPS_OVERLAYSTRETCHYN', 'LPDDBLTFX',
    'DDSCAPS_SYSTEMMEMORY', 'IDirectDrawSurface3_UpdateOverlayDisplay',
    'IDirectDraw2_GetFourCCCodes', 'DDERR_NOTFLIPPABLE', 'DDERR_NOZBUFFERHW',
    'IDirectDrawSurface_Flip', 'IDirectDraw7_CreatePalette', 'DDLOCK_EVENT',
    'DDCAPS_BLTQUEUE', 'DDERR_NOTINITIALIZED', 'DDWAITVB_BLOCKBEGINEVENT',
    'DDCAPS_OVERLAYCANTCLIP', 'DDERR_OVERLAYCOLORKEYONLYONEACTIVE',
    'DDERR_INVALIDPIXELFORMAT', 'IDirectDrawSurface3_PageLock', 'FOURCC_DXT1',
    'DDBLT_ALPHASRCSURFACEOVERRIDE', 'IDirectDraw_EnumSurfaces', '_DDSCAPSEX',
    'IDirectDrawSurface2_GetAttachedSurface', 'DDOVER_ALPHADESTNEG',
    'IDirectDraw2_GetScanLine', 'IDirectDrawSurface7_IsLost', 'DDERR_XALIGN',
    'DDSCAPS_VISIBLE', 'IDirectDraw_FlipToGDISurface', 'DDERR_NOMIRRORHW',
    'IDirectDrawSurface7_GetBltStatus', 'IDirectDrawSurface2_Flip',
    'DDBLT_EXTENDED_LINEAR_CONTENT', 'IDirectDraw_GetCaps', 'DDERR_NEWMODE',
    'DDERR_INVALIDOBJECT', 'IDirectDrawSurface7_GetPalette', 'DDPF_ZBUFFER',
    'DDCAPS2_CANCALIBRATEGAMMA', 'DDFXALPHACAPS_OVERLAYALPHASURFACESNEG',
    'DDERR_NOEXCLUSIVEMODE', 'DDERR_NOT4BITCOLOR', 'DDOVER_ARGBSCALEFACTORS',
    'IDirectDrawSurface7_EnumAttachedSurfaces', 'DIRECTDRAW_VERSION',
    'IDirectDrawSurface7_SetPalette', 'DDBLTFX_MIRRORLEFTRIGHT', 'DDBLTBATCH',
    'IDirectDrawColorControl_GetColorControls', 'DDSCAPS2_NOTUSERLOCKABLE',
    'DDERR_UNSUPPORTEDMASK', 'DDCAPS2_CANBOBINTERLEAVED', 'DDERR_NOTLOADED',
    'DDFXCAPS_OVERLAYFILTER', 'DDOVER_REFRESHDIRTYRECTS', 'DDLOCK_DONOTWAIT',
    'DDOVER_INTERLEAVED', 'DDERR_DCALREADYCREATED', 'DDERR_NOTLOCKED',
    'DDCOLOR_BRIGHTNESS', 'DDBLT_EXTENDED_FLAGS', 'DDERR_OVERLAYCANTCLIP',
    'IDirectDraw2_QueryInterface', 'DDCAPS2_RESERVED1', 'DDPF_BUMPLUMINANCE',
    'DDERR_NOTAOVERLAYSURFACE', 'DDOSD_OSCAPS', 'DDOVERFX_MIRRORUPDOWN',
    'IDirectDrawSurface7_SetClipper', 'IDirectDrawSurface4_PageUnlock',
    'DDOVER_BOBHARDWARE', 'DDCKEYCAPS_DESTOVERLAYCLRSPACEYUV', 'DDENUMRET_OK',
    'DDFXALPHACAPS_BLTALPHASURFACESNEG', 'DDERR_NONONLOCALVIDMEM',
    'IDirectDraw4_GetDisplayMode', 'IDirectDrawSurface3_EnumAttachedSurfaces',
    'DDCAPS_ALIGNBOUNDARYDEST', 'IDirectDrawSurface3_Blt', 'DDERR_MOREDATA',
    'IDirectDraw7_DuplicateSurface', 'IDirectDrawSurface4_Restore',
    'IDirectDrawSurface4_Release', 'DDCAPS2_PRIMARYGAMMA', 'DDGBS_ISBLTDONE',
    'DDCAPS_READSCANLINE', 'DDCAPS_BLTSTRETCH', 'IDirectDrawSurface4_Blt',
    'DDSD_ZBUFFERBITDEPTH', 'DDFXCAPS_BLTMIRRORUPDOWN', 'DDPCAPS_ALPHA',
    'DDSCL_NOWINDOWCHANGES', 'IDirectDrawSurface4_UpdateOverlayZOrder',
    'IDirectDrawClipper_Initialize', 'DDFXALPHACAPS_OVERLAYALPHAPIXELS',
    'DDBLT_ZBUFFERSRCCONSTOVERRIDE', 'IDirectDraw_CreateSurface',
    'DDOSDCAPS_OPTCOMPRESSED', 'DDOVERZ_INSERTINFRONTOF', 'DDPF_LUMINANCE',
    'IDirectDrawSurface_DeleteAttachedSurface', 'DDCAPS_COLORKEYHWASSIST',
    'IDirectDraw7_Compact', 'DDCKEYCAPS_NOCOSTOVERLAY', 'DDSVCAPS_RESERVED2',
    'DDSVCAPS_RESERVED1', 'IDirectDrawSurface_IsLost', 'DDOVER_AUTOFLIP',
    'DDFXALPHACAPS_OVERLAYALPHAPIXELSNEG', 'DDERR_NOTEXTUREHW', 'DDOVER_SHOW',
    'DDSCAPS2_EXTENDEDFORMATPRIMARY', 'DDBLTFAST_DONOTWAIT', 'DDSCAPS_ALPHA',
    'DDCAPS2_CANAUTOGENMIPMAP', 'DDERR_DEVICEDOESNTOWNSURFACE', 'DDLOCK_WAIT',
    'DDLOCK_NOOVERWRITE', 'DDFXCAPS_OVERLAYSHRINKY', 'DDSD_CKSRCOVERLAY',
    'IDirectDrawSurface7_SetColorKey', 'DDEDM_STANDARDVGAMODES', 'DDCAPS_DX7',
    'DDSCAPS2_TEXTUREMANAGE', 'DDCKEYCAPS_SRCOVERLAY', 'DDSCAPS_ALLOCONLOAD',
    'IDirectDrawSurface7_Restore', 'DDFXCAPS_BLTSTRETCHYN', 'GET_WHQL_YEAR',
    'IDirectDraw2_GetGDISurface', 'DDSCAPS2_CUBEMAP_NEGATIVEZ', '_DDCAPS_DX3',
    'DDLOCK_DISCARDCONTENTS', 'DDERR_CANNOTDETACHSURFACE', 'DDSD_LPSURFACE',
    'IDirectDrawSurface3_Restore', 'DDFXCAPS_OVERLAYARITHSTRETCHYN',
    'DDOVER_KEYSRCOVERRIDE', 'DDERR_UNSUPPORTEDFORMAT', 'DDCAPS_CANBLTSYSMEM',
    'DDFXCAPS_OVERLAYMIRRORLEFTRIGHT', 'DDCKEYCAPS_SRCBLTCLRSPACEYUV',
    'IDirectDrawSurface2_AddOverlayDirtyRect', 'DDERR_INVALIDSURFACETYPE',
    'DDENUM_NONDISPLAYDEVICES', 'IDirectDraw7_RestoreAllSurfaces',
    'IDirectDraw_QueryInterface', 'DDERR_COLORKEYNOTSET', 'DDERR_NOPALETTEHW',
    'DDSCAPS2_HINTDYNAMIC', 'DDERR_EXCLUSIVEMODEALREADYSET', 'DDPF_RGBTOYUV',
    'DDBLT_KEYDESTOVERRIDE', 'IDirectDrawSurface3_SetColorKey', '_DDCAPS_DX1',
    'DDFXCAPS_OVERLAYSHRINKYN', 'DDLOCK_NODIRTYUPDATE', 'DDBLT_DDROPS',
    'DDSCAPS_TEXTURE', 'DDCAPS2_VIDEOPORT', 'DDGFS_CANFLIP', 'DDSCAPS_MODEX',
    'DDERR_INVALIDCAPS', 'DDCKEYCAPS_DESTBLTCLRSPACE', 'DDERR_NOCOLORCONVHW',
    'DDSCAPS2_STEREOSURFACELEFT', 'DDSETSURFACEDESC_PRESERVEDC', 'DDCAPS_DX3',
    'DDCKEY_COLORSPACE', 'DDBLT_ALPHADEST', 'DDPF_COMPRESSED', 'DDCAPS_ZBLTS',
    'DDCOLOR_GAMMA', 'DDSCAPS3_MULTISAMPLE_QUALITY_SHIFT', 'DDERR_NOBLTHW',
    'DDERR_BLTFASTCANTCLIP', 'DDERR_DDSCAPSCOMPLEXREQUIRED', 'DDCAPS2_STEREO',
    'DDFXCAPS_OVERLAYSTRETCHXN', 'IDirectDrawClipper_QueryInterface',
    'DDGDI_GETHOSTIDENTIFIER', 'DDERR_NORASTEROPHW', 'DDBLTFX_ZBUFFERRANGE',
    'DDSVCAPS_STEREOSEQUENTIAL', 'DDPF_ALPHAPIXELS', 'DDSCL_FPUSETUP',
    'DDSCAPS3_CREATESHAREDRESOURCE', 'DDFXALPHACAPS_OVERLAYALPHASURFACES',
    'IDirectDrawSurface7_AddAttachedSurface', 'DDSCAPS2_NPATCHES',
    'DDERR_VIDEONOTACTIVE', 'DDSD_SRCVBHANDLE', 'DDSCAPS_COMPLEX',
    'DDERR_PRIMARYSURFACEALREADYEXISTS', 'IDirectDrawSurface_SetColorKey',
    'DDOVER_REFRESHALL', 'DDBLTFX_ROTATE180', 'IDirectDraw2_CreatePalette',
    'DDERR_NOMONITORINFORMATION', 'DDCAPS2_CANFLIPODDEVEN', 'DDERR_OUTOFCAPS',
    'DDSCL_CREATEDEVICEWINDOW', 'IDirectDrawSurface2_UpdateOverlayZOrder',
    'DDWAITVB_BLOCKEND', 'DDCAPS2_DYNAMICTEXTURES', 'DDERR_NOT4BITCOLORINDEX',
    'DDCKEYCAPS_SRCOVERLAYONEACTIVE', 'DDFXCAPS_BLTSHRINKX', 'DDPCAPS_2BIT',
    'DDFXCAPS_BLTSHRINKY', 'DDCAPS2_CANRENDERWINDOWED', 'DDBLT_ALPHASRCNEG',
    'IDirectDrawSurface2_EnumOverlayZOrders', 'DDSCAPS_OFFSCREENPLAIN',
    'IDirectDraw_WaitForVerticalBlank', 'DDFXCAPS_BLTARITHSTRETCHYN',
    'DDFLIP_INTERVAL4', 'DDCOLOR_COLORENABLE', 'DDFLIP_INTERVAL3',
    'DDFLIP_INTERVAL2', 'DDCAPS2_CANMANAGETEXTURE', 'DDERR_INVALIDRECT',
    'DDFXCAPS_OVERLAYSTRETCHY', 'DDERR_OUTOFVIDEOMEMORY', 'DDPCAPS_ALLOW256',
    'DDCKEYCAPS_DESTOVERLAYYUV', 'DDERR_NODRIVERSUPPORT', 'DDLOCK_OKTOSWAP',
    'IDirectDraw4_Compact', 'DDCAPS2_FLIPNOVSYNC', 'DDERR_HWNDSUBCLASSED',
    'DDSCAPS_FRONTBUFFER', 'DDERR_CLIPPERISUSINGHWND', 'DDEDM_REFRESHRATES',
    'DDOVER_ALPHADESTCONSTOVERRIDE', 'IDirectDrawPalette_AddRef',
    'DDFXCAPS_OVERLAYMIRRORUPDOWN', 'DDERR_CURRENTLYNOTAVAIL', 'DDSCAPS_FLIP',
    'DDCAPS_NOHARDWARE', 'IDirectDrawSurface2_ReleaseDC', 'DDERR_NOEMULATION',
    'DDOVER_DEGRADEARGBSCALING', 'DDERR_NOTPALETTIZED', 'DDCAPS2_COPYFOURCC',
    'DDSCAPS_STANDARDVGAMODE', 'DDCKEYCAPS_SRCBLTYUV', 'DDFXCAPS_BLTSHRINKYN',
    'DDERR_DIRECTDRAWALREADYCREATED', 'IDirectDrawSurface7_GetLOD',
    'DDLOCK_HASVOLUMETEXTUREBOXRECT', 'DDOSDCAPS_VALIDOSCAPS', 'DDERR_NOHWND',
    'DDSCAPS2_HARDWAREDEINTERLACE', 'DDENUMSURFACES_MATCH', 'DDERR_NOALPHAHW',
    'DDCKEY_DESTOVERLAY', 'DDCAPS_RESERVED1', 'DDCAPS_ALIGNSTRIDE',
    'DDSCAPS_VIDEOMEMORY', 'DDSCAPS3_MULTISAMPLE_MASK', 'DDERR_WRONGMODE',
    'DDSD_CKDESTBLT', 'DDERR_SURFACEALREADYDEPENDENT', 'DDERR_TOOBIGWIDTH',
    'DDOVER_KEYSRC', 'DDBLTFX_NOTEARING', 'DDERR_NOFOCUSWINDOW', 'DDCAPS_DX5',
    'DDSCAPS_RESERVED1', 'DDSCAPS_RESERVED2', 'DDSCAPS_RESERVED3',
    'DDFXCAPS_BLTSTRETCHXN', 'DDSCAPS2_CUBEMAP_ALLFACES', 'DDERR_NOCOLORKEY',
    'IID_IDirectDrawSurface3', 'IID_IDirectDrawClipper', 'CLSID_DirectDraw',
    'IID_IDirectDrawSurface2', 'IID_IDirectDrawSurface7', 'IID_IDirectDraw',
    'IID_IDirectDrawGammaControl', 'IID_IDirectDrawSurface4', '_DDCAPS_DX6',
    'IID_IDirectDrawColorControl', 'CLSID_DirectDrawClipper', '_DDCAPS_DX7',
    'CLSID_DirectDraw7', 'IID_IDirectDraw4', 'IID_IDirectDraw7', 'DDCAPS_DX6',
    'IID_IDirectDrawSurface', 'IID_IDirectDrawPalette', 'IID_IDirectDraw2',
    'IDirectDrawPalette', '_DDGAMMARAMP', 'DDSURFACEDESC', 'IDirectDraw',
    '_DDOVERLAYFX', 'tagDDDEVICEIDENTIFIER2', 'DDDEVICEIDENTIFIER',
    'LPDDSURFACEDESC2', 'DDSURFACEDESC2', 'IDirectDrawClipper', '_DDCAPS_DX5',
    '_DDBLTBATCH', 'LPDDSURFACEDESC', 'LPDDCOLORCONTROL', '_DDOPTSURFACEDESC',
    'LPDIRECTDRAWGAMMACONTROL', 'DDGAMMARAMP', 'LPDDDEVICEIDENTIFIER',
    'LPDIRECTDRAW7', '_DDCOLORKEY', 'DDDEVICEIDENTIFIER2', '_DDPIXELFORMAT',
    'IDirectDrawSurface', '_DDSURFACEDESC2', 'LPDIRECTDRAWSURFACE3',
    'DDPIXELFORMAT', 'LPDIRECTDRAWSURFACE7', 'LPDIRECTDRAWCLIPPER',
    'LPDIRECTDRAWSURFACE2', 'LPDIRECTDRAWCOLORCONTROL', 'LPDIRECTDRAW4',
    'LPDDSCAPSEX', 'LPDIRECTDRAWSURFACE4', '_DDCOLORCONTROL',
    'DDOVERLAYFX', 'LPDDDEVICEIDENTIFIER2', 'LPDIRECTDRAWSURFACE',
    'LPDIRECTDRAW', 'tagDDDEVICEIDENTIFIER', 'DDOPTSURFACEDESC', 'DDCAPS_DX1',
    '_DDSURFACEDESC', 'DDCOLORKEY', 'LPDIRECTDRAWPALETTE', 'DDCOLORCONTROL',
    'LPDIRECTDRAW2', 'LPDDPIXELFORMAT', 'LPDDOSCAPS', 'LPDDSCAPS2',
    'LPSURFACESTREAMINGCALLBACK', 'LPDDGAMMARAMP', 'LPDDOVERLAYFX',
    'LPDDCAPS_DX6', 'LPDDCAPS_DX7', 'LPDDCAPS_DX5', 'LPDDCAPS_DX3',
    'LPDDCAPS_DX1', 'LPDDENUMMODESCALLBACK', 'LPDDENUMSURFACESCALLBACK',
    'LPDDENUMMODESCALLBACK2', 'LPDDBLTBATCH', 'LPDDCOLORKEY',
    'LPDDENUMSURFACESCALLBACK7', 'LPDDENUMSURFACESCALLBACK2',
)
