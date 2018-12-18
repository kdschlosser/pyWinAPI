import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_NETIODEF_ = None
ASSERT = None
NETIO_INLINE = None
_NTRTL_ = None
BYTE_ORDER = None
vax = None
ns32000 = None
sun386 = None
MIPSEL = None
BIT_ZERO_ON_RIGHT = None
sel = None
pyr = None
mc68000 = None
sparc = None
is68k = None
tahoe = None
ibm032 = None
ibm370 = None
MIPSEB = None
BIT_ZERO_ON_LEFT = None
u3b2 = None
m68k = None
i286 = None
_ARM64_ = None
_DEFINE_DL_ADDRESS_TYPE_ = None
IP_EXPORT_INCLUDED = None
NETIODEF_DEFINED_ASSERT = None

class _DL_OUI(ctypes.Union):
    pass





class _DL_EI48(ctypes.Union):
    pass





class _DL_EUI48(ctypes.Union):
    pass





class _DL_EI64(ctypes.Union):
    pass





class _DL_EUI64(ctypes.Union):
    pass





class _SNAP_HEADER(ctypes.Structure):
    pass


SNAP_HEADER = _SNAP_HEADER
PSNAP_HEADER = POINTER(_SNAP_HEADER)


class _ETHERNET_HEADER(ctypes.Structure):
    pass


ETHERNET_HEADER = _ETHERNET_HEADER
PETHERNET_HEADER = POINTER(_ETHERNET_HEADER)


class _VLAN_TAG(ctypes.Structure):
    pass


VLAN_TAG = _VLAN_TAG


class _ICMP_HEADER(ctypes.Structure):
    pass


ICMP_HEADER = _ICMP_HEADER
PICMP_HEADER = POINTER(_ICMP_HEADER)


class _ICMP_MESSAGE(ctypes.Structure):
    pass


ICMP_MESSAGE = _ICMP_MESSAGE
PICMP_MESSAGE = POINTER(_ICMP_MESSAGE)


class _IPV4_HEADER(ctypes.Structure):
    pass


IPV4_HEADER = _IPV4_HEADER
PIPV4_HEADER = POINTER(_IPV4_HEADER)


class _IPV4_OPTION_HEADER(ctypes.Structure):
    pass


IPV4_OPTION_HEADER = _IPV4_OPTION_HEADER
PIPV4_OPTION_HEADER = POINTER(_IPV4_OPTION_HEADER)


class _IPV4_TIMESTAMP_OPTION(ctypes.Structure):
    pass


IPV4_TIMESTAMP_OPTION = _IPV4_TIMESTAMP_OPTION
PIPV4_TIMESTAMP_OPTION = POINTER(_IPV4_TIMESTAMP_OPTION)


class _IPV4_ROUTING_HEADER(ctypes.Structure):
    pass


IPV4_ROUTING_HEADER = _IPV4_ROUTING_HEADER
UNALIGNED *PIPV4_ROUTING_HEADER = _IPV4_ROUTING_HEADER


class _ICMPV4_ROUTER_SOLICIT(ctypes.Structure):
    pass


ICMPV4_ROUTER_SOLICIT = _ICMPV4_ROUTER_SOLICIT
PICMPV4_ROUTER_SOLICIT = POINTER(_ICMPV4_ROUTER_SOLICIT)


class _ICMPV4_ROUTER_ADVERT_HEADER(ctypes.Structure):
    pass


ICMPV4_ROUTER_ADVERT_HEADER = _ICMPV4_ROUTER_ADVERT_HEADER
PICMPV4_ROUTER_ADVERT_HEADER = POINTER(_ICMPV4_ROUTER_ADVERT_HEADER)


class _ICMPV4_ROUTER_ADVERT_ENTRY(ctypes.Structure):
    pass


ICMPV4_ROUTER_ADVERT_ENTRY = _ICMPV4_ROUTER_ADVERT_ENTRY
PICMPV4_ROUTER_ADVERT_ENTRY = POINTER(_ICMPV4_ROUTER_ADVERT_ENTRY)


class _ICMPV4_TIMESTAMP_MESSAGE(ctypes.Structure):
    pass


ICMPV4_TIMESTAMP_MESSAGE = _ICMPV4_TIMESTAMP_MESSAGE
PICMPV4_TIMESTAMP_MESSAGE = POINTER(_ICMPV4_TIMESTAMP_MESSAGE)


class _ICMPV4_ADDRESS_MASK_MESSAGE(ctypes.Structure):
    pass


ICMPV4_ADDRESS_MASK_MESSAGE = _ICMPV4_ADDRESS_MASK_MESSAGE
PICMPV4_ADDRESS_MASK_MESSAGE = POINTER(_ICMPV4_ADDRESS_MASK_MESSAGE)


class _ARP_HEADER(ctypes.Structure):
    pass


ARP_HEADER = _ARP_HEADER
PARP_HEADER = POINTER(_ARP_HEADER)


class _IGMP_HEADER(ctypes.Structure):
    pass


IGMP_HEADER = _IGMP_HEADER
PIGMP_HEADER = POINTER(_IGMP_HEADER)


class _IGMPV3_QUERY_HEADER(ctypes.Structure):
    pass


IGMPV3_QUERY_HEADER = _IGMPV3_QUERY_HEADER
PIGMPV3_QUERY_HEADER = POINTER(_IGMPV3_QUERY_HEADER)


class _IGMPV3_REPORT_RECORD_HEADER(ctypes.Structure):
    pass


IGMPV3_REPORT_RECORD_HEADER = _IGMPV3_REPORT_RECORD_HEADER
PIGMPV3_REPORT_RECORD_HEADER = POINTER(_IGMPV3_REPORT_RECORD_HEADER)


class _IGMPV3_REPORT_HEADER_(ctypes.Structure):
    pass


IGMPV3_REPORT_HEADER = _IGMPV3_REPORT_HEADER_
PIGMPV3_REPORT_HEADER = POINTER(_IGMPV3_REPORT_HEADER_)


class _IPV6_HEADER(ctypes.Structure):
    pass


IPV6_HEADER = _IPV6_HEADER
PIPV6_HEADER = POINTER(_IPV6_HEADER)


class _IPV6_FRAGMENT_HEADER(ctypes.Structure):
    pass


IPV6_FRAGMENT_HEADER = _IPV6_FRAGMENT_HEADER
PIPV6_FRAGMENT_HEADER = POINTER(_IPV6_FRAGMENT_HEADER)


class _IPV6_EXTENSION_HEADER(ctypes.Structure):
    pass


IPV6_EXTENSION_HEADER = _IPV6_EXTENSION_HEADER
PIPV6_EXTENSION_HEADER = POINTER(_IPV6_EXTENSION_HEADER)


class _IPV6_OPTION_HEADER(ctypes.Structure):
    pass


IPV6_OPTION_HEADER = _IPV6_OPTION_HEADER
PIPV6_OPTION_HEADER = POINTER(_IPV6_OPTION_HEADER)


class _IPV6_OPTION_JUMBOGRAM(ctypes.Structure):
    pass


IPV6_OPTION_JUMBOGRAM = _IPV6_OPTION_JUMBOGRAM
PIPV6_OPTION_JUMBOGRAM = POINTER(_IPV6_OPTION_JUMBOGRAM)


class _IPV6_OPTION_ROUTER_ALERT(ctypes.Structure):
    pass


IPV6_OPTION_ROUTER_ALERT = _IPV6_OPTION_ROUTER_ALERT
PIPV6_OPTION_ROUTER_ALERT = POINTER(_IPV6_OPTION_ROUTER_ALERT)


class nd_router_solicit(ctypes.Structure):
    pass


ND_ROUTER_SOLICIT_HEADER = nd_router_solicit
PND_ROUTER_SOLICIT_HEADER = POINTER(nd_router_solicit)


class nd_router_advert(ctypes.Structure):
    pass


ND_ROUTER_ADVERT_HEADER = nd_router_advert
PND_ROUTER_ADVERT_HEADER = POINTER(nd_router_advert)


class _IPV6_ROUTER_ADVERTISEMENT_FLAGS(ctypes.Union):
    pass


IPV6_ROUTER_ADVERTISEMENT_FLAGS = _IPV6_ROUTER_ADVERTISEMENT_FLAGS
PIPV6_ROUTER_ADVERTISEMENT_FLAGS = POINTER(_IPV6_ROUTER_ADVERTISEMENT_FLAGS)


class nd_neighbor_solicit(ctypes.Structure):
    pass


ND_NEIGHBOR_SOLICIT_HEADER = nd_neighbor_solicit
PND_NEIGHBOR_SOLICIT_HEADER = POINTER(nd_neighbor_solicit)


class nd_neighbor_advert(ctypes.Structure):
    pass


ND_NEIGHBOR_ADVERT_HEADER = nd_neighbor_advert
PND_NEIGHBOR_ADVERT_HEADER = POINTER(nd_neighbor_advert)


class _IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS(ctypes.Union):
    pass


IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS = _IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS
PIPV6_NEIGHBOR_ADVERTISEMENT_FLAGS = POINTER(_IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS)


class nd_redirect(ctypes.Structure):
    pass


ND_REDIRECT_HEADER = nd_redirect
PND_REDIRECT_HEADER = POINTER(nd_redirect)


class nd_opt_hdr(ctypes.Structure):
    pass


ND_OPTION_HDR = nd_opt_hdr
PND_OPTION_HDR = POINTER(nd_opt_hdr)


class nd_opt_prefix_info(ctypes.Structure):
    pass


ND_OPTION_PREFIX_INFO = nd_opt_prefix_info
PND_OPTION_PREFIX_INFO = POINTER(nd_opt_prefix_info)


class nd_opt_rd_hdr(ctypes.Structure):
    pass


ND_OPTION_RD_HDR = nd_opt_rd_hdr
PND_OPTION_RD_HDR = POINTER(nd_opt_rd_hdr)


class nd_opt_mtu(ctypes.Structure):
    pass


ND_OPTION_MTU = nd_opt_mtu
PND_OPTION_MTU = POINTER(nd_opt_mtu)


class nd_opt_route_info(ctypes.Structure):
    pass


ND_OPTION_ROUTE_INFO = nd_opt_route_info
PND_OPTION_ROUTE_INFO = POINTER(nd_opt_route_info)


class nd_opt_rdnss(ctypes.Structure):
    pass


ND_OPTION_RDNSS = nd_opt_rdnss
PND_OPTION_RDNSS = POINTER(nd_opt_rdnss)


class nd_opt_dnssl(ctypes.Structure):
    pass


ND_OPTION_DNSSL = nd_opt_dnssl
PND_OPTION_DNSSL = POINTER(nd_opt_dnssl)


class _MLD_HEADER(ctypes.Structure):
    pass


MLD_HEADER = _MLD_HEADER
PMLD_HEADER = POINTER(_MLD_HEADER)


class _MLDV2_QUERY_HEADER(ctypes.Structure):
    pass


MLDV2_QUERY_HEADER = _MLDV2_QUERY_HEADER
PMLDV2_QUERY_HEADER = POINTER(_MLDV2_QUERY_HEADER)


class _MLDV2_REPORT_RECORD_HEADER(ctypes.Structure):
    pass


MLDV2_REPORT_RECORD_HEADER = _MLDV2_REPORT_RECORD_HEADER
PMLDV2_REPORT_RECORD_HEADER = POINTER(_MLDV2_REPORT_RECORD_HEADER)


class _MLDV2_REPORT_HEADER(ctypes.Structure):
    pass


MLDV2_REPORT_HEADER = _MLDV2_REPORT_HEADER
PMLDV2_REPORT_HEADER = POINTER(_MLDV2_REPORT_HEADER)


class (ctypes.Union):
    pass


class tcp_hdr(ctypes.Structure):
    pass


TCP_HDR
            #if NDIS_RECEIVE_UNALIGNED = tcp_hdr


class tcp_opt_mss(ctypes.Structure):
    pass


TCP_OPT_MSS = tcp_opt_mss


class tcp_opt_ws(ctypes.Structure):
    pass


TCP_OPT_WS = tcp_opt_ws


class tcp_opt_sack_permitted(ctypes.Structure):
    pass


TCP_OPT_SACK_PERMITTED = tcp_opt_sack_permitted


class tcp_opt_sack(ctypes.Structure):
    pass


TCP_OPT_SACK = tcp_opt_sack


class tcp_opt_ts(ctypes.Structure):
    pass


TCP_OPT_TS = tcp_opt_ts


class tcp_opt_unknown(ctypes.Structure):
    pass


TCP_OPT_UNKNOWN = tcp_opt_unknown


class tcp_opt_fastopen(ctypes.Structure):
    pass


TCP_OPT_FASTOPEN = tcp_opt_fastopen


class DL_TUNNEL_ADDRESS(ctypes.Structure):
    pass


PDL_TUNNEL_ADDRESS = POINTER(DL_TUNNEL_ADDRESS)


class DL_TEREDO_ADDRESS(ctypes.Structure):
    pass


PDL_TEREDO_ADDRESS = POINTER(DL_TEREDO_ADDRESS)


class DL_TEREDO_ADDRESS_PRV(ctypes.Structure):
    pass


PDL_TEREDO_ADDRESS_PRV = POINTER(DL_TEREDO_ADDRESS_PRV)


class _IPTLS_METADATA(ctypes.Structure):
    pass


IPTLS_METADATA = _IPTLS_METADATA
PIPTLS_METADATA = POINTER(_IPTLS_METADATA)


class _NPI_MODULEID(ctypes.Structure):
    pass


NPI_MODULEID = _NPI_MODULEID




# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: netiodef.h Abstract: This module contains the basic definitions and
# structures for the network I/O subsystem. Environment: user mode or kernel
# mode --
if not defined(_NETIODEF_):
    _NETIODEF_ = VOID
    from winapifamily_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        from ws2def_h import * # NOQA
        from ws2ipdef_h import * # NOQA
        from mswsockdef_h import * # NOQA
        from mstcpip_h import * # NOQA
        from nldef_h import * # NOQA
        if not defined(ASSERT):
            def ASSERT(exp):
                return VOID 0
            NETIODEF_DEFINED_ASSERT = VOID
        # END IF


        if not defined(NETIO_INLINE):
            if DBG:
                NETIO_INLINE = __inline
            else:
                NETIO_INLINE = __forceinline
            # END IF

        # END IF


        def IS_POWER_OF_TWO(x):
            return ((x != 0) and ((x & (x - 1)) == 0))
        if defined(_NTDDK_) or defined(_NTRTL_):
            def IS_VALID_IPV4_MASK(x):
                return (
                    (x.S_un.S_addr == -1) or 
                    IS_POWER_OF_TWO(~RtlUlongByteSwapx.S_un.S_addr + 1)
                )
        # END IF


        if not defined(BYTE_ORDER):
            _LITTLE_ENDIAN = 1234            # least-significant byte first (vax)
            _BIG_ENDIAN = 4321            # most-significant byte first (IBM, net)
            _PDP_ENDIAN = 3412            # LSB first in word, MSW first in LONG (pdp)
            if defined(vax) or defined(ns32000) or defined(sun386) or defined(MIPSEL) or defined(BIT_ZERO_ON_RIGHT):
                BYTE_ORDER = _LITTLE_ENDIAN
            # END IF


            if defined(sel) or defined(pyr) or defined(mc68000) or defined(sparc) or defined(is68k) or defined(tahoe) or defined(ibm032) or defined(ibm370) or defined(MIPSEB) or defined (BIT_ZERO_ON_LEFT):
                BYTE_ORDER = _BIG_ENDIAN
            # END IF


            if not defined(BYTE_ORDER):
                if defined(u3b2) or defined(m68k):
                    BYTE_ORDER = _BIG_ENDIAN
                # END IF


                if defined(i286) or defined(_X86_) or defined(_AMD64_) or defined(_IA64_) or defined(_ARM_) or defined(_ARM64_):
                    BYTE_ORDER = _LITTLE_ENDIAN
                # END IF

            # END IF

        # END IF


        if not defined(BYTE_ORDER):
            # you must determine what the correct bit order is for your
            # compiler        # END IF
        # Opaque handles that are a specific number of bits wide.
        HANDLE8 = UINT8
        PHANDLE8 = POINTER(UINT8)
        HANDLE16 = UINT16
        PHANDLE16 = POINTER(UINT16)
        HANDLE32 = UINT32
        PHANDLE32 = POINTER(UINT32)
        HANDLE64 = UINT64
        PHANDLE64 = POINTER(UINT64)
        

        def MAKE_DD_DEVICE_NAME(x):
            return "\\Device\\" x
        

        def MAKE_WIN_DEVICE_NAME(x):
            return "\\\\.\\" x
        from ifdef_h import * # NOQA
            if _MSC_VER >= 1200:
                pass
            # END IF


        if defined(_MSC_VER):
            pass
        # END IF   defined(_MSC_VER)


        # For buffer sizing convenience, define a maximum datalink address
        # length.
        DL_ADDRESS_LENGTH_MAXIMUM = IF_MAX_PHYS_ADDRESS_LENGTH
        DL_HEADER_LENGTH_MAXIMUM = 64
        DL_ETHERNET_HEADER_LENGTH_MAXIMUM = (
            (ctypes.sizeof(ETHERNET_HEADER) + (ctypes.sizeof(SNAP_HEADER)
        )
        DL_TUNNEL_HEADER_LENGTH_MAXIMUM = (
            max((ctypes.sizeof(IPV4_HEADER),
            (ctypes.sizeof(IPV6_HEADER))
        )
        # DL_ADDRESS_TYPE
        # Define datalink layer address types.
        if not defined(_DEFINE_DL_ADDRESS_TYPE_):
            _DEFINE_DL_ADDRESS_TYPE_ = VOID


            class DL_ADDRESS_TYPE(ENUM):
                DlUnicast = 1
                DlMulticast = 2
                DlBroadcast = 3

            PDL_ADDRESS_TYPE = POINTER(DL_ADDRESS_TYPE)


            DlUnicast = DL_ADDRESS_TYPE.DlUnicast
            DlMulticast = DL_ADDRESS_TYPE.DlMulticast
            DlBroadcast = DL_ADDRESS_TYPE.DlBroadcast
        # END IF   _DEFINE_DL_ADDRESS_TYPE_

        # DL_OUI
        # Define Organizationally Unique Identifier.
        # least significant bit.
        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            ('Group', UINT8, 1),
            ('Local', UINT8, 1),
        ]
        _DL_OUI._Struct_1 = _Struct_1

        _DL_OUI._anonymous_ = (
            '_Struct_1',
        )

        _DL_OUI._fields_ = [
            ('Byte', UINT8 * 3),
            # 1st byte. 0bxxxxxxLG.
            ('_Struct_1', _DL_OUI._Struct_1),
        ]
        PDL_OUI = POINTER(DL_OUI,)


        # DL_EI48
        # Define Extension Identifier for EUI-48 Addresses.
        _DL_EI48._fields_ = [
            ('Byte', UINT8 * 3),
        ]
        PDL_EI48 = POINTER(DL_EI48,)


        # DL_EUI48
        # Define EUI-48 Address.
        class _Struct_2(ctypes.Structure):
            pass


        _Struct_2._fields_ = [
            ('Oui', DL_OUI),
            ('Ei48', DL_EI48),
        ]
        _DL_EUI48._Struct_2 = _Struct_2

        _DL_EUI48._anonymous_ = (
            '_Struct_2',
        )

        _DL_EUI48._fields_ = [
            ('Byte', UINT8 * 6),
            ('_Struct_2', _DL_EUI48._Struct_2),
        ]
        PDL_EUI48 = POINTER(DL_EUI48,)

        EUI48_BROADCAST_INIT = [ 0xFF,0xFF,0xFF,0xFF,0xFF,0xFF ]


        # DL_EI64
        # Define Extension Identifier for EUI-64 Addresses.
        _DL_EI64._fields_ = [
            ('Byte', UINT8 * 5),
        ]
        PDL_EI64 = POINTER(DL_EI64,)


        # DL_EUI64
        # Define EUI-64 Address.
        class _Struct_3(ctypes.Structure):
            pass


        class _Union_1(ctypes.Union):
            pass

        # Determines interpretation of rest.
        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('Type', UINT8),
            # Type specific extention.
            ('Tse', UINT8),
            # Encapsulated EUI-48 EI.
            ('Ei48', DL_EI48),
        ]
        _Union_1._Struct_4 = _Struct_4

        _Union_1._anonymous_ = (
            '_Struct_4',
        )

        _Union_1._fields_ = [
            ('Ei64', DL_EI64),
            # draft-templin-ngtrans-v6v4compat-02.
            ('_Struct_4', _Union_1._Struct_4),
        ]
        _Struct_3._Union_1 = _Union_1

        _Struct_3._anonymous_ = (
            '_Union_1',
        )

        _Struct_3._fields_ = [
            ('Oui', DL_OUI),
            ('_Union_1', _Struct_3._Union_1),
        ]
        _DL_EUI64._Struct_3 = _Struct_3

        _DL_EUI64._anonymous_ = (
            '_Struct_3',
        )

        _DL_EUI64._fields_ = [
            ('Byte', UINT8 * 8),
            ('Value', UINT64),
            ('_Struct_3', _DL_EUI64._Struct_3),
        ]
        PDL_EUI64 = POINTER(DL_EUI64,)


        # SNAP_HEADER
        # Define a structure for the SNAP header.
        _SNAP_HEADER._fields_ = [
            ('Dsap', UINT8),
            ('Ssap', UINT8),
            ('Control', UINT8),
            ('Oui', UINT8 * 3),
            ('Type', UINT16),
        ]
        SNAP_DSAP = 0xAA
        SNAP_SSAP = 0xAA
        SNAP_CONTROL = 0x03
        SNAP_OUI = 0x00

        # Since TYPE values are identical to those used by ethernet...
        SNAP_TYPE_ARP = ETHERNET_TYPE_ARP
        SNAP_TYPE_IPV4 = ETHERNET_TYPE_IPV4
        SNAP_TYPE_IPV6 = ETHERNET_TYPE_IPV6

        # ETHERNET_HEADER
        # Define a common structure for the ethernet and IEEE 802 headers.
        # NOTE: An IEEE 802 header is followed by a SNAP header.
        # Ethernet
        class _Union_1(ctypes.Union):
            pass


        _Union_1._fields_ = [
            ('Type', UINT16),
            # IEEE 802
            ('Length', UINT16),
        ]
        _ETHERNET_HEADER._Union_1 = _Union_1

        _ETHERNET_HEADER._anonymous_ = (
            '_Union_1',
        )

        _ETHERNET_HEADER._fields_ = [
            ('Destination', DL_EUI48),
            ('Source', DL_EUI48),
            ('_Union_1', _ETHERNET_HEADER._Union_1),
        ]
        ETH_LENGTH_OF_HEADER = 14
        ETH_LENGTH_OF_VLAN_HEADER = 4
        ETH_LENGTH_OF_SNAP_HEADER = 8
        ETHERNET_TYPE_MINIMUM = 0x0600        # Minimum valid Type value.
        ETHERNET_TYPE_IPV4 = 0x0800
        ETHERNET_TYPE_ARP = 0x0806
        ETHERNET_TYPE_IPV6 = 0x86DD
        ETHERNET_TYPE_802_1Q = 0x8100


        # VLAN_TAG
        class _Union_2(ctypes.Union):
            pass

        # least significant bit
        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('VID', UINT16, 12),
            ('CFI', UINT16, 1),
            ('User_Priority', UINT16, 3),
        ]
        _Union_2._Struct_4 = _Struct_4

        _Union_2._anonymous_ = (
            '_Struct_4',
        )

        _Union_2._fields_ = [
            ('Tag', UINT16),
            ('_Struct_4', _Union_2._Struct_4),
        ]
        _VLAN_TAG._Union_2 = _Union_2

        _VLAN_TAG._anonymous_ = (
            '_Union_2',
        )

        _VLAN_TAG._fields_ = [
            ('_Union_2', _VLAN_TAG._Union_2),
            # this really is the type, since we come after the SNAP header
            ('Type', UINT16),
        ]
            if _MSC_VER >= 1200:
                pass
            else:
                pass
            # END IF


        if defined (_MSC_VER):
            pass
        # END IF


        # Type of message (high bit zero for error messages).
        _ICMP_HEADER._fields_ = [
            ('Type', UINT8),
            # Type-specific differentiater.
            ('Code', UINT8),
            # Calculated over ICMP message and IPvx pseudo-header.
            ('Checksum', UINT16),
        ]

        # Type-specific field.
        class Data(ctypes.Union):
            pass


        Data._fields_ = [
            ('Data32', UINT32 * 1),
            # Type-specific field.
            ('Data16', UINT16 * 2),
            # Type-specific field.
            ('Data8', UINT8 * 4),
        ]
        _ICMP_MESSAGE.Data = Data


        _ICMP_MESSAGE._fields_ = [
            ('Header', ICMP_HEADER),
            ('Data', _ICMP_MESSAGE.Data),
        ]
            if _MSC_VER >= 1200:
                pass
            # END IF


        if defined(_MSC_VER):
            pass
        # END IF   defined(_MSC_VER)


        # IPV4_HEADER
        # Define the structure of an IPv4 header.
        # The field names match those in section 3.1 of RFC 791.
        # RFC 2474 redefines type of service to the 6 bit DSCP value. RFC 2780
        # and
        # 3168 redefine the unused 2 bits in the traffic class octet as used by
        # ECN.
        # Version and header length.
        class _Union_3(ctypes.Union):
            pass


        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('HeaderLength', UINT8, 4),
            ('Version', UINT8, 4),
        ]
        _Union_3._Struct_4 = _Struct_4

        _Union_3._anonymous_ = (
            '_Struct_4',
        )

        _Union_3._fields_ = [
            ('VersionAndHeaderLength', UINT8),
            ('_Struct_4', _Union_3._Struct_4),
        ]
        _IPV4_HEADER._Union_3 = _Union_3


        # Type of service & ECN (RFC 3168).
        class _Union_4(ctypes.Union):
            pass


        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('EcnField', UINT8, 2),
            ('TypeOfService', UINT8, 6),
        ]
        _Union_4._Struct_4 = _Struct_4

        _Union_4._anonymous_ = (
            '_Struct_4',
        )

        _Union_4._fields_ = [
            ('TypeOfServiceAndEcnField', UINT8),
            ('_Struct_4', _Union_4._Struct_4),
        ]
        _IPV4_HEADER._Union_4 = _Union_4


        # Flags and fragment offset.
        class _Union_5(ctypes.Union):
            pass

        # High bits of fragment offset.
        class _Struct_4(ctypes.Structure):
            pass


        _Struct_4._fields_ = [
            ('DontUse1', UINT16, 5),
            ('MoreFragments', UINT16, 1),
            ('DontFragment', UINT16, 1),
            ('Reserved', UINT16, 1),
            # Low bits of fragment offset.
            ('DontUse2', UINT16, 8),
        ]
        _Union_5._Struct_4 = _Struct_4

        _Union_5._anonymous_ = (
            '_Struct_4',
        )

        _Union_5._fields_ = [
            ('FlagsAndOffset', UINT16),
            ('_Struct_4', _Union_5._Struct_4),
        ]
        _IPV4_HEADER._Union_5 = _Union_5

        _IPV4_HEADER._anonymous_ = (
            '_Union_3',
            '_Union_4',
            '_Union_5',
        )

        _IPV4_HEADER._fields_ = [
            ('_Union_3', _IPV4_HEADER._Union_3),
            ('_Union_4', _IPV4_HEADER._Union_4),
            # Total length of datagram.
            ('TotalLength', UINT16),
            ('Identification', UINT16),
            ('_Union_5', _IPV4_HEADER._Union_5),
            ('TimeToLive', UINT8),
            ('Protocol', UINT8),
            ('HeaderChecksum', UINT16),
            ('SourceAddress', IN_ADDR),
            ('DestinationAddress', IN_ADDR),
        ]
        ip4_hdr = _IPV4_HEADER
        ip4_ver_hlen = VersionAndHeaderLength
        ip4_ver = Version
        ip4_hlen = HeaderLength
        ip4_tos = TypeOfService
        ip4_len = TotalLength
        ip4_id = Identification
        ip4_flags_offset = FlagsAndOffset
        ip4_flags = Flags
        ip4_offset = FragmentOffset
        ip4_ttl = TimeToLive
        ip4_protocol = Protocol
        ip4_xsum = HeaderChecksum
        ip4_src = SourceAddress
        ip4_dest = DestinationAddress
        IP_VER_MASK = 0xF0        # Version is high 4 bits of ip4_ver_hlen.
        IPV4_VERSION = 4
        IPV4_DEFAULT_VERHLEN = (
            (IPV4_VERSION << 4) | 
            ((ctypes.sizeof(IPV4_HEADER) / (ctypes.sizeof)
        )
        MAX_IPV4_PACKET = 65535
        MAX_IPV4_PAYLOAD = MAX_IPV4_PACKET - (ctypes.sizeof(IPV4_HEADER)
        MAX_IPV4_HLEN = 60
        IPV4_MINIMUM_MTU = 576
        IPV4_MINIMUM_ULMTU = IPV4_MINIMUM_MTU - (ctypes.sizeof(IPV4_HEADER)
        # The maximum and minimum values for the lower limit of the value the
        # MTU can
        # have during PMTU discovery.
        # The minimum value was chosen to be a reasonable limit for real-world
        # scenarios, while at the same time minimizing security risks.
        IPV4_MIN_MINIMUM_MTU = 352
        IPV4_MAX_MINIMUM_MTU = IPV4_MINIMUM_MTU
        # TODO: remove UNALIGNED qualifier once NetGetDataBuffer takes an
        # alignment argument.
        ntoskrnl = ctypes.windll.NTOSKRNL
        # }
        # 
        # 
        # // Maximum length of IP options.
        # 
        # #define MAX_IP_OPTIONS_LENGTH ((0xF * (ctypes.sizeof(UINT32)) - (ctypes.sizeof(IPV4_HEADER))
        # 
        # #define SIZEOF_IP_OPT_ROUTING_HEADER 3
        # 
        # #define SIZEOF_IP_OPT_TIMESTAMP_HEADER 4
        # 
        # #define SIZEOF_IP_OPT_SECURITY 11
        # #define SIZEOF_IP_OPT_STREAMIDENTIFIER 4
        # #define SIZEOF_IP_OPT_ROUTERALERT 4
        # 
        # #define IP4_OFF_MASK 0xff1f // Mask out offset from FlagsAndOffset.
        # 
        # #if defined(_NTDDK_) or defined(_NTRTL_)
        # 
        # // Only include this definition if RtlUshortByteSwap is defined.
        # 
        # 
        # __inline
        # UINT16
        # Ip4FragmentOffset(
        # _In_ CONST UNALIGNED IPV4_HEADER *Header
        # )
        # {
        # return RtlUshortByteSwap(Header.FlagsAndOffset & IP4_OFF_MASK) << 3;
        RtlUshortByteSwap = ntoskrnl.RtlUshortByteSwap
        RtlUshortByteSwap.restype = definition
    # END IF
    # IPV4_OPTION_HEADER
    # Option type.
    class _Union_6(ctypes.Union):
        pass


    class _Struct_4(ctypes.Structure):
        pass


    _Struct_4._fields_ = [
        ('OptionNumber', UINT8, 5),
        ('OptionClass', UINT8, 2),
        ('CopiedFlag', UINT8, 1),
    ]
    _Union_6._Struct_4 = _Struct_4

    _Union_6._anonymous_ = (
        '_Struct_4',
    )

    _Union_6._fields_ = [
        ('OptionType', UINT8),
        ('_Struct_4', _Union_6._Struct_4),
    ]
    _IPV4_OPTION_HEADER._Union_6 = _Union_6

    _IPV4_OPTION_HEADER._anonymous_ = (
        '_Union_6',
    )

    _IPV4_OPTION_HEADER._fields_ = [
        ('_Union_6', _IPV4_OPTION_HEADER._Union_6),
        # Length in bytes, starting from the OptionType field.
        ('OptionLength', UINT8),
    ]
    if not defined(IP_EXPORT_INCLUDED):
            # ENUM ERROR: typedef enum {
    else:
        IPV4_OPTION_TYPE = ULONG
    # END IF   IP_EXPORT_INCLUDED


    class _Union_7(ctypes.Union):
        pass


    class _Struct_4(ctypes.Structure):
        pass


    _Struct_4._fields_ = [
        ('Flags', UINT8, 4),
        ('Overflow', UINT8, 4),
    ]
    _Union_7._Struct_4 = _Struct_4

    _Union_7._anonymous_ = (
        '_Struct_4',
    )

    _Union_7._fields_ = [
        ('FlagsOverflow', UINT8),
        ('_Struct_4', _Union_7._Struct_4),
    ]
    _IPV4_TIMESTAMP_OPTION._Union_7 = _Union_7

    _IPV4_TIMESTAMP_OPTION._anonymous_ = (
        '_Union_7',
    )

    _TEMP__IPV4_TIMESTAMP_OPTION = [
    ]
    if defined(__cplusplus):
            _TEMP__IPV4_TIMESTAMP_OPTION += [
            ('OptionHeader', IPV4_OPTION_HEADER),
            ]
        # END IF


            _TEMP__IPV4_TIMESTAMP_OPTION += [
        ('Pointer', UINT8),
        ('_Union_7', _IPV4_TIMESTAMP_OPTION._Union_7),
            ]
            _IPV4_TIMESTAMP_OPTION._fields_ = _TEMP__IPV4_TIMESTAMP_OPTION
        # ENUM ERROR: typedef enum {
    # Structure to interpret the IPv4 loose and strict source routing options
    # as
    # a routing header similar to IPv6.
    _TEMP__IPV4_ROUTING_HEADER = [
    ]
    if defined(__cplusplus):
            _TEMP__IPV4_ROUTING_HEADER += [
            ('OptionHeader', IPV4_OPTION_HEADER),
            ]
        # END IF


            _TEMP__IPV4_ROUTING_HEADER += [
        ('Pointer', UINT8),
            ]
            _IPV4_ROUTING_HEADER._fields_ = _TEMP__IPV4_ROUTING_HEADER


    # ICMPV4_HEADER
    # Define the structure of an ICMPv4 header.
    ICMPV4_HEADER = ICMP_HEADER
    PICMPV4_HEADER = POINTER(ICMP_HEADER)
    ICMPV4_MESSAGE = ICMP_MESSAGE
    PICMPV4_MESSAGE = POINTER(ICMP_MESSAGE)
    icmp4_hdr = _ICMPV4_MESSAGE
    icmp4_type = Header.Type
    icmp4_code = Header.Code
    icmp4_cksum = Header.Checksum
    icmp4_un_data32 = Data32
    icmp4_un_data16 = Data16
    icmp4_un_data8 = Data8
    icmp4_dataun = Data
    icmp4_data32 = icmp4_dataun.icmp4_un_data32
    icmp4_data16 = icmp4_dataun.icmp4_un_data16
    icmp4_data8 = icmp4_dataun.icmp4_un_data8
    icmp4_pptr = icmp4_data32[0]    # Parameter problem.
    icmp4_mtu = icmp4_data32[0]    # Packet too big.
    icmp4_id = icmp4_data16[0]    # Echo request/reply.
    icmp4_seq = icmp4_data16[1]    # Echo request/reply.
    icmp4_maxdelay = icmp4_data16[0]    # Multicast group membership.

    # ICMP4_UNREACH_CODE
    # Define codes for the ICMPv4 destination-unreachable error message.
        # ENUM ERROR: typedef enum {
    # ICMP4_TIME_EXCEED_CODE
    # Define codes for the ICMPv4 time-exceeded error message.
        # ENUM ERROR: typedef enum {
    # Define a structure for IPv4 router solicitation.
    _ICMPV4_ROUTER_SOLICIT._fields_ = [
        ('RsHeader', ICMPV4_MESSAGE),
    ]
    RsType = RsHeader.icmp4_type
    RsCode = RsHeader.icmp4_code
    RsCksum = RsHeader.icmp4_cksum
    RsReserved = RsHeader.icmp4_data32[0]
    _ICMPV4_ROUTER_ADVERT_HEADER._fields_ = [
        ('RaHeader', ICMPV4_MESSAGE),
    ]
    RaType = RaHeader.icmp4_type
    RaCode = RaHeader.icmp4_code
    RaCksum = RaHeader.icmp4_cksum
    RaNumAddr = RaHeader.icmp4_data8[0]
    RaAddrEntrySize = RaHeader.icmp4_data8[1]
    RaAddrLifetime = RaHeader.icmp4_data16[1]
    _ICMPV4_ROUTER_ADVERT_ENTRY._fields_ = [
        ('RouterAdvertAddr', IN_ADDR),
        ('PreferenceLevel', LONG),
    ]
    ICMPV4_INVALID_PREFERENCE_LEVEL = 0x80000000
    _ICMPV4_TIMESTAMP_MESSAGE._fields_ = [
        ('Header', ICMPV4_MESSAGE),
        ('OriginateTimestamp', UINT32),
        ('ReceiveTimestamp', UINT32),
        ('TransmitTimestamp', UINT32),
    ]
    _ICMPV4_ADDRESS_MASK_MESSAGE._fields_ = [
        ('Header', ICMPV4_MESSAGE),
        ('AddressMask', UINT32),
    ]
    icmp4_ts_type = Header.icmp4_type
    icmp4_ts_code = Header.icmp4_code
    icmp4_ts_cksum = Header.icmp4_cksum
    icmp4_ts_id = Header.icmp4_id
    icmp4_ts_seq = Header.icmp4_seq
    icmp4_ts_originate = OriginateTimestamp
    icmp4_ts_receive = ReceiveTimestamp
    icmp4_ts_transmit = TransmitTimestamp
    # ARP_HEADER
    # Define the structure of an ARP header.
    # The field names are derived from those in RFC 826.
    _ARP_HEADER._fields_ = [
        ('HardwareAddressSpace', USHORT),
        ('ProtocolAddressSpace', USHORT),
        ('HardwareAddressLength', UCHAR),
        ('ProtocolAddressLength', UCHAR),
        ('Opcode', USHORT),
        ('SenderHardwareAddress', UCHAR * 0),
    ]
    # Opcode values in the ARP header.
    # is the authoritative source of these.        # ENUM ERROR: typedef enum {
    # HardwareAddressSpace values in the ARP header.
    # is the authoritative source of these.        # ENUM ERROR: typedef enum {
    # Types of IGMP messages.
    IGMP_QUERY_TYPE = 0x11
    IGMP_VERSION1_REPORT_TYPE = 0x12
    IGMP_VERSION2_REPORT_TYPE = 0x16
    IGMP_LEAVE_GROUP_TYPE = 0x17
    IGMP_VERSION3_REPORT_TYPE = 0x22
    # IGMP_HEADER
    # Define the structure of an IGMPv1/IGMPv2 header.
    class _Union_8(ctypes.Union):
        pass


    class _Struct_4(ctypes.Structure):
        pass


    _Struct_4._fields_ = [
        ('Type', UINT8, 4),
        ('Version', UINT8, 4),
    ]
    _Union_8._Struct_4 = _Struct_4

    _Union_8._anonymous_ = (
        '_Struct_4',
    )

    _Union_8._fields_ = [
        ('_Struct_4', _Union_8._Struct_4),
        ('VersionType', UINT8),
    ]
    _IGMP_HEADER._Union_8 = _Union_8


    # IGMPv1.
    class _Union_9(ctypes.Union):
        pass


    _Union_9._fields_ = [
        ('Reserved', UINT8),
        # IGMPv2.
        ('MaxRespTime', UINT8),
        # DVMRP.
        ('Code', UINT8),
    ]
    _IGMP_HEADER._Union_9 = _Union_9

    _IGMP_HEADER._anonymous_ = (
        '_Union_8',
        '_Union_9',
    )

    _IGMP_HEADER._fields_ = [
        ('_Union_8', _IGMP_HEADER._Union_8),
        ('_Union_9', _IGMP_HEADER._Union_9),
        ('Checksum', UINT16),
        ('MulticastAddress', IN_ADDR),
    ]
        # ENUM ERROR: typedef enum {
    # IGMPV3_QUERY_HEADER
    # Define the structure of an IGMPv3 query header. The fields names are
    # derived
    # from RFC 3376.
    class _Union_10(ctypes.Union):
        pass


    class _Struct_4(ctypes.Structure):
        pass


    _Struct_4._fields_ = [
        ('MaxRespCodeMantissa', UINT8, 4),
        ('MaxRespCodeExponent', UINT8, 3),
        ('MaxRespCodeType', UINT8, 1),
    ]
    _Union_10._Struct_4 = _Struct_4

    _Union_10._anonymous_ = (
        '_Struct_4',
    )

    _Union_10._fields_ = [
        ('MaxRespCode', UINT8),
        ('_Struct_4', _Union_10._Struct_4),
    ]
    _IGMPV3_QUERY_HEADER._Union_10 = _Union_10


    class _Union_11(ctypes.Union):
        pass


    class _Struct_4(ctypes.Structure):
        pass


    _Struct_4._fields_ = [
        ('QQCMantissa', UINT8, 4),
        ('QQCExponent', UINT8, 3),
        ('QQCType', UINT8, 1),
    ]
    _Union_11._Struct_4 = _Struct_4

    _Union_11._anonymous_ = (
        '_Struct_4',
    )

    _Union_11._fields_ = [
        ('QueriersQueryInterfaceCode', UINT8),
        ('_Struct_4', _Union_11._Struct_4),
    ]
    _IGMPV3_QUERY_HEADER._Union_11 = _Union_11

    _IGMPV3_QUERY_HEADER._anonymous_ = (
        '_Union_10',
        '_Union_11',
    )

    _IGMPV3_QUERY_HEADER._fields_ = [
        ('Type', UINT8),
        ('_Union_10', _IGMPV3_QUERY_HEADER._Union_10),
        ('Checksum', UINT16),
        ('MulticastAddress', IN_ADDR),
        ('QuerierRobustnessVariable', UINT8, 3),
        ('SuppressRouterSideProcessing', UINT8, 1),
        ('Reserved', UINT8, 4),
        ('_Union_11', _IGMPV3_QUERY_HEADER._Union_11),
        ('SourceCount', UINT16),
    ]


    # IGMPV3_REPORT_RECORD_HEADER
    # Defines the structure of the record header within a IGMPv3 report message
    # (RFC 3376).
    _IGMPV3_REPORT_RECORD_HEADER._fields_ = [
        ('Type', UINT8),
        ('AuxillaryDataLength', UINT8),
        ('SourceCount', UINT16),
        ('MulticastAddress', IN_ADDR),
    ]

    # IGMPV3_HEADER
    # Define the structure of an IGMPv3 report message header (RFC 3376).
    _IGMPV3_REPORT_HEADER_._fields_ = [
        ('Type', UINT8),
        ('Reserved', UINT8),
        ('Checksum', UINT16),
        ('Reserved2', UINT16),
        ('RecordCount', UINT16),
    ]
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF


    if defined (_MSC_VER):
        pass
    # END IF


    # IPV6_HEADER
    # The structure for an IPv6 header.
    # RAW socket applications, packetization layer modules, and
    # network-layer services all need access to this structure.
    # 4 bits Version, 8 Traffic Class, 20 Flow Label.
    _IPV6_HEADER._fields_ = [
        ('VersionClassFlow', UINT32),
        # Zero indicates Jumbo Payload hop-by-hop option.
        ('PayloadLength', UINT16),
        # Values are superset of IPv4's Protocol field.
        ('NextHeader', UINT8),
        ('HopLimit', UINT8),
        ('SourceAddress', IN6_ADDR),
        ('DestinationAddress', IN6_ADDR),
    ]

    # Defines for RFC 3542 compatibility.
    ip6_hdr = _IPV6_HEADER
    ip6_flow = VersionClassFlow
    ip6_plen = PayloadLength
    ip6_nxt = NextHeader
    ip6_hops = HopLimit
    ip6_hlim = HopLimit
    ip6_src = SourceAddress
    ip6_dst = DestinationAddress

    # Useful constants for working with various fields in the IPv6 header.
    # NOTE: We keep the Version, Traffic Class and Flow Label fields as a
    # single
    # NOTE: 32 bit value (VersionClassFlow) in network byte order (big-endian).
    # NOTE: Since NT is little-endian, this means all loads/stores to/from this
    # NOTE: field need to be byte swapped.
    IP_VER_MASK = 0xF0    # Version is high 4 bits of VersionClassFlow.


    # RFC 2474 redefines traffic class to the 6 bit DSCP value. RFC 2780 and
    # 3168 redefine the unused 2 bits in the traffic class octet as used by
    # ECN.
    IPV6_TRAFFIC_CLASS_MASK = 0x0000C00F    # 0x0FC00000 (after byte swap).
    IPV6_FULL_TRAFFIC_CLASS_MASK = 0x0000F00F    # 0x0FF00000 (after byte swap).
    IPV6_ECN_MASK = 0x00003000    # 0x00300000 (after byte swap).
    IPV6_FLOW_LABEL_MASK = 0xFFFF0F00    # 0x000FFFFF (after byte swap).
    MAX_IPV6_PAYLOAD = 65535
    MAX_IPV6_PACKET = MAX_IPV6_PAYLOAD + (ctypes.sizeof(IPV6_HEADER)
    IPV6_ECN_SHIFT = 12    # Bits to shift to recover ECN field.
    IPV6_MINIMUM_MTU = 1280
    IPV6_MINIMUM_ULMTU = IPV6_MINIMUM_MTU - (ctypes.sizeof(IPV6_HEADER)
    def IPV6_TRAFFIC_CLASS(VersionClassFlow):
        return (UCHAR(((VersionClassFlow & IPV6_TRAFFIC_CLASS_MASK) >> 12) + ((VersionClassFlow & IPV6_TRAFFIC_CLASS_MASK) << 4)))
    def IPV6_FULL_TRAFFIC_CLASS(VersionClassFlow):
        return (UCHAR(((VersionClassFlow & IPV6_FULL_TRAFFIC_CLASS_MASK) >> 12) + ((VersionClassFlow & IPV6_FULL_TRAFFIC_CLASS_MASK) << 4)))
    # IPV6_FRAGMENT_HEADER
    # The structure for an IPv6 Fragment Header.
    # RAW socket applications and network-layer services all need
    # access to this structure.
    # Next Header.
    class _Union_12(ctypes.Union):
        pass


    class _Struct_4(ctypes.Structure):
        pass


    _Struct_4._fields_ = [
        ('DontUse1', UINT16, 8),
        # Least significant bit.
        ('MoreFragments', UINT16, 1),
        ('ReservedBits', UINT16, 2),
        ('DontUse2', UINT16, 5),
    ]
    _Union_12._Struct_4 = _Struct_4

    _Union_12._anonymous_ = (
        '_Struct_4',
    )

    _Union_12._fields_ = [
        ('_Struct_4', _Union_12._Struct_4),
        ('OffsetAndFlags', UINT16),
    ]
    _IPV6_FRAGMENT_HEADER._Union_12 = _Union_12

    _IPV6_FRAGMENT_HEADER._anonymous_ = (
        '_Union_12',
    )

    _IPV6_FRAGMENT_HEADER._fields_ = [
        ('NextHeader', UINT8),
        # Reserved field.
        ('Reserved', UINT8),
        ('_Union_12', _IPV6_FRAGMENT_HEADER._Union_12),
        # Identification.
        ('Id', UINT32),
    ]

    # Defines for RFC 3542 compatibility.
    ip6_frag = _IPV6_FRAGMENT_HEADER
    ip6f_nxt = NextHeader
    ip6f_reserved = Reserved
    ip6f_offlg = OffsetAndFlags
    ip6f_ident = Id

    # Useful constants from RFC 3542 for working with the ip6f_offlg field.
    # These are in network byte order.
    IP6F_OFF_MASK = 0xF8FF    # Mask out offset from _offlg.
    IP6F_RESERVED_MASK = 0x0600    # Reserved bits in ip6f_offlg.
    IP6F_MORE_FRAG = 0x0100    # More-fragments flag.
    if defined(_NTDDK_) or defined(_NTRTL_):
        # Only include this definition if RtlUshortByteSwap is defined.
        ntoskrnl = ctypes.windll.NTOSKRNL


        # __inline
        # UINT16
        # Ip6FragmentOffset(
        # _In_ CONST UNALIGNED IPV6_FRAGMENT_HEADER *Header
        # )
        # {
        # return RtlUshortByteSwap(Header.OffsetAndFlags & IP6F_OFF_MASK);
        RtlUshortByteSwap = ntoskrnl.RtlUshortByteSwap
        RtlUshortByteSwap.restype = {
    # END IF
    # IPV6_EXTENSION_HEADER
    # Next header.
    _IPV6_EXTENSION_HEADER._fields_ = [
        ('NextHeader', UINT8),
        # In 8-byte units, not counting first 8.
        ('Length', UINT8),
    ]
    EXT_LEN_UNIT = 8    # 8-byte units used for extension hdr length.
    def IPV6_EXTENSION_HEADER_LENGTH(Blocks):
        return ((Blocks + 1) * EXT_LEN_UNIT)
    MAX_IPV6_EXTENSION_HEADER_LENGTH = IPV6_EXTENSION_HEADER_LENGTH(0xFF)
    def IPV6_EXTENSION_HEADER_BLOCKS(Length):
        return Length / EXT_LEN_UNIT - 1
    def IP_AUTHENTICATION_HEADER_LENGTH(Blocks):
        return ((Blocks + 2) * 4)
    def IP_AUTHENTICATION_HEADER_BLOCKS(Length):
    # DEFINE ERROR 4: #define IP_AUTHENTICATION_HEADER_BLOCKS(Length) (((Length + (ctypes.sizeof(AUTHENTICATION_HEADER)) / 4) - 2)
        pass
    IPV6_ROUTER_ALERT_LENGTH = IPV6_EXTENSION_HEADER_LENGTH(0)
    # Defines for RFC 3542 compatibility.
    ip6_hbh = _IPV6_EXTENSION_HEADER
    ip6h_nxt = NextHeader
    ip6h_len = Length
    ip6_dest = _IPV6_EXTENSION_HEADER
    ip6d_nxt = NextHeader
    ip6d_len = Length
    # IPV6_OPTION_HEADER
    _IPV6_OPTION_HEADER._fields_ = [
        ('Type', UINT8),
        # In bytes, not counting two for the header.
        ('DataLength', UINT8),
    ]
        # ENUM ERROR: typedef enum {
    def IP6OPT_TYPE(Type):
        return Type & 0xC0
    IP6OPT_TYPE_SKIP = 0x00
    IP6OPT_TYPE_DISCARD = 0x40
    IP6OPT_TYPE_FORCEICMP = 0x80
    IP6OPT_TYPE_ICMP = 0xC0
    IP6OPT_MUTABLE = 0x20
    def IP6OPT_ISMUTABLE(Type):
        return ((Type & IP6OPT_MUTABLE) != 0)
    _IPV6_OPTION_JUMBOGRAM._fields_ = [
        ('Header', IPV6_OPTION_HEADER),
        ('JumbogramLength', UINT8 * 4),
    ]
    ip6_opt_jumbo = _IPV6_OPTION_JUMBOGRAM
    ip6oj_type = Header.Type
    ip6oj_len = Header.DataLength
    ip6oj_jumbo_len = JumbogramLength
    _IPV6_OPTION_ROUTER_ALERT._fields_ = [
        ('Header', IPV6_OPTION_HEADER),
        ('Value', UINT8 * 2),
    ]
    ip6_opt_router = _IPV6_OPTION_ROUTER_ALERT
    ip6or_type = Header.Type
    ip6or_len = Header.DataLength
    ip6or_value = Value
    SIZEOF_IPV6_ROUTERALERT = IPV6_EXTENSION_HEADER_LENGTH(0)
    # typedef _Struct_size_bytes_(_Inexpressible_(Length)) struct _IPV6_ROUTING_HEADER {
    # UCHAR NextHeader;
    _Inexpressible_(Length = CALLBACK(
        _Struct_size_bytes_,
        UCHAR,
    )
    # In 8-byte units, not counting first 8.    # Number of nodes still left to be visited.    # Not a u_int to avoid alignment.
    # Defines for RFC 3542 compatibility.
    ip6_rthdr = _IPV6_ROUTING_HEADER
    ip6r_nxt = NextHeader
    ip6r_len = Length
    ip6r_type = RoutingType
    ip6r_segleft = SegmentsLeft
    # ICMPV6_HEADER
    # struct icmp6_hdr is the RFC 3542 structure for an ICMPv6 header.
    # RAW socket applications and network-layer services all need
    # access to this structure.
    ICMPV6_HEADER = ICMP_HEADER
    PICMPV6_HEADER = POINTER(ICMP_HEADER)
    ICMPV6_MESSAGE = ICMP_MESSAGE
    PICMPV6_MESSAGE = POINTER(ICMP_MESSAGE)
    # Defines for RFC 3542 compatibility.
    icmp6_hdr = _ICMPV6_MESSAGE
    icmp6_type = Header.Type
    icmp6_code = Header.Code
    icmp6_cksum = Header.Checksum
    icmp6_un_data32 = Data32
    icmp6_un_data16 = Data16
    icmp6_un_data8 = Data8
    icmp6_dataun = Data
    icmp6_data32 = icmp6_dataun.icmp6_un_data32
    icmp6_data16 = icmp6_dataun.icmp6_un_data16
    icmp6_data8 = icmp6_dataun.icmp6_un_data8
    icmp6_pptr = icmp6_data32[0]    # Parameter problem.
    icmp6_mtu = icmp6_data32[0]    # Packet too big.
    icmp6_id = icmp6_data16[0]    # Echo request/reply.
    icmp6_seq = icmp6_data16[1]    # Echo request/reply.
    icmp6_maxdelay = icmp6_data16[0]    # Multicast group membership.
    ICMP6_INFOMSG_MASK = 0x80    # All informational messages.
    ICMP6_DST_UNREACH_NOROUTE = 0    # No route to destination.
    ICMP6_DST_UNREACH_ADMIN = 1    # Communication with destination
    # administratively prohibited.
    ICMP6_DST_UNREACH_BEYONDSCOPE = 2    # Beyond scope of source address.
    ICMP6_DST_UNREACH_ADDR = 3    # Address unreachable.
    ICMP6_DST_UNREACH_NOPORT = 4    # Bad port.
    ICMP6_TIME_EXCEED_TRANSIT = 0    # Hop Limit == 0 in transit.
    ICMP6_TIME_EXCEED_REASSEMBLY = 1    # Reassembly time out.
    ICMP6_PARAMPROB_HEADER = 0    # Erroneous header field.
    ICMP6_PARAMPROB_NEXTHEADER = 1    # Unrecognized Next Header.
    ICMP6_PARAMPROB_OPTION = 2    # Unrecognized IPv6 option.
    ICMPV6_ECHO_REQUEST_FLAG_REVERSE = 0x1
    # ND_ROUTER_SOLICIT_HEADER
    # Define a structure for an IPv6 Router Solicitation header.
    nd_router_solicit._fields_ = [
        ('nd_rs_hdr', ICMPV6_MESSAGE),
    ]
    nd_rs_type = nd_rs_hdr.icmp6_type
    nd_rs_code = nd_rs_hdr.icmp6_code
    nd_rs_cksum = nd_rs_hdr.icmp6_cksum
    nd_rs_reserved = nd_rs_hdr.icmp6_data32[0]
    # ND_ROUTER_ADVERT_HEADER
    # Define a structure for an IPv6 Router Advertisement header.
    nd_router_advert._fields_ = [
        ('nd_ra_hdr', ICMPV6_MESSAGE),
        # Reachable Time.
        ('nd_ra_reachable', UINT32),
        # Retransmit Timer.
        ('nd_ra_retransmit', UINT32),
    ]
    nd_ra_type = nd_ra_hdr.icmp6_type
    nd_ra_code = nd_ra_hdr.icmp6_code
    nd_ra_cksum = nd_ra_hdr.icmp6_cksum
    nd_ra_curhoplimit = nd_ra_hdr.icmp6_data8[0]
    nd_ra_flags_reserved = nd_ra_hdr.icmp6_data8[1]
    ND_RA_FLAG_MANAGED = 0x80
    ND_RA_FLAG_OTHER = 0x40
    ND_RA_FLAG_HOME_AGENT = 0x20
    ND_RA_FLAG_PREFERENCE = 0x18
    nd_ra_router_lifetime = nd_ra_hdr.icmp6_data16[1]
    # IPV6_ROUTER_ADVERTISEMENT_FLAGS
    # Define flags included in an IPv6 Router Advertisement message.
    # Least significant bits.
    class _Struct_4(ctypes.Structure):
        pass


    _Struct_4._fields_ = [
        ('Reserved', UINT8, 3),
        ('Preference', UINT8, 2),
        ('HomeAgent', UINT8, 1),
        ('OtherStatefulConfiguration', UINT8, 1),
        ('ManagedAddressConfiguration', UINT8, 1),
    ]
    _IPV6_ROUTER_ADVERTISEMENT_FLAGS._Struct_4 = _Struct_4

    _IPV6_ROUTER_ADVERTISEMENT_FLAGS._anonymous_ = (
        '_Struct_4',
    )

    _IPV6_ROUTER_ADVERTISEMENT_FLAGS._fields_ = [
        ('_Struct_4', _IPV6_ROUTER_ADVERTISEMENT_FLAGS._Struct_4),
        ('Value', UINT8),
    ]

    # ND_NEIGHBOR_SOLICIT_HEADER
    # Define a structure for an IPv6 Neighbor Solicitation header.
    nd_neighbor_solicit._fields_ = [
        ('nd_ns_hdr', ICMPV6_MESSAGE),
        # Target Address.
        ('nd_ns_target', IN6_ADDR),
    ]
    nd_ns_type = nd_ns_hdr.icmp6_type
    nd_ns_code = nd_ns_hdr.icmp6_code
    nd_ns_cksum = nd_ns_hdr.icmp6_cksum
    nd_ns_reserved = nd_ns_hdr.icmp6_data32[0]


    # ND_NEIGHBOR_ADVERT_HEADER
    # Define a structure for an IPv6 Neighbor Advertisement header.
    nd_neighbor_advert._fields_ = [
        ('nd_na_hdr', ICMPV6_MESSAGE),
        # Target Address.
        ('nd_na_target', IN6_ADDR),
    ]
    nd_na_type = nd_na_hdr.icmp6_type
    nd_na_code = nd_na_hdr.icmp6_code
    nd_na_cksum = nd_na_hdr.icmp6_cksum
    nd_na_flags_reserved = nd_na_hdr.icmp6_data32[0]
    if BYTE_ORDER == _BIG_ENDIAN:
        ND_NA_FLAG_ROUTER = 0x80000000
        ND_NA_FLAG_SOLICITED = 0x40000000
        ND_NA_FLAG_OVERRIDE = 0x20000000
    else:
        ND_NA_FLAG_ROUTER = 0x00000080
        ND_NA_FLAG_SOLICITED = 0x00000040
        ND_NA_FLAG_OVERRIDE = 0x00000020
    # END IF


    # IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS
    # Define flags included in an IPv6 Neighbor Advertisement message.
    # Least significant bits.
    class _Struct_5(ctypes.Structure):
        pass


    _Struct_5._fields_ = [
        ('Reserved1', UINT8, 5),
        ('Override', UINT8, 1),
        ('Solicited', UINT8, 1),
        ('Router', UINT8, 1),
        ('Reserved2', UINT8 * 3),
    ]
    _IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS._Struct_5 = _Struct_5

    _IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS._anonymous_ = (
        '_Struct_5',
    )

    _IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS._fields_ = [
        ('_Struct_5', _IPV6_NEIGHBOR_ADVERTISEMENT_FLAGS._Struct_5),
        ('Value', UINT32),
    ]


    # ND_REDIRECT_HEADER
    # Define a structure for an IPv6 Router Redirect header.
    nd_redirect._fields_ = [
        ('nd_rd_hdr', ICMPV6_MESSAGE),
        # Target Address.
        ('nd_rd_target', IN6_ADDR),
        # Destination Address.
        ('nd_rd_dst', IN6_ADDR),
    ]
    nd_rd_type = nd_rd_hdr.icmp6_type
    nd_rd_code = nd_rd_hdr.icmp6_code
    nd_rd_cksum = nd_rd_hdr.icmp6_cksum
    nd_rd_reserved = nd_rd_hdr.icmp6_data32[0]

    # ND_OPTION_HDR
    # Define a structure for neighbor discovery option header.
    nd_opt_hdr._fields_ = [
        ('nd_opt_type', UINT8),
        # In units of 8 octets.
        ('nd_opt_len', UINT8),
    ]


    # ND_OPTION_TYPE
    # Define values for neighbor discovery option type.
        # ENUM ERROR: typedef enum {
    # ND_OPTION_PREFIX_INFO
    # Define a structure for a Prefix Information option.
    class _Union_13(ctypes.Union):
        pass

    # Least significant bit.
    class Flags(ctypes.Structure):
        pass


    Flags._fields_ = [
        ('Route', UINT8, 1),
        ('Reserved1', UINT8, 3),
        ('SitePrefix', UINT8, 1),
        ('RouterAddress', UINT8, 1),
        ('Autonomous', UINT8, 1),
        ('OnLink', UINT8, 1),
    ]
    _Union_13.Flags = Flags


    _Union_13._fields_ = [
        ('nd_opt_pi_flags_reserved', UINT8),
        ('Flags', _Union_13.Flags),
    ]
    nd_opt_prefix_info._Union_13 = _Union_13


    class _Union_14(ctypes.Union):
        pass


    class _Struct_6(ctypes.Structure):
        pass


    _Struct_6._fields_ = [
        ('nd_opt_pi_reserved3', UINT8 * 3),
        ('nd_opt_pi_site_prefix_len', UINT8),
    ]
    _Union_14._Struct_6 = _Struct_6

    _Union_14._anonymous_ = (
        '_Struct_6',
    )

    _Union_14._fields_ = [
        ('nd_opt_pi_reserved2', UINT32),
        ('_Struct_6', _Union_14._Struct_6),
    ]
    nd_opt_prefix_info._Union_14 = _Union_14

    nd_opt_prefix_info._anonymous_ = (
        '_Union_13',
        '_Union_14',
    )

    nd_opt_prefix_info._fields_ = [
        ('nd_opt_pi_type', UINT8),
        ('nd_opt_pi_len', UINT8),
        ('nd_opt_pi_prefix_len', UINT8),
        ('_Union_13', nd_opt_prefix_info._Union_13),
        ('nd_opt_pi_valid_time', UINT32),
        ('nd_opt_pi_preferred_time', UINT32),
        ('_Union_14', nd_opt_prefix_info._Union_14),
        ('nd_opt_pi_prefix', IN6_ADDR),
    ]
    ND_OPT_PI_FLAG_ONLINK = 0x80
    ND_OPT_PI_FLAG_AUTO = 0x40
    ND_OPT_PI_FLAG_ROUTER_ADDR = 0x20
    ND_OPT_PI_FLAG_SITE_PREFIX = 0x10
    ND_OPT_PI_FLAG_ROUTE = 0x01


    # ND_OPTION_RD_HDR
    # Define a structure for a Redirected Header option.
    nd_opt_rd_hdr._fields_ = [
        ('nd_opt_rh_type', UINT8),
        ('nd_opt_rh_len', UINT8),
        ('nd_opt_rh_reserved1', UINT16),
        ('nd_opt_rh_reserved2', UINT32),
    ]

    # ND_OPTION_MTU
    # Define a structure for an MTU option.
    nd_opt_mtu._fields_ = [
        ('nd_opt_mtu_type', UINT8),
        ('nd_opt_mtu_len', UINT8),
        ('nd_opt_mtu_reserved', UINT16),
        ('nd_opt_mtu_mtu', UINT32),
    ]


    # ND_OPTION_ROUTE_INFO
    # Define a structure for a Route Information option.
    # If PrefixLength is zero, then the Prefix field may be 0 bytes.
    # If PrefixLength is <= 64, then the Prefix field may be 8 bytes.
    # Otherwise the Prefix field is a full 16 bytes.
    class _Union_15(ctypes.Union):
        pass

    # Least significant bits.
    class Flags(ctypes.Structure):
        pass


    Flags._fields_ = [
        ('Reserved', UINT8, 3),
        ('Preference', UINT8, 2),
    ]
    _Union_15.Flags = Flags


    _Union_15._fields_ = [
        ('nd_opt_ri_flags_reserved', UINT8),
        ('Flags', _Union_15.Flags),
    ]
    nd_opt_route_info._Union_15 = _Union_15

    nd_opt_route_info._anonymous_ = (
        '_Union_15',
    )

    nd_opt_route_info._fields_ = [
        ('nd_opt_ri_type', UINT8),
        ('nd_opt_ri_len', UINT8),
        ('nd_opt_ri_prefix_len', UINT8),
        ('_Union_15', nd_opt_route_info._Union_15),
        ('nd_opt_ri_route_lifetime', UINT32),
        ('nd_opt_ri_prefix', IN6_ADDR),
    ]
    ND_OPT_RI_FLAG_PREFERENCE = 0x18


    # ND_OPTION_RDNSS
    # Define a structure for a RDNSS option.
    nd_opt_rdnss._fields_ = [
        ('nd_opt_rdnss_type', UINT8),
        ('nd_opt_rdnss_len', UINT8),
        ('nd_opt_rdnss_reserved', UINT16),
        ('nd_opt_rdnss_lifetime', UINT32),
    ]

    # Minimum length in bytes of the RDNSS option if there is
    # atleast one IPv6 address (3 * 8 = 24 octets).
    ND_OPT_RDNSS_MIN_LEN = 24

    # ND_OPTION_DNSSL
    # Define a structure for a DNSSL option.
    nd_opt_dnssl._fields_ = [
        ('nd_opt_dnssl_type', UINT8),
        ('nd_opt_dnssl_len', UINT8),
        ('nd_opt_dnssl_reserved', UINT16),
        ('nd_opt_dnssl_lifetime', UINT32),
    ]


    # Minimum length in bytes of the DNSSL option if there is
    # atleast one suffix (2 * 8 = 16 octets).
    ND_OPT_DNSSL_MIN_LEN = 16


    # MLD_HEADER.
    # Defines the structure of the MLD (version 1) header.
    _MLD_HEADER._fields_ = [
        ('IcmpHeader', ICMPV6_HEADER),
        ('MaxRespTime', UINT16),
        ('Reserved', UINT16),
        ('MulticastAddress', IN6_ADDR),
    ]
    mld_type = IcmpHeader.Type
    mld_checksum = IcmpHeader.Checksum

        # ENUM ERROR: typedef enum {
    # MLDV2_QUERY_HEADER.
    # Defines the structure of MLDv2 query header.
    class _Union_16(ctypes.Union):
        pass


    class _Struct_6(ctypes.Structure):
        pass


    _Struct_6._fields_ = [
        ('MaxRespCodeMantissaHi', UINT16, 4),
        ('MaxRespCodeExponent', UINT16, 3),
        ('MaxRespCodeType', UINT16, 1),
        ('MaxRespCodeMantissaLo', UINT16, 8),
    ]
    _Union_16._Struct_6 = _Struct_6

    _Union_16._anonymous_ = (
        '_Struct_6',
    )

    _Union_16._fields_ = [
        ('MaxRespCode', UINT16),
        ('_Struct_6', _Union_16._Struct_6),
    ]
    _MLDV2_QUERY_HEADER._Union_16 = _Union_16


    class _Union_17(ctypes.Union):
        pass


    class _Struct_6(ctypes.Structure):
        pass


    _Struct_6._fields_ = [
        ('QQCMantissa', UINT8, 4),
        ('QQCExponent', UINT8, 3),
        ('QQCType', UINT8, 1),
    ]
    _Union_17._Struct_6 = _Struct_6

    _Union_17._anonymous_ = (
        '_Struct_6',
    )

    _Union_17._fields_ = [
        ('QueriersQueryInterfaceCode', UINT8),
        ('_Struct_6', _Union_17._Struct_6),
    ]
    _MLDV2_QUERY_HEADER._Union_17 = _Union_17

    _MLDV2_QUERY_HEADER._anonymous_ = (
        '_Union_16',
        '_Union_17',
    )

    _MLDV2_QUERY_HEADER._fields_ = [
        ('IcmpHeader', ICMPV6_HEADER),
        ('_Union_16', _MLDV2_QUERY_HEADER._Union_16),
        ('Reserved', UINT16),
        ('MulticastAddress', IN6_ADDR),
        ('QuerierRobustnessVariable', UINT8, 3),
        ('SuppressRouterSideProcessing', UINT8, 1),
        ('QueryReserved', UINT8, 4),
        ('_Union_17', _MLDV2_QUERY_HEADER._Union_17),
        ('SourceCount', UINT16),
    ]


    # MLDV2_REPORT_RECORD_HEADER.
    # Defines the structure of the MLDv2 record header contained in a MLDv2
    # report. There can be multiple record headers in a single MLDv2 report.
    _MLDV2_REPORT_RECORD_HEADER._fields_ = [
        ('Type', UINT8),
        ('AuxillaryDataLength', UINT8),
        ('SourceCount', UINT16),
        ('MulticastAddress', IN6_ADDR),
    ]

    # MLDV2_REPORT_HEADER.
    # Defines the structure of a MLDv2 report.
    _MLDV2_REPORT_HEADER._fields_ = [
        ('IcmpHeader', ICMPV6_HEADER),
        ('Reserved', UINT16),
        ('RecordCount', UINT16),
    ]

    if defined(_NTDDK_) or defined(_NTRTL_):
        # IPv6 Version, Traffic Class, ECN Field and Flow Label fields in host
        # byte order.
        class _Struct_6(ctypes.Structure):
            pass


        _Struct_6._fields_ = [
            ('Flow', UINT32, 20),
            ('EcnField', UINT32, 2),
            ('Class', UINT32, 6),
            # Most significant bits.
            ('Version', UINT32, 4),
        ]
        ._Struct_6 = _Struct_6


        # If LSBs (20 bits) of Flow are all 0s, use its MSBs.    # END IF
    # Shared definitions for NAT64 / DNS64
    IN6_EMBEDDEDV4_UOCTET_POSITION = 8
    IN6_EMBEDDEDV4_BITS_IN_BYTE = 8


    # Checks per draft-ietf-behave-address-format-06.
    ntdll = ctypes.windll.NTDLL


    # }
    # 
    # if (PrefixLength < 96) {
    # RtlCopyMemory(
    # & TmpAddress,
    # Ipv6Address,
    # (ctypes.sizeof(IN6_ADDR));
    RtlCopyMemory = ntdll.RtlCopyMemory
    RtlCopyMemory.restype = 96)


    # } else {
    # RtlCopyMemory(
    # Ipv4Address,
    # (((PUCHAR) Ipv6Address) + PrefixLength / IN6_EMBEDDEDV4_BITS_IN_BYTE),
    # (ctypes.sizeof(IN_ADDR));
    RtlCopyMemory = ntdll.RtlCopyMemory
    RtlCopyMemory.restype = else
    # if (PrefixLength < 96) {
    # RtlZeroMemory(
    # (((PUCHAR)Ipv6Address) + PrefixByteLength + (ctypes.sizeof(IN_ADDR)),
    # (ctypes.sizeof(IN6_ADDR) - (PrefixByteLength + (ctypes.sizeof(IN_ADDR)));
    RtlZeroMemory = ntdll.RtlZeroMemory
    RtlZeroMemory.restype = 96)
    # SEQ_NUM
    # Define a type for TCP sequence numbers.
    SEQ_NUM = UINT32
    PSEQ_NUM = POINTER(UINT32)
    # TCP_HDR
    # Define the structure of a TCP header.
    # $REVIEW: We shouldn't have two different structures for representing
    # a TCP header. Can we get rid of this one?
    tcp_hdr._fields_ = [
        ('th_sport', UINT16),
        ('th_dport', UINT16),
        ('th_seq', SEQ_NUM),
        ('th_ack', SEQ_NUM),
        ('th_x2', UINT8, 4),
        ('th_len', UINT8, 4),
        ('th_flags', UINT8),
        ('th_win', UINT16),
        ('th_sum', UINT16),
        ('th_urp', UINT16),
    ]
    UNALIGNED *PTCP_HDR = TCP_HDR
else:
    pass
# END IF


# Define the maximum length of a TCP header with options.
TH_MAX_LEN = 0x0F << 2

# Define the bits in TCP_HDR.th_flags.
TH_FIN = 0x01
TH_SYN = 0x02
TH_RST = 0x04
TH_PSH = 0x08
TH_ACK = 0x10
TH_URG = 0x20
TH_ECE = 0x40
TH_CWR = 0x80
TH_ALL = TH_FIN | TH_SYN | TH_RST | TH_PSH | TH_ACK | TH_URG | TH_ECE | TH_CWR
TH_SYN_ALL = TH_FIN | TH_SYN | TH_RST | TH_ACK

# Define the options appearing in a TCP header.
TH_OPT_EOL = 0x00
TH_OPT_NOP = 0x01
TH_OPT_MSS = 0x02
TH_OPT_WS = 0x03
TH_OPT_SACK_PERMITTED = 0x04
TH_OPT_SACK = 0x05
TH_OPT_TS = 0x08
TH_OPT_FASTOPEN = 0x22

# TCP_OPT_MSS
tcp_opt_mss._fields_ = [
    ('Kind', UINT8),
    ('Length', UINT8),
    ('Mss', UINT16),
]

# TCP_OPT_WS
tcp_opt_ws._fields_ = [
    ('Kind', UINT8),
    ('Length', UINT8),
    ('ShiftCnt', UINT8),
]

# TCP_OPT_SACK_PERMITTED
tcp_opt_sack_permitted._fields_ = [
    ('Kind', UINT8),
    ('Length', UINT8),
]

# TCP_OPT_SACK
class tcp_opt_sack_block(ctypes.Structure):
    pass


tcp_opt_sack_block._fields_ = [
    ('Left', SEQ_NUM),
    ('Right', SEQ_NUM),
]
Block = tcp_opt_sack_block
tcp_opt_sack.Block = Block


tcp_opt_sack._fields_ = [
    ('Kind', UINT8),
    ('Length', UINT8),
    ('Block', tcp_opt_sack.Block * 0),
]

# TCP_OPT_TS
tcp_opt_ts._fields_ = [
    ('Kind', UINT8),
    ('Length', UINT8),
    ('Val', UINT32),
    ('EcR', UINT32),
]

# TCP_OPT_UNKNOWN
tcp_opt_unknown._fields_ = [
    ('Kind', UINT8),
    ('Length', UINT8),
]

# TCP_OPT_FASTOPEN
# A fastopen cookie can be zero bytes (for a request) or 4 to 16 bytes.
tcp_opt_fastopen._fields_ = [
    ('Kind', UINT8),
    ('Length', UINT8),
    ('Cookie', UINT8 * 0),
]
from ifdef_h import * # NOQA
    if _MSC_VER >= 1200:
        pass
    # END IF


if defined(_MSC_VER):
    pass
# END IF   defined(_MSC_VER)


# DL_TUNNEL_ADDRESS
# Define IP in IP tunnel datalink address.
DL_TUNNEL_ADDRESS._fields_ = [
    ('CompartmentId', COMPARTMENT_ID),
    ('ScopeId', SCOPE_ID),
    ('IpAddress', UCHAR * 0),
]


def DL_SIZEOF_TUNNEL_ADDRESS(AddressBytes):
    return FIELD_OFFSETDL_TUNNEL_ADDRESS, IpAddress + AddressBytes
DL_SIZEOF_IPV4_TUNNEL_ADDRESS = (
    DL_SIZEOF_TUNNEL_ADDRESS((ctypes.sizeof(IN_ADDR))
)
DL_SIZEOF_IPV6_TUNNEL_ADDRESS = (
    DL_SIZEOF_TUNNEL_ADDRESS((ctypes.sizeof(IN6_ADDR))
)
# Tunnel sub-type used to differentiate different tunnel
# technologies when the tunnel-type is TUNNEL_TYPE_OTHER
    # ENUM ERROR: typedef enum _TUNNEL_SUB_TYPE {
# DL_TEREDO_ADDRESS
# Define Teredo tunnel datalink address.
class _Union_18(ctypes.Union):
    pass


class _Struct_7(ctypes.Structure):
    pass


_Struct_7._fields_ = [
    ('Flags', USHORT),
    ('MappedPort', USHORT),
    ('MappedAddress', IN_ADDR),
]
_Union_18._Struct_7 = _Struct_7

_Union_18._anonymous_ = (
    '_Struct_7',
)

_Union_18._fields_ = [
    ('Eui64', DL_EUI64),
    ('_Struct_7', _Union_18._Struct_7),
]
DL_TEREDO_ADDRESS._Union_18 = _Union_18

DL_TEREDO_ADDRESS._anonymous_ = (
    '_Union_18',
)

DL_TEREDO_ADDRESS._fields_ = [
    ('Reserved', UINT8 * 6),
    ('_Union_18', DL_TEREDO_ADDRESS._Union_18),
]


class _Union_19(ctypes.Union):
    pass


class _Struct_7(ctypes.Structure):
    pass


_Struct_7._fields_ = [
    ('Flags', USHORT),
    ('MappedPort', USHORT),
    ('MappedAddress', IN_ADDR),
    # FL shunt
    ('LocalAddress', IN_ADDR),
    ('InterfaceIndex', IF_INDEX),
    ('LocalPort', USHORT),
    ('DlDestination', DL_EUI48),
]
_Union_19._Struct_7 = _Struct_7

_Union_19._anonymous_ = (
    '_Struct_7',
)

_Union_19._fields_ = [
    ('Eui64', DL_EUI64),
    ('_Struct_7', _Union_19._Struct_7),
]
DL_TEREDO_ADDRESS_PRV._Union_19 = _Union_19

DL_TEREDO_ADDRESS_PRV._anonymous_ = (
    '_Union_19',
)

DL_TEREDO_ADDRESS_PRV._fields_ = [
    ('Reserved', UINT8 * 6),
    ('_Union_19', DL_TEREDO_ADDRESS_PRV._Union_19),
]

_IPTLS_METADATA._fields_ = [
    ('SequenceNumber', ULONGLONG),
]
from ifdef_h import * # NOQA
    # ENUM ERROR: typedef enum _NPI_MODULEID_TYPE {
# Network Module Identifier.
# This type is persistable.
class _Union_20(ctypes.Union):
    pass

_TEMP__Union_20 = [
]
# END IF


_TEMP__Union_20 += [
    # Valid for MIT_GUID
    ('Guid', GUID),
    # TODO: NET_IFLUID is not an "RPC'able" define yet.
    ('IfLuid', LUID),
]
_Union_20._fields_ = _TEMP__Union_20
_NPI_MODULEID._Union_20 = _Union_20

_NPI_MODULEID._anonymous_ = (
    '_Union_20',
)

_TEMP__NPI_MODULEID = [
    ('Length', USHORT),
    ('Type', NPI_MODULEID_TYPE),
]
# END IF


_TEMP__NPI_MODULEID += [
    ('_Union_20', _NPI_MODULEID._Union_20),
]
_NPI_MODULEID._fields_ = _TEMP__NPI_MODULEID
NPI_MODULEID *PNPI_MODULEID = CONST
    if defined(__cplusplus):
        pass
    else:
        pass
    # END IF


if not defined(__midl):
    pass
# END IF


# Network Programming Interface Identifier: an immutable, globally
# unique identifier for the programming interface.
NPIID = GUID
NPIID *PNPIID = CONST


# "Requested Packet Filter" Bits.
FL_PACKET_TYPE_FLAGS = (
    NDIS_PACKET_TYPE_ALL_MULTICAST | 
    NDIS_PACKET_TYPE_PROMISCUOUS
)


# TODO: remove this.
    # ENUM ERROR: typedef enum {
if defined(NETIODEF_DEFINED_ASSERT):
    # ASSERT wasn't defined before, so undefine it now to restore the original
    # state.# END IF
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if defined(__cplusplus):
    pass
# END IF

# END IF   _NETIODEF_


