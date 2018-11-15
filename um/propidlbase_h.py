import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *
from pyWinAPI.shared.minwindef_h import *

COMMETHOD = comtypes.COMMETHOD
IUnknown = comtypes.IUnknown
ole32 = ctypes.windll.Ole32


IID_IPropertyStorage = MIDL_INTERFACE(
            "{00000138-0000-0000-C000-000000000046}"
        )


class IPropertyStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IPropertyStorage


IID_IPropertySetStorage = MIDL_INTERFACE(
            "{0000013A-0000-0000-C000-000000000046}"
        )


class IPropertySetStorage(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IPropertySetStorage


IID_IEnumSTATPROPSTG = MIDL_INTERFACE(
            "{00000139-0000-0000-C000-000000000046}"
        )


class IEnumSTATPROPSTG(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IEnumSTATPROPSTG


IID_IEnumSTATPROPSETSTG = MIDL_INTERFACE(
            "{0000013B-0000-0000-C000-000000000046}"
        )


class IEnumSTATPROPSETSTG(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IEnumSTATPROPSETSTG


class tagVersionedStream(ctypes.Structure):
    pass


VERSIONEDSTREAM = tagVersionedStream


class tagCAC(ctypes.Structure):
    pass


CAC = tagCAC


class tagCAUB(ctypes.Structure):
    pass


CAUB = tagCAUB


class tagCAI(ctypes.Structure):
    pass


CAI = tagCAI


class tagCAUI(ctypes.Structure):
    pass


CAUI = tagCAUI


class tagCAL(ctypes.Structure):
    pass


CAL = tagCAL


class tagCAUL(ctypes.Structure):
    pass


CAUL = tagCAUL


class tagCAFLT(ctypes.Structure):
    pass


CAFLT = tagCAFLT


class tagCADBL(ctypes.Structure):
    pass


CADBL = tagCADBL


class tagCACY(ctypes.Structure):
    pass


CACY = tagCACY


class tagCADATE(ctypes.Structure):
    pass


CADATE = tagCADATE


class tagCABSTR(ctypes.Structure):
    pass


CABSTR = tagCABSTR


class tagCABSTRBLOB(ctypes.Structure):
    pass


CABSTRBLOB = tagCABSTRBLOB


class tagCABOOL(ctypes.Structure):
    pass


CABOOL = tagCABOOL


class tagCASCODE(ctypes.Structure):
    pass


CASCODE = tagCASCODE


class tagCAPROPVARIANT(ctypes.Structure):
    pass


CAPROPVARIANT = tagCAPROPVARIANT


class tagCAH(ctypes.Structure):
    pass


CAH = tagCAH


class tagCAUH(ctypes.Structure):
    pass


CAUH = tagCAUH


class tagCALPSTR(ctypes.Structure):
    pass


CALPSTR = tagCALPSTR


class tagCALPWSTR(ctypes.Structure):
    pass


CALPWSTR = tagCALPWSTR


class tagCAFILETIME(ctypes.Structure):
    pass


CAFILETIME = tagCAFILETIME


class tagCACLIPDATA(ctypes.Structure):
    pass


CACLIPDATA = tagCACLIPDATA


class tagCACLSID(ctypes.Structure):
    pass


CACLSID = tagCACLSID


class tagPROPVARIANT(ctypes.Structure):
    pass


class tagPROPSPEC(ctypes.Structure):
    pass


PROPSPEC = tagPROPSPEC


class tagSTATPROPSTG(ctypes.Structure):
    pass


STATPROPSTG = tagSTATPROPSTG


class tagSTATPROPSETSTG(ctypes.Structure):
    pass


STATPROPSETSTG = tagSTATPROPSETSTG


class tagPROPVARIANT(ctypes.Structure):
    pass




class tag_inner_PROPVARIANT(ctypes.Structure):
    pass



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

__RPCNDR_H_VERSION__ = None
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

COM_NO_WINDOWS_H = None
if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.shared.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

__propidlbase_h__ = None
if not defined(__propidlbase_h__):
    __propidlbase_h__ = 1

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF



    # Forward Declarations
    __IPropertyStorage_FWD_DEFINED__ = None
    if not defined(__IPropertyStorage_FWD_DEFINED__):
        __IPropertyStorage_INTERFACE_DEFINED__ = None
        __IPropertyStorage_FWD_DEFINED__ = 1
    # END IF  __IPropertyStorage_FWD_DEFINED__

    __IPropertySetStorage_FWD_DEFINED__ = None
    if not defined(__IPropertySetStorage_FWD_DEFINED__):
        __IPropertySetStorage_INTERFACE_DEFINED__ = None
        __IPropertySetStorage_FWD_DEFINED__ = 1
    # END IF  __IPropertySetStorage_FWD_DEFINED__

    __IEnumSTATPROPSTG_FWD_DEFINED__ = None
    if not defined(__IEnumSTATPROPSTG_FWD_DEFINED__):
        __IEnumSTATPROPSTG_INTERFACE_DEFINED__ = None
        __IEnumSTATPROPSTG_FWD_DEFINED__ = 1
    # END IF  __IEnumSTATPROPSTG_FWD_DEFINED__

    __IEnumSTATPROPSETSTG_FWD_DEFINED__ = None
    if not defined(__IEnumSTATPROPSETSTG_FWD_DEFINED__):
        __IEnumSTATPROPSETSTG_INTERFACE_DEFINED__ = None
        __IEnumSTATPROPSETSTG_FWD_DEFINED__ = 1
    # END IF  __IEnumSTATPROPSETSTG_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.objidl_h import * # NOQA
    from pyWinAPI.um.oaidl_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF
    # interface __MIDL_itf_propidlbase_0000_0000
    # [local]
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    # + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - -
    # Microsoft Windows
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - -

    if  _MSC_VER >= 800 :
        pass
    # END IF
    if  _MSC_VER >= 1020 :
        pass
    # END IF
    _PROPIDLBASE_ = None
    if not defined(_PROPIDLBASE_):
        if _MSC_VER >= 1200:
            pass
        # END IF

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            tagVersionedStream._fields_ = [
                ('guidVersion', GUID),
                ('pStream', POINTER(IStream)),
            ]
            LPVERSIONEDSTREAM = POINTER(tagVersionedStream)


            # Flags for IPropertySetStorage::Create
            PROPSETFLAG_DEFAULT = 0
            PROPSETFLAG_NONSIMPLE = 1
            PROPSETFLAG_ANSI = 2

            # (This flag is only supported on StgCreatePropStg & StgOpenPropStg
            PROPSETFLAG_UNBUFFERED = 4

            # (This flag causes a version - 1 property set to be created
            PROPSETFLAG_CASE_SENSITIVE = 8

            # Flags for the reserved PID_BEHAVIOR property
            PROPSET_BEHAVIOR_CASE_SENSITIVE = 1

            if defined(MIDL_PASS):
                # This is the PROPVARIANT definition for marshaling.
                PROPVARIANT = tag_inner_PROPVARIANT

            else:
                # This is the standard C layout of the PROPVARIANT.
                PROPVARIANT = tagPROPVARIANT

            # END IF
            tagCAC._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(CHAR)), # [size_is]
            ]
            tagCAUB._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(UCHAR)), # [size_is]
            ]
            tagCAI._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(SHORT)), # [size_is]
            ]
            tagCAUI._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(USHORT)), # [size_is]
            ]
            tagCAL._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(LONG)), # [size_is]
            ]
            tagCAUL._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(ULONG)), # [size_is]
            ]
            tagCAFLT._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(FLOAT)), # [size_is]
            ]
            tagCADBL._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(DOUBLE)), # [size_is]
            ]
            tagCACY._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(CY)), # [size_is]
            ]
            tagCADATE._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(DATE)), # [size_is]
            ]
            tagCABSTR._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(BSTR)), # [size_is]
            ]
            tagCABSTRBLOB._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(BSTRBLOB)), # [size_is]
            ]
            tagCABOOL._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(VARIANT_BOOL)), # [size_is]
            ]
            tagCASCODE._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(SCODE)), # [size_is]
            ]
            tagCAPROPVARIANT._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(PROPVARIANT)), # [size_is]
            ]
            tagCAH._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(LARGE_INTEGER)), # [size_is]
            ]
            tagCAUH._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(ULARGE_INTEGER)), # [size_is]
            ]
            tagCALPSTR._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(LPSTR)), # [size_is]
            ]
            tagCALPWSTR._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(LPWSTR)), # [size_is]
            ]
            tagCAFILETIME._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(FILETIME)), # [size_is]
            ]
            tagCACLIPDATA._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(CLIPDATA)), # [size_is]
            ]
            tagCACLSID._fields_ = [
                ('cElems', ULONG),
                ('pElems', POINTER(CLSID)), # [size_is]
            ]
            if defined(MIDL_PASS):
                # This is the PROPVARIANT padding layout for marshaling.
                PROPVAR_PAD1 = BYTE
                PROPVAR_PAD2 = BYTE
                PROPVAR_PAD3 = ULONG
            else:
                # This is the standard C layout of the structure.
                PROPVAR_PAD1 = WORD
                PROPVAR_PAD2 = WORD
                PROPVAR_PAD3 = WORD
                tag_inner_PROPVARIANT = 1
            # END IF

            class _Union_1(ctypes.Union):
                _fields_ = [
                    ('cVal', CHAR),
                    ('bVal', UCHAR), # [case()]
                    ('iVal', SHORT), # [case()]
                    ('uiVal', USHORT), # [case()]
                    ('lVal', LONG), # [case()]
                    ('ulVal', ULONG), # [case()]
                    ('intVal', INT), # [case()]
                    ('uintVal', UINT), # [case()]
                    ('hVal', LARGE_INTEGER), # [case()]
                    ('uhVal', ULARGE_INTEGER), # [case()]
                    ('fltVal', FLOAT), # [case()]
                    ('dblVal', DOUBLE), # [case()]
                    ('BOOLVal', VARIANT_BOOL), # [case()]
                    ('BOOL', _VARIANT_BOOL), # [case()]
                    ('scode', SCODE), # [case()]
                    ('cyVal', CY), # [case()]
                    ('date', DATE), # [case()]
                    ('filetime', FILETIME), # [case()]
                    ('puuid', POINTER(CLSID)), # [case()]
                    ('pclipdata', POINTER(CLIPDATA)), # [case()]
                    ('bstrVal', BSTR), # [case()]
                    ('bstrblobVal', BSTRBLOB), # [case()]
                    ('blob', BLOB), # [case()]
                    ('pszVal', LPSTR), # [case()]
                    ('pwszVal', LPWSTR), # [case()]
                    ('punkVal', POINTER(comtypes.IUnknown)), # [case()]
                    ('pdispVal', POINTER(IDispatch)), # [case()]
                    ('pStream', POINTER(IStream)), # [case()]
                    ('pStorage', POINTER(IStorage)), # [case()]
                    ('pVersionedStream', LPVERSIONEDSTREAM), # [case()]
                    ('parray', LPSAFEARRAY), # [case()]
                    ('cac', CAC), # [case()]
                    ('caub', CAUB), # [case()]
                    ('cai', CAI), # [case()]
                    ('caui', CAUI), # [case()]
                    ('cal', CAL), # [case()]
                    ('caul', CAUL), # [case()]
                    ('cah', CAH), # [case()]
                    ('cauh', CAUH), # [case()]
                    ('caflt', CAFLT), # [case()]
                    ('cadbl', CADBL), # [case()]
                    ('caBOOL', CABOOL), # [case()]
                    ('cascode', CASCODE), # [case()]
                    ('cacy', CACY), # [case()]
                    ('cadate', CADATE), # [case()]
                    ('cafiletime', CAFILETIME), # [case()]
                    ('cauuid', CACLSID), # [case()]
                    ('caclipdata', CACLIPDATA), # [case()]
                    ('cabstr', CABSTR), # [case()]
                    ('cabstrblob', CABSTRBLOB), # [case()]
                    ('calpstr', CALPSTR), # [case()]
                    ('calpwstr', CALPWSTR), # [case()]
                    ('capropvar', CAPROPVARIANT), # [case()]
                    ('pcVal', POINTER(CHAR)), # [case()]
                    ('pbVal', POINTER(UCHAR)), # [case()]
                    ('piVal', POINTER(SHORT)), # [case()]
                    ('puiVal', POINTER(USHORT)), # [case()]
                    ('plVal', POINTER(LONG)), # [case()]
                    ('pulVal', POINTER(ULONG)), # [case()]
                    ('pintVal', POINTER(INT)), # [case()]
                    ('puintVal', POINTER(UINT)), # [case()]
                    ('pfltVal', POINTER(FLOAT)), # [case()]
                    ('pdblVal', POINTER(DOUBLE)), # [case()]
                    ('pBOOLVal', POINTER(VARIANT_BOOL)), # [case()]
                    ('pdecVal', POINTER(DECIMAL)), # [case()]
                    ('pscode', POINTER(SCODE)), # [case()]
                    ('pcyVal', POINTER(CY)), # [case()]
                    ('pdate', POINTER(DATE)), # [case()]
                    ('pbstrVal', POINTER(BSTR)), # [case()]
                    ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))), # [case()]
                    ('ppdispVal', POINTER(POINTER(IDispatch))), # [case()]
                    ('pparray', POINTER(LPSAFEARRAY)), # [case()]
                    ('pvarVal', POINTER(PROPVARIANT)), # [case()]
                ]

            tag_inner_PROPVARIANT._Union_1 = _Union_1
            tag_inner_PROPVARIANT._anonymous_ = (
                '_Union_1'
            )

            tag_inner_PROPVARIANT._fields_ = [
                ('vt', VARTYPE),
                ('wReserved1', PROPVAR_PAD1),
                ('wReserved2', PROPVAR_PAD2),
                ('wReserved3', PROPVAR_PAD3),
                ('_Union_1', tag_inner_PROPVARIANT._Union_1)
            ]
            _MSC_EXTENSIONS = None
            MIDL_PASS = None


            if not defined(_MSC_EXTENSIONS):
                pass
            else:
                if not defined(MIDL_PASS):
                    class _Union_2(ctypes.Union):
                        _fields_ = [
                            ('tag_inner_PROPVARIANT', tag_inner_PROPVARIANT),
                            ('decVal', DECIMAL)
                        ]

                    tagPROPVARIANT._anonymous_ = (
                        '_Union_2',
                    )
                    tagPROPVARIANT._Union_2 = _Union_2
                    tagPROPVARIANT.Ifields_ = [
                        ('_Union_2', _Union_2)
                    ]
                # END IF
            # END IF

            if defined(MIDL_PASS):
                # This is the LPPROPVARIANT definition for marshaling.
                LPPROPVARIANT = POINTER(tag_inner_PROPVARIANT)
                REFPROPVARIANT = POINTER(PROPVARIANT)
            else:
                # This is the standard C layout of the PROPVARIANT.
                LPPROPVARIANT = POINTER(tagPROPVARIANT)
                _REFPROPVARIANT_DEFINED = None

                if not defined(_REFPROPVARIANT_DEFINED):
                    _REFPROPVARIANT_DEFINED = 1
                    if defined(__cplusplus):
                        REFPROPVARIANT = POINTER(PROPVARIANT)
                    else:
                        REFPROPVARIANT = POINTER(PROPVARIANT)
                    # END IF
                # END IF
            # END IF MIDL_PASS

            # Reserved global Property IDs
            PID_DICTIONARY = 0
            PID_CODEPAGE = 0x1
            PID_FIRST_USABLE = 0x2
            PID_FIRST_NAME_DEFAULT = 0xFFF
            PID_LOCALE = 0x80000000
            PID_MODIFY_TIME = 0x80000001
            PID_SECURITY = 0x80000002
            PID_BEHAVIOR = 0x80000003
            PID_ILLEGAL = 0xFFFFFFFF

            # Range which is read - only to downlevel implementations
            PID_MIN_READONLY = 0x80000000
            PID_MAX_READONLY = 0xBFFFFFFF
            PRSPEC_INVALID = 0xFFFFFFFF
            PRSPEC_LPWSTR = 0
            PRSPEC_PROPID = 1


            class DUMMYUNIONNAME(ctypes.Union):
                pass

            DUMMYUNIONNAME._fields_ = [
                ('propid', PROPID),
                ('lpwstr', LPOLESTR),  # [case()]
            ]

            tagPROPSPEC.DUMMYUNIONNAME = DUMMYUNIONNAME

            tagPROPSPEC._fields_ = [
                ('ulKind', ULONG),
                ('DUMMYUNIONNAME', tagPROPSPEC.DUMMYUNIONNAME)
            ]

            tagSTATPROPSTG._fields_ = [
                ('lpwstrName', LPOLESTR),
                ('propid', PROPID),
                ('vt', VARTYPE),
            ]

            # Macros for parsing the OS Version of the Property Set Header
            def PROPSETHDR_OSVER_KIND(dwOSVer):
                return HIWORD(dwOSVer)


            def PROPSETHDR_OSVER_MAJOR(dwOSVer):
                return LOBYTE(LOWORD(dwOSVer))


            def PROPSETHDR_OSVER_MINOR(dwOSVer):
                return HIBYTE(LOWORD(dwOSVer))


            PROPSETHDR_OSVERSION_UNKNOWN = 0xFFFFFFFF
            tagSTATPROPSETSTG._fields_ = [
                ('fmtid', FMTID),
                ('clsid', CLSID),
                ('grfFlags', DWORD),
                ('mtime', FILETIME),
                ('ctime', FILETIME),
                ('atime', FILETIME),
                ('dwOSVersion', DWORD),
            ]


            if not defined(__IPropertyStorage_INTERFACE_DEFINED__):
                __IPropertyStorage_INTERFACE_DEFINED__ = 1

                # interface IPropertyStorage
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # MIDL_INTERFACE("00000138 - 0000 - 0000 - C000 - 000000000046")

                    # virtual HRESULT STDMETHODCALLTYPE ReadMultiple(
                    # /* [in] */ ULONG cpspec,
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpspec) PROPSPEC rgpspec[],
                    # /* [size_is][out] */ __RPC__out_ecount_full(cpspec) PROPVARIANT rgpropvar[]) = 0;
                    ReadMultiple = ole32.ReadMultiple
                    ReadMultiple.restype = HRESULT

                    # [in]
                    # [size_is][in]
                    # [size_is][out]
                    # virtual HRESULT STDMETHODCALLTYPE WriteMultiple(
                    # /* [in] */ ULONG cpspec,
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpspec) PROPSPEC rgpspec[],
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpspec) PROPVARIANT rgpropvar[],
                    # /* [in] */ PROPID propidNameFirst) = 0;
                    WriteMultiple = ole32.WriteMultiple
                    WriteMultiple.restype = HRESULT

                    # [in]
                    # [size_is][in]
                    # [size_is][in]
                    # [in]                    # virtual HRESULT STDMETHODCALLTYPE DeleteMultiple(
                    # /* [in] */ ULONG cpspec,
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpspec) PROPSPEC rgpspec[]) = 0;
                    DeleteMultiple = ole32.DeleteMultiple
                    DeleteMultiple.restype = HRESULT

                    # [in]
                    # [size_is][in]                    # virtual HRESULT STDMETHODCALLTYPE ReadPropertyNames(
                    # /* [in] */ ULONG cpropid,
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpropid) PROPID rgpropid[],
                    # /* [size_is][out] */ __RPC__out_ecount_full(cpropid) LPOLESTR rglpwstrName[]) = 0;
                    ReadPropertyNames = ole32.ReadPropertyNames
                    ReadPropertyNames.restype = HRESULT

                    # [in]
                    # [size_is][in]
                    # [size_is][out]                    # virtual HRESULT STDMETHODCALLTYPE WritePropertyNames(
                    # /* [in] */ ULONG cpropid,
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpropid) PROPID rgpropid[],
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpropid) LPOLESTR rglpwstrName[]) = 0;
                    WritePropertyNames = ole32.WritePropertyNames
                    WritePropertyNames.restype = HRESULT

                    # [in]
                    # [size_is][in]
                    # [size_is][in]                    # virtual HRESULT STDMETHODCALLTYPE DeletePropertyNames(
                    # /* [in] */ ULONG cpropid,
                    # /* [size_is][in] */ __RPC__in_ecount_full(cpropid) PROPID rgpropid[]) = 0;
                    DeletePropertyNames = ole32.DeletePropertyNames
                    DeletePropertyNames.restype = HRESULT

                    # [in]
                    # [size_is][in]
                    # [in]
                    # [out]                    # virtual HRESULT STDMETHODCALLTYPE SetTimes(
                    # /* [in] */ __RPC__in FILETIME *pctime,
                    # /* [in] */ __RPC__in FILETIME *patime,
                    # /* [in] */ __RPC__in FILETIME *pmtime) = 0;
                    SetTimes = ole32.SetTimes
                    SetTimes.restype = HRESULT

                    # [in]
                    # [in]
                    # [in]                    # virtual HRESULT STDMETHODCALLTYPE SetClass(
                    # /* [in] */ __RPC__in REFCLSID clsid) = 0;
                    SetClass = ole32.SetClass
                    SetClass.restype = HRESULT

                    # [in]                    # virtual HRESULT STDMETHODCALLTYPE Stat(
                    # /* [out] */ __RPC__out STATPROPSETSTG *pstatpsstg) = 0;
                    Stat = ole32.Stat
                    Stat.restype = HRESULT

                    # [out]
                else: # C style interface
                    IPropertyStorage._methods_ = [
                        # When this IDL file is used for "IProp.dll" (the
                        # standalone property set DLL), we must have local
                        # and remotable routines (call_as routines are used
                        # to remove BSTRs, which are not remotable with some
                        # RPC run - times).
                        # For the remotable routines, we must use pointer
                        # parameters (e.g. "*rgspec" rather than "rgspec[]")
                        # so that the MIDL 2.0 compiler will generate an
                        # interpereted proxy/stub, rather than inline.
                        #
                        #
                        #
                        #
                        #
                        #
                        #
                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'WritePropertyNames',
                            (['in'], ULONG, 'cpropid'),
                            (['in'], PROPID * 0, 'rgpropid'),
                            ([], LPOLESTR * 0, 'rglpwstrName'),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DeletePropertyNames',
                            (['in'], ULONG, 'cpropid'),
                            (['in'], PROPID * 0, 'rgpropid'),
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
                            'Revert',
                        ),

                        COMMETHOD(
                            [],
                            HRESULT,
                            'Enum',
                            (
                                ['out'],
                                POINTER(POINTER(IEnumSTATPROPSTG)),
                               'ppenum'
                            ),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetTimes',
                            (['in'], POINTER(FILETIME), 'pctime'),
                            ([], POINTER(FILETIME), 'patime'),
                            ([], POINTER(FILETIME), 'pmtime'),
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
                            'Stat',
                            (['out'], POINTER(STATPROPSETSTG), 'pstatpsstg'),
                        ),

                    ]
                # END IF  C style interface
            # END IF  __IPropertyStorage_INTERFACE_DEFINED__

            if not defined(__IPropertySetStorage_INTERFACE_DEFINED__):
                __IPropertySetStorage_INTERFACE_DEFINED__ = 1

                # interface IPropertySetStorage
                # [unique][uuid][object]
                # [unique]
                LPPROPERTYSETSTORAGE = POINTER(IPropertySetStorage)

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IPropertySetStorage._methods_ = [
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Create',
                            (['in'], REFFMTID, 'rfmtid'),
                            (['unique', 'in'], POINTER(CLSID), 'pclsid'),
                            (['in'], DWORD, 'grfFlags'),
                            (['in'], DWORD, 'grfMode'),
                            (
                                ['out'],
                                POINTER(POINTER(IPropertyStorage)),
                               'ppprstg'
                            ),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Open',
                            (['in'], REFFMTID, 'rfmtid'),
                            (['in'], DWORD, 'grfMode'),
                            (
                                ['out'],
                                POINTER(POINTER(IPropertyStorage)),
                               'ppprstg'
                            ),
                        ),

                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Delete',
                            (['in'], REFFMTID, 'rfmtid'),
                        ),

                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Enum',
                            (
                                ['out'],
                                POINTER(POINTER(IEnumSTATPROPSETSTG)),
                               'ppenum'
                            ),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IPropertySetStorage_INTERFACE_DEFINED__


            if not defined(__IEnumSTATPROPSTG_INTERFACE_DEFINED__):
                __IEnumSTATPROPSTG_INTERFACE_DEFINED__ = 1

                # interface IEnumSTATPROPSTG
                # [unique][uuid][object]
                # [unique]
                LPENUMSTATPROPSTG = POINTER(IEnumSTATPROPSTG)

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IEnumSTATPROPSTG._methods_ = [
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (
                                ['out', 'in', annotation('_Out_writes_to_(celt, *pceltFetched)')],
                                POINTER(STATPROPSTG),
                               'rgelt'
                            ),
                            (
                                ['out', annotation('_Out_opt_ _Deref_out_range_(0, celt)')],
                                POINTER(ULONG),
                               'pceltFetched'
                            ),
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteNext',
                            (['in'], ULONG, 'celt'),
                            (
                                ['out', 'in'],
                                POINTER(STATPROPSTG),
                               'rgelt'
                            ),
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
                            'Reset',
                        ),

                        #
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Clone',
                            (
                                ['out'],
                                POINTER(POINTER(IEnumSTATPROPSTG)),
                               'ppenum'
                            ),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IEnumSTATPROPSTG_INTERFACE_DEFINED__

            if not defined(__IEnumSTATPROPSETSTG_INTERFACE_DEFINED__):
                __IEnumSTATPROPSETSTG_INTERFACE_DEFINED__ = 1

                LPENUMSTATPROPSETSTG = POINTER(IEnumSTATPROPSETSTG)

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass

                else: # C style interface
                    IEnumSTATPROPSETSTG._methods_ = [
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (
                                ['out',  'in', annotation('_Out_writes_to_(celt, *pceltFetched)')],
                                POINTER(STATPROPSETSTG),
                               'rgelt'
                            ),
                            (
                                ['out', annotation('_Out_opt_ _Deref_out_range_(0, celt)')],
                                POINTER(ULONG),
                               'pceltFetched'
                            ),
                        ),

                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteNext',
                            (['in'], ULONG, 'celt'),
                            (
                                ['out', 'in', 'out'],
                                POINTER(STATPROPSETSTG),
                               'rgelt'
                            ),
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
                            'Reset',
                        ),
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Clone',
                            (
                                ['out'],
                                POINTER(POINTER(IEnumSTATPROPSETSTG)),
                               'ppenum'
                            ),
                        ),
                    ]
                # END IF  C style interface
            # END IF  __IEnumSTATPROPSETSTG_INTERFACE_DEFINED__
            # interface __MIDL_itf_propidlbase_0000_0004
            # [local]
            # [unique]
            LPPROPERTYSTORAGE = POINTER(IPropertyStorage)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        _PROPIDLBASE_ = 1
    # END IF
    if _MSC_VER >= 1200:
        pass
    else:
        pass
    # END IF

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OleAut32

    # UINT LONG
    # __RPC_USER
    # BSTR_UserSize(
    # __RPC__in UINT LONG *,
    #  UINT LONG ,
    # __RPC__in BSTR *
    # );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = LONG
    # UINT CHAR *
    # __RPC_USER
    # BSTR_UserMarshal(
    #  __RPC__in UINT LONG *,
    #  __RPC__inout_xcount(0) UINT CHAR *,
    # __RPC__in BSTR *
    # );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = POINTER(CHAR)
    # UINT CHAR *
    # __RPC_USER
    # BSTR_UserUnmarshal(
    # __RPC__in UINT LONG *,
    #  __RPC__in_xcount(0) UINT CHAR *,
    #  __RPC__out BSTR *
    # );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = POINTER(CHAR)
    # VOID
    # __RPC_USER
    # BSTR_UserFree(
    # __RPC__in UINT LONG *,
    #  __RPC__in BSTR *
    # );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID
    # UINT LONG
    # __RPC_USER
    # LPSAFEARRAY_UserSize(
    # __RPC__in UINT LONG *,
    # UINT LONG            ,
    #  __RPC__in LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserSize = oleaut32.LPSAFEARRAY_UserSize
    LPSAFEARRAY_UserSize.restype = LONG
    # UINT CHAR *
    # __RPC_USER
    # LPSAFEARRAY_UserMarshal(
    # __RPC__in UINT LONG *,
    # __RPC__inout_xcount(0) UINT CHAR *,
    # __RPC__in LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserMarshal = oleaut32.LPSAFEARRAY_UserMarshal
    LPSAFEARRAY_UserMarshal.restype = POINTER(CHAR)
    # UINT CHAR *
    # __RPC_USER
    # LPSAFEARRAY_UserUnmarshal(
    # __RPC__in UINT LONG *,
    #  __RPC__in_xcount(0) UINT CHAR *,
    #  __RPC__out LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserUnmarshal = oleaut32.LPSAFEARRAY_UserUnmarshal
    LPSAFEARRAY_UserUnmarshal.restype = POINTER(CHAR)
    # VOID
    # __RPC_USER
    # LPSAFEARRAY_UserFree(
    # __RPC__in UINT LONG *,
    # __RPC__in LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserFree = oleaut32.LPSAFEARRAY_UserFree
    LPSAFEARRAY_UserFree.restype = VOID
    # UINT LONG
    # __RPC_USER
    # BSTR_UserSize64(
    # __RPC__in UINT LONG *,
    # UINT LONG            ,
    # __RPC__in BSTR *
    # );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = LONG
    # UINT CHAR *
    # __RPC_USER
    # BSTR_UserMarshal64(
    # __RPC__in UINT LONG *,
    #  __RPC__inout_xcount(0) UINT CHAR *,
    # __RPC__in BSTR *
    # );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = POINTER(CHAR)
    # UINT CHAR *
    #__RPC_USER
    # BSTR_UserUnmarshal64(
    # __RPC__in UINT LONG *,
    # __RPC__in_xcount(0) UINT CHAR *,
    # __RPC__out BSTR *
    # );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = POINTER(CHAR)
    # VOID __RPC_USER
    # BSTR_UserFree64(
    # __RPC__in UINT LONG *, __RPC__in BSTR *
    # );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID
    # UINT LONG __RPC_USER  LPSAFEARRAY_UserSize64(
    # __RPC__in UINT LONG *,
    # UINT LONG            , _
    # _RPC__in LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserSize64 = oleaut32.LPSAFEARRAY_UserSize64
    LPSAFEARRAY_UserSize64.restype = LONG
    # UINT CHAR * __RPC_USER  LPSAFEARRAY_UserMarshal64(
    #  __RPC__in UINT LONG *,
    #  __RPC__inout_xcount(0) UINT CHAR *,
    #  __RPC__in LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserMarshal64 = oleaut32.LPSAFEARRAY_UserMarshal64
    LPSAFEARRAY_UserMarshal64.restype = POINTER(CHAR)
    # UINT CHAR * __RPC_USER  LPSAFEARRAY_UserUnmarshal64(
    # __RPC__in UINT LONG *,
    # __RPC__in_xcount(0) UINT CHAR *,
    # __RPC__out LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserUnmarshal64 = oleaut32.LPSAFEARRAY_UserUnmarshal64
    LPSAFEARRAY_UserUnmarshal64.restype = POINTER(CHAR)
    # VOID __RPC_USER  LPSAFEARRAY_UserFree64(
    #      __RPC__in UINT LONG *,
    #        __RPC__in LPSAFEARRAY *
    # );
    LPSAFEARRAY_UserFree64 = oleaut32.LPSAFEARRAY_UserFree64
    LPSAFEARRAY_UserFree64.restype = VOID

    if defined(__cplusplus):
        pass
    # END IF
# END IF
