import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_WS2IPDEF_ = None
_PREFAST_ = None
WS2IPDEF_ASSERT = None

class sockaddr_in6_old(ctypes.Structure):
    pass





class sockaddr_gen(ctypes.Union):
    pass





class _INTERFACE_INFO(ctypes.Structure):
    pass


INTERFACE_INFO = _INTERFACE_INFO
LPINTERFACE_INFO = POINTER(_INTERFACE_INFO)


class _INTERFACE_INFO_EX(ctypes.Structure):
    pass


INTERFACE_INFO_EX = _INTERFACE_INFO_EX
LPINTERFACE_INFO_EX = POINTER(_INTERFACE_INFO_EX)


class sockaddr_in6(ctypes.Structure):
    pass


SOCKADDR_IN6_LH = sockaddr_in6
PSOCKADDR_IN6_LH = POINTER(sockaddr_in6)
LPSOCKADDR_IN6_LH = POINTER(sockaddr_in6)


class sockaddr_in6_w2ksp1(ctypes.Structure):
    pass


SOCKADDR_IN6_W2KSP1 = sockaddr_in6_w2ksp1
PSOCKADDR_IN6_W2KSP1 = POINTER(sockaddr_in6_w2ksp1)
LPSOCKADDR_IN6_W2KSP1 = POINTER(sockaddr_in6_w2ksp1)


class _SOCKADDR_INET(ctypes.Union):
    pass


SOCKADDR_INET = _SOCKADDR_INET
PSOCKADDR_INET = POINTER(_SOCKADDR_INET)


class _sockaddr_in6_pair(ctypes.Structure):
    pass


SOCKADDR_IN6_PAIR = _sockaddr_in6_pair
PSOCKADDR_IN6_PAIR = POINTER(_sockaddr_in6_pair)


class ip_mreq(ctypes.Structure):
    pass


IP_MREQ = ip_mreq
PIP_MREQ = POINTER(ip_mreq)


class ip_mreq_source(ctypes.Structure):
    pass


IP_MREQ_SOURCE = ip_mreq_source
PIP_MREQ_SOURCE = POINTER(ip_mreq_source)


class ip_msfilter(ctypes.Structure):
    pass


IP_MSFILTER = ip_msfilter
PIP_MSFILTER = POINTER(ip_msfilter)


class ipv6_mreq(ctypes.Structure):
    pass


IPV6_MREQ = ipv6_mreq
PIPV6_MREQ = POINTER(ipv6_mreq)


class group_req(ctypes.Structure):
    pass


GROUP_REQ = group_req
PGROUP_REQ = POINTER(group_req)


class group_source_req(ctypes.Structure):
    pass


GROUP_SOURCE_REQ = group_source_req
PGROUP_SOURCE_REQ = POINTER(group_source_req)


class group_filter(ctypes.Structure):
    pass


GROUP_FILTER = group_filter
PGROUP_FILTER = POINTER(group_filter)


class in_pktinfo(ctypes.Structure):
    pass


IN_PKTINFO = in_pktinfo
PIN_PKTINFO = POINTER(in_pktinfo)


class in6_pktinfo(ctypes.Structure):
    pass


IN6_PKTINFO = in6_pktinfo
PIN6_PKTINFO = POINTER(in6_pktinfo)


class in_pktinfo_ex(ctypes.Structure):
    pass


IN_PKTINFO_EX = in_pktinfo_ex
PIN_PKTINFO_EX = POINTER(in_pktinfo_ex)


class in6_pktinfo_ex(ctypes.Structure):
    pass


IN6_PKTINFO_EX = in6_pktinfo_ex
PIN6_PKTINFO_EX = POINTER(in6_pktinfo_ex)


class in_recverr(ctypes.Structure):
    pass


IN_RECVERR = in_recverr
PIN_RECVERR = POINTER(in_recverr)


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: ws2ipdef.h Abstract: This file contains TCP/IP specific information
# for use by WinSock2 compatible applications. Copyright (c) Microsoft
# Corporation. All rights reserved. To provide the backward compatibility, all
# the TCP/IP specific definitions that were included in the WINSOCK.H file are
# now included in WINSOCK2.H file. WS2TCPIP.H file includes only the
# definitions introduced in the "WinSock 2 Protocol-Specific Annex" document.
# Rev 0.3 Nov 13, 1995 Rev 0.4 Dec 15, 1996 Environment: user mode or kernel
# mode --
if not defined(_WS2IPDEF_):
    _WS2IPDEF_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF


    from winapifamily_h import * # NOQA
        if defined(__cplusplus):
            pass
        # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if defined(_PREFAST_):
        pass
    # END IF


    if not defined(WS2IPDEF_ASSERT):
        def WS2IPDEF_ASSERT(exp):
            return 0
    # END IF


    if defined(_MSC_VER):
        WS2TCPIP_INLINE = VOID
    else:
        WS2TCPIP_INLINE = VOID
    # END IF


    from pyWinAPI.shared.in6addr_h import * # NOQA


    # Old IPv6 socket address structure (retained for sockaddr_gen definition).
    # AF_INET6.
    sockaddr_in6_old._fields_ = [
        ('sin6_family', SHORT),
        # Transport level port number.
        ('sin6_port', USHORT),
        # IPv6 flow information.
        ('sin6_flowinfo', ULONG),
        # IPv6 address.
        ('sin6_addr', IN6_ADDR),
    ]

    sockaddr_gen._fields_ = [
        ('Address', sockaddr),
        ('AddressIn', sockaddr_in),
        ('AddressIn6', sockaddr_in6_old),
    ]


    # Structure to keep interface specific information
    # Interface flags.
    _INTERFACE_INFO._fields_ = [
        ('iiFlags', ULONG),
        # Interface address.
        ('iiAddress', sockaddr_gen),
        # Broadcast address.
        ('iiBroadcastAddress', sockaddr_gen),
        # Network mask.
        ('iiNetmask', sockaddr_gen),
    ]


    # New structure that does not have dependency on the address size.
    # Interface flags.
    _INTERFACE_INFO_EX._fields_ = [
        ('iiFlags', ULONG),
        # Interface address.
        ('iiAddress', SOCKET_ADDRESS),
        # Broadcast address.
        ('iiBroadcastAddress', SOCKET_ADDRESS),
        # Network mask.
        ('iiNetmask', SOCKET_ADDRESS),
    ]


    # Possible flags for the iiFlags - bitmask.
    IFF_UP = 0x00000001    # Interface is up.
    IFF_BROADCAST = 0x00000002    # Broadcast is supported.
    IFF_MULTICAST = 0x00000010    # Multicast is supported.


    # Path MTU discovery states.
    class _PMTUD_STATE(ENUM):
        IP_PMTUDISC_NOT_SET = 1
        IP_PMTUDISC_DO = 2
        IP_PMTUDISC_DONT = 3
        IP_PMTUDISC_PROBE = 4
        IP_PMTUDISC_MAX = 5

    PMTUD_STATE = _PMTUD_STATE
    PPMTUD_STATE = POINTER(_PMTUD_STATE)


    # Options to use with [gs]etsockopt at the IPPROTO_IP level.
    # The values should be consistent with the IPv6 equivalents.
    IP_OPTIONS = 1    # Set/get IP options.
    IP_HDRINCL = 2    # Header is included with data.
    IP_TOS = 3    # IP type of service.
    IP_TTL = 4    # IP TTL (hop limit).
    IP_MULTICAST_IF = 9    # IP multicast interface.
    IP_MULTICAST_TTL = 10    # IP multicast TTL (hop limit).
    IP_MULTICAST_LOOP = 11    # IP multicast loopback.
    IP_ADD_MEMBERSHIP = 12    # Add an IP group membership.
    IP_DROP_MEMBERSHIP = 13    # Drop an IP group membership.
    IP_DONTFRAGMENT = 14    # Don't fragment IP datagrams.
    IP_ADD_SOURCE_MEMBERSHIP = 15    # Join IP group/source.
    IP_DROP_SOURCE_MEMBERSHIP = 16    # Leave IP group/source.
    IP_BLOCK_SOURCE = 17    # Block IP group/source.
    IP_UNBLOCK_SOURCE = 18    # Unblock IP group/source.
    IP_PKTINFO = 19    # Receive packet information.
    IP_HOPLIMIT = 21    # Receive packet hop limit.
    IP_RECVTTL = 21    # Receive packet Time To Live (TTL).
    IP_RECEIVE_BROADCAST = 22    # Allow/block broadcast reception.
    IP_RECVIF = 24    # Receive arrival interface.
    IP_RECVDSTADDR = 25    # Receive destination address.
    IP_IFLIST = 28    # Enable/Disable an interface list.
    IP_ADD_IFLIST = 29    # Add an interface list entry.
    IP_DEL_IFLIST = 30    # Delete an interface list entry.
    IP_UNICAST_IF = 31    # IP unicast interface.
    IP_RTHDR = 32    # Set/get IPv6 routing header.
    IP_GET_IFLIST = 33    # Get an interface list.
    IP_RECVRTHDR = 38    # Receive the routing header.
    IP_TCLASS = 39    # Packet traffic class.
    IP_RECVTCLASS = 40    # Receive packet traffic class.
    IP_RECVTOS = 40    # Receive packet Type Of Service (TOS).
    IP_ORIGINAL_ARRIVAL_IF = 47    # Original Arrival Interface Index.
    IP_ECN = 50    # Receive ECN codepoints in the IP header.
    IP_PKTINFO_EX = 51    # Receive extended packet information.
    IP_WFP_REDIRECT_RECORDS = 60    # WFP's Connection Redirect Records.
    IP_WFP_REDIRECT_CONTEXT = 70    # WFP's Connection Redirect Context.
    IP_MTU_DISCOVER = 71    # Set/get path MTU discover state.
    IP_MTU = 73    # Get path MTU.
    IP_NRT_INTERFACE = 74    # Set NRT interface constraint (outbound).
    IP_RECVERR = 75    # Receive ICMP errors.
    IP_UNSPECIFIED_TYPE_OF_SERVICE = -1
    IPV6_ADDRESS_BITS = RTL_BITS_OF(IN6_ADDR)


    # IPv6 socket address structure, RFC 3493.
    # NB: The LH version of sockaddr_in6 has the struct tag sockaddr_in6 rather
    # than sockaddr_in6_lh. This is to make sure that standard sockets apps
    # that conform to RFC 2553 (Basic Socket Interface Extensions for IPv6).
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # AF_INET6.
        # Set of interfaces for a scope.
        class _Union_1(ctypes.Union):
            pass


        _Union_1._fields_ = [
            ('sin6_scope_id', ULONG),
            ('sin6_scope_struct', SCOPE_ID),
        ]
        sockaddr_in6._Union_1 = _Union_1

        sockaddr_in6._anonymous_ = (
            '_Union_1',
        )

        sockaddr_in6._fields_ = [
            ('sin6_family', ADDRESS_FAMILY),
            # Transport level port number.
            ('sin6_port', USHORT),
            # IPv6 flow information.
            ('sin6_flowinfo', ULONG),
            # IPv6 address.
            ('sin6_addr', IN6_ADDR),
            ('_Union_1', sockaddr_in6._Union_1),
        ]

        # AF_INET6
        sockaddr_in6_w2ksp1._fields_ = [
            ('sin6_family', SHORT),
            # Transport level port number
            ('sin6_port', USHORT),
            # IPv6 flow information
            ('sin6_flowinfo', ULONG),
            # IPv6 address
            ('sin6_addr', in6_addr),
            # set of interfaces for a scope
            ('sin6_scope_id', ULONG),
        ]
        if NTDDI_VERSION >= NTDDI_VISTA:
            SOCKADDR_IN6 = SOCKADDR_IN6_LH
            PSOCKADDR_IN6 = POINTER(SOCKADDR_IN6_LH)
            LPSOCKADDR_IN6 = POINTER(SOCKADDR_IN6_LH)
        elif NTDDI_VERSION >= NTDDI_WIN2KSP1:
            SOCKADDR_IN6 = SOCKADDR_IN6_W2KSP1
            PSOCKADDR_IN6 = POINTER(SOCKADDR_IN6_W2KSP1)
            LPSOCKADDR_IN6 = POINTER(SOCKADDR_IN6_W2KSP1)
        else:
            SOCKADDR_IN6 = SOCKADDR_IN6_LH
            PSOCKADDR_IN6 = POINTER(SOCKADDR_IN6_LH)
            LPSOCKADDR_IN6 = POINTER(SOCKADDR_IN6_LH)
        # END IF


        _SOCKADDR_INET._fields_ = [
            ('Ipv4', SOCKADDR_IN),
            ('Ipv6', SOCKADDR_IN6),
            ('si_family', ADDRESS_FAMILY),
        ]


        # Structure to hold a pair of source, destination addresses.
        _sockaddr_in6_pair._fields_ = [
            ('SourceAddress', PSOCKADDR_IN6),
            ('DestinationAddress', PSOCKADDR_IN6),
        ]


        # Macro that works for both IPv4 and IPv6
        def SS_PORT(ssp):
            return PSOCKADDR_IN(ssp).sin_port

        if NTDDI_VERSION >= NTDDI_WIN2KSP1:
            # N.B. These addresses are in network byte order.
            IN6ADDR_ANY_INIT = [[[0]]]
            IN6ADDR_LOOPBACK_INIT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            IN6ADDR_ALLNODESONNODE_INIT = [
                0xFF,
                0x01,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x01
            ]
            IN6ADDR_ALLNODESONLINK_INIT = [
                0xFF,
                0x02,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x01
            ]
            IN6ADDR_ALLROUTERSONLINK_INIT = [
                0xFF,
                0x02,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x02
            ]

            IN6ADDR_ALLMLDV2ROUTERSONLINK_INIT = [
                0xFF,
                0x02,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x16
            ]
            IN6ADDR_TEREDOINITIALLINKLOCALADDRESS_INIT = [
                0xFE,
                0x80,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0xFF,
                0xFF,
                0xFE
            ]

            # The old link local address for XP-SP2/Win2K3 machines.
            IN6ADDR_TEREDOOLDLINKLOCALADDRESSXP_INIT = [
                0xFE,
                0x80,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                'T',
                'E',
                'R',
                'E',
                'D',
                'O'
            ]


            # The old link local address for Vista Beta-2 and earlier machines.
            IN6ADDR_TEREDOOLDLINKLOCALADDRESSVISTA_INIT = [
                0xFE,
                0x80,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0xFF,
                0xFF,
                0xFF,
                0xFF,
                0xFF,
                0xFF
            ]

            IN6ADDR_LINKLOCALPREFIX_INIT = [0xFE, 0x80]
            IN6ADDR_MULTICASTPREFIX_INIT = [0xFF, 0x00]
            IN6ADDR_SOLICITEDNODEMULTICASTPREFIX_INIT = [
                0xFF,
                0x02,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x01,
                0xFF,
            ]
            IN6ADDR_V4MAPPEDPREFIX_INIT = [
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0x00,
                0xFF,
                0xFF,
            ]

            IN6ADDR_6TO4PREFIX_INIT = [0x20, 0x02]
            IN6ADDR_TEREDOPREFIX_INIT = [0x20, 0x01, 0x00, 0x00]
            IN6ADDR_TEREDOPREFIX_INIT_OLD = [0x3F, 0xFE, 0x83, 0x1F]
            IN6ADDR_ULAPREFIX_INIT = [0xFC]
            IN6ADDR_SITELOCALPREFIX_INIT = [0xFE, 0xC0]
            IN6ADDR_6BONETESTPREFIX_INIT = [0x3F, 0xFE]
            IN6ADDR_LINKLOCALPREFIX_LENGTH = 64
            IN6ADDR_MULTICASTPREFIX_LENGTH = 8
            IN6ADDR_SOLICITEDNODEMULTICASTPREFIX_LENGTH = 104
            IN6ADDR_V4MAPPEDPREFIX_LENGTH = 96
            IN6ADDR_6TO4PREFIX_LENGTH = 16
            IN6ADDR_TEREDOPREFIX_LENGTH = 32
            if defined(__cplusplus):
                pass
            # END IF


            # N.B. These addresses are in network byte order.
            if defined(__cplusplus):
                pass
            # END IF


            if not defined(__midl):
                # RFC 3542 uses IN6_ARE_ADDR_EQUAL().
                IN6_ARE_ADDR_EQUAL = IN6_ADDR_EQUAL


                # We can't use the in6addr_any variable, since that would
                # require existing callers to link with a specific library.
                # We can't use the in6addr_loopback variable, since that would
                # require existing callers to link with a specific library.
                # Does the address have a format prefix
                # that indicates it uses EUI-64 interface identifiers?
                # Format prefixes 001 through 111, except for multicast.
                # Is this the subnet router anycast address?
                # See RFC 2373.
                # Is this a subnet reserved anycast address?
                # See RFC 2526. It talks about non-EUI-64
                # addresses as well, but IMHO that part
                # of the RFC doesn't make sense. For example,
                # it shouldn't apply to multicast or v4-compatible
                # addresses.
                # As best we can tell from simple inspection,
                # is this an anycast address?
                # Check the format prefix and exclude addresses
                # whose high 4 bits are all zero or all one.
                # This is a cheap way of excluding v4-compatible,
                # v4-mapped, loopback, multicast, link-local, site-local.
                # We can't use the in6addr_any variable, since that would
                # require existing callers to link with a specific library.
                # We can't use the in6addr_loopback variable, since that would
                # require existing callers to link with a specific library.
            # END IF   __midl
        # END IF   (NTDDI_VERSION >= NTDDI_WIN2KSP1)
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)


    # TCP/IP specific Ioctl codes.
    SIO_GET_INTERFACE_LIST = _IOR('t',127,ULONG)
    SIO_GET_INTERFACE_LIST_EX = _IOR('t',126,ULONG)
    SIO_SET_MULTICAST_FILTER = _IOW('t',125,ULONG)
    SIO_GET_MULTICAST_FILTER = _IOW('t', 124 | IOC_IN, ULONG)
    SIOCSIPMSFILTER = SIO_SET_MULTICAST_FILTER
    SIOCGIPMSFILTER = SIO_GET_MULTICAST_FILTER


    # Protocol independent ioctls for setting and retrieving multicast filters.
    SIOCSMSFILTER = _IOW('t',126,ULONG)
    SIOCGMSFILTER = _IOW('t', 127 | IOC_IN, ULONG)
    if NTDDI_VERSION >= NTDDI_VISTASP1:
        IDEAL_SEND_BACKLOG_IOCTLS = VOID


        # Query and change notification ioctls for the ideal send backlog size
        # for a given connection. Clients should use the wrappers defined in
        # ws2tcpip.h rather than using these ioctls directly.
        SIO_IDEAL_SEND_BACKLOG_QUERY = _IOR('t',123,ULONG)
        SIO_IDEAL_SEND_BACKLOG_CHANGE = _IO('t',122)
    # END IF


    # Protocol independent multicast source filter options.
    MCAST_JOIN_GROUP = 41    # Join all sources for a group.
    MCAST_LEAVE_GROUP = 42    # Drop all sources for a group.
    MCAST_BLOCK_SOURCE = 43    # Block IP group/source.
    MCAST_UNBLOCK_SOURCE = 44    # Unblock IP group/source.
    MCAST_JOIN_SOURCE_GROUP = 45    # Join IP group/source.
    MCAST_LEAVE_SOURCE_GROUP = 46    # Leave IP group/source.


    # Definitions of MCAST_INCLUDE and MCAST_EXCLUDE for multicast source
    # filter.
    class MULTICAST_MODE_TYPE(ENUM):
        MCAST_INCLUDE = 0
        MCAST_EXCLUDE = 1

    MCAST_INCLUDE = MULTICAST_MODE_TYPE.MCAST_INCLUDE
    MCAST_EXCLUDE = MULTICAST_MODE_TYPE.MCAST_EXCLUDE


    # Structure for IP_MREQ (used by IP_ADD_MEMBERSHIP and IP_DROP_MEMBERSHIP).
    # IP multicast address of group.
    ip_mreq._fields_ = [
        ('imr_multiaddr', IN_ADDR),
        # Local IP address of interface.
        ('imr_interface', IN_ADDR),
    ]


    # Structure for IP_MREQ_SOURCE (used by IP_BLOCK_SOURCE, IP_UNBLOCK_SOURCE
    # etc.).
    # IP multicast address of group.
    ip_mreq_source._fields_ = [
        ('imr_multiaddr', IN_ADDR),
        # IP address of source.
        ('imr_sourceaddr', IN_ADDR),
        # Local IP address of interface.
        ('imr_interface', IN_ADDR),
    ]


    # Structure for IP_MSFILTER (used by SIOCSIPMSFILTER and SIOCGIPMSFILTER).
    # IP multicast address of group.
    ip_msfilter._fields_ = [
        ('imsf_multiaddr', IN_ADDR),
        # Local IP address of interface.
        ('imsf_interface', IN_ADDR),
        # Filter mode.
        ('imsf_fmode', MULTICAST_MODE_TYPE),
        # Number of sources in src_list.
        ('imsf_numsrc', ULONG),
        # Start of source list.
        ('imsf_slist', IN_ADDR * 1),
    ]


    def IP_MSFILTER_SIZE(NumSources):
        return (
            ctypes.sizeof(IP_MSFILTER) -
            ctypes.sizeof(IN_ADDR) +
            NumSources *
            ctypes.sizeof(IN_ADDR)
        )

    # Options to use with [gs]etsockopt at the IPPROTO_IPV6 level.
    # These are specified in RFCs 3493 and 3542.
    # The values should be consistent with the IPv6 equivalents.
    IPV6_HOPOPTS = 1    # Set/get IPv6 hop-by-hop options.
    IPV6_HDRINCL = 2    # Header is included with data.
    IPV6_UNICAST_HOPS = 4    # IP unicast hop limit.
    IPV6_MULTICAST_IF = 9    # IP multicast interface.
    IPV6_MULTICAST_HOPS = 10    # IP multicast hop limit.
    IPV6_MULTICAST_LOOP = 11    # IP multicast loopback.
    IPV6_ADD_MEMBERSHIP = 12    # Add an IP group membership.
    IPV6_JOIN_GROUP = IPV6_ADD_MEMBERSHIP
    IPV6_DROP_MEMBERSHIP = 13    # Drop an IP group membership.
    IPV6_LEAVE_GROUP = IPV6_DROP_MEMBERSHIP
    IPV6_DONTFRAG = 14    # Don't fragment IP datagrams.
    IPV6_PKTINFO = 19    # Receive packet information.
    IPV6_HOPLIMIT = 21    # Receive packet hop limit.
    IPV6_PROTECTION_LEVEL = 23    # Set/get IPv6 protection level.
    IPV6_RECVIF = 24    # Receive arrival interface.
    IPV6_RECVDSTADDR = 25    # Receive destination address.
    IPV6_CHECKSUM = 26    # Offset to checksum for raw IP socket send.
    IPV6_V6ONLY = 27    # Treat wildcard bind as AF_INET6-only.
    IPV6_IFLIST = 28    # Enable/Disable an interface list.
    IPV6_ADD_IFLIST = 29    # Add an interface list entry.
    IPV6_DEL_IFLIST = 30    # Delete an interface list entry.
    IPV6_UNICAST_IF = 31    # IP unicast interface.
    IPV6_RTHDR = 32    # Set/get IPv6 routing header.
    IPV6_GET_IFLIST = 33    # Get an interface list.
    IPV6_RECVRTHDR = 38    # Receive the routing header.
    IPV6_TCLASS = 39    # Packet traffic class.
    IPV6_RECVTCLASS = 40    # Receive packet traffic class.
    IPV6_ECN = 50    # Receive ECN codepoints in the IP header.
    IPV6_PKTINFO_EX = 51    # Receive extended packet information.
    IPV6_WFP_REDIRECT_RECORDS = 60    # WFP's Connection Redirect Records
    IPV6_WFP_REDIRECT_CONTEXT = 70    # WFP's Connection Redirect Context
    IPV6_MTU_DISCOVER = 71    # Set/get path MTU discover state.
    IPV6_MTU = 72    # Get path MTU.
    IPV6_NRT_INTERFACE = 74    # Set NRT interface constraint (outbound).
    IPV6_RECVERR = 75    # Receive ICMPv6 errors.
    IP_UNSPECIFIED_HOP_LIMIT = -1
    IP_PROTECTION_LEVEL = IPV6_PROTECTION_LEVEL
    # Values of IPV6_PROTECTION_LEVEL.
    PROTECTION_LEVEL_UNRESTRICTED = 10    # For peer-to-peer apps.
    PROTECTION_LEVEL_EDGERESTRICTED = 20    # Same as unrestricted. Except for
    # Teredo.
    PROTECTION_LEVEL_RESTRICTED = 30    # For Intranet apps.
    if NTDDI_VERSION < NTDDI_VISTA:
        PROTECTION_LEVEL_DEFAULT = PROTECTION_LEVEL_EDGERESTRICTED
    else:
        PROTECTION_LEVEL_DEFAULT = -1
    # END IF


    # Structure for IPV6_JOIN_GROUP and IPV6_LEAVE_GROUP (also,
    # IPV6_ADD_MEMBERSHIP and IPV6_DROP_MEMBERSHIP).
    # IPv6 multicast address.
    ipv6_mreq._fields_ = [
        ('ipv6mr_multiaddr', IN6_ADDR),
        # Interface index.
        ('ipv6mr_interface', ULONG),
    ]

    if NTDDI_VERSION >= NTDDI_WINXP:
        # Structure for GROUP_REQ used by protocol independent source filters
        # (MCAST_JOIN_GROUP and MCAST_LEAVE_GROUP).
        # Interface index.
        group_req._fields_ = [
            ('gr_interface', ULONG),
            # Multicast address.
            ('gr_group', SOCKADDR_STORAGE),
        ]


        # Structure for GROUP_SOURCE_REQ used by protocol independent source
        # filters
        # (MCAST_JOIN_SOURCE_GROUP, MCAST_LEAVE_SOURCE_GROUP etc.).
        # Interface index.
        group_source_req._fields_ = [
            ('gsr_interface', ULONG),
            # Group address.
            ('gsr_group', SOCKADDR_STORAGE),
            # Source address.
            ('gsr_source', SOCKADDR_STORAGE),
        ]


        # Structure for GROUP_FILTER used by protocol independent source
        # filters
        # (SIOCSMSFILTER and SIOCGMSFILTER).
        # Interface index.
        group_filter._fields_ = [
            ('gf_interface', ULONG),
            # Multicast address.
            ('gf_group', SOCKADDR_STORAGE),
            # Filter mode.
            ('gf_fmode', MULTICAST_MODE_TYPE),
            # Number of sources.
            ('gf_numsrc', ULONG),
            # Source address.
            ('gf_slist', SOCKADDR_STORAGE * 1),
        ]


        def GROUP_FILTER_SIZE(numsrc):
            return (
                ctypes.sizeof(GROUP_FILTER) -
                ctypes.sizeof(SOCKADDR_STORAGE) +
                numsrc *
                ctypes.sizeof(SOCKADDR_STORAGE)
            )

    # END IF

    # Structure for IP_PKTINFO option.
    # Source/destination IPv4 address.
    in_pktinfo._fields_ = [
        ('ipi_addr', IN_ADDR),
        # Send/receive interface index.
        ('ipi_ifindex', ULONG),
    ]
    # Structure for IPV6_PKTINFO option.
    # Source/destination IPv6 address.
    in6_pktinfo._fields_ = [
        ('ipi6_addr', IN6_ADDR),
        # Send/receive interface index.
        ('ipi6_ifindex', ULONG),
    ]
    # Structure for IP_PKTINFO_EX option.
    in_pktinfo_ex._fields_ = [
        ('pkt_info', IN_PKTINFO),
        ('scope_id', SCOPE_ID),
    ]
    # Structure for IPV6_PKTINFO_EX option.
    in6_pktinfo_ex._fields_ = [
        ('pkt_info', IN6_PKTINFO),
        ('scope_id', SCOPE_ID),
    ]
    # Structure for IP_RECVERR option.
    # IPPROTO_ICMP or IPPROTO_ICMPV6.
    in_recverr._fields_ = [
        ('protocol', IPPROTO),
        # MTU if frag needed or pkt too big message.
        ('info', ULONG),
        ('type', UINT8),
        ('code', UINT8),
    ]
    # Maximum length of address literals (potentially including a port number)
    # generated by any address-to-string conversion routine. This length can
    # be used when declaring buffers used with getnameinfo, WSAAddressToString,
    # inet_ntoa, etc. We just provide one define, rather than one per api,
    # to avoid confusion.
    # The totals are derived from the following data:
    # 15: IPv4 address
    # 45: IPv6 address including embedded IPv4 address
    # 11: Scope Id
    # 2: Brackets around IPv6 address when port is present
    # 6: Port (including colon)
    # 1: Terminating null byte
    INET_ADDRSTRLEN = 22
    INET6_ADDRSTRLEN = 65
    # Options to use with [gs]etsockopt at the IPPROTO_TCP level.
    # TCP_NODELAY is defined in ws2def.h for historical reasons.
    # Offload preferences supported.
    TCP_OFFLOAD_NO_PREFERENCE = 0
    TCP_OFFLOAD_NOT_PREFERRED = 1
    TCP_OFFLOAD_PREFERRED = 2
    # TCP_NODELAY   0x0001
    TCP_EXPEDITED_1122 = 0x0002
    TCP_KEEPALIVE = 3
    TCP_MAXSEG = 4
    TCP_MAXRT = 5
    TCP_STDURG = 6
    TCP_NOURG = 7
    TCP_ATMARK = 8
    TCP_NOSYNRETRIES = 9
    TCP_TIMESTAMPS = 10
    TCP_OFFLOAD_PREFERENCE = 11
    TCP_CONGESTION_ALGORITHM = 12
    TCP_DELAY_FIN_ACK = 13
    TCP_MAXRTMS = 14
    TCP_FASTOPEN = 15
    TCP_KEEPCNT = 16
    TCP_KEEPIDLE = TCP_KEEPALIVE
    TCP_KEEPINTVL = 17


    if defined(_PREFAST_):
        pass
    # END IF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if defined(__cplusplus):
            pass
        # END IF  __cplusplus
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# END IF


