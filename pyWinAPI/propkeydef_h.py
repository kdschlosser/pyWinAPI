
from .wtypes_h import PROPERTYKEY
from .guiddef_h import GUID, IsEqualIID

PID_FIRST_USABLE = 0x2

REFPROPERTYKEY = PROPERTYKEY


def DEFINE_PROPERTYKEY(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8, pid):
    return PROPERTYKEY(
        GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8),
        pid
    )


def IsEqualPropertyKey(a, b):
    return (a.pid == b.pid) and IsEqualIID(a.fmtid, b.fmtid)

__all__ = (
    'REFPROPERTYKEY', 'DEFINE_PROPERTYKEY', 'IsEqualPropertyKey',
    'PID_FIRST_USABLE',
)
