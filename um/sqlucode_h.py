import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__SQLUCODE = None
SQL_NOUNICODEMAP = None



# -----------------------------------------------------------------------------
# File:  sqlucode.h
# Copyright:  Copyright (c) Microsoft Corporation
# Contents:  This is the the unicode include for ODBC Core functions
# Comments:
# -----------------------------------------------------------------------------
if not defined(__SQLUCODE):
    __SQLUCODE = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    odbc32 = ctypes.windll.ODBC32

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if defined(__cplusplus):
            # Assume C declarations for C + +
            pass
        # END IF  __cplusplus
        from sqlext_h import * # NOQA
        SQL_WCHAR = -8
        SQL_WVARCHAR = -9
        SQL_WLONGVARCHAR = -10
        SQL_C_WCHAR = SQL_WCHAR
        if defined(UNICODE):
            SQL_C_TCHAR = SQL_C_WCHAR
        else:
            SQL_C_TCHAR = SQL_C_CHAR
        # END IF

        SQL_SQLSTATE_SIZEW = 10        # size of SQLSTATE for unicode
        if not defined(RC_INVOKED):
            #
            # // UNICODE versions
            if defined(_WIN64):
                # SQLRETURN SQL_API SQLColAttributeW
                # (
                # SQLHSTMT        hstmt,
                # SQLUSMALLINT    iCol,
                # SQLUSMALLINT    iField,
                # _Out_writes_bytes_opt_(cbDescMax)
                # SQLPOINTER      pCharAttr,
                # SQLSMALLINT     cbDescMax,
                # _Out_opt_
                # SQLSMALLINT     *pcbCharAttr,
                # _Out_opt_
                # SQLLEN          *pNumAttr
                # );
                SQLColAttributeW = odbc32.SQLColAttributeW
                SQLColAttributeW.restype = SQLRETURN
            else:
                # SQLRETURN SQL_API SQLColAttributeW(
                # SQLHSTMT        hstmt,
                # SQLUSMALLINT    iCol,
                # SQLUSMALLINT    iField,
                # _Out_writes_bytes_opt_(cbDescMax)
                # SQLPOINTER      pCharAttr,
                # SQLSMALLINT     cbDescMax,
                # _Out_opt_
                # SQLSMALLINT     *pcbCharAttr,
                # _Out_opt_
                # SQLPOINTER      pNumAttr);
                SQLColAttributeW = odbc32.SQLColAttributeW
                SQLColAttributeW.restype = SQLRETURN
            # END IF

            # SQLRETURN SQL_API SQLColAttributesW
            # (
            # SQLHSTMT        hstmt,
            # SQLUSMALLINT    icol,
            # SQLUSMALLINT    fDescType,
            # _Out_writes_bytes_opt_(cbDescMax)
            # SQLPOINTER      rgbDesc,
            # SQLSMALLINT     cbDescMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbDesc,
            # _Out_opt_
            # SQLLEN          *pfDesc
            # );
            SQLColAttributesW = odbc32.SQLColAttributesW
            SQLColAttributesW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLConnectW
            # (
            # SQLHDBC             hdbc,
            # _In_reads_(cchDSN) SQLWCHAR* szDSN,
            # SQLSMALLINT         cchDSN,
            # _In_reads_(cchUID) SQLWCHAR* szUID,
            # SQLSMALLINT         cchUID,
            # _In_reads_(cchAuthStr) SQLWCHAR* szAuthStr,
            # SQLSMALLINT         cchAuthStr
            # );
            SQLConnectW = odbc32.SQLConnectW
            SQLConnectW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDescribeColW
            # (
            # SQLHSTMT            hstmt,
            # SQLUSMALLINT        icol,
            # _Out_writes_opt_(cchColNameMax) SQLWCHAR* szColName,
            # SQLSMALLINT         cchColNameMax,
            # _Out_opt_
            # SQLSMALLINT*        pcchColName,
            # _Out_opt_
            # SQLSMALLINT*        pfSqlType,
            # _Out_opt_
            # SQLULEN*            pcbColDef,
            # _Out_opt_
            # SQLSMALLINT*        pibScale,
            # _Out_opt_
            # SQLSMALLINT*        pfNullable
            # );
            SQLDescribeColW = odbc32.SQLDescribeColW
            SQLDescribeColW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLErrorW
            # (
            # SQLHENV             henv,
            # SQLHDBC             hdbc,
            # SQLHSTMT            hstmt,
            # _Out_writes_(6) SQLWCHAR* wszSqlState,
            # _Out_opt_ SQLINTEGER*         pfNativeError,
            # _Out_writes_opt_(cchErrorMsgMax) SQLWCHAR* wszErrorMsg,
            # SQLSMALLINT         cchErrorMsgMax,
            # _Out_opt_ SQLSMALLINT*        pcchErrorMsg
            # );
            SQLErrorW = odbc32.SQLErrorW
            SQLErrorW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLExecDirectW
            # (
            # SQLHSTMT    hstmt,
            # _In_reads_opt_(TextLength) SQLWCHAR* szSqlStr,
            # SQLINTEGER  TextLength
            # );
            SQLExecDirectW = odbc32.SQLExecDirectW
            SQLExecDirectW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetConnectAttrW
            # (
            # SQLHDBC     hdbc,
            # SQLINTEGER  fAttribute,
            # _Out_writes_opt_(_Inexpressible_(cbValueMax))
            # SQLPOINTER  rgbValue,
            # SQLINTEGER  cbValueMax,
            # _Out_opt_
            # SQLINTEGER* pcbValue
            # );
            SQLGetConnectAttrW = odbc32.SQLGetConnectAttrW
            SQLGetConnectAttrW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetCursorNameW
            # (
            # SQLHSTMT        hstmt,
            # _Out_writes_opt_(cchCursorMax) SQLWCHAR* szCursor,
            # SQLSMALLINT     cchCursorMax,
            # _Out_opt_
            # SQLSMALLINT*    pcchCursor
            # );
            SQLGetCursorNameW = odbc32.SQLGetCursorNameW
            SQLGetCursorNameW.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLSetDescFieldW
                # (
                # SQLHDESC        DescriptorHandle,
                # SQLSMALLINT     RecNumber,
                # SQLSMALLINT     FieldIdentifier,
                # SQLPOINTER      Value,
                # SQLINTEGER      BufferLength
                # );
                SQLSetDescFieldW = odbc32.SQLSetDescFieldW
                SQLSetDescFieldW.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetDescFieldW
                # (
                # SQLHDESC        hdesc,
                # SQLSMALLINT     iRecord,
                # SQLSMALLINT     iField,
                # _Out_writes_opt_(_Inexpressible_(cbBufferLength))
                # SQLPOINTER      rgbValue,
                # SQLINTEGER      cbBufferLength,
                # _Out_opt_
                # SQLINTEGER      *StringLength
                # );
                SQLGetDescFieldW = odbc32.SQLGetDescFieldW
                SQLGetDescFieldW.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetDescRecW
                # (
                # SQLHDESC        hdesc,
                # SQLSMALLINT     iRecord,
                # _Out_writes_opt_(cchNameMax) SQLWCHAR* szName,
                # SQLSMALLINT     cchNameMax,
                # _Out_opt_
                # SQLSMALLINT     *pcchName,
                # _Out_opt_
                # SQLSMALLINT     *pfType,
                # _Out_opt_
                # SQLSMALLINT     *pfSubType,
                # _Out_opt_
                # SQLLEN          *pLength,
                # _Out_opt_
                # SQLSMALLINT     *pPrecision,
                # _Out_opt_
                # SQLSMALLINT     *pScale,
                # _Out_opt_
                # SQLSMALLINT     *pNullable
                # );
                SQLGetDescRecW = odbc32.SQLGetDescRecW
                SQLGetDescRecW.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetDiagFieldW
                # (
                # SQLSMALLINT     fHandleType,
                # SQLHANDLE       handle,
                # SQLSMALLINT     iRecord,
                # SQLSMALLINT     fDiagField,
                # _Out_writes_opt_(_Inexpressible_(cbBufferLength))
                # SQLPOINTER      rgbDiagInfo,
                # SQLSMALLINT     cbBufferLength,
                # _Out_opt_
                # SQLSMALLINT     *pcbStringLength
                # );
                SQLGetDiagFieldW = odbc32.SQLGetDiagFieldW
                SQLGetDiagFieldW.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetDiagRecW
                # (
                # SQLSMALLINT     fHandleType,
                # SQLHANDLE       handle,
                # SQLSMALLINT     iRecord,
                # _Out_writes_opt_(6) SQLWCHAR* szSqlState,
                # SQLINTEGER*     pfNativeError,
                # _Out_writes_opt_(cchErrorMsgMax) SQLWCHAR* szErrorMsg,
                # SQLSMALLINT     cchErrorMsgMax,
                # SQLSMALLINT*    pcchErrorMsg
                # );
                SQLGetDiagRecW = odbc32.SQLGetDiagRecW
                SQLGetDiagRecW.restype = SQLRETURN

                if not defined(SQL_NOUNICODEMAP):
                    if defined(UNICODE):
                        SQLGetDescField = SQLGetDescFieldW
                        SQLGetDescRec = SQLGetDescRecW
                        SQLGetDiagField = SQLGetDiagFieldW
                        SQLGetDiagRec = SQLGetDiagRecW
                        SQLSetDescField = SQLSetDescFieldW
            # ENDIF

            # SQLRETURN SQL_API SQLPrepareW
            # (
            # SQLHSTMT    hstmt,
            # _In_reads_(cchSqlStr) SQLWCHAR* szSqlStr,
            # SQLINTEGER  cchSqlStr
            # );
            SQLPrepareW = odbc32.SQLPrepareW
            SQLPrepareW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetConnectAttrW(
            # SQLHDBC            hdbc,
            # SQLINTEGER         fAttribute,
            # _In_reads_bytes_opt_(cbValue)
            # SQLPOINTER         rgbValue,
            # SQLINTEGER         cbValue);
            SQLSetConnectAttrW = odbc32.SQLSetConnectAttrW
            SQLSetConnectAttrW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetCursorNameW
            # (
            # SQLHSTMT            hstmt,
            # _In_reads_(cchCursor) SQLWCHAR* szCursor,
            # SQLSMALLINT         cchCursor
            # );
            SQLSetCursorNameW = odbc32.SQLSetCursorNameW
            SQLSetCursorNameW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLColumnsW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchTableName) SQLWCHAR*      szTableName,
            # SQLSMALLINT        cchTableName,
            # _In_reads_opt_(cchColumnName) SQLWCHAR*     szColumnName,
            # SQLSMALLINT        cchColumnName
            # );
            SQLColumnsW = odbc32.SQLColumnsW
            SQLColumnsW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetConnectOptionW(
            # SQLHDBC            hdbc,
            # SQLUSMALLINT       fOption,
            # SQLPOINTER         pvParam);
            SQLGetConnectOptionW = odbc32.SQLGetConnectOptionW
            SQLGetConnectOptionW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetInfoW(
            # SQLHDBC                     hdbc,
            # SQLUSMALLINT                fInfoType,
            # _Out_writes_bytes_opt_(cbInfoValueMax) SQLPOINTER rgbInfoValue,
            # SQLSMALLINT        cbInfoValueMax,
            # _Out_opt_
            # SQLSMALLINT*                pcbInfoValue);
            SQLGetInfoW = odbc32.SQLGetInfoW
            SQLGetInfoW.restype = SQLRETURN

            # SQLRETURN SQL_API   SQLGetTypeInfoW(
            # SQLHSTMT            StatementHandle,
            # SQLSMALLINT         DataType);
            SQLGetTypeInfoW = odbc32.SQLGetTypeInfoW
            SQLGetTypeInfoW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetConnectOptionW(
            # SQLHDBC            hdbc,
            # SQLUSMALLINT       fOption,
            # SQLULEN            vParam);
            SQLSetConnectOptionW = odbc32.SQLSetConnectOptionW
            SQLSetConnectOptionW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSpecialColumnsW
            # (
            # SQLHSTMT           hstmt,
            # SQLUSMALLINT       fColType,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchTableName) SQLWCHAR*      szTableName,
            # SQLSMALLINT        cchTableName,
            # SQLUSMALLINT       fScope,
            # SQLUSMALLINT       fNullable
            # );
            SQLSpecialColumnsW = odbc32.SQLSpecialColumnsW
            SQLSpecialColumnsW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLStatisticsW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchTableName) SQLWCHAR*      szTableName,
            # SQLSMALLINT        cchTableName,
            # SQLUSMALLINT       fUnique,
            # SQLUSMALLINT       fAccuracy
            # );
            SQLStatisticsW = odbc32.SQLStatisticsW
            SQLStatisticsW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLTablesW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchTableName) SQLWCHAR*      szTableName,
            # SQLSMALLINT        cchTableName,
            # _In_reads_opt_(cchTableType) SQLWCHAR*      szTableType,
            # SQLSMALLINT        cchTableType
            # );
            SQLTablesW = odbc32.SQLTablesW
            SQLTablesW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDataSourcesW
            # (
            # SQLHENV             henv,
            # SQLUSMALLINT        fDirection,
            # _Out_writes_opt_(cchDSNMax) SQLWCHAR* szDSN,
            # SQLSMALLINT         cchDSNMax,
            # _Out_opt_
            # SQLSMALLINT*        pcchDSN,
            # _Out_writes_opt_(cchDescriptionMax) SQLWCHAR* wszDescription,
            # SQLSMALLINT         cchDescriptionMax,
            # _Out_opt_
            # SQLSMALLINT*        pcchDescription
            # );
            SQLDataSourcesW = odbc32.SQLDataSourcesW
            SQLDataSourcesW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDriverConnectW
            # (
            # SQLHDBC             hdbc,
            # SQLHWND             hwnd,
            # _In_reads_(cchConnStrIn) SQLWCHAR* szConnStrIn,
            # SQLSMALLINT         cchConnStrIn,
            # _Out_writes_opt_(cchConnStrOutMax) SQLWCHAR* szConnStrOut,
            # SQLSMALLINT         cchConnStrOutMax,
            # _Out_opt_ SQLSMALLINT*        pcchConnStrOut,
            # SQLUSMALLINT        fDriverCompletion
            # );
            SQLDriverConnectW = odbc32.SQLDriverConnectW
            SQLDriverConnectW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLBrowseConnectW
            # (
            # SQLHDBC             hdbc,
            # _In_reads_(cchConnStrIn) SQLWCHAR* szConnStrIn,
            # SQLSMALLINT         cchConnStrIn,
            # _Out_writes_opt_(cchConnStrOutMax) SQLWCHAR* szConnStrOut,
            # SQLSMALLINT         cchConnStrOutMax,
            # _Out_opt_
            # SQLSMALLINT*        pcchConnStrOut
            # );
            SQLBrowseConnectW = odbc32.SQLBrowseConnectW
            SQLBrowseConnectW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLColumnPrivilegesW(
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchTableName) SQLWCHAR*      szTableName,
            # SQLSMALLINT        cchTableName,
            # _In_reads_opt_(cchColumnName) SQLWCHAR*     szColumnName,
            # SQLSMALLINT        cchColumnName
            # );
            SQLColumnPrivilegesW = odbc32.SQLColumnPrivilegesW
            SQLColumnPrivilegesW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetStmtAttrW(
            # SQLHSTMT           hstmt,
            # SQLINTEGER         fAttribute,
            # SQLPOINTER         rgbValue,
            # SQLINTEGER         cbValueMax,
            # SQLINTEGER     *pcbValue);
            SQLGetStmtAttrW = odbc32.SQLGetStmtAttrW
            SQLGetStmtAttrW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetStmtAttrW(
            # SQLHSTMT           hstmt,
            # SQLINTEGER         fAttribute,
            # SQLPOINTER         rgbValue,
            # SQLINTEGER         cbValueMax);
            SQLSetStmtAttrW = odbc32.SQLSetStmtAttrW
            SQLSetStmtAttrW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLForeignKeysW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchPkCatalogName) SQLWCHAR*    szPkCatalogName,
            # SQLSMALLINT        cchPkCatalogName,
            # _In_reads_opt_(cchPkSchemaName) SQLWCHAR*     szPkSchemaName,
            # SQLSMALLINT        cchPkSchemaName,
            # _In_reads_opt_(cchPkTableName) SQLWCHAR*      szPkTableName,
            # SQLSMALLINT        cchPkTableName,
            # _In_reads_opt_(cchFkCatalogName) SQLWCHAR*    szFkCatalogName,
            # SQLSMALLINT        cchFkCatalogName,
            # _In_reads_opt_(cchFkSchemaName) SQLWCHAR*     szFkSchemaName,
            # SQLSMALLINT        cchFkSchemaName,
            # _In_reads_opt_(cchFkTableName) SQLWCHAR*      szFkTableName,
            # SQLSMALLINT        cchFkTableName
            # );
            SQLForeignKeysW = odbc32.SQLForeignKeysW
            SQLForeignKeysW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLNativeSqlW
            # (
            # SQLHDBC                                     hdbc,
            # _In_reads_(cchSqlStrIn) SQLWCHAR*          szSqlStrIn,
            # SQLINTEGER                                  cchSqlStrIn,
            # _Out_writes_opt_(cchSqlStrMax) SQLWCHAR*    szSqlStr,
            # SQLINTEGER                                  cchSqlStrMax,
            # SQLINTEGER*                                 pcchSqlStr
            # );
            SQLNativeSqlW = odbc32.SQLNativeSqlW
            SQLNativeSqlW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLPrimaryKeysW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchTableName) SQLWCHAR*      szTableName,
            # SQLSMALLINT        cchTableName
            # );
            SQLPrimaryKeysW = odbc32.SQLPrimaryKeysW
            SQLPrimaryKeysW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLProcedureColumnsW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchProcName) SQLWCHAR*       szProcName,
            # SQLSMALLINT        cchProcName,
            # _In_reads_opt_(cchColumnName) SQLWCHAR*     szColumnName,
            # SQLSMALLINT        cchColumnName
            # );
            SQLProcedureColumnsW = odbc32.SQLProcedureColumnsW
            SQLProcedureColumnsW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLProceduresW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchProcName) SQLWCHAR*      szProcName,
            # SQLSMALLINT        cchProcName
            # );
            SQLProceduresW = odbc32.SQLProceduresW
            SQLProceduresW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLTablePrivilegesW
            # (
            # SQLHSTMT           hstmt,
            # _In_reads_opt_(cchCatalogName) SQLWCHAR*    szCatalogName,
            # SQLSMALLINT        cchCatalogName,
            # _In_reads_opt_(cchSchemaName) SQLWCHAR*     szSchemaName,
            # SQLSMALLINT        cchSchemaName,
            # _In_reads_opt_(cchTableName) SQLWCHAR*      szTableName,
            # SQLSMALLINT        cchTableName
            # );
            SQLTablePrivilegesW = odbc32.SQLTablePrivilegesW
            SQLTablePrivilegesW.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDriversW
            # (
            # SQLHENV         henv,
            # SQLUSMALLINT    fDirection,
            # _Out_writes_opt_(cchDriverDescMax) SQLWCHAR* szDriverDesc,
            # SQLSMALLINT     cchDriverDescMax,
            # _Out_opt_
            # SQLSMALLINT*    pcchDriverDesc,
            # _Out_writes_opt_(cchDrvrAttrMax) SQLWCHAR*     szDriverAttributes,
            # SQLSMALLINT     cchDrvrAttrMax,
            # _Out_opt_
            # SQLSMALLINT*    pcchDrvrAttr
            # );
            SQLDriversW = odbc32.SQLDriversW
            SQLDriversW.restype = SQLRETURN

            # // ANSI versions
            if defined(_WIN64):
                # SQLRETURN SQL_API SQLColAttributeA(
                # SQLHSTMT        hstmt,
                # SQLSMALLINT     iCol,
                # SQLSMALLINT     iField,
                # _Out_writes_bytes_opt_(cbCharAttrMax)
                # SQLPOINTER      pCharAttr,
                # SQLSMALLINT     cbCharAttrMax,
                # _Out_opt_
                # SQLSMALLINT     *pcbCharAttr,
                # _Out_opt_
                # SQLLEN          *pNumAttr);
                SQLColAttributeA = odbc32.SQLColAttributeA
                SQLColAttributeA.restype = SQLRETURN
            else:
                # SQLRETURN SQL_API SQLColAttributeA(
                # SQLHSTMT        hstmt,
                # SQLSMALLINT     iCol,
                # SQLSMALLINT     iField,
                # _Out_writes_bytes_opt_(cbCharAttrMax)
                # SQLPOINTER      pCharAttr,
                # SQLSMALLINT     cbCharAttrMax,
                # _Out_opt_
                # SQLSMALLINT     *pcbCharAttr,
                # _Out_opt_
                # SQLPOINTER      pNumAttr);
                SQLColAttributeA = odbc32.SQLColAttributeA
                SQLColAttributeA.restype = SQLRETURN
            # END IF

            # SQLRETURN SQL_API SQLColAttributesA(
            # SQLHSTMT        hstmt,
            # SQLUSMALLINT    icol,
            # SQLUSMALLINT    fDescType,
            # _Out_writes_bytes_opt_(cbDescMax)
            # SQLPOINTER      rgbDesc,
            # SQLSMALLINT     cbDescMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbDesc,
            # _Out_opt_
            # SQLLEN          *pfDesc);
            SQLColAttributesA = odbc32.SQLColAttributesA
            SQLColAttributesA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLConnectA(
            # SQLHDBC         hdbc,
            # _In_reads_(cbDSN)
            # SQLCHAR         *szDSN,
            # SQLSMALLINT     cbDSN,
            # _In_reads_(cbUID)
            # SQLCHAR         *szUID,
            # SQLSMALLINT     cbUID,
            # _In_reads_(cbAuthStr)
            # SQLCHAR         *szAuthStr,
            # SQLSMALLINT     cbAuthStr);
            SQLConnectA = odbc32.SQLConnectA
            SQLConnectA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDescribeColA(
            # SQLHSTMT        hstmt,
            # SQLUSMALLINT    icol,
            # _Out_writes_opt_(cbColNameMax)
            # SQLCHAR         *szColName,
            # SQLSMALLINT     cbColNameMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbColName,
            # _Out_opt_
            # SQLSMALLINT     *pfSqlType,
            # _Out_opt_
            # SQLULEN         *pcbColDef,
            # _Out_opt_
            # SQLSMALLINT     *pibScale,
            # _Out_opt_
            # SQLSMALLINT     *pfNullable);
            SQLDescribeColA = odbc32.SQLDescribeColA
            SQLDescribeColA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLErrorA(
            # SQLHENV         henv,
            # SQLHDBC         hdbc,
            # SQLHSTMT        hstmt,
            # _Out_writes_(SQL_SQLSTATE_SIZE + 1)
            # SQLCHAR         *szSqlState,
            # _Out_opt_
            # SQLINTEGER      *pfNativeError,
            # _Out_writes_opt_(cbErrorMsgMax)
            # SQLCHAR         *szErrorMsg,
            # SQLSMALLINT     cbErrorMsgMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbErrorMsg);
            SQLErrorA = odbc32.SQLErrorA
            SQLErrorA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLExecDirectA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbSqlStr)
            # SQLCHAR         *szSqlStr,
            # SQLINTEGER      cbSqlStr);
            SQLExecDirectA = odbc32.SQLExecDirectA
            SQLExecDirectA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetConnectAttrA(
            # SQLHDBC         hdbc,
            # SQLINTEGER      fAttribute,
            # _Out_writes_opt_(_Inexpressible_(cbValueMax))
            # SQLPOINTER      rgbValue,
            # SQLINTEGER      cbValueMax,
            # _Out_opt_
            # SQLINTEGER      *pcbValue);
            SQLGetConnectAttrA = odbc32.SQLGetConnectAttrA
            SQLGetConnectAttrA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetCursorNameA(
            # SQLHSTMT        hstmt,
            # _Out_writes_opt_(cbCursorMax)
            # SQLCHAR         *szCursor,
            # SQLSMALLINT     cbCursorMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbCursor);
            SQLGetCursorNameA = odbc32.SQLGetCursorNameA
            SQLGetCursorNameA.restype = SQLRETURN

            if (ODBCVER >= 0x0300):
                # SQLRETURN SQL_API SQLGetDescFieldA(
                # SQLHDESC        hdesc,
                # SQLSMALLINT     iRecord,
                # SQLSMALLINT     iField,
                # _Out_writes_opt_(_Inexpressible_(cbBufferLength))
                # SQLPOINTER      rgbValue,
                # SQLINTEGER      cbBufferLength,
                # _Out_opt_
                # SQLINTEGER      *StringLength);
                SQLGetDescFieldA = odbc32.SQLGetDescFieldA
                SQLGetDescFieldA.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetDescRecA(
                # SQLHDESC        hdesc,
                # SQLSMALLINT     iRecord,
                # _Out_writes_opt_(cbNameMax)
                # SQLCHAR         *szName,
                # SQLSMALLINT     cbNameMax,
                # _Out_opt_
                # SQLSMALLINT     *pcbName,
                # _Out_opt_
                # SQLSMALLINT     *pfType,
                # _Out_opt_
                # SQLSMALLINT     *pfSubType,
                # _Out_opt_
                # SQLLEN          *pLength,
                # _Out_opt_
                # SQLSMALLINT     *pPrecision,
                # _Out_opt_
                # SQLSMALLINT     *pScale,
                # _Out_opt_
                # SQLSMALLINT     *pNullable);
                SQLGetDescRecA = odbc32.SQLGetDescRecA
                SQLGetDescRecA.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetDiagFieldA(
                # SQLSMALLINT     fHandleType,
                # SQLHANDLE       handle,
                # SQLSMALLINT     iRecord,
                # SQLSMALLINT     fDiagField,
                # _Out_writes_opt_(_Inexpressible_(cbDiagInfoMax))
                # SQLPOINTER      rgbDiagInfo,
                # SQLSMALLINT     cbDiagInfoMax,
                # _Out_opt_
                # SQLSMALLINT     *pcbDiagInfo);
                SQLGetDiagFieldA = odbc32.SQLGetDiagFieldA
                SQLGetDiagFieldA.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetDiagRecA(
                # SQLSMALLINT     fHandleType,
                # SQLHANDLE       handle,
                # SQLSMALLINT     iRecord,
                # _Out_writes_opt_(6)
                # SQLCHAR         *szSqlState,
                # SQLINTEGER      *pfNativeError,
                # _Out_writes_opt_(cbErrorMsgMax)
                # SQLCHAR         *szErrorMsg,
                # SQLSMALLINT     cbErrorMsgMax,
                # SQLSMALLINT     *pcbErrorMsg);
                SQLGetDiagRecA = odbc32.SQLGetDiagRecA
                SQLGetDiagRecA.restype = SQLRETURN

                # SQLRETURN SQL_API SQLGetStmtAttrA(
                # SQLHSTMT        hstmt,
                # SQLINTEGER      fAttribute,
                # SQLPOINTER      rgbValue,
                # SQLINTEGER      cbValueMax,
                # SQLINTEGER      *pcbValue);
                SQLGetStmtAttrA = odbc32.SQLGetStmtAttrA
                SQLGetStmtAttrA.restype = SQLRETURN
            # END IF

            # SQLRETURN SQL_API   SQLGetTypeInfoA(
            # SQLHSTMT        StatementHandle,
            # SQLSMALLINT     DataType);
            SQLGetTypeInfoA = odbc32.SQLGetTypeInfoA
            SQLGetTypeInfoA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLPrepareA(
            # SQLHSTMT        hstmt,
            # _In_reads_(cbSqlStr)
            # SQLCHAR         *szSqlStr,
            # SQLINTEGER      cbSqlStr);
            SQLPrepareA = odbc32.SQLPrepareA
            SQLPrepareA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetConnectAttrA(
            # SQLHDBC         hdbc,
            # SQLINTEGER      fAttribute,
            # _In_reads_bytes_opt_(cbValue)
            # SQLPOINTER      rgbValue,
            # SQLINTEGER      cbValue);
            SQLSetConnectAttrA = odbc32.SQLSetConnectAttrA
            SQLSetConnectAttrA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetCursorNameA(
            # SQLHSTMT        hstmt,
            # _In_reads_(cbCursor)
            # SQLCHAR         *szCursor,
            # SQLSMALLINT     cbCursor);
            SQLSetCursorNameA = odbc32.SQLSetCursorNameA
            SQLSetCursorNameA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLColumnsA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbTableName)
            # SQLCHAR         *szTableName,
            # SQLSMALLINT     cbTableName,
            # _In_reads_opt_(cbColumnName)
            # SQLCHAR         *szColumnName,
            # SQLSMALLINT     cbColumnName);
            SQLColumnsA = odbc32.SQLColumnsA
            SQLColumnsA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetConnectOptionA(
            # SQLHDBC         hdbc,
            # SQLUSMALLINT    fOption,
            # SQLPOINTER      pvParam);
            SQLGetConnectOptionA = odbc32.SQLGetConnectOptionA
            SQLGetConnectOptionA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetInfoA(
            # SQLHDBC         hdbc,
            # SQLUSMALLINT    fInfoType,
            # _Out_writes_bytes_opt_(cbInfoValueMax)
            # SQLPOINTER      rgbInfoValue,
            # SQLSMALLINT     cbInfoValueMax,
            # _Out_opt_
            # SQLSMALLINT*    pcbInfoValue);
            SQLGetInfoA = odbc32.SQLGetInfoA
            SQLGetInfoA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLGetStmtOptionA(
            # SQLHSTMT        hstmt,
            # SQLUSMALLINT    fOption,
            # SQLPOINTER      pvParam);
            SQLGetStmtOptionA = odbc32.SQLGetStmtOptionA
            SQLGetStmtOptionA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetConnectOptionA(
            # SQLHDBC         hdbc,
            # SQLUSMALLINT    fOption,
            # SQLULEN         vParam);
            SQLSetConnectOptionA = odbc32.SQLSetConnectOptionA
            SQLSetConnectOptionA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSetStmtOptionA(
            # SQLHSTMT        hstmt,
            # SQLUSMALLINT    fOption,
            # SQLULEN         vParam);
            SQLSetStmtOptionA = odbc32.SQLSetStmtOptionA
            SQLSetStmtOptionA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLSpecialColumnsA(
            # SQLHSTMT        hstmt,
            # SQLUSMALLINT    fColType,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbTableName)
            # SQLCHAR         *szTableName,
            # SQLSMALLINT     cbTableName,
            # SQLUSMALLINT    fScope,
            # SQLUSMALLINT    fNullable);
            SQLSpecialColumnsA = odbc32.SQLSpecialColumnsA
            SQLSpecialColumnsA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLStatisticsA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbTableName)
            # SQLCHAR         *szTableName,
            # SQLSMALLINT     cbTableName,
            # SQLUSMALLINT    fUnique,
            # SQLUSMALLINT    fAccuracy);
            SQLStatisticsA = odbc32.SQLStatisticsA
            SQLStatisticsA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLTablesA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbTableName)
            # SQLCHAR         *szTableName,
            # SQLSMALLINT     cbTableName,
            # _In_reads_opt_(cbTableType)
            # SQLCHAR         *szTableType,
            # SQLSMALLINT     cbTableType);
            SQLTablesA = odbc32.SQLTablesA
            SQLTablesA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDataSourcesA(
            # SQLHENV         henv,
            # SQLUSMALLINT    fDirection,
            # _Out_writes_opt_(cbDSNMax)
            # SQLCHAR         *szDSN,
            # SQLSMALLINT     cbDSNMax,
            # SQLSMALLINT     *pcbDSN,
            # _Out_writes_opt_(cbDescriptionMax)
            # SQLCHAR         *szDescription,
            # SQLSMALLINT     cbDescriptionMax,
            # SQLSMALLINT     *pcbDescription);
            SQLDataSourcesA = odbc32.SQLDataSourcesA
            SQLDataSourcesA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDriverConnectA(
            # SQLHDBC         hdbc,
            # SQLHWND         hwnd,
            # _In_reads_(cbConnStrIn)
            # SQLCHAR         *szConnStrIn,
            # SQLSMALLINT     cbConnStrIn,
            # _Out_writes_opt_(cbConnStrOutMax)
            # SQLCHAR         *szConnStrOut,
            # SQLSMALLINT     cbConnStrOutMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbConnStrOut,
            # SQLUSMALLINT    fDriverCompletion);
            SQLDriverConnectA = odbc32.SQLDriverConnectA
            SQLDriverConnectA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLBrowseConnectA(
            # SQLHDBC         hdbc,
            # _In_reads_(cbConnStrIn)
            # SQLCHAR         *szConnStrIn,
            # SQLSMALLINT     cbConnStrIn,
            # _Out_writes_opt_(cbConnStrOutMax)
            # SQLCHAR         *szConnStrOut,
            # SQLSMALLINT     cbConnStrOutMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbConnStrOut);
            SQLBrowseConnectA = odbc32.SQLBrowseConnectA
            SQLBrowseConnectA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLColumnPrivilegesA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbTableName)
            # SQLCHAR         *szTableName,
            # SQLSMALLINT     cbTableName,
            # _In_reads_opt_(cbColumnName)
            # SQLCHAR         *szColumnName,
            # SQLSMALLINT     cbColumnName);
            SQLColumnPrivilegesA = odbc32.SQLColumnPrivilegesA
            SQLColumnPrivilegesA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDescribeParamA(
            # SQLHSTMT        hstmt,
            # SQLUSMALLINT    ipar,
            # _Out_opt_
            # SQLSMALLINT     *pfSqlType,
            # _Out_opt_
            # SQLUINTEGER     *pcbParamDef,
            # _Out_opt_
            # SQLSMALLINT     *pibScale,
            # _Out_opt_
            # SQLSMALLINT     *pfNullable);
            SQLDescribeParamA = odbc32.SQLDescribeParamA
            SQLDescribeParamA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLForeignKeysA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbPkCatalogName)
            # SQLCHAR         *szPkCatalogName,
            # SQLSMALLINT     cbPkCatalogName,
            # _In_reads_opt_(cbPkSchemaName)
            # SQLCHAR         *szPkSchemaName,
            # SQLSMALLINT     cbPkSchemaName,
            # _In_reads_opt_(cbPkTableName)
            # SQLCHAR         *szPkTableName,
            # SQLSMALLINT     cbPkTableName,
            # _In_reads_opt_(cbFkCatalogName)
            # SQLCHAR         *szFkCatalogName,
            # SQLSMALLINT     cbFkCatalogName,
            # _In_reads_opt_(cbFkSchemaName)
            # SQLCHAR         *szFkSchemaName,
            # SQLSMALLINT     cbFkSchemaName,
            # _In_reads_opt_(cbFkTableName)
            # SQLCHAR         *szFkTableName,
            # SQLSMALLINT     cbFkTableName);
            SQLForeignKeysA = odbc32.SQLForeignKeysA
            SQLForeignKeysA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLNativeSqlA(
            # SQLHDBC         hdbc,
            # _In_reads_(cbSqlStrIn)
            # SQLCHAR         *szSqlStrIn,
            # SQLINTEGER      cbSqlStrIn,
            # _Out_writes_opt_(cbSqlStrMax)
            # SQLCHAR         *szSqlStr,
            # SQLINTEGER      cbSqlStrMax,
            # SQLINTEGER      *pcbSqlStr);
            SQLNativeSqlA = odbc32.SQLNativeSqlA
            SQLNativeSqlA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLPrimaryKeysA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbTableName)
            # SQLCHAR         *szTableName,
            # SQLSMALLINT     cbTableName);
            SQLPrimaryKeysA = odbc32.SQLPrimaryKeysA
            SQLPrimaryKeysA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLProcedureColumnsA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbProcName)
            # SQLCHAR         *szProcName,
            # SQLSMALLINT     cbProcName,
            # _In_reads_opt_(cbColumnName)
            # SQLCHAR         *szColumnName,
            # SQLSMALLINT     cbColumnName);
            SQLProcedureColumnsA = odbc32.SQLProcedureColumnsA
            SQLProcedureColumnsA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLProceduresA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbProcName)
            # SQLCHAR         *szProcName,
            # SQLSMALLINT     cbProcName);
            SQLProceduresA = odbc32.SQLProceduresA
            SQLProceduresA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLTablePrivilegesA(
            # SQLHSTMT        hstmt,
            # _In_reads_opt_(cbCatalogName)
            # SQLCHAR         *szCatalogName,
            # SQLSMALLINT     cbCatalogName,
            # _In_reads_opt_(cbSchemaName)
            # SQLCHAR         *szSchemaName,
            # SQLSMALLINT     cbSchemaName,
            # _In_reads_opt_(cbTableName)
            # SQLCHAR         *szTableName,
            # SQLSMALLINT     cbTableName);
            SQLTablePrivilegesA = odbc32.SQLTablePrivilegesA
            SQLTablePrivilegesA.restype = SQLRETURN

            # SQLRETURN SQL_API SQLDriversA(
            # SQLHENV         henv,
            # SQLUSMALLINT    fDirection,
            # _Out_writes_opt_(cbDriverDescMax)
            # SQLCHAR         *szDriverDesc,
            # SQLSMALLINT     cbDriverDescMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbDriverDesc,
            # _Out_writes_opt_(cbDrvrAttrMax)
            # SQLCHAR         *szDriverAttributes,
            # SQLSMALLINT     cbDrvrAttrMax,
            # _Out_opt_
            # SQLSMALLINT     *pcbDrvrAttr);
            SQLDriversA = odbc32.SQLDriversA
            SQLDriversA.restype = SQLRETURN

            # ---------------------------------------------
            # Mapping macros for Unicode
            # ---------------------------------------------
            if not defined(SQL_NOUNICODEMAP):
                if defined(UNICODE):
                    SQLColAttribute = SQLColAttributeW
                    SQLColAttributes = SQLColAttributesW
                    SQLConnect = SQLConnectW
                    SQLDescribeCol = SQLDescribeColW
                    SQLError = SQLErrorW
                    SQLExecDirect = SQLExecDirectW
                    SQLGetConnectAttr = SQLGetConnectAttrW
                    SQLGetCursorName = SQLGetCursorNameW
                    SQLPrepare = SQLPrepareW
                    SQLSetConnectAttr = SQLSetConnectAttrW
                    SQLSetCursorName = SQLSetCursorNameW
                    SQLSetStmtAttr = SQLSetStmtAttrW
                    SQLGetStmtAttr = SQLGetStmtAttrW
                    SQLColumns = SQLColumnsW
                    SQLGetConnectOption = SQLGetConnectOptionW
                    SQLGetInfo = SQLGetInfoW
                    SQLGetTypeInfo = SQLGetTypeInfoW
                    SQLSetConnectOption = SQLSetConnectOptionW
                    SQLSpecialColumns = SQLSpecialColumnsW
                    SQLStatistics = SQLStatisticsW
                    SQLTables = SQLTablesW
                    SQLDataSources = SQLDataSourcesW
                    SQLDriverConnect = SQLDriverConnectW
                    SQLBrowseConnect = SQLBrowseConnectW
                    SQLColumnPrivileges = SQLColumnPrivilegesW
                    SQLForeignKeys = SQLForeignKeysW
                    SQLNativeSql = SQLNativeSqlW
                    SQLPrimaryKeys = SQLPrimaryKeysW
                    SQLProcedureColumns = SQLProcedureColumnsW
                    SQLProcedures = SQLProceduresW
                    SQLTablePrivileges = SQLTablePrivilegesW
                    SQLDrivers = SQLDriversW
                # END IF  UNICODE
            # END IF  SQL_NOUNICODEMAP
        # END IF  RC_INVOKED

        if defined(__cplusplus):
            # End of extern "C" {
            pass
    #  END IF  __cplusplus
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  #ifndef __SQLUCODE
