import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__SQL = None
ODBCVER = None
__SQLTYPES = None



# ******************************************************          * Copyright
# (C) Microsoft. All rights reserved. *  *
# *****************************************************
# -----------------------------------------------------------------------------
# File:  sql.h
# Contents:  This is the the main include for ODBC Core functions.
# Comments:  preconditions: include "windows.h"
# -----------------------------------------------------------------------------
if defined(_MSC_VER) and (_MSC_VER > 1000):
    pass
# END IF


if not defined(__SQL):
    __SQL = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA

        # /* ODBCVER Default to ODBC version number (0x0380). To exclude
        # definitions introduced in version 3.8 (or above) define ODBCVER
        # 0x0351 before including <sql.h>
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(ODBCVER):
            ODBCVER = 0x0380
        # END IF

        if not defined(__SQLTYPES):
            from sqltypes_h import * # NOQA
        # END IF

        if defined(__cplusplus):
            # extern "C" { // Assume C declarations for C + +
            pass
        # END IF __cplusplus

        # // special length/indicator values
        SQL_NULL_DATA = -1
        SQL_DATA_AT_EXEC = -2

        # // return values from functions
        SQL_SUCCESS = 0
        SQL_SUCCESS_WITH_INFO = 1
        if (ODBCVER >= 0x0300):
            SQL_NO_DATA = 100
        # END IF
        if (ODBCVER >= 0x0380):
            SQL_PARAM_DATA_AVAILABLE = 101
        # END IF

        SQL_ERROR = -1
        SQL_INVALID_HANDLE = -2

        SQL_STILL_EXECUTING = 2
        SQL_NEED_DATA = 99

        # // test for SQL_SUCCESS or SQL_SUCCESS_WITH_INFO
        def SQL_SUCCEEDED(rc):
            return (rc & ~1) == 0

        #
        # // flags for null-terminated string
        SQL_NTS = -3
        SQL_NTSL = -3

        # // maximum message length
        SQL_MAX_MESSAGE_LENGTH = 512
        #
        # // date/time length constants
        if (ODBCVER >= 0x0300):
            SQL_DATE_LEN = 10
            SQL_TIME_LEN = 8 # add P + 1 if precision is nonzero
            SQL_TIMESTAMP_LEN = 19 # add P + 1 if precision is nonzero
        # END IF
        # // handle type identifiers
        if (ODBCVER >= 0x0300):
            SQL_HANDLE_ENV = 1
            SQL_HANDLE_DBC = 2
            SQL_HANDLE_STMT = 3
            SQL_HANDLE_DESC = 4
        # END IF

        # // environment attribute
        if (ODBCVER >= 0x0300):
            SQL_ATTR_OUTPUT_NTS = 10001
        # END IF

        # // connection attributes
        if (ODBCVER >= 0x0300):
            SQL_ATTR_AUTO_IPD = 10001
            SQL_ATTR_METADATA_ID = 10014
        # END IF ODBCVER >= 0x0300

        # // statement attributes
        if (ODBCVER >= 0x0300):
            SQL_ATTR_APP_ROW_DESC = 10010
            SQL_ATTR_APP_PARAM_DESC = 10011
            SQL_ATTR_IMP_ROW_DESC = 10012
            SQL_ATTR_IMP_PARAM_DESC = 10013
            SQL_ATTR_CURSOR_SCROLLABLE = -1
            SQL_ATTR_CURSOR_SENSITIVITY = -2
        # END IF

        # // SQL_ATTR_CURSOR_SCROLLABLE values
        if (ODBCVER >= 0x0300):
            SQL_NONSCROLLABLE = 0
            SQL_SCROLLABLE = 1
        # END IF ODBCVER >= 0x0300

        # // identifiers of fields in the SQL descriptor
        if (ODBCVER >= 0x0300):
            SQL_DESC_COUNT = 1001
            SQL_DESC_TYPE = 1002
            SQL_DESC_LENGTH = 1003
            SQL_DESC_OCTET_LENGTH_PTR = 1004
            SQL_DESC_PRECISION = 1005
            SQL_DESC_SCALE = 1006
            SQL_DESC_DATETIME_INTERVAL_CODE = 1007
            SQL_DESC_NULLABLE = 1008
            SQL_DESC_INDICATOR_PTR = 1009
            SQL_DESC_DATA_PTR = 1010
            SQL_DESC_NAME = 1011
            SQL_DESC_UNNAMED = 1012
            SQL_DESC_OCTET_LENGTH = 1013
            SQL_DESC_ALLOC_TYPE = 1099
        # END IF

        # identifiers of fields in the diagnostics area
        if ODBCVER >= 0x0300:
            SQL_DIAG_RETURNCODE = 1
            SQL_DIAG_NUMBER = 2
            SQL_DIAG_ROW_COUNT = 3
            SQL_DIAG_SQLSTATE = 4
            SQL_DIAG_NATIVE = 5
            SQL_DIAG_MESSAGE_TEXT = 6
            SQL_DIAG_DYNAMIC_FUNCTION = 7
            SQL_DIAG_CLASS_ORIGIN = 8
            SQL_DIAG_SUBCLASS_ORIGIN = 9
            SQL_DIAG_CONNECTION_NAME = 10
            SQL_DIAG_SERVER_NAME = 11
            SQL_DIAG_DYNAMIC_FUNCTION_CODE = 12
        # END IF

        # dynamic function codes
        if ODBCVER >= 0x0300:
            SQL_DIAG_ALTER_DOMAIN = 3
            SQL_DIAG_ALTER_TABLE = 4
            SQL_DIAG_CALL = 7
            SQL_DIAG_CREATE_ASSERTION = 6
            SQL_DIAG_CREATE_CHARACTER_SET = 8
            SQL_DIAG_CREATE_COLLATION = 10
            SQL_DIAG_CREATE_DOMAIN = 23
            SQL_DIAG_CREATE_INDEX = -1
            SQL_DIAG_CREATE_SCHEMA = 64
            SQL_DIAG_CREATE_TABLE = 77
            SQL_DIAG_CREATE_TRANSLATION = 79
            SQL_DIAG_CREATE_VIEW = 84
            SQL_DIAG_DELETE_WHERE = 19
            SQL_DIAG_DROP_ASSERTION = 24
            SQL_DIAG_DROP_CHARACTER_SET = 25
            SQL_DIAG_DROP_COLLATION = 26
            SQL_DIAG_DROP_DOMAIN = 27
            SQL_DIAG_DROP_INDEX = -2
            SQL_DIAG_DROP_SCHEMA = 31
            SQL_DIAG_DROP_TABLE = 32
            SQL_DIAG_DROP_TRANSLATION = 33
            SQL_DIAG_DROP_VIEW = 36
            SQL_DIAG_DYNAMIC_DELETE_CURSOR = 38
            SQL_DIAG_DYNAMIC_UPDATE_CURSOR = 81
            SQL_DIAG_GRANT = 48
            SQL_DIAG_INSERT = 50
            SQL_DIAG_REVOKE = 59
            SQL_DIAG_SELECT_CURSOR = 85
            SQL_DIAG_UNKNOWN_STATEMENT = 0
            SQL_DIAG_UPDATE_WHERE = 82
        # END IF

        # SQL data type codes
        SQL_UNKNOWN_TYPE = 0
        SQL_CHAR = 1
        SQL_NUMERIC = 2
        SQL_DECIMAL = 3
        SQL_INTEGER = 4
        SQL_SMALLINT = 5
        SQL_FLOAT = 6
        SQL_REAL = 7
        SQL_DOUBLE = 8
        if ODBCVER >= 0x0300:
            SQL_DATETIME = 9
        # END IF

        SQL_VARCHAR = 12

        # One-parameter shortcuts for date/time data types
        if ODBCVER >= 0x0300:
            SQL_TYPE_DATE = 91
            SQL_TYPE_TIME = 92
            SQL_TYPE_TIMESTAMP = 93
        # END IF

        # Statement attribute values for cursor sensitivity
        if ODBCVER >= 0x0300:
            SQL_UNSPECIFIED = 0
            SQL_INSENSITIVE = 1
            SQL_SENSITIVE = 2
        # END IF

        # GetTypeInfo() request for all data types
        SQL_ALL_TYPES = 0

        # Default conversion code for SQLBindCol(), SQLBindParam() and SQLGetData()
        if ODBCVER >= 0x0300:
            SQL_DEFAULT = 99
        # END IF

        # * specifies the data type
        if ODBCVER >= 0x0300:
            SQL_ARD_TYPE = -99
        # END IF

        if ODBCVER >= 0x0380:
            SQL_APD_TYPE = -100
        # END IF

        # SQL date/time type subcodes
        if ODBCVER >= 0x0300:
            SQL_CODE_DATE = 1
            SQL_CODE_TIME = 2
            SQL_CODE_TIMESTAMP = 3
        # END IF

        # CLI option values
        if ODBCVER >= 0x0300:
            SQL_FALSE = 0
            SQL_TRUE = 1
        # END IF

        # values of NULLABLE field in descriptor
        SQL_NO_NULLS = 0
        SQL_NULLABLE = 1

        # * not known whether or not a data type supports null values.
        SQL_NULLABLE_UNKNOWN = 2

        # * supported
        if ODBCVER >= 0x0300:
            SQL_PRED_NONE = 0
            SQL_PRED_CHAR = 1
            SQL_PRED_BASIC = 2
        # END IF

        # values of UNNAMED field in descriptor
        if ODBCVER >= 0x0300:
            SQL_NAMED = 0
            SQL_UNNAMED = 1
        # END IF

        # values of ALLOC_TYPE field in descriptor
        if ODBCVER >= 0x0300:
            SQL_DESC_ALLOC_AUTO = 1
            SQL_DESC_ALLOC_USER = 2
        # END IF

        # FreeStmt() options
        SQL_CLOSE = 0
        SQL_DROP = 1
        SQL_UNBIND = 2
        SQL_RESET_PARAMS = 3

        # and in SQLDataSources()
        SQL_FETCH_NEXT = 1
        SQL_FETCH_FIRST = 2

        # Other codes used for FetchOrientation in SQLFetchScroll()
        SQL_FETCH_LAST = 3
        SQL_FETCH_PRIOR = 4
        SQL_FETCH_ABSOLUTE = 5
        SQL_FETCH_RELATIVE = 6

        # SQLEndTran() options
        SQL_COMMIT = 0
        SQL_ROLLBACK = 1

        # null handles returned by SQLAllocHandle()
        SQL_NULL_HENV = 0
        SQL_NULL_HDBC = 0
        SQL_NULL_HSTMT = 0
        if ODBCVER >= 0x0300:
            SQL_NULL_HDESC = 0
        # END IF

        # null handle used in place of parent handle when allocating HENV
        if ODBCVER >= 0x0300:
            SQL_NULL_HANDLE = 0L
        # END IF

        # Values that may appear in the result set of SQLSpecialColumns()
        SQL_SCOPE_CURROW = 0
        SQL_SCOPE_TRANSACTION = 1
        SQL_SCOPE_SESSION = 2
        SQL_PC_UNKNOWN = 0
        if ODBCVER >= 0x0300:
            SQL_PC_NON_PSEUDO = 1
        # END IF

        SQL_PC_PSEUDO = 2

        # Reserved value for the IdentifierType argument of SQLSpecialColumns()
        if ODBCVER >= 0x0300:
            SQL_ROW_IDENTIFIER = 1
        # END IF

        # Reserved values for UNIQUE argument of SQLStatistics()
        SQL_INDEX_UNIQUE = 0
        SQL_INDEX_ALL = 1

        # Values that may appear in the result set of SQLStatistics()
        SQL_INDEX_CLUSTERED = 1
        SQL_INDEX_HASHED = 2
        SQL_INDEX_OTHER = 3

        # SQLGetFunctions() values to identify ODBC APIs
        SQL_API_SQLALLOCCONNECT = 1
        SQL_API_SQLALLOCENV = 2
        if ODBCVER >= 0x0300:
            SQL_API_SQLALLOCHANDLE = 1001
        # END IF

        SQL_API_SQLALLOCSTMT = 3
        SQL_API_SQLBINDCOL = 4
        if ODBCVER >= 0x0300:
            SQL_API_SQLBINDPARAM = 1002
        # END IF

        SQL_API_SQLCANCEL = 5
        if ODBCVER >= 0x0300:
            SQL_API_SQLCLOSECURSOR = 1003
            SQL_API_SQLCOLATTRIBUTE = 6
        # END IF

        SQL_API_SQLCOLUMNS = 40
        SQL_API_SQLCONNECT = 7
        if ODBCVER >= 0x0300:
            SQL_API_SQLCOPYDESC = 1004
        # END IF

        SQL_API_SQLDATASOURCES = 57
        SQL_API_SQLDESCRIBECOL = 8
        SQL_API_SQLDISCONNECT = 9
        if ODBCVER >= 0x0300:
            SQL_API_SQLENDTRAN = 1005
        # END IF

        SQL_API_SQLERROR = 10
        SQL_API_SQLEXECDIRECT = 11
        SQL_API_SQLEXECUTE = 12
        SQL_API_SQLFETCH = 13
        if ODBCVER >= 0x0300:
            SQL_API_SQLFETCHSCROLL = 1021
        # END IF

        SQL_API_SQLFREECONNECT = 14
        SQL_API_SQLFREEENV = 15
        if ODBCVER >= 0x0300:
            SQL_API_SQLFREEHANDLE = 1006
        # END IF

        SQL_API_SQLFREESTMT = 16
        if ODBCVER >= 0x0300:
            SQL_API_SQLGETCONNECTATTR = 1007
        # END IF

        SQL_API_SQLGETCONNECTOPTION = 42
        SQL_API_SQLGETCURSORNAME = 17
        SQL_API_SQLGETDATA = 43
        if ODBCVER >= 0x0300:
            SQL_API_SQLGETDESCFIELD = 1008
            SQL_API_SQLGETDESCREC = 1009
            SQL_API_SQLGETDIAGFIELD = 1010
            SQL_API_SQLGETDIAGREC = 1011
            SQL_API_SQLGETENVATTR = 1012
        # END IF

        SQL_API_SQLGETFUNCTIONS = 44
        SQL_API_SQLGETINFO = 45
        if ODBCVER >= 0x0300:
            SQL_API_SQLGETSTMTATTR = 1014
        # END IF

        SQL_API_SQLGETSTMTOPTION = 46
        SQL_API_SQLGETTYPEINFO = 47
        SQL_API_SQLNUMRESULTCOLS = 18
        SQL_API_SQLPARAMDATA = 48
        SQL_API_SQLPREPARE = 19
        SQL_API_SQLPUTDATA = 49
        SQL_API_SQLROWCOUNT = 20
        if ODBCVER >= 0x0300:
            SQL_API_SQLSETCONNECTATTR = 1016
        # END IF

        SQL_API_SQLSETCONNECTOPTION = 50
        SQL_API_SQLSETCURSORNAME = 21
        if ODBCVER >= 0x0300:
            SQL_API_SQLSETDESCFIELD = 1017
            SQL_API_SQLSETDESCREC = 1018
            SQL_API_SQLSETENVATTR = 1019
        # END IF

        SQL_API_SQLSETPARAM = 22
        if ODBCVER >= 0x0300:
            SQL_API_SQLSETSTMTATTR = 1020
        # END IF

        SQL_API_SQLSETSTMTOPTION = 51
        SQL_API_SQLSPECIALCOLUMNS = 52
        SQL_API_SQLSTATISTICS = 53
        SQL_API_SQLTABLES = 54
        SQL_API_SQLTRANSACT = 23
        if ODBCVER >= 0x0380:
            SQL_API_SQLCANCELHANDLE = 1550
            SQL_API_SQLCOMPLETEASYNC = 1551
        # END IF

        # Information requested by SQLGetInfo()
        if ODBCVER >= 0x0300:
            SQL_MAX_DRIVER_CONNECTIONS = 0
            SQL_MAXIMUM_DRIVER_CONNECTIONS = SQL_MAX_DRIVER_CONNECTIONS
            SQL_MAX_CONCURRENT_ACTIVITIES = 1
            SQL_MAXIMUM_CONCURRENT_ACTIVITIES = SQL_MAX_CONCURRENT_ACTIVITIES
        # END IF

        SQL_DATA_SOURCE_NAME = 2
        SQL_FETCH_DIRECTION = 8
        SQL_SERVER_NAME = 13
        SQL_SEARCH_PATTERN_ESCAPE = 14
        SQL_DBMS_NAME = 17
        SQL_DBMS_VER = 18
        SQL_ACCESSIBLE_TABLES = 19
        SQL_ACCESSIBLE_PROCEDURES = 20
        SQL_CURSOR_COMMIT_BEHAVIOR = 23
        SQL_DATA_SOURCE_READ_ONLY = 25
        SQL_DEFAULT_TXN_ISOLATION = 26
        SQL_IDENTIFIER_CASE = 28
        SQL_IDENTIFIER_QUOTE_CHAR = 29
        SQL_MAX_COLUMN_NAME_LEN = 30
        SQL_MAXIMUM_COLUMN_NAME_LENGTH = SQL_MAX_COLUMN_NAME_LEN
        SQL_MAX_CURSOR_NAME_LEN = 31
        SQL_MAXIMUM_CURSOR_NAME_LENGTH = SQL_MAX_CURSOR_NAME_LEN
        SQL_MAX_SCHEMA_NAME_LEN = 32
        SQL_MAXIMUM_SCHEMA_NAME_LENGTH = SQL_MAX_SCHEMA_NAME_LEN
        SQL_MAX_CATALOG_NAME_LEN = 34
        SQL_MAXIMUM_CATALOG_NAME_LENGTH = SQL_MAX_CATALOG_NAME_LEN
        SQL_MAX_TABLE_NAME_LEN = 35
        SQL_SCROLL_CONCURRENCY = 43
        SQL_TXN_CAPABLE = 46
        SQL_TRANSACTION_CAPABLE = SQL_TXN_CAPABLE
        SQL_USER_NAME = 47
        SQL_TXN_ISOLATION_OPTION = 72
        SQL_TRANSACTION_ISOLATION_OPTION = SQL_TXN_ISOLATION_OPTION
        SQL_INTEGRITY = 73
        SQL_GETDATA_EXTENSIONS = 81
        SQL_NULL_COLLATION = 85
        SQL_ALTER_TABLE = 86
        SQL_ORDER_BY_COLUMNS_IN_SELECT = 90
        SQL_SPECIAL_CHARACTERS = 94
        SQL_MAX_COLUMNS_IN_GROUP_BY = 97
        SQL_MAXIMUM_COLUMNS_IN_GROUP_BY = SQL_MAX_COLUMNS_IN_GROUP_BY
        SQL_MAX_COLUMNS_IN_INDEX = 98
        SQL_MAXIMUM_COLUMNS_IN_INDEX = SQL_MAX_COLUMNS_IN_INDEX
        SQL_MAX_COLUMNS_IN_ORDER_BY = 99
        SQL_MAXIMUM_COLUMNS_IN_ORDER_BY = SQL_MAX_COLUMNS_IN_ORDER_BY
        SQL_MAX_COLUMNS_IN_SELECT = 100
        SQL_MAXIMUM_COLUMNS_IN_SELECT = SQL_MAX_COLUMNS_IN_SELECT
        SQL_MAX_COLUMNS_IN_TABLE = 101
        SQL_MAX_INDEX_SIZE = 102
        SQL_MAXIMUM_INDEX_SIZE = SQL_MAX_INDEX_SIZE
        SQL_MAX_ROW_SIZE = 104
        SQL_MAXIMUM_ROW_SIZE = SQL_MAX_ROW_SIZE
        SQL_MAX_STATEMENT_LEN = 105
        SQL_MAXIMUM_STATEMENT_LENGTH = SQL_MAX_STATEMENT_LEN
        SQL_MAX_TABLES_IN_SELECT = 106
        SQL_MAXIMUM_TABLES_IN_SELECT = SQL_MAX_TABLES_IN_SELECT
        SQL_MAX_USER_NAME_LEN = 107
        SQL_MAXIMUM_USER_NAME_LENGTH = SQL_MAX_USER_NAME_LEN
        if ODBCVER >= 0x0300:
            SQL_OJ_CAPABILITIES = 115
            SQL_OUTER_JOIN_CAPABILITIES = SQL_OJ_CAPABILITIES
        # END IF

        if ODBCVER >= 0x0300:
            SQL_XOPEN_CLI_YEAR = 10000
            SQL_CURSOR_SENSITIVITY = 10001
            SQL_DESCRIBE_PARAMETER = 10002
            SQL_CATALOG_NAME = 10003
            SQL_COLLATION_SEQ = 10004
            SQL_MAX_IDENTIFIER_LEN = 10005
            SQL_MAXIMUM_IDENTIFIER_LENGTH = SQL_MAX_IDENTIFIER_LEN
        # END IF

        # SQL_ALTER_TABLE bitmasks
        if ODBCVER >= 0x0200:
            SQL_AT_ADD_COLUMN = 0x00000001
            SQL_AT_DROP_COLUMN = 0x00000002
        # END IF

        if ODBCVER >= 0x0300:
            SQL_AT_ADD_CONSTRAINT = 0x00000008
            # define SQL_AT_COLUMN_SINGLE    0x00000020L
            # define SQL_AT_ADD_COLUMN_DEFAULT   0x00000040L
            # define SQL_AT_ADD_COLUMN_COLLATION   0x00000080L
            # define SQL_AT_SET_COLUMN_DEFAULT   0x00000100L
            # define SQL_AT_DROP_COLUMN_DEFAULT   0x00000200L
            # define SQL_AT_DROP_COLUMN_CASCADE   0x00000400L
            # define SQL_AT_DROP_COLUMN_RESTRICT   0x00000800L
            # define SQL_AT_ADD_TABLE_CONSTRAINT   0x00001000L
            # define SQL_AT_DROP_TABLE_CONSTRAINT_CASCADE  0x00002000L
            # define SQL_AT_DROP_TABLE_CONSTRAINT_RESTRICT 0x00004000L
            # define SQL_AT_CONSTRAINT_NAME_DEFINITION  0x00008000L
            # define SQL_AT_CONSTRAINT_INITIALLY_DEFERRED  0x00010000L
            # define SQL_AT_CONSTRAINT_INITIALLY_IMMEDIATE 0x00020000L
            # define SQL_AT_CONSTRAINT_DEFERRABLE   0x00040000L
            # define SQL_AT_CONSTRAINT_NON_DEFERRABLE   0x00080000L# END IF
        # SQL_ASYNC_MODE values
        if ODBCVER >= 0x0300:
            SQL_AM_NONE = 0
            SQL_AM_CONNECTION = 1
            SQL_AM_STATEMENT = 2
        # END IF

        # SQL_CURSOR_COMMIT_BEHAVIOR values
        SQL_CB_DELETE = 0
        SQL_CB_CLOSE = 1
        SQL_CB_PRESERVE = 2

        # SQL_FETCH_DIRECTION bitmasks
        SQL_FD_FETCH_NEXT = 0x00000001
        SQL_FD_FETCH_FIRST = 0x00000002
        SQL_FD_FETCH_LAST = 0x00000004
        SQL_FD_FETCH_PRIOR = 0x00000008
        SQL_FD_FETCH_ABSOLUTE = 0x00000010
        SQL_FD_FETCH_RELATIVE = 0x00000020

        # SQL_GETDATA_EXTENSIONS bitmasks
        SQL_GD_ANY_COLUMN = 0x00000001
        SQL_GD_ANY_ORDER = 0x00000002

        # SQL_IDENTIFIER_CASE values
        SQL_IC_UPPER = 1
        SQL_IC_LOWER = 2
        SQL_IC_SENSITIVE = 3
        SQL_IC_MIXED = 4

        # SQL_OJ_CAPABILITIES bitmasks
        # NB: this means 'outer join', not what you may be thinking
        if ODBCVER >= 0x0201:
            SQL_OJ_LEFT = 0x00000001
            SQL_OJ_RIGHT = 0x00000002
            SQL_OJ_FULL = 0x00000004
            SQL_OJ_NESTED = 0x00000008
            SQL_OJ_NOT_ORDERED = 0x00000010
            SQL_OJ_INNER = 0x00000020
            SQL_OJ_ALL_COMPARISON_OPS = 0x00000040
        # END IF

        # SQL_SCROLL_CONCURRENCY bitmasks
        SQL_SCCO_READ_ONLY = 0x00000001
        SQL_SCCO_LOCK = 0x00000002
        SQL_SCCO_OPT_ROWVER = 0x00000004
        SQL_SCCO_OPT_VALUES = 0x00000008

        # SQL_TXN_CAPABLE values
        SQL_TC_NONE = 0
        SQL_TC_DML = 1
        SQL_TC_ALL = 2
        SQL_TC_DDL_COMMIT = 3
        SQL_TC_DDL_IGNORE = 4

        # SQL_TXN_ISOLATION_OPTION bitmasks
        SQL_TXN_READ_UNCOMMITTED = 0x00000001
        SQL_TRANSACTION_READ_UNCOMMITTED = SQL_TXN_READ_UNCOMMITTED
        SQL_TXN_READ_COMMITTED = 0x00000002
        SQL_TRANSACTION_READ_COMMITTED = SQL_TXN_READ_COMMITTED
        SQL_TXN_REPEATABLE_READ = 0x00000004
        SQL_TRANSACTION_REPEATABLE_READ = SQL_TXN_REPEATABLE_READ
        SQL_TXN_SERIALIZABLE = 0x00000008
        SQL_TRANSACTION_SERIALIZABLE = SQL_TXN_SERIALIZABLE

        # SQL_NULL_COLLATION values
        SQL_NC_HIGH = 0
        SQL_NC_LOW = 1
        if not defined(RC_INVOKED):
            odbc32 = ctypes.windll.ODBC32

            # SQLRETURN  SQL_API SQLAllocConnect(SQLHENV EnvironmentHandle,
            # _Out_ SQLHDBC *ConnectionHandle);
            SQLAllocConnect = odbc32.SQLAllocConnect
            SQLAllocConnect.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLAllocEnv(_Out_ SQLHENV *EnvironmentHandle);
            SQLAllocEnv = odbc32.SQLAllocEnv
            SQLAllocEnv.restype = SQLRETURN

            if (ODBCVER >= 0x0300):
                # SQLRETURN  SQL_API SQLAllocHandle(SQLSMALLINT HandleType,
                # SQLHANDLE InputHandle, _Out_ SQLHANDLE *OutputHandle);
                SQLAllocHandle = odbc32.SQLAllocHandle
                SQLAllocHandle.restype = SQLRETURN
                pass
            # END IF

            # SQLRETURN  SQL_API SQLAllocStmt(SQLHDBC ConnectionHandle,
            # _Out_ SQLHSTMT *StatementHandle);
            SQLAllocStmt = odbc32.SQLAllocStmt
            SQLAllocStmt.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLBindCol(SQLHSTMT StatementHandle,
            # SQLUSMALLINT ColumnNumber, SQLSMALLINT TargetType,
            # _Inout_updates_opt_(_Inexpressible_(BufferLength)) SQLPOINTER TargetValue,
            # SQLLEN BufferLength, _Inout_opt_ SQLLEN *StrLen_or_Ind);
            SQLBindCol = odbc32.SQLBindCol
            SQLBindCol.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # __declspec(deprecated("ODBC API: SQLBindParam is deprecated. Please use SQLBindParameter instead."))
                # SQLRETURN  SQL_API SQLBindParam(SQLHSTMT StatementHandle,
                # SQLUSMALLINT ParameterNumber, SQLSMALLINT ValueType,
                # SQLSMALLINT ParameterType, SQLULEN LengthPrecision,
                # SQLSMALLINT ParameterScale, SQLPOINTER ParameterValue,
                # SQLLEN *StrLen_or_Ind);
                SQLBindParam = odbc32.SQLBindParam
                SQLBindParam.restype = SQLRETURN

            # END IF

            # SQLRETURN  SQL_API SQLCancel(SQLHSTMT StatementHandle);
            SQLCancel = odbc32.SQLCancel
            SQLCancel.restype = SQL_API

            if ODBCVER >= 0x0380:
                # SQLRETURN  SQL_API SQLCancelHandle(SQLSMALLINT HandleType, SQLHANDLE InputHandle);
                SQLCancelHandle = odbc32.SQLCancelHandle
                SQLCancelHandle.restype = SQL_API
            # END IF   ODBCVER >= 0x0380

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLCloseCursor(SQLHSTMT StatementHandle);
                SQLCloseCursor = odbc32.SQLCloseCursor
                SQLCloseCursor.restype = SQL_API

                if defined(_WIN64):
                    # SQLRETURN  SQL_API SQLColAttribute (SQLHSTMT StatementHandle,
                    # SQLUSMALLINT ColumnNumber, SQLUSMALLINT FieldIdentifier,
                    # _Out_writes_bytes_opt_(BufferLength) SQLPOINTER CharacterAttribute, SQLSMALLINT BufferLength,
                    # _Out_opt_ SQLSMALLINT *StringLength, _Out_opt_ SQLLEN *NumericAttribute);
                    SQLColAttribute = odbc32.SQLColAttribute
                    SQLColAttribute.restype = SQLRETURN
                else:
                    # SQLRETURN  SQL_API SQLColAttribute (SQLHSTMT StatementHandle,
                    # SQLUSMALLINT ColumnNumber, SQLUSMALLINT FieldIdentifier,
                    # _Out_writes_bytes_opt_(BufferLength) SQLPOINTER CharacterAttribute, SQLSMALLINT BufferLength,
                    # _Out_opt_ SQLSMALLINT *StringLength, _Out_opt_ SQLPOINTER NumericAttribute);
                    SQLColAttribute = odbc32.SQLColAttribute
                    SQLColAttribute.restype = SQLRETURN
                # END IF

            # END IF


            # SQLRETURN  SQL_API SQLColumns(SQLHSTMT StatementHandle,
            # _In_reads_opt_(NameLength1) SQLCHAR *CatalogName, SQLSMALLINT NameLength1,
            # _In_reads_opt_(NameLength2) SQLCHAR *SchemaName, SQLSMALLINT NameLength2,
            # _In_reads_opt_(NameLength3) SQLCHAR *TableName, SQLSMALLINT NameLength3,
            # _In_reads_opt_(NameLength4) SQLCHAR *ColumnName, SQLSMALLINT NameLength4);
            SQLColumns = odbc32.SQLColumns
            SQLColumns.restype = SQLRETURN

            if ODBCVER >= 0x0380:
                pass
            # END IF

            # SQLRETURN  SQL_API SQLConnect(SQLHDBC ConnectionHandle,
            # _In_reads_(NameLength1) SQLCHAR *ServerName, SQLSMALLINT NameLength1,
            # _In_reads_(NameLength2) SQLCHAR *UserName, SQLSMALLINT NameLength2,
            # _In_reads_(NameLength3) SQLCHAR *Authentication, SQLSMALLINT NameLength3);
            SQLConnect = odbc32.SQLConnect
            SQLConnect.restype = SQLRETURN


            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLCopyDesc(SQLHDESC SourceDescHandle,
                # SQLHDESC TargetDescHandle);
                SQLCopyDesc = odbc32.SQLCopyDesc
                SQLCopyDesc.restype = SQLRETURN
            # END IF

            # SQLRETURN  SQL_API SQLDataSources(SQLHENV EnvironmentHandle,
            # SQLUSMALLINT Direction, _Out_writes_opt_(BufferLength1) SQLCHAR *ServerName,
            # SQLSMALLINT BufferLength1, _Out_opt_ SQLSMALLINT *NameLength1Ptr,
            # _Out_writes_opt_(BufferLength2) SQLCHAR *Description, SQLSMALLINT BufferLength2,
            # _Out_opt_ SQLSMALLINT *NameLength2Ptr);
            SQLDataSources = odbc32.SQLDataSources
            SQLDataSources.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLDescribeCol(SQLHSTMT StatementHandle,
            # SQLUSMALLINT ColumnNumber, _Out_writes_opt_(BufferLength) SQLCHAR *ColumnName,
            # SQLSMALLINT BufferLength, _Out_opt_ SQLSMALLINT *NameLength,
            # _Out_opt_ SQLSMALLINT *DataType, _Out_opt_ SQLULEN *ColumnSize,
            # _Out_opt_ SQLSMALLINT *DecimalDigits, _Out_opt_ SQLSMALLINT *Nullable);
            SQLDescribeCol = odbc32.SQLDescribeCol
            SQLDescribeCol.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLDisconnect(SQLHDBC ConnectionHandle);
            SQLDisconnect = odbc32.SQLDisconnect
            SQLDisconnect.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLEndTran(SQLSMALLINT HandleType, SQLHANDLE Handle,
                # SQLSMALLINT CompletionType);
                SQLEndTran = odbc32.SQLEndTran
                SQLEndTran.restype = SQLRETURN

            # END IF

            # SQLRETURN  SQL_API SQLError(SQLHENV EnvironmentHandle,
            # SQLHDBC ConnectionHandle, SQLHSTMT StatementHandle,
            # _Out_writes_(6) SQLCHAR *Sqlstate, _Out_opt_ SQLINTEGER *NativeError,
            # _Out_writes_opt_(BufferLength) SQLCHAR *MessageText, SQLSMALLINT BufferLength,
            # _Out_opt_ SQLSMALLINT *TextLength);
            SQLError = odbc32.SQLError
            SQLError.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLExecDirect
            # (
            # SQLHSTMT StatementHandle,
            # _In_reads_opt_(TextLength) SQLCHAR* StatementText,
            # SQLINTEGER TextLength
            # );
            SQLExecDirect = odbc32.SQLExecDirect
            SQLExecDirect.restype = SQLRETURN


            # SQLRETURN  SQL_API SQLExecute(SQLHSTMT StatementHandle);
            SQLExecute = odbc32.SQLExecute
            SQLExecute.restype = SQLRETURN


            # SQLRETURN  SQL_API SQLFetch(SQLHSTMT StatementHandle);
            SQLFetch = odbc32.SQLFetch
            SQLFetch.restype = SQLRETURN


            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLFetchScroll(SQLHSTMT StatementHandle,
                # SQLSMALLINT FetchOrientation, SQLLEN FetchOffset);
                SQLFetchScroll = odbc32.SQLFetchScroll
                SQLFetchScroll.restype = SQLRETURN

            # END IF

            # SQLRETURN  SQL_API SQLFreeConnect(SQLHDBC ConnectionHandle);
            SQLFreeConnect = odbc32.SQLFreeConnect
            SQLFreeConnect.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLFreeEnv(SQLHENV EnvironmentHandle);
            SQLFreeEnv = odbc32.SQLFreeEnv
            SQLFreeEnv.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLFreeHandle(SQLSMALLINT HandleType, SQLHANDLE Handle);
                SQLFreeHandle = odbc32.SQLFreeHandle
                SQLFreeHandle.restype = SQLRETURN


            # END IF

            # SQLRETURN  SQL_API SQLFreeStmt(SQLHSTMT StatementHandle,
            # SQLUSMALLINT Option);
            SQLFreeStmt = odbc32.SQLFreeStmt
            SQLFreeStmt.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLGetConnectAttr(SQLHDBC ConnectionHandle,
                # SQLINTEGER Attribute, _Out_writes_opt_(_Inexpressible_(BufferLength)) SQLPOINTER Value,
                # SQLINTEGER BufferLength, _Out_opt_ SQLINTEGER *StringLengthPtr);
                SQLGetConnectAttr = odbc32.SQLGetConnectAttr
                SQLGetConnectAttr.restype = SQLRETURN

                # __declspec(deprecated("ODBC API: SQLGetConnectOption is deprecated. Please use SQLGetConnectAttr instead."))
            # END IF
            #
            # SQLRETURN  SQL_API SQLGetConnectOption(SQLHDBC ConnectionHandle,
            # SQLUSMALLINT Option, SQLPOINTER Value);
            SQLGetConnectOption = odbc32.SQLGetConnectOption
            SQLGetConnectOption.restype = SQLRETURN


            # SQLRETURN  SQL_API SQLGetData(SQLHSTMT StatementHandle,
            # SQLUSMALLINT ColumnNumber, SQLSMALLINT TargetType,
            # _Out_writes_opt_(_Inexpressible_(BufferLength)) SQLPOINTER TargetValue, SQLLEN BufferLength,
            # _Out_opt_ SQLLEN *StrLen_or_IndPtr);
            SQLGetData = odbc32.SQLGetData
            SQLGetData.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLGetDescField(SQLHDESC DescriptorHandle,
                # SQLSMALLINT RecNumber, SQLSMALLINT FieldIdentifier,
                # _Out_writes_opt_(_Inexpressible_(BufferLength)) SQLPOINTER Value, SQLINTEGER BufferLength,
                # _Out_opt_ SQLINTEGER *StringLength);
                SQLGetDescField = odbc32.SQLGetDescField
                SQLGetDescField.restype = SQLRETURN

                # SQLRETURN  SQL_API SQLGetDescRec(SQLHDESC DescriptorHandle,
                # SQLSMALLINT RecNumber, _Out_writes_opt_(BufferLength) SQLCHAR *Name,
                # SQLSMALLINT BufferLength, _Out_opt_ SQLSMALLINT *StringLengthPtr,
                # _Out_opt_ SQLSMALLINT *TypePtr, _Out_opt_ SQLSMALLINT *SubTypePtr,
                # _Out_opt_ SQLLEN     *LengthPtr, _Out_opt_ SQLSMALLINT *PrecisionPtr,
                # _Out_opt_ SQLSMALLINT *ScalePtr, _Out_opt_ SQLSMALLINT *NullablePtr);
                SQLGetDescRec = odbc32.SQLGetDescRec
                SQLGetDescRec.restype = SQLRETURN

                # SQLRETURN  SQL_API SQLGetDiagField(SQLSMALLINT HandleType, SQLHANDLE Handle,
                # SQLSMALLINT RecNumber, SQLSMALLINT DiagIdentifier,
                # _Out_writes_opt_(_Inexpressible_(BufferLength)) SQLPOINTER DiagInfo, SQLSMALLINT BufferLength,
                # _Out_opt_ SQLSMALLINT *StringLength);
                SQLGetDiagField = odbc32.SQLGetDiagField
                SQLGetDiagField.restype = SQLRETURN

                # SQLRETURN  SQL_API SQLGetEnvAttr(SQLHENV EnvironmentHandle,
                # SQLINTEGER Attribute, _Out_writes_(_Inexpressible_(BufferLength)) SQLPOINTER Value,
                # SQLINTEGER BufferLength, _Out_opt_ SQLINTEGER *StringLength);
                SQLGetEnvAttr = odbc32.SQLGetEnvAttr
                SQLGetEnvAttr.restype = SQLRETURN

            # END IF  ODBCVER >= 0x0300

            # SQLRETURN  SQL_API SQLGetFunctions(SQLHDBC ConnectionHandle,
            # SQLUSMALLINT FunctionId,
            # _Out_writes_opt_(_Inexpressible_("Buffer length pfExists points to depends on fFunction value."))
            # SQLUSMALLINT *Supported);
            SQLGetFunctions = odbc32.SQLGetFunctions
            SQLGetFunctions.restype = SQLRETURN

            # _Success_(return == SQL_SUCCESS)
            # SQLRETURN  SQL_API SQLGetInfo(SQLHDBC ConnectionHandle,
            # SQLUSMALLINT InfoType, _Out_writes_bytes_opt_(BufferLength) SQLPOINTER InfoValue,
            # SQLSMALLINT BufferLength, _Out_opt_ SQLSMALLINT *StringLengthPtr);
            SQLGetInfo = odbc32.SQLGetInfo
            SQLGetInfo.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLGetStmtAttr(SQLHSTMT StatementHandle,
                # SQLINTEGER Attribute, _Out_writes_opt_(_Inexpressible_(BufferLength)) SQLPOINTER Value,
                # SQLINTEGER BufferLength, _Out_opt_ SQLINTEGER *StringLength);
                SQLGetStmtAttr = odbc32.SQLGetStmtAttr
                SQLGetStmtAttr.restype = SQLRETURN

                # __declspec(deprecated("ODBC API: SQLGetStmtOption is deprecated. Please use SQLGetStmtAttr instead."))
            # END IF ODBCVER >= 0x0300
            #
            # SQLRETURN  SQL_API SQLGetStmtOption(SQLHSTMT StatementHandle,
            # SQLUSMALLINT Option, SQLPOINTER Value);
            SQLGetStmtOption = odbc32.SQLGetStmtOption
            SQLGetStmtOption.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLGetTypeInfo(SQLHSTMT StatementHandle,
            # SQLSMALLINT DataType);
            SQLGetTypeInfo = odbc32.SQLGetTypeInfo
            SQLGetTypeInfo.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLNumResultCols(SQLHSTMT StatementHandle,
            # _Out_ SQLSMALLINT *ColumnCount);
            SQLNumResultCols = odbc32.SQLNumResultCols
            SQLNumResultCols.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLParamData(SQLHSTMT StatementHandle,
            # _Out_opt_ SQLPOINTER *Value);
            SQLParamData = odbc32.SQLParamData
            SQLParamData.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLPutData(SQLHSTMT StatementHandle,
            # _In_reads_(_Inexpressible_(StrLen_or_Ind)) SQLPOINTER Data, SQLLEN StrLen_or_Ind);
            SQLPutData = odbc32.SQLPutData
            SQLPutData.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLRowCount(_In_ SQLHSTMT StatementHandle,
            # _Out_ SQLLEN* RowCount);
            SQLRowCount = odbc32.SQLRowCount
            SQLRowCount.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLSetConnectAttr(SQLHDBC ConnectionHandle,
                # SQLINTEGER Attribute, _In_reads_bytes_opt_(StringLength) SQLPOINTER Value,
                # SQLINTEGER StringLength);
                SQLSetConnectAttr = odbc32.SQLSetConnectAttr
                SQLSetConnectAttr.restype = SQLRETURN

                # __declspec(deprecated("ODBC API: SQLSetConnectOption is deprecated. Please use SQLSetConnectAttr instead."))

            # END IF ODBCVER >= 0x0300
            #
            # SQLRETURN  SQL_API SQLSetConnectOption(SQLHDBC ConnectionHandle,
            # SQLUSMALLINT Option, SQLULEN Value);
            SQLSetConnectOption = odbc32.SQLSetConnectOption
            SQLSetConnectOption.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLSetDescField(SQLHDESC DescriptorHandle,
                # SQLSMALLINT RecNumber, SQLSMALLINT FieldIdentifier,
                # _In_reads_(_Inexpressible_(BufferLength)) SQLPOINTER Value, SQLINTEGER BufferLength);
                SQLSetDescField = odbc32.SQLSetDescField
                SQLSetDescField.restype = SQLRETURN

                # SQLRETURN  SQL_API SQLSetDescRec(SQLHDESC DescriptorHandle,
                # SQLSMALLINT RecNumber, SQLSMALLINT Type,
                # SQLSMALLINT SubType, SQLLEN Length,
                # SQLSMALLINT Precision, SQLSMALLINT Scale,
                # _Inout_updates_bytes_opt_(Length) SQLPOINTER Data, _Inout_opt_ SQLLEN *StringLength,
                #  _Inout_opt_ SQLLEN *Indicator);
                SQLSetDescRec = odbc32.SQLSetDescRec
                SQLSetDescRec.restype = SQLRETURN

                # SQLRETURN  SQL_API SQLSetEnvAttr(SQLHENV EnvironmentHandle,
                # SQLINTEGER Attribute, _In_reads_bytes_opt_(StringLength) SQLPOINTER Value,
                # SQLINTEGER StringLength);
                SQLSetEnvAttr = odbc32.SQLSetEnvAttr
                SQLSetEnvAttr.restype = SQLRETURN

            # END IF  ODBCVER >= 0x0300

            # __declspec(deprecated("ODBC API: SQLSetParam is deprecated. Please use SQLBindParameter instead."))
            # SQLRETURN  SQL_API SQLSetParam(SQLHSTMT StatementHandle,
            # SQLUSMALLINT ParameterNumber, SQLSMALLINT ValueType,
            # SQLSMALLINT ParameterType, SQLULEN LengthPrecision,
            # SQLSMALLINT ParameterScale, _In_reads_(_Inexpressible_(*StrLen_or_Ind)) SQLPOINTER ParameterValue,
            # _Inout_ SQLLEN *StrLen_or_Ind);
            SQLSetParam = odbc32.SQLSetParam
            SQLSetParam.restype = SQLRETURN

            if ODBCVER >= 0x0300:
                # SQLRETURN  SQL_API SQLSetStmtAttr(SQLHSTMT StatementHandle,
                # SQLINTEGER Attribute, _In_reads_(_Inexpressible_(StringLength)) SQLPOINTER Value,
                # SQLINTEGER StringLength);
                SQLSetStmtAttr = odbc32.SQLSetStmtAttr
                SQLSetStmtAttr.restype = SQLRETURN

                # __declspec(deprecated("ODBC API: SQLSetStmtOption is deprecated. Please use SQLSetStmtAttr instead."))
            # END IF
            #
            # SQLRETURN  SQL_API SQLSetStmtOption(SQLHSTMT StatementHandle,
            # SQLUSMALLINT Option, SQLULEN Value);
            SQLSetStmtOption = odbc32.SQLSetStmtOption
            SQLSetStmtOption.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLSpecialColumns(SQLHSTMT StatementHandle,
            # SQLUSMALLINT IdentifierType,
            # _In_reads_opt_(NameLength1) SQLCHAR *CatalogName, SQLSMALLINT NameLength1,
            # _In_reads_opt_(NameLength2) SQLCHAR *SchemaName, SQLSMALLINT NameLength2,
            # _In_reads_opt_(NameLength3) SQLCHAR *TableName, SQLSMALLINT NameLength3,
            # SQLUSMALLINT Scope, SQLUSMALLINT Nullable);
            SQLSpecialColumns = odbc32.SQLSpecialColumns
            SQLSpecialColumns.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLStatistics(SQLHSTMT StatementHandle,
            # _In_reads_opt_(NameLength1) SQLCHAR *CatalogName, SQLSMALLINT NameLength1,
            # _In_reads_opt_(NameLength2) SQLCHAR *SchemaName, SQLSMALLINT NameLength2,
            # _In_reads_opt_(NameLength3) SQLCHAR *TableName, SQLSMALLINT NameLength3,
            # SQLUSMALLINT Unique, SQLUSMALLINT Reserved);
            SQLStatistics = odbc32.SQLStatistics
            SQLStatistics.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLTables(SQLHSTMT StatementHandle,
            # _In_reads_opt_(NameLength1) SQLCHAR *CatalogName, SQLSMALLINT NameLength1,
            # _In_reads_opt_(NameLength2) SQLCHAR *SchemaName, SQLSMALLINT NameLength2,
            # _In_reads_opt_(NameLength3) SQLCHAR *TableName, SQLSMALLINT NameLength3,
            # _In_reads_opt_(NameLength4) SQLCHAR *TableType, SQLSMALLINT NameLength4);
            SQLTables = odbc32.SQLTables
            SQLTables.restype = SQLRETURN

            # SQLRETURN  SQL_API SQLTransact(SQLHENV EnvironmentHandle,
            # SQLHDBC ConnectionHandle, SQLUSMALLINT CompletionType);
            SQLTransact = odbc32.SQLTransact
            SQLTransact.restype = SQLRETURN

            # END IF  RC_INVOKED

        if defined(__cplusplus):
            # End of extern "C" {
            pass
        # END IF  __cplusplus

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  #ifndef __SQL
