

from wtypes_h import (
    ENUM,
    UINT,
    POINTER,
    HRESULT,
    BOOL,
    DWORD_PTR,
    BSTR,
    DWORD,
    HANDLE,
    INT,
    HANDLE_PTR,
    VARIANT_BOOL,
    REFCLSID,
    REFIID,
)
from guiddef_h import (
    IID,
)
import ctypes
import ntdef_h
import comtypes
from activdbg_h import * # NOQA
from activscp_h import * # NOQA

from winapifamily_h import * # NOQA

__REQUIRED_RPCNDR_H_VERSION__ = 0x000001F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x00000064
# from rpc_h import * # NOQA
# from rpcndr_h import * # NOQA
# from windows_h import * # NOQA
# from ole2_h import * # NOQA
IID_IDebugApplicationNode100 = IID(
    '{90a7734e-841b-4f77-9384-a2891e76e7e2}'
)


class IDebugApplicationNode100(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationNode100
    _idlflags_ = []


IID_IWebAppDiagnosticsSetup = IID(
    '{379BFBE1-C6C9-432A-93E1-6D17656C538C}'
)


class IWebAppDiagnosticsSetup(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWebAppDiagnosticsSetup
    _idlflags_ = []


IID_IRemoteDebugApplication110 = IID(
    '{D5FE005B-2836-485e-B1F9-89D91AA24FD4}'
)


class IRemoteDebugApplication110(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRemoteDebugApplication110
    _idlflags_ = []


IID_IDebugApplication11032 = IID(
    '{BDB3B5DE-89F2-4E11-84A5-97445F941C7D}'
)


class IDebugApplication11032(IRemoteDebugApplication110):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplication11032
    _idlflags_ = []


IID_IDebugApplication11064 = IID(
    '{2039D958-4EEB-496A-87BB-2E5201EADEEF}'
)


class IDebugApplication11064(IRemoteDebugApplication110):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplication11064
    _idlflags_ = []


IID_IWebAppDiagnosticsObjectInitialization = IID(
    '{16FF3A42-A5F5-432B-B625-8E8E16F57E15}'
)


class IWebAppDiagnosticsObjectInitialization(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWebAppDiagnosticsObjectInitialization
    _idlflags_ = []


IID_IActiveScriptWinRTErrorDebug = IID(
    '{73A3F82A-0FE9-4B33-BA3B-FE095F697E0A}'
)


class IActiveScriptWinRTErrorDebug(IActiveScriptError):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptWinRTErrorDebug
    _idlflags_ = []


IID_IActiveScriptErrorDebug110 = IID(
    '{516E42B6-89A8-4530-937B-5F0708431442}'
)


class IActiveScriptErrorDebug110(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActiveScriptErrorDebug110
    _idlflags_ = []


IID_IDebugApplicationThreadEvents110 = IID(
    '{84E5E468-D5DA-48A8-83F4-40366429007B}'
)


class IDebugApplicationThreadEvents110(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationThreadEvents110
    _idlflags_ = []


IID_IDebugApplicationThread11032 = IID(
    '{2194AC5C-6561-404A-A2E9-F57D72DE3702}'
)


class IDebugApplicationThread11032(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationThread11032
    _idlflags_ = []


IID_IDebugApplicationThread11064 = IID(
    '{420AA4CC-EFD8-4DAC-983B-47127826917D}'
)


class IDebugApplicationThread11064(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDebugApplicationThread11064
    _idlflags_ = []


IID_IRemoteDebugCriticalErrorEvent110 = IID(
    '{2f69c611-6b14-47e8-9260-4bb7c52f504b}'
)


class IRemoteDebugCriticalErrorEvent110(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRemoteDebugCriticalErrorEvent110
    _idlflags_ = []


IID_IScriptInvocationContext = IID(
    '{5D7741B7-AF7E-4A2A-85E5-C77F4D0659FB}'
)


class IScriptInvocationContext(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IScriptInvocationContext
    _idlflags_ = []


IID_IDebugStackFrame110 = IID(
    '{4B509611-B6EA-4B24-ADCB-D0CCFD1A7E33}'
)


class IDebugStackFrame110(IDebugStackFrame):
    _case_insensitive_ = True
    _iid_ = IID_IDebugStackFrame110
    _idlflags_ = []


IID_IRemoteDebugInfoEvent110 = IID(
    '{9FF56BB6-EB89-4C0F-8823-CC2A4C0B7F26}'
)


class IRemoteDebugInfoEvent110(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRemoteDebugInfoEvent110
    _idlflags_ = []


class tagAPPLICATION_NODE_EVENT_FILTER(ENUM):
    FILTER_EXCLUDE_NOTHING = 0
    FILTER_EXCLUDE_ANONYMOUS_CODE = 0x1
    FILTER_EXCLUDE_EVAL_CODE = 0x2


APPLICATION_NODE_EVENT_FILTER = tagAPPLICATION_NODE_EVENT_FILTER



class tagTEXT_DOCUMENT_ARRAY(ctypes.Structure):
    _fields_ = [
        ('dwCount', DWORD),
        ('Members', POINTER(POINTER(IDebugDocumentText))),
    ]


TEXT_DOCUMENT_ARRAY = tagTEXT_DOCUMENT_ARRAY


COMMETHOD = comtypes.COMMETHOD


IDebugApplicationNode100._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetFilterForEventSink',
        ([], DWORD, 'dwCookie'),
        ([], APPLICATION_NODE_EVENT_FILTER, 'filter'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetExcludedDocuments',
        ([], APPLICATION_NODE_EVENT_FILTER, 'filter'),
        ([], POINTER(TEXT_DOCUMENT_ARRAY), 'pDocuments'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryIsChildNode',
        ([], POINTER(IDebugDocument), 'pSearchKey'),
    ),
]


IWebAppDiagnosticsSetup._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DiagnosticsSupported',
        ([], POINTER(VARIANT_BOOL), 'pRetVal'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateObjectWithSiteAtWebApp',
        ([], REFCLSID, 'rclsid'),
        ([], DWORD, 'dwClsContext'),
        ([], REFIID, 'riid'),
        ([], DWORD_PTR, 'hPassToObject'),
    ),
]


class SCRIPT_DEBUGGER_OPTIONS(ENUM):
    SDO_NONE = 0
    SDO_ENABLE_FIRST_CHANCE_EXCEPTIONS = 0x1
    SDO_ENABLE_WEB_WORKER_SUPPORT = 0x2
    SDO_ENABLE_NONUSER_CODE_SUPPORT = 0x4
    SDO_ENABLE_LIBRARY_STACK_FRAME = 0x8


IRemoteDebugApplication110._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetDebuggerOptions',
        ([], SCRIPT_DEBUGGER_OPTIONS, 'mask'),
        ([], SCRIPT_DEBUGGER_OPTIONS, 'value'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentDebuggerOptions',
        ([], POINTER(SCRIPT_DEBUGGER_OPTIONS), 'pCurrentOptions'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetMainThread',
        ([], POINTER(POINTER(IRemoteDebugApplicationThread)), 'ppThread'),
    ),
]


IDebugApplication110 = IDebugApplication11064
IID_IDebugApplication110 = IID_IDebugApplication11064

IDebugApplication11032._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SynchronousCallInMainThread',
        ([], POINTER(IDebugThreadCall32), 'pptc'),
        ([], DWORD_PTR, 'dwParam1'),
        ([], DWORD_PTR, 'dwParam2'),
        ([], DWORD_PTR, 'dwParam3'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AsynchronousCallInMainThread',
        ([], POINTER(IDebugThreadCall32), 'pptc'),
        ([], DWORD_PTR, 'dwParam1'),
        ([], DWORD_PTR, 'dwParam2'),
        ([], DWORD_PTR, 'dwParam3'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CallableWaitForHandles',
        ([], DWORD, 'handleCount'),
        ([], POINTER(HANDLE), 'pHandles'),
        ([], POINTER(DWORD), 'pIndex'),
    ),
]


IDebugApplication11064._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SynchronousCallInMainThread',
        ([], POINTER(IDebugThreadCall64), 'pptc'),
        ([], DWORD_PTR, 'dwParam1'),
        ([], DWORD_PTR, 'dwParam2'),
        ([], DWORD_PTR, 'dwParam3'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AsynchronousCallInMainThread',
        ([], POINTER(IDebugThreadCall64), 'pptc'),
        ([], DWORD_PTR, 'dwParam1'),
        ([], DWORD_PTR, 'dwParam2'),
        ([], DWORD_PTR, 'dwParam3'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CallableWaitForHandles',
        ([], DWORD, 'handleCount'),
        ([], POINTER(HANDLE), 'pHandles'),
        ([], POINTER(DWORD), 'pIndex'),
    ),
]


IWebAppDiagnosticsObjectInitialization._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Initialize',
        ([], HANDLE_PTR, 'hPassedHandle'),
        ([], POINTER(comtypes.IUnknown), 'pDebugApplication'),
    ),
]


IActiveScriptWinRTErrorDebug._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetRestrictedErrorString',
        ([], POINTER(BSTR), 'errorString'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRestrictedErrorReference',
        ([], POINTER(BSTR), 'referenceString'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCapabilitySid',
        ([], POINTER(BSTR), 'capabilitySid'),
    ),
]


class tagSCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND(ENUM):
    ETK_FIRST_CHANCE = 0
    ETK_USER_UNHANDLED = 0x1
    ETK_UNHANDLED = 0x2


SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND = tagSCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND


IActiveScriptErrorDebug110._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetExceptionThrownKind',
        ([], POINTER(SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND), 'pExceptionKind'),
    ),
]


IDebugApplicationThreadEvents110._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnBeginThreadRequest'
    ),
]


IDebugApplicationThread110 = IDebugApplicationThread11064
IID_IDebugApplicationThread110 = IID_IDebugApplicationThread11064

IDebugApplicationThread11032._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetActiveThreadRequestCount',
        ([], POINTER(UINT), 'puiThreadRequests'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsSuspendedForBreakPoINT',
        ([], POINTER(BOOL), 'pfIsSuspended'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsThreadCallable',
        ([], POINTER(BOOL), 'pfIsCallable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AsynchronousCallIntoThread',
        ([], POINTER(IDebugThreadCall32), 'pptc'),
        ([], DWORD_PTR, 'dwParam1'),
        ([], DWORD_PTR, 'dwParam2'),
        ([], DWORD_PTR, 'dwParam3'),
    ),
]


IDebugApplicationThread11064._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetActiveThreadRequestCount',
        ([], POINTER(UINT), 'puiThreadRequests'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsSuspendedForBreakPoINT',
        ([], POINTER(BOOL), 'pfIsSuspended'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsThreadCallable',
        ([], POINTER(BOOL), 'pfIsCallable'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AsynchronousCallIntoThread',
        ([], POINTER(IDebugThreadCall64), 'pptc'),
        ([], DWORD_PTR, 'dwParam1'),
        ([], DWORD_PTR, 'dwParam2'),
        ([], DWORD_PTR, 'dwParam3'),
    ),
]


IRemoteDebugCriticalErrorEvent110._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetErrorInfo',
        ([], POINTER(BSTR), 'pbstrSource'),
        ([], POINTER(INT), 'pMessageId'),
        ([], POINTER(BSTR), 'pbstrMessage'),
        ([], POINTER(POINTER(IDebugDocumentContext)), 'ppLocation'),
    ),
]


class tagSCRIPT_INVOCATION_CONTEXT_TYPE(ENUM):
    SICT_Event = 0
    SICT_SetTimeout = SICT_Event + 1
    SICT_SetInterval = SICT_SetTimeout + 1
    SICT_SetImmediate = SICT_SetInterval + 1
    SICT_RequestAnimationFrame = SICT_SetImmediate + 1
    SICT_ToString = SICT_RequestAnimationFrame + 1
    SICT_MutationObserverCheckpoINT = SICT_ToString + 1
    SICT_WWAExecUnsafeLocalFunction = SICT_MutationObserverCheckpoINT + 1
    SICT_WWAExecAtPriority = SICT_WWAExecUnsafeLocalFunction + 1


SCRIPT_INVOCATION_CONTEXT_TYPE = tagSCRIPT_INVOCATION_CONTEXT_TYPE


IScriptInvocationContext._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetContextType',
        ([], POINTER(SCRIPT_INVOCATION_CONTEXT_TYPE), 'pInvocationContextType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetContextDescription',
        ([], POINTER(BSTR), 'pDescription'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetContextObject',
        ([], POINTER(POINTER(comtypes.IUnknown)), 'ppContextObject'),
    ),
]


class tagDEBUG_STACKFRAME_TYPE(ENUM):
    DST_SCRIPT_FRAME = 0
    DST_INTERNAL_FRAME = DST_SCRIPT_FRAME + 1
    DST_INVOCATION_FRAME = DST_INTERNAL_FRAME + 1


DEBUG_STACKFRAME_TYPE = tagDEBUG_STACKFRAME_TYPE


IDebugStackFrame110._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetStackFrameType',
        ([], POINTER(DEBUG_STACKFRAME_TYPE), 'pStackFrameKind'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetScriptInvocationContext',
        ([], POINTER(POINTER(IScriptInvocationContext)), 'ppInvocationContext'),
    ),
]


class tagDEBUG_EVENT_INFO_TYPE(ENUM):
    DEIT_GENERAL = 0
    DEIT_ASMJS_IN_DEBUGGING = DEIT_GENERAL + 1
    DEIT_ASMJS_SUCCEEDED = DEIT_ASMJS_IN_DEBUGGING + 1
    DEIT_ASMJS_FAILED = DEIT_ASMJS_SUCCEEDED + 1


DEBUG_EVENT_INFO_TYPE = tagDEBUG_EVENT_INFO_TYPE


IRemoteDebugInfoEvent110._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetEventInfo',
        ([], POINTER(DEBUG_EVENT_INFO_TYPE), 'pMessageType'),
        ([], POINTER(BSTR), 'pbstrMessage'),
        ([], POINTER(BSTR), 'pbstrUrl'),
        ([], POINTER(POINTER(IDebugDocumentContext)), 'ppLocation'),
    ),
]



__all__ = (
    'IDebugApplicationThreadEvents110', 'IRemoteDebugCriticalErrorEvent110',
    'IDebugStackFrame110', 'IScriptInvocationContext', 'IDebugApplication110',
    'IActiveScriptErrorDebug110', 'IWebAppDiagnosticsObjectInitialization',
    'IWebAppDiagnosticsSetup', 'IDebugApplicationNode100', '',
    'IRemoteDebugApplication110', 'IDebugApplicationThread11064',
    'IRemoteDebugInfoEvent110', 'IDebugApplication11032',
    'IDebugApplicationThread11032', 'IDebugApplication11064',
    'IActiveScriptWinRTErrorDebug', '__REQUIRED_RPCNDR_H_VERSION__',
    'IDebugApplicationThread110', 'IID_IDebugApplicationThread110',
    'IID_IDebugApplication110', '__REQUIRED_RPCSAL_H_VERSION__',
    'tagSCRIPT_INVOCATION_CONTEXT_TYPE', 'DEBUG_EVENT_INFO_TYPE',
    'tagDEBUG_STACKFRAME_TYPE', 'tagSCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND',
    'SCRIPT_INVOCATION_CONTEXT_TYPE', 'APPLICATION_NODE_EVENT_FILTER',
    'SCRIPT_DEBUGGER_OPTIONS', 'DEBUG_STACKFRAME_TYPE', 'TEXT_DOCUMENT_ARRAY',
    'tagAPPLICATION_NODE_EVENT_FILTER', 'tagDEBUG_EVENT_INFO_TYPE',
    'SCRIPT_ERROR_DEBUG_EXCEPTION_THROWN_KIND', 'tagTEXT_DOCUMENT_ARRAY',
)
