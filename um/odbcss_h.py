import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__ODBCSS = None
ODBCVER = 0
MAXNUMERICLEN = None
INT = None
_LPCBYTE_DEFINED = None

class dbvarychar(ctypes.Structure):
    pass


DBVARYCHAR = dbvarychar


class dbvarybin(ctypes.Structure):
    pass


DBVARYBIN = dbvarybin


class dbmoney(ctypes.Structure):
    pass


DBMONEY = dbmoney


class dbdatetime(ctypes.Structure):
    pass


DBDATETIME = dbdatetime


class dbdatetime4(ctypes.Structure):
    pass


DBDATETIM4 = dbdatetime4


class dbnumeric(ctypes.Structure):
    pass


DBNUMERIC = dbnumeric


class sqlperf(ctypes.Structure):
    pass


SQLPERF = sqlperf


# ******************************************************          * Copyright
# (C) Microsoft. All rights reserved. *  *
# *****************************************************
# -----------------------------------------------------------------------------
# File:  odbcss.h
# Contents:
# Comments: This is the application include file for the SQL Server driver
# specific defines.
# -----------------------------------------------------------------------------
if not defined(__ODBCSS):
    __ODBCSS = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    from pyWinAPI.um.sqltypes_h import * # NOQA
    from pyWinAPI.um.sqlext_h import *  # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):

        if defined(__cplusplus):
            # Assume C declarations for C + +
            pass
        # END IF  __cplusplus

        # Useful defines
        SQL_MAX_SQLSERVERNAME = 128        # max SQL Server identifier length

        # SQLSetConnectOption/SQLSetStmtOption driver specific defines.
        # Microsoft has 1200 thru 1249 reserved for Microsoft SQL Server
        # driver usage.
        # Connection Options
        SQL_COPT_SS_BASE = 1200
        SQL_COPT_SS_REMOTE_PWD = SQL_COPT_SS_BASE + 1        # dbrpwset SQLSetConnectOption only
        SQL_COPT_SS_USE_PROC_FOR_PREP = SQL_COPT_SS_BASE + 2        # Use create proc for SQLPrepare
        SQL_COPT_SS_INTEGRATED_SECURITY = SQL_COPT_SS_BASE + 3        # Force integrated security on login
        SQL_COPT_SS_PRESERVE_CURSORS = SQL_COPT_SS_BASE + 4        # Preserve server cursors after SQLTransact
        SQL_COPT_SS_USER_DATA = SQL_COPT_SS_BASE + 5        # dbgetuserdata/dbsetuserdata
        SQL_COPT_SS_ENLIST_IN_DTC = SQL_ATTR_ENLIST_IN_DTC        # Enlist in a DTC transaction
        SQL_COPT_SS_ENLIST_IN_XA = SQL_ATTR_ENLIST_IN_XA        # Enlist in a XA transaction

        # SQL_ATTR_CONNECTION_DEAD 1209
        # (It will return current connection status, it will not go to server)
        SQL_COPT_SS_FALLBACK_CONNECT = SQL_COPT_SS_BASE + 10        # Enables FallBack connections
        SQL_COPT_SS_PERF_DATA = SQL_COPT_SS_BASE + 11        # Used to access SQL Server ODBC driver performance data
        SQL_COPT_SS_PERF_DATA_LOG = SQL_COPT_SS_BASE + 12        # Used to set the logfile name for the Performance data
        SQL_COPT_SS_PERF_QUERY_INTERVAL = SQL_COPT_SS_BASE + 13        # Used to set the query logging threshold in milliseconds.
        SQL_COPT_SS_PERF_QUERY_LOG = SQL_COPT_SS_BASE + 14        # Used to set the logfile name for saving queryies.
        SQL_COPT_SS_PERF_QUERY = SQL_COPT_SS_BASE + 15        # Used to start and stop query logging.
        SQL_COPT_SS_PERF_DATA_LOG_NOW = SQL_COPT_SS_BASE + 16        # Used to make a statistics log entry to disk.
        SQL_COPT_SS_QUOTED_IDENT = SQL_COPT_SS_BASE + 17        # Enable/Disable Quoted Identifiers
        SQL_COPT_SS_ANSI_NPW = SQL_COPT_SS_BASE + 18        # Enable/Disable ANSI NULL, Padding and Warnings
        SQL_COPT_SS_BCP = SQL_COPT_SS_BASE + 19        # Allow BCP usage on connection
        SQL_COPT_SS_TRANSLATE = SQL_COPT_SS_BASE + 20        # Perform code page translation
        SQL_COPT_SS_ATTACHDBFILENAME = SQL_COPT_SS_BASE + 21        # File name to be attached as a database
        SQL_COPT_SS_CONCAT_NULL = SQL_COPT_SS_BASE + 22        # Enable/Disable CONCAT_NULL_YIELDS_NULL
        SQL_COPT_SS_ENCRYPT = SQL_COPT_SS_BASE + 23        # Allow strong encryption for data
        SQL_COPT_SS_MAX_USED = SQL_COPT_SS_ENCRYPT

        # Statement Options
        SQL_SOPT_SS_BASE = 1225
        SQL_SOPT_SS_TEXTPTR_LOGGING = SQL_SOPT_SS_BASE + 0        # Text pointer logging
        SQL_SOPT_SS_CURRENT_COMMAND = SQL_SOPT_SS_BASE + 1        # dbcurcmd SQLGetStmtOption only
        SQL_SOPT_SS_HIDDEN_COLUMNS = SQL_SOPT_SS_BASE + 2        # Expose FOR BROWSE hidden columns
        SQL_SOPT_SS_NOBROWSETABLE = SQL_SOPT_SS_BASE + 3        # Set NOBROWSETABLE option
        SQL_SOPT_SS_REGIONALIZE = SQL_SOPT_SS_BASE + 4        # Regionalize output character conversions
        SQL_SOPT_SS_CURSOR_OPTIONS = SQL_SOPT_SS_BASE + 5        # Server cursor options
        SQL_SOPT_SS_NOCOUNT_STATUS = SQL_SOPT_SS_BASE + 6        # Real vs. Not Real row count indicator
        SQL_SOPT_SS_DEFER_PREPARE = SQL_SOPT_SS_BASE + 7        # Defer prepare until necessary
        SQL_SOPT_SS_MAX_USED = SQL_SOPT_SS_DEFER_PREPARE
        SQL_COPT_SS_BASE_EX = 1240
        SQL_COPT_SS_BROWSE_CONNECT = SQL_COPT_SS_BASE_EX + 1        # Browse connect mode of operation
        SQL_COPT_SS_BROWSE_SERVER = SQL_COPT_SS_BASE_EX + 2        # Single Server browse request.
        SQL_COPT_SS_WARN_ON_CP_ERROR = SQL_COPT_SS_BASE_EX + 3        # Issues warning when data from the server

        # had a loss during code page conversion.
        SQL_COPT_SS_CONNECTION_DEAD = SQL_COPT_SS_BASE_EX + 4        # dbdead SQLGetConnectOption only

        # It will try to ping the server.
        # Expensive connection check
        SQL_COPT_SS_BROWSE_CACHE_DATA = SQL_COPT_SS_BASE_EX + 5        # Determines if we should cache browse info

        # Used when returned buffer is greater then ODBC limit (32K)
        SQL_COPT_SS_RESET_CONNECTION = SQL_COPT_SS_BASE_EX + 6        # When this option is set, we will perform connection reset

        # on next packet
        SQL_COPT_SS_EX_MAX_USED = SQL_COPT_SS_RESET_CONNECTION

        # Defines for use with SQL_COPT_SS_USE_PROC_FOR_PREP
        SQL_UP_OFF = 0L        # Procedures won't be used for prepare
        SQL_UP_ON = 1L        # Procedures will be used for prepare
        SQL_UP_ON_DROP = 2L        # Temp procedures will be explicitly dropped
        SQL_UP_DEFAULT = SQL_UP_ON

        # Defines for use with SQL_COPT_SS_INTEGRATED_SECURITY - Pre-Connect
        # Option only
        SQL_IS_OFF = 0L        # Integrated security isn't used
        SQL_IS_ON = 1L        # Integrated security is used
        SQL_IS_DEFAULT = SQL_IS_OFF

        # Defines for use with SQL_COPT_SS_PRESERVE_CURSORS
        SQL_PC_OFF = 0L        # Cursors are closed on SQLTransact
        SQL_PC_ON = 1L        # Cursors remain open on SQLTransact
        SQL_PC_DEFAULT = SQL_PC_OFF

        # Defines for use with SQL_COPT_SS_USER_DATA
        SQL_UD_NOTSET = NULL        # No user data pointer set

        # Defines for use with SQL_COPT_SS_TRANSLATE
        SQL_XL_OFF = 0L        # Code page translation is not performed
        SQL_XL_ON = 1L        # Code page translation is performed
        SQL_XL_DEFAULT = SQL_XL_ON

        # Defines for use with SQL_COPT_SS_FALLBACK_CONNECT - Pre-Connect
        # Option only
        SQL_FB_OFF = 0L        # FallBack connections are disabled
        SQL_FB_ON = 1L        # FallBack connections are enabled
        SQL_FB_DEFAULT = SQL_FB_OFF

        # Defines for use with SQL_COPT_SS_BCP - Pre-Connect Option only
        SQL_BCP_OFF = 0L        # BCP is not allowed on connection
        SQL_BCP_ON = 1L        # BCP is allowed on connection
        SQL_BCP_DEFAULT = SQL_BCP_OFF

        # Defines for use with SQL_COPT_SS_QUOTED_IDENT
        SQL_QI_OFF = 0L        # Quoted identifiers are enable
        SQL_QI_ON = 1L        # Quoted identifiers are disabled
        SQL_QI_DEFAULT = SQL_QI_ON

        # Defines for use with SQL_COPT_SS_ANSI_NPW - Pre-Connect Option only
        SQL_AD_OFF = 0L        # ANSI NULLs, Padding and Warnings are enabled
        SQL_AD_ON = 1L        # ANSI NULLs, Padding and Warnings are disabled
        SQL_AD_DEFAULT = SQL_AD_ON

        # Defines for use with SQL_COPT_SS_CONCAT_NULL - Pre-Connect Option
        # only
        SQL_CN_OFF = 0L        # CONCAT_NULL_YIELDS_NULL is off
        SQL_CN_ON = 1L        # CONCAT_NULL_YIELDS_NULL is on
        SQL_CN_DEFAULT = SQL_CN_ON

        # Defines for use with SQL_SOPT_SS_TEXTPTR_LOGGING
        SQL_TL_OFF = 0L        # No logging on text pointer ops
        SQL_TL_ON = 1L        # Logging occurs on text pointer ops
        SQL_TL_DEFAULT = SQL_TL_ON

        # Defines for use with SQL_SOPT_SS_HIDDEN_COLUMNS
        SQL_HC_OFF = 0L        # FOR BROWSE columns are hidden
        SQL_HC_ON = 1L        # FOR BROWSE columns are exposed
        SQL_HC_DEFAULT = SQL_HC_OFF

        # Defines for use with SQL_SOPT_SS_NOBROWSETABLE
        SQL_NB_OFF = 0L        # NO_BROWSETABLE is off
        SQL_NB_ON = 1L        # NO_BROWSETABLE is on
        SQL_NB_DEFAULT = SQL_NB_OFF

        # Defines for use with SQL_SOPT_SS_REGIONALIZE
        SQL_RE_OFF = 0L        # No regionalization occurs on output character conversions
        SQL_RE_ON = 1L        # Regionalization occurs on output character conversions
        SQL_RE_DEFAULT = SQL_RE_OFF

        # Defines for use with SQL_SOPT_SS_CURSOR_OPTIONS
        SQL_CO_OFF = 0L        # Clear all cursor options
        SQL_CO_FFO = 1L        # Fast-forward cursor will be used
        SQL_CO_AF = 2L        # Autofetch on cursor open
        SQL_CO_FFO_AF = SQL_CO_FFO | SQL_CO_AF        # Fast-forward cursor with autofetch
        SQL_CO_FIREHOSE_AF = 4L        # Auto fetch on fire-hose cursors
        SQL_CO_DEFAULT = SQL_CO_OFF

        # SQL_SOPT_SS_NOCOUNT_STATUS
        SQL_NC_OFF = 0L
        SQL_NC_ON = 1L

        # SQL_SOPT_SS_DEFER_PREPARE
        SQL_DP_OFF = 0L
        SQL_DP_ON = 1L

        # SQL_COPT_SS_ENCRYPT
        SQL_EN_OFF = 0L
        SQL_EN_ON = 1L

        # SQL_COPT_SS_BROWSE_CONNECT
        SQL_MORE_INFO_NO = 0L
        SQL_MORE_INFO_YES = 1L

        # SQL_COPT_SS_BROWSE_CACHE_DATA
        SQL_CACHE_DATA_NO = 0L
        SQL_CACHE_DATA_YES = 1L

        # SQL_COPT_SS_RESET_CONNECTION
        SQL_RESET_YES = 1L

        # SQL_COPT_SS_WARN_ON_CP_ERROR
        SQL_WARN_NO = 0L
        SQL_WARN_YES = 1L

        # Defines returned by SQL_ATTR_CURSOR_TYPE/SQL_CURSOR_TYPE
        SQL_CURSOR_FAST_FORWARD_ONLY = 8        # Only returned by SQLGetStmtAttr/Option

        # SQLColAttributes driver specific defines.
        # SQLSet/GetDescField driver specific defines.
        # Microsoft has 1200 thru 1249 reserved for Microsoft SQL Server
        # driver usage.
        SQL_CA_SS_BASE = 1200
        SQL_CA_SS_COLUMN_SSTYPE = SQL_CA_SS_BASE + 0        # dbcoltype/dbalttype
        SQL_CA_SS_COLUMN_UTYPE = SQL_CA_SS_BASE + 1        # dbcolutype/dbaltutype
        SQL_CA_SS_NUM_ORDERS = SQL_CA_SS_BASE + 2        # dbnumorders
        SQL_CA_SS_COLUMN_ORDER = SQL_CA_SS_BASE + 3        # dbordercol
        SQL_CA_SS_COLUMN_VARYLEN = SQL_CA_SS_BASE + 4        # dbvarylen
        SQL_CA_SS_NUM_COMPUTES = SQL_CA_SS_BASE + 5        # dbnumcompute
        SQL_CA_SS_COMPUTE_ID = SQL_CA_SS_BASE + 6        # dbnextrow status return
        SQL_CA_SS_COMPUTE_BYLIST = SQL_CA_SS_BASE + 7        # dbbylist
        SQL_CA_SS_COLUMN_ID = SQL_CA_SS_BASE + 8        # dbaltcolid
        SQL_CA_SS_COLUMN_OP = SQL_CA_SS_BASE + 9        # dbaltop
        SQL_CA_SS_COLUMN_SIZE = SQL_CA_SS_BASE + 10        # dbcollen
        SQL_CA_SS_COLUMN_HIDDEN = SQL_CA_SS_BASE + 11        # Column is hidden (FOR BROWSE)
        SQL_CA_SS_COLUMN_KEY = SQL_CA_SS_BASE + 12        # Column is key column (FOR BROWSE)

        # define SQL_DESC_BASE_COLUMN_NAME_OLD (SQL_CA_SS_BASE + 13) //This is
        # defined at another location.
        SQL_CA_SS_COLUMN_COLLATION = SQL_CA_SS_BASE + 14        # Column collation (only for chars)
        SQL_CA_SS_VARIANT_TYPE = SQL_CA_SS_BASE + 15
        SQL_CA_SS_VARIANT_SQL_TYPE = SQL_CA_SS_BASE + 16
        SQL_CA_SS_VARIANT_SERVER_TYPE = SQL_CA_SS_BASE + 17
        SQL_CA_SS_MAX_USED = SQL_CA_SS_BASE + 18

        # SQL Server Data Type Tokens.
        # New types for 6.0 and later servers
        # SQL Server Data Type Tokens.
        SQLTEXT = 0x23
        SQLVARBINARY = 0x25
        SQLINTN = 0x26
        SQLVARCHAR = 0x27
        SQLBINARY = 0x2D
        SQLIMAGE = 0x22
        SQLCHARACTER = 0x2F
        SQLINT1 = 0x30
        SQLBIT = 0x32
        SQLINT2 = 0x34
        SQLINT4 = 0x38
        SQLMONEY = 0x3C
        SQLDATETIME = 0x3D
        SQLFLT8 = 0x3E
        SQLFLTN = 0x6D
        SQLMONEYN = 0x6E
        SQLDATETIMN = 0x6F
        SQLFLT4 = 0x3B
        SQLMONEY4 = 0x7A
        SQLDATETIM4 = 0x3A

        # New types for 6.0 and later servers
        SQLDECIMAL = 0x6A
        SQLNUMERIC = 0x6C

        # New types for 7.0 and later servers
        SQLUNIQUEID = 0x24
        SQLBIGCHAR = 0xAF
        SQLBIGVARCHAR = 0xA7
        SQLBIGBINARY = 0xAD
        SQLBIGVARBINARY = 0xA5
        SQLBITN = 0x68
        SQLNCHAR = 0xEF
        SQLNVARCHAR = 0xE7
        SQLNTEXT = 0x63

        # New for 7.x
        SQLINT8 = 0x7F
        SQLVARIANT = 0x62

        # User Data Type definitions.
        # Returned by SQLColAttributes/SQL_CA_SS_COLUMN_UTYPE.
        SQLudtBINARY = 3
        SQLudtBIT = 16
        SQLudtBITN = 0
        SQLudtCHAR = 1
        SQLudtDATETIM4 = 22
        SQLudtDATETIME = 12
        SQLudtDATETIMN = 15
        SQLudtDECML = 24
        SQLudtDECMLN = 26
        SQLudtFLT4 = 23
        SQLudtFLT8 = 8
        SQLudtFLTN = 14
        SQLudtIMAGE = 20
        SQLudtINT1 = 5
        SQLudtINT2 = 6
        SQLudtINT4 = 7
        SQLudtINTN = 13
        SQLudtMONEY = 11
        SQLudtMONEY4 = 21
        SQLudtMONEYN = 17
        SQLudtNUM = 10
        SQLudtNUMN = 25
        SQLudtSYSNAME = 18
        SQLudtTEXT = 19
        SQLudtTIMESTAMP = 80
        SQLudtUNIQUEIDENTIFIER = 0
        SQLudtVARBINARY = 4
        SQLudtVARCHAR = 2
        MIN_USER_DATATYPE = 256

        # Aggregate operator types.
        # Returned by SQLColAttributes/SQL_CA_SS_COLUMN_OP.
        SQLAOPSTDEV = 0x30        # Standard deviation
        SQLAOPSTDEVP = 0x31        # Standard deviation population
        SQLAOPVAR = 0x32        # Variance
        SQLAOPVARP = 0x33        # Variance population
        SQLAOPCNT = 0x4B        # Count
        SQLAOPSUM = 0x4D        # Sum
        SQLAOPAVG = 0x4F        # Average
        SQLAOPMIN = 0x51        # Min
        SQLAOPMAX = 0x52        # Max
        SQLAOPANY = 0x53        # Any
        SQLAOPNOOP = 0x56        # None

        # SQLGetInfo driver specific defines.
        # Microsoft has 1151 thru 1200 reserved for Microsoft SQL Server
        # driver usage.
        SQL_INFO_SS_FIRST = 1199
        SQL_INFO_SS_NETLIB_NAMEW = SQL_INFO_SS_FIRST + 0        # dbprocinfo
        SQL_INFO_SS_NETLIB_NAMEA = SQL_INFO_SS_FIRST + 1        # dbprocinfo
        SQL_INFO_SS_MAX_USED = SQL_INFO_SS_NETLIB_NAMEA
        if defined(UNICODE):
            SQL_INFO_SS_NETLIB_NAME = SQL_INFO_SS_NETLIB_NAMEW
        else:
            SQL_INFO_SS_NETLIB_NAME = SQL_INFO_SS_NETLIB_NAMEA
        # END IF


        # Driver specific SQL type defines.
        # Microsoft has -150 thru -199 reserved for Microsoft SQL Server
        # driver usage.
        SQL_SS_VARIANT = -150

        # SQLGetDiagField driver specific defines.
        # Microsoft has -1150 thru -1199 reserved for Microsoft SQL Server
        # driver usage.
        SQL_DIAG_SS_BASE = -1150
        SQL_DIAG_SS_MSGSTATE = SQL_DIAG_SS_BASE
        SQL_DIAG_SS_SEVERITY = SQL_DIAG_SS_BASE-1
        SQL_DIAG_SS_SRVNAME = SQL_DIAG_SS_BASE-2
        SQL_DIAG_SS_PROCNAME = SQL_DIAG_SS_BASE-3
        SQL_DIAG_SS_LINE = SQL_DIAG_SS_BASE-4

        # SQLGetDiagField/SQL_DIAG_DYNAMIC_FUNCTION_CODE driver specific
        # defines.
        # Microsoft has -200 thru -299 reserved for Microsoft SQL Server
        # driver usage.
        SQL_DIAG_DFC_SS_BASE = -200
        SQL_DIAG_DFC_SS_ALTER_DATABASE = SQL_DIAG_DFC_SS_BASE-0
        SQL_DIAG_DFC_SS_CHECKPOINT = SQL_DIAG_DFC_SS_BASE-1
        SQL_DIAG_DFC_SS_CONDITION = SQL_DIAG_DFC_SS_BASE-2
        SQL_DIAG_DFC_SS_CREATE_DATABASE = SQL_DIAG_DFC_SS_BASE-3
        SQL_DIAG_DFC_SS_CREATE_DEFAULT = SQL_DIAG_DFC_SS_BASE-4
        SQL_DIAG_DFC_SS_CREATE_PROCEDURE = SQL_DIAG_DFC_SS_BASE-5
        SQL_DIAG_DFC_SS_CREATE_RULE = SQL_DIAG_DFC_SS_BASE-6
        SQL_DIAG_DFC_SS_CREATE_TRIGGER = SQL_DIAG_DFC_SS_BASE-7
        SQL_DIAG_DFC_SS_CURSOR_DECLARE = SQL_DIAG_DFC_SS_BASE-8
        SQL_DIAG_DFC_SS_CURSOR_OPEN = SQL_DIAG_DFC_SS_BASE-9
        SQL_DIAG_DFC_SS_CURSOR_FETCH = SQL_DIAG_DFC_SS_BASE-10
        SQL_DIAG_DFC_SS_CURSOR_CLOSE = SQL_DIAG_DFC_SS_BASE-11
        SQL_DIAG_DFC_SS_DEALLOCATE_CURSOR = SQL_DIAG_DFC_SS_BASE-12
        SQL_DIAG_DFC_SS_DBCC = SQL_DIAG_DFC_SS_BASE-13
        SQL_DIAG_DFC_SS_DISK = SQL_DIAG_DFC_SS_BASE-14
        SQL_DIAG_DFC_SS_DROP_DATABASE = SQL_DIAG_DFC_SS_BASE-15
        SQL_DIAG_DFC_SS_DROP_DEFAULT = SQL_DIAG_DFC_SS_BASE-16
        SQL_DIAG_DFC_SS_DROP_PROCEDURE = SQL_DIAG_DFC_SS_BASE-17
        SQL_DIAG_DFC_SS_DROP_RULE = SQL_DIAG_DFC_SS_BASE-18
        SQL_DIAG_DFC_SS_DROP_TRIGGER = SQL_DIAG_DFC_SS_BASE-19
        SQL_DIAG_DFC_SS_DUMP_DATABASE = SQL_DIAG_DFC_SS_BASE-20
        SQL_DIAG_DFC_SS_DUMP_TABLE = SQL_DIAG_DFC_SS_BASE-21
        SQL_DIAG_DFC_SS_DUMP_TRANSACTION = SQL_DIAG_DFC_SS_BASE-22
        SQL_DIAG_DFC_SS_GOTO = SQL_DIAG_DFC_SS_BASE-23
        SQL_DIAG_DFC_SS_INSERT_BULK = SQL_DIAG_DFC_SS_BASE-24
        SQL_DIAG_DFC_SS_KILL = SQL_DIAG_DFC_SS_BASE-25
        SQL_DIAG_DFC_SS_LOAD_DATABASE = SQL_DIAG_DFC_SS_BASE-26
        SQL_DIAG_DFC_SS_LOAD_HEADERONLY = SQL_DIAG_DFC_SS_BASE-27
        SQL_DIAG_DFC_SS_LOAD_TABLE = SQL_DIAG_DFC_SS_BASE-28
        SQL_DIAG_DFC_SS_LOAD_TRANSACTION = SQL_DIAG_DFC_SS_BASE-29
        SQL_DIAG_DFC_SS_PRINT = SQL_DIAG_DFC_SS_BASE-30
        SQL_DIAG_DFC_SS_RAISERROR = SQL_DIAG_DFC_SS_BASE-31
        SQL_DIAG_DFC_SS_READTEXT = SQL_DIAG_DFC_SS_BASE-32
        SQL_DIAG_DFC_SS_RECONFIGURE = SQL_DIAG_DFC_SS_BASE-33
        SQL_DIAG_DFC_SS_RETURN = SQL_DIAG_DFC_SS_BASE-34
        SQL_DIAG_DFC_SS_SELECT_INTO = SQL_DIAG_DFC_SS_BASE-35
        SQL_DIAG_DFC_SS_SET = SQL_DIAG_DFC_SS_BASE-36
        SQL_DIAG_DFC_SS_SET_IDENTITY_INSERT = SQL_DIAG_DFC_SS_BASE-37
        SQL_DIAG_DFC_SS_SET_ROW_COUNT = SQL_DIAG_DFC_SS_BASE-38
        SQL_DIAG_DFC_SS_SET_STATISTICS = SQL_DIAG_DFC_SS_BASE-39
        SQL_DIAG_DFC_SS_SET_TEXTSIZE = SQL_DIAG_DFC_SS_BASE-40
        SQL_DIAG_DFC_SS_SETUSER = SQL_DIAG_DFC_SS_BASE-41
        SQL_DIAG_DFC_SS_SHUTDOWN = SQL_DIAG_DFC_SS_BASE-42
        SQL_DIAG_DFC_SS_TRANS_BEGIN = SQL_DIAG_DFC_SS_BASE-43
        SQL_DIAG_DFC_SS_TRANS_COMMIT = SQL_DIAG_DFC_SS_BASE-44
        SQL_DIAG_DFC_SS_TRANS_PREPARE = SQL_DIAG_DFC_SS_BASE-45
        SQL_DIAG_DFC_SS_TRANS_ROLLBACK = SQL_DIAG_DFC_SS_BASE-46
        SQL_DIAG_DFC_SS_TRANS_SAVE = SQL_DIAG_DFC_SS_BASE-47
        SQL_DIAG_DFC_SS_TRUNCATE_TABLE = SQL_DIAG_DFC_SS_BASE-48
        SQL_DIAG_DFC_SS_UPDATE_STATISTICS = SQL_DIAG_DFC_SS_BASE-49
        SQL_DIAG_DFC_SS_UPDATETEXT = SQL_DIAG_DFC_SS_BASE-50
        SQL_DIAG_DFC_SS_USE = SQL_DIAG_DFC_SS_BASE-51
        SQL_DIAG_DFC_SS_WAITFOR = SQL_DIAG_DFC_SS_BASE-52
        SQL_DIAG_DFC_SS_WRITETEXT = SQL_DIAG_DFC_SS_BASE-53
        SQL_DIAG_DFC_SS_DENY = SQL_DIAG_DFC_SS_BASE-54
        SQL_DIAG_DFC_SS_SET_XCTLVL = SQL_DIAG_DFC_SS_BASE-55

        # Severity codes for SQL_DIAG_SS_SEVERITY
        EX_ANY = 0
        EX_INFO = 10
        EX_MAXISEVERITY = EX_INFO
        EX_MISSING = 11
        EX_TYPE = 12
        EX_DEADLOCK = 13
        EX_PERMIT = 14
        EX_SYNTAX = 15
        EX_USER = 16
        EX_RESOURCE = 17
        EX_INTOK = 18
        MAXUSEVERITY = EX_INTOK
        EX_LIMIT = 19
        EX_CMDFATAL = 20
        MINFATALERR = EX_CMDFATAL
        EX_DBFATAL = 21
        EX_TABCORRUPT = 22
        EX_DBCORRUPT = 23
        EX_HARDWARE = 24
        EX_CONTROL = 25

        # Internal server datatypes - used when binding to SQL_C_BINARY
        if not defined(MAXNUMERICLEN):
            # DB-Library datatypes
            DBMAXCHAR = 8000 + 1            # Max length of DBVARBINARY and DBVARCHAR, etc. + 1 for zero byte
            MAXNAME = SQL_MAX_SQLSERVERNAME + 1            # Max server identifier length including zero byte

            if defined(UNICODE):
                DBCHAR = WCHAR
            else:
                DBCHAR = CHAR
            # END IF

            DBBINARY = UCHAR
            DBTINYINT = UCHAR
            DBSMALLINT = SHORT
            DBUSMALLINT = USHORT
            DBFLT8 = DOUBLE
            DBBIT = UCHAR
            DBBOOL = UCHAR
            DBFLT4 = FLOAT
            DBREAL = DBFLT4
            DBUBOOL = UINT

            dbvarychar._fields_ = [
                ('len', DBSMALLINT),
                ('str', DBCHAR * DBMAXCHAR),
            ]

            dbvarybin._fields_ = [
                ('len', DBSMALLINT),
                ('array', BYTE * DBMAXCHAR),
            ]

            # Internal representation of MONEY data type
            dbmoney._fields_ = [
                # Money value *10,000 (High 32 bits/signed)
                ('mnyhigh', LONG),
                # Money value *10,000 (Low 32 bits/unsigned)
                ('mnylow', ULONG),
            ]

            # Internal representation of DATETIME data type
            dbdatetime._fields_ = [
                # No of days since Jan-1-1900 (maybe negative)
                ('dtdays', LONG),
                # No. of 300 hundredths of a second since midnight
                ('dttime', ULONG),
            ]

            # Internal representation of SMALLDATETIME data type
            dbdatetime4._fields_ = [
                # No of days since Jan-1-1900
                ('numdays', USHORT),
                # No. of minutes since midnight
                ('nummins', USHORT),
            ]

            # Internal representation of SMALLMONEY data type
            DBMONEY4 = LONG

            # Money value *10,000
            DBNUM_PREC_TYPE = BYTE
            DBNUM_SCALE_TYPE = BYTE
            DBNUM_VAL_TYPE = BYTE
            if ODBCVER < 0x0300:
                MAXNUMERICLEN = 16

                # Internal representation of NUMERIC data type
                dbnumeric._fields_ = [
                    # Precision
                    ('precision', DBNUM_PREC_TYPE),
                    # Scale
                    ('scale', DBNUM_SCALE_TYPE),
                    # Sign (1 if positive, 0 if negative)
                    ('sign', BYTE),
                    # Value
                    ('val', DBNUM_VAL_TYPE * MAXNUMERICLEN),
                ]

                # Internal representation of DECIMAL data type
                DBDECIMAL = DBNUMERIC
            else:
                MAXNUMERICLEN = SQL_MAX_NUMERIC_LEN
                DBNUMERIC = SQL_NUMERIC_STRUCT
                DBDECIMAL = SQL_NUMERIC_STRUCT
            # END IF

        # END IF      MAXNUMERICLEN

        if not defined(INT):
            DBINT = LONG
            if not defined(_LPCBYTE_DEFINED):
                _LPCBYTE_DEFINED = VOID
                LPCBYTE = LPBYTE
            # END IF


            LPDBINT = POINTER(DBINT)
        # END IF


        # *************************************************************** This
        # struct is a global used for gathering statistical data on the
        # driver. Access to this structure is controlled via the pStatCrit;
        # ***************************************************************
        sqlperf._fields_ = [
            # Application Profile Statistics
            ('TimerResolution', DWORD),
            ('SQLidu', DWORD),
            ('SQLiduRows', DWORD),
            ('SQLSelects', DWORD),
            ('SQLSelectRows', DWORD),
            ('Transactions', DWORD),
            ('SQLPrepares', DWORD),
            ('ExecDirects', DWORD),
            ('SQLExecutes', DWORD),
            ('CursorOpens', DWORD),
            ('CursorSize', DWORD),
            ('CursorUsed', DWORD),
            ('PercentCursorUsed', LDOUBLE),
            ('AvgFetchTime', LDOUBLE),
            ('AvgCursorSize', LDOUBLE),
            ('AvgCursorUsed', LDOUBLE),
            ('SQLFetchTime', DWORD),
            ('SQLFetchCount', DWORD),
            ('CurrentStmtCount', DWORD),
            ('MaxOpenStmt', DWORD),
            ('SumOpenStmt', DWORD),
            # Connection Statistics
            ('CurrentConnectionCount', DWORD),
            ('MaxConnectionsOpened', DWORD),
            ('SumConnectionsOpened', DWORD),
            ('SumConnectiontime', DWORD),
            ('AvgTimeOpened', LDOUBLE),
            # Network Statistics
            ('ServerRndTrips', DWORD),
            ('BuffersSent', DWORD),
            ('BuffersRec', DWORD),
            ('BytesSent', DWORD),
            ('BytesRec', DWORD),
            # Time Statistics;
            ('msExecutionTime', DWORD),
            ('msNetWorkServerTime', DWORD),
        ]

        # The following are options for SQL_COPT_SS_PERF_DATA and
        # SQL_COPT_SS_PERF_QUERY
        SQL_PERF_START = 1        # Starts the driver sampling performance data.
        SQL_PERF_STOP = 2        # Stops the counters from sampling performance data.

        # The following are defines for SQL_COPT_SS_PERF_DATA_LOG
        SQL_SS_DL_DEFAULT = TEXT("STATS.LOG")

        # The following are defines for SQL_COPT_SS_PERF_QUERY_LOG
        SQL_SS_QL_DEFAULT = TEXT("QUERY.LOG")

        # The following are defines for SQL_COPT_SS_PERF_QUERY_INTERVAL
        SQL_SS_QI_DEFAULT = 30000        # 30,000 milliseconds

        # ODBC BCP prototypes and defines
        # Return codes
        SUCCEED = 1
        FAIL = 0
        SUCCEED_ABORT = 2
        SUCCEED_ASYNC = 3

        # Transfer directions
        DB_IN = 1        # Transfer from client to server
        DB_OUT = 2        # Transfer from server to client

        # bcp_control option
        BCPMAXERRS = 1        # Sets max errors allowed
        BCPFIRST = 2        # Sets first row to be copied out
        BCPLAST = 3        # Sets number of rows to be copied out
        BCPBATCH = 4        # Sets input batch size
        BCPKEEPNULLS = 5        # Sets to insert NULLs for empty input values
        BCPABORT = 6        # Sets to have bcpexec return SUCCEED_ABORT
        BCPODBC = 7        # Sets ODBC canonical character output
        BCPKEEPIDENTITY = 8        # Sets IDENTITY_INSERT on
        BCP6xFILEFMT = 9        # DEPRECATED: Sets 6x file format on
        BCPHINTSA = 10        # Sets server BCP hints (ANSI string)
        BCPHINTSW = 11        # Sets server BCP hints (UNICODE string)
        BCPFILECP = 12        # Sets clients code page for the file
        BCPUNICODEFILE = 13        # Sets that the file contains unicode header

        # Sets BCP mode to expect a text file and to detect Unicode or ANSI
        # automatically
        BCPTEXTFILE = 14
        BCPFILEFMT = 15        # Sets file format version

        # BCPFILECP values
        # Any valid code page that is installed on the client can be passed
        # plus:
        BCPFILECP_ACP = 0        # Data in file is in Windows code page
        BCPFILECP_OEMCP = 1        # Data in file is in OEM code page (default)
        BCPFILECP_RAW = -1        # Data in file is in Server code page (no conversion)

        # bcp_collen definition
        SQL_VARLEN_DATA = -10        # Use default length for column

        odbcbcp = ctypes.windll.ODBCBCP

        # DBINT	SQL_API bcp_batch (HDBC);
        bcp_batch = odbcbcp.bcp_batch
        bcp_batch.restype = DBINT

        # RETCODE SQL_API bcp_bind (HDBC, LPCBYTE, INT, DBINT, LPCBYTE, INT, INT, INT);
        bcp_bind = odbcbcp.bcp_bind
        bcp_bind.restype = RETCODE

        # RETCODE SQL_API bcp_colfmt (HDBC, INT, BYTE, INT, DBINT, LPCBYTE, INT, INT);
        bcp_colfmt = odbcbcp.bcp_colfmt
        bcp_colfmt.restype = RETCODE

        # RETCODE SQL_API bcp_collen (HDBC, DBINT, INT);
        bcp_collen = odbcbcp.bcp_collen
        bcp_collen.restype = RETCODE

        # RETCODE SQL_API bcp_colptr (HDBC, LPCBYTE, INT);
        bcp_colptr = odbcbcp.bcp_colptr
        bcp_colptr.restype = RETCODE

        # RETCODE SQL_API bcp_columns (HDBC, INT);
        bcp_columns = odbcbcp.bcp_columns
        bcp_columns.restype = RETCODE

        # RETCODE SQL_API bcp_control (HDBC, INT, void *);
        bcp_control = odbcbcp.bcp_control
        bcp_control.restype = RETCODE

        # DBINT	SQL_API bcp_done (HDBC);
        bcp_done = odbcbcp.bcp_done
        bcp_done.restype = DBINT

        # RETCODE SQL_API bcp_exec (HDBC, LPDBINT);
        bcp_exec = odbcbcp.bcp_exec
        bcp_exec.restype = RETCODE

        # RETCODE SQL_API bcp_getcolfmt (HDBC, INT, INT, void *, INT, INT *);
        bcp_getcolfmt = odbcbcp.bcp_getcolfmt
        bcp_getcolfmt.restype = RETCODE

        # RETCODE SQL_API bcp_initA (HDBC, LPCSTR, LPCSTR, LPCSTR, INT);
        bcp_initA = odbcbcp.bcp_initA
        bcp_initA.restype = RETCODE

        # RETCODE SQL_API bcp_initW (HDBC, LPCWSTR, LPCWSTR, LPCWSTR, INT);
        bcp_initW = odbcbcp.bcp_initW
        bcp_initW.restype = RETCODE

        # RETCODE SQL_API bcp_moretext (HDBC, DBINT, LPCBYTE);
        bcp_moretext = odbcbcp.bcp_moretext
        bcp_moretext.restype = RETCODE

        # RETCODE SQL_API bcp_readfmtA (HDBC, LPCSTR);
        bcp_readfmtA = odbcbcp.bcp_readfmtA
        bcp_readfmtA.restype = RETCODE

        # RETCODE SQL_API bcp_readfmtW (HDBC, LPCWSTR);
        bcp_readfmtW = odbcbcp.bcp_readfmtW
        bcp_readfmtW.restype = RETCODE

        # RETCODE SQL_API bcp_sendrow (HDBC);
        bcp_sendrow = odbcbcp.bcp_sendrow
        bcp_sendrow.restype = RETCODE

        # RETCODE SQL_API bcp_setcolfmt (HDBC, INT, INT, void *, INT);
        bcp_setcolfmt = odbcbcp.bcp_setcolfmt
        bcp_setcolfmt.restype = RETCODE

        # RETCODE SQL_API bcp_writefmtA (HDBC, LPCSTR);
        bcp_writefmtA = odbcbcp.bcp_writefmtA
        bcp_writefmtA.restype = RETCODE

        # RETCODE SQL_API bcp_writefmtW (HDBC, LPCWSTR);
        bcp_writefmtW = odbcbcp.bcp_writefmtW
        bcp_writefmtW.restype = RETCODE

        # CHAR *	SQL_API dbprtypeA (INT);
        dbprtypeA = odbcbcp.dbprtypeA
        dbprtypeA.restype = CHAR

        # WCHAR * SQL_API dbprtypeW (INT);
        dbprtypeW = odbcbcp.dbprtypeW
        dbprtypeW.restype = WCHAR


        # BCP functions
        if defined(UNICODE):
            bcp_init = bcp_initW
            bcp_readfmt = bcp_readfmtW
            bcp_writefmt = bcp_writefmtW
            dbprtype = dbprtypeW
            BCPHINTS = BCPHINTSW
        else:
            bcp_init = bcp_initA
            bcp_readfmt = bcp_readfmtA
            bcp_writefmt = bcp_writefmtA
            dbprtype = dbprtypeA
            BCPHINTS = BCPHINTSA
        # END IF

        # SQL Server catalog extensions for distributed queries
        # SQLRETURN SQL_API SQLLinkedServers (SQLHSTMT);
        SQLLinkedServers = odbcbcp.SQLLinkedServers
        SQLLinkedServers.restype = SQLRETURN

        # SQLRETURN SQL_API SQLLinkedCatalogsA (SQLHSTMT, LPCSTR, SWORD);
        SQLLinkedCatalogsA = odbcbcp.SQLLinkedCatalogsA
        SQLLinkedCatalogsA.restype = SQLRETURN

        # SQLRETURN SQL_API SQLLinkedCatalogsW (SQLHSTMT, LPCWSTR, SWORD);
        SQLLinkedCatalogsW = odbcbcp.SQLLinkedCatalogsW
        SQLLinkedCatalogsW.restype = SQLRETURN

        # SQL Server extensions for server enumeration
        # HANDLE   SQL_API SQLInitEnumServers(_In_ LPWSTR pwchServerName, _In_ LPWSTR pwchInstanceName);
        SQLInitEnumServers = odbcbcp.SQLInitEnumServers
        SQLInitEnumServers.restype = HANDLE

        # RETCODE  SQL_API SQLGetNextEnumeration (HANDLE hEnumHandle,BYTE * prgEnumData,INT * piEnumLength);
        SQLGetNextEnumeration = odbcbcp.SQLGetNextEnumeration
        SQLGetNextEnumeration.restype = RETCODE

        # RETCODE  SQL_API SQLCloseEnumServers (HANDLE hEnumHandle);
        SQLCloseEnumServers = odbcbcp.SQLCloseEnumServers
        SQLCloseEnumServers.restype = RETCODE

        if defined(UNICODE):
            SQLLinkedCatalogs = SQLLinkedCatalogsW
        else:
            SQLLinkedCatalogs = SQLLinkedCatalogsA
        # END IF


        # BCP column format properties
        BCP_FMT_TYPE = 0x01
        BCP_FMT_INDICATOR_LEN = 0x02
        BCP_FMT_DATA_LEN = 0x03
        BCP_FMT_TERMINATOR = 0x04
        BCP_FMT_SERVER_COL = 0x05
        BCP_FMT_COLLATION = 0x06
        BCP_FMT_COLLATION_ID = 0x07

        # The following options have been deprecated
        SQL_FAST_CONNECT = SQL_COPT_SS_BASE + 0

        # Defines for use with SQL_FAST_CONNECT - only useable before
        # connecting
        SQL_FC_OFF = 0L        # Fast connect is off
        SQL_FC_ON = 1L        # Fast connect is on
        SQL_FC_DEFAULT = SQL_FC_OFF
        SQL_COPT_SS_ANSI_OEM = SQL_COPT_SS_BASE + 6
        SQL_AO_OFF = 0L
        SQL_AO_ON = 1L
        SQL_AO_DEFAULT = SQL_AO_OFF

        # Define old names
        SQL_REMOTE_PWD = SQL_COPT_SS_REMOTE_PWD
        SQL_USE_PROCEDURE_FOR_PREPARE = SQL_COPT_SS_USE_PROC_FOR_PREP
        SQL_INTEGRATED_SECURITY = SQL_COPT_SS_INTEGRATED_SECURITY
        SQL_PRESERVE_CURSORS = SQL_COPT_SS_PRESERVE_CURSORS
        SQL_TEXTPTR_LOGGING = SQL_SOPT_SS_TEXTPTR_LOGGING
        SQL_CA_SS_BASE_COLUMN_NAME = SQL_DESC_BASE_COLUMN_NAME
        SQLDECIMALN = 0x6A
        SQLNUMERICN = 0x6C

        if defined(__cplusplus):
            # End of extern "C" {
            pass
        #  END IF  __cplusplus

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF

# End of odbcss.h
