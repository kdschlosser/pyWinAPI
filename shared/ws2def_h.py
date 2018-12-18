import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class sockaddr(ctypes.Structure):
    pass


SOCKADDR = sockaddr
PSOCKADDR = POINTER(sockaddr)
LPSOCKADDR = POINTER(sockaddr)


class _SOCKET_ADDRESS(ctypes.Structure):
    pass


SOCKET_ADDRESS = _SOCKET_ADDRESS
PSOCKET_ADDRESS = POINTER(_SOCKET_ADDRESS)
LPSOCKET_ADDRESS = POINTER(_SOCKET_ADDRESS)


class _SOCKET_ADDRESS_LIST(ctypes.Structure):
    pass


SOCKET_ADDRESS_LIST = _SOCKET_ADDRESS_LIST
PSOCKET_ADDRESS_LIST = POINTER(_SOCKET_ADDRESS_LIST)
LPSOCKET_ADDRESS_LIST = POINTER(_SOCKET_ADDRESS_LIST)


class _CSADDR_INFO(ctypes.Structure):
    pass


CSADDR_INFO = _CSADDR_INFO
PCSADDR_INFO = POINTER(_CSADDR_INFO)
LPCSADDR_INFO = POINTER(_CSADDR_INFO)


class sockaddr_storage(ctypes.Structure):
    pass


SOCKADDR_STORAGE_LH = sockaddr_storage
PSOCKADDR_STORAGE_LH = POINTER(sockaddr_storage)
LPSOCKADDR_STORAGE_LH = POINTER(sockaddr_storage)


class sockaddr_storage_xp(ctypes.Structure):
    pass


SOCKADDR_STORAGE_XP = sockaddr_storage_xp
PSOCKADDR_STORAGE_XP = POINTER(sockaddr_storage_xp)
LPSOCKADDR_STORAGE_XP = POINTER(sockaddr_storage_xp)


class _SOCKET_PROCESSOR_AFFINITY(ctypes.Structure):
    pass


SOCKET_PROCESSOR_AFFINITY = _SOCKET_PROCESSOR_AFFINITY
PSOCKET_PROCESSOR_AFFINITY = POINTER(_SOCKET_PROCESSOR_AFFINITY)


class SCOPE_ID(ctypes.Structure):
    pass


PSCOPE_ID = POINTER(SCOPE_ID)


class sockaddr_in(ctypes.Structure):
    pass


SOCKADDR_IN = sockaddr_in
PSOCKADDR_IN = POINTER(sockaddr_in)


class sockaddr_dl(ctypes.Structure):
    pass


SOCKADDR_DL = sockaddr_dl
PSOCKADDR_DL = POINTER(sockaddr_dl)


class _WSABUF(ctypes.Structure):
    pass


WSABUF = _WSABUF
LPWSABUF = POINTER(_WSABUF)


class _WSAMSG(ctypes.Structure):
    pass


WSAMSG = _WSAMSG
PWSAMSG = POINTER(_WSAMSG)
LPWSAMSG = POINTER(_WSAMSG)


class _WSACMSGHDR(ctypes.Structure):
    pass


WSACMSGHDR = _WSACMSGHDR
PWSACMSGHDR = POINTER(_WSACMSGHDR)
LPWSACMSGHDR = POINTER(_WSACMSGHDR)


class addrinfo(ctypes.Structure):
    pass


ADDRINFOA = addrinfo
PADDRINFOA = POINTER(addrinfo)


class addrinfoW(ctypes.Structure):
    pass


ADDRINFOW = addrinfoW
PADDRINFOW = POINTER(addrinfoW)


class addrinfoexA(ctypes.Structure):
    pass


ADDRINFOEXA = addrinfoexA
PADDRINFOEXA = POINTER(addrinfoexA)
LPADDRINFOEXA = POINTER(addrinfoexA)


class addrinfoexW(ctypes.Structure):
    pass


ADDRINFOEXW = addrinfoexW
PADDRINFOEXW = POINTER(addrinfoexW)
LPADDRINFOEXW = POINTER(addrinfoexW)


class addrinfoex2A(ctypes.Structure):
    pass


ADDRINFOEX2A = addrinfoex2A
PADDRINFOEX2A = POINTER(addrinfoex2A)
LPADDRINFOEX2A = POINTER(addrinfoex2A)


class addrinfoex2W(ctypes.Structure):
    pass


ADDRINFOEX2W = addrinfoex2W
PADDRINFOEX2W = POINTER(addrinfoex2W)
LPADDRINFOEX2W = POINTER(addrinfoex2W)


class addrinfoex3(ctypes.Structure):
    pass


ADDRINFOEX3 = addrinfoex3
PADDRINFOEX3 = POINTER(addrinfoex3)
LPADDRINFOEX3 = POINTER(addrinfoex3)


class addrinfoex4(ctypes.Structure):
    pass


ADDRINFOEX4 = addrinfoex4
PADDRINFOEX4 = POINTER(addrinfoex4)
LPADDRINFOEX4 = POINTER(addrinfoex4)


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: ws2def.h Abstract: This file contains the core definitions for the
# Winsock2 specification that can be used by both user - mode and kernel mode
# modules. This file is included in WINSOCK2.H. User mode applications should
# include WINSOCK2.H rather than including this file directly. This file can
# not be included by a module that also includes WINSOCK.H. Environment: user
# mode or kernel mode - -

_WS2DEF_ = None

if not defined(_WS2DEF_):
    _WS2DEF_ = 1
    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA


    _WINSOCK_DEPRECATED_BY = None
    if not defined(_WINSOCK_DEPRECATED_BY):
        _WINSOCK_DEPRECATED_NO_WARNINGS = 1
        BUILD_WINDOWS = None
        _WINSOCK_DEPRECATE_WARNINGS = None
        if (
            (
                (
                    defined(_WINSOCK_DEPRECATED_NO_WARNINGS) or
                    defined(BUILD_WINDOWS)
                ) and
                not defined(_WINSOCK_DEPRECATE_WARNINGS)
            ) or
            defined(MIDL_PASS)
        ):
            def _WINSOCK_DEPRECATED_BY(replacement):
                pass
        else:
            def _WINSOCK_DEPRECATED_BY(replacement):
                pass

        # END IF
    # END IF
    if defined(__cplusplus):
        pass
    # END IF
    _WINSOCK2API_ = 1
    _WINSOCKAPI_ = 1
    if not defined(_WINSOCK2API_) and defined(_WINSOCKAPI_):
        raise RuntimeError(
            ' Do not include winsock.h and ws2def.h in the same module. '
            'Instead include only winsock2.h.'
        )
    # END IF

    # Allow Winsock components to disable PREfast errors.
    _PREFAST_ = 1
    IPV6_PREFAST_SAFE = 1
    if defined(_PREFAST_) and defined(IPV6_PREFAST_SAFE):
        from pyWinAPI.shared.ipv6prefast_h import * # NOQA
    # END IF   _PREFAST_

    if _WIN32_WINNT >= 0x0600:
        if defined(_MSC_VER):
            WS2DEF_INLINE = VOID
        else:
            WS2DEF_INLINE = VOID            # GNU style
        # END IF
    # END IF  (_WIN32_WINNT >= 0x0600)
    from pyWinAPI.shared.inaddr_h import * # NOQA

    if _WIN32_WINNT >= 0x0600:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # Address families.
            ADDRESS_FAMILY = USHORT
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # END IF (_WIN32_WINNT >= 0x0600)

    # Although AF_UNSPEC is defined for backwards compatibility, using
    # AF_UNSPEC for the "af" parameter when creating a socket is STRONGLY
    # DISCOURAGED. The interpretation of the "protocol" parameter
    # depends on the actual address family chosen. As environments grow
    # to include more and more address families that use overlapping
    # protocol values there is more and more chance of choosing an
    # undesired address family when AF_UNSPEC is used.
    AF_UNSPEC = 0    # unspecified
    AF_UNIX = 1    # local to host (pipes, portals)
    AF_INET = 2    # internetwork: UDP, TCP, etc.
    AF_IMPLINK = 3    # arpanet imp addresses
    AF_PUP = 4    # pup protocols: e.g. BSP
    AF_CHAOS = 5    # mit CHAOS protocols
    AF_NS = 6    # XEROX NS protocols
    AF_IPX = AF_NS    # IPX protocols: IPX, SPX, etc.
    AF_ISO = 7    # ISO protocols
    AF_OSI = AF_ISO    # OSI is ISO
    AF_ECMA = 8    # european computer manufacturers
    AF_DATAKIT = 9    # datakit protocols
    AF_CCITT = 10    # CCITT protocols, X.25 etc
    AF_SNA = 11    # IBM SNA
    AF_DECnet = 12    # DECnet
    AF_DLI = 13    # Direct data link interface
    AF_LAT = 14    # LAT
    AF_HYLINK = 15    # NSC Hyperchannel
    AF_APPLETALK = 16    # AppleTalk
    AF_NETBIOS = 17    # NetBios - style addresses
    AF_VOICEVIEW = 18    # VoiceView
    AF_FIREFOX = 19    # Protocols from Firefox
    AF_UNKNOWN1 = 20    # Somebody is using thisnot
    AF_BAN = 21    # Banyan
    AF_ATM = 22    # Native ATM Services
    AF_INET6 = 23    # Internetwork Version 6
    AF_CLUSTER = 24    # Microsoft Wolfpack
    AF_12844 = 25    # IEEE 1284.4 WG AF
    AF_IRDA = 26    # IrDA
    AF_NETDES = 28    # Network Designers OSI & gateway
    if _WIN32_WINNT < 0x0501:
        AF_MAX = 29
    else:
        AF_TCNPROCESS = 29
        AF_TCNMESSAGE = 30
        AF_ICLFXBM = 31
        if _WIN32_WINNT < 0x0600:
            AF_MAX = 32
        else:
            AF_BTH = 32            # Bluetooth RFCOMM/L2CAP protocols
            if _WIN32_WINNT < 0x0601:
                AF_MAX = 33
            else:
                AF_LINK = 33
                if _WIN32_WINNT < 0x0604:
                    AF_MAX = 34
                else:
                    AF_HYPERV = 34
                    AF_MAX = 35
                # END IF  (_WIN32_WINNT < 0x0604)
            # END IF  (_WIN32_WINNT < 0x0601)
        # END IF  (_WIN32_WINNT < 0x0600)
    # END IF  (_WIN32_WINNT < 0x0501)
    # Socket types.
    SOCK_STREAM = 1
    SOCK_DGRAM = 2
    SOCK_RAW = 3
    SOCK_RDM = 4
    SOCK_SEQPACKET = 5


    # Define a level for socket I/O controls in the same numbering space as
    # IPPROTO_TCP, IPPROTO_IP, etc.
    SOL_SOCKET = 0xFFFF


    # Define socket - level options.
    SO_DEBUG = 0x0001    # turn on debugging info recording
    SO_ACCEPTCONN = 0x0002    # socket has had listen()
    SO_REUSEADDR = 0x0004    # allow local address reuse
    SO_KEEPALIVE = 0x0008    # keep connections alive
    SO_DONTROUTE = 0x0010    # just use interface addresses
    SO_BROADCAST = 0x0020    # permit sending of broadcast msgs
    SO_USELOOPBACK = 0x0040    # bypass hardware when possible
    SO_LINGER = 0x0080    # linger on close if data present
    SO_OOBINLINE = 0x0100    # leave received OOB data in line
    SO_DONTLINGER = ~SO_LINGER
    SO_EXCLUSIVEADDRUSE = ~SO_REUSEADDR    # disallow local address reuse
    SO_SNDBUF = 0x1001    # send buffer size
    SO_RCVBUF = 0x1002    # receive buffer size
    SO_SNDLOWAT = 0x1003    # send low - water mark
    SO_RCVLOWAT = 0x1004    # receive low - water mark
    SO_SNDTIMEO = 0x1005    # send timeout
    SO_RCVTIMEO = 0x1006    # receive timeout
    SO_ERROR = 0x1007    # get error status and clear
    SO_TYPE = 0x1008    # get socket type
    SO_BSP_STATE = 0x1009    # get socket 5 - tuple state
    SO_GROUP_ID = 0x2001    # ID of a socket group
    SO_GROUP_PRIORITY = 0x2002    # the relative priority within a group
    SO_MAX_MSG_SIZE = 0x2003    # maximum message size
    SO_CONDITIONAL_ACCEPT = 0x3002    # enable true conditional accept:

    # connection is not ack - ed to the
    # other side until conditional
    # function returns CF_ACCEPT
    SO_PAUSE_ACCEPT = 0x3003    # pause accepting new connections
    SO_COMPARTMENT_ID = 0x3004    # get/set the compartment for a socket
    if _WIN32_WINNT >= 0x0600:
        SO_RANDOMIZE_PORT = 0x3005        # randomize assignment of wildcard ports
        SO_PORT_SCALABILITY = 0x3006        # enable port scalability
        SO_REUSE_UNICASTPORT = 0x3007        # defer ephemeral port allocation for

        # outbound connections
        SO_REUSE_MULTICASTPORT = 0x3008        # enable port reuse and disable unicast

        # reception.    # END IF  (_WIN32_WINNT >= 0x0600)
    # Base constant used for defining WSK - specific options.
    WSK_SO_BASE = 0x4000


    # Options to use with [gs]etsockopt at the IPPROTO_TCP level.
    TCP_NODELAY = 0x0001

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # Structure used to store most addresses.
        _TEMP_sockaddr = [
        ]
        if _WIN32_WINNT < 0x0600:
            _TEMP_sockaddr += [
                ('sa_family', USHORT),
                ]
        else:
            _TEMP_sockaddr += [
                # Address family.
                ('sa_family', ADDRESS_FAMILY),
            ]
        # END IF   (_WIN32_WINNT < 0x0600)
        _TEMP_sockaddr += [
            # Up to 14 bytes of direct address.
            ('sa_data', CHAR * 14),
        ]
        sockaddr._fields_ = _TEMP_sockaddr

        __CSADDR_DEFINED__ = None
        if not defined(__CSADDR_DEFINED__):
            __CSADDR_DEFINED__ = 1

            # /* SockAddr Information
            _SOCKET_ADDRESS._fields_ = [
                ('lpSockaddr', LPSOCKADDR),
                # _Field_range_( >= , (ctypes.sizeof(SOCKADDR_IN6)))
                ('iSockaddrLength', INT),
            ]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        # /* Address list returned via SIO_ADDRESS_LIST_QUERY
        _SOCKET_ADDRESS_LIST._fields_ = [
            ('iAddressCount', INT),
            ('Address', SOCKET_ADDRESS * 1),
        ]
        if _WIN32_WINNT >= 0x0600:
            def SIZEOF_SOCKET_ADDRESS_LIST(AddressCount):
                return (
                    FIELD_OFFSET(SOCKET_ADDRESS_LIST, 'Address') +
                    (AddressCount * ctypes.sizeof(SOCKET_ADDRESS))
                )

        # END IF  (_WIN32_WINNT >= 0x0600)
        # /* CSAddr Information
        _CSADDR_INFO._fields_ = [
            ('LocalAddr', SOCKET_ADDRESS),
            ('RemoteAddr', SOCKET_ADDRESS),
            ('iSocketType', INT),
            ('iProtocol', INT),
        ]
    # END IF  __CSADDR_DEFINED__
    # Portable socket structure (RFC 2553).
    # Desired design of maximum size and alignment.
    # These are implementation specific.
    _SS_MAXSIZE = 128    # Maximum size
    _SS_ALIGNSIZE = ctypes.sizeof(INT64)    # Desired alignment
    # Definitions used for sockaddr_storage structure paddings design.
    if _WIN32_WINNT >= 0x0600:
        _SS_PAD1SIZE = _SS_ALIGNSIZE - ctypes.sizeof(USHORT)
        _SS_PAD2SIZE = (
            _SS_MAXSIZE -
            (ctypes.sizeof(USHORT) + _SS_PAD1SIZE + _SS_ALIGNSIZE)
        )
    else:
        _SS_PAD1SIZE = _SS_ALIGNSIZE - ctypes.sizeof(SHORT)
        _SS_PAD2SIZE = (
            _SS_MAXSIZE -
            (ctypes.sizeof(SHORT) + _SS_PAD1SIZE + _SS_ALIGNSIZE)
        )
    # END IF  (_WIN32_WINNT >= 0x0600)

    sockaddr_storage._fields_ = [
        # address family
        ('ss_family', ADDRESS_FAMILY),
        # 6 byte pad, this is to make
        ('__ss_pad1', CHAR * _SS_PAD1SIZE),
        # Field to force desired structure
        ('__ss_align', INT64),
        # 112 byte pad to achieve desired size;
        ('__ss_pad2', CHAR * _SS_PAD2SIZE),
    ]
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        sockaddr_storage_xp._fields_ = [
            # Address family.
            ('ss_family', SHORT),
            # 6 byte pad, this is to make
            ('__ss_pad1', CHAR * _SS_PAD1SIZE),
            # Field to force desired structure
            ('__ss_align', INT64),
            # 112 byte pad to achieve desired size;
            ('__ss_pad2', CHAR * _SS_PAD2SIZE),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if _WIN32_WINNT >= 0x0600:
        SOCKADDR_STORAGE = SOCKADDR_STORAGE_LH
        PSOCKADDR_STORAGE = POINTER(SOCKADDR_STORAGE)
        LPSOCKADDR_STORAGE = POINTER(SOCKADDR_STORAGE)

    elif _WIN32_WINNT >= 0x0501:
        SOCKADDR_STORAGE = SOCKADDR_STORAGE_XP
        PSOCKADDR_STORAGE = POINTER(SOCKADDR_STORAGE)
        LPSOCKADDR_STORAGE = POINTER(SOCKADDR_STORAGE)

    # END IF

    if _WIN32_WINNT >= 0x0602:
        _SOCKET_PROCESSOR_AFFINITY._fields_ = [
            ('Processor', PROCESSOR_NUMBER),
            ('NumaNodeId', USHORT),
            ('Reserved', USHORT),
        ]
    # END IF  (_WIN32_WINNT >= 0x0602)

    # /* WinSock 2 extension - - manifest constants for WSAIoctl()
    IOC_UNIX = 0x00000000
    IOC_WS2 = 0x08000000
    IOC_PROTOCOL = 0x10000000
    IOC_VENDOR = 0x18000000

    if _WIN32_WINNT >= 0x0600:
        # /* WSK - specific IO control codes are Winsock2 codes with the
        # highest - order 3 bits of the Vendor/AddressFamily - specific field
        # set to 1.
        IOC_WSK = IOC_WS2 | 0x07000000
    # END IF  (_WIN32_WINNT >= 0x0600)

    def _WSAIO(x, y):
        return IOC_VOID | x | y


    def _WSAIOR(x, y):
        return IOC_OUT | x | y


    def _WSAIOW(x, y):
        return IOC_IN | x | y


    def _WSAIORW(x, y):
        return IOC_INOUT | x | y


    SIO_ASSOCIATE_HANDLE = _WSAIOW(IOC_WS2, 1)
    SIO_ENABLE_CIRCULAR_QUEUEING = _WSAIO(IOC_WS2, 2)
    SIO_FIND_ROUTE = _WSAIOR(IOC_WS2, 3)
    SIO_FLUSH = _WSAIO(IOC_WS2, 4)
    SIO_GET_BROADCAST_ADDRESS = _WSAIOR(IOC_WS2, 5)
    SIO_GET_EXTENSION_FUNCTION_POINTER = _WSAIORW(IOC_WS2, 6)
    SIO_GET_QOS = _WSAIORW(IOC_WS2, 7)
    SIO_GET_GROUP_QOS = _WSAIORW(IOC_WS2, 8)
    SIO_MULTIPOINT_LOOPBACK = _WSAIOW(IOC_WS2, 9)
    SIO_MULTICAST_SCOPE = _WSAIOW(IOC_WS2, 10)
    SIO_SET_QOS = _WSAIOW(IOC_WS2, 11)
    SIO_SET_GROUP_QOS = _WSAIOW(IOC_WS2, 12)
    SIO_TRANSLATE_HANDLE = _WSAIORW(IOC_WS2, 13)
    SIO_ROUTING_INTERFACE_QUERY = _WSAIORW(IOC_WS2, 20)
    SIO_ROUTING_INTERFACE_CHANGE = _WSAIOW(IOC_WS2, 21)
    SIO_ADDRESS_LIST_QUERY = _WSAIOR(IOC_WS2, 22)
    SIO_ADDRESS_LIST_CHANGE = _WSAIO(IOC_WS2, 23)
    SIO_QUERY_TARGET_PNP_HANDLE = _WSAIOR(IOC_WS2, 24)
    SIO_QUERY_RSS_PROCESSOR_INFO = _WSAIOR(IOC_WS2, 37)
    if _WIN32_WINNT >= 0x0501:
        SIO_ADDRESS_LIST_SORT = _WSAIORW(IOC_WS2, 25)
    # END IF  (_WIN32_WINNT >= 0x0501)

    if _WIN32_WINNT >= 0x0600:
        SIO_RESERVED_1 = _WSAIOW(IOC_WS2, 26)
        SIO_RESERVED_2 = _WSAIOW(IOC_WS2, 33)
    # END IF  (_WIN32_WINNT >= 0x0600)

    SIO_GET_MULTIPLE_EXTENSION_FUNCTION_POINTER = _WSAIORW(IOC_WS2, 36)


    # Constants and structures defined by the internet system (RFC 790)
    # N.B. required for backwards compatability to support 0 = IP for the
    # level argument to get/setsockopt.
    IPPROTO_IP = 0


    # Protocols. The IPv6 defines are specified in RFC 2292.
    class IPPROTO(ENUM):
        if _WIN32_WINNT >= 0x0501:
            IPPROTO_HOPOPTS = 0
        # END IF

        IPPROTO_ICMP = 1
        IPPROTO_IGMP = 2
        IPPROTO_GGP = 3
        if _WIN32_WINNT >= 0x0501:
            IPPROTO_IPV4 = 4
        # END IF

        if _WIN32_WINNT >= 0x0600:
            IPPROTO_ST = 5
        # END IF

        IPPROTO_TCP = 6
        if _WIN32_WINNT >= 0x0600:
            IPPROTO_CBT = 7
            IPPROTO_EGP = 8
            IPPROTO_IGP = 9
        # END IF

        IPPROTO_PUP = 12
        IPPROTO_UDP = 17
        IPPROTO_IDP = 22
        if _WIN32_WINNT >= 0x0600:
            IPPROTO_RDP = 27
        # END IF

        if _WIN32_WINNT >= 0x0501:
            IPPROTO_IPV6 = 41
            IPPROTO_ROUTING = 43
            IPPROTO_FRAGMENT = 44
            IPPROTO_ESP = 50
            IPPROTO_AH = 51
            IPPROTO_ICMPV6 = 58
            IPPROTO_NONE = 59
            IPPROTO_DSTOPTS = 60
        # END IF

        IPPROTO_ND = 77
        if _WIN32_WINNT >= 0x0501:
            IPPROTO_ICLFXBM = 78
        # END IF

        if _WIN32_WINNT >= 0x0600:
            IPPROTO_PIM = 103
            IPPROTO_PGM = 113
            IPPROTO_L2TP = 115
            IPPROTO_SCTP = 132
        # END IF

        IPPROTO_RAW = 255
        IPPROTO_MAX = 256
        IPPROTO_RESERVED_RAW = 257
        IPPROTO_RESERVED_IPSEC = 258
        IPPROTO_RESERVED_IPSECOFFLOAD = 259
        IPPROTO_RESERVED_WNV = 260
        IPPROTO_RESERVED_MAX = 261

    PIPROTO = POINTER(IPPROTO)
    if _WIN32_WINNT >= 0x0501:
        IPPROTO_HOPOPTS = IPPROTO.IPPROTO_HOPOPTS
    # END IF

    IPPROTO_ICMP = IPPROTO.IPPROTO_ICMP
    IPPROTO_IGMP = IPPROTO.IPPROTO_IGMP
    IPPROTO_GGP = IPPROTO.IPPROTO_GGP

    if _WIN32_WINNT >= 0x0501:
        IPPROTO_IPV4 = IPPROTO.IPPROTO_IPV4
    # END IF

    if _WIN32_WINNT >= 0x0501:
        IPPROTO_ST = IPPROTO.IPPROTO_ST

    IPPROTO_TCP = IPPROTO.IPPROTO_TCP

    if _WIN32_WINNT >= 0x0600:
        IPPROTO_CBT = IPPROTO.IPPROTO_CBT
        IPPROTO_EGP = IPPROTO.IPPROTO_EGP
        IPPROTO_IGP = IPPROTO.IPPROTO_IGP
    # END IF

    IPPROTO_PUP = IPPROTO.IPPROTO_PUP
    IPPROTO_UDP = IPPROTO.IPPROTO_UDP
    IPPROTO_IDP = IPPROTO.IPPROTO_IDP

    if _WIN32_WINNT >= 0x0600:
        IPPROTO_RDP = IPPROTO.IPPROTO_RDP
    # END IF

    if _WIN32_WINNT >= 0x0501:
        IPPROTO_IPV6 = IPPROTO.IPPROTO_IPV6
        IPPROTO_ROUTING = IPPROTO.IPPROTO_ROUTING
        IPPROTO_FRAGMENT = IPPROTO.IPPROTO_FRAGMENT
        IPPROTO_ESP = IPPROTO.IPPROTO_ESP
        IPPROTO_AH = IPPROTO.IPPROTO_AH
        IPPROTO_ICMPV6 = IPPROTO.IPPROTO_ICMPV6
        IPPROTO_NONE = IPPROTO.IPPROTO_NONE
        IPPROTO_DSTOPTS = IPPROTO.IPPROTO_DSTOPTS
    # END IF

    IPPROTO_ND = IPPROTO.IPPROTO_ND

    if _WIN32_WINNT >= 0x0501:
        IPPROTO_ICLFXBM = IPPROTO.IPPROTO_ICLFXBM
    # END IF

    if _WIN32_WINNT >= 0x0600:
        IPPROTO_PIM = IPPROTO.IPPROTO_PIM
        IPPROTO_PGM = IPPROTO.IPPROTO_PGM
        IPPROTO_L2TP = IPPROTO.IPPROTO_L2TP
        IPPROTO_SCTP = IPPROTO.IPPROTO_SCTP
    # END IF

    IPPROTO_RAW = IPPROTO.IPPROTO_RAW
    IPPROTO_MAX = IPPROTO.IPPROTO_MAX
    IPPROTO_RESERVED_RAW = IPPROTO.IPPROTO_RESERVED_RAW
    IPPROTO_RESERVED_IPSEC = IPPROTO.IPPROTO_RESERVED_IPSEC
    IPPROTO_RESERVED_IPSECOFFLOAD = IPPROTO.IPPROTO_RESERVED_IPSECOFFLOAD
    IPPROTO_RESERVED_WNV = IPPROTO.IPPROTO_RESERVED_WNV
    IPPROTO_RESERVED_MAX = IPPROTO.IPPROTO_RESERVED_MAX


    # Port/socket numbers: network standard functions
    IPPORT_TCPMUX = 1
    IPPORT_ECHO = 7
    IPPORT_DISCARD = 9
    IPPORT_SYSTAT = 11
    IPPORT_DAYTIME = 13
    IPPORT_NETSTAT = 15
    IPPORT_QOTD = 17
    IPPORT_MSP = 18
    IPPORT_CHARGEN = 19
    IPPORT_FTP_DATA = 20
    IPPORT_FTP = 21
    IPPORT_TELNET = 23
    IPPORT_SMTP = 25
    IPPORT_TIMESERVER = 37
    IPPORT_NAMESERVER = 42
    IPPORT_WHOIS = 43
    IPPORT_MTP = 57

    # /* Port/socket numbers: host specific functions
    IPPORT_TFTP = 69
    IPPORT_RJE = 77
    IPPORT_FINGER = 79
    IPPORT_TTYLINK = 87
    IPPORT_SUPDUP = 95

    # /* UNIX TCP sockets
    IPPORT_POP3 = 110
    IPPORT_NTP = 123
    IPPORT_EPMAP = 135
    IPPORT_NETBIOS_NS = 137
    IPPORT_NETBIOS_DGM = 138
    IPPORT_NETBIOS_SSN = 139
    IPPORT_IMAP = 143
    IPPORT_SNMP = 161
    IPPORT_SNMP_TRAP = 162
    IPPORT_IMAP3 = 220
    IPPORT_LDAP = 389
    IPPORT_HTTPS = 443
    IPPORT_MICROSOFT_DS = 445
    IPPORT_EXECSERVER = 512
    IPPORT_LOGINSERVER = 513
    IPPORT_CMDSERVER = 514
    IPPORT_EFSSERVER = 520

    # /* UNIX UDP sockets
    IPPORT_BIFFUDP = 512
    IPPORT_WHOSERVER = 513
    IPPORT_ROUTESERVER = 520

    # 520 + 1 also used
    # /* Ports < IPPORT_RESERVED are reserved for privileged processes
    # (e.g. root).
    IPPORT_RESERVED = 1024
    if _WIN32_WINNT >= 0x0600:
        IPPORT_REGISTERED_MIN = IPPORT_RESERVED
        IPPORT_REGISTERED_MAX = 0xBFFF
        IPPORT_DYNAMIC_MIN = 0xC000
        IPPORT_DYNAMIC_MAX = 0xFFFF
    # END IF  (_WIN32_WINNT >= 0x0600)
    # /* Definitions of bits in internet address integers. On subnets, the
    # decomposition of addresses to host and net parts is done according to
    # subnet mask, not the masks here. N.B. RFC - compliant definitions for
    # host - order elements are named IN_xxx, while network - order elements
    # are named IN4_xxx.

    def IN_CLASSA(i):
        return i & 0x80000000 == 0

    IN_CLASSA_NET = 0xFF000000
    IN_CLASSA_NSHIFT = 24
    IN_CLASSA_HOST = 0x00FFFFFF
    IN_CLASSA_MAX = 128


    def IN_CLASSB(i):
        return i & 0xC0000000 == 0x80000000


    IN_CLASSB_NET = 0xFFFF0000
    IN_CLASSB_NSHIFT = 16
    IN_CLASSB_HOST = 0x0000FFFF
    IN_CLASSB_MAX = 65536


    def IN_CLASSC(i):
        return i & 0xE0000000 == 0xC0000000


    IN_CLASSC_NET = 0xFFFFFF00
    IN_CLASSC_NSHIFT = 8
    IN_CLASSC_HOST = 0x000000FF


    def IN_CLASSD(i):
        return i & 0xF0000000 == 0xE0000000


    IN_CLASSD_NET = 0xF0000000    # These ones aren't really
    IN_CLASSD_NSHIFT = 28    # net and host fields, but
    IN_CLASSD_HOST = 0x0FFFFFFF    # routing needn't know.


    def IN_MULTICAST(i):
        return IN_CLASSD(i)

    INADDR_ANY = 0x00000000
    INADDR_LOOPBACK = 0x7F000001
    INADDR_BROADCAST = 0xFFFFFFFF
    INADDR_NONE = 0xFFFFFFFF

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # Scope ID definition
        class SCOPE_LEVEL(ENUM):
            ScopeLevelInterface = 1
            ScopeLevelLink = 2
            ScopeLevelSubnet = 3
            ScopeLevelAdmin = 4
            ScopeLevelSite = 5
            ScopeLevelOrganization = 8
            ScopeLevelGlobal = 14
            ScopeLevelCount = 16

        ScopeLevelInterface = SCOPE_LEVEL.ScopeLevelInterface
        ScopeLevelLink = SCOPE_LEVEL.ScopeLevelLink
        ScopeLevelSubnet = SCOPE_LEVEL.ScopeLevelSubnet
        ScopeLevelAdmin = SCOPE_LEVEL.ScopeLevelAdmin
        ScopeLevelSite = SCOPE_LEVEL.ScopeLevelSite
        ScopeLevelOrganization = SCOPE_LEVEL.ScopeLevelOrganization
        ScopeLevelGlobal = SCOPE_LEVEL.ScopeLevelGlobal
        ScopeLevelCount = SCOPE_LEVEL.ScopeLevelCount


        class _Union_1(ctypes.Union):
            pass


        class _Struct_1(ctypes.Structure):
            pass


        _Struct_1._fields_ = [
            ('Zone', ULONG, 28),
            ('Level', ULONG, 4),
        ]
        _Union_1._Struct_1 = _Struct_1

        _Union_1._anonymous_ = (
            '_Struct_1',
        )

        _Union_1._fields_ = [
            ('_Struct_1', _Union_1._Struct_1),
            ('Value', ULONG),
        ]
        SCOPE_ID._Union_1 = _Union_1

        SCOPE_ID._anonymous_ = (
            '_Union_1',
        )

        SCOPE_ID._fields_ = [
            ('_Union_1', SCOPE_ID._Union_1),
        ]
        SCOPEID_UNSPECIFIED_INIT = [0]


        # IPv4 Socket address, Internet style
        _TEMP_sockaddr_in = [
        ]
        if _WIN32_WINNT < 0x0600:
            _TEMP_sockaddr_in += [
                ('sin_family', SHORT),
                ]
        else: #  (_WIN32_WINNT < 0x0600)
            _TEMP_sockaddr_in += [
                ('sin_family', ADDRESS_FAMILY),
            ]
        # END IF   (_WIN32_WINNT < 0x0600)
        _TEMP_sockaddr_in += [
            ('sin_port', USHORT),
            ('sin_addr', IN_ADDR),
            ('sin_zero', CHAR * 8),
        ]
        sockaddr_in._fields_ = _TEMP_sockaddr_in

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # Datalink (MAC) address
    # If you don't use the entire sdl_data field, then fill it starting with
    # the low
    # bytes...
    if _WIN32_WINNT >= 0x0601:
        sockaddr_dl._fields_ = [
            ('sdl_family', ADDRESS_FAMILY),
            ('sdl_data', UCHAR * 8),
            ('sdl_zero', UCHAR * 4),
        ]
    # END IF  (_WIN32_WINNT >= 0x0601)

    IOCPARM_MASK = 0x7F    # parameters must be < 128 bytes
    IOC_VOID = 0x20000000    # no parameters
    IOC_OUT = 0x40000000    # copy out parameters
    IOC_IN = 0x80000000    # copy in parameters
    IOC_INOUT = IOC_IN | IOC_OUT

    # /* 0x20000000 distinguishes new & old ioctl's
    def _IO(x, y):
        return IOC_VOID | (x << 8) | y


    def _IOR(x, y, t):
        return IOC_OUT | ((ctypes.sizeof(t) & IOCPARM_MASK)<< 16) | (x << 8)| y


    def _IOW(x, y, t):
        return IOC_IN | ((ctypes.sizeof(t) & IOCPARM_MASK)<< 16) | (x << 8)| y

    # /* WinSock 2 extension - - WSABUF and QOS struct, include qos.h to pull
    # in FLOWSPEC and related definitions
    _WSABUF._fields_ = [
        # the length of the buffer
        ('len', ULONG),
        # the pointer to the buffer
        ('buf', POINTER(CHAR)),
    ]

    # /* WSAMSG - - for WSASendMsg
    _TEMP__WSAMSG = [
        # Remote address
        ('name', LPSOCKADDR),
        # Remote address length
        ('namelen', INT),
        # Data buffer array
        ('lpBuffers', LPWSABUF),
    ]
    if _WIN32_WINNT >= 0x0600:
        _TEMP__WSAMSG += [
            # Number of elements in the array
            ('dwBufferCount', ULONG),
        ]
    else:
        _TEMP__WSAMSG += [
            # Number of elements in the array
            ('dwBufferCount', DWORD),
        ]
    # END IF   (_WIN32_WINNT >= 0x0600)
    _TEMP__WSAMSG += [
        # Control buffer
        ('Control', WSABUF),
    ]
    if _WIN32_WINNT >= 0x0600:
        _TEMP__WSAMSG += [
            # Flags
            ('dwFlags', ULONG),
        ]
    else:
        _TEMP__WSAMSG += [
            # Flags
            ('dwFlags', DWORD),
        ]
    # END IF   (_WIN32_WINNT >= 0x0600)
    _WSAMSG._fields_ = _TEMP__WSAMSG

    # /* Layout of ancillary data objects in the control buffer (RFC 2292).
    if _WIN32_WINNT >= 0x0600:
        # _WSACMSGHDR = CMSGHDR
        pass
    # END IF  (_WIN32_WINNT >= 0x0600)

    _WSACMSGHDR._fields_ = [
        ('cmsg_len', SIZE_T),
        ('cmsg_level', INT),
        ('cmsg_type', INT),
    ]
    if _WIN32_WINNT >= 0x0600:
        CMSGHDR = WSACMSGHDR
        PCMSGHDR = POINTER(WSACMSGHDR)
    # END IF  (_WIN32_WINNT >= 0x0600)

    # /* Alignment macros for header and data members of the control buffer.
    def WSA_CMSGHDR_ALIGN(length):
        return (
            (length + TYPE_ALIGNMENT(WSACMSGHDR) - 1) &
            (~(TYPE_ALIGNMENT(WSACMSGHDR) - 1))
        )


    def WSA_CMSGDATA_ALIGN(length):
        return (
            (length + MAX_NATURAL_ALIGNMENT - 1) &
            (~(MAX_NATURAL_ALIGNMENT - 1))
        )

    if _WIN32_WINNT >= 0x0600:
        CMSGHDR_ALIGN = WSA_CMSGHDR_ALIGN
        CMSGDATA_ALIGN = WSA_CMSGDATA_ALIGN
    # END IF  (_WIN32_WINNT >= 0x0600)

    # /* WSA_CMSG_FIRSTHDR Returns a pointer to the first ancillary data
    # object, or a null pointer if there is no ancillary data in the control
    # buffer of the WSAMSG structure. LPCMSGHDR WSA_CMSG_FIRSTHDR
    # ( LPWSAMSG msg );
    def WSA_CMSG_FIRSTHDR(msg):
        if msg.Control.len >= ctypes.sizeof(WSACMSGHDR):
            return LPWSACMSGHDR(msg).Control.buf
        else:
            return LPWSACMSGHDR(NULL)


    if _WIN32_WINNT >= 0x0600:
        CMSG_FIRSTHDR = WSA_CMSG_FIRSTHDR
    # END IF  (_WIN32_WINNT >= 0x0600)
    # /* WSA_CMSG_NXTHDR Returns a pointer to the next ancillary data object,
    # or a null if there are no more data objects. LPCMSGHDR WSA_CMSG_NEXTHDR
    # ( LPWSAMSG msg, LPWSACMSGHDR cmsg );
    def WSA_CMSG_NXTHDR(msg, cmsg):
        if cmsg is NULL:
            return WSA_CMSG_FIRSTHDR(msg)
        elif (
            (
                cmsg +
                WSA_CMSGHDR_ALIGN(cmsg.cmsg_len) +
                ctypes.sizeof(WSACMSGHDR)
            ) >
            (msg.Control.buf + msg.Control.len)
        ):
            return LPWSACMSGHDR(NULL)
        else:
            return LPWSACMSGHDR(cmsg + WSA_CMSGHDR_ALIGN(cmsg.cmsg_len))


    if _WIN32_WINNT >= 0x0600:
        CMSG_NXTHDR = WSA_CMSG_NXTHDR
    # END IF  (_WIN32_WINNT >= 0x0600)

    # /* WSA_CMSG_DATA Returns a pointer to the first byte of data
    # (what is referred to as the cmsg_data member though it is not defined in the structure). Note that RFC 2292 defines this as CMSG_DATA, but that name is already used by wincrypt.h, and so Windows has used WSA_CMSG_DATA. PUCHAR WSA_CMSG_DATA ( LPWSACMSGHDR pcmsg );
    #
    def WSA_CMSG_DATA(cmsg):
        return cmsg + WSA_CMSGDATA_ALIGN(ctypes.sizeof(WSACMSGHDR))

    # /* WSA_CMSG_SPACE Returns total size of an ancillary data object given
    # the amount of data. Used to allocate the correct amount of space. SIZE_T
    # WSA_CMSG_SPACE ( SIZE_T length );
    def WSA_CMSG_SPACE(length):
        return WSA_CMSGDATA_ALIGN(
            ctypes.sizeof(WSACMSGHDR) +
            WSA_CMSGHDR_ALIGN(length)
        )


    if _WIN32_WINNT >= 0x0600:
        CMSG_SPACE = WSA_CMSG_SPACE
    # END IF  (_WIN32_WINNT >= 0x0600)
    # /* WSA_CMSG_LEN Returns the value to store in cmsg_len given the amount
    # of data. SIZE_T WSA_CMSG_LEN ( SIZE_T length );

    def WSA_CMSG_LEN(length):
        return WSA_CMSGDATA_ALIGN(ctypes.sizeof(WSACMSGHDR)) + length


    if _WIN32_WINNT >= 0x0600:
        CMSG_LEN = WSA_CMSG_LEN
    # END IF  (_WIN32_WINNT >= 0x0600)
    # /* Definition for flags member of the WSAMSG structure This is in
    # addition to other MSG_xxx flags defined for recv/recvfrom/send/sendto.
    MSG_TRUNC = 0x0100
    MSG_CTRUNC = 0x0200
    MSG_BCAST = 0x0400
    MSG_MCAST = 0x0800
    MSG_ERRQUEUE = 0x1000

    # Flags used in "hints" argument to getaddrinfo()
    # - AI_ADDRCONFIG is supported starting with Vista
    # - default is AI_ADDRCONFIG ON whether the flag is set or not
    # because the performance penalty in not having ADDRCONFIG in
    # the multi - protocol stack environment is severe;
    # this defaulting may be disabled by specifying the AI_ALL flag,
    # in that case AI_ADDRCONFIG must be EXPLICITLY specified to
    # enable ADDRCONFIG behavior
    AI_PASSIVE = 0x00000001    # Socket address will be used in bind() call
    AI_CANONNAME = 0x00000002    # Return canonical name in first ai_canonname
    AI_NUMERICHOST = 0x00000004    # Nodename must be a numeric address string
    AI_NUMERICSERV = 0x00000008    # Servicename must be a numeric port number
    AI_DNS_ONLY = 0x00000010    # Restrict queries to unicast DNS only (no LLMNR, netbios, etc.)
    AI_ALL = 0x00000100    # Query both IP6 and IP4 with AI_V4MAPPED
    AI_ADDRCONFIG = 0x00000400    # Resolution only if global address configured
    AI_V4MAPPED = 0x00000800    # On v6 failure, query v4 and convert to V4MAPPED format
    AI_NON_AUTHORITATIVE = 0x00004000    # LUP_NON_AUTHORITATIVE
    AI_SECURE = 0x00008000    # LUP_SECURE
    AI_RETURN_PREFERRED_NAMES = 0x00010000    # LUP_RETURN_PREFERRED_NAMES
    AI_FQDN = 0x00020000    # Return the FQDN in ai_canonname
    AI_FILESERVER = 0x00040000    # Resolving fileserver name resolution
    AI_DISABLE_IDN_ENCODING = 0x00080000    # Disable Internationalized Domain Names handling
    AI_EXTENDED = 0x80000000    # Indicates this is extended ADDRINFOEX(2/..) struct
    AI_RESOLUTION_HANDLE = 0x40000000    # Request resolution handle

    # Structure used in getaddrinfo() call
    addrinfo._fields_ = [
        # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
        ('ai_flags', INT),
        # PF_xxx
        ('ai_family', INT),
        # SOCK_xxx
        ('ai_socktype', INT),
        # 0 or IPPROTO_xxx for IPv4 and IPv6
        ('ai_protocol', INT),
        # Length of ai_addr
        ('ai_addrlen', SIZE_T),
        # Canonical name for nodename
        ('ai_canonname', POINTER(CHAR)),
        # Binary address
        ('ai_addr', POINTER(sockaddr)),
        # Next structure in linked list
        ('ai_next', POINTER(addrinfo)),
    ]

    addrinfoW._fields_ = [
        # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
        ('ai_flags', INT),
        # PF_xxx
        ('ai_family', INT),
        # SOCK_xxx
        ('ai_socktype', INT),
        # 0 or IPPROTO_xxx for IPv4 and IPv6
        ('ai_protocol', INT),
        # Length of ai_addr
        ('ai_addrlen', SIZE_T),
        # Canonical name for nodename
        ('ai_canonname', PWSTR),
        # Binary address
        ('ai_addr', POINTER(sockaddr)),
        # Next structure in linked list
        ('ai_next', POINTER(addrinfoW)),
    ]
    if _WIN32_WINNT >= 0x0600:
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            addrinfoexA._fields_ = [
                # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
                ('ai_flags', INT),
                # PF_xxx
                ('ai_family', INT),
                # SOCK_xxx
                ('ai_socktype', INT),
                # 0 or IPPROTO_xxx for IPv4 and IPv6
                ('ai_protocol', INT),
                # Length of ai_addr
                ('ai_addrlen', SIZE_T),
                # Canonical name for nodename
                ('ai_canonname', POINTER(CHAR)),
                # Binary address
                ('ai_addr', POINTER(sockaddr)),
                ('ai_blob', POINTER(VOID)),
                ('ai_bloblen', SIZE_T),
                ('ai_provider', LPGUID),
                # Next structure in linked list
                ('ai_next', POINTER(addrinfoexA)),
            ]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
        addrinfoexW._fields_ = [
            # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
            ('ai_flags', INT),
            # PF_xxx
            ('ai_family', INT),
            # SOCK_xxx
            ('ai_socktype', INT),
            # 0 or IPPROTO_xxx for IPv4 and IPv6
            ('ai_protocol', INT),
            # Length of ai_addr
            ('ai_addrlen', SIZE_T),
            # Canonical name for nodename
            ('ai_canonname', PWSTR),
            # Binary address
            ('ai_addr', POINTER(sockaddr)),
            ('ai_blob', POINTER(VOID)),
            ('ai_bloblen', SIZE_T),
            ('ai_provider', LPGUID),
            # Next structure in linked list
            ('ai_next', POINTER(addrinfoexW)),
        ]
    # END IF
    if _WIN32_WINNT >= 0x0602:
        ADDRINFOEX_VERSION_2 = 2
        ADDRINFOEX_VERSION_3 = 3
        ADDRINFOEX_VERSION_4 = 4

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            addrinfoex2A._fields_ = [
                # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
                ('ai_flags', INT),
                # PF_xxx
                ('ai_family', INT),
                # SOCK_xxx
                ('ai_socktype', INT),
                # 0 or IPPROTO_xxx for IPv4 and IPv6
                ('ai_protocol', INT),
                # Length of ai_addr
                ('ai_addrlen', SIZE_T),
                # Canonical name for nodename
                ('ai_canonname', POINTER(CHAR)),
                # Binary address
                ('ai_addr', POINTER(sockaddr)),
                ('ai_blob', POINTER(VOID)),
                ('ai_bloblen', SIZE_T),
                ('ai_provider', LPGUID),
                # Next structure in linked list
                ('ai_next', POINTER(addrinfoex2A)),
                ('ai_version', INT),
                ('ai_fqdn', POINTER(CHAR)),
            ]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
        addrinfoex2W._fields_ = [
            # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
            ('ai_flags', INT),
            # PF_xxx
            ('ai_family', INT),
            # SOCK_xxx
            ('ai_socktype', INT),
            # 0 or IPPROTO_xxx for IPv4 and IPv6
            ('ai_protocol', INT),
            # Length of ai_addr
            ('ai_addrlen', SIZE_T),
            # Canonical name for nodename
            ('ai_canonname', PWSTR),
            # Binary address
            ('ai_addr', POINTER(sockaddr)),
            ('ai_blob', POINTER(VOID)),
            ('ai_bloblen', SIZE_T),
            ('ai_provider', LPGUID),
            # Next structure in linked list
            ('ai_next', POINTER(addrinfoex2W)),
            ('ai_version', INT),
            ('ai_fqdn', PWSTR),
        ]

        addrinfoex3._fields_ = [
            # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
            ('ai_flags', INT),
            # PF_xxx
            ('ai_family', INT),
            # SOCK_xxx
            ('ai_socktype', INT),
            # 0 or IPPROTO_xxx for IPv4 and IPv6
            ('ai_protocol', INT),
            # Length of ai_addr
            ('ai_addrlen', SIZE_T),
            # Canonical name for nodename
            ('ai_canonname', PWSTR),
            # Binary address
            ('ai_addr', POINTER(sockaddr)),
            ('ai_blob', POINTER(VOID)),
            ('ai_bloblen', SIZE_T),
            ('ai_provider', LPGUID),
            # Next structure in linked list
            ('ai_next', POINTER(addrinfoex3)),
            ('ai_version', INT),
            ('ai_fqdn', PWSTR),
            ('ai_interfaceindex', INT),
        ]

        addrinfoex4._fields_ = [
            # AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
            ('ai_flags', INT),
            # PF_xxx
            ('ai_family', INT),
            # SOCK_xxx
            ('ai_socktype', INT),
            # 0 or IPPROTO_xxx for IPv4 and IPv6
            ('ai_protocol', INT),
            # Length of ai_addr
            ('ai_addrlen', SIZE_T),
            # Canonical name for nodename
            ('ai_canonname', PWSTR),
            # Binary address
            ('ai_addr', POINTER(sockaddr)),
            ('ai_blob', POINTER(VOID)),
            ('ai_bloblen', SIZE_T),
            ('ai_provider', POINTER(GUID)),
            # Next structure in linked list
            ('ai_next', POINTER(addrinfoex4)),
            ('ai_version', INT),
            ('ai_fqdn', PWSTR),
            ('ai_interfaceindex', INT),
            ('ai_resolutionhandle', HANDLE),
        ]
    # END IF
    # Flags for getaddrinfo()
    # Name Spaces
    NS_ALL = 0
    NS_SAP = 1
    NS_NDS = 2
    NS_PEER_BROWSE = 3
    NS_SLP = 5
    NS_DHCP = 6
    NS_TCPIP_LOCAL = 10
    NS_TCPIP_HOSTS = 11
    NS_DNS = 12
    NS_NETBT = 13
    NS_WINS = 14
    if _WIN32_WINNT >= 0x0501:
        NS_NLA = 15        # Network Location Awareness
    # END IF  (_WIN32_WINNT >= 0x0501)
    if _WIN32_WINNT >= 0x0600:
        NS_BTH = 16        # Bluetooth SDP Namespace
    # END IF  (_WIN32_WINNT >= 0x0600)
    NS_NBP = 20
    NS_MS = 30
    NS_STDA = 31
    NS_NTDS = 32
    if _WIN32_WINNT >= 0x0600:
        NS_EMAIL = 37
        NS_PNRPNAME = 38
        NS_PNRPCLOUD = 39
    # END IF  (_WIN32_WINNT >= 0x0600)
    NS_X500 = 40
    NS_NIS = 41
    NS_NISPLUS = 42
    NS_WRQ = 50
    NS_NETDES = 60    # Network Designers Limited

    # Flags for getnameinfo()
    NI_NOFQDN = 0x01    # Only return nodename portion for local hosts
    NI_NUMERICHOST = 0x02    # Return numeric form of the host's address
    NI_NAMEREQD = 0x04    # Error if the host's name not in DNS
    NI_NUMERICSERV = 0x08    # Return numeric form of the service (port )
    NI_DGRAM = 0x10    # Service is a datagram service
    NI_MAXHOST = 1025    # Max size of a fully - qualified domain name
    NI_MAXSERV = 32    # Max size of a service name
    if defined(__cplusplus):
        pass
    # END IF
# END IF
