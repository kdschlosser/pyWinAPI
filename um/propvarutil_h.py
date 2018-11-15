import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


# == == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == =
# Copyright (c) Microsoft Corporation. All rights reserved.
# propvarutil.h - Variant and PropVariant helpers
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == =

from pyWinAPI.shared.winapifamily_h import * # NOQA
if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    NTSTATUS = LONG

    from pyWinAPI.um.propapi_h import * # NOQA
    from pyWinAPI.um.shtypes_h import * # NOQA
    from pyWinAPI.um.shlwapi_h import * # NOQA
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    PSSTDAPI = None
    if not defined(PSSTDAPI):
        _PROPSYS_ = None
        if defined(_PROPSYS_):
            PSSTDAPI = STDAPI

            def PSSTDAPI_(type):
                return STDAPI_(type)
        else:
            PSSTDAPI = STDAPICALLTYPE

            def PSSTDAPI_(type):
                return STDAPICALLTYPE(type)

        # END IF
    # END IF   PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

propsys = ctypes.windll.Propsys
ole32 = ctypes.windll.Ole32
ntoskrnl = ctypes.windll.NtosKrnl

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    class tagPSTIME_FLAGS(ENUM):
        PSTF_UTC = 0x00000000
        PSTF_LOCAL = 0x00000001


    PSTF_UTC = tagPSTIME_FLAGS.PSTF_UTC
    PSTF_LOCAL = tagPSTIME_FLAGS.PSTF_LOCAL
    PSTIME_FLAGS = INT

    # == == == == == == == == == ==
    # PropVariant Helpers
    # == == == == == == == == == ==
    # Initialize a propvariant


    # PSSTDAPI InitPropVariantFromResource(
    # _In_ HINSTANCE hinst, _In_ UINT id, _Out_ PROPVARIANT *ppropvar);
    InitPropVariantFromResource = propsys.InitPropVariantFromResource
    InitPropVariantFromResource.restype = PSSTDAPI

# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    # PSSTDAPI InitPropVariantFromCLSID(
    # _In_ REFCLSID clsid, _Out_ PROPVARIANT *ppropvar);
    InitPropVariantFromCLSID = propsys.InitPropVariantFromCLSID
    InitPropVariantFromCLSID.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # PSSTDAPI InitPropVariantFromGUIDAsString(
    # _In_ REFGUID guid, _Out_ PROPVARIANT *ppropvar);
    InitPropVariantFromGUIDAsString = propsys.InitPropVariantFromGUIDAsString
    InitPropVariantFromGUIDAsString.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    # PSSTDAPI InitPropVariantFromFileTime(
    # _In_ FILETIME *pftIn, _Out_ PROPVARIANT *ppropvar);
    InitPropVariantFromFileTime = propsys.InitPropVariantFromFileTime
    InitPropVariantFromFileTime.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # PSSTDAPI InitPropVariantFromPropVariantVectorElem(
    # _In_ REFPROPVARIANT propvarIn, _In_ ULONG iElem,
    # _Out_ PROPVARIANT *ppropvar);
    InitPropVariantFromPropVariantVectorElem = (
        propsys.InitPropVariantFromPropVariantVectorElem
    )
    InitPropVariantFromPropVariantVectorElem.restype = PSSTDAPI

    # PSSTDAPI InitPropVariantVectorFromPropVariant(
    # _In_ REFPROPVARIANT propvarSingle, _Out_ PROPVARIANT *ppropvarVector);
    InitPropVariantVectorFromPropVariant = (
        propsys.InitPropVariantVectorFromPropVariant
    )
    InitPropVariantVectorFromPropVariant.restype = PSSTDAPI

    # PSSTDAPI InitPropVariantFromStrRet(
    # _Inout_ STRRET *pstrret, _In_opt_ PCUITEMID_CHILD pidl,
    #  _Out_ PROPVARIANT *ppropvar);
    InitPropVariantFromStrRet = propsys.InitPropVariantFromStrRet
    InitPropVariantFromStrRet.restype = PSSTDAPI

    # PSSTDAPI InitPropVariantFromStringAsVector(
    # _In_opt_ PCWSTR psz, _Out_ PROPVARIANT *ppropvar);
    InitPropVariantFromStringAsVector = propsys.InitPropVariantFromStringAsVector
    InitPropVariantFromStringAsVector.restype = PSSTDAPI

    if defined(__cplusplus):
        # HRESULT  InitPropVariantFromUInt32(
        # _In_ ULONG ulVal, _Out_ PROPVARIANT *ppropvar);
        InitPropVariantFromUInt32 = propsys.InitPropVariantFromUInt32
        InitPropVariantFromUInt32.restype = HRESULT
    # END IF

    # Extract data from a propvariant
    # PSSTDAPI_(BOOL)      PropVariantToBooleanWithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ BOOL fDefault);
    PropVariantToBooleanWithDefault = propsys.PropVariantToBooleanWithDefault
    PropVariantToBooleanWithDefault.restype = BOOL

    # PSSTDAPI_(SHORT)     PropVariantToInt16WithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ SHORT iDefault);
    PropVariantToInt16WithDefault = propsys.PropVariantToInt16WithDefault
    PropVariantToInt16WithDefault.restype = SHORT

    # PSSTDAPI_(USHORT)    PropVariantToUInt16WithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ USHORT uiDefault);
    PropVariantToUInt16WithDefault = propsys.PropVariantToUInt16WithDefault
    PropVariantToUInt16WithDefault.restype = USHORT

    # PSSTDAPI_(LONG)      PropVariantToInt32WithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ LONG lDefault);
    PropVariantToInt32WithDefault = propsys.PropVariantToInt32WithDefault
    PropVariantToInt32WithDefault.restype = LONG

    # PSSTDAPI_(ULONG)     PropVariantToUInt32WithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ ULONG ulDefault);
    PropVariantToUInt32WithDefault = propsys.PropVariantToUInt32WithDefault
    PropVariantToUInt32WithDefault.restype = ULONG

    # PSSTDAPI_(LONGLONG)  PropVariantToInt64WithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ LONGLONG llDefault);
    PropVariantToInt64WithDefault = propsys.PropVariantToInt64WithDefault
    PropVariantToInt64WithDefault.restype = LONGLONG

    # PSSTDAPI_(ULONGLONG) PropVariantToUInt64WithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ ULONGLONG ullDefault);
    PropVariantToUInt64WithDefault = propsys.PropVariantToUInt64WithDefault
    PropVariantToUInt64WithDefault.restype = ULONGLONG

    # PSSTDAPI_(DOUBLE)    PropVariantToDoubleWithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_ DOUBLE dblDefault);
    PropVariantToDoubleWithDefault = propsys.PropVariantToDoubleWithDefault
    PropVariantToDoubleWithDefault.restype = DOUBLE
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    # PSSTDAPI_(PCWSTR)    PropVariantToStringWithDefault(
    # _In_ REFPROPVARIANT propvarIn, _In_opt_ LPCWSTR pszDefault);
    PropVariantToStringWithDefault = propsys.PropVariantToStringWithDefault
    PropVariantToStringWithDefault.restype = PCWSTR

    # PSSTDAPI             PropVariantToBoolean(
    # _In_ REFPROPVARIANT propvarIn, _Out_ BOOL *pfRet);
    PropVariantToBoolean = propsys.PropVariantToBoolean
    PropVariantToBoolean.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # PSSTDAPI             PropVariantToInt16(
    # _In_ REFPROPVARIANT propvarIn, _Out_ SHORT *piRet);
    PropVariantToInt16 = propsys.PropVariantToInt16
    PropVariantToInt16.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToUInt16(
    # _In_ REFPROPVARIANT propvarIn, _Out_ USHORT *puiRet);
    PropVariantToUInt16 = propsys.PropVariantToUInt16
    PropVariantToUInt16.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToInt32(
    # _In_ REFPROPVARIANT propvarIn, _Out_ LONG *plRet);
    PropVariantToInt32 = propsys.PropVariantToInt32
    PropVariantToInt32.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToUInt32(
    # _In_ REFPROPVARIANT propvarIn, _Out_ ULONG *pulRet);
    PropVariantToUInt32 = propsys.PropVariantToUInt32
    PropVariantToUInt32.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToInt64(
    # _In_ REFPROPVARIANT propvarIn, _Out_ LONGLONG *pllRet);
    PropVariantToInt64 = propsys.PropVariantToInt64
    PropVariantToInt64.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToUInt64(
    # _In_ REFPROPVARIANT propvarIn, _Out_ ULONGLONG *pullRet);
    PropVariantToUInt64 = propsys.PropVariantToUInt64
    PropVariantToUInt64.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToDouble(
    # _In_ REFPROPVARIANT propvarIn, _Out_ DOUBLE *pdblRet);
    PropVariantToDouble = propsys.PropVariantToDouble
    PropVariantToDouble.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToBuffer(
    # _In_ REFPROPVARIANT propvar,
    #  _Out_writes_bytes_(cb) VOID *pv, _In_ UINT cb);
    PropVariantToBuffer = propsys.PropVariantToBuffer
    PropVariantToBuffer.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToString(
    # _In_ REFPROPVARIANT propvar, _Out_writes_(cch) PWSTR psz, _In_ UINT cch);
    PropVariantToString = propsys.PropVariantToString
    PropVariantToString.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    # PSSTDAPI             PropVariantToGUID(
    # _In_ REFPROPVARIANT propvar, _Out_ GUID *pguid);
    PropVariantToGUID = propsys.PropVariantToGUID
    PropVariantToGUID.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToStringAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_nullonfailure_ PWSTR *ppszOut);
    PropVariantToStringAlloc = propsys.PropVariantToStringAlloc
    PropVariantToStringAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToBSTR(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_nullonfailure_ BSTR *pbstrOut);
    PropVariantToBSTR = propsys.PropVariantToBSTR
    PropVariantToBSTR.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # _Check_return_ PSSTDAPI PropVariantToStrRet(
    # _In_ REFPROPVARIANT propvar, _Out_ STRRET *pstrret);
    PropVariantToStrRet = propsys.PropVariantToStrRet
    PropVariantToStrRet.restype = PSSTDAPI

    # PSSTDAPI             PropVariantToFileTime(
    # _In_ REFPROPVARIANT propvar, _In_ PSTIME_FLAGS pstfOut,
    # _Out_ FILETIME* pftOut);
    PropVariantToFileTime = propsys.PropVariantToFileTime
    PropVariantToFileTime.restype = PSSTDAPI

    if defined(__cplusplus):
        pass
    # END IF

    # Returns element count of a VT_VECTOR or VT_ARRAY value; or 1 otherwise
    # PSSTDAPI_(ULONG) PropVariantGetElementCount(_In_ REFPROPVARIANT propvar);
    PropVariantGetElementCount = propsys.PropVariantGetElementCount
    PropVariantGetElementCount.restype = ULONG

    # Extract data from a propvariant into a vector
    # Extract data from a propvariant and return an newly allocated vector
    # (free with CoTaskMemFree)
    #  _Check_return_ PSSTDAPI PropVariantToBooleanVectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    # _Outptr_result_buffer_(*pcElem) BOOL **pprgf, _Out_ ULONG *pcElem);
    PropVariantToBooleanVectorAlloc = propsys.PropVariantToBooleanVectorAlloc
    PropVariantToBooleanVectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToInt16VectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_buffer_(*pcElem) SHORT **pprgn, _Out_ ULONG *pcElem);
    PropVariantToInt16VectorAlloc = propsys.PropVariantToInt16VectorAlloc
    PropVariantToInt16VectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToUInt16VectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_buffer_(*pcElem) USHORT **pprgn, _Out_ ULONG *pcElem);
    PropVariantToUInt16VectorAlloc = propsys.PropVariantToUInt16VectorAlloc
    PropVariantToUInt16VectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToInt32VectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_buffer_(*pcElem) LONG **pprgn, _Out_ ULONG *pcElem);
    PropVariantToInt32VectorAlloc = propsys.PropVariantToInt32VectorAlloc
    PropVariantToInt32VectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToUInt32VectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    # _Outptr_result_buffer_(*pcElem) ULONG **pprgn, _Out_ ULONG *pcElem);
    PropVariantToUInt32VectorAlloc = propsys.PropVariantToUInt32VectorAlloc
    PropVariantToUInt32VectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToInt64VectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_buffer_(*pcElem) LONGLONG **pprgn, _Out_ ULONG *pcElem);
    PropVariantToInt64VectorAlloc = propsys.PropVariantToInt64VectorAlloc
    PropVariantToInt64VectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToUInt64VectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    # _Outptr_result_buffer_(*pcElem) ULONGLONG **pprgn, _Out_ ULONG *pcElem);
    PropVariantToUInt64VectorAlloc = propsys.PropVariantToUInt64VectorAlloc
    PropVariantToUInt64VectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToDoubleVectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_buffer_(*pcElem) DOUBLE **pprgn, _Out_ ULONG *pcElem);
    PropVariantToDoubleVectorAlloc = propsys.PropVariantToDoubleVectorAlloc
    PropVariantToDoubleVectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToFileTimeVectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_buffer_(*pcElem) FILETIME **pprgft, _Out_ ULONG *pcElem);
    PropVariantToFileTimeVectorAlloc = propsys.PropVariantToFileTimeVectorAlloc
    PropVariantToFileTimeVectorAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantToStringVectorAlloc(
    # _In_ REFPROPVARIANT propvar,
    #  _Outptr_result_buffer_(*pcElem) PWSTR **pprgsz, _Out_ ULONG *pcElem);
    PropVariantToStringVectorAlloc = propsys.PropVariantToStringVectorAlloc
    PropVariantToStringVectorAlloc.restype = PSSTDAPI

    # Extract a single element from a propvariant. If it is a VT_VECTOR or
    # VT_ARRAY, returns the element you request.
    # Otherwise iElem must equal 0 and the function will returns the value.
    # PSSTDAPI PropVariantGetBooleanElem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ BOOL *pfVal);
    PropVariantGetBooleanElem = propsys.PropVariantGetBooleanElem
    PropVariantGetBooleanElem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetInt16Elem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ SHORT *pnVal);
    PropVariantGetInt16Elem = propsys.PropVariantGetInt16Elem
    PropVariantGetInt16Elem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetUInt16Elem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ USHORT *pnVal);
    PropVariantGetUInt16Elem = propsys.PropVariantGetUInt16Elem
    PropVariantGetUInt16Elem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetInt32Elem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ LONG *pnVal);
    PropVariantGetInt32Elem = propsys.PropVariantGetInt32Elem
    PropVariantGetInt32Elem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetUInt32Elem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ ULONG *pnVal);
    PropVariantGetUInt32Elem = propsys.PropVariantGetUInt32Elem
    PropVariantGetUInt32Elem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetInt64Elem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ LONGLONG *pnVal);
    PropVariantGetInt64Elem = propsys.PropVariantGetInt64Elem
    PropVariantGetInt64Elem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetUInt64Elem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ ULONGLONG *pnVal);
    PropVariantGetUInt64Elem = propsys.PropVariantGetUInt64Elem
    PropVariantGetUInt64Elem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetDoubleElem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ DOUBLE *pnVal);
    PropVariantGetDoubleElem = propsys.PropVariantGetDoubleElem
    PropVariantGetDoubleElem.restype = PSSTDAPI

    # PSSTDAPI PropVariantGetFileTimeElem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Out_ FILETIME *pftVal);
    PropVariantGetFileTimeElem = propsys.PropVariantGetFileTimeElem
    PropVariantGetFileTimeElem.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI PropVariantGetStringElem(
    # _In_ REFPROPVARIANT propvar, _In_ ULONG iElem, _Outptr_ PWSTR *ppszVal);
    PropVariantGetStringElem = propsys.PropVariantGetStringElem
    PropVariantGetStringElem.restype = PSSTDAPI

    if defined(__cplusplus):
        pass
    # END IF

    # Helpers
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    class PROPVAR_COMPARE_UNIT(ENUM):
        PVCU_DEFAULT = 0
        PVCU_SECOND = 1
        PVCU_MINUTE = 2
        PVCU_HOUR = 3
        PVCU_DAY = 4
        PVCU_MONTH = 5
        PVCU_YEAR = 6


    PVCU_DEFAULT = PROPVAR_COMPARE_UNIT.PVCU_DEFAULT
    PVCU_SECOND = PROPVAR_COMPARE_UNIT.PVCU_SECOND
    PVCU_MINUTE = PROPVAR_COMPARE_UNIT.PVCU_MINUTE
    PVCU_HOUR = PROPVAR_COMPARE_UNIT.PVCU_HOUR
    PVCU_DAY = PROPVAR_COMPARE_UNIT.PVCU_DAY
    PVCU_MONTH = PROPVAR_COMPARE_UNIT.PVCU_MONTH
    PVCU_YEAR = PROPVAR_COMPARE_UNIT.PVCU_YEAR


    class tagPROPVAR_COMPARE_FLAGS(ENUM):
        PVCF_DEFAULT = 0x00000000
        PVCF_TREATEMPTYASGREATERTHAN = 0x00000001
        PVCF_USESTRCMP = 0x00000002
        PVCF_USESTRCMPC = 0x00000004
        PVCF_USESTRCMPI = 0x00000008
        PVCF_USESTRCMPIC = 0x00000010

        # When comparing strings, use CompareStringEx with
        # LOCALE_NAME_USER_DEFAULT and SORT_DIGITSASNUMBERS. This corresponds
        # to the linguistically correct order for UI lists.
        PVCF_DIGITSASNUMBERS_CASESENSITIVE = 0x00000020


    PVCF_DEFAULT = tagPROPVAR_COMPARE_FLAGS.PVCF_DEFAULT
    PVCF_TREATEMPTYASGREATERTHAN = (
        tagPROPVAR_COMPARE_FLAGS.PVCF_TREATEMPTYASGREATERTHAN
    )
    PVCF_USESTRCMP = tagPROPVAR_COMPARE_FLAGS.PVCF_USESTRCMP
    PVCF_USESTRCMPC = tagPROPVAR_COMPARE_FLAGS.PVCF_USESTRCMPC
    PVCF_USESTRCMPI = tagPROPVAR_COMPARE_FLAGS.PVCF_USESTRCMPI
    PVCF_USESTRCMPIC = tagPROPVAR_COMPARE_FLAGS.PVCF_USESTRCMPIC
    PVCF_DIGITSASNUMBERS_CASESENSITIVE = (
        tagPROPVAR_COMPARE_FLAGS.PVCF_DIGITSASNUMBERS_CASESENSITIVE
    )
    PROPVAR_COMPARE_FLAGS = INT

    # Comparisons
    # PSSTDAPI_(INT) PropVariantCompareEx(
    # _In_ REFPROPVARIANT propvar1, _In_ REFPROPVARIANT propvar2,
    # _In_ PROPVAR_COMPARE_UNIT unit, _In_ PROPVAR_COMPARE_FLAGS flags);
    PropVariantCompareEx = propsys.PropVariantCompareEx
    PropVariantCompareEx.restype = INT

    if defined(__cplusplus):
        pass
    # END IF

    class tagPROPVAR_CHANGE_FLAGS(ENUM):
        PVCHF_DEFAULT = 0x00000000
        PVCHF_NOVALUEPROP = 0x00000001
        PVCHF_ALPHABOOL = 0x00000002
        PVCHF_NOUSEROVERRIDE = 0x00000004
        PVCHF_LOCALBOOL = 0x00000008

        # Don't convert a string that looks like hexadecimal (0xABCD) to the
        # numerical equivalent
        PVCHF_NOHEXSTRING = 0x00000010


    PVCHF_DEFAULT = tagPROPVAR_CHANGE_FLAGS.PVCHF_DEFAULT
    PVCHF_NOVALUEPROP = tagPROPVAR_CHANGE_FLAGS.PVCHF_NOVALUEPROP
    PVCHF_ALPHABOOL = tagPROPVAR_CHANGE_FLAGS.PVCHF_ALPHABOOL
    PVCHF_NOUSEROVERRIDE = tagPROPVAR_CHANGE_FLAGS.PVCHF_NOUSEROVERRIDE
    PVCHF_LOCALBOOL = tagPROPVAR_CHANGE_FLAGS.PVCHF_LOCALBOOL
    PVCHF_NOHEXSTRING = tagPROPVAR_CHANGE_FLAGS.PVCHF_NOHEXSTRING
    PROPVAR_CHANGE_FLAGS = INT

    # Coersions

    # PSSTDAPI PropVariantChangeType(
    # _Out_ PROPVARIANT *ppropvarDest, _In_ REFPROPVARIANT propvarSrc,
    # _In_ PROPVAR_CHANGE_FLAGS flags, _In_ VARTYPE vt);
    PropVariantChangeType = ole32.PropVariantChangeType
    PropVariantChangeType.restype = PSSTDAPI

    # Conversions    # PSSTDAPI PropVariantToVariant(
    # _In_ PROPVARIANT *pPropVar, _Out_ VARIANT *pVar);
    PropVariantToVariant = propsys.PropVariantToVariant
    PropVariantToVariant.restype = PSSTDAPI

    # PSSTDAPI VariantToPropVariant(
    # _In_ VARIANT* pVar, _Out_ PROPVARIANT* pPropVar);
    VariantToPropVariant = propsys.VariantToPropVariant
    VariantToPropVariant.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # Stg functions    # _Check_return_ PSSTDAPI StgSerializePropVariant(
    # _In_ PROPVARIANT* ppropvar,
    # _Outptr_result_bytebuffer_(*pcb) SERIALIZEDPROPERTYVALUE** ppProp,
    # _Out_ ULONG* pcb);
    StgSerializePropVariant = propsys.StgSerializePropVariant
    StgSerializePropVariant.restype = PSSTDAPI

    # PSSTDAPI StgDeserializePropVariant(
    # _In_ SERIALIZEDPROPERTYVALUE* pprop,
    # _In_ ULONG cbMax,
    # _Out_ PROPVARIANT* ppropvar);
    StgDeserializePropVariant = propsys.StgDeserializePropVariant
    StgDeserializePropVariant.restype = PSSTDAPI

    # == == == == == == == ==
    # Variant Helpers
    # == == == == == == == ==
    if defined(__cplusplus):
        pass
    # END IF

    # Initialize a VARIANT
    # PSSTDAPI InitVariantFromResource(
    # _In_ HINSTANCE hinst, _In_ UINT id, _Out_ VARIANT *pvar);
    InitVariantFromResource = propsys.InitVariantFromResource
    InitVariantFromResource.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    pass
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # PSSTDAPI InitVariantFromGUIDAsString(
    # _In_ REFGUID guid, _Out_ VARIANT *pvar);
    InitVariantFromGUIDAsString = propsys.InitVariantFromGUIDAsString
    InitVariantFromGUIDAsString.restype = PSSTDAPI

    # PSSTDAPI InitVariantFromFileTime(
    # _In_ FILETIME *pft, _Out_ VARIANT *pvar);
    InitVariantFromFileTime = propsys.InitVariantFromFileTime
    InitVariantFromFileTime.restype = PSSTDAPI

    # PSSTDAPI InitVariantFromStrRet(
    # _In_ STRRET *pstrret, _In_ PCUITEMID_CHILD pidl, _Out_ VARIANT *pvar);
    InitVariantFromStrRet = propsys.InitVariantFromStrRet
    InitVariantFromStrRet.restype = PSSTDAPI

    # PSSTDAPI InitVariantFromVariantArrayElem(
    # _In_ REFVARIANT varIn, _In_ ULONG iElem, _Out_ VARIANT *pvar);
    InitVariantFromVariantArrayElem = propsys.InitVariantFromVariantArrayElem
    InitVariantFromVariantArrayElem.restype = PSSTDAPI

    if defined(__cplusplus):
        # HRESULT  InitVariantFromString(_In_ PCWSTR psz, _Out_ VARIANT *pvar);
        InitVariantFromString = propsys.InitVariantFromString
        InitVariantFromString.restype = HRESULT
    # END IF

    # Extract data from a VARIANT
    #  PSSTDAPI_(BOOL)       VariantToBooleanWithDefault(
    # _In_ REFVARIANT varIn, _In_ BOOL fDefault);
    VariantToBooleanWithDefault = propsys.VariantToBooleanWithDefault
    VariantToBooleanWithDefault.restype = BOOL

    # PSSTDAPI_(SHORT)      VariantToInt16WithDefault(
    # _In_ REFVARIANT varIn, _In_ SHORT iDefault);
    VariantToInt16WithDefault = propsys.VariantToInt16WithDefault
    VariantToInt16WithDefault.restype = SHORT

    # PSSTDAPI_(USHORT)     VariantToUInt16WithDefault(
    # _In_ REFVARIANT varIn, _In_ USHORT uiDefault);
    VariantToUInt16WithDefault = propsys.VariantToUInt16WithDefault
    VariantToUInt16WithDefault.restype = USHORT

    # PSSTDAPI_(LONG)       VariantToInt32WithDefault(
    # _In_ REFVARIANT varIn, _In_ LONG lDefault);
    VariantToInt32WithDefault = propsys.VariantToInt32WithDefault
    VariantToInt32WithDefault.restype = LONG

    # PSSTDAPI_(ULONG)      VariantToUInt32WithDefault(
    # _In_ REFVARIANT varIn, _In_ ULONG ulDefault);
    VariantToUInt32WithDefault = propsys.VariantToUInt32WithDefault
    VariantToUInt32WithDefault.restype = ULONG

    # PSSTDAPI_(LONGLONG)   VariantToInt64WithDefault(
    # _In_ REFVARIANT varIn, _In_ LONGLONG llDefault);
    VariantToInt64WithDefault = propsys.VariantToInt64WithDefault
    VariantToInt64WithDefault.restype = LONGLONG

    # PSSTDAPI_(ULONGLONG)  VariantToUInt64WithDefault(
    # _In_ REFVARIANT varIn, _In_ ULONGLONG ullDefault);
    VariantToUInt64WithDefault = propsys.VariantToUInt64WithDefault
    VariantToUInt64WithDefault.restype = ULONGLONG

    # PSSTDAPI_(DOUBLE)     VariantToDoubleWithDefault(
    # _In_ REFVARIANT varIn, _In_ DOUBLE dblDefault);
    VariantToDoubleWithDefault = propsys.VariantToDoubleWithDefault
    VariantToDoubleWithDefault.restype = DOUBLE

    # PSSTDAPI_(PCWSTR)     VariantToStringWithDefault(
    # _In_ REFVARIANT varIn, _In_opt_ LPCWSTR pszDefault);
    VariantToStringWithDefault = propsys.VariantToStringWithDefault
    VariantToStringWithDefault.restype = PCWSTR

    # PSSTDAPI              VariantToBoolean(
    # _In_ REFVARIANT varIn, _Out_ BOOL *pfRet);
    VariantToBoolean = propsys.VariantToBoolean
    VariantToBoolean.restype = PSSTDAPI

    # PSSTDAPI              VariantToInt16(
    # _In_ REFVARIANT varIn, _Out_ SHORT *piRet);
    VariantToInt16 = propsys.VariantToInt16
    VariantToInt16.restype = PSSTDAPI

    # PSSTDAPI              VariantToUInt16(
    # _In_ REFVARIANT varIn, _Out_ USHORT *puiRet);
    VariantToUInt16 = propsys.VariantToUInt16
    VariantToUInt16.restype = PSSTDAPI

    # PSSTDAPI              VariantToInt32(
    # _In_ REFVARIANT varIn, _Out_ LONG *plRet);
    VariantToInt32 = propsys.VariantToInt32
    VariantToInt32.restype = PSSTDAPI

    # PSSTDAPI              VariantToUInt32(
    # _In_ REFVARIANT varIn, _Out_ ULONG *pulRet);
    VariantToUInt32 = propsys.VariantToUInt32
    VariantToUInt32.restype = PSSTDAPI

    # PSSTDAPI              VariantToInt64(
    # _In_ REFVARIANT varIn, _Out_ LONGLONG *pllRet);
    VariantToInt64 = propsys.VariantToInt64
    VariantToInt64.restype = PSSTDAPI

    # PSSTDAPI              VariantToUInt64(
    # _In_ REFVARIANT varIn, _Out_ ULONGLONG *pullRet);
    VariantToUInt64 = propsys.VariantToUInt64
    VariantToUInt64.restype = PSSTDAPI

    # PSSTDAPI              VariantToDouble(
    # _In_ REFVARIANT varIn, _Out_ DOUBLE *pdblRet);
    VariantToDouble = propsys.VariantToDouble
    VariantToDouble.restype = PSSTDAPI

    # PSSTDAPI              VariantToBuffer(
    # _In_ REFVARIANT varIn, _Out_writes_bytes_(cb) VOID *pv, _In_ UINT cb);
    VariantToBuffer = propsys.VariantToBuffer
    VariantToBuffer.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
    # PSSTDAPI              VariantToGUID(
    # _In_ REFVARIANT varIn, _Out_ GUID *pguid);
    VariantToGUID = propsys.VariantToGUID
    VariantToGUID.restype = PSSTDAPI
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
    # PSSTDAPI              VariantToString(
    # _In_ REFVARIANT varIn, _Out_writes_(cchBuf) PWSTR pszBuf,
    #  _In_ UINT cchBuf);
    VariantToString = propsys.VariantToString
    VariantToString.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToStringAlloc(
    # _In_ REFVARIANT varIn, _Outptr_result_nullonfailure_ PWSTR *ppszBuf);
    VariantToStringAlloc = propsys.VariantToStringAlloc
    VariantToStringAlloc.restype = PSSTDAPI

    # PSSTDAPI              VariantToDosDateTime(
    # _In_ REFVARIANT varIn, _Out_ WORD *pwDate, _Out_ WORD *pwTime);
    VariantToDosDateTime = propsys.VariantToDosDateTime
    VariantToDosDateTime.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToStrRet(
    # _In_ REFVARIANT varIn, _Out_ STRRET *pstrret);
    VariantToStrRet = propsys.VariantToStrRet
    VariantToStrRet.restype = PSSTDAPI

    # PSSTDAPI              VariantToFileTime(
    # _In_ REFVARIANT varIn, _In_ PSTIME_FLAGS stfOut, _Out_ FILETIME* pftOut);
    VariantToFileTime = propsys.VariantToFileTime
    VariantToFileTime.restype = PSSTDAPI

    # Get the element count. Returns number of elements for values of type
    # VT_ARRAY; returns 1 otherwise.
    #  PSSTDAPI_(ULONG) VariantGetElementCount(_In_ REFVARIANT varIn);
    VariantGetElementCount = propsys.VariantGetElementCount
    VariantGetElementCount.restype = ULONG

    # Extract data from a VARIANT into a vector
    # Extract data from a VARIANT into a newly allocated vector
    # (free with CoTaskMemFree)

    #  _Check_return_ PSSTDAPI VariantToBooleanArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) BOOL **pprgf,
    #  _Out_ ULONG *pcElem);
    VariantToBooleanArrayAlloc = propsys.VariantToBooleanArrayAlloc
    VariantToBooleanArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToInt16ArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) SHORT **pprgn,
    #  _Out_ ULONG *pcElem);
    VariantToInt16ArrayAlloc = propsys.VariantToInt16ArrayAlloc
    VariantToInt16ArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToUInt16ArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) USHORT **pprgn,
    #  _Out_ ULONG *pcElem);
    VariantToUInt16ArrayAlloc = propsys.VariantToUInt16ArrayAlloc
    VariantToUInt16ArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToInt32ArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) LONG **pprgn,
    #  _Out_ ULONG *pcElem);
    VariantToInt32ArrayAlloc = propsys.VariantToInt32ArrayAlloc
    VariantToInt32ArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToUInt32ArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) ULONG **pprgn,
    #  _Out_ ULONG *pcElem);
    VariantToUInt32ArrayAlloc = propsys.VariantToUInt32ArrayAlloc
    VariantToUInt32ArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToInt64ArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) LONGLONG **pprgn,
    #  _Out_ ULONG *pcElem);
    VariantToInt64ArrayAlloc = propsys.VariantToInt64ArrayAlloc
    VariantToInt64ArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToUInt64ArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) ULONGLONG **pprgn,
    #  _Out_ ULONG *pcElem);
    VariantToUInt64ArrayAlloc = propsys.VariantToUInt64ArrayAlloc
    VariantToUInt64ArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToDoubleArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) DOUBLE **pprgn,
    #  _Out_ ULONG *pcElem);
    VariantToDoubleArrayAlloc = propsys.VariantToDoubleArrayAlloc
    VariantToDoubleArrayAlloc.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantToStringArrayAlloc(
    # _In_ REFVARIANT var, _Outptr_result_buffer_(*pcElem) PWSTR **pprgsz,
    #  _Out_ ULONG *pcElem);
    VariantToStringArrayAlloc = propsys.VariantToStringArrayAlloc
    VariantToStringArrayAlloc.restype = PSSTDAPI

    # Get a single element of a VARIANT. If it is type VT_ARRAY, returns a the
    # requested element. Otherwise
    # iElem must equal 0 and the function returns the value.

    #  PSSTDAPI VariantGetBooleanElem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ BOOL *pfVal);
    VariantGetBooleanElem = propsys.VariantGetBooleanElem
    VariantGetBooleanElem.restype = PSSTDAPI

    # PSSTDAPI VariantGetInt16Elem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ SHORT *pnVal);
    VariantGetInt16Elem = propsys.VariantGetInt16Elem
    VariantGetInt16Elem.restype = PSSTDAPI

    # PSSTDAPI VariantGetUInt16Elem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ USHORT *pnVal);
    VariantGetUInt16Elem = propsys.VariantGetUInt16Elem
    VariantGetUInt16Elem.restype = PSSTDAPI

    # PSSTDAPI VariantGetInt32Elem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ LONG *pnVal);
    VariantGetInt32Elem = propsys.VariantGetInt32Elem
    VariantGetInt32Elem.restype = PSSTDAPI

    # PSSTDAPI VariantGetUInt32Elem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ ULONG *pnVal);
    VariantGetUInt32Elem = propsys.VariantGetUInt32Elem
    VariantGetUInt32Elem.restype = PSSTDAPI

    # PSSTDAPI VariantGetInt64Elem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ LONGLONG *pnVal);
    VariantGetInt64Elem = propsys.VariantGetInt64Elem
    VariantGetInt64Elem.restype = PSSTDAPI

    # PSSTDAPI VariantGetUInt64Elem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ ULONGLONG *pnVal);
    VariantGetUInt64Elem = propsys.VariantGetUInt64Elem
    VariantGetUInt64Elem.restype = PSSTDAPI

    # PSSTDAPI VariantGetDoubleElem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Out_ DOUBLE *pnVal);
    VariantGetDoubleElem = propsys.VariantGetDoubleElem
    VariantGetDoubleElem.restype = PSSTDAPI

    # _Check_return_ PSSTDAPI VariantGetStringElem(
    # _In_ REFVARIANT var, _In_ ULONG iElem, _Outptr_ PWSTR *ppszVal);
    VariantGetStringElem = propsys.VariantGetStringElem
    VariantGetStringElem.restype = PSSTDAPI

    if defined(__cplusplus):
        pass
    # END IF

    # Helpers
    #  PSSTDAPI_(INT) VariantCompare(
    # _In_ REFVARIANT var1, _In_ REFVARIANT var2);
    VariantCompare = propsys.VariantCompare
    VariantCompare.restype = INT

    # == == == == == == == == == == == == == =
    # Property - specific notions
    # == == == == == == == == == == == == == =
    # The progress bar property control uses a specially formatted PROPVARIANT
    # to convey the look of the progress bar
    # propvar.vt = VT_UI4
    # propvar.caul.pElems[0] = current progress
    # propvar.caul.pElems[1] = total progress
    # propvar.caul.pElems[2] = DRAWPROGRESSFLAGS (see below);
    class DRAWPROGRESSFLAGS(ENUM):
        DPF_NONE = 0x0
        DPF_MARQUEE = 0x1
        DPF_MARQUEE_COMPLETE = 0x2
        DPF_ERROR = 0x4
        DPF_WARNING = 0x8
        DPF_STOPPED = 0x10


# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# == == == == == == == ==
# Inline Helpers
# == == == == == == == ==
if defined(__cplusplus) and not defined(CINTERFACE):
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # }
        #
        # inline HRESULT InitPropVariantFromUInt32(
        # _In_ ULONG ulVal, _Out_ PROPVARIANT *ppropvar)
        # {
        # V_VT(ppropvar) = VT_UI4;
        InitPropVariantFromUInt32 = propsys.InitPropVariantFromUInt32
        InitPropVariantFromUInt32.restype = HRESULT

        # inline HRESULT InitPropVariantFromUInt32(
        # _In_ ULONG ulVal, _Out_ PROPVARIANT *ppropvar)
        # {
        # V_VT(ppropvar) = VT_UI4;
        InitPropVariantFromUInt32 = propsys.InitPropVariantFromUInt32
        InitPropVariantFromUInt32.restype = HRESULT

        # Creates a VT_LPWSTR propvariant.
        # Previous API behavior counter to the SAL requirement.

        # Creates a VT_VECTOR | VT_UI1 propvariant.        # }
        #
        # // If TRUE, propvar contains a unicode string.
        # Use PropVariantToStringWithDefault(propvar, NULL) to retrieve it.
        # inline BOOL IsPropVariantString(_In_ REFPROPVARIANT propvar)
        # {
        # return (PropVariantToStringWithDefault(propvar, NULL) != NULL);
        PropVariantToStringWithDefault = propsys.PropVariantToStringWithDefault
        PropVariantToStringWithDefault.restype = BOOL

        # If TRUE, propvar contains a unicode string. Use
        # PropVariantToStringWithDefault(propvar, NULL) to retrieve it.
        #  }
        #
        # // Handles INT instead of LONG
        # inline HRESULT PropVariantToInt32(
        # _In_ REFPROPVARIANT propvarIn, _Out_ INT *piRet)
        # {
        # return PropVariantToInt32(propvarIn, (LONG*)piRet);
        PropVariantToInt32 = propsys.PropVariantToInt32
        PropVariantToInt32.restype = HRESULT

        # Handles INT instead of LONG
        #  inline HRESULT PropVariantToInt32(
        # _In_ REFPROPVARIANT propvarIn, _Out_ INT *piRet)
        # {
        # return PropVariantToInt32(propvarIn, (LONG*)piRet);
        PropVariantToInt32 = propsys.PropVariantToInt32
        PropVariantToInt32.restype = HRESULT

        # // Handles UINT instead of ULONG
        # inline HRESULT PropVariantToUInt32(
        # _In_ REFPROPVARIANT propvarIn, _Out_ UINT *piRet)
        # {
        # return PropVariantToUInt32(propvarIn, (ULONG*)piRet);
        PropVariantToUInt32 = propsys.PropVariantToUInt32
        PropVariantToUInt32.restype = HRESULT

        # Handles UINT instead of ULONG
        # inline HRESULT PropVariantToUInt32(
        # _In_ REFPROPVARIANT propvarIn, _Out_ UINT *piRet)
        # {
        # return PropVariantToUInt32(propvarIn, (ULONG*)piRet);
        PropVariantToUInt32 = propsys.PropVariantToUInt32
        PropVariantToUInt32.restype = HRESULT

        # inline HRESULT PropVariantToCLSID(
        # _In_ REFPROPVARIANT propvarIn, _Out_ CLSID *pclsid)
        # {
        # return PropVariantToGUID(propvarIn, (GUID*)pclsid);
        PropVariantToCLSID = propsys.PropVariantToCLSID
        PropVariantToCLSID.restype = HRESULT

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # inline INT PropVariantCompare(
        # _In_ REFPROPVARIANT propvar1, _In_ REFPROPVARIANT propvar2)
        # {
        # return PropVariantCompareEx(propvar1, propvar2, PVCU_DEFAULT, PVCF_DEFAULT);
        PropVariantCompare = propsys.PropVariantCompare
        PropVariantCompare.restype = INT

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # inline HRESULT PropVariantGetElem(
        # _In_ REFPROPVARIANT propvarIn,
        # _In_ ULONG iElem, _Out_ PROPVARIANT *ppropvar)
        # {
        # return InitPropVariantFromPropVariantVectorElem(
        # propvarIn, iElem, ppropvar);
        PropVariantGetElem = propsys.PropVariantGetElem
        PropVariantGetElem.restype = HRESULT

        # inline HRESULT InitVariantFromString(
        # _In_ PCWSTR psz, _Out_ VARIANT *pvar)
        # {
        # V_VT(pvar) = VT_BSTR;
        InitVariantFromString = propsys.InitVariantFromString
        InitVariantFromString.restype = HRESULT

        # Creates a VT_DATE variant
        # if TRUE, you can use VariantToStringCast to obtain the string pointer
        # Creates a VT_ARRAY | VT_UI1 variant.
        # }
        #
        # // Handles INT instead of LONG
        # inline HRESULT VariantToInt32(
        # _In_ REFVARIANT varIn, _Out_ INT *piRet)
        # {
        # return VariantToInt32(varIn, (LONG*)piRet);
        VariantToInt32 = propsys.VariantToInt32
        VariantToInt32.restype = HRESULT

        # // Handles UINT instead of ULONG
        # inline HRESULT VariantToUInt32(
        # _In_ REFVARIANT varIn, _Out_ UINT *piRet)
        # {
        # return VariantToUInt32(varIn, (ULONG*)piRet);
        VariantToUInt32 = propsys.VariantToUInt32
        VariantToUInt32.restype = HRESULT

        # inline HRESULT VariantGetElem(
        # _In_ REFVARIANT varIn, _In_ ULONG iElem, _Out_ VARIANT *pvar)
        # {
        # return InitVariantFromVariantArrayElem(varIn, iElem, pvar);
        VariantGetElem = propsys.VariantGetElem
        VariantGetElem.restype = HRESULT

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __cplusplus and not CINTERFACE
