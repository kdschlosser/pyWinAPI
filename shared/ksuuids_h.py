from pyWinAPI import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -
# File: ksuuids.h
# Desc: Contains the GUIDs for the MediaType type, subtype fields and format
# types for DVD/MPEG2 media types.
# Copyright (c) Microsoft Corporation. All rights reserved.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -
from pyWinAPI.shared.winapifamily_h import * # NOQA

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    from pyWinAPI.shared.uuids_h import * # NOQA
    from pyWinAPI.shared.sdkddkver_h import *

    # - - - MPEG 2 definitions - - -
    # 36523B13 - 8EE5 - 11d1 - 8CA3 - 0060B057664A
    MEDIATYPE_MPEG2_PACK = OUR_GUID_ENTRY(
        0x36523B13,
        0x8EE5,
        0x11D1,
        0x8C,
        0xA3,
        0x00,
        0x60,
        0xB0,
        0x57,
        0x66,
        0x4A
    )

    # e06d8020 - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIATYPE_MPEG2_PES = OUR_GUID_ENTRY(
        0xE06D8020,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x5F,
        0x6C,
        0xBB,
        0xEA
    )
    MEDIATYPE_CONTROL = DEFINE_GUID(
        0xE06D8021,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )
    if (
        NTDDI_WS03 > NTDDI_VERSION >= NTDDI_WINXPSP2 or
        NTDDI_VERSION >= NTDDI_WS03SP1
    ):
        MEDIATYPE_MPEG2_SECTIONS = OUR_GUID_ENTRY(
            0x455F176C,
            0x4B06,
            0x47CE,
            0x9A,
            0xEF,
            0x8C,
            0xAE,
            0xF7,
            0x3D,
            0xF7,
            0xB5
        )

        # {1ED988B0 - 3FFC - 4523 - 8725 - 347BEEC1A8A0}
        MEDIASUBTYPE_MPEG2_VERSIONED_TABLES = OUR_GUID_ENTRY(
            0x1ED988B0,
            0x3FFC,
            0x4523,
            0x87,
            0x25,
            0x34,
            0x7B,
            0xEE,
            0xC1,
            0xA8,
            0xA0
        )
        MEDIASUBTYPE_ATSC_SI = OUR_GUID_ENTRY(
            0xB3C7397C,
            0xD303,
            0x414D,
            0xB3,
            0x3C,
            0x4E,
            0xD2,
            0xC9,
            0xD2,
            0x97,
            0x33
        )
        MEDIASUBTYPE_DVB_SI = OUR_GUID_ENTRY(
            0xE9DD31A3,
            0x221D,
            0x4ADB,
            0x85,
            0x32,
            0x9A,
            0xF3,
            0x9,
            0xC1,
            0xA4,
            0x8
        )
        MEDIASUBTYPE_ISDB_SI = OUR_GUID_ENTRY(
            0xE89AD298,
            0x3601,
            0x4B06,
            0xAA,
            0xEC,
            0x9D,
            0xDE,
            0xED,
            0xCC,
            0x5B,
            0xD0
        )

        # {EC232EB2 - CB96 - 4191 - B226 - 0EA129F38250}
        MEDIASUBTYPE_TIF_SI = OUR_GUID_ENTRY(
            0xEC232EB2,
            0xCB96,
            0x4191,
            0xB2,
            0x26,
            0xE,
            0xA1,
            0x29,
            0xF3,
            0x82,
            0x50
        )

        # {C892E55B - 252D - 42b5 - A316 - D997E7A5D995}
        MEDIASUBTYPE_MPEG2DATA = OUR_GUID_ENTRY(
            0xC892E55B,
            0x252D,
            0x42B5,
            0xA3,
            0x16,
            0xD9,
            0x97,
            0xE7,
            0xA5,
            0xD9,
            0x95
        )
    # END IF
    MEDIASUBTYPE_MPEG2_WMDRM_TRANSPORT = OUR_GUID_ENTRY(
        0x18BEC4EA,
        0x4676,
        0x450E,
        0xB4,
        0x78,
        0x0C,
        0xD8,
        0x4C,
        0x54,
        0xB3,
        0x27
    )

    # e06d8026 - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_MPEG2_VIDEO = OUR_GUID_ENTRY(
        0xE06D8026,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x5F,
        0x6C,
        0xBB,
        0xEA
    )

    # use MPEG2VIDEOINFO (defined below) with FORMAT_MPEG2_VIDEO
    # e06d80e3 - db46 - 11cf - b4d1 - 00805f6cbbea
    FORMAT_MPEG2_VIDEO = OUR_GUID_ENTRY(
        0xE06D80E3,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x5F,
        0x6C,
        0xBB,
        0xEA
    )

    # F72A76A0 - EB0A - 11d0 - ACE4 - 0000C0CC16BA  (FORMAT_VideoInfo2)
    FORMAT_VIDEOINFO2 = OUR_GUID_ENTRY(
        0xF72A76A0,
        0xEB0A,
        0x11D0,
        0xAC,
        0xE4,
        0x0,
        0x0,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # MPEG2 Other subtypes
    # e06d8022 - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_MPEG2_PROGRAM = OUR_GUID_ENTRY(
        0xE06D8022,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d8023 - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_MPEG2_TRANSPORT = OUR_GUID_ENTRY(
        0xE06D8023,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )
    if NTDDI_VERSION >= NTDDI_WINXP:
        # 138AA9A4 - 1EE2 - 4c5b - 988E - 19ABFDBC8A11
        MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE = OUR_GUID_ENTRY(
            0x138AA9A4,
            0x1EE2,
            0x4C5B,
            0x98,
            0x8E,
            0x19,
            0xAB,
            0xFD,
            0xBC,
            0x8A,
            0x11
        )

        # {18BEC4EA - 4676 - 450e - B478 - 0CD84C54B327}
        MEDIASUBTYPE_MPEG2_UDCR_TRANSPORT = OUR_GUID_ENTRY(
            0x18BEC4EA,
            0x4676,
            0x450E,
            0xB4,
            0x78,
            0x0C,
            0xD8,
            0x4C,
            0x54,
            0xB3,
            0x27
        )

        # {0d7aed42 - cb9a - 11db - 9705 - 005056c00008}
        MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_RAW = OUR_GUID_ENTRY(
            0x0D7AED42,
            0xCB9A,
            0x11DB,
            0x97,
            0x5,
            0x0,
            0x50,
            0x56,
            0xC0,
            0x0,
            0x8
        )

        # {af748dd4 - d800 - 11db - 9705 - 005056c00008}
        MEDIASUBTYPE_MPEG2_PBDA_TRANSPORT_PROCESSED = OUR_GUID_ENTRY(
            0xAF748DD4,
            0xD80,
            0x11DB,
            0x97,
            0x5,
            0x0,
            0x50,
            0x56,
            0xC0,
            0x0,
            0x8
        )
    # END IF
    # e06d802b - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_MPEG2_AUDIO = OUR_GUID_ENTRY(
        0xE06D802B,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d802c - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_DOLBY_AC3 = OUR_GUID_ENTRY(
        0xE06D802C,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d802d - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_DVD_SUBPICTURE = OUR_GUID_ENTRY(
        0xE06D802D,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d8032 - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_DVD_LPCM_AUDIO = OUR_GUID_ENTRY(
        0xE06D8032,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )
    if NTDDI_VERSION >= NTDDI_WINXP:
        # e06d8033 - db46 - 11cf - b4d1 - 00805f6cbbea
        MEDIASUBTYPE_DTS = OUR_GUID_ENTRY(
            0xE06D8033,
            0xDB46,
            0x11CF,
            0xB4,
            0xD1,
            0x00,
            0x80,
            0x05F,
            0x6C,
            0xBB,
            0xEA
        )

        # e06d8034 - db46 - 11cf - b4d1 - 00805f6cbbea
        MEDIASUBTYPE_SDDS = OUR_GUID_ENTRY(
            0xE06D8034,
            0xDB46,
            0x11CF,
            0xB4,
            0xD1,
            0x00,
            0x80,
            0x05F,
            0x6C,
            0xBB,
            0xEA
        )
    # END IF

    # DVD - related mediatypes
    # ED0B916A - 044D - 11d1 - AA78 - 00C04FC31D60
    MEDIATYPE_DVD_ENCRYPTED_PACK = OUR_GUID_ENTRY(
        0xED0B916A,
        0x044D,
        0x11D1,
        0xAA,
        0x78,
        0x00,
        0xC0,
        0x04F,
        0xC3,
        0x1D,
        0x60
    )

    # e06d802e - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIATYPE_DVD_NAVIGATION = OUR_GUID_ENTRY(
        0xE06D802E,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d802f - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_DVD_NAVIGATION_PCI = OUR_GUID_ENTRY(
        0xE06D802F,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d8030 - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_DVD_NAVIGATION_DSI = OUR_GUID_ENTRY(
        0xE06D8030,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d8031 - db46 - 11cf - b4d1 - 00805f6cbbea
    MEDIASUBTYPE_DVD_NAVIGATION_PROVIDER = OUR_GUID_ENTRY(
        0xE06D8031,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # DVD - MPEG2/AC3 - related Formats
    # e06d80e3 - db46 - 11cf - b4d1 - 00805f6cbbea
    FORMAT_MPEG2Video = OUR_GUID_ENTRY(
        0xE06D80E3,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d80e4 - db46 - 11cf - b4d1 - 00805f6cbbea
    FORMAT_DolbyAC3 = OUR_GUID_ENTRY(
        0xE06D80E4,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d80e5 - db46 - 11cf - b4d1 - 00805f6cbbea
    FORMAT_MPEG2Audio = OUR_GUID_ENTRY(
        0xE06D80E5,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # e06d80e6 - db46 - 11cf - b4d1 - 00805f6cbbea
    FORMAT_DVD_LPCMAudio = OUR_GUID_ENTRY(
        0xE06D80E6,
        0xDB46,
        0x11CF,
        0xB4,
        0xD1,
        0x00,
        0x80,
        0x05F,
        0x6C,
        0xBB,
        0xEA
    )

    # UVC 1.2 H.264 Video Format
    # 2017be05 - 6629 - 4248 - aaed - 7e1a47bc9b9c
    FORMAT_UVCH264Video = OUR_GUID_ENTRY(
        0x2017BE05,
        0x6629,
        0x4248,
        0xAA,
        0xED,
        0x7E,
        0x1A,
        0x47,
        0xBC,
        0x9B,
        0x9C
    )

    # JPEG Image Format
    # 692fa379 - d3e8 - 4651 - b5b4 - 0b94b013eeaf
    FORMAT_JPEGImage = OUR_GUID_ENTRY(
        0x692FA379,
        0xD3E8,
        0x4651,
        0xB5,
        0xB4,
        0xB,
        0x94,
        0xB0,
        0x13,
        0xEE,
        0xAF
    )

    # Image Format
    # 692fa379 - d3e8 - 4651 - b5b4 - 0b94b013eeaf
    FORMAT_Image = OUR_GUID_ENTRY(
        0x692FA379,
        0xD3E8,
        0x4651,
        0xB5,
        0xB4,
        0xB,
        0x94,
        0xB0,
        0x13,
        0xEE,
        0xAF
    )

    # KS Property Set Id (to communicate with the WDM Proxy filter) - - from
    # ksmedia.h of WDM DDK.
    # BFABE720 - 6E1F - 11D0 - BCF2 - 444553540000
    AM_KSPROPSETID_AC3 = OUR_GUID_ENTRY(
        0xBFABE720,
        0x6E1F,
        0x11D0,
        0xBC,
        0xF2,
        0x44,
        0x45,
        0x53,
        0x54,
        0x00,
        0x00
    )

    # ac390460 - 43af - 11d0 - bd6a - 003505c103a9
    AM_KSPROPSETID_DvdSubPic = OUR_GUID_ENTRY(
        0xAC390460,
        0x43AF,
        0x11D0,
        0xBD,
        0x6A,
        0x00,
        0x35,
        0x05,
        0xC1,
        0x03,
        0xA9
    )

    # 0E8A0A40L - 6AEF - 11D0 - 9ED0 - 00A024CA19B3
    AM_KSPROPSETID_CopyProt = OUR_GUID_ENTRY(
        0x0E8A0A40,
        0x6AEF,
        0x11D0,
        0x9E,
        0xD0,
        0x00,
        0xA0,
        0x24,
        0xCA,
        0x19,
        0xB3
    )

    # A503C5C0 - 1D1D - 11d1 - AD80 - 444553540000
    AM_KSPROPSETID_TSRateChange = OUR_GUID_ENTRY(
        0xA503C5C0,
        0x1D1D,
        0x11D1,
        0xAD,
        0x80,
        0x44,
        0x45,
        0x53,
        0x54,
        0x0,
        0x0
    )
    if NTDDI_VERSION >= NTDDI_WINXP:
        # 3577EB09 - 9582 - 477f - B29C - B0C452A4FF9A
        AM_KSPROPSETID_DVD_RateChange = OUR_GUID_ENTRY(
            0x3577EB09,
            0x9582,
            0x477F,
            0xB2,
            0x9C,
            0xB0,
            0xC4,
            0x52,
            0xA4,
            0xFF,
            0x9A
        )

        # ae4720ae - aa71 - 42d8 - b82a - fffdf58b76fd
        AM_KSPROPSETID_DvdKaraoke = OUR_GUID_ENTRY(
            0xAE4720AE,
            0xAA71,
            0x42D8,
            0xB8,
            0x2A,
            0xFF,
            0xFD,
            0xF5,
            0x8B,
            0x76,
            0xFD
        )

        # c830acbd - ab07 - 492f - 8852 - 45b6987c2979
        AM_KSPROPSETID_FrameStep = OUR_GUID_ENTRY(
            0xC830ACBD,
            0xAB07,
            0x492F,
            0x88,
            0x52,
            0x45,
            0xB6,
            0x98,
            0x7C,
            0x29,
            0x79
        )
    # END IF
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - -
    # MPEG4 related KSPROPSETIDs from ksmedia.h of WDK
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - -
    # FF6C4BFA - 07A9 - 4c7b - A237 - 672F9D68065F
    AM_KSPROPSETID_MPEG4_MediaType_Attributes = OUR_GUID_ENTRY(
        0xFF6C4BFA,
        0x7A9,
        0x4C7B,
        0xA2,
        0x37,
        0x67,
        0x2F,
        0x9D,
        0x68,
        0x6,
        0x5F
    )

    # KS categories from ks.h and ksmedia.h
    # 65E8773D - 8F56 - 11D0 - A3B9 - 00A0C9223196
    AM_KSCATEGORY_CAPTURE = OUR_GUID_ENTRY(
        0x65E8773D,
        0x8F56,
        0x11D0,
        0xA3,
        0xB9,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # 65E8773E - 8F56 - 11D0 - A3B9 - 00A0C9223196
    AM_KSCATEGORY_RENDER = OUR_GUID_ENTRY(
        0x65E8773E,
        0x8F56,
        0x11D0,
        0xA3,
        0xB9,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # 1E84C900 - 7E70 - 11D0 - A5D6 - 28DB04C10000
    AM_KSCATEGORY_DATACOMPRESSOR = OUR_GUID_ENTRY(
        0x1E84C900,
        0x7E70,
        0x11D0,
        0xA5,
        0xD6,
        0x28,
        0xDB,
        0x04,
        0xC1,
        0x00,
        0x00
    )

    # 6994AD04 - 93EF - 11D0 - A3CC - 00A0C9223196
    AM_KSCATEGORY_AUDIO = OUR_GUID_ENTRY(
        0x6994AD04,
        0x93EF,
        0x11D0,
        0xA3,
        0xCC,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # 6994AD05 - 93EF - 11D0 - A3CC - 00A0C9223196
    AM_KSCATEGORY_VIDEO = OUR_GUID_ENTRY(
        0x6994AD05,
        0x93EF,
        0x11D0,
        0xA3,
        0xCC,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # a799a800 - a46d - 11d0 - a18c - 00a02401dcd4
    AM_KSCATEGORY_TVTUNER = OUR_GUID_ENTRY(
        0xA799A800,
        0xA46D,
        0x11D0,
        0xA1,
        0x8C,
        0x00,
        0xA0,
        0x24,
        0x01,
        0xDC,
        0xD4
    )

    # a799a801 - a46d - 11d0 - a18c - 00a02401dcd4
    AM_KSCATEGORY_CROSSBAR = OUR_GUID_ENTRY(
        0xA799A801,
        0xA46D,
        0x11D0,
        0xA1,
        0x8C,
        0x00,
        0xA0,
        0x24,
        0x01,
        0xDC,
        0xD4
    )

    # a799a802 - a46d - 11d0 - a18c - 00a02401dcd4
    AM_KSCATEGORY_TVAUDIO = OUR_GUID_ENTRY(
        0xA799A802,
        0xA46D,
        0x11D0,
        0xA1,
        0x8C,
        0x00,
        0xA0,
        0x24,
        0x01,
        0xDC,
        0xD4
    )

    # 07dad660L - 22f1 - 11d1 - a9f4 - 00c04fbbde8f
    AM_KSCATEGORY_VBICODEC = OUR_GUID_ENTRY(
        0x07DAD660,
        0x22F1,
        0x11D1,
        0xA9,
        0xF4,
        0x00,
        0xC0,
        0x4F,
        0xBB,
        0xDE,
        0x8F
    )
    if NTDDI_VERSION >= NTDDI_WS03SP1:
        # multi - instance safe codec categories(kernel or user mode)
        # {9C24A977 - 0951 - 451a - 8006 - 0E49BD28CD5F}
        AM_KSCATEGORY_VBICODEC_MI = OUR_GUID_ENTRY(
            0x9C24A977,
            0x951,
            0x451A,
            0x80,
            0x6,
            0xE,
            0x49,
            0xBD,
            0x28,
            0xCD,
            0x5F
        )
    # END IF
    # 0A4252A0L - 7E70 - 11D0 - A5D6 - 28DB04C10000
    AM_KSCATEGORY_SPLITTER = OUR_GUID_ENTRY(
        0x0A4252A0,
        0x7E70,
        0x11D0,
        0xA5,
        0xD6,
        0x28,
        0xDB,
        0x04,
        0xC1,
        0x00,
        0x00
    )

    # GUIDs needed to support IKsPin interface
    # d3abc7e0l - 9a61 - 11d0 - a40d00a0c9223196
    IID_IKsInterfaceHandler = OUR_GUID_ENTRY(
        0xD3ABC7E0,
        0x9A61,
        0x11D0,
        0xA4,
        0x0D,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # 5ffbaa02l - 49a3 - 11d0 - 9f3600aa00a216a1
    IID_IKsDataTypeHandler = OUR_GUID_ENTRY(
        0x5FFBAA02,
        0x49A3,
        0x11D0,
        0x9F,
        0x36,
        0x00,
        0xAA,
        0x00,
        0xA2,
        0x16,
        0xA1
    )

    # b61178d1 - a2d9 - 11cf - 9e53 - 00aa00a216a1
    IID_IKsPin = OUR_GUID_ENTRY(
        0xB61178D1,
        0xA2D9,
        0x11CF,
        0x9E,
        0x53,
        0x00,
        0xAA,
        0x00,
        0xA2,
        0x16,
        0xA1
    )

    # 28F54685 - 06FD - 11D2 - B27A - 00A0C9223196
    IID_IKsControl = OUR_GUID_ENTRY(
        0x28F54685,
        0x06FD,
        0x11D2,
        0xB2,
        0x7A,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # CD5EBE6B - 8B6E - 11D1 - 8AE0 - 00A0C9223196
    IID_IKsPinFactory = OUR_GUID_ENTRY(
        0xCD5EBE6B,
        0x8B6E,
        0x11D1,
        0x8A,
        0xE0,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # 1A8766A0 - 62CE - 11CF - A5D6 - 28DB04C10000
    AM_INTERFACESETID_Standard = OUR_GUID_ENTRY(
        0x1A8766A0,
        0x62CE,
        0x11CF,
        0xA5,
        0xD6,
        0x28,
        0xDB,
        0x04,
        0xC1,
        0x00,
        0x00
    )
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
