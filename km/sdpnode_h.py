import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *


class _SDP_NODE_HEADER(ctypes.Structure):
    pass


SDP_NODE_HEADER = _SDP_NODE_HEADER
PSDP_NODE_HEADER = POINTER(_SDP_NODE_HEADER)


class _SDP_NODE_DATA(ctypes.Union):
    pass


SDP_NODE_DATA = _SDP_NODE_DATA
PSDP_NODE_DATA = POINTER(_SDP_NODE_DATA)


class _SDP_NODE(ctypes.Structure):
    pass


SDP_NODE = _SDP_NODE
PSDP_NODE = POINTER(_SDP_NODE)


class _SDP_TREE_ROOT_NODE(ctypes.Structure):
    pass


SDP_TREE_ROOT_NODE = _SDP_TREE_ROOT_NODE
PSDP_TREE_ROOT_NODE = POINTER(_SDP_TREE_ROOT_NODE)


class ISdpNodeContainer(ctypes.Structure):
    pass


# Copyright (C) Microsoft. All rights reserved.
__SDPNODE_H__ = None
if not defined(__SDPNODE_H__):
    __SDPNODE_H__ = 1

    if _MSC_VER >= 1200:
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_VISTA:
        if defined(__cplusplus):
            pass
        # END IF

        from pyWinAPI.shared.bthsdpdef_h import * # NOQA

        SDP_BOOLEAN = UCHAR
        _SDP_NODE_HEADER._fields_ = [
            ('Link', LIST_ENTRY),
            ('Type', USHORT),
            ('SpecificType', USHORT),
        ]
        _SDP_NODE_DATA._fields_ = [
            # ISSUE is there a better way to represent a 16 byte int???
            ('int128', SDP_LARGE_INTEGER_16),
            ('uint128', SDP_ULARGE_INTEGER_16),
            # UUID
            ('uuid128', GUID),
            ('uuid32', ULONG),
            ('uuid16', USHORT),
            # 8 byte integers
            ('int64', LONGLONG),
            ('uint64', ULONGLONG),
            # 4 byte integers
            ('int32', LONG),
            ('uint32', ULONG),
            # 2 byte integers
            ('int16', SHORT),
            ('uint16', USHORT),
            # 1 bytes integers
            ('int8', CHAR),
            ('uint8', UCHAR),
            # Boolean
            ('boolean', SDP_BOOLEAN),
            # string
            ('string', PCHAR),
            # URL
            ('url', PCHAR),
            # Sequence
            ('sequence', SDP_NODE_HEADER),
            # Alt list
            ('alternative', SDP_NODE_HEADER),
            ('container', POINTER(ISdpNodeContainer)),
        ]
        _SDP_NODE._fields_ = [
            ('hdr', SDP_NODE_HEADER),
            ('DataSize', ULONG),
            ('u', SDP_NODE_DATA),
            ('Reserved', PVOID),
        ]
        _SDP_TREE_ROOT_NODE._fields_ = [
            ('RootNode', SDP_NODE),
        ]

        if defined(__cplusplus):
            pass
        # END IF

    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

    if _MSC_VER >= 1200:
        pass
    else:
        pass
    # END IF

# END IF   __SDPNODE_H__
