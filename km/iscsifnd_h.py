import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _ISCSI_DiscoveredTargetPortal(ctypes.Structure):
    pass


ISCSI_DiscoveredTargetPortal = _ISCSI_DiscoveredTargetPortal
PISCSI_DiscoveredTargetPortal = POINTER(_ISCSI_DiscoveredTargetPortal)


class _ISCSI_DiscoveredTargetPortalGroup(ctypes.Structure):
    pass


ISCSI_DiscoveredTargetPortalGroup = _ISCSI_DiscoveredTargetPortalGroup
PISCSI_DiscoveredTargetPortalGroup = POINTER(_ISCSI_DiscoveredTargetPortalGroup)


class _ISCSI_DiscoveredTarget(ctypes.Structure):
    pass


ISCSI_DiscoveredTarget = _ISCSI_DiscoveredTarget
PISCSI_DiscoveredTarget = POINTER(_ISCSI_DiscoveredTarget)


class _ISCSI_DiscoveredTargetPortal2(ctypes.Structure):
    pass


ISCSI_DiscoveredTargetPortal2 = _ISCSI_DiscoveredTargetPortal2
PISCSI_DiscoveredTargetPortal2 = POINTER(_ISCSI_DiscoveredTargetPortal2)


class _ISCSI_DiscoveredTargetPortalGroup2(ctypes.Structure):
    pass


ISCSI_DiscoveredTargetPortalGroup2 = _ISCSI_DiscoveredTargetPortalGroup2
PISCSI_DiscoveredTargetPortalGroup2 = POINTER(_ISCSI_DiscoveredTargetPortalGroup2)


class _ISCSI_DiscoveredTarget2(ctypes.Structure):
    pass


ISCSI_DiscoveredTarget2 = _ISCSI_DiscoveredTarget2
PISCSI_DiscoveredTarget2 = POINTER(_ISCSI_DiscoveredTarget2)


class _ReportDiscoveredTargets_OUT(ctypes.Structure):
    pass


ReportDiscoveredTargets_OUT = _ReportDiscoveredTargets_OUT
PReportDiscoveredTargets_OUT = POINTER(_ReportDiscoveredTargets_OUT)


class _ReportDiscoveredTargets2_OUT(ctypes.Structure):
    pass


ReportDiscoveredTargets2_OUT = _ReportDiscoveredTargets2_OUT
PReportDiscoveredTargets2_OUT = POINTER(_ReportDiscoveredTargets2_OUT)

_iscsifnd_h_ = None
if not defined(_iscsifnd_h_):
    _iscsifnd_h_ = 1
    # ISCSI_DiscoveredTargetPortal - ISCSI_DiscoveredTargetPortal
    # iSCSI target portal
    # ********************************************************************
    # iscsifnd.h
    # Module: iScsi Discovery api
    # Purpose: Header defining interface between user mode discovery
    # engine and HBA driver miniport.
    # Copyright (c) 2001 Microsoft Corporation
    # ********************************************************************
    from pyWinAPI.km.iscsidef_h import * # NOQA

    ISCSI_DiscoveredTargetPortalGuid = [
        0xFA218C5D,
        0xB306,
        0x4D5D,
        [0xB2, 0xDB, 0x6B, 0xBA, 0x05, 0x0F, 0xD8, 0xFA]
    ]

    if not defined(MIDL_PASS):
        ISCSI_DiscoveredTargetPortal_GUID = DEFINE_GUID(
            0xFA218C5D,
            0xB306,
            0x4D5D,
            0xB2,
            0xDB,
            0x6B,
            0xBA,
            0x05,
            0x0F,
            0xD8,
            0xFA
        )
    # END IF
    ISCSI_DiscoveredTargetPortal_Socket_SIZE = ctypes.sizeof(USHORT)
    ISCSI_DiscoveredTargetPortal_Socket_ID = 1
    ISCSI_DiscoveredTargetPortal_Address_SIZE = ctypes.sizeof(ISCSI_IP_Address)
    ISCSI_DiscoveredTargetPortal_Address_ID = 2
    ISCSI_DiscoveredTargetPortal_SymbolicName_ID = 3

    _ISCSI_DiscoveredTargetPortal._fields_ = [
        # Socket number
        ('Socket', USHORT),
        # Network Address
        ('Address', ISCSI_IP_Address),
        # Portal Symbolic Name
        ('SymbolicName', WCHAR * 256 + 1),
    ]

    # ISCSI_DiscoveredTargetPortalGroup - ISCSI_DiscoveredTargetPortalGroup
    # iSCSI target portal group
    ISCSI_DiscoveredTargetPortalGroupGuid = [
        0x28C3AF2C,
        0xA453,
        0x4A3D,
        [0x8E, 0x10, 0x9E, 0x09, 0xD8, 0x9E, 0xF3, 0x33]
    ]

    if not defined(MIDL_PASS):
        ISCSI_DiscoveredTargetPortalGroup_GUID = DEFINE_GUID(
            0x28C3AF2C,
            0xA453,
            0x4A3D,
            0x8E,
            0x10,
            0x9E,
            0x09,
            0xD8,
            0x9E,
            0xF3,
            0x33
        )
    # END IF


    ISCSI_DiscoveredTargetPortalGroup_PortalCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_DiscoveredTargetPortalGroup_PortalCount_ID = 1
    ISCSI_DiscoveredTargetPortalGroup_Portals_ID = 2

    _ISCSI_DiscoveredTargetPortalGroup._fields_ = [
        # Number of portals in group
        ('PortalCount', ULONG),
        # Target portals in group. NOTE: this field is a variable length array.
        ('Portals', ISCSI_DiscoveredTargetPortal * 1),
    ]

    # ISCSI_DiscoveredTarget - ISCSI_DiscoveredTarget
    # ISCSI discovered target information
    ISCSI_DiscoveredTargetGuid = [
        0x08CDF465,
        0xE18D,
        0x42FE,
        [0x8E, 0xB2, 0x56, 0x8C, 0xA9, 0x6A, 0x98, 0x56]
    ]

    if not defined(MIDL_PASS):
        ISCSI_DiscoveredTarget_GUID = DEFINE_GUID(
            0x08CDF465,
            0xE18D,
            0x42FE,
            0x8E,
            0xB2,
            0x56,
            0x8C,
            0xA9,
            0x6A,
            0x98,
            0x56
        )
    # END IF

    ISCSI_DiscoveredTarget_TargetPortalGroupCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_DiscoveredTarget_TargetPortalGroupCount_ID = 1
    ISCSI_DiscoveredTarget_TargetName_ID = 2
    ISCSI_DiscoveredTarget_TargetAlias_ID = 3
    ISCSI_DiscoveredTarget_TargetDiscoveredPortalGroups_ID = 4

    _ISCSI_DiscoveredTarget._fields_ = [
        # Number of portal groups for target
        ('TargetPortalGroupCount', ULONG),
        # Target Name
        ('TargetName', WCHAR * 223 + 1),
        # Target Alias
        ('TargetAlias', WCHAR * 255 + 1),
        # Portal Groups available for connection to target. NOTE: this field
        # is a variable length array
        ('TargetDiscoveredPortalGroups', ISCSI_DiscoveredTargetPortalGroup * 1)
    ]

    # ISCSI_DiscoveredTargetPortal2 - ISCSI_DiscoveredTargetPortal2
    # iSCSI target portal
    ISCSI_DiscoveredTargetPortal2Guid = [
        0xE95162A2,
        0x8EE5,
        0x40F1,
        [0xB0, 0x5D, 0xA5, 0x32, 0x1A, 0x30, 0xD0, 0x3D]
    ]

    if not defined(MIDL_PASS):
        ISCSI_DiscoveredTargetPortal2_GUID = DEFINE_GUID(
            0xE95162A2,
            0x8EE5,
            0x40F1,
            0xB0,
            0x5D,
            0xA5,
            0x32,
            0x1A,
            0x30,
            0xD0,
            0x3D
        )
    # END IF

    ISCSI_DiscoveredTargetPortal2_Socket_SIZE = ctypes.sizeof(USHORT)
    ISCSI_DiscoveredTargetPortal2_Socket_ID = 1
    ISCSI_DiscoveredTargetPortal2_Address_SIZE = ctypes.sizeof(ISCSI_IP_Address)
    ISCSI_DiscoveredTargetPortal2_Address_ID = 2
    ISCSI_DiscoveredTargetPortal2_SecurityBitmap_SIZE = ctypes.sizeof(ULONG)
    ISCSI_DiscoveredTargetPortal2_SecurityBitmap_ID = 3
    ISCSI_DiscoveredTargetPortal2_KeySize_SIZE = ctypes.sizeof(ULONG)
    ISCSI_DiscoveredTargetPortal2_KeySize_ID = 4
    ISCSI_DiscoveredTargetPortal2_Key_ID = 5
    ISCSI_DiscoveredTargetPortal2_SymbolicName_ID = 6

    _ISCSI_DiscoveredTargetPortal2._fields_ = [
        # Socket number
        ('Socket', USHORT),
        # Network Address
        ('Address', ISCSI_IP_Address),
        # Security capabilities bitmap as specified in iSNS spec
        ('SecurityBitmap', ULONG),
        # Number of bytes contained in key associated with portal address
        ('KeySize', ULONG),
        # Key associated with portal address. NOTE: This field is a variable
        # length array, the field that follows this field starts immediately
        # after the end of this field subject to appropriate padding. All
        # fields after this are commented out in the header.
        ('Key', UCHAR * 1),
    ]

    # ISCSI_DiscoveredTargetPortalGroup2 - ISCSI_DiscoveredTargetPortalGroup2
    # iSCSI target portal group
    ISCSI_DiscoveredTargetPortalGroup2Guid = [
        0x1732B30D,
        0xEE08,
        0x4DE7,
        [0xBE, 0xD1, 0xDE, 0x16, 0x5F, 0x1D, 0x7B, 0x45]
    ]

    if not defined(MIDL_PASS):
        ISCSI_DiscoveredTargetPortalGroup2_GUID = DEFINE_GUID(
            0x1732B30D,
            0xEE08,
            0x4DE7,
            0xBE,
            0xD1,
            0xDE,
            0x16,
            0x5F,
            0x1D,
            0x7B,
            0x45
        )
    # END IF

    ISCSI_DiscoveredTargetPortalGroup2_PortalCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_DiscoveredTargetPortalGroup2_PortalCount_ID = 1
    ISCSI_DiscoveredTargetPortalGroup2_Tag_SIZE = ctypes.sizeof(USHORT)
    ISCSI_DiscoveredTargetPortalGroup2_Tag_ID = 2
    ISCSI_DiscoveredTargetPortalGroup2_Portals_ID = 3

    _ISCSI_DiscoveredTargetPortalGroup2._fields_ = [
        # Number of portals in group
        ('PortalCount', ULONG),
        # portal group tag
        ('Tag', USHORT),
        # Target portals in group. NOTE: This field is a variable length array.
        ('Portals', ISCSI_DiscoveredTargetPortal2 * 1),
    ]

    # ISCSI_DiscoveredTarget2 - ISCSI_DiscoveredTarget2
    # ISCSI discovered target information
    ISCSI_DiscoveredTarget2Guid = [
        0xA71BCDE9,
        0x5433,
        0x4B36,
        [0xB9, 0xC1, 0x07, 0x86, 0x8E, 0x18, 0xB4, 0x8A]
    ]

    if not defined(MIDL_PASS):
        ISCSI_DiscoveredTarget2_GUID = DEFINE_GUID(
            0xA71BCDE9,
            0x5433,
            0x4B36,
            0xB9,
            0xC1,
            0x07,
            0x86,
            0x8E,
            0x18,
            0xB4,
            0x8A
        )
    # END IF

    ISCSI_DiscoveredTarget2_TargetPortalGroupCount_SIZE = ctypes.sizeof(ULONG)
    ISCSI_DiscoveredTarget2_TargetPortalGroupCount_ID = 1
    ISCSI_DiscoveredTarget2_TargetName_ID = 2
    ISCSI_DiscoveredTarget2_TargetAlias_ID = 3
    ISCSI_DiscoveredTarget2_TargetDiscoveredPortalGroups_ID = 4

    _ISCSI_DiscoveredTarget2._fields_ = [
        # Number of portal groups for target
        ('TargetPortalGroupCount', ULONG),
        # Target Name
        ('TargetName', WCHAR * 223 + 1),
        # Target Alias
        ('TargetAlias', WCHAR * 255 + 1),
        # Portal Groups available for connection to target. NOTE: This field
        # is a variable length array.
        ('TargetDiscoveredPortalGroups', ISCSI_DiscoveredTargetPortalGroup2 * 1),
    ]

    # MSiSCSI_DiscoveryOperations - MSiSCSI_DiscoveryOperations
    # Discovery operations
    # This class is required
    # This class exposes the configuration capabilities if the adapter is able
    # to
    # perform target discovery. An adapter would need to support target
    # discovery
    # if it is ever placed on a separate network from the PC NIC.
    # This classes uses PDO instance names with a single instance
    MSiSCSI_DiscoveryOperationsGuid = [
        0x556BC0B0,
        0x0FB5,
        0x40F2,
        [0x92, 0x55, 0xB7, 0xD9, 0xA6, 0x69, 0xDA, 0xEC]
    ]

    if not defined(MIDL_PASS):
        MSiSCSI_DiscoveryOperations_GUID = DEFINE_GUID(
            0x556BC0B0,
            0x0FB5,
            0x40F2,
            0x92,
            0x55,
            0xB7,
            0xD9,
            0xA6,
            0x69,
            0xDA,
            0xEC
        )
    # END IF

    # Method id definitions for MSiSCSI_DiscoveryOperations

    ReportDiscoveredTargets_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    ReportDiscoveredTargets_OUT_Status_ID = 1
    ReportDiscoveredTargets_OUT_TargetCount_SIZE = ctypes.sizeof(ULONG)
    ReportDiscoveredTargets_OUT_TargetCount_ID = 2
    ReportDiscoveredTargets_OUT_Targets_ID = 3

    ReportDiscoveredTargets = 10

    _ReportDiscoveredTargets_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Number of targets discovered
        ('TargetCount', ULONG),
        # Targets that have been discovered. NOTE: This field is a variabale
        # length array.
        ('Targets', ISCSI_DiscoveredTarget * 1),
    ]

    ReportDiscoveredTargets2_OUT_Status_SIZE = ctypes.sizeof(ULONG)
    ReportDiscoveredTargets2_OUT_Status_ID = 1
    ReportDiscoveredTargets2_OUT_TargetCount_SIZE = ctypes.sizeof(ULONG)
    ReportDiscoveredTargets2_OUT_TargetCount_ID = 2
    ReportDiscoveredTargets2_OUT_Targets_ID = 3

    ReportDiscoveredTargets2 = 11

    _ReportDiscoveredTargets2_OUT._fields_ = [
        # Status code resulting from operation
        ('Status', ULONG),
        # Number of targets discovered
        ('TargetCount', ULONG),
        # Targets that have been discovered. NOTE: This field is a variabale
        # length array.
        ('Targets', ISCSI_DiscoveredTarget2 * 1),
    ]
# END IF
