import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
_INC_COMMCTRL = None
WINCOMMCTRLAPI = None
_HRESULT_DEFINED = None
_COMCTL32_ = None
DUMMYUNIONNAME = 0
SNDMSG = None
NOUSER = None
NOHEADER = None

# ***************************************************************************\
# * commctrl.h - - Interface for the Windows Common Controls * * Version 1.2
# * * Copyright (c) Microsoft Corporation. All rights reserved. * *
# \***************************************************************************
if not defined(_INC_COMMCTRL):
    _INC_COMMCTRL = 1

    from pyWinAPI.shared.winapifamily_h import *
    from pyWinAPI.shared.sdkddkver_h import *
    from pyWinAPI.shared.guiddef_h import *
    from pyWinAPI.um.winuser_h import *

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(_MSC_VER) and (_MSC_VER >= 1200):
            pass
        # END IF

        if not defined(_HRESULT_DEFINED):
            _HRESULT_DEFINED = 1
            HRESULT = LONG
        # END IF   not _HRESULT_DEFINED

        if not defined(NOUSER):

            # Define API decoration for direct importing of DLL references.
            if not defined(WINCOMMCTRLAPI):
                if not defined(_COMCTL32_) and defined(_WIN32):
                    # WINCOMMCTRLAPI = DECLSPEC_IMPORT
                    WINCOMMCTRLAPI = 1
                else:
                    WINCOMMCTRLAPI = 1
                # END IF
            # END IF   WINCOMMCTRLAPI

            # For compilers that don't support nameless unions

            if not defined(DUMMYUNIONNAME):
                NONAMELESSUNION = 0
                if defined(NONAMELESSUNION):
                    pass
                    # DUMMYUNIONNAME = u
                    # DUMMYUNIONNAME2 = u2
                    # DUMMYUNIONNAME3 = u3
                    # DUMMYUNIONNAME4 = u4
                    # DUMMYUNIONNAME5 = u5
                else:
                    pass
                    # DUMMYUNIONNAME = 1
                    # DUMMYUNIONNAME2 = 1
                    # DUMMYUNIONNAME3 = 1
                    # DUMMYUNIONNAME4 = 1
                    # DUMMYUNIONNAME5 = 1
                # END IF
            # END IF   DUMMYUNIONNAME

            if defined(__cplusplus):
                pass
            # END IF
            if not defined(SNDMSG):
                if defined(__cplusplus):
                    if not defined(_MAC):
                        # NDMSG = ::SendMessage
                        pass
                    else:
                        # SNDMSG = ::AfxSendMessage
                        pass
                    # END IF

                else:
                    if not defined(_MAC):
                        SNDMSG = SendMessage
                    else:
                        SNDMSG = AfxSendMessage
                    # END IF  _MAC
                # END IF
            # END IF   ifndef SNDMSG
            if defined(_MAC):
                if not defined(RC_INVOKED):
                    if not defined(_WLM_NOFORCE_LIBS):
                        if not defined(_WLMDLL):
                            if defined(_DEBUG):
                                pass
                            else:
                                pass
                            # END IF
                        else:
                            if defined(_DEBUG):
                                # pragma comment(lib, "msvcctld.lib")
                                pass
                            else:
                                # pragma comment(lib, "msvcctl.lib")
                                pass
                            # END IF
                        # END IF   _WLMDLL
                    # END IF   _WLM_NOFORCE_LIBS
                # END IF   RC_INVOKED
            # END IF  _MAC

            class tagINITCOMMONCONTROLSEX(ctypes.Structure):
                pass


            tagINITCOMMONCONTROLSEX._fields_ = [
                ('dwSize', DWORD), # size of this structure
                ('dwICC', DWORD), # flags indicating which classes to be initialized
            ]
            INITCOMMONCONTROLSEX = tagINITCOMMONCONTROLSEX
            LPINITCOMMONCONTROLSEX = POINTER(tagINITCOMMONCONTROLSEX)

            ICC_LISTVIEW_CLASSES = 0x00000001
            ICC_TREEVIEW_CLASSES = 0x00000002
            ICC_BAR_CLASSES = 0x00000004
            ICC_TAB_CLASSES = 0x00000008
            ICC_UPDOWN_CLASS = 0x00000010
            ICC_PROGRESS_CLASS = 0x00000020
            ICC_HOTKEY_CLASS = 0x00000040
            ICC_ANIMATE_CLASS = 0x00000080
            ICC_WIN95_CLASSES = 0x000000FF
            ICC_DATE_CLASSES = 0x00000100
            ICC_USEREX_CLASSES = 0x00000200
            ICC_COOL_CLASSES = 0x00000400
            ICC_INTERNET_CLASSES = 0x00000800
            ICC_PAGESCROLLER_CLASS = 0x00001000
            ICC_NATIVEFNTCTL_CLASS = 0x00002000

            if NTDDI_VERSION >= NTDDI_WINXP:
                ICC_STANDARD_CLASSES = 0x00004000
                ICC_LINK_CLASS = 0x00008000
            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

            comctl32 = ctypes.windll.comctl32

            # WINCOMMCTRLAPI BOOL WINAPI InitCommonControlsEx(_In_ INITCOMMONCONTROLSEX *picce);
            InitCommonControlsEx = comctl32.InitCommonControlsEx
            InitCommonControlsEx.restype = BOOL

            ODT_HEADER = 100
            ODT_TAB = 101
            ODT_LISTVIEW = 102

            # == == == Ranges for control message IDs == == == == == == == ==
            # == == == == == == == == == == == =
            LVM_FIRST = 0x1000
            TV_FIRST = 0x1100
            HDM_FIRST = 0x1200
            TCM_FIRST = 0x1300
            PGM_FIRST = 0x1400

            if NTDDI_VERSION >= NTDDI_WINXP:
                ECM_FIRST = 0x1500
                BCM_FIRST = 0x1600
                CBM_FIRST = 0x1700
            # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

            CCM_FIRST = 0x2000
            CCM_LAST = CCM_FIRST + 0x200
            CCM_SETBKCOLOR = CCM_FIRST + 1


            class tagCOLORSCHEME(ctypes.Structure):
                pass


            tagCOLORSCHEME._fields_ = [
                ('dwSize', DWORD),
                ('clrBtnHighlight', COLORREF), # highlight color
                ('clrBtnShadow', COLORREF), # shadow color
            ]
            COLORSCHEME = tagCOLORSCHEME
            LPCOLORSCHEME = POINTER(tagCOLORSCHEME)

            CCM_SETCOLORSCHEME = CCM_FIRST + 2
            CCM_GETCOLORSCHEME = CCM_FIRST + 3
            CCM_GETDROPTARGET = CCM_FIRST + 4
            CCM_SETUNICODEFORMAT = CCM_FIRST + 5
            CCM_GETUNICODEFORMAT = CCM_FIRST + 6

            if NTDDI_VERSION >= NTDDI_WINXP:
                COMCTL32_VERSION = 6
            else:
                COMCTL32_VERSION = 5
            # END IF

            CCM_SETVERSION = CCM_FIRST + 0x7
            CCM_GETVERSION = CCM_FIRST + 0x8
            CCM_SETNOTIFYWINDOW = CCM_FIRST + 0x9

            if NTDDI_VERSION >= NTDDI_WINXP:
                CCM_SETWINDOWTHEME = CCM_FIRST + 0xB
                CCM_DPISCALE = CCM_FIRST + 0xC
            # END IF

            # for tooltips
            INFOTIPSIZE = 1024

            # == == == WM_NOTIFY Macros == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == =


            def HANDLE_WM_NOTIFY(hwnd, wParam, lParam, fn):
                return fn(hwnd, wParam, ctypes.byref(lParam))


            def FORWARD_WM_NOTIFY(hwnd, idFrom, pnmhdr, fn):
                return fn(hwnd, WM_NOTIFY, idFrom, ctypes.byref(pnmhdr))


            # == == == WM_NOTIFY codes (NMHDR.code values) == == == == == ==
            # == == == == == == == == == == ==
            NM_FIRST = 0
            NM_LAST = 99
            LVN_FIRST = 100
            LVN_LAST = 199

            # Property sheet reserved (0U - 200U) - (0U - 299U) - see prsht.h
            HDN_FIRST = 300
            HDN_LAST = 399
            TVN_FIRST = 400
            TVN_LAST = 499
            TTN_FIRST = 520
            TTN_LAST = 549
            TCN_FIRST = 550
            TCN_LAST = 580

            # Shell reserved   (0U - 580U) - (0U - 589U)
            CDN_FIRST = 601
            CDN_LAST = 699
            TBN_FIRST = 700
            TBN_LAST = 720
            UDN_FIRST = 721
            UDN_LAST = 729
            DTN_FIRST = 740
            DTN_LAST = 745
            MCN_FIRST = 746
            MCN_LAST = 752
            DTN_FIRST2 = 753
            DTN_LAST2 = 799
            CBEN_FIRST = 800
            CBEN_LAST = 830
            RBN_FIRST = 831
            RBN_LAST = 859
            IPN_FIRST = 860
            IPN_LAST = 879
            SBN_FIRST = 880
            SBN_LAST = 899
            PGN_FIRST = 900
            PGN_LAST = 950

            # == == == Generic WM_NOTIFY notification codes == == == == == ==
            # == == == == == == == == == == =
            NM_OUTOFMEMORY = NM_FIRST - 1
            NM_CLICK = NM_FIRST - 2
            NM_DBLCLK = NM_FIRST - 3
            NM_RETURN = NM_FIRST - 4
            NM_RCLICK = NM_FIRST - 5
            NM_RDBLCLK = NM_FIRST - 6
            NM_SETFOCUS = NM_FIRST - 7
            NM_KILLFOCUS = NM_FIRST - 8
            NM_CUSTOMDRAW = NM_FIRST - 12
            NM_HOVER = NM_FIRST - 13
            NM_NCHITTEST = NM_FIRST - 14
            NM_KEYDOWN = NM_FIRST - 15
            NM_RELEASEDCAPTURE = NM_FIRST - 16
            NM_SETCURSOR = NM_FIRST - 17
            NM_CHAR = NM_FIRST - 18
            NM_TOOLTIPSCREATED = NM_FIRST - 19
            NM_LDOWN = NM_FIRST - 20
            NM_RDOWN = NM_FIRST - 21
            NM_THEMECHANGED = NM_FIRST - 22

            if NTDDI_VERSION >= NTDDI_VISTA:
                NM_FONTCHANGED = NM_FIRST - 23
                NM_CUSTOMTEXT = NM_FIRST - 24
                NM_TVSTATEIMAGECHANGING = NM_FIRST - 24
            # END IF

            if not defined(CCSIZEOF_STRUCT):

                def CCSIZEOF_STRUCT(structname, member):
                    pass
                    # return ((INT(LPBYTE( & (structname*0) - >member) - (LPBYTE(structname*0)))) + ctypes.sizeof((structname*0) - >member))
            # END IF

            # == == == Generic WM_NOTIFY notification structures == == == ==
            # == == == == == == == == == ==
            class tagNMTOOLTIPSCREATED(ctypes.Structure):
                pass


            tagNMTOOLTIPSCREATED._fields_ = [
                ('hdr', NMHDR),
                ('hwndToolTips', HWND),
            ]
            NMTOOLTIPSCREATED = tagNMTOOLTIPSCREATED
             LPNMTOOLTIPSCREATED = POINTER(tagNMTOOLTIPSCREATED)


            class tagNMMOUSE(ctypes.Structure):
                pass


            tagNMMOUSE._fields_ = [
                ('hdr', NMHDR),
                ('dwItemSpec', DWORD_PTR),
                ('dwItemData', DWORD_PTR),
                ('pt', POINT),
                ('dwHitInfo', LPARAM), # any specifics about where on the item or control the mouse is
            ]
            NMMOUSE = tagNMMOUSE
            LPNMMOUSE = POINTER(tagNMMOUSE)
            NMCLICK = NMMOUSE
            LPNMCLICK = LPNMMOUSE

            # Generic structure to request an object of a specific type.
            class tagNMOBJECTNOTIFY(ctypes.Structure):
                pass


            tagNMOBJECTNOTIFY._fields_ = [
                ('hdr', NMHDR),
                ('iItem', INT),
                ('piid', POINTER(IID)) if defined(__IID_DEFINED__) else ('piid', POINTER(VOID)),
                ('pObject', POINTER(VOID)),
                ('hResult', HRESULT),
                ('dwFlags', DWORD), # control specific flags (hints as to where in iItem it hit)
            ]
            NMOBJECTNOTIFY = tagNMOBJECTNOTIFY
            LPNMOBJECTNOTIFY = POINTER(tagNMOBJECTNOTIFY)

            # Generic structure for a key
            class tagNMKEY(ctypes.Structure):
                pass


            tagNMKEY._fields_ = [
                ('hdr', NMHDR),
                ('nVKey', UINT),
                ('uFlags', UINT),
            ]
            NMKEY = tagNMKEY
            LPNMKEY = POINTER(tagNMKEY)

            # Generic structure for a CHARacter
            class tagNMCHAR(ctypes.Structure):
                pass


            tagNMCHAR._fields_ = [
                ('hdr', NMHDR),
                ('ch', UINT),
                ('dwItemPrev', DWORD), # Item previously selected
                ('dwItemNext', DWORD), # Item to be selected
            ]
            NMCHAR = tagNMCHAR
            LPNMCHAR = POINTER(tagNMCHAR)

            if _WIN32_IE >= 0x0600:
                class tagNMCUSTOMTEXT(ctypes.Structure):
                    pass


                tagNMCUSTOMTEXT._fields_ = [
                    ('hdr', NMHDR),
                    ('hDC', HDC),
                    ('lpString', LPCWSTR),
                    ('nCount', INT),
                    ('lpRect', LPRECT),
                    ('uFormat', UINT),
                    ('fLink', BOOL),
                ]
                NMCUSTOMTEXT = tagNMCUSTOMTEXT
                LPNMCUSTOMTEXT = POINTER(tagNMCUSTOMTEXT)
            # END IF   _WIN32_IE >= 0x0600



            if not defined(WMN_FIRST):
                WMN_FIRST = 1000
                WMN_LAST = 1200
            # END IF

            if NTDDI_VERSION >= NTDDI_WINXP:
                BCN_FIRST = 1250
                BCN_LAST = 1350
            # END IF

            if NTDDI_VERSION >= NTDDI_VISTA:
                TRBN_FIRST = 1501
                TRBN_LAST = 1519
            # END IF
            MSGF_COMMCTRL_BEGINDRAG = 0x4200
            MSGF_COMMCTRL_SIZEHEADER = 0x4201
            MSGF_COMMCTRL_DRAGSELECT = 0x4202
            MSGF_COMMCTRL_TOOLBARCUST = 0x4203

            # == == == == == == == == == == CUSTOM DRAW == == == == == == ==
            # == == == == == == == == == == == == == ==

            # custom draw return flags

            # values under 0x00010000 are reserved for global custom draw
            # values.

            # above that are for specific controls
            CDRF_DODEFAULT = 0x00000000
            CDRF_NEWFONT = 0x00000002
            CDRF_SKIPDEFAULT = 0x00000004
            CDRF_DOERASE = 0x00000008
            CDRF_SKIPPOSTPAINT = 0x00000100
            CDRF_NOTIFYPOSTPAINT = 0x00000010
            CDRF_NOTIFYITEMDRAW = 0x00000020
            CDRF_NOTIFYSUBITEMDRAW = 0x00000020
            CDRF_NOTIFYPOSTERASE = 0x00000040

            # drawstage flags

            # values under 0x00010000 are reserved for global custom draw
            # values.

            # above that are for specific controls
            CDDS_PREPAINT = 0x00000001
            CDDS_POSTPAINT = 0x00000002
            CDDS_PREERASE = 0x00000003
            CDDS_POSTERASE = 0x00000004

            # the 0x000010000 bit means it's individual item specific
            CDDS_ITEM = 0x00010000
            CDDS_ITEMPREPAINT = CDDS_ITEM | CDDS_PREPAINT
            CDDS_ITEMPOSTPAINT = CDDS_ITEM | CDDS_POSTPAINT
            CDDS_ITEMPREERASE = CDDS_ITEM | CDDS_PREERASE
            CDDS_ITEMPOSTERASE = CDDS_ITEM | CDDS_POSTERASE
            CDDS_SUBITEM = 0x00020000

            # itemState flags
            CDIS_SELECTED = 0x0001
            CDIS_GRAYED = 0x0002
            CDIS_DISABLED = 0x0004
            CDIS_CHECKED = 0x0008
            CDIS_FOCUS = 0x0010
            CDIS_DEFAULT = 0x0020
            CDIS_HOT = 0x0040
            CDIS_MARKED = 0x0080
            CDIS_INDETERMINATE = 0x0100

            if NTDDI_VERSION >= NTDDI_WINXP:
                CDIS_SHOWKEYBOARDCUES = 0x0200
            # END IF

            if NTDDI_VERSION >= NTDDI_VISTA:
                CDIS_NEARHOT = 0x0400
                CDIS_OTHERSIDEHOT = 0x0800
                CDIS_DROPHILITED = 0x1000
            # END IF
            class tagNMCUSTOMDRAWINFO(ctypes.Structure):
                pass


            tagNMCUSTOMDRAWINFO._fields_ = [
                ('hdr', NMHDR),
                ('dwDrawStage', DWORD),
                ('hdc', HDC),
                ('rc', RECT),

                # this is control specific, but it's how to specify an item.
                # valid only with CDDS_ITEM bit set
                ('dwItemSpec', DWORD_PTR),
                ('uItemState', UINT),
                ('lItemlParam', LPARAM),
            ]
            NMCUSTOMDRAW = tagNMCUSTOMDRAWINFO
            LPNMCUSTOMDRAW = POINTER(tagNMCUSTOMDRAWINFO)
            class tagNMTTCUSTOMDRAW(ctypes.Structure):
                pass


            tagNMTTCUSTOMDRAW._fields_ = [
                ('nmcd', NMCUSTOMDRAW),
                ('uDrawFlags', UINT),
            ]
            NMTTCUSTOMDRAW = tagNMTTCUSTOMDRAW
            LPNMTTCUSTOMDRAW = POINTER(tagNMTTCUSTOMDRAW)
            class tagNMCUSTOMSPLITRECTINFO(ctypes.Structure):
                pass


            tagNMCUSTOMSPLITRECTINFO._fields_ = [
                ('hdr', NMHDR),
                ('rcClient', RECT),
                ('rcButton', RECT),
                ('rcSplit', RECT),
            ]
            NMCUSTOMSPLITRECTINFO = tagNMCUSTOMSPLITRECTINFO
            LPNMCUSTOMSPLITRECTINFO = POINTER(tagNMCUSTOMSPLITRECTINFO)
            NM_GETCUSTOMSPLITRECT = BCN_FIRST + 0x0003

            # == == == IMAGE APIS == == == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == == =

            if not defined(NOIMAGEAPIS):
                CLR_NONE = 0xFFFFFFFF
                CLR_DEFAULT = 0xFF000000

                if not defined(HIMAGELIST):
                    class _IMAGELIST(ctypes.Structure):
                        pass

                    HIMAGELIST = POINTER(_IMAGELIST)

                # END IF
                if not defined(IMAGELISTDRAWPARAMS):
                    class _IMAGELISTDRAWPARAMS(ctypes.Structure):
                        pass

                    _TEMP__IMAGELISTDRAWPARAMS = [
                        ('cbSize', DWORD),
                        ('himl', HIMAGELIST),
                        ('i', INT),
                        ('hdcDst', HDC),
                        ('x', INT),
                        ('y', INT),
                        ('cx', INT),
                        ('cy', INT),
                        ('xBitmap', INT), # x offest from the upperleft of bitmap
                        ('yBitmap', INT), # y offset from the upperleft of bitmap
                        ('rgbBk', COLORREF),
                        ('rgbFg', COLORREF),
                        ('fStyle', UINT),
                        ('dwRop', DWORD),

                    ]

                    if _WIN32_IE >= 0x0501:
                        _TEMP__IMAGELISTDRAWPARAMS += [
                            ('fState', DWORD),
                            ('Frame', DWORD),
                            ('crEffect', COLORREF)
                        ]
                    # END IF

                    _IMAGELISTDRAWPARAMS._fields_ = _TEMP__IMAGELISTDRAWPARAMS

                    IMAGELISTDRAWPARAMS = _IMAGELISTDRAWPARAMS
                    LPIMAGELISTDRAWPARAMS = POINTER(_IMAGELISTDRAWPARAMS)


                    def IMAGELISTDRAWPARAMS_V3_SIZE():
                        return CCSIZEOF_STRUCT(
                            IMAGELISTDRAWPARAMS,
                            IMAGELISTDRAWPARAMS.dwRop
                        )
                # END IF

                ILC_MASK = 0x00000001
                ILC_COLOR = 0x00000000
                ILC_COLORDDB = 0x000000FE
                ILC_COLOR4 = 0x00000004
                ILC_COLOR8 = 0x00000008
                ILC_COLOR16 = 0x00000010
                ILC_COLOR24 = 0x00000018
                ILC_COLOR32 = 0x00000020
                ILC_PALETTE = 0x00000800

                if NTDDI_VERSION >= NTDDI_WINXP:
                    ILC_MIRROR = 0x00002000
                    ILC_PERITEMMIRROR = 0x00008000
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    ILC_ORIGINALSIZE = 0x00010000
                    ILC_HIGHQUALITYSCALE = 0x00020000
                # END IF

                comctl32 = ctypes.windll.ComCtl32
                # WINCOMMCTRLAPI HIMAGELIST  WINAPI ImageList_Create(INT cx, INT cy, UINT flags, INT cInitial, INT cGrow);
                ImageList_Create = comctl32.ImageList_Create
                ImageList_Create.restype = HIMAGELIST
                # WINCOMMCTRLAPI BOOL        WINAPI ImageList_Destroy(_In_opt_ HIMAGELIST himl);
                ImageList_Destroy = comctl32.ImageList_Destroy
                ImageList_Destroy.restype = BOOL
                # WINCOMMCTRLAPI INT         WINAPI ImageList_GetImageCount(_In_ HIMAGELIST himl);
                ImageList_GetImageCount = comctl32.ImageList_GetImageCount
                ImageList_GetImageCount.restype = INT
                # WINCOMMCTRLAPI BOOL        WINAPI ImageList_SetImageCount(_In_ HIMAGELIST himl, _In_ UINT uNewCount);
                ImageList_SetImageCount = comctl32.ImageList_SetImageCount
                ImageList_SetImageCount.restype = BOOL
                # WINCOMMCTRLAPI INT         WINAPI ImageList_Add(_In_ HIMAGELIST himl, _In_ HBITMAP hbmImage, _In_opt_ HBITMAP hbmMask);
                ImageList_Add = comctl32.ImageList_Add
                ImageList_Add.restype = INT
                # WINCOMMCTRLAPI INT         WINAPI ImageList_ReplaceIcon(_In_ HIMAGELIST himl, _In_ INT i, _In_ HICON hicon);
                ImageList_ReplaceIcon = comctl32.ImageList_ReplaceIcon
                ImageList_ReplaceIcon.restype = INT
                # WINCOMMCTRLAPI COLORREF    WINAPI ImageList_SetBkColor(_In_ HIMAGELIST himl, _In_ COLORREF clrBk);
                ImageList_SetBkColor = comctl32.ImageList_SetBkColor
                ImageList_SetBkColor.restype = COLORREF
                # WINCOMMCTRLAPI COLORREF    WINAPI ImageList_GetBkColor(_In_ HIMAGELIST himl);
                ImageList_GetBkColor = comctl32.ImageList_GetBkColor
                ImageList_GetBkColor.restype = COLORREF
                # WINCOMMCTRLAPI BOOL        WINAPI ImageList_SetOverlayImage(_In_ HIMAGELIST himl, _In_ INT iImage, _In_ INT iOverlay);
                ImageList_SetOverlayImage = comctl32.ImageList_SetOverlayImage
                ImageList_SetOverlayImage.restype = BOOL


                def ImageList_AddIcon(himl, hicon):
                    return ImageList_ReplaceIcon(himl, - 1, hicon)


                ILD_NORMAL = 0x00000000
                ILD_TRANSPARENT = 0x00000001
                ILD_MASK = 0x00000010
                ILD_IMAGE = 0x00000020
                ILD_ROP = 0x00000040
                ILD_BLEND25 = 0x00000002
                ILD_BLEND50 = 0x00000004
                ILD_OVERLAYMASK = 0x00000F00


                def INDEXTOOVERLAYMASK(i):
                    return i << 8


                ILD_PRESERVEALPHA = 0x00001000
                ILD_SCALE = 0x00002000
                ILD_DPISCALE = 0x00004000

                if NTDDI_VERSION >= NTDDI_VISTA:
                    ILD_ASYNC = 0x00008000
                # END IF
                ILD_SELECTED = ILD_BLEND50
                ILD_FOCUS = ILD_BLEND25
                ILD_BLEND = ILD_BLEND50
                CLR_HILIGHT = CLR_DEFAULT
                ILS_NORMAL = 0x00000000
                ILS_GLOW = 0x00000001
                ILS_SHADOW = 0x00000002
                ILS_SATURATE = 0x00000004
                ILS_ALPHA = 0x00000008

                if NTDDI_VERSION >= NTDDI_VISTA:
                    ILGT_NORMAL = 0x00000000
                    ILGT_ASYNC = 0x00000001
                # END IF

                # WINCOMMCTRLAPI BOOL WINAPI ImageList_Draw(_In_ HIMAGELIST himl, _In_ INT i, _In_ HDC hdcDst, _In_ INT x, _In_ INT y, _In_ UINT fStyle);
                ImageList_Draw = comctl32.ImageList_Draw
                ImageList_Draw.restype = BOOL

                if defined(_WIN32):
                    if NTDDI_VERSION >= NTDDI_VISTA:
                        HBITMAP_CALLBACK = (HBITMAP) - 1
                    # END IF

                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_Replace(_In_ HIMAGELIST himl, _In_ INT i, _In_ HBITMAP hbmImage, _In_opt_ HBITMAP hbmMask);
                    ImageList_Replace = comctl32.ImageList_Replace
                    ImageList_Replace.restype = BOOL
                    # WINCOMMCTRLAPI INT         WINAPI ImageList_AddMasked(_In_ HIMAGELIST himl, _In_ HBITMAP hbmImage, _In_ COLORREF crMask);
                    ImageList_AddMasked = comctl32.ImageList_AddMasked
                    ImageList_AddMasked.restype = INT
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_DrawEx(_In_ HIMAGELIST himl, _In_ INT i, _In_ HDC hdcDst, _In_ INT x, _In_ INT y, _In_ INT dx, _In_ INT dy, _In_ COLORREF rgbBk, _In_ COLORREF rgbFg, _In_ UINT fStyle);
                    ImageList_DrawEx = comctl32.ImageList_DrawEx
                    ImageList_DrawEx.restype = BOOL
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_DrawIndirect(_In_ IMAGELISTDRAWPARAMS* pimldp);
                    ImageList_DrawIndirect = comctl32.ImageList_DrawIndirect
                    ImageList_DrawIndirect.restype = BOOL
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_Remove(_In_ HIMAGELIST himl, _In_ INT i);
                    ImageList_Remove = comctl32.ImageList_Remove
                    ImageList_Remove.restype = BOOL
                    # WINCOMMCTRLAPI HICON       WINAPI ImageList_GetIcon(_In_ HIMAGELIST himl, _In_ INT i, _In_ UINT flags);
                    ImageList_GetIcon = comctl32.ImageList_GetIcon
                    ImageList_GetIcon.restype = HICON
                    # WINCOMMCTRLAPI HIMAGELIST  WINAPI ImageList_LoadImageA(HINSTANCE hi, LPCSTR lpbmp, INT cx, INT cGrow, COLORREF crMask, UINT uType, UINT uFlags);
                    ImageList_LoadImageA = comctl32.ImageList_LoadImageA
                    ImageList_LoadImageA.restype = HIMAGELIST
                    # WINCOMMCTRLAPI HIMAGELIST  WINAPI ImageList_LoadImageW(HINSTANCE hi, LPCWSTR lpbmp, INT cx, INT cGrow, COLORREF crMask, UINT uType, UINT uFlags);
                    ImageList_LoadImageW = comctl32.ImageList_LoadImageW
                    ImageList_LoadImageW.restype = HIMAGELIST

                    if defined(UNICODE):
                        ImageList_LoadImage = ImageList_LoadImageW
                    else:
                        ImageList_LoadImage = ImageList_LoadImageA
                    # END IF

                    ILCF_MOVE = 0x00000000
                    ILCF_SWAP = 0x00000001
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_Copy(_In_ HIMAGELIST himlDst, _In_ INT iDst, _In_ HIMAGELIST himlSrc, _In_ INT iSrc, _In_ UINT uFlags);
                    ImageList_Copy = comctl32.ImageList_Copy
                    ImageList_Copy.restype = BOOL
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_BeginDrag(_In_ HIMAGELIST himlTrack, _In_ INT iTrack, _In_ INT dxHotspot, _In_ INT dyHotspot);
                    ImageList_BeginDrag = comctl32.ImageList_BeginDrag
                    ImageList_BeginDrag.restype = BOOL
                    # WINCOMMCTRLAPI VOID        WINAPI ImageList_EndDrag(VOID);
                    ImageList_EndDrag = comctl32.ImageList_EndDrag
                    ImageList_EndDrag.restype = VOID
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_DragEnter(HWND hwndLock, INT x, INT y);
                    ImageList_DragEnter = comctl32.ImageList_DragEnter
                    ImageList_DragEnter.restype = BOOL
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_DragLeave(HWND hwndLock);
                    ImageList_DragLeave = comctl32.ImageList_DragLeave
                    ImageList_DragLeave.restype = BOOL
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_DragMove(INT x, INT y);
                    ImageList_DragMove = comctl32.ImageList_DragMove
                    ImageList_DragMove.restype = BOOL
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_SetDragCursorImage(_In_ HIMAGELIST himlDrag, _In_ INT iDrag, _In_ INT dxHotspot, _In_ INT dyHotspot);
                    ImageList_SetDragCursorImage = comctl32.ImageList_SetDragCursorImage
                    ImageList_SetDragCursorImage.restype = BOOL
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_DragShowNolock(BOOL fShow);
                    ImageList_DragShowNolock = comctl32.ImageList_DragShowNolock
                    ImageList_DragShowNolock.restype = BOOL


                    def ImageList_RemoveAll(himl):
                        return ImageList_Remove(himl, - 1)


                    def ImageList_ExtractIcon(hi, himl, i):
                        return ImageList_GetIcon(himl, i, 0)


                    def ImageList_LoadBitmap(hi, lpbmp, cx, cGrow, crMask):
                        return ImageList_LoadImage(hi, lpbmp, cx, cGrow, crMask, IMAGE_BITMAP, 0)

                    class IStream(ctypes.Structure):
                        pass

                    # WINCOMMCTRLAPI HIMAGELIST  WINAPI ImageList_Read(_In_ struct IStream *pstm);
                    ImageList_Read = comctl32.ImageList_Read
                    ImageList_Read.restype = HIMAGELIST
                    # WINCOMMCTRLAPI BOOL        WINAPI ImageList_Write(_In_ HIMAGELIST himl, _In_ struct IStream *pstm);
                    ImageList_Write = comctl32.ImageList_Write
                    ImageList_Write.restype = BOOL

                    if NTDDI_VERSION >= NTDDI_WINXP:
                        ILP_NORMAL = 0
                        ILP_DOWNLEVEL = 1
                    # END IF

                    if not defined(IMAGEINFO):
                        class _IMAGEINFO(ctypes.Structure):
                            pass


                        _IMAGEINFO._fields_ = [
                            ('hbmImage', HBITMAP),
                            ('hbmMask', HBITMAP),
                            ('Unused1', INT),
                            ('Unused2', INT),
                            ('rcImage', RECT),
                        ]
                        IMAGEINFO = _IMAGEINFO
                        LPIMAGEINFO = POINTER(_IMAGEINFO)
                    # END IF

                    # _Success_(return) WINCOMMCTRLAPI BOOL        WINAPI ImageList_GetIconSize(_In_ HIMAGELIST himl, _Out_opt_ int *cx, _Out_opt_ int *cy);
                    ImageList_GetIconSize = comctl32.ImageList_GetIconSize
                    ImageList_GetIconSize.restype = BOOL
                    # _Success_(return) WINCOMMCTRLAPI BOOL        WINAPI ImageList_SetIconSize(_In_ HIMAGELIST himl, _In_ int cx, _In_ int cy);
                    ImageList_SetIconSize = comctl32.ImageList_SetIconSize
                    ImageList_SetIconSize.restype = BOOL
                    # _Success_(return) WINCOMMCTRLAPI BOOL        WINAPI ImageList_GetImageInfo(_In_ HIMAGELIST himl, _In_ int i, _Out_ IMAGEINFO *pImageInfo);
                    ImageList_GetImageInfo = comctl32.ImageList_GetImageInfo
                    ImageList_GetImageInfo.restype = BOOL
                    # WINCOMMCTRLAPI HIMAGELIST  WINAPI ImageList_Merge(_In_ HIMAGELIST himl1, _In_ INT i1, _In_ HIMAGELIST himl2, _In_ INT i2, _In_ INT dx, _In_ INT dy);
                    ImageList_Merge = comctl32.ImageList_Merge
                    ImageList_Merge.restype = HIMAGELIST
                    # WINCOMMCTRLAPI HIMAGELIST  WINAPI ImageList_Duplicate(_In_ HIMAGELIST himl);
                    ImageList_Duplicate = comctl32.ImageList_Duplicate
                    ImageList_Duplicate.restype = HIMAGELIST
                # END IF

                if NTDDI_VERSION >= NTDDI_WINXP:
                    if defined(__cplusplus):
                        pass
                    else:
                        def IImageListToHIMAGELIST(himl):
                            return HIMAGELIST(himl)
                    # END IF
                # END IF
            # END IF

            if not defined(NOHEADER):
                if defined(_WIN32):
                    WC_HEADERA = "SysHeader32"
                    WC_HEADERW = "SysHeader32"

                    if defined(UNICODE):
                        WC_HEADER = WC_HEADERW
                    else:
                        WC_HEADER = WC_HEADERA
                    # END IF
                else:
                    WC_HEADER = "SysHeader"
                # END IF

                HDS_HORZ = 0x0000
                HDS_BUTTONS = 0x0002
                HDS_HOTTRACK = 0x0004
                HDS_HIDDEN = 0x0008
                HDS_DRAGDROP = 0x0040
                HDS_FULLDRAG = 0x0080
                HDS_FILTERBAR = 0x0100

                if NTDDI_VERSION >= NTDDI_WINXP:
                    HDS_FLAT = 0x0200
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    HDS_CHECKBOXES = 0x0400
                    HDS_NOSIZING = 0x0800
                    HDS_OVERFLOW = 0x1000
                # END IF

                HDFT_ISSTRING = 0x0000
                HDFT_ISNUMBER = 0x0001
                HDFT_ISDATE = 0x0002
                HDFT_HASNOVALUE = 0x8000


                class _HD_TEXTFILTERA(ctypes.Structure):
                    pass


                _HD_TEXTFILTERA._fields_ = [
                    ('pszText', LPSTR), # [in] pointer to the buffer containing the filter (ANSI)
                    ('cchTextMax', INT), # [in] max size of buffer/edit control buffer
                ]
                HD_TEXTFILTERA = _HD_TEXTFILTERA
                LPHD_TEXTFILTERA = POINTER(_HD_TEXTFILTERA)


                class _HD_TEXTFILTERW(ctypes.Structure):
                    pass


                _HD_TEXTFILTERW._fields_ = [

                    # [in] pointer to the buffer contiaining the filter
                    # (UNICODE)
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT), # [in] max size of buffer/edit control buffer
                ]
                HD_TEXTFILTERW = _HD_TEXTFILTERW
                LPHD_TEXTFILTERW = POINTER(_HD_TEXTFILTERW)


                if defined(UNICODE):
                    HD_TEXTFILTER = HD_TEXTFILTERW
                    HDTEXTFILTER = HD_TEXTFILTERW
                    LPHD_TEXTFILTER = LPHD_TEXTFILTERW
                    LPHDTEXTFILTER = LPHD_TEXTFILTERW
                else:
                    HD_TEXTFILTER = HD_TEXTFILTERA
                    HDTEXTFILTER = HD_TEXTFILTERA
                    LPHD_TEXTFILTER = LPHD_TEXTFILTERA
                    LPHDTEXTFILTER = LPHD_TEXTFILTERA
                # END IF

                class _HD_ITEMA(ctypes.Structure):
                    pass

                _TEMP__HD_ITEMA = [
                    ('mask', UINT),
                    ('cxy', INT),
                    ('pszText', LPSTR),
                    ('hbm', HBITMAP),
                    ('cchTextMax', INT),
                    ('fmt', INT),
                    ('lParam', LPARAM),
                    ('iImage', INT), # index of bitmap in ImageList
                    ('iOrder', INT), # where to draw this item
                    ('type', UINT), # [in] filter type (defined what pvFilter is a pointer to)
                    ('pvFilter', POINTER(VOID)), # [in] filter data see above

                ]



                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP__HD_ITEMA += [('state', UINT)]
                # END IF

                _HD_ITEMA._fields_ = _TEMP__HD_ITEMA
                HDITEMA = _HD_ITEMA
                LPHDITEMA = POINTER(_HD_ITEMA)


                def HDITEMA_V1_SIZE(lParam):
                    return CCSIZEOF_STRUCT(HDITEMA, lParam)


                def HDITEMW_V1_SIZE(lParam):
                    return CCSIZEOF_STRUCT(HDITEMW, lParam)


                class _HD_ITEMW(ctypes.Structure):
                    pass

                _TEMP__HD_ITEMW = [
                    ('mask', UINT),
                    ('cxy', INT),
                    ('pszText', LPWSTR),
                    ('hbm', HBITMAP),
                    ('cchTextMax', INT),
                    ('fmt', INT),
                    ('lParam', LPARAM),
                    ('iImage', INT), # index of bitmap in ImageList
                    ('iOrder', INT),
                    ('type', UINT), # [in] filter type (defined what pvFilter is a pointer to)
                    ('pvFilter', POINTER(VOID)), # [in] fillter data see above
                ]

                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP__HD_ITEMW += [('state', UINT)]
                # END IF

                _HD_ITEMW._fields_ = _TEMP__HD_ITEMW
                HDITEMW = _HD_ITEMW
                LPHDITEMW = POINTER(_HD_ITEMW)

                if defined(UNICODE):
                    HDITEM = HDITEMW
                    LPHDITEM = LPHDITEMW
                    HDITEM_V1_SIZE = HDITEMW_V1_SIZE
                else:
                    HDITEM = HDITEMA
                    LPHDITEM = LPHDITEMA
                    HDITEM_V1_SIZE = HDITEMA_V1_SIZE
                # END IF

                HD_ITEMA = HDITEMA
                HD_ITEMW = HDITEMW
                HD_ITEM = HDITEM

                HDI_WIDTH = 0x0001
                HDI_HEIGHT = HDI_WIDTH
                HDI_TEXT = 0x0002
                HDI_FORMAT = 0x0004
                HDI_LPARAM = 0x0008
                HDI_BITMAP = 0x0010
                HDI_IMAGE = 0x0020
                HDI_DI_SETITEM = 0x0040
                HDI_ORDER = 0x0080
                HDI_FILTER = 0x0100

                if NTDDI_VERSION >= NTDDI_VISTA:
                    HDI_STATE = 0x0200
                # END IF

                # HDF_ flags are shared with the listview control
                # (LVCFMT_ flags)
                HDF_LEFT = 0x0000
                HDF_RIGHT = 0x0001
                HDF_CENTER = 0x0002
                HDF_JUSTIFYMASK = 0x0003
                HDF_RTLREADING = 0x0004
                HDF_BITMAP = 0x2000
                HDF_STRING = 0x4000
                HDF_OWNERDRAW = 0x8000
                HDF_IMAGE = 0x0800
                HDF_BITMAP_ON_RIGHT = 0x1000

                if NTDDI_VERSION >= NTDDI_WINXP:
                    HDF_SORTUP = 0x0400
                    HDF_SORTDOWN = 0x0200
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    HDF_CHECKBOX = 0x0040
                    HDF_CHECKED = 0x0080
                    HDF_FIXEDWIDTH = 0x0100
                    HDF_SPLITBUTTON = 0x1000000
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    HDIS_FOCUSED = 0x00000001
                # END IF
                HDM_GETITEMCOUNT = HDM_FIRST + 0


                def Header_GetItemCount(hwndHD):
                    return SNDMSG(hwndHD, HDM_GETITEMCOUNT, 0, 0)

                HDM_INSERTITEMA = HDM_FIRST + 1
                HDM_INSERTITEMW = HDM_FIRST + 10

                if defined(UNICODE):
                    HDM_INSERTITEM = HDM_INSERTITEMW
                else:
                    HDM_INSERTITEM = HDM_INSERTITEMA
                # END IF


                def Header_InsertItem(hwndHD, i, phdi):
                    return SNDMSG(hwndHD, HDM_INSERTITEM, i, ctypes.byref(phdi))


                HDM_DELETEITEM = HDM_FIRST + 2


                def Header_DeleteItem(hwndHD, i):
                    return SNDMSG(hwndHD, HDM_DELETEITEM, i, 0)


                HDM_GETITEMA = HDM_FIRST + 3
                HDM_GETITEMW = HDM_FIRST + 11

                if defined(UNICODE):
                    HDM_GETITEM = HDM_GETITEMW
                else:
                    HDM_GETITEM = HDM_GETITEMA
                # END IF


                def Header_GetItem(hwndHD, i, phdi):
                    return SNDMSG(hwndHD, HDM_GETITEM, i, ctypes.byref(phdi))


                HDM_SETITEMA = HDM_FIRST + 4
                HDM_SETITEMW = HDM_FIRST + 12

                if defined(UNICODE):
                    HDM_SETITEM = HDM_SETITEMW
                else:
                    HDM_SETITEM = HDM_SETITEMA
                # END IF


                def Header_SetItem(hwndHD, i, phdi):
                    return SNDMSG(hwndHD, HDM_SETITEM, i, ctypes.byref(phdi))


                class _HD_LAYOUT(ctypes.Structure):
                    pass


                _HD_LAYOUT._fields_ = [
                    ('prc', POINTER(RECT)),
                    ('pwpos', POINTER(WINDOWPOS)),
                ]
                HDLAYOUT = _HD_LAYOUT
                LPHDLAYOUT = POINTER(_HD_LAYOUT)

                HD_LAYOUT = HDLAYOUT
                HDM_LAYOUT = HDM_FIRST + 5


                def Header_Layout(hwndHD, playout):
                    return SNDMSG(hwndHD, HDM_LAYOUT, 0, ctypes.byref(playout))


                HHT_NOWHERE = 0x0001
                HHT_ONHEADER = 0x0002
                HHT_ONDIVIDER = 0x0004
                HHT_ONDIVOPEN = 0x0008
                HHT_ONFILTER = 0x0010
                HHT_ONFILTERBUTTON = 0x0020
                HHT_ABOVE = 0x0100
                HHT_BELOW = 0x0200
                HHT_TORIGHT = 0x0400
                HHT_TOLEFT = 0x0800

                if NTDDI_VERSION >= NTDDI_VISTA:
                    HHT_ONITEMSTATEICON = 0x1000
                    HHT_ONDROPDOWN = 0x2000
                    HHT_ONOVERFLOW = 0x4000
                # END IF


                class _HD_HITTESTINFO(ctypes.Structure):
                    pass


                _HD_HITTESTINFO._fields_ = [
                    ('pt', POINT),
                    ('flags', UINT),
                    ('iItem', INT),
                ]
                HDHITTESTINFO = _HD_HITTESTINFO
                LPHDHITTESTINFO = POINTER(_HD_HITTESTINFO)

                HD_HITTESTINFO = HDHITTESTINFO

                HDSIL_NORMAL = 0
                HDSIL_STATE = 1
                HDM_HITTEST = HDM_FIRST + 6
                HDM_GETITEMRECT = HDM_FIRST + 7


                def Header_GetItemRect(hwnd, iItem, lprc):
                    return SNDMSG(hwnd, HDM_GETITEMRECT, iItem, lprc)


                HDM_SETIMAGELIST = HDM_FIRST + 8


                def Header_SetImageList(hwnd, himl):
                    return SNDMSG(hwnd, HDM_SETIMAGELIST, HDSIL_NORMAL, himl)


                def Header_SetStateImageList(hwnd, himl):
                    return SNDMSG(hwnd, HDM_SETIMAGELIST, HDSIL_STATE, himl)


                HDM_GETIMAGELIST = HDM_FIRST + 9


                def Header_GetImageList(hwnd):
                    return SNDMSG(hwnd, HDM_GETIMAGELIST, HDSIL_NORMAL, 0)


                def Header_GetStateImageList(hwnd):
                    return SNDMSG(hwnd, HDM_GETIMAGELIST, HDSIL_STATE, 0)
                HDM_ORDERTOINDEX = HDM_FIRST + 15


                def Header_OrderToIndex(hwnd, i):
                    return SNDMSG(hwnd, HDM_ORDERTOINDEX, WPARAMi, 0)
                HDM_CREATEDRAGIMAGE = HDM_FIRST + 16


                def Header_CreateDragImage(hwnd, i):
                    return SNDMSG(hwnd, HDM_CREATEDRAGIMAGE, WPARAMi, 0)
                HDM_GETORDERARRAY = HDM_FIRST + 17


                def Header_GetOrderArray(hwnd, iCount, lpi):
                    return SNDMSG(hwnd, HDM_GETORDERARRAY, iCount, lpi)


                HDM_SETORDERARRAY = HDM_FIRST + 18


                def Header_SetOrderArray(hwnd, iCount, lpi):
                    return SNDMSG(hwnd, HDM_SETORDERARRAY, iCount, lpi)

                # lparam = INT array of size HDM_GETITEMCOUNT
                # the array specifies the order that all items should be
                # displayed.
                # e.g. { 2, 0, 1}
                # says the index 2 item should be shown in the 0ths position
                # index 0 should be shown in the 1st position
                # index 1 should be shown in the 2nd position
                HDM_SETHOTDIVIDER = HDM_FIRST + 19


                def Header_SetHotDivider(hwnd, fPos, dw):
                    return SNDMSG(hwnd, HDM_SETHOTDIVIDER, fPos, dw)

                # convenience message for external dragdrop
                # wParam = BOOL specifying whether the lParam is a dwPos of
                # the cursor
                # position or the index of which divider to hotlight
                # lParam = depends on wParam
                # ( - 1 and wParm = FALSE turns off hotlight)
                HDM_SETBITMAPMARGIN = HDM_FIRST + 20


                def Header_SetBitmapMargin(hwnd, iWidth):
                    return SNDMSG(hwnd, HDM_SETBITMAPMARGIN, iWidth, 0)


                HDM_GETBITMAPMARGIN = HDM_FIRST + 21


                def Header_GetBitmapMargin(hwnd):
                    return SNDMSG(hwnd, HDM_GETBITMAPMARGIN, 0, 0)


                HDM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT


                def Header_SetUnicodeFormat(hwnd, fUnicode):
                    return SNDMSG(hwnd, HDM_SETUNICODEFORMAT, fUnicode, 0)


                HDM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT


                def Header_GetUnicodeFormat(hwnd):
                    return SNDMSG(hwnd, HDM_GETUNICODEFORMAT, 0, 0)


                HDM_SETFILTERCHANGETIMEOUT = HDM_FIRST + 22


                def Header_SetFilterChangeTimeout(hwnd, i):
                    return SNDMSG(hwnd, HDM_SETFILTERCHANGETIMEOUT, 0, i)


                HDM_EDITFILTER = HDM_FIRST + 23


                def Header_EditFilter(hwnd, i, fDiscardChanges):
                    return SNDMSG(hwnd, HDM_EDITFILTER, i, fDiscardChanges, 0)

                # Clear filter takes - 1 as a column value to indicate that all
                # the filter should be cleared. When this happens you will
                # only receive a single filter changed notification.
                HDM_CLEARFILTER = HDM_FIRST + 24


                def Header_ClearFilter(hwnd, i):
                    return SNDMSG(hwnd, HDM_CLEARFILTER, i, 0)


                def Header_ClearAllFilters(hwnd):
                    return SNDMSG(hwnd, HDM_CLEARFILTER, -1, 0)

                if _WIN32_IE >= 0x0600:
                    HDM_TRANSLATEACCELERATOR = CCM_TRANSLATEACCELERATOR
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    HDM_GETITEMDROPDOWNRECT = HDM_FIRST + 25


                    def Header_GetItemDropDownRect(hwnd, iItem, lprc):
                        return SNDMSG(hwnd, HDM_GETITEMDROPDOWNRECT, iItem, lprc)


                    HDM_GETOVERFLOWRECT = HDM_FIRST + 26


                    def Header_GetOverflowRect(hwnd, lprc):
                        return SNDMSG(hwnd, HDM_GETOVERFLOWRECT, 0, lprc)


                    HDM_GETFOCUSEDITEM = HDM_FIRST + 27


                    def Header_GetFocusedItem(hwnd):
                        return SNDMSG(hwnd, HDM_GETFOCUSEDITEM, 0, 0)


                    HDM_SETFOCUSEDITEM = HDM_FIRST + 28


                    def Header_SetFocusedItem(hwnd, iItem):
                        return SNDMSG(hwnd, HDM_SETFOCUSEDITEM, 0, iItem)


                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
                HDN_ITEMCHANGINGA = HDN_FIRST - 0
                HDN_ITEMCHANGINGW = HDN_FIRST - 20
                HDN_ITEMCHANGEDA = HDN_FIRST - 1
                HDN_ITEMCHANGEDW = HDN_FIRST - 21
                HDN_ITEMCLICKA = HDN_FIRST - 2
                HDN_ITEMCLICKW = HDN_FIRST - 22
                HDN_ITEMDBLCLICKA = HDN_FIRST - 3
                HDN_ITEMDBLCLICKW = HDN_FIRST - 23
                HDN_DIVIDERDBLCLICKA = HDN_FIRST - 5
                HDN_DIVIDERDBLCLICKW = HDN_FIRST - 25
                HDN_BEGINTRACKA = HDN_FIRST - 6
                HDN_BEGINTRACKW = HDN_FIRST - 26
                HDN_ENDTRACKA = HDN_FIRST - 7
                HDN_ENDTRACKW = HDN_FIRST - 27
                HDN_TRACKA = HDN_FIRST - 8
                HDN_TRACKW = HDN_FIRST - 28
                HDN_GETDISPINFOA = HDN_FIRST - 9
                HDN_GETDISPINFOW = HDN_FIRST - 29
                HDN_BEGINDRAG = HDN_FIRST - 10
                HDN_ENDDRAG = HDN_FIRST - 11
                HDN_FILTERCHANGE = HDN_FIRST - 12
                HDN_FILTERBTNCLICK = HDN_FIRST - 13

                if _WIN32_IE >= 0x0600:
                    HDN_BEGINFILTEREDIT = HDN_FIRST - 14
                    HDN_ENDFILTEREDIT = HDN_FIRST - 15
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    HDN_ITEMSTATEICONCLICK = HDN_FIRST - 16
                    HDN_ITEMKEYDOWN = HDN_FIRST - 17
                    HDN_DROPDOWN = HDN_FIRST - 18
                    HDN_OVERFLOWCLICK = HDN_FIRST - 19
                # END IF

                if defined(UNICODE):
                    HDN_ITEMCHANGING = HDN_ITEMCHANGINGW
                    HDN_ITEMCHANGED = HDN_ITEMCHANGEDW
                    HDN_ITEMCLICK = HDN_ITEMCLICKW
                    HDN_ITEMDBLCLICK = HDN_ITEMDBLCLICKW
                    HDN_DIVIDERDBLCLICK = HDN_DIVIDERDBLCLICKW
                    HDN_BEGINTRACK = HDN_BEGINTRACKW
                    HDN_ENDTRACK = HDN_ENDTRACKW
                    HDN_TRACK = HDN_TRACKW
                    HDN_GETDISPINFO = HDN_GETDISPINFOW
                else:
                    HDN_ITEMCHANGING = HDN_ITEMCHANGINGA
                    HDN_ITEMCHANGED = HDN_ITEMCHANGEDA
                    HDN_ITEMCLICK = HDN_ITEMCLICKA
                    HDN_ITEMDBLCLICK = HDN_ITEMDBLCLICKA
                    HDN_DIVIDERDBLCLICK = HDN_DIVIDERDBLCLICKA
                    HDN_BEGINTRACK = HDN_BEGINTRACKA
                    HDN_ENDTRACK = HDN_ENDTRACKA
                    HDN_TRACK = HDN_TRACKA
                    HDN_GETDISPINFO = HDN_GETDISPINFOA
                # END IF

                class tagNMHEADERA(ctypes.Structure):
                    pass


                tagNMHEADERA._fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('iButton', INT),
                    ('pitem', POINTER(HDITEMA)),
                ]
                NMHEADERA = tagNMHEADERA
                LPNMHEADERA = POINTER(tagNMHEADERA)


                class tagNMHEADERW(ctypes.Structure):
                    pass


                tagNMHEADERW._fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('iButton', INT),
                    ('pitem', POINTER(HDITEMW)),
                ]
                NMHEADERW = tagNMHEADERW
                LPNMHEADERW = POINTER(tagNMHEADERW)

                if defined(UNICODE):
                    NMHEADER = NMHEADERW
                    LPNMHEADER = LPNMHEADERW
                else:
                    NMHEADER = NMHEADERA
                    LPNMHEADER = LPNMHEADERA
                # END IF

                HD_NOTIFYA = NMHEADERA
                HD_NOTIFYW = NMHEADERW
                HD_NOTIFY = NMHEADER


                class tagNMHDDISPINFOW(ctypes.Structure):
                    pass


                tagNMHDDISPINFOW._fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('mask', UINT),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('lParam', LPARAM),
                ]
                NMHDDISPINFOW = tagNMHDDISPINFOW
                LPNMHDDISPINFOW = POINTER(tagNMHDDISPINFOW)


                class tagNMHDDISPINFOA(ctypes.Structure):
                    pass


                tagNMHDDISPINFOA._fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('mask', UINT),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('lParam', LPARAM),
                ]
                NMHDDISPINFOA = tagNMHDDISPINFOA
                LPNMHDDISPINFOA = POINTER(tagNMHDDISPINFOA)

                if defined(UNICODE):
                    NMHDDISPINFO = NMHDDISPINFOW
                    LPNMHDDISPINFO = LPNMHDDISPINFOW
                else:
                    NMHDDISPINFO = NMHDDISPINFOA
                    LPNMHDDISPINFO = LPNMHDDISPINFOA
                # END IF


                class tagNMHDFILTERBTNCLICK(ctypes.Structure):
                    pass


                tagNMHDFILTERBTNCLICK._fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('rc', RECT),
                ]
                NMHDFILTERBTNCLICK = tagNMHDFILTERBTNCLICK
                LPNMHDFILTERBTNCLICK = POINTER(tagNMHDFILTERBTNCLICK)
            # END IF   NOHEADER

            # == == == TOOLBAR CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == ==

            if not defined(NOTOOLBAR):
                if defined(_WIN32):
                    TOOLBARCLASSNAMEW = "ToolbarWindow32"
                    TOOLBARCLASSNAMEA = "ToolbarWindow32"

                    if defined(UNICODE):
                        TOOLBARCLASSNAME = TOOLBARCLASSNAMEW
                    else:
                        TOOLBARCLASSNAME = TOOLBARCLASSNAMEA
                    # END IF
                else:
                    TOOLBARCLASSNAME = "ToolbarWindow"
                # END IF
                class _TBBUTTON(ctypes.Structure):
                    pass


                _TBBUTTON._fields_ = [
                    ('iBitmap', INT),
                    ('idCommand', INT),
                    ('fsState', BYTE),
                    ('fsStyle', BYTE),
                    ('bReserved', BYTE * 6) if defined(_WIN64) else ('bReserved', BYTE * 2), # padding for alignment
                    ('dwData', DWORD_PTR),
                    ('iString', INT_PTR),
                ]
                TBBUTTON = _TBBUTTON
                PTBBUTTON = POINTER(_TBBUTTON)
                LPTBBUTTON = POINTER(_TBBUTTON)

                LPCTBBUTTON = POINTER(TBBUTTON)


                class _COLORMAP(ctypes.Structure):
                    pass


                _COLORMAP._fields_ = [
                    ('from', COLORREF),
                    ('to', COLORREF),
                ]
                COLORMAP = _COLORMAP
                LPCOLORMAP = POINTER(_COLORMAP)

                comctl32 = ctypes.windll.ComCtl32
                # WINCOMMCTRLAPI HWND WINAPI CreateToolbarEx(HWND hwnd, DWORD ws, UINT wID, INT nBitmaps,
                # HINSTANCE hBMInst, UINT_PTR wBMID, LPCTBBUTTON lpButtons,
                # INT iNumButtons, INT dxButton, INT dyButton,
                # INT dxBitmap, INT dyBitmap, UINT uStructSize);
                CreateToolbarEx = comctl32.CreateToolbarEx
                CreateToolbarEx.restype = HWND
                # WINCOMMCTRLAPI HBITMAP WINAPI CreateMappedBitmap(HINSTANCE hInstance, INT_PTR idBitmap,
                # UINT wFlags, _In_opt_ LPCOLORMAP lpColorMap,
                # INT iNumMaps);
                CreateMappedBitmap = comctl32.CreateMappedBitmap
                CreateMappedBitmap.restype = HBITMAP
                CMB_MASKED = 0x02
                TBSTATE_CHECKED = 0x01
                TBSTATE_PRESSED = 0x02
                TBSTATE_ENABLED = 0x04
                TBSTATE_HIDDEN = 0x08
                TBSTATE_INDETERMINATE = 0x10
                TBSTATE_WRAP = 0x20
                TBSTATE_ELLIPSES = 0x40
                TBSTATE_MARKED = 0x80

                # begin_r_commctrl
                TBSTYLE_BUTTON = 0x0000
                TBSTYLE_SEP = 0x0001
                TBSTYLE_CHECK = 0x0002
                TBSTYLE_GROUP = 0x0004
                TBSTYLE_CHECKGROUP = TBSTYLE_GROUP | TBSTYLE_CHECK
                TBSTYLE_DROPDOWN = 0x0008
                TBSTYLE_AUTOSIZE = 0x0010
                TBSTYLE_NOPREFIX = 0x0020
                TBSTYLE_TOOLTIPS = 0x0100
                TBSTYLE_WRAPABLE = 0x0200
                TBSTYLE_ALTDRAG = 0x0400
                TBSTYLE_FLAT = 0x0800
                TBSTYLE_LIST = 0x1000
                TBSTYLE_CUSTOMERASE = 0x2000
                TBSTYLE_REGISTERDROP = 0x4000
                TBSTYLE_TRANSPARENT = 0x8000

                # end_r_commctrl
                TBSTYLE_EX_DRAWDDARROWS = 0x00000001

                # begin_r_commctrl
                BTNS_BUTTON = TBSTYLE_BUTTON
                BTNS_SEP = TBSTYLE_SEP
                BTNS_CHECK = TBSTYLE_CHECK
                BTNS_GROUP = TBSTYLE_GROUP
                BTNS_CHECKGROUP = TBSTYLE_CHECKGROUP
                BTNS_DROPDOWN = TBSTYLE_DROPDOWN
                BTNS_AUTOSIZE = TBSTYLE_AUTOSIZE
                BTNS_NOPREFIX = TBSTYLE_NOPREFIX
                BTNS_SHOWTEXT = 0x0040
                BTNS_WHOLEDROPDOWN = 0x0080

                # end_r_commctrl
                TBSTYLE_EX_MIXEDBUTTONS = 0x00000008
                TBSTYLE_EX_HIDECLIPPEDBUTTONS = 0x00000010
                TBSTYLE_EX_MULTICOLUMN = 0x00000002
                TBSTYLE_EX_VERTICAL = 0x00000004

                if NTDDI_VERSION >= NTDDI_WINXP:
                    TBSTYLE_EX_DOUBLEBUFFER = 0x00000080
                # END IF

                # Custom Draw Structure
                class _NMTBCUSTOMDRAW(ctypes.Structure):
                    pass


                _TEMP__NMTBCUSTOMDRAW = [
                    ('nmcd', NMCUSTOMDRAW),
                    ('hbrMonoDither', HBRUSH),
                    ('hbrLines', HBRUSH), # For drawing lines on buttons
                    ('hpenLines', HPEN), # For drawing lines on buttons
                    ('clrText', COLORREF), # Color of text
                    ('clrMark', COLORREF), # Color of text bk when marked. (only if TBSTATE_MARKED)
                    ('clrTextHighlight', COLORREF), # Color of text when highlighted
                    ('clrBtnFace', COLORREF), # Background of the button
                    ('clrBtnHighlight', COLORREF), # 3D highlight
                    ('clrHighlightHotTrack', COLORREF), # In conjunction with fHighlightHotTrack
                    ('rcText', RECT), # Rect for text
                    ('nStringBkMode', INT),
                    ('nHLStringBkMode', INT),
                ]


                if NTDDI_VERSION >= NTDDI_WINXP:
                    _TEMP__NMTBCUSTOMDRAW += [('iListGap', INT),]
                # END IF

                _NMTBCUSTOMDRAW._fields_ = _TEMP__NMTBCUSTOMDRAW
                NMTBCUSTOMDRAW = _NMTBCUSTOMDRAW
                LPNMTBCUSTOMDRAW = POINTER(_NMTBCUSTOMDRAW)

                # Toolbar custom draw return flags
                TBCDRF_NOEDGES = 0x00010000
                TBCDRF_HILITEHOTTRACK = 0x00020000
                TBCDRF_NOOFFSET = 0x00040000
                TBCDRF_NOMARK = 0x00080000
                TBCDRF_NOETCHEDEFFECT = 0x00100000
                TBCDRF_BLENDICON = 0x00200000
                TBCDRF_NOBACKGROUND = 0x00400000

                if NTDDI_VERSION >= NTDDI_VISTA:
                    TBCDRF_USECDCOLORS = 0x00800000
                # END IF
                TB_ENABLEBUTTON = WM_USER + 1
                TB_CHECKBUTTON = WM_USER + 2
                TB_PRESSBUTTON = WM_USER + 3
                TB_HIDEBUTTON = WM_USER + 4
                TB_INDETERMINATE = WM_USER + 5
                TB_MARKBUTTON = WM_USER + 6
                TB_ISBUTTONENABLED = WM_USER + 9
                TB_ISBUTTONCHECKED = WM_USER + 10
                TB_ISBUTTONPRESSED = WM_USER + 11
                TB_ISBUTTONHIDDEN = WM_USER + 12
                TB_ISBUTTONINDETERMINATE = WM_USER + 13
                TB_ISBUTTONHIGHLIGHTED = WM_USER + 14
                TB_SETSTATE = WM_USER + 17
                TB_GETSTATE = WM_USER + 18
                TB_ADDBITMAP = WM_USER + 19

                if defined(_WIN32):
                    class tagTBADDBITMAP(ctypes.Structure):
                        pass


                    tagTBADDBITMAP._fields_ = [
                        ('hInst', HINSTANCE),
                        ('nID', UINT_PTR),
                    ]
                    TBADDBITMAP = tagTBADDBITMAP
                    LPTBADDBITMAP = POINTER(tagTBADDBITMAP)

                    HINST_COMMCTRL = -1
                    IDB_STD_SMALL_COLOR = 0
                    IDB_STD_LARGE_COLOR = 1
                    IDB_VIEW_SMALL_COLOR = 4
                    IDB_VIEW_LARGE_COLOR = 5
                    IDB_HIST_SMALL_COLOR = 8
                    IDB_HIST_LARGE_COLOR = 9

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        IDB_HIST_NORMAL = 12
                        IDB_HIST_HOT = 13
                        IDB_HIST_DISABLED = 14
                        IDB_HIST_PRESSED = 15
                    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                    # icon indexes for standard bitmap
                    STD_CUT = 0
                    STD_COPY = 1
                    STD_PASTE = 2
                    STD_UNDO = 3
                    STD_REDOW = 4
                    STD_DELETE = 5
                    STD_FILENEW = 6
                    STD_FILEOPEN = 7
                    STD_FILESAVE = 8
                    STD_PRINTPRE = 9
                    STD_PROPERTIES = 10
                    STD_HELP = 11
                    STD_FIND = 12
                    STD_REPLACE = 13
                    STD_PRINT = 14

                    # icon indexes for standard view bitmap
                    VIEW_LARGEICONS = 0
                    VIEW_SMALLICONS = 1
                    VIEW_LIST = 2
                    VIEW_DETAILS = 3
                    VIEW_SORTNAME = 4
                    VIEW_SORTSIZE = 5
                    VIEW_SORTDATE = 6
                    VIEW_SORTTYPE = 7
                    VIEW_PARENTFOLDER = 8
                    VIEW_NETCONNECT = 9
                    VIEW_NETDISCONNECT = 10
                    VIEW_NEWFOLDER = 11
                    VIEW_VIEWMENU = 12
                    HIST_BACK = 0
                    HIST_FORWARD = 1
                    HIST_FAVORITES = 2
                    HIST_ADDTOFAVORITES = 3
                    HIST_VIEWTREE = 4
                # END IF
                TB_ADDBUTTONSA = WM_USER + 20
                TB_INSERTBUTTONA = WM_USER + 21
                TB_DELETEBUTTON = WM_USER + 22
                TB_GETBUTTON = WM_USER + 23
                TB_BUTTONCOUNT = WM_USER + 24
                TB_COMMANDTOINDEX = WM_USER + 25

                if defined(_WIN32):
                    class tagTBSAVEPARAMSA(ctypes.Structure):
                        pass


                    tagTBSAVEPARAMSA._fields_ = [
                        ('hkr', HKEY),
                        ('pszSubKey', LPCSTR),
                        ('pszValueName', LPCSTR),
                    ]
                    TBSAVEPARAMSA = tagTBSAVEPARAMSA
                    LPTBSAVEPARAMSA = POINTER(tagTBSAVEPARAMSA)


                    class tagTBSAVEPARAMSW(ctypes.Structure):
                        pass


                    tagTBSAVEPARAMSW._fields_ = [
                        ('hkr', HKEY),
                        ('pszSubKey', LPCWSTR),
                        ('pszValueName', LPCWSTR),
                    ]
                    TBSAVEPARAMSW = tagTBSAVEPARAMSW
                    LPTBSAVEPARAMW = POINTER(tagTBSAVEPARAMSW)

                    if defined(UNICODE):
                        TBSAVEPARAMS = TBSAVEPARAMSW
                        LPTBSAVEPARAMS = LPTBSAVEPARAMW
                    else:
                        TBSAVEPARAMS = TBSAVEPARAMSA
                        LPTBSAVEPARAMS = LPTBSAVEPARAMSA
                    # END IF
                # END IF   _WIN32

                TB_SAVERESTOREA = WM_USER + 26
                TB_SAVERESTOREW = WM_USER + 76
                TB_CUSTOMIZE = WM_USER + 27
                TB_ADDSTRINGA = WM_USER + 28
                TB_ADDSTRINGW = WM_USER + 77
                TB_GETITEMRECT = WM_USER + 29
                TB_BUTTONSTRUCTSIZE = WM_USER + 30
                TB_SETBUTTONSIZE = WM_USER + 31
                TB_SETBITMAPSIZE = WM_USER + 32
                TB_AUTOSIZE = WM_USER + 33
                TB_GETTOOLTIPS = WM_USER + 35
                TB_SETTOOLTIPS = WM_USER + 36
                TB_SETPARENT = WM_USER + 37
                TB_SETROWS = WM_USER + 39
                TB_GETROWS = WM_USER + 40
                TB_SETCMDID = WM_USER + 42
                TB_CHANGEBITMAP = WM_USER + 43
                TB_GETBITMAP = WM_USER + 44
                TB_GETBUTTONTEXTA = WM_USER + 45
                TB_GETBUTTONTEXTW = WM_USER + 75
                TB_REPLACEBITMAP = WM_USER + 46
                TB_SETINDENT = WM_USER + 47
                TB_SETIMAGELIST = WM_USER + 48
                TB_GETIMAGELIST = WM_USER + 49
                TB_LOADIMAGES = WM_USER + 50
                TB_GETRECT = WM_USER + 51
                TB_SETHOTIMAGELIST = WM_USER + 52
                TB_GETHOTIMAGELIST = WM_USER + 53
                TB_SETDISABLEDIMAGELIST = WM_USER + 54
                TB_GETDISABLEDIMAGELIST = WM_USER + 55
                TB_SETSTYLE = WM_USER + 56
                TB_GETSTYLE = WM_USER + 57
                TB_GETBUTTONSIZE = WM_USER + 58
                TB_SETBUTTONWIDTH = WM_USER + 59
                TB_SETMAXTEXTROWS = WM_USER + 60
                TB_GETTEXTROWS = WM_USER + 61

                if defined(UNICODE):
                    TB_GETBUTTONTEXT = TB_GETBUTTONTEXTW
                    TB_SAVERESTORE = TB_SAVERESTOREW
                    TB_ADDSTRING = TB_ADDSTRINGW
                else:
                    TB_GETBUTTONTEXT = TB_GETBUTTONTEXTA
                    TB_SAVERESTORE = TB_SAVERESTOREA
                    TB_ADDSTRING = TB_ADDSTRINGA
                # END IF
                TB_GETOBJECT = WM_USER + 62
                TB_GETHOTITEM = WM_USER + 71
                TB_SETHOTITEM = WM_USER + 72
                TB_SETANCHORHIGHLIGHT = WM_USER + 73
                TB_GETANCHORHIGHLIGHT = WM_USER + 74
                TB_MAPACCELERATORA = WM_USER + 78


                class TBINSERTMARK(ctypes.Structure):
                    pass


                TBINSERTMARK._fields_ = [
                    ('iButton', INT),
                    ('dwFlags', DWORD),
                ]
                 LPTBINSERTMARK = POINTER(TBINSERTMARK)

                TBIMHT_AFTER = 0x00000001
                TBIMHT_BACKGROUND = 0x00000002
                TB_GETINSERTMARK = WM_USER + 79
                TB_SETINSERTMARK = WM_USER + 80
                TB_INSERTMARKHITTEST = WM_USER + 81
                TB_MOVEBUTTON = WM_USER + 82
                TB_GETMAXSIZE = WM_USER + 83
                TB_SETEXTENDEDSTYLE = WM_USER + 84
                TB_GETEXTENDEDSTYLE = WM_USER + 85
                TB_GETPADDING = WM_USER + 86
                TB_SETPADDING = WM_USER + 87
                TB_SETINSERTMARKCOLOR = WM_USER + 88
                TB_GETINSERTMARKCOLOR = WM_USER + 89
                TB_SETCOLORSCHEME = CCM_SETCOLORSCHEME
                TB_GETCOLORSCHEME = CCM_GETCOLORSCHEME
                TB_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
                TB_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
                TB_MAPACCELERATORW = WM_USER + 90

                if defined(UNICODE):
                    TB_MAPACCELERATOR = TB_MAPACCELERATORW
                else:
                    TB_MAPACCELERATOR = TB_MAPACCELERATORA
                # END IF

                class TBREPLACEBITMAP(ctypes.Structure):
                    pass


                TBREPLACEBITMAP._fields_ = [
                    ('hInstOld', HINSTANCE),
                    ('nIDOld', UINT_PTR),
                    ('hInstNew', HINSTANCE),
                    ('nIDNew', UINT_PTR),
                    ('nButtons', INT),
                ]
                LPTBREPLACEBITMAP = POINTER(TBREPLACEBITMAP)

                if defined(_WIN32):
                    TBBF_LARGE = 0x0001
                    TB_GETBITMAPFLAGS = WM_USER + 41
                    TBIF_IMAGE = 0x00000001
                    TBIF_TEXT = 0x00000002
                    TBIF_STATE = 0x00000004
                    TBIF_STYLE = 0x00000008
                    TBIF_LPARAM = 0x00000010
                    TBIF_COMMAND = 0x00000020
                    TBIF_SIZE = 0x00000040
                    TBIF_BYINDEX = 0x80000000


                    class TBBUTTONINFOA(ctypes.Structure):
                        pass


                    TBBUTTONINFOA._fields_ = [
                        ('cbSize', UINT),
                        ('dwMask', DWORD),
                        ('idCommand', INT),
                        ('iImage', INT),
                        ('fsState', BYTE),
                        ('fsStyle', BYTE),
                        ('cx', WORD),
                        ('lParam', DWORD_PTR),
                        ('pszText', LPSTR),
                        ('cchText', INT),
                    ]
                    LPTBBUTTONINFOA = POINTER(TBBUTTONINFOA)


                    class TBBUTTONINFOW(ctypes.Structure):
                        pass


                    TBBUTTONINFOW._fields_ = [
                        ('cbSize', UINT),
                        ('dwMask', DWORD),
                        ('idCommand', INT),
                        ('iImage', INT),
                        ('fsState', BYTE),
                        ('fsStyle', BYTE),
                        ('cx', WORD),
                        ('lParam', DWORD_PTR),
                        ('pszText', LPWSTR),
                        ('cchText', INT),
                    ]
                    LPTBBUTTONINFOW = POINTER(TBBUTTONINFOW)

                    if defined(UNICODE):
                        TBBUTTONINFO = TBBUTTONINFOW
                        LPTBBUTTONINFO = LPTBBUTTONINFOW
                    else:
                        TBBUTTONINFO = TBBUTTONINFOA
                        LPTBBUTTONINFO = LPTBBUTTONINFOA
                    # END IF

                    # BUTTONINFO APIs do NOT support the string pool.
                    TB_GETBUTTONINFOW = WM_USER + 63
                    TB_SETBUTTONINFOW = WM_USER + 64
                    TB_GETBUTTONINFOA = WM_USER + 65
                    TB_SETBUTTONINFOA = WM_USER + 66

                    if defined(UNICODE):
                        TB_GETBUTTONINFO = TB_GETBUTTONINFOW
                        TB_SETBUTTONINFO = TB_SETBUTTONINFOW
                    else:
                        TB_GETBUTTONINFO = TB_GETBUTTONINFOA
                        TB_SETBUTTONINFO = TB_SETBUTTONINFOA
                    # END IF

                    TB_INSERTBUTTONW = WM_USER + 67
                    TB_ADDBUTTONSW = WM_USER + 68
                    TB_HITTEST = WM_USER + 69

                    # New post Win95/NT4 for InsertButton and AddButton. if
                    # iString member

                    # is a pointer to a string, it will be handled as a string
                    # like listview

                    # (although LPSTR_TEXTCALLBACK is not supported).

                    if defined(UNICODE):
                        TB_INSERTBUTTON = TB_INSERTBUTTONW
                        TB_ADDBUTTONS = TB_ADDBUTTONSW
                    else:
                        TB_INSERTBUTTON = TB_INSERTBUTTONA
                        TB_ADDBUTTONS = TB_ADDBUTTONSA
                    # END IF

                    TB_SETDRAWTEXTFLAGS = WM_USER + 70
                    TB_GETSTRINGW = WM_USER + 91
                    TB_GETSTRINGA = WM_USER + 92

                    if defined(UNICODE):
                        TB_GETSTRING = TB_GETSTRINGW
                    else:
                        TB_GETSTRING = TB_GETSTRINGA
                    # END IF

                    TB_SETBOUNDINGSIZE = WM_USER + 93
                    TB_SETHOTITEM2 = WM_USER + 94
                    TB_HASACCELERATOR = WM_USER + 95
                    TB_SETLISTGAP = WM_USER + 96
                    TB_GETIMAGELISTCOUNT = WM_USER + 98
                    TB_GETIDEALSIZE = WM_USER + 99

                    # before using WM_USER + 103, recycle old space above
                    # (WM_USER + 97)
                    TB_TRANSLATEACCELERATOR = CCM_TRANSLATEACCELERATOR

                    if NTDDI_VERSION >= NTDDI_WINXP:
                        TBMF_PAD = 0x00000001
                        TBMF_BARPAD = 0x00000002
                        TBMF_BUTTONSPACING = 0x00000004


                        class TBMETRICS(ctypes.Structure):
                            pass


                        TBMETRICS._fields_ = [
                            ('cbSize', UINT),
                            ('dwMask', DWORD),
                            ('cxPad', INT), # PAD
                            ('cyPad', INT),
                            ('cxBarPad', INT), # BARPAD
                            ('cyBarPad', INT),
                            ('cxButtonSpacing', INT), # BUTTONSPACING
                            ('cyButtonSpacing', INT),
                        ]
                        LPTBMETRICS = POINTER(TBMETRICS)
                        TB_GETMETRICS = WM_USER + 101
                        TB_SETMETRICS = WM_USER + 102
                    # END IF

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        TB_GETITEMDROPDOWNRECT = WM_USER + 103
                        TB_SETPRESSEDIMAGELIST = WM_USER + 104
                        TB_GETPRESSEDIMAGELIST = WM_USER + 105
                    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                    if NTDDI_VERSION >= NTDDI_WINXP:
                        TB_SETWINDOWTHEME = CCM_SETWINDOWTHEME
                    # END IF

                    TBN_GETBUTTONINFOA = TBN_FIRST - 0
                    TBN_BEGINDRAG = TBN_FIRST - 1
                    TBN_ENDDRAG = TBN_FIRST - 2
                    TBN_BEGINADJUST = TBN_FIRST - 3
                    TBN_ENDADJUST = TBN_FIRST - 4
                    TBN_RESET = TBN_FIRST - 5
                    TBN_QUERYINSERT = TBN_FIRST - 6
                    TBN_QUERYDELETE = TBN_FIRST - 7
                    TBN_TOOLBARCHANGE = TBN_FIRST - 8
                    TBN_CUSTHELP = TBN_FIRST - 9
                    TBN_DROPDOWN = TBN_FIRST - 10
                    TBN_GETOBJECT = TBN_FIRST - 12

                    # Structure for TBN_HOTITEMCHANGE notification
                    class tagNMTBHOTITEM(ctypes.Structure):
                        pass


                    tagNMTBHOTITEM._fields_ = [
                        ('hdr', NMHDR),
                        ('idOld', INT),
                        ('idNew', INT),
                        ('dwFlags', DWORD), # HICF_*
                    ]
                    NMTBHOTITEM = tagNMTBHOTITEM
                    LPNMTBHOTITEM = POINTER(tagNMTBHOTITEM)

                    # Hot item change flags
                    HICF_OTHER = 0x00000000
                    HICF_MOUSE = 0x00000001
                    HICF_ARROWKEYS = 0x00000002
                    HICF_ACCELERATOR = 0x00000004
                    HICF_DUPACCEL = 0x00000008
                    HICF_ENTERING = 0x00000010
                    HICF_LEAVING = 0x00000020
                    HICF_RESELECT = 0x00000040
                    HICF_LMOUSE = 0x00000080
                    HICF_TOGGLEDROPDOWN = 0x00000100
                    TBN_HOTITEMCHANGE = TBN_FIRST - 13
                    TBN_DRAGOUT = TBN_FIRST - 14
                    TBN_DELETINGBUTTON = TBN_FIRST - 15
                    TBN_GETDISPINFOA = TBN_FIRST - 16
                    TBN_GETDISPINFOW = TBN_FIRST - 17
                    TBN_GETINFOTIPA = TBN_FIRST - 18
                    TBN_GETINFOTIPW = TBN_FIRST - 19
                    TBN_GETBUTTONINFOW = TBN_FIRST - 20
                    TBN_RESTORE = TBN_FIRST - 21
                    TBN_SAVE = TBN_FIRST - 22
                    TBN_INITCUSTOMIZE = TBN_FIRST - 23
                    TBNRF_HIDEHELP = 0x00000001
                    TBNRF_ENDCUSTOMIZE = 0x00000002
                    TBN_WRAPHOTITEM = TBN_FIRST - 24
                    TBN_DUPACCELERATOR = TBN_FIRST - 25
                    TBN_WRAPACCELERATOR = TBN_FIRST - 26
                    TBN_DRAGOVER = TBN_FIRST - 27
                    TBN_MAPACCELERATOR = TBN_FIRST - 28


                    class tagNMTBSAVE(ctypes.Structure):
                        pass


                    tagNMTBSAVE._fields_ = [
                        ('hdr', NMHDR),
                        ('pData', POINTER(DWORD)),
                        ('pCurrent', POINTER(DWORD)),
                        ('cbData', UINT),
                        ('iItem', INT),
                        ('cButtons', INT),
                        ('tbButton', TBBUTTON),
                    ]
                    NMTBSAVE = tagNMTBSAVE
                    LPNMTBSAVE = POINTER(tagNMTBSAVE)


                    class tagNMTBRESTORE(ctypes.Structure):
                        pass


                    tagNMTBRESTORE._fields_ = [
                        ('hdr', NMHDR),
                        ('pData', POINTER(DWORD)),
                        ('pCurrent', POINTER(DWORD)),
                        ('cbData', UINT),
                        ('iItem', INT),
                        ('cButtons', INT),
                        ('cbBytesPerRecord', INT),
                        ('tbButton', TBBUTTON),
                    ]
                    NMTBRESTORE = tagNMTBRESTORE
                    LPNMTBRESTORE = POINTER(tagNMTBRESTORE)


                    class tagNMTBGETINFOTIPA(ctypes.Structure):
                        pass


                    tagNMTBGETINFOTIPA._fields_ = [
                        ('hdr', NMHDR),
                        ('pszText', LPSTR),
                        ('cchTextMax', INT),
                        ('iItem', INT),
                        ('lParam', LPARAM),
                    ]
                    NMTBGETINFOTIPA = tagNMTBGETINFOTIPA
                    LPNMTBGETINFOTIPA = POINTER(tagNMTBGETINFOTIPA)


                    class tagNMTBGETINFOTIPW(ctypes.Structure):
                        pass


                    tagNMTBGETINFOTIPW._fields_ = [
                        ('hdr', NMHDR),
                        ('pszText', LPWSTR),
                        ('cchTextMax', INT),
                        ('iItem', INT),
                        ('lParam', LPARAM),
                    ]
                    NMTBGETINFOTIPW = tagNMTBGETINFOTIPW
                    LPNMTBGETINFOTIPW = POINTER(tagNMTBGETINFOTIPW)

                    if defined(UNICODE):
                        TBN_GETINFOTIP = TBN_GETINFOTIPW
                        NMTBGETINFOTIP = NMTBGETINFOTIPW
                        LPNMTBGETINFOTIP = LPNMTBGETINFOTIPW
                    else:
                        TBN_GETINFOTIP = TBN_GETINFOTIPA
                        NMTBGETINFOTIP = NMTBGETINFOTIPA
                        LPNMTBGETINFOTIP = LPNMTBGETINFOTIPA
                    # END IF

                    TBNF_IMAGE = 0x00000001
                    TBNF_TEXT = 0x00000002
                    TBNF_DI_SETITEM = 0x10000000


                    class NMTBDISPINFOA(ctypes.Structure):
                        pass


                    NMTBDISPINFOA._fields_ = [
                        ('hdr', NMHDR),

                        # [in] Specifies the values requested .[out] Client
                        # ask the data to be set for future use
                        ('dwMask', DWORD),
                        ('idCommand', INT), # [in] id of button we're requesting info for
                        ('lParam', DWORD_PTR), # [in] lParam of button
                        ('iImage', INT), # [out] image index
                        ('pszText', LPSTR), # [out] new text for item
                        ('cchText', INT), # [in] size of buffer pointed to by pszText
                    ]
                    LPNMTBDISPINFOA = POINTER(NMTBDISPINFOA)


                    class NMTBDISPINFOW(ctypes.Structure):
                        pass


                    NMTBDISPINFOW._fields_ = [
                        ('hdr', NMHDR),

                        # [in] Specifies the values requested .[out] Client
                        # ask the data to be set for future use
                        ('dwMask', DWORD),
                        ('idCommand', INT), # [in] id of button we're requesting info for
                        ('lParam', DWORD_PTR), # [in] lParam of button
                        ('iImage', INT), # [out] image index
                        ('pszText', LPWSTR), # [out] new text for item
                        ('cchText', INT), # [in] size of buffer pointed to by pszText
                    ]
                    LPNMTBDISPINFOW = POINTER(NMTBDISPINFOW)

                    if defined(UNICODE):
                        TBN_GETDISPINFO = TBN_GETDISPINFOW
                        NMTBDISPINFO = NMTBDISPINFOW
                        LPNMTBDISPINFO = LPNMTBDISPINFOW
                    else:
                        TBN_GETDISPINFO = TBN_GETDISPINFOA
                        NMTBDISPINFO = NMTBDISPINFOA
                        LPNMTBDISPINFO = LPNMTBDISPINFOA
                    # END IF

                    # Return codes for TBN_DROPDOWN
                    TBDDRET_DEFAULT = 0
                    TBDDRET_NODEFAULT = 1
                    TBDDRET_TREATPRESSED = 2

                    if defined(UNICODE):
                        TBN_GETBUTTONINFO = TBN_GETBUTTONINFOW
                    else:
                        TBN_GETBUTTONINFO = TBN_GETBUTTONINFOA
                    # END IF


                    class tagNMTOOLBARA(ctypes.Structure):
                        pass


                    tagNMTOOLBARA._fields_ = [
                        ('hdr', NMHDR),
                        ('iItem', INT),
                        ('tbButton', TBBUTTON),
                        ('cchText', INT),
                        ('pszText', LPSTR),
                        ('rcButton', RECT),
                    ]
                    NMTOOLBARA = tagNMTOOLBARA
                    LPNMTOOLBARA = POINTER(tagNMTOOLBARA)


                    class tagNMTOOLBARW(ctypes.Structure):
                        pass


                    tagNMTOOLBARW._fields_ = [
                        ('hdr', NMHDR),
                        ('iItem', INT),
                        ('tbButton', TBBUTTON),
                        ('cchText', INT),
                        ('pszText', LPWSTR),
                        ('rcButton', RECT),
                    ]
                    NMTOOLBARW = tagNMTOOLBARW
                    LPNMTOOLBARW = POINTER(tagNMTOOLBARW)

                    if defined(UNICODE):
                        NMTOOLBAR = NMTOOLBARW
                        LPNMTOOLBAR = LPNMTOOLBARW
                    else:
                        NMTOOLBAR = NMTOOLBARA
                        LPNMTOOLBAR = LPNMTOOLBARA

                    TBNOTIFYA = NMTOOLBARA
                    TBNOTIFYW = NMTOOLBARW
                    LPTBNOTIFYA = LPNMTOOLBARA
                    LPTBNOTIFYW = LPNMTOOLBARW
                    TBNOTIFY = NMTOOLBAR
                    LPTBNOTIFY = LPNMTOOLBAR
                    # END IF
                # END IF
            # END IF   NOTOOLBAR

            # == == == REBAR CONTROL == == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == ==

            if not defined(NOREBAR):
                if defined(_WIN32):
                    REBARCLASSNAMEW = "ReBarWindow32"
                    REBARCLASSNAMEA = "ReBarWindow32"

                    if defined(UNICODE):
                        REBARCLASSNAME = REBARCLASSNAMEW
                    else:
                        REBARCLASSNAME = REBARCLASSNAMEA
                    # END IF
                else:
                    REBARCLASSNAME = "ReBarWindow"
                # END IF
                RBIM_IMAGELIST = 0x00000001

                # begin_r_commctrl
                RBS_TOOLTIPS = 0x00000100
                RBS_VARHEIGHT = 0x00000200
                RBS_BANDBORDERS = 0x00000400
                RBS_FIXEDORDER = 0x00000800
                RBS_REGISTERDROP = 0x00001000
                RBS_AUTOSIZE = 0x00002000
                RBS_VERTICALGRIPPER = 0x00004000
                RBS_DBLCLKTOGGLE = 0x00008000

                # end_r_commctrl
                class tagREBARINFO(ctypes.Structure):
                    pass


                tagREBARINFO._fields_ = [
                    ('cbSize', UINT),
                    ('fMask', UINT),
                    ('himl', HIMAGELIST) if not defined(NOIMAGEAPIS) else ('himl', HANDLE),
                ]
                REBARINFO = tagREBARINFO
                LPREBARINFO = POINTER(tagREBARINFO)

                RBBS_BREAK = 0x00000001
                RBBS_FIXEDSIZE = 0x00000002
                RBBS_CHILDEDGE = 0x00000004
                RBBS_HIDDEN = 0x00000008
                RBBS_NOVERT = 0x00000010
                RBBS_FIXEDBMP = 0x00000020
                RBBS_VARIABLEHEIGHT = 0x00000040
                RBBS_GRIPPERALWAYS = 0x00000080
                RBBS_NOGRIPPER = 0x00000100
                RBBS_USECHEVRON = 0x00000200
                RBBS_HIDETITLE = 0x00000400
                RBBS_TOPALIGN = 0x00000800

                if NTDDI_VERSION >= NTDDI_VISTA:
                    pass
                # END IF
                RBBIM_STYLE = 0x00000001
                RBBIM_COLORS = 0x00000002
                RBBIM_TEXT = 0x00000004
                RBBIM_IMAGE = 0x00000008
                RBBIM_CHILD = 0x00000010
                RBBIM_CHILDSIZE = 0x00000020
                RBBIM_SIZE = 0x00000040
                RBBIM_BACKGROUND = 0x00000080
                RBBIM_ID = 0x00000100
                RBBIM_IDEALSIZE = 0x00000200
                RBBIM_LPARAM = 0x00000400
                RBBIM_HEADERSIZE = 0x00000800

                if NTDDI_VERSION >= NTDDI_VISTA:
                    RBBIM_CHEVRONLOCATION = 0x00001000
                    RBBIM_CHEVRONSTATE = 0x00002000
                # END IF

                class tagREBARBANDINFOA(ctypes.Structure):
                    pass

                _TEMP_tagREBARBANDINFOA = [
                    ('cbSize', UINT),
                    ('fMask', UINT),
                    ('fStyle', UINT),
                    ('clrFore', COLORREF),
                    ('clrBack', COLORREF),
                    ('lpText', LPSTR),
                    ('cch', UINT),
                    ('iImage', INT),
                    ('hwndChild', HWND),
                    ('cxMinChild', UINT),
                    ('cyMinChild', UINT),
                    ('cx', UINT),
                    ('hbmBack', HBITMAP),
                    ('wID', UINT),
                    ('cyChild', UINT),
                    ('cyMaxChild', UINT),
                    ('cyIntegral', UINT),
                    ('cxIdeal', UINT),
                    ('lParam', LPARAM),
                    ('cxHeader', UINT),

                ]


                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP_tagREBARBANDINFOA += [
                        ('rcChevronLocation', RECT),  # the rect is in client co - ord wrt hwndChild
                        ('uChevronState', UINT),  # STATE_SYSTEM_*
                    ]
                # END IF

                tagREBARBANDINFOA._fields_ = _TEMP_tagREBARBANDINFOA
                REBARBANDINFOA = tagREBARBANDINFOA
                LPREBARBANDINFOA = POINTER(tagREBARBANDINFOA)
                LPCREBARBANDINFOA = POINTER(REBARBANDINFOA)


                class tagREBARBANDINFOW(ctypes.Structure):
                    pass


                _TEMP_tagREBARBANDINFOW = [
                    ('cbSize', UINT),
                    ('fMask', UINT),
                    ('fStyle', UINT),
                    ('clrFore', COLORREF),
                    ('clrBack', COLORREF),
                    ('lpText', LPWSTR),
                    ('cch', UINT),
                    ('iImage', INT),
                    ('hwndChild', HWND),
                    ('cxMinChild', UINT),
                    ('cyMinChild', UINT),
                    ('cx', UINT),
                    ('hbmBack', HBITMAP),
                    ('wID', UINT),
                    ('cyChild', UINT),
                    ('cyMaxChild', UINT),
                    ('cyIntegral', UINT),
                    ('cxIdeal', UINT),
                    ('lParam', LPARAM),
                    ('cxHeader', UINT),

                ]

                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP_tagREBARBANDINFOW += [
                        ('rcChevronLocation', RECT),  # the rect is in client co - ord wrt hwndChild
                        ('uChevronState', UINT),  # STATE_SYSTEM_*
                    ]
                # END IF

                tagREBARBANDINFOW._fields_ = _TEMP_tagREBARBANDINFOW
                REBARBANDINFOW = tagREBARBANDINFOW
                LPREBARBANDINFOW = POINTER(tagREBARBANDINFOW)
                LPCREBARBANDINFOW = POINTER(REBARBANDINFOW)

                REBARBANDINFOA_V3_SIZE = CCSIZEOF_STRUCT(
                    REBARBANDINFOA,
                    REBARBANDINFOA.wID,
                )
                REBARBANDINFOW_V3_SIZE = CCSIZEOF_STRUCT(
                    REBARBANDINFOW,
                    REBARBANDINFOW.wID,
                )
                REBARBANDINFOA_V6_SIZE = CCSIZEOF_STRUCT(
                    REBARBANDINFOA,
                    REBARBANDINFOA_V6_SIZE.cxHeader,
                )
                REBARBANDINFOW_V6_SIZE = CCSIZEOF_STRUCT(
                    REBARBANDINFOW,
                    REBARBANDINFOW.cxHeader,
                )

                if defined(UNICODE):
                    REBARBANDINFO = REBARBANDINFOW
                    LPREBARBANDINFO = LPREBARBANDINFOW
                    LPCREBARBANDINFO = LPCREBARBANDINFOW
                    REBARBANDINFO_V3_SIZE = REBARBANDINFOW_V3_SIZE
                    REBARBANDINFO_V6_SIZE = REBARBANDINFOW_V6_SIZE
                else:
                    REBARBANDINFO = REBARBANDINFOA
                    LPREBARBANDINFO = LPREBARBANDINFOA
                    LPCREBARBANDINFO = LPCREBARBANDINFOA
                    REBARBANDINFO_V3_SIZE = REBARBANDINFOA_V3_SIZE
                    REBARBANDINFO_V6_SIZE = REBARBANDINFOA_V6_SIZE
                # END IF

                RB_INSERTBANDA = WM_USER +  1
                RB_DELETEBAND = WM_USER +  2
                RB_GETBARINFO = WM_USER +  3
                RB_SETBARINFO = WM_USER +  4
                RB_SETBANDINFOA = WM_USER +  6
                RB_SETPARENT = WM_USER +  7
                RB_HITTEST = WM_USER +  8
                RB_GETRECT = WM_USER +  9
                RB_INSERTBANDW = WM_USER +  10
                RB_SETBANDINFOW = WM_USER +  11
                RB_GETBANDCOUNT = WM_USER +  12
                RB_GETROWCOUNT = WM_USER +  13
                RB_GETROWHEIGHT = WM_USER +  14
                RB_IDTOINDEX = WM_USER +  16
                RB_GETTOOLTIPS = WM_USER +  17
                RB_SETTOOLTIPS = WM_USER +  18
                RB_SETBKCOLOR = WM_USER +  19
                RB_GETBKCOLOR = WM_USER +  20
                RB_SETTEXTCOLOR = WM_USER +  21
                RB_GETTEXTCOLOR = WM_USER +  22

                if NTDDI_VERSION >= NTDDI_WINXP:
                    RBSTR_CHANGERECT = 0x0001
                # END IF

                RB_SIZETORECT = WM_USER +  23
                RB_SETCOLORSCHEME = CCM_SETCOLORSCHEME
                RB_GETCOLORSCHEME = CCM_GETCOLORSCHEME

                if defined(UNICODE):
                    RB_INSERTBAND = RB_INSERTBANDW
                    RB_SETBANDINFO = RB_SETBANDINFOW
                else:
                    RB_INSERTBAND = RB_INSERTBANDA
                    RB_SETBANDINFO = RB_SETBANDINFOA
                # END IF

                # for manual drag control
                # lparam == cursor pos
                # - 1 means do it yourself.
                # - 2 means use what you had saved before
                RB_BEGINDRAG = WM_USER + 24
                RB_ENDDRAG = WM_USER + 25
                RB_DRAGMOVE = WM_USER + 26
                RB_GETBARHEIGHT = WM_USER + 27
                RB_GETBANDINFOW = WM_USER + 28
                RB_GETBANDINFOA = WM_USER + 29

                if defined(UNICODE):
                    RB_GETBANDINFO = RB_GETBANDINFOW
                else:
                    RB_GETBANDINFO = RB_GETBANDINFOA
                # END IF

                RB_MINIMIZEBAND = WM_USER + 30
                RB_MAXIMIZEBAND = WM_USER + 31
                RB_GETDROPTARGET = CCM_GETDROPTARGET
                RB_GETBANDBORDERS = WM_USER + 34
                RB_SHOWBAND = WM_USER + 35
                RB_SETPALETTE = WM_USER + 37
                RB_GETPALETTE = WM_USER + 38
                RB_MOVEBAND = WM_USER + 39
                RB_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
                RB_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT

                if NTDDI_VERSION >= NTDDI_WINXP:
                    RB_GETBANDMARGINS = WM_USER + 40
                    RB_SETWINDOWTHEME = CCM_SETWINDOWTHEME
                # END IF

                if _WIN32_IE >= 0x0600:
                    RB_SETEXTENDEDSTYLE = WM_USER + 41
                    RB_GETEXTENDEDSTYLE = WM_USER + 42
                # END IF   _WIN32_IE >= 0x0600

                RB_PUSHCHEVRON = WM_USER + 43

                if NTDDI_VERSION >= NTDDI_VISTA:
                    RB_SETBANDWIDTH = WM_USER + 44
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                RBN_HEIGHTCHANGE = RBN_FIRST - 0
                RBN_GETOBJECT = RBN_FIRST - 1
                RBN_LAYOUTCHANGED = RBN_FIRST - 2
                RBN_AUTOSIZE = RBN_FIRST - 3
                RBN_BEGINDRAG = RBN_FIRST - 4
                RBN_ENDDRAG = RBN_FIRST - 5
                RBN_DELETINGBAND = RBN_FIRST - 6
                RBN_DELETEDBAND = RBN_FIRST - 7
                RBN_CHILDSIZE = RBN_FIRST - 8
                RBN_CHEVRONPUSHED = RBN_FIRST - 10

                if _WIN32_IE >= 0x0600:
                    RBN_SPLITTERDRAG = RBN_FIRST - 11
                # END IF   _WIN32_IE >= 0x0600

                RBN_MINMAX = RBN_FIRST - 21

                if NTDDI_VERSION >= NTDDI_WINXP:
                    RBN_AUTOBREAK = RBN_FIRST - 22
                # END IF

                class tagNMREBARCHILDSIZE(ctypes.Structure):
                    pass


                tagNMREBARCHILDSIZE._fields_ = [
                    ('hdr', NMHDR),
                    ('uBand', UINT),
                    ('wID', UINT),
                    ('rcChild', RECT),
                    ('rcBand', RECT),
                ]
                NMREBARCHILDSIZE = tagNMREBARCHILDSIZE
                LPNMREBARCHILDSIZE = POINTER(tagNMREBARCHILDSIZE)


                class tagNMREBAR(ctypes.Structure):
                    pass


                tagNMREBAR._fields_ = [
                    ('hdr', NMHDR),
                    ('dwMask', DWORD), # RBNM_*
                    ('uBand', UINT),
                    ('fStyle', UINT),
                    ('wID', UINT),
                    ('lParam', LPARAM),
                ]
                NMREBAR = tagNMREBAR
                LPNMREBAR = POINTER(tagNMREBAR)

                # Mask flags for NMREBAR
                RBNM_ID = 0x00000001
                RBNM_STYLE = 0x00000002
                RBNM_LPARAM = 0x00000004


                class tagNMRBAUTOSIZE(ctypes.Structure):
                    pass


                tagNMRBAUTOSIZE._fields_ = [
                    ('hdr', NMHDR),
                    ('fChanged', BOOL),
                    ('rcTarget', RECT),
                    ('rcActual', RECT),
                ]
                NMRBAUTOSIZE = tagNMRBAUTOSIZE
                LPNMRBAUTOSIZE = POINTER(tagNMRBAUTOSIZE)


                class tagNMREBARCHEVRON(ctypes.Structure):
                    pass


                tagNMREBARCHEVRON._fields_ = [
                    ('hdr', NMHDR),
                    ('uBand', UINT),
                    ('wID', UINT),
                    ('lParam', LPARAM),
                    ('rc', RECT),
                    ('lParamNM', LPARAM),
                ]
                NMREBARCHEVRON = tagNMREBARCHEVRON
                LPNMREBARCHEVRON = POINTER(tagNMREBARCHEVRON)

                if _WIN32_IE >= 0x0600:
                    class tagNMREBARSPLITTER(ctypes.Structure):
                        pass


                    tagNMREBARSPLITTER._fields_ = [
                        ('hdr', NMHDR),
                        ('rcSizing', RECT),
                    ]
                    NMREBARSPLITTER = tagNMREBARSPLITTER
                    LPNMREBARSPLITTER = POINTER(tagNMREBARSPLITTER)
                # END IF

                if NTDDI_VERSION >= NTDDI_WINXP:
                    RBAB_AUTOSIZE = 0x0001
                    RBAB_ADDBAND = 0x0002


                    class tagNMREBARAUTOBREAK(ctypes.Structure):
                        pass


                    tagNMREBARAUTOBREAK._fields_ = [
                        ('hdr', NMHDR),
                        ('uBand', UINT),
                        ('wID', UINT),
                        ('lParam', LPARAM),
                        ('uMsg', UINT),
                        ('fStyleCurrent', UINT),
                        ('fAutoBreak', BOOL),
                    ]
                    NMREBARAUTOBREAK = tagNMREBARAUTOBREAK
                    LPNMREBARAUTOBREAK = POINTER(tagNMREBARAUTOBREAK)
                # END IF

                RBHT_NOWHERE = 0x0001
                RBHT_CAPTION = 0x0002
                RBHT_CLIENT = 0x0003
                RBHT_GRABBER = 0x0004
                RBHT_CHEVRON = 0x0008

                if _WIN32_IE >= 0x0600:
                    RBHT_SPLITTER = 0x0010
                # END IF
                class _RB_HITTESTINFO(ctypes.Structure):
                    pass


                _RB_HITTESTINFO._fields_ = [
                    ('pt', POINT),
                    ('flags', UINT),
                    ('iBand', INT),
                ]
                RBHITTESTINFO = _RB_HITTESTINFO
                LPRBHITTESTINFO = POINTER(_RB_HITTESTINFO)
            # END IF   NOREBAR

            # == == == TOOLTIPS CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == =

            if not defined(NOTOOLTIPS):
                if defined(_WIN32):
                    TOOLTIPS_CLASSW = "tooltips_class32"
                    TOOLTIPS_CLASSA = "tooltips_class32"

                    if defined(UNICODE):
                        TOOLTIPS_CLASS = TOOLTIPS_CLASSW
                    else:
                        TOOLTIPS_CLASS = TOOLTIPS_CLASSA
                    # END IF
                else:
                    TOOLTIPS_CLASS = "tooltips_class"
                # END IF

                class tagTOOLINFOA(ctypes.Structure):
                    pass



                _TEMP_tagTOOLINFOA = [
                    ('cbSize', UINT),
                    ('uFlags', UINT),
                    ('hwnd', HWND),
                    ('uId', UINT_PTR),
                    ('rect', RECT),
                    ('hinst', HINSTANCE),
                    ('lpszText', LPSTR),
                    ('lParam', LPARAM),

                ]


                if NTDDI_VERSION >= NTDDI_WINXP:
                    _TEMP_tagTOOLINFOA += [
                        ('lpReserved', POINTER(VOID))
                    ]
                # END IF

                tagTOOLINFOA._fields_ = _TEMP_tagTOOLINFOA
                TTTOOLINFOA = tagTOOLINFOA
                PTOOLINFOA = POINTER(tagTOOLINFOA)
                LPTTTOOLINFOA = POINTER(tagTOOLINFOA)

                class tagTOOLINFOW(ctypes.Structure):
                    pass


                _TEMP_tagTOOLINFOW = [
                    ('cbSize', UINT),
                    ('uFlags', UINT),
                    ('hwnd', HWND),
                    ('uId', UINT_PTR),
                    ('rect', RECT),
                    ('hinst', HINSTANCE),
                    ('lpszText', LPWSTR),
                    ('lParam', LPARAM),

                ]

                if NTDDI_VERSION >= NTDDI_WINXP:
                    _TEMP_tagTOOLINFOW += [
                        ('lpReserved', POINTER(VOID))
                    ]
                # END IF

                tagTOOLINFOW._fields_ = _TEMP_tagTOOLINFOW
                TTTOOLINFOW = tagTOOLINFOW
                PTOOLINFOW = POINTER(tagTOOLINFOW)
                LPTTTOOLINFOW = POINTER(tagTOOLINFOW)

                TTTOOLINFOA_V1_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOA, TTTOOLINFOA.lpszText)
                TTTOOLINFOW_V1_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOW, TTTOOLINFOW.lpszText)
                TTTOOLINFOA_V2_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOA, TTTOOLINFOA.lParam)
                TTTOOLINFOW_V2_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOW, TTTOOLINFOW.lParam)
                TTTOOLINFOA_V3_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOA, TTTOOLINFOA.lpReserved)
                TTTOOLINFOW_V3_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOW, TTTOOLINFOW.lpReserved)

                if defined(UNICODE):
                    TTTOOLINFO = TTTOOLINFOW
                    PTOOLINFO = PTOOLINFOW
                    LPTTTOOLINFO = LPTTTOOLINFOW
                    TTTOOLINFO_V1_SIZE = TTTOOLINFOW_V1_SIZE
                else:
                    PTOOLINFO = PTOOLINFOA
                    TTTOOLINFO = TTTOOLINFOA
                    LPTTTOOLINFO = LPTTTOOLINFOA
                    TTTOOLINFO_V1_SIZE = TTTOOLINFOA_V1_SIZE
                # END IF

                LPTOOLINFOA = LPTTTOOLINFOA
                LPTOOLINFOW = LPTTTOOLINFOW
                TOOLINFOA = TTTOOLINFOA
                TOOLINFOW = TTTOOLINFOW
                LPTOOLINFO = LPTTTOOLINFO
                TOOLINFO = TTTOOLINFO


                # begin_r_commctrl
                TTS_ALWAYSTIP = 0x01
                TTS_NOPREFIX = 0x02
                TTS_NOANIMATE = 0x10
                TTS_NOFADE = 0x20
                TTS_BALLOON = 0x40
                TTS_CLOSE = 0x80

                if NTDDI_VERSION >= NTDDI_VISTA:
                    TTS_USEVISUALSTYLE = 0x100
                # END IF

                # end_r_commctrl
                TTF_IDISHWND = 0x0001

                # Use this to center around trackpoint in trackmode

                # - OR- to center around tool in normal mode.

                # Use TTF_ABSOLUTE to place the tip exactly at the track
                # coords when

                # in tracking mode. TTF_ABSOLUTE can be used in conjunction
                # with TTF_CENTERTIP

                # to center the tip absolutely about the track point.
                TTF_CENTERTIP = 0x0002
                TTF_RTLREADING = 0x0004
                TTF_SUBCLASS = 0x0010
                TTF_TRACK = 0x0020
                TTF_ABSOLUTE = 0x0080
                TTF_TRANSPARENT = 0x0100
                TTF_PARSELINKS = 0x1000
                TTF_DI_SETITEM = 0x8000
                TTDT_AUTOMATIC = 0
                TTDT_RESHOW = 1
                TTDT_AUTOPOP = 2
                TTDT_INITIAL = 3

                # ToolTip Icons (Set with TTM_SETTITLE)
                TTI_NONE = 0
                TTI_INFO = 1
                TTI_WARNING = 2
                TTI_ERROR = 3

                if NTDDI_VERSION >= NTDDI_VISTA:
                    TTI_INFO_LARGE = 4
                    TTI_WARNING_LARGE = 5
                    TTI_ERROR_LARGE = 6
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                # Tool Tip Messages
                TTM_ACTIVATE = WM_USER + 1
                TTM_SETDELAYTIME = WM_USER + 3
                TTM_ADDTOOLA = WM_USER + 4
                TTM_ADDTOOLW = WM_USER + 50
                TTM_DELTOOLA = WM_USER + 5
                TTM_DELTOOLW = WM_USER + 51
                TTM_NEWTOOLRECTA = WM_USER + 6
                TTM_NEWTOOLRECTW = WM_USER + 52
                TTM_RELAYEVENT = WM_USER + 7
                TTM_GETTOOLINFOA = WM_USER + 8
                TTM_GETTOOLINFOW = WM_USER + 53
                TTM_SETTOOLINFOA = WM_USER + 9
                TTM_SETTOOLINFOW = WM_USER + 54
                TTM_HITTESTA = WM_USER  + 10
                TTM_HITTESTW = WM_USER  + 55
                TTM_GETTEXTA = WM_USER  + 11
                TTM_GETTEXTW = WM_USER  + 56
                TTM_UPDATETIPTEXTA = WM_USER  + 12
                TTM_UPDATETIPTEXTW = WM_USER  + 57
                TTM_GETTOOLCOUNT = WM_USER  + 13
                TTM_ENUMTOOLSA = WM_USER  + 14
                TTM_ENUMTOOLSW = WM_USER  + 58
                TTM_GETCURRENTTOOLA = WM_USER + 15
                TTM_GETCURRENTTOOLW = WM_USER + 59
                TTM_WINDOWFROMPOINT = WM_USER + 16
                TTM_TRACKACTIVATE = WM_USER + 17
                TTM_TRACKPOSITION = WM_USER + 18
                TTM_SETTIPBKCOLOR = WM_USER + 19
                TTM_SETTIPTEXTCOLOR = WM_USER + 20
                TTM_GETDELAYTIME = WM_USER + 21
                TTM_GETTIPBKCOLOR = WM_USER + 22
                TTM_GETTIPTEXTCOLOR = WM_USER + 23
                TTM_SETMAXTIPWIDTH = WM_USER + 24
                TTM_GETMAXTIPWIDTH = WM_USER + 25
                TTM_SETMARGIN = WM_USER + 26
                TTM_GETMARGIN = WM_USER + 27
                TTM_POP = WM_USER + 28
                TTM_UPDATE = WM_USER + 29
                TTM_GETBUBBLESIZE = WM_USER + 30
                TTM_ADJUSTRECT = WM_USER + 31
                TTM_SETTITLEA = WM_USER + 32
                TTM_SETTITLEW = WM_USER + 33

                if NTDDI_VERSION >= NTDDI_WINXP:
                    TTM_POPUP = WM_USER + 34
                    TTM_GETTITLE = WM_USER + 35


                    class _TTGETTITLE(ctypes.Structure):
                        pass


                    _TTGETTITLE._fields_ = [
                        ('dwSize', DWORD),
                        ('uTitleBitmap', UINT),
                        ('cch', UINT),
                        ('pszTitle', POINTER(WCHAR)),
                    ]
                    TTGETTITLE = _TTGETTITLE
                    PTTGETTITLE = POINTER(_TTGETTITLE)
                # END IF

                if defined(UNICODE):
                    TTM_ADDTOOL = TTM_ADDTOOLW
                    TTM_DELTOOL = TTM_DELTOOLW
                    TTM_NEWTOOLRECT = TTM_NEWTOOLRECTW
                    TTM_GETTOOLINFO = TTM_GETTOOLINFOW
                    TTM_SETTOOLINFO = TTM_SETTOOLINFOW
                    TTM_HITTEST = TTM_HITTESTW
                    TTM_GETTEXT = TTM_GETTEXTW
                    TTM_UPDATETIPTEXT = TTM_UPDATETIPTEXTW
                    TTM_ENUMTOOLS = TTM_ENUMTOOLSW
                    TTM_GETCURRENTTOOL = TTM_GETCURRENTTOOLW
                    TTM_SETTITLE = TTM_SETTITLEW
                else:
                    TTM_ADDTOOL = TTM_ADDTOOLA
                    TTM_DELTOOL = TTM_DELTOOLA
                    TTM_NEWTOOLRECT = TTM_NEWTOOLRECTA
                    TTM_GETTOOLINFO = TTM_GETTOOLINFOA
                    TTM_SETTOOLINFO = TTM_SETTOOLINFOA
                    TTM_HITTEST = TTM_HITTESTA
                    TTM_GETTEXT = TTM_GETTEXTA
                    TTM_UPDATETIPTEXT = TTM_UPDATETIPTEXTA
                    TTM_ENUMTOOLS = TTM_ENUMTOOLSA
                    TTM_GETCURRENTTOOL = TTM_GETCURRENTTOOLA
                    TTM_SETTITLE = TTM_SETTITLEA
                # END IF

                if NTDDI_VERSION >= NTDDI_WINXP:
                    TTM_SETWINDOWTHEME = CCM_SETWINDOWTHEME
                # END IF

                class _TT_HITTESTINFOA(ctypes.Structure):
                    pass


                _TT_HITTESTINFOA._fields_ = [
                    ('hwnd', HWND),
                    ('pt', POINT),
                    ('ti', TTTOOLINFOA),
                ]
                TTHITTESTINFOA = _TT_HITTESTINFOA
                LPTTHITTESTINFOA = POINTER(_TT_HITTESTINFOA)


                class _TT_HITTESTINFOW(ctypes.Structure):
                    pass


                _TT_HITTESTINFOW._fields_ = [
                    ('hwnd', HWND),
                    ('pt', POINT),
                    ('ti', TTTOOLINFOW),
                ]
                TTHITTESTINFOW = _TT_HITTESTINFOW
                LPTTHITTESTINFOW = POINTER(_TT_HITTESTINFOW)

                if defined(UNICODE):
                    TTHITTESTINFO = TTHITTESTINFOW
                    LPTTHITTESTINFO = LPTTHITTESTINFOW
                else:
                    TTHITTESTINFO = TTHITTESTINFOA
                    LPTTHITTESTINFO = LPTTHITTESTINFOA
                # END IF

                LPHITTESTINFOW = LPTTHITTESTINFOW
                LPHITTESTINFOA = LPTTHITTESTINFOA
                LPHITTESTINFO = LPTTHITTESTINFO

                TTN_GETDISPINFOA = TTN_FIRST - 0
                TTN_GETDISPINFOW = TTN_FIRST - 10
                TTN_SHOW = TTN_FIRST - 1
                TTN_POP = TTN_FIRST - 2
                TTN_LINKCLICK = TTN_FIRST - 3

                if defined(UNICODE):
                    TTN_GETDISPINFO = TTN_GETDISPINFOW
                else:
                    TTN_GETDISPINFO = TTN_GETDISPINFOA
                # END IF
                TTN_NEEDTEXT = TTN_GETDISPINFO
                TTN_NEEDTEXTA = TTN_GETDISPINFOA
                TTN_NEEDTEXTW = TTN_GETDISPINFOW

                class tagNMTTDISPINFOA(ctypes.Structure):
                    pass


                tagNMTTDISPINFOA._fields_ = [
                    ('hdr', NMHDR),
                    ('lpszText', LPSTR),
                    ('szText', CHAR * 80),
                    ('hinst', HINSTANCE),
                    ('uFlags', UINT),
                    ('lParam', LPARAM),
                ]
                NMTTDISPINFOA = tagNMTTDISPINFOA
                LPNMTTDISPINFOA = POINTER(tagNMTTDISPINFOA)


                class tagNMTTDISPINFOW(ctypes.Structure):
                    pass


                tagNMTTDISPINFOW._fields_ = [
                    ('hdr', NMHDR),
                    ('lpszText', LPWSTR),
                    ('szText', WCHAR * 80),
                    ('hinst', HINSTANCE),
                    ('uFlags', UINT),
                    ('lParam', LPARAM),
                ]
                NMTTDISPINFOW = tagNMTTDISPINFOW
                LPNMTTDISPINFOW = POINTER(tagNMTTDISPINFOW)

                TOOLTIPTEXTW = NMTTDISPINFOW
                TOOLTIPTEXTA = NMTTDISPINFOA
                LPTOOLTIPTEXTA = LPNMTTDISPINFOA
                LPTOOLTIPTEXTW = LPNMTTDISPINFOW

                NMTTDISPINFOA_V1_SIZE = CCSIZEOF_STRUCT(
                    NMTTDISPINFOA,
                    NMTTDISPINFOA.uFlags,
                )
                NMTTDISPINFOW_V1_SIZE = CCSIZEOF_STRUCT(
                    NMTTDISPINFOW,
                    NMTTDISPINFOW.uFlags,
                )

                if defined(UNICODE):
                    NMTTDISPINFO = NMTTDISPINFOW
                    LPNMTTDISPINFO = LPNMTTDISPINFOW
                    NMTTDISPINFO_V1_SIZE = NMTTDISPINFOW_V1_SIZE
                else:
                    NMTTDISPINFO = NMTTDISPINFOA
                    LPNMTTDISPINFO = LPNMTTDISPINFOA
                    NMTTDISPINFO_V1_SIZE = NMTTDISPINFOA_V1_SIZE
                # END IF

                TOOLTIPTEXT = NMTTDISPINFO
                LPTOOLTIPTEXT = LPNMTTDISPINFO
            # END IF   NOTOOLTIPS

            # == == == STATUS BAR CONTROL == == == == == == == == == == == ==
            # == == == == == == == == == == == == == =

            if not defined(NOSTATUSBAR):

                # begin_r_commctrl
                SBARS_SIZEGRIP = 0x0100
                SBARS_TOOLTIPS = 0x0800

                # this is a status bar flag, preference to SBARS_TOOLTIPS
                SBT_TOOLTIPS = 0x0800

                # end_r_commctrl
                comctl32 = ctypes.windll.ComCtl32
                # WINCOMMCTRLAPI VOID WINAPI DrawStatusTextA(HDC hDC, LPCRECT lprc, LPCSTR pszText, UINT uFlags);
                DrawStatusTextA = comctl32.DrawStatusTextA
                DrawStatusTextA.restype = VOID
                # WINCOMMCTRLAPI VOID WINAPI DrawStatusTextW(HDC hDC, LPCRECT lprc, LPCWSTR pszText, UINT uFlags);
                DrawStatusTextW = comctl32.DrawStatusTextW
                DrawStatusTextW.restype = VOID
                # WINCOMMCTRLAPI HWND WINAPI CreateStatusWindowA(LONG style, LPCSTR lpszText, HWND hwndParent, UINT wID);
                CreateStatusWindowA = comctl32.CreateStatusWindowA
                CreateStatusWindowA.restype = HWND
                # WINCOMMCTRLAPI HWND WINAPI CreateStatusWindowW(LONG style, LPCWSTR lpszText, HWND hwndParent, UINT wID);
                CreateStatusWindowW = comctl32.CreateStatusWindowW
                CreateStatusWindowW.restype = HWND

                if defined(UNICODE):
                    CreateStatusWindow = CreateStatusWindowW
                    DrawStatusText = DrawStatusTextW
                else:
                    CreateStatusWindow = CreateStatusWindowA
                    DrawStatusText = DrawStatusTextA
                # END IF

                if defined(_WIN32):
                    STATUSCLASSNAMEW = "msctls_statusbar32"
                    STATUSCLASSNAMEA = "msctls_statusbar32"

                    if defined(UNICODE):
                        STATUSCLASSNAME = STATUSCLASSNAMEW
                    else:
                        STATUSCLASSNAME = STATUSCLASSNAMEA
                    # END IF
                else:
                    STATUSCLASSNAME = "msctls_statusbar"
                # END IF
                SB_SETTEXTA = WM_USER + 1
                SB_SETTEXTW = WM_USER + 11
                SB_GETTEXTA = WM_USER + 2
                SB_GETTEXTW = WM_USER + 13
                SB_GETTEXTLENGTHA = WM_USER + 3
                SB_GETTEXTLENGTHW = WM_USER + 12

                if defined(UNICODE):
                    SB_GETTEXT = SB_GETTEXTW
                    SB_SETTEXT = SB_SETTEXTW
                    SB_GETTEXTLENGTH = SB_GETTEXTLENGTHW
                    SB_SETTIPTEXT = SB_SETTIPTEXTW
                    SB_GETTIPTEXT = SB_GETTIPTEXTW
                else:
                    SB_GETTEXT = SB_GETTEXTA
                    SB_SETTEXT = SB_SETTEXTA
                    SB_GETTEXTLENGTH = SB_GETTEXTLENGTHA
                    SB_SETTIPTEXT = SB_SETTIPTEXTA
                    SB_GETTIPTEXT = SB_GETTIPTEXTA
                # END IF
                SB_SETPARTS = WM_USER + 4
                SB_GETPARTS = WM_USER + 6
                SB_GETBORDERS = WM_USER + 7
                SB_SETMINHEIGHT = WM_USER + 8
                SB_SIMPLE = WM_USER + 9
                SB_GETRECT = WM_USER + 10
                SB_ISSIMPLE = WM_USER + 14
                SB_SETICON = WM_USER + 15
                SB_SETTIPTEXTA = WM_USER + 16
                SB_SETTIPTEXTW = WM_USER + 17
                SB_GETTIPTEXTA = WM_USER + 18
                SB_GETTIPTEXTW = WM_USER + 19
                SB_GETICON = WM_USER + 20
                SB_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
                SB_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
                SBT_OWNERDRAW = 0x1000
                SBT_NOBORDERS = 0x0100
                SBT_POPOUT = 0x0200
                SBT_RTLREADING = 0x0400
                SBT_NOTABPARSING = 0x0800
                SB_SETBKCOLOR = CCM_SETBKCOLOR

                # status bar notifications
                SBN_SIMPLEMODECHANGE = SBN_FIRST - 0

                # refers to the data saved for simple mode
                SB_SIMPLEID = 0x00FF
            # END IF   NOSTATUSBAR

            # == == == MENU HELP == == == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == == ==

            if not defined(NOMENUHELP):
                # WINCOMMCTRLAPI VOID WINAPI MenuHelp(UINT uMsg, WPARAM wParam, LPARAM lParam, HMENU hMainMenu, HINSTANCE hInst, HWND hwndStatus, _In_reads_(_Inexpressible_(2 + 2n and n >= 1)) UINT *lpwIDs);
                MenuHelp = comctl32.MenuHelp
                MenuHelp.restype = VOID
                # WINCOMMCTRLAPI BOOL WINAPI ShowHideMenuCtl(_In_ HWND hWnd, _In_ UINT_PTR uFlags, _In_z_ LPINT lpInfo);
                ShowHideMenuCtl = comctl32.ShowHideMenuCtl
                ShowHideMenuCtl.restype = BOOL
                # WINCOMMCTRLAPI VOID WINAPI GetEffectiveClientRect(_In_ HWND hWnd, _Out_ LPRECT lprc,  _In_z_ INT *lpInfo);
                GetEffectiveClientRect = comctl32.GetEffectiveClientRect
                GetEffectiveClientRect.restype = VOID
                MINSYSCOMMAND = SC_SIZE
            # END IF

            # == == == TRACKBAR CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == =

            if not defined(NOTRACKBAR):
                if defined(_WIN32):
                    TRACKBAR_CLASSA = "msctls_trackbar32"
                    TRACKBAR_CLASSW = "msctls_trackbar32"

                    if defined(UNICODE):
                        TRACKBAR_CLASS = TRACKBAR_CLASSW
                    else:
                        TRACKBAR_CLASS = TRACKBAR_CLASSA
                    # END IF
                else:
                    TRACKBAR_CLASS = "msctls_trackbar"
                # END IF

                # begin_r_commctrl
                TBS_AUTOTICKS = 0x0001
                TBS_VERT = 0x0002
                TBS_HORZ = 0x0000
                TBS_TOP = 0x0004
                TBS_BOTTOM = 0x0000
                TBS_LEFT = 0x0004
                TBS_RIGHT = 0x0000
                TBS_BOTH = 0x0008
                TBS_NOTICKS = 0x0010
                TBS_ENABLESELRANGE = 0x0020
                TBS_FIXEDLENGTH = 0x0040
                TBS_NOTHUMB = 0x0080
                TBS_TOOLTIPS = 0x0100
                TBS_REVERSED = 0x0200
                TBS_DOWNISLEFT = 0x0400

                if _WIN32_IE >= 0x0600:
                    TBS_NOTIFYBEFOREMOVE = 0x0800
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    TBS_TRANSPARENTBKGND = 0x1000
                # END IF

                # end_r_commctrl
                TBM_GETPOS = WM_USER
                TBM_GETRANGEMIN = WM_USER + 1
                TBM_GETRANGEMAX = WM_USER + 2
                TBM_GETTIC = WM_USER + 3
                TBM_SETTIC = WM_USER + 4
                TBM_SETPOS = WM_USER + 5
                TBM_SETRANGE = WM_USER + 6
                TBM_SETRANGEMIN = WM_USER + 7
                TBM_SETRANGEMAX = WM_USER + 8
                TBM_CLEARTICS = WM_USER + 9
                TBM_SETSEL = WM_USER + 10
                TBM_SETSELSTART = WM_USER + 11
                TBM_SETSELEND = WM_USER + 12
                TBM_GETPTICS = WM_USER + 14
                TBM_GETTICPOS = WM_USER + 15
                TBM_GETNUMTICS = WM_USER + 16
                TBM_GETSELSTART = WM_USER + 17
                TBM_GETSELEND = WM_USER + 18
                TBM_CLEARSEL = WM_USER + 19
                TBM_SETTICFREQ = WM_USER + 20
                TBM_SETPAGESIZE = WM_USER + 21
                TBM_GETPAGESIZE = WM_USER + 22
                TBM_SETLINESIZE = WM_USER + 23
                TBM_GETLINESIZE = WM_USER + 24
                TBM_GETTHUMBRECT = WM_USER + 25
                TBM_GETCHANNELRECT = WM_USER + 26
                TBM_SETTHUMBLENGTH = WM_USER + 27
                TBM_GETTHUMBLENGTH = WM_USER + 28
                TBM_SETTOOLTIPS = WM_USER + 29
                TBM_GETTOOLTIPS = WM_USER + 30
                TBM_SETTIPSIDE = WM_USER + 31

                # TrackBar Tip Side flags
                TBTS_TOP = 0
                TBTS_LEFT = 1
                TBTS_BOTTOM = 2
                TBTS_RIGHT = 3
                TBM_SETBUDDY = WM_USER + 32
                TBM_GETBUDDY = WM_USER + 33
                TBM_SETPOSNOTIFY = WM_USER + 34
                TBM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
                TBM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
                TB_LINEUP = 0
                TB_LINEDOWN = 1
                TB_PAGEUP = 2
                TB_PAGEDOWN = 3
                TB_THUMBPOSITION = 4
                TB_THUMBTRACK = 5
                TB_TOP = 6
                TB_BOTTOM = 7
                TB_ENDTRACK = 8

                # custom draw item specs
                TBCD_TICS = 0x0001
                TBCD_THUMB = 0x0002
                TBCD_CHANNEL = 0x0003

                if NTDDI_VERSION >= NTDDI_VISTA:
                    TRBN_THUMBPOSCHANGING = TRBN_FIRST - 1

                    # Structure for Trackbar's TRBN_THUMBPOSCHANGING
                    # notification
                    class tagTRBTHUMBPOSCHANGING(ctypes.Structure):
                        pass


                    tagTRBTHUMBPOSCHANGING._fields_ = [
                        ('hdr', NMHDR),
                        ('dwPos', DWORD),
                        ('nReason', INT),
                    ]
                    NMTRBTHUMBPOSCHANGING = tagTRBTHUMBPOSCHANGING
                # END IF
            # END IF   trackbar

            # == == == DRAG LIST CONTROL == == == == == == == == == == == ==
            # == == == == == == == == == == == == == ==

            if not defined(NODRAGLIST):
                class tagDRAGLISTINFO(ctypes.Structure):
                    pass


                tagDRAGLISTINFO._fields_ = [
                    ('uNotification', UINT),
                    ('hWnd', HWND),
                    ('ptCursor', POINT),
                ]
                DRAGLISTINFO = tagDRAGLISTINFO
                LPDRAGLISTINFO = POINTER(tagDRAGLISTINFO)

                DL_BEGINDRAG = WM_USER + 133
                DL_DRAGGING = WM_USER + 134
                DL_DROPPED = WM_USER + 135
                DL_CANCELDRAG = WM_USER + 136
                DL_CURSORSET = 0
                DL_STOPCURSOR = 1
                DL_COPYCURSOR = 2
                DL_MOVECURSOR = 3
                DRAGLISTMSGSTRING = TEXT("commctrl_DragListMsg")
                # WINCOMMCTRLAPI BOOL WINAPI MakeDragList(HWND hLB);
                MakeDragList = comctl32.MakeDragList
                MakeDragList.restype = BOOL
                # WINCOMMCTRLAPI VOID WINAPI DrawInsert(HWND handParent, HWND hLB, INT nItem);
                DrawInsert = comctl32.DrawInsert
                DrawInsert.restype = VOID
                # WINCOMMCTRLAPI INT WINAPI LBItemFromPt(HWND hLB, POINT pt, BOOL bAutoScroll);
                LBItemFromPt = comctl32.LBItemFromPt
                LBItemFromPt.restype = INT
            # END IF

            # == == == UPDOWN CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == == =

            if not defined(NOUPDOWN):
                if defined(_WIN32):
                    UPDOWN_CLASSA = "msctls_updown32"
                    UPDOWN_CLASSW = "msctls_updown32"

                    if defined(UNICODE):
                        UPDOWN_CLASS = UPDOWN_CLASSW
                    else:
                        UPDOWN_CLASS = UPDOWN_CLASSA
                    # END IF
                else:
                    UPDOWN_CLASS = "msctls_updown"
                # END IF
                class _UDACCEL(ctypes.Structure):
                    pass


                _UDACCEL._fields_ = [
                    ('nSec', UINT),
                    ('nInc', UINT),
                ]
                UDACCEL = _UDACCEL
                LPUDACCEL = POINTER(_UDACCEL)
                UD_MAXVAL = 0x7FFF
                UD_MINVAL = - UD_MAXVAL

                # begin_r_commctrl
                UDS_WRAP = 0x0001
                UDS_SETBUDDYINT = 0x0002
                UDS_ALIGNRIGHT = 0x0004
                UDS_ALIGNLEFT = 0x0008
                UDS_AUTOBUDDY = 0x0010
                UDS_ARROWKEYS = 0x0020
                UDS_HORZ = 0x0040
                UDS_NOTHOUSANDS = 0x0080
                UDS_HOTTRACK = 0x0100

                # end_r_commctrl
                UDM_SETRANGE = WM_USER + 101
                UDM_GETRANGE = WM_USER + 102
                UDM_SETPOS = WM_USER + 103
                UDM_GETPOS = WM_USER + 104
                UDM_SETBUDDY = WM_USER + 105
                UDM_GETBUDDY = WM_USER + 106
                UDM_SETACCEL = WM_USER + 107
                UDM_GETACCEL = WM_USER + 108
                UDM_SETBASE = WM_USER + 109
                UDM_GETBASE = WM_USER + 110
                UDM_SETRANGE32 = WM_USER + 111
                UDM_GETRANGE32 = WM_USER + 112
                UDM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
                UDM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
                UDM_SETPOS32 = WM_USER + 113
                UDM_GETPOS32 = WM_USER + 114
                # WINCOMMCTRLAPI HWND WINAPI CreateUpDownControl(DWORD dwStyle, INT x, INT y, INT cx, INT cy,
                # HWND hParent, INT nID, HINSTANCE hInst,
                # HWND hBuddy,
                # INT nUpper, INT nLower, INT nPos);
                CreateUpDownControl = comctl32.CreateUpDownControl
                CreateUpDownControl.restype = HWND

                class _NM_UPDOWN(ctypes.Structure):
                    pass


                _NM_UPDOWN._fields_ = [
                    ('hdr', NMHDR),
                    ('iPos', INT),
                    ('iDelta', INT),
                ]
                NMUPDOWN = _NM_UPDOWN
                LPNMUPDOWN = POINTER(_NM_UPDOWN)
                UDN_DELTAPOS = UDN_FIRST - 1

                NM_UPDOWN = NMUPDOWN
                LPNM_UPDOWN = LPNMUPDOWN
            # END IF   NOUPDOWN

            # == == == PROGRESS CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == =

            if not defined(NOPROGRESS):
                if defined(_WIN32):
                    PROGRESS_CLASSA = "msctls_progress32"
                    PROGRESS_CLASSW = "msctls_progress32"

                    if defined(UNICODE):
                        PROGRESS_CLASS = PROGRESS_CLASSW
                    else:
                        PROGRESS_CLASS = PROGRESS_CLASSA
                    # END IF
                else:
                    PROGRESS_CLASS = "msctls_progress"
                # END IF

                # begin_r_commctrl
                PBS_SMOOTH = 0x01
                PBS_VERTICAL = 0x04

                # end_r_commctrl
                PBM_SETRANGE = WM_USER + 1
                PBM_SETPOS = WM_USER + 2
                PBM_DELTAPOS = WM_USER + 3
                PBM_SETSTEP = WM_USER + 4
                PBM_STEPIT = WM_USER + 5
                PBM_SETRANGE32 = WM_USER + 6


                class PBRANGE(ctypes.Structure):
                    pass


                PBRANGE._fields_ = [
                    ('iLow', INT),
                    ('iHigh', INT),
                ]
                PPBRANGE = POINTER(PBRANGE)
                PBM_GETRANGE = WM_USER + 7
                PBM_GETPOS = WM_USER + 8
                PBM_SETBARCOLOR = WM_USER + 9
                PBM_SETBKCOLOR = CCM_SETBKCOLOR

                # begin_r_commctrl

                if NTDDI_VERSION >= NTDDI_WINXP:
                    PBS_MARQUEE = 0x08
                # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

                # end_r_commctrl

                if NTDDI_VERSION >= NTDDI_WINXP:
                    PBM_SETMARQUEE = WM_USER + 10
                # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

                # begin_r_commctrl

                if NTDDI_VERSION >= NTDDI_VISTA:
                    PBS_SMOOTHREVERSE = 0x10
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                # end_r_commctrl

                if NTDDI_VERSION >= NTDDI_VISTA:
                    PBM_GETSTEP = WM_USER + 13
                    PBM_GETBKCOLOR = WM_USER + 14
                    PBM_GETBARCOLOR = WM_USER + 15
                    PBM_SETSTATE = WM_USER + 16
                    PBM_GETSTATE = WM_USER + 17
                    PBST_NORMAL = 0x0001
                    PBST_ERROR = 0x0002
                    PBST_PAUSED = 0x0003
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
            # END IF   NOPROGRESS

            # == == == HOTKEY CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == == =

            if not defined(NOHOTKEY):
                HOTKEYF_SHIFT = 0x01
                HOTKEYF_CONTROL = 0x02
                HOTKEYF_ALT = 0x04

                if defined(_MAC):
                    HOTKEYF_EXT = 0x80
                else:
                    HOTKEYF_EXT = 0x08
                # END IF
                HKCOMB_NONE = 0x0001
                HKCOMB_S = 0x0002
                HKCOMB_C = 0x0004
                HKCOMB_A = 0x0008
                HKCOMB_SC = 0x0010
                HKCOMB_SA = 0x0020
                HKCOMB_CA = 0x0040
                HKCOMB_SCA = 0x0080
                HKM_SETHOTKEY = WM_USER + 1
                HKM_GETHOTKEY = WM_USER + 2
                HKM_SETRULES = WM_USER + 3

                if defined(_WIN32):
                    HOTKEY_CLASSA = "msctls_hotkey32"
                    HOTKEY_CLASSW = "msctls_hotkey32"

                    if defined(UNICODE):
                        HOTKEY_CLASS = HOTKEY_CLASSW
                    else:
                        HOTKEY_CLASS = HOTKEY_CLASSA
                    # END IF
                else:
                    HOTKEY_CLASS = "msctls_hotkey"
                # END IF
            # END IF   NOHOTKEY

            # begin_r_commctrl

            # == == == COMMON CONTROL STYLES == == == == == == == == == == ==
            # == == == == == == == == == == == == ==
            CCS_TOP = 0x00000001
            CCS_NOMOVEY = 0x00000002
            CCS_BOTTOM = 0x00000003
            CCS_NORESIZE = 0x00000004
            CCS_NOPARENTALIGN = 0x00000008
            CCS_ADJUSTABLE = 0x00000020
            CCS_NODIVIDER = 0x00000040
            CCS_VERT = 0x00000080
            CCS_LEFT = CCS_VERT | CCS_TOP
            CCS_RIGHT = CCS_VERT | CCS_BOTTOM
            CCS_NOMOVEX = CCS_VERT | CCS_NOMOVEY

            # end_r_commctrl

            # == == == SysLink control == == == == == == == == == == == == ==
            # == == == == == == == =

            if defined(_WIN32):
                if NTDDI_VERSION >= NTDDI_WINXP:
                    INVALID_LINK_INDEX = - 1
                    MAX_LINKID_TEXT = 48
                    L_MAX_URL_LENGTH = 2048 + 32 + ctypes.sizeof(":\n")
                    WC_LINK = "SysLink"

                    # begin_r_commctrl
                    LWS_TRANSPARENT = 0x0001
                    LWS_IGNORERETURN = 0x0002

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        LWS_NOPREFIX = 0x0004
                        LWS_USEVISUALSTYLE = 0x0008
                        LWS_USECUSTOMTEXT = 0x0010
                        LWS_RIGHT = 0x0020
                    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                    # end_r_commctrl
                    LIF_ITEMINDEX = 0x00000001
                    LIF_STATE = 0x00000002
                    LIF_ITEMID = 0x00000004
                    LIF_URL = 0x00000008
                    LIS_FOCUSED = 0x00000001
                    LIS_ENABLED = 0x00000002
                    LIS_VISITED = 0x00000004

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        LIS_HOTTRACK = 0x00000008
                        LIS_DEFAULTCOLORS = 0x00000010
                    # END IF
                    class tagLITEM(ctypes.Structure):
                        pass


                    tagLITEM._fields_ = [
                        ('mask', UINT),
                        ('iLink', INT),
                        ('state', UINT),
                        ('stateMask', UINT),
                        ('szID', WCHAR * MAX_LINKID_TEXT),
                        ('szUrl', WCHAR * L_MAX_URL_LENGTH),
                    ]
                    LITEM = tagLITEM
                    PLITEM = POINTER(tagLITEM)


                    class tagLHITTESTINFO(ctypes.Structure):
                        pass


                    tagLHITTESTINFO._fields_ = [
                        ('pt', POINT),
                        ('item', LITEM),
                    ]
                    LHITTESTINFO = tagLHITTESTINFO
                    PLHITTESTINFO = POINTER(tagLHITTESTINFO)


                    class tagNMLINK(ctypes.Structure):
                        pass


                    tagNMLINK._fields_ = [
                        ('hdr', NMHDR),
                        ('item', LITEM),
                    ]
                    NMLINK = tagNMLINK
                    PNMLINK = POINTER(tagNMLINK)

                    # SysLink notifications

                    # NM_CLICK // wParam: control ID, lParam: PNMLINK, ret:
                    # ignored.

                    # LinkWindow messages
                    LM_HITTEST = WM_USER + 0x300
                    LM_GETIDEALHEIGHT = WM_USER + 0x301
                    LM_SETITEM = WM_USER + 0x302
                    LM_GETITEM = WM_USER + 0x303
                    LM_GETIDEALSIZE = LM_GETIDEALHEIGHT
                # END IF
            # END IF   _WIN32

            # == == == End SysLink control == == == == == == == == == == == ==
            # == == == == == == == == =

            # == == == LISTVIEW CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == =

            if not defined(NOLISTVIEW):
                if defined(_WIN32):
                    WC_LISTVIEWA = "SysListView32"
                    WC_LISTVIEWW = "SysListView32"

                    if defined(UNICODE):
                        WC_LISTVIEW = WC_LISTVIEWW
                    else:
                        WC_LISTVIEW = WC_LISTVIEWA
                    # END IF
                else:
                    WC_LISTVIEW = "SysListView"
                # END IF

                # begin_r_commctrl
                LVS_ICON = 0x0000
                LVS_REPORT = 0x0001
                LVS_SMALLICON = 0x0002
                LVS_LIST = 0x0003
                LVS_TYPEMASK = 0x0003
                LVS_SINGLESEL = 0x0004
                LVS_SHOWSELALWAYS = 0x0008
                LVS_SORTASCENDING = 0x0010
                LVS_SORTDESCENDING = 0x0020
                LVS_SHAREIMAGELISTS = 0x0040
                LVS_NOLABELWRAP = 0x0080
                LVS_AUTOARRANGE = 0x0100
                LVS_EDITLABELS = 0x0200
                LVS_OWNERDATA = 0x1000
                LVS_NOSCROLL = 0x2000
                LVS_TYPESTYLEMASK = 0xFC00
                LVS_ALIGNTOP = 0x0000
                LVS_ALIGNLEFT = 0x0800
                LVS_ALIGNMASK = 0x0C00
                LVS_OWNERDRAWFIXED = 0x0400
                LVS_NOCOLUMNHEADER = 0x4000
                LVS_NOSORTHEADER = 0x8000

                # end_r_commctrl
                LVM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT


                def ListView_SetUnicodeFormat(hwnd, fUnicode):
                    return SNDMSG(hwnd, LVM_SETUNICODEFORMAT, fUnicode, 0)


                LVM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT


                def ListView_GetUnicodeFormat(hwnd):
                    return SNDMSG(hwnd, LVM_GETUNICODEFORMAT, 0, 0)


                LVM_GETBKCOLOR = LVM_FIRST + 0


                def ListView_GetBkColor(hwnd):
                    return SNDMSG(hwnd, LVM_GETBKCOLOR, 0, 0)


                LVM_SETBKCOLOR = LVM_FIRST + 1


                def ListView_SetBkColor(hwnd, clrBk):
                    return SNDMSG(hwnd, LVM_SETBKCOLOR, 0, clrBk)


                LVM_GETIMAGELIST = LVM_FIRST + 2


                def ListView_GetImageList(hwnd, iImageList):
                    return SNDMSG(hwnd, LVM_GETIMAGELIST, iImageList, 0)


                LVSIL_NORMAL = 0
                LVSIL_SMALL = 1
                LVSIL_STATE = 2
                LVSIL_GROUPHEADER = 3
                LVM_SETIMAGELIST = LVM_FIRST + 3


                def ListView_SetImageList(hwnd, himl, iImageList):
                    return SNDMSG(hwnd, LVM_SETIMAGELIST, iImageList, himl)


                LVM_GETITEMCOUNT = LVM_FIRST + 4


                def ListView_GetItemCount(hwnd):
                    return SNDMSG(hwnd, LVM_GETITEMCOUNT, 0, 0)


                LVIF_TEXT = 0x00000001
                LVIF_IMAGE = 0x00000002
                LVIF_PARAM = 0x00000004
                LVIF_STATE = 0x00000008
                LVIF_INDENT = 0x00000010
                LVIF_NORECOMPUTE = 0x00000800

                if NTDDI_VERSION >= NTDDI_WINXP:
                    LVIF_GROUPID = 0x00000100
                    LVIF_COLUMNS = 0x00000200
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    LVIF_COLFMT = 0x00010000
                # END IF

                LVIS_FOCUSED = 0x0001
                LVIS_SELECTED = 0x0002
                LVIS_CUT = 0x0004
                LVIS_DROPHILITED = 0x0008
                LVIS_GLOW = 0x0010
                LVIS_ACTIVATING = 0x0020
                LVIS_OVERLAYMASK = 0x0F00
                LVIS_STATEIMAGEMASK = 0xF000


                def INDEXTOSTATEIMAGEMASK(i):
                    return i << 12

                I_INDENTCALLBACK = - 1


                class tagLVITEMA(ctypes.Structure):
                    pass


                _TEMP_tagLVITEMA._fields_ = [
                    ('mask', UINT),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('state', UINT),
                    ('stateMask', UINT),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('lParam', LPARAM),
                    ('iIndent', INT),

                ]
                if NTDDI_VERSION >= NTDDI_WINXP:
                    _TEMP_tagLVITEMA += [
                        ('iGroupId', INT),
                        ('cColumns', UINT),  # tile view columns
                        ('puColumns', PUINT)
                    ]
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP_tagLVITEMA += [
                        ('piColFmt', POINTER(INT)),
                        ('iGroup', INT),
                        # readonly. only valid for owner data.
                    ]
                # END IF

                tagLVITEMA._fields_ = _TEMP_tagLVITEMA


                LVITEMA = tagLVITEMA
                LPLVITEMA = POINTER(tagLVITEMA)

                class tagLVITEMW(ctypes.Structure):
                    pass


                _TEMP_tagLVITEMW = [
                    ('mask', UINT),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('state', UINT),
                    ('stateMask', UINT),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('lParam', LPARAM),
                    ('iIndent', INT),

                ]

                if NTDDI_VERSION >= NTDDI_WINXP:
                    _TEMP_tagLVITEMW += [
                        ('iGroupId', INT),
                        ('cColumns', UINT),  # tile view columns
                        ('puColumns', PUINT)
                    ]
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP_tagLVITEMW += [
                        ('piColFmt', POINTER(int)),
                        ('iGroup', INT),  # readonly. only valid for owner data.
                    ]
                # END IF

                tagLVITEMW._fields_ = _TEMP_tagLVITEMW
                LVITEMW = tagLVITEMW
                LPLVITEMW = POINTER(tagLVITEMW)

                LV_ITEMA = LVITEMA
                LV_ITEMW = LVITEMW

                if NTDDI_VERSION >= NTDDI_WINXP:
                    I_GROUPIDCALLBACK = - 1
                    I_GROUPIDNONE = - 2
                # END IF

                LVITEMA_V1_SIZE = CCSIZEOF_STRUCT(LVITEMA, LVITEMA.lParam)
                LVITEMW_V1_SIZE = CCSIZEOF_STRUCT(LVITEMW, LVITEMW.lParam)

                if NTDDI_VERSION >= NTDDI_VISTA:  # Will be unused downlevel, but ctypes.sizeof(LVITEMA) must be equal to ctypes.sizeof(LVITEMW)
                    LVITEMA_V5_SIZE = CCSIZEOF_STRUCT(LVITEMA, LVITEMA.puColumns)
                    LVITEMW_V5_SIZE = CCSIZEOF_STRUCT(LVITEMW, LVITEMW.puColumns)

                    if defined(UNICODE):
                        LVITEM_V5_SIZE = LVITEMW_V5_SIZE
                    else:
                        LVITEM_V5_SIZE = LVITEMA_V5_SIZE
                    # END IF
                # END IF

                if defined(UNICODE):
                    LVITEM = LVITEMW
                    LPLVITEM = LPLVITEMW
                    LVITEM_V1_SIZE = LVITEMW_V1_SIZE
                else:
                    LVITEM = LVITEMA
                    LPLVITEM = LPLVITEMA
                    LVITEM_V1_SIZE = LVITEMA_V1_SIZE
                # END IF

                LV_ITEM = LVITEM

                LPSTR_TEXTCALLBACKW = -1
                LPSTR_TEXTCALLBACKA = -1

                if defined(UNICODE):
                    LPSTR_TEXTCALLBACK = LPSTR_TEXTCALLBACKW
                else:
                    LPSTR_TEXTCALLBACK = LPSTR_TEXTCALLBACKA
                # END IF

                I_IMAGECALLBACK = -1
                I_IMAGENONE = -2

                if NTDDI_VERSION >= NTDDI_WINXP:
                    # For tileview
                    I_COLUMNSCALLBACK = -1
                # END IF

                LVM_GETITEMA = LVM_FIRST + 5
                LVM_GETITEMW = LVM_FIRST + 75

                if defined(UNICODE):
                    LVM_GETITEM = LVM_GETITEMW
                else:
                    LVM_GETITEM = LVM_GETITEMA
                # END IF


                def ListView_GetItem(hwnd, pitem):
                    return SNDMSG(hwnd, LVM_GETITEM, 0, ctypes.byref(pitem))


                LVM_SETITEMA = LVM_FIRST + 6
                LVM_SETITEMW = LVM_FIRST + 76

                if defined(UNICODE):
                    LVM_SETITEM = LVM_SETITEMW
                else:
                    LVM_SETITEM = LVM_SETITEMA
                # END IF


                def ListView_SetItem(hwnd, pitem):
                    return SNDMSG(hwnd, LVM_SETITEM, 0, ctypes.byref(pitem))


                LVM_INSERTITEMA = LVM_FIRST + 7
                LVM_INSERTITEMW = LVM_FIRST + 77

                if defined(UNICODE):
                    LVM_INSERTITEM = LVM_INSERTITEMW
                else:
                    LVM_INSERTITEM = LVM_INSERTITEMA
                # END IF


                def ListView_InsertItem(hwnd, pitem):
                    return SNDMSG(hwnd, LVM_INSERTITEM, 0, ctypes.byref(pitem))


                LVM_DELETEITEM = LVM_FIRST + 8


                def ListView_DeleteItem(hwnd, i):
                    return BOOLSNDMSG(hwnd, LVM_DELETEITEM, WPARAMINTi, 0L)
                LVM_DELETEALLITEMS = LVM_FIRST + 9


                def ListView_DeleteAllItems(hwnd):
                    return SNDMSG(hwnd, LVM_DELETEALLITEMS, 0, 0)


                LVM_GETCALLBACKMASK = LVM_FIRST + 10


                def ListView_GetCallbackMask(hwnd):
                    return SNDMSG(hwnd, LVM_GETCALLBACKMASK, 0, 0)


                LVM_SETCALLBACKMASK = LVM_FIRST + 11


                def ListView_SetCallbackMask(hwnd, mask):
                    return SNDMSG(hwnd, LVM_SETCALLBACKMASK, mask, 0)


                LVNI_ALL = 0x0000
                LVNI_FOCUSED = 0x0001
                LVNI_SELECTED = 0x0002
                LVNI_CUT = 0x0004
                LVNI_DROPHILITED = 0x0008
                LVNI_STATEMASK = (
                    LVNI_FOCUSED |
                    LVNI_SELECTED |
                    LVNI_CUT |
                    LVNI_DROPHILITED
                )
                LVNI_VISIBLEORDER = 0x0010
                LVNI_PREVIOUS = 0x0020
                LVNI_VISIBLEONLY = 0x0040
                LVNI_SAMEGROUPONLY = 0x0080
                LVNI_ABOVE = 0x0100
                LVNI_BELOW = 0x0200
                LVNI_TOLEFT = 0x0400
                LVNI_TORIGHT = 0x0800
                LVNI_DIRECTIONMASK = (
                    LVNI_ABOVE |
                    LVNI_BELOW |
                    LVNI_TOLEFT |
                    LVNI_TORIGHT
                )
                LVM_GETNEXTITEM = LVM_FIRST + 12


                def ListView_GetNextItem(hwnd, i, flags):
                    return SNDMSG(hwnd, LVM_GETNEXTITEM, i, MAKELPARAM(flags, 0))


                LVFI_PARAM = 0x0001
                LVFI_STRING = 0x0002
                LVFI_SUBSTRING = 0x0004
                LVFI_PARTIAL = 0x0008
                LVFI_WRAP = 0x0020
                LVFI_NEARESTXY = 0x0040

                class tagLVFINDINFOA(ctypes.Structure):
                    pass


                tagLVFINDINFOA._fields_ = [
                    ('flags', UINT),
                    ('psz', LPCSTR),
                    ('lParam', LPARAM),
                    ('pt', POINT),
                    ('vkDirection', UINT),
                ]
                LVFINDINFOA = tagLVFINDINFOA
                LPFINDINFOA = POINTER(tagLVFINDINFOA)


                class tagLVFINDINFOW(ctypes.Structure):
                    pass


                tagLVFINDINFOW._fields_ = [
                    ('flags', UINT),
                    ('psz', LPCWSTR),
                    ('lParam', LPARAM),
                    ('pt', POINT),
                    ('vkDirection', UINT),
                ]
                LVFINDINFOW = tagLVFINDINFOW
                LPFINDINFOW = POINTER(tagLVFINDINFOW)

                if defined(UNICODE):
                    LVFINDINFO = LVFINDINFOW
                else:
                    LVFINDINFO = LVFINDINFOA
                # END IF

                LV_FINDINFOA = LVFINDINFOA
                LV_FINDINFOW = LVFINDINFOW
                LV_FINDINFO = LVFINDINFO


                LVM_FINDITEMA = LVM_FIRST + 13
                LVM_FINDITEMW = LVM_FIRST + 83

                if defined(UNICODE):
                    LVM_FINDITEM = LVM_FINDITEMW
                else:
                    LVM_FINDITEM = LVM_FINDITEMA
                # END IF


                def ListView_FindItem(hwnd, iStart, plvfi):
                    return SNDMSG(hwnd, LVM_FINDITEM, iStart, ctypes.byref(plvfi))


                LVIR_BOUNDS = 0
                LVIR_ICON = 1
                LVIR_LABEL = 2
                LVIR_SELECTBOUNDS = 3
                LVM_GETITEMRECT = LVM_FIRST + 14


                def ListView_GetItemRect(hwnd, i, prc, code):
                    if prc:
                        prc.left = code

                    return SNDMSG(hwnd, LVM_GETITEMRECT, i, ctypes.byref(prc) if prc else NULL)


                LVM_SETITEMPOSITION = LVM_FIRST + 15


                def ListView_SetItemPosition(hwndLV, i, x, y):
                    return SNDMSG(hwndLV, LVM_SETITEMPOSITION, i, MAKELPARAM(x, y))
                LVM_GETITEMPOSITION = LVM_FIRST + 16


                def ListView_GetItemPosition(hwndLV, i, ppt):
                    return SNDMSG(hwndLV, LVM_GETITEMPOSITION, i, ctypes.byref(ppt))


                LVM_GETSTRINGWIDTHA = LVM_FIRST + 17
                LVM_GETSTRINGWIDTHW = LVM_FIRST + 87

                if defined(UNICODE):
                    LVM_GETSTRINGWIDTH = LVM_GETSTRINGWIDTHW
                else:
                    LVM_GETSTRINGWIDTH = LVM_GETSTRINGWIDTHA
                # END IF


                def ListView_GetStringWidth(hwndLV, psz):
                    return SNDMSG(hwndLV, LVM_GETSTRINGWIDTH, 0, psz)


                LVHT_NOWHERE = 0x00000001
                LVHT_ONITEMICON = 0x00000002
                LVHT_ONITEMLABEL = 0x00000004
                LVHT_ONITEMSTATEICON = 0x00000008
                LVHT_ONITEM = (
                    LVHT_ONITEMICON |
                    LVHT_ONITEMLABEL |
                    LVHT_ONITEMSTATEICON
                )
                LVHT_ABOVE = 0x00000008
                LVHT_BELOW = 0x00000010
                LVHT_TORIGHT = 0x00000020
                LVHT_TOLEFT = 0x00000040
                LVHT_EX_GROUP_HEADER = 0x10000000
                LVHT_EX_GROUP_FOOTER = 0x20000000
                LVHT_EX_GROUP_COLLAPSE = 0x40000000
                LVHT_EX_GROUP_BACKGROUND = 0x80000000
                LVHT_EX_GROUP_STATEICON = 0x01000000
                LVHT_EX_GROUP_SUBSETLINK = 0x02000000
                LVHT_EX_GROUP = (
                    LVHT_EX_GROUP_BACKGROUND |
                    LVHT_EX_GROUP_COLLAPSE |
                    LVHT_EX_GROUP_FOOTER |
                    LVHT_EX_GROUP_HEADER |
                    LVHT_EX_GROUP_STATEICON |
                    LVHT_EX_GROUP_SUBSETLINK
                )
                LVHT_EX_ONCONTENTS = 0x04000000
                LVHT_EX_FOOTER = 0x08000000


                class tagLVHITTESTINFO(ctypes.Structure):
                    pass


                _TEMP_tagLVHITTESTINFO = [
                    ('pt', POINT),
                    ('flags', UINT),
                    ('iItem', INT),
                    # this is was NOT in win95. valid only for
                    # LVM_SUBITEMHITTEST
                    ('iSubItem', INT),
                ]


                if NTDDI_VERSION >= NTDDI_VISTA:
                    # readonly. index of group. only valid for owner data.
                    _TEMP_tagLVHITTESTINFO += [('iGroup',INT)]
                # END IF

                tagLVHITTESTINFO._fields_ = _TEMP_tagLVHITTESTINFO
                LVHITTESTINFO = tagLVHITTESTINFO
                LPLVHITTESTINFO = POINTER(tagLVHITTESTINFO)
                LV_HITTESTINFO = LVHITTESTINFO
                LVHITTESTINFO_V1_SIZE = CCSIZEOF_STRUCT(LVHITTESTINFO, LVHITTESTINFO.iItem)
                LVM_HITTEST = LVM_FIRST + 18


                def ListView_HitTest(hwndLV, pinfo):
                    return SNDMSG(hwndLV, LVM_HITTEST, 0, ctypes.byref(pinfo))


                def ListView_HitTestEx(hwndLV, pinfo):
                    return SNDMSG(hwndLV, LVM_HITTEST, -1, ctypes.byref(pinfo))


                LVM_ENSUREVISIBLE = LVM_FIRST + 19


                def ListView_EnsureVisible(hwndLV, i, fPartialOK):
                    return SNDMSG(hwndLV, LVM_ENSUREVISIBLE, i, MAKELPARAM(fPartialOK, 0))


                LVM_SCROLL = LVM_FIRST + 20


                def ListView_Scroll(hwndLV, dx, dy):
                    return SNDMSG(hwndLV, LVM_SCROLL, dx, dy)


                LVM_REDRAWITEMS = LVM_FIRST + 21


                def ListView_RedrawItems(hwndLV, iFirst, iLast):
                    return SNDMSG(hwndLV, LVM_REDRAWITEMS, iFirst, iLast)


                LVA_DEFAULT = 0x0000
                LVA_ALIGNLEFT = 0x0001
                LVA_ALIGNTOP = 0x0002
                LVA_SNAPTOGRID = 0x0005
                LVM_ARRANGE = LVM_FIRST + 22


                def ListView_Arrange(hwndLV, code):
                    return SNDMSG(hwndLV, LVM_ARRANGE, code, 0)


                LVM_EDITLABELA = LVM_FIRST + 23
                LVM_EDITLABELW = LVM_FIRST + 118

                if defined(UNICODE):
                    LVM_EDITLABEL = LVM_EDITLABELW
                else:
                    LVM_EDITLABEL = LVM_EDITLABELA
                # END IF


                def ListView_EditLabel(hwndLV, i):
                    return SNDMSG(hwndLV, LVM_EDITLABEL, i, 0)


                LVM_GETEDITCONTROL = LVM_FIRST + 24


                def ListView_GetEditControl(hwndLV):
                    return SNDMSG(hwndLV, LVM_GETEDITCONTROL, 0, 0)


                class tagLVCOLUMNA(ctypes.Structure):
                    pass


                _TEMP_tagLVCOLUMNA = [
                    ('mask', UINT),
                    ('fmt', INT),
                    ('cx', INT),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iSubItem', INT),
                    ('iImage', INT),
                    ('iOrder', INT),
                ]


                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP_tagLVCOLUMNA += [
                        ('cxMin', INT),  # min snap point
                        ('cxDefault', INT),  # default snap point

                        # read only. ideal may not eqaul current width if auto
                        # sized (LVS_EX_AUTOSIZECOLUMNS) to a lesser width.
                        ('cxIdeal', INT)
                    ]
                # END IF

                tagLVCOLUMNA._fields_ = _TEMP_tagLVCOLUMNA
                LVCOLUMNA = tagLVCOLUMNA
                LPLVCOLUMNA = POINTER(tagLVCOLUMNA)


                class tagLVCOLUMNW(ctypes.Structure):
                    pass


                _TEMP_tagLVCOLUMNW = [
                    ('mask', UINT),
                    ('fmt', INT),
                    ('cx', INT),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iSubItem', INT),
                    ('iImage', INT),
                    ('iOrder', INT),
                ]

                if NTDDI_VERSION >= NTDDI_VISTA:
                    _TEMP_tagLVCOLUMNW += [
                        ('cxMin', INT),  # min snap point
                        ('cxDefault', INT),  # default snap point

                        # read only. ideal may not eqaul current width if auto
                        # sized (LVS_EX_AUTOSIZECOLUMNS) to a lesser width.
                        ('cxIdeal', INT)
                    ]
                # END IF

                tagLVCOLUMNW._fields_ = _TEMP_tagLVCOLUMNW
                LVCOLUMNW = tagLVCOLUMNW
                LPLVCOLUMNW = POINTER(tagLVCOLUMNW)

                LVCOLUMNA_V1_SIZE = CCSIZEOF_STRUCT(LVCOLUMNA, LVCOLUMNA.iSubItem)
                LVCOLUMNW_V1_SIZE = CCSIZEOF_STRUCT(LVCOLUMNW, LVCOLUMNW.iSubItem)


                if defined(UNICODE):
                    LVCOLUMN = LVCOLUMNW
                    LPLVCOLUMN = LPLVCOLUMNW
                    LVCOLUMN_V1_SIZE = LVCOLUMNW_V1_SIZE
                else:
                    LVCOLUMN = LVCOLUMNA
                    LPLVCOLUMN = LPLVCOLUMNA
                    LVCOLUMN_V1_SIZE = LVCOLUMNA_V1_SIZE
                # END IF

                LV_COLUMNA = LVCOLUMNA
                LV_COLUMNW = LVCOLUMNW
                LV_COLUMN = LVCOLUMN

                LVCF_FMT = 0x0001
                LVCF_WIDTH = 0x0002
                LVCF_TEXT = 0x0004
                LVCF_SUBITEM = 0x0008
                LVCF_IMAGE = 0x0010
                LVCF_ORDER = 0x0020

                if NTDDI_VERSION >= NTDDI_VISTA:
                    LVCF_MINWIDTH = 0x0040
                    LVCF_DEFAULTWIDTH = 0x0080
                    LVCF_IDEALWIDTH = 0x0100
                # END IF

                # LVCFMT_ flags up to FFFF are shared with the header control
                # (HDF_ flags).

                # Flags above FFFF are listview - specific.
                LVCFMT_LEFT = 0x0000
                LVCFMT_RIGHT = 0x0001
                LVCFMT_CENTER = 0x0002
                LVCFMT_JUSTIFYMASK = 0x0003
                LVCFMT_IMAGE = 0x0800
                LVCFMT_BITMAP_ON_RIGHT = 0x1000
                LVCFMT_COL_HAS_IMAGES = 0x8000

                if NTDDI_VERSION >= NTDDI_VISTA:
                    LVCFMT_FIXED_WIDTH = 0x00100
                    LVCFMT_NO_DPI_SCALE = 0x40000
                    LVCFMT_FIXED_RATIO = 0x80000

                    # The following flags
                    LVCFMT_LINE_BREAK = 0x100000
                    LVCFMT_FILL = 0x200000
                    LVCFMT_WRAP = 0x400000
                    LVCFMT_NO_TITLE = 0x800000
                    LVCFMT_TILE_PLACEMENTMASK = LVCFMT_LINE_BREAK | LVCFMT_FILL
                    LVCFMT_SPLITBUTTON = 0x1000000
                # END IF
                LVM_GETCOLUMNA = LVM_FIRST + 25
                LVM_GETCOLUMNW = LVM_FIRST + 95

                if defined(UNICODE):
                    LVM_GETCOLUMN = LVM_GETCOLUMNW
                else:
                    LVM_GETCOLUMN = LVM_GETCOLUMNA
                # END IF


                def ListView_GetColumn(hwnd, iCol, pcol):
                    return SNDMSG(hwnd, LVM_GETCOLUMN, iCol, ctypes.byref(pcol))


                LVM_SETCOLUMNA = LVM_FIRST + 26
                LVM_SETCOLUMNW = LVM_FIRST + 96

                if defined(UNICODE):
                    LVM_SETCOLUMN = LVM_SETCOLUMNW
                else:
                    LVM_SETCOLUMN = LVM_SETCOLUMNA
                # END IF


                def ListView_SetColumn(hwnd, iCol, pcol):
                    return SNDMSG(hwnd, LVM_SETCOLUMN, iCol, ctypes.byref(pcol))


                LVM_INSERTCOLUMNA = LVM_FIRST + 27
                LVM_INSERTCOLUMNW = LVM_FIRST + 97

                if defined(UNICODE):
                    LVM_INSERTCOLUMN = LVM_INSERTCOLUMNW
                else:
                    LVM_INSERTCOLUMN = LVM_INSERTCOLUMNA
                # END IF


                def ListView_InsertColumn(hwnd, iCol, pcol):
                    return SNDMSG(hwnd, LVM_INSERTCOLUMN, iCol, ctypes.byref(pcol))


                LVM_DELETECOLUMN = LVM_FIRST + 28


                def ListView_DeleteColumn(hwnd, iCol):
                    return SNDMSG(hwnd, LVM_DELETECOLUMN, iCol, 0)


                LVM_GETCOLUMNWIDTH = LVM_FIRST + 29


                def ListView_GetColumnWidth(hwnd, iCol):
                    return SNDMSG(hwnd, LVM_GETCOLUMNWIDTH, iCol, 0)


                LVSCW_AUTOSIZE = - 1
                LVSCW_AUTOSIZE_USEHEADER = - 2
                LVM_SETCOLUMNWIDTH = LVM_FIRST + 30


                def ListView_SetColumnWidth(hwnd, iCol, cx):
                    return SNDMSG(hwnd, LVM_SETCOLUMNWIDTH, iCol, MAKELPARAM(cx, 0))


                LVM_GETHEADER = LVM_FIRST + 31


                def ListView_GetHeader(hwnd):
                    return SNDMSG(hwnd, LVM_GETHEADER, 0, 0)


                LVM_CREATEDRAGIMAGE = LVM_FIRST + 33


                def ListView_CreateDragImage(hwnd, i, lpptUpLeft):
                    return SNDMSG(hwnd, LVM_CREATEDRAGIMAGE, i, lpptUpLeft)


                LVM_GETVIEWRECT = LVM_FIRST + 34


                def ListView_GetViewRect(hwnd, prc):
                    return SNDMSG(hwnd, LVM_GETVIEWRECT, 0, ctypes.byref(prc))


                LVM_GETTEXTCOLOR = LVM_FIRST + 35


                def ListView_GetTextColor(hwnd):
                    return SNDMSG(hwnd, LVM_GETTEXTCOLOR, 0, 0)


                LVM_SETTEXTCOLOR = LVM_FIRST + 36


                def ListView_SetTextColor(hwnd, clrText):
                    return SNDMSG(hwnd, LVM_SETTEXTCOLOR, 0, clrText)


                LVM_GETTEXTBKCOLOR = LVM_FIRST + 37


                def ListView_GetTextBkColor(hwnd):
                    return SNDMSG(hwnd, LVM_GETTEXTBKCOLOR, 0, 0)


                LVM_SETTEXTBKCOLOR = LVM_FIRST + 38


                def ListView_SetTextBkColor(hwnd, clrTextBk):
                    return SNDMSG(hwnd, LVM_SETTEXTBKCOLOR, 0, clrTextBk)


                LVM_GETTOPINDEX = LVM_FIRST + 39


                def ListView_GetTopIndex(hwndLV):
                    return SNDMSG(hwndLV, LVM_GETTOPINDEX, 0, 0)


                LVM_GETCOUNTPERPAGE = LVM_FIRST + 40


                def ListView_GetCountPerPage(hwndLV):
                    return INTSNDMSG(hwndLV, LVM_GETCOUNTPERPAGE, 0, 0)


                LVM_GETORIGIN = LVM_FIRST + 41


                def ListView_GetOrigin(hwndLV, ppt):
                    return SNDMSG(hwndLV, LVM_GETORIGIN, 0, ctypes.byref(ppt))


                LVM_UPDATE = LVM_FIRST + 42


                def ListView_Update(hwndLV, i):
                    return SNDMSG(hwndLV, LVM_UPDATE, i, 0)


                LVM_SETITEMSTATE = LVM_FIRST + 43


                def ListView_SetItemState(hwndLV, i, data, mask):
                    _macro_lvi = LV_ITEM()
                    _macro_lvi.stateMask = mask
                    _macro_lvi.state = data

                    return SNDMSG(hwndLV, LVM_SETITEMSTATE, i, _macro_lvi)


                def ListView_SetCheckState(hwndLV, i, fCheck):
                    return ListView_SetItemState(hwndLV, i, INDEXTOSTATEIMAGEMASK(2 if fCheck else 1), LVIS_STATEIMAGEMASK)


                LVM_GETITEMSTATE = LVM_FIRST + 44


                def ListView_GetItemState(hwndLV, i, mask):
                    return SNDMSG(hwndLV, LVM_GETITEMSTATE, i, mask)


                def ListView_GetCheckState(hwndLV, i):
                    return (SNDMSG(hwndLV, LVM_GETITEMSTATE, i, LVIS_STATEIMAGEMASK) >> 12) - 1


                LVM_GETITEMTEXTA = LVM_FIRST + 45
                LVM_GETITEMTEXTW = LVM_FIRST + 115

                if defined(UNICODE):
                    LVM_GETITEMTEXT = LVM_GETITEMTEXTW
                else:
                    LVM_GETITEMTEXT = LVM_GETITEMTEXTA
                # END IF


                def ListView_GetItemText(hwndLV, i, iSubItem_, pszText_, cchTextMax_):
                    _macro_lvi = LV_ITEM()
                    _macro_lvi.iSubItem = iSubItem_
                    _macro_lvi.cchTextMax = cchTextMax_
                    _macro_lvi.pszText = pszText_
                    return SNDMSG(hwndLV, LVM_GETITEMTEXT, i, _macro_lvi)


                LVM_SETITEMTEXTA = LVM_FIRST + 46
                LVM_SETITEMTEXTW = LVM_FIRST + 116

                if defined(UNICODE):
                    LVM_SETITEMTEXT = LVM_SETITEMTEXTW
                else:
                    LVM_SETITEMTEXT = LVM_SETITEMTEXTA
                # END IF


                def ListView_SetItemText(hwndLV, i, iSubItem_, pszText_):
                    _macro_lvi = LV_ITEM()
                    _macro_lvi.iSubItem = iSubItem_
                    _macro_lvi.pszText = pszText_

                    return SNDMSG(hwndLV, LVM_SETITEMTEXT, i, _macro_lvi)

                # these flags only apply to LVS_OWNERDATA listviews in report
                # or list mode
                LVSICF_NOINVALIDATEALL = 0x00000001
                LVSICF_NOSCROLL = 0x00000002
                LVM_SETITEMCOUNT = LVM_FIRST + 47


                def ListView_SetItemCount(hwndLV, cItems):
                    return SNDMSG(hwndLV, LVM_SETITEMCOUNT, WPARAMcItems, 0)


                def ListView_SetItemCountEx(hwndLV, cItems, dwFlags):
                    return SNDMSG(hwndLV, LVM_SETITEMCOUNT, cItems, dwFlags)


                PFNLVCOMPARE = CALLBACK(INT, POINTER(INT), INT)
                LVM_SORTITEMS = LVM_FIRST + 48


                def ListView_SortItems(hwndLV, _pfnCompare, _lPrm):
                    return SNDMSG(hwndLV, LVM_SORTITEMS, _lPrm, _pfnCompare)


                LVM_SETITEMPOSITION32 = LVM_FIRST + 49


                def ListView_SetItemPosition32(hwndLV, i, x0, y0):
                    ptNewPos = POINT
                    ptNewPos.x = x0
                    ptNewPos.y = y0

                    return SNDMSG(hwndLV, LVM_SETITEMPOSITION32, i, ptNewPos)

                LVM_GETSELECTEDCOUNT = LVM_FIRST + 50


                def ListView_GetSelectedCount(hwndLV):
                    return SNDMSG(hwndLV, LVM_GETSELECTEDCOUNT, 0, 0)

                LVM_GETITEMSPACING = LVM_FIRST + 51


                def ListView_GetItemSpacing(hwndLV, fSmall):
                    return SNDMSG(hwndLV, LVM_GETITEMSPACING, fSmall, 0)

                LVM_GETISEARCHSTRINGA = LVM_FIRST + 52
                LVM_GETISEARCHSTRINGW = LVM_FIRST + 117

                if defined(UNICODE):
                    LVM_GETISEARCHSTRING = LVM_GETISEARCHSTRINGW
                else:
                    LVM_GETISEARCHSTRING = LVM_GETISEARCHSTRINGA
                # END IF


                def ListView_GetISearchString(hwndLV, lpsz):
                    return SNDMSG(hwndLV, LVM_GETISEARCHSTRING, 0, lpsz)
                LVM_SETICONSPACING = LVM_FIRST + 53

                # - 1 for cx and cy means we'll use the default
                # (system settings)

                # 0 for cx or cy means use the current setting
                # (allows you to change just one param)


                def ListView_SetIconSpacing(hwndLV, cx, cy):
                    return SNDMSG(hwndLV, LVM_SETICONSPACING, 0, MAKELONG(cx, cy))
                LVM_SETEXTENDEDLISTVIEWSTYLE = LVM_FIRST + 54


                def ListView_SetExtendedListViewStyle(hwndLV, dw):
                    return SNDMSG(hwndLV, LVM_SETEXTENDEDLISTVIEWSTYLE, 0, dw)


                def ListView_SetExtendedListViewStyleEx(hwndLV, dwMask, dw):
                    return SNDMSG(hwndLV, LVM_SETEXTENDEDLISTVIEWSTYLE, dwMask, dw)

                LVM_GETEXTENDEDLISTVIEWSTYLE = LVM_FIRST + 55


                def ListView_GetExtendedListViewStyle(hwndLV):
                    return SNDMSG(hwndLV, LVM_GETEXTENDEDLISTVIEWSTYLE, 0, 0)

                LVS_EX_GRIDLINES = 0x00000001
                LVS_EX_SUBITEMIMAGES = 0x00000002
                LVS_EX_CHECKBOXES = 0x00000004
                LVS_EX_TRACKSELECT = 0x00000008
                LVS_EX_HEADERDRAGDROP = 0x00000010
                LVS_EX_FULLROWSELECT = 0x00000020
                LVS_EX_ONECLICKACTIVATE = 0x00000040
                LVS_EX_TWOCLICKACTIVATE = 0x00000080
                LVS_EX_FLATSB = 0x00000100
                LVS_EX_REGIONAL = 0x00000200
                LVS_EX_INFOTIP = 0x00000400
                LVS_EX_UNDERLINEHOT = 0x00000800
                LVS_EX_UNDERLINECOLD = 0x00001000
                LVS_EX_MULTIWORKAREAS = 0x00002000
                LVS_EX_LABELTIP = 0x00004000
                LVS_EX_BORDERSELECT = 0x00008000

                if NTDDI_VERSION >= NTDDI_WINXP:
                    LVS_EX_DOUBLEBUFFER = 0x00010000
                    LVS_EX_HIDELABELS = 0x00020000
                    LVS_EX_SINGLEROW = 0x00040000
                    LVS_EX_SNAPTOGRID = 0x00080000
                    LVS_EX_SIMPLESELECT = 0x00100000
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    LVS_EX_JUSTIFYCOLUMNS = 0x00200000
                    LVS_EX_TRANSPARENTBKGND = 0x00400000
                    LVS_EX_TRANSPARENTSHADOWTEXT = 0x00800000
                    LVS_EX_AUTOAUTOARRANGE = 0x01000000
                    LVS_EX_HEADERINALLVIEWS = 0x02000000
                    LVS_EX_AUTOCHECKSELECT = 0x08000000
                    LVS_EX_AUTOSIZECOLUMNS = 0x10000000
                    LVS_EX_COLUMNSNAPPOINTS = 0x40000000
                    LVS_EX_COLUMNOVERFLOW = 0x80000000
                # END IF
                LVM_GETSUBITEMRECT = LVM_FIRST + 56


                def ListView_GetSubItemRect(hwnd, iItem, iSubItem, code, prc):
                    return BOOLSNDMSG(hwnd, LVM_GETSUBITEMRECT, WPARAMINTiItem, (prc ? (((LPRECTprc) - >top = iSubItem), ((LPRECTprc) - >left = code), LPARAMprc) : LPARAMLPRECTNULL))
                LVM_SUBITEMHITTEST = LVM_FIRST + 57


                def ListView_SubItemHitTest(hwnd, plvhti):
                    return INTSNDMSGhwnd, LVM_SUBITEMHITTEST, 0, LPARAMLPLVHITTESTINFOplvhti


                def ListView_SubItemHitTestEx(hwnd, plvhti):
                    return INTSNDMSGhwnd, LVM_SUBITEMHITTEST, WPARAM - 1, LPARAMLPLVHITTESTINFOplvhti
                LVM_SETCOLUMNORDERARRAY = LVM_FIRST + 58


                def ListView_SetColumnOrderArray(hwnd, iCount, pi):
                    return BOOLSNDMSGhwnd, LVM_SETCOLUMNORDERARRAY, WPARAMiCount, LPARAMLPINTpi
                LVM_GETCOLUMNORDERARRAY = LVM_FIRST + 59


                def ListView_GetColumnOrderArray(hwnd, iCount, pi):
                    return BOOLSNDMSGhwnd, LVM_GETCOLUMNORDERARRAY, WPARAMiCount, LPARAMLPINTpi
                LVM_SETHOTITEM = LVM_FIRST + 60


                def ListView_SetHotItem(hwnd, i):
                    return INTSNDMSG(hwnd, LVM_SETHOTITEM, WPARAMi, 0)
                LVM_GETHOTITEM = LVM_FIRST + 61


                def ListView_GetHotItem(hwnd):
                    return INTSNDMSG(hwnd, LVM_GETHOTITEM, 0, 0)
                LVM_SETHOTCURSOR = LVM_FIRST + 62


                def ListView_SetHotCursor(hwnd, hcur):
                    return HCURSORSNDMSGhwnd, LVM_SETHOTCURSOR, 0, LPARAMhcur
                LVM_GETHOTCURSOR = LVM_FIRST + 63


                def ListView_GetHotCursor(hwnd):
                    return HCURSORSNDMSG(hwnd, LVM_GETHOTCURSOR, 0, 0)
                LVM_APPROXIMATEVIEWRECT = LVM_FIRST + 64


                def ListView_ApproximateViewRect(hwnd, iWidth, iHeight, iCount):
                    return DWORDSNDMSGhwnd, LVM_APPROXIMATEVIEWRECT, WPARAMiCount, MAKELPARAMiWidth, iHeight
                LV_MAX_WORKAREAS = 16
                LVM_SETWORKAREAS = LVM_FIRST + 65


                def ListView_SetWorkAreas(hwnd, nWorkAreas, prc):
                    return BOOLSNDMSGhwnd, LVM_SETWORKAREAS, WPARAMINTnWorkAreas, LPARAMRECT *prc
                LVM_GETWORKAREAS = LVM_FIRST + 70


                def ListView_GetWorkAreas(hwnd, nWorkAreas, prc):
                    return BOOLSNDMSGhwnd, LVM_GETWORKAREAS, WPARAMINTnWorkAreas, LPARAMRECT *prc
                LVM_GETNUMBEROFWORKAREAS = LVM_FIRST + 73


                def ListView_GetNumberOfWorkAreas(hwnd, pnWorkAreas):
                    return BOOLSNDMSGhwnd, LVM_GETNUMBEROFWORKAREAS, 0, LPARAMUINT *pnWorkAreas
                LVM_GETSELECTIONMARK = LVM_FIRST + 66


                def ListView_GetSelectionMark(hwnd):
                    return INTSNDMSG(hwnd, LVM_GETSELECTIONMARK, 0, 0)
                LVM_SETSELECTIONMARK = LVM_FIRST + 67


                def ListView_SetSelectionMark(hwnd, i):
                    return INTSNDMSGhwnd, LVM_SETSELECTIONMARK, 0, LPARAMi
                LVM_SETHOVERTIME = LVM_FIRST + 71


                def ListView_SetHoverTime(hwndLV, dwHoverTimeMs):
                    return DWORDSNDMSGhwndLV, LVM_SETHOVERTIME, 0, LPARAMdwHoverTimeMs
                LVM_GETHOVERTIME = LVM_FIRST + 72


                def ListView_GetHoverTime(hwndLV):
                    return DWORDSNDMSG(hwndLV, LVM_GETHOVERTIME, 0, 0)
                LVM_SETTOOLTIPS = LVM_FIRST + 74


                def ListView_SetToolTips(hwndLV, hwndNewHwnd):
                    return HWNDSNDMSG(hwndLV, LVM_SETTOOLTIPS, WPARAMhwndNewHwnd, 0)
                LVM_GETTOOLTIPS = LVM_FIRST + 78


                def ListView_GetToolTips(hwndLV):
                    return HWNDSNDMSG(hwndLV, LVM_GETTOOLTIPS, 0, 0)
                LVM_SORTITEMSEX = LVM_FIRST + 81


                def ListView_SortItemsEx(hwndLV, _pfnCompare, _lPrm):
                    return BOOLSNDMSGhwndLV, LVM_SORTITEMSEX, WPARAMLPARAM_lPrm, LPARAMPFNLVCOMPARE_pfnCompare
                class tagLVBKIMAGEA(ctypes.Structure):
                    pass


                tagLVBKIMAGEA._fields_ = [
                    ('ulFlags', ULONG), # LVBKIF_*
                    ('hbm', HBITMAP),
                    ('pszImage', LPSTR),
                    ('cchImageMax', UINT),
                    ('xOffsetPercent', INT),
                    ('yOffsetPercent', INT),
                ]
                LVBKIMAGEA = tagLVBKIMAGEA
                LPLVBKIMAGEA = POINTER(tagLVBKIMAGEA)
                class tagLVBKIMAGEW(ctypes.Structure):
                    pass


                tagLVBKIMAGEW._fields_ = [
                    ('ulFlags', ULONG), # LVBKIF_*
                    ('hbm', HBITMAP),
                    ('pszImage', LPWSTR),
                    ('cchImageMax', UINT),
                    ('xOffsetPercent', INT),
                    ('yOffsetPercent', INT),
                ]
                LVBKIMAGEW = tagLVBKIMAGEW
                LPLVBKIMAGEW = POINTER(tagLVBKIMAGEW)
                LVBKIF_SOURCE_NONE = 0x00000000
                LVBKIF_SOURCE_HBITMAP = 0x00000001
                LVBKIF_SOURCE_URL = 0x00000002
                LVBKIF_SOURCE_MASK = 0x00000003
                LVBKIF_STYLE_NORMAL = 0x00000000
                LVBKIF_STYLE_TILE = 0x00000010
                LVBKIF_STYLE_MASK = 0x00000010

                if NTDDI_VERSION >= NTDDI_WINXP:
                    LVBKIF_FLAG_TILEOFFSET = 0x00000100
                    LVBKIF_TYPE_WATERMARK = 0x10000000
                    LVBKIF_FLAG_ALPHABLEND = 0x20000000
                # END IF
                LVM_SETBKIMAGEA = LVM_FIRST + 68
                LVM_SETBKIMAGEW = LVM_FIRST + 138
                LVM_GETBKIMAGEA = LVM_FIRST + 69
                LVM_GETBKIMAGEW = LVM_FIRST + 139

                if NTDDI_VERSION >= NTDDI_WINXP:
                    LVM_SETSELECTEDCOLUMN = LVM_FIRST + 140


                    def ListView_SetSelectedColumn(hwnd, iCol):
                        return SNDMSG(hwnd, LVM_SETSELECTEDCOLUMN, WPARAMiCol, 0)
                    LV_VIEW_ICON = 0x0000
                    LV_VIEW_DETAILS = 0x0001
                    LV_VIEW_SMALLICON = 0x0002
                    LV_VIEW_LIST = 0x0003
                    LV_VIEW_TILE = 0x0004
                    LV_VIEW_MAX = 0x0004
                    LVM_SETVIEW = LVM_FIRST + 142


                    def ListView_SetView(hwnd, iView):
                        return DWORDSNDMSG(hwnd, LVM_SETVIEW, WPARAMDWORDiView, 0)
                    LVM_GETVIEW = LVM_FIRST + 143


                    def ListView_GetView(hwnd):
                        return DWORDSNDMSG(hwnd, LVM_GETVIEW, 0, 0)
                    LVGF_NONE = 0x00000000
                    LVGF_HEADER = 0x00000001
                    LVGF_FOOTER = 0x00000002
                    LVGF_STATE = 0x00000004
                    LVGF_ALIGN = 0x00000008
                    LVGF_GROUPID = 0x00000010

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        LVGF_SUBTITLE = 0x00000100
                        LVGF_TASK = 0x00000200
                        LVGF_DESCRIPTIONTOP = 0x00000400
                        LVGF_DESCRIPTIONBOTTOM = 0x00000800
                        LVGF_TITLEIMAGE = 0x00001000
                        LVGF_EXTENDEDIMAGE = 0x00002000
                        LVGF_ITEMS = 0x00004000
                        LVGF_SUBSET = 0x00008000
                        LVGF_SUBSETITEMS = 0x00010000
                    # END IF
                    LVGS_NORMAL = 0x00000000
                    LVGS_COLLAPSED = 0x00000001
                    LVGS_HIDDEN = 0x00000002
                    LVGS_NOHEADER = 0x00000004
                    LVGS_COLLAPSIBLE = 0x00000008
                    LVGS_FOCUSED = 0x00000010
                    LVGS_SELECTED = 0x00000020
                    LVGS_SUBSETED = 0x00000040
                    LVGS_SUBSETLINKFOCUSED = 0x00000080
                    LVGA_HEADER_LEFT = 0x00000001
                    LVGA_HEADER_CENTER = 0x00000002
                    LVGA_HEADER_RIGHT = 0x00000004
                    LVGA_FOOTER_LEFT = 0x00000008
                    LVGA_FOOTER_CENTER = 0x00000010
                    LVGA_FOOTER_RIGHT = 0x00000020
                    class tagLVGROUP(ctypes.Structure):
                        pass


                    tagLVGROUP._fields_ = [
                        ('cbSize', UINT),
                        ('mask', UINT),
                        ('pszHeader', LPWSTR),
                        ('cchHeader', INT),
                        ('pszFooter', LPWSTR),
                        ('cchFooter', INT),
                        ('iGroupId', INT),
                        ('stateMask', UINT),
                        ('state', UINT),
                        ('uAlign', UINT),
                            ('pszSubtitle', LPWSTR),
                            ('cchSubtitle', UINT),
                            ('pszTask', LPWSTR),
                            ('cchTask', UINT),
                            ('pszDescriptionTop', LPWSTR),
                            ('cchDescriptionTop', UINT),
                            ('pszDescriptionBottom', LPWSTR),
                            ('cchDescriptionBottom', UINT),
                            ('iTitleImage', INT),
                            ('iExtendedImage', INT),
                            ('iFirstItem', INT), # Read only
                            ('cItems', UINT), # Read only
                            ('pszSubsetTitle', LPWSTR), # NULL if group is not subset
                            ('cchSubsetTitle', UINT),
                    ]
                    LVGROUP = tagLVGROUP
                    PLVGROUP = POINTER(tagLVGROUP)

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        LVGROUP_V5_SIZE = CCSIZEOF_STRUCT(LVGROUP, uAlign)
                    # END IF
                    LVM_INSERTGROUP = LVM_FIRST + 145


                    def ListView_InsertGroup(hwnd, index, pgrp):
                        return SNDMSGhwnd, LVM_INSERTGROUP, WPARAMindex, LPARAMpgrp
                    LVM_SETGROUPINFO = LVM_FIRST + 147


                    def ListView_SetGroupInfo(hwnd, iGroupId, pgrp):
                        return SNDMSGhwnd, LVM_SETGROUPINFO, WPARAMiGroupId, LPARAMpgrp
                    LVM_GETGROUPINFO = LVM_FIRST + 149


                    def ListView_GetGroupInfo(hwnd, iGroupId, pgrp):
                        return SNDMSGhwnd, LVM_GETGROUPINFO, WPARAMiGroupId, LPARAMpgrp
                    LVM_REMOVEGROUP = LVM_FIRST + 150


                    def ListView_RemoveGroup(hwnd, iGroupId):
                        return SNDMSG(hwnd, LVM_REMOVEGROUP, WPARAMiGroupId, 0)
                    LVM_MOVEGROUP = LVM_FIRST + 151


                    def ListView_MoveGroup(hwnd, iGroupId, toIndex):
                        return SNDMSGhwnd, LVM_MOVEGROUP, WPARAMiGroupId, LPARAMtoIndex
                    LVM_GETGROUPCOUNT = LVM_FIRST + 152


                    def ListView_GetGroupCount(hwnd):
                        return SNDMSG(hwnd, LVM_GETGROUPCOUNT, WPARAM0, LPARAM0)
                    LVM_GETGROUPINFOBYINDEX = LVM_FIRST + 153


                    def ListView_GetGroupInfoByIndex(hwnd, iIndex, pgrp):
                        return SNDMSGhwnd, LVM_GETGROUPINFOBYINDEX, WPARAMiIndex, LPARAMpgrp
                    LVM_MOVEITEMTOGROUP = LVM_FIRST + 154


                    def ListView_MoveItemToGroup(hwnd, idItemFrom, idGroupTo):
                        return SNDMSGhwnd, LVM_MOVEITEMTOGROUP, WPARAMidItemFrom, LPARAMidGroupTo
                    LVGGR_GROUP = 0
                    LVGGR_HEADER = 1
                    LVGGR_LABEL = 2
                    LVGGR_SUBSETLINK = 3
                    LVM_GETGROUPRECT = LVM_FIRST + 98


                    def ListView_GetGroupRect(hwnd, iGroupId, type, prc):
                        return SNDMSG(hwnd, LVM_GETGROUPRECT, WPARAMiGroupId, (prc ? ((RECT*prc) - >top = type), LPARAMRECT*prc : LPARAMRECT*NULL))
                    LVGMF_NONE = 0x00000000
                    LVGMF_BORDERSIZE = 0x00000001
                    LVGMF_BORDERCOLOR = 0x00000002
                    LVGMF_TEXTCOLOR = 0x00000004
                    class tagLVGROUPMETRICS(ctypes.Structure):
                        pass


                    tagLVGROUPMETRICS._fields_ = [
                        ('cbSize', UINT),
                        ('mask', UINT),
                        ('Left', UINT),
                        ('Top', UINT),
                        ('Right', UINT),
                        ('Bottom', UINT),
                        ('crLeft', COLORREF),
                        ('crTop', COLORREF),
                        ('crRight', COLORREF),
                        ('crBottom', COLORREF),
                        ('crHeader', COLORREF),
                        ('crFooter', COLORREF),
                    ]
                    LVGROUPMETRICS = tagLVGROUPMETRICS
                    PLVGROUPMETRICS = POINTER(tagLVGROUPMETRICS)
                    LVM_SETGROUPMETRICS = LVM_FIRST + 155


                    def ListView_SetGroupMetrics(hwnd, pGroupMetrics):
                        return SNDMSGhwnd, LVM_SETGROUPMETRICS, 0, LPARAMpGroupMetrics
                    LVM_GETGROUPMETRICS = LVM_FIRST + 156


                    def ListView_GetGroupMetrics(hwnd, pGroupMetrics):
                        return SNDMSGhwnd, LVM_GETGROUPMETRICS, 0, LPARAMpGroupMetrics
                    LVM_ENABLEGROUPVIEW = LVM_FIRST + 157


                    def ListView_EnableGroupView(hwnd, fEnable):
                        return SNDMSG(hwnd, LVM_ENABLEGROUPVIEW, WPARAMfEnable, 0)
                    (CALLBACK = INT
                    PFNLVGROUPCOMPARE)(int = POINTER(INT)
                    int = INT
                    VOID = INT
                    ) = POINTER(INT)
                    LVM_SORTGROUPS = LVM_FIRST + 158


                    def ListView_SortGroups(hwnd, _pfnGroupCompate, _plv):
                        return SNDMSGhwnd, LVM_SORTGROUPS, WPARAM_pfnGroupCompate, LPARAM_plv
                    class tagLVINSERTGROUPSORTED(ctypes.Structure):
                        pass


                    tagLVINSERTGROUPSORTED._fields_ = [
                        ('pfnGroupCompare', PFNLVGROUPCOMPARE),
                        ('pvData', POINTER(VOID)),
                        ('lvGroup', LVGROUP),
                    ]
                    LVINSERTGROUPSORTED = tagLVINSERTGROUPSORTED
                    PLVINSERTGROUPSORTED = POINTER(tagLVINSERTGROUPSORTED)
                    LVM_INSERTGROUPSORTED = LVM_FIRST + 159


                    def ListView_InsertGroupSorted(hwnd, structInsert):
                        return SNDMSG(hwnd, LVM_INSERTGROUPSORTED, WPARAMstructInsert, 0)
                    LVM_REMOVEALLGROUPS = LVM_FIRST + 160


                    def ListView_RemoveAllGroups(hwnd):
                        return SNDMSG(hwnd, LVM_REMOVEALLGROUPS, 0, 0)
                    LVM_HASGROUP = LVM_FIRST + 161


                    def ListView_HasGroup(hwnd, dwGroupId):
                        return SNDMSG(hwnd, LVM_HASGROUP, dwGroupId, 0)


                    def ListView_SetGroupState(hwnd, dwGroupId, dwMask, dwState):
                        return { LVGROUP _macro_lvg; _macro_lvg.cbSize = ctypes.sizeof_macro_lvg; _macro_lvg.mask = LVGF_STATE; _macro_lvg.stateMask = dwMask; _macro_lvg.state = LPARAMLVGROP * & _macro_lvg); }
                    LVM_GETGROUPSTATE = LVM_FIRST + 92


                    def ListView_GetGroupState(hwnd, dwGroupId, dwMask):
                        return UINT SNDMSGhwnd, LVM_GETGROUPSTATE, WPARAMdwGroupId, LPARAMdwMask
                    LVM_GETFOCUSEDGROUP = LVM_FIRST + 93


                    def ListView_GetFocusedGroup(hwnd):
                        return SNDMSG(hwnd, LVM_GETFOCUSEDGROUP, 0, 0)
                    LVTVIF_AUTOSIZE = 0x00000000
                    LVTVIF_FIXEDWIDTH = 0x00000001
                    LVTVIF_FIXEDHEIGHT = 0x00000002
                    LVTVIF_FIXEDSIZE = 0x00000003

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        LVTVIF_EXTENDED = 0x00000004
                    # END IF
                    LVTVIM_TILESIZE = 0x00000001
                    LVTVIM_COLUMNS = 0x00000002
                    LVTVIM_LABELMARGIN = 0x00000004
                    class tagLVTILEVIEWINFO(ctypes.Structure):
                        pass


                    tagLVTILEVIEWINFO._fields_ = [
                        ('cbSize', UINT),
                        ('dwMask', DWORD), # LVTVIM_*
                        ('dwFlags', DWORD), # LVTVIF_*
                        ('sizeTile', SIZE),
                        ('cLines', INT),
                        ('rcLabelMargin', RECT),
                    ]
                    LVTILEVIEWINFO = tagLVTILEVIEWINFO
                    PLVTILEVIEWINFO = POINTER(tagLVTILEVIEWINFO)
                    class tagLVTILEINFO(ctypes.Structure):
                        pass


                    tagLVTILEINFO._fields_ = [
                        ('cbSize', UINT),
                        ('iItem', INT),
                        ('cColumns', UINT),
                        ('puColumns', PUINT),
                            ('piColFmt', POINTER(int)),
                    ]
                    LVTILEINFO = tagLVTILEINFO
                    PLVTILEINFO = POINTER(tagLVTILEINFO)

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        pass
                    # END IF
                    LVTILEINFO_V5_SIZE = CCSIZEOF_STRUCT(
                        LVTILEINFO,
                        puColumns,
                    )
                    LVM_SETTILEVIEWINFO = LVM_FIRST + 162


                    def ListView_SetTileViewInfo(hwnd, ptvi):
                        return SNDMSGhwnd, LVM_SETTILEVIEWINFO, 0, LPARAMptvi
                    LVM_GETTILEVIEWINFO = LVM_FIRST + 163


                    def ListView_GetTileViewInfo(hwnd, ptvi):
                        return SNDMSGhwnd, LVM_GETTILEVIEWINFO, 0, LPARAMptvi
                    LVM_SETTILEINFO = LVM_FIRST + 164


                    def ListView_SetTileInfo(hwnd, pti):
                        return SNDMSGhwnd, LVM_SETTILEINFO, 0, LPARAMpti
                    LVM_GETTILEINFO = LVM_FIRST + 165


                    def ListView_GetTileInfo(hwnd, pti):
                        return SNDMSGhwnd, LVM_GETTILEINFO, 0, LPARAMpti
                    class LVINSERTMARK(ctypes.Structure):
                        pass


                    LVINSERTMARK._fields_ = [
                        ('cbSize', UINT),
                        ('dwFlags', DWORD),
                        ('iItem', INT),
                        ('dwReserved', DWORD),
                    ]
                     LPLVINSERTMARK = POINTER(LVINSERTMARK)
                    LVIM_AFTER = 0x00000001
                    LVM_SETINSERTMARK = LVM_FIRST + 166


                    def ListView_SetInsertMark(hwnd, lvim):
                        return BOOLSNDMSGhwnd, LVM_SETINSERTMARK, WPARAM 0, LPARAM lvim
                    LVM_GETINSERTMARK = LVM_FIRST + 167


                    def ListView_GetInsertMark(hwnd, lvim):
                        return BOOLSNDMSGhwnd, LVM_GETINSERTMARK, WPARAM 0, LPARAM lvim
                    LVM_INSERTMARKHITTEST = LVM_FIRST + 168


                    def ListView_InsertMarkHitTest(hwnd, point, lvim):
                        return INTSNDMSGhwnd, LVM_INSERTMARKHITTEST, WPARAMLPPOINTpoint, LPARAMLPLVINSERTMARKlvim
                    LVM_GETINSERTMARKRECT = LVM_FIRST + 169


                    def ListView_GetInsertMarkRect(hwnd, rc):
                        return INTSNDMSGhwnd, LVM_GETINSERTMARKRECT, WPARAM0, LPARAMLPRECTrc
                    LVM_SETINSERTMARKCOLOR = LVM_FIRST + 170


                    def ListView_SetInsertMarkColor(hwnd, color):
                        return COLORREFSNDMSGhwnd, LVM_SETINSERTMARKCOLOR, WPARAM0, LPARAMCOLORREFcolor
                    LVM_GETINSERTMARKCOLOR = LVM_FIRST + 171


                    def ListView_GetInsertMarkColor(hwnd):
                        return COLORREFSNDMSG(hwnd, LVM_GETINSERTMARKCOLOR, WPARAM0, LPARAM0)
                    class tagLVSETINFOTIP(ctypes.Structure):
                        pass


                    tagLVSETINFOTIP._fields_ = [
                        ('cbSize', UINT),
                        ('dwFlags', DWORD),
                        ('pszText', LPWSTR),
                        ('iItem', INT),
                        ('iSubItem', INT),
                    ]
                    LVSETINFOTIP = tagLVSETINFOTIP
                    PLVSETINFOTIP = POINTER(tagLVSETINFOTIP)
                    LVM_SETINFOTIP = LVM_FIRST + 173


                    def ListView_SetInfoTip(hwndLV, plvInfoTip):
                        return BOOLSNDMSGhwndLV, LVM_SETINFOTIP, WPARAM0, LPARAMplvInfoTip
                    LVM_GETSELECTEDCOLUMN = LVM_FIRST + 174


                    def ListView_GetSelectedColumn(hwnd):
                        return UINTSNDMSG(hwnd, LVM_GETSELECTEDCOLUMN, 0, 0)
                    LVM_ISGROUPVIEWENABLED = LVM_FIRST + 175


                    def ListView_IsGroupViewEnabled(hwnd):
                        return BOOLSNDMSG(hwnd, LVM_ISGROUPVIEWENABLED, 0, 0)
                    LVM_GETOUTLINECOLOR = LVM_FIRST + 176


                    def ListView_GetOutlineColor(hwnd):
                        return COLORREFSNDMSG(hwnd, LVM_GETOUTLINECOLOR, 0, 0)
                    LVM_SETOUTLINECOLOR = LVM_FIRST + 177


                    def ListView_SetOutlineColor(hwnd, color):
                        return COLORREFSNDMSGhwnd, LVM_SETOUTLINECOLOR, WPARAM0, LPARAMCOLORREFcolor
                    LVM_CANCELEDITLABEL = LVM_FIRST + 179


                    def ListView_CancelEditLabel(hwnd):
                        return VOIDSNDMSG(hwnd, LVM_CANCELEDITLABEL, WPARAM0, LPARAM0)

                    # These next to methods make it easy to identify an item
                    # that can be repositioned

                    # within listview. For example: Many developers use the
                    # lParam to store an identifier that is

                    # unique. Unfortunatly, in order to find this item, they
                    # have to iterate through all of the items

                    # in the listview. Listview will maintain a unique
                    # identifier. The upper bound is the size of a DWORD.
                    LVM_MAPINDEXTOID = LVM_FIRST + 180


                    def ListView_MapIndexToID(hwnd, index):
                        return UINTSNDMSG(hwnd, LVM_MAPINDEXTOID, WPARAMindex, LPARAM0)
                    LVM_MAPIDTOINDEX = LVM_FIRST + 181


                    def ListView_MapIDToIndex(hwnd, id):
                        return UINTSNDMSG(hwnd, LVM_MAPIDTOINDEX, WPARAMid, LPARAM0)
                    LVM_ISITEMVISIBLE = LVM_FIRST + 182


                    def ListView_IsItemVisible(hwnd, index):
                        return UINTSNDMSG(hwnd, LVM_ISITEMVISIBLE, WPARAMindex, LPARAM0)

                    if NTDDI_VERSION >= NTDDI_VISTA:


                        def ListView_SetGroupHeaderImageList(hwnd, himl):
                            return HIMAGELISTSNDMSGhwnd, LVM_SETIMAGELIST, WPARAMLVSIL_GROUPHEADER, LPARAMHIMAGELISThiml


                        def ListView_GetGroupHeaderImageList(hwnd):
                            return HIMAGELISTSNDMSG(hwnd, LVM_GETIMAGELIST, WPARAMLVSIL_GROUPHEADER, 0L)
                        LVM_GETEMPTYTEXT = LVM_FIRST + 204


                        def ListView_GetEmptyText(hwnd, pszText, cchText):
                            return BOOLSNDMSGhwnd, LVM_GETEMPTYTEXT, WPARAMcchText, LPARAMpszText
                        LVM_GETFOOTERRECT = LVM_FIRST + 205


                        def ListView_GetFooterRect(hwnd, prc):
                            return BOOLSNDMSGhwnd, LVM_GETFOOTERRECT, WPARAM0, LPARAMprc

                        # footer flags
                        LVFF_ITEMCOUNT = 0x00000001
                        class tagLVFOOTERINFO(ctypes.Structure):
                            pass


                        tagLVFOOTERINFO._fields_ = [
                            ('mask', UINT), # LVFF_*
                            ('pszText', LPWSTR),
                            ('cchTextMax', INT),
                            ('cItems', UINT),
                        ]
                        LVFOOTERINFO = tagLVFOOTERINFO
                        LPLVFOOTERINFO = POINTER(tagLVFOOTERINFO)
                        LVM_GETFOOTERINFO = LVM_FIRST + 206


                        def ListView_GetFooterInfo(hwnd, plvfi):
                            return BOOLSNDMSGhwnd, LVM_GETFOOTERINFO, WPARAM0, LPARAMplvfi
                        LVM_GETFOOTERITEMRECT = LVM_FIRST + 207


                        def ListView_GetFooterItemRect(hwnd, iItem, prc):
                            return BOOLSNDMSGhwnd, LVM_GETFOOTERITEMRECT, WPARAMiItem, LPARAMprc

                        # footer item flags
                        LVFIF_TEXT = 0x00000001
                        LVFIF_STATE = 0x00000002

                        # footer item state
                        LVFIS_FOCUSED = 0x0001
                        class tagLVFOOTERITEM(ctypes.Structure):
                            pass


                        tagLVFOOTERITEM._fields_ = [
                            ('mask', UINT), # LVFIF_*
                            ('iItem', INT),
                            ('pszText', LPWSTR),
                            ('cchTextMax', INT),
                            ('state', UINT), # LVFIS_*
                            ('stateMask', UINT), # LVFIS_*
                        ]
                        LVFOOTERITEM = tagLVFOOTERITEM
                        LPLVFOOTERITEM = POINTER(tagLVFOOTERITEM)
                        LVM_GETFOOTERITEM = LVM_FIRST + 208


                        def ListView_GetFooterItem(hwnd, iItem, pfi):
                            return BOOLSNDMSGhwnd, LVM_GETFOOTERITEM, WPARAMiItem, LPARAMpfi

                        # supports a single item in multiple groups.
                        class tagLVITEMINDEX(ctypes.Structure):
                            pass


                        tagLVITEMINDEX._fields_ = [
                            ('iItem', INT), # listview item index

                            # group index
                            # (must be - 1 if group view is not enabled)
                            ('iGroup', INT),
                        ]
                        LVITEMINDEX = tagLVITEMINDEX
                        PLVITEMINDEX = POINTER(tagLVITEMINDEX)
                        LVM_GETITEMINDEXRECT = LVM_FIRST + 209


                        def ListView_GetItemIndexRect(hwnd, plvii, iSubItem, code, prc):
                            return BOOLSNDMSG(hwnd, LVM_GETITEMINDEXRECT, WPARAMLVITEMINDEX*plvii, (prc ? (((LPRECTprc) - >top = iSubItem), ((LPRECTprc) - >left = code), LPARAMprc) : LPARAMLPRECTNULL))
                        LVM_SETITEMINDEXSTATE = LVM_FIRST + 210


                        def ListView_SetItemIndexState(hwndLV, plvii, data, mask):
                            return { LV_ITEM _macro_lvi; _macro_lvi.stateMask = mask; _macro_lvi.state = data; SNDMSG(hwndLV, LVM_SETITEMINDEXSTATE, WPARAMLVITEMINDEX*plvii, LPARAMLV_ITEM * & _macro_lvi); }
                        LVM_GETNEXTITEMINDEX = LVM_FIRST + 211


                        def ListView_GetNextItemIndex(hwnd, plvii, flags):
                            return BOOLSNDMSGhwnd, LVM_GETNEXTITEMINDEX, WPARAMLVITEMINDEX*plvii, MAKELPARAM(flags, 0)
                    # END IF
                # END IF

                if defined(UNICODE):
                    LVBKIMAGE = LVBKIMAGEW
                    LPLVBKIMAGE = LPLVBKIMAGEW
                    LVM_SETBKIMAGE = LVM_SETBKIMAGEW
                    LVM_GETBKIMAGE = LVM_GETBKIMAGEW
                else:
                    LVBKIMAGE = LVBKIMAGEA
                    LPLVBKIMAGE = LPLVBKIMAGEA
                    LVM_SETBKIMAGE = LVM_SETBKIMAGEA
                    LVM_GETBKIMAGE = LVM_GETBKIMAGEA
                # END IF


                def ListView_SetBkImage(hwnd, plvbki):
                    return BOOLSNDMSGhwnd, LVM_SETBKIMAGE, 0, LPARAMplvbki


                def ListView_GetBkImage(hwnd, plvbki):
                    return BOOLSNDMSGhwnd, LVM_GETBKIMAGE, 0, LPARAMplvbki
                LPNM_LISTVIEW = LPNMLISTVIEW
                NM_LISTVIEW = NMLISTVIEW
                class tagNMLISTVIEW(ctypes.Structure):
                    pass


                tagNMLISTVIEW._fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('uNewState', UINT),
                    ('uOldState', UINT),
                    ('uChanged', UINT),
                    ('ptAction', POINT),
                    ('lParam', LPARAM),
                ]
                NMLISTVIEW = tagNMLISTVIEW
                LPNMLISTVIEW = POINTER(tagNMLISTVIEW)

                # NMITEMACTIVATE is used instead of NMLISTVIEW in IE >= 0x400

                # therefore all the fields are the same except for extra
                # uKeyFlags

                # they are used to store key flags at the time of the single
                # click with

                # delayed activation - because by the time the timer goes off
                # a user may

                # not hold the keys (shift, ctrl) any more
                class tagNMITEMACTIVATE(ctypes.Structure):
                    pass


                tagNMITEMACTIVATE._fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('uNewState', UINT),
                    ('uOldState', UINT),
                    ('uChanged', UINT),
                    ('ptAction', POINT),
                    ('lParam', LPARAM),
                    ('uKeyFlags', UINT),
                ]
                NMITEMACTIVATE = tagNMITEMACTIVATE
                LPNMITEMACTIVATE = POINTER(tagNMITEMACTIVATE)

                # key flags stored in uKeyFlags
                LVKF_ALT = 0x0001
                LVKF_CONTROL = 0x0002
                LVKF_SHIFT = 0x0004
                NMLVCUSTOMDRAW_V3_SIZE = CCSIZEOF_STRUCT(
                    NMLVCUSTOMDRAW,
                    clrTextBk,
                )
                class tagNMLVCUSTOMDRAW(ctypes.Structure):
                    pass


                tagNMLVCUSTOMDRAW._fields_ = [
                    ('nmcd', NMCUSTOMDRAW),
                    ('clrText', COLORREF),
                    ('clrTextBk', COLORREF),
                    ('iSubItem', INT),
                        ('dwItemType', DWORD),
                        ('clrFace', COLORREF), # Item custom draw
                        ('iIconEffect', INT),
                        ('iIconPhase', INT),
                        ('iPartId', INT),
                        ('iStateId', INT),
                        ('rcText', RECT), # Group Custom Draw

                        # Alignment. Use LVGA_HEADER_CENTER,
                        # LVGA_HEADER_RIGHT, LVGA_HEADER_LEFT
                        ('uAlign', UINT),
                ]
                NMLVCUSTOMDRAW = tagNMLVCUSTOMDRAW
                LPNMLVCUSTOMDRAW = POINTER(tagNMLVCUSTOMDRAW)

                if NTDDI_VERSION >= NTDDI_WINXP:
                    pass
                # END IF

                # dwItemType
                LVCDI_ITEM = 0x00000000
                LVCDI_GROUP = 0x00000001
                LVCDI_ITEMSLIST = 0x00000002

                # ListView custom draw return values
                LVCDRF_NOSELECT = 0x00010000
                LVCDRF_NOGROUPFRAME = 0x00020000
                class tagNMLVCACHEHINT(ctypes.Structure):
                    pass


                tagNMLVCACHEHINT._fields_ = [
                    ('hdr', NMHDR),
                    ('iFrom', INT),
                    ('iTo', INT),
                ]
                NMLVCACHEHINT = tagNMLVCACHEHINT
                LPNMLVCACHEHINT = POINTER(tagNMLVCACHEHINT)
                LPNM_CACHEHINT = LPNMLVCACHEHINT
                PNM_CACHEHINT = LPNMLVCACHEHINT
                NM_CACHEHINT = NMLVCACHEHINT
                class tagNMLVFINDITEMA(ctypes.Structure):
                    pass


                tagNMLVFINDITEMA._fields_ = [
                    ('hdr', NMHDR),
                    ('iStart', INT),
                    ('lvfi', LVFINDINFOA),
                ]
                NMLVFINDITEMA = tagNMLVFINDITEMA
                LPNMLVFINDITEMA = POINTER(tagNMLVFINDITEMA)
                class tagNMLVFINDITEMW(ctypes.Structure):
                    pass


                tagNMLVFINDITEMW._fields_ = [
                    ('hdr', NMHDR),
                    ('iStart', INT),
                    ('lvfi', LVFINDINFOW),
                ]
                NMLVFINDITEMW = tagNMLVFINDITEMW
                LPNMLVFINDITEMW = POINTER(tagNMLVFINDITEMW)
                PNM_FINDITEMA = LPNMLVFINDITEMA
                LPNM_FINDITEMA = LPNMLVFINDITEMA
                NM_FINDITEMA = NMLVFINDITEMA
                PNM_FINDITEMW = LPNMLVFINDITEMW
                LPNM_FINDITEMW = LPNMLVFINDITEMW
                NM_FINDITEMW = NMLVFINDITEMW

                if defined(UNICODE):
                    PNM_FINDITEM = PNM_FINDITEMW
                    LPNM_FINDITEM = LPNM_FINDITEMW
                    NM_FINDITEM = NM_FINDITEMW
                    NMLVFINDITEM = NMLVFINDITEMW
                    LPNMLVFINDITEM = LPNMLVFINDITEMW
                else:
                    PNM_FINDITEM = PNM_FINDITEMA
                    LPNM_FINDITEM = LPNM_FINDITEMA
                    NM_FINDITEM = NM_FINDITEMA
                    NMLVFINDITEM = NMLVFINDITEMA
                    LPNMLVFINDITEM = LPNMLVFINDITEMA
                # END IF
                class tagNMLVODSTATECHANGE(ctypes.Structure):
                    pass


                tagNMLVODSTATECHANGE._fields_ = [
                    ('hdr', NMHDR),
                    ('iFrom', INT),
                    ('iTo', INT),
                    ('uNewState', UINT),
                    ('uOldState', UINT),
                ]
                NMLVODSTATECHANGE = tagNMLVODSTATECHANGE
                LPNMLVODSTATECHANGE = POINTER(tagNMLVODSTATECHANGE)
                PNM_ODSTATECHANGE = LPNMLVODSTATECHANGE
                LPNM_ODSTATECHANGE = LPNMLVODSTATECHANGE
                NM_ODSTATECHANGE = NMLVODSTATECHANGE
                LVN_ITEMCHANGING = LVN_FIRST - 0
                LVN_ITEMCHANGED = LVN_FIRST - 1
                LVN_INSERTITEM = LVN_FIRST - 2
                LVN_DELETEITEM = LVN_FIRST - 3
                LVN_DELETEALLITEMS = LVN_FIRST - 4
                LVN_BEGINLABELEDITA = LVN_FIRST - 5
                LVN_BEGINLABELEDITW = LVN_FIRST - 75
                LVN_ENDLABELEDITA = LVN_FIRST - 6
                LVN_ENDLABELEDITW = LVN_FIRST - 76
                LVN_COLUMNCLICK = LVN_FIRST - 8
                LVN_BEGINDRAG = LVN_FIRST - 9
                LVN_BEGINRDRAG = LVN_FIRST - 11
                LVN_ODCACHEHINT = LVN_FIRST - 13
                LVN_ODFINDITEMA = LVN_FIRST - 52
                LVN_ODFINDITEMW = LVN_FIRST - 79
                LVN_ITEMACTIVATE = LVN_FIRST - 14
                LVN_ODSTATECHANGED = LVN_FIRST - 15

                if defined(UNICODE):
                    LVN_ODFINDITEM = LVN_ODFINDITEMW
                else:
                    LVN_ODFINDITEM = LVN_ODFINDITEMA
                # END IF
                LVN_HOTTRACK = LVN_FIRST - 21
                LVN_GETDISPINFOA = LVN_FIRST - 50
                LVN_GETDISPINFOW = LVN_FIRST - 77
                LVN_SETDISPINFOA = LVN_FIRST - 51
                LVN_SETDISPINFOW = LVN_FIRST - 78

                if defined(UNICODE):
                    LVN_BEGINLABELEDIT = LVN_BEGINLABELEDITW
                    LVN_ENDLABELEDIT = LVN_ENDLABELEDITW
                    LVN_GETDISPINFO = LVN_GETDISPINFOW
                    LVN_SETDISPINFO = LVN_SETDISPINFOW
                else:
                    LVN_BEGINLABELEDIT = LVN_BEGINLABELEDITA
                    LVN_ENDLABELEDIT = LVN_ENDLABELEDITA
                    LVN_GETDISPINFO = LVN_GETDISPINFOA
                    LVN_SETDISPINFO = LVN_SETDISPINFOA
                # END IF
                LVIF_DI_SETITEM = 0x1000
                LV_DISPINFOA = NMLVDISPINFOA
                LV_DISPINFOW = NMLVDISPINFOW
                LV_DISPINFO = NMLVDISPINFO
                class tagLVDISPINFO(ctypes.Structure):
                    pass


                tagLVDISPINFO._fields_ = [
                    ('hdr', NMHDR),
                    ('item', LVITEMA),
                ]
                NMLVDISPINFOA = tagLVDISPINFO
                LPNMLVDISPINFOA = POINTER(tagLVDISPINFO)
                class tagLVDISPINFOW(ctypes.Structure):
                    pass


                tagLVDISPINFOW._fields_ = [
                    ('hdr', NMHDR),
                    ('item', LVITEMW),
                ]
                NMLVDISPINFOW = tagLVDISPINFOW
                LPNMLVDISPINFOW = POINTER(tagLVDISPINFOW)

                if defined(UNICODE):
                    NMLVDISPINFO = NMLVDISPINFOW
                else:
                    NMLVDISPINFO = NMLVDISPINFOA
                # END IF
                LVN_KEYDOWN = LVN_FIRST - 55
                LV_KEYDOWN = NMLVKEYDOWN

                if defined(_WIN32):
                    pass
                # END IF
                class tagLVKEYDOWN(ctypes.Structure):
                    pass


                tagLVKEYDOWN._fields_ = [
                    ('hdr', NMHDR),
                    ('wVKey', WORD),
                    ('flags', UINT),
                ]
                NMLVKEYDOWN = tagLVKEYDOWN
                LPNMLVKEYDOWN = POINTER(tagLVKEYDOWN)
                if defined(_WIN32):
                    pass
                # END IF
                LVN_MARQUEEBEGIN = LVN_FIRST - 56

                if NTDDI_VERSION >= NTDDI_VISTA:
                    class tagNMLVLINK(ctypes.Structure):
                        pass


                    tagNMLVLINK._fields_ = [
                        ('hdr', NMHDR),
                        ('link', LITEM),
                        ('iItem', INT),
                        ('iSubItem', INT),
                    ]
                    NMLVLINK = tagNMLVLINK
                    PNMLVLINK = POINTER(tagNMLVLINK)
                # END IF
                class tagNMLVGETINFOTIPA(ctypes.Structure):
                    pass


                tagNMLVGETINFOTIPA._fields_ = [
                    ('hdr', NMHDR),
                    ('dwFlags', DWORD),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('lParam', LPARAM),
                ]
                NMLVGETINFOTIPA = tagNMLVGETINFOTIPA
                LPNMLVGETINFOTIPA = POINTER(tagNMLVGETINFOTIPA)
                class tagNMLVGETINFOTIPW(ctypes.Structure):
                    pass


                tagNMLVGETINFOTIPW._fields_ = [
                    ('hdr', NMHDR),
                    ('dwFlags', DWORD),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('lParam', LPARAM),
                ]
                NMLVGETINFOTIPW = tagNMLVGETINFOTIPW
                LPNMLVGETINFOTIPW = POINTER(tagNMLVGETINFOTIPW)

                # NMLVGETINFOTIPA.dwFlag values
                LVGIT_UNFOLDED = 0x0001
                LVN_GETINFOTIPA = LVN_FIRST - 57
                LVN_GETINFOTIPW = LVN_FIRST - 58

                if defined(UNICODE):
                    LVN_GETINFOTIP = LVN_GETINFOTIPW
                    NMLVGETINFOTIP = NMLVGETINFOTIPW
                    LPNMLVGETINFOTIP = LPNMLVGETINFOTIPW
                else:
                    LVN_GETINFOTIP = LVN_GETINFOTIPA
                    NMLVGETINFOTIP = NMLVGETINFOTIPA
                    LPNMLVGETINFOTIP = LPNMLVGETINFOTIPA
                # END IF

                # LVN_INCREMENTALSEARCH gives the app the opportunity to
                # customize

                # incremental search. For example, if the items are numeric,

                # the app can do numerical search instead of string search.

                # ListView notifies the app with NMLVFINDITEM.

                # The app sets pnmfi - >lvfi.lParam to the result of the
                # incremental search,

                # or to LVNSCH_DEFAULT if ListView should do the default
                # search,

                # or to LVNSCH_ERROR to fail the search and just beep,

                # or to LVNSCH_IGNORE to stop all ListView processing.

                # The return value is not used.
                LVNSCH_DEFAULT = - 1
                LVNSCH_ERROR = - 2
                LVNSCH_IGNORE = - 3
                LVN_INCREMENTALSEARCHA = LVN_FIRST - 62
                LVN_INCREMENTALSEARCHW = LVN_FIRST - 63

                if defined(UNICODE):
                    LVN_INCREMENTALSEARCH = LVN_INCREMENTALSEARCHW
                else:
                    LVN_INCREMENTALSEARCH = LVN_INCREMENTALSEARCHA
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    LVN_COLUMNDROPDOWN = LVN_FIRST - 64
                    LVN_COLUMNOVERFLOWCLICK = LVN_FIRST - 66
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                if NTDDI_VERSION >= NTDDI_WINXP:
                    class tagNMLVSCROLL(ctypes.Structure):
                        pass


                    tagNMLVSCROLL._fields_ = [
                        ('hdr', NMHDR),
                        ('dx', INT),
                        ('dy', INT),
                    ]
                    NMLVSCROLL = tagNMLVSCROLL
                    LPNMLVSCROLL = POINTER(tagNMLVSCROLL)
                    LVN_BEGINSCROLL = LVN_FIRST - 80
                    LVN_ENDSCROLL = LVN_FIRST - 81
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    LVN_LINKCLICK = LVN_FIRST - 84
                    EMF_CENTERED = 0x00000001
                    class tagNMLVEMPTYMARKUP(ctypes.Structure):
                        pass


                    tagNMLVEMPTYMARKUP._fields_ = [
                        ('hdr', NMHDR),
                        ('dwFlags', DWORD), # EMF_*
                        ('szMarkup', WCHAR * L_MAX_URL_LENGTH), # markup displayed
                    ]
                    NMLVEMPTYMARKUP = tagNMLVEMPTYMARKUP
                    LVN_GETEMPTYMARKUP = LVN_FIRST - 87
                # END IF
            # END IF   NOLISTVIEW

            # == == == TREEVIEW CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == =

            if not defined(NOTREEVIEW):
                if defined(_WIN32):
                    WC_TREEVIEWA = "SysTreeView32"
                    WC_TREEVIEWW = "SysTreeView32"

                    if defined(UNICODE):
                        WC_TREEVIEW = WC_TREEVIEWW
                    else:
                        WC_TREEVIEW = WC_TREEVIEWA
                    # END IF
                else:
                    WC_TREEVIEW = "SysTreeView"
                # END IF

                # begin_r_commctrl
                TVS_HASBUTTONS = 0x0001
                TVS_HASLINES = 0x0002
                TVS_LINESATROOT = 0x0004
                TVS_EDITLABELS = 0x0008
                TVS_DISABLEDRAGDROP = 0x0010
                TVS_SHOWSELALWAYS = 0x0020
                TVS_RTLREADING = 0x0040
                TVS_NOTOOLTIPS = 0x0080
                TVS_CHECKBOXES = 0x0100
                TVS_TRACKSELECT = 0x0200
                TVS_SINGLEEXPAND = 0x0400
                TVS_INFOTIP = 0x0800
                TVS_FULLROWSELECT = 0x1000
                TVS_NOSCROLL = 0x2000
                TVS_NONEVENHEIGHT = 0x4000
                TVS_NOHSCROLL = 0x8000

                if NTDDI_VERSION >= NTDDI_WINXP:
                    TVS_EX_NOSINGLECOLLAPSE = 0x0001
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    TVS_EX_MULTISELECT = 0x0002
                    TVS_EX_DOUBLEBUFFER = 0x0004
                    TVS_EX_NOINDENTSTATE = 0x0008
                    TVS_EX_RICHTOOLTIP = 0x0010
                    TVS_EX_AUTOHSCROLL = 0x0020
                    TVS_EX_FADEINOUTEXPANDOS = 0x0040
                    TVS_EX_PARTIALCHECKBOXES = 0x0080
                    TVS_EX_EXCLUSIONCHECKBOXES = 0x0100
                    TVS_EX_DIMMEDCHECKBOXES = 0x0200
                    TVS_EX_DRAWIMAGEASYNC = 0x0400
                # END IF

                if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
                    pass
                # END IF

                # end_r_commctrl
                _TREEITEM = struct

                HTREEITEM = POINTER(_TREEITEM)

                TVIF_TEXT = 0x0001
                TVIF_IMAGE = 0x0002
                TVIF_PARAM = 0x0004
                TVIF_STATE = 0x0008
                TVIF_HANDLE = 0x0010
                TVIF_SELECTEDIMAGE = 0x0020
                TVIF_CHILDREN = 0x0040
                TVIF_INTEGRAL = 0x0080

                if _WIN32_IE >= 0x0600:
                    TVIF_STATEEX = 0x0100
                    TVIF_EXPANDEDIMAGE = 0x0200
                # END IF
                TVIS_SELECTED = 0x0002
                TVIS_CUT = 0x0004
                TVIS_DROPHILITED = 0x0008
                TVIS_BOLD = 0x0010
                TVIS_EXPANDED = 0x0020
                TVIS_EXPANDEDONCE = 0x0040
                TVIS_EXPANDPARTIAL = 0x0080
                TVIS_OVERLAYMASK = 0x0F00
                TVIS_STATEIMAGEMASK = 0xF000
                TVIS_USERMASK = 0xF000

                if _WIN32_IE >= 0x0600:
                    TVIS_EX_FLAT = 0x0001

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        TVIS_EX_DISABLED = 0x0002
                    # END IF
                    TVIS_EX_ALL = 0x0002

                    # Structure for TreeView's NM_TVSTATEIMAGECHANGING
                    # notification
                    class tagNMTVSTATEIMAGECHANGING(ctypes.Structure):
                        pass


                    tagNMTVSTATEIMAGECHANGING._fields_ = [
                        ('hdr', NMHDR),
                        ('hti', HTREEITEM),
                        ('iOldStateImageIndex', INT),
                        ('iNewStateImageIndex', INT),
                    ]
                    NMTVSTATEIMAGECHANGING = tagNMTVSTATEIMAGECHANGING
                    LPNMTVSTATEIMAGECHANGING = POINTER(tagNMTVSTATEIMAGECHANGING)
                # END IF
                I_CHILDRENCALLBACK = - 1
                I_CHILDRENAUTO = - 2
                LPTV_ITEMW = LPTVITEMW
                LPTV_ITEMA = LPTVITEMA
                TV_ITEMW = TVITEMW
                TV_ITEMA = TVITEMA
                LPTV_ITEM = LPTVITEM
                TV_ITEM = TVITEM
                class tagTVITEMA(ctypes.Structure):
                    pass


                tagTVITEMA._fields_ = [
                    ('mask', UINT),
                    ('hItem', HTREEITEM),
                    ('state', UINT),
                    ('stateMask', UINT),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('iSelectedImage', INT),
                    ('cChildren', INT),
                    ('lParam', LPARAM),
                ]
                TVITEMA = tagTVITEMA
                LPTVITEMA = POINTER(tagTVITEMA)
                class tagTVITEMW(ctypes.Structure):
                    pass


                tagTVITEMW._fields_ = [
                    ('mask', UINT),
                    ('hItem', HTREEITEM),
                    ('state', UINT),
                    ('stateMask', UINT),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('iSelectedImage', INT),
                    ('cChildren', INT),
                    ('lParam', LPARAM),
                ]
                TVITEMW = tagTVITEMW
                LPTVITEMW = POINTER(tagTVITEMW)

                # only used for Get and Set messages. no notifies
                class tagTVITEMEXA(ctypes.Structure):
                    pass


                tagTVITEMEXA._fields_ = [
                    ('mask', UINT),
                    ('hItem', HTREEITEM),
                    ('state', UINT),
                    ('stateMask', UINT),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('iSelectedImage', INT),
                    ('cChildren', INT),
                    ('lParam', LPARAM),
                    ('iIntegral', INT),
                        ('uStateEx', UINT),
                        ('hwnd', HWND),
                        ('iExpandedImage', INT),
                        ('iReserved', INT),
                ]
                TVITEMEXA = tagTVITEMEXA
                LPTVITEMEXA = POINTER(tagTVITEMEXA)

                if _WIN32_IE >= 0x0600:
                    pass
                # END IF
                if NTDDI_VERSION >= NTDDI_WIN7:
                    pass
                # END IF

                # only used for Get and Set messages. no notifies
                class tagTVITEMEXW(ctypes.Structure):
                    pass


                tagTVITEMEXW._fields_ = [
                    ('mask', UINT),
                    ('hItem', HTREEITEM),
                    ('state', UINT),
                    ('stateMask', UINT),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('iSelectedImage', INT),
                    ('cChildren', INT),
                    ('lParam', LPARAM),
                    ('iIntegral', INT),
                        ('uStateEx', UINT),
                        ('hwnd', HWND),
                        ('iExpandedImage', INT),
                        ('iReserved', INT),
                ]
                TVITEMEXW = tagTVITEMEXW
                LPTVITEMEXW = POINTER(tagTVITEMEXW)
                if _WIN32_IE >= 0x0600:
                    pass
                # END IF
                if NTDDI_VERSION >= NTDDI_WIN7:
                    pass
                # END IF
                if defined(UNICODE):
                    TVITEMEX = TVITEMEXW
                    LPTVITEMEX = LPTVITEMEXW
                else:
                    TVITEMEX = TVITEMEXA
                    LPTVITEMEX = LPTVITEMEXA
                # END IF   UNICODE
                if defined(UNICODE):
                    TVITEM = TVITEMW
                    LPTVITEM = LPTVITEMW
                else:
                    TVITEM = TVITEMA
                    LPTVITEM = LPTVITEMA
                # END IF
                TVI_ROOT = (HTREEITEM)(ULONG_PTR) - 0x10000
                TVI_FIRST = (HTREEITEM)(ULONG_PTR) - 0x0FFFF
                TVI_LAST = (HTREEITEM)(ULONG_PTR) - 0x0FFFE
                TVI_SORT = (HTREEITEM)(ULONG_PTR) - 0x0FFFD
                LPTV_INSERTSTRUCTA = LPTVINSERTSTRUCTA
                LPTV_INSERTSTRUCTW = LPTVINSERTSTRUCTW
                TV_INSERTSTRUCTA = TVINSERTSTRUCTA
                TV_INSERTSTRUCTW = TVINSERTSTRUCTW
                TV_INSERTSTRUCT = TVINSERTSTRUCT
                LPTV_INSERTSTRUCT = LPTVINSERTSTRUCT
                TVINSERTSTRUCTA_V1_SIZE = CCSIZEOF_STRUCT(
                    TVINSERTSTRUCTA,
                    item,
                )
                TVINSERTSTRUCTW_V1_SIZE = CCSIZEOF_STRUCT(
                    TVINSERTSTRUCTW,
                    item,
                )
                class tagTVINSERTSTRUCTA(ctypes.Structure):
                    pass


                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                DUMMYUNIONNAME._fields_ = [
                    ('itemex', TVITEMEXA),
                    ('item', TV_ITEMA),
                ]
                tagTVINSERTSTRUCTA.DUMMYUNIONNAME = DUMMYUNIONNAME
                tagTVINSERTSTRUCTA._fields_ = [
                    ('hParent', HTREEITEM),
                    ('hInsertAfter', HTREEITEM),
                    ('DUMMYUNIONNAME', tagTVINSERTSTRUCTA.DUMMYUNIONNAME),
                ]
                TVINSERTSTRUCTA = tagTVINSERTSTRUCTA
                LPTVINSERTSTRUCTA = POINTER(tagTVINSERTSTRUCTA)
                DUMMYUNIONNAME._fields_ = [
                    ('itemex', TVITEMEXA),
                    ('item', TV_ITEMA),
                ]
                class tagTVINSERTSTRUCTW(ctypes.Structure):
                    pass


                DUMMYUNIONNAME._fields_ = [
                    ('itemex', TVITEMEXW),
                    ('item', TV_ITEMW),
                ]
                tagTVINSERTSTRUCTW.DUMMYUNIONNAME = DUMMYUNIONNAME
                tagTVINSERTSTRUCTW._fields_ = [
                    ('hParent', HTREEITEM),
                    ('hInsertAfter', HTREEITEM),
                    ('DUMMYUNIONNAME', tagTVINSERTSTRUCTW.DUMMYUNIONNAME),
                ]
                TVINSERTSTRUCTW = tagTVINSERTSTRUCTW
                LPTVINSERTSTRUCTW = POINTER(tagTVINSERTSTRUCTW)
                DUMMYUNIONNAME._fields_ = [
                    ('itemex', TVITEMEXW),
                    ('item', TV_ITEMW),
                ]

                if defined(UNICODE):
                    TVINSERTSTRUCT = TVINSERTSTRUCTW
                    LPTVINSERTSTRUCT = LPTVINSERTSTRUCTW
                    TVINSERTSTRUCT_V1_SIZE = TVINSERTSTRUCTW_V1_SIZE
                else:
                    TVINSERTSTRUCT = TVINSERTSTRUCTA
                    LPTVINSERTSTRUCT = LPTVINSERTSTRUCTA
                    TVINSERTSTRUCT_V1_SIZE = TVINSERTSTRUCTA_V1_SIZE
                # END IF
                TVM_INSERTITEMA = TV_FIRST + 0
                TVM_INSERTITEMW = TV_FIRST + 50

                if defined(UNICODE):
                    TVM_INSERTITEM = TVM_INSERTITEMW
                else:
                    TVM_INSERTITEM = TVM_INSERTITEMA
                # END IF


                def TreeView_InsertItem(hwnd, lpis):
                    return HTREEITEMSNDMSGhwnd, TVM_INSERTITEM, 0, LPARAMLPTV_INSERTSTRUCTlpis
                TVM_DELETEITEM = TV_FIRST + 1


                def TreeView_DeleteItem(hwnd, hitem):
                    return BOOLSNDMSGhwnd, TVM_DELETEITEM, 0, LPARAMHTREEITEMhitem


                def TreeView_DeleteAllItems(hwnd):
                    return BOOLSNDMSG(hwnd, TVM_DELETEITEM, 0, LPARAMTVI_ROOT)
                TVM_EXPAND = TV_FIRST + 2


                def TreeView_Expand(hwnd, hitem, code):
                    return BOOLSNDMSGhwnd, TVM_EXPAND, WPARAMcode, LPARAMHTREEITEMhitem
                TVE_COLLAPSE = 0x0001
                TVE_EXPAND = 0x0002
                TVE_TOGGLE = 0x0003
                TVE_EXPANDPARTIAL = 0x4000
                TVE_COLLAPSERESET = 0x8000
                TVM_GETITEMRECT = TV_FIRST + 4


                def TreeView_GetItemRect(hwnd, hitem, prc, code):
                    return (*HTREEITEM *prc = hitem, BOOLSNDMSGhwnd, TVM_GETITEMRECT, WPARAMcode, LPARAMRECT *prc)
                TVM_GETCOUNT = TV_FIRST + 5


                def TreeView_GetCount(hwnd):
                    return UINTSNDMSG(hwnd, TVM_GETCOUNT, 0, 0)
                TVM_GETINDENT = TV_FIRST + 6


                def TreeView_GetIndent(hwnd):
                    return UINTSNDMSG(hwnd, TVM_GETINDENT, 0, 0)
                TVM_SETINDENT = TV_FIRST + 7


                def TreeView_SetIndent(hwnd, indent):
                    return BOOLSNDMSG(hwnd, TVM_SETINDENT, WPARAMindent, 0)
                TVM_GETIMAGELIST = TV_FIRST + 8


                def TreeView_GetImageList(hwnd, iImage):
                    return HIMAGELISTSNDMSG(hwnd, TVM_GETIMAGELIST, iImage, 0)
                TVSIL_NORMAL = 0
                TVSIL_STATE = 2
                TVM_SETIMAGELIST = TV_FIRST + 9


                def TreeView_SetImageList(hwnd, himl, iImage):
                    return HIMAGELISTSNDMSGhwnd, TVM_SETIMAGELIST, iImage, LPARAMHIMAGELISThiml
                TVM_GETNEXTITEM = TV_FIRST + 10


                def TreeView_GetNextItem(hwnd, hitem, code):
                    return HTREEITEMSNDMSGhwnd, TVM_GETNEXTITEM, WPARAMcode, LPARAMHTREEITEMhitem
                TVGN_ROOT = 0x0000
                TVGN_NEXT = 0x0001
                TVGN_PREVIOUS = 0x0002
                TVGN_PARENT = 0x0003
                TVGN_CHILD = 0x0004
                TVGN_FIRSTVISIBLE = 0x0005
                TVGN_NEXTVISIBLE = 0x0006
                TVGN_PREVIOUSVISIBLE = 0x0007
                TVGN_DROPHILITE = 0x0008
                TVGN_CARET = 0x0009
                TVGN_LASTVISIBLE = 0x000A

                if _WIN32_IE >= 0x0600:
                    TVGN_NEXTSELECTED = 0x000B
                # END IF

                if NTDDI_VERSION >= NTDDI_WINXP:
                    TVSI_NOSINGLEEXPAND = 0x8000
                # END IF


                def TreeView_GetChild(hwnd, hitem):
                    return TreeView_GetNextItemhwnd, hitem, TVGN_CHILD


                def TreeView_GetNextSibling(hwnd, hitem):
                    return TreeView_GetNextItemhwnd, hitem, TVGN_NEXT


                def TreeView_GetPrevSibling(hwnd, hitem):
                    return TreeView_GetNextItemhwnd, hitem, TVGN_PREVIOUS


                def TreeView_GetParent(hwnd, hitem):
                    return TreeView_GetNextItemhwnd, hitem, TVGN_PARENT


                def TreeView_GetFirstVisible(hwnd):
                    return TreeView_GetNextItemhwnd, NULL, TVGN_FIRSTVISIBLE


                def TreeView_GetNextVisible(hwnd, hitem):
                    return TreeView_GetNextItemhwnd, hitem, TVGN_NEXTVISIBLE


                def TreeView_GetPrevVisible(hwnd, hitem):
                    return TreeView_GetNextItemhwnd, hitem, TVGN_PREVIOUSVISIBLE


                def TreeView_GetSelection(hwnd):
                    return TreeView_GetNextItemhwnd, NULL, TVGN_CARET


                def TreeView_GetDropHilight(hwnd):
                    return TreeView_GetNextItemhwnd, NULL, TVGN_DROPHILITE


                def TreeView_GetRoot(hwnd):
                    return TreeView_GetNextItemhwnd, NULL, TVGN_ROOT


                def TreeView_GetLastVisible(hwnd):
                    return TreeView_GetNextItemhwnd, NULL, TVGN_LASTVISIBLE

                if _WIN32_IE >= 0x0600:


                    def TreeView_GetNextSelected(hwnd, hitem):
                        return TreeView_GetNextItemhwnd, hitem, TVGN_NEXTSELECTED
                # END IF
                TVM_SELECTITEM = TV_FIRST + 11


                def TreeView_Select(hwnd, hitem, code):
                    return BOOLSNDMSGhwnd, TVM_SELECTITEM, WPARAMcode, LPARAMHTREEITEMhitem


                def TreeView_SelectItem(hwnd, hitem):
                    return TreeView_Selecthwnd, hitem, TVGN_CARET


                def TreeView_SelectDropTarget(hwnd, hitem):
                    return TreeView_Selecthwnd, hitem, TVGN_DROPHILITE


                def TreeView_SelectSetFirstVisible(hwnd, hitem):
                    return TreeView_Selecthwnd, hitem, TVGN_FIRSTVISIBLE
                TVM_GETITEMA = TV_FIRST + 12
                TVM_GETITEMW = TV_FIRST + 62

                if defined(UNICODE):
                    TVM_GETITEM = TVM_GETITEMW
                else:
                    TVM_GETITEM = TVM_GETITEMA
                # END IF


                def TreeView_GetItem(hwnd, pitem):
                    return BOOLSNDMSGhwnd, TVM_GETITEM, 0, LPARAMTV_ITEM *pitem
                TVM_SETITEMA = TV_FIRST + 13
                TVM_SETITEMW = TV_FIRST + 63

                if defined(UNICODE):
                    TVM_SETITEM = TVM_SETITEMW
                else:
                    TVM_SETITEM = TVM_SETITEMA
                # END IF


                def TreeView_SetItem(hwnd, pitem):
                    return BOOLSNDMSGhwnd, TVM_SETITEM, 0, LPARAMTV_ITEM *pitem
                TVM_EDITLABELA = TV_FIRST + 14
                TVM_EDITLABELW = TV_FIRST + 65

                if defined(UNICODE):
                    TVM_EDITLABEL = TVM_EDITLABELW
                else:
                    TVM_EDITLABEL = TVM_EDITLABELA
                # END IF


                def TreeView_EditLabel(hwnd, hitem):
                    return HWNDSNDMSGhwnd, TVM_EDITLABEL, 0, LPARAMHTREEITEMhitem
                TVM_GETEDITCONTROL = TV_FIRST + 15


                def TreeView_GetEditControl(hwnd):
                    return HWNDSNDMSG(hwnd, TVM_GETEDITCONTROL, 0, 0)
                TVM_GETVISIBLECOUNT = TV_FIRST + 16


                def TreeView_GetVisibleCount(hwnd):
                    return UINTSNDMSG(hwnd, TVM_GETVISIBLECOUNT, 0, 0)
                TVM_HITTEST = TV_FIRST + 17


                def TreeView_HitTest(hwnd, lpht):
                    return HTREEITEMSNDMSGhwnd, TVM_HITTEST, 0, LPARAMLPTV_HITTESTINFOlpht
                LPTV_HITTESTINFO = LPTVHITTESTINFO
                TV_HITTESTINFO = TVHITTESTINFO
                class tagTVHITTESTINFO(ctypes.Structure):
                    pass


                tagTVHITTESTINFO._fields_ = [
                    ('pt', POINT),
                    ('flags', UINT),
                    ('hItem', HTREEITEM),
                ]
                TVHITTESTINFO = tagTVHITTESTINFO
                LPTVHITTESTINFO = POINTER(tagTVHITTESTINFO)
                TVHT_NOWHERE = 0x0001
                TVHT_ONITEMICON = 0x0002
                TVHT_ONITEMLABEL = 0x0004
                TVHT_ONITEM = (
                    TVHT_ONITEMICON |
                    TVHT_ONITEMLABEL |
                    TVHT_ONITEMSTATEICON
                )
                TVHT_ONITEMINDENT = 0x0008
                TVHT_ONITEMBUTTON = 0x0010
                TVHT_ONITEMRIGHT = 0x0020
                TVHT_ONITEMSTATEICON = 0x0040
                TVHT_ABOVE = 0x0100
                TVHT_BELOW = 0x0200
                TVHT_TORIGHT = 0x0400
                TVHT_TOLEFT = 0x0800
                TVM_CREATEDRAGIMAGE = TV_FIRST + 18


                def TreeView_CreateDragImage(hwnd, hitem):
                    return HIMAGELISTSNDMSGhwnd, TVM_CREATEDRAGIMAGE, 0, LPARAMHTREEITEMhitem
                TVM_SORTCHILDREN = TV_FIRST + 19


                def TreeView_SortChildren(hwnd, hitem, recurse):
                    return BOOLSNDMSGhwnd, TVM_SORTCHILDREN, WPARAMrecurse, LPARAMHTREEITEMhitem
                TVM_ENSUREVISIBLE = TV_FIRST + 20


                def TreeView_EnsureVisible(hwnd, hitem):
                    return BOOLSNDMSGhwnd, TVM_ENSUREVISIBLE, 0, LPARAMHTREEITEMhitem
                TVM_SORTCHILDRENCB = TV_FIRST + 21


                def TreeView_SortChildrenCB(hwnd, psort, recurse):
                    return BOOLSNDMSGhwnd, TVM_SORTCHILDRENCB, WPARAMrecurse, LPARAMLPTV_SORTCBpsort
                TVM_ENDEDITLABELNOW = TV_FIRST + 22


                def TreeView_EndEditLabelNow(hwnd, fCancel):
                    return BOOLSNDMSG(hwnd, TVM_ENDEDITLABELNOW, WPARAMfCancel, 0)
                TVM_GETISEARCHSTRINGA = TV_FIRST + 23
                TVM_GETISEARCHSTRINGW = TV_FIRST + 64

                if defined(UNICODE):
                    TVM_GETISEARCHSTRING = TVM_GETISEARCHSTRINGW
                else:
                    TVM_GETISEARCHSTRING = TVM_GETISEARCHSTRINGA
                # END IF
                TVM_SETTOOLTIPS = TV_FIRST + 24


                def TreeView_SetToolTips(hwnd, hwndTT):
                    return HWNDSNDMSG(hwnd, TVM_SETTOOLTIPS, WPARAMhwndTT, 0)
                TVM_GETTOOLTIPS = TV_FIRST + 25


                def TreeView_GetToolTips(hwnd):
                    return HWNDSNDMSG(hwnd, TVM_GETTOOLTIPS, 0, 0)


                def TreeView_GetISearchString(hwndTV, lpsz):
                    return BOOLSNDMSGhwndTV, TVM_GETISEARCHSTRING, 0, LPARAMLPTSTRlpsz
                TVM_SETINSERTMARK = TV_FIRST + 26


                def TreeView_SetInsertMark(hwnd, hItem, fAfter):
                    return BOOLSNDMSGhwnd, TVM_SETINSERTMARK, WPARAM fAfter, LPARAM hItem
                TVM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT


                def TreeView_SetUnicodeFormat(hwnd, fUnicode):
                    return BOOLSNDMSG(hwnd, TVM_SETUNICODEFORMAT, WPARAMfUnicode, 0)
                TVM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT


                def TreeView_GetUnicodeFormat(hwnd):
                    return BOOLSNDMSG(hwnd, TVM_GETUNICODEFORMAT, 0, 0)
                TVM_SETITEMHEIGHT = TV_FIRST + 27


                def TreeView_SetItemHeight(hwnd, iHeight):
                    return INTSNDMSG(hwnd, TVM_SETITEMHEIGHT, WPARAMiHeight, 0)
                TVM_GETITEMHEIGHT = TV_FIRST + 28


                def TreeView_GetItemHeight(hwnd):
                    return INTSNDMSG(hwnd, TVM_GETITEMHEIGHT, 0, 0)
                TVM_SETBKCOLOR = TV_FIRST + 29


                def TreeView_SetBkColor(hwnd, clr):
                    return COLORREFSNDMSGhwnd, TVM_SETBKCOLOR, 0, LPARAMclr
                TVM_SETTEXTCOLOR = TV_FIRST + 30


                def TreeView_SetTextColor(hwnd, clr):
                    return COLORREFSNDMSGhwnd, TVM_SETTEXTCOLOR, 0, LPARAMclr
                TVM_GETBKCOLOR = TV_FIRST + 31


                def TreeView_GetBkColor(hwnd):
                    return COLORREFSNDMSG(hwnd, TVM_GETBKCOLOR, 0, 0)
                TVM_GETTEXTCOLOR = TV_FIRST + 32


                def TreeView_GetTextColor(hwnd):
                    return COLORREFSNDMSG(hwnd, TVM_GETTEXTCOLOR, 0, 0)
                TVM_SETSCROLLTIME = TV_FIRST + 33


                def TreeView_SetScrollTime(hwnd, uTime):
                    return UINTSNDMSG(hwnd, TVM_SETSCROLLTIME, uTime, 0)
                TVM_GETSCROLLTIME = TV_FIRST + 34


                def TreeView_GetScrollTime(hwnd):
                    return UINTSNDMSG(hwnd, TVM_GETSCROLLTIME, 0, 0)
                TVM_SETINSERTMARKCOLOR = TV_FIRST + 37


                def TreeView_SetInsertMarkColor(hwnd, clr):
                    return COLORREFSNDMSGhwnd, TVM_SETINSERTMARKCOLOR, 0, LPARAMclr
                TVM_GETINSERTMARKCOLOR = TV_FIRST + 38


                def TreeView_GetInsertMarkColor(hwnd):
                    return COLORREFSNDMSG(hwnd, TVM_GETINSERTMARKCOLOR, 0, 0)
                TVM_SETBORDER = TV_FIRST + 35


                def TreeView_SetBorder(hwnd, dwFlags, xBorder, yBorder):
                    return INTSNDMSGhwnd, TVM_SETBORDER, WPARAMdwFlags, MAKELPARAMxBorder, yBorder
                TVSBF_XBORDER = 0x00000001
                TVSBF_YBORDER = 0x00000002

                # tvm_?etitemstate only uses mask, state and stateMask.

                # so unicode or ansi is irrelevant.


                def TreeView_SetItemState(hwndTV, hti, data, _mask):
                    return { TVITEM _ms_TVi; _ms_TVi.mask = TVIF_STATE; _ms_TVi.hItem = hti; _ms_TVi.stateMask = _mask; _ms_TVi.state = data; SNDMSG(hwndTV, TVM_SETITEM, 0, LPARAMTV_ITEM * & _ms_TVi); }


                def TreeView_SetCheckState(hwndTV, hti, fCheck):
                    return TreeView_SetItemState(hwndTV, hti, INDEXTOSTATEIMAGEMASK(fCheck?2:1), TVIS_STATEIMAGEMASK)
                TVM_GETITEMSTATE = TV_FIRST + 39


                def TreeView_GetItemState(hwndTV, hti, mask):
                    return UINTSNDMSGhwndTV, TVM_GETITEMSTATE, WPARAMhti, LPARAMmask


                def TreeView_GetCheckState(hwndTV, hti):
                    return (((UINT(SNDMSG(hwndTV, TVM_GETITEMSTATE, WPARAMhti, TVIS_STATEIMAGEMASK))) >> 12) - 1)
                TVM_SETLINECOLOR = TV_FIRST + 40


                def TreeView_SetLineColor(hwnd, clr):
                    return COLORREFSNDMSGhwnd, TVM_SETLINECOLOR, 0, LPARAMclr
                TVM_GETLINECOLOR = TV_FIRST + 41


                def TreeView_GetLineColor(hwnd):
                    return COLORREFSNDMSG(hwnd, TVM_GETLINECOLOR, 0, 0)

                if NTDDI_VERSION >= NTDDI_WINXP:
                    TVM_MAPACCIDTOHTREEITEM = TV_FIRST + 42


                    def TreeView_MapAccIDToHTREEITEM(hwnd, id):
                        return HTREEITEMSNDMSG(hwnd, TVM_MAPACCIDTOHTREEITEM, id, 0)
                    TVM_MAPHTREEITEMTOACCID = TV_FIRST + 43


                    def TreeView_MapHTREEITEMToAccID(hwnd, htreeitem):
                        return UINTSNDMSG(hwnd, TVM_MAPHTREEITEMTOACCID, WPARAMhtreeitem, 0)
                    TVM_SETEXTENDEDSTYLE = TV_FIRST + 44


                    def TreeView_SetExtendedStyle(hwnd, dw, mask):
                        return DWORDSNDMSG(hwnd, TVM_SETEXTENDEDSTYLE, mask, dw)
                    TVM_GETEXTENDEDSTYLE = TV_FIRST + 45


                    def TreeView_GetExtendedStyle(hwnd):
                        return DWORDSNDMSG(hwnd, TVM_GETEXTENDEDSTYLE, 0, 0)
                    TVM_SETAUTOSCROLLINFO = TV_FIRST + 59


                    def TreeView_SetAutoScrollInfo(hwnd, uPixPerSec, uUpdateTime):
                        return SNDMSGhwnd, TVM_SETAUTOSCROLLINFO, WPARAMuPixPerSec, LPARAMuUpdateTime
                # END IF
                TVM_SETHOT = TV_FIRST + 58


                def TreeView_SetHot(hwnd, hitem):
                    return SNDMSGhwnd, TVM_SETHOT, 0, LPARAMhitem

                if NTDDI_VERSION >= NTDDI_VISTA:
                    TVM_GETSELECTEDCOUNT = TV_FIRST + 70


                    def TreeView_GetSelectedCount(hwnd):
                        return DWORDSNDMSG(hwnd, TVM_GETSELECTEDCOUNT, 0, 0)
                    TVM_SHOWINFOTIP = TV_FIRST + 71


                    def TreeView_ShowInfoTip(hwnd, hitem):
                        return DWORDSNDMSGhwnd, TVM_SHOWINFOTIP, 0, LPARAMhitem


                    class _TVITEMPART(ENUM):
                        TVGIPR_BUTTON = 0x0001


                    TVITEMPART = _TVITEMPART
                    class tagTVGETITEMPARTRECTINFO(ctypes.Structure):
                        pass


                    tagTVGETITEMPARTRECTINFO._fields_ = [
                        ('hti', HTREEITEM),
                        ('prc', POINTER(RECT)),
                        ('partID', TVITEMPART),
                    ]
                    TVGETITEMPARTRECTINFO = tagTVGETITEMPARTRECTINFO
                    TVM_GETITEMPARTRECT = TV_FIRST + 72


                    def TreeView_GetItemPartRect(hwnd, hitem, prc, partid):
                        return { TVGETITEMPARTRECTINFO info; info.hti = hitem; info.prc = prc; info.partID = partid; BOOLSNDMSG(hwnd, TVM_GETITEMPARTRECT, 0, LPARAM & info); }
                # END IF
                (CALLBACK = INT
                PFNTVCOMPARE)(LPARAM = POINTER(INT)
                lParam1 = INT
                LPARAM = INT
                lParam2 = INT
                LPARAM = INT
                lParamSort) = INT
                LPTV_SORTCB = LPTVSORTCB
                TV_SORTCB = TVSORTCB
                class tagTVSORTCB(ctypes.Structure):
                    pass


                tagTVSORTCB._fields_ = [
                    ('hParent', HTREEITEM),
                    ('lpfnCompare', PFNTVCOMPARE),
                    ('lParam', LPARAM),
                ]
                TVSORTCB = tagTVSORTCB
                LPTVSORTCB = POINTER(tagTVSORTCB)
                LPNM_TREEVIEWA = LPNMTREEVIEWA
                LPNM_TREEVIEWW = LPNMTREEVIEWW
                NM_TREEVIEWW = NMTREEVIEWW
                NM_TREEVIEWA = NMTREEVIEWA
                LPNM_TREEVIEW = LPNMTREEVIEW
                NM_TREEVIEW = NMTREEVIEW
                class tagNMTREEVIEWA(ctypes.Structure):
                    pass


                tagNMTREEVIEWA._fields_ = [
                    ('hdr', NMHDR),
                    ('action', UINT),
                    ('itemOld', TVITEMA),
                    ('itemNew', TVITEMA),
                    ('ptDrag', POINT),
                ]
                NMTREEVIEWA = tagNMTREEVIEWA
                LPNMTREEVIEWA = POINTER(tagNMTREEVIEWA)
                class tagNMTREEVIEWW(ctypes.Structure):
                    pass


                tagNMTREEVIEWW._fields_ = [
                    ('hdr', NMHDR),
                    ('action', UINT),
                    ('itemOld', TVITEMW),
                    ('itemNew', TVITEMW),
                    ('ptDrag', POINT),
                ]
                NMTREEVIEWW = tagNMTREEVIEWW
                LPNMTREEVIEWW = POINTER(tagNMTREEVIEWW)

                if defined(UNICODE):
                    NMTREEVIEW = NMTREEVIEWW
                    LPNMTREEVIEW = LPNMTREEVIEWW
                else:
                    NMTREEVIEW = NMTREEVIEWA
                    LPNMTREEVIEW = LPNMTREEVIEWA
                # END IF
                TVN_SELCHANGINGA = TVN_FIRST - 1
                TVN_SELCHANGINGW = TVN_FIRST - 50
                TVN_SELCHANGEDA = TVN_FIRST - 2
                TVN_SELCHANGEDW = TVN_FIRST - 51
                TVC_UNKNOWN = 0x0000
                TVC_BYMOUSE = 0x0001
                TVC_BYKEYBOARD = 0x0002
                TVN_GETDISPINFOA = TVN_FIRST - 3
                TVN_GETDISPINFOW = TVN_FIRST - 52
                TVN_SETDISPINFOA = TVN_FIRST - 4
                TVN_SETDISPINFOW = TVN_FIRST - 53
                TVIF_DI_SETITEM = 0x1000
                TV_DISPINFOA = NMTVDISPINFOA
                TV_DISPINFOW = NMTVDISPINFOW
                TV_DISPINFO = NMTVDISPINFO
                class tagTVDISPINFOA(ctypes.Structure):
                    pass


                tagTVDISPINFOA._fields_ = [
                    ('hdr', NMHDR),
                    ('item', TVITEMA),
                ]
                NMTVDISPINFOA = tagTVDISPINFOA
                LPNMTVDISPINFOA = POINTER(tagTVDISPINFOA)
                class tagTVDISPINFOW(ctypes.Structure):
                    pass


                tagTVDISPINFOW._fields_ = [
                    ('hdr', NMHDR),
                    ('item', TVITEMW),
                ]
                NMTVDISPINFOW = tagTVDISPINFOW
                LPNMTVDISPINFOW = POINTER(tagTVDISPINFOW)

                if defined(UNICODE):
                    NMTVDISPINFO = NMTVDISPINFOW
                    LPNMTVDISPINFO = LPNMTVDISPINFOW
                else:
                    NMTVDISPINFO = NMTVDISPINFOA
                    LPNMTVDISPINFO = LPNMTVDISPINFOA
                # END IF

                if _WIN32_IE >= 0x0600:
                    class tagTVDISPINFOEXA(ctypes.Structure):
                        pass


                    tagTVDISPINFOEXA._fields_ = [
                        ('hdr', NMHDR),
                        ('item', TVITEMEXA),
                    ]
                    NMTVDISPINFOEXA = tagTVDISPINFOEXA
                    LPNMTVDISPINFOEXA = POINTER(tagTVDISPINFOEXA)
                    class tagTVDISPINFOEXW(ctypes.Structure):
                        pass


                    tagTVDISPINFOEXW._fields_ = [
                        ('hdr', NMHDR),
                        ('item', TVITEMEXW),
                    ]
                    NMTVDISPINFOEXW = tagTVDISPINFOEXW
                    LPNMTVDISPINFOEXW = POINTER(tagTVDISPINFOEXW)
                    if defined(UNICODE):
                        NMTVDISPINFOEX = NMTVDISPINFOEXW
                        LPNMTVDISPINFOEX = LPNMTVDISPINFOEXW
                    else:
                        NMTVDISPINFOEX = NMTVDISPINFOEXA
                        LPNMTVDISPINFOEX = LPNMTVDISPINFOEXA
                    # END IF
                    TV_DISPINFOEXA = NMTVDISPINFOEXA
                    TV_DISPINFOEXW = NMTVDISPINFOEXW
                    TV_DISPINFOEX = NMTVDISPINFOEX
                # END IF
                TVN_ITEMEXPANDINGA = TVN_FIRST - 5
                TVN_ITEMEXPANDINGW = TVN_FIRST - 54
                TVN_ITEMEXPANDEDA = TVN_FIRST - 6
                TVN_ITEMEXPANDEDW = TVN_FIRST - 55
                TVN_BEGINDRAGA = TVN_FIRST - 7
                TVN_BEGINDRAGW = TVN_FIRST - 56
                TVN_BEGINRDRAGA = TVN_FIRST - 8
                TVN_BEGINRDRAGW = TVN_FIRST - 57
                TVN_DELETEITEMA = TVN_FIRST - 9
                TVN_DELETEITEMW = TVN_FIRST - 58
                TVN_BEGINLABELEDITA = TVN_FIRST - 10
                TVN_BEGINLABELEDITW = TVN_FIRST - 59
                TVN_ENDLABELEDITA = TVN_FIRST - 11
                TVN_ENDLABELEDITW = TVN_FIRST - 60
                TVN_KEYDOWN = TVN_FIRST - 12
                TVN_GETINFOTIPA = TVN_FIRST - 13
                TVN_GETINFOTIPW = TVN_FIRST - 14
                TVN_SINGLEEXPAND = TVN_FIRST - 15
                TVNRET_DEFAULT = 0
                TVNRET_SKIPOLD = 1
                TVNRET_SKIPNEW = 2

                if _WIN32_IE >= 0x0600:
                    TVN_ITEMCHANGINGA = TVN_FIRST - 16
                    TVN_ITEMCHANGINGW = TVN_FIRST - 17
                    TVN_ITEMCHANGEDA = TVN_FIRST - 18
                    TVN_ITEMCHANGEDW = TVN_FIRST - 19
                    TVN_ASYNCDRAW = TVN_FIRST - 20
                # END IF
                TV_KEYDOWN = NMTVKEYDOWN

                if defined(_WIN32):
                    pass
                # END IF
                class tagTVKEYDOWN(ctypes.Structure):
                    pass


                tagTVKEYDOWN._fields_ = [
                    ('hdr', NMHDR),
                    ('wVKey', WORD),
                    ('flags', UINT),
                ]
                NMTVKEYDOWN = tagTVKEYDOWN
                LPNMTVKEYDOWN = POINTER(tagTVKEYDOWN)
                if defined(_WIN32):
                    pass
                # END IF
                if defined(UNICODE):
                    TVN_SELCHANGING = TVN_SELCHANGINGW
                    TVN_SELCHANGED = TVN_SELCHANGEDW
                    TVN_GETDISPINFO = TVN_GETDISPINFOW
                    TVN_SETDISPINFO = TVN_SETDISPINFOW
                    TVN_ITEMEXPANDING = TVN_ITEMEXPANDINGW
                    TVN_ITEMEXPANDED = TVN_ITEMEXPANDEDW
                    TVN_BEGINDRAG = TVN_BEGINDRAGW
                    TVN_BEGINRDRAG = TVN_BEGINRDRAGW
                    TVN_DELETEITEM = TVN_DELETEITEMW
                    TVN_BEGINLABELEDIT = TVN_BEGINLABELEDITW
                    TVN_ENDLABELEDIT = TVN_ENDLABELEDITW
                else:
                    TVN_SELCHANGING = TVN_SELCHANGINGA
                    TVN_SELCHANGED = TVN_SELCHANGEDA
                    TVN_GETDISPINFO = TVN_GETDISPINFOA
                    TVN_SETDISPINFO = TVN_SETDISPINFOA
                    TVN_ITEMEXPANDING = TVN_ITEMEXPANDINGA
                    TVN_ITEMEXPANDED = TVN_ITEMEXPANDEDA
                    TVN_BEGINDRAG = TVN_BEGINDRAGA
                    TVN_BEGINRDRAG = TVN_BEGINRDRAGA
                    TVN_DELETEITEM = TVN_DELETEITEMA
                    TVN_BEGINLABELEDIT = TVN_BEGINLABELEDITA
                    TVN_ENDLABELEDIT = TVN_ENDLABELEDITA
                # END IF
                NMTVCUSTOMDRAW_V3_SIZE = CCSIZEOF_STRUCT(
                    NMTVCUSTOMDRAW,
                    clrTextBk,
                )
                class tagNMTVCUSTOMDRAW(ctypes.Structure):
                    pass


                tagNMTVCUSTOMDRAW._fields_ = [
                    ('nmcd', NMCUSTOMDRAW),
                    ('clrText', COLORREF),
                    ('clrTextBk', COLORREF),
                    ('iLevel', INT),
                ]
                NMTVCUSTOMDRAW = tagNMTVCUSTOMDRAW
                LPNMTVCUSTOMDRAW = POINTER(tagNMTVCUSTOMDRAW)

                # for tooltips
                class tagNMTVGETINFOTIPA(ctypes.Structure):
                    pass


                tagNMTVGETINFOTIPA._fields_ = [
                    ('hdr', NMHDR),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('hItem', HTREEITEM),
                    ('lParam', LPARAM),
                ]
                NMTVGETINFOTIPA = tagNMTVGETINFOTIPA
                LPNMTVGETINFOTIPA = POINTER(tagNMTVGETINFOTIPA)
                class tagNMTVGETINFOTIPW(ctypes.Structure):
                    pass


                tagNMTVGETINFOTIPW._fields_ = [
                    ('hdr', NMHDR),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('hItem', HTREEITEM),
                    ('lParam', LPARAM),
                ]
                NMTVGETINFOTIPW = tagNMTVGETINFOTIPW
                LPNMTVGETINFOTIPW = POINTER(tagNMTVGETINFOTIPW)

                if defined(UNICODE):
                    TVN_GETINFOTIP = TVN_GETINFOTIPW
                    NMTVGETINFOTIP = NMTVGETINFOTIPW
                    LPNMTVGETINFOTIP = LPNMTVGETINFOTIPW
                else:
                    TVN_GETINFOTIP = TVN_GETINFOTIPA
                    NMTVGETINFOTIP = NMTVGETINFOTIPA
                    LPNMTVGETINFOTIP = LPNMTVGETINFOTIPA
                # END IF

                # treeview's customdraw return meaning don't draw images.
                # valid on CDRF_NOTIFYITEMPREPAINT
                TVCDRF_NOIMAGES = 0x00010000

                if _WIN32_IE > 0x0600:
                    class tagTVITEMCHANGE(ctypes.Structure):
                        pass


                    tagTVITEMCHANGE._fields_ = [
                        ('hdr', NMHDR),
                        ('uChanged', UINT),
                        ('hItem', HTREEITEM),
                        ('uStateNew', UINT),
                        ('uStateOld', UINT),
                        ('lParam', LPARAM),
                    ]
                    NMTVITEMCHANGE = tagTVITEMCHANGE
                    class tagNMTVASYNCDRAW(ctypes.Structure):
                        pass


                    tagNMTVASYNCDRAW._fields_ = [
                        ('hdr', NMHDR),
                        ('pimldp', POINTER(IMAGELISTDRAWPARAMS)), # the draw that failed
                        ('hr', HRESULT), # why it failed
                        ('hItem', HTREEITEM), # item that failed to draw icon
                        ('lParam', LPARAM), # its data
                        ('dwRetFlags', DWORD), # What listview should do on return
                        ('iRetImageIndex', INT), # used if ADRF_DRAWIMAGE is returned
                    ]
                    NMTVASYNCDRAW = tagNMTVASYNCDRAW
                    if defined(UNICODE):
                        TVN_ITEMCHANGING = TVN_ITEMCHANGINGW
                        TVN_ITEMCHANGED = TVN_ITEMCHANGEDW
                    else:
                        TVN_ITEMCHANGING = TVN_ITEMCHANGINGA
                        TVN_ITEMCHANGED = TVN_ITEMCHANGEDA
                    # END IF
                # END IF   _WIN32_IE >= 0x0600
            # END IF   NOTREEVIEW

            if not defined(NOUSEREXCONTROLS):

                # ////////////////// ComboBoxEx
                # ////////////////////////////////
                WC_COMBOBOXEXW = "ComboBoxEx32"
                WC_COMBOBOXEXA = "ComboBoxEx32"

                if defined(UNICODE):
                    WC_COMBOBOXEX = WC_COMBOBOXEXW
                else:
                    WC_COMBOBOXEX = WC_COMBOBOXEXA
                # END IF
                CBEIF_TEXT = 0x00000001
                CBEIF_IMAGE = 0x00000002
                CBEIF_SELECTEDIMAGE = 0x00000004
                CBEIF_OVERLAY = 0x00000008
                CBEIF_INDENT = 0x00000010
                CBEIF_LPARAM = 0x00000020
                CBEIF_DI_SETITEM = 0x10000000
                class tagCOMBOBOXEXITEMA(ctypes.Structure):
                    pass


                tagCOMBOBOXEXITEMA._fields_ = [
                    ('mask', UINT),
                    ('iItem', INT_PTR),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('iSelectedImage', INT),
                    ('iOverlay', INT),
                    ('iIndent', INT),
                    ('lParam', LPARAM),
                ]
                COMBOBOXEXITEMA = tagCOMBOBOXEXITEMA
                PCOMBOBOXEXITEMA = POINTER(tagCOMBOBOXEXITEMA)
                CONST = COMBOBOXEXITEMA
                PCCOMBOEXITEMA = POINTER(COMBOBOXEXITEMA)
                class tagCOMBOBOXEXITEMW(ctypes.Structure):
                    pass


                tagCOMBOBOXEXITEMW._fields_ = [
                    ('mask', UINT),
                    ('iItem', INT_PTR),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('iSelectedImage', INT),
                    ('iOverlay', INT),
                    ('iIndent', INT),
                    ('lParam', LPARAM),
                ]
                COMBOBOXEXITEMW = tagCOMBOBOXEXITEMW
                PCOMBOBOXEXITEMW = POINTER(tagCOMBOBOXEXITEMW)
                CONST = COMBOBOXEXITEMW
                PCCOMBOEXITEMW = POINTER(COMBOBOXEXITEMW)

                if defined(UNICODE):
                    COMBOBOXEXITEM = COMBOBOXEXITEMW
                    PCOMBOBOXEXITEM = PCOMBOBOXEXITEMW
                    PCCOMBOBOXEXITEM = PCCOMBOBOXEXITEMW
                else:
                    COMBOBOXEXITEM = COMBOBOXEXITEMA
                    PCOMBOBOXEXITEM = PCOMBOBOXEXITEMA
                    PCCOMBOBOXEXITEM = PCCOMBOBOXEXITEMA
                # END IF
                CBEM_INSERTITEMA = WM_USER + 1
                CBEM_SETIMAGELIST = WM_USER + 2
                CBEM_GETIMAGELIST = WM_USER + 3
                CBEM_GETITEMA = WM_USER + 4
                CBEM_SETITEMA = WM_USER + 5
                CBEM_DELETEITEM = CB_DELETESTRING
                CBEM_GETCOMBOCONTROL = WM_USER + 6
                CBEM_GETEDITCONTROL = WM_USER + 7
                CBEM_SETEXSTYLE = WM_USER + 8
                CBEM_SETEXTENDEDSTYLE = WM_USER + 14
                CBEM_GETEXSTYLE = WM_USER + 9
                CBEM_GETEXTENDEDSTYLE = WM_USER + 9
                CBEM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
                CBEM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
                CBEM_HASEDITCHANGED = WM_USER + 10
                CBEM_INSERTITEMW = WM_USER + 11
                CBEM_SETITEMW = WM_USER + 12
                CBEM_GETITEMW = WM_USER + 13

                if defined(UNICODE):
                    CBEM_INSERTITEM = CBEM_INSERTITEMW
                    CBEM_SETITEM = CBEM_SETITEMW
                    CBEM_GETITEM = CBEM_GETITEMW
                else:
                    CBEM_INSERTITEM = CBEM_INSERTITEMA
                    CBEM_SETITEM = CBEM_SETITEMA
                    CBEM_GETITEM = CBEM_GETITEMA
                # END IF

                if NTDDI_VERSION >= NTDDI_WINXP:
                    CBEM_SETWINDOWTHEME = CCM_SETWINDOWTHEME
                # END IF
                CBES_EX_NOEDITIMAGE = 0x00000001
                CBES_EX_NOEDITIMAGEINDENT = 0x00000002
                CBES_EX_PATHWORDBREAKPROC = 0x00000004
                CBES_EX_NOSIZELIMIT = 0x00000008
                CBES_EX_CASESENSITIVE = 0x00000010

                if NTDDI_VERSION >= NTDDI_VISTA:
                    CBES_EX_TEXTENDELLIPSIS = 0x00000020
                # END IF
                class NMCOMBOBOXEXA(ctypes.Structure):
                    pass


                NMCOMBOBOXEXA._fields_ = [
                    ('hdr', NMHDR),
                    ('ceItem', COMBOBOXEXITEMA),
                ]
                PNMCOMBOBOXEXA = POINTER(NMCOMBOBOXEXA)
                class NMCOMBOBOXEXW(ctypes.Structure):
                    pass


                NMCOMBOBOXEXW._fields_ = [
                    ('hdr', NMHDR),
                    ('ceItem', COMBOBOXEXITEMW),
                ]
                PNMCOMBOBOXEXW = POINTER(NMCOMBOBOXEXW)

                if defined(UNICODE):
                    NMCOMBOBOXEX = NMCOMBOBOXEXW
                    PNMCOMBOBOXEX = PNMCOMBOBOXEXW
                    CBEN_GETDISPINFO = CBEN_GETDISPINFOW
                else:
                    NMCOMBOBOXEX = NMCOMBOBOXEXA
                    PNMCOMBOBOXEX = PNMCOMBOBOXEXA
                    CBEN_GETDISPINFO = CBEN_GETDISPINFOA
                # END IF
                CBEN_GETDISPINFOA = CBEN_FIRST - 0
                CBEN_INSERTITEM = CBEN_FIRST - 1
                CBEN_DELETEITEM = CBEN_FIRST - 2
                CBEN_BEGINEDIT = CBEN_FIRST - 4
                CBEN_ENDEDITA = CBEN_FIRST - 5
                CBEN_ENDEDITW = CBEN_FIRST - 6
                CBEN_GETDISPINFOW = CBEN_FIRST - 7
                CBEN_DRAGBEGINA = CBEN_FIRST - 8
                CBEN_DRAGBEGINW = CBEN_FIRST - 9

                if defined(UNICODE):
                    CBEN_DRAGBEGIN = CBEN_DRAGBEGINW
                else:
                    CBEN_DRAGBEGIN = CBEN_DRAGBEGINA
                # END IF

                # lParam specifies why the endedit is happening

                if defined(UNICODE):
                    CBEN_ENDEDIT = CBEN_ENDEDITW
                else:
                    CBEN_ENDEDIT = CBEN_ENDEDITA
                # END IF
                CBENF_KILLFOCUS = 1
                CBENF_RETURN = 2
                CBENF_ESCAPE = 3
                CBENF_DROPDOWN = 4
                CBEMAXSTRLEN = 260

                # CBEN_DRAGBEGIN sends this information ...
                class NMCBEDRAGBEGINW(ctypes.Structure):
                    pass


                NMCBEDRAGBEGINW._fields_ = [
                    ('hdr', NMHDR),
                    ('iItemid', INT),
                    ('szText', WCHAR * CBEMAXSTRLEN),
                ]
                LPNMCBEDRAGBEGINW = POINTER(NMCBEDRAGBEGINW)
                PNMCBEDRAGBEGINW = POINTER(NMCBEDRAGBEGINW)
                class NMCBEDRAGBEGINA(ctypes.Structure):
                    pass


                NMCBEDRAGBEGINA._fields_ = [
                    ('hdr', NMHDR),
                    ('iItemid', INT),
                    ('szText', CHAR * CBEMAXSTRLEN),
                ]
                LPNMCBEDRAGBEGINA = POINTER(NMCBEDRAGBEGINA)
                PNMCBEDRAGBEGINA = POINTER(NMCBEDRAGBEGINA)

                if defined(UNICODE):
                    NMCBEDRAGBEGIN = NMCBEDRAGBEGINW
                    LPNMCBEDRAGBEGIN = LPNMCBEDRAGBEGINW
                    PNMCBEDRAGBEGIN = PNMCBEDRAGBEGINW
                else:
                    NMCBEDRAGBEGIN = NMCBEDRAGBEGINA
                    LPNMCBEDRAGBEGIN = LPNMCBEDRAGBEGINA
                    PNMCBEDRAGBEGIN = PNMCBEDRAGBEGINA
                # END IF

                # CBEN_ENDEDIT sends this information...

                # fChanged if the user actually did anything

                # iNewSelection gives what would be the new selection unless
                # the notify is failed

                # iNewSelection may be CB_ERR if there's no match
                class NMCBEENDEDITW(ctypes.Structure):
                    pass


                NMCBEENDEDITW._fields_ = [
                    ('hdr', NMHDR),
                    ('fChanged', BOOL),
                    ('iNewSelection', INT),
                    ('szText', WCHAR * CBEMAXSTRLEN),
                    ('iWhy', INT),
                ]
                LPNMCBEENDEDITW = POINTER(NMCBEENDEDITW)
                PNMCBEENDEDITW = POINTER(NMCBEENDEDITW)
                class NMCBEENDEDITA(ctypes.Structure):
                    pass


                NMCBEENDEDITA._fields_ = [
                    ('hdr', NMHDR),
                    ('fChanged', BOOL),
                    ('iNewSelection', INT),
                    ('szText', CHAR * CBEMAXSTRLEN),
                    ('iWhy', INT),
                ]
                LPNMCBEENDEDITA = POINTER(NMCBEENDEDITA)
                PNMCBEENDEDITA = POINTER(NMCBEENDEDITA)

                if defined(UNICODE):
                    NMCBEENDEDIT = NMCBEENDEDITW
                    LPNMCBEENDEDIT = LPNMCBEENDEDITW
                    PNMCBEENDEDIT = PNMCBEENDEDITW
                else:
                    NMCBEENDEDIT = NMCBEENDEDITA
                    LPNMCBEENDEDIT = LPNMCBEENDEDITA
                    PNMCBEENDEDIT = PNMCBEENDEDITA
                # END IF
            # END IF

            # == == == TAB CONTROL == == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == == ==

            if not defined(NOTABCONTROL):
                if defined(_WIN32):
                    WC_TABCONTROLA = "SysTabControl32"
                    WC_TABCONTROLW = "SysTabControl32"

                    if defined(UNICODE):
                        WC_TABCONTROL = WC_TABCONTROLW
                    else:
                        WC_TABCONTROL = WC_TABCONTROLA
                    # END IF
                else:
                    WC_TABCONTROL = "SysTabControl"
                # END IF

                # begin_r_commctrl
                TCS_SCROLLOPPOSITE = 0x0001
                TCS_BOTTOM = 0x0002
                TCS_RIGHT = 0x0002
                TCS_MULTISELECT = 0x0004
                TCS_FLATBUTTONS = 0x0008
                TCS_FORCEICONLEFT = 0x0010
                TCS_FORCELABELLEFT = 0x0020
                TCS_HOTTRACK = 0x0040
                TCS_VERTICAL = 0x0080
                TCS_TABS = 0x0000
                TCS_BUTTONS = 0x0100
                TCS_SINGLELINE = 0x0000
                TCS_MULTILINE = 0x0200
                TCS_RIGHTJUSTIFY = 0x0000
                TCS_FIXEDWIDTH = 0x0400
                TCS_RAGGEDRIGHT = 0x0800
                TCS_FOCUSONBUTTONDOWN = 0x1000
                TCS_OWNERDRAWFIXED = 0x2000
                TCS_TOOLTIPS = 0x4000
                TCS_FOCUSNEVER = 0x8000

                # end_r_commctrl

                # EX styles for use with TCM_SETEXTENDEDSTYLE
                TCS_EX_FLATSEPARATORS = 0x00000001
                TCS_EX_REGISTERDROP = 0x00000002
                TCM_GETIMAGELIST = TCM_FIRST + 2


                def TabCtrl_GetImageList(hwnd):
                    return HIMAGELISTSNDMSG(hwnd, TCM_GETIMAGELIST, 0, 0L)
                TCM_SETIMAGELIST = TCM_FIRST + 3


                def TabCtrl_SetImageList(hwnd, himl):
                    return HIMAGELISTSNDMSGhwnd, TCM_SETIMAGELIST, 0, LPARAMHIMAGELISThiml
                TCM_GETITEMCOUNT = TCM_FIRST + 4


                def TabCtrl_GetItemCount(hwnd):
                    return INTSNDMSG(hwnd, TCM_GETITEMCOUNT, 0, 0L)
                TCIF_TEXT = 0x0001
                TCIF_IMAGE = 0x0002
                TCIF_RTLREADING = 0x0004
                TCIF_PARAM = 0x0008
                TCIF_STATE = 0x0010
                TCIS_BUTTONPRESSED = 0x0001
                TCIS_HIGHLIGHTED = 0x0002
                TC_ITEMHEADERA = TCITEMHEADERA
                TC_ITEMHEADERW = TCITEMHEADERW
                TC_ITEMHEADER = TCITEMHEADER
                class tagTCITEMHEADERA(ctypes.Structure):
                    pass


                tagTCITEMHEADERA._fields_ = [
                    ('mask', UINT),
                    ('lpReserved1', UINT),
                    ('lpReserved2', UINT),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                ]
                TCITEMHEADERA = tagTCITEMHEADERA
                LPTCITEMHEADERA = POINTER(tagTCITEMHEADERA)
                class tagTCITEMHEADERW(ctypes.Structure):
                    pass


                tagTCITEMHEADERW._fields_ = [
                    ('mask', UINT),
                    ('lpReserved1', UINT),
                    ('lpReserved2', UINT),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                ]
                TCITEMHEADERW = tagTCITEMHEADERW
                LPTCITEMHEADERW = POINTER(tagTCITEMHEADERW)

                if defined(UNICODE):
                    TCITEMHEADER = TCITEMHEADERW
                    LPTCITEMHEADER = LPTCITEMHEADERW
                else:
                    TCITEMHEADER = TCITEMHEADERA
                    LPTCITEMHEADER = LPTCITEMHEADERA
                # END IF
                TC_ITEMA = TCITEMA
                TC_ITEMW = TCITEMW
                TC_ITEM = TCITEM
                class tagTCITEMA(ctypes.Structure):
                    pass


                tagTCITEMA._fields_ = [
                    ('mask', UINT),
                    ('dwState', DWORD),
                    ('dwStateMask', DWORD),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('lParam', LPARAM),
                ]
                TCITEMA = tagTCITEMA
                LPTCITEMA = POINTER(tagTCITEMA)
                class tagTCITEMW(ctypes.Structure):
                    pass


                tagTCITEMW._fields_ = [
                    ('mask', UINT),
                    ('dwState', DWORD),
                    ('dwStateMask', DWORD),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iImage', INT),
                    ('lParam', LPARAM),
                ]
                TCITEMW = tagTCITEMW
                LPTCITEMW = POINTER(tagTCITEMW)

                if defined(UNICODE):
                    TCITEM = TCITEMW
                    LPTCITEM = LPTCITEMW
                else:
                    TCITEM = TCITEMA
                    LPTCITEM = LPTCITEMA
                # END IF
                TCM_GETITEMA = TCM_FIRST + 5
                TCM_GETITEMW = TCM_FIRST + 60

                if defined(UNICODE):
                    TCM_GETITEM = TCM_GETITEMW
                else:
                    TCM_GETITEM = TCM_GETITEMA
                # END IF


                def TabCtrl_GetItem(hwnd, iItem, pitem):
                    return BOOLSNDMSGhwnd, TCM_GETITEM, WPARAMINTiItem, LPARAMTC_ITEM *pitem
                TCM_SETITEMA = TCM_FIRST + 6
                TCM_SETITEMW = TCM_FIRST + 61

                if defined(UNICODE):
                    TCM_SETITEM = TCM_SETITEMW
                else:
                    TCM_SETITEM = TCM_SETITEMA
                # END IF


                def TabCtrl_SetItem(hwnd, iItem, pitem):
                    return BOOLSNDMSGhwnd, TCM_SETITEM, WPARAMINTiItem, LPARAMTC_ITEM *pitem
                TCM_INSERTITEMA = TCM_FIRST + 7
                TCM_INSERTITEMW = TCM_FIRST + 62

                if defined(UNICODE):
                    TCM_INSERTITEM = TCM_INSERTITEMW
                else:
                    TCM_INSERTITEM = TCM_INSERTITEMA
                # END IF


                def TabCtrl_InsertItem(hwnd, iItem, pitem):
                    return INTSNDMSGhwnd, TCM_INSERTITEM, WPARAMINTiItem, LPARAMTC_ITEM *pitem
                TCM_DELETEITEM = TCM_FIRST + 8


                def TabCtrl_DeleteItem(hwnd, i):
                    return BOOLSNDMSG(hwnd, TCM_DELETEITEM, WPARAMINTi, 0L)
                TCM_DELETEALLITEMS = TCM_FIRST + 9


                def TabCtrl_DeleteAllItems(hwnd):
                    return BOOLSNDMSG(hwnd, TCM_DELETEALLITEMS, 0, 0L)
                TCM_GETITEMRECT = TCM_FIRST + 10


                def TabCtrl_GetItemRect(hwnd, i, prc):
                    return BOOLSNDMSGhwnd, TCM_GETITEMRECT, WPARAMINTi, LPARAMRECT *prc
                TCM_GETCURSEL = TCM_FIRST + 11


                def TabCtrl_GetCurSel(hwnd):
                    return INTSNDMSG(hwnd, TCM_GETCURSEL, 0, 0)
                TCM_SETCURSEL = TCM_FIRST + 12


                def TabCtrl_SetCurSel(hwnd, i):
                    return INTSNDMSG(hwnd, TCM_SETCURSEL, WPARAMi, 0)
                TCHT_NOWHERE = 0x0001
                TCHT_ONITEMICON = 0x0002
                TCHT_ONITEMLABEL = 0x0004
                TCHT_ONITEM = TCHT_ONITEMICON | TCHT_ONITEMLABEL
                LPTC_HITTESTINFO = LPTCHITTESTINFO
                TC_HITTESTINFO = TCHITTESTINFO
                class tagTCHITTESTINFO(ctypes.Structure):
                    pass


                tagTCHITTESTINFO._fields_ = [
                    ('pt', POINT),
                    ('flags', UINT),
                ]
                TCHITTESTINFO = tagTCHITTESTINFO
                LPTCHITTESTINFO = POINTER(tagTCHITTESTINFO)
                TCM_HITTEST = TCM_FIRST + 13


                def TabCtrl_HitTest(hwndTC, pinfo):
                    return INTSNDMSGhwndTC, TCM_HITTEST, 0, LPARAMTC_HITTESTINFO *pinfo
                TCM_SETITEMEXTRA = TCM_FIRST + 14


                def TabCtrl_SetItemExtra(hwndTC, cb):
                    return BOOLSNDMSG(hwndTC, TCM_SETITEMEXTRA, WPARAMcb, 0L)
                TCM_ADJUSTRECT = TCM_FIRST + 40


                def TabCtrl_AdjustRect(hwnd, bLarger, prc):
                    return INTSNDMSG(hwnd, TCM_ADJUSTRECT, WPARAMBOOLbLarger, LPARAMRECT *prc)
                TCM_SETITEMSIZE = TCM_FIRST + 41


                def TabCtrl_SetItemSize(hwnd, x, y):
                    return DWORDSNDMSGhwnd, TCM_SETITEMSIZE, 0, MAKELPARAMx,y
                TCM_REMOVEIMAGE = TCM_FIRST + 42


                def TabCtrl_RemoveImage(hwnd, i):
                    return VOIDSNDMSG(hwnd, TCM_REMOVEIMAGE, i, 0L)
                TCM_SETPADDING = TCM_FIRST + 43


                def TabCtrl_SetPadding(hwnd, cx, cy):
                    return VOIDSNDMSGhwnd, TCM_SETPADDING, 0, MAKELPARAMcx, cy
                TCM_GETROWCOUNT = TCM_FIRST + 44


                def TabCtrl_GetRowCount(hwnd):
                    return INTSNDMSG(hwnd, TCM_GETROWCOUNT, 0, 0L)
                TCM_GETTOOLTIPS = TCM_FIRST + 45


                def TabCtrl_GetToolTips(hwnd):
                    return HWNDSNDMSG(hwnd, TCM_GETTOOLTIPS, 0, 0L)
                TCM_SETTOOLTIPS = TCM_FIRST + 46


                def TabCtrl_SetToolTips(hwnd, hwndTT):
                    return VOIDSNDMSG(hwnd, TCM_SETTOOLTIPS, WPARAMhwndTT, 0L)
                TCM_GETCURFOCUS = TCM_FIRST + 47


                def TabCtrl_GetCurFocus(hwnd):
                    return INTSNDMSG(hwnd, TCM_GETCURFOCUS, 0, 0)
                TCM_SETCURFOCUS = TCM_FIRST + 48


                def TabCtrl_SetCurFocus(hwnd, i):
                    return SNDMSG(hwnd,TCM_SETCURFOCUS, i, 0)
                TCM_SETMINTABWIDTH = TCM_FIRST + 49


                def TabCtrl_SetMinTabWidth(hwnd, x):
                    return INTSNDMSG(hwnd, TCM_SETMINTABWIDTH, 0, x)
                TCM_DESELECTALL = TCM_FIRST + 50


                def TabCtrl_DeselectAll(hwnd, fExcludeFocus):
                    return VOIDSNDMSG(hwnd, TCM_DESELECTALL, fExcludeFocus, 0)
                TCM_HIGHLIGHTITEM = TCM_FIRST + 51


                def TabCtrl_HighlightItem(hwnd, i, fHighlight):
                    return BOOLSNDMSGhwnd, TCM_HIGHLIGHTITEM, WPARAMi, LPARAMMAKELONG fHighlight, 0
                TCM_SETEXTENDEDSTYLE = TCM_FIRST + 52


                def TabCtrl_SetExtendedStyle(hwnd, dw):
                    return DWORDSNDMSG(hwnd, TCM_SETEXTENDEDSTYLE, 0, dw)
                TCM_GETEXTENDEDSTYLE = TCM_FIRST + 53


                def TabCtrl_GetExtendedStyle(hwnd):
                    return DWORDSNDMSG(hwnd, TCM_GETEXTENDEDSTYLE, 0, 0)
                TCM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT


                def TabCtrl_SetUnicodeFormat(hwnd, fUnicode):
                    return BOOLSNDMSG(hwnd, TCM_SETUNICODEFORMAT, WPARAMfUnicode, 0)
                TCM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT


                def TabCtrl_GetUnicodeFormat(hwnd):
                    return BOOLSNDMSG(hwnd, TCM_GETUNICODEFORMAT, 0, 0)
                TCN_KEYDOWN = TCN_FIRST - 0
                TC_KEYDOWN = NMTCKEYDOWN

                if defined(_WIN32):
                    pass
                # END IF
                class tagTCKEYDOWN(ctypes.Structure):
                    pass


                tagTCKEYDOWN._fields_ = [
                    ('hdr', NMHDR),
                    ('wVKey', WORD),
                    ('flags', UINT),
                ]
                NMTCKEYDOWN = tagTCKEYDOWN
                if defined(_WIN32):
                    pass
                # END IF
                TCN_SELCHANGE = TCN_FIRST - 1
                TCN_SELCHANGING = TCN_FIRST - 2
                TCN_GETOBJECT = TCN_FIRST - 3
                TCN_FOCUSCHANGE = TCN_FIRST - 4
            # END IF   NOTABCONTROL

            # == == == ANIMATE CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == ==

            if not defined(NOANIMATE):
                if defined(_WIN32):
                    ANIMATE_CLASSW = "SysAnimate32"
                    ANIMATE_CLASSA = "SysAnimate32"

                    if defined(UNICODE):
                        ANIMATE_CLASS = ANIMATE_CLASSW
                    else:
                        ANIMATE_CLASS = ANIMATE_CLASSA
                    # END IF

                    # begin_r_commctrl
                    ACS_CENTER = 0x0001
                    ACS_TRANSPARENT = 0x0002
                    ACS_AUTOPLAY = 0x0004
                    ACS_TIMER = 0x0008

                    # end_r_commctrl
                    ACM_OPENA = WM_USER + 100
                    ACM_OPENW = WM_USER + 103

                    if defined(UNICODE):
                        ACM_OPEN = ACM_OPENW
                    else:
                        ACM_OPEN = ACM_OPENA
                    # END IF
                    ACM_PLAY = WM_USER + 101
                    ACM_STOP = WM_USER + 102
                    ACM_ISPLAYING = WM_USER + 104
                    ACN_START = 1
                    ACN_STOP = 2


                    def Animate_Create(hwndP, id, dwStyle, hInstance):
                        return CreateWindow(ANIMATE_CLASS, NULL, dwStyle, 0, 0, 0, 0, hwndP, HMENUid, hInstance, NULL)


                    def Animate_Open(hwnd, szName):
                        return BOOLSNDMSG(hwnd, ACM_OPEN, 0, LPARAMLPTSTRszName)


                    def Animate_OpenEx(hwnd, hInst, szName):
                        return BOOLSNDMSG(hwnd, ACM_OPEN, WPARAMhInst, LPARAMLPTSTRszName)


                    def Animate_Play(hwnd, from, to, rep):
                        return BOOLSNDMSG(hwnd, ACM_PLAY, WPARAMrep, LPARAMMAKELONGfrom, to)


                    def Animate_Stop(hwnd):
                        return BOOLSNDMSGhwnd, ACM_STOP, 0, 0


                    def Animate_IsPlaying(hwnd):
                        return BOOLSNDMSGhwnd, ACM_ISPLAYING, 0, 0


                    def Animate_Close(hwnd):
                        return Animate_Openhwnd, NULL


                    def Animate_Seek(hwnd, frame):
                        return Animate_Playhwnd, frame, frame, 1
                # END IF
            # END IF   NOANIMATE

            # == == == MONTHCAL CONTROL == == == == == == == == == == == == ==
            # == == == == == == == == == == == == == ==

            if not defined(NOMONTHCAL):
                if defined(_WIN32):
                    MONTHCAL_CLASSW = "SysMonthCal32"
                    MONTHCAL_CLASSA = "SysMonthCal32"

                    if defined(UNICODE):
                        MONTHCAL_CLASS = MONTHCAL_CLASSW
                    else:
                        MONTHCAL_CLASS = MONTHCAL_CLASSA
                    # END IF

                    # bit - packed array of "bold" info for a month

                    # if a bit is on, that day is drawn bold
                    MONTHDAYSTATE = DWORD
                    LPMONTHDAYSTATE = POINTER(DWORD)
                    MCM_FIRST = 0x1000

                    # BOOL MonthCal_GetCurSel(HWND hmc, LPSYSTEMTIME pst)

                    # returns FALSE if MCS_MULTISELECT

                    # returns TRUE and sets *pst to the currently selected
                    # date otherwise
                    MCM_GETCURSEL = MCM_FIRST + 1


                    def MonthCal_GetCurSel(hmc, pst):
                        return BOOLSNDMSG(hmc, MCM_GETCURSEL, 0, LPARAMpst)

                    # BOOL MonthCal_SetCurSel(HWND hmc, LPSYSTEMTIME pst)

                    # returns FALSE if MCS_MULTISELECT

                    # returns TURE and sets the currently selected date to
                    # *pst otherwise
                    MCM_SETCURSEL = MCM_FIRST + 2


                    def MonthCal_SetCurSel(hmc, pst):
                        return BOOLSNDMSG(hmc, MCM_SETCURSEL, 0, LPARAMpst)

                    # DWORD MonthCal_GetMaxSelCount(HWND hmc)

                    # returns the maximum number of selectable days allowed
                    MCM_GETMAXSELCOUNT = MCM_FIRST + 3


                    def MonthCal_GetMaxSelCount(hmc):
                        return DWORDSNDMSGhmc, MCM_GETMAXSELCOUNT, 0, 0L

                    # BOOL MonthCal_SetMaxSelCount(HWND hmc, UINT n)

                    # sets the max number days that can be selected iff
                    # MCS_MULTISELECT
                    MCM_SETMAXSELCOUNT = MCM_FIRST + 4


                    def MonthCal_SetMaxSelCount(hmc, n):
                        return BOOLSNDMSG(hmc, MCM_SETMAXSELCOUNT, WPARAMn, 0L)

                    # BOOL MonthCal_GetSelRange(HWND hmc, LPSYSTEMTIME rgst)

                    # sets rgst[0] to the first day of the selection range

                    # sets rgst[1] to the last day of the selection range
                    MCM_GETSELRANGE = MCM_FIRST + 5


                    def MonthCal_GetSelRange(hmc, rgst):
                        return SNDMSG(hmc, MCM_GETSELRANGE, 0, LPARAMrgst)

                    # BOOL MonthCal_SetSelRange(HWND hmc, LPSYSTEMTIME rgst)

                    # selects the range of days from rgst[0] to rgst[1]
                    MCM_SETSELRANGE = MCM_FIRST + 6


                    def MonthCal_SetSelRange(hmc, rgst):
                        return SNDMSG(hmc, MCM_SETSELRANGE, 0, LPARAMrgst)

                    # DWORD
                    # MonthCal_GetMonthRange(HWND hmc, gmr, LPSYSTEMTIME rgst)

                    # if rgst specified, sets rgst[0] to the starting date and

                    # and rgst[1] to the ending date of the the selectable
                    # (non - grayed)

                    # days if GMR_VISIBLE or all the displayed days
                    # (including grayed)

                    # if GMR_DAYSTATE.

                    # returns the number of months spanned by the above range.
                    MCM_GETMONTHRANGE = MCM_FIRST + 7


                    def MonthCal_GetMonthRange(hmc, gmr, rgst):
                        return DWORDSNDMSG(hmc, MCM_GETMONTHRANGE, WPARAMgmr, LPARAMrgst)

                    # BOOL
                    # MonthCal_SetDayState(HWND hmc, INT cbds, DAYSTATE *rgds)

                    # cbds is the count of DAYSTATE items in rgds and it must
                    # be equal

                    # to the value returned from
                    # MonthCal_GetMonthRange(hmc, GMR_DAYSTATE, NULL)

                    # This sets the DAYSTATE bits for each month
                    # (grayed and non - grayed

                    # days) displayed in the calendar. The first bit in a month's DAYSTATE
                    #

                    # corresponts to bolding day 1, the second bit affects day
                    # 2, etc.
                    MCM_SETDAYSTATE = MCM_FIRST + 8


                    def MonthCal_SetDayState(hmc, cbds, rgds):
                        return SNDMSG(hmc, MCM_SETDAYSTATE, WPARAMcbds, LPARAMrgds)

                    # BOOL MonthCal_GetMinReqRect(HWND hmc, LPRECT prc)

                    # sets *prc the minimal size needed to display one month

                    # To display two months, undo the AdjustWindowRect
                    # calculation already done to

                    # this rect, DOUBLE the width, and redo the
                    # AdjustWindowRect calculation - -

                    # the monthcal control will display two calendars in this
                    # window (if you also

                    # DOUBLE the vertical size, you will get 4 calendars)

                    # NOTE: if you want to gurantee that the "Today" string is
                    # not clipped,

                    # get the MCM_GETMAXTODAYWIDTH and use the max of that
                    # width and this width
                    MCM_GETMINREQRECT = MCM_FIRST + 9


                    def MonthCal_GetMinReqRect(hmc, prc):
                        return SNDMSG(hmc, MCM_GETMINREQRECT, 0, LPARAMprc)

                    # set colors to draw control with - - see MCSC_ bits below
                    MCM_SETCOLOR = MCM_FIRST + 10


                    def MonthCal_SetColor(hmc, iColor, clr):
                        return SNDMSGhmc, MCM_SETCOLOR, iColor, clr
                    MCM_GETCOLOR = MCM_FIRST + 11


                    def MonthCal_GetColor(hmc, iColor):
                        return SNDMSGhmc, MCM_GETCOLOR, iColor, 0
                    MCSC_BACKGROUND = 0
                    MCSC_TEXT = 1
                    MCSC_TITLEBK = 2
                    MCSC_TITLETEXT = 3
                    MCSC_MONTHBK = 4
                    MCSC_TRAILINGTEXT = 5

                    # set what day is "today" send NULL to revert back to real
                    # date
                    MCM_SETTODAY = MCM_FIRST + 12


                    def MonthCal_SetToday(hmc, pst):
                        return SNDMSG(hmc, MCM_SETTODAY, 0, LPARAMpst)

                    # get what day is "today"

                    # returns BOOL for success/failure
                    MCM_GETTODAY = MCM_FIRST + 13


                    def MonthCal_GetToday(hmc, pst):
                        return BOOLSNDMSG(hmc, MCM_GETTODAY, 0, LPARAMpst)

                    # determine what pinfo - >pt is over
                    MCM_HITTEST = MCM_FIRST + 14


                    def MonthCal_HitTest(hmc, pinfo):
                        return SNDMSG(hmc, MCM_HITTEST, 0, LPARAMPMCHITTESTINFOpinfo)
                    class MCHITTESTINFO(ctypes.Structure):
                        pass


                    MCHITTESTINFO._fields_ = [
                        ('cbSize', UINT),
                        ('pt', POINT),
                        ('uHit', UINT), # out param
                        ('st', SYSTEMTIME),
                            ('rc', RECT),
                            ('iOffset', INT),
                            ('iRow', INT),
                            ('iCol', INT),
                    ]
                    PMCHITTESTINFO = POINTER(MCHITTESTINFO)

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        pass
                    # END IF
                    MCHITTESTINFO_V1_SIZE = CCSIZEOF_STRUCT(
                        MCHITTESTINFO,
                        st,
                    )
                    MCHT_TITLE = 0x00010000
                    MCHT_CALENDAR = 0x00020000
                    MCHT_TODAYLINK = 0x00030000

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        MCHT_CALENDARCONTROL = 0x00100000
                    # END IF
                    MCHT_NEXT = 0x01000000
                    MCHT_PREV = 0x02000000
                    MCHT_NOWHERE = 0x00000000
                    MCHT_TITLEBK = MCHT_TITLE
                    MCHT_TITLEMONTH = MCHT_TITLE | 0x0001
                    MCHT_TITLEYEAR = MCHT_TITLE | 0x0002
                    MCHT_TITLEBTNNEXT = MCHT_TITLE | MCHT_NEXT | 0x0003
                    MCHT_TITLEBTNPREV = MCHT_TITLE | MCHT_PREV | 0x0003
                    MCHT_CALENDARBK = MCHT_CALENDAR
                    MCHT_CALENDARDATE = MCHT_CALENDAR | 0x0001
                    MCHT_CALENDARDATENEXT = MCHT_CALENDARDATE | MCHT_NEXT
                    MCHT_CALENDARDATEPREV = MCHT_CALENDARDATE | MCHT_PREV
                    MCHT_CALENDARDAY = MCHT_CALENDAR | 0x0002
                    MCHT_CALENDARWEEKNUM = MCHT_CALENDAR | 0x0003
                    MCHT_CALENDARDATEMIN = MCHT_CALENDAR | 0x0004
                    MCHT_CALENDARDATEMAX = MCHT_CALENDAR | 0x0005

                    # set first day of week to iDay:

                    # 0 for Monday, 1 for Tuesday, ..., 6 for Sunday

                    # - 1 for means use locale info
                    MCM_SETFIRSTDAYOFWEEK = MCM_FIRST + 15


                    def MonthCal_SetFirstDayOfWeek(hmc, iDay):
                        return SNDMSGhmc, MCM_SETFIRSTDAYOFWEEK, 0, iDay

                    # DWORD result... low word has the day. high word is BOOL
                    # if this is app set

                    # or not (FALSE == using locale info)
                    MCM_GETFIRSTDAYOFWEEK = MCM_FIRST + 16


                    def MonthCal_GetFirstDayOfWeek(hmc):
                        return DWORDSNDMSGhmc, MCM_GETFIRSTDAYOFWEEK, 0, 0

                    # DWORD MonthCal_GetRange(HWND hmc, LPSYSTEMTIME rgst)

                    # modifies rgst[0] to be the minimum ALLOWABLE systemtime
                    # (or 0 if no minimum)

                    # modifies rgst[1] to be the maximum ALLOWABLE systemtime
                    # (or 0 if no maximum)

                    # returns GDTR_MIN | GDTR_MAX if there is a minimum |
                    # maximum limit
                    MCM_GETRANGE = MCM_FIRST + 17


                    def MonthCal_GetRange(hmc, rgst):
                        return DWORDSNDMSG(hmc, MCM_GETRANGE, 0, LPARAMrgst)

                    # BOOL
                    # MonthCal_SetRange(HWND hmc, DWORD gdtr, LPSYSTEMTIME rgst)
                    #

                    # if GDTR_MIN, sets the minimum ALLOWABLE systemtime to
                    # rgst[0], otherwise removes minimum

                    # if GDTR_MAX, sets the maximum ALLOWABLE systemtime to
                    # rgst[1], otherwise removes maximum

                    # returns TRUE on success, FALSE on error
                    # (such as invalid parameters)
                    MCM_SETRANGE = MCM_FIRST + 18


                    def MonthCal_SetRange(hmc, gd, rgst):
                        return BOOLSNDMSG(hmc, MCM_SETRANGE, WPARAMgd, LPARAMrgst)

                    # INT MonthCal_GetMonthDelta(HWND hmc)

                    # returns the number of months one click on a next/prev
                    # button moves by
                    MCM_GETMONTHDELTA = MCM_FIRST + 19


                    def MonthCal_GetMonthDelta(hmc):
                        return INTSNDMSGhmc, MCM_GETMONTHDELTA, 0, 0

                    # INT MonthCal_SetMonthDelta(HWND hmc, INT n)

                    # sets the month delta to n. n == 0 reverts to moving by a
                    # page of months

                    # returns the previous value of n.
                    MCM_SETMONTHDELTA = MCM_FIRST + 20


                    def MonthCal_SetMonthDelta(hmc, n):
                        return INTSNDMSGhmc, MCM_SETMONTHDELTA, n, 0

                    # DWORD MonthCal_GetMaxTodayWidth(HWND hmc, LPSIZE psz)

                    # sets *psz to the maximum width/height of the "Today"
                    # string displayed

                    # at the bottom of the calendar
                    # (as LONG as MCS_NOTODAY is not specified)
                    MCM_GETMAXTODAYWIDTH = MCM_FIRST + 21


                    def MonthCal_GetMaxTodayWidth(hmc):
                        return DWORDSNDMSGhmc, MCM_GETMAXTODAYWIDTH, 0, 0
                    MCM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT


                    def MonthCal_SetUnicodeFormat(hwnd, fUnicode):
                        return BOOLSNDMSG(hwnd, MCM_SETUNICODEFORMAT, WPARAMfUnicode, 0)
                    MCM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT


                    def MonthCal_GetUnicodeFormat(hwnd):
                        return BOOLSNDMSG(hwnd, MCM_GETUNICODEFORMAT, 0, 0)

                    if NTDDI_VERSION >= NTDDI_VISTA:

                        # View
                        MCMV_MONTH = 0
                        MCMV_YEAR = 1
                        MCMV_DECADE = 2
                        MCMV_CENTURY = 3
                        MCMV_MAX = MCMV_CENTURY
                        MCM_GETCURRENTVIEW = MCM_FIRST + 22


                        def MonthCal_GetCurrentView(hmc):
                            return DWORDSNDMSGhmc, MCM_GETCURRENTVIEW, 0, 0
                        MCM_GETCALENDARCOUNT = MCM_FIRST + 23


                        def MonthCal_GetCalendarCount(hmc):
                            return DWORDSNDMSGhmc, MCM_GETCALENDARCOUNT, 0, 0

                        # Part
                        MCGIP_CALENDARCONTROL = 0
                        MCGIP_NEXT = 1
                        MCGIP_PREV = 2
                        MCGIP_FOOTER = 3
                        MCGIP_CALENDAR = 4
                        MCGIP_CALENDARHEADER = 5
                        MCGIP_CALENDARBODY = 6
                        MCGIP_CALENDARROW = 7
                        MCGIP_CALENDARCELL = 8
                        MCGIF_DATE = 0x00000001
                        MCGIF_RECT = 0x00000002
                        MCGIF_NAME = 0x00000004

                        # Note: iRow of - 1 refers to the row header and iCol
                        # of - 1 refers to the col header.
                        class tagMCGRIDINFO(ctypes.Structure):
                            pass


                        tagMCGRIDINFO._fields_ = [
                            ('cbSize', UINT),
                            ('dwPart', DWORD),
                            ('dwFlags', DWORD),
                            ('iCalendar', INT),
                            ('iRow', INT),
                            ('iCol', INT),
                            ('bSelected', BOOL),
                            ('stStart', SYSTEMTIME),
                            ('stEnd', SYSTEMTIME),
                            ('rc', RECT),
                            ('pszName', PWSTR),
                            ('cchName', size_t),
                        ]
                        MCGRIDINFO = tagMCGRIDINFO
                        PMCGRIDINFO = POINTER(tagMCGRIDINFO)
                        MCM_GETCALENDARGRIDINFO = MCM_FIRST + 24


                        def MonthCal_GetCalendarGridInfo(hmc, pmcGridInfo):
                            return BOOLSNDMSG(hmc, MCM_GETCALENDARGRIDINFO, 0, LPARAMPMCGRIDINFOpmcGridInfo)
                        MCM_GETCALID = MCM_FIRST + 27


                        def MonthCal_GetCALID(hmc):
                            return CALIDSNDMSGhmc, MCM_GETCALID, 0, 0
                        MCM_SETCALID = MCM_FIRST + 28


                        def MonthCal_SetCALID(hmc, calid):
                            return SNDMSG(hmc, MCM_SETCALID, WPARAMcalid, 0)

                        # Returns the min rect that will fit the max number of
                        # calendars for the passed in rect.
                        MCM_SIZERECTTOMIN = MCM_FIRST + 29


                        def MonthCal_SizeRectToMin(hmc, prc):
                            return SNDMSG(hmc, MCM_SIZERECTTOMIN, 0, LPARAMprc)
                        MCM_SETCALENDARBORDER = MCM_FIRST + 30


                        def MonthCal_SetCalendarBorder(hmc, fset, xyborder):
                            return SNDMSG(hmc, MCM_SETCALENDARBORDER, WPARAMfset, LPARAMxyborder)
                        MCM_GETCALENDARBORDER = MCM_FIRST + 31


                        def MonthCal_GetCalendarBorder(hmc):
                            return INTSNDMSGhmc, MCM_GETCALENDARBORDER, 0, 0
                        MCM_SETCURRENTVIEW = MCM_FIRST + 32


                        def MonthCal_SetCurrentView(hmc, dwNewView):
                            return BOOLSNDMSG(hmc, MCM_SETCURRENTVIEW, 0, LPARAMdwNewView)
                    # END IF

                    # MCN_SELCHANGE is sent whenever the currently displayed
                    # date changes

                    # via month change, year change, keyboard navigation,
                    # prev/next button
                    class tagNMSELCHANGE(ctypes.Structure):
                        pass


                    tagNMSELCHANGE._fields_ = [
                        ('nmhdr', NMHDR), # this must be first, so we don't break WM_NOTIFY
                        ('stSelStart', SYSTEMTIME),
                        ('stSelEnd', SYSTEMTIME),
                    ]
                    NMSELCHANGE = tagNMSELCHANGE
                    LPNMSELCHANGE = POINTER(tagNMSELCHANGE)
                    MCN_SELCHANGE = MCN_FIRST - 3

                    # MCN_GETDAYSTATE is sent for MCS_DAYSTATE controls
                    # whenever new daystate

                    # information is needed (month or year scroll) to draw
                    # bolding information.

                    # The app must fill in cDayState months worth of
                    # information starting from

                    # stStart date. The app may fill in the array at
                    # prgDayState or change

                    # prgDayState to point to a different array out of which
                    # the information

                    # will be copied. (similar to tooltips)
                    class tagNMDAYSTATE(ctypes.Structure):
                        pass


                    tagNMDAYSTATE._fields_ = [
                        ('nmhdr', NMHDR), # this must be first, so we don't break WM_NOTIFY
                        ('stStart', SYSTEMTIME),
                        ('cDayState', INT),
                        ('prgDayState', LPMONTHDAYSTATE), # points to cDayState MONTHDAYSTATEs
                    ]
                    NMDAYSTATE = tagNMDAYSTATE
                    LPNMDAYSTATE = POINTER(tagNMDAYSTATE)
                    MCN_GETDAYSTATE = MCN_FIRST - 1

                    # MCN_SELECT is sent whenever a selection has occured
                    # (via mouse or keyboard)
                    NMSELECT = NMSELCHANGE
                    LPNMSELECT = POINTER(NMSELCHANGE)
                    MCN_SELECT = MCN_FIRST
                    class tagNMVIEWCHANGE(ctypes.Structure):
                        pass


                    tagNMVIEWCHANGE._fields_ = [
                        ('nmhdr', NMHDR), # this must be first, so we don't break WM_NOTIFY
                        ('dwOldView', DWORD),
                        ('dwNewView', DWORD),
                    ]
                    NMVIEWCHANGE = tagNMVIEWCHANGE
                    LPNMVIEWCHANGE = POINTER(tagNMVIEWCHANGE)
                    MCN_VIEWCHANGE = MCN_FIRST - 4

                    # begin_r_commctrl
                    MCS_DAYSTATE = 0x0001
                    MCS_MULTISELECT = 0x0002
                    MCS_WEEKNUMBERS = 0x0004
                    MCS_NOTODAYCIRCLE = 0x0008
                    MCS_NOTODAY = 0x0010

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        MCS_NOTRAILINGDATES = 0x0040
                        MCS_SHORTDAYSOFWEEK = 0x0080
                        MCS_NOSELCHANGEONNAV = 0x0100
                    # END IF

                    # end_r_commctrl
                    GMR_VISIBLE = 0
                    GMR_DAYSTATE = 1

                    # partially displayed months
                # END IF   _WIN32
            # END IF   NOMONTHCAL

            # == == == DATETIMEPICK CONTROL == == == == == == == == == == ==
            # == == == == == == == == == == == == == ==

            if not defined(NODATETIMEPICK):
                if defined(_WIN32):
                    DATETIMEPICK_CLASSW = "SysDateTimePick32"
                    DATETIMEPICK_CLASSA = "SysDateTimePick32"

                    if defined(UNICODE):
                        DATETIMEPICK_CLASS = DATETIMEPICK_CLASSW
                    else:
                        DATETIMEPICK_CLASS = DATETIMEPICK_CLASSA
                    # END IF

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        class tagDATETIMEPICKERINFO(ctypes.Structure):
                            pass


                        tagDATETIMEPICKERINFO._fields_ = [
                            ('cbSize', DWORD),
                            ('rcCheck', RECT),
                            ('stateCheck', DWORD),
                            ('rcButton', RECT),
                            ('stateButton', DWORD),
                            ('hwndEdit', HWND),
                            ('hwndUD', HWND),
                            ('hwndDropDown', HWND),
                        ]
                        DATETIMEPICKERINFO = tagDATETIMEPICKERINFO
                        LPDATETIMEPICKERINFO = POINTER(tagDATETIMEPICKERINFO)
                    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
                    DTM_FIRST = 0x1000

                    # DWORD
                    # DateTimePick_GetSystemtime(HWND hdp, LPSYSTEMTIME pst)

                    # returns GDT_NONE if "none" is selected
                    # (DTS_SHOWNONE only)

                    # returns GDT_VALID and modifies *pst to be the currently
                    # selected value
                    DTM_GETSYSTEMTIME = DTM_FIRST + 1


                    def DateTime_GetSystemtime(hdp, pst):
                        return DWORDSNDMSG(hdp, DTM_GETSYSTEMTIME, 0, LPARAMpst)

                    # BOOL
                    # DateTime_SetSystemtime(HWND hdp, DWORD gd, LPSYSTEMTIME pst)
                    #

                    # if gd == GDT_NONE, sets datetimepick to None
                    # (DTS_SHOWNONE only)

                    # if gd == GDT_VALID, sets datetimepick to *pst

                    # returns TRUE on success, FALSE on error
                    # (such as bad params)
                    DTM_SETSYSTEMTIME = DTM_FIRST + 2


                    def DateTime_SetSystemtime(hdp, gd, pst):
                        return BOOLSNDMSG(hdp, DTM_SETSYSTEMTIME, WPARAMgd, LPARAMpst)

                    # DWORD DateTime_GetRange(HWND hdp, LPSYSTEMTIME rgst)

                    # modifies rgst[0] to be the minimum ALLOWABLE systemtime
                    # (or 0 if no minimum)

                    # modifies rgst[1] to be the maximum ALLOWABLE systemtime
                    # (or 0 if no maximum)

                    # returns GDTR_MIN | GDTR_MAX if there is a minimum |
                    # maximum limit
                    DTM_GETRANGE = DTM_FIRST + 3


                    def DateTime_GetRange(hdp, rgst):
                        return DWORDSNDMSG(hdp, DTM_GETRANGE, 0, LPARAMrgst)

                    # BOOL
                    # DateTime_SetRange(HWND hdp, DWORD gdtr, LPSYSTEMTIME rgst)
                    #

                    # if GDTR_MIN, sets the minimum ALLOWABLE systemtime to
                    # rgst[0], otherwise removes minimum

                    # if GDTR_MAX, sets the maximum ALLOWABLE systemtime to
                    # rgst[1], otherwise removes maximum

                    # returns TRUE on success, FALSE on error
                    # (such as invalid parameters)
                    DTM_SETRANGE = DTM_FIRST + 4


                    def DateTime_SetRange(hdp, gd, rgst):
                        return BOOLSNDMSG(hdp, DTM_SETRANGE, WPARAMgd, LPARAMrgst)

                    # BOOL DateTime_SetFormat(HWND hdp, LPCTSTR sz)

                    # sets the display formatting string to sz
                    # (see GetDateFormat and GetTimeFormat for valid formatting CHARs)
                    #

                    # NOTE: 'X' is a valid formatting CHARacter which
                    # indicates that the application

                    # will determine how to display information. Such apps
                    # must support DTN_WMKEYDOWN,

                    # DTN_FORMAT, and DTN_FORMATQUERY.
                    DTM_SETFORMATA = DTM_FIRST + 5
                    DTM_SETFORMATW = DTM_FIRST + 50

                    if defined(UNICODE):
                        DTM_SETFORMAT = DTM_SETFORMATW
                    else:
                        DTM_SETFORMAT = DTM_SETFORMATA
                    # END IF


                    def DateTime_SetFormat(hdp, sz):
                        return BOOLSNDMSG(hdp, DTM_SETFORMAT, 0, LPARAMsz)
                    DTM_SETMCCOLOR = DTM_FIRST + 6


                    def DateTime_SetMonthCalColor(hdp, iColor, clr):
                        return SNDMSGhdp, DTM_SETMCCOLOR, iColor, clr
                    DTM_GETMCCOLOR = DTM_FIRST + 7


                    def DateTime_GetMonthCalColor(hdp, iColor):
                        return SNDMSGhdp, DTM_GETMCCOLOR, iColor, 0

                    # HWND DateTime_GetMonthCal(HWND hdp)

                    # returns the HWND of the MonthCal popup window. Only valid

                    # between DTN_DROPDOWN and DTN_CLOSEUP notifications.
                    DTM_GETMONTHCAL = DTM_FIRST + 8


                    def DateTime_GetMonthCal(hdp):
                        return HWNDSNDMSGhdp, DTM_GETMONTHCAL, 0, 0
                    DTM_SETMCFONT = DTM_FIRST + 9


                    def DateTime_SetMonthCalFont(hdp, hfont, fRedraw):
                        return SNDMSG(hdp, DTM_SETMCFONT, WPARAMhfont, LPARAMfRedraw)
                    DTM_GETMCFONT = DTM_FIRST + 10


                    def DateTime_GetMonthCalFont(hdp):
                        return SNDMSGhdp, DTM_GETMCFONT, 0, 0

                    if NTDDI_VERSION >= NTDDI_VISTA:
                        DTM_SETMCSTYLE = DTM_FIRST + 11


                        def DateTime_SetMonthCalStyle(hdp, dwStyle):
                            return SNDMSG(hdp, DTM_SETMCSTYLE, 0, LPARAMdwStyle)
                        DTM_GETMCSTYLE = DTM_FIRST + 12


                        def DateTime_GetMonthCalStyle(hdp):
                            return SNDMSGhdp, DTM_GETMCSTYLE, 0, 0
                        DTM_CLOSEMONTHCAL = DTM_FIRST + 13


                        def DateTime_CloseMonthCal(hdp):
                            return SNDMSGhdp, DTM_CLOSEMONTHCAL, 0, 0

                        # DateTime_GetDateTimePickerInfo(HWND hdp, DATETIMEPICKERINFO* pdtpi)
                        #

                        # Retrieves information about the selected date time
                        # picker.
                        DTM_GETDATETIMEPICKERINFO = DTM_FIRST + 14


                        def DateTime_GetDateTimePickerInfo(hdp, pdtpi):
                            return SNDMSG(hdp, DTM_GETDATETIMEPICKERINFO, 0, LPARAMpdtpi)
                        DTM_GETIDEALSIZE = DTM_FIRST + 15


                        def DateTime_GetIdealSize(hdp, psize):
                            return BOOLSNDMSGhdp, DTM_GETIDEALSIZE, 0, LPARAMpsize
                    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                    # begin_r_commctrl
                    DTS_UPDOWN = 0x0001
                    DTS_SHOWNONE = 0x0002
                    DTS_SHORTDATEFORMAT = 0x0000
                    DTS_LONGDATEFORMAT = 0x0004
                    DTS_SHORTDATECENTURYFORMAT = 0x000C
                    DTS_TIMEFORMAT = 0x0009
                    DTS_APPCANPARSE = 0x0010
                    DTS_RIGHTALIGN = 0x0020

                    # end_r_commctrl
                    DTN_DATETIMECHANGE = DTN_FIRST2 - 6
                    class tagNMDATETIMECHANGE(ctypes.Structure):
                        pass


                    tagNMDATETIMECHANGE._fields_ = [
                        ('nmhdr', NMHDR),
                        ('dwFlags', DWORD), # GDT_VALID or GDT_NONE
                        ('st', SYSTEMTIME), # valid iff dwFlags == GDT_VALID
                    ]
                    NMDATETIMECHANGE = tagNMDATETIMECHANGE
                    LPNMDATETIMECHANGE = POINTER(tagNMDATETIMECHANGE)
                    DTN_USERSTRINGA = DTN_FIRST2 - 5
                    DTN_USERSTRINGW = DTN_FIRST - 5
                    class tagNMDATETIMESTRINGA(ctypes.Structure):
                        pass


                    tagNMDATETIMESTRINGA._fields_ = [
                        ('nmhdr', NMHDR),
                        ('pszUserString', LPCSTR), # string user entered
                        ('st', SYSTEMTIME), # app fills this in
                        ('dwFlags', DWORD), # GDT_VALID or GDT_NONE
                    ]
                    NMDATETIMESTRINGA = tagNMDATETIMESTRINGA
                    LPNMDATETIMESTRINGA = POINTER(tagNMDATETIMESTRINGA)
                    class tagNMDATETIMESTRINGW(ctypes.Structure):
                        pass


                    tagNMDATETIMESTRINGW._fields_ = [
                        ('nmhdr', NMHDR),
                        ('pszUserString', LPCWSTR), # string user entered
                        ('st', SYSTEMTIME), # app fills this in
                        ('dwFlags', DWORD), # GDT_VALID or GDT_NONE
                    ]
                    NMDATETIMESTRINGW = tagNMDATETIMESTRINGW
                    LPNMDATETIMESTRINGW = POINTER(tagNMDATETIMESTRINGW)

                    if defined(UNICODE):
                        DTN_USERSTRING = DTN_USERSTRINGW
                        NMDATETIMESTRING = NMDATETIMESTRINGW
                        LPNMDATETIMESTRING = LPNMDATETIMESTRINGW
                    else:
                        DTN_USERSTRING = DTN_USERSTRINGA
                        NMDATETIMESTRING = NMDATETIMESTRINGA
                        LPNMDATETIMESTRING = LPNMDATETIMESTRINGA
                    # END IF
                    DTN_WMKEYDOWNA = DTN_FIRST2 - 4
                    DTN_WMKEYDOWNW = DTN_FIRST - 4
                    class tagNMDATETIMEWMKEYDOWNA(ctypes.Structure):
                        pass


                    tagNMDATETIMEWMKEYDOWNA._fields_ = [
                        ('nmhdr', NMHDR),

                        # virtual key code of WM_KEYDOWN which MODIFIES an X
                        # field
                        ('nVirtKey', INT),
                        ('pszFormat', LPCSTR), # format substring
                        ('st', SYSTEMTIME), # current systemtime, app should modify based on key
                    ]
                    NMDATETIMEWMKEYDOWNA = tagNMDATETIMEWMKEYDOWNA
                    LPNMDATETIMEWMKEYDOWNA = POINTER(tagNMDATETIMEWMKEYDOWNA)
                    class tagNMDATETIMEWMKEYDOWNW(ctypes.Structure):
                        pass


                    tagNMDATETIMEWMKEYDOWNW._fields_ = [
                        ('nmhdr', NMHDR),

                        # virtual key code of WM_KEYDOWN which MODIFIES an X
                        # field
                        ('nVirtKey', INT),
                        ('pszFormat', LPCWSTR), # format substring
                        ('st', SYSTEMTIME), # current systemtime, app should modify based on key
                    ]
                    NMDATETIMEWMKEYDOWNW = tagNMDATETIMEWMKEYDOWNW
                    LPNMDATETIMEWMKEYDOWNW = POINTER(tagNMDATETIMEWMKEYDOWNW)

                    if defined(UNICODE):
                        DTN_WMKEYDOWN = DTN_WMKEYDOWNW
                        NMDATETIMEWMKEYDOWN = NMDATETIMEWMKEYDOWNW
                        LPNMDATETIMEWMKEYDOWN = LPNMDATETIMEWMKEYDOWNW
                    else:
                        DTN_WMKEYDOWN = DTN_WMKEYDOWNA
                        NMDATETIMEWMKEYDOWN = NMDATETIMEWMKEYDOWNA
                        LPNMDATETIMEWMKEYDOWN = LPNMDATETIMEWMKEYDOWNA
                    # END IF
                    DTN_FORMATA = DTN_FIRST2 - 3
                    DTN_FORMATW = DTN_FIRST - 3
                    class tagNMDATETIMEFORMATA(ctypes.Structure):
                        pass


                    tagNMDATETIMEFORMATA._fields_ = [
                        ('nmhdr', NMHDR),
                        ('pszFormat', LPCSTR), # format substring
                        ('st', SYSTEMTIME), # current systemtime
                        ('pszDisplay', LPCSTR), # string to display
                        ('szDisplay', CHAR * 64), # buffer pszDisplay originally points at
                    ]
                    NMDATETIMEFORMATA = tagNMDATETIMEFORMATA
                    LPNMDATETIMEFORMATA = POINTER(tagNMDATETIMEFORMATA)
                    class tagNMDATETIMEFORMATW(ctypes.Structure):
                        pass


                    tagNMDATETIMEFORMATW._fields_ = [
                        ('nmhdr', NMHDR),
                        ('pszFormat', LPCWSTR), # format substring
                        ('st', SYSTEMTIME), # current systemtime
                        ('pszDisplay', LPCWSTR), # string to display
                        ('szDisplay', WCHAR * 64), # buffer pszDisplay originally points at
                    ]
                    NMDATETIMEFORMATW = tagNMDATETIMEFORMATW
                    LPNMDATETIMEFORMATW = POINTER(tagNMDATETIMEFORMATW)

                    if defined(UNICODE):
                        DTN_FORMAT = DTN_FORMATW
                        NMDATETIMEFORMAT = NMDATETIMEFORMATW
                        LPNMDATETIMEFORMAT = LPNMDATETIMEFORMATW
                    else:
                        DTN_FORMAT = DTN_FORMATA
                        NMDATETIMEFORMAT = NMDATETIMEFORMATA
                        LPNMDATETIMEFORMAT = LPNMDATETIMEFORMATA
                    # END IF
                    DTN_FORMATQUERYA = DTN_FIRST2 - 2
                    DTN_FORMATQUERYW = DTN_FIRST - 2
                    class tagNMDATETIMEFORMATQUERYA(ctypes.Structure):
                        pass


                    tagNMDATETIMEFORMATQUERYA._fields_ = [
                        ('nmhdr', NMHDR),
                        ('pszFormat', LPCSTR), # format substring

                        # max bounding rectangle app will use for this format
                        # string
                        ('szMax', SIZE),
                    ]
                    NMDATETIMEFORMATQUERYA = tagNMDATETIMEFORMATQUERYA
                    LPNMDATETIMEFORMATQUERYA = POINTER(tagNMDATETIMEFORMATQUERYA)
                    class tagNMDATETIMEFORMATQUERYW(ctypes.Structure):
                        pass


                    tagNMDATETIMEFORMATQUERYW._fields_ = [
                        ('nmhdr', NMHDR),
                        ('pszFormat', LPCWSTR), # format substring

                        # max bounding rectangle app will use for this format
                        # string
                        ('szMax', SIZE),
                    ]
                    NMDATETIMEFORMATQUERYW = tagNMDATETIMEFORMATQUERYW
                    LPNMDATETIMEFORMATQUERYW = POINTER(tagNMDATETIMEFORMATQUERYW)

                    if defined(UNICODE):
                        DTN_FORMATQUERY = DTN_FORMATQUERYW
                        NMDATETIMEFORMATQUERY = NMDATETIMEFORMATQUERYW
                        LPNMDATETIMEFORMATQUERY = LPNMDATETIMEFORMATQUERYW
                    else:
                        DTN_FORMATQUERY = DTN_FORMATQUERYA
                        NMDATETIMEFORMATQUERY = NMDATETIMEFORMATQUERYA
                        LPNMDATETIMEFORMATQUERY = LPNMDATETIMEFORMATQUERYA
                    # END IF
                    DTN_DROPDOWN = DTN_FIRST2 - 1
                    DTN_CLOSEUP = DTN_FIRST2
                    GDTR_MIN = 0x0001
                    GDTR_MAX = 0x0002
                    GDT_ERROR = - 1
                    GDT_VALID = 0
                    GDT_NONE = 1
                # END IF   _WIN32
            # END IF   NODATETIMEPICK

            if not defined(NOIPADDRESS):

                # /////////////////////////////////////////////

                # IP Address edit control

                # Messages sent to IPAddress controls
                IPM_CLEARADDRESS = WM_USER + 100
                IPM_SETADDRESS = WM_USER + 101
                IPM_GETADDRESS = WM_USER + 102
                IPM_SETRANGE = WM_USER + 103
                IPM_SETFOCUS = WM_USER + 104
                IPM_ISBLANK = WM_USER + 105
                WC_IPADDRESSW = "SysIPAddress32"
                WC_IPADDRESSA = "SysIPAddress32"

                if defined(UNICODE):
                    WC_IPADDRESS = WC_IPADDRESSW
                else:
                    WC_IPADDRESS = WC_IPADDRESSA
                # END IF
                IPN_FIELDCHANGED = IPN_FIRST - 0
                class tagNMIPADDRESS(ctypes.Structure):
                    pass


                tagNMIPADDRESS._fields_ = [
                    ('hdr', NMHDR),
                    ('iField', INT),
                    ('iValue', INT),
                ]
                NMIPADDRESS = tagNMIPADDRESS
                LPNMIPADDRESS = POINTER(tagNMIPADDRESS)

                # The following is a useful macro for passing the range values
                # in the

                # IPM_SETRANGE message.


                def MAKEIPRANGE(low, high):
                    return (LPARAMWORD((BYTEhigh << 8) + BYTElow))

                # And this is a useful macro for making the IP Address to be
                # passed

                # as a LPARAM.


                def MAKEIPADDRESS(b1, b2, b3, b4):
                    return (LPARAM((DWORDb1 << 24) + (DWORDb2 << 16) + (DWORDb3 << 8) + (DWORDb4)))

                # Get individual number


                def FIRST_IPADDRESS(x):
                    return ((x >> 24) & 0xFF)


                def SECOND_IPADDRESS(x):
                    return ((x >> 16) & 0xFF)


                def THIRD_IPADDRESS(x):
                    return ((x >> 8) & 0xFF)


                def FOURTH_IPADDRESS(x):
                    return (x & 0xFF)
            # END IF   NOIPADDRESS

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - - - - - - - - - - -

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - - - - - - - - - - -

            # == == == == == == == == == == == Pager Control == == == == == ==
            # == == == == == == == == =

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - - - - - - - - - - -

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # - - - - - - - - - - - - - - - - - - - - - - -

            if not defined(NOPAGESCROLLER):

                # Pager Class Name
                WC_PAGESCROLLERW = "SysPager"
                WC_PAGESCROLLERA = "SysPager"

                if defined(UNICODE):
                    WC_PAGESCROLLER = WC_PAGESCROLLERW
                else:
                    WC_PAGESCROLLER = WC_PAGESCROLLERA
                # END IF

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # Pager Control Styles

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # begin_r_commctrl
                PGS_VERT = 0x00000000
                PGS_HORZ = 0x00000001
                PGS_AUTOSCROLL = 0x00000002
                PGS_DRAGNDROP = 0x00000004

                # end_r_commctrl

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # Pager Button State

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # The scroll can be in one of the following control State
                PGF_INVISIBLE = 0
                PGF_NORMAL = 1
                PGF_GRAYED = 2
                PGF_DEPRESSED = 4
                PGF_HOT = 8

                # The following identifiers specifies the button control
                PGB_TOPORLEFT = 0
                PGB_BOTTOMORRIGHT = 1

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # Pager Control Messages

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -
                PGM_SETCHILD = PGM_FIRST + 1


                def Pager_SetChild(hwnd, hwndChild):
                    return VOIDSNDMSGhwnd, PGM_SETCHILD, 0, LPARAMhwndChild
                PGM_RECALCSIZE = PGM_FIRST + 2


                def Pager_RecalcSize(hwnd):
                    return VOIDSNDMSG(hwnd, PGM_RECALCSIZE, 0, 0)
                PGM_FORWARDMOUSE = PGM_FIRST + 3


                def Pager_ForwardMouse(hwnd, bForward):
                    return VOIDSNDMSG(hwnd, PGM_FORWARDMOUSE, WPARAMbForward, 0)
                PGM_SETBKCOLOR = PGM_FIRST + 4


                def Pager_SetBkColor(hwnd, clr):
                    return COLORREFSNDMSGhwnd, PGM_SETBKCOLOR, 0, LPARAMclr
                PGM_GETBKCOLOR = PGM_FIRST + 5


                def Pager_GetBkColor(hwnd):
                    return COLORREFSNDMSG(hwnd, PGM_GETBKCOLOR, 0, 0)
                PGM_SETBORDER = PGM_FIRST + 6


                def Pager_SetBorder(hwnd, iBorder):
                    return INTSNDMSGhwnd, PGM_SETBORDER, 0, LPARAMiBorder
                PGM_GETBORDER = PGM_FIRST + 7


                def Pager_GetBorder(hwnd):
                    return INTSNDMSG(hwnd, PGM_GETBORDER, 0, 0)
                PGM_SETPOS = PGM_FIRST + 8


                def Pager_SetPos(hwnd, iPos):
                    return INTSNDMSGhwnd, PGM_SETPOS, 0, LPARAMiPos
                PGM_GETPOS = PGM_FIRST + 9


                def Pager_GetPos(hwnd):
                    return INTSNDMSG(hwnd, PGM_GETPOS, 0, 0)
                PGM_SETBUTTONSIZE = PGM_FIRST + 10


                def Pager_SetButtonSize(hwnd, iSize):
                    return INTSNDMSGhwnd, PGM_SETBUTTONSIZE, 0, LPARAMiSize
                PGM_GETBUTTONSIZE = PGM_FIRST + 11


                def Pager_GetButtonSize(hwnd):
                    return INTSNDMSG(hwnd, PGM_GETBUTTONSIZE, 0,0)
                PGM_GETBUTTONSTATE = PGM_FIRST + 12


                def Pager_GetButtonState(hwnd, iButton):
                    return DWORDSNDMSGhwnd, PGM_GETBUTTONSTATE, 0, LPARAMiButton
                PGM_GETDROPTARGET = CCM_GETDROPTARGET


                def Pager_GetDropTarget(hwnd, ppdt):
                    return VOIDSNDMSGhwnd, PGM_GETDROPTARGET, 0, LPARAMppdt
                PGM_SETSCROLLINFO = PGM_FIRST + 13


                def Pager_SetScrollInfo(hwnd, cTimeOut, cLinesPer, cPixelsPerLine):
                    return VOID SNDMSGhwnd, PGM_SETSCROLLINFO, cTimeOut, MAKELONGcLinesPer, cPixelsPerLine

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # Pager Control Notification Messages

                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                # - - - - - - - - - - - - - - - - - - - - - - - - - - -

                # PGN_SCROLL Notification Message
                PGN_SCROLL = PGN_FIRST - 1
                PGF_SCROLLUP = 1
                PGF_SCROLLDOWN = 2
                PGF_SCROLLLEFT = 4
                PGF_SCROLLRIGHT = 8

                # Keys down
                PGK_SHIFT = 1
                PGK_CONTROL = 2
                PGK_MENU = 4

                if defined(_WIN32):
                    pass
                # END IF

                # This structure is sent aLONG with PGN_SCROLL notifications
                class NMPGSCROLL(ctypes.Structure):
                    pass


                NMPGSCROLL._fields_ = [
                    ('hdr', NMHDR),

                    # Specifies which keys are down when this notification is
                    # send
                    ('fwKeys', WORD),
                    ('rcParent', RECT), # Contains Parent Window Rect
                    ('iDir', INT), # Scrolling Direction
                    ('iXpos', INT), # Horizontal scroll position
                    ('iYpos', INT), # Vertical scroll position
                    ('iScroll', INT), # [in/out] Amount to scroll
                ]
                LPNMPGSCROLL = POINTER(NMPGSCROLL)
                if defined(_WIN32):
                    pass
                # END IF

                # PGN_CALCSIZE Notification Message
                PGN_CALCSIZE = PGN_FIRST - 2
                PGF_CALCWIDTH = 1
                PGF_CALCHEIGHT = 2
                class NMPGCALCSIZE(ctypes.Structure):
                    pass


                NMPGCALCSIZE._fields_ = [
                    ('hdr', NMHDR),
                    ('dwFlag', DWORD),
                    ('iWidth', INT),
                    ('iHeight', INT),
                ]
                LPNMPGCALCSIZE = POINTER(NMPGCALCSIZE)

                # PGN_HOTITEMCHANGE Notification Message
                PGN_HOTITEMCHANGE = PGN_FIRST - 3

                # The PGN_HOTITEMCHANGE notification uses these notification
                # flags defined in TOOLBAR: define HICF_ENTERING 0x00000010 //
                # idOld is invalid define HICF_LEAVING 0x00000020 // idNew is
                # invalid

                # Structure for PGN_HOTITEMCHANGE notification
                class tagNMPGHOTITEM(ctypes.Structure):
                    pass


                tagNMPGHOTITEM._fields_ = [
                    ('hdr', NMHDR),
                    ('idOld', INT),
                    ('idNew', INT),
                    ('dwFlags', DWORD), # HICF_*
                ]
                NMPGHOTITEM = tagNMPGHOTITEM
                 LPNMPGHOTITEM = POINTER(tagNMPGHOTITEM)
            # END IF   NOPAGESCROLLER

            # // == == == == == == == == == == == End Pager Control == == ==
            # == == == == == == == == == == == == == == == == == ==

            # == = Native Font Control == =

            if not defined(NONATIVEFONTCTL):

                # NativeFont Class Name
                WC_NATIVEFONTCTLW = "NativeFontCtl"
                WC_NATIVEFONTCTLA = "NativeFontCtl"

                if defined(UNICODE):
                    WC_NATIVEFONTCTL = WC_NATIVEFONTCTLW
                else:
                    WC_NATIVEFONTCTL = WC_NATIVEFONTCTLA
                # END IF

                # begin_r_commctrl

                # style definition
                NFS_EDIT = 0x0001
                NFS_STATIC = 0x0002
                NFS_LISTCOMBO = 0x0004
                NFS_BUTTON = 0x0008
                NFS_ALL = 0x0010
                NFS_USEFONTASSOC = 0x0020

                # end_r_commctrl
            # END IF   NONATIVEFONTCTL

            # == = End Native Font Control == =

            # == == == == == == == == == == == Button Control == == == == ==
            # == == == == == == == == == =

            if not defined(NOBUTTON):
                if defined(_WIN32):

                    # Button Class Name
                    WC_BUTTONA = "Button"
                    WC_BUTTONW = "Button"

                    if defined(UNICODE):
                        WC_BUTTON = WC_BUTTONW
                    else:
                        WC_BUTTON = WC_BUTTONA
                    # END IF
                else:
                    WC_BUTTON = "Button"
                # END IF

                if NTDDI_VERSION >= NTDDI_WINXP:
                    BUTTON_IMAGELIST_ALIGN_LEFT = 0
                    BUTTON_IMAGELIST_ALIGN_RIGHT = 1
                    BUTTON_IMAGELIST_ALIGN_TOP = 2
                    BUTTON_IMAGELIST_ALIGN_BOTTOM = 3
                    BUTTON_IMAGELIST_ALIGN_CENTER = 4
                    class BUTTON_IMAGELIST(ctypes.Structure):
                        pass


                    BUTTON_IMAGELIST._fields_ = [

                        # Images: Normal, Hot, Pushed, Disabled. If count is
                        # less than 4, we use index 1
                        ('himl', HIMAGELIST),
                        ('margin', RECT), # Margin around icon.
                        ('uAlign', UINT),
                    ]
                    PBUTTON_IMAGELIST = POINTER(BUTTON_IMAGELIST)
                    BCM_GETIDEALSIZE = BCM_FIRST + 0x0001


                    def Button_GetIdealSize(hwnd, psize):
                        return BOOLSNDMSGhwnd, BCM_GETIDEALSIZE, 0, LPARAMpsize
                    BCM_SETIMAGELIST = BCM_FIRST + 0x0002


                    def Button_SetImageList(hwnd, pbuttonImagelist):
                        return BOOLSNDMSGhwnd, BCM_SETIMAGELIST, 0, LPARAMpbuttonImagelist
                    BCM_GETIMAGELIST = BCM_FIRST + 0x0003


                    def Button_GetImageList(hwnd, pbuttonImagelist):
                        return BOOLSNDMSGhwnd, BCM_GETIMAGELIST, 0, LPARAMpbuttonImagelist
                    BCM_SETTEXTMARGIN = BCM_FIRST + 0x0004


                    def Button_SetTextMargin(hwnd, pmargin):
                        return BOOLSNDMSGhwnd, BCM_SETTEXTMARGIN, 0, LPARAMpmargin
                    BCM_GETTEXTMARGIN = BCM_FIRST + 0x0005


                    def Button_GetTextMargin(hwnd, pmargin):
                        return BOOLSNDMSGhwnd, BCM_GETTEXTMARGIN, 0, LPARAMpmargin
                    class tagNMBCHOTITEM(ctypes.Structure):
                        pass


                    tagNMBCHOTITEM._fields_ = [
                        ('hdr', NMHDR),
                        ('dwFlags', DWORD), # HICF_*
                    ]
                    NMBCHOTITEM = tagNMBCHOTITEM
                     LPNMBCHOTITEM = POINTER(tagNMBCHOTITEM)
                    BCN_HOTITEMCHANGE = BCN_FIRST + 0x0001
                    BST_HOT = 0x0200
                # END IF   (NTDDI_VERSION >= NTDDI_WINXP)

                if NTDDI_VERSION >= NTDDI_VISTA:

                    # BUTTON STATE FLAGS
                    BST_DROPDOWNPUSHED = 0x0400

                    # begin_r_commctrl

                    # BUTTON STYLES
                    BS_SPLITBUTTON = 0x0000000C
                    BS_DEFSPLITBUTTON = 0x0000000D
                    BS_COMMANDLINK = 0x0000000E
                    BS_DEFCOMMANDLINK = 0x0000000F

                    # SPLIT BUTTON INFO mask flags
                    BCSIF_GLYPH = 0x0001
                    BCSIF_IMAGE = 0x0002
                    BCSIF_STYLE = 0x0004
                    BCSIF_SIZE = 0x0008

                    # SPLIT BUTTON STYLE flags
                    BCSS_NOSPLIT = 0x0001
                    BCSS_STRETCH = 0x0002
                    BCSS_ALIGNLEFT = 0x0004
                    BCSS_IMAGE = 0x0008

                    # end_r_commctrl

                    # BUTTON STRUCTURES
                    class tagBUTTON_SPLITINFO(ctypes.Structure):
                        pass


                    tagBUTTON_SPLITINFO._fields_ = [
                        ('mask', UINT),
                        ('himlGlyph', HIMAGELIST), # interpreted as WCHAR if BCSIF_GLYPH is set
                        ('uSplitStyle', UINT),
                        ('size', SIZE),
                    ]
                    BUTTON_SPLITINFO = tagBUTTON_SPLITINFO
                     PBUTTON_SPLITINFO = POINTER(tagBUTTON_SPLITINFO)

                    # BUTTON MESSAGES
                    BCM_SETDROPDOWNSTATE = BCM_FIRST + 0x0006


                    def Button_SetDropDownState(hwnd, fDropDown):
                        return BOOLSNDMSG(hwnd, BCM_SETDROPDOWNSTATE, WPARAMfDropDown, 0)
                    BCM_SETSPLITINFO = BCM_FIRST + 0x0007


                    def Button_SetSplitInfo(hwnd, pInfo):
                        return BOOLSNDMSGhwnd, BCM_SETSPLITINFO, 0, LPARAMpInfo
                    BCM_GETSPLITINFO = BCM_FIRST + 0x0008


                    def Button_GetSplitInfo(hwnd, pInfo):
                        return BOOLSNDMSGhwnd, BCM_GETSPLITINFO, 0, LPARAMpInfo
                    BCM_SETNOTE = BCM_FIRST + 0x0009


                    def Button_SetNote(hwnd, psz):
                        return BOOLSNDMSGhwnd, BCM_SETNOTE, 0, LPARAMpsz
                    BCM_GETNOTE = BCM_FIRST + 0x000A


                    def Button_GetNote(hwnd, psz, pcc):
                        return BOOLSNDMSG(hwnd, BCM_GETNOTE, WPARAMpcc, LPARAMpsz)
                    BCM_GETNOTELENGTH = BCM_FIRST + 0x000B


                    def Button_GetNoteLength(hwnd):
                        return LRESULTSNDMSG(hwnd, BCM_GETNOTELENGTH, 0, 0)

                    if NTDDI_VERSION >= NTDDI_VISTA:

                        # Macro to use on a button or command link to display
                        # an elevated icon
                        BCM_SETSHIELD = BCM_FIRST + 0x000C


                        def Button_SetElevationRequiredState(hwnd, fRequired):
                            return LRESULTSNDMSG(hwnd, BCM_SETSHIELD, 0, LPARAMfRequired)
                    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                    # Value to pass to BCM_SETIMAGELIST to indicate that no
                    # glyph should be

                    # displayed
                    BCCL_NOGLYPH = HIMAGELIST)( - 1

                    # NOTIFICATION MESSAGES
                    class tagNMBCDROPDOWN(ctypes.Structure):
                        pass


                    tagNMBCDROPDOWN._fields_ = [
                        ('hdr', NMHDR),
                        ('rcButton', RECT),
                    ]
                    NMBCDROPDOWN = tagNMBCDROPDOWN
                     LPNMBCDROPDOWN = POINTER(tagNMBCDROPDOWN)
                    BCN_DROPDOWN = BCN_FIRST + 0x0002
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
            # END IF   NOBUTTON

            # == == == == == == == == == == = End Button Control == == == ==
            # == == == == == == == == =

            # == == == == == == == == == == == Static Control == == == == ==
            # == == == == == == == == == =

            if not defined(NOSTATIC):
                if defined(_WIN32):

                    # Static Class Name
                    WC_STATICA = "Static"
                    WC_STATICW = "Static"

                    if defined(UNICODE):
                        WC_STATIC = WC_STATICW
                    else:
                        WC_STATIC = WC_STATICA
                    # END IF
                else:
                    WC_STATIC = "Static"
                # END IF
            # END IF   NOSTATIC

            # == == == == == == == == == == = End Static Control == == == ==
            # == == == == == == == == =

            # == == == == == == == == == == == Edit Control == == == == == ==
            # == == == == == == == == =

            if not defined(NOEDIT):
                if defined(_WIN32):

                    # Edit Class Name
                    WC_EDITA = "Edit"
                    WC_EDITW = "Edit"

                    if defined(UNICODE):
                        WC_EDIT = WC_EDITW
                    else:
                        WC_EDIT = WC_EDITA
                    # END IF
                else:
                    WC_EDIT = "Edit"
                # END IF

                if NTDDI_VERSION >= NTDDI_WINXP:
                    EM_SETCUEBANNER = ECM_FIRST + 1


                    def Edit_SetCueBannerText(hwnd, lpcwText):
                        return BOOLSNDMSGhwnd, EM_SETCUEBANNER, 0, LPARAMlpcwText


                    def Edit_SetCueBannerTextFocused(hwnd, lpcwText, fDrawFocused):
                        return BOOLSNDMSG(hwnd, EM_SETCUEBANNER, WPARAMfDrawFocused, LPARAMlpcwText)
                    EM_GETCUEBANNER = ECM_FIRST + 2


                    def Edit_GetCueBannerText(hwnd, lpwText, cchText):
                        return BOOLSNDMSGhwnd, EM_GETCUEBANNER, WPARAMlpwText, LPARAMcchText
                    class _tagEDITBALLOONTIP(ctypes.Structure):
                        pass


                    _tagEDITBALLOONTIP._fields_ = [
                        ('cbStruct', DWORD),
                        ('pszTitle', LPCWSTR),
                        ('pszText', LPCWSTR),
                        ('ttiIcon', INT), # From TTI_*
                    ]
                    EDITBALLOONTIP = _tagEDITBALLOONTIP
                    PEDITBALLOONTIP = POINTER(_tagEDITBALLOONTIP)
                    EM_SHOWBALLOONTIP = ECM_FIRST + 3


                    def Edit_ShowBalloonTip(hwnd, peditballoontip):
                        return BOOLSNDMSGhwnd, EM_SHOWBALLOONTIP, 0, LPARAMpeditballoontip
                    EM_HIDEBALLOONTIP = ECM_FIRST + 4


                    def Edit_HideBalloonTip(hwnd):
                        return BOOLSNDMSG(hwnd, EM_HIDEBALLOONTIP, 0, 0)
                # END IF

                if NTDDI_VERSION >= NTDDI_VISTA:
                    EM_SETHILITE = ECM_FIRST + 5


                    def Edit_SetHilite(hwndCtl, ichStart, ichEnd):
                        return (VOIDSNDMSG(hwndCtl, EM_SETHILITE, ichStart, ichEnd))
                    EM_GETHILITE = ECM_FIRST + 6


                    def Edit_GetHilite(hwndCtl):
                        return DWORDSNDMSG(hwndCtl, EM_GETHILITE, 0L, 0L)
                # END IF
                EM_NOSETFOCUS = ECM_FIRST + 7


                def Edit_NoSetFocus(hwndCtl):
                    return DWORDSNDMSG(hwndCtl, EM_NOSETFOCUS, 0L, 0L)
                EM_TAKEFOCUS = ECM_FIRST + 8


                def Edit_TakeFocus(hwndCtl):
                    return DWORDSNDMSG(hwndCtl, EM_TAKEFOCUS, 0L, 0L)
            # END IF   NOEDIT

            # == == == == == == == == == == = End Edit Control == == == == ==
            # == == == == == == == =

            # == == == == == == == == == == == Listbox Control == == == == ==
            # == == == == == == == == == =

            if not defined(NOLISTBOX):
                if defined(_WIN32):

                    # Listbox Class Name
                    WC_LISTBOXA = "ListBox"
                    WC_LISTBOXW = "ListBox"

                    if defined(UNICODE):
                        WC_LISTBOX = WC_LISTBOXW
                    else:
                        WC_LISTBOX = WC_LISTBOXA
                    # END IF
                else:
                    WC_LISTBOX = "ListBox"
                # END IF
            # END IF   NOLISTBOX

            # == == == == == == == == == == = End Listbox Control == == == ==
            # == == == == == == == == =

            # == == == == == == == == == == == Combobox Control == == == == ==
            # == == == == == == == == == =

            if not defined(NOCOMBOBOX):
                if defined(_WIN32):

                    # Combobox Class Name
                    WC_COMBOBOXA = "ComboBox"
                    WC_COMBOBOXW = "ComboBox"

                    if defined(UNICODE):
                        WC_COMBOBOX = WC_COMBOBOXW
                    else:
                        WC_COMBOBOX = WC_COMBOBOXA
                    # END IF
                else:
                    WC_COMBOBOX = "ComboBox"
                # END IF
            # END IF   NOCOMBOBOX

            if NTDDI_VERSION >= NTDDI_WINXP:

                # custom combobox control messages
                CB_SETMINVISIBLE = CBM_FIRST + 1
                CB_GETMINVISIBLE = CBM_FIRST + 2
                CB_SETCUEBANNER = CBM_FIRST + 3
                CB_GETCUEBANNER = CBM_FIRST + 4


                def ComboBox_SetMinVisible(hwnd, iMinVisible):
                    return BOOLSNDMSG(hwnd, CB_SETMINVISIBLE, WPARAMiMinVisible, 0)


                def ComboBox_GetMinVisible(hwnd):
                    return INTSNDMSG(hwnd, CB_GETMINVISIBLE, 0, 0)


                def ComboBox_SetCueBannerText(hwnd, lpcwText):
                    return BOOLSNDMSGhwnd, CB_SETCUEBANNER, 0, LPARAMlpcwText


                def ComboBox_GetCueBannerText(hwnd, lpwText, cchText):
                    return BOOLSNDMSGhwnd, CB_GETCUEBANNER, WPARAMlpwText, LPARAMcchText
            # END IF

            # == == == == == == == == == == = End Combobox Control == == == ==
            # == == == == == == == == =

            # == == == == == == == == == == == Scrollbar Control == == == ==
            # == == == == == == == == == ==

            if not defined(NOSCROLLBAR):
                if defined(_WIN32):

                    # Scrollbar Class Name
                    WC_SCROLLBARA = "ScrollBar"
                    WC_SCROLLBARW = "ScrollBar"

                    if defined(UNICODE):
                        WC_SCROLLBAR = WC_SCROLLBARW
                    else:
                        WC_SCROLLBAR = WC_SCROLLBARA
                    # END IF
                else:
                    WC_SCROLLBAR = "ScrollBar"
                # END IF
            # END IF   NOSCROLLBAR

            # == == == == == == == == == == = End Scrollbar Control == == ==
            # == == == == == == == == == =

            # == == == == == == == == == == = Task Dialog == == == == == == ==
            # == == == == == =

            if not defined(NOTASKDIALOG):

                # Task Dialog is only available starting Windows Vista
                    if defined(_WIN32):
                        pass
                    # END IF
                if NTDDI_VERSION >= NTDDI_VISTA:
                    (CALLBACK = HRESULT
                    PFTASKDIALOGCALLBACK)(_In_ = POINTER(HRESULT)
                    HWND = HRESULT
                    hwnd = HRESULT
                    _In_ = HRESULT
                    UINT = HRESULT
                    msg = HRESULT
                    _In_ = HRESULT
                    WPARAM = HRESULT
                    wParam = HRESULT
                    _In_ = HRESULT
                    LPARAM = HRESULT
                    lParam = HRESULT
                    _In_ = HRESULT
                    LONG_PTR = HRESULT
                    lpRefData) = HRESULT
                    class _TASKDIALOG_FLAGS(ENUM):
                        TDF_ENABLE_HYPERLINKS = 0x0001
                        TDF_USE_HICON_MAIN = 0x0002
                        TDF_USE_HICON_FOOTER = 0x0004
                        TDF_ALLOW_DIALOG_CANCELLATION = 0x0008
                        TDF_USE_COMMAND_LINKS = 0x0010
                        TDF_USE_COMMAND_LINKS_NO_ICON = 0x0020
                        TDF_EXPAND_FOOTER_AREA = 0x0040
                        TDF_EXPANDED_BY_DEFAULT = 0x0080
                        TDF_VERIFICATION_FLAG_CHECKED = 0x0100
                        TDF_SHOW_PROGRESS_BAR = 0x0200
                        TDF_SHOW_MARQUEE_PROGRESS_BAR = 0x0400
                        TDF_CALLBACK_TIMER = 0x0800
                        TDF_POSITION_RELATIVE_TO_WINDOW = 0x1000
                        TDF_RTL_LAYOUT = 0x2000
                        TDF_NO_DEFAULT_RADIO_BUTTON = 0x4000
                        TDF_CAN_BE_MINIMIZED = 0x8000
                    if NTDDI_VERSION >= NTDDI_WIN8:
                        #~#~#~ if NTDDI_VERSION >= NTDDI_WIN8:

                        # Don't call SetForegroundWindow() when activating the
                        # dialog
                        TDF_NO_SET_FOREGROUND = 0x00010000
                    # END IF

                    # used by ShellMessageBox to emulate MessageBox sizing
                    # behavior
                    TDF_SIZE_TO_CONTENT = 0x01000000


                    TDF_ENABLE_HYPERLINKS = _TASKDIALOG_FLAGS.TDF_ENABLE_HYPERLINKS
                    TDF_USE_HICON_MAIN = _TASKDIALOG_FLAGS.TDF_USE_HICON_MAIN
                    TDF_USE_HICON_FOOTER = _TASKDIALOG_FLAGS.TDF_USE_HICON_FOOTER
                    TDF_ALLOW_DIALOG_CANCELLATION = _TASKDIALOG_FLAGS.TDF_ALLOW_DIALOG_CANCELLATION
                    TDF_USE_COMMAND_LINKS = _TASKDIALOG_FLAGS.TDF_USE_COMMAND_LINKS
                    TDF_USE_COMMAND_LINKS_NO_ICON = _TASKDIALOG_FLAGS.TDF_USE_COMMAND_LINKS_NO_ICON
                    TDF_EXPAND_FOOTER_AREA = _TASKDIALOG_FLAGS.TDF_EXPAND_FOOTER_AREA
                    TDF_EXPANDED_BY_DEFAULT = _TASKDIALOG_FLAGS.TDF_EXPANDED_BY_DEFAULT
                    TDF_VERIFICATION_FLAG_CHECKED = _TASKDIALOG_FLAGS.TDF_VERIFICATION_FLAG_CHECKED
                    TDF_SHOW_PROGRESS_BAR = _TASKDIALOG_FLAGS.TDF_SHOW_PROGRESS_BAR
                    TDF_SHOW_MARQUEE_PROGRESS_BAR = _TASKDIALOG_FLAGS.TDF_SHOW_MARQUEE_PROGRESS_BAR
                    TDF_CALLBACK_TIMER = _TASKDIALOG_FLAGS.TDF_CALLBACK_TIMER
                    TDF_POSITION_RELATIVE_TO_WINDOW = _TASKDIALOG_FLAGS.TDF_POSITION_RELATIVE_TO_WINDOW
                    TDF_RTL_LAYOUT = _TASKDIALOG_FLAGS.TDF_RTL_LAYOUT
                    TDF_NO_DEFAULT_RADIO_BUTTON = _TASKDIALOG_FLAGS.TDF_NO_DEFAULT_RADIO_BUTTON
                    TDF_CAN_BE_MINIMIZED = _TASKDIALOG_FLAGS.TDF_CAN_BE_MINIMIZED
                    TDF_NO_SET_FOREGROUND = _TASKDIALOG_FLAGS.TDF_NO_SET_FOREGROUND
                TDF_SIZE_TO_CONTENT = _TASKDIALOG_FLAGS.TDF_SIZE_TO_CONTENT
                    if NTDDI_VERSION >= NTDDI_WIN8:
                        pass
                    # END IF   (NTDDI_VERSION >= NTDDI_WIN8)
                    TASKDIALOG_FLAGS = INT
                    class _TASKDIALOG_MESSAGES(ENUM):
                        #~#~#~ TDM_NAVIGATE_PAGE                   = WM_USER + 101
                        #~#~#~ TDM_CLICK_BUTTON                    = WM_USER + 102
                        #~#~#~ TDM_SET_MARQUEE_PROGRESS_BAR        = WM_USER + 103
                        #~#~#~ TDM_SET_PROGRESS_BAR_STATE          = WM_USER + 104
                        #~#~#~ TDM_SET_PROGRESS_BAR_RANGE          = WM_USER + 105
                        #~#~#~ TDM_SET_PROGRESS_BAR_POS            = WM_USER + 106

                        # wParam = 0 (stop marquee), wParam != 0
                        # (start marquee), lparam = speed
                        # (milliseconds between repaints)
                        #~#~#~ TDM_SET_PROGRESS_BAR_MARQUEE        = WM_USER + 107

                        # wParam = element (TASKDIALOG_ELEMENTS), lParam = new
                        # element text (LPCWSTR)
                        #~#~#~ TDM_SET_ELEMENT_TEXT                = WM_USER + 108
                        #~#~#~ TDM_CLICK_RADIO_BUTTON              = WM_USER + 110

                        # lParam = 0 (disable), lParam != 0 (enable), wParam =
                        # Button ID
                        #~#~#~ TDM_ENABLE_BUTTON                   = WM_USER + 111

                        # lParam = 0 (disable), lParam != 0 (enable), wParam =
                        # Radio Button ID
                        #~#~#~ TDM_ENABLE_RADIO_BUTTON             = WM_USER + 112

                        # wParam = 0 (unchecked), 1 (checked), lParam = 1
                        # (set key focus)
                        #~#~#~ TDM_CLICK_VERIFICATION              = WM_USER + 113

                        # wParam = element (TASKDIALOG_ELEMENTS), lParam = new
                        # element text (LPCWSTR)
                        #~#~#~ TDM_UPDATE_ELEMENT_TEXT             = WM_USER + 114

                        # wParam = Button ID, lParam = 0
                        # (elevation not required), lParam != 0
                        # (elevation required)
                        #~#~#~ TDM_SET_BUTTON_ELEVATION_REQUIRED_STATE = WM_USER + 115

                        # wParam = icon element (TASKDIALOG_ICON_ELEMENTS),
                        # lParam = new icon
                        # (hIcon if TDF_USE_HICON_* was set, PCWSTR otherwise)
                        #~#~#~ TDM_UPDATE_ICON                     = WM_USER + 116
                        pass


                    TASKDIALOG_MESSAGES = _TASKDIALOG_MESSAGES
                    class _TASKDIALOG_NOTIFICATIONS(ENUM):
                        TDN_CREATED = 0
                        TDN_NAVIGATED = 1
                        TDN_BUTTON_CLICKED = 2
                        TDN_HYPERLINK_CLICKED = 3

                        # wParam = Milliseconds since dialog created or timer
                        # reset
                        TDN_TIMER = 4
                        TDN_DESTROYED = 5
                        TDN_RADIO_BUTTON_CLICKED = 6
                        TDN_DIALOG_CONSTRUCTED = 7

                        # wParam = 1 if checkbox checked, 0 if not, lParam is
                        # unused and always 0
                        TDN_VERIFICATION_CLICKED = 8
                        TDN_HELP = 9

                        # wParam = 0 (dialog is now collapsed), wParam != 0
                        # (dialog is now expanded)
                        TDN_EXPANDO_BUTTON_CLICKED = 10


                    TASKDIALOG_NOTIFICATIONS = _TASKDIALOG_NOTIFICATIONS
                    class _TASKDIALOG_BUTTON(ctypes.Structure):
                        pass


                    _TASKDIALOG_BUTTON._fields_ = [
                        ('nButtonID', INT),
                        ('pszButtonText', PCWSTR),
                    ]
                    TASKDIALOG_BUTTON = _TASKDIALOG_BUTTON
                    class _TASKDIALOG_ELEMENTS(ENUM):
                        TDE_CONTENT = 1
                        TDE_EXPANDED_INFORMATION = 2
                        TDE_FOOTER = 3
                        TDE_MAIN_INSTRUCTION = 4


                    TASKDIALOG_ELEMENTS = _TASKDIALOG_ELEMENTS
                    class _TASKDIALOG_ICON_ELEMENTS(ENUM):
                        TDIE_ICON_MAIN = 1
                        TDIE_ICON_FOOTER = 2


                    TASKDIALOG_ICON_ELEMENTS = _TASKDIALOG_ICON_ELEMENTS
                    TD_WARNING_ICON = MAKEINTRESOURCEW( - 1)
                    TD_ERROR_ICON = MAKEINTRESOURCEW( - 2)
                    TD_INFORMATION_ICON = MAKEINTRESOURCEW( - 3)
                    TD_SHIELD_ICON = MAKEINTRESOURCEW( - 4)
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

                if NTDDI_VERSION >= NTDDI_VISTA:
                    class _TASKDIALOG_COMMON_BUTTON_FLAGS(ENUM):
                        TDCBF_OK_BUTTON = 0x0001
                        TDCBF_YES_BUTTON = 0x0002
                        TDCBF_NO_BUTTON = 0x0004
                        TDCBF_CANCEL_BUTTON = 0x0008
                        TDCBF_RETRY_BUTTON = 0x0010
                        TDCBF_CLOSE_BUTTON = 0x0020


                    TDCBF_OK_BUTTON = _TASKDIALOG_COMMON_BUTTON_FLAGS.TDCBF_OK_BUTTON
                    TDCBF_YES_BUTTON = _TASKDIALOG_COMMON_BUTTON_FLAGS.TDCBF_YES_BUTTON
                    TDCBF_NO_BUTTON = _TASKDIALOG_COMMON_BUTTON_FLAGS.TDCBF_NO_BUTTON
                    TDCBF_CANCEL_BUTTON = _TASKDIALOG_COMMON_BUTTON_FLAGS.TDCBF_CANCEL_BUTTON
                    TDCBF_RETRY_BUTTON = _TASKDIALOG_COMMON_BUTTON_FLAGS.TDCBF_RETRY_BUTTON
                    TDCBF_CLOSE_BUTTON = _TASKDIALOG_COMMON_BUTTON_FLAGS.TDCBF_CLOSE_BUTTON
                    TASKDIALOG_COMMON_BUTTON_FLAGS = INT
                    class _TASKDIALOGCONFIG(ctypes.Structure):
                        pass


                    DUMMYUNIONNAME._fields_ = [
                        ('hMainIcon', HICON),
                        ('pszMainIcon', PCWSTR),
                    ]
                    _TASKDIALOGCONFIG.DUMMYUNIONNAME = DUMMYUNIONNAME
                    class DUMMYUNIONNAME2(ctypes.Union):
                        pass


                    DUMMYUNIONNAME2._fields_ = [
                        ('hFooterIcon', HICON),
                        ('pszFooterIcon', PCWSTR),
                    ]
                    _TASKDIALOGCONFIG.DUMMYUNIONNAME2 = DUMMYUNIONNAME2
                    _TASKDIALOGCONFIG._fields_ = [
                        ('cbSize', UINT),

                        # incorrectly named, this is the owner window, not a
                        # parent.
                        ('hwndParent', HWND),
                        ('hInstance', HINSTANCE), # used for MAKEINTRESOURCE() strings
                        ('dwFlags', TASKDIALOG_FLAGS), # TASKDIALOG_FLAGS (TDF_XXX) flags
                        ('dwCommonButtons', TASKDIALOG_COMMON_BUTTON_FLAGS), # TASKDIALOG_COMMON_BUTTON (TDCBF_XXX) flags
                        ('pszWindowTitle', PCWSTR), # string or MAKEINTRESOURCE()
                        ('DUMMYUNIONNAME', _TASKDIALOGCONFIG.DUMMYUNIONNAME),
                        ('pszMainInstruction', PCWSTR),
                        ('pszContent', PCWSTR),
                        ('cButtons', UINT),
                        ('pButtons', POINTER(TASKDIALOG_BUTTON)),
                        ('nDefaultButton', INT),
                        ('cRadioButtons', UINT),
                        ('pRadioButtons', POINTER(TASKDIALOG_BUTTON)),
                        ('nDefaultRadioButton', INT),
                        ('pszVerificationText', PCWSTR),
                        ('pszExpandedInformation', PCWSTR),
                        ('pszExpandedControlText', PCWSTR),
                        ('pszCollapsedControlText', PCWSTR),
                        ('DUMMYUNIONNAME2', _TASKDIALOGCONFIG.DUMMYUNIONNAME2),
                        ('pszFooter', PCWSTR),
                        ('pfCallback', PFTASKDIALOGCALLBACK),
                        ('lpCallbackData', LONG_PTR),

                        # width of the Task Dialog's client area in DLU's. If
                        # 0, Task Dialog will calculate the ideal width.
                        ('cxWidth', UINT),
                    ]
                    TASKDIALOGCONFIG = _TASKDIALOGCONFIG
                    DUMMYUNIONNAME._fields_ = [
                        ('hMainIcon', HICON),
                        ('pszMainIcon', PCWSTR),
                    ]
                    DUMMYUNIONNAME2._fields_ = [
                        ('hFooterIcon', HICON),
                        ('pszFooterIcon', PCWSTR),
                    ]
                    if defined(_WIN32):
                        pass
                    # END IF
                # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
            # END IF   NOTASKDIALOG

            # == == == == == == == == == == End TaskDialog == == == == == ==
            # == == == == == =

            # == = MUI APIs == =
            if not defined(NOMUI):
                # VOID WINAPI InitMUILanguage(LANGID uiLang);
                InitMUILanguage = comctl32.InitMUILanguage
                InitMUILanguage.restype = WINAPI
                # LANGID WINAPI GetMUILanguage(VOID);
                GetMUILanguage = comctl32.GetMUILanguage
                GetMUILanguage.restype = WINAPI
            # END IF   NOMUI
            if defined(_WIN32):

                # == == == TrackMouseEvent == == == == == == == == == == == ==
                # == == == == == == == == == == == == == == =
                if not defined(NOTRACKMOUSEEVENT):

                    # If the messages for TrackMouseEvent have not been
                    # defined then define them

                    # now.
                    if not defined(WM_MOUSEHOVER):
                        WM_MOUSEHOVER = 0x02A1
                        WM_MOUSELEAVE = 0x02A3
                    # END IF

                    # If the TRACKMOUSEEVENT structure and associated flags
                    # havent been declared

                    # then declare them now.

                    if not defined(TME_HOVER):
                        TME_HOVER = 0x00000001
                        TME_LEAVE = 0x00000002

                        if WINVER >= 0x0500:
                            TME_NONCLIENT = 0x00000010
                        # END IF  WINVER >= 0x0500
                        TME_QUERY = 0x40000000
                        TME_CANCEL = 0x80000000
                        HOVER_DEFAULT = 0xFFFFFFFF
                        class tagTRACKMOUSEEVENT(ctypes.Structure):
                            pass


                        tagTRACKMOUSEEVENT._fields_ = [
                            ('cbSize', DWORD),
                            ('dwFlags', DWORD),
                            ('hwndTrack', HWND),
                            ('dwHoverTime', DWORD),
                        ]
                        TRACKMOUSEEVENT = tagTRACKMOUSEEVENT
                        LPTRACKMOUSEEVENT = POINTER(tagTRACKMOUSEEVENT)
                    # END IF   not TME_HOVER

                    # Declare _TrackMouseEvent. This API tries to use the
                    # window manager's

                    # implementation of TrackMouseEvent if it is present,
                    # otherwise it emulates.
                    # WINCOMMCTRLAPI
                    # BOOL
                    # WINAPI
                    # _TrackMouseEvent(
                    # _Inout_ LPTRACKMOUSEEVENT lpEventTrack);
                    _TrackMouseEvent = comctl32._TrackMouseEvent
                    _TrackMouseEvent.restype = BOOL
                # END IF   not NOTRACKMOUSEEVENT

                # == == == Flat Scrollbar APIs == == == == == == == == == ==
                # == == == == == == == == == == =

                if not defined(NOFLATSBAPIS):
                    WSB_PROP_CYVSCROLL = 0x00000001
                    WSB_PROP_CXHSCROLL = 0x00000002
                    WSB_PROP_CYHSCROLL = 0x00000004
                    WSB_PROP_CXVSCROLL = 0x00000008
                    WSB_PROP_CXHTHUMB = 0x00000010
                    WSB_PROP_CYVTHUMB = 0x00000020
                    WSB_PROP_VBKGCOLOR = 0x00000040
                    WSB_PROP_HBKGCOLOR = 0x00000080
                    WSB_PROP_VSTYLE = 0x00000100
                    WSB_PROP_HSTYLE = 0x00000200
                    WSB_PROP_WINSTYLE = 0x00000400
                    WSB_PROP_PALETTE = 0x00000800
                    WSB_PROP_MASK = 0x00000FFF
                    FSB_FLAT_MODE = 2
                    FSB_ENCARTA_MODE = 1
                    FSB_REGULAR_MODE = 0
                    # WINCOMMCTRLAPI BOOL WINAPI FlatSB_EnableScrollBar(HWND, int, UINT);
                    FlatSB_EnableScrollBar = comctl32.FlatSB_EnableScrollBar
                    FlatSB_EnableScrollBar.restype = BOOL
                    # WINCOMMCTRLAPI BOOL WINAPI FlatSB_ShowScrollBar(HWND, INT code, BOOL);
                    FlatSB_ShowScrollBar = comctl32.FlatSB_ShowScrollBar
                    FlatSB_ShowScrollBar.restype = BOOL
                    # WINCOMMCTRLAPI BOOL WINAPI FlatSB_GetScrollRange(HWND, INT code, LPINT, LPINT);
                    FlatSB_GetScrollRange = comctl32.FlatSB_GetScrollRange
                    FlatSB_GetScrollRange.restype = BOOL
                    # WINCOMMCTRLAPI BOOL WINAPI FlatSB_GetScrollInfo(HWND, INT code, LPSCROLLINFO);
                    FlatSB_GetScrollInfo = comctl32.FlatSB_GetScrollInfo
                    FlatSB_GetScrollInfo.restype = BOOL
                    # WINCOMMCTRLAPI INT WINAPI FlatSB_GetScrollPos(HWND, INT code);
                    FlatSB_GetScrollPos = comctl32.FlatSB_GetScrollPos
                    FlatSB_GetScrollPos.restype = INT
                    # WINCOMMCTRLAPI BOOL WINAPI FlatSB_GetScrollProp(HWND, INT propIndex, LPINT);
                    FlatSB_GetScrollProp = comctl32.FlatSB_GetScrollProp
                    FlatSB_GetScrollProp.restype = BOOL

                    if defined(_WIN64):
                        # WINCOMMCTRLAPI BOOL WINAPI FlatSB_GetScrollPropPtr(HWND, INT propIndex, PINT_PTR);
                        FlatSB_GetScrollPropPtr = comctl32.FlatSB_GetScrollPropPtr
                        FlatSB_GetScrollPropPtr.restype = BOOL
                    else:
                        FlatSB_GetScrollPropPtr = FlatSB_GetScrollProp
                    # END IF
                    # WINCOMMCTRLAPI INT WINAPI FlatSB_SetScrollPos(HWND, INT code, INT pos, BOOL fRedraw);
                    FlatSB_SetScrollPos = comctl32.FlatSB_SetScrollPos
                    FlatSB_SetScrollPos.restype = INT
                    # WINCOMMCTRLAPI INT WINAPI FlatSB_SetScrollInfo(HWND, INT code, LPSCROLLINFO psi, BOOL fRedraw);
                    FlatSB_SetScrollInfo = comctl32.FlatSB_SetScrollInfo
                    FlatSB_SetScrollInfo.restype = INT
                    # WINCOMMCTRLAPI INT WINAPI FlatSB_SetScrollRange(HWND, INT code, INT min, INT max, BOOL fRedraw);
                    FlatSB_SetScrollRange = comctl32.FlatSB_SetScrollRange
                    FlatSB_SetScrollRange.restype = INT
                    # WINCOMMCTRLAPI BOOL WINAPI FlatSB_SetScrollProp(HWND, UINT index, INT_PTR newValue, BOOL);
                    FlatSB_SetScrollProp = comctl32.FlatSB_SetScrollProp
                    FlatSB_SetScrollProp.restype = BOOL
                    FlatSB_SetScrollPropPtr = FlatSB_SetScrollProp
                    # WINCOMMCTRLAPI BOOL WINAPI InitializeFlatSB(HWND);
                    InitializeFlatSB = comctl32.InitializeFlatSB
                    InitializeFlatSB.restype = BOOL
                    # WINCOMMCTRLAPI HRESULT WINAPI UninitializeFlatSB(HWND);
                    UninitializeFlatSB = comctl32.UninitializeFlatSB
                    UninitializeFlatSB.restype = HRESULT
                # END IF    NOFLATSBAPIS
            # END IF  _WIN32

            if NTDDI_VERSION >= NTDDI_WINXP:

                # subclassing stuff
                # LRESULT WINAPI DefSubclassProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
                DefSubclassProc = comctl32.DefSubclassProc
                DefSubclassProc.restype = WINAPI
            # END IF
            if NTDDI_VERSION >= NTDDI_VISTA:
                class _LI_METRIC(ENUM):
                    LIM_SMALL = 1
                    LIM_LARGE = 2


                LIM_SMALL = _LI_METRIC.LIM_SMALL
                LIM_LARGE = _LI_METRIC.LIM_LARGE
            # END IF   NTDDI_VISTA
            if NTDDI_VERSION >= NTDDI_WINXP:
                pass
            # END IF
                if defined(ISOLATION_AWARE_ENABLED) and (ISOLATION_AWARE_ENABLED != 0):
                    pass
                # END IF  ISOLATION_AWARE_ENABLED
            if not defined(RC_INVOKED): # RC complains about LONG symbols in #ifs
                pass
            # END IF  RC
            if defined(__cplusplus):
                pass
            # END IF
        # END IF
        if defined(_MSC_VER) and (_MSC_VER >= 1200):
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  _INC_COMMCTRL
