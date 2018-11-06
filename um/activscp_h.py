

from wtypes_h import (
    ENUM,
    HRESULT,
    GUID,
    DWORD,
    LONG,
    DWORD64,
    LPCOLESTR,
    POINTER,
    ULONG,
    BSTR,
    DWORDLONG,
    LPOLESTR,
    REFGUID,
    REFIID,
    VOID,
    HWND,
    BOOL,
    LCID,
)
from guiddef_h import (
    DEFINE_GUID,
    IID,
)

import comtypes


__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
IID_IActiveScriptSite = IID(
    '{DB01A1E3-A42B-11cf-8F20-00805F2CD064}'
)


class IActiveScriptSite(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSite
    _idlflags_ = []


IID_IActiveScriptError = IID(
    '{EAE1BA61-A4ED-11cf-8F20-00805F2CD064}'
)


class IActiveScriptError(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptError
    _idlflags_ = []


IID_IActiveScriptError64 = IID(
    '{B21FB2A1-5B8F-4963-8C21-21450F84ED7F}'
)


class IActiveScriptError64(IActiveScriptError):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptError64
    _idlflags_ = []


IID_IActiveScriptSiteWindow = IID(
    '{D10F6761-83E9-11cf-8F20-00805F2CD064}'
)


class IActiveScriptSiteWindow(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSiteWindow
    _idlflags_ = []


IID_IActiveScriptSiteUIControl = IID(
    '{AEDAE97E-D7EE-4796-B960-7F092AE844AB}'
)


class IActiveScriptSiteUIControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSiteUIControl
    _idlflags_ = []


IID_IActiveScriptSiteInterruptPoll = IID(
    '{539698A0-CDCA-11CF-A5EB-00AA0047A063}'
)


class IActiveScriptSiteInterruptPoll(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSiteInterruptPoll
    _idlflags_ = []


IID_IActiveScript = IID(
    '{BB1A2AE1-A4F9-11cf-8F20-00805F2CD064}'
)


class IActiveScript(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScript
    _idlflags_ = []


IID_IActiveScriptParse32 = IID(
    '{BB1A2AE2-A4F9-11cf-8F20-00805F2CD064}'
)


class IActiveScriptParse32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParse32
    _idlflags_ = []


IID_IActiveScriptParse64 = IID(
    '{C7EF7658-E1EE-480E-97EA-D52CB4D76D17}'
)


class IActiveScriptParse64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParse64
    _idlflags_ = []


IID_IActiveScriptParseProcedureOld32 = IID(
    '{1CFF0050-6FDD-11d0-9328-00A0C90DCAA9}'
)


class IActiveScriptParseProcedureOld32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParseProcedureOld32
    _idlflags_ = []


IID_IActiveScriptParseProcedureOld64 = IID(
    '{21F57128-08C9-4638-BA12-22D15D88DC5C}'
)


class IActiveScriptParseProcedureOld64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParseProcedureOld64
    _idlflags_ = []


IID_IActiveScriptParseProcedure32 = IID(
    '{AA5B6A80-B834-11d0-932F-00A0C90DCAA9}'
)


class IActiveScriptParseProcedure32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParseProcedure32
    _idlflags_ = []


IID_IActiveScriptParseProcedure64 = IID(
    '{C64713B6-E029-4CC5-9200-438B72890B6A}'
)


class IActiveScriptParseProcedure64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParseProcedure64
    _idlflags_ = []


IID_IActiveScriptParseProcedure2_32 = IID(
    '{71EE5B20-FB04-11d1-B3A8-00A0C911E8B2}'
)


class IActiveScriptParseProcedure2_32(IActiveScriptParseProcedure32):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParseProcedure2_32
    _idlflags_ = []


IID_IActiveScriptParseProcedure2_64 = IID(
    '{FE7C4271-210C-448D-9F54-76DAB7047B28}'
)


class IActiveScriptParseProcedure2_64(IActiveScriptParseProcedure64):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptParseProcedure2_64
    _idlflags_ = []


IID_IActiveScriptEncode = IID(
    '{BB1A2AE3-A4F9-11cf-8F20-00805F2CD064}'
)


class IActiveScriptEncode(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptEncode
    _idlflags_ = []


IID_IActiveScriptHostEncode = IID(
    '{BEE9B76E-CFE3-11d1-B747-00C04FC2B085}'
)


class IActiveScriptHostEncode(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptHostEncode
    _idlflags_ = []


IID_IBindEventHandler = IID(
    '{63CDBCB0-C1B1-11d0-9336-00A0C90DCAA9}'
)


class IBindEventHandler(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBindEventHandler
    _idlflags_ = []


IID_IActiveScriptStats = IID(
    '{B8DA6310-E19B-11d0-933C-00A0C90DCAA9}'
)


class IActiveScriptStats(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptStats
    _idlflags_ = []


IID_IActiveScriptProperty = IID(
    '{4954E0D0-FBC7-11D1-8410-006008C3FBFC}'
)


class IActiveScriptProperty(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptProperty
    _idlflags_ = []


IID_ITridentEventSink = IID(
    '{1DC9CA50-06EF-11d2-8415-006008C3FBFC}'
)


class ITridentEventSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITridentEventSink
    _idlflags_ = []


IID_IActiveScriptGarbageCollector = IID(
    '{6AA2C4A0-2B53-11d4-A2A0-00104BD35090}'
)


class IActiveScriptGarbageCollector(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptGarbageCollector
    _idlflags_ = []


IID_IActiveScriptSIPInfo = IID(
    '{764651D0-38DE-11d4-A2A3-00104BD35090}'
)


class IActiveScriptSIPInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSIPInfo
    _idlflags_ = []


IID_IActiveScriptSiteTraceInfo = IID(
    '{4B7272AE-1955-4bfe-98B0-780621888569}'
)


class IActiveScriptSiteTraceInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSiteTraceInfo
    _idlflags_ = []


IID_IActiveScriptTraceInfo = IID(
    '{C35456E7-BEBF-4a1b-86A9-24D56BE8B369}'
)


class IActiveScriptTraceInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptTraceInfo
    _idlflags_ = []


IID_IActiveScriptStringCompare = IID(
    '{58562769-ED52-42f7-8403-4963514E1F11}'
)


class IActiveScriptStringCompare(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptStringCompare
    _idlflags_ = []


from ocidl_h import * # NOQA
from winapifamily_h import * # NOQA
CATID_ActiveScript = DEFINE_GUID(
    0xF0B7A1A1,
    0x9847,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
CATID_ActiveScriptParse = DEFINE_GUID(
    0xF0B7A1A2,
    0x9847,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
CATID_ActiveScriptEncode = DEFINE_GUID(
    0xF0B7A1A3,
    0x9847,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
STATIC_IID_IActiveScript = DEFINE_GUID(
    0xBB1A2AE1,
    0xA4F9,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
STATIC_IID_IActiveScriptParse32 = DEFINE_GUID(
    0xBB1A2AE2,
    0xA4F9,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
STATIC_IID_IActiveScriptParse64 = DEFINE_GUID(
    0xC7EF7658,
    0xE1EE,
    0x480E,
    0x97,
    0xEA,
    0xD5,
    0x2C,
    0xB4,
    0xD7,
    0x6D,
    0x17
)
STATIC_IID_IActiveScriptEncode = DEFINE_GUID(
    0xBB1A2AE3,
    0xA4F9,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
STATIC_IID_IActiveScriptHostEncode = DEFINE_GUID(
    0xBEE9B76E,
    0xCFE3,
    0x11D1,
    0xB7,
    0x47,
    0x00,
    0xC0,
    0x4F,
    0xC2,
    0xB0,
    0x85
)
STATIC_IID_IActiveScriptParseProcedureOld32 = DEFINE_GUID(
    0x1CFF0050,
    0x6FDD,
    0x11D0,
    0x93,
    0x28,
    0x00,
    0xA0,
    0xC9,
    0x0D,
    0xCA,
    0xA9
)
STATIC_IID_IActiveScriptParseProcedureOld64 = DEFINE_GUID(
    0x21F57128,
    0x08C9,
    0x4638,
    0xBA,
    0x12,
    0x22,
    0xD1,
    0x5D,
    0x88,
    0xDC,
    0x5C
)
STATIC_IID_IActiveScriptParseProcedure32 = DEFINE_GUID(
    0xAA5B6A80,
    0xB834,
    0x11D0,
    0x93,
    0x2F,
    0x00,
    0xA0,
    0xC9,
    0x0D,
    0xCA,
    0xA9
)
STATIC_IID_IActiveScriptParseProcedure64 = DEFINE_GUID(
    0xC64713B6,
    0xE029,
    0x4CC5,
    0x92,
    0x00,
    0x43,
    0x8B,
    0x72,
    0x89,
    0x0B,
    0x6A
)
STATIC_IID_IActiveScriptParseProcedure2_32 = DEFINE_GUID(
    0x71EE5B20,
    0xFB04,
    0x11D1,
    0xB3,
    0xA8,
    0x00,
    0xA0,
    0xC9,
    0x11,
    0xE8,
    0xB2
)
STATIC_IID_IActiveScriptParseProcedure2_64 = DEFINE_GUID(
    0xFE7C4271,
    0x210C,
    0x448D,
    0x9F,
    0x54,
    0x76,
    0xDA,
    0xB7,
    0x04,
    0x7B,
    0x28
)
STATIC_IID_IActiveScriptSite = DEFINE_GUID(
    0xDB01A1E3,
    0xA42B,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
STATIC_IID_IActiveScriptSiteTraceInfo = DEFINE_GUID(
    0x4B7272AE,
    0x1955,
    0x4BFE,
    0x98,
    0xB0,
    0x78,
    0x6,
    0x21,
    0x88,
    0x85,
    0x69
)
STATIC_IID_IActiveScriptSiteWindow = DEFINE_GUID(
    0xD10F6761,
    0x83E9,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
STATIC_IID_IActiveScriptSiteInterruptPoll = DEFINE_GUID(
    0x539698A0,
    0xCDCA,
    0x11CF,
    0xA5,
    0xEB,
    0x00,
    0xAA,
    0x00,
    0x47,
    0xA0,
    0x63
)
STATIC_IID_IActiveScriptSiteUIControl = DEFINE_GUID(
    0xAEDAE97E,
    0xD7EE,
    0x4796,
    0xB9,
    0x60,
    0x7F,
    0x9,
    0x2A,
    0xE8,
    0x44,
    0xAB
)
STATIC_IID_IActiveScriptError = DEFINE_GUID(
    0xEAE1BA61,
    0xA4ED,
    0x11CF,
    0x8F,
    0x20,
    0x00,
    0x80,
    0x5F,
    0x2C,
    0xD0,
    0x64
)
STATIC_IID_IActiveScriptError64 = DEFINE_GUID(
    0xB21FB2A1,
    0x5B8F,
    0x4963,
    0x8C,
    0x21,
    0x21,
    0x45,
    0x0F,
    0x84,
    0xED,
    0x7F
)
STATIC_IID_IBindEventHandler = DEFINE_GUID(
    0x63CDBCB0,
    0xC1B1,
    0x11D0,
    0x93,
    0x36,
    0x00,
    0xA0,
    0xC9,
    0x0D,
    0xCA,
    0xA9
)
STATIC_IID_IActiveScriptStats = DEFINE_GUID(
    0xB8DA6310,
    0xE19B,
    0x11D0,
    0x93,
    0x3C,
    0x00,
    0xA0,
    0xC9,
    0x0D,
    0xCA,
    0xA9
)
STATIC_IID_IActiveScriptProperty = DEFINE_GUID(
    0x4954E0D0,
    0xFBC7,
    0x11D1,
    0x84,
    0x10,
    0x00,
    0x60,
    0x08,
    0xC3,
    0xFB,
    0xFC
)
STATIC_IID_ITridentEventSink = DEFINE_GUID(
    0x1DC9CA50,
    0x6EF,
    0x11D2,
    0x84,
    0x15,
    0x00,
    0x60,
    0x08,
    0xC3,
    0xFB,
    0xFC
)
STATIC_IID_IActiveScriptGarbageCollector = DEFINE_GUID(
    0x6AA2C4A0,
    0x2B53,
    0x11D4,
    0xA2,
    0xA0,
    0x00,
    0x10,
    0x4B,
    0xD3,
    0x50,
    0x90
)
STATIC_IID_IActiveScriptSIPInfo = DEFINE_GUID(
    0x764651D0,
    0x38DE,
    0x11D4,
    0xA2,
    0xA3,
    0x00,
    0x10,
    0x4B,
    0xD3,
    0x50,
    0x90
)
STATIC_IID_IActiveScriptTraceInfo = DEFINE_GUID(
    0xC35456E7,
    0xBEBF,
    0x4A1B,
    0x86,
    0xA9,
    0x24,
    0xD5,
    0x6B,
    0xE8,
    0xB3,
    0x69
)
OID_VBSSIP = DEFINE_GUID(
    0x1629F04E,
    0x2799,
    0x4DB5,
    0x8F,
    0xE5,
    0xAC,
    0xE1,
    0x0F,
    0x17,
    0xEB,
    0xAB
)
OID_JSSIP = DEFINE_GUID(
    0x6C9E010,
    0x38CE,
    0x11D4,
    0xA2,
    0xA3,
    0x00,
    0x10,
    0x4B,
    0xD3,
    0x50,
    0x90
)
OID_WSFSIP = DEFINE_GUID(
    0x1A610570,
    0x38CE,
    0x11D4,
    0xA2,
    0xA3,
    0x00,
    0x10,
    0x4B,
    0xD3,
    0x50,
    0x90
)
STATIC_IID_IActiveScriptStringCompare = DEFINE_GUID(
    0x58562769,
    0xED52,
    0x42F7,
    0x84,
    0x03,
    0x49,
    0x63,
    0x51,
    0x4E,
    0x1F,
    0x11
)
SCRIPTITEM_ISVISIBLE = 0x00000002
SCRIPTITEM_ISSOURCE = 0x00000004
SCRIPTITEM_GLOBALMEMBERS = 0x00000008
SCRIPTITEM_ISPERSISTENT = 0x00000040
SCRIPTITEM_CODEONLY = 0x00000200
SCRIPTITEM_NOCODE = 0x00000400
SCRIPTITEM_ALL_FLAGS = (
    SCRIPTITEM_ISSOURCE  |
     SCRIPTITEM_ISVISIBLE  |
     SCRIPTITEM_ISPERSISTENT  |
     SCRIPTITEM_GLOBALMEMBERS  |
     SCRIPTITEM_NOCODE  |
     SCRIPTITEM_CODEONLY
)
SCRIPTTYPELIB_ISCONTROL = 0x00000010
SCRIPTTYPELIB_ISPERSISTENT = 0x00000040
SCRIPTTYPELIB_ALL_FLAGS = SCRIPTTYPELIB_ISCONTROL | SCRIPTTYPELIB_ISPERSISTENT
SCRIPTTEXT_DELAYEXECUTION = 0x00000001
SCRIPTTEXT_ISVISIBLE = 0x00000002
SCRIPTTEXT_ISEXPRESSION = 0x00000020
SCRIPTTEXT_ISPERSISTENT = 0x00000040
SCRIPTTEXT_HOSTMANAGESSOURCE = 0x00000080
SCRIPTTEXT_ISXDOMAIN = 0x00000100
SCRIPTTEXT_ISNONUSERCODE = 0x00000200
SCRIPTTEXT_ALL_FLAGS = (
    SCRIPTTEXT_DELAYEXECUTION  |
     SCRIPTTEXT_ISVISIBLE  |
     SCRIPTTEXT_ISEXPRESSION  |
     SCRIPTTEXT_ISPERSISTENT  |
     SCRIPTTEXT_HOSTMANAGESSOURCE  |
     SCRIPTTEXT_ISXDOMAIN  |
     SCRIPTTEXT_ISNONUSERCODE
)
SCRIPTPROC_ISEXPRESSION = 0x00000020
SCRIPTPROC_HOSTMANAGESSOURCE = 0x00000080
SCRIPTPROC_IMPLICIT_THIS = 0x00000100
SCRIPTPROC_IMPLICIT_PARENTS = 0x00000200
SCRIPTPROC_ISXDOMAIN = 0x00000400
SCRIPTPROC_ALL_FLAGS = (
    SCRIPTPROC_HOSTMANAGESSOURCE  |
     SCRIPTPROC_ISEXPRESSION  |
     SCRIPTPROC_IMPLICIT_THIS  |
     SCRIPTPROC_IMPLICIT_PARENTS  |
     SCRIPTPROC_ISXDOMAIN
)
SCRIPTINFO_IUNKNOWN = 0x00000001
SCRIPTINFO_ITYPEINFO = 0x00000002
SCRIPTINFO_ALL_FLAGS = SCRIPTINFO_IUNKNOWN | SCRIPTINFO_ITYPEINFO
SCRIPTINTERRUPT_DEBUG = 0x00000001
SCRIPTINTERRUPT_RAISEEXCEPTION = 0x00000002
SCRIPTINTERRUPT_ALL_FLAGS = (
    SCRIPTINTERRUPT_DEBUG  |
     SCRIPTINTERRUPT_RAISEEXCEPTION
)
SCRIPTSTAT_STATEMENT_COUNT = 0x00000001
SCRIPTSTAT_INSTRUCTION_COUNT = 0x00000002
SCRIPTSTAT_INTSTRUCTION_TIME = 0x00000003
SCRIPTSTAT_TOTAL_TIME = 0x00000004
SCRIPT_ENCODE_SECTION = 0x00000001
SCRIPT_ENCODE_DEFAULT_LANGUAGE = 0x00000001
SCRIPT_ENCODE_NO_ASP_LANGUAGE = 0x00000002
SCRIPTPROP_NAME = 0x00000000
SCRIPTPROP_MAJORVERSION = 0x00000001
SCRIPTPROP_MINORVERSION = 0x00000002
SCRIPTPROP_BUILDNUMBER = 0x00000003
SCRIPTPROP_DELAYEDEVENTSINKING = 0x00001000
SCRIPTPROP_CATCHEXCEPTION = 0x00001001
SCRIPTPROP_CONVERSIONLCID = 0x00001002
SCRIPTPROP_HOSTSTACKREQUIRED = 0x00001003
SCRIPTPROP_SCRIPTSAREFULLYTRUSTED = 0x00001004
SCRIPTPROP_DEBUGGER = 0x00001100
SCRIPTPROP_JITDEBUG = 0x00001101
SCRIPTPROP_GCCONTROLSOFTCLOSE = 0x00002000
SCRIPTPROP_INTEGERMODE = 0x00003000
SCRIPTPROP_STRINGCOMPAREINSTANCE = 0x00003001
SCRIPTPROP_INVOKEVERSIONING = 0x00004000
SCRIPTPROP_HACK_FIBERSUPPORT = 0x70000000
SCRIPTPROP_HACK_TRIDENTEVENTSINK = 0x70000001
SCRIPTPROP_ABBREVIATE_GLOBALNAME_RESOLUTION = 0x70000002
SCRIPTPROP_HOSTKEEPALIVE = 0x70000004
SCRIPT_E_RECORDED = 0x86664004
SCRIPT_E_REPORTED = 0x80020101
SCRIPT_E_PROPAGATE = 0x80020102
class tagSCRIPTLANGUAGEVERSION(ENUM):
    SCRIPTLANGUAGEVERSION_DEFAULT = 0
    SCRIPTLANGUAGEVERSION_5_7 = 1
    SCRIPTLANGUAGEVERSION_5_8 = 2
    SCRIPTLANGUAGEVERSION_MAX = 255


SCRIPTLANGUAGEVERSION = tagSCRIPTLANGUAGEVERSION


class tagSCRIPTSTATE(ENUM):
    SCRIPTSTATE_UNINITIALIZED = 0
    SCRIPTSTATE_INITIALIZED = 5
    SCRIPTSTATE_STARTED = 1
    SCRIPTSTATE_CONNECTED = 2
    SCRIPTSTATE_DISCONNECTED = 3
    SCRIPTSTATE_CLOSED = 4


SCRIPTSTATE = tagSCRIPTSTATE


class tagSCRIPTTRACEINFO(ENUM):
    SCRIPTTRACEINFO_SCRIPTSTART = 0
    SCRIPTTRACEINFO_SCRIPTEND = 1
    SCRIPTTRACEINFO_COMCALLSTART = 2
    SCRIPTTRACEINFO_COMCALLEND = 3
    SCRIPTTRACEINFO_CREATEOBJSTART = 4
    SCRIPTTRACEINFO_CREATEOBJEND = 5
    SCRIPTTRACEINFO_GETOBJSTART = 6
    SCRIPTTRACEINFO_GETOBJEND = 7


SCRIPTTRACEINFO = tagSCRIPTTRACEINFO


class tagSCRIPTTHREADSTATE(ENUM):
    SCRIPTTHREADSTATE_NOTINSCRIPT = 0
    SCRIPTTHREADSTATE_RUNNING = 1


SCRIPTTHREADSTATE = tagSCRIPTTHREADSTATE


class tagSCRIPTGCTYPE(ENUM):
    SCRIPTGCTYPE_NORMAL = 0
    SCRIPTGCTYPE_EXHAUSTIVE = 1


SCRIPTGCTYPE = tagSCRIPTGCTYPE


class tagSCRIPTUICITEM(ENUM):
    SCRIPTUICITEM_INPUTBOX = 1
    SCRIPTUICITEM_MSGBOX = 2


SCRIPTUICITEM = tagSCRIPTUICITEM


class tagSCRIPTUICHANDLING(ENUM):
    SCRIPTUICHANDLING_ALLOW = 0
    SCRIPTUICHANDLING_NOUIERROR = 1
    SCRIPTUICHANDLING_NOUIDEFAULT = 2


SCRIPTUICHANDLING = tagSCRIPTUICHANDLING


SCRIPTTHREADID = DWORD
SCRIPTTHREADID_CURRENT = -1
SCRIPTTHREADID_BASE = -2
SCRIPTTHREADID_ALL = -3
COMMETHOD = comtypes.COMMETHOD

from propidl_h import VARIANT
from oaidl_h import ITypeInfo, EXCEPINFO, IDispatch, DISPPARAMS

IActiveScriptSite._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetLCID',
        ([], POINTER(LCID), 'plcid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetItemInfo',
        ([], LPCOLESTR, 'pstrName'),
        ([], DWORD, 'dwReturnMask'),
        ([], POINTER(POINTER(comtypes.IUnknown)), 'ppiunkItem'),
        ([], POINTER(POINTER(ITypeInfo)), 'ppti'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDocVersionString',
        ([], POINTER(BSTR), 'pbstrVersion'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnScriptTerminate',
        ([], POINTER(VARIANT), 'pvarResult'),
        ([], POINTER(EXCEPINFO), 'pexcepinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnStateChange',
        ([], SCRIPTSTATE, 'ssScriptState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnScriptError',
        ([], POINTER(IActiveScriptError), 'pscripterror'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnLeaveScript'
    ),
]


IActiveScriptError._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetExceptionInfo',
        ([], POINTER(EXCEPINFO), 'pexcepinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSourcePosition',
        ([], POINTER(DWORD), 'pdwSourceContext'),
        ([], POINTER(ULONG), 'pulLineNumber'),
        ([], POINTER(LONG), 'plCharacterPosition'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSourceLineText',
        ([], POINTER(BSTR), 'pbstrSourceLine'),
    ),
]


IActiveScriptError64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSourcePosition64',
        ([], POINTER(DWORDLONG), 'pdwSourceContext'),
        ([], POINTER(ULONG), 'pulLineNumber'),
        ([], POINTER(LONG), 'plCharacterPosition'),
    ),
]


IActiveScriptSiteWindow._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetWindow',
        ([], POINTER(HWND), 'phwnd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnableModeless',
        ([], BOOL, 'fEnable'),
    ),
]


IActiveScriptSiteUIControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetUIBehavior',
        ([], SCRIPTUICITEM, 'UicItem'),
        ([], POINTER(SCRIPTUICHANDLING), 'pUicHandling'),
    ),
]


IActiveScriptSiteInterruptPoll._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryContinue'
    ),
]


IActiveScript._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetScriptSite',
        ([], POINTER(IActiveScriptSite), 'pass'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptSite',
        ([], REFIID, 'riid'),
        ([], POINTER(POINTER(VOID)), 'ppvObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetScriptState',
        ([], SCRIPTSTATE, 'ss'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptState',
        ([], POINTER(SCRIPTSTATE), 'pssState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddNamedItem',
        ([], LPCOLESTR, 'pstrName'),
        ([], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddTypeLib',
        ([], REFGUID, 'rguidTypeLib'),
        ([], DWORD, 'dwMajor'),
        ([], DWORD, 'dwMinor'),
        ([], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptDispatch',
        ([], LPCOLESTR, 'pstrItemName'),
        ([], POINTER(POINTER(IDispatch)), 'ppdisp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentScriptThreadID',
        ([], POINTER(SCRIPTTHREADID), 'pstidThread'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptThreadID',
        ([], DWORD, 'dwWin32ThreadId'),
        ([], POINTER(SCRIPTTHREADID), 'pstidThread'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptThreadState',
        ([], SCRIPTTHREADID, 'stidThread'),
        ([], POINTER(SCRIPTTHREADSTATE), 'pstsState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InterruptScriptThread',
        ([], SCRIPTTHREADID, 'stidThread'),
        ([], POINTER(EXCEPINFO), 'pexcepinfo'),
        ([], DWORD, 'dwFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        ([], POINTER(POINTER(IActiveScript)), 'ppscript'),
    ),
]


IActiveScriptParse32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddScriptlet',
        ([], LPCOLESTR, 'pstrDefaultName'),
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], LPCOLESTR, 'pstrSubItemName'),
        ([], LPCOLESTR, 'pstrEventName'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORD, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(BSTR), 'pbstrName'),
        ([], POINTER(EXCEPINFO), 'pexcepinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ParseScriptText',
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], POINTER(comtypes.IUnknown), 'punkContext'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORD, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(VARIANT), 'pvarResult'),
        ([], POINTER(EXCEPINFO), 'pexcepinfo'),
    ),
]


IActiveScriptParse64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddScriptlet',
        ([], LPCOLESTR, 'pstrDefaultName'),
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], LPCOLESTR, 'pstrSubItemName'),
        ([], LPCOLESTR, 'pstrEventName'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORDLONG, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(BSTR), 'pbstrName'),
        ([], POINTER(EXCEPINFO), 'pexcepinfo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ParseScriptText',
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], POINTER(comtypes.IUnknown), 'punkContext'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORDLONG, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(VARIANT), 'pvarResult'),
        ([], POINTER(EXCEPINFO), 'pexcepinfo'),
    ),
]


IActiveScriptParse = IActiveScriptParse64
IID_IActiveScriptParse = IID_IActiveScriptParse64

PIActiveScriptParse = POINTER(IActiveScriptParse)
IActiveScriptParseProcedureOld32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseProcedureText',
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrFormalParams'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], POINTER(comtypes.IUnknown), 'punkContext'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORD, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(POINTER(IDispatch)), 'ppdisp'),
    ),
]


IActiveScriptParseProcedureOld64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseProcedureText',
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrFormalParams'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], POINTER(comtypes.IUnknown), 'punkContext'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORDLONG, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(POINTER(IDispatch)), 'ppdisp'),
    ),
]


IActiveScriptParseProcedureOld = IActiveScriptParseProcedureOld64
IID_IActiveScriptParseProcedureOld = IID_IActiveScriptParseProcedureOld64

PIActiveScriptParseProcedureOld = POINTER(IActiveScriptParseProcedureOld)
IActiveScriptParseProcedure32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseProcedureText',
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrFormalParams'),
        ([], LPCOLESTR, 'pstrProcedureName'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], POINTER(comtypes.IUnknown), 'punkContext'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORD, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(POINTER(IDispatch)), 'ppdisp'),
    ),
]


IActiveScriptParseProcedure64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseProcedureText',
        ([], LPCOLESTR, 'pstrCode'),
        ([], LPCOLESTR, 'pstrFormalParams'),
        ([], LPCOLESTR, 'pstrProcedureName'),
        ([], LPCOLESTR, 'pstrItemName'),
        ([], POINTER(comtypes.IUnknown), 'punkContext'),
        ([], LPCOLESTR, 'pstrDelimiter'),
        ([], DWORDLONG, 'dwSourceContextCookie'),
        ([], ULONG, 'ulStartingLineNumber'),
        ([], DWORD, 'dwFlags'),
        ([], POINTER(POINTER(IDispatch)), 'ppdisp'),
    ),
]


IActiveScriptParseProcedure = IActiveScriptParseProcedure64
IID_IActiveScriptParseProcedure = IID_IActiveScriptParseProcedure64

PIActiveScriptParseProcedure = POINTER(IActiveScriptParseProcedure)
IActiveScriptParseProcedure2 = IActiveScriptParseProcedure2_64
IID_IActiveScriptParseProcedure2 = IID_IActiveScriptParseProcedure2_64

PIActiveScriptParseProcedure2 = POINTER(IActiveScriptParseProcedure2)
IActiveScriptEncode._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EncodeSection',
        ([], LPCOLESTR, 'pchIn'),
        ([], DWORD, 'cchIn'),
        ([], LPOLESTR, 'pchOut'),
        ([], DWORD, 'cchOut'),
        ([], POINTER(DWORD), 'pcchRet'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DecodeScript',
        ([], LPCOLESTR, 'pchIn'),
        ([], DWORD, 'cchIn'),
        ([], LPOLESTR, 'pchOut'),
        ([], DWORD, 'cchOut'),
        ([], POINTER(DWORD), 'pcchRet'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetEncodeProgId',
        ([], POINTER(BSTR), 'pbstrOut'),
    ),
]


IActiveScriptHostEncode._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EncodeScriptHostFile',
        ([], BSTR, 'bstrInFile'),
        ([], POINTER(BSTR), 'pbstrOutFile'),
        ([], LONG, 'cFlags'),
        ([], BSTR, 'bstrDefaultLang'),
    ),
]


IBindEventHandler._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'BindHandler',
        ([], LPCOLESTR, 'pstrEvent'),
        ([], POINTER(IDispatch), 'pdisp'),
    ),
]


IActiveScriptStats._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetStat',
        ([], DWORD, 'stid'),
        ([], POINTER(ULONG), 'pluHi'),
        ([], POINTER(ULONG), 'pluLo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStatEx',
        ([], REFGUID, 'guid'),
        ([], POINTER(ULONG), 'pluHi'),
        ([], POINTER(ULONG), 'pluLo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ResetStats'
    ),
]


IActiveScriptProperty._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetProperty',
        ([], DWORD, 'dwProperty'),
        ([], POINTER(VARIANT), 'pvarIndex'),
        ([], POINTER(VARIANT), 'pvarValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetProperty',
        ([], DWORD, 'dwProperty'),
        ([], POINTER(VARIANT), 'pvarIndex'),
        ([], POINTER(VARIANT), 'pvarValue'),
    ),
]


ITridentEventSink._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'FireEvent',
        ([], LPCOLESTR, 'pstrEvent'),
        ([], POINTER(DISPPARAMS), 'pdp'),
        ([], POINTER(VARIANT), 'pvarRes'),
        ([], POINTER(EXCEPINFO), 'pei'),
    ),
]


IActiveScriptGarbageCollector._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CollectGarbage',
        ([], SCRIPTGCTYPE, 'scriptgctype'),
    ),
]


IActiveScriptSIPInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSIPOID',
        ([], POINTER(GUID), 'poid_sip'),
    ),
]


IActiveScriptSiteTraceInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SendScriptTraceInfo',
        ([], SCRIPTTRACEINFO, 'stiEventType'),
        ([], GUID, 'guidContextID'),
        ([], DWORD, 'dwScriptContextCookie'),
        ([], LONG, 'lScriptStatementStart'),
        ([], LONG, 'lScriptStatementEnd'),
        ([], DWORD64, 'dwReserved'),
    ),
]


IActiveScriptTraceInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StartScriptTracing',
        ([], POINTER(IActiveScriptSiteTraceInfo), 'pSiteTraceInfo'),
        ([], GUID, 'guidContextID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'StopScriptTracing'
    ),
]


IActiveScriptStringCompare._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StrComp',
        ([], BSTR, 'bszStr1'),
        ([], BSTR, 'bszStr2'),
        ([], POINTER(LONG), 'iRet'),
    ),
]


__all__ = (
    'IActiveScriptGarbageCollector', 'IActiveScriptEncode', 'IActiveScript',
    'IActiveScriptHostEncode', 'IActiveScriptParseProcedure64', 'SCRIPTSTATE',
    'IActiveScriptStringCompare', 'IActiveScriptError64', 'ITridentEventSink',
    'IActiveScriptSiteUIControl', 'IActiveScriptParseProcedure2_32',
    'IActiveScriptParse32', 'IActiveScriptParseProcedureOld64', 'OID_WSFSIP',
    'IActiveScriptSiteTraceInfo', 'IActiveScriptSiteWindow', 'tagSCRIPTSTATE',
    'IBindEventHandler', 'IActiveScriptSite', 'IActiveScriptParseProcedure32',
    'IActiveScriptParse64', 'IActiveScriptStats', 'IActiveScriptError',
    'IActiveScriptParseProcedureOld32', 'IActiveScriptProperty', 'OID_JSSIP',
    'IActiveScriptParseProcedure2_64', 'IActiveScriptTraceInfo', 'OID_VBSSIP',
    'IActiveScriptSIPInfo', 'IActiveScriptSiteInterruptPoll', 'SCRIPTUICITEM',
    'SCRIPTINFO_ALL_FLAGS', 'SCRIPTINTERRUPT_DEBUG', 'SCRIPTPROC_ISXDOMAIN',
    'SCRIPTPROP_GCCONTROLSOFTCLOSE', 'SCRIPTTYPELIB_ISPERSISTENT',
    'SCRIPTPROC_HOSTMANAGESSOURCE', 'IID_IActiveScriptParseProcedureOld',
    'SCRIPTPROP_BUILDNUMBER', 'SCRIPTINFO_ITYPEINFO', 'SCRIPT_E_PROPAGATE',
    'SCRIPTPROP_HACK_FIBERSUPPORT', 'SCRIPTINTERRUPT_RAISEEXCEPTION',
    'SCRIPTPROC_ISEXPRESSION', 'SCRIPTPROP_JITDEBUG', 'SCRIPT_E_REPORTED',
    'SCRIPTSTAT_INSTRUCTION_COUNT', 'SCRIPTITEM_CODEONLY', 'SCRIPTPROP_NAME',
    'SCRIPTITEM_GLOBALMEMBERS', 'SCRIPTTEXT_ISXDOMAIN', 'SCRIPTTHREADID_BASE',
    'IID_IActiveScriptParseProcedure', 'SCRIPTINTERRUPT_ALL_FLAGS',
    'SCRIPTSTAT_STATEMENT_COUNT', 'SCRIPTTHREADID_CURRENT', 'tagSCRIPTGCTYPE',
    'SCRIPTTEXT_ISVISIBLE', 'SCRIPT_ENCODE_SECTION', 'SCRIPTITEM_ALL_FLAGS',
    'IActiveScriptParseProcedure2', 'SCRIPTINFO_IUNKNOWN', 'tagSCRIPTUICITEM',
    'SCRIPTPROP_CATCHEXCEPTION', 'SCRIPTSTAT_TOTAL_TIME', 'SCRIPT_E_RECORDED',
    'SCRIPTPROP_DEBUGGER', 'SCRIPTTEXT_ISPERSISTENT', 'SCRIPTITEM_ISSOURCE',
    'SCRIPTTEXT_HOSTMANAGESSOURCE', 'SCRIPTTYPELIB_ALL_FLAGS', 'SCRIPTGCTYPE',
    'SCRIPTPROP_STRINGCOMPAREINSTANCE', 'SCRIPT_ENCODE_DEFAULT_LANGUAGE',
    'SCRIPTTEXT_ISEXPRESSION', 'SCRIPTPROP_MAJORVERSION', 'SCRIPTITEM_NOCODE',
    '__REQUIRED_RPCNDR_H_VERSION__', 'SCRIPTPROP_MINORVERSION',
    'SCRIPTPROP_ABBREVIATE_GLOBALNAME_RESOLUTION', 'SCRIPTPROP_HOSTKEEPALIVE',
    'SCRIPTPROP_DELAYEDEVENTSINKING', '__REQUIRED_RPCSAL_H_VERSION__',
    'IID_IActiveScriptParse', 'SCRIPTPROP_INVOKEVERSIONING', 'SCRIPTTHREADID',
    'SCRIPTTHREADID_ALL', 'SCRIPTPROP_SCRIPTSAREFULLYTRUSTED',
    'SCRIPTSTAT_INTSTRUCTION_TIME', 'SCRIPTTEXT_ISNONUSERCODE',
    'SCRIPTTEXT_DELAYEXECUTION', 'SCRIPTPROP_INTEGERMODE', 'SCRIPTTRACEINFO',
    'SCRIPTTYPELIB_ISCONTROL', 'SCRIPTPROC_IMPLICIT_PARENTS',
    'IID_IActiveScriptParseProcedure2', 'SCRIPTPROP_HOSTSTACKREQUIRED',
    'SCRIPTITEM_ISVISIBLE', 'SCRIPTPROC_IMPLICIT_THIS', 'IActiveScriptParse',
    'SCRIPTPROC_ALL_FLAGS', 'SCRIPTTEXT_ALL_FLAGS', 'SCRIPTITEM_ISPERSISTENT',
    'SCRIPTPROP_HACK_TRIDENTEVENTSINK', 'SCRIPT_ENCODE_NO_ASP_LANGUAGE',
    'SCRIPTPROP_CONVERSIONLCID', 'IActiveScriptParseProcedure',
    'IActiveScriptParseProcedureOld', 'SCRIPTTHREADSTATE',
    'tagSCRIPTTHREADSTATE', 'SCRIPTUICHANDLING', 'SCRIPTLANGUAGEVERSION',
    'tagSCRIPTUICHANDLING', 'tagSCRIPTTRACEINFO', 'tagSCRIPTLANGUAGEVERSION',
    'IID_IActiveScriptError64', 'IID_IActiveScriptTraceInfo',
    'IID_IActiveScriptProperty', 'IID_IActiveScriptStats',
    'IID_IActiveScriptParseProcedure64', 'IID_IActiveScriptSiteInterruptPoll',
    'IID_IActiveScriptParseProcedure2_32', 'IID_IBindEventHandler',
    'IID_IActiveScriptStringCompare', 'IID_IActiveScriptParse32',
    'IID_IActiveScriptSiteWindow', 'IID_IActiveScriptParseProcedure32',
    'IID_IActiveScript', 'IID_IActiveScriptParseProcedure2_64',
    'IID_IActiveScriptParseProcedureOld32', 'IID_IActiveScriptSiteTraceInfo',
    'CATID_ActiveScriptParse', 'CATID_ActiveScript', 'IID_IActiveScriptError',
    'IID_IActiveScriptGarbageCollector', 'IID_IActiveScriptSiteUIControl',
    'IID_IActiveScriptEncode', 'IID_ITridentEventSink', 'PIActiveScriptParse',
    'CATID_ActiveScriptEncode', 'IID_IActiveScriptParseProcedureOld64',
    'IID_IActiveScriptSIPInfo', 'IID_IActiveScriptParse64',
    'IID_IActiveScriptSite', 'IID_IActiveScriptHostEncode',
    'PIActiveScriptParseProcedure2', 'PIActiveScriptParseProcedure',
    'PIActiveScriptParseProcedureOld',
)
