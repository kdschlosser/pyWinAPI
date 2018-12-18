import ctypes
import comtypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__propidlbase_h__ = None
__IPropertyStorage_FWD_DEFINED__ = None
__IPropertySetStorage_FWD_DEFINED__ = None
__IEnumSTATPROPSTG_FWD_DEFINED__ = None
__IEnumSTATPROPSETSTG_FWD_DEFINED__ = None
_PROPIDLBASE_ = None
_MSC_EXTENSIONS = None
_REFPROPVARIANT_DEFINED = None
__IPropertyStorage_INTERFACE_DEFINED__ = None
__IPropertySetStorage_INTERFACE_DEFINED__ = None
__IEnumSTATPROPSTG_INTERFACE_DEFINED__ = None
__IEnumSTATPROPSETSTG_INTERFACE_DEFINED__ = None


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


if not defined(__propidlbase_h__):
    # Forward Declarations
    if not defined(__IPropertyStorage_FWD_DEFINED__):
        class IPropertyStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IPropertyStorage_FWD_DEFINED__

    if not defined(__IPropertySetStorage_FWD_DEFINED__):
        class IPropertySetStorage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertySetStorage_FWD_DEFINED__

    if not defined(__IEnumSTATPROPSTG_FWD_DEFINED__):
        class IEnumSTATPROPSTG(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumSTATPROPSTG_FWD_DEFINED__

    if not defined(__IEnumSTATPROPSETSTG_FWD_DEFINED__):
        class IEnumSTATPROPSETSTG(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

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

    # +
    # -------------------------------------------------------------------------
    # Microsoft Windows
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # --------------------------------------------------------------------

    if _MSC_VER >= 800:
        if _MSC_VER >= 1200:
            pass
        # END IF
    # END IF

    if _MSC_VER >= 1020:
        pass
    # END IF

    if not defined(_PROPIDLBASE_):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            tagVersionedStream._fields_ = [
                ('guidVersion', GUID),
                ('pStream', POINTER(IStream)),
            ]
            LPVERSIONEDSTREAM = POINTER(tagVersionedStream)

            # Flags for IPropertySetStorage::Create
            PROPSETFLAG_DEFAULT = 0
            PROPSETFLAG_NONSIMPLE = 1
            ROPSETFLAG_ANSI = 2

            # This flag is only supported on StgCreatePropStg & StgOpenPropStg
            PROPSETFLAG_UNBUFFERED = 4

            # This flag causes a version-1 property set to be created
            PROPSETFLAG_CASE_SENSITIVE = 8

            # Flags for the reserved PID_BEHAVIOR property
            PROPSET_BEHAVIOR_CASE_SENSITIVE = 1

            if defined(MIDL_PASS):
                # This is the PROPVARIANT definition for marshaling.

                class tag_inner_PROPVARIANT(ctypes.Structure):
                    pass

                PROPVARIANT = tag_inner_PROPVARIANT

            else:
                # This is the standard C layout of the PROPVARIANT.
                class tagPROPVARIANT(ctypes.Structure):
                    pass

                PROPVARIANT = tagPROPVARIANT

            # END IF

            tagCAC._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(CHAR)),
            ]

            tagCAUB._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(UCHAR)),
            ]

            tagCAI._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(SHORT)),
            ]

            tagCAUI._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(USHORT)),
            ]

            tagCAL._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(LONG)),
            ]

            tagCAUL._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(ULONG)),
            ]

            tagCAFLT._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(FLOAT)),
            ]

            tagCADBL._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(DOUBLE)),
            ]

            tagCACY._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(CY)),
            ]

            tagCADATE._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(DATE)),
            ]

            tagCABSTR._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(BSTR)),
            ]

            tagCABSTRBLOB._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(BSTRBLOB)),
            ]

            tagCABOOL._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(VARIANT_BOOL)),
            ]

            tagCASCODE._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(SCODE)),
            ]

            tagCAPROPVARIANT._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(PROPVARIANT)),
            ]

            tagCAH._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(LARGE_INTEGER)),
            ]

            tagCAUH._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(ULARGE_INTEGER)),
            ]

            tagCALPSTR._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(LPSTR)),
            ]

            tagCALPWSTR._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(LPWSTR)),
            ]

            tagCAFILETIME._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(FILETIME)),
            ]

            tagCACLIPDATA._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(CLIPDATA)),
            ]

            tagCACLSID._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(CLSID)),
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
                tag_inner_PROPVARIANT = VOID
            # END IF

            if not defined(_MSC_EXTENSIONS):
                class tagPROPVARIANT(ctypes.Structure):
                    pass

            else:
                if not defined(MIDL_PASS):
                    class tagPROPVARIANT(ctypes.Structure):
                        pass

                    class _Union_1(ctypes.Union):
                        pass

                class tag_inner_PROPVARIANT(ctypes.Structure):
                    pass

                class _Union_2(ctypes.Union):
                    pass

                _Union_2._fields_ = [
                    # [case()]
                    ('cVal', CHAR),
                    # [case()]
                    ('bVal', UCHAR),
                    # [case()]
                    ('iVal', SHORT),
                    # [case()]
                    ('uiVal', USHORT),
                    # [case()]
                    ('lVal', LONG),
                    # [case()]
                    ('ulVal', ULONG),
                    # [case()]
                    ('intVal', INT),
                    # [case()]
                    ('uintVal', UINT),
                    # [case()]
                    ('hVal', LARGE_INTEGER),
                    # [case()]
                    ('uhVal', ULARGE_INTEGER),
                    # [case()]
                    ('fltVal', FLOAT),
                    # [case()]
                    ('dblVal', DOUBLE),
                    # [case()]
                    ('boolVal', VARIANT_BOOL),
                    # [case()]
                    ('bool', _VARIANT_BOOL),
                    # [case()]
                    ('scode', SCODE),
                    # [case()]
                    ('cyVal', CY),
                    # [case()]
                    ('date', DATE),
                    # [case()]
                    ('filetime', FILETIME),
                    # [case()]
                    ('puuid', POINTER(CLSID)),
                    # [case()]
                    ('pclipdata', POINTER(CLIPDATA)),
                    # [case()]
                    ('bstrVal', BSTR),
                    # [case()]
                    ('bstrblobVal', BSTRBLOB),
                    # [case()]
                    ('blob', BLOB),
                    # [case()]
                    ('pszVal', LPSTR),
                    # [case()]
                    ('pwszVal', LPWSTR),
                    # [case()]
                    ('punkVal', POINTER(comtypes.IUnknown)),
                    # [case()]
                    ('pdispVal', POINTER(IDispatch)),
                    # [case()]
                    ('pStream', POINTER(IStream)),
                    # [case()]
                    ('pStorage', POINTER(IStorage)),
                    # [case()]
                    ('pVersionedStream', LPVERSIONEDSTREAM),
                    # [case()]
                    ('parray', LPSAFEARRAY),
                    # [case()]
                    ('cac', CAC),
                    # [case()]
                    ('caub', CAUB),
                    # [case()]
                    ('cai', CAI),
                    # [case()]
                    ('caui', CAUI),
                    # [case()]
                    ('cal', CAL),
                    # [case()]
                    ('caul', CAUL),
                    # [case()]
                    ('cah', CAH),
                    # [case()]
                    ('cauh', CAUH),
                    # [case()]
                    ('caflt', CAFLT),
                    # [case()]
                    ('cadbl', CADBL),
                    # [case()]
                    ('cabool', CABOOL),
                    # [case()]
                    ('cascode', CASCODE),
                    # [case()]
                    ('cacy', CACY),
                    # [case()]
                    ('cadate', CADATE),
                    # [case()]
                    ('cafiletime', CAFILETIME),
                    # [case()]
                    ('cauuid', CACLSID),
                    # [case()]
                    ('caclipdata', CACLIPDATA),
                    # [case()]
                    ('cabstr', CABSTR),
                    # [case()]
                    ('cabstrblob', CABSTRBLOB),
                    # [case()]
                    ('calpstr', CALPSTR),
                    # [case()]
                    ('calpwstr', CALPWSTR),
                    # [case()]
                    ('capropvar', CAPROPVARIANT),
                    # [case()]
                    ('pcVal', POINTER(CHAR)),
                    # [case()]
                    ('pbVal', POINTER(UCHAR)),
                    # [case()]
                    ('piVal', POINTER(SHORT)),
                    # [case()]
                    ('puiVal', POINTER(USHORT)),
                    # [case()]
                    ('plVal', POINTER(LONG)),
                    # [case()]
                    ('pulVal', POINTER(ULONG)),
                    # [case()]
                    ('pintVal', POINTER(INT)),
                    # [case()]
                    ('puintVal', POINTER(UINT)),
                    # [case()]
                    ('pfltVal', POINTER(FLOAT)),
                    # [case()]
                    ('pdblVal', POINTER(DOUBLE)),
                    # [case()]
                    ('pboolVal', POINTER(VARIANT_BOOL)),
                    # [case()]
                    ('pdecVal', POINTER(DECIMAL)),
                    # [case()]
                    ('pscode', POINTER(SCODE)),
                    # [case()]
                    ('pcyVal', POINTER(CY)),
                    # [case()]
                    ('pdate', POINTER(DATE)),
                    # [case()]
                    ('pbstrVal', POINTER(BSTR)),
                    # [case()]
                    ('ppunkVal', POINTER(POINTER(comtypes.IUnknown))),
                    # [case()]
                    ('ppdispVal', POINTER(POINTER(IDispatch))),
                    # [case()]
                    ('pparray', POINTER(LPSAFEARRAY)),
                    # [case()]
                    ('pvarVal', POINTER(PROPVARIANT)),
                ]

                tag_inner_PROPVARIANT._Union_2 = _Union_2

                tag_inner_PROPVARIANT._anonymous_ = (
                    '_Union_2',
                )

                tag_inner_PROPVARIANT._fields_ = [
                    ('vt', VARTYPE),
                    ('wReserved1', PROPVAR_PAD1),
                    ('wReserved2', PROPVAR_PAD2),
                    ('wReserved3', PROPVAR_PAD3),
                    # [switch_is]
                    ('_Union_2', tag_inner_PROPVARIANT._Union_2),
                ]

                if not defined(MIDL_PASS):
                    _Union_1.tag_inner_PROPVARIANT = tag_inner_PROPVARIANT

                    _Union_1._fields_ = [
                        ('tag_inner_PROPVARIANT', _Union_1.tag_inner_PROPVARIANT),
                        ('decVal', DECIMAL),
                    ]
                    tagPROPVARIANT._Union_1 = _Union_1
                    tagPROPVARIANT._anonymous_ = (
                        '_Union_1',
                    )
                    tagPROPVARIANT._fields_ = [
                        ('_Union_1', tagPROPVARIANT._Union_1),
                    ]
                # END IF

            # END IF  _MSC_EXTENSIONS

            if defined(MIDL_PASS):
                # This is the LPPROPVARIANT definition for marshaling.
                LPPROPVARIANT = POINTER(tag_inner_PROPVARIANT)
                REFPROPVARIANT = POINTER(PROPVARIANT)
            else:
                # This is the standard C layout of the PROPVARIANT.
                LPPROPVARIANT = POINTER(tagPROPVARIANT)

                if not defined(_REFPROPVARIANT_DEFINED):
                    if defined(__cplusplus):
                        pass
                    else:
                        pass
                    # END IF
                # END IF
            # END IF   MIDL_PASS

            PID_DICTIONARY = 0
            PID_CODEPAGE = 0x1
            PID_FIRST_USABLE = 0x2
            PID_FIRST_NAME_DEFAULT = 0xfff
            PID_LOCALE = 0x80000000
            PID_MODIFY_TIME = 0x80000001
            PID_SECURITY = 0x80000002
            PID_BEHAVIOR = 0x80000003
            PID_ILLEGAL = 0xffffffff

            # Rangewhich is read - only to ownlevel implementations
            PID_MIN_READONLY = 0x80000000
            PID_MAX_READONLY = 0xbfffffff
            PRSPEC_INVALID = 0xffffffff
            PRSPEC_LPWSTR = 0
            PRSPEC_PROPID = 1

            # Reserved global Property IDs
            # Range which is read-only to downlevel implementations
            class DUMMYUNIONNAME(ctypes.Union):
                pass

            DUMMYUNIONNAME._fields_ = [
                # [case()]
                ('propid', PROPID),
                # [case()]
                ('lpwstr', LPOLESTR),
            ]
            tagPROPSPEC.DUMMYUNIONNAME = DUMMYUNIONNAME

            tagPROPSPEC._fields_ = [
                ('ulKind', ULONG),
                # [switch_is]
                ('DUMMYUNIONNAME', tagPROPSPEC.DUMMYUNIONNAME),
            ]

            tagSTATPROPSTG._fields_ = [
                ('lpwstrName', LPOLESTR),
                ('propid', PROPID),
                ('vt', VARTYPE),
            ]

            # Macros for parsing the OS Version of the Property Set Header
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
                # interface IPropertyStorage
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPropertyStorage = MIDL_INTERFACE(
                        "{00000138-0000-0000-C000-000000000046}"
                    )
                    IPropertyStorage._iid_ = IID_IPropertyStorage

                    IPropertyStorage._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ReadMultiple')],
                            HRESULT,
                            'ReadMultiple',
                            (['in'], ULONG, 'cpspec'),
                            (['in'], PROPSPEC * 0, 'rgpspec'),
                            (['out'], PROPVARIANT * 0, 'rgpropvar'),
                        ),
                        COMMETHOD(
                            [helpstring('Method WriteMultiple')],
                            HRESULT,
                            'WriteMultiple',
                            (['in'], ULONG, 'cpspec'),
                            (['in'], PROPSPEC * 0, 'rgpspec'),
                            (['in'], PROPVARIANT * 0, 'rgpropvar'),
                            (['in'], PROPID, 'propidNameFirst'),
                        ),
                        COMMETHOD(
                            [helpstring('Method DeleteMultiple')],
                            HRESULT,
                            'DeleteMultiple',
                            (['in'], ULONG, 'cpspec'),
                            (['in'], PROPSPEC * 0, 'rgpspec'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ReadPropertyNames')],
                            HRESULT,
                            'ReadPropertyNames',
                            (['in'], ULONG, 'cpropid'),
                            (['in'], PROPID * 0, 'rgpropid'),
                            (['out'], LPOLESTR * 0, 'rglpwstrName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method WritePropertyNames')],
                            HRESULT,
                            'WritePropertyNames',
                            (['in'], ULONG, 'cpropid'),
                            (['in'], PROPID * 0, 'rgpropid'),
                            (['in'], LPOLESTR * 0, 'rglpwstrName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method DeletePropertyNames')],
                            HRESULT,
                            'DeletePropertyNames',
                            (['in'], ULONG, 'cpropid'),
                            (['in'], PROPID * 0, 'rgpropid'),
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
                            [helpstring('Method Enum')],
                            HRESULT,
                            'Enum',
                            (
                                ['out'],
                                POINTER(POINTER(IEnumSTATPROPSTG)),
                               'ppenum'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetTimes')],
                            HRESULT,
                            'SetTimes',
                            (['in'], POINTER(FILETIME), 'pctime'),
                            (['in'], POINTER(FILETIME), 'patime'),
                            (['in'], POINTER(FILETIME), 'pmtime'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetClass')],
                            HRESULT,
                            'SetClass',
                            (['in'], REFCLSID, 'clsid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Stat')],
                            HRESULT,
                            'Stat',
                            (['out'], POINTER(STATPROPSETSTG), 'pstatpsstg'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IPropertyStorage_INTERFACE_DEFINED__

            if not defined(__IPropertySetStorage_INTERFACE_DEFINED__):
                # interface IPropertySetStorage
                # [unique][uuid][object]
                # [unique]
                LPPROPERTYSETSTORAGE = POINTER(IPropertySetStorage)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IPropertySetStorage = MIDL_INTERFACE(
                        "{0000013A-0000-0000-C000-000000000046}"
                    )
                    IPropertySetStorage._iid_ = IID_IPropertySetStorage

                    IPropertySetStorage._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Create')],
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
                            [helpstring('Method Open')],
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
                        COMMETHOD(
                            [helpstring('Method Delete')],
                            HRESULT,
                            'Delete',
                            (['in'], REFFMTID, 'rfmtid'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Enum')],
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
                # interface IEnumSTATPROPSTG
                # [unique][uuid][object]
                # [unique]
                LPENUMSTATPROPSTG = POINTER(IEnumSTATPROPSTG)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IEnumSTATPROPSTG = MIDL_INTERFACE(
                        "{00000139-0000-0000-C000-000000000046}"
                    )
                    IEnumSTATPROPSTG._iid_ = IID_IEnumSTATPROPSTG

                    IEnumSTATPROPSTG._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Next'), 'local'],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (['out'], POINTER(STATPROPSTG), 'rgelt'),
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
                                POINTER(POINTER(IEnumSTATPROPSTG)),
                               'ppenum'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IEnumSTATPROPSTG_INTERFACE_DEFINED__

            if not defined(__IEnumSTATPROPSETSTG_INTERFACE_DEFINED__):
                # interface IEnumSTATPROPSETSTG
                # [unique][uuid][object]
                # [unique]
                LPENUMSTATPROPSETSTG = POINTER(IEnumSTATPROPSETSTG)
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IEnumSTATPROPSETSTG = MIDL_INTERFACE(
                        "{0000013B-0000-0000-C000-000000000046}"
                    )
                    IEnumSTATPROPSETSTG._iid_ = IID_IEnumSTATPROPSETSTG

                    IEnumSTATPROPSETSTG._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Next'), 'local'],
                            HRESULT,
                            'Next',
                            (['in'], ULONG, 'celt'),
                            (['out'], POINTER(STATPROPSETSTG), 'rgelt'),
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
    # END IF

    if _MSC_VER >= 1200:
        pass
    else:
        pass
    # END IF

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG              BSTR_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG

    # UCHAR *  BSTR_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  BSTR_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       BSTR_UserFree(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID

    # ULONG              LPSAFEARRAY_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize = oleaut32.LPSAFEARRAY_UserSize
    LPSAFEARRAY_UserSize.restype = ULONG

    # UCHAR *  LPSAFEARRAY_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal = oleaut32.LPSAFEARRAY_UserMarshal
    LPSAFEARRAY_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  LPSAFEARRAY_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal = oleaut32.LPSAFEARRAY_UserUnmarshal
    LPSAFEARRAY_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       LPSAFEARRAY_UserFree(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree = oleaut32.LPSAFEARRAY_UserFree
    LPSAFEARRAY_UserFree.restype = VOID

    # ULONG              BSTR_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG

    # UCHAR *  BSTR_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  BSTR_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       BSTR_UserFree64(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID

    # ULONG              LPSAFEARRAY_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserSize64 = oleaut32.LPSAFEARRAY_UserSize64
    LPSAFEARRAY_UserSize64.restype = ULONG

    # UCHAR *  LPSAFEARRAY_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserMarshal64 = oleaut32.LPSAFEARRAY_UserMarshal64
    LPSAFEARRAY_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  LPSAFEARRAY_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out LPSAFEARRAY * );
    LPSAFEARRAY_UserUnmarshal64 = oleaut32.LPSAFEARRAY_UserUnmarshal64
    LPSAFEARRAY_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       LPSAFEARRAY_UserFree64(     __RPC__in ULONG *, __RPC__in LPSAFEARRAY * );
    LPSAFEARRAY_UserFree64 = oleaut32.LPSAFEARRAY_UserFree64
    LPSAFEARRAY_UserFree64.restype = VOID

    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


