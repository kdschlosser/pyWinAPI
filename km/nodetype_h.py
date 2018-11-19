import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class _NODE_TYPE_CODE_AND_SIZE_NO_REFCOUNT(ctypes.Structure):
    pass


NODE_TYPE_CODE_AND_SIZE_NO_REFCOUNT = _NODE_TYPE_CODE_AND_SIZE_NO_REFCOUNT


class _NODE_TYPE_CODE_AND_SIZE(NODE_TYPE_CODE_AND_SIZE_NO_REFCOUNT):
    pass


NODE_TYPE_CODE_AND_SIZE = _NODE_TYPE_CODE_AND_SIZE
PNODE_TYPE_AND_SIZE = POINTER(_NODE_TYPE_CODE_AND_SIZE)


# /* + + Copyright (c) 1989 Microsoft Corporation Module Name: NodeType.h
# Abstract: This module defines all of the node type codes used in the RDBSS.
# Every major data structure in the file system is assigned a node type code
# that is. This code is the first CSHORT in the structure and is followed by a
# CSHORT containing the size, in bytes, of the structure. Author: Revision
# History: - -
_NODETYPE_INCLUDED_ = None
if not defined(_NODETYPE_INCLUDED_):
    _NODETYPE_INCLUDED_ = 1
    NODE_TYPE_CODE = USHORT
    PNODE_TYPE_CODE = POINTER(NODE_TYPE_CODE)
    NODE_BYTE_SIZE = CSHORT


    # So all records start with
    # typedef struct _RECORD_NAME {
    # NODE_TYPE_CODE NodeTypeCode;
    # NODE_BYTE_SIZE NodeByteSize;
    # :
    # } RECORD_NAME, *PRECORD_NAME;

    NodeType = None
    if not defined(NodeType):

        def NodeType(Ptr):
            return ctypes.cast(Ptr, PNODE_TYPE_CODE)

    # END IF

    _NODE_TYPE_CODE_AND_SIZE_NO_REFCOUNT._fields_ = [
        ('NodeTypeCode', NODE_TYPE_CODE),
        ('NodeByteSize', NODE_BYTE_SIZE),
    ]

    _NODE_TYPE_CODE_AND_SIZE._fields_ = [
        ('NodeReferenceCount', ULONG)
    ]

    RDBSS_NTC_STORAGE_TYPE_UNKNOWN = 0xEC00
    RDBSS_NTC_STORAGE_TYPE_DIRECTORY = 0xEC02
    RDBSS_NTC_STORAGE_TYPE_FILE = 0xEC03
    RDBSS_NTC_OPENTARGETDIR_FCB = 0xECFF  # must be an fcb type and not the same
    RDBSS_NTC_IPC_SHARE = 0xECFE
    RDBSS_NTC_MAILSLOT = 0xECFD
    RDBSS_NTC_SPOOLFILE = 0xECFC
    RDBSS_NTC_SRVCALL = 0xEB10
    RDBSS_NTC_NETROOT = 0xEB11
    RDBSS_NTC_V_NETROOT = 0xEB12

    # Local filesystems sometimes need volume opens. these are not yet
    # implemented but we reserve the nodetype now.
    RDBSS_NTC_VOLUME_FCB = 0xEB1F
    RDBSS_NTC_SRVOPEN = 0xEB1C
    RDBSS_NTC_INTERNAL_SRVOPEN = 0xEB1D
    RDBSS_NTC_DEVICE_FCB = 0xEB9A
    RDBSS_NTC_DATA_HEADER = 0xEB00
    RDBSS_NTC_VCB = 0xEB01
    RDBSS_NTC_FOBX = 0xEB07
    RDBSS_NTC_RX_CONTEXT = 0xEB08
    RDBSS_NTC_PREFIX_TABLE = 0xEB0D
    RDBSS_NTC_PREFIX_ENTRY = 0xEB0E
    RDBSS_NTC_FCB_TABLE = 0xEB09
    RDBSS_NTC_FCB_TABLE_ENTRY = 0xEB0A
    RDBSS_NTC_RXCE_TRANSPORT = 0xEB71
    RDBSS_NTC_RXCE_ADDRESS = 0xEB72
    RDBSS_NTC_RXCE_CONNECTION = 0xEB73
    RDBSS_NTC_RXCE_VC = 0xEB74
    RDBSS_NTC_NONPAGED_FCB = 0xEBFD
    RDBSS_NTC_COMMON_DISPATCH = 0xEBFE
    RDBSS_NTC_MINIRDR_DISPATCH = 0xEBFF
    RDBSS_STORAGE_TYPE_CODES = USHORT
    RDBSS_NTC_FCB = RDBSS_NTC_STORAGE_TYPE_FILE


    def NodeTypeIsFcb(FCB):
        return NodeType(
            FCB) & 0xFF00 == RDBSS_NTC_STORAGE_TYPE_UNKNOWN or NodeType(
            FCB) & 0xFFF0 == 0xEB90


    # a mask to alter the type of a data structure once it is marked for
    # scavenging so
    # that subsequent tests will fail.
    RX_SCAVENGER_MASK = 0x1000


    # The following definitions are used to generate meaningful blue
    # bugcheck
    # screens. On a bugcheck the file system can output 4 ulongs of useful
    # information. The first ulong will have encoded the line number of the
    # bugcheck call in the low order 16 bits. The high order bits can be
    # whatever
    # the caller wants. In the wrapper, we actually define file
    # identifiers as well.
    # However, the system also displays quire a but of the backtrace; this
    # shows
    # the .sys file of the caller and it is frequently the case that the
    # linenumber
    # is completely disambiguating.
    # Each individual wrapper file that calls bugcheck has defined at the
    # start of the file a constant called BugCheckFileId with one of the
    # RDBSS_BUG_CHECK_ values defined below and then use RxBugCheck to
    # bugcheck
    # the system.
    class _RDBSS_BUG_CHECK_CODES(ENUM):
        RDBSS_BUG_CHECK_FCBSTRUC = 0xFCB00000
        RDBSS_BUG_CHECK_CACHESUP = 0xCA550000
        RDBSS_BUG_CHECK_CLEANUP = 0xC1EE0000
        RDBSS_BUG_CHECK_CLOSE = 0xC10E0000
        RDBSS_BUG_CHECK_NTEXCEPT = 0xBAAD0000


    RDBSS_BUG_CHECK_CODES = _RDBSS_BUG_CHECK_CODES

    # we overload on the original redirector's bugcheck code using the
    # stack
    # backtrace to differentiate among consumers

    from pyWinAPI.shared.bugcodes_h import *  # NOQA


    RDBSS_FILE_SYSTEM = RDR_FILE_SYSTEM


    def RxBugCheck(A, B, C):
        # return { KeBugCheckEx(RDBSS_FILE_SYSTEM, BugCheckFileId | ULONG__LINE__, A, B, C ); }
        pass


    # In this module we'll also define some globally known constants
    UCHAR_NUL = 0x00
    UCHAR_SOH = 0x01
    UCHAR_STX = 0x02
    UCHAR_ETX = 0x03
    UCHAR_EOT = 0x04
    UCHAR_ENQ = 0x05
    UCHAR_ACK = 0x06
    UCHAR_BEL = 0x07
    UCHAR_BS = 0x08
    UCHAR_HT = 0x09
    UCHAR_LF = 0x0A
    UCHAR_VT = 0x0B
    UCHAR_FF = 0x0C
    UCHAR_CR = 0x0D
    UCHAR_SO = 0x0E
    UCHAR_SI = 0x0F
    UCHAR_DLE = 0x10
    UCHAR_DC1 = 0x11
    UCHAR_DC2 = 0x12
    UCHAR_DC3 = 0x13
    UCHAR_DC4 = 0x14
    UCHAR_NAK = 0x15
    UCHAR_SYN = 0x16
    UCHAR_ETB = 0x17
    UCHAR_CAN = 0x18
    UCHAR_EM = 0x19
    UCHAR_SUB = 0x1A
    UCHAR_ESC = 0x1B
    UCHAR_FS = 0x1C
    UCHAR_GS = 0x1D
    UCHAR_RS = 0x1E
    UCHAR_US = 0x1F
    UCHAR_SP = 0x20
    # END IF   _NODETYPE_INCLUDED_
