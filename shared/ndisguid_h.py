from pyWinAPI import *
from pyWinAPI.shared.guiddef_h import *


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# ndisguid.h Abstract: GUID definitions for NDIS objects. Environment:
# User/Kernel mode Revision History: - -
from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # Guid for Lan Class.
    GUID_NDIS_LAN_CLASS = DEFINE_GUID(
        0xAD498944,
        0x762F,
        0x11D0,
        0x8D,
        0xCB,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_DEVINTERFACE_NET = DEFINE_GUID(
        0xCAC88484,
        0x7515,
        0x4C03,
        0x82,
        0xE6,
        0x71,
        0xA8,
        0x7A,
        0xBA,
        0xC3,
        0x61
    )
    UNSPECIFIED_NETWORK_GUID = DEFINE_GUID(
        0x12BA5BDE,
        0x143E,
        0x4C0D,
        0xB6,
        0x6D,
        0x23,
        0x79,
        0xBB,
        0x14,
        0x19,
        0x13
    )

    # NDIS global GUIDs
    GUID_NDIS_ENUMERATE_ADAPTER = DEFINE_GUID(
        0x981F2D7F,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_NOTIFY_ADAPTER_REMOVAL = DEFINE_GUID(
        0x981F2D80,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_NOTIFY_ADAPTER_ARRIVAL = DEFINE_GUID(
        0x981F2D81,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_ENUMERATE_VC = DEFINE_GUID(
        0x981F2D82,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_NOTIFY_VC_REMOVAL = DEFINE_GUID(
        0x981F2D79,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_NOTIFY_VC_ARRIVAL = DEFINE_GUID(
        0x182F9E0C,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_NOTIFY_BIND = DEFINE_GUID(
        0x5413531C,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_NOTIFY_UNBIND = DEFINE_GUID(
        0x6E3CE1EC,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_WAKE_ON_MAGIC_PACKET_ONLY = DEFINE_GUID(
        0xA14F1C97,
        0x8839,
        0x4F8A,
        0x99,
        0x96,
        0xA2,
        0x89,
        0x96,
        0xEB,
        0xBF,
        0x1D
    )
    GUID_NDIS_NOTIFY_DEVICE_POWER_ON = DEFINE_GUID(
        0x5F81CFD0,
        0xF046,
        0x4342,
        0xAF,
        0x61,
        0x89,
        0x5A,
        0xCE,
        0xDA,
        0xEF,
        0xD9
    )
    GUID_NDIS_NOTIFY_DEVICE_POWER_OFF = DEFINE_GUID(
        0x81BC8189,
        0xB026,
        0x46AB,
        0xB9,
        0x64,
        0xF1,
        0x82,
        0xE3,
        0x42,
        0x93,
        0x4E
    )
    GUID_NDIS_NOTIFY_FILTER_REMOVAL = DEFINE_GUID(
        0x1F177CD9,
        0x5955,
        0x4721,
        0x9F,
        0x6A,
        0x78,
        0xEB,
        0xDF,
        0xAE,
        0xF8,
        0x89
    )
    GUID_NDIS_NOTIFY_FILTER_ARRIVAL = DEFINE_GUID(
        0x0B6D3C89,
        0x5917,
        0x43CA,
        0xB5,
        0x78,
        0xD0,
        0x1A,
        0x79,
        0x67,
        0xC4,
        0x1C
    )
    GUID_NDIS_NOTIFY_DEVICE_POWER_ON_EX = DEFINE_GUID(
        0x2B440188,
        0x92AC,
        0x4F60,
        0x9B,
        0x2D,
        0x20,
        0xA3,
        0x0C,
        0xBB,
        0x6B,
        0xBE
    )
    GUID_NDIS_NOTIFY_DEVICE_POWER_OFF_EX = DEFINE_GUID(
        0x4159353C,
        0x5CD7,
        0x42CE,
        0x8F,
        0xE4,
        0xA4,
        0x5A,
        0x23,
        0x80,
        0xCC,
        0x4F
    )

    # {1528D111 - 708A - 4ca4 - 9215 - C05771161CDA} - used with
    # NDIS_WMI_PM_ADMIN_CONFIG
    GUID_NDIS_PM_ADMIN_CONFIG = DEFINE_GUID(
        0x1528D111,
        0x708A,
        0x4CA4,
        0x92,
        0x15,
        0xC0,
        0x57,
        0x71,
        0x16,
        0x1C,
        0xDA
    )

    # {B2CF76E3 - B3AE - 4394 - A01F - 338C9870E939} - use with
    # NDIS_WMI_PM_ACTIVE_CAPABILITIES
    GUID_NDIS_PM_ACTIVE_CAPABILITIES = DEFINE_GUID(
        0xB2CF76E3,
        0xB3AE,
        0x4394,
        0xA0,
        0x1F,
        0x33,
        0x8C,
        0x98,
        0x70,
        0xE9,
        0x39
    )
    GUID_NDIS_RSS_ENABLED = DEFINE_GUID(
        0x9565CD55,
        0x3402,
        0x4E32,
        0xA5,
        0xB6,
        0x2F,
        0x14,
        0x3F,
        0x2F,
        0x2C,
        0x30
    )

    # GUIDs for General OIDs
    GUID_NDIS_GEN_HARDWARE_STATUS = DEFINE_GUID(
        0x5EC10354,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MEDIA_SUPPORTED = DEFINE_GUID(
        0x5EC10355,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MEDIA_IN_USE = DEFINE_GUID(
        0x5EC10356,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MAXIMUM_LOOKAHEAD = DEFINE_GUID(
        0x5EC10357,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MAXIMUM_FRAME_SIZE = DEFINE_GUID(
        0x5EC10358,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_LINK_SPEED = DEFINE_GUID(
        0x5EC10359,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_TRANSMIT_BUFFER_SPACE = DEFINE_GUID(
        0x5EC1035A,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_RECEIVE_BUFFER_SPACE = DEFINE_GUID(
        0x5EC1035B,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_TRANSMIT_BLOCK_SIZE = DEFINE_GUID(
        0x5EC1035C,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_RECEIVE_BLOCK_SIZE = DEFINE_GUID(
        0x5EC1035D,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_VENDOR_ID = DEFINE_GUID(
        0x5EC1035E,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_VENDOR_DESCRIPTION = DEFINE_GUID(
        0x5EC1035F,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CURRENT_PACKET_FILTER = DEFINE_GUID(
        0x5EC10360,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CURRENT_LOOKAHEAD = DEFINE_GUID(
        0x5EC10361,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_DRIVER_VERSION = DEFINE_GUID(
        0x5EC10362,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MAXIMUM_TOTAL_SIZE = DEFINE_GUID(
        0x5EC10363,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MAC_OPTIONS = DEFINE_GUID(
        0x5EC10365,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MEDIA_CONNECT_STATUS = DEFINE_GUID(
        0x5EC10366,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_MAXIMUM_SEND_PACKETS = DEFINE_GUID(
        0x5EC10367,
        0xA61A,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_VENDOR_DRIVER_VERSION = DEFINE_GUID(
        0x447956F9,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_VLAN_ID = DEFINE_GUID(
        0x765DC702,
        0xC5E8,
        0x4B67,
        0x84,
        0x3B,
        0x3F,
        0x5A,
        0x4F,
        0xF2,
        0x64,
        0x8B
    )
    GUID_NDIS_GEN_PHYSICAL_MEDIUM = DEFINE_GUID(
        0x418CA16D,
        0x3937,
        0x4208,
        0x94,
        0x0A,
        0xEC,
        0x61,
        0x96,
        0x27,
        0x80,
        0x85
    )
#  uses NDIS_OFFLOAD
    GUID_NDIS_TCP_OFFLOAD_CURRENT_CONFIG = DEFINE_GUID(
        0x68542FED,
        0x5C74,
        0x461E,
        0x89,
        0x34,
        0x91,
        0xC6,
        0xF9,
        0xC6,
        0x09,
        0x60
    )
#  uses NDIS_OFFLOAD
    GUID_NDIS_TCP_OFFLOAD_HARDWARE_CAPABILITIES = DEFINE_GUID(
        0xCD5F1102,
        0x590F,
        0x4ADA,
        0xAB,
        0x65,
        0x5B,
        0x31,
        0xB1,
        0xDC,
        0x01,
        0x72
    )
#  uses NDIS_OFFLOAD_PARAMETERS
    GUID_NDIS_TCP_OFFLOAD_PARAMETERS = DEFINE_GUID(
        0x8EAD9A22,
        0x7F69,
        0x4BC6,
        0x94,
        0x9A,
        0xC8,
        0x18,
        0x7B,
        0x07,
        0x4E,
        0x61
    )
#  uses NDIS_TCP_CONNECTION_OFFLOAD
    GUID_NDIS_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG = DEFINE_GUID(
        0x2EE6AEF1,
        0x0851,
        0x458B,
        0xBF,
        0x0D,
        0x79,
        0x23,
        0x43,
        0xD1,
        0xCD,
        0xE1
    )
#  uses NDIS_TCP_CONNECTION_OFFLOAD
    GUID_NDIS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES = DEFINE_GUID(
        0x8CE71F2C,
        0xD63A,
        0x4390,
        0xA4,
        0x87,
        0x18,
        0xFA,
        0x47,
        0x26,
        0x2C,
        0xEB
    )
    GUID_NDIS_RECEIVE_SCALE_CAPABILITIES = DEFINE_GUID(
        0x26C28774,
        0x4252,
        0x48FE,
        0xA6,
        0x10,
        0xA5,
        0x8A,
        0x39,
        0x8C,
        0x0E,
        0xB1
    )
    GUID_NDIS_GEN_LINK_STATE = DEFINE_GUID(
        0xBA1F4C14,
        0xA945,
        0x4762,
        0xB9,
        0x16,
        0x0B,
        0x55,
        0x15,
        0xB6,
        0xF4,
        0x3A
    )
    GUID_NDIS_GEN_LINK_PARAMETERS = DEFINE_GUID(
        0x8C7D3579,
        0x252B,
        0x4614,
        0x82,
        0xC5,
        0xA6,
        0x50,
        0xDA,
        0xA1,
        0x50,
        0x49
    )
    GUID_NDIS_GEN_STATISTICS = DEFINE_GUID(
        0x368C45B5,
        0xC129,
        0x43C1,
        0x93,
        0x9E,
        0x7E,
        0xDC,
        0x2D,
        0x7F,
        0xE6,
        0x21
    )
    GUID_NDIS_GEN_PORT_STATE = DEFINE_GUID(
        0x6FBF2A5F,
        0x8B8F,
        0x4920,
        0x81,
        0x43,
        0xE6,
        0xC4,
        0x60,
        0xF5,
        0x25,
        0x24
    )
    GUID_NDIS_GEN_ENUMERATE_PORTS = DEFINE_GUID(
        0xF1D6ABE8,
        0x15E4,
        0x4407,
        0x81,
        0xB7,
        0x6B,
        0x83,
        0x0C,
        0x77,
        0x7C,
        0xD9
    )
    GUID_NDIS_ENUMERATE_ADAPTERS_EX = DEFINE_GUID(
        0x16716917,
        0x4306,
        0x4BE4,
        0x9B,
        0x5A,
        0x38,
        0x09,
        0xAE,
        0x44,
        0xB1,
        0x25
    )
    GUID_NDIS_GEN_PORT_AUTHENTICATION_PARAMETERS = DEFINE_GUID(
        0xAAB6AC31,
        0x86FB,
        0x48FB,
        0x8B,
        0x48,
        0x63,
        0xDB,
        0x23,
        0x5A,
        0xCE,
        0x16
    )
    GUID_NDIS_GEN_INTERRUPT_MODERATION = DEFINE_GUID(
        0xD9C8EEA5,
        0xF16E,
        0x467C,
        0x84,
        0xD5,
        0x63,
        0x45,
        0xA2,
        0x2C,
        0xE2,
        0x13
    )
    GUID_NDIS_GEN_INTERRUPT_MODERATION_PARAMETERS = DEFINE_GUID(
        0xD789ADFA,
        0x9C56,
        0x433B,
        0xAD,
        0x01,
        0x75,
        0x74,
        0xF3,
        0xCE,
        0xDB,
        0xE9
    )
    GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES = DEFINE_GUID(
        0xAA39F5AB,
        0xE260,
        0x4D01,
        0x82,
        0xB0,
        0xB7,
        0x37,
        0xC8,
        0x80,
        0xEA,
        0x05
    )
    GUID_NDIS_GEN_PHYSICAL_MEDIUM_EX = DEFINE_GUID(
        0x899E7782,
        0x035B,
        0x43F9,
        0x8B,
        0xB6,
        0x2B,
        0x58,
        0x97,
        0x16,
        0x12,
        0xE5
    )
#  uses NDIS_HD_SPLIT_CURRENT_CONFIGURATION
    GUID_NDIS_HD_SPLIT_CURRENT_CONFIG = DEFINE_GUID(
        0x81D1303C,
        0xAB00,
        0x4E49,
        0x80,
        0xB1,
        0x5E,
        0x6E,
        0x0B,
        0xF9,
        0xBE,
        0x53
    )
#  uses NDIS_HD_SPLIT_PARAMETERS
    GUID_NDIS_HD_SPLIT_PARAMETERS = DEFINE_GUID(
        0x8C048BEA,
        0x2913,
        0x4458,
        0xB6,
        0x8E,
        0x17,
        0xF6,
        0xC1,
        0xE5,
        0xC6,
        0x0E
    )
    GUID_NDIS_TCP_RSC_STATISTICS = DEFINE_GUID(
        0x83104445,
        0x9B5D,
        0x4EE6,
        0xA2,
        0xA5,
        0x2B,
        0xD3,
        0xFB,
        0x3C,
        0x36,
        0xAF
    )

    # {ece5360d - 3291 - 4a6e - 8044 - 00511fed27ee} - uses
    # NDIS_PM_CAPABILITIES
    GUID_PM_HARDWARE_CAPABILITIES = DEFINE_GUID(
        0xECE5360D,
        0x3291,
        0x4A6E,
        0x80,
        0x44,
        0x00,
        0x51,
        0x1F,
        0xED,
        0x27,
        0xEE
    )

    # {3ABDBD14 - D44A - 4a3f - 9A63 - A0A42A51B131} - uses
    # NDIS_PM_CAPABILITIES
    GUID_PM_CURRENT_CAPABILITIES = DEFINE_GUID(
        0x3ABDBD14,
        0xD44A,
        0x4A3F,
        0x9A,
        0x63,
        0xA0,
        0xA4,
        0x2A,
        0x51,
        0xB1,
        0x31
    )

    # {560245D2 - E251 - 409c - A280 - 311935BE3B28} - use NDIS_PM_PARAMETERS
    GUID_PM_PARAMETERS = DEFINE_GUID(
        0x560245D2,
        0xE251,
        0x409C,
        0xA2,
        0x80,
        0x31,
        0x19,
        0x35,
        0xBE,
        0x3B,
        0x28
    )

    # {6FC83BA7 - 52BC - 4faa - AC51 - 7D2FFE63BA90} - use NDIS_PM_WOL_PATTERN
    GUID_PM_ADD_WOL_PATTERN = DEFINE_GUID(
        0x6FC83BA7,
        0x52BC,
        0x4FAA,
        0xAC,
        0x51,
        0x7D,
        0x2F,
        0xFE,
        0x63,
        0xBA,
        0x90
    )

    # {A037A915 - C6CA - 4322 - B3E3 - EF754EC498DC}
    GUID_PM_REMOVE_WOL_PATTERN = DEFINE_GUID(
        0xA037A915,
        0xC6CA,
        0x4322,
        0xB3,
        0xE3,
        0xEF,
        0x75,
        0x4E,
        0xC4,
        0x98,
        0xDC
    )

    # {4022BE37 - 7EE2 - 47be - A5A5 - 050FC79AFC75}
    GUID_PM_WOL_PATTERN_LIST = DEFINE_GUID(
        0x4022BE37,
        0x7EE2,
        0x47BE,
        0xA5,
        0xA5,
        0x05,
        0x0F,
        0xC7,
        0x9A,
        0xFC,
        0x75
    )

    # {0C06C112 - 0D93 - 439b - 9E6D - 26BE130C9784} - uses
    # NDIS_PM_PROTOCOL_OFFLOAD
    GUID_PM_ADD_PROTOCOL_OFFLOAD = DEFINE_GUID(
        0x0C06C112,
        0x0D93,
        0x439B,
        0x9E,
        0x6D,
        0x26,
        0xBE,
        0x13,
        0x0C,
        0x97,
        0x84
    )

    # {A6435CD9 - 149F - 498e - 951B - 2D94BEA3E3A3} - uses
    # NDIS_PM_PROTOCOL_OFFLOAD
    GUID_PM_GET_PROTOCOL_OFFLOAD = DEFINE_GUID(
        0xA6435CD9,
        0x149F,
        0x498E,
        0x95,
        0x1B,
        0x2D,
        0x94,
        0xBE,
        0xA3,
        0xE3,
        0xA3
    )

    # {DECD7BE2 - A6B0 - 43ca - AE45 - D000D20E5265}
    GUID_PM_REMOVE_PROTOCOL_OFFLOAD = DEFINE_GUID(
        0xDECD7BE2,
        0xA6B0,
        0x43CA,
        0xAE,
        0x45,
        0xD0,
        0x00,
        0xD2,
        0x0E,
        0x52,
        0x65
    )

    # {736EC5AB - CA8F - 4043 - BB58 - DA402A48D9CC}
    GUID_PM_PROTOCOL_OFFLOAD_LIST = DEFINE_GUID(
        0x736EC5AB,
        0xCA8F,
        0x4043,
        0xBB,
        0x58,
        0xDA,
        0x40,
        0x2A,
        0x48,
        0xD9,
        0xCC
    )

    # GUIDs for receive filters#  uses NDIS_RECEIVE_FILTER_CAPABILITIES
    GUID_NDIS_RECEIVE_FILTER_HARDWARE_CAPABILITIES = DEFINE_GUID(
        0x3F2C1419,
        0x83BC,
        0x11DD,
        0x94,
        0xB8,
        0x00,
        0x1D,
        0x09,
        0x16,
        0x2B,
        0xC3
    )
#  uses NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
    GUID_NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS = DEFINE_GUID(
        0x3F2C141A,
        0x83BC,
        0x11DD,
        0x94,
        0xB8,
        0x00,
        0x1D,
        0x09,
        0x16,
        0x2B,
        0xC3
    )
#  uses NDIS_RECEIVE_QUEUE_INFO_ARRAY
    GUID_NDIS_RECEIVE_FILTER_ENUM_QUEUES = DEFINE_GUID(
        0x3F2C141B,
        0x83BC,
        0x11DD,
        0x94,
        0xB8,
        0x00,
        0x1D,
        0x09,
        0x16,
        0x2B,
        0xC3
    )
#  uses NDIS_RECEIVE_QUEUE_PARAMETERS
    GUID_NDIS_RECEIVE_FILTER_QUEUE_PARAMETERS = DEFINE_GUID(
        0x3F2C141C,
        0x83BC,
        0x11DD,
        0x94,
        0xB8,
        0x00,
        0x1D,
        0x09,
        0x16,
        0x2B,
        0xC3
    )
#  uses NDIS_RECEIVE_FILTER_INFO_ARRAY
    GUID_NDIS_RECEIVE_FILTER_ENUM_FILTERS = DEFINE_GUID(
        0x3F2C141D,
        0x83BC,
        0x11DD,
        0x94,
        0xB8,
        0x00,
        0x1D,
        0x09,
        0x16,
        0x2B,
        0xC3
    )
#  uses NDIS_RECEIVE_FILTER_PARAMETERS
    GUID_NDIS_RECEIVE_FILTER_PARAMETERS = DEFINE_GUID(
        0x3F2C141E,
        0x83BC,
        0x11DD,
        0x94,
        0xB8,
        0x00,
        0x1D,
        0x09,
        0x16,
        0x2B,
        0xC3
    )
#  uses RECEIVE_FILTER_CAPABILITIES
    GUID_RECEIVE_FILTER_CURRENT_CAPABILITIES = DEFINE_GUID(
        0x4054E80F,
        0x2BC1,
        0x4CCC,
        0xB0,
        0x33,
        0x4A,
        0xBC,
        0x0C,
        0x4A,
        0x1E,
        0x8C
    )
#  uses NIC_SWITCH_CAPABILITIES
    GUID_NIC_SWITCH_HARDWARE_CAPABILITIES = DEFINE_GUID(
        0x37CAB40C,
        0xD1E8,
        0x4301,
        0x8C,
        0x1D,
        0x58,
        0x46,
        0x5E,
        0x0C,
        0x4C,
        0x0F
    )
#  uses NIC_SWITCH_CAPABILITIES
    GUID_NIC_SWITCH_CURRENT_CAPABILITIES = DEFINE_GUID(
        0xE76FDAF3,
        0x0BE7,
        0x4D95,
        0x87,
        0xE9,
        0x5A,
        0xEA,
        0xD4,
        0xB5,
        0x90,
        0xE9
    )

    # GUIDs for switch policy
    GUID_NDIS_SWITCH_MICROSOFT_VENDOR_ID = DEFINE_GUID(
        0x202547FE,
        0x1C9C,
        0x40B9,
        0xBB,
        0xA1,
        0x8,
        0xAD,
        0xA1,
        0xF9,
        0x8B,
        0x3C
    )
    GUID_NDIS_SWITCH_PORT_PROPERTY_PROFILE_ID_DEFAULT_EXTERNAL_NIC = DEFINE_GUID(
        0xB347846,
        0xA0C,
        0x470A,
        0x9B,
        0x7A,
        0xD,
        0x96,
        0x58,
        0x50,
        0x69,
        0x8F
    )

    # GUIDs for General Required Statistics OIDs
    GUID_NDIS_GEN_XMIT_OK = DEFINE_GUID(
        0x447956FA,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_RCV_OK = DEFINE_GUID(
        0x447956FB,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_XMIT_ERROR = DEFINE_GUID(
        0x447956FC,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_RCV_ERROR = DEFINE_GUID(
        0x447956FD,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_RCV_NO_BUFFER = DEFINE_GUID(
        0x447956FE,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )

    # GUIDs for General Required CO - NDIS OIDs
    GUID_NDIS_GEN_CO_HARDWARE_STATUS = DEFINE_GUID(
        0x791AD192,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_MEDIA_SUPPORTED = DEFINE_GUID(
        0x791AD193,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_MEDIA_IN_USE = DEFINE_GUID(
        0x791AD194,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_LINK_SPEED = DEFINE_GUID(
        0x791AD195,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_VENDOR_ID = DEFINE_GUID(
        0x791AD196,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_VENDOR_DESCRIPTION = DEFINE_GUID(
        0x791AD197,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_DRIVER_VERSION = DEFINE_GUID(
        0x791AD198,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_MAC_OPTIONS = DEFINE_GUID(
        0x791AD19A,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_MEDIA_CONNECT_STATUS = DEFINE_GUID(
        0x791AD19B,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_VENDOR_DRIVER_VERSION = DEFINE_GUID(
        0x791AD19C,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_MINIMUM_LINK_SPEED = DEFINE_GUID(
        0x791AD19D,
        0xE35C,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )

    # GUIDs for General Required CO - NDIS Statistics OIDs
    GUID_NDIS_GEN_CO_XMIT_PDUS_OK = DEFINE_GUID(
        0x0A214805,
        0xE35F,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_RCV_PDUS_OK = DEFINE_GUID(
        0x0A214806,
        0xE35F,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_XMIT_PDUS_ERROR = DEFINE_GUID(
        0x0A214807,
        0xE35F,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_RCV_PDUS_ERROR = DEFINE_GUID(
        0x0A214808,
        0xE35F,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_GEN_CO_RCV_PDUS_NO_BUFFER = DEFINE_GUID(
        0x0A214809,
        0xE35F,
        0x11D0,
        0x96,
        0x92,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )

    # GUIDs for Required Ethernet OIDs
    GUID_NDIS_802_3_PERMANENT_ADDRESS = DEFINE_GUID(
        0x447956FF,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_3_CURRENT_ADDRESS = DEFINE_GUID(
        0x44795700,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_3_MULTICAST_LIST = DEFINE_GUID(
        0x44795701,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_3_MAXIMUM_LIST_SIZE = DEFINE_GUID(
        0x44795702,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_3_MAC_OPTIONS = DEFINE_GUID(
        0x44795703,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )

    # GUIDs for Required Ethernet Statistics OIDs
    GUID_NDIS_802_3_RCV_ERROR_ALIGNMENT = DEFINE_GUID(
        0x44795704,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_3_XMIT_ONE_COLLISION = DEFINE_GUID(
        0x44795705,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_3_XMIT_MORE_COLLISIONS = DEFINE_GUID(
        0x44795706,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )

    # GUIDs for Required Token - Ring OIDs
    GUID_NDIS_802_5_PERMANENT_ADDRESS = DEFINE_GUID(
        0x44795707,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_5_CURRENT_ADDRESS = DEFINE_GUID(
        0x44795708,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_5_CURRENT_FUNCTIONAL = DEFINE_GUID(
        0x44795709,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_5_CURRENT_GROUP = DEFINE_GUID(
        0x4479570A,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_5_LAST_OPEN_STATUS = DEFINE_GUID(
        0x4479570B,
        0xA61B,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_5_CURRENT_RING_STATUS = DEFINE_GUID(
        0x890A36EC,
        0xA61C,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_5_CURRENT_RING_STATE = DEFINE_GUID(
        0xACF14032,
        0xA61C,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )

    # GUIDs for Required Token - Ring Statistics OIDs
    GUID_NDIS_802_5_LINE_ERRORS = DEFINE_GUID(
        0xACF14033,
        0xA61C,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_802_5_LOST_FRAMES = DEFINE_GUID(
        0xACF14034,
        0xA61C,
        0x11D0,
        0x8D,
        0xD4,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )

    # GUIDs for required and optional 802.11 Wireless LAN OIDs
    GUID_NDIS_802_11_BSSID = DEFINE_GUID(
        0x2504B6C2,
        0x1FA5,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_SSID = DEFINE_GUID(
        0x7D2A90EA,
        0x2041,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_NETWORK_TYPES_SUPPORTED = DEFINE_GUID(
        0x8531D6E6,
        0x2041,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_NETWORK_TYPE_IN_USE = DEFINE_GUID(
        0x857E2326,
        0x2041,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_POWER_MODE = DEFINE_GUID(
        0x85BE837C,
        0x2041,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_TX_POWER_LEVEL = DEFINE_GUID(
        0x11E6BA76,
        0x2053,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_RSSI = DEFINE_GUID(
        0x1507DB16,
        0x2053,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_RSSI_TRIGGER = DEFINE_GUID(
        0x155689B8,
        0x2053,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_BSSID_LIST = DEFINE_GUID(
        0x69526F9A,
        0x2062,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_INFRASTRUCTURE_MODE = DEFINE_GUID(
        0x697D5A7E,
        0x2062,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_FRAGMENTATION_THRESHOLD = DEFINE_GUID(
        0x69AAA7C4,
        0x2062,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_RTS_THRESHOLD = DEFINE_GUID(
        0x0134D07E,
        0x2064,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_NUMBER_OF_ANTENNAS = DEFINE_GUID(
        0x01779336,
        0x2064,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_RX_ANTENNA_SELECTED = DEFINE_GUID(
        0x01AC07A2,
        0x2064,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_TX_ANTENNA_SELECTED = DEFINE_GUID(
        0x01DBB74A,
        0x2064,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_SUPPORTED_RATES = DEFINE_GUID(
        0x49DB8722,
        0x2068,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_DESIRED_RATES = DEFINE_GUID(
        0x452EE08E,
        0x2536,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_CONFIGURATION = DEFINE_GUID(
        0x4A4DF982,
        0x2068,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_STATISTICS = DEFINE_GUID(
        0x42BB73B0,
        0x2129,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_ADD_WEP = DEFINE_GUID(
        0x4307BFF0,
        0x2129,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_REMOVE_WEP = DEFINE_GUID(
        0x433C345C,
        0x2129,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_DISASSOCIATE = DEFINE_GUID(
        0x43671F40,
        0x2129,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_AUTHENTICATION_MODE = DEFINE_GUID(
        0x43920A24,
        0x2129,
        0x11D4,
        0x97,
        0xEB,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_PRIVACY_FILTER = DEFINE_GUID(
        0x6733C4E9,
        0x4792,
        0x11D4,
        0x97,
        0xF1,
        0x00,
        0xC0,
        0x4F,
        0x79,
        0xC4,
        0x03
    )
    GUID_NDIS_802_11_BSSID_LIST_SCAN = DEFINE_GUID(
        0x0D9E01E1,
        0xBA70,
        0x11D4,
        0xB6,
        0x75,
        0x00,
        0x20,
        0x48,
        0x57,
        0x03,
        0x37
    )
    GUID_NDIS_802_11_WEP_STATUS = DEFINE_GUID(
        0xB027A21F,
        0x3CFA,
        0x4125,
        0x80,
        0x0B,
        0x3F,
        0x7A,
        0x18,
        0xFD,
        0xDC,
        0xDC
    )
    GUID_NDIS_802_11_RELOAD_DEFAULTS = DEFINE_GUID(
        0x748B14E8,
        0x32EE,
        0x4425,
        0xB9,
        0x1B,
        0xC9,
        0x84,
        0x8C,
        0x58,
        0xB5,
        0x5A
    )
    GUID_NDIS_802_11_ADD_KEY = DEFINE_GUID(
        0xAB8B5A62,
        0x1D51,
        0x49D8,
        0xBA,
        0x5C,
        0xFA,
        0x98,
        0x0B,
        0xE0,
        0x3A,
        0x1D
    )
    GUID_NDIS_802_11_REMOVE_KEY = DEFINE_GUID(
        0x73CB28E9,
        0x3188,
        0x42D5,
        0xB5,
        0x53,
        0xB2,
        0x12,
        0x37,
        0xE6,
        0x08,
        0x8C
    )
    GUID_NDIS_802_11_ASSOCIATION_INFORMATION = DEFINE_GUID(
        0xA08D4DD0,
        0x960E,
        0x40BD,
        0x8C,
        0xF6,
        0xC5,
        0x38,
        0xAF,
        0x98,
        0xF2,
        0xE3
    )
    GUID_NDIS_802_11_TEST = DEFINE_GUID(
        0x4B9CA16A,
        0x6A60,
        0x4E9D,
        0x92,
        0x0C,
        0x63,
        0x35,
        0x95,
        0x3F,
        0xA0,
        0xB5
    )
    GUID_NDIS_802_11_MEDIA_STREAM_MODE = DEFINE_GUID(
        0x0A56AF66,
        0xD84B,
        0x49EB,
        0xA2,
        0x8D,
        0x52,
        0x82,
        0xCB,
        0xB6,
        0xD0,
        0xCD
    )

    # GUIDs for NDIS status indications
    GUID_NDIS_STATUS_RESET_START = DEFINE_GUID(
        0x981F2D76,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_STATUS_RESET_END = DEFINE_GUID(
        0x981F2D77,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_STATUS_MEDIA_CONNECT = DEFINE_GUID(
        0x981F2D7D,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_STATUS_MEDIA_DISCONNECT = DEFINE_GUID(
        0x981F2D7E,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION = DEFINE_GUID(
        0x981F2D84,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_STATUS_LINK_SPEED_CHANGE = DEFINE_GUID(
        0x981F2D85,
        0xB1F3,
        0x11D0,
        0x8D,
        0xD7,
        0x00,
        0xC0,
        0x4F,
        0xC3,
        0x35,
        0x8C
    )
    GUID_NDIS_STATUS_PACKET_FILTER = DEFINE_GUID(
        0xD47C5407,
        0x2E75,
        0x46DD,
        0x81,
        0x46,
        0x1D,
        0x7E,
        0xD2,
        0xD6,
        0xAB,
        0x1D
    )
    GUID_NDIS_STATUS_NETWORK_CHANGE = DEFINE_GUID(
        0xCA8A56F9,
        0xCE81,
        0x40E6,
        0xA7,
        0x0F,
        0xA0,
        0x67,
        0xA4,
        0x76,
        0xE9,
        0xE9
    )
#  NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG
    GUID_NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG = DEFINE_GUID(
        0x45049FC6,
        0x54D8,
        0x40C8,
        0x9C,
        0x3D,
        0xB0,
        0x11,
        0xC4,
        0xE7,
        0x15,
        0xBC
    )
#  NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES
    GUID_NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES = DEFINE_GUID(
        0xB6B8158B,
        0x217C,
        0x4B2A,
        0xBE,
        0x86,
        0x6A,
        0x04,
        0xBE,
        0xEA,
        0x65,
        0xB8
    )
#  NDIS_STATUS_OFFLOAD_RESUME
    GUID_NDIS_STATUS_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG = DEFINE_GUID(
        0xF8EDAEFF,
        0x24E4,
        0x4AE6,
        0xA4,
        0x13,
        0x0B,
        0x27,
        0xF7,
        0x6B,
        0x24,
        0x3D
    )
#  NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES
    GUID_NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES = DEFINE_GUID(
        0x391969B6,
        0x402C,
        0x43BF,
        0x89,
        0x22,
        0x39,
        0xEA,
        0xE0,
        0xDA,
        0x1B,
        0xB5
    )
    GUID_NDIS_STATUS_OPER_STATUS = DEFINE_GUID(
        0xF917B663,
        0x845E,
        0x4D3D,
        0xB6,
        0xD4,
        0x15,
        0xEB,
        0x27,
        0xAF,
        0x81,
        0xC5
    )
    GUID_NDIS_STATUS_LINK_STATE = DEFINE_GUID(
        0x64C6F797,
        0x878C,
        0x4311,
        0x92,
        0x46,
        0x65,
        0xDB,
        0xA8,
        0x9C,
        0x3A,
        0x61
    )
    GUID_NDIS_STATUS_PORT_STATE = DEFINE_GUID(
        0x1DAC0DFE,
        0x43E5,
        0x44B7,
        0xB7,
        0x59,
        0x7B,
        0xF4,
        0x6D,
        0xE3,
        0x2E,
        0x81
    )
    GUID_NDIS_STATUS_EXTERNAL_CONNECTIVITY_CHANGE = DEFINE_GUID(
        0xFD306974,
        0xC420,
        0x4433,
        0xB0,
        0xFE,
        0x4C,
        0xF6,
        0xA6,
        0x13,
        0xF5,
        0x9F
    )
    GUID_STATUS_MEDIA_SPECIFIC_INDICATION_EX = DEFINE_GUID(
        0xAAACFCA7,
        0x954A,
        0x4632,
        0xA1,
        0x6E,
        0xA8,
        0xA6,
        0x37,
        0x93,
        0xA9,
        0xE5
    )
#  NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG
    GUID_NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG = DEFINE_GUID(
        0x6C744B0E,
        0xEE9C,
        0x4205,
        0x90,
        0xA2,
        0x01,
        0x5F,
        0x6D,
        0x65,
        0xF4,
        0x03
    )
    GUID_NDIS_STATUS_PM_WOL_PATTERN_REJECTED = DEFINE_GUID(
        0xF72CF68E,
        0x18D4,
        0x4D63,
        0x9A,
        0x19,
        0xE6,
        0x9B,
        0x13,
        0x91,
        0x6B,
        0x1A
    )
    GUID_NDIS_STATUS_PM_OFFLOAD_REJECTED = DEFINE_GUID(
        0xADD1D481,
        0x711E,
        0x4D1A,
        0x92,
        0xCA,
        0xA6,
        0x2D,
        0xB9,
        0x32,
        0x97,
        0x12
    )
    GUID_NDIS_STATUS_PM_WAKE_REASON = DEFINE_GUID(
        0x0933FD58,
        0xCA62,
        0x438F,
        0x83,
        0xDA,
        0xDF,
        0xC1,
        0xCC,
        0xCB,
        0x81,
        0x45
    )
    GUID_NDIS_STATUS_DOT11_SCAN_CONFIRM = DEFINE_GUID(
        0x8500591E,
        0xA0C7,
        0x4EFB,
        0x93,
        0x42,
        0xB6,
        0x74,
        0xB0,
        0x02,
        0xCB,
        0xE6
    )
    GUID_NDIS_STATUS_DOT11_MPDU_MAX_LENGTH_CHANGED = DEFINE_GUID(
        0x1D6560EC,
        0x8E48,
        0x4A3E,
        0x9F,
        0xD5,
        0xA0,
        0x1B,
        0x69,
        0x8D,
        0xB6,
        0xC5
    )
    GUID_NDIS_STATUS_DOT11_ASSOCIATION_START = DEFINE_GUID(
        0x3927843B,
        0x6980,
        0x4B48,
        0xB1,
        0x5B,
        0x4D,
        0xE5,
        0x09,
        0x77,
        0xAC,
        0x40
    )
    GUID_NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION = DEFINE_GUID(
        0x458BBEA7,
        0x45A4,
        0x4AE2,
        0xB1,
        0x76,
        0xE5,
        0x1F,
        0x96,
        0xFC,
        0x05,
        0x68
    )
    GUID_NDIS_STATUS_DOT11_CONNECTION_START = DEFINE_GUID(
        0x7B74299D,
        0x998F,
        0x4454,
        0xAD,
        0x08,
        0xC5,
        0xAF,
        0x28,
        0x57,
        0x6D,
        0x1B
    )
    GUID_NDIS_STATUS_DOT11_CONNECTION_COMPLETION = DEFINE_GUID(
        0x96EFD9C9,
        0x7F1B,
        0x4A89,
        0xBC,
        0x04,
        0x3E,
        0x9E,
        0x27,
        0x17,
        0x65,
        0xF1
    )
    GUID_NDIS_STATUS_DOT11_ROAMING_START = DEFINE_GUID(
        0xB2412D0D,
        0x26C8,
        0x4F4E,
        0x93,
        0xDF,
        0xF7,
        0xB7,
        0x05,
        0xA0,
        0xB4,
        0x33
    )
    GUID_NDIS_STATUS_DOT11_ROAMING_COMPLETION = DEFINE_GUID(
        0xDD9D47D1,
        0x282B,
        0x41E4,
        0xB9,
        0x24,
        0x66,
        0x36,
        0x88,
        0x17,
        0xFC,
        0xD3
    )
    GUID_NDIS_STATUS_DOT11_DISASSOCIATION = DEFINE_GUID(
        0x3FBEB6FC,
        0x0FE2,
        0x43FD,
        0xB2,
        0xAD,
        0xBD,
        0x99,
        0xB5,
        0xF9,
        0x3E,
        0x13
    )
    GUID_NDIS_STATUS_DOT11_TKIPMIC_FAILURE = DEFINE_GUID(
        0x442C2AE4,
        0x9BC5,
        0x4B90,
        0xA8,
        0x89,
        0x45,
        0x5E,
        0xF2,
        0x20,
        0xF4,
        0xEE
    )
    GUID_NDIS_STATUS_DOT11_PMKID_CANDIDATE_LIST = DEFINE_GUID(
        0x26D8B8F6,
        0xDB82,
        0x49EB,
        0x8B,
        0xF3,
        0x4C,
        0x13,
        0x0E,
        0xF0,
        0x69,
        0x50
    )
    GUID_NDIS_STATUS_DOT11_PHY_STATE_CHANGED = DEFINE_GUID(
        0xDEB45316,
        0x71B5,
        0x4736,
        0xBD,
        0xEF,
        0x0A,
        0x9E,
        0x9F,
        0x4E,
        0x62,
        0xDC
    )
    GUID_NDIS_STATUS_DOT11_LINK_QUALITY = DEFINE_GUID(
        0xA3285184,
        0xEA99,
        0x48ED,
        0x82,
        0x5E,
        0xA4,
        0x26,
        0xB1,
        0x1C,
        0x27,
        0x54
    )
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
