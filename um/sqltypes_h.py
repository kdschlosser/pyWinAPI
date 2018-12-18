import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__SQLTYPES = None
ODBCVER = None
EXPORT = None
WIN32 = None
OS2 = None
UNIX = None
__SQLDATE = None
ODBCINT64 = None
GUID_DEFINED = None
_WCHAR_T_DEFINED = None

class tagDATE_STRUCT(ctypes.Structure):
    pass


DATE_STRUCT = tagDATE_STRUCT


class tagTIME_STRUCT(ctypes.Structure):
    pass


TIME_STRUCT = tagTIME_STRUCT


class tagTIMESTAMP_STRUCT(ctypes.Structure):
    pass


TIMESTAMP_STRUCT = tagTIMESTAMP_STRUCT


class tagSQL_YEAR_MONTH(ctypes.Structure):
    pass


SQL_YEAR_MONTH_STRUCT = tagSQL_YEAR_MONTH


class tagSQL_DAY_SECOND(ctypes.Structure):
    pass


SQL_DAY_SECOND_STRUCT = tagSQL_DAY_SECOND


class tagSQL_INTERVAL_STRUCT(ctypes.Structure):
    pass


SQL_INTERVAL_STRUCT = tagSQL_INTERVAL_STRUCT


class tagSQL_NUMERIC_STRUCT(ctypes.Structure):
    pass


SQL_NUMERIC_STRUCT = tagSQL_NUMERIC_STRUCT


class tagSQLGUID(ctypes.Structure):
    pass


SQLGUID = tagSQLGUID


# ******************************************************          * Copyright
# (C) Microsoft. All rights reserved. *  *
# *****************************************************
# -----------------------------------------------------------------------------
# File:  sqltypes.h
# Contents:  This file defines the types used in ODBC
# Comments:
# -----------------------------------------------------------------------------
if defined(_MSC_VER) and (_MSC_VER > 1000):
    pass
# END IF


if not defined(__SQLTYPES):
    __SQLTYPES = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # if ODBCVER is not defined, default to ODBC 3.80
        if not defined(ODBCVER):
            ODBCVER = 0x0380
        # END IF  ODBCVER

        if defined(__cplusplus):
            # Assume C declarations for C + +
            pass
        #  END IF  __cplusplus

        # environment specific definitions
        if not defined(EXPORT):
            EXPORT = VOID
        # END IF

        if defined(WIN32):
            SQL_API = VOID
        else:
            SQL_API = VOID
        # END IF

        if not defined(RC_INVOKED):
            SQLSMALLINT = SHORT
            SQLUSMALLINT = USHORT

            # API declaration data types
            SQLCHAR = UCHAR
            if ODBCVER >= 0x0300:
                SQLSCHAR = CHAR
                SQLDATE = UCHAR
                SQLDECIMAL = UCHAR
                SQLDOUBLE = DOUBLE
                SQLFLOAT = DOUBLE
            # END IF

            SQLINTEGER = LONG
            SQLUINTEGER = ULONG
            if defined(_WIN64):
                SQLLEN = INT64
                SQLULEN = UINT64
                SQLSETPOSIROW = UINT64
            else:
                SQLLEN = SQLINTEGER
                SQLULEN = SQLUINTEGER
                SQLSETPOSIROW = SQLUSMALLINT
            # END IF

            # For Backward compatibility
            if defined(WIN32):
                SQLROWCOUNT = SQLULEN
                SQLROWSETSIZE = SQLULEN
                SQLTRANSID = SQLULEN
                SQLROWOFFSET = SQLLEN
            # END IF

            if ODBCVER >= 0x0300:
                SQLNUMERIC = UCHAR
            # END IF

            SQLPOINTER = POINTER(VOID)
            if ODBCVER >= 0x0300:
                SQLREAL = FLOAT
            # END IF

            if ODBCVER >= 0x0300:
                SQLTIME = UCHAR
                SQLTIMESTAMP = UCHAR
                SQLVARCHAR = UCHAR
            # END IF

            # function return type
            SQLRETURN = SQLSMALLINT

            # generic data structures
            if ODBCVER >= 0x0300:
                if defined(WIN32) or defined(_WIN64):
                    SQLHANDLE = POINTER(VOID)
                else:
                    SQLHANDLE = SQLINTEGER
                # END IF  defined(WIN32) or defined(_WIN64)

                SQLHENV = SQLHANDLE
                SQLHDBC = SQLHANDLE
                SQLHSTMT = SQLHANDLE
                SQLHDESC = SQLHANDLE
            else:
                if defined(WIN32) or defined(_WIN64):
                    SQLHENV = POINTER(VOID)
                    SQLHDBC = POINTER(VOID)
                    SQLHSTMT = POINTER(VOID)
                else:
                    SQLHENV = SQLINTEGER
                    SQLHDBC = SQLINTEGER
                    SQLHSTMT = SQLINTEGER
                # END IF  defined(WIN32) or defined(_WIN64)
            # END IF  ODBCVER >= 0x0300

            # SQL portable types for C
            SCHAR = CHAR
            SQLSCHAR = SCHAR
            SDWORD = ULONG
            SWORD = SHORT
            UDWORD = ULONG
            UWORD = USHORT
            if not defined(_WIN64):
                SQLUINTEGER = UDWORD
            # END IF


            SLONG = LONG
            SSHORT = SHORT
            SDOUBLE = DOUBLE
            LDOUBLE = DOUBLE
            SFLOAT = FLOAT
            PTR = POINTER(VOID)
            HENV = POINTER(VOID)
            HDBC = POINTER(VOID)
            HSTMT = POINTER(VOID)
            RETCODE = SHORT
            if defined(WIN32) or defined(OS2):
                SQLHWND = HWND
            elif defined (UNIX):
                SQLHWND = HWND
            else:
                # placehold for future O/S GUI window handle definition
                SQLHWND = SQLPOINTER
            # END IF

            if not defined(__SQLDATE):
                __SQLDATE = VOID

                # transfer types for DATE, TIME, TIMESTAMP
                tagDATE_STRUCT._fields_ = [
                    ('year', SQLSMALLINT),
                    ('month', SQLUSMALLINT),
                    ('day', SQLUSMALLINT),
                ]
                if ODBCVER >= 0x0300:
                    SQL_DATE_STRUCT = DATE_STRUCT
                # END IF  ODBCVER >= 0x0300


                tagTIME_STRUCT._fields_ = [
                    ('hour', SQLUSMALLINT),
                    ('minute', SQLUSMALLINT),
                    ('second', SQLUSMALLINT),
                ]
                if ODBCVER >= 0x0300:
                    SQL_TIME_STRUCT = TIME_STRUCT
                # END IF  ODBCVER >= 0x0300


                tagTIMESTAMP_STRUCT._fields_ = [
                    ('year', SQLSMALLINT),
                    ('month', SQLUSMALLINT),
                    ('day', SQLUSMALLINT),
                    ('hour', SQLUSMALLINT),
                    ('minute', SQLUSMALLINT),
                    ('second', SQLUSMALLINT),
                    ('fraction', SQLUINTEGER),
                ]
                if ODBCVER >= 0x0300:
                    SQL_TIMESTAMP_STRUCT = TIMESTAMP_STRUCT
                # END IF  ODBCVER >= 0x0300

                # /* enumerations for DATETIME_INTERVAL_SUBCODE values for
                # interval data types these values are from SQL-92
                if ODBCVER >= 0x0300:
                    class SQLINTERVAL(ENUM):
                        SQL_IS_YEAR = 1
                        SQL_IS_MONTH = 2
                        SQL_IS_DAY = 3
                        SQL_IS_HOUR = 4
                        SQL_IS_MINUTE = 5
                        SQL_IS_SECOND = 6
                        SQL_IS_YEAR_TO_MONTH = 7
                        SQL_IS_DAY_TO_HOUR = 8
                        SQL_IS_DAY_TO_MINUTE = 9
                        SQL_IS_DAY_TO_SECOND = 10
                        SQL_IS_HOUR_TO_MINUTE = 11
                        SQL_IS_HOUR_TO_SECOND = 12
                        SQL_IS_MINUTE_TO_SECOND = 13

                    SQL_IS_YEAR = SQLINTERVAL.SQL_IS_YEAR
                    SQL_IS_MONTH = SQLINTERVAL.SQL_IS_MONTH
                    SQL_IS_DAY = SQLINTERVAL.SQL_IS_DAY
                    SQL_IS_HOUR = SQLINTERVAL.SQL_IS_HOUR
                    SQL_IS_MINUTE = SQLINTERVAL.SQL_IS_MINUTE
                    SQL_IS_SECOND = SQLINTERVAL.SQL_IS_SECOND
                    SQL_IS_YEAR_TO_MONTH = SQLINTERVAL.SQL_IS_YEAR_TO_MONTH
                    SQL_IS_DAY_TO_HOUR = SQLINTERVAL.SQL_IS_DAY_TO_HOUR
                    SQL_IS_DAY_TO_MINUTE = SQLINTERVAL.SQL_IS_DAY_TO_MINUTE
                    SQL_IS_DAY_TO_SECOND = SQLINTERVAL.SQL_IS_DAY_TO_SECOND
                    SQL_IS_HOUR_TO_MINUTE = SQLINTERVAL.SQL_IS_HOUR_TO_MINUTE
                    SQL_IS_HOUR_TO_SECOND = SQLINTERVAL.SQL_IS_HOUR_TO_SECOND
                    SQL_IS_MINUTE_TO_SECOND = SQLINTERVAL.SQL_IS_MINUTE_TO_SECOND
                # END IF  ODBCVER >= 0x0300

                if ODBCVER >= 0x0300:
                    tagSQL_YEAR_MONTH._fields_ = [
                        ('year', SQLUINTEGER),
                        ('month', SQLUINTEGER),
                    ]

                    tagSQL_DAY_SECOND._fields_ = [
                        ('day', SQLUINTEGER),
                        ('hour', SQLUINTEGER),
                        ('minute', SQLUINTEGER),
                        ('second', SQLUINTEGER),
                        ('fraction', SQLUINTEGER),
                    ]


                    class intval(ctypes.Union):
                        pass


                    intval._fields_ = [
                        ('year_month', SQL_YEAR_MONTH_STRUCT),
                        ('day_second', SQL_DAY_SECOND_STRUCT),
                    ]
                    tagSQL_INTERVAL_STRUCT.intval = intval


                    tagSQL_INTERVAL_STRUCT._fields_ = [
                        ('interval_type', SQLINTERVAL),
                        ('interval_sign', SQLSMALLINT),
                        ('intval', tagSQL_INTERVAL_STRUCT.intval),
                    ]
                # END IF  ODBCVER >= 0x0300
            # END IF  __SQLDATE

            # the ODBC C types for SQL_C_SBIGINT and SQL_C_UBIGINT
            if ODBCVER >= 0x0300:
                if _MSC_VER >= 900:
                    ODBCINT64 = INT64
                # END IF

                # /* If using other compilers, define ODBCINT64 to the
                # approriate 64 bit integer type
                if defined(ODBCINT64):
                    SQLBIGINT = ODBCINT64
                    SQLUBIGINT = ODBCINT64
                # END IF

            # END IF  ODBCVER >= 0x0300

            # internal representation of numeric data type
            if ODBCVER >= 0x0300:
                SQL_MAX_NUMERIC_LEN = 16

                tagSQL_NUMERIC_STRUCT._fields_ = [
                    ('precision', SQLCHAR),
                    ('scale', SQLSCHAR),
                    # 1 if positive, 0 if negative
                    ('sign', SQLCHAR),
                    ('val', SQLCHAR * SQL_MAX_NUMERIC_LEN),
                ]
            # END IF  ODBCVER >= 0x0300

            if ODBCVER >= 0x0350:
                if defined(GUID_DEFINED):
                    SQLGUID = GUID
                else:
                    # size is 16
                    tagSQLGUID._fields_ = [
                        ('Data1', DWORD),
                        ('Data2', WORD),
                        ('Data3', WORD),
                        ('Data4', BYTE * 8),
                    ]
                # END IF  GUID_DEFINED
            # END IF  ODBCVER >= 0x0350

            BOOKMARK = SQLULEN
            if defined(_WCHAR_T_DEFINED):
                SQLWCHAR = WCHAR
            else:
                SQLWCHAR = USHORT
            # END IF

            if defined(UNICODE):
                SQLTCHAR = SQLWCHAR
            else:
                SQLTCHAR = SQLCHAR
            # END IF  UNICODE
        # END IF  RC_INVOKED

        if defined(__cplusplus):
            # End of extern "C" {
            pass
        # END IF  __cplusplus
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF  #ifndef __SQLTYPES
