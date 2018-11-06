__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import *
# from .rpcndr_h import *
# from windows_h
# from .ole2_h import *

from .wtypes_h import (
    ENUM,
    REFGUID,
    POINTER,
    HRESULT,
    ULONG,
    BOOL,
    ULARGE_INTEGER,
    LARGE_INTEGER,
    DWORD,
    ULONG_PTR,
    VOID,
    HBITMAP,
    LONG,
    CLSID,
    REFIID,
    LPCOLESTR,
    LPOLESTR,
    UINT64,
    HANDLE,
    LPCWSTR,
    LPCLSID,
    DOUBLE,
    FILETIME,
    REFCLSID,
    OLECHAR,
    HICON,
    HDC,
    HTASK,
    BYTE,
    LCID,
    GUID,
    SIZE_T,
    INT,
    HMETAFILEPICT,
    HENHMETAFILE,
    HGLOBAL,
    HWND,
    wireHENHMETAFILE,
    wireHGLOBAL,
    BYTE_BLOB,
    WORD,
    LPWSTR,
    COAUTHINFO,
    wireHPALETTE,
    wireHBITMAP,
    wireHMETAFILEPICT,
    CLIPFORMAT
)
from .guiddef_h import (
    IID,
)
import ctypes
import comtypes


IID_IMarshal = IID(
    '{00000003-0000-0000-C000-000000000046}'
)


class IMarshal(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMarshal
    _idlflags_ = []


IID_INoMarshal = IID(
    '{ecc8691b-c1db-4dc0-855e-65f6c551af49}'
)


class INoMarshal(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_INoMarshal
    _idlflags_ = []


IID_IAgileObject = IID(
    '{94ea2b94-e9cc-49e0-c0ff-ee64ca8f5b90}'
)


class IAgileObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAgileObject
    _idlflags_ = []


IID_IActivationFilter = IID(
    '{00000017-0000-0000-C000-000000000046}'
)


class IActivationFilter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IActivationFilter
    _idlflags_ = []


IID_IMarshal2 = IID(
    '{000001cf-0000-0000-C000-000000000046}'
)


class IMarshal2(IMarshal):
    _case_insensitive_ = True
    _iid_ = IID_IMarshal2
    _idlflags_ = []


IID_IMalloc = IID(
    '{00000002-0000-0000-C000-000000000046}'
)


class IMalloc(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMalloc
    _idlflags_ = []


IID_IStdMarshalInfo = IID(
    '{00000018-0000-0000-C000-000000000046}'
)


class IStdMarshalInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IStdMarshalInfo
    _idlflags_ = []


IID_IExternalConnection = IID(
    '{00000019-0000-0000-C000-000000000046}'
)


class IExternalConnection(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IExternalConnection
    _idlflags_ = []


IID_IMultiQI = IID(
    '{00000020-0000-0000-C000-000000000046}'
)


class IMultiQI(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMultiQI
    _idlflags_ = []


IID_AsyncIMultiQI = IID(
    '{000e0020-0000-0000-C000-000000000046}'
)


class AsyncIMultiQI(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIMultiQI
    _idlflags_ = []


IID_IInternalUnknown = IID(
    '{00000021-0000-0000-C000-000000000046}'
)


class IInternalUnknown(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInternalUnknown
    _idlflags_ = []


IID_IEnumUnknown = IID(
    '{00000100-0000-0000-C000-000000000046}'
)


class IEnumUnknown(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumUnknown
    _idlflags_ = []


IID_IEnumString = IID(
    '{00000101-0000-0000-C000-000000000046}'
)


class IEnumString(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumString
    _idlflags_ = []


IID_ISequentialStream = IID(
    '{0c733a30-2a1c-11ce-ade5-00aa0044773d}'
)


class ISequentialStream(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISequentialStream
    _idlflags_ = []


IID_IStream = IID(
    '{0000000c-0000-0000-C000-000000000046}'
)


class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = IID_IStream
    _idlflags_ = []


IID_IRpcChannelBuffer = IID(
    '{D5F56B60-593B-101A-B569-08002B2DBF7A}'
)


class IRpcChannelBuffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRpcChannelBuffer
    _idlflags_ = []


IID_IRpcChannelBuffer2 = IID(
    '{594f31d0-7f19-11d0-b194-00a0c90dc8bf}'
)


class IRpcChannelBuffer2(IRpcChannelBuffer):
    _case_insensitive_ = True
    _iid_ = IID_IRpcChannelBuffer2
    _idlflags_ = []


IID_IAsyncRpcChannelBuffer = IID(
    '{a5029fb6-3c34-11d1-9c99-00c04fb998aa}'
)


class IAsyncRpcChannelBuffer(IRpcChannelBuffer2):
    _case_insensitive_ = True
    _iid_ = IID_IAsyncRpcChannelBuffer
    _idlflags_ = []


IID_IRpcChannelBuffer3 = IID(
    '{25B15600-0115-11d0-BF0D-00AA00B8DFD2}'
)


class IRpcChannelBuffer3(IRpcChannelBuffer2):
    _case_insensitive_ = True
    _iid_ = IID_IRpcChannelBuffer3
    _idlflags_ = []


IID_IRpcSyntaxNegotiate = IID(
    '{58a08519-24c8-4935-b482-3fd823333a4f}'
)


class IRpcSyntaxNegotiate(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRpcSyntaxNegotiate
    _idlflags_ = []


IID_IRpcProxyBuffer = IID(
    '{D5F56A34-593B-101A-B569-08002B2DBF7A}'
)


class IRpcProxyBuffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRpcProxyBuffer
    _idlflags_ = []


IID_IRpcStubBuffer = IID(
    '{D5F56AFC-593B-101A-B569-08002B2DBF7A}'
)


class IRpcStubBuffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRpcStubBuffer
    _idlflags_ = []


IID_IPSFactoryBuffer = IID(
    '{D5F569D0-593B-101A-B569-08002B2DBF7A}'
)


class IPSFactoryBuffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPSFactoryBuffer
    _idlflags_ = []


IID_IChannelHook = IID(
    '{1008c4a0-7613-11cf-9af1-0020af6e72f4}'
)


class IChannelHook(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IChannelHook
    _idlflags_ = []


IID_IClientSecurity = IID(
    '{0000013D-0000-0000-C000-000000000046}'
)


class IClientSecurity(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IClientSecurity
    _idlflags_ = []


IID_IServerSecurity = IID(
    '{0000013E-0000-0000-C000-000000000046}'
)


class IServerSecurity(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IServerSecurity
    _idlflags_ = []


IID_IRpcOptions = IID(
    '{00000144-0000-0000-C000-000000000046}'
)


class IRpcOptions(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRpcOptions
    _idlflags_ = []


IID_IGlobalOptions = IID(
    '{0000015B-0000-0000-C000-000000000046}'
)


class IGlobalOptions(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IGlobalOptions
    _idlflags_ = []


IID_ISurrogate = IID(
    '{00000022-0000-0000-C000-000000000046}'
)


class ISurrogate(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISurrogate
    _idlflags_ = []


IID_IGlobalInterfaceTable = IID(
    '{00000146-0000-0000-C000-000000000046}'
)


class IGlobalInterfaceTable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IGlobalInterfaceTable
    _idlflags_ = []


IID_ISynchronize = IID(
    '{00000030-0000-0000-C000-000000000046}'
)


class ISynchronize(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISynchronize
    _idlflags_ = []


IID_ISynchronizeHandle = IID(
    '{00000031-0000-0000-C000-000000000046}'
)


class ISynchronizeHandle(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISynchronizeHandle
    _idlflags_ = []


IID_ISynchronizeEvent = IID(
    '{00000032-0000-0000-C000-000000000046}'
)


class ISynchronizeEvent(ISynchronizeHandle):
    _case_insensitive_ = True
    _iid_ = IID_ISynchronizeEvent
    _idlflags_ = []


IID_ISynchronizeContainer = IID(
    '{00000033-0000-0000-C000-000000000046}'
)


class ISynchronizeContainer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISynchronizeContainer
    _idlflags_ = []


IID_ISynchronizeMutex = IID(
    '{00000025-0000-0000-C000-000000000046}'
)


class ISynchronizeMutex(ISynchronize):
    _case_insensitive_ = True
    _iid_ = IID_ISynchronizeMutex
    _idlflags_ = []


IID_ICancelMethodCalls = IID(
    '{00000029-0000-0000-C000-000000000046}'
)


class ICancelMethodCalls(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICancelMethodCalls
    _idlflags_ = []


IID_IAsyncManager = IID(
    '{0000002A-0000-0000-C000-000000000046}'
)


class IAsyncManager(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAsyncManager
    _idlflags_ = []


IID_ICallFactory = IID(
    '{1c733a30-2a1c-11ce-ade5-00aa0044773d}'
)


class ICallFactory(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ICallFactory
    _idlflags_ = []


IID_IRpcHelper = IID(
    '{00000149-0000-0000-C000-000000000046}'
)


class IRpcHelper(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRpcHelper
    _idlflags_ = []


IID_IReleaseMarshalBuffers = IID(
    '{eb0cb9e8-7996-11d2-872e-0000f8080859}'
)


class IReleaseMarshalBuffers(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IReleaseMarshalBuffers
    _idlflags_ = []


IID_IWaitMultiple = IID(
    '{0000002B-0000-0000-C000-000000000046}'
)


class IWaitMultiple(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IWaitMultiple
    _idlflags_ = []


IID_IAddrTrackingControl = IID(
    '{00000147-0000-0000-C000-000000000046}'
)


class IAddrTrackingControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAddrTrackingControl
    _idlflags_ = []


IID_IAddrExclusionControl = IID(
    '{00000148-0000-0000-C000-000000000046}'
)


class IAddrExclusionControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAddrExclusionControl
    _idlflags_ = []


IID_IPipeByte = IID(
    '{DB2F3ACA-2F86-11d1-8E04-00C04FB9989A}'
)


class IPipeByte(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPipeByte
    _idlflags_ = []


IID_AsyncIPipeByte = IID(
    '{DB2F3ACB-2F86-11d1-8E04-00C04FB9989A}'
)


class AsyncIPipeByte(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIPipeByte
    _idlflags_ = []


IID_IPipeLong = IID(
    '{DB2F3ACC-2F86-11d1-8E04-00C04FB9989A}'
)


class IPipeLong(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPipeLong
    _idlflags_ = []


IID_AsyncIPipeLong = IID(
    '{DB2F3ACD-2F86-11d1-8E04-00C04FB9989A}'
)


class AsyncIPipeLong(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIPipeLong
    _idlflags_ = []


IID_IPipeDouble = IID(
    '{DB2F3ACE-2F86-11d1-8E04-00C04FB9989A}'
)


class IPipeDouble(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPipeDouble
    _idlflags_ = []


IID_AsyncIPipeDouble = IID(
    '{DB2F3ACF-2F86-11d1-8E04-00C04FB9989A}'
)


class AsyncIPipeDouble(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIPipeDouble
    _idlflags_ = []


IID_IEnumContextProps = IID(
    '{000001c1-0000-0000-C000-000000000046}'
)


class IEnumContextProps(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumContextProps
    _idlflags_ = []


IID_IContext = IID(
    '{000001c0-0000-0000-C000-000000000046}'
)


class IContext(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IContext
    _idlflags_ = []


IID_IObjContext = IID(
    '{000001c6-0000-0000-C000-000000000046}'
)


class IObjContext(IContext):
    _case_insensitive_ = True
    _iid_ = IID_IObjContext
    _idlflags_ = []


IID_IComThreadingInfo = IID(
    '{000001ce-0000-0000-C000-000000000046}'
)


class IComThreadingInfo(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IComThreadingInfo
    _idlflags_ = []


IID_IProcessInitControl = IID(
    '{72380d55-8d2b-43a3-8513-2b6ef31434e9}'
)


class IProcessInitControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IProcessInitControl
    _idlflags_ = []


IID_IFastRundown = IID(
    '{00000040-0000-0000-C000-000000000046}'
)


class IFastRundown(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFastRundown
    _idlflags_ = []


IID_IMarshalingStream = IID(
    '{D8F2F5E6-6102-4863-9F26-389A4676EFDE}'
)


class IMarshalingStream(IStream):
    _case_insensitive_ = True
    _iid_ = IID_IMarshalingStream
    _idlflags_ = []


IID_IAgileReference = IID(
    '{C03F6A43-65A4-9818-987E-E0B810D2A6F2}'
)


class IAgileReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAgileReference
    _idlflags_ = []


IID_IMallocSpy = IID(
    '{0000001d-0000-0000-C000-000000000046}'
)


class IMallocSpy(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMallocSpy
    _idlflags_ = []


IID_IBindCtx = IID(
    '{0000000e-0000-0000-C000-000000000046}'
)


class IBindCtx(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBindCtx
    _idlflags_ = []


IID_IEnumMoniker = IID(
    '{00000102-0000-0000-C000-000000000046}'
)


class IEnumMoniker(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumMoniker
    _idlflags_ = []


IID_IRunnableObject = IID(
    '{00000126-0000-0000-C000-000000000046}'
)


class IRunnableObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRunnableObject
    _idlflags_ = []


IID_IRunningObjectTable = IID(
    '{00000010-0000-0000-C000-000000000046}'
)


class IRunningObjectTable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRunningObjectTable
    _idlflags_ = []


IID_IPersist = IID(
    '{0000010c-0000-0000-C000-000000000046}'
)


class IPersist(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IPersist
    _idlflags_ = []


IID_IPersistStream = IID(
    '{00000109-0000-0000-C000-000000000046}'
)


class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistStream
    _idlflags_ = []


IID_IMoniker = IID(
    '{0000000f-0000-0000-C000-000000000046}'
)


class IMoniker(IPersistStream):
    _case_insensitive_ = True
    _iid_ = IID_IMoniker
    _idlflags_ = []


IID_IROTData = IID(
    '{f29f6bc0-5021-11ce-aa15-00006901293f}'
)


class IROTData(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IROTData
    _idlflags_ = []


IID_IEnumSTATSTG = IID(
    '{0000000d-0000-0000-C000-000000000046}'
)


class IEnumSTATSTG(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumSTATSTG
    _idlflags_ = []


IID_IStorage = IID(
    '{0000000b-0000-0000-C000-000000000046}'
)


class IStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IStorage
    _idlflags_ = []


IID_IPersistFile = IID(
    '{0000010b-0000-0000-C000-000000000046}'
)


class IPersistFile(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistFile
    _idlflags_ = []


IID_IPersistStorage = IID(
    '{0000010a-0000-0000-C000-000000000046}'
)


class IPersistStorage(IPersist):
    _case_insensitive_ = True
    _iid_ = IID_IPersistStorage
    _idlflags_ = []


IID_ILockBytes = IID(
    '{0000000a-0000-0000-C000-000000000046}'
)


class ILockBytes(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ILockBytes
    _idlflags_ = []


IID_IEnumFORMATETC = IID(
    '{00000103-0000-0000-C000-000000000046}'
)


class IEnumFORMATETC(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumFORMATETC
    _idlflags_ = []


IID_IEnumSTATDATA = IID(
    '{00000105-0000-0000-C000-000000000046}'
)


class IEnumSTATDATA(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IEnumSTATDATA
    _idlflags_ = []


IID_IRootStorage = IID(
    '{00000012-0000-0000-C000-000000000046}'
)


class IRootStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IRootStorage
    _idlflags_ = []


IID_IAdviseSink = IID(
    '{0000010f-0000-0000-C000-000000000046}'
)


class IAdviseSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAdviseSink
    _idlflags_ = []


IID_AsyncIAdviseSink = IID(
    '{00000150-0000-0000-C000-000000000046}'
)


class AsyncIAdviseSink(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIAdviseSink
    _idlflags_ = []


IID_IAdviseSink2 = IID(
    '{00000125-0000-0000-C000-000000000046}'
)


class IAdviseSink2(IAdviseSink):
    _case_insensitive_ = True
    _iid_ = IID_IAdviseSink2
    _idlflags_ = []


IID_AsyncIAdviseSink2 = IID(
    '{00000151-0000-0000-C000-000000000046}'
)


class AsyncIAdviseSink2(AsyncIAdviseSink):
    _case_insensitive_ = True
    _iid_ = IID_AsyncIAdviseSink2
    _idlflags_ = []


IID_IDataObject = IID(
    '{0000010e-0000-0000-C000-000000000046}'
)


class IDataObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDataObject
    _idlflags_ = []


IID_IDataAdviseHolder = IID(
    '{00000110-0000-0000-C000-000000000046}'
)


class IDataAdviseHolder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDataAdviseHolder
    _idlflags_ = []


IID_IMessageFilter = IID(
    '{00000016-0000-0000-C000-000000000046}'
)


class IMessageFilter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IMessageFilter
    _idlflags_ = []


IID_IClassActivator = IID(
    '{00000140-0000-0000-C000-000000000046}'
)


class IClassActivator(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IClassActivator
    _idlflags_ = []


IID_IFillLockBytes = IID(
    '{99caf010-415e-11cf-8814-00aa00b569f5}'
)


class IFillLockBytes(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IFillLockBytes
    _idlflags_ = []


IID_IProgressNotify = IID(
    '{a9d758a0-4617-11cf-95fc-00aa00680db4}'
)


class IProgressNotify(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IProgressNotify
    _idlflags_ = []


IID_ILayoutStorage = IID(
    '{0e6d4d90-6738-11cf-9608-00aa00680db4}'
)


class ILayoutStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ILayoutStorage
    _idlflags_ = []


IID_IBlockingLock = IID(
    '{30f3d47a-6447-11d1-8e3c-00c04fb9386d}'
)


class IBlockingLock(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IBlockingLock
    _idlflags_ = []


IID_ITimeAndNoticeControl = IID(
    '{bc0bf6ae-8878-11d1-83e9-00c04fc2c6d4}'
)


class ITimeAndNoticeControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ITimeAndNoticeControl
    _idlflags_ = []


IID_IOplockStorage = IID(
    '{8d19c834-8879-11d1-83e9-00c04fc2c6d4}'
)


class IOplockStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IOplockStorage
    _idlflags_ = []


IID_IDirectWriterLock = IID(
    '{0e6d4d92-6738-11cf-9608-00aa00680db4}'
)


class IDirectWriterLock(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDirectWriterLock
    _idlflags_ = []


IID_IUrlMon = IID(
    '{00000026-0000-0000-C000-000000000046}'
)


class IUrlMon(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IUrlMon
    _idlflags_ = []


IID_IForegroundTransfer = IID(
    '{00000145-0000-0000-C000-000000000046}'
)


class IForegroundTransfer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IForegroundTransfer
    _idlflags_ = []


IID_IThumbnailExtractor = IID(
    '{969dc708-5c76-11d1-8d86-0000f804b057}'
)


class IThumbnailExtractor(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IThumbnailExtractor
    _idlflags_ = []


IID_IDummyHICONIncluder = IID(
    '{947990de-cc28-11d2-a0f7-00805f858fb1}'
)


class IDummyHICONIncluder(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IDummyHICONIncluder
    _idlflags_ = []


IID_IProcessLock = IID(
    '{000001d5-0000-0000-C000-000000000046}'
)


class IProcessLock(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IProcessLock
    _idlflags_ = []


IID_ISurrogateService = IID(
    '{000001d4-0000-0000-C000-000000000046}'
)


class ISurrogateService(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ISurrogateService
    _idlflags_ = []


IID_IInitializeSpy = IID(
    '{00000034-0000-0000-C000-000000000046}'
)


class IInitializeSpy(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IInitializeSpy
    _idlflags_ = []


_WIN32_WINNT = 0x0600

from .winapifamily_h import *
# from .limits_h import *




class tagDVTARGETDEVICE(ctypes.Structure):
    _fields_ = [
        ('tdSize', DWORD),
        ('tdDriverNameOffset', WORD),
        ('tdDeviceNameOffset', WORD),
        ('tdPortNameOffset', WORD),
        ('tdExtDevmodeOffset', WORD),
        ('tdData', BYTE * 1),
    ]


DVTARGETDEVICE = tagDVTARGETDEVICE
LPCLIPFORMAT = POINTER(CLIPFORMAT)


class tagFORMATETC(ctypes.Structure):
    _fields_ = [
        ('cfFormat', CLIPFORMAT),
        ('ptd', POINTER(DVTARGETDEVICE)),
        ('dwAspect', DWORD),
        ('lindex', LONG),
        ('tymed', DWORD),
    ]


FORMATETC = tagFORMATETC
LPFORMATETC = POINTER(tagFORMATETC)


class tagSTGMEDIUM(ctypes.Structure):

    class u(ctypes.Union):
        _fields_ = [
            ('hBitmap', HBITMAP),
            ('hMetaFilePict', HMETAFILEPICT),
            ('hEnhMetaFile', HENHMETAFILE),
            ('hGlobal', HGLOBAL),
            ('lpszFileName', LPOLESTR),
            ('pstm', POINTER(IStream)),
            ('pstg', POINTER(IStorage)),
        ]

    _fields_ = [
        ('tymed', DWORD),
        ('u', u),
        ('pUnkForRelease', POINTER(comtypes.IUnknown)),
    ]


STGMEDIUM = tagSTGMEDIUM

LPDATAOBJECT = POINTER(IDataObject)


from .oleidl_h import *


class _COSERVERINFO(ctypes.Structure):
    _fields_ = [
        ('dwReserved1', DWORD),
        ('pwszName', LPWSTR),
        ('pAuthInfo', POINTER(COAUTHINFO)),
        ('dwReserved2', DWORD),
    ]


COSERVERINFO = _COSERVERINFO


LPMARSHAL = POINTER(IMarshal)
COMMETHOD = comtypes.COMMETHOD


IMarshal._methods_ = [
    COMMETHOD(
        [],
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
        [],
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
        [],
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
        [],
        HRESULT,
        'UnmarshalInterface',
        (['in'], POINTER(IStream), 'pStm'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppv'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseMarshalData',
        (['in'], POINTER(IStream), 'pStm'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DisconnectObject',
        (['in'], DWORD, 'dwReserved'),
    ),
]


class tagACTIVATIONTYPE(ENUM):
    ACTIVATIONTYPE_UNCATEGORIZED = 0
    ACTIVATIONTYPE_FROM_MONIKER = 0x1
    ACTIVATIONTYPE_FROM_DATA = 0x2
    ACTIVATIONTYPE_FROM_STORAGE = 0x4
    ACTIVATIONTYPE_FROM_STREAM = 0x8
    ACTIVATIONTYPE_FROM_FILE = 0x10


ACTIVATIONTYPE = tagACTIVATIONTYPE


IActivationFilter._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'HandleActivation',
        (['in'], DWORD, 'dwActivationType'),
        (['in'], REFCLSID, 'rclsid'),
        (['out'], POINTER(CLSID), 'pReplacementClsId'),
    ),
]


LPMARSHAL2 = POINTER(IMarshal2)
LPMALLOC = POINTER(IMalloc)


IMalloc._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'Alloc',
        (['in'], SIZE_T, 'cb'),
    ),
    COMMETHOD(
        [],
        VOID,
        'Realloc',
        (['in'], POINTER(VOID), 'pv'),
        (['in'], SIZE_T, 'cb'),
    ),
    COMMETHOD(
        [],
        VOID,
        'Free',
        (['in'], POINTER(VOID), 'pv'),
    ),
    COMMETHOD(
        [],
        SIZE_T,
        'GetSize',
        (['in'], POINTER(VOID), 'pv'),
    ),
    COMMETHOD(
        [],
        INT,
        'DidAlloc',
        (['in'], POINTER(VOID), 'pv'),
    ),
    COMMETHOD(
        [],
        VOID,
        'HeapMinimize'
    ),
]


LPSTDMARSHALINFO = POINTER(IStdMarshalInfo)
IStdMarshalInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetClassForHandler',
        (['in'], DWORD, 'dwDestContext'),
        (['in'], POINTER(VOID), 'pvDestContext'),
        (['out'], POINTER(CLSID), 'pClsid'),
    ),
]


LPEXTERNALCONNECTION = POINTER(IExternalConnection)


class tagEXTCONN(ENUM):
    EXTCONN_STRONG = 0x1
    EXTCONN_WEAK = 0x2
    EXTCONN_CALLABLE = 0x4


EXTCONN = tagEXTCONN


IExternalConnection._methods_ = [
    COMMETHOD(
        [],
        DWORD,
        'AddConnection',
        (['in'], DWORD, 'extconn'),
        (['in'], DWORD, 'reserved'),
    ),
    COMMETHOD(
        [],
        DWORD,
        'ReleaseConnection',
        (['in'], DWORD, 'extconn'),
        (['in'], DWORD, 'reserved'),
        (['in'], BOOL, 'fLastReleaseCloses'),
    ),
]


LPMULTIQI = POINTER(IMultiQI)


class tagMULTI_QI(ctypes.Structure):
    _fields_ = [
        ('pIID', POINTER(IID)),
        ('pItf', POINTER(comtypes.IUnknown)),
        ('hr', HRESULT),
    ]


MULTI_QI = tagMULTI_QI


IMultiQI._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryMultipleInterfaces',
        (['in'], ULONG, 'cMQIs'),
        (['in', 'out'], POINTER(MULTI_QI), 'pMQIs'),
    ),
]


AsyncIMultiQI._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Begin_QueryMultipleInterfaces',
        (['in'], ULONG, 'cMQIs'),
        (['in', 'out'], POINTER(MULTI_QI), 'pMQIs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_QueryMultipleInterfaces',
        (['in', 'out'], POINTER(MULTI_QI), 'pMQIs'),
    ),
]


IInternalUnknown._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryInternalInterface',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppv'),
    ),
]


LPENUMUNKNOWN = POINTER(IEnumUnknown)


IEnumUnknown._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(POINTER(comtypes.IUnknown)), 'rgelt'),
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
        (['out'], POINTER(POINTER(IEnumUnknown)), 'ppenum'),
    ),
]


LPENUMSTRING = POINTER(IEnumString)


IEnumString._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(LPOLESTR), 'rgelt'),
        ([], POINTER(ULONG), 'pceltFetched'),
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
        (['out'], POINTER(POINTER(IEnumString)), 'ppenum'),
    ),
]


ISequentialStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Read',
        ([], POINTER(VOID), 'pv'),
        (['in'], ULONG, 'cb'),
        ([], POINTER(ULONG), 'pcbRead'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Write',
        ([], POINTER(VOID), 'pv'),
        (['in'], ULONG, 'cb'),
        ([], POINTER(ULONG), 'pcbWritten'),
    ),
]


LPSTREAM = POINTER(IStream)


class tagSTATSTG(ctypes.Structure):
    _fields_ = [
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


STATSTG = tagSTATSTG


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


IStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Seek',
        (['in'], LARGE_INTEGER, 'dlibMove'),
        (['in'], DWORD, 'dwOrigin'),
        ([], POINTER(ULARGE_INTEGER), 'plibNewPosition'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSize',
        (['in'], ULARGE_INTEGER, 'libNewSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CopyTo',
        (['in'], POINTER(IStream), 'pstm'),
        (['in'], ULARGE_INTEGER, 'cb'),
        ([], POINTER(ULARGE_INTEGER), 'pcbRead'),
        ([], POINTER(ULARGE_INTEGER), 'pcbWritten'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Commit',
        (['in'], DWORD, 'grfCommitFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LockRegion',
        (['in'], ULARGE_INTEGER, 'libOffset'),
        (['in'], ULARGE_INTEGER, 'cb'),
        (['in'], DWORD, 'dwLockType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnlockRegion',
        (['in'], ULARGE_INTEGER, 'libOffset'),
        (['in'], ULARGE_INTEGER, 'cb'),
        (['in'], DWORD, 'dwLockType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Stat',
        (['out'], POINTER(STATSTG), 'pstatstg'),
        (['in'], DWORD, 'grfStatFlag'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Clone',
        (['out'], POINTER(POINTER(IStream)), 'ppstm'),
    ),
]


RPCOLEDATAREP = ULONG


class tagRPCOLEMESSAGE(ctypes.Structure):
    _fields_ = [
        ('reserved1', POINTER(VOID)),
        ('dataRepresentation', RPCOLEDATAREP),
        ('Buffer', POINTER(VOID)),
        ('cbBuffer', ULONG),
        ('iMethod', ULONG),
        ('reserved2', POINTER(VOID) * 5),
        ('rpcFlags', ULONG),
    ]


RPCOLEMESSAGE = tagRPCOLEMESSAGE
PRPCOLEMESSAGE = POINTER(RPCOLEMESSAGE)


IRpcChannelBuffer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetBuffer',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMessage'),
        (['in'], REFIID, 'riid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SendReceive',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMessage'),
        (['out'], POINTER(ULONG), 'pStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FreeBuffer',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMessage'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDestCtx',
        (['out'], POINTER(DWORD), 'pdwDestContext'),
        (['out'], POINTER(POINTER(VOID)), 'ppvDestContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsConnected'
    ),
]


IRpcChannelBuffer2._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetProtocolVersion',
        (['out'], POINTER(DWORD), 'pdwVersion'),
    ),
]


IAsyncRpcChannelBuffer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Send',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['in'], POINTER(ISynchronize), 'pSync'),
        (['out'], POINTER(ULONG), 'pulStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Receive',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['out'], POINTER(ULONG), 'pulStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDestCtxEx',
        (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['out'], POINTER(DWORD), 'pdwDestContext'),
        (['out'], POINTER(POINTER(VOID)), 'ppvDestContext'),
    ),
]


IRpcChannelBuffer3._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Send',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['out'], POINTER(ULONG), 'pulStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Receive',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['in'], ULONG, 'ulSize'),
        (['out'], POINTER(ULONG), 'pulStatus'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Cancel',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCallContext',
        (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'pInterface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDestCtxEx',
        (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['out'], POINTER(DWORD), 'pdwDestContext'),
        (['out'], POINTER(POINTER(VOID)), 'ppvDestContext'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        (['in'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['out'], POINTER(DWORD), 'pState'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterAsync',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['in'], POINTER(IAsyncManager), 'pAsyncMgr'),
    ),
]


IRpcSyntaxNegotiate._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'NegotiateSyntax',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
    ),
]


IRpcProxyBuffer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Connect',
        (['in'], POINTER(IRpcChannelBuffer), 'pRpcChannelBuffer'),
    ),
    COMMETHOD(
        [],
        VOID,
        'Disconnect'
    ),
]

IRpcStubBuffer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Connect',
        (['in'], POINTER(comtypes.IUnknown), 'pUnkServer'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Invoke',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), '_prpcmsg'),
        (['in'], POINTER(IRpcChannelBuffer), '_pRpcChannelBuffer'),
    ),
    COMMETHOD(
        [],
        IRpcStubBuffer,
        'IsIIDSupported',
        (['in'], REFIID, 'riid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DebugServerQueryInterface',
        (['out'], POINTER(POINTER(VOID)), 'ppv'),
    ),
    COMMETHOD(
        [],
        VOID,
        'DebugServerRelease',
        (['in'], POINTER(VOID), 'pv'),
    ),
]


IPSFactoryBuffer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateProxy',
        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(IRpcProxyBuffer)), 'ppProxy'),
        (['out'], POINTER(POINTER(VOID)), 'ppv'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateStub',
        (['in'], REFIID, 'riid'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnkServer'),
        (['out'], POINTER(POINTER(IRpcStubBuffer)), 'ppStub'),
    ),
]


class SChannelHookCallInfo(ctypes.Structure):
    _fields_ = [
        ('iid', IID),
        ('cbSize', DWORD),
        ('uCausality', GUID),
        ('dwServerPid', DWORD),
        ('iMethod', DWORD),
        ('pObject', POINTER(VOID)),
    ]


IChannelHook._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'ClientGetSize',
        (['in'], REFGUID, 'uExtent'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(ULONG), 'pDataSize'),
    ),
    COMMETHOD(
        [],
        VOID,
        'ClientFillBuffer',
        (['in'], REFGUID, 'uExtent'),
        (['in'], REFIID, 'riid'),
        (['in', 'out'], POINTER(ULONG), 'pDataSize'),
        (['in'], POINTER(VOID), 'pDataBuffer'),
    ),
    COMMETHOD(
        [],
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
        [],
        VOID,
        'ServerNotify',
        (['in'], REFGUID, 'uExtent'),
        (['in'], REFIID, 'riid'),
        (['in'], ULONG, 'cbDataSize'),
        (['in'], POINTER(VOID), 'pDataBuffer'),
        (['in'], DWORD, 'lDataRep'),
    ),
    COMMETHOD(
        [],
        VOID,
        'ServerGetSize',
        (['in'], REFGUID, 'uExtent'),
        (['in'], REFIID, 'riid'),
        (['in'], HRESULT, 'hrFault'),
        (['out'], POINTER(ULONG), 'pDataSize'),
    ),
    COMMETHOD(
        [],
        VOID,
        'ServerFillBuffer',
        (['in'], REFGUID, 'uExtent'),
        (['in'], REFIID, 'riid'),
        (['in', 'out'], POINTER(ULONG), 'pDataSize'),
        (['in'], POINTER(VOID), 'pDataBuffer'),
        (['in'], HRESULT, 'hrFault'),
    ),
]


class tagSOLE_AUTHENTICATION_SERVICE(ctypes.Structure):
    _fields_ = [
        ('dwAuthnSvc', DWORD),
        ('dwAuthzSvc', DWORD),
        ('pPrincipalName', POINTER(OLECHAR)),
        ('hr', HRESULT),
    ]


SOLE_AUTHENTICATION_SERVICE = tagSOLE_AUTHENTICATION_SERVICE
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


COLE_DEFAULT_PRINCIPAL = -1
COLE_DEFAULT_AUTHINFO = -1


class tagSOLE_AUTHENTICATION_INFO(ctypes.Structure):
    _fields_ = [
        ('dwAuthnSvc', DWORD),
        ('dwAuthzSvc', DWORD),
        ('pAuthInfo', POINTER(VOID)),
    ]


SOLE_AUTHENTICATION_INFO = tagSOLE_AUTHENTICATION_INFO
PSOLE_AUTHENTICATION_INFO = POINTER(tagSOLE_AUTHENTICATION_INFO)


class tagSOLE_AUTHENTICATION_LIST(ctypes.Structure):
    _fields_ = [
        ('cAuthInfo', DWORD),
        ('aAuthInfo', POINTER(SOLE_AUTHENTICATION_INFO)),
    ]


SOLE_AUTHENTICATION_LIST = tagSOLE_AUTHENTICATION_LIST
PSOLE_AUTHENTICATION_LIST = POINTER(tagSOLE_AUTHENTICATION_LIST)


IClientSecurity._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryBlanket',
        (['in'], POINTER(comtypes.IUnknown), 'pProxy'),
        (['out'], POINTER(DWORD), 'pAuthnSvc'),
        (['out'], POINTER(DWORD), 'pAuthzSvc'),
        (['out'], POINTER(POINTER(OLECHAR)), 'pServerPrincName'),
        (['out'], POINTER(DWORD), 'pAuthnLevel'),
        (['out'], POINTER(DWORD), 'pImpLevel'),
        (['out'], POINTER(POINTER(VOID)), 'pAuthInfo'),
        (['out'], POINTER(DWORD), 'pCapabilites'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBlanket',
        (['in'], POINTER(comtypes.IUnknown), 'pProxy'),
        (['in'], DWORD, 'dwAuthnSvc'),
        (['in'], DWORD, 'dwAuthzSvc'),
        (['in'], POINTER(OLECHAR), 'pServerPrincName'),
        (['in'], DWORD, 'dwAuthnLevel'),
        (['in'], DWORD, 'dwImpLevel'),
        (['in'], POINTER(VOID), 'pAuthInfo'),
        (['in'], DWORD, 'dwCapabilities'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CopyProxy',
        (['in'], POINTER(comtypes.IUnknown), 'pProxy'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppCopy'),
    ),
]


IServerSecurity._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'QueryBlanket',
        (['out'], POINTER(DWORD), 'pAuthnSvc'),
        (['out'], POINTER(DWORD), 'pAuthzSvc'),
        (['out'], POINTER(POINTER(OLECHAR)), 'pServerPrincName'),
        (['out'], POINTER(DWORD), 'pAuthnLevel'),
        (['out'], POINTER(DWORD), 'pImpLevel'),
        (['out'], POINTER(POINTER(VOID)), 'pPrivs'),
        (['in', 'out'], POINTER(DWORD), 'pCapabilities'),
    ),
    COMMETHOD(
        [],
        BOOL,
        'IsImpersonating'
    ),
]


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


IRpcOptions._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Set',
        (['in'], POINTER(comtypes.IUnknown), 'pPrx'),
        (['in'], RPCOPT_PROPERTIES, 'dwProperty'),
        (['in'], ULONG_PTR, 'dwValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Query',
        (['in'], POINTER(comtypes.IUnknown), 'pPrx'),
        (['in'], RPCOPT_PROPERTIES, 'dwProperty'),
        (['out'], POINTER(ULONG_PTR), 'pdwValue'),
    ),
]


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
    COMGLB_EXCEPTION_DONOT_HANDLE = COMGLB_EXCEPTION_DONOT_HANDLE_FATAL
    COMGLB_EXCEPTION_DONOT_HANDLE_ANY = 2


GLOBALOPT_EH_VALUES = tagGLOBALOPT_EH_VALUES


class tagGLOBALOPT_RPCTP_VALUES(ENUM):
    COMGLB_RPC_THREADPOOL_SETTING_DEFAULT_POOL = 0
    COMGLB_RPC_THREADPOOL_SETTING_PRIVATE_POOL = 1


GLOBALOPT_RPCTP_VALUES = tagGLOBALOPT_RPCTP_VALUES


class tagGLOBALOPT_RO_FLAGS(ENUM):
    COMGLB_STA_MODALLOOP_REMOVE_TOUCH_MESSAGES = 0x1
    COMGLB_STA_MODALLOOP_SHARED_QUEUE_REMOVE_INPUT_MESSAGES = 0x2
    COMGLB_STA_MODALLOOP_SHARED_QUEUE_DONOT_REMOVE_INPUT_MESSAGES = 0x4
    COMGLB_FAST_RUNDOWN = 0x8
    COMGLB_RESERVED1 = 0x10
    COMGLB_RESERVED2 = 0x20
    COMGLB_RESERVED3 = 0x40
    COMGLB_STA_MODALLOOP_SHARED_QUEUE_REORDER_POINTER_MESSAGES = 0x80
    COMGLB_RESERVED4 = 0x100
    COMGLB_RESERVED5 = 0x200
    COMGLB_RESERVED6 = 0x400


GLOBALOPT_RO_FLAGS = tagGLOBALOPT_RO_FLAGS


class tagGLOBALOPT_UNMARSHALING_POLICY_VALUES(ENUM):
    COMGLB_UNMARSHALING_POLICY_NORMAL = 0
    COMGLB_UNMARSHALING_POLICY_STRONG = 1
    COMGLB_UNMARSHALING_POLICY_HYBRID = 2


GLOBALOPT_UNMARSHALING_POLICY_VALUES = tagGLOBALOPT_UNMARSHALING_POLICY_VALUES


IGlobalOptions._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Set',
        (['in'], GLOBALOPT_PROPERTIES, 'dwProperty'),
        (['in'], ULONG_PTR, 'dwValue'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Query',
        (['in'], GLOBALOPT_PROPERTIES, 'dwProperty'),
        (['out'], POINTER(ULONG_PTR), 'pdwValue'),
    ),
]


LPSURROGATE = POINTER(ISurrogate)
ISurrogate._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'LoadDllServer',
        (['in'], REFCLSID, 'Clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FreeSurrogate'
    ),
]


LPGLOBALINTERFACETABLE = POINTER(IGlobalInterfaceTable)
IGlobalInterfaceTable._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RegisterInterfaceInGlobal',
        (['in'], POINTER(comtypes.IUnknown), 'pUnk'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RevokeInterfaceFromGlobal',
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetInterfaceFromGlobal',
        (['in'], DWORD, 'dwCookie'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppv'),
    ),
]


ISynchronize._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Wait',
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD, 'dwMilliseconds'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Reset'
    ),
]


ISynchronizeHandle._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetHandle',
        (['out'], POINTER(HANDLE), 'ph'),
    ),
]


ISynchronizeEvent._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetEventHandle',
        (['in'], POINTER(HANDLE), 'ph'),
    ),
]


ISynchronizeContainer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AddSynchronize',
        (['in'], POINTER(ISynchronize), 'pSync'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'WaitMultiple',
        (['in'], DWORD, 'dwFlags'),
        (['in'], DWORD, 'dwTimeOut'),
        (['out'], POINTER(POINTER(ISynchronize)), 'ppSync'),
    ),
]


ISynchronizeMutex._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseMutex'
    ),
]


LPCANCELMETHODCALLS = POINTER(ICancelMethodCalls)
ICancelMethodCalls._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Cancel',
        (['in'], ULONG, 'ulSeconds'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'TestCancel'
    ),
]


class tagDCOM_CALL_STATE(ENUM):
    DCOM_NONE = 0
    DCOM_CALL_COMPLETE = 0x1
    DCOM_CALL_CANCELED = 0x2


DCOM_CALL_STATE = tagDCOM_CALL_STATE


IAsyncManager._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CompleteCall',
        (['in'], HRESULT, 'Result'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCallContext',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'pInterface'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetState',
        (['out'], POINTER(ULONG), 'pulStateFlags'),
    ),
]


ICallFactory._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateCall',
        (['in'], REFIID, 'riid'),
        (['in'], POINTER(comtypes.IUnknown), 'pCtrlUnk'),
        (['in'], REFIID, 'riid2'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppv'),
    ),
]


IRpcHelper._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetDCOMProtocolVersion',
        (['out'], POINTER(DWORD), 'pComVersion'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetIIDFromOBJREF',
        (['in'], POINTER(VOID), 'pObjRef'),
        (['out'], POINTER(POINTER(IID)), 'piid'),
    ),
]


IReleaseMarshalBuffers._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ReleaseMarshalBuffer',
        (['in', 'out'], POINTER(RPCOLEMESSAGE), 'pMsg'),
        (['in'], DWORD, 'dwFlags'),
        (['in'], POINTER(comtypes.IUnknown), 'pChnl'),
    ),
]


IWaitMultiple._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'WaitMultiple',
        (['in'], DWORD, 'timeout'),
        (['out'], POINTER(POINTER(ISynchronize)), 'pSync'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'AddSynchronize',
        (['in'], POINTER(ISynchronize), 'pSync'),
    ),
]


LPADDRTRACKINGCONTROL = POINTER(IAddrTrackingControl)
IAddrTrackingControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'DisableCOMDynamicAddrTracking'
    ),
]


LPADDREXCLUSIONCONTROL = POINTER(IAddrExclusionControl)


IAddrExclusionControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentAddrExclusionList',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppEnumerator'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UpdateAddrExclusionList',
        (['in'], POINTER(comtypes.IUnknown), 'pEnumerator'),
    ),
]


IPipeByte._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Pull',
        ([], POINTER(BYTE), 'buf'),
        (['in'], ULONG, 'cRequest'),
        (['out'], POINTER(ULONG), 'pcReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Push',
        (['in'], POINTER(BYTE), 'buf'),
        (['in'], ULONG, 'cSent'),
    ),
]


AsyncIPipeByte._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Begin_Pull',
        (['in'], ULONG, 'cRequest'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_Pull',
        ([], POINTER(BYTE), 'buf'),
        (['out'], POINTER(ULONG), 'pcReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Begin_Push',
        (['in'], POINTER(BYTE), 'buf'),
        (['in'], ULONG, 'cSent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_Push'
    ),
]


IPipeLong._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Pull',
        ([], POINTER(LONG), 'buf'),
        (['in'], ULONG, 'cRequest'),
        (['out'], POINTER(ULONG), 'pcReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Push',
        (['in'], POINTER(LONG), 'buf'),
        (['in'], ULONG, 'cSent'),
    ),
]


AsyncIPipeLong._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Begin_Pull',
        (['in'], ULONG, 'cRequest'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_Pull',
        ([], POINTER(LONG), 'buf'),
        (['out'], POINTER(ULONG), 'pcReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Begin_Push',
        (['in'], POINTER(LONG), 'buf'),
        (['in'], ULONG, 'cSent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_Push'
    ),
]


IPipeDouble._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Pull',
        ([], POINTER(DOUBLE), 'buf'),
        (['in'], ULONG, 'cRequest'),
        (['out'], POINTER(ULONG), 'pcReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Push',
        (['in'], POINTER(DOUBLE), 'buf'),
        (['in'], ULONG, 'cSent'),
    ),
]


AsyncIPipeDouble._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Begin_Pull',
        (['in'], ULONG, 'cRequest'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_Pull',
        ([], POINTER(DOUBLE), 'buf'),
        (['out'], POINTER(ULONG), 'pcReturned'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Begin_Push',
        (['in'], POINTER(DOUBLE), 'buf'),
        (['in'], ULONG, 'cSent'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Finish_Push'
    ),
]


CPFLAGS = DWORD


class tagContextProperty(ctypes.Structure):
    _fields_ = [
        ('policyId', GUID),
        ('flags', CPFLAGS),
        ('pUnk', POINTER(comtypes.IUnknown)),
    ]


ContextProperty = tagContextProperty


LPENUMCONTEXTPROPS = POINTER(IEnumContextProps)
IEnumContextProps._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(ContextProperty), 'pContextProperties'),
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
        (['out'], POINTER(POINTER(IEnumContextProps)), 'ppEnumContextProps'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Count',
        (['out'], POINTER(ULONG), 'pcelt'),
    ),
]


IContext._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SetProperty',
        (['in'], REFGUID, 'rpolicyId'),
        (['in'], CPFLAGS, 'flags'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RemoveProperty',
        (['in'], REFGUID, 'rPolicyId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetProperty',
        (['in'], REFGUID, 'rGuid'),
        (['out'], POINTER(CPFLAGS), 'pFlags'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppUnk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumContextProps',
        (['out'], POINTER(POINTER(IEnumContextProps)), 'ppEnumContextProps'),
    ),
]


IObjContext._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'Reserved7'
    ),
]


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


class _THDTYPE(ENUM):
    THDTYPE_BLOCKMESSAGES = 0
    THDTYPE_PROCESSMESSAGES = 1


THDTYPE = _THDTYPE
APARTMENTID = DWORD


IComThreadingInfo._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentApartmentType',
        (['out'], POINTER(APTTYPE), 'pAptType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentThreadType',
        (['out'], POINTER(THDTYPE), 'pThreadType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurrentLogicalThreadId',
        (['out'], POINTER(GUID), 'pguidLogicalThreadId'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetCurrentLogicalThreadId',
        (['in'], REFGUID, 'rguid'),
    ),
]


IProcessInitControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ResetInitializerTimeout',
        (['in'], DWORD, 'dwSecondsRemaining'),
    ),
]


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


IMarshalingStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetMarshalingContextAttribute',
        (['in'], CO_MARSHALING_CONTEXT_ATTRIBUTES, 'attribute'),
        (['out'], POINTER(ULONG_PTR), 'pAttributeValue'),
    ),
]


IAgileReference._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Resolve',
        (['in'], REFIID, 'riid'),
        (['out', 'retval'], POINTER(POINTER(VOID)), 'ppvObjectReference'),
    ),
]


IAgileReference._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Resolve',
        (['in'], REFIID, 'riid'),
        (['out', 'retval'], POINTER(POINTER(VOID)), 'ppvObjectReference'),
    ),
]


LPMALLOCSPY = POINTER(IMallocSpy)


IMallocSpy._methods_ = [
    COMMETHOD(
        [],
        SIZE_T,
        'PreAlloc',
        (['in'], SIZE_T, 'cbRequest'),
    ),
    COMMETHOD(
        [],
        VOID,
        'PostAlloc',
        (['in'], POINTER(VOID), 'pActual'),
    ),
    COMMETHOD(
        [],
        VOID,
        'PreFree',
        (['in'], POINTER(VOID), 'pRequest'),
        (['in'], BOOL, 'fSpyed'),
    ),
    COMMETHOD(
        [],
        VOID,
        'PostFree',
        (['in'], BOOL, 'fSpyed'),
    ),
    COMMETHOD(
        [],
        SIZE_T,
        'PreRealloc',
        (['in'], POINTER(VOID), 'pRequest'),
        (['in'], SIZE_T, 'cbRequest'),
        (['out'], POINTER(POINTER(VOID)), 'ppNewRequest'),
        (['in'], BOOL, 'fSpyed'),
    ),
    COMMETHOD(
        [],
        VOID,
        'PostRealloc',
        (['in'], POINTER(VOID), 'pActual'),
        (['in'], BOOL, 'fSpyed'),
    ),
    COMMETHOD(
        [],
        VOID,
        'PreGetSize',
        (['in'], POINTER(VOID), 'pRequest'),
        (['in'], BOOL, 'fSpyed'),
    ),
    COMMETHOD(
        [],
        SIZE_T,
        'PostGetSize',
        (['in'], SIZE_T, 'cbActual'),
        (['in'], BOOL, 'fSpyed'),
    ),
    COMMETHOD(
        [],
        VOID,
        'PreDidAlloc',
        (['in'], POINTER(VOID), 'pRequest'),
        (['in'], BOOL, 'fSpyed'),
    ),
    COMMETHOD(
        [],
        INT,
        'PostDidAlloc',
        (['in'], POINTER(VOID), 'pRequest'),
        (['in'], BOOL, 'fSpyed'),
        (['in'], INT, 'fActual'),
    ),
    COMMETHOD(
        [],
        VOID,
        'PostHeapMinimize'
    ),
]


LPBC = POINTER(IBindCtx)
LPBINDCTX = POINTER(IBindCtx)


class tagBIND_OPTS(ctypes.Structure):
    _fields_ = [
        ('cbStruct', DWORD),
        ('grfFlags', DWORD),
        ('grfMode', DWORD),
        ('dwTickCountDeadline', DWORD),
    ]


BIND_OPTS = tagBIND_OPTS
LPBIND_OPTS = POINTER(tagBIND_OPTS)


class tagBIND_OPTS2(ctypes.Structure):
    _fields_ = [
        ('cbStruct', DWORD),
        ('grfFlags', DWORD),
        ('grfMode', DWORD),
        ('dwTickCountDeadline', DWORD),
        ('dwTrackFlags', DWORD),
        ('dwClassContext', DWORD),
        ('locale', LCID),
        ('pServerInfo', POINTER(COSERVERINFO)),
    ]


BIND_OPTS2 = tagBIND_OPTS2
LPBIND_OPTS2 = POINTER(tagBIND_OPTS2)


class tagBIND_OPTS3(ctypes.Structure):
    _fields_ = [
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


BIND_OPTS3 = tagBIND_OPTS3
LPBIND_OPTS3 = POINTER(tagBIND_OPTS3)


class tagBIND_FLAGS(ENUM):
    BIND_MAYBOTHERUSER = 1
    BIND_JUSTTESTEXISTENCE = 2


BIND_FLAGS = tagBIND_FLAGS


IBindCtx._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'RegisterObjectBound',
        (['in'], POINTER(comtypes.IUnknown), 'punk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RevokeObjectBound',
        (['in'], POINTER(comtypes.IUnknown), 'punk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetBindOptions',
        (['in'], POINTER(BIND_OPTS), 'pbindopts'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetBindOptions',
        (['in', 'out'], POINTER(BIND_OPTS), 'pbindopts'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetRunningObjectTable',
        (['out'], POINTER(POINTER(IRunningObjectTable)), 'pprot'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RegisterObjectParam',
        (['in'], LPOLESTR, 'pszKey'),
        (['in'], POINTER(comtypes.IUnknown), 'punk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetObjectParam',
        (['in'], LPOLESTR, 'pszKey'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppunk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumObjectParam',
        (['out'], POINTER(POINTER(IEnumString)), 'ppenum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RevokeObjectParam',
        (['in'], LPOLESTR, 'pszKey'),
    ),
]


LPENUMMONIKER = POINTER(IEnumMoniker)


IEnumMoniker._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(POINTER(IMoniker)), 'rgelt'),
        ([], POINTER(ULONG), 'pceltFetched'),
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
        (['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum'),
    ),
]


LPRUNNABLEOBJECT = POINTER(IRunnableObject)


IRunnableObject._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetRunningClass',
        (['out'], LPCLSID, 'lpClsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Run',
        (['in'], LPBINDCTX, 'pbc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LockRunning',
        (['in'], BOOL, 'fLock'),
        (['in'], BOOL, 'fLastUnlockCloses'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetContainedObject',
        (['in'], BOOL, 'fContained'),
    ),
]


LPRUNNINGOBJECTTABLE = POINTER(IRunningObjectTable)


IRunningObjectTable._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Register',
        (['in'], DWORD, 'grfFlags'),
        (['in'], POINTER(comtypes.IUnknown), 'punkObject'),
        (['in'], POINTER(IMoniker), 'pmkObjectName'),
        (['out'], POINTER(DWORD), 'pdwRegister'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Revoke',
        (['in'], DWORD, 'dwRegister'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsRunning',
        (['in'], POINTER(IMoniker), 'pmkObjectName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetObject',
        (['in'], POINTER(IMoniker), 'pmkObjectName'),
        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppunkObject'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'NoteChangeTime',
        (['in'], DWORD, 'dwRegister'),
        (['in'], POINTER(FILETIME), 'pfiletime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTimeOfLastChange',
        (['in'], POINTER(IMoniker), 'pmkObjectName'),
        (['out'], POINTER(FILETIME), 'pfiletime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumRunning',
        (['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker'),
    ),
]


LPPERSIST = POINTER(IPersist)


IPersist._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetClassID',
        (['out'], POINTER(CLSID), 'pClassID'),
    ),
]


LPPERSISTSTREAM = POINTER(IPersistStream)


IPersistStream._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], POINTER(IStream), 'pStm'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], POINTER(IStream), 'pStm'),
        (['in'], BOOL, 'fClearDirty'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetSizeMax',
        (['out'], POINTER(ULARGE_INTEGER), 'pcbSize'),
    ),
]


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


IMoniker._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'BindToObject',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], POINTER(IMoniker), 'pmkToLeft'),
        (['in'], REFIID, 'riidResult'),
        (['out'], POINTER(POINTER(VOID)), 'ppvResult'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'BindToStorage',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], POINTER(IMoniker), 'pmkToLeft'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObj'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Reduce',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], DWORD, 'dwReduceHowFar'),
        (['in', 'out'], POINTER(POINTER(IMoniker)), 'ppmkToLeft'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmkReduced'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ComposeWith',
        (['in'], POINTER(IMoniker), 'pmkRight'),
        (['in'], BOOL, 'fOnlyIfNotGeneric'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmkComposite'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Enum',
        (['in'], BOOL, 'fForward'),
        (['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsEqual',
        (['in'], POINTER(IMoniker), 'pmkOtherMoniker'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Hash',
        (['out'], POINTER(DWORD), 'pdwHash'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsRunning',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], POINTER(IMoniker), 'pmkToLeft'),
        (['in'], POINTER(IMoniker), 'pmkNewlyRunning'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetTimeOfLastChange',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], POINTER(IMoniker), 'pmkToLeft'),
        (['out'], POINTER(FILETIME), 'pFileTime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Inverse',
        (['out'], POINTER(POINTER(IMoniker)), 'ppmk'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CommonPrefixWith',
        (['in'], POINTER(IMoniker), 'pmkOther'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmkPrefix'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RelativePathTo',
        (['in'], POINTER(IMoniker), 'pmkOther'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmkRelPath'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDisplayName',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], POINTER(IMoniker), 'pmkToLeft'),
        (['out'], POINTER(LPOLESTR), 'ppszDisplayName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ParseDisplayName',
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], POINTER(IMoniker), 'pmkToLeft'),
        (['in'], LPOLESTR, 'pszDisplayName'),
        (['out'], POINTER(ULONG), 'pchEaten'),
        (['out'], POINTER(POINTER(IMoniker)), 'ppmkOut'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'IsSystemMoniker',
        (['out'], POINTER(DWORD), 'pdwMksys'),
    ),
]


IROTData._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetComparisonData',
        (['out'], POINTER(BYTE), 'pbData'),
        (['in'], ULONG, 'cbMax'),
        (['out'], POINTER(ULONG), 'pcbData'),
    ),
]


LPENUMSTATSTG = POINTER(IEnumSTATSTG)


IEnumSTATSTG._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(STATSTG), 'rgelt'),
        ([], POINTER(ULONG), 'pceltFetched'),
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
        (['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum'),
    ),
]


LPSTORAGE = POINTER(IStorage)


class tagRemSNB(ctypes.Structure):
    _fields_ = [
        ('ulCntStr', ULONG),
        ('ulCntChar', ULONG),
        ('rgString', OLECHAR * 1),
    ]


RemSNB = tagRemSNB


wireSNB = POINTER(RemSNB)
SNB = POINTER(LPOLESTR)


IStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateStream',
        (['in'], POINTER(OLECHAR), 'pwcsName'),
        (['in'], DWORD, 'grfMode'),
        (['in'], DWORD, 'reserved1'),
        (['in'], DWORD, 'reserved2'),
        (['out'], POINTER(POINTER(IStream)), 'ppstm'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OpenStream',
        (['in'], POINTER(OLECHAR), 'pwcsName'),
        (['in'], POINTER(VOID), 'reserved1'),
        (['in'], DWORD, 'grfMode'),
        (['in'], DWORD, 'reserved2'),
        (['out'], POINTER(POINTER(IStream)), 'ppstm'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CreateStorage',
        (['in'], POINTER(OLECHAR), 'pwcsName'),
        (['in'], DWORD, 'grfMode'),
        (['in'], DWORD, 'reserved1'),
        (['in'], DWORD, 'reserved2'),
        (['out'], POINTER(POINTER(IStorage)), 'ppstg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OpenStorage',
        (['in'], POINTER(OLECHAR), 'pwcsName'),
        (['in'], POINTER(IStorage), 'pstgPriority'),
        (['in'], DWORD, 'grfMode'),
        (['in'], SNB, 'snbExclude'),
        (['in'], DWORD, 'reserved'),
        (['out'], POINTER(POINTER(IStorage)), 'ppstg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CopyTo',
        (['in'], DWORD, 'ciidExclude'),
        (['in'], POINTER(IID), 'rgiidExclude'),
        (['in'], SNB, 'snbExclude'),
        (['in'], POINTER(IStorage), 'pstgDest'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'MoveElementTo',
        (['in'], POINTER(OLECHAR), 'pwcsName'),
        (['in'], POINTER(IStorage), 'pstgDest'),
        (['in'], POINTER(OLECHAR), 'pwcsNewName'),
        (['in'], DWORD, 'grfFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Commit',
        (['in'], DWORD, 'grfCommitFlags'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumElements',
        (['in'], DWORD, 'reserved1'),
        (['in'], POINTER(VOID), 'reserved2'),
        (['in'], DWORD, 'reserved3'),
        (['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DestroyElement',
        (['in'], POINTER(OLECHAR), 'pwcsName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'RenameElement',
        (['in'], POINTER(OLECHAR), 'pwcsOldName'),
        (['in'], POINTER(OLECHAR), 'pwcsNewName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetElementTimes',
        (['in'], POINTER(OLECHAR), 'pwcsName'),
        (['in'], POINTER(FILETIME), 'pctime'),
        (['in'], POINTER(FILETIME), 'patime'),
        (['in'], POINTER(FILETIME), 'pmtime'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetClass',
        (['in'], REFCLSID, 'clsid'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetStateBits',
        (['in'], DWORD, 'grfStateBits'),
        (['in'], DWORD, 'grfMask'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Stat',
        (['out'], POINTER(STATSTG), 'pstatstg'),
        (['in'], DWORD, 'grfStatFlag'),
    ),
]


LPPERSISTFILE = POINTER(IPersistFile)


IPersistFile._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], LPCOLESTR, 'pszFileName'),
        (['in'], DWORD, 'dwMode'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], LPCOLESTR, 'pszFileName'),
        (['in'], BOOL, 'fRemember'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SaveCompleted',
        (['in'], LPCOLESTR, 'pszFileName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCurFile',
        (['out'], POINTER(LPOLESTR), 'ppszFileName'),
    ),
]


LPPERSISTSTORAGE = POINTER(IPersistStorage)


IPersistStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'InitNew',
        (['in'], POINTER(IStorage), 'pStg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Load',
        (['in'], POINTER(IStorage), 'pStg'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Save',
        (['in'], POINTER(IStorage), 'pStgSave'),
        (['in'], BOOL, 'fSameAsLoad'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SaveCompleted',
        (['in'], POINTER(IStorage), 'pStgNew'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HandsOffStorage'
    ),
]


LPLOCKBYTES = POINTER(ILockBytes)


ILockBytes._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'ReadAt',
        (['in'], ULARGE_INTEGER, 'ulOffset'),
        ([], POINTER(VOID), 'pv'),
        (['in'], ULONG, 'cb'),
        (['out'], POINTER(ULONG), 'pcbRead'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'WriteAt',
        (['in'], ULARGE_INTEGER, 'ulOffset'),
        (['in'], POINTER(VOID), 'pv'),
        (['in'], ULONG, 'cb'),
        (['out'], POINTER(ULONG), 'pcbWritten'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetSize',
        (['in'], ULARGE_INTEGER, 'cb'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'LockRegion',
        (['in'], ULARGE_INTEGER, 'libOffset'),
        (['in'], ULARGE_INTEGER, 'cb'),
        (['in'], DWORD, 'dwLockType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'UnlockRegion',
        (['in'], ULARGE_INTEGER, 'libOffset'),
        (['in'], ULARGE_INTEGER, 'cb'),
        (['in'], DWORD, 'dwLockType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Stat',
        (['out'], POINTER(STATSTG), 'pstatstg'),
        (['in'], DWORD, 'grfStatFlag'),
    ),
]


LPENUMFORMATETC = POINTER(IEnumFORMATETC)


IEnumFORMATETC._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(FORMATETC), 'rgelt'),
        ([], POINTER(ULONG), 'pceltFetched'),
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
        (['out'], POINTER(POINTER(IEnumFORMATETC)), 'ppenum'),
    ),
]


class tagADVF(ENUM):
    ADVF_NODATA = 1
    ADVF_PRIMEFIRST = 2
    ADVF_ONLYONCE = 4
    ADVF_DATAONSTOP = 64
    ADVFCACHE_NOHANDLER = 8
    ADVFCACHE_FORCEBUILTIN = 16
    ADVFCACHE_ONSAVE = 32


ADVF = tagADVF


class tagSTATDATA(ctypes.Structure):
    _fields_ = [
        ('formatetc', FORMATETC),
        ('advf', DWORD),
        ('pAdvSink', POINTER(IAdviseSink)),
        ('dwConnection', DWORD),
    ]


STATDATA = tagSTATDATA


IEnumSTATDATA._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Next',
        (['in'], ULONG, 'celt'),
        ([], POINTER(STATDATA), 'rgelt'),
        ([], POINTER(ULONG), 'pceltFetched'),
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
        (['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenum'),
    ),
]


LPROOTSTORAGE = POINTER(IRootStorage)


IRootStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SwitchToFile',
        (['in'], LPOLESTR, 'pszFile'),
    ),
]


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


class tagRemSTGMEDIUM(ctypes.Structure):
    _fields_ = [
        ('tymed', DWORD),
        ('dwHandleType', DWORD),
        ('pData', ULONG),
        ('pUnkForRelease', ULONG),
        ('cbData', ULONG),
        ('data', BYTE * 1),
    ]


RemSTGMEDIUM = tagRemSTGMEDIUM





class _GDI_OBJECT(ctypes.Structure):

    class __MIDL_IAdviseSink_0002(ctypes.Union):
        _fields_ = [
            ('hBitmap', wireHBITMAP),
            ('hPalette', wireHPALETTE),
            ('hGeneric', wireHGLOBAL),
        ]

    _fields_ = [
        ('ObjectType', DWORD),
        ('u', __MIDL_IAdviseSink_0002),
    ]


GDI_OBJECT = _GDI_OBJECT


class _userSTGMEDIUM(ctypes.Structure):

    class _STGMEDIUM_UNION(ctypes.Structure):

        class __MIDL_IAdviseSink_0003(ctypes.Union):
            _fields_ = [
                ('hMetaFilePict', wireHMETAFILEPICT),
                ('hHEnhMetaFile', wireHENHMETAFILE),
                ('hGdiHandle', POINTER(GDI_OBJECT)),
                ('hGlobal', wireHGLOBAL),
                ('lpszFileName', LPOLESTR),
                ('pstm', POINTER(BYTE_BLOB)),
                ('pstg', POINTER(BYTE_BLOB)),
            ]

        _fields_ = [
            ('tymed', DWORD),
            ('u', __MIDL_IAdviseSink_0003),
        ]

    _fields_ = [
        ('DUMMYUNIONNAME', _STGMEDIUM_UNION),
        ('pUnkForRelease', POINTER(comtypes.IUnknown)),
    ]


userSTGMEDIUM = _userSTGMEDIUM
wireSTGMEDIUM = POINTER(userSTGMEDIUM)
wireASYNC_STGMEDIUM = POINTER(userSTGMEDIUM)
ASYNC_STGMEDIUM = STGMEDIUM
LPSTGMEDIUM = POINTER(STGMEDIUM)


class _userFLAG_STGMEDIUM(ctypes.Structure):
    _fields_ = [
        ('ContextFlags', LONG),
        ('fPassOwnership', LONG),
        ('Stgmed', userSTGMEDIUM),
    ]


userFLAG_STGMEDIUM = _userFLAG_STGMEDIUM
wireFLAG_STGMEDIUM = POINTER(userFLAG_STGMEDIUM)


class _FLAG_STGMEDIUM(ctypes.Structure):
    _fields_ = [
        ('ContextFlags', LONG),
        ('fPassOwnership', LONG),
        ('Stgmed', STGMEDIUM),
    ]


FLAG_STGMEDIUM = _FLAG_STGMEDIUM


IAdviseSink._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'OnDataChange',
        (['in'], POINTER(FORMATETC), 'pFormatetc'),
        (['in'], POINTER(STGMEDIUM), 'pStgmed'),
    ),
    COMMETHOD(
        [],
        VOID,
        'OnViewChange',
        (['in'], DWORD, 'dwAspect'),
        (['in'], LONG, 'lindex'),
    ),
    COMMETHOD(
        [],
        VOID,
        'OnRename',
        (['in'], POINTER(IMoniker), 'pmk'),
    ),
    COMMETHOD(
        [],
        VOID,
        'OnClose'
    ),
]


AsyncIAdviseSink._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'Begin_OnDataChange',
        (['in'], POINTER(FORMATETC), 'pFormatetc'),
        (['in'], POINTER(STGMEDIUM), 'pStgmed'),
    ),
    COMMETHOD(
        [],
        VOID,
        'Begin_OnViewChange',
        (['in'], DWORD, 'dwAspect'),
        (['in'], LONG, 'lindex'),
    ),
    COMMETHOD(
        [],
        VOID,
        'Begin_OnRename',
        (['in'], POINTER(IMoniker), 'pmk'),
    ),
    COMMETHOD(
        [],
        VOID,
        'Finish_OnClose'
    ),
]


LPADVISESINK2 = POINTER(IAdviseSink2)
IAdviseSink2._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'OnLinkSrcChange',
        (['in'], POINTER(IMoniker), 'pmk'),
    ),
]


AsyncIAdviseSink2._methods_ = [
    COMMETHOD(
        [],
        VOID,
        'Begin_OnLinkSrcChange',
        (['in'], POINTER(IMoniker), 'pmk'),
    ),
    COMMETHOD(
        [],
        VOID,
        'Finish_OnLinkSrcChange'
    ),
]


class tagDATADIR(ENUM):
    DATADIR_GET = 1
    DATADIR_SET = 2


DATADIR = tagDATADIR


IDataObject._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetData',
        (['in'], POINTER(FORMATETC), 'pformatetcIn'),
        (['out'], POINTER(STGMEDIUM), 'pmedium'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDataHere',
        (['in'], POINTER(FORMATETC), 'pformatetc'),
        (['in', 'out'], POINTER(STGMEDIUM), 'pmedium'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'QueryGetData',
        (['in'], POINTER(FORMATETC), 'pformatetc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetCanonicalFormatEtc',
        (['in'], POINTER(FORMATETC), 'pformatectIn'),
        (['out'], POINTER(FORMATETC), 'pformatetcOut'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetData',
        (['in'], POINTER(FORMATETC), 'pformatetc'),
        (['in'], POINTER(STGMEDIUM), 'pmedium'),
        (['in'], BOOL, 'fRelease'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumFormatEtc',
        (['in'], DWORD, 'dwDirection'),
        (['out'], POINTER(POINTER(IEnumFORMATETC)), 'ppenumFormatEtc'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DAdvise',
        (['in'], POINTER(FORMATETC), 'pformatetc'),
        (['in'], DWORD, 'advf'),
        (['in'], POINTER(IAdviseSink), 'pAdvSink'),
        (['out'], POINTER(DWORD), 'pdwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'DUnadvise',
        (['in'], DWORD, 'dwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumDAdvise',
        (['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenumAdvise'),
    ),
]


LPDATAADVISEHOLDER = POINTER(IDataAdviseHolder)


IDataAdviseHolder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Advise',
        (['in'], POINTER(IDataObject), 'pDataObject'),
        (['in'], POINTER(FORMATETC), 'pFetc'),
        (['in'], DWORD, 'advf'),
        (['in'], POINTER(IAdviseSink), 'pAdvise'),
        (['out'], POINTER(DWORD), 'pdwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unadvise',
        (['in'], DWORD, 'dwConnection'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'EnumAdvise',
        (['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenumAdvise'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SendOnDataChange',
        (['in'], POINTER(IDataObject), 'pDataObject'),
        (['in'], DWORD, 'dwReserved'),
        (['in'], DWORD, 'advf'),
    ),
]


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


class tagINTERFACEINFO(ctypes.Structure):
    _fields_ = [
        ('pUnk', POINTER(comtypes.IUnknown)),
        ('iid', IID),
        ('wMethod', WORD),
    ]


INTERFACEINFO = tagINTERFACEINFO


LPINTERFACEINFO = POINTER(tagINTERFACEINFO)
IMessageFilter._methods_ = [
    COMMETHOD(
        [],
        DWORD,
        'HandleInComingCall',
        (['in'], DWORD, 'dwCallType'),
        (['in'], HTASK, 'htaskCaller'),
        (['in'], DWORD, 'dwTickCount'),
        (['in'], LPINTERFACEINFO, 'lpInterfaceInfo'),
    ),
    COMMETHOD(
        [],
        DWORD,
        'RetryRejectedCall',
        (['in'], HTASK, 'htaskCallee'),
        (['in'], DWORD, 'dwTickCount'),
        (['in'], DWORD, 'dwRejectType'),
    ),
    COMMETHOD(
        [],
        DWORD,
        'MessagePending',
        (['in'], HTASK, 'htaskCallee'),
        (['in'], DWORD, 'dwTickCount'),
        (['in'], DWORD, 'dwPendingType'),
    ),
]


IClassActivator._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'GetClassObject',
        (['in'], REFCLSID, 'rclsid'),
        (['in'], DWORD, 'dwClassContext'),
        (['in'], LCID, 'locale'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppv'),
    ),
]


IFillLockBytes._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'FillAppend',
        (['in'], POINTER(VOID), 'pv'),
        (['in'], ULONG, 'cb'),
        (['out'], POINTER(ULONG), 'pcbWritten'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'FillAt',
        (['in'], ULARGE_INTEGER, 'ulOffset'),
        (['in'], POINTER(VOID), 'pv'),
        (['in'], ULONG, 'cb'),
        (['out'], POINTER(ULONG), 'pcbWritten'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetFillSize',
        (['in'], ULARGE_INTEGER, 'ulSize'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Terminate',
        (['in'], BOOL, 'bCanceled'),
    ),
]


IProgressNotify._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'OnProgress',
        (['in'], DWORD, 'dwProgressCurrent'),
        (['in'], DWORD, 'dwProgressMaximum'),
        (['in'], BOOL, 'fAccurate'),
        (['in'], BOOL, 'fOwner'),
    ),
]


class tagStorageLayout(ctypes.Structure):
    _fields_ = [
        ('LayoutType', DWORD),
        ('pwcsElementName', POINTER(OLECHAR)),
        ('cOffset', LARGE_INTEGER),
        ('cBytes', LARGE_INTEGER),
    ]


StorageLayout = tagStorageLayout


ILayoutStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'LayoutScript',
        (['in'], POINTER(StorageLayout), 'pStorageLayout'),
        (['in'], DWORD, 'nEntries'),
        (['in'], DWORD, 'glfInterleavedFlag'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReLayoutDocfile',
        (['in'], POINTER(OLECHAR), 'pwcsNewDfName'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ReLayoutDocfileOnILockBytes',
        (['in'], POINTER(ILockBytes), 'pILockBytes'),
    ),
]


IBlockingLock._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Lock',
        (['in'], DWORD, 'dwTimeout'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'Unlock'
    ),
]


ITimeAndNoticeControl._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'SuppressChanges',
        (['in'], DWORD, 'res1'),
        (['in'], DWORD, 'res2'),
    ),
]


IOplockStorage._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'CreateStorageEx',
        (['in'], LPCWSTR, 'pwcsName'),
        (['in'], DWORD, 'grfMode'),
        (['in'], DWORD, 'stgfmt'),
        (['in'], DWORD, 'grfAttrs'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppstgOpen'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'OpenStorageEx',
        (['in'], LPCWSTR, 'pwcsName'),
        (['in'], DWORD, 'grfMode'),
        (['in'], DWORD, 'stgfmt'),
        (['in'], DWORD, 'grfAttrs'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppstgOpen'),
    ),
]


IDirectWriterLock._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'WaitForWriteAccess',
        (['in'], DWORD, 'dwTimeout'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'HaveWriteAccess'
    ),
]


IUrlMon._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AsyncGetClassBits',
        (['in'], REFCLSID, 'rclsid'),
        (['in'], LPCWSTR, 'pszTYPE'),
        (['in'], LPCWSTR, 'pszExt'),
        (['in'], DWORD, 'dwFileVersionMS'),
        (['in'], DWORD, 'dwFileVersionLS'),
        (['in'], LPCWSTR, 'pszCodeBase'),
        (['in'], POINTER(IBindCtx), 'pbc'),
        (['in'], DWORD, 'dwClassContext'),
        (['in'], REFIID, 'riid'),
        (['in'], DWORD, 'flags'),
    ),
]


IForegroundTransfer._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'AllowForegroundTransfer',
        (['in'], POINTER(VOID), 'lpvReserved'),
    ),
]


IThumbnailExtractor._methods_ = [
    COMMETHOD(
        [],
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
        [],
        HRESULT,
        'OnFileUpdated',
        (['in'], POINTER(IStorage), 'pStg'),
    ),
]


IDummyHICONIncluder._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Dummy',
        (['in'], HICON, 'h1'),
        (['in'], HDC, 'h2'),
    ),
]


class tagApplicationType(ENUM):
    ServerApplication = 0
    LibraryApplication = ServerApplication + 1


ApplicationType = tagApplicationType


class tagShutdownType(ENUM):
    IdleShutdown = 0
    ForcedShutdown = IdleShutdown + 1


ShutdownType = tagShutdownType


IProcessLock._methods_ = [
    COMMETHOD(
        [],
        ULONG,
        'ReleaseRefOnProcess'
    ),
]


ISurrogateService._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'Init',
        (['in'], REFGUID, 'rguidProcessID'),
        (['in'], POINTER(IProcessLock), 'pProcessLock'),
        (['out'], POINTER(BOOL), 'pfApplicationAware'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ApplicationLaunch',
        (['in'], REFGUID, 'rguidApplID'),
        (['in'], ApplicationType, 'appType'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ApplicationFree',
        (['in'], REFGUID, 'rguidApplID'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'CatalogRefresh',
        (['in'], ULONG, 'ulReserved'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'ProcessShutdown',
        (['in'], ShutdownType, 'shutdownType'),
    ),
]


LPINITIALIZESPY = POINTER(IInitializeSpy)

IInitializeSpy._methods_ = [
    COMMETHOD(
        [],
        HRESULT,
        'PreInitialize',
        (['in'], DWORD, 'dwCoInit'),
        (['in'], DWORD, 'dwCurThreadAptRefs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PostInitialize',
        (['in'], HRESULT, 'hrCoInit'),
        (['in'], DWORD, 'dwCoInit'),
        (['in'], DWORD, 'dwNewThreadAptRefs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PreUninitialize',
        (['in'], DWORD, 'dwCurThreadAptRefs'),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'PostUninitialize',
        (['in'], DWORD, 'dwNewThreadAptRefs'),
    ),
]


IID_IApartmentShutdown = IID(
    '{A2F05A09-27A2-42B5-BC0E-AC163EF49D9B}'
)


class IApartmentShutdown(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IApartmentShutdown
    _idlflags_ = []
    _methods_ = [
        COMMETHOD(
            [],
            VOID,
            'OnUninitialize',
            (['in'], UINT64, 'ui64ApartmentIdentifier'),
        ),
    ]


__all__ = (
    'ILayoutStorage', 'IFastRundown', 'IExternalConnection', 'IMallocSpy',
    'IDataAdviseHolder', 'IProcessLock', 'ISurrogateService', 'IEnumString',
    'IClientSecurity', 'IRpcOptions', 'IAddrTrackingControl', 'IRootStorage',
    'IPersistStream', 'IContext', 'IReleaseMarshalBuffers', 'IMoniker', 'SNB',
    'IRpcChannelBuffer2', 'IChannelHook', 'IOplockStorage', 'IRpcProxyBuffer',
    'AsyncIAdviseSink', 'IStdMarshalInfo', 'IObjContext', 'IUrlMon', 'LPBC',
    'IEnumSTATSTG', 'AsyncIAdviseSink2', 'IInitializeSpy', 'IStream',
    'IRpcChannelBuffer', 'IPersist', 'ICancelMethodCalls', 'IFillLockBytes',
    'ISequentialStream', 'IGlobalInterfaceTable', 'IComThreadingInfo',
    'IMarshal', 'IRpcHelper', 'ISurrogate', 'IMultiQI', 'AsyncIMultiQI',
    'AsyncIPipeLong', 'IMessageFilter', 'IStorage', 'IBindCtx', 'IPipeLong',
    'IActivationFilter', 'IPersistFile', 'ISynchronize', 'IEnumUnknown',
    'IAgileReference', 'IMarshalingStream', 'ILockBytes', 'AsyncIPipeDouble',
    'ITimeAndNoticeControl', 'IEnumMoniker', 'IPipeDouble', 'IROTData',
    'IForegroundTransfer', 'IAsyncManager', 'IDirectWriterLock', 'INoMarshal',
    'IAddrExclusionControl', 'ISynchronizeMutex', 'IServerSecurity',
    'IRpcChannelBuffer3', 'ISynchronizeContainer', 'IClassActivator',
    'AsyncIPipeByte', 'IProcessInitControl', 'IAsyncRpcChannelBuffer',
    'IGlobalOptions', 'ISynchronizeEvent', 'IRunnableObject', 'IEnumSTATDATA',
    'IEnumFORMATETC', 'IThumbnailExtractor', 'IProgressNotify', 'IDataObject',
    'IRpcStubBuffer', 'IDummyHICONIncluder', 'IAdviseSink2', 'IBlockingLock',
    'IPersistStorage', 'IPSFactoryBuffer', 'IInternalUnknown', 'IPipeByte',
    'IMalloc', 'IApartmentShutdown', 'IRpcSyntaxNegotiate', 'IAgileObject',
    'IRunningObjectTable', 'IMarshal2', 'ICallFactory', 'IAdviseSink',
    'ISynchronizeHandle', 'IEnumContextProps', 'IWaitMultiple', 'tagMKREDUCE',
    '__REQUIRED_RPCSAL_H_VERSION__', 'COLE_DEFAULT_PRINCIPAL', '_WIN32_WINNT',
    'COLE_DEFAULT_AUTHINFO', '__REQUIRED_RPCNDR_H_VERSION__', 'tagTYMED',
    'tagShutdownType', 'tagRPCOPT_SERVER_LOCALITY_VALUES', 'tagPENDINGMSG',
    'tagGLOBALOPT_RPCTP_VALUES', 'tagApplicationType', '_APTTYPEQUALIFIER',
    'tagMKSYS', 'tagSTREAM_SEEK', 'tagDCOM_CALL_STATE', 'tagSTGTY', 'tagADVF',
    '_THDTYPE', 'tagPENDINGTYPE', 'tagRPCOPT_PROPERTIES', 'tagBIND_FLAGS',
    'tagEOLE_AUTHENTICATION_CAPABILITIES', 'tagACTIVATIONTYPE', 'tagDATADIR',
    'tagGLOBALOPT_RO_FLAGS', 'tagGLOBALOPT_EH_VALUES', '_APTTYPE', 'LPSTREAM',
    'tagGLOBALOPT_UNMARSHALING_POLICY_VALUES', 'tagEXTCONN', 'tagLOCKTYPE',
    'tagGLOBALOPT_PROPERTIES', 'tagCALLTYPE', 'tagSERVERCALL', 'tagFORMATETC',
    'CO_MARSHALING_CONTEXT_ATTRIBUTES', 'tagRPCOLEMESSAGE', 'tagSTATSTG',
    'tagSOLE_AUTHENTICATION_LIST', 'tagSTGMEDIUM', '_FLAG_STGMEDIUM',
    'tagINTERFACEINFO', 'tagSTATDATA', '_COSERVERINFO', 'tagMULTI_QI',
    'tagSOLE_AUTHENTICATION_SERVICE', 'tagSOLE_AUTHENTICATION_INFO',
    'tagStorageLayout', 'tagContextProperty', 'tagRemSNB', '_GDI_OBJECT',
    'tagDVTARGETDEVICE', '_userFLAG_STGMEDIUM', '_userSTGMEDIUM', 'STGMEDIUM',
    'tagBIND_OPTS3', 'tagBIND_OPTS2', 'tagRemSTGMEDIUM', 'tagBIND_OPTS',
    'SChannelHookCallInfo', 'LPENUMSTRING', 'LPENUMCONTEXTPROPS', 'wireSNB',
    'RPCOLEDATAREP', 'LPDATAADVISEHOLDER', 'LPPERSISTFILE', 'LPMALLOCSPY',
    'LPADVISESINK', 'wireASYNC_STGMEDIUM', 'LPENUMMONIKER', 'LPENUMFORMATETC',
    'LPADDRTRACKINGCONTROL', 'LPENUMUNKNOWN', 'LPCLIPFORMAT', 'LPROOTSTORAGE',
    'ASYNC_STGMEDIUM', 'LPPERSISTSTORAGE', 'LPMESSAGEFILTER', 'LPADVISESINK2',
    'LPSURROGATE', 'LPEXTERNALCONNECTION', 'LPRUNNABLEOBJECT', 'CPFLAGS',
    'wireFLAG_STGMEDIUM', 'LPSTGMEDIUM', 'LPPERSIST', 'LPMULTIQI', 'LPMALLOC',
    'APARTMENTID', 'PRPCOLEMESSAGE', 'LPDATAOBJECT', 'LPBINDCTX', 'LPMONIKER',
    'LPRUNNINGOBJECTTABLE', 'LPGLOBALINTERFACETABLE', 'LPMARSHAL2',
    'LPINITIALIZESPY', 'LPCANCELMETHODCALLS', 'LPSTDMARSHALINFO', 'LPSTORAGE',
    'LPLOCKBYTES', 'wireSTGMEDIUM', 'LPENUMSTATSTG', 'LPADDREXCLUSIONCONTROL',
    'PSOLE_AUTHENTICATION_SERVICE', 'LPPERSISTSTREAM', 'LPMARSHAL',
)
