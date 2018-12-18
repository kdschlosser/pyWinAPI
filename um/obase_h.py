import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
__obase_h__ = None
__ObjectRpcBaseTypes_INTERFACE_DEFINED__ = None


class tagCOMVERSION(ctypes.Structure):
    pass


COMVERSION = tagCOMVERSION


class tagORPC_EXTENT(ctypes.Structure):
    pass


ORPC_EXTENT = tagORPC_EXTENT


class tagORPC_EXTENT_ARRAY(ctypes.Structure):
    pass


ORPC_EXTENT_ARRAY = tagORPC_EXTENT_ARRAY


class tagORPCTHIS(ctypes.Structure):
    pass


ORPCTHIS = tagORPCTHIS


class tagORPCTHAT(ctypes.Structure):
    pass


ORPCTHAT = tagORPCTHAT


class tagSTRINGBINDING(ctypes.Structure):
    pass


STRINGBINDING = tagSTRINGBINDING


class tagSECURITYBINDING(ctypes.Structure):
    pass


SECURITYBINDING = tagSECURITYBINDING


class tagDUALSTRINGARRAY(ctypes.Structure):
    pass


DUALSTRINGARRAY = tagDUALSTRINGARRAY


class tagSTDOBJREF(ctypes.Structure):
    pass


STDOBJREF = tagSTDOBJREF


class tagDATAELEMENT(ctypes.Structure):
    pass


DATAELEMENT = tagDATAELEMENT


class tagOBJREFDATA(ctypes.Structure):
    pass


OBJREFDATA = tagOBJREFDATA


class tagOBJREF(ctypes.Structure):
    pass


OBJREF = tagOBJREF


class tagMInterfacePointer(ctypes.Structure):
    pass


MInterfacePointer = tagMInterfacePointer


class tagOXID_INFO(ctypes.Structure):
    pass


OXID_INFO = tagOXID_INFO


class tagOpaqueData(ctypes.Structure):
    pass


OpaqueData = tagOpaqueData


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    __REQUIRED_RPCNDR_H_VERSION__ = 500
# END IF


# verify that the <rpcsal.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    __REQUIRED_RPCSAL_H_VERSION__ = 100
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

if not defined(__obase_h__):
    __obase_h__ = VOID
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    # header files for imported files
    if defined(__cplusplus):
        pass
    # END IF

    if not defined(__ObjectRpcBaseTypes_INTERFACE_DEFINED__):
        __ObjectRpcBaseTypes_INTERFACE_DEFINED__ = VOID

        # interface ObjectRpcBaseTypes
        # [unique][uuid]
        ID = VOID
        MID = ID
        OXID = ID
        OID = ID
        SETID = ID
        IPID = GUID
        CID = GUID
        REFIPID = REFGUID
        APTID = DWORD
        PROCID = DWORD
        CTXTID = DWORD
        COM_MINOR_VERSION_1 = 1
        COM_MAJOR_VERSION = 5
        COM_MINOR_VERSION = 7

        tagCOMVERSION._fields_ = [
            ('MajorVersion', USHORT),
            ('MinorVersion', USHORT),
        ]
        ORPCF_NULL = 0
        ORPCF_LOCAL = 1
        ORPCF_RESERVED1 = 2
        ORPCF_RESERVED2 = 4
        ORPCF_RESERVED3 = 8
        ORPCF_RESERVED4 = 0x10
        ORPCF_RESERVED5 = 0x20
        ORPCF_RESERVED6 = 0x40

        tagORPC_EXTENT._fields_ = [
            ('id', GUID),
            ('size', ULONG),
            # [size_is]
            ('data', BYTE * 1),
        ]

        tagORPC_EXTENT_ARRAY._fields_ = [
            ('size', ULONG),
            ('reserved', ULONG),
            # [unique][size_is][size_is]
            ('extent', POINTER(POINTER(ORPC_EXTENT))),
        ]

        tagORPCTHIS._fields_ = [
            ('version', COMVERSION),
            ('flags', ULONG),
            ('reserved1', ULONG),
            ('cid', CID),
            # [unique]
            ('extensions', POINTER(ORPC_EXTENT_ARRAY)),
        ]

        tagORPCTHAT._fields_ = [
            ('flags', ULONG),
            # [unique]
            ('extensions', POINTER(ORPC_EXTENT_ARRAY)),
        ]
        NCADG_IP_UDP = 0x8
        NCACN_IP_TCP = 0x7
        NCADG_IPX = 0xE
        NCACN_SPX = 0xC
        NCACN_NB_NB = 0x12
        NCACN_NB_IPX = 0xD
        NCACN_DNET_NSP = 0x4
        NCALRPC = 0x10

        tagSTRINGBINDING._fields_ = [
            ('wTowerId', USHORT),
            ('aNetworkAddr', USHORT),
        ]
        COM_C_AUTHZ_NONE = 0xFFFF

        tagSECURITYBINDING._fields_ = [
            ('wAuthnSvc', USHORT),
            ('wAuthzSvc', USHORT),
            ('aPrincName', USHORT),
        ]

        tagDUALSTRINGARRAY._fields_ = [
            ('wNumEntries', USHORT),
            ('wSecurityOffset', USHORT),
            # [size_is]
            ('aStringArray', USHORT * 1),
        ]
        OBJREF_SIGNATURE = 0x574F454D
        OBJREF_STANDARD = 0x1
        OBJREF_HANDLER = 0x2
        OBJREF_CUSTOM = 0x4
        OBJREF_EXTENDED = 0x8
        SORF_OXRES1 = 0x1
        SORF_OXRES2 = 0x20
        SORF_OXRES3 = 0x40
        SORF_OXRES4 = 0x80
        SORF_OXRES5 = 0x100
        SORF_OXRES6 = 0x200
        SORF_OXRES7 = 0x400
        SORF_OXRES8 = 0x800
        SORF_NULL = 0
        SORF_NOPING = 0x1000
        SORF_RES9 = 0x80000000
        SORF_RES10 = 0x40000000
        SORF_RES11 = 0x20000000

        tagSTDOBJREF._fields_ = [
            ('flags', ULONG),
            ('cPublicRefs', ULONG),
            ('oxid', OXID),
            ('oid', OID),
            ('ipid', IPID),
        ]

        tagDATAELEMENT._fields_ = [
            ('dataID', GUID),
            ('cbSize', ULONG),
            ('cbRounded', ULONG),
            # [size_is]
            ('Data', BYTE * 1),
        ]

        tagOBJREFDATA._fields_ = [
            ('nElms', ULONG),
            # [unique][size_is][size_is]
            ('ppElmArray', POINTER(POINTER(DATAELEMENT))),
        ]


        class u_objref(ctypes.Union):
            pass


        class u_standard(ctypes.Structure):
            pass


        u_standard._fields_ = [
            ('std', STDOBJREF),
            ('saResAddr', DUALSTRINGARRAY),
        ]
        u_objref.u_standard = u_standard


        class u_handler(ctypes.Structure):
            pass


        u_handler._fields_ = [
            ('std', STDOBJREF),
            ('clsid', CLSID),
            ('saResAddr', DUALSTRINGARRAY),
        ]
        u_objref.u_handler = u_handler


        class u_custom(ctypes.Structure):
            pass


        u_custom._fields_ = [
            ('clsid', CLSID),
            ('cbExtension', ULONG),
            ('size', ULONG),
            # [ref][size_is]
            ('pData', POINTER(BYTE)),
        ]
        u_objref.u_custom = u_custom


        class u_extended(ctypes.Structure):
            pass


        u_extended._fields_ = [
            ('std', STDOBJREF),
            # [unique]
            ('pORData', POINTER(OBJREFDATA)),
            ('saResAddr', DUALSTRINGARRAY),
        ]
        u_objref.u_extended = u_extended

        u_objref._fields_ = [
            # [case()]
            ('u_standard', u_objref.u_standard),
            # [case()]
            ('u_handler', u_objref.u_handler),
            # [case()]
            ('u_custom', u_objref.u_custom),
            # [case()]
            ('u_extended', u_objref.u_extended),
        ]
        tagOBJREF.u_objref = u_objref

        tagOBJREF._fields_ = [
            ('signature', ULONG),
            ('flags', ULONG),
            ('iid', GUID),
            # [switch_type][switch_is]
            ('u_objref', tagOBJREF.u_objref),
        ]

        tagMInterfacePointer._fields_ = [
            ('ulCntData', ULONG),
            # [size_is]
            ('abData', BYTE * 1),
        ]

        # [unique]
        PMInterfacePointer = POINTER(MInterfacePointer)

        tagOXID_INFO._fields_ = [
            ('dwTid', DWORD),
            ('dwPid', DWORD),
            ('dwAuthnHint', DWORD),
            ('version', COMVERSION),
            ('ipidRemUnknown', IPID),
            ('dwFlags', DWORD),
            # [unique]
            ('psa', POINTER(DUALSTRINGARRAY)),
            ('guidProcessIdentifier', GUID),
        ]
    # END IF  __ObjectRpcBaseTypes_INTERFACE_DEFINED__

    # interface __MIDL_itf_obase_0000_0001
    # [local]
    tagOpaqueData._fields_ = [
        ('guid', GUID),
        ('dataLength', ULONG),
        ('reserved1', ULONG),
        ('reserved2', ULONG),
        # [size_is]
        ('data', POINTER(BYTE)),
    ]

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


