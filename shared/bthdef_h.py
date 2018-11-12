import ctypes

from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

__BTHDEF_H__ = None
NO_BTHSDPDEF_INC = None
VISTA_KB942567 = 1


# + + Copyright (c) 2000 Microsoft Corporation Module Name: bthdef.h Abstract:
# This module contains the Bluetooth common structures and definitions Author:
# Notes: Environment: Kernel mode only Revision History: - -
if not defined(__BTHDEF_H__):
    __BTHDEF_H__ = 1
    from pyWinAPI.shared.winapifamily_h import *
    from pyWinAPI.shared.sdkddkver_h import *
    from pyWinAPI.shared.guiddef_h import *

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if (
            NTDDI_VERSION > NTDDI_VISTASP1 or
            (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
        ):
            BTH_MAJORVERSION = 2
            BTH_MINORVERSION = 1
        elif NTDDI_VERSION >= NTDDI_WINXPSP2:
            BTH_MAJORVERSION = 2
            BTH_MINORVERSION = 0
        # END IF   >= SP1 + KB942567

        if _MSC_VER >= 1200:
            pass
        # END IF
        if NTDDI_VERSION >= NTDDI_WINXPSP2:
            if not defined(GUID_DEFS_ONLY):
                if not defined(NO_BTHSDPDEF_INC):
                    from pyWinAPI.shared.bthsdpdef_h import *

                # END IF   NO_BTHSDPDEF_INC
            # END IF   GUID_DEFS_ONLY

            if not defined(NO_GUID_DEFS):

                # {0850302A-B344-4fda-9BE9-90576B8D46F0}
                GUID_BTHPORT_DEVICE_INTERFACE = DEFINE_GUID(
                    0x850302a,
                    0xb344,
                    0x4fda,
                    0x9b,
                    0xe9,
                    0x90,
                    0x57,
                    0x6b,
                    0x8d,
                    0x46,
                    0xf0
                )

                # RFCOMM device interface GUID for RFCOMM services
                # {b142fc3e-fa4e-460b-8abc-072b628b3c70}
                GUID_BTH_RFCOMM_SERVICE_DEVICE_INTERFACE = DEFINE_GUID(
                    0xb142fc3e,
                    0xfa4e,
                    0x460b,
                    0x8a,
                    0xbc,
                    0x07,
                    0x2b,
                    0x62,
                    0x8b,
                    0x3c,
                    0x70
                )

                # {EA3B5B82-26EE-450E-B0D8-D26FE30A3869}
                GUID_BLUETOOTH_RADIO_IN_RANGE = DEFINE_GUID(
                    0xea3b5b82,
                    0x26ee,
                    0x450e,
                    0xb0,
                    0xd8,
                    0xd2,
                    0x6f,
                    0xe3,
                    0x0a,
                    0x38,
                    0x69
                )

                #  {E28867C9-C2AA-4CED-B969-4570866037C4}
                GUID_BLUETOOTH_RADIO_OUT_OF_RANGE = DEFINE_GUID(
                    0xe28867c9,
                    0xc2aa,
                    0x4ced,
                    0xb9,
                    0x69,
                    0x45,
                    0x70,
                    0x86,
                    0x60,
                    0x37,
                    0xc4
                )

                # {7EAE4030-B709-4AA8-AC55-E953829C9DAA}
                GUID_BLUETOOTH_L2CAP_EVENT = DEFINE_GUID(
                    0x7eae4030,
                    0xb709,
                    0x4aa8,
                    0xac,
                    0x55,
                    0xe9,
                    0x53,
                    0x82,
                    0x9c,
                    0x9d,
                    0xaa
                )

                # {FC240062-1541-49BE-B463-84C4DCD7BF7F}
                GUID_BLUETOOTH_HCI_EVENT = DEFINE_GUID(
                    0xfc240062,
                    0x1541,
                    0x49be,
                    0xb4,
                    0x63,
                    0x84,
                    0xc4,
                    0xdc,
                    0xd7,
                    0xbf,
                    0x7f
                )

                # Support added in KB942567
                if (
                    NTDDI_VERSION > NTDDI_VISTASP1 or
                    (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
                ):
                    # {5DC9136D - 996C - 46DB - 84F5 - 32C0A3F47352}
                    GUID_BLUETOOTH_AUTHENTICATION_REQUEST = DEFINE_GUID(
                        0x5DC9136D,
                        0x996C,
                        0x46DB,
                        0x84,
                        0xF5,
                        0x32,
                        0xC0,
                        0xA3,
                        0xF4,
                        0x73,
                        0x52
                    )

                    # {D668DFCD - 0F4E - 4EFC - BFE0 - 392EEEC5109C}
                    GUID_BLUETOOTH_KEYPRESS_EVENT = DEFINE_GUID(
                        0xD668DFCD,
                        0x0F4E,
                        0x4EFC,
                        0xBF,
                        0xE0,
                        0x39,
                        0x2E,
                        0xEE,
                        0xC5,
                        0x10,
                        0x9C
                    )

                    # {547247e6 - 45bb - 4c33 - af8c - c00efe15a71d}
                    GUID_BLUETOOTH_HCI_VENDOR_EVENT = DEFINE_GUID(
                        0x547247e6,
                        0x45bb,
                        0x4c33,
                        0xaf,
                        0x8c,
                        0xc0,
                        0x0e,
                        0xfe,
                        0x15,
                        0xa7,
                        0x1d
                    )
                # END IF   >= SP1 + KB942567

                # Bluetooth base UUID for service discovery

                Bluetooth_Base_UUID = DEFINE_GUID(
                    0x00000000,
                    0x0000,
                    0x1000,
                    0x80,
                    0x00,
                    0x00,
                    0x80,
                    0x5F,
                    0x9B,
                    0x34,
                    0xFB
                )

                # Creates the 128 - bit UUID from a SHORT id by using the
                # Bluetooth base UUID
                # {<SHORT id> - 0000 - 1000 - 8000 - 00805F9B34FB}

                def DEFINE_BLUETOOTH_UUID128(shortId):
                    return DEFINE_GUID(
                        shortId,
                        0x0000,
                        0x1000,
                        0x80,
                        0x00,
                        0x00,
                        0x80,
                        0x5F,
                        0x9B,
                        0x34,
                        0xFB
                    )

                # UUIDs for the Protocol Identifiers, Service Discovery AsINT
                # Numbers
                SDP_PROTOCOL_UUID16 = 0x0001
                UDP_PROTOCOL_UUID16 = 0x0002
                RFCOMM_PROTOCOL_UUID16 = 0x0003
                TCP_PROTOCOL_UUID16 = 0x0004
                TCSBIN_PROTOCOL_UUID16 = 0x0005
                TCSAT_PROTOCOL_UUID16 = 0x0006
                ATT_PROTOCOL_UUID16 = 0x0007
                OBEX_PROTOCOL_UUID16 = 0x0008
                IP_PROTOCOL_UUID16 = 0x0009
                FTP_PROTOCOL_UUID16 = 0x000A
                HTTP_PROTOCOL_UUID16 = 0x000C
                WSP_PROTOCOL_UUID16 = 0x000E
                BNEP_PROTOCOL_UUID16 = 0x000F
                UPNP_PROTOCOL_UUID16 = 0x0010
                HID_PROTOCOL_UUID16 = 0x0011
                HCCC_PROTOCOL_UUID16 = 0x0012
                HCDC_PROTOCOL_UUID16 = 0x0014
                HCN_PROTOCOL_UUID16 = 0x0016
                AVCTP_PROTOCOL_UUID16 = 0x0017
                AVDTP_PROTOCOL_UUID16 = 0x0019
                CMPT_PROTOCOL_UUID16 = 0x001B
                UDI_C_PLANE_PROTOCOL_UUID16 = 0x001D
                L2CAP_PROTOCOL_UUID16 = 0x0100

                SDP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    SDP_PROTOCOL_UUID16
                )
                UDP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    UDP_PROTOCOL_UUID16
                )
                RFCOMM_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    RFCOMM_PROTOCOL_UUID16
                )
                TCP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    TCP_PROTOCOL_UUID16
                )
                TCSBIN_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    TCSBIN_PROTOCOL_UUID16
                )
                TCSAT_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    TCSAT_PROTOCOL_UUID16
                )
                ATT_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    ATT_PROTOCOL_UUID16
                )
                OBEX_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    OBEX_PROTOCOL_UUID16
                )
                IP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                     IP_PROTOCOL_UUID16
                )
                FTP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    FTP_PROTOCOL_UUID16
                )
                HTTP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    HTTP_PROTOCOL_UUID16
                )
                WSP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    WSP_PROTOCOL_UUID16
                )
                BNEP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    BNEP_PROTOCOL_UUID16
                )
                UPNP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    UPNP_PROTOCOL_UUID16
                )
                HID_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    HID_PROTOCOL_UUID16
                )
                HCCC_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    HCCC_PROTOCOL_UUID16
                )
                HCDC_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    HCDC_PROTOCOL_UUID16
                )
                HCN_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    HCN_PROTOCOL_UUID16
                )
                AVCTP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    AVCTP_PROTOCOL_UUID16
                )
                AVDTP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    AVDTP_PROTOCOL_UUID16
                )
                CMPT_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    CMPT_PROTOCOL_UUID16
                )
                UDI_C_PLANE_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    UDI_C_PLANE_PROTOCOL_UUID16
                )
                L2CAP_PROTOCOL_UUID = DEFINE_BLUETOOTH_UUID128(
                    L2CAP_PROTOCOL_UUID16
                )

                # UUIDs for Service Class IDs, Service Discovery AsINT Numbers
                ServiceDiscoveryServerServiceClassID_UUID16 = 0x1000
                BrowseGroupDescriptorServiceClassID_UUID16 = 0x1001
                PublicBrowseGroupServiceClassID_UUID16 = 0x1002
                SerialPortServiceClassID_UUID16 = 0x1101
                LANAccessUsingPPPServiceClassID_UUID16 = 0x1102
                DialupNetworkingServiceClassID_UUID16 = 0x1103
                IrMCSyncServiceClassID_UUID16 = 0x1104
                OBEXObjectPushServiceClassID_UUID16 = 0x1105
                OBEXFileTransferServiceClassID_UUID16 = 0x1106
                IrMcSyncCommandServiceClassID_UUID16 = 0x1107
                HeadsetServiceClassID_UUID16 = 0x1108
                CordlessTelephonyServiceClassID_UUID16 = 0x1109
                AudioSourceServiceClassID_UUID16 = 0x110A
                AudioSinkServiceClassID_UUID16 = 0x110B
                AVRemoteControlTargetServiceClassID_UUID16 = 0x110C
                AVRemoteControlServiceClassID_UUID16 = 0x110E
                AVRemoteControlControllerServiceClass_UUID16 = 0x110F
                IntercomServiceClassID_UUID16 = 0x1110
                FaxServiceClassID_UUID16 = 0x1111
                HeadsetAudioGatewayServiceClassID_UUID16 = 0x1112
                WAPServiceClassID_UUID16 = 0x1113
                WAPClientServiceClassID_UUID16 = 0x1114
                PANUServiceClassID_UUID16 = 0x1115
                NAPServiceClassID_UUID16 = 0x1116
                GNServiceClassID_UUID16 = 0x1117
                DirectPrintingServiceClassID_UUID16 = 0x1118
                ReferencePrintingServiceClassID_UUID16 = 0x1119
                ImagingResponderServiceClassID_UUID16 = 0x111B
                ImagingAutomaticArchiveServiceClassID_UUID16 = 0x111C
                ImagingReferenceObjectsServiceClassID_UUID16 = 0x111D
                HandsfreeServiceClassID_UUID16 = 0x111E
                HandsfreeAudioGatewayServiceClassID_UUID16 = 0x111F
                DirectPrintingReferenceObjectsServiceClassID_UUID16 = 0x1120
                ReflectsUIServiceClassID_UUID16 = 0x1121
                PrintingStatusServiceClassID_UUID16 = 0x1123
                HumanInterfaceDeviceServiceClassID_UUID16 = 0x1124
                HCRPrintServiceClassID_UUID16 = 0x1126
                HCRScanServiceClassID_UUID16 = 0x1127
                CommonISDNAccessServiceClassID_UUID16 = 0x1128
                VideoConferencingGWServiceClassID_UUID16 = 0x1129
                UDIMTServiceClassID_UUID16 = 0x112A
                UDITAServiceClassID_UUID16 = 0x112B
                AudioVideoServiceClassID_UUID16 = 0x112C
                SimAccessServiceClassID_UUID16 = 0x112D
                PhonebookAccessPceServiceClassID_UUID16 = 0x112E
                PhonebookAccessPseServiceClassID_UUID16 = 0x112F
                HeadsetHSServiceClassID_UUID16 = 0x1131
                MessageAccessServerServiceClassID_UUID16 = 0x1132
                MessageNotificationServerServiceClassID_UUID16 = 0x1133
                GNSSServerServiceClassID_UUID16 = 0x1136
                ThreeDimensionalDisplayServiceClassID_UUID16 = 0x1137
                ThreeDimensionalGlassesServiceClassID_UUID16 = 0x1138
                MPSServiceClassID_UUID16 = 0x113B
                CTNAccessServiceClassID_UUID16 = 0x113C
                CTNNotificationServiceClassID_UUID16 = 0x113D
                PnPInformationServiceClassID_UUID16 = 0x1200
                GenericNetworkingServiceClassID_UUID16 = 0x1201
                GenericFileTransferServiceClassID_UUID16 = 0x1202
                GenericAudioServiceClassID_UUID16 = 0x1203
                GenericTelephonyServiceClassID_UUID16 = 0x1204
                UPnpServiceClassID_UUID16 = 0x1205
                UPnpIpServiceClassID_UUID16 = 0x1206
                ESdpUpnpIpPanServiceClassID_UUID16 = 0x1300
                ESdpUpnpIpLapServiceClassID_UUID16 = 0x1301
                ESdpUpnpL2capServiceClassID_UUID16 = 0x1302
                VideoSourceServiceClassID_UUID16 = 0x1303
                VideoSinkServiceClassID_UUID16 = 0x1304
                HealthDeviceProfileSourceServiceClassID_UUID16 = 0x1401
                HealthDeviceProfileSinkServiceClassID_UUID16 = 0x1402

                ServiceDiscoveryServerServiceClassID_UUID = DEFINE_BLUETOOTH_UUID128(
                    ServiceDiscoveryServerServiceClassID_UUID16
                )
                BrowseGroupDescriptorServiceClassID_UUID = DEFINE_BLUETOOTH_UUID128(
                    BrowseGroupDescriptorServiceClassID_UUID16
                )
                PublicBrowseGroupServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    PublicBrowseGroupServiceClassID_UUID16
                )

                SerialPortServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    SerialPortServiceClassID_UUID16
                )
                LANAccessUsingPPPServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    LANAccessUsingPPPServiceClassID_UUID16
                )
                DialupNetworkingServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    DialupNetworkingServiceClassID_UUID16
                )
                IrMCSyncServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    IrMCSyncServiceClassID_UUID16
                )
                OBEXObjectPushServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    OBEXObjectPushServiceClassID_UUID16
                )
                OBEXFileTransferServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    OBEXFileTransferServiceClassID_UUID16
                )
                IrMCSyncCommandServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    IrMcSyncCommandServiceClassID_UUID16
                )
                HeadsetServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HeadsetServiceClassID_UUID16
                )
                CordlessTelephonyServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    CordlessTelephonyServiceClassID_UUID16
                )
                AudioSourceServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    AudioSourceServiceClassID_UUID16
                )
                AudioSinkServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    AudioSinkServiceClassID_UUID16
                )
                AVRemoteControlTargetServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    AVRemoteControlTargetServiceClassID_UUID16
                )
                AVRemoteControlServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    AVRemoteControlServiceClassID_UUID16
                )
                AVRemoteControlControllerServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    AVRemoteControlControllerServiceClass_UUID16
                )
                IntercomServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    IntercomServiceClassID_UUID16
                )
                FaxServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    FaxServiceClassID_UUID16
                )
                HeadsetAudioGatewayServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HeadsetAudioGatewayServiceClassID_UUID16
                )
                WAPServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    WAPServiceClassID_UUID16
                )
                WAPClientServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    WAPClientServiceClassID_UUID16
                )
                PANUServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    PANUServiceClassID_UUID16
                )
                NAPServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    NAPServiceClassID_UUID16
                )
                GNServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    GNServiceClassID_UUID16
                )
                DirectPrintingServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    DirectPrintingServiceClassID_UUID16
                )
                ReferencePrintingServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ReferencePrintingServiceClassID_UUID16
                )
                ImagingResponderServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ImagingResponderServiceClassID_UUID16
                )
                ImagingAutomaticArchiveServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ImagingAutomaticArchiveServiceClassID_UUID16
                )
                ImagingReferenceObjectsServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ImagingReferenceObjectsServiceClassID_UUID16
                )
                HandsfreeServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HandsfreeServiceClassID_UUID16
                )
                HandsfreeAudioGatewayServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HandsfreeAudioGatewayServiceClassID_UUID16
                )
                DirectPrintingReferenceObjectsServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    DirectPrintingReferenceObjectsServiceClassID_UUID16
                )
                ReflectedUIServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ReflectsUIServiceClassID_UUID16
                )
                PrintingStatusServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    PrintingStatusServiceClassID_UUID16
                )
                HumanInterfaceDeviceServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HumanInterfaceDeviceServiceClassID_UUID16
                )
                HCRPrintServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HCRPrintServiceClassID_UUID16
                )
                HCRScanServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HCRScanServiceClassID_UUID16
                )
                CommonISDNAccessServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    CommonISDNAccessServiceClassID_UUID16
                )
                VideoConferencingGWServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    VideoConferencingGWServiceClassID_UUID16
                )
                UDIMTServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    UDIMTServiceClassID_UUID16
                )
                UDITAServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    UDITAServiceClassID_UUID16
                )
                AudioVideoServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    AudioVideoServiceClassID_UUID16
                )
                SimAccessServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    SimAccessServiceClassID_UUID16
                )
                PhonebookAccessPceServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    PhonebookAccessPceServiceClassID_UUID16
                )
                PhonebookAccessPseServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    PhonebookAccessPseServiceClassID_UUID16
                )

                HeadsetHSServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HeadsetHSServiceClassID_UUID16
                )
                MessageAccessServerServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    MessageAccessServerServiceClassID_UUID16
                )
                MessageNotificationServerServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    MessageNotificationServerServiceClassID_UUID16
                )

                GNSSServerServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    GNSSServerServiceClassID_UUID16
                )
                ThreeDimensionalDisplayServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ThreeDimensionalDisplayServiceClassID_UUID16
                )
                ThreeDimensionalGlassesServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ThreeDimensionalGlassesServiceClassID_UUID16
                )

                MPSServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    MPSServiceClassID_UUID16
                )
                CTNAccessServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    CTNAccessServiceClassID_UUID16
                )
                CTNNotificationServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    CTNNotificationServiceClassID_UUID16
                )

                PnPInformationServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    PnPInformationServiceClassID_UUID16
                )
                GenericNetworkingServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    GenericNetworkingServiceClassID_UUID16
                )
                GenericFileTransferServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    GenericFileTransferServiceClassID_UUID16
                )
                GenericAudioServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    GenericAudioServiceClassID_UUID16
                )
                GenericTelephonyServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    GenericTelephonyServiceClassID_UUID16
                )
                UPnpServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    UPnpServiceClassID_UUID16
                )
                UPnpIpServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    UPnpIpServiceClassID_UUID16
                )

                ESdpUpnpIpPanServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ESdpUpnpIpPanServiceClassID_UUID16
                )
                ESdpUpnpIpLapServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ESdpUpnpIpLapServiceClassID_UUID16
                )
                ESdpUpnpL2capServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    ESdpUpnpL2capServiceClassID_UUID16
                )
                VideoSourceServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    VideoSourceServiceClassID_UUID16
                )
                VideoSinkServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    VideoSinkServiceClassID_UUID16
                )

                HealthDeviceProfileSourceServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HealthDeviceProfileSourceServiceClassID_UUID16
                )
                HealthDeviceProfileSinkServiceClass_UUID = DEFINE_BLUETOOTH_UUID128(
                    HealthDeviceProfileSinkServiceClassID_UUID16
                )

                # UUIDs for SIG defined profiles, Service Discovery AsINT
                # Numbers
                AdvancedAudioDistributionProfileID_UUID16 = 0x110D
                ImagingServiceProfileID_UUID16 = 0x111A
                BasicPrintingProfileID_UUID16 = 0x1122
                HardcopyCableReplacementProfileID_UUID16 = 0x1125
                PhonebookAccessProfileID_UUID16 = 0x1130
                MessageAccessProfileID_UUID16 = 0x1134
                GNSSProfileID_UUID16 = 0x1135
                ThreeDimensionalSynchronizationProfileID_UUID16 = 0x1139
                MPSProfileID_UUID16 = 0x113A
                CTNProfileID_UUID16 = 0x113E
                VideoDistributionProfileID_UUID16 = 0x1305
                HealthDeviceProfileID_UUID16 = 0x1400

                AdvancedAudioDistributionProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    AdvancedAudioDistributionProfileID_UUID16
                )
                ImagingServiceProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    ImagingServiceProfileID_UUID16
                )
                BasicPrintingProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    BasicPrintingProfileID_UUID16
                )
                HardcopyCableReplacementProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    HardcopyCableReplacementProfileID_UUID16
                )
                PhonebookAccessProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    PhonebookAccessProfileID_UUID16
                )
                MessageAccessProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    MessageAccessProfileID_UUID16
                )
                GNSSProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    GNSSProfileID_UUID16
                )
                ThreeDimensionalSynchronizationProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    ThreeDimensionalSynchronizationProfileID_UUID16
                )
                MPSProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                     MPSProfileID_UUID16
                )
                CTNProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                     CTNProfileID_UUID16
                )
                VideoDistributionProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    VideoDistributionProfileID_UUID16
                )
                HealthDeviceProfile_UUID = DEFINE_BLUETOOTH_UUID128(
                    HealthDeviceProfileID_UUID16
                )

                # The SIG renamed the uuid for VideoConferencingServiceClass
                VideoConferencingServiceClass_UUID = (
                    AVRemoteControlControllerServiceClass_UUID
                )
                VideoConferencingServiceClassID_UUID16 = (
                    AVRemoteControlControllerServiceClass_UUID16
                )

                # Fixing typos introduced in previous releases
                HN_PROTOCOL_UUID = HCN_PROTOCOL_UUID
                BasicPringingServiceClass_UUID = BasicPrintingProfile_UUID

                # Fixing naming inconsistencies in UUID16 list
                CommonISDNAccessServiceClass_UUID16 = (
                    CommonISDNAccessServiceClassID_UUID16
                )
                VideoConferencingGWServiceClass_UUID16 = (
                    VideoConferencingGWServiceClassID_UUID16
                )
                UDIMTServiceClass_UUID16 = UDIMTServiceClassID_UUID16
                UDITAServiceClass_UUID16 = UDITAServiceClassID_UUID16
                AudioVideoServiceClass_UUID16 = AudioVideoServiceClassID_UUID16

                # Fixing naming inconsistencies in profile list
                CordlessServiceClassID_UUID16 = (
                    CordlessTelephonyServiceClassID_UUID16
                )
                AudioSinkSourceServiceClassID_UUID16 = (
                    AudioSinkServiceClassID_UUID16
                )
                AdvancedAudioDistributionServiceClassID_UUID16 = (
                    AdvancedAudioDistributionProfileID_UUID16
                )
                ImagingServiceClassID_UUID16 = ImagingServiceProfileID_UUID16
                BasicPrintingServiceClassID_UUID16 = (
                    BasicPrintingProfileID_UUID16
                )
                HardcopyCableReplacementServiceClassID_UUID16 = (
                    HardcopyCableReplacementProfileID_UUID16
                )
                AdvancedAudioDistributionServiceClass_UUID = (
                    AdvancedAudioDistributionProfile_UUID
                )
                ImagingServiceClass_UUID = ImagingServiceProfile_UUID
                BasicPrintingServiceClass_UUID = BasicPrintingProfile_UUID
                HardcopyCableReplacementServiceClass_UUID = (
                    HardcopyCableReplacementProfile_UUID
                )
                VideoDistributionServiceClass_UUID = (
                    VideoDistributionProfile_UUID
                )
            # END IF    NO_GUID_DEFS

            if not defined(GUID_DEFS_ONLY):
                BTH_MAX_NAME_SIZE = 248
                BTH_MAX_PIN_SIZE = 16
                BTH_LINK_KEY_LENGTH = 16
                BTH_MFG_ERICSSON = 0
                BTH_MFG_NOKIA = 1
                BTH_MFG_INTEL = 2
                BTH_MFG_IBM = 3
                BTH_MFG_TOSHIBA = 4
                BTH_MFG_3COM = 5
                BTH_MFG_MICROSOFT = 6
                BTH_MFG_LUCENT = 7
                BTH_MFG_MOTOROLA = 8
                BTH_MFG_INFINEON = 9
                BTH_MFG_CSR = 10
                BTH_MFG_SILICONWAVE = 11
                BTH_MFG_DIGIANSWER = 12
                BTH_MFG_TI = 13
                BTH_MFG_PARTHUS = 14
                BTH_MFG_BROADCOM = 15
                BTH_MFG_MITEL = 16
                BTH_MFG_WIDCOMM = 17
                BTH_MFG_ZEEVO = 18
                BTH_MFG_ATMEL = 19
                BTH_MFG_MITSIBUSHI = 20
                BTH_MFG_RTX_TELECOM = 21
                BTH_MFG_KC_TECHNOLOGY = 22
                BTH_MFG_NEWLOGIC = 23
                BTH_MFG_TRANSILICA = 24
                BTH_MFG_ROHDE_SCHWARZ = 25
                BTH_MFG_TTPCOM = 26
                BTH_MFG_SIGNIA = 27
                BTH_MFG_CONEXANT = 28
                BTH_MFG_QUALCOMM = 29
                BTH_MFG_INVENTEL = 30
                BTH_MFG_AVM_BERLIN = 31
                BTH_MFG_BANDSPEED = 32
                BTH_MFG_MANSELLA = 33
                BTH_MFG_NEC = 34
                BTH_MFG_WAVEPLUS_TECHNOLOGY_CO = 35
                BTH_MFG_ALCATEL = 36
                BTH_MFG_PHILIPS_SEMICONDUCTOR = 37
                BTH_MFG_C_TECHNOLOGIES = 38
                BTH_MFG_OPEN_INTERFACE = 39
                BTH_MFG_RF_MICRO_DEVICES = 40
                BTH_MFG_HITACHI = 41
                BTH_MFG_SYMBOL_TECHNOLOGIES = 42
                BTH_MFG_TENOVIS = 43
                BTH_MFG_MACRONIX_INTERNATIONAL = 44
                BTH_MFG_MARVELL = 72
                BTH_MFG_APPLE = 76
                BTH_MFG_NORDIC_SEMICONDUCTORS_ASA = 89
                BTH_MFG_ARUBA_NETWORKS = 283
                BTH_MFG_INTERNAL_USE = 65535

                BTH_ADDR = ULONGLONG
                PBTH_ADDR = POINTER(BTH_ADDR)
                BTH_COD = ULONG
                PBTH_COD = POINTER(BTH_COD)
                BTH_LAP = ULONG
                PBTH_LAP = POINTER(BTH_LAP)


                BTH_ADDR_NULL = 0x0000000000000000
                NAP_MASK = 0xFFFF00000000
                SAP_MASK = 0x0000FFFFFFFF
                NAP_BIT_OFFSET = 8 * 4
                SAP_BIT_OFFSET = 0


                def GET_NAP(_bth_addr):
                    return (
                        USHORT((_bth_addr & NAP_MASK) >> NAP_BIT_OFFSET).value
                    )


                def GET_SAP(_bth_addr):
                    return (
                        ULONG((_bth_addr & SAP_MASK) >> SAP_BIT_OFFSET).value
                    )


                def SET_NAP(_nap):
                    return ULONGLONG(USHORT(_nap) << NAP_BIT_OFFSET).value


                def SET_SAP(_sap):
                    return ULONGLONG(ULONG (_sap) << SAP_BIT_OFFSET).value


                def SET_NAP_SAP(_nap, _sap):
                    return SET_NAP(_nap) | SET_SAP(_sap)


                COD_FORMAT_BIT_OFFSET = 0
                COD_MINOR_BIT_OFFSET = 2
                COD_MAJOR_BIT_OFFSET = 8 * 1
                COD_SERVICE_BIT_OFFSET = 8 * 1 + 5
                COD_FORMAT_MASK = 0x000003
                COD_MINOR_MASK = 0x0000FC
                COD_MAJOR_MASK = 0x001F00
                COD_SERVICE_MASK = 0xFFE000


                def GET_COD_FORMAT(_cod):
                    return (_cod & COD_FORMAT_MASK) >> COD_FORMAT_BIT_OFFSET


                def GET_COD_MINOR(_cod):
                    return (_cod & COD_MINOR_MASK) >> COD_MINOR_BIT_OFFSET


                def GET_COD_MAJOR(_cod):
                    return (_cod & COD_MAJOR_MASK) >> COD_MAJOR_BIT_OFFSET


                def GET_COD_SERVICE(_cod):
                    return (_cod & COD_SERVICE_MASK) >> COD_SERVICE_BIT_OFFSET


                def SET_COD_MINOR(_cod, _minor):
                    _cod = (
                        (_cod & ~COD_MINOR_MASK) |
                        (_minor << COD_MINOR_BIT_OFFSET)
                    )
                    return _cod


                def SET_COD_MAJOR(_cod, _major):
                    _cod = (
                        (_cod & ~COD_MAJOR_MASK) |
                        (_major << COD_MAJOR_BIT_OFFSET)
                    )
                    return _cod


                def SET_COD_SERVICE(_cod, _service):
                    _cod = (
                        (_cod & ~COD_SERVICE_MASK) |
                        (_service << COD_SERVICE_BIT_OFFSET)
                    )
                    return _cod


                COD_VERSION = 0x0
                COD_SERVICE_LIMITED = 0x0001
                COD_SERVICE_POSITIONING = 0x0008
                COD_SERVICE_NETWORKING = 0x0010
                COD_SERVICE_RENDERING = 0x0020
                COD_SERVICE_CAPTURING = 0x0040
                COD_SERVICE_OBJECT_XFER = 0x0080
                COD_SERVICE_AUDIO = 0x0100
                COD_SERVICE_TELEPHONY = 0x0200
                COD_SERVICE_INFORMATION = 0x0400
                COD_SERVICE_VALID_MASK = (
                    COD_SERVICE_LIMITED  |
                    COD_SERVICE_POSITIONING  |
                    COD_SERVICE_NETWORKING  |
                    COD_SERVICE_RENDERING  |
                    COD_SERVICE_CAPTURING  |
                    COD_SERVICE_OBJECT_XFER  |
                    COD_SERVICE_AUDIO  |
                    COD_SERVICE_TELEPHONY  |
                    COD_SERVICE_INFORMATION
                )
                COD_SERVICE_MAX_COUNT = 9

                # Major class codes
                COD_MAJOR_MISCELLANEOUS = 0x00
                COD_MAJOR_COMPUTER = 0x01
                COD_MAJOR_PHONE = 0x02
                COD_MAJOR_LAN_ACCESS = 0x03
                COD_MAJOR_AUDIO = 0x04
                COD_MAJOR_PERIPHERAL = 0x05
                COD_MAJOR_IMAGING = 0x06
                COD_MAJOR_WEARABLE = 0x07
                COD_MAJOR_TOY = 0x08
                COD_MAJOR_HEALTH = 0x09
                COD_MAJOR_UNCLASSIFIED = 0x1F

                # Minor class codes specific to each major class
                COD_COMPUTER_MINOR_UNCLASSIFIED = 0x00
                COD_COMPUTER_MINOR_DESKTOP = 0x01
                COD_COMPUTER_MINOR_SERVER = 0x02
                COD_COMPUTER_MINOR_LAPTOP = 0x03
                COD_COMPUTER_MINOR_HANDHELD = 0x04
                COD_COMPUTER_MINOR_PALM = 0x05
                COD_COMPUTER_MINOR_WEARABLE = 0x06
                COD_PHONE_MINOR_UNCLASSIFIED = 0x00
                COD_PHONE_MINOR_CELLULAR = 0x01
                COD_PHONE_MINOR_CORDLESS = 0x02
                COD_PHONE_MINOR_SMART = 0x03
                COD_PHONE_MINOR_WIRED_MODEM = 0x04
                COD_AUDIO_MINOR_UNCLASSIFIED = 0x00
                COD_AUDIO_MINOR_HEADSET = 0x01
                COD_AUDIO_MINOR_HANDS_FREE = 0x02
                COD_AUDIO_MINOR_HEADSET_HANDS_FREE = 0x03
                COD_AUDIO_MINOR_MICROPHONE = 0x04
                COD_AUDIO_MINOR_LOUDSPEAKER = 0x05
                COD_AUDIO_MINOR_HEADPHONES = 0x06
                COD_AUDIO_MINOR_PORTABLE_AUDIO = 0x07
                COD_AUDIO_MINOR_CAR_AUDIO = 0x08
                COD_AUDIO_MINOR_SET_TOP_BOX = 0x09
                COD_AUDIO_MINOR_HIFI_AUDIO = 0x0A
                COD_AUDIO_MINOR_VCR = 0x0B
                COD_AUDIO_MINOR_VIDEO_CAMERA = 0x0C
                COD_AUDIO_MINOR_CAMCORDER = 0x0D
                COD_AUDIO_MINOR_VIDEO_MONITOR = 0x0E
                COD_AUDIO_MINOR_VIDEO_DISPLAY_LOUDSPEAKER = 0x0F
                COD_AUDIO_MINOR_VIDEO_DISPLAY_CONFERENCING = 0x10

                # define COD_AUDIO_MINOR_RESERVED  (0x11)
                COD_AUDIO_MINOR_GAMING_TOY = 0x12
                COD_PERIPHERAL_MINOR_KEYBOARD_MASK = 0x10
                COD_PERIPHERAL_MINOR_POINTER_MASK = 0x20
                COD_PERIPHERAL_MINOR_NO_CATEGORY = 0x00
                COD_PERIPHERAL_MINOR_JOYSTICK = 0x01
                COD_PERIPHERAL_MINOR_GAMEPAD = 0x02
                COD_PERIPHERAL_MINOR_REMOTE_CONTROL = 0x03
                COD_PERIPHERAL_MINOR_SENSING = 0x04
                COD_IMAGING_MINOR_DISPLAY_MASK = 0x04
                COD_IMAGING_MINOR_CAMERA_MASK = 0x08
                COD_IMAGING_MINOR_SCANNER_MASK = 0x10
                COD_IMAGING_MINOR_PRINTER_MASK = 0x20
                COD_WEARABLE_MINOR_WRIST_WATCH = 0x01
                COD_WEARABLE_MINOR_PAGER = 0x02
                COD_WEARABLE_MINOR_JACKET = 0x03
                COD_WEARABLE_MINOR_HELMET = 0x04
                COD_WEARABLE_MINOR_GLASSES = 0x05
                COD_TOY_MINOR_ROBOT = 0x01
                COD_TOY_MINOR_VEHICLE = 0x02
                COD_TOY_MINOR_DOLL_ACTION_FIGURE = 0x03
                COD_TOY_MINOR_CONTROLLER = 0x04
                COD_TOY_MINOR_GAME = 0x05
                COD_HEALTH_MINOR_BLOOD_PRESSURE_MONITOR = 0x01
                COD_HEALTH_MINOR_THERMOMETER = 0x02
                COD_HEALTH_MINOR_WEIGHING_SCALE = 0x03
                COD_HEALTH_MINOR_GLUCOSE_METER = 0x04
                COD_HEALTH_MINOR_PULSE_OXIMETER = 0x05
                COD_HEALTH_MINOR_HEART_PULSE_MONITOR = 0x06
                COD_HEALTH_MINOR_HEALTH_DATA_DISPLAY = 0x07
                COD_HEALTH_MINOR_STEP_COUNTER = 0x08

                # Cannot use GET_COD_MINOR for this b/c it is embedded in a
                # different manner

                # than the rest of the major classes
                COD_LAN_ACCESS_BIT_OFFSET = 5
                COD_LAN_MINOR_MASK = 0x00001C
                COD_LAN_ACCESS_MASK = 0x0000E0


                def GET_COD_LAN_MINOR(_cod):
                    return (_cod & COD_LAN_MINOR_MASK) >> COD_MINOR_BIT_OFFSET


                def GET_COD_LAN_ACCESS(_cod):
                    return (
                        (_cod & COD_LAN_ACCESS_MASK) >>
                        COD_LAN_ACCESS_BIT_OFFSET
                    )

                # LAN access percent usage subcodes
                COD_LAN_MINOR_UNCLASSIFIED = 0x00
                COD_LAN_ACCESS_0_USED = 0x00
                COD_LAN_ACCESS_17_USED = 0x01
                COD_LAN_ACCESS_33_USED = 0x02
                COD_LAN_ACCESS_50_USED = 0x03
                COD_LAN_ACCESS_67_USED = 0x04
                COD_LAN_ACCESS_83_USED = 0x05
                COD_LAN_ACCESS_99_USED = 0x06
                COD_LAN_ACCESS_FULL = 0x07

                # Extended Inquiry Response (EIR) defines.
                BTH_EIR_FLAGS_ID = 0x01
                BTH_EIR_16_UUIDS_PARTIAL_ID = 0x02
                BTH_EIR_16_UUIDS_COMPLETE_ID = 0x03
                BTH_EIR_32_UUIDS_PARTIAL_ID = 0x04
                BTH_EIR_32_UUIDS_COMPLETE_ID = 0x05
                BTH_EIR_128_UUIDS_PARTIAL_ID = 0x06
                BTH_EIR_128_UUIDS_COMPLETE_ID = 0x07
                BTH_EIR_LOCAL_NAME_PARTIAL_ID = 0x08
                BTH_EIR_LOCAL_NAME_COMPLETE_ID = 0x09
                BTH_EIR_TX_POWER_LEVEL_ID = 0x0A
                BTH_EIR_OOB_OPT_DATA_LEN_ID = 0x0B
                BTH_EIR_OOB_BD_ADDR_ID = 0x0C
                BTH_EIR_OOB_COD_ID = 0x0D
                BTH_EIR_OOB_SP_HASH_ID = 0x0E
                BTH_EIR_OOB_SP_RANDOMIZER_ID = 0x0F
                BTH_EIR_MANUFACTURER_ID = 0xFF

                # Extended Inquiry Response (EIR) size.
                BTH_EIR_SIZE = 240

                # Used as an initializer of LAP_DATA
                LAP_GIAC_INIT = [ 0x33, 0x8B, 0x9E ]
                LAP_LIAC_INIT = [ 0x00, 0x8B, 0x9E ]

                # General Inquiry Access Code.
                LAP_GIAC_VALUE = 0x009E8B33

                # Limited Inquiry Access Code.
                LAP_LIAC_VALUE = 0x009E8B00
                BTH_ADDR_IAC_FIRST = 0x9E8B00
                BTH_ADDR_IAC_LAST = 0x9E8B3F
                BTH_ADDR_LIAC = 0x9E8B00
                BTH_ADDR_GIAC = 0x9E8B33


                def BTH_ERROR(_btStatus):
                    return _btStatus != BTH_ERROR_SUCCESS


                def BTH_SUCCESS(_btStatus):
                    return _btStatus == BTH_ERROR_SUCCESS


                BTH_ERROR_SUCCESS = 0x00
                BTH_ERROR_UNKNOWN_HCI_COMMAND = 0x01
                BTH_ERROR_NO_CONNECTION = 0x02
                BTH_ERROR_HARDWARE_FAILURE = 0x03
                BTH_ERROR_PAGE_TIMEOUT = 0x04
                BTH_ERROR_AUTHENTICATION_FAILURE = 0x05
                BTH_ERROR_KEY_MISSING = 0x06
                BTH_ERROR_MEMORY_FULL = 0x07
                BTH_ERROR_CONNECTION_TIMEOUT = 0x08
                BTH_ERROR_MAX_NUMBER_OF_CONNECTIONS = 0x09
                BTH_ERROR_MAX_NUMBER_OF_SCO_CONNECTIONS = 0x0A
                BTH_ERROR_ACL_CONNECTION_ALREADY_EXISTS = 0x0B
                BTH_ERROR_COMMAND_DISALLOWED = 0x0C
                BTH_ERROR_HOST_REJECTED_LIMITED_RESOURCES = 0x0D
                BTH_ERROR_HOST_REJECTED_SECURITY_REASONS = 0x0E
                BTH_ERROR_HOST_REJECTED_PERSONAL_DEVICE = 0x0F
                BTH_ERROR_HOST_TIMEOUT = 0x10
                BTH_ERROR_UNSUPPORTED_FEATURE_OR_PARAMETER = 0x11
                BTH_ERROR_INVALID_HCI_PARAMETER = 0x12
                BTH_ERROR_REMOTE_USER_ENDED_CONNECTION = 0x13
                BTH_ERROR_REMOTE_LOW_RESOURCES = 0x14
                BTH_ERROR_REMOTE_POWERING_OFF = 0x15
                BTH_ERROR_LOCAL_HOST_TERMINATED_CONNECTION = 0x16
                BTH_ERROR_REPEATED_ATTEMPTS = 0x17
                BTH_ERROR_PAIRING_NOT_ALLOWED = 0x18
                BTH_ERROR_UKNOWN_LMP_PDU = 0x19
                BTH_ERROR_UNSUPPORTED_REMOTE_FEATURE = 0x1A
                BTH_ERROR_SCO_OFFSET_REJECTED = 0x1B
                BTH_ERROR_SCO_INTERVAL_REJECTED = 0x1C
                BTH_ERROR_SCO_AIRMODE_REJECTED = 0x1D
                BTH_ERROR_INVALID_LMP_PARAMETERS = 0x1E
                BTH_ERROR_UNSPECIFIED_ERROR = 0x1F
                BTH_ERROR_UNSUPPORTED_LMP_PARM_VALUE = 0x20
                BTH_ERROR_ROLE_CHANGE_NOT_ALLOWED = 0x21
                BTH_ERROR_LMP_RESPONSE_TIMEOUT = 0x22
                BTH_ERROR_LMP_TRANSACTION_COLLISION = 0x23
                BTH_ERROR_LMP_PDU_NOT_ALLOWED = 0x24
                BTH_ERROR_ENCRYPTION_MODE_NOT_ACCEPTABLE = 0x25
                BTH_ERROR_UNIT_KEY_NOT_USED = 0x26
                BTH_ERROR_QOS_IS_NOT_SUPPORTED = 0x27
                BTH_ERROR_INSTANT_PASSED = 0x28
                BTH_ERROR_PAIRING_WITH_UNIT_KEY_NOT_SUPPORTED = 0x29
                BTH_ERROR_DIFFERENT_TRANSACTION_COLLISION = 0x2A
                BTH_ERROR_QOS_UNACCEPTABLE_PARAMETER = 0x2C
                BTH_ERROR_QOS_REJECTED = 0x2D
                BTH_ERROR_CHANNEL_CLASSIFICATION_NOT_SUPPORTED = 0x2E
                BTH_ERROR_INSUFFICIENT_SECURITY = 0x2F
                BTH_ERROR_PARAMETER_OUT_OF_MANDATORY_RANGE = 0x30
                BTH_ERROR_ROLE_SWITCH_PENDING = 0x32
                BTH_ERROR_RESERVED_SLOT_VIOLATION = 0x34
                BTH_ERROR_ROLE_SWITCH_FAILED = 0x35
                BTH_ERROR_EXTENDED_INQUIRY_RESPONSE_TOO_LARGE = 0x36
                BTH_ERROR_SECURE_SIMPLE_PAIRING_NOT_SUPPORTED_BY_HOST = 0x37
                BTH_ERROR_HOST_BUSY_PAIRING = 0x38
                BTH_ERROR_CONNECTION_REJECTED_DUE_TO_NO_SUITABLE_CHANNEL_FOUND = 0x39
                BTH_ERROR_CONTROLLER_BUSY = 0x3A
                BTH_ERROR_UNACCEPTABLE_CONNECTION_INTERVAL = 0x3B
                BTH_ERROR_DIRECTED_ADVERTISING_TIMEOUT = 0x3C
                BTH_ERROR_CONNECTION_TERMINATED_DUE_TO_MIC_FAILURE = 0x3D
                BTH_ERROR_CONNECTION_FAILED_TO_BE_ESTABLISHED = 0x3E
                BTH_ERROR_MAC_CONNECTION_FAILED = 0x3F
                BTH_ERROR_UNSPECIFIED = 0xFF

                # Min, max, and default L2cap MTU.
                L2CAP_MIN_MTU = 48
                L2CAP_MAX_MTU = 0xFFFF
                L2CAP_DEFAULT_MTU = 672

                # Max l2cap signal size (48) - size of signal header (4)
                MAX_L2CAP_PING_DATA_LENGTH = 44
                MAX_L2CAP_INFO_DATA_LENGTH = 44

                # the following structures provide information about

                # disocvered remote radios.
                BDIF_ADDRESS = 0x00000001
                BDIF_COD = 0x00000002
                BDIF_NAME = 0x00000004
                BDIF_PAIRED = 0x00000008
                BDIF_PERSONAL = 0x00000010
                BDIF_CONNECTED = 0x00000020

                # Support added in KB942567

                if (
                    NTDDI_VERSION > NTDDI_VISTASP1 or
                    (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
                ):
                    BDIF_SHORT_NAME = 0x00000040
                    BDIF_VISIBLE = 0x00000080
                    BDIF_SSP_SUPPORTED = 0x00000100
                    BDIF_SSP_PAIRED = 0x00000200
                    BDIF_SSP_MITM_PROTECTED = 0x00000400
                    BDIF_RSSI = 0x00001000
                    BDIF_EIR = 0x00002000

                    if NTDDI_VERSION >= NTDDI_WIN8: #  >= WIN8
                        BDIF_BR = 0x00004000
                        BDIF_LE = 0x00008000
                        BDIF_LE_PAIRED = 0x00010000
                        BDIF_LE_PERSONAL = 0x00020000
                        BDIF_LE_MITM_PROTECTED = 0x00040000
                        BDIF_LE_PRIVACY_ENABLED = 0x00080000
                        BDIF_LE_RANDOM_ADDRESS_TYPE = 0x00100000

                        if NTDDI_VERSION >= NTDDI_WIN10: #  >= WIN10
                            BDIF_LE_DISCOVERABLE = 0x00200000
                            BDIF_LE_NAME = 0x00400000
                            BDIF_LE_VISIBLE = 0x00800000

                            if NTDDI_VERSION >= NTDDI_WIN10_RS2: #  >= WIN10_RS2
                                BDIF_LE_CONNECTED = 0x01000000
                                BDIF_LE_CONNECTABLE = 0x02000000
                                BDIF_CONNECTION_INBOUND = 0x04000000
                                BDIF_BR_SECURE_CONNECTION_PAIRED = 0x08000000
                                BDIF_LE_SECURE_CONNECTION_PAIRED = 0x10000000
                                BDIF_VALID_FLAGS = (
                                    BDIF_ADDRESS  |
                                    BDIF_COD  |
                                    BDIF_NAME  |
                                    BDIF_PAIRED  |
                                    BDIF_PERSONAL  |
                                    BDIF_CONNECTED  |
                                    BDIF_SHORT_NAME  |
                                    BDIF_VISIBLE  |
                                    BDIF_RSSI  |
                                    BDIF_EIR  |
                                    BDIF_SSP_PAIRED  |
                                    BDIF_SSP_MITM_PROTECTED  |
                                    BDIF_BR  |
                                    BDIF_LE  |
                                    BDIF_LE_PAIRED  |
                                    BDIF_LE_PERSONAL  |
                                    BDIF_LE_MITM_PROTECTED  |
                                    BDIF_LE_PRIVACY_ENABLED  |
                                    BDIF_LE_RANDOM_ADDRESS_TYPE  |
                                    BDIF_LE_DISCOVERABLE  |
                                    BDIF_LE_NAME  |
                                    BDIF_LE_VISIBLE  |
                                    BDIF_LE_CONNECTED  |
                                    BDIF_LE_CONNECTABLE  |
                                    BDIF_CONNECTION_INBOUND  |
                                    BDIF_BR_SECURE_CONNECTION_PAIRED  |
                                    BDIF_LE_SECURE_CONNECTION_PAIRED
                                )
                            else:
                                BDIF_VALID_FLAGS = (
                                    BDIF_ADDRESS  |
                                    BDIF_COD  |
                                    BDIF_NAME  |
                                    BDIF_PAIRED  |
                                    BDIF_PERSONAL  |
                                    BDIF_CONNECTED  |
                                    BDIF_SHORT_NAME  |
                                    BDIF_VISIBLE  |
                                    BDIF_RSSI  |
                                    BDIF_EIR  |
                                    BDIF_SSP_PAIRED  |
                                    BDIF_SSP_MITM_PROTECTED  |
                                    BDIF_BR  |
                                    BDIF_LE  |
                                    BDIF_LE_PAIRED  |
                                    BDIF_LE_PERSONAL  |
                                    BDIF_LE_MITM_PROTECTED  |
                                    BDIF_LE_PRIVACY_ENABLED  |
                                    BDIF_LE_RANDOM_ADDRESS_TYPE  |
                                    BDIF_LE_DISCOVERABLE  |
                                    BDIF_LE_NAME  |
                                    BDIF_LE_VISIBLE
                                )
                            # END IF   >= WIN10_RS2
                        else:
                            BDIF_VALID_FLAGS = (
                                BDIF_ADDRESS  |
                                BDIF_COD  |
                                BDIF_NAME  |
                                BDIF_PAIRED  |
                                BDIF_PERSONAL  |
                                BDIF_CONNECTED  |
                                BDIF_SHORT_NAME  |
                                BDIF_VISIBLE  |
                                BDIF_RSSI  |
                                BDIF_EIR  |
                                BDIF_SSP_PAIRED  |
                                BDIF_SSP_MITM_PROTECTED  |
                                BDIF_BR  |
                                BDIF_LE  |
                                BDIF_LE_PAIRED  |
                                BDIF_LE_PERSONAL  |
                                BDIF_LE_MITM_PROTECTED  |
                                BDIF_LE_PRIVACY_ENABLED  |
                                BDIF_LE_RANDOM_ADDRESS_TYPE
                            )
                        # END IF   >= WIN10
                    else:
                        BDIF_VALID_FLAGS = (
                            BDIF_ADDRESS  |
                            BDIF_COD  |
                            BDIF_NAME  |
                            BDIF_PAIRED  |
                            BDIF_PERSONAL  |
                            BDIF_CONNECTED  |
                            BDIF_SHORT_NAME  |
                            BDIF_VISIBLE  |
                            BDIF_RSSI  |
                            BDIF_EIR  |
                            BDIF_SSP_PAIRED  |
                            BDIF_SSP_MITM_PROTECTED
                        )
                    # END IF   >= WIN8
                else: #  <= SP1
                    BDIF_VALID_FLAGS = (
                        BDIF_ADDRESS  |
                        BDIF_COD  |
                        BDIF_NAME  |
                        BDIF_PAIRED  |
                        BDIF_PERSONAL  |
                        BDIF_CONNECTED
                    )
                # END IF   >= SP1 + KB942567

                class _BTH_DEVICE_INFO(ctypes.Structure):
                    pass


                _BTH_DEVICE_INFO._fields_ = [
                    ('flags', ULONG), # Combination BDIF_Xxx flags
                    ('address', BTH_ADDR), # Address of remote device.
                    ('classOfDevice', BTH_COD), # Class Of Device.
                    ('name', CHAR * BTH_MAX_NAME_SIZE), # name of the device
                ]


                BTH_DEVICE_INFO = _BTH_DEVICE_INFO
                PBTH_DEVICE_INFO = POINTER(_BTH_DEVICE_INFO)


                # Buffer associated with GUID_BLUETOOTH_RADIO_IN_RANGE
                class _BTH_RADIO_IN_RANGE(ctypes.Structure):
                    pass


                _BTH_RADIO_IN_RANGE._fields_ = [
                    ('deviceInfo', BTH_DEVICE_INFO), # Information about the remote radio

                    # previousDeviceFlags, the remote radio's has just been
                    # retrieved.
                    ('previousDeviceFlags', ULONG),
                ]


                BTH_RADIO_IN_RANGE = _BTH_RADIO_IN_RANGE
                PBTH_RADIO_IN_RANGE = POINTER(_BTH_RADIO_IN_RANGE)


                # Buffer associated with GUID_BLUETOOTH_L2CAP_EVENT
                class _BTH_L2CAP_EVENT_INFO(ctypes.Structure):
                    pass


                _BTH_L2CAP_EVENT_INFO._fields_ = [

                    # Remote radio address which the L2CAP event is associated
                    # with
                    ('bthAddress', BTH_ADDR),

                    # The PSM that is either being connected to or
                    # disconnected from
                    ('psm', USHORT),
                    ('connected', UCHAR), # only be sent for channels successfully established.
                    ('initiated', UCHAR), # connect is != 0.
                ]


                BTH_L2CAP_EVENT_INFO = _BTH_L2CAP_EVENT_INFO
                PBTH_L2CAP_EVENT_INFO = POINTER(_BTH_L2CAP_EVENT_INFO)


                HCI_CONNECTION_TYPE_ACL = 1
                HCI_CONNECTION_TYPE_SCO = 2
                HCI_CONNECTION_TYPE_LE = 3

                # Fix typos
                HCI_CONNNECTION_TYPE_ACL = HCI_CONNECTION_TYPE_ACL
                HCI_CONNNECTION_TYPE_SCO = HCI_CONNECTION_TYPE_SCO

                # Buffer associated with GUID_BLUETOOTH_HCI_EVENT
                class _BTH_HCI_EVENT_INFO(ctypes.Structure):
                    pass


                _BTH_HCI_EVENT_INFO._fields_ = [

                    # Remote radio address which the HCI event is associated
                    # with
                    ('bthAddress', BTH_ADDR),
                    ('connectionType', UCHAR), # HCI_CONNNECTION_TYPE_XXX value
                    ('connected', UCHAR), # destroyed.
                ]


                BTH_HCI_EVENT_INFO = _BTH_HCI_EVENT_INFO
                PBTH_HCI_EVENT_INFO = POINTER(_BTH_HCI_EVENT_INFO)


                # Support added in KB942567

                if (
                    NTDDI_VERSION > NTDDI_VISTASP1 or
                    (NTDDI_VERSION == NTDDI_VISTASP1 and defined(VISTA_KB942567))
                ):
                    class _IO_CAPABILITY(ENUM):
                        IoCaps_DisplayOnly = 0x00
                        IoCaps_DisplayYesNo = 0x01
                        IoCaps_KeyboardOnly = 0x02
                        IoCaps_NoInputNoOutput = 0x03
                        IoCaps_Undefined = 0xFF


                    IO_CAPABILITY = _IO_CAPABILITY


                    class _AUTHENTICATION_REQUIREMENTS(ENUM):
                        MITMProtectionNotRequired = 0x00
                        MITMProtectionRequired = 0x01
                        MITMProtectionNotRequiredBonding = 0x02
                        MITMProtectionRequiredBonding = 0x03
                        MITMProtectionNotRequiredGeneralBonding = 0x04
                        MITMProtectionRequiredGeneralBonding = 0x05
                        MITMProtectionNotDefined = 0xFF


                    AUTHENTICATION_REQUIREMENTS = _AUTHENTICATION_REQUIREMENTS


                    def IsMITMProtectionRequired(requirements):
                        return requirements in (
                            AUTHENTICATION_REQUIREMENTS.MITMProtectionRequired,
                            AUTHENTICATION_REQUIREMENTS.MITMProtectionRequiredBonding,
                            AUTHENTICATION_REQUIREMENTS.MITMProtectionRequiredGeneralBonding
                        )



                # END IF   >= SP1 + KB942567

                # Max length we allow for ServiceName in the remote SDP records
                BTH_MAX_SERVICE_NAME_SIZE = 256
                MAX_UUIDS_IN_QUERY = 12
                BTH_VID_DEFAULT_VALUE = 0xFFFF
                SDP_ERROR_INVALID_SDP_VERSION = 0x0001
                SDP_ERROR_INVALID_RECORD_HANDLE = 0x0002
                SDP_ERROR_INVALID_REQUEST_SYNTAX = 0x0003
                SDP_ERROR_INVALID_PDU_SIZE = 0x0004
                SDP_ERROR_INVALID_CONTINUATION_STATE = 0x0005
                SDP_ERROR_INSUFFICIENT_RESOURCES = 0x0006

                # Defined by windows to handle server errors that are not
                # described by the

                # above errors. Start at 0x0100 so we don't go anywhere near
                # the spec

                # defined values.

                # Success, nothing went wrong
                SDP_ERROR_SUCCESS = 0x0000

                # The SDP PDU or parameters other than the SDP stream response
                # was not correct
                SDP_ERROR_SERVER_INVALID_RESPONSE = 0x0100

                # The SDP response stream did not parse correctly.
                SDP_ERROR_SERVER_RESPONSE_DID_NOT_PARSE = 0x0200

                # The SDP response stream was successfully parsed, but did not
                # match the

                # required format for the query.
                SDP_ERROR_SERVER_BAD_FORMAT = 0x0300

                # SDP was unable to send a continued query back to the server
                SDP_ERROR_COULD_NOT_SEND_CONTINUE = 0x0400

                # Server sent a response that was too large to fit in the
                # caller's buffer.
                SDP_ERROR_RESPONSE_TOO_LARGE = 0x0500
                SDP_ATTRIB_RECORD_HANDLE = 0x0000
                SDP_ATTRIB_CLASS_ID_LIST = 0x0001
                SDP_ATTRIB_RECORD_STATE = 0x0002
                SDP_ATTRIB_SERVICE_ID = 0x0003
                SDP_ATTRIB_PROTOCOL_DESCRIPTOR_LIST = 0x0004
                SDP_ATTRIB_BROWSE_GROUP_LIST = 0x0005
                SDP_ATTRIB_LANG_BASE_ATTRIB_ID_LIST = 0x0006
                SDP_ATTRIB_INFO_TIME_TO_LIVE = 0x0007
                SDP_ATTRIB_AVAILABILITY = 0x0008
                SDP_ATTRIB_PROFILE_DESCRIPTOR_LIST = 0x0009
                SDP_ATTRIB_DOCUMENTATION_URL = 0x000A
                SDP_ATTRIB_CLIENT_EXECUTABLE_URL = 0x000B
                SDP_ATTRIB_ICON_URL = 0x000C
                SDP_ATTRIB_ADDITIONAL_PROTOCOL_DESCRIPTOR_LIST = 0x000D

                # Attribute IDs in the range of 0x000D - 0x01FF are reserved
                # for future use
                SDP_ATTRIB_PROFILE_SPECIFIC = 0x0200
                LANG_BASE_LANGUAGE_INDEX = 0x0000
                LANG_BASE_ENCODING_INDEX = 0x0001
                LANG_BASE_OFFSET_INDEX = 0x0002
                LANG_DEFAULT_ID = 0x0100
                LANGUAGE_EN_US = 0x656E
                ENCODING_UTF_8 = 0x006A
                STRING_NAME_OFFSET = 0x0000
                STRING_DESCRIPTION_OFFSET = 0x0001
                STRING_PROVIDER_NAME_OFFSET = 0x0002
                SDP_ATTRIB_SDP_VERSION_NUMBER_LIST = 0x0200
                SDP_ATTRIB_SDP_DATABASE_STATE = 0x0201
                SDP_ATTRIB_BROWSE_GROUP_ID = 0x0200
                SDP_ATTRIB_CORDLESS_EXTERNAL_NETWORK = 0x0301
                SDP_ATTRIB_FAX_CLASS_1_SUPPORT = 0x0302
                SDP_ATTRIB_FAX_CLASS_2_0_SUPPORT = 0x0303
                SDP_ATTRIB_FAX_CLASS_2_SUPPORT = 0x0304
                SDP_ATTRIB_FAX_AUDIO_FEEDBACK_SUPPORT = 0x0305
                SDP_ATTRIB_HEADSET_REMOTE_AUDIO_VOLUME_CONTROL = 0x0302
                SDP_ATTRIB_LAN_LPSUBNET = 0x0200
                SDP_ATTRIB_OBJECT_PUSH_SUPPORTED_FORMATS_LIST = 0x0303
                SDP_ATTRIB_SYNCH_SUPPORTED_DATA_STORES_LIST = 0x0301

                # this is in the asINT numbers doc, but it does not show up in
                # any profile
                SDP_ATTRIB_SERVICE_VERSION = 0x0300
                SDP_ATTRIB_PAN_NETWORK_ADDRESS = 0x0306
                SDP_ATTRIB_PAN_WAP_GATEWAY = 0x0307
                SDP_ATTRIB_PAN_HOME_PAGE_URL = 0x0308
                SDP_ATTRIB_PAN_WAP_STACK_TYPE = 0x0309
                SDP_ATTRIB_PAN_SECURITY_DESCRIPTION = 0x030A
                SDP_ATTRIB_PAN_NET_ACCESS_TYPE = 0x030B
                SDP_ATTRIB_PAN_MAX_NET_ACCESS_RATE = 0x030C
                SDP_ATTRIB_IMAGING_SUPPORTED_CAPABILITIES = 0x0310
                SDP_ATTRIB_IMAGING_SUPPORTED_FEATURES = 0x0311
                SDP_ATTRIB_IMAGING_SUPPORTED_FUNCTIONS = 0x0312
                SDP_ATTRIB_IMAGING_TOTAL_DATA_CAPACITY = 0x0313
                SDP_ATTRIB_DI_SPECIFICATION_ID = 0x0200
                SDP_ATTRIB_DI_VENDOR_ID = 0x0201
                SDP_ATTRIB_DI_PRODUCT_ID = 0x0202
                SDP_ATTRIB_DI_VERSION = 0x0203
                SDP_ATTRIB_DI_PRIMARY_RECORD = 0x0204
                SDP_ATTRIB_DI_VENDOR_ID_SOURCE = 0x0205
                SDP_ATTRIB_HID_DEVICE_RELEASE_NUMBER = 0x0200
                SDP_ATTRIB_HID_PARSER_VERSION = 0x0201
                SDP_ATTRIB_HID_DEVICE_SUBCLASS = 0x0202
                SDP_ATTRIB_HID_COUNTRY_CODE = 0x0203
                SDP_ATTRIB_HID_VIRTUAL_CABLE = 0x0204
                SDP_ATTRIB_HID_RECONNECT_INITIATE = 0x0205
                SDP_ATTRIB_HID_DESCRIPTOR_LIST = 0x0206
                SDP_ATTRIB_HID_LANG_ID_BASE_LIST = 0x0207
                SDP_ATTRIB_HID_SDP_DISABLE = 0x0208
                SDP_ATTRIB_HID_BATTERY_POWER = 0x0209
                SDP_ATTRIB_HID_REMOTE_WAKE = 0x020A
                SDP_ATTRIB_HID_PROFILE_VERSION = 0x020B
                SDP_ATTRIB_HID_SUPERVISION_TIMEOUT = 0x020C
                SDP_ATTRIB_HID_NORMALLY_CONNECTABLE = 0x020D
                SDP_ATTRIB_HID_BOOT_DEVICE = 0x020E
                SDP_ATTRIB_HID_SSR_HOST_MAX_LATENCY = 0x020F
                SDP_ATTRIB_HID_SSR_HOST_MIN_TIMEOUT = 0x0210
                SDP_ATTRIB_AVRCP_SUPPORTED_FEATURES = 0x0311

                # Profile specific values
                AVRCP_SUPPORTED_FEATURES_CATEGORY_1 = 0x0001
                AVRCP_SUPPORTED_FEATURES_CATEGORY_2 = 0x0002
                AVRCP_SUPPORTED_FEATURES_CATEGORY_3 = 0x0004
                AVRCP_SUPPORTED_FEATURES_CATEGORY_4 = 0x0008
                AVRCP_SUPPORTED_FEATURES_CT_BROWSING = 0x0040
                AVRCP_SUPPORTED_FEATURES_CT_COVER_ART_IMAGE_PROPERTIES = 0x0080
                AVRCP_SUPPORTED_FEATURES_CT_COVER_ART_IMAGE = 0x0100
                AVRCP_SUPPORTED_FEATURES_CT_COVER_ART_LINKED_THUMBNAIL = 0x0200
                AVRCP_SUPPORTED_FEATURES_TG_PLAYER_APPLICATION_SETTINGS = 0x0010
                AVRCP_SUPPORTED_FEATURES_TG_GROUP_NAVIGATION = 0x0020
                AVRCP_SUPPORTED_FEATURES_TG_BROWSING = 0x0040
                AVRCP_SUPPORTED_FEATURES_TG_MULTIPLE_PLAYER_APPLICATIONS = 0x0080
                AVRCP_SUPPORTED_FEATURES_TG_COVER_ART = 0x0100
                CORDLESS_EXTERNAL_NETWORK_PSTN = 0x01
                CORDLESS_EXTERNAL_NETWORK_ISDN = 0x02
                CORDLESS_EXTERNAL_NETWORK_GSM = 0x03
                CORDLESS_EXTERNAL_NETWORK_CDMA = 0x04
                CORDLESS_EXTERNAL_NETWORK_ANALOG_CELLULAR = 0x05
                CORDLESS_EXTERNAL_NETWORK_PACKET_SWITCHED = 0x06
                CORDLESS_EXTERNAL_NETWORK_OTHER = 0x07
                OBJECT_PUSH_FORMAT_VCARD_2_1 = 0x01
                OBJECT_PUSH_FORMAT_VCARD_3_0 = 0x02
                OBJECT_PUSH_FORMAT_VCAL_1_0 = 0x03
                OBJECT_PUSH_FORMAT_ICAL_2_0 = 0x04
                OBJECT_PUSH_FORMAT_VNOTE = 0x05
                OBJECT_PUSH_FORMAT_VMESSAGE = 0x06
                OBJECT_PUSH_FORMAT_ANY = 0xFF
                SYNCH_DATA_STORE_PHONEBOOK = 0x01
                SYNCH_DATA_STORE_CALENDAR = 0x03
                SYNCH_DATA_STORE_NOTES = 0x05
                SYNCH_DATA_STORE_MESSAGES = 0x06
                DI_VENDOR_ID_SOURCE_BLUETOOTH_SIG = 0x0001
                DI_VENDOR_ID_SOURCE_USB_IF = 0x0002
                PSM_SDP = 0x0001
                PSM_RFCOMM = 0x0003
                PSM_TCS_BIN = 0x0005
                PSM_TCS_BIN_CORDLESS = 0x0007
                PSM_BNEP = 0x000F
                PSM_HID_CONTROL = 0x0011
                PSM_HID_INTERRUPT = 0x0013
                PSM_UPNP = 0x0015
                PSM_AVCTP = 0x0017
                PSM_AVDTP = 0x0019
                PSM_AVCTP_BROWSE = 0x001B
                PSM_UDI_C_PLANE = 0x001D
                PSM_ATT = 0x001F
                PSM_3DSP = 0x0021
                PSM_LE_IPSP = 0x0023

                # Strings
                STR_ADDR_FMTA = "(%02x:%02x:%02x:%02x:%02x:%02x)"
                STR_ADDR_FMTW = "(%02x:%02x:%02x:%02x:%02x:%02x)"
                STR_ADDR_SHORT_FMTA = "%04x%08x"
                STR_ADDR_SHORT_FMTW = "%04x%08x"
                STR_USBHCI_CLASS_HARDWAREIDA = "USB\\Class_E0 & SubClass_01 & Prot_01"
                STR_USBHCI_CLASS_HARDWAREIDW = "USB\\Class_E0 & SubClass_01 & Prot_01"

                BTH_KERN = None

                if defined(UNICODE) or defined(BTH_KERN):
                    STR_ADDR_FMT = STR_ADDR_FMTW
                    STR_ADDR_SHORT_FMT = STR_ADDR_SHORT_FMTW
                    STR_USBHCI_CLASS_HARDWAREID = STR_USBHCI_CLASS_HARDWAREIDW
                else: #  UNICODE
                    STR_ADDR_FMT = STR_ADDR_FMTA
                    STR_ADDR_SHORT_FMT = STR_ADDR_SHORT_FMTA
                    STR_USBHCI_CLASS_HARDWAREID = STR_USBHCI_CLASS_HARDWAREIDA
                # END IF   UNICODE


                def GET_BITS(field, offset, mask):
                    return (field >> offset) & mask


                def GET_BIT(field, offset):
                    return GET_BITS(field, offset, 0x1)


                def LMP_3_SLOT_PACKETS(x):
                    return GET_BIT(x, 0)


                def LMP_5_SLOT_PACKETS(x):
                    return GET_BIT(x, 1)


                def LMP_ENCRYPTION(x):
                    return GET_BIT(x, 2)


                def LMP_SLOT_OFFSET(x):
                    return GET_BIT(x, 3)


                def LMP_TIMING_ACCURACY(x):
                    return GET_BIT(x, 4)


                def LMP_SWITCH(x):
                    return GET_BIT(x, 5)


                def LMP_HOLD_MODE(x):
                    return GET_BIT(x, 6)


                def LMP_SNIFF_MODE(x):
                    return GET_BIT(x, 7)


                def LMP_PARK_MODE(x):
                    return GET_BIT(x, 8)


                def LMP_RSSI(x):
                    return GET_BIT(x, 9)


                def LMP_CHANNEL_QUALITY_DRIVEN_MODE(x):
                    return GET_BIT(x, 10)


                def LMP_SCO_LINK(x):
                    return GET_BIT(x, 11)


                def LMP_HV2_PACKETS(x):
                    return GET_BIT(x, 12)


                def LMP_HV3_PACKETS(x):
                    return GET_BIT(x, 13)


                def LMP_MU_LAW_LOG(x):
                    return GET_BIT(x, 14)


                def LMP_A_LAW_LOG(x):
                    return GET_BIT(x, 15)


                def LMP_CVSD(x):
                    return GET_BIT(x, 16)


                def LMP_PAGING_SCHEME(x):
                    return GET_BIT(x, 17)


                def LMP_POWER_CONTROL(x):
                    return GET_BIT(x, 18)


                def LMP_TRANSPARENT_SCO_DATA(x):
                    return GET_BIT(x, 19)


                def LMP_FLOW_CONTROL_LAG(x):
                    return GET_BITS(x, 20, 0x3)


                def LMP_BROADCAST_ENCRYPTION(x):
                    return GET_BIT(x, 23)


                def LMP_ENHANCED_DATA_RATE_ACL_2MBPS_MODE(x):
                    return GET_BIT(x, 25)


                def LMP_ENHANCED_DATA_RATE_ACL_3MBPS_MODE(x):
                    return GET_BIT(x, 26)


                def LMP_ENHANCED_INQUIRY_SCAN(x):
                    return GET_BIT(x, 27)


                def LMP_INTERLACED_INQUIRY_SCAN(x):
                    return GET_BIT(x, 28)


                def LMP_INTERLACED_PAGE_SCAN(x):
                    return GET_BIT(x, 29)


                def LMP_RSSI_WITH_INQUIRY_RESULTS(x):
                    return GET_BIT(x, 30)


                def LMP_ESCO_LINK(x):
                    return GET_BIT(x, 31)


                def LMP_EV4_PACKETS(x):
                    return GET_BIT(x, 32)


                def LMP_EV5_PACKETS(x):
                    return GET_BIT(x, 33)


                def LMP_AFH_CAPABLE_SLAVE(x):
                    return GET_BIT(x, 35)


                def LMP_AFH_CLASSIFICATION_SLAVE(x):
                    return GET_BIT(x, 36)


                def LMP_BR_EDR_NOT_SUPPORTED(x):
                    return GET_BIT(x, 37)


                def LMP_LE_SUPPORTED(x):
                    return GET_BIT(x, 38)


                def LMP_3SLOT_EDR_ACL_PACKETS(x):
                    return GET_BIT(x, 39)


                def LMP_5SLOT_EDR_ACL_PACKETS(x):
                    return GET_BIT(x, 40)


                def LMP_SNIFF_SUBRATING(x):
                    return GET_BIT(x, 41)


                def LMP_PAUSE_ENCRYPTION(x):
                    return GET_BIT(x, 42)


                def LMP_AFH_CAPABLE_MASTER(x):
                    return GET_BIT(x, 43)


                def LMP_AFH_CLASSIFICATION_MASTER(x):
                    return GET_BIT(x, 44)


                def LMP_EDR_ESCO_2MBPS_MODE(x):
                    return GET_BIT(x, 45)


                def LMP_EDR_ESCO_3MBPS_MODE(x):
                    return GET_BIT(x, 46)


                def LMP_3SLOT_EDR_ESCO_PACKETS(x):
                    return GET_BIT(x, 47)


                def LMP_EXTENDED_INQUIRY_RESPONSE(x):
                    return GET_BIT(x, 48)


                def LMP_SIMULT_LE_BR_TO_SAME_DEV(x):
                    return GET_BIT(x, 49)


                def LMP_SECURE_SIMPLE_PAIRING(x):
                    return GET_BIT(x, 51)


                def LMP_ENCAPSULATED_PDU(x):
                    return GET_BIT(x, 52)


                def LMP_ERRONEOUS_DATA_REPORTING(x):
                    return GET_BIT(x, 53)


                def LMP_NON_FLUSHABLE_PACKET_BOUNDARY_FLAG(x):
                    return GET_BIT(x, 54)


                def LMP_LINK_SUPERVISION_TIMEOUT_CHANGED_EVENT(x):
                    return GET_BIT(x, 56)


                def LMP_INQUIRY_RESPONSE_TX_POWER_LEVEL(x):
                    return GET_BIT(x, 57)


                def LMP_EXTENDED_FEATURES(x):
                    return GET_BIT(x, 63)


            # END IF   GUID_DEFS_ONLY
        # END IF   (NTDDI_VERSION >= NTDDI_WINXPSP2)

        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __BTHDEF_H__
