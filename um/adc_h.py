

from wtypes_h import (
    ENUM,
    VOID
)
from guiddef_h import IID, GUID, CLSID
from winapifamily_h import * # NOQA
ADCDECLSPEC = VOID

CLSID_FoxRowset = CLSID(
    0x3ff292b6,
    0xb204,
    0x11cf,
    0x8d,
    0x23,
    0x00,
    0xaa,
    0x00,
    0x5f,
    0xfe,
    0x58
)
DBPROPSET_ADC = GUID(
    0xb68e3cc1,
    0x6deb,
    0x11d0,
    0x8d,
    0xf6,
    0x00,
    0xaa,
    0x00,
    0x5f,
    0xfe,
    0x58
)
IID_IAsyncAllowed = GUID(
    0xf5f2893a,
    0xba9e,
    0x11d0,
    0xab,
    0xb9,
    0x00,
    0xc0,
    0x4f,
    0xc2,
    0x9f,
    0x8f
)
IID_IRowsetADCExtensions = IID(
    0xF17324c4,
    0x68E0,
    0x11D0,
    0xAD,
    0x45,
    0x00,
    0xC0,
    0x4F,
    0xC2,
    0x98,
    0x63
)
IID_IUpdateInfo = IID(
    0xa0385420,
    0x62b8,
    0x11d1,
    0x9a,
    0x06,
    0x00,
    0xa0,
    0xc9,
    0x03,
    0xaa,
    0x45
)
IID_IRowsetSynchronize = IID(
    0x1be41e60,
    0x807a,
    0x11d1,
    0x9a,
    0x14,
    0x00,
    0xa0,
    0xc9,
    0x03,
    0xaa,
    0x45
)
IID_IRowsetProperties = IID(
    0x1e837070,
    0xbcfc,
    0x11d1,
    0x9a,
    0x2c,
    0x00,
    0xa0,
    0xc9,
    0x03,
    0xaa,
    0x45
)


class ADCPROPENUM(ENUM):
    DBPROP_ADC_ASYNCHFETCHSIZE = 3
    DBPROP_ADC_BATCHSIZE = 4
    DBPROP_ADC_UPDATECRITERIA = 5
    DBPROP_ADC_ASYNCHPREFETCHSIZE = 7
    DBPROP_ADC_ASYNCHTHREADPRIORITY = 8
    DBPROP_ADC_CACHECHILDROWS = 9
    DBPROP_ADC_MAINTAINCHANGESTATUS = 10
    DBPROP_ADC_AUTORECALC = 11
    DBPROP_ADC_UNIQUETABLE = 13
    DBPROP_ADC_UNIQUESCHEMA = 14
    DBPROP_ADC_UNIQUECATALOG = 15
    DBPROP_ADC_CUSTOMRESYNCH = 16
    DBPROP_ADC_CEVER = 17
    DBPROP_ADC_RESHAPENAME = 18
    DBPROP_ADC_UPDATERESYNC = 19
    DBPROP_ADC_BACKINGSTORE = 21
    DBPROP_ADC_RELEASESHAPEONDISCONNECT = 22


class ADCPROP_AUTORECALC_ENUM(ENUM):
    adRecalcUpFront = 0
    adRecalcAlways = 1


class FOXROWSETPROPENUM(ENUM):
    DBPROP_FOXTABLENAME = 0


__all__ = (
    'ADCDECLSPEC', '', 'ADCPROP_AUTORECALC_ENUM', 'FOXROWSETPROPENUM',
    'ADCPROPENUM', 'CLSID_FoxRowset', 'DBPROPSET_ADC', 'IID_IAsyncAllowed',
    'IID_IRowsetADCExtensions', 'IID_IUpdateInfo', 'IID_IRowsetSynchronize',
    'IID_IRowsetProperties'
)
