
from guiddef_h import DEFINE_GUID


def STRING_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
    pass
    # return l##-##w1##-##w2##-##b1##b2##-##b3##b4##b5##b6##b7##b8


def GUID_BUILDER(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
    return DEFINE_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8)


from adogpool_h import * # NOQA

__all__ = (
    'STRING_GUID', 'GUID_BUILDER',
)
