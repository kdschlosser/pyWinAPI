

from wtypes_h import (
    UINT,
    CLSID,
)
import ctypes
import ntdef_h


from winapifamily_h import * # NOQA
CFSTR_VFW_FILTERLIST = "Video for Windows 4 Filters"

class tagVFW_FILTERLIST(ctypes.Structure):
    _fields_ = [
        ('cFilters', UINT),
        ('aClsId', CLSID * 1),
    ]


VFW_FILTERLIST = tagVFW_FILTERLIST



__all__ = (
    'CFSTR_VFW_FILTERLIST', 'VFW_FILTERLIST', 'tagVFW_FILTERLIST', 
)
