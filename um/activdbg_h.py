

from wtypes_h import (
    ENUM,
    LPCOLESTR,
    HRESULT,
    POINTER,
    DWORD,
    REFGUID,
    BOOL,
    DWORDLONG,
    ULONG,
    OLECHAR,
    UINT,
    BSTR,
    GUID,
    CLSID,
    LPCSTR,
    REFCLSID,
    REFIID,
    WCHAR,
    VARTYPE,
    WORD
)
from guiddef_h import (
    IID,
)
import ctypes
import comtypes


__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
# __REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
IID_IDebugCodeContext = IID(
    '{51973C13-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugCodeContext(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugCodeContext
    _idlflags_ = []


IID_IDebugAsyncOperation = IID(
    '{51973C1b-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugAsyncOperation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugAsyncOperation
    _idlflags_ = []


IID_IDebugAsyncOperationCallBack = IID(
    '{51973C1c-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugAsyncOperationCallBack(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugAsyncOperationCallBack
    _idlflags_ = []


IID_IDebugDocumentInfo = IID(
    '{51973C1f-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentInfo
    _idlflags_ = []


IID_IDebugDocumentProvider = IID(
    '{51973C20-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentProvider(IDebugDocumentInfo):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentProvider
    _idlflags_ = []


IID_IDebugDocument = IID(
    '{51973C21-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocument(IDebugDocumentInfo):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocument
    _idlflags_ = []


IID_IDebugDocumentText = IID(
    '{51973C22-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentText(IDebugDocument):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentText
    _idlflags_ = []


IID_IDebugDocumentTextEvents = IID(
    '{51973C23-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentTextEvents(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentTextEvents
    _idlflags_ = []


IID_IDebugDocumentTextAuthor = IID(
    '{51973C24-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentTextAuthor(IDebugDocumentText):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentTextAuthor
    _idlflags_ = []


IID_IDebugDocumentTextExternalAuthor = IID(
    '{51973C25-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentTextExternalAuthor(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentTextExternalAuthor
    _idlflags_ = []


IID_IDebugDocumentHelper32 = IID(
    '{51973C26-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentHelper32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentHelper32
    _idlflags_ = []


IID_IDebugDocumentHelper64 = IID(
    '{c4c7363c-20fd-47f9-bd82-4855e0150871}'
)


class IDebugDocumentHelper64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentHelper64
    _idlflags_ = []


IID_IDebugDocumentHost = IID(
    '{51973C27-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentHost(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentHost
    _idlflags_ = []


IID_IDebugDocumentContext = IID(
    '{51973C28-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugDocumentContext(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugDocumentContext
    _idlflags_ = []


IID_IDebugSessionProvider = IID(
    '{51973C29-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugSessionProvider(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugSessionProvider
    _idlflags_ = []


IID_IApplicationDebuggerUI = IID(
    '{51973C2b-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IApplicationDebuggerUI(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IApplicationDebuggerUI
    _idlflags_ = []


IID_IProcessDebugManager32 = IID(
    '{51973C2f-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IProcessDebugManager32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IProcessDebugManager32
    _idlflags_ = []


IID_IProcessDebugManager64 = IID(
    '{56b9fc1c-63a9-4cc1-ac21-087d69a17fab}'
)


class IProcessDebugManager64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IProcessDebugManager64
    _idlflags_ = []


IID_IRemoteDebugApplication = IID(
    '{51973C30-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IRemoteDebugApplication(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRemoteDebugApplication
    _idlflags_ = []


IID_IDebugApplication32 = IID(
    '{51973C32-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugApplication32(IRemoteDebugApplication):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplication32
    _idlflags_ = []


IID_IDebugApplication64 = IID(
    '{4dedc754-04c7-4f10-9e60-16a390fe6e62}'
)


class IDebugApplication64(IRemoteDebugApplication):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplication64
    _idlflags_ = []


IID_IDebugApplicationNode = IID(
    '{51973C34-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugApplicationNode(IDebugDocumentProvider):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationNode
    _idlflags_ = []


IID_IDebugApplicationNodeEvents = IID(
    '{51973C35-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugApplicationNodeEvents(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationNodeEvents
    _idlflags_ = []


IID_AsyncIDebugApplicationNodeEvents = IID(
    '{a2e3aa3b-aa8d-4ebf-84cd-648b737b8c13}'
)


class AsyncIDebugApplicationNodeEvents(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIDebugApplicationNodeEvents
    _idlflags_ = []


IID_IDebugThreadCall32 = IID(
    '{51973C36-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugThreadCall32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugThreadCall32
    _idlflags_ = []


IID_IDebugThreadCall64 = IID(
    '{cb3fa335-e979-42fd-9fcf-a7546a0f3905}'
)


class IDebugThreadCall64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugThreadCall64
    _idlflags_ = []


IID_IRemoteDebugApplicationThread = IID(
    '{51973C37-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IRemoteDebugApplicationThread(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRemoteDebugApplicationThread
    _idlflags_ = []


IID_IDebugApplicationThread = IID(
    '{51973C38-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugApplicationThread(IRemoteDebugApplicationThread):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationThread
    _idlflags_ = []


IID_IDebugApplicationThread64 = IID(
    '{9dac5886-dbad-456d-9dee-5dec39ab3dda}'
)


class IDebugApplicationThread64(IDebugApplicationThread):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationThread64
    _idlflags_ = []


IID_IDebugCookie = IID(
    '{51973C39-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugCookie(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugCookie
    _idlflags_ = []


IID_IEnumDebugApplicationNodes = IID(
    '{51973C3a-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumDebugApplicationNodes(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDebugApplicationNodes
    _idlflags_ = []


IID_IEnumRemoteDebugApplications = IID(
    '{51973C3b-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumRemoteDebugApplications(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumRemoteDebugApplications
    _idlflags_ = []


IID_IEnumRemoteDebugApplicationThreads = IID(
    '{51973C3c-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumRemoteDebugApplicationThreads(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumRemoteDebugApplicationThreads
    _idlflags_ = []


IID_IDebugFormatter = IID(
    '{51973C05-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugFormatter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugFormatter
    _idlflags_ = []


IID_ISimpleConnectionPoINT = IID(
    '{51973C3e-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class ISimpleConnectionPoINT(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISimpleConnectionPoINT
    _idlflags_ = []


IID_IDebugHelper = IID(
    '{51973C3f-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugHelper(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugHelper
    _idlflags_ = []


IID_IEnumDebugExpressionContexts = IID(
    '{51973C40-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumDebugExpressionContexts(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDebugExpressionContexts
    _idlflags_ = []


IID_IProvideExpressionContexts = IID(
    '{51973C41-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IProvideExpressionContexts(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IProvideExpressionContexts
    _idlflags_ = []


IID_IActiveScriptDebug32 = IID(
    '{51973C10-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IActiveScriptDebug32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptDebug32
    _idlflags_ = ['nonextensible']



CLSID_ProcessDebugManager = IID(
    '{78a51821-51f4-11d0-8f20-00805f2cd064}'
)

class ProcessDebugManagerLib(object):
    name = 'ProcessDebugManagerLib'
    _reg_typelib_ = ('', 1, 0)



IID_IActiveScriptDebug64 = IID(
    '{bc437e23-f5b8-47f4-bb79-7d1ce5483b86}'
)


class IActiveScriptDebug64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptDebug64
    _idlflags_ = []


IID_IActiveScriptErrorDebug = IID(
    '{51973C12-CB0C-11d0-B5C9-00A0244A0E7A}'
)
from activscp_h import IActiveScriptError

class IActiveScriptErrorDebug(IActiveScriptError):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptErrorDebug
    _idlflags_ = []


IID_IActiveScriptSiteDebug32 = IID(
    '{51973C11-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IActiveScriptSiteDebug32(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSiteDebug32
    _idlflags_ = []


IID_IActiveScriptSiteDebug64 = IID(
    '{d6b96b0a-7463-402c-92ac-89984226942f}'
)


class IActiveScriptSiteDebug64(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSiteDebug64
    _idlflags_ = []


IID_IActiveScriptSiteDebugEx = IID(
    '{BB722CCB-6AD2-41c6-B780-AF9C03EE69F5}'
)


class IActiveScriptSiteDebugEx(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptSiteDebugEx
    _idlflags_ = []


IID_IApplicationDebugger = IID(
    '{51973C2a-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IApplicationDebugger(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IApplicationDebugger
    _idlflags_ = []


IID_IDebugExpression = IID(
    '{51973C14-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugExpression(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugExpression
    _idlflags_ = []


IID_IDebugExpressionCallBack = IID(
    '{51973C16-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugExpressionCallBack(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugExpressionCallBack
    _idlflags_ = []


IID_IDebugExpressionContext = IID(
    '{51973C15-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugExpressionContext(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugExpressionContext
    _idlflags_ = []


IID_IDebugStackFrame = IID(
    '{51973C17-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugStackFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugStackFrame
    _idlflags_ = []


IID_IDebugStackFrameSniffer = IID(
    '{51973C18-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugStackFrameSniffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugStackFrameSniffer
    _idlflags_ = []


IID_IDebugStackFrameSnifferEx32 = IID(
    '{51973C19-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugStackFrameSnifferEx32(IDebugStackFrameSniffer):
    _case_insensitive_ = True
    _iid_ = IID_IDebugStackFrameSnifferEx32
    _idlflags_ = []


IID_IDebugStackFrameSnifferEx64 = IID(
    '{8cd12af4-49c1-4d52-8d8a-c146f47581aa}'
)


class IDebugStackFrameSnifferEx64(IDebugStackFrameSniffer):
    _case_insensitive_ = True
    _iid_ = IID_IDebugStackFrameSnifferEx64
    _idlflags_ = []


IID_IDebugSyncOperation = IID(
    '{51973C1a-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IDebugSyncOperation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugSyncOperation
    _idlflags_ = []


IID_IEnumDebugCodeContexts = IID(
    '{51973C1d-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumDebugCodeContexts(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDebugCodeContexts
    _idlflags_ = []


IID_IEnumDebugStackFrames = IID(
    '{51973C1e-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IEnumDebugStackFrames(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDebugStackFrames
    _idlflags_ = []


IID_IEnumDebugStackFrames64 = IID(
    '{0dc38853-c1b0-4176-a984-b298361027af}'
)


class IEnumDebugStackFrames64(IEnumDebugStackFrames):
    _case_insensitive_ = True
    _iid_ = IID_IEnumDebugStackFrames64
    _idlflags_ = []


IID_IMachineDebugManager = IID(
    '{51973C2c-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IMachineDebugManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMachineDebugManager
    _idlflags_ = []


IID_IMachineDebugManagerCookie = IID(
    '{51973C2d-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IMachineDebugManagerCookie(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMachineDebugManagerCookie
    _idlflags_ = []


IID_IMachineDebugManagerEvents = IID(
    '{51973C2e-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IMachineDebugManagerEvents(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMachineDebugManagerEvents
    _idlflags_ = []


IID_IRemoteDebugApplicationEvents = IID(
    '{51973C33-CB0C-11d0-B5C9-00A0244A0E7A}'
)


class IRemoteDebugApplicationEvents(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRemoteDebugApplicationEvents
    _idlflags_ = []


class ProcessDebugManager(ctypes.Structure):
    pass


class DebugHelper(ctypes.Structure):
    pass


class CDebugDocumentHelper(ctypes.Structure):
    pass


class MachineDebugManager_RETAIL(ctypes.Structure):
    pass


class MachineDebugManager_DEBUG(ctypes.Structure):
    pass


class DefaultDebugSessionProvider(ctypes.Structure):
    pass


from ocidl_h import * # NOQA
from activscp_h import * # NOQA
from dbgprop_h import * # NOQA
from winapifamily_h import * # NOQA
class tagBREAKPOINT_STATE(ENUM):
    BREAKPOINT_DELETED = 0
    BREAKPOINT_DISABLED = 1
    BREAKPOINT_ENABLED = 2


BREAKPOINT_STATE = tagBREAKPOINT_STATE


APPBREAKFLAGS = DWORD
APPBREAKFLAG_DEBUGGER_BLOCK = 0x00000001
APPBREAKFLAG_DEBUGGER_HALT = 0x00000002
APPBREAKFLAG_STEP = 0x00010000
APPBREAKFLAG_NESTED = 0x00020000
APPBREAKFLAG_STEPTYPE_SOURCE = 0x00000000
APPBREAKFLAG_STEPTYPE_BYTECODE = 0x00100000
APPBREAKFLAG_STEPTYPE_MACHINE = 0x00200000
APPBREAKFLAG_STEPTYPE_MASK = 0x00F00000
APPBREAKFLAG_IN_BREAKPOINT = 0x80000000


class tagBREAKREASON(ENUM):
    BREAKREASON_STEP = 0
    BREAKREASON_BREAKPOINT = BREAKREASON_STEP + 1
    BREAKREASON_DEBUGGER_BLOCK = BREAKREASON_BREAKPOINT + 1
    BREAKREASON_HOST_INITIATED = BREAKREASON_DEBUGGER_BLOCK + 1
    BREAKREASON_LANGUAGE_INITIATED = BREAKREASON_HOST_INITIATED + 1
    BREAKREASON_DEBUGGER_HALT = BREAKREASON_LANGUAGE_INITIATED + 1
    BREAKREASON_ERROR = BREAKREASON_DEBUGGER_HALT + 1
    BREAKREASON_JIT = BREAKREASON_ERROR + 1
    BREAKREASON_MUTATION_BREAKPOINT = BREAKREASON_JIT + 1


BREAKREASON = tagBREAKREASON


class tagBREAKRESUME_ACTION(ENUM):
    BREAKRESUMEACTION_ABORT = 0
    BREAKRESUMEACTION_CONTINUE = BREAKRESUMEACTION_ABORT + 1
    BREAKRESUMEACTION_STEP_INTO = BREAKRESUMEACTION_CONTINUE + 1
    BREAKRESUMEACTION_STEP_OVER = BREAKRESUMEACTION_STEP_INTO + 1
    BREAKRESUMEACTION_STEP_OUT = BREAKRESUMEACTION_STEP_OVER + 1
    BREAKRESUMEACTION_IGNORE = BREAKRESUMEACTION_STEP_OUT + 1
    BREAKRESUMEACTION_STEP_DOCUMENT = BREAKRESUMEACTION_IGNORE + 1


BREAKRESUMEACTION = tagBREAKRESUME_ACTION


class tagERRORRESUMEACTION(ENUM):
    ERRORRESUMEACTION_ReexecuteErrorStatement = 0
    ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller = (
        ERRORRESUMEACTION_ReexecuteErrorStatement + 1
    )
    ERRORRESUMEACTION_SkipErrorStatement = (
        ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller + 1
    )


ERRORRESUMEACTION = tagERRORRESUMEACTION


class tagDOCUMENTNAMETYPE(ENUM):
    DOCUMENTNAMETYPE_APPNODE = 0
    DOCUMENTNAMETYPE_TITLE = DOCUMENTNAMETYPE_APPNODE + 1
    DOCUMENTNAMETYPE_FILE_TAIL = DOCUMENTNAMETYPE_TITLE + 1
    DOCUMENTNAMETYPE_URL = DOCUMENTNAMETYPE_FILE_TAIL + 1
    DOCUMENTNAMETYPE_UNIQUE_TITLE = DOCUMENTNAMETYPE_URL + 1
    DOCUMENTNAMETYPE_SOURCE_MAP_URL = DOCUMENTNAMETYPE_UNIQUE_TITLE + 1


DOCUMENTNAMETYPE = tagDOCUMENTNAMETYPE


SOURCE_TEXT_ATTR = WORD
SOURCETEXT_ATTR_KEYWORD = 0x00000001
SOURCETEXT_ATTR_COMMENT = 0x00000002
SOURCETEXT_ATTR_NONSOURCE = 0x00000004
SOURCETEXT_ATTR_OPERATOR = 0x00000008
SOURCETEXT_ATTR_NUMBER = 0x00000010
SOURCETEXT_ATTR_STRING = 0x00000020
SOURCETEXT_ATTR_FUNCTION_START = 0x00000040
TEXT_DOC_ATTR = DWORD
TEXT_DOC_ATTR_READONLY = 0x00000001
TEXT_DOC_ATTR_TYPE_PRIMARY = 0x00000002
TEXT_DOC_ATTR_TYPE_WORKER = 0x00000004
TEXT_DOC_ATTR_TYPE_SCRIPT = 0x00000008
DEBUG_TEXT_ISEXPRESSION = 0x00000001
DEBUG_TEXT_RETURNVALUE = 0x00000002
DEBUG_TEXT_NOSIDEEFFECTS = 0x00000004
DEBUG_TEXT_ALLOWBREAKPOINTS = 0x00000008
DEBUG_TEXT_ALLOWERRORREPORT = 0x00000010
DEBUG_TEXT_EVALUATETOCODECONTEXT = 0x00000020
DEBUG_TEXT_ISNONUSERCODE = 0x00000040
IActiveScriptDebug = IActiveScriptDebug64
IID_IActiveScriptDebug = IID_IActiveScriptDebug64

COMMETHOD = comtypes.COMMETHOD


IActiveScriptDebug32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptTextAttributes',
        (['in'], LPCOLESTR, 'pstrCode'),
        (['in'], ULONG, 'uNumCodeChars'),
        (['in'], LPCOLESTR, 'pstrDelimiter'),
        (['in'], DWORD, 'dwFlags'),
        (['in', 'out'], POINTER(SOURCE_TEXT_ATTR), 'pattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptletTextAttributes',
        (['in'], LPCOLESTR, 'pstrCode'),
        (['in'], ULONG, 'uNumCodeChars'),
        (['in'], LPCOLESTR, 'pstrDelimiter'),
        (['in'], DWORD, 'dwFlags'),
        (['in', 'out'], POINTER(SOURCE_TEXT_ATTR), 'pattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumCodeContextsOfPosition',
        (['in'], DWORD, 'dwSourceContext'),
        (['in'], ULONG, 'uCharacterOffset'),
        (['in'], ULONG, 'uNumChars'),
        (['out'], POINTER(POINTER(IEnumDebugCodeContexts)), 'ppescc'),
    ),
]


IActiveScriptDebug64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptTextAttributes',
        (['in'], LPCOLESTR, 'pstrCode'),
        (['in'], ULONG, 'uNumCodeChars'),
        (['in'], LPCOLESTR, 'pstrDelimiter'),
        (['in'], DWORD, 'dwFlags'),
        (['in', 'out'], POINTER(SOURCE_TEXT_ATTR), 'pattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptletTextAttributes',
        (['in'], LPCOLESTR, 'pstrCode'),
        (['in'], ULONG, 'uNumCodeChars'),
        (['in'], LPCOLESTR, 'pstrDelimiter'),
        (['in'], DWORD, 'dwFlags'),
        (['in', 'out'], POINTER(SOURCE_TEXT_ATTR), 'pattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumCodeContextsOfPosition',
        (['in'], DWORDLONG, 'dwSourceContext'),
        (['in'], ULONG, 'uCharacterOffset'),
        (['in'], ULONG, 'uNumChars'),
        (['out'], POINTER(POINTER(IEnumDebugCodeContexts)), 'ppescc'),
    ),
]


IActiveScriptSiteDebug = IActiveScriptSiteDebug64
IID_IActiveScriptSiteDebug = IID_IActiveScriptSiteDebug64

IActiveScriptSiteDebug32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentContextFromPosition',
        (['in'], DWORD, 'dwSourceContext'),
        (['in'], ULONG, 'uCharacterOffset'),
        (['in'], ULONG, 'uNumChars'),
        (['out'], POINTER(POINTER(IDebugDocumentContext)), 'ppsc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetApplication',
        (['out'], POINTER(POINTER(IDebugApplication32)), 'ppda'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRootApplicationNode',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'ppdanRoot'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnScriptErrorDebug',
        (['in'], POINTER(IActiveScriptErrorDebug), 'pErrorDebug'),
        (['out'], POINTER(BOOL), 'pfEnterDebugger'),
        (['out'], POINTER(BOOL), 'pfCallOnScriptErrorWhenContinuing'),
    ),
]


IActiveScriptSiteDebug64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentContextFromPosition',
        (['in'], DWORDLONG, 'dwSourceContext'),
        (['in'], ULONG, 'uCharacterOffset'),
        (['in'], ULONG, 'uNumChars'),
        (['out'], POINTER(POINTER(IDebugDocumentContext)), 'ppsc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetApplication',
        (['out'], POINTER(POINTER(IDebugApplication64)), 'ppda'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRootApplicationNode',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'ppdanRoot'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnScriptErrorDebug',
        (['in'], POINTER(IActiveScriptErrorDebug), 'pErrorDebug'),
        (['out'], POINTER(BOOL), 'pfEnterDebugger'),
        (['out'], POINTER(BOOL), 'pfCallOnScriptErrorWhenContinuing'),
    ),
]


IActiveScriptSiteDebugEx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnCanNotJITScriptErrorDebug',
        (['in'], POINTER(IActiveScriptErrorDebug), 'pErrorDebug'),
        (['out'], POINTER(BOOL), 'pfCallOnScriptErrorWhenContinuing'),
    ),
]


IActiveScriptErrorDebug._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentContext',
        (['out'], POINTER(POINTER(IDebugDocumentContext)), 'ppssc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStackFrame',
        (['out'], POINTER(POINTER(IDebugStackFrame)), 'ppdsf'),
    ),
]


IDebugCodeContext._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentContext',
        (['out'], POINTER(POINTER(IDebugDocumentContext)), 'ppsc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBreakPoINT',
        (['in'], BREAKPOINT_STATE, 'bps'),
    ),
]


IDebugExpression._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Start',
        (['in'], POINTER(IDebugExpressionCallBack), 'pdecb'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetResultAsString',
        (['out'], POINTER(HRESULT), 'phrResult'),
        (['out'], POINTER(BSTR), 'pbstrResult'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetResultAsDebugProperty',
        (['out'], POINTER(HRESULT), 'phrResult'),
        (['out'], POINTER(POINTER(IDebugProperty)), 'ppdp'),
    ),
]


IDebugExpressionContext._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ParseLanguageText',
        (['in'], LPCOLESTR, 'pstrCode'),
        (['in'], UINT, 'nRadix'),
        (['in'], LPCOLESTR, 'pstrDelimiter'),
        (['in'], DWORD, 'dwFlags'),
        (['out'], POINTER(POINTER(IDebugExpression)), 'ppe'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLanguageInfo',
        (['out'], POINTER(BSTR), 'pbstrLanguageName'),
        (['out'], POINTER(GUID), 'pLanguageID'),
    ),
]


IDebugExpressionCallBack._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'onComplete'
    ),
]


IDebugStackFrame._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCodeContext',
        (['out'], POINTER(POINTER(IDebugCodeContext)), 'ppcc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDescriptionString',
        (['in'], BOOL, 'fLong'),
        (['out'], POINTER(BSTR), 'pbstrDescription'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLanguageString',
        (['in'], BOOL, 'fLong'),
        (['out'], POINTER(BSTR), 'pbstrLanguage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetThread',
        (['out'], POINTER(POINTER(IDebugApplicationThread)), 'ppat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDebugProperty',
        (['out'], POINTER(POINTER(IDebugProperty)), 'ppDebugProp'),
    ),
]


IDebugStackFrameSniffer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumStackFrames',
        (['out'], POINTER(POINTER(IEnumDebugStackFrames)), 'ppedsf'),
    ),
]


IDebugStackFrameSnifferEx = IDebugStackFrameSnifferEx64
IID_IDebugStackFrameSnifferEx = IID_IDebugStackFrameSnifferEx64

IDebugStackFrameSnifferEx32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumStackFramesEx32',
        (['in'], DWORD, 'dwSpMin'),
        (['out'], POINTER(POINTER(IEnumDebugStackFrames)), 'ppedsf'),
    ),
]


IDebugStackFrameSnifferEx64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumStackFramesEx64',
        (['in'], DWORDLONG, 'dwSpMin'),
        (['out'], POINTER(POINTER(IEnumDebugStackFrames64)), 'ppedsf'),
    ),
]


IDebugSyncOperation._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetTargetThread',
        (['out'], POINTER(POINTER(IDebugApplicationThread)), 'ppatTarget'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Execute',
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppunkResult'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'InProgressAbort'
    ),
]


IDebugAsyncOperation._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSyncDebugOperation',
        (['out'], POINTER(POINTER(IDebugSyncOperation)), 'ppsdo'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Start',
        ([], POINTER(IDebugAsyncOperationCallBack), 'padocb'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetResult',
        (['out'], POINTER(HRESULT), 'phrResult'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppunkResult'),
    ),
]


IDebugAsyncOperationCallBack._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'onComplete'
    ),
]


IEnumDebugCodeContexts._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(POINTER(IDebugCodeContext)), 'pscc'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumDebugCodeContexts)), 'ppescc'),
    ),
]


class tagDebugStackFrameDescriptor(ctypes.Structure):
    _fields_ = [
        ('pdsf', POINTER(IDebugStackFrame)),
        ('dwMin', DWORD),
        ('dwLim', DWORD),
        ('fFinal', BOOL),
        ('punkFinal', POINTER(comtypes.IUnknown)),
    ]


DebugStackFrameDescriptor = tagDebugStackFrameDescriptor


class tagDebugStackFrameDescriptor64(ctypes.Structure):
    _fields_ = [
        ('pdsf', POINTER(IDebugStackFrame)),
        ('dwMin', DWORDLONG),
        ('dwLim', DWORDLONG),
        ('fFinal', BOOL),
        ('punkFinal', POINTER(comtypes.IUnknown)),
    ]


DebugStackFrameDescriptor64 = tagDebugStackFrameDescriptor64


IEnumDebugStackFrames._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(DebugStackFrameDescriptor), 'prgdsfd'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumDebugStackFrames)), 'ppedsf'),
    ),
]


IEnumDebugStackFrames64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next64',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(DebugStackFrameDescriptor64), 'prgdsfd'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
    ),
]


IDebugDocumentInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetName',
        (['in'], DOCUMENTNAMETYPE, 'dnt'),
        (['out'], POINTER(BSTR), 'pbstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentClassId',
        (['out'], POINTER(CLSID), 'pclsidDocument'),
    ),
]


IDebugDocumentProvider._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDocument',
        (['out'], POINTER(POINTER(IDebugDocument)), 'ppssd'),
    ),
]


IDebugDocumentText._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDocumentAttributes',
        (['out'], POINTER(TEXT_DOC_ATTR), 'ptextdocattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSize',
        (['out'], POINTER(ULONG), 'pcNumLines'),
        (['out'], POINTER(ULONG), 'pcNumChars'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPositionOfLine',
        (['in'], ULONG, 'cLineNumber'),
        (['out'], POINTER(ULONG), 'pcCharacterPosition'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetLineOfPosition',
        (['in'], ULONG, 'cCharacterPosition'),
        (['out'], POINTER(ULONG), 'pcLineNumber'),
        (['out'], POINTER(ULONG), 'pcCharacterOffsetInLine'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetText',
        (['in'], ULONG, 'cCharacterPosition'),
        ([], POINTER(WCHAR), 'pCHARText'),
        ([], POINTER(SOURCE_TEXT_ATTR), 'pstaTextAttr'),
        (['in', 'out'], POINTER(ULONG), 'pcNumChars'),
        (['in'], ULONG, 'cMaxChars'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPositionOfContext',
        (['in'], POINTER(IDebugDocumentContext), 'psc'),
        (['out'], POINTER(ULONG), 'pcCharacterPosition'),
        (['out'], POINTER(ULONG), 'cNumChars'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetContextOfPosition',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumChars'),
        (['out'], POINTER(POINTER(IDebugDocumentContext)), 'ppsc'),
    ),
]


IDebugDocumentTextEvents._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'onInsertText',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumToInsert'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onRemoveText',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumToRemove'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onReplaceText',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumToReplace'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onUpdateTextAttributes',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumToUpdate'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onUpdateDocumentAttributes',
        (['in'], TEXT_DOC_ATTR, 'textdocattr'),
    ),
]


IDebugDocumentTextAuthor._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'InsertText',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumToInsert'),
        (['in'], OLECHAR, 'pCHARText[]'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveText',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumToRemove'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReplaceText',
        (['in'], ULONG, 'cCharacterPosition'),
        (['in'], ULONG, 'cNumToReplace'),
        (['in'], OLECHAR, 'pCHARText[]'),
    ),
]


IDebugDocumentTextExternalAuthor._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetPathName',
        (['out'], POINTER(BSTR), 'pbstrLongName'),
        (['out'], POINTER(BOOL), 'pfIsOriginalFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFileName',
        (['out'], POINTER(BSTR), 'pbstrShortName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyChanged'
    ),
]


IDebugDocumentHelper = IDebugDocumentHelper64
IID_IDebugDocumentHelper = IID_IDebugDocumentHelper64

IDebugDocumentHelper32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Init',
        (['in'], POINTER(IDebugApplication32), 'pda'),
        (['in'], LPCOLESTR, 'pszShortName'),
        (['in'], LPCOLESTR, 'pszLongName'),
        (['in'], TEXT_DOC_ATTR, 'docAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Attach',
        (['in'], POINTER(IDebugDocumentHelper32), 'pddhParent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddUnicodeText',
        (['in'], LPCOLESTR, 'pszText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddDBCSText',
        (['in'], LPCSTR, 'pszText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDebugDocumentHost',
        (['in'], POINTER(IDebugDocumentHost), 'pddh'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddDeferredText',
        (['in'], ULONG, 'cChars'),
        (['in'], DWORD, 'dwTextStartCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DefineScriptBlock',
        (['in'], ULONG, 'ulCharOffset'),
        (['in'], ULONG, 'cChars'),
        (['in'], POINTER(IActiveScript), 'pas'),
        (['in'], BOOL, 'fScriptlet'),
        (['out'], POINTER(DWORD), 'pdwSourceContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultTextAttr',
        ([], SOURCE_TEXT_ATTR, 'staTextAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTextAttributes',
        (['in'], ULONG, 'ulCharOffset'),
        (['in'], ULONG, 'cChars'),
        ([], POINTER(SOURCE_TEXT_ATTR), 'pstaTextAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLongName',
        (['in'], LPCOLESTR, 'pszLongName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetShortName',
        (['in'], LPCOLESTR, 'pszShortName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDocumentAttr',
        (['in'], TEXT_DOC_ATTR, 'pszAttributes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDebugApplicationNode',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'ppdan'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptBlockInfo',
        (['in'], DWORD, 'dwSourceContext'),
        (['out'], POINTER(POINTER(IActiveScript)), 'ppasd'),
        (['out'], POINTER(ULONG), 'piCharPos'),
        (['out'], POINTER(ULONG), 'pcChars'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateDebugDocumentContext',
        (['in'], ULONG, 'iCharPos'),
        (['in'], ULONG, 'cChars'),
        (['out'], POINTER(POINTER(IDebugDocumentContext)), 'ppddc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BringDocumentContextToTop',
        ([], POINTER(IDebugDocumentContext), 'pddc'),
    ),
]


IDebugDocumentHelper64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Init',
        (['in'], POINTER(IDebugApplication64), 'pda'),
        (['in'], LPCOLESTR, 'pszShortName'),
        (['in'], LPCOLESTR, 'pszLongName'),
        (['in'], TEXT_DOC_ATTR, 'docAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Attach',
        (['in'], POINTER(IDebugDocumentHelper64), 'pddhParent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddUnicodeText',
        (['in'], LPCOLESTR, 'pszText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddDBCSText',
        (['in'], LPCSTR, 'pszText'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDebugDocumentHost',
        (['in'], POINTER(IDebugDocumentHost), 'pddh'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddDeferredText',
        (['in'], ULONG, 'cChars'),
        (['in'], DWORD, 'dwTextStartCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DefineScriptBlock',
        (['in'], ULONG, 'ulCharOffset'),
        (['in'], ULONG, 'cChars'),
        (['in'], POINTER(IActiveScript), 'pas'),
        (['in'], BOOL, 'fScriptlet'),
        (['out'], POINTER(DWORDLONG), 'pdwSourceContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDefaultTextAttr',
        ([], SOURCE_TEXT_ATTR, 'staTextAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetTextAttributes',
        (['in'], ULONG, 'ulCharOffset'),
        (['in'], ULONG, 'cChars'),
        ([], POINTER(SOURCE_TEXT_ATTR), 'pstaTextAttr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetLongName',
        (['in'], LPCOLESTR, 'pszLongName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetShortName',
        (['in'], LPCOLESTR, 'pszShortName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDocumentAttr',
        (['in'], TEXT_DOC_ATTR, 'pszAttributes'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDebugApplicationNode',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'ppdan'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptBlockInfo',
        (['in'], DWORDLONG, 'dwSourceContext'),
        (['out'], POINTER(POINTER(IActiveScript)), 'ppasd'),
        (['out'], POINTER(ULONG), 'piCharPos'),
        (['out'], POINTER(ULONG), 'pcChars'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateDebugDocumentContext',
        (['in'], ULONG, 'iCharPos'),
        (['in'], ULONG, 'cChars'),
        (['out'], POINTER(POINTER(IDebugDocumentContext)), 'ppddc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BringDocumentContextToTop',
        ([], POINTER(IDebugDocumentContext), 'pddc'),
    ),
]


IDebugDocumentHost._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDeferredText',
        (['in'], DWORD, 'dwTextStartCookie'),
        ([], POINTER(WCHAR), 'pCHARText'),
        ([], POINTER(SOURCE_TEXT_ATTR), 'pstaTextAttr'),
        (['in', 'out'], POINTER(ULONG), 'pcNumChars'),
        (['in'], ULONG, 'cMaxChars'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptTextAttributes',
        (['in'], LPCOLESTR, 'pstrCode'),
        (['in'], ULONG, 'uNumCodeChars'),
        (['in'], LPCOLESTR, 'pstrDelimiter'),
        (['in'], DWORD, 'dwFlags'),
        (['in', 'out'], POINTER(SOURCE_TEXT_ATTR), 'pattr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnCreateDocumentContext',
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppunkOuter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetPathName',
        (['out'], POINTER(BSTR), 'pbstrLongName'),
        (['out'], POINTER(BOOL), 'pfIsOriginalFile'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetFileName',
        (['out'], POINTER(BSTR), 'pbstrShortName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NotifyChanged'
    ),
]


IDebugDocumentContext._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDocument',
        (['out'], POINTER(POINTER(IDebugDocument)), 'ppsd'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumCodeContexts',
        (['out'], POINTER(POINTER(IEnumDebugCodeContexts)), 'ppescc'),
    ),
]


IDebugSessionProvider._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'StartDebugSession',
        (['in'], POINTER(IRemoteDebugApplication), 'pda'),
    ),
]


IApplicationDebugger._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateInstanceAtDebugger',
        (['in'], REFCLSID, 'rclsid'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
        (['in'], DWORD, 'dwClsContext'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppvObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onDebugOutput',
        (['in'], LPCOLESTR, 'pstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onHandleBreakPoINT',
        (['in'], POINTER(IRemoteDebugApplicationThread), 'prpt'),
        (['in'], BREAKREASON, 'br'),
        (['in'], POINTER(IActiveScriptErrorDebug), 'pError'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onDebuggerEvent',
        (['in'], REFIID, 'riid'),
        (['in'], POINTER(comtypes.IUnknown), 'punk'),
    ),
]


IApplicationDebuggerUI._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'BringDocumentToTop',
        (['in'], POINTER(IDebugDocumentText), 'pddt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BringDocumentContextToTop',
        (['in'], POINTER(IDebugDocumentContext), 'pddc'),
    ),
]


IMachineDebugManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddApplication',
        (['in'], POINTER(IRemoteDebugApplication), 'pda'),
        (['out'], POINTER(DWORD), 'pdwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveApplication',
        (['in'], DWORD, 'dwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumApplications',
        (['out'], POINTER(POINTER(IEnumRemoteDebugApplications)), 'ppeda'),
    ),
]


IMachineDebugManagerCookie._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddApplication',
        (['in'], POINTER(IRemoteDebugApplication), 'pda'),
        (['in'], DWORD, 'dwDebugAppCookie'),
        (['out'], POINTER(DWORD), 'pdwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveApplication',
        (['in'], DWORD, 'dwDebugAppCookie'),
        (['in'], DWORD, 'dwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumApplications',
        (['out'], POINTER(POINTER(IEnumRemoteDebugApplications)), 'ppeda'),
    ),
]


IMachineDebugManagerEvents._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'onAddApplication',
        (['in'], POINTER(IRemoteDebugApplication), 'pda'),
        (['in'], DWORD, 'dwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onRemoveApplication',
        (['in'], POINTER(IRemoteDebugApplication), 'pda'),
        (['in'], DWORD, 'dwAppCookie'),
    ),
]


IProcessDebugManager = IProcessDebugManager64
IID_IProcessDebugManager = IID_IProcessDebugManager64

IProcessDebugManager32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateApplication',
        (['out'], POINTER(POINTER(IDebugApplication32)), 'ppda'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultApplication',
        (['out'], POINTER(POINTER(IDebugApplication32)), 'ppda'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddApplication',
        (['in'], POINTER(IDebugApplication32), 'pda'),
        (['out'], POINTER(DWORD), 'pdwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveApplication',
        (['in'], DWORD, 'dwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateDebugDocumentHelper',
        (['in'], POINTER(comtypes.IUnknown), 'punkOuter'),
        (['out'], POINTER(POINTER(IDebugDocumentHelper32)), 'pddh'),
    ),
]


IProcessDebugManager64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateApplication',
        (['out'], POINTER(POINTER(IDebugApplication64)), 'ppda'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDefaultApplication',
        (['out'], POINTER(POINTER(IDebugApplication64)), 'ppda'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddApplication',
        (['in'], POINTER(IDebugApplication64), 'pda'),
        (['out'], POINTER(DWORD), 'pdwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveApplication',
        (['in'], DWORD, 'dwAppCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateDebugDocumentHelper',
        (['in'], POINTER(comtypes.IUnknown), 'punkOuter'),
        (['out'], POINTER(POINTER(IDebugDocumentHelper64)), 'pddh'),
    ),
]


IRemoteDebugApplication._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ResumeFromBreakPoINT',
        (['in'], POINTER(IRemoteDebugApplicationThread), 'prptFocus'),
        (['in'], BREAKRESUMEACTION, 'bra'),
        (['in'], ERRORRESUMEACTION, 'era'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ConnectDebugger',
        (['in'], POINTER(IApplicationDebugger), 'pad'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDebugger',
        (['out'], POINTER(POINTER(IApplicationDebugger)), 'pad'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateInstanceAtApplication',
        (['in'], REFCLSID, 'rclsid'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
        (['in'], DWORD, 'dwClsContext'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppvObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumThreads',
        (['out'], POINTER(POINTER(IEnumRemoteDebugApplicationThreads)), 'pperdat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetName',
        (['out'], POINTER(BSTR), 'pbstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRootNode',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'ppdanRoot'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumGlobalExpressionContexts',
        (['out'], POINTER(POINTER(IEnumDebugExpressionContexts)), 'ppedec'),
    ),
]


IDebugApplication = IDebugApplication64
IID_IDebugApplication = IID_IDebugApplication64

IDebugApplication32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetName',
        (['in'], LPCOLESTR, 'pstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DebugOutput',
        (['in'], LPCOLESTR, 'pstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HandleBreakPoINT',
        (['in'], BREAKREASON, 'br'),
        (['out'], POINTER(BREAKRESUMEACTION), 'pbra'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBreakFlags',
        (['out'], POINTER(APPBREAKFLAGS), 'pabf'),
        (['out'], POINTER(POINTER(IRemoteDebugApplicationThread)), 'pprdatSteppingThread'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentThread',
        (['out'], POINTER(POINTER(IDebugApplicationThread)), 'pat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateAsyncDebugOperation',
        (['in'], POINTER(IDebugSyncOperation), 'psdo'),
        (['out'], POINTER(POINTER(IDebugAsyncOperation)), 'ppado'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddStackFrameSniffer',
        (['in'], POINTER(IDebugStackFrameSniffer), 'pdsfs'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveStackFrameSniffer',
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SynchronousCallInDebuggerThread',
        (['in'], POINTER(IDebugThreadCall32), 'pptc'),
        (['in'], DWORD, 'dwParam1'),
        (['in'], DWORD, 'dwParam2'),
        (['in'], DWORD, 'dwParam3'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateApplicationNode',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'ppdanNew'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FireDebuggerEvent',
        (['in'], REFGUID, 'riid'),
        (['in'], POINTER(comtypes.IUnknown), 'punk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HandleRuntimeError',
        (['in'], POINTER(IActiveScriptErrorDebug), 'pErrorDebug'),
        (['in'], POINTER(IActiveScriptSite), 'pScriptSite'),
        (['out'], POINTER(BREAKRESUMEACTION), 'pbra'),
        (['out'], POINTER(ERRORRESUMEACTION), 'perra'),
        (['out'], POINTER(BOOL), 'pfCallOnScriptError'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddGlobalExpressionContextProvider',
        (['in'], POINTER(IProvideExpressionContexts), 'pdsfs'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveGlobalExpressionContextProvider',
        (['in'], DWORD, 'dwCookie'),
    ),
]


IDebugApplication64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetName',
        (['in'], LPCOLESTR, 'pstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DebugOutput',
        (['in'], LPCOLESTR, 'pstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HandleBreakPoINT',
        (['in'], BREAKREASON, 'br'),
        (['out'], POINTER(BREAKRESUMEACTION), 'pbra'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBreakFlags',
        (['out'], POINTER(APPBREAKFLAGS), 'pabf'),
        (['out'], POINTER(POINTER(IRemoteDebugApplicationThread)), 'pprdatSteppingThread'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentThread',
        (['out'], POINTER(POINTER(IDebugApplicationThread)), 'pat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateAsyncDebugOperation',
        (['in'], POINTER(IDebugSyncOperation), 'psdo'),
        (['out'], POINTER(POINTER(IDebugAsyncOperation)), 'ppado'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddStackFrameSniffer',
        (['in'], POINTER(IDebugStackFrameSniffer), 'pdsfs'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveStackFrameSniffer',
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SynchronousCallInDebuggerThread',
        (['in'], POINTER(IDebugThreadCall64), 'pptc'),
        (['in'], DWORDLONG, 'dwParam1'),
        (['in'], DWORDLONG, 'dwParam2'),
        (['in'], DWORDLONG, 'dwParam3'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateApplicationNode',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'ppdanNew'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FireDebuggerEvent',
        (['in'], REFGUID, 'riid'),
        (['in'], POINTER(comtypes.IUnknown), 'punk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HandleRuntimeError',
        (['in'], POINTER(IActiveScriptErrorDebug), 'pErrorDebug'),
        (['in'], POINTER(IActiveScriptSite), 'pScriptSite'),
        (['out'], POINTER(BREAKRESUMEACTION), 'pbra'),
        (['out'], POINTER(ERRORRESUMEACTION), 'perra'),
        (['out'], POINTER(BOOL), 'pfCallOnScriptError'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddGlobalExpressionContextProvider',
        (['in'], POINTER(IProvideExpressionContexts), 'pdsfs'),
        (['out'], POINTER(DWORDLONG), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveGlobalExpressionContextProvider',
        (['in'], DWORDLONG, 'dwCookie'),
    ),
]


IRemoteDebugApplicationEvents._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnConnectDebugger',
        (['in'], POINTER(IApplicationDebugger), 'pad'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnSetName',
        (['in'], LPCOLESTR, 'pstrName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDebugOutput',
        (['in'], LPCOLESTR, 'pstr'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnEnterBreakPoINT',
        (['in'], POINTER(IRemoteDebugApplicationThread), 'prdat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnLeaveBreakPoINT',
        (['in'], POINTER(IRemoteDebugApplicationThread), 'prdat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnCreateThread',
        (['in'], POINTER(IRemoteDebugApplicationThread), 'prdat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnDestroyThread',
        (['in'], POINTER(IRemoteDebugApplicationThread), 'prdat'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OnBreakFlagChange',
        (['in'], APPBREAKFLAGS, 'abf'),
        (['in'], POINTER(IRemoteDebugApplicationThread), 'prdatSteppingThread'),
    ),
]


IDebugApplicationNode._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumChildren',
        (['out'], POINTER(POINTER(IEnumDebugApplicationNodes)), 'pperddp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetParent',
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'pprddp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDocumentProvider',
        (['in'], POINTER(IDebugDocumentProvider), 'pddp'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Attach',
        (['in'], POINTER(IDebugApplicationNode), 'pdanParent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Detach'
    ),
]


IDebugApplicationNodeEvents._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'onAddChild',
        (['in'], POINTER(IDebugApplicationNode), 'prddpChild'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onRemoveChild',
        (['in'], POINTER(IDebugApplicationNode), 'prddpChild'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'onAttach',
        (['in'], POINTER(IDebugApplicationNode), 'prddpParent'),
    ),
]


AsyncIDebugApplicationNodeEvents._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Begin_onAddChild',
        (['in'], POINTER(IDebugApplicationNode), 'prddpChild'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Begin_onRemoveChild',
        (['in'], POINTER(IDebugApplicationNode), 'prddpChild'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Begin_onAttach',
        (['in'], POINTER(IDebugApplicationNode), 'prddpParent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_onAttach'
    ),
]


IDebugThreadCall = IDebugThreadCall64
IID_IDebugThreadCall = IID_IDebugThreadCall64


IDebugThreadCall32._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ThreadCallHandler',
        (['in'], DWORD, 'dwParam1'),
        (['in'], DWORD, 'dwParam2'),
        (['in'], DWORD, 'dwParam3'),
    ),
]


IDebugThreadCall64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ThreadCallHandler',
        (['in'], DWORDLONG, 'dwParam1'),
        (['in'], DWORDLONG, 'dwParam2'),
        (['in'], DWORDLONG, 'dwParam3'),
    ),
]


THREAD_STATE = DWORD
THREAD_STATE_RUNNING = 0x00000001
THREAD_STATE_SUSPENDED = 0x00000002
THREAD_BLOCKED = 0x00000004
THREAD_OUT_OF_CONTEXT = 0x00000008


IRemoteDebugApplicationThread._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetSystemThreadId',
        (['out'], POINTER(DWORD), 'dwThreadId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetApplication',
        (['out'], POINTER(POINTER(IRemoteDebugApplication)), 'pprda'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumStackFrames',
        (['out'], POINTER(POINTER(IEnumDebugStackFrames)), 'ppedsf'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDescription',
        (['out'], POINTER(BSTR), 'pbstrDescription'),
        (['out'], POINTER(BSTR), 'pbstrState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetNextStatement',
        (['in'], POINTER(IDebugStackFrame), 'pStackFrame'),
        (['in'], POINTER(IDebugCodeContext), 'pCodeContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        (['out'], POINTER(DWORD), 'pState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Suspend',
        (['out'], POINTER(DWORD), 'pdwCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Resume',
        (['out'], POINTER(DWORD), 'pdwCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSuspendCount',
        (['out'], POINTER(DWORD), 'pdwCount'),
    ),
]


IDebugApplicationThread._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SynchronousCallIntoThread32',
        (['in'], POINTER(IDebugThreadCall32), 'pstcb'),
        (['in'], DWORD, 'dwParam1'),
        (['in'], DWORD, 'dwParam2'),
        (['in'], DWORD, 'dwParam3'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetDescription',
        (['in'], LPCOLESTR, 'pstrDescription'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetStateString',
        (['in'], LPCOLESTR, 'pstrState'),
    ),
]


IDebugApplicationThread64._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SynchronousCallIntoThread64',
        (['in'], POINTER(IDebugThreadCall64), 'pstcb'),
        (['in'], DWORDLONG, 'dwParam1'),
        (['in'], DWORDLONG, 'dwParam2'),
        (['in'], DWORDLONG, 'dwParam3'),
    ),
]


IDebugCookie._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetDebugCookie',
        (['in'], DWORD, 'dwDebugAppCookie'),
    ),
]


IEnumDebugApplicationNodes._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(POINTER(IDebugApplicationNode)), 'pprddp'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumDebugApplicationNodes)), 'pperddp'),
    ),
]


IEnumRemoteDebugApplications._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(POINTER(IRemoteDebugApplication)), 'ppda'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumRemoteDebugApplications)), 'ppessd'),
    ),
]


IEnumRemoteDebugApplicationThreads._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(POINTER(IRemoteDebugApplicationThread)), 'pprdat'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumRemoteDebugApplicationThreads)), 'pperdat'),
    ),
]


from propidl_h import VARIANT
from oaidl_h import DISPID, TYPEDESC, IDispatch


IDebugFormatter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetStringForVariant',
        (['in'], POINTER(VARIANT), 'pvar'),
        (['in'], ULONG, 'nRadix'),
        (['out'], POINTER(BSTR), 'pbstrValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetVariantForString',
        (['in'], LPCOLESTR, 'pwstrValue'),
        (['out'], POINTER(VARIANT), 'pvar'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetStringForVarType',
        (['in'], VARTYPE, 'vt'),
        (['in'], POINTER(TYPEDESC), 'ptdescArrayType'),
        (['out'], POINTER(BSTR), 'pbstr'),
    ),
]


ISimpleConnectionPoINT._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetEventCount',
        (['out'], POINTER(ULONG), 'pulCount'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DescribeEvents',
        (['in'], ULONG, 'iEvent'),
        (['in'], ULONG, 'cEvents'),
        (['out'], POINTER(DISPID), 'prgid'),
        (['out'], POINTER(BSTR), 'prgbstr'),
        (['out'], POINTER(ULONG), 'pcEventsFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Advise',
        (['in'], POINTER(IDispatch), 'pdisp'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise',
        (['in'], DWORD, 'dwCookie'),
    ),
]


IDebugHelper._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreatePropertyBrowser',
        (['in'], POINTER(VARIANT), 'pvar'),
        (['in'], LPCOLESTR, 'bstrName'),
        (['in'], POINTER(IDebugApplicationThread), 'pdat'),
        (['out'], POINTER(POINTER(IDebugProperty)), 'ppdob'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreatePropertyBrowserEx',
        (['in'], POINTER(VARIANT), 'pvar'),
        (['in'], LPCOLESTR, 'bstrName'),
        (['in'], POINTER(IDebugApplicationThread), 'pdat'),
        (['in'], POINTER(IDebugFormatter), 'pdf'),
        (['out'], POINTER(POINTER(IDebugProperty)), 'ppdob'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateSimpleConnectionPoINT',
        (['in'], POINTER(IDispatch), 'pdisp'),
        (['out'], POINTER(POINTER(ISimpleConnectionPoINT)), 'ppscp'),
    ),
]


IEnumDebugExpressionContexts._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        (['out'], POINTER(POINTER(IDebugExpressionContext)), 'ppdec'),
        (['out'], POINTER(ULONG), 'pceltFetched'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Skip',
        (['in'], ULONG, 'celt'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IEnumDebugExpressionContexts)), 'ppedec'),
    ),
]


IProvideExpressionContexts._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'EnumExpressionContexts',
        (['out'], POINTER(POINTER(IEnumDebugExpressionContexts)), 'ppedec'),
    ),
]


MachineDebugManger = MachineDebugManager_RETAIL

__all__ = (
    'IDebugAsyncOperationCallBack', 'IEnumDebugApplicationNodes',
    'IActiveScriptSiteDebug64', 'IDebugDocumentHelper32', 'IDebugHelper',
    'IProvideExpressionContexts', 'IDebugDocumentTextAuthor', 'IDebugCookie',
    'IDebugThreadCall64', 'IActiveScriptSiteDebugEx', 'IDebugApplication32',
    'ProcessDebugManagerLib', 'IDebugDocumentText', 'IEnumDebugStackFrames64',
    'IDebugDocumentHost', 'IDebugCodeContext', 'IDebugApplication64',
    'IDebugDocumentTextEvents', 'IApplicationDebuggerUI', 'IDebugFormatter',
    'ISimpleConnectionPoINT', 'IDebugApplicationThread64', 'IDebugDocument',
    'IRemoteDebugApplicationEvents', 'IEnumDebugStackFrames', 'BREAKREASON',
    'IDebugStackFrameSnifferEx64', 'IDebugApplicationThread', 'DebugHelper',
    'IDebugDocumentInfo', 'IActiveScriptDebug32', 'IDebugExpressionCallBack',
    'IEnumDebugExpressionContexts', 'IRemoteDebugApplicationThread',
    'IDebugDocumentTextExternalAuthor', 'IRemoteDebugApplication',
    'IDebugDocumentProvider', 'IDebugThreadCall32', 'IApplicationDebugger',
    'IDebugStackFrameSnifferEx32', 'IDebugSessionProvider', 'THREAD_BLOCKED',
    'IMachineDebugManagerCookie', 'IMachineDebugManager', 'IDebugStackFrame',
    'IProcessDebugManager64', 'IDebugAsyncOperation', 'IDebugApplicationNode',
    'IActiveScriptSiteDebug32', 'IEnumDebugCodeContexts', 'IDebugExpression',
    'IProcessDebugManager32', 'IDebugExpressionContext', 'IActiveScriptDebug',
    'IDebugDocumentContext', 'IDebugApplicationNodeEvents', 'tagBREAKREASON',
    'IDebugSyncOperation', 'IActiveScriptDebug64', 'IDebugStackFrameSniffer',
    'AsyncIDebugApplicationNodeEvents', 'IEnumRemoteDebugApplicationThreads',
    'IEnumRemoteDebugApplications', 'IMachineDebugManagerEvents',
    'IActiveScriptErrorDebug', 'IDebugDocumentHelper64',
    'IID_IDebugDocumentHelper', 'IID_IActiveScriptDebug', 'IDebugApplication',
    'TEXT_DOC_ATTR_TYPE_SCRIPT', 'TEXT_DOC_ATTR',
    'APPBREAKFLAG_STEPTYPE_SOURCE', 'IDebugStackFrameSnifferEx',
    'IDebugDocumentHelper', 'APPBREAKFLAG_STEPTYPE_MASK', 'IDebugThreadCall',
    'DEBUG_TEXT_NOSIDEEFFECTS', 'SOURCETEXT_ATTR_COMMENT', 'DOCUMENTNAMETYPE',
    'IID_IActiveScriptSiteDebug', 'IProcessDebugManager', 'APPBREAKFLAG_STEP',
    'IID_IProcessDebugManager', 'SOURCETEXT_ATTR_FUNCTION_START',
    'THREAD_STATE_SUSPENDED', 'SOURCETEXT_ATTR_KEYWORD', 'MachineDebugManger',
    'DEBUG_TEXT_ISEXPRESSION', 'DEBUG_TEXT_RETURNVALUE', 'BREAKRESUMEACTION',
    'DEBUG_TEXT_ALLOWBREAKPOINTS', 'IID_IDebugStackFrameSnifferEx',
    'APPBREAKFLAG_IN_BREAKPOINT', 'IID_IDebugApplication', 'BREAKPOINT_STATE',
    'DEBUG_TEXT_ISNONUSERCODE', 'SOURCETEXT_ATTR_NUMBER', 'ERRORRESUMEACTION',
    'IID_IDebugThreadCall', '__REQUIRED_RPCNDR_H_VERSION__', 'THREAD_STATE',
    'THREAD_OUT_OF_CONTEXT', 'TEXT_DOC_ATTR_TYPE_WORKER', 'SOURCE_TEXT_ATTR',
    'DEBUG_TEXT_ALLOWERRORREPORT', 'THREAD_STATE_RUNNING', 'APPBREAKFLAGS',
    'APPBREAKFLAG_STEPTYPE_BYTECODE', 'APPBREAKFLAG_NESTED',
    'TEXT_DOC_ATTR_TYPE_PRIMARY', 'APPBREAKFLAG_DEBUGGER_BLOCK',
    'APPBREAKFLAG_STEPTYPE_MACHINE', 'APPBREAKFLAG_DEBUGGER_HALT',
    'DEBUG_TEXT_EVALUATETOCODECONTEXT', 'TEXT_DOC_ATTR_READONLY',
    'IActiveScriptSiteDebug', 'SOURCETEXT_ATTR_OPERATOR',
    'SOURCETEXT_ATTR_NONSOURCE', '__REQUIRED_RPCSAL_H_VERSION__',
    'SOURCETEXT_ATTR_STRING',
    'tagERRORRESUMEACTION', 'tagBREAKPOINT_STATE', 'tagBREAKRESUME_ACTION',
    'tagDOCUMENTNAMETYPE', 'tagDebugStackFrameDescriptor64',
    'DefaultDebugSessionProvider', 'DebugStackFrameDescriptor',
    'MachineDebugManager_RETAIL', 'DebugStackFrameDescriptor64',
    'ProcessDebugManager', 'tagDebugStackFrameDescriptor',
    'CDebugDocumentHelper', 'MachineDebugManager_DEBUG',
)
