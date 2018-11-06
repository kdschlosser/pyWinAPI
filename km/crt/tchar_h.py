

from wtypes_h import (
    NULL,
    TCHAR,
    CHAR,
    POINTER,
    INT,
    UINT,
    WCHAR
)
import ntdef_h


from crtdefs_h import * # NOQA
from ctype_h import *
from wchar_h import *


wINT_t = UINT
wctype_t = UINT
_TCHAR = WCHAR
_TSCHAR = TCHAR
_TUCHAR = TCHAR
_TXCHAR = TCHAR
_TINT = wINT_t
_TEOF = WEOF


def _strdec(_cpc1, _cpc2):
    if _cpc1 >= _cpc2:
        return None
    else:
        return _cpc2 - 1


def _strinc(_pc):
    return _pc + 1


def _strnextc(_cpc):
    return _cpc


def _strninc(_pc, _sz):
    return _pc + _sz


def _strncnt(_cpc, _sz):
    return __strncnt(_cpc, _sz)


def _strspnp(_cpc1, _cpc2):
    if _cpc1 is None:
        return None
    elif _cpc1 + strspn(_cpc1,_cpc2):
        return _cpc1 + strspn(_cpc1, _cpc2)
    else:
        return None


def _strncpy_l(_Destination, _Source, _Count, _Locale):
    return strncpy(_Destination, _Source, _Count)


def _strncpy_s_l(_Destination, _Destination_size_CHARs, _Source, _Count, _Locale):
    return strncpy_s(_Destination, _Destination_size_CHARs, _Source, _Count)


def _strncat_l(_Destination, _Source, _Count, _Locale):
    return strncat(_Destination, _Source, _Count)


def _strncat_s_l(_Destination, _Destination_size_CHARs, _Source, _Count, _Locale):
    return strncat_s(_Destination, _Destination_size_CHARs, _Source, _Count)


def _strtok_l(_String, _Delimiters, _Locale):
    return strtok(_String, _Delimiters)


def _strtok_s_l(_String, _Delimiters, _Current_position, _Locale):
    return strtok_s(_String, _Delimiters, _Current_position)


def _strnset_l(_Destination, _Value, _Count, _Locale):
    return _strnset(_Destination, _Value, _Count)


def _strnset_s_l(_Destination, _Destination_size_CHARs, _Value, _Count, _Locale):
    return _strnset_s(_Destination, _Destination_size_CHARs, _Value, _Count)


def _strset_l(_Destination, _Value, _Locale):
    return _strset(_Destination, _Value)


def _strset_s_l(_Destination, _Destination_size_CHARs, _Value, _Locale):
    return _strset_s(_Destination, _Destination_size_CHARs, _Value)


def _tcsclen_l(_String, _Locale):
    return wcslen(_String)


def _tcscnlen_l(_String, _Max_count, _Locale):
    return wcsnlen(_String, _Max_count)


def _tclen(_pc):
    return 1


def _tccpy(_pc1, _cpc2):
    _pc1 = _cpc2
    return _pc1


def _tccpy_l(_pc1, _cpc2, _locale):
    return _tccpy(_pc1, _cpc2)


def _tccmp(_cpc1, _cpc2):
    return _cpc1 - _cpc2


def _istlegal(_Char):
    return 1


def _istlead(_Char):
    return 0


def _istleadbyte(_Char):
    return 0


def _istleadbyte_l(_Char, _Locale):
    return 0


def _wcsdec(_cpc1, _cpc2):
    if _cpc1 >= _cpc2:
        return NULL
    else:
        return _cpc2 - 1


def _wcsinc(_pc):
    return _pc + 1


def _wcsnextc(_cpc):
    return _cpc


def _wcsninc(_pc, _sz):
    return _pc + _sz


def _wcsncnt(_cpc, _sz):
    return __wcsncnt(_cpc, _sz)


def _wcsspnp(_cpc1, _cpc2):
    if _cpc1 == NULL:
        return None
    elif _cpc1 + wcsspn(_cpc1, _cpc2):
        return _cpc1 + wcsspn(_cpc1, _cpc2)
    else:
        return NULL


def _wcsncpy_l(_Destination, _Source, _Count, _Locale):
    return wcsncpy(_Destination, _Source, _Count)


def _wcsncpy_s_l(_Destination, _Destination_size_CHARs, _Source, _Count, _Locale):
    return wcsncpy_s(_Destination, _Destination_size_CHARs, _Source, _Count)


def _wcsncat_l(_Destination, _Source, _Count, _Locale):
    return wcsncat(_Destination, _Source, _Count)


def _wcsncat_s_l(_Destination, _Destination_size_CHARs, _Source, _Count, _Locale):
    return wcsncat_s(_Destination, _Destination_size_CHARs, _Source, _Count)


def _wcstok_l(_String, _Delimiters, _Locale):
    return wcstok(_String, _Delimiters)


def _wcstok_s_l(_String, _Delimiters, _Current_position, _Locale):
    return wcstok_s(_String, _Delimiters, _Current_position)


def _wcsnset_l(_Destination, _Value, _Count, _Locale):
    return _wcsnset(_Destination, _Value, _Count)


def _wcsnset_s_l(_Destination, _Destination_size_CHARs, _Value, _Count, _Locale):
    return _wcsnset_s(_Destination, _Destination_size_CHARs, _Value, _Count)


def _wcsset_l(_Destination, _Value, _Locale):
    return _wcsset(_Destination, _Value)


def _wcsset_s_l(_Destination, _Destination_size_CHARs, _Value, _Locale):
    return _wcsset_s(_Destination, _Destination_size_CHARs, _Value)


def __T(x):
    return x


def _T(x):
    return __T(x)


def _TEXT(x):
    return __T(x)


iswalnum = isalnum
iswalpha = isalpha
iswascii = isascii
iswcntrl = iscntrl
iswdigit = isdigit
iswgraph = isgraph
iswlower = islower
iswprint = isprint
iswpunct = ispunct
iswspace = isspace
iswupper = isupper
iswxdigit = isxdigit
towupper = toupper
towlower = tolower

_iswalnum_l = isalnum
_iswalpha_l = isalpha
_iswascii_l = isascii
_iswcntrl_l = iscntrl
_iswdigit_l = isdigit
_iswgraph_l = isgraph
_iswlower_l = islower
_iswprint_l = isprint
_iswpunct_l = ispunct
_iswspace_l = isspace
_iswupper_l = isupper
_iswxdigit_l = isxdigit
_towupper_l = toupper
_towlower_l = tolower


_tmain = wmain
_tWinMain = wWinMain
_tenviron = _wenviron
__targv = __wargv
_tprintf = wprintf
_tprintf_l = _wprintf_l
_tprintf_s = wprintf_s
_tprintf_s_l = _wprintf_s_l
_tprintf_p = _wprintf_p
_tprintf_p_l = _wprintf_p_l
_tcprintf = _cwprintf
_tcprintf_l = _cwprintf_l
_tcprintf_s = _cwprintf_s
_tcprintf_s_l = _cwprintf_s_l
_tcprintf_p = _cwprintf_p
_tcprintf_p_l = _cwprintf_p_l
_vtcprintf = _vcwprintf
_vtcprintf_l = _vcwprintf_l
_vtcprintf_s = _vcwprintf_s
_vtcprintf_s_l = _vcwprintf_s_l
_vtcprintf_p = _vcwprintf_p
_vtcprintf_p_l = _vcwprintf_p_l
_ftprintf = fwprintf
_ftprintf_l = _fwprintf_l
_ftprintf_s = fwprintf_s
_ftprintf_s_l = _fwprintf_s_l
_ftprintf_p = _fwprintf_p
_ftprintf_p_l = _fwprintf_p_l
_stprintf = swprintf
_stprintf_l = __swprintf_l
_stprintf_s = swprintf_s
_stprintf_s_l = _swprintf_s_l
_stprintf_p = _swprintf_p
_stprintf_p_l = _swprintf_p_l
_sctprintf = _scwprintf
_sctprintf_l = _scwprintf_l
_sctprintf_p = _scwprintf_p
_sctprintf_p_l = _scwprintf_p_l
_sntprintf = _snwprintf
_sntprintf_l = _snwprintf_l
_sntprintf_s = _snwprintf_s
_sntprintf_s_l = _snwprintf_s_l
_vtprintf = vwprintf
_vtprintf_l = _vwprintf_l
_vtprintf_s = vwprintf_s
_vtprintf_s_l = _vwprintf_s_l
_vtprintf_p = _vwprintf_p
_vtprintf_p_l = _vwprintf_p_l
_vftprintf = vfwprintf
_vftprintf_l = _vfwprintf_l
_vftprintf_s = vfwprintf_s
_vftprintf_s_l = _vfwprintf_s_l
_vftprintf_p = _vfwprintf_p
_vftprintf_p_l = _vfwprintf_p_l
_vstprintf = vswprintf
_vstprintf_l = _vswprintf_l
_vstprintf_s = vswprintf_s
_vstprintf_s_l = _vswprintf_s_l
_vstprintf_p = _vswprintf_p
_vstprintf_p_l = _vswprintf_p_l
_vsctprintf = _vscwprintf
_vsctprintf_l = _vscwprintf_l
_vsctprintf_p = _vscwprintf_p
_vsctprintf_p_l = _vscwprintf_p_l
_vsntprintf = _vsnwprintf
_vsntprintf_l = _vsnwprintf_l
_vsntprintf_s = _vsnwprintf_s
_vsntprintf_s_l = _vsnwprintf_s_l
_tscanf = wscanf
_tscanf_l = _wscanf_l
_tscanf_s = wscanf_s
_tscanf_s_l = _wscanf_s_l
_tcscanf = _cwscanf
_tcscanf_l = _cwscanf_l
_tcscanf_s = _cwscanf_s
_tcscanf_s_l = _cwscanf_s_l
_ftscanf = fwscanf
_ftscanf_l = _fwscanf_l
_ftscanf_s = fwscanf_s
_ftscanf_s_l = _fwscanf_s_l
_stscanf = swscanf
_stscanf_l = _swscanf_l
_stscanf_s = swscanf_s
_stscanf_s_l = _swscanf_s_l
_sntscanf = _snwscanf
_sntscanf_l = _snwscanf_l
_sntscanf_s = _snwscanf_s
_sntscanf_s_l = _snwscanf_s_l
_fgettc = fgetwc
_fgettc_nolock = _fgetwc_nolock
_fgettCHAR = _fgetwCHAR
_fgetts = fgetws
_fputtc = fputwc
_fputtc_nolock = _fputwc_nolock
_fputtCHAR = _fputwCHAR
_fputts = fputws
_cputts = _cputws
_cgetts = _cgetws
_cgetts_s = _cgetws_s
_gettc = getwc
_gettc_nolock = _getwc_nolock
_gettch = _getwch
_gettch_nolock = _getwch_nolock
_gettche = _getwche
_gettche_nolock = _getwche_nolock
_gettCHAR = getwCHAR
_gettCHAR_nolock = _getwCHAR_nolock
_getts = _getws
_getts_s = _getws_s
_puttc = putwc
_puttc_nolock = _putwc_nolock
_puttCHAR = putwCHAR
_puttCHAR_nolock = _putwCHAR_nolock
_puttch = _putwch
_puttch_nolock = _putwch_nolock
_putts = _putws
_ungettc = ungetwc
_ungettc_nolock = _ungetwc_nolock
_ungettch = _ungetwch
_ungettch_nolock = _ungetwch_nolock
_tcstod = wcstod
_tcstol = wcstol
_tcstoul = wcstoul
_tcstoi64 = _wcstoi64
_tcstoui64 = _wcstoui64
_tstof = _wtof
_tstol = _wtol
_tstoi = _wtoi
_tstoi64 = _wtoi64
_tcstod_l = _wcstod_l
_tcstol_l = _wcstol_l
_tcstoul_l = _wcstoul_l
_tcstoi64_l = _wcstoi64_l
_tcstoui64_l = _wcstoui64_l
_tstof_l = _wtof_l
_tstol_l = _wtol_l
_tstoi_l = _wtoi_l
_tstoi64_l = _wtoi64_l
_itot_s = _itow_s
_ltot_s = _ltow_s
_ultot_s = _ultow_s
_itot = _itow
_ltot = _ltow
_ultot = _ultow
_ttoi = _wtoi
_ttol = _wtol
_ttoi64 = _wtoi64
_i64tot_s = _i64tow_s
_ui64tot_s = _ui64tow_s
_i64tot = _i64tow
_ui64tot = _ui64tow
_tcscat = wcscat
_tcscat_s = wcscat_s
_tcschr = wcschr
_tcscpy = wcscpy
_tcscpy_s = wcscpy_s
_tcscspn = wcscspn
_tcslen = wcslen
_tcsnlen = wcsnlen
_tcsncat = wcsncat
_tcsncat_s = wcsncat_s
_tcsncat_l = _wcsncat_l
_tcsncat_s_l = _wcsncat_s_l
_tcsncpy = wcsncpy
_tcsncpy_s = wcsncpy_s
_tcsncpy_l = _wcsncpy_l
_tcsncpy_s_l = _wcsncpy_s_l
_tcspbrk = wcspbrk
_tcsrchr = wcsrchr
_tcsspn = wcsspn
_tcsstr = wcsstr
_tcstok = wcstok
_tcstok_s = wcstok_s
_tcstok_l = _wcstok_l
_tcstok_s_l = _wcstok_s_l
_tcserror = _wcserror
_tcserror_s = _wcserror_s
__tcserror = __wcserror
__tcserror_s = __wcserror_s
_tcsdup = _wcsdup
_tcsnset = _wcsnset
_tcsnset_s = _wcsnset_s
_tcsnset_l = _wcsnset_l
_tcsnset_s_l = _wcsnset_s_l
_tcsrev = _wcsrev
_tcsset = _wcsset
_tcsset_s = _wcsset_s
_tcsset_l = _wcsset_l
_tcsset_s_l = _wcsset_s_l
_tcscmp = wcscmp
_tcsicmp = _wcsicmp
_tcsicmp_l = _wcsicmp_l
_tcsnccmp = wcsncmp
_tcsncmp = wcsncmp
_tcsncicmp = _wcsnicmp
_tcsncicmp_l = _wcsnicmp_l
_tcsnicmp = _wcsnicmp
_tcsnicmp_l = _wcsnicmp_l
_tcscoll = wcscoll
_tcscoll_l = _wcscoll_l
_tcsicoll = _wcsicoll
_tcsicoll_l = _wcsicoll_l
_tcsnccoll = _wcsncoll
_tcsnccoll_l = _wcsncoll_l
_tcsncoll = _wcsncoll
_tcsncoll_l = _wcsncoll_l
_tcsncicoll = _wcsnicoll
_tcsncicoll_l = _wcsnicoll_l
_tcsnicoll = _wcsnicoll
_tcsnicoll_l = _wcsnicoll_l
_tcsdup_dbg = _wcsdup_dbg
_texecl = _wexecl
_texecle = _wexecle
_texeclp = _wexeclp
_texeclpe = _wexeclpe
_texecv = _wexecv
_texecve = _wexecve
_texecvp = _wexecvp
_texecvpe = _wexecvpe
_tspawnl = _wspawnl
_tspawnle = _wspawnle
_tspawnlp = _wspawnlp
_tspawnlpe = _wspawnlpe
_tspawnv = _wspawnv
_tspawnve = _wspawnve
_tspawnvp = _wspawnvp
_tspawnvpe = _wspawnvpe
_tsystem = _wsystem
_tasctime = _wasctime
_tctime = _wctime
_tctime32 = _wctime32
_tctime64 = _wctime64
_tstrdate = _wstrdate
_tstrtime = _wstrtime
_tutime = _wutime
_tutime32 = _wutime32
_tutime64 = _wutime64
_tcsftime = wcsftime
_tcsftime_l = _wcsftime_l
_tasctime_s = _wasctime_s
_tctime_s = _wctime_s
_tctime32_s = _wctime32_s
_tctime64_s = _wctime64_s
_tstrdate_s = _wstrdate_s
_tstrtime_s = _wstrtime_s
_tchdir = _wchdir
_tgetcwd = _wgetcwd
_tgetdcwd = _wgetdcwd
_tgetdcwd_nolock = _wgetdcwd_nolock
_tmkdir = _wmkdir
_trmdir = _wrmdir
_tgetcwd_dbg = _wgetcwd_dbg
_tgetdcwd_dbg = _wgetdcwd_dbg
_tgetdcwd_lk_dbg = _wgetdcwd_lk_dbg
_tfullpath = _wfullpath
_tgetenv = _wgetenv
_tgetenv_s = _wgetenv_s
_tdupenv_s = _wdupenv_s
_tmakepath = _wmakepath
_tmakepath_s = _wmakepath_s
_tpgmptr = _wpgmptr
_get_tpgmptr = _get_wpgmptr
_tputenv = _wputenv
_tputenv_s = _wputenv_s
_tsearchenv = _wsearchenv
_tsearchenv_s = _wsearchenv_s
_tsplitpath = _wsplitpath
_tsplitpath_s = _wsplitpath_s
_tfullpath_dbg = _wfullpath_dbg
_tdupenv_s_dbg = _wdupenv_s_dbg
_tfdopen = _wfdopen
_tfsopen = _wfsopen
_tfopen = _wfopen
_tfopen_s = _wfopen_s
_tfreopen = _wfreopen
_tfreopen_s = _wfreopen_s
_tperror = _wperror
_tpopen = _wpopen
_ttempnam = _wtempnam
_ttmpnam = _wtmpnam
_ttmpnam_s = _wtmpnam_s
_ttempnam_dbg = _wtempnam_dbg
_taccess = _waccess
_taccess_s = _waccess_s
_tchmod = _wchmod
_tcreat = _wcreat
_tfindfirst = _wfindfirst
_tfindfirst32 = _wfindfirst32
_tfindfirst64 = _wfindfirst64
_tfindfirsti64 = _wfindfirsti64
_tfindfirst32i64 = _wfindfirst32i64
_tfindfirst64i32 = _wfindfirst64i32
_tfindnext = _wfindnext
_tfindnext32 = _wfindnext32
_tfindnext64 = _wfindnext64
_tfindnexti64 = _wfindnexti64
_tfindnext32i64 = _wfindnext32i64
_tfindnext64i32 = _wfindnext64i32
_tmktemp = _wmktemp
_tmktemp_s = _wmktemp_s
_topen = _wopen
_tremove = _wremove
_trename = _wrename
_tsopen = _wsopen
_tsopen_s = _wsopen_s
_tunlink = _wunlink
_tfinddata_t = _wfinddata_t
_tfinddata32_t = _wfinddata32_t
_tfinddata64_t = _wfinddata64_t
_tfinddatai64_t = _wfinddatai64_t
_tfinddata32i64_t = _wfinddata32i64_t
_tfinddata64i32_t = _wfinddata64i32_t
_tstat = _wstat
_tstat32 = _wstat32
_tstat32i64 = _wstat32i64
_tstat64 = _wstat64
_tstat64i32 = _wstat64i32
_tstati64 = _wstati64
_tsetlocale = _wsetlocale
_tcsclen = wcslen
_tcscnlen = wcsnlen


_ftcscpy = _tcscpy
_ftcscat = _tcscat
_ftcschr = _tcschr
_ftcscspn = _tcscspn
_ftcslen = _tcslen
_ftcsncat = _tcsncat
_ftcsncpy = _tcsncpy
_ftcspbrk = _tcspbrk
_ftcsrchr = _tcsrchr
_ftcsspn = _tcsspn
_ftcsstr = _tcsstr
_ftcstok = _tcstok
_ftcsdup = _tcsdup
_ftcsnset = _tcsnset
_ftcsrev = _tcsrev
_ftcsset = _tcsset
_ftcscmp = _tcscmp
_ftcsicmp = _tcsicmp
_ftcsnccmp = _tcsnccmp
_ftcsncmp = _tcsncmp
_ftcsncicmp = _tcsncicmp
_ftcsnicmp = _tcsnicmp
_ftcscoll = _tcscoll
_ftcsicoll = _tcsicoll
_ftcsnccoll = _tcsnccoll
_ftcsncoll = _tcsncoll
_ftcsncicoll = _tcsncicoll
_ftcsnicoll = _tcsnicoll
_ftcsclen = _tcsclen
_ftcsnccat = _tcsnccat
_ftcsnccpy = _tcsnccpy
_ftcsncset = _tcsncset
_ftcsdec = _tcsdec
_ftcsinc = _tcsinc
_ftcsnbcnt = _tcsnbcnt
_ftcsnccnt = _tcsnccnt
_ftcsnextc = _tcsnextc
_ftcsninc = _tcsninc
_ftcsspnp = _tcsspnp
_ftcslwr = _tcslwr
_ftcsupr = _tcsupr
_ftclen = _tclen
_ftccpy = _tccpy
_ftccmp = _tccmp


_istalnum = iswalnum
_istalnum_l = _iswalnum_l
_istalpha = iswalpha
_istalpha_l = _iswalpha_l
_istascii = iswascii
_istcntrl = iswcntrl
_istcntrl_l = _iswcntrl_l
_istdigit = iswdigit
_istdigit_l = _iswdigit_l
_istgraph = iswgraph
_istgraph_l = _iswgraph_l
_istlower = iswlower
_istlower_l = _iswlower_l
_istprint = iswprint
_istprint_l = _iswprint_l
_istpunct = iswpunct
_istpunct_l = _iswpunct_l
_istspace = iswspace
_istspace_l = _iswspace_l
_istupper = iswupper
_istupper_l = _iswupper_l
_istxdigit = iswxdigit
_istxdigit_l = _iswxdigit_l
_totupper = towupper
_totupper_l = _towupper_l
_totlower = towlower
_totlower_l = _towlower_l



_tcsnccat = wcsncat
_tcsnccat_s = wcsncat_s
_tcsnccat_l = _wcsncat_l
_tcsnccat_s_l = _wcsncat_s_l
_tcsnccpy = wcsncpy
_tcsnccpy_s = wcsncpy_s
_tcsnccpy_l = _wcsncpy_l
_tcsnccpy_s_l = _wcsncpy_s_l
_tcsncset = _wcsnset
_tcsncset_s = _wcsnset_s
_tcsncset_l = _wcsnset_l
_tcsncset_s_l = _wcsnset_s_l
_tcsdec = _wcsdec
_tcsinc = _wcsinc
_tcsnbcnt = _wcsncnt
_tcsnccnt = _wcsncnt
_tcsnextc = _wcsnextc
_tcsninc = _wcsninc
_tcsspnp = _wcsspnp
_tcslwr = _wcslwr
_tcslwr_l = _wcslwr_l
_tcslwr_s = _wcslwr_s
_tcslwr_s_l = _wcslwr_s_l
_tcsupr = _wcsupr
_tcsupr_l = _wcsupr_l
_tcsupr_s = _wcsupr_s
_tcsupr_s_l = _wcsupr_s_l
_tcsxfrm = wcsxfrm
_tcsxfrm_l = _wcsxfrm_l


from string_h import * # NOQA

_tcscat = strcat
_tcscpy = strcpy
_tcsdup = _strdup
_tcslen = strlen


from mbstring_h import * # NOQA

_tcschr = _mbschr
_tcscspn = _mbscspn
_tcsncat = _mbsnbcat

_tcsncpy = _mbsnbcpy

_tcspbrk = _mbspbrk
_tcsrchr = _mbsrchr
_tcsspn = _mbsspn
_tcsstr = _mbsstr
_tcstok = _mbstok
_tcsnset = _mbsnbset
_tcsrev = _mbsrev
_tcsset = _mbsset
_tcscmp = _mbscmp
_tcsicmp = _mbsicmp
_tcsnccmp = _mbsncmp
_tcsncmp = _mbsnbcmp
_tcsncicmp = _mbsnicmp
_tcsnicmp = _mbsnbicmp
_tcscoll = _mbscoll
_tcsicoll = _mbsicoll
_tcsnccoll = _mbsncoll
_tcsncoll = _mbsnbcoll
_tcsncicoll = _mbsnicoll
_tcsnicoll = _mbsnbicoll
_tcsclen = _mbslen
_tclen = _mbclen
_tccpy = _mbccpy
_tccpy_s = _mbccpy_s
_tccpy_s_l = _mbccpy_s_l
_PUC = POINTER(CHAR)
_CPUC = POINTER(CHAR)
_PC = POINTER(CHAR)
_CRPC = POINTER(CHAR)
_CPC = POINTER(CHAR)
_UI = UINT



_istlegal_l = _ismbclegal_l
_istprint = _ismbcprint
_istprint_l = _ismbcprint_l


__all__ = (
    '_tfreopen', '_tfullpath', '_istpunct_l', '_wcsdec', '_ui64tot', '_UI',
    '_strncat_l', '_istdigit', '_tcsncat_s', '_ftccpy', '_strnextc', '_tccpy',
    '_tcsrev', '_tcsncat_l', '_istlead', '_wcsninc', '_tfsopen', '_ftcspbrk',
    '_puttch_nolock', '_ftcsspnp', '_tstat32', '_tcscnlen_l', '_wcsinc', '_T',
    '_ungettch_nolock', '_strnset_s_l', '_tgetenv_s', '_vtcprintf_p_l', '__T',
    '_vsntprintf', '_tcsxfrm', '_texeclpe', '_topen', '_tcsncset', '_trmdir',
    '__tcserror_s', '_tcprintf_l', '_tcsncicmp', '_tcprintf_s', '_istupper',
    '_tcprintf_p', '_tcscspn', '_tstat', '_tcstoui64', '_tscanf_l', '_CPC',
    '_tcsnset_s', '_tstoi64_l', '_tprintf_s_l', '_ftcsnicmp', '_ftcsspn',
    '_tcsnset_l', '_tscanf_s', '_ftcsnccmp', '_fgettc_nolock', '_istspace',
    '_vftprintf_s_l', '_vsctprintf_l', '_strtok_l', '_tcsclen_l', '__targv',
    '_tchdir', '_tcsncoll', '_ftcsupr', '_vsctprintf_p', '_tcscpy_s', '_TEXT',
    '_wcsset_l', '_tcsnccat_s', '_tmain', '_tcstok_s_l', '_sctprintf_p_l',
    '_tcsncset_s_l', '_tcreat', '_ftcsinc', '_gettCHAR_nolock', '_tutime',
    '_wcsnset_s_l', '_vtcprintf_l', '_tdupenv_s', '_putts', '_sctprintf_l',
    '_istalpha_l', '_istpunct', '_puttc', '_texecvpe', '_istprint', '_strdec',
    '_tfinddata32i64_t', '_sctprintf_p', '_vtcprintf_p', '_vtcprintf_s',
    '_sntprintf_s_l', '_tcsicoll_l', '_istlower', '_tcsdup_dbg', '_tctime_s',
    '_ftcsnicoll', '_wcsncat_s_l', '_tfindnext', '_strncat_s_l', '_wcsnset_l',
    '_tcsinc', '_vsntprintf_l', '_tcsnccat_l', '_gettche', '_tstrtime', '_PC',
    '_tcsdec', '_tstrdate', '_tfinddata64i32_t', '_puttc_nolock', '_totlower',
    '_wcsncpy_l', '_ftscanf_s_l', '_vsntprintf_s', '_strncpy_s_l', '_wcsncnt',
    '_ftcsnset', '_tccpy_l', '_tspawnle', '_tcsnccat_s_l', '_tccpy_s', '_PUC',
    '_trename', '_tfopen', '_ftcsstr', '_tspawnlp', '_tsopen', '_ftcsncicoll',
    '_strset_l', '_gettCHAR', '_tcscnlen', '_tccmp', '_getts_s', '_fgettc',
    '_istlower_l', '_sntscanf_s_l', '_tstrtime_s', '_wcsspnp', '_fgetts',
    '_stscanf_s_l', '_tfinddatai64_t', '_tfinddata64_t', '_tcsnccpy_s_l',
    '_tspawnvpe', '_istlegal', '_fputtc_nolock', '_istleadbyte_l', '_puttch',
    '_tctime64', '_tcprintf_p_l', '_tgetdcwd_nolock', '_tprintf_s', '_gettc',
    '_tcsnicoll_l', '_sntprintf_l', '_stprintf_s_l', '_sntprintf_s', '_getts',
    '_tprintf_l', '_strncpy_l', '_tstat64i32', '_tfdopen', '_wcstok_s_l',
    '_totupper_l', '_tcsclen', '_ftcsnccpy', '_tfindfirst32', '_ftcsrchr',
    '_tfindnext32i64', '_tsearchenv_s', '_strspnp', '_sctprintf', '_tcsnextc',
    '_vftprintf_p_l', '_tfindnext64i32', '_tcsupr_s_l', '_tfindfirst32i64',
    '_stprintf_p', '_stprintf_s', '_sntprintf', '_tfindfirst64i32', '_cgetts',
    '_tcsicmp', '_ftprintf', '_stprintf_l', '_ultot_s', '_tpgmptr', '_tcsupr',
    '_tcsncpy_s_l', '_vtprintf', '_ftprintf_l', '_ftcsnbcnt', '_tcspbrk',
    '_ftprintf_s', '_ftprintf_p', '_tstof_l', '_tcscat_s', '_wcsnextc',
    '_tutime64', '_tcsncoll_l', '_tgetcwd', '_tgetdcwd_lk_dbg', '_tcsnicmp_l',
    '_ftcslwr', '_tcstod', '_tcstol', '_tcstok', '_ftcsncset', '_strinc',
    '_tcstoui64_l', '_CPUC', '_ttmpnam', '_tmkdir', '_wcstok_l', '_ungettc',
    '_wcsncpy_s_l', '_tstoi64', '_ftcsdup', '_ftcslen', '_ftcsncoll', '_ttoi',
    '_stscanf_s', '_gettch', '_ttol', '_vsntprintf_s_l', '_tremove', '_ultot',
    '_stscanf_l', '_ftccmp', '_ftcsncat', '_tcsxfrm_l', '_ftcsicmp', '_TEOF',
    '_tstrdate_s', '_tcsnset_s_l', '_tfindfirst', '_tcsnccoll', '_tcstoi64',
    '_tfindnexti64', '_tunlink', '_i64tot', '_stprintf_p_l', '_taccess_s',
    '_istgraph_l', '_tcscanf_s', '_tstat64', '_texeclp', '_tcscoll', '_ltot',
    '_ftcsnccat', '_tcslwr', '_tcscanf_l', '_texecle', '_tcsncicmp_l',
    '_ftcsicoll', '_istupper_l', '_tstat32i64', '_tcprintf_s_l', '_tpopen',
    '_vtprintf_p_l', '_istalnum_l', '_tenviron', '_tcsncmp', '_totlower_l',
    '_tspawnve', '_cgetts_s', '_texecv', '_itot_s', '_tspawnvp', '_tcsnccnt',
    '_texecl', '_tcsset', '_stprintf', '_tcsncset_s', '_tcsnccpy_s', '_CRPC',
    '_tcsnccpy_l', '_tfullpath_dbg', '_puttCHAR_nolock', '_tcsncset_l',
    '_tscanf', '__tcserror', '_tputenv', '_gettc_nolock', '_strset_s_l',
    '_sntscanf_s', '_tcsnicmp', '_tstoi_l', '_puttCHAR', '_fputtCHAR',
    '_sntscanf_l', '_strnset_l', '_vtcprintf', '_tstati64', '_tcsnicoll',
    '_istgraph', '_ftprintf_s_l', '_tcschr', '_istcntrl', '_ftcsncmp',
    '_tasctime_s', '_tprintf_p', '_totupper', '_tfinddata32_t', '_tcserror_s',
    '_sntscanf', '_tcsnccoll_l', '_tsetlocale', '_tcsupr_l', '_tcsnlen',
    '_gettche_nolock', '_tcsupr_s', '_ftcscat', '_tcsdup', '_tcsncat',
    '_vftprintf', '_tcslwr_l', '_ttempnam', '_ftscanf_s', '_tcstoul_l',
    '_ftscanf_l', '_ungettc_nolock', '_tcprintf', '_i64tot_s', '_istcntrl_l',
    '_tccpy_s_l', '_stscanf', '_tcslwr_s_l', '_tcscat', '_ftcstok', '_tcslen',
    '_ftcschr', '_tscanf_s_l', '_ttempnam_dbg', '_tcsnccpy', '_fputtc',
    '_tgetcwd_dbg', '_fputts', '_ftcsrev', '_texecvp', '_vtprintf_s', '_itot',
    '_vtprintf_p', '_ltot_s', '_tWinMain', '_tcstoi64_l', '_ftcsset', '_TINT',
    '_vtprintf_l', '_tchmod', '_tcsninc', '_tcscanf_s_l', '_vstprintf_l',
    '_vstprintf_s', '_vstprintf_p', '_vtprintf_s_l', '_tmktemp', '_tstol_l',
    '_tcsrchr', '_vstprintf_s_l', '_tfindfirsti64', '_tcsncicoll', '_tcsstr',
    '_tcsnccmp', '_ftcsncicmp', '_istspace_l', '_tmakepath', '_tcstod_l',
    '_strtok_s_l', '_ftprintf_p_l', '_istxdigit', '_tfindnext64', '_ftcsninc',
    '_tcsncpy_s', '_tgetdcwd_dbg', '_vsctprintf_p_l', '_ungettch', '_tcscmp',
    '_tcsncpy_l', '_tcsicmp_l', '_tclen', '_tcslwr_s', '_strninc', '_ftcscpy',
    '_tctime32_s', '_vtcprintf_s_l', '_tcstol_l', '_tfinddata_t', '_tsystem',
    '_wcsncat_l', '_tspawnlpe', '_tcsncpy', '_vstprintf', '_tmakepath_s',
    '_tctime32', '_wcsset_s_l', '_tsplitpath', '_tcsftime', '_tcscpy',
    '_tfopen_s', '_tcsnset', '_ftcscoll', '_tgetdcwd', '_tcsset_s_l',
    '_tputenv_s', '_tcsnccat', '_tasctime', '_ui64tot_s', '_tcscoll_l',
    '_vsctprintf', '_vftprintf_p', '_vftprintf_s', '_istprint_l', '_istascii',
    '_tcsncicoll_l', '_vftprintf_l', '_strncnt', '_ftclen', '_taccess',
    '_tprintf', '_tcsspn', '_istleadbyte', '_tsearchenv', '_get_tpgmptr',
    '_tstof', '_ftscanf', '_tstol', '_vstprintf_p_l', '_tstoi', '_istalnum',
    '_tfindfirst64', '_tfreopen_s', '_ftcsnccnt', '_tdupenv_s_dbg', '_ttoi64',
    '_tsplitpath_s', '_tcserror', '_tmktemp_s', '_tcsspnp', '_tspawnl',
    '_tspawnv', '_tprintf_p_l', '_ftcsclen', '_texecve', '_istdigit_l',
    '_ftcsdec', '_tcsnbcnt', '_tgetenv', '_istalpha', '_tutime32', '_ftcscmp',
    '_tcsftime_l', '_tfindnext32', '_istxdigit_l', '_tcstok_s', '_tctime',
    '_tcsncat_s_l', '_fgettCHAR', '_tcsicoll', '_tctime64_s', '_tcstok_l',
    '_tperror', '_cputts', '_ttmpnam_s', '_gettch_nolock', '_istlegal_l',
    '_tcstoul', '_ftcscspn', '_tcsset_s', '_ftcsnccoll', '_ftcsnextc',
    '_ftcsncpy', '_tcscanf', '_tsopen_s', '_tcsset_l', 'wctype_t', '_TSCHAR',
    'wINT_t', '_TCHAR', '_TXCHAR', '_TUCHAR',
)
