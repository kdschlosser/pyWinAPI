from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# wdmguid.h Abstract: Defines GUIDs for function device classes and device
# events used in Plug & Play. Revision History: - -

from pyWinAPI.shared.winapifamily_h import * # NOQA

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    if not defined(FAR):
        FAR = 1
    # END IF
    # Device events that can be broadcasted to drivers and user - mode apps.
    if NTDDI_VERSION >= NTDDI_WIN2K:
        GUID_HWPROFILE_QUERY_CHANGE = DEFINE_GUID(
            0xCB3A4001,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_HWPROFILE_CHANGE_CANCELLED = DEFINE_GUID(
            0xCB3A4002,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_HWPROFILE_CHANGE_COMPLETE = DEFINE_GUID(
            0xCB3A4003,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_DEVICE_INTERFACE_ARRIVAL = DEFINE_GUID(
            0xCB3A4004,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_DEVICE_INTERFACE_REMOVAL = DEFINE_GUID(
            0xCB3A4005,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_TARGET_DEVICE_QUERY_REMOVE = DEFINE_GUID(
            0xCB3A4006,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_TARGET_DEVICE_REMOVE_CANCELLED = DEFINE_GUID(
            0xCB3A4007,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_TARGET_DEVICE_REMOVE_COMPLETE = DEFINE_GUID(
            0xCB3A4008,
            0x46F0,
            0x11D0,
            0xB0,
            0x8F,
            0x00,
            0x60,
            0x97,
            0x13,
            0x05,
            0x3F
        )
        GUID_PNP_CUSTOM_NOTIFICATION = DEFINE_GUID(
            0xACA73F8E,
            0x8D23,
            0x11D1,
            0xAC,
            0x7D,
            0x00,
            0x00,
            0xF8,
            0x75,
            0x71,
            0xD0
        )
        GUID_PNP_POWER_NOTIFICATION = DEFINE_GUID(
            0xC2CF0660,
            0xEB7A,
            0x11D1,
            0xBD,
            0x7F,
            0x00,
            0x00,
            0xF8,
            0x75,
            0x71,
            0xD0
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        GUID_PNP_POWER_SETTING_CHANGE = DEFINE_GUID(
            0x29C69B3E,
            0xC79A,
            0x43BF,
            0xBB,
            0xDE,
            0xA9,
            0x32,
            0xFA,
            0x1B,
            0xEA,
            0x7E
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        GUID_TARGET_DEVICE_TRANSPORT_RELATIONS_CHANGED = DEFINE_GUID(
            0xFCF528F6,
            0xA82F,
            0x47B1,
            0xAD,
            0x3A,
            0x80,
            0x50,
            0x59,
            0x4C,
            0xAD,
            0x28
        )
    # END IF
    # Interface GUIDs used for IRP_MN_QUERY_INTERFACE
    if NTDDI_VERSION >= NTDDI_WIN2K:
        GUID_BUS_INTERFACE_STANDARD = DEFINE_GUID(
            0x496B8280,
            0x6F25,
            0x11D0,
            0xBE,
            0xAF,
            0x08,
            0x00,
            0x2B,
            0xE2,
            0x09,
            0x2F
        )
        GUID_PCI_BUS_INTERFACE_STANDARD = DEFINE_GUID(
            0x496B8281,
            0x6F25,
            0x11D0,
            0xBE,
            0xAF,
            0x08,
            0x00,
            0x2B,
            0xE2,
            0x09,
            0x2F
        )
        GUID_PCI_BUS_INTERFACE_STANDARD2 = DEFINE_GUID(
            0xDE94E966,
            0xFDFF,
            0x4C9C,
            0x99,
            0x98,
            0x67,
            0x47,
            0xB1,
            0x50,
            0xE7,
            0x4C
        )
        GUID_ARBITER_INTERFACE_STANDARD = DEFINE_GUID(
            0xE644F185,
            0x8C0E,
            0x11D0,
            0xBE,
            0xCF,
            0x08,
            0x00,
            0x2B,
            0xE2,
            0x09,
            0x2F
        )
        GUID_TRANSLATOR_INTERFACE_STANDARD = DEFINE_GUID(
            0x6C154A92,
            0xAACF,
            0x11D0,
            0x8D,
            0x2A,
            0x00,
            0xA0,
            0xC9,
            0x06,
            0xB2,
            0x44
        )
        GUID_ACPI_INTERFACE_STANDARD = DEFINE_GUID(
            0xB091A08A,
            0xBA97,
            0x11D0,
            0xBD,
            0x14,
            0x00,
            0xAA,
            0x00,
            0xB7,
            0xB3,
            0x2A
        )
        GUID_INT_ROUTE_INTERFACE_STANDARD = DEFINE_GUID(
            0x70941BF4,
            0x0073,
            0x11D1,
            0xA0,
            0x9E,
            0x00,
            0xC0,
            0x4F,
            0xC3,
            0x40,
            0xB1
        )
        GUID_PCMCIA_BUS_INTERFACE_STANDARD = DEFINE_GUID(
            0x76173AF0,
            0xC504,
            0x11D1,
            0x94,
            0x7F,
            0x00,
            0xC0,
            0x4F,
            0xB9,
            0x60,
            0xEE
        )
        GUID_ACPI_REGS_INTERFACE_STANDARD = DEFINE_GUID(
            0x06141966,
            0x7245,
            0x6369,
            0x46,
            0x2E,
            0x4E,
            0x65,
            0x6C,
            0x73,
            0x6F,
            0x6E
        )
        GUID_LEGACY_DEVICE_DETECTION_STANDARD = DEFINE_GUID(
            0x50FEB0DE,
            0x596A,
            0x11D2,
            0xA5,
            0xB8,
            0x00,
            0x00,
            0xF8,
            0x1A,
            0x46,
            0x19
        )
        GUID_PCI_DEVICE_PRESENT_INTERFACE = DEFINE_GUID(
            0xD1B82C26,
            0xBF49,
            0x45EF,
            0xB2,
            0x16,
            0x71,
            0xCB,
            0xD7,
            0x88,
            0x9B,
            0x57
        )
        GUID_MF_ENUMERATION_INTERFACE = DEFINE_GUID(
            0xAEB895F0,
            0x5586,
            0x11D1,
            0x8D,
            0x84,
            0x00,
            0xA0,
            0xC9,
            0x06,
            0xB2,
            0x44
        )
        GUID_REENUMERATE_SELF_INTERFACE_STANDARD = DEFINE_GUID(
            0x2AEB0243,
            0x6A6E,
            0x486B,
            0x82,
            0xFC,
            0xD8,
            0x15,
            0xF6,
            0xB9,
            0x70,
            0x06
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        GUID_AGP_TARGET_BUS_INTERFACE_STANDARD = DEFINE_GUID(
            0xB15CFCE8,
            0x06D1,
            0x4D37,
            0x9D,
            0x4C,
            0xBE,
            0xDD,
            0xE0,
            0xC2,
            0xA6,
            0xFF
        )
        GUID_ACPI_CMOS_INTERFACE_STANDARD = DEFINE_GUID(
            0x3A8D0384,
            0x6505,
            0x40CA,
            0xBC,
            0x39,
            0x56,
            0xC1,
            0x5F,
            0x8C,
            0x5F,
            0xED
        )
        GUID_ACPI_PORT_RANGES_INTERFACE_STANDARD = DEFINE_GUID(
            0xF14F609B,
            0xCBBD,
            0x4957,
            0xA6,
            0x74,
            0xBC,
            0x0,
            0x21,
            0x3F,
            0x1C,
            0x97
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_VISTA:
        GUID_ACPI_INTERFACE_STANDARD2 = DEFINE_GUID(
            0xE8695F63,
            0x1831,
            0x4870,
            0xA8,
            0xCF,
            0x9C,
            0x2F,
            0x03,
            0xF9,
            0xDC,
            0xB5
        )
        GUID_PNP_LOCATION_INTERFACE = DEFINE_GUID(
            0x70211B0E,
            0x0AFB,
            0x47DB,
            0xAF,
            0xC1,
            0x41,
            0x0B,
            0xF8,
            0x42,
            0x49,
            0x7A
        )
        GUID_PCI_EXPRESS_LINK_QUIESCENT_INTERFACE = DEFINE_GUID(
            0x146CD41C,
            0xDAE3,
            0x4437,
            0x8A,
            0xFF,
            0x2A,
            0xF3,
            0xF0,
            0x38,
            0x09,
            0x9B
        )
        GUID_PCI_EXPRESS_ROOT_PORT_INTERFACE = DEFINE_GUID(
            0x83A7734A,
            0x84C7,
            0x4161,
            0x9A,
            0x98,
            0x60,
            0x00,
            0xED,
            0x0C,
            0x4A,
            0x33
        )
        GUID_MSIX_TABLE_CONFIG_INTERFACE = DEFINE_GUID(
            0x1A6A460B,
            0x194F,
            0x455D,
            0xB3,
            0x4B,
            0xB8,
            0x4C,
            0x5B,
            0x05,
            0x71,
            0x2B
        )
        GUID_D3COLD_SUPPORT_INTERFACE = DEFINE_GUID(
            0xB38290E5,
            0x3CD0,
            0x4F9D,
            0x99,
            0x37,
            0xF5,
            0xFE,
            0x2B,
            0x44,
            0xD4,
            0x7A
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN7:
        GUID_PROCESSOR_PCC_INTERFACE_STANDARD = DEFINE_GUID(
            0x37B17E9A,
            0xC21C,
            0x4296,
            0x97,
            0x2D,
            0x11,
            0xC4,
            0xB3,
            0x2B,
            0x28,
            0xF0
        )
        GUID_PCI_VIRTUALIZATION_INTERFACE = DEFINE_GUID(
            0x64897B47,
            0x3A4A,
            0x4D75,
            0xBC,
            0x74,
            0x89,
            0xDD,
            0x6C,
            0x7,
            0x82,
            0x93
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        GUID_PCC_INTERFACE_STANDARD = DEFINE_GUID(
            0x3EE8BA63,
            0x0F59,
            0x4A24,
            0x8A,
            0x45,
            0x35,
            0x80,
            0x8B,
            0xDD,
            0x12,
            0x49
        )
        GUID_PCC_INTERFACE_INTERNAL = DEFINE_GUID(
            0x7CCE62CE,
            0xC189,
            0x4814,
            0xA6,
            0xA7,
            0x12,
            0x11,
            0x20,
            0x89,
            0xE9,
            0x38
        )
        GUID_THERMAL_COOLING_INTERFACE = DEFINE_GUID(
            0xECBE47A8,
            0xC498,
            0x4BB9,
            0xBD,
            0x70,
            0xE8,
            0x67,
            0xE0,
            0x94,
            0x0D,
            0x22
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WINTHRESHOLD:
        GUID_DMA_CACHE_COHERENCY_INTERFACE = DEFINE_GUID(
            0xB520F7FA,
            0x8A5A,
            0x4E40,
            0xA3,
            0xF6,
            0x6B,
            0xE1,
            0xE1,
            0x62,
            0xD9,
            0x35
        )
        GUID_DEVICE_RESET_INTERFACE_STANDARD = DEFINE_GUID(
            0x649FDF26,
            0x3BC0,
            0x4813,
            0xAD,
            0x24,
            0x7E,
            0xC,
            0x1E,
            0xDA,
            0x3F,
            0xA3
        )
        GUID_IOMMU_BUS_INTERFACE = DEFINE_GUID(
            0x1EFEE0B2,
            0xD278,
            0x4AE4,
            0xBD,
            0xDC,
            0x1B,
            0x34,
            0xDD,
            0x64,
            0x80,
            0x43
        )
        GUID_PCI_SECURITY_INTERFACE = DEFINE_GUID(
            0x6E7F1451,
            0x199E,
            0x4ACC,
            0xBA,
            0x2D,
            0x76,
            0x2B,
            0x4E,
            0xDF,
            0x46,
            0x74
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_TH2:
        GUID_SCM_BUS_INTERFACE = DEFINE_GUID(
            0x25944783,
            0xCE79,
            0x4232,
            0x81,
            0x5E,
            0x4A,
            0x30,
            0x1,
            0x4E,
            0x8E,
            0xB4
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_RS2:
        GUID_SECURE_DRIVER_INTERFACE = DEFINE_GUID(
            0x370F67E1,
            0x4FF5,
            0x4A94,
            0x9A,
            0x35,
            0x6,
            0xC5,
            0xD9,
            0xCC,
            0x30,
            0xE2
        )
        GUID_SDEV_IDENTIFIER_INTERFACE = DEFINE_GUID(
            0x49D67AF8,
            0x916C,
            0x4EE8,
            0x9D,
            0xF1,
            0x88,
            0x9F,
            0x17,
            0xD2,
            0x1E,
            0x91
        )
        GUID_SCM_BUS_NVD_INTERFACE = DEFINE_GUID(
            0x8DE064FF,
            0xB630,
            0x42E4,
            0x88,
            0xEA,
            0x6F,
            0x24,
            0xC8,
            0x64,
            0x11,
            0x75
        )
        GUID_SCM_BUS_LD_INTERFACE = DEFINE_GUID(
            0x9B89307D,
            0xD76B,
            0x4F48,
            0xB1,
            0x86,
            0x54,
            0x4,
            0x1A,
            0xE9,
            0x2E,
            0x8D
        )
        GUID_SCM_PHYSICAL_NVDIMM_INTERFACE = DEFINE_GUID(
            0x79C21B,
            0x917E,
            0x405E,
            0xA9,
            0xCE,
            0x7,
            0x32,
            0xB5,
            0xBB,
            0xCE,
            0xBD
        )
        GUID_PNP_EXTENDED_ADDRESS_INTERFACE = DEFINE_GUID(
            0xB8E992EC,
            0xA797,
            0x4DC4,
            0x88,
            0x46,
            0x84,
            0xD0,
            0x41,
            0x70,
            0x74,
            0x46
        )
    # END IF
    # TODO_NTDDI_WIN10_RS4
    if NTDDI_VERSION >= NTDDI_WIN10_RS3:
        GUID_D3COLD_AUX_POWER_AND_TIMING_INTERFACE = DEFINE_GUID(
            0x44D8AA,
            0xF664,
            0x4588,
            0x9F,
            0xFC,
            0x2A,
            0xFE,
            0xAF,
            0x59,
            0x50,
            0xB9
        )
        GUID_PCI_FPGA_CONTROL_INTERFACE = DEFINE_GUID(
            0x2DF3F7A8,
            0xB9B3,
            0x4063,
            0x92,
            0x15,
            0xB5,
            0xD1,
            0x4A,
            0x0B,
            0x26,
            0x6E
        )
    # END IF
    # Bus type GUIDs
    if NTDDI_VERSION >= NTDDI_WIN2K:
        GUID_BUS_TYPE_INTERNAL = DEFINE_GUID(
            0x1530EA73,
            0x086B,
            0x11D1,
            0xA0,
            0x9F,
            0x00,
            0xC0,
            0x4F,
            0xC3,
            0x40,
            0xB1
        )
        GUID_BUS_TYPE_PCMCIA = DEFINE_GUID(
            0x09343630,
            0xAF9F,
            0x11D0,
            0x92,
            0xE9,
            0x00,
            0x00,
            0xF8,
            0x1E,
            0x1B,
            0x30
        )
        GUID_BUS_TYPE_PCI = DEFINE_GUID(
            0xC8EBDFB0,
            0xB510,
            0x11D0,
            0x80,
            0xE5,
            0x00,
            0xA0,
            0xC9,
            0x25,
            0x42,
            0xE3
        )
        GUID_BUS_TYPE_ISAPNP = DEFINE_GUID(
            0xE676F854,
            0xD87D,
            0x11D0,
            0x92,
            0xB2,
            0x00,
            0xA0,
            0xC9,
            0x05,
            0x5F,
            0xC5
        )
        GUID_BUS_TYPE_EISA = DEFINE_GUID(
            0xDDC35509,
            0xF3FC,
            0x11D0,
            0xA5,
            0x37,
            0x00,
            0x00,
            0xF8,
            0x75,
            0x3E,
            0xD1
        )
        GUID_BUS_TYPE_MCA = DEFINE_GUID(
            0x1C75997A,
            0xDC33,
            0x11D0,
            0x92,
            0xB2,
            0x00,
            0xA0,
            0xC9,
            0x05,
            0x5F,
            0xC5
        )
        GUID_BUS_TYPE_SERENUM = DEFINE_GUID(
            0x77114A87,
            0x8944,
            0x11D1,
            0xBD,
            0x90,
            0x00,
            0xA0,
            0xC9,
            0x06,
            0xBE,
            0x2D
        )
        GUID_BUS_TYPE_USB = DEFINE_GUID(
            0x9D7DEBBC,
            0xC85D,
            0x11D1,
            0x9E,
            0xB4,
            0x00,
            0x60,
            0x08,
            0xC3,
            0xA1,
            0x9A
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WINXP:
        GUID_BUS_TYPE_LPTENUM = DEFINE_GUID(
            0xC4CA1000,
            0x2DDC,
            0x11D5,
            0xA1,
            0x7A,
            0x00,
            0xC0,
            0x4F,
            0x60,
            0x52,
            0x4D
        )
        GUID_BUS_TYPE_USBPRINT = DEFINE_GUID(
            0x441EE000,
            0x4342,
            0x11D5,
            0xA1,
            0x84,
            0x00,
            0xC0,
            0x4F,
            0x60,
            0x52,
            0x4D
        )
        GUID_BUS_TYPE_DOT4PRT = DEFINE_GUID(
            0x441EE001,
            0x4342,
            0x11D5,
            0xA1,
            0x84,
            0x00,
            0xC0,
            0x4F,
            0x60,
            0x52,
            0x4D
        )
        GUID_BUS_TYPE_1394 = DEFINE_GUID(
            0xF74E73EB,
            0x9AC5,
            0x45EB,
            0xBE,
            0x4D,
            0x77,
            0x2C,
            0xC7,
            0x1D,
            0xDF,
            0xB3
        )
        GUID_BUS_TYPE_HID = DEFINE_GUID(
            0xEEAF37D0,
            0x1963,
            0x47C4,
            0xAA,
            0x48,
            0x72,
            0x47,
            0x6D,
            0xB7,
            0xCF,
            0x49
        )
        GUID_BUS_TYPE_AVC = DEFINE_GUID(
            0xC06FF265,
            0xAE09,
            0x48F0,
            0x81,
            0x2C,
            0x16,
            0x75,
            0x3D,
            0x7C,
            0xBA,
            0x83
        )
        GUID_BUS_TYPE_IRDA = DEFINE_GUID(
            0x7AE17DC1,
            0xC944,
            0x44D6,
            0x88,
            0x1F,
            0x4C,
            0x2E,
            0x61,
            0x05,
            0x3B,
            0xC1
        )
        GUID_BUS_TYPE_SD = DEFINE_GUID(
            0xE700CC04,
            0x4036,
            0x4E89,
            0x95,
            0x79,
            0x89,
            0xEB,
            0xF4,
            0x5F,
            0x00,
            0xCD
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN8:
        GUID_BUS_TYPE_ACPI = DEFINE_GUID(
            0xD7B46895,
            0x001A,
            0x4942,
            0x89,
            0x1F,
            0xA7,
            0xD4,
            0x66,
            0x10,
            0xA8,
            0x43
        )
        GUID_BUS_TYPE_SW_DEVICE = DEFINE_GUID(
            0x06D10322,
            0x7DE0,
            0x4CEF,
            0x8E,
            0x25,
            0x19,
            0x7D,
            0x0E,
            0x74,
            0x42,
            0xE2
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WIN10_TH2:
        GUID_BUS_TYPE_SCM = DEFINE_GUID(
            0x375A5912,
            0x804C,
            0x45AA,
            0xBD,
            0xC2,
            0xFD,
            0xD2,
            0x5A,
            0x1D,
            0x95,
            0x12
        )
    # END IF
    # Power management WMI guids for device control
    if NTDDI_VERSION >= NTDDI_WIN2K:
        GUID_POWER_DEVICE_ENABLE = DEFINE_GUID(
            0x827C0A6F,
            0xFEB0,
            0x11D0,
            0xBD,
            0x26,
            0x00,
            0xAA,
            0x00,
            0xB7,
            0xB3,
            0x2A
        )
        GUID_POWER_DEVICE_TIMEOUTS = DEFINE_GUID(
            0xA45DA735,
            0xFEB0,
            0x11D0,
            0xBD,
            0x26,
            0x00,
            0xAA,
            0x00,
            0xB7,
            0xB3,
            0x2A
        )
        GUID_POWER_DEVICE_WAKE_ENABLE = DEFINE_GUID(
            0xA9546A82,
            0xFEB0,
            0x11D0,
            0xBD,
            0x26,
            0x00,
            0xAA,
            0x00,
            0xB7,
            0xB3,
            0x2A
        )
    # END IF
    # User - Mode Driver Framework device events for detecting driver host
    # crashes.
    if NTDDI_VERSION >= NTDDI_WINXP:
        GUID_WUDF_DEVICE_HOST_PROBLEM = DEFINE_GUID(
            0xC43D25BD,
            0x9346,
            0x40EE,
            0xA2,
            0xD2,
            0xD7,
            0x0C,
            0x15,
            0xF8,
            0xB7,
            0x5B
        )
    # END IF
    # Dynamic partitioning replace interface.
    if NTDDI_VERSION >= NTDDI_VISTA:
        GUID_PARTITION_UNIT_INTERFACE_STANDARD = DEFINE_GUID(
            0x52363F5B,
            0xD891,
            0x429B,
            0x81,
            0x95,
            0xAE,
            0xC5,
            0xFE,
            0xF6,
            0x85,
            0x3C
        )
    # END IF
    if NTDDI_VERSION >= NTDDI_WINBLUE:
        GUID_QUERY_CRASHDUMP_FUNCTIONS = DEFINE_GUID(
            0x9CC6B8FF,
            0x32E2,
            0x4834,
            0xB1,
            0xDE,
            0xB3,
            0x2E,
            0xF8,
            0x88,
            0x0A,
            0x4B
        )
    # END IF# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
