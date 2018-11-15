from pyWinAPI import *
from pyWinAPI.shared.guiddef_h import *


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -
# File: uuids.h
# Desc: Contains the GUIDs for the MediaType type, subtype fields and format
# types for standard media types, and also class ids for well - known
# components.
# Copyright (c) 1992 - 2002, Microsoft Corporation. All rights reserved.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - -
# We want to use this list for generating strings for debugging too
# so we redefine OUR_GUID_ENTRY depending on what we want to do
# It is imperative that all entries in this file are declared using
# OUR_GUID_ENTRY as that macro might have been defined in advance of
# including this file. See wxdebug.cpp in sdk\classes\base.
from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

    OUR_GUID_ENTRY = None

    if not defined(OUR_GUID_ENTRY):
        def OUR_GUID_ENTRY(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
            return DEFINE_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8)
    # END IF
    # - - to allow consistent labeling of Media types and subtypes - -
    MEDIATYPE_NULL = GUID_NULL
    MEDIASUBTYPE_NULL = GUID_NULL

    # - - Use this subtype if you don't have a use for a subtype for your type
    # e436eb8e - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_None
    MEDIASUBTYPE_None = OUR_GUID_ENTRY(
        0xE436EB8E,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # - - major types - - -
    # 73646976 - 0000 - 0010 - 8000 - 00AA00389B71 'vids' == MEDIATYPE_Video
    MEDIATYPE_Video = OUR_GUID_ENTRY(
        0x73646976,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 73647561 - 0000 - 0010 - 8000 - 00AA00389B71 'auds' == MEDIATYPE_Audio
    MEDIATYPE_Audio = OUR_GUID_ENTRY(
        0x73647561,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 73747874 - 0000 - 0010 - 8000 - 00AA00389B71 'txts' == MEDIATYPE_Text
    MEDIATYPE_Text = OUR_GUID_ENTRY(
        0x73747874,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 7364696D - 0000 - 0010 - 8000 - 00AA00389B71 'mids' == MEDIATYPE_Midi
    MEDIATYPE_Midi = OUR_GUID_ENTRY(
        0x7364696D,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # e436eb83 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIATYPE_Stream
    MEDIATYPE_Stream = OUR_GUID_ENTRY(
        0xE436EB83,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # 73(s)76(v)61(a)69(i) - 0000 - 0010 - 8000 - 00AA00389B71 'iavs' ==
    # MEDIATYPE_Interleaved
    MEDIATYPE_Interleaved = OUR_GUID_ENTRY(
        0x73766169,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 656c6966 - 0000 - 0010 - 8000 - 00AA00389B71 'file' == MEDIATYPE_File
    MEDIATYPE_File = OUR_GUID_ENTRY(
        0x656C6966,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 73636d64 - 0000 - 0010 - 8000 - 00AA00389B71 'scmd' ==
    # MEDIATYPE_ScriptCommand
    MEDIATYPE_ScriptCommand = OUR_GUID_ENTRY(
        0x73636D64,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 670AEA80 - 3A82 - 11d0 - B79B - 00AA003767A7  MEDIATYPE_AUXLine21Data
    MEDIATYPE_AUXLine21Data = OUR_GUID_ENTRY(
        0x670AEA80,
        0x3A82,
        0x11D0,
        0xB7,
        0x9B,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x67,
        0xA7
    )

    # {11264ACB - 37DE - 4eba - 8C35 - 7F04A1A68332}
    MEDIATYPE_AUXTeletextPage = OUR_GUID_ENTRY(
        0x11264ACB,
        0x37DE,
        0x4EBA,
        0x8C,
        0x35,
        0x7F,
        0x4,
        0xA1,
        0xA6,
        0x83,
        0x32
    )

    # AEB312E9 - 3357 - 43ca - B701 - 97EC198E2B62  MEDIATYPE_CC_CONTAINER
    MEDIATYPE_CC_CONTAINER = OUR_GUID_ENTRY(
        0xAEB312E9,
        0x3357,
        0x43CA,
        0xB7,
        0x1,
        0x97,
        0xEC,
        0x19,
        0x8E,
        0x2B,
        0x62
    )

    # FB77E152 - 53B2 - 499c - B46B - 509FC33EDFD7   MEDIATYPE_DTVCCData
    MEDIATYPE_DTVCCData = OUR_GUID_ENTRY(
        0xFB77E152,
        0x53B2,
        0x499C,
        0xB4,
        0x6B,
        0x50,
        0x9F,
        0xC3,
        0x3E,
        0xDF,
        0xD7
    )

    # B88B8A89 - B049 - 4C80 - ADCF - 5898985E22C1   MEDIATYPE_MSTVCaption
    MEDIATYPE_MSTVCaption = OUR_GUID_ENTRY(
        0xB88B8A89,
        0xB049,
        0x4C80,
        0xAD,
        0xCF,
        0x58,
        0x98,
        0x98,
        0x5E,
        0x22,
        0xC1
    )

    # F72A76E1 - EB0A - 11D0 - ACE4 - 0000C0CC16BA  MEDIATYPE_VBI
    MEDIATYPE_VBI = OUR_GUID_ENTRY(
        0xF72A76E1,
        0xEB0A,
        0x11D0,
        0xAC,
        0xE4,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # 34FFCBC3 - D5B3 - 4171 - 9002 - D4C60301697F   DVB_SUBTITLES
    MEDIASUBTYPE_DVB_SUBTITLES = OUR_GUID_ENTRY(
        0x34FFCBC3,
        0xD5B3,
        0x4171,
        0x90,
        0x02,
        0xD4,
        0xC6,
        0x03,
        0x01,
        0x69,
        0x7F
    )

    # 059DD67D - 2E55 - 4d41 - 8D1B - 01F5E4F50607  ISDB_CAPTIONS
    MEDIASUBTYPE_ISDB_CAPTIONS = OUR_GUID_ENTRY(
        0x059DD67D,
        0x2E55,
        0x4D41,
        0x8D,
        0x1B,
        0x01,
        0xF5,
        0xE4,
        0xF5,
        0x06,
        0x07
    )

    # 36dc6d28 - f1a6 - 4216 - 9048 - 9cfcefeb5eba  ISDB_SUPERIMPOSE
    MEDIASUBTYPE_ISDB_SUPERIMPOSE = OUR_GUID_ENTRY(
        0x36DC6D28,
        0xF1A6,
        0x4216,
        0x90,
        0x48,
        0x9C,
        0xFC,
        0xEF,
        0xEB,
        0x5E,
        0xBA
    )

    # 0482DEE3 - 7817 - 11cf - 8a03 - 00aa006ecb65  MEDIATYPE_Timecode
    MEDIATYPE_Timecode = OUR_GUID_ENTRY(
        0x482DEE3,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 74726c6d - 0000 - 0010 - 8000 - 00AA00389B71 'lmrt' == MEDIATYPE_LMRT
    MEDIATYPE_LMRT = OUR_GUID_ENTRY(
        0x74726C6D,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 74726c6d - 0000 - 0010 - 8000 - 00AA00389B71 'urls' ==
    # MEDIATYPE_URL_STREAM
    MEDIATYPE_URL_STREAM = OUR_GUID_ENTRY(
        0x736C7275,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # - - sub types - - -
    # 4C504C43 - 0000 - 0010 - 8000 - 00AA00389B71 'CLPL' == MEDIASUBTYPE_CLPL
    MEDIASUBTYPE_CLPL = OUR_GUID_ENTRY(
        0x4C504C43,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 56595559 - 0000 - 0010 - 8000 - 00AA00389B71 'YUYV' == MEDIASUBTYPE_YUYV
    MEDIASUBTYPE_YUYV = OUR_GUID_ENTRY(
        0x56595559,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 56555949 - 0000 - 0010 - 8000 - 00AA00389B71 'IYUV' == MEDIASUBTYPE_IYUV
    MEDIASUBTYPE_IYUV = OUR_GUID_ENTRY(
        0x56555949,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 39555659 - 0000 - 0010 - 8000 - 00AA00389B71 'YVU9' == MEDIASUBTYPE_YVU9
    MEDIASUBTYPE_YVU9 = OUR_GUID_ENTRY(
        0x39555659,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 31313459 - 0000 - 0010 - 8000 - 00AA00389B71 'Y411' == MEDIASUBTYPE_Y411
    MEDIASUBTYPE_Y411 = OUR_GUID_ENTRY(
        0x31313459,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 50313459 - 0000 - 0010 - 8000 - 00AA00389B71 'Y41P' == MEDIASUBTYPE_Y41P
    MEDIASUBTYPE_Y41P = OUR_GUID_ENTRY(
        0x50313459,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 32595559 - 0000 - 0010 - 8000 - 00AA00389B71 'YUY2' == MEDIASUBTYPE_YUY2
    MEDIASUBTYPE_YUY2 = OUR_GUID_ENTRY(
        0x32595559,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 55595659 - 0000 - 0010 - 8000 - 00AA00389B71 'YVYU' == MEDIASUBTYPE_YVYU
    MEDIASUBTYPE_YVYU = OUR_GUID_ENTRY(
        0x55595659,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 59565955 - 0000 - 0010 - 8000 - 00AA00389B71 'UYVY' == MEDIASUBTYPE_UYVY
    MEDIASUBTYPE_UYVY = OUR_GUID_ENTRY(
        0x59565955,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 31313259 - 0000 - 0010 - 8000 - 00AA00389B71 'Y211' == MEDIASUBTYPE_Y211
    MEDIASUBTYPE_Y211 = OUR_GUID_ENTRY(
        0x31313259,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 524a4c43 - 0000 - 0010 - 8000 - 00AA00389B71 'CLJR' == MEDIASUBTYPE_CLJR
    MEDIASUBTYPE_CLJR = OUR_GUID_ENTRY(
        0x524A4C43,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 39304649 - 0000 - 0010 - 8000 - 00AA00389B71 'IF09' == MEDIASUBTYPE_IF09
    MEDIASUBTYPE_IF09 = OUR_GUID_ENTRY(
        0x39304649,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 414c5043 - 0000 - 0010 - 8000 - 00AA00389B71 'CPLA' == MEDIASUBTYPE_CPLA
    MEDIASUBTYPE_CPLA = OUR_GUID_ENTRY(
        0x414C5043,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 47504A4D - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_MJPG
    MEDIASUBTYPE_MJPG = OUR_GUID_ENTRY(
        0x47504A4D,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 4A4D5654 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_TVMJ
    MEDIASUBTYPE_TVMJ = OUR_GUID_ENTRY(
        0x4A4D5654,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 454B4157 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_WAKE
    MEDIASUBTYPE_WAKE = OUR_GUID_ENTRY(
        0x454B4157,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 43434643 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_CFCC
    MEDIASUBTYPE_CFCC = OUR_GUID_ENTRY(
        0x43434643,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 47504A49 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_IJPG
    MEDIASUBTYPE_IJPG = OUR_GUID_ENTRY(
        0x47504A49,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 6D756C50 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_Plum
    MEDIASUBTYPE_Plum = OUR_GUID_ENTRY(
        0x6D756C50,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # FAST DV - Master
    # 53435644 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_DVCS
    MEDIASUBTYPE_DVCS = OUR_GUID_ENTRY(
        0x53435644,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # H.264 compressed video stream
    # 34363248 - 0000 - 0010 - 8000 - 00AA00389B71 'H264' == MEDIASUBTYPE_H264
    MEDIASUBTYPE_H264 = OUR_GUID_ENTRY(
        0x34363248,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # FAST DV - Master
    # 44535644 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_DVSD
    MEDIASUBTYPE_DVSD = OUR_GUID_ENTRY(
        0x44535644,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # MIROVideo DV
    # 4656444D - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_MDVF
    MEDIASUBTYPE_MDVF = OUR_GUID_ENTRY(
        0x4656444D,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # e436eb78 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB1
    # e436eb78 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB1
    MEDIASUBTYPE_RGB1 = OUR_GUID_ENTRY(
        0xE436EB78,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb79 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB4
    MEDIASUBTYPE_RGB4 = OUR_GUID_ENTRY(
        0xE436EB79,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb7a - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB8
    MEDIASUBTYPE_RGB8 = OUR_GUID_ENTRY(
        0xE436EB7A,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb7b - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB565
    MEDIASUBTYPE_RGB565 = OUR_GUID_ENTRY(
        0xE436EB7B,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb7c - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB555
    MEDIASUBTYPE_RGB555 = OUR_GUID_ENTRY(
        0xE436EB7C,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb7d - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB24
    MEDIASUBTYPE_RGB24 = OUR_GUID_ENTRY(
        0xE436EB7D,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb7e - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_RGB32
    MEDIASUBTYPE_RGB32 = OUR_GUID_ENTRY(
        0xE436EB7E,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # RGB surfaces that contain per pixel alpha values.
    # 297C55AF - E209 - 4cb3 - B757 - C76D6B9C88A8  MEDIASUBTYPE_ARGB1555
    MEDIASUBTYPE_ARGB1555 = OUR_GUID_ENTRY(
        0x297C55AF,
        0xE209,
        0x4CB3,
        0xB7,
        0x57,
        0xC7,
        0x6D,
        0x6B,
        0x9C,
        0x88,
        0xA8
    )

    # 6E6415E6 - 5C24 - 425f - 93CD - 80102B3D1CCA  MEDIASUBTYPE_ARGB4444
    MEDIASUBTYPE_ARGB4444 = OUR_GUID_ENTRY(
        0x6E6415E6,
        0x5C24,
        0x425F,
        0x93,
        0xCD,
        0x80,
        0x10,
        0x2B,
        0x3D,
        0x1C,
        0xCA
    )

    # 773c9ac0 - 3274 - 11d0 - B724 - 00aa006c1A01  MEDIASUBTYPE_ARGB32
    MEDIASUBTYPE_ARGB32 = OUR_GUID_ENTRY(
        0x773C9AC0,
        0x3274,
        0x11D0,
        0xB7,
        0x24,
        0x0,
        0xAA,
        0x0,
        0x6C,
        0x1A,
        0x1
    )

    # 2f8bb76d - b644 - 4550 - acf3 - d30caa65d5c5  MEDIASUBTYPE_A2R10G10B10
    MEDIASUBTYPE_A2R10G10B10 = OUR_GUID_ENTRY(
        0x2F8BB76D,
        0xB644,
        0x4550,
        0xAC,
        0xF3,
        0xD3,
        0x0C,
        0xAA,
        0x65,
        0xD5,
        0xC5
    )

    # 576f7893 - bdf6 - 48c4 - 875f - ae7b81834567  MEDIASUBTYPE_A2B10G10R10
    MEDIASUBTYPE_A2B10G10R10 = OUR_GUID_ENTRY(
        0x576F7893,
        0xBDF6,
        0x48C4,
        0x87,
        0x5F,
        0xAE,
        0x7B,
        0x81,
        0x83,
        0x45,
        0x67
    )

    # 56555941 - 0000 - 0010 - 8000 - 00AA00389B71 'AYUV' == MEDIASUBTYPE_AYUV
    # See the DX - VA header and documentation for a description of this
    # format.
    MEDIASUBTYPE_AYUV = OUR_GUID_ENTRY(
        0x56555941,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 34344941 - 0000 - 0010 - 8000 - 00AA00389B71 'AI44' == MEDIASUBTYPE_AI44
    # See the DX - VA header and documentation for a description of this
    # format.
    MEDIASUBTYPE_AI44 = OUR_GUID_ENTRY(
        0x34344941,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 34344149 - 0000 - 0010 - 8000 - 00AA00389B71 'IA44' == MEDIASUBTYPE_IA44
    # See the DX - VA header and documentation for a description of this
    # format.
    MEDIASUBTYPE_IA44 = OUR_GUID_ENTRY(
        0x34344149,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # DirectX7 D3D Render Target media subtypes.
    # 32335237 - 0000 - 0010 - 8000 - 00AA00389B71 '7R32' ==
    # MEDIASUBTYPE_RGB32_D3D_DX7_RT
    MEDIASUBTYPE_RGB32_D3D_DX7_RT = OUR_GUID_ENTRY(
        0x32335237,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 36315237 - 0000 - 0010 - 8000 - 00AA00389B71 '7R16' ==
    # MEDIASUBTYPE_RGB16_D3D_DX7_RT
    MEDIASUBTYPE_RGB16_D3D_DX7_RT = OUR_GUID_ENTRY(
        0x36315237,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38384137 - 0000 - 0010 - 8000 - 00AA00389B71 '7A88' ==
    # MEDIASUBTYPE_ARGB32_D3D_DX7_RT
    MEDIASUBTYPE_ARGB32_D3D_DX7_RT = OUR_GUID_ENTRY(
        0x38384137,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 34344137 - 0000 - 0010 - 8000 - 00AA00389B71 '7A44' ==
    # MEDIASUBTYPE_ARGB4444_D3D_DX7_RT
    MEDIASUBTYPE_ARGB4444_D3D_DX7_RT = OUR_GUID_ENTRY(
        0x34344137,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 35314137 - 0000 - 0010 - 8000 - 00AA00389B71 '7A15' ==
    # MEDIASUBTYPE_ARGB1555_D3D_DX7_RT
    MEDIASUBTYPE_ARGB1555_D3D_DX7_RT = OUR_GUID_ENTRY(
        0x35314137,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # DirectX9 D3D Render Target media subtypes.
    # 32335239 - 0000 - 0010 - 8000 - 00AA00389B71 '9R32' ==
    # MEDIASUBTYPE_RGB32_D3D_DX9_RT
    MEDIASUBTYPE_RGB32_D3D_DX9_RT = OUR_GUID_ENTRY(
        0x32335239,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 36315239 - 0000 - 0010 - 8000 - 00AA00389B71 '9R16' ==
    # MEDIASUBTYPE_RGB16_D3D_DX9_RT
    MEDIASUBTYPE_RGB16_D3D_DX9_RT = OUR_GUID_ENTRY(
        0x36315239,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38384139 - 0000 - 0010 - 8000 - 00AA00389B71 '9A88' ==
    # MEDIASUBTYPE_ARGB32_D3D_DX9_RT
    MEDIASUBTYPE_ARGB32_D3D_DX9_RT = OUR_GUID_ENTRY(
        0x38384139,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 34344139 - 0000 - 0010 - 8000 - 00AA00389B71 '9A44' ==
    # MEDIASUBTYPE_ARGB4444_D3D_DX9_RT
    MEDIASUBTYPE_ARGB4444_D3D_DX9_RT = OUR_GUID_ENTRY(
        0x34344139,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 35314139 - 0000 - 0010 - 8000 - 00AA00389B71 '9A15' ==
    # MEDIASUBTYPE_ARGB1555_D3D_DX9_RT
    MEDIASUBTYPE_ARGB1555_D3D_DX9_RT = OUR_GUID_ENTRY(
        0x35314139,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )


    def MEDIASUBTYPE_HASALPHA(mt):
        return mt.subtype in (
            MEDIASUBTYPE_ARGB4444,
            MEDIASUBTYPE_ARGB32,
            MEDIASUBTYPE_AYUV,
            MEDIASUBTYPE_AI44,
            MEDIASUBTYPE_IA44,
            MEDIASUBTYPE_ARGB1555,
            MEDIASUBTYPE_ARGB32_D3D_DX7_RT,
            MEDIASUBTYPE_ARGB4444_D3D_DX7_RT,
            MEDIASUBTYPE_ARGB1555_D3D_DX7_RT,
            MEDIASUBTYPE_ARGB32_D3D_DX9_RT,
            MEDIASUBTYPE_ARGB4444_D3D_DX9_RT,
            MEDIASUBTYPE_ARGB1555_D3D_DX9_RT
        )


    def MEDIASUBTYPE_HASALPHA7(mt):
        return mt.subtype in (
            MEDIASUBTYPE_ARGB32_D3D_DX7_RT,
            MEDIASUBTYPE_ARGB4444_D3D_DX7_RT,
            MEDIASUBTYPE_ARGB1555_D3D_DX7_RT
        )


    def MEDIASUBTYPE_D3D_DX7_RT(mt):
        return mt.subtype in (
            MEDIASUBTYPE_ARGB32_D3D_DX7_RT,
            MEDIASUBTYPE_ARGB4444_D3D_DX7_RT,
            MEDIASUBTYPE_ARGB1555_D3D_DX7_RT,
            MEDIASUBTYPE_RGB32_D3D_DX7_RT,
            MEDIASUBTYPE_RGB16_D3D_DX7_RT
        )


    def MEDIASUBTYPE_HASALPHA9(mt):
        return mt.subtype in (
            MEDIASUBTYPE_ARGB32_D3D_DX9_RT,
            MEDIASUBTYPE_ARGB4444_D3D_DX9_RT,
            MEDIASUBTYPE_ARGB1555_D3D_DX9_RT
        )


    def MEDIASUBTYPE_D3D_DX9_RT(mt):
        return mt.subtype in (
            MEDIASUBTYPE_ARGB32_D3D_DX9_RT,
            MEDIASUBTYPE_ARGB4444_D3D_DX9_RT,
            MEDIASUBTYPE_ARGB1555_D3D_DX9_RT,
            MEDIASUBTYPE_RGB32_D3D_DX9_RT,
            MEDIASUBTYPE_RGB16_D3D_DX9_RT
        )

    # DX - VA uncompressed surface formats
    # 32315659 - 0000 - 0010 - 8000 - 00AA00389B71 'YV12' == MEDIASUBTYPE_YV12
    MEDIASUBTYPE_YV12 = OUR_GUID_ENTRY(
        0x32315659,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 3231564E - 0000 - 0010 - 8000 - 00AA00389B71 'NV12' == MEDIASUBTYPE_NV12
    MEDIASUBTYPE_NV12 = OUR_GUID_ENTRY(
        0x3231564E,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 3131564E - 0000 - 0010 - 8000 - 00AA00389B71 'NV11' == MEDIASUBTYPE_NV11

    MEDIASUBTYPE_NV11_DEFINED = None
    if not defined(MEDIASUBTYPE_NV11_DEFINED):
        MEDIASUBTYPE_NV11_DEFINED = 1
        MEDIASUBTYPE_NV11 = OUR_GUID_ENTRY(
            0x3131564E,
            0x0000,
            0x0010,
            0x80,
            0x00,
            0x00,
            0xAA,
            0x00,
            0x38,
            0x9B,
            0x71
        )
    # END IF
    # 38303250 - 0000 - 0010 - 8000 - 00AA00389B71 'P208' == MEDIASUBTYPE_P208
    MEDIASUBTYPE_P208 = OUR_GUID_ENTRY(
        0x38303250,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38303250 - 0000 - 0010 - 8000 - 00AA00389B71 'P210' == MEDIASUBTYPE_P210
    MEDIASUBTYPE_P210 = OUR_GUID_ENTRY(
        0x38303250,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38303250 - 0000 - 0010 - 8000 - 00AA00389B71 'P216' == MEDIASUBTYPE_P216
    MEDIASUBTYPE_P216 = OUR_GUID_ENTRY(
        0x38303250,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38303250 - 0000 - 0010 - 8000 - 00AA00389B71 'P010' == MEDIASUBTYPE_P010
    MEDIASUBTYPE_P010 = OUR_GUID_ENTRY(
        0x38303250,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38303250 - 0000 - 0010 - 8000 - 00AA00389B71 'P016' == MEDIASUBTYPE_P016
    MEDIASUBTYPE_P016 = OUR_GUID_ENTRY(
        0x38303250,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38303250 - 0000 - 0010 - 8000 - 00AA00389B71 'Y210' == MEDIASUBTYPE_Y210
    MEDIASUBTYPE_Y210 = OUR_GUID_ENTRY(
        0x38303250,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38303250 - 0000 - 0010 - 8000 - 00AA00389B71 'Y216' == MEDIASUBTYPE_Y216
    MEDIASUBTYPE_Y216 = OUR_GUID_ENTRY(
        0x38303250,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 38303450 - 0000 - 0010 - 8000 - 00AA00389B71 'P408' == MEDIASUBTYPE_P408
    MEDIASUBTYPE_P408 = OUR_GUID_ENTRY(
        0x38303450,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 3432564E - 0000 - 0010 - 8000 - 00AA00389B71 'NV24' == MEDIASUBTYPE_NV24
    MEDIASUBTYPE_NV24 = OUR_GUID_ENTRY(
        0x3432564E,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 4F303234 - 0000 - 0010 - 8000 - 00AA00389B71 '420O' == MEDIASUBTYPE_420O
    MEDIASUBTYPE_420O = OUR_GUID_ENTRY(
        0x4F303234,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 31434D49 - 0000 - 0010 - 8000 - 00AA00389B71 'IMC1' == MEDIASUBTYPE_IMC1
    MEDIASUBTYPE_IMC1 = OUR_GUID_ENTRY(
        0x31434D49,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 32434d49 - 0000 - 0010 - 8000 - 00AA00389B71 'IMC2' == MEDIASUBTYPE_IMC2
    MEDIASUBTYPE_IMC2 = OUR_GUID_ENTRY(
        0x32434D49,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 33434d49 - 0000 - 0010 - 8000 - 00AA00389B71 'IMC3' == MEDIASUBTYPE_IMC3
    MEDIASUBTYPE_IMC3 = OUR_GUID_ENTRY(
        0x33434D49,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 34434d49 - 0000 - 0010 - 8000 - 00AA00389B71 'IMC4' == MEDIASUBTYPE_IMC4
    MEDIASUBTYPE_IMC4 = OUR_GUID_ENTRY(
        0x34434D49,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 30343353 - 0000 - 0010 - 8000 - 00AA00389B71 'S340' == MEDIASUBTYPE_S340
    MEDIASUBTYPE_S340 = OUR_GUID_ENTRY(
        0x30343353,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 32343353 - 0000 - 0010 - 8000 - 00AA00389B71 'S342' == MEDIASUBTYPE_S342
    MEDIASUBTYPE_S342 = OUR_GUID_ENTRY(
        0x32343353,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # e436eb7f - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_Overlay
    MEDIASUBTYPE_Overlay = OUR_GUID_ENTRY(
        0xE436EB7F,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb80 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_MPEGPacket
    MEDIASUBTYPE_MPEG1Packet = OUR_GUID_ENTRY(
        0xE436EB80,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb81 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_MPEG1Payload
    MEDIASUBTYPE_MPEG1Payload = OUR_GUID_ENTRY(
        0xE436EB81,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # 00000050 - 0000 - 0010 - 8000 - 00AA00389B71
    # MEDIASUBTYPE_MPEG1AudioPayload
    MEDIASUBTYPE_MPEG1AudioPayload = OUR_GUID_ENTRY(
        0x00000050,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # e436eb82 - 524f - 11ce - 9f53 - 0020af0ba770
    # MEDIASUBTYPE_MPEG1SystemStream
    MEDIATYPE_MPEG1SystemStream = OUR_GUID_ENTRY(
        0xE436EB82,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # the next consecutive number is asINT to MEDIATYPE_Stream and appears
    # higher up
    # e436eb84 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_MPEG1System
    MEDIASUBTYPE_MPEG1System = OUR_GUID_ENTRY(
        0xE436EB84,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb85 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_MPEG1VideoCD
    MEDIASUBTYPE_MPEG1VideoCD = OUR_GUID_ENTRY(
        0xE436EB85,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb86 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_MPEG1Video
    MEDIASUBTYPE_MPEG1Video = OUR_GUID_ENTRY(
        0xE436EB86,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb87 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_MPEG1Audio
    MEDIASUBTYPE_MPEG1Audio = OUR_GUID_ENTRY(
        0xE436EB87,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb88 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_Avi
    MEDIASUBTYPE_Avi = OUR_GUID_ENTRY(
        0xE436EB88,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # {3DB80F90 - 9412 - 11d1 - ADED - 0000F8754B99}  MEDIASUBTYPE_Asf
    MEDIASUBTYPE_Asf = OUR_GUID_ENTRY(
        0x3DB80F90,
        0x9412,
        0x11D1,
        0xAD,
        0xED,
        0x0,
        0x0,
        0xF8,
        0x75,
        0x4B,
        0x99
    )

    # e436eb89 - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_QTMovie
    MEDIASUBTYPE_QTMovie = OUR_GUID_ENTRY(
        0xE436EB89,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # 617a7072 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_Rpza
    MEDIASUBTYPE_QTRpza = OUR_GUID_ENTRY(
        0x617A7072,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 20636d73 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_Smc
    MEDIASUBTYPE_QTSmc = OUR_GUID_ENTRY(
        0x20636D73,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 20656c72 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_Rle
    MEDIASUBTYPE_QTRle = OUR_GUID_ENTRY(
        0x20656C72,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 6765706a - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_Jpeg
    MEDIASUBTYPE_QTJpeg = OUR_GUID_ENTRY(
        0x6765706A,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # e436eb8a - 524f - 11ce - 9f53 - 0020af0ba770
    # MEDIASUBTYPE_PCMAudio_Obsolete
    MEDIASUBTYPE_PCMAudio_Obsolete = OUR_GUID_ENTRY(
        0xE436EB8A,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # 00000001 - 0000 - 0010 - 8000 - 00AA00389B71  MEDIASUBTYPE_PCM
    MEDIASUBTYPE_PCM = OUR_GUID_ENTRY(
        0x00000001,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # e436eb8b - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_WAVE
    MEDIASUBTYPE_WAVE = OUR_GUID_ENTRY(
        0xE436EB8B,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb8c - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_AU
    MEDIASUBTYPE_AU = OUR_GUID_ENTRY(
        0xE436EB8C,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436eb8d - 524f - 11ce - 9f53 - 0020af0ba770  MEDIASUBTYPE_AIFF
    MEDIASUBTYPE_AIFF = OUR_GUID_ENTRY(
        0xE436EB8D,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # 64(d)73(s)76(v)64(d) - 0000 - 0010 - 8000 - 00AA00389B71 'dvsd' ==
    # MEDIASUBTYPE_dvsd
    MEDIASUBTYPE_dvsd = OUR_GUID_ENTRY(
        0x64737664,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 64(d)68(h)76(v)64(d) - 0000 - 0010 - 8000 - 00AA00389B71 'dvhd' ==
    # MEDIASUBTYPE_dvhd
    MEDIASUBTYPE_dvhd = OUR_GUID_ENTRY(
        0x64687664,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 6c(l)73(s)76(v)64(d) - 0000 - 0010 - 8000 - 00AA00389B71 'dvsl' ==
    # MEDIASUBTYPE_dvsl
    MEDIASUBTYPE_dvsl = OUR_GUID_ENTRY(
        0x6C737664,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 35(5)32(2)76(v)64(d) - 0000 - 0010 - 8000 - 00AA00389B71 'dv25' ==
    # MEDIASUBTYPE_dv25
    MEDIASUBTYPE_dv25 = OUR_GUID_ENTRY(
        0x35327664,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 30(0)35(5)76(v)64(d) - 0000 - 0010 - 8000 - 00AA00389B71 'dv50' ==
    # MEDIASUBTYPE_dv50
    MEDIASUBTYPE_dv50 = OUR_GUID_ENTRY(
        0x30357664,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 31(1)68(h)76(v)64(d) - 0000 - 0010 - 8000 - 00AA00389B71 'dvh1' ==
    # MEDIASUBTYPE_dvh1
    MEDIASUBTYPE_dvh1 = OUR_GUID_ENTRY(
        0x31687664,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # 6E8D4A22 - 310C - 11d0 - B79A - 00AA003767A7
    # MEDIASUBTYPE_Line21_BytePair
    MEDIASUBTYPE_Line21_BytePair = OUR_GUID_ENTRY(
        0x6E8D4A22,
        0x310C,
        0x11D0,
        0xB7,
        0x9A,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x67,
        0xA7
    )

    # 6E8D4A23 - 310C - 11d0 - B79A - 00AA003767A7
    # MEDIASUBTYPE_Line21_GOPPacket
    MEDIASUBTYPE_Line21_GOPPacket = OUR_GUID_ENTRY(
        0x6E8D4A23,
        0x310C,
        0x11D0,
        0xB7,
        0x9A,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x67,
        0xA7
    )

    # 6E8D4A24 - 310C - 11d0 - B79A - 00AA003767A7
    # MEDIASUBTYPE_Line21_VBIRawData
    MEDIASUBTYPE_Line21_VBIRawData = OUR_GUID_ENTRY(
        0x6E8D4A24,
        0x310C,
        0x11D0,
        0xB7,
        0x9A,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x67,
        0xA7
    )

    # 0AF414BC - 4ED2 - 445e - 9839 - 8F095568AB3C  MEDIASUBTYPE_708_608Data
    MEDIASUBTYPE_708_608Data = OUR_GUID_ENTRY(
        0xAF414BC,
        0x4ED2,
        0x445E,
        0x98,
        0x39,
        0x8F,
        0x9,
        0x55,
        0x68,
        0xAB,
        0x3C
    )

    # F52ADDAA - 36F0 - 43F5 - 95EA - 6D866484262A  MEDIASUBTYPE_DtvCcData
    MEDIASUBTYPE_DtvCcData = OUR_GUID_ENTRY(
        0xF52ADDAA,
        0x36F0,
        0x43F5,
        0x95,
        0xEA,
        0x6D,
        0x86,
        0x64,
        0x84,
        0x26,
        0x2A
    )

    # 7EA626DB - 54DA - 437b - BE9F - F73073ADFA3C  MEDIASUBTYPE_CC_CONTAINER
    MEDIASUBTYPE_CC_CONTAINER = OUR_GUID_ENTRY(
        0x7EA626DB,
        0x54DA,
        0x437B,
        0xBE,
        0x9F,
        0xF7,
        0x30,
        0x73,
        0xAD,
        0xFA,
        0x3C
    )

    # F72A76E3 - EB0A - 11D0 - ACE4 - 0000C0CC16BA  MEDIASUBTYPE_TELETEXT
    MEDIASUBTYPE_TELETEXT = OUR_GUID_ENTRY(
        0xF72A76E3,
        0xEB0A,
        0x11D0,
        0xAC,
        0xE4,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # 663DA43C - 03E8 - 4e9a - 9CD5 - BF11ED0DEF76  MEDIASUBTYPE_VBI
    MEDIASUBTYPE_VBI = OUR_GUID_ENTRY(
        0x663DA43C,
        0x3E8,
        0x4E9A,
        0x9C,
        0xD5,
        0xBF,
        0x11,
        0xED,
        0xD,
        0xEF,
        0x76
    )

    # 2791D576 - 8E7A - 466F - 9E90 - 5D3F3083738B  MEDIASUBTYPE_WSS
    MEDIASUBTYPE_WSS = OUR_GUID_ENTRY(
        0x2791D576,
        0x8E7A,
        0x466F,
        0x9E,
        0x90,
        0x5D,
        0x3F,
        0x30,
        0x83,
        0x73,
        0x8B
    )

    # 01CA73E3 - DCE6 - 4575 - AFE1 - 2BF1C902CAF3  MEDIASUBTYPE_XDS
    MEDIASUBTYPE_XDS = OUR_GUID_ENTRY(
        0x1CA73E3,
        0xDCE6,
        0x4575,
        0xAF,
        0xE1,
        0x2B,
        0xF1,
        0xC9,
        0x2,
        0xCA,
        0xF3
    )

    # A1B3F620 - 9792 - 4d8d - 81A4 - 86AF25772090  MEDIASUBTYPE_VPS
    MEDIASUBTYPE_VPS = OUR_GUID_ENTRY(
        0xA1B3F620,
        0x9792,
        0x4D8D,
        0x81,
        0xA4,
        0x86,
        0xAF,
        0x25,
        0x77,
        0x20,
        0x90
    )

    # derived from WAVE_FORMAT_DRM
    # 00000009 - 0000 - 0010 - 8000 - 00aa00389b71
    MEDIASUBTYPE_DRM_Audio = OUR_GUID_ENTRY(
        0x00000009,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # derived from WAVE_FORMAT_IEEE_FLOAT
    # 00000003 - 0000 - 0010 - 8000 - 00aa00389b71
    MEDIASUBTYPE_IEEE_FLOAT = OUR_GUID_ENTRY(
        0x00000003,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # derived from WAVE_FORMAT_DOLBY_AC3_SPDIF
    # 00000092 - 0000 - 0010 - 8000 - 00aa00389b71
    MEDIASUBTYPE_DOLBY_AC3_SPDIF = OUR_GUID_ENTRY(
        0x00000092,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # derived from WAVE_FORMAT_RAW_SPORT
    # 00000240 - 0000 - 0010 - 8000 - 00aa00389b71
    MEDIASUBTYPE_RAW_SPORT = OUR_GUID_ENTRY(
        0x00000240,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # derived from wave format tag 0x241, call it SPDIF_TAG_241h for now
    # 00000241 - 0000 - 0010 - 8000 - 00aa00389b71
    MEDIASUBTYPE_SPDIF_TAG_241h = OUR_GUID_ENTRY(
        0x00000241,
        0x0000,
        0x0010,
        0x80,
        0x00,
        0x00,
        0xAA,
        0x00,
        0x38,
        0x9B,
        0x71
    )

    # DirectShow DSS definitions
    # A0AF4F81 - E163 - 11d0 - BAD9 - 00609744111A
    MEDIASUBTYPE_DssVideo = OUR_GUID_ENTRY(
        0xA0AF4F81,
        0xE163,
        0x11D0,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # A0AF4F82 - E163 - 11d0 - BAD9 - 00609744111A
    MEDIASUBTYPE_DssAudio = OUR_GUID_ENTRY(
        0xA0AF4F82,
        0xE163,
        0x11D0,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # 5A9B6A40 - 1A22 - 11D1 - BAD9 - 00609744111A
    MEDIASUBTYPE_VPVideo = OUR_GUID_ENTRY(
        0x5A9B6A40,
        0x1A22,
        0x11D1,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # 5A9B6A41 - 1A22 - 11D1 - BAD9 - 00609744111A
    MEDIASUBTYPE_VPVBI = OUR_GUID_ENTRY(
        0x5A9B6A41,
        0x1A22,
        0x11D1,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # BF87B6E0 - 8C27 - 11d0 - B3F0 - 00AA003761C5  Capture graph building
    CLSID_CaptureGraphBuilder = OUR_GUID_ENTRY(
        0xBF87B6E0,
        0x8C27,
        0x11D0,
        0xB3,
        0xF0,
        0x0,
        0xAA,
        0x00,
        0x37,
        0x61,
        0xC5
    )

    # BF87B6E1 - 8C27 - 11d0 - B3F0 - 00AA003761C5  New Capture graph building
    CLSID_CaptureGraphBuilder2 = OUR_GUID_ENTRY(
        0xBF87B6E1,
        0x8C27,
        0x11D0,
        0xB3,
        0xF0,
        0x0,
        0xAA,
        0x00,
        0x37,
        0x61,
        0xC5
    )

    # e436ebb0 - 524f - 11ce - 9f53 - 0020af0ba770  Prototype filtergraph
    CLSID_ProtoFilterGraph = OUR_GUID_ENTRY(
        0xE436EBB0,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436ebb1 - 524f - 11ce - 9f53 - 0020af0ba770  Reference clock
    CLSID_SystemClock = OUR_GUID_ENTRY(
        0xE436EBB1,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436ebb2 - 524f - 11ce - 9f53 - 0020af0ba770   Filter Mapper
    CLSID_FilterMapper = OUR_GUID_ENTRY(
        0xE436EBB2,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436ebb3 - 524f - 11ce - 9f53 - 0020af0ba770   Filter Graph
    CLSID_FilterGraph = OUR_GUID_ENTRY(
        0xE436EBB3,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # e436ebb8 - 524f - 11ce - 9f53 - 0020af0ba770   Filter Graph no thread
    CLSID_FilterGraphNoThread = OUR_GUID_ENTRY(
        0xE436EBB8,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # a3ecbc41 - 581a - 4476 - b693 - a63340462d8b
    CLSID_FilterGraphPrivateThread = OUR_GUID_ENTRY(
        0xA3ECBC41,
        0x581A,
        0x4476,
        0xB6,
        0x93,
        0xA6,
        0x33,
        0x40,
        0x46,
        0x2D,
        0x8B
    )

    # e4bbd160 - 4269 - 11ce - 838d - 00aa0055595a   MPEG System stream
    CLSID_MPEG1Doc = OUR_GUID_ENTRY(
        0xE4BBD160,
        0x4269,
        0x11CE,
        0x83,
        0x8D,
        0x0,
        0xAA,
        0x0,
        0x55,
        0x59,
        0x5A
    )

    # 701722e0 - 8ae3 - 11ce - a85c - 00aa002feab5   MPEG file reader
    CLSID_FileSource = OUR_GUID_ENTRY(
        0x701722E0,
        0x8AE3,
        0x11CE,
        0xA8,
        0x5C,
        0x00,
        0xAA,
        0x00,
        0x2F,
        0xEA,
        0xB5
    )

    # 26C25940 - 4CA9 - 11ce - A828 - 00AA002FEAB5   Takes MPEG1 packets as
    # input
    CLSID_MPEG1PacketPlayer = OUR_GUID_ENTRY(
        0x26C25940,
        0x4CA9,
        0x11CE,
        0xA8,
        0x28,
        0x0,
        0xAA,
        0x0,
        0x2F,
        0xEA,
        0xB5
    )

    # 336475d0 - 942a - 11ce - a870 - 00aa002feab5   MPEG splitter
    CLSID_MPEG1Splitter = OUR_GUID_ENTRY(
        0x336475D0,
        0x942A,
        0x11CE,
        0xA8,
        0x70,
        0x00,
        0xAA,
        0x00,
        0x2F,
        0xEA,
        0xB5
    )

    # feb50740 - 7bef - 11ce - 9bd9 - 0000e202599c   MPEG video decoder
    CLSID_CMpegVideoCodec = OUR_GUID_ENTRY(
        0xFEB50740,
        0x7BEF,
        0x11CE,
        0x9B,
        0xD9,
        0x0,
        0x0,
        0xE2,
        0x2,
        0x59,
        0x9C
    )

    # 4a2286e0 - 7bef - 11ce - 9bd9 - 0000e202599c   MPEG audio decoder
    CLSID_CMpegAudioCodec = OUR_GUID_ENTRY(
        0x4A2286E0,
        0x7BEF,
        0x11CE,
        0x9B,
        0xD9,
        0x0,
        0x0,
        0xE2,
        0x2,
        0x59,
        0x9C
    )

    # e30629d3 - 27e5 - 11ce - 875d - 00608cb78066   Text renderer
    CLSID_TextRender = OUR_GUID_ENTRY(
        0xE30629D3,
        0x27E5,
        0x11CE,
        0x87,
        0x5D,
        0x0,
        0x60,
        0x8C,
        0xB7,
        0x80,
        0x66
    )

    # {F8388A40 - D5BB - 11d0 - BE5A - 0080C706568E}
    CLSID_InfTee = OUR_GUID_ENTRY(
        0xF8388A40,
        0xD5BB,
        0x11D0,
        0xBE,
        0x5A,
        0x0,
        0x80,
        0xC7,
        0x6,
        0x56,
        0x8E
    )

    # 1b544c20 - fd0b - 11ce - 8c63 - 00aa0044b51e   Avi Stream Splitter
    CLSID_AviSplitter = OUR_GUID_ENTRY(
        0x1B544C20,
        0xFD0B,
        0x11CE,
        0x8C,
        0x63,
        0x0,
        0xAA,
        0x00,
        0x44,
        0xB5,
        0x1E
    )

    # 1b544c21 - fd0b - 11ce - 8c63 - 00aa0044b51e   Avi File Reader
    CLSID_AviReader = OUR_GUID_ENTRY(
        0x1B544C21,
        0xFD0B,
        0x11CE,
        0x8C,
        0x63,
        0x0,
        0xAA,
        0x00,
        0x44,
        0xB5,
        0x1E
    )

    # 1b544c22 - fd0b - 11ce - 8c63 - 00aa0044b51e   Vfw 2.0 Capture Driver
    CLSID_VfwCapture = OUR_GUID_ENTRY(
        0x1B544C22,
        0xFD0B,
        0x11CE,
        0x8C,
        0x63,
        0x0,
        0xAA,
        0x00,
        0x44,
        0xB5,
        0x1E
    )
    CLSID_CaptureProperties = OUR_GUID_ENTRY(
        0x1B544C22,
        0xFD0B,
        0x11CE,
        0x8C,
        0x63,
        0x00,
        0xAA,
        0x00,
        0x44,
        0xB5,
        0x1F
    )

    # e436ebb4 - 524f - 11ce - 9f53 - 0020af0ba770  Control Distributor
    CLSID_FGControl = OUR_GUID_ENTRY(
        0xE436EBB4,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # 44584800 - F8EE - 11ce - B2D4 - 00DD01101B85   .MOV reader (old)
    CLSID_MOVReader = OUR_GUID_ENTRY(
        0x44584800,
        0xF8EE,
        0x11CE,
        0xB2,
        0xD4,
        0x00,
        0xDD,
        0x1,
        0x10,
        0x1B,
        0x85
    )

    # D51BD5A0 - 7548 - 11cf - A520 - 0080C77EF58A   QT Splitter
    CLSID_QuickTimeParser = OUR_GUID_ENTRY(
        0xD51BD5A0,
        0x7548,
        0x11CF,
        0xA5,
        0x20,
        0x0,
        0x80,
        0xC7,
        0x7E,
        0xF5,
        0x8A
    )

    # FDFE9681 - 74A3 - 11d0 - AFA7 - 00AA00B67A42   QT Decoder
    CLSID_QTDec = OUR_GUID_ENTRY(
        0xFDFE9681,
        0x74A3,
        0x11D0,
        0xAF,
        0xA7,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # D3588AB0 - 0781 - 11ce - B03A - 0020AF0BA770   AVIFile - based reader
    CLSID_AVIDoc = OUR_GUID_ENTRY(
        0xD3588AB0,
        0x0781,
        0x11CE,
        0xB0,
        0x3A,
        0x00,
        0x20,
        0xAF,
        0xB,
        0xA7,
        0x70
    )

    # 70e102b0 - 5556 - 11ce - 97c0 - 00aa0055595a   Video renderer
    CLSID_VideoRenderer = OUR_GUID_ENTRY(
        0x70E102B0,
        0x5556,
        0x11CE,
        0x97,
        0xC0,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # 1643e180 - 90f5 - 11ce - 97d5 - 00aa0055595a   Colour space convertor
    CLSID_Colour = OUR_GUID_ENTRY(
        0x1643E180,
        0x90F5,
        0x11CE,
        0x97,
        0xD5,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # 1da08500 - 9edc - 11cf - bc10 - 00aa00ac74f6   VGA 16 color ditherer
    CLSID_Dither = OUR_GUID_ENTRY(
        0x1DA08500,
        0x9EDC,
        0x11CF,
        0xBC,
        0x10,
        0x00,
        0xAA,
        0x00,
        0xAC,
        0x74,
        0xF6
    )

    # 07167665 - 5011 - 11cf - BF33 - 00AA0055595A   Modex video renderer
    CLSID_ModexRenderer = OUR_GUID_ENTRY(
        0x7167665,
        0x5011,
        0x11CF,
        0xBF,
        0x33,
        0x0,
        0xAA,
        0x0,
        0x55,
        0x59,
        0x5A
    )

    # e30629d1 - 27e5 - 11ce - 875d - 00608cb78066   Waveout audio renderer
    CLSID_AudioRender = OUR_GUID_ENTRY(
        0xE30629D1,
        0x27E5,
        0x11CE,
        0x87,
        0x5D,
        0x0,
        0x60,
        0x8C,
        0xB7,
        0x80,
        0x66
    )

    # 05589faf - c356 - 11ce - bf01 - 00aa0055595a   Audio Renderer Property
    # Page
    CLSID_AudioProperties = OUR_GUID_ENTRY(
        0x05589FAF,
        0xC356,
        0x11CE,
        0xBF,
        0x01,
        0x0,
        0xAA,
        0x0,
        0x55,
        0x59,
        0x5A
    )

    # 79376820 - 07D0 - 11cf - A24D - 0020AFD79767   DSound audio renderer
    CLSID_DSoundRender = OUR_GUID_ENTRY(
        0x79376820,
        0x07D0,
        0x11CF,
        0xA2,
        0x4D,
        0x0,
        0x20,
        0xAF,
        0xD7,
        0x97,
        0x67
    )

    # e30629d2 - 27e5 - 11ce - 875d - 00608cb78066   Wavein audio recorder
    CLSID_AudioRecord = OUR_GUID_ENTRY(
        0xE30629D2,
        0x27E5,
        0x11CE,
        0x87,
        0x5D,
        0x0,
        0x60,
        0x8C,
        0xB7,
        0x80,
        0x66
    )

    # {2CA8CA52 - 3C3F - 11d2 - B73D - 00C04FB6BD3D}  IAMAudioInputMixer
    # property page
    CLSID_AudioInputMixerProperties = OUR_GUID_ENTRY(
        0x2CA8CA52,
        0x3C3F,
        0x11D2,
        0xB7,
        0x3D,
        0x0,
        0xC0,
        0x4F,
        0xB6,
        0xBD,
        0x3D
    )

    # {CF49D4E0 - 1115 - 11ce - B03A - 0020AF0BA770}  AVI Decoder
    CLSID_AVIDec = OUR_GUID_ENTRY(
        0xCF49D4E0,
        0x1115,
        0x11CE,
        0xB0,
        0x3A,
        0x0,
        0x20,
        0xAF,
        0xB,
        0xA7,
        0x70
    )

    # {A888DF60 - 1E90 - 11cf - AC98 - 00AA004C0FA9}  AVI ICDraw* wrapper
    CLSID_AVIDraw = OUR_GUID_ENTRY(
        0xA888DF60,
        0x1E90,
        0x11CF,
        0xAC,
        0x98,
        0x0,
        0xAA,
        0x0,
        0x4C,
        0xF,
        0xA9
    )

    # 6a08cf80 - 0e18 - 11cf - a24d - 0020afd79767  ACM Wrapper
    CLSID_ACMWrapper = OUR_GUID_ENTRY(
        0x6A08CF80,
        0x0E18,
        0x11CF,
        0xA2,
        0x4D,
        0x0,
        0x20,
        0xAF,
        0xD7,
        0x97,
        0x67
    )

    # {e436ebb5 - 524f - 11ce - 9f53 - 0020af0ba770} Async File Reader
    CLSID_AsyncReader = OUR_GUID_ENTRY(
        0xE436EBB5,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # {e436ebb6 - 524f - 11ce - 9f53 - 0020af0ba770} Async URL Reader
    CLSID_URLReader = OUR_GUID_ENTRY(
        0xE436EBB6,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # {e436ebb7 - 524f - 11ce - 9f53 - 0020af0ba770} IPersistMoniker PID
    CLSID_PersistMonikerPID = OUR_GUID_ENTRY(
        0xE436EBB7,
        0x524F,
        0x11CE,
        0x9F,
        0x53,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0xA7,
        0x70
    )

    # {D76E2820 - 1563 - 11cf - AC98 - 00AA004C0FA9}
    CLSID_AVICo = OUR_GUID_ENTRY(
        0xD76E2820,
        0x1563,
        0x11CF,
        0xAC,
        0x98,
        0x0,
        0xAA,
        0x0,
        0x4C,
        0xF,
        0xA9
    )

    # {8596E5F0 - 0DA5 - 11d0 - BD21 - 00A0C911CE86}
    CLSID_FileWriter = OUR_GUID_ENTRY(
        0x8596E5F0,
        0xDA5,
        0x11D0,
        0xBD,
        0x21,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # {E2510970 - F137 - 11CE - 8B67 - 00AA00A3F1A6}  AVI mux filter
    CLSID_AviDest = OUR_GUID_ENTRY(
        0xE2510970,
        0xF137,
        0x11CE,
        0x8B,
        0x67,
        0x0,
        0xAA,
        0x0,
        0xA3,
        0xF1,
        0xA6
    )

    # {C647B5C0 - 157C - 11d0 - BD23 - 00A0C911CE86}
    CLSID_AviMuxProptyPage = OUR_GUID_ENTRY(
        0xC647B5C0,
        0x157C,
        0x11D0,
        0xBD,
        0x23,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # {0A9AE910 - 85C0 - 11d0 - BD42 - 00A0C911CE86}
    CLSID_AviMuxProptyPage1 = OUR_GUID_ENTRY(
        0xA9AE910,
        0x85C0,
        0x11D0,
        0xBD,
        0x42,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # {07b65360 - c445 - 11ce - afde - 00aa006c14f4}
    CLSID_AVIMIDIRender = OUR_GUID_ENTRY(
        0x07B65360,
        0xC445,
        0x11CE,
        0xAF,
        0xDE,
        0x00,
        0xAA,
        0x00,
        0x6C,
        0x14,
        0xF4
    )

    # {187463A0 - 5BB7 - 11d3 - ACBE - 0080C75E246E} WMSDK - based ASF reader
    CLSID_WMAsfReader = OUR_GUID_ENTRY(
        0x187463A0,
        0x5BB7,
        0x11D3,
        0xAC,
        0xBE,
        0x0,
        0x80,
        0xC7,
        0x5E,
        0x24,
        0x6E
    )

    # {7c23220e - 55bb - 11d3 - 8b16 - 00c04fb6bd3d} WMSDK - based ASF writer
    CLSID_WMAsfWriter = OUR_GUID_ENTRY(
        0x7C23220E,
        0x55BB,
        0x11D3,
        0x8B,
        0x16,
        0x0,
        0xC0,
        0x4F,
        0xB6,
        0xBD,
        0x3D
    )

    # {afb6c280 - 2c41 - 11d3 - 8a60 - 0000f81e0e4a}
    CLSID_MPEG2Demultiplexer = OUR_GUID_ENTRY(
        0xAFB6C280,
        0x2C41,
        0x11D3,
        0x8A,
        0x60,
        0x00,
        0x00,
        0xF8,
        0x1E,
        0x0E,
        0x4A
    )

    # {687D3367 - 3644 - 467a - ADFE - 6CD7A85C4A2C}
    CLSID_MPEG2Demultiplexer_NoClock = OUR_GUID_ENTRY(
        0x687D3367,
        0x3644,
        0x467A,
        0xAD,
        0xFE,
        0x6C,
        0xD7,
        0xA8,
        0x5C,
        0x4A,
        0x2C
    )

    # {3ae86b20 - 7be8 - 11d1 - abe6 - 00a0c905f375}
    CLSID_MMSPLITTER = OUR_GUID_ENTRY(
        0x3AE86B20,
        0x7BE8,
        0x11D1,
        0xAB,
        0xE6,
        0x00,
        0xA0,
        0xC9,
        0x05,
        0xF3,
        0x75
    )

    # {2DB47AE5 - CF39 - 43c2 - B4D6 - 0CD8D90946F4}
    CLSID_StreamBufferSink = OUR_GUID_ENTRY(
        0x2DB47AE5,
        0xCF39,
        0x43C2,
        0xB4,
        0xD6,
        0xC,
        0xD8,
        0xD9,
        0x9,
        0x46,
        0xF4
    )

    # {E2448508 - 95DA - 4205 - 9A27 - 7EC81E723B1A}
    CLSID_SBE2Sink = OUR_GUID_ENTRY(
        0xE2448508,
        0x95DA,
        0x4205,
        0x9A,
        0x27,
        0x7E,
        0xC8,
        0x1E,
        0x72,
        0x3B,
        0x1A
    )

    # {C9F5FE02 - F851 - 4eb5 - 99EE - AD602AF1E619}
    CLSID_StreamBufferSource = OUR_GUID_ENTRY(
        0xC9F5FE02,
        0xF851,
        0x4EB5,
        0x99,
        0xEE,
        0xAD,
        0x60,
        0x2A,
        0xF1,
        0xE6,
        0x19
    )

    # {FA8A68B2 - C864 - 4ba2 - AD53 - D3876A87494B}
    CLSID_StreamBufferConfig = OUR_GUID_ENTRY(
        0xFA8A68B2,
        0xC864,
        0x4BA2,
        0xAD,
        0x53,
        0xD3,
        0x87,
        0x6A,
        0x87,
        0x49,
        0x4B
    )

    # {E37A73F8 - FB01 - 43dc - 914E - AAEE76095AB9}
    CLSID_StreamBufferPropertyHandler = OUR_GUID_ENTRY(
        0xE37A73F8,
        0xFB01,
        0x43DC,
        0x91,
        0x4E,
        0xAA,
        0xEE,
        0x76,
        0x9,
        0x5A,
        0xB9
    )

    # {713790EE - 5EE1 - 45ba - 8070 - A1337D2762FA}
    CLSID_StreamBufferThumbnailHandler = OUR_GUID_ENTRY(
        0x713790EE,
        0x5EE1,
        0x45BA,
        0x80,
        0x70,
        0xA1,
        0x33,
        0x7D,
        0x27,
        0x62,
        0xFA
    )

    # {6CFAD761 - 735D - 4aa5 - 8AFC - AF91A7D61EBA}
    CLSID_Mpeg2VideoStreamAnalyzer = OUR_GUID_ENTRY(
        0x6CFAD761,
        0x735D,
        0x4AA5,
        0x8A,
        0xFC,
        0xAF,
        0x91,
        0xA7,
        0xD6,
        0x1E,
        0xBA
    )

    # {CCAA63AC - 1057 - 4778 - AE92 - 1206AB9ACEE6}
    CLSID_StreamBufferRecordingAttributes = OUR_GUID_ENTRY(
        0xCCAA63AC,
        0x1057,
        0x4778,
        0xAE,
        0x92,
        0x12,
        0x6,
        0xAB,
        0x9A,
        0xCE,
        0xE6
    )

    # {D682C4BA - A90A - 42fe - B9E1 - 03109849C423}
    CLSID_StreamBufferComposeRecording = OUR_GUID_ENTRY(
        0xD682C4BA,
        0xA90A,
        0x42FE,
        0xB9,
        0xE1,
        0x3,
        0x10,
        0x98,
        0x49,
        0xC4,
        0x23
    )

    # {93A094D7 - 51E8 - 485b - 904A - 8D6B97DC6B39}
    CLSID_SBE2File = OUR_GUID_ENTRY(
        0x93A094D7,
        0x51E8,
        0x485B,
        0x90,
        0x4A,
        0x8D,
        0x6B,
        0x97,
        0xDC,
        0x6B,
        0x39
    )

    # {B1B77C00 - C3E4 - 11cf - AF79 - 00AA00B67A42}   DV video decoder
    CLSID_DVVideoCodec = OUR_GUID_ENTRY(
        0xB1B77C00,
        0xC3E4,
        0x11CF,
        0xAF,
        0x79,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # {13AA3650 - BB6F - 11d0 - AFB9 - 00AA00B67A42}   DV video encoder
    CLSID_DVVideoEnc = OUR_GUID_ENTRY(
        0x13AA3650,
        0xBB6F,
        0x11D0,
        0xAF,
        0xB9,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # {4EB31670 - 9FC6 - 11cf - AF6E - 00AA00B67A42}   DV splitter
    CLSID_DVSplitter = OUR_GUID_ENTRY(
        0x4EB31670,
        0x9FC6,
        0x11CF,
        0xAF,
        0x6E,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # {129D7E40 - C10D - 11d0 - AFB9 - 00AA00B67A42}   DV muxer
    CLSID_DVMux = OUR_GUID_ENTRY(
        0x129D7E40,
        0xC10D,
        0x11D0,
        0xAF,
        0xB9,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # {060AF76C - 68DD - 11d0 - 8FC1 - 00C04FD9189D}
    CLSID_SeekingPassThru = OUR_GUID_ENTRY(
        0x60AF76C,
        0x68DD,
        0x11D0,
        0x8F,
        0xC1,
        0x0,
        0xC0,
        0x4F,
        0xD9,
        0x18,
        0x9D
    )

    # 6E8D4A20 - 310C - 11d0 - B79A - 00AA003767A7    Line21 (CC) Decoder
    CLSID_Line21Decoder = OUR_GUID_ENTRY(
        0x6E8D4A20,
        0x310C,
        0x11D0,
        0xB7,
        0x9A,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x67,
        0xA7
    )

    # E4206432 - 01A1 - 4BEE - B3E1 - 3702C8EDC574    Line21 (CC) Decoder v2
    CLSID_Line21Decoder2 = OUR_GUID_ENTRY(
        0xE4206432,
        0x01A1,
        0x4BEE,
        0xB3,
        0xE1,
        0x37,
        0x02,
        0xC8,
        0xED,
        0xC5,
        0x74
    )
    CLSID_CCAFilter = OUR_GUID_ENTRY(
        0x3D07A539,
        0x35CA,
        0x447C,
        0x9B,
        0x5,
        0x8D,
        0x85,
        0xCE,
        0x92,
        0x4F,
        0x9E
    )

    # {CD8743A1 - 3736 - 11d0 - 9E69 - 00C04FD7C15B}
    CLSID_OverlayMixer = OUR_GUID_ENTRY(
        0xCD8743A1,
        0x3736,
        0x11D0,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {814B9800 - 1C88 - 11d1 - BAD9 - 00609744111A}
    CLSID_VBISurfaces = OUR_GUID_ENTRY(
        0x814B9800,
        0x1C88,
        0x11D1,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # {70BC06E0 - 5666 - 11d3 - A184 - 00105AEF9F33}   WST Teletext Decoder
    CLSID_WSTDecoder = OUR_GUID_ENTRY(
        0x70BC06E0,
        0x5666,
        0x11D3,
        0xA1,
        0x84,
        0x0,
        0x10,
        0x5A,
        0xEF,
        0x9F,
        0x33
    )

    # {301056D0 - 6DFF - 11d2 - 9EEB - 006008039E37}
    CLSID_MjpegDec = OUR_GUID_ENTRY(
        0x301056D0,
        0x6DFF,
        0x11D2,
        0x9E,
        0xEB,
        0x0,
        0x60,
        0x8,
        0x3,
        0x9E,
        0x37
    )

    # {B80AB0A0 - 7416 - 11d2 - 9EEB - 006008039E37}
    CLSID_MJPGEnc = OUR_GUID_ENTRY(
        0xB80AB0A0,
        0x7416,
        0x11D2,
        0x9E,
        0xEB,
        0x0,
        0x60,
        0x8,
        0x3,
        0x9E,
        0x37
    )

    # pnp objects and categories
    # 62BE5D10 - 60EB - 11d0 - BD3B - 00A0C911CE86    ICreateDevEnum
    CLSID_SystemDeviceEnum = OUR_GUID_ENTRY(
        0x62BE5D10,
        0x60EB,
        0x11D0,
        0xBD,
        0x3B,
        0x00,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 4315D437 - 5B8C - 11d0 - BD3B - 00A0C911CE86
    CLSID_CDeviceMoniker = OUR_GUID_ENTRY(
        0x4315D437,
        0x5B8C,
        0x11D0,
        0xBD,
        0x3B,
        0x00,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 860BB310 - 5D01 - 11d0 - BD3B - 00A0C911CE86    Video capture category
    CLSID_VideoInputDeviceCategory = OUR_GUID_ENTRY(
        0x860BB310,
        0x5D01,
        0x11D0,
        0xBD,
        0x3B,
        0x00,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )
    CLSID_CVidCapClassManager = OUR_GUID_ENTRY(
        0x860BB310,
        0x5D01,
        0x11D0,
        0xBD,
        0x3B,
        0x00,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 083863F1 - 70DE - 11d0 - BD40 - 00A0C911CE86    Filter category
    CLSID_LegacyAmFilterCategory = OUR_GUID_ENTRY(
        0x083863F1,
        0x70DE,
        0x11D0,
        0xBD,
        0x40,
        0x00,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )
    CLSID_CQzFilterClassManager = OUR_GUID_ENTRY(
        0x083863F1,
        0x70DE,
        0x11D0,
        0xBD,
        0x40,
        0x00,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 33D9A760 - 90C8 - 11d0 - BD43 - 00A0C911CE86
    CLSID_VideoCompressorCategory = OUR_GUID_ENTRY(
        0x33D9A760,
        0x90C8,
        0x11D0,
        0xBD,
        0x43,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )
    CLSID_CIcmCoClassManager = OUR_GUID_ENTRY(
        0x33D9A760,
        0x90C8,
        0x11D0,
        0xBD,
        0x43,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 33D9A761 - 90C8 - 11d0 - BD43 - 00A0C911CE86
    CLSID_AudioCompressorCategory = OUR_GUID_ENTRY(
        0x33D9A761,
        0x90C8,
        0x11D0,
        0xBD,
        0x43,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )
    CLSID_CAcmCoClassManager = OUR_GUID_ENTRY(
        0x33D9A761,
        0x90C8,
        0x11D0,
        0xBD,
        0x43,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 33D9A762 - 90C8 - 11d0 - BD43 - 00A0C911CE86    Audio source cateogry
    CLSID_AudioInputDeviceCategory = OUR_GUID_ENTRY(
        0x33D9A762,
        0x90C8,
        0x11D0,
        0xBD,
        0x43,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )
    CLSID_CWaveinClassManager = OUR_GUID_ENTRY(
        0x33D9A762,
        0x90C8,
        0x11D0,
        0xBD,
        0x43,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # E0F158E1 - CB04 - 11d0 - BD4E - 00A0C911CE86    Audio renderer category
    CLSID_AudioRendererCategory = OUR_GUID_ENTRY(
        0xE0F158E1,
        0xCB04,
        0x11D0,
        0xBD,
        0x4E,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )
    CLSID_CWaveOutClassManager = OUR_GUID_ENTRY(
        0xE0F158E1,
        0xCB04,
        0x11D0,
        0xBD,
        0x4E,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 4EFE2452 - 168A - 11d1 - BC76 - 00C04FB9453B    Midi renderer category
    CLSID_MidiRendererCategory = OUR_GUID_ENTRY(
        0x4EFE2452,
        0x168A,
        0x11D1,
        0xBC,
        0x76,
        0x0,
        0xC0,
        0x4F,
        0xB9,
        0x45,
        0x3B
    )
    CLSID_CMidiOutClassManager = OUR_GUID_ENTRY(
        0x4EFE2452,
        0x168A,
        0x11D1,
        0xBC,
        0x76,
        0x0,
        0xC0,
        0x4F,
        0xB9,
        0x45,
        0x3B
    )

    # CC7BFB41 - F175 - 11d1 - A392 - 00E0291F3959  External Renderers Category
    CLSID_TransmitCategory = OUR_GUID_ENTRY(
        0xCC7BFB41,
        0xF175,
        0x11D1,
        0xA3,
        0x92,
        0x0,
        0xE0,
        0x29,
        0x1F,
        0x39,
        0x59
    )

    # CC7BFB46 - F175 - 11d1 - A392 - 00E0291F3959  Device Control Filters
    CLSID_DeviceControlCategory = OUR_GUID_ENTRY(
        0xCC7BFB46,
        0xF175,
        0x11D1,
        0xA3,
        0x92,
        0x0,
        0xE0,
        0x29,
        0x1F,
        0x39,
        0x59
    )

    # DA4E3DA0 - D07D - 11d0 - BD50 - 00A0C911CE86
    CLSID_ActiveMovieCategories = OUR_GUID_ENTRY(
        0xDA4E3DA0,
        0xD07D,
        0x11D0,
        0xBD,
        0x50,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 2721AE20 - 7E70 - 11D0 - A5D6 - 28DB04C10000
    CLSID_DVDHWDecodersCategory = OUR_GUID_ENTRY(
        0x2721AE20,
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

    # 7D22E920 - 5CA9 - 4787 - 8C2B - A6779BD11781  Encoder API encoder
    # category
    CLSID_MediaEncoderCategory = OUR_GUID_ENTRY(
        0x7D22E920,
        0x5CA9,
        0x4787,
        0x8C,
        0x2B,
        0xA6,
        0x77,
        0x9B,
        0xD1,
        0x17,
        0x81
    )

    # 236C9559 - ADCE - 4736 - BF72 - BAB34E392196  Encoder API multiplexer
    # category
    CLSID_MediaMultiplexerCategory = OUR_GUID_ENTRY(
        0x236C9559,
        0xADCE,
        0x4736,
        0xBF,
        0x72,
        0xBA,
        0xB3,
        0x4E,
        0x39,
        0x21,
        0x96
    )

    # CDA42200 - BD88 - 11d0 - BD4E - 00A0C911CE86
    CLSID_FilterMapper2 = OUR_GUID_ENTRY(
        0xCDA42200,
        0xBD88,
        0x11D0,
        0xBD,
        0x4E,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # 1e651cc0 - b199 - 11d0 - 8212 - 00c04fc32c45
    CLSID_MemoryAllocator = OUR_GUID_ENTRY(
        0x1E651CC0,
        0xB199,
        0x11D0,
        0x82,
        0x12,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x2C,
        0x45
    )

    # CDBD8D00 - C193 - 11d0 - BD4E - 00A0C911CE86
    CLSID_MediaPropertyBag = OUR_GUID_ENTRY(
        0xCDBD8D00,
        0xC193,
        0x11D0,
        0xBD,
        0x4E,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0xCE,
        0x86
    )

    # FCC152B7 - F372 - 11d0 - 8E00 - 00C04FD7C08B
    CLSID_DvdGraphBuilder = OUR_GUID_ENTRY(
        0xFCC152B7,
        0xF372,
        0x11D0,
        0x8E,
        0x00,
        0x00,
        0xC0,
        0x4F,
        0xD7,
        0xC0,
        0x8B
    )

    # 9B8C4620 - 2C1A - 11d0 - 8493 - 00A02438AD48
    CLSID_DVDNavigator = OUR_GUID_ENTRY(
        0x9B8C4620,
        0x2C1A,
        0x11D0,
        0x84,
        0x93,
        0x0,
        0xA0,
        0x24,
        0x38,
        0xAD,
        0x48
    )

    # f963c5cf - a659 - 4a93 - 9638 - caf3cd277d13
    CLSID_DVDState = OUR_GUID_ENTRY(
        0xF963C5CF,
        0xA659,
        0x4A93,
        0x96,
        0x38,
        0xCA,
        0xF3,
        0xCD,
        0x27,
        0x7D,
        0x13
    )

    # CC58E280 - 8AA1 - 11d1 - B3F1 - 00AA003761C5
    CLSID_SmartTee = OUR_GUID_ENTRY(
        0xCC58E280,
        0x8AA1,
        0x11D1,
        0xB3,
        0xF1,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x61,
        0xC5
    )

    # FB056BA0 - 2502 - 45B9 - 8E86 - 2B40DE84AD29
    CLSID_DtvCcFilter = OUR_GUID_ENTRY(
        0xFB056BA0,
        0x2502,
        0x45B9,
        0x8E,
        0x86,
        0x2B,
        0x40,
        0xDE,
        0x84,
        0xAD,
        0x29
    )

    # 2F7EE4B6 - 6FF5 - 4EB4 - B24A - 2BFC41117171
    CLSID_CaptionsFilter = OUR_GUID_ENTRY(
        0x2F7EE4B6,
        0x6FF5,
        0x4EB4,
        0xB2,
        0x4A,
        0x2B,
        0xFC,
        0x41,
        0x11,
        0x71,
        0x71
    )

    # {9F22CFEA - CE07 - 41ab - 8BA0 - C7364AF90AF9}
    CLSID_SubtitlesFilter = OUR_GUID_ENTRY(
        0x9F22CFEA,
        0xCE07,
        0x41AB,
        0x8B,
        0xA0,
        0xC7,
        0x36,
        0x4A,
        0xF9,
        0x0A,
        0xF9
    )

    # {8670C736 - F614 - 427b - 8ADA - BBADC587194B}
    CLSID_DirectShowPluginControl = OUR_GUID_ENTRY(
        0x8670C736,
        0xF614,
        0x427B,
        0x8A,
        0xDA,
        0xBB,
        0xAD,
        0xC5,
        0x87,
        0x19,
        0x4B
    )

    # - - format types - - -
    # 0F6417D6 - C318 - 11D0 - A43F - 00A0C9223196  FORMAT_None
    FORMAT_None = OUR_GUID_ENTRY(
        0x0F6417D6,
        0xC318,
        0x11D0,
        0xA4,
        0x3F,
        0x00,
        0xA0,
        0xC9,
        0x22,
        0x31,
        0x96
    )

    # 05589f80 - c356 - 11ce - bf01 - 00aa0055595a  FORMAT_VideoInfo
    FORMAT_VideoInfo = OUR_GUID_ENTRY(
        0x05589F80,
        0xC356,
        0x11CE,
        0xBF,
        0x01,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # F72A76A0 - EB0A - 11d0 - ACE4 - 0000C0CC16BA  FORMAT_VideoInfo2
    FORMAT_VideoInfo2 = OUR_GUID_ENTRY(
        0xF72A76A0,
        0xEB0A,
        0x11D0,
        0xAC,
        0xE4,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # 05589f81 - c356 - 11ce - bf01 - 00aa0055595a  FORMAT_WaveFormatEx
    FORMAT_WaveFormatEx = OUR_GUID_ENTRY(
        0x05589F81,
        0xC356,
        0x11CE,
        0xBF,
        0x01,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # 05589f82 - c356 - 11ce - bf01 - 00aa0055595a  FORMAT_MPEGVideo
    FORMAT_MPEGVideo = OUR_GUID_ENTRY(
        0x05589F82,
        0xC356,
        0x11CE,
        0xBF,
        0x01,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # 05589f83 - c356 - 11ce - bf01 - 00aa0055595a  FORMAT_MPEGStreams
    FORMAT_MPEGStreams = OUR_GUID_ENTRY(
        0x05589F83,
        0xC356,
        0x11CE,
        0xBF,
        0x01,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # 05589f84 - c356 - 11ce - bf01 - 00aa0055595a  FORMAT_DvInfo, DVINFO
    FORMAT_DvInfo = OUR_GUID_ENTRY(
        0x05589F84,
        0xC356,
        0x11CE,
        0xBF,
        0x01,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # C7ECF04D - 4582 - 4869 - 9ABB - BFB523B62EDF  FORMAT_525WSS
    FORMAT_525WSS = OUR_GUID_ENTRY(
        0xC7ECF04D,
        0x4582,
        0x4869,
        0x9A,
        0xBB,
        0xBF,
        0xB5,
        0x23,
        0xB6,
        0x2E,
        0xDF
    )

    # - - Video related GUIDs - - -
    # 944d4c00 - dd52 - 11ce - bf0e - 00aa0055595a
    CLSID_DirectDrawProperties = OUR_GUID_ENTRY(
        0x944D4C00,
        0xDD52,
        0x11CE,
        0xBF,
        0x0E,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # 59ce6880 - acf8 - 11cf - b56e - 0080c7c4b68a
    CLSID_PerformanceProperties = OUR_GUID_ENTRY(
        0x59CE6880,
        0xACF8,
        0x11CF,
        0xB5,
        0x6E,
        0x00,
        0x80,
        0xC7,
        0xC4,
        0xB6,
        0x8A
    )

    # 418afb70 - f8b8 - 11ce - aac6 - 0020af0b99a3
    CLSID_QualityProperties = OUR_GUID_ENTRY(
        0x418AFB70,
        0xF8B8,
        0x11CE,
        0xAA,
        0xC6,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0x99,
        0xA3
    )

    # 61ded640 - e912 - 11ce - a099 - 00aa00479a58
    IID_IBaseVideoMixer = OUR_GUID_ENTRY(
        0x61DED640,
        0xE912,
        0x11CE,
        0xA0,
        0x99,
        0x00,
        0xAA,
        0x00,
        0x47,
        0x9A,
        0x58
    )

    # 36d39eb0 - dd75 - 11ce - bf0e - 00aa0055595a
    IID_IDirectDrawVideo = OUR_GUID_ENTRY(
        0x36D39EB0,
        0xDD75,
        0x11CE,
        0xBF,
        0x0E,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # bd0ecb0 - f8e2 - 11ce - aac6 - 0020af0b99a3
    IID_IQualProp = OUR_GUID_ENTRY(
        0x1BD0ECB0,
        0xF8E2,
        0x11CE,
        0xAA,
        0xC6,
        0x00,
        0x20,
        0xAF,
        0x0B,
        0x99,
        0xA3
    )

    # {CE292861 - FC88 - 11d0 - 9E69 - 00C04FD7C15B}
    CLSID_VPObject = OUR_GUID_ENTRY(
        0xCE292861,
        0xFC88,
        0x11D0,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {CE292862 - FC88 - 11d0 - 9E69 - 00C04FD7C15B}
    IID_IVPObject = OUR_GUID_ENTRY(
        0xCE292862,
        0xFC88,
        0x11D0,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {25DF12C1 - 3DE0 - 11d1 - 9E69 - 00C04FD7C15B}
    IID_IVPControl = OUR_GUID_ENTRY(
        0x25DF12C1,
        0x3DE0,
        0x11D1,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {814B9801 - 1C88 - 11d1 - BAD9 - 00609744111A}
    CLSID_VPVBIObject = OUR_GUID_ENTRY(
        0x814B9801,
        0x1C88,
        0x11D1,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # {814B9802 - 1C88 - 11d1 - BAD9 - 00609744111A}
    IID_IVPVBIObject = OUR_GUID_ENTRY(
        0x814B9802,
        0x1C88,
        0x11D1,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # {BC29A660 - 30E3 - 11d0 - 9E69 - 00C04FD7C15B}
    IID_IVPConfig = OUR_GUID_ENTRY(
        0xBC29A660,
        0x30E3,
        0x11D0,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {C76794A1 - D6C5 - 11d0 - 9E69 - 00C04FD7C15B}
    IID_IVPNotify = OUR_GUID_ENTRY(
        0xC76794A1,
        0xD6C5,
        0x11D0,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {EBF47183 - 8764 - 11d1 - 9E69 - 00C04FD7C15B}
    IID_IVPNotify2 = OUR_GUID_ENTRY(
        0xEBF47183,
        0x8764,
        0x11D1,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {EC529B00 - 1A1F - 11D1 - BAD9 - 00609744111A}
    IID_IVPVBIConfig = OUR_GUID_ENTRY(
        0xEC529B00,
        0x1A1F,
        0x11D1,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # {EC529B01 - 1A1F - 11D1 - BAD9 - 00609744111A}
    IID_IVPVBINotify = OUR_GUID_ENTRY(
        0xEC529B01,
        0x1A1F,
        0x11D1,
        0xBA,
        0xD9,
        0x0,
        0x60,
        0x97,
        0x44,
        0x11,
        0x1A
    )

    # {593CDDE1 - 0759 - 11d1 - 9E69 - 00C04FD7C15B}
    IID_IMixerPinConfig = OUR_GUID_ENTRY(
        0x593CDDE1,
        0x759,
        0x11D1,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # {EBF47182 - 8764 - 11d1 - 9E69 - 00C04FD7C15B}
    IID_IMixerPinConfig2 = OUR_GUID_ENTRY(
        0xEBF47182,
        0x8764,
        0x11D1,
        0x9E,
        0x69,
        0x0,
        0xC0,
        0x4F,
        0xD7,
        0xC1,
        0x5B
    )

    # This is a real pain in the neck. The OLE GUIDs are separated out into a
    # different file from the main header files. The header files can then be
    # included multiple times and are protected with the following statements,
    # ifndef __SOMETHING_DEFINED__
    # define __SOMETHING_DEFINED__
    # all the header contents
    # endif // __SOMETHING_DEFINED__
    # When the actual GUIDs are to be defined (using initguid) the GUID header
    # file can then be included to really define them just once. Unfortunately
    # DirectDraw has the GUIDs defined in the main header file. So if the base
    # classes bring in ddraw.h to get at the DirectDraw structures and so on
    # nobody would then be able to really include ddraw.h to allocate the GUID
    # memory structures because of the aforementioned header file protection
    # Therefore the DirectDraw GUIDs are defined and allocated for real here

    __DDRAW_INCLUDED__ = None
    if not defined(__DDRAW_INCLUDED__):
        CLSID_DirectDraw = OUR_GUID_ENTRY(
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
        CLSID_DirectDrawClipper = OUR_GUID_ENTRY(
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
        IID_IDirectDraw = OUR_GUID_ENTRY(
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
        IID_IDirectDraw2 = OUR_GUID_ENTRY(
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
        IID_IDirectDrawSurface = OUR_GUID_ENTRY(
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
        IID_IDirectDrawSurface2 = OUR_GUID_ENTRY(
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
        IID_IDirectDrawSurface3 = OUR_GUID_ENTRY(
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
        IID_IDirectDrawSurface4 = OUR_GUID_ENTRY(
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
        IID_IDirectDrawSurface7 = OUR_GUID_ENTRY(
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
        IID_IDirectDrawPalette = OUR_GUID_ENTRY(
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
        IID_IDirectDrawClipper = OUR_GUID_ENTRY(
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
        IID_IDirectDrawColorControl = OUR_GUID_ENTRY(
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
    # END IF

    __DVP_INCLUDED__ = None
    if not defined(__DVP_INCLUDED__):
        IID_IDDVideoPortContainer = OUR_GUID_ENTRY(
            0x6C142760,
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
    # END IF

    __DDKM_INCLUDED__ = None
    if not defined(__DDKM_INCLUDED__):
        IID_IDirectDrawKernel = OUR_GUID_ENTRY(
            0x8D56C120,
            0x6A08,
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
        IID_IDirectDrawSurfaceKernel = OUR_GUID_ENTRY(
            0x60755DA0,
            0x6A40,
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

    # END IF


    # 0618aa30 - 6bc4 - 11cf - bf36 - 00aa0055595a
    CLSID_ModexProperties = OUR_GUID_ENTRY(
        0x0618AA30,
        0x6BC4,
        0x11CF,
        0xBF,
        0x36,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # dd1d7110 - 7836 - 11cf - bf47 - 00aa0055595a
    IID_IFullScreenVideo = OUR_GUID_ENTRY(
        0xDD1D7110,
        0x7836,
        0x11CF,
        0xBF,
        0x47,
        0x00,
        0xAA,
        0x00,
        0x55,
        0x59,
        0x5A
    )

    # 53479470 - f1dd - 11cf - bc42 - 00aa00ac74f6
    IID_IFullScreenVideoEx = OUR_GUID_ENTRY(
        0x53479470,
        0xF1DD,
        0x11CF,
        0xBC,
        0x42,
        0x00,
        0xAA,
        0x00,
        0xAC,
        0x74,
        0xF6
    )

    # {101193C0 - 0BFE - 11d0 - AF91 - 00AA00B67A42}   DV decoder property
    CLSID_DVDecPropertiesPage = OUR_GUID_ENTRY(
        0x101193C0,
        0xBFE,
        0x11D0,
        0xAF,
        0x91,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # {4150F050 - BB6F - 11d0 - AFB9 - 00AA00B67A42}   DV encoder property
    CLSID_DVEncPropertiesPage = OUR_GUID_ENTRY(
        0x4150F050,
        0xBB6F,
        0x11D0,
        0xAF,
        0xB9,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # {4DB880E0 - C10D - 11d0 - AFB9 - 00AA00B67A42}   DV Muxer property
    CLSID_DVMuxPropertyPage = OUR_GUID_ENTRY(
        0x4DB880E0,
        0xC10D,
        0x11D0,
        0xAF,
        0xB9,
        0x0,
        0xAA,
        0x0,
        0xB6,
        0x7A,
        0x42
    )

    # - - Direct Sound Audio related GUID - - -
    # 546F4260 - D53E - 11cf - B3F0 - 00AA003761C5
    IID_IAMDirectSound = OUR_GUID_ENTRY(
        0x546F4260,
        0xD53E,
        0x11CF,
        0xB3,
        0xF0,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x61,
        0xC5
    )

    # - - MPEG audio decoder properties
    # {b45dd570 - 3c77 - 11d1 - abe1 - 00a0c905f375}
    IID_IMpegAudioDecoder = OUR_GUID_ENTRY(
        0xB45DD570,
        0x3C77,
        0x11D1,
        0xAB,
        0xE1,
        0x00,
        0xA0,
        0xC9,
        0x05,
        0xF3,
        0x75
    )

    # - - - Line21 Decoder interface GUID - - -
    # 6E8D4A21 - 310C - 11d0 - B79A - 00AA003767A7  IID_IAMLine21Decoder
    IID_IAMLine21Decoder = OUR_GUID_ENTRY(
        0x6E8D4A21,
        0x310C,
        0x11D0,
        0xB7,
        0x9A,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x67,
        0xA7
    )

    # - - - WST Decoder interface GUID - - -
    # C056DE21 - 75C2 - 11d3 - A184 - 00105AEF9F33  IID_IAMWstDecoder
    IID_IAMWstDecoder = OUR_GUID_ENTRY(
        0xC056DE21,
        0x75C2,
        0x11D3,
        0xA1,
        0x84,
        0x0,
        0x10,
        0x5A,
        0xEF,
        0x9F,
        0x33
    )

    # - - - WST Decoder Property Page - - -
    # 04E27F80 - 91E4 - 11d3 - A184 - 00105AEF9F33  WST Decoder Property Page
    CLSID_WstDecoderPropertyPage = OUR_GUID_ENTRY(
        0x4E27F80,
        0x91E4,
        0x11D3,
        0xA1,
        0x84,
        0x0,
        0x10,
        0x5A,
        0xEF,
        0x9F,
        0x33
    )

    # - - Analog video related GUIDs - - -
    # - - format types - - -
    # 0482DDE0 - 7817 - 11cf - 8A03 - 00AA006ECB65
    FORMAT_AnalogVideo = OUR_GUID_ENTRY(
        0x482DDE0,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # - - major type, Analog Video
    # 0482DDE1 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIATYPE_AnalogVideo = OUR_GUID_ENTRY(
        0x482DDE1,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # - - Analog Video subtypes, NTSC
    # 0482DDE2 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_NTSC_M = OUR_GUID_ENTRY(
        0x482DDE2,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # - - Analog Video subtypes, PAL
    # 0482DDE5 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_B = OUR_GUID_ENTRY(
        0x482DDE5,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDE6 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_D = OUR_GUID_ENTRY(
        0x482DDE6,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDE7 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_G = OUR_GUID_ENTRY(
        0x482DDE7,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDE8 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_H = OUR_GUID_ENTRY(
        0x482DDE8,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDE9 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_I = OUR_GUID_ENTRY(
        0x482DDE9,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDEA - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_M = OUR_GUID_ENTRY(
        0x482DDEA,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDEB - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_N = OUR_GUID_ENTRY(
        0x482DDEB,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDEC - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_PAL_N_COMBO = OUR_GUID_ENTRY(
        0x482DDEC,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # - - Analog Video subtypes, SECAM
    # 0482DDF0 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_SECAM_B = OUR_GUID_ENTRY(
        0x482DDF0,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDF1 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_SECAM_D = OUR_GUID_ENTRY(
        0x482DDF1,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDF2 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_SECAM_G = OUR_GUID_ENTRY(
        0x482DDF2,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDF3 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_SECAM_H = OUR_GUID_ENTRY(
        0x482DDF3,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDF4 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_SECAM_K = OUR_GUID_ENTRY(
        0x482DDF4,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDF5 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_SECAM_K1 = OUR_GUID_ENTRY(
        0x482DDF5,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # 0482DDF6 - 7817 - 11cf - 8A03 - 00AA006ECB65
    MEDIASUBTYPE_AnalogVideo_SECAM_L = OUR_GUID_ENTRY(
        0x482DDF6,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # - - External audio related GUIDs - - -
    # - - major types, Analog Audio
    # 0482DEE1 - 7817 - 11cf - 8a03 - 00aa006ecb65
    MEDIATYPE_AnalogAudio = OUR_GUID_ENTRY(
        0x482DEE1,
        0x7817,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # - - Video analysis related GUIDs - - -
    # - - format types used by VA - - H.264, captioning
    # {A4EFC024 - 873E - 4da3 - 898B - 474DDBD79FD0}
    FORMAT_CAPTIONED_H264VIDEO = OUR_GUID_ENTRY(
        0xA4EFC024,
        0x873E,
        0x4DA3,
        0x89,
        0x8B,
        0x47,
        0x4D,
        0xDB,
        0xD7,
        0x9F,
        0xD0
    )

    # - - media, media subtype, and format types, CC container
    # {50997A4A - E508 - 4054 - A2B2 - 10FF0AC1A69A}
    FORMAT_CC_CONTAINER = OUR_GUID_ENTRY(
        0x50997A4A,
        0xE508,
        0x4054,
        0xA2,
        0xB2,
        0x10,
        0xFF,
        0xA,
        0xC1,
        0xA6,
        0x9A
    )

    # {3ED9CB31 - FD10 - 4ade - BCCC - FB9105D2F3EF}
    CAPTION_FORMAT_ATSC = OUR_GUID_ENTRY(
        0x3ED9CB31,
        0xFD10,
        0x4ADE,
        0xBC,
        0xCC,
        0xFB,
        0x91,
        0x5,
        0xD2,
        0xF3,
        0xEF
    )

    # {12230DB4 - FF2A - 447e - BB88 - 6841C416D068}
    CAPTION_FORMAT_DVB = OUR_GUID_ENTRY(
        0x12230DB4,
        0xFF2A,
        0x447E,
        0xBB,
        0x88,
        0x68,
        0x41,
        0xC4,
        0x16,
        0xD0,
        0x68
    )

    # {E9CA1CE7 - 915E - 47be - 9BB9 - BF1D8A13A5EC}
    CAPTION_FORMAT_DIRECTV = OUR_GUID_ENTRY(
        0xE9CA1CE7,
        0x915E,
        0x47BE,
        0x9B,
        0xB9,
        0xBF,
        0x1D,
        0x8A,
        0x13,
        0xA5,
        0xEC
    )

    # {EBB1A262 - 1158 - 4b99 - AE80 - 92AC776952C4}
    CAPTION_FORMAT_ECHOSTAR = OUR_GUID_ENTRY(
        0xEBB1A262,
        0x1158,
        0x4B99,
        0xAE,
        0x80,
        0x92,
        0xAC,
        0x77,
        0x69,
        0x52,
        0xC4
    )

    # - - format types, MPEG - 2
    # {7AB2ADA2 - 81B6 - 4f14 - B3C8 - D0C486393B67}
    FORMAT_CAPTIONED_MPEG2VIDEO = OUR_GUID_ENTRY(
        0x7AB2ADA2,
        0x81B6,
        0x4F14,
        0xB3,
        0xC8,
        0xD0,
        0xC4,
        0x86,
        0x39,
        0x3B,
        0x67
    )

    # DirectShow's include file based on ksmedia.h from WDM DDK
    from pyWinAPI.shared.ksuuids_h import * # NOQA

    # - - Well known time format GUIDs - - -
    # 00000000 - 0000 - 0000 - 0000 - 000000000000
    TIME_FORMAT_NONE = OUR_GUID_ENTRY(
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0
    )

    # 7b785570 - 8c82 - 11cf - bc0c - 00aa00ac74f6
    TIME_FORMAT_FRAME = OUR_GUID_ENTRY(
        0x7B785570,
        0x8C82,
        0x11CF,
        0xBC,
        0xC,
        0x0,
        0xAA,
        0x0,
        0xAC,
        0x74,
        0xF6
    )

    # 7b785571 - 8c82 - 11cf - bc0c - 00aa00ac74f6
    TIME_FORMAT_BYTE = OUR_GUID_ENTRY(
        0x7B785571,
        0x8C82,
        0x11CF,
        0xBC,
        0xC,
        0x0,
        0xAA,
        0x0,
        0xAC,
        0x74,
        0xF6
    )

    # 7b785572 - 8c82 - 11cf - bc0c - 00aa00ac74f6
    TIME_FORMAT_SAMPLE = OUR_GUID_ENTRY(
        0x7B785572,
        0x8C82,
        0x11CF,
        0xBC,
        0xC,
        0x0,
        0xAA,
        0x0,
        0xAC,
        0x74,
        0xF6
    )

    # 7b785573 - 8c82 - 11cf - bc0c - 00aa00ac74f6
    TIME_FORMAT_FIELD = OUR_GUID_ENTRY(
        0x7B785573,
        0x8C82,
        0x11CF,
        0xBC,
        0xC,
        0x0,
        0xAA,
        0x0,
        0xAC,
        0x74,
        0xF6
    )

    # 7b785574 - 8c82 - 11cf - bc0c - 00aa00ac74f6
    TIME_FORMAT_MEDIA_TIME = OUR_GUID_ENTRY(
        0x7B785574,
        0x8C82,
        0x11CF,
        0xBC,
        0xC,
        0x0,
        0xAA,
        0x0,
        0xAC,
        0x74,
        0xF6
    )

    # for IKsPropertySet
    # 9B00F101 - 1567 - 11d1 - B3F1 - 00AA003761C5
    AMPROPSETID_Pin = OUR_GUID_ENTRY(
        0x9B00F101,
        0x1567,
        0x11D1,
        0xB3,
        0xF1,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x61,
        0xC5
    )

    # fb6c4281 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_CAPTURE = OUR_GUID_ENTRY(
        0xFB6C4281,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4282 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_PREVIEW = OUR_GUID_ENTRY(
        0xFB6C4282,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4283 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_ANALOGVIDEOIN = OUR_GUID_ENTRY(
        0xFB6C4283,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4284 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_VBI = OUR_GUID_ENTRY(
        0xFB6C4284,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4285 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_VIDEOPORT = OUR_GUID_ENTRY(
        0xFB6C4285,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4286 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_NABTS = OUR_GUID_ENTRY(
        0xFB6C4286,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4287 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_EDS = OUR_GUID_ENTRY(
        0xFB6C4287,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4288 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_TELETEXT = OUR_GUID_ENTRY(
        0xFB6C4288,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c4289 - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_CC = OUR_GUID_ENTRY(
        0xFB6C4289,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c428a - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_STILL = OUR_GUID_ENTRY(
        0xFB6C428A,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c428b - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_TIMECODE = OUR_GUID_ENTRY(
        0xFB6C428B,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # fb6c428c - 0353 - 11d1 - 905f - 0000c0cc16ba
    PIN_CATEGORY_VIDEOPORT_VBI = OUR_GUID_ENTRY(
        0xFB6C428C,
        0x0353,
        0x11D1,
        0x90,
        0x5F,
        0x00,
        0x00,
        0xC0,
        0xCC,
        0x16,
        0xBA
    )

    # the following special GUIDS are used by
    # ICaptureGraphBuilder::FindInterface
    # {AC798BE0 - 98E3 - 11d1 - B3F1 - 00AA003761C5}
    LOOK_UPSTREAM_ONLY = OUR_GUID_ENTRY(
        0xAC798BE0,
        0x98E3,
        0x11D1,
        0xB3,
        0xF1,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x61,
        0xC5
    )

    # {AC798BE1 - 98E3 - 11d1 - B3F1 - 00AA003761C5}
    LOOK_DOWNSTREAM_ONLY = OUR_GUID_ENTRY(
        0xAC798BE1,
        0x98E3,
        0x11D1,
        0xB3,
        0xF1,
        0x0,
        0xAA,
        0x0,
        0x37,
        0x61,
        0xC5
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # KSProxy GUIDS
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # {266EEE41 - 6C63 - 11cf - 8A03 - 00AA006ECB65}
    CLSID_TVTunerFilterPropertyPage = OUR_GUID_ENTRY(
        0x266EEE41,
        0x6C63,
        0x11CF,
        0x8A,
        0x3,
        0x0,
        0xAA,
        0x0,
        0x6E,
        0xCB,
        0x65
    )

    # {71F96461 - 78F3 - 11d0 - A18C - 00A0C9118956}
    CLSID_CrossbarFilterPropertyPage = OUR_GUID_ENTRY(
        0x71F96461,
        0x78F3,
        0x11D0,
        0xA1,
        0x8C,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0x89,
        0x56
    )

    # {71F96463 - 78F3 - 11d0 - A18C - 00A0C9118956}
    CLSID_TVAudioFilterPropertyPage = OUR_GUID_ENTRY(
        0x71F96463,
        0x78F3,
        0x11D0,
        0xA1,
        0x8C,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0x89,
        0x56
    )

    # {71F96464 - 78F3 - 11d0 - A18C - 00A0C9118956}
    CLSID_VideoProcAmpPropertyPage = OUR_GUID_ENTRY(
        0x71F96464,
        0x78F3,
        0x11D0,
        0xA1,
        0x8C,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0x89,
        0x56
    )

    # {71F96465 - 78F3 - 11d0 - A18C - 00A0C9118956}
    CLSID_CameraControlPropertyPage = OUR_GUID_ENTRY(
        0x71F96465,
        0x78F3,
        0x11D0,
        0xA1,
        0x8C,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0x89,
        0x56
    )

    # {71F96466 - 78F3 - 11d0 - A18C - 00A0C9118956}
    CLSID_AnalogVideoDecoderPropertyPage = OUR_GUID_ENTRY(
        0x71F96466,
        0x78F3,
        0x11D0,
        0xA1,
        0x8C,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0x89,
        0x56
    )

    # {71F96467 - 78F3 - 11d0 - A18C - 00A0C9118956}
    CLSID_VideoStreamConfigPropertyPage = OUR_GUID_ENTRY(
        0x71F96467,
        0x78F3,
        0x11D0,
        0xA1,
        0x8C,
        0x0,
        0xA0,
        0xC9,
        0x11,
        0x89,
        0x56
    )

    # {37E92A92 - D9AA - 11d2 - BF84 - 8EF2B1555AED} Audio Renderer Advanced
    # Property Page
    CLSID_AudioRendererAdvancedProperties = OUR_GUID_ENTRY(
        0x37E92A92,
        0xD9AA,
        0x11D2,
        0xBF,
        0x84,
        0x8E,
        0xF2,
        0xB1,
        0x55,
        0x5A,
        0xED
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # VMR GUIDS
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # {B87BEB7B - 8D29 - 423f - AE4D - 6582C10175AC}
    CLSID_VideoMixingRenderer = OUR_GUID_ENTRY(
        0xB87BEB7B,
        0x8D29,
        0x423F,
        0xAE,
        0x4D,
        0x65,
        0x82,
        0xC1,
        0x01,
        0x75,
        0xAC
    )

    # {6BC1CFFA - 8FC1 - 4261 - AC22 - CFB4CC38DB50}
    CLSID_VideoRendererDefault = OUR_GUID_ENTRY(
        0x6BC1CFFA,
        0x8FC1,
        0x4261,
        0xAC,
        0x22,
        0xCF,
        0xB4,
        0xCC,
        0x38,
        0xDB,
        0x50
    )

    # {99d54f63 - 1a69 - 41ae - aa4d - c976eb3f0713}
    CLSID_AllocPresenter = OUR_GUID_ENTRY(
        0x99D54F63,
        0x1A69,
        0x41AE,
        0xAA,
        0x4D,
        0xC9,
        0x76,
        0xEB,
        0x3F,
        0x07,
        0x13
    )

    # {4444ac9e - 242e - 471b - a3c7 - 45dcd46352bc}
    CLSID_AllocPresenterDDXclMode = OUR_GUID_ENTRY(
        0x4444AC9E,
        0x242E,
        0x471B,
        0xA3,
        0xC7,
        0x45,
        0xDC,
        0xD4,
        0x63,
        0x52,
        0xBC
    )

    # {6f26a6cd - 967b - 47fd - 874a - 7aed2c9d25a2}
    CLSID_VideoPortManager = OUR_GUID_ENTRY(
        0x6F26A6CD,
        0x967B,
        0x47FD,
        0x87,
        0x4A,
        0x7A,
        0xED,
        0x2C,
        0x9D,
        0x25,
        0xA2
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # VMR GUIDS for DX9
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # {51b4abf3 - 748f - 4e3b - a276 - c828330e926a}
    CLSID_VideoMixingRenderer9 = OUR_GUID_ENTRY(
        0x51B4ABF3,
        0x748F,
        0x4E3B,
        0xA2,
        0x76,
        0xC8,
        0x28,
        0x33,
        0x0E,
        0x92,
        0x6A
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # EVR GUIDS
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # {FA10746C - 9B63 - 4b6c - BC49 - FC300EA5F256}
    CLSID_EnhancedVideoRenderer = OUR_GUID_ENTRY(
        0xFA10746C,
        0x9B63,
        0x4B6C,
        0xBC,
        0x49,
        0xFC,
        0x30,
        0xE,
        0xA5,
        0xF2,
        0x56
    )

    __EVR_GUIDS__ = None

    if not defined(__EVR_GUIDS__):
        __EVR_GUIDS__ = 1

        # {E474E05A - AB65 - 4f6a - 827C - 218B1BAAF31F}
        CLSID_MFVideoMixer9 = OUR_GUID_ENTRY(
            0xE474E05A,
            0xAB65,
            0x4F6A,
            0x82,
            0x7C,
            0x21,
            0x8B,
            0x1B,
            0xAA,
            0xF3,
            0x1F
        )

        # {98455561 - 5136 - 4d28 - AB08 - 4CEE40EA2781}
        CLSID_MFVideoPresenter9 = OUR_GUID_ENTRY(
            0x98455561,
            0x5136,
            0x4D28,
            0xAB,
            0x8,
            0x4C,
            0xEE,
            0x40,
            0xEA,
            0x27,
            0x81
        )
    # END IF   __EVR_GUIDS__

    # {a0a7a57b - 59b2 - 4919 - a694 - add0a526c373}
    CLSID_EVRTearlessWindowPresenter9 = OUR_GUID_ENTRY(
        0xA0A7A57B,
        0x59B2,
        0x4919,
        0xA6,
        0x94,
        0xAD,
        0xD0,
        0xA5,
        0x26,
        0xC3,
        0x73
    )

    # {62079164 - 233b - 41f8 - a80f - f01705f514a8}
    CLSID_EVRPlaybackPipelineOptimizer = OUR_GUID_ENTRY(
        0x62079164,
        0x233B,
        0x41F8,
        0xA8,
        0x0F,
        0xF0,
        0x17,
        0x05,
        0xF5,
        0x14,
        0xA8
    )

    # {e447df01 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df02 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df03 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df04 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df05 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df06 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df07 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df08 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df09 - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    # {e447df0a - 10ca - 4d17 - b17e - 6a840f8a3a4c}
    EVRConfig_ForceBob = OUR_GUID_ENTRY(
        0xE447DF01,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_AllowDropToBob = OUR_GUID_ENTRY(
        0xE447DF02,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_ForceThrottle = OUR_GUID_ENTRY(
        0xE447DF03,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_AllowDropToThrottle = OUR_GUID_ENTRY(
        0xE447DF04,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_ForceHalfInterlace = OUR_GUID_ENTRY(
        0xE447DF05,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_AllowDropToHalfInterlace = OUR_GUID_ENTRY(
        0xE447DF06,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_ForceScaling = OUR_GUID_ENTRY(
        0xE447DF07,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_AllowScaling = OUR_GUID_ENTRY(
        0xE447DF08,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_ForceBatching = OUR_GUID_ENTRY(
        0xE447DF09,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )
    EVRConfig_AllowBatching = OUR_GUID_ENTRY(
        0xE447DF0A,
        0x10CA,
        0x4D17,
        0xB1,
        0x7E,
        0x6A,
        0x84,
        0x0F,
        0x8A,
        0x3A,
        0x4C
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # BDA Network Provider GUIDS
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # This is the GUID for the generic NP which would replace ATSC, DVBT, DVBS
    # and DVBC NP. All the other GUIDs are still kept for backward
    # compatibility
    # {B2F3A67C - 29DA - 4c78 - 8831 - 091ED509A475}
    CLSID_NetworkProvider = OUR_GUID_ENTRY(
        0xB2F3A67C,
        0x29DA,
        0x4C78,
        0x88,
        0x31,
        0x9,
        0x1E,
        0xD5,
        0x9,
        0xA4,
        0x75
    )

    # {0DAD2FDD - 5FD7 - 11D3 - 8F50 - 00C04F7971E2}
    CLSID_ATSCNetworkProvider = OUR_GUID_ENTRY(
        0x0DAD2FDD,
        0x5FD7,
        0x11D3,
        0x8F,
        0x50,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0x71,
        0xE2
    )

    # {E3444D16 - 5AC4 - 4386 - 88DF - 13FD230E1DDA}
    CLSID_ATSCNetworkPropertyPage = OUR_GUID_ENTRY(
        0xE3444D16,
        0x5AC4,
        0x4386,
        0x88,
        0xDF,
        0x13,
        0xFD,
        0x23,
        0x0E,
        0x1D,
        0xDA
    )

    # {FA4B375A - 45B4 - 4d45 - 8440 - 263957B11623}
    CLSID_DVBSNetworkProvider = OUR_GUID_ENTRY(
        0xFA4B375A,
        0x45B4,
        0x4D45,
        0x84,
        0x40,
        0x26,
        0x39,
        0x57,
        0xB1,
        0x16,
        0x23
    )

    # {216C62DF - 6D7F - 4e9a - 8571 - 05F14EDB766A}
    CLSID_DVBTNetworkProvider = OUR_GUID_ENTRY(
        0x216C62DF,
        0x6D7F,
        0x4E9A,
        0x85,
        0x71,
        0x5,
        0xF1,
        0x4E,
        0xDB,
        0x76,
        0x6A
    )

    # {DC0C0FE7 - 0485 - 4266 - B93F - 68FBF80ED834}
    CLSID_DVBCNetworkProvider = OUR_GUID_ENTRY(
        0xDC0C0FE7,
        0x485,
        0x4266,
        0xB9,
        0x3F,
        0x68,
        0xFB,
        0xF8,
        0xE,
        0xD8,
        0x34
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # attribute GUIDs
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # {EB7836CA - 14FF - 4919 - BCE7 - 3AF12319E50C}
    DSATTRIB_UDCRTag = OUR_GUID_ENTRY(
        0xEB7836CA,
        0x14FF,
        0x4919,
        0xBC,
        0xE7,
        0x3A,
        0xF1,
        0x23,
        0x19,
        0xE5,
        0x0C
    )

    # {2F5BAE02 - 7B8F - 4f60 - 82D6 - E4EA2F1F4C99}
    DSATTRIB_PicSampleSeq = OUR_GUID_ENTRY(
        0x2F5BAE02,
        0x7B8F,
        0x4F60,
        0x82,
        0xD6,
        0xE4,
        0xEA,
        0x2F,
        0x1F,
        0x4C,
        0x99
    )

    # {5A5F08CA - 55C2 - 4033 - 92AB - 55DB8F781226}
    DSATTRIB_OptionalVideoAttributes = OUR_GUID_ENTRY(
        0x5A5F08CA,
        0x55C2,
        0x4033,
        0x92,
        0xAB,
        0x55,
        0xDB,
        0x8F,
        0x78,
        0x12,
        0x26
    )

    # {e7e050fb - dd5d - 40dd - 9915 - 35dcb81bdc8a}
    DSATTRIB_CC_CONTAINER_INFO = OUR_GUID_ENTRY(
        0xE7E050FB,
        0xDD5D,
        0x40DD,
        0x99,
        0x15,
        0x35,
        0xDC,
        0xB8,
        0x1B,
        0xDC,
        0x8A
    )

    # {B622F612 - 47AD - 4671 - AD6C - 05A98E65DE3A}
    DSATTRIB_TRANSPORT_PROPERTIES = OUR_GUID_ENTRY(
        0xB622F612,
        0x47AD,
        0x4671,
        0xAD,
        0x6C,
        0x5,
        0xA9,
        0x8E,
        0x65,
        0xDE,
        0x3A
    )

    # {e0b56679 - 12b9 - 43cc - b7df - 578caa5a7b63}
    DSATTRIB_PBDATAG_ATTRIBUTE = OUR_GUID_ENTRY(
        0xE0B56679,
        0x12B9,
        0x43CC,
        0xB7,
        0xDF,
        0x57,
        0x8C,
        0xAA,
        0x5A,
        0x7B,
        0x63
    )

    # {0c1a5614 - 30cd - 4f40 - bcbf - d03e52306207}
    DSATTRIB_CAPTURE_STREAMTIME = OUR_GUID_ENTRY(
        0x0C1A5614,
        0x30CD,
        0x4F40,
        0xBC,
        0xBF,
        0xD0,
        0x3E,
        0x52,
        0x30,
        0x62,
        0x07
    )

    # {5FB5673B - 0A2A - 4565 - 827B - 6853FD75E611}
    # DSATTRIB_DSHOW_STREAM_DESC
    DSATTRIB_DSHOW_STREAM_DESC = OUR_GUID_ENTRY(
        0x5FB5673B,
        0xA2A,
        0x4565,
        0x82,
        0x7B,
        0x68,
        0x53,
        0xFD,
        0x75,
        0xE6,
        0x11
    )

    # {892CD111 - 72F3 - 411d - 8B91 - A9E9123AC29A}
    DSATTRIB_SAMPLE_LIVE_STREAM_TIME = OUR_GUID_ENTRY(
        0x892CD111,
        0x72F3,
        0x411D,
        0x8B,
        0x91,
        0xA9,
        0xE9,
        0x12,
        0x3A,
        0xC2,
        0x9A
    )

    # UUID for supported UDRI TAG tables
    UUID_UdriTagTables = OUR_GUID_ENTRY(
        0xE1B98D74,
        0x9778,
        0x4878,
        0xB6,
        0x64,
        0xEB,
        0x20,
        0x20,
        0x36,
        0x4D,
        0x88
    )

    # UUID for supported WMDRM TAG tables
    UUID_WMDRMTagTables = OUR_GUID_ENTRY(
        0x5DCD1101,
        0x9263,
        0x45BB,
        0xA4,
        0xD5,
        0xC4,
        0x15,
        0xAB,
        0x8C,
        0x58,
        0x9C
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # TVE Receiver filter guids
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # The CLSID used by the TVE Receiver filter
    # {05500280 - FAA5 - 4DF9 - 8246 - BFC23AC5CEA8}
    CLSID_DShowTVEFilter = OUR_GUID_ENTRY(
        0x05500280,
        0xFAA5,
        0x4DF9,
        0x82,
        0x46,
        0xBF,
        0xC2,
        0x3A,
        0xC5,
        0xCE,
        0xA8
    )

    # {05500281 - FAA5 - 4DF9 - 8246 - BFC23AC5CEA8}
    CLSID_TVEFilterTuneProperties = OUR_GUID_ENTRY(
        0x05500281,
        0xFAA5,
        0x4DF9,
        0x82,
        0x46,
        0xBF,
        0xC2,
        0x3A,
        0xC5,
        0xCE,
        0xA8
    )

    # {05500282 - FAA5 - 4DF9 - 8246 - BFC23AC5CEA8}
    CLSID_TVEFilterCCProperties = OUR_GUID_ENTRY(
        0x05500282,
        0xFAA5,
        0x4DF9,
        0x82,
        0x46,
        0xBF,
        0xC2,
        0x3A,
        0xC5,
        0xCE,
        0xA8
    )

    # {05500283 - FAA5 - 4DF9 - 8246 - BFC23AC5CEA8}
    CLSID_TVEFilterStatsProperties = OUR_GUID_ENTRY(
        0x05500283,
        0xFAA5,
        0x4DF9,
        0x82,
        0x46,
        0xBF,
        0xC2,
        0x3A,
        0xC5,
        0xCE,
        0xA8
    )

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # Defined ENCAPI parameter GUIDs
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # -
    # The CLSID for the original IVideoEncoder proxy plug - in
    # {B43C4EEC - 8C32 - 4791 - 9102 - 508ADA5EE8E7}
    CLSID_IVideoEncoderProxy = OUR_GUID_ENTRY(
        0xB43C4EEC,
        0x8C32,
        0x4791,
        0x91,
        0x2,
        0x50,
        0x8A,
        0xDA,
        0x5E,
        0xE8,
        0xE7
    )

    # The CLSID for the ICodecAPI proxy plug - in
    # {7ff0997a - 1999 - 4286 - a73c - 622b8814e7eb}
    CLSID_ICodecAPIProxy = OUR_GUID_ENTRY(
        0x7FF0997A,
        0x1999,
        0x4286,
        0xA7,
        0x3C,
        0x62,
        0x2B,
        0x88,
        0x14,
        0xE7,
        0xEB
    )

    # The CLSID for the combination ICodecAPI/IVideoEncoder proxy plug - in
    # {b05dabd9 - 56e5 - 4fdc - afa4 - 8a47e91f1c9c}
    CLSID_IVideoEncoderCodecAPIProxy = OUR_GUID_ENTRY(
        0xB05DABD9,
        0x56E5,
        0x4FDC,
        0xAF,
        0xA4,
        0x8A,
        0x47,
        0xE9,
        0x1F,
        0x1C,
        0x9C
    )

    __ENCODER_API_GUIDS__ = None

    if not defined(__ENCODER_API_GUIDS__):
        __ENCODER_API_GUIDS__ = 1

        # {49CC4C43 - CA83 - 4ad4 - A9AF - F3696AF666DF}
        ENCAPIPARAM_BITRATE = OUR_GUID_ENTRY(
            0x49CC4C43,
            0xCA83,
            0x4AD4,
            0xA9,
            0xAF,
            0xF3,
            0x69,
            0x6A,
            0xF6,
            0x66,
            0xDF
        )

        # {703F16A9 - 3D48 - 44a1 - B077 - 018DFF915D19}
        ENCAPIPARAM_PEAK_BITRATE = OUR_GUID_ENTRY(
            0x703F16A9,
            0x3D48,
            0x44A1,
            0xB0,
            0x77,
            0x1,
            0x8D,
            0xFF,
            0x91,
            0x5D,
            0x19
        )

        # {EE5FB25C - C713 - 40d1 - 9D58 - C0D7241E250F}
        ENCAPIPARAM_BITRATE_MODE = OUR_GUID_ENTRY(
            0xEE5FB25C,
            0xC713,
            0x40D1,
            0x9D,
            0x58,
            0xC0,
            0xD7,
            0x24,
            0x1E,
            0x25,
            0xF
        )

        # {0C0171DB - FEFC - 4af7 - 9991 - A5657C191CD1}
        ENCAPIPARAM_SAP_MODE = OUR_GUID_ENTRY(
            0xC0171DB,
            0xFEFC,
            0x4AF7,
            0x99,
            0x91,
            0xA5,
            0x65,
            0x7C,
            0x19,
            0x1C,
            0xD1
        )

        # for kernel control
        # {62b12acf - f6b0 - 47d9 - 9456 - 96f22c4e0b9d}
        CODECAPI_CHANGELISTS = OUR_GUID_ENTRY(
            0x62B12ACF,
            0xF6B0,
            0x47D9,
            0x94,
            0x56,
            0x96,
            0xF2,
            0x2C,
            0x4E,
            0x0B,
            0x9D
        )

        # {7112e8e1 - 3d03 - 47ef - 8e60 - 03f1cf537301 }
        CODECAPI_VIDEO_ENCODER = OUR_GUID_ENTRY(
            0x7112E8E1,
            0x3D03,
            0x47EF,
            0x8E,
            0x60,
            0x03,
            0xF1,
            0xCF,
            0x53,
            0x73,
            0x01
        )

        # {b9d19a3e - f897 - 429c - bc46 - 8138b7272b2d }
        CODECAPI_AUDIO_ENCODER = OUR_GUID_ENTRY(
            0xB9D19A3E,
            0xF897,
            0x429C,
            0xBC,
            0x46,
            0x81,
            0x38,
            0xB7,
            0x27,
            0x2B,
            0x2D
        )

        # {6c5e6a7c - acf8 - 4f55 - a999 - 1a628109051b }
        CODECAPI_SETALLDEFAULTS = OUR_GUID_ENTRY(
            0x6C5E6A7C,
            0xACF8,
            0x4F55,
            0xA9,
            0x99,
            0x1A,
            0x62,
            0x81,
            0x09,
            0x05,
            0x1B
        )

        # {6a577e92 - 83e1 - 4113 - adc2 - 4fcec32f83a1 }
        CODECAPI_ALLSETTINGS = OUR_GUID_ENTRY(
            0x6A577E92,
            0x83E1,
            0x4113,
            0xAD,
            0xC2,
            0x4F,
            0xCE,
            0xC3,
            0x2F,
            0x83,
            0xA1
        )

        # {0581af97 - 7693 - 4dbd - 9dca - 3f9ebd6585a1 }
        CODECAPI_SUPPORTSEVENTS = OUR_GUID_ENTRY(
            0x0581AF97,
            0x7693,
            0x4DBD,
            0x9D,
            0xCA,
            0x3F,
            0x9E,
            0xBD,
            0x65,
            0x85,
            0xA1
        )

        # {1cb14e83 - 7d72 - 4657 - 83fd - 47a2c5b9d13d }
        CODECAPI_CURRENTCHANGELIST = OUR_GUID_ENTRY(
            0x1CB14E83,
            0x7D72,
            0x4657,
            0x83,
            0xFD,
            0x47,
            0xA2,
            0xC5,
            0xB9,
            0xD1,
            0x3D
        )

        # {1f26a602 - 2b5c - 4b63 - b8e8 - 9ea5c1a7dc2e}
        CLSID_SBE2MediaTypeProfile = OUR_GUID_ENTRY(
            0x1F26A602,
            0x2B5C,
            0x4B63,
            0xB8,
            0xE8,
            0x9E,
            0xA5,
            0xC1,
            0xA7,
            0xDC,
            0x2E
        )

        # {3E458037 - 0CA6 - 41aa - A594 - 2AA6C02D709B}
        CLSID_SBE2FileScan = OUR_GUID_ENTRY(
            0x3E458037,
            0xCA6,
            0x41AA,
            0xA5,
            0x94,
            0x2A,
            0xA6,
            0xC0,
            0x2D,
            0x70,
            0x9B
        )

        # When generating strmiids.lib, include codecapi definitions
        INITGUID = 0
        if defined(INITGUID):
            UUID_GEN = 1
            from pyWinAPI.um.codecapi_h import * # NOQA

        # END IF
    # END IF   __ENCODER_API_GUIDS__
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - -
    # Used for decoders that exposing ICodecAPI
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - -
    CODECAPI_AVDecMmcssClass = OUR_GUID_ENTRY(
        0xE0AD4828,
        0xDF66,
        0x4893,
        0x9F,
        0x33,
        0x78,
        0x8A,
        0xA4,
        0xEC,
        0x40,
        0x82
    )
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
