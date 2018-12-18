import ctypes
import comtypes
import comtypes.automation

from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring
IDispatch = comtypes.automation.IDispatch

__STDC__ = 0
__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__oaidl_h__ = None
__ICreateTypeInfo_FWD_DEFINED__ = None
__ICreateTypeInfo2_FWD_DEFINED__ = None
__ICreateTypeLib_FWD_DEFINED__ = None
__ICreateTypeLib2_FWD_DEFINED__ = None
__IDispatch_FWD_DEFINED__ = None
__IEnumVARIANT_FWD_DEFINED__ = None
__ITypeComp_FWD_DEFINED__ = None
__ITypeInfo_FWD_DEFINED__ = None
__ITypeInfo2_FWD_DEFINED__ = None
__ITypeLib_FWD_DEFINED__ = None
__ITypeLib2_FWD_DEFINED__ = None
__ITypeChangeEvents_FWD_DEFINED__ = None
__IErrorInfo_FWD_DEFINED__ = None
__ICreateErrorInfo_FWD_DEFINED__ = None
__ISupportErrorInfo_FWD_DEFINED__ = None
__ITypeFactory_FWD_DEFINED__ = None
__ITypeMarshal_FWD_DEFINED__ = None
__IRecordInfo_FWD_DEFINED__ = None
__IErrorLog_FWD_DEFINED__ = None
__IPropertyBag_FWD_DEFINED__ = None
__ITypeLibRegistrationReader_FWD_DEFINED__ = None
__ITypeLibRegistration_FWD_DEFINED__ = None
__IOleAutomationTypes_INTERFACE_DEFINED__ = None
_FORCENAMELESSUNION = None
NONAMELESSUNION = None
_MSC_EXTENSIONS = None
_REFVARIANT_DEFINED = None
__ICreateTypeInfo_INTERFACE_DEFINED__ = None
__ICreateTypeInfo2_INTERFACE_DEFINED__ = None
__ICreateTypeLib_INTERFACE_DEFINED__ = None
__ICreateTypeLib2_INTERFACE_DEFINED__ = None
__IDispatch_INTERFACE_DEFINED__ = None
__IEnumVARIANT_INTERFACE_DEFINED__ = None
__ITypeComp_INTERFACE_DEFINED__ = None
__ITypeInfo_INTERFACE_DEFINED__ = None
__ITypeInfo2_INTERFACE_DEFINED__ = None
__ITypeLib_INTERFACE_DEFINED__ = None
__ITypeLib2_INTERFACE_DEFINED__ = None
__ITypeChangeEvents_INTERFACE_DEFINED__ = None
__IErrorInfo_INTERFACE_DEFINED__ = None
__ICreateErrorInfo_INTERFACE_DEFINED__ = None
__ISupportErrorInfo_INTERFACE_DEFINED__ = None
__ITypeFactory_INTERFACE_DEFINED__ = None
__ITypeMarshal_INTERFACE_DEFINED__ = None
__IRecordInfo_INTERFACE_DEFINED__ = None
__IErrorLog_INTERFACE_DEFINED__ = None
__IPropertyBag_INTERFACE_DEFINED__ = None
__ITypeLibRegistrationReader_INTERFACE_DEFINED__ = None
__ITypeLibRegistration_INTERFACE_DEFINED__ = None


class tagSAFEARRAYBOUND(ctypes.Structure):
    pass


SAFEARRAYBOUND = tagSAFEARRAYBOUND


class _wireSAFEARR_BSTR(ctypes.Structure):
    pass


SAFEARR_BSTR = _wireSAFEARR_BSTR


class _wireSAFEARR_UNKNOWN(ctypes.Structure):
    pass


SAFEARR_UNKNOWN = _wireSAFEARR_UNKNOWN


class _wireSAFEARR_DISPATCH(ctypes.Structure):
    pass


SAFEARR_DISPATCH = _wireSAFEARR_DISPATCH


class _wireSAFEARR_VARIANT(ctypes.Structure):
    pass


SAFEARR_VARIANT = _wireSAFEARR_VARIANT


class _wireSAFEARR_BRECORD(ctypes.Structure):
    pass


SAFEARR_BRECORD = _wireSAFEARR_BRECORD


class _wireSAFEARR_HAVEIID(ctypes.Structure):
    pass


SAFEARR_HAVEIID = _wireSAFEARR_HAVEIID


class _wireSAFEARRAY(ctypes.Structure):
    pass

wireSAFEARRAY = _wireSAFEARRAY


class _wireSAFEARRAY_UNION(ctypes.Structure):
    pass


SAFEARRAYUNION = _wireSAFEARRAY_UNION


class tagSAFEARRAY(ctypes.Structure):
    pass


SAFEARRAY = tagSAFEARRAY


class tagVARIANT(ctypes.Structure):
    pass


class _wireBRECORD(ctypes.Structure):
    pass


class _wireVARIANT(ctypes.Structure):
    pass


class tagTYPEDESC(ctypes.Structure):
    pass


TYPEDESC = tagTYPEDESC


class tagARRAYDESC(ctypes.Structure):
    pass


ARRAYDESC = tagARRAYDESC


class tagPARAMDESCEX(ctypes.Structure):
    pass


PARAMDESCEX = tagPARAMDESCEX


class tagPARAMDESC(ctypes.Structure):
    pass


PARAMDESC = tagPARAMDESC


class tagIDLDESC(ctypes.Structure):
    pass


IDLDESC = tagIDLDESC


class tagELEMDESC(ctypes.Structure):
    pass


ELEMDESC = tagELEMDESC


ELEMDESC = tagELEMDESC
LPELEMDESC = POINTER(tagELEMDESC)


class tagTYPEATTR(ctypes.Structure):
    pass


TYPEATTR = tagTYPEATTR


class tagDISPPARAMS(ctypes.Structure):
    pass


DISPPARAMS = tagDISPPARAMS


class tagEXCEPINFO(ctypes.Structure):
    pass


EXCEPINFO = tagEXCEPINFO


EXCEPINFO = tagEXCEPINFO
LPEXCEPINFO = POINTER(tagEXCEPINFO)


class tagFUNCDESC(ctypes.Structure):
    pass


FUNCDESC = tagFUNCDESC


class tagVARDESC(ctypes.Structure):
    pass


VARDESC = tagVARDESC


class tagCLEANLOCALSTORAGE(ctypes.Structure):
    pass


CLEANLOCALSTORAGE = tagCLEANLOCALSTORAGE


class tagCUSTDATAITEM(ctypes.Structure):
    pass


CUSTDATAITEM = tagCUSTDATAITEM


class tagCUSTDATA(ctypes.Structure):
    pass


CUSTDATA = tagCUSTDATA


class tagBINDPTR(ctypes.Union):
    pass


BINDPTR = tagBINDPTR


class tagTLIBATTR(ctypes.Structure):
    pass


TLIBATTR = tagTLIBATTR



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

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

if not defined(__oaidl_h__):
    __oaidl_h__ = VOID
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF


    # Forward Declarations
    if not defined(__ICreateTypeInfo_FWD_DEFINED__):
        __ICreateTypeInfo_FWD_DEFINED__ = VOID


        class ICreateTypeInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICreateTypeInfo_FWD_DEFINED__

    if not defined(__ICreateTypeInfo2_FWD_DEFINED__):
        __ICreateTypeInfo2_FWD_DEFINED__ = VOID


        class ICreateTypeInfo2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICreateTypeInfo2_FWD_DEFINED__

    if not defined(__ICreateTypeLib_FWD_DEFINED__):
        __ICreateTypeLib_FWD_DEFINED__ = VOID


        class ICreateTypeLib(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICreateTypeLib_FWD_DEFINED__

    if not defined(__ICreateTypeLib2_FWD_DEFINED__):
        __ICreateTypeLib2_FWD_DEFINED__ = VOID


        class ICreateTypeLib2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICreateTypeLib2_FWD_DEFINED__

    if not defined(__IDispatch_FWD_DEFINED__):
        __IDispatch_FWD_DEFINED__ = VOID


        class IDispatch(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDispatch_FWD_DEFINED__

    if not defined(__IEnumVARIANT_FWD_DEFINED__):
        __IEnumVARIANT_FWD_DEFINED__ = VOID


        class IEnumVARIANT(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumVARIANT_FWD_DEFINED__

    if not defined(__ITypeComp_FWD_DEFINED__):
        __ITypeComp_FWD_DEFINED__ = VOID


        class ITypeComp(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeComp_FWD_DEFINED__

    if not defined(__ITypeInfo_FWD_DEFINED__):
        __ITypeInfo_FWD_DEFINED__ = VOID


        class ITypeInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeInfo_FWD_DEFINED__

    if not defined(__ITypeInfo2_FWD_DEFINED__):
        __ITypeInfo2_FWD_DEFINED__ = VOID


        class ITypeInfo2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeInfo2_FWD_DEFINED__

    if not defined(__ITypeLib_FWD_DEFINED__):
        __ITypeLib_FWD_DEFINED__ = VOID


        class ITypeLib(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeLib_FWD_DEFINED__

    if not defined(__ITypeLib2_FWD_DEFINED__):
        __ITypeLib2_FWD_DEFINED__ = VOID


        class ITypeLib2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeLib2_FWD_DEFINED__

    if not defined(__ITypeChangeEvents_FWD_DEFINED__):
        __ITypeChangeEvents_FWD_DEFINED__ = VOID


        class ITypeChangeEvents(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeChangeEvents_FWD_DEFINED__

    if not defined(__IErrorInfo_FWD_DEFINED__):
        __IErrorInfo_FWD_DEFINED__ = VOID


        class IErrorInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IErrorInfo_FWD_DEFINED__

    if not defined(__ICreateErrorInfo_FWD_DEFINED__):
        __ICreateErrorInfo_FWD_DEFINED__ = VOID


        class ICreateErrorInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICreateErrorInfo_FWD_DEFINED__

    if not defined(__ISupportErrorInfo_FWD_DEFINED__):
        __ISupportErrorInfo_FWD_DEFINED__ = VOID


        class ISupportErrorInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISupportErrorInfo_FWD_DEFINED__

    if not defined(__ITypeFactory_FWD_DEFINED__):
        __ITypeFactory_FWD_DEFINED__ = VOID


        class ITypeFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeFactory_FWD_DEFINED__

    if not defined(__ITypeMarshal_FWD_DEFINED__):
        __ITypeMarshal_FWD_DEFINED__ = VOID


        class ITypeMarshal(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeMarshal_FWD_DEFINED__

    if not defined(__IRecordInfo_FWD_DEFINED__):
        __IRecordInfo_FWD_DEFINED__ = VOID


        class IRecordInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRecordInfo_FWD_DEFINED__

    if not defined(__IErrorLog_FWD_DEFINED__):
        __IErrorLog_FWD_DEFINED__ = VOID


        class IErrorLog(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IErrorLog_FWD_DEFINED__

    if not defined(__IPropertyBag_FWD_DEFINED__):
        __IPropertyBag_FWD_DEFINED__ = VOID


        class IPropertyBag(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyBag_FWD_DEFINED__

    if not defined(__ITypeLibRegistrationReader_FWD_DEFINED__):
        __ITypeLibRegistrationReader_FWD_DEFINED__ = VOID


        class ITypeLibRegistrationReader(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeLibRegistrationReader_FWD_DEFINED__

    if not defined(__ITypeLibRegistration_FWD_DEFINED__):
        __ITypeLibRegistration_FWD_DEFINED__ = VOID


        class ITypeLibRegistration(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITypeLibRegistration_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.objidl_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    # interface __MIDL_itf_oaidl_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    # +
    # -------------------------------------------------------------------------
    # Microsoft Windows
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # --------------------------------------------------------------------


    if  _MSC_VER >= 800 :
        if _MSC_VER >= 1200:
            pass
        # END IF
    # END IF

    if  _MSC_VER >= 1020 :
        pass
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IOleAutomationTypes_INTERFACE_DEFINED__):
            __IOleAutomationTypes_INTERFACE_DEFINED__ = VOID

            # interface IOleAutomationTypes
            # [unique][version]
            CURRENCY = CY


            tagSAFEARRAYBOUND._fields_ = [
                ('cElements', ULONG),
                ('lLbound', LONG),
            ]
            LPSAFEARRAYBOUND = POINTER(tagSAFEARRAYBOUND)


            # the following is what MIDL knows how to remote
            # [unique]
            wireVARIANT = POINTER(_wireVARIANT)

            # [unique]
            wireBRECORD = POINTER(_wireBRECORD)
            _wireSAFEARR_BSTR._fields_ = [
                ('Size', ULONG),
                # [ref][size_is]
                ('aBstr', POINTER(wireBSTR)),
            ]

            _wireSAFEARR_UNKNOWN._fields_ = [
                ('Size', ULONG),
                # [ref][size_is]
                ('apUnknown', POINTER(POINTER(comtypes.IUnknown))),
            ]

            _wireSAFEARR_DISPATCH._fields_ = [
                ('Size', ULONG),
                # [ref][size_is]
                ('apDispatch', POINTER(POINTER(IDispatch))),
            ]

            _wireSAFEARR_VARIANT._fields_ = [
                ('Size', ULONG),
                # [ref][size_is]
                ('aVariant', POINTER(wireVARIANT)),
            ]

            _wireSAFEARR_BRECORD._fields_ = [
                ('Size', ULONG),
                # [ref][size_is]
                ('aRecord', POINTER(wireBRECORD)),
            ]

            _wireSAFEARR_HAVEIID._fields_ = [
                ('Size', ULONG),
                # [ref][size_is]
                ('apUnknown', POINTER(POINTER(comtypes.IUnknown))),
                ('iid', IID),
            ]

            class tagSF_TYPE(ENUM):
                SF_ERROR = VARENUM.VT_ERROR
                SF_I1 = VARENUM.VT_I1
                SF_I2 = VARENUM.VT_I2
                SF_I4 = VARENUM.VT_I4
                SF_I8 = VARENUM.VT_I8
                SF_BSTR = VARENUM.VT_BSTR
                SF_UNKNOWN = VARENUM.VT_UNKNOWN
                SF_DISPATCH = VARENUM.VT_DISPATCH
                SF_VARIANT = VARENUM.VT_VARIANT
                SF_RECORD = VARENUM.VT_RECORD
                SF_HAVEIID = VARENUM.VT_UNKNOWN | VARENUM.VT_RESERVED

            SF_TYPE = tagSF_TYPE


            class __MIDL_IOleAutomationTypes_0001(ctypes.Union):
                pass


            __MIDL_IOleAutomationTypes_0001._fields_ = [
                # [case()]
                ('BstrStr', SAFEARR_BSTR),
                # [case()]
                ('UnknownStr', SAFEARR_UNKNOWN),
                # [case()]
                ('DispatchStr', SAFEARR_DISPATCH),
                # [case()]
                ('VariantStr', SAFEARR_VARIANT),
                # [case()]
                ('RecordStr', SAFEARR_BRECORD),
                # [case()]
                ('HaveIidStr', SAFEARR_HAVEIID),
                # [case()]
                ('ByteStr', BYTE_SIZEDARR),
                # [case()]
                ('WordStr', WORD_SIZEDARR),
                # [case()]
                ('LongStr', DWORD_SIZEDARR),
                # [case()]
                ('HyperStr', HYPER_SIZEDARR),
            ]
            u = __MIDL_IOleAutomationTypes_0001
            _wireSAFEARRAY_UNION.u = u

            _wireSAFEARRAY_UNION._fields_ = [
                ('sfType', ULONG),
                # [switch_is]
                ('u', _wireSAFEARRAY_UNION.u),
            ]

            _wireSAFEARRAY._fields_ = [
                ('cDims', USHORT),
                ('fFeatures', USHORT),
                ('cbElements', ULONG),
                ('cLocks', ULONG),
                ('uArrayStructs', SAFEARRAYUNION),
                ('rgsabound', SAFEARRAYBOUND * 1),
            ]

            wirePSAFEARRAY = POINTER(wireSAFEARRAY)

            tagSAFEARRAY._fields_ = [
                ('cDims', USHORT),
                ('fFeatures', USHORT),
                ('cbElements', ULONG),
                ('cLocks', ULONG),
                ('pvData', PVOID),
                ('rgsabound', SAFEARRAYBOUND * 1),
            ]
            # [wire_marshal]
            LPSAFEARRAY = POINTER(SAFEARRAY)
            FADF_AUTO = 0x1
            FADF_STATIC = 0x2
            FADF_EMBEDDED = 0x4
            FADF_FIXEDSIZE = 0x10
            FADF_RECORD = 0x20
            FADF_HAVEIID = 0x40
            FADF_HAVEVARTYPE = 0x80
            FADF_BSTR = 0x100
            FADF_UNKNOWN = 0x200
            FADF_DISPATCH = 0x400
            FADF_VARIANT = 0x800
            FADF_RESERVED = 0xF008
            # /* VARIANT STRUCTURE VARTYPE vt; WORD wReserved1; WORD
            # wReserved2; WORD wReserved3; union
            # { LONGLONG VT_I8
            # LONG VT_I4
            # BYTE VT_UI1
            # SHORT VT_I2
            # FLOAT VT_R4
            # DOUBLE VT_R8
            # VARIANT_BOOL VT_BOOL
            # SCODE VT_ERROR
            # CY VT_CY
            # DATE VT_DATE
            # BSTR VT_BSTR
            # IUnknown * VT_UNKNOWN
            # IDispatch * VT_DISPATCH
            # SAFEARRAY * VT_ARRAY
            # BYTE * VT_BYREF | VT_UI1
            # SHORT * VT_BYREF | VT_I2
            # LONG * VT_BYREF | VT_I4
            # LONGLONG * VT_BYREF | VT_I8
            # FLOAT * VT_BYREF | VT_R4
            # DOUBLE * VT_BYREF | VT_R8
            # VARIANT_BOOL * VT_BYREF | VT_BOOL
            # SCODE * VT_BYREF | VT_ERROR
            # CY * VT_BYREF | VT_CY
            # DATE * VT_BYREF | VT_DATE
            # BSTR * VT_BYREF | VT_BSTR
            # IUnknown ** VT_BYREF | VT_UNKNOWN
            # IDispatch ** VT_BYREF | VT_DISPATCH
            # SAFEARRAY ** VT_BYREF | VT_ARRAY
            # VARIANT * VT_BYREF | VT_VARIANT
            # PVOID VT_BYREF (Generic ByRef)
            # CHAR VT_I1
            # USHORT VT_UI2
            # ULONG VT_UI4
            # ULONGLONG VT_UI8
            # INT VT_INT
            # UINT VT_UINT
            # DECIMAL * VT_BYREF | VT_DECIMAL
            # CHAR * VT_BYREF | VT_I1
            # USHORT * VT_BYREF | VT_UI2
            # ULONG * VT_BYREF | VT_UI4
            # ULONGLONG * VT_BYREF | VT_UI8
            # INT * VT_BYREF | VT_INT
            # UINT * VT_BYREF | VT_UINT
            # }
            #
            if (__STDC__ and not defined(_FORCENAMELESSUNION)) or defined(NONAMELESSUNION) or (not defined(_MSC_EXTENSIONS) and not defined(_FORCENAMELESSUNION)):
                __VARIANT_NAME_1 = VOID
                __VARIANT_NAME_2 = VOID
                __VARIANT_NAME_3 = VOID
                __VARIANT_NAME_4 = VOID
            else:
                __tagVARIANT = VOID
                __VARIANT_NAME_1 = VOID
                __VARIANT_NAME_2 = VOID
                __VARIANT_NAME_3 = VOID
                __tagBRECORD = VOID
                __VARIANT_NAME_4 = VOID
            # END IF

            VARIANT = tagVARIANT


            class __VARIANT_NAME_1(ctypes.Union):
                pass


            class __tagVARIANT(ctypes.Structure):
                pass


            class __VARIANT_NAME_3(ctypes.Union):
                pass


            class __tagBRECORD(ctypes.Structure):
                pass


            __tagBRECORD._fields_ = [
                ('pvRecord', PVOID),
                ('pRecInfo', POINTER(IRecordInfo)),
            ]
            __VARIANT_NAME_4 = __tagBRECORD
            __VARIANT_NAME_3.__VARIANT_NAME_4 = __VARIANT_NAME_4


            __VARIANT_NAME_3._fields_ = [
                ('llVal', LONGLONG),
                ('lVal', LONG),
                ('bVal', BYTE),
                ('iVal', SHORT),
                ('fltVal', FLOAT),
                ('dblVal', DOUBLE),
                ('boolVal', VARIANT_BOOL),
                ('bool', _VARIANT_BOOL),
                ('scode', SCODE),
                ('cyVal', CY),
                ('date', DATE),
                ('bstrVal', BSTR),
                ('punkVal', POINTER(comtypes.IUnknown)),
                ('pdispVal', POINTER(IDispatch)),
                ('parray', POINTER(SAFEARRAY)),
                ('pbVal', POINTER(BYTE)),
                ('piVal', POINTER(SHORT)),
                ('plVal', POINTER(LONG)),
                ('pllVal', POINTER(LONGLONG)),
                ('pfltVal', POINTER(FLOAT)),
                ('pdblVal', POINTER(DOUBLE)),
                ('pboolVal', POINTER(VARIANT_BOOL)),
                ('pbool', POINTER(_VARIANT_BOOL)),
                ('pscode', POINTER(SCODE)),
                ('pcyVal', POINTER(CY)),
                ('pdate', POINTER(DATE)),
                ('pbstrVal', POINTER(BSTR)),
                ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))),
                ('ppdispVal', POINTER(POINTER(IDispatch))),
                ('pparray', POINTER(POINTER(SAFEARRAY))),
                ('pvarVal', POINTER(VARIANT)),
                ('byref', PVOID),
                ('cVal', CHAR),
                ('uiVal', USHORT),
                ('ulVal', ULONG),
                ('ullVal', ULONGLONG),
                ('intVal', INT),
                ('uintVal', UINT),
                ('pdecVal', POINTER(DECIMAL)),
                ('pcVal', POINTER(CHAR)),
                ('puiVal', POINTER(USHORT)),
                ('pulVal', POINTER(ULONG)),
                ('pullVal', POINTER(ULONGLONG)),
                ('pintVal', POINTER(INT)),
                ('puintVal', POINTER(UINT)),
                ('__VARIANT_NAME_4', __VARIANT_NAME_3.__VARIANT_NAME_4),
            ]
            __tagVARIANT.__VARIANT_NAME_3 = __VARIANT_NAME_3


            __tagVARIANT._fields_ = [
                ('vt', VARTYPE),
                ('wReserved1', WORD),
                ('wReserved2', WORD),
                ('wReserved3', WORD),
                ('__VARIANT_NAME_3', __tagVARIANT.__VARIANT_NAME_3),
            ]
            __VARIANT_NAME_2 = __tagVARIANT
            __VARIANT_NAME_1.__VARIANT_NAME_2 = __VARIANT_NAME_2


            __VARIANT_NAME_1._fields_ = [
                ('__VARIANT_NAME_2', __VARIANT_NAME_1.__VARIANT_NAME_2),
                ('decVal', DECIMAL),
            ]
            tagVARIANT.__VARIANT_NAME_1 = __VARIANT_NAME_1


            tagVARIANT._fields_ = [
                ('__VARIANT_NAME_1', tagVARIANT.__VARIANT_NAME_1),
            ]
            LPVARIANT = POINTER(VARIANT)
            VARIANTARG = VARIANT
            LPVARIANTARG = POINTER(VARIANT)
            if defined(MIDL_PASS):
                REFVARIANT = POINTER(VARIANT)
            else:
                if not defined(_REFVARIANT_DEFINED):
                    _REFVARIANT_DEFINED = VOID
                    if defined(__cplusplus):
                        REFVARIANT = VARIANT
                    else:
                        REFVARIANT = VARIANT
                    # END IF

                # END IF

            # END IF   MIDL_PASS

            # the following is what MIDL knows how to remote
            _wireBRECORD._fields_ = [
                ('fFlags', ULONG),
                ('clSize', ULONG),
                ('pRecInfo', POINTER(IRecordInfo)),
                # [size_is]
                ('pRecord', POINTER(BYTE)),
            ]


            class DUMMYUNIONNAME(ctypes.Union):
                pass


            DUMMYUNIONNAME._fields_ = [
                # [case()]
                ('llVal', LONGLONG),
                # [case()]
                ('lVal', LONG),
                # [case()]
                ('bVal', BYTE),
                # [case()]
                ('iVal', SHORT),
                # [case()]
                ('fltVal', FLOAT),
                # [case()]
                ('dblVal', DOUBLE),
                # [case()]
                ('boolVal', VARIANT_BOOL),
                # [case()]
                ('scode', SCODE),
                # [case()]
                ('cyVal', CY),
                # [case()]
                ('date', DATE),
                # [case()]
                ('bstrVal', wireBSTR),
                # [case()]
                ('punkVal', POINTER(comtypes.IUnknown)),
                # [case()]
                ('pdispVal', POINTER(IDispatch)),
                # [case()]
                ('parray', wirePSAFEARRAY),
                # [case()]
                ('brecVal', wireBRECORD),
                # [case()]
                ('pbVal', POINTER(BYTE)),
                # [case()]
                ('piVal', POINTER(SHORT)),
                # [case()]
                ('plVal', POINTER(LONG)),
                # [case()]
                ('pllVal', POINTER(LONGLONG)),
                # [case()]
                ('pfltVal', POINTER(FLOAT)),
                # [case()]
                ('pdblVal', POINTER(DOUBLE)),
                # [case()]
                ('pboolVal', POINTER(VARIANT_BOOL)),
                # [case()]
                ('pscode', POINTER(SCODE)),
                # [case()]
                ('pcyVal', POINTER(CY)),
                # [case()]
                ('pdate', POINTER(DATE)),
                # [case()]
                ('pbstrVal', POINTER(wireBSTR)),
                # [case()]
                ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))),
                # [case()]
                ('ppdispVal', POINTER(POINTER(IDispatch))),
                # [case()]
                ('pparray', POINTER(wirePSAFEARRAY)),
                # [case()]
                ('pvarVal', POINTER(wireVARIANT)),
                # [case()]
                ('cVal', CHAR),
                # [case()]
                ('uiVal', USHORT),
                # [case()]
                ('ulVal', ULONG),
                # [case()]
                ('ullVal', ULONGLONG),
                # [case()]
                ('intVal', INT),
                # [case()]
                ('uintVal', UINT),
                # [case()]
                ('decVal', DECIMAL),
                # [case()]
                ('pdecVal', POINTER(DECIMAL)),
                # [case()]
                ('pcVal', POINTER(CHAR)),
                # [case()]
                ('puiVal', POINTER(USHORT)),
                # [case()]
                ('pulVal', POINTER(ULONG)),
                # [case()]
                ('pullVal', POINTER(ULONGLONG)),
                # [case()]
                ('pintVal', POINTER(INT)),
                # [case()]
                ('puintVal', POINTER(UINT)),
            ]
            _wireVARIANT.DUMMYUNIONNAME = DUMMYUNIONNAME


            _wireVARIANT._fields_ = [
                ('clSize', DWORD),
                ('rpcReserved', DWORD),
                ('vt', USHORT),
                ('wReserved1', USHORT),
                ('wReserved2', USHORT),
                ('wReserved3', USHORT),
                # [switch_is][switch_type]
                ('DUMMYUNIONNAME', _wireVARIANT.DUMMYUNIONNAME),
            ]
            DISPID = LONG
            MEMBERID = DISPID
            HREFTYPE = DWORD


            class tagTYPEKIND(ENUM):
                TKIND_ENUM = 0
                TKIND_RECORD = TKIND_ENUM + 1
                TKIND_MODULE = TKIND_RECORD + 1
                TKIND_INTERFACE = TKIND_MODULE + 1
                TKIND_DISPATCH = TKIND_INTERFACE + 1
                TKIND_COCLASS = TKIND_DISPATCH + 1
                TKIND_ALIAS = TKIND_COCLASS + 1
                TKIND_UNION = TKIND_ALIAS + 1
                TKIND_MAX = TKIND_UNION + 1


            TYPEKIND = tagTYPEKIND


            class DUMMYUNIONNAME(ctypes.Union):
                pass


            DUMMYUNIONNAME._fields_ = [
                # [case()]
                ('lptdesc', POINTER(tagTYPEDESC)),
                # [case()]
                ('lpadesc', POINTER(tagARRAYDESC)),
                # [case()]
                ('hreftype', HREFTYPE),
            ]
            tagTYPEDESC.DUMMYUNIONNAME = DUMMYUNIONNAME


            tagTYPEDESC._fields_ = [
                # [switch_is][switch_type]
                ('DUMMYUNIONNAME', tagTYPEDESC.DUMMYUNIONNAME),
                ('vt', VARTYPE),
            ]

            tagARRAYDESC._fields_ = [
                ('tdescElem', TYPEDESC),
                ('cDims', USHORT),
                # [size_is]
                ('rgbounds', SAFEARRAYBOUND * 1),
            ]

            tagPARAMDESCEX._fields_ = [
                ('cBytes', ULONG),
                ('varDefaultValue', VARIANTARG),
            ]
            LPPARAMDESCEX = POINTER(tagPARAMDESCEX)


            tagPARAMDESC._fields_ = [
                ('pparamdescex', LPPARAMDESCEX),
                ('wParamFlags', USHORT),
            ]
            LPPARAMDESC = POINTER(tagPARAMDESC)

            PARAMFLAG_NONE = 0
            PARAMFLAG_FIN = 0x1
            PARAMFLAG_FOUT = 0x2
            PARAMFLAG_FLCID = 0x4
            PARAMFLAG_FRETVAL = 0x8
            PARAMFLAG_FOPT = 0x10
            PARAMFLAG_FHASDEFAULT = 0x20
            PARAMFLAG_FHASCUSTDATA = 0x40


            tagIDLDESC._fields_ = [
                ('dwReserved', ULONG_PTR),
                ('wIDLFlags', USHORT),
            ]
            LPIDLDESC = POINTER(tagIDLDESC)

            IDLFLAG_NONE = PARAMFLAG_NONE
            IDLFLAG_FIN = PARAMFLAG_FIN
            IDLFLAG_FOUT = PARAMFLAG_FOUT
            IDLFLAG_FLCID = PARAMFLAG_FLCID
            IDLFLAG_FRETVAL = PARAMFLAG_FRETVAL

            # ;begin_internal

            __ZERO__ = 0
            if __ZERO__:
                # the following is what MIDL knows how to remote
                tagELEMDESC._fields_ = [
                    ('tdesc', TYPEDESC),
                    ('paramdesc', PARAMDESC),
                ]
            else:
                # ;end_internal
                # the type of the element
                # info for remoting the element
                class DUMMYUNIONNAME(ctypes.Union):
                    pass


                DUMMYUNIONNAME._fields_ = [
                    ('idldesc', IDLDESC),
                    # info about the parameter
                    ('paramdesc', PARAMDESC),
                ]
                tagELEMDESC.DUMMYUNIONNAME = DUMMYUNIONNAME


                tagELEMDESC._fields_ = [
                    ('tdesc', TYPEDESC),
                    ('DUMMYUNIONNAME', tagELEMDESC.DUMMYUNIONNAME),
                ]

                # ;begin_internal
            # END IF  0

            # ;end_internal
            tagTYPEATTR._fields_ = [
                ('guid', GUID),
                ('lcid', LCID),
                ('dwReserved', DWORD),
                ('memidConstructor', MEMBERID),
                ('memidDestructor', MEMBERID),
                ('lpstrSchema', LPOLESTR),
                ('cbSizeInstance', ULONG),
                ('typekind', TYPEKIND),
                ('cFuncs', WORD),
                ('cVars', WORD),
                ('cImplTypes', WORD),
                ('cbSizeVft', WORD),
                ('cbAlignment', WORD),
                ('wTypeFlags', WORD),
                ('wMajorVerNum', WORD),
                ('wMinorVerNum', WORD),
                ('tdescAlias', TYPEDESC),
                ('idldescType', IDLDESC),
            ]
            LPTYPEATTR = POINTER(tagTYPEATTR)


            tagDISPPARAMS._fields_ = [
                # [size_is]
                ('rgvarg', POINTER(VARIANTARG)),
                # [size_is]
                ('rgdispidNamedArgs', POINTER(DISPID)),
                ('cArgs', UINT),
                ('cNamedArgs', UINT),
            ]

            # ;begin_internal
            if __ZERO__:
                # the following is what MIDL knows how to remote
                tagEXCEPINFO._fields_ = [
                    ('wCode', WORD),
                    ('wReserved', WORD),
                    ('bstrSource', BSTR),
                    ('bstrDescription', BSTR),
                    ('bstrHelpFile', BSTR),
                    ('dwHelpContext', DWORD),
                    ('pvReserved', ULONG_PTR),
                    ('pfnDeferredFillIn', ULONG_PTR),
                    ('scode', SCODE),
                ]
            else:
                # ;end_internal
                tagEXCEPINFO._fields_ = [
                    ('wCode', WORD),
                    ('wReserved', WORD),
                    ('bstrSource', BSTR),
                    ('bstrDescription', BSTR),
                    ('bstrHelpFile', BSTR),
                    ('dwHelpContext', DWORD),
                    ('pvReserved', PVOID),
                    ('pfnDeferredFillIn', HRESULT),
                    ('scode', SCODE),
                ]

                # ;begin_internal
            # END IF  0

            # ;end_internal
            class tagCALLCONV(ENUM):
                CC_FASTCALL = 0
                CC_CDECL = 1
                CC_MSCPASCAL = CC_CDECL + 1
                CC_PASCAL = CC_MSCPASCAL
                CC_MACPASCAL = CC_PASCAL + 1
                CC_STDCALL = CC_MACPASCAL + 1
                CC_FPFASTCALL = CC_STDCALL + 1
                CC_SYSCALL = CC_FPFASTCALL + 1
                CC_MPWCDECL = CC_SYSCALL + 1
                CC_MPWPASCAL = CC_MPWCDECL + 1
                CC_MAX = CC_MPWPASCAL + 1


            CALLCONV = tagCALLCONV


            class tagFUNCKIND(ENUM):
                FUNC_VIRTUAL = 0
                FUNC_PUREVIRTUAL = FUNC_VIRTUAL + 1
                FUNC_NONVIRTUAL = FUNC_PUREVIRTUAL + 1
                FUNC_STATIC = FUNC_NONVIRTUAL + 1
                FUNC_DISPATCH = FUNC_STATIC + 1


            FUNCKIND = tagFUNCKIND


            class tagINVOKEKIND(ENUM):
                INVOKE_FUNC = 1
                INVOKE_PROPERTYGET = 2
                INVOKE_PROPERTYPUT = 4
                INVOKE_PROPERTYPUTREF = 8

            INVOKEKIND = tagINVOKEKIND

            tagFUNCDESC._fields_ = [
                ('memid', MEMBERID),
                # [size_is]
                ('lprgscode', POINTER(SCODE)),
                # [size_is]
                ('lprgelemdescParam', POINTER(ELEMDESC)),
                ('funckind', FUNCKIND),
                ('invkind', INVOKEKIND),
                ('callconv', CALLCONV),
                ('cParams', SHORT),
                ('cParamsOpt', SHORT),
                ('oVft', SHORT),
                ('cScodes', SHORT),
                ('elemdescFunc', ELEMDESC),
                ('wFuncFlags', WORD),
            ]
            LPFUNCDESC = POINTER(tagFUNCDESC)


            class tagVARKIND(ENUM):
                VAR_PERINSTANCE = 0
                VAR_STATIC = VAR_PERINSTANCE + 1
                VAR_CONST = VAR_STATIC + 1
                VAR_DISPATCH = VAR_CONST + 1


            VARKIND = tagVARKIND
            IMPLTYPEFLAG_FDEFAULT = 0x1
            IMPLTYPEFLAG_FSOURCE = 0x2
            IMPLTYPEFLAG_FRESTRICTED = 0x4
            IMPLTYPEFLAG_FDEFAULTVTABLE = 0x8


            class DUMMYUNIONNAME(ctypes.Union):
                pass


            DUMMYUNIONNAME._fields_ = [
                # [case()]
                ('oInst', ULONG),
                # [case()]
                ('lpvarValue', POINTER(VARIANT)),
            ]
            tagVARDESC.DUMMYUNIONNAME = DUMMYUNIONNAME


            tagVARDESC._fields_ = [
                ('memid', MEMBERID),
                ('lpstrSchema', LPOLESTR),
                # [switch_is][switch_type]
                ('DUMMYUNIONNAME', tagVARDESC.DUMMYUNIONNAME),
                ('elemdescVar', ELEMDESC),
                ('wVarFlags', WORD),
                ('varkind', VARKIND),
            ]
            LPVARDESC = POINTER(tagVARDESC)


            class tagTYPEFLAGS(ENUM):
                TYPEFLAG_FAPPOBJECT = 0x1
                TYPEFLAG_FCANCREATE = 0x2
                TYPEFLAG_FLICENSED = 0x4
                TYPEFLAG_FPREDECLID = 0x8
                TYPEFLAG_FHIDDEN = 0x10
                TYPEFLAG_FCONTROL = 0x20
                TYPEFLAG_FDUAL = 0x40
                TYPEFLAG_FNONEXTENSIBLE = 0x80
                TYPEFLAG_FOLEAUTOMATION = 0x100
                TYPEFLAG_FRESTRICTED = 0x200
                TYPEFLAG_FAGGREGATABLE = 0x400
                TYPEFLAG_FREPLACEABLE = 0x800
                TYPEFLAG_FDISPATCHABLE = 0x1000
                TYPEFLAG_FREVERSEBIND = 0x2000
                TYPEFLAG_FPROXY = 0x4000

            TYPEFLAGS = tagTYPEFLAGS


            class tagFUNCFLAGS(ENUM):
                FUNCFLAG_FRESTRICTED = 0x1
                FUNCFLAG_FSOURCE = 0x2
                FUNCFLAG_FBINDABLE = 0x4
                FUNCFLAG_FREQUESTEDIT = 0x8
                FUNCFLAG_FDISPLAYBIND = 0x10
                FUNCFLAG_FDEFAULTBIND = 0x20
                FUNCFLAG_FHIDDEN = 0x40
                FUNCFLAG_FUSESGETLASTERROR = 0x80
                FUNCFLAG_FDEFAULTCOLLELEM = 0x100
                FUNCFLAG_FUIDEFAULT = 0x200
                FUNCFLAG_FNONBROWSABLE = 0x400
                FUNCFLAG_FREPLACEABLE = 0x800
                FUNCFLAG_FIMMEDIATEBIND = 0x1000

            FUNCFLAGS = tagFUNCFLAGS


            class tagVARFLAGS(ENUM):
                VARFLAG_FREADONLY = 0x1
                VARFLAG_FSOURCE = 0x2
                VARFLAG_FBINDABLE = 0x4
                VARFLAG_FREQUESTEDIT = 0x8
                VARFLAG_FDISPLAYBIND = 0x10
                VARFLAG_FDEFAULTBIND = 0x20
                VARFLAG_FHIDDEN = 0x40
                VARFLAG_FRESTRICTED = 0x80
                VARFLAG_FDEFAULTCOLLELEM = 0x100
                VARFLAG_FUIDEFAULT = 0x200
                VARFLAG_FNONBROWSABLE = 0x400
                VARFLAG_FREPLACEABLE = 0x800
                VARFLAG_FIMMEDIATEBIND = 0x1000

            VARFLAGS = tagVARFLAGS

            tagCLEANLOCALSTORAGE._fields_ = [
                ('pInterface', POINTER(comtypes.IUnknown)),
                ('pStorage', PVOID),
                ('flags', DWORD),
            ]

            tagCUSTDATAITEM._fields_ = [
                ('guid', GUID),
                ('varValue', VARIANTARG),
            ]
            LPCUSTDATAITEM = POINTER(tagCUSTDATAITEM)


            tagCUSTDATA._fields_ = [
                ('cCustData', DWORD),
                # [size_is]
                ('prgCustData', LPCUSTDATAITEM),
            ]
            LPCUSTDATA = POINTER(tagCUSTDATA)

        # END IF  __IOleAutomationTypes_INTERFACE_DEFINED__

        # interface __MIDL_itf_oaidl_0000_0001
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__ICreateTypeInfo_INTERFACE_DEFINED__):
            __ICreateTypeInfo_INTERFACE_DEFINED__ = VOID

            # interface ICreateTypeInfo
            # [local][unique][uuid][object]
            # [unique]
            LPCREATETYPEINFO = POINTER(ICreateTypeInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICreateTypeInfo = MIDL_INTERFACE(
                    "{00020405-0000-0000-C000-000000000046}"
                )
                ICreateTypeInfo._iid_ = IID_ICreateTypeInfo

                ICreateTypeInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetGuid')],
                        HRESULT,
                        'SetGuid',
                        (['in'], REFGUID, 'guid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetTypeFlags')],
                        HRESULT,
                        'SetTypeFlags',
                        (['in'], UINT, 'uTypeFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetDocString')],
                        HRESULT,
                        'SetDocString',
                        (['in'], LPOLESTR, 'pStrDoc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpContext')],
                        HRESULT,
                        'SetHelpContext',
                        (['in'], DWORD, 'dwHelpContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVersion')],
                        HRESULT,
                        'SetVersion',
                        (['in'], WORD, 'wMajorVerNum'),
                        (['in'], WORD, 'wMinorVerNum'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddRefTypeInfo')],
                        HRESULT,
                        'AddRefTypeInfo',
                        (['in'], POINTER(ITypeInfo), 'pTInfo'),
                        (['in'], POINTER(HREFTYPE), 'phRefType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddFuncDesc')],
                        HRESULT,
                        'AddFuncDesc',
                        (['in'], UINT, 'index'),
                        (['in'], POINTER(FUNCDESC), 'pFuncDesc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddImplType')],
                        HRESULT,
                        'AddImplType',
                        (['in'], UINT, 'index'),
                        (['in'], HREFTYPE, 'hRefType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetImplTypeFlags')],
                        HRESULT,
                        'SetImplTypeFlags',
                        (['in'], UINT, 'index'),
                        (['in'], INT, 'implTypeFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetAlignment')],
                        HRESULT,
                        'SetAlignment',
                        (['in'], WORD, 'cbAlignment'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetSchema')],
                        HRESULT,
                        'SetSchema',
                        (['in'], LPOLESTR, 'pStrSchema'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddVarDesc')],
                        HRESULT,
                        'AddVarDesc',
                        (['in'], UINT, 'index'),
                        (['in'], POINTER(VARDESC), 'pVarDesc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFuncAndParamNames')],
                        HRESULT,
                        'SetFuncAndParamNames',
                        (['in'], UINT, 'index'),
                        (
                            ['in'],
                            POINTER(LPOLESTR),
                            'rgszNames'
                        ),
                        (['in'], UINT, 'cNames'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVarName')],
                        HRESULT,
                        'SetVarName',
                        (['in'], UINT, 'index'),
                        (['in'], LPOLESTR, 'szName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetTypeDescAlias')],
                        HRESULT,
                        'SetTypeDescAlias',
                        (['in'], POINTER(TYPEDESC), 'pTDescAlias'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DefineFuncAsDllEntry')],
                        HRESULT,
                        'DefineFuncAsDllEntry',
                        (['in'], UINT, 'index'),
                        (['in'], LPOLESTR, 'szDllName'),
                        (['in'], LPOLESTR, 'szProcName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFuncDocString')],
                        HRESULT,
                        'SetFuncDocString',
                        (['in'], UINT, 'index'),
                        (['in'], LPOLESTR, 'szDocString'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVarDocString')],
                        HRESULT,
                        'SetVarDocString',
                        (['in'], UINT, 'index'),
                        (['in'], LPOLESTR, 'szDocString'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFuncHelpContext')],
                        HRESULT,
                        'SetFuncHelpContext',
                        (['in'], UINT, 'index'),
                        (['in'], DWORD, 'dwHelpContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVarHelpContext')],
                        HRESULT,
                        'SetVarHelpContext',
                        (['in'], UINT, 'index'),
                        (['in'], DWORD, 'dwHelpContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetMops')],
                        HRESULT,
                        'SetMops',
                        (['in'], UINT, 'index'),
                        (['in'], BSTR, 'bstrMops'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetTypeIdldesc')],
                        HRESULT,
                        'SetTypeIdldesc',
                        (['in'], POINTER(IDLDESC), 'pIdlDesc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method LayOut')],
                        HRESULT,
                        'LayOut',
                    ),
                ]
            # END IF  C style interface
        # END IF  __ICreateTypeInfo_INTERFACE_DEFINED__


        if not defined(__ICreateTypeInfo2_INTERFACE_DEFINED__):
            __ICreateTypeInfo2_INTERFACE_DEFINED__ = VOID

            # interface ICreateTypeInfo2
            # [local][unique][uuid][object]
            # [unique]
            LPCREATETYPEINFO2 = POINTER(ICreateTypeInfo2)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICreateTypeInfo2 = MIDL_INTERFACE(
                    "{0002040E-0000-0000-C000-000000000046}"
                )
                ICreateTypeInfo2._iid_ = IID_ICreateTypeInfo2

                ICreateTypeInfo2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method DeleteFuncDesc')],
                        HRESULT,
                        'DeleteFuncDesc',
                        (['in'], UINT, 'index'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteFuncDescByMemId')],
                        HRESULT,
                        'DeleteFuncDescByMemId',
                        (['in'], MEMBERID, 'memid'),
                        (['in'], INVOKEKIND, 'invKind'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteVarDesc')],
                        HRESULT,
                        'DeleteVarDesc',
                        (['in'], UINT, 'index'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteVarDescByMemId')],
                        HRESULT,
                        'DeleteVarDescByMemId',
                        (['in'], MEMBERID, 'memid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DeleteImplType')],
                        HRESULT,
                        'DeleteImplType',
                        (['in'], UINT, 'index'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetCustData')],
                        HRESULT,
                        'SetCustData',
                        (['in'], REFGUID, 'guid'),
                        (['in'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFuncCustData')],
                        HRESULT,
                        'SetFuncCustData',
                        (['in'], UINT, 'index'),
                        (['in'], REFGUID, 'guid'),
                        (['in'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetParamCustData')],
                        HRESULT,
                        'SetParamCustData',
                        (['in'], UINT, 'indexFunc'),
                        (['in'], UINT, 'indexParam'),
                        (['in'], REFGUID, 'guid'),
                        (['in'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVarCustData')],
                        HRESULT,
                        'SetVarCustData',
                        (['in'], UINT, 'index'),
                        (['in'], REFGUID, 'guid'),
                        (['in'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetImplTypeCustData')],
                        HRESULT,
                        'SetImplTypeCustData',
                        (['in'], UINT, 'index'),
                        (['in'], REFGUID, 'guid'),
                        (['in'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpStringContext')],
                        HRESULT,
                        'SetHelpStringContext',
                        (['in'], ULONG, 'dwHelpStringContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFuncHelpStringContext')],
                        HRESULT,
                        'SetFuncHelpStringContext',
                        (['in'], UINT, 'index'),
                        (['in'], ULONG, 'dwHelpStringContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVarHelpStringContext')],
                        HRESULT,
                        'SetVarHelpStringContext',
                        (['in'], UINT, 'index'),
                        (['in'], ULONG, 'dwHelpStringContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Invalidate')],
                        HRESULT,
                        'Invalidate',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetName')],
                        HRESULT,
                        'SetName',
                        (['in'], LPOLESTR, 'szName'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ICreateTypeInfo2_INTERFACE_DEFINED__

        if not defined(__ICreateTypeLib_INTERFACE_DEFINED__):
            __ICreateTypeLib_INTERFACE_DEFINED__ = VOID

            # interface ICreateTypeLib
            # [local][unique][uuid][object]
            # [unique]
            LPCREATETYPELIB = POINTER(ICreateTypeLib)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICreateTypeLib = MIDL_INTERFACE(
                    "{00020406-0000-0000-C000-000000000046}"
                )
                ICreateTypeLib._iid_ = IID_ICreateTypeLib

                ICreateTypeLib._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateTypeInfo')],
                        HRESULT,
                        'CreateTypeInfo',
                        (['in'], LPOLESTR, 'szName'),
                        (['in'], TYPEKIND, 'tkind'),
                        (
                            ['out'],
                            POINTER(POINTER(ICreateTypeInfo)),
                            'ppCTInfo'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetName')],
                        HRESULT,
                        'SetName',
                        (['in'], LPOLESTR, 'szName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetVersion')],
                        HRESULT,
                        'SetVersion',
                        (['in'], WORD, 'wMajorVerNum'),
                        (['in'], WORD, 'wMinorVerNum'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetGuid')],
                        HRESULT,
                        'SetGuid',
                        (['in'], REFGUID, 'guid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetDocString')],
                        HRESULT,
                        'SetDocString',
                        (['in'], LPOLESTR, 'szDoc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpFileName')],
                        HRESULT,
                        'SetHelpFileName',
                        (['in'], LPOLESTR, 'szHelpFileName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpContext')],
                        HRESULT,
                        'SetHelpContext',
                        (['in'], DWORD, 'dwHelpContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetLcid')],
                        HRESULT,
                        'SetLcid',
                        (['in'], LCID, 'lcid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetLibFlags')],
                        HRESULT,
                        'SetLibFlags',
                        (['in'], UINT, 'uLibFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SaveAllChanges')],
                        HRESULT,
                        'SaveAllChanges',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ICreateTypeLib_INTERFACE_DEFINED__

        if not defined(__ICreateTypeLib2_INTERFACE_DEFINED__):
            __ICreateTypeLib2_INTERFACE_DEFINED__ = VOID

            # interface ICreateTypeLib2
            # [local][unique][uuid][object]
            # [unique]
            LPCREATETYPELIB2 = POINTER(ICreateTypeLib2)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICreateTypeLib2 = MIDL_INTERFACE(
                    "{0002040F-0000-0000-C000-000000000046}"
                )
                ICreateTypeLib2._iid_ = IID_ICreateTypeLib2

                ICreateTypeLib2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method DeleteTypeInfo')],
                        HRESULT,
                        'DeleteTypeInfo',
                        (['in'], LPOLESTR, 'szName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetCustData')],
                        HRESULT,
                        'SetCustData',
                        (['in'], REFGUID, 'guid'),
                        (['in'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpStringContext')],
                        HRESULT,
                        'SetHelpStringContext',
                        (['in'], ULONG, 'dwHelpStringContext'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpStringDll')],
                        HRESULT,
                        'SetHelpStringDll',
                        (['in'], LPOLESTR, 'szFileName'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ICreateTypeLib2_INTERFACE_DEFINED__

        # interface __MIDL_itf_oaidl_0000_0005
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IDispatch_INTERFACE_DEFINED__):
            __IDispatch_INTERFACE_DEFINED__ = VOID

            # interface IDispatch
            # [unique][uuid][object]
            # [unique]
            LPDISPATCH = POINTER(IDispatch)

            # DISPID reserved to indicate an "unknown" name
            # only reserved for data members (properties); reused as a method
            # dispid below
            DISPID_UNKNOWN = -1

            # DISPID reserved for the "value" property
            DISPID_VALUE = 0

            # /* The following DISPID is reserved to indicate the param that
            # is the right-hand-side (or "put" value) of a PropertyPut
            DISPID_PROPERTYPUT = -3

            # DISPID reserved for the standard "NewEnum" method
            DISPID_NEWENUM = -4

            # DISPID reserved for the standard "Evaluate" method
            DISPID_EVALUATE = -5
            DISPID_CONSTRUCTOR = -6
            DISPID_DESTRUCTOR = -7
            DISPID_COLLECT = -8

            # The range -500 through -999 is reserved for Controls
            # The range 0x80010000 through 0x8001FFFF is reserved for Controls
            # The range -5000 through -5499 is reserved for ActiveX
            # Accessability
            # The range -2000 through -2499 is reserved for VB5
            # The range -3900 through -3999 is reserved for Forms
            # The range -5500 through -5550 is reserved for Forms
            # The remainder of the negative DISPIDs are reserved for future use
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDispatch = MIDL_INTERFACE(
                    "{00020400-0000-0000-C000-000000000046}"
                )
                IDispatch._iid_ = IID_IDispatch

                IDispatch._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetTypeInfoCount')],
                        HRESULT,
                        'GetTypeInfoCount',
                        (['out'], POINTER(UINT), 'pctinfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeInfo')],
                        HRESULT,
                        'GetTypeInfo',
                        (['in'], UINT, 'iTInfo'),
                        (['in'], LCID, 'lcid'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetIDsOfNames')],
                        HRESULT,
                        'GetIDsOfNames',
                        (['in'], REFIID, 'riid'),
                        (['in'], POINTER(LPOLESTR), 'rgszNames'),
                        (['range', 'in'], UINT, 'cNames'),
                        (['in'], LCID, 'lcid'),
                        (['out'], POINTER(DISPID), 'rgDispId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Invoke'), 'local'],
                        HRESULT,
                        'Invoke',
                        (['in'], DISPID, 'dispIdMember'),
                        (['in'], REFIID, 'riid'),
                        (['in'], LCID, 'lcid'),
                        (['in'], WORD, 'wFlags'),
                        (['in'], POINTER(DISPPARAMS), 'pDispParams'),
                        (['out'], POINTER(VARIANT), 'pVarResult'),
                        (['out'], POINTER(EXCEPINFO), 'pExcepInfo'),
                        (['out'], POINTER(UINT), 'puArgErr'),
                    ),
                ]

                # DISPID reserved to indicate an \"unknown\" name only
                # reserved for data members (properties); reused as a
                # method dispid below
                # DISPID reserved for the \"value\" property
                # The following DISPID is reserved to indicate the
                # param") cpp_quote(" * that is the right-hand-side
                # (or \"put\" value) of a PropertyPut") cpp_quote("
                # DISPID reserved for the standard \"Evaluate\" method
                # The range -500 through -999 is reserved for Controls The
                # range 0x80010000 through 0x8001FFFF is reserved for
                # Controls The range -5000 through -5499 is reserved for
                # ActiveX Accessability The range -2000 through -2499 is
                # reserved for VB5 The range -3900 through -3999 is
                # reserved for Forms The range -5500 through -5550 is
                # reserved for Forms The remainder of the negative DISPIDs
                # are reserved for future use                ]

            # END IF  C style interface
        # END IF __IDispatch_INTERFACE_DEFINED__

        if not defined(__IEnumVARIANT_INTERFACE_DEFINED__):
            __IEnumVARIANT_INTERFACE_DEFINED__ = VOID

            # interface IEnumVARIANT
            # [unique][uuid][object]
            # [unique]
            LPENUMVARIANT = POINTER(IEnumVARIANT)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumVARIANT = MIDL_INTERFACE(
                    "{00020404-0000-0000-C000-000000000046}"
                )
                IEnumVARIANT._iid_ = IID_IEnumVARIANT

                IEnumVARIANT._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'celt'),
                        (['out'], POINTER(VARIANT), 'rgVar'),
                        (['out'], POINTER(ULONG), 'pCeltFetched'),
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
                        (['out'], POINTER(POINTER(IEnumVARIANT)), 'ppEnum'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __IEnumVARIANT_INTERFACE_DEFINED__

        if not defined(__ITypeComp_INTERFACE_DEFINED__):
            __ITypeComp_INTERFACE_DEFINED__ = VOID

            # interface ITypeComp
            # [unique][uuid][object]
            # [unique]
            LPTYPECOMP = POINTER(ITypeComp)


            class tagDESCKIND(ENUM):
                DESCKIND_NONE = 0
                DESCKIND_FUNCDESC = DESCKIND_NONE + 1
                DESCKIND_VARDESC = DESCKIND_FUNCDESC + 1
                DESCKIND_TYPECOMP = DESCKIND_VARDESC + 1
                DESCKIND_IMPLICITAPPOBJ = DESCKIND_TYPECOMP + 1
                DESCKIND_MAX = DESCKIND_IMPLICITAPPOBJ + 1


            DESCKIND = tagDESCKIND

            tagBINDPTR._fields_ = [
                ('lpfuncdesc', POINTER(FUNCDESC)),
                ('lpvardesc', POINTER(VARDESC)),
                ('lptcomp', POINTER(ITypeComp)),
            ]
            LPBINDPTR = POINTER(tagBINDPTR)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeComp = MIDL_INTERFACE(
                    "{00020403-0000-0000-C000-000000000046}"
                )
                ITypeComp._iid_ = IID_ITypeComp

                ITypeComp._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Bind'), 'local'],
                        HRESULT,
                        'Bind',
                        (['in'], LPOLESTR, 'szName'),
                        (['in'], ULONG, 'lHashVal'),
                        (['in'], WORD, 'wFlags'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
                        (['out'], POINTER(DESCKIND), 'pDescKind'),
                        (['out'], POINTER(BINDPTR), 'pBindPtr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BindType'), 'local'],
                        HRESULT,
                        'BindType',
                        (['in'], LPOLESTR, 'szName'),
                        (['in'], ULONG, 'lHashVal'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
                        (['out'], POINTER(POINTER(ITypeComp)), 'ppTComp'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITypeComp_INTERFACE_DEFINED__

        # interface __MIDL_itf_oaidl_0000_0008
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__ITypeInfo_INTERFACE_DEFINED__):
            __ITypeInfo_INTERFACE_DEFINED__ = VOID

            # interface ITypeInfo
            # [unique][uuid][object]
            # [unique]
            LPTYPEINFO = POINTER(ITypeInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeInfo = MIDL_INTERFACE(
                    "{00020401-0000-0000-C000-000000000046}"
                )
                ITypeInfo._iid_ = IID_ITypeInfo

                ITypeInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetTypeAttr'), 'local'],
                        HRESULT,
                        'GetTypeAttr',
                        (['out'], POINTER(POINTER(TYPEATTR)), 'ppTypeAttr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeComp')],
                        HRESULT,
                        'GetTypeComp',
                        (['out'], POINTER(POINTER(ITypeComp)), 'ppTComp'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFuncDesc'), 'local'],
                        HRESULT,
                        'GetFuncDesc',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(POINTER(FUNCDESC)), 'ppFuncDesc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVarDesc'), 'local'],
                        HRESULT,
                        'GetVarDesc',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(POINTER(VARDESC)), 'ppVarDesc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNames'), 'local'],
                        HRESULT,
                        'GetNames',
                        (['in'], MEMBERID, 'memid'),
                        (['out'], POINTER(BSTR), 'rgBstrNames'),
                        (['in'], UINT, 'cMaxNames'),
                        (['out'], POINTER(UINT), 'pcNames'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRefTypeOfImplType')],
                        HRESULT,
                        'GetRefTypeOfImplType',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(HREFTYPE), 'pRefType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetImplTypeFlags')],
                        HRESULT,
                        'GetImplTypeFlags',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(INT), 'pImplTypeFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetIDsOfNames'), 'local'],
                        HRESULT,
                        'GetIDsOfNames',
                        (['in'], POINTER(LPOLESTR), 'rgszNames'),
                        (['in'], UINT, 'cNames'),
                        (['out'], POINTER(MEMBERID), 'pMemId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Invoke'), 'local'],
                        HRESULT,
                        'Invoke',
                        (['in'], PVOID, 'pvInstance'),
                        (['in'], MEMBERID, 'memid'),
                        (['in'], WORD, 'wFlags'),
                        (['out', 'in'], POINTER(DISPPARAMS), 'pDispParams'),
                        (['out'], POINTER(VARIANT), 'pVarResult'),
                        (['out'], POINTER(EXCEPINFO), 'pExcepInfo'),
                        (['out'], POINTER(UINT), 'puArgErr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDocumentation'), 'local'],
                        HRESULT,
                        'GetDocumentation',
                        (['in'], MEMBERID, 'memid'),
                        (['out'], POINTER(BSTR), 'pBstrName'),
                        (['out'], POINTER(BSTR), 'pBstrDocString'),
                        (['out'], POINTER(DWORD), 'pdwHelpContext'),
                        (['out'], POINTER(BSTR), 'pBstrHelpFile'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDllEntry'), 'local'],
                        HRESULT,
                        'GetDllEntry',
                        (['in'], MEMBERID, 'memid'),
                        (['in'], INVOKEKIND, 'invKind'),
                        (['out'], POINTER(BSTR), 'pBstrDllName'),
                        (['out'], POINTER(BSTR), 'pBstrName'),
                        (['out'], POINTER(WORD), 'pwOrdinal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRefTypeInfo')],
                        HRESULT,
                        'GetRefTypeInfo',
                        (['in'], HREFTYPE, 'hRefType'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddressOfMember'), 'local'],
                        HRESULT,
                        'AddressOfMember',
                        (['in'], MEMBERID, 'memid'),
                        (['in'], INVOKEKIND, 'invKind'),
                        (['out'], POINTER(PVOID), 'ppv'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CreateInstance'), 'local'],
                        HRESULT,
                        'CreateInstance',
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
                        (['in'], REFIID, 'riid'),
                        (['iid_is', 'out'], POINTER(PVOID), 'ppvObj'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetMops')],
                        HRESULT,
                        'GetMops',
                        (['in'], MEMBERID, 'memid'),
                        (['out'], POINTER(BSTR), 'pBstrMops'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetContainingTypeLib'), 'local'],
                        HRESULT,
                        'GetContainingTypeLib',
                        (['out'], POINTER(POINTER(ITypeLib)), 'ppTLib'),
                        (['out'], POINTER(UINT), 'pIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseTypeAttr'), 'local'],
                        VOID,
                        'ReleaseTypeAttr',
                        (['in'], POINTER(TYPEATTR), 'pTypeAttr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseFuncDesc'), 'local'],
                        VOID,
                        'ReleaseFuncDesc',
                        (['in'], POINTER(FUNCDESC), 'pFuncDesc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseVarDesc'), 'local'],
                        VOID,
                        'ReleaseVarDesc',
                        (['in'], POINTER(VARDESC), 'pVarDesc'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITypeInfo_INTERFACE_DEFINED__

        if not defined(__ITypeInfo2_INTERFACE_DEFINED__):
            __ITypeInfo2_INTERFACE_DEFINED__ = VOID

            # interface ITypeInfo2
            # [unique][uuid][object]
            # [unique]
            LPTYPEINFO2 = POINTER(ITypeInfo2)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeInfo2 = MIDL_INTERFACE(
                    "{00020412-0000-0000-C000-000000000046}"
                )
                ITypeInfo2._iid_ = IID_ITypeInfo2

                ITypeInfo2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetTypeKind')],
                        HRESULT,
                        'GetTypeKind',
                        (['out'], POINTER(TYPEKIND), 'pTypeKind'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeFlags')],
                        HRESULT,
                        'GetTypeFlags',
                        (['out'], POINTER(ULONG), 'pTypeFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFuncIndexOfMemId')],
                        HRESULT,
                        'GetFuncIndexOfMemId',
                        (['in'], MEMBERID, 'memid'),
                        (['in'], INVOKEKIND, 'invKind'),
                        (['out'], POINTER(UINT), 'pFuncIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVarIndexOfMemId')],
                        HRESULT,
                        'GetVarIndexOfMemId',
                        (['in'], MEMBERID, 'memid'),
                        (['out'], POINTER(UINT), 'pVarIndex'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCustData')],
                        HRESULT,
                        'GetCustData',
                        (['in'], REFGUID, 'guid'),
                        (['out'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFuncCustData')],
                        HRESULT,
                        'GetFuncCustData',
                        (['in'], UINT, 'index'),
                        (['in'], REFGUID, 'guid'),
                        (['out'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetParamCustData')],
                        HRESULT,
                        'GetParamCustData',
                        (['in'], UINT, 'indexFunc'),
                        (['in'], UINT, 'indexParam'),
                        (['in'], REFGUID, 'guid'),
                        (['out'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVarCustData')],
                        HRESULT,
                        'GetVarCustData',
                        (['in'], UINT, 'index'),
                        (['in'], REFGUID, 'guid'),
                        (['out'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetImplTypeCustData')],
                        HRESULT,
                        'GetImplTypeCustData',
                        (['in'], UINT, 'index'),
                        (['in'], REFGUID, 'guid'),
                        (['out'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDocumentation2'), 'local'],
                        HRESULT,
                        'GetDocumentation2',
                        (['in'], MEMBERID, 'memid'),
                        (['in'], LCID, 'lcid'),
                        (['out'], POINTER(BSTR), 'pbstrHelpString'),
                        (['out'], POINTER(DWORD), 'pdwHelpStringContext'),
                        (['out'], POINTER(BSTR), 'pbstrHelpStringDll'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllCustData')],
                        HRESULT,
                        'GetAllCustData',
                        (['out'], POINTER(CUSTDATA), 'pCustData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllFuncCustData')],
                        HRESULT,
                        'GetAllFuncCustData',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(CUSTDATA), 'pCustData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllParamCustData')],
                        HRESULT,
                        'GetAllParamCustData',
                        (['in'], UINT, 'indexFunc'),
                        (['in'], UINT, 'indexParam'),
                        (['out'], POINTER(CUSTDATA), 'pCustData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllVarCustData')],
                        HRESULT,
                        'GetAllVarCustData',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(CUSTDATA), 'pCustData'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllImplTypeCustData')],
                        HRESULT,
                        'GetAllImplTypeCustData',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(CUSTDATA), 'pCustData'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ITypeInfo2_INTERFACE_DEFINED__
        # interface __MIDL_itf_oaidl_0000_0010
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__ITypeLib_INTERFACE_DEFINED__):
            __ITypeLib_INTERFACE_DEFINED__ = VOID

            # interface ITypeLib
            # [unique][uuid][object]
            class tagSYSKIND(ENUM):
                SYS_WIN16 = 0
                SYS_WIN32 = SYS_WIN16 + 1
                SYS_MAC = SYS_WIN32 + 1
                SYS_WIN64 = SYS_MAC + 1


            SYSKIND = tagSYSKIND


            class tagLIBFLAGS(ENUM):
                LIBFLAG_FRESTRICTED = 0x1
                LIBFLAG_FCONTROL = 0x2
                LIBFLAG_FHIDDEN = 0x4
                LIBFLAG_FHASDISKIMAGE = 0x8

            LIBFLAGS = tagLIBFLAGS

            # [unique]
            LPTYPELIB = POINTER(ITypeLib)

            tagTLIBATTR._fields_ = [
                ('guid', GUID),
                ('lcid', LCID),
                ('syskind', SYSKIND),
                ('wMajorVerNum', WORD),
                ('wMinorVerNum', WORD),
                ('wLibFlags', WORD),
            ]
            LPTLIBATTR = POINTER(tagTLIBATTR)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeLib = MIDL_INTERFACE(
                    "{00020402-0000-0000-C000-000000000046}"
                )
                ITypeLib._iid_ = IID_ITypeLib

                ITypeLib._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetTypeInfoCount'), 'local'],
                        UINT,
                        'GetTypeInfoCount',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeInfo')],
                        HRESULT,
                        'GetTypeInfo',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeInfoType')],
                        HRESULT,
                        'GetTypeInfoType',
                        (['in'], UINT, 'index'),
                        (['out'], POINTER(TYPEKIND), 'pTKind'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeInfoOfGuid')],
                        HRESULT,
                        'GetTypeInfoOfGuid',
                        (['in'], REFGUID, 'guid'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTinfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLibAttr'), 'local'],
                        HRESULT,
                        'GetLibAttr',
                        (['out'], POINTER(POINTER(TLIBATTR)), 'ppTLibAttr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeComp')],
                        HRESULT,
                        'GetTypeComp',
                        (['out'], POINTER(POINTER(ITypeComp)), 'ppTComp'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDocumentation'), 'local'],
                        HRESULT,
                        'GetDocumentation',
                        (['in'], INT, 'index'),
                        (['out'], POINTER(BSTR), 'pBstrName'),
                        (['out'], POINTER(BSTR), 'pBstrDocString'),
                        (['out'], POINTER(DWORD), 'pdwHelpContext'),
                        (['out'], POINTER(BSTR), 'pBstrHelpFile'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsName'), 'local'],
                        HRESULT,
                        'IsName',
                        (['in', 'out'], LPOLESTR, 'szNameBuf'),
                        (['in'], ULONG, 'lHashVal'),
                        (['out'], POINTER(BOOL), 'pfName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FindName'), 'local'],
                        HRESULT,
                        'FindName',
                        (['in', 'out'], LPOLESTR, 'szNameBuf'),
                        (['in'], ULONG, 'lHashVal'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTInfo'),
                        (['out'], POINTER(MEMBERID), 'rgMemId'),
                        (['out', 'in'], POINTER(USHORT), 'pcFound'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseTLibAttr'), 'local'],
                        VOID,
                        'ReleaseTLibAttr',
                        (['in'], POINTER(TLIBATTR), 'pTLibAttr'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ITypeLib_INTERFACE_DEFINED__
        # interface __MIDL_itf_oaidl_0000_0011
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__ITypeLib2_INTERFACE_DEFINED__):
            __ITypeLib2_INTERFACE_DEFINED__ = VOID

            # interface ITypeLib2
            # [unique][uuid][object]
            # [unique]
            LPTYPELIB2 = POINTER(ITypeLib2)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeLib2 = MIDL_INTERFACE(
                    "{00020411-0000-0000-C000-000000000046}"
                )
                ITypeLib2._iid_ = IID_ITypeLib2

                ITypeLib2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetCustData')],
                        HRESULT,
                        'GetCustData',
                        (['in'], REFGUID, 'guid'),
                        (['out'], POINTER(VARIANT), 'pVarVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLibStatistics'), 'local'],
                        HRESULT,
                        'GetLibStatistics',
                        (['out'], POINTER(ULONG), 'pcUniqueNames'),
                        (['out'], POINTER(ULONG), 'pcchUniqueNames'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDocumentation2'), 'local'],
                        HRESULT,
                        'GetDocumentation2',
                        (['in'], INT, 'index'),
                        (['in'], LCID, 'lcid'),
                        (['out'], POINTER(BSTR), 'pbstrHelpString'),
                        (['out'], POINTER(DWORD), 'pdwHelpStringContext'),
                        (['out'], POINTER(BSTR), 'pbstrHelpStringDll'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAllCustData')],
                        HRESULT,
                        'GetAllCustData',
                        (['out'], POINTER(CUSTDATA), 'pCustData'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ITypeLib2_INTERFACE_DEFINED__

        if not defined(__ITypeChangeEvents_INTERFACE_DEFINED__):
            __ITypeChangeEvents_INTERFACE_DEFINED__ = VOID

            # interface ITypeChangeEvents
            # [local][unique][uuid][object]
            # [unique]
            LPTYPECHANGEEVENTS = POINTER(ITypeChangeEvents)


            class tagCHANGEKIND(ENUM):
                CHANGEKIND_ADDMEMBER = 0
                CHANGEKIND_DELETEMEMBER = CHANGEKIND_ADDMEMBER + 1
                CHANGEKIND_SETNAMES = CHANGEKIND_DELETEMEMBER + 1
                CHANGEKIND_SETDOCUMENTATION = CHANGEKIND_SETNAMES + 1
                CHANGEKIND_GENERAL = CHANGEKIND_SETDOCUMENTATION + 1
                CHANGEKIND_INVALIDATE = CHANGEKIND_GENERAL + 1
                CHANGEKIND_CHANGEFAILED = CHANGEKIND_INVALIDATE + 1
                CHANGEKIND_MAX = CHANGEKIND_CHANGEFAILED + 1


            CHANGEKIND = tagCHANGEKIND
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeChangeEvents = MIDL_INTERFACE(
                    "{00020410-0000-0000-C000-000000000046}"
                )
                ITypeChangeEvents._iid_ = IID_ITypeChangeEvents

                ITypeChangeEvents._methods_ = [
                    COMMETHOD(
                        [helpstring('Method RequestTypeChange')],
                        HRESULT,
                        'RequestTypeChange',
                        (['in'], CHANGEKIND, 'changeKind'),
                        (['in'], POINTER(ITypeInfo), 'pTInfoBefore'),
                        (['in'], LPOLESTR, 'pStrName'),
                        (['out'], POINTER(INT), 'pfCancel'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AfterTypeChange')],
                        HRESULT,
                        'AfterTypeChange',
                        (['in'], CHANGEKIND, 'changeKind'),
                        (['in'], POINTER(ITypeInfo), 'pTInfoAfter'),
                        (['in'], LPOLESTR, 'pStrName'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ITypeChangeEvents_INTERFACE_DEFINED__

        if not defined(__IErrorInfo_INTERFACE_DEFINED__):
            __IErrorInfo_INTERFACE_DEFINED__ = VOID

            # interface IErrorInfo
            # [unique][uuid][object]
            # [unique]
            LPERRORINFO = POINTER(IErrorInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IErrorInfo = MIDL_INTERFACE(
                    "{1CF2B120-547D-101B-8E65-08002B2BD119}"
                )
                IErrorInfo._iid_ = IID_IErrorInfo

                IErrorInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetGUID')],
                        HRESULT,
                        'GetGUID',
                        (['out'], POINTER(GUID), 'pGUID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSource')],
                        HRESULT,
                        'GetSource',
                        (['out'], POINTER(BSTR), 'pBstrSource'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDescription')],
                        HRESULT,
                        'GetDescription',
                        (['out'], POINTER(BSTR), 'pBstrDescription'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetHelpFile')],
                        HRESULT,
                        'GetHelpFile',
                        (['out'], POINTER(BSTR), 'pBstrHelpFile'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetHelpContext')],
                        HRESULT,
                        'GetHelpContext',
                        (['out'], POINTER(DWORD), 'pdwHelpContext'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __IErrorInfo_INTERFACE_DEFINED__

        if not defined(__ICreateErrorInfo_INTERFACE_DEFINED__):
            __ICreateErrorInfo_INTERFACE_DEFINED__ = VOID

            # interface ICreateErrorInfo
            # [unique][uuid][object]
            # [unique]
            LPCREATEERRORINFO = POINTER(ICreateErrorInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICreateErrorInfo = MIDL_INTERFACE(
                    "{22F03340-547D-101B-8E65-08002B2BD119}"
                )
                ICreateErrorInfo._iid_ = IID_ICreateErrorInfo

                ICreateErrorInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetGUID')],
                        HRESULT,
                        'SetGUID',
                        (['in'], REFGUID, 'rguid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetSource')],
                        HRESULT,
                        'SetSource',
                        (['in'], LPOLESTR, 'szSource'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetDescription')],
                        HRESULT,
                        'SetDescription',
                        (['in'], LPOLESTR, 'szDescription'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpFile')],
                        HRESULT,
                        'SetHelpFile',
                        (['in'], LPOLESTR, 'szHelpFile'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHelpContext')],
                        HRESULT,
                        'SetHelpContext',
                        (['in'], DWORD, 'dwHelpContext'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ICreateErrorInfo_INTERFACE_DEFINED__

        if not defined(__ISupportErrorInfo_INTERFACE_DEFINED__):
            __ISupportErrorInfo_INTERFACE_DEFINED__ = VOID

            # interface ISupportErrorInfo
            # [unique][uuid][object]
            # [unique]
            LPSUPPORTERRORINFO = POINTER(ISupportErrorInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISupportErrorInfo = MIDL_INTERFACE(
                    "{DF0B3D60-548F-101B-8E65-08002B2BD119}"
                )
                ISupportErrorInfo._iid_ = IID_ISupportErrorInfo

                ISupportErrorInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InterfaceSupportsErrorInfo')],
                        HRESULT,
                        'InterfaceSupportsErrorInfo',
                        (['in'], REFIID, 'riid'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ISupportErrorInfo_INTERFACE_DEFINED__

        if not defined(__ITypeFactory_INTERFACE_DEFINED__):
            __ITypeFactory_INTERFACE_DEFINED__ = VOID

            # interface ITypeFactory
            # [uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeFactory = MIDL_INTERFACE(
                    "{0000002E-0000-0000-C000-000000000046}"
                )
                ITypeFactory._iid_ = IID_ITypeFactory

                ITypeFactory._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateFromTypeInfo')],
                        HRESULT,
                        'CreateFromTypeInfo',
                        (['in'], POINTER(ITypeInfo), 'pTypeInfo'),
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(comtypes.IUnknown)), 'ppv'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ITypeFactory_INTERFACE_DEFINED__

        if not defined(__ITypeMarshal_INTERFACE_DEFINED__):
            __ITypeMarshal_INTERFACE_DEFINED__ = VOID

            # interface ITypeMarshal
            # [uuid][object][local]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeMarshal = MIDL_INTERFACE(
                    "{0000002D-0000-0000-C000-000000000046}"
                )
                ITypeMarshal._iid_ = IID_ITypeMarshal

                ITypeMarshal._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Size')],
                        HRESULT,
                        'Size',
                        (['in'], PVOID, 'pvType'),
                        (['in'], DWORD, 'dwDestContext'),
                        (['in'], PVOID, 'pvDestContext'),
                        (['out'], POINTER(ULONG), 'pSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Marshal')],
                        HRESULT,
                        'Marshal',
                        (['in'], PVOID, 'pvType'),
                        (['in'], DWORD, 'dwDestContext'),
                        (['in'], PVOID, 'pvDestContext'),
                        (['in'], ULONG, 'cbBufferLength'),
                        (['out'], POINTER(BYTE), 'pBuffer'),
                        (['out'], POINTER(ULONG), 'pcbWritten'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Unmarshal')],
                        HRESULT,
                        'Unmarshal',
                        (['out'], PVOID, 'pvType'),
                        (['in'], DWORD, 'dwFlags'),
                        (['in'], ULONG, 'cbBufferLength'),
                        (['in'], POINTER(BYTE), 'pBuffer'),
                        (['out'], POINTER(ULONG), 'pcbRead'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Free')],
                        HRESULT,
                        'Free',
                        (['in'], PVOID, 'pvType'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __ITypeMarshal_INTERFACE_DEFINED__

        if not defined(__IRecordInfo_INTERFACE_DEFINED__):
            __IRecordInfo_INTERFACE_DEFINED__ = VOID

            # interface IRecordInfo
            # [uuid][object][local]
            # [unique]
            LPRECORDINFO = POINTER(IRecordInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRecordInfo = MIDL_INTERFACE(
                    "{0000002F-0000-0000-C000-000000000046}"
                )
                IRecordInfo._iid_ = IID_IRecordInfo

                IRecordInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method RecordInit')],
                        HRESULT,
                        'RecordInit',
                        (['out'], PVOID, 'pvNew'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RecordClear')],
                        HRESULT,
                        'RecordClear',
                        (['in'], PVOID, 'pvExisting'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RecordCopy')],
                        HRESULT,
                        'RecordCopy',
                        (['in'], PVOID, 'pvExisting'),
                        (['out'], PVOID, 'pvNew'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetGuid')],
                        HRESULT,
                        'GetGuid',
                        (['out'], POINTER(GUID), 'pguid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetName')],
                        HRESULT,
                        'GetName',
                        (['out'], POINTER(BSTR), 'pbstrName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSize')],
                        HRESULT,
                        'GetSize',
                        (['out'], POINTER(ULONG), 'pcbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetTypeInfo')],
                        HRESULT,
                        'GetTypeInfo',
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTypeInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetField')],
                        HRESULT,
                        'GetField',
                        (['in'], PVOID, 'pvData'),
                        (['in'], LPCOLESTR, 'szFieldName'),
                        (['out'], POINTER(VARIANT), 'pvarField'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFieldNoCopy')],
                        HRESULT,
                        'GetFieldNoCopy',
                        (['in'], PVOID, 'pvData'),
                        (['in'], LPCOLESTR, 'szFieldName'),
                        (['out'], POINTER(VARIANT), 'pvarField'),
                        (['out'], POINTER(PVOID), 'ppvDataCArray'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PutField')],
                        HRESULT,
                        'PutField',
                        (['in'], ULONG, 'wFlags'),
                        (['out', 'in'], PVOID, 'pvData'),
                        (['in'], LPCOLESTR, 'szFieldName'),
                        (['in'], POINTER(VARIANT), 'pvarField'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PutFieldNoCopy')],
                        HRESULT,
                        'PutFieldNoCopy',
                        (['in'], ULONG, 'wFlags'),
                        (['in', 'out'], PVOID, 'pvData'),
                        (['in'], LPCOLESTR, 'szFieldName'),
                        (['in'], POINTER(VARIANT), 'pvarField'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFieldNames')],
                        HRESULT,
                        'GetFieldNames',
                        (['in', 'out'], POINTER(ULONG), 'pcNames'),
                        (['out'], POINTER(BSTR), 'rgBstrNames'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsMatchingType')],
                        BOOL,
                        'IsMatchingType',
                        (['in'], POINTER(IRecordInfo), 'pRecordInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RecordCreate')],
                        PVOID,
                        'RecordCreate',
                    ),
                    COMMETHOD(
                        [helpstring('Method RecordCreateCopy')],
                        HRESULT,
                        'RecordCreateCopy',
                        (['in'], PVOID, 'pvSource'),
                        (['out'], POINTER(PVOID), 'ppvDest'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RecordDestroy')],
                        HRESULT,
                        'RecordDestroy',
                        (['in'], PVOID, 'pvRecord'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __IRecordInfo_INTERFACE_DEFINED__

        if not defined(__IErrorLog_INTERFACE_DEFINED__):
            __IErrorLog_INTERFACE_DEFINED__ = VOID

            # interface IErrorLog
            # [unique][uuid][object]
            LPERRORLOG = POINTER(IErrorLog)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IErrorLog = MIDL_INTERFACE(
                    "{3127CA40-446E-11CE-8135-00AA004BB851}"
                )
                IErrorLog._iid_ = IID_IErrorLog

                IErrorLog._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AddError')],
                        HRESULT,
                        'AddError',
                        (['in'], LPCOLESTR, 'pszPropName'),
                        (['in'], POINTER(EXCEPINFO), 'pExcepInfo'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IErrorLog_INTERFACE_DEFINED__

        if not defined(__IPropertyBag_INTERFACE_DEFINED__):
            __IPropertyBag_INTERFACE_DEFINED__ = VOID

            # interface IPropertyBag
            # [unique][uuid][object]
            LPPROPERTYBAG = POINTER(IPropertyBag)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyBag = MIDL_INTERFACE(
                    "{55272A00-42CB-11CE-8135-00AA004BB851}"
                )
                IPropertyBag._iid_ = IID_IPropertyBag

                IPropertyBag._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Read'), 'local'],
                        HRESULT,
                        'Read',
                        (['in'], LPCOLESTR, 'pszPropName'),
                        (['out', 'in'], POINTER(VARIANT), 'pVar'),
                        (['in', 'unique'], POINTER(IErrorLog), 'pErrorLog'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Write')],
                        HRESULT,
                        'Write',
                        (['in'], LPCOLESTR, 'pszPropName'),
                        (['in'], POINTER(VARIANT), 'pVar'),
                    ),
                ]
            # END IF  C style interface
        # END IF  __IPropertyBag_INTERFACE_DEFINED__

        if not defined(__ITypeLibRegistrationReader_INTERFACE_DEFINED__):
            __ITypeLibRegistrationReader_INTERFACE_DEFINED__ = VOID

            # interface ITypeLibRegistrationReader
            # [uuid][object][local]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeLibRegistrationReader = MIDL_INTERFACE(
                    "{ED6A8A2A-B160-4E77-8F73-AA7435CD5C27}"
                )
                ITypeLibRegistrationReader._iid_ = IID_ITypeLibRegistrationReader

                ITypeLibRegistrationReader._methods_ = [
                    COMMETHOD(
                        [helpstring('Method EnumTypeLibRegistrations')],
                        HRESULT,
                        'EnumTypeLibRegistrations',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumUnknown)),
                            'ppEnumUnknown'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITypeLibRegistrationReader_INTERFACE_DEFINED__

        if not defined(__ITypeLibRegistration_INTERFACE_DEFINED__):
            __ITypeLibRegistration_INTERFACE_DEFINED__ = VOID

            # interface ITypeLibRegistration
            # [uuid][object][local]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITypeLibRegistration = MIDL_INTERFACE(
                    "{76A3E735-02DF-4A12-98EB-043AD3600AF3}"
                )
                ITypeLibRegistration._iid_ = IID_ITypeLibRegistration

                ITypeLibRegistration._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetGuid')],
                        HRESULT,
                        'GetGuid',
                        (['out'], POINTER(GUID), 'pGuid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVersion')],
                        HRESULT,
                        'GetVersion',
                        (['out'], POINTER(BSTR), 'pVersion'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLcid')],
                        HRESULT,
                        'GetLcid',
                        (['out'], POINTER(LCID), 'pLcid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetWin32Path')],
                        HRESULT,
                        'GetWin32Path',
                        (['out'], POINTER(BSTR), 'pWin32Path'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetWin64Path')],
                        HRESULT,
                        'GetWin64Path',
                        (['out'], POINTER(BSTR), 'pWin64Path'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDisplayName')],
                        HRESULT,
                        'GetDisplayName',
                        (['out'], POINTER(BSTR), 'pDisplayName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFlags')],
                        HRESULT,
                        'GetFlags',
                        (['out'], POINTER(DWORD), 'pFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetHelpDir')],
                        HRESULT,
                        'GetHelpDir',
                        (['out'], POINTER(BSTR), 'pHelpDir'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITypeLibRegistration_INTERFACE_DEFINED__

        # interface __MIDL_itf_oaidl_0000_0023
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if  _MSC_VER >= 800 :
        if _MSC_VER >= 1200:
            pass
        else:
            pass
        # END IF
    # END IF


    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32


    # ULONG             __RPC_USER  BSTR_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG


    # UCHAR * __RPC_USER  BSTR_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = UCHAR


    # UCHAR * __RPC_USER  BSTR_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = UCHAR


    # VOID                      __RPC_USER  BSTR_UserFree(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID


    # ULONG             __RPC_USER  VARIANT_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in VARIANT * );
    VARIANT_UserSize = oleaut32.VARIANT_UserSize
    VARIANT_UserSize.restype = ULONG


    # UCHAR * __RPC_USER  VARIANT_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal = oleaut32.VARIANT_UserMarshal
    VARIANT_UserMarshal.restype = UCHAR


    # UCHAR * __RPC_USER  VARIANT_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal = oleaut32.VARIANT_UserUnmarshal
    VARIANT_UserUnmarshal.restype = UCHAR


    # VOID                      __RPC_USER  VARIANT_UserFree(     __RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree = oleaut32.VARIANT_UserFree
    VARIANT_UserFree.restype = VOID


    # ULONG             __RPC_USER  BSTR_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG


    # UCHAR * __RPC_USER  BSTR_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = UCHAR


    # UCHAR * __RPC_USER  BSTR_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = UCHAR


    # VOID                      __RPC_USER  BSTR_UserFree64(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID


    # ULONG             __RPC_USER  CLEANLOCALSTORAGE_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in CLEANLOCALSTORAGE * );
    CLEANLOCALSTORAGE_UserSize64 = oleaut32.CLEANLOCALSTORAGE_UserSize64
    CLEANLOCALSTORAGE_UserSize64.restype = ULONG


    # UCHAR * __RPC_USER  CLEANLOCALSTORAGE_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in CLEANLOCALSTORAGE * );
    CLEANLOCALSTORAGE_UserMarshal64 = oleaut32.CLEANLOCALSTORAGE_UserMarshal64
    CLEANLOCALSTORAGE_UserMarshal64.restype = UCHAR


    # UCHAR * __RPC_USER  CLEANLOCALSTORAGE_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out CLEANLOCALSTORAGE * );
    CLEANLOCALSTORAGE_UserUnmarshal64 = (
        oleaut32.CLEANLOCALSTORAGE_UserUnmarshal64
    )
    CLEANLOCALSTORAGE_UserUnmarshal64.restype = UCHAR


    # VOID                      __RPC_USER  CLEANLOCALSTORAGE_UserFree64(     __RPC__in ULONG *, __RPC__in CLEANLOCALSTORAGE * );
    CLEANLOCALSTORAGE_UserFree64 = oleaut32.CLEANLOCALSTORAGE_UserFree64
    CLEANLOCALSTORAGE_UserFree64.restype = VOID


    # ULONG             __RPC_USER  VARIANT_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in VARIANT * );
    VARIANT_UserSize64 = oleaut32.VARIANT_UserSize64
    VARIANT_UserSize64.restype = ULONG


    # UCHAR * __RPC_USER  VARIANT_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal64 = oleaut32.VARIANT_UserMarshal64
    VARIANT_UserMarshal64.restype = UCHAR


    # UCHAR * __RPC_USER  VARIANT_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal64 = oleaut32.VARIANT_UserUnmarshal64
    VARIANT_UserUnmarshal64.restype = UCHAR


    # VOID                      __RPC_USER  VARIANT_UserFree64(     __RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree64 = oleaut32.VARIANT_UserFree64
    VARIANT_UserFree64.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF
