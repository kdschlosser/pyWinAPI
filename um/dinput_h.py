import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

PASCAL = CALLBACK

def INTERFACE(name):
    return type(name, (comtypes.IUnknown,), {})


def STDMETHOD(name):

    def method_wrapper(restype=None, args=()):
        if restype is None:
            restype = HRESULT

        if isinstance(restype, tuple):
            args = restype
            restype = HRESULT

        argtypes = ()
        argnames = []

        for arg in args:
            if isinstance(arg, tuple):
                argtypes += (arg[0],)
                argnames += [arg[1]]
            else:
                argtypes += (arg,)

        res = comtypes.STDMETHOD(restype, name, argtypes)
        return argnames, res

    return method_wrapper


def DECLARE_INTERFACE_(cls, super_cls):
    if super_cls != comtypes.IUnknown:
        bases = super_cls.__bases__
        cls.__bases__ = (
            (super_cls,) +
            tuple(base for base in cls.__bases__ if base not in bases)
        )

    def wrapper(*args):
        argnames = list(arg[0] for arg in args)
        _methods_ = list(arg[1] for arg in args)

        method_names = list(itm[1] for itm in _methods_)

        for i, method_name in enumerate(method_names):
            defaults = argnames[i]

            class MethodWrapper(object):

                def __init__(self, parent, name, keywords):
                    self.__parent = parent
                    self.__name__ = name
                    self.__keywords = keywords

                def __call__(self, *args, **kwargs):
                    args = list(args)
                    for j, keyword in enumerate(self.__keywords):
                        if keyword in kwargs:
                            args.insert(j, kwargs.pop(keyword))

                    getattr(self.__parent, '__com_' + self.__name__)(*args)


            method = MethodWrapper(cls, method_name, defaults)
            setattr(cls, method_name, method)

        cls._methods_ = _methods_

    return wrapper


__DINPUT_INCLUDED__ = None
DIJ_RINGZERO = None
DIRECTINPUT_VERSION = None
D3DCOLOR_DEFINED = None
E_PENDING = None
_INC_MMSYSTEM = None
MMNOJOY = None
__VJOYDX_INCLUDED__ = None
_INC_MMDDK = None
MMNOJOYDEV = None
__VJOYDXD_INCLUDED__ = None

class DICONSTANTFORCE(ctypes.Structure):
    pass


LPDICONSTANTFORCE = POINTER(DICONSTANTFORCE)


class DIRAMPFORCE(ctypes.Structure):
    pass


LPDIRAMPFORCE = POINTER(DIRAMPFORCE)


class DIPERIODIC(ctypes.Structure):
    pass


LPDIPERIODIC = POINTER(DIPERIODIC)


class DICONDITION(ctypes.Structure):
    pass


LPDICONDITION = POINTER(DICONDITION)


class DICUSTOMFORCE(ctypes.Structure):
    pass


LPDICUSTOMFORCE = POINTER(DICUSTOMFORCE)


class DIENVELOPE(ctypes.Structure):
    pass


LPDIENVELOPE = POINTER(DIENVELOPE)


class DIEFFECT_DX5(ctypes.Structure):
    pass


LPDIEFFECT_DX5 = POINTER(DIEFFECT_DX5)


class DIEFFECT(ctypes.Structure):
    pass


LPDIEFFECT = POINTER(DIEFFECT)


class DIFILEEFFECT(ctypes.Structure):
    pass


LPDIFILEEFFECT = POINTER(DIFILEEFFECT)


class DIEFFESCAPE(ctypes.Structure):
    pass


LPDIEFFESCAPE = POINTER(DIEFFESCAPE)


class DIDEVCAPS_DX3(ctypes.Structure):
    pass


LPDIDEVCAPS_DX3 = POINTER(DIDEVCAPS_DX3)


class DIDEVCAPS(ctypes.Structure):
    pass


LPDIDEVCAPS = POINTER(DIDEVCAPS)


class _DIOBJECTDATAFORMAT(ctypes.Structure):
    pass


DIOBJECTDATAFORMAT = _DIOBJECTDATAFORMAT
LPDIOBJECTDATAFORMAT = POINTER(_DIOBJECTDATAFORMAT)


class _DIDATAFORMAT(ctypes.Structure):
    pass


DIDATAFORMAT = _DIDATAFORMAT
LPDIDATAFORMAT = POINTER(_DIDATAFORMAT)


class _DIACTIONA(ctypes.Structure):
    pass


DIACTIONA = _DIACTIONA
LPDIACTIONA = POINTER(_DIACTIONA)


class _DIACTIONW(ctypes.Structure):
    pass


DIACTIONW = _DIACTIONW
LPDIACTIONW = POINTER(_DIACTIONW)


class _DIACTIONFORMATA(ctypes.Structure):
    pass


DIACTIONFORMATA = _DIACTIONFORMATA
LPDIACTIONFORMATA = POINTER(_DIACTIONFORMATA)


class _DIACTIONFORMATW(ctypes.Structure):
    pass


DIACTIONFORMATW = _DIACTIONFORMATW
LPDIACTIONFORMATW = POINTER(_DIACTIONFORMATW)


class _DICOLORSET(ctypes.Structure):
    pass


DICOLORSET = _DICOLORSET
LPDICOLORSET = POINTER(_DICOLORSET)


class _DICONFIGUREDEVICESPARAMSA(ctypes.Structure):
    pass


DICONFIGUREDEVICESPARAMSA = _DICONFIGUREDEVICESPARAMSA
LPDICONFIGUREDEVICESPARAMSA = POINTER(_DICONFIGUREDEVICESPARAMSA)


class _DICONFIGUREDEVICESPARAMSW(ctypes.Structure):
    pass


DICONFIGUREDEVICESPARAMSW = _DICONFIGUREDEVICESPARAMSW
LPDICONFIGUREDEVICESPARAMSW = POINTER(_DICONFIGUREDEVICESPARAMSW)


class _DIDEVICEIMAGEINFOA(ctypes.Structure):
    pass


DIDEVICEIMAGEINFOA = _DIDEVICEIMAGEINFOA
LPDIDEVICEIMAGEINFOA = POINTER(_DIDEVICEIMAGEINFOA)


class _DIDEVICEIMAGEINFOW(ctypes.Structure):
    pass


DIDEVICEIMAGEINFOW = _DIDEVICEIMAGEINFOW
LPDIDEVICEIMAGEINFOW = POINTER(_DIDEVICEIMAGEINFOW)


class _DIDEVICEIMAGEINFOHEADERA(ctypes.Structure):
    pass


DIDEVICEIMAGEINFOHEADERA = _DIDEVICEIMAGEINFOHEADERA
LPDIDEVICEIMAGEINFOHEADERA = POINTER(_DIDEVICEIMAGEINFOHEADERA)


class _DIDEVICEIMAGEINFOHEADERW(ctypes.Structure):
    pass


DIDEVICEIMAGEINFOHEADERW = _DIDEVICEIMAGEINFOHEADERW
LPDIDEVICEIMAGEINFOHEADERW = POINTER(_DIDEVICEIMAGEINFOHEADERW)


class DIDEVICEOBJECTINSTANCE_DX3A(ctypes.Structure):
    pass


LPDIDEVICEOBJECTINSTANCE_DX3A = POINTER(DIDEVICEOBJECTINSTANCE_DX3A)


class DIDEVICEOBJECTINSTANCE_DX3W(ctypes.Structure):
    pass


LPDIDEVICEOBJECTINSTANCE_DX3W = POINTER(DIDEVICEOBJECTINSTANCE_DX3W)


class DIDEVICEOBJECTINSTANCEA(ctypes.Structure):
    pass


LPDIDEVICEOBJECTINSTANCEA = POINTER(DIDEVICEOBJECTINSTANCEA)


class DIDEVICEOBJECTINSTANCEW(ctypes.Structure):
    pass


LPDIDEVICEOBJECTINSTANCEW = POINTER(DIDEVICEOBJECTINSTANCEW)


class DIPROPHEADER(ctypes.Structure):
    pass


LPDIPROPHEADER = POINTER(DIPROPHEADER)


class DIPROPDWORD(ctypes.Structure):
    pass


LPDIPROPDWORD = POINTER(DIPROPDWORD)


class DIPROPPOINTER(ctypes.Structure):
    pass


LPDIPROPPOINTER = POINTER(DIPROPPOINTER)


class DIPROPRANGE(ctypes.Structure):
    pass


LPDIPROPRANGE = POINTER(DIPROPRANGE)


class DIPROPCAL(ctypes.Structure):
    pass


LPDIPROPCAL = POINTER(DIPROPCAL)


class DIPROPCALPOV(ctypes.Structure):
    pass


LPDIPROPCALPOV = POINTER(DIPROPCALPOV)


class DIPROPGUIDANDPATH(ctypes.Structure):
    pass


LPDIPROPGUIDANDPATH = POINTER(DIPROPGUIDANDPATH)


class DIPROPSTRING(ctypes.Structure):
    pass


LPDIPROPSTRING = POINTER(DIPROPSTRING)


class _CPOINT(ctypes.Structure):
    pass


CPOINT = _CPOINT
PCPOINT = POINTER(_CPOINT)


class DIPROPCPOINTS(ctypes.Structure):
    pass


LPDIPROPCPOINTS = POINTER(DIPROPCPOINTS)


class DIDEVICEOBJECTDATA_DX3(ctypes.Structure):
    pass


LPDIDEVICEOBJECTDATA_DX3 = POINTER(DIDEVICEOBJECTDATA_DX3)


class DIDEVICEOBJECTDATA(ctypes.Structure):
    pass


LPDIDEVICEOBJECTDATA = POINTER(DIDEVICEOBJECTDATA)


class DIDEVICEINSTANCE_DX3A(ctypes.Structure):
    pass


LPDIDEVICEINSTANCE_DX3A = POINTER(DIDEVICEINSTANCE_DX3A)


class DIDEVICEINSTANCE_DX3W(ctypes.Structure):
    pass


LPDIDEVICEINSTANCE_DX3W = POINTER(DIDEVICEINSTANCE_DX3W)


class DIDEVICEINSTANCEA(ctypes.Structure):
    pass


LPDIDEVICEINSTANCEA = POINTER(DIDEVICEINSTANCEA)


class DIDEVICEINSTANCEW(ctypes.Structure):
    pass


LPDIDEVICEINSTANCEW = POINTER(DIDEVICEINSTANCEW)


class DIEFFECTINFOA(ctypes.Structure):
    pass


LPDIEFFECTINFOA = POINTER(DIEFFECTINFOA)


class DIEFFECTINFOW(ctypes.Structure):
    pass


LPDIEFFECTINFOW = POINTER(DIEFFECTINFOW)


class _DIMOUSESTATE(ctypes.Structure):
    pass


DIMOUSESTATE = _DIMOUSESTATE
LPDIMOUSESTATE = POINTER(_DIMOUSESTATE)


class _DIMOUSESTATE2(ctypes.Structure):
    pass


DIMOUSESTATE2 = _DIMOUSESTATE2
LPDIMOUSESTATE2 = POINTER(_DIMOUSESTATE2)


class DIJOYSTATE(ctypes.Structure):
    pass


LPDIJOYSTATE = POINTER(DIJOYSTATE)


class DIJOYSTATE2(ctypes.Structure):
    pass


LPDIJOYSTATE2 = POINTER(DIJOYSTATE2)

# **************************************************************************
# Copyright (C) 1996-2002 Microsoft Corporation. All Rights Reserved. File:
# dinput.h Content: DirectInput include file
# *************************************************************************
if not defined(__DINPUT_INCLUDED__):
    __DINPUT_INCLUDED__ = VOID
    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if not defined(DIJ_RINGZERO):
        if defined(_WIN32):
            COM_NO_WINDOWS_H = VOID
            from pyWinAPI.um.objbase_h import * # NOQA
        # END IF
    # END IF  DIJ_RINGZERO

    if defined(__cplusplus):
        pass
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # /* To build applications for older versions of DirectInput define
        # DIRECTINPUT_VERSION [ 0x0300 | 0x0500 | 0x0700 ] before include
        # <dinput.h>. By default, include <dinput.h> will produce a DirectX
        # 8-compatible header file.

        DIRECTINPUT_HEADER_VERSION = 0x0800
        if not defined(DIRECTINPUT_VERSION):
            DIRECTINPUT_VERSION = DIRECTINPUT_HEADER_VERSION
        # END IF

        if not defined(DIJ_RINGZERO):
            # *****************************************************************
            # Class IDs
            # *****************************************************************

            CLSID_DirectInput = DEFINE_GUID(
                0x25E609E0,
                0xB259,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            CLSID_DirectInputDevice = DEFINE_GUID(
                0x25E609E1,
                0xB259,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            CLSID_DirectInput8 = DEFINE_GUID(
                0x25E609E4,
                0xB259,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            CLSID_DirectInputDevice8 = DEFINE_GUID(
                0x25E609E5,
                0xB259,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )

            # *****************************************************************
            # Interfaces
            # *****************************************************************

            IID_IDirectInputA = DEFINE_GUID(
                0x89521360,
                0xAA8A,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInputW = DEFINE_GUID(
                0x89521361,
                0xAA8A,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInput2A = DEFINE_GUID(
                0x5944E662,
                0xAA8A,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInput2W = DEFINE_GUID(
                0x5944E663,
                0xAA8A,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInput7A = DEFINE_GUID(
                0x9A4CB684,
                0x236D,
                0x11D3,
                0x8E,
                0x9D,
                0x00,
                0xC0,
                0x4F,
                0x68,
                0x44,
                0xAE
            )
            IID_IDirectInput7W = DEFINE_GUID(
                0x9A4CB685,
                0x236D,
                0x11D3,
                0x8E,
                0x9D,
                0x00,
                0xC0,
                0x4F,
                0x68,
                0x44,
                0xAE
            )
            IID_IDirectInput8A = DEFINE_GUID(
                0xBF798030,
                0x483A,
                0x4DA2,
                0xAA,
                0x99,
                0x5D,
                0x64,
                0xED,
                0x36,
                0x97,
                0x00
            )
            IID_IDirectInput8W = DEFINE_GUID(
                0xBF798031,
                0x483A,
                0x4DA2,
                0xAA,
                0x99,
                0x5D,
                0x64,
                0xED,
                0x36,
                0x97,
                0x00
            )
            IID_IDirectInputDeviceA = DEFINE_GUID(
                0x5944E680,
                0xC92E,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInputDeviceW = DEFINE_GUID(
                0x5944E681,
                0xC92E,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInputDevice2A = DEFINE_GUID(
                0x5944E682,
                0xC92E,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInputDevice2W = DEFINE_GUID(
                0x5944E683,
                0xC92E,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            IID_IDirectInputDevice7A = DEFINE_GUID(
                0x57D7C6BC,
                0x2356,
                0x11D3,
                0x8E,
                0x9D,
                0x00,
                0xC0,
                0x4F,
                0x68,
                0x44,
                0xAE
            )
            IID_IDirectInputDevice7W = DEFINE_GUID(
                0x57D7C6BD,
                0x2356,
                0x11D3,
                0x8E,
                0x9D,
                0x00,
                0xC0,
                0x4F,
                0x68,
                0x44,
                0xAE
            )
            IID_IDirectInputDevice8A = DEFINE_GUID(
                0x54D41080,
                0xDC15,
                0x4833,
                0xA4,
                0x1B,
                0x74,
                0x8F,
                0x73,
                0xA3,
                0x81,
                0x79
            )
            IID_IDirectInputDevice8W = DEFINE_GUID(
                0x54D41081,
                0xDC15,
                0x4833,
                0xA4,
                0x1B,
                0x74,
                0x8F,
                0x73,
                0xA3,
                0x81,
                0x79
            )
            IID_IDirectInputEffect = DEFINE_GUID(
                0xE7E1F7C0,
                0x88D2,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )

            # *****************************************************************
            # Predefined object types
            # *****************************************************************

            GUID_XAxis = DEFINE_GUID(
                0xA36D02E0,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_YAxis = DEFINE_GUID(
                0xA36D02E1,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_ZAxis = DEFINE_GUID(
                0xA36D02E2,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_RxAxis = DEFINE_GUID(
                0xA36D02F4,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_RyAxis = DEFINE_GUID(
                0xA36D02F5,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_RzAxis = DEFINE_GUID(
                0xA36D02E3,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_Slider = DEFINE_GUID(
                0xA36D02E4,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_Button = DEFINE_GUID(
                0xA36D02F0,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_Key = DEFINE_GUID(
                0x55728220,
                0xD33C,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_POV = DEFINE_GUID(
                0xA36D02F2,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_Unknown = DEFINE_GUID(
                0xA36D02F3,
                0xC9F3,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )

            # *****************************************************************
            # Predefined product GUIDs
            # *****************************************************************

            GUID_SysMouse = DEFINE_GUID(
                0x6F1D2B60,
                0xD5A0,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_SysKeyboard = DEFINE_GUID(
                0x6F1D2B61,
                0xD5A0,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_Joystick = DEFINE_GUID(
                0x6F1D2B70,
                0xD5A0,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_SysMouseEm = DEFINE_GUID(
                0x6F1D2B80,
                0xD5A0,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_SysMouseEm2 = DEFINE_GUID(
                0x6F1D2B81,
                0xD5A0,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_SysKeyboardEm = DEFINE_GUID(
                0x6F1D2B82,
                0xD5A0,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )
            GUID_SysKeyboardEm2 = DEFINE_GUID(
                0x6F1D2B83,
                0xD5A0,
                0x11CF,
                0xBF,
                0xC7,
                0x44,
                0x45,
                0x53,
                0x54,
                0x00,
                0x00
            )

            # *****************************************************************
            # Predefined force feedback effects
            # *****************************************************************

            GUID_ConstantForce = DEFINE_GUID(
                0x13541C20,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_RampForce = DEFINE_GUID(
                0x13541C21,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_Square = DEFINE_GUID(
                0x13541C22,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_Sine = DEFINE_GUID(
                0x13541C23,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_Triangle = DEFINE_GUID(
                0x13541C24,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_SawtoothUp = DEFINE_GUID(
                0x13541C25,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_SawtoothDown = DEFINE_GUID(
                0x13541C26,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_Spring = DEFINE_GUID(
                0x13541C27,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_Damper = DEFINE_GUID(
                0x13541C28,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_Inertia = DEFINE_GUID(
                0x13541C29,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_Friction = DEFINE_GUID(
                0x13541C2A,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
            GUID_CustomForce = DEFINE_GUID(
                0x13541C2B,
                0x8E33,
                0x11D0,
                0x9A,
                0xD0,
                0x00,
                0xA0,
                0xC9,
                0xA0,
                0x6E,
                0x35
            )
        # END IF  DIJ_RINGZERO

        # *********************************************************************
        # Interfaces and Structures...
        # *********************************************************************

        if DIRECTINPUT_VERSION >= 0x0500:
            # *****************************************************************
            # IDirectInputEffect
            # *****************************************************************

            DIEFT_ALL = 0x00000000
            DIEFT_CONSTANTFORCE = 0x00000001
            DIEFT_RAMPFORCE = 0x00000002
            DIEFT_PERIODIC = 0x00000003
            DIEFT_CONDITION = 0x00000004
            DIEFT_CUSTOMFORCE = 0x00000005
            DIEFT_HARDWARE = 0x000000FF
            DIEFT_FFATTACK = 0x00000200
            DIEFT_FFFADE = 0x00000400
            DIEFT_SATURATION = 0x00000800
            DIEFT_POSNEGCOEFFICIENTS = 0x00001000
            DIEFT_POSNEGSATURATION = 0x00002000
            DIEFT_DEADBAND = 0x00004000
            DIEFT_STARTDELAY = 0x00008000


            def DIEFT_GETTYPE(n):
                return LOBYTE(n)


            DI_DEGREES = 100
            DI_FFNOMINALMAX = 10000
            DI_SECONDS = 1000000


            DICONSTANTFORCE._fields_ = [
                ('lMagnitude', LONG),
            ]
            LPCDICONSTANTFORCE = POINTER(DICONSTANTFORCE)

            DIRAMPFORCE._fields_ = [
                ('lStart', LONG),
                ('lEnd', LONG),
            ]
            LPCDIRAMPFORCE = POINTER(DIRAMPFORCE)

            DIPERIODIC._fields_ = [
                ('dwMagnitude', DWORD),
                ('lOffset', LONG),
                ('dwPhase', DWORD),
                ('dwPeriod', DWORD),
            ]
            LPCDIPERIODIC = POINTER(DIPERIODIC)

            DICONDITION._fields_ = [
                ('lOffset', LONG),
                ('lPositiveCoefficient', LONG),
                ('lNegativeCoefficient', LONG),
                ('dwPositiveSaturation', DWORD),
                ('dwNegativeSaturation', DWORD),
                ('lDeadBand', LONG),
            ]
            LPCDICONDITION = POINTER(DICONDITION)

            DICUSTOMFORCE._fields_ = [
                ('cChannels', DWORD),
                ('dwSamplePeriod', DWORD),
                ('cSamples', DWORD),
                ('rglForceData', LPLONG),
            ]
            LPCDICUSTOMFORCE = POINTER(DICUSTOMFORCE)

            # (ctypes.sizeof(DIENVELOPE)
            DIENVELOPE._fields_ = [
                ('dwSize', DWORD),
                ('dwAttackLevel', DWORD),
                # Microseconds
                ('dwAttackTime', DWORD),
                ('dwFadeLevel', DWORD),
                # Microseconds
                ('dwFadeTime', DWORD),
            ]
            LPCDIENVELOPE = POINTER(DIENVELOPE)

            # This structure is defined for DirectX 5.0 compatibility
            DIEFFECT_DX5._fields_ = [
                # ctypes.sizeof(DIEFFECT_DX5)
                ('dwSize', DWORD),
                # DIEFF_*
                ('dwFlags', DWORD),
                # Microseconds
                ('dwDuration', DWORD),
                # Microseconds
                ('dwSamplePeriod', DWORD),
                ('dwGain', DWORD),
                # or DIEB_NOTRIGGER
                ('dwTriggerButton', DWORD),
                # Microseconds
                ('dwTriggerRepeatInterval', DWORD),
                # Number of axes
                ('cAxes', DWORD),
                # Array of axes
                ('rgdwAxes', LPDWORD),
                # Array of directions
                ('rglDirection', LPLONG),
                # Optional
                ('lpEnvelope', LPDIENVELOPE),
                # Size of params
                ('cbTypeSpecificParams', DWORD),
                # Pointer to params
                ('lpvTypeSpecificParams', LPVOID),
            ]
            LPCDIEFFECT_DX5 = POINTER(DIEFFECT_DX5)

            _TEMP_DIEFFECT = [
                # ctypes.sizeof(DIEFFECT)
                ('dwSize', DWORD),
                # DIEFF_*
                ('dwFlags', DWORD),
                # Microseconds
                ('dwDuration', DWORD),
                # Microseconds
                ('dwSamplePeriod', DWORD),
                ('dwGain', DWORD),
                # or DIEB_NOTRIGGER
                ('dwTriggerButton', DWORD),
                # Microseconds
                ('dwTriggerRepeatInterval', DWORD),
                # Number of axes
                ('cAxes', DWORD),
                # Array of axes
                ('rgdwAxes', LPDWORD),
                # Array of directions
                ('rglDirection', LPLONG),
                # Optional
                ('lpEnvelope', LPDIENVELOPE),
                # Size of params
                ('cbTypeSpecificParams', DWORD),
                # Pointer to params
                ('lpvTypeSpecificParams', LPVOID),
            ]
            if DIRECTINPUT_VERSION >= 0x0600:
                _TEMP_DIEFFECT += [
                    # Microseconds
                    ('dwStartDelay', DWORD),
                ]
            # END IF   DIRECTINPUT_VERSION >= 0x0600


            DIEFFECT._fields_ = _TEMP_DIEFFECT
            DIEFFECT_DX6 = DIEFFECT
            LPDIEFFECT_DX6 = LPDIEFFECT
            LPCDIEFFECT = POINTER(DIEFFECT)

            if DIRECTINPUT_VERSION >= 0x0700:
                if not defined(DIJ_RINGZERO):
                    DIFILEEFFECT._fields_ = [
                        ('dwSize', DWORD),
                        ('GuidEffect', GUID),
                        ('lpDiEffect', LPCDIEFFECT),
                        ('szFriendlyName', CHAR * MAX_PATH),
                    ]
                    LPCDIFILEEFFECT = POINTER(DIFILEEFFECT)

                    # typedef BOOL (FAR PASCAL * LPDIENUMEFFECTSINFILECALLBACK)(LPCDIFILEEFFECT , LPVOID);
                    LPDIENUMEFFECTSINFILECALLBACK = PASCAL(
                        BOOL,
                        LPCDIFILEEFFECT,
                        LPVOID
                    )
                # END IF  DIJ_RINGZERO
            # END IF  DIRECTINPUT_VERSION >= 0x0700

            DIEFF_OBJECTIDS = 0x00000001
            DIEFF_OBJECTOFFSETS = 0x00000002
            DIEFF_CARTESIAN = 0x00000010
            DIEFF_POLAR = 0x00000020
            DIEFF_SPHERICAL = 0x00000040
            DIEP_DURATION = 0x00000001
            DIEP_SAMPLEPERIOD = 0x00000002
            DIEP_GAIN = 0x00000004
            DIEP_TRIGGERBUTTON = 0x00000008
            DIEP_TRIGGERREPEATINTERVAL = 0x00000010
            DIEP_AXES = 0x00000020
            DIEP_DIRECTION = 0x00000040
            DIEP_ENVELOPE = 0x00000080
            DIEP_TYPESPECIFICPARAMS = 0x00000100

            if DIRECTINPUT_VERSION >= 0x0600:
                DIEP_STARTDELAY = 0x00000200
                DIEP_ALLPARAMS_DX5 = 0x000001FF
                DIEP_ALLPARAMS = 0x000003FF
            else:
                DIEP_ALLPARAMS = 0x000001FF
            # END IF  DIRECTINPUT_VERSION < 0x0600

            DIEP_START = 0x20000000
            DIEP_NORESTART = 0x40000000
            DIEP_NODOWNLOAD = 0x80000000
            DIEB_NOTRIGGER = 0xFFFFFFFF
            DIES_SOLO = 0x00000001
            DIES_NODOWNLOAD = 0x80000000
            DIEGES_PLAYING = 0x00000001
            DIEGES_EMULATED = 0x00000002

            DIEFFESCAPE._fields_ = [
                ('dwSize', DWORD),
                ('dwCommand', DWORD),
                ('lpvInBuffer', LPVOID),
                ('cbInBuffer', DWORD),
                ('lpvOutBuffer', LPVOID),
                ('cbOutBuffer', DWORD),
            ]

            if not defined(DIJ_RINGZERO):
                IDirectInputEffect = INTERFACE('IDirectInputEffect')
                IDirectInputEffect._iid_ = IID_IDirectInputEffect
                DECLARE_INTERFACE_(IDirectInputEffect, comtypes.IUnknown)(
                    # * IUnknown methods *
                    # * IDirectInputEffect methods

                    STDMETHOD('Initialize')((HINSTANCE, DWORD, REFGUID)),
                    STDMETHOD('GetEffectGuid')((LPGUID,)),
                    STDMETHOD('GetParameters')((LPDIEFFECT, DWORD)),
                    STDMETHOD('SetParameters')((LPCDIEFFECT, DWORD)),
                    STDMETHOD('Start')((DWORD, DWORD)),
                    STDMETHOD('Stop')(),
                    STDMETHOD('GetEffectStatus')((LPDWORD,)),
                    STDMETHOD('Download')(),
                    STDMETHOD('Unload')(),
                    STDMETHOD('Escape')((LPDIEFFESCAPE,)),
                )

                LPDIRECTINPUTEFFECT = POINTER(IDirectInputEffect)

                if not defined(__cplusplus) or defined(CINTERFACE):
                    def IDirectInputEffect_QueryInterface(p, a, b):
                        return p.lpVtbl.QueryInterface(p, a, b)


                    def IDirectInputEffect_AddRef(p):
                        return p.lpVtbl.AddRef(p)


                    def IDirectInputEffect_Release(p):
                        return p.lpVtbl.Release(p)


                    def IDirectInputEffect_Initialize(p, a, b, c):
                        return p.lpVtbl.Initialize(p, a, b, c)


                    def IDirectInputEffect_GetEffectGuid(p, a):
                        return p.lpVtbl.GetEffectGuid(p, a)


                    def IDirectInputEffect_GetParameters(p, a, b):
                        return p.lpVtbl.GetParameters(p, a, b)


                    def IDirectInputEffect_SetParameters(p, a, b):
                        return p.lpVtbl.SetParameters(p, a, b)


                    def IDirectInputEffect_Start(p, a, b):
                        return p.lpVtbl.Start(p, a, b)


                    def IDirectInputEffect_Stop(p):
                        return p.lpVtbl.Stop(p)


                    def IDirectInputEffect_GetEffectStatus(p, a):
                        return p.lpVtbl.GetEffectStatus(p, a)


                    def IDirectInputEffect_Download(p):
                        return p.lpVtbl.Download(p)


                    def IDirectInputEffect_Unload(p):
                        return p.lpVtbl.Unload(p)


                    def IDirectInputEffect_Escape(p, a):
                        return p.lpVtbl.Escape(p, a)
                else:
                    def IDirectInputEffect_QueryInterface(p, a, b):
                        return p.QueryInterface(a, b)


                    def IDirectInputEffect_AddRef(p):
                        return p.AddRef()


                    def IDirectInputEffect_Release(p):
                        return p.Release()


                    def IDirectInputEffect_Initialize(p, a, b, c):
                        return p.Initialize(a, b, c)


                    def IDirectInputEffect_GetEffectGuid(p, a):
                        return p.GetEffectGuid(a)


                    def IDirectInputEffect_GetParameters(p, a, b):
                        return p.GetParameters(a, b)


                    def IDirectInputEffect_SetParameters(p, a, b):
                        return p.SetParameters(a, b)


                    def IDirectInputEffect_Start(p, a, b):
                        return p.Start(a, b)


                    def IDirectInputEffect_Stop(p):
                        return p.Stop()


                    def IDirectInputEffect_GetEffectStatus(p, a):
                        return p.GetEffectStatus(a)


                    def IDirectInputEffect_Download(p):
                        return p.Download()


                    def IDirectInputEffect_Unload(p):
                        return p.Unload()


                    def IDirectInputEffect_Escape(p, a):
                        return p.Escape(a)
                # END IF
            # END IF  DIJ_RINGZERO
        # END IF  DIRECTINPUT_VERSION >= 0x0500

        # *********************************************************************
        # IDirectInputDevice
        # *********************************************************************

        if DIRECTINPUT_VERSION <= 0x700:
            DIDEVTYPE_DEVICE = 1
            DIDEVTYPE_MOUSE = 2
            DIDEVTYPE_KEYBOARD = 3
            DIDEVTYPE_JOYSTICK = 4
        else:
            DI8DEVCLASS_ALL = 0
            DI8DEVCLASS_DEVICE = 1
            DI8DEVCLASS_POINTER = 2
            DI8DEVCLASS_KEYBOARD = 3
            DI8DEVCLASS_GAMECTRL = 4
            DI8DEVTYPE_DEVICE = 0x11
            DI8DEVTYPE_MOUSE = 0x12
            DI8DEVTYPE_KEYBOARD = 0x13
            DI8DEVTYPE_JOYSTICK = 0x14
            DI8DEVTYPE_GAMEPAD = 0x15
            DI8DEVTYPE_DRIVING = 0x16
            DI8DEVTYPE_FLIGHT = 0x17
            DI8DEVTYPE_1STPERSON = 0x18
            DI8DEVTYPE_DEVICECTRL = 0x19
            DI8DEVTYPE_SCREENPOINTER = 0x1A
            DI8DEVTYPE_REMOTE = 0x1B
            DI8DEVTYPE_SUPPLEMENTAL = 0x1C
        # END IF  DIRECTINPUT_VERSION <= 0x700

        DIDEVTYPE_HID = 0x00010000

        if DIRECTINPUT_VERSION <= 0x700:
            DIDEVTYPEMOUSE_UNKNOWN = 1
            DIDEVTYPEMOUSE_TRADITIONAL = 2
            DIDEVTYPEMOUSE_FINGERSTICK = 3
            DIDEVTYPEMOUSE_TOUCHPAD = 4
            DIDEVTYPEMOUSE_TRACKBALL = 5
            DIDEVTYPEKEYBOARD_UNKNOWN = 0
            DIDEVTYPEKEYBOARD_PCXT = 1
            DIDEVTYPEKEYBOARD_OLIVETTI = 2
            DIDEVTYPEKEYBOARD_PCAT = 3
            DIDEVTYPEKEYBOARD_PCENH = 4
            DIDEVTYPEKEYBOARD_NOKIA1050 = 5
            DIDEVTYPEKEYBOARD_NOKIA9140 = 6
            DIDEVTYPEKEYBOARD_NEC98 = 7
            DIDEVTYPEKEYBOARD_NEC98LAPTOP = 8
            DIDEVTYPEKEYBOARD_NEC98106 = 9
            DIDEVTYPEKEYBOARD_JAPAN106 = 10
            DIDEVTYPEKEYBOARD_JAPANAX = 11
            DIDEVTYPEKEYBOARD_J3100 = 12
            DIDEVTYPEJOYSTICK_UNKNOWN = 1
            DIDEVTYPEJOYSTICK_TRADITIONAL = 2
            DIDEVTYPEJOYSTICK_FLIGHTSTICK = 3
            DIDEVTYPEJOYSTICK_GAMEPAD = 4
            DIDEVTYPEJOYSTICK_RUDDER = 5
            DIDEVTYPEJOYSTICK_WHEEL = 6
            DIDEVTYPEJOYSTICK_HEADTRACKER = 7
        else:
            DI8DEVTYPEMOUSE_UNKNOWN = 1
            DI8DEVTYPEMOUSE_TRADITIONAL = 2
            DI8DEVTYPEMOUSE_FINGERSTICK = 3
            DI8DEVTYPEMOUSE_TOUCHPAD = 4
            DI8DEVTYPEMOUSE_TRACKBALL = 5
            DI8DEVTYPEMOUSE_ABSOLUTE = 6
            DI8DEVTYPEKEYBOARD_UNKNOWN = 0
            DI8DEVTYPEKEYBOARD_PCXT = 1
            DI8DEVTYPEKEYBOARD_OLIVETTI = 2
            DI8DEVTYPEKEYBOARD_PCAT = 3
            DI8DEVTYPEKEYBOARD_PCENH = 4
            DI8DEVTYPEKEYBOARD_NOKIA1050 = 5
            DI8DEVTYPEKEYBOARD_NOKIA9140 = 6
            DI8DEVTYPEKEYBOARD_NEC98 = 7
            DI8DEVTYPEKEYBOARD_NEC98LAPTOP = 8
            DI8DEVTYPEKEYBOARD_NEC98106 = 9
            DI8DEVTYPEKEYBOARD_JAPAN106 = 10
            DI8DEVTYPEKEYBOARD_JAPANAX = 11
            DI8DEVTYPEKEYBOARD_J3100 = 12
            DI8DEVTYPE_LIMITEDGAMESUBTYPE = 1
            DI8DEVTYPEJOYSTICK_LIMITED = DI8DEVTYPE_LIMITEDGAMESUBTYPE
            DI8DEVTYPEJOYSTICK_STANDARD = 2
            DI8DEVTYPEGAMEPAD_LIMITED = DI8DEVTYPE_LIMITEDGAMESUBTYPE
            DI8DEVTYPEGAMEPAD_STANDARD = 2
            DI8DEVTYPEGAMEPAD_TILT = 3
            DI8DEVTYPEDRIVING_LIMITED = DI8DEVTYPE_LIMITEDGAMESUBTYPE
            DI8DEVTYPEDRIVING_COMBINEDPEDALS = 2
            DI8DEVTYPEDRIVING_DUALPEDALS = 3
            DI8DEVTYPEDRIVING_THREEPEDALS = 4
            DI8DEVTYPEDRIVING_HANDHELD = 5
            DI8DEVTYPEFLIGHT_LIMITED = DI8DEVTYPE_LIMITEDGAMESUBTYPE
            DI8DEVTYPEFLIGHT_STICK = 2
            DI8DEVTYPEFLIGHT_YOKE = 3
            DI8DEVTYPEFLIGHT_RC = 4
            DI8DEVTYPE1STPERSON_LIMITED = DI8DEVTYPE_LIMITEDGAMESUBTYPE
            DI8DEVTYPE1STPERSON_UNKNOWN = 2
            DI8DEVTYPE1STPERSON_SIXDOF = 3
            DI8DEVTYPE1STPERSON_SHOOTER = 4
            DI8DEVTYPESCREENPTR_UNKNOWN = 2
            DI8DEVTYPESCREENPTR_LIGHTGUN = 3
            DI8DEVTYPESCREENPTR_LIGHTPEN = 4
            DI8DEVTYPESCREENPTR_TOUCH = 5
            DI8DEVTYPEREMOTE_UNKNOWN = 2
            DI8DEVTYPEDEVICECTRL_UNKNOWN = 2
            DI8DEVTYPEDEVICECTRL_COMMSSELECTION = 3
            DI8DEVTYPEDEVICECTRL_COMMSSELECTION_HARDWIRED = 4
            DI8DEVTYPESUPPLEMENTAL_UNKNOWN = 2
            DI8DEVTYPESUPPLEMENTAL_2NDHANDCONTROLLER = 3
            DI8DEVTYPESUPPLEMENTAL_HEADTRACKER = 4
            DI8DEVTYPESUPPLEMENTAL_HANDTRACKER = 5
            DI8DEVTYPESUPPLEMENTAL_SHIFTSTICKGATE = 6
            DI8DEVTYPESUPPLEMENTAL_SHIFTER = 7
            DI8DEVTYPESUPPLEMENTAL_THROTTLE = 8
            DI8DEVTYPESUPPLEMENTAL_SPLITTHROTTLE = 9
            DI8DEVTYPESUPPLEMENTAL_COMBINEDPEDALS = 10
            DI8DEVTYPESUPPLEMENTAL_DUALPEDALS = 11
            DI8DEVTYPESUPPLEMENTAL_THREEPEDALS = 12
            DI8DEVTYPESUPPLEMENTAL_RUDDERPEDALS = 13
        # END IF  DIRECTINPUT_VERSION <= 0x700


        def GET_DIDEVICE_TYPE(dwDevType):
            return LOBYTE(dwDevType)


        def GET_DIDEVICE_SUBTYPE(dwDevType):
            return HIBYTE(dwDevType)


        if DIRECTINPUT_VERSION >= 0x0500:
            # This structure is defined for DirectX 3.0 compatibility
            DIDEVCAPS_DX3._fields_ = [
                ('dwSize', DWORD),
                ('dwFlags', DWORD),
                ('dwDevType', DWORD),
                ('dwAxes', DWORD),
                ('dwButtons', DWORD),
                ('dwPOVs', DWORD),
            ]
        # END IF  DIRECTINPUT_VERSION >= 0x0500


        _TEMP_DIDEVCAPS = [
            ('dwSize', DWORD),
            ('dwFlags', DWORD),
            ('dwDevType', DWORD),
            ('dwAxes', DWORD),
            ('dwButtons', DWORD),
            ('dwPOVs', DWORD),
        ]

        if DIRECTINPUT_VERSION >= 0x0500:
            _TEMP_DIDEVCAPS += [
                ('dwFFSamplePeriod', DWORD),
                ('dwFFMinTimeResolution', DWORD),
                ('dwFirmwareRevision', DWORD),
                ('dwHardwareRevision', DWORD),
                ('dwFFDriverVersion', DWORD),
            ]
            # END IF   DIRECTINPUT_VERSION >= 0x0500


        DIDEVCAPS._fields_ = _TEMP_DIDEVCAPS

        DIDC_ATTACHED = 0x00000001
        DIDC_POLLEDDEVICE = 0x00000002
        DIDC_EMULATED = 0x00000004
        DIDC_POLLEDDATAFORMAT = 0x00000008

        if DIRECTINPUT_VERSION >= 0x0500:
            DIDC_FORCEFEEDBACK = 0x00000100
            DIDC_FFATTACK = 0x00000200
            DIDC_FFFADE = 0x00000400
            DIDC_SATURATION = 0x00000800
            DIDC_POSNEGCOEFFICIENTS = 0x00001000
            DIDC_POSNEGSATURATION = 0x00002000
            DIDC_DEADBAND = 0x00004000
        # END IF  DIRECTINPUT_VERSION >= 0x0500

        DIDC_STARTDELAY = 0x00008000
        if DIRECTINPUT_VERSION >= 0x050a:
            DIDC_ALIAS = 0x00010000
            DIDC_PHANTOM = 0x00020000
        # END IF  DIRECTINPUT_VERSION >= 0x050a

        if DIRECTINPUT_VERSION >= 0x0800:
            DIDC_HIDDEN = 0x00040000
        # END IF  DIRECTINPUT_VERSION >= 0x0800

        DIDFT_ALL = 0x00000000
        DIDFT_RELAXIS = 0x00000001
        DIDFT_ABSAXIS = 0x00000002
        DIDFT_AXIS = 0x00000003
        DIDFT_PSHBUTTON = 0x00000004
        DIDFT_TGLBUTTON = 0x00000008
        DIDFT_BUTTON = 0x0000000C
        DIDFT_POV = 0x00000010
        DIDFT_COLLECTION = 0x00000040
        DIDFT_NODATA = 0x00000080
        DIDFT_ANYINSTANCE = 0x00FFFF00
        DIDFT_INSTANCEMASK = DIDFT_ANYINSTANCE


        def DIDFT_MAKEINSTANCE(n):
            return n << 8


        def DIDFT_GETTYPE(n):
            return LOBYTE(n)


        def DIDFT_GETINSTANCE(n):
            return LOWORD(n >> 8)


        DIDFT_FFACTUATOR = 0x01000000
        DIDFT_FFEFFECTTRIGGER = 0x02000000

        if DIRECTINPUT_VERSION >= 0x050a:
            DIDFT_OUTPUT = 0x10000000
            DIDFT_VENDORDEFINED = 0x04000000
            DIDFT_ALIAS = 0x08000000
        # END IF  DIRECTINPUT_VERSION >= 0x050a


        def DIDFT_ENUMCOLLECTION(n):
            return n << 8


        DIDFT_NOCOLLECTION = 0x00FFFF00

        if not defined(DIJ_RINGZERO):
            _DIOBJECTDATAFORMAT._fields_ = [
                ('pguid', POINTER(GUID)),
                ('dwOfs', DWORD),
                ('dwType', DWORD),
                ('dwFlags', DWORD),
            ]
            LPCDIOBJECTDATAFORMAT = POINTER(DIOBJECTDATAFORMAT)

            _DIDATAFORMAT._fields_ = [
                ('dwSize', DWORD),
                ('dwObjSize', DWORD),
                ('dwFlags', DWORD),
                ('dwDataSize', DWORD),
                ('dwNumObjs', DWORD),
                ('rgodf', LPDIOBJECTDATAFORMAT),
            ]
            LPCDIDATAFORMAT = POINTER(DIDATAFORMAT)
            DIDF_ABSAXIS = 0x00000001
            DIDF_RELAXIS = 0x00000002

            if defined(__cplusplus):
                pass
            # END IF


            if DIRECTINPUT_VERSION >= 0x0700:
                c_dfDIMouse2 = DIDATAFORMAT
            # END IF  DIRECTINPUT_VERSION >= 0x0700

            c_dfDIKeyboard = DIDATAFORMAT

            if DIRECTINPUT_VERSION >= 0x0500:
                c_dfDIJoystick = DIDATAFORMAT
                c_dfDIJoystick2 = DIDATAFORMAT
            # END IF  DIRECTINPUT_VERSION >= 0x0500

            if defined(__cplusplus):
                pass
            # END IF

            if DIRECTINPUT_VERSION > 0x0700:

                class Union_1(ctypes.Union):
                    pass

                Union_1._fields_ = [
                    ('lptszActionName', LPCSTR),
                    ('uResIdString', UINT)
                ]

                _DIACTIONA._Union_1 = Union_1
                _DIACTIONA._anonymouse_ = ('Union_1',)

                _DIACTIONA._fields_ = [
                    ('uAppData', UINT_PTR),
                    ('dwSemantic', DWORD),
                    ('dwFlags', DWORD),
                    ('Union_1', _DIACTIONA._Union_1),
                    ('guidInstance', GUID),
                    ('dwObjID', DWORD),
                    ('dwHow', DWORD),
                ]


                class Union_2(ctypes.Union):
                    pass


                Union_2._fields_ = [
                    ('lptszActionName', LPCWSTR),
                    ('uResIdString', UINT)
                ]

                _DIACTIONW._Union_2 = Union_2
                _DIACTIONW._anonymouse_ = ('Union_2',)

                _DIACTIONW._fields_ = [
                    ('uAppData', UINT_PTR),
                    ('dwSemantic', DWORD),
                    ('dwFlags', DWORD),
                    ('Union_2', _DIACTIONW._Union_2),
                    ('guidInstance', GUID),
                    ('dwObjID', DWORD),
                    ('dwHow', DWORD),
                ]

                if defined(UNICODE):
                    DIACTION = DIACTIONW
                    LPDIACTION = LPDIACTIONW
                else:
                    DIACTION = DIACTIONA
                    LPDIACTION = LPDIACTIONA
                # END IF   UNICODE

                LPCDIACTIONA = POINTER(DIACTIONA)
                LPCDIACTIONW = POINTER(DIACTIONW)

                if defined(UNICODE):
                    DIACTION = DIACTIONW
                    LPCDIACTION = LPCDIACTIONW
                else:
                    DIACTION = DIACTIONA
                    LPCDIACTION = LPCDIACTIONA
                # END IF   UNICODE

                LPCDIACTION = POINTER(DIACTION)
                DIA_FORCEFEEDBACK = 0x00000001
                DIA_APPMAPPED = 0x00000002
                DIA_APPNOMAP = 0x00000004
                DIA_NORANGE = 0x00000008
                DIA_APPFIXED = 0x00000010
                DIAH_UNMAPPED = 0x00000000
                DIAH_USERCONFIG = 0x00000001
                DIAH_APPREQUESTED = 0x00000002
                DIAH_HWAPP = 0x00000004
                DIAH_HWDEFAULT = 0x00000008
                DIAH_DEFAULT = 0x00000020
                DIAH_ERROR = 0x80000000


                _DIACTIONFORMATA._fields_ = [
                    ('dwSize', DWORD),
                    ('dwActionSize', DWORD),
                    ('dwDataSize', DWORD),
                    ('dwNumActions', DWORD),
                    ('rgoAction', LPDIACTIONA),
                    ('guidActionMap', GUID),
                    ('dwGenre', DWORD),
                    ('dwBufferSize', DWORD),
                    ('lAxisMin', LONG),
                    ('lAxisMax', LONG),
                    ('hInstString', HINSTANCE),
                    ('ftTimeStamp', FILETIME),
                    ('dwCRC', DWORD),
                    ('tszActionMap', CHAR * MAX_PATH),
                ]

                _DIACTIONFORMATW._fields_ = [
                    ('dwSize', DWORD),
                    ('dwActionSize', DWORD),
                    ('dwDataSize', DWORD),
                    ('dwNumActions', DWORD),
                    ('rgoAction', LPDIACTIONW),
                    ('guidActionMap', GUID),
                    ('dwGenre', DWORD),
                    ('dwBufferSize', DWORD),
                    ('lAxisMin', LONG),
                    ('lAxisMax', LONG),
                    ('hInstString', HINSTANCE),
                    ('ftTimeStamp', FILETIME),
                    ('dwCRC', DWORD),
                    ('tszActionMap', WCHAR * MAX_PATH),
                ]
                if defined(UNICODE):
                    DIACTIONFORMAT = DIACTIONFORMATW
                    LPDIACTIONFORMAT = LPDIACTIONFORMATW
                else:
                    DIACTIONFORMAT = DIACTIONFORMATA
                    LPDIACTIONFORMAT = LPDIACTIONFORMATA
                # END IF   UNICODE

                LPCDIACTIONFORMATA = POINTER(DIACTIONFORMATA)
                LPCDIACTIONFORMATW = POINTER(DIACTIONFORMATW)
                if defined(UNICODE):
                    DIACTIONFORMAT = DIACTIONFORMATW
                    LPCDIACTIONFORMAT = LPCDIACTIONFORMATW
                else:
                    DIACTIONFORMAT = DIACTIONFORMATA
                    LPCDIACTIONFORMAT = LPCDIACTIONFORMATA
                # END IF   UNICODE

                LPCDIACTIONFORMAT = POINTER(DIACTIONFORMAT)
                DIAFTS_NEWDEVICELOW = 0xFFFFFFFF
                DIAFTS_NEWDEVICEHIGH = 0xFFFFFFFF
                DIAFTS_UNUSEDDEVICELOW = 0x00000000
                DIAFTS_UNUSEDDEVICEHIGH = 0x00000000
                DIDBAM_DEFAULT = 0x00000000
                DIDBAM_PRESERVE = 0x00000001
                DIDBAM_INITIALIZE = 0x00000002
                DIDBAM_HWDEFAULTS = 0x00000004
                DIDSAM_DEFAULT = 0x00000000
                DIDSAM_NOUSER = 0x00000001
                DIDSAM_FORCESAVE = 0x00000002
                DICD_DEFAULT = 0x00000000
                DICD_EDIT = 0x00000001

                # /* The following definition is normally defined in d3dtypes.h
                if not defined(D3DCOLOR_DEFINED):
                    D3DCOLOR = DWORD
                    D3DCOLOR_DEFINED = VOID
                # END IF


                _DICOLORSET._fields_ = [
                    ('dwSize', DWORD),
                    ('cTextFore', D3DCOLOR),
                    ('cTextHighlight', D3DCOLOR),
                    ('cCalloutLine', D3DCOLOR),
                    ('cCalloutHighlight', D3DCOLOR),
                    ('cBorder', D3DCOLOR),
                    ('cControlFill', D3DCOLOR),
                    ('cHighlightFill', D3DCOLOR),
                    ('cAreaFill', D3DCOLOR),
                ]
                LPCDICOLORSET = POINTER(DICOLORSET)

                _DICONFIGUREDEVICESPARAMSA._fields_ = [
                    ('dwSize', DWORD),
                    ('dwcUsers', DWORD),
                    ('lptszUserNames', LPSTR),
                    ('dwcFormats', DWORD),
                    ('lprgFormats', LPDIACTIONFORMATA),
                    ('hwnd', HWND),
                    ('dics', DICOLORSET),
                    ('lpUnkDDSTarget', POINTER(comtypes.IUnknown)),
                ]

                _DICONFIGUREDEVICESPARAMSW._fields_ = [
                    ('dwSize', DWORD),
                    ('dwcUsers', DWORD),
                    ('lptszUserNames', LPWSTR),
                    ('dwcFormats', DWORD),
                    ('lprgFormats', LPDIACTIONFORMATW),
                    ('hwnd', HWND),
                    ('dics', DICOLORSET),
                    ('lpUnkDDSTarget', POINTER(comtypes.IUnknown)),
                ]
                if defined(UNICODE):
                    DICONFIGUREDEVICESPARAMS = DICONFIGUREDEVICESPARAMSW
                    LPDICONFIGUREDEVICESPARAMS = LPDICONFIGUREDEVICESPARAMSW
                else:
                    DICONFIGUREDEVICESPARAMS = DICONFIGUREDEVICESPARAMSA
                    LPDICONFIGUREDEVICESPARAMS = LPDICONFIGUREDEVICESPARAMSA
                # END IF   UNICODE

                LPCDICONFIGUREDEVICESPARAMSA = POINTER(DICONFIGUREDEVICESPARAMSA)
                LPCDICONFIGUREDEVICESPARAMSW = POINTER(DICONFIGUREDEVICESPARAMSW)
                if defined(UNICODE):
                    DICONFIGUREDEVICESPARAMS = DICONFIGUREDEVICESPARAMSW
                    LPCDICONFIGUREDEVICESPARAMS = LPCDICONFIGUREDEVICESPARAMSW
                else:
                    DICONFIGUREDEVICESPARAMS = DICONFIGUREDEVICESPARAMSA
                    LPCDICONFIGUREDEVICESPARAMS = LPCDICONFIGUREDEVICESPARAMSA
                # END IF   UNICODE

                LPCDICONFIGUREDEVICESPARAMS = POINTER(DICONFIGUREDEVICESPARAMS)
                DIDIFT_CONFIGURATION = 0x00000001
                DIDIFT_OVERLAY = 0x00000002
                DIDAL_CENTERED = 0x00000000
                DIDAL_LEFTALIGNED = 0x00000001
                DIDAL_RIGHTALIGNED = 0x00000002
                DIDAL_MIDDLE = 0x00000000
                DIDAL_TOPALIGNED = 0x00000004
                DIDAL_BOTTOMALIGNED = 0x00000008

                _DIDEVICEIMAGEINFOA._fields_ = [
                    ('tszImagePath', CHAR * MAX_PATH),
                    ('dwFlags', DWORD),
                    # These are valid if DIDIFT_OVERLAY is present in dwFlags.
                    ('dwViewID', DWORD),
                    ('rcOverlay', RECT),
                    ('dwObjID', DWORD),
                    ('dwcValidPts', DWORD),
                    ('rgptCalloutLine', POINT * 5),
                    ('rcCalloutRect', RECT),
                    ('dwTextAlign', DWORD),
                ]

                _DIDEVICEIMAGEINFOW._fields_ = [
                    ('tszImagePath', WCHAR * MAX_PATH),
                    ('dwFlags', DWORD),
                    # These are valid if DIDIFT_OVERLAY is present in dwFlags.
                    ('dwViewID', DWORD),
                    ('rcOverlay', RECT),
                    ('dwObjID', DWORD),
                    ('dwcValidPts', DWORD),
                    ('rgptCalloutLine', POINT * 5),
                    ('rcCalloutRect', RECT),
                    ('dwTextAlign', DWORD),
                ]
                if defined(UNICODE):
                    DIDEVICEIMAGEINFO = DIDEVICEIMAGEINFOW
                    LPDIDEVICEIMAGEINFO = LPDIDEVICEIMAGEINFOW
                else:
                    DIDEVICEIMAGEINFO = DIDEVICEIMAGEINFOA
                    LPDIDEVICEIMAGEINFO = LPDIDEVICEIMAGEINFOA
                # END IF   UNICODE

                LPCDIDEVICEIMAGEINFOA = POINTER(DIDEVICEIMAGEINFOA)
                LPCDIDEVICEIMAGEINFOW = POINTER(DIDEVICEIMAGEINFOW)
                if defined(UNICODE):
                    DIDEVICEIMAGEINFO = DIDEVICEIMAGEINFOW
                    LPCDIDEVICEIMAGEINFO = LPCDIDEVICEIMAGEINFOW
                else:
                    DIDEVICEIMAGEINFO = DIDEVICEIMAGEINFOA
                    LPCDIDEVICEIMAGEINFO = LPCDIDEVICEIMAGEINFOA
                # END IF   UNICODE

                LPCDIDEVICEIMAGEINFO = POINTER(DIDEVICEIMAGEINFO)

                _DIDEVICEIMAGEINFOHEADERA._fields_ = [
                    ('dwSize', DWORD),
                    ('dwSizeImageInfo', DWORD),
                    ('dwcViews', DWORD),
                    ('dwcButtons', DWORD),
                    ('dwcAxes', DWORD),
                    ('dwcPOVs', DWORD),
                    ('dwBufferSize', DWORD),
                    ('dwBufferUsed', DWORD),
                    ('lprgImageInfoArray', LPDIDEVICEIMAGEINFOA),
                ]

                _DIDEVICEIMAGEINFOHEADERW._fields_ = [
                    ('dwSize', DWORD),
                    ('dwSizeImageInfo', DWORD),
                    ('dwcViews', DWORD),
                    ('dwcButtons', DWORD),
                    ('dwcAxes', DWORD),
                    ('dwcPOVs', DWORD),
                    ('dwBufferSize', DWORD),
                    ('dwBufferUsed', DWORD),
                    ('lprgImageInfoArray', LPDIDEVICEIMAGEINFOW),
                ]
                if defined(UNICODE):
                    DIDEVICEIMAGEINFOHEADER = DIDEVICEIMAGEINFOHEADERW
                    LPDIDEVICEIMAGEINFOHEADER = LPDIDEVICEIMAGEINFOHEADERW
                else:
                    DIDEVICEIMAGEINFOHEADER = DIDEVICEIMAGEINFOHEADERA
                    LPDIDEVICEIMAGEINFOHEADER = LPDIDEVICEIMAGEINFOHEADERA
                # END IF   UNICODE

                LPCDIDEVICEIMAGEINFOHEADERA = POINTER(DIDEVICEIMAGEINFOHEADERA)
                LPCDIDEVICEIMAGEINFOHEADERW = POINTER(DIDEVICEIMAGEINFOHEADERW)
                if defined(UNICODE):
                    DIDEVICEIMAGEINFOHEADER = DIDEVICEIMAGEINFOHEADERW
                    LPCDIDEVICEIMAGEINFOHEADER = LPCDIDEVICEIMAGEINFOHEADERW
                else:
                    DIDEVICEIMAGEINFOHEADER = DIDEVICEIMAGEINFOHEADERA
                    LPCDIDEVICEIMAGEINFOHEADER = LPCDIDEVICEIMAGEINFOHEADERA
                # END IF   UNICODE

                LPCDIDEVICEIMAGEINFOHEADER = POINTER(DIDEVICEIMAGEINFOHEADER)
            # END IF  DIRECTINPUT_VERSION > 0x0700

            if DIRECTINPUT_VERSION >= 0x0500:
                # These structures are defined for DirectX 3.0 compatibility
                DIDEVICEOBJECTINSTANCE_DX3A._fields_ = [
                    ('dwSize', DWORD),
                    ('guidType', GUID),
                    ('dwOfs', DWORD),
                    ('dwType', DWORD),
                    ('dwFlags', DWORD),
                    ('tszName', CHAR * MAX_PATH),
                ]

                DIDEVICEOBJECTINSTANCE_DX3W._fields_ = [
                    ('dwSize', DWORD),
                    ('guidType', GUID),
                    ('dwOfs', DWORD),
                    ('dwType', DWORD),
                    ('dwFlags', DWORD),
                    ('tszName', WCHAR * MAX_PATH),
                ]
                if defined(UNICODE):
                    DIDEVICEOBJECTINSTANCE_DX3 = DIDEVICEOBJECTINSTANCE_DX3W
                    LPDIDEVICEOBJECTINSTANCE_DX3 = LPDIDEVICEOBJECTINSTANCE_DX3W
                else:
                    DIDEVICEOBJECTINSTANCE_DX3 = DIDEVICEOBJECTINSTANCE_DX3A
                    LPDIDEVICEOBJECTINSTANCE_DX3 = LPDIDEVICEOBJECTINSTANCE_DX3A
                # END IF   UNICODE

                LPCDIDEVICEOBJECTINSTANCE_DX3A = POINTER(DIDEVICEOBJECTINSTANCE_DX3A)
                LPCDIDEVICEOBJECTINSTANCE_DX3W = POINTER(DIDEVICEOBJECTINSTANCE_DX3W)
                LPCDIDEVICEOBJECTINSTANCE_DX3 = POINTER(DIDEVICEOBJECTINSTANCE_DX3)
            # END IF  DIRECTINPUT_VERSION >= 0x0500

            _TEMP_DIDEVICEOBJECTINSTANCEA = [
                ('dwSize', DWORD),
                ('guidType', GUID),
                ('dwOfs', DWORD),
                ('dwType', DWORD),
                ('dwFlags', DWORD),
                ('tszName', CHAR * MAX_PATH),
            ]

            if DIRECTINPUT_VERSION >= 0x0500:
                _TEMP_DIDEVICEOBJECTINSTANCEA += [
                    ('dwFFMaxForce', DWORD),
                    ('dwFFForceResolution', DWORD),
                    ('wCollectionNumber', WORD),
                    ('wDesignatorIndex', WORD),
                    ('wUsagePage', WORD),
                    ('wUsage', WORD),
                    ('dwDimension', DWORD),
                    ('wExponent', WORD),
                    ('wReportId', WORD),
                ]
            # END IF   DIRECTINPUT_VERSION >= 0x0500

            DIDEVICEOBJECTINSTANCEA._fields_ = _TEMP_DIDEVICEOBJECTINSTANCEA

            _TEMP_DIDEVICEOBJECTINSTANCEW = [
                ('dwSize', DWORD),
                ('guidType', GUID),
                ('dwOfs', DWORD),
                ('dwType', DWORD),
                ('dwFlags', DWORD),
                ('tszName', WCHAR * MAX_PATH),
            ]

            if DIRECTINPUT_VERSION >= 0x0500:
                _TEMP_DIDEVICEOBJECTINSTANCEW += [
                    ('dwFFMaxForce', DWORD),
                    ('dwFFForceResolution', DWORD),
                    ('wCollectionNumber', WORD),
                    ('wDesignatorIndex', WORD),
                    ('wUsagePage', WORD),
                    ('wUsage', WORD),
                    ('dwDimension', DWORD),
                    ('wExponent', WORD),
                    ('wReportId', WORD),
                ]
            # END IF   DIRECTINPUT_VERSION >= 0x0500

            DIDEVICEOBJECTINSTANCEW._fields_ = _TEMP_DIDEVICEOBJECTINSTANCEW

            if defined(UNICODE):
                DIDEVICEOBJECTINSTANCE = DIDEVICEOBJECTINSTANCEW
                LPDIDEVICEOBJECTINSTANCE = LPDIDEVICEOBJECTINSTANCEW
            else:
                DIDEVICEOBJECTINSTANCE = DIDEVICEOBJECTINSTANCEA
                LPDIDEVICEOBJECTINSTANCE = LPDIDEVICEOBJECTINSTANCEA
            # END IF   UNICODE

            LPCDIDEVICEOBJECTINSTANCEA = POINTER(DIDEVICEOBJECTINSTANCEA)
            LPCDIDEVICEOBJECTINSTANCEW = POINTER(DIDEVICEOBJECTINSTANCEW)
            LPCDIDEVICEOBJECTINSTANCE = POINTER(DIDEVICEOBJECTINSTANCE)

            # typedef BOOL (FAR PASCAL * LPDIENUMDEVICEOBJECTSCALLBACKA)(LPCDIDEVICEOBJECTINSTANCEA, LPVOID);
            LPDIENUMDEVICEOBJECTSCALLBACKA = PASCAL(
                BOOL,
                LPCDIDEVICEOBJECTINSTANCEA,
                LPVOID
            )


            # typedef BOOL (FAR PASCAL * LPDIENUMDEVICEOBJECTSCALLBACKW)(LPCDIDEVICEOBJECTINSTANCEW, LPVOID);
            LPDIENUMDEVICEOBJECTSCALLBACKW = PASCAL(
                BOOL,
                LPCDIDEVICEOBJECTINSTANCEW,
                LPVOID
            )

            if defined(UNICODE):
                LPDIENUMDEVICEOBJECTSCALLBACK = LPDIENUMDEVICEOBJECTSCALLBACKW
            else:
                LPDIENUMDEVICEOBJECTSCALLBACK = LPDIENUMDEVICEOBJECTSCALLBACKA
            # END IF   not UNICODE

            if DIRECTINPUT_VERSION >= 0x0500:
                DIDOI_FFACTUATOR = 0x00000001
                DIDOI_FFEFFECTTRIGGER = 0x00000002
                DIDOI_POLLED = 0x00008000
                DIDOI_ASPECTPOSITION = 0x00000100
                DIDOI_ASPECTVELOCITY = 0x00000200
                DIDOI_ASPECTACCEL = 0x00000300
                DIDOI_ASPECTFORCE = 0x00000400
                DIDOI_ASPECTMASK = 0x00000F00
            # END IF  DIRECTINPUT_VERSION >= 0x0500

            if DIRECTINPUT_VERSION >= 0x050a:
                DIDOI_GUIDISUSAGE = 0x00010000
            # END IF  DIRECTINPUT_VERSION >= 0x050a

            DIPROPHEADER._fields_ = [
                ('dwSize', DWORD),
                ('dwHeaderSize', DWORD),
                ('dwObj', DWORD),
                ('dwHow', DWORD),
            ]
            LPCDIPROPHEADER = POINTER(DIPROPHEADER)
            DIPH_DEVICE = 0
            DIPH_BYOFFSET = 1
            DIPH_BYID = 2

            if DIRECTINPUT_VERSION >= 0x050a:
                DIPH_BYUSAGE = 3
            # END IF  DIRECTINPUT_VERSION >= 0x050a

            if DIRECTINPUT_VERSION >= 0x050a:
                def DIMAKEUSAGEDWORD(UsagePage, Usage):
                    return MAKELONG(Usage, UsagePage)
            # END IF  DIRECTINPUT_VERSION >= 0x050a


            DIPROPDWORD._fields_ = [
                ('diph', DIPROPHEADER),
                ('dwData', DWORD),
            ]

            LPCDIPROPDWORD = POINTER(DIPROPDWORD)

            if DIRECTINPUT_VERSION >= 0x0800:
                DIPROPPOINTER._fields_ = [
                    ('diph', DIPROPHEADER),
                    ('uData', UINT_PTR),
                ]
                LPCDIPROPPOINTER = POINTER(DIPROPPOINTER)
            # END IF  DIRECTINPUT_VERSION >= 0x0800

            DIPROPRANGE._fields_ = [
                ('diph', DIPROPHEADER),
                ('lMin', LONG),
                ('lMax', LONG),
            ]
            LPCDIPROPRANGE = POINTER(DIPROPRANGE)
            DIPROPRANGE_NOMIN = 0x80000000
            DIPROPRANGE_NOMAX = 0x7FFFFFFF

            if DIRECTINPUT_VERSION >= 0x050a:
                DIPROPCAL._fields_ = [
                    ('diph', DIPROPHEADER),
                    ('lMin', LONG),
                    ('lCenter', LONG),
                    ('lMax', LONG),
                ]
                LPCDIPROPCAL = POINTER(DIPROPCAL)

                DIPROPCALPOV._fields_ = [
                    ('diph', DIPROPHEADER),
                    ('lMin', LONG * 5),
                    ('lMax', LONG * 5),
                ]
                LPCDIPROPCALPOV = POINTER(DIPROPCALPOV)

                DIPROPGUIDANDPATH._fields_ = [
                    ('diph', DIPROPHEADER),
                    ('guidClass', GUID),
                    ('wszPath', WCHAR * MAX_PATH),
                ]
                LPCDIPROPGUIDANDPATH = POINTER(DIPROPGUIDANDPATH)

                DIPROPSTRING._fields_ = [
                    ('diph', DIPROPHEADER),
                    ('wsz', WCHAR * MAX_PATH),
                ]
                LPCDIPROPSTRING = POINTER(DIPROPSTRING)
            # END IF  DIRECTINPUT_VERSION >= 0x050a

            if DIRECTINPUT_VERSION >= 0x0800:
                MAXCPOINTSNUM = 8

                _CPOINT._fields_ = [
                    # raw value
                    ('lP', LONG),
                    # logical_value / max_logical_value * 10000
                    ('dwLog', DWORD),
                ]

                DIPROPCPOINTS._fields_ = [
                    ('diph', DIPROPHEADER),
                    ('dwCPointsNum', DWORD),
                    ('cp', CPOINT * MAXCPOINTSNUM),
                ]
                LPCDIPROPCPOINTS = POINTER(DIPROPCPOINTS)
            # END IF  DIRECTINPUT_VERSION >= 0x0800

            if defined(__cplusplus):
                def MAKEDIPROP(prop):
                    return GUID(prop)
            else:
                def MAKEDIPROP(prop):
                    return REFGUID(prop)
            # END IF

            DIPROP_BUFFERSIZE = MAKEDIPROP(1)
            DIPROP_AXISMODE = MAKEDIPROP(2)
            DIPROPAXISMODE_ABS = 0
            DIPROPAXISMODE_REL = 1
            DIPROP_GRANULARITY = MAKEDIPROP(3)
            DIPROP_RANGE = MAKEDIPROP(4)
            DIPROP_DEADZONE = MAKEDIPROP(5)
            DIPROP_SATURATION = MAKEDIPROP(6)
            DIPROP_FFGAIN = MAKEDIPROP(7)
            DIPROP_FFLOAD = MAKEDIPROP(8)
            DIPROP_AUTOCENTER = MAKEDIPROP(9)
            DIPROPAUTOCENTER_OFF = 0
            DIPROPAUTOCENTER_ON = 1
            DIPROP_CALIBRATIONMODE = MAKEDIPROP(10)
            DIPROPCALIBRATIONMODE_COOKED = 0
            DIPROPCALIBRATIONMODE_RAW = 1
            if DIRECTINPUT_VERSION >= 0x050a:
                DIPROP_CALIBRATION = MAKEDIPROP(11)
                DIPROP_GUIDANDPATH = MAKEDIPROP(12)
                DIPROP_INSTANCENAME = MAKEDIPROP(13)
                DIPROP_PRODUCTNAME = MAKEDIPROP(14)
            # END IF  DIRECTINPUT_VERSION >= 0x050a

            if DIRECTINPUT_VERSION >= 0x05b2:
                DIPROP_JOYSTICKID = MAKEDIPROP(15)
                DIPROP_GETPORTDISPLAYNAME = MAKEDIPROP(16)
            # END IF  DIRECTINPUT_VERSION >= 0x05b2

            if DIRECTINPUT_VERSION >= 0x0700:
                DIPROP_PHYSICALRANGE = MAKEDIPROP(18)
                DIPROP_LOGICALRANGE = MAKEDIPROP(19)
            # END IF  DIRECTINPUT_VERSION >= 0x0700

            if DIRECTINPUT_VERSION >= 0x0800:
                DIPROP_KEYNAME = MAKEDIPROP(20)
                DIPROP_CPOINTS = MAKEDIPROP(21)
                DIPROP_APPDATA = MAKEDIPROP(22)
                DIPROP_SCANCODE = MAKEDIPROP(23)
                DIPROP_VIDPID = MAKEDIPROP(24)
                DIPROP_USERNAME = MAKEDIPROP(25)
                DIPROP_TYPENAME = MAKEDIPROP(26)
            # END IF  DIRECTINPUT_VERSION >= 0x0800


            DIDEVICEOBJECTDATA_DX3._fields_ = [
                ('dwOfs', DWORD),
                ('dwData', DWORD),
                ('dwTimeStamp', DWORD),
                ('dwSequence', DWORD),
            ]
            LPCDIDEVICEOBJECTDATA_DX = POINTER(DIDEVICEOBJECTDATA_DX3)

            _TEMP_DIDEVICEOBJECTDATA = [
                ('dwOfs', DWORD),
                ('dwData', DWORD),
                ('dwTimeStamp', DWORD),
                ('dwSequence', DWORD),
            ]
            if DIRECTINPUT_VERSION >= 0x0800:
                _TEMP_DIDEVICEOBJECTDATA += [
                    ('uAppData', UINT_PTR),
                ]
            # END IF   DIRECTINPUT_VERSION >= 0x0800


            DIDEVICEOBJECTDATA._fields_ = _TEMP_DIDEVICEOBJECTDATA
            LPCDIDEVICEOBJECTDATA = POINTER(DIDEVICEOBJECTDATA)
            DIGDD_PEEK = 0x00000001


            def DISEQUENCE_COMPARE(dwSequence1, cmp, dwSequence2):
                return (dwSequence1 - dwSequence2), cmp, 0

            DISCL_EXCLUSIVE = 0x00000001
            DISCL_NONEXCLUSIVE = 0x00000002
            DISCL_FOREGROUND = 0x00000004
            DISCL_BACKGROUND = 0x00000008
            DISCL_NOWINKEY = 0x00000010
            if DIRECTINPUT_VERSION >= 0x0500:
                # These structures are defined for DirectX 3.0 compatibility
                DIDEVICEINSTANCE_DX3A._fields_ = [
                    ('dwSize', DWORD),
                    ('guidInstance', GUID),
                    ('guidProduct', GUID),
                    ('dwDevType', DWORD),
                    ('tszInstanceName', CHAR * MAX_PATH),
                    ('tszProductName', CHAR * MAX_PATH),
                ]

                DIDEVICEINSTANCE_DX3W._fields_ = [
                    ('dwSize', DWORD),
                    ('guidInstance', GUID),
                    ('guidProduct', GUID),
                    ('dwDevType', DWORD),
                    ('tszInstanceName', WCHAR * MAX_PATH),
                    ('tszProductName', WCHAR * MAX_PATH),
                ]
                if defined(UNICODE):
                    DIDEVICEINSTANCE_DX3 = DIDEVICEINSTANCE_DX3W
                    LPDIDEVICEINSTANCE_DX3 = LPDIDEVICEINSTANCE_DX3W
                else:
                    DIDEVICEINSTANCE_DX3 = DIDEVICEINSTANCE_DX3A
                    LPDIDEVICEINSTANCE_DX3 = LPDIDEVICEINSTANCE_DX3A
                # END IF   UNICODE

                LPCDIDEVICEINSTANCE_DX3A = POINTER(DIDEVICEINSTANCE_DX3A)
                LPCDIDEVICEINSTANCE_DX3W = POINTER(DIDEVICEINSTANCE_DX3W)
                LPCDIDEVICEINSTANCE_DX3 = POINTER(DIDEVICEINSTANCE_DX3)
            # END IF  DIRECTINPUT_VERSION >= 0x0500

            _TEMP_DIDEVICEINSTANCEA = [
                ('dwSize', DWORD),
                ('guidInstance', GUID),
                ('guidProduct', GUID),
                ('dwDevType', DWORD),
                ('tszInstanceName', CHAR * MAX_PATH),
                ('tszProductName', CHAR * MAX_PATH),
            ]
            if DIRECTINPUT_VERSION >= 0x0500:
                _TEMP_DIDEVICEINSTANCEA += [
                    ('guidFFDriver', GUID),
                    ('wUsagePage', WORD),
                    ('wUsage', WORD),
                ]
            # END IF   DIRECTINPUT_VERSION >= 0x0500


            DIDEVICEINSTANCEA._fields_ = _TEMP_DIDEVICEINSTANCEA

            _TEMP_DIDEVICEINSTANCEW = [
                ('dwSize', DWORD),
                ('guidInstance', GUID),
                ('guidProduct', GUID),
                ('dwDevType', DWORD),
                ('tszInstanceName', WCHAR * MAX_PATH),
                ('tszProductName', WCHAR * MAX_PATH),
            ]

            if DIRECTINPUT_VERSION >= 0x0500:
                _TEMP_DIDEVICEINSTANCEW += [
                    ('guidFFDriver', GUID),
                    ('wUsagePage', WORD),
                    ('wUsage', WORD),
                ]
            # END IF   DIRECTINPUT_VERSION >= 0x0500


            DIDEVICEINSTANCEW._fields_ = _TEMP_DIDEVICEINSTANCEW

            if defined(UNICODE):
                DIDEVICEINSTANCE = DIDEVICEINSTANCEW
                LPDIDEVICEINSTANCE = LPDIDEVICEINSTANCEW
            else:
                DIDEVICEINSTANCE = DIDEVICEINSTANCEA
                LPDIDEVICEINSTANCE = LPDIDEVICEINSTANCEA
            # END IF   UNICODE

            LPCDIDEVICEINSTANCEA = POINTER(DIDEVICEINSTANCEA)
            LPCDIDEVICEINSTANCEW = POINTER(DIDEVICEINSTANCEW)

            if defined(UNICODE):
                DIDEVICEINSTANCE = DIDEVICEINSTANCEW
                LPCDIDEVICEINSTANCE = LPCDIDEVICEINSTANCEW
            else:
                DIDEVICEINSTANCE = DIDEVICEINSTANCEA
                LPCDIDEVICEINSTANCE = LPCDIDEVICEINSTANCEA
            # END IF   UNICODE

            LPCDIDEVICEINSTANCE = POINTER(DIDEVICEINSTANCE)
            IDirectInputDeviceW = INTERFACE('IDirectInputDeviceW')
            IDirectInputDeviceW._iid_ = IID_IDirectInputDeviceW
            DECLARE_INTERFACE_(IDirectInputDeviceW, comtypes.IUnknown)(
            # * IUnknown methods *
            # * IDirectInputDeviceW methods

                STDMETHOD('GetCapabilities')((LPDIDEVCAPS,)),
                STDMETHOD('EnumObjects')(
                    (LPDIENUMDEVICEOBJECTSCALLBACKW, LPVOID, DWORD)
                ),
                STDMETHOD('GetProperty')((REFGUID, LPDIPROPHEADER)),
                STDMETHOD('SetProperty')((REFGUID, LPCDIPROPHEADER)),
                STDMETHOD('Acquire')(),
                STDMETHOD('Unacquire')(),
                STDMETHOD('GetDeviceState')((DWORD, LPVOID)),
                STDMETHOD('GetDeviceData')(
                    (DWORD, LPDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                ),
                STDMETHOD('SetDataFormat')((LPCDIDATAFORMAT,)),
                STDMETHOD('SetEventNotification')((HANDLE,)),
                STDMETHOD('SetCooperativeLevel')((HWND, DWORD)),
                STDMETHOD('GetObjectInfo')(
                    (LPDIDEVICEOBJECTINSTANCEW, DWORD, DWORD)
                ),
                STDMETHOD('GetDeviceInfo')((LPDIDEVICEINSTANCEW,)),
                STDMETHOD('RunControlPanel')((HWND, DWORD)),
                STDMETHOD('Initialize')((HINSTANCE, DWORD, REFGUID))
            )

            LPDIRECTINPUTDEVICEW = POINTER(IDirectInputDeviceW)

            IDirectInputDeviceA = INTERFACE('IDirectInputDeviceA')
            IDirectInputDeviceA._iid_ = IID_IDirectInputDeviceA
            DECLARE_INTERFACE_(IDirectInputDeviceA, comtypes.IUnknown)(
            # * IUnknown methods *
            # * IDirectInputDeviceA methods
                STDMETHOD('GetCapabilities')((LPDIDEVCAPS,)),
                STDMETHOD('EnumObjects')(
                    (LPDIENUMDEVICEOBJECTSCALLBACKW, LPVOID, DWORD)
                ),
                STDMETHOD('GetProperty')((REFGUID, LPDIPROPHEADER)),
                STDMETHOD('SetProperty')((REFGUID, LPCDIPROPHEADER)),
                STDMETHOD('Acquire')(),
                STDMETHOD('Unacquire')(),
                STDMETHOD('GetDeviceState')((DWORD, LPVOID)),
                STDMETHOD('GetDeviceData')(
                    (DWORD, LPDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                ),
                STDMETHOD('SetDataFormat')((LPCDIDATAFORMAT,)),
                STDMETHOD('SetEventNotification')((HANDLE,)),
                STDMETHOD('SetCooperativeLevel')((HWND, DWORD)),
                STDMETHOD('GetObjectInfo')(
                    (LPDIDEVICEOBJECTINSTANCEA, DWORD, DWORD)
                ),
                STDMETHOD('GetDeviceInfo')((LPDIDEVICEINSTANCEA,)),
                STDMETHOD('RunControlPanel')((HWND, DWORD)),
                STDMETHOD('Initialize')((HINSTANCE, DWORD, REFGUID))
            )

            LPDIRECTINPUTDEVICEA = POINTER(IDirectInputDeviceA)

            if defined(UNICODE):
                IID_IDirectInputDevice = IID_IDirectInputDeviceW
                IDirectInputDevice = IDirectInputDeviceW
            else:
                IID_IDirectInputDevice = IID_IDirectInputDeviceA
                IDirectInputDevice = IDirectInputDeviceA
            # END IF

            LPDIRECTINPUTDEVICE = POINTER(IDirectInputDevice)

            if not defined(__cplusplus) or defined(CINTERFACE):
                def IDirectInputDevice_QueryInterface(p, a, b):
                    return p.lpVtbl.QueryInterface(p, a, b)


                def IDirectInputDevice_AddRef(p):
                    return p.lpVtbl.AddRef(p)


                def IDirectInputDevice_Release(p):
                    return p.lpVtbl.Release(p)


                def IDirectInputDevice_GetCapabilities(p, a):
                    return p.lpVtbl.GetCapabilities(p, a)


                def IDirectInputDevice_EnumObjects(p, a, b, c):
                    return p.lpVtbl.EnumObjects(p, a, b, c)


                def IDirectInputDevice_GetProperty(p, a, b):
                    return p.lpVtbl.GetProperty(p, a, b)


                def IDirectInputDevice_SetProperty(p, a, b):
                    return p.lpVtbl.SetProperty(p, a, b)


                def IDirectInputDevice_Acquire(p):
                    return p.lpVtbl.Acquire(p)


                def IDirectInputDevice_Unacquire(p):
                    return p.lpVtbl.Unacquire(p)


                def IDirectInputDevice_GetDeviceState(p, a, b):
                    return p.lpVtbl.GetDeviceState(p, a, b)


                def IDirectInputDevice_GetDeviceData(p, a, b, c, d):
                    return p.lpVtbl.GetDeviceData(p, a, b, c, d)


                def IDirectInputDevice_SetDataFormat(p, a):
                    return p.lpVtbl.SetDataFormat(p, a)


                def IDirectInputDevice_SetEventNotification(p, a):
                    return p.lpVtbl.SetEventNotification(p, a)


                def IDirectInputDevice_SetCooperativeLevel(p, a, b):
                    return p.lpVtbl.SetCooperativeLevel(p, a, b)


                def IDirectInputDevice_GetObjectInfo(p, a, b, c):
                    return p.lpVtbl.GetObjectInfo(p, a, b, c)


                def IDirectInputDevice_GetDeviceInfo(p, a):
                    return p.lpVtbl.GetDeviceInfo(p, a)


                def IDirectInputDevice_RunControlPanel(p, a, b):
                    return p.lpVtbl.RunControlPanel(p, a, b)


                def IDirectInputDevice_Initialize(p, a, b, c):
                    return p.lpVtbl.Initialize(p, a, b, c)
            else:
                def IDirectInputDevice_QueryInterface(p, a, b):
                    return p.QueryInterface(a, b)


                def IDirectInputDevice_AddRef(p):
                    return p.AddRef()


                def IDirectInputDevice_Release(p):
                    return p.Release()


                def IDirectInputDevice_GetCapabilities(p, a):
                    return p.GetCapabilities(a)


                def IDirectInputDevice_EnumObjects(p, a, b, c):
                    return p.EnumObjects(a, b, c)


                def IDirectInputDevice_GetProperty(p, a, b):
                    return p.GetProperty(a, b)


                def IDirectInputDevice_SetProperty(p, a, b):
                    return p.SetProperty(a, b)


                def IDirectInputDevice_Acquire(p):
                    return p.Acquire()


                def IDirectInputDevice_Unacquire(p):
                    return p.Unacquire()


                def IDirectInputDevice_GetDeviceState(p, a, b):
                    return p.GetDeviceState(a, b)


                def IDirectInputDevice_GetDeviceData(p, a, b, c, d):
                    return p.GetDeviceData(a, b, c, d)


                def IDirectInputDevice_SetDataFormat(p, a):
                    return p.SetDataFormat(a)


                def IDirectInputDevice_SetEventNotification(p, a):
                    return p.SetEventNotification(a)


                def IDirectInputDevice_SetCooperativeLevel(p, a, b):
                    return p.SetCooperativeLevel(a, b)


                def IDirectInputDevice_GetObjectInfo(p, a, b, c):
                    return p.GetObjectInfo(a, b, c)


                def IDirectInputDevice_GetDeviceInfo(p, a):
                    return p.GetDeviceInfo(a)


                def IDirectInputDevice_RunControlPanel(p, a, b):
                    return p.RunControlPanel(a, b)


                def IDirectInputDevice_Initialize(p, a, b, c):
                    return p.Initialize(a, b, c)
            # END IF

        # END IF  DIJ_RINGZERO

        if DIRECTINPUT_VERSION >= 0x0500:
            DISFFC_RESET = 0x00000001
            DISFFC_STOPALL = 0x00000002
            DISFFC_PAUSE = 0x00000004
            DISFFC_CONTINUE = 0x00000008
            DISFFC_SETACTUATORSON = 0x00000010
            DISFFC_SETACTUATORSOFF = 0x00000020
            DIGFFS_EMPTY = 0x00000001
            DIGFFS_STOPPED = 0x00000002
            DIGFFS_PAUSED = 0x00000004
            DIGFFS_ACTUATORSON = 0x00000010
            DIGFFS_ACTUATORSOFF = 0x00000020
            DIGFFS_POWERON = 0x00000040
            DIGFFS_POWEROFF = 0x00000080
            DIGFFS_SAFETYSWITCHON = 0x00000100
            DIGFFS_SAFETYSWITCHOFF = 0x00000200
            DIGFFS_USERFFSWITCHON = 0x00000400
            DIGFFS_USERFFSWITCHOFF = 0x00000800
            DIGFFS_DEVICELOST = 0x80000000

            if not defined(DIJ_RINGZERO):
                DIEFFECTINFOA._fields_ = [
                    ('dwSize', DWORD),
                    ('guid', GUID),
                    ('dwEffType', DWORD),
                    ('dwStaticParams', DWORD),
                    ('dwDynamicParams', DWORD),
                    ('tszName', CHAR * MAX_PATH),
                ]

                DIEFFECTINFOW._fields_ = [
                    ('dwSize', DWORD),
                    ('guid', GUID),
                    ('dwEffType', DWORD),
                    ('dwStaticParams', DWORD),
                    ('dwDynamicParams', DWORD),
                    ('tszName', WCHAR * MAX_PATH),
                ]
                if defined(UNICODE):
                    DIEFFECTINFO = DIEFFECTINFOW
                    LPDIEFFECTINFO = LPDIEFFECTINFOW
                else:
                    DIEFFECTINFO = DIEFFECTINFOA
                    LPDIEFFECTINFO = LPDIEFFECTINFOA
                # END IF   UNICODE

                LPCDIEFFECTINFOA = POINTER(DIEFFECTINFOA)
                LPCDIEFFECTINFOW = POINTER(DIEFFECTINFOW)
                LPCDIEFFECTINFO = POINTER(DIEFFECTINFO)
                DISDD_CONTINUE = 0x00000001

                # typedef BOOL (FAR PASCAL * LPDIENUMEFFECTSCALLBACKA)(
                # LPCDIEFFECTINFOA,
                # LPVOID
                # );
                LPDIENUMEFFECTSCALLBACKA = PASCAL(
                    BOOL,
                    LPCDIEFFECTINFOA,
                    LPVOID
                )


                # typedef BOOL (FAR PASCAL * LPDIENUMEFFECTSCALLBACKW)(
                # LPCDIEFFECTINFOW,
                # LPVOID
                # );
                LPDIENUMEFFECTSCALLBACKW = PASCAL(
                    BOOL,
                    LPCDIEFFECTINFOW,
                    LPVOID
                )


                if defined(UNICODE):
                    LPDIENUMEFFECTSCALLBACK = LPDIENUMEFFECTSCALLBACKW
                else:
                    LPDIENUMEFFECTSCALLBACK = LPDIENUMEFFECTSCALLBACKA
                # END IF   not UNICODE

                # typedef BOOL (
                # FAR PASCAL * LPDIENUMCREATEDEFFECTOBJECTSCALLBACK
                # )(LPDIRECTINPUTEFFECT, LPVOID);
                LPDIENUMCREATEDEFFECTOBJECTSCALLBACK = PASCAL(
                    BOOL,
                    LPDIRECTINPUTEFFECT,
                    LPVOID
                )

                IDirectInputDevice2W = INTERFACE('IDirectInputDevice2W')

                IDirectInputDevice2W._iid_ = IID_IDirectInputDevice2W
                DECLARE_INTERFACE_(IDirectInputDevice2W, IDirectInputDeviceW)(
                    # * IUnknown methods *
                    # * IDirectInputDeviceW methods *
                    # * IDirectInputDevice2W methods
                    STDMETHOD('CreateEffect')(
                        (
                            REFGUID,
                            LPCDIEFFECT,
                            POINTER(LPDIRECTINPUTEFFECT),
                            LPUNKNOWN
                        )
                    ),
                    STDMETHOD('EnumEffects')(
                        (LPDIENUMEFFECTSCALLBACKW, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetEffectInfo')((LPDIEFFECTINFOW, REFGUID)),
                    STDMETHOD('GetForceFeedbackState')((LPDWORD,)),
                    STDMETHOD('SendForceFeedbackCommand')((DWORD,)),
                    STDMETHOD('EnumCreatedEffectObjects')(
                        (LPDIENUMCREATEDEFFECTOBJECTSCALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('Escape')((LPDIEFFESCAPE,)),
                    STDMETHOD('Poll')(),
                    STDMETHOD('SendDeviceData')(
                        (DWORD, LPCDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                    ),

                )

                LPDIRECTINPUTDEVICE2W = POINTER(IDirectInputDevice2W)

                IDirectInputDevice2A = INTERFACE('IDirectInputDevice2A')
                IDirectInputDevice2A._iid_ = IID_IDirectInputDevice2A
                DECLARE_INTERFACE_(IDirectInputDevice2A, IDirectInputDeviceA)(
                    # * IUnknown methods *
                    # * IDirectInputDeviceA methods *
                    # * IDirectInputDevice2A methods
                    STDMETHOD('CreateEffect')(
                        (
                            REFGUID,
                            LPCDIEFFECT,
                            POINTER(LPDIRECTINPUTEFFECT),
                            LPUNKNOWN
                        )
                    ),
                    STDMETHOD('EnumEffects')(
                        (LPDIENUMEFFECTSCALLBACKA, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetEffectInfo')((LPDIEFFECTINFOA, REFGUID)),
                    STDMETHOD('GetForceFeedbackState')((LPDWORD,)),
                    STDMETHOD('SendForceFeedbackCommand')((DWORD,)),
                    STDMETHOD('EnumCreatedEffectObjects')(
                        (LPDIENUMCREATEDEFFECTOBJECTSCALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('Escape')((LPDIEFFESCAPE,)),
                    STDMETHOD('Poll')(),
                    STDMETHOD('SendDeviceData')(
                        (DWORD, LPCDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                    ),
                )

                LPDIRECTINPUTDEVICE2A = POINTER(IDirectInputDevice2A)

                if defined(UNICODE):
                    IID_IDirectInputDevice2 = IID_IDirectInputDevice2W
                    IDirectInputDevice2 = IDirectInputDevice2W
                else:
                    IID_IDirectInputDevice2 = IID_IDirectInputDevice2A
                    IDirectInputDevice2 = IDirectInputDevice2A
                # END IF

                LPDIRECTINPUTDEVICE2 = POINTER(IDirectInputDevice2)

                if not defined(__cplusplus) or defined(CINTERFACE):
                    def IDirectInputDevice2_QueryInterface(p, a, b):
                        return p.lpVtbl.QueryInterface(p, a, b)


                    def IDirectInputDevice2_AddRef(p):
                        return p.lpVtbl.AddRef(p)


                    def IDirectInputDevice2_Release(p):
                        return p.lpVtbl.Release(p)


                    def IDirectInputDevice2_GetCapabilities(p, a):
                        return p.lpVtbl.GetCapabilities(p, a)


                    def IDirectInputDevice2_EnumObjects(p, a, b, c):
                        return p.lpVtbl.EnumObjects(p, a, b, c)


                    def IDirectInputDevice2_GetProperty(p, a, b):
                        return p.lpVtbl.GetProperty(p, a, b)


                    def IDirectInputDevice2_SetProperty(p, a, b):
                        return p.lpVtbl.SetProperty(p, a, b)


                    def IDirectInputDevice2_Acquire(p):
                        return p.lpVtbl.Acquire(p)


                    def IDirectInputDevice2_Unacquire(p):
                        return p.lpVtbl.Unacquire(p)


                    def IDirectInputDevice2_GetDeviceState(p, a, b):
                        return p.lpVtbl.GetDeviceState(p, a, b)


                    def IDirectInputDevice2_GetDeviceData(p, a, b, c, d):
                        return p.lpVtbl.GetDeviceData(p, a,b, c, d)


                    def IDirectInputDevice2_SetDataFormat(p, a):
                        return p.lpVtbl.SetDataFormat(p, a)


                    def IDirectInputDevice2_SetEventNotification(p, a):
                        return p.lpVtbl.SetEventNotification(p, a)


                    def IDirectInputDevice2_SetCooperativeLevel(p, a, b):
                        return p.lpVtbl.SetCooperativeLevel(p, a, b)


                    def IDirectInputDevice2_GetObjectInfo(p, a, b, c):
                        return p.lpVtbl.GetObjectInfo(p, a, b, c)


                    def IDirectInputDevice2_GetDeviceInfo(p, a):
                        return p.lpVtbl.GetDeviceInfo(p, a)


                    def IDirectInputDevice2_RunControlPanel(p, a, b):
                        return p.lpVtbl.RunControlPanel(p, a, b)


                    def IDirectInputDevice2_Initialize(p, a, b, c):
                        return p.lpVtbl.Initialize(p, a, b, c)


                    def IDirectInputDevice2_CreateEffect(p, a, b, c, d):
                        return p.lpVtbl.CreateEffect(p, a, b, c, d)


                    def IDirectInputDevice2_EnumEffects(p, a, b, c):
                        return p.lpVtbl.EnumEffects(p, a, b, c)


                    def IDirectInputDevice2_GetEffectInfo(p, a, b):
                        return p.lpVtbl.GetEffectInfo(p, a, b)


                    def IDirectInputDevice2_GetForceFeedbackState(p, a):
                        return p.lpVtbl.GetForceFeedbackState(p, a)


                    def IDirectInputDevice2_SendForceFeedbackCommand(p, a):
                        return p.lpVtbl.SendForceFeedbackCommand(p, a)


                    def IDirectInputDevice2_EnumCreatedEffectObjects(p, a, b, c):
                        return p.lpVtbl.EnumCreatedEffectObjects(p, a, b, c)


                    def IDirectInputDevice2_Escape(p, a):
                        return p.lpVtbl.Escape(p, a)


                    def IDirectInputDevice2_Poll(p):
                        return p.lpVtbl.Poll(p)


                    def IDirectInputDevice2_SendDeviceData(p, a, b, c, d):
                        return p.lpVtbl.SendDeviceData(p, a, b, c, d)
                else:
                    def IDirectInputDevice2_QueryInterface(p, a, b):
                        return p.QueryInterface(a,b)


                    def IDirectInputDevice2_AddRef(p):
                        return p.AddRef()


                    def IDirectInputDevice2_Release(p):
                        return p.Release()


                    def IDirectInputDevice2_GetCapabilities(p, a):
                        return p.GetCapabilities(a)


                    def IDirectInputDevice2_EnumObjects(p, a, b, c):
                        return p.EnumObjects(a, b, c)


                    def IDirectInputDevice2_GetProperty(p, a, b):
                        return p.GetProperty(a, b)


                    def IDirectInputDevice2_SetProperty(p, a, b):
                        return p.SetProperty(a, b)


                    def IDirectInputDevice2_Acquire(p):
                        return p.Acquire()


                    def IDirectInputDevice2_Unacquire(p):
                        return p.Unacquire()


                    def IDirectInputDevice2_GetDeviceState(p, a, b):
                        return p.GetDeviceState(a, b)


                    def IDirectInputDevice2_GetDeviceData(p, a, b, c, d):
                        return p.GetDeviceData(a, b, c, d)


                    def IDirectInputDevice2_SetDataFormat(p, a):
                        return p.SetDataFormat(a)


                    def IDirectInputDevice2_SetEventNotification(p, a):
                        return p.SetEventNotification(a)


                    def IDirectInputDevice2_SetCooperativeLevel(p, a, b):
                        return p.SetCooperativeLevel(a, b)


                    def IDirectInputDevice2_GetObjectInfo(p, a, b, c):
                        return p.GetObjectInfo(a, b, c)


                    def IDirectInputDevice2_GetDeviceInfo(p, a):
                        return p.GetDeviceInfo(a)


                    def IDirectInputDevice2_RunControlPanel(p, a, b):
                        return p.RunControlPanel(a, b)


                    def IDirectInputDevice2_Initialize(p, a, b, c):
                        return p.Initialize(a, b, c)


                    def IDirectInputDevice2_CreateEffect(p, a, b, c, d):
                        return p.CreateEffect(a,b,c,d)


                    def IDirectInputDevice2_EnumEffects(p, a, b, c):
                        return p.EnumEffects(a, b, c)


                    def IDirectInputDevice2_GetEffectInfo(p, a, b):
                        return p.GetEffectInfo(a, b)


                    def IDirectInputDevice2_GetForceFeedbackState(p, a):
                        return p.GetForceFeedbackState(a)


                    def IDirectInputDevice2_SendForceFeedbackCommand(p, a):
                        return p.SendForceFeedbackCommand(a)


                    def IDirectInputDevice2_EnumCreatedEffectObjects(p, a, b, c):
                        return p.EnumCreatedEffectObjects(a, b, c)


                    def IDirectInputDevice2_Escape(p, a):
                        return p.Escape(a)


                    def IDirectInputDevice2_Poll(p):
                        return p.Poll()


                    def IDirectInputDevice2_SendDeviceData(p, a, b, c, d):
                        return p.SendDeviceData(a, b, c, d)
                # END IF
            # END IF  DIJ_RINGZERO
        # END IF  DIRECTINPUT_VERSION >= 0x0500

        if DIRECTINPUT_VERSION >= 0x0700:
            DIFEF_DEFAULT = 0x00000000
            DIFEF_INCLUDENONSTANDARD = 0x00000001
            DIFEF_MODIFYIFNEEDED = 0x00000010

            if not defined(DIJ_RINGZERO):
                IDirectInputDevice7W = INTERFACE('IDirectInputDevice7W')
                IDirectInputDevice7W._iid_ = IID_IDirectInputDevice7W
                DECLARE_INTERFACE_(IDirectInputDevice7W, IDirectInputDevice2W)(
                    # * IUnknown methods *
                    # * IDirectInputDevice2W methods *
                    # * IDirectInputDevice7W methods
                    STDMETHOD('EnumEffectsInFile')(
                        (LPCWSTR,LPDIENUMEFFECTSINFILECALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('WriteEffectToFile')(
                        (LPCWSTR, DWORD, LPDIFILEEFFECT, DWORD)
                    ),
                )

                LPDIRECTINPUTDEVICE7W = POINTER(IDirectInputDevice7W)

                IDirectInputDevice7A = INTERFACE('IDirectInputDevice7A')
                IDirectInputDevice7A._iid_ = IID_IDirectInputDevice7A
                DECLARE_INTERFACE_(IDirectInputDevice7A, IDirectInputDevice2A)(
                    # * IUnknown methods *
                    # * IDirectInputDevice2W methods *
                    # * IDirectInputDevice7W methods
                    STDMETHOD('EnumEffectsInFile')(
                        (LPCWSTR, LPDIENUMEFFECTSINFILECALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('WriteEffectToFile')(
                        (LPCWSTR, DWORD, LPDIFILEEFFECT, DWORD)
                    ),
                )

                LPDIRECTINPUTDEVICE7A = POINTER(IDirectInputDevice7A)

                if defined(UNICODE):
                    IID_IDirectInputDevice7 = IID_IDirectInputDevice7W
                    IDirectInputDevice7 = IDirectInputDevice7W
                else:
                    IID_IDirectInputDevice7 = IID_IDirectInputDevice7A
                    IDirectInputDevice7 = IDirectInputDevice7A
                # END IF

                LPDIRECTINPUTDEVICE7 = POINTER(IDirectInputDevice7)

                if not defined(__cplusplus) or defined(CINTERFACE):
                    def IDirectInputDevice7_QueryInterface(p, a, b):
                        return p.lpVtbl.QueryInterface(p, a, b)


                    def IDirectInputDevice7_AddRef(p):
                        return p.lpVtbl.AddRef(p)


                    def IDirectInputDevice7_Release(p):
                        return p.lpVtbl.Release(p)


                    def IDirectInputDevice7_GetCapabilities(p, a):
                        return p.lpVtbl.GetCapabilities(p, a)


                    def IDirectInputDevice7_EnumObjects(p, a, b, c):
                        return p.lpVtbl.EnumObjects(p, a, b, c)


                    def IDirectInputDevice7_GetProperty(p, a, b):
                        return p.lpVtbl.GetProperty(p, a, b)


                    def IDirectInputDevice7_SetProperty(p, a, b):
                        return p.lpVtbl.SetProperty(p, a, b)


                    def IDirectInputDevice7_Acquire(p):
                        return p.lpVtbl.Acquire(p)


                    def IDirectInputDevice7_Unacquire(p):
                        return p.lpVtbl.Unacquire(p)


                    def IDirectInputDevice7_GetDeviceState(p, a, b):
                        return p.lpVtbl.GetDeviceState(p, a, b)


                    def IDirectInputDevice7_GetDeviceData(p, a, b, c, d):
                        return p.lpVtbl.GetDeviceData(p, a, b, c, d)


                    def IDirectInputDevice7_SetDataFormat(p, a):
                        return p.lpVtbl.SetDataFormat(p, a)


                    def IDirectInputDevice7_SetEventNotification(p, a):
                        return p.lpVtbl.SetEventNotification(p, a)


                    def IDirectInputDevice7_SetCooperativeLevel(p, a, b):
                        return p.lpVtbl.SetCooperativeLevel(p, a, b)


                    def IDirectInputDevice7_GetObjectInfo(p, a, b, c):
                        return p.lpVtbl.GetObjectInfo(p, a, b, c)


                    def IDirectInputDevice7_GetDeviceInfo(p, a):
                        return p.lpVtbl.GetDeviceInfo(p, a)


                    def IDirectInputDevice7_RunControlPanel(p, a, b):
                        return p.lpVtbl.RunControlPanel(p, a, b)


                    def IDirectInputDevice7_Initialize(p, a, b, c):
                        return p.lpVtbl.Initialize(p, a, b, c)


                    def IDirectInputDevice7_CreateEffect(p, a, b, c, d):
                        return p.lpVtbl.CreateEffect(p, a, b, c, d)


                    def IDirectInputDevice7_EnumEffects(p, a, b, c):
                        return p.lpVtbl.EnumEffects(p, a, b, c)


                    def IDirectInputDevice7_GetEffectInfo(p, a, b):
                        return p.lpVtbl.GetEffectInfo(p, a, b)


                    def IDirectInputDevice7_GetForceFeedbackState(p, a):
                        return p.lpVtbl.GetForceFeedbackState(p, a)


                    def IDirectInputDevice7_SendForceFeedbackCommand(p, a):
                        return p.lpVtbl.SendForceFeedbackCommand(p, a)


                    def IDirectInputDevice7_EnumCreatedEffectObjects(p, a, b, c):
                        return p.lpVtbl.EnumCreatedEffectObjects(p, a, b, c)


                    def IDirectInputDevice7_Escape(p, a):
                        return p.lpVtbl.Escape(p, a)


                    def IDirectInputDevice7_Poll(p):
                        return p.lpVtbl.Poll(p)


                    def IDirectInputDevice7_SendDeviceData(p, a, b, c, d):
                        return p.lpVtbl.SendDeviceData(p, a, b, c, d)


                    def IDirectInputDevice7_EnumEffectsInFile(p, a, b, c, d):
                        return p.lpVtbl.EnumEffectsInFile(p, a, b, c, d)


                    def IDirectInputDevice7_WriteEffectToFile(p, a, b, c, d):
                        return p.lpVtbl.WriteEffectToFile(p, a, b, c, d)
                else:
                    def IDirectInputDevice7_QueryInterface(p, a, b):
                        return p.QueryInterface(a, b)


                    def IDirectInputDevice7_AddRef(p):
                        return p.AddRef()


                    def IDirectInputDevice7_Release(p):
                        return p.Release()


                    def IDirectInputDevice7_GetCapabilities(p, a):
                        return p.GetCapabilities(a)


                    def IDirectInputDevice7_EnumObjects(p, a, b, c):
                        return p.EnumObjects(a, b, c)


                    def IDirectInputDevice7_GetProperty(p, a, b):
                        return p.GetProperty(a, b)


                    def IDirectInputDevice7_SetProperty(p, a, b):
                        return p.SetProperty(a, b)


                    def IDirectInputDevice7_Acquire(p):
                        return p.Acquire()


                    def IDirectInputDevice7_Unacquire(p):
                        return p.Unacquire()


                    def IDirectInputDevice7_GetDeviceState(p, a, b):
                        return p.GetDeviceState(a, b)


                    def IDirectInputDevice7_GetDeviceData(p, a, b, c, d):
                        return p.GetDeviceData(a, b, c, d)


                    def IDirectInputDevice7_SetDataFormat(p, a):
                        return p.SetDataFormat(a)


                    def IDirectInputDevice7_SetEventNotification(p, a):
                        return p.SetEventNotification(a)


                    def IDirectInputDevice7_SetCooperativeLevel(p, a, b):
                        return p.SetCooperativeLevel(a, b)


                    def IDirectInputDevice7_GetObjectInfo(p, a, b, c):
                        return p.GetObjectInfo(a, b, c)


                    def IDirectInputDevice7_GetDeviceInfo(p, a):
                        return p.GetDeviceInfo(a)


                    def IDirectInputDevice7_RunControlPanel(p, a, b):
                        return p.RunControlPanel(a, b)


                    def IDirectInputDevice7_Initialize(p, a, b, c):
                        return p.Initialize(a, b, c)


                    def IDirectInputDevice7_CreateEffect(p, a, b, c, d):
                        return p.CreateEffect(a, b, c, d)


                    def IDirectInputDevice7_EnumEffects(p, a, b, c):
                        return p.EnumEffects(a, b, c)


                    def IDirectInputDevice7_GetEffectInfo(p, a, b):
                        return p.GetEffectInfo(a, b)


                    def IDirectInputDevice7_GetForceFeedbackState(p, a):
                        return p.GetForceFeedbackState(a)


                    def IDirectInputDevice7_SendForceFeedbackCommand(p, a):
                        return p.SendForceFeedbackCommand(a)


                    def IDirectInputDevice7_EnumCreatedEffectObjects(p, a, b, c):
                        return p.EnumCreatedEffectObjects(a, b, c)


                    def IDirectInputDevice7_Escape(p, a):
                        return p.Escape(a)


                    def IDirectInputDevice7_Poll(p):
                        return p.Poll()


                    def IDirectInputDevice7_SendDeviceData(p, a, b, c, d):
                        return p.SendDeviceData(a, b, c, d)


                    def IDirectInputDevice7_EnumEffectsInFile(p, a, b, c, d):
                        return p.EnumEffectsInFile(a, b, c, d)


                    def IDirectInputDevice7_WriteEffectToFile(p, a, b, c, d):
                        return p.WriteEffectToFile(a, b, c, d)
                # END IF
            # END IF  DIJ_RINGZERO
        # END IF  DIRECTINPUT_VERSION >= 0x0700

        if DIRECTINPUT_VERSION >= 0x0800:
            if not defined(DIJ_RINGZERO):
                IDirectInputDevice8W = INTERFACE('IDirectInputDevice8W')
                IDirectInputDevice8W._iid_ = IID_IDirectInputDevice8W
                DECLARE_INTERFACE_(IDirectInputDevice8W, comtypes.IUnknown)(
                    # * IUnknown methods *
                    # * IDirectInputDevice8W methods
                    STDMETHOD('GetCapabilities')((LPDIDEVCAPS,)),
                    STDMETHOD('EnumObjects')(
                        (LPDIENUMDEVICEOBJECTSCALLBACKW, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetProperty')((REFGUID, LPDIPROPHEADER)),
                    STDMETHOD('SetProperty')((REFGUID, LPCDIPROPHEADER)),
                    STDMETHOD(Acquire)(),
                    STDMETHOD(Unacquire)(),
                    STDMETHOD('GetDeviceState')((DWORD, LPVOID)),
                    STDMETHOD('GetDeviceData')(
                        (DWORD, LPDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                    ),
                    STDMETHOD('SetDataFormat')((LPCDIDATAFORMAT,)),
                    STDMETHOD('SetEventNotification')((HANDLE,)),
                    STDMETHOD('SetCooperativeLevel')((HWND, DWORD)),
                    STDMETHOD('GetObjectInfo')(
                        (LPDIDEVICEOBJECTINSTANCEW, DWORD, DWORD)
                    ),
                    STDMETHOD('GetDeviceInfo')((LPDIDEVICEINSTANCEW,)),
                    STDMETHOD('RunControlPanel')((HWND, DWORD)),
                    STDMETHOD('Initialize')((HINSTANCE, DWORD, REFGUID)),
                    STDMETHOD('CreateEffect')(
                        (
                            REFGUID,
                            LPCDIEFFECT,
                            POINTER(LPDIRECTINPUTEFFECT),
                            LPUNKNOWN
                        )
                    ),
                    STDMETHOD('EnumEffects')(
                        (LPDIENUMEFFECTSCALLBACKW, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetEffectInfo')((LPDIEFFECTINFOW, REFGUID)),
                    STDMETHOD('GetForceFeedbackState')((LPDWORD,)),
                    STDMETHOD('SendForceFeedbackCommand')((DWORD,)),
                    STDMETHOD('EnumCreatedEffectObjects')(
                        (LPDIENUMCREATEDEFFECTOBJECTSCALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('Escape')((LPDIEFFESCAPE,)),
                    STDMETHOD(Poll)(),
                    STDMETHOD('SendDeviceData')(
                        (DWORD, LPCDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                    ),
                    STDMETHOD('EnumEffectsInFile')(
                        (LPCWSTR, LPDIENUMEFFECTSINFILECALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('WriteEffectToFile')(
                        (LPCWSTR, DWORD, LPDIFILEEFFECT, DWORD)
                    ),
                    STDMETHOD('BuildActionMap')(
                        (LPDIACTIONFORMATW, LPCWSTR, DWORD)
                    ),
                    STDMETHOD('SetActionMap')(
                        (LPDIACTIONFORMATW, LPCWSTR, DWORD)
                    ),
                    STDMETHOD('GetImageInfo')((LPDIDEVICEIMAGEINFOHEADERW,)),
                )

                LPDIRECTINPUTDEVICE8W = POINTER(IDirectInputDevice8W)

                IDirectInputDevice8A = INTERFACE('IDirectInputDevice8A')
                IDirectInputDevice8A._iid_ = IID_IDirectInputDevice8A
                DECLARE_INTERFACE_(IDirectInputDevice8A, comtypes.IUnknown)(
                    # * IUnknown methods *
                    # * IDirectInputDevice8A methods
                    STDMETHOD('GetCapabilities')((LPDIDEVCAPS,)),
                    STDMETHOD('EnumObjects')(
                        (LPDIENUMDEVICEOBJECTSCALLBACKA, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetProperty')((REFGUID, LPDIPROPHEADER)),
                    STDMETHOD('SetProperty')((REFGUID, LPCDIPROPHEADER)),
                    STDMETHOD(Acquire)(),
                    STDMETHOD(Unacquire)(),
                    STDMETHOD('GetDeviceState')((DWORD, LPVOID)),
                    STDMETHOD('GetDeviceData')(
                        (DWORD, LPDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                    ),
                    STDMETHOD('SetDataFormat')((LPCDIDATAFORMAT,)),
                    STDMETHOD('SetEventNotification')((HANDLE,)),
                    STDMETHOD('SetCooperativeLevel')((HWND, DWORD)),
                    STDMETHOD('GetObjectInfo')(
                        (LPDIDEVICEOBJECTINSTANCEA, DWORD, DWORD)
                    ),
                    STDMETHOD('GetDeviceInfo')((LPDIDEVICEINSTANCEA,)),
                    STDMETHOD('RunControlPanel')((HWND, DWORD)),
                    STDMETHOD('Initialize')((HINSTANCE, DWORD, REFGUID)),
                    STDMETHOD('CreateEffect')(
                        (
                            REFGUID,
                            LPCDIEFFECT,
                            POINTER(LPDIRECTINPUTEFFECT),
                            LPUNKNOWN
                        )
                    ),
                    STDMETHOD('EnumEffects')(
                        (LPDIENUMEFFECTSCALLBACKA, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetEffectInfo')((LPDIEFFECTINFOA, REFGUID)),
                    STDMETHOD('GetForceFeedbackState')((LPDWORD,)),
                    STDMETHOD('SendForceFeedbackCommand')((DWORD,)),
                    STDMETHOD('EnumCreatedEffectObjects')(
                        (LPDIENUMCREATEDEFFECTOBJECTSCALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('Escape')((LPDIEFFESCAPE,)),
                    STDMETHOD(Poll)(),
                    STDMETHOD('SendDeviceData')(
                        (DWORD, LPCDIDEVICEOBJECTDATA, LPDWORD, DWORD)
                    ),
                    STDMETHOD('EnumEffectsInFile')(
                        (LPCSTR, LPDIENUMEFFECTSINFILECALLBACK, LPVOID, DWORD)
                    ),
                    STDMETHOD('WriteEffectToFile')(
                        (LPCSTR, DWORD, LPDIFILEEFFECT, DWORD)
                    ),
                    STDMETHOD('BuildActionMap')(
                        (LPDIACTIONFORMATW, LPCSTR, DWORD)
                    ),
                    STDMETHOD('SetActionMap')(
                        (LPDIACTIONFORMATA, LPCSTR, DWORD)
                    ),
                    STDMETHOD('GetImageInfo')((LPDIDEVICEIMAGEINFOHEADERA,)),
                )

                LPDIRECTINPUTDEVICE8A = POINTER(IDirectInputDevice8A)

                if defined(UNICODE):
                    IID_IDirectInputDevice8 = IID_IDirectInputDevice8W
                    IDirectInputDevice8 = IDirectInputDevice8W
                    IDirectInputDevice8Vtbl = IDirectInputDevice8WVtbl
                else:
                    IID_IDirectInputDevice8 = IID_IDirectInputDevice8A
                    IDirectInputDevice8 = IDirectInputDevice8A
                    IDirectInputDevice8Vtbl = IDirectInputDevice8AVtbl
                # END IF

                LPDIRECTINPUTDEVICE8 = POINTER(IDirectInputDevice8)

                if not defined(__cplusplus) or defined(CINTERFACE):
                    def IDirectInputDevice8_QueryInterface(p, a, b):
                        return p.lpVtbl.QueryInterface(p, a, b)


                    def IDirectInputDevice8_AddRef(p):
                        return p.lpVtbl.AddRef(p)


                    def IDirectInputDevice8_Release(p):
                        return p.lpVtbl.Release(p)


                    def IDirectInputDevice8_GetCapabilities(p, a):
                        return p.lpVtbl.GetCapabilities(p, a)


                    def IDirectInputDevice8_EnumObjects(p, a, b, c):
                        return p.lpVtbl.EnumObjects(p, a, b, c)


                    def IDirectInputDevice8_GetProperty(p, a, b):
                        return p.lpVtbl.GetProperty(p, a, b)


                    def IDirectInputDevice8_SetProperty(p, a, b):
                        return p.lpVtbl.SetProperty(p, a, b)


                    def IDirectInputDevice8_Acquire(p):
                        return p.lpVtbl.Acquire(p)


                    def IDirectInputDevice8_Unacquire(p):
                        return p.lpVtbl.Unacquire(p)


                    def IDirectInputDevice8_GetDeviceState(p, a, b):
                        return p.lpVtbl.GetDeviceState(p, a, b)


                    def IDirectInputDevice8_GetDeviceData(p, a, b, c, d):
                        return p.lpVtbl.GetDeviceData(p, a, b, c, d)


                    def IDirectInputDevice8_SetDataFormat(p, a):
                        return p.lpVtbl.SetDataFormat(p, a)


                    def IDirectInputDevice8_SetEventNotification(p, a):
                        return p.lpVtbl.SetEventNotification(p, a)


                    def IDirectInputDevice8_SetCooperativeLevel(p, a, b):
                        return p.lpVtbl.SetCooperativeLevel(p, a, b)


                    def IDirectInputDevice8_GetObjectInfo(p, a, b, c):
                        return p.lpVtbl.GetObjectInfo(p, a, b, c)


                    def IDirectInputDevice8_GetDeviceInfo(p, a):
                        return p.lpVtbl.GetDeviceInfo(p, a)


                    def IDirectInputDevice8_RunControlPanel(p, a, b):
                        return p.lpVtbl.RunControlPanel(p, a, b)


                    def IDirectInputDevice8_Initialize(p, a, b, c):
                        return p.lpVtbl.Initialize(p, a, b, c)


                    def IDirectInputDevice8_CreateEffect(p, a, b, c, d):
                        return p.lpVtbl.CreateEffect(p, a, b, c, d)


                    def IDirectInputDevice8_EnumEffects(p, a, b, c):
                        return p.lpVtbl.EnumEffects(p, a, b, c)


                    def IDirectInputDevice8_GetEffectInfo(p, a, b):
                        return p.lpVtbl.GetEffectInfo(p, a, b)


                    def IDirectInputDevice8_GetForceFeedbackState(p, a):
                        return p.lpVtbl.GetForceFeedbackState(p, a)


                    def IDirectInputDevice8_SendForceFeedbackCommand(p, a):
                        return p.lpVtbl.SendForceFeedbackCommand(p, a)


                    def IDirectInputDevice8_EnumCreatedEffectObjects(p, a, b, c):
                        return p.lpVtbl.EnumCreatedEffectObjects(p, a, b, c)


                    def IDirectInputDevice8_Escape(p, a):
                        return p.lpVtbl.Escape(p, a)


                    def IDirectInputDevice8_Poll(p):
                        return p.lpVtbl.Poll(p)


                    def IDirectInputDevice8_SendDeviceData(p, a, b, c, d):
                        return p.lpVtbl.SendDeviceData(p, a, b, c, d)


                    def IDirectInputDevice8_EnumEffectsInFile(p, a, b, c, d):
                        return p.lpVtbl.EnumEffectsInFile(p, a, b, c, d)


                    def IDirectInputDevice8_WriteEffectToFile(p, a, b, c, d):
                        return p.lpVtbl.WriteEffectToFile(p, a, b, c, d)


                    def IDirectInputDevice8_BuildActionMap(p, a, b, c):
                        return p.lpVtbl.BuildActionMap(p, a, b, c)


                    def IDirectInputDevice8_SetActionMap(p, a, b, c):
                        return p.lpVtbl.SetActionMap(p, a, b, c)


                    def IDirectInputDevice8_GetImageInfo(p, a):
                        return p.lpVtbl.GetImageInfo(p, a)
                else:
                    def IDirectInputDevice8_QueryInterface(p, a, b):
                        return p.QueryInterface(a, b)


                    def IDirectInputDevice8_AddRef(p):
                        return p.AddRef()


                    def IDirectInputDevice8_Release(p):
                        return p.Release()


                    def IDirectInputDevice8_GetCapabilities(p, a):
                        return p.GetCapabilities(a)


                    def IDirectInputDevice8_EnumObjects(p, a, b, c):
                        return p.EnumObjects(a, b, c)


                    def IDirectInputDevice8_GetProperty(p, a, b):
                        return p.GetProperty(a, b)


                    def IDirectInputDevice8_SetProperty(p, a, b):
                        return p.SetProperty(a, b)


                    def IDirectInputDevice8_Acquire(p):
                        return p.Acquire()


                    def IDirectInputDevice8_Unacquire(p):
                        return p.Unacquire()


                    def IDirectInputDevice8_GetDeviceState(p, a, b):
                        return p.GetDeviceState(a, b)


                    def IDirectInputDevice8_GetDeviceData(p, a, b, c, d):
                        return p.GetDeviceData(a, b, c, d)


                    def IDirectInputDevice8_SetDataFormat(p, a):
                        return p.SetDataFormat(a)


                    def IDirectInputDevice8_SetEventNotification(p, a):
                        return p.SetEventNotification(a)


                    def IDirectInputDevice8_SetCooperativeLevel(p, a, b):
                        return p.SetCooperativeLevel(a, b)


                    def IDirectInputDevice8_GetObjectInfo(p, a, b, c):
                        return p.GetObjectInfo(a, b, c)


                    def IDirectInputDevice8_GetDeviceInfo(p, a):
                        return p.GetDeviceInfo(a)


                    def IDirectInputDevice8_RunControlPanel(p, a, b):
                        return p.RunControlPanel(a, b)


                    def IDirectInputDevice8_Initialize(p, a, b, c):
                        return p.Initialize(a, b, c)


                    def IDirectInputDevice8_CreateEffect(p, a, b, c, d):
                        return p.CreateEffect(a, b, c, d)


                    def IDirectInputDevice8_EnumEffects(p, a, b, c):
                        return p.EnumEffects(a, b, c)


                    def IDirectInputDevice8_GetEffectInfo(p, a, b):
                        return p.GetEffectInfo(a, b)


                    def IDirectInputDevice8_GetForceFeedbackState(p, a):
                        return p.GetForceFeedbackState(a)


                    def IDirectInputDevice8_SendForceFeedbackCommand(p, a):
                        return p.SendForceFeedbackCommand(a)


                    def IDirectInputDevice8_EnumCreatedEffectObjects(p, a, b, c):
                        return p.EnumCreatedEffectObjects(a, b, c)


                    def IDirectInputDevice8_Escape(p, a):
                        return p.Escape(a)


                    def IDirectInputDevice8_Poll(p):
                        return p.Poll()


                    def IDirectInputDevice8_SendDeviceData(p, a, b, c, d):
                        return p.SendDeviceData(a, b, c, d)


                    def IDirectInputDevice8_EnumEffectsInFile(p, a, b, c, d):
                        return p.EnumEffectsInFile(a, b, c, d)


                    def IDirectInputDevice8_WriteEffectToFile(p, a, b, c, d):
                        return p.WriteEffectToFile(a, b, c, d)


                    def IDirectInputDevice8_BuildActionMap(p, a, b, c):
                        return p.BuildActionMap(a, b, c)


                    def IDirectInputDevice8_SetActionMap(p, a, b, c):
                        return p.SetActionMap(a, b, c)


                    def IDirectInputDevice8_GetImageInfo(p, a):
                        return p.GetImageInfo(a)
                # END IF
            # END IF  DIJ_RINGZERO
        # END IF  DIRECTINPUT_VERSION >= 0x0800

        # *********************************************************************
        # Mouse
        # *********************************************************************

        if not defined(DIJ_RINGZERO):
            _DIMOUSESTATE._fields_ = [
                ('lX', LONG),
                ('lY', LONG),
                ('lZ', LONG),
                ('rgbButtons', BYTE * 4),
            ]

            if DIRECTINPUT_VERSION >= 0x0700:
                _DIMOUSESTATE2._fields_ = [
                    ('lX', LONG),
                    ('lY', LONG),
                    ('lZ', LONG),
                    ('rgbButtons', BYTE * 8),
                ]
            # END IF

            DIMOFS_X = FIELD_OFFSET(DIMOUSESTATE, 'lX')
            DIMOFS_Y = FIELD_OFFSET(DIMOUSESTATE, 'lY')
            DIMOFS_Z = FIELD_OFFSET(DIMOUSESTATE, 'lZ')
            DIMOFS_BUTTON0 = FIELD_OFFSET(DIMOUSESTATE, 'rgbButtons') + 0
            DIMOFS_BUTTON1 = FIELD_OFFSET(DIMOUSESTATE, 'rgbButtons') + 1
            DIMOFS_BUTTON2 = FIELD_OFFSET(DIMOUSESTATE, 'rgbButtons') + 2
            DIMOFS_BUTTON3 = FIELD_OFFSET(DIMOUSESTATE, 'rgbButtons') + 3

            if DIRECTINPUT_VERSION >= 0x0700:
                DIMOFS_BUTTON4 = FIELD_OFFSET(DIMOUSESTATE2, 'rgbButtons') + 4
                DIMOFS_BUTTON5 = FIELD_OFFSET(DIMOUSESTATE2, 'rgbButtons') + 5
                DIMOFS_BUTTON6 = FIELD_OFFSET(DIMOUSESTATE2, 'rgbButtons') + 6
                DIMOFS_BUTTON7 = FIELD_OFFSET(DIMOUSESTATE2, 'rgbButtons') + 7
            # END IF
        # END IF  DIJ_RINGZERO

        # *********************************************************************
        # Keyboard
        # *********************************************************************

        if not defined(DIJ_RINGZERO):
            # *****************************************************************
            # DirectInput keyboard scan codes
            # *****************************************************************

            # Copyright (C) Microsoft. All rights reserved.
            DIK_ESCAPE = 0x01
            DIK_1 = 0x02
            DIK_2 = 0x03
            DIK_3 = 0x04
            DIK_4 = 0x05
            DIK_5 = 0x06
            DIK_6 = 0x07
            DIK_7 = 0x08
            DIK_8 = 0x09
            DIK_9 = 0x0A
            DIK_0 = 0x0B
            DIK_MINUS = 0x0C            # - on main keyboard
            DIK_EQUALS = 0x0D
            DIK_BACK = 0x0E            # backspace
            DIK_TAB = 0x0F
            DIK_Q = 0x10
            DIK_W = 0x11
            DIK_E = 0x12
            DIK_R = 0x13
            DIK_T = 0x14
            DIK_Y = 0x15
            DIK_U = 0x16
            DIK_I = 0x17
            DIK_O = 0x18
            DIK_P = 0x19
            DIK_LBRACKET = 0x1A
            DIK_RBRACKET = 0x1B
            DIK_RETURN = 0x1C            # Enter on main keyboard
            DIK_LCONTROL = 0x1D
            DIK_A = 0x1E
            DIK_S = 0x1F
            DIK_D = 0x20
            DIK_F = 0x21
            DIK_G = 0x22
            DIK_H = 0x23
            DIK_J = 0x24
            DIK_K = 0x25
            DIK_L = 0x26
            DIK_SEMICOLON = 0x27
            DIK_APOSTROPHE = 0x28
            DIK_GRAVE = 0x29            # accent grave
            DIK_LSHIFT = 0x2A
            DIK_BACKSLASH = 0x2B
            DIK_Z = 0x2C
            DIK_X = 0x2D
            DIK_C = 0x2E
            DIK_V = 0x2F
            DIK_B = 0x30
            DIK_N = 0x31
            DIK_M = 0x32
            DIK_COMMA = 0x33
            DIK_PERIOD = 0x34            # . on main keyboard
            DIK_SLASH = 0x35            # / on main keyboard
            DIK_RSHIFT = 0x36
            DIK_MULTIPLY = 0x37            # * on numeric keypad
            DIK_LMENU = 0x38            # left Alt
            DIK_SPACE = 0x39
            DIK_CAPITAL = 0x3A
            DIK_F1 = 0x3B
            DIK_F2 = 0x3C
            DIK_F3 = 0x3D
            DIK_F4 = 0x3E
            DIK_F5 = 0x3F
            DIK_F6 = 0x40
            DIK_F7 = 0x41
            DIK_F8 = 0x42
            DIK_F9 = 0x43
            DIK_F10 = 0x44
            DIK_NUMLOCK = 0x45
            DIK_SCROLL = 0x46            # Scroll Lock
            DIK_NUMPAD7 = 0x47
            DIK_NUMPAD8 = 0x48
            DIK_NUMPAD9 = 0x49
            DIK_SUBTRACT = 0x4A            # - on numeric keypad
            DIK_NUMPAD4 = 0x4B
            DIK_NUMPAD5 = 0x4C
            DIK_NUMPAD6 = 0x4D
            DIK_ADD = 0x4E            # + on numeric keypad
            DIK_NUMPAD1 = 0x4F
            DIK_NUMPAD2 = 0x50
            DIK_NUMPAD3 = 0x51
            DIK_NUMPAD0 = 0x52
            DIK_DECIMAL = 0x53            # . on numeric keypad
            DIK_OEM_102 = 0x56            # <> or \| on RT 102-key keyboard (Non-U.S.)
            DIK_F11 = 0x57
            DIK_F12 = 0x58
            DIK_F13 = 0x64            # (NEC PC98)
            DIK_F14 = 0x65            # (NEC PC98)
            DIK_F15 = 0x66            # (NEC PC98)
            DIK_KANA = 0x70            # (Japanese keyboard)
            DIK_ABNT_C1 = 0x73            # /? on Brazilian keyboard
            DIK_CONVERT = 0x79            # (Japanese keyboard)
            DIK_NOCONVERT = 0x7B            # (Japanese keyboard)
            DIK_YEN = 0x7D            # (Japanese keyboard)
            DIK_ABNT_C2 = 0x7E            # Numpad . on Brazilian keyboard
            DIK_NUMPADEQUALS = 0x8D            # = on numeric keypad (NEC PC98)
            DIK_PREVTRACK = 0x90            # Previous Track (DIK_CIRCUMFLEX on Japanese keyboard)
            DIK_AT = 0x91            # (NEC PC98)
            DIK_COLON = 0x92            # (NEC PC98)
            DIK_UNDERLINE = 0x93            # (NEC PC98)
            DIK_KANJI = 0x94            # (Japanese keyboard)
            DIK_STOP = 0x95            # (NEC PC98)
            DIK_AX = 0x96            # (Japan AX)
            DIK_UNLABELED = 0x97            # (J3100)
            DIK_NEXTTRACK = 0x99            # Next Track
            DIK_NUMPADENTER = 0x9C            # Enter on numeric keypad
            DIK_RCONTROL = 0x9D
            DIK_MUTE = 0xA0            # Mute
            DIK_CALCULATOR = 0xA1            # Calculator
            DIK_PLAYPAUSE = 0xA2            # Play / Pause
            DIK_MEDIASTOP = 0xA4            # Media Stop
            DIK_VOLUMEDOWN = 0xAE            # Volume -
            DIK_VOLUMEUP = 0xB0            # Volume +
            DIK_WEBHOME = 0xB2            # Web home
            DIK_NUMPADCOMMA = 0xB3            # , on numeric keypad (NEC PC98)
            DIK_DIVIDE = 0xB5            # / on numeric keypad
            DIK_SYSRQ = 0xB7
            DIK_RMENU = 0xB8            # right Alt
            DIK_PAUSE = 0xC5            # Pause
            DIK_HOME = 0xC7            # Home on arrow keypad
            DIK_UP = 0xC8            # UpArrow on arrow keypad
            DIK_PRIOR = 0xC9            # PgUp on arrow keypad
            DIK_LEFT = 0xCB            # LeftArrow on arrow keypad
            DIK_RIGHT = 0xCD            # RightArrow on arrow keypad
            DIK_END = 0xCF            # End on arrow keypad
            DIK_DOWN = 0xD0            # DownArrow on arrow keypad
            DIK_NEXT = 0xD1            # PgDn on arrow keypad
            DIK_INSERT = 0xD2            # Insert on arrow keypad
            DIK_DELETE = 0xD3            # Delete on arrow keypad
            DIK_LWIN = 0xDB            # Left Windows key
            DIK_RWIN = 0xDC            # Right Windows key
            DIK_APPS = 0xDD            # AppMenu key
            DIK_POWER = 0xDE            # System Power
            DIK_SLEEP = 0xDF            # System Sleep
            DIK_WAKE = 0xE3            # System Wake
            DIK_WEBSEARCH = 0xE5            # Web Search
            DIK_WEBFAVORITES = 0xE6            # Web Favorites
            DIK_WEBREFRESH = 0xE7            # Web Refresh
            DIK_WEBSTOP = 0xE8            # Web Stop
            DIK_WEBFORWARD = 0xE9            # Web Forward
            DIK_WEBBACK = 0xEA            # Web Back
            DIK_MYCOMPUTER = 0xEB            # My Computer
            DIK_MAIL = 0xEC            # Mail
            DIK_MEDIASELECT = 0xED            # Media Select

            # /* Alternate names for keys, to facilitate transition from DOS.
            DIK_BACKSPACE = DIK_BACK            # backspace
            DIK_NUMPADSTAR = DIK_MULTIPLY            # * on numeric keypad
            DIK_LALT = DIK_LMENU            # left Alt
            DIK_CAPSLOCK = DIK_CAPITAL            # CapsLock
            DIK_NUMPADMINUS = DIK_SUBTRACT            # - on numeric keypad
            DIK_NUMPADPLUS = DIK_ADD            # + on numeric keypad
            DIK_NUMPADPERIOD = DIK_DECIMAL            # . on numeric keypad
            DIK_NUMPADSLASH = DIK_DIVIDE            # / on numeric keypad
            DIK_RALT = DIK_RMENU            # right Alt
            DIK_UPARROW = DIK_UP            # UpArrow on arrow keypad
            DIK_PGUP = DIK_PRIOR            # PgUp on arrow keypad
            DIK_LEFTARROW = DIK_LEFT            # LeftArrow on arrow keypad
            DIK_RIGHTARROW = DIK_RIGHT            # RightArrow on arrow keypad
            DIK_DOWNARROW = DIK_DOWN            # DownArrow on arrow keypad
            DIK_PGDN = DIK_NEXT            # PgDn on arrow keypad

            # /* Alternate names for keys originally not used on US keyboards.
            DIK_CIRCUMFLEX = DIK_PREVTRACK            # Japanese keyboard
        # END IF  DIJ_RINGZERO

        # *********************************************************************
        # Joystick
        # *********************************************************************

        if not defined(DIJ_RINGZERO):
            # x-axis position
            DIJOYSTATE._fields_ = [
                ('lX', LONG),
                # y-axis position
                ('lY', LONG),
                # z-axis position
                ('lZ', LONG),
                # x-axis rotation
                ('lRx', LONG),
                # y-axis rotation
                ('lRy', LONG),
                # z-axis rotation
                ('lRz', LONG),
                # extra axes positions
                ('rglSlider', LONG * 2),
                # POV directions
                ('rgdwPOV', DWORD * 4),
                # 32 buttons
                ('rgbButtons', BYTE * 32),
            ]

            # x-axis position
            DIJOYSTATE2._fields_ = [
                ('lX', LONG),
                # y-axis position
                ('lY', LONG),
                # z-axis position
                ('lZ', LONG),
                # x-axis rotation
                ('lRx', LONG),
                # y-axis rotation
                ('lRy', LONG),
                # z-axis rotation
                ('lRz', LONG),
                # extra axes positions
                ('rglSlider', LONG * 2),
                # POV directions
                ('rgdwPOV', DWORD * 4),
                # 128 buttons
                ('rgbButtons', BYTE * 128),
                # x-axis velocity
                ('lVX', LONG),
                # y-axis velocity
                ('lVY', LONG),
                # z-axis velocity
                ('lVZ', LONG),
                # x-axis angular velocity
                ('lVRx', LONG),
                # y-axis angular velocity
                ('lVRy', LONG),
                # z-axis angular velocity
                ('lVRz', LONG),
                # extra axes velocities
                ('rglVSlider', LONG * 2),
                # x-axis acceleration
                ('lAX', LONG),
                # y-axis acceleration
                ('lAY', LONG),
                # z-axis acceleration
                ('lAZ', LONG),
                # x-axis angular acceleration
                ('lARx', LONG),
                # y-axis angular acceleration
                ('lARy', LONG),
                # z-axis angular acceleration
                ('lARz', LONG),
                # extra axes accelerations
                ('rglASlider', LONG * 2),
                # x-axis force
                ('lFX', LONG),
                # y-axis force
                ('lFY', LONG),
                # z-axis force
                ('lFZ', LONG),
                # x-axis torque
                ('lFRx', LONG),
                # y-axis torque
                ('lFRy', LONG),
                # z-axis torque
                ('lFRz', LONG),
                # extra axes forces
                ('rglFSlider', LONG * 2),
            ]
            DIJOFS_X = FIELD_OFFSET(DIJOYSTATE, 'lX')
            DIJOFS_Y = FIELD_OFFSET(DIJOYSTATE, 'lY')
            DIJOFS_Z = FIELD_OFFSET(DIJOYSTATE, 'lZ')
            DIJOFS_RX = FIELD_OFFSET(DIJOYSTATE, 'lRx')
            DIJOFS_RY = FIELD_OFFSET(DIJOYSTATE, 'lRy')
            DIJOFS_RZ = FIELD_OFFSET(DIJOYSTATE, 'lRz')


            def DIJOFS_SLIDER(n):
                return (
                    FIELD_OFFSET(DIJOYSTATE, rglSlider) +
                    n *
                    ctypes.sizeof(LONG)
                )


            def DIJOFS_POV(n):
                return (
                    FIELD_OFFSET(DIJOYSTATE, rgdwPOV) +
                    n *
                    ctypes.sizeof(DWORD)
                )


            def DIJOFS_BUTTON(n):
                return FIELD_OFFSET(DIJOYSTATE, rgbButtons) + n


            DIJOFS_BUTTON0 = DIJOFS_BUTTON(0)
            DIJOFS_BUTTON1 = DIJOFS_BUTTON(1)
            DIJOFS_BUTTON2 = DIJOFS_BUTTON(2)
            DIJOFS_BUTTON3 = DIJOFS_BUTTON(3)
            DIJOFS_BUTTON4 = DIJOFS_BUTTON(4)
            DIJOFS_BUTTON5 = DIJOFS_BUTTON(5)
            DIJOFS_BUTTON6 = DIJOFS_BUTTON(6)
            DIJOFS_BUTTON7 = DIJOFS_BUTTON(7)
            DIJOFS_BUTTON8 = DIJOFS_BUTTON(8)
            DIJOFS_BUTTON9 = DIJOFS_BUTTON(9)
            DIJOFS_BUTTON10 = DIJOFS_BUTTON(10)
            DIJOFS_BUTTON11 = DIJOFS_BUTTON(11)
            DIJOFS_BUTTON12 = DIJOFS_BUTTON(12)
            DIJOFS_BUTTON13 = DIJOFS_BUTTON(13)
            DIJOFS_BUTTON14 = DIJOFS_BUTTON(14)
            DIJOFS_BUTTON15 = DIJOFS_BUTTON(15)
            DIJOFS_BUTTON16 = DIJOFS_BUTTON(16)
            DIJOFS_BUTTON17 = DIJOFS_BUTTON(17)
            DIJOFS_BUTTON18 = DIJOFS_BUTTON(18)
            DIJOFS_BUTTON19 = DIJOFS_BUTTON(19)
            DIJOFS_BUTTON20 = DIJOFS_BUTTON(20)
            DIJOFS_BUTTON21 = DIJOFS_BUTTON(21)
            DIJOFS_BUTTON22 = DIJOFS_BUTTON(22)
            DIJOFS_BUTTON23 = DIJOFS_BUTTON(23)
            DIJOFS_BUTTON24 = DIJOFS_BUTTON(24)
            DIJOFS_BUTTON25 = DIJOFS_BUTTON(25)
            DIJOFS_BUTTON26 = DIJOFS_BUTTON(26)
            DIJOFS_BUTTON27 = DIJOFS_BUTTON(27)
            DIJOFS_BUTTON28 = DIJOFS_BUTTON(28)
            DIJOFS_BUTTON29 = DIJOFS_BUTTON(29)
            DIJOFS_BUTTON30 = DIJOFS_BUTTON(30)
            DIJOFS_BUTTON31 = DIJOFS_BUTTON(31)
        # END IF  DIJ_RINGZERO
        # *********************************************************************
        # IDirectInput
        # *********************************************************************

        if not defined(DIJ_RINGZERO):
            DIENUM_STOP = 0
            DIENUM_CONTINUE = 1

            # typedef BOOL (FAR PASCAL * LPDIENUMDEVICESCALLBACKA)(
            # LPCDIDEVICEINSTANCEA,
            # LPVOID
            # );
            LPDIENUMDEVICESCALLBACKA = PASCAL(
                BOOL,
                LPCDIDEVICEINSTANCEA,
                LPVOID
            )

            # typedef BOOL (FAR PASCAL * LPDIENUMDEVICESCALLBACKW)(
            # LPCDIDEVICEINSTANCEW,
            #  LPVOID
            # );
            LPDIENUMDEVICESCALLBACKW = PASCAL(
                BOOL,
                LPCDIDEVICEINSTANCEW,
                LPVOID
            )

            if defined(UNICODE):
                LPDIENUMDEVICESCALLBACK = LPDIENUMDEVICESCALLBACKW
            else:
                LPDIENUMDEVICESCALLBACK = LPDIENUMDEVICESCALLBACKA
            # END IF   not UNICODE

            # typedef BOOL (FAR PASCAL * LPDICONFIGUREDEVICESCALLBACK)(
            # IUnknown FAR *,
            #  LPVOID
            # );
            LPDICONFIGUREDEVICESCALLBACK = PASCAL(
                BOOL,
                POINTER(IUnknown),
                LPVOID
            )

            DIEDFL_ALLDEVICES = 0x00000000
            DIEDFL_ATTACHEDONLY = 0x00000001

            if DIRECTINPUT_VERSION >= 0x0500:
                DIEDFL_FORCEFEEDBACK = 0x00000100
            # END IF  DIRECTINPUT_VERSION >= 0x0500

            if DIRECTINPUT_VERSION >= 0x050a:
                DIEDFL_INCLUDEALIASES = 0x00010000
                DIEDFL_INCLUDEPHANTOMS = 0x00020000
            # END IF  DIRECTINPUT_VERSION >= 0x050a

            if DIRECTINPUT_VERSION >= 0x0800:
                DIEDFL_INCLUDEHIDDEN = 0x00040000
            # END IF  DIRECTINPUT_VERSION >= 0x0800

            if DIRECTINPUT_VERSION >= 0x0800:
                # typedef BOOL (FAR PASCAL * LPDIENUMDEVICESBYSEMANTICSCBA)(
                # LPCDIDEVICEINSTANCEA,
                # LPDIRECTINPUTDEVICE8A,
                # DWORD,
                # DWORD,
                # LPVOID
                # );
                LPDIENUMDEVICESBYSEMANTICSCBA = PASCAL(
                    BOOL,
                    LPCDIDEVICEINSTANCEA,
                    LPDIRECTINPUTDEVICE8A,
                    DWORD,
                    DWORD,
                    LPVOID
                )

                # typedef BOOL (FAR PASCAL * LPDIENUMDEVICESBYSEMANTICSCBW)(
                # LPCDIDEVICEINSTANCEW,
                # LPDIRECTINPUTDEVICE8W,
                # DWORD,
                #  DWORD,
                # LPVOID
                # );
                LPDIENUMDEVICESBYSEMANTICSCBW = PASCAL(
                    BOOL,
                    LPCDIDEVICEINSTANCEW,
                    LPDIRECTINPUTDEVICE8W,
                    DWORD,
                    DWORD,
                    LPVOID
                )

                if defined(UNICODE):
                    LPDIENUMDEVICESBYSEMANTICSCB = (
                        LPDIENUMDEVICESBYSEMANTICSCBW
                    )
                else:
                    LPDIENUMDEVICESBYSEMANTICSCB = (
                        LPDIENUMDEVICESBYSEMANTICSCBA
                    )
                # END IF   not UNICODE
            # END IF  DIRECTINPUT_VERSION >= 0x0800

            if DIRECTINPUT_VERSION >= 0x0800:
                DIEDBS_MAPPEDPRI1 = 0x00000001
                DIEDBS_MAPPEDPRI2 = 0x00000002
                DIEDBS_RECENTDEVICE = 0x00000010
                DIEDBS_NEWDEVICE = 0x00000020
            # END IF  DIRECTINPUT_VERSION >= 0x0800

            if DIRECTINPUT_VERSION >= 0x0800:
                DIEDBSFL_ATTACHEDONLY = 0x00000000
                DIEDBSFL_THISUSER = 0x00000010
                DIEDBSFL_FORCEFEEDBACK = DIEDFL_FORCEFEEDBACK
                DIEDBSFL_AVAILABLEDEVICES = 0x00001000
                DIEDBSFL_MULTIMICEKEYBOARDS = 0x00002000
                DIEDBSFL_NONGAMINGDEVICES = 0x00004000
                DIEDBSFL_VALID = 0x00007110
            # END IF  DIRECTINPUT_VERSION >= 0x0800

            IDirectInputW = INTERFACE('IDirectInputW')
            IDirectInputW._iid_ = IID_IDirectInputW
            DECLARE_INTERFACE_(IDirectInputW, comtypes.IUnknown)(
                # * IUnknown methods *
                # * IDirectInputW methods
                STDMETHOD('CreateDevice')(
                    (REFGUID, POINTER(LPDIRECTINPUTDEVICEW), LPUNKNOWN)
                ),
                STDMETHOD('EnumDevices')(
                    (DWORD, LPDIENUMDEVICESCALLBACKW, LPVOID, DWORD)
                ),
                STDMETHOD('GetDeviceStatus')((REFGUID,)),
                STDMETHOD('RunControlPanel')((HWND, DWORD)),
                STDMETHOD('Initialize')((HINSTANCE, DWORD)),
            )

            LPDIRECTINPUTW = POINTER(IDirectInputW)

            IDirectInputA = INTERFACE('IDirectInputA')
            IDirectInputA._iid_ = IID_IDirectInputA
            DECLARE_INTERFACE_(IDirectInputA, comtypes.IUnknown)(
                # * IUnknown methods *
                # * IDirectInputA methods
                STDMETHOD('CreateDevice')(
                    (REFGUID, POINTER(LPDIRECTINPUTDEVICEA), LPUNKNOWN)
                ),
                STDMETHOD('EnumDevices')(
                    (DWORD, LPDIENUMDEVICESCALLBACKA, LPVOID, DWORD)
                ),
                STDMETHOD('GetDeviceStatus')((REFGUID,)),
                STDMETHOD('RunControlPanel')((HWND, DWORD)),
                STDMETHOD('Initialize')((HINSTANCE, DWORD)),
            )

            LPDIRECTINPUTA = POINTER(IDirectInputA)

            if defined(UNICODE):
                IID_IDirectInput = IID_IDirectInputW
                IDirectInput = IDirectInputW
                IDirectInputVtbl = IDirectInputWVtbl
            else:
                IID_IDirectInput = IID_IDirectInputA
                IDirectInput = IDirectInputA
                IDirectInputVtbl = IDirectInputAVtbl
            # END IF

            LPDIRECTINPUT = POINTER(IDirectInput)

            if not defined(__cplusplus) or defined(CINTERFACE):
                def IDirectInput_QueryInterface(p, a, b):
                    return p.lpVtbl.QueryInterface(p, a, b)


                def IDirectInput_AddRef(p):
                    return p.lpVtbl.AddRef(p)


                def IDirectInput_Release(p):
                    return p.lpVtbl.Release(p)


                def IDirectInput_CreateDevice(p, a, b, c):
                    return p.lpVtbl.CreateDevice(p, a, b, c)


                def IDirectInput_EnumDevices(p, a, b, c, d):
                    return p.lpVtbl.EnumDevices(p, a, b, c, d)


                def IDirectInput_GetDeviceStatus(p, a):
                    return p.lpVtbl.GetDeviceStatus(p, a)


                def IDirectInput_RunControlPanel(p, a, b):
                    return p.lpVtbl.RunControlPanel(p, a, b)


                def IDirectInput_Initialize(p, a, b):
                    return p.lpVtbl.Initialize(p, a, b)
            else:
                def IDirectInput_QueryInterface(p, a, b):
                    return p.QueryInterface(a, b)


                def IDirectInput_AddRef(p):
                    return p.AddRef()


                def IDirectInput_Release(p):
                    return p.Release()


                def IDirectInput_CreateDevice(p, a, b, c):
                    return p.CreateDevice(a, b, c)


                def IDirectInput_EnumDevices(p, a, b, c, d):
                    return p.EnumDevices(a, b, c, d)


                def IDirectInput_GetDeviceStatus(p, a):
                    return p.GetDeviceStatus(a)


                def IDirectInput_RunControlPanel(p, a, b):
                    return p.RunControlPanel(a, b)


                def IDirectInput_Initialize(p, a, b):
                    return p.Initialize(a, b)
            # END IF


            IDirectInput2W = INTERFACE('IDirectInput2W')

            IDirectInput2W._iid_ = IID_IDirectInput2W
            DECLARE_INTERFACE_(IDirectInput2W, IDirectInputW)(
                # * IUnknown methods *
                # * IDirectInputW methods *
                # * IDirectInput2W methods
                STDMETHOD('FindDevice')((REFGUID, LPCWSTR, LPGUID))
            )

            LPDIRECTINPUT2W = POINTER(IDirectInput2W)

            IDirectInput2A = INTERFACE('IDirectInput2A')
            IDirectInput2A._iid_ = IID_IDirectInput2A
            DECLARE_INTERFACE_(IDirectInput2A, IDirectInputA)(
                # * IUnknown methods *
                # * IDirectInputA methods *
                # * IDirectInput2A methods
                STDMETHOD('FindDevice')((REFGUID, LPCSTR, LPGUID))
            )

            LPDIRECTINPUT2A = POINTER(IDirectInput2A)

            if defined(UNICODE):
                IID_IDirectInput2 = IID_IDirectInput2W
                IDirectInput2 = IDirectInput2W
                IDirectInput2Vtbl = IDirectInput2WVtbl
            else:
                IID_IDirectInput2 = IID_IDirectInput2A
                IDirectInput2 = IDirectInput2A
                IDirectInput2Vtbl = IDirectInput2AVtbl
            # END IF


            LPDIRECTINPUT2 = POINTER(IDirectInput2)

            if not defined(__cplusplus) or defined(CINTERFACE):
                def IDirectInput2_QueryInterface(p, a, b):
                    return p.lpVtbl.QueryInterface(p, a, b)


                def IDirectInput2_AddRef(p):
                    return p.lpVtbl.AddRef(p)


                def IDirectInput2_Release(p):
                    return p.lpVtbl.Release(p)


                def IDirectInput2_CreateDevice(p, a, b, c):
                    return p.lpVtbl.CreateDevice(p, a, b, c)


                def IDirectInput2_EnumDevices(p, a, b, c, d):
                    return p.lpVtbl.EnumDevices(p, a, b, c, d)


                def IDirectInput2_GetDeviceStatus(p, a):
                    return p.lpVtbl.GetDeviceStatus(p, a)


                def IDirectInput2_RunControlPanel(p, a, b):
                    return p.lpVtbl.RunControlPanel(p, a, b)


                def IDirectInput2_Initialize(p, a, b):
                    return p.lpVtbl.Initialize(p, a, b)


                def IDirectInput2_FindDevice(p, a, b, c):
                    return p.lpVtbl.FindDevice(p, a, b, c)
            else:
                def IDirectInput2_QueryInterface(p, a, b):
                    return p.QueryInterface(a, b)


                def IDirectInput2_AddRef(p):
                    return p.AddRef()


                def IDirectInput2_Release(p):
                    return p.Release()


                def IDirectInput2_CreateDevice(p, a, b, c):
                    return p.CreateDevice(a, b, c)



                def IDirectInput2_EnumDevices(p, a, b, c, d):
                    return p.EnumDevices(a, b, c, d)


                def IDirectInput2_GetDeviceStatus(p, a):
                    return p.GetDeviceStatus(a)


                def IDirectInput2_RunControlPanel(p, a, b):
                    return p.RunControlPanel(a, b)


                def IDirectInput2_Initialize(p, a, b):
                    return p.Initialize(a, b)


                def IDirectInput2_FindDevice(p, a, b, c):
                    return p.FindDevice(a, b, c)
            # END IF


            IDirectInput7W = INTERFACE('IDirectInput7W')

            IDirectInput7W._iid_ = IID_IDirectInput7W
            DECLARE_INTERFACE_(IDirectInput7W, IDirectInput2W)(
                # * IUnknown methods *
                # * IDirectInput2W methods *
                # * IDirectInput7W methods
                STDMETHOD('CreateDeviceEx')(
                    (REFGUID, REFIID, POINTER(LPVOID), LPUNKNOWN)
                )
            )

            LPDIRECTINPUT7W = POINTER(IDirectInput7W)

            IDirectInput7A = INTERFACE('IDirectInput7A')
            IDirectInput7A._iid_ = IID_IDirectInput7A
            DECLARE_INTERFACE_(IDirectInput7A, IDirectInput2A)(
                # * IUnknown methods *
                # * IDirectInput2A methods *
                # * IDirectInput7A methods
                STDMETHOD('CreateDeviceEx')(
                    (REFGUID, REFIID, POINTER(LPVOID), LPUNKNOWN)
                )
            )

            LPDIRECTINPUT7A = POINTER(IDirectInput7A)

            if defined(UNICODE):
                IID_IDirectInput7 = IID_IDirectInput7W
                IDirectInput7 = IDirectInput7W
                IDirectInput7Vtbl = IDirectInput7WVtbl
            else:
                IID_IDirectInput7 = IID_IDirectInput7A
                IDirectInput7 = IDirectInput7A
                IDirectInput7Vtbl = IDirectInput7AVtbl
            # END IF

            LPDIRECTINPUT7 = POINTER(IDirectInput7)

            if not defined(__cplusplus) or defined(CINTERFACE):
                def IDirectInput7_QueryInterface(p, a, b):
                    return p.lpVtbl.QueryInterface(p, a, b)


                def IDirectInput7_AddRef(p):
                    return p.lpVtbl.AddRef(p)


                def IDirectInput7_Release(p):
                    return p.lpVtbl.Release(p)


                def IDirectInput7_CreateDevice(p, a, b, c):
                    return p.lpVtbl.CreateDevice(p, a, b, c)


                def IDirectInput7_EnumDevices(p, a, b, c, d):
                    return p.lpVtbl.EnumDevices(p, a, b, c, d)


                def IDirectInput7_GetDeviceStatus(p, a):
                    return p.lpVtbl.GetDeviceStatus(p, a)


                def IDirectInput7_RunControlPanel(p, a, b):
                    return p.lpVtbl.RunControlPanel(p, a, b)


                def IDirectInput7_Initialize(p, a, b):
                    return p.lpVtbl.Initialize(p, a, b)


                def IDirectInput7_FindDevice(p, a, b, c):
                    return p.lpVtbl.FindDevice(p, a, b, c)


                def IDirectInput7_CreateDeviceEx(p, a, b, c, d):
                    return p.lpVtbl.CreateDeviceEx(p, a, b, c, d)
            else:
                def IDirectInput7_QueryInterface(p, a, b):
                    return p.QueryInterface(a, b)


                def IDirectInput7_AddRef(p):
                    return p.AddRef()


                def IDirectInput7_Release(p):
                    return p.Release()


                def IDirectInput7_CreateDevice(p, a, b, c):
                    return p.CreateDevice(a, b, c)


                def IDirectInput7_EnumDevices(p, a, b, c, d):
                    return p.EnumDevices(a, b, c, d)


                def IDirectInput7_GetDeviceStatus(p, a):
                    return p.GetDeviceStatus(a)


                def IDirectInput7_RunControlPanel(p, a, b):
                    return p.RunControlPanel(a, b)


                def IDirectInput7_Initialize(p, a, b):
                    return p.Initialize(a, b)


                def IDirectInput7_FindDevice(p, a, b, c):
                    return p.FindDevice(a, b, c)


                def IDirectInput7_CreateDeviceEx(p, a, b, c, d):
                    return p.CreateDeviceEx(a, b, c, d)
            # END IF

            if DIRECTINPUT_VERSION >= 0x0800:

                IDirectInput8W = INTERFACE('IDirectInput8W')
                IDirectInput8W._iid_ = IID_IDirectInput8W
                DECLARE_INTERFACE_(IDirectInput8W, comtypes.IUnknown)(
                    # * IUnknown methods *
                    # * IDirectInput8W methods

                    STDMETHOD('CreateDevice')(
                        (REFGUID, POINTER(LPDIRECTINPUTDEVICE8W), LPUNKNOWN)
                    ),
                    STDMETHOD('EnumDevices')(
                        (DWORD, LPDIENUMDEVICESCALLBACKW, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetDeviceStatus')((REFGUID,)),
                    STDMETHOD('RunControlPanel')((HWND, DWORD)),
                    STDMETHOD('Initialize')((HINSTANCE, DWORD)),
                    STDMETHOD('FindDevice')((REFGUID, LPCWSTR, LPGUID)),
                    STDMETHOD('EnumDevicesBySemantics')(
                        (
                            LPCWSTR,
                            LPDIACTIONFORMATW,
                            LPDIENUMDEVICESBYSEMANTICSCBW,
                            LPVOID,
                            DWORD
                        )
                    ),
                    STDMETHOD('ConfigureDevices')(
                        (
                            LPDICONFIGUREDEVICESCALLBACK,
                            LPDICONFIGUREDEVICESPARAMSW,
                            DWORD,
                            LPVOID
                        )
                    ),
                )

                LPDIRECTINPUT8W = POINTER(IDirectInput8W)

                IDirectInput8A = INTERFACE('IDirectInput8A')
                IDirectInput8A._iid_ = IID_IDirectInput8A
                DECLARE_INTERFACE_(IDirectInput8A, comtypes.IUnknown)(
                    # * IUnknown methods *
                    # * IDirectInput8A methods

                    STDMETHOD('CreateDevice')(
                        (REFGUID, POINTER(LPDIRECTINPUTDEVICE8A), LPUNKNOWN)
                    ),
                    STDMETHOD('EnumDevices')(
                        (DWORD, LPDIENUMDEVICESCALLBACKA, LPVOID, DWORD)
                    ),
                    STDMETHOD('GetDeviceStatus')((REFGUID,)),
                    STDMETHOD('RunControlPanel')((HWND, DWORD)),
                    STDMETHOD('Initialize')((HINSTANCE, DWORD)),
                    STDMETHOD('FindDevice')((REFGUID, LPCSTR, LPGUID)),
                    STDMETHOD('EnumDevicesBySemantics')(
                        (
                            LPCSTR,
                            LPDIACTIONFORMATW,
                            LPDIENUMDEVICESBYSEMANTICSCBA,
                            LPVOID,
                            DWORD
                        )
                    ),
                    STDMETHOD('ConfigureDevices')(
                        (
                            LPDICONFIGUREDEVICESCALLBACK,
                            LPDICONFIGUREDEVICESPARAMSA,
                            DWORD,
                            LPVOID
                        )
                    ),
                )

                LPDIRECTINPUT8A = POINTER(IDirectInput8A)

                if defined(UNICODE):
                    IID_IDirectInput8 = IID_IDirectInput8W
                    IDirectInput8 = IDirectInput8W
                    IDirectInput8Vtbl = IDirectInput8WVtbl
                else:
                    IID_IDirectInput8 = IID_IDirectInput8A
                    IDirectInput8 = IDirectInput8A
                    IDirectInput8Vtbl = IDirectInput8AVtbl
                # END IF

                LPDIRECTINPUT8 = POINTER(IDirectInput8)

                if not defined(__cplusplus) or defined(CINTERFACE):
                    def IDirectInput8_QueryInterface(p, a, b):
                        return p.lpVtbl.QueryInterface(p, a, b)


                    def IDirectInput8_AddRef(p):
                        return p.lpVtbl.AddRef(p)


                    def IDirectInput8_Release(p):
                        return p.lpVtbl.Release(p)


                    def IDirectInput8_CreateDevice(p, a, b, c):
                        return p.lpVtbl.CreateDevice(p, a, b, c)


                    def IDirectInput8_EnumDevices(p, a, b, c, d):
                        return p.lpVtbl.EnumDevices(p, a, b, c, d)


                    def IDirectInput8_GetDeviceStatus(p, a):
                        return p.lpVtbl.GetDeviceStatus(p, a)


                    def IDirectInput8_RunControlPanel(p, a, b):
                        return p.lpVtbl.RunControlPanel(p, a, b)


                    def IDirectInput8_Initialize(p, a, b):
                        return p.lpVtbl.Initialize(p, a, b)


                    def IDirectInput8_FindDevice(p, a, b, c):
                        return p.lpVtbl.FindDevice(p, a, b, c)


                    def IDirectInput8_EnumDevicesBySemantics(p, a, b, c, d, e):
                        return p.lpVtbl.EnumDevicesBySemantics(p, a, b, c, d, e)


                    def IDirectInput8_ConfigureDevices(p, a, b, c, d):
                        return p.lpVtbl.ConfigureDevices(p, a, b, c, d)
                else:
                    def IDirectInput8_QueryInterface(p, a, b):
                        return p.QueryInterface(a, b)


                    def IDirectInput8_AddRef(p):
                        return p.AddRef()


                    def IDirectInput8_Release(p):
                        return p.Release()


                    def IDirectInput8_CreateDevice(p, a, b, c):
                        return p.CreateDevice(a, b, c)


                    def IDirectInput8_EnumDevices(p, a, b, c, d):
                        return p.EnumDevices(a, b, c, d)


                    def IDirectInput8_GetDeviceStatus(p, a):
                        return p.GetDeviceStatus(a)


                    def IDirectInput8_RunControlPanel(p, a, b):
                        return p.RunControlPanel(a, b)


                    def IDirectInput8_Initialize(p, a, b):
                        return p.Initialize(a, b)


                    def IDirectInput8_FindDevice(p, a, b, c):
                        return p.FindDevice(a, b, c)


                    def IDirectInput8_EnumDevicesBySemantics(p, a, b, c, d, e):
                        return p.EnumDevicesBySemantics(a, b, c, d, e)


                    def IDirectInput8_ConfigureDevices(p, a, b, c, d):
                        return p.ConfigureDevices(a, b, c, d)
                # END IF
            # END IF  DIRECTINPUT_VERSION >= 0x0800

            if DIRECTINPUT_VERSION > 0x0700:
                dinput8 = ctypes.windll.DINPUT8

                # extern HRESULT WINAPI DirectInput8Create(
                # HINSTANCE hinst,
                # DWORD dwVersion,
                #  REFIID riidltf,
                # LPVOID *ppvOut,
                #  LPUNKNOWN punkOuter
                # );
                DirectInput8Create = dinput8.DirectInput8Create
                DirectInput8Create.restype = HRESULT

            else:
                dinput = ctypes.windll.DINPUT
                # extern HRESULT WINAPI DirectInputCreateA(
                # HINSTANCE hinst,
                # DWORD dwVersion,
                #  LPDIRECTINPUTA *ppDI,
                #  LPUNKNOWN punkOuter
                # );
                DirectInputCreateA = dinput.DirectInputCreateA
                DirectInputCreateA.restype = HRESULT

                # extern HRESULT WINAPI DirectInputCreateW(
                # HINSTANCE hinst,
                # DWORD dwVersion,
                # LPDIRECTINPUTW *ppDI,
                # LPUNKNOWN punkOuter
                # );
                DirectInputCreateW = dinput.DirectInputCreateW
                DirectInputCreateW.restype = HRESULT

                if defined(UNICODE):
                    DirectInputCreate = DirectInputCreateW
                else:
                    DirectInputCreate = DirectInputCreateA
                # END IF   not UNICODE

                # extern HRESULT WINAPI DirectInputCreateEx(
                # HINSTANCE hinst,
                # DWORD dwVersion,
                #  REFIID riidltf,
                #  LPVOID *ppvOut,
                # LPUNKNOWN punkOuter
                # );
                DirectInputCreateEx = dinput.DirectInputCreateEx
                DirectInputCreateEx.restype = HRESULT
            # END IF  DIRECTINPUT_VERSION > 0x700
        # END IF  DIJ_RINGZERO

        # *********************************************************************
        # Return Codes
        # *********************************************************************

        # /* The operation completed successfully.
        DI_OK = S_OK

        # /* The device exists but is not currently attached.
        DI_NOTATTACHED = S_FALSE

        # /* The device buffer overflowed. Some input was lost.
        DI_BUFFEROVERFLOW = S_FALSE

        # /* The change in device properties had no effect.
        DI_PROPNOEFFECT = S_FALSE

        # /* The operation had no effect.
        DI_NOEFFECT = S_FALSE

        # /* The device is a polled device. As a result, device buffering will
        # not collect any data and event notifications will not be signalled
        # until GetDeviceState is called.
        DI_POLLEDDEVICE = 0x00000002

        # /* The parameters of the effect were successfully updated by
        # IDirectInputEffect::SetParameters, but the effect was not downloaded
        # because the device is not exclusively acquired or because the
        # DIEP_NODOWNLOAD flag was passed.
        DI_DOWNLOADSKIPPED = 0x00000003

        # /* The parameters of the effect were successfully updated by
        # IDirectInputEffect::SetParameters, but in order to change the
        # parameters, the effect needed to be restarted.
        DI_EFFECTRESTARTED = 0x00000004

        # /* The parameters of the effect were successfully updated by
        # IDirectInputEffect::SetParameters, but some of them were beyond the
        # capabilities of the device and were truncated.
        DI_TRUNCATED = 0x00000008

        # /* The settings have been successfully applied but could not be
        # persisted.
        DI_SETTINGSNOTSAVED = 0x0000000B

        # /* Equal to DI_EFFECTRESTARTED | DI_TRUNCATED.
        DI_TRUNCATEDANDRESTARTED = 0x0000000C

        # /* A SUCCESS code indicating that settings cannot be modified.
        DI_WRITEPROTECT = 0x00000013

        # /* The application requires a newer version of DirectInput.
        DIERR_OLDDIRECTINPUTVERSION = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_OLD_WIN_VERSION
        )

        # /* The application was written for an unsupported prerelease version
        # of DirectInput.
        DIERR_BETADIRECTINPUTVERSION = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_RMODE_APP
        )

        # /* The object could not be created due to an incompatible driver
        # version or mismatched or incomplete driver components.
        DIERR_BADDRIVERVER = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_BAD_DRIVER_LEVEL
        )

        # /* The device or device instance or effect is not registered with
        # DirectInput.
        DIERR_DEVICENOTREG = REGDB_E_CLASSNOTREG

        # /* The requested object does not exist.
        DIERR_NOTFOUND = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_FILE_NOT_FOUND
        )

        # /* The requested object does not exist.
        DIERR_OBJECTNOTFOUND = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_FILE_NOT_FOUND
        )

        # /* An invalid parameter was passed to the returning function, or the
        # object was not in a state that admitted the function to be called.
        DIERR_INVALIDPARAM = E_INVALIDARG

        # /* The specified interface is not supported by the object
        DIERR_NOINTERFACE = E_NOINTERFACE

        # /* An undetermined error occured inside the DInput subsystem
        DIERR_GENERIC = E_FAIL

        # /* The DInput subsystem couldn't allocate sufficient memory to
        # complete the caller's request.
        DIERR_OUTOFMEMORY = E_OUTOFMEMORY

        # /* The function called is not supported at this time
        DIERR_UNSUPPORTED = E_NOTIMPL

        # /* This object has not been initialized
        DIERR_NOTINITIALIZED = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_NOT_READY
        )

        # /* This object is already initialized
        DIERR_ALREADYINITIALIZED = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_ALREADY_INITIALIZED
        )

        # /* This object does not support aggregation
        DIERR_NOAGGREGATION = CLASS_E_NOAGGREGATION

        # /* Another app has a higher priority level, preventing this call
        # from succeeding.
        DIERR_OTHERAPPHASPRIO = E_ACCESSDENIED

        # /* Access to the device has been lost. It must be re-acquired.
        DIERR_INPUTLOST = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_READ_FAULT
        )

        # /* The operation cannot be performed while the device is acquired.
        DIERR_ACQUIRED = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_BUSY
        )

        # /* The operation cannot be performed unless the device is acquired.
        DIERR_NOTACQUIRED = MAKE_HRESULT(
            SEVERITY_ERROR,
            FACILITY_WIN32,
            ERROR_INVALID_ACCESS
        )

        # /* The specified property cannot be changed.
        DIERR_READONLY = E_ACCESSDENIED

        # /* The device already has an event notification associated with it.
        DIERR_HANDLEEXISTS = E_ACCESSDENIED

        # /* Data is not yet available.
        if not defined(E_PENDING):
            E_PENDING = 0x8000000A
        # END IF

        # /* Unable to IDirectInputJoyConfig_Acquire because the user does not
        # have sufficient privileges to change the joystick configuration.
        DIERR_INSUFFICIENTPRIVS = 0x80040200

        # /* The device is full.
        DIERR_DEVICEFULL = 0x80040201

        # /* Not all the requested information fit into the buffer.
        DIERR_MOREDATA = 0x80040202

        # /* The effect is not downloaded.
        DIERR_NOTDOWNLOADED = 0x80040203

        # /* The device cannot be reinitialized because there are still
        # effects attached to it.
        DIERR_HASEFFECTS = 0x80040204

        # /* The operation cannot be performed unless the device is acquired
        # in DISCL_EXCLUSIVE mode.
        DIERR_NOTEXCLUSIVEACQUIRED = 0x80040205

        # /* The effect could not be downloaded because essential information
        # is missing. For example, no axes have been associated with the
        # effect, or no type-specific information has been created.
        DIERR_INCOMPLETEEFFECT = 0x80040206

        # /* Attempted to read buffered device data from a device that is not
        # buffered.
        DIERR_NOTBUFFERED = 0x80040207

        # /* An attempt was made to modify parameters of an effect while it is
        # playing. Not all hardware devices support altering the parameters of
        # an effect while it is playing.
        DIERR_EFFECTPLAYING = 0x80040208

        # /* The operation could not be completed because the device is not
        # plugged in.
        DIERR_UNPLUGGED = 0x80040209

        # /* SendDeviceData failed because more information was requested to
        # be sent than can be sent to the device. Some devices have
        # restrictions on how much data can be sent to them.
        # (For example, there might be a limit on the number of buttons that
        # can be pressed at once.)
        #
        DIERR_REPORTFULL = 0x8004020A

        # /* A mapper file function failed because reading or writing the user
        # or IHV settings file failed.
        DIERR_MAPFILEFAIL = 0x8004020B

        # Copyright (C) Microsoft. All rights reserved.
        # Copyright (C) Microsoft. All rights reserved.
        # --- DINPUT Mapper Definitions: New for Dx8  ---
        # /*--- Keyboard Physical Keyboard Device  ---
        # Copyright (C) Microsoft. All rights reserved.
        DIKEYBOARD_ESCAPE = 0x81000401
        DIKEYBOARD_1 = 0x81000402
        DIKEYBOARD_2 = 0x81000403
        DIKEYBOARD_3 = 0x81000404
        DIKEYBOARD_4 = 0x81000405
        DIKEYBOARD_5 = 0x81000406
        DIKEYBOARD_6 = 0x81000407
        DIKEYBOARD_7 = 0x81000408
        DIKEYBOARD_8 = 0x81000409
        DIKEYBOARD_9 = 0x8100040A
        DIKEYBOARD_0 = 0x8100040B
        DIKEYBOARD_MINUS = 0x8100040C        # - on main keyboard
        DIKEYBOARD_EQUALS = 0x8100040D
        DIKEYBOARD_BACK = 0x8100040E        # backspace
        DIKEYBOARD_TAB = 0x8100040F
        DIKEYBOARD_Q = 0x81000410
        DIKEYBOARD_W = 0x81000411
        DIKEYBOARD_E = 0x81000412
        DIKEYBOARD_R = 0x81000413
        DIKEYBOARD_T = 0x81000414
        DIKEYBOARD_Y = 0x81000415
        DIKEYBOARD_U = 0x81000416
        DIKEYBOARD_I = 0x81000417
        DIKEYBOARD_O = 0x81000418
        DIKEYBOARD_P = 0x81000419
        DIKEYBOARD_LBRACKET = 0x8100041A
        DIKEYBOARD_RBRACKET = 0x8100041B
        DIKEYBOARD_RETURN = 0x8100041C        # Enter on main keyboard
        DIKEYBOARD_LCONTROL = 0x8100041D
        DIKEYBOARD_A = 0x8100041E
        DIKEYBOARD_S = 0x8100041F
        DIKEYBOARD_D = 0x81000420
        DIKEYBOARD_F = 0x81000421
        DIKEYBOARD_G = 0x81000422
        DIKEYBOARD_H = 0x81000423
        DIKEYBOARD_J = 0x81000424
        DIKEYBOARD_K = 0x81000425
        DIKEYBOARD_L = 0x81000426
        DIKEYBOARD_SEMICOLON = 0x81000427
        DIKEYBOARD_APOSTROPHE = 0x81000428
        DIKEYBOARD_GRAVE = 0x81000429        # accent grave
        DIKEYBOARD_LSHIFT = 0x8100042A
        DIKEYBOARD_BACKSLASH = 0x8100042B
        DIKEYBOARD_Z = 0x8100042C
        DIKEYBOARD_X = 0x8100042D
        DIKEYBOARD_C = 0x8100042E
        DIKEYBOARD_V = 0x8100042F
        DIKEYBOARD_B = 0x81000430
        DIKEYBOARD_N = 0x81000431
        DIKEYBOARD_M = 0x81000432
        DIKEYBOARD_COMMA = 0x81000433
        DIKEYBOARD_PERIOD = 0x81000434        # . on main keyboard
        DIKEYBOARD_SLASH = 0x81000435        # / on main keyboard
        DIKEYBOARD_RSHIFT = 0x81000436
        DIKEYBOARD_MULTIPLY = 0x81000437        # * on numeric keypad
        DIKEYBOARD_LMENU = 0x81000438        # left Alt
        DIKEYBOARD_SPACE = 0x81000439
        DIKEYBOARD_CAPITAL = 0x8100043A
        DIKEYBOARD_F1 = 0x8100043B
        DIKEYBOARD_F2 = 0x8100043C
        DIKEYBOARD_F3 = 0x8100043D
        DIKEYBOARD_F4 = 0x8100043E
        DIKEYBOARD_F5 = 0x8100043F
        DIKEYBOARD_F6 = 0x81000440
        DIKEYBOARD_F7 = 0x81000441
        DIKEYBOARD_F8 = 0x81000442
        DIKEYBOARD_F9 = 0x81000443
        DIKEYBOARD_F10 = 0x81000444
        DIKEYBOARD_NUMLOCK = 0x81000445
        DIKEYBOARD_SCROLL = 0x81000446        # Scroll Lock
        DIKEYBOARD_NUMPAD7 = 0x81000447
        DIKEYBOARD_NUMPAD8 = 0x81000448
        DIKEYBOARD_NUMPAD9 = 0x81000449
        DIKEYBOARD_SUBTRACT = 0x8100044A        # - on numeric keypad
        DIKEYBOARD_NUMPAD4 = 0x8100044B
        DIKEYBOARD_NUMPAD5 = 0x8100044C
        DIKEYBOARD_NUMPAD6 = 0x8100044D
        DIKEYBOARD_ADD = 0x8100044E        # + on numeric keypad
        DIKEYBOARD_NUMPAD1 = 0x8100044F
        DIKEYBOARD_NUMPAD2 = 0x81000450
        DIKEYBOARD_NUMPAD3 = 0x81000451
        DIKEYBOARD_NUMPAD0 = 0x81000452
        DIKEYBOARD_DECIMAL = 0x81000453        # . on numeric keypad
        DIKEYBOARD_OEM_102 = 0x81000456        # <> or \| on RT 102-key keyboard (Non-U.S.)
        DIKEYBOARD_F11 = 0x81000457
        DIKEYBOARD_F12 = 0x81000458
        DIKEYBOARD_F13 = 0x81000464        # (NEC PC98)
        DIKEYBOARD_F14 = 0x81000465        # (NEC PC98)
        DIKEYBOARD_F15 = 0x81000466        # (NEC PC98)
        DIKEYBOARD_KANA = 0x81000470        # (Japanese keyboard)
        DIKEYBOARD_ABNT_C1 = 0x81000473        # /? on Brazilian keyboard
        DIKEYBOARD_CONVERT = 0x81000479        # (Japanese keyboard)
        DIKEYBOARD_NOCONVERT = 0x8100047B        # (Japanese keyboard)
        DIKEYBOARD_YEN = 0x8100047D        # (Japanese keyboard)
        DIKEYBOARD_ABNT_C2 = 0x8100047E        # Numpad . on Brazilian keyboard
        DIKEYBOARD_NUMPADEQUALS = 0x8100048D        # = on numeric keypad (NEC PC98)
        DIKEYBOARD_PREVTRACK = 0x81000490        # Previous Track (DIK_CIRCUMFLEX on Japanese keyboard)
        DIKEYBOARD_AT = 0x81000491        # (NEC PC98)
        DIKEYBOARD_COLON = 0x81000492        # (NEC PC98)
        DIKEYBOARD_UNDERLINE = 0x81000493        # (NEC PC98)
        DIKEYBOARD_KANJI = 0x81000494        # (Japanese keyboard)
        DIKEYBOARD_STOP = 0x81000495        # (NEC PC98)
        DIKEYBOARD_AX = 0x81000496        # (Japan AX)
        DIKEYBOARD_UNLABELED = 0x81000497        # (J3100)
        DIKEYBOARD_NEXTTRACK = 0x81000499        # Next Track
        DIKEYBOARD_NUMPADENTER = 0x8100049C        # Enter on numeric keypad
        DIKEYBOARD_RCONTROL = 0x8100049D
        DIKEYBOARD_MUTE = 0x810004A0        # Mute
        DIKEYBOARD_CALCULATOR = 0x810004A1        # Calculator
        DIKEYBOARD_PLAYPAUSE = 0x810004A2        # Play / Pause
        DIKEYBOARD_MEDIASTOP = 0x810004A4        # Media Stop
        DIKEYBOARD_VOLUMEDOWN = 0x810004AE        # Volume -
        DIKEYBOARD_VOLUMEUP = 0x810004B0        # Volume +
        DIKEYBOARD_WEBHOME = 0x810004B2        # Web home
        DIKEYBOARD_NUMPADCOMMA = 0x810004B3        # , on numeric keypad (NEC PC98)
        DIKEYBOARD_DIVIDE = 0x810004B5        # / on numeric keypad
        DIKEYBOARD_SYSRQ = 0x810004B7
        DIKEYBOARD_RMENU = 0x810004B8        # right Alt
        DIKEYBOARD_PAUSE = 0x810004C5        # Pause
        DIKEYBOARD_HOME = 0x810004C7        # Home on arrow keypad
        DIKEYBOARD_UP = 0x810004C8        # UpArrow on arrow keypad
        DIKEYBOARD_PRIOR = 0x810004C9        # PgUp on arrow keypad
        DIKEYBOARD_LEFT = 0x810004CB        # LeftArrow on arrow keypad
        DIKEYBOARD_RIGHT = 0x810004CD        # RightArrow on arrow keypad
        DIKEYBOARD_END = 0x810004CF        # End on arrow keypad
        DIKEYBOARD_DOWN = 0x810004D0        # DownArrow on arrow keypad
        DIKEYBOARD_NEXT = 0x810004D1        # PgDn on arrow keypad
        DIKEYBOARD_INSERT = 0x810004D2        # Insert on arrow keypad
        DIKEYBOARD_DELETE = 0x810004D3        # Delete on arrow keypad
        DIKEYBOARD_LWIN = 0x810004DB        # Left Windows key
        DIKEYBOARD_RWIN = 0x810004DC        # Right Windows key
        DIKEYBOARD_APPS = 0x810004DD        # AppMenu key
        DIKEYBOARD_POWER = 0x810004DE        # System Power
        DIKEYBOARD_SLEEP = 0x810004DF        # System Sleep
        DIKEYBOARD_WAKE = 0x810004E3        # System Wake
        DIKEYBOARD_WEBSEARCH = 0x810004E5        # Web Search
        DIKEYBOARD_WEBFAVORITES = 0x810004E6        # Web Favorites
        DIKEYBOARD_WEBREFRESH = 0x810004E7        # Web Refresh
        DIKEYBOARD_WEBSTOP = 0x810004E8        # Web Stop
        DIKEYBOARD_WEBFORWARD = 0x810004E9        # Web Forward
        DIKEYBOARD_WEBBACK = 0x810004EA        # Web Back
        DIKEYBOARD_MYCOMPUTER = 0x810004EB        # My Computer
        DIKEYBOARD_MAIL = 0x810004EC        # Mail
        DIKEYBOARD_MEDIASELECT = 0x810004ED        # Media Select

        # /*--- MOUSE Physical Mouse Device   ---
        DIMOUSE_XAXISAB = 0x82000200 | DIMOFS_X        # X Axis-absolute: Some mice natively report absolute coordinates
        DIMOUSE_YAXISAB = 0x82000200 | DIMOFS_Y        # Y Axis-absolute: Some mice natively report absolute coordinates
        DIMOUSE_XAXIS = 0x82000300 | DIMOFS_X        # X Axis
        DIMOUSE_YAXIS = 0x82000300 | DIMOFS_Y        # Y Axis
        DIMOUSE_WHEEL = 0x82000300 | DIMOFS_Z        # Z Axis
        DIMOUSE_BUTTON0 = 0x82000400 | DIMOFS_BUTTON0        # Button 0
        DIMOUSE_BUTTON1 = 0x82000400 | DIMOFS_BUTTON1        # Button 1
        DIMOUSE_BUTTON2 = 0x82000400 | DIMOFS_BUTTON2        # Button 2
        DIMOUSE_BUTTON3 = 0x82000400 | DIMOFS_BUTTON3        # Button 3
        DIMOUSE_BUTTON4 = 0x82000400 | DIMOFS_BUTTON4        # Button 4
        DIMOUSE_BUTTON5 = 0x82000400 | DIMOFS_BUTTON5        # Button 5
        DIMOUSE_BUTTON6 = 0x82000400 | DIMOFS_BUTTON6        # Button 6
        DIMOUSE_BUTTON7 = 0x82000400 | DIMOFS_BUTTON7        # Button 7

        # /*--- VOICE Physical Dplay Voice Device  ---
        DIVOICE_CHANNEL1 = 0x83000401
        DIVOICE_CHANNEL2 = 0x83000402
        DIVOICE_CHANNEL3 = 0x83000403
        DIVOICE_CHANNEL4 = 0x83000404
        DIVOICE_CHANNEL5 = 0x83000405
        DIVOICE_CHANNEL6 = 0x83000406
        DIVOICE_CHANNEL7 = 0x83000407
        DIVOICE_CHANNEL8 = 0x83000408
        DIVOICE_TEAM = 0x83000409
        DIVOICE_ALL = 0x8300040A
        DIVOICE_RECORDMUTE = 0x8300040B
        DIVOICE_PLAYBACKMUTE = 0x8300040C
        DIVOICE_TRANSMIT = 0x8300040D
        DIVOICE_VOICECOMMAND = 0x83000410

        # /*--- Driving Simulator - Racing Vehicle control is primary
        # objective ---
        DIVIRTUAL_DRIVING_RACE = 0x01000000
        DIAXIS_DRIVINGR_STEER = 0x01008A01        # Steering
        DIAXIS_DRIVINGR_ACCELERATE = 0x01039202        # Accelerate
        DIAXIS_DRIVINGR_BRAKE = 0x01041203        # Brake-Axis
        DIBUTTON_DRIVINGR_SHIFTUP = 0x01000C01        # Shift to next higher gear
        DIBUTTON_DRIVINGR_SHIFTDOWN = 0x01000C02        # Shift to next lower gear
        DIBUTTON_DRIVINGR_VIEW = 0x01001C03        # Cycle through view options
        DIBUTTON_DRIVINGR_MENU = 0x010004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIAXIS_DRIVINGR_ACCEL_AND_BRAKE = 0x01014A04        # Some devices combine accelerate and brake in a single axis
        DIHATSWITCH_DRIVINGR_GLANCE = 0x01004601        # Look around
        DIBUTTON_DRIVINGR_BRAKE = 0x01004C04        # Brake-button
        DIBUTTON_DRIVINGR_DASHBOARD = 0x01004405        # Select next dashboard option
        DIBUTTON_DRIVINGR_AIDS = 0x01004406        # Driver correction aids
        DIBUTTON_DRIVINGR_MAP = 0x01004407        # Display Driving Map
        DIBUTTON_DRIVINGR_BOOST = 0x01004408        # Turbo Boost
        DIBUTTON_DRIVINGR_PIT = 0x01004409        # Pit stop notification
        DIBUTTON_DRIVINGR_ACCELERATE_LINK = 0x0103D4E0        # Fallback Accelerate button
        DIBUTTON_DRIVINGR_STEER_LEFT_LINK = 0x0100CCE4        # Fallback Steer Left button
        DIBUTTON_DRIVINGR_STEER_RIGHT_LINK = 0x0100CCEC        # Fallback Steer Right button
        DIBUTTON_DRIVINGR_GLANCE_LEFT_LINK = 0x0107C4E4        # Fallback Glance Left button
        DIBUTTON_DRIVINGR_GLANCE_RIGHT_LINK = 0x0107C4EC        # Fallback Glance Right button
        DIBUTTON_DRIVINGR_DEVICE = 0x010044FE        # Show input device and controls
        DIBUTTON_DRIVINGR_PAUSE = 0x010044FC        # Start / Pause / Restart game

        # /*--- Driving Simulator - Combat Combat from within a vehicle is
        # primary objective ---
        DIVIRTUAL_DRIVING_COMBAT = 0x02000000
        DIAXIS_DRIVINGC_STEER = 0x02008A01        # Steering
        DIAXIS_DRIVINGC_ACCELERATE = 0x02039202        # Accelerate
        DIAXIS_DRIVINGC_BRAKE = 0x02041203        # Brake-axis
        DIBUTTON_DRIVINGC_FIRE = 0x02000C01        # Fire
        DIBUTTON_DRIVINGC_WEAPONS = 0x02000C02        # Select next weapon
        DIBUTTON_DRIVINGC_TARGET = 0x02000C03        # Select next available target
        DIBUTTON_DRIVINGC_MENU = 0x020004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIAXIS_DRIVINGC_ACCEL_AND_BRAKE = 0x02014A04        # Some devices combine accelerate and brake in a single axis
        DIHATSWITCH_DRIVINGC_GLANCE = 0x02004601        # Look around
        DIBUTTON_DRIVINGC_SHIFTUP = 0x02004C04        # Shift to next higher gear
        DIBUTTON_DRIVINGC_SHIFTDOWN = 0x02004C05        # Shift to next lower gear
        DIBUTTON_DRIVINGC_DASHBOARD = 0x02004406        # Select next dashboard option
        DIBUTTON_DRIVINGC_AIDS = 0x02004407        # Driver correction aids
        DIBUTTON_DRIVINGC_BRAKE = 0x02004C08        # Brake-button
        DIBUTTON_DRIVINGC_FIRESECONDARY = 0x02004C09        # Alternative fire button
        DIBUTTON_DRIVINGC_ACCELERATE_LINK = 0x0203D4E0        # Fallback Accelerate button
        DIBUTTON_DRIVINGC_STEER_LEFT_LINK = 0x0200CCE4        # Fallback Steer Left button
        DIBUTTON_DRIVINGC_STEER_RIGHT_LINK = 0x0200CCEC        # Fallback Steer Right button
        DIBUTTON_DRIVINGC_GLANCE_LEFT_LINK = 0x0207C4E4        # Fallback Glance Left button
        DIBUTTON_DRIVINGC_GLANCE_RIGHT_LINK = 0x0207C4EC        # Fallback Glance Right button
        DIBUTTON_DRIVINGC_DEVICE = 0x020044FE        # Show input device and controls
        DIBUTTON_DRIVINGC_PAUSE = 0x020044FC        # Start / Pause / Restart game

        # /*--- Driving Simulator - Tank Combat from withing a tank is primary
        # objective ---
        DIVIRTUAL_DRIVING_TANK = 0x03000000
        DIAXIS_DRIVINGT_STEER = 0x03008A01        # Turn tank left / right
        DIAXIS_DRIVINGT_BARREL = 0x03010202        # Raise / lower barrel
        DIAXIS_DRIVINGT_ACCELERATE = 0x03039203        # Accelerate
        DIAXIS_DRIVINGT_ROTATE = 0x03020204        # Turn barrel left / right
        DIBUTTON_DRIVINGT_FIRE = 0x03000C01        # Fire
        DIBUTTON_DRIVINGT_WEAPONS = 0x03000C02        # Select next weapon
        DIBUTTON_DRIVINGT_TARGET = 0x03000C03        # Selects next available target
        DIBUTTON_DRIVINGT_MENU = 0x030004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_DRIVINGT_GLANCE = 0x03004601        # Look around
        DIAXIS_DRIVINGT_BRAKE = 0x03045205        # Brake-axis
        DIAXIS_DRIVINGT_ACCEL_AND_BRAKE = 0x03014A06        # Some devices combine accelerate and brake in a single axis
        DIBUTTON_DRIVINGT_VIEW = 0x03005C04        # Cycle through view options
        DIBUTTON_DRIVINGT_DASHBOARD = 0x03005C05        # Select next dashboard option
        DIBUTTON_DRIVINGT_BRAKE = 0x03004C06        # Brake-button
        DIBUTTON_DRIVINGT_FIRESECONDARY = 0x03004C07        # Alternative fire button
        DIBUTTON_DRIVINGT_ACCELERATE_LINK = 0x0303D4E0        # Fallback Accelerate button
        DIBUTTON_DRIVINGT_STEER_LEFT_LINK = 0x0300CCE4        # Fallback Steer Left button
        DIBUTTON_DRIVINGT_STEER_RIGHT_LINK = 0x0300CCEC        # Fallback Steer Right button
        DIBUTTON_DRIVINGT_BARREL_UP_LINK = 0x030144E0        # Fallback Barrel up button
        DIBUTTON_DRIVINGT_BARREL_DOWN_LINK = 0x030144E8        # Fallback Barrel down button
        DIBUTTON_DRIVINGT_ROTATE_LEFT_LINK = 0x030244E4        # Fallback Rotate left button
        DIBUTTON_DRIVINGT_ROTATE_RIGHT_LINK = 0x030244EC        # Fallback Rotate right button
        DIBUTTON_DRIVINGT_GLANCE_LEFT_LINK = 0x0307C4E4        # Fallback Glance Left button
        DIBUTTON_DRIVINGT_GLANCE_RIGHT_LINK = 0x0307C4EC        # Fallback Glance Right button
        DIBUTTON_DRIVINGT_DEVICE = 0x030044FE        # Show input device and controls
        DIBUTTON_DRIVINGT_PAUSE = 0x030044FC        # Start / Pause / Restart game

        # /*--- Flight Simulator - Civilian Plane control is the primary
        # objective ---
        DIVIRTUAL_FLYING_CIVILIAN = 0x04000000
        DIAXIS_FLYINGC_BANK = 0x04008A01        # Roll ship left / right
        DIAXIS_FLYINGC_PITCH = 0x04010A02        # Nose up / down
        DIAXIS_FLYINGC_THROTTLE = 0x04039203        # Throttle
        DIBUTTON_FLYINGC_VIEW = 0x04002401        # Cycle through view options
        DIBUTTON_FLYINGC_DISPLAY = 0x04002402        # Select next dashboard / heads up display option
        DIBUTTON_FLYINGC_GEAR = 0x04002C03        # Gear up / down
        DIBUTTON_FLYINGC_MENU = 0x040004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_FLYINGC_GLANCE = 0x04004601        # Look around
        DIAXIS_FLYINGC_BRAKE = 0x04046A04        # Apply Brake
        DIAXIS_FLYINGC_RUDDER = 0x04025205        # Yaw ship left/right
        DIAXIS_FLYINGC_FLAPS = 0x04055A06        # Flaps
        DIBUTTON_FLYINGC_FLAPSUP = 0x04006404        # Increment stepping up until fully retracted
        DIBUTTON_FLYINGC_FLAPSDOWN = 0x04006405        # Decrement stepping down until fully extended
        DIBUTTON_FLYINGC_BRAKE_LINK = 0x04046CE0        # Fallback brake button
        DIBUTTON_FLYINGC_FASTER_LINK = 0x0403D4E0        # Fallback throttle up button
        DIBUTTON_FLYINGC_SLOWER_LINK = 0x0403D4E8        # Fallback throttle down button
        DIBUTTON_FLYINGC_GLANCE_LEFT_LINK = 0x0407C4E4        # Fallback Glance Left button
        DIBUTTON_FLYINGC_GLANCE_RIGHT_LINK = 0x0407C4EC        # Fallback Glance Right button
        DIBUTTON_FLYINGC_GLANCE_UP_LINK = 0x0407C4E0        # Fallback Glance Up button
        DIBUTTON_FLYINGC_GLANCE_DOWN_LINK = 0x0407C4E8        # Fallback Glance Down button
        DIBUTTON_FLYINGC_DEVICE = 0x040044FE        # Show input device and controls
        DIBUTTON_FLYINGC_PAUSE = 0x040044FC        # Start / Pause / Restart game

        # /*--- Flight Simulator - Military Aerial combat is the primary
        # objective ---
        DIVIRTUAL_FLYING_MILITARY = 0x05000000
        DIAXIS_FLYINGM_BANK = 0x05008A01        # Bank - Roll ship left / right
        DIAXIS_FLYINGM_PITCH = 0x05010A02        # Pitch - Nose up / down
        DIAXIS_FLYINGM_THROTTLE = 0x05039203        # Throttle - faster / slower
        DIBUTTON_FLYINGM_FIRE = 0x05000C01        # Fire
        DIBUTTON_FLYINGM_WEAPONS = 0x05000C02        # Select next weapon
        DIBUTTON_FLYINGM_TARGET = 0x05000C03        # Selects next available target
        DIBUTTON_FLYINGM_MENU = 0x050004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_FLYINGM_GLANCE = 0x05004601        # Look around
        DIBUTTON_FLYINGM_COUNTER = 0x05005C04        # Activate counter measures
        DIAXIS_FLYINGM_RUDDER = 0x05024A04        # Rudder - Yaw ship left/right
        DIAXIS_FLYINGM_BRAKE = 0x05046205        # Brake-axis
        DIBUTTON_FLYINGM_VIEW = 0x05006405        # Cycle through view options
        DIBUTTON_FLYINGM_DISPLAY = 0x05006406        # Select next dashboard option
        DIAXIS_FLYINGM_FLAPS = 0x05055206        # Flaps
        DIBUTTON_FLYINGM_FLAPSUP = 0x05005407        # Increment stepping up until fully retracted
        DIBUTTON_FLYINGM_FLAPSDOWN = 0x05005408        # Decrement stepping down until fully extended
        DIBUTTON_FLYINGM_FIRESECONDARY = 0x05004C09        # Alternative fire button
        DIBUTTON_FLYINGM_GEAR = 0x0500640A        # Gear up / down
        DIBUTTON_FLYINGM_BRAKE_LINK = 0x050464E0        # Fallback brake button
        DIBUTTON_FLYINGM_FASTER_LINK = 0x0503D4E0        # Fallback throttle up button
        DIBUTTON_FLYINGM_SLOWER_LINK = 0x0503D4E8        # Fallback throttle down button
        DIBUTTON_FLYINGM_GLANCE_LEFT_LINK = 0x0507C4E4        # Fallback Glance Left button
        DIBUTTON_FLYINGM_GLANCE_RIGHT_LINK = 0x0507C4EC        # Fallback Glance Right button
        DIBUTTON_FLYINGM_GLANCE_UP_LINK = 0x0507C4E0        # Fallback Glance Up button
        DIBUTTON_FLYINGM_GLANCE_DOWN_LINK = 0x0507C4E8        # Fallback Glance Down button
        DIBUTTON_FLYINGM_DEVICE = 0x050044FE        # Show input device and controls
        DIBUTTON_FLYINGM_PAUSE = 0x050044FC        # Start / Pause / Restart game

        # /*--- Flight Simulator - Combat Helicopter Combat from helicopter is
        # primary objective ---
        DIVIRTUAL_FLYING_HELICOPTER = 0x06000000
        DIAXIS_FLYINGH_BANK = 0x06008A01        # Bank - Roll ship left / right
        DIAXIS_FLYINGH_PITCH = 0x06010A02        # Pitch - Nose up / down
        DIAXIS_FLYINGH_COLLECTIVE = 0x06018A03        # Collective - Blade pitch/power
        DIBUTTON_FLYINGH_FIRE = 0x06001401        # Fire
        DIBUTTON_FLYINGH_WEAPONS = 0x06001402        # Select next weapon
        DIBUTTON_FLYINGH_TARGET = 0x06001403        # Selects next available target
        DIBUTTON_FLYINGH_MENU = 0x060004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_FLYINGH_GLANCE = 0x06004601        # Look around
        DIAXIS_FLYINGH_TORQUE = 0x06025A04        # Torque - Rotate ship around left / right axis
        DIAXIS_FLYINGH_THROTTLE = 0x0603DA05        # Throttle
        DIBUTTON_FLYINGH_COUNTER = 0x06005404        # Activate counter measures
        DIBUTTON_FLYINGH_VIEW = 0x06006405        # Cycle through view options
        DIBUTTON_FLYINGH_GEAR = 0x06006406        # Gear up / down
        DIBUTTON_FLYINGH_FIRESECONDARY = 0x06004C07        # Alternative fire button
        DIBUTTON_FLYINGH_FASTER_LINK = 0x0603DCE0        # Fallback throttle up button
        DIBUTTON_FLYINGH_SLOWER_LINK = 0x0603DCE8        # Fallback throttle down button
        DIBUTTON_FLYINGH_GLANCE_LEFT_LINK = 0x0607C4E4        # Fallback Glance Left button
        DIBUTTON_FLYINGH_GLANCE_RIGHT_LINK = 0x0607C4EC        # Fallback Glance Right button
        DIBUTTON_FLYINGH_GLANCE_UP_LINK = 0x0607C4E0        # Fallback Glance Up button
        DIBUTTON_FLYINGH_GLANCE_DOWN_LINK = 0x0607C4E8        # Fallback Glance Down button
        DIBUTTON_FLYINGH_DEVICE = 0x060044FE        # Show input device and controls
        DIBUTTON_FLYINGH_PAUSE = 0x060044FC        # Start / Pause / Restart game

        # /*--- Space Simulator - Combat Space Simulator with weapons ---
        DIVIRTUAL_SPACESIM = 0x07000000
        DIAXIS_SPACESIM_LATERAL = 0x07008201        # Move ship left / right
        DIAXIS_SPACESIM_MOVE = 0x07010202        # Move ship forward/backward
        DIAXIS_SPACESIM_THROTTLE = 0x07038203        # Throttle - Engine speed
        DIBUTTON_SPACESIM_FIRE = 0x07000401        # Fire
        DIBUTTON_SPACESIM_WEAPONS = 0x07000402        # Select next weapon
        DIBUTTON_SPACESIM_TARGET = 0x07000403        # Selects next available target
        DIBUTTON_SPACESIM_MENU = 0x070004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_SPACESIM_GLANCE = 0x07004601        # Look around
        DIAXIS_SPACESIM_CLIMB = 0x0701C204        # Climb - Pitch ship up/down
        DIAXIS_SPACESIM_ROTATE = 0x07024205        # Rotate - Turn ship left/right
        DIBUTTON_SPACESIM_VIEW = 0x07004404        # Cycle through view options
        DIBUTTON_SPACESIM_DISPLAY = 0x07004405        # Select next dashboard / heads up display option
        DIBUTTON_SPACESIM_RAISE = 0x07004406        # Raise ship while maintaining current pitch
        DIBUTTON_SPACESIM_LOWER = 0x07004407        # Lower ship while maintaining current pitch
        DIBUTTON_SPACESIM_GEAR = 0x07004408        # Gear up / down
        DIBUTTON_SPACESIM_FIRESECONDARY = 0x07004409        # Alternative fire button
        DIBUTTON_SPACESIM_LEFT_LINK = 0x0700C4E4        # Fallback move left button
        DIBUTTON_SPACESIM_RIGHT_LINK = 0x0700C4EC        # Fallback move right button
        DIBUTTON_SPACESIM_FORWARD_LINK = 0x070144E0        # Fallback move forward button
        DIBUTTON_SPACESIM_BACKWARD_LINK = 0x070144E8        # Fallback move backwards button
        DIBUTTON_SPACESIM_FASTER_LINK = 0x0703C4E0        # Fallback throttle up button
        DIBUTTON_SPACESIM_SLOWER_LINK = 0x0703C4E8        # Fallback throttle down button
        DIBUTTON_SPACESIM_TURN_LEFT_LINK = 0x070244E4        # Fallback turn left button
        DIBUTTON_SPACESIM_TURN_RIGHT_LINK = 0x070244EC        # Fallback turn right button
        DIBUTTON_SPACESIM_GLANCE_LEFT_LINK = 0x0707C4E4        # Fallback Glance Left button
        DIBUTTON_SPACESIM_GLANCE_RIGHT_LINK = 0x0707C4EC        # Fallback Glance Right button
        DIBUTTON_SPACESIM_GLANCE_UP_LINK = 0x0707C4E0        # Fallback Glance Up button
        DIBUTTON_SPACESIM_GLANCE_DOWN_LINK = 0x0707C4E8        # Fallback Glance Down button
        DIBUTTON_SPACESIM_DEVICE = 0x070044FE        # Show input device and controls
        DIBUTTON_SPACESIM_PAUSE = 0x070044FC        # Start / Pause / Restart game

        # /*--- Fighting - First Person Hand to Hand combat is primary
        # objective ---
        DIVIRTUAL_FIGHTING_HAND2HAND = 0x08000000
        DIAXIS_FIGHTINGH_LATERAL = 0x08008201        # Sidestep left/right
        DIAXIS_FIGHTINGH_MOVE = 0x08010202        # Move forward/backward
        DIBUTTON_FIGHTINGH_PUNCH = 0x08000401        # Punch
        DIBUTTON_FIGHTINGH_KICK = 0x08000402        # Kick
        DIBUTTON_FIGHTINGH_BLOCK = 0x08000403        # Block
        DIBUTTON_FIGHTINGH_CROUCH = 0x08000404        # Crouch
        DIBUTTON_FIGHTINGH_JUMP = 0x08000405        # Jump
        DIBUTTON_FIGHTINGH_SPECIAL1 = 0x08000406        # Apply first special move
        DIBUTTON_FIGHTINGH_SPECIAL2 = 0x08000407        # Apply second special move
        DIBUTTON_FIGHTINGH_MENU = 0x080004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_FIGHTINGH_SELECT = 0x08004408        # Select special move
        DIHATSWITCH_FIGHTINGH_SLIDE = 0x08004601        # Look around
        DIBUTTON_FIGHTINGH_DISPLAY = 0x08004409        # Shows next on-screen display option
        DIAXIS_FIGHTINGH_ROTATE = 0x08024203        # Rotate - Turn body left/right
        DIBUTTON_FIGHTINGH_DODGE = 0x0800440A        # Dodge
        DIBUTTON_FIGHTINGH_LEFT_LINK = 0x0800C4E4        # Fallback left sidestep button
        DIBUTTON_FIGHTINGH_RIGHT_LINK = 0x0800C4EC        # Fallback right sidestep button
        DIBUTTON_FIGHTINGH_FORWARD_LINK = 0x080144E0        # Fallback forward button
        DIBUTTON_FIGHTINGH_BACKWARD_LINK = 0x080144E8        # Fallback backward button
        DIBUTTON_FIGHTINGH_DEVICE = 0x080044FE        # Show input device and controls
        DIBUTTON_FIGHTINGH_PAUSE = 0x080044FC        # Start / Pause / Restart game

        # /*--- Fighting - First Person Shooting Navigation and combat are
        # primary objectives ---
        DIVIRTUAL_FIGHTING_FPS = 0x09000000
        DIAXIS_FPS_ROTATE = 0x09008201        # Rotate character left/right
        DIAXIS_FPS_MOVE = 0x09010202        # Move forward/backward
        DIBUTTON_FPS_FIRE = 0x09000401        # Fire
        DIBUTTON_FPS_WEAPONS = 0x09000402        # Select next weapon
        DIBUTTON_FPS_APPLY = 0x09000403        # Use item
        DIBUTTON_FPS_SELECT = 0x09000404        # Select next inventory item
        DIBUTTON_FPS_CROUCH = 0x09000405        # Crouch/ climb down/ swim down
        DIBUTTON_FPS_JUMP = 0x09000406        # Jump/ climb up/ swim up
        DIAXIS_FPS_LOOKUPDOWN = 0x09018203        # Look up / down
        DIBUTTON_FPS_STRAFE = 0x09000407        # Enable strafing while active
        DIBUTTON_FPS_MENU = 0x090004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_FPS_GLANCE = 0x09004601        # Look around
        DIBUTTON_FPS_DISPLAY = 0x09004408        # Shows next on-screen display option/ map
        DIAXIS_FPS_SIDESTEP = 0x09024204        # Sidestep
        DIBUTTON_FPS_DODGE = 0x09004409        # Dodge
        DIBUTTON_FPS_GLANCEL = 0x0900440A        # Glance Left
        DIBUTTON_FPS_GLANCER = 0x0900440B        # Glance Right
        DIBUTTON_FPS_FIRESECONDARY = 0x0900440C        # Alternative fire button
        DIBUTTON_FPS_ROTATE_LEFT_LINK = 0x0900C4E4        # Fallback rotate left button
        DIBUTTON_FPS_ROTATE_RIGHT_LINK = 0x0900C4EC        # Fallback rotate right button
        DIBUTTON_FPS_FORWARD_LINK = 0x090144E0        # Fallback forward button
        DIBUTTON_FPS_BACKWARD_LINK = 0x090144E8        # Fallback backward button
        DIBUTTON_FPS_GLANCE_UP_LINK = 0x0901C4E0        # Fallback look up button
        DIBUTTON_FPS_GLANCE_DOWN_LINK = 0x0901C4E8        # Fallback look down button
        DIBUTTON_FPS_STEP_LEFT_LINK = 0x090244E4        # Fallback step left button
        DIBUTTON_FPS_STEP_RIGHT_LINK = 0x090244EC        # Fallback step right button
        DIBUTTON_FPS_DEVICE = 0x090044FE        # Show input device and controls
        DIBUTTON_FPS_PAUSE = 0x090044FC        # Start / Pause / Restart game

        # /*--- Fighting - Third Person action Perspective of camera is behind
        # the main character ---
        DIVIRTUAL_FIGHTING_THIRDPERSON = 0x0A000000
        DIAXIS_TPS_TURN = 0x0A020201        # Turn left/right
        DIAXIS_TPS_MOVE = 0x0A010202        # Move forward/backward
        DIBUTTON_TPS_RUN = 0x0A000401        # Run or walk toggle switch
        DIBUTTON_TPS_ACTION = 0x0A000402        # Action Button
        DIBUTTON_TPS_SELECT = 0x0A000403        # Select next weapon
        DIBUTTON_TPS_USE = 0x0A000404        # Use inventory item currently selected
        DIBUTTON_TPS_JUMP = 0x0A000405        # Character Jumps
        DIBUTTON_TPS_MENU = 0x0A0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_TPS_GLANCE = 0x0A004601        # Look around
        DIBUTTON_TPS_VIEW = 0x0A004406        # Select camera view
        DIBUTTON_TPS_STEPLEFT = 0x0A004407        # Character takes a left step
        DIBUTTON_TPS_STEPRIGHT = 0x0A004408        # Character takes a right step
        DIAXIS_TPS_STEP = 0x0A00C203        # Character steps left/right
        DIBUTTON_TPS_DODGE = 0x0A004409        # Character dodges or ducks
        DIBUTTON_TPS_INVENTORY = 0x0A00440A        # Cycle through inventory
        DIBUTTON_TPS_TURN_LEFT_LINK = 0x0A0244E4        # Fallback turn left button
        DIBUTTON_TPS_TURN_RIGHT_LINK = 0x0A0244EC        # Fallback turn right button
        DIBUTTON_TPS_FORWARD_LINK = 0x0A0144E0        # Fallback forward button
        DIBUTTON_TPS_BACKWARD_LINK = 0x0A0144E8        # Fallback backward button
        DIBUTTON_TPS_GLANCE_UP_LINK = 0x0A07C4E0        # Fallback look up button
        DIBUTTON_TPS_GLANCE_DOWN_LINK = 0x0A07C4E8        # Fallback look down button
        DIBUTTON_TPS_GLANCE_LEFT_LINK = 0x0A07C4E4        # Fallback glance up button
        DIBUTTON_TPS_GLANCE_RIGHT_LINK = 0x0A07C4EC        # Fallback glance right button
        DIBUTTON_TPS_DEVICE = 0x0A0044FE        # Show input device and controls
        DIBUTTON_TPS_PAUSE = 0x0A0044FC        # Start / Pause / Restart game

        # /*--- Strategy - Role Playing Navigation and problem solving are
        # primary actions ---
        DIVIRTUAL_STRATEGY_ROLEPLAYING = 0x0B000000
        DIAXIS_STRATEGYR_LATERAL = 0x0B008201        # sidestep - left/right
        DIAXIS_STRATEGYR_MOVE = 0x0B010202        # move forward/backward
        DIBUTTON_STRATEGYR_GET = 0x0B000401        # Acquire item
        DIBUTTON_STRATEGYR_APPLY = 0x0B000402        # Use selected item
        DIBUTTON_STRATEGYR_SELECT = 0x0B000403        # Select nextitem
        DIBUTTON_STRATEGYR_ATTACK = 0x0B000404        # Attack
        DIBUTTON_STRATEGYR_CAST = 0x0B000405        # Cast Spell
        DIBUTTON_STRATEGYR_CROUCH = 0x0B000406        # Crouch
        DIBUTTON_STRATEGYR_JUMP = 0x0B000407        # Jump
        DIBUTTON_STRATEGYR_MENU = 0x0B0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_STRATEGYR_GLANCE = 0x0B004601        # Look around
        DIBUTTON_STRATEGYR_MAP = 0x0B004408        # Cycle through map options
        DIBUTTON_STRATEGYR_DISPLAY = 0x0B004409        # Shows next on-screen display option
        DIAXIS_STRATEGYR_ROTATE = 0x0B024203        # Turn body left/right
        DIBUTTON_STRATEGYR_LEFT_LINK = 0x0B00C4E4        # Fallback sidestep left button
        DIBUTTON_STRATEGYR_RIGHT_LINK = 0x0B00C4EC        # Fallback sidestep right button
        DIBUTTON_STRATEGYR_FORWARD_LINK = 0x0B0144E0        # Fallback move forward button
        DIBUTTON_STRATEGYR_BACK_LINK = 0x0B0144E8        # Fallback move backward button
        DIBUTTON_STRATEGYR_ROTATE_LEFT_LINK = 0x0B0244E4        # Fallback turn body left button
        DIBUTTON_STRATEGYR_ROTATE_RIGHT_LINK = 0x0B0244EC        # Fallback turn body right button
        DIBUTTON_STRATEGYR_DEVICE = 0x0B0044FE        # Show input device and controls
        DIBUTTON_STRATEGYR_PAUSE = 0x0B0044FC        # Start / Pause / Restart game

        # /*--- Strategy - Turn based Navigation and problem solving are
        # primary actions ---
        DIVIRTUAL_STRATEGY_TURN = 0x0C000000
        DIAXIS_STRATEGYT_LATERAL = 0x0C008201        # Sidestep left/right
        DIAXIS_STRATEGYT_MOVE = 0x0C010202        # Move forward/backwards
        DIBUTTON_STRATEGYT_SELECT = 0x0C000401        # Select unit or object
        DIBUTTON_STRATEGYT_INSTRUCT = 0x0C000402        # Cycle through instructions
        DIBUTTON_STRATEGYT_APPLY = 0x0C000403        # Apply selected instruction
        DIBUTTON_STRATEGYT_TEAM = 0x0C000404        # Select next team / cycle through all
        DIBUTTON_STRATEGYT_TURN = 0x0C000405        # Indicate turn over
        DIBUTTON_STRATEGYT_MENU = 0x0C0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_STRATEGYT_ZOOM = 0x0C004406        # Zoom - in / out
        DIBUTTON_STRATEGYT_MAP = 0x0C004407        # cycle through map options
        DIBUTTON_STRATEGYT_DISPLAY = 0x0C004408        # shows next on-screen display options
        DIBUTTON_STRATEGYT_LEFT_LINK = 0x0C00C4E4        # Fallback sidestep left button
        DIBUTTON_STRATEGYT_RIGHT_LINK = 0x0C00C4EC        # Fallback sidestep right button
        DIBUTTON_STRATEGYT_FORWARD_LINK = 0x0C0144E0        # Fallback move forward button
        DIBUTTON_STRATEGYT_BACK_LINK = 0x0C0144E8        # Fallback move back button
        DIBUTTON_STRATEGYT_DEVICE = 0x0C0044FE        # Show input device and controls
        DIBUTTON_STRATEGYT_PAUSE = 0x0C0044FC        # Start / Pause / Restart game

        # /*--- Sports - Hunting Hunting   ---
        DIVIRTUAL_SPORTS_HUNTING = 0x0D000000
        DIAXIS_HUNTING_LATERAL = 0x0D008201        # sidestep left/right
        DIAXIS_HUNTING_MOVE = 0x0D010202        # move forward/backwards
        DIBUTTON_HUNTING_FIRE = 0x0D000401        # Fire selected weapon
        DIBUTTON_HUNTING_AIM = 0x0D000402        # Select aim/move
        DIBUTTON_HUNTING_WEAPON = 0x0D000403        # Select next weapon
        DIBUTTON_HUNTING_BINOCULAR = 0x0D000404        # Look through Binoculars
        DIBUTTON_HUNTING_CALL = 0x0D000405        # Make animal call
        DIBUTTON_HUNTING_MAP = 0x0D000406        # View Map
        DIBUTTON_HUNTING_SPECIAL = 0x0D000407        # Special game operation
        DIBUTTON_HUNTING_MENU = 0x0D0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_HUNTING_GLANCE = 0x0D004601        # Look around
        DIBUTTON_HUNTING_DISPLAY = 0x0D004408        # show next on-screen display option
        DIAXIS_HUNTING_ROTATE = 0x0D024203        # Turn body left/right
        DIBUTTON_HUNTING_CROUCH = 0x0D004409        # Crouch/ Climb / Swim down
        DIBUTTON_HUNTING_JUMP = 0x0D00440A        # Jump/ Climb up / Swim up
        DIBUTTON_HUNTING_FIRESECONDARY = 0x0D00440B        # Alternative fire button
        DIBUTTON_HUNTING_LEFT_LINK = 0x0D00C4E4        # Fallback sidestep left button
        DIBUTTON_HUNTING_RIGHT_LINK = 0x0D00C4EC        # Fallback sidestep right button
        DIBUTTON_HUNTING_FORWARD_LINK = 0x0D0144E0        # Fallback move forward button
        DIBUTTON_HUNTING_BACK_LINK = 0x0D0144E8        # Fallback move back button
        DIBUTTON_HUNTING_ROTATE_LEFT_LINK = 0x0D0244E4        # Fallback turn body left button
        DIBUTTON_HUNTING_ROTATE_RIGHT_LINK = 0x0D0244EC        # Fallback turn body right button
        DIBUTTON_HUNTING_DEVICE = 0x0D0044FE        # Show input device and controls
        DIBUTTON_HUNTING_PAUSE = 0x0D0044FC        # Start / Pause / Restart game

        # /*--- Sports - Fishing Catching Fish is primary objective ---
        DIVIRTUAL_SPORTS_FISHING = 0x0E000000
        DIAXIS_FISHING_LATERAL = 0x0E008201        # sidestep left/right
        DIAXIS_FISHING_MOVE = 0x0E010202        # move forward/backwards
        DIBUTTON_FISHING_CAST = 0x0E000401        # Cast line
        DIBUTTON_FISHING_TYPE = 0x0E000402        # Select cast type
        DIBUTTON_FISHING_BINOCULAR = 0x0E000403        # Look through Binocular
        DIBUTTON_FISHING_BAIT = 0x0E000404        # Select type of Bait
        DIBUTTON_FISHING_MAP = 0x0E000405        # View Map
        DIBUTTON_FISHING_MENU = 0x0E0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_FISHING_GLANCE = 0x0E004601        # Look around
        DIBUTTON_FISHING_DISPLAY = 0x0E004406        # Show next on-screen display option
        DIAXIS_FISHING_ROTATE = 0x0E024203        # Turn character left / right
        DIBUTTON_FISHING_CROUCH = 0x0E004407        # Crouch/ Climb / Swim down
        DIBUTTON_FISHING_JUMP = 0x0E004408        # Jump/ Climb up / Swim up
        DIBUTTON_FISHING_LEFT_LINK = 0x0E00C4E4        # Fallback sidestep left button
        DIBUTTON_FISHING_RIGHT_LINK = 0x0E00C4EC        # Fallback sidestep right button
        DIBUTTON_FISHING_FORWARD_LINK = 0x0E0144E0        # Fallback move forward button
        DIBUTTON_FISHING_BACK_LINK = 0x0E0144E8        # Fallback move back button
        DIBUTTON_FISHING_ROTATE_LEFT_LINK = 0x0E0244E4        # Fallback turn body left button
        DIBUTTON_FISHING_ROTATE_RIGHT_LINK = 0x0E0244EC        # Fallback turn body right button
        DIBUTTON_FISHING_DEVICE = 0x0E0044FE        # Show input device and controls
        DIBUTTON_FISHING_PAUSE = 0x0E0044FC        # Start / Pause / Restart game

        # /*--- Sports - Baseball - Batting Batter control is primary
        # objective ---
        DIVIRTUAL_SPORTS_BASEBALL_BAT = 0x0F000000
        DIAXIS_BASEBALLB_LATERAL = 0x0F008201        # Aim left / right
        DIAXIS_BASEBALLB_MOVE = 0x0F010202        # Aim up / down
        DIBUTTON_BASEBALLB_SELECT = 0x0F000401        # cycle through swing options
        DIBUTTON_BASEBALLB_NORMAL = 0x0F000402        # normal swing
        DIBUTTON_BASEBALLB_POWER = 0x0F000403        # swing for the fence
        DIBUTTON_BASEBALLB_BUNT = 0x0F000404        # bunt
        DIBUTTON_BASEBALLB_STEAL = 0x0F000405        # Base runner attempts to steal a base
        DIBUTTON_BASEBALLB_BURST = 0x0F000406        # Base runner invokes burst of speed
        DIBUTTON_BASEBALLB_SLIDE = 0x0F000407        # Base runner slides into base
        DIBUTTON_BASEBALLB_CONTACT = 0x0F000408        # Contact swing
        DIBUTTON_BASEBALLB_MENU = 0x0F0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_BASEBALLB_NOSTEAL = 0x0F004409        # Base runner goes back to a base
        DIBUTTON_BASEBALLB_BOX = 0x0F00440A        # Enter or exit batting box
        DIBUTTON_BASEBALLB_LEFT_LINK = 0x0F00C4E4        # Fallback sidestep left button
        DIBUTTON_BASEBALLB_RIGHT_LINK = 0x0F00C4EC        # Fallback sidestep right button
        DIBUTTON_BASEBALLB_FORWARD_LINK = 0x0F0144E0        # Fallback move forward button
        DIBUTTON_BASEBALLB_BACK_LINK = 0x0F0144E8        # Fallback move back button
        DIBUTTON_BASEBALLB_DEVICE = 0x0F0044FE        # Show input device and controls
        DIBUTTON_BASEBALLB_PAUSE = 0x0F0044FC        # Start / Pause / Restart game

        # /*--- Sports - Baseball - Pitching Pitcher control is primary
        # objective ---
        DIVIRTUAL_SPORTS_BASEBALL_PITCH = 0x10000000
        DIAXIS_BASEBALLP_LATERAL = 0x10008201        # Aim left / right
        DIAXIS_BASEBALLP_MOVE = 0x10010202        # Aim up / down
        DIBUTTON_BASEBALLP_SELECT = 0x10000401        # cycle through pitch selections
        DIBUTTON_BASEBALLP_PITCH = 0x10000402        # throw pitch
        DIBUTTON_BASEBALLP_BASE = 0x10000403        # select base to throw to
        DIBUTTON_BASEBALLP_THROW = 0x10000404        # throw to base
        DIBUTTON_BASEBALLP_FAKE = 0x10000405        # Fake a throw to a base
        DIBUTTON_BASEBALLP_MENU = 0x100004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_BASEBALLP_WALK = 0x10004406        # Throw intentional walk / pitch out
        DIBUTTON_BASEBALLP_LOOK = 0x10004407        # Look at runners on bases
        DIBUTTON_BASEBALLP_LEFT_LINK = 0x1000C4E4        # Fallback sidestep left button
        DIBUTTON_BASEBALLP_RIGHT_LINK = 0x1000C4EC        # Fallback sidestep right button
        DIBUTTON_BASEBALLP_FORWARD_LINK = 0x100144E0        # Fallback move forward button
        DIBUTTON_BASEBALLP_BACK_LINK = 0x100144E8        # Fallback move back button
        DIBUTTON_BASEBALLP_DEVICE = 0x100044FE        # Show input device and controls
        DIBUTTON_BASEBALLP_PAUSE = 0x100044FC        # Start / Pause / Restart game

        # /*--- Sports - Baseball - Fielding Fielder control is primary
        # objective ---
        DIVIRTUAL_SPORTS_BASEBALL_FIELD = 0x11000000
        DIAXIS_BASEBALLF_LATERAL = 0x11008201        # Aim left / right
        DIAXIS_BASEBALLF_MOVE = 0x11010202        # Aim up / down
        DIBUTTON_BASEBALLF_NEAREST = 0x11000401        # Switch to fielder nearest to the ball
        DIBUTTON_BASEBALLF_THROW1 = 0x11000402        # Make conservative throw
        DIBUTTON_BASEBALLF_THROW2 = 0x11000403        # Make aggressive throw
        DIBUTTON_BASEBALLF_BURST = 0x11000404        # Invoke burst of speed
        DIBUTTON_BASEBALLF_JUMP = 0x11000405        # Jump to catch ball
        DIBUTTON_BASEBALLF_DIVE = 0x11000406        # Dive to catch ball
        DIBUTTON_BASEBALLF_MENU = 0x110004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_BASEBALLF_SHIFTIN = 0x11004407        # Shift the infield positioning
        DIBUTTON_BASEBALLF_SHIFTOUT = 0x11004408        # Shift the outfield positioning
        DIBUTTON_BASEBALLF_AIM_LEFT_LINK = 0x1100C4E4        # Fallback aim left button
        DIBUTTON_BASEBALLF_AIM_RIGHT_LINK = 0x1100C4EC        # Fallback aim right button
        DIBUTTON_BASEBALLF_FORWARD_LINK = 0x110144E0        # Fallback move forward button
        DIBUTTON_BASEBALLF_BACK_LINK = 0x110144E8        # Fallback move back button
        DIBUTTON_BASEBALLF_DEVICE = 0x110044FE        # Show input device and controls
        DIBUTTON_BASEBALLF_PAUSE = 0x110044FC        # Start / Pause / Restart game

        # /*--- Sports - Basketball - Offense Offense ---
        DIVIRTUAL_SPORTS_BASKETBALL_OFFENSE = 0x12000000
        DIAXIS_BBALLO_LATERAL = 0x12008201        # left / right
        DIAXIS_BBALLO_MOVE = 0x12010202        # up / down
        DIBUTTON_BBALLO_SHOOT = 0x12000401        # shoot basket
        DIBUTTON_BBALLO_DUNK = 0x12000402        # dunk basket
        DIBUTTON_BBALLO_PASS = 0x12000403        # throw pass
        DIBUTTON_BBALLO_FAKE = 0x12000404        # fake shot or pass
        DIBUTTON_BBALLO_SPECIAL = 0x12000405        # apply special move
        DIBUTTON_BBALLO_PLAYER = 0x12000406        # select next player
        DIBUTTON_BBALLO_BURST = 0x12000407        # invoke burst
        DIBUTTON_BBALLO_CALL = 0x12000408        # call for ball / pass to me
        DIBUTTON_BBALLO_MENU = 0x120004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_BBALLO_GLANCE = 0x12004601        # scroll view
        DIBUTTON_BBALLO_SCREEN = 0x12004409        # Call for screen
        DIBUTTON_BBALLO_PLAY = 0x1200440A        # Call for specific offensive play
        DIBUTTON_BBALLO_JAB = 0x1200440B        # Initiate fake drive to basket
        DIBUTTON_BBALLO_POST = 0x1200440C        # Perform post move
        DIBUTTON_BBALLO_TIMEOUT = 0x1200440D        # Time Out
        DIBUTTON_BBALLO_SUBSTITUTE = 0x1200440E        # substitute one player for another
        DIBUTTON_BBALLO_LEFT_LINK = 0x1200C4E4        # Fallback sidestep left button
        DIBUTTON_BBALLO_RIGHT_LINK = 0x1200C4EC        # Fallback sidestep right button
        DIBUTTON_BBALLO_FORWARD_LINK = 0x120144E0        # Fallback move forward button
        DIBUTTON_BBALLO_BACK_LINK = 0x120144E8        # Fallback move back button
        DIBUTTON_BBALLO_DEVICE = 0x120044FE        # Show input device and controls
        DIBUTTON_BBALLO_PAUSE = 0x120044FC        # Start / Pause / Restart game

        # /*--- Sports - Basketball - Defense Defense ---
        DIVIRTUAL_SPORTS_BASKETBALL_DEFENSE = 0x13000000
        DIAXIS_BBALLD_LATERAL = 0x13008201        # left / right
        DIAXIS_BBALLD_MOVE = 0x13010202        # up / down
        DIBUTTON_BBALLD_JUMP = 0x13000401        # jump to block shot
        DIBUTTON_BBALLD_STEAL = 0x13000402        # attempt to steal ball
        DIBUTTON_BBALLD_FAKE = 0x13000403        # fake block or steal
        DIBUTTON_BBALLD_SPECIAL = 0x13000404        # apply special move
        DIBUTTON_BBALLD_PLAYER = 0x13000405        # select next player
        DIBUTTON_BBALLD_BURST = 0x13000406        # invoke burst
        DIBUTTON_BBALLD_PLAY = 0x13000407        # call for specific defensive play
        DIBUTTON_BBALLD_MENU = 0x130004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_BBALLD_GLANCE = 0x13004601        # scroll view
        DIBUTTON_BBALLD_TIMEOUT = 0x13004408        # Time Out
        DIBUTTON_BBALLD_SUBSTITUTE = 0x13004409        # substitute one player for another
        DIBUTTON_BBALLD_LEFT_LINK = 0x1300C4E4        # Fallback sidestep left button
        DIBUTTON_BBALLD_RIGHT_LINK = 0x1300C4EC        # Fallback sidestep right button
        DIBUTTON_BBALLD_FORWARD_LINK = 0x130144E0        # Fallback move forward button
        DIBUTTON_BBALLD_BACK_LINK = 0x130144E8        # Fallback move back button
        DIBUTTON_BBALLD_DEVICE = 0x130044FE        # Show input device and controls
        DIBUTTON_BBALLD_PAUSE = 0x130044FC        # Start / Pause / Restart game

        # /*--- Sports - Football - Play Play selection ---
        DIVIRTUAL_SPORTS_FOOTBALL_FIELD = 0x14000000
        DIBUTTON_FOOTBALLP_PLAY = 0x14000401        # cycle through available plays
        DIBUTTON_FOOTBALLP_SELECT = 0x14000402        # select play
        DIBUTTON_FOOTBALLP_HELP = 0x14000403        # Bring up pop-up help
        DIBUTTON_FOOTBALLP_MENU = 0x140004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_FOOTBALLP_DEVICE = 0x140044FE        # Show input device and controls
        DIBUTTON_FOOTBALLP_PAUSE = 0x140044FC        # Start / Pause / Restart game

        # /*--- Sports - Football - QB Offense: Quarterback / Kicker ---
        DIVIRTUAL_SPORTS_FOOTBALL_QBCK = 0x15000000
        DIAXIS_FOOTBALLQ_LATERAL = 0x15008201        # Move / Aim: left / right
        DIAXIS_FOOTBALLQ_MOVE = 0x15010202        # Move / Aim: up / down
        DIBUTTON_FOOTBALLQ_SELECT = 0x15000401        # Select
        DIBUTTON_FOOTBALLQ_SNAP = 0x15000402        # snap ball - start play
        DIBUTTON_FOOTBALLQ_JUMP = 0x15000403        # jump over defender
        DIBUTTON_FOOTBALLQ_SLIDE = 0x15000404        # Dive/Slide
        DIBUTTON_FOOTBALLQ_PASS = 0x15000405        # throws pass to receiver
        DIBUTTON_FOOTBALLQ_FAKE = 0x15000406        # pump fake pass or fake kick
        DIBUTTON_FOOTBALLQ_MENU = 0x150004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_FOOTBALLQ_FAKESNAP = 0x15004407        # Fake snap
        DIBUTTON_FOOTBALLQ_MOTION = 0x15004408        # Send receivers in motion
        DIBUTTON_FOOTBALLQ_AUDIBLE = 0x15004409        # Change offensive play at line of scrimmage
        DIBUTTON_FOOTBALLQ_LEFT_LINK = 0x1500C4E4        # Fallback sidestep left button
        DIBUTTON_FOOTBALLQ_RIGHT_LINK = 0x1500C4EC        # Fallback sidestep right button
        DIBUTTON_FOOTBALLQ_FORWARD_LINK = 0x150144E0        # Fallback move forward button
        DIBUTTON_FOOTBALLQ_BACK_LINK = 0x150144E8        # Fallback move back button
        DIBUTTON_FOOTBALLQ_DEVICE = 0x150044FE        # Show input device and controls
        DIBUTTON_FOOTBALLQ_PAUSE = 0x150044FC        # Start / Pause / Restart game

        # /*--- Sports - Football - Offense Offense - Runner ---
        DIVIRTUAL_SPORTS_FOOTBALL_OFFENSE = 0x16000000
        DIAXIS_FOOTBALLO_LATERAL = 0x16008201        # Move / Aim: left / right
        DIAXIS_FOOTBALLO_MOVE = 0x16010202        # Move / Aim: up / down
        DIBUTTON_FOOTBALLO_JUMP = 0x16000401        # jump or hurdle over defender
        DIBUTTON_FOOTBALLO_LEFTARM = 0x16000402        # holds out left arm
        DIBUTTON_FOOTBALLO_RIGHTARM = 0x16000403        # holds out right arm
        DIBUTTON_FOOTBALLO_THROW = 0x16000404        # throw pass or lateral ball to another runner
        DIBUTTON_FOOTBALLO_SPIN = 0x16000405        # Spin to avoid defenders
        DIBUTTON_FOOTBALLO_MENU = 0x160004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_FOOTBALLO_JUKE = 0x16004406        # Use special move to avoid defenders
        DIBUTTON_FOOTBALLO_SHOULDER = 0x16004407        # Lower shoulder to run over defenders
        DIBUTTON_FOOTBALLO_TURBO = 0x16004408        # Speed burst past defenders
        DIBUTTON_FOOTBALLO_DIVE = 0x16004409        # Dive over defenders
        DIBUTTON_FOOTBALLO_ZOOM = 0x1600440A        # Zoom view in / out
        DIBUTTON_FOOTBALLO_SUBSTITUTE = 0x1600440B        # substitute one player for another
        DIBUTTON_FOOTBALLO_LEFT_LINK = 0x1600C4E4        # Fallback sidestep left button
        DIBUTTON_FOOTBALLO_RIGHT_LINK = 0x1600C4EC        # Fallback sidestep right button
        DIBUTTON_FOOTBALLO_FORWARD_LINK = 0x160144E0        # Fallback move forward button
        DIBUTTON_FOOTBALLO_BACK_LINK = 0x160144E8        # Fallback move back button
        DIBUTTON_FOOTBALLO_DEVICE = 0x160044FE        # Show input device and controls
        DIBUTTON_FOOTBALLO_PAUSE = 0x160044FC        # Start / Pause / Restart game

        # /*--- Sports - Football - Defense Defense  ---
        DIVIRTUAL_SPORTS_FOOTBALL_DEFENSE = 0x17000000
        DIAXIS_FOOTBALLD_LATERAL = 0x17008201        # Move / Aim: left / right
        DIAXIS_FOOTBALLD_MOVE = 0x17010202        # Move / Aim: up / down
        DIBUTTON_FOOTBALLD_PLAY = 0x17000401        # cycle through available plays
        DIBUTTON_FOOTBALLD_SELECT = 0x17000402        # select player closest to the ball
        DIBUTTON_FOOTBALLD_JUMP = 0x17000403        # jump to intercept or block
        DIBUTTON_FOOTBALLD_TACKLE = 0x17000404        # tackler runner
        DIBUTTON_FOOTBALLD_FAKE = 0x17000405        # hold down to fake tackle or intercept
        DIBUTTON_FOOTBALLD_SUPERTACKLE = 0x17000406        # Initiate special tackle
        DIBUTTON_FOOTBALLD_MENU = 0x170004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_FOOTBALLD_SPIN = 0x17004407        # Spin to beat offensive line
        DIBUTTON_FOOTBALLD_SWIM = 0x17004408        # Swim to beat the offensive line
        DIBUTTON_FOOTBALLD_BULLRUSH = 0x17004409        # Bull rush the offensive line
        DIBUTTON_FOOTBALLD_RIP = 0x1700440A        # Rip the offensive line
        DIBUTTON_FOOTBALLD_AUDIBLE = 0x1700440B        # Change defensive play at the line of scrimmage
        DIBUTTON_FOOTBALLD_ZOOM = 0x1700440C        # Zoom view in / out
        DIBUTTON_FOOTBALLD_SUBSTITUTE = 0x1700440D        # substitute one player for another
        DIBUTTON_FOOTBALLD_LEFT_LINK = 0x1700C4E4        # Fallback sidestep left button
        DIBUTTON_FOOTBALLD_RIGHT_LINK = 0x1700C4EC        # Fallback sidestep right button
        DIBUTTON_FOOTBALLD_FORWARD_LINK = 0x170144E0        # Fallback move forward button
        DIBUTTON_FOOTBALLD_BACK_LINK = 0x170144E8        # Fallback move back button
        DIBUTTON_FOOTBALLD_DEVICE = 0x170044FE        # Show input device and controls
        DIBUTTON_FOOTBALLD_PAUSE = 0x170044FC        # Start / Pause / Restart game

        # /*--- Sports - Golf ---
        DIVIRTUAL_SPORTS_GOLF = 0x18000000
        DIAXIS_GOLF_LATERAL = 0x18008201        # Move / Aim: left / right
        DIAXIS_GOLF_MOVE = 0x18010202        # Move / Aim: up / down
        DIBUTTON_GOLF_SWING = 0x18000401        # swing club
        DIBUTTON_GOLF_SELECT = 0x18000402        # cycle between: club / swing strength / ball arc / ball spin
        DIBUTTON_GOLF_UP = 0x18000403        # increase selection
        DIBUTTON_GOLF_DOWN = 0x18000404        # decrease selection
        DIBUTTON_GOLF_TERRAIN = 0x18000405        # shows terrain detail
        DIBUTTON_GOLF_FLYBY = 0x18000406        # view the hole via a flyby
        DIBUTTON_GOLF_MENU = 0x180004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_GOLF_SCROLL = 0x18004601        # scroll view
        DIBUTTON_GOLF_ZOOM = 0x18004407        # Zoom view in / out
        DIBUTTON_GOLF_TIMEOUT = 0x18004408        # Call for time out
        DIBUTTON_GOLF_SUBSTITUTE = 0x18004409        # substitute one player for another
        DIBUTTON_GOLF_LEFT_LINK = 0x1800C4E4        # Fallback sidestep left button
        DIBUTTON_GOLF_RIGHT_LINK = 0x1800C4EC        # Fallback sidestep right button
        DIBUTTON_GOLF_FORWARD_LINK = 0x180144E0        # Fallback move forward button
        DIBUTTON_GOLF_BACK_LINK = 0x180144E8        # Fallback move back button
        DIBUTTON_GOLF_DEVICE = 0x180044FE        # Show input device and controls
        DIBUTTON_GOLF_PAUSE = 0x180044FC        # Start / Pause / Restart game

        # /*--- Sports - Hockey - Offense Offense  ---
        DIVIRTUAL_SPORTS_HOCKEY_OFFENSE = 0x19000000
        DIAXIS_HOCKEYO_LATERAL = 0x19008201        # Move / Aim: left / right
        DIAXIS_HOCKEYO_MOVE = 0x19010202        # Move / Aim: up / down
        DIBUTTON_HOCKEYO_SHOOT = 0x19000401        # Shoot
        DIBUTTON_HOCKEYO_PASS = 0x19000402        # pass the puck
        DIBUTTON_HOCKEYO_BURST = 0x19000403        # invoke speed burst
        DIBUTTON_HOCKEYO_SPECIAL = 0x19000404        # invoke special move
        DIBUTTON_HOCKEYO_FAKE = 0x19000405        # hold down to fake pass or kick
        DIBUTTON_HOCKEYO_MENU = 0x190004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_HOCKEYO_SCROLL = 0x19004601        # scroll view
        DIBUTTON_HOCKEYO_ZOOM = 0x19004406        # Zoom view in / out
        DIBUTTON_HOCKEYO_STRATEGY = 0x19004407        # Invoke coaching menu for strategy help
        DIBUTTON_HOCKEYO_TIMEOUT = 0x19004408        # Call for time out
        DIBUTTON_HOCKEYO_SUBSTITUTE = 0x19004409        # substitute one player for another
        DIBUTTON_HOCKEYO_LEFT_LINK = 0x1900C4E4        # Fallback sidestep left button
        DIBUTTON_HOCKEYO_RIGHT_LINK = 0x1900C4EC        # Fallback sidestep right button
        DIBUTTON_HOCKEYO_FORWARD_LINK = 0x190144E0        # Fallback move forward button
        DIBUTTON_HOCKEYO_BACK_LINK = 0x190144E8        # Fallback move back button
        DIBUTTON_HOCKEYO_DEVICE = 0x190044FE        # Show input device and controls
        DIBUTTON_HOCKEYO_PAUSE = 0x190044FC        # Start / Pause / Restart game

        # /*--- Sports - Hockey - Defense Defense  ---
        DIVIRTUAL_SPORTS_HOCKEY_DEFENSE = 0x1A000000
        DIAXIS_HOCKEYD_LATERAL = 0x1A008201        # Move / Aim: left / right
        DIAXIS_HOCKEYD_MOVE = 0x1A010202        # Move / Aim: up / down
        DIBUTTON_HOCKEYD_PLAYER = 0x1A000401        # control player closest to the puck
        DIBUTTON_HOCKEYD_STEAL = 0x1A000402        # attempt steal
        DIBUTTON_HOCKEYD_BURST = 0x1A000403        # speed burst or body check
        DIBUTTON_HOCKEYD_BLOCK = 0x1A000404        # block puck
        DIBUTTON_HOCKEYD_FAKE = 0x1A000405        # hold down to fake tackle or intercept
        DIBUTTON_HOCKEYD_MENU = 0x1A0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_HOCKEYD_SCROLL = 0x1A004601        # scroll view
        DIBUTTON_HOCKEYD_ZOOM = 0x1A004406        # Zoom view in / out
        DIBUTTON_HOCKEYD_STRATEGY = 0x1A004407        # Invoke coaching menu for strategy help
        DIBUTTON_HOCKEYD_TIMEOUT = 0x1A004408        # Call for time out
        DIBUTTON_HOCKEYD_SUBSTITUTE = 0x1A004409        # substitute one player for another
        DIBUTTON_HOCKEYD_LEFT_LINK = 0x1A00C4E4        # Fallback sidestep left button
        DIBUTTON_HOCKEYD_RIGHT_LINK = 0x1A00C4EC        # Fallback sidestep right button
        DIBUTTON_HOCKEYD_FORWARD_LINK = 0x1A0144E0        # Fallback move forward button
        DIBUTTON_HOCKEYD_BACK_LINK = 0x1A0144E8        # Fallback move back button
        DIBUTTON_HOCKEYD_DEVICE = 0x1A0044FE        # Show input device and controls
        DIBUTTON_HOCKEYD_PAUSE = 0x1A0044FC        # Start / Pause / Restart game

        # /*--- Sports - Hockey - Goalie Goal tending ---
        DIVIRTUAL_SPORTS_HOCKEY_GOALIE = 0x1B000000
        DIAXIS_HOCKEYG_LATERAL = 0x1B008201        # Move / Aim: left / right
        DIAXIS_HOCKEYG_MOVE = 0x1B010202        # Move / Aim: up / down
        DIBUTTON_HOCKEYG_PASS = 0x1B000401        # pass puck
        DIBUTTON_HOCKEYG_POKE = 0x1B000402        # poke / check / hack
        DIBUTTON_HOCKEYG_STEAL = 0x1B000403        # attempt steal
        DIBUTTON_HOCKEYG_BLOCK = 0x1B000404        # block puck
        DIBUTTON_HOCKEYG_MENU = 0x1B0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_HOCKEYG_SCROLL = 0x1B004601        # scroll view
        DIBUTTON_HOCKEYG_ZOOM = 0x1B004405        # Zoom view in / out
        DIBUTTON_HOCKEYG_STRATEGY = 0x1B004406        # Invoke coaching menu for strategy help
        DIBUTTON_HOCKEYG_TIMEOUT = 0x1B004407        # Call for time out
        DIBUTTON_HOCKEYG_SUBSTITUTE = 0x1B004408        # substitute one player for another
        DIBUTTON_HOCKEYG_LEFT_LINK = 0x1B00C4E4        # Fallback sidestep left button
        DIBUTTON_HOCKEYG_RIGHT_LINK = 0x1B00C4EC        # Fallback sidestep right button
        DIBUTTON_HOCKEYG_FORWARD_LINK = 0x1B0144E0        # Fallback move forward button
        DIBUTTON_HOCKEYG_BACK_LINK = 0x1B0144E8        # Fallback move back button
        DIBUTTON_HOCKEYG_DEVICE = 0x1B0044FE        # Show input device and controls
        DIBUTTON_HOCKEYG_PAUSE = 0x1B0044FC        # Start / Pause / Restart game

        # /*--- Sports - Mountain Biking ---
        DIVIRTUAL_SPORTS_BIKING_MOUNTAIN = 0x1C000000
        DIAXIS_BIKINGM_TURN = 0x1C008201        # left / right
        DIAXIS_BIKINGM_PEDAL = 0x1C010202        # Pedal faster / slower / brake
        DIBUTTON_BIKINGM_JUMP = 0x1C000401        # jump over obstacle
        DIBUTTON_BIKINGM_CAMERA = 0x1C000402        # switch camera view
        DIBUTTON_BIKINGM_SPECIAL1 = 0x1C000403        # perform first special move
        DIBUTTON_BIKINGM_SELECT = 0x1C000404        # Select
        DIBUTTON_BIKINGM_SPECIAL2 = 0x1C000405        # perform second special move
        DIBUTTON_BIKINGM_MENU = 0x1C0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_BIKINGM_SCROLL = 0x1C004601        # scroll view
        DIBUTTON_BIKINGM_ZOOM = 0x1C004406        # Zoom view in / out
        DIAXIS_BIKINGM_BRAKE = 0x1C044203        # Brake axis
        DIBUTTON_BIKINGM_LEFT_LINK = 0x1C00C4E4        # Fallback turn left button
        DIBUTTON_BIKINGM_RIGHT_LINK = 0x1C00C4EC        # Fallback turn right button
        DIBUTTON_BIKINGM_FASTER_LINK = 0x1C0144E0        # Fallback pedal faster button
        DIBUTTON_BIKINGM_SLOWER_LINK = 0x1C0144E8        # Fallback pedal slower button
        DIBUTTON_BIKINGM_BRAKE_BUTTON_LINK = 0x1C0444E8        # Fallback brake button
        DIBUTTON_BIKINGM_DEVICE = 0x1C0044FE        # Show input device and controls
        DIBUTTON_BIKINGM_PAUSE = 0x1C0044FC        # Start / Pause / Restart game

        # /*--- Sports: Skiing / Snowboarding / Skateboarding ---
        DIVIRTUAL_SPORTS_SKIING = 0x1D000000
        DIAXIS_SKIING_TURN = 0x1D008201        # left / right
        DIAXIS_SKIING_SPEED = 0x1D010202        # faster / slower
        DIBUTTON_SKIING_JUMP = 0x1D000401        # Jump
        DIBUTTON_SKIING_CROUCH = 0x1D000402        # crouch down
        DIBUTTON_SKIING_CAMERA = 0x1D000403        # switch camera view
        DIBUTTON_SKIING_SPECIAL1 = 0x1D000404        # perform first special move
        DIBUTTON_SKIING_SELECT = 0x1D000405        # Select
        DIBUTTON_SKIING_SPECIAL2 = 0x1D000406        # perform second special move
        DIBUTTON_SKIING_MENU = 0x1D0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_SKIING_GLANCE = 0x1D004601        # scroll view
        DIBUTTON_SKIING_ZOOM = 0x1D004407        # Zoom view in / out
        DIBUTTON_SKIING_LEFT_LINK = 0x1D00C4E4        # Fallback turn left button
        DIBUTTON_SKIING_RIGHT_LINK = 0x1D00C4EC        # Fallback turn right button
        DIBUTTON_SKIING_FASTER_LINK = 0x1D0144E0        # Fallback increase speed button
        DIBUTTON_SKIING_SLOWER_LINK = 0x1D0144E8        # Fallback decrease speed button
        DIBUTTON_SKIING_DEVICE = 0x1D0044FE        # Show input device and controls
        DIBUTTON_SKIING_PAUSE = 0x1D0044FC        # Start / Pause / Restart game

        # /*--- Sports - Soccer - Offense Offense  ---
        DIVIRTUAL_SPORTS_SOCCER_OFFENSE = 0x1E000000
        DIAXIS_SOCCERO_LATERAL = 0x1E008201        # Move / Aim: left / right
        DIAXIS_SOCCERO_MOVE = 0x1E010202        # Move / Aim: up / down
        DIAXIS_SOCCERO_BEND = 0x1E018203        # Bend to soccer shot/pass
        DIBUTTON_SOCCERO_SHOOT = 0x1E000401        # Shoot the ball
        DIBUTTON_SOCCERO_PASS = 0x1E000402        # Pass
        DIBUTTON_SOCCERO_FAKE = 0x1E000403        # Fake
        DIBUTTON_SOCCERO_PLAYER = 0x1E000404        # Select next player
        DIBUTTON_SOCCERO_SPECIAL1 = 0x1E000405        # Apply special move
        DIBUTTON_SOCCERO_SELECT = 0x1E000406        # Select special move
        DIBUTTON_SOCCERO_MENU = 0x1E0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_SOCCERO_GLANCE = 0x1E004601        # scroll view
        DIBUTTON_SOCCERO_SUBSTITUTE = 0x1E004407        # Substitute one player for another
        DIBUTTON_SOCCERO_SHOOTLOW = 0x1E004408        # Shoot the ball low
        DIBUTTON_SOCCERO_SHOOTHIGH = 0x1E004409        # Shoot the ball high
        DIBUTTON_SOCCERO_PASSTHRU = 0x1E00440A        # Make a thru pass
        DIBUTTON_SOCCERO_SPRINT = 0x1E00440B        # Sprint / turbo boost
        DIBUTTON_SOCCERO_CONTROL = 0x1E00440C        # Obtain control of the ball
        DIBUTTON_SOCCERO_HEAD = 0x1E00440D        # Attempt to head the ball
        DIBUTTON_SOCCERO_LEFT_LINK = 0x1E00C4E4        # Fallback sidestep left button
        DIBUTTON_SOCCERO_RIGHT_LINK = 0x1E00C4EC        # Fallback sidestep right button
        DIBUTTON_SOCCERO_FORWARD_LINK = 0x1E0144E0        # Fallback move forward button
        DIBUTTON_SOCCERO_BACK_LINK = 0x1E0144E8        # Fallback move back button
        DIBUTTON_SOCCERO_DEVICE = 0x1E0044FE        # Show input device and controls
        DIBUTTON_SOCCERO_PAUSE = 0x1E0044FC        # Start / Pause / Restart game

        # /*--- Sports - Soccer - Defense Defense  ---
        DIVIRTUAL_SPORTS_SOCCER_DEFENSE = 0x1F000000
        DIAXIS_SOCCERD_LATERAL = 0x1F008201        # Move / Aim: left / right
        DIAXIS_SOCCERD_MOVE = 0x1F010202        # Move / Aim: up / down
        DIBUTTON_SOCCERD_BLOCK = 0x1F000401        # Attempt to block shot
        DIBUTTON_SOCCERD_STEAL = 0x1F000402        # Attempt to steal ball
        DIBUTTON_SOCCERD_FAKE = 0x1F000403        # Fake a block or a steal
        DIBUTTON_SOCCERD_PLAYER = 0x1F000404        # Select next player
        DIBUTTON_SOCCERD_SPECIAL = 0x1F000405        # Apply special move
        DIBUTTON_SOCCERD_SELECT = 0x1F000406        # Select special move
        DIBUTTON_SOCCERD_SLIDE = 0x1F000407        # Attempt a slide tackle
        DIBUTTON_SOCCERD_MENU = 0x1F0004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_SOCCERD_GLANCE = 0x1F004601        # scroll view
        DIBUTTON_SOCCERD_FOUL = 0x1F004408        # Initiate a foul / hard-foul
        DIBUTTON_SOCCERD_HEAD = 0x1F004409        # Attempt a Header
        DIBUTTON_SOCCERD_CLEAR = 0x1F00440A        # Attempt to clear the ball down the field
        DIBUTTON_SOCCERD_GOALIECHARGE = 0x1F00440B        # Make the goalie charge out of the box
        DIBUTTON_SOCCERD_SUBSTITUTE = 0x1F00440C        # Substitute one player for another
        DIBUTTON_SOCCERD_LEFT_LINK = 0x1F00C4E4        # Fallback sidestep left button
        DIBUTTON_SOCCERD_RIGHT_LINK = 0x1F00C4EC        # Fallback sidestep right button
        DIBUTTON_SOCCERD_FORWARD_LINK = 0x1F0144E0        # Fallback move forward button
        DIBUTTON_SOCCERD_BACK_LINK = 0x1F0144E8        # Fallback move back button
        DIBUTTON_SOCCERD_DEVICE = 0x1F0044FE        # Show input device and controls
        DIBUTTON_SOCCERD_PAUSE = 0x1F0044FC        # Start / Pause / Restart game

        # /*--- Sports - Racquet Tennis - Table-Tennis - Squash ---
        DIVIRTUAL_SPORTS_RACQUET = 0x20000000
        DIAXIS_RACQUET_LATERAL = 0x20008201        # Move / Aim: left / right
        DIAXIS_RACQUET_MOVE = 0x20010202        # Move / Aim: up / down
        DIBUTTON_RACQUET_SWING = 0x20000401        # Swing racquet
        DIBUTTON_RACQUET_BACKSWING = 0x20000402        # Swing backhand
        DIBUTTON_RACQUET_SMASH = 0x20000403        # Smash shot
        DIBUTTON_RACQUET_SPECIAL = 0x20000404        # Special shot
        DIBUTTON_RACQUET_SELECT = 0x20000405        # Select special shot
        DIBUTTON_RACQUET_MENU = 0x200004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_RACQUET_GLANCE = 0x20004601        # scroll view
        DIBUTTON_RACQUET_TIMEOUT = 0x20004406        # Call for time out
        DIBUTTON_RACQUET_SUBSTITUTE = 0x20004407        # Substitute one player for another
        DIBUTTON_RACQUET_LEFT_LINK = 0x2000C4E4        # Fallback sidestep left button
        DIBUTTON_RACQUET_RIGHT_LINK = 0x2000C4EC        # Fallback sidestep right button
        DIBUTTON_RACQUET_FORWARD_LINK = 0x200144E0        # Fallback move forward button
        DIBUTTON_RACQUET_BACK_LINK = 0x200144E8        # Fallback move back button
        DIBUTTON_RACQUET_DEVICE = 0x200044FE        # Show input device and controls
        DIBUTTON_RACQUET_PAUSE = 0x200044FC        # Start / Pause / Restart game

        # /*--- Arcade- 2D Side to Side movement  ---
        DIVIRTUAL_ARCADE_SIDE2SIDE = 0x21000000
        DIAXIS_ARCADES_LATERAL = 0x21008201        # left / right
        DIAXIS_ARCADES_MOVE = 0x21010202        # up / down
        DIBUTTON_ARCADES_THROW = 0x21000401        # throw object
        DIBUTTON_ARCADES_CARRY = 0x21000402        # carry object
        DIBUTTON_ARCADES_ATTACK = 0x21000403        # attack
        DIBUTTON_ARCADES_SPECIAL = 0x21000404        # apply special move
        DIBUTTON_ARCADES_SELECT = 0x21000405        # select special move
        DIBUTTON_ARCADES_MENU = 0x210004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_ARCADES_VIEW = 0x21004601        # scroll view left / right / up / down
        DIBUTTON_ARCADES_LEFT_LINK = 0x2100C4E4        # Fallback sidestep left button
        DIBUTTON_ARCADES_RIGHT_LINK = 0x2100C4EC        # Fallback sidestep right button
        DIBUTTON_ARCADES_FORWARD_LINK = 0x210144E0        # Fallback move forward button
        DIBUTTON_ARCADES_BACK_LINK = 0x210144E8        # Fallback move back button
        DIBUTTON_ARCADES_VIEW_UP_LINK = 0x2107C4E0        # Fallback scroll view up button
        DIBUTTON_ARCADES_VIEW_DOWN_LINK = 0x2107C4E8        # Fallback scroll view down button
        DIBUTTON_ARCADES_VIEW_LEFT_LINK = 0x2107C4E4        # Fallback scroll view left button
        DIBUTTON_ARCADES_VIEW_RIGHT_LINK = 0x2107C4EC        # Fallback scroll view right button
        DIBUTTON_ARCADES_DEVICE = 0x210044FE        # Show input device and controls
        DIBUTTON_ARCADES_PAUSE = 0x210044FC        # Start / Pause / Restart game

        # /*--- Arcade - Platform Game Character moves around on screen ---
        DIVIRTUAL_ARCADE_PLATFORM = 0x22000000
        DIAXIS_ARCADEP_LATERAL = 0x22008201        # Left / right
        DIAXIS_ARCADEP_MOVE = 0x22010202        # Up / down
        DIBUTTON_ARCADEP_JUMP = 0x22000401        # Jump
        DIBUTTON_ARCADEP_FIRE = 0x22000402        # Fire
        DIBUTTON_ARCADEP_CROUCH = 0x22000403        # Crouch
        DIBUTTON_ARCADEP_SPECIAL = 0x22000404        # Apply special move
        DIBUTTON_ARCADEP_SELECT = 0x22000405        # Select special move
        DIBUTTON_ARCADEP_MENU = 0x220004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_ARCADEP_VIEW = 0x22004601        # Scroll view
        DIBUTTON_ARCADEP_FIRESECONDARY = 0x22004406        # Alternative fire button
        DIBUTTON_ARCADEP_LEFT_LINK = 0x2200C4E4        # Fallback sidestep left button
        DIBUTTON_ARCADEP_RIGHT_LINK = 0x2200C4EC        # Fallback sidestep right button
        DIBUTTON_ARCADEP_FORWARD_LINK = 0x220144E0        # Fallback move forward button
        DIBUTTON_ARCADEP_BACK_LINK = 0x220144E8        # Fallback move back button
        DIBUTTON_ARCADEP_VIEW_UP_LINK = 0x2207C4E0        # Fallback scroll view up button
        DIBUTTON_ARCADEP_VIEW_DOWN_LINK = 0x2207C4E8        # Fallback scroll view down button
        DIBUTTON_ARCADEP_VIEW_LEFT_LINK = 0x2207C4E4        # Fallback scroll view left button
        DIBUTTON_ARCADEP_VIEW_RIGHT_LINK = 0x2207C4EC        # Fallback scroll view right button
        DIBUTTON_ARCADEP_DEVICE = 0x220044FE        # Show input device and controls
        DIBUTTON_ARCADEP_PAUSE = 0x220044FC        # Start / Pause / Restart game

        # /*--- CAD - 2D Object Control Controls to select and move objects in
        # 2D ---
        DIVIRTUAL_CAD_2DCONTROL = 0x23000000
        DIAXIS_2DCONTROL_LATERAL = 0x23008201        # Move view left / right
        DIAXIS_2DCONTROL_MOVE = 0x23010202        # Move view up / down
        DIAXIS_2DCONTROL_INOUT = 0x23018203        # Zoom - in / out
        DIBUTTON_2DCONTROL_SELECT = 0x23000401        # Select Object
        DIBUTTON_2DCONTROL_SPECIAL1 = 0x23000402        # Do first special operation
        DIBUTTON_2DCONTROL_SPECIAL = 0x23000403        # Select special operation
        DIBUTTON_2DCONTROL_SPECIAL2 = 0x23000404        # Do second special operation
        DIBUTTON_2DCONTROL_MENU = 0x230004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_2DCONTROL_HATSWITCH = 0x23004601        # Hat switch
        DIAXIS_2DCONTROL_ROTATEZ = 0x23024204        # Rotate view clockwise / counterclockwise
        DIBUTTON_2DCONTROL_DISPLAY = 0x23004405        # Shows next on-screen display options
        DIBUTTON_2DCONTROL_DEVICE = 0x230044FE        # Show input device and controls
        DIBUTTON_2DCONTROL_PAUSE = 0x230044FC        # Start / Pause / Restart game

        # /*--- CAD - 3D object control Controls to select and move objects
        # within a 3D environment ---
        DIVIRTUAL_CAD_3DCONTROL = 0x24000000
        DIAXIS_3DCONTROL_LATERAL = 0x24008201        # Move view left / right
        DIAXIS_3DCONTROL_MOVE = 0x24010202        # Move view up / down
        DIAXIS_3DCONTROL_INOUT = 0x24018203        # Zoom - in / out
        DIBUTTON_3DCONTROL_SELECT = 0x24000401        # Select Object
        DIBUTTON_3DCONTROL_SPECIAL1 = 0x24000402        # Do first special operation
        DIBUTTON_3DCONTROL_SPECIAL = 0x24000403        # Select special operation
        DIBUTTON_3DCONTROL_SPECIAL2 = 0x24000404        # Do second special operation
        DIBUTTON_3DCONTROL_MENU = 0x240004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_3DCONTROL_HATSWITCH = 0x24004601        # Hat switch
        DIAXIS_3DCONTROL_ROTATEX = 0x24034204        # Rotate view forward or up / backward or down
        DIAXIS_3DCONTROL_ROTATEY = 0x2402C205        # Rotate view clockwise / counterclockwise
        DIAXIS_3DCONTROL_ROTATEZ = 0x24024206        # Rotate view left / right
        DIBUTTON_3DCONTROL_DISPLAY = 0x24004405        # Show next on-screen display options
        DIBUTTON_3DCONTROL_DEVICE = 0x240044FE        # Show input device and controls
        DIBUTTON_3DCONTROL_PAUSE = 0x240044FC        # Start / Pause / Restart game

        # /*--- CAD - 3D Navigation - Fly through Controls for 3D modeling ---
        DIVIRTUAL_CAD_FLYBY = 0x25000000
        DIAXIS_CADF_LATERAL = 0x25008201        # move view left / right
        DIAXIS_CADF_MOVE = 0x25010202        # move view up / down
        DIAXIS_CADF_INOUT = 0x25018203        # in / out
        DIBUTTON_CADF_SELECT = 0x25000401        # Select Object
        DIBUTTON_CADF_SPECIAL1 = 0x25000402        # do first special operation
        DIBUTTON_CADF_SPECIAL = 0x25000403        # Select special operation
        DIBUTTON_CADF_SPECIAL2 = 0x25000404        # do second special operation
        DIBUTTON_CADF_MENU = 0x250004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_CADF_HATSWITCH = 0x25004601        # Hat switch
        DIAXIS_CADF_ROTATEX = 0x25034204        # Rotate view forward or up / backward or down
        DIAXIS_CADF_ROTATEY = 0x2502C205        # Rotate view clockwise / counterclockwise
        DIAXIS_CADF_ROTATEZ = 0x25024206        # Rotate view left / right
        DIBUTTON_CADF_DISPLAY = 0x25004405        # shows next on-screen display options
        DIBUTTON_CADF_DEVICE = 0x250044FE        # Show input device and controls
        DIBUTTON_CADF_PAUSE = 0x250044FC        # Start / Pause / Restart game

        # /*--- CAD - 3D Model Control Controls for 3D modeling ---
        DIVIRTUAL_CAD_MODEL = 0x26000000
        DIAXIS_CADM_LATERAL = 0x26008201        # move view left / right
        DIAXIS_CADM_MOVE = 0x26010202        # move view up / down
        DIAXIS_CADM_INOUT = 0x26018203        # in / out
        DIBUTTON_CADM_SELECT = 0x26000401        # Select Object
        DIBUTTON_CADM_SPECIAL1 = 0x26000402        # do first special operation
        DIBUTTON_CADM_SPECIAL = 0x26000403        # Select special operation
        DIBUTTON_CADM_SPECIAL2 = 0x26000404        # do second special operation
        DIBUTTON_CADM_MENU = 0x260004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIHATSWITCH_CADM_HATSWITCH = 0x26004601        # Hat switch
        DIAXIS_CADM_ROTATEX = 0x26034204        # Rotate view forward or up / backward or down
        DIAXIS_CADM_ROTATEY = 0x2602C205        # Rotate view clockwise / counterclockwise
        DIAXIS_CADM_ROTATEZ = 0x26024206        # Rotate view left / right
        DIBUTTON_CADM_DISPLAY = 0x26004405        # shows next on-screen display options
        DIBUTTON_CADM_DEVICE = 0x260044FE        # Show input device and controls
        DIBUTTON_CADM_PAUSE = 0x260044FC        # Start / Pause / Restart game

        # /*--- Control - Media Equipment Remote  ---
        DIVIRTUAL_REMOTE_CONTROL = 0x27000000
        DIAXIS_REMOTE_SLIDER = 0x27050201        # Slider for adjustment: volume / color / bass / etc
        DIBUTTON_REMOTE_MUTE = 0x27000401        # Set volume on current device to zero
        DIBUTTON_REMOTE_SELECT = 0x27000402        # Next/previous: channel/ track / chapter / picture / station
        DIBUTTON_REMOTE_PLAY = 0x27002403        # Start or pause entertainment on current device
        DIBUTTON_REMOTE_CUE = 0x27002404        # Move through current media
        DIBUTTON_REMOTE_REVIEW = 0x27002405        # Move through current media
        DIBUTTON_REMOTE_CHANGE = 0x27002406        # Select next device
        DIBUTTON_REMOTE_RECORD = 0x27002407        # Start recording the current media
        DIBUTTON_REMOTE_MENU = 0x270004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIAXIS_REMOTE_SLIDER2 = 0x27054202        # Slider for adjustment: volume
        DIBUTTON_REMOTE_TV = 0x27005C08        # Select TV
        DIBUTTON_REMOTE_CABLE = 0x27005C09        # Select cable box
        DIBUTTON_REMOTE_CD = 0x27005C0A        # Select CD player
        DIBUTTON_REMOTE_VCR = 0x27005C0B        # Select VCR
        DIBUTTON_REMOTE_TUNER = 0x27005C0C        # Select tuner
        DIBUTTON_REMOTE_DVD = 0x27005C0D        # Select DVD player
        DIBUTTON_REMOTE_ADJUST = 0x27005C0E        # Enter device adjustment menu
        DIBUTTON_REMOTE_DIGIT0 = 0x2700540F        # Digit 0
        DIBUTTON_REMOTE_DIGIT1 = 0x27005410        # Digit 1
        DIBUTTON_REMOTE_DIGIT2 = 0x27005411        # Digit 2
        DIBUTTON_REMOTE_DIGIT3 = 0x27005412        # Digit 3
        DIBUTTON_REMOTE_DIGIT4 = 0x27005413        # Digit 4
        DIBUTTON_REMOTE_DIGIT5 = 0x27005414        # Digit 5
        DIBUTTON_REMOTE_DIGIT6 = 0x27005415        # Digit 6
        DIBUTTON_REMOTE_DIGIT7 = 0x27005416        # Digit 7
        DIBUTTON_REMOTE_DIGIT8 = 0x27005417        # Digit 8
        DIBUTTON_REMOTE_DIGIT9 = 0x27005418        # Digit 9
        DIBUTTON_REMOTE_DEVICE = 0x270044FE        # Show input device and controls
        DIBUTTON_REMOTE_PAUSE = 0x270044FC        # Start / Pause / Restart game

        # /*--- Control- Web Help or Browser  ---
        DIVIRTUAL_BROWSER_CONTROL = 0x28000000
        DIAXIS_BROWSER_LATERAL = 0x28008201        # Move on screen pointer
        DIAXIS_BROWSER_MOVE = 0x28010202        # Move on screen pointer
        DIBUTTON_BROWSER_SELECT = 0x28000401        # Select current item
        DIAXIS_BROWSER_VIEW = 0x28018203        # Move view up/down
        DIBUTTON_BROWSER_REFRESH = 0x28000402        # Refresh
        DIBUTTON_BROWSER_MENU = 0x280004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_BROWSER_SEARCH = 0x28004403        # Use search tool
        DIBUTTON_BROWSER_STOP = 0x28004404        # Cease current update
        DIBUTTON_BROWSER_HOME = 0x28004405        # Go directly to "home" location
        DIBUTTON_BROWSER_FAVORITES = 0x28004406        # Mark current site as favorite
        DIBUTTON_BROWSER_NEXT = 0x28004407        # Select Next page
        DIBUTTON_BROWSER_PREVIOUS = 0x28004408        # Select Previous page
        DIBUTTON_BROWSER_HISTORY = 0x28004409        # Show/Hide History
        DIBUTTON_BROWSER_PRINT = 0x2800440A        # Print current page
        DIBUTTON_BROWSER_DEVICE = 0x280044FE        # Show input device and controls
        DIBUTTON_BROWSER_PAUSE = 0x280044FC        # Start / Pause / Restart game

        # /*--- Driving Simulator - Giant Walking Robot Walking tank with
        # weapons ---
        DIVIRTUAL_DRIVING_MECHA = 0x29000000
        DIAXIS_MECHA_STEER = 0x29008201        # Turns mecha left/right
        DIAXIS_MECHA_TORSO = 0x29010202        # Tilts torso forward/backward
        DIAXIS_MECHA_ROTATE = 0x29020203        # Turns torso left/right
        DIAXIS_MECHA_THROTTLE = 0x29038204        # Engine Speed
        DIBUTTON_MECHA_FIRE = 0x29000401        # Fire
        DIBUTTON_MECHA_WEAPONS = 0x29000402        # Select next weapon group
        DIBUTTON_MECHA_TARGET = 0x29000403        # Select closest enemy available target
        DIBUTTON_MECHA_REVERSE = 0x29000404        # Toggles throttle in/out of reverse
        DIBUTTON_MECHA_ZOOM = 0x29000405        # Zoom in/out targeting reticule
        DIBUTTON_MECHA_JUMP = 0x29000406        # Fires jump jets
        DIBUTTON_MECHA_MENU = 0x290004FD        # Show menu options

        # --- Priority 2 controls     ---
        DIBUTTON_MECHA_CENTER = 0x29004407        # Center torso to legs
        DIHATSWITCH_MECHA_GLANCE = 0x29004601        # Look around
        DIBUTTON_MECHA_VIEW = 0x29004408        # Cycle through view options
        DIBUTTON_MECHA_FIRESECONDARY = 0x29004409        # Alternative fire button
        DIBUTTON_MECHA_LEFT_LINK = 0x2900C4E4        # Fallback steer left button
        DIBUTTON_MECHA_RIGHT_LINK = 0x2900C4EC        # Fallback steer right button
        DIBUTTON_MECHA_FORWARD_LINK = 0x290144E0        # Fallback tilt torso forward button
        DIBUTTON_MECHA_BACK_LINK = 0x290144E8        # Fallback tilt toroso backward button
        DIBUTTON_MECHA_ROTATE_LEFT_LINK = 0x290244E4        # Fallback rotate toroso right button
        DIBUTTON_MECHA_ROTATE_RIGHT_LINK = 0x290244EC        # Fallback rotate torso left button
        DIBUTTON_MECHA_FASTER_LINK = 0x2903C4E0        # Fallback increase engine speed
        DIBUTTON_MECHA_SLOWER_LINK = 0x2903C4E8        # Fallback decrease engine speed
        DIBUTTON_MECHA_DEVICE = 0x290044FE        # Show input device and controls
        DIBUTTON_MECHA_PAUSE = 0x290044FC        # Start / Pause / Restart game

        # /* "ANY" semantics can be used as a last resort to get mappings for
        # actions that match nothing in the chosen virtual genre. These
        # semantics will be mapped at a lower priority that virtual genre
        # semantics. Also, hardware vendors will not be able to provide
        # sensible mappings for these unless they provide application specific
        # mappings.
        DIAXIS_ANY_X_1 = 0xFF00C201
        DIAXIS_ANY_X_2 = 0xFF00C202
        DIAXIS_ANY_Y_1 = 0xFF014201
        DIAXIS_ANY_Y_2 = 0xFF014202
        DIAXIS_ANY_Z_1 = 0xFF01C201
        DIAXIS_ANY_Z_2 = 0xFF01C202
        DIAXIS_ANY_R_1 = 0xFF024201
        DIAXIS_ANY_R_2 = 0xFF024202
        DIAXIS_ANY_U_1 = 0xFF02C201
        DIAXIS_ANY_U_2 = 0xFF02C202
        DIAXIS_ANY_V_1 = 0xFF034201
        DIAXIS_ANY_V_2 = 0xFF034202
        DIAXIS_ANY_A_1 = 0xFF03C201
        DIAXIS_ANY_A_2 = 0xFF03C202
        DIAXIS_ANY_B_1 = 0xFF044201
        DIAXIS_ANY_B_2 = 0xFF044202
        DIAXIS_ANY_C_1 = 0xFF04C201
        DIAXIS_ANY_C_2 = 0xFF04C202
        DIAXIS_ANY_S_1 = 0xFF054201
        DIAXIS_ANY_S_2 = 0xFF054202
        DIAXIS_ANY_1 = 0xFF004201
        DIAXIS_ANY_2 = 0xFF004202
        DIAXIS_ANY_3 = 0xFF004203
        DIAXIS_ANY_4 = 0xFF004204
        DIPOV_ANY_1 = 0xFF004601
        DIPOV_ANY_2 = 0xFF004602
        DIPOV_ANY_3 = 0xFF004603
        DIPOV_ANY_4 = 0xFF004604


        def DIBUTTON_ANY(instance):
            return 0xFF004400 | instance
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF

# END IF  __DINPUT_INCLUDED__

# **************************************************************************
# Definitions for non-IDirectInput (VJoyD) features defined more recently than
# the current sdk files
# *************************************************************************
if defined(_INC_MMSYSTEM):
    if not defined(MMNOJOY):
        if not defined(__VJOYDX_INCLUDED__):
            __VJOYDX_INCLUDED__ = VOID
            if defined(__cplusplus):
                pass
            # END IF

            if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
                # /* Flag to indicate that the dwReserved2 field of the
                # JOYINFOEX structure contains mini-driver specific data to be
                # passed by VJoyD to the mini- driver instead of doing a poll.
                JOY_PASSDRIVERDATA = 0x10000000

                # /* Informs the joystick driver that the configuration has
                # been changed and should be reloaded from the registery.
                # dwFlags is reserved and should be set to zero
                winmm = ctypes.windll.WINMM

                # WINMMAPI MMRESULT WINAPI joyConfigChanged( DWORD dwFlags );
                joyConfigChanged = winmm.joyConfigChanged
                joyConfigChanged.restype = MMRESULT

                if not defined(DIJ_RINGZERO):
                    # /* Invoke the joystick control panel directly, using the
                    # passed window handle as the parent of the dialog. This
                    # API is only supported for compatibility purposes; new
                    # applications should use the RunControlPanel method of a
                    # device interface for a game controller. The API is
                    # called by using the function pointer returned by
                    # GetProcAddress( hCPL, TEXT("ShowJoyCPL") ) where hCPL is
                    # a HMODULE returned by LoadLibrary( TEXT("joy.cpl") ).
                    # The typedef is provided to allow declaration and casting
                    # of an appropriately typed variable.
                    # typedef VOID (WINAPI* LPFNSHOWJOYCPL)( HWND hWnd );
                    WINAPILPFNSHOWJOYCPL = CALLBACK(
                        VOID,
                        HWND
                    )
                # END IF

                # /* Hardware Setting indicating that the device is a
                # headtracker
                JOY_HWS_ISHEADTRACKER = 0x02000000

                # /* Hardware Setting indicating that the VxD is used to
                # replace the standard analog polling
                JOY_HWS_ISGAMEPORTDRIVER = 0x04000000

                # /* Hardware Setting indicating that the driver needs a
                # standard gameport in order to communicate with the device.
                JOY_HWS_ISANALOGPORTDRIVER = 0x08000000

                # /* Hardware Setting indicating that VJoyD should not load
                # this driver, it will be loaded externally and will register
                # with VJoyD of it's own accord.
                JOY_HWS_AUTOLOAD = 0x10000000

                # /* Hardware Setting indicating that the driver acquires any
                # resources needed without needing a devnode through VJoyD.
                JOY_HWS_NODEVNODE = 0x20000000

                # /* Hardware Setting indicating that the device is a gameport
                # bus
                JOY_HWS_ISGAMEPORTBUS = 0x80000000
                JOY_HWS_GAMEPORTBUSBUSY = 0x00000001

                # /* Usage Setting indicating that the settings are volatile
                # and should be removed if still present on a reboot.
                JOY_US_VOLATILE = 0x00000008
            # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

            if defined(__cplusplus):
                pass
            # END IF

        # END IF  __VJOYDX_INCLUDED__
    # END IF  not MMNOJOY
# END IF  _INC_MMSYSTEM

# **************************************************************************
# Definitions for non-IDirectInput (VJoyD) features defined more recently than
# the current ddk files
# *************************************************************************
if not defined(DIJ_RINGZERO):
    if defined(_INC_MMDDK):
        if not defined(MMNOJOYDEV):
            if not defined(__VJOYDXD_INCLUDED__):
                __VJOYDXD_INCLUDED__ = VOID

                # /* Poll type in which the do_other field of the
                # JOYOEMPOLLDATA structure contains mini-driver specific data
                # passed from an app.
                JOY_OEMPOLL_PASSDRIVERDATA = 7
            # END IF  __VJOYDXD_INCLUDED__
        # END IF  not MMNOJOYDEV
    # END IF  _INC_MMDDK
# END IF  DIJ_RINGZERO


