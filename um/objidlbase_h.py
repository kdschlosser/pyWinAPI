import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

helpstring = comtypes.helpstring
COMMMETHOD = comtypes.COMMETHOD


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__objidlbase_h__ = None
__IMarshal_FWD_DEFINED__ = None
__INoMarshal_FWD_DEFINED__ = None
__IAgileObject_FWD_DEFINED__ = None
__IActivationFilter_FWD_DEFINED__ = None
__IMarshal2_FWD_DEFINED__ = None
__IMalloc_FWD_DEFINED__ = None
__IStdMarshalInfo_FWD_DEFINED__ = None
__IExternalConnection_FWD_DEFINED__ = None
__IMultiQI_FWD_DEFINED__ = None
__AsyncIMultiQI_FWD_DEFINED__ = None
__IInternalUnknown_FWD_DEFINED__ = None
__IEnumUnknown_FWD_DEFINED__ = None
__IEnumString_FWD_DEFINED__ = None
__ISequentialStream_FWD_DEFINED__ = None
__IStream_FWD_DEFINED__ = None
__IRpcChannelBuffer_FWD_DEFINED__ = None
__IRpcChannelBuffer2_FWD_DEFINED__ = None
__IAsyncRpcChannelBuffer_FWD_DEFINED__ = None
__IRpcChannelBuffer3_FWD_DEFINED__ = None
__IRpcSyntaxNegotiate_FWD_DEFINED__ = None
__IRpcProxyBuffer_FWD_DEFINED__ = None
__IRpcStubBuffer_FWD_DEFINED__ = None
__IPSFactoryBuffer_FWD_DEFINED__ = None
__IChannelHook_FWD_DEFINED__ = None
__IClientSecurity_FWD_DEFINED__ = None
__IServerSecurity_FWD_DEFINED__ = None
__IRpcOptions_FWD_DEFINED__ = None
__IGlobalOptions_FWD_DEFINED__ = None
__ISurrogate_FWD_DEFINED__ = None
__IGlobalInterfaceTable_FWD_DEFINED__ = None
__ISynchronize_FWD_DEFINED__ = None
__ISynchronizeHandle_FWD_DEFINED__ = None
__ISynchronizeEvent_FWD_DEFINED__ = None
__ISynchronizeContainer_FWD_DEFINED__ = None
__ISynchronizeMutex_FWD_DEFINED__ = None
__ICancelMethodCalls_FWD_DEFINED__ = None
__IAsyncManager_FWD_DEFINED__ = None
__ICallFactory_FWD_DEFINED__ = None
__IRpcHelper_FWD_DEFINED__ = None
__IReleaseMarshalBuffers_FWD_DEFINED__ = None
__IWaitMultiple_FWD_DEFINED__ = None
__IAddrTrackingControl_FWD_DEFINED__ = None
__IAddrExclusionControl_FWD_DEFINED__ = None
__IPipeByte_FWD_DEFINED__ = None
__AsyncIPipeByte_FWD_DEFINED__ = None
__IPipeLong_FWD_DEFINED__ = None
__AsyncIPipeLong_FWD_DEFINED__ = None
__IPipeDouble_FWD_DEFINED__ = None
__AsyncIPipeDouble_FWD_DEFINED__ = None
__IEnumContextProps_FWD_DEFINED__ = None
__IContext_FWD_DEFINED__ = None
__IObjContext_FWD_DEFINED__ = None
__IComThreadingInfo_FWD_DEFINED__ = None
__IProcessInitControl_FWD_DEFINED__ = None
__IFastRundown_FWD_DEFINED__ = None
__IMarshalingStream_FWD_DEFINED__ = None
__IAgileReference_FWD_DEFINED__ = None
_MSC_EXTENSIONS = None
_OBJIDLBASE_ = None
__IMarshal_INTERFACE_DEFINED__ = None
__INoMarshal_INTERFACE_DEFINED__ = None
__IAgileObject_INTERFACE_DEFINED__ = None
__IActivationFilter_INTERFACE_DEFINED__ = None
__IMarshal2_INTERFACE_DEFINED__ = None
__IMalloc_INTERFACE_DEFINED__ = None
__IStdMarshalInfo_INTERFACE_DEFINED__ = None
__IExternalConnection_INTERFACE_DEFINED__ = None
__IMultiQI_INTERFACE_DEFINED__ = None
__AsyncIMultiQI_INTERFACE_DEFINED__ = None
__IInternalUnknown_INTERFACE_DEFINED__ = None
__IEnumUnknown_INTERFACE_DEFINED__ = None
__IEnumString_INTERFACE_DEFINED__ = None
__ISequentialStream_INTERFACE_DEFINED__ = None
__IStream_INTERFACE_DEFINED__ = None
__IRpcChannelBuffer_INTERFACE_DEFINED__ = None
__IRpcChannelBuffer2_INTERFACE_DEFINED__ = None
__IAsyncRpcChannelBuffer_INTERFACE_DEFINED__ = None
__IRpcChannelBuffer3_INTERFACE_DEFINED__ = None
__IRpcSyntaxNegotiate_INTERFACE_DEFINED__ = None
__IRpcProxyBuffer_INTERFACE_DEFINED__ = None
__IRpcStubBuffer_INTERFACE_DEFINED__ = None
__IPSFactoryBuffer_INTERFACE_DEFINED__ = None
_WIN32_DCOM = None
__IChannelHook_INTERFACE_DEFINED__ = None
__IClientSecurity_INTERFACE_DEFINED__ = None
__IServerSecurity_INTERFACE_DEFINED__ = None
__IRpcOptions_INTERFACE_DEFINED__ = None
__IGlobalOptions_INTERFACE_DEFINED__ = None
__ISurrogate_INTERFACE_DEFINED__ = None
__IGlobalInterfaceTable_INTERFACE_DEFINED__ = None
__ISynchronize_INTERFACE_DEFINED__ = None
__ISynchronizeHandle_INTERFACE_DEFINED__ = None
__ISynchronizeEvent_INTERFACE_DEFINED__ = None
__ISynchronizeContainer_INTERFACE_DEFINED__ = None
__ISynchronizeMutex_INTERFACE_DEFINED__ = None
__ICancelMethodCalls_INTERFACE_DEFINED__ = None
__IAsyncManager_INTERFACE_DEFINED__ = None
__ICallFactory_INTERFACE_DEFINED__ = None
__IRpcHelper_INTERFACE_DEFINED__ = None
__IReleaseMarshalBuffers_INTERFACE_DEFINED__ = None
__IWaitMultiple_INTERFACE_DEFINED__ = None
__IAddrTrackingControl_INTERFACE_DEFINED__ = None
__IAddrExclusionControl_INTERFACE_DEFINED__ = None
__IPipeByte_INTERFACE_DEFINED__ = None
__AsyncIPipeByte_INTERFACE_DEFINED__ = None
__IPipeLong_INTERFACE_DEFINED__ = None
__AsyncIPipeLong_INTERFACE_DEFINED__ = None
__IPipeDouble_INTERFACE_DEFINED__ = None
__AsyncIPipeDouble_INTERFACE_DEFINED__ = None
__IEnumContextProps_INTERFACE_DEFINED__ = None
__IContext_INTERFACE_DEFINED__ = None
__IObjContext_INTERFACE_DEFINED__ = None
__IComThreadingInfo_INTERFACE_DEFINED__ = None
__IProcessInitControl_INTERFACE_DEFINED__ = None
__IFastRundown_INTERFACE_DEFINED__ = None
__IMarshalingStream_INTERFACE_DEFINED__ = None
__IAgileReference_INTERFACE_DEFINED__ = None
USE_COM_CONTEXT_DEF = None
BUILDTYPE_COMSVCS = None
_COMBASEAPI_ = None
_OLE32_ = None

class _COSERVERINFO(ctypes.Structure):
    pass


COSERVERINFO = _COSERVERINFO


class tagMULTI_QI(ctypes.Structure):
    pass


MULTI_QI = tagMULTI_QI


class tagSTATSTG(ctypes.Structure):
    pass


STATSTG = tagSTATSTG


class tagRPCOLEMESSAGE(ctypes.Structure):
    pass


RPCOLEMESSAGE = tagRPCOLEMESSAGE


class SChannelHookCallInfo(ctypes.Structure):
    pass


class tagSOLE_AUTHENTICATION_SERVICE(ctypes.Structure):
    pass


SOLE_AUTHENTICATION_SERVICE = tagSOLE_AUTHENTICATION_SERVICE


class tagSOLE_AUTHENTICATION_INFO(ctypes.Structure):
    pass


SOLE_AUTHENTICATION_INFO = tagSOLE_AUTHENTICATION_INFO


class tagSOLE_AUTHENTICATION_LIST(ctypes.Structure):
    pass


SOLE_AUTHENTICATION_LIST = tagSOLE_AUTHENTICATION_LIST


class tagContextProperty(ctypes.Structure):
    pass


ContextProperty = tagContextProperty



def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    pass
# END IF


# verify that the <rpcsal.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    pass
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF


if not defined(__objidlbase_h__):
    # Forward Declarations
    if not defined(__IMarshal_FWD_DEFINED__):
        class IMarshal(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMarshal_FWD_DEFINED__

    if not defined(__INoMarshal_FWD_DEFINED__):
        class INoMarshal(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __INoMarshal_FWD_DEFINED__

    if not defined(__IAgileObject_FWD_DEFINED__):
        class IAgileObject(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAgileObject_FWD_DEFINED__

    if not defined(__IActivationFilter_FWD_DEFINED__):
        class IActivationFilter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IActivationFilter_FWD_DEFINED__

    if not defined(__IMarshal2_FWD_DEFINED__):
        class IMarshal2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMarshal2_FWD_DEFINED__

    if not defined(__IMalloc_FWD_DEFINED__):
        class IMalloc(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMalloc_FWD_DEFINED__

    if not defined(__IStdMarshalInfo_FWD_DEFINED__):
        class IStdMarshalInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IStdMarshalInfo_FWD_DEFINED__

    if not defined(__IExternalConnection_FWD_DEFINED__):
        class IExternalConnection(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IExternalConnection_FWD_DEFINED__

    if not defined(__IMultiQI_FWD_DEFINED__):
        class IMultiQI(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMultiQI_FWD_DEFINED__

    if not defined(__AsyncIMultiQI_FWD_DEFINED__):
        class AsyncIMultiQI(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __AsyncIMultiQI_FWD_DEFINED__

    if not defined(__IInternalUnknown_FWD_DEFINED__):
        class IInternalUnknown(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IInternalUnknown_FWD_DEFINED__

    if not defined(__IEnumUnknown_FWD_DEFINED__):
        class IEnumUnknown(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumUnknown_FWD_DEFINED__

    if not defined(__IEnumString_FWD_DEFINED__):
        class IEnumString(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumString_FWD_DEFINED__

    if not defined(__ISequentialStream_FWD_DEFINED__):
        class ISequentialStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISequentialStream_FWD_DEFINED__

    if not defined(__IStream_FWD_DEFINED__):
        class IStream(ISequentialStream):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IStream_FWD_DEFINED__

    if not defined(__IRpcChannelBuffer_FWD_DEFINED__):
        class IRpcChannelBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcChannelBuffer_FWD_DEFINED__

    if not defined(__IRpcChannelBuffer2_FWD_DEFINED__):
        class IRpcChannelBuffer2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcChannelBuffer2_FWD_DEFINED__

    if not defined(__IAsyncRpcChannelBuffer_FWD_DEFINED__):
        class IAsyncRpcChannelBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAsyncRpcChannelBuffer_FWD_DEFINED__

    if not defined(__IRpcChannelBuffer3_FWD_DEFINED__):
        class IRpcChannelBuffer3(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcChannelBuffer3_FWD_DEFINED__

    if not defined(__IRpcSyntaxNegotiate_FWD_DEFINED__):
        class IRpcSyntaxNegotiate(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcSyntaxNegotiate_FWD_DEFINED__

    if not defined(__IRpcProxyBuffer_FWD_DEFINED__):
        class IRpcProxyBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcProxyBuffer_FWD_DEFINED__

    if not defined(__IRpcStubBuffer_FWD_DEFINED__):
        class IRpcStubBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcStubBuffer_FWD_DEFINED__

    if not defined(__IPSFactoryBuffer_FWD_DEFINED__):
        class IPSFactoryBuffer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPSFactoryBuffer_FWD_DEFINED__

    if not defined(__IChannelHook_FWD_DEFINED__):
        class IChannelHook(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IChannelHook_FWD_DEFINED__

    if not defined(__IClientSecurity_FWD_DEFINED__):
        class IClientSecurity(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IClientSecurity_FWD_DEFINED__

    if not defined(__IServerSecurity_FWD_DEFINED__):
        class IServerSecurity(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IServerSecurity_FWD_DEFINED__

    if not defined(__IRpcOptions_FWD_DEFINED__):
        class IRpcOptions(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcOptions_FWD_DEFINED__

    if not defined(__IGlobalOptions_FWD_DEFINED__):
        class IGlobalOptions(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IGlobalOptions_FWD_DEFINED__

    if not defined(__ISurrogate_FWD_DEFINED__):
        class ISurrogate(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISurrogate_FWD_DEFINED__

    if not defined(__IGlobalInterfaceTable_FWD_DEFINED__):
        class IGlobalInterfaceTable(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IGlobalInterfaceTable_FWD_DEFINED__

    if not defined(__ISynchronize_FWD_DEFINED__):
        class ISynchronize(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISynchronize_FWD_DEFINED__

    if not defined(__ISynchronizeHandle_FWD_DEFINED__):
        class ISynchronizeHandle(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISynchronizeHandle_FWD_DEFINED__

    if not defined(__ISynchronizeEvent_FWD_DEFINED__):
        class ISynchronizeEvent(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISynchronizeEvent_FWD_DEFINED__

    if not defined(__ISynchronizeContainer_FWD_DEFINED__):
        class ISynchronizeContainer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISynchronizeContainer_FWD_DEFINED__

    if not defined(__ISynchronizeMutex_FWD_DEFINED__):
        class ISynchronizeMutex(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISynchronizeMutex_FWD_DEFINED__

    if not defined(__ICancelMethodCalls_FWD_DEFINED__):
        class ICancelMethodCalls(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICancelMethodCalls_FWD_DEFINED__

    if not defined(__IAsyncManager_FWD_DEFINED__):
        class IAsyncManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAsyncManager_FWD_DEFINED__

    if not defined(__ICallFactory_FWD_DEFINED__):
        class ICallFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICallFactory_FWD_DEFINED__

    if not defined(__IRpcHelper_FWD_DEFINED__):
        class IRpcHelper(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRpcHelper_FWD_DEFINED__

    if not defined(__IReleaseMarshalBuffers_FWD_DEFINED__):
        class IReleaseMarshalBuffers(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IReleaseMarshalBuffers_FWD_DEFINED__

    if not defined(__IWaitMultiple_FWD_DEFINED__):
        class IWaitMultiple(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IWaitMultiple_FWD_DEFINED__

    if not defined(__IAddrTrackingControl_FWD_DEFINED__):
        class IAddrTrackingControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAddrTrackingControl_FWD_DEFINED__

    if not defined(__IAddrExclusionControl_FWD_DEFINED__):
        class IAddrExclusionControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAddrExclusionControl_FWD_DEFINED__

    if not defined(__IPipeByte_FWD_DEFINED__):
        class IPipeByte(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPipeByte_FWD_DEFINED__

    if not defined(__AsyncIPipeByte_FWD_DEFINED__):
        class AsyncIPipeByte(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __AsyncIPipeByte_FWD_DEFINED__

    if not defined(__IPipeLong_FWD_DEFINED__):
        class IPipeLong(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPipeLong_FWD_DEFINED__

    if not defined(__AsyncIPipeLong_FWD_DEFINED__):
        class AsyncIPipeLong(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __AsyncIPipeLong_FWD_DEFINED__

    if not defined(__IPipeDouble_FWD_DEFINED__):
        class IPipeDouble(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPipeDouble_FWD_DEFINED__

    if not defined(__AsyncIPipeDouble_FWD_DEFINED__):
        class AsyncIPipeDouble(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __AsyncIPipeDouble_FWD_DEFINED__

    if not defined(__IEnumContextProps_FWD_DEFINED__):
        class IEnumContextProps(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumContextProps_FWD_DEFINED__

    if not defined(__IContext_FWD_DEFINED__):
        class IContext(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IContext_FWD_DEFINED__

    if not defined(__IObjContext_FWD_DEFINED__):
        class IObjContext(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IObjContext_FWD_DEFINED__

    if not defined(__IComThreadingInfo_FWD_DEFINED__):
        class IComThreadingInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IComThreadingInfo_FWD_DEFINED__

    if not defined(__IProcessInitControl_FWD_DEFINED__):
        class IProcessInitControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProcessInitControl_FWD_DEFINED__

    if not defined(__IFastRundown_FWD_DEFINED__):
        class IFastRundown(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IFastRundown_FWD_DEFINED__

    if not defined(__IMarshalingStream_FWD_DEFINED__):
        class IMarshalingStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMarshalingStream_FWD_DEFINED__

    if not defined(__IAgileReference_FWD_DEFINED__):
        class IAgileReference(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAgileReference_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.unknwnbase_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_objidlbase_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    # +
    # -------------------------------------------------------------------------
    # +
    # -------------------------------------------------------------------------
    # Microsoft Windows
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # --------------------------------------------------------------------
    if NTDDI_VERSION >= NTDDI_VISTA and not defined(_WIN32_WINNT):
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WS03 and not defined(_WIN32_WINNT):
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WINXP and not defined(_WIN32_WINNT):
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K and not defined(_WIN32_WINNT):
        pass
    # END IF

    if  _MSC_VER >= 800 :
        if _MSC_VER >= 1200:
            if not defined(_MSC_EXTENSIONS):
                pass
            # END IF
        # END IF
    # END IF

    if  _MSC_VER >= 1020 :
        pass
    # END IF

    from pyWinAPI.km.crt.limits_h import * # NOQA

    if not defined(_OBJIDLBASE_):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            _COSERVERINFO._fields_ = [
                ('dwReserved1', DWORD),
                ('pwszName', LPWSTR),
                ('pAuthInfo', POINTER(COAUTHINFO)),
                ('dwReserved2', DWORD),
            ]
            if not defined(__IMarshal_INTERFACE_DEFINED__):
                # interface IMarshal
                # [uuid][object][local]
                # [unique]
                LPMARSHAL = POINTER(IMarshal)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMarshal = MIDL_INTERFACE(
                        "{00000003-0000-0000-C000-000000000046}"
                    )
                    IMarshal._iid_ = IID_IMarshal

                    IMarshal._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetUnmarshalClass')],
                            HRESULT,
                            'GetUnmarshalClass',
                            (['in'], REFIID, 'riid'),
                            (['in'], POINTER(VOID), 'pv'),
                            (['in'], DWORD, 'dwDestContext'),
                            (['in'], POINTER(VOID), 'pvDestContext'),
                            (['in'], DWORD, 'mshlflags'),
                            (['out'], POINTER(CLSID), 'pCid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetMarshalSizeMax')],
                            HRESULT,
                            'GetMarshalSizeMax',
                            (['in'], REFIID, 'riid'),
                            (['in'], POINTER(VOID), 'pv'),
                            (['in'], DWORD, 'dwDestContext'),
                            (['in'], POINTER(VOID), 'pvDestContext'),
                            (['in'], DWORD, 'mshlflags'),
                            (['out'], POINTER(DWORD), 'pSize'),
                        ),
                        COMMETHOD(
                            [helpstring('Method MarshalInterface')],
                            HRESULT,
                            'MarshalInterface',
                            (['in'], POINTER(IStream), 'pStm'),
                            (['in'], REFIID, 'riid'),
                            (['in'], POINTER(VOID), 'pv'),
                            (['in'], DWORD, 'dwDestContext'),
                            (['in'], POINTER(VOID), 'pvDestContext'),
                            (['in'], DWORD, 'mshlflags'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UnmarshalInterface')],
                            HRESULT,
                            'UnmarshalInterface',
                            (['in'], POINTER(IStream), 'pStm'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ReleaseMarshalData')],
                            HRESULT,
                            'ReleaseMarshalData',
                            (['in'], POINTER(IStream), 'pStm'),
                        ),
                        COMMETHOD(
                            [helpstring('Method DisconnectObject')],
                            HRESULT,
                            'DisconnectObject',
                            (['in'], DWORD, 'dwReserved'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMarshal_INTERFACE_DEFINED__

            if not defined(__INoMarshal_INTERFACE_DEFINED__):
                # interface INoMarshal
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_INoMarshal = MIDL_INTERFACE(
                        "{ECC8691B-C1DB-4DC0-855E-65F6C551AF49}"
                    )
                    INoMarshal._iid_ = IID_INoMarshal

                    INoMarshal._methods_ = []


                # END IF  C style interface
            # END IF  __INoMarshal_INTERFACE_DEFINED__

            if not defined(__IAgileObject_INTERFACE_DEFINED__):
                # interface IAgileObject
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAgileObject = MIDL_INTERFACE(
                        "{94EA2B94-E9CC-49E0-C0FF-EE64CA8F5B90}"
                    )
                    IAgileObject._iid_ = IID_IAgileObject

                    IAgileObject._methods_ = []


                # END IF  C style interface
            # END IF  __IAgileObject_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0003
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            if not defined(__IActivationFilter_INTERFACE_DEFINED__):
                # interface IActivationFilter
                # [uuid][object][local]
                class tagACTIVATIONTYPE(ENUM):
                    ACTIVATIONTYPE_UNCATEGORIZED = 0
                    ACTIVATIONTYPE_FROM_MONIKER = 0x1
                    ACTIVATIONTYPE_FROM_DATA = 0x2
                    ACTIVATIONTYPE_FROM_STORAGE = 0x4
                    ACTIVATIONTYPE_FROM_STREAM = 0x8
                    ACTIVATIONTYPE_FROM_FILE = 0x10

                ACTIVATIONTYPE = tagACTIVATIONTYPE
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IActivationFilter = MIDL_INTERFACE(
                        "{00000017-0000-0000-C000-000000000046}"
                    )
                    IActivationFilter._iid_ = IID_IActivationFilter

                    IActivationFilter._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandleActivation')],
                            HRESULT,
                            'HandleActivation',
                            (['in'], DWORD, 'dwActivationType'),
                            (['in'], REFCLSID, 'rclsid'),
                            (['out'], POINTER(CLSID), 'pReplacementClsId'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IActivationFilter_INTERFACE_DEFINED__

            if not defined(__IMarshal2_INTERFACE_DEFINED__):
                # interface IMarshal2
                # [uuid][object][local]
                # [unique]
                LPMARSHAL2 = POINTER(IMarshal2)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMarshal2 = MIDL_INTERFACE(
                        "{000001CF-0000-0000-C000-000000000046}"
                    )
                    IMarshal2._iid_ = IID_IMarshal2

                    IMarshal2._methods_ = []


                # END IF  C style interface
            # END IF  __IMarshal2_INTERFACE_DEFINED__

            if not defined(__IMalloc_INTERFACE_DEFINED__):
                # interface IMalloc
                # [uuid][object][local]
                # [unique]
                LPMALLOC = POINTER(IMalloc)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMalloc = MIDL_INTERFACE(
                        "{00000002-0000-0000-C000-000000000046}"
                    )
                    IMalloc._iid_ = IID_IMalloc

                    IMalloc._methods_ = [
                        COMMETHOD(
                            [helpstring('Method *Alloc')],
                            VOID,
                            '*Alloc',
                            (['in'], SIZE_T, 'cb'),
                        ),
                        COMMETHOD(
                            [helpstring('Method *Realloc')],
                            VOID,
                            '*Realloc',
                            (['in'], POINTER(VOID), 'pv'),
                            (['in'], SIZE_T, 'cb'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Free')],
                            VOID,
                            'Free',
                            (['in'], POINTER(VOID), 'pv'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSize')],
                            SIZE_T,
                            'GetSize',
                            (['in'], POINTER(VOID), 'pv'),
                        ),
                        COMMETHOD(
                            [helpstring('Method DidAlloc')],
                            INT,
                            'DidAlloc',
                            (['in'], POINTER(VOID), 'pv'),
                        ),
                        COMMETHOD(
                            [helpstring('Method HeapMinimize')],
                            VOID,
                            'HeapMinimize',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMalloc_INTERFACE_DEFINED__

            if not defined(__IStdMarshalInfo_INTERFACE_DEFINED__):
                # interface IStdMarshalInfo
                # [uuid][object][local]
                # [unique]
                LPSTDMARSHALINFO = POINTER(IStdMarshalInfo)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IStdMarshalInfo = MIDL_INTERFACE(
                        "{00000018-0000-0000-C000-000000000046}"
                    )
                    IStdMarshalInfo._iid_ = IID_IStdMarshalInfo

                    IStdMarshalInfo._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetClassForHandler')],
                            HRESULT,
                            'GetClassForHandler',
                            (['in'], DWORD, 'dwDestContext'),
                            (['in'], POINTER(VOID), 'pvDestContext'),
                            (['out'], POINTER(CLSID), 'pClsid'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IStdMarshalInfo_INTERFACE_DEFINED__

            if not defined(__IExternalConnection_INTERFACE_DEFINED__):
                # interface IExternalConnection
                # [uuid][local][object]
                # [unique]
                LPEXTERNALCONNECTION = POINTER(IExternalConnection)


                class tagEXTCONN(ENUM):
                    EXTCONN_STRONG = 0x1
                    EXTCONN_WEAK = 0x2
                    EXTCONN_CALLABLE = 0x4

                EXTCONN = tagEXTCONN
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IExternalConnection = MIDL_INTERFACE(
                        "{00000019-0000-0000-C000-000000000046}"
                    )
                    IExternalConnection._iid_ = IID_IExternalConnection

                    IExternalConnection._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddConnection')],
                            DWORD,
                            'AddConnection',
                            (['in'], DWORD, 'extconn'),
                            (['in'], DWORD, 'reserved'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ReleaseConnection')],
                            DWORD,
                            'ReleaseConnection',
                            (['in'], DWORD, 'extconn'),
                            (['in'], DWORD, 'reserved'),
                            (['in'], BOOL, 'fLastReleaseCloses'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IExternalConnection_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0008
            # [local]
            # [unique]
            LPMULTIQI = POINTER(IMultiQI)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            tagMULTI_QI._fields_ = [
                ('pIID', POINTER(IID)),
                ('pItf', POINTER(comtypes.IUnknown)),
                ('hr', HRESULT),
            ]
            if not defined(__IMultiQI_INTERFACE_DEFINED__):
                # interface IMultiQI
                # [async_uuid][uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMultiQI = MIDL_INTERFACE(
                        "{00000020-0000-0000-C000-000000000046}"
                    )
                    IMultiQI._iid_ = IID_IMultiQI

                    IMultiQI._methods_ = [
                        COMMETHOD(
                            [helpstring('Method QueryMultipleInterfaces')],
                            HRESULT,
                            'QueryMultipleInterfaces',
                            (['in'], ULONG, 'cMQIs'),
                            (['out', 'in'], POINTER(MULTI_QI), 'pMQIs'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMultiQI_INTERFACE_DEFINED__

            if not defined(__AsyncIMultiQI_INTERFACE_DEFINED__):
                # interface AsyncIMultiQI
                # [uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_AsyncIMultiQI = MIDL_INTERFACE(
                        "{000E0020-0000-0000-C000-000000000046}"
                    )
                    AsyncIMultiQI._iid_ = IID_AsyncIMultiQI

                    AsyncIMultiQI._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Begin_QueryMultipleInterfaces')],
                            HRESULT,
                            'Begin_QueryMultipleInterfaces',
                            (['in'], ULONG, 'cMQIs'),
                            (['out', 'in'], POINTER(MULTI_QI), 'pMQIs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finish_QueryMultipleInterfaces')],
                            HRESULT,
                            'Finish_QueryMultipleInterfaces',
                            (['out', 'in'], POINTER(MULTI_QI), 'pMQIs'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __AsyncIMultiQI_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0009
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            if not defined(__IInternalUnknown_INTERFACE_DEFINED__):
                # interface IInternalUnknown
                # [uuid][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IInternalUnknown = MIDL_INTERFACE(
                        "{00000021-0000-0000-C000-000000000046}"
                    )
                    IInternalUnknown._iid_ = IID_IInternalUnknown

                    IInternalUnknown._methods_ = [
                        COMMETHOD(
                            [helpstring('Method QueryInternalInterface')],
                            HRESULT,
                            'QueryInternalInterface',
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IInternalUnknown_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0010
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if not defined(__IEnumUnknown_INTERFACE_DEFINED__):
                # interface IEnumUnknown
                # [unique][uuid][object]
                # [unique]
                LPENUMUNKNOWN = POINTER(IEnumUnknown)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IEnumUnknown = MIDL_INTERFACE(
                        "{00000100-0000-0000-C000-000000000046}"
                    )
                    IEnumUnknown._iid_ = IID_IEnumUnknown

                    IEnumUnknown._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Next'), 'local'],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                               'rgelt'
                            ),
                            (['out'], POINTER(ULONG), 'pceltFetched'),
                        ),
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
                                POINTER(POINTER(IEnumUnknown)),
                               'ppenum'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IEnumUnknown_INTERFACE_DEFINED__

            if not defined(__IEnumString_INTERFACE_DEFINED__):
                # interface IEnumString
                # [unique][uuid][object]
                # [unique]
                LPENUMSTRING = POINTER(IEnumString)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IEnumString = MIDL_INTERFACE(
                        "{00000101-0000-0000-C000-000000000046}"
                    )
                    IEnumString._iid_ = IID_IEnumString

                    IEnumString._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Next'), 'local'],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (['out'], POINTER(LPOLESTR), 'rgelt'),
                            (['out'], POINTER(ULONG), 'pceltFetched'),
                        ),
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
                                POINTER(POINTER(IEnumString)),
                               'ppenum'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IEnumString_INTERFACE_DEFINED__

            if not defined(__ISequentialStream_INTERFACE_DEFINED__):
                # interface ISequentialStream
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ISequentialStream = MIDL_INTERFACE(
                        "{0C733A30-2A1C-11CE-ADE5-00AA0044773D}"
                    )
                    ISequentialStream._iid_ = IID_ISequentialStream

                    ISequentialStream._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Read'), 'local'],
                            HRESULT,
                            'Read',
                            (['out'], POINTER(VOID), 'pv'),
                            (['in'], ULONG, 'cb'),
                            (['out'], POINTER(ULONG), 'pcbRead'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Write'), 'local'],
                            HRESULT,
                            'Write',
                            (['in'], POINTER(VOID), 'pv'),
                            (['in'], ULONG, 'cb'),
                            (['out'], POINTER(ULONG), 'pcbWritten'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ISequentialStream_INTERFACE_DEFINED__

            if not defined(__IStream_INTERFACE_DEFINED__):
                # interface IStream
                # [unique][uuid][object]
                # [unique]
                LPSTREAM = POINTER(IStream)

                tagSTATSTG._fields_ = [
                    ('pwcsName', LPOLESTR),
                    ('type', DWORD),
                    ('cbSize', ULARGE_INTEGER),
                    ('mtime', FILETIME),
                    ('ctime', FILETIME),
                    ('atime', FILETIME),
                    ('grfMode', DWORD),
                    ('grfLocksSupported', DWORD),
                    ('clsid', CLSID),
                    ('grfStateBits', DWORD),
                    ('reserved', DWORD),
                ]


                class tagSTGTY(ENUM):
                    STGTY_STORAGE = 1
                    STGTY_STREAM = 2
                    STGTY_LOCKBYTES = 3
                    STGTY_PROPERTY = 4

                STGTY = tagSTGTY


                class tagSTREAM_SEEK(ENUM):
                    STREAM_SEEK_SET = 0
                    STREAM_SEEK_CUR = 1
                    STREAM_SEEK_END = 2

                STREAM_SEEK = tagSTREAM_SEEK


                class tagLOCKTYPE(ENUM):
                    LOCK_WRITE = 1
                    LOCK_EXCLUSIVE = 2
                    LOCK_ONLYONCE = 4

                LOCKTYPE = tagLOCKTYPE
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IStream = MIDL_INTERFACE(
                        "{0000000C-0000-0000-C000-000000000046}"
                    )
                    IStream._iid_ = IID_IStream

                    IStream._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Seek'), 'local'],
                            HRESULT,
                            'Seek',
                            (['in'], LARGE_INTEGER, 'dlibMove'),
                            (['in'], DWORD, 'dwOrigin'),
                            (
                                ['out'],
                                POINTER(ULARGE_INTEGER),
                               'plibNewPosition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetSize')],
                            HRESULT,
                            'SetSize',
                            (['in'], ULARGE_INTEGER, 'libNewSize'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CopyTo'), 'local'],
                            HRESULT,
                            'CopyTo',
                            (['in'], POINTER(IStream), 'pstm'),
                            (['in'], ULARGE_INTEGER, 'cb'),
                            (['out'], POINTER(ULARGE_INTEGER), 'pcbRead'),
                            (['out'], POINTER(ULARGE_INTEGER), 'pcbWritten'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Commit')],
                            HRESULT,
                            'Commit',
                            (['in'], DWORD, 'grfCommitFlags'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Revert')],
                            HRESULT,
                            'Revert',
                        ),
                        COMMETHOD(
                            [helpstring('Method LockRegion')],
                            HRESULT,
                            'LockRegion',
                            (['in'], ULARGE_INTEGER, 'libOffset'),
                            (['in'], ULARGE_INTEGER, 'cb'),
                            (['in'], DWORD, 'dwLockType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UnlockRegion')],
                            HRESULT,
                            'UnlockRegion',
                            (['in'], ULARGE_INTEGER, 'libOffset'),
                            (['in'], ULARGE_INTEGER, 'cb'),
                            (['in'], DWORD, 'dwLockType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Stat')],
                            HRESULT,
                            'Stat',
                            (['out'], POINTER(STATSTG), 'pstatstg'),
                            (['in'], DWORD, 'grfStatFlag'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Clone')],
                            HRESULT,
                            'Clone',
                            (['out'], POINTER(POINTER(IStream)), 'ppstm'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IStream_INTERFACE_DEFINED__

            if not defined(__IRpcChannelBuffer_INTERFACE_DEFINED__):
                # interface IRpcChannelBuffer
                # [uuid][object][local]
                RPCOLEDATAREP = ULONG

                tagRPCOLEMESSAGE._fields_ = [
                    ('reserved1', POINTER(VOID)),
                    ('dataRepresentation', RPCOLEDATAREP),
                    ('Buffer', POINTER(VOID)),
                    ('cbBuffer', ULONG),
                    ('iMethod', ULONG),
                    ('reserved2', POINTER(VOID) * 5),
                    ('rpcFlags', ULONG),
                ]
                PRPCOLEMESSAGE = POINTER(RPCOLEMESSAGE)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IRpcChannelBuffer = MIDL_INTERFACE(
                        "{D5F56B60-593B-101A-B569-08002B2DBF7A}"
                    )
                    IRpcChannelBuffer._iid_ = IID_IRpcChannelBuffer

                    IRpcChannelBuffer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetBuffer')],
                            HRESULT,
                            'GetBuffer',
                            (
                                ['out', 'in'],
                                POINTER(RPCOLEMESSAGE),
                               'pMessage'
                            ),
                            (['in'], REFIID, 'riid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SendReceive')],
                            HRESULT,
                            'SendReceive',
                            (
                                ['out', 'in'],
                                POINTER(RPCOLEMESSAGE),
                               'pMessage'
                            ),
                            (['out'], POINTER(ULONG), 'pStatus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method FreeBuffer')],
                            HRESULT,
                            'FreeBuffer',
                            (
                                ['out', 'in'],
                                POINTER(RPCOLEMESSAGE),
                               'pMessage'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDestCtx')],
                            HRESULT,
                            'GetDestCtx',
                            (['out'], POINTER(DWORD), 'pdwDestContext'),
                            (
                                ['out'],
                                POINTER(POINTER(VOID)),
                               'ppvDestContext'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method IsConnected')],
                            HRESULT,
                            'IsConnected',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IRpcChannelBuffer_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0015
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            if not defined(__IRpcChannelBuffer2_INTERFACE_DEFINED__):
                # interface IRpcChannelBuffer2
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IRpcChannelBuffer2 = MIDL_INTERFACE(
                        "{594F31D0-7F19-11D0-B194-00A0C90DC8BF}"
                    )
                    IRpcChannelBuffer2._iid_ = IID_IRpcChannelBuffer2

                    IRpcChannelBuffer2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetProtocolVersion')],
                            HRESULT,
                            'GetProtocolVersion',
                            (['out'], POINTER(DWORD), 'pdwVersion'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IRpcChannelBuffer2_INTERFACE_DEFINED__

            if not defined(__IAsyncRpcChannelBuffer_INTERFACE_DEFINED__):
                # interface IAsyncRpcChannelBuffer
                # [unique][uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAsyncRpcChannelBuffer = MIDL_INTERFACE(
                        "{A5029FB6-3C34-11D1-9C99-00C04FB998AA}"
                    )
                    IAsyncRpcChannelBuffer._iid_ = IID_IAsyncRpcChannelBuffer

                    IAsyncRpcChannelBuffer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Send')],
                            HRESULT,
                            'Send',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['in'], POINTER(ISynchronize), 'pSync'),
                            (['out'], POINTER(ULONG), 'pulStatus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Receive')],
                            HRESULT,
                            'Receive',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['out'], POINTER(ULONG), 'pulStatus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDestCtxEx')],
                            HRESULT,
                            'GetDestCtxEx',
                            (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['out'], POINTER(DWORD), 'pdwDestContext'),
                            (
                                ['out'],
                                POINTER(POINTER(VOID)),
                               'ppvDestContext'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAsyncRpcChannelBuffer_INTERFACE_DEFINED__

            if not defined(__IRpcChannelBuffer3_INTERFACE_DEFINED__):
                # interface IRpcChannelBuffer3
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IRpcChannelBuffer3 = MIDL_INTERFACE(
                        "{25B15600-0115-11D0-BF0D-00AA00B8DFD2}"
                    )
                    IRpcChannelBuffer3._iid_ = IID_IRpcChannelBuffer3

                    IRpcChannelBuffer3._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Send')],
                            HRESULT,
                            'Send',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['out'], POINTER(ULONG), 'pulStatus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Receive')],
                            HRESULT,
                            'Receive',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['in'], ULONG, 'ulSize'),
                            (['out'], POINTER(ULONG), 'pulStatus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCallContext')],
                            HRESULT,
                            'GetCallContext',
                            (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'pInterface'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetDestCtxEx')],
                            HRESULT,
                            'GetDestCtxEx',
                            (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['out'], POINTER(DWORD), 'pdwDestContext'),
                            (
                                ['out'],
                                POINTER(POINTER(VOID)),
                               'ppvDestContext'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetState')],
                            HRESULT,
                            'GetState',
                            (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['out'], POINTER(DWORD), 'pState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RegisterAsync')],
                            HRESULT,
                            'RegisterAsync',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['in'], POINTER(IAsyncManager), 'pAsyncMgr'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IRpcChannelBuffer3_INTERFACE_DEFINED__

            if not defined(__IRpcSyntaxNegotiate_INTERFACE_DEFINED__):
                # interface IRpcSyntaxNegotiate
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IRpcSyntaxNegotiate = MIDL_INTERFACE(
                        "{58A08519-24C8-4935-B482-3FD823333A4F}"
                    )
                    IRpcSyntaxNegotiate._iid_ = IID_IRpcSyntaxNegotiate

                    IRpcSyntaxNegotiate._methods_ = [
                        COMMETHOD(
                            [helpstring('Method NegotiateSyntax')],
                            HRESULT,
                            'NegotiateSyntax',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IRpcSyntaxNegotiate_INTERFACE_DEFINED__

            if not defined(__IRpcProxyBuffer_INTERFACE_DEFINED__):
                # interface IRpcProxyBuffer
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IRpcProxyBuffer = MIDL_INTERFACE(
                        "{D5F56A34-593B-101A-B569-08002B2DBF7A}"
                    )
                    IRpcProxyBuffer._iid_ = IID_IRpcProxyBuffer

                    IRpcProxyBuffer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Connect')],
                            HRESULT,
                            'Connect',
                            (
                                ['in'],
                                POINTER(IRpcChannelBuffer),
                               'pRpcChannelBuffer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Disconnect')],
                            VOID,
                            'Disconnect',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IRpcProxyBuffer_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0020
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if not defined(__IRpcStubBuffer_INTERFACE_DEFINED__):
                # interface IRpcStubBuffer
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IRpcStubBuffer = MIDL_INTERFACE(
                        "{D5F56AFC-593B-101A-B569-08002B2DBF7A}"
                    )
                    IRpcStubBuffer._iid_ = IID_IRpcStubBuffer

                    IRpcStubBuffer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Connect')],
                            HRESULT,
                            'Connect',
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                               'pUnkServer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Disconnect')],
                            VOID,
                            'Disconnect',
                        ),
                        COMMETHOD(
                            [helpstring('Method Invoke')],
                            HRESULT,
                            'Invoke',
                            (
                                ['out', 'in'],
                                POINTER(RPCOLEMESSAGE),
                               '_prpcmsg'
                            ),
                            (
                                ['in'],
                                POINTER(IRpcChannelBuffer),
                               '_pRpcChannelBuffer'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method *IsIIDSupported')],
                            IRpcStubBuffer,
                            '*IsIIDSupported',
                            (['in'], REFIID, 'riid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CountRefs')],
                            ULONG,
                            'CountRefs',
                        ),
                        COMMETHOD(
                            [helpstring('Method DebugServerQueryInterface')],
                            HRESULT,
                            'DebugServerQueryInterface',
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),
                        COMMETHOD(
                            [helpstring('Method DebugServerRelease')],
                            VOID,
                            'DebugServerRelease',
                            (['in'], POINTER(VOID), 'pv'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IRpcStubBuffer_INTERFACE_DEFINED__

            if not defined(__IPSFactoryBuffer_INTERFACE_DEFINED__):
                # interface IPSFactoryBuffer
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPSFactoryBuffer = MIDL_INTERFACE(
                        "{D5F569D0-593B-101A-B569-08002B2DBF7A}"
                    )
                    IPSFactoryBuffer._iid_ = IID_IPSFactoryBuffer


                    IPSFactoryBuffer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateProxy')],
                            HRESULT,
                            'CreateProxy',
                            (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
                            (['in'], REFIID, 'riid'),
                            (
                                ['out'],
                                POINTER(POINTER(IRpcProxyBuffer)),
                               'ppProxy'
                            ),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateStub')],
                            HRESULT,
                            'CreateStub',
                            (['in'], REFIID, 'riid'),
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                               'pUnkServer'
                            ),
                            (
                                ['out'],
                                POINTER(POINTER(IRpcStubBuffer)),
                               'ppStub'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPSFactoryBuffer_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0022
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            if (_WIN32_WINNT >= 0x0400) or defined(_WIN32_DCOM):
                # This interface is only valid on Windows NT 4.0
                SChannelHookCallInfo._fields_ = [
                    ('iid', IID),
                    ('cbSize', DWORD),
                    ('uCausality', GUID),
                    ('dwServerPid', DWORD),
                    ('iMethod', DWORD),
                    ('pObject', POINTER(VOID)),
                ]
                if not defined(__IChannelHook_INTERFACE_DEFINED__):
                    # interface IChannelHook
                    # [uuid][object][local]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IChannelHook = MIDL_INTERFACE(
                            "{1008C4A0-7613-11CF-9AF1-0020AF6E72F4}"
                        )
                        IChannelHook._iid_ = IID_IChannelHook

                        IChannelHook._methods_ = [
                            COMMETHOD(
                                [helpstring('Method ClientGetSize')],
                                VOID,
                                'ClientGetSize',
                                (['in'], REFGUID, 'uExtent'),
                                (['in'], REFIID, 'riid'),
                                (['out'], POINTER(ULONG), 'pDataSize'),
                            ),
                            COMMETHOD(
                                [helpstring('Method ClientFillBuffer')],
                                VOID,
                                'ClientFillBuffer',
                                (['in'], REFGUID, 'uExtent'),
                                (['in'], REFIID, 'riid'),
                                (['out', 'in'], POINTER(ULONG), 'pDataSize'),
                                (['in'], POINTER(VOID), 'pDataBuffer'),
                            ),
                            COMMETHOD(
                                [helpstring('Method ClientNotify')],
                                VOID,
                                'ClientNotify',
                                (['in'], REFGUID, 'uExtent'),
                                (['in'], REFIID, 'riid'),
                                (['in'], ULONG, 'cbDataSize'),
                                (['in'], POINTER(VOID), 'pDataBuffer'),
                                (['in'], DWORD, 'lDataRep'),
                                (['in'], HRESULT, 'hrFault'),
                            ),
                            COMMETHOD(
                                [helpstring('Method ServerNotify')],
                                VOID,
                                'ServerNotify',
                                (['in'], REFGUID, 'uExtent'),
                                (['in'], REFIID, 'riid'),
                                (['in'], ULONG, 'cbDataSize'),
                                (['in'], POINTER(VOID), 'pDataBuffer'),
                                (['in'], DWORD, 'lDataRep'),
                            ),
                            COMMETHOD(
                                [helpstring('Method ServerGetSize')],
                                VOID,
                                'ServerGetSize',
                                (['in'], REFGUID, 'uExtent'),
                                (['in'], REFIID, 'riid'),
                                (['in'], HRESULT, 'hrFault'),
                                (['out'], POINTER(ULONG), 'pDataSize'),
                            ),
                            COMMETHOD(
                                [helpstring('Method ServerFillBuffer')],
                                VOID,
                                'ServerFillBuffer',
                                (['in'], REFGUID, 'uExtent'),
                                (['in'], REFIID, 'riid'),
                                (['out', 'in'], POINTER(ULONG), 'pDataSize'),
                                (['in'], POINTER(VOID), 'pDataBuffer'),
                                (['in'], HRESULT, 'hrFault'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IChannelHook_INTERFACE_DEFINED__

                # interface __MIDL_itf_objidlbase_0000_0023
                # [local]
            # END IF  DCOM
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if (_WIN32_WINNT >= 0x0400) or defined(_WIN32_DCOM):
            # This interface is only valid on Windows NT 4.0
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                if not defined(__IClientSecurity_INTERFACE_DEFINED__):
                    # interface IClientSecurity
                    # [uuid][object][local]
                    tagSOLE_AUTHENTICATION_SERVICE._fields_ = [
                        ('dwAuthnSvc', DWORD),
                        ('dwAuthzSvc', DWORD),
                        ('pPrincipalName', POINTER(OLECHAR)),
                        ('hr', HRESULT),
                    ]
                    PSOLE_AUTHENTICATION_SERVICE = POINTER(SOLE_AUTHENTICATION_SERVICE)


                    class tagEOLE_AUTHENTICATION_CAPABILITIES(ENUM):
                        EOAC_NONE = 0
                        EOAC_MUTUAL_AUTH = 0x1
                        EOAC_STATIC_CLOAKING = 0x20
                        EOAC_DYNAMIC_CLOAKING = 0x40
                        EOAC_ANY_AUTHORITY = 0x80
                        EOAC_MAKE_FULLSIC = 0x100
                        EOAC_DEFAULT = 0x800
                        EOAC_SECURE_REFS = 0x2
                        EOAC_ACCESS_CONTROL = 0x4
                        EOAC_APPID = 0x8
                        EOAC_DYNAMIC = 0x10
                        EOAC_REQUIRE_FULLSIC = 0x200
                        EOAC_AUTO_IMPERSONATE = 0x400
                        EOAC_DISABLE_AAA = 0x1000
                        EOAC_NO_CUSTOM_MARSHAL = 0x2000
                        EOAC_RESERVED1 = 0x4000

                    EOLE_AUTHENTICATION_CAPABILITIES = tagEOLE_AUTHENTICATION_CAPABILITIES

                    tagSOLE_AUTHENTICATION_INFO._fields_ = [
                        ('dwAuthnSvc', DWORD),
                        ('dwAuthzSvc', DWORD),
                        ('pAuthInfo', POINTER(VOID)),
                    ]
                    PSOLE_AUTHENTICATION_INFO = POINTER(tagSOLE_AUTHENTICATION_INFO)


                    tagSOLE_AUTHENTICATION_LIST._fields_ = [
                        ('cAuthInfo', DWORD),
                        ('aAuthInfo', POINTER(SOLE_AUTHENTICATION_INFO)),
                    ]
                    PSOLE_AUTHENTICATION_LIST = POINTER(tagSOLE_AUTHENTICATION_LIST)

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IClientSecurity = MIDL_INTERFACE(
                            "{0000013D-0000-0000-C000-000000000046}"
                        )
                        IClientSecurity._iid_ = IID_IClientSecurity

                        IClientSecurity._methods_ = [
                            COMMETHOD(
                                [helpstring('Method QueryBlanket')],
                                HRESULT,
                                'QueryBlanket',
                                (
                                    ['in'],
                                    POINTER(comtypes.IUnknown),
                                   'pProxy'
                                ),
                                (['out'], POINTER(DWORD), 'pAuthnSvc'),
                                (['out'], POINTER(DWORD), 'pAuthzSvc'),
                                (
                                    ['out'],
                                    POINTER(POINTER(OLECHAR)),
                                   'pServerPrincName'
                                ),
                                (['out'], POINTER(DWORD), 'pAuthnLevel'),
                                (['out'], POINTER(DWORD), 'pImpLevel'),
                                (
                                    ['out'],
                                    POINTER(POINTER(VOID)),
                                   'pAuthInfo'
                                ),
                                (['out'], POINTER(DWORD), 'pCapabilites'),
                            ),
                            COMMETHOD(
                                [helpstring('Method SetBlanket')],
                                HRESULT,
                                'SetBlanket',
                                (
                                    ['in'],
                                    POINTER(comtypes.IUnknown),
                                   'pProxy'
                                ),
                                (['in'], DWORD, 'dwAuthnSvc'),
                                (['in'], DWORD, 'dwAuthzSvc'),
                                (
                                    ['in'],
                                    POINTER(OLECHAR),
                                   'pServerPrincName'
                                ),
                                (['in'], DWORD, 'dwAuthnLevel'),
                                (['in'], DWORD, 'dwImpLevel'),
                                (['in'], POINTER(VOID), 'pAuthInfo'),
                                (['in'], DWORD, 'dwCapabilities'),
                            ),
                            COMMETHOD(
                                [helpstring('Method CopyProxy')],
                                HRESULT,
                                'CopyProxy',
                                (
                                    ['in'],
                                    POINTER(comtypes.IUnknown),
                                   'pProxy'
                                ),
                                (
                                    ['out'],
                                    POINTER(POINTER(comtypes.IUnknown)),
                                   'ppCopy'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IClientSecurity_INTERFACE_DEFINED__

                # interface __MIDL_itf_objidlbase_0000_0024
                # [local]
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
                if not defined(__IServerSecurity_INTERFACE_DEFINED__):
                    # interface IServerSecurity
                    # [uuid][object][local]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IServerSecurity = MIDL_INTERFACE(
                            "{0000013E-0000-0000-C000-000000000046}"
                        )
                        IServerSecurity._iid_ = IID_IServerSecurity

                        IServerSecurity._methods_ = [
                            COMMETHOD(
                                [helpstring('Method QueryBlanket')],
                                HRESULT,
                                'QueryBlanket',
                                (['out'], POINTER(DWORD), 'pAuthnSvc'),
                                (['out'], POINTER(DWORD), 'pAuthzSvc'),
                                (
                                    ['out'],
                                    POINTER(POINTER(OLECHAR)),
                                   'pServerPrincName'
                                ),
                                (['out'], POINTER(DWORD), 'pAuthnLevel'),
                                (['out'], POINTER(DWORD), 'pImpLevel'),
                                (['out'], POINTER(POINTER(VOID)), 'pPrivs'),
                                (
                                    ['out', 'in'],
                                    POINTER(DWORD),
                                   'pCapabilities'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method ImpersonateClient')],
                                HRESULT,
                                'ImpersonateClient',
                            ),
                            COMMETHOD(
                                [helpstring('Method RevertToSelf')],
                                HRESULT,
                                'RevertToSelf',
                            ),
                            COMMETHOD(
                                [helpstring('Method IsImpersonating')],
                                BOOL,
                                'IsImpersonating',
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IServerSecurity_INTERFACE_DEFINED__

                # interface __MIDL_itf_objidlbase_0000_0025
                # [local]
                class tagRPCOPT_PROPERTIES(ENUM):
                    COMBND_RPCTIMEOUT = 0x1
                    COMBND_SERVER_LOCALITY = 0x2
                    COMBND_RESERVED1 = 0x4
                    COMBND_RESERVED2 = 0x5
                    COMBND_RESERVED3 = 0x8
                    COMBND_RESERVED4 = 0x10

                RPCOPT_PROPERTIES = tagRPCOPT_PROPERTIES


                class tagRPCOPT_SERVER_LOCALITY_VALUES(ENUM):
                    SERVER_LOCALITY_PROCESS_LOCAL = 0
                    SERVER_LOCALITY_MACHINE_LOCAL = 1
                    SERVER_LOCALITY_REMOTE = 2

                RPCOPT_SERVER_LOCALITY_VALUES = tagRPCOPT_SERVER_LOCALITY_VALUES
                if not defined(__IRpcOptions_INTERFACE_DEFINED__):
                    # interface IRpcOptions
                    # [uuid][local][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IRpcOptions = MIDL_INTERFACE(
                            "{00000144-0000-0000-C000-000000000046}"
                        )
                        IRpcOptions._iid_ = IID_IRpcOptions

                        IRpcOptions._methods_ = [
                            COMMETHOD(
                                [helpstring('Method Set')],
                                HRESULT,
                                'Set',
                                (['in'], POINTER(comtypes.IUnknown), 'pPrx'),
                                (['in'], RPCOPT_PROPERTIES, 'dwProperty'),
                                (['in'], ULONG_PTR, 'dwValue'),
                            ),
                            COMMETHOD(
                                [helpstring('Method Query')],
                                HRESULT,
                                'Query',
                                (['in'], POINTER(comtypes.IUnknown), 'pPrx'),
                                (['in'], RPCOPT_PROPERTIES, 'dwProperty'),
                                (['out'], POINTER(ULONG_PTR), 'pdwValue'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IRpcOptions_INTERFACE_DEFINED__

                # interface __MIDL_itf_objidlbase_0000_0026
                # [local]
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                class tagGLOBALOPT_PROPERTIES(ENUM):
                    COMGLB_EXCEPTION_HANDLING = 1
                    COMGLB_APPID = 2
                    COMGLB_RPC_THREADPOOL_SETTING = 3
                    COMGLB_RO_SETTINGS = 4
                    COMGLB_UNMARSHALING_POLICY = 5
                    COMGLB_PROPERTIES_RESERVED1 = 6
                    COMGLB_PROPERTIES_RESERVED2 = 7

                GLOBALOPT_PROPERTIES = tagGLOBALOPT_PROPERTIES


                class tagGLOBALOPT_EH_VALUES(ENUM):
                    COMGLB_EXCEPTION_HANDLE = 0
                    COMGLB_EXCEPTION_DONOT_HANDLE_FATAL = 1
                    COMGLB_EXCEPTION_DONOT_HANDLE = (
                        COMGLB_EXCEPTION_DONOT_HANDLE_FATAL
                    )
                    COMGLB_EXCEPTION_DONOT_HANDLE_ANY = 2

                GLOBALOPT_EH_VALUES = tagGLOBALOPT_EH_VALUES


                class tagGLOBALOPT_RPCTP_VALUES(ENUM):
                    COMGLB_RPC_THREADPOOL_SETTING_DEFAULT_POOL = 0
                    COMGLB_RPC_THREADPOOL_SETTING_PRIVATE_POOL = 1

                GLOBALOPT_RPCTP_VALUES = tagGLOBALOPT_RPCTP_VALUES


                class tagGLOBALOPT_RO_FLAGS(ENUM):
                    COMGLB_STA_MODALLOOP_REMOVE_TOUCH_MESSAGES = 0x1
                    COMGLB_STA_MODALLOOP_SHARED_QUEUE_REMOVE_INPUT_MESSAGES = (
                        0x2
                    )
                    COMGLB_STA_MODALLOOP_SHARED_QUEUE_DONOT_REMOVE_INPUT_MESSAGES = (
                        0x4
                    )
                    COMGLB_FAST_RUNDOWN = 0x8
                    COMGLB_RESERVED1 = 0x10
                    COMGLB_RESERVED2 = 0x20
                    COMGLB_RESERVED3 = 0x40
                    COMGLB_STA_MODALLOOP_SHARED_QUEUE_REORDER_POINTER_MESSAGES = (
                        0x80
                    )
                    COMGLB_RESERVED4 = 0x100
                    COMGLB_RESERVED5 = 0x200
                    COMGLB_RESERVED6 = 0x400

                GLOBALOPT_RO_FLAGS = tagGLOBALOPT_RO_FLAGS


                class tagGLOBALOPT_UNMARSHALING_POLICY_VALUES(ENUM):
                    COMGLB_UNMARSHALING_POLICY_NORMAL = 0
                    COMGLB_UNMARSHALING_POLICY_STRONG = 1
                    COMGLB_UNMARSHALING_POLICY_HYBRID = 2

                GLOBALOPT_UNMARSHALING_POLICY_VALUES = tagGLOBALOPT_UNMARSHALING_POLICY_VALUES
                if not defined(__IGlobalOptions_INTERFACE_DEFINED__):
                    # interface IGlobalOptions
                    # [uuid][unique][local][object]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IGlobalOptions = MIDL_INTERFACE(
                            "{0000015B-0000-0000-C000-000000000046}"
                        )
                        IGlobalOptions._iid_ = IID_IGlobalOptions

                        IGlobalOptions._methods_ = [
                            COMMETHOD(
                                [helpstring('Method Set')],
                                HRESULT,
                                'Set',
                                (['in'], GLOBALOPT_PROPERTIES, 'dwProperty'),
                                (['in'], ULONG_PTR, 'dwValue'),
                            ),
                            COMMETHOD(
                                [helpstring('Method Query')],
                                HRESULT,
                                'Query',
                                (['in'], GLOBALOPT_PROPERTIES, 'dwProperty'),
                                (['out'], POINTER(ULONG_PTR), 'pdwValue'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IGlobalOptions_INTERFACE_DEFINED__

                # interface __MIDL_itf_objidlbase_0000_0027
                # [local]
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        # END IF  DCOM

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if not defined(__ISurrogate_INTERFACE_DEFINED__):
                # interface ISurrogate
                # [object][unique][version][uuid]
                # [unique]
                LPSURROGATE = POINTER(ISurrogate)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ISurrogate = MIDL_INTERFACE(
                        "{00000022-0000-0000-C000-000000000046}"
                    )
                    ISurrogate._iid_ = IID_ISurrogate

                    ISurrogate._methods_ = [
                        COMMETHOD(
                            [helpstring('Method LoadDllServer')],
                            HRESULT,
                            'LoadDllServer',
                            (['in'], REFCLSID, 'Clsid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method FreeSurrogate')],
                            HRESULT,
                            'FreeSurrogate',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ISurrogate_INTERFACE_DEFINED__

            if not defined(__IGlobalInterfaceTable_INTERFACE_DEFINED__):
                # interface IGlobalInterfaceTable
                # [uuid][object][local]
                # [unique]
                LPGLOBALINTERFACETABLE = POINTER(IGlobalInterfaceTable)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IGlobalInterfaceTable = MIDL_INTERFACE(
                        "{00000146-0000-0000-C000-000000000046}"
                    )
                    IGlobalInterfaceTable._iid_ = IID_IGlobalInterfaceTable

                    IGlobalInterfaceTable._methods_ = [
                        COMMETHOD(
                            [helpstring('Method RegisterInterfaceInGlobal')],
                            HRESULT,
                            'RegisterInterfaceInGlobal',
                            (['in'], POINTER(comtypes.IUnknown), 'pUnk'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(DWORD), 'pdwCookie'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RevokeInterfaceFromGlobal')],
                            HRESULT,
                            'RevokeInterfaceFromGlobal',
                            (['in'], DWORD, 'dwCookie'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetInterfaceFromGlobal')],
                            HRESULT,
                            'GetInterfaceFromGlobal',
                            (['in'], DWORD, 'dwCookie'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IGlobalInterfaceTable_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0029
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            if not defined(__ISynchronize_INTERFACE_DEFINED__):
                # interface ISynchronize
                # [uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ISynchronize = MIDL_INTERFACE(
                        "{00000030-0000-0000-C000-000000000046}"
                    )
                    ISynchronize._iid_ = IID_ISynchronize

                    ISynchronize._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Wait')],
                            HRESULT,
                            'Wait',
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], DWORD, 'dwMilliseconds'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Signal')],
                            HRESULT,
                            'Signal',
                        ),
                        COMMETHOD(
                            [helpstring('Method Reset')],
                            HRESULT,
                            'Reset',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ISynchronize_INTERFACE_DEFINED__

            if not defined(__ISynchronizeHandle_INTERFACE_DEFINED__):
                # interface ISynchronizeHandle
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ISynchronizeHandle = MIDL_INTERFACE(
                        "{00000031-0000-0000-C000-000000000046}"
                    )
                    ISynchronizeHandle._iid_ = IID_ISynchronizeHandle

                    ISynchronizeHandle._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetHandle')],
                            HRESULT,
                            'GetHandle',
                            (['out'], POINTER(HANDLE), 'ph'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ISynchronizeHandle_INTERFACE_DEFINED__

            if not defined(__ISynchronizeEvent_INTERFACE_DEFINED__):
                # interface ISynchronizeEvent
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ISynchronizeEvent = MIDL_INTERFACE(
                        "{00000032-0000-0000-C000-000000000046}"
                    )
                    ISynchronizeEvent._iid_ = IID_ISynchronizeEvent

                    ISynchronizeEvent._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetEventHandle')],
                            HRESULT,
                            'SetEventHandle',
                            (['in'], POINTER(HANDLE), 'ph'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ISynchronizeEvent_INTERFACE_DEFINED__

            if not defined(__ISynchronizeContainer_INTERFACE_DEFINED__):
                # interface ISynchronizeContainer
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ISynchronizeContainer = MIDL_INTERFACE(
                        "{00000033-0000-0000-C000-000000000046}"
                    )
                    ISynchronizeContainer._iid_ = IID_ISynchronizeContainer

                    ISynchronizeContainer._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddSynchronize')],
                            HRESULT,
                            'AddSynchronize',
                            (['in'], POINTER(ISynchronize), 'pSync'),
                        ),
                        COMMETHOD(
                            [helpstring('Method WaitMultiple')],
                            HRESULT,
                            'WaitMultiple',
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], DWORD, 'dwTimeOut'),
                            (
                                ['out'],
                                POINTER(POINTER(ISynchronize)),
                               'ppSync'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ISynchronizeContainer_INTERFACE_DEFINED__

            if not defined(__ISynchronizeMutex_INTERFACE_DEFINED__):
                # interface ISynchronizeMutex
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ISynchronizeMutex = MIDL_INTERFACE(
                        "{00000025-0000-0000-C000-000000000046}"
                    )
                    ISynchronizeMutex._iid_ = IID_ISynchronizeMutex

                    ISynchronizeMutex._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ReleaseMutex')],
                            HRESULT,
                            'ReleaseMutex',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ISynchronizeMutex_INTERFACE_DEFINED__

            if not defined(__ICancelMethodCalls_INTERFACE_DEFINED__):
                # interface ICancelMethodCalls
                # [uuid][object][local]
                # [unique]
                LPCANCELMETHODCALLS = POINTER(ICancelMethodCalls)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ICancelMethodCalls = MIDL_INTERFACE(
                        "{00000029-0000-0000-C000-000000000046}"
                    )
                    ICancelMethodCalls._iid_ = IID_ICancelMethodCalls

                    ICancelMethodCalls._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Cancel')],
                            HRESULT,
                            'Cancel',
                            (['in'], ULONG, 'ulSeconds'),
                        ),
                        COMMETHOD(
                            [helpstring('Method TestCancel')],
                            HRESULT,
                            'TestCancel',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ICancelMethodCalls_INTERFACE_DEFINED__

            if not defined(__IAsyncManager_INTERFACE_DEFINED__):
                # interface IAsyncManager
                # [uuid][object][local]
                class tagDCOM_CALL_STATE(ENUM):
                    DCOM_NONE = 0
                    DCOM_CALL_COMPLETE = 0x1
                    DCOM_CALL_CANCELED = 0x2

                DCOM_CALL_STATE = tagDCOM_CALL_STATE
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAsyncManager = MIDL_INTERFACE(
                        "{0000002A-0000-0000-C000-000000000046}"
                    )
                    IAsyncManager._iid_ = IID_IAsyncManager

                    IAsyncManager._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CompleteCall')],
                            HRESULT,
                            'CompleteCall',
                            (['in'], HRESULT, 'Result'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCallContext')],
                            HRESULT,
                            'GetCallContext',
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'pInterface'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetState')],
                            HRESULT,
                            'GetState',
                            (['out'], POINTER(ULONG), 'pulStateFlags'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAsyncManager_INTERFACE_DEFINED__

            if not defined(__ICallFactory_INTERFACE_DEFINED__):
                # interface ICallFactory
                # [unique][uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_ICallFactory = MIDL_INTERFACE(
                        "{1C733A30-2A1C-11CE-ADE5-00AA0044773D}"
                    )
                    ICallFactory._iid_ = IID_ICallFactory

                    ICallFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateCall')],
                            HRESULT,
                            'CreateCall',
                            (['in'], REFIID, 'riid'),
                            (['in'], POINTER(comtypes.IUnknown), 'pCtrlUnk'),
                            (['in'], REFIID, 'riid2'),
                            (
                                ['out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                               'ppv'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __ICallFactory_INTERFACE_DEFINED__

            if not defined(__IRpcHelper_INTERFACE_DEFINED__):
                # interface IRpcHelper
                # [object][local][unique][version][uuid]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IRpcHelper = MIDL_INTERFACE(
                        "{00000149-0000-0000-C000-000000000046}"
                    )
                    IRpcHelper._iid_ = IID_IRpcHelper

                    IRpcHelper._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetDCOMProtocolVersion')],
                            HRESULT,
                            'GetDCOMProtocolVersion',
                            (['out'], POINTER(DWORD), 'pComVersion'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetIIDFromOBJREF')],
                            HRESULT,
                            'GetIIDFromOBJREF',
                            (['in'], POINTER(VOID), 'pObjRef'),
                            (['out'], POINTER(POINTER(IID)), 'piid'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IRpcHelper_INTERFACE_DEFINED__

            if not defined(__IReleaseMarshalBuffers_INTERFACE_DEFINED__):
                # interface IReleaseMarshalBuffers
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IReleaseMarshalBuffers = MIDL_INTERFACE(
                        "{EB0CB9E8-7996-11D2-872E-0000F8080859}"
                    )
                    IReleaseMarshalBuffers._iid_ = IID_IReleaseMarshalBuffers

                    IReleaseMarshalBuffers._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ReleaseMarshalBuffer')],
                            HRESULT,
                            'ReleaseMarshalBuffer',
                            (['out', 'in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], POINTER(comtypes.IUnknown), 'pChnl'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IReleaseMarshalBuffers_INTERFACE_DEFINED__

            if not defined(__IWaitMultiple_INTERFACE_DEFINED__):
                # interface IWaitMultiple
                # [uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IWaitMultiple = MIDL_INTERFACE(
                        "{0000002B-0000-0000-C000-000000000046}"
                    )
                    IWaitMultiple._iid_ = IID_IWaitMultiple

                    IWaitMultiple._methods_ = [
                        COMMETHOD(
                            [helpstring('Method WaitMultiple')],
                            HRESULT,
                            'WaitMultiple',
                            (['in'], DWORD, 'timeout'),
                            (
                                ['out'],
                                POINTER(POINTER(ISynchronize)),
                               'pSync'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddSynchronize')],
                            HRESULT,
                            'AddSynchronize',
                            (['in'], POINTER(ISynchronize), 'pSync'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IWaitMultiple_INTERFACE_DEFINED__

            if not defined(__IAddrTrackingControl_INTERFACE_DEFINED__):
                # interface IAddrTrackingControl
                # [uuid][object][local]
                # [unique]
                LPADDRTRACKINGCONTROL = POINTER(IAddrTrackingControl)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAddrTrackingControl = MIDL_INTERFACE(
                        "{00000147-0000-0000-C000-000000000046}"
                    )
                    IAddrTrackingControl._iid_ = IID_IAddrTrackingControl

                    IAddrTrackingControl._methods_ = [
                        COMMETHOD(
                            [helpstring('Method EnableCOMDynamicAddrTracking')],
                            HRESULT,
                            'EnableCOMDynamicAddrTracking',
                        ),
                        COMMETHOD(
                            [helpstring('Method DisableCOMDynamicAddrTracking')],
                            HRESULT,
                            'DisableCOMDynamicAddrTracking',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAddrTrackingControl_INTERFACE_DEFINED__

            if not defined(__IAddrExclusionControl_INTERFACE_DEFINED__):
                # interface IAddrExclusionControl
                # [uuid][object][local]
                # [unique]
                LPADDREXCLUSIONCONTROL = POINTER(IAddrExclusionControl)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IAddrExclusionControl = MIDL_INTERFACE(
                        "{00000148-0000-0000-C000-000000000046}"
                    )
                    IAddrExclusionControl._iid_ = IID_IAddrExclusionControl

                    IAddrExclusionControl._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCurrentAddrExclusionList')],
                            HRESULT,
                            'GetCurrentAddrExclusionList',
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppEnumerator'),
                        ),
                        COMMETHOD(
                            [helpstring('Method UpdateAddrExclusionList')],
                            HRESULT,
                            'UpdateAddrExclusionList',
                            (
                                ['in'],
                                POINTER(comtypes.IUnknown),
                               'pEnumerator'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAddrExclusionControl_INTERFACE_DEFINED__

            if not defined(__IPipeByte_INTERFACE_DEFINED__):
                # interface IPipeByte
                # [unique][async_uuid][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPipeByte = MIDL_INTERFACE(
                        "{DB2F3ACA-2F86-11D1-8E04-00C04FB9989A}"
                    )
                    IPipeByte._iid_ = IID_IPipeByte

                    IPipeByte._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Pull')],
                            HRESULT,
                            'Pull',
                            (['out'], POINTER(BYTE), 'buf'),
                            (['in'], ULONG, 'cRequest'),
                            (['out'], POINTER(ULONG), 'pcReturned'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Push')],
                            HRESULT,
                            'Push',
                            (['in'], POINTER(BYTE), 'buf'),
                            (['in'], ULONG, 'cSent'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPipeByte_INTERFACE_DEFINED__

            if not defined(__AsyncIPipeByte_INTERFACE_DEFINED__):
                # interface AsyncIPipeByte
                # [uuid][unique][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_AsyncIPipeByte = MIDL_INTERFACE(
                        "{DB2F3ACB-2F86-11D1-8E04-00C04FB9989A}"
                    )
                    AsyncIPipeByte._iid_ = IID_AsyncIPipeByte

                    AsyncIPipeByte._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Begin_Pull')],
                            HRESULT,
                            'Begin_Pull',
                            (['in'], ULONG, 'cRequest'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finish_Pull')],
                            HRESULT,
                            'Finish_Pull',
                            (['out'], POINTER(BYTE), 'buf'),
                            (['out'], POINTER(ULONG), 'pcReturned'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Begin_Push')],
                            HRESULT,
                            'Begin_Push',
                            (['in'], POINTER(BYTE), 'buf'),
                            (['in'], ULONG, 'cSent'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finish_Push')],
                            HRESULT,
                            'Finish_Push',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __AsyncIPipeByte_INTERFACE_DEFINED__

            if not defined(__IPipeLong_INTERFACE_DEFINED__):
                # interface IPipeLong
                # [unique][async_uuid][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPipeLong = MIDL_INTERFACE(
                        "{DB2F3ACC-2F86-11D1-8E04-00C04FB9989A}"
                    )
                    IPipeLong._iid_ = IID_IPipeLong

                    IPipeLong._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Pull')],
                            HRESULT,
                            'Pull',
                            (['out'], POINTER(LONG), 'buf'),
                            (['in'], ULONG, 'cRequest'),
                            (['out'], POINTER(ULONG), 'pcReturned'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Push')],
                            HRESULT,
                            'Push',
                            (['in'], POINTER(LONG), 'buf'),
                            (['in'], ULONG, 'cSent'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPipeLong_INTERFACE_DEFINED__

            if not defined(__AsyncIPipeLong_INTERFACE_DEFINED__):
                # interface AsyncIPipeLong
                # [uuid][unique][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_AsyncIPipeLong = MIDL_INTERFACE(
                        "{DB2F3ACD-2F86-11D1-8E04-00C04FB9989A}"
                    )
                    AsyncIPipeLong._iid_ = IID_AsyncIPipeLong

                    AsyncIPipeLong._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Begin_Pull')],
                            HRESULT,
                            'Begin_Pull',
                            (['in'], ULONG, 'cRequest'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finish_Pull')],
                            HRESULT,
                            'Finish_Pull',
                            (['out'], POINTER(LONG), 'buf'),
                            (['out'], POINTER(ULONG), 'pcReturned'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Begin_Push')],
                            HRESULT,
                            'Begin_Push',
                            (['in'], POINTER(LONG), 'buf'),
                            (['in'], ULONG, 'cSent'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finish_Push')],
                            HRESULT,
                            'Finish_Push',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __AsyncIPipeLong_INTERFACE_DEFINED__

            if not defined(__IPipeDouble_INTERFACE_DEFINED__):
                # interface IPipeDouble
                # [unique][async_uuid][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPipeDouble = MIDL_INTERFACE(
                        "{DB2F3ACE-2F86-11D1-8E04-00C04FB9989A}"
                    )
                    IPipeDouble._iid_ = IID_IPipeDouble

                    IPipeDouble._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Pull')],
                            HRESULT,
                            'Pull',
                            (['out'], POINTER(DOUBLE), 'buf'),
                            (['in'], ULONG, 'cRequest'),
                            (['out'], POINTER(ULONG), 'pcReturned'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Push')],
                            HRESULT,
                            'Push',
                            (['in'], POINTER(DOUBLE), 'buf'),
                            (['in'], ULONG, 'cSent'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPipeDouble_INTERFACE_DEFINED__

            if not defined(__AsyncIPipeDouble_INTERFACE_DEFINED__):
                # interface AsyncIPipeDouble
                # [uuid][unique][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_AsyncIPipeDouble = MIDL_INTERFACE(
                        "{DB2F3ACF-2F86-11D1-8E04-00C04FB9989A}"
                    )
                    AsyncIPipeDouble._iid_ = IID_AsyncIPipeDouble

                    AsyncIPipeDouble._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Begin_Pull')],
                            HRESULT,
                            'Begin_Pull',
                            (['in'], ULONG, 'cRequest'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finish_Pull')],
                            HRESULT,
                            'Finish_Pull',
                            (['out'], POINTER(DOUBLE), 'buf'),
                            (['out'], POINTER(ULONG), 'pcReturned'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Begin_Push')],
                            HRESULT,
                            'Begin_Push',
                            (['in'], POINTER(DOUBLE), 'buf'),
                            (['in'], ULONG, 'cSent'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Finish_Push')],
                            HRESULT,
                            'Finish_Push',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __AsyncIPipeDouble_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0045
            # [local]

            if (
                defined(USE_COM_CONTEXT_DEF) or
                defined(BUILDTYPE_COMSVCS) or
                defined(_COMBASEAPI_) or
                defined(_OLE32_)
            ):

                CPFLAGS = DWORD

                tagContextProperty._fields_ = [
                    ('policyId', GUID),
                    ('flags', CPFLAGS),
                    # [unique]
                    ('pUnk', POINTER(comtypes.IUnknown)),
                ]
                if not defined(__IEnumContextProps_INTERFACE_DEFINED__):
                    # interface IEnumContextProps
                    # [unique][uuid][object][local]
                    # [unique]
                    LPENUMCONTEXTPROPS = POINTER(IEnumContextProps)
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IEnumContextProps = MIDL_INTERFACE(
                            "{000001C1-0000-0000-C000-000000000046}"
                        )
                        IEnumContextProps._iid_ = IID_IEnumContextProps

                        IEnumContextProps._methods_ = [
                            COMMETHOD(
                                [helpstring('Method Next')],
                                HRESULT,
                                'Next',
                                (['in'], ULONG, 'celt'),
                                (
                                    ['out'],
                                    POINTER(ContextProperty),
                                   'pContextProperties'
                                ),
                                (['out'], POINTER(ULONG), 'pceltFetched'),
                            ),
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
                                    POINTER(POINTER(IEnumContextProps)),
                                   'ppEnumContextProps'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method Count')],
                                HRESULT,
                                'Count',
                                (['out'], POINTER(ULONG), 'pcelt'),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IEnumContextProps_INTERFACE_DEFINED__

                if not defined(__IContext_INTERFACE_DEFINED__):
                    # interface IContext
                    # [unique][uuid][object][local]
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IContext = MIDL_INTERFACE(
                            "{000001C0-0000-0000-C000-000000000046}"
                        )
                        IContext._iid_ = IID_IContext

                        IContext._methods_ = [
                            COMMETHOD(
                                [helpstring('Method SetProperty')],
                                HRESULT,
                                'SetProperty',
                                (['in'], REFGUID, 'rpolicyId'),
                                (['in'], CPFLAGS, 'flags'),
                                (['in'], POINTER(comtypes.IUnknown), 'pUnk'),
                            ),
                            COMMETHOD(
                                [helpstring('Method RemoveProperty')],
                                HRESULT,
                                'RemoveProperty',
                                (['in'], REFGUID, 'rPolicyId'),
                            ),
                            COMMETHOD(
                                [helpstring('Method GetProperty')],
                                HRESULT,
                                'GetProperty',
                                (['in'], REFGUID, 'rGuid'),
                                (['out'], POINTER(CPFLAGS), 'pFlags'),
                                (
                                    ['out'],
                                    POINTER(POINTER(comtypes.IUnknown)),
                                   'ppUnk'
                                ),
                            ),
                            COMMETHOD(
                                [helpstring('Method EnumContextProps')],
                                HRESULT,
                                'EnumContextProps',
                                (
                                    ['out'],
                                    POINTER(POINTER(IEnumContextProps)),
                                   'ppEnumContextProps'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IContext_INTERFACE_DEFINED__

                # interface __MIDL_itf_objidlbase_0000_0047
                # [local]
                if (
                    not defined(BUILDTYPE_COMSVCS) and
                    not (defined(_COMBASEAPI_) or defined(_OLE32_))
                ):
                    if not defined(__IObjContext_INTERFACE_DEFINED__):
                        # interface IObjContext
                        # [unique][uuid][object][local]
                        if defined(__cplusplus) and not defined(CINTERFACE):
                            pass
                        else:
                            IID_IObjContext = MIDL_INTERFACE(
                                "{000001C6-0000-0000-C000-000000000046}"
                            )
                            IObjContext._iid_ = IID_IObjContext

                            IObjContext._methods_ = [
                                COMMETHOD(
                                    [helpstring('Method Reserved1')],
                                    VOID,
                                    'Reserved1',
                                ),
                                COMMETHOD(
                                    [helpstring('Method Reserved2')],
                                    VOID,
                                    'Reserved2',
                                ),
                                COMMETHOD(
                                    [helpstring('Method Reserved3')],
                                    VOID,
                                    'Reserved3',
                                ),
                                COMMETHOD(
                                    [helpstring('Method Reserved4')],
                                    VOID,
                                    'Reserved4',
                                ),
                                COMMETHOD(
                                    [helpstring('Method Reserved5')],
                                    VOID,
                                    'Reserved5',
                                ),
                                COMMETHOD(
                                    [helpstring('Method Reserved6')],
                                    VOID,
                                    'Reserved6',
                                ),
                                COMMETHOD(
                                    [helpstring('Method Reserved7')],
                                    VOID,
                                    'Reserved7',
                                ),
                            ]

                        # END IF  C style interface
                    # END IF  __IObjContext_INTERFACE_DEFINED__

                    # interface __MIDL_itf_objidlbase_0000_0048
                    # [local]                # END IF
            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            class _APTTYPEQUALIFIER(ENUM):
                APTTYPEQUALIFIER_NONE = 0
                APTTYPEQUALIFIER_IMPLICIT_MTA = 1
                APTTYPEQUALIFIER_NA_ON_MTA = 2
                APTTYPEQUALIFIER_NA_ON_STA = 3
                APTTYPEQUALIFIER_NA_ON_IMPLICIT_MTA = 4
                APTTYPEQUALIFIER_NA_ON_MAINSTA = 5
                APTTYPEQUALIFIER_APPLICATION_STA = 6

            APTTYPEQUALIFIER = _APTTYPEQUALIFIER


            class _APTTYPE(ENUM):
                APTTYPE_CURRENT = - 1
                APTTYPE_STA = 0
                APTTYPE_MTA = 1
                APTTYPE_NA = 2
                APTTYPE_MAINSTA = 3

            APTTYPE = _APTTYPE
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            class _THDTYPE(ENUM):
                THDTYPE_BLOCKMESSAGES = 0
                THDTYPE_PROCESSMESSAGES = 1

            THDTYPE = _THDTYPE
            APARTMENTID = DWORD
            if not defined(__IComThreadingInfo_INTERFACE_DEFINED__):
                # interface IComThreadingInfo
                # [unique][uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IComThreadingInfo = MIDL_INTERFACE(
                        "{000001CE-0000-0000-C000-000000000046}"
                    )
                    IComThreadingInfo._iid_ = IID_IComThreadingInfo

                    IComThreadingInfo._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCurrentApartmentType')],
                            HRESULT,
                            'GetCurrentApartmentType',
                            (['out'], POINTER(APTTYPE), 'pAptType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentThreadType')],
                            HRESULT,
                            'GetCurrentThreadType',
                            (['out'], POINTER(THDTYPE), 'pThreadType'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentLogicalThreadId')],
                            HRESULT,
                            'GetCurrentLogicalThreadId',
                            (['out'], POINTER(GUID), 'pguidLogicalThreadId'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCurrentLogicalThreadId')],
                            HRESULT,
                            'SetCurrentLogicalThreadId',
                            (['in'], REFGUID, 'rguid'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IComThreadingInfo_INTERFACE_DEFINED__

            if not defined(__IProcessInitControl_INTERFACE_DEFINED__):
                # interface IProcessInitControl
                # [uuid][unique][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IProcessInitControl = MIDL_INTERFACE(
                        "{72380D55-8D2B-43A3-8513-2B6EF31434E9}"
                    )
                    IProcessInitControl._iid_ = IID_IProcessInitControl

                    IProcessInitControl._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ResetInitializerTimeout')],
                            HRESULT,
                            'ResetInitializerTimeout',
                            (['in'], DWORD, 'dwSecondsRemaining'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IProcessInitControl_INTERFACE_DEFINED__

            if not defined(__IFastRundown_INTERFACE_DEFINED__):
                # interface IFastRundown
                # [uuid][unique][local][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IFastRundown = MIDL_INTERFACE(
                        "{00000040-0000-0000-C000-000000000046}"
                    )
                    IFastRundown._iid_ = IID_IFastRundown

                    IFastRundown._methods_ = []


                # END IF  C style interface
            # END IF  __IFastRundown_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0051
            # [local]
            class CO_MARSHALING_CONTEXT_ATTRIBUTES(ENUM):
                CO_MARSHALING_SOURCE_IS_APP_CONTAINER = 0
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_1 = 0x80000000
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_2 = 0x80000001
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_3 = 0x80000002
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_4 = 0x80000003
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_5 = 0x80000004
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_6 = 0x80000005
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_7 = 0x80000006
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_8 = 0x80000007
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_9 = 0x80000008
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_10 = 0x80000009
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_11 = 0x8000000A
                CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_12 = 0x8000000B

            if not defined(__IMarshalingStream_INTERFACE_DEFINED__):
                # interface IMarshalingStream
                # [unique][uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IMarshalingStream = MIDL_INTERFACE(
                        "{D8F2F5E6-6102-4863-9F26-389A4676EFDE}"
                    )
                    IMarshalingStream._iid_ = IID_IMarshalingStream

                    IMarshalingStream._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetMarshalingContextAttribute')],
                            HRESULT,
                            'GetMarshalingContextAttribute',
                            (
                                ['in'],
                                CO_MARSHALING_CONTEXT_ATTRIBUTES,
                               'attribute'
                            ),
                            (['out'], POINTER(ULONG_PTR), 'pAttributeValue'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IMarshalingStream_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidlbase_0000_0052
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if not defined(__IAgileReference_INTERFACE_DEFINED__):
                # interface IAgileReference
                # [unique][uuid][object][local]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else:
                        IID_IAgileReference = MIDL_INTERFACE(
                            "{C03F6A43-65A4-9818-987E-E0B810D2A6F2}"
                        )
                        IAgileReference._iid_ = IID_IAgileReference

                        IAgileReference._methods_ = [
                            COMMETHOD(
                                [helpstring('Method Resolve')],
                                HRESULT,
                                'Resolve',
                                (['in'], REFIID, 'riid'),
                                (
                                    ['out', 'iid_is', 'retval'],
                                    POINTER(POINTER(VOID)),
                                   'ppvObjectReference'
                                ),
                            ),
                        ]

                    # END IF  C style interface
                # END IF  __IAgileReference_INTERFACE_DEFINED__

                # interface __MIDL_itf_objidlbase_0000_0053
                # [local]
            # END IF
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF

    if  _MSC_VER >= 800 :
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF
    # END IF

    ole32 = ctypes.windll.OLE32

    # HRESULT STDMETHODCALLTYPE IStream_Seek_Proxy( // [local]
    # IStream * This,
    # LARGE_INTEGER dlibMove, // [in]
    # DWORD dwOrigin, // [in]
    # // [annotation]
    # _Out_opt_  ULARGE_INTEGER *plibNewPosition);
    IStream_Seek_Proxy = ole32.IStream_Seek_Proxy
    IStream_Seek_Proxy.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStream_Seek_Stub( // [call_as]
    # __RPC__in IStream * This,
    # LARGE_INTEGER dlibMove, // [in]
    # DWORD dwOrigin, // [in]
    # __RPC__out ULARGE_INTEGER *plibNewPosition); // [out]
    IStream_Seek_Stub = ole32.IStream_Seek_Stub
    IStream_Seek_Stub.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStream_CopyTo_Proxy( // [local]
    # IStream * This,
    # // [annotation][unique][in]
    # _In_  IStream *pstm,
    # ULARGE_INTEGER cb, // [in]
    # // [annotation]
    # _Out_opt_  ULARGE_INTEGER *pcbRead,
    # // [annotation]
    # _Out_opt_  ULARGE_INTEGER *pcbWritten);
    IStream_CopyTo_Proxy = ole32.IStream_CopyTo_Proxy
    IStream_CopyTo_Proxy.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStream_CopyTo_Stub( // [call_as]
    # __RPC__in IStream * This,
    # __RPC__in_opt IStream *pstm, // [unique][in]
    # ULARGE_INTEGER cb, // [in]
    # __RPC__out ULARGE_INTEGER *pcbRead, // [out]
    # __RPC__out ULARGE_INTEGER *pcbWritten); // [out]
    IStream_CopyTo_Stub = ole32.IStream_CopyTo_Stub
    IStream_CopyTo_Stub.restype = HRESULT

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


