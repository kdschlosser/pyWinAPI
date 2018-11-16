import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *


class _BTHDDI_SDP_NODE_INTERFACE(ctypes.Structure):
    pass


BTHDDI_SDP_NODE_INTERFACE = _BTHDDI_SDP_NODE_INTERFACE
PBTHDDI_SDP_NODE_INTERFACE = POINTER(_BTHDDI_SDP_NODE_INTERFACE)


class _BTHDDI_SDP_PARSE_INTERFACE(ctypes.Structure):
    pass


BTHDDI_SDP_PARSE_INTERFACE = _BTHDDI_SDP_PARSE_INTERFACE
PBTHDDI_SDP_PARSE_INTERFACE = POINTER(_BTHDDI_SDP_PARSE_INTERFACE)

__BTHSDPDDI_H__ = None
# Copyright (C) Microsoft. All rights reserved.
if not defined(__BTHSDPDDI_H__):
    __BTHSDPDDI_H__ = 1

    if NTDDI_VERSION >= NTDDI_VISTA:
        from pyWinAPI.km.sdpnode_h import *  # NOQA

        if defined(__cplusplus):
            pass
        # END IF

        BTHDDI_SDP_PARSE_INTERFACE_VERSION_FOR_QI = 0x0100
        BTHDDI_SDP_NODE_INTERFACE_VERSION_FOR_QI = 0x0100

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_TREE_ROOT_NODE (*PCREATENODETREEROOT)(_In_ ULONG tag);

        class _CREATENODETREEROOT(PSDP_TREE_ROOT_NODE):

            def __init__(self, tag):
                PSDP_TREE_ROOT_NODE.__init__(self)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODETREEROOT = POINTER(_CREATENODETREEROOT)

        # _IRQL_requires_same_
        # typedef NTSTATUS (*PFREETREE)(
        # _In_ __drv_freesMem(Mem) PSDP_TREE_ROOT_NODE Tree
        # );

        class _PFREETREE(NTSTATUS):

            def __init__(self, Tree):
                super(_PFREETREE).__init__()
                self.Tree = ctypes.cast(Tree, PSDP_TREE_ROOT_NODE)


        PFREETREE = POINTER(_PFREETREE)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # typedef NTSTATUS (
        # *PAPPENDNODETOCONTAINERNODE)(
        # _In_ PSDP_NODE Container,
        # _In_ __drv_aliasesMem PSDP_NODE Node
        # );

        class _PAPPENDNODETOCONTAINERNODE(NTSTATUS):

            def __init__(self, Container, Node):
                super(_PAPPENDNODETOCONTAINERNODE).__init__()
                self.Container = ctypes.cast(Container, PSDP_NODE)
                self.Node = ctypes.cast(Node, PSDP_NODE)


        PAPPENDNODETOCONTAINERNODE = POINTER(_PAPPENDNODETOCONTAINERNODE)

        # Must_inspect_result_
        # _IRQL_requires_same_
        # typedef NTSTATUS (*PADDATTRIBUTETOTREEE)(
        # _In_ PSDP_TREE_ROOT_NODE Root,
        # _In_ USHORT AttribId,
        # _In_ __drv_aliasesMem PSDP_NODE AttribValueNode,
        # _In_ ULONG tag
        # );
        class _ADDATTRIBUTETOTREEE(NTSTATUS):

            def __init__(self, Root, AttribId, AttribValueNode, tag):
                super(_ADDATTRIBUTETOTREEE).__init__()
                self.Root = ctypes.cast(Root, PSDP_TREE_ROOT_NODE)
                self.AttribId = ctypes.cast(AttribId, USHORT)
                self.AttribValueNode = ctypes.cast(AttribValueNode, PSDP_NODE)
                self.tag = ctypes.cast(tag, ULONG)


        PADDATTRIBUTETOTREEE = POINTER(_ADDATTRIBUTETOTREEE)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODENIL)(
        # _In_ ULONG tag
        # );
        class _CREATENODENIL(PSDP_NODE):

            def __init__(self, tag):
                PSDP_NODE.__init__(self)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODENIL = POINTER(_CREATENODENIL)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEBOOLEAN)(
        # _In_ UCHAR bVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEBOOLEAN(PSDP_NODE):

            def __init__(self, bVal, tag):
                PSDP_NODE.__init__(self)
                self.bVal = ctypes.cast(bVal, UCHAR)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEBOOLEAN = POINTER(_CREATENODEBOOLEAN)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUINT8)(
        # _In_ UCHAR ucVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEUINT8(PSDP_NODE):

            def __init__(self, ucVal, tag):
                PSDP_NODE.__init__(self)
                self.ucVal = ctypes.cast(ucVal, UCHAR)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUINT8 = POINTER(_CREATENODEUINT8)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUINT16)(
        # _In_ USHORT usVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEUINT16(PSDP_NODE):

            def __init__(self, usVal, tag):
                PSDP_NODE.__init__(self)
                self.usVal = ctypes.cast(usVal, USHORT)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUINT16 = POINTER(_CREATENODEUINT16)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUINT32)(
        # _In_ ULONG ulVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEUINT32(PSDP_NODE):

            def __init__(self, ulVal, tag):
                PSDP_NODE.__init__(self)
                self.ulVal = ctypes.cast(ulVal, ULONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUINT32 = POINTER(_CREATENODEUINT32)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUINT64)(
        # _In_ ULONGLONG ullVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEUINT64(PSDP_NODE):

            def __init__(self, ullVal, tag):
                PSDP_NODE.__init__(self)
                self.ullVal = ctypes.cast(ullVal, ULONGLONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUINT64 = POINTER(_CREATENODEUINT64)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUINT128)(
        # _In_ PSDP_ULARGE_INTEGER_16 puli16Val,
        # _In_ ULONG tag
        # );
        class _CREATENODEUINT128(PSDP_NODE):

            def __init__(self, puli16Val, tag):
                PSDP_NODE.__init__(self)
                self.puli16Val = ctypes.cast(puli16Val, PSDP_ULARGE_INTEGER_16)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUINT128 = POINTER(_CREATENODEUINT128)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEINT8)(
        # _In_ CHAR cVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEINT8(PSDP_NODE):

            def __init__(self, cVal, tag):
                PSDP_NODE.__init__(self)
                self.cVal = ctypes.cast(cVal, CHAR)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEINT8 = POINTER(_CREATENODEINT8)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEINT16)(
        # _In_ SHORT sVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEINT16(PSDP_NODE):

            def __init__(self, sVal, tag):
                PSDP_NODE.__init__(self)
                self.sVal = ctypes.cast(sVal, SHORT)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEINT16 = POINTER(_CREATENODEINT16)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEINT32)(
        # _In_ LONG lVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEINT32(PSDP_NODE):

            def __init__(self, lVal, tag):
                PSDP_NODE.__init__(self)
                self.lVal = ctypes.cast(lVal, LONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEINT32 = POINTER(_CREATENODEINT32)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEINT64)(
        # _In_ LONGLONG llVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEINT64(PSDP_NODE):

            def __init__(self, llVal, tag):
                PSDP_NODE.__init__(self)
                self.llVal = ctypes.cast(llVal, LONGLONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEINT64 = POINTER(_CREATENODEINT64)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEINT128)(
        # _In_ PSDP_LARGE_INTEGER_16 pul16Val,
        # _In_ ULONG tag
        # );
        class _CREATENODEINT128(PSDP_NODE):

            def __init__(self, pul16Val, tag):
                PSDP_NODE.__init__(self)
                self.pul16Val = ctypes.cast(pul16Val, PSDP_LARGE_INTEGER_16)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEINT128 = POINTER(_CREATENODEINT128)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUUID16)(
        # _In_ USHORT usVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEUUID16(PSDP_NODE):

            def __init__(self, usVal, tag):
                PSDP_NODE.__init__(self)
                self.usVal = ctypes.cast(usVal, USHORT)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUUID16 = POINTER(_CREATENODEUUID16)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUUID32)(
        # _In_ ULONG ulVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEUUID32(PSDP_NODE):

            def __init__(self, ulVal, tag):
                PSDP_NODE.__init__(self)
                self.ulVal = ctypes.cast(ulVal, ULONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUUID32 = POINTER(_CREATENODEUUID32)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEUUID128)(
        # _In_ const GUID * pUuidVal,
        # _In_ ULONG tag
        # );
        class _CREATENODEUUID128(PSDP_NODE):

            def __init__(self, pUuidVal, tag):
                PSDP_NODE.__init__(self)
                self.pUuidVal = ctypes.cast(pUuidVal, GUID)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEUUID128 = POINTER(_CREATENODEUUID128)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODESTRING)(
        # _In_reads_bytes_(stringLength) PCHAR string,
        # _In_ ULONG stringLength,
        # _In_ ULONG tag
        # );
        class _CREATENODESTRING(PSDP_NODE):

            def __init__(self, string, stringLength, tag):
                PSDP_NODE.__init__(self)
                self.string = ctypes.cast(string, PCHAR)
                self.stringLength = ctypes.cast(stringLength, ULONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODESTRING = POINTER(_CREATENODESTRING)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEURL)(
        # _In_reads_bytes_(urlLength) PCHAR url,
        # _In_ ULONG urlLength,
        # _In_ ULONG tag
        # );
        class _CREATENODEURL(PSDP_NODE):

            def __init__(self, url, urlLength, tag):
                PSDP_NODE.__init__(self)
                self.url = ctypes.cast(url, PCHAR)
                self.urlLength = ctypes.cast(urlLength, ULONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEURL = POINTER(_CREATENODEURL)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODEALTERNATIVE)(
        # _In_ ULONG tag
        # );
        class _CREATENODEALTERNATIVE(PSDP_NODE):

            def __init__(self, tag):
                PSDP_NODE.__init__(self)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODEALTERNATIVE = POINTER(_CREATENODEALTERNATIVE)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # _When_(return!=0, __drv_allocatesMem(Mem))
        # typedef PSDP_NODE (*PCREATENODESEQUENCE)(
        # _In_ ULONG tag
        # );
        class _CREATENODESEQUENCE(PSDP_NODE):

            def __init__(self, tag):
                PSDP_NODE.__init__(self)
                self.tag = ctypes.cast(tag, ULONG)


        PCREATENODESEQUENCE = POINTER(_CREATENODESEQUENCE)

        # GUID_BTHDDI_SDP_NODE_INTERFACE
        _BTHDDI_SDP_NODE_INTERFACE._fields_ = [
            ('Interface', INTERFACE),
            ('SdpCreateNodeTree', PCREATENODETREEROOT),
            ('SdpFreeTree', PFREETREE),
            ('SdpCreateNodeNil', PCREATENODENIL),
            ('SdpCreateNodeBoolean', PCREATENODEBOOLEAN),
            ('SdpCreateNodeUint8', PCREATENODEUINT8),
            ('SdpCreateNodeUint16', PCREATENODEUINT16),
            ('SdpCreateNodeUint32', PCREATENODEUINT32),
            ('SdpCreateNodeUint64', PCREATENODEUINT64),
            ('SdpCreateNodeUint128', PCREATENODEUINT128),
            ('SdpCreateNodeInt8', PCREATENODEINT8),
            ('SdpCreateNodeInt16', PCREATENODEINT16),
            ('SdpCreateNodeInt32', PCREATENODEINT32),
            ('SdpCreateNodeInt64', PCREATENODEINT64),
            ('SdpCreateNodeInt128', PCREATENODEINT128),
            ('SdpCreateNodeUuid16', PCREATENODEUUID16),
            ('SdpCreateNodeUuid32', PCREATENODEUUID32),
            ('SdpCreateNodeUuid128', PCREATENODEUUID128),
            ('SdpCreateNodeString', PCREATENODESTRING),
            ('SdpCreateNodeUrl', PCREATENODEURL),
            ('SdpCreateNodeAlternative', PCREATENODEALTERNATIVE),
            ('SdpCreateNodeSequence', PCREATENODESEQUENCE),
            ('SdpAddAttributeToTree', PADDATTRIBUTETOTREEE),
            ('SdpAppendNodeToContainerNode', PAPPENDNODETOCONTAINERNODE),
        ]

        # _IRQL_requires_same_
        # typedef void (*PBYTESWAPUUID128)(
        # _In_ GUID *pUuidFrom,
        # _Out_ GUID *pUuiidTo
        # );
        class _BYTESWAPUUID128(VOID):

            def __init__(self, pUuidFrom, pUuiidTo):
                super(_BYTESWAPUUID128).__init__(self)
                self.pUuidFrom = ctypes.cast(pUuidFrom, GUID)
                self.pUuiidTo = ctypes.cast(pUuiidTo, GUID)


        PBYTESWAPUUID128 = POINTER(_BYTESWAPUUID128)

        # _IRQL_requires_same_
        # typedef void (*PBYTESWAPUINT128)(
        # _In_ PSDP_ULARGE_INTEGER_16 pInUint128,
        # _Out_ PSDP_ULARGE_INTEGER_16 pOutUint128
        # );
        class _BYTESWAPUINT128(VOID):

            def __init__(self, pInUint128, pOutUint128):
                super(_BYTESWAPUINT128).__init__(self)
                self.pInUint128 = ctypes.cast(pInUint128, PSDP_ULARGE_INTEGER_16)
                self.pOutUint128 = ctypes.cast(pOutUint128, PSDP_ULARGE_INTEGER_16)


        PBYTESWAPUINT128 = POINTER(_BYTESWAPUINT128)

        # _IRQL_requires_same_
        # typedef ULONGLONG (*PBYTESWAPUINT64)(
        # _In_ ULONGLONG uint64
        # );
        class _BYTESWAPUINT64(ULONGLONG):

            def __init__(self, uint64):
                super(_BYTESWAPUINT64).__init__(self)
                self.uint64 = ctypes.cast(uint64, ULONGLONG)


        PBYTESWAPUINT64 = POINTER(_BYTESWAPUINT64)

        # _IRQL_requires_same_
        # typedef void (*PRETRIEVEUUID128)(
        # _In_ PUCHAR Stream,
        # _Out_ GUID *uuid128
        # );
        class _RETRIEVEUUID128(VOID):

            def __init__(self, Stream, uuid128):
                super(_RETRIEVEUUID128).__init__(self)
                self.Stream = ctypes.cast(Stream, PUCHAR)
                self.uuid128 = ctypes.cast(uuid128, GUID)


        PRETRIEVEUUID128 = POINTER(_RETRIEVEUUID128)

        # _IRQL_requires_same_
        # typedef void (*PRETRIEVEUINT128)(
        # _In_ PUCHAR Stream,
        # _Out_ PSDP_ULARGE_INTEGER_16 pUint128
        # );
        class _RETRIEVEUINT128(VOID):

            def __init__(self, Stream, pUint128):
                super(_RETRIEVEUINT128).__init__(self)
                self.Stream = ctypes.cast(Stream, PUCHAR)
                self.pUint128 = ctypes.cast(pUint128, PSDP_ULARGE_INTEGER_16)


        PRETRIEVEUINT128 = POINTER(_RETRIEVEUINT128)

        # _IRQL_requires_same_
        # typedef void (*PRETRIEVEUINT64)(
        # _In_ PUCHAR Stream,
        # _Out_ PULONGLONG pUint16
        # );
        class _RETRIEVEUINT64(VOID):

            def __init__(self, Stream, pUint16):
                super(_RETRIEVEUINT64).__init__(self)
                self.Stream = ctypes.cast(Stream, PUCHAR)
                self.pUint16 = ctypes.cast(pUint16, PULONGLONG)


        PRETRIEVEUINT64 = POINTER(_RETRIEVEUINT64)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # typedef NTSTATUS (*PVALIDATESTREAM)(
        # _In_reads_bytes_(Size) PUCHAR Stream,
        # _In_ ULONG Size,
        # _Out_ PULONG_PTR ErrorByte
        # );
        class _VALIDATESTREAM(NTSTATUS):

            def __init__(self, Stream, Size, ErrorByte):
                super(_VALIDATESTREAM).__init__(self)
                self.Stream = ctypes.cast(Stream, PUCHAR)
                self.Size = ctypes.cast(Size, ULONG)
                self.ErrorByte = ctypes.cast(ErrorByte, PULONG_PTR)


        PVALIDATESTREAM = POINTER(_VALIDATESTREAM)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # typedef NTSTATUS (*PFINDATTRIBUTEINTREE)(
        # _In_ PSDP_TREE_ROOT_NODE Tree,
        # _In_ USHORT AttribId,
        # _Outptr_ PSDP_NODE *AttribValue
        # );
        class _FINDATTRIBUTEINTREE(NTSTATUS):

            def __init__(self, Tree, AttribId, AttribValue):
                super(_FINDATTRIBUTEINTREE).__init__(self)
                self.Tree = ctypes.cast(Tree, PSDP_TREE_ROOT_NODE)
                self.AttribId = ctypes.cast(AttribId, USHORT)
                self.AttribValue = ctypes.cast(AttribValue, PSDP_NODE)


        PFINDATTRIBUTEINTREE = POINTER(_FINDATTRIBUTEINTREE)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # typedef NTSTATUS (*PCONVERTTREETOSTREAM)(
        # _In_ PSDP_TREE_ROOT_NODE Root,
        # _Post_ _When_(return==0, __drv_allocatesMem(Mem)) PUCHAR *Stream,
        # _Out_ PULONG Size,
        # _In_ ULONG tag
        # );
        class _CONVERTTREETOSTREAM(NTSTATUS):

            def __init__(self, Root, Stream, Size, tag):
                super(_CONVERTTREETOSTREAM).__init__(self)
                self.Root = ctypes.cast(Root, PSDP_TREE_ROOT_NODE)
                self.Stream = ctypes.cast(Stream, PUCHAR)
                self.Size = ctypes.cast(Size, PULONG)
                self.tag = ctypes.cast(tag, ULONG)


        PCONVERTTREETOSTREAM = POINTER(_CONVERTTREETOSTREAM)

        # _Must_inspect_result_
        # _IRQL_requires_same_
        # typedef NTSTATUS (*PCONVERTSTREAMTOTREE)(
        # _In_reads_bytes_(Size) PUCHAR Stream,
        # _In_ ULONG Size,
        # _Out_ PSDP_TREE_ROOT_NODE *Node,
        # _In_ ULONG tag
        # );
        class _CONVERTSTREAMTOTREE(NTSTATUS):

            def __init__(self, Stream, Size, Node, tag):
                super(_CONVERTSTREAMTOTREE).__init__(self)
                self.Stream = ctypes.cast(Stream, PUCHAR)
                self.Size = ctypes.cast(Size, ULONG)
                self.Node = ctypes.cast(Node, PSDP_TREE_ROOT_NODE)
                self.tag = ctypes.cast(tag, ULONG)


        PCONVERTSTREAMTOTREE = POINTER(_CONVERTSTREAMTOTREE)

        # _IRQL_requires_same_
        # typedef VOID (*PGETNEXTELEMENT)(
        # _In_reads_bytes_(StreamSize) PUCHAR Stream,
        # _In_ ULONG StreamSize,
        # _In_opt_ PUCHAR CurrentElement,
        # _Outptr_result_bytebuffer_(*NextElementSize) PUCHAR* NextElement,
        # _Out_ PULONG NextElementSize
        # );
        class _GETNEXTELEMENT(VOID):

            def __init__(
                self,
                Stream,
                StreamSize,
                CurrentElement,
                NextElement,
                NextElementSize
            ):
                super(_GETNEXTELEMENT).__init__(self)
                self.Stream = ctypes.cast(Stream, PUCHAR)
                self.StreamSize = ctypes.cast(StreamSize, ULONG)
                self.CurrentElement = ctypes.cast(CurrentElement, PUCHAR)
                self.NextElement = ctypes.cast(NextElement, PUCHAR)
                self.NextElementSize = ctypes.cast(NextElementSize, PULONG)


        PGETNEXTELEMENT = POINTER(_GETNEXTELEMENT)

        # typedef VOID (*pReservedFunction)(
        # );
        class _ReservedFunction(VOID):
            pass


        pReservedFunction = POINTER(_ReservedFunction)

        __BTHSDPDDIP_H__ = None
        if not defined(__BTHSDPDDIP_H__):
            _BTHDDI_SDP_PARSE_INTERFACE._fields_ = [
                ('Interface', INTERFACE),
                ('SdpValidateStream', PVALIDATESTREAM),
                ('SdpConvertStreamToTree', PCONVERTSTREAMTOTREE),
                ('SdpConvertTreeToStream', PCONVERTTREETOSTREAM),
                ('SdpFreeTree', PFREETREE),
                ('SdpByteSwapUuid128', PBYTESWAPUUID128),
                ('SdpByteSwapUint128', PBYTESWAPUINT128),
                ('SdpByteSwapUint64', PBYTESWAPUINT64),
                ('SdpRetrieveUuid128', PRETRIEVEUUID128),
                ('SdpRetrieveUint128', PRETRIEVEUINT128),
                ('SdpRetrieveUint64', PRETRIEVEUINT64),
                ('SdpFindAttributeInTree', PFINDATTRIBUTEINTREE),
                ('SdpGetNextElement', PGETNEXTELEMENT),
                ('Reserved1', pReservedFunction),
                ('Reserved2', pReservedFunction),
                ('Reserved3', pReservedFunction),
                ('Reserved4', pReservedFunction),
            ]
        # END IF

        if defined(__cplusplus):
            pass
        # END IF

    # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
# END IF    __BTHSDPDDI_H__
