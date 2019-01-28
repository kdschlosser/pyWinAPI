import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_WINNLS_ = None
NOAPISET = None
DISABLE_NLS_DEPRECATION = None
NONLS = None
_NORMALIZE_ = None
STRICT = None
_M_CEE = None
GetDurationFormatEx_DEFINED = None

class _cpinfo(ctypes.Structure):
    pass


CPINFO = _cpinfo
LPCPINFO = POINTER(_cpinfo)


class _cpinfoexA(ctypes.Structure):
    pass


CPINFOEXA = _cpinfoexA
LPCPINFOEXA = POINTER(_cpinfoexA)


class _cpinfoexW(ctypes.Structure):
    pass


CPINFOEXW = _cpinfoexW
LPCPINFOEXW = POINTER(_cpinfoexW)


class _numberfmtA(ctypes.Structure):
    pass


NUMBERFMTA = _numberfmtA
LPNUMBERFMTA = POINTER(_numberfmtA)


class _numberfmtW(ctypes.Structure):
    pass


NUMBERFMTW = _numberfmtW
LPNUMBERFMTW = POINTER(_numberfmtW)


class _currencyfmtA(ctypes.Structure):
    pass


CURRENCYFMTA = _currencyfmtA
LPCURRENCYFMTA = POINTER(_currencyfmtA)


class _currencyfmtW(ctypes.Structure):
    pass


CURRENCYFMTW = _currencyfmtW
LPCURRENCYFMTW = POINTER(_currencyfmtW)


class _nlsversioninfo(ctypes.Structure):
    pass


NLSVERSIONINFO = _nlsversioninfo
LPNLSVERSIONINFO = POINTER(_nlsversioninfo)


NLSVERSIONINFO = _nlsversioninfo
LPNLSVERSIONINFO = POINTER(_nlsversioninfo)


class _nlsversioninfoex(ctypes.Structure):
    pass


NLSVERSIONINFOEX = _nlsversioninfoex
LPNLSVERSIONINFOEX = POINTER(_nlsversioninfoex)


class _FILEMUIINFO(ctypes.Structure):
    pass


FILEMUIINFO = _FILEMUIINFO
PFILEMUIINFO = POINTER(_FILEMUIINFO)




# /* + + Copyright (c) Microsoft Corporation All rights reserved. Module Name:
# winnls.h Abstract: Procedure declarations, constant definitions, and macros
# for the NLS component. --
if not defined(_WINNLS_):
    _WINNLS_ = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    if not defined(NOAPISET):
        # Datetime APISET dependencies
        from pyWinAPI.um.datetimeapi_h import * # NOQA

        # LibLoader Apiset dependencies
        from pyWinAPI.um.libloaderapi_h import * # NOQA
    # END IF


    if _MSC_VER >= 1200:
        pass
    # END IF


    # Deprecated attribute support for NLS
    # Disable NLS deprecation for the moment
    if not defined(DISABLE_NLS_DEPRECATION):
        DISABLE_NLS_DEPRECATION = VOID
    # END IF


    # Deprecated NLS types/functions
    if not defined(DISABLE_NLS_DEPRECATION):
        if defined(__cplusplus):
            if __cplusplus >= 201402:
                def DEPRECATED(x):
                    return [[deprecated(x)]]
            elif defined(_MSC_VER):
                if _MSC_VER > 1900:
                    def DEPRECATED(x):
                        return [[deprecated(x)]]
                else:
                    def DEPRECATED(x):
                        return __declspec(deprecated(x))
                # END IF   _MSC_VER > 1900

            else:
                DEPRECATED = VOID
            # END IF   C + + deprecation

        else:
            DEPRECATED = VOID
        # END IF


    else:
        DEPRECATED = VOID
    # END IF  DISABLE_NLS_DEPRECATION

    if not defined(NONLS):
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if defined(_MAC):
                from macwin32_h import * # NOQA
            # END IF


            if not defined(_NORMALIZE_):
                WINNORMALIZEAPI = DECLSPEC_IMPORT
            else:
                WINNORMALIZEAPI = VOID
            # END IF


            # //////////////////////////////////////////////////////////////////////////
            #
            # Constants
            # Define all constants for the NLS component here.
            # //////////////////////////////////////////////////////////////////////////
            #
            # String Length Maximums.
            MAX_LEADBYTES = 12            # 5 ranges, 2 bytes ea., 0 term.
            MAX_DEFAULTCHAR = 2            # single or DOUBLE byte

            # Surrogate pairs
            # Conversion examples:
            # A) The first character in the Surrogate range (D800,
            # DC00) as UTF-32:
            # 1. D800: binary 1101100000000000 (lower ten bits: 0000000000)
            # 2. DC00: binary 1101110000000000 (lower ten bits: 0000000000)
            # 3. Concatenate 0000000000 + 0000000000 = 0x0000
            # 4. Add 0x10000
            # Result: U + 10000. This is correct, since the first character in
            # the Supplementary character
            # range immediately follows the last code point in the 16-bit
            # UTF-16 range (U + FFFF)
            # B) A UTF-32 code point such as U + 2040A (this a CJK character
            # in CJK Extension B), and wish
            # to convert it in UTF-16:
            # 1. Subtract 0x10000 - Result: 0x1040A
            # 2. Split into two ten-bit pieces: 0001000001 0000001010
            # 3. Add 1101100000000000 (0xD800) to the high 10 bits piece
            # (0001000001) - Result: 1101100001000001 (0xD841)
            # 4. Add 1101110000000000 (0xDC00) to the low 10 bits piece
            # (0000001010) - Result: 1101110000001010 (0xDC0A)
            # RESULT: The surrogate pair: U + D841, U + DC0A
            # Special Unicode code point values, for use with UTF-16 surrogate
            # pairs.
            HIGH_SURROGATE_START = 0xD800
            HIGH_SURROGATE_END = 0xDBFF
            LOW_SURROGATE_START = 0xDC00
            LOW_SURROGATE_END = 0xDFFF
            # MBCS and Unicode Translation Flags.
            # Please use Unicode, either UTF-16 (WCHAR) or UTF-8 (CP_UTF8)
            # MB_PRECOMPOSED and MB_COMPOSITE are deprecated, not recommended,
            # and
            # provide out-of-date behavior.
            # Windows typically uses Unicode Normalization Form C type
            # sequences,
            # If explicit normalization forms are required, please use
            # NormalizeString.
            MB_PRECOMPOSED = 0x00000001            # DEPRECATED: use single precomposed characters when possible.
            MB_COMPOSITE = 0x00000002            # DEPRECATED: use multiple discrete characters when possible.
            MB_USEGLYPHCHARS = 0x00000004            # DEPRECATED: use glyph chars, not ctrl chars
            MB_ERR_INVALID_CHARS = 0x00000008            # error for invalid chars
            # WC_COMPOSITECHECK, WC_DISCARDNS and WC_SEPCHARS are deprecated,
            # not recommended,
            # and provide out-of-date behavior.
            # Windows typically uses Unicode Normalization Form C type
            # sequences,
            # If explicit normalization forms are required, please use
            # NormalizeString.
            WC_COMPOSITECHECK = 0x00000200            # convert composite to precomposed
            # efine WC_DISCARDNS   0x00000010 // discard non-spacing chars  //
            # Used with WC_COMPOSITECHECK
            # efine WC_SEPCHARS   0x00000020 // generate separate chars  //
            # Used with WC_COMPOSITECHECK
            # efine WC_DEFAULTCHAR  0x00000040 // replace w/ default CHAR  //
            # Used with WC_COMPOSITECHECK
            if WINVER >= 0x0600:
                WC_ERR_INVALID_CHARS = 0x00000080                # error for invalid chars
            # END IF


            if WINVER >= 0x0500:
                WC_NO_BEST_FIT_CHARS = 0x00000400                # do not use best fit chars
            # END IF  WINVER >= 0x0500

            # Character Type Flags.
            CT_CTYPE1 = 0x00000001            # ctype 1 information
            CT_CTYPE2 = 0x00000002            # ctype 2 information
            CT_CTYPE3 = 0x00000004            # ctype 3 information

            # CType 1 Flag Bits.
            C1_UPPER = 0x0001            # upper case
            C1_LOWER = 0x0002            # lower case
            C1_DIGIT = 0x0004            # decimal digits
            C1_SPACE = 0x0008            # spacing characters
            C1_PUNCT = 0x0010            # punctuation characters
            C1_CNTRL = 0x0020            # control characters
            C1_BLANK = 0x0040            # blank characters
            C1_XDIGIT = 0x0080            # other digits
            C1_ALPHA = 0x0100            # any linguistic character
            C1_DEFINED = 0x0200            # defined character

            # CType 2 Flag Bits.
            C2_LEFTTORIGHT = 0x0001            # left to right
            C2_RIGHTTOLEFT = 0x0002            # right to left
            C2_EUROPENUMBER = 0x0003            # European number, digit
            C2_EUROPESEPARATOR = 0x0004            # European numeric separator
            C2_EUROPETERMINATOR = 0x0005            # European numeric terminator
            C2_ARABICNUMBER = 0x0006            # Arabic number
            C2_COMMONSEPARATOR = 0x0007            # common numeric separator
            C2_BLOCKSEPARATOR = 0x0008            # block separator
            C2_SEGMENTSEPARATOR = 0x0009            # segment separator
            C2_WHITESPACE = 0x000A            # white space
            C2_OTHERNEUTRAL = 0x000B            # other neutrals
            C2_NOTAPPLICABLE = 0x0000            # no implicit directionality

            # CType 3 Flag Bits.
            C3_NONSPACING = 0x0001            # nonspacing character
            C3_DIACRITIC = 0x0002            # diacritic mark
            C3_VOWELMARK = 0x0004            # vowel mark
            C3_SYMBOL = 0x0008            # symbols
            C3_KATAKANA = 0x0010            # katakana character
            C3_HIRAGANA = 0x0020            # hiragana character
            C3_HALFWIDTH = 0x0040            # half width character
            C3_FULLWIDTH = 0x0080            # full width character
            C3_IDEOGRAPH = 0x0100            # ideographic character
            C3_KASHIDA = 0x0200            # Arabic kashida character
            C3_LEXICAL = 0x0400            # lexical character
            C3_HIGHSURROGATE = 0x0800            # high surrogate code unit
            C3_LOWSURROGATE = 0x1000            # low surrogate code unit
            C3_ALPHA = 0x8000            # any linguistic CHAR (C1_ALPHA)
            C3_NOTAPPLICABLE = 0x0000            # ctype 3 is not applicable

            # String Flags.
            NORM_IGNORECASE = 0x00000001            # ignore case
            NORM_IGNORENONSPACE = 0x00000002            # ignore nonspacing chars
            NORM_IGNORESYMBOLS = 0x00000004            # ignore symbols
            LINGUISTIC_IGNORECASE = 0x00000010            # linguistically appropriate 'ignore case'
            LINGUISTIC_IGNOREDIACRITIC = 0x00000020            # linguistically appropriate 'ignore nonspace'
            NORM_IGNOREKANATYPE = 0x00010000            # ignore kanatype
            NORM_IGNOREWIDTH = 0x00020000            # ignore width
            NORM_LINGUISTIC_CASING = 0x08000000            # use linguistic rules for casing

            # Locale Independent Mapping Flags.
            MAP_FOLDCZONE = 0x00000010            # fold compatibility zone chars
            MAP_PRECOMPOSED = 0x00000020            # convert to precomposed chars
            MAP_COMPOSITE = 0x00000040            # convert to composite chars
            MAP_FOLDDIGITS = 0x00000080            # all digits to ASCII 0-9
            if WINVER >= 0x0500:
                MAP_EXPAND_LIGATURES = 0x00002000                # expand all ligatures
            # END IF  WINVER >= 0x0500

            # Locale Dependent Mapping Flags.
            LCMAP_LOWERCASE = 0x00000100            # lower case letters
            LCMAP_UPPERCASE = 0x00000200            # UPPER CASE LETTERS
            if WINVER >= _WIN32_WINNT_WIN7:
                LCMAP_TITLECASE = 0x00000300                # Title Case Letters
            # END IF   (WINVER >= _WIN32_WINNT_WIN7)

            LCMAP_SORTKEY = 0x00000400            # WC sort key (normalize)
            LCMAP_BYTEREV = 0x00000800            # byte reversal
            LCMAP_HIRAGANA = 0x00100000            # map katakana to hiragana
            LCMAP_KATAKANA = 0x00200000            # map hiragana to katakana
            LCMAP_HALFWIDTH = 0x00400000            # map DOUBLE byte to single byte
            LCMAP_FULLWIDTH = 0x00800000            # map single byte to DOUBLE byte
            LCMAP_LINGUISTIC_CASING = 0x01000000            # use linguistic rules for casing
            LCMAP_SIMPLIFIED_CHINESE = 0x02000000            # map traditional chinese to simplified chinese
            LCMAP_TRADITIONAL_CHINESE = 0x04000000            # map simplified chinese to traditional chinese
            if WINVER >= _WIN32_WINNT_WIN8:
                LCMAP_SORTHANDLE = 0x20000000
                LCMAP_HASH = 0x00040000
            # END IF   (WINVER >= _WIN32_WINNT_WIN7)

            # Search Flags
            FIND_STARTSWITH = 0x00100000            # see if value is at the beginning of source
            FIND_ENDSWITH = 0x00200000            # see if value is at the end of source
            FIND_FROMSTART = 0x00400000            # look for value in source, starting at the beginning
            FIND_FROMEND = 0x00800000            # look for value in source, starting at the end

            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            # Language Group Enumeration Flags.
            # The "Language Group" concept is an obsolete concept.
            # The groups returned are not well defined, arbitrary,
            # inconsistent, inaccurate,
            # no longer maintained, and no longer supported.
            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            LGRPID_INSTALLED = 0x00000001            # installed language group ids
            LGRPID_SUPPORTED = 0x00000002            # supported language group ids


            # Locale Enumeration Flags.
            LCID_INSTALLED = 0x00000001            # installed locale ids
            LCID_SUPPORTED = 0x00000002            # supported locale ids
            LCID_ALTERNATE_SORTS = 0x00000004            # alternate sort locale ids

            if WINVER >= _WIN32_WINNT_VISTA:
                # Named based enumeration flags.
                LOCALE_ALL = 0                # enumerate all named based locales
                LOCALE_WINDOWS = 0x00000001                # shipped locales and/or replacements for them
                LOCALE_SUPPLEMENTAL = 0x00000002                # supplemental locales only
                LOCALE_ALTERNATE_SORTS = 0x00000004                # alternate sort locales
                LOCALE_REPLACEMENT = 0x00000008                # locales that replace shipped locales (callback flag only)
            # END IF   (WINVER >= _WIN32_WINNT_VISTA)

            if WINVER >= _WIN32_WINNT_WIN7:
                # Locales that are "neutral"
                # (language only, region data is default)
                LOCALE_NEUTRALDATA = 0x00000010
                LOCALE_SPECIFICDATA = 0x00000020                # Locales that contain language and region data
            # END IF   (WINVER >= _WIN32_WINNT_WIN7)


            # Code Page Enumeration Flags.
            CP_INSTALLED = 0x00000001            # installed code page ids
            CP_SUPPORTED = 0x00000002            # supported code page ids


            # Sorting Flags.
            # WORD Sort: culturally correct sort
            # hyphen and apostrophe are special cased
            # example: "coop" and "co-op" will sort together in a list
            # co_op  <------- underscore (symbol)
            # coat
            # comb
            # coop
            # co-op  <------- hyphen (punctuation)
            # cork
            # went
            # were
            # we're  <------- apostrophe (punctuation)
            # STRING Sort: hyphen and apostrophe will sort with all other
            # symbols
            # co-op  <------- hyphen (punctuation)
            # co_op  <------- underscore (symbol)
            # coat
            # comb
            # coop
            # cork
            # we're  <------- apostrophe (punctuation)
            # went
            # were
            SORT_STRINGSORT = 0x00001000            # use string sort method

            # Sort digits as numbers (ie: 2 comes before 10)
            if WINVER >= _WIN32_WINNT_WIN7:
                SORT_DIGITSASNUMBERS = 0x00000008                # use digits as numbers sort method
            # END IF   (WINVER >= _WIN32_WINNT_WIN7)

            # Compare String Return Values.
            CSTR_LESS_THAN = 1            # string 1 less than string 2
            CSTR_EQUAL = 2            # string 1 equal to string 2
            CSTR_GREATER_THAN = 3            # string 1 greater than string 2

            # Code Page Default Values.
            # Please Use Unicode, either UTF-16 (as in WCHAR) or UTF-8
            # (code page CP_ACP)
            CP_ACP = 0            # default to ANSI code page
            CP_OEMCP = 1            # default to OEM code page
            CP_MACCP = 2            # default to MAC code page
            CP_THREAD_ACP = 3            # current thread's ANSI code page
            CP_SYMBOL = 42            # SYMBOL translations
            CP_UTF7 = 65000            # UTF-7 translation
            CP_UTF8 = 65001            # UTF-8 translation

            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            # Country/Region Codes.
            # DEPRECATED: The GEOID concept is deprecated, please use
            # Country/Region Names instead, eg: "US" instead of a GEOID like
            # 244.
            # See the documentation for GetGeoInfoEx.
            # WARNING: These values are arbitrarily assigned values, please use
            # standard country/region names instead, such as "US".
            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            CTRY_DEFAULT = 0
            CTRY_ALBANIA = 355            # Albania
            CTRY_ALGERIA = 213            # Algeria
            CTRY_ARGENTINA = 54            # Argentina
            CTRY_ARMENIA = 374            # Armenia
            CTRY_AUSTRALIA = 61            # Australia
            CTRY_AUSTRIA = 43            # Austria
            CTRY_AZERBAIJAN = 994            # Azerbaijan
            CTRY_BAHRAIN = 973            # Bahrain
            CTRY_BELARUS = 375            # Belarus
            CTRY_BELGIUM = 32            # Belgium
            CTRY_BELIZE = 501            # Belize
            CTRY_BOLIVIA = 591            # Bolivia
            CTRY_BRAZIL = 55            # Brazil
            CTRY_BRUNEI_DARUSSALAM = 673            # Brunei Darussalam
            CTRY_BULGARIA = 359            # Bulgaria
            CTRY_CANADA = 2            # Canada
            CTRY_CARIBBEAN = 1            # Caribbean
            CTRY_CHILE = 56            # Chile
            CTRY_COLOMBIA = 57            # Colombia
            CTRY_COSTA_RICA = 506            # Costa Rica
            CTRY_CROATIA = 385            # Croatia
            CTRY_CZECH = 420            # Czech Republic
            CTRY_DENMARK = 45            # Denmark
            CTRY_DOMINICAN_REPUBLIC = 1            # Dominican Republic
            CTRY_ECUADOR = 593            # Ecuador
            CTRY_EGYPT = 20            # Egypt
            CTRY_EL_SALVADOR = 503            # El Salvador
            CTRY_ESTONIA = 372            # Estonia
            CTRY_FAEROE_ISLANDS = 298            # Faeroe Islands
            CTRY_FINLAND = 358            # Finland
            CTRY_FRANCE = 33            # France
            CTRY_GEORGIA = 995            # Georgia
            CTRY_GERMANY = 49            # Germany
            CTRY_GREECE = 30            # Greece
            CTRY_GUATEMALA = 502            # Guatemala
            CTRY_HONDURAS = 504            # Honduras
            CTRY_HONG_KONG = 852            # Hong Kong S.A.R., P.R.C.
            CTRY_HUNGARY = 36            # Hungary
            CTRY_ICELAND = 354            # Iceland
            CTRY_INDIA = 91            # India
            CTRY_INDONESIA = 62            # Indonesia
            CTRY_IRAN = 981            # Iran
            CTRY_IRAQ = 964            # Iraq
            CTRY_IRELAND = 353            # Ireland
            CTRY_ISRAEL = 972            # Israel
            CTRY_ITALY = 39            # Italy
            CTRY_JAMAICA = 1            # Jamaica
            CTRY_JAPAN = 81            # Japan
            CTRY_JORDAN = 962            # Jordan
            CTRY_KAZAKSTAN = 7            # Kazakstan
            CTRY_KENYA = 254            # Kenya
            CTRY_KUWAIT = 965            # Kuwait
            CTRY_KYRGYZSTAN = 996            # Kyrgyzstan
            CTRY_LATVIA = 371            # Latvia
            CTRY_LEBANON = 961            # Lebanon
            CTRY_LIBYA = 218            # Libya
            CTRY_LIECHTENSTEIN = 41            # Liechtenstein
            CTRY_LITHUANIA = 370            # Lithuania
            CTRY_LUXEMBOURG = 352            # Luxembourg
            CTRY_MACAU = 853            # Macao SAR, PRC
            CTRY_MACEDONIA = 389            # Former Yugoslav Republic of Macedonia
            CTRY_MALAYSIA = 60            # Malaysia
            CTRY_MALDIVES = 960            # Maldives
            CTRY_MEXICO = 52            # Mexico
            CTRY_MONACO = 33            # Principality of Monaco
            CTRY_MONGOLIA = 976            # Mongolia
            CTRY_MOROCCO = 212            # Morocco
            CTRY_NETHERLANDS = 31            # Netherlands
            CTRY_NEW_ZEALAND = 64            # New Zealand
            CTRY_NICARAGUA = 505            # Nicaragua
            CTRY_NORWAY = 47            # Norway
            CTRY_OMAN = 968            # Oman
            CTRY_PAKISTAN = 92            # Islamic Republic of Pakistan
            CTRY_PANAMA = 507            # Panama
            CTRY_PARAGUAY = 595            # Paraguay
            CTRY_PERU = 51            # Peru
            CTRY_PHILIPPINES = 63            # Republic of the Philippines
            CTRY_POLAND = 48            # Poland
            CTRY_PORTUGAL = 351            # Portugal
            CTRY_PRCHINA = 86            # People's Republic of China
            CTRY_PUERTO_RICO = 1            # Puerto Rico
            CTRY_QATAR = 974            # Qatar
            CTRY_ROMANIA = 40            # Romania
            CTRY_RUSSIA = 7            # Russia
            CTRY_SAUDI_ARABIA = 966            # Saudi Arabia
            CTRY_SERBIA = 381            # Serbia
            CTRY_SINGAPORE = 65            # Singapore
            CTRY_SLOVAK = 421            # Slovak Republic
            CTRY_SLOVENIA = 386            # Slovenia
            CTRY_SOUTH_AFRICA = 27            # South Africa
            CTRY_SOUTH_KOREA = 82            # Korea
            CTRY_SPAIN = 34            # Spain
            CTRY_SWEDEN = 46            # Sweden
            CTRY_SWITZERLAND = 41            # Switzerland
            CTRY_SYRIA = 963            # Syria
            CTRY_TAIWAN = 886            # Taiwan
            CTRY_TATARSTAN = 7            # Tatarstan
            CTRY_THAILAND = 66            # Thailand
            CTRY_TRINIDAD_Y_TOBAGO = 1            # Trinidad y Tobago
            CTRY_TUNISIA = 216            # Tunisia
            CTRY_TURKEY = 90            # Turkey
            CTRY_UAE = 971            # U.A.E.
            CTRY_UKRAINE = 380            # Ukraine
            CTRY_UNITED_KINGDOM = 44            # United Kingdom
            CTRY_UNITED_STATES = 1            # United States
            CTRY_URUGUAY = 598            # Uruguay
            CTRY_UZBEKISTAN = 7            # Uzbekistan
            CTRY_VENEZUELA = 58            # Venezuela
            CTRY_VIET_NAM = 84            # Viet Nam
            CTRY_YEMEN = 967            # Yemen
            CTRY_ZIMBABWE = 263            # Zimbabwe

            # Locale Types.
            # These types are used for the GetLocaleInfo NLS API routine.
            # Some of these types are also used for the SetLocaleInfo NLS API
            # routine.
            # The following LCTypes may be used in combination with any other
            # LCTypes.
            # LOCALE_NOUSEROVERRIDE is also used in GetTimeFormat and
            # GetDateFormat.
            # LOCALE_RETURN_NUMBER will return the result from GetLocaleInfo
            # as a
            # number instead of a string. This flag is only valid for the
            # LCTypes
            # beginning with LOCALE_I.
            # DEPRECATED: LOCALE_USE_CP_ACP is used in many of the A (Ansi)
            # apis that need
            # to do string translation. Callers are encouraged to use the W
            # (WCHAR/Unicode) apis instead.
            LOCALE_NOUSEROVERRIDE = 0x80000000            # Not Recommended - do not use user overrides
            LOCALE_USE_CP_ACP = 0x40000000            # DEPRECATED, call Unicode APIs instead: use the system ACP
            if WINVER >= 0x0400:
                LOCALE_RETURN_NUMBER = 0x20000000                # return number instead of string
            # END IF  WINVER >= 0x0400

            if WINVER >= _WIN32_WINNT_WIN7:
                LOCALE_RETURN_GENITIVE_NAMES = 0x10000000                # Flag to return the Genitive forms of month names

                # Flag to allow returning neutral names/lcids for name
                # conversion
                LOCALE_ALLOW_NEUTRAL_NAMES = 0x08000000
            # END IF  (WINVER >= _WIN32_WINNT_WIN7)

            # The following LCTypes are mutually exclusive in that they may NOT
            # be used in combination with each other.
            # These are the various forms of the name of the locale:
            LOCALE_SLOCALIZEDDISPLAYNAME = 0x00000002            # localized name of locale, eg "German (Germany)" in UI language
            if WINVER >= _WIN32_WINNT_WIN7:
                # Display name (language + country/region usually) in English,
                # eg "German (Germany)"
                LOCALE_SENGLISHDISPLAYNAME = 0x00000072

                # Display name in native locale language, eg
                # "Deutsch (Deutschland)
                LOCALE_SNATIVEDISPLAYNAME = 0x00000073
            # END IF  (WINVER >= _WIN32_WINNT_WIN7)

            if WINVER >= _WIN32_WINNT_VISTA:
                # Language Display Name for a language, eg "German" in UI
                # language
                LOCALE_SLOCALIZEDLANGUAGENAME = 0x0000006F
            # END IF  (WINVER >= _WIN32_WINNT_VISTA)

            LOCALE_SENGLISHLANGUAGENAME = 0x00001001            # English name of language, eg "German"
            LOCALE_SNATIVELANGUAGENAME = 0x00000004            # native name of language, eg "Deutsch"
            LOCALE_SLOCALIZEDCOUNTRYNAME = 0x00000006            # localized name of country/region, eg "Germany" in UI language
            LOCALE_SENGLISHCOUNTRYNAME = 0x00001002            # English name of country/region, eg "Germany"
            LOCALE_SNATIVECOUNTRYNAME = 0x00000008            # native name of country/region, eg "Deutschland"

            # Additional LCTypes
            LOCALE_IDIALINGCODE = 0x00000005            # country/region dialing code, example: en-US and en-CA return 1.
            LOCALE_SLIST = 0x0000000C            # list item separator, eg "," for "1,2,3,4"
            LOCALE_IMEASURE = 0x0000000D            # 0 = metric, 1 = US measurement system
            LOCALE_SDECIMAL = 0x0000000E            # decimal separator, eg "." for 1,234.00
            LOCALE_STHOUSAND = 0x0000000F            # thousand separator, eg "," for 1,234.00
            LOCALE_SGROUPING = 0x00000010            # digit grouping, eg "3;0" for 1,000,000
            LOCALE_IDIGITS = 0x00000011            # number of fractional digits eg 2 for 1.00
            LOCALE_ILZERO = 0x00000012            # leading zeros for decimal, 0 for .97, 1 for 0.97
            LOCALE_INEGNUMBER = 0x00001010            # negative number mode, 0-4, see documentation
            LOCALE_SNATIVEDIGITS = 0x00000013            # native digits for 0-9, eg "0123456789"
            LOCALE_SCURRENCY = 0x00000014            # local monetary symbol, eg "$"
            LOCALE_SINTLSYMBOL = 0x00000015            # intl monetary symbol, eg "USD"
            LOCALE_SMONDECIMALSEP = 0x00000016            # monetary decimal separator, eg "." for $1,234.00
            LOCALE_SMONTHOUSANDSEP = 0x00000017            # monetary thousand separator, eg "," for $1,234.00
            LOCALE_SMONGROUPING = 0x00000018            # monetary grouping, eg "3;0" for $1,000,000.00
            LOCALE_ICURRDIGITS = 0x00000019            # local monetary digits, eg 2 for $1.00
            LOCALE_ICURRENCY = 0x0000001B            # positive currency mode, 0-3, see documentation
            LOCALE_INEGCURR = 0x0000001C            # negative currency mode, 0-15, see documentation
            LOCALE_SSHORTDATE = 0x0000001F            # SHORT date format string, eg "MM/dd/yyyy"
            LOCALE_SLONGDATE = 0x00000020            # LONG date format string, eg "dddd, MMMM dd, yyyy"
            LOCALE_STIMEFORMAT = 0x00001003            # time format string, eg "HH:mm:ss"
            LOCALE_SAM = 0x00000028            # AM designator, eg "AM"
            LOCALE_SPM = 0x00000029            # PM designator, eg "PM"
            LOCALE_ICALENDARTYPE = 0x00001009            # type of calendar specifier, eg CAL_GREGORIAN
            LOCALE_IOPTIONALCALENDAR = 0x0000100B            # additional calendar types specifier, eg CAL_GREGORIAN_US
            LOCALE_IFIRSTDAYOFWEEK = 0x0000100C            # first day of week specifier, 0-6, 0=Monday, 6=Sunday
            LOCALE_IFIRSTWEEKOFYEAR = 0x0000100D            # first week of year specifier, 0-2, see documentation
            LOCALE_SDAYNAME1 = 0x0000002A            # LONG name for Monday
            LOCALE_SDAYNAME2 = 0x0000002B            # LONG name for Tuesday
            LOCALE_SDAYNAME3 = 0x0000002C            # LONG name for Wednesday
            LOCALE_SDAYNAME4 = 0x0000002D            # LONG name for Thursday
            LOCALE_SDAYNAME5 = 0x0000002E            # LONG name for Friday
            LOCALE_SDAYNAME6 = 0x0000002F            # LONG name for Saturday
            LOCALE_SDAYNAME7 = 0x00000030            # LONG name for Sunday
            LOCALE_SABBREVDAYNAME1 = 0x00000031            # abbreviated name for Monday
            LOCALE_SABBREVDAYNAME2 = 0x00000032            # abbreviated name for Tuesday
            LOCALE_SABBREVDAYNAME3 = 0x00000033            # abbreviated name for Wednesday
            LOCALE_SABBREVDAYNAME4 = 0x00000034            # abbreviated name for Thursday
            LOCALE_SABBREVDAYNAME5 = 0x00000035            # abbreviated name for Friday
            LOCALE_SABBREVDAYNAME6 = 0x00000036            # abbreviated name for Saturday
            LOCALE_SABBREVDAYNAME7 = 0x00000037            # abbreviated name for Sunday
            LOCALE_SMONTHNAME1 = 0x00000038            # LONG name for January
            LOCALE_SMONTHNAME2 = 0x00000039            # LONG name for February
            LOCALE_SMONTHNAME3 = 0x0000003A            # LONG name for March
            LOCALE_SMONTHNAME4 = 0x0000003B            # LONG name for April
            LOCALE_SMONTHNAME5 = 0x0000003C            # LONG name for May
            LOCALE_SMONTHNAME6 = 0x0000003D            # LONG name for June
            LOCALE_SMONTHNAME7 = 0x0000003E            # LONG name for July
            LOCALE_SMONTHNAME8 = 0x0000003F            # LONG name for August
            LOCALE_SMONTHNAME9 = 0x00000040            # LONG name for September
            LOCALE_SMONTHNAME10 = 0x00000041            # LONG name for October
            LOCALE_SMONTHNAME11 = 0x00000042            # LONG name for November
            LOCALE_SMONTHNAME12 = 0x00000043            # LONG name for December
            LOCALE_SMONTHNAME13 = 0x0000100E            # LONG name for 13th month (if exists)
            LOCALE_SABBREVMONTHNAME1 = 0x00000044            # abbreviated name for January
            LOCALE_SABBREVMONTHNAME2 = 0x00000045            # abbreviated name for February
            LOCALE_SABBREVMONTHNAME3 = 0x00000046            # abbreviated name for March
            LOCALE_SABBREVMONTHNAME4 = 0x00000047            # abbreviated name for April
            LOCALE_SABBREVMONTHNAME5 = 0x00000048            # abbreviated name for May
            LOCALE_SABBREVMONTHNAME6 = 0x00000049            # abbreviated name for June
            LOCALE_SABBREVMONTHNAME7 = 0x0000004A            # abbreviated name for July
            LOCALE_SABBREVMONTHNAME8 = 0x0000004B            # abbreviated name for August
            LOCALE_SABBREVMONTHNAME9 = 0x0000004C            # abbreviated name for September
            LOCALE_SABBREVMONTHNAME10 = 0x0000004D            # abbreviated name for October
            LOCALE_SABBREVMONTHNAME11 = 0x0000004E            # abbreviated name for November
            LOCALE_SABBREVMONTHNAME12 = 0x0000004F            # abbreviated name for December
            LOCALE_SABBREVMONTHNAME13 = 0x0000100F            # abbreviated name for 13th month (if exists)
            LOCALE_SPOSITIVESIGN = 0x00000050            # positive sign, eg ""
            LOCALE_SNEGATIVESIGN = 0x00000051            # negative sign, eg "-"
            LOCALE_IPOSSIGNPOSN = 0x00000052            # positive sign position (derived from INEGCURR)
            LOCALE_INEGSIGNPOSN = 0x00000053            # negative sign position (derived from INEGCURR)
            LOCALE_IPOSSYMPRECEDES = 0x00000054            # mon sym precedes pos amt (derived from ICURRENCY)
            LOCALE_IPOSSEPBYSPACE = 0x00000055            # mon sym sep by space from pos amt (derived from ICURRENCY)
            LOCALE_INEGSYMPRECEDES = 0x00000056            # mon sym precedes neg amt (derived from INEGCURR)
            LOCALE_INEGSEPBYSPACE = 0x00000057            # mon sym sep by space from neg amt (derived from INEGCURR)
            if WINVER >= 0x0400:
                LOCALE_FONTSIGNATURE = 0x00000058                # font signature
                LOCALE_SISO639LANGNAME = 0x00000059                # ISO abbreviated language name, eg "en"
                LOCALE_SISO3166CTRYNAME = 0x0000005A                # ISO abbreviated country/region name, eg "US"
            # END IF  WINVER >= 0x0400

            if WINVER >= 0x0500:
                LOCALE_IPAPERSIZE = 0x0000100A                # 1 = letter, 5 = legal, 8 = a3, 9 = a4
                LOCALE_SENGCURRNAME = 0x00001007                # english name of currency, eg "Euro"
                LOCALE_SNATIVECURRNAME = 0x00001008                # native name of currency, eg "euro"
                LOCALE_SYEARMONTH = 0x00001006                # year month format string, eg "MM/yyyy"
                LOCALE_SSORTNAME = 0x00001013                # sort name, usually "", eg "Dictionary" in UI Language
                LOCALE_IDIGITSUBSTITUTION = 0x00001014                # 0 = context, 1 = none, 2 = national
            # END IF  WINVER >= 0x0500

            if WINVER >= 0x0600:
                LOCALE_SNAME = 0x0000005C                # locale name (ie: en-us)
                LOCALE_SDURATION = 0x0000005D                # time duration format, eg "hh:mm:ss"
                LOCALE_SSHORTESTDAYNAME1 = 0x00000060                # Shortest day name for Monday
                LOCALE_SSHORTESTDAYNAME2 = 0x00000061                # Shortest day name for Tuesday
                LOCALE_SSHORTESTDAYNAME3 = 0x00000062                # Shortest day name for Wednesday
                LOCALE_SSHORTESTDAYNAME4 = 0x00000063                # Shortest day name for Thursday
                LOCALE_SSHORTESTDAYNAME5 = 0x00000064                # Shortest day name for Friday
                LOCALE_SSHORTESTDAYNAME6 = 0x00000065                # Shortest day name for Saturday
                LOCALE_SSHORTESTDAYNAME7 = 0x00000066                # Shortest day name for Sunday
                LOCALE_SISO639LANGNAME2 = 0x00000067                # 3 character ISO abbreviated language name, eg "eng"
                LOCALE_SISO3166CTRYNAME2 = 0x00000068                # 3 character ISO country/region name, eg "USA"
                LOCALE_SNAN = 0x00000069                # Not a Number, eg "NaN"
                LOCALE_SPOSINFINITY = 0x0000006A                # + Infinity, eg "infinity"
                LOCALE_SNEGINFINITY = 0x0000006B                # - Infinity, eg "-infinity"

                # Typical scripts in the locale: ; delimited script codes, eg
                # "Latn;"
                LOCALE_SSCRIPTS = 0x0000006C
                LOCALE_SPARENT = 0x0000006D                # Fallback name for resources, eg "en" for "en-US"

                # Fallback name for within the console for Unicode Only
                # locales, eg "en" for bn-IN
                LOCALE_SCONSOLEFALLBACKNAME = 0x0000006E
            # END IF  (WINVER >= 0x0600)

            if WINVER >= _WIN32_WINNT_WIN7:
                LOCALE_IREADINGLAYOUT = 0x00000070                # Returns one of the following 4 reading layout values:

                # 0 - Left to right (eg en-US)
                # 1 - Right to left (eg arabic locales)
                # 2 - Vertical top to bottom with columns to the left and also
                # left to right (ja-JP locales)
                # 3 - Vertical top to bottom with columns proceeding to the
                # right
                LOCALE_INEUTRAL = 0x00000071                # Returns 0 for specific cultures, 1 for neutral cultures.
                LOCALE_INEGATIVEPERCENT = 0x00000074                # Returns 0-11 for the negative percent format
                LOCALE_IPOSITIVEPERCENT = 0x00000075                # Returns 0-3 for the positive percent formatIPOSITIVEPERCENT
                LOCALE_SPERCENT = 0x00000076                # Returns the percent symbol
                LOCALE_SPERMILLE = 0x00000077                # Returns the permille (U + 2030) symbol
                LOCALE_SMONTHDAY = 0x00000078                # Returns the preferred month/day format

                # Returns the preferred SHORT time format
                # (ie: no seconds, just h:mm)
                LOCALE_SSHORTTIME = 0x00000079
                LOCALE_SOPENTYPELANGUAGETAG = 0x0000007A                # Open type language tag, eg: "latn" or "dflt"
                LOCALE_SSORTLOCALE = 0x0000007B                # Name of locale to use for sorting/collation/casing behavior.
            # END IF  (WINVER >= _WIN32_WINNT_WIN7)

            if WINVER >= _WIN32_WINNT_WIN8:
                # Long date without year, day of week, month, date, eg: for
                # lock screen
                LOCALE_SRELATIVELONGDATE = 0x0000007C
            # END IF


            if WINVER >= _WIN32_WINNT_WIN10:
                LOCALE_SSHORTESTAM = 0x0000007E                # Shortest AM designator, eg "A"
                LOCALE_SSHORTESTPM = 0x0000007F                # Shortest PM designator, eg "P"
            # END IF


            # DEPRECATED LCTYPEs
            # DEPRECATED LCTYPEs for Code Pages
            # Applications are strongly encouraged to Use Unicode, such as
            # UTF-16 (WCHAR type)
            # or the CP_UTF8 Code Page. Legacy encodings are unable to
            # represent the full
            # set of scripts/language and characters (& emojinot ) available
            # on modern computers.
            # Use of legacy code pages (encodings) is a leading cause of data
            # loss and corruption.
            # default oem code page for locale
            # (user may configure as UTF-8, use of Unicode is recommended instead)
            #
            LOCALE_IDEFAULTCODEPAGE = 0x0000000B

            # default ansi code page for locale
            # (user may configure as UTF-8, use of Unicode is recommended instead)
            #
            LOCALE_IDEFAULTANSICODEPAGE = 0x00001004

            # default mac code page for locale
            # (user may configure as UTF-8, use of Unicode is recommended instead)
            #
            LOCALE_IDEFAULTMACCODEPAGE = 0x00001011
            if WINVER >= 0x0500:
                # default ebcdic code page for a locale
                # (use of Unicode is recommended instead)
                LOCALE_IDEFAULTEBCDICCODEPAGE = 0x00001012
            # END IF  WINVER >= 0x0500

            # LCTYPEs using out-of-date concepts
            LOCALE_ILANGUAGE = 0x00000001            # DEPRECATED language id (LCID), LOCALE_SNAME preferred

            # DEPRECATED arbitrary abbreviated language name,
            # LOCALE_SISO639LANGNAME instead.
            LOCALE_SABBREVLANGNAME = 0x00000003

            # DEPRECATED arbitrary abbreviated country/region name,
            # LOCALE_SISO3166CTRYNAME instead.
            LOCALE_SABBREVCTRYNAME = 0x00000007

            # DEPRECATED geographical location id, use LOCALE_SISO3166CTRYNAME
            # instead.
            LOCALE_IGEOID = 0x0000005B
            LOCALE_IDEFAULTLANGUAGE = 0x00000009            # DEPRECATED default language id, deprecated
            LOCALE_IDEFAULTCOUNTRY = 0x0000000A            # DEPRECATED default country/region code, deprecated

            # DEPRECATED, use LOCALE_ICURRDIGITS intl monetary digits, eg 2
            # for $1.00
            LOCALE_IINTLCURRDIGITS = 0x0000001A

            # Derived legacy date & time values for compatibility only.
            # Please use the appropriate date or time pattern instead.
            # These can be misleading, for example a locale configured as
            # 12h24m52s could have a time separator of "h".
            # DEPRECATED date separator
            # (derived from LOCALE_SSHORTDATE, use that instead)
            LOCALE_SDATE = 0x0000001D

            # DEPRECATED time separator
            # (derived from LOCALE_STIMEFORMAT, use that instead)
            LOCALE_STIME = 0x0000001E

            # DEPRECATED SHORT date format ordering
            # (derived from LOCALE_SSHORTDATE, use that instead)
            LOCALE_IDATE = 0x00000021

            # DEPRECATED LONG date format ordering
            # (derived from LOCALE_SLONGDATE, use that instead)
            LOCALE_ILDATE = 0x00000022

            # DEPRECATED time format specifier
            # (derived from LOCALE_STIMEFORMAT, use that instead)
            LOCALE_ITIME = 0x00000023

            # DEPRECATED time marker position
            # (derived from LOCALE_STIMEFORMAT, use that instead)
            LOCALE_ITIMEMARKPOSN = 0x00001005

            # DEPRECATED century format specifier
            # (short date, LOCALE_SSHORTDATE is preferred)
            LOCALE_ICENTURY = 0x00000024

            # DEPRECATED leading zeros in time field
            # (derived from LOCALE_STIMEFORMAT, use that instead)
            LOCALE_ITLZERO = 0x00000025

            # DEPRECATED leading zeros in day field
            # (short date, LOCALE_SSHORTDATE is preferred)
            LOCALE_IDAYLZERO = 0x00000026

            # DEPRECATED leading zeros in month field
            # (short date, LOCALE_SSHORTDATE is preferred)
            LOCALE_IMONLZERO = 0x00000027
            if WINVER >= 0x0600:
                LOCALE_SKEYBOARDSTOINSTALL = 0x0000005E                # Used internally, see GetKeyboardLayoutName() function
            # END IF  WINVER >= 0x0600

            # LCTYPEs which have been renamed to enable more understandable
            # source code.
            LOCALE_SLANGUAGE = LOCALE_SLOCALIZEDDISPLAYNAME            # DEPRECATED as new name is more readable.
            if WINVER >= _WIN32_WINNT_VISTA:
                LOCALE_SLANGDISPLAYNAME = LOCALE_SLOCALIZEDLANGUAGENAME                # DEPRECATED as new name is more readable.
            # END IF  (WINVER >= _WIN32_WINNT_VISTA)

            LOCALE_SENGLANGUAGE = LOCALE_SENGLISHLANGUAGENAME            # DEPRECATED as new name is more readable.
            LOCALE_SNATIVELANGNAME = LOCALE_SNATIVELANGUAGENAME            # DEPRECATED as new name is more readable.
            LOCALE_SCOUNTRY = LOCALE_SLOCALIZEDCOUNTRYNAME            # DEPRECATED as new name is more readable.
            LOCALE_SENGCOUNTRY = LOCALE_SENGLISHCOUNTRYNAME            # DEPRECATED as new name is more readable.
            LOCALE_SNATIVECTRYNAME = LOCALE_SNATIVECOUNTRYNAME            # DEPRECATED as new name is more readable.

            # DEPRECATED: Use LOCALE_SISO3166CTRYNAME to query for a region
            # identifier, LOCALE_ICOUNTRY is not a region identifier.
            LOCALE_ICOUNTRY = LOCALE_IDIALINGCODE            # Deprecated synonym for LOCALE_IDIALINGCODE
            LOCALE_S1159 = LOCALE_SAM            # DEPRECATED: Please use LOCALE_SAM, which is more readable.
            LOCALE_S2359 = LOCALE_SPM            # DEPRECATED: Please use LOCALE_SPM, which is more readable.

            # Time Flags for GetTimeFormat.
            TIME_NOMINUTESORSECONDS = 0x00000001            # do not use minutes or seconds
            TIME_NOSECONDS = 0x00000002            # do not use seconds
            TIME_NOTIMEMARKER = 0x00000004            # do not use time marker
            TIME_FORCE24HOURFORMAT = 0x00000008            # always use 24 hour format

            # Date Flags for GetDateFormat.
            DATE_SHORTDATE = 0x00000001            # use SHORT date picture
            DATE_LONGDATE = 0x00000002            # use LONG date picture
            DATE_USE_ALT_CALENDAR = 0x00000004            # use alternate calendar (if any)
            if WINVER >= 0x0500:
                DATE_YEARMONTH = 0x00000008                # use year month picture
                DATE_LTRREADING = 0x00000010                # add marks for left to right reading order layout
                DATE_RTLREADING = 0x00000020                # add marks for right to left reading order layout
            # END IF  WINVER >= 0x0500

            if WINVER >= _WIN32_WINNT_WIN7:
                # add appropriate marks for left-to-right or right-to-left
                # reading order layout
                DATE_AUTOLAYOUT = 0x00000040
            # END IF  (WINVER >= _WIN32_WINNT_WIN7)

            if WINVER >= _WIN32_WINNT_WINTHRESHOLD:
                DATE_MONTHDAY = 0x00000080                # include month day pictures
            # END IF  (WINVER >= _WIN32_WINNT_WINTHRESHOLD)

            # Calendar Types.
            # These types are used for the EnumCalendarInfo and GetCalendarInfo
            # NLS API routines.
            # Some of these types are also used for the SetCalendarInfo NLS API
            # routine.
            # The following CalTypes may be used in combination with any other
            # CalTypes.
            # CAL_NOUSEROVERRIDE
            # CAL_RETURN_NUMBER will return the result from GetCalendarInfo as
            # a
            # number instead of a string. This flag is only valid for the
            # CalTypes
            # beginning with CAL_I.
            # DEPRECATED: CAL_USE_CP_ACP is used in many of the A (Ansi) apis
            # that need
            # to do string translation. Callers are encouraged to use the W
            # (WCHAR/Unicode) apis instead.
            if WINVER >= 0x0500:
                CAL_NOUSEROVERRIDE = LOCALE_NOUSEROVERRIDE                # Not Recommended - do not use user overrides
                CAL_USE_CP_ACP = LOCALE_USE_CP_ACP                # DEPRECATED, call Unicode APIs instead: use the system ACP
                CAL_RETURN_NUMBER = LOCALE_RETURN_NUMBER                # return number instead of string
            # END IF  WINVER >= 0x0500

            if WINVER >= _WIN32_WINNT_WIN7:
                CAL_RETURN_GENITIVE_NAMES = LOCALE_RETURN_GENITIVE_NAMES                # return genitive forms of month names
            # END IF   winver >= windows 7

            # The following CalTypes are mutually exclusive in that they may
            # NOT
            # be used in combination with each other.
            CAL_ICALINTVALUE = 0x00000001            # calendar type
            CAL_SCALNAME = 0x00000002            # native name of calendar
            CAL_IYEAROFFSETRANGE = 0x00000003            # starting years of eras
            CAL_SERASTRING = 0x00000004            # era name for IYearOffsetRanges, eg A.D.
            CAL_SSHORTDATE = 0x00000005            # SHORT date format string
            CAL_SLONGDATE = 0x00000006            # LONG date format string
            CAL_SDAYNAME1 = 0x00000007            # native name for Monday
            CAL_SDAYNAME2 = 0x00000008            # native name for Tuesday
            CAL_SDAYNAME3 = 0x00000009            # native name for Wednesday
            CAL_SDAYNAME4 = 0x0000000A            # native name for Thursday
            CAL_SDAYNAME5 = 0x0000000B            # native name for Friday
            CAL_SDAYNAME6 = 0x0000000C            # native name for Saturday
            CAL_SDAYNAME7 = 0x0000000D            # native name for Sunday
            CAL_SABBREVDAYNAME1 = 0x0000000E            # abbreviated name for Mon
            CAL_SABBREVDAYNAME2 = 0x0000000F            # abbreviated name for Tue
            CAL_SABBREVDAYNAME3 = 0x00000010            # abbreviated name for Wed
            CAL_SABBREVDAYNAME4 = 0x00000011            # abbreviated name for Thu
            CAL_SABBREVDAYNAME5 = 0x00000012            # abbreviated name for Fri
            CAL_SABBREVDAYNAME6 = 0x00000013            # abbreviated name for Sat
            CAL_SABBREVDAYNAME7 = 0x00000014            # abbreviated name for Sun

            # Note that in the hebrew calendar the leap month name is always
            # returned as the 7th month
            CAL_SMONTHNAME1 = 0x00000015            # native name for January
            CAL_SMONTHNAME2 = 0x00000016            # native name for February
            CAL_SMONTHNAME3 = 0x00000017            # native name for March
            CAL_SMONTHNAME4 = 0x00000018            # native name for April
            CAL_SMONTHNAME5 = 0x00000019            # native name for May
            CAL_SMONTHNAME6 = 0x0000001A            # native name for June
            CAL_SMONTHNAME7 = 0x0000001B            # native name for July
            CAL_SMONTHNAME8 = 0x0000001C            # native name for August
            CAL_SMONTHNAME9 = 0x0000001D            # native name for September
            CAL_SMONTHNAME10 = 0x0000001E            # native name for October
            CAL_SMONTHNAME11 = 0x0000001F            # native name for November
            CAL_SMONTHNAME12 = 0x00000020            # native name for December
            CAL_SMONTHNAME13 = 0x00000021            # native name for 13th month (if any)
            CAL_SABBREVMONTHNAME1 = 0x00000022            # abbreviated name for Jan
            CAL_SABBREVMONTHNAME2 = 0x00000023            # abbreviated name for Feb
            CAL_SABBREVMONTHNAME3 = 0x00000024            # abbreviated name for Mar
            CAL_SABBREVMONTHNAME4 = 0x00000025            # abbreviated name for Apr
            CAL_SABBREVMONTHNAME5 = 0x00000026            # abbreviated name for May
            CAL_SABBREVMONTHNAME6 = 0x00000027            # abbreviated name for Jun
            CAL_SABBREVMONTHNAME7 = 0x00000028            # abbreviated name for July
            CAL_SABBREVMONTHNAME8 = 0x00000029            # abbreviated name for Aug
            CAL_SABBREVMONTHNAME9 = 0x0000002A            # abbreviated name for Sep
            CAL_SABBREVMONTHNAME10 = 0x0000002B            # abbreviated name for Oct
            CAL_SABBREVMONTHNAME11 = 0x0000002C            # abbreviated name for Nov
            CAL_SABBREVMONTHNAME12 = 0x0000002D            # abbreviated name for Dec
            CAL_SABBREVMONTHNAME13 = 0x0000002E            # abbreviated name for 13th month (if any)
            if WINVER >= 0x0500:
                CAL_SYEARMONTH = 0x0000002F                # year month format string
                CAL_ITWODIGITYEARMAX = 0x00000030                # two digit year max
            # END IF  WINVER >= 0x0500

            if WINVER >= 0x0600:
                CAL_SSHORTESTDAYNAME1 = 0x00000031                # Shortest day name for Mo
                CAL_SSHORTESTDAYNAME2 = 0x00000032                # Shortest day name for Tu
                CAL_SSHORTESTDAYNAME3 = 0x00000033                # Shortest day name for We
                CAL_SSHORTESTDAYNAME4 = 0x00000034                # Shortest day name for Th
                CAL_SSHORTESTDAYNAME5 = 0x00000035                # Shortest day name for Fr
                CAL_SSHORTESTDAYNAME6 = 0x00000036                # Shortest day name for Sa
                CAL_SSHORTESTDAYNAME7 = 0x00000037                # Shortest day name for Su
            # END IF  (WINVER >= 0x0600)

            if WINVER >= _WIN32_WINNT_WIN7:
                CAL_SMONTHDAY = 0x00000038                # Month/day format
                CAL_SABBREVERASTRING = 0x00000039                # Abbreviated era string (eg: AD)
            # END IF   winver >= windows 7

            if WINVER >= _WIN32_WINNT_WIN8:
                # Long date without year, day of week, month, date, eg: for
                # lock screen
                CAL_SRELATIVELONGDATE = 0x0000003A
            # END IF


            if NTDDI_VERSION >= NTDDI_WIN10_RS2:
                # Japanese calendar only: return the English era names for
                # .Net compatibility
                CAL_SENGLISHERANAME = 0x0000003B

                # Japanese calendar only: return the English Abbreviated era
                # names for .Net compatibility
                CAL_SENGLISHABBREVERANAME = 0x0000003C
            # END IF


            # Calendar Enumeration Value.
            ENUM_ALL_CALENDARS = 0xFFFFFFFF            # enumerate all calendars

            # Calendar ID Values.
            CAL_GREGORIAN = 1            # Gregorian (localized) calendar
            CAL_GREGORIAN_US = 2            # Gregorian (U.S.) calendar
            CAL_JAPAN = 3            # Japanese Emperor Era calendar
            CAL_TAIWAN = 4            # Taiwan calendar
            CAL_KOREA = 5            # Korean Tangun Era calendar
            CAL_HIJRI = 6            # Hijri (Arabic Lunar) calendar
            CAL_THAI = 7            # Thai calendar
            CAL_HEBREW = 8            # Hebrew (Lunar) calendar
            CAL_GREGORIAN_ME_FRENCH = 9            # Gregorian Middle East French calendar
            CAL_GREGORIAN_ARABIC = 10            # Gregorian Arabic calendar
            CAL_GREGORIAN_XLIT_ENGLISH = 11            # Gregorian Transliterated English calendar
            CAL_GREGORIAN_XLIT_FRENCH = 12            # Gregorian Transliterated French calendar
            CAL_PERSIAN = 22            # Persian (Solar Hijri) calendar
            CAL_UMALQURA = 23            # UmAlQura Hijri (Arabic Lunar) calendar

            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            # Language Group ID Values
            # The "Language Group" concept is an obsolete concept.
            # The groups returned are not well defined, arbitrary,
            # inconsistent, inaccurate,
            # no longer maintained, and no longer supported.
            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            LGRPID_WESTERN_EUROPE = 0x0001            # Western Europe & U.S.
            LGRPID_CENTRAL_EUROPE = 0x0002            # Central Europe
            LGRPID_BALTIC = 0x0003            # Baltic
            LGRPID_GREEK = 0x0004            # Greek
            LGRPID_CYRILLIC = 0x0005            # Cyrillic
            LGRPID_TURKIC = 0x0006            # Turkic
            LGRPID_TURKISH = 0x0006            # Turkish
            LGRPID_JAPANESE = 0x0007            # Japanese
            LGRPID_KOREAN = 0x0008            # Korean
            LGRPID_TRADITIONAL_CHINESE = 0x0009            # Traditional Chinese
            LGRPID_SIMPLIFIED_CHINESE = 0x000A            # Simplified Chinese
            LGRPID_THAI = 0x000B            # Thai
            LGRPID_HEBREW = 0x000C            # Hebrew
            LGRPID_ARABIC = 0x000D            # Arabic
            LGRPID_VIETNAMESE = 0x000E            # Vietnamese
            LGRPID_INDIC = 0x000F            # Indic
            LGRPID_GEORGIAN = 0x0010            # Georgian
            LGRPID_ARMENIAN = 0x0011            # Armenian

            if WINVER >= 0x0600:
                # MUI function flag values
                MUI_LANGUAGE_ID = 0x4                # Use traditional language ID convention
                MUI_LANGUAGE_NAME = 0x8                # Use ISO language (culture) name convention

                # GetThreadPreferredUILanguages merges in parent and base
                # languages
                MUI_MERGE_SYSTEM_FALLBACK = 0x10

                # GetThreadPreferredUILanguages merges in user preferred
                # languages
                MUI_MERGE_USER_FALLBACK = 0x20
                MUI_UI_FALLBACK = (
                    MUI_MERGE_SYSTEM_FALLBACK |
                    MUI_MERGE_USER_FALLBACK
                )

                # GetThreadPreferredUILanguages merges in user preferred
                # languages
                MUI_THREAD_LANGUAGES = 0x40

                # SetThreadPreferredUILanguages takes on console specific
                # behavior
                MUI_CONSOLE_FILTER = 0x100

                # SetThreadPreferredUILanguages takes on complex script
                # specific behavior
                MUI_COMPLEX_SCRIPT_FILTER = 0x200
                MUI_RESET_FILTERS = 0x001                # Reset MUI_CONSOLE_FILTER and MUI_COMPLEX_SCRIPT_FILTER

                # GetFileMUIPath returns the MUI files for the languages in
                # the fallback list
                MUI_USER_PREFERRED_UI_LANGUAGES = 0x10

                # GetFileMUIPath returns all the MUI files installed in the
                # machine
                MUI_USE_INSTALLED_LANGUAGES = 0x20

                # GetFileMUIPath returns all the MUI files irrespective of
                # whether language is installed
                MUI_USE_SEARCH_ALL_LANGUAGES = 0x40
                MUI_LANG_NEUTRAL_PE_FILE = 0x100                # GetFileMUIPath returns target file with .mui extension
                MUI_NON_LANG_NEUTRAL_FILE = 0x200                # GetFileMUIPath returns target file with same name as source
                MUI_MACHINE_LANGUAGE_SETTINGS = 0x400
                MUI_FILETYPE_NOT_LANGUAGE_NEUTRAL = 0x001                # GetFileMUIInfo found a non-split resource file
                MUI_FILETYPE_LANGUAGE_NEUTRAL_MAIN = 0x002                # GetFileMUIInfo found a LN main module resource file
                MUI_FILETYPE_LANGUAGE_NEUTRAL_MUI = 0x004                # GetFileMUIInfo found a LN MUI module resource file
                MUI_QUERY_TYPE = 0x001                # GetFileMUIInfo will look for the type of the resource file

                # GetFileMUIInfo will look for the checksum of the resource
                # file
                MUI_QUERY_CHECKSUM = 0x002
                MUI_QUERY_LANGUAGE_NAME = 0x004                # GetFileMUIInfo will look for the culture of the resource file

                # GetFileMUIInfo will look for the resource types of the
                # resource file
                MUI_QUERY_RESOURCE_TYPES = 0x008
                MUI_FILEINFO_VERSION = 0x001                # Version of FILEMUIINFO structure used with GetFileMUIInfo
                MUI_FULL_LANGUAGE = 0x01
                MUI_PARTIAL_LANGUAGE = 0x02
                MUI_LIP_LANGUAGE = 0x04
                MUI_LANGUAGE_INSTALLED = 0x20
                MUI_LANGUAGE_LICENSED = 0x40


                # MUI_CALLBACK_FLAG defines are duplicated in rtlmui.h
                MUI_CALLBACK_ALL_FLAGS = (
                    MUI_CALLBACK_FLAG_UPGRADED_INSTALLATION
                )                # OR all other flags when defined.


                # MUI_CALLBACK_ flags are duplicated in rtlmui.h            # END IF
            # //////////////////////////////////////////////////////////////////////////
            #
            # Typedefs
            # Define all types for the NLS component here.
            # //////////////////////////////////////////////////////////////////////////
            #
            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            # Language Group ID
            # The "Language Group" concept is an obsolete concept.
            # The groups returned are not well defined, arbitrary,
            # inconsistent, inaccurate,
            # no longer maintained, and no longer supported.
            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            LGRPID = DWORD


            # Locale type constant.
            LCTYPE = DWORD


            # Calendar type constant.
            CALTYPE = DWORD


            # Calendar ID.
            CALID = DWORD


            # CP Info.
            # Deprecated. Applications should use Unicode
            # (WCHAR / UTF-16 or UTF-8)
            # WARNING: These structures fail for some encodings, including
            # UTF-8, which
            # do not fit into the assumptions of these APIs.
            # max length (in bytes) of a char
            _cpinfo._fields_ = [
                ('MaxCharSize', UINT),
                # default character
                ('DefaultChar', BYTE * MAX_DEFAULTCHAR),
                # lead byte ranges
                ('LeadByte', BYTE * MAX_LEADBYTES),
            ]

            # max length (in bytes) of a char
            _cpinfoexA._fields_ = [
                ('MaxCharSize', UINT),
                # default character (MB)
                ('DefaultChar', BYTE * MAX_DEFAULTCHAR),
                # lead byte ranges
                ('LeadByte', BYTE * MAX_LEADBYTES),
                # default character (Unicode)
                ('UnicodeDefaultChar', WCHAR),
                # code page id
                ('CodePage', UINT),
                # code page name (Unicode)
                ('CodePageName', CHAR * MAX_PATH),
            ]

            # max length (in bytes) of a char
            _cpinfoexW._fields_ = [
                ('MaxCharSize', UINT),
                # default character (MB)
                ('DefaultChar', BYTE * MAX_DEFAULTCHAR),
                # lead byte ranges
                ('LeadByte', BYTE * MAX_LEADBYTES),
                # default character (Unicode)
                ('UnicodeDefaultChar', WCHAR),
                # code page id
                ('CodePage', UINT),
                # code page name (Unicode)
                ('CodePageName', WCHAR * MAX_PATH),
            ]
            if defined(UNICODE):
                CPINFOEX = CPINFOEXW
                LPCPINFOEX = LPCPINFOEXW
            else:
                CPINFOEX = CPINFOEXA
                LPCPINFOEX = LPCPINFOEXA
            # END IF   UNICODE


            # Number format.
            # number of decimal digits
            _numberfmtA._fields_ = [
                ('NumDigits', UINT),
                # if leading zero in decimal fields
                ('LeadingZero', UINT),
                # group size left of decimal
                ('Grouping', UINT),
                # ptr to decimal separator string
                ('lpDecimalSep', LPSTR),
                # ptr to thousand separator string
                ('lpThousandSep', LPSTR),
                # negative number ordering
                ('NegativeOrder', UINT),
            ]

            # number of decimal digits
            _numberfmtW._fields_ = [
                ('NumDigits', UINT),
                # if leading zero in decimal fields
                ('LeadingZero', UINT),
                # group size left of decimal
                ('Grouping', UINT),
                # ptr to decimal separator string
                ('lpDecimalSep', LPWSTR),
                # ptr to thousand separator string
                ('lpThousandSep', LPWSTR),
                # negative number ordering
                ('NegativeOrder', UINT),
            ]
            if defined(UNICODE):
                NUMBERFMT = NUMBERFMTW
                LPNUMBERFMT = LPNUMBERFMTW
            else:
                NUMBERFMT = NUMBERFMTA
                LPNUMBERFMT = LPNUMBERFMTA
            # END IF   UNICODE


            # Currency format.
            # number of decimal digits
            _currencyfmtA._fields_ = [
                ('NumDigits', UINT),
                # if leading zero in decimal fields
                ('LeadingZero', UINT),
                # group size left of decimal
                ('Grouping', UINT),
                # ptr to decimal separator string
                ('lpDecimalSep', LPSTR),
                # ptr to thousand separator string
                ('lpThousandSep', LPSTR),
                # negative currency ordering
                ('NegativeOrder', UINT),
                # positive currency ordering
                ('PositiveOrder', UINT),
                # ptr to currency symbol string
                ('lpCurrencySymbol', LPSTR),
            ]

            # number of decimal digits
            _currencyfmtW._fields_ = [
                ('NumDigits', UINT),
                # if leading zero in decimal fields
                ('LeadingZero', UINT),
                # group size left of decimal
                ('Grouping', UINT),
                # ptr to decimal separator string
                ('lpDecimalSep', LPWSTR),
                # ptr to thousand separator string
                ('lpThousandSep', LPWSTR),
                # negative currency ordering
                ('NegativeOrder', UINT),
                # positive currency ordering
                ('PositiveOrder', UINT),
                # ptr to currency symbol string
                ('lpCurrencySymbol', LPWSTR),
            ]
            if defined(UNICODE):
                CURRENCYFMT = CURRENCYFMTW
                LPCURRENCYFMT = LPCURRENCYFMTW
            else:
                CURRENCYFMT = CURRENCYFMTA
                LPCURRENCYFMT = LPCURRENCYFMTA
            # END IF   UNICODE


            # NLS function capabilities
            class SYSNLS_FUNCTION(ENUM):
                COMPARE_STRING = 0x0001

            COMPARE_STRING = SYSNLS_FUNCTION.COMPARE_STRING
            NLS_FUNCTION = DWORD


            # NLS version structure.
            if WINVER >= _WIN32_WINNT_WIN8:
                # New structures are the same
                # The combination of dwNLSVersion, and guidCustomVersion
                # identify specific sort behavior, persist those to ensure
                # identical
                # behavior in the future.
                # (ctypes.sizeof(NLSVERSIONINFO) == 32 bytes
                _nlsversioninfo._fields_ = [
                    ('dwNLSVersionInfoSize', DWORD),
                    ('dwNLSVersion', DWORD),
                    # Deprecated, use dwNLSVersion instead
                    ('dwDefinedVersion', DWORD),
                    # Deprecated, use guidCustomVerison instead
                    ('dwEffectiveId', DWORD),
                    # Explicit sort version
                    ('guidCustomVersion', GUID),
                ]
            else:
                # Windows 7 and below had different sizes
                # This is to be deprecated, please use the NLSVERSIONINFOEX
                # structure below in the future. The difference is that
                # guidCustomversion is required to uniquely identify a sort
                # 12 bytes
                _nlsversioninfo._fields_ = [
                    ('dwNLSVersionInfoSize', DWORD),
                    ('dwNLSVersion', DWORD),
                    # Deprecated, use dwNLSVersion instead
                    ('dwDefinedVersion', DWORD),
                ]
            # END IF


            # The combination of dwNLSVersion, and guidCustomVersion
            # identify specific sort behavior, persist those to ensure
            # identical
            # behavior in the future.
            # (ctypes.sizeof(NLSVERSIONINFOEX) == 32 bytes
            _nlsversioninfoex._fields_ = [
                ('dwNLSVersionInfoSize', DWORD),
                ('dwNLSVersion', DWORD),
                # Deprecated, use dwNLSVersion instead
                ('dwDefinedVersion', DWORD),
                # Deprecated, use guidCustomVerison instead
                ('dwEffectiveId', DWORD),
                # Explicit sort version
                ('guidCustomVersion', GUID),
            ]
            # GEO defines            # TYPEDEF ERROR: DWORD   GEOTYPE;            # TYPEDEF ERROR: DWORD   GEOCLASS;
            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            # DEPRECATED: The GEOID concept is deprecated, please use
            # Country/Region Names instead, eg: "US" instead of a GEOID like
            # 244.
            # See the documentation for GetGeoInfoEx.
            # WARNING: These values are arbitrarily assigned values, please use
            # standard country/region names instead, such as "US".
            # ** DEPRECATED ** DEPRECATED ** DEPRECATED ** DEPRECATED **
            # DEPRECATED **
            # TYPEDEF ERROR: LONG    GEOID;
            GEOID_NOT_AVAILABLE = -1
            if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                GEO_NAME_USER_DEFAULT = NULL
            # END IF


            # GEO information types for clients to query
            # Please use GetGeoInfoEx and query by country/region name instead
            # of GEOID (eg: "US" instead of 244)
            class SYSGEOTYPE(ENUM):
                GEO_NATION = 0x0001
                GEO_LATITUDE = 0x0002
                GEO_LONGITUDE = 0x0003
                GEO_ISO2 = 0x0004
                GEO_ISO3 = 0x0005
                GEO_RFC1766 = 0x0006
                GEO_LCID = 0x0007
                GEO_FRIENDLYNAME = 0x0008
                GEO_OFFICIALNAME = 0x0009
                GEO_TIMEZONES = 0x000A
                GEO_OFFICIALLANGUAGES = 0x000B
                GEO_ISO_UN_NUMBER = 0x000C
                GEO_PARENT = 0x000D
                GEO_DIALINGCODE = 0x000E
                GEO_CURRENCYCODE = 0x000F
                GEO_CURRENCYSYMBOL = 0x0010
                if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                    GEO_NAME = 0x0011
                    GEO_ID = 0x0012
                # END IF

            GEO_NATION = SYSGEOTYPE.GEO_NATION
            GEO_LATITUDE = SYSGEOTYPE.GEO_LATITUDE
            GEO_LONGITUDE = SYSGEOTYPE.GEO_LONGITUDE
            GEO_ISO2 = SYSGEOTYPE.GEO_ISO2
            GEO_ISO3 = SYSGEOTYPE.GEO_ISO3
            GEO_RFC1766 = SYSGEOTYPE.GEO_RFC1766
            GEO_LCID = SYSGEOTYPE.GEO_LCID
            GEO_FRIENDLYNAME = SYSGEOTYPE.GEO_FRIENDLYNAME
            GEO_OFFICIALNAME = SYSGEOTYPE.GEO_OFFICIALNAME
            GEO_TIMEZONES = SYSGEOTYPE.GEO_TIMEZONES
            GEO_OFFICIALLANGUAGES = SYSGEOTYPE.GEO_OFFICIALLANGUAGES
            GEO_ISO_UN_NUMBER = SYSGEOTYPE.GEO_ISO_UN_NUMBER
            GEO_PARENT = SYSGEOTYPE.GEO_PARENT
            GEO_DIALINGCODE = SYSGEOTYPE.GEO_DIALINGCODE
            GEO_CURRENCYCODE = SYSGEOTYPE.GEO_CURRENCYCODE
            GEO_CURRENCYSYMBOL = SYSGEOTYPE.GEO_CURRENCYSYMBOL
            if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                GEO_NAME = SYSGEOTYPE.GEO_NAME
                GEO_ID = SYSGEOTYPE.GEO_ID
            # END IF

            # More GEOCLASS defines will be listed here
            class SYSGEOCLASS(ENUM):
                GEOCLASS_NATION = 16
                GEOCLASS_REGION = 14
                GEOCLASS_ALL = 0

            GEOCLASS_NATION = SYSGEOCLASS.GEOCLASS_NATION
            GEOCLASS_REGION = SYSGEOCLASS.GEOCLASS_REGION
            GEOCLASS_ALL = SYSGEOCLASS.GEOCLASS_ALL
            if WINVER >= 0x0600:
                # Normalization forms
                class _NORM_FORM(ENUM):
                    NormalizationOther = 0

                    # Each base plus combining characters to the canonical
                    # precomposed equivalent.
                    NormalizationC = 0x1

                    # Each precomposed character to its canonical decomposed
                    # equivalent.
                    NormalizationD = 0x2

                    # Each base plus combining characters to the canonical
                    # precomposed
                    NormalizationKC = 0x5

                    # Each precomposed character to its canonical decomposed
                    # equivalent
                    NormalizationKD = 0x6

                NORM_FORM = _NORM_FORM

                # IDN (International Domain Name) Flags
                IDN_ALLOW_UNASSIGNED = 0x01                # Allow unassigned "query" behavior per RFC 3454
                IDN_USE_STD3_ASCII_RULES = 0x02                # Enforce STD3 ASCII restrictions for legal characters

                # Enable EAI algorithmic fallback for email local parts
                # behavior
                IDN_EMAIL_ADDRESS = 0x04
                IDN_RAW_PUNYCODE = 0x08                # Disable validation and mapping of punycode.

                # Allow Latin in test script even if not present in locale
                # script
                VS_ALLOW_LATIN = 0x0001

                # Output script ids for inherited and common character types
                # if present
                GSS_ALLOW_INHERITED_COMMON = 0x0001
            # END IF  (WINVER >= 0x0600)

            # Enumeration function constants.
            if defined(STRICT):
                # BOOL (CALLBACK* LANGUAGEGROUP_ENUMPROCA)(LGRPID, LPSTR, LPSTR, DWORD, LONG_PTR);
                LANGUAGEGROUP_ENUMPROCA = CALLBACK(
                    BOOL,
                    LGRPID,
                    LPSTR,
                    LPSTR,
                    DWORD,
                    LONG_PTR,
                )


                # BOOL (CALLBACK* LANGGROUPLOCALE_ENUMPROCA)(LGRPID, LCID, LPSTR, LONG_PTR);
                LANGGROUPLOCALE_ENUMPROCA = CALLBACK(
                    BOOL,
                    LGRPID,
                    LCID,
                    LPSTR,
                    LONG_PTR,
                )


                # BOOL (CALLBACK* UILANGUAGE_ENUMPROCA)(LPSTR, LONG_PTR);
                UILANGUAGE_ENUMPROCA = CALLBACK(
                    BOOL,
                    LPSTR,
                    LONG_PTR,
                )


                # BOOL (CALLBACK* CODEPAGE_ENUMPROCA)(LPSTR);
                CODEPAGE_ENUMPROCA = CALLBACK(
                    BOOL,
                    LPSTR,
                )


                # BOOL (CALLBACK* DATEFMT_ENUMPROCA)(LPSTR);
                DATEFMT_ENUMPROCA = CALLBACK(
                    BOOL,
                    LPSTR,
                )


                # BOOL (CALLBACK* DATEFMT_ENUMPROCEXA)(LPSTR, CALID);
                DATEFMT_ENUMPROCEXA = CALLBACK(
                    BOOL,
                    LPSTR,
                    CALID,
                )


                # BOOL (CALLBACK* TIMEFMT_ENUMPROCA)(LPSTR);
                TIMEFMT_ENUMPROCA = CALLBACK(
                    BOOL,
                    LPSTR,
                )


                # BOOL (CALLBACK* CALINFO_ENUMPROCA)(LPSTR);
                CALINFO_ENUMPROCA = CALLBACK(
                    BOOL,
                    LPSTR,
                )


                # BOOL (CALLBACK* CALINFO_ENUMPROCEXA)(LPSTR, CALID);
                CALINFO_ENUMPROCEXA = CALLBACK(
                    BOOL,
                    LPSTR,
                    CALID,
                )


                # BOOL (CALLBACK* LOCALE_ENUMPROCA)(LPSTR);
                LOCALE_ENUMPROCA = CALLBACK(
                    BOOL,
                    LPSTR,
                )


                # BOOL (CALLBACK* LOCALE_ENUMPROCW)(LPWSTR);
                LOCALE_ENUMPROCW = CALLBACK(
                    BOOL,
                    LPWSTR,
                )


                # BOOL (CALLBACK* LANGUAGEGROUP_ENUMPROCW)(LGRPID, LPWSTR, LPWSTR, DWORD, LONG_PTR);
                LANGUAGEGROUP_ENUMPROCW = CALLBACK(
                    BOOL,
                    LGRPID,
                    LPWSTR,
                    LPWSTR,
                    DWORD,
                    LONG_PTR,
                )


                # BOOL (CALLBACK* LANGGROUPLOCALE_ENUMPROCW)(LGRPID, LCID, LPWSTR, LONG_PTR);
                LANGGROUPLOCALE_ENUMPROCW = CALLBACK(
                    BOOL,
                    LGRPID,
                    LCID,
                    LPWSTR,
                    LONG_PTR,
                )


                # BOOL (CALLBACK* UILANGUAGE_ENUMPROCW)(LPWSTR, LONG_PTR);
                UILANGUAGE_ENUMPROCW = CALLBACK(
                    BOOL,
                    LPWSTR,
                    LONG_PTR,
                )


                # BOOL (CALLBACK* CODEPAGE_ENUMPROCW)(LPWSTR);
                CODEPAGE_ENUMPROCW = CALLBACK(
                    BOOL,
                    LPWSTR,
                )


                # BOOL (CALLBACK* DATEFMT_ENUMPROCW)(LPWSTR);
                DATEFMT_ENUMPROCW = CALLBACK(
                    BOOL,
                    LPWSTR,
                )


                # BOOL (CALLBACK* DATEFMT_ENUMPROCEXW)(LPWSTR, CALID);
                DATEFMT_ENUMPROCEXW = CALLBACK(
                    BOOL,
                    LPWSTR,
                    CALID,
                )


                # BOOL (CALLBACK* TIMEFMT_ENUMPROCW)(LPWSTR);
                TIMEFMT_ENUMPROCW = CALLBACK(
                    BOOL,
                    LPWSTR,
                )


                # BOOL (CALLBACK* CALINFO_ENUMPROCW)(LPWSTR);
                CALINFO_ENUMPROCW = CALLBACK(
                    BOOL,
                    LPWSTR,
                )


                # BOOL (CALLBACK* CALINFO_ENUMPROCEXW)(LPWSTR, CALID);
                CALINFO_ENUMPROCEXW = CALLBACK(
                    BOOL,
                    LPWSTR,
                    CALID,
                )


                # BOOL (CALLBACK* GEO_ENUMPROC)(GEOID);
                GEO_ENUMPROC = CALLBACK(
                    BOOL,
                    GEOID,
                )


                if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                    # BOOL (CALLBACK* GEO_ENUMNAMEPROC)(PWSTR, LPARAM);
                    GEO_ENUMNAMEPROC = CALLBACK(
                        BOOL,
                        PWSTR,
                        LPARAM,
                    )


                # END IF


            else:
                LANGUAGEGROUP_ENUMPROCA = FARPROC
                LANGGROUPLOCALE_ENUMPROCA = FARPROC
                UILANGUAGE_ENUMPROCA = FARPROC
                CODEPAGE_ENUMPROCA = FARPROC
                DATEFMT_ENUMPROCA = FARPROC
                DATEFMT_ENUMPROCEXA = FARPROC
                TIMEFMT_ENUMPROCA = FARPROC
                CALINFO_ENUMPROCA = FARPROC
                CALINFO_ENUMPROCEXA = FARPROC
                GEO_ENUMPROC = FARPROC
                LOCALE_ENUMPROCA = FARPROC
                LOCALE_ENUMPROCW = FARPROC
                LANGUAGEGROUP_ENUMPROCW = FARPROC
                LANGGROUPLOCALE_ENUMPROCW = FARPROC
                UILANGUAGE_ENUMPROCW = FARPROC
                CODEPAGE_ENUMPROCW = FARPROC
                DATEFMT_ENUMPROCW = FARPROC
                DATEFMT_ENUMPROCEXW = FARPROC
                TIMEFMT_ENUMPROCW = FARPROC
                CALINFO_ENUMPROCW = FARPROC
                CALINFO_ENUMPROCEXW = FARPROC
                if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                    GEO_ENUMNAMEPROC = FARPROC
                # END IF

            # END IF   not STRICT

            if defined(UNICODE):
                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                #
                LANGUAGEGROUP_ENUMPROC = LANGUAGEGROUP_ENUMPROCW

                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                #
                LANGGROUPLOCALE_ENUMPROC = LANGGROUPLOCALE_ENUMPROCW
                UILANGUAGE_ENUMPROC = UILANGUAGE_ENUMPROCW
                CODEPAGE_ENUMPROC = CODEPAGE_ENUMPROCW
                DATEFMT_ENUMPROC = DATEFMT_ENUMPROCW
                DATEFMT_ENUMPROCEX = DATEFMT_ENUMPROCEXW
                TIMEFMT_ENUMPROC = TIMEFMT_ENUMPROCW
                CALINFO_ENUMPROC = CALINFO_ENUMPROCW
                CALINFO_ENUMPROCEX = CALINFO_ENUMPROCEXW
                LOCALE_ENUMPROC = LOCALE_ENUMPROCW
            else:
                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                #
                LANGUAGEGROUP_ENUMPROC = LANGUAGEGROUP_ENUMPROCA

                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                #
                LANGGROUPLOCALE_ENUMPROC = LANGGROUPLOCALE_ENUMPROCA
                UILANGUAGE_ENUMPROC = UILANGUAGE_ENUMPROCA
                CODEPAGE_ENUMPROC = CODEPAGE_ENUMPROCA
                DATEFMT_ENUMPROC = DATEFMT_ENUMPROCA
                DATEFMT_ENUMPROCEX = DATEFMT_ENUMPROCEXA
                TIMEFMT_ENUMPROC = TIMEFMT_ENUMPROCA
                CALINFO_ENUMPROC = CALINFO_ENUMPROCA
                CALINFO_ENUMPROCEX = CALINFO_ENUMPROCEXA
                LOCALE_ENUMPROC = LOCALE_ENUMPROCA
            # END IF   not UNICODE

            # Information about a MUI file, used as input/output in
            # GetFileMUIInfo
            # All offsets are relative to start of the structure. Offsets with
            # value 0 mean empty field.
            # Size of the structure including buffer size [in]
            _FILEMUIINFO._fields_ = [
                ('dwSize', DWORD),
                # Version of the structure [in]
                ('dwVersion', DWORD),
                # Type of the file [out]
                ('dwFileType', DWORD),
                # Checksum of the file [out]
                ('pChecksum', BYTE * 16),
                # Checksum of the file [out]
                ('pServiceChecksum', BYTE * 16),
                # Language name of the file [out]
                ('dwLanguageNameOffset', DWORD),
                # Number of TypeIDs in main module [out]
                ('dwTypeIDMainSize', DWORD),
                # Array of TypeIDs (DWORD) in main module [out]
                ('dwTypeIDMainOffset', DWORD),
                # Multistring array of TypeNames in main module [out]
                ('dwTypeNameMainOffset', DWORD),
                # Number of TypeIDs in MUI module [out]
                ('dwTypeIDMUISize', DWORD),
                # Array of TypeIDs (DWORD) in MUI module [out]
                ('dwTypeIDMUIOffset', DWORD),
                # Multistring array of TypeNames in MUI module [out]
                ('dwTypeNameMUIOffset', DWORD),
                # Buffer for extra data [in] (Size 4 is for padding)
                ('abBuffer', BYTE * 8),
            ]
            if not defined(NOAPISET):
                # String APISET dependencies
                from pyWinAPI.um.stringapiset_h import * # NOQA
            # END IF


            # //////////////////////////////////////////////////////////////////////////
            #
            # Macros
            # Define all macros for the NLS component here.
            # //////////////////////////////////////////////////////////////////////////
            #
            # Macros to determine whether a character is a high or low
            # surrogate,
            # and whether two code points make up a surrogate pair
            # (a high surrogate
            # and a low surrogate).
            def IS_HIGH_SURROGATE(wch):
                return (
                    (wch >= HIGH_SURROGATE_START) and
                    (wch <= HIGH_SURROGATE_END)
                )


            def IS_LOW_SURROGATE(wch):
                return (
                    (wch >= LOW_SURROGATE_START) and
                    (wch <= LOW_SURROGATE_END)
                )


            def IS_SURROGATE_PAIR(hs, ls):
                return IS_HIGH_SURROGATEhs and IS_LOW_SURROGATEls

            # --------------------------------------------------------
            # The following macros retrieve information from a MUIFILEINFO
            # structure
            # Gets the culture name (LPWSTR), NULL if not initialized
            def FILEMUIINFO_GET_CULTURE(pInfo):
                if pInfo.dwLanguageNameOffset > 0:
                    return ctypes.byref(pInfo) + pInfo.dwLanguageNameOffset
                else:
                    return NULL

            # Gets the main module types array (DWORD[]), NULL if not
            # initialized
            def FILEMUIINFO_GET_MAIN_TYPEIDS(pInfo):
                if pInfo.dwTypeIDMainOffset > 0:
                    return ctypes.byref(pInfo) + pInfo.dwTypeIDMainOffset
                else:
                    return NULL
            # Gets the main module type array element iType (DWORD), the array
            # is not initialized or index is out of bounds
            def FILEMUIINFO_GET_MAIN_TYPEID(pInfo, iType):
                if iType < pInfo.dwTypeIDMainSize and pInfo.dwTypeIDMainOffset > 0:
                    return ctypes.byref(pInfo) + pInfo.dwTypeIDMainOffset + iType
                else:
                    return 0
            # Gets the main module names multistring array (LPWSTR), NULL if
            # not initialized
            def FILEMUIINFO_GET_MAIN_TYPENAMES(pInfo):
                if  pInfo.dwTypeNameMainOffset > 0:
                    return ctypes.byref(pInfo) + pInfo.dwTypeNameMainOffset
                else:
                    return NULL
            # Gets the mui module types array (DWORD[]), NULL if not
            # initialized
            def FILEMUIINFO_GET_MUI_TYPEIDS(pInfo):
                if pInfo.dwTypeIDMUIOffset > 0:
                    return ctypes.byref(pInfo) + pInfo.dwTypeIDMUIOffset
                else:
                    return NULL
            # Gets the mui module type array element iType (DWORD), the array
            # is not initialized or index is out of bounds
            def FILEMUIINFO_GET_MUI_TYPEID(pInfo, iType):
                if iType < pInfo.dwTypeIDMUISize and pInfo.dwTypeIDMUIOffset > 0:
                    return ctypes.byref(pInfo) + pInfo.dwTypeIDMUIOffset + iType
                else:
                    return 0
            # Gets the mui module names multistring array (LPWSTR), NULL if
            # not initialized
            def FILEMUIINFO_GET_MUI_TYPENAMES(pInfo):
                if pInfo.dwTypeNameMUIOffset > 0:
                    return ctypes.byref(pInfo) + pInfo.dwTypeNameMUIOffset
                else:
                    return NULL
            # ----------------------------------------------------------
            # //////////////////////////////////////////////////////////////////////////
            #
            # Function Prototypes
            # Only prototypes for the NLS APIs should go here.
            # //////////////////////////////////////////////////////////////////////////
            #
            # Code Page Dependent APIs.
            # Applications should use Unicode (WCHAR / UTF-16 & /or UTF-8)
            kernel32 = ctypes.windll.KERNEL32
            # WINBASEAPI
            # BOOL
            # WINAPI
            # IsValidCodePage(
            # _In_ UINT  CodePage);
            IsValidCodePage = kernel32.IsValidCodePage
            IsValidCodePage.restype = BOOL
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM):
            kernel32 = ctypes.windll.KERNEL32


            # DEPRECATED("Use Unicode. The information in this structure cannot represent all encodings accuratedly and may be unreliable on many machines. Set DISABLE_NLS_DEPRECATION to disable this warning.")
            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetCPInfo(
            # _In_ UINT       CodePage,
            # _Out_ LPCPINFO  lpCPInfo);
            GetCPInfo = kernel32.GetCPInfo
            GetCPInfo.restype = BOOL


            # DEPRECATED("Use Unicode. The information in this structure cannot represent all encodings accurately and may be unreliable on many machines. Set DISABLE_NLS_DEPRECATION to disable this warning.")
            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetCPInfoExA(
            # _In_ UINT          CodePage,
            # _In_ DWORD         dwFlags,
            # _Out_ LPCPINFOEXA  lpCPInfoEx);
            GetCPInfoExA = kernel32.GetCPInfoExA
            GetCPInfoExA.restype = BOOL


            # DEPRECATED("Use Unicode. The information in this structure cannot represent all encodings accurately and may be unreliable on many machines. Set DISABLE_NLS_DEPRECATION to disable this warning.")
            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetCPInfoExW(
            # _In_ UINT          CodePage,
            # _In_ DWORD         dwFlags,
            # _Out_ LPCPINFOEXW  lpCPInfoEx);
            GetCPInfoExW = kernel32.GetCPInfoExW
            GetCPInfoExW.restype = BOOL

            if defined(UNICODE):
                GetCPInfoEx = GetCPInfoExW
            else:
                GetCPInfoEx = GetCPInfoExA
            # END IF   not UNICODE
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # Locale Dependent APIs.
            # DEPRECATED: CompareStringEx is preferred
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # int
            # WINAPI
            # CompareStringA(
            # _In_ LCID     Locale,
            # _In_ DWORD    dwCmpFlags,
            # _In_reads_(cchCount1) PCNZCH lpString1,
            # _In_ INT      cchCount1,
            # _In_reads_(cchCount2) PCNZCH  lpString2,
            # _In_ INT      cchCount2);
            CompareStringA = kernel32.CompareStringA
            CompareStringA.restype = INT

            if not defined(UNICODE):
                CompareString = CompareStringA
            # END IF   not UNICODE

            if defined(_M_CEE):
                kernel32 = ctypes.windll.KERNEL32


                # __inline
                # int
                # CompareString(
                # LCID     Locale,
                # DWORD    dwCmpFlags,
                # LPCTSTR  lpString1,
                # INT      cchCount1,
                # LPCTSTR  lpString2,
                # INT      cchCount2
                # )
                # {
                # #ifdef UNICODE
                # return CompareStringW(
                # #else
                # return CompareStringA(
                # #endif
                # Locale,
                # dwCmpFlags,
                # lpString1,
                # cchCount1,
                # lpString2,
                # cchCount2
                # );
                CompareStringW = kernel32.CompareStringW
                CompareStringW.restype = UNICODE
                # }
                # #endif // _M_CEE
                #
                # #if (WINVER >= 0x0600)
                #
                # // DEPRECATED: FindNLSStringEx is preferred
                # WINBASEAPI
                # int
                # WINAPI
                # FindNLSString(
                # _In_                    LCID Locale,
                # _In_                    DWORD dwFindNLSStringFlags,
                # _In_reads_(cchSource)  LPCWSTR lpStringSource,
                # _In_                    INT cchSource,
                # _In_reads_(cchValue)   LPCWSTR lpStringValue,
                # _In_                    INT cchValue,
                # _Out_opt_               LPINT pcchFound);
                FindNLSString = kernel32.FindNLSString
                FindNLSString.restype = INT

            # END IF  (WINVER >= 0x0600)
            # DEPRECATED: LCMapStringEx is preferred
            # WINBASEAPI
            # int
            # WINAPI
            # LCMapStringW(
            # _In_ LCID     Locale,
            # _In_ DWORD    dwMapFlags,
            # _In_reads_(cchSrc) LPCWSTR  lpSrcStr,
            # _In_ INT      cchSrc,
            # _Out_writes_opt_(_Inexpressible_(cchDest)) LPWSTR  lpDestStr,
            # _In_ INT      cchDest);
            LCMapStringW = kernel32.LCMapStringW
            LCMapStringW.restype = INT
            if defined(UNICODE):
                LCMapString = LCMapStringW
            # END IF


            # DEPRECATED: Use Unicode, LCMapStringEx is preferred
            # WINBASEAPI
            # int
            # WINAPI
            # LCMapStringA(
            # _In_ LCID     Locale,
            # _In_ DWORD    dwMapFlags,
            # _In_reads_(cchSrc) LPCSTR  lpSrcStr,
            # _In_ INT      cchSrc,
            # _Out_writes_opt_(_Inexpressible_(cchDest)) LPSTR  lpDestStr,
            # _In_ INT      cchDest);
            LCMapStringA = kernel32.LCMapStringA
            LCMapStringA.restype = INT

            if not defined(UNICODE):
                LCMapString = LCMapStringA
            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # DEPRECATED: GetLocaleInfoEx is preferred
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # int
            # WINAPI
            # GetLocaleInfoW(
            # _In_ LCID     Locale,
            # _In_ LCTYPE   LCType,
            # _Out_writes_opt_(cchData) LPWSTR lpLCData,
            # _In_ INT      cchData);
            GetLocaleInfoW = kernel32.GetLocaleInfoW
            GetLocaleInfoW.restype = INT

            if defined(UNICODE):
                GetLocaleInfo = GetLocaleInfoW
            # END IF


            # DEPRECATED: Use Unicode. GetLocaleInfoEx is preferred
            # WINBASEAPI
            # INT
            # WINAPI
            # GetLocaleInfoA(
            # _In_ LCID Locale,
            # _In_ LCTYPE LCType,
            # _Out_writes_opt_(cchData) LPSTR lpLCData,
            # _In_ INT cchData
            # );
            GetLocaleInfoA = kernel32.GetLocaleInfoA
            GetLocaleInfoA.restype = INT

            if not defined(UNICODE):
                GetLocaleInfo = GetLocaleInfoA
            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # BOOL
            # WINAPI
            # SetLocaleInfoA(
            # _In_ LCID     Locale,
            # _In_ LCTYPE   LCType,
            # _In_ LPCSTR  lpLCData);
            SetLocaleInfoA = kernel32.SetLocaleInfoA
            SetLocaleInfoA.restype = BOOL


            # WINBASEAPI
            # BOOL
            # WINAPI
            # SetLocaleInfoW(
            # _In_ LCID     Locale,
            # _In_ LCTYPE   LCType,
            # _In_ LPCWSTR  lpLCData);
            SetLocaleInfoW = kernel32.SetLocaleInfoW
            SetLocaleInfoW.restype = BOOL

            if defined(UNICODE):
                SetLocaleInfo = SetLocaleInfoW
            else:
                SetLocaleInfo = SetLocaleInfoA
            # END IF   not UNICODE

            if WINVER >= 0x040A:
                # DEPRECATED: GetCalendarInfoEx is preferred
                # WINBASEAPI
                # int
                # WINAPI
                # GetCalendarInfoA(
                # _In_ LCID     Locale,
                # _In_ CALID    Calendar,
                # _In_ CALTYPE  CalType,
                # _Out_writes_opt_(cchData) LPSTR   lpCalData,
                # _In_ INT      cchData,
                # _Out_opt_ LPDWORD  lpValue);
                GetCalendarInfoA = kernel32.GetCalendarInfoA
                GetCalendarInfoA.restype = INT

                # DEPRECATED: GetCalendarInfoEx is preferred
                # WINBASEAPI
                # int
                # WINAPI
                # GetCalendarInfoW(
                # _In_ LCID     Locale,
                # _In_ CALID    Calendar,
                # _In_ CALTYPE  CalType,
                # _Out_writes_opt_(cchData) LPWSTR   lpCalData,
                # _In_ INT      cchData,
                # _Out_opt_ LPDWORD  lpValue);
                GetCalendarInfoW = kernel32.GetCalendarInfoW
                GetCalendarInfoW.restype = INT

                if defined(UNICODE):
                    GetCalendarInfo = GetCalendarInfoW
                else:
                    GetCalendarInfo = GetCalendarInfoA
                # END IF   not UNICODE


                # WINBASEAPI
                # BOOL
                # WINAPI
                # SetCalendarInfoA(
                # _In_ LCID     Locale,
                # _In_ CALID    Calendar,
                # _In_ CALTYPE  CalType,
                # _In_ LPCSTR  lpCalData);
                SetCalendarInfoA = kernel32.SetCalendarInfoA
                SetCalendarInfoA.restype = BOOL


                # WINBASEAPI
                # BOOL
                # WINAPI
                # SetCalendarInfoW(
                # _In_ LCID     Locale,
                # _In_ CALID    Calendar,
                # _In_ CALTYPE  CalType,
                # _In_ LPCWSTR  lpCalData);
                SetCalendarInfoW = kernel32.SetCalendarInfoW
                SetCalendarInfoW.restype = BOOL

                if defined(UNICODE):
                    SetCalendarInfo = SetCalendarInfoW
                else:
                    SetCalendarInfo = SetCalendarInfoA
                # END IF   not UNICODE
            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            if WINVER >= _WIN32_WINNT_WIN7:
                # Flags used by LoadStringByReference
                MUI_FORMAT_REG_COMPAT = 0x0001
                MUI_FORMAT_INF_COMPAT = 0x0002
                MUI_VERIFY_FILE_EXISTS = 0x0004
                MUI_SKIP_STRING_CACHE = 0x0008
                MUI_IMMUTABLE_LOOKUP = 0x0010
                kernelbase = ctypes.windll.KERNELBASE


                # WINBASEAPI
                # BOOL
                # WINAPI
                # LoadStringByReference(
                # _In_       DWORD   Flags,
                # _In_opt_       PCWSTR  Language,
                # _In_       PCWSTR  SourceString,
                # _Out_writes_opt_(cchBuffer)   PWSTR   Buffer,
                # _In_       ULONG  cchBuffer,
                # _In_opt_   PCWSTR  Directory,
                # _Out_opt_  PULONG  pcchBufferOut
                # );
                LoadStringByReference = kernelbase.LoadStringByReference
                LoadStringByReference.restype = BOOL

            # END IF   (WINVER >= _WIN32_WINNT_WIN7)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            kernel32 = ctypes.windll.KERNEL32


            # DEPRECATED("Use Unicode. The information provided by this structure is inaccurate for some encodings and may be unreliable on many machines.")
            # WINBASEAPI
            # BOOL
            # WINAPI
            # IsDBCSLeadByte(
            # _In_ BYTE  TestChar
            # );
            IsDBCSLeadByte = kernel32.IsDBCSLeadByte
            IsDBCSLeadByte.restype = BOOL


            # DEPRECATED("Use Unicode. The information provided by this structure is inaccurate for some encodings and may be unreliable on many machines.")
            # WINBASEAPI
            # BOOL
            # WINAPI
            # IsDBCSLeadByteEx(
            # _In_ UINT  CodePage,
            # _In_ BYTE  TestChar
            # );
            IsDBCSLeadByteEx = kernel32.IsDBCSLeadByteEx
            IsDBCSLeadByteEx.restype = BOOL

            if WINVER >= 0x0600:
                # Use of Locale Names is preferred, LCIDs are deprecated.
                # This function is provided to enable compatibility with
                # legacy data sets only.
                # WINBASEAPI
                # int
                # WINAPI
                # LCIDToLocaleName(
                # _In_ LCID     Locale,
                # _Out_writes_opt_(cchName) LPWSTR  lpName,
                # _In_ INT      cchName,
                # _In_ DWORD    dwFlags);
                LCIDToLocaleName = kernel32.LCIDToLocaleName
                LCIDToLocaleName.restype = INT

                # Use of Locale Names is preferred, LCIDs are deprecated.
                # This function is provided to enable compatibility with
                # legacy data sets only.
                # WINBASEAPI
                # LCID
                # WINAPI
                # LocaleNameToLCID(
                # _In_ LPCWSTR lpName,
                # _In_ DWORD dwFlags);
                LocaleNameToLCID = kernel32.LocaleNameToLCID
                LocaleNameToLCID.restype = LCID
            # END IF   (WINVER >= 0x0600)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            # DEPRECATED: GetDurationFormatEx is preferred
            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # int
                # WINAPI
                # GetDurationFormat(
                # _In_ LCID             Locale,
                # _In_ DWORD            dwFlags,
                # _In_opt_ CONST SYSTEMTIME *lpDuration,
                # _In_ ULONGLONG ullDuration,
                # _In_opt_ LPCWSTR          lpFormat,
                # _Out_writes_opt_(cchDuration) LPWSTR          lpDurationStr,
                # _In_ INT              cchDuration);
                GetDurationFormat = kernel32.GetDurationFormat
                GetDurationFormat.restype = INT

            # END IF  (WINVER >= 0x0600)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # DEPRECATED: GetNumberFormatEx is preferred
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # int
            # WINAPI
            # GetNumberFormatA(
            # _In_ LCID             Locale,
            # _In_ DWORD            dwFlags,
            # _In_ LPCSTR          lpValue,
            # _In_opt_ CONST NUMBERFMTA *lpFormat,
            # _Out_writes_opt_(cchNumber) LPSTR          lpNumberStr,
            # _In_ INT              cchNumber);
            GetNumberFormatA = kernel32.GetNumberFormatA
            GetNumberFormatA.restype = INT


            # DEPRECATED: GetNumberFormatEx is preferred
            # WINBASEAPI
            # int
            # WINAPI
            # GetNumberFormatW(
            # _In_ LCID             Locale,
            # _In_ DWORD            dwFlags,
            # _In_ LPCWSTR          lpValue,
            # _In_opt_ CONST NUMBERFMTW *lpFormat,
            # _Out_writes_opt_(cchNumber) LPWSTR          lpNumberStr,
            # _In_ INT              cchNumber);
            GetNumberFormatW = kernel32.GetNumberFormatW
            GetNumberFormatW.restype = INT

            if defined(UNICODE):
                GetNumberFormat = GetNumberFormatW
            else:
                GetNumberFormat = GetNumberFormatA
            # END IF   not UNICODE

            # DEPRECATED: GetCurrencyFormatEx is preferred
            # WINBASEAPI
            # int
            # WINAPI
            # GetCurrencyFormatA(
            # _In_ LCID               Locale,
            # _In_ DWORD              dwFlags,
            # _In_ LPCSTR            lpValue,
            # _In_opt_ CONST CURRENCYFMTA *lpFormat,
            # _Out_writes_opt_(cchCurrency) LPSTR            lpCurrencyStr,
            # _In_ INT                cchCurrency);
            GetCurrencyFormatA = kernel32.GetCurrencyFormatA
            GetCurrencyFormatA.restype = INT

            # DEPRECATED: GetCurrencyFormatEx is preferred
            # WINBASEAPI
            # int
            # WINAPI
            # GetCurrencyFormatW(
            # _In_ LCID               Locale,
            # _In_ DWORD              dwFlags,
            # _In_ LPCWSTR            lpValue,
            # _In_opt_ CONST CURRENCYFMTW *lpFormat,
            # _Out_writes_opt_(cchCurrency) LPWSTR            lpCurrencyStr,
            # _In_ INT                cchCurrency);
            GetCurrencyFormatW = kernel32.GetCurrencyFormatW
            GetCurrencyFormatW.restype = INT

            if defined(UNICODE):
                GetCurrencyFormat = GetCurrencyFormatW
            else:
                GetCurrencyFormat = GetCurrencyFormatA
            # END IF   not UNICODE

            # DEPRECATED: EnumCalendarInfoExEx is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumCalendarInfoA(
            # _In_ CALINFO_ENUMPROCA lpCalInfoEnumProc,
            # _In_ LCID              Locale,
            # _In_ CALID             Calendar,
            # _In_ CALTYPE           CalType);
            EnumCalendarInfoA = kernel32.EnumCalendarInfoA
            EnumCalendarInfoA.restype = BOOL

            # DEPRECATED: EnumCalendarInfoExEx is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumCalendarInfoW(
            # _In_ CALINFO_ENUMPROCW lpCalInfoEnumProc,
            # _In_ LCID              Locale,
            # _In_ CALID             Calendar,
            # _In_ CALTYPE           CalType);
            EnumCalendarInfoW = kernel32.EnumCalendarInfoW
            EnumCalendarInfoW.restype = BOOL

            if defined(UNICODE):
                EnumCalendarInfo = EnumCalendarInfoW
            else:
                EnumCalendarInfo = EnumCalendarInfoA
            # END IF   not UNICODE

            if WINVER >= 0x0500:
                # DEPRECATED: EnumCalendarInfoExEx is preferred
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumCalendarInfoExA(
                # _In_ CALINFO_ENUMPROCEXA lpCalInfoEnumProcEx,
                # _In_ LCID                Locale,
                # _In_ CALID               Calendar,
                # _In_ CALTYPE             CalType);
                EnumCalendarInfoExA = kernel32.EnumCalendarInfoExA
                EnumCalendarInfoExA.restype = BOOL

                # DEPRECATED: EnumCalendarInfoExEx is preferred
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumCalendarInfoExW(
                # _In_ CALINFO_ENUMPROCEXW lpCalInfoEnumProcEx,
                # _In_ LCID                Locale,
                # _In_ CALID               Calendar,
                # _In_ CALTYPE             CalType);
                EnumCalendarInfoExW = kernel32.EnumCalendarInfoExW
                EnumCalendarInfoExW.restype = BOOL

                if defined(UNICODE):
                    EnumCalendarInfoEx = EnumCalendarInfoExW
                else:
                    EnumCalendarInfoEx = EnumCalendarInfoExA
                # END IF   not UNICODE
            # END IF  WINVER >= 0x0500

            # DEPRECATED: EnumTimeFormatsEx is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumTimeFormatsA(
            # _In_ TIMEFMT_ENUMPROCA lpTimeFmtEnumProc,
            # _In_ LCID              Locale,
            # _In_ DWORD             dwFlags);
            EnumTimeFormatsA = kernel32.EnumTimeFormatsA
            EnumTimeFormatsA.restype = BOOL

            # DEPRECATED: EnumTimeFormatsEx is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumTimeFormatsW(
            # _In_ TIMEFMT_ENUMPROCW lpTimeFmtEnumProc,
            # _In_ LCID              Locale,
            # _In_ DWORD             dwFlags);
            EnumTimeFormatsW = kernel32.EnumTimeFormatsW
            EnumTimeFormatsW.restype = BOOL

            if defined(UNICODE):
                EnumTimeFormats = EnumTimeFormatsW
            else:
                EnumTimeFormats = EnumTimeFormatsA
            # END IF   not UNICODE

            # DEPRECATED: EnumDateFormatsExEx is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumDateFormatsA(
            # _In_ DATEFMT_ENUMPROCA lpDateFmtEnumProc,
            # _In_ LCID              Locale,
            # _In_ DWORD             dwFlags);
            EnumDateFormatsA = kernel32.EnumDateFormatsA
            EnumDateFormatsA.restype = BOOL

            # DEPRECATED: EnumDateFormatsExEx is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumDateFormatsW(
            # _In_ DATEFMT_ENUMPROCW lpDateFmtEnumProc,
            # _In_ LCID              Locale,
            # _In_ DWORD             dwFlags);
            EnumDateFormatsW = kernel32.EnumDateFormatsW
            EnumDateFormatsW.restype = BOOL

            if defined(UNICODE):
                EnumDateFormats = EnumDateFormatsW
            else:
                EnumDateFormats = EnumDateFormatsA
            # END IF   not UNICODE

            if WINVER >= 0x0500:
                # DEPRECATED: EnumDateFormatsExEx is preferred
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumDateFormatsExA(
                # _In_ DATEFMT_ENUMPROCEXA lpDateFmtEnumProcEx,
                # _In_ LCID                Locale,
                # _In_ DWORD               dwFlags);
                EnumDateFormatsExA = kernel32.EnumDateFormatsExA
                EnumDateFormatsExA.restype = BOOL

                # DEPRECATED: EnumDateFormatsExEx is preferred
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumDateFormatsExW(
                # _In_ DATEFMT_ENUMPROCEXW lpDateFmtEnumProcEx,
                # _In_ LCID                Locale,
                # _In_ DWORD               dwFlags);
                EnumDateFormatsExW = kernel32.EnumDateFormatsExW
                EnumDateFormatsExW.restype = BOOL

                if defined(UNICODE):
                    EnumDateFormatsEx = EnumDateFormatsExW
                else:
                    EnumDateFormatsEx = EnumDateFormatsExA
                # END IF   not UNICODE
            # END IF  WINVER >= 0x0500

            if WINVER >= 0x0500:
                kernel32 = ctypes.windll.KERNEL32


                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                # WINBASEAPI
                # BOOL
                # WINAPI
                # IsValidLanguageGroup(
                # _In_ LGRPID  LanguageGroup,
                # _In_ DWORD   dwFlags);
                IsValidLanguageGroup = kernel32.IsValidLanguageGroup
                IsValidLanguageGroup.restype = BOOL

            # END IF  WINVER >= 0x0500

            # DEPRECATED: GetNLSVersionEx is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetNLSVersion(
            # _In_    NLS_FUNCTION     Function,
            # _In_    LCID             Locale,
            # _Inout_ LPNLSVERSIONINFO lpVersionInformation);
            GetNLSVersion = kernel32.GetNLSVersion
            GetNLSVersion.restype = BOOL

            # DEPRECATED: IsValidLocaleName is preferred
            # WINBASEAPI
            # BOOL
            # WINAPI
            # IsValidLocale(
            # _In_ LCID   Locale,
            # _In_ DWORD  dwFlags);
            IsValidLocale = kernel32.IsValidLocale
            IsValidLocale.restype = BOOL
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # GetGeoInfoEx is preferred where available
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # int
            # WINAPI
            # GetGeoInfoA(
            # _In_ GEOID       Location,
            # _In_ GEOTYPE     GeoType,
            # _Out_writes_opt_(cchData) LPSTR     lpGeoData,
            # _In_ INT         cchData,
            # _In_ LANGID      LangId);
            GetGeoInfoA = kernel32.GetGeoInfoA
            GetGeoInfoA.restype = INT


            # GetGeoInfoEx is preferred where available
            # WINBASEAPI
            # int
            # WINAPI
            # GetGeoInfoW(
            # _In_ GEOID       Location,
            # _In_ GEOTYPE     GeoType,
            # _Out_writes_opt_(cchData) LPWSTR     lpGeoData,
            # _In_ INT         cchData,
            # _In_ LANGID      LangId);
            GetGeoInfoW = kernel32.GetGeoInfoW
            GetGeoInfoW.restype = INT

            if defined(UNICODE):
                GetGeoInfo = GetGeoInfoW
            else:
                GetGeoInfo = GetGeoInfoA
            # END IF   not UNICODE

            if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # int
                # WINAPI
                # GetGeoInfoEx(
                # _In_ PWSTR       location,
                # _In_ GEOTYPE     geoType,
                # _Out_writes_opt_(geoDataCount) PWSTR    geoData,
                # _In_ INT         geoDataCount);
                GetGeoInfoEx = kernel32.GetGeoInfoEx
                GetGeoInfoEx.restype = INT

            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM):
            # EnumSystemGeoNames is preferred where available
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumSystemGeoID(
            # _In_ GEOCLASS        GeoClass,
            # _In_ GEOID           ParentGeoId,
            # _In_ GEO_ENUMPROC    lpGeoEnumProc);
            EnumSystemGeoID = kernel32.EnumSystemGeoID
            EnumSystemGeoID.restype = BOOL

            if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumSystemGeoNames(
                # _In_ GEOCLASS            geoClass,
                # _In_ GEO_ENUMNAMEPROC    geoEnumProc,
                # _In_opt_ LPARAM          data);
                EnumSystemGeoNames = kernel32.EnumSystemGeoNames
                EnumSystemGeoNames.restype = BOOL

            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            # GetUserDefaultGeoName is preferred where available
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # GEOID
            # WINAPI
            # GetUserGeoID(
            # _In_ GEOCLASS    GeoClass);
            GetUserGeoID = kernel32.GetUserGeoID
            GetUserGeoID.restype = GEOID


            # Note: This API was added in the Windows 10 Fall Creators Update.
            # (Please use this API instead of calling GetUserGeoID.)
            # WINBASEAPI
            # int
            # WINAPI
            # GetUserDefaultGeoName(
            # _Out_writes_z_(geoNameCount) LPWSTR geoName,
            # _In_ INT geoNameCount
            # );
            GetUserDefaultGeoName = kernel32.GetUserDefaultGeoName
            GetUserDefaultGeoName.restype = INT
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # GetUserDefaultGeoName is preferred where available
            # Applications are recommended to not change user settings
            # themselves.
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # BOOL
            # WINAPI
            # SetUserGeoID(
            # _In_ GEOID       GeoId);
            SetUserGeoID = kernel32.SetUserGeoID
            SetUserGeoID.restype = BOOL

            if NTDDI_VERSION >= NTDDI_WIN10_RS3:
                # Applications are recommended to not change user settings
                # themselves.
                # WINBASEAPI
                # BOOL
                # WINAPI
                # SetUserGeoName(
                # _In_ PWSTR       geoName);
                SetUserGeoName = kernel32.SetUserGeoName
                SetUserGeoName.restype = BOOL
            # END IF


            # DEPRECATED: Please use ResolveLocaleName
            # WINBASEAPI
            # LCID
            # WINAPI
            # ConvertDefaultLocale(
            # _In_ LCID   Locale);
            ConvertDefaultLocale = kernel32.ConvertDefaultLocale
            ConvertDefaultLocale.restype = LCID


            # WINBASEAPI
            # BOOL
            # WINAPI
            # SetThreadLocale(
            # _In_ LCID  Locale
            # );
            SetThreadLocale = kernel32.SetThreadLocale
            SetThreadLocale.restype = BOOL

            if WINVER >= 0x0500:
                # DEPRECATED: Please use the user's language profile.

                if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                    # DEPRECATED: Please use the user's language profile.
                    pass
                # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

            # END IF  WINVER >= 0x0500
            # DEPRECATED: Please use GetUserDefaultLocaleName
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # DEPRECATED: Please use GetUserDefaultLocaleName or the user's
            # Language Profile
            # DEPRECATED: Please use GetUserDefaultLocaleName or the user's
            # Language Profile
            # DEPRECATED: Please use GetUserDefaultLocaleName
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            pass
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # LANGID
            # WINAPI
            # SetThreadUILanguage(_In_ LANGID LangId);
            SetThreadUILanguage = kernel32.SetThreadUILanguage
            SetThreadUILanguage.restype = LANGID

            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetProcessPreferredUILanguages(
                # _In_ DWORD dwFlags,
                # _Out_ PULONG pulNumLanguages,
                # _Out_writes_opt_(*pcchLanguagesBuffer) PZZWSTR pwszLanguagesBuffer,
                # _Inout_ PULONG pcchLanguagesBuffer
                # );
                GetProcessPreferredUILanguages = (
                    kernel32.GetProcessPreferredUILanguages
                )
                GetProcessPreferredUILanguages.restype = BOOL


                # WINBASEAPI
                # BOOL
                # WINAPI
                # SetProcessPreferredUILanguages(
                # _In_        DWORD dwFlags,
                # _In_opt_    PCZZWSTR pwszLanguagesBuffer,
                # _Out_opt_   PULONG pulNumLanguages
                # );
                SetProcessPreferredUILanguages = (
                    kernel32.SetProcessPreferredUILanguages
                )
                SetProcessPreferredUILanguages.restype = BOOL
            # END IF  WINVER >= 0x0600
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PHONE_APP | WINAPI_PARTITION_SYSTEM):
            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetUserPreferredUILanguages(
                # _In_ DWORD dwFlags,
                # _Out_ PULONG pulNumLanguages,
                # _Out_writes_opt_(*pcchLanguagesBuffer) PZZWSTR pwszLanguagesBuffer,
                # _Inout_ PULONG pcchLanguagesBuffer
                # );
                GetUserPreferredUILanguages = (
                    kernel32.GetUserPreferredUILanguages
                )
                GetUserPreferredUILanguages.restype = BOOL

            # END IF  WINVER >= 0x0600
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PHONE_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetSystemPreferredUILanguages(
                # _In_ DWORD dwFlags,
                # _Out_ PULONG pulNumLanguages,
                # _Out_writes_opt_(*pcchLanguagesBuffer) PZZWSTR pwszLanguagesBuffer,
                # _Inout_ PULONG pcchLanguagesBuffer
                # );
                GetSystemPreferredUILanguages = (
                    kernel32.GetSystemPreferredUILanguages
                )
                GetSystemPreferredUILanguages.restype = BOOL


                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetThreadPreferredUILanguages(
                # _In_ DWORD dwFlags,
                # _Out_ PULONG pulNumLanguages,
                # _Out_writes_opt_(*pcchLanguagesBuffer) PZZWSTR pwszLanguagesBuffer,
                # _Inout_ PULONG pcchLanguagesBuffer
                # );
                GetThreadPreferredUILanguages = (
                    kernel32.GetThreadPreferredUILanguages
                )
                GetThreadPreferredUILanguages.restype = BOOL


                # WINBASEAPI
                # BOOL
                # WINAPI
                # SetThreadPreferredUILanguages(
                # _In_        DWORD dwFlags,
                # _In_opt_    PCZZWSTR pwszLanguagesBuffer,
                # _Out_opt_   PULONG pulNumLanguages
                # );
                SetThreadPreferredUILanguages = (
                    kernel32.SetThreadPreferredUILanguages
                )
                SetThreadPreferredUILanguages.restype = BOOL


                # WINBASEAPI
                # _Success_(return != FALSE)
                # BOOL
                # WINAPI
                # GetFileMUIInfo(
                # DWORD           dwFlags,
                # _In_                PCWSTR          pcwszFilePath,
                # _Inout_updates_bytes_to_opt_(*pcbFileMUIInfo,*pcbFileMUIInfo) PFILEMUIINFO    pFileMUIInfo,
                # _Inout_             DWORD*          pcbFileMUIInfo);
                GetFileMUIInfo = kernel32.GetFileMUIInfo
                GetFileMUIInfo.restype = BOOL


                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetFileMUIPath(
                # _In_ DWORD      dwFlags,
                # _In_ PCWSTR     pcwszFilePath ,
                # _Inout_updates_opt_    (*pcchLanguage)   PWSTR pwszLanguage,
                # _Inout_ PULONG  pcchLanguage,
                # _Out_writes_opt_    (*pcchFileMUIPath) PWSTR pwszFileMUIPath,
                # _Inout_         PULONG pcchFileMUIPath,
                # _Inout_         PULONGLONG pululEnumerator
                # );
                GetFileMUIPath = kernel32.GetFileMUIPath
                GetFileMUIPath.restype = BOOL


                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetUILanguageInfo(
                # _In_ DWORD dwFlags,
                # _In_ PCZZWSTR pwmszLanguage,
                # _Out_writes_opt_(*pcchFallbackLanguages) PZZWSTR pwszFallbackLanguages,
                # _Inout_opt_ PDWORD pcchFallbackLanguages,
                # _Out_ PDWORD pAttributes
                # );
                GetUILanguageInfo = kernel32.GetUILanguageInfo
                GetUILanguageInfo.restype = BOOL
            # END IF  WINVER >= 0x0600
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # BOOL
                # WINAPI
                # NotifyUILanguageChange(
                # _In_        DWORD dwFlags,
                # _In_opt_    PCWSTR pcwstrNewLanguage,
                # _In_opt_    PCWSTR pcwstrPreviousLanguage,
                # _In_        DWORD dwReserved,
                # _Out_opt_   PDWORD pdwStatusRtrn
                # );
                NotifyUILanguageChange = kernel32.NotifyUILanguageChange
                NotifyUILanguageChange.restype = BOOL

            # END IF  WINVER >= 0x0600
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # Locale Independent APIs.
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetStringTypeExA(
            # _In_                 LCID       Locale,
            # _In_                 DWORD      dwInfoType,
            # _In_reads_(cchSrc)   LPCSTR   lpSrcStr,
            # _In_                 INT        cchSrc,
            # _Out_writes_(cchSrc) LPWORD     lpCharType);
            GetStringTypeExA = kernel32.GetStringTypeExA
            GetStringTypeExA.restype = BOOL

            if not defined(UNICODE):
                GetStringTypeEx = GetStringTypeExA
            # END IF

        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
            # NOTE: The parameters for GetStringTypeA and GetStringTypeW are
            # NOT the same. The W version was shipped in NT 3.1. The
            # A version was then shipped in 16-bit OLE with the wrong
            # parameters (ported from Win95). To be compatible, we
            # must break the relationship between the A and W versions
            # of GetStringType. There will be NO function call for the
            # generic GetStringType.
            # GetStringTypeEx (above) should be used instead.
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # BOOL
            # WINAPI
            # GetStringTypeA(
            # _In_ LCID     Locale,
            # _In_ DWORD    dwInfoType,
            # _In_reads_(cchSrc) LPCSTR   lpSrcStr,
            # _In_ INT      cchSrc,
            # _Out_ LPWORD  lpCharType);
            GetStringTypeA = kernel32.GetStringTypeA
            GetStringTypeA.restype = BOOL


            # WINBASEAPI
            # int
            # WINAPI
            # FoldStringA(
            # _In_ DWORD    dwMapFlags,
            # _In_reads_(cchSrc) LPCSTR  lpSrcStr,
            # _In_ INT      cchSrc,
            # _Out_writes_opt_(cchDest) LPSTR  lpDestStr,
            # _In_ INT      cchDest);
            FoldStringA = kernel32.FoldStringA
            FoldStringA.restype = INT

            if not defined(UNICODE):
                FoldString = FoldStringA
            # END IF


            if WINVER >= 0x0500:
                # DEPRECATED, please use Locale Names and call
                # EnumSystemLocalesEx
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumSystemLocalesA(
                # _In_ LOCALE_ENUMPROCA lpLocaleEnumProc,
                # _In_ DWORD            dwFlags);
                EnumSystemLocalesA = kernel32.EnumSystemLocalesA
                EnumSystemLocalesA.restype = BOOL

                # DEPRECATED, please use Locale Names and call
                # EnumSystemLocalesEx
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumSystemLocalesW(
                # _In_ LOCALE_ENUMPROCW lpLocaleEnumProc,
                # _In_ DWORD            dwFlags);
                EnumSystemLocalesW = kernel32.EnumSystemLocalesW
                EnumSystemLocalesW.restype = BOOL

                if defined(UNICODE):
                    EnumSystemLocales = EnumSystemLocalesW
                else:
                    EnumSystemLocales = EnumSystemLocalesA
                # END IF   not UNICODE
            # END IF  WINVER >= 0x0500

            if WINVER >= 0x0500:
                kernel32 = ctypes.windll.KERNEL32


                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumSystemLanguageGroupsA(
                # _In_ LANGUAGEGROUP_ENUMPROCA lpLanguageGroupEnumProc,
                # _In_ DWORD                   dwFlags,
                # _In_ LONG_PTR                lParam);
                EnumSystemLanguageGroupsA = kernel32.EnumSystemLanguageGroupsA
                EnumSystemLanguageGroupsA.restype = BOOL


                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumSystemLanguageGroupsW(
                # _In_ LANGUAGEGROUP_ENUMPROCW lpLanguageGroupEnumProc,
                # _In_ DWORD                   dwFlags,
                # _In_ LONG_PTR                lParam);
                EnumSystemLanguageGroupsW = kernel32.EnumSystemLanguageGroupsW
                EnumSystemLanguageGroupsW.restype = BOOL

                if defined(UNICODE):
                    EnumSystemLanguageGroups = EnumSystemLanguageGroupsW
                else:
                    EnumSystemLanguageGroups = EnumSystemLanguageGroupsA
                # END IF   not UNICODE


                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumLanguageGroupLocalesA(
                # _In_ LANGGROUPLOCALE_ENUMPROCA lpLangGroupLocaleEnumProc,
                # _In_ LGRPID                    LanguageGroup,
                # _In_ DWORD                     dwFlags,
                # _In_ LONG_PTR                  lParam);
                EnumLanguageGroupLocalesA = kernel32.EnumLanguageGroupLocalesA
                EnumLanguageGroupLocalesA.restype = BOOL


                # DEPRECATED("The Language Group concept is obsolete and no longer supported. Set DISABLE_NLS_DEPRECATION to disable this warning.")
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumLanguageGroupLocalesW(
                # _In_ LANGGROUPLOCALE_ENUMPROCW lpLangGroupLocaleEnumProc,
                # _In_ LGRPID                    LanguageGroup,
                # _In_ DWORD                     dwFlags,
                # _In_ LONG_PTR                  lParam);
                EnumLanguageGroupLocalesW = kernel32.EnumLanguageGroupLocalesW
                EnumLanguageGroupLocalesW.restype = BOOL

                if defined(UNICODE):
                    EnumLanguageGroupLocales = EnumLanguageGroupLocalesW
                else:
                    EnumLanguageGroupLocales = EnumLanguageGroupLocalesA
                # END IF   not UNICODE
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # DEPRECATED: use the user language profile instead.
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumUILanguagesA(
                # _In_ UILANGUAGE_ENUMPROCA lpUILanguageEnumProc,
                # _In_ DWORD                dwFlags,
                # _In_ LONG_PTR             lParam);
                EnumUILanguagesA = kernel32.EnumUILanguagesA
                EnumUILanguagesA.restype = BOOL

                # DEPRECATED: use the user language profile instead.
                # WINBASEAPI
                # BOOL
                # WINAPI
                # EnumUILanguagesW(
                # _In_ UILANGUAGE_ENUMPROCW lpUILanguageEnumProc,
                # _In_ DWORD                dwFlags,
                # _In_ LONG_PTR             lParam);
                EnumUILanguagesW = kernel32.EnumUILanguagesW
                EnumUILanguagesW.restype = BOOL

                if defined(UNICODE):
                    EnumUILanguages = EnumUILanguagesW
                else:
                    EnumUILanguages = EnumUILanguagesA
                # END IF   not UNICODE
            # END IF  WINVER >= 0x0500
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP  | WINAPI_PARTITION_SYSTEM):
            # Please use Unicode instead. Use of other code pages/encodings is
            # discouraged.
            kernel32 = ctypes.windll.KERNEL32


            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumSystemCodePagesA(
            # _In_ CODEPAGE_ENUMPROCA lpCodePageEnumProc,
            # _In_ DWORD              dwFlags);
            EnumSystemCodePagesA = kernel32.EnumSystemCodePagesA
            EnumSystemCodePagesA.restype = BOOL


            # Please use Unicode instead. Use of other code pages/encodings is
            # discouraged.
            # WINBASEAPI
            # BOOL
            # WINAPI
            # EnumSystemCodePagesW(
            # _In_ CODEPAGE_ENUMPROCW lpCodePageEnumProc,
            # _In_ DWORD              dwFlags);
            EnumSystemCodePagesW = kernel32.EnumSystemCodePagesW
            EnumSystemCodePagesW.restype = BOOL

            if defined(UNICODE):
                EnumSystemCodePages = EnumSystemCodePagesW
            else:
                EnumSystemCodePages = EnumSystemCodePagesA
            # END IF   not UNICODE
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP  | WINAPI_PARTITION_SYSTEM)


        # Windows API Normalization Functions
        if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINNORMALIZEAPI
                # int
                # WINAPI NormalizeString( _In_                          NORM_FORM NormForm,
                # _In_reads_(cwSrcLength)      LPCWSTR   lpSrcString,
                # _In_                          INT       cwSrcLength,
                # _Out_writes_opt_(cwDstLength) LPWSTR    lpDstString,
                # _In_                          INT       cwDstLength );
                NormalizeString = kernel32.NormalizeString
                NormalizeString.restype = INT


                # WINNORMALIZEAPI
                # BOOL
                # WINAPI IsNormalizedString( _In_                   NORM_FORM NormForm,
                # _In_reads_(cwLength)  LPCWSTR   lpString,
                # _In_                   INT       cwLength );
                IsNormalizedString = kernel32.IsNormalizedString
                IsNormalizedString.restype = BOOL
            # END IF  (WINVER >= 0x0600)


            if WINVER >= 0x0600:
                # IDN (International Domain Name) Functions
                # WINNORMALIZEAPI
                # int
                # WINAPI IdnToAscii(_In_                           DWORD    dwFlags,
                # _In_reads_(cchUnicodeChar)      LPCWSTR  lpUnicodeCharStr,
                # _In_                             INT      cchUnicodeChar,
                # _Out_writes_opt_(cchASCIIChar) LPWSTR   lpASCIICharStr,
                # _In_                             INT      cchASCIIChar);
                IdnToAscii = kernel32.IdnToAscii
                IdnToAscii.restype = INT
            # END IF  (WINVER >= 0x0600)

            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINNORMALIZEAPI
                # int
                # WINAPI IdnToNameprepUnicode(_In_                                DWORD   dwFlags,
                # _In_reads_(cchUnicodeChar)         LPCWSTR lpUnicodeCharStr,
                # _In_                                int     cchUnicodeChar,
                # _Out_writes_opt_(cchNameprepChar)   LPWSTR  lpNameprepCharStr,
                # _In_                                int     cchNameprepChar);
                IdnToNameprepUnicode = kernel32.IdnToNameprepUnicode
                IdnToNameprepUnicode.restype = INT

            # END IF  (WINVER >= 0x0600)

            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINNORMALIZEAPI
                # int
                # WINAPI IdnToUnicode(_In_                              DWORD   dwFlags,
                # _In_reads_(cchASCIIChar)         LPCWSTR lpASCIICharStr,
                # _In_                              INT     cchASCIIChar,
                # _Out_writes_opt_(cchUnicodeChar) LPWSTR  lpUnicodeCharStr,
                # _In_                              INT     cchUnicodeChar);
                IdnToUnicode = kernel32.IdnToUnicode
                IdnToUnicode.restype = INT

            # END IF  (WINVER >= 0x0600)

            if WINVER >= 0x0600:
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # BOOL
                # WINAPI VerifyScripts(
                # _In_    DWORD   dwFlags, // optional behavior flags
                # _In_    LPCWSTR lpLocaleScripts, // Locale list of scripts string
                # _In_    INT     cchLocaleScripts, // size of locale script list string
                # _In_    LPCWSTR lpTestScripts, // test scripts string
                # _In_    INT     cchTestScripts); // size of test list string
                VerifyScripts = kernel32.VerifyScripts
                VerifyScripts.restype = BOOL


                # WINBASEAPI
                # int
                # WINAPI GetStringScripts(
                # _In_                         DWORD   dwFlags, // optional behavior flags
                # _In_                         LPCWSTR lpString, // Unicode character input string
                # _In_                         INT     cchString, // size of input string
                # _Out_writes_opt_(cchScripts) LPWSTR  lpScripts, // Script list output string
                # _In_                         INT     cchScripts); // size of output string
                GetStringScripts = kernel32.GetStringScripts
                GetStringScripts.restype = INT
            # END IF  (WINVER >= 0x0600)
        # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)


        if WINVER >= 0x0600:
            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                # String based NLS APIs
                LOCALE_NAME_USER_DEFAULT = NULL
                LOCALE_NAME_INVARIANT = ""
                LOCALE_NAME_SYSTEM_DEFAULT = "not x-sys-default-locale"
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # int
                # WINAPI
                # GetLocaleInfoEx(
                # _In_opt_ LPCWSTR lpLocaleName,
                # _In_ LCTYPE LCType,
                # _Out_writes_to_opt_(cchData, return) LPWSTR lpLCData,
                # _In_ INT cchData
                # );
                GetLocaleInfoEx = kernel32.GetLocaleInfoEx
                GetLocaleInfoEx.restype = INT

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM):
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # int
                # WINAPI
                # GetCalendarInfoEx(
                # _In_opt_ LPCWSTR lpLocaleName,
                # _In_ CALID Calendar,
                # _In_opt_ LPCWSTR lpReserved,
                # _In_ CALTYPE CalType,
                # _Out_writes_opt_(cchData) LPWSTR lpCalData,
                # _In_ INT cchData,
                # _Out_opt_ LPDWORD lpValue
                # );
                GetCalendarInfoEx = kernel32.GetCalendarInfoEx
                GetCalendarInfoEx.restype = INT

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
                if not defined(GetDurationFormatEx_DEFINED):
                    kernel32 = ctypes.windll.KERNEL32


                    # WINBASEAPI
                    # int
                    # WINAPI
                    # GetDurationFormatEx(
                    # _In_opt_ LPCWSTR lpLocaleName,
                    # _In_ DWORD dwFlags,
                    # _In_opt_ CONST SYSTEMTIME *lpDuration,
                    # _In_ ULONGLONG ullDuration,
                    # _In_opt_ LPCWSTR lpFormat,
                    # _Out_writes_opt_(cchDuration) LPWSTR lpDurationStr,
                    # _In_ INT cchDuration
                    # );
                    GetDurationFormatEx = kernel32.GetDurationFormatEx
                    GetDurationFormatEx.restype = INT

                # END IF

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # int
                # WINAPI
                # GetNumberFormatEx(
                # _In_opt_ LPCWSTR lpLocaleName,
                # _In_ DWORD dwFlags,
                # _In_ LPCWSTR lpValue,
                # _In_opt_ CONST NUMBERFMTW *lpFormat,
                # _Out_writes_opt_(cchNumber) LPWSTR lpNumberStr,
                # _In_ INT cchNumber
                # );
                GetNumberFormatEx = kernel32.GetNumberFormatEx
                GetNumberFormatEx.restype = INT


                # WINBASEAPI
                # int
                # WINAPI
                # GetCurrencyFormatEx(
                # _In_opt_ LPCWSTR lpLocaleName,
                # _In_ DWORD dwFlags,
                # _In_ LPCWSTR lpValue,
                # _In_opt_ CONST CURRENCYFMTW *lpFormat,
                # _Out_writes_opt_(cchCurrency) LPWSTR lpCurrencyStr,
                # _In_ INT cchCurrency
                # );
                GetCurrencyFormatEx = kernel32.GetCurrencyFormatEx
                GetCurrencyFormatEx.restype = INT


                # WINBASEAPI
                # int
                # WINAPI
                # GetUserDefaultLocaleName(
                # _Out_writes_(cchLocaleName) LPWSTR lpLocaleName,
                # _In_ INT cchLocaleName
                # );
                GetUserDefaultLocaleName = kernel32.GetUserDefaultLocaleName
                GetUserDefaultLocaleName.restype = INT
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM):
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # int
                # WINAPI
                # GetSystemDefaultLocaleName(
                # _Out_writes_(cchLocaleName) LPWSTR lpLocaleName,
                # _In_ INT cchLocaleName
                # );
                GetSystemDefaultLocaleName = (
                    kernel32.GetSystemDefaultLocaleName
                )
                GetSystemDefaultLocaleName.restype = INT


                # WINBASEAPI
                # BOOL
                # WINAPI
                # IsNLSDefinedString(
                # _In_ NLS_FUNCTION     Function,
                # _In_ DWORD            dwFlags,
                # _In_ LPNLSVERSIONINFO lpVersionInformation,
                # _In_reads_(cchStr) LPCWSTR          lpString,
                # _In_ INT              cchStr);
                IsNLSDefinedString = kernel32.IsNLSDefinedString
                IsNLSDefinedString.restype = BOOL


                # WINBASEAPI
                # BOOL
                # WINAPI
                # GetNLSVersionEx(
                # _In_        NLS_FUNCTION function,
                # _In_opt_    LPCWSTR lpLocaleName,
                # _Inout_        LPNLSVERSIONINFOEX lpVersionInformation
                # );
                GetNLSVersionEx = kernel32.GetNLSVersionEx
                GetNLSVersionEx.restype = BOOL

                if WINVER >= _WIN32_WINNT_WIN8:
                    kernel32 = ctypes.windll.KERNEL32


                    # WINBASEAPI
                    # DWORD
                    # WINAPI
                    # IsValidNLSVersion(
                    # _In_        NLS_FUNCTION function,
                    # _In_opt_    LPCWSTR lpLocaleName,
                    # _In_        LPNLSVERSIONINFOEX lpVersionInformation
                    # );
                    IsValidNLSVersion = kernel32.IsValidNLSVersion
                    IsValidNLSVersion.restype = DWORD

                # END IF

            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                kernel32 = ctypes.windll.KERNEL32


                # WINBASEAPI
                # int
                # WINAPI
                # FindNLSStringEx(
                # _In_opt_ LPCWSTR lpLocaleName,
                # _In_ DWORD dwFindNLSStringFlags,
                # _In_reads_(cchSource) LPCWSTR lpStringSource,
                # _In_ INT cchSource,
                # _In_reads_(cchValue) LPCWSTR lpStringValue,
                # _In_ INT cchValue,
                # _Out_opt_ LPINT pcchFound,
                # _In_opt_ LPNLSVERSIONINFO lpVersionInformation,
                # _In_opt_ LPVOID lpReserved,
                # _In_opt_ LPARAM sortHandle
                # );
                FindNLSStringEx = kernel32.FindNLSStringEx
                FindNLSStringEx.restype = INT

                if WINVER >= _WIN32_WINNT_WIN8:
                    kernel32 = ctypes.windll.KERNEL32


                    # _When_((dwMapFlags & (LCMAP_SORTKEY | LCMAP_BYTEREV | LCMAP_HASH | LCMAP_SORTHANDLE)) != 0, _At_((LPBYTE) lpDestStr, _Out_writes_bytes_opt_(cchDest)))
                    # #else
                    # _When_((dwMapFlags & (LCMAP_SORTKEY | LCMAP_BYTEREV)) != 0, _At_((LPBYTE) lpDestStr, _Out_writes_bytes_opt_(cchDest)))
                    # #endif
                    # _When_(cchSrc != -1,  _At_((WCHAR *) lpSrcStr, _Out_writes_opt_(cchSrc)))
                    # _When_(cchDest != -1, _At_((WCHAR *) lpDestStr, _Out_writes_opt_(cchDest)))
                    # WINBASEAPI
                    # int
                    # WINAPI
                    # LCMapStringEx(
                    # _In_opt_ LPCWSTR lpLocaleName,
                    # _In_ DWORD dwMapFlags,
                    # _In_reads_(cchSrc) LPCWSTR lpSrcStr,
                    # _In_ INT cchSrc,
                    # _Out_writes_opt_(cchDest) LPWSTR lpDestStr,
                    # _In_ INT cchDest,
                    # _In_opt_ LPNLSVERSIONINFO lpVersionInformation,
                    # _In_opt_ LPVOID lpReserved,
                    # _In_opt_ LPARAM sortHandle
                    # );
                    LCMapStringEx = kernel32.LCMapStringEx
                    LCMapStringEx.restype = INT


                    # WINBASEAPI
                    # BOOL
                    # WINAPI
                    # IsValidLocaleName(
                    # _In_ LPCWSTR lpLocaleName
                    # );
                    IsValidLocaleName = kernel32.IsValidLocaleName
                    IsValidLocaleName.restype = BOOL
                # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

                if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM):
                    # BOOL (CALLBACK* CALINFO_ENUMPROCEXEX)(LPWSTR, CALID, LPWSTR, LPARAM);
                    CALINFO_ENUMPROCEXEX = CALLBACK(
                        BOOL,
                        LPWSTR,
                        CALID,
                        LPWSTR,
                        LPARAM,
                    )


                    # WINBASEAPI
                    # BOOL
                    # WINAPI
                    # EnumCalendarInfoExEx(
                    # _In_ CALINFO_ENUMPROCEXEX pCalInfoEnumProcExEx,
                    # _In_opt_ LPCWSTR lpLocaleName,
                    # _In_ CALID Calendar,
                    # _In_opt_ LPCWSTR lpReserved,
                    # _In_ CALTYPE CalType,
                    # _In_ LPARAM lParam
                    # );
                    EnumCalendarInfoExEx = kernel32.EnumCalendarInfoExEx
                    EnumCalendarInfoExEx.restype = BOOL

                    # BOOL (CALLBACK* DATEFMT_ENUMPROCEXEX)(LPWSTR, CALID, LPARAM);
                    DATEFMT_ENUMPROCEXEX = CALLBACK(
                        BOOL,
                        LPWSTR,
                        CALID,
                        LPARAM,
                    )


                    # WINBASEAPI
                    # BOOL
                    # WINAPI
                    # EnumDateFormatsExEx(
                    # _In_ DATEFMT_ENUMPROCEXEX lpDateFmtEnumProcExEx,
                    # _In_opt_ LPCWSTR lpLocaleName,
                    # _In_ DWORD dwFlags,
                    # _In_ LPARAM lParam
                    # );
                    EnumDateFormatsExEx = kernel32.EnumDateFormatsExEx
                    EnumDateFormatsExEx.restype = BOOL

                    # BOOL (CALLBACK* TIMEFMT_ENUMPROCEX)(LPWSTR, LPARAM);
                    TIMEFMT_ENUMPROCEX = CALLBACK(
                        BOOL,
                        LPWSTR,
                        LPARAM,
                    )


                    # WINBASEAPI
                    # BOOL
                    # WINAPI
                    # EnumTimeFormatsEx(
                    # _In_ TIMEFMT_ENUMPROCEX lpTimeFmtEnumProcEx,
                    # _In_opt_ LPCWSTR lpLocaleName,
                    # _In_ DWORD dwFlags,
                    # _In_ LPARAM lParam
                    # );
                    EnumTimeFormatsEx = kernel32.EnumTimeFormatsEx
                    EnumTimeFormatsEx.restype = BOOL

                    # BOOL (CALLBACK* LOCALE_ENUMPROCEX)(LPWSTR, DWORD, LPARAM);
                    LOCALE_ENUMPROCEX = CALLBACK(
                        BOOL,
                        LPWSTR,
                        DWORD,
                        LPARAM,
                    )


                    # WINBASEAPI
                    # BOOL
                    # WINAPI
                    # EnumSystemLocalesEx(
                    # _In_ LOCALE_ENUMPROCEX lpLocaleEnumProcEx,
                    # _In_ DWORD dwFlags,
                    # _In_ LPARAM lParam,
                    # _In_opt_ LPVOID lpReserved
                    # );
                    EnumSystemLocalesEx = kernel32.EnumSystemLocalesEx
                    EnumSystemLocalesEx.restype = BOOL
                # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP | WINAPI_PARTITION_SYSTEM)
            # END IF  (WINVER >= 0x0600)

            if WINVER >= _WIN32_WINNT_WIN7:
                if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
                    kernel32 = ctypes.windll.KERNEL32


                    # WINBASEAPI
                    # int
                    # WINAPI
                    # ResolveLocaleName(
                    # _In_opt_                        LPCWSTR lpNameToResolve,
                    # _Out_writes_opt_(cchLocaleName) LPWSTR  lpLocaleName,
                    # _In_                            INT     cchLocaleName
                    # );
                    ResolveLocaleName = kernel32.ResolveLocaleName
                    ResolveLocaleName.restype = INT

                # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)
            # END IF   (WINVER >= _WIN32_WINNT_WIN7)

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                pass
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
        # END IF   NONLS

        # Restore the original value of the 'DEPRECATED' macro");
        if _MSC_VER >= 1200:
            pass
        # END IF


        if defined(__cplusplus):
            pass
        # END IF

    # END IF   _WINNLS_


