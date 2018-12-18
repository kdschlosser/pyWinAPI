import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_OLEAUTO_H_ = None
_OLEAUT32_ = None
_LCID_DEFINED = None
BEGIN_INTERFACE = None
LOCALE_USE_NLS = None
_FORCENAMELESSUNION = None
NONAMELESSUNION = None
_MSC_EXTENSIONS = None
__STDC__ = None


class NUMPARSE(ctypes.Structure):
    pass


class UDATE(ctypes.Structure):
    pass


class tagPARAMDATA(ctypes.Structure):
    pass


PARAMDATA = tagPARAMDATA
LPPARAMDATA = POINTER(tagPARAMDATA)


class tagMETHODDATA(ctypes.Structure):
    pass


METHODDATA = tagMETHODDATA
LPMETHODDATA = POINTER(tagMETHODDATA)


class tagINTERFACEDATA(ctypes.Structure):
    pass


INTERFACEDATA = tagINTERFACEDATA
LPINTERFACEDATA = POINTER(tagINTERFACEDATA)


from pyWinAPI.shared.winapifamily_h import * # NOQA
if _MSC_VER >= 1200:
    pass
# END IF


# + ---------------------------------------------------------------------------
# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  oleauto.h
# Contents: Defines Ole Automation support function prototypes, constants
# ----------------------------------------------------------------------------
if not defined(_OLEAUTO_H_):
    _OLEAUTO_H_ = VOID
    if _MSC_VER > 1000:
        pass
    # END IF

    # Set packing to 8 for ISV, and Win95 support
    if not defined(RC_INVOKED):
        from pyWinAPI.shared.pshpack8_h import * # NOQA
    # END IF   RC_INVOKED

    # Definition of the OLE Automation APIs, and macros.
    if defined(_OLEAUT32_):
        WINOLEAUTAPI = STDAPI

        def WINOLEAUTAPI_(type):
            return STDAPI_(type)
    else:
        WINOLEAUTAPI = HRESULT

        def WINOLEAUTAPI_(type):

            return DECLSPEC_IMPORT(type(STDAPICALLTYPE))
    # END IF

    STDOLE_MAJORVERNUM = 0x1
    STDOLE_MINORVERNUM = 0x0
    STDOLE_LCID = 0x0000

    # Version of stdole2.tlb
    STDOLE2_MAJORVERNUM = 0x2
    STDOLE2_MINORVERNUM = 0x0
    STDOLE2_LCID = 0x0000

    # if not already picked up from olenls.h
    if not defined(_LCID_DEFINED):
        LCID = DWORD
        _LCID_DEFINED = VOID
    # END IF  _LCID_DEFINED

    if not defined(BEGIN_INTERFACE):
        BEGIN_INTERFACE = VOID
        END_INTERFACE = VOID
    # END IF

    # pull in the MIDL generated header
    from pyWinAPI.um.oaidl_h import * # NOQA

    # ---------------------------------------------------------------------
    # BSTR API
    # ---------------------------------------------------------------------
    oleaut32 = ctypes.windll.OLEAUT32

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI_(BSTR) SysAllocString(_In_opt_z_ OLECHAR * psz);
        SysAllocString = oleaut32.SysAllocString
        SysAllocString.restype = BSTR

        # WINOLEAUTAPI_(INT)  SysReAllocString(_Inout_ _At_(*pbstr, _Pre_z_ _Post_z_ _Post_readable_size_(_String_length_(psz) + 1)) BSTR* pbstr, _In_opt_z_ OLECHAR* psz);
        SysReAllocString = oleaut32.SysReAllocString
        SysReAllocString.restype = INT

        # WINOLEAUTAPI SysAddRefString(_In_ BSTR bstrString);
        SysAddRefString = oleaut32.SysAddRefString
        SysAddRefString.restype = WINOLEAUTAPI

        # WINOLEAUTAPI_(VOID) SysReleaseString(_In_ BSTR bstrString);
        SysReleaseString = oleaut32.SysReleaseString
        SysReleaseString.restype = VOID

        # WINOLEAUTAPI_(VOID) SysFreeString(_In_opt_ BSTR bstrString);
        SysFreeString = oleaut32.SysFreeString
        SysFreeString.restype = VOID

        # WINOLEAUTAPI_(_Post_equal_to_(pbstr == NULL ? 0 : _String_length_(pbstr)) UINT) SysStringLen(_In_opt_ BSTR pbstr);
        SysStringLen = oleaut32.SysStringLen
        SysStringLen.restype = UINT

        if defined(_WIN32) or defined(_WIN64):
            # WINOLEAUTAPI_(_Post_equal_to_(_String_length_(bstr) * (ctypes.sizeof(OLECHAR)) UINT) SysStringByteLen(_In_opt_ BSTR bstr);
            SysStringByteLen = oleaut32.SysStringByteLen
            SysStringByteLen.restype = UINT
            # WINOLEAUTAPI_(BSTR) SysAllocStringByteLen(_In_opt_z_ LPCSTR psz, _In_ UINT len);
            SysAllocStringByteLen = oleaut32.SysAllocStringByteLen
            SysAllocStringByteLen.restype = BSTR
        # END IF  (defined (_WIN32) or defined (_WIN64))
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # ---------------------------------------------------------------------
    # Time API
    # ---------------------------------------------------------------------
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI_(INT) DosDateTimeToVariantTime(_In_ USHORT wDosDate, _In_ USHORT wDosTime, _Out_ DOUBLE * pvtime);
        DosDateTimeToVariantTime = oleaut32.DosDateTimeToVariantTime
        DosDateTimeToVariantTime.restype = INT

        # WINOLEAUTAPI_(INT) VariantTimeToDosDateTime(_In_ DOUBLE vtime, _Out_ USHORT * pwDosDate, _Out_ USHORT * pwDosTime);
        VariantTimeToDosDateTime = oleaut32.VariantTimeToDosDateTime
        VariantTimeToDosDateTime.restype = INT

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if (defined (_WIN32) or defined (_WIN64)):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # WINOLEAUTAPI_(INT) SystemTimeToVariantTime(_In_ LPSYSTEMTIME lpSystemTime, _Out_ DOUBLE *pvtime);
            SystemTimeToVariantTime = oleaut32.SystemTimeToVariantTime
            SystemTimeToVariantTime.restype = INT

            # WINOLEAUTAPI_(INT) VariantTimeToSystemTime(_In_ DOUBLE vtime, _Out_ LPSYSTEMTIME lpSystemTime);
            VariantTimeToSystemTime = oleaut32.VariantTimeToSystemTime
            VariantTimeToSystemTime.restype = INT

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # END IF  (defined (_WIN32) or defined (_WIN64))

    # ---------------------------------------------------------------------
    # SafeArray API
    # ---------------------------------------------------------------------
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI SafeArrayAllocDescriptor(_In_ UINT cDims, _Outptr_ SAFEARRAY ** ppsaOut);
        SafeArrayAllocDescriptor = oleaut32.SafeArrayAllocDescriptor
        SafeArrayAllocDescriptor.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayAllocDescriptorEx(_In_ VARTYPE vt, _In_ UINT cDims, _Outptr_ SAFEARRAY ** ppsaOut);
        SafeArrayAllocDescriptorEx = oleaut32.SafeArrayAllocDescriptorEx
        SafeArrayAllocDescriptorEx.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayAllocData(_In_ SAFEARRAY * psa);
        SafeArrayAllocData = oleaut32.SafeArrayAllocData
        SafeArrayAllocData.restype = WINOLEAUTAPI

        # WINOLEAUTAPI_(SAFEARRAY *) SafeArrayCreate(_In_ VARTYPE vt, _In_ UINT cDims, _In_ SAFEARRAYBOUND * rgsabound);
        SafeArrayCreate = oleaut32.SafeArrayCreate
        SafeArrayCreate.restype = POINTER(SAFEARRAY)

        # WINOLEAUTAPI_(SAFEARRAY *) SafeArrayCreateEx(_In_ VARTYPE vt, _In_ UINT cDims, _In_ SAFEARRAYBOUND * rgsabound, _In_ PVOID pvExtra);
        SafeArrayCreateEx = oleaut32.SafeArrayCreateEx
        SafeArrayCreateEx.restype = POINTER(SAFEARRAY)

        # _Check_return_
        # WINOLEAUTAPI SafeArrayCopyData(_In_ SAFEARRAY *psaSource, _In_ SAFEARRAY *psaTarget);
        SafeArrayCopyData = oleaut32.SafeArrayCopyData
        SafeArrayCopyData.restype = WINOLEAUTAPI

        # WINOLEAUTAPI_(VOID) SafeArrayReleaseDescriptor(_In_ SAFEARRAY * psa);
        SafeArrayReleaseDescriptor = oleaut32.SafeArrayReleaseDescriptor
        SafeArrayReleaseDescriptor.restype = VOID

        # WINOLEAUTAPI SafeArrayDestroyDescriptor(_In_ SAFEARRAY * psa);
        SafeArrayDestroyDescriptor = oleaut32.SafeArrayDestroyDescriptor
        SafeArrayDestroyDescriptor.restype = WINOLEAUTAPI

        # WINOLEAUTAPI_(VOID) SafeArrayReleaseData(_In_ PVOID pData);
        SafeArrayReleaseData = oleaut32.SafeArrayReleaseData
        SafeArrayReleaseData.restype = VOID

        # WINOLEAUTAPI SafeArrayDestroyData(_In_ SAFEARRAY * psa);
        SafeArrayDestroyData = oleaut32.SafeArrayDestroyData
        SafeArrayDestroyData.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayAddRef(_In_ SAFEARRAY * psa, _Out_ PVOID *ppDataToRelease);
        SafeArrayAddRef = oleaut32.SafeArrayAddRef
        SafeArrayAddRef.restype = WINOLEAUTAPI
        # WINOLEAUTAPI SafeArrayDestroy(_In_ SAFEARRAY * psa);
        SafeArrayDestroy = oleaut32.SafeArrayDestroy
        SafeArrayDestroy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayRedim(_Inout_ SAFEARRAY * psa, _In_ SAFEARRAYBOUND * psaboundNew);
        SafeArrayRedim = oleaut32.SafeArrayRedim
        SafeArrayRedim.restype = WINOLEAUTAPI

        # WINOLEAUTAPI_(UINT) SafeArrayGetDim(_In_ SAFEARRAY * psa);
        SafeArrayGetDim = oleaut32.SafeArrayGetDim
        SafeArrayGetDim.restype = UINT

        # WINOLEAUTAPI_(UINT) SafeArrayGetElemsize(_In_ SAFEARRAY * psa);
        SafeArrayGetElemsize = oleaut32.SafeArrayGetElemsize
        SafeArrayGetElemsize.restype = UINT

        # WINOLEAUTAPI SafeArrayGetUBound(_In_ SAFEARRAY * psa, _In_ UINT nDim, _Out_ LONG * plUbound);
        SafeArrayGetUBound = oleaut32.SafeArrayGetUBound
        SafeArrayGetUBound.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayGetLBound(_In_ SAFEARRAY * psa, _In_ UINT nDim, _Out_ LONG * plLbound);
        SafeArrayGetLBound = oleaut32.SafeArrayGetLBound
        SafeArrayGetLBound.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayLock(_In_ SAFEARRAY * psa);
        SafeArrayLock = oleaut32.SafeArrayLock
        SafeArrayLock.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayUnlock(_In_ SAFEARRAY * psa);
        SafeArrayUnlock = oleaut32.SafeArrayUnlock
        SafeArrayUnlock.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayUnaccessData(_In_ SAFEARRAY * psa);
        SafeArrayUnaccessData = oleaut32.SafeArrayUnaccessData
        SafeArrayUnaccessData.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayGetElement(_In_ SAFEARRAY * psa, _In_reads_(_Inexpressible_(psa.cDims)) LONG * rgIndices, _Out_ VOID * pv);
        SafeArrayGetElement = oleaut32.SafeArrayGetElement
        SafeArrayGetElement.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI SafeArrayPutElement(_In_ SAFEARRAY * psa, _In_reads_(_Inexpressible_(psa.cDims)) LONG * rgIndices, _In_ VOID * pv);
        SafeArrayPutElement = oleaut32.SafeArrayPutElement
        SafeArrayPutElement.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI SafeArrayCopy(_In_ SAFEARRAY * psa, _Outptr_ SAFEARRAY ** ppsaOut);
        SafeArrayCopy = oleaut32.SafeArrayCopy
        SafeArrayCopy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayPtrOfIndex(_In_ SAFEARRAY * psa, _In_reads_(psa.cDims) LONG * rgIndices, _Outptr_result_bytebuffer_(psa.cbElements) VOID ** ppvData);
        SafeArrayPtrOfIndex = oleaut32.SafeArrayPtrOfIndex
        SafeArrayPtrOfIndex.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArraySetRecordInfo(_In_ SAFEARRAY * psa, _In_ IRecordInfo * prinfo);
        SafeArraySetRecordInfo = oleaut32.SafeArraySetRecordInfo
        SafeArraySetRecordInfo.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayGetRecordInfo(_In_ SAFEARRAY * psa, _Outptr_ IRecordInfo ** prinfo);
        SafeArrayGetRecordInfo = oleaut32.SafeArrayGetRecordInfo
        SafeArrayGetRecordInfo.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArraySetIID(_In_ SAFEARRAY * psa, _In_ REFGUID guid);
        SafeArraySetIID = oleaut32.SafeArraySetIID
        SafeArraySetIID.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayGetIID(_In_ SAFEARRAY * psa, _Out_ GUID * pguid);
        SafeArrayGetIID = oleaut32.SafeArrayGetIID
        SafeArrayGetIID.restype = WINOLEAUTAPI

        # WINOLEAUTAPI SafeArrayGetVartype(_In_ SAFEARRAY * psa, _Out_ VARTYPE * pvt);
        SafeArrayGetVartype = oleaut32.SafeArrayGetVartype
        SafeArrayGetVartype.restype = WINOLEAUTAPI

        # WINOLEAUTAPI_(SAFEARRAY *) SafeArrayCreateVector(_In_ VARTYPE vt, _In_ LONG lLbound, _In_ ULONG cElements);
        SafeArrayCreateVector = oleaut32.SafeArrayCreateVector
        SafeArrayCreateVector.restype = POINTER(SAFEARRAY)

        # WINOLEAUTAPI_(SAFEARRAY *) SafeArrayCreateVectorEx(_In_ VARTYPE vt, _In_ LONG lLbound, _In_ ULONG cElements, _In_ PVOID pvExtra);
        SafeArrayCreateVectorEx = oleaut32.SafeArrayCreateVectorEx
        SafeArrayCreateVectorEx.restype = POINTER(SAFEARRAY)

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
    # ---------------------------------------------------------------------
    # VARIANT API
    # ---------------------------------------------------------------------
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI_(VOID) VariantInit(_Out_ VARIANTARG * pvarg);
        VariantInit = oleaut32.VariantInit
        VariantInit.restype = VOID

        # WINOLEAUTAPI VariantClear(_Inout_ VARIANTARG * pvarg);
        VariantClear = oleaut32.VariantClear
        VariantClear.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI VariantCopy(_Inout_ VARIANTARG * pvargDest, _In_ VARIANTARG * pvargSrc);
        VariantCopy = oleaut32.VariantCopy
        VariantCopy.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI VariantCopyInd(_Inout_ VARIANT * pvarDest, _In_ VARIANTARG * pvargSrc);
        VariantCopyInd = oleaut32.VariantCopyInd
        VariantCopyInd.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI VariantChangeType(_Inout_ VARIANTARG * pvargDest,
        # _In_ VARIANTARG * pvarSrc, _In_ USHORT wFlags, _In_ VARTYPE vt);
        VariantChangeType = oleaut32.VariantChangeType
        VariantChangeType.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI VariantChangeTypeEx(_Inout_ VARIANTARG * pvargDest,
        # _In_ VARIANTARG * pvarSrc, _In_ LCID lcid, _In_ USHORT wFlags, _In_ VARTYPE vt);
        VariantChangeTypeEx = oleaut32.VariantChangeTypeEx
        VariantChangeTypeEx.restype = WINOLEAUTAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # Flags for VariantChangeType/VariantChangeTypeEx
    VARIANT_NOVALUEPROP = 0x01
    VARIANT_ALPHABOOL = 0x02    # For VT_BOOL to VT_BSTR conversions,

    # convert to "True"/"False" instead of
    # "-1"/"0"
    VARIANT_NOUSEROVERRIDE = 0x04    # For conversions to/from VT_BSTR,

    # passes LOCALE_NOUSEROVERRIDE
    # to core coercion routines
    VARIANT_CALENDAR_HIJRI = 0x08
    VARIANT_LOCALBOOL = 0x10    # For VT_BOOL to VT_BSTR and back,

    # convert to local language rather than
    # English
    VARIANT_CALENDAR_THAI = 0x20    # SOUTHASIA calendar support
    VARIANT_CALENDAR_GREGORIAN = 0x40    # SOUTHASIA calendar support
    VARIANT_USE_NLS = 0x80    # NLS function call support

    # ---------------------------------------------------------------------
    # Vector <.Bstr conversion APIs
    # ---------------------------------------------------------------------
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # ---------------------------------------------------------------------
    # Variant API Flags
    # ---------------------------------------------------------------------
    # /* Any of the coersion functions that converts either from or to a
    # string takes an additional lcid and dwFlags arguments. The lcid argument
    # allows locale specific parsing to occur. The dwFlags allow additional
    # function specific condition to occur. All function that accept the
    # dwFlags argument can include either 0 or LOCALE_NOUSEROVERRIDE flag.
    # /* The VarDateFromStr and VarBstrFromDate functions also accept the
    # VAR_TIMEVALUEONLY and VAR_DATEVALUEONLY flags
    VAR_TIMEVALUEONLY = 0x00000001    # return time value
    VAR_DATEVALUEONLY = 0x00000002    # return date value

    # VarDateFromUdate() only
    VAR_VALIDDATE = 0x00000004

    # Accepted by all date & format APIs
    VAR_CALENDAR_HIJRI = 0x00000008    # use Hijri calender

    # /* Booleans can optionally be accepted in localized form. Pass
    # VAR_LOCALBOOL into VarBoolFromStr and VarBstrFromBool to use localized
    # BOOLEAN names
    VAR_LOCALBOOL = 0x00000010

    # /* When passed into VarFormat and VarFormatFromTokens, prevents
    # substitution of formats in the case where a string is passed in that can
    # not be coverted into the desired type.
    # (for ex, 'Format("Hello", "General Number")')
    VAR_FORMAT_NOSUBSTITUTE = 0x00000020

    # /* For VarBstrFromDate only - forces years to be 4 digits rather than
    # shortening to 2-digits when the years is in the date window.
    VAR_FOURDIGITYEARS = 0x00000040

    # /* Use NLS functions to format date, currency, time, and number.
    if not defined(LOCALE_USE_NLS):
        LOCALE_USE_NLS = 0x10000000
    # END IF

    # SOUTHASIA START
    # /* SOUTHASIA For VarBstrFromDate only - forces years to be 4 digits
    # rather than shortening to 2-digits when the years is in the date window.
    VAR_CALENDAR_THAI = 0x00000080
    VAR_CALENDAR_GREGORIAN = 0x00000100

    # SOUTHASIA END
    VTDATEGRE_MAX = 2958465    # Dec 31, 9999, 0:0:0 in Gregorain Calendar
    VTDATEGRE_MIN = -657434    # Jan 1, 100, 0:0:0 in Gregorain Calendar

    # ---------------------------------------------------------------------
    # VARTYPE Coercion API
    # ---------------------------------------------------------------------
    # /* Note: The routines that convert *from* a string are defined to take a
    # OLECHAR* rather than a BSTR because no allocation is required, and this
    # makes the routines a bit more generic. They may of course still be
    # passed a BSTR as the strIn param.
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI VarUI1FromI2(SHORT sIn, _Out_ BYTE * pbOut);
        VarUI1FromI2 = oleaut32.VarUI1FromI2
        VarUI1FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromI4(LONG lIn, _Out_ BYTE * pbOut);
        VarUI1FromI4 = oleaut32.VarUI1FromI4
        VarUI1FromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromI8(LONG64 i64In, _Out_ BYTE FAR* pbOut);
        VarUI1FromI8 = oleaut32.VarUI1FromI8
        VarUI1FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromR4(FLOAT fltIn, _Out_ BYTE * pbOut);
        VarUI1FromR4 = oleaut32.VarUI1FromR4
        VarUI1FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromR8(DOUBLE dblIn, _Out_ BYTE * pbOut);
        VarUI1FromR8 = oleaut32.VarUI1FromR8
        VarUI1FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromCy(CY cyIn, _Out_ BYTE * pbOut);
        VarUI1FromCy = oleaut32.VarUI1FromCy
        VarUI1FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromDate(DATE dateIn, _Out_ BYTE * pbOut);
        VarUI1FromDate = oleaut32.VarUI1FromDate
        VarUI1FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromStr(_In_ LPCOLESTR strIn, LCID lcid, ULONG dwFlags, _Out_ BYTE * pbOut);
        VarUI1FromStr = oleaut32.VarUI1FromStr
        VarUI1FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromDisp(IDispatch * pdispIn, LCID lcid, _Out_ BYTE * pbOut);
        VarUI1FromDisp = oleaut32.VarUI1FromDisp
        VarUI1FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromBool(VARIANT_BOOL boolIn, _Out_ BYTE * pbOut);
        VarUI1FromBool = oleaut32.VarUI1FromBool
        VarUI1FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromI1(CHAR cIn, _Out_ BYTE *pbOut);
        VarUI1FromI1 = oleaut32.VarUI1FromI1
        VarUI1FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromUI2(USHORT uiIn, _Out_ BYTE *pbOut);
        VarUI1FromUI2 = oleaut32.VarUI1FromUI2
        VarUI1FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromUI4(ULONG ulIn, _Out_ BYTE *pbOut);
        VarUI1FromUI4 = oleaut32.VarUI1FromUI4
        VarUI1FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromUI8(ULONG64 ui64In, _Out_ BYTE FAR* pbOut);
        VarUI1FromUI8 = oleaut32.VarUI1FromUI8
        VarUI1FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI1FromDec(_In_ DECIMAL *pdecIn, _Out_ BYTE *pbOut);
        VarUI1FromDec = oleaut32.VarUI1FromDec
        VarUI1FromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromUI1(BYTE bIn, _Out_ SHORT * psOut);
        VarI2FromUI1 = oleaut32.VarI2FromUI1
        VarI2FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromI4(LONG lIn, _Out_ SHORT * psOut);
        VarI2FromI4 = oleaut32.VarI2FromI4
        VarI2FromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromI8(LONG64 i64In, _Out_ SHORT FAR* psOut);
        VarI2FromI8 = oleaut32.VarI2FromI8
        VarI2FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromR4(FLOAT fltIn, _Out_ SHORT * psOut);
        VarI2FromR4 = oleaut32.VarI2FromR4
        VarI2FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromR8(DOUBLE dblIn, _Out_ SHORT * psOut);
        VarI2FromR8 = oleaut32.VarI2FromR8
        VarI2FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromCy(CY cyIn, SHORT * psOut);
        VarI2FromCy = oleaut32.VarI2FromCy
        VarI2FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromDate(DATE dateIn, _Out_ SHORT * psOut);
        VarI2FromDate = oleaut32.VarI2FromDate
        VarI2FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromStr(_In_ LPCOLESTR strIn, LCID lcid, ULONG dwFlags, _Out_ SHORT * psOut);
        VarI2FromStr = oleaut32.VarI2FromStr
        VarI2FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromDisp(IDispatch * pdispIn, LCID lcid, _Out_ SHORT * psOut);
        VarI2FromDisp = oleaut32.VarI2FromDisp
        VarI2FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromBool(VARIANT_BOOL boolIn, _Out_ SHORT * psOut);
        VarI2FromBool = oleaut32.VarI2FromBool
        VarI2FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromI1(CHAR cIn, _Out_ SHORT *psOut);
        VarI2FromI1 = oleaut32.VarI2FromI1
        VarI2FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromUI2(USHORT uiIn, _Out_ SHORT *psOut);
        VarI2FromUI2 = oleaut32.VarI2FromUI2
        VarI2FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromUI4(ULONG ulIn, _Out_ SHORT *psOut);
        VarI2FromUI4 = oleaut32.VarI2FromUI4
        VarI2FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromUI8(ULONG64 ui64In, _Out_ SHORT FAR* psOut);
        VarI2FromUI8 = oleaut32.VarI2FromUI8
        VarI2FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI2FromDec(_In_ DECIMAL *pdecIn, _Out_ SHORT *psOut);
        VarI2FromDec = oleaut32.VarI2FromDec
        VarI2FromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromUI1(BYTE bIn, _Out_ LONG * plOut);
        VarI4FromUI1 = oleaut32.VarI4FromUI1
        VarI4FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromI2(SHORT sIn, _Out_ LONG * plOut);
        VarI4FromI2 = oleaut32.VarI4FromI2
        VarI4FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromI8(LONG64 i64In, _Out_ LONG FAR* plOut);
        VarI4FromI8 = oleaut32.VarI4FromI8
        VarI4FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromR4(FLOAT fltIn, _Out_ LONG * plOut);
        VarI4FromR4 = oleaut32.VarI4FromR4
        VarI4FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromR8(DOUBLE dblIn, _Out_ LONG * plOut);
        VarI4FromR8 = oleaut32.VarI4FromR8
        VarI4FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromCy(CY cyIn, _Out_ LONG * plOut);
        VarI4FromCy = oleaut32.VarI4FromCy
        VarI4FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromDate(DATE dateIn, _Out_ LONG * plOut);
        VarI4FromDate = oleaut32.VarI4FromDate
        VarI4FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromStr(_In_ LPCOLESTR strIn, LCID lcid, ULONG dwFlags, _Out_ LONG * plOut);
        VarI4FromStr = oleaut32.VarI4FromStr
        VarI4FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromDisp(IDispatch * pdispIn, _In_ LCID lcid, _Out_ LONG * plOut);
        VarI4FromDisp = oleaut32.VarI4FromDisp
        VarI4FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromBool(VARIANT_BOOL boolIn, _Out_ LONG * plOut);
        VarI4FromBool = oleaut32.VarI4FromBool
        VarI4FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromI1(CHAR cIn, _Out_ LONG *plOut);
        VarI4FromI1 = oleaut32.VarI4FromI1
        VarI4FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromUI2(USHORT uiIn, _Out_ LONG *plOut);
        VarI4FromUI2 = oleaut32.VarI4FromUI2
        VarI4FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromUI4(ULONG ulIn, _Out_ LONG *plOut);
        VarI4FromUI4 = oleaut32.VarI4FromUI4
        VarI4FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromUI8(ULONG64 ui64In, _Out_ LONG FAR* plOut);
        VarI4FromUI8 = oleaut32.VarI4FromUI8
        VarI4FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromDec(_In_ DECIMAL *pdecIn, _Out_ LONG *plOut);
        VarI4FromDec = oleaut32.VarI4FromDec
        VarI4FromDec.restype = WINOLEAUTAPI

        # **************************************
        # WINOLEAUTAPI VarI8FromUI1(BYTE bIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromUI1 = oleaut32.VarI8FromUI1
        VarI8FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromI2(SHORT sIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromI2 = oleaut32.VarI8FromI2
        VarI8FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromR4(FLOAT fltIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromR4 = oleaut32.VarI8FromR4
        VarI8FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromR8(DOUBLE dblIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromR8 = oleaut32.VarI8FromR8
        VarI8FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromCy(_In_ CY cyIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromCy = oleaut32.VarI8FromCy
        VarI8FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromDate(DATE dateIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromDate = oleaut32.VarI8FromDate
        VarI8FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ LONG64 FAR* pi64Out);
        VarI8FromStr = oleaut32.VarI8FromStr
        VarI8FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromDisp(IDispatch FAR* pdispIn, _In_ LCID lcid, _Out_ LONG64 FAR* pi64Out);
        VarI8FromDisp = oleaut32.VarI8FromDisp
        VarI8FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromBool(VARIANT_BOOL boolIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromBool = oleaut32.VarI8FromBool
        VarI8FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromI1(CHAR cIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromI1 = oleaut32.VarI8FromI1
        VarI8FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromUI2(USHORT uiIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromUI2 = oleaut32.VarI8FromUI2
        VarI8FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromUI4(ULONG ulIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromUI4 = oleaut32.VarI8FromUI4
        VarI8FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromUI8(ULONG64 ui64In, _Out_ LONG64 FAR* pi64Out);
        VarI8FromUI8 = oleaut32.VarI8FromUI8
        VarI8FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI8FromDec(_In_ DECIMAL *pdecIn, _Out_ LONG64 FAR* pi64Out);
        VarI8FromDec = oleaut32.VarI8FromDec
        VarI8FromDec.restype = WINOLEAUTAPI

        # *****************
        # WINOLEAUTAPI VarR4FromUI1(BYTE bIn, _Out_ FLOAT * pfltOut);
        VarR4FromUI1 = oleaut32.VarR4FromUI1
        VarR4FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromI2(SHORT sIn, _Out_ FLOAT * pfltOut);
        VarR4FromI2 = oleaut32.VarR4FromI2
        VarR4FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromI4(LONG lIn, _Out_ FLOAT * pfltOut);
        VarR4FromI4 = oleaut32.VarR4FromI4
        VarR4FromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromI8(LONG64 i64In, _Out_ FLOAT FAR* pfltOut);
        VarR4FromI8 = oleaut32.VarR4FromI8
        VarR4FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromR8(DOUBLE dblIn, _Out_ FLOAT * pfltOut);
        VarR4FromR8 = oleaut32.VarR4FromR8
        VarR4FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromCy(CY cyIn, FLOAT * pfltOut);
        VarR4FromCy = oleaut32.VarR4FromCy
        VarR4FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromDate(DATE dateIn, _Out_ FLOAT * pfltOut);
        VarR4FromDate = oleaut32.VarR4FromDate
        VarR4FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromStr(_In_ LPCOLESTR strIn, LCID lcid, ULONG dwFlags, _Out_ FLOAT *pfltOut);
        VarR4FromStr = oleaut32.VarR4FromStr
        VarR4FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromDisp(IDispatch * pdispIn, LCID lcid, _Out_ FLOAT * pfltOut);
        VarR4FromDisp = oleaut32.VarR4FromDisp
        VarR4FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromBool(VARIANT_BOOL boolIn, _Out_ FLOAT * pfltOut);
        VarR4FromBool = oleaut32.VarR4FromBool
        VarR4FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromI1(CHAR cIn, _Out_ FLOAT *pfltOut);
        VarR4FromI1 = oleaut32.VarR4FromI1
        VarR4FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromUI2(USHORT uiIn, _Out_ FLOAT *pfltOut);
        VarR4FromUI2 = oleaut32.VarR4FromUI2
        VarR4FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromUI4(ULONG ulIn, _Out_ FLOAT *pfltOut);
        VarR4FromUI4 = oleaut32.VarR4FromUI4
        VarR4FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromUI8(ULONG64 ui64In, _Out_ FLOAT FAR* pfltOut);
        VarR4FromUI8 = oleaut32.VarR4FromUI8
        VarR4FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR4FromDec(_In_ DECIMAL *pdecIn, _Out_ FLOAT *pfltOut);
        VarR4FromDec = oleaut32.VarR4FromDec
        VarR4FromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromUI1(BYTE bIn, _Out_ DOUBLE * pdblOut);
        VarR8FromUI1 = oleaut32.VarR8FromUI1
        VarR8FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromI2(SHORT sIn, _Out_ DOUBLE * pdblOut);
        VarR8FromI2 = oleaut32.VarR8FromI2
        VarR8FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromI4(LONG lIn, _Out_ DOUBLE * pdblOut);
        VarR8FromI4 = oleaut32.VarR8FromI4
        VarR8FromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromI8(LONG64 i64In, _Out_ DOUBLE FAR* pdblOut);
        VarR8FromI8 = oleaut32.VarR8FromI8
        VarR8FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromR4(FLOAT fltIn, _Out_ DOUBLE * pdblOut);
        VarR8FromR4 = oleaut32.VarR8FromR4
        VarR8FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromCy(CY cyIn, DOUBLE * pdblOut);
        VarR8FromCy = oleaut32.VarR8FromCy
        VarR8FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromDate(DATE dateIn, _Out_ DOUBLE * pdblOut);
        VarR8FromDate = oleaut32.VarR8FromDate
        VarR8FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromStr(_In_ LPCOLESTR strIn, LCID lcid, ULONG dwFlags, _Out_ DOUBLE *pdblOut);
        VarR8FromStr = oleaut32.VarR8FromStr
        VarR8FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromDisp(IDispatch * pdispIn, LCID lcid, _Out_ DOUBLE * pdblOut);
        VarR8FromDisp = oleaut32.VarR8FromDisp
        VarR8FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromBool(VARIANT_BOOL boolIn, _Out_ DOUBLE * pdblOut);
        VarR8FromBool = oleaut32.VarR8FromBool
        VarR8FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromI1(CHAR cIn, DOUBLE *pdblOut);
        VarR8FromI1 = oleaut32.VarR8FromI1
        VarR8FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromUI2(USHORT uiIn, _Out_ DOUBLE *pdblOut);
        VarR8FromUI2 = oleaut32.VarR8FromUI2
        VarR8FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromUI4(ULONG ulIn, _Out_ DOUBLE *pdblOut);
        VarR8FromUI4 = oleaut32.VarR8FromUI4
        VarR8FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromUI8(ULONG64 ui64In, _Out_ DOUBLE FAR* pdblOut);
        VarR8FromUI8 = oleaut32.VarR8FromUI8
        VarR8FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarR8FromDec(_In_ DECIMAL *pdecIn, _Out_ DOUBLE *pdblOut);
        VarR8FromDec = oleaut32.VarR8FromDec
        VarR8FromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromUI1(BYTE bIn, _Out_ DATE * pdateOut);
        VarDateFromUI1 = oleaut32.VarDateFromUI1
        VarDateFromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromI2(SHORT sIn, _Out_ DATE * pdateOut);
        VarDateFromI2 = oleaut32.VarDateFromI2
        VarDateFromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromI4(LONG lIn, _Out_ DATE * pdateOut);
        VarDateFromI4 = oleaut32.VarDateFromI4
        VarDateFromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromI8(LONG64 i64In, _Out_ DATE FAR* pdateOut);
        VarDateFromI8 = oleaut32.VarDateFromI8
        VarDateFromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromR4(FLOAT fltIn, _Out_ DATE * pdateOut);
        VarDateFromR4 = oleaut32.VarDateFromR4
        VarDateFromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromR8(DOUBLE dblIn, _Out_ DATE * pdateOut);
        VarDateFromR8 = oleaut32.VarDateFromR8
        VarDateFromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromCy(CY cyIn, _Out_ DATE * pdateOut);
        VarDateFromCy = oleaut32.VarDateFromCy
        VarDateFromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ DATE *pdateOut);
        VarDateFromStr = oleaut32.VarDateFromStr
        VarDateFromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromDisp(IDispatch * pdispIn, LCID lcid, _Out_ DATE * pdateOut);
        VarDateFromDisp = oleaut32.VarDateFromDisp
        VarDateFromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromBool(VARIANT_BOOL boolIn, _Out_ DATE * pdateOut);
        VarDateFromBool = oleaut32.VarDateFromBool
        VarDateFromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromI1(CHAR cIn, _Out_ DATE *pdateOut);
        VarDateFromI1 = oleaut32.VarDateFromI1
        VarDateFromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromUI2(USHORT uiIn, _Out_ DATE *pdateOut);
        VarDateFromUI2 = oleaut32.VarDateFromUI2
        VarDateFromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromUI4(ULONG ulIn, _Out_ DATE *pdateOut);
        VarDateFromUI4 = oleaut32.VarDateFromUI4
        VarDateFromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromUI8(ULONG64 ui64In, _Out_ DATE FAR* pdateOut);
        VarDateFromUI8 = oleaut32.VarDateFromUI8
        VarDateFromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromDec(_In_ DECIMAL *pdecIn, _Out_ DATE *pdateOut);
        VarDateFromDec = oleaut32.VarDateFromDec
        VarDateFromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromUI1(BYTE bIn, _Out_ CY * pcyOut);
        VarCyFromUI1 = oleaut32.VarCyFromUI1
        VarCyFromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromI2(SHORT sIn, _Out_ CY * pcyOut);
        VarCyFromI2 = oleaut32.VarCyFromI2
        VarCyFromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromI4(LONG lIn, _Out_ CY * pcyOut);
        VarCyFromI4 = oleaut32.VarCyFromI4
        VarCyFromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromI8(LONG64 i64In, _Out_ CY FAR* pcyOut);
        VarCyFromI8 = oleaut32.VarCyFromI8
        VarCyFromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromR4(FLOAT fltIn, _Out_ CY * pcyOut);
        VarCyFromR4 = oleaut32.VarCyFromR4
        VarCyFromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromR8(DOUBLE dblIn, _Out_ CY * pcyOut);
        VarCyFromR8 = oleaut32.VarCyFromR8
        VarCyFromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromDate(DATE dateIn, _Out_ CY * pcyOut);
        VarCyFromDate = oleaut32.VarCyFromDate
        VarCyFromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ CY * pcyOut);
        VarCyFromStr = oleaut32.VarCyFromStr
        VarCyFromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromDisp(_In_ IDispatch * pdispIn, LCID lcid, _Out_ CY * pcyOut);
        VarCyFromDisp = oleaut32.VarCyFromDisp
        VarCyFromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromBool(VARIANT_BOOL boolIn, _Out_ CY * pcyOut);
        VarCyFromBool = oleaut32.VarCyFromBool
        VarCyFromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromI1(CHAR cIn, _Out_ CY *pcyOut);
        VarCyFromI1 = oleaut32.VarCyFromI1
        VarCyFromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromUI2(USHORT uiIn, _Out_ CY *pcyOut);
        VarCyFromUI2 = oleaut32.VarCyFromUI2
        VarCyFromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromUI4(ULONG ulIn, _Out_ CY *pcyOut);
        VarCyFromUI4 = oleaut32.VarCyFromUI4
        VarCyFromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromUI8(ULONG64 ui64In, _Out_ CY FAR* pcyOut);
        VarCyFromUI8 = oleaut32.VarCyFromUI8
        VarCyFromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarCyFromDec(_In_ DECIMAL *pdecIn, _Out_ CY *pcyOut);
        VarCyFromDec = oleaut32.VarCyFromDec
        VarCyFromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromUI1(BYTE bVal, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromUI1 = oleaut32.VarBstrFromUI1
        VarBstrFromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromI2(SHORT iVal, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromI2 = oleaut32.VarBstrFromI2
        VarBstrFromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromI4(LONG lIn, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromI4 = oleaut32.VarBstrFromI4
        VarBstrFromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromI8(LONG64 i64In, LCID lcid, ULONG dwFlags, _Out_ BSTR FAR* pbstrOut);
        VarBstrFromI8 = oleaut32.VarBstrFromI8
        VarBstrFromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromR4(FLOAT fltIn, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromR4 = oleaut32.VarBstrFromR4
        VarBstrFromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromR8(DOUBLE dblIn, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromR8 = oleaut32.VarBstrFromR8
        VarBstrFromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromCy(CY cyIn, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromCy = oleaut32.VarBstrFromCy
        VarBstrFromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromDate(_In_ DATE dateIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromDate = oleaut32.VarBstrFromDate
        VarBstrFromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromDisp(IDispatch * pdispIn, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromDisp = oleaut32.VarBstrFromDisp
        VarBstrFromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromBool(VARIANT_BOOL boolIn, LCID lcid, ULONG dwFlags, _Out_ BSTR * pbstrOut);
        VarBstrFromBool = oleaut32.VarBstrFromBool
        VarBstrFromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromI1(CHAR cIn, LCID lcid, ULONG dwFlags, _Out_ BSTR *pbstrOut);
        VarBstrFromI1 = oleaut32.VarBstrFromI1
        VarBstrFromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromUI2(USHORT uiIn, LCID lcid, ULONG dwFlags, _Out_ BSTR *pbstrOut);
        VarBstrFromUI2 = oleaut32.VarBstrFromUI2
        VarBstrFromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromUI4(ULONG ulIn, LCID lcid, ULONG dwFlags, _Out_ BSTR *pbstrOut);
        VarBstrFromUI4 = oleaut32.VarBstrFromUI4
        VarBstrFromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromUI8(ULONG64 ui64In, LCID lcid, ULONG dwFlags, _Out_ BSTR FAR* pbstrOut);
        VarBstrFromUI8 = oleaut32.VarBstrFromUI8
        VarBstrFromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBstrFromDec(_In_ DECIMAL *pdecIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ BSTR *pbstrOut);
        VarBstrFromDec = oleaut32.VarBstrFromDec
        VarBstrFromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromUI1(BYTE bIn, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromUI1 = oleaut32.VarBoolFromUI1
        VarBoolFromUI1.restype = WINOLEAUTAPI

        # _Check_return_ WINOLEAUTAPI VarBoolFromI2(_In_ SHORT sIn, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromI2 = oleaut32.VarBoolFromI2
        VarBoolFromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromI4(LONG lIn, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromI4 = oleaut32.VarBoolFromI4
        VarBoolFromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromI8(LONG64 i64In, _Out_ VARIANT_BOOL FAR* pboolOut);
        VarBoolFromI8 = oleaut32.VarBoolFromI8
        VarBoolFromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromR4(FLOAT fltIn, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromR4 = oleaut32.VarBoolFromR4
        VarBoolFromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromR8(DOUBLE dblIn, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromR8 = oleaut32.VarBoolFromR8
        VarBoolFromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromDate(DATE dateIn, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromDate = oleaut32.VarBoolFromDate
        VarBoolFromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromCy(CY cyIn, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromCy = oleaut32.VarBoolFromCy
        VarBoolFromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromStr(_In_ LPCOLESTR strIn, LCID lcid, ULONG dwFlags, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromStr = oleaut32.VarBoolFromStr
        VarBoolFromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromDisp(IDispatch * pdispIn, LCID lcid, _Out_ VARIANT_BOOL * pboolOut);
        VarBoolFromDisp = oleaut32.VarBoolFromDisp
        VarBoolFromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromI1(CHAR cIn, _Out_ VARIANT_BOOL *pboolOut);
        VarBoolFromI1 = oleaut32.VarBoolFromI1
        VarBoolFromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromUI2(USHORT uiIn, _Out_ VARIANT_BOOL *pboolOut);
        VarBoolFromUI2 = oleaut32.VarBoolFromUI2
        VarBoolFromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromUI4(ULONG ulIn, _Out_ VARIANT_BOOL *pboolOut);
        VarBoolFromUI4 = oleaut32.VarBoolFromUI4
        VarBoolFromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromUI8(ULONG64 i64In, _Out_ VARIANT_BOOL FAR* pboolOut);
        VarBoolFromUI8 = oleaut32.VarBoolFromUI8
        VarBoolFromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarBoolFromDec(_In_ DECIMAL *pdecIn, _Out_ VARIANT_BOOL *pboolOut);
        VarBoolFromDec = oleaut32.VarBoolFromDec
        VarBoolFromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromUI1(
        # _In_ BYTE bIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromUI1 = oleaut32.VarI1FromUI1
        VarI1FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromI2(
        # _In_ SHORT uiIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromI2 = oleaut32.VarI1FromI2
        VarI1FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromI4(
        # _In_ LONG lIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromI4 = oleaut32.VarI1FromI4
        VarI1FromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromI8(
        # _In_ LONG64 i64In,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromI8 = oleaut32.VarI1FromI8
        VarI1FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromR4(
        # _In_ FLOAT fltIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromR4 = oleaut32.VarI1FromR4
        VarI1FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromR8(
        # _In_ DOUBLE dblIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromR8 = oleaut32.VarI1FromR8
        VarI1FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromDate(
        # _In_ DATE dateIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromDate = oleaut32.VarI1FromDate
        VarI1FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromCy(
        # _In_ CY cyIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromCy = oleaut32.VarI1FromCy
        VarI1FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromStr(
        # _In_ LPCOLESTR strIn,
        # _In_ LCID lcid,
        # _In_ ULONG dwFlags,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromStr = oleaut32.VarI1FromStr
        VarI1FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromDisp(
        # _In_ IDispatch *pdispIn,
        # _In_ LCID lcid,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromDisp = oleaut32.VarI1FromDisp
        VarI1FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromBool(
        # _In_ VARIANT_BOOL boolIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromBool = oleaut32.VarI1FromBool
        VarI1FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromUI2(
        # _In_ USHORT uiIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromUI2 = oleaut32.VarI1FromUI2
        VarI1FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromUI4(
        # _In_ ULONG ulIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromUI4 = oleaut32.VarI1FromUI4
        VarI1FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromUI8(
        # _In_ ULONG64 i64In,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromUI8 = oleaut32.VarI1FromUI8
        VarI1FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI
        # VarI1FromDec(
        # _In_ DECIMAL *pdecIn,
        # _Out_ CHAR *pcOut
        # );
        VarI1FromDec = oleaut32.VarI1FromDec
        VarI1FromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromUI1(BYTE bIn, _Out_ USHORT *puiOut);
        VarUI2FromUI1 = oleaut32.VarUI2FromUI1
        VarUI2FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromI2(SHORT uiIn, _Out_ USHORT *puiOut);
        VarUI2FromI2 = oleaut32.VarUI2FromI2
        VarUI2FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromI4(LONG lIn, _Out_ USHORT *puiOut);
        VarUI2FromI4 = oleaut32.VarUI2FromI4
        VarUI2FromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromI8(LONG64 i64In, _Out_ USHORT *puiOut);
        VarUI2FromI8 = oleaut32.VarUI2FromI8
        VarUI2FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromR4(FLOAT fltIn, _Out_ USHORT *puiOut);
        VarUI2FromR4 = oleaut32.VarUI2FromR4
        VarUI2FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromR8(DOUBLE dblIn, USHORT *puiOut);
        VarUI2FromR8 = oleaut32.VarUI2FromR8
        VarUI2FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromDate(DATE dateIn, _Out_ USHORT *puiOut);
        VarUI2FromDate = oleaut32.VarUI2FromDate
        VarUI2FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromCy(CY cyIn, _Out_ USHORT *puiOut);
        VarUI2FromCy = oleaut32.VarUI2FromCy
        VarUI2FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ USHORT *puiOut);
        VarUI2FromStr = oleaut32.VarUI2FromStr
        VarUI2FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromDisp(_In_ IDispatch *pdispIn, LCID lcid, _Out_ USHORT *puiOut);
        VarUI2FromDisp = oleaut32.VarUI2FromDisp
        VarUI2FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromBool(VARIANT_BOOL boolIn, _Out_ USHORT *puiOut);
        VarUI2FromBool = oleaut32.VarUI2FromBool
        VarUI2FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromI1(CHAR cIn, _Out_ USHORT *puiOut);
        VarUI2FromI1 = oleaut32.VarUI2FromI1
        VarUI2FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromUI4(ULONG ulIn, _Out_ USHORT *puiOut);
        VarUI2FromUI4 = oleaut32.VarUI2FromUI4
        VarUI2FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromUI8(ULONG64 i64In, _Out_ USHORT *puiOut);
        VarUI2FromUI8 = oleaut32.VarUI2FromUI8
        VarUI2FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI2FromDec(_In_ DECIMAL *pdecIn, _Out_ USHORT *puiOut);
        VarUI2FromDec = oleaut32.VarUI2FromDec
        VarUI2FromDec.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromUI1(BYTE bIn, _Out_ ULONG *pulOut);
        VarUI4FromUI1 = oleaut32.VarUI4FromUI1
        VarUI4FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromI2(_In_ SHORT uiIn, _Out_ ULONG *pulOut);
        VarUI4FromI2 = oleaut32.VarUI4FromI2
        VarUI4FromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromI4(LONG lIn, _Out_ ULONG *pulOut);
        VarUI4FromI4 = oleaut32.VarUI4FromI4
        VarUI4FromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromI8(LONG64 i64In, _Out_ ULONG *plOut);
        VarUI4FromI8 = oleaut32.VarUI4FromI8
        VarUI4FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromR4(FLOAT fltIn, _Out_ ULONG *pulOut);
        VarUI4FromR4 = oleaut32.VarUI4FromR4
        VarUI4FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromR8(DOUBLE dblIn, _Out_ ULONG *pulOut);
        VarUI4FromR8 = oleaut32.VarUI4FromR8
        VarUI4FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromDate(DATE dateIn, _Out_ ULONG *pulOut);
        VarUI4FromDate = oleaut32.VarUI4FromDate
        VarUI4FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromCy(CY cyIn, _Out_ ULONG *pulOut);
        VarUI4FromCy = oleaut32.VarUI4FromCy
        VarUI4FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ ULONG *pulOut);
        VarUI4FromStr = oleaut32.VarUI4FromStr
        VarUI4FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromDisp(_In_ IDispatch *pdispIn, LCID lcid, _Out_ ULONG *pulOut);
        VarUI4FromDisp = oleaut32.VarUI4FromDisp
        VarUI4FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromBool(VARIANT_BOOL boolIn, _Out_ ULONG *pulOut);
        VarUI4FromBool = oleaut32.VarUI4FromBool
        VarUI4FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromI1(CHAR cIn, _Out_ ULONG *pulOut);
        VarUI4FromI1 = oleaut32.VarUI4FromI1
        VarUI4FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromUI2(USHORT uiIn, _Out_ ULONG *pulOut);
        VarUI4FromUI2 = oleaut32.VarUI4FromUI2
        VarUI4FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromUI8(ULONG64 ui64In, _Out_ ULONG *plOut);
        VarUI4FromUI8 = oleaut32.VarUI4FromUI8
        VarUI4FromUI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI4FromDec(_In_ DECIMAL *pdecIn, _Out_ ULONG *pulOut);
        VarUI4FromDec = oleaut32.VarUI4FromDec
        VarUI4FromDec.restype = WINOLEAUTAPI

        # **************************************
        # WINOLEAUTAPI VarUI8FromUI1(BYTE bIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromUI1 = oleaut32.VarUI8FromUI1
        VarUI8FromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromI2(SHORT sIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromI2 = oleaut32.VarUI8FromI2
        VarUI8FromI2.restype = WINOLEAUTAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI VarUI8FromI8(LONG64 ui64In, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromI8 = oleaut32.VarUI8FromI8
        VarUI8FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromR4(FLOAT fltIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromR4 = oleaut32.VarUI8FromR4
        VarUI8FromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromR8(DOUBLE dblIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromR8 = oleaut32.VarUI8FromR8
        VarUI8FromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromCy(CY cyIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromCy = oleaut32.VarUI8FromCy
        VarUI8FromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromDate(DATE dateIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromDate = oleaut32.VarUI8FromDate
        VarUI8FromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromStr = oleaut32.VarUI8FromStr
        VarUI8FromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromDisp(_In_ IDispatch FAR* pdispIn, LCID lcid, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromDisp = oleaut32.VarUI8FromDisp
        VarUI8FromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromBool(VARIANT_BOOL boolIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromBool = oleaut32.VarUI8FromBool
        VarUI8FromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromI1(CHAR cIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromI1 = oleaut32.VarUI8FromI1
        VarUI8FromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromUI2(USHORT uiIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromUI2 = oleaut32.VarUI8FromUI2
        VarUI8FromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromUI4(ULONG ulIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromUI4 = oleaut32.VarUI8FromUI4
        VarUI8FromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarUI8FromDec(_In_ DECIMAL *pdecIn, _Out_ ULONG64 FAR* pi64Out);
        VarUI8FromDec = oleaut32.VarUI8FromDec
        VarUI8FromDec.restype = WINOLEAUTAPI

        # *****************
        # WINOLEAUTAPI VarDecFromUI1(_In_ BYTE bIn, _Out_ DECIMAL *pdecOut);
        VarDecFromUI1 = oleaut32.VarDecFromUI1
        VarDecFromUI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromI2(_In_ SHORT uiIn, _Out_ DECIMAL *pdecOut);
        VarDecFromI2 = oleaut32.VarDecFromI2
        VarDecFromI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromI4(_In_ LONG lIn, _Out_ DECIMAL *pdecOut);
        VarDecFromI4 = oleaut32.VarDecFromI4
        VarDecFromI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromI8(LONG64 i64In, _Out_ DECIMAL *pdecOut);
        VarDecFromI8 = oleaut32.VarDecFromI8
        VarDecFromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromR4(_In_ FLOAT fltIn, _Out_ DECIMAL *pdecOut);
        VarDecFromR4 = oleaut32.VarDecFromR4
        VarDecFromR4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromR8(_In_ DOUBLE dblIn, _Out_ DECIMAL *pdecOut);
        VarDecFromR8 = oleaut32.VarDecFromR8
        VarDecFromR8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromDate(_In_ DATE dateIn, _Out_ DECIMAL *pdecOut);
        VarDecFromDate = oleaut32.VarDecFromDate
        VarDecFromDate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromCy(_In_ CY cyIn, _Out_ DECIMAL *pdecOut);
        VarDecFromCy = oleaut32.VarDecFromCy
        VarDecFromCy.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ DECIMAL *pdecOut);
        VarDecFromStr = oleaut32.VarDecFromStr
        VarDecFromStr.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromDisp(_In_ IDispatch *pdispIn, _In_ LCID lcid, _Out_ DECIMAL *pdecOut);
        VarDecFromDisp = oleaut32.VarDecFromDisp
        VarDecFromDisp.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromBool(_In_ VARIANT_BOOL boolIn, _Out_ DECIMAL *pdecOut);
        VarDecFromBool = oleaut32.VarDecFromBool
        VarDecFromBool.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromI1(_In_ CHAR cIn, _Out_ DECIMAL *pdecOut);
        VarDecFromI1 = oleaut32.VarDecFromI1
        VarDecFromI1.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromUI2(_In_ USHORT uiIn, _Out_ DECIMAL *pdecOut);
        VarDecFromUI2 = oleaut32.VarDecFromUI2
        VarDecFromUI2.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromUI4(_In_ ULONG ulIn, _Out_ DECIMAL *pdecOut);
        VarDecFromUI4 = oleaut32.VarDecFromUI4
        VarDecFromUI4.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDecFromUI8(ULONG64 ui64In, _Out_ DECIMAL *pdecOut);
        VarDecFromUI8 = oleaut32.VarDecFromUI8
        VarDecFromUI8.restype = WINOLEAUTAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)


    def VarUI4FromUI4(_in, pOut):
        return _in


    def VarI4FromI4(_in, pOut):
        return _in


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI VarI4FromI8(LONG64 i64In, _Out_ LONG *plOut);
        VarI4FromI8 = oleaut32.VarI4FromI8
        VarI4FromI8.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarI4FromUI8(ULONG64 ui64In, _Out_ LONG *plOut);
        VarI4FromUI8 = oleaut32.VarI4FromUI8
        VarI4FromUI8.restype = WINOLEAUTAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)


    def VarUI8FromUI8(_in, pOut):
        return _in


    def VarI8FromI8(_in, pOut):
        return _in


    VarUI1FromInt = VarUI1FromI4
    VarUI1FromUint = VarUI1FromUI4
    VarI2FromInt = VarI2FromI4
    VarI2FromUint = VarI2FromUI4

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        VarI4FromInt = VarI4FromI4
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    VarI4FromUint = VarI4FromUI4
    VarI8FromUint = VarI8FromUI4
    VarR4FromInt = VarR4FromI4
    VarR4FromUint = VarR4FromUI4
    VarR8FromInt = VarR8FromI4
    VarR8FromUint = VarR8FromUI4
    VarDateFromInt = VarDateFromI4
    VarDateFromUint = VarDateFromUI4
    VarCyFromInt = VarCyFromI4
    VarCyFromUint = VarCyFromUI4
    VarBstrFromInt = VarBstrFromI4
    VarBstrFromUint = VarBstrFromUI4
    VarBoolFromInt = VarBoolFromI4
    VarBoolFromUint = VarBoolFromUI4
    VarI1FromInt = VarI1FromI4
    VarI1FromUint = VarI1FromUI4
    VarUI2FromInt = VarUI2FromI4
    VarUI2FromUint = VarUI2FromUI4
    VarUI4FromInt = VarUI4FromI4
    VarUI4FromUint = VarUI4FromUI4
    VarDecFromInt = VarDecFromI4
    VarDecFromUint = VarDecFromUI4
    VarIntFromUI1 = VarI4FromUI1
    VarIntFromI2 = VarI4FromI2
    VarIntFromI4 = VarI4FromI4
    VarIntFromI8 = VarI4FromI8
    VarIntFromR4 = VarI4FromR4
    VarIntFromR8 = VarI4FromR8
    VarIntFromDate = VarI4FromDate
    VarIntFromCy = VarI4FromCy
    VarIntFromStr = VarI4FromStr
    VarIntFromDisp = VarI4FromDisp
    VarIntFromBool = VarI4FromBool
    VarIntFromI1 = VarI4FromI1
    VarIntFromUI2 = VarI4FromUI2
    VarIntFromUI4 = VarI4FromUI4
    VarIntFromUI8 = VarI4FromUI8
    VarIntFromDec = VarI4FromDec
    VarIntFromUint = VarI4FromUI4
    VarUintFromUI1 = VarUI4FromUI1
    VarUintFromI2 = VarUI4FromI2
    VarUintFromI4 = VarUI4FromI4
    VarUintFromI8 = VarUI4FromI8
    VarUintFromR4 = VarUI4FromR4
    VarUintFromR8 = VarUI4FromR8
    VarUintFromDate = VarUI4FromDate
    VarUintFromCy = VarUI4FromCy
    VarUintFromStr = VarUI4FromStr
    VarUintFromDisp = VarUI4FromDisp
    VarUintFromBool = VarUI4FromBool
    VarUintFromI1 = VarUI4FromI1
    VarUintFromUI2 = VarUI4FromUI2
    VarUintFromUI4 = VarUI4FromUI4
    VarUintFromUI8 = VarUI4FromUI8
    VarUintFromDec = VarUI4FromDec
    VarUintFromInt = VarUI4FromI4

    # /* Mac Note: On the Mac, the coersion functions support the Symantec C +
    # + calling convention for float/double. To support float/double arguments
    # compiled with the MPW C compiler, use the following APIs to move MPW
    # float/double values into a VARIANT.
    # ---------------------------------------------------------------------
    # New VARIANT <.string parsing functions
    # ---------------------------------------------------------------------
    NUMPARSE._fields_ = [
        ('cDig', INT),
        ('dwInFlags', ULONG),
        ('dwOutFlags', ULONG),
        ('cchUsed', INT),
        ('nBaseShift', INT),
        ('nPwr10', INT),
    ]

    # /* flags used by both dwInFlags and dwOutFlags:
    NUMPRS_LEADING_WHITE = 0x0001
    NUMPRS_TRAILING_WHITE = 0x0002
    NUMPRS_LEADING_PLUS = 0x0004
    NUMPRS_TRAILING_PLUS = 0x0008
    NUMPRS_LEADING_MINUS = 0x0010
    NUMPRS_TRAILING_MINUS = 0x0020
    NUMPRS_HEX_OCT = 0x0040
    NUMPRS_PARENS = 0x0080
    NUMPRS_DECIMAL = 0x0100
    NUMPRS_THOUSANDS = 0x0200
    NUMPRS_CURRENCY = 0x0400
    NUMPRS_EXPONENT = 0x0800
    NUMPRS_USE_ALL = 0x1000
    NUMPRS_STD = 0x1FFF

    # /* flags used by dwOutFlags only:
    NUMPRS_NEG = 0x10000
    NUMPRS_INEXACT = 0x20000

    # /* flags used by VarNumFromParseNum to indicate acceptable result types:
    VTBIT_I1 = 1 << VARENUM.VT_I1
    VTBIT_UI1 = 1 << VARENUM.VT_UI1
    VTBIT_I2 = 1 << VARENUM.VT_I2
    VTBIT_UI2 = 1 << VARENUM.VT_UI2
    VTBIT_I4 = 1 << VARENUM.VT_I4
    VTBIT_UI4 = 1 << VARENUM.VT_UI4
    VTBIT_I8 = 1 << VARENUM.VT_I8
    VTBIT_UI8 = 1 << VARENUM.VT_UI8
    VTBIT_R4 = 1 << VARENUM.VT_R4
    VTBIT_R8 = 1 << VARENUM.VT_R8
    VTBIT_CY = 1 << VARENUM.VT_CY
    VTBIT_DECIMAL = 1 << VARENUM.VT_DECIMAL

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_
        # WINOLEAUTAPI VarParseNumFromStr(_In_ LPCOLESTR strIn, _In_ LCID lcid, _In_ ULONG dwFlags,
        # _Inout_ NUMPARSE * pnumprs, _Out_writes_(pnumprs.cDig) BYTE * rgbDig);
        VarParseNumFromStr = oleaut32.VarParseNumFromStr
        VarParseNumFromStr.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI VarNumFromParseNum(_In_ NUMPARSE * pnumprs, _In_reads_(pnumprs.cDig) BYTE * rgbDig,
        # _In_ ULONG dwVtBits, _Out_ VARIANT * pvar);
        VarNumFromParseNum = oleaut32.VarNumFromParseNum
        VarNumFromParseNum.restype = WINOLEAUTAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # ---------------------------------------------------------------------
    # VARTYPE Math API
    # ---------------------------------------------------------------------
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # STDAPI VarAdd(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarAdd = oleaut32.VarAdd
        VarAdd.restype = STDAPI

        # STDAPI VarAnd(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarAnd = oleaut32.VarAnd
        VarAnd.restype = STDAPI

        # STDAPI VarCat(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarCat = oleaut32.VarCat
        VarCat.restype = STDAPI

        # STDAPI VarDiv(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarDiv = oleaut32.VarDiv
        VarDiv.restype = STDAPI

        # STDAPI VarEqv(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarEqv = oleaut32.VarEqv
        VarEqv.restype = STDAPI

        # STDAPI VarIdiv(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarIdiv = oleaut32.VarIdiv
        VarIdiv.restype = STDAPI

        # STDAPI VarImp(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarImp = oleaut32.VarImp
        VarImp.restype = STDAPI

        # STDAPI VarMod(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarMod = oleaut32.VarMod
        VarMod.restype = STDAPI

        # STDAPI VarMul(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarMul = oleaut32.VarMul
        VarMul.restype = STDAPI

        # STDAPI VarOr(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarOr = oleaut32.VarOr
        VarOr.restype = STDAPI

        # STDAPI VarPow(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarPow = oleaut32.VarPow
        VarPow.restype = STDAPI

        # STDAPI VarSub(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarSub = oleaut32.VarSub
        VarSub.restype = STDAPI

        # STDAPI VarXor(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _Out_ LPVARIANT pvarResult);
        VarXor = oleaut32.VarXor
        VarXor.restype = STDAPI

        # STDAPI VarAbs(_In_ LPVARIANT pvarIn, _Out_ LPVARIANT pvarResult);
        VarAbs = oleaut32.VarAbs
        VarAbs.restype = STDAPI

        # STDAPI VarFix(_In_ LPVARIANT pvarIn, _Out_ LPVARIANT pvarResult);
        VarFix = oleaut32.VarFix
        VarFix.restype = STDAPI

        # STDAPI VarInt(_In_ LPVARIANT pvarIn, _Out_ LPVARIANT pvarResult);
        VarInt = oleaut32.VarInt
        VarInt.restype = STDAPI

        # STDAPI VarNeg(_In_ LPVARIANT pvarIn, _Out_ LPVARIANT pvarResult);
        VarNeg = oleaut32.VarNeg
        VarNeg.restype = STDAPI

        # STDAPI VarNot(_In_ LPVARIANT pvarIn, _Out_ LPVARIANT pvarResult);
        VarNot = oleaut32.VarNot
        VarNot.restype = STDAPI

        # STDAPI VarRound(_In_ LPVARIANT pvarIn, _In_ INT cDecimals, _Out_ LPVARIANT pvarResult);
        VarRound = oleaut32.VarRound
        VarRound.restype = STDAPI

        # dwFlags passed to CompareString if a string compare
        # STDAPI VarCmp(_In_ LPVARIANT pvarLeft, _In_ LPVARIANT pvarRight, _In_ LCID lcid, _In_ ULONG dwFlags);
        VarCmp = oleaut32.VarCmp
        VarCmp.restype = STDAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if defined(__cplusplus):

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            #
            # // Add wrapper for old ATL headers to call
            # __inline
            # HRESULT
            if not defined(_M_CEE_PURE):
                # STDAPICALLTYPE
                pass
            # END IF
            # VarCmp(LPVARIANT pvarLeft, LPVARIANT pvarRight, LCID lcid) {
            # return VarCmp(pvarLeft, pvarRight, lcid, 0);
            # }
            #
        # END IF WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        # #pragma endregion
        #
        # } // extern "C +  + "
    # END IF __cplusplus

    # // Decimal math
    # #pragma region Application Family or OneCore Family
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # STDAPI VarDecAdd(_In_ LPDECIMAL pdecLeft, _In_ LPDECIMAL pdecRight, _Out_ LPDECIMAL pdecResult);
        VarDecAdd = oleaut32.VarDecAdd
        VarDecAdd.restype = STDAPI
        # STDAPI VarDecDiv(_In_ LPDECIMAL pdecLeft, _In_ LPDECIMAL pdecRight, _Out_ LPDECIMAL pdecResult);
        VarDecDiv = oleaut32.VarDecDiv
        VarDecDiv.restype = STDAPI
        # STDAPI VarDecMul(_In_ LPDECIMAL pdecLeft, _In_ LPDECIMAL pdecRight, _Out_ LPDECIMAL pdecResult);
        VarDecMul = oleaut32.VarDecMul
        VarDecMul.restype = STDAPI
        # STDAPI VarDecSub(_In_ LPDECIMAL pdecLeft, _In_ LPDECIMAL pdecRight, _Out_ LPDECIMAL pdecResult);
        VarDecSub = oleaut32.VarDecSub
        VarDecSub.restype = STDAPI
        # STDAPI VarDecAbs(_In_ LPDECIMAL pdecIn, _Out_ LPDECIMAL pdecResult);
        VarDecAbs = oleaut32.VarDecAbs
        VarDecAbs.restype = STDAPI
        # STDAPI VarDecFix(_In_ LPDECIMAL pdecIn, _Out_ LPDECIMAL pdecResult);
        VarDecFix = oleaut32.VarDecFix
        VarDecFix.restype = STDAPI
        # STDAPI VarDecInt(_In_ LPDECIMAL pdecIn, _Out_ LPDECIMAL pdecResult);
        VarDecInt = oleaut32.VarDecInt
        VarDecInt.restype = STDAPI
        # STDAPI VarDecNeg(_In_ LPDECIMAL pdecIn, _Out_ LPDECIMAL pdecResult);
        VarDecNeg = oleaut32.VarDecNeg
        VarDecNeg.restype = STDAPI
        # STDAPI VarDecRound(_In_ LPDECIMAL pdecIn, INT cDecimals, _Out_ LPDECIMAL pdecResult);
        VarDecRound = oleaut32.VarDecRound
        VarDecRound.restype = STDAPI
        # STDAPI VarDecCmp(_In_ LPDECIMAL pdecLeft, _In_ LPDECIMAL pdecRight);
        VarDecCmp = oleaut32.VarDecCmp
        VarDecCmp.restype = STDAPI
        # STDAPI VarDecCmpR8(_In_ LPDECIMAL pdecLeft, _In_ DOUBLE dblRight);
        VarDecCmpR8 = oleaut32.VarDecCmpR8
        VarDecCmpR8.restype = STDAPI

        # Currency math

        # STDAPI VarCyAdd(_In_ CY cyLeft, _In_ CY cyRight, _Out_ LPCY pcyResult);
        VarCyAdd = oleaut32.VarCyAdd
        VarCyAdd.restype = STDAPI
        # STDAPI VarCyMul(_In_ CY cyLeft, _In_ CY cyRight, _Out_ LPCY pcyResult);
        VarCyMul = oleaut32.VarCyMul
        VarCyMul.restype = STDAPI
        # STDAPI VarCyMulI4(_In_ CY cyLeft, _In_ LONG lRight, _Out_ LPCY pcyResult);
        VarCyMulI4 = oleaut32.VarCyMulI4
        VarCyMulI4.restype = STDAPI
        # STDAPI VarCyMulI8(_In_ CY cyLeft, _In_ LONG64 lRight, _Out_ LPCY pcyResult);
        VarCyMulI8 = oleaut32.VarCyMulI8
        VarCyMulI8.restype = STDAPI
        # STDAPI VarCySub(_In_ CY cyLeft, _In_ CY cyRight, _Out_ LPCY pcyResult);
        VarCySub = oleaut32.VarCySub
        VarCySub.restype = STDAPI
        # STDAPI VarCyAbs(_In_ CY cyIn, _Out_ LPCY pcyResult);
        VarCyAbs = oleaut32.VarCyAbs
        VarCyAbs.restype = STDAPI
        # STDAPI VarCyFix(_In_ CY cyIn, _Out_ LPCY pcyResult);
        VarCyFix = oleaut32.VarCyFix
        VarCyFix.restype = STDAPI
        # STDAPI VarCyInt(_In_ CY cyIn, _Out_ LPCY pcyResult);
        VarCyInt = oleaut32.VarCyInt
        VarCyInt.restype = STDAPI
        # STDAPI VarCyNeg(_In_ CY cyIn, _Out_ LPCY pcyResult);
        VarCyNeg = oleaut32.VarCyNeg
        VarCyNeg.restype = STDAPI
        # STDAPI VarCyRound(_In_ CY cyIn, _In_ INT cDecimals, _Out_ LPCY pcyResult);
        VarCyRound = oleaut32.VarCyRound
        VarCyRound.restype = STDAPI
        # STDAPI VarCyCmp(_In_ CY cyLeft, _In_ CY cyRight);
        VarCyCmp = oleaut32.VarCyCmp
        VarCyCmp.restype = STDAPI
        # STDAPI VarCyCmpR8(_In_ CY cyLeft, _In_ DOUBLE dblRight);
        VarCyCmpR8 = oleaut32.VarCyCmpR8
        VarCyCmpR8.restype = STDAPI

        # Misc support functions

        # STDAPI VarBstrCat(_In_ BSTR bstrLeft, _In_ BSTR bstrRight, _Out_ LPBSTR pbstrResult);
        VarBstrCat = oleaut32.VarBstrCat
        VarBstrCat.restype = STDAPI
        # STDAPI VarBstrCmp(_In_ BSTR bstrLeft, _In_ BSTR bstrRight, _In_ LCID lcid, _In_ ULONG dwFlags); // dwFlags passed to CompareString
        VarBstrCmp = oleaut32.VarBstrCmp
        VarBstrCmp.restype = STDAPI
        # STDAPI VarR8Pow(_In_ DOUBLE dblLeft, _In_ DOUBLE dblRight, _Out_ DOUBLE *pdblResult);
        VarR8Pow = oleaut32.VarR8Pow
        VarR8Pow.restype = STDAPI
        # STDAPI VarR4CmpR8(_In_ FLOAT fltLeft, _In_ DOUBLE dblRight);
        VarR4CmpR8 = oleaut32.VarR4CmpR8
        VarR4CmpR8.restype = STDAPI
        # STDAPI VarR8Round(_In_ DOUBLE dblIn, _In_ INT cDecimals, _Out_ DOUBLE *pdblResult);
        VarR8Round = oleaut32.VarR8Round
        VarR8Round.restype = STDAPI
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # Compare results. These are returned as a SUCCESS HResult. Subtracting
    # one gives the usual values of -1 for Less Than, 0 for Equal To, + 1 for
    # Greater Than.
    VARCMP_LT = 0
    VARCMP_EQ = 1
    VARCMP_GT = 2
    VARCMP_NULL = 3
    # VT_HARDTYPE tells the compare routine that the argument is a literal or
    # otherwise declared of that specific type. It causes comparison rules to
    # change. For example, if a hard-type string is compared to a variant
    # (not hard
    # -type) number, the number is converted to string. If a hard-type number is
    #
    # compared to a variant string, the string is converted to number. If
    # they're
    # both variant, then number < string.
    VT_HARDTYPE = VARENUM.VT_RESERVED
    # ---------------------------------------------------------------------
    # New date functions
    # ---------------------------------------------------------------------
    # /* The UDATE structure is used with VarDateFromUdate() and
    # VarUdateFromDate(). It represents an "unpacked date".
    UDATE._fields_ = [
        ('st', SYSTEMTIME),
        ('wDayOfYear', USHORT),
    ]
    # /* APIs to "pack" and "unpack" dates. NOTE: Ex version of
    # VarDateFromUdate obeys 2 digit year setting in control panel.
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # _Check_return_
        # WINOLEAUTAPI VarDateFromUdate(_In_ UDATE *pudateIn, _In_ ULONG dwFlags, _Out_ DATE *pdateOut);
        VarDateFromUdate = oleaut32.VarDateFromUdate
        VarDateFromUdate.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarDateFromUdateEx(_In_ UDATE *pudateIn, _In_ LCID lcid, _In_ ULONG dwFlags, _Out_ DATE *pdateOut);
        VarDateFromUdateEx = oleaut32.VarDateFromUdateEx
        VarDateFromUdateEx.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI VarUdateFromDate(_In_ DATE dateIn, _In_ ULONG dwFlags, _Out_ UDATE *pudateOut);
        VarUdateFromDate = oleaut32.VarUdateFromDate
        VarUdateFromDate.restype = WINOLEAUTAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # /* API to retrieve the secondary(altername) month names Useful for
        # Hijri, Polish and Russian alternate month names

        # _Check_return_
        # WINOLEAUTAPI GetAltMonthNames(LCID lcid, _Outptr_result_buffer_maybenull_(13) LPOLESTR * * prgp);
        GetAltMonthNames = oleaut32.GetAltMonthNames
        GetAltMonthNames.restype = WINOLEAUTAPI

        # ---------------------------------------------------------------------
        # Format
        # ---------------------------------------------------------------------
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # WINOLEAUTAPI VarFormat(
        # _In_ LPVARIANT pvarIn,
        # _In_opt_ LPOLESTR pstrFormat,
        # int iFirstDay,
        # int iFirstWeek,
        # ULONG dwFlags,
        # _Out_ BSTR *pbstrOut
        # );
        VarFormat = oleaut32.VarFormat
        VarFormat.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarFormatDateTime(
        # _In_ LPVARIANT pvarIn,
        # int iNamedFormat,
        # ULONG dwFlags,
        # _Out_ BSTR *pbstrOut
        # );
        VarFormatDateTime = oleaut32.VarFormatDateTime
        VarFormatDateTime.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarFormatNumber(
        # _In_ LPVARIANT pvarIn,
        # int iNumDig,
        # int iIncLead,
        # int iUseParens,
        # int iGroup,
        # ULONG dwFlags,
        # _Out_ BSTR *pbstrOut
        # );
        VarFormatNumber = oleaut32.VarFormatNumber
        VarFormatNumber.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarFormatPercent(
        # _In_ LPVARIANT pvarIn,
        # int iNumDig,
        # int iIncLead,
        # int iUseParens,
        # int iGroup,
        # ULONG dwFlags,
        # _Out_ BSTR *pbstrOut
        # );
        VarFormatPercent = oleaut32.VarFormatPercent
        VarFormatPercent.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarFormatCurrency(
        # _In_ LPVARIANT pvarIn,
        # int iNumDig,
        # int iIncLead,
        # int iUseParens,
        # int iGroup,
        # ULONG dwFlags,
        # _Out_ BSTR *pbstrOut
        # );
        VarFormatCurrency = oleaut32.VarFormatCurrency
        VarFormatCurrency.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarWeekdayName(
        # int iWeekday,
        # int fAbbrev,
        # int iFirstDay,
        # ULONG dwFlags,
        # _Out_ BSTR *pbstrOut
        # );
        VarWeekdayName = oleaut32.VarWeekdayName
        VarWeekdayName.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarMonthName(
        # int iMonth,
        # int fAbbrev,
        # ULONG dwFlags,
        # _Out_ BSTR *pbstrOut
        # );
        VarMonthName = oleaut32.VarMonthName
        VarMonthName.restype = WINOLEAUTAPI

        # WINOLEAUTAPI VarTokenizeFormatString(
        # _In_opt_ LPOLESTR pstrFormat,
        # _Inout_updates_(cbTok) LPBYTE rgbTok,
        # int cbTok,
        # int iFirstDay,
        # int iFirstWeek,
        # LCID lcid,
        # _In_opt_ INT *pcbActual
        # );
        VarTokenizeFormatString = oleaut32.VarTokenizeFormatString
        VarTokenizeFormatString.restype = WINOLEAUTAPI

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # ---------------------------------------------------------------------
        # ITypeLib
        # ---------------------------------------------------------------------
        # [unique]
        LPTYPELIB = POINTER(ITypeLib)

        # ---------------------------------------------------------------------
        # ITypeInfo
        # ---------------------------------------------------------------------
        DISPID = LONG
        MEMBERID = DISPID
        MEMBERID_NIL = DISPID_UNKNOWN
        ID_DEFAULTINST = -2
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        # Flags for IDispatch::Invoke
        DISPATCH_METHOD = 0x1
        DISPATCH_PROPERTYGET = 0x2
        DISPATCH_PROPERTYPUT = 0x4
        DISPATCH_PROPERTYPUTREF = 0x8
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # [unique]
        LPTYPEINFO = POINTER(ITypeInfo)

        # ---------------------------------------------------------------------
        # ITypeComp
        # ---------------------------------------------------------------------
        # [unique]
        LPTYPECOMP = POINTER(ITypeComp)

        # ---------------------------------------------------------------------
        # ICreateTypeLib
        # ---------------------------------------------------------------------
        LPCREATETYPELIB = POINTER(ICreateTypeLib)
        LPCREATETYPEINFO = POINTER(ICreateTypeInfo)

        # ---------------------------------------------------------------------
        # TypeInfo API
        # ---------------------------------------------------------------------
        # /* compute a 16bit hash value for the given name
        if (defined (_WIN32) or defined (_WIN64)):
            # _Check_return_
            # WINOLEAUTAPI_(ULONG) LHashValOfNameSysA(SYSKIND syskind, LCID lcid,
            # LPCSTR szName);
            LHashValOfNameSysA = oleaut32.LHashValOfNameSysA
            LHashValOfNameSysA.restype = ULONG
        # END IF

        # _Check_return_
        # ULONG
        # LHashValOfNameSys(SYSKIND syskind, LCID lcid, OLECHAR * szName);
        LHashValOfNameSys = oleaut32.LHashValOfNameSys
        LHashValOfNameSys.restype = ULONG

        def LHashValOfName(lcid, szName):
            return LHashValOfNameSys(SYSKIND.SYS_WIN32, lcid, szName)


        def WHashValOfLHashVal(lhashval):
            return 0x0000FFFF & lhashval


        def IsHashValCompatible(lhashval1, lhashval2):
            return (0x00FF0000 & lhashval1) == (0x00FF0000 & lhashval2)

        # /* load the typelib from the file with the given filename
        # WINOLEAUTAPI LoadTypeLib(_In_z_ LPCOLESTR szFile, ITypeLib ** pptlib);
        LoadTypeLib = oleaut32.LoadTypeLib
        LoadTypeLib.restype = WINOLEAUTAPI

        # /* Control how a type library is registered
        class tagREGKIND(ENUM):
            REGKIND_DEFAULT = 1
            REGKIND_REGISTER = 2
            REGKIND_NONE = 3

        REGKIND = tagREGKIND

        # Constants for specifying format in which TLB should be loaded
        # (the default format is 32-bit on WIN32 and 64-bit on WIN64)
        LOAD_TLB_AS_32BIT = 0x20
        LOAD_TLB_AS_64BIT = 0x40
        MASK_TO_RESET_TLB_BITS = ~(LOAD_TLB_AS_32BIT | LOAD_TLB_AS_64BIT)


        # _Check_return_
        # WINOLEAUTAPI LoadTypeLibEx(LPCOLESTR szFile, REGKIND regkind,
        # ITypeLib ** pptlib);
        LoadTypeLibEx = oleaut32.LoadTypeLibEx
        LoadTypeLibEx.restype = WINOLEAUTAPI

        # /* load registered typelib
        # _Check_return_
        # WINOLEAUTAPI LoadRegTypeLib(REFGUID rguid, WORD wVerMajor, WORD wVerMinor,
        # LCID lcid, ITypeLib ** pptlib);
        LoadRegTypeLib = oleaut32.LoadRegTypeLib
        LoadRegTypeLib.restype = WINOLEAUTAPI

        # /* get path to registered typelib
        # WINOLEAUTAPI QueryPathOfRegTypeLib(REFGUID guid, USHORT wMaj, USHORT wMin,
        # LCID lcid, _Out_ LPBSTR lpbstrPathName);
        QueryPathOfRegTypeLib = oleaut32.QueryPathOfRegTypeLib
        QueryPathOfRegTypeLib.restype = WINOLEAUTAPI

        # /* add typelib to registry
        # _Check_return_
        # WINOLEAUTAPI RegisterTypeLib(ITypeLib * ptlib, _In_ LPCOLESTR szFullPath,
        # _In_opt_ LPCOLESTR szHelpDir);
        RegisterTypeLib = oleaut32.RegisterTypeLib
        RegisterTypeLib.restype = WINOLEAUTAPI

        # /* remove typelib from registry
        # _Check_return_
        # WINOLEAUTAPI UnRegisterTypeLib(REFGUID libID, WORD wVerMajor,
        # WORD wVerMinor, LCID lcid, SYSKIND syskind);
        UnRegisterTypeLib = oleaut32.UnRegisterTypeLib
        UnRegisterTypeLib.restype = WINOLEAUTAPI

        # /* Registers a type library for use by the calling user.
        # WINOLEAUTAPI RegisterTypeLibForUser(ITypeLib *ptlib,_In_ OLECHAR  *szFullPath,
        # _In_opt_ OLECHAR  *szHelpDir);
        RegisterTypeLibForUser = oleaut32.RegisterTypeLibForUser
        RegisterTypeLibForUser.restype = WINOLEAUTAPI

        # /* Removes type library information that was registered by using
        # RegisterTypeLibForUser.
        # WINOLEAUTAPI UnRegisterTypeLibForUser(
        # REFGUID         libID,
        # WORD   wMajorVerNum,
        # WORD   wMinorVerNum,
        # LCID            lcid,
        # SYSKIND         syskind);
        UnRegisterTypeLibForUser = oleaut32.UnRegisterTypeLibForUser
        UnRegisterTypeLibForUser.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI CreateTypeLib(SYSKIND syskind, LPCOLESTR szFile,
        # ICreateTypeLib ** ppctlib);
        CreateTypeLib = oleaut32.CreateTypeLib
        CreateTypeLib.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI CreateTypeLib2(SYSKIND syskind, LPCOLESTR szFile,
        # ICreateTypeLib2 **ppctlib);
        CreateTypeLib2 = oleaut32.CreateTypeLib2
        CreateTypeLib2.restype = WINOLEAUTAPI

        # ---------------------------------------------------------------------
        # IDispatch implementation support
        # ---------------------------------------------------------------------
        # [unique]
        LPDISPATCH = POINTER(IDispatch)

        # parameter name
        tagPARAMDATA._fields_ = [
            ('szName', POINTER(OLECHAR)),
            # parameter type
            ('vt', VARTYPE),
        ]

        # method name
        tagMETHODDATA._fields_ = [
            ('szName', POINTER(OLECHAR)),
            # pointer to an array of PARAMDATAs
            ('ppdata', POINTER(PARAMDATA)),
            # method ID
            ('dispid', DISPID),
            # method index
            ('iMeth', UINT),
            # calling convention
            ('cc', CALLCONV),
            # count of arguments
            ('cArgs', UINT),
            # same wFlags as on IDispatch::Invoke()
            ('wFlags', WORD),
            ('vtReturn', VARTYPE),
        ]

        # pointer to an array of METHODDATAs
        tagINTERFACEDATA._fields_ = [
            ('pmethdata', POINTER(METHODDATA)),
            # count of members
            ('cMembers', UINT),
        ]

        # /* Locate the parameter indicated by the given position, and return
        # it coerced to the given target VARTYPE (vtTarg).
        # _Check_return_
        # WINOLEAUTAPI DispGetParam(
        # _In_ DISPPARAMS * pdispparams,
        # UINT position,
        # VARTYPE vtTarg,
        # _Out_ VARIANT * pvarResult,
        # _Out_opt_ UINT * puArgErr
        # );
        DispGetParam = oleaut32.DispGetParam
        DispGetParam.restype = WINOLEAUTAPI

        # /* Automatic TypeInfo driven implementation of
        # IDispatch::GetIDsOfNames()
        # _Check_return_ WINOLEAUTAPI DispGetIDsOfNames(ITypeInfo * ptinfo, _In_reads_(cNames) LPOLESTR* rgszNames,
        # UINT cNames, _Out_writes_(cNames) DISPID * rgdispid);
        DispGetIDsOfNames = oleaut32.DispGetIDsOfNames
        DispGetIDsOfNames.restype = WINOLEAUTAPI

        # /* Automatic TypeInfo driven implementation of IDispatch::Invoke()
        # _Check_return_
        #
    # END IF WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
    # #pragma endregion
    #
    # #pragma region Application Family or OneCore Family
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        #
        # WINOLEAUTAPI DispInvoke(VOID * _this, ITypeInfo * ptinfo, DISPID dispidMember,
        # WORD wFlags, DISPPARAMS * pparams, VARIANT * pvarResult,
        # EXCEPINFO * pexcepinfo, UINT * puArgErr);
        DispInvoke = oleaut32.DispInvoke
        DispInvoke.restype = WINOLEAUTAPI
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        # /* Construct a TypeInfo from an interface data description
        # _Check_return_
        # WINOLEAUTAPI CreateDispTypeInfo(INTERFACEDATA * pidata, LCID lcid,
        # ITypeInfo ** pptinfo);
        CreateDispTypeInfo = oleaut32.CreateDispTypeInfo
        CreateDispTypeInfo.restype = WINOLEAUTAPI

        # /* Create an instance of the standard TypeInfo driven IDispatch
        # implementation.
        # _Check_return_
        # WINOLEAUTAPI CreateStdDispatch(IUnknown * punkOuter, VOID * pvThis,
        # ITypeInfo * ptinfo, IUnknown ** ppunkStdDisp);
        CreateStdDispatch = oleaut32.CreateStdDispatch
        CreateStdDispatch.restype = WINOLEAUTAPI

        # /* Low-level helper for IDispatch::Invoke() provides machine
        # independence for customized Invoke().
        # WINOLEAUTAPI DispCallFunc(VOID * pvInstance, ULONG_PTR oVft, CALLCONV cc,
        # VARTYPE vtReturn, UINT  cActuals, VARTYPE * prgvt,
        # VARIANTARG ** prgpvarg, VARIANT * pvargResult);
        DispCallFunc = oleaut32.DispCallFunc
        DispCallFunc.restype = WINOLEAUTAPI

        # ---------------------------------------------------------------------
        # Active Object Registration API
        # ---------------------------------------------------------------------
        # flags for RegisterActiveObject
        ACTIVEOBJECT_STRONG = 0x0
        ACTIVEOBJECT_WEAK = 0x1


        # _Check_return_
        # WINOLEAUTAPI RegisterActiveObject(IUnknown * punk, REFCLSID rclsid,
        # DWORD dwFlags, DWORD * pdwRegister);
        RegisterActiveObject = oleaut32.RegisterActiveObject
        RegisterActiveObject.restype = WINOLEAUTAPI

        # WINOLEAUTAPI RevokeActiveObject(DWORD dwRegister, VOID * pvReserved);
        RevokeActiveObject = oleaut32.RevokeActiveObject
        RevokeActiveObject.restype = WINOLEAUTAPI

        # WINOLEAUTAPI GetActiveObject(REFCLSID rclsid, VOID * pvReserved,
        # IUnknown ** ppunk);
        GetActiveObject = oleaut32.GetActiveObject
        GetActiveObject.restype = WINOLEAUTAPI

        # ---------------------------------------------------------------------
        # ErrorInfo API
        # ---------------------------------------------------------------------

        # WINOLEAUTAPI SetErrorInfo(_In_ ULONG dwReserved, _In_opt_ IErrorInfo * perrinfo);
        SetErrorInfo = ole32.SetErrorInfo
        SetErrorInfo.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI GetErrorInfo(_In_ ULONG dwReserved, _Outptr_ IErrorInfo ** pperrinfo);
        GetErrorInfo = ole32.GetErrorInfo
        GetErrorInfo.restype = WINOLEAUTAPI

        # _Check_return_
        # WINOLEAUTAPI CreateErrorInfo(_Outptr_ ICreateErrorInfo ** pperrinfo);
        CreateErrorInfo = ole32.CreateErrorInfo
        CreateErrorInfo.restype = WINOLEAUTAPI

        # ---------------------------------------------------------------------
        # User Defined Data types support
        # ---------------------------------------------------------------------
        # WINOLEAUTAPI GetRecordInfoFromTypeInfo(ITypeInfo * pTypeInfo,
        # IRecordInfo ** ppRecInfo);
        GetRecordInfoFromTypeInfo = oleaut32.GetRecordInfoFromTypeInfo
        GetRecordInfoFromTypeInfo.restype = WINOLEAUTAPI

        # WINOLEAUTAPI GetRecordInfoFromGuids(REFGUID rGuidTypeLib,
        # ULONG uVerMajor, ULONG uVerMinor, LCID lcid,
        # REFGUID rGuidTypeInfo, IRecordInfo ** ppRecInfo);
        GetRecordInfoFromGuids = oleaut32.GetRecordInfoFromGuids
        GetRecordInfoFromGuids.restype = WINOLEAUTAPI

        # ---------------------------------------------------------------------
        # MISC API
        # ---------------------------------------------------------------------
        # WINOLEAUTAPI_(VOID) ClearCustData(LPCUSTDATA pCustData);
        ClearCustData = oleaut32.ClearCustData
        ClearCustData.restype = VOID

        if NTDDI_VERSION >= NTDDI_VISTASP1:
            pass
        # END IF

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # Declare variant access functions.
    if (
        (__STDC__ and not defined(_FORCENAMELESSUNION)) or
        defined(NONAMELESSUNION) or
        (not defined(_MSC_EXTENSIONS) and not defined(_FORCENAMELESSUNION))
    ):
        def V_UNION(X, Y):
            return getattr(X.n1.n2.n3, Y)


        def V_VT(X):
            return X.n1.n2.vt


        def V_RECORDINFO(X):
            return X.n1.n2.n3.brecVal.pRecInfo


        def V_RECORD(X):
            return X.n1.n2.n3.brecVal.pvRecord
    else:
        def V_UNION(X, Y):
            return getattr(X, Y)


        def V_VT(X):
            return X.vt


        def V_RECORDINFO(X):
            return X.pRecInfo


        def V_RECORD(X):
            return X.pvRecord
    # END IF

    # /* Variant access macros
    def V_ISBYREF(X):
        return V_VT(X) & VARENUM.VT_BYREF


    def V_ISARRAY(X):
        return V_VT(X) & VARENUM.VT_ARRAY


    def V_ISVECTOR(X):
        return V_VT(X) & VARENUM.VT_VECTOR


    def V_NONE(X):
        return V_I2(X)


    def V_UI1(X):
        return V_UNION(X, 'bVal')


    def V_UI1REF(X):
        return V_UNION(X, 'pbVal')


    def V_I2(X):
        return V_UNION(X, 'iVal')


    def V_I2REF(X):
        return V_UNION(X, 'piVal')


    def V_I4(X):
        return V_UNION(X, 'lVal')


    def V_I4REF(X):
        return V_UNION(X, 'plVal')


    def V_I8(X):
        return V_UNION(X, 'llVal')


    def V_I8REF(X):
        return V_UNION(X, 'pllVal')


    def V_R4(X):
        return V_UNION(X, 'fltVal')


    def V_R4REF(X):
        return V_UNION(X, 'pfltVal')


    def V_R8(X):
        return V_UNION(X, 'dblVal')


    def V_R8REF(X):
        return V_UNION(X, 'pdblVal')


    def V_I1(X):
        return V_UNION(X, 'cVal')


    def V_I1REF(X):
        return V_UNION(X, 'pcVal')


    def V_UI2(X):
        return V_UNION(X, 'uiVal')


    def V_UI2REF(X):
        return V_UNION(X, 'puiVal')


    def V_UI4(X):
        return V_UNION(X, 'ulVal')


    def V_UI4REF(X):
        return V_UNION(X, 'pulVal')


    def V_UI8(X):
        return V_UNION(X, 'ullVal')


    def V_UI8REF(X):
        return V_UNION(X, 'pullVal')


    def V_INT(X):
        return V_UNION(X, 'intVal')


    def V_INTREF(X):
        return V_UNION(X, 'pintVal')


    def V_UINT(X):
        return V_UNION(X, 'uintVal')


    def V_UINTREF(X):
        return V_UNION(X, 'puintVal')


    if defined(_WIN64):
        def V_INT_PTR(X):
            return V_UNION(X, 'llVal')


        def V_UINT_PTR(X):
            return V_UNION(X, 'ullVal')


        def V_INT_PTRREF(X):
            return V_UNION(X, 'pllVal')


        def V_UINT_PTRREF(X):
            return V_UNION(X, 'pullVal')
    else:
        def V_INT_PTR(X):
            return V_UNION(X, 'lVal')


        def V_UINT_PTR(X):
            return V_UNION(X, 'ulVal')


        def V_INT_PTRREF(X):
            return V_UNION(X, 'plVal')


        def V_UINT_PTRREF(X):
            return V_UNION(X, 'pulVal')
    # END IF


    def V_CY(X):
        return V_UNION(X, 'cyVal')


    def V_CYREF(X):
        return V_UNION(X, 'pcyVal')


    def V_DATE(X):
        return V_UNION(X, 'date')


    def V_DATEREF(X):
        return V_UNION(X, 'pdate')


    def V_BSTR(X):
        return V_UNION(X, 'bstrVal')


    def V_BSTRREF(X):
        return V_UNION(X, 'pbstrVal')


    def V_DISPATCH(X):
        return V_UNION(X, 'pdispVal')


    def V_DISPATCHREF(X):
        return V_UNION(X, 'ppdispVal')


    def V_ERROR(X):
        return V_UNION(X, 'scode')


    def V_ERRORREF(X):
        return V_UNION(X, 'pscode')


    def V_BOOL(X):
        return V_UNION(X, 'boolVal')


    def V_BOOLREF(X):
        return V_UNION(X, 'pboolVal')


    def V_UNKNOWN(X):
        return V_UNION(X, 'punkVal')


    def V_UNKNOWNREF(X):
        return V_UNION(X, 'ppunkVal')


    def V_VARIANTREF(X):
        return V_UNION(X, 'pvarVal')


    def V_ARRAY(X):
        return V_UNION(X, 'parray')


    def V_ARRAYREF(X):
        return V_UNION(X, 'pparray')


    def V_BYREF(X):
        return V_UNION(X, 'byref')


    def V_DECIMAL(X):
        return V_UNION(X, 'decVal')


    def V_DECIMALREF(X):
        return V_UNION(X, 'pdecVal')


    if not defined(RC_INVOKED):
        from pyWinAPI.shared.poppack_h import * # NOQA
    # END IF   RC_INVOKED
# END IF   __OLEAUTO_H__

if _MSC_VER >= 1200:
    pass
# END IF


