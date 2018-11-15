from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# codecapi.h Abstract: CodecAPI Definitions. - -

__CODECAPI_H = None
if not defined(__CODECAPI_H):
    __CODECAPI_H = 1
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        UUID_GEN = 0
        if defined(UUID_GEN):
            def DEFINE_CODECAPI_GUID(guidstr, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11):
                return GUID(g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11)

        else:
            if not defined(DEFINE_GUIDSTRUCT):
                if defined(__cplusplus) and _MSC_VER >= 1100:
                    def DEFINE_GUIDSTRUCT(g):
                        if isinstance(g, GUID):
                            return g
                        return GUID(g)


                    def DEFINE_GUIDNAMED(g):
                        if isinstance(g, GUID):
                            return g

                        return GUID(g)
                else: #  not defined(__cplusplus)
                    def DEFINE_GUIDSTRUCT(g):
                        if isinstance(g, GUID):
                            return g
                        return GUID(g)


                    def DEFINE_GUIDNAMED(g):
                        if isinstance(g, GUID):
                            return g
                        return GUID(g)

                # END IF   not defined(__cplusplus)
            # END IF

            # Ideally we would like:
            # #define DEFINE_CODECAPI_GUID( name, guidstr, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11 ) \
            # #define STATIC_CODECAPI_##name 0x##g1, 0x##g2, 0x##g3, 0x##g4, 0x##g5, 0x##g6, 0x##g7, 0x##g8, 0x##g9, 0x##g10, 0x##g11
            #                         DEFINE_GUIDSTRUCT( guidstr, CODECAPI_##name )
            # #define CODECAPI_##name DEFINE_GUIDNAMED( CODECAPI_##name )
            # Unfortunately you can't invoke multiple defines from a single statement

            def DEFINE_CODECAPI_GUID(guidstr, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11):
                return DEFINE_GUIDSTRUCT(guidstr)


            def DEFINE_CODECAPI_GUIDNAMED(g):
                return DEFINE_GUIDNAMED(g)
        # END IF

        # Windows CodecAPI Properties
        # Legend for the
        # Reference VariantType VariantField
        # UINT8  VT_UI1 bVal
        # UINT16 VT_UI2 uiVal
        # UINT32 VT_UI4 ulVal
        # UINT64 VT_UI8 ullVal
        # INT8  VT_I1  eVal
        # INT16  VT_I2  iVal
        # INT32  VT_I4  lVal
        # INT64  VT_I8  llVal
        # BOOL  VT_BOOL  BOOLVal
        # GUID  VT_BSTR  bstrVal (guid string)
        # UINT32/UNINT32 VT_UI8 ullVal (ratio)
        # { Static definitions
        STATIC_CODECAPI_AVEncCommonFormatConstraint = (
            0x57CBB9B8, 0x116F, 0x4951, 0xB4, 0x0C, 0xC2, 0xA0, 0x35, 0xED, 0x8F, 0x17
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatUnSpecified = (
            0xAF46A35A, 0x6024, 0x4525, 0xA4, 0x8A, 0x09, 0x4B, 0x97, 0xF5, 0xB3, 0xC2
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatDVD_V = (
            0xCC9598C4, 0xE7FE, 0x451D, 0xB1, 0xCA, 0x76, 0x1B, 0xC8, 0x40, 0xB7, 0xF3
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatDVD_DashVR = (
            0xE55199D6, 0x044C, 0x4DAE, 0xA4, 0x88, 0x53, 0x1E, 0xD3, 0x06, 0x23, 0x5B
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatDVD_PlusVR = (
            0xE74C6F2E, 0xEC37, 0x478D, 0x9A, 0xF4, 0xA5, 0xE1, 0x35, 0xB6, 0x27, 0x1C
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatVCD = (
            0x95035BF7, 0x9D90, 0x40FF, 0xAD, 0x5C, 0x5C, 0xF8, 0xCF, 0x71, 0xCA, 0x1D
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatSVCD = (
            0x51D85818, 0x8220, 0x448C, 0x80, 0x66, 0xD6, 0x9B, 0xED, 0x16, 0xC9, 0xAD
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatATSC = (
            0x8D7B897C, 0xA019, 0x4670, 0xAA, 0x76, 0x2E, 0xDC, 0xAC, 0x7A, 0xC2, 0x96
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatDVB = (
            0x71830D8F, 0x6C33, 0x430D, 0x84, 0x4B, 0xC2, 0x70, 0x5B, 0xAA, 0xE6, 0xDB
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatMP3 = (
            0x349733CD, 0xEB08, 0x4DC2, 0x81, 0x97, 0xE4, 0x98, 0x35, 0xEF, 0x82, 0x8B
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatHighMAT = (
            0x1EABE760, 0xFB2B, 0x4928, 0x90, 0xD1, 0x78, 0xDB, 0x88, 0xEE, 0xE8, 0x89
        )
        STATIC_CODECAPI_GUID_AVEncCommonFormatHighMPV = (
            0xA2D25DB8, 0xB8F9, 0x42C2, 0x8B, 0xC7, 0x0B, 0x93, 0xCF, 0x60, 0x47, 0x88
        )
        STATIC_CODECAPI_AVEncCodecType = (
            0x08AF4AC1, 0xF3F2, 0x4C74, 0x9D, 0xCF, 0x37, 0xF2, 0xEC, 0x79, 0xF8, 0x26
        )
        STATIC_CODECAPI_GUID_AVEncMPEG1Video = (
            0xC8DAFEFE, 0xDA1E, 0x4774, 0xB2, 0x7D, 0x11, 0x83, 0x0C, 0x16, 0xB1, 0xFE
        )
        STATIC_CODECAPI_GUID_AVEncMPEG2Video = (
            0x046DC19A, 0x6677, 0x4AAA, 0xA3, 0x1D, 0xC1, 0xAB, 0x71, 0x6F, 0x45, 0x60
        )
        STATIC_CODECAPI_GUID_AVEncMPEG1Audio = (
            0xD4DD1362, 0xCD4A, 0x4CD6, 0x81, 0x38, 0xB9, 0x4D, 0xB4, 0x54, 0x2B, 0x04
        )
        STATIC_CODECAPI_GUID_AVEncMPEG2Audio = (
            0xEE4CBB1F, 0x9C3F, 0x4770, 0x92, 0xB5, 0xFC, 0xB7, 0xC2, 0xA8, 0xD3, 0x81
        )
        STATIC_CODECAPI_GUID_AVEncWMV = (
            0x4E0FEF9B, 0x1D43, 0x41BD, 0xB8, 0xBD, 0x4D, 0x7B, 0xF7, 0x45, 0x7A, 0x2A
        )
        STATIC_CODECAPI_GUID_AVEndMPEG4Video = (
            0xDD37B12A, 0x9503, 0x4F8B, 0xB8, 0xD0, 0x32, 0x4A, 0x00, 0xC0, 0xA1, 0xCF
        )
        STATIC_CODECAPI_GUID_AVEncH264Video = (
            0x95044EAB, 0x31B3, 0x47DE, 0x8E, 0x75, 0x38, 0xA4, 0x2B, 0xB0, 0x3E, 0x28
        )
        STATIC_CODECAPI_GUID_AVEncDV = (
            0x09B769C7, 0x3329, 0x44FB, 0x89, 0x54, 0xFA, 0x30, 0x93, 0x7D, 0x3D, 0x5A
        )
        STATIC_CODECAPI_GUID_AVEncWMAPro = (
            0x1955F90C, 0x33F7, 0x4A68, 0xAB, 0x81, 0x53, 0xF5, 0x65, 0x71, 0x25, 0xC4
        )
        STATIC_CODECAPI_GUID_AVEncWMALossless = (
            0x55CA7265, 0x23D8, 0x4761, 0x90, 0x31, 0xB7, 0x4F, 0xBE, 0x12, 0xF4, 0xC1
        )
        STATIC_CODECAPI_GUID_AVEncWMAVoice = (
            0x13ED18CB, 0x50E8, 0x4276, 0xA2, 0x88, 0xA6, 0xAA, 0x22, 0x83, 0x82, 0xD9
        )
        STATIC_CODECAPI_GUID_AVEncDolbyDigitalPro = (
            0xF5BE76CC, 0x0FF8, 0x40EB, 0x9C, 0xB1, 0xBB, 0xA9, 0x40, 0x04, 0xD4, 0x4F
        )
        STATIC_CODECAPI_GUID_AVEncDolbyDigitalConsumer = (
            0xC1A7BF6C, 0x0059, 0x4BFA, 0x94, 0xEF, 0xEF, 0x74, 0x7A, 0x76, 0x8D, 0x52
        )
        STATIC_CODECAPI_GUID_AVEncDolbyDigitalPlus = (
            0x698D1B80, 0xF7DD, 0x415C, 0x97, 0x1C, 0x42, 0x49, 0x2A, 0x20, 0x56, 0xC6
        )
        STATIC_CODECAPI_GUID_AVEncDTSHD = (
            0x2052E630, 0x469D, 0x4BFB, 0x80, 0xCA, 0x1D, 0x65, 0x6E, 0x7E, 0x91, 0x8F
        )
        STATIC_CODECAPI_GUID_AVEncDTS = (
            0x45FBCAA2, 0x5E6E, 0x4AB0, 0x88, 0x93, 0x59, 0x03, 0xBE, 0xE9, 0x3A, 0xCF
        )
        STATIC_CODECAPI_GUID_AVEncMLP = (
            0x05F73E29, 0xF0D1, 0x431E, 0xA4, 0x1C, 0xA4, 0x74, 0x32, 0xEC, 0x5A, 0x66
        )
        STATIC_CODECAPI_GUID_AVEncPCM = (
            0x844BE7F4, 0x26CF, 0x4779, 0xB3, 0x86, 0xCC, 0x05, 0xD1, 0x87, 0x99, 0x0C
        )
        STATIC_CODECAPI_GUID_AVEncSDDS = (
            0x1DC1B82F, 0x11C8, 0x4C71, 0xB7, 0xB6, 0xEE, 0x3E, 0xB9, 0xBC, 0x2B, 0x94
        )
        STATIC_CODECAPI_AVEncCommonRateControlMode = (
            0x1C0608E9, 0x370C, 0x4710, 0x8A, 0x58, 0xCB, 0x61, 0x81, 0xC4, 0x24, 0x23
        )
        STATIC_CODECAPI_AVEncCommonLowLatency = (
            0x9D3ECD55, 0x89E8, 0x490A, 0x97, 0x0A, 0x0C, 0x95, 0x48, 0xD5, 0xA5, 0x6E
        )
        STATIC_CODECAPI_AVEncCommonMultipassMode = (
            0x22533D4C, 0x47E1, 0x41B5, 0x93, 0x52, 0xA2, 0xB7, 0x78, 0x0E, 0x7A, 0xC4
        )
        STATIC_CODECAPI_AVEncCommonPassStart = (
            0x6A67739F, 0x4EB5, 0x4385, 0x99, 0x28, 0xF2, 0x76, 0xA9, 0x39, 0xEF, 0x95
        )
        STATIC_CODECAPI_AVEncCommonPassEnd = (
            0x0E3D01BC, 0xC85C, 0x467D, 0x8B, 0x60, 0xC4, 0x10, 0x12, 0xEE, 0x3B, 0xF6
        )
        STATIC_CODECAPI_AVEncCommonRealTime = (
            0x143A0FF6, 0xA131, 0x43DA, 0xB8, 0x1E, 0x98, 0xFB, 0xB8, 0xEC, 0x37, 0x8E
        )
        STATIC_CODECAPI_AVEncCommonQuality = (
            0xFCBF57A3, 0x7EA5, 0x4B0C, 0x96, 0x44, 0x69, 0xB4, 0x0C, 0x39, 0xC3, 0x91
        )
        STATIC_CODECAPI_AVEncCommonQualityVsSpeed = (
            0x98332DF8, 0x03CD, 0x476B, 0x89, 0xFA, 0x3F, 0x9E, 0x44, 0x2D, 0xEC, 0x9F
        )
        STATIC_CODECAPI_AVEncCommonTranscodeEncodingProfile = (
            0x6947787C, 0xF508, 0x4EA9, 0xB1, 0xE9, 0xA1, 0xFE, 0x3A, 0x49, 0xFB, 0xC9
        )
        STATIC_CODECAPI_AVEncCommonMeanBitRate = (
            0xF7222374, 0x2144, 0x4815, 0xB5, 0x50, 0xA3, 0x7F, 0x8E, 0x12, 0xEE, 0x52
        )
        STATIC_CODECAPI_AVEncCommonMeanBitRateInterval = (
            0xBFAA2F0C, 0xCB82, 0x4BC0, 0x84, 0x74, 0xF0, 0x6A, 0x8A, 0x0D, 0x02, 0x58
        )
        STATIC_CODECAPI_AVEncCommonMaxBitRate = (
            0x9651EAE4, 0x39B9, 0x4EBF, 0x85, 0xEF, 0xD7, 0xF4, 0x44, 0xEC, 0x74, 0x65
        )
        STATIC_CODECAPI_AVEncCommonMinBitRate = (
            0x101405B2, 0x2083, 0x4034, 0xA8, 0x06, 0xEF, 0xBE, 0xDD, 0xD7, 0xC9, 0xFF
        )
        STATIC_CODECAPI_AVEncCommonBufferSize = (
            0x0DB96574, 0xB6A4, 0x4C8B, 0x81, 0x06, 0x37, 0x73, 0xDE, 0x03, 0x10, 0xCD
        )
        STATIC_CODECAPI_AVEncCommonBufferInLevel = (
            0xD9C5C8DB, 0xFC74, 0x4064, 0x94, 0xE9, 0xCD, 0x19, 0xF9, 0x47, 0xED, 0x45
        )
        STATIC_CODECAPI_AVEncCommonBufferOutLevel = (
            0xCCAE7F49, 0xD0BC, 0x4E3D, 0xA5, 0x7E, 0xFB, 0x57, 0x40, 0x14, 0x00, 0x69
        )
        STATIC_CODECAPI_AVEncCommonStreamEndHandling = (
            0x6AAD30AF, 0x6BA8, 0x4CCC, 0x8F, 0xCA, 0x18, 0xD1, 0x9B, 0xEA, 0xEB, 0x1C
        )
        STATIC_CODECAPI_AVEncStatCommonCompletedPasses = (
            0x3E5DE533, 0x9DF7, 0x438C, 0x85, 0x4F, 0x9F, 0x7D, 0xD3, 0x68, 0x3D, 0x34
        )
        STATIC_CODECAPI_AVEncVideoOutputFrameRate = (
            0xEA85E7C3, 0x9567, 0x4D99, 0x87, 0xC4, 0x02, 0xC1, 0xC2, 0x78, 0xCA, 0x7C
        )
        STATIC_CODECAPI_AVEncVideoOutputFrameRateConversion = (
            0x8C068BF4, 0x369A, 0x4BA3, 0x82, 0xFD, 0xB2, 0x51, 0x8F, 0xB3, 0x39, 0x6E
        )
        STATIC_CODECAPI_AVEncVideoPixelAspectRatio = (
            0x3CDC718F, 0xB3E9, 0x4EB6, 0xA5, 0x7F, 0xCF, 0x1F, 0x1B, 0x32, 0x1B, 0x87
        )
        STATIC_CODECAPI_AVEncVideoForceSourceScanType = (
            0x1EF2065F, 0x058A, 0x4765, 0xA4, 0xFC, 0x8A, 0x86, 0x4C, 0x10, 0x30, 0x12
        )
        STATIC_CODECAPI_AVEncVideoNoOfFieldsToEncode = (
            0x61E4BBE2, 0x4EE0, 0x40E7, 0x80, 0xAB, 0x51, 0xDD, 0xEE, 0xBE, 0x62, 0x91
        )
        STATIC_CODECAPI_AVEncVideoNoOfFieldsToSkip = (
            0xA97E1240, 0x1427, 0x4C16, 0xA7, 0xF7, 0x3D, 0xCF, 0xD8, 0xBA, 0x4C, 0xC5
        )
        STATIC_CODECAPI_AVEncVideoEncodeDimension = (
            0x1074DF28, 0x7E0F, 0x47A4, 0xA4, 0x53, 0xCD, 0xD7, 0x38, 0x70, 0xF5, 0xCE
        )
        STATIC_CODECAPI_AVEncVideoEncodeOffsetOrigin = (
            0x6BC098FE, 0xA71A, 0x4454, 0x85, 0x2E, 0x4D, 0x2D, 0xDE, 0xB2, 0xCD, 0x24
        )
        STATIC_CODECAPI_AVEncVideoDisplayDimension = (
            0xDE053668, 0xF4EC, 0x47A9, 0x86, 0xD0, 0x83, 0x67, 0x70, 0xF0, 0xC1, 0xD5
        )
        STATIC_CODECAPI_AVEncVideoOutputScanType = (
            0x460B5576, 0x842E, 0x49AB, 0xA6, 0x2D, 0xB3, 0x6F, 0x73, 0x12, 0xC9, 0xDB
        )
        STATIC_CODECAPI_AVEncVideoInverseTelecineEnable = (
            0x2EA9098B, 0xE76D, 0x4CCD, 0xA0, 0x30, 0xD3, 0xB8, 0x89, 0xC1, 0xB6, 0x4C
        )
        STATIC_CODECAPI_AVEncVideoInverseTelecineThreshold = (
            0x40247D84, 0xE895, 0x497F, 0xB4, 0x4C, 0xB7, 0x45, 0x60, 0xAC, 0xFE, 0x27
        )
        STATIC_CODECAPI_AVEncVideoSourceFilmContent = (
            0x1791C64B, 0xCCFC, 0x4827, 0xA0, 0xED, 0x25, 0x57, 0x79, 0x3B, 0x2B, 0x1C
        )
        STATIC_CODECAPI_AVEncVideoSourceIsBW = (
            0x42FFC49B, 0x1812, 0x4FDC, 0x8D, 0x24, 0x70, 0x54, 0xC5, 0x21, 0xE6, 0xEB
        )
        STATIC_CODECAPI_AVEncVideoFieldSwap = (
            0xFEFD7569, 0x4E0A, 0x49F2, 0x9F, 0x2B, 0x36, 0x0E, 0xA4, 0x8C, 0x19, 0xA2
        )
        STATIC_CODECAPI_AVEncVideoInputChromaResolution = (
            0xBB0CEC33, 0x16F1, 0x47B0, 0x8A, 0x88, 0x37, 0x81, 0x5B, 0xEE, 0x17, 0x39
        )
        STATIC_CODECAPI_AVEncVideoOutputChromaResolution = (
            0x6097B4C9, 0x7C1D, 0x4E64, 0xBF, 0xCC, 0x9E, 0x97, 0x65, 0x31, 0x8A, 0xE7
        )
        STATIC_CODECAPI_AVEncVideoInputChromaSubsampling = (
            0xA8E73A39, 0x4435, 0x4EC3, 0xA6, 0xEA, 0x98, 0x30, 0x0F, 0x4B, 0x36, 0xF7
        )
        STATIC_CODECAPI_AVEncVideoOutputChromaSubsampling = (
            0xFA561C6C, 0x7D17, 0x44F0, 0x83, 0xC9, 0x32, 0xED, 0x12, 0xE9, 0x63, 0x43
        )
        STATIC_CODECAPI_AVEncVideoInputColorPrimaries = (
            0xC24D783F, 0x7CE6, 0x4278, 0x90, 0xAB, 0x28, 0xA4, 0xF1, 0xE5, 0xF8, 0x6C
        )
        STATIC_CODECAPI_AVEncVideoOutputColorPrimaries = (
            0xBE95907C, 0x9D04, 0x4921, 0x89, 0x85, 0xA6, 0xD6, 0xD8, 0x7D, 0x1A, 0x6C
        )
        STATIC_CODECAPI_AVEncVideoInputColorTransferFunction = (
            0x8C056111, 0xA9C3, 0x4B08, 0xA0, 0xA0, 0xCE, 0x13, 0xF8, 0xA2, 0x7C, 0x75
        )
        STATIC_CODECAPI_AVEncVideoOutputColorTransferFunction = (
            0x4A7F884A, 0xEA11, 0x460D, 0xBF, 0x57, 0xB8, 0x8B, 0xC7, 0x59, 0x00, 0xDE
        )
        STATIC_CODECAPI_AVEncVideoInputColorTransferMatrix = (
            0x52ED68B9, 0x72D5, 0x4089, 0x95, 0x8D, 0xF5, 0x40, 0x5D, 0x55, 0x08, 0x1C
        )
        STATIC_CODECAPI_AVEncVideoOutputColorTransferMatrix = (
            0xA9B90444, 0xAF40, 0x4310, 0x8F, 0xBE, 0xED, 0x6D, 0x93, 0x3F, 0x89, 0x2B
        )
        STATIC_CODECAPI_AVEncVideoInputColorLighting = (
            0x46A99549, 0x0015, 0x4A45, 0x9C, 0x30, 0x1D, 0x5C, 0xFA, 0x25, 0x83, 0x16
        )
        STATIC_CODECAPI_AVEncVideoOutputColorLighting = (
            0x0E5AAAC6, 0xACE6, 0x4C5C, 0x99, 0x8E, 0x1A, 0x8C, 0x9C, 0x6C, 0x0F, 0x89
        )
        STATIC_CODECAPI_AVEncVideoInputColorNominalRange = (
            0x16CF25C6, 0xA2A6, 0x48E9, 0xAE, 0x80, 0x21, 0xAE, 0xC4, 0x1D, 0x42, 0x7E
        )
        STATIC_CODECAPI_AVEncVideoOutputColorNominalRange = (
            0x972835ED, 0x87B5, 0x4E95, 0x95, 0x00, 0xC7, 0x39, 0x58, 0x56, 0x6E, 0x54
        )
        STATIC_CODECAPI_AVEncInputVideoSystem = (
            0xBEDE146D, 0xB616, 0x4DC7, 0x92, 0xB2, 0xF5, 0xD9, 0xFA, 0x92, 0x98, 0xF7
        )
        STATIC_CODECAPI_AVEncVideoHeaderDropFrame = (
            0x6ED9E124, 0x7925, 0x43FE, 0x97, 0x1B, 0xE0, 0x19, 0xF6, 0x22, 0x22, 0xB4
        )
        STATIC_CODECAPI_AVEncVideoHeaderHours = (
            0x2ACC7702, 0xE2DA, 0x4158, 0xBF, 0x9B, 0x88, 0x88, 0x01, 0x29, 0xD7, 0x40
        )
        STATIC_CODECAPI_AVEncVideoHeaderMinutes = (
            0xDC1A99CE, 0x0307, 0x408B, 0x88, 0x0B, 0xB8, 0x34, 0x8E, 0xE8, 0xCA, 0x7F
        )
        STATIC_CODECAPI_AVEncVideoHeaderSeconds = (
            0x4A2E1A05, 0xA780, 0x4F58, 0x81, 0x20, 0x9A, 0x44, 0x9D, 0x69, 0x65, 0x6B
        )
        STATIC_CODECAPI_AVEncVideoHeaderFrames = (
            0xAFD5F567, 0x5C1B, 0x4ADC, 0xBD, 0xAF, 0x73, 0x56, 0x10, 0x38, 0x14, 0x36
        )
        STATIC_CODECAPI_AVEncVideoDefaultUpperFieldDominant = (
            0x810167C4, 0x0BC1, 0x47CA, 0x8F, 0xC2, 0x57, 0x05, 0x5A, 0x14, 0x74, 0xA5
        )
        STATIC_CODECAPI_AVEncVideoCBRMotionTradeoff = (
            0x0D49451E, 0x18D5, 0x4367, 0xA4, 0xEF, 0x32, 0x40, 0xDF, 0x16, 0x93, 0xC4
        )
        STATIC_CODECAPI_AVEncVideoCodedVideoAccessUnitSize = (
            0xB4B10C15, 0x14A7, 0x4CE8, 0xB1, 0x73, 0xDC, 0x90, 0xA0, 0xB4, 0xFC, 0xDB
        )
        STATIC_CODECAPI_AVEncVideoMaxKeyframeDistance = (
            0x2987123A, 0xBA93, 0x4704, 0xB4, 0x89, 0xEC, 0x1E, 0x5F, 0x25, 0x29, 0x2C
        )
        STATIC_CODECAPI_AVEncH264CABACEnable = (
            0xEE6CAD62, 0xD305, 0x4248, 0xA5, 0xE, 0xE1, 0xB2, 0x55, 0xF7, 0xCA, 0xF8
        )
        STATIC_CODECAPI_AVEncVideoContentType = (
            0x66117ACA, 0xEB77, 0x459D, 0x93, 0xC, 0xA4, 0x8D, 0x9D, 0x6, 0x83, 0xFC
        )
        STATIC_CODECAPI_AVEncNumWorkerThreads = (
            0xB0C8BF60, 0x16F7, 0x4951, 0xA3, 0xB, 0x1D, 0xB1, 0x60, 0x92, 0x93, 0xD6
        )
        STATIC_CODECAPI_AVEncVideoEncodeQP = (
            0x2CB5696B, 0x23FB, 0x4CE1, 0xA0, 0xF9, 0xEF, 0x5B, 0x90, 0xFD, 0x55, 0xCA
        )
        STATIC_CODECAPI_AVEncVideoMinQP = (
            0x0EE22C6A, 0xA37C, 0x4568, 0xB5, 0xF1, 0x9D, 0x4C, 0x2B, 0x3A, 0xB8, 0x86
        )
        STATIC_CODECAPI_AVEncVideoForceKeyFrame = (
            0x398C1B98, 0x8353, 0x475A, 0x9E, 0xF2, 0x8F, 0x26, 0x5D, 0x26, 0x3, 0x45
        )
        STATIC_CODECAPI_AVEncH264SPSID = (
            0x50F38F51, 0x2B79, 0x40E3, 0xB3, 0x9C, 0x7E, 0x9F, 0xA0, 0x77, 0x5, 0x1
        )
        STATIC_CODECAPI_AVEncH264PPSID = (
            0xBFE29EC2, 0x56C, 0x4D68, 0xA3, 0x8D, 0xAE, 0x59, 0x44, 0xC8, 0x58, 0x2E
        )
        STATIC_CODECAPI_AVEncAdaptiveMode = (
            0x4419B185, 0xDA1F, 0x4F53, 0xBC, 0x76, 0x9, 0x7D, 0xC, 0x1E, 0xFB, 0x1E
        )
        STATIC_CODECAPI_AVEncVideoTemporalLayerCount = (
            0x19CAEBFF, 0xB74D, 0x4CFD, 0x8C, 0x27, 0xC2, 0xF9, 0xD9, 0x7D, 0x5F, 0x52
        )
        STATIC_CODECAPI_AVEncVideoUsage = (
            0x1F636849, 0x5DC1, 0x49F1, 0xB1, 0xD8, 0xCE, 0x3C, 0xF6, 0x2E, 0xA3, 0x85
        )
        STATIC_CODECAPI_AVEncVideoSelectLayer = (
            0xEB1084F5, 0x6AAA, 0x4914, 0xBB, 0x2F, 0x61, 0x47, 0x22, 0x7F, 0x12, 0xE7
        )
        STATIC_CODECAPI_AVEncVideoRateControlParams = (
            0x87D43767, 0x7645, 0x44EC, 0xB4, 0x38, 0xD3, 0x32, 0x2F, 0xBC, 0xA2, 0x9F
        )
        STATIC_CODECAPI_AVEncVideoSupportedControls = (
            0xD3F40FDD, 0x77B9, 0x473D, 0x81, 0x96, 0x6, 0x12, 0x59, 0xE6, 0x9C, 0xFF
        )
        STATIC_CODECAPI_AVEncVideoEncodeFrameTypeQP = (
            0xAA70B610, 0xE03F, 0x450C, 0xAD, 0x07, 0x07, 0x31, 0x4E, 0x63, 0x9C, 0xE7
        )
        STATIC_CODECAPI_AVEncSliceControlMode = (
            0xE9E782EF, 0x5F18, 0x44C9, 0xA9, 0x0B, 0xE9, 0xC3, 0xC2, 0xC1, 0x7B, 0x0B
        )
        STATIC_CODECAPI_AVEncSliceControlSize = (
            0x92F51DF3, 0x07A5, 0x4172, 0xAE, 0xFE, 0xC6, 0x9C, 0xA3, 0xB6, 0x0E, 0x35
        )
        STATIC_CODECAPI_AVEncSliceGenerationMode = (
            0x8A6BC67F, 0x9497, 0x4286, 0xB4, 0x6B, 0x02, 0xDB, 0x8D, 0x60, 0xED, 0xBC
        )
        STATIC_CODECAPI_AVEncVideoMaxNumRefFrame = (
            0x964829ED, 0x94F9, 0x43B4, 0xB7, 0x4D, 0xEF, 0x40, 0x94, 0x4B, 0x69, 0xA0
        )
        STATIC_CODECAPI_AVEncVideoMeanAbsoluteDifference = (
            0xE5C0C10F, 0x81A4, 0x422D, 0x8C, 0x3F, 0xB4, 0x74, 0xA4, 0x58, 0x13, 0x36
        )
        STATIC_CODECAPI_AVEncVideoMaxQP = (
            0x3DAF6F66, 0xA6A7, 0x45E0, 0xA8, 0xE5, 0xF2, 0x74, 0x3F, 0x46, 0xA3, 0xA2
        )
        STATIC_CODECAPI_AVEncVideoLTRBufferControl = (
            0xA4A0E93D, 0x4CBC, 0x444C, 0x89, 0xF4, 0x82, 0x6D, 0x31, 0x0E, 0x92, 0xA7
        )
        STATIC_CODECAPI_AVEncVideoMarkLTRFrame = (
            0xE42F4748, 0xA06D, 0x4EF9, 0x8C, 0xEA, 0x3D, 0x05, 0xFD, 0xE3, 0xBD, 0x3B
        )
        STATIC_CODECAPI_AVEncVideoUseLTRFrame = (
            0x00752DB8, 0x55F7, 0x4F80, 0x89, 0x5B, 0x27, 0x63, 0x91, 0x95, 0xF2, 0xAD
        )
        STATIC_CODECAPI_AVEncVideoROIEnabled = (
            0xD74F7F18, 0x44DD, 0x4B85, 0xAB, 0xA3, 0x5, 0xD9, 0xF4, 0x2A, 0x82, 0x80
        )
        STATIC_CODECAPI_AVEncVideoDirtyRectEnabled = (
            0x8ACB8FDD, 0x5E0C, 0x4C66, 0x87, 0x29, 0xB8, 0xF6, 0x29, 0xAB, 0x04, 0xFB
        )
        STATIC_CODECAPI_AVScenarioInfo = (
            0xB28A6E64, 0x3FF9, 0x446A, 0x8A, 0x4B, 0x0D, 0x7A, 0x53, 0x41, 0x32, 0x36
        )
        STATIC_CODECAPI_AVEncMPVGOPSizeMin = (
            0x7155CF20, 0xD440, 0x4852, 0xAD, 0x0F, 0x9C, 0x4A, 0xBF, 0xE3, 0x7A, 0x6A
        )
        STATIC_CODECAPI_AVEncMPVGOPSizeMax = (
            0xFE7DE4C4, 0x1936, 0x4FE2, 0xBD, 0xF7, 0x1F, 0x18, 0xCA, 0x1D, 0x00, 0x1F
        )
        STATIC_CODECAPI_AVEncVideoMaxCTBSize = (
            0x822363FF, 0xCEC8, 0x43E5, 0x92, 0xFD, 0xE0, 0x97, 0x48, 0x84, 0x85, 0xE9
        )
        STATIC_CODECAPI_AVEncVideoCTBSize = (
            0xD47DB8B2, 0xE73B, 0x4CB9, 0x8C, 0x3E, 0xBD, 0x87, 0x7D, 0x06, 0xD7, 0x7B
        )
        STATIC_CODECAPI_VideoEncoderDisplayContentType = (
            0x79B90B27, 0xF4B1, 0x42DC, 0x9D, 0xD7, 0xCD, 0xAF, 0x81, 0x35, 0xC4, 0x00
        )
        STATIC_CODECAPI_AVEncEnableVideoProcessing = (
            0x006F4BF6, 0x0EA3, 0x4D42, 0x87, 0x02, 0xB5, 0xD8, 0xBE, 0x0F, 0x7A, 0x92
        )
        STATIC_CODECAPI_AVEncVideoGradualIntraRefresh = (
            0x8F347DEE, 0xCB0D, 0x49BA, 0xB4, 0x62, 0xDB, 0x69, 0x27, 0xEE, 0x21, 0x01
        )
        STATIC_CODECAPI_GetOPMContext = (
            0x2F036C05, 0x4C14, 0x4689, 0x88, 0x39, 0x29, 0x4C, 0x6D, 0x73, 0xE0, 0x53
        )
        STATIC_CODECAPI_SetHDCPManagerContext = (
            0x6D2D1FC8, 0x3DC9, 0x47EB, 0xA1, 0xA2, 0x47, 0x1C, 0x80, 0xCD, 0x60, 0xD0
        )
        STATIC_CODECAPI_AVEncVideoMaxTemporalLayers = (
            0x9C668CFE, 0x08E1, 0x424A, 0x93, 0x4E, 0xB7, 0x64, 0xB0, 0x64, 0x80, 0x2A
        )
        STATIC_CODECAPI_AVEncVideoNumGOPsPerIDR = (
            0x83BC5BDB, 0x5B89, 0x4521, 0x8F, 0x66, 0x33, 0x15, 0x1C, 0x37, 0x31, 0x76
        )
        STATIC_CODECAPI_AVEncCommonAllowFrameDrops = (
            0xD8477DCB, 0x9598, 0x48E3, 0x8D, 0x0C, 0x75, 0x2B, 0xF2, 0x06, 0x09, 0x3E
        )
        STATIC_CODECAPI_AVEncVideoIntraLayerPrediction = (
            0xD3AF46B8, 0xBF47, 0x44BB, 0xA2, 0x83, 0x69, 0xF0, 0xB0, 0x22, 0x8F, 0xF9
        )
        STATIC_CODECAPI_AVEncVideoInstantTemporalUpSwitching = (
            0xA3308307, 0x0D96, 0x4BA4, 0xB1, 0xF0, 0xB9, 0x1A, 0x5E, 0x49, 0xDF, 0x10
        )
        STATIC_CODECAPI_AVEncLowPowerEncoder = (
            0xB668D582, 0x8BAD, 0x4F6A, 0x91, 0x41, 0x37, 0x5A, 0x95, 0x35, 0x8B, 0x6D
        )
        STATIC_CODECAPI_AVEnableInLoopDeblockFilter = (
            0xD2E8E399, 0x0623, 0x4BF3, 0x92, 0xA8, 0x4D, 0x18, 0x18, 0x52, 0x9D, 0xED
        )
        STATIC_CODECAPI_AVEncMuxOutputStreamType = (
            0xCEDD9E8F, 0x34D3, 0x44DB, 0xA1, 0xD8, 0xF8, 0x15, 0x20, 0x25, 0x4F, 0x3E
        )
        STATIC_CODECAPI_AVEncStatVideoOutputFrameRate = (
            0xBE747849, 0x9AB4, 0x4A63, 0x98, 0xFE, 0xF1, 0x43, 0xF0, 0x4F, 0x8E, 0xE9
        )
        STATIC_CODECAPI_AVEncStatVideoCodedFrames = (
            0xD47F8D61, 0x6F5A, 0x4A26, 0xBB, 0x9F, 0xCD, 0x95, 0x18, 0x46, 0x2B, 0xCD
        )
        STATIC_CODECAPI_AVEncStatVideoTotalFrames = (
            0xFDAA9916, 0x119A, 0x4222, 0x9A, 0xD6, 0x3F, 0x7C, 0xAB, 0x99, 0xCC, 0x8B
        )
        STATIC_CODECAPI_AVEncAudioIntervalToEncode = (
            0x866E4B4D, 0x725A, 0x467C, 0xBB, 0x01, 0xB4, 0x96, 0xB2, 0x3B, 0x25, 0xF9
        )
        STATIC_CODECAPI_AVEncAudioIntervalToSkip = (
            0x88C15F94, 0xC38C, 0x4796, 0xA9, 0xE8, 0x96, 0xE9, 0x67, 0x98, 0x3F, 0x26
        )
        STATIC_CODECAPI_AVEncAudioDualMono = (
            0x3648126B, 0xA3E8, 0x4329, 0x9B, 0x3A, 0x5C, 0xE5, 0x66, 0xA4, 0x3B, 0xD3
        )
        STATIC_CODECAPI_AVEncAudioMeanBitRate = (
            0x921295BB, 0x4FCA, 0x4679, 0xAA, 0xB8, 0x9E, 0x2A, 0x1D, 0x75, 0x33, 0x84
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel0 = (
            0xBC5D0B60, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel1 = (
            0xBC5D0B61, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel2 = (
            0xBC5D0B62, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel3 = (
            0xBC5D0B63, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel4 = (
            0xBC5D0B64, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel5 = (
            0xBC5D0B65, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel6 = (
            0xBC5D0B66, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel7 = (
            0xBC5D0B67, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel8 = (
            0xBC5D0B68, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel9 = (
            0xBC5D0B69, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel10 = (
            0xBC5D0B6A, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel11 = (
            0xBC5D0B6B, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel12 = (
            0xBC5D0B6C, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel13 = (
            0xBC5D0B6D, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel14 = (
            0xBC5D0B6E, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioMapDestChannel15 = (
            0xBC5D0B6F, 0xDF6A, 0x4E16, 0x98, 0x03, 0xB8, 0x20, 0x07, 0xA3, 0x0C, 0x8D
        )
        STATIC_CODECAPI_AVEncAudioInputContent = (
            0x3E226C2B, 0x60B9, 0x4A39, 0xB0, 0x0B, 0xA7, 0xB4, 0x0F, 0x70, 0xD5, 0x66
        )
        STATIC_CODECAPI_AVEncStatAudioPeakPCMValue = (
            0xDCE7FD34, 0xDC00, 0x4C16, 0x82, 0x1B, 0x35, 0xD9, 0xEB, 0x00, 0xFB, 0x1A
        )
        STATIC_CODECAPI_AVEncStatAudioAveragePCMValue = (
            0x979272F8, 0xD17F, 0x4E32, 0xBB, 0x73, 0x4E, 0x73, 0x1C, 0x68, 0xBA, 0x2D
        )
        STATIC_CODECAPI_AVEncStatAudioAverageBPS = (
            0xCA6724DB, 0x7059, 0x4351, 0x8B, 0x43, 0xF8, 0x21, 0x98, 0x82, 0x6A, 0x14
        )
        STATIC_CODECAPI_AVEncStatAverageBPS = (
            0xCA6724DB, 0x7059, 0x4351, 0x8B, 0x43, 0xF8, 0x21, 0x98, 0x82, 0x6A, 0x14
        )
        STATIC_CODECAPI_AVEncStatHardwareProcessorUtilitization = (
            0x995DC027, 0xCB95, 0x49E6, 0xB9, 0x1B, 0x59, 0x67, 0x75, 0x3C, 0xDC, 0xB8
        )
        STATIC_CODECAPI_AVEncStatHardwareBandwidthUtilitization = (
            0x0124BA9B, 0xDC41, 0x4826, 0xB4, 0x5F, 0x18, 0xAC, 0x01, 0xB3, 0xD5, 0xA8
        )
        STATIC_CODECAPI_AVEncMPVGOPSize = (
            0x95F31B26, 0x95A4, 0x41AA, 0x93, 0x03, 0x24, 0x6A, 0x7F, 0xC6, 0xEE, 0xF1
        )
        STATIC_CODECAPI_AVEncMPVGOPOpen = (
            0xB1D5D4A6, 0x3300, 0x49B1, 0xAE, 0x61, 0xA0, 0x99, 0x37, 0xAB, 0x0E, 0x49
        )
        STATIC_CODECAPI_AVEncMPVDefaultBPictureCount = (
            0x8D390AAC, 0xDC5C, 0x4200, 0xB5, 0x7F, 0x81, 0x4D, 0x04, 0xBA, 0xBA, 0xB2
        )
        STATIC_CODECAPI_AVEncMPVProfile = (
            0xDABB534A, 0x1D99, 0x4284, 0x97, 0x5A, 0xD9, 0x0E, 0x22, 0x39, 0xBA, 0xA1
        )
        STATIC_CODECAPI_AVEncMPVLevel = (
            0x6EE40C40, 0xA60C, 0x41EF, 0x8F, 0x50, 0x37, 0xC2, 0x24, 0x9E, 0x2C, 0xB3
        )
        STATIC_CODECAPI_AVEncMPVFrameFieldMode = (
            0xACB5DE96, 0x7B93, 0x4C2F, 0x88, 0x25, 0xB0, 0x29, 0x5F, 0xA9, 0x3B, 0xF4
        )
        STATIC_CODECAPI_AVEncMPVAddSeqEndCode = (
            0xA823178F, 0x57DF, 0x4C7A, 0xB8, 0xFD, 0xE5, 0xEC, 0x88, 0x87, 0x70, 0x8D
        )
        STATIC_CODECAPI_AVEncMPVGOPSInSeq = (
            0x993410D4, 0x2691, 0x4192, 0x99, 0x78, 0x98, 0xDC, 0x26, 0x03, 0x66, 0x9F
        )
        STATIC_CODECAPI_AVEncMPVUseConcealmentMotionVectors = (
            0xEC770CF3, 0x6908, 0x4B4B, 0xAA, 0x30, 0x7F, 0xB9, 0x86, 0x21, 0x4F, 0xEA
        )
        STATIC_CODECAPI_AVEncMPVSceneDetection = (
            0x552799F1, 0xDB4C, 0x405B, 0x8A, 0x3A, 0xC9, 0x3F, 0x2D, 0x06, 0x74, 0xDC
        )
        STATIC_CODECAPI_AVEncMPVGenerateHeaderSeqExt = (
            0xD5E78611, 0x082D, 0x4E6B, 0x98, 0xAF, 0x0F, 0x51, 0xAB, 0x13, 0x92, 0x22
        )
        STATIC_CODECAPI_AVEncMPVGenerateHeaderSeqDispExt = (
            0x6437AA6F, 0x5A3C, 0x4DE9, 0x8A, 0x16, 0x53, 0xD9, 0xC4, 0xAD, 0x32, 0x6F
        )
        STATIC_CODECAPI_AVEncMPVGenerateHeaderPicExt = (
            0x1B8464AB, 0x944F, 0x45F0, 0xB7, 0x4E, 0x3A, 0x58, 0xDA, 0xD1, 0x1F, 0x37
        )
        STATIC_CODECAPI_AVEncMPVGenerateHeaderPicDispExt = (
            0xC6412F84, 0xC03F, 0x4F40, 0xA0, 0x0C, 0x42, 0x93, 0xDF, 0x83, 0x95, 0xBB
        )
        STATIC_CODECAPI_AVEncMPVGenerateHeaderSeqScaleExt = (
            0x0722D62F, 0xDD59, 0x4A86, 0x9C, 0xD5, 0x64, 0x4F, 0x8E, 0x26, 0x53, 0xD8
        )
        STATIC_CODECAPI_AVEncMPVScanPattern = (
            0x7F8A478E, 0x7BBB, 0x4AE2, 0xB2, 0xFC, 0x96, 0xD1, 0x7F, 0xC4, 0xA2, 0xD6
        )
        STATIC_CODECAPI_AVEncMPVIntraDCPrecision = (
            0xA0116151, 0xCBC8, 0x4AF3, 0x97, 0xDC, 0xD0, 0x0C, 0xCE, 0xB8, 0x2D, 0x79
        )
        STATIC_CODECAPI_AVEncMPVQScaleType = (
            0x2B79EBB7, 0xF484, 0x4AF7, 0xBB, 0x58, 0xA2, 0xA1, 0x88, 0xC5, 0xCB, 0xBE
        )
        STATIC_CODECAPI_AVEncMPVIntraVLCTable = (
            0xA2B83FF5, 0x1A99, 0x405A, 0xAF, 0x95, 0xC5, 0x99, 0x7D, 0x55, 0x8D, 0x3A
        )
        STATIC_CODECAPI_AVEncMPVQuantMatrixIntra = (
            0x9BEA04F3, 0x6621, 0x442C, 0x8B, 0xA1, 0x3A, 0xC3, 0x78, 0x97, 0x96, 0x98
        )
        STATIC_CODECAPI_AVEncMPVQuantMatrixNonIntra = (
            0x87F441D8, 0x0997, 0x4BEB, 0xA0, 0x8E, 0x85, 0x73, 0xD4, 0x09, 0xCF, 0x75
        )
        STATIC_CODECAPI_AVEncMPVQuantMatrixChromaIntra = (
            0x9EB9ECD4, 0x018D, 0x4FFD, 0x8F, 0x2D, 0x39, 0xE4, 0x9F, 0x07, 0xB1, 0x7A
        )
        STATIC_CODECAPI_AVEncMPVQuantMatrixChromaNonIntra = (
            0x1415B6B1, 0x362A, 0x4338, 0xBA, 0x9A, 0x1E, 0xF5, 0x87, 0x03, 0xC0, 0x5B
        )
        STATIC_CODECAPI_AVEncMPALayer = (
            0x9D377230, 0xF91B, 0x453D, 0x9C, 0xE0, 0x78, 0x44, 0x54, 0x14, 0xC2, 0x2D
        )
        STATIC_CODECAPI_AVEncMPACodingMode = (
            0xB16ADE03, 0x4B93, 0x43D7, 0xA5, 0x50, 0x90, 0xB4, 0xFE, 0x22, 0x45, 0x37
        )
        STATIC_CODECAPI_AVEncDDService = (
            0xD2E1BEC7, 0x5172, 0x4D2A, 0xA5, 0x0E, 0x2F, 0x3B, 0x82, 0xB1, 0xDD, 0xF8
        )
        STATIC_CODECAPI_AVEncDDDialogNormalization = (
            0xD7055ACF, 0xF125, 0x437D, 0xA7, 0x04, 0x79, 0xC7, 0x9F, 0x04, 0x04, 0xA8
        )
        STATIC_CODECAPI_AVEncDDCentreDownMixLevel = (
            0xE285072C, 0xC958, 0x4A81, 0xAF, 0xD2, 0xE5, 0xE0, 0xDA, 0xF1, 0xB1, 0x48
        )
        STATIC_CODECAPI_AVEncDDSurroundDownMixLevel = (
            0x7B20D6E5, 0x0BCF, 0x4273, 0xA4, 0x87, 0x50, 0x6B, 0x04, 0x79, 0x97, 0xE9
        )
        STATIC_CODECAPI_AVEncDDProductionInfoExists = (
            0xB0B7FE5F, 0xB6AB, 0x4F40, 0x96, 0x4D, 0x8D, 0x91, 0xF1, 0x7C, 0x19, 0xE8
        )
        STATIC_CODECAPI_AVEncDDProductionRoomType = (
            0xDAD7AD60, 0x23D8, 0x4AB7, 0xA2, 0x84, 0x55, 0x69, 0x86, 0xD8, 0xA6, 0xFE
        )
        STATIC_CODECAPI_AVEncDDProductionMixLevel = (
            0x301D103A, 0xCBF9, 0x4776, 0x88, 0x99, 0x7C, 0x15, 0xB4, 0x61, 0xAB, 0x26
        )
        STATIC_CODECAPI_AVEncDDCopyright = (
            0x8694F076, 0xCD75, 0x481D, 0xA5, 0xC6, 0xA9, 0x04, 0xDC, 0xC8, 0x28, 0xF0
        )
        STATIC_CODECAPI_AVEncDDOriginalBitstream = (
            0x966AE800, 0x5BD3, 0x4FF9, 0x95, 0xB9, 0xD3, 0x05, 0x66, 0x27, 0x38, 0x56
        )
        STATIC_CODECAPI_AVEncDDDigitalDeemphasis = (
            0xE024A2C2, 0x947C, 0x45AC, 0x87, 0xD8, 0xF1, 0x03, 0x0C, 0x5C, 0x00, 0x82
        )
        STATIC_CODECAPI_AVEncDDDCHighPassFilter = (
            0x9565239F, 0x861C, 0x4AC8, 0xBF, 0xDA, 0xE0, 0x0C, 0xB4, 0xDB, 0x85, 0x48
        )
        STATIC_CODECAPI_AVEncDDChannelBWLowPassFilter = (
            0xE197821D, 0xD2E7, 0x43E2, 0xAD, 0x2C, 0x00, 0x58, 0x2F, 0x51, 0x85, 0x45
        )
        STATIC_CODECAPI_AVEncDDLFELowPassFilter = (
            0xD3B80F6F, 0x9D15, 0x45E5, 0x91, 0xBE, 0x01, 0x9C, 0x3F, 0xAB, 0x1F, 0x01
        )
        STATIC_CODECAPI_AVEncDDSurround90DegreeePhaseShift = (
            0x25ECEC9D, 0x3553, 0x42C0, 0xBB, 0x56, 0xD2, 0x57, 0x92, 0x10, 0x4F, 0x80
        )
        STATIC_CODECAPI_AVEncDDSurround3dBAttenuation = (
            0x4D43B99D, 0x31E2, 0x48B9, 0xBF, 0x2E, 0x5C, 0xBF, 0x1A, 0x57, 0x27, 0x84
        )
        STATIC_CODECAPI_AVEncDDDynamicRangeCompressionControl = (
            0xCFC2FF6D, 0x79B8, 0x4B8D, 0xA8, 0xAA, 0xA0, 0xC9, 0xBD, 0x1C, 0x29, 0x40
        )
        STATIC_CODECAPI_AVEncDDRFPreEmphasisFilter = (
            0x21AF44C0, 0x244E, 0x4F3D, 0xA2, 0xCC, 0x3D, 0x30, 0x68, 0xB2, 0xE7, 0x3F
        )
        STATIC_CODECAPI_AVEncDDSurroundExMode = (
            0x91607CEE, 0xDBDD, 0x4EB6, 0xBC, 0xA2, 0xAA, 0xDF, 0xAF, 0xA3, 0xDD, 0x68
        )
        STATIC_CODECAPI_AVEncDDPreferredStereoDownMixMode = (
            0x7F4E6B31, 0x9185, 0x403D, 0xB0, 0xA2, 0x76, 0x37, 0x43, 0xE6, 0xF0, 0x63
        )
        STATIC_CODECAPI_AVEncDDLtRtCenterMixLvl_x10 = (
            0xDCA128A2, 0x491F, 0x4600, 0xB2, 0xDA, 0x76, 0xE3, 0x34, 0x4B, 0x41, 0x97
        )
        STATIC_CODECAPI_AVEncDDLtRtSurroundMixLvl_x10 = (
            0x212246C7, 0x3D2C, 0x4DFA, 0xBC, 0x21, 0x65, 0x2A, 0x90, 0x98, 0x69, 0x0D
        )
        STATIC_CODECAPI_AVEncDDLoRoCenterMixLvl_x10 = (
            0x1CFBA222, 0x25B3, 0x4BF4, 0x9B, 0xFD, 0xE7, 0x11, 0x12, 0x67, 0x85, 0x8C
        )
        STATIC_CODECAPI_AVEncDDLoRoSurroundMixLvl_x10 = (
            0xE725CFF6, 0xEB56, 0x40C7, 0x84, 0x50, 0x2B, 0x93, 0x67, 0xE9, 0x15, 0x55
        )
        STATIC_CODECAPI_AVEncDDAtoDConverterType = (
            0x719F9612, 0x81A1, 0x47E0, 0x9A, 0x05, 0xD9, 0x4A, 0xD5, 0xFC, 0xA9, 0x48
        )
        STATIC_CODECAPI_AVEncDDHeadphoneMode = (
            0x4052DBEC, 0x52F5, 0x42F5, 0x9B, 0x00, 0xD1, 0x34, 0xB1, 0x34, 0x1B, 0x9D
        )
        STATIC_CODECAPI_AVEncWMVKeyFrameDistance = (
            0x5569055E, 0xE268, 0x4771, 0xB8, 0x3E, 0x95, 0x55, 0xEA, 0x28, 0xAE, 0xD3
        )
        STATIC_CODECAPI_AVEncWMVInterlacedEncoding = (
            0xE3D00F8A, 0xC6F5, 0x4E14, 0xA5, 0x88, 0x0E, 0xC8, 0x7A, 0x72, 0x6F, 0x9B
        )
        STATIC_CODECAPI_AVEncWMVDecoderComplexity = (
            0xF32C0DAB, 0xF3CB, 0x4217, 0xB7, 0x9F, 0x87, 0x62, 0x76, 0x8B, 0x5F, 0x67
        )
        STATIC_CODECAPI_AVEncWMVKeyFrameBufferLevelMarker = (
            0x51FF1115, 0x33AC, 0x426C, 0xA1, 0xB1, 0x09, 0x32, 0x1B, 0xDF, 0x96, 0xB4
        )
        STATIC_CODECAPI_AVEncWMVProduceDummyFrames = (
            0xD669D001, 0x183C, 0x42E3, 0xA3, 0xCA, 0x2F, 0x45, 0x86, 0xD2, 0x39, 0x6C
        )
        STATIC_CODECAPI_AVEncStatWMVCBAvg = (
            0x6AA6229F, 0xD602, 0x4B9D, 0xB6, 0x8C, 0xC1, 0xAD, 0x78, 0x88, 0x4B, 0xEF
        )
        STATIC_CODECAPI_AVEncStatWMVCBMax = (
            0xE976BEF8, 0x00FE, 0x44B4, 0xB6, 0x25, 0x8F, 0x23, 0x8B, 0xC0, 0x34, 0x99
        )
        STATIC_CODECAPI_AVEncStatWMVDecoderComplexityProfile = (
            0x89E69FC3, 0x0F9B, 0x436C, 0x97, 0x4A, 0xDF, 0x82, 0x12, 0x27, 0xC9, 0x0D
        )
        STATIC_CODECAPI_AVEncStatMPVSkippedEmptyFrames = (
            0x32195FD3, 0x590D, 0x4812, 0xA7, 0xED, 0x6D, 0x63, 0x9A, 0x1F, 0x97, 0x11
        )
        STATIC_CODECAPI_AVEncMP12PktzSTDBuffer = (
            0x0B751BD0, 0x819E, 0x478C, 0x94, 0x35, 0x75, 0x20, 0x89, 0x26, 0xB3, 0x77
        )
        STATIC_CODECAPI_AVEncMP12PktzStreamID = (
            0xC834D038, 0xF5E8, 0x4408, 0x9B, 0x60, 0x88, 0xF3, 0x64, 0x93, 0xFE, 0xDF
        )
        STATIC_CODECAPI_AVEncMP12PktzInitialPTS = (
            0x2A4F2065, 0x9A63, 0x4D20, 0xAE, 0x22, 0x0A, 0x1B, 0xC8, 0x96, 0xA3, 0x15
        )
        STATIC_CODECAPI_AVEncMP12PktzPacketSize = (
            0xAB71347A, 0x1332, 0x4DDE, 0xA0, 0xE5, 0xCC, 0xF7, 0xDA, 0x8A, 0x0F, 0x22
        )
        STATIC_CODECAPI_AVEncMP12PktzCopyright = (
            0xC8F4B0C1, 0x094C, 0x43C7, 0x8E, 0x68, 0xA5, 0x95, 0x40, 0x5A, 0x6E, 0xF8
        )
        STATIC_CODECAPI_AVEncMP12PktzOriginal = (
            0x6B178416, 0x31B9, 0x4964, 0x94, 0xCB, 0x6B, 0xFF, 0x86, 0x6C, 0xDF, 0x83
        )
        STATIC_CODECAPI_AVEncMP12MuxPacketOverhead = (
            0xE40BD720, 0x3955, 0x4453, 0xAC, 0xF9, 0xB7, 0x91, 0x32, 0xA3, 0x8F, 0xA0
        )
        STATIC_CODECAPI_AVEncMP12MuxNumStreams = (
            0xF7164A41, 0xDCED, 0x4659, 0xA8, 0xF2, 0xFB, 0x69, 0x3F, 0x2A, 0x4C, 0xD0
        )
        STATIC_CODECAPI_AVEncMP12MuxEarliestPTS = (
            0x157232B6, 0xF809, 0x474E, 0x94, 0x64, 0xA7, 0xF9, 0x30, 0x14, 0xA8, 0x17
        )
        STATIC_CODECAPI_AVEncMP12MuxLargestPacketSize = (
            0x35CEB711, 0xF461, 0x4B92, 0xA4, 0xEF, 0x17, 0xB6, 0x84, 0x1E, 0xD2, 0x54
        )
        STATIC_CODECAPI_AVEncMP12MuxInitialSCR = (
            0x3433AD21, 0x1B91, 0x4A0B, 0xB1, 0x90, 0x2B, 0x77, 0x06, 0x3B, 0x63, 0xA4
        )
        STATIC_CODECAPI_AVEncMP12MuxMuxRate = (
            0xEE047C72, 0x4BDB, 0x4A9D, 0x8E, 0x21, 0x41, 0x92, 0x6C, 0x82, 0x3D, 0xA7
        )
        STATIC_CODECAPI_AVEncMP12MuxPackSize = (
            0xF916053A, 0x1CE8, 0x4FAF, 0xAA, 0x0B, 0xBA, 0x31, 0xC8, 0x00, 0x34, 0xB8
        )
        STATIC_CODECAPI_AVEncMP12MuxSysSTDBufferBound = (
            0x35746903, 0xB545, 0x43E7, 0xBB, 0x35, 0xC5, 0xE0, 0xA7, 0xD5, 0x09, 0x3C
        )
        STATIC_CODECAPI_AVEncMP12MuxSysRateBound = (
            0x05F0428A, 0xEE30, 0x489D, 0xAE, 0x28, 0x20, 0x5C, 0x72, 0x44, 0x67, 0x10
        )
        STATIC_CODECAPI_AVEncMP12MuxTargetPacketizer = (
            0xD862212A, 0x2015, 0x45DD, 0x9A, 0x32, 0x1B, 0x3A, 0xA8, 0x82, 0x05, 0xA0
        )
        STATIC_CODECAPI_AVEncMP12MuxSysFixed = (
            0xCEFB987E, 0x894F, 0x452E, 0x8F, 0x89, 0xA4, 0xEF, 0x8C, 0xEC, 0x06, 0x3A
        )
        STATIC_CODECAPI_AVEncMP12MuxSysCSPS = (
            0x7952FF45, 0x9C0D, 0x4822, 0xBC, 0x82, 0x8A, 0xD7, 0x72, 0xE0, 0x29, 0x93
        )
        STATIC_CODECAPI_AVEncMP12MuxSysVideoLock = (
            0xB8296408, 0x2430, 0x4D37, 0xA2, 0xA1, 0x95, 0xB3, 0xE4, 0x35, 0xA9, 0x1D
        )
        STATIC_CODECAPI_AVEncMP12MuxSysAudioLock = (
            0x0FBB5752, 0x1D43, 0x47BF, 0xBD, 0x79, 0xF2, 0x29, 0x3D, 0x8C, 0xE3, 0x37
        )
        STATIC_CODECAPI_AVEncMP12MuxDVDNavPacks = (
            0xC7607CED, 0x8CF1, 0x4A99, 0x83, 0xA1, 0xEE, 0x54, 0x61, 0xBE, 0x35, 0x74
        )
        STATIC_CODECAPI_AVEncMPACopyright = (
            0xA6AE762A, 0xD0A9, 0x4454, 0xB8, 0xEF, 0xF2, 0xDB, 0xEE, 0xFD, 0xD3, 0xBD
        )
        STATIC_CODECAPI_AVEncMPAOriginalBitstream = (
            0x3CFB7855, 0x9CC9, 0x47FF, 0xB8, 0x29, 0xB3, 0x67, 0x86, 0xC9, 0x23, 0x46
        )
        STATIC_CODECAPI_AVEncMPAEnableRedundancyProtection = (
            0x5E54B09E, 0xB2E7, 0x4973, 0xA8, 0x9B, 0x0B, 0x36, 0x50, 0xA3, 0xBE, 0xDA
        )
        STATIC_CODECAPI_AVEncMPAPrivateUserBit = (
            0xAFA505CE, 0xC1E3, 0x4E3D, 0x85, 0x1B, 0x61, 0xB7, 0x00, 0xE5, 0xE6, 0xCC
        )
        STATIC_CODECAPI_AVEncMPAEmphasisType = (
            0x2D59FCDA, 0xBF4E, 0x4ED6, 0xB5, 0xDF, 0x5B, 0x03, 0xB3, 0x6B, 0x0A, 0x1F
        )
        STATIC_CODECAPI_AVDecCommonMeanBitRate = (
            0x59488217, 0x007A, 0x4F7A, 0x8E, 0x41, 0x5C, 0x48, 0xB1, 0xEA, 0xC5, 0xC6
        )
        STATIC_CODECAPI_AVDecCommonMeanBitRateInterval = (
            0x0EE437C6, 0x38A7, 0x4C5C, 0x94, 0x4C, 0x68, 0xAB, 0x42, 0x11, 0x6B, 0x85
        )
        STATIC_CODECAPI_AVDecCommonInputFormat = (
            0xE5005239, 0xBD89, 0x4BE3, 0x9C, 0x0F, 0x5D, 0xDE, 0x31, 0x79, 0x88, 0xCC
        )
        STATIC_CODECAPI_AVDecCommonOutputFormat = (
            0x3C790028, 0xC0CE, 0x4256, 0xB1, 0xA2, 0x1B, 0x0F, 0xC8, 0xB1, 0xDC, 0xDC
        )
        STATIC_CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_MatrixEncoded = (
            0x696E1D30, 0x548F, 0x4036, 0x82, 0x5F, 0x70, 0x26, 0xC6, 0x00, 0x11, 0xBD
        )
        STATIC_CODECAPI_GUID_AVDecAudioOutputFormat_PCM = (
            0x696E1D31, 0x548F, 0x4036, 0x82, 0x5F, 0x70, 0x26, 0xC6, 0x00, 0x11, 0xBD
        )
        STATIC_CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_PCM = (
            0x696E1D32, 0x548F, 0x4036, 0x82, 0x5F, 0x70, 0x26, 0xC6, 0x00, 0x11, 0xBD
        )
        STATIC_CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_Bitstream = (
            0x696E1D33, 0x548F, 0x4036, 0x82, 0x5F, 0x70, 0x26, 0xC6, 0x00, 0x11, 0xBD
        )
        STATIC_CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Headphones = (
            0x696E1D34, 0x548F, 0x4036, 0x82, 0x5F, 0x70, 0x26, 0xC6, 0x00, 0x11, 0xBD
        )
        STATIC_CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_Auto = (
            0x696E1D35, 0x548F, 0x4036, 0x82, 0x5F, 0x70, 0x26, 0xC6, 0x00, 0x11, 0xBD
        )
        STATIC_CODECAPI_AVDecVideoImageSize = (
            0x5EE5747C, 0x6801, 0x4CAB, 0xAA, 0xF1, 0x62, 0x48, 0xFA, 0x84, 0x1B, 0xA4
        )
        STATIC_CODECAPI_AVDecVideoInputScanType = (
            0x38477E1F, 0x0EA7, 0x42CD, 0x8C, 0xD1, 0x13, 0x0C, 0xED, 0x57, 0xC5, 0x80
        )
        STATIC_CODECAPI_AVDecVideoPixelAspectRatio = (
            0xB0CF8245, 0xF32D, 0x41DF, 0xB0, 0x2C, 0x87, 0xBD, 0x30, 0x4D, 0x12, 0xAB
        )
        STATIC_CODECAPI_AVDecVideoAcceleration_MPEG2 = (
            0xF7DB8A2E, 0x4F48, 0x4EE8, 0xAE, 0x31, 0x8B, 0x6E, 0xBE, 0x55, 0x8A, 0xE2
        )
        STATIC_CODECAPI_AVDecVideoAcceleration_H264 = (
            0xF7DB8A2F, 0x4F48, 0x4EE8, 0xAE, 0x31, 0x8B, 0x6E, 0xBE, 0x55, 0x8A, 0xE2
        )
        STATIC_CODECAPI_AVDecVideoAcceleration_VC1 = (
            0xF7DB8A30, 0x4F48, 0x4EE8, 0xAE, 0x31, 0x8B, 0x6E, 0xBE, 0x55, 0x8A, 0xE2
        )
        STATIC_CODECAPI_AVDecVideoProcDeinterlaceCSC = (
            0xF7DB8A31, 0x4F48, 0x4EE8, 0xAE, 0x31, 0x8B, 0x6E, 0xBE, 0x55, 0x8A, 0xE2
        )
        STATIC_CODECAPI_AVDecVideoThumbnailGenerationMode = (
            0x2EFD8EEE, 0x1150, 0x4328, 0x9C, 0xF5, 0x66, 0xDC, 0xE9, 0x33, 0xFC, 0xF4
        )
        STATIC_CODECAPI_AVDecVideoDropPicWithMissingRef = (
            0xF8226383, 0x14C2, 0x4567, 0x97, 0x34, 0x50,  0x4, 0xE9, 0x6F, 0xF8, 0x87
        )
        STATIC_CODECAPI_AVDecVideoSoftwareDeinterlaceMode = (
            0x0C08D1CE, 0x9CED, 0x4540, 0xBA, 0xE3, 0xCE, 0xB3, 0x80, 0x14, 0x11, 0x09
        )
        STATIC_CODECAPI_AVDecVideoFastDecodeMode = (
            0x6B529F7D, 0xD3B1, 0x49C6, 0xA9, 0x99, 0x9E, 0xC6, 0x91, 0x1B, 0xED, 0xBF
        )
        STATIC_CODECAPI_AVLowLatencyMode = (
            0x9C27891A, 0xED7A, 0x40E1, 0x88, 0xE8, 0xB2, 0x27, 0x27, 0xA0, 0x24, 0xEE
        )
        STATIC_CODECAPI_AVDecVideoH264ErrorConcealment = (
            0xECECACE8, 0x3436, 0x462C, 0x92, 0x94, 0xCD, 0x7B, 0xAC, 0xD7, 0x58, 0xA9
        )
        STATIC_CODECAPI_AVDecVideoMPEG2ErrorConcealment = (
            0x9D2BFE18, 0x728D, 0x48D2, 0xB3, 0x58, 0xBC, 0x7E, 0x43, 0x6C, 0x66, 0x74
        )
        STATIC_CODECAPI_AVDecVideoCodecType = (
            0x434528E5, 0x21F0, 0x46B6, 0xB6, 0x2C, 0x9B, 0x1B, 0x6B, 0x65, 0x8C, 0xD1
        )
        STATIC_CODECAPI_AVDecVideoDXVAMode = (
            0xF758F09E, 0x7337, 0x4AE7, 0x83, 0x87, 0x73, 0xDC, 0x2D, 0x54, 0xE6, 0x7D
        )
        STATIC_CODECAPI_AVDecVideoDXVABusEncryption = (
            0x42153C8B, 0xFD0B, 0x4765, 0xA4, 0x62, 0xDD, 0xD9, 0xE8, 0xBC, 0xC3, 0x88
        )
        STATIC_CODECAPI_AVDecVideoSWPowerLevel = (
            0xFB5D2347, 0x4DD8, 0x4509, 0xAE, 0xD0, 0xDB, 0x5F, 0xA9, 0xAA, 0x93, 0xF4
        )
        STATIC_CODECAPI_AVDecVideoMaxCodedWidth = (
            0x5AE557B8, 0x77AF, 0x41F5, 0x9F, 0xA6, 0x4D, 0xB2, 0xFE, 0x1D, 0x4B, 0xCA
        )
        STATIC_CODECAPI_AVDecVideoMaxCodedHeight = (
            0x7262A16A, 0xD2DC, 0x4E75, 0x9B, 0xA8, 0x65, 0xC0, 0xC6, 0xD3, 0x2B, 0x13
        )
        STATIC_CODECAPI_AVDecNumWorkerThreads = (
            0x9561C3E8, 0xEA9E, 0x4435, 0x9B, 0x1E, 0xA9, 0x3E, 0x69, 0x18, 0x94, 0xD8
        )
        STATIC_CODECAPI_AVDecSoftwareDynamicFormatChange = (
            0x862E2F0A, 0x507B, 0x47FF, 0xAF, 0x47,  0x1, 0xE2, 0x62, 0x42, 0x98, 0xB7
        )
        STATIC_CODECAPI_AVDecDisableVideoPostProcessing = (
            0xF8749193, 0x667A, 0x4F2C, 0xA9, 0xE8, 0x5D, 0x4A, 0xF9, 0x24, 0xF0, 0x8F
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputWMA = (
            0xC95E8DCF, 0x4058, 0x4204, 0x8C, 0x42, 0xCB, 0x24, 0xD9, 0x1E, 0x4B, 0x9B
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputWMAPro = (
            0x0128B7C7, 0xDA72, 0x4FE3, 0xBE, 0xF8, 0x5C, 0x52, 0xE3, 0x55, 0x77, 0x04
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputDolby = (
            0x8E4228A0, 0xF000, 0x4E0B, 0x8F, 0x54, 0xAB, 0x8D, 0x24, 0xAD, 0x61, 0xA2
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputDTS = (
            0x600BC0CA, 0x6A1F, 0x4E91, 0xB2, 0x41, 0x1B, 0xBE, 0xB1, 0xCB, 0x19, 0xE0
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputPCM = (
            0xF2421DA5, 0xBBB4, 0x4CD5, 0xA9, 0x96, 0x93, 0x3C, 0x6B, 0x5D, 0x13, 0x47
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputMPEG = (
            0x91106F36, 0x02C5, 0x4F75, 0x97, 0x19, 0x3B, 0x7A, 0xBF, 0x75, 0xE1, 0xF6
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputAAC = (
            0x97DF7828, 0xB94A, 0x47E2, 0xA4, 0xBC, 0x51, 0x19, 0x4D, 0xB2, 0x2A, 0x4D
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputHEAAC = (
            0x16EFB4AA, 0x330E, 0x4F5C, 0x98, 0xA8, 0xCF, 0x6A, 0xC5, 0x5C, 0xBE, 0x60
        )
        STATIC_CODECAPI_GUID_AVDecAudioInputDolbyDigitalPlus = (
            0x0803E185, 0x8F5D, 0x47F5, 0x99, 0x08, 0x19, 0xA5, 0xBB, 0xC9, 0xFE, 0x34
        )
        STATIC_CODECAPI_AVDecAACDownmixMode = (
            0x01274475, 0xF6BB, 0x4017, 0xB0, 0x84, 0x81, 0xA7, 0x63, 0xC9, 0x42, 0xD4
        )
        STATIC_CODECAPI_AVDecHEAACDynamicRangeControl = (
            0x287C8ABE, 0x69A4, 0x4D39, 0x80, 0x80, 0xD3, 0xD9, 0x71, 0x21, 0x78, 0xA0
        )
        STATIC_CODECAPI_AVDecAudioDualMono = (
            0x4A52CDA8, 0x30F8, 0x4216, 0xBE, 0x0F, 0xBA, 0x0B, 0x20, 0x25, 0x92, 0x1D
        )
        STATIC_CODECAPI_AVDecAudioDualMonoReproMode = (
            0xA5106186, 0xCC94, 0x4BC9, 0x8C, 0xD9, 0xAA, 0x2F, 0x61, 0xF6, 0x80, 0x7E
        )
        STATIC_CODECAPI_AVAudioChannelCount = (
            0x1D3583C4, 0x1583, 0x474E, 0xB7, 0x1A, 0x5E, 0xE4, 0x63, 0xC1, 0x98, 0xE4
        )
        STATIC_CODECAPI_AVAudioChannelConfig = (
            0x17F89CB3, 0xC38D, 0x4368, 0x9E, 0xDE, 0x63, 0xB9, 0x4D, 0x17, 0x7F, 0x9F
        )
        STATIC_CODECAPI_AVAudioSampleRate = (
            0x971D2723, 0x1ACB, 0x42E7, 0x85, 0x5C, 0x52, 0x0A, 0x4B, 0x70, 0xA5, 0xF2
        )
        STATIC_CODECAPI_AVDDSurroundMode = (
            0x99F2F386, 0x98D1, 0x4452, 0xA1, 0x63, 0xAB, 0xC7, 0x8A, 0x6E, 0xB7, 0x70
        )
        STATIC_CODECAPI_AVDecDDOperationalMode = (
            0xD6D6C6D1, 0x064E, 0x4FDD, 0xA4, 0x0E, 0x3E, 0xCB, 0xFC, 0xB7, 0xEB, 0xD0
        )
        STATIC_CODECAPI_AVDecDDMatrixDecodingMode = (
            0xDDC811A5, 0x04ED, 0x4BF3, 0xA0, 0xCA, 0xD0, 0x04, 0x49, 0xF9, 0x35, 0x5F
        )
        STATIC_CODECAPI_AVDecDDDynamicRangeScaleHigh = (
            0x50196C21, 0x1F33, 0x4AF5, 0xB2, 0x96, 0x11, 0x42, 0x6D, 0x6C, 0x87, 0x89
        )
        STATIC_CODECAPI_AVDecDDDynamicRangeScaleLow = (
            0x044E62E4, 0x11A5, 0x42D5, 0xA3, 0xB2, 0x3B, 0xB2, 0xC7, 0xC2, 0xD7, 0xCF
        )
        STATIC_CODECAPI_AVDecDDStereoDownMixMode = (
            0x6CE4122C, 0x3EE9, 0x4182, 0xB4, 0xAE, 0xC1, 0x0F, 0xC0, 0x88, 0x64, 0x9D
        )
        STATIC_CODECAPI_AVDSPLoudnessEqualization = (
            0x8AFD1A15, 0x1812, 0x4CBF, 0x93, 0x19, 0x43, 0x3A, 0x5B, 0x2A, 0x3B, 0x27
        )
        STATIC_CODECAPI_AVDSPSpeakerFill = (
            0x5612BCA1, 0x56DA, 0x4582, 0x8D, 0xA1, 0xCA, 0x80, 0x90, 0xF9, 0x27, 0x68
        )
        STATIC_CODECAPI_AVPriorityControl = (
            0x54BA3DC8, 0xBDDE, 0x4329, 0xB1, 0x87, 0x20, 0x18, 0xBC, 0x5C, 0x2B, 0xA1
        )
        STATIC_CODECAPI_AVRealtimeControl = (
            0x6F440632, 0xC4AD, 0x4BF7, 0x9E, 0x52, 0x45, 0x69, 0x42, 0xB4, 0x54, 0xB0
        )
        STATIC_CODECAPI_AVEncMaxFrameRate = (
            0xB98E1B31, 0x19FA, 0x4D4F, 0x99, 0x31, 0xD6, 0xA5, 0xB8, 0xAA, 0xB9, 0x3C
        )
        STATIC_CODECAPI_AVEncNoInputCopy = (
            0xD2B46A2A, 0xE8EE, 0x4EC5, 0x86, 0x9E, 0x44, 0x9B, 0x6C, 0x62, 0xC8, 0x1A
        )
        STATIC_CODECAPI_AVEncChromaEncodeMode = (
            0x8A47AB5A, 0x4798, 0x4C93, 0xB5, 0xA5, 0x55, 0x4F, 0x9A, 0x3B, 0x9F, 0x50
        )

        # end of static definitions }
        # Common Parameters
        # AVEncCommonFormatConstraint (GUID)
        CODECAPI_AVEncCommonFormatConstraint = DEFINE_CODECAPI_GUID(
            "57CBB9B8-116F-4951-B40C-C2A035ED8F17",
            0x57CBB9B8,
            0x116F,
            0x4951,
            0xB4,
            0x0C,
            0xC2,
            0xA0,
            0x35,
            0xED,
            0x8F,
            0x17
        )
        CODECAPI_GUID_AVEncCommonFormatUnSpecified = DEFINE_CODECAPI_GUID(
            "AF46A35A-6024-4525-A48A-094B97F5B3C2",
            0xAF46A35A,
            0x6024,
            0x4525,
            0xA4,
            0x8A,
            0x09,
            0x4B,
            0x97,
            0xF5,
            0xB3,
            0xC2
        )
        CODECAPI_GUID_AVEncCommonFormatDVD_V = DEFINE_CODECAPI_GUID(
            "CC9598C4-E7FE-451D-B1CA-761BC840B7F3",
            0xCC9598C4,
            0xE7FE,
            0x451D,
            0xB1,
            0xCA,
            0x76,
            0x1B,
            0xC8,
            0x40,
            0xB7,
            0xF3
        )
        CODECAPI_GUID_AVEncCommonFormatDVD_DashVR = DEFINE_CODECAPI_GUID(
            "E55199D6-044C-4DAE-A488-531ED306235B",
            0xE55199D6,
            0x044C,
            0x4DAE,
            0xA4,
            0x88,
            0x53,
            0x1E,
            0xD3,
            0x06,
            0x23,
            0x5B
        )
        CODECAPI_GUID_AVEncCommonFormatDVD_PlusVR = DEFINE_CODECAPI_GUID(
            "E74C6F2E-EC37-478D-9AF4-A5E135B6271C",
            0xE74C6F2E,
            0xEC37,
            0x478D,
            0x9A,
            0xF4,
            0xA5,
            0xE1,
            0x35,
            0xB6,
            0x27,
            0x1C
        )
        CODECAPI_GUID_AVEncCommonFormatVCD = DEFINE_CODECAPI_GUID(
            "95035BF7-9D90-40FF-AD5C-5CF8CF71CA1D",
            0x95035BF7,
            0x9D90,
            0x40FF,
            0xAD,
            0x5C,
            0x5C,
            0xF8,
            0xCF,
            0x71,
            0xCA,
            0x1D
        )
        CODECAPI_GUID_AVEncCommonFormatSVCD = DEFINE_CODECAPI_GUID(
            "51D85818-8220-448C-8066-D69BED16C9AD",
            0x51D85818,
            0x8220,
            0x448C,
            0x80,
            0x66,
            0xD6,
            0x9B,
            0xED,
            0x16,
            0xC9,
            0xAD
        )
        CODECAPI_GUID_AVEncCommonFormatATSC = DEFINE_CODECAPI_GUID(
            "8D7B897C-A019-4670-AA76-2EDCAC7AC296",
            0x8D7B897C,
            0xA019,
            0x4670,
            0xAA,
            0x76,
            0x2E,
            0xDC,
            0xAC,
            0x7A,
            0xC2,
            0x96
        )
        CODECAPI_GUID_AVEncCommonFormatDVB = DEFINE_CODECAPI_GUID(
            "71830D8F-6C33-430D-844B-C2705BAAE6DB",
            0x71830D8F,
            0x6C33,
            0x430D,
            0x84,
            0x4B,
            0xC2,
            0x70,
            0x5B,
            0xAA,
            0xE6,
            0xDB
        )
        CODECAPI_GUID_AVEncCommonFormatMP3 = DEFINE_CODECAPI_GUID(
            "349733CD-EB08-4DC2-8197-E49835EF828B",
            0x349733CD,
            0xEB08,
            0x4DC2,
            0x81,
            0x97,
            0xE4,
            0x98,
            0x35,
            0xEF,
            0x82,
            0x8B
        )
        CODECAPI_GUID_AVEncCommonFormatHighMAT = DEFINE_CODECAPI_GUID(
            "1EABE760-FB2B-4928-90D1-78DB88EEE889",
            0x1EABE760,
            0xFB2B,
            0x4928,
            0x90,
            0xD1,
            0x78,
            0xDB,
            0x88,
            0xEE,
            0xE8,
            0x89
        )
        CODECAPI_GUID_AVEncCommonFormatHighMPV = DEFINE_CODECAPI_GUID(
            "A2D25DB8-B8F9-42C2-8BC7-0B93CF604788",
            0xA2D25DB8,
            0xB8F9,
            0x42C2,
            0x8B,
            0xC7,
            0x0B,
            0x93,
            0xCF,
            0x60,
            0x47,
            0x88
        )

        # AVEncCodecType (GUID)
        CODECAPI_AVEncCodecType = DEFINE_CODECAPI_GUID(
            "08AF4AC1-F3F2-4C74-9DCF-37F2EC79F826",
            0x08AF4AC1,
            0xF3F2,
            0x4C74,
            0x9D,
            0xCF,
            0x37,
            0xF2,
            0xEC,
            0x79,
            0xF8,
            0x26
        )
        CODECAPI_GUID_AVEncMPEG1Video = DEFINE_CODECAPI_GUID(
            "C8DAFEFE-DA1E-4774-B27D-11830C16B1FE",
            0xC8DAFEFE,
            0xDA1E,
            0x4774,
            0xB2,
            0x7D,
            0x11,
            0x83,
            0x0C,
            0x16,
            0xB1,
            0xFE
        )
        CODECAPI_GUID_AVEncMPEG2Video = DEFINE_CODECAPI_GUID(
            "046DC19A-6677-4AAA-A31D-C1AB716F4560",
            0x046DC19A,
            0x6677,
            0x4AAA,
            0xA3,
            0x1D,
            0xC1,
            0xAB,
            0x71,
            0x6F,
            0x45,
            0x60
        )
        CODECAPI_GUID_AVEncMPEG1Audio = DEFINE_CODECAPI_GUID(
            "D4DD1362-CD4A-4CD6-8138-B94DB4542B04",
            0xD4DD1362,
            0xCD4A,
            0x4CD6,
            0x81,
            0x38,
            0xB9,
            0x4D,
            0xB4,
            0x54,
            0x2B,
            0x04
        )
        CODECAPI_GUID_AVEncMPEG2Audio = DEFINE_CODECAPI_GUID(
            "EE4CBB1F-9C3F-4770-92B5-FCB7C2A8D381",
            0xEE4CBB1F,
            0x9C3F,
            0x4770,
            0x92,
            0xB5,
            0xFC,
            0xB7,
            0xC2,
            0xA8,
            0xD3,
            0x81
        )
        CODECAPI_GUID_AVEncWMV = DEFINE_CODECAPI_GUID(
            "4E0FEF9B-1D43-41BD-B8BD-4D7BF7457A2A",
            0x4E0FEF9B,
            0x1D43,
            0x41BD,
            0xB8,
            0xBD,
            0x4D,
            0x7B,
            0xF7,
            0x45,
            0x7A,
            0x2A
        )
        CODECAPI_GUID_AVEndMPEG4Video = DEFINE_CODECAPI_GUID(
            "DD37B12A-9503-4F8B-B8D0-324A00C0A1CF",
            0xDD37B12A,
            0x9503,
            0x4F8B,
            0xB8,
            0xD0,
            0x32,
            0x4A,
            0x00,
            0xC0,
            0xA1,
            0xCF
        )
        CODECAPI_GUID_AVEncH264Video = DEFINE_CODECAPI_GUID(
            "95044EAB-31B3-47DE-8E75-38A42BB03E28",
            0x95044EAB,
            0x31B3,
            0x47DE,
            0x8E,
            0x75,
            0x38,
            0xA4,
            0x2B,
            0xB0,
            0x3E,
            0x28
        )
        CODECAPI_GUID_AVEncDV = DEFINE_CODECAPI_GUID(
            "09B769C7-3329-44FB-8954-FA30937D3D5A",
            0x09B769C7,
            0x3329,
            0x44FB,
            0x89,
            0x54,
            0xFA,
            0x30,
            0x93,
            0x7D,
            0x3D,
            0x5A
        )
        CODECAPI_GUID_AVEncWMAPro = DEFINE_CODECAPI_GUID(
            "1955F90C-33F7-4A68-AB81-53F5657125C4",
            0x1955F90C,
            0x33F7,
            0x4A68,
            0xAB,
            0x81,
            0x53,
            0xF5,
            0x65,
            0x71,
            0x25,
            0xC4
        )
        CODECAPI_GUID_AVEncWMALossless = DEFINE_CODECAPI_GUID(
            "55CA7265-23D8-4761-9031-B74FBE12F4C1",
            0x55CA7265,
            0x23D8,
            0x4761,
            0x90,
            0x31,
            0xB7,
            0x4F,
            0xBE,
            0x12,
            0xF4,
            0xC1
        )
        CODECAPI_GUID_AVEncWMAVoice = DEFINE_CODECAPI_GUID(
            "13ED18CB-50E8-4276-A288-A6AA228382D9",
            0x13ED18CB,
            0x50E8,
            0x4276,
            0xA2,
            0x88,
            0xA6,
            0xAA,
            0x22,
            0x83,
            0x82,
            0xD9
        )
        CODECAPI_GUID_AVEncDolbyDigitalPro = DEFINE_CODECAPI_GUID(
            "F5BE76CC-0FF8-40EB-9CB1-BBA94004D44F",
            0xF5BE76CC,
            0x0FF8,
            0x40EB,
            0x9C,
            0xB1,
            0xBB,
            0xA9,
            0x40,
            0x04,
            0xD4,
            0x4F
        )
        CODECAPI_GUID_AVEncDolbyDigitalConsumer = DEFINE_CODECAPI_GUID(
            "C1A7BF6C-0059-4BFA-94EF-EF747A768D52",
            0xC1A7BF6C,
            0x0059,
            0x4BFA,
            0x94,
            0xEF,
            0xEF,
            0x74,
            0x7A,
            0x76,
            0x8D,
            0x52
        )
        CODECAPI_GUID_AVEncDolbyDigitalPlus = DEFINE_CODECAPI_GUID(
            "698D1B80-F7DD-415C-971C-42492A2056C6",
            0x698D1B80,
            0xF7DD,
            0x415C,
            0x97,
            0x1C,
            0x42,
            0x49,
            0x2A,
            0x20,
            0x56,
            0xC6
        )
        CODECAPI_GUID_AVEncDTSHD = DEFINE_CODECAPI_GUID(
            "2052E630-469D-4BFB-80CA-1D656E7E918F",
            0x2052E630,
            0x469D,
            0x4BFB,
            0x80,
            0xCA,
            0x1D,
            0x65,
            0x6E,
            0x7E,
            0x91,
            0x8F
        )
        CODECAPI_GUID_AVEncDTS = DEFINE_CODECAPI_GUID(
            "45FBCAA2-5E6E-4AB0-8893-5903BEE93ACF",
            0x45FBCAA2,
            0x5E6E,
            0x4AB0,
            0x88,
            0x93,
            0x59,
            0x03,
            0xBE,
            0xE9,
            0x3A,
            0xCF
        )
        CODECAPI_GUID_AVEncMLP = DEFINE_CODECAPI_GUID(
            "05F73E29-F0D1-431E-A41C-A47432EC5A66",
            0x05F73E29,
            0xF0D1,
            0x431E,
            0xA4,
            0x1C,
            0xA4,
            0x74,
            0x32,
            0xEC,
            0x5A,
            0x66
        )
        CODECAPI_GUID_AVEncPCM = DEFINE_CODECAPI_GUID(
            "844BE7F4-26CF-4779-B386-CC05D187990C",
            0x844BE7F4,
            0x26CF,
            0x4779,
            0xB3,
            0x86,
            0xCC,
            0x05,
            0xD1,
            0x87,
            0x99,
            0x0C
        )
        CODECAPI_GUID_AVEncSDDS = DEFINE_CODECAPI_GUID(
            "1DC1B82F-11C8-4C71-B7B6-EE3EB9BC2B94",
            0x1DC1B82F,
            0x11C8,
            0x4C71,
            0xB7,
            0xB6,
            0xEE,
            0x3E,
            0xB9,
            0xBC,
            0x2B,
            0x94
        )

        # AVEncCommonRateControlMode (UINT32)
        CODECAPI_AVEncCommonRateControlMode = DEFINE_CODECAPI_GUID(
            "1C0608E9-370C-4710-8A58-CB6181C42423",
            0x1C0608E9,
            0x370C,
            0x4710,
            0x8A,
            0x58,
            0xCB,
            0x61,
            0x81,
            0xC4,
            0x24,
            0x23
        )


        class eAVEncCommonRateControlMode(ENUM):
            eAVEncCommonRateControlMode_CBR = 0
            eAVEncCommonRateControlMode_PeakConstrainedVBR = 1
            eAVEncCommonRateControlMode_UnconstrainedVBR = 2
            eAVEncCommonRateControlMode_Quality = 3
            eAVEncCommonRateControlMode_LowDelayVBR = 4
            eAVEncCommonRateControlMode_GlobalVBR = 5
            eAVEncCommonRateControlMode_GlobalLowDelayVBR = 6


        eAVEncCommonRateControlMode_CBR = eAVEncCommonRateControlMode.eAVEncCommonRateControlMode_CBR
        eAVEncCommonRateControlMode_PeakConstrainedVBR = eAVEncCommonRateControlMode.eAVEncCommonRateControlMode_PeakConstrainedVBR
        eAVEncCommonRateControlMode_UnconstrainedVBR = eAVEncCommonRateControlMode.eAVEncCommonRateControlMode_UnconstrainedVBR
        eAVEncCommonRateControlMode_Quality = eAVEncCommonRateControlMode.eAVEncCommonRateControlMode_Quality
        eAVEncCommonRateControlMode_LowDelayVBR = eAVEncCommonRateControlMode.eAVEncCommonRateControlMode_LowDelayVBR
        eAVEncCommonRateControlMode_GlobalVBR = eAVEncCommonRateControlMode.eAVEncCommonRateControlMode_GlobalVBR
        eAVEncCommonRateControlMode_GlobalLowDelayVBR = eAVEncCommonRateControlMode.eAVEncCommonRateControlMode_GlobalLowDelayVBR

        # AVEncCommonLowLatency (BOOL)
        CODECAPI_AVEncCommonLowLatency = DEFINE_CODECAPI_GUID(
            "9D3ECD55-89E8-490A-970A-0C9548D5A56E",
            0x9D3ECD55,
            0x89E8,
            0x490A,
            0x97,
            0x0A,
            0x0C,
            0x95,
            0x48,
            0xD5,
            0xA5,
            0x6E
        )

        # AVEncCommonMultipassMode (UINT32)
        CODECAPI_AVEncCommonMultipassMode = DEFINE_CODECAPI_GUID(
            "22533D4C-47E1-41B5-9352-A2B7780E7AC4",
            0x22533D4C,
            0x47E1,
            0x41B5,
            0x93,
            0x52,
            0xA2,
            0xB7,
            0x78,
            0x0E,
            0x7A,
            0xC4
        )

        # AVEncCommonPassStart (UINT32)
        CODECAPI_AVEncCommonPassStart = DEFINE_CODECAPI_GUID(
            "6A67739F-4EB5-4385-9928-F276A939EF95",
            0x6A67739F,
            0x4EB5,
            0x4385,
            0x99,
            0x28,
            0xF2,
            0x76,
            0xA9,
            0x39,
            0xEF,
            0x95
        )

        # AVEncCommonPassEnd (UINT32)
        CODECAPI_AVEncCommonPassEnd = DEFINE_CODECAPI_GUID(
            "0E3D01BC-C85C-467D-8B60-C41012EE3BF6",
            0x0E3D01BC,
            0xC85C,
            0x467D,
            0x8B,
            0x60,
            0xC4,
            0x10,
            0x12,
            0xEE,
            0x3B,
            0xF6
        )

        # AVEncCommonRealTime (BOOL)
        CODECAPI_AVEncCommonRealTime = DEFINE_CODECAPI_GUID(
            "143A0FF6-A131-43DA-B81E-98FBB8EC378E",
            0x143A0FF6,
            0xA131,
            0x43DA,
            0xB8,
            0x1E,
            0x98,
            0xFB,
            0xB8,
            0xEC,
            0x37,
            0x8E
        )

        # AVEncCommonQuality (UINT32)
        CODECAPI_AVEncCommonQuality = DEFINE_CODECAPI_GUID(
            "FCBF57A3-7EA5-4B0C-9644-69B40C39C391",
            0xFCBF57A3,
            0x7EA5,
            0x4B0C,
            0x96,
            0x44,
            0x69,
            0xB4,
            0x0C,
            0x39,
            0xC3,
            0x91
        )

        # AVEncCommonQualityVsSpeed (UINT32)
        CODECAPI_AVEncCommonQualityVsSpeed = DEFINE_CODECAPI_GUID(
            "98332DF8-03CD-476B-89FA-3F9E442DEC9F",
            0x98332DF8,
            0x03CD,
            0x476B,
            0x89,
            0xFA,
            0x3F,
            0x9E,
            0x44,
            0x2D,
            0xEC,
            0x9F
        )

        # AVEncCommonTranscodeEncodingProfile (BSTR)
        CODECAPI_AVEncCommonTranscodeEncodingProfile = DEFINE_CODECAPI_GUID(
            "6947787C-F508-4EA9-B1E9-A1FE3A49FBC9",
            0x6947787C,
            0xF508,
            0x4EA9,
            0xB1,
            0xE9,
            0xA1,
            0xFE,
            0x3A,
            0x49,
            0xFB,
            0xC9
        )

        # AVEncCommonMeanBitRate (UINT32)
        CODECAPI_AVEncCommonMeanBitRate = DEFINE_CODECAPI_GUID(
            "F7222374-2144-4815-B550-A37F8E12EE52",
            0xF7222374,
            0x2144,
            0x4815,
            0xB5,
            0x50,
            0xA3,
            0x7F,
            0x8E,
            0x12,
            0xEE,
            0x52
        )

        # AVEncCommonMeanBitRateInterval (UINT64)
        CODECAPI_AVEncCommonMeanBitRateInterval = DEFINE_CODECAPI_GUID(
            "BFAA2F0C-CB82-4BC0-8474-F06A8A0D0258",
            0xBFAA2F0C,
            0xCB82,
            0x4BC0,
            0x84,
            0x74,
            0xF0,
            0x6A,
            0x8A,
            0x0D,
            0x02,
            0x58
        )

        # AVEncCommonMaxBitRate (UINT32)
        CODECAPI_AVEncCommonMaxBitRate = DEFINE_CODECAPI_GUID(
            "9651EAE4-39B9-4EBF-85EF-D7F444EC7465",
            0x9651EAE4,
            0x39B9,
            0x4EBF,
            0x85,
            0xEF,
            0xD7,
            0xF4,
            0x44,
            0xEC,
            0x74,
            0x65
        )

        # AVEncCommonMinBitRate (UINT32)
        CODECAPI_AVEncCommonMinBitRate = DEFINE_CODECAPI_GUID(
            "101405B2-2083-4034-A806-EFBEDDD7C9FF",
            0x101405B2,
            0x2083,
            0x4034,
            0xA8,
            0x06,
            0xEF,
            0xBE,
            0xDD,
            0xD7,
            0xC9,
            0xFF
        )

        # AVEncCommonBufferSize (UINT32)
        CODECAPI_AVEncCommonBufferSize = DEFINE_CODECAPI_GUID(
            "0DB96574-B6A4-4C8B-8106-3773DE0310CD",
            0x0DB96574,
            0xB6A4,
            0x4C8B,
            0x81,
            0x06,
            0x37,
            0x73,
            0xDE,
            0x03,
            0x10,
            0xCD
        )

        # AVEncCommonBufferInLevel (UINT32)
        CODECAPI_AVEncCommonBufferInLevel = DEFINE_CODECAPI_GUID(
            "D9C5C8DB-FC74-4064-94E9-CD19F947ED45",
            0xD9C5C8DB,
            0xFC74,
            0x4064,
            0x94,
            0xE9,
            0xCD,
            0x19,
            0xF9,
            0x47,
            0xED,
            0x45
        )

        # AVEncCommonBufferOutLevel (UINT32)
        CODECAPI_AVEncCommonBufferOutLevel = DEFINE_CODECAPI_GUID(
            "CCAE7F49-D0BC-4E3D-A57E-FB5740140069",
            0xCCAE7F49,
            0xD0BC,
            0x4E3D,
            0xA5,
            0x7E,
            0xFB,
            0x57,
            0x40,
            0x14,
            0x00,
            0x69
        )

        # AVEncCommonStreamEndHandling (UINT32)
        CODECAPI_AVEncCommonStreamEndHandling = DEFINE_CODECAPI_GUID(
            "6AAD30AF-6BA8-4CCC-8FCA-18D19BEAEB1C",
            0x6AAD30AF,
            0x6BA8,
            0x4CCC,
            0x8F,
            0xCA,
            0x18,
            0xD1,
            0x9B,
            0xEA,
            0xEB,
            0x1C
        )


        class eAVEncCommonStreamEndHandling(ENUM):
            eAVEncCommonStreamEndHandling_DiscardPartial = 0
            eAVEncCommonStreamEndHandling_EnsureComplete = 1


        eAVEncCommonStreamEndHandling_DiscardPartial = eAVEncCommonStreamEndHandling.eAVEncCommonStreamEndHandling_DiscardPartial
        eAVEncCommonStreamEndHandling_EnsureComplete = eAVEncCommonStreamEndHandling.eAVEncCommonStreamEndHandling_EnsureComplete

        # Common Post Encode Statistical Parameters
        # AVEncStatCommonCompletedPasses (UINT32)
        CODECAPI_AVEncStatCommonCompletedPasses = DEFINE_CODECAPI_GUID(
            "3E5DE533-9DF7-438C-854F-9F7DD3683D34",
            0x3E5DE533,
            0x9DF7,
            0x438C,
            0x85,
            0x4F,
            0x9F,
            0x7D,
            0xD3,
            0x68,
            0x3D,
            0x34
        )

        # Common Video Parameters
        # AVEncVideoOutputFrameRate (UINT32)
        CODECAPI_AVEncVideoOutputFrameRate = DEFINE_CODECAPI_GUID(
            "EA85E7C3-9567-4D99-87C4-02C1C278CA7C",
            0xEA85E7C3,
            0x9567,
            0x4D99,
            0x87,
            0xC4,
            0x02,
            0xC1,
            0xC2,
            0x78,
            0xCA,
            0x7C
        )

        # AVEncVideoOutputFrameRateConversion (UINT32)
        CODECAPI_AVEncVideoOutputFrameRateConversion = DEFINE_CODECAPI_GUID(
            "8C068BF4-369A-4BA3-82FD-B2518FB3396E",
            0x8C068BF4,
            0x369A,
            0x4BA3,
            0x82,
            0xFD,
            0xB2,
            0x51,
            0x8F,
            0xB3,
            0x39,
            0x6E
        )


        class eAVEncVideoOutputFrameRateConversion(ENUM):
            eAVEncVideoOutputFrameRateConversion_Disable = 0
            eAVEncVideoOutputFrameRateConversion_Enable = 1
            eAVEncVideoOutputFrameRateConversion_Alias = 2


        eAVEncVideoOutputFrameRateConversion_Disable = eAVEncVideoOutputFrameRateConversion.eAVEncVideoOutputFrameRateConversion_Disable
        eAVEncVideoOutputFrameRateConversion_Enable = eAVEncVideoOutputFrameRateConversion.eAVEncVideoOutputFrameRateConversion_Enable
        eAVEncVideoOutputFrameRateConversion_Alias = eAVEncVideoOutputFrameRateConversion.eAVEncVideoOutputFrameRateConversion_Alias

        # AVEncVideoPixelAspectRatio (UINT32 as UINT16/UNIT16) < - - - - You
        # have WORD in the doc
        CODECAPI_AVEncVideoPixelAspectRatio = DEFINE_CODECAPI_GUID(
            "3CDC718F-B3E9-4EB6-A57F-CF1F1B321B87",
            0x3CDC718F,
            0xB3E9,
            0x4EB6,
            0xA5,
            0x7F,
            0xCF,
            0x1F,
            0x1B,
            0x32,
            0x1B,
            0x87
        )

        # AVDecVideoAcceleration_MPEG2 (UINT32)
        CODECAPI_AVDecVideoAcceleration_MPEG2 = DEFINE_CODECAPI_GUID(
            "F7DB8A2E-4F48-4EE8-AE31-8B6EBE558AE2",
            0xF7DB8A2E,
            0x4F48,
            0x4EE8,
            0xAE,
            0x31,
            0x8B,
            0x6E,
            0xBE,
            0x55,
            0x8A,
            0xE2
        )
        CODECAPI_AVDecVideoAcceleration_H264 = DEFINE_CODECAPI_GUID(
            "F7DB8A2F-4F48-4EE8-AE31-8B6EBE558AE2",
            0xF7DB8A2F,
            0x4F48,
            0x4EE8,
            0xAE,
            0x31,
            0x8B,
            0x6E,
            0xBE,
            0x55,
            0x8A,
            0xE2
        )
        CODECAPI_AVDecVideoAcceleration_VC1 = DEFINE_CODECAPI_GUID(
            "F7DB8A30-4F48-4EE8-AE31-8B6EBE558AE2",
            0xF7DB8A30,
            0x4F48,
            0x4EE8,
            0xAE,
            0x31,
            0x8B,
            0x6E,
            0xBE,
            0x55,
            0x8A,
            0xE2
        )

        # AVDecVideoProcDeinterlaceCSC (UINT32)
        CODECAPI_AVDecVideoProcDeinterlaceCSC = DEFINE_CODECAPI_GUID(
            "F7DB8A31-4F48-4EE8-AE31-8B6EBE558AE2",
            0xF7DB8A31,
            0x4F48,
            0x4EE8,
            0xAE,
            0x31,
            0x8B,
            0x6E,
            0xBE,
            0x55,
            0x8A,
            0xE2
        )

        # AVDecVideoThumbnailGenerationMode (BOOL)
        # Related to video thumbnail generation.
        # Video decoders can have special configurations for fast thumbnail
        # generation.
        # For example:
        # - They can use only one decoding thread so that multiple instances
        # can be used at the same time.
        # - They can also decode I frames only.
        CODECAPI_AVDecVideoThumbnailGenerationMode = DEFINE_CODECAPI_GUID(
            "2EFD8EEE-1150-4328-9CF5-66DCE933FCF4",
            0x2EFD8EEE,
            0x1150,
            0x4328,
            0x9C,
            0xF5,
            0x66,
            0xDC,
            0xE9,
            0x33,
            0xFC,
            0xF4
        )

        # AVDecVideoMaxCodedWidth and AVDecVideoMaxCodedHeight
        # Maximum codec width and height for current stream.
        # This is used to optimize memory usage for a particular stream.
        CODECAPI_AVDecVideoMaxCodedWidth = DEFINE_CODECAPI_GUID(
            "5AE557B8-77AF-41F5-9FA6-4DB2FE1D4BCA",
            0x5AE557B8,
            0x77AF,
            0x41F5,
            0x9F,
            0xA6,
            0x4D,
            0xB2,
            0xFE,
            0x1D,
            0x4B,
            0xCA
        )
        CODECAPI_AVDecVideoMaxCodedHeight = DEFINE_CODECAPI_GUID(
            "7262A16A-D2DC-4E75-9BA8-65C0C6D32B13",
            0x7262A16A,
            0xD2DC,
            0x4E75,
            0x9B,
            0xA8,
            0x65,
            0xC0,
            0xC6,
            0xD3,
            0x2B,
            0x13
        )

        # AVDecNumWorkerThreads (INT32)
        # Number of worker threads used in decoder core.
        # If this number is set to - 1, it means that the decoder will decide
        # how many threads to create.
        CODECAPI_AVDecNumWorkerThreads = DEFINE_CODECAPI_GUID(
            "9561C3E8-EA9E-4435-9B1E-A93E691894D8",
            0x9561C3E8,
            0xEA9E,
            0x4435,
            0x9B,
            0x1E,
            0xA9,
            0x3E,
            0x69,
            0x18,
            0x94,
            0xD8
        )

        # AVDecSoftwareDynamicFormatChange (BOOL)
        # Set whether to use software dynamic format change to internal
        # resizing
        CODECAPI_AVDecSoftwareDynamicFormatChange = DEFINE_CODECAPI_GUID(
            "862E2F0A-507B-47FF-AF47-01E2624298B7",
            0x862E2F0A,
            0x507B,
            0x47FF,
            0xAF,
            0x47,
            0x1,
            0xE2,
            0x62,
            0x42,
            0x98,
            0xB7
        )

        # AVDecDisableVideoPostProcessing (UINT32)
        # Default value is 0
        # If this is non - zero, decoder should not do post processing like
        # deblocking/deringing. This only controls the out of loop post
        # processing
        # all processing required by video standard
        # (like in - loop deblocking) should still be performed.
        CODECAPI_AVDecDisableVideoPostProcessing = DEFINE_CODECAPI_GUID(
            "F8749193-667A-4F2C-A9E8-5D4AF924F08F",
            0xF8749193,
            0x667A,
            0x4F2C,
            0xA9,
            0xE8,
            0x5D,
            0x4A,
            0xF9,
            0x24,
            0xF0,
            0x8F
        )

        # AVDecVideoDropPicWithMissingRef (BOOL)
        # Related to Video decoding mode of whether to drop pictures with
        # missing references.
        # For DVD playback, we may want to do so to aVOID bad blocking. For
        # Digital TV, we may
        # want to decode all pictures no matter what.
        CODECAPI_AVDecVideoDropPicWithMissingRef = DEFINE_CODECAPI_GUID(
            "F8226383-14C2-4567-9734-5004E96FF887",
            0xF8226383,
            0x14C2,
            0x4567,
            0x97,
            0x34,
            0x50,
            0x4,
            0xE9,
            0x6F,
            0xF8,
            0x87
        )

        # AVDecSoftwareVideoDeinterlaceMode (UINT32)
        CODECAPI_AVDecVideoSoftwareDeinterlaceMode = DEFINE_CODECAPI_GUID(
            "0C08D1CE-9CED-4540-BAE3-CEB380141109",
            0x0C08D1CE,
            0x9CED,
            0x4540,
            0xBA,
            0xE3,
            0xCE,
            0xB3,
            0x80,
            0x14,
            0x11,
            0x09
        )


        class eAVDecVideoSoftwareDeinterlaceMode(ENUM):
            eAVDecVideoSoftwareDeinterlaceMode_NoDeinterlacing = 0
            eAVDecVideoSoftwareDeinterlaceMode_ProgressiveDeinterlacing = 1
            eAVDecVideoSoftwareDeinterlaceMode_BOBDeinterlacing = 2
            eAVDecVideoSoftwareDeinterlaceMode_SmartBOBDeinterlacing = 3


        eAVDecVideoSoftwareDeinterlaceMode_NoDeinterlacing = eAVDecVideoSoftwareDeinterlaceMode.eAVDecVideoSoftwareDeinterlaceMode_NoDeinterlacing
        eAVDecVideoSoftwareDeinterlaceMode_ProgressiveDeinterlacing = eAVDecVideoSoftwareDeinterlaceMode.eAVDecVideoSoftwareDeinterlaceMode_ProgressiveDeinterlacing
        eAVDecVideoSoftwareDeinterlaceMode_BOBDeinterlacing = eAVDecVideoSoftwareDeinterlaceMode.eAVDecVideoSoftwareDeinterlaceMode_BOBDeinterlacing
        eAVDecVideoSoftwareDeinterlaceMode_SmartBOBDeinterlacing = eAVDecVideoSoftwareDeinterlaceMode.eAVDecVideoSoftwareDeinterlaceMode_SmartBOBDeinterlacing

        # AVDecVideoFastDecodeMode (UINT32)
        # 0: normal decoding
        # 1 - 32 : Where 32 is fastest decoding. Any value between
        # (and including) 1 to 32 is valid
        CODECAPI_AVDecVideoFastDecodeMode = DEFINE_CODECAPI_GUID(
            "6B529F7D-D3B1-49C6-A999-9EC6911BEDBF",
            0x6B529F7D,
            0xD3B1,
            0x49C6,
            0xA9,
            0x99,
            0x9E,
            0xC6,
            0x91,
            0x1B,
            0xED,
            0xBF
        )


        class eAVFastDecodeMode(ENUM):
            eVideoDecodeCompliant = 0
            eVideoDecodeOptimalLF = 1
            eVideoDecodeDisableLF = 2
            eVideoDecodeFastest = 32


        eVideoDecodeCompliant = eAVFastDecodeMode.eVideoDecodeCompliant
        eVideoDecodeOptimalLF = eAVFastDecodeMode.eVideoDecodeOptimalLF
        eVideoDecodeDisableLF = eAVFastDecodeMode.eVideoDecodeDisableLF
        eVideoDecodeFastest = eAVFastDecodeMode.eVideoDecodeFastest

        # AVLowLatencyMode (DWORD)
        # Related to low latency processing/decoding.
        # This GUID lets the application to decrease latency.
        CODECAPI_AVLowLatencyMode = DEFINE_CODECAPI_GUID(
            "9C27891A-ED7A-40E1-88E8-B22727A024EE",
            0x9C27891A,
            0xED7A,
            0x40E1,
            0x88,
            0xE8,
            0xB2,
            0x27,
            0x27,
            0xA0,
            0x24,
            0xEE
        )

        # AVDecVideoH264ErrorConcealment (UINT32)
        # Related to Video decoding mode of whether to conceal pictures with
        # corruptions.
        # For DVD playback, we may not want to do so to aVOID unnecessary
        # computation. For Digital TV, we may
        # want to perform error concealment.
        CODECAPI_AVDecVideoH264ErrorConcealment = DEFINE_CODECAPI_GUID(
            "ECECACE8-3436-462C-9294-CD7BACD758A9",
            0xECECACE8,
            0x3436,
            0x462C,
            0x92,
            0x94,
            0xCD,
            0x7B,
            0xAC,
            0xD7,
            0x58,
            0xA9
        )


        class eAVDecVideoH264ErrorConcealment(ENUM):
            eErrorConcealmentTypeDrop = 0

            # ERR_CONCEALMENT_TYPE_BASIC
            # (the default, and good mode used most of the time)
            eErrorConcealmentTypeBasic = 1
            eErrorConcealmentTypeAdvanced = 2
            eErrorConcealmentTypeDXVASetBlack = 3


        eErrorConcealmentTypeDrop = eAVDecVideoH264ErrorConcealment.eErrorConcealmentTypeDrop
        eErrorConcealmentTypeBasic = eAVDecVideoH264ErrorConcealment.eErrorConcealmentTypeBasic
        eErrorConcealmentTypeAdvanced = eAVDecVideoH264ErrorConcealment.eErrorConcealmentTypeAdvanced
        eErrorConcealmentTypeDXVASetBlack = eAVDecVideoH264ErrorConcealment.eErrorConcealmentTypeDXVASetBlack

        # AVDecVideoMPEG2ErrorConcealment (UINT32)
        # Related to Video decoding mode of whether to conceal pictures with
        # corruptions.
        # For DVD playback, we may not want to do so to aVOID unnecessary
        # computation. For Digital TV, we may
        # want to perform error concealment.
        CODECAPI_AVDecVideoMPEG2ErrorConcealment = DEFINE_CODECAPI_GUID(
            "9D2BFE18-728D-48D2-B358-BC7E436C6674",
            0x9D2BFE18,
            0x728D,
            0x48D2,
            0xB3,
            0x58,
            0xBC,
            0x7E,
            0x43,
            0x6C,
            0x66,
            0x74
        )


        class eAVDecVideoMPEG2ErrorConcealment(ENUM):
            eErrorConcealmentOff = 0
            eErrorConcealmentOn = 1


        eErrorConcealmentOff = eAVDecVideoMPEG2ErrorConcealment.eErrorConcealmentOff
        eErrorConcealmentOn = eAVDecVideoMPEG2ErrorConcealment.eErrorConcealmentOn

        # CODECAPI_AVDecVideoCodecType (UINT32)
        CODECAPI_AVDecVideoCodecType = DEFINE_CODECAPI_GUID(
            "434528E5-21F0-46B6-B62C-9B1B6B658CD1",
            0x434528E5,
            0x21F0,
            0x46B6,
            0xB6,
            0x2C,
            0x9B,
            0x1B,
            0x6B,
            0x65,
            0x8C,
            0xD1
        )


        class eAVDecVideoCodecType(ENUM):
            eAVDecVideoCodecType_NOTPLAYING = 0
            eAVDecVideoCodecType_MPEG2 = 1
            eAVDecVideoCodecType_H264 = 2


        eAVDecVideoCodecType_NOTPLAYING = eAVDecVideoCodecType.eAVDecVideoCodecType_NOTPLAYING
        eAVDecVideoCodecType_MPEG2 = eAVDecVideoCodecType.eAVDecVideoCodecType_MPEG2
        eAVDecVideoCodecType_H264 = eAVDecVideoCodecType.eAVDecVideoCodecType_H264

        # CODECAPI_AVDecVideoDXVAMode (UINT32)
        CODECAPI_AVDecVideoDXVAMode = DEFINE_CODECAPI_GUID(
            "F758F09E-7337-4AE7-8387-73DC2D54E67D",
            0xF758F09E,
            0x7337,
            0x4AE7,
            0x83,
            0x87,
            0x73,
            0xDC,
            0x2D,
            0x54,
            0xE6,
            0x7D
        )


        class eAVDecVideoDXVAMode(ENUM):
            eAVDecVideoDXVAMode_NOTPLAYING = 0
            eAVDecVideoDXVAMode_SW = 1
            eAVDecVideoDXVAMode_MC = 2
            eAVDecVideoDXVAMode_IDCT = 3
            eAVDecVideoDXVAMode_VLD = 4


        eAVDecVideoDXVAMode_NOTPLAYING = eAVDecVideoDXVAMode.eAVDecVideoDXVAMode_NOTPLAYING
        eAVDecVideoDXVAMode_SW = eAVDecVideoDXVAMode.eAVDecVideoDXVAMode_SW
        eAVDecVideoDXVAMode_MC = eAVDecVideoDXVAMode.eAVDecVideoDXVAMode_MC
        eAVDecVideoDXVAMode_IDCT = eAVDecVideoDXVAMode.eAVDecVideoDXVAMode_IDCT
        eAVDecVideoDXVAMode_VLD = eAVDecVideoDXVAMode.eAVDecVideoDXVAMode_VLD

        # CODECAPI_AVDecVideoDXVABusEncryption (UINT32)
        CODECAPI_AVDecVideoDXVABusEncryption = DEFINE_CODECAPI_GUID(
            "42153C8B-FD0B-4765-A462-DDD9E8BCC388",
            0x42153C8B,
            0xFD0B,
            0x4765,
            0xA4,
            0x62,
            0xDD,
            0xD9,
            0xE8,
            0xBC,
            0xC3,
            0x88
        )


        class eAVDecVideoDXVABusEncryption(ENUM):
            eAVDecVideoDXVABusEncryption_NONE = 0
            eAVDecVideoDXVABusEncryption_PRIVATE = 1
            eAVDecVideoDXVABusEncryption_AES = 2


        eAVDecVideoDXVABusEncryption_NONE = eAVDecVideoDXVABusEncryption.eAVDecVideoDXVABusEncryption_NONE
        eAVDecVideoDXVABusEncryption_PRIVATE = eAVDecVideoDXVABusEncryption.eAVDecVideoDXVABusEncryption_PRIVATE
        eAVDecVideoDXVABusEncryption_AES = eAVDecVideoDXVABusEncryption.eAVDecVideoDXVABusEncryption_AES

        # AVEncVideoForceSourceScanType (UINT32)
        CODECAPI_AVEncVideoForceSourceScanType = DEFINE_CODECAPI_GUID(
            "1EF2065F-058A-4765-A4FC-8A864C103012",
            0x1EF2065F,
            0x058A,
            0x4765,
            0xA4,
            0xFC,
            0x8A,
            0x86,
            0x4C,
            0x10,
            0x30,
            0x12
        )


        class eAVEncVideoSourceScanType(ENUM):
            eAVEncVideoSourceScan_Automatic = 0
            eAVEncVideoSourceScan_Interlaced = 1
            eAVEncVideoSourceScan_Progressive = 2


        eAVEncVideoSourceScan_Automatic = eAVEncVideoSourceScanType.eAVEncVideoSourceScan_Automatic
        eAVEncVideoSourceScan_Interlaced = eAVEncVideoSourceScanType.eAVEncVideoSourceScan_Interlaced
        eAVEncVideoSourceScan_Progressive = eAVEncVideoSourceScanType.eAVEncVideoSourceScan_Progressive

        # AVEncVideoNoOfFieldsToEncode (UINT64)
        CODECAPI_AVEncVideoNoOfFieldsToEncode = DEFINE_CODECAPI_GUID(
            "61E4BBE2-4EE0-40E7-80AB-51DDEEBE6291",
            0x61E4BBE2,
            0x4EE0,
            0x40E7,
            0x80,
            0xAB,
            0x51,
            0xDD,
            0xEE,
            0xBE,
            0x62,
            0x91
        )

        # AVEncVideoNoOfFieldsToSkip (UINT64)
        CODECAPI_AVEncVideoNoOfFieldsToSkip = DEFINE_CODECAPI_GUID(
            "A97E1240-1427-4C16-A7F7-3DCFD8BA4CC5",
            0xA97E1240,
            0x1427,
            0x4C16,
            0xA7,
            0xF7,
            0x3D,
            0xCF,
            0xD8,
            0xBA,
            0x4C,
            0xC5
        )

        # AVEncVideoEncodeDimension (UINT32)
        CODECAPI_AVEncVideoEncodeDimension = DEFINE_CODECAPI_GUID(
            "1074DF28-7E0F-47A4-A453-CDD73870F5CE",
            0x1074DF28,
            0x7E0F,
            0x47A4,
            0xA4,
            0x53,
            0xCD,
            0xD7,
            0x38,
            0x70,
            0xF5,
            0xCE
        )

        # AVEncVideoEncodeOffsetOrigin (UINT32)
        CODECAPI_AVEncVideoEncodeOffsetOrigin = DEFINE_CODECAPI_GUID(
            "6BC098FE-A71A-4454-852E-4D2DDEB2CD24",
            0x6BC098FE,
            0xA71A,
            0x4454,
            0x85,
            0x2E,
            0x4D,
            0x2D,
            0xDE,
            0xB2,
            0xCD,
            0x24
        )

        # AVEncVideoDisplayDimension (UINT32)
        CODECAPI_AVEncVideoDisplayDimension = DEFINE_CODECAPI_GUID(
            "DE053668-F4EC-47A9-86D0-836770F0C1D5",
            0xDE053668,
            0xF4EC,
            0x47A9,
            0x86,
            0xD0,
            0x83,
            0x67,
            0x70,
            0xF0,
            0xC1,
            0xD5
        )

        # AVEncVideoOutputScanType (UINT32)
        CODECAPI_AVEncVideoOutputScanType = DEFINE_CODECAPI_GUID(
            "460B5576-842E-49AB-A62D-B36F7312C9DB",
            0x460B5576,
            0x842E,
            0x49AB,
            0xA6,
            0x2D,
            0xB3,
            0x6F,
            0x73,
            0x12,
            0xC9,
            0xDB
        )


        class eAVEncVideoOutputScanType(ENUM):
            eAVEncVideoOutputScan_Progressive = 0
            eAVEncVideoOutputScan_Interlaced = 1
            eAVEncVideoOutputScan_SameAsInput = 2
            eAVEncVideoOutputScan_Automatic = 3


        eAVEncVideoOutputScan_Progressive = eAVEncVideoOutputScanType.eAVEncVideoOutputScan_Progressive
        eAVEncVideoOutputScan_Interlaced = eAVEncVideoOutputScanType.eAVEncVideoOutputScan_Interlaced
        eAVEncVideoOutputScan_SameAsInput = eAVEncVideoOutputScanType.eAVEncVideoOutputScan_SameAsInput
        eAVEncVideoOutputScan_Automatic = eAVEncVideoOutputScanType.eAVEncVideoOutputScan_Automatic

        # AVEncVideoInverseTelecineEnable (BOOL)
        CODECAPI_AVEncVideoInverseTelecineEnable = DEFINE_CODECAPI_GUID(
            "2EA9098B-E76D-4CCD-A030-D3B889C1B64C",
            0x2EA9098B,
            0xE76D,
            0x4CCD,
            0xA0,
            0x30,
            0xD3,
            0xB8,
            0x89,
            0xC1,
            0xB6,
            0x4C
        )

        # AVEncVideoInverseTelecineThreshold (UINT32)
        CODECAPI_AVEncVideoInverseTelecineThreshold = DEFINE_CODECAPI_GUID(
            "40247D84-E895-497F-B44C-B74560ACFE27",
            0x40247D84,
            0xE895,
            0x497F,
            0xB4,
            0x4C,
            0xB7,
            0x45,
            0x60,
            0xAC,
            0xFE,
            0x27
        )

        # AVEncVideoSourceFilmContent (UINT32)
        CODECAPI_AVEncVideoSourceFilmContent = DEFINE_CODECAPI_GUID(
            "1791C64B-CCFC-4827-A0ED-2557793B2B1C",
            0x1791C64B,
            0xCCFC,
            0x4827,
            0xA0,
            0xED,
            0x25,
            0x57,
            0x79,
            0x3B,
            0x2B,
            0x1C
        )


        class eAVEncVideoFilmContent(ENUM):
            eAVEncVideoFilmContent_VideoOnly = 0
            eAVEncVideoFilmContent_FilmOnly = 1
            eAVEncVideoFilmContent_Mixed = 2


        eAVEncVideoFilmContent_VideoOnly = eAVEncVideoFilmContent.eAVEncVideoFilmContent_VideoOnly
        eAVEncVideoFilmContent_FilmOnly = eAVEncVideoFilmContent.eAVEncVideoFilmContent_FilmOnly
        eAVEncVideoFilmContent_Mixed = eAVEncVideoFilmContent.eAVEncVideoFilmContent_Mixed

        # AVEncVideoSourceIsBW (BOOL)
        CODECAPI_AVEncVideoSourceIsBW = DEFINE_CODECAPI_GUID(
            "42FFC49B-1812-4FDC-8D24-7054C521E6EB",
            0x42FFC49B,
            0x1812,
            0x4FDC,
            0x8D,
            0x24,
            0x70,
            0x54,
            0xC5,
            0x21,
            0xE6,
            0xEB
        )

        # AVEncVideoFieldSwap (BOOL)
        CODECAPI_AVEncVideoFieldSwap = DEFINE_CODECAPI_GUID(
            "FEFD7569-4E0A-49F2-9F2B-360EA48C19A2",
            0xFEFD7569,
            0x4E0A,
            0x49F2,
            0x9F,
            0x2B,
            0x36,
            0x0E,
            0xA4,
            0x8C,
            0x19,
            0xA2
        )

        # AVEncVideoInputChromaResolution (UINT32)
        # AVEncVideoOutputChromaSubsamplingFormat (UINT32)
        CODECAPI_AVEncVideoInputChromaResolution = DEFINE_CODECAPI_GUID(
            "BB0CEC33-16F1-47B0-8A88-37815BEE1739",
            0xBB0CEC33,
            0x16F1,
            0x47B0,
            0x8A,
            0x88,
            0x37,
            0x81,
            0x5B,
            0xEE,
            0x17,
            0x39
        )
        CODECAPI_AVEncVideoOutputChromaResolution = DEFINE_CODECAPI_GUID(
            "6097B4C9-7C1D-4E64-BFCC-9E9765318AE7",
            0x6097B4C9,
            0x7C1D,
            0x4E64,
            0xBF,
            0xCC,
            0x9E,
            0x97,
            0x65,
            0x31,
            0x8A,
            0xE7
        )


        class eAVEncVideoChromaResolution(ENUM):
            eAVEncVideoChromaResolution_SameAsSource = 0
            eAVEncVideoChromaResolution_444 = 1
            eAVEncVideoChromaResolution_422 = 2
            eAVEncVideoChromaResolution_420 = 3
            eAVEncVideoChromaResolution_411 = 4


        eAVEncVideoChromaResolution_SameAsSource = eAVEncVideoChromaResolution.eAVEncVideoChromaResolution_SameAsSource
        eAVEncVideoChromaResolution_444 = eAVEncVideoChromaResolution.eAVEncVideoChromaResolution_444
        eAVEncVideoChromaResolution_422 = eAVEncVideoChromaResolution.eAVEncVideoChromaResolution_422
        eAVEncVideoChromaResolution_420 = eAVEncVideoChromaResolution.eAVEncVideoChromaResolution_420
        eAVEncVideoChromaResolution_411 = eAVEncVideoChromaResolution.eAVEncVideoChromaResolution_411

        # AVEncVideoInputChromaSubsampling (UINT32)
        # AVEncVideoOutputChromaSubsampling (UINT32)
        CODECAPI_AVEncVideoInputChromaSubsampling = DEFINE_CODECAPI_GUID(
            "A8E73A39-4435-4EC3-A6EA-98300F4B36F7",
            0xA8E73A39,
            0x4435,
            0x4EC3,
            0xA6,
            0xEA,
            0x98,
            0x30,
            0x0F,
            0x4B,
            0x36,
            0xF7
        )
        CODECAPI_AVEncVideoOutputChromaSubsampling = DEFINE_CODECAPI_GUID(
            "FA561C6C-7D17-44F0-83C9-32ED12E96343",
            0xFA561C6C,
            0x7D17,
            0x44F0,
            0x83,
            0xC9,
            0x32,
            0xED,
            0x12,
            0xE9,
            0x63,
            0x43
        )


        class eAVEncVideoChromaSubsampling(ENUM):
            eAVEncVideoChromaSubsamplingFormat_SameAsSource = 0
            eAVEncVideoChromaSubsamplingFormat_ProgressiveChroma = 0x8
            eAVEncVideoChromaSubsamplingFormat_Horizontally_Cosited = 0x4
            eAVEncVideoChromaSubsamplingFormat_Vertically_Cosited = 0x2
            eAVEncVideoChromaSubsamplingFormat_Vertically_AlignedChromaPlanes = (
                0x1
            )


        eAVEncVideoChromaSubsamplingFormat_SameAsSource = eAVEncVideoChromaSubsampling.eAVEncVideoChromaSubsamplingFormat_SameAsSource
        eAVEncVideoChromaSubsamplingFormat_ProgressiveChroma = eAVEncVideoChromaSubsampling.eAVEncVideoChromaSubsamplingFormat_ProgressiveChroma
        eAVEncVideoChromaSubsamplingFormat_Horizontally_Cosited = eAVEncVideoChromaSubsampling.eAVEncVideoChromaSubsamplingFormat_Horizontally_Cosited
        eAVEncVideoChromaSubsamplingFormat_Vertically_Cosited = eAVEncVideoChromaSubsampling.eAVEncVideoChromaSubsamplingFormat_Vertically_Cosited
        eAVEncVideoChromaSubsamplingFormat_Vertically_AlignedChromaPlanes = eAVEncVideoChromaSubsampling.eAVEncVideoChromaSubsamplingFormat_Vertically_AlignedChromaPlanes

        # AVEncVideoInputColorPrimaries (UINT32)
        # AVEncVideoOutputColorPrimaries (UINT32)
        CODECAPI_AVEncVideoInputColorPrimaries = DEFINE_CODECAPI_GUID(
            "C24D783F-7CE6-4278-90AB-28A4F1E5F86C",
            0xC24D783F,
            0x7CE6,
            0x4278,
            0x90,
            0xAB,
            0x28,
            0xA4,
            0xF1,
            0xE5,
            0xF8,
            0x6C
        )
        CODECAPI_AVEncVideoOutputColorPrimaries = DEFINE_CODECAPI_GUID(
            "BE95907C-9D04-4921-8985-A6D6D87D1A6C",
            0xBE95907C,
            0x9D04,
            0x4921,
            0x89,
            0x85,
            0xA6,
            0xD6,
            0xD8,
            0x7D,
            0x1A,
            0x6C
        )


        class eAVEncVideoColorPrimaries(ENUM):
            eAVEncVideoColorPrimaries_SameAsSource = 0
            eAVEncVideoColorPrimaries_Reserved = 1
            eAVEncVideoColorPrimaries_BT709 = 2
            eAVEncVideoColorPrimaries_BT470_2_SysM = 3
            eAVEncVideoColorPrimaries_BT470_2_SysBG = 4
            eAVEncVideoColorPrimaries_SMPTE170M = 5
            eAVEncVideoColorPrimaries_SMPTE240M = 6
            eAVEncVideoColorPrimaries_EBU3231 = 7
            eAVEncVideoColorPrimaries_SMPTE_C = 8


        eAVEncVideoColorPrimaries_SameAsSource = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_SameAsSource
        eAVEncVideoColorPrimaries_Reserved = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_Reserved
        eAVEncVideoColorPrimaries_BT709 = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_BT709
        eAVEncVideoColorPrimaries_BT470_2_SysM = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_BT470_2_SysM
        eAVEncVideoColorPrimaries_BT470_2_SysBG = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_BT470_2_SysBG
        eAVEncVideoColorPrimaries_SMPTE170M = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_SMPTE170M
        eAVEncVideoColorPrimaries_SMPTE240M = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_SMPTE240M
        eAVEncVideoColorPrimaries_EBU3231 = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_EBU3231
        eAVEncVideoColorPrimaries_SMPTE_C = eAVEncVideoColorPrimaries.eAVEncVideoColorPrimaries_SMPTE_C

        # AVEncVideoInputColorTransferFunction (UINT32)
        # AVEncVideoOutputColorTransferFunction (UINT32)
        CODECAPI_AVEncVideoInputColorTransferFunction = DEFINE_CODECAPI_GUID(
            "8C056111-A9C3-4B08-A0A0-CE13F8A27C75",
            0x8C056111,
            0xA9C3,
            0x4B08,
            0xA0,
            0xA0,
            0xCE,
            0x13,
            0xF8,
            0xA2,
            0x7C,
            0x75
        )
        CODECAPI_AVEncVideoOutputColorTransferFunction = DEFINE_CODECAPI_GUID(
            "4A7F884A-EA11-460D-BF57-B88BC75900DE",
            0x4A7F884A,
            0xEA11,
            0x460D,
            0xBF,
            0x57,
            0xB8,
            0x8B,
            0xC7,
            0x59,
            0x00,
            0xDE
        )


        class eAVEncVideoColorTransferFunction(ENUM):
            eAVEncVideoColorTransferFunction_SameAsSource = 0
            eAVEncVideoColorTransferFunction_10 = 1
            eAVEncVideoColorTransferFunction_18 = 2
            eAVEncVideoColorTransferFunction_20 = 3
            eAVEncVideoColorTransferFunction_22 = 4
            eAVEncVideoColorTransferFunction_22_709 = 5
            eAVEncVideoColorTransferFunction_22_240M = 6
            eAVEncVideoColorTransferFunction_22_8bit_sRGB = 7
            eAVEncVideoColorTransferFunction_28 = 8


        eAVEncVideoColorTransferFunction_SameAsSource = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_SameAsSource
        eAVEncVideoColorTransferFunction_10 = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_10
        eAVEncVideoColorTransferFunction_18 = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_18
        eAVEncVideoColorTransferFunction_20 = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_20
        eAVEncVideoColorTransferFunction_22 = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_22
        eAVEncVideoColorTransferFunction_22_709 = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_22_709
        eAVEncVideoColorTransferFunction_22_240M = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_22_240M
        eAVEncVideoColorTransferFunction_22_8bit_sRGB = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_22_8bit_sRGB
        eAVEncVideoColorTransferFunction_28 = eAVEncVideoColorTransferFunction.eAVEncVideoColorTransferFunction_28

        # AVEncVideoInputColorTransferMatrix (UINT32)
        # AVEncVideoOutputColorTransferMatrix (UINT32)
        CODECAPI_AVEncVideoInputColorTransferMatrix = DEFINE_CODECAPI_GUID(
            "52ED68B9-72D5-4089-958D-F5405D55081C",
            0x52ED68B9,
            0x72D5,
            0x4089,
            0x95,
            0x8D,
            0xF5,
            0x40,
            0x5D,
            0x55,
            0x08,
            0x1C
        )
        CODECAPI_AVEncVideoOutputColorTransferMatrix = DEFINE_CODECAPI_GUID(
            "A9B90444-AF40-4310-8FBE-ED6D933F892B",
            0xA9B90444,
            0xAF40,
            0x4310,
            0x8F,
            0xBE,
            0xED,
            0x6D,
            0x93,
            0x3F,
            0x89,
            0x2B
        )


        class eAVEncVideoColorTransferMatrix(ENUM):
            eAVEncVideoColorTransferMatrix_SameAsSource = 0
            eAVEncVideoColorTransferMatrix_BT709 = 1
            eAVEncVideoColorTransferMatrix_BT601 = 2
            eAVEncVideoColorTransferMatrix_SMPTE240M = 3


        eAVEncVideoColorTransferMatrix_SameAsSource = eAVEncVideoColorTransferMatrix.eAVEncVideoColorTransferMatrix_SameAsSource
        eAVEncVideoColorTransferMatrix_BT709 = eAVEncVideoColorTransferMatrix.eAVEncVideoColorTransferMatrix_BT709
        eAVEncVideoColorTransferMatrix_BT601 = eAVEncVideoColorTransferMatrix.eAVEncVideoColorTransferMatrix_BT601
        eAVEncVideoColorTransferMatrix_SMPTE240M = eAVEncVideoColorTransferMatrix.eAVEncVideoColorTransferMatrix_SMPTE240M

        # AVEncVideoInputColorLighting (UINT32)
        # AVEncVideoOutputColorLighting (UINT32)
        CODECAPI_AVEncVideoInputColorLighting = DEFINE_CODECAPI_GUID(
            "46A99549-0015-4A45-9C30-1D5CFA258316",
            0x46A99549,
            0x0015,
            0x4A45,
            0x9C,
            0x30,
            0x1D,
            0x5C,
            0xFA,
            0x25,
            0x83,
            0x16
        )
        CODECAPI_AVEncVideoOutputColorLighting = DEFINE_CODECAPI_GUID(
            "0E5AAAC6-ACE6-4C5C-998E-1A8C9C6C0F89",
            0x0E5AAAC6,
            0xACE6,
            0x4C5C,
            0x99,
            0x8E,
            0x1A,
            0x8C,
            0x9C,
            0x6C,
            0x0F,
            0x89
        )


        class eAVEncVideoColorLighting(ENUM):
            eAVEncVideoColorLighting_SameAsSource = 0
            eAVEncVideoColorLighting_Unknown = 1
            eAVEncVideoColorLighting_Bright = 2
            eAVEncVideoColorLighting_Office = 3
            eAVEncVideoColorLighting_Dim = 4
            eAVEncVideoColorLighting_Dark = 5


        eAVEncVideoColorLighting_SameAsSource = eAVEncVideoColorLighting.eAVEncVideoColorLighting_SameAsSource
        eAVEncVideoColorLighting_Unknown = eAVEncVideoColorLighting.eAVEncVideoColorLighting_Unknown
        eAVEncVideoColorLighting_Bright = eAVEncVideoColorLighting.eAVEncVideoColorLighting_Bright
        eAVEncVideoColorLighting_Office = eAVEncVideoColorLighting.eAVEncVideoColorLighting_Office
        eAVEncVideoColorLighting_Dim = eAVEncVideoColorLighting.eAVEncVideoColorLighting_Dim
        eAVEncVideoColorLighting_Dark = eAVEncVideoColorLighting.eAVEncVideoColorLighting_Dark

        # AVEncVideoInputColorNominalRange (UINT32)
        # AVEncVideoOutputColorNominalRange (UINT32)
        CODECAPI_AVEncVideoInputColorNominalRange = DEFINE_CODECAPI_GUID(
            "16CF25C6-A2A6-48E9-AE80-21AEC41D427E",
            0x16CF25C6,
            0xA2A6,
            0x48E9,
            0xAE,
            0x80,
            0x21,
            0xAE,
            0xC4,
            0x1D,
            0x42,
            0x7E
        )
        CODECAPI_AVEncVideoOutputColorNominalRange = DEFINE_CODECAPI_GUID(
            "972835ED-87B5-4E95-9500-C73958566E54",
            0x972835ED,
            0x87B5,
            0x4E95,
            0x95,
            0x00,
            0xC7,
            0x39,
            0x58,
            0x56,
            0x6E,
            0x54
        )


        class eAVEncVideoColorNominalRange(ENUM):
            eAVEncVideoColorNominalRange_SameAsSource = 0
            eAVEncVideoColorNominalRange_0_255 = 1
            eAVEncVideoColorNominalRange_16_235 = 2
            eAVEncVideoColorNominalRange_48_208 = 3


        eAVEncVideoColorNominalRange_SameAsSource = eAVEncVideoColorNominalRange.eAVEncVideoColorNominalRange_SameAsSource
        eAVEncVideoColorNominalRange_0_255 = eAVEncVideoColorNominalRange.eAVEncVideoColorNominalRange_0_255
        eAVEncVideoColorNominalRange_16_235 = eAVEncVideoColorNominalRange.eAVEncVideoColorNominalRange_16_235
        eAVEncVideoColorNominalRange_48_208 = eAVEncVideoColorNominalRange.eAVEncVideoColorNominalRange_48_208

        # AVEncInputVideoSystem (UINT32)
        CODECAPI_AVEncInputVideoSystem = DEFINE_CODECAPI_GUID(
            "BEDE146D-B616-4DC7-92B2-F5D9FA9298F7",
            0xBEDE146D,
            0xB616,
            0x4DC7,
            0x92,
            0xB2,
            0xF5,
            0xD9,
            0xFA,
            0x92,
            0x98,
            0xF7
        )


        class eAVEncInputVideoSystem(ENUM):
            eAVEncInputVideoSystem_Unspecified = 0
            eAVEncInputVideoSystem_PAL = 1
            eAVEncInputVideoSystem_NTSC = 2
            eAVEncInputVideoSystem_SECAM = 3
            eAVEncInputVideoSystem_MAC = 4
            eAVEncInputVideoSystem_HDV = 5
            eAVEncInputVideoSystem_Component = 6


        eAVEncInputVideoSystem_Unspecified = eAVEncInputVideoSystem.eAVEncInputVideoSystem_Unspecified
        eAVEncInputVideoSystem_PAL = eAVEncInputVideoSystem.eAVEncInputVideoSystem_PAL
        eAVEncInputVideoSystem_NTSC = eAVEncInputVideoSystem.eAVEncInputVideoSystem_NTSC
        eAVEncInputVideoSystem_SECAM = eAVEncInputVideoSystem.eAVEncInputVideoSystem_SECAM
        eAVEncInputVideoSystem_MAC = eAVEncInputVideoSystem.eAVEncInputVideoSystem_MAC
        eAVEncInputVideoSystem_HDV = eAVEncInputVideoSystem.eAVEncInputVideoSystem_HDV
        eAVEncInputVideoSystem_Component = eAVEncInputVideoSystem.eAVEncInputVideoSystem_Component

        # AVEncVideoHeaderDropFrame (UINT32)
        CODECAPI_AVEncVideoHeaderDropFrame = DEFINE_CODECAPI_GUID(
            "6ED9E124-7925-43FE-971B-E019F62222B4",
            0x6ED9E124,
            0x7925,
            0x43FE,
            0x97,
            0x1B,
            0xE0,
            0x19,
            0xF6,
            0x22,
            0x22,
            0xB4
        )

        # AVEncVideoHeaderHours (UINT32)
        CODECAPI_AVEncVideoHeaderHours = DEFINE_CODECAPI_GUID(
            "2ACC7702-E2DA-4158-BF9B-88880129D740",
            0x2ACC7702,
            0xE2DA,
            0x4158,
            0xBF,
            0x9B,
            0x88,
            0x88,
            0x01,
            0x29,
            0xD7,
            0x40
        )

        # AVEncVideoHeaderMinutes (UINT32)
        CODECAPI_AVEncVideoHeaderMinutes = DEFINE_CODECAPI_GUID(
            "DC1A99CE-0307-408B-880B-B8348EE8CA7F",
            0xDC1A99CE,
            0x0307,
            0x408B,
            0x88,
            0x0B,
            0xB8,
            0x34,
            0x8E,
            0xE8,
            0xCA,
            0x7F
        )

        # AVEncVideoHeaderSeconds (UINT32)
        CODECAPI_AVEncVideoHeaderSeconds = DEFINE_CODECAPI_GUID(
            "4A2E1A05-A780-4F58-8120-9A449D69656B",
            0x4A2E1A05,
            0xA780,
            0x4F58,
            0x81,
            0x20,
            0x9A,
            0x44,
            0x9D,
            0x69,
            0x65,
            0x6B
        )

        # AVEncVideoHeaderFrames (UINT32)
        CODECAPI_AVEncVideoHeaderFrames = DEFINE_CODECAPI_GUID(
            "AFD5F567-5C1B-4ADC-BDAF-735610381436",
            0xAFD5F567,
            0x5C1B,
            0x4ADC,
            0xBD,
            0xAF,
            0x73,
            0x56,
            0x10,
            0x38,
            0x14,
            0x36
        )

        # AVEncVideoDefaultUpperFieldDominant (BOOL)
        CODECAPI_AVEncVideoDefaultUpperFieldDominant = DEFINE_CODECAPI_GUID(
            "810167C4-0BC1-47CA-8FC2-57055A1474A5",
            0x810167C4,
            0x0BC1,
            0x47CA,
            0x8F,
            0xC2,
            0x57,
            0x05,
            0x5A,
            0x14,
            0x74,
            0xA5
        )

        # AVEncVideoCBRMotionTradeoff (UINT32)
        CODECAPI_AVEncVideoCBRMotionTradeoff = DEFINE_CODECAPI_GUID(
            "0D49451E-18D5-4367-A4EF-3240DF1693C4",
            0x0D49451E,
            0x18D5,
            0x4367,
            0xA4,
            0xEF,
            0x32,
            0x40,
            0xDF,
            0x16,
            0x93,
            0xC4
        )

        # AVEncVideoCodedVideoAccessUnitSize (UINT32)
        CODECAPI_AVEncVideoCodedVideoAccessUnitSize = DEFINE_CODECAPI_GUID(
            "B4B10C15-14A7-4CE8-B173-DC90A0B4FCDB",
            0xB4B10C15,
            0x14A7,
            0x4CE8,
            0xB1,
            0x73,
            0xDC,
            0x90,
            0xA0,
            0xB4,
            0xFC,
            0xDB
        )

        # AVEncVideoMaxKeyframeDistance (UINT32)
        CODECAPI_AVEncVideoMaxKeyframeDistance = DEFINE_CODECAPI_GUID(
            "2987123A-BA93-4704-B489-EC1E5F25292C",
            0x2987123A,
            0xBA93,
            0x4704,
            0xB4,
            0x89,
            0xEC,
            0x1E,
            0x5F,
            0x25,
            0x29,
            0x2C
        )

        # AVEncH264CABACEnable (BOOL)
        CODECAPI_AVEncH264CABACEnable = DEFINE_CODECAPI_GUID(
            "EE6CAD62-D305-4248-A50E-E1B255F7CAF8",
            0xEE6CAD62,
            0xD305,
            0x4248,
            0xA5,
            0xE,
            0xE1,
            0xB2,
            0x55,
            0xF7,
            0xCA,
            0xF8
        )

        # AVEncVideoContentType (UINT32)
        CODECAPI_AVEncVideoContentType = DEFINE_CODECAPI_GUID(
            "66117ACA-EB77-459D-930C-A48D9D0683FC",
            0x66117ACA,
            0xEB77,
            0x459D,
            0x93,
            0xC,
            0xA4,
            0x8D,
            0x9D,
            0x6,
            0x83,
            0xFC
        )


        class eAVEncVideoContentType(ENUM):
            eAVEncVideoContentType_Unknown = 0
            eAVEncVideoContentType_FixedCameraAngle = 1


        eAVEncVideoContentType_Unknown = eAVEncVideoContentType.eAVEncVideoContentType_Unknown
        eAVEncVideoContentType_FixedCameraAngle = eAVEncVideoContentType.eAVEncVideoContentType_FixedCameraAngle

        # AVEncNumWorkerThreads (UINT32)
        CODECAPI_AVEncNumWorkerThreads = DEFINE_CODECAPI_GUID(
            "B0C8BF60-16F7-4951-A30B-1DB1609293D6",
            0xB0C8BF60,
            0x16F7,
            0x4951,
            0xA3,
            0xB,
            0x1D,
            0xB1,
            0x60,
            0x92,
            0x93,
            0xD6
        )

        # AVEncVideoEncodeQP (UINT64)
        CODECAPI_AVEncVideoEncodeQP = DEFINE_CODECAPI_GUID(
            "2CB5696B-23FB-4CE1-A0F9-EF5B90FD55CA",
            0x2CB5696B,
            0x23FB,
            0x4CE1,
            0xA0,
            0xF9,
            0xEF,
            0x5B,
            0x90,
            0xFD,
            0x55,
            0xCA
        )

        # AVEncVideoMinQP (UINT32)
        CODECAPI_AVEncVideoMinQP = DEFINE_CODECAPI_GUID(
            "0EE22C6A-A37C-4568-B5F1-9D4C2B3AB886",
            0xEE22C6A,
            0xA37C,
            0x4568,
            0xB5,
            0xF1,
            0x9D,
            0x4C,
            0x2B,
            0x3A,
            0xB8,
            0x86
        )

        # AVEncVideoForceKeyFrame (UINT32)
        CODECAPI_AVEncVideoForceKeyFrame = DEFINE_CODECAPI_GUID(
            "398C1B98-8353-475A-9EF2-8F265D260345",
            0x398C1B98,
            0x8353,
            0x475A,
            0x9E,
            0xF2,
            0x8F,
            0x26,
            0x5D,
            0x26,
            0x3,
            0x45
        )

        # AVEncH264SPSID (UINT32)
        CODECAPI_AVEncH264SPSID = DEFINE_CODECAPI_GUID(
            "50F38F51-2B79-40E3-B39C-7E9FA0770501",
            0x50F38F51,
            0x2B79,
            0x40E3,
            0xB3,
            0x9C,
            0x7E,
            0x9F,
            0xA0,
            0x77,
            0x5,
            0x1
        )

        # AVEncH264PPSID (UINT32)
        CODECAPI_AVEncH264PPSID = DEFINE_CODECAPI_GUID(
            "BFE29EC2-056C-4D68-A38D-AE5944C8582E",
            0xBFE29EC2,
            0x56C,
            0x4D68,
            0xA3,
            0x8D,
            0xAE,
            0x59,
            0x44,
            0xC8,
            0x58,
            0x2E
        )

        # AVEncAdaptiveMode (UINT32)
        CODECAPI_AVEncAdaptiveMode = DEFINE_CODECAPI_GUID(
            "4419B185-DA1F-4F53-BC76-097D0C1EFB1E",
            0x4419B185,
            0xDA1F,
            0x4F53,
            0xBC,
            0x76,
            0x9,
            0x7D,
            0xC,
            0x1E,
            0xFB,
            0x1E
        )

        # AVScenarioInfo (UINT32)
        CODECAPI_AVScenarioInfo = DEFINE_CODECAPI_GUID(
            "B28A6E64-3FF9-446A-8A4B-0D7A53413236",
            0xB28A6E64,
            0x3FF9,
            0x446A,
            0x8A,
            0x4B,
            0x0D,
            0x7A,
            0x53,
            0x41,
            0x32,
            0x36
        )

        # AVEncMPVGOPSizeMin (UINT32)
        CODECAPI_AVEncMPVGOPSizeMin = DEFINE_CODECAPI_GUID(
            "7155CF20-D440-4852-AD0F-9C4ABFE37A6A",
            0x7155CF20,
            0xD440,
            0x4852,
            0xAD,
            0x0F,
            0x9C,
            0x4A,
            0xBF,
            0xE3,
            0x7A,
            0x6A
        )

        # AVEncMPVGOPSizeMax (UINT32)
        CODECAPI_AVEncMPVGOPSizeMax = DEFINE_CODECAPI_GUID(
            "FE7DE4C4-1936-4FE2-BDF7-1F18CA1D001F",
            0xFE7DE4C4,
            0x1936,
            0x4FE2,
            0xBD,
            0xF7,
            0x1F,
            0x18,
            0xCA,
            0x1D,
            0x00,
            0x1F
        )

        # AVEncVideoMaxCTBSize (UINT32)
        CODECAPI_AVEncVideoMaxCTBSize = DEFINE_CODECAPI_GUID(
            "822363FF-CEC8-43E5-92FD-E097488485E9",
            0x822363FF,
            0xCEC8,
            0x43E5,
            0x92,
            0xFD,
            0xE0,
            0x97,
            0x48,
            0x84,
            0x85,
            0xE9
        )

        # AVEncVideoCTBSize (UINT32)
        CODECAPI_AVEncVideoCTBSize = DEFINE_CODECAPI_GUID(
            "D47DB8B2-E73B-4CB9-8C3E-BD877D06D77B",
            0xD47DB8B2,
            0xE73B,
            0x4CB9,
            0x8C,
            0x3E,
            0xBD,
            0x87,
            0x7D,
            0x06,
            0xD7,
            0x7B
        )

        # VideoEncoderDisplayContentType (UINT32)
        CODECAPI_VideoEncoderDisplayContentType = DEFINE_CODECAPI_GUID(
            "79B90B27-F4B1-42DC-9DD7-CDAF8135C400",
            0x79B90B27,
            0xF4B1,
            0x42DC,
            0x9D,
            0xD7,
            0xCD,
            0xAF,
            0x81,
            0x35,
            0xC4,
            0x00
        )

        # AVEncEnableVideoProcessing (UINT32)
        CODECAPI_AVEncEnableVideoProcessing = DEFINE_CODECAPI_GUID(
            "006F4BF6-0EA3-4D42-8702-B5D8BE0F7A92",
            0x006F4BF6,
            0x0EA3,
            0x4D42,
            0x87,
            0x02,
            0xB5,
            0xD8,
            0xBE,
            0x0F,
            0x7A,
            0x92
        )

        # AVEncVideoGradualIntraRefresh (UINT32)
        CODECAPI_AVEncVideoGradualIntraRefresh = DEFINE_CODECAPI_GUID(
            "8F347DEE-CB0D-49BA-B462-DB6927EE2101",
            0x8F347DEE,
            0xCB0D,
            0x49BA,
            0xB4,
            0x62,
            0xDB,
            0x69,
            0x27,
            0xEE,
            0x21,
            0x01
        )

        # GetOPMContext (UINT64)
        CODECAPI_GetOPMContext = DEFINE_CODECAPI_GUID(
            "2F036C05-4C14-4689-8839-294C6D73E053",
            0x2F036C05,
            0x4C14,
            0x4689,
            0x88,
            0x39,
            0x29,
            0x4C,
            0x6D,
            0x73,
            0xE0,
            0x53
        )

        # SetHDCPManagerContext (VOID)
        CODECAPI_SetHDCPManagerContext = DEFINE_CODECAPI_GUID(
            "6D2D1FC8-3DC9-47EB-A1A2-471C80CD60D0",
            0x6D2D1FC8,
            0x3DC9,
            0x47EB,
            0xA1,
            0xA2,
            0x47,
            0x1C,
            0x80,
            0xCD,
            0x60,
            0xD0
        )

        # AVEncVideoMaxTemporalLayers (UINT32)
        CODECAPI_AVEncVideoMaxTemporalLayers = DEFINE_CODECAPI_GUID(
            "9C668CFE-08E1-424A-934E-B764B064802A",
            0x9C668CFE,
            0x08E1,
            0x424A,
            0x93,
            0x4E,
            0xB7,
            0x64,
            0xB0,
            0x64,
            0x80,
            0x2A
        )

        # AVEncVideoNumGOPsPerIDR (UINT32)
        CODECAPI_AVEncVideoNumGOPsPerIDR = DEFINE_CODECAPI_GUID(
            "83BC5BDB-5B89-4521-8F66-33151C373176",
            0x83BC5BDB,
            0x5B89,
            0x4521,
            0x8F,
            0x66,
            0x33,
            0x15,
            0x1C,
            0x37,
            0x31,
            0x76
        )

        # AVEncCommonAllowFrameDrops (UINT32)
        CODECAPI_AVEncCommonAllowFrameDrops = DEFINE_CODECAPI_GUID(
            "D8477DCB-9598-48E3-8D0C-752BF206093E",
            0xD8477DCB,
            0x9598,
            0x48E3,
            0x8D,
            0x0C,
            0x75,
            0x2B,
            0xF2,
            0x06,
            0x09,
            0x3E
        )

        # AVEncVideoIntraLayerPrediction (UINT32)
        CODECAPI_AVEncVideoIntraLayerPrediction = DEFINE_CODECAPI_GUID(
            "D3AF46B8-BF47-44BB-A283-69F0B0228FF9",
            0xD3AF46B8,
            0xBF47,
            0x44BB,
            0xA2,
            0x83,
            0x69,
            0xF0,
            0xB0,
            0x22,
            0x8F,
            0xF9
        )

        # AVEncVideoInstantTemporalUpSwitching (UINT32)
        CODECAPI_AVEncVideoInstantTemporalUpSwitching = DEFINE_CODECAPI_GUID(
            "A3308307-0D96-4BA4-B1F0-B91A5E49DF10",
            0xA3308307,
            0x0D96,
            0x4BA4,
            0xB1,
            0xF0,
            0xB9,
            0x1A,
            0x5E,
            0x49,
            0xDF,
            0x10
        )

        # AVEncLowPowerEncoder (UINT32)
        CODECAPI_AVEncLowPowerEncoder = DEFINE_CODECAPI_GUID(
            "B668D582-8BAD-4F6A-9141-375A95358B6D",
            0xB668D582,
            0x8BAD,
            0x4F6A,
            0x91,
            0x41,
            0x37,
            0x5A,
            0x95,
            0x35,
            0x8B,
            0x6D
        )

        # AVEnableInLoopDeblockFilter (UINT32)
        CODECAPI_AVEnableInLoopDeblockFilter = DEFINE_CODECAPI_GUID(
            "D2E8E399-0623-4BF3-92A8-4D1818529DED",
            0xD2E8E399,
            0x0623,
            0x4BF3,
            0x92,
            0xA8,
            0x4D,
            0x18,
            0x18,
            0x52,
            0x9D,
            0xED
        )


        class eAVEncAdaptiveMode(ENUM):
            eAVEncAdaptiveMode_None = 0
            eAVEncAdaptiveMode_Resolution = 1
            eAVEncAdaptiveMode_FrameRate = 2


        eAVEncAdaptiveMode_None = eAVEncAdaptiveMode.eAVEncAdaptiveMode_None
        eAVEncAdaptiveMode_Resolution = eAVEncAdaptiveMode.eAVEncAdaptiveMode_Resolution
        eAVEncAdaptiveMode_FrameRate = eAVEncAdaptiveMode.eAVEncAdaptiveMode_FrameRate


        class eAVScenarioInfo(ENUM):
            eAVScenarioInfo_Unknown = 0
            eAVScenarioInfo_DisplayRemoting = 1
            eAVScenarioInfo_VideoConference = 2
            eAVScenarioInfo_Archive = 3
            eAVScenarioInfo_LiveStreaming = 4
            eAVScenarioInfo_CameraRecord = 5
            eAVScenarioInfo_DisplayRemotingWithFeatureMap = 6


        eAVScenarioInfo_Unknown = eAVScenarioInfo.eAVScenarioInfo_Unknown
        eAVScenarioInfo_DisplayRemoting = eAVScenarioInfo.eAVScenarioInfo_DisplayRemoting
        eAVScenarioInfo_VideoConference = eAVScenarioInfo.eAVScenarioInfo_VideoConference
        eAVScenarioInfo_Archive = eAVScenarioInfo.eAVScenarioInfo_Archive
        eAVScenarioInfo_LiveStreaming = eAVScenarioInfo.eAVScenarioInfo_LiveStreaming
        eAVScenarioInfo_CameraRecord = eAVScenarioInfo.eAVScenarioInfo_CameraRecord
        eAVScenarioInfo_DisplayRemotingWithFeatureMap = eAVScenarioInfo.eAVScenarioInfo_DisplayRemotingWithFeatureMap


        class eVideoEncoderDisplayContentType(ENUM):
            eVideoEncoderDisplayContent_Unknown = 0
            eVideoEncoderDisplayContent_FullScreenVideo = 1


        eVideoEncoderDisplayContent_Unknown = eVideoEncoderDisplayContentType.eVideoEncoderDisplayContent_Unknown
        eVideoEncoderDisplayContent_FullScreenVideo = eVideoEncoderDisplayContentType.eVideoEncoderDisplayContent_FullScreenVideo

        # AVEncVideoSelectLayer (UINT32)
        CODECAPI_AVEncVideoSelectLayer = DEFINE_CODECAPI_GUID(
            "EB1084F5-6AAA-4914-BB2F-6147227F12E7",
            0xEB1084F5,
            0x6AAA,
            0x4914,
            0xBB,
            0x2F,
            0x61,
            0x47,
            0x22,
            0x7F,
            0x12,
            0xE7
        )

        # AVEncVideoTemporalLayerCount (UINT32)
        CODECAPI_AVEncVideoTemporalLayerCount = DEFINE_CODECAPI_GUID(
            "19CAEBFF-B74D-4CFD-8C27-C2F9D97D5F52",
            0x19CAEBFF,
            0xB74D,
            0x4CFD,
            0x8C,
            0x27,
            0xC2,
            0xF9,
            0xD9,
            0x7D,
            0x5F,
            0x52
        )

        # AVEncVideoUsage (UINT32)
        CODECAPI_AVEncVideoUsage = DEFINE_CODECAPI_GUID(
            "1F636849-5DC1-49F1-B1D8-CE3CF62EA385",
            0x1F636849,
            0x5DC1,
            0x49F1,
            0xB1,
            0xD8,
            0xCE,
            0x3C,
            0xF6,
            0x2E,
            0xA3,
            0x85
        )

        # AVEncVideoRateControlParams (UINT64)
        CODECAPI_AVEncVideoRateControlParams = DEFINE_CODECAPI_GUID(
            "87D43767-7645-44EC-B438-D3322FBCA29F",
            0x87D43767,
            0x7645,
            0x44EC,
            0xB4,
            0x38,
            0xD3,
            0x32,
            0x2F,
            0xBC,
            0xA2,
            0x9F
        )

        # AVEncVideoSupportedControls (UINT64)
        CODECAPI_AVEncVideoSupportedControls = DEFINE_CODECAPI_GUID(
            "D3F40FDD-77B9-473D-8196-061259E69CFF",
            0xD3F40FDD,
            0x77B9,
            0x473D,
            0x81,
            0x96,
            0x06,
            0x12,
            0x59,
            0xE6,
            0x9C,
            0xFF
        )

        # AVEncVideoEncodeFrameTypeQP (UINT64)
        CODECAPI_AVEncVideoEncodeFrameTypeQP = DEFINE_CODECAPI_GUID(
            "AA70B610-E03F-450C-AD07-07314E639CE7",
            0xAA70B610,
            0xE03F,
            0x450C,
            0xAD,
            0x07,
            0x07,
            0x31,
            0x4E,
            0x63,
            0x9C,
            0xE7
        )

        # AVEncSliceControlMode (UINT32)
        CODECAPI_AVEncSliceControlMode = DEFINE_CODECAPI_GUID(
            "E9E782EF-5F18-44C9-A90B-E9C3C2C17B0B",
            0xE9E782EF,
            0x5F18,
            0x44C9,
            0xA9,
            0x0B,
            0xE9,
            0xC3,
            0xC2,
            0xC1,
            0x7B,
            0x0B
        )

        # AVEncSliceControlSize (UINT32)
        CODECAPI_AVEncSliceControlSize = DEFINE_CODECAPI_GUID(
            "92F51DF3-07A5-4172-AEFE-C69CA3B60E35",
            0x92F51DF3,
            0x07A5,
            0x4172,
            0xAE,
            0xFE,
            0xC6,
            0x9C,
            0xA3,
            0xB6,
            0x0E,
            0x35
        )

        # CODECAPI_AVEncSliceGenerationMode (UINT32)
        CODECAPI_AVEncSliceGenerationMode = DEFINE_CODECAPI_GUID(
            "8A6BC67F-9497-4286-B46B-02DB8D60EDBC",
            0x8A6BC67F,
            0x9497,
            0x4286,
            0xB4,
            0x6B,
            0x02,
            0xDB,
            0x8D,
            0x60,
            0xED,
            0xBC
        )

        # AVEncVideoMaxNumRefFrame (UINT32)
        CODECAPI_AVEncVideoMaxNumRefFrame = DEFINE_CODECAPI_GUID(
            "964829ED-94F9-43B4-B74D-EF40944B69A0",
            0x964829ED,
            0x94F9,
            0x43B4,
            0xB7,
            0x4D,
            0xEF,
            0x40,
            0x94,
            0x4B,
            0x69,
            0xA0
        )

        # AVEncVideoMeanAbsoluteDifference (UINT32)
        CODECAPI_AVEncVideoMeanAbsoluteDifference = DEFINE_CODECAPI_GUID(
            "E5C0C10F-81A4-422D-8C3F-B474A4581336",
            0xE5C0C10F,
            0x81A4,
            0x422D,
            0x8C,
            0x3F,
            0xB4,
            0x74,
            0xA4,
            0x58,
            0x13,
            0x36
        )

        # AVEncVideoMaxQP (UINT32)
        CODECAPI_AVEncVideoMaxQP = DEFINE_CODECAPI_GUID(
            "3DAF6F66-A6A7-45E0-A8E5-F2743F46A3A2",
            0x3DAF6F66,
            0xA6A7,
            0x45E0,
            0xA8,
            0xE5,
            0xF2,
            0x74,
            0x3F,
            0x46,
            0xA3,
            0xA2
        )

        # AVEncVideoLTRBufferControl (UINT32)
        CODECAPI_AVEncVideoLTRBufferControl = DEFINE_CODECAPI_GUID(
            "A4A0E93D-4CBC-444C-89F4-826D310E92A7",
            0xA4A0E93D,
            0x4CBC,
            0x444C,
            0x89,
            0xF4,
            0x82,
            0x6D,
            0x31,
            0x0E,
            0x92,
            0xA7
        )

        # AVEncVideoMarkLTRFrame (UINT32)
        CODECAPI_AVEncVideoMarkLTRFrame = DEFINE_CODECAPI_GUID(
            "E42F4748-A06D-4EF9-8CEA-3D05FDE3BD3B",
            0xE42F4748,
            0xA06D,
            0x4EF9,
            0x8C,
            0xEA,
            0x3D,
            0x05,
            0xFD,
            0xE3,
            0xBD,
            0x3B
        )

        # AVEncVideoUseLTRFrame (UINT32)
        CODECAPI_AVEncVideoUseLTRFrame = DEFINE_CODECAPI_GUID(
            "00752DB8-55F7-4F80-895B-27639195F2AD",
            0x00752DB8,
            0x55F7,
            0x4F80,
            0x89,
            0x5B,
            0x27,
            0x63,
            0x91,
            0x95,
            0xF2,
            0xAD
        )

        # AVEncVideoROIEnabled (UINT32)
        CODECAPI_AVEncVideoROIEnabled = DEFINE_CODECAPI_GUID(
            "D74F7F18-44DD-4B85-ABA3-05D9F42A8280",
            0xD74F7F18,
            0x44DD,
            0x4B85,
            0xAB,
            0xA3,
            0x5,
            0xD9,
            0xF4,
            0x2A,
            0x82,
            0x80
        )

        # AVEncVideoDirtyRectEnabled (UINT32)
        CODECAPI_AVEncVideoDirtyRectEnabled = DEFINE_CODECAPI_GUID(
            "8ACB8FDD-5E0C-4C66-8729-B8F629AB04FB",
            0x8ACB8FDD,
            0x5E0C,
            0x4C66,
            0x87,
            0x29,
            0xB8,
            0xF6,
            0x29,
            0xAB,
            0x04,
            0xFB
        )

        # AVEncMaxFrameRate (UINT64)
        CODECAPI_AVEncMaxFrameRate = DEFINE_CODECAPI_GUID(
            "B98E1B31-19FA-4D4F-9931-D6A5B8AAB93C",
            0xB98E1B31,
            0x19FA,
            0x4D4F,
            0x99,
            0x31,
            0xD6,
            0xA5,
            0xB8,
            0xAA,
            0xB9,
            0x3C
        )

        # Audio/Video Mux
        # AVEncMuxOutputStreamType (UINT32)
        CODECAPI_AVEncMuxOutputStreamType = DEFINE_CODECAPI_GUID(
            "CEDD9E8F-34D3-44DB-A1D8-F81520254F3E",
            0xCEDD9E8F,
            0x34D3,
            0x44DB,
            0xA1,
            0xD8,
            0xF8,
            0x15,
            0x20,
            0x25,
            0x4F,
            0x3E
        )


        class eAVEncMuxOutput(ENUM):

            # Decision is made automatically be the mux
            # (elementary stream, program stream or transport stream)
            eAVEncMuxOutputAuto = 0
            eAVEncMuxOutputPS = 1
            eAVEncMuxOutputTS = 2


        eAVEncMuxOutputAuto = eAVEncMuxOutput.eAVEncMuxOutputAuto
        eAVEncMuxOutputPS = eAVEncMuxOutput.eAVEncMuxOutputPS
        eAVEncMuxOutputTS = eAVEncMuxOutput.eAVEncMuxOutputTS

        # Common Post - Encode Video Statistical Parameters
        # AVEncStatVideoOutputFrameRate (UINT32/UINT32)
        CODECAPI_AVEncStatVideoOutputFrameRate = DEFINE_CODECAPI_GUID(
            "BE747849-9AB4-4A63-98FE-F143F04F8EE9",
            0xBE747849,
            0x9AB4,
            0x4A63,
            0x98,
            0xFE,
            0xF1,
            0x43,
            0xF0,
            0x4F,
            0x8E,
            0xE9
        )

        # AVEncStatVideoCodedFrames (UINT32)
        CODECAPI_AVEncStatVideoCodedFrames = DEFINE_CODECAPI_GUID(
            "D47F8D61-6F5A-4A26-BB9F-CD9518462BCD",
            0xD47F8D61,
            0x6F5A,
            0x4A26,
            0xBB,
            0x9F,
            0xCD,
            0x95,
            0x18,
            0x46,
            0x2B,
            0xCD
        )

        # AVEncStatVideoTotalFrames (UINT32)
        CODECAPI_AVEncStatVideoTotalFrames = DEFINE_CODECAPI_GUID(
            "FDAA9916-119A-4222-9AD6-3F7CAB99CC8B",
            0xFDAA9916,
            0x119A,
            0x4222,
            0x9A,
            0xD6,
            0x3F,
            0x7C,
            0xAB,
            0x99,
            0xCC,
            0x8B
        )

        # Common Audio Parameters
        # AVEncAudioIntervalToEncode (UINT64)
        CODECAPI_AVEncAudioIntervalToEncode = DEFINE_CODECAPI_GUID(
            "866E4B4D-725A-467C-BB01-B496B23B25F9",
            0x866E4B4D,
            0x725A,
            0x467C,
            0xBB,
            0x01,
            0xB4,
            0x96,
            0xB2,
            0x3B,
            0x25,
            0xF9
        )

        # AVEncAudioIntervalToSkip (UINT64)
        CODECAPI_AVEncAudioIntervalToSkip = DEFINE_CODECAPI_GUID(
            "88C15F94-C38C-4796-A9E8-96E967983F26",
            0x88C15F94,
            0xC38C,
            0x4796,
            0xA9,
            0xE8,
            0x96,
            0xE9,
            0x67,
            0x98,
            0x3F,
            0x26
        )

        # AVEncAudioDualMono (UINT32) - Read/Write
        # Some audio encoders can encode 2 channel input as "dual mono". Use
        # this
        # property to set the appropriate field in the bitstream header to
        # indicate that the
        # 2 channel bitstream is or isn't dual mono.
        # For encoding MPEG audio, use the DualChannel option in
        # AVEncMPACodingMode instead
        CODECAPI_AVEncAudioDualMono = DEFINE_CODECAPI_GUID(
            "3648126B-A3E8-4329-9B3A-5CE566A43BD3",
            0x3648126B,
            0xA3E8,
            0x4329,
            0x9B,
            0x3A,
            0x5C,
            0xE5,
            0x66,
            0xA4,
            0x3B,
            0xD3
        )


        class eAVEncAudioDualMono(ENUM):
            eAVEncAudioDualMono_SameAsInput = 0
            eAVEncAudioDualMono_Off = 1
            eAVEncAudioDualMono_On = 2


        eAVEncAudioDualMono_SameAsInput = eAVEncAudioDualMono.eAVEncAudioDualMono_SameAsInput
        eAVEncAudioDualMono_Off = eAVEncAudioDualMono.eAVEncAudioDualMono_Off
        eAVEncAudioDualMono_On = eAVEncAudioDualMono.eAVEncAudioDualMono_On

        # AVEncAudioMeanBitRate (UINT32) - Read/Write - Used to specify audio
        # bitrate (in bits per second) when the encoder is instantiated as an
        # audio + video encoder.
        CODECAPI_AVEncAudioMeanBitRate = DEFINE_CODECAPI_GUID(
            "921295BB-4FCA-4679-AAB8-9E2A1D753384",
            0x921295BB,
            0x4FCA,
            0x4679,
            0xAA,
            0xB8,
            0x9E,
            0x2A,
            0x1D,
            0x75,
            0x33,
            0x84
        )

        # AVEncAudioMapDestChannel0..15 (UINT32)
        CODECAPI_AVEncAudioMapDestChannel0 = DEFINE_CODECAPI_GUID(
            "BC5D0B60-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B60,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel1 = DEFINE_CODECAPI_GUID(
            "BC5D0B61-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B61,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel2 = DEFINE_CODECAPI_GUID(
            "BC5D0B62-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B62,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel3 = DEFINE_CODECAPI_GUID(
            "BC5D0B63-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B63,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel4 = DEFINE_CODECAPI_GUID(
            "BC5D0B64-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B64,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel5 = DEFINE_CODECAPI_GUID(
            "BC5D0B65-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B65,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel6 = DEFINE_CODECAPI_GUID(
            "BC5D0B66-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B66,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel7 = DEFINE_CODECAPI_GUID(
            "BC5D0B67-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B67,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel8 = DEFINE_CODECAPI_GUID(
            "BC5D0B68-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B68,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel9 = DEFINE_CODECAPI_GUID(
            "BC5D0B69-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B69,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel10 = DEFINE_CODECAPI_GUID(
            "BC5D0B6A-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B6A,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel11 = DEFINE_CODECAPI_GUID(
            "BC5D0B6B-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B6B,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel12 = DEFINE_CODECAPI_GUID(
            "BC5D0B6C-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B6C,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel13 = DEFINE_CODECAPI_GUID(
            "BC5D0B6D-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B6D,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel14 = DEFINE_CODECAPI_GUID(
            "BC5D0B6E-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B6E,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )
        CODECAPI_AVEncAudioMapDestChannel15 = DEFINE_CODECAPI_GUID(
            "BC5D0B6F-DF6A-4E16-9803-B82007A30C8D",
            0xBC5D0B6F,
            0xDF6A,
            0x4E16,
            0x98,
            0x03,
            0xB8,
            0x20,
            0x07,
            0xA3,
            0x0C,
            0x8D
        )

        # AVEncAudioInputContent (UINT32) < - - - - You have ENUM in the doc
        CODECAPI_AVEncAudioInputContent = DEFINE_CODECAPI_GUID(
            "3E226C2B-60B9-4A39-B00B-A7B40F70D566",
            0x3E226C2B,
            0x60B9,
            0x4A39,
            0xB0,
            0x0B,
            0xA7,
            0xB4,
            0x0F,
            0x70,
            0xD5,
            0x66
        )


        class eAVEncAudioInputContent(ENUM):
            AVEncAudioInputContent_Unknown = 0
            AVEncAudioInputContent_Voice = 1
            AVEncAudioInputContent_Music = 2


        AVEncAudioInputContent_Unknown = eAVEncAudioInputContent.AVEncAudioInputContent_Unknown
        AVEncAudioInputContent_Voice = eAVEncAudioInputContent.AVEncAudioInputContent_Voice
        AVEncAudioInputContent_Music = eAVEncAudioInputContent.AVEncAudioInputContent_Music

        # Common Post - Encode Audio Statistical Parameters
        # AVEncStatAudioPeakPCMValue (UINT32)
        CODECAPI_AVEncStatAudioPeakPCMValue = DEFINE_CODECAPI_GUID(
            "DCE7FD34-DC00-4C16-821B-35D9EB00FB1A",
            0xDCE7FD34,
            0xDC00,
            0x4C16,
            0x82,
            0x1B,
            0x35,
            0xD9,
            0xEB,
            0x00,
            0xFB,
            0x1A
        )

        # AVEncStatAudioAveragePCMValue (UINT32)
        CODECAPI_AVEncStatAudioAveragePCMValue = DEFINE_CODECAPI_GUID(
            "979272F8-D17F-4E32-BB73-4E731C68BA2D",
            0x979272F8,
            0xD17F,
            0x4E32,
            0xBB,
            0x73,
            0x4E,
            0x73,
            0x1C,
            0x68,
            0xBA,
            0x2D
        )

        # AVEncStatAverageBPS (UINT32)
        CODECAPI_AVEncStatAudioAverageBPS = DEFINE_CODECAPI_GUID(
            "CA6724DB-7059-4351-8B43-F82198826A14",
            0xCA6724DB,
            0x7059,
            0x4351,
            0x8B,
            0x43,
            0xF8,
            0x21,
            0x98,
            0x82,
            0x6A,
            0x14
        )
        CODECAPI_AVEncStatAverageBPS = DEFINE_CODECAPI_GUID(
            "CA6724DB-7059-4351-8B43-F82198826A14",
            0xCA6724DB,
            0x7059,
            0x4351,
            0x8B,
            0x43,
            0xF8,
            0x21,
            0x98,
            0x82,
            0x6A,
            0x14
        )

        # AVEncStatHardwareProcessorUtilitization (UINT32)
        # HW usage % x 1000
        CODECAPI_AVEncStatHardwareProcessorUtilitization = DEFINE_CODECAPI_GUID(
            "995DC027-CB95-49E6-B91B-5967753CDCB8",
            0x995DC027,
            0xCB95,
            0x49E6,
            0xB9,
            0x1B,
            0x59,
            0x67,
            0x75,
            0x3C,
            0xDC,
            0xB8
        )

        # AVEncStatHardwareBandwidthUtilitization (UINT32)
        # HW usage % x 1000
        CODECAPI_AVEncStatHardwareBandwidthUtilitization = DEFINE_CODECAPI_GUID(
            "0124BA9B-DC41-4826-B45F-18AC01B3D5A8",
            0x0124BA9B,
            0xDC41,
            0x4826,
            0xB4,
            0x5F,
            0x18,
            0xAC,
            0x01,
            0xB3,
            0xD5,
            0xA8
        )

        # MPEG Video Encoding Interface
        # MPV Encoder Specific Parameters
        # AVEncMPVGOPSize (UINT32)
        CODECAPI_AVEncMPVGOPSize = DEFINE_CODECAPI_GUID(
            "95F31B26-95A4-41AA-9303-246A7FC6EEF1",
            0x95F31B26,
            0x95A4,
            0x41AA,
            0x93,
            0x03,
            0x24,
            0x6A,
            0x7F,
            0xC6,
            0xEE,
            0xF1
        )

        # AVEncMPVGOPOpen (BOOL)
        CODECAPI_AVEncMPVGOPOpen = DEFINE_CODECAPI_GUID(
            "B1D5D4A6-3300-49B1-AE61-A09937AB0E49",
            0xB1D5D4A6,
            0x3300,
            0x49B1,
            0xAE,
            0x61,
            0xA0,
            0x99,
            0x37,
            0xAB,
            0x0E,
            0x49
        )

        # AVEncMPVDefaultBPictureCount (UINT32)
        CODECAPI_AVEncMPVDefaultBPictureCount = DEFINE_CODECAPI_GUID(
            "8D390AAC-DC5C-4200-B57F-814D04BABAB2",
            0x8D390AAC,
            0xDC5C,
            0x4200,
            0xB5,
            0x7F,
            0x81,
            0x4D,
            0x04,
            0xBA,
            0xBA,
            0xB2
        )

        # AVEncMPVProfile (UINT32) < - - - - You have GUID in the doc
        CODECAPI_AVEncMPVProfile = DEFINE_CODECAPI_GUID(
            "DABB534A-1D99-4284-975A-D90E2239BAA1",
            0xDABB534A,
            0x1D99,
            0x4284,
            0x97,
            0x5A,
            0xD9,
            0x0E,
            0x22,
            0x39,
            0xBA,
            0xA1
        )


        class eAVEncMPVProfile(ENUM):
            eAVEncMPVProfile_unknown = 0
            eAVEncMPVProfile_Simple = 1
            eAVEncMPVProfile_Main = 2
            eAVEncMPVProfile_High = 3
            eAVEncMPVProfile_422 = 4


        eAVEncMPVProfile_unknown = eAVEncMPVProfile.eAVEncMPVProfile_unknown
        eAVEncMPVProfile_Simple = eAVEncMPVProfile.eAVEncMPVProfile_Simple
        eAVEncMPVProfile_Main = eAVEncMPVProfile.eAVEncMPVProfile_Main
        eAVEncMPVProfile_High = eAVEncMPVProfile.eAVEncMPVProfile_High
        eAVEncMPVProfile_422 = eAVEncMPVProfile.eAVEncMPVProfile_422

        # AVEncMPVLevel (UINT32) < - - - - You have GUID in the doc
        CODECAPI_AVEncMPVLevel = DEFINE_CODECAPI_GUID(
            "6EE40C40-A60C-41EF-8F50-37C2249E2CB3",
            0x6EE40C40,
            0xA60C,
            0x41EF,
            0x8F,
            0x50,
            0x37,
            0xC2,
            0x24,
            0x9E,
            0x2C,
            0xB3
        )


        class eAVEncMPVLevel(ENUM):
            eAVEncMPVLevel_Low = 1
            eAVEncMPVLevel_Main = 2
            eAVEncMPVLevel_High1440 = 3
            eAVEncMPVLevel_High = 4


        eAVEncMPVLevel_Low = eAVEncMPVLevel.eAVEncMPVLevel_Low
        eAVEncMPVLevel_Main = eAVEncMPVLevel.eAVEncMPVLevel_Main
        eAVEncMPVLevel_High1440 = eAVEncMPVLevel.eAVEncMPVLevel_High1440
        eAVEncMPVLevel_High = eAVEncMPVLevel.eAVEncMPVLevel_High


        class eAVEncH263VProfile(ENUM):
            eAVEncH263VProfile_Base = 0
            eAVEncH263VProfile_CompatibilityV2 = 1
            eAVEncH263VProfile_CompatibilityV1 = 2
            eAVEncH263VProfile_WirelessV2 = 3
            eAVEncH263VProfile_WirelessV3 = 4
            eAVEncH263VProfile_HighCompression = 5
            eAVEncH263VProfile_Internet = 6
            eAVEncH263VProfile_Interlace = 7
            eAVEncH263VProfile_HighLatency = 8


        eAVEncH263VProfile_Base = eAVEncH263VProfile.eAVEncH263VProfile_Base
        eAVEncH263VProfile_CompatibilityV2 = eAVEncH263VProfile.eAVEncH263VProfile_CompatibilityV2
        eAVEncH263VProfile_CompatibilityV1 = eAVEncH263VProfile.eAVEncH263VProfile_CompatibilityV1
        eAVEncH263VProfile_WirelessV2 = eAVEncH263VProfile.eAVEncH263VProfile_WirelessV2
        eAVEncH263VProfile_WirelessV3 = eAVEncH263VProfile.eAVEncH263VProfile_WirelessV3
        eAVEncH263VProfile_HighCompression = eAVEncH263VProfile.eAVEncH263VProfile_HighCompression
        eAVEncH263VProfile_Internet = eAVEncH263VProfile.eAVEncH263VProfile_Internet
        eAVEncH263VProfile_Interlace = eAVEncH263VProfile.eAVEncH263VProfile_Interlace
        eAVEncH263VProfile_HighLatency = eAVEncH263VProfile.eAVEncH263VProfile_HighLatency


        class eAVEncH264VProfile(ENUM):
            eAVEncH264VProfile_unknown = 0
            eAVEncH264VProfile_Simple = 66
            eAVEncH264VProfile_Base = 66
            eAVEncH264VProfile_Main = 77
            eAVEncH264VProfile_High = 100
            eAVEncH264VProfile_422 = 122
            eAVEncH264VProfile_High10 = 110
            eAVEncH264VProfile_444 = 244
            eAVEncH264VProfile_Extended = 88
            eAVEncH264VProfile_ScalableBase = 83
            eAVEncH264VProfile_ScalableHigh = 86
            eAVEncH264VProfile_MultiviewHigh = 118
            eAVEncH264VProfile_StereoHigh = 128
            eAVEncH264VProfile_ConstrainedBase = 256
            eAVEncH264VProfile_UCConstrainedHigh = 257
            eAVEncH264VProfile_UCScalableConstrainedBase = 258
            eAVEncH264VProfile_UCScalableConstrainedHigh = 259


        eAVEncH264VProfile_unknown = eAVEncH264VProfile.eAVEncH264VProfile_unknown
        eAVEncH264VProfile_Simple = eAVEncH264VProfile.eAVEncH264VProfile_Simple
        eAVEncH264VProfile_Base = eAVEncH264VProfile.eAVEncH264VProfile_Base
        eAVEncH264VProfile_Main = eAVEncH264VProfile.eAVEncH264VProfile_Main
        eAVEncH264VProfile_High = eAVEncH264VProfile.eAVEncH264VProfile_High
        eAVEncH264VProfile_422 = eAVEncH264VProfile.eAVEncH264VProfile_422
        eAVEncH264VProfile_High10 = eAVEncH264VProfile.eAVEncH264VProfile_High10
        eAVEncH264VProfile_444 = eAVEncH264VProfile.eAVEncH264VProfile_444
        eAVEncH264VProfile_Extended = eAVEncH264VProfile.eAVEncH264VProfile_Extended
        eAVEncH264VProfile_ScalableBase = eAVEncH264VProfile.eAVEncH264VProfile_ScalableBase
        eAVEncH264VProfile_ScalableHigh = eAVEncH264VProfile.eAVEncH264VProfile_ScalableHigh
        eAVEncH264VProfile_MultiviewHigh = eAVEncH264VProfile.eAVEncH264VProfile_MultiviewHigh
        eAVEncH264VProfile_StereoHigh = eAVEncH264VProfile.eAVEncH264VProfile_StereoHigh
        eAVEncH264VProfile_ConstrainedBase = eAVEncH264VProfile.eAVEncH264VProfile_ConstrainedBase
        eAVEncH264VProfile_UCConstrainedHigh = eAVEncH264VProfile.eAVEncH264VProfile_UCConstrainedHigh
        eAVEncH264VProfile_UCScalableConstrainedBase = eAVEncH264VProfile.eAVEncH264VProfile_UCScalableConstrainedBase
        eAVEncH264VProfile_UCScalableConstrainedHigh = eAVEncH264VProfile.eAVEncH264VProfile_UCScalableConstrainedHigh
        eAVEncH264VProfile_ConstrainedHigh = (
            eAVEncH264VProfile_UCConstrainedHigh
        )


        class eAVEncH265VProfile(ENUM):
            eAVEncH265VProfile_unknown = 0
            eAVEncH265VProfile_Main_420_8 = 1
            eAVEncH265VProfile_Main_420_10 = 2
            eAVEncH265VProfile_Main_420_12 = 3
            eAVEncH265VProfile_Main_422_10 = 4
            eAVEncH265VProfile_Main_422_12 = 5
            eAVEncH265VProfile_Main_444_8 = 6
            eAVEncH265VProfile_Main_444_10 = 7
            eAVEncH265VProfile_Main_444_12 = 8
            eAVEncH265VProfile_Monochrome_12 = 9
            eAVEncH265VProfile_Monochrome_16 = 10
            eAVEncH265VProfile_MainIntra_420_8 = 11
            eAVEncH265VProfile_MainIntra_420_10 = 12
            eAVEncH265VProfile_MainIntra_420_12 = 13
            eAVEncH265VProfile_MainIntra_422_10 = 14
            eAVEncH265VProfile_MainIntra_422_12 = 15
            eAVEncH265VProfile_MainIntra_444_8 = 16
            eAVEncH265VProfile_MainIntra_444_10 = 17
            eAVEncH265VProfile_MainIntra_444_12 = 18
            eAVEncH265VProfile_MainIntra_444_16 = 19
            eAVEncH265VProfile_MainStill_420_8 = 20
            eAVEncH265VProfile_MainStill_444_8 = 21
            eAVEncH265VProfile_MainStill_444_16 = 22


        eAVEncH265VProfile_unknown = eAVEncH265VProfile.eAVEncH265VProfile_unknown
        eAVEncH265VProfile_Main_420_8 = eAVEncH265VProfile.eAVEncH265VProfile_Main_420_8
        eAVEncH265VProfile_Main_420_10 = eAVEncH265VProfile.eAVEncH265VProfile_Main_420_10
        eAVEncH265VProfile_Main_420_12 = eAVEncH265VProfile.eAVEncH265VProfile_Main_420_12
        eAVEncH265VProfile_Main_422_10 = eAVEncH265VProfile.eAVEncH265VProfile_Main_422_10
        eAVEncH265VProfile_Main_422_12 = eAVEncH265VProfile.eAVEncH265VProfile_Main_422_12
        eAVEncH265VProfile_Main_444_8 = eAVEncH265VProfile.eAVEncH265VProfile_Main_444_8
        eAVEncH265VProfile_Main_444_10 = eAVEncH265VProfile.eAVEncH265VProfile_Main_444_10
        eAVEncH265VProfile_Main_444_12 = eAVEncH265VProfile.eAVEncH265VProfile_Main_444_12
        eAVEncH265VProfile_Monochrome_12 = eAVEncH265VProfile.eAVEncH265VProfile_Monochrome_12
        eAVEncH265VProfile_Monochrome_16 = eAVEncH265VProfile.eAVEncH265VProfile_Monochrome_16
        eAVEncH265VProfile_MainIntra_420_8 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_420_8
        eAVEncH265VProfile_MainIntra_420_10 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_420_10
        eAVEncH265VProfile_MainIntra_420_12 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_420_12
        eAVEncH265VProfile_MainIntra_422_10 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_422_10
        eAVEncH265VProfile_MainIntra_422_12 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_422_12
        eAVEncH265VProfile_MainIntra_444_8 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_444_8
        eAVEncH265VProfile_MainIntra_444_10 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_444_10
        eAVEncH265VProfile_MainIntra_444_12 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_444_12
        eAVEncH265VProfile_MainIntra_444_16 = eAVEncH265VProfile.eAVEncH265VProfile_MainIntra_444_16
        eAVEncH265VProfile_MainStill_420_8 = eAVEncH265VProfile.eAVEncH265VProfile_MainStill_420_8
        eAVEncH265VProfile_MainStill_444_8 = eAVEncH265VProfile.eAVEncH265VProfile_MainStill_444_8
        eAVEncH265VProfile_MainStill_444_16 = eAVEncH265VProfile.eAVEncH265VProfile_MainStill_444_16


        class eAVEncVP9VProfile(ENUM):
            eAVEncVP9VProfile_unknown = 0
            eAVEncVP9VProfile_420_8 = 1
            eAVEncVP9VProfile_420_10 = 2
            eAVEncVP9VProfile_420_12 = 3


        eAVEncVP9VProfile_unknown = eAVEncVP9VProfile.eAVEncVP9VProfile_unknown
        eAVEncVP9VProfile_420_8 = eAVEncVP9VProfile.eAVEncVP9VProfile_420_8
        eAVEncVP9VProfile_420_10 = eAVEncVP9VProfile.eAVEncVP9VProfile_420_10
        eAVEncVP9VProfile_420_12 = eAVEncVP9VProfile.eAVEncVP9VProfile_420_12


        class eAVEncH263PictureType(ENUM):
            eAVEncH263PictureType_I = 0
            eAVEncH263PictureType_P = 1
            eAVEncH263PictureType_B = 2


        eAVEncH263PictureType_I = eAVEncH263PictureType.eAVEncH263PictureType_I
        eAVEncH263PictureType_P = eAVEncH263PictureType.eAVEncH263PictureType_P
        eAVEncH263PictureType_B = eAVEncH263PictureType.eAVEncH263PictureType_B


        class eAVEncH264PictureType(ENUM):
            eAVEncH264PictureType_IDR = 0
            eAVEncH264PictureType_P = 1
            eAVEncH264PictureType_B = 2


        eAVEncH264PictureType_IDR = eAVEncH264PictureType.eAVEncH264PictureType_IDR
        eAVEncH264PictureType_P = eAVEncH264PictureType.eAVEncH264PictureType_P
        eAVEncH264PictureType_B = eAVEncH264PictureType.eAVEncH264PictureType_B
        AVENC_H263V_LEVELCOUNT = 8


        class eAVEncH263VLevel(ENUM):
            eAVEncH263VLevel1 = 10
            eAVEncH263VLevel2 = 20
            eAVEncH263VLevel3 = 30
            eAVEncH263VLevel4 = 40
            eAVEncH263VLevel4_5 = 45
            eAVEncH263VLevel5 = 50
            eAVEncH263VLevel6 = 60
            eAVEncH263VLevel7 = 70


        eAVEncH263VLevel1 = eAVEncH263VLevel.eAVEncH263VLevel1
        eAVEncH263VLevel2 = eAVEncH263VLevel.eAVEncH263VLevel2
        eAVEncH263VLevel3 = eAVEncH263VLevel.eAVEncH263VLevel3
        eAVEncH263VLevel4 = eAVEncH263VLevel.eAVEncH263VLevel4
        eAVEncH263VLevel4_5 = eAVEncH263VLevel.eAVEncH263VLevel4_5
        eAVEncH263VLevel5 = eAVEncH263VLevel.eAVEncH263VLevel5
        eAVEncH263VLevel6 = eAVEncH263VLevel.eAVEncH263VLevel6
        eAVEncH263VLevel7 = eAVEncH263VLevel.eAVEncH263VLevel7
        AVENC_H264V_LEVELCOUNT = 16
        AVENC_H264V_MAX_MBBITS = 3200


        class eAVEncH264VLevel(ENUM):
            eAVEncH264VLevel1 = 10
            eAVEncH264VLevel1_b = 11
            eAVEncH264VLevel1_1 = 11
            eAVEncH264VLevel1_2 = 12
            eAVEncH264VLevel1_3 = 13
            eAVEncH264VLevel2 = 20
            eAVEncH264VLevel2_1 = 21
            eAVEncH264VLevel2_2 = 22
            eAVEncH264VLevel3 = 30
            eAVEncH264VLevel3_1 = 31
            eAVEncH264VLevel3_2 = 32
            eAVEncH264VLevel4 = 40
            eAVEncH264VLevel4_1 = 41
            eAVEncH264VLevel4_2 = 42
            eAVEncH264VLevel5 = 50
            eAVEncH264VLevel5_1 = 51
            eAVEncH264VLevel5_2 = 52


        eAVEncH264VLevel1 = eAVEncH264VLevel.eAVEncH264VLevel1
        eAVEncH264VLevel1_b = eAVEncH264VLevel.eAVEncH264VLevel1_b
        eAVEncH264VLevel1_1 = eAVEncH264VLevel.eAVEncH264VLevel1_1
        eAVEncH264VLevel1_2 = eAVEncH264VLevel.eAVEncH264VLevel1_2
        eAVEncH264VLevel1_3 = eAVEncH264VLevel.eAVEncH264VLevel1_3
        eAVEncH264VLevel2 = eAVEncH264VLevel.eAVEncH264VLevel2
        eAVEncH264VLevel2_1 = eAVEncH264VLevel.eAVEncH264VLevel2_1
        eAVEncH264VLevel2_2 = eAVEncH264VLevel.eAVEncH264VLevel2_2
        eAVEncH264VLevel3 = eAVEncH264VLevel.eAVEncH264VLevel3
        eAVEncH264VLevel3_1 = eAVEncH264VLevel.eAVEncH264VLevel3_1
        eAVEncH264VLevel3_2 = eAVEncH264VLevel.eAVEncH264VLevel3_2
        eAVEncH264VLevel4 = eAVEncH264VLevel.eAVEncH264VLevel4
        eAVEncH264VLevel4_1 = eAVEncH264VLevel.eAVEncH264VLevel4_1
        eAVEncH264VLevel4_2 = eAVEncH264VLevel.eAVEncH264VLevel4_2
        eAVEncH264VLevel5 = eAVEncH264VLevel.eAVEncH264VLevel5
        eAVEncH264VLevel5_1 = eAVEncH264VLevel.eAVEncH264VLevel5_1
        eAVEncH264VLevel5_2 = eAVEncH264VLevel.eAVEncH264VLevel5_2


        class eAVEncH265VLevel(ENUM):
            eAVEncH265VLevel1 = 30
            eAVEncH265VLevel2 = 60
            eAVEncH265VLevel2_1 = 63
            eAVEncH265VLevel3 = 90
            eAVEncH265VLevel3_1 = 93
            eAVEncH265VLevel4 = 120
            eAVEncH265VLevel4_1 = 123
            eAVEncH265VLevel5 = 150
            eAVEncH265VLevel5_1 = 153
            eAVEncH265VLevel5_2 = 156
            eAVEncH265VLevel6 = 180
            eAVEncH265VLevel6_1 = 183
            eAVEncH265VLevel6_2 = 186


        eAVEncH265VLevel1 = eAVEncH265VLevel.eAVEncH265VLevel1
        eAVEncH265VLevel2 = eAVEncH265VLevel.eAVEncH265VLevel2
        eAVEncH265VLevel2_1 = eAVEncH265VLevel.eAVEncH265VLevel2_1
        eAVEncH265VLevel3 = eAVEncH265VLevel.eAVEncH265VLevel3
        eAVEncH265VLevel3_1 = eAVEncH265VLevel.eAVEncH265VLevel3_1
        eAVEncH265VLevel4 = eAVEncH265VLevel.eAVEncH265VLevel4
        eAVEncH265VLevel4_1 = eAVEncH265VLevel.eAVEncH265VLevel4_1
        eAVEncH265VLevel5 = eAVEncH265VLevel.eAVEncH265VLevel5
        eAVEncH265VLevel5_1 = eAVEncH265VLevel.eAVEncH265VLevel5_1
        eAVEncH265VLevel5_2 = eAVEncH265VLevel.eAVEncH265VLevel5_2
        eAVEncH265VLevel6 = eAVEncH265VLevel.eAVEncH265VLevel6
        eAVEncH265VLevel6_1 = eAVEncH265VLevel.eAVEncH265VLevel6_1
        eAVEncH265VLevel6_2 = eAVEncH265VLevel.eAVEncH265VLevel6_2

        # AVEncMPVFrameFieldMode (UINT32)
        CODECAPI_AVEncMPVFrameFieldMode = DEFINE_CODECAPI_GUID(
            "ACB5DE96-7B93-4C2F-8825-B0295FA93BF4",
            0xACB5DE96,
            0x7B93,
            0x4C2F,
            0x88,
            0x25,
            0xB0,
            0x29,
            0x5F,
            0xA9,
            0x3B,
            0xF4
        )


        class eAVEncMPVFrameFieldMode(ENUM):
            eAVEncMPVFrameFieldMode_FieldMode = 0
            eAVEncMPVFrameFieldMode_FrameMode = 1


        eAVEncMPVFrameFieldMode_FieldMode = eAVEncMPVFrameFieldMode.eAVEncMPVFrameFieldMode_FieldMode
        eAVEncMPVFrameFieldMode_FrameMode = eAVEncMPVFrameFieldMode.eAVEncMPVFrameFieldMode_FrameMode

        # Advanced MPV Encoder Specific Parameters
        # AVEncMPVAddSeqEndCode (BOOL)
        CODECAPI_AVEncMPVAddSeqEndCode = DEFINE_CODECAPI_GUID(
            "A823178F-57DF-4C7A-B8FD-E5EC8887708D",
            0xA823178F,
            0x57DF,
            0x4C7A,
            0xB8,
            0xFD,
            0xE5,
            0xEC,
            0x88,
            0x87,
            0x70,
            0x8D
        )

        # AVEncMPVGOPSInSeq (UINT32)
        CODECAPI_AVEncMPVGOPSInSeq = DEFINE_CODECAPI_GUID(
            "993410D4-2691-4192-9978-98DC2603669F",
            0x993410D4,
            0x2691,
            0x4192,
            0x99,
            0x78,
            0x98,
            0xDC,
            0x26,
            0x03,
            0x66,
            0x9F
        )

        # AVEncMPVUseConcealmentMotionVectors (BOOL)
        CODECAPI_AVEncMPVUseConcealmentMotionVectors = DEFINE_CODECAPI_GUID(
            "EC770CF3-6908-4B4B-AA30-7FB986214FEA",
            0xEC770CF3,
            0x6908,
            0x4B4B,
            0xAA,
            0x30,
            0x7F,
            0xB9,
            0x86,
            0x21,
            0x4F,
            0xEA
        )

        # AVEncMPVSceneDetection (UINT32)
        CODECAPI_AVEncMPVSceneDetection = DEFINE_CODECAPI_GUID(
            "552799F1-DB4C-405B-8A3A-C93F2D0674DC",
            0x552799F1,
            0xDB4C,
            0x405B,
            0x8A,
            0x3A,
            0xC9,
            0x3F,
            0x2D,
            0x06,
            0x74,
            0xDC
        )


        class eAVEncMPVSceneDetection(ENUM):
            eAVEncMPVSceneDetection_None = 0
            eAVEncMPVSceneDetection_InsertIPicture = 1
            eAVEncMPVSceneDetection_StartNewGOP = 2
            eAVEncMPVSceneDetection_StartNewLocatableGOP = 3


        eAVEncMPVSceneDetection_None = eAVEncMPVSceneDetection.eAVEncMPVSceneDetection_None
        eAVEncMPVSceneDetection_InsertIPicture = eAVEncMPVSceneDetection.eAVEncMPVSceneDetection_InsertIPicture
        eAVEncMPVSceneDetection_StartNewGOP = eAVEncMPVSceneDetection.eAVEncMPVSceneDetection_StartNewGOP
        eAVEncMPVSceneDetection_StartNewLocatableGOP = eAVEncMPVSceneDetection.eAVEncMPVSceneDetection_StartNewLocatableGOP

        # AVEncMPVGenerateHeaderSeqExt (BOOL)
        CODECAPI_AVEncMPVGenerateHeaderSeqExt = DEFINE_CODECAPI_GUID(
            "D5E78611-082D-4E6B-98AF-0F51AB139222",
            0xD5E78611,
            0x082D,
            0x4E6B,
            0x98,
            0xAF,
            0x0F,
            0x51,
            0xAB,
            0x13,
            0x92,
            0x22
        )

        # AVEncMPVGenerateHeaderSeqDispExt (BOOL)
        CODECAPI_AVEncMPVGenerateHeaderSeqDispExt = DEFINE_CODECAPI_GUID(
            "6437AA6F-5A3C-4DE9-8A16-53D9C4AD326F",
            0x6437AA6F,
            0x5A3C,
            0x4DE9,
            0x8A,
            0x16,
            0x53,
            0xD9,
            0xC4,
            0xAD,
            0x32,
            0x6F
        )

        # AVEncMPVGenerateHeaderPicExt (BOOL)
        CODECAPI_AVEncMPVGenerateHeaderPicExt = DEFINE_CODECAPI_GUID(
            "1B8464AB-944F-45F0-B74E-3A58DAD11F37",
            0x1B8464AB,
            0x944F,
            0x45F0,
            0xB7,
            0x4E,
            0x3A,
            0x58,
            0xDA,
            0xD1,
            0x1F,
            0x37
        )

        # AVEncMPVGenerateHeaderPicDispExt (BOOL)
        CODECAPI_AVEncMPVGenerateHeaderPicDispExt = DEFINE_CODECAPI_GUID(
            "C6412F84-C03F-4F40-A00C-4293DF8395BB",
            0xC6412F84,
            0xC03F,
            0x4F40,
            0xA0,
            0x0C,
            0x42,
            0x93,
            0xDF,
            0x83,
            0x95,
            0xBB
        )

        # AVEncMPVGenerateHeaderSeqScaleExt (BOOL)
        CODECAPI_AVEncMPVGenerateHeaderSeqScaleExt = DEFINE_CODECAPI_GUID(
            "0722D62F-DD59-4A86-9CD5-644F8E2653D8",
            0x0722D62F,
            0xDD59,
            0x4A86,
            0x9C,
            0xD5,
            0x64,
            0x4F,
            0x8E,
            0x26,
            0x53,
            0xD8
        )

        # AVEncMPVScanPattern (UINT32)
        CODECAPI_AVEncMPVScanPattern = DEFINE_CODECAPI_GUID(
            "7F8A478E-7BBB-4AE2-B2FC-96D17FC4A2D6",
            0x7F8A478E,
            0x7BBB,
            0x4AE2,
            0xB2,
            0xFC,
            0x96,
            0xD1,
            0x7F,
            0xC4,
            0xA2,
            0xD6
        )


        class eAVEncMPVScanPattern(ENUM):
            eAVEncMPVScanPattern_Auto = 0
            eAVEncMPVScanPattern_ZigZagScan = 1
            eAVEncMPVScanPattern_AlternateScan = 2


        eAVEncMPVScanPattern_Auto = eAVEncMPVScanPattern.eAVEncMPVScanPattern_Auto
        eAVEncMPVScanPattern_ZigZagScan = eAVEncMPVScanPattern.eAVEncMPVScanPattern_ZigZagScan
        eAVEncMPVScanPattern_AlternateScan = eAVEncMPVScanPattern.eAVEncMPVScanPattern_AlternateScan

        # AVEncMPVIntraDCPrecision (UINT32)
        CODECAPI_AVEncMPVIntraDCPrecision = DEFINE_CODECAPI_GUID(
            "A0116151-CBC8-4AF3-97DC-D00CCEB82D79",
            0xA0116151,
            0xCBC8,
            0x4AF3,
            0x97,
            0xDC,
            0xD0,
            0x0C,
            0xCE,
            0xB8,
            0x2D,
            0x79
        )

        # AVEncMPVQScaleType (UINT32)
        CODECAPI_AVEncMPVQScaleType = DEFINE_CODECAPI_GUID(
            "2B79EBB7-F484-4AF7-BB58-A2A188C5CBBE",
            0x2B79EBB7,
            0xF484,
            0x4AF7,
            0xBB,
            0x58,
            0xA2,
            0xA1,
            0x88,
            0xC5,
            0xCB,
            0xBE
        )


        class eAVEncMPVQScaleType(ENUM):
            eAVEncMPVQScaleType_Auto = 0
            eAVEncMPVQScaleType_Linear = 1
            eAVEncMPVQScaleType_NonLinear = 2


        eAVEncMPVQScaleType_Auto = eAVEncMPVQScaleType.eAVEncMPVQScaleType_Auto
        eAVEncMPVQScaleType_Linear = eAVEncMPVQScaleType.eAVEncMPVQScaleType_Linear
        eAVEncMPVQScaleType_NonLinear = eAVEncMPVQScaleType.eAVEncMPVQScaleType_NonLinear

        # AVEncMPVIntraVLCTable (UINT32)
        CODECAPI_AVEncMPVIntraVLCTable = DEFINE_CODECAPI_GUID(
            "A2B83FF5-1A99-405A-AF95-C5997D558D3A",
            0xA2B83FF5,
            0x1A99,
            0x405A,
            0xAF,
            0x95,
            0xC5,
            0x99,
            0x7D,
            0x55,
            0x8D,
            0x3A
        )


        class eAVEncMPVIntraVLCTable(ENUM):
            eAVEncMPVIntraVLCTable_Auto = 0
            eAVEncMPVIntraVLCTable_MPEG1 = 1
            eAVEncMPVIntraVLCTable_Alternate = 2


        eAVEncMPVIntraVLCTable_Auto = eAVEncMPVIntraVLCTable.eAVEncMPVIntraVLCTable_Auto
        eAVEncMPVIntraVLCTable_MPEG1 = eAVEncMPVIntraVLCTable.eAVEncMPVIntraVLCTable_MPEG1
        eAVEncMPVIntraVLCTable_Alternate = eAVEncMPVIntraVLCTable.eAVEncMPVIntraVLCTable_Alternate

        # AVEncMPVQuantMatrixIntra
        # (BYTE[64] encoded as a string of 128 hex digits)
        CODECAPI_AVEncMPVQuantMatrixIntra = DEFINE_CODECAPI_GUID(
            "9BEA04F3-6621-442C-8BA1-3AC378979698",
            0x9BEA04F3,
            0x6621,
            0x442C,
            0x8B,
            0xA1,
            0x3A,
            0xC3,
            0x78,
            0x97,
            0x96,
            0x98
        )

        # AVEncMPVQuantMatrixNonIntra
        # (BYTE[64] encoded as a string of 128 hex digits)
        CODECAPI_AVEncMPVQuantMatrixNonIntra = DEFINE_CODECAPI_GUID(
            "87F441D8-0997-4BEB-A08E-8573D409CF75",
            0x87F441D8,
            0x0997,
            0x4BEB,
            0xA0,
            0x8E,
            0x85,
            0x73,
            0xD4,
            0x09,
            0xCF,
            0x75
        )

        # AVEncMPVQuantMatrixChromaIntra
        # (BYTE[64] encoded as a string of 128 hex digits)
        CODECAPI_AVEncMPVQuantMatrixChromaIntra = DEFINE_CODECAPI_GUID(
            "9EB9ECD4-018D-4FFD-8F2D-39E49F07B17A",
            0x9EB9ECD4,
            0x018D,
            0x4FFD,
            0x8F,
            0x2D,
            0x39,
            0xE4,
            0x9F,
            0x07,
            0xB1,
            0x7A
        )

        # AVEncMPVQuantMatrixChromaNonIntra
        # (BYTE[64] encoded as a string of 128 hex digits)
        CODECAPI_AVEncMPVQuantMatrixChromaNonIntra = DEFINE_CODECAPI_GUID(
            "1415B6B1-362A-4338-BA9A-1EF58703C05B",
            0x1415B6B1,
            0x362A,
            0x4338,
            0xBA,
            0x9A,
            0x1E,
            0xF5,
            0x87,
            0x03,
            0xC0,
            0x5B
        )

        # MPEG1 Audio Encoding Interface
        # MPEG1 Audio Specific Parameters
        # AVEncMPALayer (UINT)
        CODECAPI_AVEncMPALayer = DEFINE_CODECAPI_GUID(
            "9D377230-F91B-453D-9CE0-78445414C22D",
            0x9D377230,
            0xF91B,
            0x453D,
            0x9C,
            0xE0,
            0x78,
            0x44,
            0x54,
            0x14,
            0xC2,
            0x2D
        )


        class eAVEncMPALayer(ENUM):
            eAVEncMPALayer_1 = 1
            eAVEncMPALayer_2 = 2
            eAVEncMPALayer_3 = 3


        eAVEncMPALayer_1 = eAVEncMPALayer.eAVEncMPALayer_1
        eAVEncMPALayer_2 = eAVEncMPALayer.eAVEncMPALayer_2
        eAVEncMPALayer_3 = eAVEncMPALayer.eAVEncMPALayer_3

        # AVEncMPACodingMode (UINT)
        CODECAPI_AVEncMPACodingMode = DEFINE_CODECAPI_GUID(
            "B16ADE03-4B93-43D7-A550-90B4FE224537",
            0xB16ADE03,
            0x4B93,
            0x43D7,
            0xA5,
            0x50,
            0x90,
            0xB4,
            0xFE,
            0x22,
            0x45,
            0x37
        )


        class eAVEncMPACodingMode(ENUM):
            eAVEncMPACodingMode_Mono = 0
            eAVEncMPACodingMode_Stereo = 1
            eAVEncMPACodingMode_DualChannel = 2
            eAVEncMPACodingMode_JointStereo = 3
            eAVEncMPACodingMode_Surround = 4


        eAVEncMPACodingMode_Mono = eAVEncMPACodingMode.eAVEncMPACodingMode_Mono
        eAVEncMPACodingMode_Stereo = eAVEncMPACodingMode.eAVEncMPACodingMode_Stereo
        eAVEncMPACodingMode_DualChannel = eAVEncMPACodingMode.eAVEncMPACodingMode_DualChannel
        eAVEncMPACodingMode_JointStereo = eAVEncMPACodingMode.eAVEncMPACodingMode_JointStereo
        eAVEncMPACodingMode_Surround = eAVEncMPACodingMode.eAVEncMPACodingMode_Surround

        # AVEncMPACopyright (BOOL) - default state to encode into the stream
        # (may be overridden by input)
        # 1 (true) - copyright protected
        # 0 (false) - not copyright protected
        CODECAPI_AVEncMPACopyright = DEFINE_CODECAPI_GUID(
            "A6AE762A-D0A9-4454-B8EF-F2DBEEFDD3BD",
            0xA6AE762A,
            0xD0A9,
            0x4454,
            0xB8,
            0xEF,
            0xF2,
            0xDB,
            0xEE,
            0xFD,
            0xD3,
            0xBD
        )

        # AVEncMPAOriginalBitstream (BOOL) - default value to encode into the
        # stream (may be overridden by input)
        # 1 (true) - for original bitstream
        # 0 (false) - for copy bitstream
        CODECAPI_AVEncMPAOriginalBitstream = DEFINE_CODECAPI_GUID(
            "3CFB7855-9CC9-47FF-B829-B36786C92346",
            0x3CFB7855,
            0x9CC9,
            0x47FF,
            0xB8,
            0x29,
            0xB3,
            0x67,
            0x86,
            0xC9,
            0x23,
            0x46
        )

        # AVEncMPAEnableRedundancyProtection (BOOL)
        # 1 (true) - Redundancy should be added to facilitate error detection
        # and concealment (CRC)
        # 0 (false) - No redundancy should be added
        CODECAPI_AVEncMPAEnableRedundancyProtection = DEFINE_CODECAPI_GUID(
            "5E54B09E-B2E7-4973-A89B-0B3650A3BEDA",
            0x5E54B09E,
            0xB2E7,
            0x4973,
            0xA8,
            0x9B,
            0x0B,
            0x36,
            0x50,
            0xA3,
            0xBE,
            0xDA
        )

        # AVEncMPAPrivateUserBit (UINT) - User data bit value to encode in the
        # stream
        CODECAPI_AVEncMPAPrivateUserBit = DEFINE_CODECAPI_GUID(
            "AFA505CE-C1E3-4E3D-851B-61B700E5E6CC",
            0xAFA505CE,
            0xC1E3,
            0x4E3D,
            0x85,
            0x1B,
            0x61,
            0xB7,
            0x00,
            0xE5,
            0xE6,
            0xCC
        )

        # AVEncMPAEmphasisType (UINT)
        # Indicates type of de - emphasis filter to be used
        CODECAPI_AVEncMPAEmphasisType = DEFINE_CODECAPI_GUID(
            "2D59FCDA-BF4E-4ED6-B5DF-5B03B36B0A1F",
            0x2D59FCDA,
            0xBF4E,
            0x4ED6,
            0xB5,
            0xDF,
            0x5B,
            0x03,
            0xB3,
            0x6B,
            0x0A,
            0x1F
        )


        class eAVEncMPAEmphasisType(ENUM):
            eAVEncMPAEmphasisType_None = 0
            eAVEncMPAEmphasisType_50_15 = 1
            eAVEncMPAEmphasisType_Reserved = 2
            eAVEncMPAEmphasisType_CCITT_J17 = 3


        eAVEncMPAEmphasisType_None = eAVEncMPAEmphasisType.eAVEncMPAEmphasisType_None
        eAVEncMPAEmphasisType_50_15 = eAVEncMPAEmphasisType.eAVEncMPAEmphasisType_50_15
        eAVEncMPAEmphasisType_Reserved = eAVEncMPAEmphasisType.eAVEncMPAEmphasisType_Reserved
        eAVEncMPAEmphasisType_CCITT_J17 = eAVEncMPAEmphasisType.eAVEncMPAEmphasisType_CCITT_J17

        # Dolby Digital(TM) Audio Encoding Interface
        # Dolby Digital(TM) Audio Specific Parameters
        # AVEncDDService (UINT)
        CODECAPI_AVEncDDService = DEFINE_CODECAPI_GUID(
            "D2E1BEC7-5172-4D2A-A50E-2F3B82B1DDF8",
            0xD2E1BEC7,
            0x5172,
            0x4D2A,
            0xA5,
            0x0E,
            0x2F,
            0x3B,
            0x82,
            0xB1,
            0xDD,
            0xF8
        )


        class eAVEncDDService(ENUM):
            eAVEncDDService_CM = 0
            eAVEncDDService_ME = 1
            eAVEncDDService_VI = 2
            eAVEncDDService_HI = 3
            eAVEncDDService_D = 4
            eAVEncDDService_C = 5
            eAVEncDDService_E = 6
            eAVEncDDService_VO = 7


        eAVEncDDService_CM = eAVEncDDService.eAVEncDDService_CM
        eAVEncDDService_ME = eAVEncDDService.eAVEncDDService_ME
        eAVEncDDService_VI = eAVEncDDService.eAVEncDDService_VI
        eAVEncDDService_HI = eAVEncDDService.eAVEncDDService_HI
        eAVEncDDService_D = eAVEncDDService.eAVEncDDService_D
        eAVEncDDService_C = eAVEncDDService.eAVEncDDService_C
        eAVEncDDService_E = eAVEncDDService.eAVEncDDService_E
        eAVEncDDService_VO = eAVEncDDService.eAVEncDDService_VO

        # AVEncDDDialogNormalization (UINT32)
        CODECAPI_AVEncDDDialogNormalization = DEFINE_CODECAPI_GUID(
            "D7055ACF-F125-437D-A704-79C79F0404A8",
            0xD7055ACF,
            0xF125,
            0x437D,
            0xA7,
            0x04,
            0x79,
            0xC7,
            0x9F,
            0x04,
            0x04,
            0xA8
        )

        # AVEncDDCentreDownMixLevel (UINT32)
        CODECAPI_AVEncDDCentreDownMixLevel = DEFINE_CODECAPI_GUID(
            "E285072C-C958-4A81-AFD2-E5E0DAF1B148",
            0xE285072C,
            0xC958,
            0x4A81,
            0xAF,
            0xD2,
            0xE5,
            0xE0,
            0xDA,
            0xF1,
            0xB1,
            0x48
        )

        # AVEncDDSurroundDownMixLevel (UINT32)
        CODECAPI_AVEncDDSurroundDownMixLevel = DEFINE_CODECAPI_GUID(
            "7B20D6E5-0BCF-4273-A487-506B047997E9",
            0x7B20D6E5,
            0x0BCF,
            0x4273,
            0xA4,
            0x87,
            0x50,
            0x6B,
            0x04,
            0x79,
            0x97,
            0xE9
        )

        # AVEncDDProductionInfoExists (BOOL)
        CODECAPI_AVEncDDProductionInfoExists = DEFINE_CODECAPI_GUID(
            "B0B7FE5F-B6AB-4F40-964D-8D91F17C19E8",
            0xB0B7FE5F,
            0xB6AB,
            0x4F40,
            0x96,
            0x4D,
            0x8D,
            0x91,
            0xF1,
            0x7C,
            0x19,
            0xE8
        )

        # AVEncDDProductionRoomType (UINT32)
        CODECAPI_AVEncDDProductionRoomType = DEFINE_CODECAPI_GUID(
            "DAD7AD60-23D8-4AB7-A284-556986D8A6FE",
            0xDAD7AD60,
            0x23D8,
            0x4AB7,
            0xA2,
            0x84,
            0x55,
            0x69,
            0x86,
            0xD8,
            0xA6,
            0xFE
        )


        class eAVEncDDProductionRoomType(ENUM):
            eAVEncDDProductionRoomType_NotIndicated = 0
            eAVEncDDProductionRoomType_Large = 1
            eAVEncDDProductionRoomType_Small = 2


        eAVEncDDProductionRoomType_NotIndicated = eAVEncDDProductionRoomType.eAVEncDDProductionRoomType_NotIndicated
        eAVEncDDProductionRoomType_Large = eAVEncDDProductionRoomType.eAVEncDDProductionRoomType_Large
        eAVEncDDProductionRoomType_Small = eAVEncDDProductionRoomType.eAVEncDDProductionRoomType_Small

        # AVEncDDProductionMixLevel (UINT32)
        CODECAPI_AVEncDDProductionMixLevel = DEFINE_CODECAPI_GUID(
            "301D103A-CBF9-4776-8899-7C15B461AB26",
            0x301D103A,
            0xCBF9,
            0x4776,
            0x88,
            0x99,
            0x7C,
            0x15,
            0xB4,
            0x61,
            0xAB,
            0x26
        )

        # AVEncDDCopyright (BOOL)
        CODECAPI_AVEncDDCopyright = DEFINE_CODECAPI_GUID(
            "8694F076-CD75-481D-A5C6-A904DCC828F0",
            0x8694F076,
            0xCD75,
            0x481D,
            0xA5,
            0xC6,
            0xA9,
            0x04,
            0xDC,
            0xC8,
            0x28,
            0xF0
        )

        # AVEncDDOriginalBitstream (BOOL)
        CODECAPI_AVEncDDOriginalBitstream = DEFINE_CODECAPI_GUID(
            "966AE800-5BD3-4FF9-95B9-D30566273856",
            0x966AE800,
            0x5BD3,
            0x4FF9,
            0x95,
            0xB9,
            0xD3,
            0x05,
            0x66,
            0x27,
            0x38,
            0x56
        )

        # AVEncDDDigitalDeemphasis (BOOL)
        CODECAPI_AVEncDDDigitalDeemphasis = DEFINE_CODECAPI_GUID(
            "E024A2C2-947C-45AC-87D8-F1030C5C0082",
            0xE024A2C2,
            0x947C,
            0x45AC,
            0x87,
            0xD8,
            0xF1,
            0x03,
            0x0C,
            0x5C,
            0x00,
            0x82
        )

        # AVEncDDDCHighPassFilter (BOOL)
        CODECAPI_AVEncDDDCHighPassFilter = DEFINE_CODECAPI_GUID(
            "9565239F-861C-4AC8-BFDA-E00CB4DB8548",
            0x9565239F,
            0x861C,
            0x4AC8,
            0xBF,
            0xDA,
            0xE0,
            0x0C,
            0xB4,
            0xDB,
            0x85,
            0x48
        )

        # AVEncDDChannelBWLowPassFilter (BOOL)
        CODECAPI_AVEncDDChannelBWLowPassFilter = DEFINE_CODECAPI_GUID(
            "E197821D-D2E7-43E2-AD2C-00582F518545",
            0xE197821D,
            0xD2E7,
            0x43E2,
            0xAD,
            0x2C,
            0x00,
            0x58,
            0x2F,
            0x51,
            0x85,
            0x45
        )

        # AVEncDDLFELowPassFilter (BOOL)
        CODECAPI_AVEncDDLFELowPassFilter = DEFINE_CODECAPI_GUID(
            "D3B80F6F-9D15-45E5-91BE-019C3FAB1F01",
            0xD3B80F6F,
            0x9D15,
            0x45E5,
            0x91,
            0xBE,
            0x01,
            0x9C,
            0x3F,
            0xAB,
            0x1F,
            0x01
        )

        # AVEncDDSurround90DegreeePhaseShift (BOOL)
        CODECAPI_AVEncDDSurround90DegreeePhaseShift = DEFINE_CODECAPI_GUID(
            "25ECEC9D-3553-42C0-BB56-D25792104F80",
            0x25ECEC9D,
            0x3553,
            0x42C0,
            0xBB,
            0x56,
            0xD2,
            0x57,
            0x92,
            0x10,
            0x4F,
            0x80
        )

        # AVEncDDSurround3dBAttenuation (BOOL)
        CODECAPI_AVEncDDSurround3dBAttenuation = DEFINE_CODECAPI_GUID(
            "4D43B99D-31E2-48B9-BF2E-5CBF1A572784",
            0x4D43B99D,
            0x31E2,
            0x48B9,
            0xBF,
            0x2E,
            0x5C,
            0xBF,
            0x1A,
            0x57,
            0x27,
            0x84
        )

        # AVEncDDDynamicRangeCompressionControl (UINT32)
        CODECAPI_AVEncDDDynamicRangeCompressionControl = DEFINE_CODECAPI_GUID(
            "CFC2FF6D-79B8-4B8D-A8AA-A0C9BD1C2940",
            0xCFC2FF6D,
            0x79B8,
            0x4B8D,
            0xA8,
            0xAA,
            0xA0,
            0xC9,
            0xBD,
            0x1C,
            0x29,
            0x40
        )


        class eAVEncDDDynamicRangeCompressionControl(ENUM):
            eAVEncDDDynamicRangeCompressionControl_None = 0
            eAVEncDDDynamicRangeCompressionControl_FilmStandard = 1
            eAVEncDDDynamicRangeCompressionControl_FilmLight = 2
            eAVEncDDDynamicRangeCompressionControl_MusicStandard = 3
            eAVEncDDDynamicRangeCompressionControl_MusicLight = 4
            eAVEncDDDynamicRangeCompressionControl_Speech = 5


        eAVEncDDDynamicRangeCompressionControl_None = eAVEncDDDynamicRangeCompressionControl.eAVEncDDDynamicRangeCompressionControl_None
        eAVEncDDDynamicRangeCompressionControl_FilmStandard = eAVEncDDDynamicRangeCompressionControl.eAVEncDDDynamicRangeCompressionControl_FilmStandard
        eAVEncDDDynamicRangeCompressionControl_FilmLight = eAVEncDDDynamicRangeCompressionControl.eAVEncDDDynamicRangeCompressionControl_FilmLight
        eAVEncDDDynamicRangeCompressionControl_MusicStandard = eAVEncDDDynamicRangeCompressionControl.eAVEncDDDynamicRangeCompressionControl_MusicStandard
        eAVEncDDDynamicRangeCompressionControl_MusicLight = eAVEncDDDynamicRangeCompressionControl.eAVEncDDDynamicRangeCompressionControl_MusicLight
        eAVEncDDDynamicRangeCompressionControl_Speech = eAVEncDDDynamicRangeCompressionControl.eAVEncDDDynamicRangeCompressionControl_Speech

        # AVEncDDRFPreEmphasisFilter (BOOL)
        CODECAPI_AVEncDDRFPreEmphasisFilter = DEFINE_CODECAPI_GUID(
            "21AF44C0-244E-4F3D-A2CC-3D3068B2E73F",
            0x21AF44C0,
            0x244E,
            0x4F3D,
            0xA2,
            0xCC,
            0x3D,
            0x30,
            0x68,
            0xB2,
            0xE7,
            0x3F
        )

        # AVEncDDSurroundExMode (UINT32)
        CODECAPI_AVEncDDSurroundExMode = DEFINE_CODECAPI_GUID(
            "91607CEE-DBDD-4EB6-BCA2-AADFAFA3DD68",
            0x91607CEE,
            0xDBDD,
            0x4EB6,
            0xBC,
            0xA2,
            0xAA,
            0xDF,
            0xAF,
            0xA3,
            0xDD,
            0x68
        )


        class eAVEncDDSurroundExMode(ENUM):
            eAVEncDDSurroundExMode_NotIndicated = 0
            eAVEncDDSurroundExMode_No = 1
            eAVEncDDSurroundExMode_Yes = 2


        eAVEncDDSurroundExMode_NotIndicated = eAVEncDDSurroundExMode.eAVEncDDSurroundExMode_NotIndicated
        eAVEncDDSurroundExMode_No = eAVEncDDSurroundExMode.eAVEncDDSurroundExMode_No
        eAVEncDDSurroundExMode_Yes = eAVEncDDSurroundExMode.eAVEncDDSurroundExMode_Yes

        # AVEncDDPreferredStereoDownMixMode (UINT32)
        CODECAPI_AVEncDDPreferredStereoDownMixMode = DEFINE_CODECAPI_GUID(
            "7F4E6B31-9185-403D-B0A2-763743E6F063",
            0x7F4E6B31,
            0x9185,
            0x403D,
            0xB0,
            0xA2,
            0x76,
            0x37,
            0x43,
            0xE6,
            0xF0,
            0x63
        )


        class eAVEncDDPreferredStereoDownMixMode(ENUM):
            eAVEncDDPreferredStereoDownMixMode_LtRt = 0
            eAVEncDDPreferredStereoDownMixMode_LoRo = 1


        eAVEncDDPreferredStereoDownMixMode_LtRt = eAVEncDDPreferredStereoDownMixMode.eAVEncDDPreferredStereoDownMixMode_LtRt
        eAVEncDDPreferredStereoDownMixMode_LoRo = eAVEncDDPreferredStereoDownMixMode.eAVEncDDPreferredStereoDownMixMode_LoRo

        # AVEncDDLtRtCenterMixLvl_x10 (INT32)
        CODECAPI_AVEncDDLtRtCenterMixLvl_x10 = DEFINE_CODECAPI_GUID(
            "DCA128A2-491F-4600-B2DA-76E3344B4197",
            0xDCA128A2,
            0x491F,
            0x4600,
            0xB2,
            0xDA,
            0x76,
            0xE3,
            0x34,
            0x4B,
            0x41,
            0x97
        )

        # AVEncDDLtRtSurroundMixLvl_x10 (INT32)
        CODECAPI_AVEncDDLtRtSurroundMixLvl_x10 = DEFINE_CODECAPI_GUID(
            "212246C7-3D2C-4DFA-BC21-652A9098690D",
            0x212246C7,
            0x3D2C,
            0x4DFA,
            0xBC,
            0x21,
            0x65,
            0x2A,
            0x90,
            0x98,
            0x69,
            0x0D
        )

        # AVEncDDLoRoCenterMixLvl (INT32)
        CODECAPI_AVEncDDLoRoCenterMixLvl_x10 = DEFINE_CODECAPI_GUID(
            "1CFBA222-25B3-4BF4-9BFD-E7111267858C",
            0x1CFBA222,
            0x25B3,
            0x4BF4,
            0x9B,
            0xFD,
            0xE7,
            0x11,
            0x12,
            0x67,
            0x85,
            0x8C
        )

        # AVEncDDLoRoSurroundMixLvl_x10 (INT32)
        CODECAPI_AVEncDDLoRoSurroundMixLvl_x10 = DEFINE_CODECAPI_GUID(
            "E725CFF6-EB56-40C7-8450-2B9367E91555",
            0xE725CFF6,
            0xEB56,
            0x40C7,
            0x84,
            0x50,
            0x2B,
            0x93,
            0x67,
            0xE9,
            0x15,
            0x55
        )

        # AVEncDDAtoDConverterType (UINT32)
        CODECAPI_AVEncDDAtoDConverterType = DEFINE_CODECAPI_GUID(
            "719F9612-81A1-47E0-9A05-D94AD5FCA948",
            0x719F9612,
            0x81A1,
            0x47E0,
            0x9A,
            0x05,
            0xD9,
            0x4A,
            0xD5,
            0xFC,
            0xA9,
            0x48
        )


        class eAVEncDDAtoDConverterType(ENUM):
            eAVEncDDAtoDConverterType_Standard = 0
            eAVEncDDAtoDConverterType_HDCD = 1


        eAVEncDDAtoDConverterType_Standard = eAVEncDDAtoDConverterType.eAVEncDDAtoDConverterType_Standard
        eAVEncDDAtoDConverterType_HDCD = eAVEncDDAtoDConverterType.eAVEncDDAtoDConverterType_HDCD

        # AVEncDDHeadphoneMode (UINT32)
        CODECAPI_AVEncDDHeadphoneMode = DEFINE_CODECAPI_GUID(
            "4052DBEC-52F5-42F5-9B00-D134B1341B9D",
            0x4052DBEC,
            0x52F5,
            0x42F5,
            0x9B,
            0x00,
            0xD1,
            0x34,
            0xB1,
            0x34,
            0x1B,
            0x9D
        )


        class eAVEncDDHeadphoneMode(ENUM):
            eAVEncDDHeadphoneMode_NotIndicated = 0
            eAVEncDDHeadphoneMode_NotEncoded = 1
            eAVEncDDHeadphoneMode_Encoded = 2


        eAVEncDDHeadphoneMode_NotIndicated = eAVEncDDHeadphoneMode.eAVEncDDHeadphoneMode_NotIndicated
        eAVEncDDHeadphoneMode_NotEncoded = eAVEncDDHeadphoneMode.eAVEncDDHeadphoneMode_NotEncoded
        eAVEncDDHeadphoneMode_Encoded = eAVEncDDHeadphoneMode.eAVEncDDHeadphoneMode_Encoded

        # WMV Video Encoding Interface
        # WMV Video Specific Parameters
        # AVEncWMVKeyFrameDistance (UINT32)
        CODECAPI_AVEncWMVKeyFrameDistance = DEFINE_CODECAPI_GUID(
            "5569055E-E268-4771-B83E-9555EA28AED3",
            0x5569055E,
            0xE268,
            0x4771,
            0xB8,
            0x3E,
            0x95,
            0x55,
            0xEA,
            0x28,
            0xAE,
            0xD3
        )

        # AVEncWMVInterlacedEncoding (UINT32)
        CODECAPI_AVEncWMVInterlacedEncoding = DEFINE_CODECAPI_GUID(
            "E3D00F8A-C6F5-4E14-A588-0EC87A726F9B",
            0xE3D00F8A,
            0xC6F5,
            0x4E14,
            0xA5,
            0x88,
            0x0E,
            0xC8,
            0x7A,
            0x72,
            0x6F,
            0x9B
        )

        # AVEncWMVDecoderComplexity (UINT32)
        CODECAPI_AVEncWMVDecoderComplexity = DEFINE_CODECAPI_GUID(
            "F32C0DAB-F3CB-4217-B79F-8762768B5F67",
            0xF32C0DAB,
            0xF3CB,
            0x4217,
            0xB7,
            0x9F,
            0x87,
            0x62,
            0x76,
            0x8B,
            0x5F,
            0x67
        )

        # AVEncWMVHasKeyFrameBufferLevelMarker (BOOL)
        CODECAPI_AVEncWMVKeyFrameBufferLevelMarker = DEFINE_CODECAPI_GUID(
            "51FF1115-33AC-426C-A1B1-09321BDF96B4",
            0x51FF1115,
            0x33AC,
            0x426C,
            0xA1,
            0xB1,
            0x09,
            0x32,
            0x1B,
            0xDF,
            0x96,
            0xB4
        )

        # AVEncWMVProduceDummyFrames (UINT32)
        CODECAPI_AVEncWMVProduceDummyFrames = DEFINE_CODECAPI_GUID(
            "D669D001-183C-42E3-A3CA-2F4586D2396C",
            0xD669D001,
            0x183C,
            0x42E3,
            0xA3,
            0xCA,
            0x2F,
            0x45,
            0x86,
            0xD2,
            0x39,
            0x6C
        )

        # WMV Post - Encode Statistical Parameters
        # AVEncStatWMVCBAvg (UINT32/UINT32)
        CODECAPI_AVEncStatWMVCBAvg = DEFINE_CODECAPI_GUID(
            "6AA6229F-D602-4B9D-B68C-C1AD78884BEF",
            0x6AA6229F,
            0xD602,
            0x4B9D,
            0xB6,
            0x8C,
            0xC1,
            0xAD,
            0x78,
            0x88,
            0x4B,
            0xEF
        )

        # AVEncStatWMVCBMax (UINT32/UINT32)
        CODECAPI_AVEncStatWMVCBMax = DEFINE_CODECAPI_GUID(
            "E976BEF8-00FE-44B4-B625-8F238BC03499",
            0xE976BEF8,
            0x00FE,
            0x44B4,
            0xB6,
            0x25,
            0x8F,
            0x23,
            0x8B,
            0xC0,
            0x34,
            0x99
        )

        # AVEncStatWMVDecoderComplexityProfile (UINT32)
        CODECAPI_AVEncStatWMVDecoderComplexityProfile = DEFINE_CODECAPI_GUID(
            "89E69FC3-0F9B-436C-974A-DF821227C90D",
            0x89E69FC3,
            0x0F9B,
            0x436C,
            0x97,
            0x4A,
            0xDF,
            0x82,
            0x12,
            0x27,
            0xC9,
            0x0D
        )

        # AVEncStatMPVSkippedEmptyFrames (UINT32)
        CODECAPI_AVEncStatMPVSkippedEmptyFrames = DEFINE_CODECAPI_GUID(
            "32195FD3-590D-4812-A7ED-6D639A1F9711",
            0x32195FD3,
            0x590D,
            0x4812,
            0xA7,
            0xED,
            0x6D,
            0x63,
            0x9A,
            0x1F,
            0x97,
            0x11
        )

        # MPEG1/2 Multiplexer Interfaces
        # MPEG1/2 Packetizer Interface
        # Shared with Mux:
        # AVEncMP12MuxEarliestPTS (UINT32)
        # AVEncMP12MuxLargestPacketSize (UINT32)
        # AVEncMP12MuxSysSTDBufferBound (UINT32)
        # AVEncMP12PktzSTDBuffer (UINT32)
        CODECAPI_AVEncMP12PktzSTDBuffer = DEFINE_CODECAPI_GUID(
            "0B751BD0-819E-478C-9435-75208926B377",
            0x0B751BD0,
            0x819E,
            0x478C,
            0x94,
            0x35,
            0x75,
            0x20,
            0x89,
            0x26,
            0xB3,
            0x77
        )

        # AVEncMP12PktzStreamID (UINT32)
        CODECAPI_AVEncMP12PktzStreamID = DEFINE_CODECAPI_GUID(
            "C834D038-F5E8-4408-9B60-88F36493FEDF",
            0xC834D038,
            0xF5E8,
            0x4408,
            0x9B,
            0x60,
            0x88,
            0xF3,
            0x64,
            0x93,
            0xFE,
            0xDF
        )

        # AVEncMP12PktzInitialPTS (UINT32)
        CODECAPI_AVEncMP12PktzInitialPTS = DEFINE_CODECAPI_GUID(
            "2A4F2065-9A63-4D20-AE22-0A1BC896A315",
            0x2A4F2065,
            0x9A63,
            0x4D20,
            0xAE,
            0x22,
            0x0A,
            0x1B,
            0xC8,
            0x96,
            0xA3,
            0x15
        )

        # AVEncMP12PktzPacketSize (UINT32)
        CODECAPI_AVEncMP12PktzPacketSize = DEFINE_CODECAPI_GUID(
            "AB71347A-1332-4DDE-A0E5-CCF7DA8A0F22",
            0xAB71347A,
            0x1332,
            0x4DDE,
            0xA0,
            0xE5,
            0xCC,
            0xF7,
            0xDA,
            0x8A,
            0x0F,
            0x22
        )

        # AVEncMP12PktzCopyright (BOOL)
        CODECAPI_AVEncMP12PktzCopyright = DEFINE_CODECAPI_GUID(
            "C8F4B0C1-094C-43C7-8E68-A595405A6EF8",
            0xC8F4B0C1,
            0x094C,
            0x43C7,
            0x8E,
            0x68,
            0xA5,
            0x95,
            0x40,
            0x5A,
            0x6E,
            0xF8
        )

        # AVEncMP12PktzOriginal (BOOL)
        CODECAPI_AVEncMP12PktzOriginal = DEFINE_CODECAPI_GUID(
            "6B178416-31B9-4964-94CB-6BFF866CDF83",
            0x6B178416,
            0x31B9,
            0x4964,
            0x94,
            0xCB,
            0x6B,
            0xFF,
            0x86,
            0x6C,
            0xDF,
            0x83
        )

        # MPEG1/2 Multiplexer Interface
        # AVEncMP12MuxPacketOverhead (UINT32)
        CODECAPI_AVEncMP12MuxPacketOverhead = DEFINE_CODECAPI_GUID(
            "E40BD720-3955-4453-ACF9-B79132A38FA0",
            0xE40BD720,
            0x3955,
            0x4453,
            0xAC,
            0xF9,
            0xB7,
            0x91,
            0x32,
            0xA3,
            0x8F,
            0xA0
        )

        # AVEncMP12MuxNumStreams (UINT32)
        CODECAPI_AVEncMP12MuxNumStreams = DEFINE_CODECAPI_GUID(
            "F7164A41-DCED-4659-A8F2-FB693F2A4CD0",
            0xF7164A41,
            0xDCED,
            0x4659,
            0xA8,
            0xF2,
            0xFB,
            0x69,
            0x3F,
            0x2A,
            0x4C,
            0xD0
        )

        # AVEncMP12MuxEarliestPTS (UINT32)
        CODECAPI_AVEncMP12MuxEarliestPTS = DEFINE_CODECAPI_GUID(
            "157232B6-F809-474E-9464-A7F93014A817",
            0x157232B6,
            0xF809,
            0x474E,
            0x94,
            0x64,
            0xA7,
            0xF9,
            0x30,
            0x14,
            0xA8,
            0x17
        )

        # AVEncMP12MuxLargestPacketSize (UINT32)
        CODECAPI_AVEncMP12MuxLargestPacketSize = DEFINE_CODECAPI_GUID(
            "35CEB711-F461-4B92-A4EF-17B6841ED254",
            0x35CEB711,
            0xF461,
            0x4B92,
            0xA4,
            0xEF,
            0x17,
            0xB6,
            0x84,
            0x1E,
            0xD2,
            0x54
        )

        # AVEncMP12MuxInitialSCR (UINT32)
        CODECAPI_AVEncMP12MuxInitialSCR = DEFINE_CODECAPI_GUID(
            "3433AD21-1B91-4A0B-B190-2B77063B63A4",
            0x3433AD21,
            0x1B91,
            0x4A0B,
            0xB1,
            0x90,
            0x2B,
            0x77,
            0x06,
            0x3B,
            0x63,
            0xA4
        )

        # AVEncMP12MuxMuxRate (UINT32)
        CODECAPI_AVEncMP12MuxMuxRate = DEFINE_CODECAPI_GUID(
            "EE047C72-4BDB-4A9D-8E21-41926C823DA7",
            0xEE047C72,
            0x4BDB,
            0x4A9D,
            0x8E,
            0x21,
            0x41,
            0x92,
            0x6C,
            0x82,
            0x3D,
            0xA7
        )

        # AVEncMP12MuxPackSize (UINT32)
        CODECAPI_AVEncMP12MuxPackSize = DEFINE_CODECAPI_GUID(
            "F916053A-1CE8-4FAF-AA0B-BA31C80034B8",
            0xF916053A,
            0x1CE8,
            0x4FAF,
            0xAA,
            0x0B,
            0xBA,
            0x31,
            0xC8,
            0x00,
            0x34,
            0xB8
        )

        # AVEncMP12MuxSysSTDBufferBound (UINT32)
        CODECAPI_AVEncMP12MuxSysSTDBufferBound = DEFINE_CODECAPI_GUID(
            "35746903-B545-43E7-BB35-C5E0A7D5093C",
            0x35746903,
            0xB545,
            0x43E7,
            0xBB,
            0x35,
            0xC5,
            0xE0,
            0xA7,
            0xD5,
            0x09,
            0x3C
        )

        # AVEncMP12MuxSysRateBound (UINT32)
        CODECAPI_AVEncMP12MuxSysRateBound = DEFINE_CODECAPI_GUID(
            "05F0428A-EE30-489D-AE28-205C72446710",
            0x05F0428A,
            0xEE30,
            0x489D,
            0xAE,
            0x28,
            0x20,
            0x5C,
            0x72,
            0x44,
            0x67,
            0x10
        )

        # AVEncMP12MuxTargetPacketizer (UINT32)
        CODECAPI_AVEncMP12MuxTargetPacketizer = DEFINE_CODECAPI_GUID(
            "D862212A-2015-45DD-9A32-1B3AA88205A0",
            0xD862212A,
            0x2015,
            0x45DD,
            0x9A,
            0x32,
            0x1B,
            0x3A,
            0xA8,
            0x82,
            0x05,
            0xA0
        )

        # AVEncMP12MuxSysFixed (UINT32)
        CODECAPI_AVEncMP12MuxSysFixed = DEFINE_CODECAPI_GUID(
            "CEFB987E-894F-452E-8F89-A4EF8CEC063A",
            0xCEFB987E,
            0x894F,
            0x452E,
            0x8F,
            0x89,
            0xA4,
            0xEF,
            0x8C,
            0xEC,
            0x06,
            0x3A
        )

        # AVEncMP12MuxSysCSPS (UINT32)
        CODECAPI_AVEncMP12MuxSysCSPS = DEFINE_CODECAPI_GUID(
            "7952FF45-9C0D-4822-BC82-8AD772E02993",
            0x7952FF45,
            0x9C0D,
            0x4822,
            0xBC,
            0x82,
            0x8A,
            0xD7,
            0x72,
            0xE0,
            0x29,
            0x93
        )

        # AVEncMP12MuxSysVideoLock (BOOL)
        CODECAPI_AVEncMP12MuxSysVideoLock = DEFINE_CODECAPI_GUID(
            "B8296408-2430-4D37-A2A1-95B3E435A91D",
            0xB8296408,
            0x2430,
            0x4D37,
            0xA2,
            0xA1,
            0x95,
            0xB3,
            0xE4,
            0x35,
            0xA9,
            0x1D
        )

        # AVEncMP12MuxSysAudioLock (BOOL)
        CODECAPI_AVEncMP12MuxSysAudioLock = DEFINE_CODECAPI_GUID(
            "0FBB5752-1D43-47BF-BD79-F2293D8CE337",
            0x0FBB5752,
            0x1D43,
            0x47BF,
            0xBD,
            0x79,
            0xF2,
            0x29,
            0x3D,
            0x8C,
            0xE3,
            0x37
        )

        # AVEncMP12MuxDVDNavPacks (BOOL)
        CODECAPI_AVEncMP12MuxDVDNavPacks = DEFINE_CODECAPI_GUID(
            "C7607CED-8CF1-4A99-83A1-EE5461BE3574",
            0xC7607CED,
            0x8CF1,
            0x4A99,
            0x83,
            0xA1,
            0xEE,
            0x54,
            0x61,
            0xBE,
            0x35,
            0x74
        )

        # Decoding Interface
        # format values are GUIDs as VARIANT BSTRs
        CODECAPI_AVDecCommonInputFormat = DEFINE_CODECAPI_GUID(
            "E5005239-BD89-4BE3-9C0F-5DDE317988CC",
            0xE5005239,
            0xBD89,
            0x4BE3,
            0x9C,
            0x0F,
            0x5D,
            0xDE,
            0x31,
            0x79,
            0x88,
            0xCC
        )
        CODECAPI_AVDecCommonOutputFormat = DEFINE_CODECAPI_GUID(
            "3C790028-C0CE-4256-B1A2-1B0FC8B1DCDC",
            0x3C790028,
            0xC0CE,
            0x4256,
            0xB1,
            0xA2,
            0x1B,
            0x0F,
            0xC8,
            0xB1,
            0xDC,
            0xDC
        )

        # AVDecCommonMeanBitRate - Mean bitrate in mbits/sec (UINT32)
        CODECAPI_AVDecCommonMeanBitRate = DEFINE_CODECAPI_GUID(
            "59488217-007A-4F7A-8E41-5C48B1EAC5C6",
            0x59488217,
            0x007A,
            0x4F7A,
            0x8E,
            0x41,
            0x5C,
            0x48,
            0xB1,
            0xEA,
            0xC5,
            0xC6
        )

        # AVDecCommonMeanBitRateInterval - Mean bitrate interval (in 100ns)
        # (UINT64)
        CODECAPI_AVDecCommonMeanBitRateInterval = DEFINE_CODECAPI_GUID(
            "0EE437C6-38A7-4C5C-944C-68AB42116B85",
            0x0EE437C6,
            0x38A7,
            0x4C5C,
            0x94,
            0x4C,
            0x68,
            0xAB,
            0x42,
            0x11,
            0x6B,
            0x85
        )

        # Audio Decoding Interface
        # Value GUIDS
        # The following 6 GUIDs are values of the AVDecCommonOutputFormat
        # property
        # Stereo PCM output using matrix - encoded stereo down mix (aka Lt/Rt)
        CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_MatrixEncoded = DEFINE_CODECAPI_GUID(
            "696E1D30-548F-4036-825F-7026C60011BD",
            0x696E1D30,
            0x548F,
            0x4036,
            0x82,
            0x5F,
            0x70,
            0x26,
            0xC6,
            0x00,
            0x11,
            0xBD
        )

        # Regular PCM output (any number of channels)
        CODECAPI_GUID_AVDecAudioOutputFormat_PCM = DEFINE_CODECAPI_GUID(
            "696E1D31-548F-4036-825F-7026C60011BD",
            0x696E1D31,
            0x548F,
            0x4036,
            0x82,
            0x5F,
            0x70,
            0x26,
            0xC6,
            0x00,
            0x11,
            0xBD
        )

        # SPDIF PCM (IEC 60958) stereo output. Type of stereo down mix should
        # be specified by the application.
        CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_PCM = DEFINE_CODECAPI_GUID(
            "696E1D32-548F-4036-825F-7026C60011BD",
            0x696E1D32,
            0x548F,
            0x4036,
            0x82,
            0x5F,
            0x70,
            0x26,
            0xC6,
            0x00,
            0x11,
            0xBD
        )

        # SPDIF bitstream (IEC 61937) output, such as AC3, MPEG or DTS.
        CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_Bitstream = DEFINE_CODECAPI_GUID(
            "696E1D33-548F-4036-825F-7026C60011BD",
            0x696E1D33,
            0x548F,
            0x4036,
            0x82,
            0x5F,
            0x70,
            0x26,
            0xC6,
            0x00,
            0x11,
            0xBD
        )

        # Stereo PCM output using regular stereo down mix (aka Lo/Ro)
        CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Headphones = DEFINE_CODECAPI_GUID(
            "696E1D34-548F-4036-825F-7026C60011BD",
            0x696E1D34,
            0x548F,
            0x4036,
            0x82,
            0x5F,
            0x70,
            0x26,
            0xC6,
            0x00,
            0x11,
            0xBD
        )

        # Stereo PCM output using automatic selection of stereo down mix
        # mode (Lo/Ro or Lt/Rt). Use this when the input stream includes
        # information about the preferred downmix mode
        # (such as Annex D of AC3).
        # Default down mix mode should be specified by the application.
        CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_Auto = DEFINE_CODECAPI_GUID(
            "696E1D35-548F-4036-825F-7026C60011BD",
            0x696E1D35,
            0x548F,
            0x4036,
            0x82,
            0x5F,
            0x70,
            0x26,
            0xC6,
            0x00,
            0x11,
            0xBD
        )

        # Video Decoder properties
        # AVDecVideoImageSize (UINT32) - High UINT16 width, low UINT16 height
        CODECAPI_AVDecVideoImageSize = DEFINE_CODECAPI_GUID(
            "5EE5747C-6801-4CAB-AAF1-6248FA841BA4",
            0x5EE5747C,
            0x6801,
            0x4CAB,
            0xAA,
            0xF1,
            0x62,
            0x48,
            0xFA,
            0x84,
            0x1B,
            0xA4
        )

        # AVDecVideoPixelAspectRatio (UINT32 as UINT16/UNIT16) - High UINT16
        # width, low UINT16 height
        CODECAPI_AVDecVideoPixelAspectRatio = DEFINE_CODECAPI_GUID(
            "B0CF8245-F32D-41DF-B02C-87BD304D12AB",
            0xB0CF8245,
            0xF32D,
            0x41DF,
            0xB0,
            0x2C,
            0x87,
            0xBD,
            0x30,
            0x4D,
            0x12,
            0xAB
        )

        # AVDecVideoInputScanType (UINT32)
        CODECAPI_AVDecVideoInputScanType = DEFINE_CODECAPI_GUID(
            "38477E1F-0EA7-42CD-8CD1-130CED57C580",
            0x38477E1F,
            0x0EA7,
            0x42CD,
            0x8C,
            0xD1,
            0x13,
            0x0C,
            0xED,
            0x57,
            0xC5,
            0x80
        )


        class eAVDecVideoInputScanType(ENUM):
            eAVDecVideoInputScan_Unknown = 0
            eAVDecVideoInputScan_Progressive = 1
            eAVDecVideoInputScan_Interlaced_UpperFieldFirst = 2
            eAVDecVideoInputScan_Interlaced_LowerFieldFirst = 3


        eAVDecVideoInputScan_Unknown = eAVDecVideoInputScanType.eAVDecVideoInputScan_Unknown
        eAVDecVideoInputScan_Progressive = eAVDecVideoInputScanType.eAVDecVideoInputScan_Progressive
        eAVDecVideoInputScan_Interlaced_UpperFieldFirst = eAVDecVideoInputScanType.eAVDecVideoInputScan_Interlaced_UpperFieldFirst
        eAVDecVideoInputScan_Interlaced_LowerFieldFirst = eAVDecVideoInputScanType.eAVDecVideoInputScan_Interlaced_LowerFieldFirst

        # AVDecVideoSWPowerLevel (UINT32)
        # Related to video decoder software power saving level in MPEG4 Part
        # 2, VC1 and H264.
        # "SW Power Level" will take a range from 0 to 100 to indicate the
        # current power saving level. 0 - Optimize for battery life, 50 -
        # balanced, 100 - Optimize for video quality.
        CODECAPI_AVDecVideoSWPowerLevel = DEFINE_CODECAPI_GUID(
            "FB5D2347-4DD8-4509-AED0-DB5FA9AA93F4",
            0xFB5D2347,
            0x4DD8,
            0x4509,
            0xAE,
            0xD0,
            0xDB,
            0x5F,
            0xA9,
            0xAA,
            0x93,
            0xF4
        )


        class eAVDecVideoSWPowerLevel(ENUM):
            eAVDecVideoSWPowerLevel_BatteryLife = 0
            eAVDecVideoSWPowerLevel_Balanced = 50
            eAVDecVideoSWPowerLevel_VideoQuality = 100


        eAVDecVideoSWPowerLevel_BatteryLife = eAVDecVideoSWPowerLevel.eAVDecVideoSWPowerLevel_BatteryLife
        eAVDecVideoSWPowerLevel_Balanced = eAVDecVideoSWPowerLevel.eAVDecVideoSWPowerLevel_Balanced
        eAVDecVideoSWPowerLevel_VideoQuality = eAVDecVideoSWPowerLevel.eAVDecVideoSWPowerLevel_VideoQuality

        # Audio Decoder properties
        CODECAPI_GUID_AVDecAudioInputWMA = DEFINE_CODECAPI_GUID(
            "C95E8DCF-4058-4204-8C42-CB24D91E4B9B",
            0xC95E8DCF,
            0x4058,
            0x4204,
            0x8C,
            0x42,
            0xCB,
            0x24,
            0xD9,
            0x1E,
            0x4B,
            0x9B
        )
        CODECAPI_GUID_AVDecAudioInputWMAPro = DEFINE_CODECAPI_GUID(
            "0128B7C7-DA72-4FE3-BEF8-5C52E3557704",
            0x0128B7C7,
            0xDA72,
            0x4FE3,
            0xBE,
            0xF8,
            0x5C,
            0x52,
            0xE3,
            0x55,
            0x77,
            0x04
        )
        CODECAPI_GUID_AVDecAudioInputDolby = DEFINE_CODECAPI_GUID(
            "8E4228A0-F000-4E0B-8F54-AB8D24AD61A2",
            0x8E4228A0,
            0xF000,
            0x4E0B,
            0x8F,
            0x54,
            0xAB,
            0x8D,
            0x24,
            0xAD,
            0x61,
            0xA2
        )
        CODECAPI_GUID_AVDecAudioInputDTS = DEFINE_CODECAPI_GUID(
            "600BC0CA-6A1F-4E91-B241-1BBEB1CB19E0",
            0x600BC0CA,
            0x6A1F,
            0x4E91,
            0xB2,
            0x41,
            0x1B,
            0xBE,
            0xB1,
            0xCB,
            0x19,
            0xE0
        )
        CODECAPI_GUID_AVDecAudioInputPCM = DEFINE_CODECAPI_GUID(
            "F2421DA5-BBB4-4CD5-A996-933C6B5D1347",
            0xF2421DA5,
            0xBBB4,
            0x4CD5,
            0xA9,
            0x96,
            0x93,
            0x3C,
            0x6B,
            0x5D,
            0x13,
            0x47
        )
        CODECAPI_GUID_AVDecAudioInputMPEG = DEFINE_CODECAPI_GUID(
            "91106F36-02C5-4F75-9719-3B7ABF75E1F6",
            0x91106F36,
            0x02C5,
            0x4F75,
            0x97,
            0x19,
            0x3B,
            0x7A,
            0xBF,
            0x75,
            0xE1,
            0xF6
        )
        CODECAPI_GUID_AVDecAudioInputAAC = DEFINE_CODECAPI_GUID(
            "97DF7828-B94A-47E2-A4BC-51194DB22A4D",
            0x97DF7828,
            0xB94A,
            0x47E2,
            0xA4,
            0xBC,
            0x51,
            0x19,
            0x4D,
            0xB2,
            0x2A,
            0x4D
        )
        CODECAPI_GUID_AVDecAudioInputHEAAC = DEFINE_CODECAPI_GUID(
            "16EFB4AA-330E-4F5C-98A8-CF6AC55CBE60",
            0x16EFB4AA,
            0x330E,
            0x4F5C,
            0x98,
            0xA8,
            0xCF,
            0x6A,
            0xC5,
            0x5C,
            0xBE,
            0x60
        )
        CODECAPI_GUID_AVDecAudioInputDolbyDigitalPlus = DEFINE_CODECAPI_GUID(
            "0803E185-8F5D-47F5-9908-19A5BBC9FE34",
            0x0803E185,
            0x8F5D,
            0x47F5,
            0x99,
            0x08,
            0x19,
            0xA5,
            0xBB,
            0xC9,
            0xFE,
            0x34
        )

        # AVDecAACDownmixMode (UINT32)
        # AAC/HE - AAC Decoder uses standard ISO/IEC MPEG - 2/MPEG - 4 stereo
        # downmix equations or uses
        # non - standard downmix. An example of a non standard downmix would
        # be the one defined by ARIB document STD - B21 version 4.4.
        CODECAPI_AVDecAACDownmixMode = DEFINE_CODECAPI_GUID(
            "01274475-F6BB-4017-B084-81A763C942D4",
            0x1274475,
            0xF6BB,
            0x4017,
            0xB0,
            0x84,
            0x81,
            0xA7,
            0x63,
            0xC9,
            0x42,
            0xD4
        )


        class eAVDecAACDownmixMode(ENUM):
            eAVDecAACUseISODownmix = 0
            eAVDecAACUseARIBDownmix = 1


        eAVDecAACUseISODownmix = eAVDecAACDownmixMode.eAVDecAACUseISODownmix
        eAVDecAACUseARIBDownmix = eAVDecAACDownmixMode.eAVDecAACUseARIBDownmix

        # AVDecHEAACDynamicRangeControl (UINT32)
        # Set this property on an AAC/HE - AAC decoder to select whether
        # Dynamic Range Control (DRC) should be applied or not.
        # If DRC is ON and the AAC/HE - AAC stream includes extension payload
        # of type EXT_DYNAMIC_RANGE, DRC will be applied.
        CODECAPI_AVDecHEAACDynamicRangeControl = DEFINE_CODECAPI_GUID(
            "287C8ABE-69A4-4D39-8080-D3D9712178A0",
            0x287C8ABE,
            0x69A4,
            0x4D39,
            0x80,
            0x80,
            0xD3,
            0xD9,
            0x71,
            0x21,
            0x78,
            0xA0
        )


        class eAVDecHEAACDynamicRangeControl(ENUM):
            eAVDecHEAACDynamicRangeControl_OFF = 0
            eAVDecHEAACDynamicRangeControl_ON = 1


        eAVDecHEAACDynamicRangeControl_OFF = eAVDecHEAACDynamicRangeControl.eAVDecHEAACDynamicRangeControl_OFF
        eAVDecHEAACDynamicRangeControl_ON = eAVDecHEAACDynamicRangeControl.eAVDecHEAACDynamicRangeControl_ON

        # AVDecAudioDualMono (UINT32) - Read only
        # The input bitstream header might have a field indicating whether the
        # 2 - ch bitstream
        # is dual mono or not. Use this property to read this field.
        # If it's dual mono, the application can set
        # AVDecAudioDualMonoReproMode to determine
        # one of 4 reproduction modes
        CODECAPI_AVDecAudioDualMono = DEFINE_CODECAPI_GUID(
            "4A52CDA8-30F8-4216-BE0F-BA0B2025921D",
            0x4A52CDA8,
            0x30F8,
            0x4216,
            0xBE,
            0x0F,
            0xBA,
            0x0B,
            0x20,
            0x25,
            0x92,
            0x1D
        )


        class eAVDecAudioDualMono(ENUM):
            eAVDecAudioDualMono_IsNotDualMono = 0
            eAVDecAudioDualMono_IsDualMono = 1
            eAVDecAudioDualMono_UnSpecified = 2


        eAVDecAudioDualMono_IsNotDualMono = eAVDecAudioDualMono.eAVDecAudioDualMono_IsNotDualMono
        eAVDecAudioDualMono_IsDualMono = eAVDecAudioDualMono.eAVDecAudioDualMono_IsDualMono
        eAVDecAudioDualMono_UnSpecified = eAVDecAudioDualMono.eAVDecAudioDualMono_UnSpecified

        # AVDecAudioDualMonoReproMode (UINT32)
        # Reproduction modes for programs containing two independent mono
        # channels (Ch1 & Ch2).
        # In case of 2 - ch input, the decoder should get AVDecAudioDualMono
        # to check if the input
        # is regular stereo or dual mono. If dual mono, the application can
        # ask the user to set the playback
        # mode by setting AVDecAudioDualReproMonoMode. If output is not
        # stereo, use AVDecDDMatrixDecodingMode or
        # equivalent.
        CODECAPI_AVDecAudioDualMonoReproMode = DEFINE_CODECAPI_GUID(
            "A5106186-CC94-4BC9-8CD9-AA2F61F6807E",
            0xA5106186,
            0xCC94,
            0x4BC9,
            0x8C,
            0xD9,
            0xAA,
            0x2F,
            0x61,
            0xF6,
            0x80,
            0x7E
        )


        class eAVDecAudioDualMonoReproMode(ENUM):

            # Ch1 + Ch2 for mono output, (Ch1 left,  Ch2 right) for stereo
            # output
            eAVDecAudioDualMonoReproMode_STEREO = 0
            eAVDecAudioDualMonoReproMode_LEFT_MONO = 1
            eAVDecAudioDualMonoReproMode_RIGHT_MONO = 2

            # Ch1 + Ch2 for mono output, (Ch1 + Ch2 left, Ch1 + Ch2 right) for
            # stereo output
            eAVDecAudioDualMonoReproMode_MIX_MONO = 3


        eAVDecAudioDualMonoReproMode_STEREO = eAVDecAudioDualMonoReproMode.eAVDecAudioDualMonoReproMode_STEREO
        eAVDecAudioDualMonoReproMode_LEFT_MONO = eAVDecAudioDualMonoReproMode.eAVDecAudioDualMonoReproMode_LEFT_MONO
        eAVDecAudioDualMonoReproMode_RIGHT_MONO = eAVDecAudioDualMonoReproMode.eAVDecAudioDualMonoReproMode_RIGHT_MONO
        eAVDecAudioDualMonoReproMode_MIX_MONO = eAVDecAudioDualMonoReproMode.eAVDecAudioDualMonoReproMode_MIX_MONO

        # Audio Common Properties
        # AVAudioChannelCount (UINT32)
        # Total number of audio channels, including LFE if it exists.
        CODECAPI_AVAudioChannelCount = DEFINE_CODECAPI_GUID(
            "1D3583C4-1583-474E-B71A-5EE463C198E4",
            0x1D3583C4,
            0x1583,
            0x474E,
            0xB7,
            0x1A,
            0x5E,
            0xE4,
            0x63,
            0xC1,
            0x98,
            0xE4
        )

        # AVAudioChannelConfig (UINT32)
        # A bit - wise OR of any number of enum values specified by
        # eAVAudioChannelConfig
        CODECAPI_AVAudioChannelConfig = DEFINE_CODECAPI_GUID(
            "17F89CB3-C38D-4368-9EDE-63B94D177F9F",
            0x17F89CB3,
            0xC38D,
            0x4368,
            0x9E,
            0xDE,
            0x63,
            0xB9,
            0x4D,
            0x17,
            0x7F,
            0x9F
        )

        # Enumerated values for AVAudioChannelConfig are identical
        # to the speaker positions defined in ksmedia.h and used
        # in WAVE_FORMAT_EXTENSIBLE. Configurations for 5.1 and
        # 7.1 channels should be identical to KSAUDIO_SPEAKER_5POINT1_SURROUND
        # and KSAUDIO_SPEAKER_7POINT1_SURROUND in ksmedia.h. This means:
        # 5.1 ch - > LOW_FREQUENCY | FRONT_LEFT | FRONT_RIGHT | FRONT_CENTER |
        # SIDE_LEFT | SIDE_RIGHT
        # 7.1 ch - > LOW_FREQUENCY | FRONT_LEFT | FRONT_RIGHT | FRONT_CENTER |
        # SIDE_LEFT | SIDE_RIGHT | BACK_LEFT | BACK_RIGHT
        class eAVAudioChannelConfig(ENUM):
            eAVAudioChannelConfig_FRONT_LEFT = 0x1
            eAVAudioChannelConfig_FRONT_RIGHT = 0x2
            eAVAudioChannelConfig_FRONT_CENTER = 0x4
            eAVAudioChannelConfig_LOW_FREQUENCY = 0x8
            eAVAudioChannelConfig_BACK_LEFT = 0x10
            eAVAudioChannelConfig_BACK_RIGHT = 0x20
            eAVAudioChannelConfig_FRONT_LEFT_OF_CENTER = 0x40
            eAVAudioChannelConfig_FRONT_RIGHT_OF_CENTER = 0x80
            eAVAudioChannelConfig_BACK_CENTER = 0x100
            eAVAudioChannelConfig_SIDE_LEFT = 0x200
            eAVAudioChannelConfig_SIDE_RIGHT = 0x400
            eAVAudioChannelConfig_TOP_CENTER = 0x800
            eAVAudioChannelConfig_TOP_FRONT_LEFT = 0x1000
            eAVAudioChannelConfig_TOP_FRONT_CENTER = 0x2000
            eAVAudioChannelConfig_TOP_FRONT_RIGHT = 0x4000
            eAVAudioChannelConfig_TOP_BACK_LEFT = 0x8000
            eAVAudioChannelConfig_TOP_BACK_CENTER = 0x10000
            eAVAudioChannelConfig_TOP_BACK_RIGHT = 0x20000


        eAVAudioChannelConfig_FRONT_LEFT = eAVAudioChannelConfig.eAVAudioChannelConfig_FRONT_LEFT
        eAVAudioChannelConfig_FRONT_RIGHT = eAVAudioChannelConfig.eAVAudioChannelConfig_FRONT_RIGHT
        eAVAudioChannelConfig_FRONT_CENTER = eAVAudioChannelConfig.eAVAudioChannelConfig_FRONT_CENTER
        eAVAudioChannelConfig_LOW_FREQUENCY = eAVAudioChannelConfig.eAVAudioChannelConfig_LOW_FREQUENCY
        eAVAudioChannelConfig_BACK_LEFT = eAVAudioChannelConfig.eAVAudioChannelConfig_BACK_LEFT
        eAVAudioChannelConfig_BACK_RIGHT = eAVAudioChannelConfig.eAVAudioChannelConfig_BACK_RIGHT
        eAVAudioChannelConfig_FRONT_LEFT_OF_CENTER = eAVAudioChannelConfig.eAVAudioChannelConfig_FRONT_LEFT_OF_CENTER
        eAVAudioChannelConfig_FRONT_RIGHT_OF_CENTER = eAVAudioChannelConfig.eAVAudioChannelConfig_FRONT_RIGHT_OF_CENTER
        eAVAudioChannelConfig_BACK_CENTER = eAVAudioChannelConfig.eAVAudioChannelConfig_BACK_CENTER
        eAVAudioChannelConfig_SIDE_LEFT = eAVAudioChannelConfig.eAVAudioChannelConfig_SIDE_LEFT
        eAVAudioChannelConfig_SIDE_RIGHT = eAVAudioChannelConfig.eAVAudioChannelConfig_SIDE_RIGHT
        eAVAudioChannelConfig_TOP_CENTER = eAVAudioChannelConfig.eAVAudioChannelConfig_TOP_CENTER
        eAVAudioChannelConfig_TOP_FRONT_LEFT = eAVAudioChannelConfig.eAVAudioChannelConfig_TOP_FRONT_LEFT
        eAVAudioChannelConfig_TOP_FRONT_CENTER = eAVAudioChannelConfig.eAVAudioChannelConfig_TOP_FRONT_CENTER
        eAVAudioChannelConfig_TOP_FRONT_RIGHT = eAVAudioChannelConfig.eAVAudioChannelConfig_TOP_FRONT_RIGHT
        eAVAudioChannelConfig_TOP_BACK_LEFT = eAVAudioChannelConfig.eAVAudioChannelConfig_TOP_BACK_LEFT
        eAVAudioChannelConfig_TOP_BACK_CENTER = eAVAudioChannelConfig.eAVAudioChannelConfig_TOP_BACK_CENTER
        eAVAudioChannelConfig_TOP_BACK_RIGHT = eAVAudioChannelConfig.eAVAudioChannelConfig_TOP_BACK_RIGHT

        # AVAudioSampleRate (UINT32)
        # In samples per second (Hz)
        CODECAPI_AVAudioSampleRate = DEFINE_CODECAPI_GUID(
            "971D2723-1ACB-42E7-855C-520A4B70A5F2",
            0x971D2723,
            0x1ACB,
            0x42E7,
            0x85,
            0x5C,
            0x52,
            0x0A,
            0x4B,
            0x70,
            0xA5,
            0xF2
        )

        # Dolby Digital(TM) Audio Specific Parameters
        # AVDDSurroundMode (UINT32) common to encoder/decoder
        CODECAPI_AVDDSurroundMode = DEFINE_CODECAPI_GUID(
            "99F2F386-98D1-4452-A163-ABC78A6EB770",
            0x99F2F386,
            0x98D1,
            0x4452,
            0xA1,
            0x63,
            0xAB,
            0xC7,
            0x8A,
            0x6E,
            0xB7,
            0x70
        )


        class eAVDDSurroundMode(ENUM):
            eAVDDSurroundMode_NotIndicated = 0
            eAVDDSurroundMode_No = 1
            eAVDDSurroundMode_Yes = 2


        eAVDDSurroundMode_NotIndicated = eAVDDSurroundMode.eAVDDSurroundMode_NotIndicated
        eAVDDSurroundMode_No = eAVDDSurroundMode.eAVDDSurroundMode_No
        eAVDDSurroundMode_Yes = eAVDDSurroundMode.eAVDDSurroundMode_Yes

        # AVDecDDOperationalMode (UINT32)
        CODECAPI_AVDecDDOperationalMode = DEFINE_CODECAPI_GUID(
            "D6D6C6D1-064E-4FDD-A40E-3ECBFCB7EBD0",
            0xD6D6C6D1,
            0x064E,
            0x4FDD,
            0xA4,
            0x0E,
            0x3E,
            0xCB,
            0xFC,
            0xB7,
            0xEB,
            0xD0
        )


        class eAVDecDDOperationalMode(ENUM):
            eAVDecDDOperationalMode_NONE = 0

            # Dialnorm enabled, dialogue at - 31dBFS, dynrng used, high/low
            # scaling allowed
            eAVDecDDOperationalMode_LINE = 1

            # Dialnorm enabled, dialogue at - 20dBFS, dynrng & compr used,
            # high/low scaling NOT allowed (always fully compressed)
            eAVDecDDOperationalMode_RF = 2
            eAVDecDDOperationalMode_CUSTOM0 = 3
            eAVDecDDOperationalMode_CUSTOM1 = 4

            # Dialnorm enabled, dialogue at - 8dBFS, dynrng & compr used,
            # high/low scaling NOT allowed (always fully compressed)
            eAVDecDDOperationalMode_PORTABLE8 = 5

            # Dialnorm enabled, dialogue at - 11dBFS, dynrng & compr used,
            # high/low scaling NOT allowed (always fully compressed)
            eAVDecDDOperationalMode_PORTABLE11 = 6

            # Dialnorm enabled, dialogue at - 14dBFS, dynrng & compr used,
            # high/low scaling NOT allowed (always fully compressed)
            eAVDecDDOperationalMode_PORTABLE14 = 7


        eAVDecDDOperationalMode_NONE = eAVDecDDOperationalMode.eAVDecDDOperationalMode_NONE
        eAVDecDDOperationalMode_LINE = eAVDecDDOperationalMode.eAVDecDDOperationalMode_LINE
        eAVDecDDOperationalMode_RF = eAVDecDDOperationalMode.eAVDecDDOperationalMode_RF
        eAVDecDDOperationalMode_CUSTOM0 = eAVDecDDOperationalMode.eAVDecDDOperationalMode_CUSTOM0
        eAVDecDDOperationalMode_CUSTOM1 = eAVDecDDOperationalMode.eAVDecDDOperationalMode_CUSTOM1
        eAVDecDDOperationalMode_PORTABLE8 = eAVDecDDOperationalMode.eAVDecDDOperationalMode_PORTABLE8
        eAVDecDDOperationalMode_PORTABLE11 = eAVDecDDOperationalMode.eAVDecDDOperationalMode_PORTABLE11
        eAVDecDDOperationalMode_PORTABLE14 = eAVDecDDOperationalMode.eAVDecDDOperationalMode_PORTABLE14

        # AVDecDDMatrixDecodingMode(UINT32)
        # A ProLogic decoder has a built - in auto - detection feature. When
        # the Dolby Digital decoder
        # is set to the 6 - channel output configuration and it is fed a 2/0
        # bit stream to decode, it can
        # do one of the following:
        # a) decode the bit stream and output it on the two front channels (eAVDecDDMatrixDecodingMode_OFF),
        #
        # b) decode the bit stream followed by ProLogic decoding to create 6 - channels (eAVDecDDMatrixDecodingMode_ON).
        #
        # c) the decoder will look at the Surround bit ("dsurmod") in the bit stream to determine whether
        #
        # apply ProLogic decoding or not (eAVDecDDMatrixDecodingMode_AUTO).
        CODECAPI_AVDecDDMatrixDecodingMode = DEFINE_CODECAPI_GUID(
            "DDC811A5-04ED-4BF3-A0CA-D00449F9355F",
            0xDDC811A5,
            0x04ED,
            0x4BF3,
            0xA0,
            0xCA,
            0xD0,
            0x04,
            0x49,
            0xF9,
            0x35,
            0x5F
        )


        class eAVDecDDMatrixDecodingMode(ENUM):
            eAVDecDDMatrixDecodingMode_OFF = 0
            eAVDecDDMatrixDecodingMode_ON = 1
            eAVDecDDMatrixDecodingMode_AUTO = 2


        eAVDecDDMatrixDecodingMode_OFF = eAVDecDDMatrixDecodingMode.eAVDecDDMatrixDecodingMode_OFF
        eAVDecDDMatrixDecodingMode_ON = eAVDecDDMatrixDecodingMode.eAVDecDDMatrixDecodingMode_ON
        eAVDecDDMatrixDecodingMode_AUTO = eAVDecDDMatrixDecodingMode.eAVDecDDMatrixDecodingMode_AUTO

        # AVDecDDDynamicRangeScaleHigh (UINT32)
        # Indicates what fraction of the dynamic range compression
        # to apply. Relevant for negative values of dynrng only.
        # Linear range 0 - 100, where:
        # 0 - No dynamic range compression (preserve full dynamic range)
        # 100 - Apply full dynamic range compression
        CODECAPI_AVDecDDDynamicRangeScaleHigh = DEFINE_CODECAPI_GUID(
            "50196C21-1F33-4AF5-B296-11426D6C8789",
            0x50196C21,
            0x1F33,
            0x4AF5,
            0xB2,
            0x96,
            0x11,
            0x42,
            0x6D,
            0x6C,
            0x87,
            0x89
        )

        # AVDecDDDynamicRangeScaleLow (UINT32)
        # Indicates what fraction of the dynamic range compression
        # to apply. Relevant for positive values of dynrng only.
        # Linear range 0 - 100, where:
        # 0 - No dynamic range compression (preserve full dynamic range)
        # 100 - Apply full dynamic range compression
        CODECAPI_AVDecDDDynamicRangeScaleLow = DEFINE_CODECAPI_GUID(
            "044E62E4-11A5-42D5-A3B2-3BB2C7C2D7CF",
            0x044E62E4,
            0x11A5,
            0x42D5,
            0xA3,
            0xB2,
            0x3B,
            0xB2,
            0xC7,
            0xC2,
            0xD7,
            0xCF
        )

        # AVDecDDStereoDownMixMode (UINT32)
        # A Dolby Digital Decoder may apply stereo downmix in one of several
        # ways, after decoding multichannel PCM.
        # Use one of the UINT32 values specified by eAVDecDDStereoDownMixMode
        # to set stereo downmix mode.
        # Only relevant when the decoder's output is set to stereo.
        CODECAPI_AVDecDDStereoDownMixMode = DEFINE_CODECAPI_GUID(
            "6CE4122C-3EE9-4182-B4AE-C10FC088649D",
            0x6CE4122C,
            0x3EE9,
            0x4182,
            0xB4,
            0xAE,
            0xC1,
            0x0F,
            0xC0,
            0x88,
            0x64,
            0x9D
        )


        class eAVDecDDStereoDownMixMode(ENUM):
            eAVDecDDStereoDownMixMode_Auto = 0
            eAVDecDDStereoDownMixMode_LtRt = 1
            eAVDecDDStereoDownMixMode_LoRo = 2


        eAVDecDDStereoDownMixMode_Auto = eAVDecDDStereoDownMixMode.eAVDecDDStereoDownMixMode_Auto
        eAVDecDDStereoDownMixMode_LtRt = eAVDecDDStereoDownMixMode.eAVDecDDStereoDownMixMode_LtRt
        eAVDecDDStereoDownMixMode_LoRo = eAVDecDDStereoDownMixMode.eAVDecDDStereoDownMixMode_LoRo

        # AVDSPLoudnessEqualization (UINT32)
        # Related to audio digital signal processing (DSP).
        # Apply "Loudness Equalization" to the audio stream, so users will not
        # have to adjust volume control when audio stream changes.
        CODECAPI_AVDSPLoudnessEqualization = DEFINE_CODECAPI_GUID(
            "8AFD1A15-1812-4CBF-9319-433A5B2A3B27",
            0x8AFD1A15,
            0x1812,
            0x4CBF,
            0x93,
            0x19,
            0x43,
            0x3A,
            0x5B,
            0x2A,
            0x3B,
            0x27
        )


        class eAVDSPLoudnessEqualization(ENUM):
            eAVDSPLoudnessEqualization_OFF = 0
            eAVDSPLoudnessEqualization_ON = 1
            eAVDSPLoudnessEqualization_AUTO = 2


        eAVDSPLoudnessEqualization_OFF = eAVDSPLoudnessEqualization.eAVDSPLoudnessEqualization_OFF
        eAVDSPLoudnessEqualization_ON = eAVDSPLoudnessEqualization.eAVDSPLoudnessEqualization_ON
        eAVDSPLoudnessEqualization_AUTO = eAVDSPLoudnessEqualization.eAVDSPLoudnessEqualization_AUTO

        # AVDSPSpeakerFill (UINT32)
        # Related to audio digital signal processing (DSP).
        # "Speaker Fill" will take a mono or stereo audio stream and convert
        # it to a multi channel (e.g. 5.1) audio stream.
        CODECAPI_AVDSPSpeakerFill = DEFINE_CODECAPI_GUID(
            "5612BCA1-56DA-4582-8DA1-CA8090F92768",
            0x5612BCA1,
            0x56DA,
            0x4582,
            0x8D,
            0xA1,
            0xCA,
            0x80,
            0x90,
            0xF9,
            0x27,
            0x68
        )


        class eAVDSPSpeakerFill(ENUM):
            eAVDSPSpeakerFill_OFF = 0
            eAVDSPSpeakerFill_ON = 1
            eAVDSPSpeakerFill_AUTO = 2


        eAVDSPSpeakerFill_OFF = eAVDSPSpeakerFill.eAVDSPSpeakerFill_OFF
        eAVDSPSpeakerFill_ON = eAVDSPSpeakerFill.eAVDSPSpeakerFill_ON
        eAVDSPSpeakerFill_AUTO = eAVDSPSpeakerFill.eAVDSPSpeakerFill_AUTO

        # AVPriorityControl (UINT32)
        # Indicates the task priority when not realtime (0..15)
        # Linear range 0 - 15, where:
        # 0 - idle
        # 15 - Highest
        CODECAPI_AVPriorityControl = DEFINE_CODECAPI_GUID(
            "54BA3DC8-BDDE-4329-B187-2018BC5C2BA1",
            0x54BA3DC8,
            0xBDDE,
            0x4329,
            0xB1,
            0x87,
            0x20,
            0x18,
            0xBC,
            0x5C,
            0x2B,
            0xA1
        )

        # AVRealtimeControl (UINT32)
        # Indicates the task is realtime or not
        # Linear range 0 - 1, where:
        # 0 - no realtime
        # 1 - realtime
        CODECAPI_AVRealtimeControl = DEFINE_CODECAPI_GUID(
            "6F440632-C4AD-4BF7-9E52-456942B454B0",
            0x6F440632,
            0xC4AD,
            0x4BF7,
            0x9E,
            0x52,
            0x45,
            0x69,
            0x42,
            0xB4,
            0x54,
            0xB0
        )

        # AVEncNoInputCopy (UINT32)
        # Enables the encoder to aVOID copying the input buffer
        # 0 - default behavior (copy input buffer to encoder internal buffer)
        # 1 - use input buffer directly
        # Input color space must be IYUV or YV12 for this to be effective.
        # Input buffers must be fully contiguous. Input buffers
        # must be macroblock - aligned (width and height divisible by 16).
        CODECAPI_AVEncNoInputCopy = DEFINE_CODECAPI_GUID(
            "D2B46A2A-E8EE-4EC5-869E-449B6C62C81A",
            0xD2B46A2A,
            0xE8EE,
            0x4EC5,
            0x86,
            0x9E,
            0x44,
            0x9B,
            0x6C,
            0x62,
            0xC8,
            0x1A
        )

        # AVEncChromaEncodeMode (UINT32)
        # Change the mode used to encode chroma - only frames
        # A member of the eAVChromaEncodeMode structure, where:
        # eAVChromaEncodeMode_420 - default encoding
        # eAVChromaEncodeMode_444 - enhanced encoding of chroma for repeated
        # input frames
        # eAVChromaEncodeMode_444_v2 - encoder will skip non - chroma
        # macroblocks, in addition to functionality for eAVChromaEncodeMode_444
        class eAVEncChromaEncodeMode(ENUM):
            eAVEncChromaEncodeMode_420 = 1
            eAVEncChromaEncodeMode_444 = 2
            eAVEncChromaEncodeMode_444_v2 = 3


        eAVEncChromaEncodeMode_420 = eAVEncChromaEncodeMode.eAVEncChromaEncodeMode_420
        eAVEncChromaEncodeMode_444 = eAVEncChromaEncodeMode.eAVEncChromaEncodeMode_444
        eAVEncChromaEncodeMode_444_v2 = eAVEncChromaEncodeMode.eAVEncChromaEncodeMode_444_v2
        CODECAPI_AVEncChromaEncodeMode = DEFINE_CODECAPI_GUID(
            "8A47AB5A-4798-4C93-B5A5-554F9A3B9F50",
            0x8A47AB5A,
            0x4798,
            0x4C93,
            0xB5,
            0xA5,
            0x55,
            0x4F,
            0x9A,
            0x3B,
            0x9F,
            0x50
        )
        if not defined(UUID_GEN):
            # { GUID refs
            CODECAPI_AVEncCommonFormatConstraint = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonFormatConstraint)
            )
            CODECAPI_GUID_AVEncCommonFormatUnSpecified = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatUnSpecified)
            )
            CODECAPI_GUID_AVEncCommonFormatDVD_V = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatDVD_V)
            )
            CODECAPI_GUID_AVEncCommonFormatDVD_DashVR = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatDVD_DashVR)
            )
            CODECAPI_GUID_AVEncCommonFormatDVD_PlusVR = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatDVD_PlusVR)
            )
            CODECAPI_GUID_AVEncCommonFormatVCD = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatVCD)
            )
            CODECAPI_GUID_AVEncCommonFormatSVCD = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatSVCD)
            )
            CODECAPI_GUID_AVEncCommonFormatATSC = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatATSC)
            )
            CODECAPI_GUID_AVEncCommonFormatDVB = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatDVB)
            )
            CODECAPI_GUID_AVEncCommonFormatMP3 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatMP3)
            )
            CODECAPI_GUID_AVEncCommonFormatHighMAT = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatHighMAT)
            )
            CODECAPI_GUID_AVEncCommonFormatHighMPV = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncCommonFormatHighMPV)
            )
            CODECAPI_AVEncCodecType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCodecType)
            )
            CODECAPI_GUID_AVEncMPEG1Video = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncMPEG1Video)
            )
            CODECAPI_GUID_AVEncMPEG2Video = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncMPEG2Video)
            )
            CODECAPI_GUID_AVEncMPEG1Audio = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncMPEG1Audio)
            )
            CODECAPI_GUID_AVEncMPEG2Audio = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncMPEG2Audio)
            )
            CODECAPI_GUID_AVEncWMV = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncWMV)
            CODECAPI_GUID_AVEndMPEG4Video = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEndMPEG4Video)
            )
            CODECAPI_GUID_AVEncH264Video = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncH264Video)
            )
            CODECAPI_GUID_AVEncDV = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncDV)
            CODECAPI_GUID_AVEncWMAPro = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncWMAPro)
            )
            CODECAPI_GUID_AVEncWMALossless = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncWMALossless)
            )
            CODECAPI_GUID_AVEncWMAVoice = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncWMAVoice)
            )
            CODECAPI_GUID_AVEncDolbyDigitalPro = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncDolbyDigitalPro)
            )
            CODECAPI_GUID_AVEncDolbyDigitalConsumer = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncDolbyDigitalConsumer)
            )
            CODECAPI_GUID_AVEncDolbyDigitalPlus = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncDolbyDigitalPlus)
            )
            CODECAPI_GUID_AVEncDTSHD = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncDTSHD)
            )
            CODECAPI_GUID_AVEncDTS = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncDTS)
            CODECAPI_GUID_AVEncMLP = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncMLP)
            CODECAPI_GUID_AVEncPCM = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncPCM)
            CODECAPI_GUID_AVEncSDDS = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVEncSDDS)
            )
            CODECAPI_AVEncCommonRateControlMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonRateControlMode)
            )
            CODECAPI_AVEncCommonLowLatency = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonLowLatency)
            )
            CODECAPI_AVEncCommonMultipassMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonMultipassMode)
            )
            CODECAPI_AVEncCommonPassStart = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonPassStart)
            )
            CODECAPI_AVEncCommonPassEnd = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonPassEnd)
            )
            CODECAPI_AVEncCommonRealTime = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonRealTime)
            )
            CODECAPI_AVEncCommonQuality = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonQuality)
            )
            CODECAPI_AVEncCommonQualityVsSpeed = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonQualityVsSpeed)
            )
            CODECAPI_AVEncCommonTranscodeEncodingProfile = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonTranscodeEncodingProfile)
            )
            CODECAPI_AVEncCommonMeanBitRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonMeanBitRate)
            )
            CODECAPI_AVEncCommonMeanBitRateInterval = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonMeanBitRateInterval)
            )
            CODECAPI_AVEncCommonMaxBitRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonMaxBitRate)
            )
            CODECAPI_AVEncCommonMinBitRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonMinBitRate)
            )
            CODECAPI_AVEncCommonBufferSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonBufferSize)
            )
            CODECAPI_AVEncCommonBufferInLevel = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonBufferInLevel)
            )
            CODECAPI_AVEncCommonBufferOutLevel = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonBufferOutLevel)
            )
            CODECAPI_AVEncCommonStreamEndHandling = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonStreamEndHandling)
            )
            CODECAPI_AVEncStatCommonCompletedPasses = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatCommonCompletedPasses)
            )
            CODECAPI_AVEncVideoOutputFrameRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputFrameRate)
            )
            CODECAPI_AVEncVideoOutputFrameRateConversion = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputFrameRateConversion)
            )
            CODECAPI_AVEncVideoPixelAspectRatio = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoPixelAspectRatio)
            )
            CODECAPI_AVDecVideoAcceleration_MPEG2 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoAcceleration_MPEG2)
            )
            CODECAPI_AVDecVideoAcceleration_H264 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoAcceleration_H264)
            )
            CODECAPI_AVDecVideoAcceleration_VC1 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoAcceleration_VC1)
            )
            CODECAPI_AVDecVideoProcDeinterlaceCSC = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoProcDeinterlaceCSC)
            )
            CODECAPI_AVEncVideoForceSourceScanType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoForceSourceScanType)
            )
            CODECAPI_AVEncVideoNoOfFieldsToEncode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoNoOfFieldsToEncode)
            )
            CODECAPI_AVEncVideoNoOfFieldsToSkip = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoNoOfFieldsToSkip)
            )
            CODECAPI_AVEncVideoEncodeDimension = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoEncodeDimension)
            )
            CODECAPI_AVEncVideoEncodeOffsetOrigin = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoEncodeOffsetOrigin)
            )
            CODECAPI_AVEncVideoDisplayDimension = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoDisplayDimension)
            )
            CODECAPI_AVEncVideoOutputScanType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputScanType)
            )
            CODECAPI_AVEncVideoInverseTelecineEnable = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInverseTelecineEnable)
            )
            CODECAPI_AVEncVideoInverseTelecineThreshold = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInverseTelecineThreshold)
            )
            CODECAPI_AVEncVideoSourceFilmContent = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoSourceFilmContent)
            )
            CODECAPI_AVEncVideoSourceIsBW = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoSourceIsBW)
            )
            CODECAPI_AVEncVideoFieldSwap = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoFieldSwap)
            )
            CODECAPI_AVEncVideoInputChromaResolution = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInputChromaResolution)
            )
            CODECAPI_AVEncVideoOutputChromaResolution = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputChromaResolution)
            )
            CODECAPI_AVEncVideoInputChromaSubsampling = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInputChromaSubsampling)
            )
            CODECAPI_AVEncVideoOutputChromaSubsampling = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputChromaSubsampling)
            )
            CODECAPI_AVEncVideoInputColorPrimaries = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInputColorPrimaries)
            )
            CODECAPI_AVEncVideoOutputColorPrimaries = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputColorPrimaries)
            )
            CODECAPI_AVEncVideoInputColorTransferFunction = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInputColorTransferFunction)
            )
            CODECAPI_AVEncVideoOutputColorTransferFunction = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputColorTransferFunction)
            )
            CODECAPI_AVEncVideoInputColorTransferMatrix = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInputColorTransferMatrix)
            )
            CODECAPI_AVEncVideoOutputColorTransferMatrix = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputColorTransferMatrix )
            )
            CODECAPI_AVEncVideoInputColorLighting = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInputColorLighting)
            )
            CODECAPI_AVEncVideoOutputColorLighting = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputColorLighting )
            )
            CODECAPI_AVEncVideoInputColorNominalRange = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInputColorNominalRange)
            )
            CODECAPI_AVEncVideoOutputColorNominalRange = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoOutputColorNominalRange )
            )
            CODECAPI_AVEncInputVideoSystem = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncInputVideoSystem)
            )
            CODECAPI_AVEncVideoHeaderDropFrame = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoHeaderDropFrame)
            )
            CODECAPI_AVEncVideoHeaderHours = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoHeaderHours)
            )
            CODECAPI_AVEncVideoHeaderMinutes = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoHeaderMinutes)
            )
            CODECAPI_AVEncVideoHeaderSeconds = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoHeaderSeconds)
            )
            CODECAPI_AVEncVideoHeaderFrames = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoHeaderFrames)
            )
            CODECAPI_AVEncVideoDefaultUpperFieldDominant = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoDefaultUpperFieldDominant)
            )
            CODECAPI_AVEncVideoCBRMotionTradeoff = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoCBRMotionTradeoff)
            )
            CODECAPI_AVEncVideoCodedVideoAccessUnitSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoCodedVideoAccessUnitSize)
            )
            CODECAPI_AVEncVideoMaxKeyframeDistance = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMaxKeyframeDistance)
            )
            CODECAPI_AVEncH264CABACEnable = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncH264CABACEnable)
            )
            CODECAPI_AVEncVideoContentType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoContentType)
            )
            CODECAPI_AVEncNumWorkerThreads = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncNumWorkerThreads)
            )
            CODECAPI_AVEncVideoEncodeQP = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoEncodeQP)
            )
            CODECAPI_AVEncVideoMinQP = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMinQP)
            )
            CODECAPI_AVEncVideoForceKeyFrame = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoForceKeyFrame)
            )
            CODECAPI_AVEncH264SPSID = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncH264SPSID)
            )
            CODECAPI_AVEncH264PPSID = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncH264PPSID)
            )
            CODECAPI_AVEncAdaptiveMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAdaptiveMode)
            )
            CODECAPI_AVEncVideoSelectLayer = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoSelectLayer)
            )
            CODECAPI_AVEncVideoTemporalLayerCount = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoTemporalLayerCount)
            )
            CODECAPI_AVEncVideoUsage = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoUsage)
            )
            CODECAPI_AVEncVideoRateControlParams = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoRateControlParams)
            )
            CODECAPI_AVEncVideoSupportedControls = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoSupportedControls)
            )
            CODECAPI_AVEncVideoEncodeFrameTypeQP = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoEncodeFrameTypeQP)
            )
            CODECAPI_AVEncSliceControlMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncSliceControlMode)
            )
            CODECAPI_AVEncSliceControlSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncSliceControlSize)
            )
            CODECAPI_AVEncSliceGenerationMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncSliceGenerationMode)
            )
            CODECAPI_AVEncVideoMaxNumRefFrame = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMaxNumRefFrame)
            )
            CODECAPI_AVEncVideoMeanAbsoluteDifference = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMeanAbsoluteDifference)
            )
            CODECAPI_AVEncVideoMaxQP = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMaxQP)
            )
            CODECAPI_AVEncVideoLTRBufferControl = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoLTRBufferControl)
            )
            CODECAPI_AVEncVideoMarkLTRFrame = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMarkLTRFrame)
            )
            CODECAPI_AVEncVideoUseLTRFrame = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoUseLTRFrame)
            )
            CODECAPI_AVEncVideoROIEnabled = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoROIEnabled)
            )
            CODECAPI_AVEncVideoDirtyRectEnabled = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoDirtyRectEnabled)
            )
            CODECAPI_AVScenarioInfo = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVScenarioInfo)
            )
            CODECAPI_AVEncMPVGOPSizeMin = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGOPSizeMin)
            )
            CODECAPI_AVEncMPVGOPSizeMax = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGOPSizeMax)
            )
            CODECAPI_AVEncVideoMaxCTBSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMaxCTBSize)
            )
            CODECAPI_AVEncVideoCTBSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoCTBSize)
            )
            CODECAPI_VideoEncoderDisplayContentType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_VideoEncoderDisplayContentType)
            )
            CODECAPI_AVEncEnableVideoProcessing = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncEnableVideoProcessing)
            )
            CODECAPI_AVEncVideoGradualIntraRefresh = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoGradualIntraRefresh)
            )
            CODECAPI_GetOPMContext = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GetOPMContext)
            CODECAPI_SetHDCPManagerContext = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_SetHDCPManagerContext)
            )
            CODECAPI_AVEncVideoMaxTemporalLayers = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoMaxTemporalLayers)
            )
            CODECAPI_AVEncVideoNumGOPsPerIDR = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoNumGOPsPerIDR)
            )
            CODECAPI_AVEncCommonAllowFrameDrops = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncCommonAllowFrameDrops)
            )
            CODECAPI_AVEncVideoIntraLayerPrediction = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoIntraLayerPrediction)
            )
            CODECAPI_AVEncVideoInstantTemporalUpSwitching = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncVideoInstantTemporalUpSwitching)
            )
            CODECAPI_AVEncLowPowerEncoder = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncLowPowerEncoder)
            )
            CODECAPI_AVEnableInLoopDeblockFilter = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEnableInLoopDeblockFilter)
            )
            CODECAPI_AVEncMuxOutputStreamType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMuxOutputStreamType)
            )
            CODECAPI_AVEncStatVideoOutputFrameRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatVideoOutputFrameRate)
            )
            CODECAPI_AVEncStatVideoCodedFrames = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatVideoCodedFrames)
            )
            CODECAPI_AVEncStatVideoTotalFrames = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatVideoTotalFrames)
            )
            CODECAPI_AVEncAudioIntervalToEncode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioIntervalToEncode)
            )
            CODECAPI_AVEncAudioIntervalToSkip = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioIntervalToSkip)
            )
            CODECAPI_AVEncAudioDualMono = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioDualMono)
            )
            CODECAPI_AVEncAudioMeanBitRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMeanBitRate)
            )
            CODECAPI_AVEncAudioMapDestChannel0 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel0)
            )
            CODECAPI_AVEncAudioMapDestChannel1 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel1)
            )
            CODECAPI_AVEncAudioMapDestChannel2 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel2)
            )
            CODECAPI_AVEncAudioMapDestChannel3 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel3)
            )
            CODECAPI_AVEncAudioMapDestChannel4 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel4)
            )
            CODECAPI_AVEncAudioMapDestChannel5 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel5)
            )
            CODECAPI_AVEncAudioMapDestChannel6 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel6)
            )
            CODECAPI_AVEncAudioMapDestChannel7 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel7)
            )
            CODECAPI_AVEncAudioMapDestChannel8 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel8)
            )
            CODECAPI_AVEncAudioMapDestChannel9 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel9)
            )
            CODECAPI_AVEncAudioMapDestChannel10 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel10)
            )
            CODECAPI_AVEncAudioMapDestChannel11 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel11)
            )
            CODECAPI_AVEncAudioMapDestChannel12 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel12)
            )
            CODECAPI_AVEncAudioMapDestChannel13 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel13)
            )
            CODECAPI_AVEncAudioMapDestChannel14 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel14)
            )
            CODECAPI_AVEncAudioMapDestChannel15 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioMapDestChannel15)
            )
            CODECAPI_AVEncAudioInputContent = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncAudioInputContent)
            )
            CODECAPI_AVEncStatAudioPeakPCMValue = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatAudioPeakPCMValue)
            )
            CODECAPI_AVEncStatAudioAveragePCMValue = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatAudioAveragePCMValue)
            )
            CODECAPI_AVEncStatAudioAverageBPS = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatAudioAverageBPS)
            )
            CODECAPI_AVEncStatAverageBPS = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatAverageBPS)
            )
            CODECAPI_AVEncStatHardwareProcessorUtilitization = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatHardwareProcessorUtilitization)
            )
            CODECAPI_AVEncStatBandwidthProcessorUtilitization = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatHardwareBandwidthUtilitization)
            )
            CODECAPI_AVEncMPVGOPSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGOPSize)
            )
            CODECAPI_AVEncMPVGOPOpen = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGOPOpen)
            )
            CODECAPI_AVEncMPVDefaultBPictureCount = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVDefaultBPictureCount)
            )
            CODECAPI_AVEncMPVProfile = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVProfile)
            )
            CODECAPI_AVEncMPVLevel = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVLevel)
            CODECAPI_AVEncMPVFrameFieldMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVFrameFieldMode)
            )
            CODECAPI_AVEncMPVAddSeqEndCode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVAddSeqEndCode)
            )
            CODECAPI_AVEncMPVGOPSInSeq = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGOPSInSeq)
            )
            CODECAPI_AVEncMPVUseConcealmentMotionVectors = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVUseConcealmentMotionVectors)
            )
            CODECAPI_AVEncMPVSceneDetection = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVSceneDetection)
            )
            CODECAPI_AVEncMPVGenerateHeaderSeqExt = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGenerateHeaderSeqExt)
            )
            CODECAPI_AVEncMPVGenerateHeaderSeqDispExt = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGenerateHeaderSeqDispExt)
            )
            CODECAPI_AVEncMPVGenerateHeaderPicExt = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGenerateHeaderPicExt)
            )
            CODECAPI_AVEncMPVGenerateHeaderPicDispExt = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGenerateHeaderPicDispExt)
            )
            CODECAPI_AVEncMPVGenerateHeaderSeqScaleExt = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVGenerateHeaderSeqScaleExt)
            )
            CODECAPI_AVEncMPVScanPattern = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVScanPattern)
            )
            CODECAPI_AVEncMPVIntraDCPrecision = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVIntraDCPrecision)
            )
            CODECAPI_AVEncMPVQScaleType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVQScaleType)
            )
            CODECAPI_AVEncMPVIntraVLCTable = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVIntraVLCTable)
            )
            CODECAPI_AVEncMPVQuantMatrixIntra = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVQuantMatrixIntra)
            )
            CODECAPI_AVEncMPVQuantMatrixNonIntra = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVQuantMatrixNonIntra)
            )
            CODECAPI_AVEncMPVQuantMatrixChromaIntra = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVQuantMatrixChromaIntra)
            )
            CODECAPI_AVEncMPVQuantMatrixChromaNonIntra = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPVQuantMatrixChromaNonIntra)
            )
            CODECAPI_AVEncMPALayer = DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPALayer)
            CODECAPI_AVEncMPACodingMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPACodingMode)
            )
            CODECAPI_AVEncDDService = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDService)
            )
            CODECAPI_AVEncDDDialogNormalization = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDDialogNormalization)
            )
            CODECAPI_AVEncDDCentreDownMixLevel = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDCentreDownMixLevel)
            )
            CODECAPI_AVEncDDSurroundDownMixLevel = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDSurroundDownMixLevel)
            )
            CODECAPI_AVEncDDProductionInfoExists = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDProductionInfoExists)
            )
            CODECAPI_AVEncDDProductionRoomType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDProductionRoomType)
            )
            CODECAPI_AVEncDDProductionMixLevel = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDProductionMixLevel)
            )
            CODECAPI_AVEncDDCopyright = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDCopyright)
            )
            CODECAPI_AVEncDDOriginalBitstream = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDOriginalBitstream)
            )
            CODECAPI_AVEncDDDigitalDeemphasis = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDDigitalDeemphasis)
            )
            CODECAPI_AVEncDDDCHighPassFilter = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDDCHighPassFilter)
            )
            CODECAPI_AVEncDDChannelBWLowPassFilter = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDChannelBWLowPassFilter)
            )
            CODECAPI_AVEncDDLFELowPassFilter = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDLFELowPassFilter)
            )
            CODECAPI_AVEncDDSurround90DegreeePhaseShift = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDSurround90DegreeePhaseShift)
            )
            CODECAPI_AVEncDDSurround3dBAttenuation = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDSurround3dBAttenuation)
            )
            CODECAPI_AVEncDDDynamicRangeCompressionControl = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDDynamicRangeCompressionControl)
            )
            CODECAPI_AVEncDDRFPreEmphasisFilter = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDRFPreEmphasisFilter)
            )
            CODECAPI_AVEncDDSurroundExMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDSurroundExMode)
            )
            CODECAPI_AVEncDDPreferredStereoDownMixMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDPreferredStereoDownMixMode)
            )
            CODECAPI_AVEncDDLtRtCenterMixLvl_x10 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDLtRtCenterMixLvl_x10)
            )
            CODECAPI_AVEncDDLtRtSurroundMixLvl_x10 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDLtRtSurroundMixLvl_x10)
            )
            CODECAPI_AVEncDDLoRoCenterMixLvl_x10 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDLoRoCenterMixLvl_x10)
            )
            CODECAPI_AVEncDDLoRoSurroundMixLvl_x10 = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDLoRoSurroundMixLvl_x10)
            )
            CODECAPI_AVEncDDAtoDConverterType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDAtoDConverterType)
            )
            CODECAPI_AVEncDDHeadphoneMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncDDHeadphoneMode)
            )
            CODECAPI_AVEncWMVKeyFrameDistance = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncWMVKeyFrameDistance)
            )
            CODECAPI_AVEncWMVInterlacedEncoding = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncWMVInterlacedEncoding)
            )
            CODECAPI_AVEncWMVDecoderComplexity = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncWMVDecoderComplexity)
            )
            CODECAPI_AVEncWMVKeyFrameBufferLevelMarker = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncWMVKeyFrameBufferLevelMarker)
            )
            CODECAPI_AVEncWMVProduceDummyFrames = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncWMVProduceDummyFrames)
            )
            CODECAPI_AVEncStatWMVCBAvg = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatWMVCBAvg)
            )
            CODECAPI_AVEncStatWMVCBMax = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatWMVCBMax)
            )
            CODECAPI_AVEncStatWMVDecoderComplexityProfile = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatWMVDecoderComplexityProfile)
            )
            CODECAPI_AVEncStatMPVSkippedEmptyFrames = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncStatMPVSkippedEmptyFrames)
            )
            CODECAPI_AVEncMP12PktzSTDBuffer = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12PktzSTDBuffer)
            )
            CODECAPI_AVEncMP12PktzStreamID = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12PktzStreamID)
            )
            CODECAPI_AVEncMP12PktzInitialPTS = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12PktzInitialPTS)
            )
            CODECAPI_AVEncMP12PktzPacketSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12PktzPacketSize)
            )
            CODECAPI_AVEncMP12PktzCopyright = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12PktzCopyright)
            )
            CODECAPI_AVEncMP12PktzOriginal = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12PktzOriginal)
            )
            CODECAPI_AVEncMP12MuxPacketOverhead = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxPacketOverhead)
            )
            CODECAPI_AVEncMP12MuxNumStreams = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxNumStreams)
            )
            CODECAPI_AVEncMP12MuxEarliestPTS = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxEarliestPTS)
            )
            CODECAPI_AVEncMP12MuxLargestPacketSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxLargestPacketSize)
            )
            CODECAPI_AVEncMP12MuxInitialSCR = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxInitialSCR)
            )
            CODECAPI_AVEncMP12MuxMuxRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxMuxRate)
            )
            CODECAPI_AVEncMP12MuxPackSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxPackSize)
            )
            CODECAPI_AVEncMP12MuxSysSTDBufferBound = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxSysSTDBufferBound)
            )
            CODECAPI_AVEncMP12MuxSysRateBound = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxSysRateBound)
            )
            CODECAPI_AVEncMP12MuxTargetPacketizer = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxTargetPacketizer)
            )
            CODECAPI_AVEncMP12MuxSysFixed = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxSysFixed)
            )
            CODECAPI_AVEncMP12MuxSysCSPS = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxSysCSPS)
            )
            CODECAPI_AVEncMP12MuxSysVideoLock = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxSysVideoLock)
            )
            CODECAPI_AVEncMP12MuxSysAudioLock = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxSysAudioLock)
            )
            CODECAPI_AVEncMP12MuxDVDNavPacks = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMP12MuxDVDNavPacks)
            )
            CODECAPI_AVEncMPACopyright = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPACopyright)
            )
            CODECAPI_AVEncMPAOriginalBitstream = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPAOriginalBitstream)
            )
            CODECAPI_AVEncMPAEnableRedundancyProtection = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPAEnableRedundancyProtection)
            )
            CODECAPI_AVEncMPAPrivateUserBit = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPAPrivateUserBit)
            )
            CODECAPI_AVEncMPAEmphasisType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMPAEmphasisType)
            )
            CODECAPI_AVDecCommonOutputFormat = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecCommonOutputFormat)
            )
            CODECAPI_AVDecCommonInputFormat = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecCommonInputFormat)
            )
            CODECAPI_AVDecCommonMeanBitRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecCommonMeanBitRate)
            )
            CODECAPI_AVDecCommonMeanBitRateInterval = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecCommonMeanBitRateInterval)
            )
            CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_MatrixEncoded = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_MatrixEncoded)
            )
            CODECAPI_GUID_AVDecAudioOutputFormat_PCM = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioOutputFormat_PCM)
            )
            CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_PCM = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_PCM)
            )
            CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_Bitstream = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioOutputFormat_SPDIF_Bitstream)
            )
            CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Headphones = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Headphones)
            )
            CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_Auto = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioOutputFormat_PCM_Stereo_Auto)
            )
            CODECAPI_AVDecVideoImageSize = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoImageSize)
            )
            CODECAPI_AVDecVideoInputScanType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoInputScanType)
            )
            CODECAPI_AVDecVideoPixelAspectRatio = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoPixelAspectRatio)
            )
            CODECAPI_AVDecVideoThumbnailGenerationMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoThumbnailGenerationMode)
            )
            CODECAPI_AVDecVideoDropPicWithMissingRef = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoDropPicWithMissingRef)
            )
            CODECAPI_AVDecVideoSoftwareDeinterlaceMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoSoftwareDeinterlaceMode)
            )
            CODECAPI_AVDecVideoFastDecodeMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoFastDecodeMode)
            )
            CODECAPI_AVLowLatencyMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVLowLatencyMode)
            )
            CODECAPI_AVDecVideoH264ErrorConcealment = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoH264ErrorConcealment)
            )
            CODECAPI_AVDecVideoMPEG2ErrorConcealment = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoMPEG2ErrorConcealment)
            )
            CODECAPI_AVDecVideoCodecType = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoCodecType)
            )
            CODECAPI_AVDecVideoDXVAMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoDXVAMode)
            )
            CODECAPI_AVDecVideoDXVABusEncryption = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoDXVABusEncryption)
            )
            CODECAPI_AVDecVideoSWPowerLevel = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoSWPowerLevel)
            )
            CODECAPI_AVDecVideoMaxCodedWidth = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoMaxCodedWidth)
            )
            CODECAPI_AVDecVideoMaxCodedHeight = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecVideoMaxCodedHeight)
            )
            CODECAPI_AVDecNumWorkerThreads = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecNumWorkerThreads)
            )
            CODECAPI_AVDecSoftwareDynamicFormatChange = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecSoftwareDynamicFormatChange)
            )
            CODECAPI_AVDecDisableVideoPostProcessing = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecDisableVideoPostProcessing)
            )
            CODECAPI_GUID_AVDecAudioInputWMA = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputWMA)
            )
            CODECAPI_GUID_AVDecAudioInputWMAPro = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputWMAPro)
            )
            CODECAPI_GUID_AVDecAudioInputDolby = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputDolby)
            )
            CODECAPI_GUID_AVDecAudioInputDTS = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputDTS)
            )
            CODECAPI_GUID_AVDecAudioInputPCM = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputPCM)
            )
            CODECAPI_GUID_AVDecAudioInputMPEG = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputMPEG)
            )
            CODECAPI_GUID_AVDecAudioInputAAC = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputAAC)
            )
            CODECAPI_GUID_AVDecAudioInputHEAAC = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputHEAAC)
            )
            CODECAPI_GUID_AVDecAudioInputDolbyDigitalPlus = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_GUID_AVDecAudioInputDolbyDigitalPlus)
            )
            CODECAPI_AVDecAACDownmixMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecAACDownmixMode)
            )
            CODECAPI_AVDecHEAACDynamicRangeControl = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecHEAACDynamicRangeControl)
            )
            CODECAPI_AVDecAudioDualMono = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecAudioDualMono)
            )
            CODECAPI_AVDecAudioDualMonoReproMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecAudioDualMonoReproMode)
            )
            CODECAPI_AVAudioChannelCount = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVAudioChannelCount)
            )
            CODECAPI_AVAudioChannelConfig = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVAudioChannelConfig)
            )
            CODECAPI_AVAudioSampleRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVAudioSampleRate)
            )
            CODECAPI_AVDDSurroundMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDDSurroundMode)
            )
            CODECAPI_AVDecDDOperationalMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecDDOperationalMode)
            )
            CODECAPI_AVDecDDMatrixDecodingMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecDDMatrixDecodingMode)
            )
            CODECAPI_AVDecDDDynamicRangeScaleHigh = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecDDDynamicRangeScaleHigh)
            )
            CODECAPI_AVDecDDDynamicRangeScaleLow = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecDDDynamicRangeScaleLow)
            )
            CODECAPI_AVDecDDStereoDownMixMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDecDDStereoDownMixMode)
            )
            CODECAPI_AVDSPLoudnessEqualization = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDSPLoudnessEqualization)
            )
            CODECAPI_AVDSPSpeakerFill = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVDSPSpeakerFill)
            )
            CODECAPI_AVPriorityControl = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVPriorityControl)
            )
            CODECAPI_AVRealtimeControl = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVRealtimeControl)
            )
            CODECAPI_AVEncMaxFrameRate = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncMaxFrameRate)
            )
            CODECAPI_AVEncNoInputCopy = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncNoInputCopy)
            )
            CODECAPI_AVEncChromaEncodeMode = (
                DEFINE_CODECAPI_GUIDNAMED(CODECAPI_AVEncChromaEncodeMode)
            )
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
# END IF   not defined(_CODECAPI_)
