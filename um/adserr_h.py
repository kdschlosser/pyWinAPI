# ++ BUILD Version: 0001     Increment this if a change has global effects
# Copyright (c) 1991-1999  Microsoft Corporation
# Module Name:
# oledserr.mc
# Abstract:
# Error codes for ADs
# Revision History:
# --
from winapifamily_h import * # NOQA

# ---------------------- HRESULT value definitions -----------------

# HRESULT definitions


def _HRESULT_TYPEDEF_(_sc):
    return _sc

# Values are 32 bit values layed out as follows:

# 3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
# 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
# +---+-+-+-----------------------+-------------------------------+
# |Sev|C|R|     Facility          |               Code            |
# +---+-+-+-----------------------+-------------------------------+

# where

# Sev - is the severity code

# 00 - Success
# 01 - Informational
# 10 - Warning
# 11 - Error

# C - is the Customer code flag

# R - is a reserved bit

# Facility - is the facility code

# Code - is the facility's status code


# Define the facility codes

FACILITY_WINDOWS = 0x00000008
FACILITY_STORAGE = 0x00000003
FACILITY_RPC = 0x00000001
FACILITY_SSPI = 0x00000009
FACILITY_WIN32 = 0x00000007
FACILITY_CONTROL = 0x0000000A
FACILITY_NULL = 0x00000000
FACILITY_ITF = 0x00000004
FACILITY_DISPATCH = 0x00000002

# Define the severity codes


# MessageId: E_ADS_BAD_PATHNAME
# MessageText: An invalid directory pathname was passed
E_ADS_BAD_PATHNAME = _HRESULT_TYPEDEF_(0x80005000)

# MessageId: E_ADS_INVALID_DOMAIN_OBJECT
# MessageText: An unknown directory domain object was requested
E_ADS_INVALID_DOMAIN_OBJECT = _HRESULT_TYPEDEF_(0x80005001)

# MessageId: E_ADS_INVALID_USER_OBJECT
# MessageText: An unknown directory user object was requested
E_ADS_INVALID_USER_OBJECT = _HRESULT_TYPEDEF_(0x80005002)

# MessageId: E_ADS_INVALID_COMPUTER_OBJECT
# MessageText: An unknown directory computer object was requested
E_ADS_INVALID_COMPUTER_OBJECT = _HRESULT_TYPEDEF_(0x80005003)

# MessageId: E_ADS_UNKNOWN_OBJECT
# MessageText: An unknown directory object was requested
E_ADS_UNKNOWN_OBJECT = _HRESULT_TYPEDEF_(0x80005004)

# MessageId: E_ADS_PROPERTY_NOT_SET
# MessageText: The specified directory property was not set
E_ADS_PROPERTY_NOT_SET = _HRESULT_TYPEDEF_(0x80005005)

# MessageId: E_ADS_PROPERTY_NOT_SUPPORTED
# MessageText: The specified directory property is not supported
E_ADS_PROPERTY_NOT_SUPPORTED = _HRESULT_TYPEDEF_(0x80005006)

# MessageId: E_ADS_PROPERTY_INVALID
# MessageText: The specified directory property is invalid
E_ADS_PROPERTY_INVALID = _HRESULT_TYPEDEF_(0x80005007)

# MessageId: E_ADS_BAD_PARAMETER
# MessageText: One or more input parameters are invalid
E_ADS_BAD_PARAMETER = _HRESULT_TYPEDEF_(0x80005008)

# MessageId: E_ADS_OBJECT_UNBOUND
# MessageText: The specified directory object is not bound to a remote resource
E_ADS_OBJECT_UNBOUND = _HRESULT_TYPEDEF_(0x80005009)

# MessageId: E_ADS_PROPERTY_NOT_MODIFIED
# MessageText: The specified directory object has not been modified
E_ADS_PROPERTY_NOT_MODIFIED = _HRESULT_TYPEDEF_(0x8000500A)

# MessageId: E_ADS_PROPERTY_MODIFIED
# MessageText: The specified directory object has been modified
E_ADS_PROPERTY_MODIFIED = _HRESULT_TYPEDEF_(0x8000500B)

# MessageId: E_ADS_CANT_CONVERT_DATATYPE
# MessageText: The directory datatype cannot be converted to/from a native DS datatype
E_ADS_CANT_CONVERT_DATATYPE = _HRESULT_TYPEDEF_(0x8000500C)

# MessageId: E_ADS_PROPERTY_NOT_FOUND
# MessageText: The directory property cannot be found in the cache.
E_ADS_PROPERTY_NOT_FOUND = _HRESULT_TYPEDEF_(0x8000500D)

# MessageId: E_ADS_OBJECT_EXISTS
# MessageText: The directory object exists.
E_ADS_OBJECT_EXISTS = _HRESULT_TYPEDEF_(0x8000500E)

# MessageId: E_ADS_SCHEMA_VIOLATION
# MessageText: The attempted action violates the DS schema rules.
E_ADS_SCHEMA_VIOLATION = _HRESULT_TYPEDEF_(0x8000500F)

# MessageId: E_ADS_COLUMN_NOT_SET
# MessageText: The specified column in the directory was not set.
E_ADS_COLUMN_NOT_SET = _HRESULT_TYPEDEF_(0x80005010)

# MessageId: S_ADS_ERRORSOCCURRED
# MessageText: One or more errors occurred
S_ADS_ERRORSOCCURRED = _HRESULT_TYPEDEF_(0x00005011)

# MessageId: S_ADS_NOMORE_ROWS
# MessageText: No more rows to be obatained by the search result.
S_ADS_NOMORE_ROWS = _HRESULT_TYPEDEF_(0x00005012)

# MessageId: S_ADS_NOMORE_COLUMNS
# MessageText: No more columns to be obatained for the current row.
S_ADS_NOMORE_COLUMNS = _HRESULT_TYPEDEF_(0x00005013)

# MessageId: E_ADS_INVALID_FILTER
# MessageText: The search filter specified is invalid
E_ADS_INVALID_FILTER = _HRESULT_TYPEDEF_(0x80005014)
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

__all__ = (
    'E_ADS_CANT_CONVERT_DATATYPE', 'FACILITY_WINDOWS', 'E_ADS_INVALID_FILTER',
    'E_ADS_PROPERTY_MODIFIED', 'FACILITY_NULL', 'FACILITY_DISPATCH',
    'E_ADS_PROPERTY_INVALID', 'E_ADS_BAD_PARAMETER', 'FACILITY_STORAGE',
    'E_ADS_PROPERTY_NOT_SET', 'FACILITY_WIN32', 'E_ADS_PROPERTY_NOT_MODIFIED',
    'E_ADS_COLUMN_NOT_SET', '_HRESULT_TYPEDEF_', 'E_ADS_INVALID_USER_OBJECT',
    'FACILITY_SSPI', 'E_ADS_PROPERTY_NOT_FOUND', 'S_ADS_NOMORE_COLUMNS',
    'E_ADS_INVALID_DOMAIN_OBJECT', 'FACILITY_ITF', 'E_ADS_UNKNOWN_OBJECT',
    'E_ADS_PROPERTY_NOT_SUPPORTED', 'FACILITY_RPC', 'E_ADS_OBJECT_UNBOUND',
    'E_ADS_OBJECT_EXISTS', 'E_ADS_BAD_PATHNAME', 'S_ADS_ERRORSOCCURRED',
    'S_ADS_NOMORE_ROWS', 'FACILITY_CONTROL', 'E_ADS_INVALID_COMPUTER_OBJECT',
    'E_ADS_SCHEMA_VIOLATION',
)
