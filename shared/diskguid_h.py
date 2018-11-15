from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *


# + + Copyright (c) Microsoft Corporation. All rights reserved. Module Name:
# diskguid.h Abstract: GPT disk GUIDs. Revision History: - -
from pyWinAPI.shared.winapifamily_h import * # NOQA

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
    # GPT Partition Type GUIDs
    # need these GUIDs outside conditional includes so that user can
    # include <ntdddisk.h> in precompiled header
    # include <initguid.h> in a single source file
    # include <ntdddisk.h> in that source file a second time to instantiate
    # the GUIDs
    if defined(DEFINE_GUID):
        # Make sure FAR is defined...
        if not defined(FAR):
            if defined(_WIN32):
                FAR = 1
            else:
                FAR = 1
            # END IF
        # END IF

        # Define the GPT partition guids known by disk drivers and volume
        # managers.#  Basic data partition
        PARTITION_BASIC_DATA_GUID = DEFINE_GUID(
            0xEBD0A0A2,
            0xB9E5,
            0x4433,
            0x87,
            0xC0,
            0x68,
            0xB6,
            0xB7,
            0x26,
            0x99,
            0xC7
        )
        # BSP partition
        PARTITION_BSP_GUID = DEFINE_GUID(
            0x57434F53,
            0x4DF9,
            0x45B9,
            0x8E,
            0x9E,
            0x23,
            0x70,
            0xF0,
            0x06,
            0x45,
            0x7C
        )
        # Cluster metadata partition
        PARTITION_CLUSTER_GUID = DEFINE_GUID(
            0xDB97DBA9,
            0x0840,
            0x4BAE,
            0x97,
            0xF0,
            0xFF,
            0xB9,
            0xA3,
            0x27,
            0xC7,
            0xE1
        )
        # DPP partition
        PARTITION_DPP_GUID = DEFINE_GUID(
            0x57434F53,
            0x94CB,
            0x43F0,
            0xA5,
            0x33,
            0xD7,
            0x3C,
            0x10,
            0xCF,
            0xA5,
            0x7D
        )
        # Entry unused
        PARTITION_ENTRY_UNUSED_GUID = DEFINE_GUID(
            0x00000000,
            0x0000,
            0x0000,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00
        )
        # Logical Disk Manager data partition
        PARTITION_LDM_DATA_GUID = DEFINE_GUID(
            0xAF9B60A0,
            0x1431,
            0x4F62,
            0xBC,
            0x68,
            0x33,
            0x11,
            0x71,
            0x4A,
            0x69,
            0xAD
        )
        # Logical Disk Manager metadata partition
        PARTITION_LDM_METADATA_GUID = DEFINE_GUID(
            0x5808C8AA,
            0x7E8F,
            0x42E0,
            0x85,
            0xD2,
            0xE1,
            0xE9,
            0x04,
            0x34,
            0xCF,
            0xB3
        )
        # Main OS partition
        PARTITION_MAIN_OS_GUID = DEFINE_GUID(
            0x57434F53,
            0x8F45,
            0x405E,
            0x8A,
            0x23,
            0x18,
            0x6D,
            0x8A,
            0x43,
            0x30,
            0xD3
        )
        # Microsoft recovery partition
        PARTITION_MSFT_RECOVERY_GUID = DEFINE_GUID(
            0xDE94BBA4,
            0x06D1,
            0x4D40,
            0xA1,
            0x6A,
            0xBF,
            0xD5,
            0x01,
            0x79,
            0xD6,
            0xAC
        )
        # Microsoft reserved space
        PARTITION_MSFT_RESERVED_GUID = DEFINE_GUID(
            0xE3C9E316,
            0x0B5C,
            0x4DB8,
            0x81,
            0x7D,
            0xF9,
            0x2D,
            0xF0,
            0x02,
            0x15,
            0xAE
        )
        # Microsoft shadow copy partition
        PARTITION_MSFT_SNAPSHOT_GUID = DEFINE_GUID(
            0xCADDEBF1,
            0x4400,
            0x4DE8,
            0xB1,
            0x03,
            0x12,
            0x11,
            0x7D,
            0xCF,
            0x3C,
            0xCF
        )
        # OS data partition
        PARTITION_OS_DATA_GUID = DEFINE_GUID(
            0x57434F53,
            0x23F2,
            0x44D5,
            0xA8,
            0x30,
            0x67,
            0xBB,
            0xDA,
            0xA6,
            0x09,
            0xF9
        )
        # Patch partition
        PARTITION_PATCH_GUID = DEFINE_GUID(
            0x8967A686,
            0x96AA,
            0x6AA8,
            0x95,
            0x89,
            0xA8,
            0x42,
            0x56,
            0x54,
            0x10,
            0x90
        )
        # PreInstalled partition
        PARTITION_PRE_INSTALLED_GUID = DEFINE_GUID(
            0x57434F53,
            0x7FE0,
            0x4196,
            0x9B,
            0x42,
            0x42,
            0x7B,
            0x51,
            0x64,
            0x34,
            0x84
        )
        # Storage Spaces protective partition
        PARTITION_SPACES_GUID = DEFINE_GUID(
            0xE75CAF8F,
            0xF680,
            0x4CEE,
            0xAF,
            0xA3,
            0xB0,
            0x01,
            0xE5,
            0x6E,
            0xFC,
            0x2D
        )
        # EFI system partition
        PARTITION_SYSTEM_GUID = DEFINE_GUID(
            0xC12A7328,
            0xF81F,
            0x11D2,
            0xBA,
            0x4B,
            0x00,
            0xA0,
            0xC9,
            0x3E,
            0xC9,
            0x3B
        )
        # Windows system partition
        PARTITION_WINDOWS_SYSTEM_GUID = DEFINE_GUID(
            0x57434F53,
            0xE3E3,
            0x4631,
            0xA5,
            0xC5,
            0x26,
            0xD2,
            0x24,
            0x38,
            0x73,
            0xAA
        )
    # END IF
    if defined(__cplusplus):
        IsEqualPartitionType = IsEqualGUID
    else:
        def IsEqualPartitionType(_a, _b):
            return IsEqualGUID(_a, _b)
    # END IF
    def IsRecognizedGptPartition(_t):
        return (
            IsEqualPartitionType(_t, PARTITION_BSP_GUID) or
            IsEqualPartitionType(_t, PARTITION_DPP_GUID) or
            IsEqualPartitionType(_t, PARTITION_BASIC_DATA_GUID) or
            IsEqualPartitionType(_t, PARTITION_MAIN_OS_GUID) or
            IsEqualPartitionType(_t, PARTITION_MSFT_RECOVERY_GUID) or
            IsEqualPartitionType(_t, PARTITION_OS_DATA_GUID) or
            IsEqualPartitionType(_t, PARTITION_PRE_INSTALLED_GUID) or
            IsEqualPartitionType(_t, PARTITION_WINDOWS_SYSTEM_GUID)
        )
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
