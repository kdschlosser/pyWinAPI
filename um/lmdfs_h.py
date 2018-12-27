import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMDFS_ = None
DFS_FORCE_REMOVE = None
_DFSFSCTL_ = None


class _DFS_TARGET_PRIORITY(ctypes.Structure):
    pass


DFS_TARGET_PRIORITY = _DFS_TARGET_PRIORITY
PDFS_TARGET_PRIORITY = POINTER(_DFS_TARGET_PRIORITY)


class _DFS_INFO_1(ctypes.Structure):
    pass


DFS_INFO_1 = _DFS_INFO_1
PDFS_INFO_1 = POINTER(_DFS_INFO_1)
LPDFS_INFO_1 = POINTER(_DFS_INFO_1)


class _DFS_INFO_1_32(ctypes.Structure):
    pass


DFS_INFO_1_32 = _DFS_INFO_1_32
PDFS_INFO_1_32 = POINTER(_DFS_INFO_1_32)
LPDFS_INFO_1_32 = POINTER(_DFS_INFO_1_32)


class _DFS_INFO_2(ctypes.Structure):
    pass


DFS_INFO_2 = _DFS_INFO_2
PDFS_INFO_2 = POINTER(_DFS_INFO_2)
LPDFS_INFO_2 = POINTER(_DFS_INFO_2)


class _DFS_INFO_2_32(ctypes.Structure):
    pass


DFS_INFO_2_32 = _DFS_INFO_2_32
PDFS_INFO_2_32 = POINTER(_DFS_INFO_2_32)
LPDFS_INFO_2_32 = POINTER(_DFS_INFO_2_32)


class _DFS_STORAGE_INFO(ctypes.Structure):
    pass


DFS_STORAGE_INFO = _DFS_STORAGE_INFO
PDFS_STORAGE_INFO = POINTER(_DFS_STORAGE_INFO)
LPDFS_STORAGE_INFO = POINTER(_DFS_STORAGE_INFO)


class _DFS_STORAGE_INFO_0_32(ctypes.Structure):
    pass


DFS_STORAGE_INFO_0_32 = _DFS_STORAGE_INFO_0_32
PDFS_STORAGE_INFO_0_32 = POINTER(_DFS_STORAGE_INFO_0_32)
LPDFS_STORAGE_INFO_0_32 = POINTER(_DFS_STORAGE_INFO_0_32)


class _DFS_STORAGE_INFO_1(ctypes.Structure):
    pass


DFS_STORAGE_INFO_1 = _DFS_STORAGE_INFO_1
PDFS_STORAGE_INFO_1 = POINTER(_DFS_STORAGE_INFO_1)
LPDFS_STORAGE_INFO_1 = POINTER(_DFS_STORAGE_INFO_1)


class _DFS_INFO_3(ctypes.Structure):
    pass


DFS_INFO_3 = _DFS_INFO_3
PDFS_INFO_3 = POINTER(_DFS_INFO_3)
LPDFS_INFO_3 = POINTER(_DFS_INFO_3)


class _DFS_INFO_3_32(ctypes.Structure):
    pass


DFS_INFO_3_32 = _DFS_INFO_3_32
PDFS_INFO_3_32 = POINTER(_DFS_INFO_3_32)
LPDFS_INFO_3_32 = POINTER(_DFS_INFO_3_32)


class _DFS_INFO_4(ctypes.Structure):
    pass


DFS_INFO_4 = _DFS_INFO_4
PDFS_INFO_4 = POINTER(_DFS_INFO_4)
LPDFS_INFO_4 = POINTER(_DFS_INFO_4)


class _DFS_INFO_4_32(ctypes.Structure):
    pass


DFS_INFO_4_32 = _DFS_INFO_4_32
PDFS_INFO_4_32 = POINTER(_DFS_INFO_4_32)
LPDFS_INFO_4_32 = POINTER(_DFS_INFO_4_32)


class _DFS_INFO_5(ctypes.Structure):
    pass


DFS_INFO_5 = _DFS_INFO_5
PDFS_INFO_5 = POINTER(_DFS_INFO_5)
LPDFS_INFO_5 = POINTER(_DFS_INFO_5)


class _DFS_INFO_6(ctypes.Structure):
    pass


DFS_INFO_6 = _DFS_INFO_6
PDFS_INFO_6 = POINTER(_DFS_INFO_6)
LPDFS_INFO_6 = POINTER(_DFS_INFO_6)


class _DFS_INFO_7(ctypes.Structure):
    pass


DFS_INFO_7 = _DFS_INFO_7
PDFS_INFO_7 = POINTER(_DFS_INFO_7)
LPDFS_INFO_7 = POINTER(_DFS_INFO_7)


class _DFS_INFO_8(ctypes.Structure):
    pass


DFS_INFO_8 = _DFS_INFO_8
PDFS_INFO_8 = POINTER(_DFS_INFO_8)
LPDFS_INFO_8 = POINTER(_DFS_INFO_8)


class _DFS_INFO_9(ctypes.Structure):
    pass


DFS_INFO_9 = _DFS_INFO_9
PDFS_INFO_9 = POINTER(_DFS_INFO_9)
LPDFS_INFO_9 = POINTER(_DFS_INFO_9)


class _DFS_INFO_50(ctypes.Structure):
    pass


DFS_INFO_50 = _DFS_INFO_50
PDFS_INFO_50 = POINTER(_DFS_INFO_50)
LPDFS_INFO_50 = POINTER(_DFS_INFO_50)


class _DFS_INFO_100(ctypes.Structure):
    pass


DFS_INFO_100 = _DFS_INFO_100
PDFS_INFO_100 = POINTER(_DFS_INFO_100)
LPDFS_INFO_100 = POINTER(_DFS_INFO_100)


class _DFS_INFO_101(ctypes.Structure):
    pass


DFS_INFO_101 = _DFS_INFO_101
PDFS_INFO_101 = POINTER(_DFS_INFO_101)
LPDFS_INFO_101 = POINTER(_DFS_INFO_101)


class _DFS_INFO_102(ctypes.Structure):
    pass


DFS_INFO_102 = _DFS_INFO_102
PDFS_INFO_102 = POINTER(_DFS_INFO_102)
LPDFS_INFO_102 = POINTER(_DFS_INFO_102)


class _DFS_INFO_103(ctypes.Structure):
    pass


DFS_INFO_103 = _DFS_INFO_103
PDFS_INFO_103 = POINTER(_DFS_INFO_103)
LPDFS_INFO_103 = POINTER(_DFS_INFO_103)


class _DFS_INFO_104(ctypes.Structure):
    pass


DFS_INFO_104 = _DFS_INFO_104
PDFS_INFO_104 = POINTER(_DFS_INFO_104)
LPDFS_INFO_104 = POINTER(_DFS_INFO_104)


class _DFS_INFO_105(ctypes.Structure):
    pass


DFS_INFO_105 = _DFS_INFO_105
PDFS_INFO_105 = POINTER(_DFS_INFO_105)
LPDFS_INFO_105 = POINTER(_DFS_INFO_105)


class _DFS_INFO_106(ctypes.Structure):
    pass


DFS_INFO_106 = _DFS_INFO_106
PDFS_INFO_106 = POINTER(_DFS_INFO_106)
LPDFS_INFO_106 = POINTER(_DFS_INFO_106)


class _DFS_INFO_107(ctypes.Structure):
    pass


DFS_INFO_107 = _DFS_INFO_107
PDFS_INFO_107 = POINTER(_DFS_INFO_107)
LPDFS_INFO_107 = POINTER(_DFS_INFO_107)


class _DFS_INFO_150(ctypes.Structure):
    pass


DFS_INFO_150 = _DFS_INFO_150
PDFS_INFO_150 = POINTER(_DFS_INFO_150)
LPDFS_INFO_150 = POINTER(_DFS_INFO_150)


class _DFS_INFO_200(ctypes.Structure):
    pass


DFS_INFO_200 = _DFS_INFO_200
PDFS_INFO_200 = POINTER(_DFS_INFO_200)
LPDFS_INFO_200 = POINTER(_DFS_INFO_200)


class _DFS_INFO_300(ctypes.Structure):
    pass


DFS_INFO_300 = _DFS_INFO_300
PDFS_INFO_300 = POINTER(_DFS_INFO_300)
LPDFS_INFO_300 = POINTER(_DFS_INFO_300)


class DFS_SITENAME_INFO(ctypes.Structure):
    pass


PDFS_SITENAME_INFO = POINTER(DFS_SITENAME_INFO)
LPDFS_SITENAME_INFO = POINTER(DFS_SITENAME_INFO)


class DFS_SITELIST_INFO(ctypes.Structure):
    pass


PDFS_SITELIST_INFO = POINTER(DFS_SITELIST_INFO)
LPDFS_SITELIST_INFO = POINTER(DFS_SITELIST_INFO)


class _DFS_SUPPORTED_NAMESPACE_VERSION_INFO(ctypes.Structure):
    pass


DFS_SUPPORTED_NAMESPACE_VERSION_INFO = _DFS_SUPPORTED_NAMESPACE_VERSION_INFO
PDFS_SUPPORTED_NAMESPACE_VERSION_INFO = POINTER(_DFS_SUPPORTED_NAMESPACE_VERSION_INFO)


class DFS_GET_PKT_ENTRY_STATE_ARG(ctypes.Structure):
    pass


PDFS_GET_PKT_ENTRY_STATE_ARG = POINTER(DFS_GET_PKT_ENTRY_STATE_ARG)


# /* + + BUILD Version: 0001 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmdfs.h Abstract:
# This file contains structures, function prototypes, and definitions for the
# NetDfs API Environment: User Mode - Win32 Notes: You must include <windef.h>
# and <lmcons.h> before this file. --
if not defined(_LMDFS_):
    from pyWinAPI.shared.lmcons_h import *  # NOQA
    from pyWinAPI.um.winnt_h import * # NOQA

    _LMDFS_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if defined(__cplusplus):
            pass
        # END IF

        # DFS Volume state
        DFS_VOLUME_STATES = 0xF
        DFS_VOLUME_STATE_OK = 1
        DFS_VOLUME_STATE_INCONSISTENT = 2
        DFS_VOLUME_STATE_OFFLINE = 3
        DFS_VOLUME_STATE_ONLINE = 4

        # These are valid for setting the volume state on the root
        # These are available to force a resynchronize on the root
        # volume or to put it in a standby mode.
        DFS_VOLUME_STATE_RESYNCHRONIZE = 0x10
        DFS_VOLUME_STATE_STANDBY = 0x20

        # When supported by a DFS namespace, the local state on
        # the DFS root target is refreshed with information from
        # the master state in the DFS metadata forcibly.
        DFS_VOLUME_STATE_FORCE_SYNC = 0x40

        # These are valid on getting the volume state on the root
        # These are available to determine the flavor of DFS
        # A few bits are reserved to determine the flavor of the DFS root.
        # To get the flavor, and the state with DFS_VOLUME_FLAVORS.
        # (_state & DFS_VOLUME_FLAVORS) will tell you the flavor of the dfs
        # root.
        DFS_VOLUME_FLAVORS = 0x0300
        DFS_VOLUME_FLAVOR_UNUSED1 = 0x0000
        DFS_VOLUME_FLAVOR_STANDALONE = 0x0100
        DFS_VOLUME_FLAVOR_AD_BLOB = 0x0200
        DFS_STORAGE_FLAVOR_UNUSED2 = 0x0300

        # DFS Storage State
        DFS_STORAGE_STATES = 0xF
        DFS_STORAGE_STATE_OFFLINE = 1
        DFS_STORAGE_STATE_ONLINE = 2
        DFS_STORAGE_STATE_ACTIVE = 4

        # Priority of a DFS target consists of the
        # tuple <priority class, priority rank>. Priority
        # ranks are valid only within a priority class and
        # not across priority classes.
        # Priority rank is 0-n, where 0 is highest rank.
        # We have consciously chosen 0 to indicate the
        # "normal" priority class, i.e. one that would
        # be used if target priorities aren't used.
        # The members of the enumeration have been explicitly
        # set in a specific order (in the enumeration).
        # We need the MIDL_PASS decoration to force sending
        # the enums as 32-bit values instead of the default
        # 16-bit values for enums.
        if defined(MIDL_PASS):
            class _DFS_TARGET_PRIORITY_CLASS(ENUM):
                pass
        else:
            class _DFS_TARGET_PRIORITY_CLASS(ENUM):
                pass
        # END IF

        _DFS_TARGET_PRIORITY_CLASS.DfsInvalidPriorityClass = -1
        _DFS_TARGET_PRIORITY_CLASS.DfsSiteCostNormalPriorityClass = 0
        _DFS_TARGET_PRIORITY_CLASS.DfsGlobalHighPriorityClass = 1
        _DFS_TARGET_PRIORITY_CLASS.DfsSiteCostHighPriorityClass = 2
        _DFS_TARGET_PRIORITY_CLASS.DfsSiteCostLowPriorityClass = 3
        _DFS_TARGET_PRIORITY_CLASS.DfsGlobalLowPriorityClass = 4
        DFS_TARGET_PRIORITY_CLASS = _DFS_TARGET_PRIORITY_CLASS

        _DFS_TARGET_PRIORITY._fields_ = [
            ('TargetPriorityClass', DFS_TARGET_PRIORITY_CLASS),
            # Priority rank of target.
            ('TargetPriorityRank', USHORT),
            # Must be set to 0.
            ('Reserved', USHORT),
        ]
        # Level 1:
        # Dfs name for the top of this piece of storage
        _DFS_INFO_1._fields_ = [
            ('EntryPath', LPWSTR),
        ]
        if defined(_WIN64):
            # WOW64 support: Permit 32-bit callers to use 64-bit
            # driver.
            # Dfs name for the top of this volume
            _DFS_INFO_1_32._fields_ = [
                ('EntryPath', ULONG),
            ]
        # END IF  _WIN64

        # Level 2:
        # Dfs name for the top of this volume
        _DFS_INFO_2._fields_ = [
            ('EntryPath', LPWSTR),
            # Comment for this volume
            ('Comment', LPWSTR),
            # State of this volume, one of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Number of storages for this volume
            ('NumberOfStorages', DWORD),
        ]
        if defined(_WIN64):
            # WOW64 support: Permit 32-bit callers to use 64-bit
            # driver.
            # Dfs name for the top of this volume
            _DFS_INFO_2_32._fields_ = [
                ('EntryPath', ULONG),
                # Comment for this volume
                ('Comment', ULONG),
                # State of this volume, one of DFS_VOLUME_STATE_*
                ('State', DWORD),
                # Number of storage servers for this volume
                ('NumberOfStorages', DWORD),
            ]
        # END IF  _WIN64

        # State of this storage, one of DFS_STORAGE_STATE_*
        _DFS_STORAGE_INFO._fields_ = [
            ('State', ULONG),
            # Name of server hosting this storage
            ('ServerName', LPWSTR),
            # Name of share hosting this storage
            ('ShareName', LPWSTR),
        ]
        if defined(_WIN64):
            # We should be calling this structure DFS_STORAGE_INFO_32 as
            # per
            # convention. However, we don't want to pollute the namespace
            # of new
            # types that have been defined
            # (for example, DFS_STORAGE_INFO_1) as
            # enhancements to the "base" DFS_STORAGE_INFO structure. Hence,
            # we define the WOW64 support structure as
            # DFS_STORAGE_INFO_0_32.
            # State of this storage, one of DFS_STORAGE_STATE_*
            _DFS_STORAGE_INFO_0_32._fields_ = [
                ('State', ULONG),
                # Name of server hosting this storage
                ('ServerName', ULONG),
                # Name of share hosting this storage
                ('ShareName', ULONG),
            ]
        # END IF   _WIN64.

        # WOW64 support: Permit 32-bit callers to use 64-bit
        # driver.
        # State of this target, one of DFS_TARGET_STATE_*
        _DFS_STORAGE_INFO_1._fields_ = [
            ('State', ULONG),
            # Name of server hosting this target
            ('ServerName', LPWSTR),
            # Name of share hosting this target
            ('ShareName', LPWSTR),
            # Priority of this target.
            ('TargetPriority', DFS_TARGET_PRIORITY),
        ]

        # Level 3:
        # Dfs name for the top of this volume
        _TEMP__DFS_INFO_3 = [
            ('EntryPath', LPWSTR),
            # Comment for this volume
            ('Comment', LPWSTR),
            # State of this volume, one of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Number of storage servers for this volume
            ('NumberOfStorages', DWORD),
        ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_3 += [
                ('Storage', LPDFS_STORAGE_INFO),
            ]
        else:
            _TEMP__DFS_INFO_3 += [
                # An array (of NumberOfStorages elements) of
                ('Storage', LPDFS_STORAGE_INFO),
            ]
        # END IF   MIDL_PASS

        _DFS_INFO_3._fields_ = _TEMP__DFS_INFO_3

        if defined(_WIN64):
            # WOW64 support: Permit 32-bit callers to use 64-bit
            # driver.
            # Dfs name for the top of this volume
            _DFS_INFO_3_32._fields_ = [
                ('EntryPath', ULONG),
                # Comment for this volume
                ('Comment', ULONG),
                # State of this volume, one of DFS_VOLUME_STATE_*
                ('State', DWORD),
                # Number of storage servers for this volume
                ('NumberOfStorages', DWORD),
                # An array (of NumberOfStorages elements) of
                ('Storage', ULONG),
            ]
        # END IF  _WIN64

        # Level 4:
        # Dfs name for the top of this volume
        _TEMP__DFS_INFO_4 = [
            ('EntryPath', LPWSTR),
            # Comment for this volume
            ('Comment', LPWSTR),
            # State of this volume, one of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Timeout, in seconds, of this junction point
            ('Timeout', ULONG),
            # Guid of this junction point
            ('Guid', GUID),
            # Number of storage servers for this volume
            ('NumberOfStorages', DWORD),
        ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_4 += [
                ('Storage', LPDFS_STORAGE_INFO),
            ]
        else:
            _TEMP__DFS_INFO_4 += [
                # An array (of NumberOfStorages elements) of
                ('Storage', LPDFS_STORAGE_INFO),
            ]
        # END IF   MIDL_PASS

        _DFS_INFO_4._fields_ = _TEMP__DFS_INFO_4

        if defined(_WIN64):
            # WOW64 support: Permit 32-bit callers to use 64-bit
            # driver.
            # Dfs name for the top of this volume
            _DFS_INFO_4_32._fields_ = [
                ('EntryPath', ULONG),
                # Comment for this volume
                ('Comment', ULONG),
                # State of this volume, one of DFS_VOLUME_STATE_*
                ('State', DWORD),
                # Timeout, in seconds, of this junction point
                ('Timeout', ULONG),
                # Guid of this junction point
                ('Guid', GUID),
                # Number of storage servers for this volume
                ('NumberOfStorages', DWORD),
                # An array (of NumberOfStorages elements) of
                ('Storage', ULONG),
            ]
        # END IF  _WIN64

        # Level 5:
        # Name of DFS namespace, DFS root name.
        _DFS_INFO_5._fields_ = [
            ('EntryPath', LPWSTR),
            # Comment for root/link.
            ('Comment', LPWSTR),
            # State of the root/link, one of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Referral TTL, in seconds, of root/link.
            ('Timeout', ULONG),
            # GUID of this root/link.
            ('Guid', GUID),
            # Properties of root/link. One of DFS_PROPERTY_FLAG_*
            ('PropertyFlags', ULONG),
            # Size of Active Directory BLOB for a domain-based
            ('MetadataSize', ULONG),
            # Number of storage servers for this volume
            ('NumberOfStorages', DWORD),
        ]

        # Level 6:
        # Name of DFS namespace, DFS root name.
        _TEMP__DFS_INFO_6 = [
            ('EntryPath', LPWSTR),
            # Comment for root/link.
            ('Comment', LPWSTR),
            # State of the root/link, one of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Referral TTL, in seconds, of root/link.
            ('Timeout', ULONG),
            # GUID of this root/link.
            ('Guid', GUID),
            # Properties of root/link. One of DFS_PROPERTY_FLAG_*
            ('PropertyFlags', ULONG),
            # Size of Active Directory BLOB for a domain-based
            ('MetadataSize', ULONG),
            # Number of targets for this root/link.
            ('NumberOfStorages', DWORD),
        ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_6 += [
                ('Storage', LPDFS_STORAGE_INFO_1),
            ]
        else:
            _TEMP__DFS_INFO_6 += [
                # An array (of NumberOfStorages elements) of
                ('Storage', LPDFS_STORAGE_INFO_1),
            ]
        # END IF   MIDL_PASS

        _DFS_INFO_6._fields_ = _TEMP__DFS_INFO_6

        # Level 7:
        # Guid representation of the version/generation
        _DFS_INFO_7._fields_ = [
            ('GenerationGuid', GUID),
        ]

        # Level 8:
        # Name of DFS namespace, DFS root name.
        _TEMP__DFS_INFO_8 = [
            ('EntryPath', LPWSTR),
            # Comment for root/link.
            ('Comment', LPWSTR),
            # State of the root/link, one of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Referral TTL, in seconds, of root/link.
            ('Timeout', ULONG),
            # GUID of this root/link.
            ('Guid', GUID),
            # Properties of root/link. One of DFS_PROPERTY_FLAG_*
            ('PropertyFlags', ULONG),
            # Size of Active Directory BLOB for a domain-based
            ('MetadataSize', ULONG),
        ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_8 += [
                # For use by the RPC marshalling code only.
                ('SecurityDescriptorLength', ULONG),
                # on disk).
                ('pSecurityDescriptor', PUCHAR),
            ]
        else:
            _TEMP__DFS_INFO_8 += [
                ('SdLengthReserved', ULONG),
                ('pSecurityDescriptor', PSECURITY_DESCRIPTOR),
            ]
        # END IF

        _TEMP__DFS_INFO_8 += [
            # Number of storage servers for this volume
            ('NumberOfStorages', DWORD),
        ]
        _DFS_INFO_8._fields_ = _TEMP__DFS_INFO_8

        # Level 9:
        # Name of DFS namespace, DFS root name.
        _TEMP__DFS_INFO_9 = [
            ('EntryPath', LPWSTR),
            # Comment for root/link.
            ('Comment', LPWSTR),
            # State of the root/link, one of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Referral TTL, in seconds, of root/link.
            ('Timeout', ULONG),
            # GUID of this root/link.
            ('Guid', GUID),
            # Properties of root/link. One of DFS_PROPERTY_FLAG_*
            ('PropertyFlags', ULONG),
            # Size of Active Directory BLOB for a domain-based
            ('MetadataSize', ULONG),
        ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_9 += [
                # For use by the RPC marshalling code only.
                ('SecurityDescriptorLength', ULONG),
                # on disk).
                ('pSecurityDescriptor', PUCHAR),
            ]
        else:
            _TEMP__DFS_INFO_9 += [
                ('SdLengthReserved', ULONG),
                ('pSecurityDescriptor', PSECURITY_DESCRIPTOR),
            ]
        # END IF

        _TEMP__DFS_INFO_9 += [
                # Number of targets for this root/link.
            ('NumberOfStorages', DWORD),
         ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_9 += [
                ('Storage', LPDFS_STORAGE_INFO_1),
            ]
        else:
            _TEMP__DFS_INFO_9 += [
                # An array (of NumberOfStorages elements) of
                ('Storage', LPDFS_STORAGE_INFO_1),
            ]
        # END IF   MIDL_PASS

        _DFS_INFO_9._fields_ = _TEMP__DFS_INFO_9

        # The "insite" flag. When set, only targets in the same
        # site as the client are returned.
        # Valid for domain/standalone roots/links
        DFS_PROPERTY_FLAG_INSITE_REFERRALS = 0x00000001

        # "Root scalability" mode. When set, DFS server polls
        # the nearest DC instead of PDC to check for DFS namespace
        # changes. Valid only for domain roots.
        DFS_PROPERTY_FLAG_ROOT_SCALABILITY = 0x00000002

        # Enables Active Directory site costing of targets. When enabled,
        # targets are grouped into sets of increasing site costs from
        # DFS client to target. Each set has targets of same cost.
        # If not set, there are only two sets: set of targets in same
        # site as client and set of targets not in the same site as the
        # client.
        # The latter is called "site awareness".
        # Valid only domain/standalone roots
        DFS_PROPERTY_FLAG_SITE_COSTING = 0x00000004

        # Should the DFS client attempt to failback to a closer target
        # when it is available after failing over to a non-optimal target?
        # Valid for domain/standalone roots/links.
        DFS_PROPERTY_FLAG_TARGET_FAILBACK = 0x00000008

        # Bit will be 1 if the DFS root is clustered. Cannot be set
        # using the NetDfsSetInfo() API.
        DFS_PROPERTY_FLAG_CLUSTER_ENABLED = 0x00000010

        # When set by the caller, Access-Based Directory Enumeration
        # support
        # is enabled on all the DFS root target share of the DFS namespace.
        # Valid only for DFS namespaces which support the capability
        # DFS_NAMESPACE_CAPABILITY_ABDE. Valid only on the DFS namespace
        # root
        # and not on root targets, link or link targets.
        # This property must be enabled to associate security descriptor
        # with a DFS link.
        DFS_PROPERTY_FLAG_ABDE = 0x00000020

        # The PropertyFlags field of DFS_INFO_5, DFS_INFO_6,
        # DFS_INFO_103, DFS_INFO_105 & DFS_INFO_107.
        DFS_VALID_PROPERTY_FLAGS = (
            DFS_PROPERTY_FLAG_INSITE_REFERRALS |
            DFS_PROPERTY_FLAG_ROOT_SCALABILITY |
            DFS_PROPERTY_FLAG_SITE_COSTING |
            DFS_PROPERTY_FLAG_TARGET_FAILBACK |
            DFS_PROPERTY_FLAG_CLUSTER_ENABLED |
            DFS_PROPERTY_FLAG_ABDE
        )

        # Level 50:
        # DFS metadata version and capabilities of an existing
        # DFS namespace.
        _DFS_INFO_50._fields_ = [
            ('NamespaceMajorVersion', ULONG),
            ('NamespaceMinorVersion', ULONG),
            ('NamespaceCapabilities', ULONGLONG),
        ]

        # Level 100:
        # Comment for this volume or storage
        _DFS_INFO_100._fields_ = [
            ('Comment', LPWSTR),
        ]

        # Level 101:
        # State of this storage, one of DFS_STORAGE_STATE_*
        _DFS_INFO_101._fields_ = [
            ('State', DWORD),
        ]

        # Level 102:
        # Timeout, in seconds, of the junction
        _DFS_INFO_102._fields_ = [
            ('Timeout', ULONG),
        ]

        # Level 103:
        # Indicates which flags in PropertyFlags are valid.
        _DFS_INFO_103._fields_ = [
            ('PropertyFlagMask', ULONG),
            # Flag meaningful only if corresponding bit set in
            ('PropertyFlags', ULONG),
        ]

        # Level 104:
        # Priority of target.
        _DFS_INFO_104._fields_ = [
            ('TargetPriority', DFS_TARGET_PRIORITY),
        ]

        # Level 105:
        # Comment for this root/link.
        _DFS_INFO_105._fields_ = [
            ('Comment', LPWSTR),
            # State of this root/link. One of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Referral TTL, in seconds, of root/link.
            ('Timeout', ULONG),
            # Indicates which flags in PropertyFlags are valid.
            ('PropertyFlagMask', ULONG),
            # One of DFS_PROPERTY_FLAG_*
            ('PropertyFlags', ULONG),
        ]

        # Level 106:
        # State of this root/link target.
        _DFS_INFO_106._fields_ = [
            ('State', DWORD),
            # Priority of this target.
            ('TargetPriority', DFS_TARGET_PRIORITY),
        ]

        # Level 107:
        # Comment for this root/link.
        _TEMP__DFS_INFO_107 = [
            ('Comment', LPWSTR),
            # State of this root/link. One of DFS_VOLUME_STATE_*
            ('State', DWORD),
            # Referral TTL, in seconds, of root/link.
            ('Timeout', ULONG),
            # Indicates which flags in PropertyFlags are valid.
            ('PropertyFlagMask', ULONG),
            # One of DFS_PROPERTY_FLAG_*
            ('PropertyFlags', ULONG),
        ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_107 += [
                # For use by the RPC marshalling code only.
                ('SecurityDescriptorLength', ULONG),
                # on disk).
                ('pSecurityDescriptor', PUCHAR),
            ]
        else:
            _TEMP__DFS_INFO_107 += [
                ('SdLengthReserved', ULONG),
                ('pSecurityDescriptor', PSECURITY_DESCRIPTOR),
            ]
        # END IF

        _DFS_INFO_107._fields_ = _TEMP__DFS_INFO_107

        # Level 150:
        _TEMP__DFS_INFO_150 = [
        ]
        if defined(MIDL_PASS):
            _TEMP__DFS_INFO_150 += [
                # For use by the RPC marshalling code only.
                ('SecurityDescriptorLength', ULONG),
                # on disk).
                ('pSecurityDescriptor', PUCHAR),
            ]
        else:
            _TEMP__DFS_INFO_150 += [
                ('SdLengthReserved', ULONG),
                ('pSecurityDescriptor', PSECURITY_DESCRIPTOR),
            ]
        # END IF

        _DFS_INFO_150._fields_ = _TEMP__DFS_INFO_150

        # Level 200:
        # FtDfs name
        _DFS_INFO_200._fields_ = [
            ('FtDfsName', LPWSTR),
        ]

        # Level 300:
        _DFS_INFO_300._fields_ = [
            ('Flags', DWORD),
            # Dfs name
            ('DfsName', LPWSTR),
        ]

        # Add a new volume or additional storage for an existing volume at
        # DfsEntryPath.
        netapi32 = ctypes.windll.NETAPI32

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsAdd(
        # _In_ LPWSTR     DfsEntryPath, // DFS entry path for this added volume or storage
        # _In_ LPWSTR     ServerName, // Name of server hosting the storage
        # _In_ LPWSTR     ShareName, // Existing share name for the storage
        # _In_opt_ LPWSTR Comment, // Optional comment for this volume or storage
        # _In_  DWORD     Flags // See below. Zero for no flags.
        # );
        NetDfsAdd = netapi32.NetDfsAdd
        NetDfsAdd.restype = NET_API_STATUS

        # Flags:
        DFS_ADD_VOLUME = 1  # Add a new volume to the DFS if not already there
        DFS_RESTORE_VOLUME = 2  # Volume/Replica is being restored - do not verify share etc.

        # Setup/teardown API's for standard and FtDfs roots.
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsAddStdRoot(
        # _In_ LPWSTR     ServerName, // Server to remote to
        # _In_ LPWSTR     RootShare, // Share to make Dfs root
        # _In_opt_ LPWSTR Comment, // Comment
        # _In_  DWORD     Flags // Flags for operation.  Zero for no flags.
        # );
        NetDfsAddStdRoot = netapi32.NetDfsAddStdRoot
        NetDfsAddStdRoot.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsRemoveStdRoot(
        # _In_  LPWSTR ServerName, // Server to remote to
        # _In_  LPWSTR RootShare, // Share that host Dfs root
        # _Reserved_  DWORD  Flags // Flags for operation.  Zero for no flags.
        # );
        NetDfsRemoveStdRoot = netapi32.NetDfsRemoveStdRoot
        NetDfsRemoveStdRoot.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsAddFtRoot(
        # _In_ LPWSTR         ServerName, // Server to remote to
        # _In_ LPWSTR         RootShare, // Share to make Dfs root
        # _In_  LPWSTR        FtDfsName, // Name of FtDfs to create/join
        # _In_opt_ LPWSTR     Comment, // Comment
        # _In_ DWORD          Flags // Flags for operation.  Zero for no flags.
        # );
        NetDfsAddFtRoot = netapi32.NetDfsAddFtRoot
        NetDfsAddFtRoot.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsRemoveFtRoot(
        # _In_ LPWSTR         ServerName, // Server to remote to
        # _In_ LPWSTR         RootShare, // Share that host Dfs root
        # _In_ LPWSTR         FtDfsName, // Name of FtDfs to remove or unjoin from.
        # _Reserved_ DWORD    Flags // Flags for operation.  Zero for no flags.
        # );
        NetDfsRemoveFtRoot = netapi32.NetDfsRemoveFtRoot
        NetDfsRemoveFtRoot.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsRemoveFtRootForced(
        # _In_  LPWSTR        DomainName, // Name of domain the server is in
        # _In_  LPWSTR        ServerName, // Server to remote to
        # _In_  LPWSTR        RootShare, // Share that host Dfs root
        # _In_  LPWSTR        FtDfsName, // Name of FtDfs to remove or unjoin from.
        # _Reserved_ DWORD    Flags // Flags for operation.  Zero for no flags.
        # );
        NetDfsRemoveFtRootForced = netapi32.NetDfsRemoveFtRootForced
        NetDfsRemoveFtRootForced.restype = NET_API_STATUS

        # Flags for NetDfsSetDcAddress()
        NET_DFS_SETDC_FLAGS = 0x00000000
        NET_DFS_SETDC_TIMEOUT = 0x00000001
        NET_DFS_SETDC_INITPKT = 0x00000002

        # Structures used for site reporting. Last used in Windows 2000,
        # maintained for
        # the obsolete SRVSVC RPC API NetrDfsManagerReportSiteInfo.
        # Below
        _TEMP_DFS_SITENAME_INFO = [
            ('SiteFlags', ULONG),
        ]
        if defined(MIDL_PASS):
            _TEMP_DFS_SITENAME_INFO += [
                ('SiteName', LPWSTR),
            ]
        else:
            _TEMP_DFS_SITENAME_INFO += [
                ('SiteName', LPWSTR),
            ]
        # END IF

        DFS_SITENAME_INFO._fields_ = _TEMP_DFS_SITENAME_INFO

        # SiteFlags
        _TEMP_DFS_SITELIST_INFO = [
            ('cSites', ULONG),
        ]
        if defined(MIDL_PASS):
            _TEMP_DFS_SITELIST_INFO += [
                ('Site', DFS_SITENAME_INFO * 1),
            ]
        else:
            _TEMP_DFS_SITELIST_INFO += [
                ('Site', DFS_SITENAME_INFO * 1),
            ]
        # END IF

        DFS_SITELIST_INFO._fields_ = _TEMP_DFS_SITELIST_INFO

        # Remove a volume or additional storage for volume from the Dfs at
        # DfsEntryPath. When applied to the last storage in a volume,
        # removes
        # the volume from the DFS.
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsRemove(
        # _In_ LPWSTR     DfsEntryPath, // DFS entry path for this added volume or storage
        # _In_opt_ LPWSTR ServerName, // Name of server hosting the storage
        # _In_opt_ LPWSTR ShareName // Name of share hosting the storage
        # );
        NetDfsRemove = netapi32.NetDfsRemove
        NetDfsRemove.restype = NET_API_FUNCTION

        # Get information about all of the volumes in the Dfs. DfsName is
        # the "server" part of the UNC name used to refer to this
        # particular Dfs.
        # Valid levels are 1-5, 200, 300
        # _When_(Level == 1, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_1))))
        # _When_(Level == 2, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_2))))
        # _When_(Level == 3, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_3))))
        # _When_(Level == 4, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_4))))
        # _When_(Level == 5, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_5))))
        # _When_(Level == 6, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_6))))
        # _When_(Level == 8, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_8))))
        # _When_(Level == 9, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_9))))
        # _When_(Level == 200, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_200))))
        # _When_(Level == 300, _At_(Buffer, _Outptr_result_bytebuffer_(*EntriesRead * (ctypes.sizeof(DFS_INFO_300))))
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsEnum(
        # _In_ LPWSTR         DfsName, // Name of the Dfs for enumeration
        # _In_ DWORD          Level, // Level of information requested
        # _In_ DWORD          PrefMaxLen, // Advisory, but -1 means "get it all"
        # _Out_ LPBYTE        *Buffer, // API allocates and returns buffer with requested info
        # _Out_ LPDWORD       EntriesRead, // Number of entries returned
        # _Inout_ LPDWORD     ResumeHandle // Must be 0 on first call, reused on subsequent calls
        # );
        NetDfsEnum = netapi32.NetDfsEnum
        NetDfsEnum.restype = NET_API_STATUS

        # Get information about the volume or storage.
        # If ServerName and ShareName are specified, the information
        # returned
        # is specific to that server and share, else the information is
        # specific
        # to the volume as a whole.
        # Valid levels are 1-5, 100
        # _When_(Level == 1, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_1))))
        # _When_(Level == 2, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_2))))
        # _When_(Level == 3, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_3))))
        # _When_(Level == 4, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_4))))
        # _When_(Level == 5, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_5))))
        # _When_(Level == 6, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_6))))
        # _When_(Level == 7, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_7))))
        # _When_(Level == 8, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_8))))
        # _When_(Level == 9, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_9))))
        # _When_(Level == 50, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_50))))
        # _When_(Level == 100, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_100))))
        # _When_(Level == 150, _At_(Buffer, _Outptr_result_bytebuffer_((ctypes.sizeof(DFS_INFO_150))))
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsGetInfo(
        # _In_ LPWSTR         DfsEntryPath, // DFS entry path for the volume
        # _In_opt_ LPWSTR     ServerName, // Name of server hosting a storage
        # _In_opt_ LPWSTR     ShareName, // Name of share on server serving the volume
        # _In_ DWORD          Level, // Level of information requested
        # _Out_ LPBYTE        *Buffer // API allocates and returns buffer with requested info
        # );
        NetDfsGetInfo = netapi32.NetDfsGetInfo
        NetDfsGetInfo.restype = NET_API_STATUS

        # Set info about the volume or storage.
        # If ServerName and ShareName are specified, the information set is
        # specific to that server and share, else the information is
        # specific
        # to the volume as a whole.
        # Valid levels are 100, 101 and 102
        # _When_(Level == 101, _At_(Buffer, _In_reads_bytes_((ctypes.sizeof(DFS_INFO_101))))
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsSetInfo(
        # _In_ LPWSTR         DfsEntryPath, // DFS entry path for the volume
        # _In_opt_ LPWSTR     ServerName, // Name of server hosting a storage
        # _In_opt_ LPWSTR     ShareName, // Name of share hosting a storage
        # _In_ DWORD          Level, // Level of information to be set
        # _In_ LPBYTE         Buffer // Buffer holding information
        # );
        NetDfsSetInfo = netapi32.NetDfsSetInfo
        NetDfsSetInfo.restype = NET_API_STATUS

        # Get client's cached information about the volume or storage.
        # If ServerName and ShareName are specified, the information
        # returned
        # is specific to that server and share, else the information is
        # specific
        # to the volume as a whole.
        # Valid levels are 1-4
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsGetClientInfo(
        # _In_ LPWSTR         DfsEntryPath, // DFS entry path for the volume
        # _In_opt_ LPWSTR     ServerName, // Name of server hosting a storage
        # _In_opt_ LPWSTR     ShareName, // Name of share on server serving the volume
        # _In_ DWORD          Level, // Level of information requested
        # _Out_ LPBYTE        *Buffer // API allocates and returns buffer with requested info
        # );
        NetDfsGetClientInfo = netapi32.NetDfsGetClientInfo
        NetDfsGetClientInfo.restype = NET_API_STATUS

        # Set client's cached info about the volume or storage.
        # If ServerName and ShareName are specified, the information set is
        # specific to that server and share, else the information is
        # specific
        # to the volume as a whole.
        # Valid levels are 101 and 102.
        # _When_(Level == 101, _At_(Buffer, _In_reads_bytes_((ctypes.sizeof(DFS_INFO_101))))
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsSetClientInfo(
        # _In_ LPWSTR         DfsEntryPath, // DFS entry path for the volume
        # _In_opt_ LPWSTR     ServerName, // Name of server hosting a storage
        # _In_opt_ LPWSTR     ShareName, // Name of share hosting a storage
        # _In_ DWORD          Level, // Level of information to be set
        # _In_ LPBYTE         Buffer // Buffer holding information
        # );
        NetDfsSetClientInfo = netapi32.NetDfsSetClientInfo
        NetDfsSetClientInfo.restype = NET_API_STATUS

        # Move a DFS volume and all subordinate volumes from one place in
        # the
        # DFS to another place in the DFS.
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsMove(
        # _In_ LPWSTR     OldDfsEntryPath, // Current DFS entry path for this volume
        # _In_ LPWSTR     NewDfsEntryPath, // New DFS entry path for this volume
        # _In_ ULONG      Flags
        # );
        NetDfsMove = netapi32.NetDfsMove
        NetDfsMove.restype = NET_API_STATUS

        # Flags accepted by NetDfsMove
        # This indicates that if a colliding link is found it should be
        # replaced
        DFS_MOVE_FLAG_REPLACE_IF_EXISTS = 0x00000001
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsRename(
        # _In_ LPWSTR     Path, // Current Win32 path in a Dfs
        # _In_ LPWSTR     NewPath // New Win32 path in the same Dfs
        # );
        NetDfsRename = netapi32.NetDfsRename
        NetDfsRename.restype = NET_API_STATUS

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsAddRootTarget(
        # _In_        LPWSTR  pDfsPath,
        # _In_opt_    LPWSTR  pTargetPath,
        # _In_        ULONG   MajorVersion,
        # _In_opt_    LPWSTR  pComment,
        # _In_        ULONG   Flags
        # );
        NetDfsAddRootTarget = netapi32.NetDfsAddRootTarget
        NetDfsAddRootTarget.restype = NET_API_STATUS

        # Reuse existing definition used by NetrDfsRemoveFtRoot().
        if not defined(DFS_FORCE_REMOVE):
            DFS_FORCE_REMOVE = 0x80000000
        # END IF

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsRemoveRootTarget(
        # _In_        LPWSTR  pDfsPath,
        # _In_opt_    LPWSTR  pTargetPath,
        # _In_        ULONG   Flags
        # );
        NetDfsRemoveRootTarget = netapi32.NetDfsRemoveRootTarget
        NetDfsRemoveRootTarget.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsGetSecurity(
        # _In_ LPWSTR                                                         DfsEntryPath,
        # _In_ SECURITY_INFORMATION                                           SecurityInformation,
        # _Outptr_result_bytebuffer_(*lpcbSecurityDescriptor) PSECURITY_DESCRIPTOR    *ppSecurityDescriptor,
        # _Out_ LPDWORD                                                       lpcbSecurityDescriptor
        # );
        NetDfsGetSecurity = netapi32.NetDfsGetSecurity
        NetDfsGetSecurity.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsSetSecurity(
        # _In_ LPWSTR                 DfsEntryPath,
        # _In_ SECURITY_INFORMATION   SecurityInformation,
        # _In_ PSECURITY_DESCRIPTOR   pSecurityDescriptor
        # );
        NetDfsSetSecurity = netapi32.NetDfsSetSecurity
        NetDfsSetSecurity.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsGetStdContainerSecurity(
        # _In_ LPWSTR                                                         MachineName,
        # _In_ SECURITY_INFORMATION                                           SecurityInformation,
        # _Outptr_result_bytebuffer_(*lpcbSecurityDescriptor) PSECURITY_DESCRIPTOR    *ppSecurityDescriptor,
        # _Out_ LPDWORD                                                       lpcbSecurityDescriptor
        # );
        NetDfsGetStdContainerSecurity = (
            netapi32.NetDfsGetStdContainerSecurity
        )
        NetDfsGetStdContainerSecurity.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsSetStdContainerSecurity(
        # _In_ LPWSTR                 MachineName,
        # _In_ SECURITY_INFORMATION   SecurityInformation,
        # _In_ PSECURITY_DESCRIPTOR   pSecurityDescriptor
        # );
        NetDfsSetStdContainerSecurity = (
            netapi32.NetDfsSetStdContainerSecurity
        )
        NetDfsSetStdContainerSecurity.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsGetFtContainerSecurity(
        # _In_ LPWSTR                                                         DomainName,
        # _In_ SECURITY_INFORMATION                                           SecurityInformation,
        # _Outptr_result_bytebuffer_(*lpcbSecurityDescriptor) PSECURITY_DESCRIPTOR    *ppSecurityDescriptor,
        # _Out_ LPDWORD                                                       lpcbSecurityDescriptor
        # );
        NetDfsGetFtContainerSecurity = (
            netapi32.NetDfsGetFtContainerSecurity
        )
        NetDfsGetFtContainerSecurity.restype = NET_API_STATUS

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsSetFtContainerSecurity(
        # _In_ LPWSTR                 DomainName,
        # _In_ SECURITY_INFORMATION   SecurityInformation,
        # _In_ PSECURITY_DESCRIPTOR   pSecurityDescriptor
        # );
        NetDfsSetFtContainerSecurity = (
            netapi32.NetDfsSetFtContainerSecurity
        )
        NetDfsSetFtContainerSecurity.restype = NET_API_STATUS

        # Origin of DFS namespace version information.
        class DFS_NAMESPACE_VERSION_ORIGIN(ENUM):
            DFS_NAMESPACE_VERSION_ORIGIN_COMBINED = 0
            DFS_NAMESPACE_VERSION_ORIGIN_SERVER = 1
            DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN = 2


        PDFS_NAMESPACE_VERSION_ORIGIN = POINTER(DFS_NAMESPACE_VERSION_ORIGIN)

        DFS_NAMESPACE_VERSION_ORIGIN_COMBINED = DFS_NAMESPACE_VERSION_ORIGIN.DFS_NAMESPACE_VERSION_ORIGIN_COMBINED
        DFS_NAMESPACE_VERSION_ORIGIN_SERVER = DFS_NAMESPACE_VERSION_ORIGIN.DFS_NAMESPACE_VERSION_ORIGIN_SERVER
        DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN = DFS_NAMESPACE_VERSION_ORIGIN.DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN

        # Capabilities:
        # Set of bit flags which indicates support for a specific
        # capability.
        # DFS namespace supports associating a security descriptor with
        # DFS link
        # for Access-Based Directory Enumeration purposes.
        DFS_NAMESPACE_CAPABILITY_ABDE = 0x0000000000000001

        _DFS_SUPPORTED_NAMESPACE_VERSION_INFO._fields_ = [
            # Valid only if DomainDfsMajorVersion != 0.
            ('DomainDfsMajorVersion', ULONG),
            ('DomainDfsMinorVersion', ULONG),
            ('DomainDfsCapabilities', ULONGLONG),
            # Valid only if StandaloneDfsMajorVersion != 0.
            ('StandaloneDfsMajorVersion', ULONG),
            ('StandaloneDfsMinorVersion', ULONG),
            ('StandaloneDfsCapabilities', ULONGLONG),
        ]

        # NET_API_STATUS NET_API_FUNCTION
        # NetDfsGetSupportedNamespaceVersion(
        # _In_        DFS_NAMESPACE_VERSION_ORIGIN            Origin,
        # _In_opt_    PWSTR                                   pName,
        # _Outptr_ PDFS_SUPPORTED_NAMESPACE_VERSION_INFO   *ppVersionInfo
        # );
        NetDfsGetSupportedNamespaceVersion = (
            netapi32.NetDfsGetSupportedNamespaceVersion
        )
        NetDfsGetSupportedNamespaceVersion.restype = NET_API_STATUS

        from pyWinAPI.shared.devioctl_h import * # NOQA

        if not defined(_DFSFSCTL_):
            FSCTL_DFS_BASE = 0

            FSCTL_DFS_GET_PKT_ENTRY_STATE = CTL_CODE(
                FSCTL_DFS_BASE,
                2031,
                METHOD_BUFFERED,
                FILE_ANY_ACCESS,
            )

            # FSCTL_DFS_GET_PKT_ENTRY_STATE Input Buffer
            # All the strings appear in Buffer in the same order as the
            # length fields. The strings
            # are not NULL terminated. The length values are in bytes.
            DFS_GET_PKT_ENTRY_STATE_ARG._fields_ = [
                ('DfsEntryPathLen', USHORT),
                ('ServerNameLen', USHORT),
                ('ShareNameLen', USHORT),
                ('Level', ULONG),
                ('Buffer', WCHAR * 1),
            ]
        # END IF

        if defined(__cplusplus):
            pass
        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
# END IF   _LMDFS_





