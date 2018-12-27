from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *


__SMTPGUID_H__ = None
SMTPINITGUID = None


# + ------------------------------------------------------------
# Copyright (C) 1998, Microsoft Corporation
# File: smtpguid.h
# Contents: Event related GUIDS published from SMTPSVC
# Instructions: Include this file to declare the various
# GUIDS/strings as external global variables.
# To actually define these global variables,
# define SMTPINITGUID and include <initguid.h> before this
# header file.
# History:
# Jeffrey C Stamerjohn 1998/07/14 15:22:29: Created.
# -------------------------------------------------------------
if not defined(__SMTPGUID_H__):
    __SMTPGUID_H__ = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(SMTPINITGUID):
            def DECLARE_EVENTGUID_STRING(Value):
                return WCHAR(Value)
        else:
            def DECLARE_EVENTGUID_STRING(Value):
                return WCHAR(Value)
        # END IF  SMTPINITGUID

        # SMTP SourceType GUID
        # {fb65c4dc-e468-11d1-aa67-00c04fa345f6}
        GUID_SMTP_SOURCE_TYPE = DEFINE_GUID(
            0xFB65C4DC,
            0xE468,
            0x11D1,
            0xAA,
            0x67,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x45,
            0xF6
        )

        # /* * SMTP Source GUID
        # {1b3c0666-e470-11d1-aa67-00c04fa345f6}
        GUID_SMTPSVC_SOURCE = DEFINE_GUID(
            0x1B3C0666,
            0xE470,
            0x11D1,
            0xAA,
            0x67,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x45,
            0xF6
        )

        # /* * Protocol Events
        # SMTP OnInboundCommand
        # {F6628C8D-0D5E-11d2-AA68-00C04FA35B82}
        CATID_SMTP_ON_INBOUND_COMMAND = DEFINE_GUID(
            0xF6628C8D,
            0xD5E,
            0x11D2,
            0xAA,
            0x68,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x5B,
            0x82
        )

        # SMTP OnServerResponse
        # {F6628C8E-0D5E-11d2-AA68-00C04FA35B82}
        CATID_SMTP_ON_SERVER_RESPONSE = DEFINE_GUID(
            0xF6628C8E,
            0xD5E,
            0x11D2,
            0xAA,
            0x68,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x5B,
            0x82
        )

        # SMTP OnSessionStart
        # {F6628C8F-0D5E-11d2-AA68-00C04FA35B82}
        CATID_SMTP_ON_SESSION_START = DEFINE_GUID(
            0xF6628C8F,
            0xD5E,
            0x11D2,
            0xAA,
            0x68,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x5B,
            0x82
        )

        # SMTP OnMessageStart
        # {F6628C90-0D5E-11d2-AA68-00C04FA35B82}
        CATID_SMTP_ON_MESSAGE_START = DEFINE_GUID(
            0xF6628C90,
            0xD5E,
            0x11D2,
            0xAA,
            0x68,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x5B,
            0x82
        )

        # SMTP OnPerRecipient
        # {F6628C91-0D5E-11d2-AA68-00C04FA35B82}
        CATID_SMTP_ON_PER_RECIPIENT = DEFINE_GUID(
            0xF6628C91,
            0xD5E,
            0x11D2,
            0xAA,
            0x68,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x5B,
            0x82
        )

        # Smtp OnBeforeData
        # {F6628C92-0D5E-11d2-AA68-00C04FA35B82}
        CATID_SMTP_ON_BEFORE_DATA = DEFINE_GUID(
            0xF6628C92,
            0xD5E,
            0x11D2,
            0xAA,
            0x68,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x5B,
            0x82
        )

        # SMTP OnSessionEnd
        # {F6628C93-0D5E-11d2-AA68-00C04FA35B82}
        CATID_SMTP_ON_SESSION_END = DEFINE_GUID(
            0xF6628C93,
            0xD5E,
            0x11D2,
            0xAA,
            0x68,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x5B,
            0x82
        )

        # /* * Transport Events
        # SMTP Store Events
        # {59175850-e533-11d1-aa67-00c04fa345f6}
        CATID_SMTP_STORE_DRIVER = DEFINE_GUID(
            0x59175850,
            0xE533,
            0x11D1,
            0xAA,
            0x67,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x45,
            0xF6
        )

        # SMTP OnTransportSubmission
        # {FF3CAA23-00B9-11d2-9DFB-00C04FA322BA}
        CATID_SMTP_TRANSPORT_SUBMISSION = DEFINE_GUID(
            0xFF3CAA23,
            0xB9,
            0x11D2,
            0x9D,
            0xFB,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x22,
            0xBA
        )

        # SMTP onPrecategorize
        # {A3ACFB0D-83FF-11d2-9E14-00C04FA322BA}
        CATID_SMTP_TRANSPORT_PRECATEGORIZE = DEFINE_GUID(
            0xA3ACFB0D,
            0x83FF,
            0x11D2,
            0x9E,
            0x14,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x22,
            0xBA
        )

        # SMTP Categorizer events
        # {960252A3-0A3A-11d2-9E00-00C04FA322BA}
        CATID_SMTP_TRANSPORT_CATEGORIZE = DEFINE_GUID(
            0x960252A3,
            0xA3A,
            0x11D2,
            0x9E,
            0x0,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x22,
            0xBA
        )

        # SMTP onPostcategorize
        # {76719654-05A6-11d2-9DFD-00C04FA322BA}
        CATID_SMTP_TRANSPORT_POSTCATEGORIZE = DEFINE_GUID(
            0x76719654,
            0x5A6,
            0x11D2,
            0x9D,
            0xFD,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x22,
            0xBA
        )

        # SMTP OnTransportRouter
        # {283430C9-1850-11d2-9E03-00C04FA322BA}
        CATID_SMTP_TRANSPORT_ROUTER = DEFINE_GUID(
            0x283430C9,
            0x1850,
            0x11D2,
            0x9E,
            0x3,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x22,
            0xBA
        )

        # SMTP MsgTrackLog
        # {c6df52aa-7db0-11d2-94f4-00c04f79f1d6}
        CATID_SMTP_MSGTRACKLOG = DEFINE_GUID(
            0xC6DF52AA,
            0x7DB0,
            0x11D2,
            0x94,
            0xF4,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0xF1,
            0xD6
        )

        # SMTP DnsResolver
        # {bd0b4366-8e03-11d2-94f6-00c04f79f1d6}
        CATID_SMTP_DNSRESOLVERRECORDSINK = DEFINE_GUID(
            0xBD0B4366,
            0x8E03,
            0x11D2,
            0x94,
            0xF6,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0xF1,
            0xD6
        )

        # SMTP MaxMsgSize
        # {ebf159de-a67e-11d2-94f7-00c04f79f1d6}
        CATID_SMTP_MAXMSGSIZE = DEFINE_GUID(
            0xEBF159DE,
            0xA67E,
            0x11D2,
            0x94,
            0xF7,
            0x0,
            0xC0,
            0x4F,
            0x79,
            0xF1,
            0xD6
        )

        # SMTP Log
        # {93d0a538-2c1e-4b68-a7c9-d73a8aa6ee97}
        CATID_SMTP_LOG = DEFINE_GUID(
            0x93D0A538,
            0x2C1E,
            0x4B68,
            0xA7,
            0xC9,
            0xD7,
            0x3A,
            0x8A,
            0xA6,
            0xEE,
            0x97
        )

        # SMTP GET_AUX_DOMAIN_INFO_FLAGS
        # {84ff368a-fab3-43d7-bcdf-692c5b46e6b1}
        CATID_SMTP_GET_AUX_DOMAIN_INFO_FLAGS = DEFINE_GUID(
            0x84FF368A,
            0xFAB3,
            0x43D7,
            0xBC,
            0xDF,
            0x69,
            0x2C,
            0x5B,
            0x46,
            0xE6,
            0xB1
        )


        # CLSID of the CoCreateable categorizer
        # {B23C35B7-9219-11d2-9E17-00C04FA322BA}"
        CLSID_SmtpCat = DEFINE_GUID(
            0xB23C35B7,
            0x9219,
            0x11D2,
            0x9E,
            0x17,
            0x0,
            0xC0,
            0x4F,
            0xA3,
            0x22,
            0xBA
        )


        # SMTP DSN
        # {22B55731-F5F8-4d23-BD8F-87B52371A73A}
        CATID_SMTP_DSN = DEFINE_GUID(
            0x22B55731,
            0xF5F8,
            0x4D23,
            0xBD,
            0x8F,
            0x87,
            0xB5,
            0x23,
            0x71,
            0xA7,
            0x3A
        )
        SZ_PROGID_SMTPCAT = "Smtp.Cat"
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  __SMTPGUID_H__


