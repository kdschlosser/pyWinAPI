import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *


__BTHSDPDEF_H__ = None

# Copyright (C) Microsoft. All rights reserved.
if not defined(__BTHSDPDEF_H__):
    __BTHSDPDEF_H__ = 1

    from pyWinAPI.shared.winapifamily_h import *
    from pyWinAPI.shared.sdkddkver_h import *
    from pyWinAPI.shared.guiddef_h import *

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if NTDDI_VERSION >= NTDDI_WINXPSP2:
            if defined(__cplusplus):
                pass
            # END IF

            class SDP_LARGE_INTEGER_16(ctypes.Structure):
                pass


            SDP_LARGE_INTEGER_16._fields_ = [
                ('LowPart', ULONGLONG),
                ('HighPart', LONGLONG),
            ]


            class SDP_ULARGE_INTEGER_16(ctypes.Structure):
                pass


            SDP_ULARGE_INTEGER_16._fields_ = [
                ('LowPart', ULONGLONG),
                ('HighPart', ULONGLONG),
            ]

            PSDP_ULARGE_INTEGER_16 = POINTER(SDP_ULARGE_INTEGER_16)
            LPSDP_ULARGE_INTEGER_16 = POINTER(SDP_ULARGE_INTEGER_16)

            PSDP_LARGE_INTEGER_16 = POINTER(SDP_LARGE_INTEGER_16)
            LPSDP_LARGE_INTEGER_16 = POINTER(SDP_LARGE_INTEGER_16)


            class NodeContainerType(ENUM):
                NodeContainerTypeSequence = 1
                NodeContainerTypeAlternative = 2


            NodeContainerTypeSequence = NodeContainerType.NodeContainerTypeSequence
            NodeContainerTypeAlternative = NodeContainerType.NodeContainerTypeAlternative


            class SDP_TYPE(ENUM):
                SDP_TYPE_NIL = 0x00
                SDP_TYPE_UINT = 0x01
                SDP_TYPE_INT = 0x02
                SDP_TYPE_UUID = 0x03
                SDP_TYPE_STRING = 0x04
                SDP_TYPE_BOOLEAN = 0x05
                SDP_TYPE_SEQUENCE = 0x06
                SDP_TYPE_ALTERNATIVE = 0x07
                SDP_TYPE_URL = 0x08
                SDP_TYPE_CONTAINER = 0x20


            SDP_TYPE_NIL = SDP_TYPE.SDP_TYPE_NIL
            SDP_TYPE_UINT = SDP_TYPE.SDP_TYPE_UINT
            SDP_TYPE_INT = SDP_TYPE.SDP_TYPE_INT
            SDP_TYPE_UUID = SDP_TYPE.SDP_TYPE_UUID
            SDP_TYPE_STRING = SDP_TYPE.SDP_TYPE_STRING
            SDP_TYPE_BOOLEAN = SDP_TYPE.SDP_TYPE_BOOLEAN
            SDP_TYPE_SEQUENCE = SDP_TYPE.SDP_TYPE_SEQUENCE
            SDP_TYPE_ALTERNATIVE = SDP_TYPE.SDP_TYPE_ALTERNATIVE
            SDP_TYPE_URL = SDP_TYPE.SDP_TYPE_URL
            SDP_TYPE_CONTAINER = SDP_TYPE.SDP_TYPE_CONTAINER

            # 9 - 31 are reserved

            # allow for a little easier type checking / sizing for integers
            # and UUIDs

            # ((SDP_ST_XXX & 0xF0) >> 4) == SDP_TYPE_XXX

            # size of the data (in bytes) is encoded as
            # ((SDP_ST_XXX & 0xF0) >> 8)
            class SDP_SPECIFICTYPE(ENUM):
                SDP_ST_NONE = 0x0000
                SDP_ST_UINT8 = 0x0010
                SDP_ST_UINT16 = 0x0110
                SDP_ST_UINT32 = 0x0210
                SDP_ST_UINT64 = 0x0310
                SDP_ST_UINT128 = 0x0410
                SDP_ST_INT8 = 0x0020
                SDP_ST_INT16 = 0x0120
                SDP_ST_INT32 = 0x0220
                SDP_ST_INT64 = 0x0320
                SDP_ST_INT128 = 0x0420
                SDP_ST_UUID16 = 0x0130
                SDP_ST_UUID32 = 0x0220
                SDP_ST_UUID128 = 0x0430


            SDP_ST_NONE = SDP_SPECIFICTYPE.SDP_ST_NONE
            SDP_ST_UINT8 = SDP_SPECIFICTYPE.SDP_ST_UINT8
            SDP_ST_UINT16 = SDP_SPECIFICTYPE.SDP_ST_UINT16
            SDP_ST_UINT32 = SDP_SPECIFICTYPE.SDP_ST_UINT32
            SDP_ST_UINT64 = SDP_SPECIFICTYPE.SDP_ST_UINT64
            SDP_ST_UINT128 = SDP_SPECIFICTYPE.SDP_ST_UINT128
            SDP_ST_INT8 = SDP_SPECIFICTYPE.SDP_ST_INT8
            SDP_ST_INT16 = SDP_SPECIFICTYPE.SDP_ST_INT16
            SDP_ST_INT32 = SDP_SPECIFICTYPE.SDP_ST_INT32
            SDP_ST_INT64 = SDP_SPECIFICTYPE.SDP_ST_INT64
            SDP_ST_INT128 = SDP_SPECIFICTYPE.SDP_ST_INT128
            SDP_ST_UUID16 = SDP_SPECIFICTYPE.SDP_ST_UUID16
            SDP_ST_UUID32 = SDP_SPECIFICTYPE.SDP_ST_UUID32
            SDP_ST_UUID128 = SDP_SPECIFICTYPE.SDP_ST_UUID128


            class _SdpAttributeRange(ctypes.Structure):
                pass


            _SdpAttributeRange._fields_ = [
                ('minAttribute', USHORT),
                ('maxAttribute', USHORT),
            ]

            SdpAttributeRange = _SdpAttributeRange


            class SdpQueryUuidUnion(ctypes.Union):
                pass


            SdpQueryUuidUnion._fields_ = [
                ('uuid128', GUID),
                ('uuid32', ULONG),
                ('uuid16', USHORT),
            ]


            class _SdpQueryUuid(ctypes.Structure):
                pass
            _SdpQueryUuid._fields_ = [
                ('u', SdpQueryUuidUnion),
                ('uuidType', USHORT),
            ]

            SdpQueryUuid = _SdpQueryUuid

            if defined(__cplusplus):
                pass
            # END IF

        # END IF   (NTDDI_VERSION >= NTDDI_WINXPSP2)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __BTHSDPDEF_H__
