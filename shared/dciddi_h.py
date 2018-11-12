import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

_INC_DCIDDI = None



# ***************************************************************** FILE:
# dciddi.h DESCRIPTION: definitions for MS/Intel - defined DCI interface
# Copyright (C) 1994 - 1999 Intel/Microsoft Corporation. All Rights Reserved.
# ****************************************************************
if not defined(_INC_DCIDDI):
    _INC_DCIDDI = 1

    from pyWinAPI.shared.winapifamily_h import *
    from pyWinAPI.shared.guiddef_h import *
    from pyWinAPI.shared.mmreg_h import mmioFOURCC

    if _MSC_VER > 1000:
        pass
    # END IF
    if defined(__cplusplus):
        pass
    # END IF
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        DCICOMMAND = 3075
        DCI_VERSION = 0x0100
        DCICREATEPRIMARYSURFACE = 1
        DCICREATEOFFSCREENSURFACE = 2
        DCICREATEOVERLAYSURFACE = 3
        DCIENUMSURFACE = 4
        DCIESCAPE = 5
        DCI_OK = 0
        DCI_FAIL_GENERIC = - 1
        DCI_FAIL_UNSUPPORTEDVERSION = - 2
        DCI_FAIL_INVALIDSURFACE = - 3
        DCI_FAIL_UNSUPPORTED = - 4
        DCI_ERR_CURRENTLYNOTAVAIL = - 5
        DCI_ERR_INVALIDRECT = - 6
        DCI_ERR_UNSUPPORTEDFORMAT = - 7
        DCI_ERR_UNSUPPORTEDMASK = - 8
        DCI_ERR_TOOBIGHEIGHT = - 9
        DCI_ERR_TOOBIGWIDTH = - 10
        DCI_ERR_TOOBIGSIZE = - 11
        DCI_ERR_OUTOFMEMORY = - 12
        DCI_ERR_INVALIDPOSITION = - 13
        DCI_ERR_INVALIDSTRETCH = - 14
        DCI_ERR_INVALIDCLIPLIST = - 15
        DCI_ERR_SURFACEISOBSCURED = - 16
        DCI_ERR_XALIGN = - 17
        DCI_ERR_YALIGN = - 18
        DCI_ERR_XYALIGN = - 19
        DCI_ERR_WIDTHALIGN = - 20
        DCI_ERR_HEIGHTALIGN = - 21
        DCI_STATUS_POINTERCHANGED = 1
        DCI_STATUS_STRIDECHANGED = 2
        DCI_STATUS_FORMATCHANGED = 4
        DCI_STATUS_SURFACEINFOCHANGED = 8
        DCI_STATUS_CHROMAKEYCHANGED = 16
        DCI_STATUS_WASSTILLDRAWING = 32


        def DCI_SUCCESS(error):
            return error >= 0


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

        if WINVER < 0x0400:
            RDH_RECTANGLES = None

            if not defined(RDH_RECTANGLES):
                class tagRECTL(ctypes.Structure):
                    pass


                tagRECTL._fields_ = [
                    ('left', LONG),
                    ('top', LONG),
                    ('right', LONG),
                    ('bottom', LONG),
                ]

                RECTL = tagRECTL

                RDH_RECTANGLES = 0

                class tagRGNDATAHEADER(ctypes.Structure):
                    pass


                tagRGNDATAHEADER._fields_ = [
                    ('dwSize', DWORD), # size of structure
                    ('iType', DWORD), # Will be RDH_RECTANGLES
                    ('nCount', DWORD), # of clipping rectangles
                    ('nRgnSize', DWORD), # size of buffer - - can be zero
                    ('rcBound', RECTL), # bounding rectangle for region
                ]

                RGNDATAHEADER = tagRGNDATAHEADER


                class tagRGNDATA(ctypes.Structure):
                    pass


                tagRGNDATA._fields_ = [
                    ('rdh', RGNDATAHEADER),
                    ('Buffer', CHAR * 1),
                ]

                RGNDATA = tagRGNDATA


            # END IF
        # END IF

        # ************************************************************************ input structures ***********************************************************************
        #

        # Used by a DCI client to provide input parameters for the
        # DCICREATEPRIMARYSURFACE escape.
        class _DCICMD(ctypes.Structure):
            pass


        _DCICMD._fields_ = [
            ('dwCommand', DWORD),
            ('dwParam1', DWORD),
            ('dwParam2', DWORD),
            ('dwVersion', DWORD),
            ('dwReserved', DWORD),
        ]


        DCICMD = _DCICMD


        # This structure is used by a DCI client to provide input parameters
        # for the DCICREATE... calls. The fields that are actually relevant
        # differ for each of the three calls. Details are in the DCI Spec
        # chapter providing the function specifications.
        class _DCICREATEINPUT(ctypes.Structure):
            pass


        _DCICREATEINPUT._fields_ = [
            ('cmd', DCICMD), # common header structure
            ('dwCompression', DWORD), # format of surface to be created
            ('dwMask', DWORD * 3), # for nonstandard RGB (e.g. 5 - 6 - 5, RGB32)
            ('dwWidth', DWORD), # height of the surface to be created
            ('dwHeight', DWORD), # width of input surfaces
            ('dwDCICaps', DWORD), # capabilities of surface wanted
            ('dwBitCount', DWORD), # bit depth of format to be created
            ('lpSurface', LPVOID), # pointer to an associated surface
        ]


        DCICREATEINPUT = _DCICREATEINPUT
        LPDCICREATEINPUT = POINTER(_DCICREATEINPUT)


        # ************************************************************************ surface info. structures ***********************************************************************
        #

        # This structure is used to return information about available support
        # during a DCIEnumSurface call. It is also used to create a primary
        # surface, and as a member of the larger structures returned by the
        # offscreen and overlay calls.
        class _DCISURFACEINFO(ctypes.Structure):
            pass


        _DCISURFACEINFO._fields_ = [
            ('dwSize', DWORD), # size of structure
            ('dwDCICaps', DWORD), # capability flags (stretch, etc.)
            ('dwCompression', DWORD), # format of surface to be created
            ('dwMask', DWORD * 3), # for BI_BITMASK surfaces
            ('dwWidth', DWORD), # width of surface
            ('dwHeight', DWORD), # height of surface
            ('lStride', LONG), # distance in bytes betw. one pixel
            ('dwBitCount', DWORD), # Bits per pixel for this dwCompression
            ('dwOffSurface', ULONG_PTR), # offset of surface pointer
            ('wSelSurface', WORD), # selector of surface pointer
            ('wReserved', WORD),
            ('dwReserved1', DWORD), # reserved for provider
            ('dwReserved2', DWORD), # reserved for DCIMAN
            ('dwReserved3', DWORD), # reserved for future
            ('BeginAccess', POINTER(VOID)), # BeginAccess callback
            ('EndAccess', POINTER(VOID)), # EndAcess callback
            ('DestroySurface', POINTER(VOID)), # Destroy surface callback
        ]

        DCISURFACEINFO = _DCISURFACEINFO
        LPDCISURFACEINFO = POINTER(_DCISURFACEINFO)

        # This structure is used by a DCI client to provide input parameters
        # for the DCIEnumSurface call.
        class _DCIENUMINPUT(ctypes.Structure):
            pass


        _DCIENUMINPUT._fields_ = [
            ('cmd', DCICMD), # common header structure
            ('rSrc', RECT), # source rect. for stretch
            ('rDst', RECT), # dest. rect. for stretch
            ('EnumCallback', POINTER(VOID)), # callback for supported formats
            ('LPVOID)', VOID), # callback for supported formats
            ('lpContext', LPVOID),
        ]

        DCIENUMINPUT = _DCIENUMINPUT
        LPDCIENUMINPUT = POINTER(_DCIENUMINPUT)

        # This structure must be allocated and returned by the DCI provider in
        # response to a DCICREATEPRIMARYSURFACE call.

        # This structure must be allocated and returned by the DCI provider in
        # response to a DCICREATEOFFSCREENSURFACE call.
        class _DCIOFFSCREEN(ctypes.Structure):
            pass


        _DCIOFFSCREEN._fields_ = [
            ('dciInfo', DCISURFACEINFO), # surface info
            ('Draw', POINTER(VOID)), # copy to onscreen buffer
            ('SetClipList', POINTER(VOID)), # SetCliplist callback
            ('SetDestination', POINTER(VOID)), # SetDestination callback
        ]

        DCIOFFSCREEN = _DCIOFFSCREEN
        LPDCIOFFSCREEN = POINTER(_DCIOFFSCREEN)

        # This structure must be allocated and returned by the DCI provider in
        # response to a DCICREATEOVERLAYSURFACE call.
        class _DCIOVERLAY(ctypes.Structure):
            pass


        _DCIOVERLAY._fields_ = [
            ('dciInfo', DCISURFACEINFO), # surface info
            ('dwChromakeyValue', DWORD), # chromakey color value
            ('dwChromakeyMask', DWORD), # specifies valid bits of value
        ]

        DCIOVERLAY = _DCIOVERLAY
        LPDCIOVERLAY = POINTER(_DCIOVERLAY)

        # DCI FOURCC def.s for extended DIB formats

        YVU9 = None
        if not defined(YVU9):
            YVU9 = mmioFOURCC('Y', 'V', 'U', '9')
        # END IF

        Y411 = None
        if not defined(Y411):
            Y411 = mmioFOURCC('Y', '4', '1', '1')
        # END IF

        YUY2 = None
        if not defined(YUY2):
            YUY2 = mmioFOURCC('Y', 'U', 'Y', '2')
        # END IF

        YVYU = None
        if not defined(YVYU):
            YVYU = mmioFOURCC('Y', 'V', 'Y', 'U')
        # END IF

        UYVY = None
        if not defined(UYVY):
            UYVY = mmioFOURCC('U', 'Y', 'V', 'Y')
        # END IF

        Y211 = None
        if not defined(Y211):
            Y211 = mmioFOURCC('Y', '2', '1', '1')
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF
# END IF   _INC_DCIDDI
