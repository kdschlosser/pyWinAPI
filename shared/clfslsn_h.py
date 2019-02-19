import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_CLFS_LSN_H_ = None


class _CLS_LSN(ctypes.Union):
    pass

CLS_LSN = _CLS_LSN
PCLS_LSN = POINTER(_CLS_LSN)
PPCLS_LSN = POINTER(POINTER(_CLS_LSN))


from pyWinAPI.shared.winapifamily_h import * # NOQA

# /* == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == == == = Copyright (c) 1998 Microsoft
# Corporation Module Name: clfslsn.h Abstract: Header file containing the
# private definition for the common log file system's log sequence number
# structure. Author: Dexter Bradshaw [DexterB] 09-Dec-1998 Revision History:
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == == =
if not defined(_CLFS_LSN_H_):
    _CLFS_LSN_H_ = VOID

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLFS_RECORD_INDEX
            # Log record offset on container file. The log record offset
            # consists of a block
            # offset in the container and a bucket identifier indexing the
            # records in the block.
            # Declared up here because including clfs_x.h will try to define
            # the LSN, which needs
            # this.
            CLFS_RECORD_INDEX = UINT32
        # END IF  NTDDI_VERSION or _WIN32_WINNT

        if (NTDDI_VERSION  >= NTDDI_WS03SP1) or (_WIN32_WINNT  >= _WIN32_WINNT_WS03):
            # CLS_LSN
            # The log sequence number (LSN) is a valid log file address. The
            # LSN consists of
            # three (3) parts: (a) a log identifier to identify which physical
            # log the log record
            # belongs to, (b) a container index identifying the log container
            # where the log record
            # lies, and (c) a record offset identified by the offset of the
            # block in the container
            # and an ordinal number for the record within the container.
            # The structure of the LSN poses some inherent limitations of the
            # number of logs,
            # the number of containers, the size of a container, and the
            # number of log records in
            # a log block.
            # Maximum number of physical log files is 64K.
            # Maximum number of container identifiers is 4G.
            # Maximum size of a container is 4G.
            # Maximum number of sector-aligned log blocks is 8M
            # Maximum number of record buckets in a log block is 512
            class offset(ctypes.Structure):
                pass


            offset._fields_ = [
                # Record offset on container.
                ('idxRecord', CLFS_RECORD_INDEX),
                # Container identifier.
                ('cidContainer', CLFS_CONTAINER_ID),
            ]
            _CLS_LSN.offset = offset

            _CLS_LSN._fields_ = [
                # Container identifier
                ('offset', _CLS_LSN.offset),
                # Sequence number within physical log.
                ('ULONGLONG               ullOffset', __volatile),
            ]

            # Alias CLS prefixed types with CLFS prefixes.
            CLFS_LSN = CLS_LSN
            PCLFS_LSN = POINTER(CLFS_LSN)
            PPCLFS_LSN = PONITER(POINTER(CLFS_LSN))
        # END IF  NTDDI_VERSION or _WIN32_WINNT
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF


