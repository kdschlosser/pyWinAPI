import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_CLFS_PUBLIC_H_ = None
CLFSUSER_API = None
__CLFSUSER_EXPORTS__ = None
CLFS_KERNEL_MODE = None
__CLFS_PRIVATE_LSN__ = None
_cplusplus = None
CLFS_OPERATORS = None


class _CLS_LSN(ctypes.Structure):
    pass


CLS_LSN = _CLS_LSN
PCLS_LSN = POINTER(_CLS_LSN)
PPCLS_LSN = POINTER(POINTER(_CLS_LSN))


class _CLFS_NODE_ID(ctypes.Structure):
    pass


CLFS_NODE_ID = _CLFS_NODE_ID
PCLFS_NODE_ID = POINTER(_CLFS_NODE_ID)


class _CLS_WRITE_ENTRY(ctypes.Structure):
    pass


CLS_WRITE_ENTRY = _CLS_WRITE_ENTRY
PCLS_WRITE_ENTRY = POINTER(_CLS_WRITE_ENTRY)
PPCLS_WRITE_ENTRY = POINTER(POINTER(_CLS_WRITE_ENTRY))


class _CLS_INFORMATION(ctypes.Structure):
    pass


CLS_INFORMATION = _CLS_INFORMATION
PCLS_INFORMATION = POINTER(_CLS_INFORMATION)
PPCLS_INFORMATION = POINTER(_CLS_INFORMATION)


class _CLFS_LOG_NAME_INFORMATION(ctypes.Structure):
    pass


CLFS_LOG_NAME_INFORMATION = _CLFS_LOG_NAME_INFORMATION
PCLFS_LOG_NAME_INFORMATION = POINTER(_CLFS_LOG_NAME_INFORMATION)
PPCLFS_LOG_NAME_INFORMATION = POINTER(POINTER(_CLFS_LOG_NAME_INFORMATION))


class _CLFS_STREAM_ID_INFORMATION(ctypes.Structure):
    pass


CLFS_STREAM_ID_INFORMATION = _CLFS_STREAM_ID_INFORMATION
PCLFS_STREAM_ID_INFORMATION = POINTER(_CLFS_STREAM_ID_INFORMATION)
PPCLFS_STREAM_ID_INFORMATION = POINTER(POINTER(_CLFS_STREAM_ID_INFORMATION))


class _CLFS_PHYSICAL_LSN_INFORMATION(ctypes.Structure):
    pass


CLFS_PHYSICAL_LSN_INFORMATION = _CLFS_PHYSICAL_LSN_INFORMATION
PCLFS_PHYSICAL_LSN_INFORMATION = POINTER(_CLFS_PHYSICAL_LSN_INFORMATION)


class _CLS_CONTAINER_INFORMATION(ctypes.Structure):
    pass


CLS_CONTAINER_INFORMATION = _CLS_CONTAINER_INFORMATION
PCLS_CONTAINER_INFORMATION = POINTER(_CLS_CONTAINER_INFORMATION)
PPCLS_CONTAINER_INFORMATION = POINTER(POINTER(_CLS_CONTAINER_INFORMATION))


class _CLS_IO_STATISTICS_HEADER(ctypes.Structure):
    pass


CLS_IO_STATISTICS_HEADER = _CLS_IO_STATISTICS_HEADER
PCLS_IO_STATISTICS_HEADER = POINTER(_CLS_IO_STATISTICS_HEADER)
PPCLS_IO_STATISTICS_HEADER = POINTER(POINTER(_CLS_IO_STATISTICS_HEADER))


class _CLS_IO_STATISTICS(ctypes.Structure):
    pass


CLS_IO_STATISTICS = _CLS_IO_STATISTICS
PCLS_IO_STATISTICS = POINTER(_CLS_IO_STATISTICS)
PPCLS_IO_STATISTICS = POINTER(POINTER(_CLS_IO_STATISTICS))


class _CLS_SCAN_CONTEXT(ctypes.Structure):
    pass


CLS_SCAN_CONTEXT = _CLS_SCAN_CONTEXT
PCLS_SCAN_CONTEXT = POINTER(_CLS_SCAN_CONTEXT)
PPCLS_SCAN_CONTEXT = POINTER(POINTER(_CLS_SCAN_CONTEXT))


CLS_SCAN_CONTEXT = _CLS_SCAN_CONTEXT
PCLS_SCAN_CONTEXT = POINTER(_CLS_SCAN_CONTEXT)
PPCLS_SCAN_CONTEXT = POINTER(POINTER(_CLS_SCAN_CONTEXT))


class _CLS_ARCHIVE_DESCRIPTOR(ctypes.Structure):
    pass


CLS_ARCHIVE_DESCRIPTOR = _CLS_ARCHIVE_DESCRIPTOR
PCLS_ARCHIVE_DESCRIPTOR = POINTER(_CLS_ARCHIVE_DESCRIPTOR)
PPCLS_ARCHIVE_DESCRIPTOR = POINTER(POINTER(_CLS_ARCHIVE_DESCRIPTOR))


# /* == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == == == = Copyright (c) 1998 Microsoft
# Corporation Module Name: clfs.h Abstract: Header file containing all
# publicly defined data structures for the common log file system. Author:
# Dexter Bradshaw [DexterB] 09-Dec-1998 Revision History: == == == == == == ==
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == =
from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_BOOTABLESKU):
    # begin_wdm
    if not defined(_CLFS_PUBLIC_H_):
        _CLFS_PUBLIC_H_ = VOID

        # end_wdm
        # begin_wdm
        if not defined(CLFSUSER_API):
            if defined(__CLFSUSER_EXPORTS__):
                CLFSUSER_API = VOID
            else:
                CLFSUSER_API = __declspec(dllimport)
            # END IF

        # END IF


        # end_wdm
        if not defined(CLFS_KERNEL_MODE):
            from pyWinAPI.ucrt.stdio_h import * # NOQA

            if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                # PFILE
                # Define PFILE to be a pointer to _iobuf *
                # TYPEDEF ERROR: 1FILE *PFILE, **PPFILE;
                CLFSSTATUS = DWORD
                ClfsLsnEqual = LsnEqual
                ClfsLsnLess = LsnLess
                ClfsLsnGreater = LsnGreater
                ClfsLsnNull = LsnNull
                ClfsLsnCreate = LsnCreate
                ClfsLsnContainer = LsnContainer
                ClfsLsnBlockOffset = LsnBlockOffset
                ClfsLsnRecordSequence = LsnRecordSequence
                ClfsLsnInvalid = LsnInvalid
                ClfsLsnIncrement = LsnIncrement
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        # END IF  CLFS_KERNEL_MODE

        # begin_wdm
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # FILE_ATTRIBUTE_DEDICATED is defined as FILE_ATTRIBUTE_TEMPORARY.
            FILE_ATTRIBUTE_DEDICATED = FILE_ATTRIBUTE_TEMPORARY

            # Container name and container size extended attribute entry names.
            EA_CONTAINER_NAME = "ContainerName"
            EA_CONTAINER_SIZE = "ContainerSize"

            # Base log file name 3-letter extension.
            CLFS_BASELOG_EXTENSION = ".blf"

            # Common log file system public flags and constants.
            # No flags.
            CLFS_FLAG_NO_FLAGS = 0x00000000

            # Flag to force an append to log queue
            CLFS_FLAG_FORCE_APPEND = 0x00000001

            # Flag to force a log flush
            CLFS_FLAG_FORCE_FLUSH = 0x00000002

            # Flag to charge a data append to reservation
            CLFS_FLAG_USE_RESERVATION = 0x00000004

            # Kernel mode create flag indicating a re-entrant file system.
            CLFS_FLAG_REENTRANT_FILE_SYSTEM = 0x00000008

            # Kernel mode create flag indicating non-reentrant filter.
            CLFS_FLAG_NON_REENTRANT_FILTER = 0x00000010

            # Kernel mode create flag indicating reentrant filter.
            CLFS_FLAG_REENTRANT_FILTER = 0x00000020

            # Kernel mode create flag indicating IO_IGNORE_SHARE_ACCESS_CHECK
            # semantics.
            CLFS_FLAG_IGNORE_SHARE_ACCESS = 0x00000040

            # Flag indicating read in progress and not completed.
            CLFS_FLAG_READ_IN_PROGRESS = 0x00000080

            # Kernel mode create flag indicating mini-filter target.
            CLFS_FLAG_MINIFILTER_LEVEL = 0x00000100

            # Kernel mode create flag indicating the log and containers should
            # be marked hidden & system.
            CLFS_FLAG_HIDDEN_SYSTEM_LOG = 0x00000200

            # Marshalling Context Flag
            # No flags
            CLFS_MARSHALLING_FLAG_NONE = 0x00000000

            # Flag to disable mashalling buffer intialization
            CLFS_MARSHALLING_FLAG_DISABLE_BUFF_INIT = 0x00000001

            # Flag indicating all CLFS I/O will be targeted to an intermediate
            # level of the I/O stack
            CLFS_FLAG_FILTER_INTERMEDIATE_LEVEL = (
                CLFS_FLAG_NON_REENTRANT_FILTER
            )

            # Flag indicating all CLFS I/O will be targeted to the top level
            # of the I/O stack
            CLFS_FLAG_FILTER_TOP_LEVEL = CLFS_FLAG_REENTRANT_FILTER

            # CLFS_CONTAINER_INDEX
            # Index into the container table.
            CLFS_CONTAINER_ID = ULONG
            PCLFS_CONTAINER_ID = POINTER(CLFS_CONTAINER_ID)
            PPCLFS_CONTAINER_ID = POINTER(POINTER(CLFS_CONTAINER_ID))

        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if defined(__CLFS_PRIVATE_LSN__):
            from pyWinAPI.shared.clfslsn_h import * # NOQA

        else:
            if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                # CLS_LSN
                _CLS_LSN._fields_ = [
                    ('Internal', ULONGLONG),
                ]
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        # END IF  __CLFS_PRIVATE_LSN__


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Alias CLS prefixed types with CLFS prefixes.
            CLFS_LSN = CLS_LSN
            PCLFS_LSN = POINTER(CLFS_LSN)
            PPCLFS_LSN = POINTER(POINTER(CLFS_LSN))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if defined(__cplusplus):
            pass
        # END IF  __cplusplus

        # end_wdm
        # Definition of special LSN's: CLFS_LSN_INVALID and CLFS_LSN_NULL.
        # Note that
        # [CLFS_LSN_NULL,
        # CLFS_LSN_INVALID) define the only valid LSN range. LSN values
        # are strictly monotonic increasing.

        if defined(CLFS_KERNEL_MODE):
            if defined(__CLFS_SUPPORT_LIBRARY__):
                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    CLFS_LSN_INVALID = CLFS_LSN
                    CLFS_LSN_NULL = CLFS_LSN
                # END IF  NTDDI_VERSION or _WIN32_WINNT

            elif defined(__CLFSUSER_EXPORTS__):
                if (NTDDI_VERSION >= NTDDI_WS03SP1) or (_WIN32_WINNT >= _WIN32_WINNT_WS03):
                    CLFS_LSN_INVALID = CLFS_LSN
                    CLFS_LSN_NULL = CLFS_LSN
                # END IF  NTDDI_VERSION or _WIN32_WINNT
            else:
                # begin_wdm
                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    CLFS_LSN_INVALID = CLFS_LSN
                    CLFS_LSN_NULL = CLFS_LSN

                # END IF  NTDDI_VERSION or _WIN32_WINNT

                # end_wdm
            # END IF  __CLFSUSER_EXPORTS__


        else:
            if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                CLFS_LSN_INVALID = CLFS_LSN
                CLFS_LSN_NULL = CLFS_LSN
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        # END IF  CLFS_KERNEL_MODE

        # begin_wdm
        if defined(__cplusplus):
            pass
        # END IF  __cplusplus


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_RECORD_TYPE
            # Definition of record types.
            if defined(__cplusplus):
                # Null record type.
                ClfsNullRecord = 0x00

                # Client data record.
                ClfsDataRecord = 0x01

                # Restart record.
                ClfsRestartRecord = 0x02

                # Valid client records are restart and data records.
                ClfsClientRecord = ClfsDataRecord | ClfsRestartRecord
            else:
                # Null record type.
                ClfsNullRecord = 0x00

                # Client data record.
                ClfsDataRecord = 0x01

                # Restart record.
                ClfsRestartRecord = 0x02

                # Valid client records are restart and data records.
                ClfsClientRecord = ClfsDataRecord | ClfsRestartRecord
            # END IF  _cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Log container path prefix indicating the log container's
            # location is
            # actually a stream inside of the BLF.
            if defined(_cplusplus):
                CLFS_CONTAINER_STREAM_PREFIX = "%BLF%:"
            else:
                CLFS_CONTAINER_STREAM_PREFIX = "%BLF%:"
            # END IF  _cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Log container path prefix indicating the log container's
            # location is
            # relative to the base log file (BLF) and not an absolute path.
            # Paths which do not being with said prefix are absolute paths.
            if defined(_cplusplus):
                CLFS_CONTAINER_RELATIVE_PREFIX = "%BLF%\\"
            else:
                CLFS_CONTAINER_RELATIVE_PREFIX = "%BLF%\\"
            # END IF  _cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Alias CLS prefix with CLFS prefixes.
            CLS_RECORD_TYPE = UCHAR
            PCLS_RECORD_TYPE = POINTER(UCHAR)
            PPCLS_RECORD_TYPE = POINTER(POINTER(UCHAR))

            CLFS_RECORD_TYPE = CLS_RECORD_TYPE
            PCLFS_RECORD_TYPE = POINTER(CLS_RECORD_TYPE)
            PPCLFS_RECORD_TYPE = POINTER(POINTER(CLS_RECORD_TYPE))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_CONTEXT_MODE
            # The context mode specifies the direction and access methods used
            # to scan the
            # log file.
            class _CLS_CONTEXT_MODE(ENUM):
                ClsContextNone = 0x00
                ClsContextUndoNext = 1
                ClsContextPrevious = 2
                ClsContextForward = 3

            CLS_CONTEXT_MODE = _CLS_CONTEXT_MODE
            PCLS_CONTEXT_MODE = POINTER(_CLS_CONTEXT_MODE)
            PPCLS_CONTEXT_MODE = POINTER(POINTER(_CLS_CONTEXT_MODE))
        # END IF  NTDDI_VERSION or _WIN32_WINNT


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Alias all CLS prefixes with CLFS prefixes.
            class _CLFS_CONTEXT_MODE(ENUM):
                ClfsContextNone = 0x00
                ClfsContextUndoNext = 1
                ClfsContextPrevious = 2
                ClfsContextForward = 3

            CLFS_CONTEXT_MODE = _CLFS_CONTEXT_MODE
            PCLFS_CONTEXT_MODE = POINTER(_CLFS_CONTEXT_MODE)
            PPCLFS_CONTEXT_MODE = POINTER(POINTER(_CLFS_CONTEXT_MODE))
        # END IF  NTDDI_VERSION or _WIN32_WINNT


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFSD_NODE_ID
            # Common log file system node identifier. Every CLFS file system
            # structure has a node identity and type. The node type is a
            # signature
            # field while the size is used in for consistency checking.
            _CLFS_NODE_ID._fields_ = [
                # CLFS node type.
                ('cType', ULONG),
                # CLFS node size.
                ('cbNode', ULONG),
            ]
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_WRITE_ENTRY
            # Write entry specifying the contents of a user buffer and length
            # that are
            # marshaled in the space reservation and append interface of the
            # CLS API.
            _CLS_WRITE_ENTRY._fields_ = [
                ('Buffer', PVOID),
                ('ByteLength', ULONG),
            ]
        # END IF  NTDDI_VERSION or _WIN32_WINNT


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_WRITE_ENTRY = CLS_WRITE_ENTRY
            PCLFS_WRITE_ENTRY = POINTER(CLFS_WRITE_ENTRY)
            PPCLFS_WRITE_ENTRY = POINTER(POINTER(CLFS_WRITE_ENTRY))
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_LOG_ID
            # A log identifier is a GUID that describes uniquely a physical
            # log file.
            CLFS_LOG_ID = GUID
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_INFORMATION
            # Logical log file information structure describing either virtual
            # or physical log
            # file data, depending on the type of information queried.
            _CLS_INFORMATION._fields_ = [
                # Total log data space available.
                ('TotalAvailable', LONGLONG),
                # Usable space in the log file.
                ('CurrentAvailable', LONGLONG),
                # Space reserved for UNDO's (aggregate for physical log)
                ('TotalReservation', LONGLONG),
                # Size of the base log file.
                ('BaseFileSize', ULONGLONG),
                # Uniform size of log containers.
                ('ContainerSize', ULONGLONG),
                # Total number of containers.
                ('TotalContainers', ULONG),
                # Number of containers not in active log.
                ('FreeContainers', ULONG),
                # Total number of clients.
                ('TotalClients', ULONG),
                # Log file attributes.
                ('Attributes', ULONG),
                # Log file flush threshold.
                ('FlushThreshold', ULONG),
                # Underlying container sector size.
                ('SectorSize', ULONG),
                # Marks the global archive tail.
                ('MinArchiveTailLsn', CLS_LSN),
                # Start of the active log region.
                ('BaseLsn', CLS_LSN),
                # Last flushed LSN in active log.
                ('LastFlushedLsn', CLS_LSN),
                # End of active log region.
                ('LastLsn', CLS_LSN),
                # Location of restart record.
                ('RestartLsn', CLS_LSN),
                # Unique identifier for the log.
                ('Identity', GUID),
            ]
        # END IF  NTDDI_VERSION or _WIN32_WINNT


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Alias CLS prefixes with CLS prefixes.
            CLFS_INFORMATION = CLS_INFORMATION
            PCLFS_INFORMATION = POINTER(CLFS_INFORMATION)
            PPCLFS_INFORMATION = POINTER(POINTER(CLFS_INFORMATION))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        # /* // // CLFS_CLIENT_INFORMATION // // The client information
        # structure maintains client-based log metadata. // typedef struct
        # _CLS_CLIENT_INFORMATION
        #
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_LOG_NAME_INFORMATION
            # The client information structure stores the name of a log. It is
            # used
            # to communicate ClfsLogNameInformation and
            # ClfsLogPhysicalNameInformation.
            _CLFS_LOG_NAME_INFORMATION._fields_ = [
                ('NameLengthInBytes', USHORT),
                ('Name', WCHAR * 1),
            ]
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_STREAM_ID_INFORMATION
            # The client information structure provides a permanent identifier
            # unique
            # to the log for the stream in question.
            _CLFS_STREAM_ID_INFORMATION._fields_ = [
                ('StreamIdentifier', UCHAR),
            ]
        # END IF  NTDDI_VERSION or _WIN32_WINNT


        if (NTDDI_VERSION  >= NTDDI_VISTA) or (_WIN32_WINNT  >= _WIN32_WINNT_LONGHORN):
            # CLFS_PHYSICAL_LSN_INFORMATION
            # An information structure that describes a virtual:physical LSN
            # pairing
            # for the stream identified in the structure.
            _CLFS_PHYSICAL_LSN_INFORMATION._fields_ = [
                ('StreamIdentifier', UCHAR),
                ('VirtualLsn', CLFS_LSN),
                ('PhysicalLsn', CLFS_LSN),
            ]
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_CONTAINER_STATE
            # At any point in time a container could be inactive or
            # uninitialized, active,
            # pending deletion from the list of free containers, pending
            # archival, or
            # pending deletion while waiting to be archived.
            CLS_CONTAINER_STATE = UINT32
            PCLS_CONTAINER_STATE = POINTER(UINT32)
            PPCLS_CONTAINER_STATE = POINTER(POINTER(UINT32))

            CLFS_CONTAINER_STATE = CLS_CONTAINER_STATE
            PCLFS_CONTAINER_STATE = POINTER(CLS_CONTAINER_STATE)
            PPCLFS_CONTAINER_STATE = POINTER(POINTER(CLS_CONTAINER_STATE))
        # END IF  NTDDI_VERSION or _WIN32_WINNT


        if defined(__cplusplus):
            if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                ClsContainerInitializing = 0x01
                ClsContainerInactive = 0x02
                ClsContainerActive = 0x04
                ClsContainerActivePendingDelete = 0x08
                ClsContainerPendingArchive = 0x10
                ClsContainerPendingArchiveAndDelete = 0x20
                ClfsContainerInitializing = 0x01
                ClfsContainerInactive = 0x02
                ClfsContainerActive = 0x04
                ClfsContainerActivePendingDelete = 0x08
                ClfsContainerPendingArchive = 0x10
                ClfsContainerPendingArchiveAndDelete = 0x20
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        else:
            if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                ClsContainerInitializing = 0x01
                ClsContainerInactive = 0x02
                ClsContainerActive = 0x04
                ClsContainerActivePendingDelete = 0x08
                ClsContainerPendingArchive = 0x10
                ClsContainerPendingArchiveAndDelete = 0x20
                ClfsContainerInitializing = 0x01
                ClfsContainerInactive = 0x02
                ClfsContainerActive = 0x04
                ClfsContainerActivePendingDelete = 0x08
                ClfsContainerPendingArchive = 0x10
                ClfsContainerPendingArchiveAndDelete = 0x20
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        # END IF  __cplusplus


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_MAX_CONTAINER_INFO
            # The maximum length, in bytes, of the FileName field in the CLFS
            # container information structure.
            if defined(__cplusplus):
                pass
            else:
                CLFS_MAX_CONTAINER_INFO = 256
            # END IF  __cplusplus
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_CONTAINER_INFORMATION
            # This structure defines a container descriptor. The descriptor
            # specifies the
            # container's creation and access times, size, file system name,
            # file system
            # attributes, state, minimum, and maximum LSNs.
            _CLS_CONTAINER_INFORMATION._fields_ = [
                # File system attribute flag.
                ('FileAttributes', ULONG),
                # File creation time.
                ('CreationTime', ULONGLONG),
                # Last time container was read/written.
                ('LastAccessTime', ULONGLONG),
                # Last time container was written.
                ('LastWriteTime', ULONGLONG),
                # Size of container in bytes.
                ('ContainerSize', LONGLONG),
                # Length of the actual file name.
                ('FileNameActualLength', ULONG),
                # Length of file name in buffer
                ('FileNameLength', ULONG),
                # File system name for container.
                ('FileName', WCHAR * CLFS_MAX_CONTAINER_INFO),
                # Current state of the container.
                ('State', CLFS_CONTAINER_STATE),
                # Physical container identifier.
                ('PhysicalContainerId', CLFS_CONTAINER_ID),
                # Logical container identifier.
                ('LogicalContainerId', CLFS_CONTAINER_ID),
            ]


            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_CONTAINER_INFORMATION = CLS_CONTAINER_INFORMATION
            PCLFS_CONTAINER_INFORMATION = POINTER(CLFS_CONTAINER_INFORMATION)
            PPCLFS_CONTAINER_INFORMATION = POINTER(POINTER(CLFS_CONTAINER_INFORMATION))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_LOG_INFORMATION_CLASS
            # The information class specifies the kind of information a caller
            # wishes to query or set on a log file.
            class _CLS_LOG_INFORMATION_CLASS(ENUM):

                # For virtual or physical logs, indicates the respective basic
                # information.
                ClfsLogBasicInformation = 0x00
                ClfsLogBasicInformationPhysical = 1
                ClfsLogPhysicalNameInformation = 2
                ClfsLogStreamIdentifierInformation = 3
                if (NTDDI_VERSION  >= NTDDI_VISTA) or (_WIN32_WINNT  >= _WIN32_WINNT_LONGHORN):
                    ClfsLogSystemMarkingInformation = 4

                    # Maps virtual LSNs to physical LSNs; only valid for
                    # physical logs.
                    ClfsLogPhysicalLsnInformation = 5
                # END IF

            CLS_LOG_INFORMATION_CLASS = _CLS_LOG_INFORMATION_CLASS
            PCLS_LOG_INFORMATION_CLASS = POINTER(_CLS_LOG_INFORMATION_CLASS)
            PPCLS_LOG_INFORMATION_CLASS = POINTER(POINTER(_CLS_LOG_INFORMATION_CLASS))

            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_LOG_INFORMATION_CLASS = CLS_LOG_INFORMATION_CLASS
            PCLFS_LOG_INFORMATION_CLASS = POINTER(CLFS_LOG_INFORMATION_CLASS)
            PPCLFS_LOG_INFORMATION_CLASS = POINTER(POINTER(CLFS_LOG_INFORMATION_CLASS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_IOSTATS_CLASS
            # Enumerated type defining the class of I/O statistics.
            class _CLS_IOSTATS_CLASS(ENUM):
                ClsIoStatsDefault = 0x0000
                ClsIoStatsMax = 0xFFFF

            CLS_IOSTATS_CLASS = _CLS_IOSTATS_CLASS
            PCLS_IOSTATS_CLASS = POINTER(_CLS_IOSTATS_CLASS)
            PPCLS_IOSTATS_CLASS = POINTER(POINTER(_CLS_IOSTATS_CLASS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_IOSTATS_CLASS
            # Alias all CLS prefixes with CLFS prefixes.
            class _CLFS_IOSTATS_CLASS(ENUM):
                ClfsIoStatsDefault = 0x0000
                ClfsIoStatsMax = 0xFFFF

            CLFS_IOSTATS_CLASS = _CLFS_IOSTATS_CLASS
            PCLFS_IOSTATS_CLASS = POINTER(_CLFS_IOSTATS_CLASS)
            PPCLFS_IOSTATS_CLASS = POINTER(POINTER(_CLFS_IOSTATS_CLASS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_IO_STATISTICS
            # This structure defines I/O performance counters particular to a
            # log file. It consists
            # of a header followed by the I/O statistics counters. The header
            # is being ignored for
            # now.
            _CLS_IO_STATISTICS_HEADER._fields_ = [
                # Major version of the statistics buffer.
                ('ubMajorVersion', UCHAR),
                # Minor version of the statistics buffer.
                ('ubMinorVersion', UCHAR),
                # I/O statistics class.
                ('eStatsClass', CLFS_IOSTATS_CLASS),
                # Length of the statistics buffer.
                ('cbLength', USHORT),
                # Offset of statistics counters.
                ('coffData', ULONG),
            ]


            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_IO_STATISTICS_HEADER = CLS_IO_STATISTICS_HEADER
            PCLFS_IO_STATISTICS_HEADER = POINTER(CLFS_IO_STATISTICS_HEADER)
            PPCLFS_IO_STATISTICS_HEADER = POINTER(POINTER(CLFS_IO_STATISTICS_HEADER))
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            _CLS_IO_STATISTICS._fields_ = [
                # Statistics buffer header.
                ('hdrIoStats', CLS_IO_STATISTICS_HEADER),
                # Flush count.
                ('cFlush', ULONGLONG),
                # Cumulative number of bytes flushed.
                ('cbFlush', ULONGLONG),
                # Metadata flush count.
                ('cMetaFlush', ULONGLONG),
                # Cumulative number of metadata bytes flushed.
                ('cbMetaFlush', ULONGLONG),
            ]


            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_IO_STATISTICS = CLS_IO_STATISTICS
            PCLFS_IO_STATISTICS = POINTER(CLFS_IO_STATISTICS)
            PPCLFS_IO_STATISTICS = POINTER(POINTER(CLFS_IO_STATISTICS))
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_SCAN_MODE
            # Container scan mode flags.
            if defined(__cplusplus):
                pass
            else:
                CLFS_SCAN_INIT = 0x01
                CLFS_SCAN_FORWARD = 0x02
                CLFS_SCAN_BACKWARD = 0x04
                CLFS_SCAN_CLOSE = 0x08
                CLFS_SCAN_INITIALIZED = 0x10
                CLFS_SCAN_BUFFERED = 0x20
            # END IF

            CLFS_SCAN_MODE = UCHAR
            PCLFS_SCAN_MODE = POINTER(UCHAR)
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        # end_wdm
        if defined(CLFS_KERNEL_MODE):
            # begin_wdm
            if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                # CLFS_SCAN_CONTEXT
                # Container scan context for scanning all containers in a
                # given physical log
                # file.
                # The log file object wraps an NT file object and the size of
                # the structure.
                # The log file object may be modified in the near future and
                # there should be no
                # dependencies on the size of the structure itself.
                LOG_FILE_OBJECT = FILE_OBJECT
                PLOG_FILE_OBJECT = POINTER(FILE_OBJECT)
                PPLOG_FILE_OBJECT = POINTER(POINTER(FILE_OBJECT))

                if defined(_MSC_VER):
                    if _MSC_VER  >= 1200:
                        pass
                    # END IF
                # END IF

                _CLS_SCAN_CONTEXT._fields_ = [
                    ('cidNode', CLFS_NODE_ID),
                    ('plfoLog', PLOG_FILE_OBJECT),
                    ('cIndex', ULONG),
                    ('cContainers', ULONG),
                    ('cContainersReturned', ULONG),
                    ('eScanMode', CLFS_SCAN_MODE),
                    ('pinfoContainer', PCLS_CONTAINER_INFORMATION),
                ]

                if defined(_MSC_VER):
                    if _MSC_VER  >= 1200:
                        pass
                    # END IF
                # END IF

            # END IF  NTDDI_VERSION or _WIN32_WINNT

            # end_wdm
        else:
            if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                _CLS_SCAN_CONTEXT._fields_ = [
                    ('cidNode', CLFS_NODE_ID),
                    ('hLog', HANDLE),
                    ('cIndex', ULONG),
                    ('cContainers', ULONG),
                    ('cContainersReturned', ULONG),
                    ('eScanMode', CLFS_SCAN_MODE),
                    ('pinfoContainer', PCLS_CONTAINER_INFORMATION),
                ]
            # END IF  NTDDI_VERSION or _WIN32_WINNT
        # END IF  CLFS_KERNEL_MODE

        # begin_wdm
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # Alias all CLS prefixes with CLFS prefixes.
            CLFS_SCAN_CONTEXT = CLS_SCAN_CONTEXT
            PCLFS_SCAN_CONTEXT = POINTER(CLFS_SCAN_CONTEXT)
            PPCLFS_SCAN_CONTEXT = POINTEER(POINTER(CLFS_SCAN_CONTEXT))

        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_ARCHIVE_DESCRIPTOR
            # Log archive descriptors describe the set of discrete but
            # logically
            # contiguous disk extents comprising a snapshot of the active log
            # when
            # preparing for archival. Log archive descriptors specify enough
            # information
            # for log archive clients directly access the relevant contents of
            # containers
            # for archiving and restoring a snapshot of the log.
            _CLS_ARCHIVE_DESCRIPTOR._fields_ = [
                ('coffLow', ULONGLONG),
                ('coffHigh', ULONGLONG),
                ('infoContainer', CLS_CONTAINER_INFORMATION),
            ]

            # Alias CLS prefixes with CLFS prefixes.
            CLFS_ARCHIVE_DESCRIPTOR = CLS_ARCHIVE_DESCRIPTOR
            PCLFS_ARCHIVE_DESCRIPTOR = POINTER(CLFS_ARCHIVE_DESCRIPTOR)
            PPCLFS_ARCHIVE_DESCRIPTOR = POINTER(POINTER(CLFS_ARCHIVE_DESCRIPTOR))
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_ALLOCATION_ROUTINE
            # Allocate a blocks for marshaled reads or writes
            # PVOID (* CLFS_BLOCK_ALLOCATION) (ULONG cbBufferLength, PVOID pvUserContext);
            CLFS_BLOCK_ALLOCATION = CALLBACK(
                PVOID,
                ULONG,
                PVOID,
            )
            # CLFS_DEALLOCATION_ROUTINE
            # Deallocate buffers allocated by the CLFS_ALLOCATION_ROUTINE.
            # VOID (* CLFS_BLOCK_DEALLOCATION) (PVOID pvBuffer, PVOID pvUserContext);
            CLFS_BLOCK_DEALLOCATION = CALLBACK(
                VOID,
                PVOID,
                PVOID,
            )
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_LOG_ARCHIVE_MODE
            # Describes the archive support behavior for the log.
            class _CLFS_LOG_ARCHIVE_MODE(ENUM):
                ClfsLogArchiveEnabled = 0x01
                ClfsLogArchiveDisabled = 0x02

            CLFS_LOG_ARCHIVE_MODE = _CLFS_LOG_ARCHIVE_MODE
            PCLFS_LOG_ARCHIVE_MODE = POINTER(_CLFS_LOG_ARCHIVE_MODE)
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        # -------------------------------------------------------------------
        # LSN OPERATORS
        # -------------------------------------------------------------------
        if defined(__cplusplus):
            pass
        # END IF


        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnEqual
            # Method Description:
            # Check for the equivalence of LSNs.
            # Arguments:
            # plsn1 -- first LSN comparator
            # plsn2 -- second LSN comparator
            # Return Value:
            # TRUE if LSN values are equivalent and FALSE otherwise.
            # ---------------------------------------------------------------
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnLess
            # Method Description:
            # Check if LSN1 is less than LSN2.
            # Arguments:
            # plsn1 -- first LSN comparator
            # plsn2 -- second LSN comparator
            # Return Value:
            # TRUE if LSN1 is less than LSN2 and FALSE otherwise.
            # ---------------------------------------------------------------
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnGreater
            # Method Description:
            # Check if LSN1 is greater than LSN2.
            # Arguments:
            # plsn1 -- first LSN comparator
            # plsn2 -- second LSN comparator
            # Return Value:
            # TRUE if LSN1 is greater than LSN2 and FALSE otherwise.
            # ---------------------------------------------------------------
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnNull (Inline)
            # Method Description:
            # Check whether or not an LSN is CLFS_LSN_NULL.
            # Arguments:
            # plsn -- reference to LSN tested against the NULL value.
            # Return Value:
            # TRUE if and only if an LSN is equivalent to CLFS_LSN_NULL.
            # LSNs with the value CLFS_LSN_INVALID will return FALSE.
            # ---------------------------------------------------------------
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnContainer (Inline)
            # Routine Description:
            # Extract the container identifier from the LSN.
            # Arguments:
            # plsn -- get block offset from this LSN
            # Return Value:
            # Returns the container identifier for the LSN.
            # ---------------------------------------------------------------
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnCreate (Inline)
            # Routine Description:
            # Create an LSN given a log identifier, a container identifier, a
            # block
            # offset and a bucket identifier. Caller must test for invalid LSN
            # after
            # making this call.
            # Arguments:
            # cidContainer -- container identifier
            # offBlock  -- block offset
            # cRecord  -- ordinal number of the record in block
            # Return Value:
            # Returns a valid LSN if successful, otherwise it returns
            # CLFS_LSN_INVALID
            # ---------------------------------------------------------------
            pass
        # END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnBlockOffset (Inline)
            # Routine Description:
            # Extract the block offset from the LSN.
            # Arguments:
            # plsn -- get block offset from this LSN
            # Return Value:
            # Returns the block offset for the LSN.
            # ---------------------------------------------------------------
            pass
        #  END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnRecordSequence (Inline)
            # Routine Description:
            # Extract the bucket identifier from the LSN.
            # Arguments:
            # plsn -- get block offset from this LSN
            # Return Value:
            # Returns the bucket identifier for the LSN.
            # ---------------------------------------------------------------
            pass
        #  END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnInvalid
            # Method Description:
            # Check whether or not an LSN is CLFS_LSN_INVALID.
            # Arguments:
            # plsn -- reference to LSN tested against CLFS_LSN_INVALID.
            # Return Value:
            # TRUE if and only if an LSN is equivalent to CLFS_LSN_INVALID.
            # LSNs with the value CLFS_LSN_NULL will return FALSE.
            # ---------------------------------------------------------------
            pass
        #  END IF  NTDDI_VERSION or _WIN32_WINNT
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # ---------------------------------------------------------------
            # ClfsLsnIncrement
            # Method Description:
            # Increment and LSN by 1
            # Arguments:
            # plsn -- LSN to be incremented.
            # Return Value:
            # A valid LSN next in sequence to the input LSN, if successful.
            # Otherwise, this function returns CLFS_LSN_INVALID.
            # ---------------------------------------------------------------
            pass
        #  END IF  NTDDI_VERSION or _WIN32_WINNT
        if defined(__cplusplus):
            pass
        # END IF

        if defined(__cplusplus):
            if defined(CLFS_OPERATORS):
                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    # LSN arithmetic increment operator.
                    # Prefix increment operator.
                    pass
                # END IF  NTDDI_VERSION or _WIN32_WINNT
                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    # BOOLEAN LSN operators.
                    pass
                # END IF  NTDDI_VERSION or _WIN32_WINNT
                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    pass
                # END IF  NTDDI_VERSION or _WIN32_WINNT

                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    pass
                # END IF  NTDDI_VERSION or _WIN32_WINNT

                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    pass
                # END IF  NTDDI_VERSION or _WIN32_WINNT

                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    pass
                # END IF  NTDDI_VERSION or _WIN32_WINNT

                if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
                    pass
                # END IF  NTDDI_VERSION or _WIN32_WINNT
            # END IF  CLFS_OPERATORS
        # END IF  __cplusplus
    # END IF  _CLFS_PUBLIC_H_

    # end_wdm
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_BOOTABLESKU)
# -----------------------------------------------------------------------------
# END OF FILE
# -----------------------------------------------------------------------------
