import ctypes
import comtypes
import comtypes.automation
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *

IDispatch = comtypes.automation.IDispatch
COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__objidl_h__ = None
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
__IMallocSpy_FWD_DEFINED__ = None
__IBindCtx_FWD_DEFINED__ = None
__IEnumMoniker_FWD_DEFINED__ = None
__IRunnableObject_FWD_DEFINED__ = None
__IRunningObjectTable_FWD_DEFINED__ = None
__IPersist_FWD_DEFINED__ = None
__IPersistStream_FWD_DEFINED__ = None
__IMoniker_FWD_DEFINED__ = None
__IROTData_FWD_DEFINED__ = None
__IEnumSTATSTG_FWD_DEFINED__ = None
__IStorage_FWD_DEFINED__ = None
__IPersistFile_FWD_DEFINED__ = None
__IPersistStorage_FWD_DEFINED__ = None
__ILockBytes_FWD_DEFINED__ = None
__IEnumFORMATETC_FWD_DEFINED__ = None
__IEnumSTATDATA_FWD_DEFINED__ = None
__IRootStorage_FWD_DEFINED__ = None
__IAdviseSink_FWD_DEFINED__ = None
__AsyncIAdviseSink_FWD_DEFINED__ = None
__IAdviseSink2_FWD_DEFINED__ = None
__AsyncIAdviseSink2_FWD_DEFINED__ = None
__IDataObject_FWD_DEFINED__ = None
__IDataAdviseHolder_FWD_DEFINED__ = None
__IMessageFilter_FWD_DEFINED__ = None
__IClassActivator_FWD_DEFINED__ = None
__IFillLockBytes_FWD_DEFINED__ = None
__IProgressNotify_FWD_DEFINED__ = None
__ILayoutStorage_FWD_DEFINED__ = None
__IBlockingLock_FWD_DEFINED__ = None
__ITimeAndNoticeControl_FWD_DEFINED__ = None
__IOplockStorage_FWD_DEFINED__ = None
__IDirectWriterLock_FWD_DEFINED__ = None
__IUrlMon_FWD_DEFINED__ = None
__IForegroundTransfer_FWD_DEFINED__ = None
__IThumbnailExtractor_FWD_DEFINED__ = None
__IDummyHICONIncluder_FWD_DEFINED__ = None
__IProcessLock_FWD_DEFINED__ = None
__ISurrogateService_FWD_DEFINED__ = None
__IInitializeSpy_FWD_DEFINED__ = None
__IApartmentShutdown_FWD_DEFINED__ = None
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
__IMallocSpy_INTERFACE_DEFINED__ = None
__IBindCtx_INTERFACE_DEFINED__ = None
__IEnumMoniker_INTERFACE_DEFINED__ = None
__IRunnableObject_INTERFACE_DEFINED__ = None
__IRunningObjectTable_INTERFACE_DEFINED__ = None
__IPersist_INTERFACE_DEFINED__ = None
__IPersistStream_INTERFACE_DEFINED__ = None
__IMoniker_INTERFACE_DEFINED__ = None
__IROTData_INTERFACE_DEFINED__ = None
__IEnumSTATSTG_INTERFACE_DEFINED__ = None
__IStorage_INTERFACE_DEFINED__ = None
__IPersistFile_INTERFACE_DEFINED__ = None
__IPersistStorage_INTERFACE_DEFINED__ = None
__ILockBytes_INTERFACE_DEFINED__ = None
__IEnumFORMATETC_INTERFACE_DEFINED__ = None
__IEnumSTATDATA_INTERFACE_DEFINED__ = None
__IRootStorage_INTERFACE_DEFINED__ = None
__IAdviseSink_INTERFACE_DEFINED__ = None
NONAMELESSUNION = None
__AsyncIAdviseSink_INTERFACE_DEFINED__ = None
__IAdviseSink2_INTERFACE_DEFINED__ = None
__AsyncIAdviseSink2_INTERFACE_DEFINED__ = None
__IDataObject_INTERFACE_DEFINED__ = None
__IDataAdviseHolder_INTERFACE_DEFINED__ = None
__IMessageFilter_INTERFACE_DEFINED__ = None
__IClassActivator_INTERFACE_DEFINED__ = None
__IFillLockBytes_INTERFACE_DEFINED__ = None
__IProgressNotify_INTERFACE_DEFINED__ = None
__ILayoutStorage_INTERFACE_DEFINED__ = None
__IBlockingLock_INTERFACE_DEFINED__ = None
__ITimeAndNoticeControl_INTERFACE_DEFINED__ = None
__IOplockStorage_INTERFACE_DEFINED__ = None
__IDirectWriterLock_INTERFACE_DEFINED__ = None
__IUrlMon_INTERFACE_DEFINED__ = None
__IForegroundTransfer_INTERFACE_DEFINED__ = None
__IThumbnailExtractor_INTERFACE_DEFINED__ = None
__IDummyHICONIncluder_INTERFACE_DEFINED__ = None
__IProcessLock_INTERFACE_DEFINED__ = None
__ISurrogateService_INTERFACE_DEFINED__ = None
__IInitializeSpy_INTERFACE_DEFINED__ = None
__IApartmentShutdown_INTERFACE_DEFINED__ = None
BUILDTYPE_COMSVCS = None
_COMBASEAPI_ = None
_OLE32_ = None
USE_COM_CONTEXT_DEF = None


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


class tagBIND_OPTS(ctypes.Structure):
    pass


BIND_OPTS = tagBIND_OPTS


BIND_OPTS2 = tagBIND_OPTS
LPBIND_OPTS2 = POINTER(tagBIND_OPTS)


class tagBIND_OPTS2(ctypes.Structure):
    pass


BIND_OPTS2 = tagBIND_OPTS2


BIND_OPTS3 = tagBIND_OPTS2
LPBIND_OPTS3 = POINTER(tagBIND_OPTS2)


class tagBIND_OPTS3(ctypes.Structure):
    pass


BIND_OPTS3 = tagBIND_OPTS3


class tagRemSNB(ctypes.Structure):
    pass


RemSNB = tagRemSNB


class tagDVTARGETDEVICE(ctypes.Structure):
    pass


DVTARGETDEVICE = tagDVTARGETDEVICE


class tagFORMATETC(ctypes.Structure):
    pass


FORMATETC = tagFORMATETC


class tagSTATDATA(ctypes.Structure):
    pass


STATDATA = tagSTATDATA


class tagRemSTGMEDIUM(ctypes.Structure):
    pass


RemSTGMEDIUM = tagRemSTGMEDIUM


class tagSTGMEDIUM(ctypes.Structure):
    pass


uSTGMEDIUM = tagSTGMEDIUM


uSTGMEDIUM = tagSTGMEDIUM


class _GDI_OBJECT(ctypes.Structure):
    pass


GDI_OBJECT = _GDI_OBJECT


class _userSTGMEDIUM(ctypes.Structure):
    pass


userSTGMEDIUM = _userSTGMEDIUM


class _userFLAG_STGMEDIUM(ctypes.Structure):
    pass


userFLAG_STGMEDIUM = _userFLAG_STGMEDIUM


class _FLAG_STGMEDIUM(ctypes.Structure):
    pass


FLAG_STGMEDIUM = _FLAG_STGMEDIUM


class tagINTERFACEINFO(ctypes.Structure):
    pass


INTERFACEINFO = tagINTERFACEINFO


class tagStorageLayout(ctypes.Structure):
    pass


StorageLayout = tagStorageLayout



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
    from pyWinAPI.shared.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H


if not defined(__objidl_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

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
        class IStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

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

    if not defined(__IMallocSpy_FWD_DEFINED__):
        class IMallocSpy(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMallocSpy_FWD_DEFINED__

    if not defined(__IBindCtx_FWD_DEFINED__):
        class IBindCtx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IBindCtx_FWD_DEFINED__

    if not defined(__IEnumMoniker_FWD_DEFINED__):
        class IEnumMoniker(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumMoniker_FWD_DEFINED__

    if not defined(__IRunnableObject_FWD_DEFINED__):
        class IRunnableObject(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRunnableObject_FWD_DEFINED__

    if not defined(__IRunningObjectTable_FWD_DEFINED__):
        class IRunningObjectTable(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRunningObjectTable_FWD_DEFINED__

    if not defined(__IPersist_FWD_DEFINED__):
        class IPersist(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersist_FWD_DEFINED__

    if not defined(__IPersistStream_FWD_DEFINED__):
        class IPersistStream(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistStream_FWD_DEFINED__

    if not defined(__IMoniker_FWD_DEFINED__):

        class IMoniker(IPersistStream):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None
    # END IF  __IMoniker_FWD_DEFINED__

    if not defined(__IROTData_FWD_DEFINED__):
        class IROTData(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IROTData_FWD_DEFINED__

    if not defined(__IEnumSTATSTG_FWD_DEFINED__):
        class IEnumSTATSTG(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumSTATSTG_FWD_DEFINED__

    if not defined(__IStorage_FWD_DEFINED__):
        class IStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IStorage_FWD_DEFINED__

    if not defined(__IPersistFile_FWD_DEFINED__):
        class IPersistFile(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistFile_FWD_DEFINED__

    if not defined(__IPersistStorage_FWD_DEFINED__):
        class IPersistStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistStorage_FWD_DEFINED__

    if not defined(__ILockBytes_FWD_DEFINED__):
        class ILockBytes(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ILockBytes_FWD_DEFINED__

    if not defined(__IEnumFORMATETC_FWD_DEFINED__):
        class IEnumFORMATETC(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumFORMATETC_FWD_DEFINED__

    if not defined(__IEnumSTATDATA_FWD_DEFINED__):
        class IEnumSTATDATA(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumSTATDATA_FWD_DEFINED__

    if not defined(__IRootStorage_FWD_DEFINED__):
        class IRootStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRootStorage_FWD_DEFINED__

    if not defined(__IAdviseSink_FWD_DEFINED__):
        class IAdviseSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAdviseSink_FWD_DEFINED__

    if not defined(__AsyncIAdviseSink_FWD_DEFINED__):
        class AsyncIAdviseSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __AsyncIAdviseSink_FWD_DEFINED__

    if not defined(__IAdviseSink2_FWD_DEFINED__):
        class IAdviseSink2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAdviseSink2_FWD_DEFINED__

    if not defined(__AsyncIAdviseSink2_FWD_DEFINED__):
        class AsyncIAdviseSink2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __AsyncIAdviseSink2_FWD_DEFINED__

    if not defined(__IDataObject_FWD_DEFINED__):
        class IDataObject(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDataObject_FWD_DEFINED__

    if not defined(__IDataAdviseHolder_FWD_DEFINED__):
        class IDataAdviseHolder(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDataAdviseHolder_FWD_DEFINED__

    if not defined(__IMessageFilter_FWD_DEFINED__):
        class IMessageFilter(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMessageFilter_FWD_DEFINED__

    if not defined(__IClassActivator_FWD_DEFINED__):
        class IClassActivator(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IClassActivator_FWD_DEFINED__

    if not defined(__IFillLockBytes_FWD_DEFINED__):
        class IFillLockBytes(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IFillLockBytes_FWD_DEFINED__

    if not defined(__IProgressNotify_FWD_DEFINED__):
        class IProgressNotify(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProgressNotify_FWD_DEFINED__

    if not defined(__ILayoutStorage_FWD_DEFINED__):
        class ILayoutStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ILayoutStorage_FWD_DEFINED__

    if not defined(__IBlockingLock_FWD_DEFINED__):
        class IBlockingLock(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IBlockingLock_FWD_DEFINED__

    if not defined(__ITimeAndNoticeControl_FWD_DEFINED__):
        class ITimeAndNoticeControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITimeAndNoticeControl_FWD_DEFINED__

    if not defined(__IOplockStorage_FWD_DEFINED__):
        class IOplockStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOplockStorage_FWD_DEFINED__

    if not defined(__IDirectWriterLock_FWD_DEFINED__):
        class IDirectWriterLock(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDirectWriterLock_FWD_DEFINED__

    if not defined(__IUrlMon_FWD_DEFINED__):
        class IUrlMon(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUrlMon_FWD_DEFINED__

    if not defined(__IForegroundTransfer_FWD_DEFINED__):
        class IForegroundTransfer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IForegroundTransfer_FWD_DEFINED__

    if not defined(__IThumbnailExtractor_FWD_DEFINED__):
        class IThumbnailExtractor(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IThumbnailExtractor_FWD_DEFINED__

    if not defined(__IDummyHICONIncluder_FWD_DEFINED__):
        class IDummyHICONIncluder(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDummyHICONIncluder_FWD_DEFINED__

    if not defined(__IProcessLock_FWD_DEFINED__):
        class IProcessLock(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProcessLock_FWD_DEFINED__

    if not defined(__ISurrogateService_FWD_DEFINED__):
        class ISurrogateService(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISurrogateService_FWD_DEFINED__

    if not defined(__IInitializeSpy_FWD_DEFINED__):
        class IInitializeSpy(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IInitializeSpy_FWD_DEFINED__

    if not defined(__IApartmentShutdown_FWD_DEFINED__):
        class IApartmentShutdown(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IApartmentShutdown_FWD_DEFINED__

    # header files for imported files
    from unknwn_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_objidl_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import *  # NOQA
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

    if (NTDDI_VERSION >= NTDDI_WS03 and not defined(_WIN32_WINNT)):
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WINXP and not defined(_WIN32_WINNT):
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K and not defined(_WIN32_WINNT):
        pass
    # END IF

    if _MSC_VER >= 800:
        if _MSC_VER >= 1200:
            pass
        # END IF
    # END IF

    if _MSC_VER >= 1020:
        pass
    # END IF

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

    if (NTDDI_VERSION >= NTDDI_WS03 and not defined(_WIN32_WINNT)):
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WINXP and not defined(_WIN32_WINNT):
        pass
    # END IF

    if NTDDI_VERSION >= NTDDI_WIN2K and not defined(_WIN32_WINNT):
        pass
    # END IF

    if  _MSC_VER >= 800:
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

            # interface __MIDL_itf_objidl_0000_0003
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
                            [helpstring('Method Alloc')],
                            VOID,
                            'Alloc',
                            (['in'], SIZE_T, 'cb'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Realloc')],
                            VOID,
                            'Realloc',
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

            # interface __MIDL_itf_objidl_0000_0008
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

            # interface __MIDL_itf_objidl_0000_0009
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

            # interface __MIDL_itf_objidl_0000_0010
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

            # interface __MIDL_itf_objidl_0000_0015
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

            # interface __MIDL_itf_objidl_0000_0020
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

            # interface __MIDL_itf_objidl_0000_0022
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

                # interface __MIDL_itf_objidl_0000_0023
                # [local]            # END IF  DCOM
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

                # interface __MIDL_itf_objidl_0000_0024
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

                # interface __MIDL_itf_objidl_0000_0025
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

                # interface __MIDL_itf_objidl_0000_0026
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

                # interface __MIDL_itf_objidl_0000_0027
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

            # interface __MIDL_itf_objidl_0000_0029
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

            # interface __MIDL_itf_objidl_0000_0045
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

                # interface __MIDL_itf_objidl_0000_0047
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

                    # interface __MIDL_itf_objidl_0000_0048
                    # [local]
                # END IF
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

            # interface __MIDL_itf_objidl_0000_0051
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

            # interface __MIDL_itf_objidl_0000_0052
            # [local]
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if not defined(__IAgileReference_INTERFACE_DEFINED__):
                # interface IAgileReference
                # [unique][uuid][object][local]
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
                                ['iid_is', 'out', 'retval'],
                                POINTER(POINTER(VOID)),
                                'ppvObjectReference'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IAgileReference_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidl_0000_0053
            # [local]            # END IF
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


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IMallocSpy_INTERFACE_DEFINED__):
            # interface IMallocSpy
            # [uuid][object][local]
            # [unique]
            LPMALLOCSPY = POINTER(IMallocSpy)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMallocSpy = MIDL_INTERFACE(
                    "{0000001D-0000-0000-C000-000000000046}"
                )
                IMallocSpy._iid_ = IID_IMallocSpy


                IMallocSpy._methods_ = [
                    COMMETHOD(
                        [helpstring('Method PreAlloc')],
                        SIZE_T,
                        'PreAlloc',
                        (['in'], SIZE_T, 'cbRequest'),
                    ),
                    COMMETHOD(
                        [helpstring('Method *PostAlloc')],
                        VOID,
                        'PostAlloc',
                        (['in'], POINTER(VOID), 'pActual'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PreFree')],
                        VOID,
                        'PreFree',
                        (['in'], POINTER(VOID), 'pRequest'),
                        (['in'], BOOL, 'fSpyed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PostFree')],
                        VOID,
                        'PostFree',
                        (['in'], BOOL, 'fSpyed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PreRealloc')],
                        SIZE_T,
                        'PreRealloc',
                        (['in'], POINTER(VOID), 'pRequest'),
                        (['in'], SIZE_T, 'cbRequest'),
                        (['out'], POINTER(POINTER(VOID)), 'ppNewRequest'),
                        (['in'], BOOL, 'fSpyed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PostRealloc')],
                        VOID,
                        'PostRealloc',
                        (['in'], POINTER(VOID), 'pActual'),
                        (['in'], BOOL, 'fSpyed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PreGetSize')],
                        VOID,
                        'PreGetSize',
                        (['in'], POINTER(VOID), 'pRequest'),
                        (['in'], BOOL, 'fSpyed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PostGetSize')],
                        SIZE_T,
                        'PostGetSize',
                        (['in'], SIZE_T, 'cbActual'),
                        (['in'], BOOL, 'fSpyed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PreDidAlloc')],
                        VOID,
                        'PreDidAlloc',
                        (['in'], POINTER(VOID), 'pRequest'),
                        (['in'], BOOL, 'fSpyed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PostDidAlloc')],
                        INT,
                        'PostDidAlloc',
                        (['in'], POINTER(VOID), 'pRequest'),
                        (['in'], BOOL, 'fSpyed'),
                        (['in'], INT, 'fActual'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PreHeapMinimize')],
                        VOID,
                        'PreHeapMinimize',
                    ),
                    COMMETHOD(
                        [helpstring('Method PostHeapMinimize')],
                        VOID,
                        'PostHeapMinimize',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMallocSpy_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0054
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IBindCtx_INTERFACE_DEFINED__):
            # interface IBindCtx
            # [unique][uuid][object]
            # [unique]
            LPBC = POINTER(IBindCtx)

            # [unique]
            LPBINDCTX = POINTER(IBindCtx)
            if defined(__cplusplus):
                pass
            else:
                tagBIND_OPTS._fields_ = [
                    ('cbStruct', DWORD),
                    ('grfFlags', DWORD),
                    ('grfMode', DWORD),
                    ('dwTickCountDeadline', DWORD),
                ]
                LPBIND_OPTS = POINTER(tagBIND_OPTS)

            # END IF

            if defined(__cplusplus):
                tagBIND_OPTS._fields_ = [
                    ('dwTrackFlags', DWORD),
                    ('dwClassContext', DWORD),
                    ('locale', LCID),
                    ('pServerInfo', POINTER(COSERVERINFO)),
                ]
            else:
                tagBIND_OPTS2._fields_ = [
                    ('cbStruct', DWORD),
                    ('grfFlags', DWORD),
                    ('grfMode', DWORD),
                    ('dwTickCountDeadline', DWORD),
                    ('dwTrackFlags', DWORD),
                    ('dwClassContext', DWORD),
                    ('locale', LCID),
                    ('pServerInfo', POINTER(COSERVERINFO)),
                ]
                LPBIND_OPTS2 = POINTER(tagBIND_OPTS2)

            # END IF

            if defined(__cplusplus):
                pass
            else:
                tagBIND_OPTS3._fields_ = [
                    ('cbStruct', DWORD),
                    ('grfFlags', DWORD),
                    ('grfMode', DWORD),
                    ('dwTickCountDeadline', DWORD),
                    ('dwTrackFlags', DWORD),
                    ('dwClassContext', DWORD),
                    ('locale', LCID),
                    ('pServerInfo', POINTER(COSERVERINFO)),
                    ('hwnd', HWND),
                ]
                LPBIND_OPTS3 = POINTER(tagBIND_OPTS3)

            # END IF

            class tagBIND_FLAGS(ENUM):
                BIND_MAYBOTHERUSER = 1
                BIND_JUSTTESTEXISTENCE = 2

            BIND_FLAGS = tagBIND_FLAGS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IBindCtx = MIDL_INTERFACE(
                    "{0000000E-0000-0000-C000-000000000046}"
                )
                IBindCtx._iid_ = IID_IBindCtx


                IBindCtx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method RegisterObjectBound')],
                        HRESULT,
                        'RegisterObjectBound',
                        (
                            ['in', 'unique'],
                            POINTER(comtypes.IUnknown),
                            'punk'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method RevokeObjectBound')],
                        HRESULT,
                        'RevokeObjectBound',
                        (
                            ['unique', 'in'],
                            POINTER(comtypes.IUnknown),
                            'punk'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseBoundObjects')],
                        HRESULT,
                        'ReleaseBoundObjects',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetBindOptions'), 'local'],
                        HRESULT,
                        'SetBindOptions',
                        (['in'], POINTER(BIND_OPTS), 'pbindopts'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetBindOptions'), 'local'],
                        HRESULT,
                        'GetBindOptions',
                        (['out', 'in'], POINTER(BIND_OPTS), 'pbindopts'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRunningObjectTable')],
                        HRESULT,
                        'GetRunningObjectTable',
                        (
                            ['out'],
                            POINTER(POINTER(IRunningObjectTable)),
                            'pprot'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method RegisterObjectParam')],
                        HRESULT,
                        'RegisterObjectParam',
                        (['in'], LPOLESTR, 'pszKey'),
                        (
                            ['unique', 'in'],
                            POINTER(comtypes.IUnknown),
                            'punk'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetObjectParam')],
                        HRESULT,
                        'GetObjectParam',
                        (['in'], LPOLESTR, 'pszKey'),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'ppunk'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumObjectParam')],
                        HRESULT,
                        'EnumObjectParam',
                        (['out'], POINTER(POINTER(IEnumString)), 'ppenum'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RevokeObjectParam')],
                        HRESULT,
                        'RevokeObjectParam',
                        (['in'], LPOLESTR, 'pszKey'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IBindCtx_INTERFACE_DEFINED__

        if not defined(__IEnumMoniker_INTERFACE_DEFINED__):
            # interface IEnumMoniker
            # [unique][uuid][object]
            # [unique]
            LPENUMMONIKER = POINTER(IEnumMoniker)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumMoniker = MIDL_INTERFACE(
                    "{00000102-0000-0000-C000-000000000046}"
                )
                IEnumMoniker._iid_ = IID_IEnumMoniker

                IEnumMoniker._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'celt'),
                        (['out'], POINTER(POINTER(IMoniker)), 'rgelt'),
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
                        (['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumMoniker_INTERFACE_DEFINED__
        # interface __MIDL_itf_objidl_0000_0056
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IRunnableObject_INTERFACE_DEFINED__):
            # interface IRunnableObject
            # [uuid][object]
            # [unique]
            LPRUNNABLEOBJECT = POINTER(IRunnableObject)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRunnableObject = MIDL_INTERFACE(
                    "{00000126-0000-0000-C000-000000000046}"
                )
                IRunnableObject._iid_ = IID_IRunnableObject

                IRunnableObject._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetRunningClass')],
                        HRESULT,
                        'GetRunningClass',
                        (['out'], LPCLSID, 'lpClsid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Run')],
                        HRESULT,
                        'Run',
                        (['in'], LPBINDCTX, 'pbc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsRunning'), 'local'],
                        BOOL,
                        'IsRunning',
                    ),
                    COMMETHOD(
                        [helpstring('Method LockRunning')],
                        HRESULT,
                        'LockRunning',
                        (['in'], BOOL, 'fLock'),
                        (['in'], BOOL, 'fLastUnlockCloses'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetContainedObject')],
                        HRESULT,
                        'SetContainedObject',
                        (['in'], BOOL, 'fContained'),
                    ),
                ]

            # END IF  C style interface
            # [call_as]
        # END IF  __IRunnableObject_INTERFACE_DEFINED__

        if not defined(__IRunningObjectTable_INTERFACE_DEFINED__):
            # interface IRunningObjectTable
            # [uuid][object]
            # [unique]
            LPRUNNINGOBJECTTABLE = POINTER(IRunningObjectTable)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRunningObjectTable = MIDL_INTERFACE(
                    "{00000010-0000-0000-C000-000000000046}"
                )
                IRunningObjectTable._iid_ = IID_IRunningObjectTable

                IRunningObjectTable._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Register')],
                        HRESULT,
                        'Register',
                        (['in'], DWORD, 'grfFlags'),
                        (
                            ['unique', 'in'],
                            POINTER(comtypes.IUnknown),
                            'punkObject'
                        ),
                        (
                            ['unique', 'in'],
                            POINTER(IMoniker),
                            'pmkObjectName'
                        ),
                        (['out'], POINTER(DWORD), 'pdwRegister'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Revoke')],
                        HRESULT,
                        'Revoke',
                        (['in'], DWORD, 'dwRegister'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsRunning')],
                        HRESULT,
                        'IsRunning',
                        (
                            ['unique', 'in'],
                            POINTER(IMoniker),
                            'pmkObjectName'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetObject')],
                        HRESULT,
                        'GetObject',
                        (
                            ['unique', 'in'],
                            POINTER(IMoniker),
                            'pmkObjectName'
                        ),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'ppunkObject'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method NoteChangeTime')],
                        HRESULT,
                        'NoteChangeTime',
                        (['in'], DWORD, 'dwRegister'),
                        (['in'], POINTER(FILETIME), 'pfiletime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTimeOfLastChange')],
                        HRESULT,
                        'GetTimeOfLastChange',
                        (
                            ['in', 'unique'],
                            POINTER(IMoniker),
                            'pmkObjectName'
                        ),
                        (['out'], POINTER(FILETIME), 'pfiletime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumRunning')],
                        HRESULT,
                        'EnumRunning',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumMoniker)),
                            'ppenumMoniker'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRunningObjectTable_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0058
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IPersist_INTERFACE_DEFINED__):
            # interface IPersist
            # [uuid][object]
            # [unique]
            LPPERSIST = POINTER(IPersist)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersist = MIDL_INTERFACE(
                    "{0000010C-0000-0000-C000-000000000046}"
                )
                IPersist._iid_ = IID_IPersist

                IPersist._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetClassID')],
                        HRESULT,
                        'GetClassID',
                        (['out'], POINTER(CLSID), 'pClassID'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersist_INTERFACE_DEFINED__

        if not defined(__IPersistStream_INTERFACE_DEFINED__):
            # interface IPersistStream
            # [unique][uuid][object]
            # [unique]
            LPPERSISTSTREAM = POINTER(IPersistStream)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistStream = MIDL_INTERFACE(
                    "{00000109-0000-0000-C000-000000000046}"
                )
                IPersistStream._iid_ = IID_IPersistStream

                IPersistStream._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsDirty')],
                        HRESULT,
                        'IsDirty',
                    ),
                    COMMETHOD(
                        [helpstring('Method Load')],
                        HRESULT,
                        'Load',
                        (['unique', 'in'], POINTER(IStream), 'pStm'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Save')],
                        HRESULT,
                        'Save',
                        (['unique', 'in'], POINTER(IStream), 'pStm'),
                        (['in'], BOOL, 'fClearDirty'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSizeMax')],
                        HRESULT,
                        'GetSizeMax',
                        (['out'], POINTER(ULARGE_INTEGER), 'pcbSize'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistStream_INTERFACE_DEFINED__

        if not defined(__IMoniker_INTERFACE_DEFINED__):
            # interface IMoniker
            # [unique][uuid][object]
            # [unique]
            LPMONIKER = POINTER(IMoniker)


            class tagMKSYS(ENUM):
                MKSYS_NONE = 0
                MKSYS_GENERICCOMPOSITE = 1
                MKSYS_FILEMONIKER = 2
                MKSYS_ANTIMONIKER = 3
                MKSYS_ITEMMONIKER = 4
                MKSYS_POINTERMONIKER = 5
                MKSYS_CLASSMONIKER = 7
                MKSYS_OBJREFMONIKER = 8
                MKSYS_SESSIONMONIKER = 9
                MKSYS_LUAMONIKER = 10

            MKSYS = tagMKSYS


            class tagMKREDUCE(ENUM):
                MKRREDUCE_ONE = 3 << 16
                MKRREDUCE_TOUSER = 2 << 16
                MKRREDUCE_THROUGHUSER = 1 << 16
                MKRREDUCE_ALL = 0


            MKRREDUCE = tagMKREDUCE

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMoniker = MIDL_INTERFACE(
                    "{0000000F-0000-0000-C000-000000000046}"
                )
                IMoniker._iid_ = IID_IMoniker

                IMoniker._methods_ = [
                    COMMETHOD(
                        [helpstring('Method BindToObject'), 'local'],
                        HRESULT,
                        'BindToObject',
                        (['in'], POINTER(IBindCtx), 'pbc'),
                        (['in'], POINTER(IMoniker), 'pmkToLeft'),
                        (['in'], REFIID, 'riidResult'),
                        (['out'], POINTER(POINTER(VOID)), 'ppvResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BindToStorage'), 'local'],
                        HRESULT,
                        'BindToStorage',
                        (['in'], POINTER(IBindCtx), 'pbc'),
                        (['in'], POINTER(IMoniker), 'pmkToLeft'),
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppvObj'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Reduce')],
                        HRESULT,
                        'Reduce',
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        (['in'], DWORD, 'dwReduceHowFar'),
                        (
                            ['out', 'in', 'unique'],
                            POINTER(POINTER(IMoniker)),
                            'ppmkToLeft'
                        ),
                        (['out'], POINTER(POINTER(IMoniker)), 'ppmkReduced'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ComposeWith')],
                        HRESULT,
                        'ComposeWith',
                        (['unique', 'in'], POINTER(IMoniker), 'pmkRight'),
                        (['in'], BOOL, 'fOnlyIfNotGeneric'),
                        (
                            ['out'],
                            POINTER(POINTER(IMoniker)),
                            'ppmkComposite'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Enum')],
                        HRESULT,
                        'Enum',
                        (['in'], BOOL, 'fForward'),
                        (
                            ['out'],
                            POINTER(POINTER(IEnumMoniker)),
                            'ppenumMoniker'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsEqual')],
                        HRESULT,
                        'IsEqual',
                        (
                            ['unique', 'in'],
                            POINTER(IMoniker),
                            'pmkOtherMoniker'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Hash')],
                        HRESULT,
                        'Hash',
                        (['out'], POINTER(DWORD), 'pdwHash'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsRunning')],
                        HRESULT,
                        'IsRunning',
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        (['unique', 'in'], POINTER(IMoniker), 'pmkToLeft'),
                        (
                            ['unique', 'in'],
                            POINTER(IMoniker),
                            'pmkNewlyRunning'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTimeOfLastChange')],
                        HRESULT,
                        'GetTimeOfLastChange',
                        (['in', 'unique'], POINTER(IBindCtx), 'pbc'),
                        (['unique', 'in'], POINTER(IMoniker), 'pmkToLeft'),
                        (['out'], POINTER(FILETIME), 'pFileTime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Inverse')],
                        HRESULT,
                        'Inverse',
                        (['out'], POINTER(POINTER(IMoniker)), 'ppmk'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CommonPrefixWith')],
                        HRESULT,
                        'CommonPrefixWith',
                        (['unique', 'in'], POINTER(IMoniker), 'pmkOther'),
                        (['out'], POINTER(POINTER(IMoniker)), 'ppmkPrefix'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RelativePathTo')],
                        HRESULT,
                        'RelativePathTo',
                        (['unique', 'in'], POINTER(IMoniker), 'pmkOther'),
                        (['out'], POINTER(POINTER(IMoniker)), 'ppmkRelPath'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDisplayName')],
                        HRESULT,
                        'GetDisplayName',
                        (['in', 'unique'], POINTER(IBindCtx), 'pbc'),
                        (['unique', 'in'], POINTER(IMoniker), 'pmkToLeft'),
                        (['out'], POINTER(LPOLESTR), 'ppszDisplayName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ParseDisplayName')],
                        HRESULT,
                        'ParseDisplayName',
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        (['in', 'unique'], POINTER(IMoniker), 'pmkToLeft'),
                        (['in'], LPOLESTR, 'pszDisplayName'),
                        (['out'], POINTER(ULONG), 'pchEaten'),
                        (['out'], POINTER(POINTER(IMoniker)), 'ppmkOut'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsSystemMoniker')],
                        HRESULT,
                        'IsSystemMoniker',
                        (['out'], POINTER(DWORD), 'pdwMksys'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMoniker_INTERFACE_DEFINED__
        # interface __MIDL_itf_objidl_0000_0061
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IROTData_INTERFACE_DEFINED__):
            # interface IROTData
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IROTData = MIDL_INTERFACE(
                    "{F29F6BC0-5021-11CE-AA15-00006901293F}"
                )
                IROTData._iid_ = IID_IROTData

                IROTData._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetComparisonData')],
                        HRESULT,
                        'GetComparisonData',
                        (['out'], POINTER(BYTE), 'pbData'),
                        (['in'], ULONG, 'cbMax'),
                        (['out'], POINTER(ULONG), 'pcbData'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IROTData_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0062
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IEnumSTATSTG_INTERFACE_DEFINED__):
            # interface IEnumSTATSTG
            # [unique][uuid][object]
            # [unique]
            LPENUMSTATSTG = POINTER(IEnumSTATSTG)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumSTATSTG = MIDL_INTERFACE(
                    "{0000000D-0000-0000-C000-000000000046}"
                )
                IEnumSTATSTG._iid_ = IID_IEnumSTATSTG

                IEnumSTATSTG._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'celt'),
                        (['out'], POINTER(STATSTG), 'rgelt'),
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
                        (['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumSTATSTG_INTERFACE_DEFINED__

        if not defined(__IStorage_INTERFACE_DEFINED__):
            # interface IStorage
            # [unique][uuid][object]
            # [unique]
            LPSTORAGE = POINTER(IStorage)

            tagRemSNB._fields_ = [
                ('ulCntStr', ULONG),
                ('ulCntChar', ULONG),
                # [size_is]
                ('rgString', OLECHAR * 1),
            ]

            # [unique]
            wireSNB = POINTER(RemSNB)

            # [annotation][wire_marshal]
            SNB = POINTER(LPOLESTR)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IStorage = MIDL_INTERFACE(
                    "{0000000B-0000-0000-C000-000000000046}"
                )
                IStorage._iid_ = IID_IStorage

                IStorage._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateStream')],
                        HRESULT,
                        'CreateStream',
                        (['in'], POINTER(OLECHAR), 'pwcsName'),
                        (['in'], DWORD, 'grfMode'),
                        (['in'], DWORD, 'reserved1'),
                        (['in'], DWORD, 'reserved2'),
                        (['out'], POINTER(POINTER(IStream)), 'ppstm'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OpenStream'), 'local'],
                        HRESULT,
                        'OpenStream',
                        (['in'], POINTER(OLECHAR), 'pwcsName'),
                        (['in'], POINTER(VOID), 'reserved1'),
                        (['in'], DWORD, 'grfMode'),
                        (['in'], DWORD, 'reserved2'),
                        (['out'], POINTER(POINTER(IStream)), 'ppstm'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CreateStorage')],
                        HRESULT,
                        'CreateStorage',
                        (['in'], POINTER(OLECHAR), 'pwcsName'),
                        (['in'], DWORD, 'grfMode'),
                        (['in'], DWORD, 'reserved1'),
                        (['in'], DWORD, 'reserved2'),
                        (['out'], POINTER(POINTER(IStorage)), 'ppstg'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OpenStorage')],
                        HRESULT,
                        'OpenStorage',
                        (['unique', 'in'], POINTER(OLECHAR), 'pwcsName'),
                        (['unique', 'in'], POINTER(IStorage), 'pstgPriority'),
                        (['in'], DWORD, 'grfMode'),
                        (['unique', 'in'], SNB, 'snbExclude'),
                        (['in'], DWORD, 'reserved'),
                        (['out'], POINTER(POINTER(IStorage)), 'ppstg'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CopyTo'), 'local'],
                        HRESULT,
                        'CopyTo',
                        (['in'], DWORD, 'ciidExclude'),
                        (['in'], POINTER(IID), 'rgiidExclude'),
                        (['in'], SNB, 'snbExclude'),
                        (['in'], POINTER(IStorage), 'pstgDest'),
                    ),
                    COMMETHOD(
                        [helpstring('Method MoveElementTo')],
                        HRESULT,
                        'MoveElementTo',
                        (['in'], POINTER(OLECHAR), 'pwcsName'),
                        (['unique', 'in'], POINTER(IStorage), 'pstgDest'),
                        (['in'], POINTER(OLECHAR), 'pwcsNewName'),
                        (['in'], DWORD, 'grfFlags'),
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
                        [helpstring('Method EnumElements'), 'local'],
                        HRESULT,
                        'EnumElements',
                        (['in'], DWORD, 'reserved1'),
                        (['in'], POINTER(VOID), 'reserved2'),
                        (['in'], DWORD, 'reserved3'),
                        (['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DestroyElement')],
                        HRESULT,
                        'DestroyElement',
                        (['in'], POINTER(OLECHAR), 'pwcsName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RenameElement')],
                        HRESULT,
                        'RenameElement',
                        (['in'], POINTER(OLECHAR), 'pwcsOldName'),
                        (['in'], POINTER(OLECHAR), 'pwcsNewName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetElementTimes')],
                        HRESULT,
                        'SetElementTimes',
                        (['unique', 'in'], POINTER(OLECHAR), 'pwcsName'),
                        (['unique', 'in'], POINTER(FILETIME), 'pctime'),
                        (['unique', 'in'], POINTER(FILETIME), 'patime'),
                        (['unique', 'in'], POINTER(FILETIME), 'pmtime'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetClass')],
                        HRESULT,
                        'SetClass',
                        (['in'], REFCLSID, 'clsid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetStateBits')],
                        HRESULT,
                        'SetStateBits',
                        (['in'], DWORD, 'grfStateBits'),
                        (['in'], DWORD, 'grfMask'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Stat')],
                        HRESULT,
                        'Stat',
                        (['out'], POINTER(STATSTG), 'pstatstg'),
                        (['in'], DWORD, 'grfStatFlag'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IStorage_INTERFACE_DEFINED__
        # interface __MIDL_itf_objidl_0000_0064
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IPersistFile_INTERFACE_DEFINED__):
            # interface IPersistFile
            # [unique][uuid][object]
            # [unique]
            LPPERSISTFILE = POINTER(IPersistFile)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistFile = MIDL_INTERFACE(
                    "{0000010B-0000-0000-C000-000000000046}"
                )
                IPersistFile._iid_ = IID_IPersistFile

                IPersistFile._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsDirty')],
                        HRESULT,
                        'IsDirty',
                    ),
                    COMMETHOD(
                        [helpstring('Method Load')],
                        HRESULT,
                        'Load',
                        (['in'], LPCOLESTR, 'pszFileName'),
                        (['in'], DWORD, 'dwMode'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Save')],
                        HRESULT,
                        'Save',
                        (['unique', 'in'], LPCOLESTR, 'pszFileName'),
                        (['in'], BOOL, 'fRemember'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SaveCompleted')],
                        HRESULT,
                        'SaveCompleted',
                        (['unique', 'in'], LPCOLESTR, 'pszFileName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCurFile')],
                        HRESULT,
                        'GetCurFile',
                        (['out'], POINTER(LPOLESTR), 'ppszFileName'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistFile_INTERFACE_DEFINED__

        if not defined(__IPersistStorage_INTERFACE_DEFINED__):
            # interface IPersistStorage
            # [unique][uuid][object]
            # [unique]
            LPPERSISTSTORAGE = POINTER(IPersistStorage)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistStorage = MIDL_INTERFACE(
                    "{0000010A-0000-0000-C000-000000000046}"
                )
                IPersistStorage._iid_ = IID_IPersistStorage

                IPersistStorage._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsDirty')],
                        HRESULT,
                        'IsDirty',
                    ),
                    COMMETHOD(
                        [helpstring('Method InitNew')],
                        HRESULT,
                        'InitNew',
                        (['unique', 'in'], POINTER(IStorage), 'pStg'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Load')],
                        HRESULT,
                        'Load',
                        (['unique', 'in'], POINTER(IStorage), 'pStg'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Save')],
                        HRESULT,
                        'Save',
                        (['unique', 'in'], POINTER(IStorage), 'pStgSave'),
                        (['in'], BOOL, 'fSameAsLoad'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SaveCompleted')],
                        HRESULT,
                        'SaveCompleted',
                        (['unique', 'in'], POINTER(IStorage), 'pStgNew'),
                    ),
                    COMMETHOD(
                        [helpstring('Method HandsOffStorage')],
                        HRESULT,
                        'HandsOffStorage',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistStorage_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0066
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__ILockBytes_INTERFACE_DEFINED__):
            # interface ILockBytes
            # [unique][uuid][object]
            # [unique]
            LPLOCKBYTES = POINTER(ILockBytes)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ILockBytes = MIDL_INTERFACE(
                    "{0000000A-0000-0000-C000-000000000046}"
                )
                ILockBytes._iid_ = IID_ILockBytes

                ILockBytes._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ReadAt'), 'local'],
                        HRESULT,
                        'ReadAt',
                        (['in'], ULARGE_INTEGER, 'ulOffset'),
                        (['out'], POINTER(VOID), 'pv'),
                        (['in'], ULONG, 'cb'),
                        (['out'], POINTER(ULONG), 'pcbRead'),
                    ),
                    COMMETHOD(
                        [helpstring('Method WriteAt'), 'local'],
                        HRESULT,
                        'WriteAt',
                        (['in'], ULARGE_INTEGER, 'ulOffset'),
                        (['in'], POINTER(VOID), 'pv'),
                        (['in'], ULONG, 'cb'),
                        (['out'], POINTER(ULONG), 'pcbWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Flush')],
                        HRESULT,
                        'Flush',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetSize')],
                        HRESULT,
                        'SetSize',
                        (['in'], ULARGE_INTEGER, 'cb'),
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
                ]

            # END IF  C style interface
        # END IF  __ILockBytes_INTERFACE_DEFINED__

        if not defined(__IEnumFORMATETC_INTERFACE_DEFINED__):
            # interface IEnumFORMATETC
            # [unique][uuid][object]
            # [unique]
            LPENUMFORMATETC = POINTER(IEnumFORMATETC)

            tagDVTARGETDEVICE._fields_ = [
                ('tdSize', DWORD),
                ('tdDriverNameOffset', WORD),
                ('tdDeviceNameOffset', WORD),
                ('tdPortNameOffset', WORD),
                ('tdExtDevmodeOffset', WORD),
                # [size_is]
                ('tdData', BYTE * 1),
            ]
            LPCLIPFORMAT = POINTER(CLIPFORMAT)

            tagFORMATETC._fields_ = [
                ('cfFormat', CLIPFORMAT),
                # [unique]
                ('ptd', POINTER(DVTARGETDEVICE)),
                ('dwAspect', DWORD),
                ('lindex', LONG),
                ('tymed', DWORD),
            ]
            LPFORMATETC = POINTER(tagFORMATETC)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumFORMATETC = MIDL_INTERFACE(
                    "{00000103-0000-0000-C000-000000000046}"
                )
                IEnumFORMATETC._iid_ = IID_IEnumFORMATETC

                IEnumFORMATETC._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'celt'),
                        (['out'], POINTER(FORMATETC), 'rgelt'),
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
                        (['out'], POINTER(POINTER(IEnumFORMATETC)), 'ppenum'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumFORMATETC_INTERFACE_DEFINED__

        if not defined(__IEnumSTATDATA_INTERFACE_DEFINED__):
            # interface IEnumSTATDATA
            # [unique][uuid][object]
            # [unique]
            LPENUMSTATDATA = POINTER(IEnumSTATDATA)


            class tagADVF(ENUM):
                ADVF_NODATA = 1
                ADVF_PRIMEFIRST = 2
                ADVF_ONLYONCE = 4
                ADVF_DATAONSTOP = 64
                ADVFCACHE_NOHANDLER = 8
                ADVFCACHE_FORCEBUILTIN = 16
                ADVFCACHE_ONSAVE = 32

            ADVF = tagADVF

            tagSTATDATA._fields_ = [
                ('formatetc', FORMATETC),
                ('advf', DWORD),
                # [unique]
                ('pAdvSink', POINTER(IAdviseSink)),
                ('dwConnection', DWORD),
            ]

            LPSTATDATA = POINTER(STATDATA)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumSTATDATA = MIDL_INTERFACE(
                    "{00000105-0000-0000-C000-000000000046}"
                )
                IEnumSTATDATA._iid_ = IID_IEnumSTATDATA

                IEnumSTATDATA._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'celt'),
                        (['out'], POINTER(STATDATA), 'rgelt'),
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
                        (['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenum'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumSTATDATA_INTERFACE_DEFINED__

        if not defined(__IRootStorage_INTERFACE_DEFINED__):
            # interface IRootStorage
            # [unique][uuid][object]
            # [unique]
            LPROOTSTORAGE = POINTER(IRootStorage)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRootStorage = MIDL_INTERFACE(
                    "{00000012-0000-0000-C000-000000000046}"
                )
                IRootStorage._iid_ = IID_IRootStorage

                IRootStorage._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SwitchToFile')],
                        HRESULT,
                        'SwitchToFile',
                        (['in'], LPOLESTR, 'pszFile'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRootStorage_INTERFACE_DEFINED__

        if not defined(__IAdviseSink_INTERFACE_DEFINED__):
            # interface IAdviseSink
            # [unique][async_uuid][uuid][object]
            LPADVISESINK = POINTER(IAdviseSink)


            class tagTYMED(ENUM):
                TYMED_HGLOBAL = 1
                TYMED_FILE = 2
                TYMED_ISTREAM = 4
                TYMED_ISTORAGE = 8
                TYMED_GDI = 16
                TYMED_MFPICT = 32
                TYMED_ENHMF = 64
                TYMED_NULL = 0

            TYMED = tagTYMED

            if not defined(RC_INVOKED):
                if _MSC_VER >= 1200:
                    pass
                # END IF
            # END IF

            tagRemSTGMEDIUM._fields_ = [
                ('tymed', DWORD),
                ('dwHandleType', DWORD),
                ('pData', ULONG),
                ('pUnkForRelease', ULONG),
                ('cbData', ULONG),
                # [size_is]
                ('data', BYTE * 1),
            ]

            if not defined(RC_INVOKED):
                if _MSC_VER >= 1200:
                    pass
                else:
                    pass
                # END IF
            # END IF

            if defined(NONAMELESSUNION):
                class u(ctypes.Union):
                    pass


                u._fields_ = [
                    ('hBitmap', HBITMAP),
                    ('hMetaFilePict', HMETAFILEPICT),
                    ('hEnhMetaFile', HENHMETAFILE),
                    ('hGlobal', HGLOBAL),
                    ('lpszFileName', LPOLESTR),
                    ('pstm', POINTER(IStream)),
                    ('pstg', POINTER(IStorage)),
                ]
                tagSTGMEDIUM.u = u

                tagSTGMEDIUM._fields_ = [
                    ('tymed', DWORD),
                    ('u', tagSTGMEDIUM.u),
                    ('pUnkForRelease', POINTER(comtypes.IUnknown)),
                ]
            else:
                class DUMMYUNIONNAME(ctypes.Union):
                    pass

                DUMMYUNIONNAME._fields_ = [
                    # [case()]
                    ('hBitmap', HBITMAP),
                    # [case()]
                    ('hMetaFilePict', HMETAFILEPICT),
                    # [case()]
                    ('hEnhMetaFile', HENHMETAFILE),
                    # [case()]
                    ('hGlobal', HGLOBAL),
                    # [case()]
                    ('lpszFileName', LPOLESTR),
                    # [case()]
                    ('pstm', POINTER(IStream)),
                    # [case()]
                    ('pstg', POINTER(IStorage)),
                ]
                tagSTGMEDIUM.DUMMYUNIONNAME = DUMMYUNIONNAME


                tagSTGMEDIUM._fields_ = [
                    ('tymed', DWORD),
                    # [switch_is][switch_type]
                    ('DUMMYUNIONNAME', tagSTGMEDIUM.DUMMYUNIONNAME),
                    # [unique]
                    ('pUnkForRelease', POINTER(comtypes.IUnknown)),
                ]
            # END IF  not NONAMELESSUNION


            class __MIDL_IAdviseSink_0002(ctypes.Union):
                pass

            __MIDL_IAdviseSink_0002._fields_ = [
                # [case()]
                ('hBitmap', wireHBITMAP),
                # [case()]
                ('hPalette', wireHPALETTE),
                # [default]
                ('hGeneric', wireHGLOBAL),
            ]
            u = __MIDL_IAdviseSink_0002
            _GDI_OBJECT.u = u

            _GDI_OBJECT._fields_ = [
                ('ObjectType', DWORD),
                # [switch_is]
                ('u', _GDI_OBJECT.u),
            ]

            class _STGMEDIUM_UNION(ctypes.Structure):
                pass


            class __MIDL_IAdviseSink_0003(ctypes.Union):
                pass

            __MIDL_IAdviseSink_0003._fields_ = [
                # [case()]
                ('hHEnhMetaFile', wireHENHMETAFILE),
                # [case()]
                ('hGdiHandle', POINTER(GDI_OBJECT)),
                # [case()]
                ('hGlobal', wireHGLOBAL),
                # [case()]
                ('lpszFileName', LPOLESTR),
                # [case()]
                ('pstm', POINTER(BYTE_BLOB)),
                # [case()]
                ('pstg', POINTER(BYTE_BLOB)),
            ]
            u = __MIDL_IAdviseSink_0003
            _STGMEDIUM_UNION.u = u

            _STGMEDIUM_UNION._fields_ = [
                ('tymed', DWORD),
                # [switch_is]
                ('u', _STGMEDIUM_UNION.u),
            ]

            DUMMYUNIONNAME = _STGMEDIUM_UNION
            _userSTGMEDIUM.DUMMYUNIONNAME = DUMMYUNIONNAME

            _userSTGMEDIUM._fields_ = [
                ('DUMMYUNIONNAME', _userSTGMEDIUM.DUMMYUNIONNAME),
                ('pUnkForRelease', POINTER(comtypes.IUnknown)),
            ]

            # [unique]
            wireSTGMEDIUM = POINTER(userSTGMEDIUM)

            # [wire_marshal]
            STGMEDIUM = uSTGMEDIUM

            # [unique]
            wireASYNC_STGMEDIUM = POINTER(userSTGMEDIUM)

            # [wire_marshal]
            ASYNC_STGMEDIUM = STGMEDIUM
            LPSTGMEDIUM = POINTER(STGMEDIUM)

            _userFLAG_STGMEDIUM._fields_ = [
                ('ContextFlags', LONG),
                ('fPassOwnership', LONG),
                ('Stgmed', userSTGMEDIUM),
            ]

            # [unique]
            wireFLAG_STGMEDIUM = POINTER(userFLAG_STGMEDIUM)

            _FLAG_STGMEDIUM._fields_ = [
                ('ContextFlags', LONG),
                ('fPassOwnership', LONG),
                ('Stgmed', STGMEDIUM),
            ]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IAdviseSink = MIDL_INTERFACE(
                    "{0000010F-0000-0000-C000-000000000046}"
                )
                IAdviseSink._iid_ = IID_IAdviseSink

                IAdviseSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnDataChange'), 'local'],
                        VOID,
                        'OnDataChange',
                        (['in'], POINTER(FORMATETC), 'pFormatetc'),
                        (['in'], POINTER(STGMEDIUM), 'pStgmed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnViewChange'), 'local'],
                        VOID,
                        'OnViewChange',
                        (['in'], DWORD, 'dwAspect'),
                        (['in'], LONG, 'lindex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnRename'), 'local'],
                        VOID,
                        'OnRename',
                        (['in'], POINTER(IMoniker), 'pmk'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnSave'), 'local'],
                        VOID,
                        'OnSave',
                    ),
                    COMMETHOD(
                        [helpstring('Method OnClose'), 'local'],
                        VOID,
                        'OnClose',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IAdviseSink_INTERFACE_DEFINED__

        if not defined(__AsyncIAdviseSink_INTERFACE_DEFINED__):
            # interface AsyncIAdviseSink
            # [uuid][unique][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_AsyncIAdviseSink = MIDL_INTERFACE(
                    "{00000150-0000-0000-C000-000000000046}"
                )
                AsyncIAdviseSink._iid_ = IID_AsyncIAdviseSink

                AsyncIAdviseSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Begin_OnDataChange'), 'local'],
                        VOID,
                        'Begin_OnDataChange',
                        (['in'], POINTER(FORMATETC), 'pFormatetc'),
                        (['in'], POINTER(STGMEDIUM), 'pStgmed'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_OnDataChange'), 'local'],
                        VOID,
                        'Finish_OnDataChange',
                    ),
                    COMMETHOD(
                        [helpstring('Method Begin_OnViewChange'), 'local'],
                        VOID,
                        'Begin_OnViewChange',
                        (['in'], DWORD, 'dwAspect'),
                        (['in'], LONG, 'lindex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_OnViewChange'), 'local'],
                        VOID,
                        'Finish_OnViewChange',
                    ),
                    COMMETHOD(
                        [helpstring('Method Begin_OnRename'), 'local'],
                        VOID,
                        'Begin_OnRename',
                        (['in'], POINTER(IMoniker), 'pmk'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_OnRename'), 'local'],
                        VOID,
                        'Finish_OnRename',
                    ),
                    COMMETHOD(
                        [helpstring('Method Begin_OnSave'), 'local'],
                        VOID,
                        'Begin_OnSave',
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_OnSave'), 'local'],
                        VOID,
                        'Finish_OnSave',
                    ),
                    COMMETHOD(
                        [helpstring('Method Begin_OnClose'), 'local'],
                        VOID,
                        'Begin_OnClose',
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_OnClose'), 'local'],
                        VOID,
                        'Finish_OnClose',
                    ),
                ]

            # END IF  C style interface
        # END IF  __AsyncIAdviseSink_INTERFACE_DEFINED__
        # interface __MIDL_itf_objidl_0000_0071
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IAdviseSink2_INTERFACE_DEFINED__):
            # interface IAdviseSink2
            # [unique][async_uuid][uuid][object]
            # [unique]
            LPADVISESINK2 = POINTER(IAdviseSink2)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IAdviseSink2 = MIDL_INTERFACE(
                    "{00000125-0000-0000-C000-000000000046}"
                )
                IAdviseSink2._iid_ = IID_IAdviseSink2

                IAdviseSink2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnLinkSrcChange'), 'local'],
                        VOID,
                        'OnLinkSrcChange',
                        (['in'], POINTER(IMoniker), 'pmk'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IAdviseSink2_INTERFACE_DEFINED__

        if not defined(__AsyncIAdviseSink2_INTERFACE_DEFINED__):
            # interface AsyncIAdviseSink2
            # [uuid][unique][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_AsyncIAdviseSink2 = MIDL_INTERFACE(
                    "{00000151-0000-0000-C000-000000000046}"
                )
                AsyncIAdviseSink2._iid_ = IID_AsyncIAdviseSink2

                AsyncIAdviseSink2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Begin_OnLinkSrcChange'), 'local'],
                        VOID,
                        'Begin_OnLinkSrcChange',
                        (['in'], POINTER(IMoniker), 'pmk'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Finish_OnLinkSrcChange'), 'local'],
                        VOID,
                        'Finish_OnLinkSrcChange',
                    ),
                ]

            # END IF  C style interface
        # END IF  __AsyncIAdviseSink2_INTERFACE_DEFINED__
        # interface __MIDL_itf_objidl_0000_0072
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IDataObject_INTERFACE_DEFINED__):
            # interface IDataObject
            # [unique][uuid][object]
            # [unique]
            LPDATAOBJECT = POINTER(IDataObject)


            class tagDATADIR(ENUM):
                DATADIR_GET = 1
                DATADIR_SET = 2

            DATADIR = tagDATADIR
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDataObject = MIDL_INTERFACE(
                    "{0000010E-0000-0000-C000-000000000046}"
                )
                IDataObject._iid_ = IID_IDataObject

                IDataObject._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetData'), 'local'],
                        HRESULT,
                        'GetData',
                        (['in'], POINTER(FORMATETC), 'pformatetcIn'),
                        (['out'], POINTER(STGMEDIUM), 'pmedium'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDataHere'), 'local'],
                        HRESULT,
                        'GetDataHere',
                        (['in'], POINTER(FORMATETC), 'pformatetc'),
                        (['out', 'in'], POINTER(STGMEDIUM), 'pmedium'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueryGetData')],
                        HRESULT,
                        'QueryGetData',
                        (['unique', 'in'], POINTER(FORMATETC), 'pformatetc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCanonicalFormatEtc')],
                        HRESULT,
                        'GetCanonicalFormatEtc',
                        (
                            ['unique', 'in'],
                            POINTER(FORMATETC),
                            'pformatectIn'
                        ),
                        (['out'], POINTER(FORMATETC), 'pformatetcOut'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetData'), 'local'],
                        HRESULT,
                        'SetData',
                        (['in'], POINTER(FORMATETC), 'pformatetc'),
                        (['in'], POINTER(STGMEDIUM), 'pmedium'),
                        (['in'], BOOL, 'fRelease'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumFormatEtc')],
                        HRESULT,
                        'EnumFormatEtc',
                        (['in'], DWORD, 'dwDirection'),
                        (
                            ['out'],
                            POINTER(POINTER(IEnumFORMATETC)),
                            'ppenumFormatEtc'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method DAdvise')],
                        HRESULT,
                        'DAdvise',
                        (['in'], POINTER(FORMATETC), 'pformatetc'),
                        (['in'], DWORD, 'advf'),
                        (['unique', 'in'], POINTER(IAdviseSink), 'pAdvSink'),
                        (['out'], POINTER(DWORD), 'pdwConnection'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DUnadvise')],
                        HRESULT,
                        'DUnadvise',
                        (['in'], DWORD, 'dwConnection'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumDAdvise')],
                        HRESULT,
                        'EnumDAdvise',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumSTATDATA)),
                            'ppenumAdvise'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDataObject_INTERFACE_DEFINED__
        # interface __MIDL_itf_objidl_0000_0073
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IDataAdviseHolder_INTERFACE_DEFINED__):
            # interface IDataAdviseHolder
            # [uuid][object][local]
            # [unique]
            LPDATAADVISEHOLDER = POINTER(IDataAdviseHolder)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDataAdviseHolder = MIDL_INTERFACE(
                    "{00000110-0000-0000-C000-000000000046}"
                )
                IDataAdviseHolder._iid_ = IID_IDataAdviseHolder

                IDataAdviseHolder._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Advise')],
                        HRESULT,
                        'Advise',
                        (['in'], POINTER(IDataObject), 'pDataObject'),
                        (['in'], POINTER(FORMATETC), 'pFetc'),
                        (['in'], DWORD, 'advf'),
                        (['in'], POINTER(IAdviseSink), 'pAdvise'),
                        (['out'], POINTER(DWORD), 'pdwConnection'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Unadvise')],
                        HRESULT,
                        'Unadvise',
                        (['in'], DWORD, 'dwConnection'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumAdvise')],
                        HRESULT,
                        'EnumAdvise',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumSTATDATA)),
                            'ppenumAdvise'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SendOnDataChange')],
                        HRESULT,
                        'SendOnDataChange',
                        (['in'], POINTER(IDataObject), 'pDataObject'),
                        (['in'], DWORD, 'dwReserved'),
                        (['in'], DWORD, 'advf'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDataAdviseHolder_INTERFACE_DEFINED__

        if not defined(__IMessageFilter_INTERFACE_DEFINED__):
            # interface IMessageFilter
            # [uuid][object][local]
            # [unique]
            LPMESSAGEFILTER = POINTER(IMessageFilter)


            class tagCALLTYPE(ENUM):
                CALLTYPE_TOPLEVEL = 1
                CALLTYPE_NESTED = 2
                CALLTYPE_ASYNC = 3
                CALLTYPE_TOPLEVEL_CALLPENDING = 4
                CALLTYPE_ASYNC_CALLPENDING = 5

            CALLTYPE = tagCALLTYPE


            class tagSERVERCALL(ENUM):
                SERVERCALL_ISHANDLED = 0
                SERVERCALL_REJECTED = 1
                SERVERCALL_RETRYLATER = 2

            SERVERCALL = tagSERVERCALL


            class tagPENDINGTYPE(ENUM):
                PENDINGTYPE_TOPLEVEL = 1
                PENDINGTYPE_NESTED = 2

            PENDINGTYPE = tagPENDINGTYPE


            class tagPENDINGMSG(ENUM):
                PENDINGMSG_CANCELCALL = 0
                PENDINGMSG_WAITNOPROCESS = 1
                PENDINGMSG_WAITDEFPROCESS = 2

            PENDINGMSG = tagPENDINGMSG

            tagINTERFACEINFO._fields_ = [
                ('pUnk', POINTER(comtypes.IUnknown)),
                ('iid', IID),
                ('wMethod', WORD),
            ]
            LPINTERFACEINFO = POINTER(tagINTERFACEINFO)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMessageFilter = MIDL_INTERFACE(
                    "{00000016-0000-0000-C000-000000000046}"
                )
                IMessageFilter._iid_ = IID_IMessageFilter

                IMessageFilter._methods_ = [
                    COMMETHOD(
                        [helpstring('Method HandleInComingCall')],
                        DWORD,
                        'HandleInComingCall',
                        (['in'], DWORD, 'dwCallType'),
                        (['in'], HTASK, 'htaskCaller'),
                        (['in'], DWORD, 'dwTickCount'),
                        (['in'], LPINTERFACEINFO, 'lpInterfaceInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RetryRejectedCall')],
                        DWORD,
                        'RetryRejectedCall',
                        (['in'], HTASK, 'htaskCallee'),
                        (['in'], DWORD, 'dwTickCount'),
                        (['in'], DWORD, 'dwRejectType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method MessagePending')],
                        DWORD,
                        'MessagePending',
                        (['in'], HTASK, 'htaskCallee'),
                        (['in'], DWORD, 'dwTickCount'),
                        (['in'], DWORD, 'dwPendingType'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMessageFilter_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0075
        # [local]
        # Well-known Property Set Format IDs
        if not defined(__IClassActivator_INTERFACE_DEFINED__):
            # interface IClassActivator
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IClassActivator = MIDL_INTERFACE(
                    "{00000140-0000-0000-C000-000000000046}"
                )
                IClassActivator._iid_ = IID_IClassActivator

                IClassActivator._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetClassObject')],
                        HRESULT,
                        'GetClassObject',
                        (['in'], REFCLSID, 'rclsid'),
                        (['in'], DWORD, 'dwClassContext'),
                        (['in'], LCID, 'locale'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IClassActivator_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0076
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IFillLockBytes_INTERFACE_DEFINED__):
            # interface IFillLockBytes
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IFillLockBytes = MIDL_INTERFACE(
                    "{99CAF010-415E-11CF-8814-00AA00B569F5}"
                )
                IFillLockBytes._iid_ = IID_IFillLockBytes

                IFillLockBytes._methods_ = [
                    COMMETHOD(
                        [helpstring('Method FillAppend'), 'local'],
                        HRESULT,
                        'FillAppend',
                        (['in'], POINTER(VOID), 'pv'),
                        (['in'], ULONG, 'cb'),
                        (['out'], POINTER(ULONG), 'pcbWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FillAt'), 'local'],
                        HRESULT,
                        'FillAt',
                        (['in'], ULARGE_INTEGER, 'ulOffset'),
                        (['in'], POINTER(VOID), 'pv'),
                        (['in'], ULONG, 'cb'),
                        (['out'], POINTER(ULONG), 'pcbWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFillSize')],
                        HRESULT,
                        'SetFillSize',
                        (['in'], ULARGE_INTEGER, 'ulSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Terminate')],
                        HRESULT,
                        'Terminate',
                        (['in'], BOOL, 'bCanceled'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IFillLockBytes_INTERFACE_DEFINED__
        # interface __MIDL_itf_objidl_0000_0077
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IProgressNotify_INTERFACE_DEFINED__):
            # interface IProgressNotify
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IProgressNotify = MIDL_INTERFACE(
                    "{A9D758A0-4617-11CF-95FC-00AA00680DB4}"
                )
                IProgressNotify._iid_ = IID_IProgressNotify

                IProgressNotify._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnProgress')],
                        HRESULT,
                        'OnProgress',
                        (['in'], DWORD, 'dwProgressCurrent'),
                        (['in'], DWORD, 'dwProgressMaximum'),
                        (['in'], BOOL, 'fAccurate'),
                        (['in'], BOOL, 'fOwner'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IProgressNotify_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0078
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__ILayoutStorage_INTERFACE_DEFINED__):
            # interface ILayoutStorage
            # [unique][uuid][object][local]
            tagStorageLayout._fields_ = [
                ('LayoutType', DWORD),
                ('pwcsElementName', POINTER(OLECHAR)),
                ('cOffset', LARGE_INTEGER),
                ('cBytes', LARGE_INTEGER),
            ]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ILayoutStorage = MIDL_INTERFACE(
                    "{0E6D4D90-6738-11CF-9608-00AA00680DB4}"
                )
                ILayoutStorage._iid_ = IID_ILayoutStorage

                ILayoutStorage._methods_ = [
                    COMMETHOD(
                        [helpstring('Method LayoutScript')],
                        HRESULT,
                        'LayoutScript',
                        (['in'], POINTER(StorageLayout), 'pStorageLayout'),
                        (['in'], DWORD, 'nEntries'),
                        (['in'], DWORD, 'glfInterleavedFlag'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BeginMonitor')],
                        HRESULT,
                        'BeginMonitor',
                    ),
                    COMMETHOD(
                        [helpstring('Method EndMonitor')],
                        HRESULT,
                        'EndMonitor',
                    ),
                    COMMETHOD(
                        [helpstring('Method ReLayoutDocfile')],
                        HRESULT,
                        'ReLayoutDocfile',
                        (['in'], POINTER(OLECHAR), 'pwcsNewDfName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReLayoutDocfileOnILockBytes')],
                        HRESULT,
                        'ReLayoutDocfileOnILockBytes',
                        (['in'], POINTER(ILockBytes), 'pILockBytes'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ILayoutStorage_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0079
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IBlockingLock_INTERFACE_DEFINED__):
            # interface IBlockingLock
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IBlockingLock = MIDL_INTERFACE(
                    "{30F3D47A-6447-11D1-8E3C-00C04FB9386D}"
                )
                IBlockingLock._iid_ = IID_IBlockingLock

                IBlockingLock._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Lock')],
                        HRESULT,
                        'Lock',
                        (['in'], DWORD, 'dwTimeout'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Unlock')],
                        HRESULT,
                        'Unlock',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IBlockingLock_INTERFACE_DEFINED__

        if not defined(__ITimeAndNoticeControl_INTERFACE_DEFINED__):
            # interface ITimeAndNoticeControl
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITimeAndNoticeControl = MIDL_INTERFACE(
                    "{BC0BF6AE-8878-11D1-83E9-00C04FC2C6D4}"
                )
                ITimeAndNoticeControl._iid_ = IID_ITimeAndNoticeControl

                ITimeAndNoticeControl._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SuppressChanges')],
                        HRESULT,
                        'SuppressChanges',
                        (['in'], DWORD, 'res1'),
                        (['in'], DWORD, 'res2'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITimeAndNoticeControl_INTERFACE_DEFINED__

        if not defined(__IOplockStorage_INTERFACE_DEFINED__):
            # interface IOplockStorage
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOplockStorage = MIDL_INTERFACE(
                    "{8D19C834-8879-11D1-83E9-00C04FC2C6D4}"
                )
                IOplockStorage._iid_ = IID_IOplockStorage

                IOplockStorage._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateStorageEx')],
                        HRESULT,
                        'CreateStorageEx',
                        (['in'], LPCWSTR, 'pwcsName'),
                        (['in'], DWORD, 'grfMode'),
                        (['in'], DWORD, 'stgfmt'),
                        (['in'], DWORD, 'grfAttrs'),
                        (['in'], REFIID, 'riid'),
                        (
                            ['out', 'iid_is'],
                            POINTER(POINTER(VOID)),
                            'ppstgOpen'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method OpenStorageEx')],
                        HRESULT,
                        'OpenStorageEx',
                        (['in'], LPCWSTR, 'pwcsName'),
                        (['in'], DWORD, 'grfMode'),
                        (['in'], DWORD, 'stgfmt'),
                        (['in'], DWORD, 'grfAttrs'),
                        (['in'], REFIID, 'riid'),
                        (
                            ['out', 'iid_is'],
                            POINTER(POINTER(VOID)),
                            'ppstgOpen'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOplockStorage_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0082
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IDirectWriterLock_INTERFACE_DEFINED__):
            # interface IDirectWriterLock
            # [unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDirectWriterLock = MIDL_INTERFACE(
                    "{0E6D4D92-6738-11CF-9608-00AA00680DB4}"
                )
                IDirectWriterLock._iid_ = IID_IDirectWriterLock

                IDirectWriterLock._methods_ = [
                    COMMETHOD(
                        [helpstring('Method WaitForWriteAccess')],
                        HRESULT,
                        'WaitForWriteAccess',
                        (['in'], DWORD, 'dwTimeout'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseWriteAccess')],
                        HRESULT,
                        'ReleaseWriteAccess',
                    ),
                    COMMETHOD(
                        [helpstring('Method HaveWriteAccess')],
                        HRESULT,
                        'HaveWriteAccess',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDirectWriterLock_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0083
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IUrlMon_INTERFACE_DEFINED__):
            # interface IUrlMon
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IUrlMon = MIDL_INTERFACE(
                    "{00000026-0000-0000-C000-000000000046}"
                )
                IUrlMon._iid_ = IID_IUrlMon

                IUrlMon._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AsyncGetClassBits')],
                        HRESULT,
                        'AsyncGetClassBits',
                        (['in'], REFCLSID, 'rclsid'),
                        (['unique', 'in'], LPCWSTR, 'pszTYPE'),
                        (['unique', 'in'], LPCWSTR, 'pszExt'),
                        (['in'], DWORD, 'dwFileVersionMS'),
                        (['in'], DWORD, 'dwFileVersionLS'),
                        (['unique', 'in'], LPCWSTR, 'pszCodeBase'),
                        (['in'], POINTER(IBindCtx), 'pbc'),
                        (['in'], DWORD, 'dwClassContext'),
                        (['in'], REFIID, 'riid'),
                        (['in'], DWORD, 'flags'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IUrlMon_INTERFACE_DEFINED__

        if not defined(__IForegroundTransfer_INTERFACE_DEFINED__):
            # interface IForegroundTransfer
            # [uuid][object][local]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IForegroundTransfer = MIDL_INTERFACE(
                    "{00000145-0000-0000-C000-000000000046}"
                )
                IForegroundTransfer._iid_ = IID_IForegroundTransfer

                IForegroundTransfer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AllowForegroundTransfer')],
                        HRESULT,
                        'AllowForegroundTransfer',
                        (['in'], POINTER(VOID), 'lpvReserved'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IForegroundTransfer_INTERFACE_DEFINED__

        if not defined(__IThumbnailExtractor_INTERFACE_DEFINED__):
            # interface IThumbnailExtractor
            # [object][uuid]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IThumbnailExtractor = MIDL_INTERFACE(
                    "{969DC708-5C76-11D1-8D86-0000F804B057}"
                )
                IThumbnailExtractor._iid_ = IID_IThumbnailExtractor

                IThumbnailExtractor._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ExtractThumbnail')],
                        HRESULT,
                        'ExtractThumbnail',
                        (['in'], POINTER(IStorage), 'pStg'),
                        (['in'], ULONG, 'ulLength'),
                        (['in'], ULONG, 'ulHeight'),
                        (['out'], POINTER(ULONG), 'pulOutputLength'),
                        (['out'], POINTER(ULONG), 'pulOutputHeight'),
                        (['out'], POINTER(HBITMAP), 'phOutputBitmap'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnFileUpdated')],
                        HRESULT,
                        'OnFileUpdated',
                        (['in'], POINTER(IStorage), 'pStg'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IThumbnailExtractor_INTERFACE_DEFINED__

        if not defined(__IDummyHICONIncluder_INTERFACE_DEFINED__):
            # interface IDummyHICONIncluder
            # [uuid][unique][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDummyHICONIncluder = MIDL_INTERFACE(
                    "{947990DE-CC28-11D2-A0F7-00805F858FB1}"
                )
                IDummyHICONIncluder._iid_ = IID_IDummyHICONIncluder

                IDummyHICONIncluder._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Dummy')],
                        HRESULT,
                        'Dummy',
                        (['in'], HICON, 'h1'),
                        (['in'], HDC, 'h2'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDummyHICONIncluder_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0087
        # [local]
        class tagApplicationType(ENUM):
            ServerApplication = 0
            LibraryApplication = ServerApplication + 1
        ApplicationType = tagApplicationType


        class tagShutdownType(ENUM):
            IdleShutdown = 0
            ForcedShutdown = IdleShutdown + 1
        ShutdownType = tagShutdownType
        if not defined(__IProcessLock_INTERFACE_DEFINED__):
            # interface IProcessLock
            # [unique][uuid][local][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IProcessLock = MIDL_INTERFACE(
                    "{000001D5-0000-0000-C000-000000000046}"
                )
                IProcessLock._iid_ = IID_IProcessLock

                IProcessLock._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AddRefOnProcess')],
                        ULONG,
                        'AddRefOnProcess',
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseRefOnProcess')],
                        ULONG,
                        'ReleaseRefOnProcess',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IProcessLock_INTERFACE_DEFINED__

        if not defined(__ISurrogateService_INTERFACE_DEFINED__):
            # interface ISurrogateService
            # [unique][uuid][local][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISurrogateService = MIDL_INTERFACE(
                    "{000001D4-0000-0000-C000-000000000046}"
                )
                ISurrogateService._iid_ = IID_ISurrogateService

                ISurrogateService._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Init')],
                        HRESULT,
                        'Init',
                        (['in'], REFGUID, 'rguidProcessID'),
                        (['in'], POINTER(IProcessLock), 'pProcessLock'),
                        (['out'], POINTER(BOOL), 'pfApplicationAware'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ApplicationLaunch')],
                        HRESULT,
                        'ApplicationLaunch',
                        (['in'], REFGUID, 'rguidApplID'),
                        (['in'], ApplicationType, 'appType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ApplicationFree')],
                        HRESULT,
                        'ApplicationFree',
                        (['in'], REFGUID, 'rguidApplID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CatalogRefresh')],
                        HRESULT,
                        'CatalogRefresh',
                        (['in'], ULONG, 'ulReserved'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ProcessShutdown')],
                        HRESULT,
                        'ProcessShutdown',
                        (['in'], ShutdownType, 'shutdownType'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISurrogateService_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0089
        # [local]
        if _WIN32_WINNT >= 0x0501:
            if not defined(__IInitializeSpy_INTERFACE_DEFINED__):
                # interface IInitializeSpy
                # [unique][uuid][object][local]
                # [unique]
                LPINITIALIZESPY = POINTER(IInitializeSpy)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IInitializeSpy = MIDL_INTERFACE(
                        "{00000034-0000-0000-C000-000000000046}"
                    )
                    IInitializeSpy._iid_ = IID_IInitializeSpy

                    IInitializeSpy._methods_ = [
                        COMMETHOD(
                            [helpstring('Method PreInitialize')],
                            HRESULT,
                            'PreInitialize',
                            (['in'], DWORD, 'dwCoInit'),
                            (['in'], DWORD, 'dwCurThreadAptRefs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method PostInitialize')],
                            HRESULT,
                            'PostInitialize',
                            (['in'], HRESULT, 'hrCoInit'),
                            (['in'], DWORD, 'dwCoInit'),
                            (['in'], DWORD, 'dwNewThreadAptRefs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method PreUninitialize')],
                            HRESULT,
                            'PreUninitialize',
                            (['in'], DWORD, 'dwCurThreadAptRefs'),
                        ),
                        COMMETHOD(
                            [helpstring('Method PostUninitialize')],
                            HRESULT,
                            'PostUninitialize',
                            (['in'], DWORD, 'dwNewThreadAptRefs'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IInitializeSpy_INTERFACE_DEFINED__

            # interface __MIDL_itf_objidl_0000_0090
            # [local]        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IApartmentShutdown_INTERFACE_DEFINED__):
            # interface IApartmentShutdown
            # [unique][uuid][object][local]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IApartmentShutdown = MIDL_INTERFACE(
                    "{A2F05A09-27A2-42B5-BC0E-AC163EF49D9B}"
                )
                IApartmentShutdown._iid_ = IID_IApartmentShutdown

                IApartmentShutdown._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnUninitialize')],
                        VOID,
                        'OnUninitialize',
                        (['in'], UINT64, 'ui64ApartmentIdentifier'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IApartmentShutdown_INTERFACE_DEFINED__

        # interface __MIDL_itf_objidl_0000_0091
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if _MSC_VER >= 800:
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF
    # END IF

    # Additional Prototypes for ALL interfaces
    ole32 = ctypes.windll.OLE32

    # ULONG CLIPFORMAT_UserSize(
    # __RPC__in ULONG *, ULONG, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserSize = ole32.CLIPFORMAT_UserSize
    CLIPFORMAT_UserSize.restype = ULONG

    # UCHAR * CLIPFORMAT_UserMarshal(
    # __RPC__in ULONG *,
    # __RPC__inout_xcount(0) UCHAR *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserMarshal = ole32.CLIPFORMAT_UserMarshal
    CLIPFORMAT_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * CLIPFORMAT_UserUnmarshal(
    # __RPC__in ULONG *,
    # __RPC__in_xcount(0) UCHAR *, __RPC__out CLIPFORMAT * );
    CLIPFORMAT_UserUnmarshal = ole32.CLIPFORMAT_UserUnmarshal
    CLIPFORMAT_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID CLIPFORMAT_UserFree(__RPC__in ULONG *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserFree = ole32.CLIPFORMAT_UserFree
    CLIPFORMAT_UserFree.restype = VOID

    # ULONG HBITMAP_UserSize(__RPC__in ULONG *, ULONG, __RPC__in HBITMAP * );
    HBITMAP_UserSize = ole32.HBITMAP_UserSize
    HBITMAP_UserSize.restype = ULONG

    # UCHAR *  HBITMAP_UserMarshal(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HBITMAP * );
    HBITMAP_UserMarshal = ole32.HBITMAP_UserMarshal
    HBITMAP_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * HBITMAP_UserUnmarshal(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HBITMAP * );
    HBITMAP_UserUnmarshal = ole32.HBITMAP_UserUnmarshal
    HBITMAP_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID HBITMAP_UserFree(__RPC__in ULONG *, __RPC__in HBITMAP * );
    HBITMAP_UserFree = ole32.HBITMAP_UserFree
    HBITMAP_UserFree.restype = VOID

    # ULONG HDC_UserSize(__RPC__in ULONG *, ULONG, __RPC__in HDC * );
    HDC_UserSize = ole32.HDC_UserSize
    HDC_UserSize.restype = ULONG

    # UCHAR *  HDC_UserMarshal(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HDC * );
    HDC_UserMarshal = ole32.HDC_UserMarshal
    HDC_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * HDC_UserUnmarshal(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HDC * );
    HDC_UserUnmarshal = ole32.HDC_UserUnmarshal
    HDC_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID HDC_UserFree(__RPC__in ULONG *, __RPC__in HDC * );
    HDC_UserFree = ole32.HDC_UserFree
    HDC_UserFree.restype = VOID

    # ULONG HICON_UserSize(__RPC__in ULONG *, ULONG, __RPC__in HICON * );
    HICON_UserSize = ole32.HICON_UserSize
    HICON_UserSize.restype = ULONG

    # UCHAR * HICON_UserMarshal(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HICON * );
    HICON_UserMarshal = ole32.HICON_UserMarshal
    HICON_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * HICON_UserUnmarshal(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HICON * );
    HICON_UserUnmarshal = ole32.HICON_UserUnmarshal
    HICON_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID HICON_UserFree(__RPC__in ULONG *, __RPC__in HICON * );
    HICON_UserFree = ole32.HICON_UserFree
    HICON_UserFree.restype = VOID

    # ULONG SNB_UserSize(__RPC__in ULONG *, ULONG, __RPC__in SNB * );
    SNB_UserSize = ole32.SNB_UserSize
    SNB_UserSize.restype = ULONG

    # UCHAR * SNB_UserMarshal(
    #  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in SNB * );
    SNB_UserMarshal = ole32.SNB_UserMarshal
    SNB_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  SNB_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out SNB * );
    SNB_UserUnmarshal = ole32.SNB_UserUnmarshal
    SNB_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID SNB_UserFree(__RPC__in ULONG *, __RPC__in SNB * );
    SNB_UserFree = ole32.SNB_UserFree
    SNB_UserFree.restype = VOID

    # ULONG STGMEDIUM_UserSize(
    # __RPC__in ULONG *, ULONG, __RPC__in STGMEDIUM * );
    STGMEDIUM_UserSize = ole32.STGMEDIUM_UserSize
    STGMEDIUM_UserSize.restype = ULONG

    # UCHAR * STGMEDIUM_UserMarshal(
    # __RPC__in ULONG *,
    # __RPC__inout_xcount(0) UCHAR *, __RPC__in STGMEDIUM * );
    STGMEDIUM_UserMarshal = ole32.STGMEDIUM_UserMarshal
    STGMEDIUM_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR * STGMEDIUM_UserUnmarshal(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out STGMEDIUM * );
    STGMEDIUM_UserUnmarshal = ole32.STGMEDIUM_UserUnmarshal
    STGMEDIUM_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID STGMEDIUM_UserFree(__RPC__in ULONG *, __RPC__in STGMEDIUM * );
    STGMEDIUM_UserFree = ole32.STGMEDIUM_UserFree
    STGMEDIUM_UserFree.restype = VOID

    # ULONG CLIPFORMAT_UserSize64(
    # __RPC__in ULONG *, ULONG, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserSize64 = ole32.CLIPFORMAT_UserSize64
    CLIPFORMAT_UserSize64.restype = ULONG

    # UCHAR *  CLIPFORMAT_UserMarshal64(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserMarshal64 = ole32.CLIPFORMAT_UserMarshal64
    CLIPFORMAT_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR * CLIPFORMAT_UserUnmarshal64(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out CLIPFORMAT * );
    CLIPFORMAT_UserUnmarshal64 = ole32.CLIPFORMAT_UserUnmarshal64
    CLIPFORMAT_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID CLIPFORMAT_UserFree64(__RPC__in ULONG *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserFree64 = ole32.CLIPFORMAT_UserFree64
    CLIPFORMAT_UserFree64.restype = VOID

    # ULONG HBITMAP_UserSize64(__RPC__in ULONG *, ULONG, __RPC__in HBITMAP * );
    HBITMAP_UserSize64 = ole32.HBITMAP_UserSize64
    HBITMAP_UserSize64.restype = ULONG

    # UCHAR * HBITMAP_UserMarshal64(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HBITMAP * );
    HBITMAP_UserMarshal64 = ole32.HBITMAP_UserMarshal64
    HBITMAP_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR * HBITMAP_UserUnmarshal64(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HBITMAP * );
    HBITMAP_UserUnmarshal64 = ole32.HBITMAP_UserUnmarshal64
    HBITMAP_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID HBITMAP_UserFree64(__RPC__in ULONG *, __RPC__in HBITMAP * );
    HBITMAP_UserFree64 = ole32.HBITMAP_UserFree64
    HBITMAP_UserFree64.restype = VOID

    # ULONG HDC_UserSize64(__RPC__in ULONG *, ULONG, __RPC__in HDC * );
    HDC_UserSize64 = ole32.HDC_UserSize64
    HDC_UserSize64.restype = ULONG

    # UCHAR * HDC_UserMarshal64(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HDC * );
    HDC_UserMarshal64 = ole32.HDC_UserMarshal64
    HDC_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR * HDC_UserUnmarshal64(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HDC * );
    HDC_UserUnmarshal64 = ole32.HDC_UserUnmarshal64
    HDC_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID HDC_UserFree64(__RPC__in ULONG *, __RPC__in HDC * );
    HDC_UserFree64 = ole32.HDC_UserFree64
    HDC_UserFree64.restype = VOID

    # ULONG HICON_UserSize64(__RPC__in ULONG *, ULONG , __RPC__in HICON * );
    HICON_UserSize64 = ole32.HICON_UserSize64
    HICON_UserSize64.restype = ULONG

    # UCHAR * HICON_UserMarshal64(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HICON * );
    HICON_UserMarshal64 = ole32.HICON_UserMarshal64
    HICON_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR * HICON_UserUnmarshal64
    # (__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HICON * );
    HICON_UserUnmarshal64 = ole32.HICON_UserUnmarshal64
    HICON_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID  HICON_UserFree64(     __RPC__in ULONG *, __RPC__in HICON * );
    HICON_UserFree64 = ole32.HICON_UserFree64
    HICON_UserFree64.restype = VOID

    # ULONG SNB_UserSize64( __RPC__in ULONG *, ULONG , __RPC__in SNB * );
    SNB_UserSize64 = ole32.SNB_UserSize64
    SNB_UserSize64.restype = ULONG

    # UCHAR * SNB_UserMarshal64(
    # __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in SNB * );
    SNB_UserMarshal64 = ole32.SNB_UserMarshal64
    SNB_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR * SNB_UserUnmarshal64(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out SNB * );
    SNB_UserUnmarshal64 = ole32.SNB_UserUnmarshal64
    SNB_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID SNB_UserFree64(__RPC__in ULONG *, __RPC__in SNB * );
    SNB_UserFree64 = ole32.SNB_UserFree64
    SNB_UserFree64.restype = VOID

    # ULONG STGMEDIUM_UserSize64(
    # __RPC__in ULONG *, ULONG            , __RPC__in STGMEDIUM * );
    STGMEDIUM_UserSize64 = ole32.STGMEDIUM_UserSize64
    STGMEDIUM_UserSize64.restype = ULONG

    # UCHAR *  STGMEDIUM_UserMarshal64(
    #   __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in STGMEDIUM * );
    STGMEDIUM_UserMarshal64 = ole32.STGMEDIUM_UserMarshal64
    STGMEDIUM_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR * STGMEDIUM_UserUnmarshal64(
    # __RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out STGMEDIUM * );
    STGMEDIUM_UserUnmarshal64 = ole32.STGMEDIUM_UserUnmarshal64
    STGMEDIUM_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID STGMEDIUM_UserFree64( __RPC__in ULONG *, __RPC__in STGMEDIUM * );
    STGMEDIUM_UserFree64 = ole32.STGMEDIUM_UserFree64
    STGMEDIUM_UserFree64.restype = VOID

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

    # HRESULT STDMETHODCALLTYPE IEnumSTATSTG_Next_Proxy( // [local]
    # IEnumSTATSTG * This,
    # ULONG celt, // [in]
    # // [annotation]
    # _Out_writes_to_(celt,*pceltFetched)  STATSTG *rgelt,
    # // [annotation]
    # _Out_opt_  ULONG *pceltFetched);
    IEnumSTATSTG_Next_Proxy = ole32.IEnumSTATSTG_Next_Proxy
    IEnumSTATSTG_Next_Proxy.restype = HRESULT

    # [call_as]    # [in]    # [length_is][size_is][out]    # [out]
    # HRESULT STDMETHODCALLTYPE IStorage_OpenStream_Proxy( // [local]
    # IStorage * This,
    # // [annotation][string][in]
    # _In_z_  OLECHAR *pwcsName,
    # // [annotation][unique][in]
    # _Reserved_  VOID *reserved1,
    # DWORD grfMode, // [in]
    # DWORD reserved2, // [in]
    # // [annotation][out]
    # _Outptr_  IStream **ppstm);
    IStorage_OpenStream_Proxy = ole32.IStorage_OpenStream_Proxy
    IStorage_OpenStream_Proxy.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStorage_OpenStream_Stub( // [call_as]
    # __RPC__in IStorage * This,
    # __RPC__in_string OLECHAR *pwcsName, // [string][in]
    # ULONG cbReserved1, // [in]
    # __RPC__in_ecount_full_opt(cbReserved1) BYTE *reserved1,
    #  [size_is][unique][in]
    # DWORD grfMode, // [in]
    # DWORD reserved2, // [in]
    # __RPC__deref_out_opt IStream **ppstm); // [out]
    IStorage_OpenStream_Stub = ole32.IStorage_OpenStream_Stub
    IStorage_OpenStream_Stub.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStorage_CopyTo_Proxy( // [local]
    # IStorage * This,
    # DWORD ciidExclude, // [in]
    # // [annotation][size_is][unique][in]
    # _In_reads_opt_(ciidExclude)  IID *rgiidExclude,
    # // [annotation][unique][in]
    # _In_opt_  SNB snbExclude,
    # // [annotation][unique][in]
    # _In_  IStorage *pstgDest);
    IStorage_CopyTo_Proxy = ole32.IStorage_CopyTo_Proxy
    IStorage_CopyTo_Proxy.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStorage_CopyTo_Stub(
    # [call_as]
    # __RPC__in IStorage * This,
    # DWORD ciidExclude, // [in]
    # __RPC__in_ecount_full_opt(ciidExclude) IID *rgiidExclude,
    # [size_is][unique][in]
    # __RPC__deref_opt_in_opt SNB snbExclude, // [unique][in]
    # __RPC__in_opt IStorage *pstgDest); // [unique][in]
    IStorage_CopyTo_Stub = ole32.IStorage_CopyTo_Stub
    IStorage_CopyTo_Stub.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStorage_EnumElements_Proxy( // [local]
    # IStorage * This,
    # // [annotation][in]
    # _Reserved_  DWORD reserved1,
    # // [annotation][size_is][unique][in]
    # _Reserved_  VOID *reserved2,
    # // [annotation][in]
    # _Reserved_  DWORD reserved3,
    # // [annotation][out]
    # _Outptr_  IEnumSTATSTG **ppenum);
    IStorage_EnumElements_Proxy = ole32.IStorage_EnumElements_Proxy
    IStorage_EnumElements_Proxy.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IStorage_EnumElements_Stub(
    # __RPC__in IStorage * This,
    # DWORD reserved1, // [in]
    # ULONG cbReserved2, // [in]
    # __RPC__in_ecount_full_opt(cbReserved2) BYTE *reserved2,
    # DWORD reserved3, // [in]
    # __RPC__deref_out_opt IEnumSTATSTG **ppenum); // [out]
    IStorage_EnumElements_Stub = ole32.IStorage_EnumElements_Stub
    IStorage_EnumElements_Stub.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE ILockBytes_WriteAt_Proxy( // [local]
    # ILockBytes * This,
    # ULARGE_INTEGER ulOffset, // [in]
    # // [annotation][size_is][in]
    # _In_reads_BYTEs_(cb)  VOID *pv,
    # ULONG cb, // [in]
    # // [annotation][out]
    # _Out_opt_  ULONG *pcbWritten);
    ILockBytes_WriteAt_Proxy = ole32.ILockBytes_WriteAt_Proxy
    ILockBytes_WriteAt_Proxy.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE ILockBytes_WriteAt_Stub( // [call_as]
    # __RPC__in ILockBytes * This,
    # ULARGE_INTEGER ulOffset, // [in]
    # __RPC__in_ecount_full(cb) BYTE *pv, // [size_is][in]
    # ULONG cb, // [in]
    # __RPC__out ULONG *pcbWritten); // [out]
    ILockBytes_WriteAt_Stub = ole32.ILockBytes_WriteAt_Stub
    ILockBytes_WriteAt_Stub.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IFillLockBytes_FillAppend_Proxy( // [local]
    # IFillLockBytes * This,
    # // [annotation][size_is][in]
    # _In_reads_BYTEs_(cb)  VOID *pv,
    # // [annotation][in]
    # _In_  ULONG cb,
    # // [annotation][out]
    # _Out_  ULONG *pcbWritten);
    IFillLockBytes_FillAppend_Proxy = ole32.IFillLockBytes_FillAppend_Proxy
    IFillLockBytes_FillAppend_Proxy.restype = HRESULT

    # HRESULT __stdcall IFillLockBytes_FillAppend_Stub( // [call_as]
    # __RPC__in IFillLockBytes * This,
    # __RPC__in_ecount_full(cb) BYTE *pv, // [size_is][in]
    # ULONG cb, // [in]
    # __RPC__out ULONG *pcbWritten); // [out]
    IFillLockBytes_FillAppend_Stub = ole32.IFillLockBytes_FillAppend_Stub
    IFillLockBytes_FillAppend_Stub.restype = HRESULT

    # HRESULT STDMETHODCALLTYPE IFillLockBytes_FillAt_Proxy( // [local]
    # IFillLockBytes * This,
    # // [annotation][in]
    # _In_  ULARGE_INTEGER ulOffset,
    # // [annotation][size_is][in]
    # _In_reads_BYTEs_(cb)  VOID *pv,
    # // [annotation][in]
    # _In_  ULONG cb,
    # // [annotation][out]
    # _Out_  ULONG *pcbWritten);
    IFillLockBytes_FillAt_Proxy = ole32.IFillLockBytes_FillAt_Proxy
    IFillLockBytes_FillAt_Proxy.restype = HRESULT

    # HRESULT __stdcall IFillLockBytes_FillAt_Stub( // [call_as]
    # __RPC__in IFillLockBytes * This,
    # ULARGE_INTEGER ulOffset, // [in]
    # __RPC__in_ecount_full(cb) BYTE *pv, // [size_is][in]
    # ULONG cb, // [in]
    # __RPC__out ULONG *pcbWritten); // [out]
    IFillLockBytes_FillAt_Stub = ole32.IFillLockBytes_FillAt_Stub
    IFillLockBytes_FillAt_Stub.restype = HRESULT

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


