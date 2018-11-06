

from wtypes_h import (
    LIST_ENTRY,
    VOID,
    LPWSTR,
    LPVOID,
    HRESULT,
    BOOL,
)

from minwinbase_h_1 import CRITICAL_SECTION
import ctypes


activeds = ctypes.windll.Activeds
from winapifamily_h import * # NOQA
# +---------------------------------------------------------------------------

# Microsoft Windows
# Copyright (C) Microsoft Corporation, 1996-1999

# File:       oleds.h

# Contents:   Public header file for all oleds client code

# ----------------------------------------------------------------------------

# HRESULT WINAPI
# ADsGetObject(
#     LPCWSTR lpszPathName,
#     REFIID riid,
#     VOID * * ppObject
#     );
ADsGetObject = activeds.ADsGetObject
ADsGetObject.restype = HRESULT


# HRESULT WINAPI
# ADsBuildEnumerator(
#     IADsContainer *pADsContainer,
#     IEnumVARIANT   **ppEnumVariant
#     );
ADsBuildEnumerator = activeds.ADsBuildEnumerator
ADsBuildEnumerator.restype = HRESULT


# HRESULT WINAPI
# ADsFreeEnumerator(
#     IEnumVARIANT *pEnumVariant
#     );
ADsFreeEnumerator = activeds.ADsFreeEnumerator
ADsFreeEnumerator.restype = HRESULT


# HRESULT WINAPI
# ADsEnumerateNext(
#     IEnumVARIANT *pEnumVariant,
#     ULONG         cElements,
#     VARIANT FAR  *pvar,
#     ULONG FAR    *pcElementsFetched
#     );
ADsEnumerateNext = activeds.ADsEnumerateNext
ADsEnumerateNext.restype = HRESULT


# HRESULT WINAPI
# ADsBuildVarArrayStr(
#     _In_reads_(dwPathNames) LPWSTR * lppPathNames,
#     DWORD  dwPathNames,
#     VARIANT * pVar
#     );
ADsBuildVarArrayStr = activeds.ADsBuildVarArrayStr
ADsBuildVarArrayStr.restype = HRESULT


# HRESULT WINAPI
# ADsBuildVarArrayInt(
#     LPDWORD    lpdwObjectTypes,
#     DWORD      dwObjectTypes,
#     VARIANT * pVar
#     );
ADsBuildVarArrayInt = activeds.ADsBuildVarArrayInt
ADsBuildVarArrayInt.restype = HRESULT


# HRESULT WINAPI
# ADsOpenObject(
#     LPCWSTR lpszPathName,
#     LPCWSTR lpszUserName,
#     LPCWSTR lpszPassword,
#     DWORD  dwReserved,
#     REFIID riid,
#     VOID FAR * FAR * ppObject
#     );
ADsOpenObject = activeds.ADsOpenObject
ADsOpenObject.restype = HRESULT


# Helper functions for extended error support


# HRESULT WINAPI
# ADsGetLastError(
#     OUT     LPDWORD lpError,
#     _Out_writes_(dwErrorBufLen)    LPWSTR  lpErrorBuf,
#     IN      DWORD   dwErrorBufLen,
#     _Out_writes_(dwNameBufLen)     LPWSTR  lpNameBuf,
#     IN      DWORD   dwNameBufLen
#     );
ADsGetLastError = activeds.ADsGetLastError
ADsGetLastError.restype = HRESULT


# VOID WINAPI
# ADsSetLastError(
#     IN  DWORD   dwErr,
#     IN  LPCWSTR  pszError,
#     IN  LPCWSTR  pszProvider
#     );
ADsSetLastError = activeds.ADsSetLastError
ADsSetLastError.restype = VOID


# VOID WINAPI
# ADsFreeAllErrorRecords(
#     VOID);
ADsFreeAllErrorRecords = activeds.ADsFreeAllErrorRecords
ADsFreeAllErrorRecords.restype = VOID


# LPVOID WINAPI
# AllocADsMem(
#     DWORD cb
# );
AllocADsMem = activeds.AllocADsMem
AllocADsMem.restype = LPVOID


# BOOL WINAPI
# FreeADsMem(
#    LPVOID pMem
# );
FreeADsMem = activeds.FreeADsMem
FreeADsMem.restype = BOOL


# LPVOID WINAPI
# ReallocADsMem(
#    LPVOID pOldMem,
#    DWORD cbOld,
#    DWORD cbNew
# );
ReallocADsMem = activeds.ReallocADsMem
ReallocADsMem.restype = LPVOID


# LPWSTR WINAPI
# AllocADsStr(
#     LPCWSTR pStr
# );
AllocADsStr = activeds.AllocADsStr
AllocADsStr.restype = LPWSTR


# BOOL WINAPI
# FreeADsStr(
#    _In_ LPWSTR pStr
# );
FreeADsStr = activeds.FreeADsStr
FreeADsStr.restype = BOOL


# BOOL WINAPI
# ReallocADsStr(
#    _Inout_ LPWSTR *ppStr,
#    _In_ LPWSTR pStr
# );
ReallocADsStr = activeds.ReallocADsStr
ReallocADsStr.restype = BOOL


# HRESULT WINAPI
# ADsEncodeBinaryData (
#    PBYTE   pbSrcData,
#    DWORD   dwSrcLen,
#    _Outptr_ LPWSTR  * ppszDestData
#    );
ADsEncodeBinaryData = activeds.ADsEncodeBinaryData
ADsEncodeBinaryData.restype = HRESULT


# HRESULT WINAPI
# ADsDecodeBinaryData (
#    LPCWSTR szSrcData,
#    PBYTE  *ppbDestData,
#    ULONG  *pdwDestLen
#    );
ADsDecodeBinaryData = activeds.ADsDecodeBinaryData
ADsDecodeBinaryData.restype = HRESULT


# HRESULT WINAPI
# PropVariantToAdsType(
#     VARIANT * pVariant,
#     DWORD dwNumVariant,
#     PADSVALUE *ppAdsValues,
#     PDWORD pdwNumValues
#     );
PropVariantToAdsType = activeds.PropVariantToAdsType
PropVariantToAdsType.restype = HRESULT


# HRESULT WINAPI
# AdsTypeToPropVariant(
#     PADSVALUE pAdsValues,
#     DWORD dwNumValues,
#     VARIANT * pVariant
#     );
AdsTypeToPropVariant = activeds.AdsTypeToPropVariant
AdsTypeToPropVariant.restype = HRESULT


# VOID WINAPI
# AdsFreeAdsValues(
#     PADSVALUE pAdsValues,
#     DWORD dwNumValues
#     );
AdsFreeAdsValues = activeds.AdsFreeAdsValues
AdsFreeAdsValues.restype = VOID


# Helper routines to convert IADsSecurityDescriptor to a binary
# security descriptor and also to convert a binary SD to
# IADsSecurityDescriptor.


# HRESULT WINAPI
# BinarySDToSecurityDescriptor(
#     PSECURITY_DESCRIPTOR  pSecurityDescriptor,
#     VARIANT *pVarsec,
#     LPCWSTR pszServerName,
#     LPCWSTR userName,
#     LPCWSTR passWord,
#     DWORD dwFlags
#     );
BinarySDToSecurityDescriptor = activeds.BinarySDToSecurityDescriptor
BinarySDToSecurityDescriptor.restype = HRESULT


# HRESULT WINAPI
# SecurityDescriptorToBinarySD(
#     VARIANT vVarSecDes,
#     PSECURITY_DESCRIPTOR * ppSecurityDescriptor,
#     PDWORD pdwSDLength,
#     LPCWSTR pszServerName,
#     LPCWSTR userName,
#     LPCWSTR passWord,
#     DWORD dwFlags
#     );
SecurityDescriptorToBinarySD = activeds.SecurityDescriptorToBinarySD
SecurityDescriptorToBinarySD.restype = HRESULT

ADsMemList = LIST_ENTRY
ADsMemCritSect = CRITICAL_SECTION


#
# VOID InitADsMem(
#     VOID
#     ) ;
InitADsMem = activeds.InitADsMem
InitADsMem.restype = VOID


#
# VOID AssertADsMemLeaks(
#     VOID
#     ) ;
AssertADsMemLeaks = activeds.AssertADsMemLeaks
AssertADsMemLeaks.restype = VOID

# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# _ADSHLP_

__all__ = (
    'InitADsMem', 'ADsDecodeBinaryData', 'ADsEnumerateNext', 'FreeADsStr',
    'AdsTypeToPropVariant', 'AssertADsMemLeaks', 'ADsBuildEnumerator',
    'FreeADsMem', 'ReallocADsStr', 'ADsBuildVarArrayInt', 'AllocADsStr',
    'AllocADsMem', 'ADsFreeAllErrorRecords', 'AdsFreeAdsValues',
    'ADsBuildVarArrayStr', 'ADsFreeEnumerator', 'ADsEncodeBinaryData',
    'PropVariantToAdsType', 'ADsSetLastError', 'ADsGetLastError',
    'ADsOpenObject', 'ReallocADsMem', 'ADsGetObject',
    'BinarySDToSecurityDescriptor', 'SecurityDescriptorToBinarySD',
)
