

import ntdef_h


from crtdefs_h import * # NOQA
from vadefs_h import * # NOQA
va_start = _crt_va_start
va_arg = _crt_va_arg
va_end = _crt_va_end

__all__ = (
    'va_arg', 'va_end', 'va_start', 
)
