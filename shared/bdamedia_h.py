import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_KSMEDIA_ = None
_BDATYPES_ = None
_BDAMEDIA_ = None

class _KSP_BDA_NODE_PIN(ctypes.Structure):
    pass


KSP_BDA_NODE_PIN = _KSP_BDA_NODE_PIN
PKSP_BDA_NODE_PIN = POINTER(_KSP_BDA_NODE_PIN)


class _KSM_BDA_PIN(ctypes.Structure):
    pass


KSM_BDA_PIN = _KSM_BDA_PIN
PKSM_BDA_PIN = POINTER(_KSM_BDA_PIN)


class _KSM_BDA_PIN_PAIR(ctypes.Structure):
    pass


KSM_BDA_PIN_PAIR = _KSM_BDA_PIN_PAIR
PKSM_BDA_PIN_PAIR = POINTER(_KSM_BDA_PIN_PAIR)


class KSP_NODE_ESPID(ctypes.Structure):
    pass


PKSP_NODE_ESPID = POINTER(KSP_NODE_ESPID)


class _KSM_BDA_DEBUG_LEVEL(ctypes.Structure):
    pass


KSM_BDA_DEBUG_LEVEL = _KSM_BDA_DEBUG_LEVEL
PKSM_BDA_DEBUG_LEVEL = POINTER(_KSM_BDA_DEBUG_LEVEL)


class _BDA_DEBUG_DATA(ctypes.Structure):
    pass


BDA_DEBUG_DATA = _BDA_DEBUG_DATA


class _BDA_EVENT_DATA(ctypes.Structure):
    pass


BDA_EVENT_DATA = _BDA_EVENT_DATA
PBDA_EVENT_DATA = POINTER(_BDA_EVENT_DATA)


class _KSM_BDA_EVENT_COMPLETE(ctypes.Structure):
    pass


KSM_BDA_EVENT_COMPLETE = _KSM_BDA_EVENT_COMPLETE
PKSM_BDA_EVENT_COMPLETE = POINTER(_KSM_BDA_EVENT_COMPLETE)


class _KSM_BDA_DRM_SETDRM(ctypes.Structure):
    pass


KSM_BDA_DRM_SETDRM = _KSM_BDA_DRM_SETDRM
PKSM_BDA_DRM_SETDRM = POINTER(_KSM_BDA_DRM_SETDRM)


class _KSM_BDA_BUFFER(ctypes.Structure):
    pass


KSM_BDA_BUFFER = _KSM_BDA_BUFFER
PKSM_BDA_BUFFER = POINTER(_KSM_BDA_BUFFER)


class KSM_BDA_WMDRM_LICENSE(ctypes.Structure):
    pass


PKSM_BDA_WMDRM_LICENSE = POINTER(KSM_BDA_WMDRM_LICENSE)


class _KSM_BDA_WMDRM_RENEWLICENSE(ctypes.Structure):
    pass


KSM_BDA_WMDRM_RENEWLICENSE = _KSM_BDA_WMDRM_RENEWLICENSE
PKSM_BDA_WMDRM_RENEWLICENSE = POINTER(_KSM_BDA_WMDRM_RENEWLICENSE)


class _KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT(ctypes.Structure):
    pass


KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT = _KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT
PKSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT = POINTER(_KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT)


class _KSM_BDA_WMDRMTUNER_SETPIDPROTECTION(ctypes.Structure):
    pass


KSM_BDA_WMDRMTUNER_SETPIDPROTECTION = _KSM_BDA_WMDRMTUNER_SETPIDPROTECTION
PKSM_BDA_WMDRMTUNER_SETPIDPROTECTION = POINTER(_KSM_BDA_WMDRMTUNER_SETPIDPROTECTION)


class _KSM_BDA_WMDRMTUNER_GETPIDPROTECTION(ctypes.Structure):
    pass


KSM_BDA_WMDRMTUNER_GETPIDPROTECTION = _KSM_BDA_WMDRMTUNER_GETPIDPROTECTION
PKSM_BDA_WMDRMTUNER_GETPIDPROTECTION = POINTER(_KSM_BDA_WMDRMTUNER_GETPIDPROTECTION)


class _KSM_BDA_WMDRMTUNER_SYNCVALUE(ctypes.Structure):
    pass


KSM_BDA_WMDRMTUNER_SYNCVALUE = _KSM_BDA_WMDRMTUNER_SYNCVALUE
PKSM_BDA_WMDRMTUNER_SYNCVALUE = POINTER(_KSM_BDA_WMDRMTUNER_SYNCVALUE)


class _KSM_BDA_TUNER_TUNEREQUEST(ctypes.Structure):
    pass


KSM_BDA_TUNER_TUNEREQUEST = _KSM_BDA_TUNER_TUNEREQUEST
PKSM_BDA_TUNER_TUNEREQUEST = POINTER(_KSM_BDA_TUNER_TUNEREQUEST)


class _KSM_BDA_GPNV_GETVALUE(ctypes.Structure):
    pass


KSM_BDA_GPNV_GETVALUE = _KSM_BDA_GPNV_GETVALUE
PKSM_BDA_GPNV_GETVALUE = POINTER(_KSM_BDA_GPNV_GETVALUE)


class _KSM_BDA_GPNV_SETVALUE(ctypes.Structure):
    pass


KSM_BDA_GPNV_SETVALUE = _KSM_BDA_GPNV_SETVALUE
PKSM_BDA_GPNV_SETVALUE = POINTER(_KSM_BDA_GPNV_SETVALUE)


class _KSM_BDA_GPNV_NAMEINDEX(ctypes.Structure):
    pass


KSM_BDA_GPNV_NAMEINDEX = _KSM_BDA_GPNV_NAMEINDEX
PKSM_BDA_GPNV_NAMEINDEX = POINTER(_KSM_BDA_GPNV_NAMEINDEX)


class _KSM_BDA_SCAN_CAPABILTIES(ctypes.Structure):
    pass


KSM_BDA_SCAN_CAPABILTIES = _KSM_BDA_SCAN_CAPABILTIES
PKSM_BDA_SCAN_CAPABILTIES = POINTER(_KSM_BDA_SCAN_CAPABILTIES)


class _KSM_BDA_SCAN_FILTER(ctypes.Structure):
    pass


KSM_BDA_SCAN_FILTER = _KSM_BDA_SCAN_FILTER
PKSM_BDA_SCAN_FILTER = POINTER(_KSM_BDA_SCAN_FILTER)


class _KSM_BDA_SCAN_START(ctypes.Structure):
    pass


KSM_BDA_SCAN_START = _KSM_BDA_SCAN_START
PKSM_BDA_SCAN_START = POINTER(_KSM_BDA_SCAN_START)


class _KSM_BDA_GDDS_TUNEXMLFROMIDX(ctypes.Structure):
    pass


KSM_BDA_GDDS_TUNEXMLFROMIDX = _KSM_BDA_GDDS_TUNEXMLFROMIDX
PKSM_BDA_GDDS_TUNEXMLFROMIDX = POINTER(_KSM_BDA_GDDS_TUNEXMLFROMIDX)


class _KSM_BDA_GDDS_SERVICEFROMTUNEXML(ctypes.Structure):
    pass


KSM_BDA_GDDS_SERVICEFROMTUNEXML = _KSM_BDA_GDDS_SERVICEFROMTUNEXML
PKSM_BDA_GDDS_SERVICEFROMTUNEXML = POINTER(_KSM_BDA_GDDS_SERVICEFROMTUNEXML)


class _KSM_BDA_USERACTIVITY_USEREASON(ctypes.Structure):
    pass


KSM_BDA_USERACTIVITY_USEREASON = _KSM_BDA_USERACTIVITY_USEREASON
PKSM_BDA_USERACTIVITY_USEREASON = POINTER(_KSM_BDA_USERACTIVITY_USEREASON)


class _KSM_BDA_CAS_ENTITLEMENTTOKEN(ctypes.Structure):
    pass


KSM_BDA_CAS_ENTITLEMENTTOKEN = _KSM_BDA_CAS_ENTITLEMENTTOKEN
PKSM_BDA_CAS_ENTITLEMENTTOKEN = POINTER(_KSM_BDA_CAS_ENTITLEMENTTOKEN)


class _KSM_BDA_CAS_CAPTURETOKEN(ctypes.Structure):
    pass


KSM_BDA_CAS_CAPTURETOKEN = _KSM_BDA_CAS_CAPTURETOKEN
PKSM_BDA_CAS_CAPTURETOKEN = POINTER(_KSM_BDA_CAS_CAPTURETOKEN)


class _KSM_BDA_CAS_OPENBROADCASTMMI(ctypes.Structure):
    pass


KSM_BDA_CAS_OPENBROADCASTMMI = _KSM_BDA_CAS_OPENBROADCASTMMI
PKSM_BDA_CAS_OPENBROADCASTMMI = POINTER(_KSM_BDA_CAS_OPENBROADCASTMMI)


class _KSM_BDA_CAS_CLOSEMMIDIALOG(ctypes.Structure):
    pass


KSM_BDA_CAS_CLOSEMMIDIALOG = _KSM_BDA_CAS_CLOSEMMIDIALOG
PKSM_BDA_CAS_CLOSEMMIDIALOG = POINTER(_KSM_BDA_CAS_CLOSEMMIDIALOG)


class _KSM_BDA_ISDBCAS_REQUEST(ctypes.Structure):
    pass


KSM_BDA_ISDBCAS_REQUEST = _KSM_BDA_ISDBCAS_REQUEST
PKSM_BDA_ISDBCAS_REQUEST = POINTER(_KSM_BDA_ISDBCAS_REQUEST)


class _KSM_BDA_TS_SELECTOR_SETTSID(ctypes.Structure):
    pass


KSM_BDA_TS_SELECTOR_SETTSID = _KSM_BDA_TS_SELECTOR_SETTSID
PKSM_BDA_TS_SELECTOR_SETTSID = POINTER(_KSM_BDA_TS_SELECTOR_SETTSID)


class tagKS_DATARANGE_BDA_ANTENNA(ctypes.Structure):
    pass


KS_DATARANGE_BDA_ANTENNA = tagKS_DATARANGE_BDA_ANTENNA
PKS_DATARANGE_BDA_ANTENNA = POINTER(tagKS_DATARANGE_BDA_ANTENNA)


class tagBDA_TRANSPORT_INFO(ctypes.Structure):
    pass


BDA_TRANSPORT_INFO = tagBDA_TRANSPORT_INFO
PBDA_TRANSPORT_INFO = POINTER(tagBDA_TRANSPORT_INFO)


class tagKS_DATARANGE_BDA_TRANSPORT(ctypes.Structure):
    pass


KS_DATARANGE_BDA_TRANSPORT = tagKS_DATARANGE_BDA_TRANSPORT
PKS_DATARANGE_BDA_TRANSPORT = POINTER(tagKS_DATARANGE_BDA_TRANSPORT)


class _ChannelChangeInfo(ctypes.Structure):
    pass


ChannelChangeInfo = _ChannelChangeInfo


class _ChannelTypeInfo(ctypes.Structure):
    pass


ChannelTypeInfo = _ChannelTypeInfo


class _ChannelInfo(ctypes.Structure):
    pass


ChannelInfo = _ChannelInfo


class _SpanningEventDescriptor(ctypes.Structure):
    pass


SpanningEventDescriptor = _SpanningEventDescriptor


class _DVBScramblingControlSpanningEvent(ctypes.Structure):
    pass


DVBScramblingControlSpanningEvent = _DVBScramblingControlSpanningEvent


class _SpanningEventEmmMessage(ctypes.Structure):
    pass


SpanningEventEmmMessage = _SpanningEventEmmMessage


class _LanguageInfo(ctypes.Structure):
    pass


LanguageInfo = _LanguageInfo


class _DualMonoInfo(ctypes.Structure):
    pass


DualMonoInfo = _DualMonoInfo


class _PIDListSpanningEvent(ctypes.Structure):
    pass


PIDListSpanningEvent = _PIDListSpanningEvent


class RATING_ATTRIBUTE(ctypes.Structure):
    pass


LPRATING_ATTRIBUTE = POINTER(RATING_ATTRIBUTE)


class RATING_SYSTEM(ctypes.Structure):
    pass


LPRATING_SYSTEM = POINTER(RATING_SYSTEM)


class RATING_INFO(ctypes.Structure):
    pass


LPRATING_INFO = POINTER(RATING_INFO)


class _PBDAParentalControl(ctypes.Structure):
    pass


PBDAParentalControl = _PBDAParentalControl


class DvbParentalRatingParam(ctypes.Structure):
    pass





class DvbParentalRatingDescriptor(ctypes.Structure):
    pass



class KSPROPERTY_BDA_RF_TUNER_CAPS_S(ctypes.Structure):
    pass


PKSPROPERTY_BDA_RF_TUNER_CAPS_S = POINTER(KSPROPERTY_BDA_RF_TUNER_CAPS_S)


class KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S(ctypes.Structure):
    pass


PKSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S = POINTER(KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S)


class KSPROPERTY_BDA_RF_TUNER_STANDARD_S(ctypes.Structure):
    pass


PKSPROPERTY_BDA_RF_TUNER_STANDARD_S = POINTER(KSPROPERTY_BDA_RF_TUNER_STANDARD_S)


class KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S(ctypes.Structure):
    pass


PKSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S = POINTER(KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S)


class KSEVENTDATA_BDA_RF_TUNER_SCAN_S(ctypes.Structure):
    pass


PKSEVENTDATA_BDA_RF_TUNER_SCAN_S = POINTER(KSEVENTDATA_BDA_RF_TUNER_SCAN_S)


# ----------------------------------------------------------------------------
# File: BDAMedia.h
# Desc: Broadcast Driver Architecture Multimedia Definitions.
# Copyright (c) 1996 - 2001, Microsoft Corporation. All rights reserved.
# ----------------------------------------------------------------------------
from pyWinAPI.shared.winapifamily_h import * # NOQA


if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    if not defined(_KSMEDIA_):
        pass
    # END IF   not defined(_KSMEDIA_)

    if not defined(_BDATYPES_):
        pass
    # END IF   not defined(_BDATYPES_)

    if not defined(_BDAMEDIA_):
        _BDAMEDIA_ = VOID
        if defined(__cplusplus):
            pass
        # END IF   defined(__cplusplus)

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSProperty Set Structure Definitions for BDA
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSP_BDA_NODE_PIN._fields_ = [
            ('Property', KSPROPERTY),
            ('ulNodeType', ULONG),
            ('ulInputPinId', ULONG),
            ('ulOutputPinId', ULONG),
        ]


        class _Union_1(ctypes.Union):
            pass


        _Union_1._fields_ = [
            ('PinId', ULONG),
            ('PinType', ULONG),
        ]
        _KSM_BDA_PIN._Union_1 = _Union_1

        _KSM_BDA_PIN._anonymous_ = (
            '_Union_1',
        )

        _KSM_BDA_PIN._fields_ = [
            ('Method', KSMETHOD),
            ('_Union_1', _KSM_BDA_PIN._Union_1),
            ('Reserved', ULONG),
        ]


        class _Union_2(ctypes.Union):
            pass


        _Union_2._fields_ = [
            ('InputPinId', ULONG),
            ('InputPinType', ULONG),
        ]
        _KSM_BDA_PIN_PAIR._Union_2 = _Union_2


        class _Union_3(ctypes.Union):
            pass


        _Union_3._fields_ = [
            ('OutputPinId', ULONG),
            ('OutputPinType', ULONG),
        ]
        _KSM_BDA_PIN_PAIR._Union_3 = _Union_3

        _KSM_BDA_PIN_PAIR._anonymous_ = (
            '_Union_2',
            '_Union_3',
        )

        _KSM_BDA_PIN_PAIR._fields_ = [
            ('Method', KSMETHOD),
            ('_Union_2', _KSM_BDA_PIN_PAIR._Union_2),
            ('_Union_3', _KSM_BDA_PIN_PAIR._Union_3),
        ]

        KSP_NODE_ESPID._fields_ = [
            ('Property', KSP_NODE),
            ('EsPid', ULONG),
        ]

        _KSM_BDA_DEBUG_LEVEL._fields_ = [
            ('Method', KSMETHOD),
            ('ucDebugLevel', UCHAR),
            ('ulDebugStringSize', ULONG),
            ('argbDebugString', BYTE * MIN_DIMENSION),
        ]

        _BDA_DEBUG_DATA._fields_ = [
            ('lResult', PBDARESULT),
            ('uuidDebugDataType', GUID),
            ('ulDataSize', ULONG),
            ('argbDebugData', BYTE * MIN_DIMENSION),
        ]

        _BDA_EVENT_DATA._fields_ = [
            ('lResult', PBDARESULT),
            ('ulEventID', ULONG),
            ('uuidEventType', GUID),
            ('ulEventDataLength', ULONG),
            ('argbEventData', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_EVENT_COMPLETE._fields_ = [
            ('Method', KSMETHOD),
            ('ulEventID', ULONG),
            ('ulEventResult', ULONG),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for DRM, WMDRM, WMDRMTUNER
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_DRM_SETDRM._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('NewDRMuuid', GUID),
        ]

        _KSM_BDA_BUFFER._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulBufferSize', ULONG),
            ('argbBuffer', BYTE * MIN_DIMENSION),
        ]

        KSM_BDA_WMDRM_LICENSE._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('uuidKeyID', GUID),
        ]

        _KSM_BDA_WMDRM_RENEWLICENSE._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulXMRLicenseLength', ULONG),
            ('ulEntitlementTokenLength', ULONG),
            # License and Entitlement Token Buffer
            ('argbDataBuffer', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulDialogRequest', ULONG),
            ('cLanguage', CHAR * 12),
            ('ulPurchaseTokenLength', ULONG),
            # Language Buffer before PurchaseToken
            ('argbDataBuffer', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_WMDRMTUNER_SETPIDPROTECTION._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulPID', ULONG),
            ('uuidKeyID', GUID),
        ]

        _KSM_BDA_WMDRMTUNER_GETPIDPROTECTION._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulPID', ULONG),
        ]

        _KSM_BDA_WMDRMTUNER_SYNCVALUE._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulSyncValue', ULONG),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for PBDA TUNER
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_TUNER_TUNEREQUEST._fields_ = [
            ('Method', KSMETHOD),
            ('ulTuneLength', ULONG),
            ('argbTuneData', BYTE * MIN_DIMENSION),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for PBDA GENERAL PURPOSE NAME
        # VALUES
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_GPNV_GETVALUE._fields_ = [
            ('Method', KSMETHOD),
            ('ulNameLength', ULONG),
            ('cLanguage', CHAR * 12),
            ('argbData', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_GPNV_SETVALUE._fields_ = [
            ('Method', KSMETHOD),
            ('ulDialogRequest', ULONG),
            ('cLanguage', CHAR * 12),
            ('ulNameLength', ULONG),
            ('ulValueLength', ULONG),
            ('argbName', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_GPNV_NAMEINDEX._fields_ = [
            ('Method', KSMETHOD),
            ('ulValueNameIndex', ULONG),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for PBDA SCANNING
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_SCAN_CAPABILTIES._fields_ = [
            ('Method', KSMETHOD),
            ('uuidBroadcastStandard', GUID),
        ]

        _KSM_BDA_SCAN_FILTER._fields_ = [
            ('Method', KSMETHOD),
            ('ulScanModulationTypeSize', ULONG),
            ('AnalogVideoStandards', ULONG64),
            ('argbScanModulationTypes', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_SCAN_START._fields_ = [
            ('Method', KSMETHOD),
            ('LowerFrequency', ULONG),
            ('HigherFrequency', ULONG),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for PBDA GUIDE DATA
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_GDDS_TUNEXMLFROMIDX._fields_ = [
            ('Method', KSMETHOD),
            ('ulIdx', ULONG64),
        ]

        _KSM_BDA_GDDS_SERVICEFROMTUNEXML._fields_ = [
            ('Method', KSMETHOD),
            ('ulTuneXmlLength', ULONG),
            ('argbTuneXml', BYTE * MIN_DIMENSION),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for PBDA USER ACTIVITY
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_USERACTIVITY_USEREASON._fields_ = [
            ('Method', KSMETHOD),
            ('ulUseReason', ULONG),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for PBDA CAS
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_CAS_ENTITLEMENTTOKEN._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulDialogRequest', ULONG),
            ('cLanguage', CHAR * 12),
            ('ulRequestType', ULONG),
            ('ulEntitlementTokenLen', ULONG),
            ('argbEntitlementToken', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_CAS_CAPTURETOKEN._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulTokenLength', ULONG),
            ('argbToken', BYTE * MIN_DIMENSION),
        ]

        _KSM_BDA_CAS_OPENBROADCASTMMI._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulDialogRequest', ULONG),
            ('cLanguage', CHAR * 12),
            ('ulEventId', ULONG),
        ]

        _KSM_BDA_CAS_CLOSEMMIDIALOG._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulDialogRequest', ULONG),
            ('cLanguage', CHAR * 12),
            ('ulDialogNumber', ULONG),
            ('ulReason', ULONG),
        ]

        _KSM_BDA_ISDBCAS_REQUEST._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('ulRequestID', ULONG),
            ('ulIsdbCommandSize', ULONG),
            ('argbIsdbCommandData', BYTE * MIN_DIMENSION),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSMethod Set Structure Definitions for Transprt Stream Selector
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        _KSM_BDA_TS_SELECTOR_SETTSID._fields_ = [
            ('NodeMethod', KSM_NODE),
            ('usTSID', USHORT),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA Data Range definitions. Includes specifier definitions.
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # Antenna Signal Formats
        tagKS_DATARANGE_BDA_ANTENNA._fields_ = [
            ('DataRange', KSDATARANGE),
        ]

        # Transport Formats
        # Size, in bytes, of a physical packet
        tagBDA_TRANSPORT_INFO._fields_ = [
            ('ulcbPhyiscalPacket', ULONG),
            # Size, in bytes, of each physical frame
            ('ulcbPhyiscalFrame', ULONG),
            # Capture buffer alignment in bytes
            ('ulcbPhyiscalFrameAlignment', ULONG),
            # Normal ActiveMovie units (100 nS)
            ('AvgTimePerFrame', REFERENCE_TIME),
        ]

        tagKS_DATARANGE_BDA_TRANSPORT._fields_ = [
            ('DataRange', KSDATARANGE),
            ('BdaTransportInfo', BDA_TRANSPORT_INFO),
        ]

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA Event Guids
        # These are sent by the IBroadcastEvent service on the graph.
        # To receive,
        # 0) Implement IBroadcastEvent in your receiving object - this has one Method on it: Fire()
        #
        # 1) QI the graphs service provider for SID_SBroadcastEventService
        # for the IID_IBroadcastEvent object
        # 2) OR create the event service (CLSID_BroadcastEventService) if not already there
        #
        # and register it
        # 3) QI that object for it's IConnectionPoint interface (*pCP)
        # 4) Advise your object on *pCP (e.g.
        # pCP.Advise(static_cast < IBroadCastEvent* > (this), & dwCookie)
        # 5) Unadvise when done..
        # 6) Implement IBroadcastEvent::Fire(GUID gEventID)
        # Check for relevant event below and deal with it appropriatly...
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # {83183C03-C09E-45c4-A719-807A94952BF9}
        STATIC_EVENTID_TuningChanging = (
            0x83183C03,
            0xC09E,
            0x45C4,
            0xA7,
            0x19,
            0x80,
            0x7A,
            0x94,
            0x95,
            0x2B,
            0xF9
        )
        EVENTID_TuningChanging = DEFINE_GUIDSTRUCT(
            "83183C03-C09E-45c4-A719-807A94952BF9"
        )
        EVENTID_TuningChanging = DEFINE_GUIDNAMED(EVENTID_TuningChanging)
        # {9D7E6235-4B7D-425d-A6D1-D717C33B9C4C}
        STATIC_EVENTID_TuningChanged = (
            0x9D7E6235,
            0x4B7D,
            0x425D,
            0xA6,
            0xD1,
            0xD7,
            0x17,
            0xC3,
            0x3B,
            0x9C,
            0x4C
        )
        EVENTID_TuningChanged = DEFINE_GUIDSTRUCT(
            "9D7E6235-4B7D-425d-A6D1-D717C33B9C4C"
        )
        EVENTID_TuningChanged = DEFINE_GUIDNAMED(EVENTID_TuningChanged)
        # {9F02D3D0-9F06-4369-9F1E-3AD6CA19807E}
        STATIC_EVENTID_CandidatePostTuneData = (
            0x9F02D3D0,
            0x9F06,
            0x4369,
            0x9F,
            0x1E,
            0x3A,
            0xD6,
            0xCA,
            0x19,
            0x80,
            0x7E
        )
        EVENTID_CandidatePostTuneData = DEFINE_GUIDSTRUCT(
            "9F02D3D0-9F06-4369-9F1E-3AD6CA19807E"
        )
        EVENTID_CandidatePostTuneData = (
            DEFINE_GUIDNAMED(EVENTID_CandidatePostTuneData)
        )
        # {2A65C528-2249-4070-AC16-00390CDFB2DD}
        STATIC_EVENTID_CADenialCountChanged = (
            0x2A65C528,
            0x2249,
            0x4070,
            0xAC,
            0x16,
            0x0,
            0x39,
            0xC,
            0xDF,
            0xB2,
            0xDD
        )
        EVENTID_CADenialCountChanged = DEFINE_GUIDSTRUCT(
            "2A65C528-2249-4070-AC16-00390CDFB2DD"
        )
        EVENTID_CADenialCountChanged = (
            DEFINE_GUIDNAMED(EVENTID_CADenialCountChanged)
        )
        # {6D9CFAF2-702D-4b01-8DFF-6892AD20D191}
        STATIC_EVENTID_SignalStatusChanged = (
            0x6D9CFAF2,
            0x702D,
            0x4B01,
            0x8D,
            0xFF,
            0x68,
            0x92,
            0xAD,
            0x20,
            0xD1,
            0x91
        )
        EVENTID_SignalStatusChanged = DEFINE_GUIDSTRUCT(
            "6D9CFAF2-702D-4b01-8DFF-6892AD20D191"
        )
        EVENTID_SignalStatusChanged = (
            DEFINE_GUIDNAMED(EVENTID_SignalStatusChanged)
        )
        # {C87EC52D-CD18-404a-A076-C02A273D3DE7}
        STATIC_EVENTID_NewSignalAcquired = (
            0xC87EC52D,
            0xCD18,
            0x404A,
            0xA0,
            0x76,
            0xC0,
            0x2A,
            0x27,
            0x3D,
            0x3D,
            0xE7
        )
        EVENTID_NewSignalAcquired = DEFINE_GUIDSTRUCT(
            "C87EC52D-CD18-404a-A076-C02A273D3DE7"
        )
        EVENTID_NewSignalAcquired = DEFINE_GUIDNAMED(EVENTID_NewSignalAcquired)
        # {D10DF9D5-C261-4b85-9E8A-517B3299CAB2}
        STATIC_EVENTID_EASMessageReceived = (
            0xD10DF9D5,
            0xC261,
            0x4B85,
            0x9E,
            0x8A,
            0x51,
            0x7B,
            0x32,
            0x99,
            0xCA,
            0xB2
        )
        EVENTID_EASMessageReceived = DEFINE_GUIDSTRUCT(
            "D10DF9D5-C261-4b85-9E8A-517B3299CAB2"
        )
        EVENTID_EASMessageReceived = (
            DEFINE_GUIDNAMED(EVENTID_EASMessageReceived)
        )
        # This event is broadcasted with FireEx when a
        # table(currently, PAT, PMT, NIT
        # and SDT for DVB; PAT, PMT, MGT and VCT for
        # ATSC). The four parameters are:
        # dwPara1 - TSID, ONID | TSID for DVB EIT
        # dwPara2 - TID | PID
        # dwPara3 - dwHashedVersion
        # dwPara4 - program number for PMT, Segment | SID for EIT, but not
        # used for others
        # {1B9C3703-D447-4e16-97BB-01799FC031ED}
        STATIC_EVENTID_PSITable = (
            0x1B9C3703,
            0xD447,
            0x4E16,
            0x97,
            0xBB,
            0x1,
            0x79,
            0x9F,
            0xC0,
            0x31,
            0xED
        )
        EVENTID_PSITable = DEFINE_GUIDSTRUCT(
            "1B9C3703-D447-4e16-97BB-01799FC031ED"
        )
        EVENTID_PSITable = DEFINE_GUIDNAMED(EVENTID_PSITable)
        # This event is broadcasted with FireEx when the capture graph
        # recognized that a
        # current tuning channel has been terminated by broadcaster.
        # The four parameters are:
        # dwPara1 - TSID
        # dwPara2 - ONID | SID
        # dwPara3 - channel frequency
        # dwPara4 - satellite orbital position (0xFFFFFFFF for non-satellite)
        # {0A1D591C-E0D2-4f8e-8960-2335BEF45CCB}
        STATIC_EVENTID_ServiceTerminated = (
            0xA1D591C,
            0xE0D2,
            0x4F8E,
            0x89,
            0x60,
            0x23,
            0x35,
            0xBE,
            0xF4,
            0x5C,
            0xCB
        )
        EVENTID_ServiceTerminated = DEFINE_GUIDSTRUCT(
            "0A1D591C-E0D2-4f8e-8960-2335BEF45CCB"
        )
        EVENTID_ServiceTerminated = DEFINE_GUIDNAMED(EVENTID_ServiceTerminated)
        # {A265FAEA-F874-4b38-9FF7-C53D02969996}
        STATIC_EVENTID_CardStatusChanged = (
            0xA265FAEA,
            0xF874,
            0x4B38,
            0x9F,
            0xF7,
            0xC5,
            0x3D,
            0x2,
            0x96,
            0x99,
            0x96
        )
        EVENTID_CardStatusChanged = DEFINE_GUIDSTRUCT(
            "A265FAEA-F874-4b38-9FF7-C53D02969996"
        )
        EVENTID_CardStatusChanged = DEFINE_GUIDNAMED(EVENTID_CardStatusChanged)
        DTV_CardStatus_Inserted = 0
        DTV_CardStatus_Removed = 1
        DTV_CardStatus_Error = 2
        DTV_CardStatus_FirmwareDownload = 3
        # {000906F5-F0D1-41d6-A7DF-4028697669F6}
        STATIC_EVENTID_DRMParingStatusChanged = (
            0x906F5,
            0xF0D1,
            0x41D6,
            0xA7,
            0xDF,
            0x40,
            0x28,
            0x69,
            0x76,
            0x69,
            0xF6
        )
        EVENTID_DRMParingStatusChanged = DEFINE_GUIDSTRUCT(
            "000906F5-F0D1-41d6-A7DF-4028697669F6"
        )
        EVENTID_DRMParingStatusChanged = (
            DEFINE_GUIDNAMED(EVENTID_DRMParingStatusChanged)
        )
        # The 1st parameter to this event is a BDA_DRMPairingStatus and 2nd is
        # the error code.
        # {5B2EBF78-B752-4420-B41E-A472DC95828E}
        STATIC_EVENTID_DRMParingStepComplete = (
            0x5B2EBF78,
            0xB752,
            0x4420,
            0xB4,
            0x1E,
            0xA4,
            0x72,
            0xDC,
            0x95,
            0x82,
            0x8E
        )
        EVENTID_DRMParingStepComplete = DEFINE_GUIDSTRUCT(
            "5B2EBF78-B752-4420-B41E-A472DC95828E"
        )
        EVENTID_DRMParingStepComplete = (
            DEFINE_GUIDNAMED(EVENTID_DRMParingStepComplete)
        )
        # The 1st parameter is which pairing manager is generting the event
        # The 2nd parameter is the step in the pairing process which is now
        # complete
        # The 3rd parameter is the result of the step
        OCUR_PAIRING_PROTOCOL_VERSION = 2
        PBDA_PAIRING_PROTOCOL_VERSION = 3
        # {052C29AF-09A4-4b93-890F-BD6A348968A4}
        STATIC_EVENTID_MMIMessage = (
            0x52C29AF,
            0x9A4,
            0x4B93,
            0x89,
            0xF,
            0xBD,
            0x6A,
            0x34,
            0x89,
            0x68,
            0xA4
        )
        EVENTID_MMIMessage = DEFINE_GUIDSTRUCT(
            "052C29AF-09A4-4b93-890F-BD6A348968A4"
        )
        EVENTID_MMIMessage = DEFINE_GUIDNAMED(EVENTID_MMIMessage)
        DTV_MMIMessage_Open = 0
        DTV_MMIMessage_Close = 1
        # {9071AD5D-2359-4c95-8694-AFA81D70BFD5}
        STATIC_EVENTID_EntitlementChanged = (
            0x9071AD5D,
            0x2359,
            0x4C95,
            0x86,
            0x94,
            0xAF,
            0xA8,
            0x1D,
            0x70,
            0xBF,
            0xD5
        )
        EVENTID_EntitlementChanged = DEFINE_GUIDSTRUCT(
            "9071AD5D-2359-4c95-8694-AFA81D70BFD5"
        )
        EVENTID_EntitlementChanged = (
            DEFINE_GUIDNAMED(EVENTID_EntitlementChanged)
        )
        DTV_Entitlement_CanDecrypt = 0
        DTV_Entitlement_NotEntitled = 1
        DTV_Entitlement_TechnicalFailure = 2
        # This FireEx event is fired when tuning to a STB channel number
        # the first parameter passed is the channel number the STB has been
        # tuned to
        # {17C4D730-D0F0-413a-8C99-500469DE35AD}
        STATIC_EVENTID_STBChannelNumber = (
            0x17C4D730,
            0xD0F0,
            0x413A,
            0x8C,
            0x99,
            0x50,
            0x04,
            0x69,
            0xDE,
            0x35,
            0xAD
        )
        EVENTID_STBChannelNumber = DEFINE_GUIDSTRUCT(
            "17C4D730-D0F0-413a-8C99-500469DE35AD"
        )
        EVENTID_STBChannelNumber = DEFINE_GUIDNAMED(EVENTID_STBChannelNumber)
        # {5CA51711-5DDC-41a6-9430-E41B8B3BBC5B}
        STATIC_EVENTID_BDAEventingServicePendingEvent = (
            0x5CA51711,
            0x5DDC,
            0x41A6,
            0x94,
            0x30,
            0xE4,
            0x1B,
            0x8B,
            0x3B,
            0xBC,
            0x5B
        )
        EVENTID_BDAEventingServicePendingEvent = DEFINE_GUIDSTRUCT(
            "5CA51711-5DDC-41a6-9430-E41B8B3BBC5B"
        )
        EVENTID_BDAEventingServicePendingEvent = (
            DEFINE_GUIDNAMED(EVENTID_BDAEventingServicePendingEvent)
        )
        # {EFC3A459-AE8B-4b4a-8FE9-79A0D097F3EA}
        STATIC_EVENTID_BDAConditionalAccessTAG = (
            0xEFC3A459,
            0xAE8B,
            0x4B4A,
            0x8F,
            0xE9,
            0x79,
            0xA0,
            0xD0,
            0x97,
            0xF3,
            0xEA
        )
        EVENTID_BDAConditionalAccessTAG = DEFINE_GUIDSTRUCT(
            "EFC3A459-AE8B-4b4a-8FE9-79A0D097F3EA"
        )
        EVENTID_BDAConditionalAccessTAG = (
            DEFINE_GUIDNAMED(EVENTID_BDAConditionalAccessTAG)
        )
        # {B2127D42-7BE5-4f4b-9130-6679899F4F4B}
        STATIC_EVENTTYPE_CASDescrambleFailureEvent = (
            0xB2127D42,
            0x7BE5,
            0x4F4B,
            0x91,
            0x30,
            0x66,
            0x79,
            0x89,
            0x9F,
            0x4F,
            0x4B
        )
        EVENTTYPE_CASDescrambleFailureEvent = DEFINE_GUIDSTRUCT(
            "B2127D42-7BE5-4f4b-9130-6679899F4F4B"
        )
        EVENTTYPE_CASDescrambleFailureEvent = (
            DEFINE_GUIDNAMED(EVENTTYPE_CASDescrambleFailureEvent)
        )
        # {EAD831AE-5529-4d1f-AFCE-0D8CD1257D30}
        STATIC_EVENTID_CASFailureSpanningEvent = (
            0xEAD831AE,
            0x5529,
            0x4D1F,
            0xAF,
            0xCE,
            0xD,
            0x8C,
            0xD1,
            0x25,
            0x7D,
            0x30
        )
        EVENTID_CASFailureSpanningEvent = DEFINE_GUIDSTRUCT(
            "EAD831AE-5529-4d1f-AFCE-0D8CD1257D30"
        )
        EVENTID_CASFailureSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_CASFailureSpanningEvent)
        )


        class ChannelChangeSpanningEvent_State(ENUM):
            ChannelChangeSpanningEvent_Start = 0
            ChannelChangeSpanningEvent_End = 2

        ChannelChangeSpanningEvent_Start = ChannelChangeSpanningEvent_State.ChannelChangeSpanningEvent_Start
        ChannelChangeSpanningEvent_End = ChannelChangeSpanningEvent_State.ChannelChangeSpanningEvent_End

        # {9067C5E5-4C5C-4205-86C8-7AFE20FE1EFA} same as
        # __uuidof(EH_MSNP_TUNING_EVENT) defined in ehtraceguids.h
        STATIC_EVENTID_ChannelChangeSpanningEvent = (
            0x9067C5E5,
            0x4C5C,
            0x4205,
            0x86,
            0xC8,
            0x7A,
            0xFE,
            0x20,
            0xFE,
            0x1E,
            0xFA
        )
        EVENTID_ChannelChangeSpanningEvent = DEFINE_GUIDSTRUCT(
            "9067C5E5-4C5C-4205-86C8-7AFE20FE1EFA"
        )
        EVENTID_ChannelChangeSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_ChannelChangeSpanningEvent)
        )


        _ChannelChangeInfo._fields_ = [
            ('state', ChannelChangeSpanningEvent_State),
            ('TimeStamp', ULONGLONG),
        ]
        STATIC_EVENTID_ChannelTypeSpanningEvent = (
            0x72AB1D51,
            0x87D2,
            0x489B,
            0xBA,
            0x11,
            0xE,
            0x8,
            0xDC,
            0x21,
            0x2,
            0x43
        )
        EVENTID_ChannelTypeSpanningEvent = DEFINE_GUIDSTRUCT(
            "72ab1d51-87d2-489b-ba11-0e08dc210243"
        )
        EVENTID_ChannelTypeSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_ChannelTypeSpanningEvent)
        )


        class ChannelType(ENUM):
            ChannelTypeNone = 0x0000
            ChannelTypeOther = 0x0001
            ChannelTypeVideo = 0x0002
            ChannelTypeAudio = 0x0004
            ChannelTypeText = 0x0008
            ChannelTypeSubtitles = 0x0010
            ChannelTypeCaptions = 0x0020
            ChannelTypeSuperimpose = 0x0040
            ChannelTypeData = 0x0080

        ChannelTypeNone = ChannelType.ChannelTypeNone
        ChannelTypeOther = ChannelType.ChannelTypeOther
        ChannelTypeVideo = ChannelType.ChannelTypeVideo
        ChannelTypeAudio = ChannelType.ChannelTypeAudio
        ChannelTypeText = ChannelType.ChannelTypeText
        ChannelTypeSubtitles = ChannelType.ChannelTypeSubtitles
        ChannelTypeCaptions = ChannelType.ChannelTypeCaptions
        ChannelTypeSuperimpose = ChannelType.ChannelTypeSuperimpose
        ChannelTypeData = ChannelType.ChannelTypeData

        _ChannelTypeInfo._fields_ = [
            ('channelType', ChannelType),
            ('timeStamp', ULONGLONG),
        ]


        class _Union_4(ctypes.Union):
            pass


        class DVB(ctypes.Structure):
            pass


        DVB._fields_ = [
            ('lONID', LONG),
            ('lTSID', LONG),
            ('lSID', LONG),
        ]
        _Union_4.DVB = DVB


        class DC(ctypes.Structure):
            pass


        DC._fields_ = [
            ('lProgNumber', LONG),
        ]
        _Union_4.DC = DC


        class ATSC(ctypes.Structure):
            pass


        ATSC._fields_ = [
            ('lProgNumber', LONG),
        ]
        _Union_4.ATSC = ATSC


        _Union_4._fields_ = [
            ('DVB', _Union_4.DVB),
            ('DC', _Union_4.DC),
            ('ATSC', _Union_4.ATSC),
        ]
        _ChannelInfo._Union_4 = _Union_4

        _ChannelInfo._anonymous_ = (
            '_Union_4',
        )

        _ChannelInfo._fields_ = [
            ('lFrequency', LONG),
            ('_Union_4', _ChannelInfo._Union_4),
        ]

        # {41F36D80-4132-4cc2-B121-01A43219D81B}
        STATIC_EVENTID_ChannelInfoSpanningEvent = (
            0x41F36D80,
            0x4132,
            0x4CC2,
            0xB1,
            0x21,
            0x1,
            0xA4,
            0x32,
            0x19,
            0xD8,
            0x1B
        )
        EVENTID_ChannelInfoSpanningEvent = DEFINE_GUIDSTRUCT(
            "41F36D80-4132-4cc2-B121-01A43219D81B"
        )
        EVENTID_ChannelInfoSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_ChannelInfoSpanningEvent)
        )

        # F6CFC8F4-DA93-4f2f-BFF8-BA1EE6FCA3A2 same as __uuidof(EH_RRT_EVENT)
        # defined in ehtraceguids.h
        STATIC_EVENTID_RRTSpanningEvent = (
            0xF6CFC8F4,
            0xDA93,
            0x4F2F,
            0xBF,
            0xF8,
            0xBA,
            0x1E,
            0xE6,
            0xFC,
            0xA3,
            0xA2
        )
        EVENTID_RRTSpanningEvent = DEFINE_GUIDSTRUCT(
            "F6CFC8F4-DA93-4f2f-BFF8-BA1EE6FCA3A2"
        )
        EVENTID_RRTSpanningEvent = DEFINE_GUIDNAMED(EVENTID_RRTSpanningEvent)

        # Data sturcture for both CaptionServiceDescriptor and Content
        # Advisory descriptor
        # Total length of the
        # data(2*ctypes.sizeof(WORD) + lengthof(bDescriptor))
        _SpanningEventDescriptor._fields_ = [
            ('wDataLen', WORD),
            # Program numberassociated with this descriptor
            ('wProgNumber', WORD),
            # Source ID associated with this descriptor
            ('wSID', WORD),
            # Raw descriptor data
            ('bDescriptor', BYTE * 1),
        ]
        # Caption Service descriptior spanning event
        # {EFE779D9-97F0-4786-800D-95CF505DDC66} same as
        # __uuidof(EH_CaptionService_EVENT) defined in ehtraceguids.h
        STATIC_EVENTID_CSDescriptorSpanningEvent = (
            0xEFE779D9,
            0x97F0,
            0x4786,
            0x80,
            0xD,
            0x95,
            0xCF,
            0x50,
            0x5D,
            0xDC,
            0x66
        )
        EVENTID_CSDescriptorSpanningEvent = DEFINE_GUIDSTRUCT(
            "EFE779D9-97F0-4786-800D-95CF505DDC66"
        )
        EVENTID_CSDescriptorSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_CSDescriptorSpanningEvent)
        )
        # Content Advisory descriptor spanning event
        # {3AB4A2E6-4247-4b34-896C-30AFA5D21C24} same as
        # __uuidof(EH_ContentAdvisory_EVENT) defined in ehtraceguids.h
        STATIC_EVENTID_CtxADescriptorSpanningEvent = (
            0x3AB4A2E6,
            0x4247,
            0x4B34,
            0x89,
            0x6C,
            0x30,
            0xAF,
            0xA5,
            0xD2,
            0x1C,
            0x24
        )
        EVENTID_CtxADescriptorSpanningEvent = DEFINE_GUIDSTRUCT(
            "3AB4A2E6-4247-4b34-896C-30AFA5D21C24"
        )
        EVENTID_CtxADescriptorSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_CtxADescriptorSpanningEvent)
        )
        _DVBScramblingControlSpanningEvent._fields_ = [
            ('ulPID', ULONG),
            ('fScrambled', BOOL),
        ]
        # transport_scarmbling_control flag global event
        # {4BD4E1C4-90A1-4109-8236-27F00E7DCC5B}
        STATIC_EVENTID_DVBScramblingControlSpanningEvent = (
            0x4BD4E1C4,
            0x90A1,
            0x4109,
            0x82,
            0x36,
            0x27,
            0xF0,
            0xE,
            0x7D,
            0xCC,
            0x5B
        )
        EVENTID_DVBScramblingControlSpanningEvent = DEFINE_GUIDSTRUCT(
            "4BD4E1C4-90A1-4109-8236-27F00E7DCC5B"
        )
        EVENTID_DVBScramblingControlSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_DVBScramblingControlSpanningEvent)
        )


        class SignalAndServiceStatusSpanningEvent_State(ENUM):
            SignalAndServiceStatusSpanningEvent_None = - 1
            SignalAndServiceStatusSpanningEvent_Clear = 0
            SignalAndServiceStatusSpanningEvent_NoTVSignal = 1
            SignalAndServiceStatusSpanningEvent_ServiceOffAir = 2
            SignalAndServiceStatusSpanningEvent_WeakTVSignal = 3
            SignalAndServiceStatusSpanningEvent_NoSubscription = 4
            SignalAndServiceStatusSpanningEvent_AllAVScrambled = 5

        SignalAndServiceStatusSpanningEvent_None = SignalAndServiceStatusSpanningEvent_State.SignalAndServiceStatusSpanningEvent_None
        SignalAndServiceStatusSpanningEvent_Clear = SignalAndServiceStatusSpanningEvent_State.SignalAndServiceStatusSpanningEvent_Clear
        SignalAndServiceStatusSpanningEvent_NoTVSignal = SignalAndServiceStatusSpanningEvent_State.SignalAndServiceStatusSpanningEvent_NoTVSignal
        SignalAndServiceStatusSpanningEvent_ServiceOffAir = SignalAndServiceStatusSpanningEvent_State.SignalAndServiceStatusSpanningEvent_ServiceOffAir
        SignalAndServiceStatusSpanningEvent_WeakTVSignal = SignalAndServiceStatusSpanningEvent_State.SignalAndServiceStatusSpanningEvent_WeakTVSignal
        SignalAndServiceStatusSpanningEvent_NoSubscription = SignalAndServiceStatusSpanningEvent_State.SignalAndServiceStatusSpanningEvent_NoSubscription
        SignalAndServiceStatusSpanningEvent_AllAVScrambled = SignalAndServiceStatusSpanningEvent_State.SignalAndServiceStatusSpanningEvent_AllAVScrambled

        # Signal and Service Status event
        # {8068C5CB-3C04-492b-B47D-0308820DCE51} same as
        # __uuidof(EH_MSNP_SIGNALANDSERVICE_EVENT) defined in ehtraceguids.h
        STATIC_EVENTID_SignalAndServiceStatusSpanningEvent = (
            0x8068C5CB,
            0x3C04,
            0x492B,
            0xB4,
            0x7D,
            0x3,
            0x8,
            0x82,
            0xD,
            0xCE,
            0x51
        )
        EVENTID_SignalAndServiceStatusSpanningEvent = DEFINE_GUIDSTRUCT(
            "8068C5CB-3C04-492b-B47D-0308820DCE51"
        )
        EVENTID_SignalAndServiceStatusSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_SignalAndServiceStatusSpanningEvent)
        )
        EVENTID_SignalAndServiceStatusEvent = (
            EVENTID_SignalAndServiceStatusSpanningEvent
        )

        # Data structure for EmmMessageSpanningEvent
        # CA Broadcaster Group ID from CA_service_descriptor (ARIB STD-B25)
        _SpanningEventEmmMessage._fields_ = [
            ('bCAbroadcasterGroupId', BYTE),
            # Message Control from CA_service_descriptor (ARIB STD-B25)
            ('bMessageControl', BYTE),
            # Service ID of ISDB bound with this
            ('wServiceId', WORD),
            # Zero means the followings are inoperable
            ('wTableIdExtension', WORD),
            ('bDeletionStatus', BYTE),
            ('bDisplayingDuration1', BYTE),
            ('bDisplayingDuration2', BYTE),
            ('bDisplayingDuration3', BYTE),
            ('bDisplayingCycle', BYTE),
            ('bFormatVersion', BYTE),
            ('bDisplayPosition', BYTE),
            ('wMessageLength', WORD),
            ('szMessageArea', WCHAR * MIN_DIMENSION),
        ]

        # EMM Message spanning event
        # {6BF00268-4F7E-4294-AA87-E9E953E43F14} same as
        # __uuidof(EH_EmmMessage_EVENT) defined in ehtraceguids.h
        STATIC_EVENTID_EmmMessageSpanningEvent = (
            0x6BF00268,
            0x4F7E,
            0x4294,
            0xAA,
            0x87,
            0xE9,
            0xE9,
            0x53,
            0xE4,
            0x3F,
            0x14
        )
        EVENTID_EmmMessageSpanningEvent = DEFINE_GUIDSTRUCT(
            "6BF00268-4F7E-4294-AA87-E9E953E43F14"
        )
        EVENTID_EmmMessageSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_EmmMessageSpanningEvent)
        )

        # {501CBFBE-B849-42ce-9BE9-3DB869FB82B3}
        STATIC_EVENTID_AudioTypeSpanningEvent = (
            0x501CBFBE,
            0xB849,
            0x42CE,
            0x9B,
            0xE9,
            0x3D,
            0xB8,
            0x69,
            0xFB,
            0x82,
            0xB3
        )
        EVENTID_AudioTypeSpanningEvent = DEFINE_GUIDSTRUCT(
            "501CBFBE-B849-42ce-9BE9-3DB869FB82B3"
        )
        EVENTID_AudioTypeSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_AudioTypeSpanningEvent)
        )

        # AC 3 audio type and ISO639 language descriptor audio type are slight
        # different. The
        # AudioType values defined here is for the convenience of the user of
        # audio type info
        # and the conversion from the original spec to these values is done in
        # capture.
        # ISO639 language descriptor audio types:
        # 0x00 undefined   (standard audio)
        # 0x01 clean effects
        # 0x02 hearing impaired
        # 0x03 visual impaired commentary
        # 0x04-0xFF reserved
        # AC3 audio types
        # 0 Complete Main (CM)
        # 1 Music and Effects (ME)
        # 2 Visually Impaired (VI)
        # 3 Hearing Impaired (HI)
        # 4 Dialogue (D)
        # 5 Commentary (C)
        # 6 Emergency (E)
        # 7 Voiceover (VO)
        AudioType_Standard = 0
        AudioType_Music_And_Effects = 1
        AudioType_Visually_Impaired = 2
        AudioType_Hearing_Impaired = 3
        AudioType_Dialogue = 4
        AudioType_Commentary = 5
        AudioType_Emergency = 6
        AudioType_Voiceover = 7
        AudioType_Reserved = -1

        # {82af2ebc-30a6-4264-a80b-ad2e1372ac60}
        STATIC_EVENTID_StreamTypeSpanningEvent = (
            0x82AF2EBC,
            0x30A6,
            0x4264,
            0xA8,
            0x0B,
            0xAD,
            0x2E,
            0x13,
            0x72,
            0xAC,
            0x60
        )
        EVENTID_StreamTypeSpanningEvent = DEFINE_GUIDSTRUCT(
            "82af2ebc-30a6-4264-a80b-ad2e1372ac60"
        )
        EVENTID_StreamTypeSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_StreamTypeSpanningEvent)
        )

        # {3A954083-93D0-463e-90B2-0742C496EDF0}
        STATIC_EVENTID_ARIBcontentSpanningEvent = (
            0x3A954083,
            0x93D0,
            0x463E,
            0x90,
            0xB2,
            0x7,
            0x42,
            0xC4,
            0x96,
            0xED,
            0xF0
        )
        EVENTID_ARIBcontentSpanningEvent = DEFINE_GUIDSTRUCT(
            "3A954083-93D0-463e-90B2-0742C496EDF0"
        )
        EVENTID_ARIBcontentSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_ARIBcontentSpanningEvent)
        )

        # {E292666D-9C02-448d-AA8D-781A93FDC395}
        STATIC_EVENTID_LanguageSpanningEvent = (
            0xE292666D,
            0x9C02,
            0x448D,
            0xAA,
            0x8D,
            0x78,
            0x1A,
            0x93,
            0xFD,
            0xC3,
            0x95
        )
        EVENTID_LanguageSpanningEvent = DEFINE_GUIDSTRUCT(
            "E292666D-9C02-448d-AA8D-781A93FDC395"
        )
        EVENTID_LanguageSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_LanguageSpanningEvent)
        )


        _LanguageInfo._fields_ = [
            ('LangID', LANGID),
            ('lISOLangCode', LONG),
        ]

        # {A9A29B56-A84B-488c-89D5-0D4E7657C8CE}
        STATIC_EVENTID_DualMonoSpanningEvent = (
            0xA9A29B56,
            0xA84B,
            0x488C,
            0x89,
            0xD5,
            0x0D,
            0x4E,
            0x76,
            0x57,
            0xC8,
            0xCE
        )
        EVENTID_DualMonoSpanningEvent = DEFINE_GUIDSTRUCT(
            "A9A29B56-A84B-488c-89D5-0D4E7657C8CE"
        )
        EVENTID_DualMonoSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_DualMonoSpanningEvent)
        )


        _DualMonoInfo._fields_ = [
            ('LangID1', LANGID),
            ('LangID2', LANGID),
            ('lISOLangCode1', LONG),
            ('lISOLangCode2', LONG),
        ]

        # {47FC8F65-E2BB-4634-9CEF-FDBFE6261D5C}
        STATIC_EVENTID_PIDListSpanningEvent = (
            0x47FC8F65,
            0xE2BB,
            0x4634,
            0x9C,
            0xEF,
            0xFD,
            0xBF,
            0xE6,
            0x26,
            0x1D,
            0x5C
        )
        EVENTID_PIDListSpanningEvent = DEFINE_GUIDSTRUCT(
            "47FC8F65-E2BB-4634-9CEF-FDBFE6261D5C"
        )
        EVENTID_PIDListSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_PIDListSpanningEvent)
        )


        _PIDListSpanningEvent._fields_ = [
            ('wPIDCount', WORD),
            ('pulPIDs', ULONG * 1),
        ]

        # {107BD41C-A6DA-4691-8369-11B2CDAA288E}
        STATIC_EVENTID_AudioDescriptorSpanningEvent = (
            0x107BD41C,
            0xA6DA,
            0x4691,
            0x83,
            0x69,
            0x11,
            0xB2,
            0xCD,
            0xAA,
            0x28,
            0x8E
        )
        EVENTID_AudioDescriptorSpanningEvent = DEFINE_GUIDSTRUCT(
            "107BD41C-A6DA-4691-8369-11B2CDAA288E"
        )
        EVENTID_AudioDescriptorSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_AudioDescriptorSpanningEvent)
        )

        # {5DCEC048-D0B9-4163-872C-4F32223BE88A}
        STATIC_EVENTID_SubtitleSpanningEvent = (
            0x5DCEC048,
            0xD0B9,
            0x4163,
            0x87,
            0x2C,
            0x4F,
            0x32,
            0x22,
            0x3B,
            0xE8,
            0x8A
        )
        EVENTID_SubtitleSpanningEvent = DEFINE_GUIDSTRUCT(
            "5DCEC048-D0B9-4163-872C-4F32223BE88A"
        )
        EVENTID_SubtitleSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_SubtitleSpanningEvent)
        )

        # {9599D950-5F33-4617-AF7C-1E54B510DAA3}
        STATIC_EVENTID_TeletextSpanningEvent = (
            0x9599D950,
            0x5F33,
            0x4617,
            0xAF,
            0x7C,
            0x1E,
            0x54,
            0xB5,
            0x10,
            0xDA,
            0xA3
        )
        EVENTID_TeletextSpanningEvent = DEFINE_GUIDSTRUCT(
            "9599D950-5F33-4617-AF7C-1E54B510DAA3"
        )
        EVENTID_TeletextSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_TeletextSpanningEvent)
        )

        # {CAF1AB68-E153-4d41-A6B3-A7C998DB75EE}
        STATIC_EVENTID_StreamIDSpanningEvent = (
            0xCAF1AB68,
            0xE153,
            0x4D41,
            0xA6,
            0xB3,
            0xA7,
            0xC9,
            0x98,
            0xDB,
            0x75,
            0xEE
        )
        EVENTID_StreamIDSpanningEvent = DEFINE_GUIDSTRUCT(
            "CAF1AB68-E153-4d41-A6B3-A7C998DB75EE"
        )
        EVENTID_StreamIDSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_StreamIDSpanningEvent)
        )

        # {F947AA85-FB52-48e8-B9C5-E1E1F411A51A}
        STATIC_EVENTID_PBDAParentalControlEvent = (
            0xF947AA85,
            0xFB52,
            0x48E8,
            0xB9,
            0xC5,
            0xE1,
            0xE1,
            0xF4,
            0x11,
            0xA5,
            0x1A
        )
        EVENTID_PBDAParentalControlEvent = DEFINE_GUIDSTRUCT(
            "F947AA85-FB52-48e8-B9C5-E1E1F411A51A"
        )
        EVENTID_PBDAParentalControlEvent = (
            DEFINE_GUIDNAMED(EVENTID_PBDAParentalControlEvent)
        )
        MAX_COUNTRY_CODE_STRING = 3


        RATING_ATTRIBUTE._fields_ = [
            ('rating_attribute_id', DWORD),
            ('rating_attribute_value', DWORD),
        ]

        RATING_SYSTEM._fields_ = [
            ('rating_system_id', GUID),
            ('rating_system_is_age_type', BYTE, 1),
            ('reserved', BYTE, 7),
            ('country_code', BYTE * MAX_COUNTRY_CODE_STRING),
            ('rating_attribute_count', DWORD),
            ('lpratingattrib', POINTER(RATING_ATTRIBUTE)),
        ]

        RATING_INFO._fields_ = [
            ('rating_system_count', DWORD),
            ('lpratingsystem', POINTER(RATING_SYSTEM)),
        ]

        # attribute_id
        # Parental Control Time Range
        PARENTAL_CONTROL_TIME_RANGE = 0x00000001

        # Required Parental Control Time Range
        REQUIRED_PARENTAL_CONTROL_TIME_RANGE = 0x00000002

        # Rating (overall/primary content rating)
        PARENTAL_CONTROL_CONTENT_RATING = 0x00000100

        # Violence
        PARENTAL_CONTROL_ATTRIB_VIOLENCE = 0x00000200

        # Language
        PARENTAL_CONTROL_ATTRIB_LANGUAGE = 0x00000201

        # Sexual Content
        PARENTAL_CONTROL_ATTRIB_SEXUAL = 0x00000202

        # Dialogue
        PARENTAL_CONTROL_ATTRIB_DIALOGUE = 0x00000203

        # Fantasy Violence
        PARENTAL_CONTROL_ATTRIB_FANTASY = 0x00000204

        # UNDEFINED
        PARENTAL_CONTROL_VALUE_UNDEFINED = 0


        _PBDAParentalControl._fields_ = [
            # number of rating systems in PBDA parenatl control table
            ('rating_system_count', ULONG),
            # PBDA unified rating systems
            ('rating_systems', POINTER(RATING_SYSTEM)),
        ]

        # {D97287B2-2DFD-436a-9485-99D7D4AB5A69}
        STATIC_EVENTID_TuneFailureEvent = (
            0xD97287B2,
            0x2DFD,
            0x436A,
            0x94,
            0x85,
            0x99,
            0xD7,
            0xD4,
            0xAB,
            0x5A,
            0x69
        )
        EVENTID_TuneFailureEvent = DEFINE_GUIDSTRUCT(
            "D97287B2-2DFD-436a-9485-99D7D4AB5A69"
        )
        EVENTID_TuneFailureEvent = DEFINE_GUIDNAMED(EVENTID_TuneFailureEvent)

        # {6F8AA455-5EE1-48ab-A27C-4C8D70B9AEBA}
        STATIC_EVENTID_TuneFailureSpanningEvent = (
            0x6F8AA455,
            0x5EE1,
            0x48AB,
            0xA2,
            0x7C,
            0x4C,
            0x8D,
            0x70,
            0xB9,
            0xAE,
            0xBA
        )
        EVENTID_TuneFailureSpanningEvent = DEFINE_GUIDSTRUCT(
            "6F8AA455-5EE1-48ab-A27C-4C8D70B9AEBA"
        )
        EVENTID_TuneFailureSpanningEvent = (
            DEFINE_GUIDNAMED(EVENTID_TuneFailureSpanningEvent)
        )

        # {2A67A58D-ECA5-4eac-ABCB-E734D3776D0A}
        STATIC_EVENTID_DvbParentalRatingDescriptor = (
            0x2A67A58D,
            0xECA5,
            0x4EAC,
            0xAB,
            0xCB,
            0xE7,
            0x34,
            0xD3,
            0x77,
            0x6D,
            0x0A
        )
        EVENTID_DvbParentalRatingDescriptor = DEFINE_GUIDSTRUCT(
            "2A67A58D-ECA5-4eac-ABCB-E734D3776D0A"
        )
        EVENTID_DvbParentalRatingDescriptor = (
            DEFINE_GUIDNAMED(EVENTID_DvbParentalRatingDescriptor)
        )


        DvbParentalRatingParam._fields_ = [
            # 3-chars + null
            ('szCountryCode', CHAR * 4),
            # rating
            ('bRating', BYTE),
        ]

        DvbParentalRatingDescriptor._fields_ = [
            # if zero, no rating
            ('ulNumParams', ULONG),
            ('pParams', DvbParentalRatingParam * 1),
        ]

        # {F5689FFE-55F9-4bb3-96BE-AE971C63BAE0}
        STATIC_EVENTID_DFNWithNoActualAVData = (
            0xF5689FFE,
            0x55F9,
            0x4BB3,
            0x96,
            0xBE,
            0xAE,
            0x97,
            0x1C,
            0x63,
            0xBA,
            0xE0
        )
        EVENTID_DFNWithNoActualAVData = DEFINE_GUIDSTRUCT(
            "F5689FFE-55F9-4bb3-96BE-AE971C63BAE0"
        )
        EVENTID_DFNWithNoActualAVData = (
            DEFINE_GUIDNAMED(EVENTID_DFNWithNoActualAVData)
        )

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA Stream Format GUIDs
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_KSDATAFORMAT_TYPE_BDA_ANTENNA = (
            0x71985F41,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSDATAFORMAT_TYPE_BDA_ANTENNA = DEFINE_GUIDSTRUCT(
            "71985F41-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSDATAFORMAT_TYPE_BDA_ANTENNA = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_BDA_ANTENNA)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT = (
            0xF4AEB342,
            0x0329,
            0x4FDD,
            0xA8,
            0xFD,
            0x4A,
            0xFF,
            0x49,
            0x26,
            0xC9,
            0x78
        )
        KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT = DEFINE_GUIDSTRUCT(
            "F4AEB342-0329-4fdd-A8FD-4AFF4926C978"
        )
        KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_BDA_MPEG2_TRANSPORT)
        )
        STATIC_KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT = (
            0x8DEDA6FD,
            0xAC5F,
            0x4334,
            0x8E,
            0xCF,
            0xA4,
            0xBA,
            0x8F,
            0xA7,
            0xD0,
            0xF0
        )
        KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT = DEFINE_GUIDSTRUCT(
            "8DEDA6FD-AC5F-4334-8ECF-A4BA8FA7D0F0"
        )
        KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SPECIFIER_BDA_TRANSPORT)
        )
        STATIC_KSDATAFORMAT_TYPE_BDA_IF_SIGNAL = (
            0x61BE0B47,
            0xA5EB,
            0x499B,
            0x9A,
            0x85,
            0x5B,
            0x16,
            0xC0,
            0x7F,
            0x12,
            0x58
        )
        KSDATAFORMAT_TYPE_BDA_IF_SIGNAL = DEFINE_GUIDSTRUCT(
            "61BE0B47-A5EB-499b-9A85-5B16C07F1258"
        )
        KSDATAFORMAT_TYPE_BDA_IF_SIGNAL = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_BDA_IF_SIGNAL)
        )
        STATIC_KSDATAFORMAT_TYPE_MPEG2_SECTIONS = (
            0x455F176C,
            0x4B06,
            0x47CE,
            0x9A,
            0xEF,
            0x8C,
            0xAE,
            0xF7,
            0x3D,
            0xF7,
            0xB5
        )
        KSDATAFORMAT_TYPE_MPEG2_SECTIONS = DEFINE_GUIDSTRUCT(
            "455F176C-4B06-47CE-9AEF-8CAEF73DF7B5"
        )
        KSDATAFORMAT_TYPE_MPEG2_SECTIONS = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_MPEG2_SECTIONS)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_ATSC_SI = (
            0xB3C7397C,
            0xD303,
            0x414D,
            0xB3,
            0x3C,
            0x4E,
            0xD2,
            0xC9,
            0xD2,
            0x97,
            0x33
        )
        KSDATAFORMAT_SUBTYPE_ATSC_SI = DEFINE_GUIDSTRUCT(
            "B3C7397C-D303-414D-B33C-4ED2C9D29733"
        )
        KSDATAFORMAT_SUBTYPE_ATSC_SI = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_ATSC_SI)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_DVB_SI = (
            0xE9DD31A3,
            0x221D,
            0x4ADB,
            0x85,
            0x32,
            0x9A,
            0xF3,
            0x9,
            0xC1,
            0xA4,
            0x8
        )
        KSDATAFORMAT_SUBTYPE_DVB_SI = DEFINE_GUIDSTRUCT(
            "e9dd31a3-221d-4adb-8532-9af309c1a408"
        )
        KSDATAFORMAT_SUBTYPE_DVB_SI = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_DVB_SI)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP = (
            0x762E3F66,
            0x336F,
            0x48D1,
            0xBF,
            0x83,
            0x2B,
            0x0,
            0x35,
            0x2C,
            0x11,
            0xF0
        )
        KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP = DEFINE_GUIDSTRUCT(
            "762E3F66-336F-48d1-BF83-2B00352C11F0"
        )
        KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_PSIP)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP = (
            0x951727DB,
            0xD2CE,
            0x4528,
            0x96,
            0xF6,
            0x33,
            0x1,
            0xFA,
            0xBB,
            0x2D,
            0xE0
        )
        KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP = DEFINE_GUIDSTRUCT(
            "951727DB-D2CE-4528-96F6-3301FABB2DE0"
        )
        KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_BDA_OPENCABLE_OOB_PSIP)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_ISDB_SI = (
            0x4A2EEB99,
            0x6458,
            0x4538,
            0xB1,
            0x87,
            0x04,
            0x01,
            0x7C,
            0x41,
            0x41,
            0x3F
        )
        KSDATAFORMAT_SUBTYPE_ISDB_SI = DEFINE_GUIDSTRUCT(
            "4a2eeb99-6458-4538-b187-04017c41413f"
        )
        KSDATAFORMAT_SUBTYPE_ISDB_SI = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_ISDB_SI)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_PBDA_TRANSPORT_RAW = (
            0x0D7AED42,
            0xCB9A,
            0x11DB,
            0x97,
            0x05,
            0x00,
            0x50,
            0x56,
            0xC0,
            0x00,
            0x08
        )
        KSDATAFORMAT_SUBTYPE_PBDA_TRANSPORT_RAW = DEFINE_GUIDSTRUCT(
            "0d7AED42-CB9A-11DB-9705-005056C00008"
        )
        KSDATAFORMAT_SUBTYPE_PBDA_TRANSPORT_RAW = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_PBDA_TRANSPORT_RAW)
        )

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSPinName Definitions for BDA
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # Pin name for a BDA transport pin
        # {78216A81-CFA8-493e-9711-36A61C08BD9D}
        STATIC_PINNAME_BDA_TRANSPORT = (
            0x78216A81,
            0xCFA8,
            0x493E,
            0x97,
            0x11,
            0x36,
            0xA6,
            0x1C,
            0x8,
            0xBD,
            0x9D
        )
        PINNAME_BDA_TRANSPORT = DEFINE_GUIDSTRUCT(
            "78216A81-CFA8-493e-9711-36A61C08BD9D"
        )
        PINNAME_BDA_TRANSPORT = DEFINE_GUIDNAMED(PINNAME_BDA_TRANSPORT)

        # Pin name for a BDA analog video pin
        # {5C0C8281-5667-486c-8482-63E31F01A6E9}
        STATIC_PINNAME_BDA_ANALOG_VIDEO = (
            0x5C0C8281,
            0x5667,
            0x486C,
            0x84,
            0x82,
            0x63,
            0xE3,
            0x1F,
            0x1,
            0xA6,
            0xE9
        )
        PINNAME_BDA_ANALOG_VIDEO = DEFINE_GUIDSTRUCT(
            "5C0C8281-5667-486c-8482-63E31F01A6E9"
        )
        PINNAME_BDA_ANALOG_VIDEO = DEFINE_GUIDNAMED(PINNAME_BDA_ANALOG_VIDEO)

        # Pin name for a BDA analog audio pin
        # {D28A580A-9B1F-4b0c-9C33-9BF0A8EA636B}
        STATIC_PINNAME_BDA_ANALOG_AUDIO = (
            0xD28A580A,
            0x9B1F,
            0x4B0C,
            0x9C,
            0x33,
            0x9B,
            0xF0,
            0xA8,
            0xEA,
            0x63,
            0x6B
        )
        PINNAME_BDA_ANALOG_AUDIO = DEFINE_GUIDSTRUCT(
            "D28A580A-9B1F-4b0c-9C33-9BF0A8EA636B"
        )
        PINNAME_BDA_ANALOG_AUDIO = DEFINE_GUIDNAMED(PINNAME_BDA_ANALOG_AUDIO)

        # Pin name for a BDA FM Radio pin
        # {D2855FED-B2D3-4eeb-9BD0-193436A2F890}
        STATIC_PINNAME_BDA_FM_RADIO = (
            0xD2855FED,
            0xB2D3,
            0x4EEB,
            0x9B,
            0xD0,
            0x19,
            0x34,
            0x36,
            0xA2,
            0xF8,
            0x90
        )
        PINNAME_BDA_FM_RADIO = DEFINE_GUIDSTRUCT(
            "D2855FED-B2D3-4eeb-9BD0-193436A2F890"
        )
        PINNAME_BDA_FM_RADIO = DEFINE_GUIDNAMED(PINNAME_BDA_FM_RADIO)

        # Pin name for a BDA Intermediate Frequency pin
        # {1A9D4A42-F3CD-48a1-9AEA-71DE133CBE14}
        STATIC_PINNAME_BDA_IF_PIN = (
            0x1A9D4A42,
            0xF3CD,
            0x48A1,
            0x9A,
            0xEA,
            0x71,
            0xDE,
            0x13,
            0x3C,
            0xBE,
            0x14
        )
        PINNAME_BDA_IF_PIN = DEFINE_GUIDSTRUCT(
            "1A9D4A42-F3CD-48a1-9AEA-71DE133CBE14"
        )
        PINNAME_BDA_IF_PIN = DEFINE_GUIDNAMED(PINNAME_BDA_IF_PIN)

        # Pin name for a BDA Open Cable PSIP pin
        # {297BB104-E5C9-4ACE-B123-95C3CBB24D4F}
        STATIC_PINNAME_BDA_OPENCABLE_PSIP_PIN = (
            0x297BB104,
            0xE5C9,
            0x4ACE,
            0xB1,
            0x23,
            0x95,
            0xC3,
            0xCB,
            0xB2,
            0x4D,
            0x4F
        )
        PINNAME_BDA_OPENCABLE_PSIP_PIN = DEFINE_GUIDSTRUCT(
            "297BB104-E5C9-4ACE-B123-95C3CBB24D4F"
        )
        PINNAME_BDA_OPENCABLE_PSIP_PIN = (
            DEFINE_GUIDNAMED(PINNAME_BDA_OPENCABLE_PSIP_PIN)
        )

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # KSProperty Set Definitions for BDA
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # ------------------------------------------------------------
        # BDA Network Ethernet Filter Property Set
        # {71985F43-1CA1-11d3-9CC8-00C04F7971E0}
        STATIC_KSPROPSETID_BdaEthernetFilter = (
            0x71985F43,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSPROPSETID_BdaEthernetFilter = DEFINE_GUIDSTRUCT(
            "71985F43-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSPROPSETID_BdaEthernetFilter = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaEthernetFilter)
        )


        class KSPROPERTY_BDA_ETHERNET_FILTER(ENUM):
            KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST_SIZE = 0
            KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST = 1
            KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_MODE = 2

        KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST_SIZE = KSPROPERTY_BDA_ETHERNET_FILTER.KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST_SIZE
        KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST = KSPROPERTY_BDA_ETHERNET_FILTER.KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST
        KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_MODE = KSPROPERTY_BDA_ETHERNET_FILTER.KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_MODE


        def DEFINE_KSPROPERTY_ITEM_BDA_ETHERNET_FILTER_MULTICAST_LIST_SIZE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST_SIZE,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(ULONG),
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_ETHERNET_FILTER_MULTICAST_LIST(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_LIST,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(BDA_ETHERNET_ADDRESS_LIST),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_ETHERNET_FILTER_MULTICAST_MODE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_ETHERNET_FILTER_MULTICAST_MODE,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(BDA_MULTICAST_MODE),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # BDA Network IPv4 Filter Property Set
        # {71985F44-1CA1-11d3-9CC8-00C04F7971E0}
        STATIC_KSPROPSETID_BdaIPv4Filter = (
            0x71985F44,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSPROPSETID_BdaIPv4Filter = DEFINE_GUIDSTRUCT(
            "71985F44-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSPROPSETID_BdaIPv4Filter = DEFINE_GUIDNAMED(KSPROPSETID_BdaIPv4Filter)


        class KSPROPERTY_BDA_IPv4_FILTER(ENUM):
            KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST_SIZE = 0
            KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST = 1
            KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_MODE = 2

        KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST_SIZE = KSPROPERTY_BDA_IPv4_FILTER.KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST_SIZE
        KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST = KSPROPERTY_BDA_IPv4_FILTER.KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST
        KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_MODE = KSPROPERTY_BDA_IPv4_FILTER.KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_MODE


        def DEFINE_KSPROPERTY_ITEM_BDA_IPv4_FILTER_MULTICAST_LIST_SIZE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST_SIZE,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(ULONG),
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_IPv4_FILTER_MULTICAST_LIST(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_LIST,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(BDA_IPv4_ADDRESS_LIST),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_IPv4_FILTER_MULTICAST_MODE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_IPv4_FILTER_MULTICAST_MODE,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(BDA_MULTICAST_MODE),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # BDA Network IPv6 Filter Property Set
        # {E1785A74-2A23-4fb3-9245-A8F88017EF33}
        STATIC_KSPROPSETID_BdaIPv6Filter = (
            0xE1785A74,
            0x2A23,
            0x4FB3,
            0x92,
            0x45,
            0xA8,
            0xF8,
            0x80,
            0x17,
            0xEF,
            0x33
        )
        KSPROPSETID_BdaIPv6Filter = DEFINE_GUIDSTRUCT(
            "E1785A74-2A23-4fb3-9245-A8F88017EF33"
        )
        KSPROPSETID_BdaIPv6Filter = DEFINE_GUIDNAMED(KSPROPSETID_BdaIPv6Filter)


        class KSPROPERTY_BDA_IPv6_FILTER(ENUM):
            KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST_SIZE = 0
            KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST = 1
            KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_MODE = 2

        KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST_SIZE = KSPROPERTY_BDA_IPv6_FILTER.KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST_SIZE
        KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST = KSPROPERTY_BDA_IPv6_FILTER.KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST
        KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_MODE = KSPROPERTY_BDA_IPv6_FILTER.KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_MODE


        def DEFINE_KSPROPERTY_ITEM_BDA_IPv6_FILTER_MULTICAST_LIST_SIZE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST_SIZE,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(ULONG),
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_IPv6_FILTER_MULTICAST_LIST(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_LIST,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(BDA_IPv6_ADDRESS_LIST),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_IPv6_FILTER_MULTICAST_MODE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_IPv6_FILTER_MULTICAST_MODE,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(BDA_MULTICAST_MODE),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # BDA Signal Statistics Property Set
        # Used to get signal statistics from a control node or a pin.
        # Set NodeId == -1 to get properties from the pin.
        # {1347D106-CF3A-428a-A5CB-AC0D9A2A4338}
        STATIC_KSPROPSETID_BdaSignalStats = (
            0x1347D106,
            0xCF3A,
            0x428A,
            0xA5,
            0xCB,
            0xAC,
            0xD,
            0x9A,
            0x2A,
            0x43,
            0x38
        )
        KSPROPSETID_BdaSignalStats = DEFINE_GUIDSTRUCT(
            "1347D106-CF3A-428a-A5CB-AC0D9A2A4338"
        )
        KSPROPSETID_BdaSignalStats = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaSignalStats)
        )


        class KSPROPERTY_BDA_SIGNAL_STATS(ENUM):
            KSPROPERTY_BDA_SIGNAL_STRENGTH = 0
            KSPROPERTY_BDA_SIGNAL_QUALITY = 1
            KSPROPERTY_BDA_SIGNAL_PRESENT = 2
            KSPROPERTY_BDA_SIGNAL_LOCKED = 3
            KSPROPERTY_BDA_SAMPLE_TIME = 4
            KSPROPERTY_BDA_SIGNAL_LOCK_CAPS = 5
            KSPROPERTY_BDA_SIGNAL_LOCK_TYPE = 6

        KSPROPERTY_BDA_SIGNAL_STRENGTH = KSPROPERTY_BDA_SIGNAL_STATS.KSPROPERTY_BDA_SIGNAL_STRENGTH
        KSPROPERTY_BDA_SIGNAL_QUALITY = KSPROPERTY_BDA_SIGNAL_STATS.KSPROPERTY_BDA_SIGNAL_QUALITY
        KSPROPERTY_BDA_SIGNAL_PRESENT = KSPROPERTY_BDA_SIGNAL_STATS.KSPROPERTY_BDA_SIGNAL_PRESENT
        KSPROPERTY_BDA_SIGNAL_LOCKED = KSPROPERTY_BDA_SIGNAL_STATS.KSPROPERTY_BDA_SIGNAL_LOCKED
        KSPROPERTY_BDA_SAMPLE_TIME = KSPROPERTY_BDA_SIGNAL_STATS.KSPROPERTY_BDA_SAMPLE_TIME
        KSPROPERTY_BDA_SIGNAL_LOCK_CAPS = KSPROPERTY_BDA_SIGNAL_STATS.KSPROPERTY_BDA_SIGNAL_LOCK_CAPS
        KSPROPERTY_BDA_SIGNAL_LOCK_TYPE = KSPROPERTY_BDA_SIGNAL_STATS.KSPROPERTY_BDA_SIGNAL_LOCK_TYPE


        class _BdaLockType(ENUM):
            Bda_LockType_None = 0x00
            Bda_LockType_PLL = 0x01
            Bda_LockType_DecoderDemod = 0x02
            Bda_LockType_Complete = 0x80

        BDA_LockType = _BdaLockType

        # OPTIONAL
        # Carrier strength in mDb (1/1000 of a DB).
        # A strength of 0 is nominal strength as expected for the given
        # type of broadcast network.
        # Sub-nominal strengths are reported as positive mDb
        # Super-nominal strengths are reported as negative mDb
        def DEFINE_KSPROPERTY_ITEM_BDA_SIGNAL_STRENGTH(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SIGNAL_STRENGTH,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(LONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # OPTIONAL
        # Amount of data successfully extracted from the signal as a percent.
        # Signal Quality is usually reported by the demodulation node and is
        # a representation of how much of the original data could be extracted
        # from the signal.
        # In the case of Analog Signals, this percentage can be
        # computed by examining the timing of HSync and VSync as will as by
        # looking at information contained in HBlanking and VBlanking
        # intervals.
        # In the case of Digital Signals, this percentage can be
        # computed by examining packet CRCs and FEC confidence values.
        # 100 percent is ideal.
        # 95 percent shows very little (almost unnoticable) artifacts when
        # rendered.
        # 90 percent contains few enough artifacts as to be easily viewable.
        # 80 percent is the minimum level to be viewable.
        # 60 percent is the minimum level to expect data services
        # (including EPG) to work.
        # 20 percent indicates that the demodulator knows that a properly
        # modulated
        # signal exists but can't produce enough data to be useful.
        def DEFINE_KSPROPERTY_ITEM_BDA_SIGNAL_QUALITY(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SIGNAL_QUALITY,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(LONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # REQUIRED
        # True if a signal carrier is present.
        # Should be returned by the RF tuner node.
        def DEFINE_KSPROPERTY_ITEM_BDA_SIGNAL_PRESENT(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SIGNAL_PRESENT,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BOOL),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # REQUIRED
        # True if the signal can be locked.
        # Ususally represents PLL lock when returned by the RF Tuner Node.
        # Represents Signal Quality of at least 20% when returned by the
        # demodulator node.
        def DEFINE_KSPROPERTY_ITEM_BDA_SIGNAL_LOCKED(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SIGNAL_LOCKED,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BOOL),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # OPTIONAL
        # Indicates the sample time overwhich signal level and quality are
        # averaged.
        # Each time a signal statistics property is requested, the node should
        # report the average value for the last n milliseconds where n is the
        # value set by this property. If no value is set or if the driver does
        # not support this property, the driver should default to
        # 100 millisecond sample times.
        # The driver may report values for the most recently completed sample
        # period.
        def DEFINE_KSPROPERTY_ITEM_BDA_SAMPLE_TIME(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SAMPLE_TIME,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(LONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # REQUIRED
        # returns a bitmask of supported BDA_LockType_ values
        # Should be returned by the RF tuner node.
        def DEFINE_KSPROPERTY_ITEM_BDA_SIGNAL_LOCK_CAPS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SIGNAL_LOCK_CAPS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BOOL),
                NULL,
                NULL,
                0,
                NULL,
                NULL,
                0,
            )


        # REQUIRED
        # returns current BDA_LockType_ value
        # Should be returned by the RF tuner node.
        def DEFINE_KSPROPERTY_ITEM_BDA_SIGNAL_LOCK_TYPE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SIGNAL_LOCK_TYPE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_LockType),
                NULL,
                NULL,
                0,
                NULL,
                NULL,
                0,
            )


        # ------------------------------------------------------------
        # BDA Change Sync Method Set
        # {FD0A5AF3-B41D-11d2-9C95-00C04F7971E0}
        STATIC_KSMETHODSETID_BdaChangeSync = (
            0xFD0A5AF3,
            0xB41D,
            0x11D2,
            0x9C,
            0x95,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSMETHODSETID_BdaChangeSync = DEFINE_GUIDSTRUCT(
            "FD0A5AF3-B41D-11d2-9C95-00C04F7971E0"
        )
        KSMETHODSETID_BdaChangeSync = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaChangeSync)
        )


        class KSMETHOD_BDA_CHANGE_SYNC(ENUM):
            KSMETHOD_BDA_START_CHANGES = 0
            KSMETHOD_BDA_CHECK_CHANGES = 1
            KSMETHOD_BDA_COMMIT_CHANGES = 2
            KSMETHOD_BDA_GET_CHANGE_STATE = 3

        KSMETHOD_BDA_START_CHANGES = KSMETHOD_BDA_CHANGE_SYNC.KSMETHOD_BDA_START_CHANGES
        KSMETHOD_BDA_CHECK_CHANGES = KSMETHOD_BDA_CHANGE_SYNC.KSMETHOD_BDA_CHECK_CHANGES
        KSMETHOD_BDA_COMMIT_CHANGES = KSMETHOD_BDA_CHANGE_SYNC.KSMETHOD_BDA_COMMIT_CHANGES
        KSMETHOD_BDA_GET_CHANGE_STATE = KSMETHOD_BDA_CHANGE_SYNC.KSMETHOD_BDA_GET_CHANGE_STATE


        def DEFINE_KSMETHOD_ITEM_BDA_START_CHANGES(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_START_CHANGES,
                KSMETHOD_TYPE_NONE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                0,
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_CHECK_CHANGES(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_CHECK_CHANGES,
                KSMETHOD_TYPE_NONE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                0,
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_COMMIT_CHANGES(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_COMMIT_CHANGES,
                KSMETHOD_TYPE_NONE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                0,
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_GET_CHANGE_STATE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GET_CHANGE_STATE,
                KSMETHOD_TYPE_READ,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                0,
                SupportHandler,
            )


        # ------------------------------------------------------------
        # BDA Device Configuration Method Set
        # {71985F45-1CA1-11d3-9CC8-00C04F7971E0}
        STATIC_KSMETHODSETID_BdaDeviceConfiguration = (
            0x71985F45,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSMETHODSETID_BdaDeviceConfiguration = DEFINE_GUIDSTRUCT(
            "71985F45-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSMETHODSETID_BdaDeviceConfiguration = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaDeviceConfiguration)
        )


        class KSMETHOD_BDA_DEVICE_CONFIGURATION(ENUM):
            KSMETHOD_BDA_CREATE_PIN_FACTORY = 0
            KSMETHOD_BDA_DELETE_PIN_FACTORY = 1
            KSMETHOD_BDA_CREATE_TOPOLOGY = 2

        KSMETHOD_BDA_CREATE_PIN_FACTORY = KSMETHOD_BDA_DEVICE_CONFIGURATION.KSMETHOD_BDA_CREATE_PIN_FACTORY
        KSMETHOD_BDA_DELETE_PIN_FACTORY = KSMETHOD_BDA_DEVICE_CONFIGURATION.KSMETHOD_BDA_DELETE_PIN_FACTORY
        KSMETHOD_BDA_CREATE_TOPOLOGY = KSMETHOD_BDA_DEVICE_CONFIGURATION.KSMETHOD_BDA_CREATE_TOPOLOGY


        def DEFINE_KSMETHOD_ITEM_BDA_CREATE_PIN_FACTORY(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_CREATE_PIN_FACTORY,
                KSMETHOD_TYPE_READ,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_PIN),
                ctypes.sizeof(ULONG),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_DELETE_PIN_FACTORY(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_DELETE_PIN_FACTORY,
                KSMETHOD_TYPE_NONE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_PIN),
                0,
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_CREATE_TOPOLOGY(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_CREATE_TOPOLOGY,
                KSMETHOD_TYPE_WRITE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_PIN_PAIR),
                0,
                SupportHandler,
            )


        # ------------------------------------------------------------
        # BDA Topology Property Set
        # {A14EE835-0A23-11d3-9CC7-00C04F7971E0}
        STATIC_KSPROPSETID_BdaTopology = (
            0xA14EE835,
            0x0A23,
            0x11D3,
            0x9C,
            0xC7,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSPROPSETID_BdaTopology = DEFINE_GUIDSTRUCT(
            "A14EE835-0A23-11d3-9CC7-00C04F7971E0"
        )
        KSPROPSETID_BdaTopology = DEFINE_GUIDNAMED(KSPROPSETID_BdaTopology)


        class KSPROPERTY_BDA_TOPOLOGY(ENUM):
            KSPROPERTY_BDA_NODE_TYPES = 1
            KSPROPERTY_BDA_PIN_TYPES = 2
            KSPROPERTY_BDA_TEMPLATE_CONNECTIONS = 3
            KSPROPERTY_BDA_NODE_METHODS = 4
            KSPROPERTY_BDA_NODE_PROPERTIES = 5
            KSPROPERTY_BDA_NODE_EVENTS = 6
            KSPROPERTY_BDA_CONTROLLING_PIN_ID = 7
            KSPROPERTY_BDA_NODE_DESCRIPTORS = 8

        KSPROPERTY_BDA_NODE_TYPES = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_NODE_TYPES
        KSPROPERTY_BDA_PIN_TYPES = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_PIN_TYPES
        KSPROPERTY_BDA_TEMPLATE_CONNECTIONS = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_TEMPLATE_CONNECTIONS
        KSPROPERTY_BDA_NODE_METHODS = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_NODE_METHODS
        KSPROPERTY_BDA_NODE_PROPERTIES = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_NODE_PROPERTIES
        KSPROPERTY_BDA_NODE_EVENTS = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_NODE_EVENTS
        KSPROPERTY_BDA_CONTROLLING_PIN_ID = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_CONTROLLING_PIN_ID
        KSPROPERTY_BDA_NODE_DESCRIPTORS = KSPROPERTY_BDA_TOPOLOGY.KSPROPERTY_BDA_NODE_DESCRIPTORS


        def DEFINE_KSPROPERTY_ITEM_BDA_NODE_TYPES(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_NODE_TYPES,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                0,
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_PIN_TYPES(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_PIN_TYPES, GetHandler, ctypes.sizeof(KSPROPERTY), 0, FALSE, NULL, 0, NULL, NULL, 0)



        def DEFINE_KSPROPERTY_ITEM_BDA_TEMPLATE_CONNECTIONS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_TEMPLATE_CONNECTIONS,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(BDA_TEMPLATE_CONNECTION),
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0,
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_NODE_METHODS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_NODE_METHODS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                0,
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_NODE_PROPERTIES(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_NODE_PROPERTIES,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                0,
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0
            )



        def DEFINE_KSPROPERTY_ITEM_BDA_NODE_EVENTS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_NODE_EVENTS, GetHandler, ctypes.sizeof(KSP_NODE), 0, FALSE, NULL, 0, NULL, NULL, 0)



        def DEFINE_KSPROPERTY_ITEM_BDA_CONTROLLING_PIN_ID(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_CONTROLLING_PIN_ID,
                GetHandler,
                ctypes.sizeof(KSP_BDA_NODE_PIN),
                ctypes.sizeof(ULONG),
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0,
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_NODE_DESCRIPTORS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_NODE_DESCRIPTORS, GetHandler, ctypes.sizeof(KSPROPERTY), 0, FALSE, NULL, 0, NULL, NULL, 0)



        # ------------------------------------------------------------
        # BDA Pin Control Property Set
        # {0DED49D5-A8B7-4d5d-97A1-12B0C195874D}
        STATIC_KSPROPSETID_BdaPinControl = (
            0xDED49D5,
            0xA8B7,
            0x4D5D,
            0x97,
            0xA1,
            0x12,
            0xB0,
            0xC1,
            0x95,
            0x87,
            0x4D
        )
        KSPROPSETID_BdaPinControl = DEFINE_GUIDSTRUCT(
            "0DED49D5-A8B7-4d5d-97A1-12B0C195874D"
        )
        KSPROPSETID_BdaPinControl = DEFINE_GUIDNAMED(KSPROPSETID_BdaPinControl)


        class KSPROPERTY_BDA_PIN_CONTROL(ENUM):
            KSPROPERTY_BDA_PIN_ID = 0
            KSPROPERTY_BDA_PIN_TYPE = 1

        KSPROPERTY_BDA_PIN_ID = KSPROPERTY_BDA_PIN_CONTROL.KSPROPERTY_BDA_PIN_ID
        KSPROPERTY_BDA_PIN_TYPE = KSPROPERTY_BDA_PIN_CONTROL.KSPROPERTY_BDA_PIN_TYPE


        def DEFINE_KSPROPERTY_ITEM_BDA_PIN_ID(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_PIN_ID,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(ULONG),
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0,
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_PIN_TYPE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_PIN_TYPE,
                GetHandler,
                ctypes.sizeof(KSPROPERTY),
                ctypes.sizeof(ULONG),
                FALSE,
                NULL,
                0,
                NULL,
                NULL,
                0,
            )


        # ------------------------------------------------------------
        # BDA Pin Event Set
        # {104781CD-50BD-40d5-95FB-087E0E86A591}
        STATIC_KSEVENTSETID_BdaPinEvent = (
            0x104781CD,
            0x50BD,
            0x40D5,
            0x95,
            0xFB,
            0x08,
            0x7E,
            0xE,
            0x86,
            0xA5,
            0x91
        )
        KSEVENTSETID_BdaPinEvent = DEFINE_GUIDSTRUCT(
            "104781CD-50BD-40d5-95FB-087E0E86A591"
        )
        KSEVENTSETID_BdaPinEvent = DEFINE_GUIDNAMED(KSEVENTSETID_BdaPinEvent)


        class KSPROPERTY_BDA_PIN_EVENT(ENUM):
            KSEVENT_BDA_PIN_CONNECTED = 0
            KSEVENT_BDA_PIN_DISCONNECTED = 1

        KSEVENT_BDA_PIN_CONNECTED = KSPROPERTY_BDA_PIN_EVENT.KSEVENT_BDA_PIN_CONNECTED
        KSEVENT_BDA_PIN_DISCONNECTED = KSPROPERTY_BDA_PIN_EVENT.KSEVENT_BDA_PIN_DISCONNECTED


        def DEFINE_KSEVENT_ITEM_BDA_PIN_CONNECTED(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_PIN_CONNECTED, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)



        def DEFINE_KSEVENT_ITEM_BDA_PIN_DISCONNECTED(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_PIN_DISCONNECTED, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)



        # ------------------------------------------------------------
        # BDA Void Transform Property Set
        # {71985F46-1CA1-11d3-9CC8-00C04F7971E0}
        STATIC_KSPROPSETID_BdaVoidTransform = (
            0x71985F46,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSPROPSETID_BdaVoidTransform = DEFINE_GUIDSTRUCT(
            "71985F46-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSPROPSETID_BdaVoidTransform = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaVoidTransform)
        )


        class KSPROPERTY_BDA_VOID_TRANSFORM(ENUM):
            KSPROPERTY_BDA_VOID_TRANSFORM_START = 0
            KSPROPERTY_BDA_VOID_TRANSFORM_STOP = 1

        KSPROPERTY_BDA_VOID_TRANSFORM_START = KSPROPERTY_BDA_VOID_TRANSFORM.KSPROPERTY_BDA_VOID_TRANSFORM_START
        KSPROPERTY_BDA_VOID_TRANSFORM_STOP = KSPROPERTY_BDA_VOID_TRANSFORM.KSPROPERTY_BDA_VOID_TRANSFORM_STOP


        def DEFINE_KSPROPERTY_ITEM_BDA_VOID_TRANSFORM_START(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_VOID_TRANSFORM_START, FALSE, ctypes.sizeof(KSPROPERTY), 0, SetHandler, NULL, 0, NULL, NULL, 0)



        def DEFINE_KSPROPERTY_ITEM_BDA_VOID_TRANSFORM_STOP(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_VOID_TRANSFORM_STOP, FALSE, ctypes.sizeof(KSPROPERTY), 0, SetHandler, NULL, 0, NULL, NULL, 0)



        # ------------------------------------------------------------
        # BDA Null Transform Property Set
        # {DDF15B0D-BD25-11d2-9CA0-00C04F7971E0}
        STATIC_KSPROPSETID_BdaNullTransform = (
            0xDDF15B0D,
            0xBD25,
            0x11D2,
            0x9C,
            0xA0,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSPROPSETID_BdaNullTransform = DEFINE_GUIDSTRUCT(
            "DDF15B0D-BD25-11d2-9CA0-00C04F7971E0"
        )
        KSPROPSETID_BdaNullTransform = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaNullTransform)
        )


        class KSPROPERTY_BDA_NULL_TRANSFORM(ENUM):
            KSPROPERTY_BDA_NULL_TRANSFORM_START = 0
            KSPROPERTY_BDA_NULL_TRANSFORM_STOP = 1

        KSPROPERTY_BDA_NULL_TRANSFORM_START = KSPROPERTY_BDA_NULL_TRANSFORM.KSPROPERTY_BDA_NULL_TRANSFORM_START
        KSPROPERTY_BDA_NULL_TRANSFORM_STOP = KSPROPERTY_BDA_NULL_TRANSFORM.KSPROPERTY_BDA_NULL_TRANSFORM_STOP


        def DEFINE_KSPROPERTY_ITEM_BDA_NULL_TRANSFORM_START(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_NULL_TRANSFORM_START, FALSE, ctypes.sizeof(KSPROPERTY), 0, SetHandler, NULL, 0, NULL, NULL, 0)



        def DEFINE_KSPROPERTY_ITEM_BDA_NULL_TRANSFORM_STOP(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_NULL_TRANSFORM_STOP, FALSE, ctypes.sizeof(KSPROPERTY), 0, SetHandler, NULL, 0, NULL, NULL, 0)



        # ------------------------------------------------------------
        # BDA Frequency Filter Property Set
        # {71985F47-1CA1-11d3-9CC8-00C04F7971E0}
        STATIC_KSPROPSETID_BdaFrequencyFilter = (
            0x71985F47,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSPROPSETID_BdaFrequencyFilter = DEFINE_GUIDSTRUCT(
            "71985F47-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSPROPSETID_BdaFrequencyFilter = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaFrequencyFilter)
        )


        class KSPROPERTY_BDA_FREQUENCY_FILTER(ENUM):
            KSPROPERTY_BDA_RF_TUNER_FREQUENCY = 0
            KSPROPERTY_BDA_RF_TUNER_POLARITY = 1
            KSPROPERTY_BDA_RF_TUNER_RANGE = 2
            KSPROPERTY_BDA_RF_TUNER_TRANSPONDER = 3
            KSPROPERTY_BDA_RF_TUNER_BANDWIDTH = 4
            KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER = 5
            KSPROPERTY_BDA_RF_TUNER_CAPS = 6
            KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS = 7
            KSPROPERTY_BDA_RF_TUNER_STANDARD = 8
            KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE = 9

        KSPROPERTY_BDA_RF_TUNER_FREQUENCY = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_FREQUENCY
        KSPROPERTY_BDA_RF_TUNER_POLARITY = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_POLARITY
        KSPROPERTY_BDA_RF_TUNER_RANGE = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_RANGE
        KSPROPERTY_BDA_RF_TUNER_TRANSPONDER = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_TRANSPONDER
        KSPROPERTY_BDA_RF_TUNER_BANDWIDTH = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_BANDWIDTH
        KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER
        KSPROPERTY_BDA_RF_TUNER_CAPS = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_CAPS
        KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS
        KSPROPERTY_BDA_RF_TUNER_STANDARD = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_STANDARD
        KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE = KSPROPERTY_BDA_FREQUENCY_FILTER.KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE


        class _BdaSignalType(ENUM):
            Bda_SignalType_Unknown = 0
            Bda_SignalType_Analog = 1
            Bda_SignalType_Digital = 2

        BDA_SignalType = _BdaSignalType


        # The BDA_DigitalSignalStandard enumeration is tentatively put out for
        # Beta review
        # Based on feedback, this may be updated or entirely removed in a
        # later release
        class BDA_DigitalSignalStandard(ENUM):
            Bda_DigitalStandard_None = 0x00000000
            Bda_DigitalStandard_DVB_T = 0x00000001
            Bda_DigitalStandard_DVB_S = 0x00000002
            Bda_DigitalStandard_DVB_C = 0x00000004
            Bda_DigitalStandard_ATSC = 0x00000008
            Bda_DigitalStandard_ISDB_T = 0x00000010
            Bda_DigitalStandard_ISDB_S = 0x00000020
            Bda_DigitalStandard_ISDB_C = 0x00000040

        Bda_DigitalStandard_None = BDA_DigitalSignalStandard.Bda_DigitalStandard_None
        Bda_DigitalStandard_DVB_T = BDA_DigitalSignalStandard.Bda_DigitalStandard_DVB_T
        Bda_DigitalStandard_DVB_S = BDA_DigitalSignalStandard.Bda_DigitalStandard_DVB_S
        Bda_DigitalStandard_DVB_C = BDA_DigitalSignalStandard.Bda_DigitalStandard_DVB_C
        Bda_DigitalStandard_ATSC = BDA_DigitalSignalStandard.Bda_DigitalStandard_ATSC
        Bda_DigitalStandard_ISDB_T = BDA_DigitalSignalStandard.Bda_DigitalStandard_ISDB_T
        Bda_DigitalStandard_ISDB_S = BDA_DigitalSignalStandard.Bda_DigitalStandard_ISDB_S
        Bda_DigitalStandard_ISDB_C = BDA_DigitalSignalStandard.Bda_DigitalStandard_ISDB_C

        KSPROPERTY_BDA_RF_TUNER_CAPS_S._fields_ = [
            ('Property', KSP_NODE),
            # IN: KSPROPERTY_TUNER_MODE
            ('Mode', ULONG),
            # Bda_AnalogStandard_* (if TV or DSS)
            ('AnalogStandardsSupported', ULONG),
            # Bda_DigitalStandard_*
            ('DigitalStandardsSupported', ULONG),
            # R - Hz
            ('MinFrequency', ULONG),
            # R - Hz
            ('MaxFrequency', ULONG),
            # R - milliSeconds to settle for any sort of update to the tuner
            ('SettlingTime', ULONG),
            # R - max range (kHz) in which tuner can detect an analog signal
            ('AnalogSensingRange', ULONG),
            # R - max range (kHz) in which tuner can detect an digital signal
            ('DigitalSensingRange', ULONG),
            # R - max time to lock in to a signal 1MHz away assuming the
            # signal has been detected, but its offset is unknown
            ('MilliSecondsPerMHz', ULONG),
        ]

        KSPROPERTY_BDA_RF_TUNER_SCAN_STATUS_S._fields_ = [
            ('Property', KSP_NODE),
            # R - current frequency
            ('CurrentFrequency', ULONG),
            # R - lower limit of range left to scan
            ('FrequencyRangeMin', ULONG),
            # R - upper limit of range left to scan
            ('FrequencyRangeMax', ULONG),
            # R - time left to complete scanning
            ('MilliSecondsLeft', ULONG),
        ]

        KSPROPERTY_BDA_RF_TUNER_STANDARD_S._fields_ = [
            ('Property', KSP_NODE),
            # RW - specifies whether the signal is Analog or Digital. this is
            # required to interpret the SignalStandard field
            ('SignalType', BDA_SignalType),
            # RW - current signal standard
            # (KS_AnalogVideo_* or Bda_DigitalStandard_*) set by the
            # application or detected by the device
            ('SignalStandard', ULONG),
        ]

        KSPROPERTY_BDA_RF_TUNER_STANDARD_MODE_S._fields_ = [
            ('Property', KSP_NODE),
            # RW - specifies whether the driver is in auto-detect mode for the
            # signal standard
            ('AutoDetect', BOOL),
        ]


        def DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_FREQUENCY(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_RF_TUNER_FREQUENCY,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_POLARITY(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_RF_TUNER_POLARITY,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_RANGE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_RF_TUNER_RANGE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_TRANSPONDER(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_RF_TUNER_TRANSPONDER,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_BANDWIDTH(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_RF_TUNER_BANDWIDTH,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_FREQUENCY_MULTIPLIER(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # BDA Tuner Event Set
        # {AAB59E17-01C9-4ebf-93F2-FC3B79B46F91}
        STATIC_KSEVENTSETID_BdaTunerEvent = (
            0xAAB59E17,
            0x1C9,
            0x4EBF,
            0x93,
            0xF2,
            0xFC,
            0x3B,
            0x79,
            0xB4,
            0x6F,
            0x91
        )
        KSEVENTSETID_BdaTunerEvent = DEFINE_GUIDSTRUCT(
            "AAB59E17-01C9-4ebf-93F2-FC3B79B46F91"
        )
        KSEVENTSETID_BdaTunerEvent = (
            DEFINE_GUIDNAMED(KSEVENTSETID_BdaTunerEvent)
        )


        class KSEVENT_BDA_TUNER(ENUM):
            KSEVENT_BDA_TUNER_SCAN = 0

        KSEVENT_BDA_TUNER_SCAN = KSEVENT_BDA_TUNER.KSEVENT_BDA_TUNER_SCAN

        KSEVENTDATA_BDA_RF_TUNER_SCAN_S._fields_ = [
            ('EventData', KSEVENTDATA),
            # W - initial frequency for the scan
            ('StartFrequency', ULONG),
            # W - final frequency for the scan, can be less than the initial
            # value indicating a "scan down" is requested
            ('EndFrequency', ULONG),
            # W - whether the device should look for just a PLL lock, decoder
            # lock, etc. should be a supported lock type.
            ('LockRequested', BDA_LockType),
        ]

        # ------------------------------------------------------------
        # BDA LNB Info Property Set
        # {992CF102-49F9-4719-A664-C4F23E2408F4}
        STATIC_KSPROPSETID_BdaLNBInfo = (
            0x992CF102,
            0x49F9,
            0x4719,
            0xA6,
            0x64,
            0xC4,
            0xF2,
            0x3E,
            0x24,
            0x8,
            0xF4
        )
        KSPROPSETID_BdaLNBInfo = DEFINE_GUIDSTRUCT(
            "992CF102-49F9-4719-A664-C4F23E2408F4"
        )
        KSPROPSETID_BdaLNBInfo = DEFINE_GUIDNAMED(KSPROPSETID_BdaLNBInfo)


        class KSPROPERTY_BDA_LNB_INFO(ENUM):
            KSPROPERTY_BDA_LNB_LOF_LOW_BAND = 0
            KSPROPERTY_BDA_LNB_LOF_HIGH_BAND = 1
            KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY = 2

        KSPROPERTY_BDA_LNB_LOF_LOW_BAND = KSPROPERTY_BDA_LNB_INFO.KSPROPERTY_BDA_LNB_LOF_LOW_BAND
        KSPROPERTY_BDA_LNB_LOF_HIGH_BAND = KSPROPERTY_BDA_LNB_INFO.KSPROPERTY_BDA_LNB_LOF_HIGH_BAND
        KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY = KSPROPERTY_BDA_LNB_INFO.KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY


        def DEFINE_KSPROPERTY_ITEM_BDA_LNB_LOF_LOW_BAND(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_LNB_LOF_LOW_BAND,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_LNB_LOF_HIGH_BAND(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_LNB_LOF_HIGH_BAND,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_LNB_SWITCH_FREQUENCY(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # DiseqC Specific commands and source selection
        # DVB-S applications can use the commands to select there LNB Source
        # or control there installation equipment (e.g. motor dish, switches)
        # {F84E2AB0-3C6B-45e3-A0FC-8669D4B81F11}
        STATIC_KSPROPSETID_BdaDiseqCommand = (
            0xF84E2AB0,
            0x3C6B,
            0x45E3,
            0xA0,
            0xFC,
            0x86,
            0x69,
            0xD4,
            0xB8,
            0x1F,
            0x11
        )
        KSPROPSETID_BdaDiseqCommand = DEFINE_GUIDSTRUCT(
            "F84E2AB0-3C6B-45e3-A0FC-8669D4B81F11"
        )
        KSPROPSETID_BdaDiseqCommand = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaDiseqCommand)
        )


        class KSPROPERTY_BDA_DISEQC_COMMAND(ENUM):
            KSPROPERTY_BDA_DISEQC_ENABLE = 0
            KSPROPERTY_BDA_DISEQC_LNB_SOURCE = 1
            KSPROPERTY_BDA_DISEQC_USETONEBURST = 2
            KSPROPERTY_BDA_DISEQC_REPEATS = 3
            KSPROPERTY_BDA_DISEQC_SEND = 4
            KSPROPERTY_BDA_DISEQC_RESPONSE = 5

        KSPROPERTY_BDA_DISEQC_ENABLE = KSPROPERTY_BDA_DISEQC_COMMAND.KSPROPERTY_BDA_DISEQC_ENABLE
        KSPROPERTY_BDA_DISEQC_LNB_SOURCE = KSPROPERTY_BDA_DISEQC_COMMAND.KSPROPERTY_BDA_DISEQC_LNB_SOURCE
        KSPROPERTY_BDA_DISEQC_USETONEBURST = KSPROPERTY_BDA_DISEQC_COMMAND.KSPROPERTY_BDA_DISEQC_USETONEBURST
        KSPROPERTY_BDA_DISEQC_REPEATS = KSPROPERTY_BDA_DISEQC_COMMAND.KSPROPERTY_BDA_DISEQC_REPEATS
        KSPROPERTY_BDA_DISEQC_SEND = KSPROPERTY_BDA_DISEQC_COMMAND.KSPROPERTY_BDA_DISEQC_SEND
        KSPROPERTY_BDA_DISEQC_RESPONSE = KSPROPERTY_BDA_DISEQC_COMMAND.KSPROPERTY_BDA_DISEQC_RESPONSE


        def DEFINE_KSPROPERTY_ITEM_BDA_DISEQC_ENABLE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_DISEQC_ENABLE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BOOL),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_DISEQC_LNB_SOURCE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_DISEQC_LNB_SOURCE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_DISEQC_USETONEBURST(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_DISEQC_USETONEBURST,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BOOL),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_DISEQC_REPEATS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_DISEQC_REPEATS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_DISEQC_SEND(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_DISEQC_SEND,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_DISEQC_SEND),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_DISEQC_RESPONSE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_DISEQC_RESPONSE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_DISEQC_RESPONSE),
                NULL,
                NULL,
                0,
                NULL,
                NULL,
                0,
            )


        # ------------------------------------------------------------
        # BDA DiseqC Event Set
        # {8B19BBF0-4184-43ac-AD3C-0C889BE4C212}
        STATIC_KSEVENTSETID_BdaDiseqCEvent = (
            0x8B19BBF0,
            0x4184,
            0x43AC,
            0xAD,
            0x3C,
            0xC,
            0x88,
            0x9B,
            0xE4,
            0xC2,
            0x12
        )
        KSEVENTSETID_BdaDiseqCEvent = DEFINE_GUIDSTRUCT(
            "8B19BBF0-4184-43ac-AD3C-0C889BE4C212"
        )
        KSEVENTSETID_BdaDiseqCEvent = (
            DEFINE_GUIDNAMED(KSEVENTSETID_BdaDiseqCEvent)
        )


        class KSPROPERTY_BDA_DISEQC_EVENT(ENUM):
            KSEVENT_BDA_DISEQC_DATA_RECEIVED = 0

        KSEVENT_BDA_DISEQC_DATA_RECEIVED = KSPROPERTY_BDA_DISEQC_EVENT.KSEVENT_BDA_DISEQC_DATA_RECEIVED


        def DEFINE_KSEVENT_BDA_DISEQC_DATA_RECEIVED(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_DISEQC_DATA_RECEIVED, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)



        # ------------------------------------------------------------
        # BDA Digital Demodulator Property Set
        # {EF30F379-985B-4d10-B640-A79D5E04E1E0}
        STATIC_KSPROPSETID_BdaDigitalDemodulator = (
            0xEF30F379,
            0x985B,
            0x4D10,
            0xB6,
            0x40,
            0xA7,
            0x9D,
            0x5E,
            0x4,
            0xE1,
            0xE0
        )
        KSPROPSETID_BdaDigitalDemodulator = DEFINE_GUIDSTRUCT(
            "EF30F379-985B-4d10-B640-A79D5E04E1E0"
        )
        KSPROPSETID_BdaDigitalDemodulator = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaDigitalDemodulator)
        )


        class KSPROPERTY_BDA_DIGITAL_DEMODULATOR(ENUM):
            KSPROPERTY_BDA_MODULATION_TYPE = 0
            KSPROPERTY_BDA_INNER_FEC_TYPE = 1
            KSPROPERTY_BDA_INNER_FEC_RATE = 2
            KSPROPERTY_BDA_OUTER_FEC_TYPE = 3
            KSPROPERTY_BDA_OUTER_FEC_RATE = 4
            KSPROPERTY_BDA_SYMBOL_RATE = 5
            KSPROPERTY_BDA_SPECTRAL_INVERSION = 6
            KSPROPERTY_BDA_GUARD_INTERVAL = 7
            KSPROPERTY_BDA_TRANSMISSION_MODE = 8
            KSPROPERTY_BDA_ROLL_OFF = 9
            KSPROPERTY_BDA_PILOT = 10
            KSPROPERTY_BDA_SIGNALTIMEOUTS = 11
            KSPROPERTY_BDA_PLP_NUMBER = 12

        KSPROPERTY_BDA_MODULATION_TYPE = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_MODULATION_TYPE
        KSPROPERTY_BDA_INNER_FEC_TYPE = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_INNER_FEC_TYPE
        KSPROPERTY_BDA_INNER_FEC_RATE = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_INNER_FEC_RATE
        KSPROPERTY_BDA_OUTER_FEC_TYPE = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_OUTER_FEC_TYPE
        KSPROPERTY_BDA_OUTER_FEC_RATE = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_OUTER_FEC_RATE
        KSPROPERTY_BDA_SYMBOL_RATE = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_SYMBOL_RATE
        KSPROPERTY_BDA_SPECTRAL_INVERSION = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_SPECTRAL_INVERSION
        KSPROPERTY_BDA_GUARD_INTERVAL = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_GUARD_INTERVAL
        KSPROPERTY_BDA_TRANSMISSION_MODE = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_TRANSMISSION_MODE
        KSPROPERTY_BDA_ROLL_OFF = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_ROLL_OFF
        KSPROPERTY_BDA_PILOT = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_PILOT
        KSPROPERTY_BDA_SIGNALTIMEOUTS = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_SIGNALTIMEOUTS
        KSPROPERTY_BDA_PLP_NUMBER = KSPROPERTY_BDA_DIGITAL_DEMODULATOR.KSPROPERTY_BDA_PLP_NUMBER


        def DEFINE_KSPROPERTY_ITEM_BDA_MODULATION_TYPE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_MODULATION_TYPE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ModulationType),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_INNER_FEC_TYPE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_INNER_FEC_TYPE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(FECMethod),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_INNER_FEC_RATE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_INNER_FEC_RATE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BinaryConvolutionCodeRate),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_OUTER_FEC_TYPE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_OUTER_FEC_TYPE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(FECMethod),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_OUTER_FEC_RATE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_OUTER_FEC_RATE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BinaryConvolutionCodeRate),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_SYMBOL_RATE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SYMBOL_RATE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_SPECTRAL_INVERSION(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SPECTRAL_INVERSION,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(SpectralInversion),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_GUARD_INTERVAL(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_GUARD_INTERVAL,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(GuardInterval),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_TRANSMISSION_MODE(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_TRANSMISSION_MODE,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(TransmissionMode),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_ROLL_OFF(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_ROLL_OFF,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(RollOff),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_PILOT(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_PILOT,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(Pilot),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_SIGNALTIMEOUTS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_SIGNALTIMEOUTS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_SIGNAL_TIMEOUTS),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_PLP_NUMBER(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_PLP_NUMBER,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # BDA Autodemodulate Property Set
        # {DDF15B12-BD25-11d2-9CA0-00C04F7971E0}
        STATIC_KSPROPSETID_BdaAutodemodulate = (
            0xDDF15B12,
            0xBD25,
            0x11D2,
            0x9C,
            0xA0,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSPROPSETID_BdaAutodemodulate = DEFINE_GUIDSTRUCT(
            "DDF15B12-BD25-11d2-9CA0-00C04F7971E0"
        )
        KSPROPSETID_BdaAutodemodulate = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaAutodemodulate)
        )


        class KSPROPERTY_BDA_AUTODEMODULATE(ENUM):
            KSPROPERTY_BDA_AUTODEMODULATE_START = 0
            KSPROPERTY_BDA_AUTODEMODULATE_STOP = 1

        KSPROPERTY_BDA_AUTODEMODULATE_START = KSPROPERTY_BDA_AUTODEMODULATE.KSPROPERTY_BDA_AUTODEMODULATE_START
        KSPROPERTY_BDA_AUTODEMODULATE_STOP = KSPROPERTY_BDA_AUTODEMODULATE.KSPROPERTY_BDA_AUTODEMODULATE_STOP


        def DEFINE_KSPROPERTY_ITEM_BDA_AUTODEMODULATE_START(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_AUTODEMODULATE_START, FALSE, ctypes.sizeof(KSP_NODE), 0, SetHandler, NULL, 0, NULL, NULL, 0)



        def DEFINE_KSPROPERTY_ITEM_BDA_AUTODEMODULATE_STOP(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_AUTODEMODULATE_STOP, FALSE, ctypes.sizeof(KSP_NODE), 0, SetHandler, NULL, 0, NULL, NULL, 0)



        # ------------------------------------------------------------
        # BDA Table Section Property Set
        # {516B99C5-971C-4aaf-B3F3-D9FDA8A15E16}
        STATIC_KSPROPSETID_BdaTableSection = (
            0x516B99C5,
            0x971C,
            0x4AAF,
            0xB3,
            0xF3,
            0xD9,
            0xFD,
            0xA8,
            0xA1,
            0x5E,
            0x16
        )
        KSPROPSETID_BdaTableSection = DEFINE_GUIDSTRUCT(
            "516B99C5-971C-4aaf-B3F3-D9FDA8A15E16"
        )
        KSPROPSETID_BdaTableSection = (
            DEFINE_GUIDNAMED(KSPROPSETID_BdaTableSection)
        )


        class KSPROPERTY_IDS_BDA_TABLE(ENUM):
            KSPROPERTY_BDA_TABLE_SECTION = 0

        KSPROPERTY_BDA_TABLE_SECTION = KSPROPERTY_IDS_BDA_TABLE.KSPROPERTY_BDA_TABLE_SECTION


        def DEFINE_KSPROPERTY_ITEM_BDA_TABLE_SECTION(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_TABLE_SECTION,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_TABLE_SECTION),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # BDA PID Filter Property Set
        # {D0A67D65-08DF-4fec-8533-E5B550410B85}
        STATIC_KSPROPSETID_BdaPIDFilter = (
            0xD0A67D65,
            0x8DF,
            0x4FEC,
            0x85,
            0x33,
            0xE5,
            0xB5,
            0x50,
            0x41,
            0xB,
            0x85
        )
        KSPROPSETID_BdaPIDFilter = DEFINE_GUIDSTRUCT(
            "D0A67D65-08DF-4fec-8533-E5B550410B85"
        )
        KSPROPSETID_BdaPIDFilter = DEFINE_GUIDNAMED(KSPROPSETID_BdaPIDFilter)


        class KSPROPERTY_BDA_PIDFILTER(ENUM):
            KSPROPERTY_BDA_PIDFILTER_MAP_PIDS = 0
            KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS = 1
            KSPROPERTY_BDA_PIDFILTER_LIST_PIDS = 2

        KSPROPERTY_BDA_PIDFILTER_MAP_PIDS = KSPROPERTY_BDA_PIDFILTER.KSPROPERTY_BDA_PIDFILTER_MAP_PIDS
        KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS = KSPROPERTY_BDA_PIDFILTER.KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS
        KSPROPERTY_BDA_PIDFILTER_LIST_PIDS = KSPROPERTY_BDA_PIDFILTER.KSPROPERTY_BDA_PIDFILTER_LIST_PIDS


        def DEFINE_KSPROPERTY_ITEM_BDA_PIDFILTER_MAP_PIDS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_PIDFILTER_MAP_PIDS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_PID_MAP),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_PIDFILTER_UNMAP_PIDS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_PID_UNMAP),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_PIDFILTER_LIST_PIDS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM( KSPROPERTY_BDA_PIDFILTER_LIST_PIDS, GetHandler, ctypes.sizeof(KSP_NODE), 0, SetHandler, NULL, 0, NULL, NULL, 0)



        # ------------------------------------------------------------
        # BDA CA Property Set
        # {B0693766-5278-4ec6-B9E1-3CE40560EF5A}
        STATIC_KSPROPSETID_BdaCA = (
            0xB0693766,
            0x5278,
            0x4EC6,
            0xB9,
            0xE1,
            0x3C,
            0xE4,
            0x5,
            0x60,
            0xEF,
            0x5A
        )
        KSPROPSETID_BdaCA = DEFINE_GUIDSTRUCT(
            "B0693766-5278-4ec6-B9E1-3CE40560EF5A"
        )
        KSPROPSETID_BdaCA = DEFINE_GUIDNAMED(KSPROPSETID_BdaCA)


        class KSPROPERTY_BDA_CA(ENUM):
            KSPROPERTY_BDA_ECM_MAP_STATUS = 0
            KSPROPERTY_BDA_CA_MODULE_STATUS = 1
            KSPROPERTY_BDA_CA_SMART_CARD_STATUS = 2
            KSPROPERTY_BDA_CA_MODULE_UI = 3
            KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS = 4
            KSPROPERTY_BDA_CA_REMOVE_PROGRAM = 5

        KSPROPERTY_BDA_ECM_MAP_STATUS = KSPROPERTY_BDA_CA.KSPROPERTY_BDA_ECM_MAP_STATUS
        KSPROPERTY_BDA_CA_MODULE_STATUS = KSPROPERTY_BDA_CA.KSPROPERTY_BDA_CA_MODULE_STATUS
        KSPROPERTY_BDA_CA_SMART_CARD_STATUS = KSPROPERTY_BDA_CA.KSPROPERTY_BDA_CA_SMART_CARD_STATUS
        KSPROPERTY_BDA_CA_MODULE_UI = KSPROPERTY_BDA_CA.KSPROPERTY_BDA_CA_MODULE_UI
        KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS = KSPROPERTY_BDA_CA.KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS
        KSPROPERTY_BDA_CA_REMOVE_PROGRAM = KSPROPERTY_BDA_CA.KSPROPERTY_BDA_CA_REMOVE_PROGRAM


        def DEFINE_KSPROPERTY_ITEM_BDA_ECM_MAP_STATUS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_ECM_MAP_STATUS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_CA_MODULE_STATUS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_CA_MODULE_STATUS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_CA_SMART_CARD_STATUS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_CA_SMART_CARD_STATUS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_CA_MODULE_UI(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_CA_MODULE_UI,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_CA_MODULE_UI),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_CA_SET_PROGRAM_PIDS(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_PROGRAM_PID_LIST),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        def DEFINE_KSPROPERTY_ITEM_BDA_CA_REMOVE_PROGRAM(GetHandler, SetHandler):
            return DEFINE_KSPROPERTY_ITEM(
                KSPROPERTY_BDA_CA_REMOVE_PROGRAM,
                GetHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(ULONG),
                SetHandler,
                NULL,
                0,
                NULL,
                NULL,
                0
            )


        # ------------------------------------------------------------
        # BDA CA Event Set
        # {488C4CCC-B768-4129-8EB1-B00A071F9068}
        STATIC_KSEVENTSETID_BdaCAEvent = (
            0x488C4CCC,
            0xB768,
            0x4129,
            0x8E,
            0xB1,
            0xB0,
            0xA,
            0x7,
            0x1F,
            0x90,
            0x68
        )
        KSEVENTSETID_BdaCAEvent = DEFINE_GUIDSTRUCT(
            "488C4CCC-B768-4129-8EB1-B00A071F9068"
        )
        KSEVENTSETID_BdaCAEvent = DEFINE_GUIDNAMED(KSEVENTSETID_BdaCAEvent)


        class KSPROPERTY_BDA_CA_EVENT(ENUM):
            KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED = 0
            KSEVENT_BDA_CA_MODULE_STATUS_CHANGED = 1
            KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED = 2
            KSEVENT_BDA_CA_MODULE_UI_REQUESTED = 3

        KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED = KSPROPERTY_BDA_CA_EVENT.KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED
        KSEVENT_BDA_CA_MODULE_STATUS_CHANGED = KSPROPERTY_BDA_CA_EVENT.KSEVENT_BDA_CA_MODULE_STATUS_CHANGED
        KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED = KSPROPERTY_BDA_CA_EVENT.KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED
        KSEVENT_BDA_CA_MODULE_UI_REQUESTED = KSPROPERTY_BDA_CA_EVENT.KSEVENT_BDA_CA_MODULE_UI_REQUESTED


        def DEFINE_KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)



        def DEFINE_KSEVENT_BDA_CA_MODULE_STATUS_CHANGED(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_CA_MODULE_STATUS_CHANGED, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)



        def DEFINE_KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_CA_SMART_CARD_STATUS_CHANGED, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)



        def DEFINE_KSEVENT_BDA_CA_MODULE_UI_REQUESTED(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_CA_MODULE_UI_REQUESTED, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)


        # ------------------------------------------------------------
        # BdaDrmService Method Set
        # {BFF6B5BB-B0AE-484c-9DCA-73528FB0B46E}
        STATIC_KSMETHODSETID_BdaDrmService = (
            0xBFF6B5BB,
            0xB0AE,
            0x484C,
            0x9D,
            0xCA,
            0x73,
            0x52,
            0x8F,
            0xB0,
            0xB4,
            0x6E
        )
        KSMETHODSETID_BdaDrmService = DEFINE_GUIDSTRUCT(
            "BFF6B5BB-B0AE-484c-9DCA-73528FB0B46E"
        )
        KSMETHODSETID_BdaDrmService = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaDrmService)
        )


        class KSMETHOD_BDA_DRM(ENUM):
            KSMETHOD_BDA_DRM_CURRENT = 0
            KSMETHOD_BDA_DRM_DRMSTATUS = 1

        KSMETHOD_BDA_DRM_CURRENT = KSMETHOD_BDA_DRM.KSMETHOD_BDA_DRM_CURRENT
        KSMETHOD_BDA_DRM_DRMSTATUS = KSMETHOD_BDA_DRM.KSMETHOD_BDA_DRM_DRMSTATUS


        def DEFINE_KSMETHOD_BDA_DRM_SETDRM(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_DRM_CURRENT,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_DRM_SETDRM),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_DRM_DRMSTATUS(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_DRM_DRMSTATUS,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_NODE),
                ctypes.sizeof(BDA_DRM_DRMSTATUS),
                SupportHandler,
            )


        # ------------------------------------------------------------
        # PBDA WMDRM SESSION Method Set
        # {4BE6FA3D-07CD-4139-8B80-8C18BA3AEC88}
        STATIC_KSMETHODSETID_BdaWmdrmSession = (
            0x4BE6FA3D,
            0x7CD,
            0x4139,
            0x8B,
            0x80,
            0x8C,
            0x18,
            0xBA,
            0x3A,
            0xEC,
            0x88
        )
        KSMETHODSETID_BdaWmdrmSession = DEFINE_GUIDSTRUCT(
            "4BE6FA3D-07CD-4139-8B80-8C18BA3AEC88"
        )
        KSMETHODSETID_BdaWmdrmSession = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaWmdrmSession)
        )


        class KSMETHOD_BDA_WMDRM(ENUM):
            KSMETHOD_BDA_WMDRM_STATUS = 0
            KSMETHOD_BDA_WMDRM_REVINFO = 1
            KSMETHOD_BDA_WMDRM_CRL = 2
            KSMETHOD_BDA_WMDRM_MESSAGE = 3
            KSMETHOD_BDA_WMDRM_REISSUELICENSE = 4
            KSMETHOD_BDA_WMDRM_RENEWLICENSE = 5
            KSMETHOD_BDA_WMDRM_LICENSE = 6
            KSMETHOD_BDA_WMDRM_KEYINFO = 7

        KSMETHOD_BDA_WMDRM_STATUS = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_STATUS
        KSMETHOD_BDA_WMDRM_REVINFO = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_REVINFO
        KSMETHOD_BDA_WMDRM_CRL = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_CRL
        KSMETHOD_BDA_WMDRM_MESSAGE = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_MESSAGE
        KSMETHOD_BDA_WMDRM_REISSUELICENSE = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_REISSUELICENSE
        KSMETHOD_BDA_WMDRM_RENEWLICENSE = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_RENEWLICENSE
        KSMETHOD_BDA_WMDRM_LICENSE = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_LICENSE
        KSMETHOD_BDA_WMDRM_KEYINFO = KSMETHOD_BDA_WMDRM.KSMETHOD_BDA_WMDRM_KEYINFO


        def DEFINE_KSMETHOD_BDA_WMDRM_STATUS(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_STATUS,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_NODE),
                ctypes.sizeof(BDA_WMDRM_STATUS),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRM_REVINFO(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_REVINFO,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_BUFFER),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRM_CRL(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_CRL,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_BUFFER),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRM_TRANSACTMESSAGE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_MESSAGE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_BUFFER),
                ctypes.sizeof(BDA_BUFFER),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRM_REISSUELICENSE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_REISSUELICENSE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_WMDRM_LICENSE),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRM_RENEWLICENSE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_RENEWLICENSE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_WMDRM_RENEWLICENSE),
                ctypes.sizeof(BDA_WMDRM_RENEWLICENSE),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRM_GETLICENSE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_LICENSE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_WMDRM_LICENSE),
                ctypes.sizeof(BDA_BUFFER),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRM_KEYINFO(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRM_KEYINFO,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_NODE),
                ctypes.sizeof(BDA_WMDRM_KEYINFOLIST),
                SupportHandler,
            )


        # ------------------------------------------------------------
        # PBDA WMDRM Tuner Method Set
        # {86D979CF-A8A7-4f94-B5FB-14C0ACA68FE6}
        STATIC_KSMETHODSETID_BdaWmdrmTuner = (
            0x86D979CF,
            0xA8A7,
            0x4F94,
            0xB5,
            0xFB,
            0x14,
            0xC0,
            0xAC,
            0xA6,
            0x8F,
            0xE6
        )
        KSMETHODSETID_BdaWmdrmTuner = DEFINE_GUIDSTRUCT(
            "86D979CF-A8A7-4f94-B5FB-14C0ACA68FE6"
        )
        KSMETHODSETID_BdaWmdrmTuner = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaWmdrmTuner)
        )


        class KSMETHOD_BDA_WMDRM_TUNER(ENUM):
            KSMETHOD_BDA_WMDRMTUNER_CANCELCAPTURETOKEN = 0
            KSMETHOD_BDA_WMDRMTUNER_SETPIDPROTECTION = 1
            KSMETHOD_BDA_WMDRMTUNER_GETPIDPROTECTION = 2
            KSMETHOD_BDA_WMDRMTUNER_SETSYNCVALUE = 3
            KSMETHOD_BDA_WMDRMTUNER_STARTCODEPROFILE = 4
            KSMETHOD_BDA_WMDRMTUNER_PURCHASE_ENTITLEMENT = 5

        KSMETHOD_BDA_WMDRMTUNER_CANCELCAPTURETOKEN = KSMETHOD_BDA_WMDRM_TUNER.KSMETHOD_BDA_WMDRMTUNER_CANCELCAPTURETOKEN
        KSMETHOD_BDA_WMDRMTUNER_SETPIDPROTECTION = KSMETHOD_BDA_WMDRM_TUNER.KSMETHOD_BDA_WMDRMTUNER_SETPIDPROTECTION
        KSMETHOD_BDA_WMDRMTUNER_GETPIDPROTECTION = KSMETHOD_BDA_WMDRM_TUNER.KSMETHOD_BDA_WMDRMTUNER_GETPIDPROTECTION
        KSMETHOD_BDA_WMDRMTUNER_SETSYNCVALUE = KSMETHOD_BDA_WMDRM_TUNER.KSMETHOD_BDA_WMDRMTUNER_SETSYNCVALUE
        KSMETHOD_BDA_WMDRMTUNER_STARTCODEPROFILE = KSMETHOD_BDA_WMDRM_TUNER.KSMETHOD_BDA_WMDRMTUNER_STARTCODEPROFILE
        KSMETHOD_BDA_WMDRMTUNER_PURCHASE_ENTITLEMENT = KSMETHOD_BDA_WMDRM_TUNER.KSMETHOD_BDA_WMDRMTUNER_PURCHASE_ENTITLEMENT


        def DEFINE_KSMETHOD_BDA_WMDRMTUNER_CANCELCAPTURETOKEN(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRMTUNER_CANCELCAPTURETOKEN,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_BUFFER),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRMTUNER_SETPIDPROTECTION(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRMTUNER_SETPIDPROTECTION,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_WMDRMTUNER_SETPIDPROTECTION),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRMTUNER_GETPIDPROTECTION(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRMTUNER_GETPIDPROTECTION,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_WMDRMTUNER_GETPIDPROTECTION),
                ctypes.sizeof(BDA_WMDRMTUNER_PIDPROTECTION),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRMTUNER_SETSYNCVALUE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRMTUNER_SETSYNCVALUE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_WMDRMTUNER_SYNCVALUE),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRMTUNER_STARTCODEPROFILE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRMTUNER_STARTCODEPROFILE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSP_NODE),
                ctypes.sizeof(BDA_BUFFER),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_BDA_WMDRMTUNER_PURCHASE_ENTITLEMENT(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_WMDRMTUNER_PURCHASE_ENTITLEMENT,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_WMDRMTUNER_PURCHASEENTITLEMENT),
                ctypes.sizeof(BDA_WMDRMTUNER_PURCHASEENTITLEMENT),
                SupportHandler,
            )


        # ------------------------------------------------------------
        # BDA Eventing Service Property Set
        # {B0693766-5278-4ec6-B9E1-3CE40560EF5A}
        STATIC_KSMETHODSETID_BdaEventing = (
            0xF99492DA,
            0x6193,
            0x4EB0,
            0x86,
            0x90,
            0x66,
            0x86,
            0xCB,
            0xFF,
            0x71,
            0x3E
        )
        KSMETHODSETID_BdaEventing = DEFINE_GUIDSTRUCT(
            "f99492da-6193-4eb0-8690-6686cbff713e"
        )
        KSMETHODSETID_BdaEventing = DEFINE_GUIDNAMED(KSMETHODSETID_BdaEventing)


        class KSMETHOD_BDA_EVENTING_SERVICE(ENUM):
            KSMETHOD_BDA_EVENT_DATA = 0
            KSMETHOD_BDA_EVENT_COMPLETE = 1

        KSMETHOD_BDA_EVENT_DATA = KSMETHOD_BDA_EVENTING_SERVICE.KSMETHOD_BDA_EVENT_DATA
        KSMETHOD_BDA_EVENT_COMPLETE = KSMETHOD_BDA_EVENTING_SERVICE.KSMETHOD_BDA_EVENT_COMPLETE


        def DEFINE_KSMETHOD_ITEM_BDA_EVENT_DATA(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_EVENT_DATA,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_EVENT_DATA),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_EVENT_COMPLETE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_EVENT_COMPLETE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_EVENT_COMPLETE),
                ctypes.sizeof(LONG),
                SupportHandler,
            )


        # ------------------------------------------------------------
        # BDA Eventing Service Event
        # ae7e55b2-96d7-4e29-908f-62f95b2a1679
        STATIC_KSEVENTSETID_BdaEvent = (
            0xAE7E55B2,
            0x96D7,
            0x4E29,
            0x90,
            0x8F,
            0x62,
            0xF9,
            0x5B,
            0x2A,
            0x16,
            0x79
        )
        KSEVENTSETID_BdaEvent = DEFINE_GUIDSTRUCT(
            "ae7e55b2-96d7-4e29-908f-62f95b2a1679"
        )
        KSEVENTSETID_BdaEvent = DEFINE_GUIDNAMED(KSEVENTSETID_BdaEvent)


        class KSEVENT_BDA_EVENT_TYPE(ENUM):
            KSEVENT_BDA_EVENT_PENDINGEVENT = 0

        KSEVENT_BDA_EVENT_PENDINGEVENT = KSEVENT_BDA_EVENT_TYPE.KSEVENT_BDA_EVENT_PENDINGEVENT


        def DEFINE_KSEVENT_ITEM_BDA_PENDINGEVENT(AddHandler, RemoveHandler, SupportHandler):
            return DEFINE_KSEVENT_ITEM(KSEVENT_BDA_EVENT_PENDINGEVENT, ctypes.sizeof(KSEVENTDATA), 0, AddHandler, RemoveHandler, SupportHandler)


        # ------------------------------------------------------------
        # BDA Debug Service Property Set
        # {0d4a90ec-c69d-4ee2-8c5a-fb1f63a50da1}
        STATIC_KSMETHODSETID_BdaDebug = (
            0x0D4A90EC,
            0xC69D,
            0x4EE2,
            0x8C,
            0x5A,
            0xFB,
            0x1F,
            0x63,
            0xA5,
            0x0D,
            0xA1
        )
        KSMETHODSETID_BdaDebug = DEFINE_GUIDSTRUCT(
            "0d4a90ec-c69d-4ee2-8c5a-fb1f63a50da1"
        )
        KSMETHODSETID_BdaDebug = DEFINE_GUIDNAMED(KSMETHODSETID_BdaDebug)


        class KSMETHOD_BDA_DEBUG_SERVICE(ENUM):
            KSMETHOD_BDA_DEBUG_LEVEL = 0
            KSMETHOD_BDA_DEBUG_DATA = 1

        KSMETHOD_BDA_DEBUG_LEVEL = KSMETHOD_BDA_DEBUG_SERVICE.KSMETHOD_BDA_DEBUG_LEVEL
        KSMETHOD_BDA_DEBUG_DATA = KSMETHOD_BDA_DEBUG_SERVICE.KSMETHOD_BDA_DEBUG_DATA


        def DEFINE_KSMETHOD_ITEM_BDA_DEBUG_LEVEL(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_DEBUG_LEVEL,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_DEBUG_LEVEL),
                ctypes.sizeof(LONG),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_DEBUG_DATA(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_DEBUG_DATA,
                KSMETHOD_TYPE_MODIFY,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                0,
                SupportHandler,
            )


        # ------------------------------------------------------------
        # BDA Tuner Service Method Set
        # {B774102F-AC07-478a-8228-2742D961FA7E}
        STATIC_KSMETHODSETID_BdaTuner = (
            0xB774102F,
            0xAC07,
            0x478A,
            0x82,
            0x28,
            0x27,
            0x42,
            0xD9,
            0x61,
            0xFA,
            0x7E
        )
        KSMETHODSETID_BdaTuner = DEFINE_GUIDSTRUCT(
            "b774102f-ac07-478a-8228-2742d961fa7e"
        )
        KSMETHODSETID_BdaTuner = DEFINE_GUIDNAMED(KSMETHODSETID_BdaTuner)


        class KSMETHOD_BDA_TUNER_SERVICE(ENUM):
            KSMETHOD_BDA_TUNER_SETTUNER = 0
            KSMETHOD_BDA_TUNER_GETTUNERSTATE = 1
            KSMETHOD_BDA_TUNER_SIGNALNOISERATIO = 2

        KSMETHOD_BDA_TUNER_SETTUNER = KSMETHOD_BDA_TUNER_SERVICE.KSMETHOD_BDA_TUNER_SETTUNER
        KSMETHOD_BDA_TUNER_GETTUNERSTATE = KSMETHOD_BDA_TUNER_SERVICE.KSMETHOD_BDA_TUNER_GETTUNERSTATE
        KSMETHOD_BDA_TUNER_SIGNALNOISERATIO = KSMETHOD_BDA_TUNER_SERVICE.KSMETHOD_BDA_TUNER_SIGNALNOISERATIO


        def DEFINE_KSMETHOD_ITEM_BDA_TUNER_SETTUNER(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_TUNER_SETTUNER,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_TUNER_TUNEREQUEST),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_TUNER_GETTUNERSTATE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_TUNER_GETTUNERSTATE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_TUNER_TUNERSTATE),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_TUNER_SIGNALNOISERATIO(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_TUNER_SIGNALNOISERATIO,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_TUNER_DIAGNOSTICS),
                SupportHandler,
            )


        # ------------------------------------------------------------
        # BDA General Purpose Name Value Service Method Set
        # {0c24096d-5ff5-47de-a856-062e587e3727}//8bit string
        # {36e07304-9f0d-4e88-9118-ac0ba317b7f2}//unicode version
        STATIC_KSMETHODSETID_BdaNameValueA = (
            0xC24096D,
            0x5FF5,
            0x47DE,
            0xA8,
            0x56,
            0x6,
            0x2E,
            0x58,
            0x7E,
            0x37,
            0x27
        )
        KSMETHODSETID_BdaNameValueA = DEFINE_GUIDSTRUCT(
            "0c24096d-5ff5-47de-a856-062e587e3727"
        )
        KSMETHODSETID_BdaNameValueA = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaNameValueA)
        )
        STATIC_KSMETHODSETID_BdaNameValue = (
            0x36E07304,
            0x9F0D,
            0x4E88,
            0x91,
            0x18,
            0xAC,
            0xB,
            0xA3,
            0x17,
            0xB7,
            0xF2
        )
        KSMETHODSETID_BdaNameValue = DEFINE_GUIDSTRUCT(
            "36e07304-9f0d-4e88-9118-ac0ba317b7f2"
        )
        KSMETHODSETID_BdaNameValue = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaNameValue)
        )


        class KSMETHOD_BDA_GPNV_SERVICE(ENUM):
            KSMETHOD_BDA_GPNV_GETVALUE = 0
            KSMETHOD_BDA_GPNV_SETVALUE = 1
            KSMETHOD_BDA_GPNV_NAMEFROMINDEX = 2
            KSMETHOD_BDA_GPNV_GETVALUEUPDATENAME = 3

        KSMETHOD_BDA_GPNV_GETVALUE = KSMETHOD_BDA_GPNV_SERVICE.KSMETHOD_BDA_GPNV_GETVALUE
        KSMETHOD_BDA_GPNV_SETVALUE = KSMETHOD_BDA_GPNV_SERVICE.KSMETHOD_BDA_GPNV_SETVALUE
        KSMETHOD_BDA_GPNV_NAMEFROMINDEX = KSMETHOD_BDA_GPNV_SERVICE.KSMETHOD_BDA_GPNV_NAMEFROMINDEX
        KSMETHOD_BDA_GPNV_GETVALUEUPDATENAME = KSMETHOD_BDA_GPNV_SERVICE.KSMETHOD_BDA_GPNV_GETVALUEUPDATENAME


        def DEFINE_KSMETHOD_ITEM_BDA_GPNV_GETVALUE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GPNV_GETVALUE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_GPNV_GETVALUE),
                ctypes.sizeof(BDA_STRING),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_GPNV_SETVALUE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GPNV_SETVALUE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_GPNV_SETVALUE),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_GPNV_NAMEFROMINDEX(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GPNV_NAMEFROMINDEX,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_GPNV_NAMEINDEX),
                ctypes.sizeof(BDA_STRING),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_GPNV_GETVALUEUPDATENAME(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GPNV_GETVALUEUPDATENAME,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_STRING),
                SupportHandler,
            )


        # ------------------------------------------------------------
        # BDA Mux Service Method Set
        # {942AAFEC-4C05-4c74-B8EB-8706C2A4943F}
        STATIC_KSMETHODSETID_BdaMux = (
            0x942AAFEC,
            0x4C05,
            0x4C74,
            0xB8,
            0xEB,
            0x87,
            0x6,
            0xC2,
            0xA4,
            0x94,
            0x3F
        )
        KSMETHODSETID_BdaMux = DEFINE_GUIDSTRUCT(
            "942AAFEC-4C05-4c74-B8EB-8706C2A4943F"
        )
        KSMETHODSETID_BdaMux = DEFINE_GUIDNAMED(KSMETHODSETID_BdaMux)


        class KSMETHOD_BDA_MUX_SERVICE(ENUM):
            KSMETHOD_BDA_MUX_GETPIDLIST = 0
            KSMETHOD_BDA_MUX_SETPIDLIST = 1

        KSMETHOD_BDA_MUX_GETPIDLIST = KSMETHOD_BDA_MUX_SERVICE.KSMETHOD_BDA_MUX_GETPIDLIST
        KSMETHOD_BDA_MUX_SETPIDLIST = KSMETHOD_BDA_MUX_SERVICE.KSMETHOD_BDA_MUX_SETPIDLIST


        def DEFINE_KSMETHOD_ITEM_BDA_MUX_GETPIDLIST(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_MUX_GETPIDLIST,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_NODE),
                ctypes.sizeof(BDA_BUFFER),
                SupportHandler,
            )


        def DEFINE_KSMETHOD_ITEM_BDA_MUX_SETPIDLIST(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_MUX_SETPIDLIST,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_BUFFER),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        # ------------------------------------------------------------
        # BDA Scanning Service Method Set
        # {12EB49DF-6249-47f3-B190-E21E6E2F8A9C}
        STATIC_KSMETHODSETID_BdaScanning = (
            0x12EB49DF,
            0x6249,
            0x47F3,
            0xB1,
            0x90,
            0xE2,
            0x1E,
            0x6E,
            0x2F,
            0x8A,
            0x9C
        )
        KSMETHODSETID_BdaScanning = DEFINE_GUIDSTRUCT(
            "12EB49DF-6249-47f3-B190-E21E6E2F8A9C"
        )
        KSMETHODSETID_BdaScanning = DEFINE_GUIDNAMED(KSMETHODSETID_BdaScanning)


        class KSMETHOD_BDA_SCAN_SERVICE(ENUM):
            KSMETHOD_BDA_SCAN_CAPABILTIES = 0
            KSMETHOD_BDA_SCANNING_STATE = 1
            KSMETHOD_BDA_SCAN_FILTER = 2
            KSMETHOD_BDA_SCAN_START = 3
            KSMETHOD_BDA_SCAN_RESUME = 4
            KSMETHOD_BDA_SCAN_STOP = 5

        KSMETHOD_BDA_SCAN_CAPABILTIES = KSMETHOD_BDA_SCAN_SERVICE.KSMETHOD_BDA_SCAN_CAPABILTIES
        KSMETHOD_BDA_SCANNING_STATE = KSMETHOD_BDA_SCAN_SERVICE.KSMETHOD_BDA_SCANNING_STATE
        KSMETHOD_BDA_SCAN_FILTER = KSMETHOD_BDA_SCAN_SERVICE.KSMETHOD_BDA_SCAN_FILTER
        KSMETHOD_BDA_SCAN_START = KSMETHOD_BDA_SCAN_SERVICE.KSMETHOD_BDA_SCAN_START
        KSMETHOD_BDA_SCAN_RESUME = KSMETHOD_BDA_SCAN_SERVICE.KSMETHOD_BDA_SCAN_RESUME
        KSMETHOD_BDA_SCAN_STOP = KSMETHOD_BDA_SCAN_SERVICE.KSMETHOD_BDA_SCAN_STOP


        def DEFINE_KSMETHOD_ITEM_BDA_SCAN_CAPABILTIES(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_SCAN_CAPABILTIES,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_SCAN_CAPABILTIES),
                ctypes.sizeof(BDA_SCAN_CAPABILTIES),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_SCANNING_STATE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_SCANNING_STATE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_SCAN_STATE),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_SCAN_FILTER(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_SCAN_FILTER,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_SCAN_FILTER),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_SCAN_START(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_SCAN_START,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_SCAN_START),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_SCAN_RESUME(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_SCAN_RESUME,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_SCAN_STOP(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_SCAN_STOP,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        # ------------------------------------------------------------
        # BDA Guide Data Delivery Service Method Set
        # {8D9D5562-1589-417d-99CE-AC531DDA19F9}
        STATIC_KSMETHODSETID_BdaGuideDataDeliveryService = (
            0x8D9D5562,
            0x1589,
            0x417D,
            0x99,
            0xCE,
            0xAC,
            0x53,
            0x1D,
            0xDA,
            0x19,
            0xF9
        )
        KSMETHODSETID_BdaGuideDataDeliveryService = DEFINE_GUIDSTRUCT(
            "8D9D5562-1589-417d-99CE-AC531DDA19F9"
        )
        KSMETHODSETID_BdaGuideDataDeliveryService = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaGuideDataDeliveryService)
        )


        class KSMETHOD_BDA_GDDS_SERVICE(ENUM):
            KSMETHOD_BDA_GDDS_DATATYPE = 0
            KSMETHOD_BDA_GDDS_DATA = 1
            KSMETHOD_BDA_GDDS_TUNEXMLFROMIDX = 2
            KSMETHOD_BDA_GDDS_GETSERVICES = 3
            KSMETHOD_BDA_GDDS_SERVICEFROMTUNEXML = 4
            KSMETHOD_BDA_GDDS_DATAUPDATE = 5

        KSMETHOD_BDA_GDDS_DATATYPE = KSMETHOD_BDA_GDDS_SERVICE.KSMETHOD_BDA_GDDS_DATATYPE
        KSMETHOD_BDA_GDDS_DATA = KSMETHOD_BDA_GDDS_SERVICE.KSMETHOD_BDA_GDDS_DATA
        KSMETHOD_BDA_GDDS_TUNEXMLFROMIDX = KSMETHOD_BDA_GDDS_SERVICE.KSMETHOD_BDA_GDDS_TUNEXMLFROMIDX
        KSMETHOD_BDA_GDDS_GETSERVICES = KSMETHOD_BDA_GDDS_SERVICE.KSMETHOD_BDA_GDDS_GETSERVICES
        KSMETHOD_BDA_GDDS_SERVICEFROMTUNEXML = KSMETHOD_BDA_GDDS_SERVICE.KSMETHOD_BDA_GDDS_SERVICEFROMTUNEXML
        KSMETHOD_BDA_GDDS_DATAUPDATE = KSMETHOD_BDA_GDDS_SERVICE.KSMETHOD_BDA_GDDS_DATAUPDATE


        def DEFINE_KSMETHOD_ITEM_BDA_GDDS_DATATYPE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GDDS_DATATYPE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_GDDS_DATATYPE),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_GDDS_DATA(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GDDS_DATA,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_GDDS_DATA),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_GDDS_TUNEXMLFROMIDX(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GDDS_TUNEXMLFROMIDX,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_GDDS_TUNEXMLFROMIDX),
                ctypes.sizeof(BDA_STRING),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_GDDS_GETSERVICES(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GDDS_GETSERVICES,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_BUFFER),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_GDDS_SERVICEFROMTUNEXML(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GDDS_SERVICEFROMTUNEXML,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_GDDS_SERVICEFROMTUNEXML),
                ctypes.sizeof(BDA_STRING),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_GDDS_DATAUPDATE(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_GDDS_DATAUPDATE,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        # ------------------------------------------------------------
        # BDA CAS Core Service Method Set
        # {10CED3B4-320B-41bf-9824-1B2E68E71EB9}
        STATIC_KSMETHODSETID_BdaConditionalAccessService = (
            0x10CED3B4,
            0x320B,
            0x41BF,
            0x98,
            0x24,
            0x1B,
            0x2E,
            0x68,
            0xE7,
            0x1E,
            0xB9
        )
        KSMETHODSETID_BdaConditionalAccessService = DEFINE_GUIDSTRUCT(
            "10CED3B4-320B-41bf-9824-1B2E68E71EB9"
        )
        KSMETHODSETID_BdaConditionalAccessService = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaConditionalAccessService)
        )


        class KSMETHOD_BDA_CAS_SERVICE(ENUM):
            KSMETHOD_BDA_CAS_CHECKENTITLEMENTTOKEN = 0
            KSMETHOD_BDA_CAS_SETCAPTURETOKEN = 1
            KSMETHOD_BDA_CAS_OPENBROADCASTMMI = 2
            KSMETHOD_BDA_CAS_CLOSEMMIDIALOG = 3

        KSMETHOD_BDA_CAS_CHECKENTITLEMENTTOKEN = KSMETHOD_BDA_CAS_SERVICE.KSMETHOD_BDA_CAS_CHECKENTITLEMENTTOKEN
        KSMETHOD_BDA_CAS_SETCAPTURETOKEN = KSMETHOD_BDA_CAS_SERVICE.KSMETHOD_BDA_CAS_SETCAPTURETOKEN
        KSMETHOD_BDA_CAS_OPENBROADCASTMMI = KSMETHOD_BDA_CAS_SERVICE.KSMETHOD_BDA_CAS_OPENBROADCASTMMI
        KSMETHOD_BDA_CAS_CLOSEMMIDIALOG = KSMETHOD_BDA_CAS_SERVICE.KSMETHOD_BDA_CAS_CLOSEMMIDIALOG


        def DEFINE_KSMETHOD_ITEM_BDA_CAS_CHECKENTITLEMENTTOKEN(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_CAS_CHECKENTITLEMENTTOKEN,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_CAS_ENTITLEMENTTOKEN),
                ctypes.sizeof(BDA_CAS_CHECK_ENTITLEMENTTOKEN),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_CAS_SETCAPTURETOKEN(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_CAS_SETCAPTURETOKEN,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_CAS_CAPTURETOKEN),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_CAS_OPENBROADCASTMMI(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_CAS_OPENBROADCASTMMI,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_CAS_OPENBROADCASTMMI),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_CAS_CLOSEMMIDIALOG(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_CAS_CLOSEMMIDIALOG,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_CAS_CLOSEMMIDIALOG),
                ctypes.sizeof(BDA_CAS_CLOSE_MMIDIALOG),
                SupportHandler,
            )



        # ------------------------------------------------------------
        # BDA ISDB CAS Service Method Set
        # {5E68C627-16C2-4e6c-B1E2-D00170CDAA0F}
        STATIC_KSMETHODSETID_BdaIsdbConditionalAccess = (
            0x5E68C627,
            0x16C2,
            0x4E6C,
            0xB1,
            0xE2,
            0xD0,
            0x1,
            0x70,
            0xCD,
            0xAA,
            0xF
        )
        KSMETHODSETID_BdaIsdbConditionalAccess = DEFINE_GUIDSTRUCT(
            "5E68C627-16C2-4e6c-B1E2-D00170CDAA0F"
        )
        KSMETHODSETID_BdaIsdbConditionalAccess = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaIsdbConditionalAccess)
        )


        class KSMETHOD_BDA_ISDB_CAS(ENUM):
            KSMETHOD_BDA_ISDBCAS_SETREQUEST = 0
            KSMETHOD_BDA_ISDBCAS_RESPONSEDATA = 1

        KSMETHOD_BDA_ISDBCAS_SETREQUEST = KSMETHOD_BDA_ISDB_CAS.KSMETHOD_BDA_ISDBCAS_SETREQUEST
        KSMETHOD_BDA_ISDBCAS_RESPONSEDATA = KSMETHOD_BDA_ISDB_CAS.KSMETHOD_BDA_ISDBCAS_RESPONSEDATA


        def DEFINE_KSMETHOD_ITEM_BDA_ISDBCAS_SETREQUEST(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_ISDBCAS_SETREQUEST,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_ISDBCAS_REQUEST),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_ISDBCAS_RESPONSEDATA(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_ISDBCAS_RESPONSEDATA,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_NODE),
                ctypes.sizeof(BDA_ISDBCAS_RESPONSEDATA),
                SupportHandler,
            )



        # ------------------------------------------------------------
        # BDA Transprt Stream Selector Service Method Set
        # {1DCFAFE9-B45E-41b3-BB2A-561EB129AE98}
        STATIC_KSMETHODSETID_BdaTSSelector = (
            0x1DCFAFE9,
            0xB45E,
            0x41B3,
            0xBB,
            0x2A,
            0x56,
            0x1E,
            0xB1,
            0x29,
            0xAE,
            0x98
        )
        KSMETHODSETID_BdaTSSelector = DEFINE_GUIDSTRUCT(
            "1DCFAFE9-B45E-41b3-BB2A-561EB129AE98"
        )
        KSMETHODSETID_BdaTSSelector = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaTSSelector)
        )


        class KSMETHOD_BDA_TS_SELECTOR(ENUM):
            KSMETHOD_BDA_TS_SELECTOR_SETTSID = 0
            KSMETHOD_BDA_TS_SELECTOR_GETTSINFORMATION = 1

        KSMETHOD_BDA_TS_SELECTOR_SETTSID = KSMETHOD_BDA_TS_SELECTOR.KSMETHOD_BDA_TS_SELECTOR_SETTSID
        KSMETHOD_BDA_TS_SELECTOR_GETTSINFORMATION = KSMETHOD_BDA_TS_SELECTOR.KSMETHOD_BDA_TS_SELECTOR_GETTSINFORMATION


        def DEFINE_KSMETHOD_ITEM_BDA_TS_SELECTOR_SETTSID(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_TS_SELECTOR_SETTSID,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_TS_SELECTOR_SETTSID),
                ctypes.sizeof(ULONG),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_TS_SELECTOR_GETTSINFORMATION(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_TS_SELECTOR_GETTSINFORMATION,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_NODE),
                ctypes.sizeof(BDA_TS_SELECTORINFO),
                SupportHandler,
            )



        # ------------------------------------------------------------
        # BDA User Activity Service Method Set
        # {EDA5C834-4531-483c-BE0A-94E6C96FF396}
        STATIC_KSMETHODSETID_BdaUserActivity = (
            0xEDA5C834,
            0x4531,
            0x483C,
            0xBE,
            0xA,
            0x94,
            0xE6,
            0xC9,
            0x6F,
            0xF3,
            0x96
        )
        KSMETHODSETID_BdaUserActivity = DEFINE_GUIDSTRUCT(
            "EDA5C834-4531-483c-BE0A-94E6C96FF396"
        )
        KSMETHODSETID_BdaUserActivity = (
            DEFINE_GUIDNAMED(KSMETHODSETID_BdaUserActivity)
        )


        class KSMETHOD_BDA_USERACTIVITY_SERVICE(ENUM):
            KSMETHOD_BDA_USERACTIVITY_USEREASON = 0
            KSMETHOD_BDA_USERACTIVITY_INTERVAL = 1
            KSMETHOD_BDA_USERACTIVITY_DETECTED = 2

        KSMETHOD_BDA_USERACTIVITY_USEREASON = KSMETHOD_BDA_USERACTIVITY_SERVICE.KSMETHOD_BDA_USERACTIVITY_USEREASON
        KSMETHOD_BDA_USERACTIVITY_INTERVAL = KSMETHOD_BDA_USERACTIVITY_SERVICE.KSMETHOD_BDA_USERACTIVITY_INTERVAL
        KSMETHOD_BDA_USERACTIVITY_DETECTED = KSMETHOD_BDA_USERACTIVITY_SERVICE.KSMETHOD_BDA_USERACTIVITY_DETECTED


        def DEFINE_KSMETHOD_ITEM_BDA_USERACTIVITY_USEREASON(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_USERACTIVITY_USEREASON,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSM_BDA_USERACTIVITY_USEREASON),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_USERACTIVITY_INTERVAL(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_USERACTIVITY_INTERVAL,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(BDA_USERACTIVITY_INTERVAL),
                SupportHandler,
            )



        def DEFINE_KSMETHOD_ITEM_BDA_USERACTIVITY_DETECTED(MethodHandler, SupportHandler):
            return DEFINE_KSMETHOD_ITEM(
                KSMETHOD_BDA_USERACTIVITY_DETECTED,
                KSMETHOD_TYPE_MODIFY | KSMETHOD_TYPE_SOURCE,
                MethodHandler,
                ctypes.sizeof(KSMETHOD),
                ctypes.sizeof(PBDARESULT),
                SupportHandler,
            )



        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA Filter Categories
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_KSCATEGORY_BDA_RECEIVER_COMPONENT = (
            0xFD0A5AF4,
            0xB41D,
            0x11D2,
            0x9C,
            0x95,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSCATEGORY_BDA_RECEIVER_COMPONENT = DEFINE_GUIDSTRUCT(
            "FD0A5AF4-B41D-11d2-9C95-00C04F7971E0"
        )
        KSCATEGORY_BDA_RECEIVER_COMPONENT = (
            DEFINE_GUIDNAMED(KSCATEGORY_BDA_RECEIVER_COMPONENT)
        )
        STATIC_KSCATEGORY_BDA_NETWORK_TUNER = (
            0x71985F48,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSCATEGORY_BDA_NETWORK_TUNER = DEFINE_GUIDSTRUCT(
            "71985F48-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSCATEGORY_BDA_NETWORK_TUNER = (
            DEFINE_GUIDNAMED(KSCATEGORY_BDA_NETWORK_TUNER)
        )
        STATIC_KSCATEGORY_BDA_NETWORK_EPG = (
            0x71985F49,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSCATEGORY_BDA_NETWORK_EPG = DEFINE_GUIDSTRUCT(
            "71985F49-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSCATEGORY_BDA_NETWORK_EPG = (
            DEFINE_GUIDNAMED(KSCATEGORY_BDA_NETWORK_EPG)
        )
        STATIC_KSCATEGORY_BDA_IP_SINK = (
            0x71985F4A,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x00,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSCATEGORY_BDA_IP_SINK = DEFINE_GUIDSTRUCT(
            "71985F4A-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSCATEGORY_IP_SINK = DEFINE_GUIDNAMED(KSCATEGORY_BDA_IP_SINK)
        STATIC_KSCATEGORY_BDA_NETWORK_PROVIDER = (
            0x71985F4B,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSCATEGORY_BDA_NETWORK_PROVIDER = DEFINE_GUIDSTRUCT(
            "71985F4B-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSCATEGORY_BDA_NETWORK_PROVIDER = (
            DEFINE_GUIDNAMED(KSCATEGORY_BDA_NETWORK_PROVIDER)
        )
        # {A2E3074F-6C3D-11d3-B653-00C04F79498E}
        STATIC_KSCATEGORY_BDA_TRANSPORT_INFORMATION = (
            0xA2E3074F,
            0x6C3D,
            0x11D3,
            0xB6,
            0x53,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x49,
            0x8E
        )
        KSCATEGORY_BDA_TRANSPORT_INFORMATION = DEFINE_GUIDSTRUCT(
            "A2E3074F-6C3D-11d3-B653-00C04F79498E"
        )
        KSCATEGORY_BDA_TRANSPORT_INFORMATION = (
            DEFINE_GUIDNAMED(KSCATEGORY_BDA_TRANSPORT_INFORMATION)
        )
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA Node Categories
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # Typical usage of the node categories to define supported tuner
        # device standards.
        # Analog (only)
        # KSNODE_BDA_RF_TUNER
        # ATSC (only):
        # KSNODE_BDA_8VSB_DEMODULATOR node
        # DVB-T (only):
        # KSNODE_BDA_COFDM_DEMODULATOR
        # DVB-S (only)
        # KSNODE_BDA_QPSK_DEMODULATOR
        # DVB-S2 (only)
        # KSNODE_BDA_8PSK_DEMODULATOR
        # Digital Cable (both DVB-C and US):
        # KSNODE_BDA_QAM_DEMODULATOR node
        # Hybrid Analog/ATSC:
        # KSNODE_BDA_RF_TUNER & KSNODE_BDA_8VSB_DEMODULATOR nodes
        # Hybrid Analog/Digital Cable:
        # KSNODE_BDA_RF_TUNER & KSNODE_BDA_QAM_DEMODULATOR nodes
        # Hybrid Analog and Digital Cable w/ CableCard:
        # KSNODE_BDA_RF_TUNER & KSNODE_BDA_QAM_DEMODULATOR &
        # KSNODE_BDA_OPENCABLE_POD nodes
        # Hybrid Analog and DVB-T:
        # KSNODE_BDA_RF_TUNER & KSNODE_BDA_COFDM_DEMODULATOR
        # ISDB-S (only)
        # KSNODE_BDA_ISDB_S_DEMODULATOR & KSNODE_BDA_TS_SELECTOR
        STATIC_KSNODE_BDA_RF_TUNER = (
            0x71985F4C,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSNODE_BDA_RF_TUNER = DEFINE_GUIDSTRUCT(
            "71985F4C-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSNODE_BDA_RF_TUNER = DEFINE_GUIDNAMED(KSNODE_BDA_RF_TUNER)
        STATIC_KSNODE_BDA_ANALOG_DEMODULATOR = (
            0x634DB199,
            0x27DD,
            0x46B8,
            0xAC,
            0xFB,
            0xEC,
            0xC9,
            0x8E,
            0x61,
            0xA2,
            0xAD
        )
        KSNODE_BDA_ANALOG_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "634DB199-27DD-46b8-ACFB-ECC98E61A2AD"
        )
        KSNODE_BDA_ANALOG_DEMODULATOR = (
            DEFINE_GUIDNAMED( KSNODE_BDA_ANALOG_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_QAM_DEMODULATOR = (
            0x71985F4D,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSNODE_BDA_QAM_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "71985F4D-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSNODE_BDA_QAM_DEMODULATOR = (
            DEFINE_GUIDNAMED(KSNODE_BDA_QAM_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_QPSK_DEMODULATOR = (
            0x6390C905,
            0x27C1,
            0x4D67,
            0xBD,
            0xB7,
            0x77,
            0xC5,
            0xD,
            0x7,
            0x93,
            0x0
        )
        KSNODE_BDA_QPSK_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "6390C905-27C1-4d67-BDB7-77C50D079300"
        )
        KSNODE_BDA_QPSK_DEMODULATOR = (
            DEFINE_GUIDNAMED(KSNODE_BDA_QPSK_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_8VSB_DEMODULATOR = (
            0x71985F4F,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSNODE_BDA_8VSB_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "71985F4F-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSNODE_BDA_8VSB_DEMODULATOR = (
            DEFINE_GUIDNAMED(KSNODE_BDA_8VSB_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_COFDM_DEMODULATOR = (
            0x2DAC6E05,
            0xEDBE,
            0x4B9C,
            0xB3,
            0x87,
            0x1B,
            0x6F,
            0xAD,
            0x7D,
            0x64,
            0x95
        )
        KSNODE_BDA_COFDM_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "2DAC6E05-EDBE-4b9c-B387-1B6FAD7D6495"
        )
        KSNODE_BDA_COFDM_DEMODULATOR = (
            DEFINE_GUIDNAMED(KSNODE_BDA_COFDM_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_8PSK_DEMODULATOR = (
            0xE957A0E7,
            0xDD98,
            0x4A3C,
            0x81,
            0x0B,
            0x35,
            0x25,
            0x15,
            0x7A,
            0xB6,
            0x2E
        )
        KSNODE_BDA_8PSK_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "E957A0E7-DD98-4A3C-810B-3525157AB62E"
        )
        KSNODE_BDA_8PSK_DEMODULATOR = (
            DEFINE_GUIDNAMED(KSNODE_BDA_8PSK_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_ISDB_T_DEMODULATOR = (
            0xFCEA3AE3,
            0x2CB2,
            0x464D,
            0x8F,
            0x5D,
            0x30,
            0x5C,
            0x0B,
            0xB7,
            0x78,
            0xA2
        )
        KSNODE_BDA_ISDB_T_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "fcea3ae3-2cb2-464d-8f5d-305c0bb778a2"
        )
        KSNODE_BDA_ISDB_T_DEMODULATOR = (
            DEFINE_GUIDNAMED(KSNODE_BDA_ISDB_T_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_ISDB_S_DEMODULATOR = (
            0xEDDE230A,
            0x9086,
            0x432D,
            0xB8,
            0xA5,
            0x66,
            0x70,
            0x26,
            0x38,
            0x07,
            0xE9
        )
        KSNODE_BDA_ISDB_S_DEMODULATOR = DEFINE_GUIDSTRUCT(
            "edde230a-9086-432d-b8a5-6670263807e9"
        )
        KSNODE_BDA_ISDB_S_DEMODULATOR = (
            DEFINE_GUIDNAMED(KSNODE_BDA_ISDB_S_DEMODULATOR)
        )
        STATIC_KSNODE_BDA_OPENCABLE_POD = (
            0x345812A0,
            0xFB7C,
            0x4790,
            0xAA,
            0x7E,
            0xB1,
            0xDB,
            0x88,
            0xAC,
            0x19,
            0xC9
        )
        KSNODE_BDA_OPENCABLE_POD = DEFINE_GUIDSTRUCT(
            "345812A0-FB7C-4790-AA7E-B1DB88AC19C9"
        )
        KSNODE_BDA_OPENCABLE_POD = DEFINE_GUIDNAMED(KSNODE_BDA_OPENCABLE_POD)
        STATIC_KSNODE_BDA_COMMON_CA_POD = (
            0xD83EF8FC,
            0xF3B8,
            0x45AB,
            0x8B,
            0x71,
            0xEC,
            0xF7,
            0xC3,
            0x39,
            0xDE,
            0xB4
        )
        KSNODE_BDA_COMMON_CA_POD = DEFINE_GUIDSTRUCT(
            "D83EF8FC-F3B8-45ab-8B71-ECF7C339DEB4"
        )
        KSNODE_BDA_COMMON_CA_POD = DEFINE_GUIDNAMED(KSNODE_BDA_COMMON_CA_POD)
        STATIC_KSNODE_BDA_PID_FILTER = (
            0xF5412789,
            0xB0A0,
            0x44E1,
            0xAE,
            0x4F,
            0xEE,
            0x99,
            0x9B,
            0x1B,
            0x7F,
            0xBE
        )
        KSNODE_BDA_PID_FILTER = DEFINE_GUIDSTRUCT(
            "F5412789-B0A0-44e1-AE4F-EE999B1B7FBE"
        )
        KSNODE_BDA_PID_FILTER = DEFINE_GUIDNAMED(KSNODE_BDA_PID_FILTER)
        STATIC_KSNODE_BDA_IP_SINK = (
            0x71985F4E,
            0x1CA1,
            0x11D3,
            0x9C,
            0xC8,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE0
        )
        KSNODE_BDA_IP_SINK = DEFINE_GUIDSTRUCT(
            "71985F4E-1CA1-11d3-9CC8-00C04F7971E0"
        )
        KSNODE_IP_SINK = DEFINE_GUIDNAMED(KSNODE_BDA_IP_SINK)
        STATIC_KSNODE_BDA_VIDEO_ENCODER = (
            0xD98429E3,
            0x65C9,
            0x4AC4,
            0x93,
            0xAA,
            0x76,
            0x67,
            0x82,
            0x83,
            0x3B,
            0x7A
        )
        KSNODE_BDA_VIDEO_ENCODER = DEFINE_GUIDSTRUCT(
            "d98429e3-65c9-4ac4-93aa-766782833b7a"
        )
        KSNODE_BDA_VIDEO_ENCODER = DEFINE_GUIDNAMED(KSNODE_BDA_VIDEO_ENCODER)
        STATIC_KSNODE_BDA_PBDA_CAS = (
            0xC026869F,
            0x7129,
            0x4E71,
            0x86,
            0x96,
            0xEC,
            0x8F,
            0x75,
            0x29,
            0x9B,
            0x77
        )
        KSNODE_BDA_PBDA_CAS = DEFINE_GUIDSTRUCT(
            "C026869F-7129-4e71-8696-EC8F75299B77"
        )
        KSNODE_BDA_PBDA_CAS = DEFINE_GUIDNAMED(KSNODE_BDA_PBDA_CAS)
        STATIC_KSNODE_BDA_PBDA_ISDBCAS = (
            0xF2CF2AB3,
            0x5B9D,
            0x40AE,
            0xAB,
            0x7C,
            0x4E,
            0x7A,
            0xD0,
            0xBD,
            0x1C,
            0x52
        )
        KSNODE_BDA_PBDA_ISDBCAS = DEFINE_GUIDSTRUCT(
            "F2CF2AB3-5B9D-40ae-AB7C-4E7AD0BD1C52"
        )
        KSNODE_BDA_PBDA_ISDBCAS = DEFINE_GUIDNAMED(KSNODE_BDA_PBDA_ISDBCAS)
        STATIC_KSNODE_BDA_PBDA_TUNER = (
            0xAA5E8286,
            0x593C,
            0x4979,
            0x94,
            0x94,
            0x46,
            0xA2,
            0xA9,
            0xDF,
            0xE0,
            0x76
        )
        KSNODE_BDA_PBDA_TUNER = DEFINE_GUIDSTRUCT(
            "AA5E8286-593C-4979-9494-46A2A9DFE076"
        )
        KSNODE_BDA_PBDA_TUNER = DEFINE_GUIDNAMED(KSNODE_BDA_PBDA_TUNER)
        STATIC_KSNODE_BDA_PBDA_MUX = (
            0xF88C7787,
            0x6678,
            0x4F4B,
            0xA1,
            0x3E,
            0xDA,
            0x9,
            0x86,
            0x1D,
            0x68,
            0x2B
        )
        KSNODE_BDA_PBDA_MUX = DEFINE_GUIDSTRUCT(
            "F88C7787-6678-4f4b-A13E-DA09861D682B"
        )
        KSNODE_BDA_PBDA_MUX = DEFINE_GUIDNAMED(KSNODE_BDA_PBDA_MUX)
        STATIC_KSNODE_BDA_PBDA_DRM = (
            0x9EEEBD03,
            0xEEA1,
            0x450F,
            0x96,
            0xAE,
            0x63,
            0x3E,
            0x6D,
            0xE6,
            0x3C,
            0xCE
        )
        KSNODE_BDA_PBDA_DRM = DEFINE_GUIDSTRUCT(
            "9EEEBD03-EEA1-450f-96AE-633E6DE63CCE"
        )
        KSNODE_BDA_PBDA_DRM = DEFINE_GUIDNAMED(KSNODE_BDA_PBDA_DRM)
        STATIC_KSNODE_BDA_DRI_DRM = (
            0x4F95AD74,
            0xCEFB,
            0x42D2,
            0x94,
            0xA9,
            0x68,
            0xC5,
            0xB2,
            0xC1,
            0xAA,
            0xBE
        )
        KSNODE_BDA_DRI_DRM = DEFINE_GUIDSTRUCT(
            "4F95AD74-CEFB-42d2-94A9-68C5B2C1AABE"
        )
        KSNODE_BDA_DRI_DRM = DEFINE_GUIDNAMED(KSNODE_BDA_DRI_DRM)
        STATIC_KSNODE_BDA_TS_SELECTOR = (
            0x5EDDF185,
            0xFED1,
            0x4F45,
            0x96,
            0x85,
            0xBB,
            0xB7,
            0x3C,
            0x32,
            0x3C,
            0xFC
        )
        KSNODE_BDA_TS_SELECTOR = DEFINE_GUIDSTRUCT(
            "5EDDF185-FED1-4f45-9685-BBB73C323CFC"
        )
        KSNODE_BDA_TS_SELECTOR = DEFINE_GUIDNAMED(KSNODE_BDA_TS_SELECTOR)
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # IPSink PINNAME GUID
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_PINNAME_IPSINK_INPUT = (
            0x3FDFFA70,
            0xAC9A,
            0x11D2,
            0x8F,
            0x17,
            0x00,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE2
        )
        PINNAME_IPSINK_INPUT = DEFINE_GUIDSTRUCT(
            "3fdffa70-ac9a-11d2-8f17-00c04f7971e2"
        )
        PINNAME_IPSINK_INPUT = DEFINE_GUIDNAMED(PINNAME_IPSINK_INPUT)
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA IPSink Categories/Types
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_KSDATAFORMAT_TYPE_BDA_IP = (
            0xE25F7B8E,
            0xCCCC,
            0x11D2,
            0x8F,
            0x25,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE2
        )
        KSDATAFORMAT_TYPE_BDA_IP = DEFINE_GUIDSTRUCT(
            "e25f7b8e-cccc-11d2-8f25-00c04f7971e2"
        )
        KSDATAFORMAT_TYPE_BDA_IP = DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_BDA_IP)
        STATIC_KSDATAFORMAT_SUBTYPE_BDA_IP = (
            0x5A9A213C,
            0xDB08,
            0x11D2,
            0x8F,
            0x32,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE2
        )
        KSDATAFORMAT_SUBTYPE_BDA_IP = DEFINE_GUIDSTRUCT(
            "5a9a213c-db08-11d2-8f32-00c04f7971e2"
        )
        KSDATAFORMAT_SUBTYPE_BDA_IP = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_BDA_IP)
        )
        STATIC_KSDATAFORMAT_SPECIFIER_BDA_IP = (
            0x6B891420,
            0xDB09,
            0x11D2,
            0x8F,
            0x32,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE2
        )
        KSDATAFORMAT_SPECIFIER_BDA_IP = DEFINE_GUIDSTRUCT(
            "6B891420-DB09-11d2-8F32-00C04F7971E2"
        )
        KSDATAFORMAT_SPECIFIER_BDA_IP = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SPECIFIER_BDA_IP)
        )
        STATIC_KSDATAFORMAT_TYPE_BDA_IP_CONTROL = (
            0xDADD5799,
            0x7D5B,
            0x4B63,
            0x80,
            0xFB,
            0xD1,
            0x44,
            0x2F,
            0x26,
            0xB6,
            0x21
        )
        KSDATAFORMAT_TYPE_BDA_IP_CONTROL = DEFINE_GUIDSTRUCT(
            "DADD5799-7D5B-4b63-80FB-D1442F26B621"
        )
        KSDATAFORMAT_TYPE_BDA_IP_CONTROL = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_BDA_IP_CONTROL)
        )
        STATIC_KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL = (
            0x499856E8,
            0xE85B,
            0x48ED,
            0x9B,
            0xEA,
            0x41,
            0xD,
            0xD,
            0xD4,
            0xEF,
            0x81
        )
        KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL = DEFINE_GUIDSTRUCT(
            "499856E8-E85B-48ed-9BEA-410D0DD4EF81"
        )
        KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL = (
            DEFINE_GUIDNAMED(KSDATAFORMAT_SUBTYPE_BDA_IP_CONTROL)
        )
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # MPE PINNAME GUID
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_PINNAME_MPE = (
            0xC1B06D73,
            0x1DBB,
            0x11D3,
            0x8F,
            0x46,
            0x00,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE2
        )
        PINNAME_MPE = DEFINE_GUIDSTRUCT(
            "C1B06D73-1DBB-11d3-8F46-00C04F7971E2"
        )
        PINNAME_MPE = DEFINE_GUIDNAMED(PINNAME_MPE)
        # ///////////////////////////////////////////////////////////
        # BDA MPE Categories/Types
        STATIC_KSDATAFORMAT_TYPE_MPE = (
            0x455F176C,
            0x4B06,
            0x47CE,
            0x9A,
            0xEF,
            0x8C,
            0xAE,
            0xF7,
            0x3D,
            0xF7,
            0xB5
        )
        KSDATAFORMAT_TYPE_MPE = DEFINE_GUIDSTRUCT(
            "455F176C-4B06-47ce-9AEF-8CAEF73DF7B5"
        )
        KSDATAFORMAT_TYPE_MPE = DEFINE_GUIDNAMED(KSDATAFORMAT_TYPE_MPE)
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # BDA NETWORK TYPE GUID
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_DIGITAL_CABLE_NETWORK_TYPE = (
            0x143827AB,
            0xF77B,
            0x498D,
            0x81,
            0xCA,
            0x5A,
            0x00,
            0x7A,
            0xEC,
            0x28,
            0xBF
        )
        DIGITAL_CABLE_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "143827AB-F77B-498d-81CA-5A007AEC28BF"
        )
        DIGITAL_CABLE_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(DIGITAL_CABLE_NETWORK_TYPE)
        )
        STATIC_ANALOG_TV_NETWORK_TYPE = (
            0xB820D87E,
            0xE0E3,
            0x478F,
            0x8A,
            0x38,
            0x4E,
            0x13,
            0xF7,
            0xB3,
            0xDF,
            0x42
        )
        ANALOG_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "B820D87E-E0E3-478f-8A38-4E13F7B3DF42"
        )
        ANALOG_TV_NETWORK_TYPE = DEFINE_GUIDNAMED(ANALOG_TV_NETWORK_TYPE)
        STATIC_ANALOG_AUXIN_NETWORK_TYPE = (
            0x742EF867,
            0x9E1,
            0x40A3,
            0x82,
            0xD3,
            0x96,
            0x69,
            0xBA,
            0x35,
            0x32,
            0x5F
        )
        ANALOG_AUXIN_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "742EF867-09E1-40A3-82D3-9669BA35325F"
        )
        ANALOG_AUXIN_NETWORK_TYPE = DEFINE_GUIDNAMED(ANALOG_AUXIN_NETWORK_TYPE)
        STATIC_ANALOG_FM_NETWORK_TYPE = (
            0x7728087B,
            0x2BB9,
            0x4E30,
            0x80,
            0x78,
            0x44,
            0x94,
            0x76,
            0xE5,
            0x9D,
            0xBB
        )
        ANALOG_FM_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "7728087B-2BB9-4E30-8078-449476E59DBB"
        )
        ANALOG_FM_NETWORK_TYPE = DEFINE_GUIDNAMED(ANALOG_FM_NETWORK_TYPE)
        STATIC_ISDB_TERRESTRIAL_TV_NETWORK_TYPE = (
            0x95037F6F,
            0x3AC7,
            0x4452,
            0xB6,
            0xC4,
            0x45,
            0xA9,
            0xCE,
            0x92,
            0x92,
            0xA2
        )
        ISDB_TERRESTRIAL_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "95037F6F-3AC7-4452-B6C4-45A9CE9292A2"
        )
        ISDB_TERRESTRIAL_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(ISDB_TERRESTRIAL_TV_NETWORK_TYPE)
        )
        STATIC_ISDB_T_NETWORK_TYPE = (
            0xFC3855A6,
            0xC901,
            0x4F2E,
            0xAB,
            0xA8,
            0x90,
            0x81,
            0x5A,
            0xFC,
            0x6C,
            0x83
        )
        ISDB_T_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "fc3855a6-c901-4f2e-aba8-90815afc6c83"
        )
        ISDB_T_NETWORK_TYPE = DEFINE_GUIDNAMED(ISDB_T_NETWORK_TYPE)
        STATIC_ISDB_SATELLITE_TV_NETWORK_TYPE = (
            0xB0A4E6A0,
            0x6A1A,
            0x4B83,
            0xBB,
            0x5B,
            0x90,
            0x3E,
            0x1D,
            0x90,
            0xE6,
            0xB6
        )
        ISDB_SATELLITE_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "B0A4E6A0-6A1A-4B83-BB5B-903E1D90E6B6"
        )
        ISDB_SATELLITE_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(ISDB_SATELLITE_TV_NETWORK_TYPE)
        )
        STATIC_ISDB_S_NETWORK_TYPE = (
            0xA1E78202,
            0x1459,
            0x41B1,
            0x9C,
            0xA9,
            0x2A,
            0x92,
            0x58,
            0x7A,
            0x42,
            0xCC
        )
        ISDB_S_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "a1e78202-1459-41b1-9ca9-2a92587a42cc"
        )
        ISDB_S_NETWORK_TYPE = DEFINE_GUIDNAMED(ISDB_S_NETWORK_TYPE)
        STATIC_ISDB_CABLE_TV_NETWORK_TYPE = (
            0xC974DDB5,
            0x41FE,
            0x4B25,
            0x97,
            0x41,
            0x92,
            0xF0,
            0x49,
            0xF1,
            0xD5,
            0xD1
        )
        ISDB_CABLE_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "C974DDB5-41FE-4B25-9741-92F049F1D5D1"
        )
        ISDB_CABLE_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(ISDB_CABLE_TV_NETWORK_TYPE)
        )
        STATIC_DIRECT_TV_SATELLITE_TV_NETWORK_TYPE = (
            0x93B66FB5,
            0x93D4,
            0x4323,
            0x92,
            0x1C,
            0xC1,
            0xF5,
            0x2D,
            0xF6,
            0x1D,
            0x3F
        )
        DIRECT_TV_SATELLITE_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "93B66FB5-93D4-4323-921C-C1F52DF61D3F"
        )
        DIRECT_TV_SATELLITE_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(DIRECT_TV_SATELLITE_TV_NETWORK_TYPE)
        )
        STATIC_ECHOSTAR_SATELLITE_TV_NETWORK_TYPE = (
            0xC4F6B31B,
            0xC6BF,
            0x4759,
            0x88,
            0x6F,
            0xA7,
            0x38,
            0x6D,
            0xCA,
            0x27,
            0xA0
        )
        ECHOSTAR_SATELLITE_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "C4F6B31B-C6BF-4759-886F-A7386DCA27A0"
        )
        ECHOSTAR_SATELLITE_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(ECHOSTAR_SATELLITE_TV_NETWORK_TYPE)
        )
        # Same as CLSID_ATSCNetworkProvider in uuids.h
        STATIC_ATSC_TERRESTRIAL_TV_NETWORK_TYPE = (
            0x0DAD2FDD,
            0x5FD7,
            0x11D3,
            0x8F,
            0x50,
            0x00,
            0xC0,
            0x4F,
            0x79,
            0x71,
            0xE2
        )
        ATSC_TERRESTRIAL_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "0DAD2FDD-5FD7-11D3-8F50-00C04F7971E2"
        )
        ATSC_TERRESTRIAL_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(ATSC_TERRESTRIAL_TV_NETWORK_TYPE)
        )
        # Same as CLSID_DVBTNetworkProvider in uuids.h
        STATIC_DVB_TERRESTRIAL_TV_NETWORK_TYPE = (
            0x216C62DF,
            0x6D7F,
            0x4E9A,
            0x85,
            0x71,
            0x05,
            0xF1,
            0x4E,
            0xDB,
            0x76,
            0x6A
        )
        DVB_TERRESTRIAL_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "216C62DF-6D7F-4E9A-8571-05F14EDB766A"
        )
        DVB_TERRESTRIAL_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(DVB_TERRESTRIAL_TV_NETWORK_TYPE)
        )
        # Same as CLSID_DVBSNetworkProvider in uuids.h
        STATIC_BSKYB_TERRESTRIAL_TV_NETWORK_TYPE = (
            0x9E9E46C6,
            0x3ABA,
            0x4F08,
            0xAD,
            0x0E,
            0xCC,
            0x5A,
            0xC8,
            0x14,
            0x8C,
            0x2B
        )
        BSKYB_TERRESTRIAL_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "9E9E46C6-3ABA-4f08-AD0E-CC5AC8148C2B"
        )
        BSKYB_TERRESTRIAL_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(BSKYB_TERRESTRIAL_TV_NETWORK_TYPE)
        )
        # Same as CLSID_DVBSNetworkProvider in uuids.h
        STATIC_DVB_SATELLITE_TV_NETWORK_TYPE = (
            0xFA4B375A,
            0x45B4,
            0x4D45,
            0x84,
            0x40,
            0x26,
            0x39,
            0x57,
            0xB1,
            0x16,
            0x23
        )
        DVB_SATELLITE_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "FA4B375A-45B4-4D45-8440-263957B11623"
        )
        DVB_SATELLITE_TV_NETWORK_TYPE = (
            DEFINE_GUIDNAMED(DVB_SATELLITE_TV_NETWORK_TYPE)
        )
        # Same as CLSID_DVBCNetworkProvider in uuids.h
        STATIC_DVB_CABLE_TV_NETWORK_TYPE = (
            0xDC0C0FE7,
            0x485,
            0x4266,
            0xB9,
            0x3F,
            0x68,
            0xFB,
            0xF8,
            0x0E,
            0xD8,
            0x34
        )
        DVB_CABLE_TV_NETWORK_TYPE = DEFINE_GUIDSTRUCT(
            "DC0C0FE7-0485-4266-B93F-68FBF80ED834"
        )
        DVB_CABLE_TV_NETWORK_TYPE = DEFINE_GUIDNAMED(DVB_CABLE_TV_NETWORK_TYPE)
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # PBDA EVENT GUIDS
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_BDA_DEBUG_DATA_AVAILABLE = (
            0x69C24F54,
            0x9983,
            0x497E,
            0xB4,
            0x15,
            0x28,
            0x2B,
            0xE4,
            0xC5,
            0x55,
            0xFB
        )
        BDA_DEBUG_DATA_AVAILABLE = DEFINE_GUIDSTRUCT(
            "69C24F54-9983-497e-B415-282BE4C555FB"
        )
        BDA_DEBUG_DATA_AVAILABLE = DEFINE_GUIDNAMED(BDA_DEBUG_DATA_AVAILABLE)
        STATIC_BDA_DEBUG_DATA_TYPE_STRING = (
            0xA806E767,
            0xDE5C,
            0x430C,
            0x80,
            0xBF,
            0xA2,
            0x1E,
            0xBE,
            0x06,
            0xC7,
            0x48
        )
        BDA_DEBUG_DATA_TYPE_STRING = DEFINE_GUIDSTRUCT(
            "a806e767-de5c-430c-80bf-a21ebe06c748"
        )
        BDA_DEBUG_DATA_TYPE_STRING = (
            DEFINE_GUIDNAMED(BDA_DEBUG_DATA_TYPE_STRING)
        )
        STATIC_EVENTID_BDA_IsdbCASResponse = (
            0xD4CB1966,
            0x41BC,
            0x4CED,
            0x9A,
            0x20,
            0xFD,
            0xCE,
            0xAC,
            0x78,
            0xF7,
            0x0D
        )
        EVENTID_BDA_IsdbCASResponse = DEFINE_GUIDSTRUCT(
            "D4CB1966-41BC-4ced-9A20-FDCEAC78F70D"
        )
        EVENTID_BDA_IsdbCASResponse = (
            DEFINE_GUIDNAMED(EVENTID_BDA_IsdbCASResponse)
        )
        STATIC_EVENTID_BDA_CASRequestTuner = (
            0xCF39A9D8,
            0xF5D3,
            0x4685,
            0xBE,
            0x57,
            0xED,
            0x81,
            0xDB,
            0xA4,
            0x6B,
            0x27
        )
        EVENTID_BDA_CASRequestTuner = DEFINE_GUIDSTRUCT(
            "CF39A9D8-F5D3-4685-BE57-ED81DBA46B27"
        )
        EVENTID_BDA_CASRequestTuner = (
            DEFINE_GUIDNAMED(EVENTID_BDA_CASRequestTuner)
        )
        STATIC_EVENTID_BDA_CASReleaseTuner = (
            0x20C1A16B,
            0x441F,
            0x49A5,
            0xBB,
            0x5C,
            0xE9,
            0xA0,
            0x44,
            0x95,
            0xC6,
            0xC1
        )
        EVENTID_BDA_CASReleaseTuner = DEFINE_GUIDSTRUCT(
            "20C1A16B-441F-49a5-BB5C-E9A04495C6C1"
        )
        EVENTID_BDA_CASReleaseTuner = (
            DEFINE_GUIDNAMED(EVENTID_BDA_CASReleaseTuner)
        )
        STATIC_EVENTID_BDA_CASOpenMMI = (
            0x85DAC915,
            0xE593,
            0x410D,
            0x84,
            0x71,
            0xD6,
            0x81,
            0x21,
            0x05,
            0xF2,
            0x8E
        )
        EVENTID_BDA_CASOpenMMI = DEFINE_GUIDSTRUCT(
            "85DAC915-E593-410d-8471-D6812105F28E"
        )
        EVENTID_BDA_CASOpenMMI = DEFINE_GUIDNAMED(EVENTID_BDA_CASOpenMMI)
        STATIC_EVENTID_BDA_CASCloseMMI = (
            0x5D0F550F,
            0xDE2E,
            0x479D,
            0x83,
            0x45,
            0xEC,
            0x0E,
            0x95,
            0x57,
            0xE8,
            0xA2
        )
        EVENTID_BDA_CASCloseMMI = DEFINE_GUIDSTRUCT(
            "5D0F550F-DE2E-479d-8345-EC0E9557E8A2"
        )
        EVENTID_BDA_CASCloseMMI = DEFINE_GUIDNAMED(EVENTID_BDA_CASCloseMMI)
        STATIC_EVENTID_BDA_CASBroadcastMMI = (
            0x676876F0,
            0x1132,
            0x404C,
            0xA7,
            0xCA,
            0xE7,
            0x20,
            0x69,
            0xA9,
            0xD5,
            0x4F
        )
        EVENTID_BDA_CASBroadcastMMI = DEFINE_GUIDSTRUCT(
            "676876F0-1132-404c-A7CA-E72069A9D54F"
        )
        EVENTID_BDA_CASBroadcastMMI = (
            DEFINE_GUIDNAMED(EVENTID_BDA_CASBroadcastMMI)
        )
        STATIC_EVENTID_BDA_TunerSignalLock = (
            0x1872E740,
            0xF573,
            0x429B,
            0xA0,
            0x0E,
            0xD9,
            0xC1,
            0xE4,
            0x08,
            0xAF,
            0x09
        )
        EVENTID_BDA_TunerSignalLock = DEFINE_GUIDSTRUCT(
            "1872E740-F573-429b-A00E-D9C1E408AF09"
        )
        EVENTID_BDA_TunerSignalLock = (
            DEFINE_GUIDNAMED(EVENTID_BDA_TunerSignalLock)
        )
        STATIC_EVENTID_BDA_TunerNoSignal = (
            0xE29B382B,
            0x1EDD,
            0x4930,
            0xBC,
            0x46,
            0x68,
            0x2F,
            0xD7,
            0x2D,
            0x2D,
            0xFB
        )
        EVENTID_BDA_TunerNoSignal = DEFINE_GUIDSTRUCT(
            "E29B382B-1EDD-4930-BC46-682FD72D2DFB"
        )
        EVENTID_BDA_TunerNoSignal = DEFINE_GUIDNAMED(EVENTID_BDA_TunerNoSignal)
        STATIC_EVENTID_BDA_GPNVValueUpdate = (
            0xFF75C68C,
            0xF416,
            0x4E7E,
            0xBF,
            0x17,
            0x6D,
            0x55,
            0xC5,
            0xDF,
            0x15,
            0x75
        )
        EVENTID_BDA_GPNVValueUpdate = DEFINE_GUIDSTRUCT(
            "FF75C68C-F416-4e7e-BF17-6D55C5DF1575"
        )
        EVENTID_BDA_GPNVValueUpdate = (
            DEFINE_GUIDNAMED(EVENTID_BDA_GPNVValueUpdate)
        )
        STATIC_EVENTID_BDA_UpdateDrmStatus = (
            0x65A6F681,
            0x1462,
            0x473B,
            0x88,
            0xCE,
            0xCB,
            0x73,
            0x14,
            0x27,
            0xBD,
            0xB5
        )
        EVENTID_BDA_UpdateDrmStatus = DEFINE_GUIDSTRUCT(
            "65A6F681-1462-473b-88CE-CB731427BDB5"
        )
        EVENTID_BDA_UpdateDrmStatus = (
            DEFINE_GUIDNAMED(EVENTID_BDA_UpdateDrmStatus)
        )
        STATIC_EVENTID_BDA_UpdateScanState = (
            0x55702B50,
            0x7B49,
            0x42B8,
            0xA8,
            0x2F,
            0x4A,
            0xFB,
            0x69,
            0x1B,
            0x06,
            0x28
        )
        EVENTID_BDA_UpdateScanState = DEFINE_GUIDSTRUCT(
            "55702B50-7B49-42B8-A82F-4AFB691B0628"
        )
        EVENTID_BDA_UpdateScanState = (
            DEFINE_GUIDNAMED(EVENTID_BDA_UpdateScanState)
        )
        STATIC_EVENTID_BDA_GuideDataAvailable = (
            0x98DB717A,
            0x478A,
            0x4CD4,
            0x92,
            0xD0,
            0x95,
            0xF6,
            0x6B,
            0x89,
            0xE5,
            0xB1
        )
        EVENTID_BDA_GuideDataAvailable = DEFINE_GUIDSTRUCT(
            "98DB717A-478A-4cd4-92D0-95F66B89E5B1"
        )
        EVENTID_BDA_GuideDataAvailable = (
            DEFINE_GUIDNAMED(EVENTID_BDA_GuideDataAvailable)
        )
        STATIC_EVENTID_BDA_GuideServiceInformationUpdated = (
            0xA1C3EA2B,
            0x175F,
            0x4458,
            0xB7,
            0x35,
            0x50,
            0x7D,
            0x22,
            0xDB,
            0x23,
            0xA6
        )
        EVENTID_BDA_GuideServiceInformationUpdated = DEFINE_GUIDSTRUCT(
            "A1C3EA2B-175F-4458-B735-507D22DB23A6"
        )
        EVENTID_BDA_GuideServiceInformationUpdated = (
            DEFINE_GUIDNAMED(EVENTID_BDA_GuideServiceInformationUpdated)
        )
        STATIC_EVENTID_BDA_GuideDataError = (
            0xAC33C448,
            0x6F73,
            0x4FD7,
            0xB3,
            0x41,
            0x59,
            0x4C,
            0x36,
            0x0D,
            0x8D,
            0x74
        )
        EVENTID_BDA_GuideDataError = DEFINE_GUIDSTRUCT(
            "AC33C448-6F73-4fd7-B341-594C360D8D74"
        )
        EVENTID_BDA_GuideDataError = (
            DEFINE_GUIDNAMED(EVENTID_BDA_GuideDataError)
        )
        STATIC_EVENTID_BDA_DiseqCResponseAvailable = (
            0xEFA628F8,
            0x1F2C,
            0x4B67,
            0x9E,
            0xA5,
            0xAC,
            0xF6,
            0xFA,
            0x9A,
            0x1F,
            0x36
        )
        EVENTID_BDA_DiseqCResponseAvailable = DEFINE_GUIDSTRUCT(
            "EFA628F8-1F2C-4b67-9EA5-ACF6FA9A1F36"
        )
        EVENTID_BDA_DiseqCResponseAvailable = (
            DEFINE_GUIDNAMED(EVENTID_BDA_DiseqCResponseAvailable)
        )
        STATIC_EVENTID_BDA_LbigsOpenConnection = (
            0x356207B2,
            0x6F31,
            0x4EB0,
            0xA2,
            0x71,
            0xB3,
            0xFA,
            0x6B,
            0xB7,
            0x68,
            0x0F
        )
        EVENTID_BDA_LbigsOpenConnection = DEFINE_GUIDSTRUCT(
            "356207B2-6F31-4eb0-A271-B3FA6BB7680F"
        )
        EVENTID_BDA_LbigsOpenConnection = (
            DEFINE_GUIDNAMED(EVENTID_BDA_LbigsOpenConnection)
        )
        STATIC_EVENTID_BDA_LbigsSendData = (
            0x1123277B,
            0xF1C6,
            0x4154,
            0x8B,
            0x0D,
            0x48,
            0xE6,
            0x15,
            0x70,
            0x59,
            0xAA
        )
        EVENTID_BDA_LbigsSendData = DEFINE_GUIDSTRUCT(
            "1123277B-F1C6-4154-8B0D-48E6157059AA"
        )
        EVENTID_BDA_LbigsSendData = DEFINE_GUIDNAMED(EVENTID_BDA_LbigsSendData)
        STATIC_EVENTID_BDA_LbigsCloseConnectionHandle = (
            0xC2F08B99,
            0x65EF,
            0x4314,
            0x96,
            0x71,
            0xE9,
            0x9D,
            0x4C,
            0xCE,
            0x0B,
            0xAE
        )
        EVENTID_BDA_LbigsCloseConnectionHandle = DEFINE_GUIDSTRUCT(
            "C2F08B99-65EF-4314-9671-E99D4CCE0BAE"
        )
        EVENTID_BDA_LbigsCloseConnectionHandle = (
            DEFINE_GUIDNAMED(EVENTID_BDA_LbigsCloseConnectionHandle)
        )
        STATIC_EVENTID_BDA_EncoderSignalLock = (
            0x5EC90EB9,
            0x39FA,
            0x4CFC,
            0xB9,
            0x3F,
            0x00,
            0xBB,
            0x11,
            0x07,
            0x7F,
            0x5E
        )
        EVENTID_BDA_EncoderSignalLock = DEFINE_GUIDSTRUCT(
            "5EC90EB9-39FA-4CFC-B93F-00BB11077F5E"
        )
        EVENTID_BDA_EncoderSignalLock = (
            DEFINE_GUIDNAMED(EVENTID_BDA_EncoderSignalLock)
        )
        STATIC_EVENTID_BDA_FdcStatus = (
            0x05F25366,
            0xD0EB,
            0x43D2,
            0xBC,
            0x3C,
            0x68,
            0x2B,
            0x86,
            0x3D,
            0xF1,
            0x42
        )
        EVENTID_BDA_FdcStatus = DEFINE_GUIDSTRUCT(
            "05F25366-D0EB-43d2-BC3C-682B863DF142"
        )
        EVENTID_BDA_FdcStatus = DEFINE_GUIDNAMED(EVENTID_BDA_FdcStatus)
        STATIC_EVENTID_BDA_FdcTableSection = (
            0x6A0CD757,
            0x4CE3,
            0x4E5B,
            0x94,
            0x44,
            0x71,
            0x87,
            0xB8,
            0x71,
            0x52,
            0xC5
        )
        EVENTID_BDA_FdcTableSection = DEFINE_GUIDSTRUCT(
            "6A0CD757-4CE3-4e5b-9444-7187B87152C5"
        )
        EVENTID_BDA_FdcTableSection = (
            DEFINE_GUIDNAMED(EVENTID_BDA_FdcTableSection)
        )
        STATIC_EVENTID_BDA_TransprtStreamSelectorInfo = (
            0xC40F9F85,
            0x9D0,
            0x489C,
            0x9E,
            0x9C,
            0x0A,
            0xBB,
            0xB5,
            0x69,
            0x51,
            0xB0
        )
        EVENTID_BDA_TransprtStreamSelectorInfo = DEFINE_GUIDSTRUCT(
            "C40F9F85-09D0-489c-9E9C-0ABBB56951B0"
        )
        EVENTID_BDA_TransprtStreamSelectorInfo = (
            DEFINE_GUIDNAMED(EVENTID_BDA_TransprtStreamSelectorInfo)
        )
        STATIC_EVENTID_BDA_RatingPinReset = (
            0xC6E048C0,
            0xC574,
            0x4C26,
            0xBC,
            0xDA,
            0x2F,
            0x4D,
            0x35,
            0xEB,
            0x5E,
            0x85
        )
        EVENTID_BDA_RatingPinReset = DEFINE_GUIDSTRUCT(
            "C6E048C0-C574-4C26-BCDA-2F4D35EB5E85"
        )
        EVENTID_BDA_RatingPinReset = (
            DEFINE_GUIDNAMED(EVENTID_BDA_RatingPinReset)
        )
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        # PBDA COMMON USE GUIDs
        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =
        STATIC_PBDA_ALWAYS_TUNE_IN_MUX = (
            0x1E1D7141,
            0x583F,
            0x4AC2,
            0xB0,
            0x19,
            0x1F,
            0x43,
            0x0E,
            0xDA,
            0x0F,
            0x4C
        )
        PBDA_ALWAYS_TUNE_IN_MUX = DEFINE_GUIDSTRUCT(
            "1E1D7141-583F-4ac2-B019-1F430EDA0F4C"
        )
        PBDA_ALWAYS_TUNE_IN_MUX = DEFINE_GUIDNAMED(PBDA_ALWAYS_TUNE_IN_MUX)
        if defined(__cplusplus):
            pass
        # END IF   defined(__cplusplus)
    # END IF   not defined(_BDAMEDIA_)
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)


