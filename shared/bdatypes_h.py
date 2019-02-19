import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_BDATYPES_ = None
MANAGED_ENUMS = None
_MANAGED = None

class _BDA_TEMPLATE_CONNECTION(ctypes.Structure):
    pass


BDA_TEMPLATE_CONNECTION = _BDA_TEMPLATE_CONNECTION
PBDA_TEMPLATE_CONNECTION = POINTER(_BDA_TEMPLATE_CONNECTION)


class _BDA_TEMPLATE_PIN_JOINT(ctypes.Structure):
    pass


BDA_TEMPLATE_PIN_JOINT = _BDA_TEMPLATE_PIN_JOINT
PBDA_TEMPLATE_PIN_JOINT = POINTER(_BDA_TEMPLATE_PIN_JOINT)


class tagKS_BDA_FRAME_INFO(ctypes.Structure):
    pass


KS_BDA_FRAME_INFO = tagKS_BDA_FRAME_INFO
PKS_BDA_FRAME_INFO = POINTER(tagKS_BDA_FRAME_INFO)


class _BDA_ETHERNET_ADDRESS(ctypes.Structure):
    pass


BDA_ETHERNET_ADDRESS = _BDA_ETHERNET_ADDRESS
PBDA_ETHERNET_ADDRESS = POINTER(_BDA_ETHERNET_ADDRESS)


class _BDA_ETHERNET_ADDRESS_LIST(ctypes.Structure):
    pass


BDA_ETHERNET_ADDRESS_LIST = _BDA_ETHERNET_ADDRESS_LIST
PBDA_ETHERNET_ADDRESS_LIST = POINTER(_BDA_ETHERNET_ADDRESS_LIST)


class _BDA_IPv4_ADDRESS(ctypes.Structure):
    pass


BDA_IPv4_ADDRESS = _BDA_IPv4_ADDRESS
PBDA_IPv4_ADDRESS = POINTER(_BDA_IPv4_ADDRESS)


class _BDA_IPv4_ADDRESS_LIST(ctypes.Structure):
    pass


BDA_IPv4_ADDRESS_LIST = _BDA_IPv4_ADDRESS_LIST
PBDA_IPv4_ADDRESS_LIST = POINTER(_BDA_IPv4_ADDRESS_LIST)


class _BDA_IPv6_ADDRESS(ctypes.Structure):
    pass


BDA_IPv6_ADDRESS = _BDA_IPv6_ADDRESS
PBDA_IPv6_ADDRESS = POINTER(_BDA_IPv6_ADDRESS)


class _BDA_IPv6_ADDRESS_LIST(ctypes.Structure):
    pass


BDA_IPv6_ADDRESS_LIST = _BDA_IPv6_ADDRESS_LIST
PBDA_IPv6_ADDRESS_LIST = POINTER(_BDA_IPv6_ADDRESS_LIST)


class _BDANODE_DESCRIPTOR(ctypes.Structure):
    pass


BDANODE_DESCRIPTOR = _BDANODE_DESCRIPTOR
PBDANODE_DESCRIPTOR = POINTER(_BDANODE_DESCRIPTOR)


class _BDA_TABLE_SECTION(ctypes.Structure):
    pass


BDA_TABLE_SECTION = _BDA_TABLE_SECTION
PBDA_TABLE_SECTION = POINTER(_BDA_TABLE_SECTION)


class _BDA_DISEQC_SEND(ctypes.Structure):
    pass


BDA_DISEQC_SEND = _BDA_DISEQC_SEND
PBDA_DISEQC_SEND = POINTER(_BDA_DISEQC_SEND)


class _BDA_DISEQC_RESPONSE(ctypes.Structure):
    pass


BDA_DISEQC_RESPONSE = _BDA_DISEQC_RESPONSE
PBDA_DISEQC_RESPONSE = POINTER(_BDA_DISEQC_RESPONSE)


class PID_MAP(ctypes.Structure):
    pass


class _BDA_PID_MAP(ctypes.Structure):
    pass


BDA_PID_MAP = _BDA_PID_MAP
PBDA_PID_MAP = POINTER(_BDA_PID_MAP)


class _BDA_PID_UNMAP(ctypes.Structure):
    pass


BDA_PID_UNMAP = _BDA_PID_UNMAP
PBDA_PID_UNMAP = POINTER(_BDA_PID_UNMAP)


class _BDA_CA_MODULE_UI(ctypes.Structure):
    pass


BDA_CA_MODULE_UI = _BDA_CA_MODULE_UI
PBDA_CA_MODULE_UI = POINTER(_BDA_CA_MODULE_UI)


class _BDA_PROGRAM_PID_LIST(ctypes.Structure):
    pass


BDA_PROGRAM_PID_LIST = _BDA_PROGRAM_PID_LIST
PBDA_PROGRAM_PID_LIST = POINTER(_BDA_PROGRAM_PID_LIST)


class _BDA_DRM_DRMSTATUS(ctypes.Structure):
    pass


BDA_DRM_DRMSTATUS = _BDA_DRM_DRMSTATUS
PBDA_DRM_DRMSTATUS = POINTER(_BDA_DRM_DRMSTATUS)


class _BDA_WMDRM_STATUS(ctypes.Structure):
    pass


BDA_WMDRM_STATUS = _BDA_WMDRM_STATUS
PBDA_WMDRM_STATUS = POINTER(_BDA_WMDRM_STATUS)


class _BDA_WMDRM_KEYINFOLIST(ctypes.Structure):
    pass


BDA_WMDRM_KEYINFOLIST = _BDA_WMDRM_KEYINFOLIST
PBDA_WMDRM_KEYINFOLIST = POINTER(_BDA_WMDRM_KEYINFOLIST)


class _BDA_BUFFER(ctypes.Structure):
    pass


BDA_BUFFER = _BDA_BUFFER
PBDA_BUFFER = POINTER(_BDA_BUFFER)


class _BDA_WMDRM_RENEWLICENSE(ctypes.Structure):
    pass


BDA_WMDRM_RENEWLICENSE = _BDA_WMDRM_RENEWLICENSE
PBDA_WMDRM_RENEWLICENSE = POINTER(_BDA_WMDRM_RENEWLICENSE)


class _BDA_WMDRMTUNER_PIDPROTECTION(ctypes.Structure):
    pass


BDA_WMDRMTUNER_PIDPROTECTION = _BDA_WMDRMTUNER_PIDPROTECTION
PBDA_WMDRMTUNER_PIDPROTECTION = POINTER(_BDA_WMDRMTUNER_PIDPROTECTION)


class _BDA_WMDRMTUNER_PURCHASEENTITLEMENT(ctypes.Structure):
    pass


BDA_WMDRMTUNER_PURCHASEENTITLEMENT = _BDA_WMDRMTUNER_PURCHASEENTITLEMENT
PBDA_WMDRMTUNER_PURCHASEENTITLEMENT = POINTER(_BDA_WMDRMTUNER_PURCHASEENTITLEMENT)


class _BDA_TUNER_TUNERSTATE(ctypes.Structure):
    pass


BDA_TUNER_TUNERSTATE = _BDA_TUNER_TUNERSTATE
PBDA_TUNER_TUNERSTATE = POINTER(_BDA_TUNER_TUNERSTATE)


class _BDA_TUNER_DIAGNOSTICS(ctypes.Structure):
    pass


BDA_TUNER_DIAGNOSTICS = _BDA_TUNER_DIAGNOSTICS
PBDA_TUNER_DIAGNOSTICS = POINTER(_BDA_TUNER_DIAGNOSTICS)


class _BDA_STRING(ctypes.Structure):
    pass


BDA_STRING = _BDA_STRING
PBDA_STRING = POINTER(_BDA_STRING)


class _BDA_SCAN_CAPABILTIES(ctypes.Structure):
    pass


BDA_SCAN_CAPABILTIES = _BDA_SCAN_CAPABILTIES
PBDA_SCAN_CAPABILTIES = POINTER(_BDA_SCAN_CAPABILTIES)


class _BDA_SCAN_STATE(ctypes.Structure):
    pass


BDA_SCAN_STATE = _BDA_SCAN_STATE
PBDA_SCAN_STATE = POINTER(_BDA_SCAN_STATE)


class _BDA_SCAN_START(ctypes.Structure):
    pass


BDA_SCAN_START = _BDA_SCAN_START
PBDA_SCAN_START = POINTER(_BDA_SCAN_START)


class _BDA_GDDS_DATATYPE(ctypes.Structure):
    pass


BDA_GDDS_DATATYPE = _BDA_GDDS_DATATYPE
P_BDA_GDDS_DATATYPE = POINTER(_BDA_GDDS_DATATYPE)


class _BDA_GDDS_DATA(ctypes.Structure):
    pass


BDA_GDDS_DATA = _BDA_GDDS_DATA
P_BDA_GDDS_DATA = POINTER(_BDA_GDDS_DATA)


class _BDA_USERACTIVITY_INTERVAL(ctypes.Structure):
    pass


BDA_USERACTIVITY_INTERVAL = _BDA_USERACTIVITY_INTERVAL
P_BDA_USERACTIVITY_INTERVAL = POINTER(_BDA_USERACTIVITY_INTERVAL)


class _BDA_CAS_CHECK_ENTITLEMENTTOKEN(ctypes.Structure):
    pass


BDA_CAS_CHECK_ENTITLEMENTTOKEN = _BDA_CAS_CHECK_ENTITLEMENTTOKEN
PBDA_CAS_CHECK_ENTITLEMENTTOKEN = POINTER(_BDA_CAS_CHECK_ENTITLEMENTTOKEN)


class _BDA_CAS_CLOSE_MMIDIALOG(ctypes.Structure):
    pass


BDA_CAS_CLOSE_MMIDIALOG = _BDA_CAS_CLOSE_MMIDIALOG
PBDA_CAS_CLOSE_MMIDIALOG = POINTER(_BDA_CAS_CLOSE_MMIDIALOG)


class _BDA_CAS_REQUESTTUNERDATA(ctypes.Structure):
    pass


BDA_CAS_REQUESTTUNERDATA = _BDA_CAS_REQUESTTUNERDATA
PBDA_CAS_REQUESTTUNERDATA = POINTER(_BDA_CAS_REQUESTTUNERDATA)


class _BDA_CAS_OPENMMIDATA(ctypes.Structure):
    pass


BDA_CAS_OPENMMIDATA = _BDA_CAS_OPENMMIDATA
PBDA_CAS_OPENMMIDATA = POINTER(_BDA_CAS_OPENMMIDATA)


class _BDA_CAS_CLOSEMMIDATA(ctypes.Structure):
    pass


BDA_CAS_CLOSEMMIDATA = _BDA_CAS_CLOSEMMIDATA
PBDA_CAS_CLOSEMMIDATA = POINTER(_BDA_CAS_CLOSEMMIDATA)


class _BDA_ISDBCAS_REQUESTHEADER(ctypes.Structure):
    pass


BDA_ISDBCAS_REQUESTHEADER = _BDA_ISDBCAS_REQUESTHEADER
PBDA_ISDBCAS_REQUESTHEADER = POINTER(_BDA_ISDBCAS_REQUESTHEADER)


class _BDA_ISDBCAS_RESPONSEDATA(ctypes.Structure):
    pass


BDA_ISDBCAS_RESPONSEDATA = _BDA_ISDBCAS_RESPONSEDATA
PBDA_ISDBCAS_RESPONSEDATA = POINTER(_BDA_ISDBCAS_RESPONSEDATA)


class _BDA_ISDBCAS_EMG_REQ(ctypes.Structure):
    pass


BDA_ISDBCAS_EMG_REQ = _BDA_ISDBCAS_EMG_REQ
PBDA_ISDBCAS_EMG_REQ = POINTER(_BDA_ISDBCAS_EMG_REQ)


class _BDA_MUX_PIDLISTITEM(ctypes.Structure):
    pass


BDA_MUX_PIDLISTITEM = _BDA_MUX_PIDLISTITEM
PBDA_MUX_PIDLISTITEM = POINTER(_BDA_MUX_PIDLISTITEM)


class _BDA_TS_SELECTORINFO(ctypes.Structure):
    pass


BDA_TS_SELECTORINFO = _BDA_TS_SELECTORINFO
PBDA_TS_SELECTORINFO = POINTER(_BDA_TS_SELECTORINFO)


class _BDA_TS_SELECTORINFO_ISDBS_EXT(ctypes.Structure):
    pass


BDA_TS_SELECTORINFO_ISDBS_EXT = _BDA_TS_SELECTORINFO_ISDBS_EXT
PBDA_TS_SELECTORINFO_ISDBS_EXT = POINTER(_BDA_TS_SELECTORINFO_ISDBS_EXT)


class _BDA_DVBT2_L1_SIGNALLING_DATA(ctypes.Structure):
    pass


BDA_DVBT2_L1_SIGNALLING_DATA = _BDA_DVBT2_L1_SIGNALLING_DATA
PBDA_DVBT2_L1_SIGNALLING_DATA = POINTER(_BDA_DVBT2_L1_SIGNALLING_DATA)


class _BDA_RATING_PINRESET(ctypes.Structure):
    pass


BDA_RATING_PINRESET = _BDA_RATING_PINRESET
PBDA_RATING_PINRESET = POINTER(_BDA_RATING_PINRESET)


class _MPEG2_TRANSPORT_STRIDE(ctypes.Structure):
    pass


MPEG2_TRANSPORT_STRIDE = _MPEG2_TRANSPORT_STRIDE
PMPEG2_TRANSPORT_STRIDE = POINTER(_MPEG2_TRANSPORT_STRIDE)


class _BDA_SIGNAL_TIMEOUTS(ctypes.Structure):
    pass


BDA_SIGNAL_TIMEOUTS = _BDA_SIGNAL_TIMEOUTS
PBDA_SIGNAL_TIMEOUTS = POINTER(_BDA_SIGNAL_TIMEOUTS)




# ----------------------------------------------------------------------------
# File: BDATypes.h
# Desc: Typedefs and enums needed by both the WDM drivers and the user mode
# COM interfaces.
# Copyright (c) 1999 - 2004, Microsoft Corporation. All rights reserved.
# ----------------------------------------------------------------------------
if not defined(_BDATYPES_):
    _BDATYPES_ = 1

    # not not not not do not pragma once, we use this file
    # twice(once for native and once for mgd) in managed interop
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        from pyWinAPI.shared.exposeenums2managed_h import * # NOQA

        # Utility Macros
        MIN_DIMENSION = 1

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA Topology Structures
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        if not defined(MANAGED_ENUMS):
            _BDA_TEMPLATE_CONNECTION._fields_ = [
                ('FromNodeType', ULONG),
                ('FromNodePinType', ULONG),
                ('ToNodeType', ULONG),
                ('ToNodePinType', ULONG),
            ]

            _BDA_TEMPLATE_PIN_JOINT._fields_ = [
                ('uliTemplateConnection', ULONG),
                ('ulcInstancesMax', ULONG),
            ]
        # END IF


        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA Events
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # In-band Event IDs
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =

        class BDA_EVENT_ID(ENUM):
            BDA_EVENT_SIGNAL_LOSS = 0
            BDA_EVENT_SIGNAL_LOCK = 1
            BDA_EVENT_DATA_START = 2
            BDA_EVENT_DATA_STOP = 3
            BDA_EVENT_CHANNEL_ACQUIRED = 4
            BDA_EVENT_CHANNEL_LOST = 5
            BDA_EVENT_CHANNEL_SOURCE_CHANGED = 6
            BDA_EVENT_CHANNEL_ACTIVATED = 7
            BDA_EVENT_CHANNEL_DEACTIVATED = 8
            BDA_EVENT_SUBCHANNEL_ACQUIRED = 9
            BDA_EVENT_SUBCHANNEL_LOST = 10
            BDA_EVENT_SUBCHANNEL_SOURCE_CHANGED = 11
            BDA_EVENT_SUBCHANNEL_ACTIVATED = 12
            BDA_EVENT_SUBCHANNEL_DEACTIVATED = 13
            BDA_EVENT_ACCESS_GRANTED = 14
            BDA_EVENT_ACCESS_DENIED = 15
            BDA_EVENT_OFFER_EXTENDED = 16
            BDA_EVENT_PURCHASE_COMPLETED = 17
            BDA_EVENT_SMART_CARD_INSERTED = 18
            BDA_EVENT_SMART_CARD_REMOVED = 19


        PBDA_EVENT_ID = POINTER(BDA_EVENT_ID)


        # KSSTREAM_HEADER extensions for BDA
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        if not defined(MANAGED_ENUMS):
            # Size of this extended header
            tagKS_BDA_FRAME_INFO._fields_ = [
                ('ExtendedHeaderSize', ULONG),
                ('dwFrameFlags', DWORD),
                ('ulEvent', ULONG),
                ('ulChannelNumber', ULONG),
                ('ulSubchannelNumber', ULONG),
                ('ulReason', ULONG),
            ]

            # ------------------------------------------------------------
            # BDA Network Ethernet Filter Property Set
            # {71985F43-1CA1-11d3-9CC8-00C04F7971E0}
            _BDA_ETHERNET_ADDRESS._fields_ = [
                ('rgbAddress', BYTE * 6),
            ]

            _BDA_ETHERNET_ADDRESS_LIST._fields_ = [
                ('ulcAddresses', ULONG),
                ('rgAddressl', BDA_ETHERNET_ADDRESS * MIN_DIMENSION),
            ]
        # END IF


        class BDA_MULTICAST_MODE(ENUM):
            BDA_PROMISCUOUS_MULTICAST = 0
            BDA_FILTERED_MULTICAST = 1
            BDA_NO_MULTICAST = 2


        PBDA_MULTICAST_MODE = POINTER(BDA_MULTICAST_MODE)
        # ------------------------------------------------------------
        # BDA Network IPv4 Filter Property Set
        # {71985F44-1CA1-11d3-9CC8-00C04F7971E0}
        if not defined(MANAGED_ENUMS):
            _BDA_IPv4_ADDRESS._fields_ = [
                ('rgbAddress', BYTE * 4),
            ]

            _BDA_IPv4_ADDRESS_LIST._fields_ = [
                ('ulcAddresses', ULONG),
                ('rgAddressl', BDA_IPv4_ADDRESS * MIN_DIMENSION),
            ]

            # ------------------------------------------------------------
            # BDA Network IPv4 Filter Property Set
            # {E1785A74-2A23-4fb3-9245-A8F88017EF33}
            _BDA_IPv6_ADDRESS._fields_ = [
                ('rgbAddress', BYTE * 6),
            ]

            _BDA_IPv6_ADDRESS_LIST._fields_ = [
                ('ulcAddresses', ULONG),
                ('rgAddressl', BDA_IPv6_ADDRESS * MIN_DIMENSION),
            ]
        # END IF


        # ------------------------------------------------------------
        # BDA Signal Property Set
        # {D2F1644B-B409-11d2-BC69-00A0C9EE9E16}
        class BDA_SIGNAL_STATE(ENUM):
            BDA_SIGNAL_UNAVAILABLE = 0
            BDA_SIGNAL_INACTIVE = 1
            BDA_SIGNAL_ACTIVE = 2


        PBDA_SIGNAL_STATE = POINTER(BDA_SIGNAL_STATE)

        # ------------------------------------------------------------
        # BDA Change Sync Method Set
        # {FD0A5AF3-B41D-11d2-9C95-00C04F7971E0}
        class BDA_CHANGE_STATE(ENUM):
            BDA_CHANGES_COMPLETE = 0
            BDA_CHANGES_PENDING = 1


        PBDA_CHANGE_STATE = POINTER(BDA_CHANGE_STATE)

        # ------------------------------------------------------------
        # BDA Device Configuration Method Set
        # {71985F45-1CA1-11d3-9CC8-00C04F7971E0}


        # ------------------------------------------------------------
        # BDA Topology Property Set
        # {A14EE835-0A23-11d3-9CC7-00C04F7971E0}


        if not defined(MANAGED_ENUMS):
            _BDANODE_DESCRIPTOR._fields_ = [
                # The node type as it is used
                ('ulBdaNodeType', ULONG),
                # GUID from BdaMedia.h describing
                ('guidFunction', GUID),
                # GUID that can be use to look up
                ('guidName', GUID),
            ]

            # ------------------------------------------------------------
            # BDA Void Transform Property Set
            # {71985F46-1CA1-11d3-9CC8-00C04F7971E0}
            # ------------------------------------------------------------
            # BDA Null Transform Property Set
            # {DDF15B0D-BD25-11d2-9CA0-00C04F7971E0}
            # ------------------------------------------------------------
            # BDA Frequency Filter Property Set
            # {71985F47-1CA1-11d3-9CC8-00C04F7971E0}
            # ------------------------------------------------------------
            # BDA Autodemodulate Property Set
            # {DDF15B12-BD25-11d2-9CA0-00C04F7971E0}
            # ------------------------------------------------------------
            # BDA Table Section Property Set
            # {516B99C5-971C-4aaf-B3F3-D9FDA8A15E16}
            _BDA_TABLE_SECTION._fields_ = [
                ('ulPrimarySectionId', ULONG),
                ('ulSecondarySectionId', ULONG),
                ('ulcbSectionLength', ULONG),
                ('argbSectionData', ULONG * MIN_DIMENSION),
            ]
        # END IF


        if not defined(MANAGED_ENUMS):
            # ------------------------------------------------------------
            # BDA Diseq Command Property Set
            # {F84E2AB0-3C6B-45e3-A0FC-8669D4B81F11}
            _BDA_DISEQC_SEND._fields_ = [
                ('ulRequestId', ULONG),
                ('ulPacketLength', ULONG),
                ('argbPacketData', BYTE * 8),
            ]

            _BDA_DISEQC_RESPONSE._fields_ = [
                ('ulRequestId', ULONG),
                ('ulPacketLength', ULONG),
                ('argbPacketData', BYTE * 8),
            ]
        # END IF


        # ------------------------------------------------------------
        # BDA PID Filter Property Set
        # {D0A67D65-08DF-4fec-8533-E5B550410B85}
        # ---------------------------------------------------------------------
        # From IEnumPIDMap interface
        # ---------------------------------------------------------------------


        class MEDIA_SAMPLE_CONTENT(ENUM):
            # complete TS packet e.g. pass-through mode
            MEDIA_TRANSPORT_PACKET = 0
            # PES payloads; audio/video only
            MEDIA_ELEMENTARY_STREAM = 1
            # PAT, PMT, CAT, Private
            MEDIA_MPEG2_PSI = 2
            # gathered TS packet payloads (PES packets, etc...)
            MEDIA_TRANSPORT_PAYLOAD = 3


        if not defined(MANAGED_ENUMS):
            PID_MAP._fields_ = [
                ('ulPID', ULONG),
                ('MediaSampleContent', MEDIA_SAMPLE_CONTENT),
            ]

            _BDA_PID_MAP._fields_ = [
                ('MediaSampleContent', MEDIA_SAMPLE_CONTENT),
                ('ulcPIDs', ULONG),
                ('aulPIDs', ULONG * MIN_DIMENSION),
            ]

            _BDA_PID_UNMAP._fields_ = [
                ('ulcPIDs', ULONG),
                ('aulPIDs', ULONG * MIN_DIMENSION),
            ]

            # ------------------------------------------------------------
            # BDA CA Property Set
            # {B0693766-5278-4ec6-B9E1-3CE40560EF5A}
            _BDA_CA_MODULE_UI._fields_ = [
                ('ulFormat', ULONG),
                ('ulbcDesc', ULONG),
                ('ulDesc', ULONG * MIN_DIMENSION),
            ]

            _BDA_PROGRAM_PID_LIST._fields_ = [
                ('ulProgramNumber', ULONG),
                ('ulcPIDs', ULONG),
                ('ulPID', ULONG * MIN_DIMENSION),
            ]
        # END IF


        # ------------------------------------------------------------
        # BDA CA Event Set
        # {488C4CCC-B768-4129-8EB1-B00A071F9068}
        if not defined(MANAGED_ENUMS):
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA RESULT parameter definition
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            PBDARESULT = LONG

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # BDA_DRM_STATUS used by the DRMService
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_DRM_DRMSTATUS._fields_ = [
                ('lResult', PBDARESULT),
                ('DRMuuid', GUID),
                ('ulDrmUuidListStringSize', ULONG),
                ('argbDrmUuidListString', GUID * MIN_DIMENSION),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA_WMDRM and PBDA_WMDRMTuner structures
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_WMDRM_STATUS._fields_ = [
                ('lResult', PBDARESULT),
                ('ulMaxCaptureTokenSize', ULONG),
                ('uMaxStreamingPid', ULONG),
                ('ulMaxLicense', ULONG),
                ('ulMinSecurityLevel', ULONG),
                ('ulRevInfoSequenceNumber', ULONG),
                ('ulRevInfoIssuedTime', ULONGLONG),
                ('ulRevListVersion', ULONG),
                ('ulRevInfoTTL', ULONG),
                ('ulState', ULONG),
            ]

            _BDA_WMDRM_KEYINFOLIST._fields_ = [
                ('lResult', PBDARESULT),
                ('ulKeyuuidBufferLen', ULONG),
                ('argKeyuuidBuffer', GUID * MIN_DIMENSION),
            ]

            _BDA_BUFFER._fields_ = [
                ('lResult', PBDARESULT),
                ('ulBufferSize', ULONG),
                ('argbBuffer', BYTE * MIN_DIMENSION),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - DRM structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_WMDRM_RENEWLICENSE._fields_ = [
                ('lResult', PBDARESULT),
                ('ulDescrambleStatus', ULONG),
                ('ulXmrLicenseOutputLength', ULONG),
                # License and Entitlement Token Buffer
                ('argbXmrLicenceOutputBuffer', BYTE * MIN_DIMENSION),
            ]

            _BDA_WMDRMTUNER_PIDPROTECTION._fields_ = [
                ('lResult', PBDARESULT),
                ('uuidKeyID', GUID),
            ]

            _BDA_WMDRMTUNER_PURCHASEENTITLEMENT._fields_ = [
                ('lResult', PBDARESULT),
                ('ulDescrambleStatus', ULONG),
                ('ulCaptureTokenLength', ULONG),
                ('argbCaptureTokenBuffer', BYTE * MIN_DIMENSION),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - TUNER structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_TUNER_TUNERSTATE._fields_ = [
                ('lResult', PBDARESULT),
                ('ulTuneLength', ULONG),
                ('argbTuneData', BYTE * MIN_DIMENSION),
            ]

            _BDA_TUNER_DIAGNOSTICS._fields_ = [
                ('lResult', PBDARESULT),
                ('ulSignalLevel', ULONG),
                ('ulSignalLevelQuality', ULONG),
                ('ulSignalNoiseRatio', ULONG),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - STRING structure used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_STRING._fields_ = [
                ('lResult', PBDARESULT),
                ('ulStringSize', ULONG),
                ('argbString', BYTE * MIN_DIMENSION),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - SCANNING structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_SCAN_CAPABILTIES._fields_ = [
                ('lResult', PBDARESULT),
                ('ul64AnalogStandardsSupported', UINT64),
            ]

            _BDA_SCAN_STATE._fields_ = [
                ('lResult', PBDARESULT),
                ('ulSignalLock', ULONG),
                ('ulSecondsLeft', ULONG),
                ('ulCurrentFrequency', ULONG),
            ]

            _BDA_SCAN_START._fields_ = [
                ('lResult', PBDARESULT),
                ('LowerFrequency', ULONG),
                ('HigerFrequency', ULONG),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - GUIDE DATA structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_GDDS_DATATYPE._fields_ = [
                ('lResult', PBDARESULT),
                ('uuidDataType', GUID),
            ]

            _BDA_GDDS_DATA._fields_ = [
                ('lResult', PBDARESULT),
                ('ulDataLength', ULONG),
                ('ulPercentageProgress', ULONG),
                ('argbData', BYTE * MIN_DIMENSION),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - USER ACTIVITY structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_USERACTIVITY_INTERVAL._fields_ = [
                ('lResult', PBDARESULT),
                ('ulActivityInterval', ULONG),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - CAS structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            _BDA_CAS_CHECK_ENTITLEMENTTOKEN._fields_ = [
                ('lResult', PBDARESULT),
                ('ulDescrambleStatus', ULONG),
            ]

            _BDA_CAS_CLOSE_MMIDIALOG._fields_ = [
                ('lResult', PBDARESULT),
                ('SessionResult', ULONG),
            ]

            _BDA_CAS_REQUESTTUNERDATA._fields_ = [
                ('ucRequestPriority', UCHAR),
                ('ucRequestReason', UCHAR),
                ('ucRequestConsequences', UCHAR),
                ('ulEstimatedTime', ULONG),
            ]

            _BDA_CAS_OPENMMIDATA._fields_ = [
                ('ulDialogNumber', ULONG),
                ('ulDialogRequest', ULONG),
                ('uuidDialogType', GUID),
                ('usDialogDataLength', USHORT),
                ('argbDialogData', BYTE * MIN_DIMENSION),
            ]

            _BDA_CAS_CLOSEMMIDATA._fields_ = [
                ('ulDialogNumber', ULONG),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - ISDB CAS structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =

            class ISDBCAS_REQUEST_ID(ENUM):
                ISDBCAS_REQUEST_ID_EMG = 0x38
                ISDBCAS_REQUEST_ID_EMD = 0x3A


            _BDA_ISDBCAS_REQUESTHEADER._fields_ = [
                # EMD/EMG
                ('bInstruction', BYTE),
                # future use
                ('bReserved', BYTE * 3),
                # byte size of argbIsdbCommand
                ('ulDataLength', ULONG),
                ('argbIsdbCommand', BYTE * MIN_DIMENSION),
            ]

            _BDA_ISDBCAS_RESPONSEDATA._fields_ = [
                ('lResult', PBDARESULT),
                ('ulRequestID', ULONG),
                ('ulIsdbStatus', ULONG),
                ('ulIsdbDataSize', ULONG),
                ('argbIsdbCommandData', BYTE * MIN_DIMENSION),
            ]

            _BDA_ISDBCAS_EMG_REQ._fields_ = [
                # 0x90
                ('bCLA', BYTE),
                # 0x38
                ('bINS', BYTE),
                # 0x00
                ('bP1', BYTE),
                # 0x00
                ('bP2', BYTE),
                # Following bytes - 1(LE)
                ('bLC', BYTE),
                # from EMM message packet
                ('bCardId', BYTE * 6),
                # from EMM message packet
                ('bProtocol', BYTE),
                # from EMM message packet
                ('bCABroadcasterGroupId', BYTE),
                # from EMM message packet
                ('bMessageControl', BYTE),
                # Last byte is reserved as 'LE'
                ('bMessageCode', BYTE * MIN_DIMENSION),
            ]

            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =
            # PBDA - MUX structures used in methods
            # == == == == == == == == == == == == == == == == == == == == ==
            # == == == == == == == == == =

            class MUX_PID_TYPE(ENUM):
                PID_OTHER = -1
                # PES payloads
                PID_ELEMENTARY_STREAM = 0
                # ISO 13818_1 Sections PAT, PMT, CAT, Private. Service
                # Information Sections e.g SDT, NIT, EIT, BAT
                PID_MPEG2_SECTION_PSI_SI = 1


            _BDA_MUX_PIDLISTITEM._fields_ = [
                # PID number of the stream
                ('usPIDNumber', USHORT),
                # associated Service Id, if applicable
                ('usProgramNumber', USHORT),
                # PID Type of the stream if applicable
                ('ePIDType', MUX_PID_TYPE),
            ]
        # END IF

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == =
        # BDA - TS Selector structures used in methods
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == =
        # | < -------------- bTSInfolength ---------------------. |
        # |         |
        # |    |      |
        # | BDA_TS_SELECTORINFO | BDA_TS_SELECTORINFO_ISDBS_EXT |
        # |    | (for ISDB-S extension)  |
        # |    |      |
        _BDA_TS_SELECTORINFO._fields_ = [
            # buffer length including extension
            ('bTSInfolength', BYTE),
            ('bReserved', BYTE * 2),
            # current type of tuning
            ('guidNetworkType', GUID),
            # number of usTSID
            ('bTSIDCount', BYTE),
            ('usTSID', USHORT * MIN_DIMENSION),
        ]

        _BDA_TS_SELECTORINFO_ISDBS_EXT._fields_ = [
            ('bTMCC', BYTE * 48),
        ]

        # DVB-T2 related L1 signalling information returned in
        # _GETTSINFORMATION
        _BDA_DVBT2_L1_SIGNALLING_DATA._fields_ = [
            ('L1Pre_TYPE', BYTE),
            ('L1Pre_BWT_S1_S2', BYTE),
            ('L1Pre_REPETITION_GUARD_PAPR', BYTE),
            ('L1Pre_MOD_COD_FEC', BYTE),
            ('L1Pre_POSTSIZE_INFO_PILOT', BYTE * 5),
            ('L1Pre_TX_ID_AVAIL', BYTE),
            ('L1Pre_CELL_ID', BYTE * 2),
            ('L1Pre_NETWORK_ID', BYTE * 2),
            ('L1Pre_T2SYSTEM_ID', BYTE * 2),
            ('L1Pre_NUM_T2_FRAMES', BYTE),
            ('L1Pre_NUM_DATA_REGENFLAG_L1POSTEXT', BYTE * 2),
            ('L1Pre_NUMRF_CURRENTRF_RESERVED', BYTE * 2),
            ('L1Pre_CRC32', BYTE * 4),
            ('L1PostData', BYTE * MIN_DIMENSION),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == =
        # PBDA - RATING structures used in methods
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == =
        _BDA_RATING_PINRESET._fields_ = [
            # Buffer size including a null termination
            ('bPinLength', BYTE),
            # Null terminated UTF8. Use empty string if disable pin
            ('argbNewPin', BYTE * MIN_DIMENSION),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == =
        # BDA Tuning Model enumerations
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == =
        # system type for particular DVB Tuning Space instance
        class DVBSystemType(ENUM):
            DVB_Cable = 0
            DVB_Terrestrial = 1
            DVB_Satellite = 2
            ISDB_Terrestrial = 3
            ISDB_Satellite = 4

        # ------------------------------------------------------------
        # BDA Channel Tune Request
        # ------------------------------------------------------------
        class BDA_Channel(ENUM):
            BDA_UNDEFINED_CHANNEL = -1


        # BDA Component(substream)
        # Note: Persistent TS remember preferred component categories by their
        # number.
        # Please update the rgs files at multimedia\dshow\vidctl\msvidctl\res
        # and multimedia\dshow\vidctl\manifests\Video-TVVideoControl.man
        # accordingly
        # if the order/value changes.
        # Also make sure ehiProxy.asmmeta, ehiVidCtl.asmmeta and
        # bdatunepia.asmmeta
        # are properly updated.
        class ComponentCategory(ENUM):
            CategoryNotSet = -1
            CategoryOther = 0
            CategoryVideo = 1
            CategoryAudio = 2
            CategoryText = 3
            CategorySubtitles = 4
            CategoryCaptions = 5
            CategorySuperimpose = 6
            CategoryData = 7
            CATEGORY_COUNT = 8

        # Component Status
        class ComponentStatus(ENUM):
            StatusActive = 0
            StatusInactive = 1
            StatusUnavailable = 2

        # ------------------------------------------------------------
        # BDA MPEG2 Component Type
        class MPEG2StreamType(ENUM):
            BDA_UNITIALIZED_MPEG2STREAMTYPE = -1
            Reserved1                       = 0x00
            ISO_IEC_11172_2_VIDEO           = 0x01
            ISO_IEC_13818_2_VIDEO           = 0x02
            ISO_IEC_11172_3_AUDIO           = 0x03
            ISO_IEC_13818_3_AUDIO           = 0x04
            ISO_IEC_13818_1_PRIVATE_SECTION = 0x05
            ISO_IEC_13818_1_PES             = 0x06
            ISO_IEC_13522_MHEG              = 0x07
            ANNEX_A_DSM_CC                  = 0x08
            ITU_T_REC_H_222_1               = 0x09
            ISO_IEC_13818_6_TYPE_A          = 0x0A
            ISO_IEC_13818_6_TYPE_B          = 0x0B
            ISO_IEC_13818_6_TYPE_C          = 0x0C
            ISO_IEC_13818_6_TYPE_D          = 0x0D
            ISO_IEC_13818_1_AUXILIARY       = 0x0E
            ISO_IEC_13818_7_AUDIO           = 0x0F
            ISO_IEC_14496_2_VISUAL          = 0x10
            ISO_IEC_14496_3_AUDIO           = 0x11
            ISO_IEC_14496_1_IN_PES          = 0x12
            ISO_IEC_14496_1_IN_SECTION      = 0x13
            ISO_IEC_13818_6_DOWNLOAD        = 0x14
            METADATA_IN_PES                 = 0x15
            METADATA_IN_SECTION             = 0x16
            METADATA_IN_DATA_CAROUSEL       = 0x17
            METADATA_IN_OBJECT_CAROUSEL     = 0x18
            METADATA_IN_DOWNLOAD_PROTOCOL   = 0x19
            IRPM_STREAMM                    = 0x1A
            ITU_T_H264                      = 0x1B
            ISO_IEC_13818_1_RESERVED        = 0x1C # continues until 0x7F
            USER_PRIVATE                    = 0x10 # standard says 0x80, retaining for backwards compatibility
            HEVC_VIDEO_OR_TEMPORAL_VIDEO    = 0x24
            HEVC_TEMPORAL_VIDEO_SUBSET      = 0x25
            ISO_IEC_USER_PRIVATE            = 0x80
            DOLBY_AC3_AUDIO                 = 0x81
            DOLBY_DIGITAL_PLUS_AUDIO_ATSC   = 0x87

        # ------------------------------------------------------------
        # mpeg-2 transport stride format block; associated with media
        # types MEDIATYPE_Stream/MEDIASUBTYPE_MPEG2_TRANSPORT_STRIDE;
        # *all* format blocks associated with above media type *must*
        # start with the MPEG2_TRANSPORT_STRIDE structure
        if not defined(MANAGED_ENUMS):
            _MPEG2_TRANSPORT_STRIDE._fields_ = [
                ('dwOffset', DWORD),
                ('dwPacketLength', DWORD),
                ('dwStride', DWORD),
            ]
        # END IF


        # ------------------------------------------------------------
        # BDA ATSC Component Type
        # ATSC made AC3 Audio a descriptor instead of
        # defining a user private stream type.
        class ATSCComponentTypeFlags(FLAGS):
            # bit flags for various component type properties
            ATSCCT_AC3 = 0x00000001

        # ------------------------------------------------------------
        # BDA Locators
        class BinaryConvolutionCodeRate(ENUM):
            BDA_BCC_RATE_NOT_SET = -1
            BDA_BCC_RATE_NOT_DEFINED = 0
            BDA_BCC_RATE_1_2 = 1,      # 1/2
            BDA_BCC_RATE_2_3 = 2       # 2/3
            BDA_BCC_RATE_3_4 = 3       # 3/4
            BDA_BCC_RATE_3_5 = 4       # 3/5
            BDA_BCC_RATE_4_5 = 5       # 4/5
            BDA_BCC_RATE_5_6 = 6       # 5/6
            BDA_BCC_RATE_5_11 = 7      # 5/11
            BDA_BCC_RATE_7_8 = 8       # 7/8
            BDA_BCC_RATE_1_4 = 9       # 1/4
            BDA_BCC_RATE_1_3 = 10      # 1/3
            BDA_BCC_RATE_2_5 = 11      # 2/5
            BDA_BCC_RATE_6_7 = 12      # 6/7
            BDA_BCC_RATE_8_9 = 13      # 8/9
            BDA_BCC_RATE_9_10 = 14     # 9/10
            BDA_BCC_RATE_MAX = 15


        class  FECMethod(ENUM):
            BDA_FEC_METHOD_NOT_SET = -1
            BDA_FEC_METHOD_NOT_DEFINED = 0
            BDA_FEC_VITERBI = 1     # FEC is a Viterbi Binary Convolution.
            BDA_FEC_RS_204_188 = 2  # The FEC is Reed-Solomon 204/188 (outer FEC)
            BDA_FEC_LDPC = 3        # Low Density Parity Check error correction code
            BDA_FEC_BCH = 4         # Bose-Chaudhuri-Hocquenghem multiple error correction binary block code
            BDA_FEC_RS_147_130 = 5  # The FEC is Reed-Solomon 147/130 (outer FEC) DirecTV-DSS
            BDA_FEC_MAX = 6


        class ModulationType(ENUM):
            BDA_MOD_NOT_SET = -1
            BDA_MOD_NOT_DEFINED = 0
            BDA_MOD_16QAM = 1
            BDA_MOD_32QAM = 2
            BDA_MOD_64QAM = 3
            BDA_MOD_80QAM = 4
            BDA_MOD_96QAM = 5
            BDA_MOD_112QAM = 6
            BDA_MOD_128QAM = 7
            BDA_MOD_160QAM = 8
            BDA_MOD_192QAM = 9
            BDA_MOD_224QAM = 10
            BDA_MOD_256QAM = 11
            BDA_MOD_320QAM = 12
            BDA_MOD_384QAM = 13
            BDA_MOD_448QAM = 14
            BDA_MOD_512QAM = 15
            BDA_MOD_640QAM = 16
            BDA_MOD_768QAM = 17
            BDA_MOD_896QAM = 18
            BDA_MOD_1024QAM = 19
            BDA_MOD_QPSK = 20             # Quadrature Phase Shift Keying (including backwards compatible mode)
            BDA_MOD_BPSK = 21             # Binary Phase Shift Keying
            BDA_MOD_OQPSK = 22            # Offset QPSK
            BDA_MOD_8VSB = 23             # 8-Level Vestigial Sideband
            BDA_MOD_16VSB = 24            # 16-Level Vestigial Sideband
            BDA_MOD_ANALOG_AMPLITUDE = 25 # std am
            BDA_MOD_ANALOG_FREQUENCY = 26 # std fm
            BDA_MOD_8PSK = 27             # 8 Phase Shift Keying (including backwards compatible mode)
            BDA_MOD_RF = 28 # analog TV (Video standards such as NTSC/PAL/SECAM specified in IAnalogLocator VideoStandard property)
            BDA_MOD_16APSK = 29           # DVB-S2 modulation 16-Level APSK
            BDA_MOD_32APSK = 30           # DVB-S2 modulation 32-Level APSK
            BDA_MOD_NBC_QPSK = 31         # Non-Backwards Compatible Quadrature Phase Shift Keying
            BDA_MOD_NBC_8PSK = 32         # Non-Backwards Compatible 8 Phase Shift Keying
            BDA_MOD_DIRECTV = 33          # DIRECTV DSS
            BDA_MOD_ISDB_T_TMCC = 34      # Automatic demodulation by Transmission and Multiplexing Configuration Control signal for ISDB-T
            BDA_MOD_ISDB_S_TMCC = 35      # Automatic demodulation by Transmission and Multiplexing Configuration Control signal for ISDB-S
            BDA_MOD_MAX = 36


        if defined(_MANAGED):
            class ScanModulationTypes(FLAGS):
                pass
        else:
            class ScanModulationTypes(FLAGS):
                pass

        # END IF

        ScanModulationTypes.BDA_SCAN_MOD_16QAM = 0x00000001
        ScanModulationTypes.BDA_SCAN_MOD_32QAM = 0x00000002
        ScanModulationTypes.BDA_SCAN_MOD_64QAM = 0x00000004
        ScanModulationTypes.BDA_SCAN_MOD_80QAM = 0x00000008
        ScanModulationTypes.BDA_SCAN_MOD_96QAM = 0x00000010
        ScanModulationTypes.BDA_SCAN_MOD_112QAM = 0x00000020
        ScanModulationTypes.BDA_SCAN_MOD_128QAM = 0x00000040
        ScanModulationTypes.BDA_SCAN_MOD_160QAM = 0x00000080
        ScanModulationTypes.BDA_SCAN_MOD_192QAM = 0x00000100
        ScanModulationTypes.BDA_SCAN_MOD_224QAM = 0x00000200
        ScanModulationTypes.BDA_SCAN_MOD_256QAM = 0x00000400
        ScanModulationTypes.BDA_SCAN_MOD_320QAM = 0x00000800
        ScanModulationTypes.BDA_SCAN_MOD_384QAM = 0x00001000
        ScanModulationTypes.BDA_SCAN_MOD_448QAM = 0x00002000
        ScanModulationTypes.BDA_SCAN_MOD_512QAM = 0x00004000
        ScanModulationTypes.BDA_SCAN_MOD_640QAM = 0x00008000
        ScanModulationTypes.BDA_SCAN_MOD_768QAM = 0x00010000
        ScanModulationTypes.BDA_SCAN_MOD_896QAM = 0x00020000
        ScanModulationTypes.BDA_SCAN_MOD_1024QAM = 0x00040000
        ScanModulationTypes.BDA_SCAN_MOD_QPSK = 0x00080000
        ScanModulationTypes.BDA_SCAN_MOD_BPSK = 0x00100000
        ScanModulationTypes.BDA_SCAN_MOD_OQPSK = 0x00200000
        ScanModulationTypes.BDA_SCAN_MOD_8VSB = 0x00400000
        ScanModulationTypes.BDA_SCAN_MOD_16VSB = 0x00800000
        ScanModulationTypes.BDA_SCAN_MOD_AM_RADIO = 0x01000000
        ScanModulationTypes.BDA_SCAN_MOD_FM_RADIO = 0x02000000
        ScanModulationTypes.BDA_SCAN_MOD_8PSK = 0x04000000
        ScanModulationTypes.BDA_SCAN_MOD_RF = 0x08000000 # analog TV
        ScanModulationTypesMask_MCE_DigitalCable = (
            ScanModulationTypes.BDA_MOD_64QAM |
            ScanModulationTypes.BDA_MOD_256QAM
        )
        ScanModulationTypes.ScanModulationTypesMask_MCE_TerrestrialATSC = (
            ScanModulationTypes.BDA_MOD_8VSB
        )
        ScanModulationTypes.ScanModulationTypesMask_MCE_AnalogTv = (
            ScanModulationTypes.BDA_MOD_RF
        )
        ScanModulationTypes.ScanModulationTypesMask_MCE_All_TV = 0xffffffff
        ScanModulationTypes.ScanModulationTypesMask_DVBC = (
            ScanModulationTypes.BDA_MOD_64QAM |
            ScanModulationTypes.BDA_SCAN_MOD_128QAM |
            ScanModulationTypes.BDA_MOD_256QAM
        )
        ScanModulationTypes.BDA_SCAN_MOD_16APSK = 0x10000000
        ScanModulationTypes.BDA_SCAN_MOD_32APSK = 0x20000000

        class SpectralInversion(ENUM):
            BDA_SPECTRAL_INVERSION_NOT_SET = -1
            BDA_SPECTRAL_INVERSION_NOT_DEFINED = 0
            BDA_SPECTRAL_INVERSION_AUTOMATIC = 1
            BDA_SPECTRAL_INVERSION_NORMAL = 2
            BDA_SPECTRAL_INVERSION_INVERTED = 3
            BDA_SPECTRAL_INVERSION_MAX = 4


        class Polarisation(ENUM):
            BDA_POLARISATION_NOT_SET = -1
            BDA_POLARISATION_NOT_DEFINED = 0
            BDA_POLARISATION_LINEAR_H = 1 # Linear horizontal polarisation
            BDA_POLARISATION_LINEAR_V = 2 # Linear vertical polarisation
            BDA_POLARISATION_CIRCULAR_L = 3 # Circular left polarisation
            BDA_POLARISATION_CIRCULAR_R = 4 # Circular right polarisation
            BDA_POLARISATION_MAX = 5


        class LNB_Source(ENUM):
            BDA_LNB_SOURCE_NOT_SET = -1
            BDA_LNB_SOURCE_NOT_DEFINED = 0
            BDA_LNB_SOURCE_A = 1
            BDA_LNB_SOURCE_B = 2
            BDA_LNB_SOURCE_C = 3
            BDA_LNB_SOURCE_D = 4
            BDA_LNB_SOURCE_MAX = 5


        class GuardInterval(ENUM):
            BDA_GUARD_NOT_SET = -1
            BDA_GUARD_NOT_DEFINED = 0
            BDA_GUARD_1_32 = 1 # Guard interval is 1/32
            BDA_GUARD_1_16 = 2 # Guard interval is 1/16
            BDA_GUARD_1_8 = 3 # Guard interval is 1/8
            BDA_GUARD_1_4 = 4 # Guard interval is 1/4
            BDA_GUARD_1_128 = 5 # Guard interval is 1/128 (DVB-T2)
            BDA_GUARD_19_128 = 6 # Guard interval is 19/128 (DVB-T2)
            BDA_GUARD_19_256 = 7 # Guard interval is 19/256 (DVB-T2)
            BDA_GUARD_MAX = 8


        class HierarchyAlpha(ENUM):
            BDA_HALPHA_NOT_SET = -1
            BDA_HALPHA_NOT_DEFINED = 0
            BDA_HALPHA_1 = 1 # Hierarchy alpha is 1.
            BDA_HALPHA_2 = 2 # Hierarchy alpha is 2.
            BDA_HALPHA_4 = 3 # Hierarchy alpha is 4.
            BDA_HALPHA_MAX = 4


        class TransmissionMode(ENUM):
            BDA_XMIT_MODE_NOT_SET = -1
            BDA_XMIT_MODE_NOT_DEFINED = 0
            BDA_XMIT_MODE_2K = 1 # Transmission uses 1705 carriers (use a 2K FFT)
            BDA_XMIT_MODE_8K = 2     # Transmission uses 6817 carriers (use an 8K FFT)
            BDA_XMIT_MODE_4K = 3
            BDA_XMIT_MODE_2K_INTERLEAVED = 4
            BDA_XMIT_MODE_4K_INTERLEAVED = 5
            BDA_XMIT_MODE_1K = 6    # DVB-T2 (use 1K FFT)
            BDA_XMIT_MODE_16K = 7   # DVB-T2 (use 16K FFT)
            BDA_XMIT_MODE_32K = 8   # DVB-T2 (use 32K FFT)
            BDA_XMIT_MODE_MAX = 9


        class RollOff(ENUM):
            BDA_ROLL_OFF_NOT_SET = -1
            BDA_ROLL_OFF_NOT_DEFINED = 0
            BDA_ROLL_OFF_20 = 1         # .20 Roll Off (DVB-S2 Only)
            BDA_ROLL_OFF_25 = 2             # .25 Roll Off (DVB-S2 Only)
            BDA_ROLL_OFF_35 = 3             # .35 Roll Off (DVB-S2 Only)
            BDA_ROLL_OFF_MAX = 4


        class Pilot(ENUM):
            BDA_PILOT_NOT_SET = -1
            BDA_PILOT_NOT_DEFINED = 0
            BDA_PILOT_OFF = 1           # Pilot Off (DVB-S2 Only)
            BDA_PILOT_ON = 2            # Pilot On  (DVB-S2 Only)
            BDA_PILOT_MAX = 3


        _BDA_SIGNAL_TIMEOUTS._fields_ = [
            ('ulCarrierTimeoutMs', ULONG),
            ('ulScanningTimeoutMs', ULONG),
            ('ulTuningTimeoutMs', ULONG),
        ]

        # Settings for Tuner Frequency
        class BDA_Frequency(ENUM):
            BDA_FREQUENCY_NOT_SET = -1
            BDA_FREQUENCY_NOT_DEFINED = 0


        # Settings for Tuner Range
        class BDA_Range(ENUM):
            BDA_RANGE_NOT_SET = -1
            BDA_RANGE_NOT_DEFINED = 0


        # Tuner range refers to the setting of LNB High/Low as well as the
        # selection of a satellite on a multiple satellite switch.
        # Settings for Tuner Channel Bandwidth
        class BDA_Channel_Bandwidth(ENUM):
            BDA_CHAN_BANDWITH_NOT_SET      = -1
            BDA_CHAN_BANDWITH_NOT_DEFINED  = 0


        # Settings for Tuner Frequency Multiplier
        class BDA_Frequency_Multiplier(ENUM):
            BDA_FREQUENCY_MULTIPLIER_NOT_SET = -1
            BDA_FREQUENCY_MULTIPLIER_NOT_DEFINED = 0


        class BDA_Comp_Flags(FLAGS):
            # equiv comparison rule overrides, default behavior is type specific
            BDACOMP_NOT_DEFINED              = 0x00000000
            BDACOMP_EXCLUDE_TS_FROM_TR       = 0x00000001 # never put TS in TR equiv comparison
            BDACOMP_INCLUDE_LOCATOR_IN_TR    = 0x00000002 # always include loc in TR equiv comparison
            BDACOMP_INCLUDE_COMPONENTS_IN_TR = 0x00000004 # always include components in TR equiv comparison


        class ApplicationTypeType(ENUM):
            SCTE28_ConditionalAccess = 0
            SCTE28_POD_Host_Binding_Information = 1
            SCTE28_IPService = 2
            SCTE28_NetworkInterface_SCTE55_2 = 3
            SCTE28_NetworkInterface_SCTE55_1 = 4
            SCTE28_CopyProtection = 5
            SCTE28_Diagnostic = 6
            SCTE28_Undesignated = 7
            SCTE28_Reserved = 8


        class BDA_CONDITIONALACCESS_REQUESTTYPE(ENUM):
            CONDITIONALACCESS_ACCESS_UNSPECIFIED = 0
            CONDITIONALACCESS_ACCESS_NOT_POSSIBLE = 1
            CONDITIONALACCESS_ACCESS_POSSIBLE = 2
            CONDITIONALACCESS_ACCESS_POSSIBLE_NO_STREAMING_DISRUPTION = 3


        class BDA_CONDITIONALACCESS_MMICLOSEREASON(ENUM):
            CONDITIONALACCESS_UNSPECIFIED = 0
            CONDITIONALACCESS_CLOSED_ITSELF = 1
            CONDITIONALACCESS_TUNER_REQUESTED_CLOSE = 2
            CONDITIONALACCESS_DIALOG_TIMEOUT = 3
            CONDITIONALACCESS_DIALOG_FOCUS_CHANGE = 4
            CONDITIONALACCESS_DIALOG_USER_DISMISSED = 5
            CONDITIONALACCESS_DIALOG_USER_NOT_AVAILABLE = 6


        class BDA_CONDITIONALACCESS_SESSION_RESULT(ENUM):
            CONDITIONALACCESS_SUCCESSFULL = 0
            CONDITIONALACCESS_ENDED_NOCHANGE = 1
            CONDITIONALACCESS_ABORTED = 2


        class BDA_DISCOVERY_STATE(ENUM):
            BDA_DISCOVERY_UNSPECIFIED = 0
            BDA_DISCOVERY_REQUIRED = 1
            BDA_DISCOVERY_COMPLETE = 2


        # Digital Demodulator for DVBT2 Physical Layer Pipe
        BDA_PLP_ID_NOT_SET = -1
        from pyWinAPI.shared.unexposeenums2managed_h import * # NOQA
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   not defined _BDATYPES_

# end of file -- bdatypes.h
