import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

COMMETHOD = comtypes.COMMETHOD

__REQUIRED_RPCNDR_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__corprof_h__ = None
__ICorProfilerCallback_FWD_DEFINED__ = None
__ICorProfilerCallback2_FWD_DEFINED__ = None
__ICorProfilerInfo_FWD_DEFINED__ = None
__ICorProfilerInfo2_FWD_DEFINED__ = None
__ICorProfilerObjectEnum_FWD_DEFINED__ = None
__IMethodMalloc_FWD_DEFINED__ = None
_COR_IL_MAP = None
_COR_DEBUG_IL_TO_NATIVE_MAP_ = None
_COR_FIELD_OFFSET_ = None
__ICorProfilerCallback_INTERFACE_DEFINED__ = None
__ICorProfilerCallback2_INTERFACE_DEFINED__ = None
__ICorProfilerInfo_INTERFACE_DEFINED__ = None
__ICorProfilerInfo2_INTERFACE_DEFINED__ = None
__ICorProfilerObjectEnum_INTERFACE_DEFINED__ = None
__IMethodMalloc_INTERFACE_DEFINED__ = None


class _COR_IL_MAP(ctypes.Structure):
    pass


COR_IL_MAP = _COR_IL_MAP


class COR_DEBUG_IL_TO_NATIVE_MAP(ctypes.Structure):
    pass


class _COR_FIELD_OFFSET(ctypes.Structure):
    pass


COR_FIELD_OFFSET = _COR_FIELD_OFFSET


class _COR_PRF_FUNCTION_ARGUMENT_RANGE(ctypes.Structure):
    pass


COR_PRF_FUNCTION_ARGUMENT_RANGE = _COR_PRF_FUNCTION_ARGUMENT_RANGE


class _COR_PRF_FUNCTION_ARGUMENT_INFO(ctypes.Structure):
    pass


COR_PRF_FUNCTION_ARGUMENT_INFO = _COR_PRF_FUNCTION_ARGUMENT_INFO


class _COR_PRF_CODE_INFO(ctypes.Structure):
    pass


COR_PRF_CODE_INFO = _COR_PRF_CODE_INFO


class COR_PRF_GC_GENERATION_RANGE(ctypes.Structure):
    pass


class COR_PRF_EX_CLAUSE_INFO(ctypes.Structure):
    pass


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 6.00.0366
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file

if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    __REQUIRED_RPCNDR_H_VERSION__ = 475
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF   __RPCNDR_H_VERSION__

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

if not defined(__corprof_h__):
    __corprof_h__ = VOID
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__ICorProfilerCallback_FWD_DEFINED__):
        __ICorProfilerCallback_FWD_DEFINED__ = VOID


        class ICorProfilerCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorProfilerCallback_FWD_DEFINED__

    if not defined(__ICorProfilerCallback2_FWD_DEFINED__):
        __ICorProfilerCallback2_FWD_DEFINED__ = VOID


        class ICorProfilerCallback2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorProfilerCallback2_FWD_DEFINED__

    if not defined(__ICorProfilerInfo_FWD_DEFINED__):
        __ICorProfilerInfo_FWD_DEFINED__ = VOID


        class ICorProfilerInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorProfilerInfo_FWD_DEFINED__

    if not defined(__ICorProfilerInfo2_FWD_DEFINED__):
        __ICorProfilerInfo2_FWD_DEFINED__ = VOID


        class ICorProfilerInfo2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorProfilerInfo2_FWD_DEFINED__

    if not defined(__ICorProfilerObjectEnum_FWD_DEFINED__):
        __ICorProfilerObjectEnum_FWD_DEFINED__ = VOID


        class ICorProfilerObjectEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorProfilerObjectEnum_FWD_DEFINED__

    if not defined(__IMethodMalloc_FWD_DEFINED__):
        __IMethodMalloc_FWD_DEFINED__ = VOID


        class IMethodMalloc(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMethodMalloc_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwn_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_corprof_0000
    # [local]
    PROFILER_REGKEY_ROOT = "software\\microsoft\\.NETFramework\\Profilers"
    PROFILER_REGVALUE_HELPSTRING = "HelpString"
    PROFILER_REGVALUE_PROFID = "ProfilerID"
    CorDB_CONTROL_Profiling = "Cor_Enable_Profiling"
    CorDB_CONTROL_ProfilingL = "Cor_Enable_Profiling"
    _ZERO_ = 0
    if _ZERO_:
        mdToken = LONG32
        mdModule = mdToken
        mdTypeDef = mdToken
        mdMethodDef = mdToken
        mdFieldDef = mdToken
        CorElementType = ULONG

    else:
        mdToken = VOID
        mdModule = mdToken
        mdTypeDef = mdToken
        mdMethodDef = mdToken
        mdFieldDef = mdToken
        CorElementType = VOID
    # END IF

    LPCBYTE = POINTER(BYTE)
    LPBYTE = POINTER(BYTE)

    if not defined(_COR_IL_MAP):
        _COR_IL_MAP = VOID

        _COR_IL_MAP._fields_ = [
            ('oldOffset', ULONG32),
            ('newOffset', ULONG32),
            ('fAccurate', BOOL),
        ]
    # END IF  _COR_IL_MAP

    if not defined(_COR_DEBUG_IL_TO_NATIVE_MAP_):
        _COR_DEBUG_IL_TO_NATIVE_MAP_ = VOID


        class CorDebugIlToNativeMappingTypes(ENUM):
            NO_MAPPING = - 1
            PROLOG = - 2
            EPILOG = - 3

        COR_DEBUG_IL_TO_NATIVE_MAP._fields_ = [
            ('ilOffset', ULONG32),
            ('nativeStartOffset', ULONG32),
            ('nativeEndOffset', ULONG32),
        ]
    # END IF   _COR_DEBUG_IL_TO_NATIVE_MAP_

    if not defined(_COR_FIELD_OFFSET_):
        _COR_FIELD_OFFSET_ = VOID

        _COR_FIELD_OFFSET._fields_ = [
            ('ridOfField', mdFieldDef),
            ('ulOffset', ULONG),
        ]
    # END IF   _COR_FIELD_OFFSET_

    ProcessID = UINT_PTR
    AssemblyID = UINT_PTR
    AppDomainID = UINT_PTR
    ModuleID = UINT_PTR
    ClassID = UINT_PTR
    ThreadID = UINT_PTR
    ContextID = UINT_PTR
    FunctionID = UINT_PTR
    ObjectID = UINT_PTR
    GCHandleID = UINT_PTR

    # typedef UINT_PTR __stdcall __stdcall FunctionIDMapper(
    # FunctionID funcId,
    # BOOL *pbHookFunction);

    class _COR_PRF_SNAPSHOT_INFO(ENUM):
        COR_PRF_SNAPSHOT_DEFAULT = 0
        COR_PRF_SNAPSHOT_REGISTER_CONTEXT = 0x1

    COR_PRF_SNAPSHOT_INFO = _COR_PRF_SNAPSHOT_INFO
    COR_PRF_FRAME_INFO = UINT_PTR

    _COR_PRF_FUNCTION_ARGUMENT_RANGE._fields_ = [
        ('startAddress', UINT_PTR),
        ('length', ULONG),
    ]

    _COR_PRF_FUNCTION_ARGUMENT_INFO._fields_ = [
        ('numRanges', ULONG),
        ('totalArgumentSize', ULONG),
        ('ranges', COR_PRF_FUNCTION_ARGUMENT_RANGE * 1),
    ]

    _COR_PRF_CODE_INFO._fields_ = [
        ('startAddress', UINT_PTR),
        ('size', SIZE_T),
    ]


    class __MIDL___MIDL_itf_corprof_0000_0001(ENUM):
        COR_PRF_FIELD_NOT_A_STATIC = 0
        COR_PRF_FIELD_APP_DOMAIN_STATIC = 0x1
        COR_PRF_FIELD_THREAD_STATIC = 0x2
        COR_PRF_FIELD_CONTEXT_STATIC = 0x4
        COR_PRF_FIELD_RVA_STATIC = 0x8

    COR_PRF_STATIC_TYPE = __MIDL___MIDL_itf_corprof_0000_0001

    # typedef VOID FunctionEnter(
    # FunctionID funcID);

    # typedef VOID FunctionLeave(
    # FunctionID funcID);

    # typedef VOID FunctionTailcall(
    # FunctionID funcID);

    # typedef VOID FunctionEnter2(
    # FunctionID funcId,
    # UINT_PTR clientData,
    # COR_PRF_FRAME_INFO func,
    # COR_PRF_FUNCTION_ARGUMENT_INFO *argumentInfo);

    # typedef VOID FunctionLeave2(
    # FunctionID funcId,
    # UINT_PTR clientData,
    # COR_PRF_FRAME_INFO func,
    # COR_PRF_FUNCTION_ARGUMENT_RANGE *retvalRange);

    # typedef VOID FunctionTailcall2(
    # FunctionID funcId,
    # UINT_PTR clientData,
    # COR_PRF_FRAME_INFO func);

    # typedef HRESULT __stdcall __stdcall StackSnapshotCallback(
    # FunctionID funcId,
    # UINT_PTR ip,
    # COR_PRF_FRAME_INFO frameInfo,
    # ULONG32 contextSize,
    # BYTE context[],
    # VOID *clientData);

    class __MIDL___MIDL_itf_corprof_0000_0002(ENUM):
        COR_PRF_MONITOR_NONE = 0
        COR_PRF_MONITOR_FUNCTION_UNLOADS = 0x1
        COR_PRF_MONITOR_CLASS_LOADS = 0x2
        COR_PRF_MONITOR_MODULE_LOADS = 0x4
        COR_PRF_MONITOR_ASSEMBLY_LOADS = 0x8
        COR_PRF_MONITOR_APPDOMAIN_LOADS = 0x10
        COR_PRF_MONITOR_JIT_COMPILATION = 0x20
        COR_PRF_MONITOR_EXCEPTIONS = 0x40
        COR_PRF_MONITOR_GC = 0x80
        COR_PRF_MONITOR_OBJECT_ALLOCATED = 0x100
        COR_PRF_MONITOR_THREADS = 0x200
        COR_PRF_MONITOR_REMOTING = 0x400
        COR_PRF_MONITOR_CODE_TRANSITIONS = 0x800
        COR_PRF_MONITOR_ENTERLEAVE = 0x1000
        COR_PRF_MONITOR_CCW = 0x2000
        COR_PRF_MONITOR_REMOTING_COOKIE = 0x4000 | COR_PRF_MONITOR_REMOTING
        COR_PRF_MONITOR_REMOTING_ASYNC = 0x8000 | COR_PRF_MONITOR_REMOTING
        COR_PRF_MONITOR_SUSPENDS = 0x10000
        COR_PRF_MONITOR_CACHE_SEARCHES = 0x20000
        COR_PRF_MONITOR_CLR_EXCEPTIONS = 0x1000000
        COR_PRF_MONITOR_ALL = 0x107FFFF
        COR_PRF_ENABLE_REJIT = 0x40000
        COR_PRF_ENABLE_INPROC_DEBUGGING = 0x80000
        COR_PRF_ENABLE_JIT_MAPS = 0x100000
        COR_PRF_DISABLE_INLINING = 0x200000
        COR_PRF_DISABLE_OPTIMIZATIONS = 0x400000
        COR_PRF_ENABLE_OBJECT_ALLOCATED = 0x800000
        COR_PRF_ENABLE_FUNCTION_ARGS = 0x2000000
        COR_PRF_ENABLE_FUNCTION_RETVAL = 0x4000000
        COR_PRF_ENABLE_FRAME_INFO = 0x8000000
        COR_PRF_ENABLE_STACK_SNAPSHOT = 0x10000000
        COR_PRF_USE_PROFILE_IMAGES = 0x20000000
        COR_PRF_ALL = 0x3FFFFFFF
        COR_PRF_MONITOR_IMMUTABLE = (
            COR_PRF_MONITOR_CODE_TRANSITIONS |
            COR_PRF_MONITOR_REMOTING |
            COR_PRF_MONITOR_REMOTING_COOKIE |
            COR_PRF_MONITOR_REMOTING_ASYNC |
            COR_PRF_MONITOR_GC |
            COR_PRF_ENABLE_REJIT |
            COR_PRF_ENABLE_INPROC_DEBUGGING |
            COR_PRF_ENABLE_JIT_MAPS |
            COR_PRF_DISABLE_OPTIMIZATIONS |
            COR_PRF_DISABLE_INLINING |
            COR_PRF_ENABLE_OBJECT_ALLOCATED |
            COR_PRF_ENABLE_FUNCTION_ARGS |
            COR_PRF_ENABLE_FUNCTION_RETVAL |
            COR_PRF_ENABLE_FRAME_INFO |
            COR_PRF_ENABLE_STACK_SNAPSHOT |
            COR_PRF_USE_PROFILE_IMAGES
        )

    COR_PRF_MONITOR = __MIDL___MIDL_itf_corprof_0000_0002


    class __MIDL___MIDL_itf_corprof_0000_0003(ENUM):
        PROFILER_PARENT_UNKNOWN = 0xFFFFFFFD
        PROFILER_GLOBAL_CLASS = 0xFFFFFFFE
        PROFILER_GLOBAL_MODULE = 0xFFFFFFFF

    COR_PRF_MISC = __MIDL___MIDL_itf_corprof_0000_0003


    class __MIDL___MIDL_itf_corprof_0000_0004(ENUM):
        COR_PRF_CACHED_FUNCTION_FOUND = 0
        COR_PRF_CACHED_FUNCTION_NOT_FOUND = COR_PRF_CACHED_FUNCTION_FOUND + 1

    COR_PRF_JIT_CACHE = __MIDL___MIDL_itf_corprof_0000_0004


    class __MIDL___MIDL_itf_corprof_0000_0005(ENUM):
        COR_PRF_TRANSITION_CALL = 0
        COR_PRF_TRANSITION_RETURN = COR_PRF_TRANSITION_CALL + 1

    COR_PRF_TRANSITION_REASON = __MIDL___MIDL_itf_corprof_0000_0005


    class __MIDL___MIDL_itf_corprof_0000_0006(ENUM):
        COR_PRF_SUSPEND_OTHER = 0
        COR_PRF_SUSPEND_FOR_GC = 1
        COR_PRF_SUSPEND_FOR_APPDOMAIN_SHUTDOWN = 2
        COR_PRF_SUSPEND_FOR_CODE_PITCHING = 3
        COR_PRF_SUSPEND_FOR_SHUTDOWN = 4
        COR_PRF_SUSPEND_FOR_INPROC_DEBUGGER = 6
        COR_PRF_SUSPEND_FOR_GC_PREP = 7

    COR_PRF_SUSPEND_REASON = __MIDL___MIDL_itf_corprof_0000_0006
    if not defined(__ICorProfilerCallback_INTERFACE_DEFINED__):
        __ICorProfilerCallback_INTERFACE_DEFINED__ = VOID

        # interface ICorProfilerCallback
        # [local][unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorProfilerCallback = MIDL_INTERFACE(
                "{176FBED1-A55C-4796-98CA-A9DA0EF883E7}"
            )
            ICorProfilerCallback._iid_ = IID_ICorProfilerCallback

            ICorProfilerCallback._methods_ = [
                COMMETHOD(
                    [helpstring('Method Initialize')],
                    HRESULT,
                    'Initialize',
                    (
                        ['in'],
                        POINTER(comtypes.IUnknown),
                        'pICorProfilerInfoUnk'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method Shutdown')],
                    HRESULT,
                    'Shutdown',
                ),
                COMMETHOD(
                    [helpstring('Method AppDomainCreationStarted')],
                    HRESULT,
                    'AppDomainCreationStarted',
                    (['in'], AppDomainID, 'appDomainId'),
                ),
                COMMETHOD(
                    [helpstring('Method AppDomainCreationFinished')],
                    HRESULT,
                    'AppDomainCreationFinished',
                    (['in'], AppDomainID, 'appDomainId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method AppDomainShutdownStarted')],
                    HRESULT,
                    'AppDomainShutdownStarted',
                    (['in'], AppDomainID, 'appDomainId'),
                ),
                COMMETHOD(
                    [helpstring('Method AppDomainShutdownFinished')],
                    HRESULT,
                    'AppDomainShutdownFinished',
                    (['in'], AppDomainID, 'appDomainId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method AssemblyLoadStarted')],
                    HRESULT,
                    'AssemblyLoadStarted',
                    (['in'], AssemblyID, 'assemblyId'),
                ),
                COMMETHOD(
                    [helpstring('Method AssemblyLoadFinished')],
                    HRESULT,
                    'AssemblyLoadFinished',
                    (['in'], AssemblyID, 'assemblyId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method AssemblyUnloadStarted')],
                    HRESULT,
                    'AssemblyUnloadStarted',
                    (['in'], AssemblyID, 'assemblyId'),
                ),
                COMMETHOD(
                    [helpstring('Method AssemblyUnloadFinished')],
                    HRESULT,
                    'AssemblyUnloadFinished',
                    (['in'], AssemblyID, 'assemblyId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method ModuleLoadStarted')],
                    HRESULT,
                    'ModuleLoadStarted',
                    (['in'], ModuleID, 'moduleId'),
                ),
                COMMETHOD(
                    [helpstring('Method ModuleLoadFinished')],
                    HRESULT,
                    'ModuleLoadFinished',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method ModuleUnloadStarted')],
                    HRESULT,
                    'ModuleUnloadStarted',
                    (['in'], ModuleID, 'moduleId'),
                ),
                COMMETHOD(
                    [helpstring('Method ModuleUnloadFinished')],
                    HRESULT,
                    'ModuleUnloadFinished',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method ModuleAttachedToAssembly')],
                    HRESULT,
                    'ModuleAttachedToAssembly',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], AssemblyID, 'AssemblyId'),
                ),
                COMMETHOD(
                    [helpstring('Method ClassLoadStarted')],
                    HRESULT,
                    'ClassLoadStarted',
                    (['in'], ClassID, 'classId'),
                ),
                COMMETHOD(
                    [helpstring('Method ClassLoadFinished')],
                    HRESULT,
                    'ClassLoadFinished',
                    (['in'], ClassID, 'classId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method ClassUnloadStarted')],
                    HRESULT,
                    'ClassUnloadStarted',
                    (['in'], ClassID, 'classId'),
                ),
                COMMETHOD(
                    [helpstring('Method ClassUnloadFinished')],
                    HRESULT,
                    'ClassUnloadFinished',
                    (['in'], ClassID, 'classId'),
                    (['in'], HRESULT, 'hrStatus'),
                ),
                COMMETHOD(
                    [helpstring('Method FunctionUnloadStarted')],
                    HRESULT,
                    'FunctionUnloadStarted',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method JITCompilationStarted')],
                    HRESULT,
                    'JITCompilationStarted',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], BOOL, 'fIsSafeToBlock'),
                ),
                COMMETHOD(
                    [helpstring('Method JITCompilationFinished')],
                    HRESULT,
                    'JITCompilationFinished',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], HRESULT, 'hrStatus'),
                    (['in'], BOOL, 'fIsSafeToBlock'),
                ),
                COMMETHOD(
                    [helpstring('Method JITCachedFunctionSearchStarted')],
                    HRESULT,
                    'JITCachedFunctionSearchStarted',
                    (['in'], FunctionID, 'functionId'),
                    (['out'], POINTER(BOOL), 'pbUseCachedFunction'),
                ),
                COMMETHOD(
                    [helpstring('Method JITCachedFunctionSearchFinished')],
                    HRESULT,
                    'JITCachedFunctionSearchFinished',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], COR_PRF_JIT_CACHE, 'result'),
                ),
                COMMETHOD(
                    [helpstring('Method JITFunctionPitched')],
                    HRESULT,
                    'JITFunctionPitched',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method JITInlining')],
                    HRESULT,
                    'JITInlining',
                    (['in'], FunctionID, 'callerId'),
                    (['in'], FunctionID, 'calleeId'),
                    (['out'], POINTER(BOOL), 'pfShouldInline'),
                ),
                COMMETHOD(
                    [helpstring('Method ThreadCreated')],
                    HRESULT,
                    'ThreadCreated',
                    (['in'], ThreadID, 'threadId'),
                ),
                COMMETHOD(
                    [helpstring('Method ThreadDestroyed')],
                    HRESULT,
                    'ThreadDestroyed',
                    (['in'], ThreadID, 'threadId'),
                ),
                COMMETHOD(
                    [helpstring('Method ThreadAssignedToOSThread')],
                    HRESULT,
                    'ThreadAssignedToOSThread',
                    (['in'], ThreadID, 'managedThreadId'),
                    (['in'], DWORD, 'osThreadId'),
                ),
                COMMETHOD(
                    [helpstring('Method RemotingClientInvocationStarted')],
                    HRESULT,
                    'RemotingClientInvocationStarted',
                ),
                COMMETHOD(
                    [helpstring('Method RemotingClientSendingMessage')],
                    HRESULT,
                    'RemotingClientSendingMessage',
                    (['in'], POINTER(GUID), 'pCookie'),
                    (['in'], BOOL, 'fIsAsync'),
                ),
                COMMETHOD(
                    [helpstring('Method RemotingClientReceivingReply')],
                    HRESULT,
                    'RemotingClientReceivingReply',
                    (['in'], POINTER(GUID), 'pCookie'),
                    (['in'], BOOL, 'fIsAsync'),
                ),
                COMMETHOD(
                    [helpstring('Method RemotingClientInvocationFinished')],
                    HRESULT,
                    'RemotingClientInvocationFinished',
                ),
                COMMETHOD(
                    [helpstring('Method RemotingServerReceivingMessage')],
                    HRESULT,
                    'RemotingServerReceivingMessage',
                    (['in'], POINTER(GUID), 'pCookie'),
                    (['in'], BOOL, 'fIsAsync'),
                ),
                COMMETHOD(
                    [helpstring('Method RemotingServerInvocationStarted')],
                    HRESULT,
                    'RemotingServerInvocationStarted',
                ),
                COMMETHOD(
                    [helpstring('Method RemotingServerInvocationReturned')],
                    HRESULT,
                    'RemotingServerInvocationReturned',
                ),
                COMMETHOD(
                    [helpstring('Method RemotingServerSendingReply')],
                    HRESULT,
                    'RemotingServerSendingReply',
                    (['in'], POINTER(GUID), 'pCookie'),
                    (['in'], BOOL, 'fIsAsync'),
                ),
                COMMETHOD(
                    [helpstring('Method UnmanagedToManagedTransition')],
                    HRESULT,
                    'UnmanagedToManagedTransition',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], COR_PRF_TRANSITION_REASON, 'reason'),
                ),
                COMMETHOD(
                    [helpstring('Method ManagedToUnmanagedTransition')],
                    HRESULT,
                    'ManagedToUnmanagedTransition',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], COR_PRF_TRANSITION_REASON, 'reason'),
                ),
                COMMETHOD(
                    [helpstring('Method RuntimeSuspendStarted')],
                    HRESULT,
                    'RuntimeSuspendStarted',
                    (['in'], COR_PRF_SUSPEND_REASON, 'suspendReason'),
                ),
                COMMETHOD(
                    [helpstring('Method RuntimeSuspendFinished')],
                    HRESULT,
                    'RuntimeSuspendFinished',
                ),
                COMMETHOD(
                    [helpstring('Method RuntimeSuspendAborted')],
                    HRESULT,
                    'RuntimeSuspendAborted',
                ),
                COMMETHOD(
                    [helpstring('Method RuntimeResumeStarted')],
                    HRESULT,
                    'RuntimeResumeStarted',
                ),
                COMMETHOD(
                    [helpstring('Method RuntimeResumeFinished')],
                    HRESULT,
                    'RuntimeResumeFinished',
                ),
                COMMETHOD(
                    [helpstring('Method RuntimeThreadSuspended')],
                    HRESULT,
                    'RuntimeThreadSuspended',
                    (['in'], ThreadID, 'threadId'),
                ),
                COMMETHOD(
                    [helpstring('Method RuntimeThreadResumed')],
                    HRESULT,
                    'RuntimeThreadResumed',
                    (['in'], ThreadID, 'threadId'),
                ),
                COMMETHOD(
                    [helpstring('Method MovedReferences')],
                    HRESULT,
                    'MovedReferences',
                    (['in'], ULONG, 'cMovedObjectIDRanges'),
                    (['in'], ObjectID * 0, 'oldObjectIDRangeStart'),
                    (['in'], ObjectID * 0, 'newObjectIDRangeStart'),
                    (['in'], ULONG * 0, 'cObjectIDRangeLength'),
                ),
                COMMETHOD(
                    [helpstring('Method ObjectAllocated')],
                    HRESULT,
                    'ObjectAllocated',
                    (['in'], ObjectID, 'objectId'),
                    (['in'], ClassID, 'classId'),
                ),
                COMMETHOD(
                    [helpstring('Method ObjectsAllocatedByClass')],
                    HRESULT,
                    'ObjectsAllocatedByClass',
                    (['in'], ULONG, 'cClassCount'),
                    (['in'], ClassID * 0, 'classIds'),
                    (['in'], ULONG * 0, 'cObjects'),
                ),
                COMMETHOD(
                    [helpstring('Method ObjectReferences')],
                    HRESULT,
                    'ObjectReferences',
                    (['in'], ObjectID, 'objectId'),
                    (['in'], ClassID, 'classId'),
                    (['in'], ULONG, 'cObjectRefs'),
                    (['in'], ObjectID * 0, 'objectRefIds'),
                ),
                COMMETHOD(
                    [helpstring('Method RootReferences')],
                    HRESULT,
                    'RootReferences',
                    (['in'], ULONG, 'cRootRefs'),
                    (['in'], ObjectID * 0, 'rootRefIds'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionThrown')],
                    HRESULT,
                    'ExceptionThrown',
                    (['in'], ObjectID, 'thrownObjectId'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionSearchFunctionEnter')],
                    HRESULT,
                    'ExceptionSearchFunctionEnter',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionSearchFunctionLeave')],
                    HRESULT,
                    'ExceptionSearchFunctionLeave',
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionSearchFilterEnter')],
                    HRESULT,
                    'ExceptionSearchFilterEnter',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionSearchFilterLeave')],
                    HRESULT,
                    'ExceptionSearchFilterLeave',
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionSearchCatcherFound')],
                    HRESULT,
                    'ExceptionSearchCatcherFound',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionOSHandlerEnter')],
                    HRESULT,
                    'ExceptionOSHandlerEnter',
                    (['in'], UINT_PTR, '__unused'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionOSHandlerLeave')],
                    HRESULT,
                    'ExceptionOSHandlerLeave',
                    (['in'], UINT_PTR, '__unused'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionUnwindFunctionEnter')],
                    HRESULT,
                    'ExceptionUnwindFunctionEnter',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionUnwindFunctionLeave')],
                    HRESULT,
                    'ExceptionUnwindFunctionLeave',
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionUnwindFinallyEnter')],
                    HRESULT,
                    'ExceptionUnwindFinallyEnter',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionUnwindFinallyLeave')],
                    HRESULT,
                    'ExceptionUnwindFinallyLeave',
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionCatcherEnter')],
                    HRESULT,
                    'ExceptionCatcherEnter',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], ObjectID, 'objectId'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionCatcherLeave')],
                    HRESULT,
                    'ExceptionCatcherLeave',
                ),
                COMMETHOD(
                    [helpstring('Method COMClassicVTableCreated')],
                    HRESULT,
                    'COMClassicVTableCreated',
                    (['in'], ClassID, 'wrappedClassId'),
                    (['in'], REFGUID, 'implementedIID'),
                    (['in'], POINTER(VOID), 'pVTable'),
                    (['in'], ULONG, 'cSlots'),
                ),
                COMMETHOD(
                    [helpstring('Method COMClassicVTableDestroyed')],
                    HRESULT,
                    'COMClassicVTableDestroyed',
                    (['in'], ClassID, 'wrappedClassId'),
                    (['in'], REFGUID, 'implementedIID'),
                    (['in'], POINTER(VOID), 'pVTable'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionCLRCatcherFound')],
                    HRESULT,
                    'ExceptionCLRCatcherFound',
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionCLRCatcherExecute')],
                    HRESULT,
                    'ExceptionCLRCatcherExecute',
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorProfilerCallback_INTERFACE_DEFINED__

    # interface __MIDL_itf_corprof_0011
    # [local]
    class __MIDL___MIDL_itf_corprof_0011_0001(ENUM):
        COR_PRF_GC_ROOT_STACK = 1
        COR_PRF_GC_ROOT_FINALIZER = 2
        COR_PRF_GC_ROOT_HANDLE = 3
        COR_PRF_GC_ROOT_OTHER = 0

    COR_PRF_GC_ROOT_KIND = __MIDL___MIDL_itf_corprof_0011_0001


    class __MIDL___MIDL_itf_corprof_0011_0002(ENUM):
        COR_PRF_GC_ROOT_PINNING = 0x1
        COR_PRF_GC_ROOT_WEAKREF = 0x2
        COR_PRF_GC_ROOT_INTERIOR = 0x4
        COR_PRF_GC_ROOT_REFCOUNTED = 0x8

    COR_PRF_GC_ROOT_FLAGS = __MIDL___MIDL_itf_corprof_0011_0002


    class __MIDL___MIDL_itf_corprof_0011_0003(ENUM):
        COR_PRF_FINALIZER_CRITICAL = 0x1

    COR_PRF_FINALIZER_FLAGS = __MIDL___MIDL_itf_corprof_0011_0003


    class __MIDL___MIDL_itf_corprof_0011_0004(ENUM):
        COR_PRF_GC_GEN_0 = 0
        COR_PRF_GC_GEN_1 = 1
        COR_PRF_GC_GEN_2 = 2
        COR_PRF_GC_LARGE_OBJECT_HEAP = 3

    COR_PRF_GC_GENERATION = __MIDL___MIDL_itf_corprof_0011_0004

    COR_PRF_GC_GENERATION_RANGE._fields_ = [
        ('generation', COR_PRF_GC_GENERATION),
        ('rangeStart', ObjectID),
        ('rangeLength', UINT_PTR),
        ('rangeLengthReserved', UINT_PTR),
    ]


    class __MIDL___MIDL_itf_corprof_0011_0005(ENUM):
        COR_PRF_CLAUSE_NONE = 0
        COR_PRF_CLAUSE_FILTER = 1
        COR_PRF_CLAUSE_CATCH = 2
        COR_PRF_CLAUSE_FINALLY = 3

    COR_PRF_CLAUSE_TYPE = __MIDL___MIDL_itf_corprof_0011_0005

    COR_PRF_EX_CLAUSE_INFO._fields_ = [
        ('clauseType', COR_PRF_CLAUSE_TYPE),
        ('programCounter', UINT_PTR),
        ('framePointer', UINT_PTR),
        ('shadowStackPointer', UINT_PTR),
    ]


    class __MIDL___MIDL_itf_corprof_0011_0006(ENUM):
        COR_PRF_GC_INDUCED = 1
        COR_PRF_GC_OTHER = 0

    COR_PRF_GC_REASON = __MIDL___MIDL_itf_corprof_0011_0006
    if not defined(__ICorProfilerCallback2_INTERFACE_DEFINED__):
        __ICorProfilerCallback2_INTERFACE_DEFINED__ = VOID

        # interface ICorProfilerCallback2
        # [local][unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorProfilerCallback2 = MIDL_INTERFACE(
                "{8A8CC829-CCF2-49FE-BBAE-0F022228071A}"
            )
            ICorProfilerCallback2._iid_ = IID_ICorProfilerCallback2

            ICorProfilerCallback2._methods_ = [
                COMMETHOD(
                    [helpstring('Method ThreadNameChanged')],
                    HRESULT,
                    'ThreadNameChanged',
                    (['in'], ThreadID, 'threadId'),
                    (['in'], ULONG, 'cchName'),
                    (['in'], WCHAR * 0, 'name'),
                ),
                COMMETHOD(
                    [helpstring('Method GarbageCollectionStarted')],
                    HRESULT,
                    'GarbageCollectionStarted',
                    (['in'], INT, 'cGenerations'),
                    (['in'], BOOL * 0, 'generationCollected'),
                    (['in'], COR_PRF_GC_REASON, 'reason'),
                ),
                COMMETHOD(
                    [helpstring('Method SurvivingReferences')],
                    HRESULT,
                    'SurvivingReferences',
                    (['in'], ULONG, 'cSurvivingObjectIDRanges'),
                    (['in'], ObjectID * 0, 'objectIDRangeStart'),
                    (['in'], ULONG * 0, 'cObjectIDRangeLength'),
                ),
                COMMETHOD(
                    [helpstring('Method GarbageCollectionFinished')],
                    HRESULT,
                    'GarbageCollectionFinished',
                ),
                COMMETHOD(
                    [helpstring('Method FinalizeableObjectQueued')],
                    HRESULT,
                    'FinalizeableObjectQueued',
                    (['in'], DWORD, 'finalizerFlags'),
                    (['in'], ObjectID, 'objectID'),
                ),
                COMMETHOD(
                    [helpstring('Method RootReferences2')],
                    HRESULT,
                    'RootReferences2',
                    (['in'], ULONG, 'cRootRefs'),
                    (['in'], ObjectID * 0, 'rootRefIds'),
                    (['in'], COR_PRF_GC_ROOT_KIND * 0, 'rootKinds'),
                    (['in'], COR_PRF_GC_ROOT_FLAGS * 0, 'rootFlags'),
                    (['in'], UINT_PTR * 0, 'rootIds'),
                ),
                COMMETHOD(
                    [helpstring('Method HandleCreated')],
                    HRESULT,
                    'HandleCreated',
                    (['in'], GCHandleID, 'handleId'),
                    (['in'], ObjectID, 'initialObjectId'),
                ),
                COMMETHOD(
                    [helpstring('Method HandleDestroyed')],
                    HRESULT,
                    'HandleDestroyed',
                    (['in'], GCHandleID, 'handleId'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorProfilerCallback2_INTERFACE_DEFINED__

    if not defined(__ICorProfilerInfo_INTERFACE_DEFINED__):
        __ICorProfilerInfo_INTERFACE_DEFINED__ = VOID

        # interface ICorProfilerInfo
        # [local][unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorProfilerInfo = MIDL_INTERFACE(
                "{28B5557D-3F3F-48B4-90B2-5F9EEA2F6C48}"
            )
            ICorProfilerInfo._iid_ = IID_ICorProfilerInfo

            ICorProfilerInfo._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetClassFromObject')],
                    HRESULT,
                    'GetClassFromObject',
                    (['in'], ObjectID, 'objectId'),
                    (['out'], POINTER(ClassID), 'pClassId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetClassFromToken')],
                    HRESULT,
                    'GetClassFromToken',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], mdTypeDef, 'typeDef'),
                    (['out'], POINTER(ClassID), 'pClassId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCodeInfo')],
                    HRESULT,
                    'GetCodeInfo',
                    (['in'], FunctionID, 'functionId'),
                    (['out'], POINTER(LPCBYTE), 'pStart'),
                    (['out'], POINTER(ULONG), 'pcSize'),
                ),
                COMMETHOD(
                    [helpstring('Method GetEventMask')],
                    HRESULT,
                    'GetEventMask',
                    (['out'], POINTER(DWORD), 'pdwEvents'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionFromIP')],
                    HRESULT,
                    'GetFunctionFromIP',
                    (['in'], LPCBYTE, 'ip'),
                    (['out'], POINTER(FunctionID), 'pFunctionId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionFromToken')],
                    HRESULT,
                    'GetFunctionFromToken',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], mdToken, 'token'),
                    (['out'], POINTER(FunctionID), 'pFunctionId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetHandleFromThread')],
                    HRESULT,
                    'GetHandleFromThread',
                    (['in'], ThreadID, 'threadId'),
                    (['out'], POINTER(HANDLE), 'phThread'),
                ),
                COMMETHOD(
                    [helpstring('Method GetObjectSize')],
                    HRESULT,
                    'GetObjectSize',
                    (['in'], ObjectID, 'objectId'),
                    (['out'], POINTER(ULONG), 'pcSize'),
                ),
                COMMETHOD(
                    [helpstring('Method IsArrayClass')],
                    HRESULT,
                    'IsArrayClass',
                    (['in'], ClassID, 'classId'),
                    (['out'], POINTER(CorElementType), 'pBaseElemType'),
                    (['out'], POINTER(ClassID), 'pBaseClassId'),
                    (['out'], POINTER(ULONG), 'pcRank'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThreadInfo')],
                    HRESULT,
                    'GetThreadInfo',
                    (['in'], ThreadID, 'threadId'),
                    (['out'], POINTER(DWORD), 'pdwWin32ThreadId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCurrentThreadID')],
                    HRESULT,
                    'GetCurrentThreadID',
                    (['out'], POINTER(ThreadID), 'pThreadId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetClassIDInfo')],
                    HRESULT,
                    'GetClassIDInfo',
                    (['in'], ClassID, 'classId'),
                    (['out'], POINTER(ModuleID), 'pModuleId'),
                    (['out'], POINTER(mdTypeDef), 'pTypeDefToken'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionInfo')],
                    HRESULT,
                    'GetFunctionInfo',
                    (['in'], FunctionID, 'functionId'),
                    (['out'], POINTER(ClassID), 'pClassId'),
                    (['out'], POINTER(ModuleID), 'pModuleId'),
                    (['out'], POINTER(mdToken), 'pToken'),
                ),
                COMMETHOD(
                    [helpstring('Method SetEventMask')],
                    HRESULT,
                    'SetEventMask',
                    (['in'], DWORD, 'dwEvents'),
                ),
                COMMETHOD(
                    [helpstring('Method SetEnterLeaveFunctionHooks')],
                    HRESULT,
                    'SetEnterLeaveFunctionHooks',
                    (['in'], POINTER(FunctionEnter), 'pFuncEnter'),
                    (['in'], POINTER(FunctionLeave), 'pFuncLeave'),
                    (['in'], POINTER(FunctionTailcall), 'pFuncTailcall'),
                ),
                COMMETHOD(
                    [helpstring('Method SetFunctionIDMapper')],
                    HRESULT,
                    'SetFunctionIDMapper',
                    (['in'], POINTER(FunctionIDMapper), 'pFunc'),
                ),
                COMMETHOD(
                    [helpstring('Method GetTokenAndMetaDataFromFunction')],
                    HRESULT,
                    'GetTokenAndMetaDataFromFunction',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], REFIID, 'riid'),
                    (
                        ['out'],
                        POINTER(POINTER(comtypes.IUnknown)),
                        'ppImport'
                    ),
                    (['out'], POINTER(mdToken), 'pToken'),
                ),
                COMMETHOD(
                    [helpstring('Method GetModuleInfo')],
                    HRESULT,
                    'GetModuleInfo',
                    (['in'], ModuleID, 'moduleId'),
                    (['out'], POINTER(LPCBYTE), 'ppBaseLoadAddress'),
                    (['in'], ULONG, 'cchName'),
                    (['out'], POINTER(ULONG), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                    (['out'], POINTER(AssemblyID), 'pAssemblyId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetModuleMetaData')],
                    HRESULT,
                    'GetModuleMetaData',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], DWORD, 'dwOpenFlags'),
                    (['in'], REFIID, 'riid'),
                    (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppOut'),
                ),
                COMMETHOD(
                    [helpstring('Method GetILFunctionBody')],
                    HRESULT,
                    'GetILFunctionBody',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], mdMethodDef, 'methodId'),
                    (['out'], POINTER(LPCBYTE), 'ppMethodHeader'),
                    (['out'], POINTER(ULONG), 'pcbMethodSize'),
                ),
                COMMETHOD(
                    [helpstring('Method GetILFunctionBodyAllocator')],
                    HRESULT,
                    'GetILFunctionBodyAllocator',
                    (['in'], ModuleID, 'moduleId'),
                    (['out'], POINTER(POINTER(IMethodMalloc)), 'ppMalloc'),
                ),
                COMMETHOD(
                    [helpstring('Method SetILFunctionBody')],
                    HRESULT,
                    'SetILFunctionBody',
                    (['in'], ModuleID, 'moduleId'),
                    (['in'], mdMethodDef, 'methodid'),
                    (['in'], LPCBYTE, 'pbNewILMethodHeader'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAppDomainInfo')],
                    HRESULT,
                    'GetAppDomainInfo',
                    (['in'], AppDomainID, 'appDomainId'),
                    (['in'], ULONG, 'cchName'),
                    (['out'], POINTER(ULONG), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                    (['out'], POINTER(ProcessID), 'pProcessId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAssemblyInfo')],
                    HRESULT,
                    'GetAssemblyInfo',
                    (['in'], AssemblyID, 'assemblyId'),
                    (['in'], ULONG, 'cchName'),
                    (['out'], POINTER(ULONG), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                    (['out'], POINTER(AppDomainID), 'pAppDomainId'),
                    (['out'], POINTER(ModuleID), 'pModuleId'),
                ),
                COMMETHOD(
                    [helpstring('Method SetFunctionReJIT')],
                    HRESULT,
                    'SetFunctionReJIT',
                    (['in'], FunctionID, 'functionId'),
                ),
                COMMETHOD(
                    [helpstring('Method ForceGC')],
                    HRESULT,
                    'ForceGC',
                ),
                COMMETHOD(
                    [helpstring('Method SetILInstrumentedCodeMap')],
                    HRESULT,
                    'SetILInstrumentedCodeMap',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], BOOL, 'fStartJit'),
                    (['in'], ULONG, 'cILMapEntries'),
                    (['in'], COR_IL_MAP * 0, 'rgILMapEntries'),
                ),
                COMMETHOD(
                    [helpstring('Method GetInprocInspectionInterface')],
                    HRESULT,
                    'GetInprocInspectionInterface',
                    (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppicd'),
                ),
                COMMETHOD(
                    [helpstring('Method GetInprocInspectionIThisThread')],
                    HRESULT,
                    'GetInprocInspectionIThisThread',
                    (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppicd'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThreadContext')],
                    HRESULT,
                    'GetThreadContext',
                    (['in'], ThreadID, 'threadId'),
                    (['out'], POINTER(ContextID), 'pContextId'),
                ),
                COMMETHOD(
                    [helpstring('Method BeginInprocDebugging')],
                    HRESULT,
                    'BeginInprocDebugging',
                    (['in'], BOOL, 'fThisThreadOnly'),
                    (['out'], POINTER(DWORD), 'pdwProfilerContext'),
                ),
                COMMETHOD(
                    [helpstring('Method EndInprocDebugging')],
                    HRESULT,
                    'EndInprocDebugging',
                    (['in'], DWORD, 'dwProfilerContext'),
                ),
                COMMETHOD(
                    [helpstring('Method GetILToNativeMapping')],
                    HRESULT,
                    'GetILToNativeMapping',
                    (['in'], FunctionID, 'functionId'),
                    (['in'], ULONG32, 'cMap'),
                    (['out'], POINTER(ULONG32), 'pcMap'),
                    (['out'], COR_DEBUG_IL_TO_NATIVE_MAP * 0, 'map'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorProfilerInfo_INTERFACE_DEFINED__

    if not defined(__ICorProfilerInfo2_INTERFACE_DEFINED__):
        __ICorProfilerInfo2_INTERFACE_DEFINED__ = VOID

        # interface ICorProfilerInfo2
        # [local][unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorProfilerInfo2 = MIDL_INTERFACE(
                "{CC0935CD-A518-487D-B0BB-A93214E65478}"
            )
            ICorProfilerInfo2._iid_ = IID_ICorProfilerInfo2

            ICorProfilerInfo2._methods_ = [
                COMMETHOD(
                    [helpstring('Method DoStackSnapshot')],
                    HRESULT,
                    'DoStackSnapshot',
                    (['in'], ThreadID, 'thread'),
                    (['in'], POINTER(StackSnapshotCallback), 'callback'),
                    (['in'], ULONG32, 'infoFlags'),
                    (['in'], POINTER(VOID), 'clientData'),
                    (['in'], BYTE * 0, 'context'),
                    (['in'], ULONG32, 'contextSize'),
                ),
                COMMETHOD(
                    [helpstring('Method SetEnterLeaveFunctionHooks2')],
                    HRESULT,
                    'SetEnterLeaveFunctionHooks2',
                    (['in'], POINTER(FunctionEnter2), 'pFuncEnter'),
                    (['in'], POINTER(FunctionLeave2), 'pFuncLeave'),
                    (['in'], POINTER(FunctionTailcall2), 'pFuncTailcall'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionInfo2')],
                    HRESULT,
                    'GetFunctionInfo2',
                    (['in'], FunctionID, 'funcId'),
                    (['in'], COR_PRF_FRAME_INFO, 'frameInfo'),
                    (['out'], POINTER(ClassID), 'pClassId'),
                    (['out'], POINTER(ModuleID), 'pModuleId'),
                    (['out'], POINTER(mdToken), 'pToken'),
                    (['in'], ULONG32, 'cTypeArgs'),
                    (['out'], POINTER(ULONG32), 'pcTypeArgs'),
                    (['out'], ClassID * 0, 'typeArgs'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStringLayout')],
                    HRESULT,
                    'GetStringLayout',
                    (['out'], POINTER(ULONG), 'pBufferLengthOffset'),
                    (['out'], POINTER(ULONG), 'pStringLengthOffset'),
                    (['out'], POINTER(ULONG), 'pBufferOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method GetClassLayout')],
                    HRESULT,
                    'GetClassLayout',
                    (['in'], ClassID, 'classID'),
                    (['out', 'in'], COR_FIELD_OFFSET * 0, 'rFieldOffset'),
                    (['in'], ULONG, 'cFieldOffset'),
                    (['out'], POINTER(ULONG), 'pcFieldOffset'),
                    (['out'], POINTER(ULONG), 'pulClassSize'),
                ),
                COMMETHOD(
                    [helpstring('Method GetClassIDInfo2')],
                    HRESULT,
                    'GetClassIDInfo2',
                    (['in'], ClassID, 'classId'),
                    (['out'], POINTER(ModuleID), 'pModuleId'),
                    (['out'], POINTER(mdTypeDef), 'pTypeDefToken'),
                    (['out'], POINTER(ClassID), 'pParentClassId'),
                    (['in'], ULONG32, 'cNumTypeArgs'),
                    (['out'], POINTER(ULONG32), 'pcNumTypeArgs'),
                    (['out'], ClassID * 0, 'typeArgs'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCodeInfo2')],
                    HRESULT,
                    'GetCodeInfo2',
                    (['in'], FunctionID, 'functionID'),
                    (['in'], ULONG32, 'cCodeInfos'),
                    (['out'], POINTER(ULONG32), 'pcCodeInfos'),
                    (['out'], COR_PRF_CODE_INFO * 0, 'codeInfos'),
                ),
                COMMETHOD(
                    [helpstring('Method GetClassFromTokenAndTypeArgs')],
                    HRESULT,
                    'GetClassFromTokenAndTypeArgs',
                    (['in'], ModuleID, 'moduleID'),
                    (['in'], mdTypeDef, 'typeDef'),
                    (['in'], ULONG32, 'cTypeArgs'),
                    (['in'], ClassID * 0, 'typeArgs'),
                    (['out'], POINTER(ClassID), 'pClassID'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionFromTokenAndTypeArgs')],
                    HRESULT,
                    'GetFunctionFromTokenAndTypeArgs',
                    (['in'], ModuleID, 'moduleID'),
                    (['in'], mdMethodDef, 'funcDef'),
                    (['in'], ClassID, 'classId'),
                    (['in'], ULONG32, 'cTypeArgs'),
                    (['in'], ClassID * 0, 'typeArgs'),
                    (['out'], POINTER(FunctionID), 'pFunctionID'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumModuleFrozenObjects')],
                    HRESULT,
                    'EnumModuleFrozenObjects',
                    (['in'], ModuleID, 'moduleID'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorProfilerObjectEnum)),
                        'ppEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetArrayObjectInfo')],
                    HRESULT,
                    'GetArrayObjectInfo',
                    (['in'], ObjectID, 'objectId'),
                    (['in'], ULONG32, 'cDimensions'),
                    (['out'], ULONG32 * 0, 'pDimensionSizes'),
                    (['out'], INT * 0, 'pDimensionLowerBounds'),
                    (['out'], POINTER(POINTER(BYTE)), 'ppData'),
                ),
                COMMETHOD(
                    [helpstring('Method GetBoxClassLayout')],
                    HRESULT,
                    'GetBoxClassLayout',
                    (['in'], ClassID, 'classId'),
                    (['out'], POINTER(ULONG32), 'pBufferOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThreadAppDomain')],
                    HRESULT,
                    'GetThreadAppDomain',
                    (['in'], ThreadID, 'threadId'),
                    (['out'], POINTER(AppDomainID), 'pAppDomainId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRVAStaticAddress')],
                    HRESULT,
                    'GetRVAStaticAddress',
                    (['in'], ClassID, 'classId'),
                    (['in'], mdFieldDef, 'fieldToken'),
                    (['out'], POINTER(POINTER(VOID)), 'ppAddress'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAppDomainStaticAddress')],
                    HRESULT,
                    'GetAppDomainStaticAddress',
                    (['in'], ClassID, 'classId'),
                    (['in'], mdFieldDef, 'fieldToken'),
                    (['in'], AppDomainID, 'appDomainId'),
                    (['out'], POINTER(POINTER(VOID)), 'ppAddress'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThreadStaticAddress')],
                    HRESULT,
                    'GetThreadStaticAddress',
                    (['in'], ClassID, 'classId'),
                    (['in'], mdFieldDef, 'fieldToken'),
                    (['in'], ThreadID, 'threadId'),
                    (['out'], POINTER(POINTER(VOID)), 'ppAddress'),
                ),
                COMMETHOD(
                    [helpstring('Method GetContextStaticAddress')],
                    HRESULT,
                    'GetContextStaticAddress',
                    (['in'], ClassID, 'classId'),
                    (['in'], mdFieldDef, 'fieldToken'),
                    (['in'], ContextID, 'contextId'),
                    (['out'], POINTER(POINTER(VOID)), 'ppAddress'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStaticFieldInfo')],
                    HRESULT,
                    'GetStaticFieldInfo',
                    (['in'], ClassID, 'classId'),
                    (['in'], mdFieldDef, 'fieldToken'),
                    (['out'], POINTER(COR_PRF_STATIC_TYPE), 'pFieldInfo'),
                ),
                COMMETHOD(
                    [helpstring('Method GetGenerationBounds')],
                    HRESULT,
                    'GetGenerationBounds',
                    (['in'], ULONG, 'cObjectRanges'),
                    (['out'], POINTER(ULONG), 'pcObjectRanges'),
                    (['out'], COR_PRF_GC_GENERATION_RANGE * 0, 'ranges'),
                ),
                COMMETHOD(
                    [helpstring('Method GetObjectGeneration')],
                    HRESULT,
                    'GetObjectGeneration',
                    (['in'], ObjectID, 'objectId'),
                    (['out'], POINTER(COR_PRF_GC_GENERATION_RANGE), 'range'),
                ),
                COMMETHOD(
                    [helpstring('Method GetNotifiedExceptionClauseInfo')],
                    HRESULT,
                    'GetNotifiedExceptionClauseInfo',
                    (['out'], POINTER(COR_PRF_EX_CLAUSE_INFO), 'pinfo'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorProfilerInfo2_INTERFACE_DEFINED__

    if not defined(__ICorProfilerObjectEnum_INTERFACE_DEFINED__):
        __ICorProfilerObjectEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorProfilerObjectEnum
        # [local][unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorProfilerObjectEnum = MIDL_INTERFACE(
                "{2C6269BD-2D13-4321-AE12-6686365FD6AF}"
            )
            ICorProfilerObjectEnum._iid_ = IID_ICorProfilerObjectEnum

            ICorProfilerObjectEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Skip')],
                    HRESULT,
                    'Skip',
                    (['in'], ULONG, 'celt'),
                ),
                COMMETHOD(
                    [helpstring('Method Reset')],
                    HRESULT,
                    'Reset',
                ),
                COMMETHOD(
                    [helpstring('Method Clone')],
                    HRESULT,
                    'Clone',
                    (
                        ['out'],
                        POINTER(POINTER(ICorProfilerObjectEnum)),
                        'ppEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetCount')],
                    HRESULT,
                    'GetCount',
                    (['out'], POINTER(ULONG), 'pcelt'),
                ),
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], ObjectID * 0, 'objects'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorProfilerObjectEnum_INTERFACE_DEFINED__

    if not defined(__IMethodMalloc_INTERFACE_DEFINED__):
        __IMethodMalloc_INTERFACE_DEFINED__ = VOID

        # interface IMethodMalloc
        # [local][unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_IMethodMalloc = MIDL_INTERFACE(
                "{A0EFB28B-6EE2-4D7B-B983-A75EF7BEEDB8}"
            )
            IMethodMalloc._iid_ = IID_IMethodMalloc

            IMethodMalloc._methods_ = [
                COMMETHOD(
                    [helpstring('Method Alloc')],
                    PVOID,
                    'Alloc',
                    (['in'], ULONG, 'cb'),
                ),
            ]

        # END IF  C style interface
    # END IF  __IMethodMalloc_INTERFACE_DEFINED__

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF
# END IF


