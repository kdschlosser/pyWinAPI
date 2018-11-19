import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _RX_CONNECTION_ID(ctypes.Structure):
    pass


RX_CONNECTION_ID = _RX_CONNECTION_ID
PRX_CONNECTION_ID = POINTER(_RX_CONNECTION_ID)


class _RX_PREFIX_ENTRY(ctypes.Structure):
    pass


RX_PREFIX_ENTRY = _RX_PREFIX_ENTRY
PRX_PREFIX_ENTRY = POINTER(_RX_PREFIX_ENTRY)


class _RX_PREFIX_TABLE(ctypes.Structure):
    pass


RX_PREFIX_TABLE = _RX_PREFIX_TABLE
PRX_PREFIX_TABLE = POINTER(_RX_PREFIX_TABLE)


# /* + + Copyright (c) 1989 Microsoft Corporation Module Name: prefix.h
# Abstract: This module defines the data structures that enable the RDBSS to
# use the prefix package to catalog its server and netroot names. For the
# moment, file/directory names use the same stuff. Author: Revision History: -
# -

_RXPREFIX_ = None

if not defined(_RXPREFIX_):
    _RXPREFIX_ = 1

    from pyWinAPI.km.nodetype_h import * # NOQA
    from pyWinAPI.missing_structures_h import * # NOQA
    # this stuff is implemented in prefix.c
    # /* The current implementation uses a table that has as components:
    # 1) a prefix table 2) a queue 3) a version 4) a lock You use the lock in the normal way: shared to lookup; eclusive to change. the version changes eith each change. The reason that we have the queue is that the prefix table package allows caller to be enumerating at a time..... the Q/version approach allows multiple guys at a time. The Q could be used as a faster lookup for filenames but the prefix table is definitely the right thing for netroots.
    #
    rdbss = ctypes.windll.RDBSS

    # ULONG
    # RxTableComputeHashValue (
    # IN  PUNICODE_STRING Name
    # );

    RxTableComputeHashValue = rdbss.RxTableComputeHashValue
    RxTableComputeHashValue.restype = ULONG

    # PVOID
    # RxPrefixTableLookupName(
    # IN PRX_PREFIX_TABLE ThisTable,
    # IN PUNICODE_STRING CanonicalName,
    # OUT PUNICODE_STRING RemainingName,
    # IN PRX_CONNECTION_ID ConnectionId
    # );
    RxPrefixTableLookupName = rdbss.RxPrefixTableLookupName
    RxPrefixTableLookupName.restype = PVOID

    # PRX_PREFIX_ENTRY
    # RxPrefixTableInsertName (
    # IN OUT PRX_PREFIX_TABLE ThisTable,
    # IN OUT PRX_PREFIX_ENTRY ThisEntry,
    # IN PVOID Container,
    # IN PULONG ContainerRefCount,
    # IN USHORT CaseInsensitiveLength,
    # IN PRX_CONNECTION_ID ConnectionId
    # );
    RxPrefixTableInsertName = rdbss.RxPrefixTableInsertName
    RxPrefixTableInsertName.restype = PRX_PREFIX_ENTRY

    # VOID
    # RxRemovePrefixTableEntry (
    # IN OUT PRX_PREFIX_TABLE ThisTable,
    # IN OUT PRX_PREFIX_ENTRY Entry
    # );
    RxRemovePrefixTableEntry = rdbss.RxRemovePrefixTableEntry
    RxRemovePrefixTableEntry.restype = VOID

    # VOID
    # RxInitializePrefixTable (
    # IN OUT PRX_PREFIX_TABLE ThisTable,
    # IN ULONG TableSize OPTIONAL,
    # IN BOOLEAN CaseInsensitiveMatch
    # );
    RxInitializePrefixTable = rdbss.RxInitializePrefixTable
    RxInitializePrefixTable.restype = VOID

    # VOID
    # RxFinalizePrefixTable (
    # IN OUT PRX_PREFIX_TABLE ThisTable
    # );
    RxFinalizePrefixTable = rdbss.RxFinalizePrefixTable
    RxFinalizePrefixTable.restype = VOID


    # Rx form of a table entry.
    _RX_PREFIX_ENTRY._fields_ = [
        # Normal Header for Refcounted Structure
        ('NodeTypeCode', NODE_TYPE_CODE),
        ('NodeByteSize', NODE_BYTE_SIZE),
        # the initial part of the name that is always case insensitive
        ('CaseInsensitiveLength', USHORT),
        ('Spare1', USHORT),
        ('SavedHashValue', ULONG),
        ('HashLinks', LIST_ENTRY),
        # queue of the set members
        ('MemberQLinks', LIST_ENTRY),
        # Name of the entry
        ('Prefix', UNICODE_STRING),
        # Pointer to the reference count of the container
        ('ContainerRefCount', PULONG),
        # thus, i need this backptr.
        ('ContainingRecord', PVOID),
        # some space that alternate table routines can use
        ('Context', PVOID),
        # Used for controlled multiplexing
        ('ConnectionId', RX_CONNECTION_ID),
    ]
    # Rx form of name table. wraps in a lock and a queue. Originally, this
    # implementation used the prefix tables
    # in Rtl which don't allow an empty string entry. so, we special case this.
    RX_PREFIX_TABLE_DEFAULT_LENGTH = 32

    # TODO: Figure out if these are CALLBACKS or functions. don't know what
    # to do with them
    # typedef
    # PVOID
    # (*PRX_TABLE_LOOKUPNAME) (
    # IN PRX_PREFIX_TABLE ThisTable,
    # IN PUNICODE_STRING CanonicalName,
    # OUT PUNICODE_STRING RemainingName
    # );
    #
    # typedef
    # PRX_PREFIX_ENTRY
    # (*PRX_TABLE_INSERTENTRY) (
    # IN OUT PRX_PREFIX_TABLE ThisTable,
    # IN OUT PRX_PREFIX_ENTRY ThisEntry
    # );
    #
    # typedef
    # VOID
    # (*PRX_TABLE_REMOVEENTRY) (
    # IN OUT PRX_PREFIX_TABLE ThisTable,
    # IN OUT PRX_PREFIX_ENTRY Entry
    # );

    _TEMP__RX_PREFIX_TABLE = [
        # Normal Header
        ('NodeTypeCode', NODE_TYPE_CODE),
        ('NodeByteSize', NODE_BYTE_SIZE),
        # version stamp changes on each insertion/removal
        ('Version', ULONG),
        # queue of the inserted names
        ('MemberQueue', LIST_ENTRY),
        # Resource used to control table access
        ('TableLock', ERESOURCE),
        # PrefixEntry for the Null string
        ('TableEntryForNull', PRX_PREFIX_ENTRY),
        ('CaseInsensitiveMatch', BOOLEAN),
        # we may act differently for this....esp for debugnot
        ('IsNetNameTable', BOOLEAN),
        ('TableSize', ULONG)
    ]

    if DBG:
        _TEMP__RX_PREFIX_TABLE += [
            ('Lookups', ULONG),
            ('FailedLookups', ULONG),
            ('Considers', ULONG),
            ('Compares', ULONG),
            ('HashBuckets', LIST_ENTRY * RX_PREFIX_TABLE_DEFAULT_LENGTH),
        ]

    _RX_PREFIX_TABLE._fields_ = _TEMP__RX_PREFIX_TABLE

    ntoskrnl = ctypes.windll.NtosKrnl

    _dummy_macro_ = None
    if defined(_dummy_macro_):
        def RxAcquirePrefixTableLockShared(PrefixTable, Wait):
            pass
            # return RxpAcquirePrefixTableLockShared(
            #     PrefixTable,
            #     Wait,
            #     TRUE,
            #     __FILE__,
            #     __LINE__
            # )


        def RxAcquirePrefixTableLockExclusive(PrefixTable, Wait):
            pass
            # return RxpAcquirePrefixTableLockExclusive(
            #     PrefixTable,
            #     Wait,
            #     TRUE,
            #     __FILE__,
            #     __LINE__
            # )


        def RxReleasePrefixTableLock(PrefixTable):
            pass
            # return RxpReleasePrefixTableLock(
            #     PrefixTable,
            #     TRUE,
            #     __FILE__,
            #     __LINE__
            # )

    else:
        ExAcquireResourceSharedLite = ntoskrnl.ExAcquireResourceSharedLite
        ExAcquireResourceSharedLite.restype = BOOLEAN

        ExAcquireResourceExclusiveLite = ntoskrnl.ExAcquireResourceExclusiveLite
        ExAcquireResourceExclusiveLite.restype = BOOLEAN

        ExReleaseResourceLite = ntoskrnl.ExReleaseResourceLite
        ExReleaseResourceLite.restype = VOID

        def RxAcquirePrefixTableLockShared(TABLE, WAIT):
            return ExAcquireResourceSharedLite(TABLE.TableLock, WAIT)


        def RxAcquirePrefixTableLockExclusive(TABLE, WAIT):
            return ExAcquireResourceExclusiveLite(TABLE.TableLock, WAIT)


        def RxReleasePrefixTableLock(TABLE):
            return ExReleaseResourceLite(TABLE.TableLock)
    # END IF

    ExIsResourceAcquiredExclusiveLite = ntoskrnl.ExIsResourceAcquiredExclusiveLite
    ExIsResourceAcquiredExclusiveLite.restype = BOOLEAN

    ExIsResourceAcquiredSharedLite = ntoskrnl.ExIsResourceAcquiredSharedLite
    ExIsResourceAcquiredSharedLite.restype = ULONG


    def RxIsPrefixTableLockExclusive(TABLE):
        return ExIsResourceAcquiredExclusiveLite(TABLE.TableLock)


    def RxIsPrefixTableLockAcquired(TABLE):
        return (
            ExIsResourceAcquiredSharedLite(TABLE.TableLock) or
            ExIsResourceAcquiredExclusiveLite(TABLE.TableLock)
        )

# END IF   _RXPREFIX_
