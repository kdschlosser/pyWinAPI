import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


class * NDR_SCONTEXT(ctypes.Structure):
    pass


class _SCONTEXT_QUEUE(ctypes.Structure):
    pass

SCONTEXT_QUEUE = _SCONTEXT_QUEUE
PSCONTEXT_QUEUE = POINTER(_SCONTEXT_QUEUE)


class ARRAY_INFO(ctypes.Structure):
    pass

PARRAY_INFO = POINTER(ARRAY_INFO)


class _MIDL_STUB_MESSAGE(ctypes.Structure):
    pass

MIDL_STUB_MESSAGE = _MIDL_STUB_MESSAGE
PMIDL_STUB_MESSAGE = POINTER(_MIDL_STUB_MESSAGE)


class _GENERIC_BINDING_ROUTINE_PAIR(ctypes.Structure):
    pass

GENERIC_BINDING_ROUTINE_PAIR = _GENERIC_BINDING_ROUTINE_PAIR
PGENERIC_BINDING_ROUTINE_PAIR = POINTER(_GENERIC_BINDING_ROUTINE_PAIR)


class __GENERIC_BINDING_INFO(ctypes.Structure):
    pass

GENERIC_BINDING_INFO = __GENERIC_BINDING_INFO
PGENERIC_BINDING_INFO = POINTER(__GENERIC_BINDING_INFO)


class _XMIT_ROUTINE_QUINTUPLE(ctypes.Structure):
    pass

XMIT_ROUTINE_QUINTUPLE = _XMIT_ROUTINE_QUINTUPLE
PXMIT_ROUTINE_QUINTUPLE = POINTER(_XMIT_ROUTINE_QUINTUPLE)


class _USER_MARSHAL_ROUTINE_QUADRUPLE(ctypes.Structure):
    pass

USER_MARSHAL_ROUTINE_QUADRUPLE = _USER_MARSHAL_ROUTINE_QUADRUPLE


class _USER_MARSHAL_CB(ctypes.Structure):
    pass

USER_MARSHAL_CB = _USER_MARSHAL_CB


class _MALLOC_FREE_STRUCT(ctypes.Structure):
    pass

MALLOC_FREE_STRUCT = _MALLOC_FREE_STRUCT


class _COMM_FAULT_OFFSETS(ctypes.Structure):
    pass

COMM_FAULT_OFFSETS = _COMM_FAULT_OFFSETS


class _NDR_CS_SIZE_CONVERT_ROUTINES(ctypes.Structure):
    pass

NDR_CS_SIZE_CONVERT_ROUTINES = _NDR_CS_SIZE_CONVERT_ROUTINES


class _NDR_CS_ROUTINES(ctypes.Structure):
    pass

NDR_CS_ROUTINES = _NDR_CS_ROUTINES


class _NDR_EXPR_DESC(ctypes.Structure):
    pass

NDR_EXPR_DESC = _NDR_EXPR_DESC


class _MIDL_STUB_DESC(ctypes.Structure):
    pass

MIDL_STUB_DESC = _MIDL_STUB_DESC


class _MIDL_FORMAT_STRING(ctypes.Structure):
    pass

MIDL_FORMAT_STRING = _MIDL_FORMAT_STRING


class _MIDL_METHOD_PROPERTY(ctypes.Structure):
    pass

MIDL_METHOD_PROPERTY = _MIDL_METHOD_PROPERTY
PMIDL_METHOD_PROPERTY = POINTER(_MIDL_METHOD_PROPERTY)


class _MIDL_METHOD_PROPERTY_MAP(ctypes.Structure):
    pass

MIDL_METHOD_PROPERTY_MAP = _MIDL_METHOD_PROPERTY_MAP
PMIDL_METHOD_PROPERTY_MAP = POINTER(_MIDL_METHOD_PROPERTY_MAP)


class _MIDL_INTERFACE_METHOD_PROPERTIES(ctypes.Structure):
    pass

MIDL_INTERFACE_METHOD_PROPERTIES = _MIDL_INTERFACE_METHOD_PROPERTIES


class _MIDL_SERVER_INFO_(ctypes.Structure):
    pass

MIDL_SERVER_INFO = _MIDL_SERVER_INFO_
PMIDL_SERVER_INFO = POINTER(_MIDL_SERVER_INFO_)


class _MIDL_STUBLESS_PROXY_INFO(ctypes.Structure):
    pass

MIDL_STUBLESS_PROXY_INFO = _MIDL_STUBLESS_PROXY_INFO


class _MIDL_SYNTAX_INFO(ctypes.Structure):
    pass

MIDL_SYNTAX_INFO = _MIDL_SYNTAX_INFO
PMIDL_SYNTAX_INFO = POINTER(_MIDL_SYNTAX_INFO)


class _CLIENT_CALL_RETURN(ctypes.Union):
    pass

CLIENT_CALL_RETURN = _CLIENT_CALL_RETURN


class _FULL_PTR_XLAT_TABLES(ctypes.Structure):
    pass

FULL_PTR_XLAT_TABLES = _FULL_PTR_XLAT_TABLES
PFULL_PTR_XLAT_TABLES = POINTER(_FULL_PTR_XLAT_TABLES)


class _MIDL_INTERCEPTION_INFO(ctypes.Structure):
    pass

MIDL_INTERCEPTION_INFO = _MIDL_INTERCEPTION_INFO
PMIDL_INTERCEPTION_INFO = POINTER(_MIDL_INTERCEPTION_INFO)


class _MIDL_WINRT_TYPE_SERIALIZATION_INFO(ctypes.Structure):
    pass

MIDL_WINRT_TYPE_SERIALIZATION_INFO = _MIDL_WINRT_TYPE_SERIALIZATION_INFO
PMIDL_WINRT_TYPE_SERIALIZATION_INFO = POINTER(_MIDL_WINRT_TYPE_SERIALIZATION_INFO)


class _NDR_USER_MARSHAL_INFO_LEVEL1(ctypes.Structure):
    pass

NDR_USER_MARSHAL_INFO_LEVEL1 = _NDR_USER_MARSHAL_INFO_LEVEL1


NDR_USER_MARSHAL_INFO = _NDR_USER_MARSHAL_INFO


# /* + + Copyright (c) Microsoft Corporation. All rights reserved. Module
# Name: rpcndr.h Abstract: Definitions for stub data structures and prototypes
# of helper functions. - -
if _MSC_VER >= 1200:
    pass
# END IF
# This version of the rpcndr.h file corresponds to MIDL version 5.0. +
# used with Windows 2000/XP build 1700 +
if not defined(__RPCNDR_H_VERSION__):
    __RPCNDR_H_VERSION__ = 500
# END IF   __RPCNDR_H_VERSION__
if not defined(__RPCNDR_H__):
    #~#~#~    #define __RPCNDR_H__
    if _MSC_VER > 1000:
        pass
    # END IF
        if  __RPCNDR_H_VERSION__ < __REQUIRED_RPCNDR_H_VERSION__ :
            pass
        # END IF
    if defined(__REQUIRED_RPCNDR_H_VERSION__):
        pass
    # END IF
    from winapifamily_h import * # NOQA
    from pshpack8_h import * # NOQA
    from basetsd_h import * # NOQA
    if not defined(_KRPCENV_):
        from rpcnsip_h import * # NOQA
    # END IF
    from rpcsal_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF
        # ************************************************************************** Network Computing Architecture (NCA) definition: Network Data Representation: (NDR) Label format: An ULONG (32 bits) with the following layout: 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 + - - - - - - - - - - - - - - - + - - - - - - - - - - - - - - - + - - - - - - - - - - - - - - - + - - - - - - - + - - - - - - - + | Reserved | Reserved  | Floating point | Int | Char | |   |   | Representation | Rep. | Rep. | + - - - - - - - - - - - - - - - + - - - - - - - - - - - - - - - + - - - - - - - - - - - - - - - + - - - - - - - + - - - - - - - + Where Reserved: Must be zero (0) for NCA 1.5 and NCA 2.0. Floating point Representation is: 0 - IEEE 1 - VAX 2 - Cray 3 - IBM Int Rep. is Integer Representation: 0 - Big Endian 1 - Little Endian Char Rep. is Character Representation: 0 - ASCII 1 - EBCDIC The Microsoft Local Data Representation (for all platforms which are of interest currently is edefined below: *************************************************************************
        # 
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        NDR_CHAR_REP_MASK = (unsigned long)0x0000000F
        NDR_INT_REP_MASK = (unsigned long)0x000000F0
        NDR_FLOAT_REP_MASK = (unsigned long)0x0000FF00
        NDR_LITTLE_ENDIAN = (unsigned long)0x00000010
        NDR_BIG_ENDIAN = (unsigned long)0x00000000
        NDR_IEEE_FLOAT = (unsigned long)0x00000000
        NDR_VAX_FLOAT = (unsigned long)0x00000100
        NDR_IBM_FLOAT = (unsigned long)0x00000300
        NDR_ASCII_CHAR = (unsigned long)0x00000000
        NDR_EBCDIC_CHAR = (unsigned long)0x00000001
        if defined(__RPC_MAC__):
            NDR_LOCAL_DATA_REPRESENTATION = (unsigned long)0x00000000
            NDR_LOCAL_ENDIAN = NDR_BIG_ENDIAN
        else:
            NDR_LOCAL_DATA_REPRESENTATION = (unsigned long)0x00000010
            NDR_LOCAL_ENDIAN = NDR_LITTLE_ENDIAN
        # END IF
        # ************************************************************************** Macros for targeted platforms *************************************************************************
        # 
        if 0x0A00 <= _WIN32_WINNT:
            TARGET_IS_NT100_OR_LATER = 1
        else:
            TARGET_IS_NT100_OR_LATER = 0
        # END IF
        if 0x603 <= _WIN32_WINNT:
            TARGET_IS_NT63_OR_LATER = 1
        else:
            TARGET_IS_NT63_OR_LATER = 0
        # END IF
        if 0x602 <= _WIN32_WINNT:
            TARGET_IS_NT62_OR_LATER = 1
        else:
            TARGET_IS_NT62_OR_LATER = 0
        # END IF
        if 0x601 <= _WIN32_WINNT:
            TARGET_IS_NT61_OR_LATER = 1
        else:
            TARGET_IS_NT61_OR_LATER = 0
        # END IF
        if 0x600 <= _WIN32_WINNT:
            TARGET_IS_NT60_OR_LATER = 1
        else:
            TARGET_IS_NT60_OR_LATER = 0
        # END IF
        if 0x501 <= _WIN32_WINNT:
            TARGET_IS_NT51_OR_LATER = 1
        else:
            TARGET_IS_NT51_OR_LATER = 0
        # END IF
        if 0x500 <= _WIN32_WINNT:
            TARGET_IS_NT50_OR_LATER = 1
        else:
            TARGET_IS_NT50_OR_LATER = 0
        # END IF
        if defined(_WIN32_DCOM) or 0x400 <= _WIN32_WINNT:
            TARGET_IS_NT40_OR_LATER = 1
        else:
            TARGET_IS_NT40_OR_LATER = 0
        # END IF
        if 0x400 <= WINVER:
            TARGET_IS_NT351_OR_WIN95_OR_LATER = 1
        else:
            TARGET_IS_NT351_OR_WIN95_OR_LATER = 0
        # END IF
        # ************************************************************************** Other MIDL base types / predefined types: *************************************************************************
        # 
        small = char
        if not defined(_HYPER_DEFINED):
            #~#~#~            #define _HYPER_DEFINED
            if not defined(_M_IX86) or (defined(_INTEGRAL_MAX_BITS) and _INTEGRAL_MAX_BITS >= 64):
                hyper = __int64
                MIDL_uhyper = UINT __int64
            else:
            # END IF
        # END IF   _HYPER_DEFINED
        if not defined(_WCHAR_T_DEFINED):
            #~#~#~            #define _WCHAR_T_DEFINED        # END IF
        if not defined(_SIZE_T_DEFINED):
            if defined(__RPC_WIN64__) or defined(__RPC_ARM64__):
            else:
            # END IF
            #~#~#~            #define _SIZE_T_DEFINED        # END IF
        if defined(__RPC_WIN32__):
            if _MSC_VER >= 800) or defined(_STDCALL_SUPPORTED:
                __RPC_CALLEE = __stdcall
            else:
                #~#~#~                #define __RPC_CALLEE            # END IF
        # END IF
        if not defined(__MIDL_USER_DEFINED):
            midl_user_allocate = MIDL_user_allocate
            midl_user_free = MIDL_user_free
            #~#~#~            #define __MIDL_USER_DEFINED        # END IF
        RPC_VAR_ENTRY = __cdecl

        # winnt only
        if defined(_M_IX86) or defined(_M_AMD64) or defined(_M_IA64):
            __MIDL_DECLSPEC_DLLIMPORT = __declspec(dllimport)
            __MIDL_DECLSPEC_DLLEXPORT = __declspec(dllexport)
        else:
            #~#~#~            #define __MIDL_DECLSPEC_DLLIMPORT            #~#~#~            #define __MIDL_DECLSPEC_DLLEXPORT        # END IF
        # ************************************************************************** Context handle management related definitions: Client and Server Contexts. *************************************************************************
        # 
        * NDR_SCONTEXT._fields_ = [
            ('pad', POINTER(VOID) * 2),
            ('userContext', POINTER(VOID)),
        ]
        

        def NDRSContextValue(hContext):
            return (& hContext - >userContext)
        cbNDRContext = 20        # size of context on WIRE

# typedef VOID (__RPC_USER  * NDR_RUNDOWN)(VOID  * context);
        NDR_RUNDOWN = __RPC_USER(
            VOID,        )


# typedef VOID (__RPC_USER  * NDR_NOTIFY_ROUTINE)(VOID);
        NDR_NOTIFY_ROUTINE = __RPC_USER(
            VOID,        )


# typedef VOID (__RPC_USER  * NDR_NOTIFY2_ROUTINE)(BOOLEAN flag);
        NDR_NOTIFY2_ROUTINE = __RPC_USER(
            VOID,        )


        _SCONTEXT_QUEUE._fields_ = [
            ('NumberOfObjects', ULONG),
            ('ArrayOfObjects', POINTER(NDR_SCONTEXT)),
        ]
        rpcrt4 = ctypes.windll.RPCRT4


        # RPCRTAPI
        # RPC_BINDING_HANDLE
        # RPC_ENTRY
        # NDRCContextBinding(
        # _In_ NDR_CCONTEXT     CContext
        # );
        NDRCContextBinding = rpcrt4.NDRCContextBinding
        NDRCContextBinding.restype = RPC_BINDING_HANDLE


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NDRCContextMarshall(
        # _In_opt_  NDR_CCONTEXT    CContext,
        # _Out_ VOID  *pBuff
        # );
        NDRCContextMarshall = rpcrt4.NDRCContextMarshall
        NDRCContextMarshall.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NDRCContextUnmarshall(
        # _Inout_opt_ NDR_CCONTEXT        *   pCContext,
        # _In_  RPC_BINDING_HANDLE      hBinding,
        # _In_  VOID                *   pBuff,
        # _In_  ULONG           DataRepresentation
        # );
        NDRCContextUnmarshall = rpcrt4.NDRCContextUnmarshall
        NDRCContextUnmarshall.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NDRSContextMarshall(
        # _In_  NDR_SCONTEXT    CContext,
        # _Out_ VOID          * pBuff,
        # _In_  NDR_RUNDOWN     userRunDownIn
        # );
        NDRSContextMarshall = rpcrt4.NDRSContextMarshall
        NDRSContextMarshall.restype = void


        # RPCRTAPI
        # NDR_SCONTEXT
        # RPC_ENTRY
        # NDRSContextUnmarshall(
        # _In_  VOID          * pBuff,
        # _In_  ULONG   DataRepresentation
        # );
        NDRSContextUnmarshall = rpcrt4.NDRSContextUnmarshall
        NDRSContextUnmarshall.restype = NDR_SCONTEXT


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NDRSContextMarshallEx(
        # _In_  RPC_BINDING_HANDLE  BindingHandle,
        # _In_  NDR_SCONTEXT        CContext,
        # _Out_ VOID              * pBuff,
        # _In_  NDR_RUNDOWN         userRunDownIn
        # );
        NDRSContextMarshallEx = rpcrt4.NDRSContextMarshallEx
        NDRSContextMarshallEx.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NDRSContextMarshall2(
        # _In_  RPC_BINDING_HANDLE  BindingHandle,
        # _In_  NDR_SCONTEXT        CContext,
        # _Out_ VOID              * pBuff,
        # _In_  NDR_RUNDOWN         userRunDownIn,
        # _In_opt_  VOID              * CtxGuard,
        # _In_ ULONG        Flags
        # );
        NDRSContextMarshall2 = rpcrt4.NDRSContextMarshall2
        NDRSContextMarshall2.restype = void


        # RPCRTAPI
        # NDR_SCONTEXT
        # RPC_ENTRY
        # NDRSContextUnmarshallEx(
        # _In_  RPC_BINDING_HANDLE  BindingHandle,
        # _In_  VOID              * pBuff,
        # _In_  ULONG       DataRepresentation
        # );
        NDRSContextUnmarshallEx = rpcrt4.NDRSContextUnmarshallEx
        NDRSContextUnmarshallEx.restype = NDR_SCONTEXT


        # RPCRTAPI
        # NDR_SCONTEXT
        # RPC_ENTRY
        # NDRSContextUnmarshall2(
        # _In_  RPC_BINDING_HANDLE  BindingHandle,
        # _In_opt_  VOID              * pBuff,
        # _In_  ULONG       DataRepresentation,
        # _In_opt_  VOID              * CtxGuard,
        # _In_ ULONG        Flags
        # );
        NDRSContextUnmarshall2 = rpcrt4.NDRSContextUnmarshall2
        NDRSContextUnmarshall2.restype = NDR_SCONTEXT


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # RpcSsDestroyClientContext(
        # _In_ VOID  *  * ContextHandle
        # );
        RpcSsDestroyClientContext = rpcrt4.RpcSsDestroyClientContext
        RpcSsDestroyClientContext.restype = void


        # ************************************************************************** NDR conversion related definitions. *************************************************************************
        # 
        def byte_from_ndr(source, target):
            return { *target = *(*CHAR * * & source - >Buffer) + + ; }
        

        def byte_array_from_ndr(Source, LowerIndex, UpperIndex, Target):
            return { NDRcopy ( ((CHAR *Target) + LowerIndex), Source - >Buffer, unsigned int(UpperIndex - LowerIndex)); *unsigned LONG * & Source - >Buffer + = (UpperIndex - LowerIndex); }
        

        def boolean_from_ndr(source, target):
            return { *target = *(*CHAR * * & source - >Buffer) + + ; }
        

        def boolean_array_from_ndr(Source, LowerIndex, UpperIndex, Target):
            return { NDRcopy ( ((CHAR *Target) + LowerIndex), Source - >Buffer, unsigned int(UpperIndex - LowerIndex)); *unsigned LONG * & Source - >Buffer + = (UpperIndex - LowerIndex); }
        

        def small_from_ndr(source, target):
            return { *target = *(*CHAR * * & source - >Buffer) + + ; }
        

        def small_from_ndr_temp(source, target, format):
            return { *target = *(*CHAR * *source) + + ; }
        

        def small_array_from_ndr(Source, LowerIndex, UpperIndex, Target):
            return { NDRcopy ( ((CHAR *Target) + LowerIndex), Source - >Buffer, unsigned int(UpperIndex - LowerIndex)); *unsigned LONG * & Source - >Buffer + = (UpperIndex - LowerIndex); }

        # ************************************************************************** Platform specific mapping of c - runtime functions. *************************************************************************
        # 
        if defined(__RPC_WIN32__) or defined(__RPC_WIN64__) or defined(__RPC_ARM32__) or defined(__RPC_ARM64__):
            def MIDL_ascii_strlen(string):
                return strlenstring
            

            def MIDL_ascii_strcpy(target, source):
                return strcpytarget,source
            

            def MIDL_(ctypes.memset(s, c, n)(ctypes.memset(s, c, n):
                return 1
        # END IF
        # ************************************************************************** MIDL 2.0 ndr definitions. *************************************************************************
        # 
        def _midl_ma1(p, cast):
            return *(* cast ** & p) + +
        def _midl_ma2(p, cast):
            return *(* cast ** & p) + +
        def _midl_ma4(p, cast):
            return *(* cast ** & p) + +
        def _midl_ma8(p, cast):
            return *(* cast ** & p) + +
        def _midl_unma1(p, cast):
            return *( cast *p) + +
        def _midl_unma2(p, cast):
            return *( cast *p) + +
        def _midl_unma3(p, cast):
            return *( cast *p) + +
        def _midl_unma4(p, cast):
            return *( cast *p) + +
        # Some alignment specific macros.
        # RKK64
        # these appear to be used in fossils inside MIDL
        def _midl_fa2(p):
            return (p = RPC_BUFPTR (ULONG_PTR(p + 1) & ~0x1))
        def _midl_fa4(p):
            return (p = RPC_BUFPTR (ULONG_PTR(p + 3) & ~0x3))
        def _midl_fa8(p):
            return (p = RPC_BUFPTR (ULONG_PTR(p + 7) & ~0x7))
        def _midl_addp(p, n):
            return (p + = n)
        # Marshalling macros
        def _midl_marsh_lhs(p, cast):
            return *(* cast ** & p) + +
        def _midl_marsh_up(mp, p):
            return *(*unsigned LONG ** & mp) + + = unsigned longp
        def _midl_advmp(mp):
            return *(*unsigned LONG ** & mp) + +
        def _midl_unmarsh_up(p):
            return (*(*unsigned LONG ** & p) + +)
        # //////////////////////////////////////////////////////////////////////////
        # 
        # Ndr macros.
        # //////////////////////////////////////////////////////////////////////////
        # 
        # RKK64
        # these appear to be used in fossils inside MIDL
        def NdrMarshConfStringHdr(p, s, l):
            return (_midl_ma4 p, UINT long = s, _midl_ma4 p, UINT long = 0, _midl_ma4 p, UINT long = l)
        def NdrUnMarshConfStringHdr(p, s, l):
            return 1
        def NdrMarshCCtxtHdl(pc, p):
            return (NDRCContextMarshall( NDR_CCONTEXTpc, p ),p + 20)
        def NdrUnMarshCCtxtHdl(pc, p, h, drep):
            return (NDRCContextUnmarshall(NDR_CONTEXTpc,h,p,drep), p + 20)
        def NdrUnMarshSCtxtHdl(pc, p, drep):
            return (pc = NdrSContextUnMarshallp,drep )
        def NdrMarshSCtxtHdl(pc, p, rd):
            return 1
        # end of unused
        def NdrFieldOffset(s, f):
            return LONG_PTR(& ((s *0) - >f))
        def NdrFieldPad(s, f, p, t):
            return 1
        def NdrFcShort(s):
            return UCHAR(s & 0xFF), UCHAR(s >> 8)
        def NdrFcLong(s):
            return UCHAR(s & 0xFF), UCHAR((s & 0x0000FF00) >> 8), UCHAR((s & 0x00FF0000) >> 16), UCHAR(s >> 24)
        # On the server side, the following exceptions are mapped to
        # the bad stub data exception if - error stub_data is used.
        RPC_BAD_STUB_DATA_EXCEPTION_FILTER = (
            (RpcExceptionCode() == STATUS_ACCESS_VIOLATION) or 
            (RpcExceptionCode() == STATUS_DATATYPE_MISALIGNMENT) or 
            (RpcExceptionCode() == RPC_X_BAD_STUB_DATA) or 
            (RpcExceptionCode() == RPC_S_INVALID_BOUND)
        )
        # ///////////////////////////////////////////////////////////////////////////
        # 
        # Some stub helper functions.
        # ///////////////////////////////////////////////////////////////////////////
        # 
        # //////////////////////////////////////////////////////////////////////////
        # 
        # Stub helper structures.
        # //////////////////////////////////////////////////////////////////////////
        # 
        _MIDL_STUB_MESSAGE = struct
        _MIDL_STUB_DESC = struct
        _FULL_PTR_XLAT_TABLES = struct
        # Expression evaluation callback routine prototype.
# typedef VOID (__RPC_USER  * EXPR_EVAL)( struct _MIDL_STUB_MESSAGE  * );
        EXPR_EVAL = __RPC_USER(
            VOID,        )
        # /* Multidimensional conformant/varying array struct.
        ARRAY_INFO._fields_ = [
            ('Dimension', LONG),
            # These fields MUST be (unsigned LONG *)
            ('BufferConformanceMark', POINTER(ULONG)),
            ('BufferVarianceMark', POINTER(ULONG)),
            # Count arrays, used for top level arrays in - Os stubs
            ('MaxCountArray', POINTER(ULONG)),
            ('OffsetArray', POINTER(ULONG)),
            ('ActualCountArray', POINTER(ULONG)),
        ]
        PNDR_ASYNC_MESSAGE = 
        PNDR_CORRELATION_INFO = POINTER(_NDR_CORRELATION_INFO)
        # /* MIDL Stub Message
        PMIDL_SYNTAX_INFO = POINTER(MIDL_SYNTAX_INFO,)
        NDR_ALLOC_ALL_NODES_CONTEXT = struct
        NDR_POINTER_QUEUE_STATE = struct
        _NDR_PROC_CONTEXT = struct
        _MIDL_STUB_MESSAGE._fields_ = [
            # RPC message structure.
            ('RpcMsg', PRPC_MESSAGE),
            # Pointer into RPC message buffer.
            ('Buffer', POINTER(UCHAR)),
            ('These are used internally by the Ndr routines to mark the beginning * and end of an incoming RPC buffer. UCHAR       *   BufferStart', POINTER()),
            ('BufferEnd', POINTER(UCHAR)),
            ('Used internally by the Ndr routines as a place holder in the buffer. * On the marshalling side it's used to mark the location where conformance * size should be marshalled. * On the unmarshalling side it's used to mark the location in the buffer * used during pointer unmarshalling to base pointer offsets off of. UCHAR       *   BufferMark', POINTER()),
            # Set by the buffer sizing routines.
            ('BufferLength', ULONG),
            # Set by the memory sizing routines.
            ('MemorySize', ULONG),
            # Pointer to user memory.
            ('Memory', POINTER(UCHAR)),
            # Is the Ndr routine begin called from a client side stub.
            ('IsClient', UCHAR),
            ('Pad', UCHAR),
            ('uFlags2', USHORT),
            # Can the buffer be re - used for memory on unmarshalling.
            ('ReuseBuffer', INT),
            # Hold the context for allocate all nodes
            ('pAllocAllNodesContext', POINTER(NDR_ALLOC_ALL_NODES_CONTEXT)),
            ('pPointerQueueState', POINTER(NDR_POINTER_QUEUE_STATE)),
            # Ignore imbeded pointers while computing buffer or memory sizes.
            ('Stuff needed while handling complex structures INT                     IgnoreEmbeddedPointers', POINTER()),
            ('This marks the location in the buffer where pointees of a complex * struct reside. UCHAR       *   PointerBufferMark', POINTER()),
            ('Used to catch errors in SendReceive. UCHAR           CorrDespIncrement', POINTER()),
            ('uFlags', UCHAR),
            ('UniquePtrCount', USHORT),
            ('Used internally by the Ndr routines.  Holds the max counts for * a conformant array. ULONG_PTR               MaxCount', POINTER()),
            ('Used internally by the Ndr routines.  Holds the offsets for a varying * array. ULONG           Offset', POINTER()),
            ('Used internally by the Ndr routines.  Holds the actual counts for * a varying array. ULONG           ActualCount', POINTER()),
            # Allocation and Free routine to be used by the Ndr routines.
            ('( __RPC_API * pfnAllocate)( size_t )', POINTER(VOID)),
            ('( __RPC_API * pfnFree)(VOID  *)', VOID),
            ('Top of parameter stack.  Used for "single call" stubs during marshalling * to hold the beginning of the parameter list on the stack.  Needed to * extract parameters which hold attribute values for top level arrays and * pointers. UCHAR       *   StackTop', POINTER()),
            ('Fields used for the transmit_as and represent_as objects. *  For represent_as the mapping is', POINTER(), presented=local),
            ('transmit=named. UCHAR       *   pPresentedType', POINTER()),
            ('pTransmitType', POINTER(UCHAR)),
            ('When we first construct a binding on the client side', POINTER()),
            ('stick it * in the rpcmessage and later call RpcGetBuffer', POINTER()),
            ('the handle field * in the rpcmessage is changed. That's fine except that we need to * have that original handle for use in unmarshalling context handles * (the second argument in NDRCContextUnmarshall to be exact). So * stash the contructed handle here and extract it when needed. handle_t                SavedHandle', POINTER()),
            ('Pointer back to the stub descriptor.  Use this to get all handle info. _MIDL_STUB_DESC  * StubDesc', POINTER()),
            ('Full pointer stuff. _FULL_PTR_XLAT_TABLES  * FullPtrXlatTables', POINTER()),
            ('FullPtrRefId', ULONG),
            ('PointerLength', ULONG),
            ('fInDontFree', INT, 1),
            ('fDontCallFreeInst', INT, 1),
            ('fUnused1', INT, 1),
            ('fHasReturn', INT, 1),
            ('fHasExtensions', INT, 1),
            ('fHasNewCorrDesc', INT, 1),
            ('fIsIn', INT, 1),
            ('fIsOut', INT, 1),
            ('fIsOicf', INT, 1),
            ('fBufferValid', INT, 1),
            ('fHasMemoryValidateCallback', INT, 1),
            ('fInFree', INT, 1),
            ('fNeedMCCP', INT, 1),
            ('fUnused2', INT, 3),
            ('fUnused3', INT, 16),
            ('dwDestContext', ULONG),
            ('pvDestContext', POINTER(VOID)),
            ('SavedContextHandles', POINTER(NDR_SCONTEXT)),
            ('ParamNumber', LONG),
            ('pRpcChannelBuffer', POINTER(IRpcChannelBuffer)),
            ('pArrayInfo', PARRAY_INFO),
            ('SizePtrCountArray', POINTER(ULONG)),
            ('SizePtrOffsetArray', POINTER(ULONG)),
            ('SizePtrLengthArray', POINTER(ULONG)),
            ('Interpreter argument queue.  Used on server side only. VOID                    *       pArgQueue', POINTER()),
            ('dwStubPhase', ULONG),
            ('LowStackMark', POINTER(VOID)),
            ('Async message pointer', POINTER()),
            ('correlation data - NT 5.0 features. PNDR_ASYNC_MESSAGE              pAsyncMsg', POINTER()),
            ('pCorrInfo', PNDR_CORRELATION_INFO),
            ('pCorrMemory', POINTER(UCHAR)),
            ('pMemoryList', POINTER(VOID)),
            ('Reserved fields up to this point present since the 3.50 release. *  Reserved fields below were introduced for Windows 2000 release. *  (but not used). * International character support information - NT 5.1 feature. INT_PTR                         pCSInfo', POINTER()),
            ('ConformanceMark', POINTER(UCHAR)),
            ('VarianceMark', POINTER(UCHAR)),
            ('Unused', INT_PTR),
            ('pContext', POINTER(_NDR_PROC_CONTEXT)),
            ('Reserved fields up to this point present since Windows 2000 release. *  Fields added for NT5.1 *  pUserMarshalList is used to keep a linked list of nodes pointing to *  marshalled data to be freed.  This list can contain (as the name *  implies) User Marshalled data', POINTER()),
            ('but also can contain Interface Pointer *  data. VOID *                             ContextHandleHash', POINTER()),
            ('pUserMarshalList', POINTER(VOID)),
            ('Reserved51_3', INT_PTR),
            ('Reserved51_4', INT_PTR),
            ('Reserved51_5', INT_PTR),
        ]
        # /* Generic handle bind/unbind routine pair.
# typedef VOID  *
# ( __RPC_API * GENERIC_BINDING_ROUTINE)
# (VOID  *);
        *GENERIC_BINDING_ROUTINE = __RPC_API(
            *,            POINTER(),        )
# typedef void
# ( __RPC_API * GENERIC_UNBIND_ROUTINE)
# (VOID  *, UCHAR  *);
        *GENERIC_UNBIND_ROUTINE = __RPC_API(
            void,            POINTER(),            POINTER(),        )
        _GENERIC_BINDING_ROUTINE_PAIR._fields_ = [
            ('pfnBind', GENERIC_BINDING_ROUTINE),
            ('pfnUnbind', GENERIC_UNBIND_ROUTINE),
        ]
        __GENERIC_BINDING_INFO._fields_ = [
            ('pObj', POINTER(VOID)),
            ('Size', UINT),
            ('pfnBind', GENERIC_BINDING_ROUTINE),
            ('pfnUnbind', GENERIC_UNBIND_ROUTINE),
        ]
        # typedef EXPR_EVAL - see above
        # typedefs for xmit_as
        if defined(_MSC_VER)) and not defined(MIDL_PASS:
            # a Microsoft C + + compiler
            NDR_SHAREABLE = __inline
        else:
            NDR_SHAREABLE = static
        # END IF
# typedef VOID ( __RPC_USER * XMIT_HELPER_ROUTINE)
# ( PMIDL_STUB_MESSAGE );
        XMIT_HELPER_ROUTINE = __RPC_USER(
            VOID,            PMIDL_STUB_MESSAGE,        )


        _XMIT_ROUTINE_QUINTUPLE._fields_ = [
            ('pfnTranslateToXmit', XMIT_HELPER_ROUTINE),
            ('pfnTranslateFromXmit', XMIT_HELPER_ROUTINE),
            ('pfnFreeXmit', XMIT_HELPER_ROUTINE),
            ('pfnFreeInst', XMIT_HELPER_ROUTINE),
        ]

# typedef UINT long
# ( __RPC_USER * USER_MARSHAL_SIZING_ROUTINE)
# (unsigned LONG  *,
# UINT long,
# VOID  * );
        *USER_MARSHAL_SIZING_ROUTINE = __RPC_USER(
            long,            POINTER(),            UINT,            POINTER(),        )


# typedef UCHAR  *
# ( __RPC_USER * USER_MARSHAL_MARSHALLING_ROUTINE)
# (unsigned LONG  *,
# UCHAR  * ,
# VOID  * );
        *USER_MARSHAL_MARSHALLING_ROUTINE = __RPC_USER(
            *,            POINTER(),            POINTER(),            POINTER(),        )


# typedef UCHAR  *
# ( __RPC_USER * USER_MARSHAL_UNMARSHALLING_ROUTINE)
# (unsigned LONG  *,
# UCHAR  *,
# VOID  * );
        *USER_MARSHAL_UNMARSHALLING_ROUTINE = __RPC_USER(
            *,            POINTER(),            POINTER(),            POINTER(),        )


# typedef VOID ( __RPC_USER * USER_MARSHAL_FREEING_ROUTINE)
# (unsigned LONG  *,
# VOID  * );
        USER_MARSHAL_FREEING_ROUTINE = __RPC_USER(
            VOID,            POINTER(),            POINTER(),        )


        _USER_MARSHAL_ROUTINE_QUADRUPLE._fields_ = [
            ('pfnBufferSize', USER_MARSHAL_SIZING_ROUTINE),
            ('pfnMarshall', USER_MARSHAL_MARSHALLING_ROUTINE),
            ('pfnUnmarshall', USER_MARSHAL_UNMARSHALLING_ROUTINE),
            ('pfnFree', USER_MARSHAL_FREEING_ROUTINE),
        ]
        USER_MARSHAL_CB_SIGNATURE = 'USRC'


        class _USER_MARSHAL_CB_TYPE(ENUM):
            USER_MARSHAL_CB_BUFFER_SIZE = 1
            USER_MARSHAL_CB_MARSHALL = 2
            USER_MARSHAL_CB_UNMARSHALL = 3
            USER_MARSHAL_CB_FREE = 4

        USER_MARSHAL_CB_TYPE = _USER_MARSHAL_CB_TYPE

        _USER_MARSHAL_CB._fields_ = [
            ('Flags', ULONG),
            ('pStubMsg', PMIDL_STUB_MESSAGE),
            ('pReserve', PFORMAT_STRING),
            ('Signature', ULONG),
            ('CBType', USER_MARSHAL_CB_TYPE),
            ('pFormat', PFORMAT_STRING),
            ('pTypeFormat', PFORMAT_STRING),
        ]
        

        def USER_CALL_CTXT_MASK(f):
            return (f & 0x00FF)
        

        def USER_CALL_AUX_MASK(f):
            return (f & 0xFF00)
        

        def GET_USER_DATA_REP(f):
            return (f >> 16)
        USER_CALL_IS_ASYNC = 0x0100        # aux flag: in an [async] call
        USER_CALL_NEW_CORRELATION_DESC = 0x0200


        _MALLOC_FREE_STRUCT._fields_ = [
            ('( __RPC_USER * pfnAllocate)(size_t)', POINTER(VOID)),
            ('( __RPC_USER * pfnFree)(VOID  *)', VOID),
        ]

        _COMM_FAULT_OFFSETS._fields_ = [
            ('CommOffset', SHORT),
            ('FaultOffset', SHORT),
        ]

        # /* International character support definitions
        class _IDL_CS_CONVERT(ENUM):
            IDL_CS_NO_CONVERT = 1
            IDL_CS_IN_PLACE_CONVERT = 2
            IDL_CS_NEW_BUFFER_CONVERT = 3

        IDL_CS_CONVERT = _IDL_CS_CONVERT

# typedef void
# ( __RPC_USER * CS_TYPE_NET_SIZE_ROUTINE)
# (RPC_BINDING_HANDLE     hBinding,
# ULONG          ulNetworkCodeSet,
# ULONG          ulLocalBufferSize,
# IDL_CS_CONVERT     *   conversionType,
# ULONG      *   pulNetworkBufferSize,
# error_status_t     *   pStatus);
        *CS_TYPE_NET_SIZE_ROUTINE = __RPC_USER(
            void,            ,            ,            ,            ,            ,            ,        )


# typedef void
# ( __RPC_USER * CS_TYPE_LOCAL_SIZE_ROUTINE)
# (RPC_BINDING_HANDLE     hBinding,
# ULONG          ulNetworkCodeSet,
# ULONG          ulNetworkBufferSize,
# IDL_CS_CONVERT     *   conversionType,
# ULONG      *   pulLocalBufferSize,
# error_status_t     *   pStatus);
        *CS_TYPE_LOCAL_SIZE_ROUTINE = __RPC_USER(
            void,            ,            ,            ,            ,            ,            ,        )


# typedef void
# ( __RPC_USER * CS_TYPE_TO_NETCS_ROUTINE)
# (RPC_BINDING_HANDLE     hBinding,
# ULONG          ulNetworkCodeSet,
# VOID               *   pLocalData,
# ULONG          ulLocalDataLength,
# byte               *   pNetworkData,
# ULONG      *   pulNetworkDataLength,
# error_status_t     *   pStatus);
        *CS_TYPE_TO_NETCS_ROUTINE = __RPC_USER(
            void,            ,            ,            ,            ,            ,            ,            ,        )


# typedef void
# ( __RPC_USER * CS_TYPE_FROM_NETCS_ROUTINE)
# (RPC_BINDING_HANDLE     hBinding,
# ULONG          ulNetworkCodeSet,
# byte               *   pNetworkData,
# ULONG          ulNetworkDataLength,
# ULONG          ulLocalBufferSize,
# VOID               *   pLocalData,
# ULONG      *   pulLocalDataLength,
# error_status_t     *   pStatus);
        *CS_TYPE_FROM_NETCS_ROUTINE = __RPC_USER(
            void,            ,            ,            ,            ,            ,            ,            ,            ,        )


# typedef void
# ( __RPC_USER * CS_TAG_GETTING_ROUTINE)
# (RPC_BINDING_HANDLE     hBinding,
# INT                    fServerSide,
# ULONG      *   pulSendingTag,
# ULONG      *   pulDesiredReceivingTag,
# ULONG      *   pulReceivingTag,
# error_status_t     *   pStatus);
        *CS_TAG_GETTING_ROUTINE = __RPC_USER(
            void,            ,            ,            ,            ,            ,            ,        )


        _NDR_CS_SIZE_CONVERT_ROUTINES._fields_ = [
            ('pfnNetSize', CS_TYPE_NET_SIZE_ROUTINE),
            ('pfnToNetCs', CS_TYPE_TO_NETCS_ROUTINE),
            ('pfnLocalSize', CS_TYPE_LOCAL_SIZE_ROUTINE),
            ('pfnFromNetCs', CS_TYPE_FROM_NETCS_ROUTINE),
        ]

        _NDR_CS_ROUTINES._fields_ = [
            ('pSizeConvertRoutines', POINTER(NDR_CS_SIZE_CONVERT_ROUTINES)),
            ('pTagGettingRoutines', POINTER(CS_TAG_GETTING_ROUTINE)),
        ]

        _NDR_EXPR_DESC._fields_ = [
            ('pOffset', POINTER(USHORT)),
            ('pFormatExpr', PFORMAT_STRING),
        ]

        # /* MIDL Stub Descriptor
        _MIDL_STUB_DESC._fields_ = [
            ('RpcInterfaceInformation', POINTER(VOID)),
            ('( __RPC_API * pfnAllocate)(size_t)', POINTER(VOID)),
            ('( __RPC_API * pfnFree)(VOID  *)', VOID),
            ('pAutoHandle', POINTER(handle_t)),
            ('pPrimitiveHandle', POINTER(handle_t)),
            ('pGenericBindingInfo', PGENERIC_BINDING_INFO),
            ('IMPLICIT_HANDLE_INFO', }),
            ('apfnNdrRundownRoutines', POINTER(NDR_RUNDOWN)),
            ('aGenericBindingRoutinePairs', POINTER(GENERIC_BINDING_ROUTINE_PAIR)),
            ('apfnExprEval', POINTER(EXPR_EVAL)),
            ('aXmitQuintuple', POINTER(XMIT_ROUTINE_QUINTUPLE)),
            ('pFormatTypes', POINTER(UCHAR)),
            ('fCheckBounds', INT),

            # Ndr library version.
            ('Version', ULONG),
            ('pMallocFreeStruct', POINTER(MALLOC_FREE_STRUCT)),
            ('MIDLVersion', LONG),
            ('CommFaultOffsets', POINTER(COMM_FAULT_OFFSETS)),

            # New fields for version 3.0 +
            ('aUserMarshalQuadruple', POINTER(USER_MARSHAL_ROUTINE_QUADRUPLE)),

            # Notify routines - added for NT5, MIDL 5.0
            ('NotifyRoutineTable', POINTER(NDR_NOTIFY_ROUTINE)),
            ('Reserved for future use. ULONG_PTR                               mFlags', POINTER()),

            # International support routines - added for 64bit post NT5
            ('CsRoutineTables', POINTER(NDR_CS_ROUTINES)),
            ('ProxyServerInfo', POINTER(VOID)),
            ('pExprInfo', POINTER(NDR_EXPR_DESC)),
        ]
        # /* MIDL Stub Format String. This is a in the stub.
                if _MSC_VER >= 1200:
                    pass
                # END IF
            if not defined( RC_INVOKED ):
                pass
            # END IF
        if defined(_MSC_EXTENSIONS):
            _MIDL_FORMAT_STRING._fields_ = [
                ('Pad', SHORT),
                ('Format', UCHAR * ),
            ]
                if _MSC_VER >= 1200:
                    pass
                else:
                    pass
                # END IF
            if not defined( RC_INVOKED ):
                pass
            # END IF
        # END IF  _MSC_EXTENSIONS
        # /* Stub thunk used for some interpreted server stubs.
# typedef VOID ( __RPC_API * STUB_THUNK)( PMIDL_STUB_MESSAGE );
        STUB_THUNK = __RPC_API(
            VOID,        )


        if not defined(_MANAGED):
# typedef LONG ( __RPC_API * SERVER_ROUTINE)();
            SERVER_ROUTINE = __RPC_API(
                LONG,            )


        else:
# typedef LONG ( __RPC_API * SERVER_ROUTINE)(VOID);
            SERVER_ROUTINE = __RPC_API(
                LONG,            )


        # END IF
        # /* Method property structures
        _MIDL_METHOD_PROPERTY._fields_ = [
            ('Id', ULONG),
            ('Value', ULONG_PTR),
        ]

        _MIDL_METHOD_PROPERTY_MAP._fields_ = [
            ('Count', ULONG),
            ('Properties', POINTER(MIDL_METHOD_PROPERTY)),
        ]

        _MIDL_INTERFACE_METHOD_PROPERTIES._fields_ = [
            ('MethodCount', USHORT),
            ('MethodProperties', POINTER(POINTER(MIDL_METHOD_PROPERTY_MAP))),
        ]

        # /* Server Interpreter's information strucuture.
        _MIDL_SERVER_INFO_._fields_ = [
            ('pStubDesc', PMIDL_STUB_DESC),
            ('DispatchTable', POINTER(SERVER_ROUTINE)),
            ('ProcString', PFORMAT_STRING),
            ('FmtStringOffset', POINTER(USHORT)),
            ('ThunkTable', POINTER(STUB_THUNK)),
            ('pTransferSyntax', PRPC_SYNTAX_IDENTIFIER),
            ('nCount', ULONG_PTR),
            ('pSyntaxInfo', PMIDL_SYNTAX_INFO),
        ]

        # /* Stubless object proxy information structure.
        _MIDL_STUBLESS_PROXY_INFO._fields_ = [
            ('pStubDesc', PMIDL_STUB_DESC),
            ('ProcFormatString', PFORMAT_STRING),
            ('FormatStringOffset', POINTER(USHORT)),
            ('pTransferSyntax', PRPC_SYNTAX_IDENTIFIER),
            ('nCount', ULONG_PTR),
            ('pSyntaxInfo', PMIDL_SYNTAX_INFO),
        ]

        # /* Multiple transfer syntax information.
        _MIDL_SYNTAX_INFO._fields_ = [
            ('TransferSyntax', RPC_SYNTAX_IDENTIFIER),
            ('DispatchTable', POINTER(RPC_DISPATCH_TABLE)),
            ('ProcString', PFORMAT_STRING),
            ('FmtStringOffset', POINTER(USHORT)),
            ('TypeString', PFORMAT_STRING),
            ('aUserMarshalQuadruple', POINTER(VOID)),
            ('pMethodProperties', POINTER(MIDL_INTERFACE_METHOD_PROPERTIES)),
            ('pReserved2', ULONG_PTR),
        ]

        # /* This is the return value from NdrClientCall.
        _CLIENT_CALL_RETURN._fields_ = [
            ('Pointer', POINTER(VOID)),
            ('Simple', LONG_PTR),
        ]

        # BUGBUG: can we get rid of this defintion altogether, just leave VOID
        # * here?
        class XLAT_SIDE(ENUM):
            XLAT_SERVER = 1
            XLAT_CLIENT = 2

        XLAT_SERVER = XLAT_SIDE.XLAT_SERVER
        XLAT_CLIENT = XLAT_SIDE.XLAT_CLIENT

        _FULL_PTR_XLAT_TABLES._fields_ = [
            ('RefIdToPointer', POINTER(VOID)),
            ('PointerToRefId', POINTER(VOID)),
            ('NextRefId', ULONG),
            ('XlatSide', XLAT_SIDE),
        ]

        # /* Different types of System Handles
        class _system_handle_t(ENUM):
            SYSTEM_HANDLE_FILE = 0
            SYSTEM_HANDLE_SEMAPHORE = 1
            SYSTEM_HANDLE_EVENT = 2
            SYSTEM_HANDLE_MUTEX = 3
            SYSTEM_HANDLE_PROCESS = 4
            SYSTEM_HANDLE_TOKEN = 5
            SYSTEM_HANDLE_SECTION = 6
            SYSTEM_HANDLE_REG_KEY = 7
            SYSTEM_HANDLE_THREAD = 8
            SYSTEM_HANDLE_COMPOSITION_OBJECT = 9
            SYSTEM_HANDLE_SOCKET = 10
            SYSTEM_HANDLE_JOB = 11
            SYSTEM_HANDLE_PIPE = 12
            SYSTEM_HANDLE_MAX = 12
            SYSTEM_HANDLE_INVALID = 0xFF

        system_handle_t = _system_handle_t

        # /* Interception info.
        MidlInterceptionInfoVersionOne = 1
        MidlWinrtTypeSerializationInfoVersionOne = 1
        MIDL_WINRT_TYPE_SERIALIZATION_INFO_CURRENT_VERSION = (
            MidlWinrtTypeSerializationInfoVersionOne
        )


        _MIDL_INTERCEPTION_INFO._fields_ = [
            ('Version', ULONG),
            ('ProcString', PFORMAT_STRING),
            ('ProcFormatOffsetTable', POINTER(USHORT)),
            ('ProcCount', ULONG),
            ('TypeString', PFORMAT_STRING),
        ]

        _MIDL_WINRT_TYPE_SERIALIZATION_INFO._fields_ = [
            ('Version', ULONG),
            ('TypeFormatString', PFORMAT_STRING),
            ('FormatStringSize', USHORT),
            ('TypeOffset', USHORT),
            ('StubDesc', PMIDL_STUB_DESC),
        ]

        # ************************************************************************* * New MIDL 2.0 Ndr routine templates ************************************************************************
        # 
        # /* Marshall routines
        # SAL can't adequately express buffer sizes from rpc format strings
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrSimpleTypeMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # UCHAR           FormatChar
        # );
        NdrSimpleTypeMarshall = rpcrt4.NdrSimpleTypeMarshall
        NdrSimpleTypeMarshall.restype = void


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrPointerMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrPointerMarshall = rpcrt4.NdrPointerMarshall
        NdrPointerMarshall.restype = *


        # Structures
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrSimpleStructMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrSimpleStructMarshall = rpcrt4.NdrSimpleStructMarshall
        NdrSimpleStructMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantStructMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantStructMarshall = rpcrt4.NdrConformantStructMarshall
        NdrConformantStructMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantVaryingStructMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingStructMarshall = (
            rpcrt4.NdrConformantVaryingStructMarshall
        )
        NdrConformantVaryingStructMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrComplexStructMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexStructMarshall = rpcrt4.NdrComplexStructMarshall
        NdrComplexStructMarshall.restype = *


        # Arrays
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrFixedArrayMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrFixedArrayMarshall = rpcrt4.NdrFixedArrayMarshall
        NdrFixedArrayMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantArrayMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantArrayMarshall = rpcrt4.NdrConformantArrayMarshall
        NdrConformantArrayMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantVaryingArrayMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingArrayMarshall = (
            rpcrt4.NdrConformantVaryingArrayMarshall
        )
        NdrConformantVaryingArrayMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrVaryingArrayMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrVaryingArrayMarshall = rpcrt4.NdrVaryingArrayMarshall
        NdrVaryingArrayMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrComplexArrayMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexArrayMarshall = rpcrt4.NdrComplexArrayMarshall
        NdrComplexArrayMarshall.restype = *


        # Strings
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrNonConformantStringMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrNonConformantStringMarshall = rpcrt4.NdrNonConformantStringMarshall
        NdrNonConformantStringMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantStringMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantStringMarshall = rpcrt4.NdrConformantStringMarshall
        NdrConformantStringMarshall.restype = *


        # Unions
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrEncapsulatedUnionMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrEncapsulatedUnionMarshall = rpcrt4.NdrEncapsulatedUnionMarshall
        NdrEncapsulatedUnionMarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrNonEncapsulatedUnionMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrNonEncapsulatedUnionMarshall = (
            rpcrt4.NdrNonEncapsulatedUnionMarshall
        )
        NdrNonEncapsulatedUnionMarshall.restype = *


        # Byte count pointer
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrByteCountPointerMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrByteCountPointerMarshall = rpcrt4.NdrByteCountPointerMarshall
        NdrByteCountPointerMarshall.restype = *


        # Transmit as and represent as
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrXmitOrRepAsMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrXmitOrRepAsMarshall = rpcrt4.NdrXmitOrRepAsMarshall
        NdrXmitOrRepAsMarshall.restype = *


        # User_marshal
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrUserMarshalMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrUserMarshalMarshall = rpcrt4.NdrUserMarshalMarshall
        NdrUserMarshalMarshall.restype = *


        # Interface pointer
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrInterfacePointerMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrInterfacePointerMarshall = rpcrt4.NdrInterfacePointerMarshall
        NdrInterfacePointerMarshall.restype = *


        # Context handles
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrClientContextMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # NDR_CCONTEXT            ContextHandle,
        # INT                     fCheck
        # );
        NdrClientContextMarshall = rpcrt4.NdrClientContextMarshall
        NdrClientContextMarshall.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrServerContextMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # NDR_SCONTEXT            ContextHandle,
        # NDR_RUNDOWN             RundownRoutine
        # );
        NdrServerContextMarshall = rpcrt4.NdrServerContextMarshall
        NdrServerContextMarshall.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrServerContextNewMarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # NDR_SCONTEXT            ContextHandle,
        # NDR_RUNDOWN             RundownRoutine,
        # PFORMAT_STRING          pFormat
        # );
        NdrServerContextNewMarshall = rpcrt4.NdrServerContextNewMarshall
        NdrServerContextNewMarshall.restype = void


        # /* Unmarshall routines
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrSimpleTypeUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # UCHAR           FormatChar
        # );
        NdrSimpleTypeUnmarshall = rpcrt4.NdrSimpleTypeUnmarshall
        NdrSimpleTypeUnmarshall.restype = void


        # RPCRTAPI
        # UCHAR *
        # RPC_ENTRY
        # NdrRangeUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR **        ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrRangeUnmarshall = rpcrt4.NdrRangeUnmarshall
        NdrRangeUnmarshall.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrCorrelationInitialize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # VOID  *                 pMemory,
        # ULONG           CacheSize,
        # ULONG           flags
        # );
        NdrCorrelationInitialize = rpcrt4.NdrCorrelationInitialize
        NdrCorrelationInitialize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrCorrelationPass(
        # PMIDL_STUB_MESSAGE      pStubMsg
        # );
        NdrCorrelationPass = rpcrt4.NdrCorrelationPass
        NdrCorrelationPass.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrCorrelationFree(
        # PMIDL_STUB_MESSAGE      pStubMsg
        # );
        NdrCorrelationFree = rpcrt4.NdrCorrelationFree
        NdrCorrelationFree.restype = void


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrPointerUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrPointerUnmarshall = rpcrt4.NdrPointerUnmarshall
        NdrPointerUnmarshall.restype = *


        # Structures
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrSimpleStructUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrSimpleStructUnmarshall = rpcrt4.NdrSimpleStructUnmarshall
        NdrSimpleStructUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantStructUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrConformantStructUnmarshall = rpcrt4.NdrConformantStructUnmarshall
        NdrConformantStructUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantVaryingStructUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrConformantVaryingStructUnmarshall = (
            rpcrt4.NdrConformantVaryingStructUnmarshall
        )
        NdrConformantVaryingStructUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrComplexStructUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrComplexStructUnmarshall = rpcrt4.NdrComplexStructUnmarshall
        NdrComplexStructUnmarshall.restype = *


        # Arrays
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrFixedArrayUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrFixedArrayUnmarshall = rpcrt4.NdrFixedArrayUnmarshall
        NdrFixedArrayUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantArrayUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrConformantArrayUnmarshall = rpcrt4.NdrConformantArrayUnmarshall
        NdrConformantArrayUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantVaryingArrayUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrConformantVaryingArrayUnmarshall = (
            rpcrt4.NdrConformantVaryingArrayUnmarshall
        )
        NdrConformantVaryingArrayUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrVaryingArrayUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrVaryingArrayUnmarshall = rpcrt4.NdrVaryingArrayUnmarshall
        NdrVaryingArrayUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrComplexArrayUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrComplexArrayUnmarshall = rpcrt4.NdrComplexArrayUnmarshall
        NdrComplexArrayUnmarshall.restype = *


        # Strings
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrNonConformantStringUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrNonConformantStringUnmarshall = (
            rpcrt4.NdrNonConformantStringUnmarshall
        )
        NdrNonConformantStringUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrConformantStringUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrConformantStringUnmarshall = rpcrt4.NdrConformantStringUnmarshall
        NdrConformantStringUnmarshall.restype = *


        # Unions
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrEncapsulatedUnionUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrEncapsulatedUnionUnmarshall = rpcrt4.NdrEncapsulatedUnionUnmarshall
        NdrEncapsulatedUnionUnmarshall.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrNonEncapsulatedUnionUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrNonEncapsulatedUnionUnmarshall = (
            rpcrt4.NdrNonEncapsulatedUnionUnmarshall
        )
        NdrNonEncapsulatedUnionUnmarshall.restype = *


        # Byte count pointer
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrByteCountPointerUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrByteCountPointerUnmarshall = rpcrt4.NdrByteCountPointerUnmarshall
        NdrByteCountPointerUnmarshall.restype = *


        # Transmit as and represent as
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrXmitOrRepAsUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrXmitOrRepAsUnmarshall = rpcrt4.NdrXmitOrRepAsUnmarshall
        NdrXmitOrRepAsUnmarshall.restype = *


        # User_marshal
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrUserMarshalUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrUserMarshalUnmarshall = rpcrt4.NdrUserMarshalUnmarshall
        NdrUserMarshalUnmarshall.restype = *


        # Interface pointer
        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrInterfacePointerUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *  *     ppMemory,
        # PFORMAT_STRING          pFormat,
        # UCHAR           fMustAlloc
        # );
        NdrInterfacePointerUnmarshall = rpcrt4.NdrInterfacePointerUnmarshall
        NdrInterfacePointerUnmarshall.restype = *


        # Context handles
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrClientContextUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # NDR_CCONTEXT        *   pContextHandle,
        # RPC_BINDING_HANDLE      BindHandle
        # );
        NdrClientContextUnmarshall = rpcrt4.NdrClientContextUnmarshall
        NdrClientContextUnmarshall.restype = void


        # RPCRTAPI
        # NDR_SCONTEXT
        # RPC_ENTRY
        # NdrServerContextUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg
        # );
        NdrServerContextUnmarshall = rpcrt4.NdrServerContextUnmarshall
        NdrServerContextUnmarshall.restype = NDR_SCONTEXT


        # New context handle flavors
        # RPCRTAPI
        # NDR_SCONTEXT
        # RPC_ENTRY
        # NdrContextHandleInitialize(
        # _In_  PMIDL_STUB_MESSAGE            pStubMsg,
        # _In_reads_(_Inexpressible_(2)) PFORMAT_STRING      pFormat
        # );
        NdrContextHandleInitialize = rpcrt4.NdrContextHandleInitialize
        NdrContextHandleInitialize.restype = NDR_SCONTEXT


        # RPCRTAPI
        # NDR_SCONTEXT
        # RPC_ENTRY
        # NdrServerContextNewUnmarshall(
        # _In_  PMIDL_STUB_MESSAGE            pStubMsg,
        # _In_reads_(_Inexpressible_(2)) PFORMAT_STRING       pFormat
        # );
        NdrServerContextNewUnmarshall = rpcrt4.NdrServerContextNewUnmarshall
        NdrServerContextNewUnmarshall.restype = NDR_SCONTEXT


        # /* Buffer sizing routines
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrPointerBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrPointerBufferSize = rpcrt4.NdrPointerBufferSize
        NdrPointerBufferSize.restype = void


        # Structures
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrSimpleStructBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrSimpleStructBufferSize = rpcrt4.NdrSimpleStructBufferSize
        NdrSimpleStructBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantStructBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantStructBufferSize = rpcrt4.NdrConformantStructBufferSize
        NdrConformantStructBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantVaryingStructBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingStructBufferSize = (
            rpcrt4.NdrConformantVaryingStructBufferSize
        )
        NdrConformantVaryingStructBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrComplexStructBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexStructBufferSize = rpcrt4.NdrComplexStructBufferSize
        NdrComplexStructBufferSize.restype = void


        # Arrays
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrFixedArrayBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrFixedArrayBufferSize = rpcrt4.NdrFixedArrayBufferSize
        NdrFixedArrayBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantArrayBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantArrayBufferSize = rpcrt4.NdrConformantArrayBufferSize
        NdrConformantArrayBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantVaryingArrayBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingArrayBufferSize = (
            rpcrt4.NdrConformantVaryingArrayBufferSize
        )
        NdrConformantVaryingArrayBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrVaryingArrayBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrVaryingArrayBufferSize = rpcrt4.NdrVaryingArrayBufferSize
        NdrVaryingArrayBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrComplexArrayBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexArrayBufferSize = rpcrt4.NdrComplexArrayBufferSize
        NdrComplexArrayBufferSize.restype = void


        # Strings
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantStringBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantStringBufferSize = rpcrt4.NdrConformantStringBufferSize
        NdrConformantStringBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrNonConformantStringBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrNonConformantStringBufferSize = (
            rpcrt4.NdrNonConformantStringBufferSize
        )
        NdrNonConformantStringBufferSize.restype = void


        # Unions
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrEncapsulatedUnionBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrEncapsulatedUnionBufferSize = rpcrt4.NdrEncapsulatedUnionBufferSize
        NdrEncapsulatedUnionBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrNonEncapsulatedUnionBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrNonEncapsulatedUnionBufferSize = (
            rpcrt4.NdrNonEncapsulatedUnionBufferSize
        )
        NdrNonEncapsulatedUnionBufferSize.restype = void


        # Byte count pointer
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrByteCountPointerBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrByteCountPointerBufferSize = rpcrt4.NdrByteCountPointerBufferSize
        NdrByteCountPointerBufferSize.restype = void


        # Transmit as and represent as
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrXmitOrRepAsBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrXmitOrRepAsBufferSize = rpcrt4.NdrXmitOrRepAsBufferSize
        NdrXmitOrRepAsBufferSize.restype = void


        # User_marshal
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrUserMarshalBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrUserMarshalBufferSize = rpcrt4.NdrUserMarshalBufferSize
        NdrUserMarshalBufferSize.restype = void


        # Interface pointer
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrInterfacePointerBufferSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrInterfacePointerBufferSize = rpcrt4.NdrInterfacePointerBufferSize
        NdrInterfacePointerBufferSize.restype = void


        # Context Handle size
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrContextHandleSize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrContextHandleSize = rpcrt4.NdrContextHandleSize
        NdrContextHandleSize.restype = void


        # /* Memory sizing routines
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrPointerMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrPointerMemorySize = rpcrt4.NdrPointerMemorySize
        NdrPointerMemorySize.restype = long


        rpcrt4 = ctypes.windll.RPCRT4


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrContextHandleMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrContextHandleMemorySize = rpcrt4.NdrContextHandleMemorySize
        NdrContextHandleMemorySize.restype = long


        # cs_char things
        # Structures
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrSimpleStructMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrSimpleStructMemorySize = rpcrt4.NdrSimpleStructMemorySize
        NdrSimpleStructMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrConformantStructMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantStructMemorySize = rpcrt4.NdrConformantStructMemorySize
        NdrConformantStructMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrConformantVaryingStructMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingStructMemorySize = (
            rpcrt4.NdrConformantVaryingStructMemorySize
        )
        NdrConformantVaryingStructMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrComplexStructMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexStructMemorySize = rpcrt4.NdrComplexStructMemorySize
        NdrComplexStructMemorySize.restype = long


        # Arrays
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrFixedArrayMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrFixedArrayMemorySize = rpcrt4.NdrFixedArrayMemorySize
        NdrFixedArrayMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrConformantArrayMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantArrayMemorySize = rpcrt4.NdrConformantArrayMemorySize
        NdrConformantArrayMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrConformantVaryingArrayMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingArrayMemorySize = (
            rpcrt4.NdrConformantVaryingArrayMemorySize
        )
        NdrConformantVaryingArrayMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrVaryingArrayMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrVaryingArrayMemorySize = rpcrt4.NdrVaryingArrayMemorySize
        NdrVaryingArrayMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrComplexArrayMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexArrayMemorySize = rpcrt4.NdrComplexArrayMemorySize
        NdrComplexArrayMemorySize.restype = long


        # Strings
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrConformantStringMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantStringMemorySize = rpcrt4.NdrConformantStringMemorySize
        NdrConformantStringMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrNonConformantStringMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrNonConformantStringMemorySize = (
            rpcrt4.NdrNonConformantStringMemorySize
        )
        NdrNonConformantStringMemorySize.restype = long


        # Unions
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrEncapsulatedUnionMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrEncapsulatedUnionMemorySize = rpcrt4.NdrEncapsulatedUnionMemorySize
        NdrEncapsulatedUnionMemorySize.restype = long


        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrNonEncapsulatedUnionMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrNonEncapsulatedUnionMemorySize = (
            rpcrt4.NdrNonEncapsulatedUnionMemorySize
        )
        NdrNonEncapsulatedUnionMemorySize.restype = long


        # Transmit as and represent as
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrXmitOrRepAsMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrXmitOrRepAsMemorySize = rpcrt4.NdrXmitOrRepAsMemorySize
        NdrXmitOrRepAsMemorySize.restype = long


        # User_marshal
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrUserMarshalMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrUserMarshalMemorySize = rpcrt4.NdrUserMarshalMemorySize
        NdrUserMarshalMemorySize.restype = long


        # Interface pointer
        # RPCRTAPI
        # UINT long
        # RPC_ENTRY
        # NdrInterfacePointerMemorySize(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrInterfacePointerMemorySize = rpcrt4.NdrInterfacePointerMemorySize
        NdrInterfacePointerMemorySize.restype = long


        # /* Freeing routines
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrPointerFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrPointerFree = rpcrt4.NdrPointerFree
        NdrPointerFree.restype = void


        # Structures
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrSimpleStructFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrSimpleStructFree = rpcrt4.NdrSimpleStructFree
        NdrSimpleStructFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantStructFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantStructFree = rpcrt4.NdrConformantStructFree
        NdrConformantStructFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantVaryingStructFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingStructFree = rpcrt4.NdrConformantVaryingStructFree
        NdrConformantVaryingStructFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrComplexStructFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexStructFree = rpcrt4.NdrComplexStructFree
        NdrComplexStructFree.restype = void


        # Arrays
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrFixedArrayFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrFixedArrayFree = rpcrt4.NdrFixedArrayFree
        NdrFixedArrayFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantArrayFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantArrayFree = rpcrt4.NdrConformantArrayFree
        NdrConformantArrayFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConformantVaryingArrayFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrConformantVaryingArrayFree = rpcrt4.NdrConformantVaryingArrayFree
        NdrConformantVaryingArrayFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrVaryingArrayFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrVaryingArrayFree = rpcrt4.NdrVaryingArrayFree
        NdrVaryingArrayFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrComplexArrayFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrComplexArrayFree = rpcrt4.NdrComplexArrayFree
        NdrComplexArrayFree.restype = void


        # Unions
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrEncapsulatedUnionFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrEncapsulatedUnionFree = rpcrt4.NdrEncapsulatedUnionFree
        NdrEncapsulatedUnionFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrNonEncapsulatedUnionFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrNonEncapsulatedUnionFree = rpcrt4.NdrNonEncapsulatedUnionFree
        NdrNonEncapsulatedUnionFree.restype = void


        # Byte count
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrByteCountPointerFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrByteCountPointerFree = rpcrt4.NdrByteCountPointerFree
        NdrByteCountPointerFree.restype = void


        # Transmit as and represent as
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrXmitOrRepAsFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrXmitOrRepAsFree = rpcrt4.NdrXmitOrRepAsFree
        NdrXmitOrRepAsFree.restype = void


        # User_marshal
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrUserMarshalFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrUserMarshalFree = rpcrt4.NdrUserMarshalFree
        NdrUserMarshalFree.restype = void


        # Interface pointer
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrInterfacePointerFree(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pMemory,
        # PFORMAT_STRING          pFormat
        # );
        NdrInterfacePointerFree = rpcrt4.NdrInterfacePointerFree
        NdrInterfacePointerFree.restype = void


        # /* Endian conversion routine.
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConvert2(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat,
        # LONG                    NumberParams
        # );
        NdrConvert2 = rpcrt4.NdrConvert2
        NdrConvert2.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrConvert(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat
        # );
        NdrConvert = rpcrt4.NdrConvert
        NdrConvert.restype = void


        USER_MARSHAL_FC_BYTE = 1
        USER_MARSHAL_FC_CHAR = 2
        USER_MARSHAL_FC_SMALL = 3
        USER_MARSHAL_FC_USMALL = 4
        USER_MARSHAL_FC_WCHAR = 5
        USER_MARSHAL_FC_SHORT = 6
        USER_MARSHAL_FC_USHORT = 7
        USER_MARSHAL_FC_LONG = 8
        USER_MARSHAL_FC_ULONG = 9
        USER_MARSHAL_FC_FLOAT = 10
        USER_MARSHAL_FC_HYPER = 11
        USER_MARSHAL_FC_DOUBLE = 12

        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrUserMarshalSimpleTypeConvert(
        # ULONG *         pFlags,
        # UCHAR *         pBuffer,
        # UCHAR           FormatChar
        # );
        NdrUserMarshalSimpleTypeConvert = (
            rpcrt4.NdrUserMarshalSimpleTypeConvert
        )
        NdrUserMarshalSimpleTypeConvert.restype = *


        # /* Auxilary routines
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrClientInitializeNew(
        # PRPC_MESSAGE            pRpcMsg,
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PMIDL_STUB_DESC         pStubDescriptor,
        # UINT            ProcNum
        # );
        NdrClientInitializeNew = rpcrt4.NdrClientInitializeNew
        NdrClientInitializeNew.restype = void


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrServerInitializeNew(
        # PRPC_MESSAGE            pRpcMsg,
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PMIDL_STUB_DESC         pStubDescriptor
        # );
        NdrServerInitializeNew = rpcrt4.NdrServerInitializeNew
        NdrServerInitializeNew.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrServerInitializePartial(
        # PRPC_MESSAGE            pRpcMsg,
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PMIDL_STUB_DESC         pStubDescriptor,
        # ULONG           RequestedBufferSize
        # );
        NdrServerInitializePartial = rpcrt4.NdrServerInitializePartial
        NdrServerInitializePartial.restype = void


        msrpc = ctypes.windll.MSRPC


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrClientInitialize(
        # PRPC_MESSAGE            pRpcMsg,
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PMIDL_STUB_DESC         pStubDescriptor,
        # UINT            ProcNum
        # );
        NdrClientInitialize = msrpc.NdrClientInitialize
        NdrClientInitialize.restype = void


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrServerInitialize(
        # PRPC_MESSAGE            pRpcMsg,
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PMIDL_STUB_DESC         pStubDescriptor
        # );
        NdrServerInitialize = rpcrt4.NdrServerInitialize
        NdrServerInitialize.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrServerInitializeUnmarshall(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PMIDL_STUB_DESC         pStubDescriptor,
        # PRPC_MESSAGE            pRpcMsg
        # );
        NdrServerInitializeUnmarshall = rpcrt4.NdrServerInitializeUnmarshall
        NdrServerInitializeUnmarshall.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrServerInitializeMarshall(
        # PRPC_MESSAGE            pRpcMsg,
        # PMIDL_STUB_MESSAGE      pStubMsg
        # );
        NdrServerInitializeMarshall = rpcrt4.NdrServerInitializeMarshall
        NdrServerInitializeMarshall.restype = void


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrGetBuffer(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # ULONG           BufferLength,
        # RPC_BINDING_HANDLE      Handle
        # );
        NdrGetBuffer = rpcrt4.NdrGetBuffer
        NdrGetBuffer.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrNsGetBuffer(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # ULONG           BufferLength,
        # RPC_BINDING_HANDLE      Handle
        # );
        NdrNsGetBuffer = rpcrt4.NdrNsGetBuffer
        NdrNsGetBuffer.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrSendReceive(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR *         pBufferEnd
        # );
        NdrSendReceive = rpcrt4.NdrSendReceive
        NdrSendReceive.restype = *


        # RPCRTAPI
        # UCHAR  *
        # RPC_ENTRY
        # NdrNsSendReceive(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # UCHAR  *        pBufferEnd,
        # RPC_BINDING_HANDLE  *   pAutoHandle
        # );
        NdrNsSendReceive = rpcrt4.NdrNsSendReceive
        NdrNsSendReceive.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrFreeBuffer(
        # PMIDL_STUB_MESSAGE      pStubMsg
        # );
        NdrFreeBuffer = rpcrt4.NdrFreeBuffer
        NdrFreeBuffer.restype = void


        # RPCRTAPI
        # HRESULT
        # RPC_ENTRY
        # NdrGetDcomProtocolVersion(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # RPC_VERSION *           pVersion );
        NdrGetDcomProtocolVersion = rpcrt4.NdrGetDcomProtocolVersion
        NdrGetDcomProtocolVersion.restype = HRESULT


        # /* Interpreter calls.
        # client
        # CLIENT_CALL_RETURN RPC_VAR_ENTRY
        # NdrClientCall2(
        # PMIDL_STUB_DESC         pStubDescriptor,
        # PFORMAT_STRING          pFormat,
        # ...
        # );
        NdrClientCall2 = msrpc.NdrClientCall2
        NdrClientCall2.restype = RPC_VAR_ENTRY


        # CLIENT_CALL_RETURN RPC_VAR_ENTRY
        # NdrClientCall(
        # PMIDL_STUB_DESC         pStubDescriptor,
        # PFORMAT_STRING          pFormat,
        # ...
        # );
        NdrClientCall = rpcrt4.NdrClientCall
        NdrClientCall.restype = RPC_VAR_ENTRY


        # CLIENT_CALL_RETURN RPC_VAR_ENTRY
        # NdrAsyncClientCall(
        # PMIDL_STUB_DESC         pStubDescriptor,
        # PFORMAT_STRING          pFormat,
        # ...
        # );
        NdrAsyncClientCall = rpcrt4.NdrAsyncClientCall
        NdrAsyncClientCall.restype = RPC_VAR_ENTRY


            rpcrt4 = ctypes.windll.RPCRT4

        if  not defined(_WIN64) and not defined(_ARM_) :
            # CLIENT_CALL_RETURN RPC_VAR_ENTRY
            # NdrClientCall4(
            # PMIDL_STUB_DESC         pStubDescriptor,
            # PFORMAT_STRING          pFormat,
            # ...
            # );
            NdrClientCall4 = rpcrt4.NdrClientCall4
            NdrClientCall4.restype = RPC_VAR_ENTRY


            # CLIENT_CALL_RETURN RPC_VAR_ENTRY
            # NdrAsyncClientCall2(
            # PMIDL_STUB_DESC         pStubDescriptor,
            # PFORMAT_STRING          pFormat,
            # ...
            # );
            NdrAsyncClientCall2 = rpcrt4.NdrAsyncClientCall2
            NdrAsyncClientCall2.restype = RPC_VAR_ENTRY


            # CLIENT_CALL_RETURN RPC_VAR_ENTRY
            # NdrMesProcEncodeDecode4(
            # handle_t                Handle,
            # MIDL_STUB_DESC *  pStubDescriptor,
            # PFORMAT_STRING          pFormat,
            # ...
            # );
            NdrMesProcEncodeDecode4 = rpcrt4.NdrMesProcEncodeDecode4
            NdrMesProcEncodeDecode4.restype = RPC_VAR_ENTRY

        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        rpcrt4 = ctypes.windll.RPCRT4

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # CLIENT_CALL_RETURN RPC_VAR_ENTRY
        # NdrDcomAsyncClientCall(
        # PMIDL_STUB_DESC         pStubDescriptor,
        # PFORMAT_STRING          pFormat,
        # ...
        # );
        NdrDcomAsyncClientCall = rpcrt4.NdrDcomAsyncClientCall
        NdrDcomAsyncClientCall.restype = RPC_VAR_ENTRY


            rpcrt4 = ctypes.windll.RPCRT4

        if  not defined(_WIN64) and not defined(_ARM_) :
            # CLIENT_CALL_RETURN  RPC_VAR_ENTRY
            # NdrDcomAsyncClientCall2(
            # PMIDL_STUB_DESC         pStubDescriptor,
            # PFORMAT_STRING          pFormat,
            # ...
            # );
            NdrDcomAsyncClientCall2 = rpcrt4.NdrDcomAsyncClientCall2
            NdrDcomAsyncClientCall2.restype = RPC_VAR_ENTRY

        # END IF
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # server
        class STUB_PHASE(ENUM):
            STUB_UNMARSHAL = 1
            STUB_CALL_SERVER = 2
            STUB_MARSHAL = 3
            STUB_CALL_SERVER_NO_HRESULT = 4

        STUB_UNMARSHAL = STUB_PHASE.STUB_UNMARSHAL
        STUB_CALL_SERVER = STUB_PHASE.STUB_CALL_SERVER
        STUB_MARSHAL = STUB_PHASE.STUB_MARSHAL
        STUB_CALL_SERVER_NO_HRESULT = STUB_PHASE.STUB_CALL_SERVER_NO_HRESULT


        class PROXY_PHASE(ENUM):
            PROXY_CALCSIZE = 1
            PROXY_GETBUFFER = 2
            PROXY_MARSHAL = 3
            PROXY_SENDRECEIVE = 4
            PROXY_UNMARSHAL = 5

        PROXY_CALCSIZE = PROXY_PHASE.PROXY_CALCSIZE
        PROXY_GETBUFFER = PROXY_PHASE.PROXY_GETBUFFER
        PROXY_MARSHAL = PROXY_PHASE.PROXY_MARSHAL
        PROXY_SENDRECEIVE = PROXY_PHASE.PROXY_SENDRECEIVE
        PROXY_UNMARSHAL = PROXY_PHASE.PROXY_UNMARSHAL
        declaration = Forward


        # Raw RPC only
        rpcrt4 = ctypes.windll.RPCRT4


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrAsyncServerCall(
        # PRPC_MESSAGE                pRpcMsg
        # );
        NdrAsyncServerCall = rpcrt4.NdrAsyncServerCall
        NdrAsyncServerCall.restype = void


        # old dcom async scheme
        ) = IRpcStubBuffer *     pThis,  IRpcChannelBuffer *  pChannel,                PRPC_MESSAGE                pRpcMsg,                ULONG *             pdwStubPhase
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # async uuid
        rpcrt4 = ctypes.windll.RPCRT4


        # RPCRTAPI
        # long
        # RPC_ENTRY
        # NdrDcomAsyncStubCall(
        # struct IRpcStubBuffer    *  pThis,
        # struct IRpcChannelBuffer *  pChannel,
        # PRPC_MESSAGE                pRpcMsg,
        # ULONG            *  pdwStubPhase
        # );
        NdrDcomAsyncStubCall = rpcrt4.NdrDcomAsyncStubCall
        NdrDcomAsyncStubCall.restype = long

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
        rpcrt4 = ctypes.windll.RPCRT4

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # RPCRTAPI
        # long
        # RPC_ENTRY
        # NdrStubCall2(
        # VOID  *    pThis, // struct IRpcStubBuffer
        # VOID  * pChannel, // struct IRpcChannelBuffer
        # PRPC_MESSAGE                pRpcMsg,
        # ULONG  *            pdwStubPhase
        # );
        NdrStubCall2 = rpcrt4.NdrStubCall2
        NdrStubCall2.restype = long


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrServerCall2(
        # PRPC_MESSAGE                pRpcMsg
        # );
        NdrServerCall2 = rpcrt4.NdrServerCall2
        NdrServerCall2.restype = void

        # struct IRpcStubBuffer        # struct IRpcChannelBuffer        # Converted to struct IRpcChannelBuffer        # Converted to struct IRpcStubBuffer        # Converted to struct IRpcChannelBuffer
        # Comm and Fault status
        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # NdrMapCommAndFaultStatus(
        # PMIDL_STUB_MESSAGE          pStubMsg,
        # ULONG  *            pCommStatus,
        # ULONG  *            pFaultStatus,
        # RPC_STATUS                  Status
        # );
        NdrMapCommAndFaultStatus = rpcrt4.NdrMapCommAndFaultStatus
        NdrMapCommAndFaultStatus.restype = RPC_STATUS


        # ************************************************************************** MIDL 2.0 memory package: rpc_ss_* rpc_sm_* *************************************************************************
        # 
# typedef VOID  * __RPC_API
# RPC_CLIENT_ALLOC (
# _In_ size_t Size
# );
        [] = CALLBACK(
            ,            size_t,        )


# typedef VOID __RPC_API
# RPC_CLIENT_FREE (
# _In_ VOID  * Ptr
# );
        [] = CALLBACK(
            ,            POINTER(),        )


        # /* + + RpcSs* package - -
        # RPCRTAPI
        # VOID  *
        # RPC_ENTRY
        # RpcSsAllocate(
        # _In_ size_t Size
        # );
        RpcSsAllocate = rpcrt4.RpcSsAllocate
        RpcSsAllocate.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # RpcSsDisableAllocate(
        # void
        # );
        RpcSsDisableAllocate = rpcrt4.RpcSsDisableAllocate
        RpcSsDisableAllocate.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # RpcSsEnableAllocate(
        # void
        # );
        RpcSsEnableAllocate = rpcrt4.RpcSsEnableAllocate
        RpcSsEnableAllocate.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # RpcSsFree(
        # _In_ VOID  * NodeToFree
        # );
        RpcSsFree = rpcrt4.RpcSsFree
        RpcSsFree.restype = void


        # RPCRTAPI
        # RPC_SS_THREAD_HANDLE
        # RPC_ENTRY
        # RpcSsGetThreadHandle(
        # void
        # );
        RpcSsGetThreadHandle = rpcrt4.RpcSsGetThreadHandle
        RpcSsGetThreadHandle.restype = RPC_SS_THREAD_HANDLE


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # RpcSsSetClientAllocFree(
        # _In_ RPC_CLIENT_ALLOC  * ClientAlloc,
        # _In_ RPC_CLIENT_FREE   * ClientFree
        # );
        RpcSsSetClientAllocFree = rpcrt4.RpcSsSetClientAllocFree
        RpcSsSetClientAllocFree.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # RpcSsSetThreadHandle(
        # _In_ RPC_SS_THREAD_HANDLE Id
        # );
        RpcSsSetThreadHandle = rpcrt4.RpcSsSetThreadHandle
        RpcSsSetThreadHandle.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # RpcSsSwapClientAllocFree(
        # _In_ RPC_CLIENT_ALLOC     * ClientAlloc,
        # _In_ RPC_CLIENT_FREE      * ClientFree,
        # _Out_ RPC_CLIENT_ALLOC *  * OldClientAlloc,
        # _Out_ RPC_CLIENT_FREE  *  * OldClientFree
        # );
        RpcSsSwapClientAllocFree = rpcrt4.RpcSsSwapClientAllocFree
        RpcSsSwapClientAllocFree.restype = void


        # /* + + RpcSm* package - -
        # RPCRTAPI
        # VOID  *
        # RPC_ENTRY
        # RpcSmAllocate(
        # _In_  size_t          Size,
        # _Out_ RPC_STATUS  *   pStatus
        # );
        RpcSmAllocate = rpcrt4.RpcSmAllocate
        RpcSmAllocate.restype = *


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmClientFree(
        # _In_  VOID        *   pNodeToFree
        # );
        RpcSmClientFree = rpcrt4.RpcSmClientFree
        RpcSmClientFree.restype = RPC_STATUS


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmDestroyClientContext(
        # _In_ VOID         * * ContextHandle
        # );
        RpcSmDestroyClientContext = rpcrt4.RpcSmDestroyClientContext
        RpcSmDestroyClientContext.restype = RPC_STATUS


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmDisableAllocate(
        # void
        # );
        RpcSmDisableAllocate = rpcrt4.RpcSmDisableAllocate
        RpcSmDisableAllocate.restype = RPC_STATUS


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmEnableAllocate(
        # void
        # );
        RpcSmEnableAllocate = rpcrt4.RpcSmEnableAllocate
        RpcSmEnableAllocate.restype = RPC_STATUS


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmFree(
        # _In_ VOID         *   NodeToFree
        # );
        RpcSmFree = rpcrt4.RpcSmFree
        RpcSmFree.restype = RPC_STATUS


        # RPCRTAPI
        # RPC_SS_THREAD_HANDLE
        # RPC_ENTRY
        # RpcSmGetThreadHandle(
        # _Out_ RPC_STATUS  *   pStatus
        # );
        RpcSmGetThreadHandle = rpcrt4.RpcSmGetThreadHandle
        RpcSmGetThreadHandle.restype = RPC_SS_THREAD_HANDLE


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmSetClientAllocFree(
        # _In_ RPC_CLIENT_ALLOC * ClientAlloc,
        # _In_ RPC_CLIENT_FREE  * ClientFree
        # );
        RpcSmSetClientAllocFree = rpcrt4.RpcSmSetClientAllocFree
        RpcSmSetClientAllocFree.restype = RPC_STATUS


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmSetThreadHandle(
        # _In_ RPC_SS_THREAD_HANDLE Id
        # );
        RpcSmSetThreadHandle = rpcrt4.RpcSmSetThreadHandle
        RpcSmSetThreadHandle.restype = RPC_STATUS


        # RPCRTAPI
        # RPC_STATUS
        # RPC_ENTRY
        # RpcSmSwapClientAllocFree(
        # _In_ RPC_CLIENT_ALLOC     *   ClientAlloc,
        # _In_ RPC_CLIENT_FREE      *   ClientFree,
        # _Out_ RPC_CLIENT_ALLOC    * * OldClientAlloc,
        # _Out_ RPC_CLIENT_FREE     * * OldClientFree
        # );
        RpcSmSwapClientAllocFree = rpcrt4.RpcSmSwapClientAllocFree
        RpcSmSwapClientAllocFree.restype = RPC_STATUS


        # /* + + Ndr stub entry points - -
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrRpcSsEnableAllocate(
        # PMIDL_STUB_MESSAGE      pMessage );
        NdrRpcSsEnableAllocate = rpcrt4.NdrRpcSsEnableAllocate
        NdrRpcSsEnableAllocate.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrRpcSsDisableAllocate(
        # PMIDL_STUB_MESSAGE      pMessage );
        NdrRpcSsDisableAllocate = rpcrt4.NdrRpcSsDisableAllocate
        NdrRpcSsDisableAllocate.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrRpcSmSetClientToOsf(
        # PMIDL_STUB_MESSAGE      pMessage );
        NdrRpcSmSetClientToOsf = rpcrt4.NdrRpcSmSetClientToOsf
        NdrRpcSmSetClientToOsf.restype = void


        # RPCRTAPI
        # VOID  *
        # RPC_ENTRY
        # NdrRpcSmClientAllocate(
        # _In_ size_t Size
        # );
        NdrRpcSmClientAllocate = rpcrt4.NdrRpcSmClientAllocate
        NdrRpcSmClientAllocate.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrRpcSmClientFree(
        # _In_ VOID  * NodeToFree
        # );
        NdrRpcSmClientFree = rpcrt4.NdrRpcSmClientFree
        NdrRpcSmClientFree.restype = void


        # RPCRTAPI
        # VOID  *
        # RPC_ENTRY
        # NdrRpcSsDefaultAllocate(
        # _In_ size_t Size
        # );
        NdrRpcSsDefaultAllocate = rpcrt4.NdrRpcSsDefaultAllocate
        NdrRpcSsDefaultAllocate.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrRpcSsDefaultFree(
        # _In_ VOID  * NodeToFree
        # );
        NdrRpcSsDefaultFree = rpcrt4.NdrRpcSsDefaultFree
        NdrRpcSsDefaultFree.restype = void


        # ************************************************************************** end of memory package: rpc_ss_* rpc_sm_* *************************************************************************
        # 
        # ************************************************************************** Full Pointer APIs *************************************************************************
        # 
        # RPCRTAPI
        # PFULL_PTR_XLAT_TABLES
        # RPC_ENTRY
        # NdrFullPointerXlatInit(
        # ULONG           NumberOfPointers,
        # XLAT_SIDE               XlatSide
        # );
        NdrFullPointerXlatInit = rpcrt4.NdrFullPointerXlatInit
        NdrFullPointerXlatInit.restype = PFULL_PTR_XLAT_TABLES


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrFullPointerXlatFree(
        # PFULL_PTR_XLAT_TABLES   pXlatTables
        # );
        NdrFullPointerXlatFree = rpcrt4.NdrFullPointerXlatFree
        NdrFullPointerXlatFree.restype = void


        msrpc = ctypes.windll.MSRPC


        # RPCRTAPI
        # VOID  *
        # RPC_ENTRY
        # NdrAllocate(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # size_t                  Len
        # );
        NdrAllocate = msrpc.NdrAllocate
        NdrAllocate.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrClearOutParameters(
        # PMIDL_STUB_MESSAGE      pStubMsg,
        # PFORMAT_STRING          pFormat,
        # VOID  *                 ArgAddr
        # );
        NdrClearOutParameters = rpcrt4.NdrClearOutParameters
        NdrClearOutParameters.restype = void


        # ************************************************************************** Proxy APIs *************************************************************************
        # 
        # RPCRTAPI
        # VOID  *
        # RPC_ENTRY
        # NdrOleAllocate(
        # _In_ size_t Size
        # );
        NdrOleAllocate = rpcrt4.NdrOleAllocate
        NdrOleAllocate.restype = *


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrOleFree(
        # _In_ VOID  * NodeToFree
        # );
        NdrOleFree = rpcrt4.NdrOleFree
        NdrOleFree.restype = void


        if defined(CONST_VTABLE):
            CONST_VTBL = const
        else:
            #~#~#~            #define CONST_VTBL        # END IF
        # ************************************************************************** VC COM support *************************************************************************
        # 
        if not defined(DECLSPEC_SELECTANY):
            if _MSC_VER >= 1100:
                DECLSPEC_SELECTANY = __declspec(selectany)
            else:
                #~#~#~                #define DECLSPEC_SELECTANY            # END IF
        # END IF
        if not defined(DECLSPEC_NOVTABLE):
            if _MSC_VER >= 1100) and defined(__cplusplus:
                DECLSPEC_NOVTABLE = __declspec(novtable)
            else:
                #~#~#~                #define DECLSPEC_NOVTABLE            # END IF
        # END IF
        if not defined(DECLSPEC_UUID):
            if _MSC_VER >= 1100) and defined(__cplusplus:
                def DECLSPEC_UUID(x):
                    return __declspec(uuidx)
            else:
                #~#~#~                #define DECLSPEC_UUID(x)            # END IF
        # END IF
        def MIDL_INTERFACE(x):
            return struct DECLSPEC_UUIDx DECLSPEC_NOVTABLE
        if _MSC_VER >= 1100:
            def EXTERN_GUID(itf, l1, s1, s2, c1, c2, c3, c4, c5, c6, c7, c8):
                return EXTERN_C IID DECLSPEC_SELECTANY itf = {l1,s1,s2,{c1,c2,c3,c4,c5,c6,c7,c8}}
        else:
            def EXTERN_GUID(itf, l1, s1, s2, c1, c2, c3, c4, c5, c6, c7, c8):
                return EXTERN_C IID itf
        # END IF
        # ************************************************************************** UserMarshal information *************************************************************************
        # 
        _NDR_USER_MARSHAL_INFO_LEVEL1._fields_ = [
            ('Buffer', POINTER(VOID)),
            ('BufferSize', ULONG),
            ('(__RPC_API * pfnAllocate)(size_t)', POINTER(VOID)),
            ('(__RPC_API * pfnFree)(VOID *)', VOID),
            ('pRpcChannelBuffer', POINTER(IRpcChannelBuffer)),
            ('Reserved', ULONG_PTR * 5),
        ]
            if _MSC_VER >= 1200:
                pass
            # END IF
        if not defined( RC_INVOKED ):
            pass
        # END IF
        class DUMMYUNIONNAME(ctypes.Union):
            pass


        DUMMYUNIONNAME._fields_ = [
            ('Level1', NDR_USER_MARSHAL_INFO_LEVEL1),
        ]
        _NDR_USER_MARSHAL_INFO.DUMMYUNIONNAME = DUMMYUNIONNAME


        _NDR_USER_MARSHAL_INFO._fields_ = [
            ('InformationLevel', ULONG),
            ('DUMMYUNIONNAME', _NDR_USER_MARSHAL_INFO.DUMMYUNIONNAME),
        ]
            if _MSC_VER >= 1200:
                pass
            else:
                pass
            # END IF
        if not defined( RC_INVOKED ):
            pass
        # END IF
        # RPC_STATUS
        # RPC_ENTRY
        # NdrGetUserMarshalInfo(
        # _In_ ULONG * pFlags,
        # _In_ ULONG            InformationLevel,
        # _Out_ NDR_USER_MARSHAL_INFO * pMarshalInfo
        # );
        NdrGetUserMarshalInfo = rpcrt4.NdrGetUserMarshalInfo
        NdrGetUserMarshalInfo.restype = RPC_ENTRY


        # ************************************************************************** 64bit APIs *************************************************************************
        # 
        # RPC_STATUS RPC_ENTRY
        # NdrCreateServerInterfaceFromStub(
        # _In_ struct IRpcStubBuffer* pStub,
        # _Inout_ RPC_SERVER_INTERFACE *pServerIf );
        NdrCreateServerInterfaceFromStub = (
            rpcrt4.NdrCreateServerInterfaceFromStub
        )
        NdrCreateServerInterfaceFromStub.restype = RPC_ENTRY


        # /* Interpreter calls
        # CLIENT_CALL_RETURN RPC_VAR_ENTRY
        # NdrClientCall3(
        # MIDL_STUBLESS_PROXY_INFO   *pProxyInfo,
        # ULONG               nProcNum,
        # VOID *                      pReturnValue,
        # ...
        # );
        NdrClientCall3 = rpcrt4.NdrClientCall3
        NdrClientCall3.restype = RPC_VAR_ENTRY


        # CLIENT_CALL_RETURN RPC_VAR_ENTRY
        # Ndr64AsyncClientCall(
        # MIDL_STUBLESS_PROXY_INFO   *pProxyInfo,
        # ULONG               nProcNum,
        # VOID *                      pReturnValue,
        # ...
        # );
        Ndr64AsyncClientCall = rpcrt4.Ndr64AsyncClientCall
        Ndr64AsyncClientCall.restype = RPC_VAR_ENTRY

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        rpcrt4 = ctypes.windll.RPCRT4

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # CLIENT_CALL_RETURN RPC_VAR_ENTRY
        # Ndr64DcomAsyncClientCall(
        # MIDL_STUBLESS_PROXY_INFO   *pProxyInfo,
        # ULONG               nProcNum,
        # VOID *                      pReturnValue,
        # ...
        # );
        Ndr64DcomAsyncClientCall = rpcrt4.Ndr64DcomAsyncClientCall
        Ndr64DcomAsyncClientCall.restype = RPC_VAR_ENTRY

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        declaration = Forward

        rpcrt4 = ctypes.windll.RPCRT4


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # Ndr64AsyncServerCall64(
        # PRPC_MESSAGE                pRpcMsg
        # );
        Ndr64AsyncServerCall64 = rpcrt4.Ndr64AsyncServerCall64
        Ndr64AsyncServerCall64.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # Ndr64AsyncServerCallAll(
        # PRPC_MESSAGE                pRpcMsg
        # );
        Ndr64AsyncServerCallAll = rpcrt4.Ndr64AsyncServerCallAll
        Ndr64AsyncServerCallAll.restype = void


        ) = IRpcStubBuffer *     pThis,  IRpcChannelBuffer *  pChannel,                PRPC_MESSAGE                pRpcMsg,                ULONG *             pdwStubPhase
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # async uuid
        rpcrt4 = ctypes.windll.RPCRT4


        # RPCRTAPI
        # long
        # RPC_ENTRY
        # Ndr64DcomAsyncStubCall(
        # struct IRpcStubBuffer    *  pThis,
        # struct IRpcChannelBuffer *  pChannel,
        # PRPC_MESSAGE                pRpcMsg,
        # ULONG            *  pdwStubPhase
        # );
        Ndr64DcomAsyncStubCall = rpcrt4.Ndr64DcomAsyncStubCall
        Ndr64DcomAsyncStubCall.restype = long

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
        rpcrt4 = ctypes.windll.RPCRT4

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # RPCRTAPI
        # long
        # RPC_ENTRY
        # NdrStubCall3(
        # VOID  *    pThis, // struct IRpcStubBuffer
        # VOID  * pChannel, // struct IRpcChannelBuffer
        # PRPC_MESSAGE                pRpcMsg,
        # ULONG  *            pdwStubPhase
        # );
        NdrStubCall3 = rpcrt4.NdrStubCall3
        NdrStubCall3.restype = long


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrServerCallAll(
        # PRPC_MESSAGE                pRpcMsg
        # );
        NdrServerCallAll = rpcrt4.NdrServerCallAll
        NdrServerCallAll.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrServerCallNdr64(
        # PRPC_MESSAGE                pRpcMsg
        # );
        NdrServerCallNdr64 = rpcrt4.NdrServerCallNdr64
        NdrServerCallNdr64.restype = void


        # [partial_ignore] functions
        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrPartialIgnoreClientMarshall(
        # PMIDL_STUB_MESSAGE          pStubMsg,
        # VOID *                      pMemory
        # );
        NdrPartialIgnoreClientMarshall = rpcrt4.NdrPartialIgnoreClientMarshall
        NdrPartialIgnoreClientMarshall.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrPartialIgnoreServerUnmarshall(
        # PMIDL_STUB_MESSAGE          pStubMsg,
        # VOID **                     ppMemory
        # );
        NdrPartialIgnoreServerUnmarshall = (
            rpcrt4.NdrPartialIgnoreServerUnmarshall
        )
        NdrPartialIgnoreServerUnmarshall.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrPartialIgnoreClientBufferSize(
        # PMIDL_STUB_MESSAGE          pStubMsg,
        # VOID *                      pMemory
        # );
        NdrPartialIgnoreClientBufferSize = (
            rpcrt4.NdrPartialIgnoreClientBufferSize
        )
        NdrPartialIgnoreClientBufferSize.restype = void


        # RPCRTAPI
        # void
        # RPC_ENTRY
        # NdrPartialIgnoreServerInitialize(
        # PMIDL_STUB_MESSAGE          pStubMsg,
        # VOID **                     ppMemory,
        # PFORMAT_STRING              pFormat
        # );
        NdrPartialIgnoreServerInitialize = (
            rpcrt4.NdrPartialIgnoreServerInitialize
        )
        NdrPartialIgnoreServerInitialize.restype = void


        # VOID RPC_ENTRY
        # RpcUserFree( handle_t AsyncHandle, VOID * pBuffer );
        RpcUserFree = rpcrt4.RpcUserFree
        RpcUserFree.restype = RPC_ENTRY

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    if defined(__cplusplus):
        pass
    # END IF
    from poppack_h import * # NOQA
# END IF  __RPCNDR_H__
if _MSC_VER >= 1200:
    pass
# END IF
