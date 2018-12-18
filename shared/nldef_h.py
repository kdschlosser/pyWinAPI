import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_NLDEF_ = None

class _NL_INTERFACE_OFFLOAD_ROD(ctypes.Structure):
    pass


NL_INTERFACE_OFFLOAD_ROD = _NL_INTERFACE_OFFLOAD_ROD
PNL_INTERFACE_OFFLOAD_ROD = POINTER(_NL_INTERFACE_OFFLOAD_ROD)


class _NL_PATH_BANDWIDTH_ROD(ctypes.Structure):
    pass


NL_PATH_BANDWIDTH_ROD = _NL_PATH_BANDWIDTH_ROD
PNL_PATH_BANDWIDTH_ROD = POINTER(_NL_PATH_BANDWIDTH_ROD)


class _NL_BANDWIDTH_INFORMATION(ctypes.Structure):
    pass


NL_BANDWIDTH_INFORMATION = _NL_BANDWIDTH_INFORMATION
PNL_BANDWIDTH_INFORMATION = POINTER(_NL_BANDWIDTH_INFORMATION)




# /* + + Copyright (c) 2000-2001 Microsoft Corporation Module Name: nldef.h
# Abstract: This module contains basic network layer definitions. Previously
# some of these were duplicated in both routprot.h and iprtrmib.h. Author:
# Environment: user mode or kernel mode --
if not defined(_NLDEF_):
    _NLDEF_ = VOID
    from winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        class NL_PREFIX_ORIGIN(ENUM):
            IpPrefixOriginOther = 0
            IpPrefixOriginManual = 1
            IpPrefixOriginWellKnown = 2
            IpPrefixOriginDhcp = 3
            IpPrefixOriginRouterAdvertisement = 4
            IpPrefixOriginUnchanged = 1 << 4

        IpPrefixOriginOther = NL_PREFIX_ORIGIN.IpPrefixOriginOther
        IpPrefixOriginManual = NL_PREFIX_ORIGIN.IpPrefixOriginManual
        IpPrefixOriginWellKnown = NL_PREFIX_ORIGIN.IpPrefixOriginWellKnown
        IpPrefixOriginDhcp = NL_PREFIX_ORIGIN.IpPrefixOriginDhcp
        IpPrefixOriginRouterAdvertisement = NL_PREFIX_ORIGIN.IpPrefixOriginRouterAdvertisement
        IpPrefixOriginUnchanged = NL_PREFIX_ORIGIN.IpPrefixOriginUnchanged


        # TODO: Remove these definitions.
        NlpoOther = IpPrefixOriginOther
        NlpoManual = IpPrefixOriginManual
        NlpoWellKnown = IpPrefixOriginWellKnown
        NlpoDhcp = IpPrefixOriginDhcp
        NlpoRouterAdvertisement = IpPrefixOriginRouterAdvertisement


        class NL_SUFFIX_ORIGIN(ENUM):
            NlsoOther = 0
            NlsoManual = 1
            NlsoWellKnown = 2
            NlsoDhcp = 3
            NlsoLinkLayerAddress = 4
            NlsoRandom = 5
            IpSuffixOriginOther = 0
            IpSuffixOriginManual = 1
            IpSuffixOriginWellKnown = 2
            IpSuffixOriginDhcp = 3
            IpSuffixOriginLinkLayerAddress = 4
            IpSuffixOriginRandom = 5
            IpSuffixOriginUnchanged = 1 << 4

        NlsoOther = NL_SUFFIX_ORIGIN.NlsoOther
        NlsoManual = NL_SUFFIX_ORIGIN.NlsoManual
        NlsoWellKnown = NL_SUFFIX_ORIGIN.NlsoWellKnown
        NlsoDhcp = NL_SUFFIX_ORIGIN.NlsoDhcp
        NlsoLinkLayerAddress = NL_SUFFIX_ORIGIN.NlsoLinkLayerAddress
        NlsoRandom = NL_SUFFIX_ORIGIN.NlsoRandom
        IpSuffixOriginOther = NL_SUFFIX_ORIGIN.IpSuffixOriginOther
        IpSuffixOriginManual = NL_SUFFIX_ORIGIN.IpSuffixOriginManual
        IpSuffixOriginWellKnown = NL_SUFFIX_ORIGIN.IpSuffixOriginWellKnown
        IpSuffixOriginDhcp = NL_SUFFIX_ORIGIN.IpSuffixOriginDhcp
        IpSuffixOriginLinkLayerAddress = NL_SUFFIX_ORIGIN.IpSuffixOriginLinkLayerAddress
        IpSuffixOriginRandom = NL_SUFFIX_ORIGIN.IpSuffixOriginRandom
        IpSuffixOriginUnchanged = NL_SUFFIX_ORIGIN.IpSuffixOriginUnchanged


        class NL_DAD_STATE(ENUM):
            NldsInvalid = 1
            NldsTentative = 2
            NldsDuplicate = 3
            NldsDeprecated = 4
            NldsPreferred = 5
            IpDadStateInvalid = 0
            IpDadStateTentative = 1
            IpDadStateDuplicate = 2
            IpDadStateDeprecated = 3
            IpDadStatePreferred = 4

        NldsInvalid = NL_DAD_STATE.NldsInvalid
        NldsTentative = NL_DAD_STATE.NldsTentative
        NldsDuplicate = NL_DAD_STATE.NldsDuplicate
        NldsDeprecated = NL_DAD_STATE.NldsDeprecated
        NldsPreferred = NL_DAD_STATE.NldsPreferred
        IpDadStateInvalid = NL_DAD_STATE.IpDadStateInvalid
        IpDadStateTentative = NL_DAD_STATE.IpDadStateTentative
        IpDadStateDuplicate = NL_DAD_STATE.IpDadStateDuplicate
        IpDadStateDeprecated = NL_DAD_STATE.IpDadStateDeprecated
        IpDadStatePreferred = NL_DAD_STATE.IpDadStatePreferred
        NL_MAX_METRIC_COMPONENT = (( 1) << 31) - 1


        # MIB_IPPROTO_* values were previously in iprtrmib.h.
        # PROTO_IP_* values were previously in routprot.h.
        def MAKE_ROUTE_PROTOCOL(suffix, value):
            return MIB_IPPROTO_ ## suffix = value, PROTO_IP_ ## suffix = value


        # Routing protocol values from RFC.
        class NL_ROUTE_PROTOCOL(ENUM):
            RouteProtocolOther = 1
            RouteProtocolLocal = 2
            RouteProtocolNetMgmt = 3
            RouteProtocolIcmp = 4
            RouteProtocolEgp = 5
            RouteProtocolGgp = 6
            RouteProtocolHello = 7
            RouteProtocolRip = 8
            RouteProtocolIsIs = 9
            RouteProtocolEsIs = 10
            RouteProtocolCisco = 11
            RouteProtocolBbn = 12
            RouteProtocolOspf = 13
            RouteProtocolBgp = 14
            RouteProtocolIdpr = 15
            RouteProtocolEigrp = 16
            RouteProtocolDvmrp = 17
            RouteProtocolRpl = 18
            RouteProtocolDhcp = 19
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(OTHER
            # ENUM ERROR: 1)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(LOCAL
            # ENUM ERROR: 2)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(NETMGMT
            # ENUM ERROR: 3)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(ICMP
            # ENUM ERROR: 4)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(EGP
            # ENUM ERROR: 5)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(GGP
            # ENUM ERROR: 6)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(HELLO
            # ENUM ERROR: 7)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(RIP
            # ENUM ERROR: 8)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(IS_IS
            # ENUM ERROR: 9)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(ES_IS
            # ENUM ERROR: 10)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(CISCO
            # ENUM ERROR: 11)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(BBN
            # ENUM ERROR: 12)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(OSPF
            # ENUM ERROR: 13)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(BGP
            # ENUM ERROR: 14)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(IDPR
            # ENUM ERROR: 15)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(EIGRP
            # ENUM ERROR: 16)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(DVMRP
            # ENUM ERROR: 17)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(RPL
            # ENUM ERROR: 18)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(DHCP
            # ENUM ERROR: 19)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(NT_AUTOSTATIC
            # ENUM ERROR: 10002)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(NT_STATIC
            # ENUM ERROR: 10006)
            # ENUM ERROR: MAKE_ROUTE_PROTOCOL(NT_STATIC_NON_DOD
            # ENUM ERROR: 10007)
        PNL_ROUTE_PROTOCOL = POINTER(NL_ROUTE_PROTOCOL)


        RouteProtocolOther = NL_ROUTE_PROTOCOL.RouteProtocolOther
        RouteProtocolLocal = NL_ROUTE_PROTOCOL.RouteProtocolLocal
        RouteProtocolNetMgmt = NL_ROUTE_PROTOCOL.RouteProtocolNetMgmt
        RouteProtocolIcmp = NL_ROUTE_PROTOCOL.RouteProtocolIcmp
        RouteProtocolEgp = NL_ROUTE_PROTOCOL.RouteProtocolEgp
        RouteProtocolGgp = NL_ROUTE_PROTOCOL.RouteProtocolGgp
        RouteProtocolHello = NL_ROUTE_PROTOCOL.RouteProtocolHello
        RouteProtocolRip = NL_ROUTE_PROTOCOL.RouteProtocolRip
        RouteProtocolIsIs = NL_ROUTE_PROTOCOL.RouteProtocolIsIs
        RouteProtocolEsIs = NL_ROUTE_PROTOCOL.RouteProtocolEsIs
        RouteProtocolCisco = NL_ROUTE_PROTOCOL.RouteProtocolCisco
        RouteProtocolBbn = NL_ROUTE_PROTOCOL.RouteProtocolBbn
        RouteProtocolOspf = NL_ROUTE_PROTOCOL.RouteProtocolOspf
        RouteProtocolBgp = NL_ROUTE_PROTOCOL.RouteProtocolBgp
        RouteProtocolIdpr = NL_ROUTE_PROTOCOL.RouteProtocolIdpr
        RouteProtocolEigrp = NL_ROUTE_PROTOCOL.RouteProtocolEigrp
        RouteProtocolDvmrp = NL_ROUTE_PROTOCOL.RouteProtocolDvmrp
        RouteProtocolRpl = NL_ROUTE_PROTOCOL.RouteProtocolRpl
        RouteProtocolDhcp = NL_ROUTE_PROTOCOL.RouteProtocolDhcp


        class NL_ADDRESS_TYPE(ENUM):
            NlatUnspecified = 1
            NlatUnicast = 2
            NlatAnycast = 3
            NlatMulticast = 4
            NlatBroadcast = 5
            NlatInvalid = 6

        PNL_ADDRESS_TYPE = POINTER(NL_ADDRESS_TYPE)


        NlatUnspecified = NL_ADDRESS_TYPE.NlatUnspecified
        NlatUnicast = NL_ADDRESS_TYPE.NlatUnicast
        NlatAnycast = NL_ADDRESS_TYPE.NlatAnycast
        NlatMulticast = NL_ADDRESS_TYPE.NlatMulticast
        NlatBroadcast = NL_ADDRESS_TYPE.NlatBroadcast
        NlatInvalid = NL_ADDRESS_TYPE.NlatInvalid


        # NL_ROUTE_ORIGIN
        # Define route origin values.
        class _NL_ROUTE_ORIGIN(ENUM):
            NlroManual = 1
            NlroWellKnown = 2
            NlroDHCP = 3
            NlroRouterAdvertisement = 4
            Nlro6to4 = 5

        NL_ROUTE_ORIGIN = _NL_ROUTE_ORIGIN
        PNL_ROUTE_ORIGIN = POINTER(_NL_ROUTE_ORIGIN)

        # NL_NEIGHBOR_STATE
        # Define network layer neighbor state. RFC 2461, section 7.3.2 has
        # details.
        # Note: Only state names are documented, we chose the values used here.
        class _NL_NEIGHBOR_STATE(ENUM):
            NlnsUnreachable = 1
            NlnsIncomplete = 2
            NlnsProbe = 3
            NlnsDelay = 4
            NlnsStale = 5
            NlnsReachable = 6
            NlnsPermanent = 7
            NlnsMaximum = 8

        NL_NEIGHBOR_STATE = _NL_NEIGHBOR_STATE
        PNL_NEIGHBOR_STATE = POINTER(_NL_NEIGHBOR_STATE)


        class _NL_LINK_LOCAL_ADDRESS_BEHAVIOR(ENUM):
            LinkLocalAlwaysOff = 0
            LinkLocalDelayed = 1
            LinkLocalAlwaysOn = 2
            LinkLocalUnchanged = - 1

        NL_LINK_LOCAL_ADDRESS_BEHAVIOR = _NL_LINK_LOCAL_ADDRESS_BEHAVIOR

        _NL_INTERFACE_OFFLOAD_ROD._fields_ = [
            ('NlChecksumSupported', BOOLEAN, 1),
            ('NlOptionsSupported', BOOLEAN, 1),
            ('TlDatagramChecksumSupported', BOOLEAN, 1),
            ('TlStreamChecksumSupported', BOOLEAN, 1),
            ('TlStreamOptionsSupported', BOOLEAN, 1),
            ('FastPathCompatible', BOOLEAN, 1),
            ('TlLargeSendOffloadSupported', BOOLEAN, 1),
            ('TlGiantSendOffloadSupported', BOOLEAN, 1),
        ]


        class _NL_ROUTER_DISCOVERY_BEHAVIOR(ENUM):
            RouterDiscoveryDisabled = 0
            RouterDiscoveryEnabled = 1
            RouterDiscoveryDhcp = 2
            RouterDiscoveryUnchanged = - 1

        NL_ROUTER_DISCOVERY_BEHAVIOR = _NL_ROUTER_DISCOVERY_BEHAVIOR


        class _NL_BANDWIDTH_FLAG(ENUM):
            NlbwDisabled = 0
            NlbwEnabled = 1
            NlbwUnchanged = - 1

        NL_BANDWIDTH_FLAG = _NL_BANDWIDTH_FLAG
        PNL_BANDWIDTH_FLAG = POINTER(_NL_BANDWIDTH_FLAG)

        _NL_PATH_BANDWIDTH_ROD._fields_ = [
            ('Bandwidth', ULONG64),
            ('Instability', ULONG64),
            ('BandwidthPeaked', BOOLEAN),
        ]


        class _NL_NETWORK_CATEGORY(ENUM):
            NetworkCategoryPublic = 1
            NetworkCategoryPrivate = 2
            NetworkCategoryDomainAuthenticated = 3
            NetworkCategoryUnchanged = - 1
            NetworkCategoryUnknown = - 1

        NL_NETWORK_CATEGORY = _NL_NETWORK_CATEGORY
        PNL_NETWORK_CATEGORY = POINTER(_NL_NETWORK_CATEGORY)


        class _NL_INTERFACE_NETWORK_CATEGORY_STATE(ENUM):
            NlincCategoryUnknown = 0
            NlincPublic = 1
            NlincPrivate = 2
            NlincDomainAuthenticated = 3
            NlincCategoryStateMax = 4
            # ENUM ERROR: *PNL_INTERFACE_NETWORK_CATEGORY_STATE;
        NL_INTERFACE_NETWORK_CATEGORY_STATE = _NL_INTERFACE_NETWORK_CATEGORY_STATE
        PNL_INTERFACE_NETWORK_CATEGORY_STATE = POINTER(_NL_INTERFACE_NETWORK_CATEGORY_STATE)
        NET_IF_CURRENT_SESSION = -1


        _NL_BANDWIDTH_INFORMATION._fields_ = [
            ('Bandwidth', ULONG64),
            ('Instability', ULONG64),
            ('BandwidthPeaked', BOOLEAN),
        ]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
# END IF   _NLDEF_


