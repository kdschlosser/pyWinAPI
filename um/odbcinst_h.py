import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__ODBCINST_H = None
__SQL = None
ODBCVER = None
EXPORT = None
SQL_NOUNICODEMAP = None

# ******************************************************          * Copyright
# (C) Microsoft. All rights reserved. *  *
# *****************************************************
# -----------------------------------------------------------------------------
# File:  odbcinst.h
# Contents:  Prototypes for ODBCCP32.DLL
# Comments:
# -----------------------------------------------------------------------------
if not defined(__ODBCINST_H):
    __ODBCINST_H = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__SQL):
            from pyWinAPI.um.sql_h import * # NOQA
        # END IF

        if defined(__cplusplus):
            # Assume C declarations for C + +
            pass
        # END IF   __cplusplus
        if not defined(ODBCVER):
            ODBCVER = 0x0380            # Default to ODBC 3.80
        # END IF

        if not defined(WINVER):
            WINVER = 0x0400            # Assume Windows 4.0
        # END IF

        # Constants
        # ---------------------------------------------------------------
        # SQLConfigDataSource request flags
        ODBC_ADD_DSN = 1        # Add data source
        ODBC_CONFIG_DSN = 2        # Configure (edit) data source
        ODBC_REMOVE_DSN = 3        # Remove data source
        if ODBCVER >= 0x0250:
            ODBC_ADD_SYS_DSN = 4            # add a system DSN
            ODBC_CONFIG_SYS_DSN = 5            # Configure a system DSN
            ODBC_REMOVE_SYS_DSN = 6            # remove a system DSN
            if ODBCVER >= 0x0300:
                ODBC_REMOVE_DEFAULT_DSN = 7                # remove the default DSN
            # END IF  ODBCVER >= 0x0300

            # install request flags
            ODBC_INSTALL_INQUIRY = 1
            ODBC_INSTALL_COMPLETE = 2

            # config driver flags
            ODBC_INSTALL_DRIVER = 1
            ODBC_REMOVE_DRIVER = 2
            ODBC_CONFIG_DRIVER = 3
            ODBC_CONFIG_DRIVER_MAX = 100
        # END IF


        # SQLGetConfigMode and SQLSetConfigMode flags
        if ODBCVER >= 0x0300:
            ODBC_BOTH_DSN = 0
            ODBC_USER_DSN = 1
            ODBC_SYSTEM_DSN = 2
        # END IF  ODBCVER >= 0x0300

        # SQLInstallerError code
        if ODBCVER >= 0x0300:
            ODBC_ERROR_GENERAL_ERR = 1
            ODBC_ERROR_INVALID_BUFF_LEN = 2
            ODBC_ERROR_INVALID_HWND = 3
            ODBC_ERROR_INVALID_STR = 4
            ODBC_ERROR_INVALID_REQUEST_TYPE = 5
            ODBC_ERROR_COMPONENT_NOT_FOUND = 6
            ODBC_ERROR_INVALID_NAME = 7
            ODBC_ERROR_INVALID_KEYWORD_VALUE = 8
            ODBC_ERROR_INVALID_DSN = 9
            ODBC_ERROR_INVALID_INF = 10
            ODBC_ERROR_REQUEST_FAILED = 11
            ODBC_ERROR_INVALID_PATH = 12
            ODBC_ERROR_LOAD_LIB_FAILED = 13
            ODBC_ERROR_INVALID_PARAM_SEQUENCE = 14
            ODBC_ERROR_INVALID_LOG_FILE = 15
            ODBC_ERROR_USER_CANCELED = 16
            ODBC_ERROR_USAGE_UPDATE_FAILED = 17
            ODBC_ERROR_CREATE_DSN_FAILED = 18
            ODBC_ERROR_WRITING_SYSINFO_FAILED = 19
            ODBC_ERROR_REMOVE_DSN_FAILED = 20
            ODBC_ERROR_OUT_OF_MEM = 21
            ODBC_ERROR_OUTPUT_STRING_TRUNCATED = 22
            ODBC_ERROR_NOTRANINFO = 23
            ODBC_ERROR_MAX = ODBC_ERROR_NOTRANINFO            # update this when we add new error message
        # END IF  ODBCVER >= 0x0300

        if not defined(EXPORT):
            EXPORT = VOID
        # END IF


        if not defined(RC_INVOKED):
            # Prototypes
            # --------------------------------------------------------------
            INSTAPI = VOID

            # High level APIs
            # Low level APIs
            # NOTE: The high-level APIs should always be used. These APIs
            # have been left for compatibility.
            odbccp32 = ctypes.windll.ODBCCP32

            #
            # High level APIs
            # __declspec(deprecated("ODBC Installer API: SQLInstallODBC is no-op."))
            # BOOL INSTAPI SQLInstallODBC          (_Reserved_ HWND,
            # _Reserved_ LPCSTR,
            # _Reserved_ LPCSTR,
            # _Reserved_ LPCSTR);
            SQLInstallODBC = (
                odbccp32.SQLInstallODBC
            )
            SQLInstallODBC.restype = BOOL

            #
            # BOOL INSTAPI SQLManageDataSources    (HWND       hwndParent);
            SQLManageDataSources = (
                odbccp32.SQLManageDataSources
            )
            SQLManageDataSources.restype = BOOL

            # BOOL INSTAPI SQLCreateDataSource     (HWND       hwndParent,
            # LPCSTR     lpszDSN);
            SQLCreateDataSource = (
                odbccp32.SQLCreateDataSource
            )
            SQLCreateDataSource.restype = BOOL

            #
            # _Success_(return)
            # BOOL INSTAPI SQLGetTranslator
            # (
            # HWND    hwnd,
            # _Inout_updates_(cchNameMax) LPSTR lpszName,
            # WORD     cchNameMax,
            # WORD*    pcchNameOut,
            # _Out_writes_(cchPathMax) LPSTR lpszPath,
            # WORD     cchPathMax,
            # WORD*    pcchPathOut,
            # DWORD*   pvOption
            # );
            SQLGetTranslator = (
                odbccp32.SQLGetTranslator
            )
            SQLGetTranslator.restype = BOOL

            #
            # Low level APIs
            # NOTE: The high-level APIs should always be used. These APIs
            # have been left for compatibility.
            # _Success_(return)
            # BOOL INSTAPI SQLInstallDriver
            # (
            # LPCSTR     lpszInfFile,
            # LPCSTR     lpszDriver,
            # _Out_writes_opt_(cchPathMax) LPSTR lpszPath,
            # WORD       cchPathMax,
            # WORD*      pcchPathOut
            # );
            SQLInstallDriver = (
                odbccp32.SQLInstallDriver
            )
            SQLInstallDriver.restype = BOOL

            #
            # BOOL INSTAPI SQLInstallDriverManager
            # (
            # _Inout_updates_(cchPathMax) LPSTR  lpszPath,
            # WORD       cchPathMax,
            # WORD*      pcchPathOut
            # );
            SQLInstallDriverManager = (
                odbccp32.SQLInstallDriverManager
            )
            SQLInstallDriverManager.restype = BOOL

            #
            # _Success_(return)
            # BOOL INSTAPI SQLGetInstalledDrivers
            # (
            # _Out_writes_(cchBufMax) LPSTR lpszBuf,
            # WORD  cchBufMax,
            # WORD* pcchBufOut
            # );
            SQLGetInstalledDrivers = (
                odbccp32.SQLGetInstalledDrivers
            )
            SQLGetInstalledDrivers.restype = BOOL

            #
            # __declspec(deprecated("ODBC API: SQLGetAvailableDrivers is a no-op."))
            # BOOL INSTAPI SQLGetAvailableDrivers
            # (
            # _Reserved_ LPCSTR,
            # _Reserved_ LPSTR,
            # _Reserved_ WORD,
            # _Reserved_ WORD*
            # );
            SQLGetAvailableDrivers = (
                odbccp32.SQLGetAvailableDrivers
            )
            SQLGetAvailableDrivers.restype = BOOL

            #
            # BOOL INSTAPI SQLConfigDataSource     (HWND       hwndParent,
            # WORD       fRequest,
            # LPCSTR     lpszDriver,
            # LPCSTR     lpszAttributes);
            SQLConfigDataSource = (
                odbccp32.SQLConfigDataSource
            )
            SQLConfigDataSource.restype = BOOL

            # BOOL INSTAPI SQLRemoveDefaultDataSource(void);
            SQLRemoveDefaultDataSource = (
                odbccp32.SQLRemoveDefaultDataSource
            )
            SQLRemoveDefaultDataSource.restype = BOOL

            # BOOL INSTAPI SQLWriteDSNToIni        (LPCSTR     lpszDSN,
            # LPCSTR     lpszDriver);
            SQLWriteDSNToIni = (
                odbccp32.SQLWriteDSNToIni
            )
            SQLWriteDSNToIni.restype = BOOL

            # BOOL INSTAPI SQLRemoveDSNFromIni     (LPCSTR     lpszDSN);
            SQLRemoveDSNFromIni = (
                odbccp32.SQLRemoveDSNFromIni
            )
            SQLRemoveDSNFromIni.restype = BOOL

            # BOOL INSTAPI SQLValidDSN             (LPCSTR     lpszDSN);
            SQLValidDSN = (
                odbccp32.SQLValidDSN
            )
            SQLValidDSN.restype = BOOL

            # BOOL INSTAPI SQLWritePrivateProfileString(LPCSTR lpszSection,
            # LPCSTR lpszEntry,
            # LPCSTR lpszString,
            # LPCSTR lpszFilename);
            SQLWritePrivateProfileString = (
                odbccp32.SQLWritePrivateProfileString
            )
            SQLWritePrivateProfileString.restype = BOOL

            # _Success_(return != 0)
            # int  INSTAPI SQLGetPrivateProfileString
            # (
            # LPCSTR lpszSection,
            # LPCSTR lpszEntry,
            # LPCSTR lpszDefault,
            # _Out_writes_opt_(cchRetBuffer) LPSTR lpszRetBuffer,
            # int    cchRetBuffer,
            # LPCSTR lpszFilename
            # );
            SQLGetPrivateProfileString = (
                odbccp32.SQLGetPrivateProfileString
            )
            SQLGetPrivateProfileString.restype = BOOL

            if ODBCVER >= 0x0250:
                # BOOL INSTAPI SQLRemoveDriverManager(LPDWORD lpdwUsageCount);
                SQLRemoveDriverManager = (
                    odbccp32.SQLRemoveDriverManager
                )
                SQLRemoveDriverManager.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI SQLInstallTranslator
                # (
                # LPCSTR  lpszInfFile,
                # LPCSTR  lpszTranslator,
                # LPCSTR  lpszPathIn,
                # _Out_writes_(cchPathOutMax) LPSTR  lpszPathOut,
                # WORD    cchPathOutMax,
                # WORD*   pcchPathOut,
                # WORD    fRequest,
                # LPDWORD lpdwUsageCount
                # );
                SQLInstallTranslator = (
                    odbccp32.SQLInstallTranslator
                )
                SQLInstallTranslator.restype = BOOL

                # BOOL INSTAPI SQLRemoveTranslator(LPCSTR lpszTranslator,
                # LPDWORD lpdwUsageCount);
                # BOOL INSTAPI SQLRemoveDriver(LPCSTR lpszDriver,
                # BOOL fRemoveDSN,
                # LPDWORD lpdwUsageCount);
                SQLRemoveTranslator = (
                    odbccp32.SQLRemoveTranslator
                )
                SQLRemoveTranslator.restype = BOOL

                # _Succs_(return)
                # BOOL INSTAPI SQLConfigDriver
                # (
                # HWND    hwndParent,
                # WORD    fRequest,
                # LPCSTR  lpszDriver,
                # LPCSTR  lpszArgs,
                # _Out_writes_(cchMsgMax) LPSTR lpszMsg,
                # WORD    cchMsgMax,
                # WORD*   pcchMsgOut
                # );
                SQLConfigDriver = (
                    odbccp32.SQLConfigDriver
                )
                SQLConfigDriver.restype = BOOL

            # END IF

            if ODBCVER >=  0x0300:
                # _Success_(return==0 ||return==1)
                # SQLRETURN INSTAPI SQLInstallerError
                # (
                # WORD    iError,
                # DWORD*  pfErrorCode,
                # _Out_writes_opt_(cchErrorMsgMax) LPSTR lpszErrorMsg,
                # WORD    cchErrorMsgMax,
                # WORD*   pcchErrorMsg
                # );
                SQLInstallerError = (
                    odbccp32.SQLInstallerError
                )
                SQLInstallerError.restype = INSTAPI

                # SQLRETURN INSTAPI SQLPostInstallerError(DWORD dwErrorCode, LPCSTR lpszErrMsg);
                SQLPostInstallerError = (
                    odbccp32.SQLPostInstallerError
                )
                SQLPostInstallerError.restype = INSTAPI

                # BOOL INSTAPI SQLWriteFileDSN(LPCSTR  lpszFileName,
                # LPCSTR  lpszAppName,
                # LPCSTR  lpszKeyName,
                # LPCSTR  lpszString);
                SQLWriteFileDSN = (
                    odbccp32.SQLWriteFileDSN
                )
                SQLWriteFileDSN.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI  SQLReadFileDSN
                # (
                # LPCSTR  lpszFileName,
                # LPCSTR  lpszAppName,
                # LPCSTR  lpszKeyName,
                # _Out_writes_(cchString) LPSTR lpszString,
                # WORD    cchString,
                # WORD*   pcchString
                # );
                SQLReadFileDSN = (
                    odbccp32.SQLReadFileDSN
                )
                SQLReadFileDSN.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI SQLInstallDriverEx
                # (
                # LPCSTR      lpszDriver,
                # LPCSTR      lpszPathIn,
                # _Out_writes_(cchPathOutMax) LPSTR lpszPathOut,
                # WORD        cchPathOutMax,
                # WORD*       pcchPathOut,
                # WORD        fRequest,
                # LPDWORD     lpdwUsageCount
                # );
                SQLInstallDriverEx = (
                    odbccp32.SQLInstallDriverEx
                )
                SQLInstallDriverEx.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI SQLInstallTranslatorEx
                # (
                # LPCSTR  lpszTranslator,
                # LPCSTR  lpszPathIn,
                # _Out_writes_(cchPathOutMax) LPSTR  lpszPathOut,
                # WORD    cchPathOutMax,
                # WORD*   pcchPathOut,
                # WORD    fRequest,
                # LPDWORD lpdwUsageCount
                # );
                SQLInstallTranslatorEx = (
                    odbccp32.SQLInstallTranslatorEx
                )
                SQLInstallTranslatorEx.restype = BOOL

                # BOOL INSTAPI SQLGetConfigMode(UWORD *pwConfigMode);
                SQLGetConfigMode = (
                    odbccp32.SQLGetConfigMode
                )
                SQLGetConfigMode.restype = BOOL

                # BOOL INSTAPI SQLSetConfigMode(UWORD wConfigMode);
                SQLSetConfigMode = (
                    odbccp32.SQLSetConfigMode
                )
                SQLSetConfigMode.restype = BOOL

            # END IF  ODBCVER >= 0x0300

            # Driver specific Setup APIs called by installer

            # BOOL INSTAPI ConfigDSN (HWND    hwndParent,
            # WORD    fRequest,
            # LPCSTR  lpszDriver,
            # LPCSTR  lpszAttributes);
            ConfigDSN = (
                odbccp32.ConfigDSN
            )
            ConfigDSN.restype = BOOL

            # BOOL INSTAPI ConfigTranslator ( HWND        hwndParent,
            # DWORD       *pvOption);
            ConfigTranslator = (
                odbccp32.ConfigTranslator
            )
            ConfigTranslator.restype = BOOL

            if ODBCVER >= 0x0250:
                # BOOL INSTAPI ConfigDriver
                # (
                # HWND    hwndParent,
                # WORD    fRequest,
                # LPCSTR  lpszDriver,
                # LPCSTR  lpszArgs,
                # _Out_writes_(cchMsgMax) LPSTR  lpszMsg,
                # WORD    cchMsgMax,
                # WORD*   pcchMsgOut
                # );
                ConfigDriver = (
                    odbccp32.ConfigDriver
                )
                ConfigDriver.restype = BOOL
            # END IF

            # UNICODE APIs
            # High level APIs
            # __declspec(deprecated("ODBC API: SQLInstallODBCW is a no-op."))
            # BOOL INSTAPI SQLInstallODBCW         (_Reserved_ HWND,
            # _Reserved_ LPCWSTR,
            # _Reserved_ LPCWSTR,
            # _Reserved_ LPCWSTR);
            SQLInstallODBCW = (
                odbccp32.SQLInstallODBCW
            )
            SQLInstallODBCW.restype = BOOL

            # BOOL INSTAPI SQLCreateDataSourceW     (HWND       hwndParent,
            # LPCWSTR     lpszDSN);
            SQLCreateDataSourceW = (
                odbccp32.SQLCreateDataSourceW
            )
            SQLCreateDataSourceW.restype = BOOL

            # _Success_(return)
            # BOOL INSTAPI SQLGetTranslatorW
            # (
            # HWND    hwnd,
            # _Out_writes_to_opt_(cchNameMax, *pcchNameOut) LPWSTR lpszName,
            # WORD     cchNameMax,
            # WORD*    pcchNameOut,
            # _Out_writes_to_opt_(cchPathMax, *pcchPathOut) LPWSTR lpszPath,
            # WORD     cchPathMax,
            # WORD*    pcchPathOut,
            # DWORD*   pvOption
            # );
            SQLGetTranslatorW = (
                odbccp32.SQLGetTranslatorW
            )
            SQLGetTranslatorW.restype = BOOL

            # Low level APIs
            # NOTE: The high-level APIs should always be used. These APIs
            # have been left for compatibility.
            #
            # _Success_(return)
            # BOOL INSTAPI SQLInstallDriverW
            # (
            # LPCWSTR     lpszInfFile,
            # LPCWSTR     lpszDriver,
            # _Out_writes_(cchPathMax) LPWSTR lpszPath,
            # WORD       cchPathMax,
            # WORD*      pcchPathOut
            # );
            SQLInstallDriverW = (
                odbccp32.SQLInstallDriverW
            )
            SQLInstallDriverW.restype = BOOL

            # BOOL INSTAPI SQLInstallDriverManagerW
            # (
            # _Inout_updates_(cchPathMax) LPWSTR lpszPath,
            # WORD       cchPathMax,
            # WORD*      pcchPathOut
            # );
            SQLInstallDriverManagerW = (
                odbccp32.SQLInstallDriverManagerW
            )
            SQLInstallDriverManagerW.restype = BOOL

            # _Success_(return)
            # BOOL INSTAPI SQLGetInstalledDriversW
            # (
            # _Out_writes_(cchBufMax) LPWSTR lpszBuf,
            # WORD  cchBufMax,
            # WORD* pcchBufOut
            # );
            SQLGetInstalledDriversW = (
                odbccp32.SQLGetInstalledDriversW
            )
            SQLGetInstalledDriversW.restype = BOOL

            # __declspec(deprecated("ODBC API: SQLGetAvailableDriversW is a no-op."))
            # BOOL INSTAPI SQLGetAvailableDriversW
            # (
            # _Reserved_ LPCWSTR,
            # _Reserved_ LPWSTR,
            # _Reserved_ WORD,
            # _Reserved_ WORD*
            # );
            SQLGetAvailableDriversW = (
                odbccp32.SQLGetAvailableDriversW
            )
            SQLGetAvailableDriversW.restype = BOOL

            # BOOL INSTAPI SQLConfigDataSourceW     (HWND       hwndParent,
            # WORD       fRequest,
            # LPCWSTR     lpszDriver,
            # LPCWSTR     lpszAttributes);
            SQLConfigDataSourceW = (
                odbccp32.SQLConfigDataSourceW
            )
            SQLConfigDataSourceW.restype = BOOL

            # BOOL INSTAPI SQLWriteDSNToIniW        (LPCWSTR     lpszDSN,
            # LPCWSTR     lpszDriver);
            SQLWriteDSNToIniW = (
                odbccp32.SQLWriteDSNToIniW
            )
            SQLWriteDSNToIniW.restype = BOOL

            # BOOL INSTAPI SQLRemoveDSNFromIniW     (LPCWSTR     lpszDSN);
            SQLRemoveDSNFromIniW = (
                odbccp32.SQLRemoveDSNFromIniW
            )
            SQLRemoveDSNFromIniW.restype = BOOL

            # BOOL INSTAPI SQLValidDSNW             (LPCWSTR     lpszDSN);
            SQLValidDSNW = (
                odbccp32.SQLValidDSNW
            )
            SQLValidDSNW.restype = BOOL

            # BOOL INSTAPI SQLWritePrivateProfileStringW(LPCWSTR lpszSection,
            # LPCWSTR lpszEntry,
            # LPCWSTR lpszString,
            # LPCWSTR lpszFilename);
            SQLWritePrivateProfileStringW = (
                odbccp32.SQLWritePrivateProfileStringW
            )
            SQLWritePrivateProfileStringW.restype = BOOL

            # _Success_(return != 0)
            # int  INSTAPI SQLGetPrivateProfileStringW
            # (
            # _In_opt_ LPCWSTR lpszSection,
            # _In_opt_ LPCWSTR lpszEntry,
            # _In_opt_ LPCWSTR lpszDefault,
            # _Out_writes_opt_(cchRetBuffer) LPWSTR lpszRetBuffer,
            # int              cchRetBuffer,
            # _In_opt_ LPCWSTR lpszFilename
            # );
            SQLGetPrivateProfileStringW = (
                odbccp32.SQLGetPrivateProfileStringW
            )
            SQLGetPrivateProfileStringW.restype = BOOL


            if ODBCVER >= 0x0250:
                # _Success_(return)
                # BOOL INSTAPI SQLInstallTranslatorW
                # (
                # LPCWSTR  lpszInfFile,
                # LPCWSTR  lpszTranslator,
                # LPCWSTR  lpszPathIn,
                # _Out_writes_(cchPathOutMax) LPWSTR  lpszPathOut,
                # WORD     cchPathOutMax,
                # WORD*    pcchPathOut,
                # WORD     fRequest,
                # LPDWORD  lpdwUsageCount
                # );
                SQLInstallTranslatorW = (
                    odbccp32.SQLInstallTranslatorW
                )
                SQLInstallTranslatorW.restype = BOOL

                # BOOL INSTAPI SQLRemoveTranslatorW(LPCWSTR lpszTranslator,
                # LPDWORD lpdwUsageCount);
                SQLRemoveTranslatorW = (
                    odbccp32.SQLRemoveTranslatorW
                )
                SQLRemoveTranslatorW.restype = BOOL

                # BOOL INSTAPI SQLRemoveDriverW(LPCWSTR lpszDriver,
                # BOOL fRemoveDSN,
                # LPDWORD lpdwUsageCount);
                SQLRemoveDriverW = (
                    odbccp32.SQLRemoveDriverW
                )
                SQLRemoveDriverW.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI SQLConfigDriverW
                # (
                # HWND    hwndParent,
                # WORD    fRequest,
                # LPCWSTR lpszDriver,
                # LPCWSTR lpszArgs,
                # _Out_writes_(cchMsgMax) LPWSTR lpszMsg,
                # WORD    cchMsgMax,
                # WORD*   pcchMsgOut
                # );
                SQLConfigDriverW = (
                    odbccp32.SQLConfigDriverW
                )
                SQLConfigDriverW.restype = BOOL

                if not defined(SQL_NOUNICODEMAP):
                    if defined(UNICODE):
                        SQLInstallTranslator = SQLInstallTranslatorW
                        SQLRemoveTranslator = SQLRemoveTranslatorW
                        SQLRemoveDriver = SQLRemoveDriverW
                        SQLConfigDriver = SQLConfigDriverW

            # END IF

            if ODBCVER >= 0x0300:
                # _Success_(return==0 ||return==1)
                # SQLRETURN INSTAPI SQLInstallerErrorW
                # (
                # WORD    iError,
                # DWORD*  pfErrorCode,
                # _Out_writes_opt_(cchErrorMsgMax) LPWSTR lpszErrorMsg,
                # WORD    cchErrorMsgMax,
                # WORD*   pcchErrorMsg
                # );
                SQLInstallerErrorW = (
                    odbccp32.SQLInstallerErrorW
                )
                SQLInstallerErrorW.restype = INSTAPI

                # SQLRETURN INSTAPI   SQLPostInstallerErrorW(DWORD dwErrorCode,
                # LPCWSTR lpszErrorMsg);
                SQLPostInstallerErrorW = (
                    odbccp32.SQLPostInstallerErrorW
                )
                SQLPostInstallerErrorW.restype = INSTAPI

                # BOOL INSTAPI SQLWriteFileDSNW(LPCWSTR  lpszFileName,
                # LPCWSTR  lpszAppName,
                # LPCWSTR  lpszKeyName,
                # LPCWSTR  lpszString);
                SQLWriteFileDSNW = (
                    odbccp32.SQLWriteFileDSNW
                )
                SQLWriteFileDSNW.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI  SQLReadFileDSNW
                # (
                # LPCWSTR  lpszFileName,
                # LPCWSTR  lpszAppName,
                # LPCWSTR  lpszKeyName,
                # _Out_writes_(cchString) LPWSTR lpszString,
                # WORD    cchString,
                # WORD*   pcchString
                # );
                SQLReadFileDSNW = (
                    odbccp32.SQLReadFileDSNW
                )
                SQLReadFileDSNW.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI SQLInstallDriverExW
                # (
                # LPCWSTR     lpszDriver,
                # LPCWSTR     lpszPathIn,
                # _Out_writes_(cchPathOutMax) LPWSTR lpszPathOut,
                # WORD        cchPathOutMax,
                # WORD*       pcchPathOut,
                # WORD        fRequest,
                # LPDWORD     lpdwUsageCount
                # );
                SQLInstallDriverExW = (
                    odbccp32.SQLInstallDriverExW
                )
                SQLInstallDriverExW.restype = BOOL

                # _Success_(return)
                # BOOL INSTAPI SQLInstallTranslatorExW
                # (
                # LPCWSTR  lpszTranslator,
                # LPCWSTR  lpszPathIn,
                # _Out_writes_(cchPathOutMax) LPWSTR  lpszPathOut,
                # WORD     cchPathOutMax,
                # WORD*    pcchPathOut,
                # WORD     fRequest,
                # LPDWORD  lpdwUsageCount
                # );
                SQLInstallTranslatorExW = (
                    odbccp32.SQLInstallTranslatorExW
                )
                SQLInstallTranslatorExW.restype = BOOL

                if not defined(SQL_NOUNICODEMAP):
                    if defined(UNICODE):
                        SQLInstallerError = SQLInstallerErrorW
                        SQLPostInstallerError = SQLPostInstallerErrorW
                        SQLReadFileDSN = SQLReadFileDSNW
                        SQLWriteFileDSN = SQLWriteFileDSNW
                        SQLInstallDriverEx = SQLInstallDriverExW
                        SQLInstallTranslatorEx = SQLInstallTranslatorExW

            # END IF  ODBCVER >= 0x0300

            # Driver specific Setup APIs called by installer

            # BOOL INSTAPI ConfigDSNW (HWND   hwndParent,
            # WORD    fRequest,
            # LPCWSTR lpszDriver,
            # LPCWSTR lpszAttributes);
            ConfigDSNW = (
                odbccp32.ConfigDSNW
            )
            ConfigDSNW.restype = BOOL

            if ODBCVER >= 0x0250:
                # BOOL INSTAPI ConfigDriverW
                # (
                # HWND    hwndParent,
                # WORD    fRequest,
                # LPCWSTR  lpszDriver,
                # LPCWSTR  lpszArgs,
                # _Out_writes_(cchMsgMax) LPWSTR  lpszMsg,
                # WORD    cchMsgMax,
                # WORD*   pcchMsgOut
                # );
                ConfigDriverW = (
                    odbccp32.ConfigDriverW
                )
                ConfigDriverW.restype = BOOL

            # END IF

            if not defined(SQL_NOUNICODEMAP):
                if defined(UNICODE):
                    SQLInstallODBC = SQLInstallODBCW
                    SQLCreateDataSource = SQLCreateDataSourceW
                    SQLGetTranslator = SQLGetTranslatorW
                    SQLInstallDriver = SQLInstallDriverW
                    SQLInstallDriverManager = SQLInstallDriverManagerW
                    SQLGetInstalledDrivers = SQLGetInstalledDriversW
                    SQLGetAvailableDrivers = SQLGetAvailableDriversW
                    SQLConfigDataSource = SQLConfigDataSourceW
                    SQLWriteDSNToIni = SQLWriteDSNToIniW
                    SQLRemoveDSNFromIni = SQLRemoveDSNFromIniW
                    SQLValidDSN = SQLValidDSNW
                    SQLWritePrivateProfileString = (
                        SQLWritePrivateProfileStringW
                    )
                    SQLGetPrivateProfileString = SQLGetPrivateProfileStringW

                # END IF   UNICODE
            # END IF   SQL_NOUNICODEMAP
        # END IF   RC_INVOKED

        if defined(__cplusplus):
            # End of extern "C" {
            pass
        # END IF   __cplusplus
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF   __ODBCINST_H
