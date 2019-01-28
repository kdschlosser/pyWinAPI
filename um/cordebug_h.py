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
__cordebug_h__ = None
__ICorDebugManagedCallback_FWD_DEFINED__ = None
__ICorDebugManagedCallback2_FWD_DEFINED__ = None
__ICorDebugUnmanagedCallback_FWD_DEFINED__ = None
__ICorDebug_FWD_DEFINED__ = None
__ICorDebug2_FWD_DEFINED__ = None
__ICorDebugController_FWD_DEFINED__ = None
__ICorDebugAppDomain_FWD_DEFINED__ = None
__ICorDebugAppDomain2_FWD_DEFINED__ = None
__ICorDebugAssembly_FWD_DEFINED__ = None
__ICorDebugAssembly2_FWD_DEFINED__ = None
__ICorDebugProcess_FWD_DEFINED__ = None
__ICorDebugProcess2_FWD_DEFINED__ = None
__ICorDebugBreakpoint_FWD_DEFINED__ = None
__ICorDebugFunctionBreakpoint_FWD_DEFINED__ = None
__ICorDebugModuleBreakpoint_FWD_DEFINED__ = None
__ICorDebugValueBreakpoint_FWD_DEFINED__ = None
__ICorDebugStepper_FWD_DEFINED__ = None
__ICorDebugStepper2_FWD_DEFINED__ = None
__ICorDebugRegisterSet_FWD_DEFINED__ = None
__ICorDebugRegisterSet2_FWD_DEFINED__ = None
__ICorDebugThread_FWD_DEFINED__ = None
__ICorDebugThread2_FWD_DEFINED__ = None
__ICorDebugChain_FWD_DEFINED__ = None
__ICorDebugFrame_FWD_DEFINED__ = None
__ICorDebugInternalFrame_FWD_DEFINED__ = None
__ICorDebugILFrame_FWD_DEFINED__ = None
__ICorDebugILFrame2_FWD_DEFINED__ = None
__ICorDebugNativeFrame_FWD_DEFINED__ = None
__ICorDebugModule_FWD_DEFINED__ = None
__ICorDebugModule2_FWD_DEFINED__ = None
__ICorDebugFunction_FWD_DEFINED__ = None
__ICorDebugFunction2_FWD_DEFINED__ = None
__ICorDebugCode_FWD_DEFINED__ = None
__ICorDebugCode2_FWD_DEFINED__ = None
__ICorDebugClass_FWD_DEFINED__ = None
__ICorDebugClass2_FWD_DEFINED__ = None
__ICorDebugEval_FWD_DEFINED__ = None
__ICorDebugEval2_FWD_DEFINED__ = None
__ICorDebugValue_FWD_DEFINED__ = None
__ICorDebugValue2_FWD_DEFINED__ = None
__ICorDebugGenericValue_FWD_DEFINED__ = None
__ICorDebugReferenceValue_FWD_DEFINED__ = None
__ICorDebugHeapValue_FWD_DEFINED__ = None
__ICorDebugHeapValue2_FWD_DEFINED__ = None
__ICorDebugObjectValue_FWD_DEFINED__ = None
__ICorDebugObjectValue2_FWD_DEFINED__ = None
__ICorDebugBoxValue_FWD_DEFINED__ = None
__ICorDebugStringValue_FWD_DEFINED__ = None
__ICorDebugArrayValue_FWD_DEFINED__ = None
__ICorDebugHandleValue_FWD_DEFINED__ = None
__ICorDebugContext_FWD_DEFINED__ = None
__ICorDebugEnum_FWD_DEFINED__ = None
__ICorDebugObjectEnum_FWD_DEFINED__ = None
__ICorDebugBreakpointEnum_FWD_DEFINED__ = None
__ICorDebugStepperEnum_FWD_DEFINED__ = None
__ICorDebugProcessEnum_FWD_DEFINED__ = None
__ICorDebugThreadEnum_FWD_DEFINED__ = None
__ICorDebugFrameEnum_FWD_DEFINED__ = None
__ICorDebugChainEnum_FWD_DEFINED__ = None
__ICorDebugModuleEnum_FWD_DEFINED__ = None
__ICorDebugValueEnum_FWD_DEFINED__ = None
__ICorDebugCodeEnum_FWD_DEFINED__ = None
__ICorDebugTypeEnum_FWD_DEFINED__ = None
__ICorDebugType_FWD_DEFINED__ = None
__ICorDebugErrorInfoEnum_FWD_DEFINED__ = None
__ICorDebugAppDomainEnum_FWD_DEFINED__ = None
__ICorDebugAssemblyEnum_FWD_DEFINED__ = None
__ICorDebugMDA_FWD_DEFINED__ = None
__ICorDebugEditAndContinueErrorInfo_FWD_DEFINED__ = None
__ICorDebugEditAndContinueSnapshot_FWD_DEFINED__ = None
__CorDebug_FWD_DEFINED__ = None
__EmbeddedCLRCorDebug_FWD_DEFINED__ = None
_COR_IL_MAP = None
_COR_DEBUG_IL_TO_NATIVE_MAP_ = None
__ICorDebugManagedCallback_INTERFACE_DEFINED__ = None
__ICorDebugManagedCallback2_INTERFACE_DEFINED__ = None
__ICorDebugUnmanagedCallback_INTERFACE_DEFINED__ = None
__ICorDebug_INTERFACE_DEFINED__ = None
__ICorDebug2_INTERFACE_DEFINED__ = None
__ICorDebugController_INTERFACE_DEFINED__ = None
__ICorDebugAppDomain_INTERFACE_DEFINED__ = None
__ICorDebugAppDomain2_INTERFACE_DEFINED__ = None
__ICorDebugAssembly_INTERFACE_DEFINED__ = None
__ICorDebugAssembly2_INTERFACE_DEFINED__ = None
__ICorDebugProcess_INTERFACE_DEFINED__ = None
__ICorDebugProcess2_INTERFACE_DEFINED__ = None
__ICorDebugBreakpoint_INTERFACE_DEFINED__ = None
__ICorDebugFunctionBreakpoint_INTERFACE_DEFINED__ = None
__ICorDebugModuleBreakpoint_INTERFACE_DEFINED__ = None
__ICorDebugValueBreakpoint_INTERFACE_DEFINED__ = None
__ICorDebugStepper_INTERFACE_DEFINED__ = None
__ICorDebugStepper2_INTERFACE_DEFINED__ = None
__ICorDebugRegisterSet_INTERFACE_DEFINED__ = None
__ICorDebugRegisterSet2_INTERFACE_DEFINED__ = None
__ICorDebugThread_INTERFACE_DEFINED__ = None
__ICorDebugThread2_INTERFACE_DEFINED__ = None
__ICorDebugChain_INTERFACE_DEFINED__ = None
__ICorDebugFrame_INTERFACE_DEFINED__ = None
__ICorDebugInternalFrame_INTERFACE_DEFINED__ = None
__ICorDebugILFrame_INTERFACE_DEFINED__ = None
__ICorDebugILFrame2_INTERFACE_DEFINED__ = None
__ICorDebugNativeFrame_INTERFACE_DEFINED__ = None
__ICorDebugModule_INTERFACE_DEFINED__ = None
__ICorDebugModule2_INTERFACE_DEFINED__ = None
__ICorDebugFunction_INTERFACE_DEFINED__ = None
__ICorDebugFunction2_INTERFACE_DEFINED__ = None
__ICorDebugCode_INTERFACE_DEFINED__ = None
__ICorDebugCode2_INTERFACE_DEFINED__ = None
__ICorDebugClass_INTERFACE_DEFINED__ = None
__ICorDebugClass2_INTERFACE_DEFINED__ = None
__ICorDebugEval_INTERFACE_DEFINED__ = None
__ICorDebugEval2_INTERFACE_DEFINED__ = None
__ICorDebugValue_INTERFACE_DEFINED__ = None
__ICorDebugValue2_INTERFACE_DEFINED__ = None
__ICorDebugGenericValue_INTERFACE_DEFINED__ = None
__ICorDebugReferenceValue_INTERFACE_DEFINED__ = None
__ICorDebugHeapValue_INTERFACE_DEFINED__ = None
__ICorDebugHeapValue2_INTERFACE_DEFINED__ = None
__ICorDebugObjectValue_INTERFACE_DEFINED__ = None
__ICorDebugObjectValue2_INTERFACE_DEFINED__ = None
__ICorDebugBoxValue_INTERFACE_DEFINED__ = None
__ICorDebugStringValue_INTERFACE_DEFINED__ = None
__ICorDebugArrayValue_INTERFACE_DEFINED__ = None
__ICorDebugHandleValue_INTERFACE_DEFINED__ = None
__ICorDebugContext_INTERFACE_DEFINED__ = None
__ICorDebugEnum_INTERFACE_DEFINED__ = None
__ICorDebugObjectEnum_INTERFACE_DEFINED__ = None
__ICorDebugBreakpointEnum_INTERFACE_DEFINED__ = None
__ICorDebugStepperEnum_INTERFACE_DEFINED__ = None
__ICorDebugProcessEnum_INTERFACE_DEFINED__ = None
__ICorDebugThreadEnum_INTERFACE_DEFINED__ = None
__ICorDebugFrameEnum_INTERFACE_DEFINED__ = None
__ICorDebugChainEnum_INTERFACE_DEFINED__ = None
__ICorDebugModuleEnum_INTERFACE_DEFINED__ = None
__ICorDebugValueEnum_INTERFACE_DEFINED__ = None
__ICorDebugCodeEnum_INTERFACE_DEFINED__ = None
__ICorDebugTypeEnum_INTERFACE_DEFINED__ = None
__ICorDebugType_INTERFACE_DEFINED__ = None
__ICorDebugErrorInfoEnum_INTERFACE_DEFINED__ = None
__ICorDebugAppDomainEnum_INTERFACE_DEFINED__ = None
__ICorDebugAssemblyEnum_INTERFACE_DEFINED__ = None
__ICorDebugMDA_INTERFACE_DEFINED__ = None
__ICorDebugEditAndContinueErrorInfo_INTERFACE_DEFINED__ = None
__ICorDebugEditAndContinueSnapshot_INTERFACE_DEFINED__ = None
__CORDBLib_LIBRARY_DEFINED__ = None


class _COR_IL_MAP(ctypes.Structure):
    pass


COR_IL_MAP = _COR_IL_MAP


class COR_DEBUG_IL_TO_NATIVE_MAP(ctypes.Structure):
    pass


class _COR_VERSION(ctypes.Structure):
    pass


COR_VERSION = _COR_VERSION


class COR_DEBUG_STEP_RANGE(ctypes.Structure):
    pass


class _COR_ACTIVE_FUNCTION(ctypes.Structure):
    pass


COR_ACTIVE_FUNCTION = _COR_ACTIVE_FUNCTION


class _CodeChunkInfo(ctypes.Structure):
    pass


CodeChunkInfo = _CodeChunkInfo


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

if not defined(__cordebug_h__):
    __cordebug_h__ = VOID
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__ICorDebugManagedCallback_FWD_DEFINED__):
        __ICorDebugManagedCallback_FWD_DEFINED__ = VOID

        class ICorDebugManagedCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugManagedCallback_FWD_DEFINED__

    if not defined(__ICorDebugManagedCallback2_FWD_DEFINED__):
        __ICorDebugManagedCallback2_FWD_DEFINED__ = VOID


        class ICorDebugManagedCallback2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugManagedCallback2_FWD_DEFINED__

    if not defined(__ICorDebugUnmanagedCallback_FWD_DEFINED__):
        __ICorDebugUnmanagedCallback_FWD_DEFINED__ = VOID


        class ICorDebugUnmanagedCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugUnmanagedCallback_FWD_DEFINED__

    if not defined(__ICorDebug_FWD_DEFINED__):
        __ICorDebug_FWD_DEFINED__ = VOID


        class ICorDebug(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebug_FWD_DEFINED__

    if not defined(__ICorDebug2_FWD_DEFINED__):
        __ICorDebug2_FWD_DEFINED__ = VOID


        class ICorDebug2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebug2_FWD_DEFINED__

    if not defined(__ICorDebugController_FWD_DEFINED__):
        __ICorDebugController_FWD_DEFINED__ = VOID


        class ICorDebugController(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugController_FWD_DEFINED__

    if not defined(__ICorDebugAppDomain_FWD_DEFINED__):
        __ICorDebugAppDomain_FWD_DEFINED__ = VOID


        class ICorDebugAppDomain(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAppDomain_FWD_DEFINED__

    if not defined(__ICorDebugAppDomain2_FWD_DEFINED__):
        __ICorDebugAppDomain2_FWD_DEFINED__ = VOID


        class ICorDebugAppDomain2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAppDomain2_FWD_DEFINED__

    if not defined(__ICorDebugAssembly_FWD_DEFINED__):
        __ICorDebugAssembly_FWD_DEFINED__ = VOID


        class ICorDebugAssembly(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAssembly_FWD_DEFINED__

    if not defined(__ICorDebugAssembly2_FWD_DEFINED__):
        __ICorDebugAssembly2_FWD_DEFINED__ = VOID


        class ICorDebugAssembly2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAssembly2_FWD_DEFINED__

    if not defined(__ICorDebugProcess_FWD_DEFINED__):
        __ICorDebugProcess_FWD_DEFINED__ = VOID


        class ICorDebugProcess(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugProcess_FWD_DEFINED__

    if not defined(__ICorDebugProcess2_FWD_DEFINED__):
        __ICorDebugProcess2_FWD_DEFINED__ = VOID


        class ICorDebugProcess2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugProcess2_FWD_DEFINED__

    if not defined(__ICorDebugBreakpoint_FWD_DEFINED__):
        __ICorDebugBreakpoint_FWD_DEFINED__ = VOID


        class ICorDebugBreakpoint(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugBreakpoint_FWD_DEFINED__

    if not defined(__ICorDebugFunctionBreakpoint_FWD_DEFINED__):
        __ICorDebugFunctionBreakpoint_FWD_DEFINED__ = VOID


        class ICorDebugFunctionBreakpoint(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugFunctionBreakpoint_FWD_DEFINED__

    if not defined(__ICorDebugModuleBreakpoint_FWD_DEFINED__):
        __ICorDebugModuleBreakpoint_FWD_DEFINED__ = VOID


        class ICorDebugModuleBreakpoint(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugModuleBreakpoint_FWD_DEFINED__

    if not defined(__ICorDebugValueBreakpoint_FWD_DEFINED__):
        __ICorDebugValueBreakpoint_FWD_DEFINED__ = VOID


        class ICorDebugValueBreakpoint(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugValueBreakpoint_FWD_DEFINED__

    if not defined(__ICorDebugStepper_FWD_DEFINED__):
        __ICorDebugStepper_FWD_DEFINED__ = VOID


        class ICorDebugStepper(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugStepper_FWD_DEFINED__

    if not defined(__ICorDebugStepper2_FWD_DEFINED__):
        __ICorDebugStepper2_FWD_DEFINED__ = VOID


        class ICorDebugStepper2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugStepper2_FWD_DEFINED__

    if not defined(__ICorDebugRegisterSet_FWD_DEFINED__):
        __ICorDebugRegisterSet_FWD_DEFINED__ = VOID


        class ICorDebugRegisterSet(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugRegisterSet_FWD_DEFINED__

    if not defined(__ICorDebugRegisterSet2_FWD_DEFINED__):
        __ICorDebugRegisterSet2_FWD_DEFINED__ = VOID


        class ICorDebugRegisterSet2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugRegisterSet2_FWD_DEFINED__

    if not defined(__ICorDebugThread_FWD_DEFINED__):
        __ICorDebugThread_FWD_DEFINED__ = VOID


        class ICorDebugThread(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugThread_FWD_DEFINED__

    if not defined(__ICorDebugThread2_FWD_DEFINED__):
        __ICorDebugThread2_FWD_DEFINED__ = VOID


        class ICorDebugThread2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugThread2_FWD_DEFINED__

    if not defined(__ICorDebugChain_FWD_DEFINED__):
        __ICorDebugChain_FWD_DEFINED__ = VOID


        class ICorDebugChain(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugChain_FWD_DEFINED__

    if not defined(__ICorDebugFrame_FWD_DEFINED__):
        __ICorDebugFrame_FWD_DEFINED__ = VOID


        class ICorDebugFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugFrame_FWD_DEFINED__

    if not defined(__ICorDebugInternalFrame_FWD_DEFINED__):
        __ICorDebugInternalFrame_FWD_DEFINED__ = VOID


        class ICorDebugInternalFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugInternalFrame_FWD_DEFINED__

    if not defined(__ICorDebugILFrame_FWD_DEFINED__):
        __ICorDebugILFrame_FWD_DEFINED__ = VOID


        class ICorDebugILFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugILFrame_FWD_DEFINED__

    if not defined(__ICorDebugILFrame2_FWD_DEFINED__):
        __ICorDebugILFrame2_FWD_DEFINED__ = VOID


        class ICorDebugILFrame2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugILFrame2_FWD_DEFINED__

    if not defined(__ICorDebugNativeFrame_FWD_DEFINED__):
        __ICorDebugNativeFrame_FWD_DEFINED__ = VOID


        class ICorDebugNativeFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugNativeFrame_FWD_DEFINED__

    if not defined(__ICorDebugModule_FWD_DEFINED__):
        __ICorDebugModule_FWD_DEFINED__ = VOID


        class ICorDebugModule(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugModule_FWD_DEFINED__

    if not defined(__ICorDebugModule2_FWD_DEFINED__):
        __ICorDebugModule2_FWD_DEFINED__ = VOID


        class ICorDebugModule2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugModule2_FWD_DEFINED__

    if not defined(__ICorDebugFunction_FWD_DEFINED__):
        __ICorDebugFunction_FWD_DEFINED__ = VOID


        class ICorDebugFunction(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugFunction_FWD_DEFINED__

    if not defined(__ICorDebugFunction2_FWD_DEFINED__):
        __ICorDebugFunction2_FWD_DEFINED__ = VOID


        class ICorDebugFunction2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugFunction2_FWD_DEFINED__

    if not defined(__ICorDebugCode_FWD_DEFINED__):
        __ICorDebugCode_FWD_DEFINED__ = VOID


        class ICorDebugCode(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugCode_FWD_DEFINED__

    if not defined(__ICorDebugCode2_FWD_DEFINED__):
        __ICorDebugCode2_FWD_DEFINED__ = VOID


        class ICorDebugCode2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugCode2_FWD_DEFINED__

    if not defined(__ICorDebugClass_FWD_DEFINED__):
        __ICorDebugClass_FWD_DEFINED__ = VOID


        class ICorDebugClass(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugClass_FWD_DEFINED__

    if not defined(__ICorDebugClass2_FWD_DEFINED__):
        __ICorDebugClass2_FWD_DEFINED__ = VOID


        class ICorDebugClass2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugClass2_FWD_DEFINED__

    if not defined(__ICorDebugEval_FWD_DEFINED__):
        __ICorDebugEval_FWD_DEFINED__ = VOID


        class ICorDebugEval(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugEval_FWD_DEFINED__

    if not defined(__ICorDebugEval2_FWD_DEFINED__):
        __ICorDebugEval2_FWD_DEFINED__ = VOID


        class ICorDebugEval2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugEval2_FWD_DEFINED__

    if not defined(__ICorDebugValue_FWD_DEFINED__):
        __ICorDebugValue_FWD_DEFINED__ = VOID


        class ICorDebugValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugValue_FWD_DEFINED__

    if not defined(__ICorDebugValue2_FWD_DEFINED__):
        __ICorDebugValue2_FWD_DEFINED__ = VOID


        class ICorDebugValue2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugValue2_FWD_DEFINED__

    if not defined(__ICorDebugGenericValue_FWD_DEFINED__):
        __ICorDebugGenericValue_FWD_DEFINED__ = VOID


        class ICorDebugGenericValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugGenericValue_FWD_DEFINED__

    if not defined(__ICorDebugReferenceValue_FWD_DEFINED__):
        __ICorDebugReferenceValue_FWD_DEFINED__ = VOID


        class ICorDebugReferenceValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugReferenceValue_FWD_DEFINED__

    if not defined(__ICorDebugHeapValue_FWD_DEFINED__):
        __ICorDebugHeapValue_FWD_DEFINED__ = VOID


        class ICorDebugHeapValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugHeapValue_FWD_DEFINED__

    if not defined(__ICorDebugHeapValue2_FWD_DEFINED__):
        __ICorDebugHeapValue2_FWD_DEFINED__ = VOID


        class ICorDebugHeapValue2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugHeapValue2_FWD_DEFINED__

    if not defined(__ICorDebugObjectValue_FWD_DEFINED__):
        __ICorDebugObjectValue_FWD_DEFINED__ = VOID


        class ICorDebugObjectValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugObjectValue_FWD_DEFINED__

    if not defined(__ICorDebugObjectValue2_FWD_DEFINED__):
        __ICorDebugObjectValue2_FWD_DEFINED__ = VOID


        class ICorDebugObjectValue2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugObjectValue2_FWD_DEFINED__

    if not defined(__ICorDebugBoxValue_FWD_DEFINED__):
        __ICorDebugBoxValue_FWD_DEFINED__ = VOID


        class ICorDebugBoxValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugBoxValue_FWD_DEFINED__

    if not defined(__ICorDebugStringValue_FWD_DEFINED__):
        __ICorDebugStringValue_FWD_DEFINED__ = VOID


        class ICorDebugStringValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugStringValue_FWD_DEFINED__

    if not defined(__ICorDebugArrayValue_FWD_DEFINED__):
        __ICorDebugArrayValue_FWD_DEFINED__ = VOID


        class ICorDebugArrayValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugArrayValue_FWD_DEFINED__

    if not defined(__ICorDebugHandleValue_FWD_DEFINED__):
        __ICorDebugHandleValue_FWD_DEFINED__ = VOID


        class ICorDebugHandleValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugHandleValue_FWD_DEFINED__

    if not defined(__ICorDebugContext_FWD_DEFINED__):
        __ICorDebugContext_FWD_DEFINED__ = VOID


        class ICorDebugContext(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugContext_FWD_DEFINED__

    if not defined(__ICorDebugEnum_FWD_DEFINED__):
        __ICorDebugEnum_FWD_DEFINED__ = VOID


        class ICorDebugEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugEnum_FWD_DEFINED__

    if not defined(__ICorDebugObjectEnum_FWD_DEFINED__):
        __ICorDebugObjectEnum_FWD_DEFINED__ = VOID


        class ICorDebugObjectEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugObjectEnum_FWD_DEFINED__

    if not defined(__ICorDebugBreakpointEnum_FWD_DEFINED__):
        __ICorDebugBreakpointEnum_FWD_DEFINED__ = VOID


        class ICorDebugBreakpointEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugBreakpointEnum_FWD_DEFINED__

    if not defined(__ICorDebugStepperEnum_FWD_DEFINED__):
        __ICorDebugStepperEnum_FWD_DEFINED__ = VOID


        class ICorDebugStepperEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugStepperEnum_FWD_DEFINED__

    if not defined(__ICorDebugProcessEnum_FWD_DEFINED__):
        __ICorDebugProcessEnum_FWD_DEFINED__ = VOID


        class ICorDebugProcessEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugProcessEnum_FWD_DEFINED__

    if not defined(__ICorDebugThreadEnum_FWD_DEFINED__):
        __ICorDebugThreadEnum_FWD_DEFINED__ = VOID


        class ICorDebugThreadEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugThreadEnum_FWD_DEFINED__

    if not defined(__ICorDebugFrameEnum_FWD_DEFINED__):
        __ICorDebugFrameEnum_FWD_DEFINED__ = VOID


        class ICorDebugFrameEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugFrameEnum_FWD_DEFINED__

    if not defined(__ICorDebugChainEnum_FWD_DEFINED__):
        __ICorDebugChainEnum_FWD_DEFINED__ = VOID


        class ICorDebugChainEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugChainEnum_FWD_DEFINED__

    if not defined(__ICorDebugModuleEnum_FWD_DEFINED__):
        __ICorDebugModuleEnum_FWD_DEFINED__ = VOID


        class ICorDebugModuleEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugModuleEnum_FWD_DEFINED__

    if not defined(__ICorDebugValueEnum_FWD_DEFINED__):
        __ICorDebugValueEnum_FWD_DEFINED__ = VOID


        class ICorDebugValueEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugValueEnum_FWD_DEFINED__

    if not defined(__ICorDebugCodeEnum_FWD_DEFINED__):
        __ICorDebugCodeEnum_FWD_DEFINED__ = VOID


        class ICorDebugCodeEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugCodeEnum_FWD_DEFINED__

    if not defined(__ICorDebugTypeEnum_FWD_DEFINED__):
        __ICorDebugTypeEnum_FWD_DEFINED__ = VOID


        class ICorDebugTypeEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugTypeEnum_FWD_DEFINED__

    if not defined(__ICorDebugType_FWD_DEFINED__):
        __ICorDebugType_FWD_DEFINED__ = VOID


        class ICorDebugType(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugType_FWD_DEFINED__

    if not defined(__ICorDebugErrorInfoEnum_FWD_DEFINED__):
        __ICorDebugErrorInfoEnum_FWD_DEFINED__ = VOID


        class ICorDebugErrorInfoEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugErrorInfoEnum_FWD_DEFINED__

    if not defined(__ICorDebugAppDomainEnum_FWD_DEFINED__):
        __ICorDebugAppDomainEnum_FWD_DEFINED__ = VOID


        class ICorDebugAppDomainEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAppDomainEnum_FWD_DEFINED__

    if not defined(__ICorDebugAssemblyEnum_FWD_DEFINED__):
        __ICorDebugAssemblyEnum_FWD_DEFINED__ = VOID


        class ICorDebugAssemblyEnum(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAssemblyEnum_FWD_DEFINED__

    if not defined(__ICorDebugMDA_FWD_DEFINED__):
        __ICorDebugMDA_FWD_DEFINED__ = VOID


        class ICorDebugMDA(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugMDA_FWD_DEFINED__

    if not defined(__ICorDebugEditAndContinueErrorInfo_FWD_DEFINED__):
        __ICorDebugEditAndContinueErrorInfo_FWD_DEFINED__ = VOID


        class ICorDebugEditAndContinueErrorInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugEditAndContinueErrorInfo_FWD_DEFINED__

    if not defined(__ICorDebugEditAndContinueSnapshot_FWD_DEFINED__):
        __ICorDebugEditAndContinueSnapshot_FWD_DEFINED__ = VOID


        class ICorDebugEditAndContinueSnapshot(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugEditAndContinueSnapshot_FWD_DEFINED__

    if not defined(__CorDebug_FWD_DEFINED__):
        __CorDebug_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class CorDebug(object):
                pass
        # END IF  __cplusplus
    # END IF  __CorDebug_FWD_DEFINED__

    if not defined(__EmbeddedCLRCorDebug_FWD_DEFINED__):
        __EmbeddedCLRCorDebug_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class EmbeddedCLRCorDebug(object):
                pass
        # END IF  __cplusplus
    # END IF  __EmbeddedCLRCorDebug_FWD_DEFINED__

    if not defined(__ICorDebugValue_FWD_DEFINED__):
        __ICorDebugValue_FWD_DEFINED__ = VOID


        class ICorDebugValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugValue_FWD_DEFINED__

    if not defined(__ICorDebugReferenceValue_FWD_DEFINED__):
        __ICorDebugReferenceValue_FWD_DEFINED__ = VOID


        class ICorDebugReferenceValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugReferenceValue_FWD_DEFINED__

    if not defined(__ICorDebugHeapValue_FWD_DEFINED__):
        __ICorDebugHeapValue_FWD_DEFINED__ = VOID


        class ICorDebugHeapValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugHeapValue_FWD_DEFINED__

    if not defined(__ICorDebugStringValue_FWD_DEFINED__):
        __ICorDebugStringValue_FWD_DEFINED__ = VOID


        class ICorDebugStringValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugStringValue_FWD_DEFINED__

    if not defined(__ICorDebugGenericValue_FWD_DEFINED__):
        __ICorDebugGenericValue_FWD_DEFINED__ = VOID


        class ICorDebugGenericValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugGenericValue_FWD_DEFINED__

    if not defined(__ICorDebugBoxValue_FWD_DEFINED__):
        __ICorDebugBoxValue_FWD_DEFINED__ = VOID


        class ICorDebugBoxValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugBoxValue_FWD_DEFINED__

    if not defined(__ICorDebugArrayValue_FWD_DEFINED__):
        __ICorDebugArrayValue_FWD_DEFINED__ = VOID


        class ICorDebugArrayValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugArrayValue_FWD_DEFINED__

    if not defined(__ICorDebugFrame_FWD_DEFINED__):
        __ICorDebugFrame_FWD_DEFINED__ = VOID


        class ICorDebugFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugFrame_FWD_DEFINED__

    if not defined(__ICorDebugILFrame_FWD_DEFINED__):
        __ICorDebugILFrame_FWD_DEFINED__ = VOID


        class ICorDebugILFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugILFrame_FWD_DEFINED__

    if not defined(__ICorDebugInternalFrame_FWD_DEFINED__):
        __ICorDebugInternalFrame_FWD_DEFINED__ = VOID


        class ICorDebugInternalFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugInternalFrame_FWD_DEFINED__

    if not defined(__ICorDebugNativeFrame_FWD_DEFINED__):
        __ICorDebugNativeFrame_FWD_DEFINED__ = VOID


        class ICorDebugNativeFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugNativeFrame_FWD_DEFINED__

    if not defined(__ICorDebugManagedCallback2_FWD_DEFINED__):
        __ICorDebugManagedCallback2_FWD_DEFINED__ = VOID


        class ICorDebugManagedCallback2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugManagedCallback2_FWD_DEFINED__

    if not defined(__ICorDebugAppDomain2_FWD_DEFINED__):
        __ICorDebugAppDomain2_FWD_DEFINED__ = VOID


        class ICorDebugAppDomain2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAppDomain2_FWD_DEFINED__

    if not defined(__ICorDebugAssembly2_FWD_DEFINED__):
        __ICorDebugAssembly2_FWD_DEFINED__ = VOID


        class ICorDebugAssembly2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugAssembly2_FWD_DEFINED__

    if not defined(__ICorDebugProcess2_FWD_DEFINED__):
        __ICorDebugProcess2_FWD_DEFINED__ = VOID


        class ICorDebugProcess2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugProcess2_FWD_DEFINED__

    if not defined(__ICorDebugStepper2_FWD_DEFINED__):
        __ICorDebugStepper2_FWD_DEFINED__ = VOID


        class ICorDebugStepper2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugStepper2_FWD_DEFINED__

    if not defined(__ICorDebugThread2_FWD_DEFINED__):
        __ICorDebugThread2_FWD_DEFINED__ = VOID


        class ICorDebugThread2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugThread2_FWD_DEFINED__

    if not defined(__ICorDebugILFrame2_FWD_DEFINED__):
        __ICorDebugILFrame2_FWD_DEFINED__ = VOID


        class ICorDebugILFrame2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugILFrame2_FWD_DEFINED__

    if not defined(__ICorDebugModule2_FWD_DEFINED__):
        __ICorDebugModule2_FWD_DEFINED__ = VOID


        class ICorDebugModule2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugModule2_FWD_DEFINED__

    if not defined(__ICorDebugFunction2_FWD_DEFINED__):
        __ICorDebugFunction2_FWD_DEFINED__ = VOID


        class ICorDebugFunction2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugFunction2_FWD_DEFINED__

    if not defined(__ICorDebugClass2_FWD_DEFINED__):
        __ICorDebugClass2_FWD_DEFINED__ = VOID


        class ICorDebugClass2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugClass2_FWD_DEFINED__

    if not defined(__ICorDebugEval2_FWD_DEFINED__):
        __ICorDebugEval2_FWD_DEFINED__ = VOID


        class ICorDebugEval2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugEval2_FWD_DEFINED__

    if not defined(__ICorDebugValue2_FWD_DEFINED__):
        __ICorDebugValue2_FWD_DEFINED__ = VOID


        class ICorDebugValue2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugValue2_FWD_DEFINED__

    if not defined(__ICorDebugObjectValue2_FWD_DEFINED__):
        __ICorDebugObjectValue2_FWD_DEFINED__ = VOID


        class ICorDebugObjectValue2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugObjectValue2_FWD_DEFINED__

    if not defined(__ICorDebugHandleValue_FWD_DEFINED__):
        __ICorDebugHandleValue_FWD_DEFINED__ = VOID


        class ICorDebugHandleValue(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugHandleValue_FWD_DEFINED__

    if not defined(__ICorDebugHeapValue2_FWD_DEFINED__):
        __ICorDebugHeapValue2_FWD_DEFINED__ = VOID


        class ICorDebugHeapValue2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICorDebugHeapValue2_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwn_h import * # NOQA
    from pyWinAPI.um.objidl_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    # interface __MIDL_itf_cordebug_0000
    # [local]

    _ZERO_ = 0
    if _ZERO_:
        mdToken = UINT32
        mdModule = mdToken
        mdScope = SIZE_T
        mdTypeDef = mdToken
        mdSourceFile = mdToken
        mdMemberRef = mdToken
        mdMethodDef = mdToken
        mdFieldDef = mdToken
        mdSignature = mdToken
        CorElementType = ULONG
        PCCOR_SIGNATURE = SIZE_T
        LPDEBUG_EVENT = SIZE_T
        LPSTARTUPINFOW = SIZE_T
        LPPROCESS_INFORMATION = SIZE_T
    # END IF

    # [wire_marshal]
    HPROCESS = POINTER(VOID)

    # [wire_marshal]
    HTHREAD = POINTER(VOID)
    TASKID = UINT64
    CONNID = DWORD
    if not defined(_COR_IL_MAP):
        _COR_IL_MAP._fields_ = [
            ('oldOffset', ULONG32),
            ('newOffset', ULONG32),
            ('fAccurate', BOOL),
        ]
    # END IF  _COR_IL_MAP

    if not defined(_COR_DEBUG_IL_TO_NATIVE_MAP_):

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

    REMOTE_DEBUGGING_DLL_ENTRY = (
        "Software\\Microsoft\\.NETFramework\\Debugger\\ActivateRemoteDebugging"
    )


    class CorDebugJITCompilerFlags(ENUM):
        CORDEBUG_JIT_DEFAULT = 0x1
        CORDEBUG_JIT_DISABLE_OPTIMIZATION = 0x3
        CORDEBUG_JIT_ENABLE_ENC = 0x7


    class CorDebugJITCompilerFlagsDecprecated(ENUM):
        CORDEBUG_JIT_TRACK_DEBUG_INFO = 0x1

    CorDebugJITCompilerFlagsDeprecated = CorDebugJITCompilerFlagsDecprecated
    CORDB_ADDRESS = ULONG64
    CORDB_REGISTER = ULONG64
    if not defined(__ICorDebugManagedCallback_INTERFACE_DEFINED__):
        __ICorDebugManagedCallback_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugManagedCallback
        # [unique][uuid][object]
        class CorDebugStepReason(ENUM):
            STEP_NORMAL = 0
            STEP_RETURN = STEP_NORMAL + 1
            STEP_CALL = STEP_RETURN + 1
            STEP_EXCEPTION_FILTER = STEP_CALL + 1
            STEP_EXCEPTION_HANDLER = STEP_EXCEPTION_FILTER + 1
            STEP_INTERCEPT = STEP_EXCEPTION_HANDLER + 1
            STEP_EXIT = STEP_INTERCEPT + 1


        class LoggingLevelEnum(ENUM):
            LTraceLevel0 = 0
            LTraceLevel1 = LTraceLevel0 + 1
            LTraceLevel2 = LTraceLevel1 + 1
            LTraceLevel3 = LTraceLevel2 + 1
            LTraceLevel4 = LTraceLevel3 + 1
            LStatusLevel0 = 20
            LStatusLevel1 = LStatusLevel0 + 1
            LStatusLevel2 = LStatusLevel1 + 1
            LStatusLevel3 = LStatusLevel2 + 1
            LStatusLevel4 = LStatusLevel3 + 1
            LWarningLevel = 40
            LErrorLevel = 50
            LPanicLevel = 100


        class LogSwitchCallReason(ENUM):
            SWITCH_CREATE = 0
            SWITCH_MODIFY = SWITCH_CREATE + 1
            SWITCH_DELETE = SWITCH_MODIFY + 1

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugManagedCallback = MIDL_INTERFACE(
                "{3D6F5F60-7538-11D3-8D5B-00104B35E7EF}"
            )
            ICorDebugManagedCallback._iid_ = IID_ICorDebugManagedCallback

            ICorDebugManagedCallback._methods_ = [
                COMMETHOD(
                    [helpstring('Method Breakpoint')],
                    HRESULT,
                    'Breakpoint',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugBreakpoint), 'pBreakpoint'),
                ),
                COMMETHOD(
                    [helpstring('Method StepComplete')],
                    HRESULT,
                    'StepComplete',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugStepper), 'pStepper'),
                    (['in'], CorDebugStepReason, 'reason'),
                ),
                COMMETHOD(
                    [helpstring('Method Break')],
                    HRESULT,
                    'Break',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'thread'),
                ),
                COMMETHOD(
                    [helpstring('Method Exception')],
                    HRESULT,
                    'Exception',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], BOOL, 'unhandled'),
                ),
                COMMETHOD(
                    [helpstring('Method EvalComplete')],
                    HRESULT,
                    'EvalComplete',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugEval), 'pEval'),
                ),
                COMMETHOD(
                    [helpstring('Method EvalException')],
                    HRESULT,
                    'EvalException',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugEval), 'pEval'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateProcess')],
                    HRESULT,
                    'CreateProcess',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                ),
                COMMETHOD(
                    [helpstring('Method ExitProcess')],
                    HRESULT,
                    'ExitProcess',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateThread')],
                    HRESULT,
                    'CreateThread',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'thread'),
                ),
                COMMETHOD(
                    [helpstring('Method ExitThread')],
                    HRESULT,
                    'ExitThread',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'thread'),
                ),
                COMMETHOD(
                    [helpstring('Method LoadModule')],
                    HRESULT,
                    'LoadModule',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugModule), 'pModule'),
                ),
                COMMETHOD(
                    [helpstring('Method UnloadModule')],
                    HRESULT,
                    'UnloadModule',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugModule), 'pModule'),
                ),
                COMMETHOD(
                    [helpstring('Method LoadClass')],
                    HRESULT,
                    'LoadClass',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugClass), 'c'),
                ),
                COMMETHOD(
                    [helpstring('Method UnloadClass')],
                    HRESULT,
                    'UnloadClass',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugClass), 'c'),
                ),
                COMMETHOD(
                    [helpstring('Method DebuggerError')],
                    HRESULT,
                    'DebuggerError',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                    (['in'], HRESULT, 'errorHR'),
                    (['in'], DWORD, 'errorCode'),
                ),
                COMMETHOD(
                    [helpstring('Method LogMessage')],
                    HRESULT,
                    'LogMessage',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], LONG, 'lLevel'),
                    (['in'], POINTER(WCHAR), 'pLogSwitchName'),
                    (['in'], POINTER(WCHAR), 'pMessage'),
                ),
                COMMETHOD(
                    [helpstring('Method LogSwitch')],
                    HRESULT,
                    'LogSwitch',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], LONG, 'lLevel'),
                    (['in'], ULONG, 'ulReason'),
                    (['in'], POINTER(WCHAR), 'pLogSwitchName'),
                    (['in'], POINTER(WCHAR), 'pParentName'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateAppDomain')],
                    HRESULT,
                    'CreateAppDomain',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                ),
                COMMETHOD(
                    [helpstring('Method ExitAppDomain')],
                    HRESULT,
                    'ExitAppDomain',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                ),
                COMMETHOD(
                    [helpstring('Method LoadAssembly')],
                    HRESULT,
                    'LoadAssembly',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugAssembly), 'pAssembly'),
                ),
                COMMETHOD(
                    [helpstring('Method UnloadAssembly')],
                    HRESULT,
                    'UnloadAssembly',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugAssembly), 'pAssembly'),
                ),
                COMMETHOD(
                    [helpstring('Method ControlCTrap')],
                    HRESULT,
                    'ControlCTrap',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                ),
                COMMETHOD(
                    [helpstring('Method NameChange')],
                    HRESULT,
                    'NameChange',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                ),
                COMMETHOD(
                    [helpstring('Method UpdateModuleSymbols')],
                    HRESULT,
                    'UpdateModuleSymbols',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugModule), 'pModule'),
                    (['in'], POINTER(IStream), 'pSymbolStream'),
                ),
                COMMETHOD(
                    [helpstring('Method EditAndContinueRemap')],
                    HRESULT,
                    'EditAndContinueRemap',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugFunction), 'pFunction'),
                    (['in'], BOOL, 'fAccurate'),
                ),
                COMMETHOD(
                    [helpstring('Method BreakpointSetError')],
                    HRESULT,
                    'BreakpointSetError',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugBreakpoint), 'pBreakpoint'),
                    (['in'], DWORD, 'dwError'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugManagedCallback_INTERFACE_DEFINED__

    if not defined(__ICorDebugManagedCallback2_INTERFACE_DEFINED__):
        __ICorDebugManagedCallback2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugManagedCallback2
        # [unique][uuid][object]
        class CorDebugExceptionCallbackType(ENUM):
            DEBUG_EXCEPTION_FIRST_CHANCE = 1
            DEBUG_EXCEPTION_USER_FIRST_CHANCE = 2
            DEBUG_EXCEPTION_CATCH_HANDLER_FOUND = 3
            DEBUG_EXCEPTION_UNHANDLED = 4


        class CorDebugExceptionFlags(ENUM):
            DEBUG_EXCEPTION_CAN_BE_INTERCEPTED = 0x1


        class CorDebugExceptionUnwindCallbackType(ENUM):
            DEBUG_EXCEPTION_UNWIND_BEGIN = 1
            DEBUG_EXCEPTION_INTERCEPTED = 2

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugManagedCallback2 = MIDL_INTERFACE(
                "{250E5EEA-DB5C-4C76-B6F3-8C46F12E3203}"
            )
            ICorDebugManagedCallback2._iid_ = IID_ICorDebugManagedCallback2

            ICorDebugManagedCallback2._methods_ = [
                COMMETHOD(
                    [helpstring('Method FunctionRemapOpportunity')],
                    HRESULT,
                    'FunctionRemapOpportunity',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugFunction), 'pOldFunction'),
                    (['in'], POINTER(ICorDebugFunction), 'pNewFunction'),
                    (['in'], ULONG32, 'oldILOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateConnection')],
                    HRESULT,
                    'CreateConnection',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                    (['in'], CONNID, 'dwConnectionId'),
                    (['in'], POINTER(WCHAR), 'pConnName'),
                ),
                COMMETHOD(
                    [helpstring('Method ChangeConnection')],
                    HRESULT,
                    'ChangeConnection',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                    (['in'], CONNID, 'dwConnectionId'),
                ),
                COMMETHOD(
                    [helpstring('Method DestroyConnection')],
                    HRESULT,
                    'DestroyConnection',
                    (['in'], POINTER(ICorDebugProcess), 'pProcess'),
                    (['in'], CONNID, 'dwConnectionId'),
                ),
                COMMETHOD(
                    [helpstring('Method Exception')],
                    HRESULT,
                    'Exception',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugFrame), 'pFrame'),
                    (['in'], ULONG32, 'nOffset'),
                    (['in'], CorDebugExceptionCallbackType, 'dwEventType'),
                    (['in'], DWORD, 'dwFlags'),
                ),
                COMMETHOD(
                    [helpstring('Method ExceptionUnwind')],
                    HRESULT,
                    'ExceptionUnwind',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (
                        ['in'],
                        CorDebugExceptionUnwindCallbackType,
                        'dwEventType'
                    ),
                    (['in'], DWORD, 'dwFlags'),
                ),
                COMMETHOD(
                    [helpstring('Method FunctionRemapComplete')],
                    HRESULT,
                    'FunctionRemapComplete',
                    (['in'], POINTER(ICorDebugAppDomain), 'pAppDomain'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugFunction), 'pFunction'),
                ),
                COMMETHOD(
                    [helpstring('Method MDANotification')],
                    HRESULT,
                    'MDANotification',
                    (['in'], POINTER(ICorDebugController), 'pController'),
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['in'], POINTER(ICorDebugMDA), 'pMDA'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugManagedCallback2_INTERFACE_DEFINED__

    if not defined(__ICorDebugUnmanagedCallback_INTERFACE_DEFINED__):
        __ICorDebugUnmanagedCallback_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugUnmanagedCallback
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugUnmanagedCallback = MIDL_INTERFACE(
                "{5263E909-8CB5-11D3-BD2F-0000F80849BD}"
            )
            ICorDebugUnmanagedCallback._iid_ = IID_ICorDebugUnmanagedCallback

            ICorDebugUnmanagedCallback._methods_ = [
                COMMETHOD(
                    [helpstring('Method DebugEvent')],
                    HRESULT,
                    'DebugEvent',
                    (['in'], LPDEBUG_EVENT, 'pDebugEvent'),
                    (['in'], BOOL, 'fOutOfBand'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugUnmanagedCallback_INTERFACE_DEFINED__

    # interface __MIDL_itf_cordebug_0096
    # [local]
    class CorDebugCreateProcessFlags(ENUM):
        DEBUG_NO_SPECIAL_OPTIONS = 0


    class CorDebugHandleType(ENUM):
        HANDLE_STRONG = 1
        HANDLE_WEAK_TRACK_RESURRECTION = 2

    if not defined(__ICorDebug_INTERFACE_DEFINED__):
        __ICorDebug_INTERFACE_DEFINED__ = VOID

        # interface ICorDebug
        # [unique][uuid][local][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebug = MIDL_INTERFACE(
                "{3D6F5F61-7538-11D3-8D5B-00104B35E7EF}"
            )
            ICorDebug._iid_ = IID_ICorDebug

            ICorDebug._methods_ = [
                COMMETHOD(
                    [helpstring('Method Initialize')],
                    HRESULT,
                    'Initialize',
                ),
                COMMETHOD(
                    [helpstring('Method Terminate')],
                    HRESULT,
                    'Terminate',
                ),
                COMMETHOD(
                    [helpstring('Method SetManagedHandler')],
                    HRESULT,
                    'SetManagedHandler',
                    (['in'], POINTER(ICorDebugManagedCallback), 'pCallback'),
                ),
                COMMETHOD(
                    [helpstring('Method SetUnmanagedHandler')],
                    HRESULT,
                    'SetUnmanagedHandler',
                    (
                        ['in'],
                        POINTER(ICorDebugUnmanagedCallback),
                        'pCallback'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method CreateProcess')],
                    HRESULT,
                    'CreateProcess',
                    (['in'], LPCWSTR, 'lpApplicationName'),
                    (['in'], LPWSTR, 'lpCommandLine'),
                    (['in'], LPSECURITY_ATTRIBUTES, 'lpProcessAttributes'),
                    (['in'], LPSECURITY_ATTRIBUTES, 'lpThreadAttributes'),
                    (['in'], BOOL, 'bInheritHandles'),
                    (['in'], DWORD, 'dwCreationFlags'),
                    (['in'], PVOID, 'lpEnvironment'),
                    (['in'], LPCWSTR, 'lpCurrentDirectory'),
                    (['in'], LPSTARTUPINFOW, 'lpStartupInfo'),
                    (['in'], LPPROCESS_INFORMATION, 'lpProcessInformation'),
                    (['in'], CorDebugCreateProcessFlags, 'debuggingFlags'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcess)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method DebugActiveProcess')],
                    HRESULT,
                    'DebugActiveProcess',
                    (['in'], DWORD, 'id'),
                    (['in'], BOOL, 'win32Attach'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcess)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateProcesses')],
                    HRESULT,
                    'EnumerateProcesses',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcessEnum)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetProcess')],
                    HRESULT,
                    'GetProcess',
                    (['in'], DWORD, 'dwProcessId'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcess)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method CanLaunchOrAttach')],
                    HRESULT,
                    'CanLaunchOrAttach',
                    (['in'], DWORD, 'dwProcessId'),
                    (['in'], BOOL, 'win32DebuggingEnabled'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebug_INTERFACE_DEFINED__

    # interface __MIDL_itf_cordebug_0097
    # [local]
    _COR_VERSION._fields_ = [
        ('dwMajor', DWORD),
        ('dwMinor', DWORD),
        ('dwBuild', DWORD),
        ('dwSubBuild', DWORD),
    ]
    if not defined(__ICorDebug2_INTERFACE_DEFINED__):
        __ICorDebug2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebug2
        # [unique][uuid][local][object]
        class CorDebugInterfaceVersion(ENUM):
            CorDebugInvalidVersion = 0
            CorDebugVersion_1_0 = CorDebugInvalidVersion + 1
            ver_ICorDebugManagedCallback = CorDebugVersion_1_0
            ver_ICorDebugUnmanagedCallback = CorDebugVersion_1_0
            ver_ICorDebug = CorDebugVersion_1_0
            ver_ICorDebugController = CorDebugVersion_1_0
            ver_ICorDebugAppDomain = CorDebugVersion_1_0
            ver_ICorDebugAssembly = CorDebugVersion_1_0
            ver_ICorDebugProcess = CorDebugVersion_1_0
            ver_ICorDebugBreakpoint = CorDebugVersion_1_0
            ver_ICorDebugFunctionBreakpoint = CorDebugVersion_1_0
            ver_ICorDebugModuleBreakpoint = CorDebugVersion_1_0
            ver_ICorDebugValueBreakpoint = CorDebugVersion_1_0
            ver_ICorDebugStepper = CorDebugVersion_1_0
            ver_ICorDebugRegisterSet = CorDebugVersion_1_0
            ver_ICorDebugThread = CorDebugVersion_1_0
            ver_ICorDebugChain = CorDebugVersion_1_0
            ver_ICorDebugFrame = CorDebugVersion_1_0
            ver_ICorDebugILFrame = CorDebugVersion_1_0
            ver_ICorDebugNativeFrame = CorDebugVersion_1_0
            ver_ICorDebugModule = CorDebugVersion_1_0
            ver_ICorDebugFunction = CorDebugVersion_1_0
            ver_ICorDebugCode = CorDebugVersion_1_0
            ver_ICorDebugClass = CorDebugVersion_1_0
            ver_ICorDebugEval = CorDebugVersion_1_0
            ver_ICorDebugValue = CorDebugVersion_1_0
            ver_ICorDebugGenericValue = CorDebugVersion_1_0
            ver_ICorDebugReferenceValue = CorDebugVersion_1_0
            ver_ICorDebugHeapValue = CorDebugVersion_1_0
            ver_ICorDebugObjectValue = CorDebugVersion_1_0
            ver_ICorDebugBoxValue = CorDebugVersion_1_0
            ver_ICorDebugStringValue = CorDebugVersion_1_0
            ver_ICorDebugArrayValue = CorDebugVersion_1_0
            ver_ICorDebugContext = CorDebugVersion_1_0
            ver_ICorDebugEnum = CorDebugVersion_1_0
            ver_ICorDebugObjectEnum = CorDebugVersion_1_0
            ver_ICorDebugBreakpointEnum = CorDebugVersion_1_0
            ver_ICorDebugStepperEnum = CorDebugVersion_1_0
            ver_ICorDebugProcessEnum = CorDebugVersion_1_0
            ver_ICorDebugThreadEnum = CorDebugVersion_1_0
            ver_ICorDebugFrameEnum = CorDebugVersion_1_0
            ver_ICorDebugChainEnum = CorDebugVersion_1_0
            ver_ICorDebugModuleEnum = CorDebugVersion_1_0
            ver_ICorDebugValueEnum = CorDebugVersion_1_0
            ver_ICorDebugCodeEnum = CorDebugVersion_1_0
            ver_ICorDebugTypeEnum = CorDebugVersion_1_0
            ver_ICorDebugErrorInfoEnum = CorDebugVersion_1_0
            ver_ICorDebugAppDomainEnum = CorDebugVersion_1_0
            ver_ICorDebugAssemblyEnum = CorDebugVersion_1_0
            ver_ICorDebugEditAndContinueErrorInfo = CorDebugVersion_1_0
            ver_ICorDebugEditAndContinueSnapshot = CorDebugVersion_1_0
            CorDebugVersion_1_1 = CorDebugVersion_1_0 + 1
            CorDebugVersion_2_0 = CorDebugVersion_1_1 + 1
            ver_ICorDebugManagedCallback2 = CorDebugVersion_2_0
            ver_ICorDebugAppDomain2 = CorDebugVersion_2_0
            ver_ICorDebugAssembly2 = CorDebugVersion_2_0
            ver_ICorDebugProcess2 = CorDebugVersion_2_0
            ver_ICorDebugStepper2 = CorDebugVersion_2_0
            ver_ICorDebugRegisterSet2 = CorDebugVersion_2_0
            ver_ICorDebugThread2 = CorDebugVersion_2_0
            ver_ICorDebugILFrame2 = CorDebugVersion_2_0
            ver_ICorDebugModule2 = CorDebugVersion_2_0
            ver_ICorDebugFunction2 = CorDebugVersion_2_0
            ver_ICorDebugCode2 = CorDebugVersion_2_0
            ver_ICorDebugClass2 = CorDebugVersion_2_0
            ver_ICorDebugValue2 = CorDebugVersion_2_0
            ver_ICorDebugEval2 = CorDebugVersion_2_0
            ver_ICorDebugObjectValue2 = CorDebugVersion_2_0
            CorDebugLatestVersion = CorDebugVersion_2_0

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebug2 = MIDL_INTERFACE(
                "{ECCCCF2E-B286-4B3E-A983-860A8793D105}"
            )
            ICorDebug2._iid_ = IID_ICorDebug2

            ICorDebug2._methods_ = []

        # END IF  C style interface
    # END IF  __ICorDebug2_INTERFACE_DEFINED__

    # interface __MIDL_itf_cordebug_0098
    # [local]
    class CorDebugThreadState(ENUM):
        THREAD_RUN = 0
        THREAD_SUSPEND = THREAD_RUN + 1

    if not defined(__ICorDebugController_INTERFACE_DEFINED__):
        __ICorDebugController_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugController
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugController = MIDL_INTERFACE(
                "{3D6F5F62-7538-11D3-8D5B-00104B35E7EF}"
            )
            ICorDebugController._iid_ = IID_ICorDebugController

            ICorDebugController._methods_ = [
                COMMETHOD(
                    [helpstring('Method Stop')],
                    HRESULT,
                    'Stop',
                    (['in'], DWORD, 'dwTimeoutIgnored'),
                ),
                COMMETHOD(
                    [helpstring('Method Continue')],
                    HRESULT,
                    'Continue',
                    (['in'], BOOL, 'fIsOutOfBand'),
                ),
                COMMETHOD(
                    [helpstring('Method IsRunning')],
                    HRESULT,
                    'IsRunning',
                    (['out'], POINTER(BOOL), 'pbRunning'),
                ),
                COMMETHOD(
                    [helpstring('Method HasQueuedCallbacks')],
                    HRESULT,
                    'HasQueuedCallbacks',
                    (['in'], POINTER(ICorDebugThread), 'pThread'),
                    (['out'], POINTER(BOOL), 'pbQueued'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateThreads')],
                    HRESULT,
                    'EnumerateThreads',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugThreadEnum)),
                        'ppThreads'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method SetAllThreadsDebugState')],
                    HRESULT,
                    'SetAllThreadsDebugState',
                    (['in'], CorDebugThreadState, 'state'),
                    (['in'], POINTER(ICorDebugThread), 'pExceptThisThread'),
                ),
                COMMETHOD(
                    [helpstring('Method Detach')],
                    HRESULT,
                    'Detach',
                ),
                COMMETHOD(
                    [helpstring('Method Terminate')],
                    HRESULT,
                    'Terminate',
                    (['in'], UINT, 'exitCode'),
                ),
                COMMETHOD(
                    [helpstring('Method CanCommitChanges')],
                    HRESULT,
                    'CanCommitChanges',
                    (['in'], ULONG, 'cSnapshots'),
                    (
                        ['in'],
                        POINTER(ICorDebugEditAndContinueSnapshot * 0),
                        'pSnapshots'
                    ),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugErrorInfoEnum)),
                        'pError'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method CommitChanges')],
                    HRESULT,
                    'CommitChanges',
                    (['in'], ULONG, 'cSnapshots'),
                    (
                        ['in'],
                        POINTER(ICorDebugEditAndContinueSnapshot * 0),
                        'pSnapshots'
                    ),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugErrorInfoEnum)),
                        'pError'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugController_INTERFACE_DEFINED__

    if not defined(__ICorDebugAppDomain_INTERFACE_DEFINED__):
        __ICorDebugAppDomain_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugAppDomain
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugAppDomain = MIDL_INTERFACE(
                "{3D6F5F63-7538-11D3-8D5B-00104B35E7EF}"
            )
            ICorDebugAppDomain._iid_ = IID_ICorDebugAppDomain

            ICorDebugAppDomain._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetProcess')],
                    HRESULT,
                    'GetProcess',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcess)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateAssemblies')],
                    HRESULT,
                    'EnumerateAssemblies',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugAssemblyEnum)),
                        'ppAssemblies'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetModuleFromMetaDataInterface')],
                    HRESULT,
                    'GetModuleFromMetaDataInterface',
                    (['in'], POINTER(comtypes.IUnknown), 'pIMetaData'),
                    (['out'], POINTER(POINTER(ICorDebugModule)), 'ppModule'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateBreakpoints')],
                    HRESULT,
                    'EnumerateBreakpoints',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugBreakpointEnum)),
                        'ppBreakpoints'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateSteppers')],
                    HRESULT,
                    'EnumerateSteppers',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugStepperEnum)),
                        'ppSteppers'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method IsAttached')],
                    HRESULT,
                    'IsAttached',
                    (['out'], POINTER(BOOL), 'pbAttached'),
                ),
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetObject')],
                    HRESULT,
                    'GetObject',
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppObject'),
                ),
                COMMETHOD(
                    [helpstring('Method Attach')],
                    HRESULT,
                    'Attach',
                ),
                COMMETHOD(
                    [helpstring('Method GetID')],
                    HRESULT,
                    'GetID',
                    (['out'], POINTER(ULONG32), 'pId'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugAppDomain_INTERFACE_DEFINED__

    if not defined(__ICorDebugAppDomain2_INTERFACE_DEFINED__):
        __ICorDebugAppDomain2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugAppDomain2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugAppDomain2 = MIDL_INTERFACE(
                "{096E81D5-ECDA-4202-83F5-C65980A9EF75}"
            )
            ICorDebugAppDomain2._iid_ = IID_ICorDebugAppDomain2

            ICorDebugAppDomain2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetArrayOrPointerType')],
                    HRESULT,
                    'GetArrayOrPointerType',
                    (['in'], CorElementType, 'elementType'),
                    (['in'], ULONG32, 'nRank'),
                    (['in'], POINTER(ICorDebugType), 'pTypeArg'),
                    (['out'], POINTER(POINTER(ICorDebugType)), 'ppType'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionPointerType')],
                    HRESULT,
                    'GetFunctionPointerType',
                    (['in'], ULONG32, 'nTypeArgs'),
                    (['in'], POINTER(ICorDebugType * 0), 'ppTypeArgs'),
                    (['out'], POINTER(POINTER(ICorDebugType)), 'ppType'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugAppDomain2_INTERFACE_DEFINED__

    if not defined(__ICorDebugAssembly_INTERFACE_DEFINED__):
        __ICorDebugAssembly_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugAssembly
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugAssembly = MIDL_INTERFACE(
                "{DF59507C-D47A-459E-BCE2-6427EAC8FD06}"
            )
            ICorDebugAssembly._iid_ = IID_ICorDebugAssembly

            ICorDebugAssembly._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetProcess')],
                    HRESULT,
                    'GetProcess',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcess)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetAppDomain')],
                    HRESULT,
                    'GetAppDomain',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugAppDomain)),
                        'ppAppDomain'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateModules')],
                    HRESULT,
                    'EnumerateModules',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugModuleEnum)),
                        'ppModules'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetCodeBase')],
                    HRESULT,
                    'GetCodeBase',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugAssembly_INTERFACE_DEFINED__

    if not defined(__ICorDebugAssembly2_INTERFACE_DEFINED__):
        __ICorDebugAssembly2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugAssembly2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugAssembly2 = MIDL_INTERFACE(
                "{426D1F9E-6DD4-44C8-AEC7-26CDBAF4E398}"
            )
            ICorDebugAssembly2._iid_ = IID_ICorDebugAssembly2

            ICorDebugAssembly2._methods_ = [
                COMMETHOD(
                    [helpstring('Method IsFullyTrusted')],
                    HRESULT,
                    'IsFullyTrusted',
                    (['out'], POINTER(BOOL), 'pbFullyTrusted'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugAssembly2_INTERFACE_DEFINED__

    if not defined(__ICorDebugProcess_INTERFACE_DEFINED__):
        __ICorDebugProcess_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugProcess
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugProcess = MIDL_INTERFACE(
                "{3D6F5F64-7538-11D3-8D5B-00104B35E7EF}"
            )
            ICorDebugProcess._iid_ = IID_ICorDebugProcess

            ICorDebugProcess._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetID')],
                    HRESULT,
                    'GetID',
                    (['out'], POINTER(DWORD), 'pdwProcessId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetHandle')],
                    HRESULT,
                    'GetHandle',
                    (['out'], POINTER(HPROCESS), 'phProcessHandle'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThread')],
                    HRESULT,
                    'GetThread',
                    (['in'], DWORD, 'dwThreadId'),
                    (['out'], POINTER(POINTER(ICorDebugThread)), 'ppThread'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateObjects')],
                    HRESULT,
                    'EnumerateObjects',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugObjectEnum)),
                        'ppObjects'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method IsTransitionStub')],
                    HRESULT,
                    'IsTransitionStub',
                    (['in'], CORDB_ADDRESS, 'address'),
                    (['out'], POINTER(BOOL), 'pbTransitionStub'),
                ),
                COMMETHOD(
                    [helpstring('Method IsOSSuspended')],
                    HRESULT,
                    'IsOSSuspended',
                    (['in'], DWORD, 'threadID'),
                    (['out'], POINTER(BOOL), 'pbSuspended'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThreadContext')],
                    HRESULT,
                    'GetThreadContext',
                    (['in'], DWORD, 'threadID'),
                    (['in'], ULONG32, 'contextSize'),
                    (['out', 'in'], BYTE * 0, 'context'),
                ),
                COMMETHOD(
                    [helpstring('Method SetThreadContext')],
                    HRESULT,
                    'SetThreadContext',
                    (['in'], DWORD, 'threadID'),
                    (['in'], ULONG32, 'contextSize'),
                    (['in'], BYTE * 0, 'context'),
                ),
                COMMETHOD(
                    [helpstring('Method ReadMemory')],
                    HRESULT,
                    'ReadMemory',
                    (['in'], CORDB_ADDRESS, 'address'),
                    (['in'], DWORD, 'size'),
                    (['out'], BYTE * 0, 'buffer'),
                    (['out'], POINTER(SIZE_T), 'read'),
                ),
                COMMETHOD(
                    [helpstring('Method WriteMemory')],
                    HRESULT,
                    'WriteMemory',
                    (['in'], CORDB_ADDRESS, 'address'),
                    (['in'], DWORD, 'size'),
                    (['in'], BYTE * 0, 'buffer'),
                    (['out'], POINTER(SIZE_T), 'written'),
                ),
                COMMETHOD(
                    [helpstring('Method ClearCurrentException')],
                    HRESULT,
                    'ClearCurrentException',
                    (['in'], DWORD, 'threadID'),
                ),
                COMMETHOD(
                    [helpstring('Method EnableLogMessages')],
                    HRESULT,
                    'EnableLogMessages',
                    (['in'], BOOL, 'fOnOff'),
                ),
                COMMETHOD(
                    [helpstring('Method ModifyLogSwitch')],
                    HRESULT,
                    'ModifyLogSwitch',
                    (['in'], POINTER(WCHAR), 'pLogSwitchName'),
                    (['in'], LONG, 'lLevel'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateAppDomains')],
                    HRESULT,
                    'EnumerateAppDomains',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugAppDomainEnum)),
                        'ppAppDomains'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetObject')],
                    HRESULT,
                    'GetObject',
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppObject'),
                ),
                COMMETHOD(
                    [helpstring('Method ThreadForFiberCookie')],
                    HRESULT,
                    'ThreadForFiberCookie',
                    (['in'], DWORD, 'fiberCookie'),
                    (['out'], POINTER(POINTER(ICorDebugThread)), 'ppThread'),
                ),
                COMMETHOD(
                    [helpstring('Method GetHelperThreadID')],
                    HRESULT,
                    'GetHelperThreadID',
                    (['out'], POINTER(DWORD), 'pThreadID'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugProcess_INTERFACE_DEFINED__

    if not defined(__ICorDebugProcess2_INTERFACE_DEFINED__):
        __ICorDebugProcess2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugProcess2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugProcess2 = MIDL_INTERFACE(
                "{AD1B3588-0EF0-4744-A496-AA09A9F80371}"
            )
            ICorDebugProcess2._iid_ = IID_ICorDebugProcess2

            ICorDebugProcess2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetThreadForTaskID')],
                    HRESULT,
                    'GetThreadForTaskID',
                    (['in'], TASKID, 'taskid'),
                    (['out'], POINTER(POINTER(ICorDebugThread2)), 'ppThread'),
                ),
                COMMETHOD(
                    [helpstring('Method GetVersion')],
                    HRESULT,
                    'GetVersion',
                    (['out'], POINTER(COR_VERSION), 'version'),
                ),
                COMMETHOD(
                    [helpstring('Method SetUnmanagedBreakpoint')],
                    HRESULT,
                    'SetUnmanagedBreakpoint',
                    (['in'], CORDB_ADDRESS, 'address'),
                    (['in'], ULONG32, 'bufsize'),
                    (['out'], BYTE * 0, 'buffer'),
                    (['out'], POINTER(ULONG32), 'bufLen'),
                ),
                COMMETHOD(
                    [helpstring('Method ClearUnmanagedBreakpoint')],
                    HRESULT,
                    'ClearUnmanagedBreakpoint',
                    (['in'], CORDB_ADDRESS, 'address'),
                ),
                COMMETHOD(
                    [helpstring('Method SetDesiredNGENCompilerFlags')],
                    HRESULT,
                    'SetDesiredNGENCompilerFlags',
                    (['in'], DWORD, 'pdwFlags'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDesiredNGENCompilerFlags')],
                    HRESULT,
                    'GetDesiredNGENCompilerFlags',
                    (['out'], POINTER(DWORD), 'pdwFlags'),
                ),
                COMMETHOD(
                    [helpstring('Method GetReferenceValueFromGCHandle')],
                    HRESULT,
                    'GetReferenceValueFromGCHandle',
                    (['in'], UINT_PTR, 'handle'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugReferenceValue)),
                        'pOutValue'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugProcess2_INTERFACE_DEFINED__

    if not defined(__ICorDebugBreakpoint_INTERFACE_DEFINED__):
        __ICorDebugBreakpoint_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugBreakpoint
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugBreakpoint = MIDL_INTERFACE(
                "{CC7BCAE8-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugBreakpoint._iid_ = IID_ICorDebugBreakpoint

            ICorDebugBreakpoint._methods_ = [
                COMMETHOD(
                    [helpstring('Method Activate')],
                    HRESULT,
                    'Activate',
                    (['in'], BOOL, 'bActive'),
                ),
                COMMETHOD(
                    [helpstring('Method IsActive')],
                    HRESULT,
                    'IsActive',
                    (['out'], POINTER(BOOL), 'pbActive'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugBreakpoint_INTERFACE_DEFINED__

    if not defined(__ICorDebugFunctionBreakpoint_INTERFACE_DEFINED__):
        __ICorDebugFunctionBreakpoint_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugFunctionBreakpoint
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugFunctionBreakpoint = MIDL_INTERFACE(
                "{CC7BCAE9-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugFunctionBreakpoint._iid_ = IID_ICorDebugFunctionBreakpoint

            ICorDebugFunctionBreakpoint._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetFunction')],
                    HRESULT,
                    'GetFunction',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunction)),
                        'ppFunction'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetOffset')],
                    HRESULT,
                    'GetOffset',
                    (['out'], POINTER(ULONG32), 'pnOffset'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugFunctionBreakpoint_INTERFACE_DEFINED__

    if not defined(__ICorDebugModuleBreakpoint_INTERFACE_DEFINED__):
        __ICorDebugModuleBreakpoint_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugModuleBreakpoint
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugModuleBreakpoint = MIDL_INTERFACE(
                "{CC7BCAEA-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugModuleBreakpoint._iid_ = IID_ICorDebugModuleBreakpoint

            ICorDebugModuleBreakpoint._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetModule')],
                    HRESULT,
                    'GetModule',
                    (['out'], POINTER(POINTER(ICorDebugModule)), 'ppModule'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugModuleBreakpoint_INTERFACE_DEFINED__

    if not defined(__ICorDebugValueBreakpoint_INTERFACE_DEFINED__):
        __ICorDebugValueBreakpoint_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugValueBreakpoint
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugValueBreakpoint = MIDL_INTERFACE(
                "{CC7BCAEB-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugValueBreakpoint._iid_ = IID_ICorDebugValueBreakpoint

            ICorDebugValueBreakpoint._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetValue')],
                    HRESULT,
                    'GetValue',
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugValueBreakpoint_INTERFACE_DEFINED__

    if not defined(__ICorDebugStepper_INTERFACE_DEFINED__):
        __ICorDebugStepper_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugStepper
        # [unique][uuid][object]
        class CorDebugIntercept(ENUM):
            INTERCEPT_NONE = 0
            INTERCEPT_CLASS_INIT = 0x1
            INTERCEPT_EXCEPTION_FILTER = 0x2
            INTERCEPT_SECURITY = 0x4
            INTERCEPT_CONTEXT_POLICY = 0x8
            INTERCEPT_INTERCEPTION = 0x10
            INTERCEPT_ALL = 0xFFFF


        class CorDebugUnmappedStop(ENUM):
            STOP_NONE = 0
            STOP_PROLOG = 0x1
            STOP_EPILOG = 0x2
            STOP_NO_MAPPING_INFO = 0x4
            STOP_OTHER_UNMAPPED = 0x8
            STOP_UNMANAGED = 0x10
            STOP_ALL = 0xFFFF

        COR_DEBUG_STEP_RANGE._fields_ = [
            ('startOffset', ULONG32),
            ('endOffset', ULONG32),
        ]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugStepper = MIDL_INTERFACE(
                "{CC7BCAEC-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugStepper._iid_ = IID_ICorDebugStepper

            ICorDebugStepper._methods_ = [
                COMMETHOD(
                    [helpstring('Method IsActive')],
                    HRESULT,
                    'IsActive',
                    (['out'], POINTER(BOOL), 'pbActive'),
                ),
                COMMETHOD(
                    [helpstring('Method Deactivate')],
                    HRESULT,
                    'Deactivate',
                ),
                COMMETHOD(
                    [helpstring('Method SetInterceptMask')],
                    HRESULT,
                    'SetInterceptMask',
                    (['in'], CorDebugIntercept, 'mask'),
                ),
                COMMETHOD(
                    [helpstring('Method SetUnmappedStopMask')],
                    HRESULT,
                    'SetUnmappedStopMask',
                    (['in'], CorDebugUnmappedStop, 'mask'),
                ),
                COMMETHOD(
                    [helpstring('Method Step')],
                    HRESULT,
                    'Step',
                    (['in'], BOOL, 'bStepIn'),
                ),
                COMMETHOD(
                    [helpstring('Method StepRange')],
                    HRESULT,
                    'StepRange',
                    (['in'], BOOL, 'bStepIn'),
                    (['in'], COR_DEBUG_STEP_RANGE * 0, 'ranges'),
                    (['in'], ULONG32, 'cRangeCount'),
                ),
                COMMETHOD(
                    [helpstring('Method StepOut')],
                    HRESULT,
                    'StepOut',
                ),
                COMMETHOD(
                    [helpstring('Method SetRangeIL')],
                    HRESULT,
                    'SetRangeIL',
                    (['in'], BOOL, 'bIL'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugStepper_INTERFACE_DEFINED__

    if not defined(__ICorDebugStepper2_INTERFACE_DEFINED__):
        __ICorDebugStepper2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugStepper2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugStepper2 = MIDL_INTERFACE(
                "{C5B6E9C3-E7D1-4A8E-873B-7F047F0706F7}"
            )
            ICorDebugStepper2._iid_ = IID_ICorDebugStepper2

            ICorDebugStepper2._methods_ = [
                COMMETHOD(
                    [helpstring('Method SetJMC')],
                    HRESULT,
                    'SetJMC',
                    (['in'], BOOL, 'fIsJMCStepper'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugStepper2_INTERFACE_DEFINED__

    if not defined(__ICorDebugRegisterSet_INTERFACE_DEFINED__):
        __ICorDebugRegisterSet_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugRegisterSet
        # [unique][uuid][object]
        class CorDebugRegister(ENUM):
            REGISTER_INSTRUCTION_POINTER = 0
            REGISTER_STACK_POINTER = REGISTER_INSTRUCTION_POINTER + 1
            REGISTER_FRAME_POINTER = REGISTER_STACK_POINTER + 1
            REGISTER_X86_EIP = 0
            REGISTER_X86_ESP = REGISTER_X86_EIP + 1
            REGISTER_X86_EBP = REGISTER_X86_ESP + 1
            REGISTER_X86_EAX = REGISTER_X86_EBP + 1
            REGISTER_X86_ECX = REGISTER_X86_EAX + 1
            REGISTER_X86_EDX = REGISTER_X86_ECX + 1
            REGISTER_X86_EBX = REGISTER_X86_EDX + 1
            REGISTER_X86_ESI = REGISTER_X86_EBX + 1
            REGISTER_X86_EDI = REGISTER_X86_ESI + 1
            REGISTER_X86_FPSTACK_0 = REGISTER_X86_EDI + 1
            REGISTER_X86_FPSTACK_1 = REGISTER_X86_FPSTACK_0 + 1
            REGISTER_X86_FPSTACK_2 = REGISTER_X86_FPSTACK_1 + 1
            REGISTER_X86_FPSTACK_3 = REGISTER_X86_FPSTACK_2 + 1
            REGISTER_X86_FPSTACK_4 = REGISTER_X86_FPSTACK_3 + 1
            REGISTER_X86_FPSTACK_5 = REGISTER_X86_FPSTACK_4 + 1
            REGISTER_X86_FPSTACK_6 = REGISTER_X86_FPSTACK_5 + 1
            REGISTER_X86_FPSTACK_7 = REGISTER_X86_FPSTACK_6 + 1
            REGISTER_AMD64_RIP = 0
            REGISTER_AMD64_RSP = REGISTER_AMD64_RIP + 1
            REGISTER_AMD64_RBP = REGISTER_AMD64_RSP + 1
            REGISTER_AMD64_RAX = REGISTER_AMD64_RBP + 1
            REGISTER_AMD64_RCX = REGISTER_AMD64_RAX + 1
            REGISTER_AMD64_RDX = REGISTER_AMD64_RCX + 1
            REGISTER_AMD64_RBX = REGISTER_AMD64_RDX + 1
            REGISTER_AMD64_RSI = REGISTER_AMD64_RBX + 1
            REGISTER_AMD64_RDI = REGISTER_AMD64_RSI + 1
            REGISTER_AMD64_R8 = REGISTER_AMD64_RDI + 1
            REGISTER_AMD64_R9 = REGISTER_AMD64_R8 + 1
            REGISTER_AMD64_R10 = REGISTER_AMD64_R9 + 1
            REGISTER_AMD64_R11 = REGISTER_AMD64_R10 + 1
            REGISTER_AMD64_R12 = REGISTER_AMD64_R11 + 1
            REGISTER_AMD64_R13 = REGISTER_AMD64_R12 + 1
            REGISTER_AMD64_R14 = REGISTER_AMD64_R13 + 1
            REGISTER_AMD64_R15 = REGISTER_AMD64_R14 + 1
            REGISTER_AMD64_XMM0 = REGISTER_AMD64_R15 + 1
            REGISTER_AMD64_XMM1 = REGISTER_AMD64_XMM0 + 1
            REGISTER_AMD64_XMM2 = REGISTER_AMD64_XMM1 + 1
            REGISTER_AMD64_XMM3 = REGISTER_AMD64_XMM2 + 1
            REGISTER_AMD64_XMM4 = REGISTER_AMD64_XMM3 + 1
            REGISTER_AMD64_XMM5 = REGISTER_AMD64_XMM4 + 1
            REGISTER_AMD64_XMM6 = REGISTER_AMD64_XMM5 + 1
            REGISTER_AMD64_XMM7 = REGISTER_AMD64_XMM6 + 1
            REGISTER_AMD64_XMM8 = REGISTER_AMD64_XMM7 + 1
            REGISTER_AMD64_XMM9 = REGISTER_AMD64_XMM8 + 1
            REGISTER_AMD64_XMM10 = REGISTER_AMD64_XMM9 + 1
            REGISTER_AMD64_XMM11 = REGISTER_AMD64_XMM10 + 1
            REGISTER_AMD64_XMM12 = REGISTER_AMD64_XMM11 + 1
            REGISTER_AMD64_XMM13 = REGISTER_AMD64_XMM12 + 1
            REGISTER_AMD64_XMM14 = REGISTER_AMD64_XMM13 + 1
            REGISTER_AMD64_XMM15 = REGISTER_AMD64_XMM14 + 1
            REGISTER_IA64_BSP = REGISTER_FRAME_POINTER
            REGISTER_IA64_R0 = REGISTER_IA64_BSP + 1
            REGISTER_IA64_F0 = REGISTER_IA64_R0 + 128

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugRegisterSet = MIDL_INTERFACE(
                "{CC7BCB0B-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugRegisterSet._iid_ = IID_ICorDebugRegisterSet

            ICorDebugRegisterSet._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetRegistersAvailable')],
                    HRESULT,
                    'GetRegistersAvailable',
                    (['out'], POINTER(ULONG64), 'pAvailable'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRegisters')],
                    HRESULT,
                    'GetRegisters',
                    (['in'], ULONG64, 'mask'),
                    (['in'], ULONG32, 'regCount'),
                    (['out'], CORDB_REGISTER * 0, 'regBuffer'),
                ),
                COMMETHOD(
                    [helpstring('Method SetRegisters')],
                    HRESULT,
                    'SetRegisters',
                    (['in'], ULONG64, 'mask'),
                    (['in'], ULONG32, 'regCount'),
                    (['in'], CORDB_REGISTER * 0, 'regBuffer'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThreadContext')],
                    HRESULT,
                    'GetThreadContext',
                    (['in'], ULONG32, 'contextSize'),
                    (['out', 'in'], BYTE * 0, 'context'),
                ),
                COMMETHOD(
                    [helpstring('Method SetThreadContext')],
                    HRESULT,
                    'SetThreadContext',
                    (['in'], ULONG32, 'contextSize'),
                    (['in'], BYTE * 0, 'context'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugRegisterSet_INTERFACE_DEFINED__

    if not defined(__ICorDebugRegisterSet2_INTERFACE_DEFINED__):
        __ICorDebugRegisterSet2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugRegisterSet2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugRegisterSet2 = MIDL_INTERFACE(
                "{6DC7BA3F-89BA-4459-9EC1-9D60937B468D}"
            )
            ICorDebugRegisterSet2._iid_ = IID_ICorDebugRegisterSet2

            ICorDebugRegisterSet2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetRegistersAvailable')],
                    HRESULT,
                    'GetRegistersAvailable',
                    (['in'], ULONG32, 'numChunks'),
                    (['out'], BYTE * 0, 'availableRegChunks'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRegisters')],
                    HRESULT,
                    'GetRegisters',
                    (['in'], ULONG32, 'maskCount'),
                    (['in'], BYTE * 0, 'mask'),
                    (['in'], ULONG32, 'regCount'),
                    (['out'], CORDB_REGISTER * 0, 'regBuffer'),
                ),
                COMMETHOD(
                    [helpstring('Method SetRegisters')],
                    HRESULT,
                    'SetRegisters',
                    (['in'], ULONG32, 'maskCount'),
                    (['in'], BYTE * 0, 'mask'),
                    (['in'], ULONG32, 'regCount'),
                    (['in'], CORDB_REGISTER * 0, 'regBuffer'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugRegisterSet2_INTERFACE_DEFINED__

    if not defined(__ICorDebugThread_INTERFACE_DEFINED__):
        __ICorDebugThread_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugThread
        # [unique][uuid][object]
        class CorDebugUserState(ENUM):
            USER_STOP_REQUESTED = 0x1
            USER_SUSPEND_REQUESTED = 0x2
            USER_BACKGROUND = 0x4
            USER_UNSTARTED = 0x8
            USER_STOPPED = 0x10
            USER_WAIT_SLEEP_JOIN = 0x20
            USER_SUSPENDED = 0x40
            USER_UNSAFE_POINT = 0x80

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugThread = MIDL_INTERFACE(
                "{938C6D66-7FB6-4F69-B389-425B8987329B}"
            )
            ICorDebugThread._iid_ = IID_ICorDebugThread

            ICorDebugThread._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetProcess')],
                    HRESULT,
                    'GetProcess',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcess)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetID')],
                    HRESULT,
                    'GetID',
                    (['out'], POINTER(DWORD), 'pdwThreadId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetHandle')],
                    HRESULT,
                    'GetHandle',
                    (['out'], POINTER(HTHREAD), 'phThreadHandle'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAppDomain')],
                    HRESULT,
                    'GetAppDomain',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugAppDomain)),
                        'ppAppDomain'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method SetDebugState')],
                    HRESULT,
                    'SetDebugState',
                    (['in'], CorDebugThreadState, 'state'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDebugState')],
                    HRESULT,
                    'GetDebugState',
                    (['out'], POINTER(CorDebugThreadState), 'pState'),
                ),
                COMMETHOD(
                    [helpstring('Method GetUserState')],
                    HRESULT,
                    'GetUserState',
                    (['out'], POINTER(CorDebugUserState), 'pState'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCurrentException')],
                    HRESULT,
                    'GetCurrentException',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugValue)),
                        'ppExceptionObject'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method ClearCurrentException')],
                    HRESULT,
                    'ClearCurrentException',
                ),
                COMMETHOD(
                    [helpstring('Method CreateStepper')],
                    HRESULT,
                    'CreateStepper',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugStepper)),
                        'ppStepper'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateChains')],
                    HRESULT,
                    'EnumerateChains',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugChainEnum)),
                        'ppChains'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetActiveChain')],
                    HRESULT,
                    'GetActiveChain',
                    (['out'], POINTER(POINTER(ICorDebugChain)), 'ppChain'),
                ),
                COMMETHOD(
                    [helpstring('Method GetActiveFrame')],
                    HRESULT,
                    'GetActiveFrame',
                    (['out'], POINTER(POINTER(ICorDebugFrame)), 'ppFrame'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRegisterSet')],
                    HRESULT,
                    'GetRegisterSet',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugRegisterSet)),
                        'ppRegisters'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method CreateEval')],
                    HRESULT,
                    'CreateEval',
                    (['out'], POINTER(POINTER(ICorDebugEval)), 'ppEval'),
                ),
                COMMETHOD(
                    [helpstring('Method GetObject')],
                    HRESULT,
                    'GetObject',
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppObject'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugThread_INTERFACE_DEFINED__

    if not defined(__ICorDebugThread2_INTERFACE_DEFINED__):
        __ICorDebugThread2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugThread2
        # [unique][uuid][object]
        _COR_ACTIVE_FUNCTION._fields_ = [
            ('pAppDomain', POINTER(ICorDebugAppDomain)),
            ('pModule', POINTER(ICorDebugModule)),
            ('pFunction', POINTER(ICorDebugFunction2)),
            ('ilOffset', ULONG32),
            ('flags', ULONG32),
        ]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugThread2 = MIDL_INTERFACE(
                "{2BD956D9-7B07-4BEF-8A98-12AA862417C5}"
            )
            ICorDebugThread2._iid_ = IID_ICorDebugThread2

            ICorDebugThread2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetActiveFunctions')],
                    HRESULT,
                    'GetActiveFunctions',
                    (['in'], ULONG32, 'cFunctions'),
                    (['out'], POINTER(ULONG32), 'pcFunctions'),
                    (['in', 'out'], COR_ACTIVE_FUNCTION * 0, 'pFunctions'),
                ),
                COMMETHOD(
                    [helpstring('Method GetConnectionID')],
                    HRESULT,
                    'GetConnectionID',
                    (['out'], POINTER(CONNID), 'pdwConnectionId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetTaskID')],
                    HRESULT,
                    'GetTaskID',
                    (['out'], POINTER(TASKID), 'pTaskId'),
                ),
                COMMETHOD(
                    [helpstring('Method GetVolatileOSThreadID')],
                    HRESULT,
                    'GetVolatileOSThreadID',
                    (['out'], POINTER(DWORD), 'pdwTid'),
                ),
                COMMETHOD(
                    [helpstring('Method InterceptCurrentException')],
                    HRESULT,
                    'InterceptCurrentException',
                    (['in'], POINTER(ICorDebugFrame), 'pFrame'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugThread2_INTERFACE_DEFINED__

    if not defined(__ICorDebugChain_INTERFACE_DEFINED__):
        __ICorDebugChain_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugChain
        # [unique][uuid][object]
        class CorDebugChainReason(ENUM):
            CHAIN_NONE = 0
            CHAIN_CLASS_INIT = 0x1
            CHAIN_EXCEPTION_FILTER = 0x2
            CHAIN_SECURITY = 0x4
            CHAIN_CONTEXT_POLICY = 0x8
            CHAIN_INTERCEPTION = 0x10
            CHAIN_PROCESS_START = 0x20
            CHAIN_THREAD_START = 0x40
            CHAIN_ENTER_MANAGED = 0x80
            CHAIN_ENTER_UNMANAGED = 0x100
            CHAIN_DEBUGGER_EVAL = 0x200
            CHAIN_CONTEXT_SWITCH = 0x400
            CHAIN_FUNC_EVAL = 0x800

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugChain = MIDL_INTERFACE(
                "{CC7BCAEE-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugChain._iid_ = IID_ICorDebugChain

            ICorDebugChain._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetThread')],
                    HRESULT,
                    'GetThread',
                    (['out'], POINTER(POINTER(ICorDebugThread)), 'ppThread'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStackRange')],
                    HRESULT,
                    'GetStackRange',
                    (['out'], POINTER(CORDB_ADDRESS), 'pStart'),
                    (['out'], POINTER(CORDB_ADDRESS), 'pEnd'),
                ),
                COMMETHOD(
                    [helpstring('Method GetContext')],
                    HRESULT,
                    'GetContext',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugContext)),
                        'ppContext'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetCaller')],
                    HRESULT,
                    'GetCaller',
                    (['out'], POINTER(POINTER(ICorDebugChain)), 'ppChain'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCallee')],
                    HRESULT,
                    'GetCallee',
                    (['out'], POINTER(POINTER(ICorDebugChain)), 'ppChain'),
                ),
                COMMETHOD(
                    [helpstring('Method GetPrevious')],
                    HRESULT,
                    'GetPrevious',
                    (['out'], POINTER(POINTER(ICorDebugChain)), 'ppChain'),
                ),
                COMMETHOD(
                    [helpstring('Method GetNext')],
                    HRESULT,
                    'GetNext',
                    (['out'], POINTER(POINTER(ICorDebugChain)), 'ppChain'),
                ),
                COMMETHOD(
                    [helpstring('Method IsManaged')],
                    HRESULT,
                    'IsManaged',
                    (['out'], POINTER(BOOL), 'pManaged'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateFrames')],
                    HRESULT,
                    'EnumerateFrames',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFrameEnum)),
                        'ppFrames'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetActiveFrame')],
                    HRESULT,
                    'GetActiveFrame',
                    (['out'], POINTER(POINTER(ICorDebugFrame)), 'ppFrame'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRegisterSet')],
                    HRESULT,
                    'GetRegisterSet',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugRegisterSet)),
                        'ppRegisters'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetReason')],
                    HRESULT,
                    'GetReason',
                    (['out'], POINTER(CorDebugChainReason), 'pReason'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugChain_INTERFACE_DEFINED__

    if not defined(__ICorDebugFrame_INTERFACE_DEFINED__):
        __ICorDebugFrame_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugFrame
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugFrame = MIDL_INTERFACE(
                "{CC7BCAEF-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugFrame._iid_ = IID_ICorDebugFrame

            ICorDebugFrame._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetChain')],
                    HRESULT,
                    'GetChain',
                    (['out'], POINTER(POINTER(ICorDebugChain)), 'ppChain'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCode')],
                    HRESULT,
                    'GetCode',
                    (['out'], POINTER(POINTER(ICorDebugCode)), 'ppCode'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunction')],
                    HRESULT,
                    'GetFunction',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunction)),
                        'ppFunction'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionToken')],
                    HRESULT,
                    'GetFunctionToken',
                    (['out'], POINTER(mdMethodDef), 'pToken'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStackRange')],
                    HRESULT,
                    'GetStackRange',
                    (['out'], POINTER(CORDB_ADDRESS), 'pStart'),
                    (['out'], POINTER(CORDB_ADDRESS), 'pEnd'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCaller')],
                    HRESULT,
                    'GetCaller',
                    (['out'], POINTER(POINTER(ICorDebugFrame)), 'ppFrame'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCallee')],
                    HRESULT,
                    'GetCallee',
                    (['out'], POINTER(POINTER(ICorDebugFrame)), 'ppFrame'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateStepper')],
                    HRESULT,
                    'CreateStepper',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugStepper)),
                        'ppStepper'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugFrame_INTERFACE_DEFINED__

    if not defined(__ICorDebugInternalFrame_INTERFACE_DEFINED__):
        __ICorDebugInternalFrame_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugInternalFrame
        # [unique][uuid][object]
        class CorDebugInternalFrameType(ENUM):
            STUBFRAME_NONE = 0
            STUBFRAME_M2U = 0x1
            STUBFRAME_U2M = 0x2
            STUBFRAME_APPDOMAIN_TRANSITION = 0x3
            STUBFRAME_LIGHTWEIGHT_FUNCTION = 0x4
            STUBFRAME_FUNC_EVAL = 0x5
            STUBFRAME_INTERNALCALL = 0x6

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugInternalFrame = MIDL_INTERFACE(
                "{B92CC7F7-9D2D-45C4-BC2B-621FCC9DFBF4}"
            )
            ICorDebugInternalFrame._iid_ = IID_ICorDebugInternalFrame

            ICorDebugInternalFrame._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetFrameType')],
                    HRESULT,
                    'GetFrameType',
                    (['out'], POINTER(CorDebugInternalFrameType), 'pType'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugInternalFrame_INTERFACE_DEFINED__

    if not defined(__ICorDebugILFrame_INTERFACE_DEFINED__):
        __ICorDebugILFrame_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugILFrame
        # [unique][uuid][object]
        class CorDebugMappingResult(ENUM):
            MAPPING_PROLOG = 0x1
            MAPPING_EPILOG = 0x2
            MAPPING_NO_INFO = 0x4
            MAPPING_UNMAPPED_ADDRESS = 0x8
            MAPPING_EXACT = 0x10
            MAPPING_APPROXIMATE = 0x20

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugILFrame = MIDL_INTERFACE(
                "{03E26311-4F76-11D3-88C6-006097945418}"
            )
            ICorDebugILFrame._iid_ = IID_ICorDebugILFrame

            ICorDebugILFrame._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetIP')],
                    HRESULT,
                    'GetIP',
                    (['out'], POINTER(ULONG32), 'pnOffset'),
                    (
                        ['out'],
                        POINTER(CorDebugMappingResult),
                        'pMappingResult'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method SetIP')],
                    HRESULT,
                    'SetIP',
                    (['in'], ULONG32, 'nOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateLocalVariables')],
                    HRESULT,
                    'EnumerateLocalVariables',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugValueEnum)),
                        'ppValueEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalVariable')],
                    HRESULT,
                    'GetLocalVariable',
                    (['in'], DWORD, 'dwIndex'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateArguments')],
                    HRESULT,
                    'EnumerateArguments',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugValueEnum)),
                        'ppValueEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetArgument')],
                    HRESULT,
                    'GetArgument',
                    (['in'], DWORD, 'dwIndex'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStackDepth')],
                    HRESULT,
                    'GetStackDepth',
                    (['out'], POINTER(ULONG32), 'pDepth'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStackValue')],
                    HRESULT,
                    'GetStackValue',
                    (['in'], DWORD, 'dwIndex'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method CanSetIP')],
                    HRESULT,
                    'CanSetIP',
                    (['in'], ULONG32, 'nOffset'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugILFrame_INTERFACE_DEFINED__

    if not defined(__ICorDebugILFrame2_INTERFACE_DEFINED__):
        __ICorDebugILFrame2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugILFrame2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugILFrame2 = MIDL_INTERFACE(
                "{5D88A994-6C30-479B-890F-BCEF88B129A5}"
            )
            ICorDebugILFrame2._iid_ = IID_ICorDebugILFrame2

            ICorDebugILFrame2._methods_ = [
                COMMETHOD(
                    [helpstring('Method RemapFunction')],
                    HRESULT,
                    'RemapFunction',
                    (['in'], ULONG32, 'newILOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateTypeParameters')],
                    HRESULT,
                    'EnumerateTypeParameters',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugTypeEnum)),
                        'ppTyParEnum'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugILFrame2_INTERFACE_DEFINED__

    if not defined(__ICorDebugNativeFrame_INTERFACE_DEFINED__):
        __ICorDebugNativeFrame_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugNativeFrame
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugNativeFrame = MIDL_INTERFACE(
                "{03E26314-4F76-11D3-88C6-006097945418}"
            )
            ICorDebugNativeFrame._iid_ = IID_ICorDebugNativeFrame

            ICorDebugNativeFrame._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetIP')],
                    HRESULT,
                    'GetIP',
                    (['out'], POINTER(ULONG32), 'pnOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method SetIP')],
                    HRESULT,
                    'SetIP',
                    (['in'], ULONG32, 'nOffset'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRegisterSet')],
                    HRESULT,
                    'GetRegisterSet',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugRegisterSet)),
                        'ppRegisters'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalRegisterValue')],
                    HRESULT,
                    'GetLocalRegisterValue',
                    (['in'], CorDebugRegister, 'reg'),
                    (['in'], ULONG, 'cbSigBlob'),
                    (['in'], PCCOR_SIGNATURE, 'pvSigBlob'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalDoubleRegisterValue')],
                    HRESULT,
                    'GetLocalDoubleRegisterValue',
                    (['in'], CorDebugRegister, 'highWordReg'),
                    (['in'], CorDebugRegister, 'lowWordReg'),
                    (['in'], ULONG, 'cbSigBlob'),
                    (['in'], PCCOR_SIGNATURE, 'pvSigBlob'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalMemoryValue')],
                    HRESULT,
                    'GetLocalMemoryValue',
                    (['in'], CORDB_ADDRESS, 'address'),
                    (['in'], ULONG, 'cbSigBlob'),
                    (['in'], PCCOR_SIGNATURE, 'pvSigBlob'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalRegisterMemoryValue')],
                    HRESULT,
                    'GetLocalRegisterMemoryValue',
                    (['in'], CorDebugRegister, 'highWordReg'),
                    (['in'], CORDB_ADDRESS, 'lowWordAddress'),
                    (['in'], ULONG, 'cbSigBlob'),
                    (['in'], PCCOR_SIGNATURE, 'pvSigBlob'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalMemoryRegisterValue')],
                    HRESULT,
                    'GetLocalMemoryRegisterValue',
                    (['in'], CORDB_ADDRESS, 'highWordAddress'),
                    (['in'], CorDebugRegister, 'lowWordRegister'),
                    (['in'], ULONG, 'cbSigBlob'),
                    (['in'], PCCOR_SIGNATURE, 'pvSigBlob'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method CanSetIP')],
                    HRESULT,
                    'CanSetIP',
                    (['in'], ULONG32, 'nOffset'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugNativeFrame_INTERFACE_DEFINED__

    if not defined(__ICorDebugModule_INTERFACE_DEFINED__):
        __ICorDebugModule_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugModule
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugModule = MIDL_INTERFACE(
                "{DBA2D8C1-E5C5-4069-8C13-10A7C6ABF43D}"
            )
            ICorDebugModule._iid_ = IID_ICorDebugModule

            ICorDebugModule._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetProcess')],
                    HRESULT,
                    'GetProcess',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugProcess)),
                        'ppProcess'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetBaseAddress')],
                    HRESULT,
                    'GetBaseAddress',
                    (['out'], POINTER(CORDB_ADDRESS), 'pAddress'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAssembly')],
                    HRESULT,
                    'GetAssembly',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugAssembly)),
                        'ppAssembly'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method EnableJITDebugging')],
                    HRESULT,
                    'EnableJITDebugging',
                    (['in'], BOOL, 'bTrackJITInfo'),
                    (['in'], BOOL, 'bAllowJitOpts'),
                ),
                COMMETHOD(
                    [helpstring('Method EnableClassLoadCallbacks')],
                    HRESULT,
                    'EnableClassLoadCallbacks',
                    (['in'], BOOL, 'bClassLoadCallbacks'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionFromToken')],
                    HRESULT,
                    'GetFunctionFromToken',
                    (['in'], mdMethodDef, 'methodDef'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunction)),
                        'ppFunction'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunctionFromRVA')],
                    HRESULT,
                    'GetFunctionFromRVA',
                    (['in'], CORDB_ADDRESS, 'rva'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunction)),
                        'ppFunction'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetClassFromToken')],
                    HRESULT,
                    'GetClassFromToken',
                    (['in'], mdTypeDef, 'typeDef'),
                    (['out'], POINTER(POINTER(ICorDebugClass)), 'ppClass'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateBreakpoint')],
                    HRESULT,
                    'CreateBreakpoint',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugModuleBreakpoint)),
                        'ppBreakpoint'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetEditAndContinueSnapshot')],
                    HRESULT,
                    'GetEditAndContinueSnapshot',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugEditAndContinueSnapshot)),
                        'ppEditAndContinueSnapshot'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetMetaDataInterface')],
                    HRESULT,
                    'GetMetaDataInterface',
                    (['in'], REFIID, 'riid'),
                    (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppObj'),
                ),
                COMMETHOD(
                    [helpstring('Method GetToken')],
                    HRESULT,
                    'GetToken',
                    (['out'], POINTER(mdModule), 'pToken'),
                ),
                COMMETHOD(
                    [helpstring('Method IsDynamic')],
                    HRESULT,
                    'IsDynamic',
                    (['out'], POINTER(BOOL), 'pDynamic'),
                ),
                COMMETHOD(
                    [helpstring('Method GetGlobalVariableValue')],
                    HRESULT,
                    'GetGlobalVariableValue',
                    (['in'], mdFieldDef, 'fieldDef'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSize')],
                    HRESULT,
                    'GetSize',
                    (['out'], POINTER(ULONG32), 'pcBytes'),
                ),
                COMMETHOD(
                    [helpstring('Method IsInMemory')],
                    HRESULT,
                    'IsInMemory',
                    (['out'], POINTER(BOOL), 'pInMemory'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugModule_INTERFACE_DEFINED__

    if not defined(__ICorDebugModule2_INTERFACE_DEFINED__):
        __ICorDebugModule2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugModule2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugModule2 = MIDL_INTERFACE(
                "{7FCC5FB5-49C0-41DE-9938-3B88B5B9ADD7}"
            )
            ICorDebugModule2._iid_ = IID_ICorDebugModule2

            ICorDebugModule2._methods_ = [
                COMMETHOD(
                    [helpstring('Method SetJMCStatus')],
                    HRESULT,
                    'SetJMCStatus',
                    (['in'], BOOL, 'bIsJustMyCode'),
                    (['in'], ULONG32, 'cTokens'),
                    (['in'], mdToken * 0, 'pTokens'),
                ),
                COMMETHOD(
                    [helpstring('Method ApplyChanges')],
                    HRESULT,
                    'ApplyChanges',
                    (['in'], ULONG, 'cbMetadata'),
                    (['in'], BYTE * 0, 'pbMetadata'),
                    (['in'], ULONG, 'cbIL'),
                    (['in'], BYTE * 0, 'pbIL'),
                ),
                COMMETHOD(
                    [helpstring('Method SetJITCompilerFlags')],
                    HRESULT,
                    'SetJITCompilerFlags',
                    (['in'], DWORD, 'dwFlags'),
                ),
                COMMETHOD(
                    [helpstring('Method GetJITCompilerFlags')],
                    HRESULT,
                    'GetJITCompilerFlags',
                    (['out'], POINTER(DWORD), 'pdwFlags'),
                ),
                COMMETHOD(
                    [helpstring('Method ResolveAssembly')],
                    HRESULT,
                    'ResolveAssembly',
                    (['in'], mdToken, 'tkAssemblyRef'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugAssembly)),
                        'ppAssembly'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugModule2_INTERFACE_DEFINED__

    if not defined(__ICorDebugFunction_INTERFACE_DEFINED__):
        __ICorDebugFunction_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugFunction
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugFunction = MIDL_INTERFACE(
                "{CC7BCAF3-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugFunction._iid_ = IID_ICorDebugFunction

            ICorDebugFunction._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetModule')],
                    HRESULT,
                    'GetModule',
                    (['out'], POINTER(POINTER(ICorDebugModule)), 'ppModule'),
                ),
                COMMETHOD(
                    [helpstring('Method GetClass')],
                    HRESULT,
                    'GetClass',
                    (['out'], POINTER(POINTER(ICorDebugClass)), 'ppClass'),
                ),
                COMMETHOD(
                    [helpstring('Method GetToken')],
                    HRESULT,
                    'GetToken',
                    (['out'], POINTER(mdMethodDef), 'pMethodDef'),
                ),
                COMMETHOD(
                    [helpstring('Method GetILCode')],
                    HRESULT,
                    'GetILCode',
                    (['out'], POINTER(POINTER(ICorDebugCode)), 'ppCode'),
                ),
                COMMETHOD(
                    [helpstring('Method GetNativeCode')],
                    HRESULT,
                    'GetNativeCode',
                    (['out'], POINTER(POINTER(ICorDebugCode)), 'ppCode'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateBreakpoint')],
                    HRESULT,
                    'CreateBreakpoint',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunctionBreakpoint)),
                        'ppBreakpoint'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetLocalVarSigToken')],
                    HRESULT,
                    'GetLocalVarSigToken',
                    (['out'], POINTER(mdSignature), 'pmdSig'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCurrentVersionNumber')],
                    HRESULT,
                    'GetCurrentVersionNumber',
                    (['out'], POINTER(ULONG32), 'pnCurrentVersion'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugFunction_INTERFACE_DEFINED__

    if not defined(__ICorDebugFunction2_INTERFACE_DEFINED__):
        __ICorDebugFunction2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugFunction2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugFunction2 = MIDL_INTERFACE(
                "{EF0C490B-94C3-4E4D-B629-DDC134C532D8}"
            )
            ICorDebugFunction2._iid_ = IID_ICorDebugFunction2

            ICorDebugFunction2._methods_ = [
                COMMETHOD(
                    [helpstring('Method SetJMCStatus')],
                    HRESULT,
                    'SetJMCStatus',
                    (['in'], BOOL, 'bIsJustMyCode'),
                ),
                COMMETHOD(
                    [helpstring('Method GetJMCStatus')],
                    HRESULT,
                    'GetJMCStatus',
                    (['out'], POINTER(BOOL), 'pbIsJustMyCode'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateNativeCode')],
                    HRESULT,
                    'EnumerateNativeCode',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugCodeEnum)),
                        'ppCodeEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetVersionNumber')],
                    HRESULT,
                    'GetVersionNumber',
                    (['out'], POINTER(ULONG32), 'pnVersion'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugFunction2_INTERFACE_DEFINED__

    if not defined(__ICorDebugCode_INTERFACE_DEFINED__):
        __ICorDebugCode_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugCode
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugCode = MIDL_INTERFACE(
                "{CC7BCAF4-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugCode._iid_ = IID_ICorDebugCode

            ICorDebugCode._methods_ = [
                COMMETHOD(
                    [helpstring('Method IsIL')],
                    HRESULT,
                    'IsIL',
                    (['out'], POINTER(BOOL), 'pbIL'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFunction')],
                    HRESULT,
                    'GetFunction',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunction)),
                        'ppFunction'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetAddress')],
                    HRESULT,
                    'GetAddress',
                    (['out'], POINTER(CORDB_ADDRESS), 'pStart'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSize')],
                    HRESULT,
                    'GetSize',
                    (['out'], POINTER(ULONG32), 'pcBytes'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateBreakpoint')],
                    HRESULT,
                    'CreateBreakpoint',
                    (['in'], ULONG32, 'offset'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunctionBreakpoint)),
                        'ppBreakpoint'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetCode')],
                    HRESULT,
                    'GetCode',
                    (['in'], ULONG32, 'startOffset'),
                    (['in'], ULONG32, 'endOffset'),
                    (['in'], ULONG32, 'cBufferAlloc'),
                    (['out'], BYTE * 0, 'buffer'),
                    (['out'], POINTER(ULONG32), 'pcBufferSize'),
                ),
                COMMETHOD(
                    [helpstring('Method GetVersionNumber')],
                    HRESULT,
                    'GetVersionNumber',
                    (['out'], POINTER(ULONG32), 'nVersion'),
                ),
                COMMETHOD(
                    [helpstring('Method GetILToNativeMapping')],
                    HRESULT,
                    'GetILToNativeMapping',
                    (['in'], ULONG32, 'cMap'),
                    (['out'], POINTER(ULONG32), 'pcMap'),
                    (['out'], COR_DEBUG_IL_TO_NATIVE_MAP * 0, 'map'),
                ),
                COMMETHOD(
                    [helpstring('Method GetEnCRemapSequencePoints')],
                    HRESULT,
                    'GetEnCRemapSequencePoints',
                    (['in'], ULONG32, 'cMap'),
                    (['out'], POINTER(ULONG32), 'pcMap'),
                    (['out'], ULONG32 * 0, 'offsets'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugCode_INTERFACE_DEFINED__

    if not defined(__ICorDebugCode2_INTERFACE_DEFINED__):
        __ICorDebugCode2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugCode2
        # [unique][uuid][object]
        _CodeChunkInfo._fields_ = [
            ('startAddr', CORDB_ADDRESS),
            ('length', ULONG32),
        ]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugCode2 = MIDL_INTERFACE(
                "{5F696509-452F-4436-A3FE-4D11FE7E2347}"
            )
            ICorDebugCode2._iid_ = IID_ICorDebugCode2

            ICorDebugCode2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetCodeChunks')],
                    HRESULT,
                    'GetCodeChunks',
                    (['in'], ULONG32, 'cbufSize'),
                    (['out'], POINTER(ULONG32), 'pcnumChunks'),
                    (['out'], CodeChunkInfo * 0, 'chunks'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCompilerFlags')],
                    HRESULT,
                    'GetCompilerFlags',
                    (['out'], POINTER(DWORD), 'pdwFlags'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugCode2_INTERFACE_DEFINED__

    if not defined(__ICorDebugClass_INTERFACE_DEFINED__):
        __ICorDebugClass_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugClass
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugClass = MIDL_INTERFACE(
                "{CC7BCAF5-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugClass._iid_ = IID_ICorDebugClass

            ICorDebugClass._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetModule')],
                    HRESULT,
                    'GetModule',
                    (['out'], POINTER(POINTER(ICorDebugModule)), 'pModule'),
                ),
                COMMETHOD(
                    [helpstring('Method GetToken')],
                    HRESULT,
                    'GetToken',
                    (['out'], POINTER(mdTypeDef), 'pTypeDef'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStaticFieldValue')],
                    HRESULT,
                    'GetStaticFieldValue',
                    (['in'], mdFieldDef, 'fieldDef'),
                    (['in'], POINTER(ICorDebugFrame), 'pFrame'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugClass_INTERFACE_DEFINED__

    if not defined(__ICorDebugClass2_INTERFACE_DEFINED__):
        __ICorDebugClass2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugClass2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugClass2 = MIDL_INTERFACE(
                "{B008EA8D-7AB1-43F7-BB20-FBB5A04038AE}"
            )
            ICorDebugClass2._iid_ = IID_ICorDebugClass2

            ICorDebugClass2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetParameterizedType')],
                    HRESULT,
                    'GetParameterizedType',
                    (['in'], CorElementType, 'elementType'),
                    (['in'], ULONG32, 'nTypeArgs'),
                    (['in'], POINTER(ICorDebugType * 0), 'ppTypeArgs'),
                    (['out'], POINTER(POINTER(ICorDebugType)), 'ppType'),
                ),
                COMMETHOD(
                    [helpstring('Method SetJMCStatus')],
                    HRESULT,
                    'SetJMCStatus',
                    (['in'], BOOL, 'bIsJustMyCode'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugClass2_INTERFACE_DEFINED__

    if not defined(__ICorDebugEval_INTERFACE_DEFINED__):
        __ICorDebugEval_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugEval
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugEval = MIDL_INTERFACE(
                "{CC7BCAF6-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugEval._iid_ = IID_ICorDebugEval

            ICorDebugEval._methods_ = [
                COMMETHOD(
                    [helpstring('Method CallFunction')],
                    HRESULT,
                    'CallFunction',
                    (['in'], POINTER(ICorDebugFunction), 'pFunction'),
                    (['in'], ULONG32, 'nArgs'),
                    (['in'], POINTER(ICorDebugValue * 0), 'ppArgs'),
                ),
                COMMETHOD(
                    [helpstring('Method NewObject')],
                    HRESULT,
                    'NewObject',
                    (['in'], POINTER(ICorDebugFunction), 'pConstructor'),
                    (['in'], ULONG32, 'nArgs'),
                    (['in'], POINTER(ICorDebugValue * 0), 'ppArgs'),
                ),
                COMMETHOD(
                    [helpstring('Method NewObjectNoConstructor')],
                    HRESULT,
                    'NewObjectNoConstructor',
                    (['in'], POINTER(ICorDebugClass), 'pClass'),
                ),
                COMMETHOD(
                    [helpstring('Method NewString')],
                    HRESULT,
                    'NewString',
                    (['in'], LPCWSTR, 'string'),
                ),
                COMMETHOD(
                    [helpstring('Method NewArray')],
                    HRESULT,
                    'NewArray',
                    (['in'], CorElementType, 'elementType'),
                    (['in'], POINTER(ICorDebugClass), 'pElementClass'),
                    (['in'], ULONG32, 'rank'),
                    (['in'], ULONG32 * 0, 'dims'),
                    (['in'], ULONG32 * 0, 'lowBounds'),
                ),
                COMMETHOD(
                    [helpstring('Method IsActive')],
                    HRESULT,
                    'IsActive',
                    (['out'], POINTER(BOOL), 'pbActive'),
                ),
                COMMETHOD(
                    [helpstring('Method Abort')],
                    HRESULT,
                    'Abort',
                ),
                COMMETHOD(
                    [helpstring('Method GetResult')],
                    HRESULT,
                    'GetResult',
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppResult'),
                ),
                COMMETHOD(
                    [helpstring('Method GetThread')],
                    HRESULT,
                    'GetThread',
                    (['out'], POINTER(POINTER(ICorDebugThread)), 'ppThread'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateValue')],
                    HRESULT,
                    'CreateValue',
                    (['in'], CorElementType, 'elementType'),
                    (['in'], POINTER(ICorDebugClass), 'pElementClass'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugEval_INTERFACE_DEFINED__

    if not defined(__ICorDebugEval2_INTERFACE_DEFINED__):
        __ICorDebugEval2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugEval2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugEval2 = MIDL_INTERFACE(
                "{FB0D9CE7-BE66-4683-9D32-A42A04E2FD91}"
            )
            ICorDebugEval2._iid_ = IID_ICorDebugEval2

            ICorDebugEval2._methods_ = [
                COMMETHOD(
                    [helpstring('Method CallParameterizedFunction')],
                    HRESULT,
                    'CallParameterizedFunction',
                    (['in'], POINTER(ICorDebugFunction), 'pFunction'),
                    (['in'], ULONG32, 'nTypeArgs'),
                    (['in'], POINTER(ICorDebugType * 0), 'ppTypeArgs'),
                    (['in'], ULONG32, 'nArgs'),
                    (['in'], POINTER(ICorDebugValue * 0), 'ppArgs'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateValueForType')],
                    HRESULT,
                    'CreateValueForType',
                    (['in'], POINTER(ICorDebugType), 'pType'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method NewParameterizedObject')],
                    HRESULT,
                    'NewParameterizedObject',
                    (['in'], POINTER(ICorDebugFunction), 'pConstructor'),
                    (['in'], ULONG32, 'nTypeArgs'),
                    (['in'], POINTER(ICorDebugType * 0), 'ppTypeArgs'),
                    (['in'], ULONG32, 'nArgs'),
                    (['in'], POINTER(ICorDebugValue * 0), 'ppArgs'),
                ),
                COMMETHOD(
                    [helpstring('Method NewParameterizedObjectNoConstructor')],
                    HRESULT,
                    'NewParameterizedObjectNoConstructor',
                    (['in'], POINTER(ICorDebugClass), 'pClass'),
                    (['in'], ULONG32, 'nTypeArgs'),
                    (['in'], POINTER(ICorDebugType * 0), 'ppTypeArgs'),
                ),
                COMMETHOD(
                    [helpstring('Method NewParameterizedArray')],
                    HRESULT,
                    'NewParameterizedArray',
                    (['in'], POINTER(ICorDebugType), 'pElementType'),
                    (['in'], ULONG32, 'rank'),
                    (['in'], ULONG32 * 0, 'dims'),
                    (['in'], ULONG32 * 0, 'lowBounds'),
                ),
                COMMETHOD(
                    [helpstring('Method NewStringWithLength')],
                    HRESULT,
                    'NewStringWithLength',
                    (['in'], LPCWSTR, 'string'),
                    (['in'], UINT, 'uiLength'),
                ),
                COMMETHOD(
                    [helpstring('Method RudeAbort')],
                    HRESULT,
                    'RudeAbort',
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugEval2_INTERFACE_DEFINED__

    if not defined(__ICorDebugValue_INTERFACE_DEFINED__):
        __ICorDebugValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugValue = MIDL_INTERFACE(
                "{CC7BCAF7-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugValue._iid_ = IID_ICorDebugValue

            ICorDebugValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetType')],
                    HRESULT,
                    'GetType',
                    (['out'], POINTER(CorElementType), 'pType'),
                ),
                COMMETHOD(
                    [helpstring('Method GetSize')],
                    HRESULT,
                    'GetSize',
                    (['out'], POINTER(ULONG32), 'pSize'),
                ),
                COMMETHOD(
                    [helpstring('Method GetAddress')],
                    HRESULT,
                    'GetAddress',
                    (['out'], POINTER(CORDB_ADDRESS), 'pAddress'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateBreakpoint')],
                    HRESULT,
                    'CreateBreakpoint',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugValueBreakpoint)),
                        'ppBreakpoint'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugValue_INTERFACE_DEFINED__
    if not defined(__ICorDebugValue2_INTERFACE_DEFINED__):
        __ICorDebugValue2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugValue2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugValue2 = MIDL_INTERFACE(
                "{5E0B54E7-D88A-4626-9420-A691E0A78B49}"
            )
            ICorDebugValue2._iid_ = IID_ICorDebugValue2

            ICorDebugValue2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetExactType')],
                    HRESULT,
                    'GetExactType',
                    (['out'], POINTER(POINTER(ICorDebugType)), 'ppType'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugValue2_INTERFACE_DEFINED__

    if not defined(__ICorDebugGenericValue_INTERFACE_DEFINED__):
        __ICorDebugGenericValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugGenericValue
        # [unique][uuid][local][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugGenericValue = MIDL_INTERFACE(
                "{CC7BCAF8-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugGenericValue._iid_ = IID_ICorDebugGenericValue

            ICorDebugGenericValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetValue')],
                    HRESULT,
                    'GetValue',
                    (['out'], POINTER(VOID), 'pTo'),
                ),
                COMMETHOD(
                    [helpstring('Method SetValue')],
                    HRESULT,
                    'SetValue',
                    (['in'], POINTER(VOID), 'pFrom'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugGenericValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugReferenceValue_INTERFACE_DEFINED__):
        __ICorDebugReferenceValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugReferenceValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugReferenceValue = MIDL_INTERFACE(
                "{CC7BCAF9-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugReferenceValue._iid_ = IID_ICorDebugReferenceValue

            ICorDebugReferenceValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method IsNull')],
                    HRESULT,
                    'IsNull',
                    (['out'], POINTER(BOOL), 'pbNull'),
                ),
                COMMETHOD(
                    [helpstring('Method GetValue')],
                    HRESULT,
                    'GetValue',
                    (['out'], POINTER(CORDB_ADDRESS), 'pValue'),
                ),
                COMMETHOD(
                    [helpstring('Method SetValue')],
                    HRESULT,
                    'SetValue',
                    (['in'], CORDB_ADDRESS, 'value'),
                ),
                COMMETHOD(
                    [helpstring('Method Dereference')],
                    HRESULT,
                    'Dereference',
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method DereferenceStrong')],
                    HRESULT,
                    'DereferenceStrong',
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugReferenceValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugHeapValue_INTERFACE_DEFINED__):
        __ICorDebugHeapValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugHeapValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugHeapValue = MIDL_INTERFACE(
                "{CC7BCAFA-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugHeapValue._iid_ = IID_ICorDebugHeapValue

            ICorDebugHeapValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method IsValid')],
                    HRESULT,
                    'IsValid',
                    (['out'], POINTER(BOOL), 'pbValid'),
                ),
                COMMETHOD(
                    [helpstring('Method CreateRelocBreakpoint')],
                    HRESULT,
                    'CreateRelocBreakpoint',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugValueBreakpoint)),
                        'ppBreakpoint'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugHeapValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugHeapValue2_INTERFACE_DEFINED__):
        __ICorDebugHeapValue2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugHeapValue2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugHeapValue2 = MIDL_INTERFACE(
                "{E3AC4D6C-9CB7-43E6-96CC-B21540E5083C}"
            )
            ICorDebugHeapValue2._iid_ = IID_ICorDebugHeapValue2

            ICorDebugHeapValue2._methods_ = [
                COMMETHOD(
                    [helpstring('Method CreateHandle')],
                    HRESULT,
                    'CreateHandle',
                    (['in'], CorDebugHandleType, 'type'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugHandleValue)),
                        'ppHandle'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugHeapValue2_INTERFACE_DEFINED__

    if not defined(__ICorDebugObjectValue_INTERFACE_DEFINED__):
        __ICorDebugObjectValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugObjectValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugObjectValue = MIDL_INTERFACE(
                "{18AD3D6E-B7D2-11D2-BD04-0000F80849BD}"
            )
            ICorDebugObjectValue._iid_ = IID_ICorDebugObjectValue

            ICorDebugObjectValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetClass')],
                    HRESULT,
                    'GetClass',
                    (['out'], POINTER(POINTER(ICorDebugClass)), 'ppClass'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFieldValue')],
                    HRESULT,
                    'GetFieldValue',
                    (['in'], POINTER(ICorDebugClass), 'pClass'),
                    (['in'], mdFieldDef, 'fieldDef'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetVirtualMethod')],
                    HRESULT,
                    'GetVirtualMethod',
                    (['in'], mdMemberRef, 'memberRef'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunction)),
                        'ppFunction'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetContext')],
                    HRESULT,
                    'GetContext',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugContext)),
                        'ppContext'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method IsValueClass')],
                    HRESULT,
                    'IsValueClass',
                    (['out'], POINTER(BOOL), 'pbIsValueClass'),
                ),
                COMMETHOD(
                    [helpstring('Method GetManagedCopy')],
                    HRESULT,
                    'GetManagedCopy',
                    (
                        ['out'],
                        POINTER(POINTER(comtypes.IUnknown)),
                        'ppObject'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method SetFromManagedCopy')],
                    HRESULT,
                    'SetFromManagedCopy',
                    (['in'], POINTER(comtypes.IUnknown), 'pObject'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugObjectValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugObjectValue2_INTERFACE_DEFINED__):
        __ICorDebugObjectValue2_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugObjectValue2
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugObjectValue2 = MIDL_INTERFACE(
                "{49E4A320-4A9B-4ECA-B105-229FB7D5009F}"
            )
            ICorDebugObjectValue2._iid_ = IID_ICorDebugObjectValue2

            ICorDebugObjectValue2._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetVirtualMethodAndType')],
                    HRESULT,
                    'GetVirtualMethodAndType',
                    (['in'], mdMemberRef, 'memberRef'),
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugFunction)),
                        'ppFunction'
                    ),
                    (['out'], POINTER(POINTER(ICorDebugType)), 'ppType'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugObjectValue2_INTERFACE_DEFINED__

    if not defined(__ICorDebugBoxValue_INTERFACE_DEFINED__):
        __ICorDebugBoxValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugBoxValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugBoxValue = MIDL_INTERFACE(
                "{CC7BCAFC-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugBoxValue._iid_ = IID_ICorDebugBoxValue

            ICorDebugBoxValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetObject')],
                    HRESULT,
                    'GetObject',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugObjectValue)),
                        'ppObject'
                    ),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugBoxValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugStringValue_INTERFACE_DEFINED__):
        __ICorDebugStringValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugStringValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugStringValue = MIDL_INTERFACE(
                "{CC7BCAFD-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugStringValue._iid_ = IID_ICorDebugStringValue

            ICorDebugStringValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetLength')],
                    HRESULT,
                    'GetLength',
                    (['out'], POINTER(ULONG32), 'pcchString'),
                ),
                COMMETHOD(
                    [helpstring('Method GetString')],
                    HRESULT,
                    'GetString',
                    (['in'], ULONG32, 'cchString'),
                    (['out'], POINTER(ULONG32), 'pcchString'),
                    (['out'], WCHAR * 0, 'szString'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugStringValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugArrayValue_INTERFACE_DEFINED__):
        __ICorDebugArrayValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugArrayValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugArrayValue = MIDL_INTERFACE(
                "{0405B0DF-A660-11D2-BD02-0000F80849BD}"
            )
            ICorDebugArrayValue._iid_ = IID_ICorDebugArrayValue

            ICorDebugArrayValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetElementType')],
                    HRESULT,
                    'GetElementType',
                    (['out'], POINTER(CorElementType), 'pType'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRank')],
                    HRESULT,
                    'GetRank',
                    (['out'], POINTER(ULONG32), 'pnRank'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCount')],
                    HRESULT,
                    'GetCount',
                    (['out'], POINTER(ULONG32), 'pnCount'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDimensions')],
                    HRESULT,
                    'GetDimensions',
                    (['in'], ULONG32, 'cdim'),
                    (['out'], ULONG32 * 0, 'dims'),
                ),
                COMMETHOD(
                    [helpstring('Method HasBaseIndicies')],
                    HRESULT,
                    'HasBaseIndicies',
                    (['out'], POINTER(BOOL), 'pbHasBaseIndicies'),
                ),
                COMMETHOD(
                    [helpstring('Method GetBaseIndicies')],
                    HRESULT,
                    'GetBaseIndicies',
                    (['in'], ULONG32, 'cdim'),
                    (['out'], ULONG32 * 0, 'indicies'),
                ),
                COMMETHOD(
                    [helpstring('Method GetElement')],
                    HRESULT,
                    'GetElement',
                    (['in'], ULONG32, 'cdim'),
                    (['in'], ULONG32 * 0, 'indices'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetElementAtPosition')],
                    HRESULT,
                    'GetElementAtPosition',
                    (['in'], ULONG32, 'nPosition'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugArrayValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugHandleValue_INTERFACE_DEFINED__):
        __ICorDebugHandleValue_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugHandleValue
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugHandleValue = MIDL_INTERFACE(
                "{029596E8-276B-46A1-9821-732E96BBB00B}"
            )
            ICorDebugHandleValue._iid_ = IID_ICorDebugHandleValue

            ICorDebugHandleValue._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetHandleType')],
                    HRESULT,
                    'GetHandleType',
                    (['out'], POINTER(CorDebugHandleType), 'pType'),
                ),
                COMMETHOD(
                    [helpstring('Method Dispose')],
                    HRESULT,
                    'Dispose',
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugHandleValue_INTERFACE_DEFINED__

    if not defined(__ICorDebugContext_INTERFACE_DEFINED__):
        __ICorDebugContext_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugContext
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugContext = MIDL_INTERFACE(
                "{CC7BCB00-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugContext._iid_ = IID_ICorDebugContext

            ICorDebugContext._methods_ = []


        # END IF  C style interface
    # END IF  __ICorDebugContext_INTERFACE_DEFINED__

    if not defined(__ICorDebugEnum_INTERFACE_DEFINED__):
        __ICorDebugEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugEnum = MIDL_INTERFACE(
                "{CC7BCB01-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugEnum._iid_ = IID_ICorDebugEnum

            ICorDebugEnum._methods_ = [
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
                    (['out'], POINTER(POINTER(ICorDebugEnum)), 'ppEnum'),
                ),
                COMMETHOD(
                    [helpstring('Method GetCount')],
                    HRESULT,
                    'GetCount',
                    (['out'], POINTER(ULONG), 'pcelt'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugObjectEnum_INTERFACE_DEFINED__):
        __ICorDebugObjectEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugObjectEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugObjectEnum = MIDL_INTERFACE(
                "{CC7BCB02-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugObjectEnum._iid_ = IID_ICorDebugObjectEnum

            ICorDebugObjectEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], CORDB_ADDRESS * 0, 'objects'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugObjectEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugBreakpointEnum_INTERFACE_DEFINED__):
        __ICorDebugBreakpointEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugBreakpointEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugBreakpointEnum = MIDL_INTERFACE(
                "{CC7BCB03-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugBreakpointEnum._iid_ = IID_ICorDebugBreakpointEnum

            ICorDebugBreakpointEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (
                        ['out'],
                        POINTER(ICorDebugBreakpoint * 0),
                        'breakpoints'
                    ),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugBreakpointEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugStepperEnum_INTERFACE_DEFINED__):
        __ICorDebugStepperEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugStepperEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugStepperEnum = MIDL_INTERFACE(
                "{CC7BCB04-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugStepperEnum._iid_ = IID_ICorDebugStepperEnum

            ICorDebugStepperEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugStepper * 0), 'steppers'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugStepperEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugProcessEnum_INTERFACE_DEFINED__):
        __ICorDebugProcessEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugProcessEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugProcessEnum = MIDL_INTERFACE(
                "{CC7BCB05-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugProcessEnum._iid_ = IID_ICorDebugProcessEnum

            ICorDebugProcessEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugProcess * 0), 'processes'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugProcessEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugThreadEnum_INTERFACE_DEFINED__):
        __ICorDebugThreadEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugThreadEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugThreadEnum = MIDL_INTERFACE(
                "{CC7BCB06-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugThreadEnum._iid_ = IID_ICorDebugThreadEnum

            ICorDebugThreadEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugThread * 0), 'threads'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugThreadEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugFrameEnum_INTERFACE_DEFINED__):
        __ICorDebugFrameEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugFrameEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugFrameEnum = MIDL_INTERFACE(
                "{CC7BCB07-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugFrameEnum._iid_ = IID_ICorDebugFrameEnum

            ICorDebugFrameEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugFrame * 0), 'frames'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugFrameEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugChainEnum_INTERFACE_DEFINED__):
        __ICorDebugChainEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugChainEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugChainEnum = MIDL_INTERFACE(
                "{CC7BCB08-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugChainEnum._iid_ = IID_ICorDebugChainEnum

            ICorDebugChainEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugChain * 0), 'chains'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugChainEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugModuleEnum_INTERFACE_DEFINED__):
        __ICorDebugModuleEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugModuleEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugModuleEnum = MIDL_INTERFACE(
                "{CC7BCB09-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugModuleEnum._iid_ = IID_ICorDebugModuleEnum

            ICorDebugModuleEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugModule * 0), 'modules'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugModuleEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugValueEnum_INTERFACE_DEFINED__):
        __ICorDebugValueEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugValueEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugValueEnum = MIDL_INTERFACE(
                "{CC7BCB0A-8A68-11D2-983C-0000F808342D}"
            )
            ICorDebugValueEnum._iid_ = IID_ICorDebugValueEnum

            ICorDebugValueEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugValue * 0), 'values'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugValueEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugCodeEnum_INTERFACE_DEFINED__):
        __ICorDebugCodeEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugCodeEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugCodeEnum = MIDL_INTERFACE(
                "{55E96461-9645-45E4-A2FF-0367877ABCDE}"
            )
            ICorDebugCodeEnum._iid_ = IID_ICorDebugCodeEnum

            ICorDebugCodeEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugCode * 0), 'values'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugCodeEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugTypeEnum_INTERFACE_DEFINED__):
        __ICorDebugTypeEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugTypeEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugTypeEnum = MIDL_INTERFACE(
                "{10F27499-9DF2-43CE-8333-A321D7C99CB4}"
            )
            ICorDebugTypeEnum._iid_ = IID_ICorDebugTypeEnum

            ICorDebugTypeEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugType * 0), 'values'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugTypeEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugType_INTERFACE_DEFINED__):
        __ICorDebugType_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugType
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugType = MIDL_INTERFACE(
                "{D613F0BB-ACE1-4C19-BD72-E4C08D5DA7F5}"
            )
            ICorDebugType._iid_ = IID_ICorDebugType

            ICorDebugType._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetType')],
                    HRESULT,
                    'GetType',
                    (['out'], POINTER(CorElementType), 'ty'),
                ),
                COMMETHOD(
                    [helpstring('Method GetClass')],
                    HRESULT,
                    'GetClass',
                    (['out'], POINTER(POINTER(ICorDebugClass)), 'ppClass'),
                ),
                COMMETHOD(
                    [helpstring('Method EnumerateTypeParameters')],
                    HRESULT,
                    'EnumerateTypeParameters',
                    (
                        ['out'],
                        POINTER(POINTER(ICorDebugTypeEnum)),
                        'ppTyParEnum'
                    ),
                ),
                COMMETHOD(
                    [helpstring('Method GetFirstTypeParameter')],
                    HRESULT,
                    'GetFirstTypeParameter',
                    (['out'], POINTER(POINTER(ICorDebugType)), 'value'),
                ),
                COMMETHOD(
                    [helpstring('Method GetBase')],
                    HRESULT,
                    'GetBase',
                    (['out'], POINTER(POINTER(ICorDebugType)), 'pBase'),
                ),
                COMMETHOD(
                    [helpstring('Method GetStaticFieldValue')],
                    HRESULT,
                    'GetStaticFieldValue',
                    (['in'], mdFieldDef, 'fieldDef'),
                    (['in'], POINTER(ICorDebugFrame), 'pFrame'),
                    (['out'], POINTER(POINTER(ICorDebugValue)), 'ppValue'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRank')],
                    HRESULT,
                    'GetRank',
                    (['out'], POINTER(ULONG32), 'pnRank'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugType_INTERFACE_DEFINED__

    if not defined(__ICorDebugErrorInfoEnum_INTERFACE_DEFINED__):
        __ICorDebugErrorInfoEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugErrorInfoEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugErrorInfoEnum = MIDL_INTERFACE(
                "{F0E18809-72B5-11D2-976F-00A0C9B4D50C}"
            )
            ICorDebugErrorInfoEnum._iid_ = IID_ICorDebugErrorInfoEnum

            ICorDebugErrorInfoEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (
                        ['out'],
                        POINTER(ICorDebugEditAndContinueErrorInfo * 0),
                        'errors'
                    ),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugErrorInfoEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugAppDomainEnum_INTERFACE_DEFINED__):
        __ICorDebugAppDomainEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugAppDomainEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugAppDomainEnum = MIDL_INTERFACE(
                "{63CA1B24-4359-4883-BD57-13F815F58744}"
            )
            ICorDebugAppDomainEnum._iid_ = IID_ICorDebugAppDomainEnum

            ICorDebugAppDomainEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugAppDomain * 0), 'values'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugAppDomainEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugAssemblyEnum_INTERFACE_DEFINED__):
        __ICorDebugAssemblyEnum_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugAssemblyEnum
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugAssemblyEnum = MIDL_INTERFACE(
                "{4A2A1EC9-85EC-4BFB-9F15-A89FDFE0FE83}"
            )
            ICorDebugAssemblyEnum._iid_ = IID_ICorDebugAssemblyEnum

            ICorDebugAssemblyEnum._methods_ = [
                COMMETHOD(
                    [helpstring('Method Next')],
                    HRESULT,
                    'Next',
                    (['in'], ULONG, 'celt'),
                    (['out'], POINTER(ICorDebugAssembly * 0), 'values'),
                    (['out'], POINTER(ULONG), 'pceltFetched'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugAssemblyEnum_INTERFACE_DEFINED__

    if not defined(__ICorDebugMDA_INTERFACE_DEFINED__):
        __ICorDebugMDA_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugMDA
        # [unique][uuid][object]
        class CorDebugMDAFlags(ENUM):
            MDA_FLAG_SLIP = 0x2

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugMDA = MIDL_INTERFACE(
                "{CC726F2F-1DB7-459B-B0EC-05F01D841B42}"
            )
            ICorDebugMDA._iid_ = IID_ICorDebugMDA

            ICorDebugMDA._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetName')],
                    HRESULT,
                    'GetName',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetDescription')],
                    HRESULT,
                    'GetDescription',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetXML')],
                    HRESULT,
                    'GetXML',
                    (['in'], ULONG32, 'cchName'),
                    (['out'], POINTER(ULONG32), 'pcchName'),
                    (['out'], WCHAR * 0, 'szName'),
                ),
                COMMETHOD(
                    [helpstring('Method GetFlags')],
                    HRESULT,
                    'GetFlags',
                    (['in'], POINTER(CorDebugMDAFlags), 'pFlags'),
                ),
                COMMETHOD(
                    [helpstring('Method GetOSThreadId')],
                    HRESULT,
                    'GetOSThreadId',
                    (['out'], POINTER(DWORD), 'pOsTid'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugMDA_INTERFACE_DEFINED__

    if not defined(__ICorDebugEditAndContinueErrorInfo_INTERFACE_DEFINED__):
        __ICorDebugEditAndContinueErrorInfo_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugEditAndContinueErrorInfo
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugEditAndContinueErrorInfo = MIDL_INTERFACE(
                "{8D600D41-F4F6-4CB3-B7EC-7BD164944036}"
            )
            ICorDebugEditAndContinueErrorInfo._iid_ = IID_ICorDebugEditAndContinueErrorInfo

            ICorDebugEditAndContinueErrorInfo._methods_ = [
                COMMETHOD(
                    [helpstring('Method GetModule')],
                    HRESULT,
                    'GetModule',
                    (['out'], POINTER(POINTER(ICorDebugModule)), 'ppModule'),
                ),
                COMMETHOD(
                    [helpstring('Method GetToken')],
                    HRESULT,
                    'GetToken',
                    (['out'], POINTER(mdToken), 'pToken'),
                ),
                COMMETHOD(
                    [helpstring('Method GetErrorCode')],
                    HRESULT,
                    'GetErrorCode',
                    (['out'], POINTER(HRESULT), 'pHr'),
                ),
                COMMETHOD(
                    [helpstring('Method GetString')],
                    HRESULT,
                    'GetString',
                    (['in'], ULONG32, 'cchString'),
                    (['out'], POINTER(ULONG32), 'pcchString'),
                    (['out'], WCHAR * 0, 'szString'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugEditAndContinueErrorInfo_INTERFACE_DEFINED__

    if not defined(__ICorDebugEditAndContinueSnapshot_INTERFACE_DEFINED__):
        __ICorDebugEditAndContinueSnapshot_INTERFACE_DEFINED__ = VOID

        # interface ICorDebugEditAndContinueSnapshot
        # [unique][uuid][object]
        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else:
            IID_ICorDebugEditAndContinueSnapshot = MIDL_INTERFACE(
                "{6DC3FA01-D7CB-11D2-8A95-0080C792E5D8}"
            )
            ICorDebugEditAndContinueSnapshot._iid_ = IID_ICorDebugEditAndContinueSnapshot

            ICorDebugEditAndContinueSnapshot._methods_ = [
                COMMETHOD(
                    [helpstring('Method CopyMetaData')],
                    HRESULT,
                    'CopyMetaData',
                    (['in'], POINTER(IStream), 'pIStream'),
                    (['out'], POINTER(GUID), 'pMvid'),
                ),
                COMMETHOD(
                    [helpstring('Method GetMvid')],
                    HRESULT,
                    'GetMvid',
                    (['out'], POINTER(GUID), 'pMvid'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRoDataRVA')],
                    HRESULT,
                    'GetRoDataRVA',
                    (['out'], POINTER(ULONG32), 'pRoDataRVA'),
                ),
                COMMETHOD(
                    [helpstring('Method GetRwDataRVA')],
                    HRESULT,
                    'GetRwDataRVA',
                    (['out'], POINTER(ULONG32), 'pRwDataRVA'),
                ),
                COMMETHOD(
                    [helpstring('Method SetPEBytes')],
                    HRESULT,
                    'SetPEBytes',
                    (['in'], POINTER(IStream), 'pIStream'),
                ),
                COMMETHOD(
                    [helpstring('Method SetILMap')],
                    HRESULT,
                    'SetILMap',
                    (['in'], mdToken, 'mdFunction'),
                    (['in'], ULONG, 'cMapSize'),
                    (['in'], COR_IL_MAP * 0, 'map'),
                ),
                COMMETHOD(
                    [helpstring('Method SetPESymbolBytes')],
                    HRESULT,
                    'SetPESymbolBytes',
                    (['in'], POINTER(IStream), 'pIStream'),
                ),
            ]

        # END IF  C style interface
    # END IF  __ICorDebugEditAndContinueSnapshot_INTERFACE_DEFINED__

    if not defined(__CORDBLib_LIBRARY_DEFINED__):
        __CORDBLib_LIBRARY_DEFINED__ = VOID

        # library CORDBLib
        # [helpstring][version][uuid]
        if defined(__cplusplus):
            pass
        # END IF


        if defined(__cplusplus):
            pass
        # END IF

    # END IF  __CORDBLib_LIBRARY_DEFINED__

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


