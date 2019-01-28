import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.guiddef_h import *

__MFGRL_H_ = None


class _GRL_HEADER(ctypes.Structure):
    pass


GRL_HEADER = _GRL_HEADER


class _GRL_ENTRY(ctypes.Structure):
    pass


GRL_ENTRY = _GRL_ENTRY


class _GRL_EXTENSIBLE_ENTRY(ctypes.Structure):
    pass


GRL_EXTENSIBLE_ENTRY = _GRL_EXTENSIBLE_ENTRY


class _GRL_RENEWAL_ENTRY(ctypes.Structure):
    pass


GRL_RENEWAL_ENTRY = _GRL_RENEWAL_ENTRY


class _MF_SIGNATURE(ctypes.Structure):
    pass


MF_SIGNATURE = _MF_SIGNATURE

# @@@ + + +
# @@@@******************************************************************
# Microsoft Windows Media
# Copyright (C) Microsoft Corporation. All rights reserved.
# @@@---@@@@******************************************************************
# mfgrl.h

if not defined(__MFGRL_H_):
    __MFGRL_H_ = VOID

    # Values GRLReader will match against GRL header to verify it recognizes
    # the format
    GRL_HEADER_IDENTIFIER = "MSGRL"
    GRL_FORMAT_MAJOR = 1
    GRL_FORMAT_MINOR = 0

    # Very very conservative max sizes (in bytes) for each section.
    # This allows GRLReader to avoid over-allocating memory for corrupted /
    # malicious data
    GRL_CORE_SIZE_MAX = 1048576
    GRL_EXT_SIZE_MAX = 1048576
    GRL_RENEWAL_SIZE_MAX = 1048576
    GRL_CORE_SIG_SIZE_MAX = 1048576
    GRL_EXT_SIG_SIZE_MAX = 1048576
    GRL_PATH_KEY = "System\\CurrentControlSet\\Services\\PEAuth"
    GRL_PATH_KEY_KERNEL = (
        "\\Registry\\Machine\\System\\CurrentControlSet\\Services\\PEAuth"
    )
    GRL_PATH_VALUE = "DataPath"

    # /////////////////////////////////////////////////////////////////////////////
    #
    _GRL_HEADER._fields_ = [
        ('wszIdentifier', WCHAR * 6),
        ('wFormatMajor', WORD),
        ('wFormatMinor', WORD),
        ('CreationTime', FILETIME),
        ('dwSequenceNumber', DWORD),
        ('dwForceRebootVersion', DWORD),
        ('dwForceProcessRestartVersion', DWORD),
        ('cbRevocationSectionOffset', DWORD),
        ('cRevokedKernelBinaries', DWORD),
        ('cRevokedUserBinaries', DWORD),
        ('cRevokedCertificates', DWORD),
        ('cTrustedRoots', DWORD),
        ('cbExtensibleSectionOffset', DWORD),
        ('cExtensibleEntries', DWORD),
        ('cbRenewalSectionOffset', DWORD),
        ('cRevokedKernelBinaryRenewals', DWORD),
        ('cRevokedUserBinaryRenewals', DWORD),
        ('cRevokedCertificateRenewals', DWORD),
        ('cbSignatureCoreOffset', DWORD),
        ('cbSignatureExtOffset', DWORD),
    ]

    # /////////////////////////////////////////////////////////////////////////
    # This corresponds to RTL_MAX_HASH_LEN_V1
    GRL_HASH_SIZE = 20
    GRL_EXTENSIBLE_ENTRY_SIZE = 4096

    # /////////////////////////////////////////////////////////////////////////
    _GRL_ENTRY._fields_ = [
        ('rgbGRLEntry', BYTE * GRL_HASH_SIZE),
    ]

    # /////////////////////////////////////////////////////////////////////////
    _GRL_EXTENSIBLE_ENTRY._fields_ = [
        ('guidExtensionID', GUID),
        ('rgbExtensibleEntry', BYTE * GRL_EXTENSIBLE_ENTRY_SIZE),
    ]

    # /////////////////////////////////////////////////////////////////////////
    _GRL_RENEWAL_ENTRY._fields_ = [
        ('grlEntry', GRL_ENTRY),
        ('guidRenewalID', GUID),
    ]

    # /////////////////////////////////////////////////////////////////////////
    _MF_SIGNATURE._fields_ = [
        ('dwSignVer', DWORD),
        ('cbSign', DWORD),
        ('rgSign', BYTE * 1),
    ]

    # /////////////////////////////////////////////////////////////////////////
    # Other GRL constants
    # /////////////////////////////////////////////////////////////////////////
    # The value of dwForceRebootVersion in the GRL header before the first
    # component
    # is added to the GRL that requires a reboot.
    GRL_FORCEREBOOTVERSION_INITIAL = 0

    # The value of dwForceProcessRestartVersion in the GRL header before the
    # first component
    # is added to the GRL that requires processes to be restarted.
    GRL_FORCEPROCESSRESTARTVERSION_INITIAL = 0
# END IF   __MFGRL_H_
