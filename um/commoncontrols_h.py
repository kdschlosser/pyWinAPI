
import comtypes
import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD

IUnknown = comtypes.IUnknown

IID_IImageList = MIDL_INTERFACE(
    "{46EB5926-582E-4017-9FDF-E8998DAA0950}"
)


class IImageList(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IImageList


IID_IImageList2 = MIDL_INTERFACE(
    "{192B9D83-50FC-457B-90A0-2B82A8B5DAE1}"
)


class IImageList2(IImageList):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IImageList2


CLSID_ImageList = DECLSPEC_UUID(
    "{7C476BA2-02B1-48F4-8048-B24619DDC058}"
)



LIBID_CommonControlObjects = IID(
    '{BCADA15B-B428-420c-8D28-023590924C9F}'
)


class CommonControlObjects(object):
    name = 'CommonControlObjects'
    _reg_typelib_ = (LIBID_CommonControlObjects,)


class ImageList(comtypes.CoClass):
    _case_insensitive_ = True
    _idlflags_ = []
    _reg_clsid_ = CLSID_ImageList
    _reg_typelib_ = (LIBID_CommonControlObjects,)
    _com_interfaces_ = [IImageList2, IImageList]


class _IMAGELISTDRAWPARAMS(ctypes.Structure):
    pass


IMAGELISTDRAWPARAMS = _IMAGELISTDRAWPARAMS


class tagIMAGEINFO(ctypes.Structure):
    pass


IMAGEINFO = tagIMAGEINFO


class tagIMAGELISTSTATS(ctypes.Structure):
    pass


IMAGELISTSTATS = tagIMAGELISTSTATS


def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    __REQUIRED_RPCNDR_H_VERSION__ = 500
# END IF
# verify that the <rpcsal.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    __REQUIRED_RPCSAL_H_VERSION__ = 100
# END IF
from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA


__RPCNDR_H_VERSION__ = None
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

COM_NO_WINDOWS_H = None
if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

__commoncontrols_h__ = None
if not defined(__commoncontrols_h__):
    __commoncontrols_h__ = 1

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF
    # Forward Declarations
    __IImageList_FWD_DEFINED__ = None
    if not defined(__IImageList_FWD_DEFINED__):
        __IImageList_INTERFACE_DEFINED__ = None
        __IImageList_FWD_DEFINED__ = 1
    # END IF  __IImageList_FWD_DEFINED__

    __IImageList2_FWD_DEFINED__ = None
    if not defined(__IImageList2_FWD_DEFINED__):
        __IImageList2_INTERFACE_DEFINED__ = None
        __IImageList2_FWD_DEFINED__ = 1
    # END IF  __IImageList2_FWD_DEFINED__

    __ImageList_FWD_DEFINED__ = None
    if not defined(__ImageList_FWD_DEFINED__):
        __ImageList_INTERFACE_DEFINED__ = None
        __ImageList_FWD_DEFINED__ = 1

        if defined(__cplusplus):
           pass
        else:
            pass
        # END IF  __cplusplus    # END IF  __ImageList_FWD_DEFINED__
    # header files for imported files
    from oaidl_h import * # NOQA
    from ocidl_h import * # NOQA
    if defined(__cplusplus):
        pass
    comctl32 = ctypes.windll.Comctl32

    # END IF
    # interface __MIDL_itf_commoncontrols_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        WINCOMMCTRLAPI = None

        if not defined(WINCOMMCTRLAPI):
            _COMCTL32_ = None
            if not defined(_COMCTL32_) and defined(_WIN32):
                WINCOMMCTRLAPI = 1
            else:
                WINCOMMCTRLAPI = 1
            # END IF        # END IF   WINCOMMCTRLAPI
        if defined(MIDL_PASS):
            RGBQUAD = DWORD

            HIMAGELIST = POINTER(IUnknown)

            _IMAGELISTDRAWPARAMS._fields_ = [
                ('cbSize', DWORD),
                ('himl', HIMAGELIST),
                ('i', INT),
                ('hdcDst', HDC),
                ('x', INT),
                ('y', INT),
                ('cx', INT),
                ('cy', INT),
                ('xBitmap', INT),
                ('yBitmap', INT),
                ('rgbBk', COLORREF),
                ('rgbFg', COLORREF),
                ('fStyle', UINT),
                ('dwRop', DWORD),
                ('fState', DWORD),
                ('Frame', DWORD),
                ('crEffect', COLORREF),
            ]
            LPIMAGELISTDRAWPARAMS = POINTER(IMAGELISTDRAWPARAMS)
            tagIMAGEINFO._fields_ = [
                ('hbmImage', HBITMAP),
                ('hbmMask', HBITMAP),
                ('Unused1', INT),
                ('Unused2', INT),
                ('rcImage', RECT),
            ]
            LPIMAGEINFO = POINTER(IMAGEINFO)
        # END IF
        if NTDDI_VERSION >= NTDDI_VISTA:


            # WINCOMMCTRLAPI HRESULT WINAPI ImageList_CoCreateInstance(
            # _In_  REFCLSID rclsid,
            # _In_opt_  IUnknown *punkOuter,
            # _In_  REFIID riid,
            # _Outptr_ VOID **ppv);
            ImageList_CoCreateInstance = comctl32.ImageList_CoCreateInstance
            ImageList_CoCreateInstance.restype = HRESULT

        # END IF
        ILIF_ALPHA = 0x00000001
        ILIF_LOWQUALITY = 0x00000002
        ILDRF_IMAGELOWQUALITY = 0x00000001
        ILDRF_OVERLAYLOWQUALITY = 0x00000010

        if not defined(__IImageList_INTERFACE_DEFINED__):
            __IImageList_INTERFACE_DEFINED__ = 1

            # interface IImageList
            # [object][local][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass

            else: # C style interface
                IImageList._methods_ = [
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Add',
                        ([annotation('_In_'), 'in'], HBITMAP, 'hbmImage'),
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            HBITMAP,
                           'hbmMask'
                        ),
                        ([annotation('_Out_'), 'out'], POINTER(int), 'pi'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'ReplaceIcon',
                        ([], INT, 'i'),
                        ([annotation('_In_'), 'in'], HICON, 'hicon'),
                        (['out', annotation('_Out_')], POINTER(int), 'pi'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetOverlayImage',
                        ([], INT, 'iImage'),
                        ([], INT, 'iOverlay'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Replace',
                        ([], INT, 'i'),
                        ([annotation('_In_'), 'in'], HBITMAP, 'hbmImage'),
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            HBITMAP,
                           'hbmMask'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'AddMasked',
                        ([annotation('_In_'), 'in'], HBITMAP, 'hbmImage'),
                        ([], COLORREF, 'crMask'),
                        (['out', annotation('_Out_')], POINTER(int), 'pi'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Draw',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IMAGELISTDRAWPARAMS),
                           'pimldp'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Remove',
                        ([], INT, 'i'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIcon',
                        ([], INT, 'i'),
                        ([], UINT, 'flags'),
                        (
                            ['out', annotation('_Out_')],
                            POINTER(HICON),
                           'picon'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetImageInfo',
                        ([], INT, 'i'),
                        (
                            ['out', annotation('_Out_')],
                            POINTER(IMAGEINFO),
                           'pImageInfo'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Copy',
                        ([], INT, 'iDst'),
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IUnknown),
                           'punkSrc'
                        ),
                        ([], INT, 'iSrc'),
                        ([], UINT, 'uFlags'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Merge',
                        ([], INT, 'i1'),
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IUnknown),
                           'punk2'
                        ),
                        ([], INT, 'i2'),
                        ([], INT, 'dx'),
                        ([], INT, 'dy'),
                        ([], REFIID, 'riid'),
                        (
                            [annotation('_Outptr_'), 'out'],
                            POINTER(POINTER(VOID)),
                           'ppv'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Clone',
                        ([], REFIID, 'riid'),
                        (
                            [annotation('_Outptr_'), 'out'],
                            POINTER(POINTER(VOID)),
                           'ppv'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetImageRect',
                        ([], INT, 'i'),
                        (['out', annotation('_Out_')], POINTER(RECT), 'prc'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIconSize',
                        (['out', annotation('_Out_')], POINTER(int), 'cx'),
                        ([], POINTER(int), 'cy'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetIconSize',
                        ([], INT, 'cx'),
                        ([], INT, 'cy'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetImageCount',
                        (['out', annotation('_Out_')], POINTER(int), 'pi'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetImageCount',
                        ([], UINT, 'uNewCount'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetBkColor',
                        ([], COLORREF, 'clrBk'),
                        (
                            ['out', annotation('_Out_')],
                            POINTER(COLORREF),
                           'pclr'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetBkColor',
                        (
                            [annotation('_Out_'), 'out'],
                            POINTER(COLORREF),
                           'pclr'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'BeginDrag',
                        ([], INT, 'iTrack'),
                        ([], INT, 'dxHotspot'),
                        ([], INT, 'dyHotspot'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'EndDrag',
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'DragEnter',
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            HWND,
                           'hwndLock'
                        ),
                        ([], INT, 'x'),
                        ([], INT, 'y'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'DragLeave',
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            HWND,
                           'hwndLock'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'DragMove',
                        ([], INT, 'x'),
                        ([], INT, 'y'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetDragCursorImage',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IUnknown),
                           'punk'
                        ),
                        ([], INT, 'iDrag'),
                        ([], INT, 'dxHotspot'),
                        ([], INT, 'dyHotspot'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'DragShowNolock',
                        ([], BOOL, 'fShow'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDragImage',
                        (
                            ['out', annotation('_Out_opt_')],
                            POINTER(POINT),
                           'ppt'
                        ),
                        ([], POINTER(POINT), 'pptHotspot'),
                        ([], REFIID, 'riid'),
                        (
                            [annotation('_Outptr_'), 'out'],
                            POINTER(POINTER(VOID)),
                           'ppv'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetItemFlags',
                        ([], INT, 'i'),
                        (
                            ['out', annotation('_Out_')],
                            POINTER(DWORD),
                           'dwFlags'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetOverlayImage',
                        ([], INT, 'iOverlay'),
                        (
                            ['out', annotation('_Out_')],
                            POINTER(int),
                           'piIndex'
                        ),
                    ),
                ]


                # [in]
                # [annotation][iid_is][out]
                # [annotation][in]
                # [annotation][unique][in]
                # [annotation][out]
                # [annotation][in]
                # [annotation][out]
                # [annotation][in]
                # [annotation][unique][in]
                # [annotation][in]
                # [annotation][out]
                # [annotation][in]
                # [annotation][out]
                # [annotation][out]
                # [annotation][in]
                # [annotation][in]
                # [annotation][iid_is][out]
                # [annotation][iid_is][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][unique][in]
                # [annotation][unique][in]
                # [annotation][in]
                # [annotation][out]
                # [annotation][out]
                # [annotation][iid_is][out]
                # [annotation][out]
                # [annotation][out]            # END IF  C style interface        # END IF  __IImageList_INTERFACE_DEFINED__
        # interface __MIDL_itf_commoncontrols_0000_0001
        # [local]
        ILR_DEFAULT = 0x0000
        ILR_HORIZONTAL_LEFT = 0x0000
        ILR_HORIZONTAL_CENTER = 0x0001
        ILR_HORIZONTAL_RIGHT = 0x0002
        ILR_VERTICAL_TOP = 0x0000
        ILR_VERTICAL_CENTER = 0x0010
        ILR_VERTICAL_BOTTOM = 0x0020
        ILR_SCALE_CLIP = 0x0000
        ILR_SCALE_ASPECTRATIO = 0x0100

        if not defined(__IImageList2_INTERFACE_DEFINED__):
            __IImageList2_INTERFACE_DEFINED__ = 1

            # interface IImageList2
            # [object][local][uuid]
            ILGOS_ALWAYS = 0x00000000
            ILGOS_FROMSTANDBY = 0x00000001
            ILFIP_ALWAYS = 0x00000000
            ILFIP_FROMSTANDBY = 0x00000001
            ILDI_PURGE = 0x00000001
            ILDI_STANDBY = 0x00000002
            ILDI_RESETACCESS = 0x00000004
            ILDI_QUERYACCESS = 0x00000008
            tagIMAGELISTSTATS._fields_ = [
                ('cbSize', DWORD),
                ('cAlloc', INT),
                ('cUsed', INT),
                ('cStandby', INT),
            ]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IImageList2._methods_ = [
                    # Flags for GetOriginalSize
                    # always get the original size (can be slow) only if
                    # present or on standby Flags for ForceImagePresent always
                    # get the image (can be slow) only if on standby Flags for
                    # DiscardImages ILDI_STANDBY and ILDI_PURGE are mutually
                    # exclusive. ILDI_RESETACCESS can be combined with either.
                    # discard and purge discard to standby list reset
                    # "has been accessed" flag ask whether access flag is set
                    # (but do not reset)
                    # number of images allocated
                    # number of images in use
                    # number of standby images
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Resize',
                        ([], INT, 'cxNewIconSize'),
                        ([], INT, 'cyNewIconSize'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetOriginalSize',
                        (['in'], INT, 'iImage'),
                        ([], DWORD, 'dwFlags'),
                        ([annotation('_Out_'), 'out'], POINTER(INT), 'pcx'),
                        ([], POINTER(INT), 'pcy'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetOriginalSize',
                        (['in'], INT, 'iImage'),
                        ([], INT, 'cx'),
                        ([], INT, 'cy'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetCallback',
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            POINTER(IUnknown),
                           'punk'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCallback',
                        (['in'], REFIID, 'riid'),
                        (
                            [annotation('_Outptr_'), 'out'],
                            POINTER(POINTER(VOID)),
                           'ppv'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'ForceImagePresent',
                        (['in'], INT, 'iImage'),
                        ([], DWORD, 'dwFlags'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'DiscardImages',
                        (['in'], INT, 'iFirstImage'),
                        ([], INT, 'iLastImage'),
                        ([], DWORD, 'dwFlags'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'PreloadImages',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IMAGELISTDRAWPARAMS),
                           'pimldp'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetStatistics',
                        (
                            [annotation('_Inout_'), 'out', 'in'],
                            POINTER(IMAGELISTSTATS),
                           'pils'
                        ),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], INT, 'cx'),
                        ([], INT, 'cy'),
                        ([], UINT, 'flags'),
                        ([], INT, 'cInitial'),
                        ([], INT, 'cGrow'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'Replace2',
                        (['in'], INT, 'i'),
                        ([annotation('_In_'), 'in'], HBITMAP, 'hbmImage'),
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            HBITMAP,
                           'hbmMask'
                        ),
                        ([], POINTER(IUnknown), 'punk'),
                        ([], DWORD, 'dwFlags'),
                    ),

                    COMMETHOD(
                        [],
                        HRESULT,
                        'ReplaceFromImageList',
                        (['in'], INT, 'i'),
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IImageList),
                           'pil'
                        ),
                        ([], INT, 'iSrc'),
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            POINTER(IUnknown),
                           'punk'
                        ),
                        ([], DWORD, 'dwFlags'),
                    ),
                ]


                # [in]
                # [annotation][iid_is][out]
                # [annotation][in]
                # [annotation][unique][in]
                # [annotation][out]
                # [annotation][in]
                # [annotation][out]
                # [annotation][in]
                # [annotation][unique][in]
                # [annotation][in]
                # [annotation][out]
                # [annotation][in]
                # [annotation][out]
                # [annotation][out]
                # [annotation][in]
                # [annotation][in]
                # [annotation][iid_is][out]
                # [annotation][iid_is][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][out]
                # [annotation][unique][in]
                # [annotation][unique][in]
                # [annotation][in]
                # [annotation][out]
                # [annotation][out]
                # [annotation][iid_is][out]
                # [annotation][out]
                # [annotation][out]
                # [in]
                # [in]
                # [annotation][out]
                # [annotation][out]
                # [in]
                # [in]
                # [in]
                # [annotation][unique][in]
                # [in]
                # [annotation][iid_is][out]
                # [in]
                # [in]
                # [in]
                # [in]
                # [annotation][in]
                # [annotation][out][in]
                # [in]
                # [in]
                # [in]
                # [in]
                # [in]
                # [in]
                # [annotation][in]
                # [annotation][unique][in]
                # [annotation][unique][in]
                # [in]
                # [in]
                # [annotation][in]
                # [in]
                # [annotation][unique][in]
                # [in]
            # END IF  C style interface
        # END IF  __IImageList2_INTERFACE_DEFINED__

        __CommonControlObjects_LIBRARY_DEFINED__ = None

        if not defined(__CommonControlObjects_LIBRARY_DEFINED__):
            __CommonControlObjects_LIBRARY_DEFINED__ = 1

            # library CommonControlObjects
            # [uuid]
            if defined(__cplusplus):
                pass
            # END IF
        # END IF  __CommonControlObjects_LIBRARY_DEFINED__

        # interface __MIDL_itf_commoncontrols_0000_0003
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF
# END IF
