import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__SQLEXT = None
__SQL = None
ODBC_STD = None
WIN32 = None

class tagODBC_VS_ARGS(ctypes.Structure):
    pass


ODBC_VS_ARGS = tagODBC_VS_ARGS
PODBC_VS_ARGS = POINTER(tagODBC_VS_ARGS)

# ******************************************************          * Copyright
# (C) Microsoft. All rights reserved. *  *
# *****************************************************
# -----------------------------------------------------------------------------
# File:  sqlext.h
# Contents:  This is the include for applications using the Microsoft SQL
# Extensions
# Comments:
# -----------------------------------------------------------------------------
if defined(_MSC_VER) and (_MSC_VER > 1000):
    pass
# END IF


if not defined(__SQLEXT):
    __SQLEXT = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(__SQL):
            from pyWinAPI.um.sql_h import * # NOQA
        # END IF

        from pyWinAPI.um.sqlucode_h import * # NOQA

        if defined(__cplusplus):
            # Assume C declarations for C + +
            pass
        #  END IF  __cplusplus
        # generally useful constants
        SQL_SPEC_MAJOR = 3        # Major version of specification
        SQL_SPEC_MINOR = 80        # Minor version of specification
        SQL_SPEC_STRING = "03.80"        # String constant for version
        SQL_SQLSTATE_SIZE = 5        # size of SQLSTATE
        SQLSTATE = SQLTCHAR * SQL_SQLSTATE_SIZE + 1
        SQL_MAX_DSN_LENGTH = 32        # maximum data source name size
        SQL_MAX_OPTION_STRING_LENGTH = 256

        # return code SQL_NO_DATA_FOUND is the same as SQL_NO_DATA
        if ODBCVER < 0x0300:
            SQL_NO_DATA_FOUND = 100
        else:
            SQL_NO_DATA_FOUND = SQL_NO_DATA
        # END IF

        # an end handle type
        if ODBCVER >= 0x0300:
            SQL_HANDLE_SENV = 5
        # END IF  ODBCVER >= 0x0300

        # env attribute
        if ODBCVER >= 0x0300:
            SQL_ATTR_ODBC_VERSION = 200
            SQL_ATTR_CONNECTION_POOLING = 201
            SQL_ATTR_CP_MATCH = 202

            # For private driver manager
            SQL_ATTR_APPLICATION_KEY = 203
        # END IF  ODBCVER >= 0x0300

        if ODBCVER >= 0x0300:
            # values for SQL_ATTR_CONNECTION_POOLING
            SQL_CP_OFF = 0
            SQL_CP_ONE_PER_DRIVER = 1
            SQL_CP_ONE_PER_HENV = 2
            SQL_CP_DRIVER_AWARE = 3
            SQL_CP_DEFAULT = SQL_CP_OFF

            # values for SQL_ATTR_CP_MATCH
            SQL_CP_STRICT_MATCH = 0
            SQL_CP_RELAXED_MATCH = 1
            SQL_CP_MATCH_DEFAULT = SQL_CP_STRICT_MATCH

            # values for SQL_ATTR_ODBC_VERSION
            SQL_OV_ODBC2 = 2
            SQL_OV_ODBC3 = 3
        # END IF  ODBCVER >= 0x0300

        if ODBCVER >= 0x0380:
            # new values for SQL_ATTR_ODBC_VERSION
            # From ODBC 3.8 onwards, we should use <major version> * 100 +
            # <minor version>
            SQL_OV_ODBC3_80 = 380

            # endif /* ODBCVER >= 0x0380 /* connection attributes
            SQL_ACCESS_MODE = 101
            SQL_AUTOCOMMIT = 102
            SQL_LOGIN_TIMEOUT = 103
            SQL_OPT_TRACE = 104
            SQL_OPT_TRACEFILE = 105
            SQL_TRANSLATE_DLL = 106
            SQL_TRANSLATE_OPTION = 107
            SQL_TXN_ISOLATION = 108
            SQL_CURRENT_QUALIFIER = 109
            SQL_ODBC_CURSORS = 110
            SQL_QUIET_MODE = 111
            SQL_PACKET_SIZE = 112

            # connection attributes with new names
            if ODBCVER >= 0x0300:
                SQL_ATTR_ACCESS_MODE = SQL_ACCESS_MODE
                SQL_ATTR_AUTOCOMMIT = SQL_AUTOCOMMIT
                SQL_ATTR_CONNECTION_TIMEOUT = 113
                SQL_ATTR_CURRENT_CATALOG = SQL_CURRENT_QUALIFIER
                SQL_ATTR_DISCONNECT_BEHAVIOR = 114
                SQL_ATTR_ENLIST_IN_DTC = 1207
                SQL_ATTR_ENLIST_IN_XA = 1208
                SQL_ATTR_LOGIN_TIMEOUT = SQL_LOGIN_TIMEOUT
                SQL_ATTR_ODBC_CURSORS = SQL_ODBC_CURSORS
                SQL_ATTR_PACKET_SIZE = SQL_PACKET_SIZE
                SQL_ATTR_QUIET_MODE = SQL_QUIET_MODE
                SQL_ATTR_TRACE = SQL_OPT_TRACE
                SQL_ATTR_TRACEFILE = SQL_OPT_TRACEFILE
                SQL_ATTR_TRANSLATE_LIB = SQL_TRANSLATE_DLL
                SQL_ATTR_TRANSLATE_OPTION = SQL_TRANSLATE_OPTION
                SQL_ATTR_TXN_ISOLATION = SQL_TXN_ISOLATION
            # END IF  ODBCVER >= 0x0300

            SQL_ATTR_CONNECTION_DEAD = 1209            # GetConnectAttr only

            if ODBCVER >= 0x0351:
                # /* ODBC Driver Manager sets this connection attribute to a
                # unicode driver (which supports SQLConnectW) when the
                # application is an ANSI application
                # (which calls SQLConnect, SQLDriverConnect, or
                # SQLBrowseConnect). This is SetConnectAttr only and application
                # does not set this attribute This attribute was introduced
                # because some unicode driver's some APIs may need to behave
                # differently on ANSI or Unicode applications. A unicode driver,
                # which has same behavior for both ANSI or Unicode applications,
                # should return SQL_ERROR when the driver manager sets this
                # connection attribute. When a unicode driver returns SQL_SUCCESS
                # on this attribute, the driver manager treates ANSI and Unicode
                # connections differently in connection pooling.
                #
                SQL_ATTR_ANSI_APP = 115
            # END IF

            if ODBCVER >= 0x0380:
                SQL_ATTR_RESET_CONNECTION = 116
                SQL_ATTR_ASYNC_DBC_FUNCTIONS_ENABLE = 117
            # END IF

            # Connection attribute 118 is defined in sqlspi.h
            if ODBCVER >= 0x0380:
                SQL_ATTR_ASYNC_DBC_EVENT = 119
            # END IF  ODBCVER >= 0x0380

            # Connection attribute 120 and 121 are defined in sqlspi.h
            # SQL_CONNECT_OPT_DRVR_START is not meaningful for 3.0 driver
            if ODBCVER < 0x0300:
                SQL_CONNECT_OPT_DRVR_START = 1000
            # END IF  ODBCVER < 0x0300

            if ODBCVER < 0x0300:
                SQL_CONN_OPT_MAX = SQL_PACKET_SIZE
                SQL_CONN_OPT_MIN = SQL_ACCESS_MODE
            # END IF  ODBCVER < 0x0300

            # SQL_ACCESS_MODE options
            SQL_MODE_READ_WRITE = 0
            SQL_MODE_READ_ONLY = 1
            SQL_MODE_DEFAULT = SQL_MODE_READ_WRITE

            # SQL_AUTOCOMMIT options
            SQL_AUTOCOMMIT_OFF = 0
            SQL_AUTOCOMMIT_ON = 1
            SQL_AUTOCOMMIT_DEFAULT = SQL_AUTOCOMMIT_ON

            # SQL_LOGIN_TIMEOUT options
            SQL_LOGIN_TIMEOUT_DEFAULT = 15

            # SQL_OPT_TRACE options
            SQL_OPT_TRACE_OFF = 0
            SQL_OPT_TRACE_ON = 1
            SQL_OPT_TRACE_DEFAULT = SQL_OPT_TRACE_OFF
            SQL_OPT_TRACE_FILE_DEFAULT = "\\SQL.LOG"

            # SQL_ODBC_CURSORS options
            # SQL_CUR_USE_IF_NEEDED and SQL_CUR_USE_ODBC are deprecated.
            # Please use SQL_CUR_USE_DRIVER for cursor functionalities
            # provided by drivers
            SQL_CUR_USE_IF_NEEDED = 0
            SQL_CUR_USE_ODBC = 1
            SQL_CUR_USE_DRIVER = 2
            SQL_CUR_DEFAULT = SQL_CUR_USE_DRIVER
            if ODBCVER >= 0x0300:
                # values for SQL_ATTR_DISCONNECT_BEHAVIOR
                SQL_DB_RETURN_TO_POOL = 0
                SQL_DB_DISCONNECT = 1
                SQL_DB_DEFAULT = SQL_DB_RETURN_TO_POOL

                # values for SQL_ATTR_ENLIST_IN_DTC
                SQL_DTC_DONE = 0
            # END IF  ODBCVER >= 0x0300

            # values for SQL_ATTR_CONNECTION_DEAD
            SQL_CD_TRUE = 1            # Connection is closed/dead
            SQL_CD_FALSE = 0            # Connection is open/available

            # values for SQL_ATTR_ANSI_APP
            if ODBCVER >= 0x0351:
                SQL_AA_TRUE = 1                # the application is an ANSI app
                SQL_AA_FALSE = 0                # the application is a Unicode app
            # END IF

            # values for SQL_ATTR_RESET_CONNECTION
            if ODBCVER >= 0x0380:
                SQL_RESET_CONNECTION_YES = 1
            # END IF

            # values for SQL_ATTR_ASYNC_DBC_FUNCTIONS_ENABLE
            if ODBCVER >= 0x0380:
                SQL_ASYNC_DBC_ENABLE_ON = 1
                SQL_ASYNC_DBC_ENABLE_OFF = 0
                SQL_ASYNC_DBC_ENABLE_DEFAULT = SQL_ASYNC_DBC_ENABLE_OFF
            # END IF   ODBCVER >= 0x0380

            # SQLColAttributes defines
            SQL_COLUMN_COUNT = 0
            SQL_COLUMN_NAME = 1
            SQL_COLUMN_TYPE = 2
            SQL_COLUMN_LENGTH = 3
            SQL_COLUMN_PRECISION = 4
            SQL_COLUMN_SCALE = 5
            SQL_COLUMN_DISPLAY_SIZE = 6
            SQL_COLUMN_NULLABLE = 7
            SQL_COLUMN_UNSIGNED = 8
            SQL_COLUMN_MONEY = 9
            SQL_COLUMN_UPDATABLE = 10
            SQL_COLUMN_AUTO_INCREMENT = 11
            SQL_COLUMN_CASE_SENSITIVE = 12
            SQL_COLUMN_SEARCHABLE = 13
            SQL_COLUMN_TYPE_NAME = 14
            SQL_COLUMN_TABLE_NAME = 15
            SQL_COLUMN_OWNER_NAME = 16
            SQL_COLUMN_QUALIFIER_NAME = 17
            SQL_COLUMN_LABEL = 18

            # SQLColAttributes subdefines for SQL_COLUMN_SEARCHABLE
            # These are also used by SQLGetInfo
            SQL_UNSEARCHABLE = 0
            SQL_LIKE_ONLY = 1
            SQL_ALL_EXCEPT_LIKE = 2
            SQL_SEARCHABLE = 3
            SQL_PRED_SEARCHABLE = SQL_SEARCHABLE

            # statement attributes
            SQL_QUERY_TIMEOUT = 0
            SQL_MAX_ROWS = 1
            SQL_NOSCAN = 2
            SQL_MAX_LENGTH = 3
            SQL_ASYNC_ENABLE = 4
            SQL_BIND_TYPE = 5
            SQL_CURSOR_TYPE = 6
            SQL_CONCURRENCY = 7
            SQL_KEYSET_SIZE = 8
            SQL_ROWSET_SIZE = 9
            SQL_SIMULATE_CURSOR = 10
            SQL_RETRIEVE_DATA = 11
            SQL_USE_BOOKMARKS = 12
            SQL_GET_BOOKMARK = 13            # GetStmtOption Only
            SQL_ROW_NUMBER = 14            # GetStmtOption Only

            # statement attributes for ODBC 3.0
            if ODBCVER >= 0x0300:
                SQL_ATTR_ASYNC_ENABLE = SQL_ASYNC_ENABLE
                SQL_ATTR_CONCURRENCY = SQL_CONCURRENCY
                SQL_ATTR_CURSOR_TYPE = SQL_CURSOR_TYPE
                SQL_ATTR_ENABLE_AUTO_IPD = 15
                SQL_ATTR_FETCH_BOOKMARK_PTR = 16
                SQL_ATTR_KEYSET_SIZE = SQL_KEYSET_SIZE
                SQL_ATTR_MAX_LENGTH = SQL_MAX_LENGTH
                SQL_ATTR_MAX_ROWS = SQL_MAX_ROWS
                SQL_ATTR_NOSCAN = SQL_NOSCAN
                SQL_ATTR_PARAM_BIND_OFFSET_PTR = 17
                SQL_ATTR_PARAM_BIND_TYPE = 18
                SQL_ATTR_PARAM_OPERATION_PTR = 19
                SQL_ATTR_PARAM_STATUS_PTR = 20
                SQL_ATTR_PARAMS_PROCESSED_PTR = 21
                SQL_ATTR_PARAMSET_SIZE = 22
                SQL_ATTR_QUERY_TIMEOUT = SQL_QUERY_TIMEOUT
                SQL_ATTR_RETRIEVE_DATA = SQL_RETRIEVE_DATA
                SQL_ATTR_ROW_BIND_OFFSET_PTR = 23
                SQL_ATTR_ROW_BIND_TYPE = SQL_BIND_TYPE
                SQL_ATTR_ROW_NUMBER = SQL_ROW_NUMBER                # GetStmtAttr
                SQL_ATTR_ROW_OPERATION_PTR = 24
                SQL_ATTR_ROW_STATUS_PTR = 25
                SQL_ATTR_ROWS_FETCHED_PTR = 26
                SQL_ATTR_ROW_ARRAY_SIZE = 27
                SQL_ATTR_SIMULATE_CURSOR = SQL_SIMULATE_CURSOR
                SQL_ATTR_USE_BOOKMARKS = SQL_USE_BOOKMARKS
            # END IF  ODBCVER >= 0x0300

            if ODBCVER >= 0x0380:
                SQL_ATTR_ASYNC_STMT_EVENT = 29
            # END IF  ODBCVER >= 0x0380

            if ODBCVER < 0x0300:
                SQL_STMT_OPT_MAX = SQL_ROW_NUMBER
                SQL_STMT_OPT_MIN = SQL_QUERY_TIMEOUT
            # END IF  ODBCVER < 0x0300

            # New defines for SEARCHABLE column in SQLGetTypeInfo
            if ODBCVER >= 0x0300:
                SQL_COL_PRED_CHAR = SQL_LIKE_ONLY
                SQL_COL_PRED_BASIC = SQL_ALL_EXCEPT_LIKE
            # END IF  ODBCVER >= 0x0300

            # whether an attribute is a pointer or not
            if ODBCVER >= 0x0300:
                SQL_IS_POINTER = -4
                SQL_IS_UINTEGER = -5
                SQL_IS_INTEGER = -6
                SQL_IS_USMALLINT = -7
                SQL_IS_SMALLINT = -8
            # END IF  ODBCVER >= 0x0300

            # the value of SQL_ATTR_PARAM_BIND_TYPE
            if ODBCVER >= 0x0300:
                SQL_PARAM_BIND_BY_COLUMN = 0
                SQL_PARAM_BIND_TYPE_DEFAULT = SQL_PARAM_BIND_BY_COLUMN
            # END IF  ODBCVER >= 0x0300

            # SQL_QUERY_TIMEOUT options
            SQL_QUERY_TIMEOUT_DEFAULT = 0

            # SQL_MAX_ROWS options
            SQL_MAX_ROWS_DEFAULT = 0

            # SQL_NOSCAN options
            SQL_NOSCAN_OFF = 0            # 1.0 FALSE
            SQL_NOSCAN_ON = 1            # 1.0 TRUE
            SQL_NOSCAN_DEFAULT = SQL_NOSCAN_OFF

            # SQL_MAX_LENGTH options
            SQL_MAX_LENGTH_DEFAULT = 0

            # values for SQL_ATTR_ASYNC_ENABLE
            SQL_ASYNC_ENABLE_OFF = 0
            SQL_ASYNC_ENABLE_ON = 1
            SQL_ASYNC_ENABLE_DEFAULT = SQL_ASYNC_ENABLE_OFF

            # SQL_BIND_TYPE options
            SQL_BIND_BY_COLUMN = 0
            SQL_BIND_TYPE_DEFAULT = SQL_BIND_BY_COLUMN            # Default value

            # SQL_CONCURRENCY options
            SQL_CONCUR_READ_ONLY = 1
            SQL_CONCUR_LOCK = 2
            SQL_CONCUR_ROWVER = 3
            SQL_CONCUR_VALUES = 4
            SQL_CONCUR_DEFAULT = SQL_CONCUR_READ_ONLY            # Default value

            # SQL_CURSOR_TYPE options
            SQL_CURSOR_FORWARD_ONLY = 0
            SQL_CURSOR_KEYSET_DRIVEN = 1
            SQL_CURSOR_DYNAMIC = 2
            SQL_CURSOR_STATIC = 3
            SQL_CURSOR_TYPE_DEFAULT = SQL_CURSOR_FORWARD_ONLY            # Default value

            # SQL_ROWSET_SIZE options
            SQL_ROWSET_SIZE_DEFAULT = 1

            # SQL_KEYSET_SIZE options
            SQL_KEYSET_SIZE_DEFAULT = 0

            # SQL_SIMULATE_CURSOR options
            SQL_SC_NON_UNIQUE = 0
            SQL_SC_TRY_UNIQUE = 1
            SQL_SC_UNIQUE = 2

            # SQL_RETRIEVE_DATA options
            SQL_RD_OFF = 0
            SQL_RD_ON = 1
            SQL_RD_DEFAULT = SQL_RD_ON

            # SQL_USE_BOOKMARKS options
            SQL_UB_OFF = 0
            SQL_UB_ON = 01
            SQL_UB_DEFAULT = SQL_UB_OFF

            # New values for SQL_USE_BOOKMARKS attribute
            if ODBCVER >= 0x0300:
                SQL_UB_FIXED = SQL_UB_ON
                SQL_UB_VARIABLE = 2
            # END IF  ODBCVER >= 0x0300

            # extended descriptor field
            if ODBCVER >= 0x0300:
                SQL_DESC_ARRAY_SIZE = 20
                SQL_DESC_ARRAY_STATUS_PTR = 21
                SQL_DESC_AUTO_UNIQUE_VALUE = SQL_COLUMN_AUTO_INCREMENT
                SQL_DESC_BASE_COLUMN_NAME = 22
                SQL_DESC_BASE_TABLE_NAME = 23
                SQL_DESC_BIND_OFFSET_PTR = 24
                SQL_DESC_BIND_TYPE = 25
                SQL_DESC_CASE_SENSITIVE = SQL_COLUMN_CASE_SENSITIVE
                SQL_DESC_CATALOG_NAME = SQL_COLUMN_QUALIFIER_NAME
                SQL_DESC_CONCISE_TYPE = SQL_COLUMN_TYPE
                SQL_DESC_DATETIME_INTERVAL_PRECISION = 26
                SQL_DESC_DISPLAY_SIZE = SQL_COLUMN_DISPLAY_SIZE
                SQL_DESC_FIXED_PREC_SCALE = SQL_COLUMN_MONEY
                SQL_DESC_LABEL = SQL_COLUMN_LABEL
                SQL_DESC_LITERAL_PREFIX = 27
                SQL_DESC_LITERAL_SUFFIX = 28
                SQL_DESC_LOCAL_TYPE_NAME = 29
                SQL_DESC_MAXIMUM_SCALE = 30
                SQL_DESC_MINIMUM_SCALE = 31
                SQL_DESC_NUM_PREC_RADIX = 32
                SQL_DESC_PARAMETER_TYPE = 33
                SQL_DESC_ROWS_PROCESSED_PTR = 34
                if ODBCVER >= 0x0350:
                    SQL_DESC_ROWVER = 35
                # END IF  ODBCVER >= 0x0350

                SQL_DESC_SCHEMA_NAME = SQL_COLUMN_OWNER_NAME
                SQL_DESC_SEARCHABLE = SQL_COLUMN_SEARCHABLE
                SQL_DESC_TYPE_NAME = SQL_COLUMN_TYPE_NAME
                SQL_DESC_TABLE_NAME = SQL_COLUMN_TABLE_NAME
                SQL_DESC_UNSIGNED = SQL_COLUMN_UNSIGNED
                SQL_DESC_UPDATABLE = SQL_COLUMN_UPDATABLE
            # END IF  ODBCVER >= 0x0300

            # defines for diagnostics fields
            if ODBCVER >= 0x0300:
                SQL_DIAG_CURSOR_ROW_COUNT = -1249
                SQL_DIAG_ROW_NUMBER = -1248
                SQL_DIAG_COLUMN_NUMBER = -1247
            # END IF  ODBCVER >= 0x0300

            # SQL extended datatypes
            SQL_DATE = 9
            if ODBCVER >= 0x0300:
                SQL_INTERVAL = 10
            # END IF  ODBCVER >= 0x0300

            SQL_TIME = 10
            SQL_TIMESTAMP = 11
            SQL_LONGVARCHAR = -1
            SQL_BINARY = -2
            SQL_VARBINARY = -3
            SQL_LONGVARBINARY = -4
            SQL_BIGINT = -5
            SQL_TINYINT = -6
            SQL_BIT = -7
            if ODBCVER >= 0x0350:
                SQL_GUID = -11
            # END IF  ODBCVER >= 0x0350

            if ODBCVER >= 0x0300:
                # interval code
                SQL_CODE_YEAR = 1
                SQL_CODE_MONTH = 2
                SQL_CODE_DAY = 3
                SQL_CODE_HOUR = 4
                SQL_CODE_MINUTE = 5
                SQL_CODE_SECOND = 6
                SQL_CODE_YEAR_TO_MONTH = 7
                SQL_CODE_DAY_TO_HOUR = 8
                SQL_CODE_DAY_TO_MINUTE = 9
                SQL_CODE_DAY_TO_SECOND = 10
                SQL_CODE_HOUR_TO_MINUTE = 11
                SQL_CODE_HOUR_TO_SECOND = 12
                SQL_CODE_MINUTE_TO_SECOND = 13
                SQL_INTERVAL_YEAR = 100 + SQL_CODE_YEAR
                SQL_INTERVAL_MONTH = 100 + SQL_CODE_MONTH
                SQL_INTERVAL_DAY = 100 + SQL_CODE_DAY
                SQL_INTERVAL_HOUR = 100 + SQL_CODE_HOUR
                SQL_INTERVAL_MINUTE = 100 + SQL_CODE_MINUTE
                SQL_INTERVAL_SECOND = 100 + SQL_CODE_SECOND
                SQL_INTERVAL_YEAR_TO_MONTH = 100 + SQL_CODE_YEAR_TO_MONTH
                SQL_INTERVAL_DAY_TO_HOUR = 100 + SQL_CODE_DAY_TO_HOUR
                SQL_INTERVAL_DAY_TO_MINUTE = 100 + SQL_CODE_DAY_TO_MINUTE
                SQL_INTERVAL_DAY_TO_SECOND = 100 + SQL_CODE_DAY_TO_SECOND
                SQL_INTERVAL_HOUR_TO_MINUTE = 100 + SQL_CODE_HOUR_TO_MINUTE
                SQL_INTERVAL_HOUR_TO_SECOND = 100 + SQL_CODE_HOUR_TO_SECOND
                SQL_INTERVAL_MINUTE_TO_SECOND = 100 + SQL_CODE_MINUTE_TO_SECOND
            else:
                SQL_INTERVAL_YEAR = -80
                SQL_INTERVAL_MONTH = -81
                SQL_INTERVAL_YEAR_TO_MONTH = -82
                SQL_INTERVAL_DAY = -83
                SQL_INTERVAL_HOUR = -84
                SQL_INTERVAL_MINUTE = -85
                SQL_INTERVAL_SECOND = -86
                SQL_INTERVAL_DAY_TO_HOUR = -87
                SQL_INTERVAL_DAY_TO_MINUTE = -88
                SQL_INTERVAL_DAY_TO_SECOND = -89
                SQL_INTERVAL_HOUR_TO_MINUTE = -90
                SQL_INTERVAL_HOUR_TO_SECOND = -91
                SQL_INTERVAL_MINUTE_TO_SECOND = -92
            # END IF  ODBCVER >= 0x0300

            if ODBCVER <= 0x0300:
                SQL_UNICODE = -95
                SQL_UNICODE_VARCHAR = -96
                SQL_UNICODE_LONGVARCHAR = -97
                SQL_UNICODE_CHAR = SQL_UNICODE
            else:
                # The previous definitions for SQL_UNICODE_ are historical and
                # obsolete
                SQL_UNICODE = SQL_WCHAR
                SQL_UNICODE_VARCHAR = SQL_WVARCHAR
                SQL_UNICODE_LONGVARCHAR = SQL_WLONGVARCHAR
                SQL_UNICODE_CHAR = SQL_WCHAR
            # END IF

            if ODBCVER < 0x0300:
                SQL_TYPE_DRIVER_START = SQL_INTERVAL_YEAR
                SQL_TYPE_DRIVER_END = SQL_UNICODE_LONGVARCHAR
            # END IF  ODBCVER < 0x0300

            # /* C datatype to SQL datatype mapping SQL types
            # -------------------
            SQL_C_CHAR = SQL_CHAR            # CHAR, VARCHAR, DECIMAL, NUMERIC
            SQL_C_LONG = SQL_INTEGER            # INTEGER
            SQL_C_SHORT = SQL_SMALLINT            # SMALLINT
            SQL_C_FLOAT = SQL_REAL            # REAL
            SQL_C_DOUBLE = SQL_DOUBLE            # FLOAT, DOUBLE
            if ODBCVER >= 0x0300:
                SQL_C_NUMERIC = SQL_NUMERIC
            # END IF  ODBCVER >= 0x0300

            SQL_C_DEFAULT = 99
            SQL_SIGNED_OFFSET = -20
            SQL_UNSIGNED_OFFSET = -22

            # C datatype to SQL datatype mapping
            SQL_C_DATE = SQL_DATE
            SQL_C_TIME = SQL_TIME
            SQL_C_TIMESTAMP = SQL_TIMESTAMP
            if ODBCVER >= 0x0300:
                SQL_C_TYPE_DATE = SQL_TYPE_DATE
                SQL_C_TYPE_TIME = SQL_TYPE_TIME
                SQL_C_TYPE_TIMESTAMP = SQL_TYPE_TIMESTAMP
                SQL_C_INTERVAL_YEAR = SQL_INTERVAL_YEAR
                SQL_C_INTERVAL_MONTH = SQL_INTERVAL_MONTH
                SQL_C_INTERVAL_DAY = SQL_INTERVAL_DAY
                SQL_C_INTERVAL_HOUR = SQL_INTERVAL_HOUR
                SQL_C_INTERVAL_MINUTE = SQL_INTERVAL_MINUTE
                SQL_C_INTERVAL_SECOND = SQL_INTERVAL_SECOND
                SQL_C_INTERVAL_YEAR_TO_MONTH = SQL_INTERVAL_YEAR_TO_MONTH
                SQL_C_INTERVAL_DAY_TO_HOUR = SQL_INTERVAL_DAY_TO_HOUR
                SQL_C_INTERVAL_DAY_TO_MINUTE = SQL_INTERVAL_DAY_TO_MINUTE
                SQL_C_INTERVAL_DAY_TO_SECOND = SQL_INTERVAL_DAY_TO_SECOND
                SQL_C_INTERVAL_HOUR_TO_MINUTE = SQL_INTERVAL_HOUR_TO_MINUTE
                SQL_C_INTERVAL_HOUR_TO_SECOND = SQL_INTERVAL_HOUR_TO_SECOND
                SQL_C_INTERVAL_MINUTE_TO_SECOND = SQL_INTERVAL_MINUTE_TO_SECOND
            # END IF  ODBCVER >= 0x0300

            SQL_C_BINARY = SQL_BINARY
            SQL_C_BIT = SQL_BIT
            if ODBCVER >= 0x0300:
                SQL_C_SBIGINT = SQL_BIGINT + SQL_SIGNED_OFFSET                # SIGNED BIGINT
                SQL_C_UBIGINT = SQL_BIGINT + SQL_UNSIGNED_OFFSET                # UNSIGNED BIGINT
            # END IF  ODBCVER >= 0x0300

            SQL_C_TINYINT = SQL_TINYINT
            SQL_C_SLONG = SQL_C_LONG + SQL_SIGNED_OFFSET            # SIGNED INTEGER
            SQL_C_SSHORT = SQL_C_SHORT + SQL_SIGNED_OFFSET            # SIGNED SMALLINT
            SQL_C_STINYINT = SQL_TINYINT + SQL_SIGNED_OFFSET            # SIGNED TINYINT
            SQL_C_ULONG = SQL_C_LONG + SQL_UNSIGNED_OFFSET            # UNSIGNED INTEGER
            SQL_C_USHORT = SQL_C_SHORT + SQL_UNSIGNED_OFFSET            # UNSIGNED SMALLINT
            SQL_C_UTINYINT = SQL_TINYINT + SQL_UNSIGNED_OFFSET            # UNSIGNED TINYINT
            if defined(_WIN64):
                SQL_C_BOOKMARK = SQL_C_UBIGINT                # BOOKMARK
            else:
                SQL_C_BOOKMARK = SQL_C_ULONG                # BOOKMARK
            # END IF

            if ODBCVER >= 0x0350:
                SQL_C_GUID = SQL_GUID
            # END IF  ODBCVER >= 0x0350

            SQL_TYPE_NULL = 0
            if ODBCVER < 0x0300:
                SQL_TYPE_MIN = SQL_BIT
                SQL_TYPE_MAX = SQL_VARCHAR
            # END IF


            # base value of driver-specific C-Type (max is 0x7fff)
            # define driver-specific C-Type, named as SQL_DRIVER_C_TYPE_BASE,
            # SQL_DRIVER_C_TYPE_BASE + 1, SQL_DRIVER_C_TYPE_BASE + 2, etc.
            if ODBCVER >= 0x380:
                SQL_DRIVER_C_TYPE_BASE = 0x4000
            # END IF


            # base value of driver-specific fields/attributes
            # (max are 0x7fff [16-bit] or 0x00007fff [32-bit])
            # define driver-specific SQL-Type, named as
            # SQL_DRIVER_SQL_TYPE_BASE,
            # SQL_DRIVER_SQL_TYPE_BASE + 1, SQL_DRIVER_SQL_TYPE_BASE + 2, etc.
            # Please note that there is no runtime change in this version of
            # DM.
            # However, we suggest that driver manufacturers adhere to this
            # range
            # as future versions of the DM may enforce these constraints
            if ODBCVER >= 0x380:
                SQL_DRIVER_SQL_TYPE_BASE = 0x4000
                SQL_DRIVER_DESC_FIELD_BASE = 0x4000
                SQL_DRIVER_DIAG_FIELD_BASE = 0x4000
                SQL_DRIVER_INFO_TYPE_BASE = 0x4000
                SQL_DRIVER_CONN_ATTR_BASE = 0x00004000                # 32-bit
                SQL_DRIVER_STMT_ATTR_BASE = 0x00004000                # 32-bit
            # END IF


            if ODBCVER >= 0x0300:
                SQL_C_VARBOOKMARK = SQL_C_BINARY
            # END IF  ODBCVER >= 0x0300

            # define for SQL_DIAG_ROW_NUMBER and SQL_DIAG_COLUMN_NUMBER
            if ODBCVER >= 0x0300:
                SQL_NO_ROW_NUMBER = -1
                SQL_NO_COLUMN_NUMBER = -1
                SQL_ROW_NUMBER_UNKNOWN = -2
                SQL_COLUMN_NUMBER_UNKNOWN = -2
            # END IF


            # SQLBindParameter extensions
            SQL_DEFAULT_PARAM = -5
            SQL_IGNORE = -6
            if ODBCVER >= 0x0300:
                SQL_COLUMN_IGNORE = SQL_IGNORE
            # END IF  ODBCVER >= 0x0300

            SQL_LEN_DATA_AT_EXEC_OFFSET = -100


            def SQL_LEN_DATA_AT_EXEC(length):
                return -length + SQL_LEN_DATA_AT_EXEC_OFFSET

            # binary length for driver specific attributes
            SQL_LEN_BINARY_ATTR_OFFSET = -100


            def SQL_LEN_BINARY_ATTR(length):
                return -length + SQL_LEN_BINARY_ATTR_OFFSET

            # /* Defines used by Driver Manager when mapping SQLSetParam to
            # SQLBindParameter
            SQL_PARAM_TYPE_DEFAULT = SQL_PARAM_INPUT_OUTPUT
            SQL_SETPARAM_VALUE_MAX = -1


            SQL_COLATT_OPT_MAX = SQL_COLUMN_LABEL
            if ODBCVER < 0x0300:
                SQL_COLUMN_DRIVER_START = 1000
            # END IF  ODBCVER < 0x0300

            SQL_COLATT_OPT_MIN = SQL_COLUMN_COUNT

            # SQLColAttributes subdefines for SQL_COLUMN_UPDATABLE
            SQL_ATTR_READONLY = 0
            SQL_ATTR_WRITE = 1
            SQL_ATTR_READWRITE_UNKNOWN = 2


            # Special return values for SQLGetData
            SQL_NO_TOTAL = -4

            # ****************************************
            # SQLGetFunctions: additional values for
            # fFunction to represent functions that
            # are not in the X/Open spec.
            # ****************************************
            if ODBCVER >= 0x0300:
                SQL_API_SQLALLOCHANDLESTD = 73
                SQL_API_SQLBULKOPERATIONS = 24
            # END IF  ODBCVER >= 0x0300

            SQL_API_SQLBINDPARAMETER = 72
            SQL_API_SQLBROWSECONNECT = 55
            SQL_API_SQLCOLATTRIBUTES = 6
            SQL_API_SQLCOLUMNPRIVILEGES = 56
            SQL_API_SQLDESCRIBEPARAM = 58
            SQL_API_SQLDRIVERCONNECT = 41
            SQL_API_SQLDRIVERS = 71
            SQL_API_SQLPRIVATEDRIVERS = 79
            SQL_API_SQLEXTENDEDFETCH = 59
            SQL_API_SQLFOREIGNKEYS = 60
            SQL_API_SQLMORERESULTS = 61
            SQL_API_SQLNATIVESQL = 62
            SQL_API_SQLNUMPARAMS = 63
            SQL_API_SQLPARAMOPTIONS = 64
            SQL_API_SQLPRIMARYKEYS = 65
            SQL_API_SQLPROCEDURECOLUMNS = 66
            SQL_API_SQLPROCEDURES = 67
            SQL_API_SQLSETPOS = 68
            SQL_API_SQLSETSCROLLOPTIONS = 69
            SQL_API_SQLTABLEPRIVILEGES = 70

            # -------------------------------------------
            # SQL_EXT_API_LAST is not useful with ODBC
            # version 3.0 because some of the values
            # from X/Open are in the 10000 range.
            # -------------------------------------------
            if ODBCVER < 0x0300:
                SQL_EXT_API_LAST = SQL_API_SQLBINDPARAMETER
                SQL_NUM_FUNCTIONS = 23
                SQL_EXT_API_START = 40
                SQL_NUM_EXTENSIONS = SQL_EXT_API_LAST-SQL_EXT_API_START + 1
            # END IF

            # --------------------------------------------
            # SQL_API_ALL_FUNCTIONS returns an array
            # of 'booleans' representing whether a
            # function is implemented by the driver.
            #
            # CAUTION: Only functions defined in ODBC
            # version 2.0 and earlier are returned, the
            # new high-range function numbers defined by
            # X/Open break this scheme. See the new
            # method -- SQL_API_ODBC3_ALL_FUNCTIONS
            # --------------------------------------------
            SQL_API_ALL_FUNCTIONS = 0            # See CAUTION above

            # ----------------------------------------------
            # 2.X drivers export a dummy function with
            # ordinal number SQL_API_LOADBYORDINAL to speed
            # loading under the windows operating system.
            #
            # CAUTION: Loading by ordinal is not supported
            # for 3.0 and above drivers.
            # ----------------------------------------------
            SQL_API_LOADBYORDINAL = 199            # See CAUTION above

            # ----------------------------------------------
            # SQL_API_ODBC3_ALL_FUNCTIONS
            # This returns a bitmap, which allows us to
            # handle the higher-valued function numbers.
            # Use SQL_FUNC_EXISTS(bitmap,function_number)
            # to determine if the function exists.
            # ----------------------------------------------
            if ODBCVER >= 0x0300:
                SQL_API_ODBC3_ALL_FUNCTIONS = 999
                SQL_API_ODBC3_ALL_FUNCTIONS_SIZE = 250                # array of 250 words


                def SQL_FUNC_EXISTS(pfExists, uwAPI):
                    if (pfExists + (uwAPI >> 4)) & (1 << (uwAPI & 0x000F)):
                        return SQL_TRUE
                    else:
                        return SQL_FALSE


            # END IF  ODBCVER >= 0x0300
            # ********************************************
            # Extended definitions for SQLGetInfo
            # ********************************************
            # ---------------------------------
            # Values in ODBC 2.0 that are not
            # in the X/Open spec
            # ---------------------------------
            SQL_INFO_FIRST = 0
            SQL_ACTIVE_CONNECTIONS = 0            # MAX_DRIVER_CONNECTIONS
            SQL_ACTIVE_STATEMENTS = 1            # MAX_CONCURRENT_ACTIVITIES
            SQL_DRIVER_HDBC = 3
            SQL_DRIVER_HENV = 4
            SQL_DRIVER_HSTMT = 5
            SQL_DRIVER_NAME = 6
            SQL_DRIVER_VER = 7
            SQL_ODBC_API_CONFORMANCE = 9
            SQL_ODBC_VER = 10
            SQL_ROW_UPDATES = 11
            SQL_ODBC_SAG_CLI_CONFORMANCE = 12
            SQL_ODBC_SQL_CONFORMANCE = 15
            SQL_PROCEDURES = 21
            SQL_CONCAT_NULL_BEHAVIOR = 22
            SQL_CURSOR_ROLLBACK_BEHAVIOR = 24
            SQL_EXPRESSIONS_IN_ORDERBY = 27
            SQL_MAX_OWNER_NAME_LEN = 32            # MAX_SCHEMA_NAME_LEN
            SQL_MAX_PROCEDURE_NAME_LEN = 33
            SQL_MAX_QUALIFIER_NAME_LEN = 34            # MAX_CATALOG_NAME_LEN
            SQL_MULT_RESULT_SETS = 36
            SQL_MULTIPLE_ACTIVE_TXN = 37
            SQL_OUTER_JOINS = 38
            SQL_OWNER_TERM = 39
            SQL_PROCEDURE_TERM = 40
            SQL_QUALIFIER_NAME_SEPARATOR = 41
            SQL_QUALIFIER_TERM = 42
            SQL_SCROLL_OPTIONS = 44
            SQL_TABLE_TERM = 45
            SQL_CONVERT_FUNCTIONS = 48
            SQL_NUMERIC_FUNCTIONS = 49
            SQL_STRING_FUNCTIONS = 50
            SQL_SYSTEM_FUNCTIONS = 51
            SQL_TIMEDATE_FUNCTIONS = 52
            SQL_CONVERT_BIGINT = 53
            SQL_CONVERT_BINARY = 54
            SQL_CONVERT_BIT = 55
            SQL_CONVERT_CHAR = 56
            SQL_CONVERT_DATE = 57
            SQL_CONVERT_DECIMAL = 58
            SQL_CONVERT_DOUBLE = 59
            SQL_CONVERT_FLOAT = 60
            SQL_CONVERT_INTEGER = 61
            SQL_CONVERT_LONGVARCHAR = 62
            SQL_CONVERT_NUMERIC = 63
            SQL_CONVERT_REAL = 64
            SQL_CONVERT_SMALLINT = 65
            SQL_CONVERT_TIME = 66
            SQL_CONVERT_TIMESTAMP = 67
            SQL_CONVERT_TINYINT = 68
            SQL_CONVERT_VARBINARY = 69
            SQL_CONVERT_VARCHAR = 70
            SQL_CONVERT_LONGVARBINARY = 71
            SQL_ODBC_SQL_OPT_IEF = 73            # SQL_INTEGRITY
            SQL_CORRELATION_NAME = 74
            SQL_NON_NULLABLE_COLUMNS = 75
            SQL_DRIVER_HLIB = 76
            SQL_DRIVER_ODBC_VER = 77
            SQL_LOCK_TYPES = 78
            SQL_POS_OPERATIONS = 79
            SQL_POSITIONED_STATEMENTS = 80
            SQL_BOOKMARK_PERSISTENCE = 82
            SQL_STATIC_SENSITIVITY = 83
            SQL_FILE_USAGE = 84
            SQL_COLUMN_ALIAS = 87
            SQL_GROUP_BY = 88
            SQL_KEYWORDS = 89
            SQL_OWNER_USAGE = 91
            SQL_QUALIFIER_USAGE = 92
            SQL_QUOTED_IDENTIFIER_CASE = 93
            SQL_SUBQUERIES = 95
            SQL_UNION = 96
            SQL_MAX_ROW_SIZE_INCLUDES_LONG = 103
            SQL_MAX_CHAR_LITERAL_LEN = 108
            SQL_TIMEDATE_ADD_INTERVALS = 109
            SQL_TIMEDATE_DIFF_INTERVALS = 110
            SQL_NEED_LONG_DATA_LEN = 111
            SQL_MAX_BINARY_LITERAL_LEN = 112
            SQL_LIKE_ESCAPE_CLAUSE = 113
            SQL_QUALIFIER_LOCATION = 114
            if ODBCVER >= 0x0201 and ODBCVER < 0x0300:
                SQL_OJ_CAPABILITIES = 65003                # Temp value until ODBC 3.0
            # END IF  ODBCVER >= 0x0201 and ODBCVER < 0x0300

            # ----------------------------------------------
            # SQL_INFO_LAST and SQL_INFO_DRIVER_START are
            # not useful anymore, because X/Open has
            # values in the 10000 range. You
            # must contact X/Open directly to get a range
            # of numbers for driver-specific values.
            # ----------------------------------------------
            if ODBCVER < 0x0300:
                SQL_INFO_LAST = SQL_QUALIFIER_LOCATION
                SQL_INFO_DRIVER_START = 1000
            # END IF  ODBCVER < 0x0300

            # -----------------------------------------------
            # ODBC 3.0 SQLGetInfo values that are not part
            # of the X/Open standard at this time. X/Open
            # standard values are in sql.h.
            # -----------------------------------------------
            if ODBCVER >= 0x0300:
                SQL_ACTIVE_ENVIRONMENTS = 116
                SQL_ALTER_DOMAIN = 117
                SQL_SQL_CONFORMANCE = 118
                SQL_DATETIME_LITERALS = 119
                SQL_ASYNC_MODE = 10021                # new X/Open spec
                SQL_BATCH_ROW_COUNT = 120
                SQL_BATCH_SUPPORT = 121
                SQL_CATALOG_LOCATION = SQL_QUALIFIER_LOCATION
                SQL_CATALOG_NAME_SEPARATOR = SQL_QUALIFIER_NAME_SEPARATOR
                SQL_CATALOG_TERM = SQL_QUALIFIER_TERM
                SQL_CATALOG_USAGE = SQL_QUALIFIER_USAGE
                SQL_CONVERT_WCHAR = 122
                SQL_CONVERT_INTERVAL_DAY_TIME = 123
                SQL_CONVERT_INTERVAL_YEAR_MONTH = 124
                SQL_CONVERT_WLONGVARCHAR = 125
                SQL_CONVERT_WVARCHAR = 126
                SQL_CREATE_ASSERTION = 127
                SQL_CREATE_CHARACTER_SET = 128
                SQL_CREATE_COLLATION = 129
                SQL_CREATE_DOMAIN = 130
                SQL_CREATE_SCHEMA = 131
                SQL_CREATE_TABLE = 132
                SQL_CREATE_TRANSLATION = 133
                SQL_CREATE_VIEW = 134
                SQL_DRIVER_HDESC = 135
                SQL_DROP_ASSERTION = 136
                SQL_DROP_CHARACTER_SET = 137
                SQL_DROP_COLLATION = 138
                SQL_DROP_DOMAIN = 139
                SQL_DROP_SCHEMA = 140
                SQL_DROP_TABLE = 141
                SQL_DROP_TRANSLATION = 142
                SQL_DROP_VIEW = 143
                SQL_DYNAMIC_CURSOR_ATTRIBUTES1 = 144
                SQL_DYNAMIC_CURSOR_ATTRIBUTES2 = 145
                SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1 = 146
                SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES2 = 147
                SQL_INDEX_KEYWORDS = 148
                SQL_INFO_SCHEMA_VIEWS = 149
                SQL_KEYSET_CURSOR_ATTRIBUTES1 = 150
                SQL_KEYSET_CURSOR_ATTRIBUTES2 = 151
                SQL_MAX_ASYNC_CONCURRENT_STATEMENTS = 10022                # new X/Open spec
                SQL_ODBC_INTERFACE_CONFORMANCE = 152
                SQL_PARAM_ARRAY_ROW_COUNTS = 153
                SQL_PARAM_ARRAY_SELECTS = 154
                SQL_SCHEMA_TERM = SQL_OWNER_TERM
                SQL_SCHEMA_USAGE = SQL_OWNER_USAGE
                SQL_SQL92_DATETIME_FUNCTIONS = 155
                SQL_SQL92_FOREIGN_KEY_DELETE_RULE = 156
                SQL_SQL92_FOREIGN_KEY_UPDATE_RULE = 157
                SQL_SQL92_GRANT = 158
                SQL_SQL92_NUMERIC_VALUE_FUNCTIONS = 159
                SQL_SQL92_PREDICATES = 160
                SQL_SQL92_RELATIONAL_JOIN_OPERATORS = 161
                SQL_SQL92_REVOKE = 162
                SQL_SQL92_ROW_VALUE_CONSTRUCTOR = 163
                SQL_SQL92_STRING_FUNCTIONS = 164
                SQL_SQL92_VALUE_EXPRESSIONS = 165
                SQL_STANDARD_CLI_CONFORMANCE = 166
                SQL_STATIC_CURSOR_ATTRIBUTES1 = 167
                SQL_STATIC_CURSOR_ATTRIBUTES2 = 168
                SQL_AGGREGATE_FUNCTIONS = 169
                SQL_DDL_INDEX = 170
                SQL_DM_VER = 171
                SQL_INSERT_STATEMENT = 172
                SQL_CONVERT_GUID = 173
                SQL_UNION_STATEMENT = SQL_UNION
                if ODBCVER >= 0x0380:
                    # Info Types
                    SQL_ASYNC_DBC_FUNCTIONS = 10023
                # END IF   ODBCVER >= 0x0380

                SQL_DRIVER_AWARE_POOLING_SUPPORTED = 10024
                if ODBCVER >= 0x0380:
                    SQL_ASYNC_NOTIFICATION = 10025

                    # Possible values for SQL_ASYNC_NOTIFICATION
                    SQL_ASYNC_NOTIFICATION_NOT_CAPABLE = 0x00000000
                    SQL_ASYNC_NOTIFICATION_CAPABLE = 0x00000001
                # END IF   ODBCVER >= 0x0380
            # END IF  ODBCVER >= 0x0300

            SQL_DTC_TRANSITION_COST = 1750

            # SQL_ALTER_TABLE bitmasks
                # /* the following 5 bitmasks are defined in sql.h define
                # SQL_AT_ADD_COLUMN 0x00000001 define SQL_AT_DROP_COLUMN
                # 0x00000002 define SQL_AT_ADD_CONSTRAINT 0x00000008
            if ODBCVER >= 0x0300:
                SQL_AT_ADD_COLUMN_SINGLE = 0x00000020
                SQL_AT_ADD_COLUMN_DEFAULT = 0x00000040
                SQL_AT_ADD_COLUMN_COLLATION = 0x00000080
                SQL_AT_SET_COLUMN_DEFAULT = 0x00000100
                SQL_AT_DROP_COLUMN_DEFAULT = 0x00000200
                SQL_AT_DROP_COLUMN_CASCADE = 0x00000400
                SQL_AT_DROP_COLUMN_RESTRICT = 0x00000800
                SQL_AT_ADD_TABLE_CONSTRAINT = 0x00001000
                SQL_AT_DROP_TABLE_CONSTRAINT_CASCADE = 0x00002000
                SQL_AT_DROP_TABLE_CONSTRAINT_RESTRICT = 0x00004000
                SQL_AT_CONSTRAINT_NAME_DEFINITION = 0x00008000
                SQL_AT_CONSTRAINT_INITIALLY_DEFERRED = 0x00010000
                SQL_AT_CONSTRAINT_INITIALLY_IMMEDIATE = 0x00020000
                SQL_AT_CONSTRAINT_DEFERRABLE = 0x00040000
                SQL_AT_CONSTRAINT_NON_DEFERRABLE = 0x00080000
            # END IF  ODBCVER >= 0x0300

            # SQL_CONVERT_* return value bitmasks
            SQL_CVT_CHAR = 0x00000001
            SQL_CVT_NUMERIC = 0x00000002
            SQL_CVT_DECIMAL = 0x00000004
            SQL_CVT_INTEGER = 0x00000008
            SQL_CVT_SMALLINT = 0x00000010
            SQL_CVT_FLOAT = 0x00000020
            SQL_CVT_REAL = 0x00000040
            SQL_CVT_DOUBLE = 0x00000080
            SQL_CVT_VARCHAR = 0x00000100
            SQL_CVT_LONGVARCHAR = 0x00000200
            SQL_CVT_BINARY = 0x00000400
            SQL_CVT_VARBINARY = 0x00000800
            SQL_CVT_BIT = 0x00001000
            SQL_CVT_TINYINT = 0x00002000
            SQL_CVT_BIGINT = 0x00004000
            SQL_CVT_DATE = 0x00008000
            SQL_CVT_TIME = 0x00010000
            SQL_CVT_TIMESTAMP = 0x00020000
            SQL_CVT_LONGVARBINARY = 0x00040000
            if ODBCVER >= 0x0300:
                SQL_CVT_INTERVAL_YEAR_MONTH = 0x00080000
                SQL_CVT_INTERVAL_DAY_TIME = 0x00100000
                SQL_CVT_WCHAR = 0x00200000
                SQL_CVT_WLONGVARCHAR = 0x00400000
                SQL_CVT_WVARCHAR = 0x00800000
                SQL_CVT_GUID = 0x01000000
            # END IF  ODBCVER >= 0x0300

            # SQL_CONVERT_FUNCTIONS functions
            SQL_FN_CVT_CONVERT = 0x00000001
            if ODBCVER >= 0x0300:
                SQL_FN_CVT_CAST = 0x00000002
            # END IF  ODBCVER >= 0x0300

            # SQL_STRING_FUNCTIONS functions
            SQL_FN_STR_CONCAT = 0x00000001
            SQL_FN_STR_INSERT = 0x00000002
            SQL_FN_STR_LEFT = 0x00000004
            SQL_FN_STR_LTRIM = 0x00000008
            SQL_FN_STR_LENGTH = 0x00000010
            SQL_FN_STR_LOCATE = 0x00000020
            SQL_FN_STR_LCASE = 0x00000040
            SQL_FN_STR_REPEAT = 0x00000080
            SQL_FN_STR_REPLACE = 0x00000100
            SQL_FN_STR_RIGHT = 0x00000200
            SQL_FN_STR_RTRIM = 0x00000400
            SQL_FN_STR_SUBSTRING = 0x00000800
            SQL_FN_STR_UCASE = 0x00001000
            SQL_FN_STR_ASCII = 0x00002000
            SQL_FN_STR_CHAR = 0x00004000
            SQL_FN_STR_DIFFERENCE = 0x00008000
            SQL_FN_STR_LOCATE_2 = 0x00010000
            SQL_FN_STR_SOUNDEX = 0x00020000
            SQL_FN_STR_SPACE = 0x00040000
            if ODBCVER >= 0x0300:
                SQL_FN_STR_BIT_LENGTH = 0x00080000
                SQL_FN_STR_CHAR_LENGTH = 0x00100000
                SQL_FN_STR_CHARACTER_LENGTH = 0x00200000
                SQL_FN_STR_OCTET_LENGTH = 0x00400000
                SQL_FN_STR_POSITION = 0x00800000
            # END IF  ODBCVER >= 0x0300

            # SQL_SQL92_STRING_FUNCTIONS
            if ODBCVER >= 0x0300:
                SQL_SSF_CONVERT = 0x00000001
                SQL_SSF_LOWER = 0x00000002
                SQL_SSF_UPPER = 0x00000004
                SQL_SSF_SUBSTRING = 0x00000008
                SQL_SSF_TRANSLATE = 0x00000010
                SQL_SSF_TRIM_BOTH = 0x00000020
                SQL_SSF_TRIM_LEADING = 0x00000040
                SQL_SSF_TRIM_TRAILING = 0x00000080
            # END IF  ODBCVER >= 0x0300

            # SQL_NUMERIC_FUNCTIONS functions
            SQL_FN_NUM_ABS = 0x00000001
            SQL_FN_NUM_ACOS = 0x00000002
            SQL_FN_NUM_ASIN = 0x00000004
            SQL_FN_NUM_ATAN = 0x00000008
            SQL_FN_NUM_ATAN2 = 0x00000010
            SQL_FN_NUM_CEILING = 0x00000020
            SQL_FN_NUM_COS = 0x00000040
            SQL_FN_NUM_COT = 0x00000080
            SQL_FN_NUM_EXP = 0x00000100
            SQL_FN_NUM_FLOOR = 0x00000200
            SQL_FN_NUM_LOG = 0x00000400
            SQL_FN_NUM_MOD = 0x00000800
            SQL_FN_NUM_SIGN = 0x00001000
            SQL_FN_NUM_SIN = 0x00002000
            SQL_FN_NUM_SQRT = 0x00004000
            SQL_FN_NUM_TAN = 0x00008000
            SQL_FN_NUM_PI = 0x00010000
            SQL_FN_NUM_RAND = 0x00020000
            SQL_FN_NUM_DEGREES = 0x00040000
            SQL_FN_NUM_LOG10 = 0x00080000
            SQL_FN_NUM_POWER = 0x00100000
            SQL_FN_NUM_RADIANS = 0x00200000
            SQL_FN_NUM_ROUND = 0x00400000
            SQL_FN_NUM_TRUNCATE = 0x00800000

            # SQL_SQL92_NUMERIC_VALUE_FUNCTIONS
            if ODBCVER >= 0x0300:
                SQL_SNVF_BIT_LENGTH = 0x00000001
                SQL_SNVF_CHAR_LENGTH = 0x00000002
                SQL_SNVF_CHARACTER_LENGTH = 0x00000004
                SQL_SNVF_EXTRACT = 0x00000008
                SQL_SNVF_OCTET_LENGTH = 0x00000010
                SQL_SNVF_POSITION = 0x00000020
            # END IF  ODBCVER >= 0x0300

            # SQL_TIMEDATE_FUNCTIONS functions
            SQL_FN_TD_NOW = 0x00000001
            SQL_FN_TD_CURDATE = 0x00000002
            SQL_FN_TD_DAYOFMONTH = 0x00000004
            SQL_FN_TD_DAYOFWEEK = 0x00000008
            SQL_FN_TD_DAYOFYEAR = 0x00000010
            SQL_FN_TD_MONTH = 0x00000020
            SQL_FN_TD_QUARTER = 0x00000040
            SQL_FN_TD_WEEK = 0x00000080
            SQL_FN_TD_YEAR = 0x00000100
            SQL_FN_TD_CURTIME = 0x00000200
            SQL_FN_TD_HOUR = 0x00000400
            SQL_FN_TD_MINUTE = 0x00000800
            SQL_FN_TD_SECOND = 0x00001000
            SQL_FN_TD_TIMESTAMPADD = 0x00002000
            SQL_FN_TD_TIMESTAMPDIFF = 0x00004000
            SQL_FN_TD_DAYNAME = 0x00008000
            SQL_FN_TD_MONTHNAME = 0x00010000
            if ODBCVER >= 0x0300:
                SQL_FN_TD_CURRENT_DATE = 0x00020000
                SQL_FN_TD_CURRENT_TIME = 0x00040000
                SQL_FN_TD_CURRENT_TIMESTAMP = 0x00080000
                SQL_FN_TD_EXTRACT = 0x00100000
            # END IF  ODBCVER >= 0x0300

            # SQL_SQL92_DATETIME_FUNCTIONS
            if ODBCVER >= 0x0300:
                SQL_SDF_CURRENT_DATE = 0x00000001
                SQL_SDF_CURRENT_TIME = 0x00000002
                SQL_SDF_CURRENT_TIMESTAMP = 0x00000004
            # END IF  ODBCVER >= 0x0300

            # SQL_SYSTEM_FUNCTIONS functions
            SQL_FN_SYS_USERNAME = 0x00000001
            SQL_FN_SYS_DBNAME = 0x00000002
            SQL_FN_SYS_IFNULL = 0x00000004

            # SQL_TIMEDATE_ADD_INTERVALS and SQL_TIMEDATE_DIFF_INTERVALS
            # functions
            SQL_FN_TSI_FRAC_SECOND = 0x00000001
            SQL_FN_TSI_SECOND = 0x00000002
            SQL_FN_TSI_MINUTE = 0x00000004
            SQL_FN_TSI_HOUR = 0x00000008
            SQL_FN_TSI_DAY = 0x00000010
            SQL_FN_TSI_WEEK = 0x00000020
            SQL_FN_TSI_MONTH = 0x00000040
            SQL_FN_TSI_QUARTER = 0x00000080
            SQL_FN_TSI_YEAR = 0x00000100

            # /* bitmasks for SQL_DYNAMIC_CURSOR_ATTRIBUTES1,
            # SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES1,
            # SQL_KEYSET_CURSOR_ATTRIBUTES1, and SQL_STATIC_CURSOR_ATTRIBUTES1
            if ODBCVER >= 0x0300:
                # supported SQLFetchScroll FetchOrientation's
                SQL_CA1_NEXT = 0x00000001
                SQL_CA1_ABSOLUTE = 0x00000002
                SQL_CA1_RELATIVE = 0x00000004
                SQL_CA1_BOOKMARK = 0x00000008

                # supported SQLSetPos LockType's
                SQL_CA1_LOCK_NO_CHANGE = 0x00000040
                SQL_CA1_LOCK_EXCLUSIVE = 0x00000080
                SQL_CA1_LOCK_UNLOCK = 0x00000100

                # supported SQLSetPos Operations
                SQL_CA1_POS_POSITION = 0x00000200
                SQL_CA1_POS_UPDATE = 0x00000400
                SQL_CA1_POS_DELETE = 0x00000800
                SQL_CA1_POS_REFRESH = 0x00001000

                # positioned updates and deletes
                SQL_CA1_POSITIONED_UPDATE = 0x00002000
                SQL_CA1_POSITIONED_DELETE = 0x00004000
                SQL_CA1_SELECT_FOR_UPDATE = 0x00008000

                # supported SQLBulkOperations operations
                SQL_CA1_BULK_ADD = 0x00010000
                SQL_CA1_BULK_UPDATE_BY_BOOKMARK = 0x00020000
                SQL_CA1_BULK_DELETE_BY_BOOKMARK = 0x00040000
                SQL_CA1_BULK_FETCH_BY_BOOKMARK = 0x00080000
            # END IF  ODBCVER >= 0x0300

            # /* bitmasks for SQL_DYNAMIC_CURSOR_ATTRIBUTES2,
            # SQL_FORWARD_ONLY_CURSOR_ATTRIBUTES2,
            # SQL_KEYSET_CURSOR_ATTRIBUTES2, and SQL_STATIC_CURSOR_ATTRIBUTES2
            if ODBCVER >= 0x0300:
                # supported values for SQL_ATTR_SCROLL_CONCURRENCY
                SQL_CA2_READ_ONLY_CONCURRENCY = 0x00000001
                SQL_CA2_LOCK_CONCURRENCY = 0x00000002
                SQL_CA2_OPT_ROWVER_CONCURRENCY = 0x00000004
                SQL_CA2_OPT_VALUES_CONCURRENCY = 0x00000008

                # sensitivity of the cursor to its own inserts, deletes, and
                # updates
                SQL_CA2_SENSITIVITY_ADDITIONS = 0x00000010
                SQL_CA2_SENSITIVITY_DELETIONS = 0x00000020
                SQL_CA2_SENSITIVITY_UPDATES = 0x00000040

                # semantics of SQL_ATTR_MAX_ROWS
                SQL_CA2_MAX_ROWS_SELECT = 0x00000080
                SQL_CA2_MAX_ROWS_INSERT = 0x00000100
                SQL_CA2_MAX_ROWS_DELETE = 0x00000200
                SQL_CA2_MAX_ROWS_UPDATE = 0x00000400
                SQL_CA2_MAX_ROWS_CATALOG = 0x00000800
                SQL_CA2_MAX_ROWS_AFFECTS_ALL = (
                    SQL_CA2_MAX_ROWS_SELECT |
                    SQL_CA2_MAX_ROWS_INSERT |
                    SQL_CA2_MAX_ROWS_DELETE |
                    SQL_CA2_MAX_ROWS_UPDATE |
                    SQL_CA2_MAX_ROWS_CATALOG
                )

                # semantics of SQL_DIAG_CURSOR_ROW_COUNT
                SQL_CA2_CRC_EXACT = 0x00001000
                SQL_CA2_CRC_APPROXIMATE = 0x00002000

                # the kinds of positioned statements that can be simulated
                SQL_CA2_SIMULATE_NON_UNIQUE = 0x00004000
                SQL_CA2_SIMULATE_TRY_UNIQUE = 0x00008000
                SQL_CA2_SIMULATE_UNIQUE = 0x00010000
            # END IF  ODBCVER >= 0x0300

            # SQL_ODBC_API_CONFORMANCE values
            SQL_OAC_NONE = 0x0000
            SQL_OAC_LEVEL1 = 0x0001
            SQL_OAC_LEVEL2 = 0x0002

            # SQL_ODBC_SAG_CLI_CONFORMANCE values
            SQL_OSCC_NOT_COMPLIANT = 0x0000
            SQL_OSCC_COMPLIANT = 0x0001

            # SQL_ODBC_SQL_CONFORMANCE values
            SQL_OSC_MINIMUM = 0x0000
            SQL_OSC_CORE = 0x0001
            SQL_OSC_EXTENDED = 0x0002

            # SQL_CONCAT_NULL_BEHAVIOR values
            SQL_CB_NULL = 0x0000
            SQL_CB_NON_NULL = 0x0001

            # SQL_SCROLL_OPTIONS masks
            SQL_SO_FORWARD_ONLY = 0x00000001
            SQL_SO_KEYSET_DRIVEN = 0x00000002
            SQL_SO_DYNAMIC = 0x00000004
            SQL_SO_MIXED = 0x00000008
            SQL_SO_STATIC = 0x00000010

            # SQL_FETCH_DIRECTION masks
            # /* SQL_FETCH_RESUME is no longer supported define
            # SQL_FD_FETCH_RESUME 0x00000040
            SQL_FD_FETCH_BOOKMARK = 0x00000080

            # SQL_TXN_ISOLATION_OPTION masks
            # /* SQL_TXN_VERSIONING is no longer supported define
            # SQL_TXN_VERSIONING 0x00000010
            # SQL_CORRELATION_NAME values
            SQL_CN_NONE = 0x0000
            SQL_CN_DIFFERENT = 0x0001
            SQL_CN_ANY = 0x0002

            # SQL_NON_NULLABLE_COLUMNS values
            SQL_NNC_NULL = 0x0000
            SQL_NNC_NON_NULL = 0x0001

            # SQL_NULL_COLLATION values
            SQL_NC_START = 0x0002
            SQL_NC_END = 0x0004

            # SQL_FILE_USAGE values
            SQL_FILE_NOT_SUPPORTED = 0x0000
            SQL_FILE_TABLE = 0x0001
            SQL_FILE_QUALIFIER = 0x0002
            SQL_FILE_CATALOG = SQL_FILE_QUALIFIER            # ODBC 3.0

            # SQL_GETDATA_EXTENSIONS values
            SQL_GD_BLOCK = 0x00000004
            SQL_GD_BOUND = 0x00000008
            if ODBCVER >= 0x0380:
                SQL_GD_OUTPUT_PARAMS = 0x00000010
            # END IF


            # SQL_POSITIONED_STATEMENTS masks
            SQL_PS_POSITIONED_DELETE = 0x00000001
            SQL_PS_POSITIONED_UPDATE = 0x00000002
            SQL_PS_SELECT_FOR_UPDATE = 0x00000004

            # SQL_GROUP_BY values
            SQL_GB_NOT_SUPPORTED = 0x0000
            SQL_GB_GROUP_BY_EQUALS_SELECT = 0x0001
            SQL_GB_GROUP_BY_CONTAINS_SELECT = 0x0002
            SQL_GB_NO_RELATION = 0x0003
            if ODBCVER >= 0x0300:
                SQL_GB_COLLATE = 0x0004
            # END IF  ODBCVER >= 0x0300

            # SQL_OWNER_USAGE masks
            SQL_OU_DML_STATEMENTS = 0x00000001
            SQL_OU_PROCEDURE_INVOCATION = 0x00000002
            SQL_OU_TABLE_DEFINITION = 0x00000004
            SQL_OU_INDEX_DEFINITION = 0x00000008
            SQL_OU_PRIVILEGE_DEFINITION = 0x00000010

            # SQL_SCHEMA_USAGE masks
            if ODBCVER >= 0x0300:
                SQL_SU_DML_STATEMENTS = SQL_OU_DML_STATEMENTS
                SQL_SU_PROCEDURE_INVOCATION = SQL_OU_PROCEDURE_INVOCATION
                SQL_SU_TABLE_DEFINITION = SQL_OU_TABLE_DEFINITION
                SQL_SU_INDEX_DEFINITION = SQL_OU_INDEX_DEFINITION
                SQL_SU_PRIVILEGE_DEFINITION = SQL_OU_PRIVILEGE_DEFINITION
            # END IF  ODBCVER >= 0x0300

            # SQL_QUALIFIER_USAGE masks
            SQL_QU_DML_STATEMENTS = 0x00000001
            SQL_QU_PROCEDURE_INVOCATION = 0x00000002
            SQL_QU_TABLE_DEFINITION = 0x00000004
            SQL_QU_INDEX_DEFINITION = 0x00000008
            SQL_QU_PRIVILEGE_DEFINITION = 0x00000010
            if ODBCVER >= 0x0300:
                # SQL_CATALOG_USAGE masks
                SQL_CU_DML_STATEMENTS = SQL_QU_DML_STATEMENTS
                SQL_CU_PROCEDURE_INVOCATION = SQL_QU_PROCEDURE_INVOCATION
                SQL_CU_TABLE_DEFINITION = SQL_QU_TABLE_DEFINITION
                SQL_CU_INDEX_DEFINITION = SQL_QU_INDEX_DEFINITION
                SQL_CU_PRIVILEGE_DEFINITION = SQL_QU_PRIVILEGE_DEFINITION
            # END IF  ODBCVER >= 0x0300

            # SQL_SUBQUERIES masks
            SQL_SQ_COMPARISON = 0x00000001
            SQL_SQ_EXISTS = 0x00000002
            SQL_SQ_IN = 0x00000004
            SQL_SQ_QUANTIFIED = 0x00000008
            SQL_SQ_CORRELATED_SUBQUERIES = 0x00000010

            # SQL_UNION masks
            SQL_U_UNION = 0x00000001
            SQL_U_UNION_ALL = 0x00000002

            # SQL_BOOKMARK_PERSISTENCE values
            SQL_BP_CLOSE = 0x00000001
            SQL_BP_DELETE = 0x00000002
            SQL_BP_DROP = 0x00000004
            SQL_BP_TRANSACTION = 0x00000008
            SQL_BP_UPDATE = 0x00000010
            SQL_BP_OTHER_HSTMT = 0x00000020
            SQL_BP_SCROLL = 0x00000040

            # SQL_STATIC_SENSITIVITY values
            SQL_SS_ADDITIONS = 0x00000001
            SQL_SS_DELETIONS = 0x00000002
            SQL_SS_UPDATES = 0x00000004

            # SQL_VIEW values
            SQL_CV_CREATE_VIEW = 0x00000001
            SQL_CV_CHECK_OPTION = 0x00000002
            SQL_CV_CASCADED = 0x00000004
            SQL_CV_LOCAL = 0x00000008

            # SQL_LOCK_TYPES masks
            SQL_LCK_NO_CHANGE = 0x00000001
            SQL_LCK_EXCLUSIVE = 0x00000002
            SQL_LCK_UNLOCK = 0x00000004

            # SQL_POS_OPERATIONS masks
            SQL_POS_POSITION = 0x00000001
            SQL_POS_REFRESH = 0x00000002
            SQL_POS_UPDATE = 0x00000004
            SQL_POS_DELETE = 0x00000008
            SQL_POS_ADD = 0x00000010

            # SQL_QUALIFIER_LOCATION values
            SQL_QL_START = 0x0001
            SQL_QL_END = 0x0002

            # Here start return values for ODBC 3.0 SQLGetInfo
            if ODBCVER >= 0x0300:
                # SQL_AGGREGATE_FUNCTIONS bitmasks
                SQL_AF_AVG = 0x00000001
                SQL_AF_COUNT = 0x00000002
                SQL_AF_MAX = 0x00000004
                SQL_AF_MIN = 0x00000008
                SQL_AF_SUM = 0x00000010
                SQL_AF_DISTINCT = 0x00000020
                SQL_AF_ALL = 0x00000040

                # SQL_SQL_CONFORMANCE bit masks
                SQL_SC_SQL92_ENTRY = 0x00000001
                SQL_SC_FIPS127_2_TRANSITIONAL = 0x00000002
                SQL_SC_SQL92_INTERMEDIATE = 0x00000004
                SQL_SC_SQL92_FULL = 0x00000008

                # SQL_DATETIME_LITERALS masks
                SQL_DL_SQL92_DATE = 0x00000001
                SQL_DL_SQL92_TIME = 0x00000002
                SQL_DL_SQL92_TIMESTAMP = 0x00000004
                SQL_DL_SQL92_INTERVAL_YEAR = 0x00000008
                SQL_DL_SQL92_INTERVAL_MONTH = 0x00000010
                SQL_DL_SQL92_INTERVAL_DAY = 0x00000020
                SQL_DL_SQL92_INTERVAL_HOUR = 0x00000040
                SQL_DL_SQL92_INTERVAL_MINUTE = 0x00000080
                SQL_DL_SQL92_INTERVAL_SECOND = 0x00000100
                SQL_DL_SQL92_INTERVAL_YEAR_TO_MONTH = 0x00000200
                SQL_DL_SQL92_INTERVAL_DAY_TO_HOUR = 0x00000400
                SQL_DL_SQL92_INTERVAL_DAY_TO_MINUTE = 0x00000800
                SQL_DL_SQL92_INTERVAL_DAY_TO_SECOND = 0x00001000
                SQL_DL_SQL92_INTERVAL_HOUR_TO_MINUTE = 0x00002000
                SQL_DL_SQL92_INTERVAL_HOUR_TO_SECOND = 0x00004000
                SQL_DL_SQL92_INTERVAL_MINUTE_TO_SECOND = 0x00008000

                # SQL_CATALOG_LOCATION values
                SQL_CL_START = SQL_QL_START
                SQL_CL_END = SQL_QL_END

                # values for SQL_BATCH_ROW_COUNT
                SQL_BRC_PROCEDURES = 0x0000001
                SQL_BRC_EXPLICIT = 0x0000002
                SQL_BRC_ROLLED_UP = 0x0000004

                # bitmasks for SQL_BATCH_SUPPORT
                SQL_BS_SELECT_EXPLICIT = 0x00000001
                SQL_BS_ROW_COUNT_EXPLICIT = 0x00000002
                SQL_BS_SELECT_PROC = 0x00000004
                SQL_BS_ROW_COUNT_PROC = 0x00000008

                # Values for SQL_PARAM_ARRAY_ROW_COUNTS getinfo
                SQL_PARC_BATCH = 1
                SQL_PARC_NO_BATCH = 2

                # values for SQL_PARAM_ARRAY_SELECTS
                SQL_PAS_BATCH = 1
                SQL_PAS_NO_BATCH = 2
                SQL_PAS_NO_SELECT = 3

                # Bitmasks for SQL_INDEX_KEYWORDS
                SQL_IK_NONE = 0x00000000
                SQL_IK_ASC = 0x00000001
                SQL_IK_DESC = 0x00000002
                SQL_IK_ALL = SQL_IK_ASC | SQL_IK_DESC

                # Bitmasks for SQL_INFO_SCHEMA_VIEWS
                SQL_ISV_ASSERTIONS = 0x00000001
                SQL_ISV_CHARACTER_SETS = 0x00000002
                SQL_ISV_CHECK_CONSTRAINTS = 0x00000004
                SQL_ISV_COLLATIONS = 0x00000008
                SQL_ISV_COLUMN_DOMAIN_USAGE = 0x00000010
                SQL_ISV_COLUMN_PRIVILEGES = 0x00000020
                SQL_ISV_COLUMNS = 0x00000040
                SQL_ISV_CONSTRAINT_COLUMN_USAGE = 0x00000080
                SQL_ISV_CONSTRAINT_TABLE_USAGE = 0x00000100
                SQL_ISV_DOMAIN_CONSTRAINTS = 0x00000200
                SQL_ISV_DOMAINS = 0x00000400
                SQL_ISV_KEY_COLUMN_USAGE = 0x00000800
                SQL_ISV_REFERENTIAL_CONSTRAINTS = 0x00001000
                SQL_ISV_SCHEMATA = 0x00002000
                SQL_ISV_SQL_LANGUAGES = 0x00004000
                SQL_ISV_TABLE_CONSTRAINTS = 0x00008000
                SQL_ISV_TABLE_PRIVILEGES = 0x00010000
                SQL_ISV_TABLES = 0x00020000
                SQL_ISV_TRANSLATIONS = 0x00040000
                SQL_ISV_USAGE_PRIVILEGES = 0x00080000
                SQL_ISV_VIEW_COLUMN_USAGE = 0x00100000
                SQL_ISV_VIEW_TABLE_USAGE = 0x00200000
                SQL_ISV_VIEWS = 0x00400000

                # Bitmasks for SQL_ASYNC_MODE
                SQL_AM_NONE = 0
                SQL_AM_CONNECTION = 1
                SQL_AM_STATEMENT = 2

                # Bitmasks for SQL_ALTER_DOMAIN
                SQL_AD_CONSTRAINT_NAME_DEFINITION = 0x00000001
                SQL_AD_ADD_DOMAIN_CONSTRAINT = 0x00000002
                SQL_AD_DROP_DOMAIN_CONSTRAINT = 0x00000004
                SQL_AD_ADD_DOMAIN_DEFAULT = 0x00000008
                SQL_AD_DROP_DOMAIN_DEFAULT = 0x00000010
                SQL_AD_ADD_CONSTRAINT_INITIALLY_DEFERRED = 0x00000020
                SQL_AD_ADD_CONSTRAINT_INITIALLY_IMMEDIATE = 0x00000040
                SQL_AD_ADD_CONSTRAINT_DEFERRABLE = 0x00000080
                SQL_AD_ADD_CONSTRAINT_NON_DEFERRABLE = 0x00000100

                # SQL_CREATE_SCHEMA bitmasks
                SQL_CS_CREATE_SCHEMA = 0x00000001
                SQL_CS_AUTHORIZATION = 0x00000002
                SQL_CS_DEFAULT_CHARACTER_SET = 0x00000004

                # SQL_CREATE_TRANSLATION bitmasks
                SQL_CTR_CREATE_TRANSLATION = 0x00000001

                # SQL_CREATE_ASSERTION bitmasks
                SQL_CA_CREATE_ASSERTION = 0x00000001
                SQL_CA_CONSTRAINT_INITIALLY_DEFERRED = 0x00000010
                SQL_CA_CONSTRAINT_INITIALLY_IMMEDIATE = 0x00000020
                SQL_CA_CONSTRAINT_DEFERRABLE = 0x00000040
                SQL_CA_CONSTRAINT_NON_DEFERRABLE = 0x00000080

                # SQL_CREATE_CHARACTER_SET bitmasks
                SQL_CCS_CREATE_CHARACTER_SET = 0x00000001
                SQL_CCS_COLLATE_CLAUSE = 0x00000002
                SQL_CCS_LIMITED_COLLATION = 0x00000004

                # SQL_CREATE_COLLATION bitmasks
                SQL_CCOL_CREATE_COLLATION = 0x00000001

                # SQL_CREATE_DOMAIN bitmasks
                SQL_CDO_CREATE_DOMAIN = 0x00000001
                SQL_CDO_DEFAULT = 0x00000002
                SQL_CDO_CONSTRAINT = 0x00000004
                SQL_CDO_COLLATION = 0x00000008
                SQL_CDO_CONSTRAINT_NAME_DEFINITION = 0x00000010
                SQL_CDO_CONSTRAINT_INITIALLY_DEFERRED = 0x00000020
                SQL_CDO_CONSTRAINT_INITIALLY_IMMEDIATE = 0x00000040
                SQL_CDO_CONSTRAINT_DEFERRABLE = 0x00000080
                SQL_CDO_CONSTRAINT_NON_DEFERRABLE = 0x00000100

                # SQL_CREATE_TABLE bitmasks
                SQL_CT_CREATE_TABLE = 0x00000001
                SQL_CT_COMMIT_PRESERVE = 0x00000002
                SQL_CT_COMMIT_DELETE = 0x00000004
                SQL_CT_GLOBAL_TEMPORARY = 0x00000008
                SQL_CT_LOCAL_TEMPORARY = 0x00000010
                SQL_CT_CONSTRAINT_INITIALLY_DEFERRED = 0x00000020
                SQL_CT_CONSTRAINT_INITIALLY_IMMEDIATE = 0x00000040
                SQL_CT_CONSTRAINT_DEFERRABLE = 0x00000080
                SQL_CT_CONSTRAINT_NON_DEFERRABLE = 0x00000100
                SQL_CT_COLUMN_CONSTRAINT = 0x00000200
                SQL_CT_COLUMN_DEFAULT = 0x00000400
                SQL_CT_COLUMN_COLLATION = 0x00000800
                SQL_CT_TABLE_CONSTRAINT = 0x00001000
                SQL_CT_CONSTRAINT_NAME_DEFINITION = 0x00002000

                # SQL_DDL_INDEX bitmasks
                SQL_DI_CREATE_INDEX = 0x00000001
                SQL_DI_DROP_INDEX = 0x00000002

                # SQL_DROP_COLLATION bitmasks
                SQL_DC_DROP_COLLATION = 0x00000001

                # SQL_DROP_DOMAIN bitmasks
                SQL_DD_DROP_DOMAIN = 0x00000001
                SQL_DD_RESTRICT = 0x00000002
                SQL_DD_CASCADE = 0x00000004

                # SQL_DROP_SCHEMA bitmasks
                SQL_DS_DROP_SCHEMA = 0x00000001
                SQL_DS_RESTRICT = 0x00000002
                SQL_DS_CASCADE = 0x00000004

                # SQL_DROP_CHARACTER_SET bitmasks
                SQL_DCS_DROP_CHARACTER_SET = 0x00000001

                # SQL_DROP_ASSERTION bitmasks
                SQL_DA_DROP_ASSERTION = 0x00000001

                # SQL_DROP_TABLE bitmasks
                SQL_DT_DROP_TABLE = 0x00000001
                SQL_DT_RESTRICT = 0x00000002
                SQL_DT_CASCADE = 0x00000004

                # SQL_DROP_TRANSLATION bitmasks
                SQL_DTR_DROP_TRANSLATION = 0x00000001

                # SQL_DROP_VIEW bitmasks
                SQL_DV_DROP_VIEW = 0x00000001
                SQL_DV_RESTRICT = 0x00000002
                SQL_DV_CASCADE = 0x00000004

                # SQL_INSERT_STATEMENT bitmasks
                SQL_IS_INSERT_LITERALS = 0x00000001
                SQL_IS_INSERT_SEARCHED = 0x00000002
                SQL_IS_SELECT_INTO = 0x00000004

                # SQL_ODBC_INTERFACE_CONFORMANCE values
                SQL_OIC_CORE = 1
                SQL_OIC_LEVEL1 = 2
                SQL_OIC_LEVEL2 = 3

                # SQL_SQL92_FOREIGN_KEY_DELETE_RULE bitmasks
                SQL_SFKD_CASCADE = 0x00000001
                SQL_SFKD_NO_ACTION = 0x00000002
                SQL_SFKD_SET_DEFAULT = 0x00000004
                SQL_SFKD_SET_NULL = 0x00000008

                # SQL_SQL92_FOREIGN_KEY_UPDATE_RULE bitmasks
                SQL_SFKU_CASCADE = 0x00000001
                SQL_SFKU_NO_ACTION = 0x00000002
                SQL_SFKU_SET_DEFAULT = 0x00000004
                SQL_SFKU_SET_NULL = 0x00000008

                # SQL_SQL92_GRANT bitmasks
                SQL_SG_USAGE_ON_DOMAIN = 0x00000001
                SQL_SG_USAGE_ON_CHARACTER_SET = 0x00000002
                SQL_SG_USAGE_ON_COLLATION = 0x00000004
                SQL_SG_USAGE_ON_TRANSLATION = 0x00000008
                SQL_SG_WITH_GRANT_OPTION = 0x00000010
                SQL_SG_DELETE_TABLE = 0x00000020
                SQL_SG_INSERT_TABLE = 0x00000040
                SQL_SG_INSERT_COLUMN = 0x00000080
                SQL_SG_REFERENCES_TABLE = 0x00000100
                SQL_SG_REFERENCES_COLUMN = 0x00000200
                SQL_SG_SELECT_TABLE = 0x00000400
                SQL_SG_UPDATE_TABLE = 0x00000800
                SQL_SG_UPDATE_COLUMN = 0x00001000

                # SQL_SQL92_PREDICATES bitmasks
                SQL_SP_EXISTS = 0x00000001
                SQL_SP_ISNOTNULL = 0x00000002
                SQL_SP_ISNULL = 0x00000004
                SQL_SP_MATCH_FULL = 0x00000008
                SQL_SP_MATCH_PARTIAL = 0x00000010
                SQL_SP_MATCH_UNIQUE_FULL = 0x00000020
                SQL_SP_MATCH_UNIQUE_PARTIAL = 0x00000040
                SQL_SP_OVERLAPS = 0x00000080
                SQL_SP_UNIQUE = 0x00000100
                SQL_SP_LIKE = 0x00000200
                SQL_SP_IN = 0x00000400
                SQL_SP_BETWEEN = 0x00000800
                SQL_SP_COMPARISON = 0x00001000
                SQL_SP_QUANTIFIED_COMPARISON = 0x00002000

                # SQL_SQL92_RELATIONAL_JOIN_OPERATORS bitmasks
                SQL_SRJO_CORRESPONDING_CLAUSE = 0x00000001
                SQL_SRJO_CROSS_JOIN = 0x00000002
                SQL_SRJO_EXCEPT_JOIN = 0x00000004
                SQL_SRJO_FULL_OUTER_JOIN = 0x00000008
                SQL_SRJO_INNER_JOIN = 0x00000010
                SQL_SRJO_INTERSECT_JOIN = 0x00000020
                SQL_SRJO_LEFT_OUTER_JOIN = 0x00000040
                SQL_SRJO_NATURAL_JOIN = 0x00000080
                SQL_SRJO_RIGHT_OUTER_JOIN = 0x00000100
                SQL_SRJO_UNION_JOIN = 0x00000200

                # SQL_SQL92_REVOKE bitmasks
                SQL_SR_USAGE_ON_DOMAIN = 0x00000001
                SQL_SR_USAGE_ON_CHARACTER_SET = 0x00000002
                SQL_SR_USAGE_ON_COLLATION = 0x00000004
                SQL_SR_USAGE_ON_TRANSLATION = 0x00000008
                SQL_SR_GRANT_OPTION_FOR = 0x00000010
                SQL_SR_CASCADE = 0x00000020
                SQL_SR_RESTRICT = 0x00000040
                SQL_SR_DELETE_TABLE = 0x00000080
                SQL_SR_INSERT_TABLE = 0x00000100
                SQL_SR_INSERT_COLUMN = 0x00000200
                SQL_SR_REFERENCES_TABLE = 0x00000400
                SQL_SR_REFERENCES_COLUMN = 0x00000800
                SQL_SR_SELECT_TABLE = 0x00001000
                SQL_SR_UPDATE_TABLE = 0x00002000
                SQL_SR_UPDATE_COLUMN = 0x00004000

                # SQL_SQL92_ROW_VALUE_CONSTRUCTOR bitmasks
                SQL_SRVC_VALUE_EXPRESSION = 0x00000001
                SQL_SRVC_NULL = 0x00000002
                SQL_SRVC_DEFAULT = 0x00000004
                SQL_SRVC_ROW_SUBQUERY = 0x00000008

                # SQL_SQL92_VALUE_EXPRESSIONS bitmasks
                SQL_SVE_CASE = 0x00000001
                SQL_SVE_CAST = 0x00000002
                SQL_SVE_COALESCE = 0x00000004
                SQL_SVE_NULLIF = 0x00000008

                # SQL_STANDARD_CLI_CONFORMANCE bitmasks
                SQL_SCC_XOPEN_CLI_VERSION1 = 0x00000001
                SQL_SCC_ISO92_CLI = 0x00000002

                # SQL_UNION_STATEMENT bitmasks
                SQL_US_UNION = SQL_U_UNION
                SQL_US_UNION_ALL = SQL_U_UNION_ALL

                # values for SQL_DRIVER_AWARE_POOLING_SUPPORTED
                SQL_DRIVER_AWARE_POOLING_NOT_CAPABLE = 0x00000000
                SQL_DRIVER_AWARE_POOLING_CAPABLE = 0x00000001
            # END IF  ODBCVER >= 0x0300

            # SQL_DTC_TRANSITION_COST bitmasks
            SQL_DTC_ENLIST_EXPENSIVE = 0x00000001
            SQL_DTC_UNENLIST_EXPENSIVE = 0x00000002
            if ODBCVER >= 0x0380:
                # possible values for SQL_ASYNC_DBC_FUNCTIONS
                SQL_ASYNC_DBC_NOT_CAPABLE = 0x00000000
                SQL_ASYNC_DBC_CAPABLE = 0x00000001
            # END IF   ODBCVER >= 0x0380

            # additional SQLDataSources fetch directions
            if ODBCVER >= 0x0300:
                SQL_FETCH_FIRST_USER = 31
                SQL_FETCH_FIRST_SYSTEM = 32
            # END IF  ODBCVER >= 0x0300

            # Defines for SQLSetPos
            SQL_ENTIRE_ROWSET = 0

            # Operations in SQLSetPos
            SQL_POSITION = 0            # 1.0 FALSE
            SQL_REFRESH = 1            # 1.0 TRUE
            SQL_UPDATE = 2
            SQL_DELETE = 3

            # Operations in SQLBulkOperations
            SQL_ADD = 4
            SQL_SETPOS_MAX_OPTION_VALUE = SQL_ADD
            if ODBCVER >= 0x0300:
                SQL_UPDATE_BY_BOOKMARK = 5
                SQL_DELETE_BY_BOOKMARK = 6
                SQL_FETCH_BY_BOOKMARK = 7
            # END IF  ODBCVER >= 0x0300

            # Lock options in SQLSetPos
            SQL_LOCK_NO_CHANGE = 0            # 1.0 FALSE
            SQL_LOCK_EXCLUSIVE = 1            # 1.0 TRUE
            SQL_LOCK_UNLOCK = 2
            SQL_SETPOS_MAX_LOCK_VALUE = SQL_LOCK_UNLOCK

            # Macros for SQLSetPos
            def SQL_POSITION_TO(hstmt, irow):
                return SQLSetPos(hstmt,irow,SQL_POSITION,SQL_LOCK_NO_CHANGE)


            def SQL_LOCK_RECORD(hstmt, irow, fLock):
                return SQLSetPos(hstmt,irow,SQL_POSITION,fLock)


            def SQL_REFRESH_RECORD(hstmt, irow, fLock):
                return SQLSetPos(hstmt,irow,SQL_REFRESH,fLock)


            def SQL_UPDATE_RECORD(hstmt, irow):
                return SQLSetPos(hstmt,irow,SQL_UPDATE,SQL_LOCK_NO_CHANGE)


            def SQL_DELETE_RECORD(hstmt, irow):
                return SQLSetPos(hstmt,irow,SQL_DELETE,SQL_LOCK_NO_CHANGE)


            def SQL_ADD_RECORD(hstmt, irow):
                return SQLSetPos(hstmt,irow,SQL_ADD,SQL_LOCK_NO_CHANGE)

            # Column types and scopes in SQLSpecialColumns.
            SQL_BEST_ROWID = 1
            SQL_ROWVER = 2

            # /* Defines for SQLSpecialColumns (returned in the result set)
            # SQL_PC_UNKNOWN and SQL_PC_PSEUDO are defined in sql.h
            SQL_PC_NOT_PSEUDO = 1

            # Defines for SQLStatistics
            SQL_QUICK = 0
            SQL_ENSURE = 1

            # /* Defines for SQLStatistics (returned in the result set)
            # SQL_INDEX_CLUSTERED, SQL_INDEX_HASHED, and SQL_INDEX_OTHER are
            # defined in sql.h
            SQL_TABLE_STAT = 0

            # Defines for SQLTables
            if ODBCVER >= 0x0300:
                SQL_ALL_CATALOGS = "%"
                SQL_ALL_SCHEMAS = "%"
                SQL_ALL_TABLE_TYPES = "%"
            # END IF  ODBCVER >= 0x0300

            # Options for SQLDriverConnect
            SQL_DRIVER_NOPROMPT = 0
            SQL_DRIVER_COMPLETE = 1
            SQL_DRIVER_PROMPT = 2
            SQL_DRIVER_COMPLETE_REQUIRED = 3
            if not defined(RC_INVOKED):
                # SQLRETURN SQL_API SQLDriverConnect(
                # SQLHDBC            hdbc,
                # SQLHWND            hwnd,
                # _In_reads_(cchConnStrIn)
                # SQLCHAR           *szConnStrIn,
                # SQLSMALLINT        cchConnStrIn,
                # _Out_writes_opt_(cchConnStrOutMax)
                # SQLCHAR           *szConnStrOut,
                # SQLSMALLINT        cchConnStrOutMax,
                # _Out_opt_
                # SQLSMALLINT       *pcchConnStrOut,
                # SQLUSMALLINT       fDriverCompletion);
                SQLDriverConnect = odbc32.SQLDriverConnect
                SQLDriverConnect.restype = SQL_API

            # END IF  RC_INVOKED

            # Level 2 Functions
            # SQLExtendedFetch "fFetchType" values
            SQL_FETCH_BOOKMARK = 8

            # SQLExtendedFetch "rgfRowStatus" element values
            SQL_ROW_SUCCESS = 0
            SQL_ROW_DELETED = 1
            SQL_ROW_UPDATED = 2
            SQL_ROW_NOROW = 3
            SQL_ROW_ADDED = 4
            SQL_ROW_ERROR = 5
            if ODBCVER >= 0x0300:
                SQL_ROW_SUCCESS_WITH_INFO = 6
                SQL_ROW_PROCEED = 0
                SQL_ROW_IGNORE = 1
            # END IF

            # value for SQL_DESC_ARRAY_STATUS_PTR
            if ODBCVER >= 0x0300:
                SQL_PARAM_SUCCESS = 0
                SQL_PARAM_SUCCESS_WITH_INFO = 6
                SQL_PARAM_ERROR = 5
                SQL_PARAM_UNUSED = 7
                SQL_PARAM_DIAG_UNAVAILABLE = 1
                SQL_PARAM_PROCEED = 0
                SQL_PARAM_IGNORE = 1
            # END IF  ODBCVER >= 0x0300

            # Defines for SQLForeignKeys (UPDATE_RULE and DELETE_RULE)
            SQL_CASCADE = 0
            SQL_RESTRICT = 1
            SQL_SET_NULL = 2
            if ODBCVER >= 0x0250:
                SQL_NO_ACTION = 3
                SQL_SET_DEFAULT = 4
            # END IF  ODBCVER >= 0x0250

            if ODBCVER >= 0x0300:
                # Note that the following are in a different column of
                # SQLForeignKeys than
                # the previous defines. These are for DEFERRABILITY.
                SQL_INITIALLY_DEFERRED = 5
                SQL_INITIALLY_IMMEDIATE = 6
                SQL_NOT_DEFERRABLE = 7
            # END IF  ODBCVER >= 0x0300

            # /* Defines for SQLBindParameter and SQLProcedureColumns
            # (returned in the result set)
            SQL_PARAM_TYPE_UNKNOWN = 0
            SQL_PARAM_INPUT = 1
            SQL_PARAM_INPUT_OUTPUT = 2
            SQL_RESULT_COL = 3
            SQL_PARAM_OUTPUT = 4
            SQL_RETURN_VALUE = 5
            if ODBCVER >= 0x0380:
                SQL_PARAM_INPUT_OUTPUT_STREAM = 8
                SQL_PARAM_OUTPUT_STREAM = 16
            # END IF

            # Defines for SQLProcedures (returned in the result set)
            SQL_PT_UNKNOWN = 0
            SQL_PT_PROCEDURE = 1
            SQL_PT_FUNCTION = 2
            if not defined(RC_INVOKED):
                # This define is too large for RC
                SQL_ODBC_KEYWORDS = (
                    "ABSOLUTE,ACTION,ADA,ADD,ALL,ALLOCATE,ALTER,AND,ANY,ARE,"
                    "AS,ASC,ASSERTION,AT,AUTHORIZATION,AVG,BEGIN,BETWEEN,BIT,"
                    "BIT_LENGTH,BOTH,BY,CASCADE,CASCADED,CASE,CAST,CATALOG,"
                    "CHAR,CHAR_LENGTH,CHARACTER,CHARACTER_LENGTH,CHECK,CLOSE,"
                    "COALESCE,COLLATE,COLLATION,COLUMN,COMMIT,CONNECT,"
                    "CONNECTION,CONSTRAINT,CONSTRAINTS,CONTINUE,CONVERT,"
                    "CORRESPONDING,COUNT,CREATE,CROSS,CURRENT,CURRENT_DATE,"
                    "CURRENT_TIME,CURRENT_TIMESTAMP,CURRENT_USER,CURSOR,DATE,"
                    "DAY,DEALLOCATE,DEC,DECIMAL,DECLARE,DEFAULT,DEFERRABLE,"
                    "DEFERRED,DELETE,DESC,DESCRIBE,DESCRIPTOR,DIAGNOSTICS,"
                    "DISCONNECT,DISTINCT,DOMAIN,DOUBLE,DROP,ELSE,END,END-EXEC,"
                    "ESCAPE,EXCEPT,EXCEPTION,EXEC,EXECUTE,EXISTS,EXTERNAL,"
                    "EXTRACT,FALSE,FETCH,FIRST,FLOAT,FOR,FOREIGN,FORTRAN,"
                    "FOUND,FROM,FULL,GET,GLOBAL,GO,GOTO,GRANT,GROUP,HAVING,"
                    "HOUR,IDENTITY,IMMEDIATE,IN,INCLUDE,INDEX,INDICATOR,"
                    "INITIALLY,INNER,INPUT,INSENSITIVE,INSERT,INT,INTEGER,"
                    "INTERSECT,INTERVAL,INTO,IS,ISOLATION,JOIN,KEY,LANGUAGE,"
                    "LAST,LEADING,LEFT,LEVEL,LIKE,LOCAL,LOWER,MATCH,MAX,MIN,"
                    "MINUTE,MODULE,MONTH,NAMES,NATIONAL,NATURAL,NCHAR,NEXT,NO,"
                    "NONE,NOT,NULL,NULLIF,NUMERIC,OCTET_LENGTH,OF,ON,ONLY,"
                    "OPEN,OPTION,OR,ORDER,OUTER,OUTPUT,OVERLAPS,PAD,PARTIAL,"
                    "PASCAL,PLI,POSITION,PRECISION,PREPARE,PRESERVE,PRIMARY,"
                    "PRIOR,PRIVILEGES,PROCEDURE,PUBLIC,READ,REAL,REFERENCES,"
                    "RELATIVE,RESTRICT,REVOKE,RIGHT,ROLLBACK,ROWS,SCHEMA,"
                    "SCROLL,SECOND,SECTION,SELECT,SESSION,SESSION_USER,SET,"
                    "SIZE,SMALLINT,SOME,SPACE,SQL,SQLCA,SQLCODE,SQLERROR,"
                    "SQLSTATE,SQLWARNING,SUBSTRING,SUM,SYSTEM_USER,TABLE,"
                    "TEMPORARY,THEN,TIME,TIMESTAMP,TIMEZONE_HOUR,"
                    "TIMEZONE_MINUTE,TO,TRAILING,TRANSACTION,TRANSLATE,"
                    "TRANSLATION,TRIM,TRUE,UNION,UNIQUE,UNKNOWN,UPDATE,UPPER,"
                    "USAGE,USER,USING,VALUE,VALUES,VARCHAR,VARYING,VIEW,WHEN,"
                    "WHENEVER,WHERE,WITH,WORK,WRITE,YEAR,ZONE"
                )

                # SQLRETURN SQL_API SQLBrowseConnect(
                # SQLHDBC            hdbc,
                # _In_reads_(cchConnStrIn)
                # SQLCHAR           *szConnStrIn,
                # SQLSMALLINT        cchConnStrIn,
                # _Out_writes_opt_(cchConnStrOutMax)
                # SQLCHAR           *szConnStrOut,
                # SQLSMALLINT        cchConnStrOutMax,
                # _Out_opt_
                # SQLSMALLINT       *pcchConnStrOut);
                SQLBrowseConnect = odbc32.SQLBrowseConnect
                SQLBrowseConnect.restype = SQL_API

                if ODBCVER >= 0x0300:
                    # SQLRETURN   SQL_API SQLBulkOperations(
                    # SQLHSTMT            StatementHandle,
                    # SQLSMALLINT         Operation);
                    SQLBulkOperations = odbc32.SQLBulkOperations
                    SQLBulkOperations.restype = SQL_API

                # END IF  ODBCVER >= 0x0300

                # SQLRETURN SQL_API SQLColAttributes(
                # SQLHSTMT           hstmt,
                # SQLUSMALLINT       icol,
                # SQLUSMALLINT       fDescType,
                # SQLPOINTER         rgbDesc,
                # SQLSMALLINT        cbDescMax,
                # SQLSMALLINT       *pcbDesc,
                # SQLLEN            * pfDesc);
                SQLColAttributes = odbc32.SQLColAttributes
                SQLColAttributes.restype = SQL_API

                # SQLRETURN SQL_API SQLColumnPrivileges(
                # SQLHSTMT           hstmt,
                # _In_reads_opt_(cchCatalogName)
                # SQLCHAR           *szCatalogName,
                # SQLSMALLINT        cchCatalogName,
                # _In_reads_opt_(cchSchemaName)
                # SQLCHAR           *szSchemaName,
                # SQLSMALLINT        cchSchemaName,
                # _In_reads_opt_(cchTableName)
                # SQLCHAR           *szTableName,
                # SQLSMALLINT        cchTableName,
                # _In_reads_opt_(cchColumnName)
                # SQLCHAR           *szColumnName,
                # SQLSMALLINT        cchColumnName);
                SQLColumnPrivileges = odbc32.SQLColumnPrivileges
                SQLColumnPrivileges.restype = SQL_API

                # SQLRETURN SQL_API SQLDescribeParam(
                # SQLHSTMT           hstmt,
                # SQLUSMALLINT       ipar,
                # _Out_opt_
                # SQLSMALLINT       *pfSqlType,
                # _Out_opt_
                # SQLULEN           *pcbParamDef,
                # _Out_opt_
                # SQLSMALLINT       *pibScale,
                # _Out_opt_
                # SQLSMALLINT       *pfNullable);
                SQLDescribeParam = odbc32.SQLDescribeParam
                SQLDescribeParam.restype = SQL_API

                # SQLRETURN SQL_API SQLExtendedFetch(
                # SQLHSTMT           hstmt,
                # SQLUSMALLINT       fFetchType,
                # SQLLEN             irow,
                # _Out_opt_
                # SQLULEN           *pcrow,
                # _Out_opt_
                # SQLUSMALLINT      *rgfRowStatus);
                SQLExtendedFetch = odbc32.SQLExtendedFetch
                SQLExtendedFetch.restype = SQL_API

                # SQLRETURN SQL_API SQLForeignKeys(
                # SQLHSTMT           hstmt,
                # _In_reads_opt_(cchPkCatalogName)
                # SQLCHAR           *szPkCatalogName,
                # SQLSMALLINT        cchPkCatalogName,
                # _In_reads_opt_(cchPkSchemaName)
                # SQLCHAR           *szPkSchemaName,
                # SQLSMALLINT        cchPkSchemaName,
                # _In_reads_opt_(cchPkTableName)
                # SQLCHAR           *szPkTableName,
                # SQLSMALLINT        cchPkTableName,
                # _In_reads_opt_(cchFkCatalogName)
                # SQLCHAR           *szFkCatalogName,
                # SQLSMALLINT        cchFkCatalogName,
                # _In_reads_opt_(cchFkSchemaName)
                # SQLCHAR           *szFkSchemaName,
                # SQLSMALLINT        cchFkSchemaName,
                # _In_reads_opt_(cchFkTableName)
                # SQLCHAR           *szFkTableName,
                # SQLSMALLINT        cchFkTableName);
                SQLForeignKeys = odbc32.SQLForeignKeys
                SQLForeignKeys.restype = SQL_API

                # SQLRETURN SQL_API SQLMoreResults(
                # SQLHSTMT           hstmt);
                SQLMoreResults = odbc32.SQLMoreResults
                SQLMoreResults.restype = SQL_API

                # SQLRETURN SQL_API SQLNumParams(
                # SQLHSTMT           hstmt,
                # _Out_opt_
                # SQLSMALLINT       *pcpar);
                SQLNumParams = odbc32.SQLNumParams
                SQLNumParams.restype = SQL_API

                # SQLRETURN SQL_API SQLParamOptions(
                # SQLHSTMT           hstmt,
                # SQLULEN            crow,
                # SQLULEN            *pirow);
                SQLParamOptions = odbc32.SQLParamOptions
                SQLParamOptions.restype = SQL_API

                # SQLRETURN SQL_API SQLPrimaryKeys(
                # SQLHSTMT           hstmt,
                # _In_reads_opt_(cchCatalogName)
                # SQLCHAR           *szCatalogName,
                # SQLSMALLINT        cchCatalogName,
                # _In_reads_opt_(cchSchemaName)
                # SQLCHAR           *szSchemaName,
                # SQLSMALLINT        cchSchemaName,
                # _In_reads_opt_(cchTableName)
                # SQLCHAR           *szTableName,
                # SQLSMALLINT        cchTableName);
                SQLPrimaryKeys = odbc32.SQLPrimaryKeys
                SQLPrimaryKeys.restype = SQL_API

                # SQLRETURN SQL_API SQLProcedureColumns(
                # SQLHSTMT           hstmt,
                # _In_reads_opt_(cchCatalogName)
                # SQLCHAR           *szCatalogName,
                # SQLSMALLINT        cchCatalogName,
                # _In_reads_opt_(cchSchemaName)
                # SQLCHAR           *szSchemaName,
                # SQLSMALLINT        cchSchemaName,
                # _In_reads_opt_(cchProcName)
                # SQLCHAR           *szProcName,
                # SQLSMALLINT        cchProcName,
                # _In_reads_opt_(cchColumnName)
                # SQLCHAR           *szColumnName,
                # SQLSMALLINT        cchColumnName);
                SQLProcedureColumns = odbc32.SQLProcedureColumns
                SQLProcedureColumns.restype = SQL_API

                # SQLRETURN SQL_API SQLProcedures(
                # SQLHSTMT           hstmt,
                # _In_reads_opt_(cchCatalogName)
                # SQLCHAR           *szCatalogName,
                # SQLSMALLINT        cchCatalogName,
                # _In_reads_opt_(cchSchemaName)
                # SQLCHAR           *szSchemaName,
                # SQLSMALLINT        cchSchemaName,
                # _In_reads_opt_(cchProcName)
                # SQLCHAR           *szProcName,
                # SQLSMALLINT        cchProcName);
                SQLProcedures = odbc32.SQLProcedures
                SQLProcedures.restype = SQL_API

                # SQLRETURN SQL_API SQLSetPos(
                # SQLHSTMT           hstmt,
                # SQLSETPOSIROW      irow,
                # SQLUSMALLINT       fOption,
                # SQLUSMALLINT       fLock);
                SQLSetPos = odbc32.SQLSetPos
                SQLSetPos.restype = SQL_API

                # SQLRETURN SQL_API SQLTablePrivileges(
                # SQLHSTMT           hstmt,
                # _In_reads_opt_(cchCatalogName)
                # SQLCHAR           *szCatalogName,
                # SQLSMALLINT        cchCatalogName,
                # _In_reads_opt_(cchSchemaName)
                # SQLCHAR           *szSchemaName,
                # SQLSMALLINT        cchSchemaName,
                # _In_reads_opt_(cchTableName)
                # SQLCHAR           *szTableName,
                # SQLSMALLINT        cchTableName);
                SQLTablePrivileges = odbc32.SQLTablePrivileges
                SQLTablePrivileges.restype = SQL_API

                # SQLRETURN SQL_API SQLDrivers(
                # SQLHENV            henv,
                # SQLUSMALLINT       fDirection,
                # _Out_writes_opt_(cchDriverDescMax)
                # SQLCHAR           *szDriverDesc,
                # SQLSMALLINT        cchDriverDescMax,
                # _Out_opt_
                # SQLSMALLINT       *pcchDriverDesc,
                # _Out_writes_opt_(cchDrvrAttrMax)
                # SQLCHAR           *szDriverAttributes,
                # SQLSMALLINT        cchDrvrAttrMax,
                # _Out_opt_
                # SQLSMALLINT       *pcchDrvrAttr);
                SQLDrivers = odbc32.SQLDrivers
                SQLDrivers.restype = SQL_API

                # SQLRETURN SQL_API SQLBindParameter(
                # SQLHSTMT           hstmt,
                # SQLUSMALLINT       ipar,
                # SQLSMALLINT        fParamType,
                # SQLSMALLINT        fCType,
                # SQLSMALLINT        fSqlType,
                # SQLULEN            cbColDef,
                # SQLSMALLINT        ibScale,
                # SQLPOINTER         rgbValue,
                # SQLLEN             cbValueMax,
                # SQLLEN             *pcbValue);
                SQLBindParameter = odbc32.SQLBindParameter
                SQLBindParameter.restype = SQL_API

            # END IF  RC_INVOKED

            # ---------------------------------------------------------
            # SQLAllocHandleStd is implemented to make SQLAllocHandle
            # compatible with X/Open standard. an application should
            # not call SQLAllocHandleStd directly
            # ---------------------------------------------------------
            if defined(ODBC_STD):
                SQLAllocHandle = SQLAllocHandleStd

                def SQLAllocEnv(phenv):
                    return (
                        SQLAllocHandleStd(
                            SQL_HANDLE_ENV,
                            SQL_NULL_HANDLE,
                            phenv
                        )
                    )

                # Internal type subcodes
                SQL_YEAR = SQL_CODE_YEAR
                SQL_MONTH = SQL_CODE_MONTH
                SQL_DAY = SQL_CODE_DAY
                SQL_HOUR = SQL_CODE_HOUR
                SQL_MINUTE = SQL_CODE_MINUTE
                SQL_SECOND = SQL_CODE_SECOND
                SQL_YEAR_TO_MONTH = SQL_CODE_YEAR_TO_MONTH
                SQL_DAY_TO_HOUR = SQL_CODE_DAY_TO_HOUR
                SQL_DAY_TO_MINUTE = SQL_CODE_DAY_TO_MINUTE
                SQL_DAY_TO_SECOND = SQL_CODE_DAY_TO_SECOND
                SQL_HOUR_TO_MINUTE = SQL_CODE_HOUR_TO_MINUTE
                SQL_HOUR_TO_SECOND = SQL_CODE_HOUR_TO_SECOND
                SQL_MINUTE_TO_SECOND = SQL_CODE_MINUTE_TO_SECOND
            # END IF  ODBC_STD

            if ODBCVER >= 0x0300:
                if not defined(RC_INVOKED):
                    # SQLRETURN SQL_API SQLAllocHandleStd(
                    # SQLSMALLINT     fHandleType,
                    # SQLHANDLE       hInput,
                    # _Out_
                    # SQLHANDLE      *phOutput);
                    SQLAllocHandleStd = odbc32.SQLAllocHandleStd
                    SQLAllocHandleStd.restype = SQL_API

                # END IF  RC_INVOKED
            # END IF

            # Deprecated defines from prior versions of ODBC
            SQL_DATABASE_NAME = 16            # Use SQLGetConnectOption/SQL_CURRENT_QUALIFIER
            SQL_FD_FETCH_PREV = SQL_FD_FETCH_PRIOR
            SQL_FETCH_PREV = SQL_FETCH_PRIOR
            SQL_CONCUR_TIMESTAMP = SQL_CONCUR_ROWVER
            SQL_SCCO_OPT_TIMESTAMP = SQL_SCCO_OPT_ROWVER
            SQL_CC_DELETE = SQL_CB_DELETE
            SQL_CR_DELETE = SQL_CB_DELETE
            SQL_CC_CLOSE = SQL_CB_CLOSE
            SQL_CR_CLOSE = SQL_CB_CLOSE
            SQL_CC_PRESERVE = SQL_CB_PRESERVE
            SQL_CR_PRESERVE = SQL_CB_PRESERVE

            # /* SQL_FETCH_RESUME is not supported by 2.0+ drivers define
            # SQL_FETCH_RESUME 7
            SQL_SCROLL_FORWARD_ONLY = 0            # -SQL_CURSOR_FORWARD_ONLY
            SQL_SCROLL_KEYSET_DRIVEN = -1            # -SQL_CURSOR_KEYSET_DRIVEN
            SQL_SCROLL_DYNAMIC = -2            # -SQL_CURSOR_DYNAMIC
            SQL_SCROLL_STATIC = -3            # -SQL_CURSOR_STATIC

            # Deprecated functions from prior versions of ODBC
            if not defined(RC_INVOKED):
                # SQLRETURN SQL_API SQLSetScrollOptions( // Use SQLSetStmtOptions
                # SQLHSTMT           hstmt,
                # SQLUSMALLINT       fConcurrency,
                # SQLLEN             crowKeyset,
                # SQLUSMALLINT       crowRowset);
                SQLSetScrollOptions = odbc32.SQLSetScrollOptions
                SQLSetScrollOptions.restype = SQL_API

                # Tracing section
                TRACE_VERSION = 1000                # Version of trace API

                # open a trace log file                # Request to close a trace log                # Processes trace after FN is called                # Returns trace API version
                # Functions for Visual Studio Analyzer
                # to turn on/off tracing or VS events, call TraceVSControl by
                # setting or clearing the following bits
                TRACE_ON = 0x00000001
                TRACE_VS_EVENT_ON = 0x00000002

                # Functions for setting the connection pooling failure
                # detection code
                # The "TryWait" value is the time (in seconds) that the DM
                # will wait
                # between detecting that a connection is dead (using
                # SQL_ATTR_CONNECTION_DEAD) and retrying the connection. During that
                #
                # interval, connection requests will get
                # "The server appears to be
                # dead" error returns.
                # BOOL SQL_API    ODBCSetTryWaitValue(DWORD dwValue); // In seconds
                ODBCSetTryWaitValue = odbc32.ODBCSetTryWaitValue
                ODBCSetTryWaitValue.restype = SQL_API

                # In Milliseconds(not )
                # ------------- Visual Studio Analyzer Support is removed from
                # ODBC (Windows 8 and onwards) ---------
                # From Windows 8 and onwards, Visual Studio Analyzer Support
                # for ODBC is removed. Third-party trace
                # library does not need to define the function
                # FireVSDebugEvent any more, which would not be called
                # from ODBC DM in Windows 8.
                # If your trace library is going to work on downlevel
                # platforms, you may still want to define the
                # function FireVSDebugEvent. But the trace library can still
                # be loaded on downlevel platforms even
                # if this function is not defined.
                # the flags in ODBC_VS_ARGS
                ODBC_VS_FLAG_UNICODE_ARG = 0x00000001                # the argument is unicode
                ODBC_VS_FLAG_UNICODE_COR = 0x00000002                # the correlation is unicode
                ODBC_VS_FLAG_RETCODE = 0x00000004                # RetCode field is set
                ODBC_VS_FLAG_STOP = 0x00000008                # Stop firing visual studio analyzer events


                # the GUID for event
                class _Union_1(ctypes.Union):
                    pass


                _Union_1._fields_ = [
                    ('wszArg', POINTER(WCHAR)),
                    ('szArg', POINTER(CHAR)),
                ]
                tagODBC_VS_ARGS._Union_1 = _Union_1


                class _Union_2(ctypes.Union):
                    pass


                _Union_2._fields_ = [
                    ('wszCorrelation', POINTER(WCHAR)),
                    ('szCorrelation', POINTER(CHAR)),
                ]
                tagODBC_VS_ARGS._Union_2 = _Union_2

                tagODBC_VS_ARGS._anonymous_ = (
                    '_Union_1',
                    '_Union_2',
                )

                tagODBC_VS_ARGS._fields_ = [
                    ('pguidEvent', POINTER(GUID)),
                    # flags for the call
                    ('dwFlags', DWORD),
                    ('_Union_1', tagODBC_VS_ARGS._Union_1),
                    ('_Union_2', tagODBC_VS_ARGS._Union_2),
                    ('RetCode', RETCODE),
                ]
            # END IF  RC_INVOKED

            if defined(__cplusplus):
                # End of extern "C" {
                pass
            #  END IF  __cplusplus
            if defined(WIN32) or defined(_WIN64):
                from pyWinAPI.um.sqlucode_h import * # NOQA
            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # END IF  __SQLEXT


