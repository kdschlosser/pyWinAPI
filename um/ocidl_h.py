import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
COM_NO_WINDOWS_H = None
__ocidl_h__ = None
__IEnumConnections_FWD_DEFINED__ = None
__IConnectionPoint_FWD_DEFINED__ = None
__IEnumConnectionPoints_FWD_DEFINED__ = None
__IConnectionPointContainer_FWD_DEFINED__ = None
__IClassFactory2_FWD_DEFINED__ = None
__IProvideClassInfo_FWD_DEFINED__ = None
__IProvideClassInfo2_FWD_DEFINED__ = None
__IProvideMultipleClassInfo_FWD_DEFINED__ = None
__IOleControl_FWD_DEFINED__ = None
__IOleControlSite_FWD_DEFINED__ = None
__IPropertyPage_FWD_DEFINED__ = None
__IPropertyPage2_FWD_DEFINED__ = None
__IPropertyPageSite_FWD_DEFINED__ = None
__IPropertyNotifySink_FWD_DEFINED__ = None
__ISpecifyPropertyPages_FWD_DEFINED__ = None
__IPersistMemory_FWD_DEFINED__ = None
__IPersistStreamInit_FWD_DEFINED__ = None
__IPersistPropertyBag_FWD_DEFINED__ = None
__ISimpleFrameSite_FWD_DEFINED__ = None
__IFont_FWD_DEFINED__ = None
__IPicture_FWD_DEFINED__ = None
__IPicture2_FWD_DEFINED__ = None
__IFontEventsDisp_FWD_DEFINED__ = None
__IFontDisp_FWD_DEFINED__ = None
__IPictureDisp_FWD_DEFINED__ = None
__IOleInPlaceObjectWindowless_FWD_DEFINED__ = None
__IOleInPlaceSiteEx_FWD_DEFINED__ = None
__IOleInPlaceSiteWindowless_FWD_DEFINED__ = None
__IViewObjectEx_FWD_DEFINED__ = None
__IOleUndoUnit_FWD_DEFINED__ = None
__IOleParentUndoUnit_FWD_DEFINED__ = None
__IEnumOleUndoUnits_FWD_DEFINED__ = None
__IOleUndoManager_FWD_DEFINED__ = None
__IPointerInactive_FWD_DEFINED__ = None
__IObjectWithSite_FWD_DEFINED__ = None
__IPerPropertyBrowsing_FWD_DEFINED__ = None
__IPropertyBag2_FWD_DEFINED__ = None
__IPersistPropertyBag2_FWD_DEFINED__ = None
__IAdviseSinkEx_FWD_DEFINED__ = None
__IQuickActivate_FWD_DEFINED__ = None
__IOleControlTypes_INTERFACE_DEFINED__ = None
__IEnumConnections_INTERFACE_DEFINED__ = None
__IConnectionPoint_INTERFACE_DEFINED__ = None
__IEnumConnectionPoints_INTERFACE_DEFINED__ = None
__IConnectionPointContainer_INTERFACE_DEFINED__ = None
__IClassFactory2_INTERFACE_DEFINED__ = None
__IProvideClassInfo_INTERFACE_DEFINED__ = None
__IProvideClassInfo2_INTERFACE_DEFINED__ = None
__IProvideMultipleClassInfo_INTERFACE_DEFINED__ = None
__IOleControl_INTERFACE_DEFINED__ = None
__IOleControlSite_INTERFACE_DEFINED__ = None
__IPropertyPage_INTERFACE_DEFINED__ = None
__IPropertyPage2_INTERFACE_DEFINED__ = None
__IPropertyPageSite_INTERFACE_DEFINED__ = None
__IPropertyNotifySink_INTERFACE_DEFINED__ = None
__ISpecifyPropertyPages_INTERFACE_DEFINED__ = None
__IPersistMemory_INTERFACE_DEFINED__ = None
__IPersistStreamInit_INTERFACE_DEFINED__ = None
__IPersistPropertyBag_INTERFACE_DEFINED__ = None
__ISimpleFrameSite_INTERFACE_DEFINED__ = None
__IFont_INTERFACE_DEFINED__ = None
OLE2ANSI = None
__IPicture_INTERFACE_DEFINED__ = None
__IPicture2_INTERFACE_DEFINED__ = None
__IFontEventsDisp_INTERFACE_DEFINED__ = None
__IFontDisp_INTERFACE_DEFINED__ = None
__IPictureDisp_INTERFACE_DEFINED__ = None
__IOleInPlaceObjectWindowless_INTERFACE_DEFINED__ = None
__IOleInPlaceSiteEx_INTERFACE_DEFINED__ = None
__IOleInPlaceSiteWindowless_INTERFACE_DEFINED__ = None
__IViewObjectEx_INTERFACE_DEFINED__ = None
__IOleUndoUnit_INTERFACE_DEFINED__ = None
__IOleParentUndoUnit_INTERFACE_DEFINED__ = None
__IEnumOleUndoUnits_INTERFACE_DEFINED__ = None
__IOleUndoManager_INTERFACE_DEFINED__ = None
__IPointerInactive_INTERFACE_DEFINED__ = None
__IObjectWithSite_INTERFACE_DEFINED__ = None
__IPerPropertyBrowsing_INTERFACE_DEFINED__ = None
__IPropertyBag2_INTERFACE_DEFINED__ = None
__IPersistPropertyBag2_INTERFACE_DEFINED__ = None
__IAdviseSinkEx_INTERFACE_DEFINED__ = None
__IQuickActivate_INTERFACE_DEFINED__ = None


class tagCONNECTDATA(ctypes.Structure):
    pass


CONNECTDATA = tagCONNECTDATA


class tagLICINFO(ctypes.Structure):
    pass


LICINFO = tagLICINFO


class tagCONTROLINFO(ctypes.Structure):
    pass


CONTROLINFO = tagCONTROLINFO


class tagPOINTF(ctypes.Structure):
    pass


POINTF = tagPOINTF


class tagPROPPAGEINFO(ctypes.Structure):
    pass


PROPPAGEINFO = tagPROPPAGEINFO


class tagCAUUID(ctypes.Structure):
    pass


CAUUID = tagCAUUID


class tagExtentInfo(ctypes.Structure):
    pass


DVEXTENTINFO = tagExtentInfo


class tagAspectInfo(ctypes.Structure):
    pass


DVASPECTINFO = tagAspectInfo


class tagCALPOLESTR(ctypes.Structure):
    pass


CALPOLESTR = tagCALPOLESTR


class tagCADWORD(ctypes.Structure):
    pass


CADWORD = tagCADWORD


class tagPROPBAG2(ctypes.Structure):
    pass


PROPBAG2 = tagPROPBAG2


class tagQACONTAINER(ctypes.Structure):
    pass


QACONTAINER = tagQACONTAINER


class tagQACONTROL(ctypes.Structure):
    pass


QACONTROL = tagQACONTROL


def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the <rpcndr.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    pass
# END IF


# verify that the <rpcsal.h> version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    pass
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA
if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

if not defined(COM_NO_WINDOWS_H):
    from pyWinAPI.um.windows_h import * # NOQA
    from pyWinAPI.um.ole2_h import * # NOQA
# END IF  COM_NO_WINDOWS_H

if not defined(__ocidl_h__):
    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IEnumConnections_FWD_DEFINED__):
        class IEnumConnections(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = None

    # END IF  __IEnumConnections_FWD_DEFINED__

    if not defined(__IConnectionPoint_FWD_DEFINED__):
        class IConnectionPoint(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IConnectionPoint_FWD_DEFINED__

    if not defined(__IEnumConnectionPoints_FWD_DEFINED__):
        class IEnumConnectionPoints(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumConnectionPoints_FWD_DEFINED__

    if not defined(__IConnectionPointContainer_FWD_DEFINED__):
        class IConnectionPointContainer(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IConnectionPointContainer_FWD_DEFINED__

    if not defined(__IClassFactory2_FWD_DEFINED__):
        class IClassFactory2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IClassFactory2_FWD_DEFINED__

    if not defined(__IProvideClassInfo_FWD_DEFINED__):
        class IProvideClassInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProvideClassInfo_FWD_DEFINED__

    if not defined(__IProvideClassInfo2_FWD_DEFINED__):
        class IProvideClassInfo2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProvideClassInfo2_FWD_DEFINED__

    if not defined(__IProvideMultipleClassInfo_FWD_DEFINED__):
        class IProvideMultipleClassInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProvideMultipleClassInfo_FWD_DEFINED__

    if not defined(__IOleControl_FWD_DEFINED__):
        class IOleControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleControl_FWD_DEFINED__

    if not defined(__IOleControlSite_FWD_DEFINED__):
        class IOleControlSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleControlSite_FWD_DEFINED__

    if not defined(__IPropertyPage_FWD_DEFINED__):
        class IPropertyPage(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyPage_FWD_DEFINED__

    if not defined(__IPropertyPage2_FWD_DEFINED__):
        class IPropertyPage2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyPage2_FWD_DEFINED__

    if not defined(__IPropertyPageSite_FWD_DEFINED__):
        class IPropertyPageSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyPageSite_FWD_DEFINED__

    if not defined(__IPropertyNotifySink_FWD_DEFINED__):
        class IPropertyNotifySink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyNotifySink_FWD_DEFINED__

    if not defined(__ISpecifyPropertyPages_FWD_DEFINED__):
        class ISpecifyPropertyPages(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpecifyPropertyPages_FWD_DEFINED__

    if not defined(__IPersistMemory_FWD_DEFINED__):
        class IPersistMemory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistMemory_FWD_DEFINED__

    if not defined(__IPersistStreamInit_FWD_DEFINED__):
        class IPersistStreamInit(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistStreamInit_FWD_DEFINED__

    if not defined(__IPersistPropertyBag_FWD_DEFINED__):
        class IPersistPropertyBag(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistPropertyBag_FWD_DEFINED__

    if not defined(__ISimpleFrameSite_FWD_DEFINED__):
        class ISimpleFrameSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISimpleFrameSite_FWD_DEFINED__

    if not defined(__IFont_FWD_DEFINED__):
        class IFont(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IFont_FWD_DEFINED__

    if not defined(__IPicture_FWD_DEFINED__):
        class IPicture(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPicture_FWD_DEFINED__

    if not defined(__IPicture2_FWD_DEFINED__):
        class IPicture2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPicture2_FWD_DEFINED__

    if not defined(__IFontEventsDisp_FWD_DEFINED__):
        class IFontEventsDisp(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IFontEventsDisp_FWD_DEFINED__

    if not defined(__IFontDisp_FWD_DEFINED__):
        class IFontDisp(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IFontDisp_FWD_DEFINED__

    if not defined(__IPictureDisp_FWD_DEFINED__):
        class IPictureDisp(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPictureDisp_FWD_DEFINED__

    if not defined(__IOleInPlaceObjectWindowless_FWD_DEFINED__):
        class IOleInPlaceObjectWindowless(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleInPlaceObjectWindowless_FWD_DEFINED__

    if not defined(__IOleInPlaceSiteEx_FWD_DEFINED__):
        class IOleInPlaceSiteEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleInPlaceSiteEx_FWD_DEFINED__

    if not defined(__IOleInPlaceSiteWindowless_FWD_DEFINED__):
        class IOleInPlaceSiteWindowless(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleInPlaceSiteWindowless_FWD_DEFINED__

    if not defined(__IViewObjectEx_FWD_DEFINED__):
        class IViewObjectEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IViewObjectEx_FWD_DEFINED__

    if not defined(__IOleUndoUnit_FWD_DEFINED__):
        class IOleUndoUnit(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleUndoUnit_FWD_DEFINED__

    if not defined(__IOleParentUndoUnit_FWD_DEFINED__):
        class IOleParentUndoUnit(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleParentUndoUnit_FWD_DEFINED__

    if not defined(__IEnumOleUndoUnits_FWD_DEFINED__):
        class IEnumOleUndoUnits(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IEnumOleUndoUnits_FWD_DEFINED__

    if not defined(__IOleUndoManager_FWD_DEFINED__):
        class IOleUndoManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IOleUndoManager_FWD_DEFINED__

    if not defined(__IPointerInactive_FWD_DEFINED__):
        class IPointerInactive(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPointerInactive_FWD_DEFINED__

    if not defined(__IObjectWithSite_FWD_DEFINED__):
        class IObjectWithSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IObjectWithSite_FWD_DEFINED__

    if not defined(__IPerPropertyBrowsing_FWD_DEFINED__):
        class IPerPropertyBrowsing(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPerPropertyBrowsing_FWD_DEFINED__

    if not defined(__IPropertyBag2_FWD_DEFINED__):
        class IPropertyBag2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPropertyBag2_FWD_DEFINED__

    if not defined(__IPersistPropertyBag2_FWD_DEFINED__):
        class IPersistPropertyBag2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IPersistPropertyBag2_FWD_DEFINED__

    if not defined(__IAdviseSinkEx_FWD_DEFINED__):
        class IAdviseSinkEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAdviseSinkEx_FWD_DEFINED__

    if not defined(__IQuickActivate_FWD_DEFINED__):
        class IQuickActivate(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IQuickActivate_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.oleidl_h import * # NOQA
    from pyWinAPI.um.oaidl_h import * # NOQA
    from pyWinAPI.um.servprov_h import * # NOQA
    from pyWinAPI.um.urlmon_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_ocidl_0000_0000
    # [local]
    from  pyWinAPI.shared.winapifamily_h import * # NOQA

    # +
    # -------------------------------------------------------------------------
    # Microsoft Windows
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # --------------------------------------------------------------------
    if  _MSC_VER >= 1020 :
        pass
    # END IF

    if _MSC_VER >= 1200:
        pass
    # END IF


    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        pass
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IOleControlTypes_INTERFACE_DEFINED__):
            # interface IOleControlTypes
            # [unique][version]
            class tagUASFLAGS(ENUM):
                UAS_NORMAL = 0
                UAS_BLOCKED = 0x1
                UAS_NOPARENTENABLE = 0x2
                UAS_MASK = 0x3

            UASFLAGS = tagUASFLAGS

            # State values for the DISPID_READYSTATE property
            class tagREADYSTATE(ENUM):
                READYSTATE_UNINITIALIZED = 0
                READYSTATE_LOADING = 1
                READYSTATE_LOADED = 2
                READYSTATE_INTERACTIVE = 3
                READYSTATE_COMPLETE = 4

            READYSTATE = tagREADYSTATE
        # END IF  __IOleControlTypes_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocidl_0000_0001
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IEnumConnections_INTERFACE_DEFINED__):
            # interface IEnumConnections
            # [unique][uuid][object]
            PENUMCONNECTIONS = POINTER(IEnumConnections)
            LPENUMCONNECTIONS = POINTER(IEnumConnections)

            tagCONNECTDATA._fields_ = [
                ('pUnk', POINTER(comtypes.IUnknown)),
                ('dwCookie', DWORD),
            ]
            PCONNECTDATA = POINTER(tagCONNECTDATA)

            LPCONNECTDATA = POINTER(tagCONNECTDATA)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumConnections = MIDL_INTERFACE(
                    "{B196B287-BAB4-101A-B69C-00AA00341D07}"
                )
                IEnumConnections._iid_ = IID_IEnumConnections

                IEnumConnections._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'cConnections'),
                        (['out'], LPCONNECTDATA, 'rgcd'),
                        (['out'], POINTER(ULONG), 'pcFetched'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Skip')],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'cConnections'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Reset')],
                        HRESULT,
                        'Reset',
                    ),
                    COMMETHOD(
                        [helpstring('Method Clone')],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumConnections)),
                           'ppEnum'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumConnections_INTERFACE_DEFINED__

        if not defined(__IConnectionPoint_INTERFACE_DEFINED__):
            # interface IConnectionPoint
            # [unique][uuid][object]
            PCONNECTIONPOINT = POINTER(IConnectionPoint)
            LPCONNECTIONPOINT = POINTER(IConnectionPoint)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IConnectionPoint = MIDL_INTERFACE(
                    "{B196B286-BAB4-101A-B69C-00AA00341D07}"
                )
                IConnectionPoint._iid_ = IID_IConnectionPoint

                IConnectionPoint._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetConnectionInterface')],
                        HRESULT,
                        'GetConnectionInterface',
                        (['out'], POINTER(IID), 'pIID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetConnectionPointContainer')],
                        HRESULT,
                        'GetConnectionPointContainer',
                        (
                            ['out'],
                            POINTER(POINTER(IConnectionPointContainer)),
                           'ppCPC'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Advise')],
                        HRESULT,
                        'Advise',
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkSink'),
                        (['out'], POINTER(DWORD), 'pdwCookie'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Unadvise')],
                        HRESULT,
                        'Unadvise',
                        (['in'], DWORD, 'dwCookie'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumConnections')],
                        HRESULT,
                        'EnumConnections',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumConnections)),
                           'ppEnum'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IConnectionPoint_INTERFACE_DEFINED__

        if not defined(__IEnumConnectionPoints_INTERFACE_DEFINED__):
            # interface IEnumConnectionPoints
            # [unique][uuid][object]
            PENUMCONNECTIONPOINTS = POINTER(IEnumConnectionPoints)
            LPENUMCONNECTIONPOINTS = POINTER(IEnumConnectionPoints)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumConnectionPoints = MIDL_INTERFACE(
                    "{B196B285-BAB4-101A-B69C-00AA00341D07}"
                )
                IEnumConnectionPoints._iid_ = IID_IEnumConnectionPoints

                IEnumConnectionPoints._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'cConnections'),
                        (['out'], POINTER(LPCONNECTIONPOINT), 'ppCP'),
                        (['out'], POINTER(ULONG), 'pcFetched'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Skip')],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'cConnections'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Reset')],
                        HRESULT,
                        'Reset',
                    ),
                    COMMETHOD(
                        [helpstring('Method Clone')],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumConnectionPoints)),
                           'ppEnum'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumConnectionPoints_INTERFACE_DEFINED__

        if not defined(__IConnectionPointContainer_INTERFACE_DEFINED__):
            # interface IConnectionPointContainer
            # [unique][uuid][object]
            PCONNECTIONPOINTCONTAINER = POINTER(IConnectionPointContainer)
            LPCONNECTIONPOINTCONTAINER = POINTER(IConnectionPointContainer)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IConnectionPointContainer = MIDL_INTERFACE(
                    "{B196B284-BAB4-101A-B69C-00AA00341D07}"
                )
                IConnectionPointContainer._iid_ = IID_IConnectionPointContainer

                IConnectionPointContainer._methods_ = [
                    COMMETHOD(
                        [helpstring('Method EnumConnectionPoints')],
                        HRESULT,
                        'EnumConnectionPoints',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumConnectionPoints)),
                           'ppEnum'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method FindConnectionPoint')],
                        HRESULT,
                        'FindConnectionPoint',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(IConnectionPoint)), 'ppCP'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IConnectionPointContainer_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocidl_0000_0005
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IClassFactory2_INTERFACE_DEFINED__):
            # interface IClassFactory2
            # [unique][uuid][object]
            LPCLASSFACTORY2 = POINTER(IClassFactory2)

            tagLICINFO._fields_ = [
                ('cbLicInfo', LONG),
                ('fRuntimeKeyAvail', BOOL),
                ('fLicVerified', BOOL),
            ]
            LPLICINFO = POINTER(tagLICINFO)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IClassFactory2 = MIDL_INTERFACE(
                    "{B196B28F-BAB4-101A-B69C-00AA00341D07}"
                )
                IClassFactory2._iid_ = IID_IClassFactory2

                IClassFactory2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetLicInfo')],
                        HRESULT,
                        'GetLicInfo',
                        (['out', 'in'], POINTER(LICINFO), 'pLicInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RequestLicKey')],
                        HRESULT,
                        'RequestLicKey',
                        (['in'], DWORD, 'dwReserved'),
                        (['out'], POINTER(BSTR), 'pBstrKey'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CreateInstanceLic'), 'local'],
                        HRESULT,
                        'CreateInstanceLic',
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkOuter'),
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkReserved'),
                        (['in'], REFIID, 'riid'),
                        (['in'], BSTR, 'bstrKey'),
                        (['out'], POINTER(PVOID), 'ppvObj'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IClassFactory2_INTERFACE_DEFINED__

        if not defined(__IProvideClassInfo_INTERFACE_DEFINED__):
            # interface IProvideClassInfo
            # [unique][uuid][object]
            LPPROVIDECLASSINFO = POINTER(IProvideClassInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IProvideClassInfo = MIDL_INTERFACE(
                    "{B196B283-BAB4-101A-B69C-00AA00341D07}"
                )
                IProvideClassInfo._iid_ = IID_IProvideClassInfo

                IProvideClassInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetClassInfo')],
                        HRESULT,
                        'GetClassInfo',
                        (['out'], POINTER(POINTER(ITypeInfo)), 'ppTI'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IProvideClassInfo_INTERFACE_DEFINED__

        if not defined(__IProvideClassInfo2_INTERFACE_DEFINED__):
            # interface IProvideClassInfo2
            # [unique][uuid][object]
            LPPROVIDECLASSINFO2 = POINTER(IProvideClassInfo2)


            class tagGUIDKIND(ENUM):
                GUIDKIND_DEFAULT_SOURCE_DISP_IID = 1

            GUIDKIND = tagGUIDKIND
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IProvideClassInfo2 = MIDL_INTERFACE(
                    "{A6BC3AC0-DBAA-11CE-9DE3-00AA004BB851}"
                )
                IProvideClassInfo2._iid_ = IID_IProvideClassInfo2

                IProvideClassInfo2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetGUID')],
                        HRESULT,
                        'GetGUID',
                        (['in'], DWORD, 'dwGuidKind'),
                        (['out'], POINTER(GUID), 'pGUID'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IProvideClassInfo2_INTERFACE_DEFINED__

        if not defined(__IProvideMultipleClassInfo_INTERFACE_DEFINED__):
            # interface IProvideMultipleClassInfo
            # [unique][uuid][object]
            LPPROVIDEMULTIPLECLASSINFO = POINTER(IProvideMultipleClassInfo)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IProvideMultipleClassInfo = MIDL_INTERFACE(
                    "{A7ABA9C1-8983-11CF-8F20-00805F2CD064}"
                )
                IProvideMultipleClassInfo._iid_ = IID_IProvideMultipleClassInfo

                IProvideMultipleClassInfo._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetMultiTypeInfoCount')],
                        HRESULT,
                        'GetMultiTypeInfoCount',
                        (['out'], POINTER(ULONG), 'pcti'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetInfoOfIndex')],
                        HRESULT,
                        'GetInfoOfIndex',
                        (['in'], ULONG, 'iti'),
                        (['in'], DWORD, 'dwFlags'),
                        (['out'], POINTER(POINTER(ITypeInfo)), 'pptiCoClass'),
                        (['out'], POINTER(DWORD), 'pdwTIFlags'),
                        (['out'], POINTER(ULONG), 'pcdispidReserved'),
                        (['out'], POINTER(IID), 'piidPrimary'),
                        (['out'], POINTER(IID), 'piidSource'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IProvideMultipleClassInfo_INTERFACE_DEFINED__

        if not defined(__IOleControl_INTERFACE_DEFINED__):
            # interface IOleControl
            # [unique][uuid][object]
            LPOLECONTROL = POINTER(IOleControl)

            tagCONTROLINFO._fields_ = [
                ('cb', ULONG),
                ('hAccel', HACCEL),
                ('cAccel', USHORT),
                ('dwFlags', DWORD),
            ]
            LPCONTROLINFO = POINTER(tagCONTROLINFO)


            class tagCTRLINFO(ENUM):
                CTRLINFO_EATS_RETURN = 1
                CTRLINFO_EATS_ESCAPE = 2

            CTRLINFO = tagCTRLINFO
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleControl = MIDL_INTERFACE(
                    "{B196B288-BAB4-101A-B69C-00AA00341D07}"
                )
                IOleControl._iid_ = IID_IOleControl

                IOleControl._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetControlInfo')],
                        HRESULT,
                        'GetControlInfo',
                        (['out', 'in'], POINTER(CONTROLINFO), 'pCI'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnMnemonic')],
                        HRESULT,
                        'OnMnemonic',
                        (['in'], POINTER(MSG), 'pMsg'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnAmbientPropertyChange')],
                        HRESULT,
                        'OnAmbientPropertyChange',
                        (['in'], DISPID, 'dispID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FreezeEvents')],
                        HRESULT,
                        'FreezeEvents',
                        (['in'], BOOL, 'bFreeze'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleControl_INTERFACE_DEFINED__

        if not defined(__IOleControlSite_INTERFACE_DEFINED__):
            # interface IOleControlSite
            # [unique][uuid][object]
            LPOLECONTROLSITE = POINTER(IOleControlSite)

            tagPOINTF._fields_ = [
                ('x', FLOAT),
                ('y', FLOAT),
            ]
            LPPOINTF = POINTER(tagPOINTF)


            class tagXFORMCOORDS(ENUM):
                XFORMCOORDS_POSITION = 0x1
                XFORMCOORDS_SIZE = 0x2
                XFORMCOORDS_HIMETRICTOCONTAINER = 0x4
                XFORMCOORDS_CONTAINERTOHIMETRIC = 0x8
                XFORMCOORDS_EVENTCOMPAT = 0x10

            XFORMCOORDS = tagXFORMCOORDS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleControlSite = MIDL_INTERFACE(
                    "{B196B289-BAB4-101A-B69C-00AA00341D07}"
                )
                IOleControlSite._iid_ = IID_IOleControlSite

                IOleControlSite._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnControlInfoChanged')],
                        HRESULT,
                        'OnControlInfoChanged',
                    ),
                    COMMETHOD(
                        [helpstring('Method LockInPlaceActive')],
                        HRESULT,
                        'LockInPlaceActive',
                        (['in'], BOOL, 'fLock'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetExtendedControl')],
                        HRESULT,
                        'GetExtendedControl',
                        (['out'], POINTER(POINTER(IDispatch)), 'ppDisp'),
                    ),
                    COMMETHOD(
                        [helpstring('Method TransformCoords')],
                        HRESULT,
                        'TransformCoords',
                        (['out', 'in'], POINTER(POINTL), 'pPtlHimetric'),
                        (['out', 'in'], POINTER(POINTF), 'pPtfContainer'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method TranslateAccelerator')],
                        HRESULT,
                        'TranslateAccelerator',
                        (['in'], POINTER(MSG), 'pMsg'),
                        (['in'], DWORD, 'grfModifiers'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnFocus')],
                        HRESULT,
                        'OnFocus',
                        (['in'], BOOL, 'fGotFocus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ShowPropertyFrame')],
                        HRESULT,
                        'ShowPropertyFrame',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleControlSite_INTERFACE_DEFINED__

        if not defined(__IPropertyPage_INTERFACE_DEFINED__):
            # interface IPropertyPage
            # [unique][uuid][object]
            LPPROPERTYPAGE = POINTER(IPropertyPage)

            tagPROPPAGEINFO._fields_ = [
                ('cb', ULONG),
                ('pszTitle', LPOLESTR),
                ('size', SIZE),
                ('pszDocString', LPOLESTR),
                ('pszHelpFile', LPOLESTR),
                ('dwHelpContext', DWORD),
            ]
            LPPROPPAGEINFO = POINTER(tagPROPPAGEINFO)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyPage = MIDL_INTERFACE(
                    "{B196B28D-BAB4-101A-B69C-00AA00341D07}"
                )
                IPropertyPage._iid_ = IID_IPropertyPage

                IPropertyPage._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetPageSite')],
                        HRESULT,
                        'SetPageSite',
                        (['in'], POINTER(IPropertyPageSite), 'pPageSite'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Activate')],
                        HRESULT,
                        'Activate',
                        (['in'], HWND, 'hWndParent'),
                        (['in'], LPCRECT, 'pRect'),
                        (['in'], BOOL, 'bModal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Deactivate')],
                        HRESULT,
                        'Deactivate',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPageInfo')],
                        HRESULT,
                        'GetPageInfo',
                        (['out'], POINTER(PROPPAGEINFO), 'pPageInfo'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetObjects')],
                        HRESULT,
                        'SetObjects',
                        (['in'], ULONG, 'cObjects'),
                        (
                            ['in'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppUnk'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Show')],
                        HRESULT,
                        'Show',
                        (['in'], UINT, 'nCmdShow'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Move')],
                        HRESULT,
                        'Move',
                        (['in'], LPCRECT, 'pRect'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsPageDirty')],
                        HRESULT,
                        'IsPageDirty',
                    ),
                    COMMETHOD(
                        [helpstring('Method Apply')],
                        HRESULT,
                        'Apply',
                    ),
                    COMMETHOD(
                        [helpstring('Method Help')],
                        HRESULT,
                        'Help',
                        (['in'], LPCOLESTR, 'pszHelpDir'),
                    ),
                    COMMETHOD(
                        [helpstring('Method TranslateAccelerator')],
                        HRESULT,
                        'TranslateAccelerator',
                        (['in'], POINTER(MSG), 'pMsg'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyPage_INTERFACE_DEFINED__

        if not defined(__IPropertyPage2_INTERFACE_DEFINED__):
            # interface IPropertyPage2
            # [unique][uuid][object]
            LPPROPERTYPAGE2 = POINTER(IPropertyPage2)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyPage2 = MIDL_INTERFACE(
                    "{01E44665-24AC-101B-84ED-08002B2EC713}"
                )
                IPropertyPage2._iid_ = IID_IPropertyPage2

                IPropertyPage2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method EditProperty')],
                        HRESULT,
                        'EditProperty',
                        (['in'], DISPID, 'dispID'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyPage2_INTERFACE_DEFINED__

        if not defined(__IPropertyPageSite_INTERFACE_DEFINED__):
            # interface IPropertyPageSite
            # [unique][uuid][object]
            LPPROPERTYPAGESITE = POINTER(IPropertyPageSite)


            class tagPROPPAGESTATUS(ENUM):
                PROPPAGESTATUS_DIRTY = 0x1
                PROPPAGESTATUS_VALIDATE = 0x2
                PROPPAGESTATUS_CLEAN = 0x4

            PROPPAGESTATUS = tagPROPPAGESTATUS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyPageSite = MIDL_INTERFACE(
                    "{B196B28C-BAB4-101A-B69C-00AA00341D07}"
                )
                IPropertyPageSite._iid_ = IID_IPropertyPageSite

                IPropertyPageSite._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnStatusChange')],
                        HRESULT,
                        'OnStatusChange',
                        (['in'], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLocaleID')],
                        HRESULT,
                        'GetLocaleID',
                        (['out'], POINTER(LCID), 'pLocaleID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPageContainer')],
                        HRESULT,
                        'GetPageContainer',
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                           'ppUnk'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method TranslateAccelerator')],
                        HRESULT,
                        'TranslateAccelerator',
                        (['in'], POINTER(MSG), 'pMsg'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyPageSite_INTERFACE_DEFINED__

        if not defined(__IPropertyNotifySink_INTERFACE_DEFINED__):
            # interface IPropertyNotifySink
            # [unique][uuid][object]
            LPPROPERTYNOTIFYSINK = POINTER(IPropertyNotifySink)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyNotifySink = MIDL_INTERFACE(
                    "{9BFBBC02-EFF1-101A-84ED-00AA00341D07}"
                )
                IPropertyNotifySink._iid_ = IID_IPropertyNotifySink

                IPropertyNotifySink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnChanged')],
                        HRESULT,
                        'OnChanged',
                        (['in'], DISPID, 'dispID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnRequestEdit')],
                        HRESULT,
                        'OnRequestEdit',
                        (['in'], DISPID, 'dispID'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyNotifySink_INTERFACE_DEFINED__

        if not defined(__ISpecifyPropertyPages_INTERFACE_DEFINED__):
            # interface ISpecifyPropertyPages
            # [unique][uuid][object]
            LPSPECIFYPROPERTYPAGES = POINTER(ISpecifyPropertyPages)

            tagCAUUID._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(GUID)),
            ]
            LPCAUUID = POINTER(tagCAUUID)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpecifyPropertyPages = MIDL_INTERFACE(
                    "{B196B28B-BAB4-101A-B69C-00AA00341D07}"
                )
                ISpecifyPropertyPages._iid_ = IID_ISpecifyPropertyPages

                ISpecifyPropertyPages._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetPages')],
                        HRESULT,
                        'GetPages',
                        (['out'], POINTER(CAUUID), 'pPages'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpecifyPropertyPages_INTERFACE_DEFINED__

        if not defined(__IPersistMemory_INTERFACE_DEFINED__):
            # interface IPersistMemory
            # [unique][uuid][object]
            LPPERSISTMEMORY = POINTER(IPersistMemory)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistMemory = MIDL_INTERFACE(
                    "{BD1AE5E0-A6AE-11CE-BD37-504200C10000}"
                )
                IPersistMemory._iid_ = IID_IPersistMemory

                IPersistMemory._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsDirty')],
                        HRESULT,
                        'IsDirty',
                    ),
                    COMMETHOD(
                        [helpstring('Method Load'), 'local'],
                        HRESULT,
                        'Load',
                        (['in'], LPVOID, 'pMem'),
                        (['in'], ULONG, 'cbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Save'), 'local'],
                        HRESULT,
                        'Save',
                        (['out'], LPVOID, 'pMem'),
                        (['in'], BOOL, 'fClearDirty'),
                        (['in'], ULONG, 'cbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSizeMax')],
                        HRESULT,
                        'GetSizeMax',
                        (['out'], POINTER(ULONG), 'pCbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method InitNew')],
                        HRESULT,
                        'InitNew',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistMemory_INTERFACE_DEFINED__

        if not defined(__IPersistStreamInit_INTERFACE_DEFINED__):
            # interface IPersistStreamInit
            # [unique][uuid][object]
            LPPERSISTSTREAMINIT = POINTER(IPersistStreamInit)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistStreamInit = MIDL_INTERFACE(
                    "{7FD52380-4E07-101B-AE2D-08002B2EC713}"
                )
                IPersistStreamInit._iid_ = IID_IPersistStreamInit

                IPersistStreamInit._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsDirty')],
                        HRESULT,
                        'IsDirty',
                    ),
                    COMMETHOD(
                        [helpstring('Method Load')],
                        HRESULT,
                        'Load',
                        (['in'], LPSTREAM, 'pStm'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Save')],
                        HRESULT,
                        'Save',
                        (['in'], LPSTREAM, 'pStm'),
                        (['in'], BOOL, 'fClearDirty'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSizeMax')],
                        HRESULT,
                        'GetSizeMax',
                        (['out'], POINTER(ULARGE_INTEGER), 'pCbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method InitNew')],
                        HRESULT,
                        'InitNew',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistStreamInit_INTERFACE_DEFINED__

        if not defined(__IPersistPropertyBag_INTERFACE_DEFINED__):
            # interface IPersistPropertyBag
            # [unique][uuid][object]
            LPPERSISTPROPERTYBAG = POINTER(IPersistPropertyBag)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistPropertyBag = MIDL_INTERFACE(
                    "{37D84F60-42CB-11CE-8135-00AA004BB851}"
                )
                IPersistPropertyBag._iid_ = IID_IPersistPropertyBag

                IPersistPropertyBag._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InitNew')],
                        HRESULT,
                        'InitNew',
                    ),
                    COMMETHOD(
                        [helpstring('Method Load')],
                        HRESULT,
                        'Load',
                        (['in'], POINTER(IPropertyBag), 'pPropBag'),
                        (['unique', 'in'], POINTER(IErrorLog), 'pErrorLog'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Save')],
                        HRESULT,
                        'Save',
                        (['in'], POINTER(IPropertyBag), 'pPropBag'),
                        (['in'], BOOL, 'fClearDirty'),
                        (['in'], BOOL, 'fSaveAllProperties'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistPropertyBag_INTERFACE_DEFINED__

        if not defined(__ISimpleFrameSite_INTERFACE_DEFINED__):
            # interface ISimpleFrameSite
            # [unique][uuid][object]
            LPSIMPLEFRAMESITE = POINTER(ISimpleFrameSite)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISimpleFrameSite = MIDL_INTERFACE(
                    "{742B0E01-14E6-101B-914E-00AA00300CAB}"
                )
                ISimpleFrameSite._iid_ = IID_ISimpleFrameSite

                ISimpleFrameSite._methods_ = [
                    COMMETHOD(
                        [helpstring('Method PreMessageFilter')],
                        HRESULT,
                        'PreMessageFilter',
                        (['in'], HWND, 'hWnd'),
                        (['in'], UINT, 'msg'),
                        (['in'], WPARAM, 'wp'),
                        (['in'], LPARAM, 'lp'),
                        (['out'], POINTER(LRESULT), 'plResult'),
                        (['out'], POINTER(DWORD), 'pdwCookie'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PostMessageFilter')],
                        HRESULT,
                        'PostMessageFilter',
                        (['in'], HWND, 'hWnd'),
                        (['in'], UINT, 'msg'),
                        (['in'], WPARAM, 'wp'),
                        (['in'], LPARAM, 'lp'),
                        (['out'], POINTER(LRESULT), 'plResult'),
                        (['in'], DWORD, 'dwCookie'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISimpleFrameSite_INTERFACE_DEFINED__

        if not defined(__IFont_INTERFACE_DEFINED__):
            # interface IFont
            # [unique][uuid][object]
            LPFONT = POINTER(IFont)
            if (defined(_WIN32) or defined (_WIN64)) and not defined(OLE2ANSI):
                TEXTMETRICOLE = TEXTMETRICW
            else:
                from pyWinAPI.um.wingdi_h import TEXTMETRICA
                TEXTMETRICOLE = TEXTMETRICA
            # END IF

            LPTEXTMETRICOLE = POINTER(TEXTMETRICOLE)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IFont = MIDL_INTERFACE(
                    "{BEF6E002-A874-101A-8BBA-00AA00300CAB}"
                )
                IFont._iid_ = IID_IFont

                IFont._methods_ = [
                    COMMETHOD(
                        [helpstring('Method get_Name')],
                        HRESULT,
                        'get_Name',
                        (['out'], POINTER(BSTR), 'pName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Name')],
                        HRESULT,
                        'put_Name',
                        (['in'], BSTR, 'name'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Size')],
                        HRESULT,
                        'get_Size',
                        (['out'], POINTER(CY), 'pSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Size')],
                        HRESULT,
                        'put_Size',
                        (['in'], CY, 'size'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Bold')],
                        HRESULT,
                        'get_Bold',
                        (['out'], POINTER(BOOL), 'pBold'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Bold')],
                        HRESULT,
                        'put_Bold',
                        (['in'], BOOL, 'bold'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Italic')],
                        HRESULT,
                        'get_Italic',
                        (['out'], POINTER(BOOL), 'pItalic'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Italic')],
                        HRESULT,
                        'put_Italic',
                        (['in'], BOOL, 'italic'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Underline')],
                        HRESULT,
                        'get_Underline',
                        (['out'], POINTER(BOOL), 'pUnderline'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Underline')],
                        HRESULT,
                        'put_Underline',
                        (['in'], BOOL, 'underline'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Strikethrough')],
                        HRESULT,
                        'get_Strikethrough',
                        (['out'], POINTER(BOOL), 'pStrikethrough'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Strikethrough')],
                        HRESULT,
                        'put_Strikethrough',
                        (['in'], BOOL, 'strikethrough'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Weight')],
                        HRESULT,
                        'get_Weight',
                        (['out'], POINTER(SHORT), 'pWeight'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Weight')],
                        HRESULT,
                        'put_Weight',
                        (['in'], SHORT, 'weight'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Charset')],
                        HRESULT,
                        'get_Charset',
                        (['out'], POINTER(SHORT), 'pCharset'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_Charset')],
                        HRESULT,
                        'put_Charset',
                        (['in'], SHORT, 'charset'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_hFont')],
                        HRESULT,
                        'get_hFont',
                        (['out'], POINTER(HFONT), 'phFont'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Clone')],
                        HRESULT,
                        'Clone',
                        (['out'], POINTER(POINTER(IFont)), 'ppFont'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsEqual')],
                        HRESULT,
                        'IsEqual',
                        (['in'], POINTER(IFont), 'pFontOther'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetRatio')],
                        HRESULT,
                        'SetRatio',
                        (['in'], LONG, 'cyLogical'),
                        (['in'], LONG, 'cyHimetric'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueryTextMetrics')],
                        HRESULT,
                        'QueryTextMetrics',
                        (['out'], POINTER(TEXTMETRICOLE), 'pTM'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddRefHfont')],
                        HRESULT,
                        'AddRefHfont',
                        (['in'], HFONT, 'hFont'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseHfont')],
                        HRESULT,
                        'ReleaseHfont',
                        (['in'], HFONT, 'hFont'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetHdc')],
                        HRESULT,
                        'SetHdc',
                        (['in'], HDC, 'hDC'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IFont_INTERFACE_DEFINED__

        if not defined(__IPicture_INTERFACE_DEFINED__):
            # interface IPicture
            # [unique][uuid][object]
            LPPICTURE = POINTER(IPicture)

            class tagPictureAttributes(ENUM):
                PICTURE_SCALABLE = 0x1
                PICTURE_TRANSPARENT = 0x2

            PICTUREATTRIBUTES = tagPictureAttributes

            # typedef DECLSPEC_UUID("66504313-BE0F-101A-8BBB-00AA00300CAB") UINT OLE_HANDLE; // [public][uuid]
            OLE_HANDLE = DECLSPEC_UUID(
                "{66504313-BE0F-101A-8BBB-00AA00300CAB}"
            )

            # typedef DECLSPEC_UUID("66504306-BE0F-101A-8BBB-00AA00300CAB") LONG OLE_XPOS_HIMETRIC; // [hidden][uuid]
            OLE_XPOS_HIMETRIC = DECLSPEC_UUID(
                "{66504306-BE0F-101A-8BBB-00AA00300CAB}"
            )

            # typedef DECLSPEC_UUID("66504307-BE0F-101A-8BBB-00AA00300CAB") LONG OLE_YPOS_HIMETRIC; // [hidden][uuid]
            OLE_YPOS_HIMETRIC = DECLSPEC_UUID(
                "{66504307-BE0F-101A-8BBB-00AA00300CAB}"
            )

            # typedef DECLSPEC_UUID("66504308-BE0F-101A-8BBB-00AA00300CAB") LONG OLE_XSIZE_HIMETRIC; // [hidden][uuid]
            OLE_XSIZE_HIMETRIC = DECLSPEC_UUID(
                "{66504308-BE0F-101A-8BBB-00AA00300CAB}"
            )

            # typedef DECLSPEC_UUID("66504309-BE0F-101A-8BBB-00AA00300CAB") LONG OLE_YSIZE_HIMETRIC; // [hidden][uuid]
            OLE_YSIZE_HIMETRIC = DECLSPEC_UUID(
                "{66504309-BE0F-101A-8BBB-00AA00300CAB}"
            )

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPicture = MIDL_INTERFACE(
                    "{7BF80980-BF32-101A-8BBB-00AA00300CAB}"
                )
                IPicture._iid_ = IID_IPicture

                IPicture._methods_ = [
                    COMMETHOD(
                        [helpstring('Method get_Handle')],
                        HRESULT,
                        'get_Handle',
                        (['out'], POINTER(OLE_HANDLE), 'pHandle'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_hPal')],
                        HRESULT,
                        'get_hPal',
                        (['out'], POINTER(OLE_HANDLE), 'phPal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Type')],
                        HRESULT,
                        'get_Type',
                        (['out'], POINTER(SHORT), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Width')],
                        HRESULT,
                        'get_Width',
                        (['out'], POINTER(OLE_XSIZE_HIMETRIC), 'pWidth'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Height')],
                        HRESULT,
                        'get_Height',
                        (['out'], POINTER(OLE_YSIZE_HIMETRIC), 'pHeight'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Render')],
                        HRESULT,
                        'Render',
                        (['in'], HDC, 'hDC'),
                        (['in'], LONG, 'x'),
                        (['in'], LONG, 'y'),
                        (['in'], LONG, 'cx'),
                        (['in'], LONG, 'cy'),
                        (['in'], OLE_XPOS_HIMETRIC, 'xSrc'),
                        (['in'], OLE_YPOS_HIMETRIC, 'ySrc'),
                        (['in'], OLE_XSIZE_HIMETRIC, 'cxSrc'),
                        (['in'], OLE_YSIZE_HIMETRIC, 'cySrc'),
                        (['in'], LPCRECT, 'pRcWBounds'),
                    ),
                    COMMETHOD(
                        [helpstring('Method set_hPal')],
                        HRESULT,
                        'set_hPal',
                        (['in'], OLE_HANDLE, 'hPal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_CurDC')],
                        HRESULT,
                        'get_CurDC',
                        (['out'], POINTER(HDC), 'phDC'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SelectPicture')],
                        HRESULT,
                        'SelectPicture',
                        (['in'], HDC, 'hDCIn'),
                        (['out'], POINTER(HDC), 'phDCOut'),
                        (['out'], POINTER(OLE_HANDLE), 'phBmpOut'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_KeepOriginalFormat')],
                        HRESULT,
                        'get_KeepOriginalFormat',
                        (['out'], POINTER(BOOL), 'pKeep'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_KeepOriginalFormat')],
                        HRESULT,
                        'put_KeepOriginalFormat',
                        (['in'], BOOL, 'keep'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PictureChanged')],
                        HRESULT,
                        'PictureChanged',
                    ),
                    COMMETHOD(
                        [helpstring('Method SaveAsFile')],
                        HRESULT,
                        'SaveAsFile',
                        (['in'], LPSTREAM, 'pStream'),
                        (['in'], BOOL, 'fSaveMemCopy'),
                        (['out'], POINTER(LONG), 'pCbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Attributes')],
                        HRESULT,
                        'get_Attributes',
                        (['out'], POINTER(DWORD), 'pDwAttr'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPicture_INTERFACE_DEFINED__

        if not defined(__IPicture2_INTERFACE_DEFINED__):
            # interface IPicture2
            # [unique][uuid][object]
            LPPICTURE2 = POINTER(IPicture2)
            HHANDLE = UINT_PTR
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPicture2 = MIDL_INTERFACE(
                    "{F5185DD8-2012-4B0B-AAD9-F052C6BD482B}"
                )
                IPicture2._iid_ = IID_IPicture2

                IPicture2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method get_Handle')],
                        HRESULT,
                        'get_Handle',
                        (['out'], POINTER(HHANDLE), 'pHandle'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_hPal')],
                        HRESULT,
                        'get_hPal',
                        (['out'], POINTER(HHANDLE), 'phPal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Type')],
                        HRESULT,
                        'get_Type',
                        (['out'], POINTER(SHORT), 'pType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Width')],
                        HRESULT,
                        'get_Width',
                        (['out'], POINTER(OLE_XSIZE_HIMETRIC), 'pWidth'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Height')],
                        HRESULT,
                        'get_Height',
                        (['out'], POINTER(OLE_YSIZE_HIMETRIC), 'pHeight'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Render')],
                        HRESULT,
                        'Render',
                        (['in'], HDC, 'hDC'),
                        (['in'], LONG, 'x'),
                        (['in'], LONG, 'y'),
                        (['in'], LONG, 'cx'),
                        (['in'], LONG, 'cy'),
                        (['in'], OLE_XPOS_HIMETRIC, 'xSrc'),
                        (['in'], OLE_YPOS_HIMETRIC, 'ySrc'),
                        (['in'], OLE_XSIZE_HIMETRIC, 'cxSrc'),
                        (['in'], OLE_YSIZE_HIMETRIC, 'cySrc'),
                        (['in'], LPCRECT, 'pRcWBounds'),
                    ),
                    COMMETHOD(
                        [helpstring('Method set_hPal')],
                        HRESULT,
                        'set_hPal',
                        (['in'], HHANDLE, 'hPal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_CurDC')],
                        HRESULT,
                        'get_CurDC',
                        (['out'], POINTER(HDC), 'phDC'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SelectPicture')],
                        HRESULT,
                        'SelectPicture',
                        (['in'], HDC, 'hDCIn'),
                        (['out'], POINTER(HDC), 'phDCOut'),
                        (['out'], POINTER(HHANDLE), 'phBmpOut'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_KeepOriginalFormat')],
                        HRESULT,
                        'get_KeepOriginalFormat',
                        (['out'], POINTER(BOOL), 'pKeep'),
                    ),
                    COMMETHOD(
                        [helpstring('Method put_KeepOriginalFormat')],
                        HRESULT,
                        'put_KeepOriginalFormat',
                        (['in'], BOOL, 'keep'),
                    ),
                    COMMETHOD(
                        [helpstring('Method PictureChanged')],
                        HRESULT,
                        'PictureChanged',
                    ),
                    COMMETHOD(
                        [helpstring('Method SaveAsFile')],
                        HRESULT,
                        'SaveAsFile',
                        (['in'], LPSTREAM, 'pStream'),
                        (['in'], BOOL, 'fSaveMemCopy'),
                        (['out'], POINTER(LONG), 'pCbSize'),
                    ),
                    COMMETHOD(
                        [helpstring('Method get_Attributes')],
                        HRESULT,
                        'get_Attributes',
                        (['out'], POINTER(DWORD), 'pDwAttr'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPicture2_INTERFACE_DEFINED__

        if not defined(__IFontEventsDisp_INTERFACE_DEFINED__):
            # interface IFontEventsDisp
            # [unique][uuid][object]
            LPFONTEVENTS = POINTER(IFontEventsDisp)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IFontEventsDisp = MIDL_INTERFACE(
                    "{4EF6100A-AF88-11D0-9846-00C04FC29993}"
                )
                IFontEventsDisp._iid_ = IID_IFontEventsDisp

                IFontEventsDisp._methods_ = []

            # END IF  C style interface
        # END IF  __IFontEventsDisp_INTERFACE_DEFINED__

        if not defined(__IFontDisp_INTERFACE_DEFINED__):
            # interface IFontDisp
            # [unique][uuid][object]
            LPFONTDISP = POINTER(IFontDisp)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IFontDisp = MIDL_INTERFACE(
                    "{BEF6E003-A874-101A-8BBA-00AA00300CAB}"
                )
                IFontDisp._iid_ = IID_IFontDisp

                IFontDisp._methods_ = []

            # END IF  C style interface
        # END IF  __IFontDisp_INTERFACE_DEFINED__

        if not defined(__IPictureDisp_INTERFACE_DEFINED__):
            # interface IPictureDisp
            # [unique][uuid][object]
            LPPICTUREDISP = POINTER(IPictureDisp)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPictureDisp = MIDL_INTERFACE(
                    "{7BF80981-BF32-101A-8BBB-00AA00300CAB}"
                )
                IPictureDisp._iid_ = IID_IPictureDisp

                IPictureDisp._methods_ = []

            # END IF  C style interface
        # END IF  __IPictureDisp_INTERFACE_DEFINED__

        if not defined(__IOleInPlaceObjectWindowless_INTERFACE_DEFINED__):
            # interface IOleInPlaceObjectWindowless
            # [uuid][unique][object]
            LPOLEINPLACEOBJECTWINDOWLESS = POINTER(IOleInPlaceObjectWindowless)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleInPlaceObjectWindowless = MIDL_INTERFACE(
                    "{1C2056CC-5EF4-101B-8BC8-00AA003E3B29}"
                )
                IOleInPlaceObjectWindowless._iid_ = IID_IOleInPlaceObjectWindowless

                IOleInPlaceObjectWindowless._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnWindowMessage')],
                        HRESULT,
                        'OnWindowMessage',
                        (['in'], UINT, 'msg'),
                        (['in'], WPARAM, 'wParam'),
                        (['in'], LPARAM, 'lParam'),
                        (['out'], POINTER(LRESULT), 'plResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDropTarget')],
                        HRESULT,
                        'GetDropTarget',
                        (
                            ['out'],
                            POINTER(POINTER(IDropTarget)),
                           'ppDropTarget'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleInPlaceObjectWindowless_INTERFACE_DEFINED__

        if not defined(__IOleInPlaceSiteEx_INTERFACE_DEFINED__):
            # interface IOleInPlaceSiteEx
            # [uuid][unique][object]
            LPOLEINPLACESITEEX = POINTER(IOleInPlaceSiteEx)


            class tagACTIVATEFLAGS(ENUM):
                ACTIVATE_WINDOWLESS = 1

            ACTIVATEFLAGS = tagACTIVATEFLAGS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleInPlaceSiteEx = MIDL_INTERFACE(
                    "{9C2CAD80-3424-11CF-B670-00AA004CD6D8}"
                )
                IOleInPlaceSiteEx._iid_ = IID_IOleInPlaceSiteEx

                IOleInPlaceSiteEx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnInPlaceActivateEx')],
                        HRESULT,
                        'OnInPlaceActivateEx',
                        (['out'], POINTER(BOOL), 'pfNoRedraw'),
                        (['in'], DWORD, 'dwFlags'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnInPlaceDeactivateEx')],
                        HRESULT,
                        'OnInPlaceDeactivateEx',
                        (['in'], BOOL, 'fNoRedraw'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RequestUIActivate')],
                        HRESULT,
                        'RequestUIActivate',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleInPlaceSiteEx_INTERFACE_DEFINED__

        if not defined(__IOleInPlaceSiteWindowless_INTERFACE_DEFINED__):
            # interface IOleInPlaceSiteWindowless
            # [uuid][unique][object]
            LPOLEINPLACESITEWINDOWLESS = POINTER(IOleInPlaceSiteWindowless)


            class tagOLEDCFLAGS(ENUM):
                OLEDC_NODRAW = 0x1
                OLEDC_PAINTBKGND = 0x2
                OLEDC_OFFSCREEN = 0x4

            OLEDCFLAGS = tagOLEDCFLAGS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleInPlaceSiteWindowless = MIDL_INTERFACE(
                    "{922EADA0-3424-11CF-B670-00AA004CD6D8}"
                )
                IOleInPlaceSiteWindowless._iid_ = IID_IOleInPlaceSiteWindowless

                IOleInPlaceSiteWindowless._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CanWindowlessActivate')],
                        HRESULT,
                        'CanWindowlessActivate',
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCapture')],
                        HRESULT,
                        'GetCapture',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetCapture')],
                        HRESULT,
                        'SetCapture',
                        (['in'], BOOL, 'fCapture'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFocus')],
                        HRESULT,
                        'GetFocus',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFocus')],
                        HRESULT,
                        'SetFocus',
                        (['in'], BOOL, 'fFocus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDC')],
                        HRESULT,
                        'GetDC',
                        (['unique', 'in'], LPCRECT, 'pRect'),
                        (['in'], DWORD, 'grfFlags'),
                        (['out'], POINTER(HDC), 'phDC'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ReleaseDC')],
                        HRESULT,
                        'ReleaseDC',
                        (['in'], HDC, 'hDC'),
                    ),
                    COMMETHOD(
                        [helpstring('Method InvalidateRect')],
                        HRESULT,
                        'InvalidateRect',
                        (['unique', 'in'], LPCRECT, 'pRect'),
                        (['in'], BOOL, 'fErase'),
                    ),
                    COMMETHOD(
                        [helpstring('Method InvalidateRgn')],
                        HRESULT,
                        'InvalidateRgn',
                        (['in'], HRGN, 'hRGN'),
                        (['in'], BOOL, 'fErase'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ScrollRect')],
                        HRESULT,
                        'ScrollRect',
                        (['in'], INT, 'dx'),
                        (['in'], INT, 'dy'),
                        (['in'], LPCRECT, 'pRectScroll'),
                        (['in'], LPCRECT, 'pRectClip'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AdjustRect')],
                        HRESULT,
                        'AdjustRect',
                        (['out', 'in'], LPRECT, 'prc'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnDefWindowMessage')],
                        HRESULT,
                        'OnDefWindowMessage',
                        (['in'], UINT, 'msg'),
                        (['in'], WPARAM, 'wParam'),
                        (['in'], LPARAM, 'lParam'),
                        (['out'], POINTER(LRESULT), 'plResult'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleInPlaceSiteWindowless_INTERFACE_DEFINED__

        if not defined(__IViewObjectEx_INTERFACE_DEFINED__):
            # interface IViewObjectEx
            # [uuid][unique][object]
            LPVIEWOBJECTEX = POINTER(IViewObjectEx)


            class tagVIEWSTATUS(ENUM):
                VIEWSTATUS_OPAQUE = 1
                VIEWSTATUS_SOLIDBKGND = 2
                VIEWSTATUS_DVASPECTOPAQUE = 4
                VIEWSTATUS_DVASPECTTRANSPARENT = 8
                VIEWSTATUS_SURFACE = 16
                VIEWSTATUS_3DSURFACE = 32

            VIEWSTATUS = tagVIEWSTATUS


            class tagHITRESULT(ENUM):
                HITRESULT_OUTSIDE = 0
                HITRESULT_TRANSPARENT = 1
                HITRESULT_CLOSE = 2
                HITRESULT_HIT = 3

            HITRESULT = tagHITRESULT


            class tagDVASPECT2(ENUM):
                DVASPECT_OPAQUE = 16
                DVASPECT_TRANSPARENT = 32

            DVASPECT2 = tagDVASPECT2

            tagExtentInfo._fields_ = [
                ('cb', ULONG),
                ('dwExtentMode', DWORD),
                ('sizelProposed', SIZEL),
            ]


            class tagExtentMode(ENUM):
                DVEXTENT_CONTENT = 0
                DVEXTENT_INTEGRAL = DVEXTENT_CONTENT + 1
            DVEXTENTMODE = tagExtentMode


            class tagAspectInfoFlag(ENUM):
                DVASPECTINFOFLAG_CANOPTIMIZE = 1

            DVASPECTINFOFLAG = tagAspectInfoFlag

            tagAspectInfo._fields_ = [
                ('cb', ULONG),
                ('dwFlags', DWORD),
            ]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IViewObjectEx = MIDL_INTERFACE(
                    "{3AF24292-0C96-11CE-A0CF-00AA00600AB8}"
                )
                IViewObjectEx._iid_ = IID_IViewObjectEx

                IViewObjectEx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetRect')],
                        HRESULT,
                        'GetRect',
                        (['in'], DWORD, 'dwAspect'),
                        (['out'], LPRECTL, 'pRect'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetViewStatus')],
                        HRESULT,
                        'GetViewStatus',
                        (['out'], POINTER(DWORD), 'pdwStatus'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueryHitPoint')],
                        HRESULT,
                        'QueryHitPoint',
                        (['in'], DWORD, 'dwAspect'),
                        (['in'], LPCRECT, 'pRectBounds'),
                        (['in'], POINT, 'ptlLoc'),
                        (['in'], LONG, 'lCloseHint'),
                        (['out'], POINTER(DWORD), 'pHitResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method QueryHitRect')],
                        HRESULT,
                        'QueryHitRect',
                        (['in'], DWORD, 'dwAspect'),
                        (['in'], LPCRECT, 'pRectBounds'),
                        (['in'], LPCRECT, 'pRectLoc'),
                        (['in'], LONG, 'lCloseHint'),
                        (['out'], POINTER(DWORD), 'pHitResult'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetNaturalExtent')],
                        HRESULT,
                        'GetNaturalExtent',
                        (['in'], DWORD, 'dwAspect'),
                        (['in'], LONG, 'lindex'),
                        (['in'], POINTER(DVTARGETDEVICE), 'ptd'),
                        (['in'], HDC, 'hicTargetDev'),
                        (['in'], POINTER(DVEXTENTINFO), 'pExtentInfo'),
                        (['out'], LPSIZEL, 'pSizel'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IViewObjectEx_INTERFACE_DEFINED__

        if not defined(__IOleUndoUnit_INTERFACE_DEFINED__):
            # interface IOleUndoUnit
            # [uuid][unique][object]
            LPOLEUNDOUNIT = POINTER(IOleUndoUnit)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleUndoUnit = MIDL_INTERFACE(
                    "{894AD3B0-EF97-11CE-9BC9-00AA00608E01}"
                )
                IOleUndoUnit._iid_ = IID_IOleUndoUnit

                IOleUndoUnit._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Do')],
                        HRESULT,
                        'Do',
                        (['in'], POINTER(IOleUndoManager), 'pUndoManager'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetDescription')],
                        HRESULT,
                        'GetDescription',
                        (['out'], POINTER(BSTR), 'pBstr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetUnitType')],
                        HRESULT,
                        'GetUnitType',
                        (['out'], POINTER(CLSID), 'pClsid'),
                        (['out'], POINTER(LONG), 'plID'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnNextAdd')],
                        HRESULT,
                        'OnNextAdd',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleUndoUnit_INTERFACE_DEFINED__

        if not defined(__IOleParentUndoUnit_INTERFACE_DEFINED__):
            # interface IOleParentUndoUnit
            # [uuid][unique][object]
            LPOLEPARENTUNDOUNIT = POINTER(IOleParentUndoUnit)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleParentUndoUnit = MIDL_INTERFACE(
                    "{A1FAF330-EF97-11CE-9BC9-00AA00608E01}"
                )
                IOleParentUndoUnit._iid_ = IID_IOleParentUndoUnit

                IOleParentUndoUnit._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Open')],
                        HRESULT,
                        'Open',
                        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
                        (['in'], BOOL, 'fCommit'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Add')],
                        HRESULT,
                        'Add',
                        (['in'], POINTER(IOleUndoUnit), 'pUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FindUnit')],
                        HRESULT,
                        'FindUnit',
                        (['in'], POINTER(IOleUndoUnit), 'pUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetParentState')],
                        HRESULT,
                        'GetParentState',
                        (['out'], POINTER(DWORD), 'pdwState'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleParentUndoUnit_INTERFACE_DEFINED__

        if not defined(__IEnumOleUndoUnits_INTERFACE_DEFINED__):
            # interface IEnumOleUndoUnits
            # [uuid][unique][object]
            LPENUMOLEUNDOUNITS = POINTER(IEnumOleUndoUnits)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IEnumOleUndoUnits = MIDL_INTERFACE(
                    "{B3E7C340-EF97-11CE-9BC9-00AA00608E01}"
                )
                IEnumOleUndoUnits._iid_ = IID_IEnumOleUndoUnits

                IEnumOleUndoUnits._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Next'), 'local'],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'cElt'),
                        (['out'], POINTER(POINTER(IOleUndoUnit)), 'rgElt'),
                        (['out'], POINTER(ULONG), 'pcEltFetched'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Skip')],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'cElt'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Reset')],
                        HRESULT,
                        'Reset',
                    ),
                    COMMETHOD(
                        [helpstring('Method Clone')],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumOleUndoUnits)),
                           'ppEnum'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IEnumOleUndoUnits_INTERFACE_DEFINED__

        if not defined(__IOleUndoManager_INTERFACE_DEFINED__):
            # interface IOleUndoManager
            # [uuid][unique][object]
            LPOLEUNDOMANAGER = POINTER(IOleUndoManager)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IOleUndoManager = MIDL_INTERFACE(
                    "{D001F200-EF97-11CE-9BC9-00AA00608E01}"
                )
                IOleUndoManager._iid_ = IID_IOleUndoManager

                IOleUndoManager._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Open')],
                        HRESULT,
                        'Open',
                        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                        (['in'], POINTER(IOleParentUndoUnit), 'pPUU'),
                        (['in'], BOOL, 'fCommit'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Add')],
                        HRESULT,
                        'Add',
                        (['in'], POINTER(IOleUndoUnit), 'pUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetOpenParentState')],
                        HRESULT,
                        'GetOpenParentState',
                        (['out'], POINTER(DWORD), 'pdwState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DiscardFrom')],
                        HRESULT,
                        'DiscardFrom',
                        (['in'], POINTER(IOleUndoUnit), 'pUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method UndoTo')],
                        HRESULT,
                        'UndoTo',
                        (['in'], POINTER(IOleUndoUnit), 'pUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RedoTo')],
                        HRESULT,
                        'RedoTo',
                        (['in'], POINTER(IOleUndoUnit), 'pUU'),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumUndoable')],
                        HRESULT,
                        'EnumUndoable',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumOleUndoUnits)),
                           'ppEnum'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method EnumRedoable')],
                        HRESULT,
                        'EnumRedoable',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumOleUndoUnits)),
                           'ppEnum'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLastUndoDescription')],
                        HRESULT,
                        'GetLastUndoDescription',
                        (['out'], POINTER(BSTR), 'pBstr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetLastRedoDescription')],
                        HRESULT,
                        'GetLastRedoDescription',
                        (['out'], POINTER(BSTR), 'pBstr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Enable')],
                        HRESULT,
                        'Enable',
                        (['in'], BOOL, 'fEnable'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IOleUndoManager_INTERFACE_DEFINED__

        if not defined(__IPointerInactive_INTERFACE_DEFINED__):
            # interface IPointerInactive
            # [uuid][unique][object]
            LPPOINTERINACTIVE = POINTER(IPointerInactive)


            class tagPOINTERINACTIVE(ENUM):
                POINTERINACTIVE_ACTIVATEONENTRY = 1
                POINTERINACTIVE_DEACTIVATEONLEAVE = 2
                POINTERINACTIVE_ACTIVATEONDRAG = 4

            POINTERINACTIVE = tagPOINTERINACTIVE
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPointerInactive = MIDL_INTERFACE(
                    "{55980BA0-35AA-11CF-B671-00AA004CD6D8}"
                )
                IPointerInactive._iid_ = IID_IPointerInactive

                IPointerInactive._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetActivationPolicy')],
                        HRESULT,
                        'GetActivationPolicy',
                        (['out'], POINTER(DWORD), 'pdwPolicy'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnInactiveMouseMove')],
                        HRESULT,
                        'OnInactiveMouseMove',
                        (['in'], LPCRECT, 'pRectBounds'),
                        (['in'], LONG, 'x'),
                        (['in'], LONG, 'y'),
                        (['in'], DWORD, 'grfKeyState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method OnInactiveSetCursor')],
                        HRESULT,
                        'OnInactiveSetCursor',
                        (['in'], LPCRECT, 'pRectBounds'),
                        (['in'], LONG, 'x'),
                        (['in'], LONG, 'y'),
                        (['in'], DWORD, 'dwMouseMsg'),
                        (['in'], BOOL, 'fSetAlways'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPointerInactive_INTERFACE_DEFINED__

        if not defined(__IObjectWithSite_INTERFACE_DEFINED__):
            # interface IObjectWithSite
            # [unique][uuid][object]
            LPOBJECTWITHSITE = POINTER(IObjectWithSite)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IObjectWithSite = MIDL_INTERFACE(
                    "{FC4801A3-2BA9-11CF-A229-00AA003D7352}"
                )
                IObjectWithSite._iid_ = IID_IObjectWithSite

                IObjectWithSite._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetSite')],
                        HRESULT,
                        'SetSite',
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkSite'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSite')],
                        HRESULT,
                        'GetSite',
                        (['in'], REFIID, 'riid'),
                        (
                            ['iid_is', 'out'],
                            POINTER(POINTER(VOID)),
                           'ppvSite'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IObjectWithSite_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocidl_0000_0036
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IPerPropertyBrowsing_INTERFACE_DEFINED__):
            # interface IPerPropertyBrowsing
            # [unique][uuid][object]
            LPPERPROPERTYBROWSING = POINTER(IPerPropertyBrowsing)

            tagCALPOLESTR._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(LPOLESTR)),
            ]
            LPCALPOLESTR = POINTER(tagCALPOLESTR)

            tagCADWORD._fields_ = [
                ('cElems', ULONG),
                # [size_is]
                ('pElems', POINTER(DWORD)),
            ]
            LPCADWORD = POINTER(tagCADWORD)

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPerPropertyBrowsing = MIDL_INTERFACE(
                    "{376BD3AA-3845-101B-84ED-08002B2EC713}"
                )
                IPerPropertyBrowsing._iid_ = IID_IPerPropertyBrowsing

                IPerPropertyBrowsing._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetDisplayString')],
                        HRESULT,
                        'GetDisplayString',
                        (['in'], DISPID, 'dispID'),
                        (['out'], POINTER(BSTR), 'pBstr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method MapPropertyToPage')],
                        HRESULT,
                        'MapPropertyToPage',
                        (['in'], DISPID, 'dispID'),
                        (['out'], POINTER(CLSID), 'pClsid'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPredefinedStrings')],
                        HRESULT,
                        'GetPredefinedStrings',
                        (['in'], DISPID, 'dispID'),
                        (['out'], POINTER(CALPOLESTR), 'pCaStringsOut'),
                        (['out'], POINTER(CADWORD), 'pCaCookiesOut'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPredefinedValue')],
                        HRESULT,
                        'GetPredefinedValue',
                        (['in'], DISPID, 'dispID'),
                        (['in'], DWORD, 'dwCookie'),
                        (['out'], POINTER(VARIANT), 'pVarOut'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPerPropertyBrowsing_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocidl_0000_0037
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IPropertyBag2_INTERFACE_DEFINED__):
            # interface IPropertyBag2
            # [unique][uuid][object]
            LPPROPERTYBAG2 = POINTER(IPropertyBag2)


            class tagPROPBAG2_TYPE(ENUM):
                PROPBAG2_TYPE_UNDEFINED = 0
                PROPBAG2_TYPE_DATA = 1
                PROPBAG2_TYPE_URL = 2
                PROPBAG2_TYPE_OBJECT = 3
                PROPBAG2_TYPE_STREAM = 4
                PROPBAG2_TYPE_STORAGE = 5
                PROPBAG2_TYPE_MONIKER = 6

            PROPBAG2_TYPE = tagPROPBAG2_TYPE

            tagPROPBAG2._fields_ = [
                ('dwType', DWORD),
                ('vt', VARTYPE),
                ('cfType', CLIPFORMAT),
                ('dwHint', DWORD),
                ('pstrName', LPOLESTR),
                ('clsid', CLSID),
            ]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPropertyBag2 = MIDL_INTERFACE(
                    "{22F55882-280B-11D0-A8A9-00A0C90C2004}"
                )
                IPropertyBag2._iid_ = IID_IPropertyBag2

                IPropertyBag2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Read')],
                        HRESULT,
                        'Read',
                        (['in'], ULONG, 'cProperties'),
                        (['in'], POINTER(PROPBAG2), 'pPropBag'),
                        (['unique', 'in'], POINTER(IErrorLog), 'pErrLog'),
                        (['out'], POINTER(VARIANT), 'pvarValue'),
                        (
                            ['out', 'unique', 'in'],
                            POINTER(HRESULT),
                           'phrError'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Write')],
                        HRESULT,
                        'Write',
                        (['in'], ULONG, 'cProperties'),
                        (['in'], POINTER(PROPBAG2), 'pPropBag'),
                        (['in'], POINTER(VARIANT), 'pvarValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CountProperties')],
                        HRESULT,
                        'CountProperties',
                        (['out'], POINTER(ULONG), 'pcProperties'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyInfo')],
                        HRESULT,
                        'GetPropertyInfo',
                        (['in'], ULONG, 'iProperty'),
                        (['in'], ULONG, 'cProperties'),
                        (['out'], POINTER(PROPBAG2), 'pPropBag'),
                        (['out'], POINTER(ULONG), 'pcProperties'),
                    ),
                    COMMETHOD(
                        [helpstring('Method LoadObject')],
                        HRESULT,
                        'LoadObject',
                        (['in'], LPCOLESTR, 'pstrName'),
                        (['in'], DWORD, 'dwHint'),
                        (['in'], POINTER(comtypes.IUnknown), 'pUnkObject'),
                        (['unique', 'in'], POINTER(IErrorLog), 'pErrLog'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPropertyBag2_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocidl_0000_0038
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IPersistPropertyBag2_INTERFACE_DEFINED__):
            # interface IPersistPropertyBag2
            # [unique][uuid][object]
            LPPERSISTPROPERTYBAG2 = POINTER(IPersistPropertyBag2)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IPersistPropertyBag2 = MIDL_INTERFACE(
                    "{22F55881-280B-11D0-A8A9-00A0C90C2004}"
                )
                IPersistPropertyBag2._iid_ = IID_IPersistPropertyBag2

                IPersistPropertyBag2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method InitNew')],
                        HRESULT,
                        'InitNew',
                    ),
                    COMMETHOD(
                        [helpstring('Method Load')],
                        HRESULT,
                        'Load',
                        (['in'], POINTER(IPropertyBag2), 'pPropBag'),
                        (['unique', 'in'], POINTER(IErrorLog), 'pErrLog'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Save')],
                        HRESULT,
                        'Save',
                        (['in'], POINTER(IPropertyBag2), 'pPropBag'),
                        (['in'], BOOL, 'fClearDirty'),
                        (['in'], BOOL, 'fSaveAllProperties'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsDirty')],
                        HRESULT,
                        'IsDirty',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IPersistPropertyBag2_INTERFACE_DEFINED__

        # interface __MIDL_itf_ocidl_0000_0039
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IAdviseSinkEx_INTERFACE_DEFINED__):
            # interface IAdviseSinkEx
            # [uuid][unique][object]
            LPADVISESINKEX = POINTER(IAdviseSinkEx)
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IAdviseSinkEx = MIDL_INTERFACE(
                    "{3AF24290-0C96-11CE-A0CF-00AA00600AB8}"
                )
                IAdviseSinkEx._iid_ = IID_IAdviseSinkEx

                IAdviseSinkEx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method OnViewStatusChange'), 'local'],
                        VOID,
                        'OnViewStatusChange',
                        (['in'], DWORD, 'dwViewStatus'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IAdviseSinkEx_INTERFACE_DEFINED__
        # interface __MIDL_itf_ocidl_0000_0040
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM):
        if not defined(__IQuickActivate_INTERFACE_DEFINED__):
            # interface IQuickActivate
            # [uuid][unique][object]
            LPQUICKACTIVATE = POINTER(IQuickActivate)


            class tagQACONTAINERFLAGS(ENUM):
                QACONTAINER_SHOWHATCHING = 0x1
                QACONTAINER_SHOWGRABHANDLES = 0x2
                QACONTAINER_USERMODE = 0x4
                QACONTAINER_DISPLAYASDEFAULT = 0x8
                QACONTAINER_UIDEAD = 0x10
                QACONTAINER_AUTOCLIP = 0x20
                QACONTAINER_MESSAGEREFLECT = 0x40
                QACONTAINER_SUPPORTSMNEMONICS = 0x80

            QACONTAINERFLAGS = tagQACONTAINERFLAGS

            # typedef DECLSPEC_UUID("66504301-BE0F-101A-8BBB-00AA00300CAB") DWORD OLE_COLOR; // [public][uuid]
            OLE_COLOR = DECLSPEC_UUID(
                "{66504301-BE0F-101A-8BBB-00AA00300CAB}"
            )

            tagQACONTAINER._fields_ = [
                ('cbSize', ULONG),
                ('pClientSite', POINTER(IOleClientSite)),
                ('pAdviseSink', POINTER(IAdviseSinkEx)),
                ('pPropertyNotifySink', POINTER(IPropertyNotifySink)),
                ('pUnkEventSink', POINTER(comtypes.IUnknown)),
                ('dwAmbientFlags', DWORD),
                ('colorFore', OLE_COLOR),
                ('colorBack', OLE_COLOR),
                ('pFont', POINTER(IFont)),
                ('pUndoMgr', POINTER(IOleUndoManager)),
                ('dwAppearance', DWORD),
                ('lcid', LONG),
                ('hpal', HPALETTE),
                ('pBindHost', POINTER(IBindHost)),
                ('pOleControlSite', POINTER(IOleControlSite)),
                ('pServiceProvider', POINTER(IServiceProvider)),
            ]

            tagQACONTROL._fields_ = [
                ('cbSize', ULONG),
                ('dwMiscStatus', DWORD),
                ('dwViewStatus', DWORD),
                ('dwEventCookie', DWORD),
                ('dwPropNotifyCookie', DWORD),
                ('dwPointerActivationPolicy', DWORD),
            ]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IQuickActivate = MIDL_INTERFACE(
                    "{CF51ED10-62FE-11CF-BF86-00A0C9034836}"
                )
                IQuickActivate._iid_ = IID_IQuickActivate

                IQuickActivate._methods_ = [
                    COMMETHOD(
                        [helpstring('Method QuickActivate'), 'local'],
                        HRESULT,
                        'QuickActivate',
                        (['in'], POINTER(QACONTAINER), 'pQaContainer'),
                        (['in', 'out'], POINTER(QACONTROL), 'pQaControl'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetContentExtent')],
                        HRESULT,
                        'SetContentExtent',
                        (['in'], LPSIZEL, 'pSizel'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetContentExtent')],
                        HRESULT,
                        'GetContentExtent',
                        (['out'], LPSIZEL, 'pSizel'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IQuickActivate_INTERFACE_DEFINED__
        # interface __MIDL_itf_ocidl_0000_0041
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    if _MSC_VER >= 1200:
        pass
    # END IF

    # Additional Prototypes for ALL interfaces
    oleaut32 = ctypes.windll.OLEAUT32

    # ULONG              BSTR_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize = oleaut32.BSTR_UserSize
    BSTR_UserSize.restype = ULONG

    # UCHAR *  BSTR_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal = oleaut32.BSTR_UserMarshal
    BSTR_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  BSTR_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal = oleaut32.BSTR_UserUnmarshal
    BSTR_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       BSTR_UserFree(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree = oleaut32.BSTR_UserFree
    BSTR_UserFree.restype = VOID

    ole32 = ctypes.windll.OLE32

    # ULONG              CLIPFORMAT_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserSize = ole32.CLIPFORMAT_UserSize
    CLIPFORMAT_UserSize.restype = ULONG

    # UCHAR *  CLIPFORMAT_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserMarshal = ole32.CLIPFORMAT_UserMarshal
    CLIPFORMAT_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  CLIPFORMAT_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out CLIPFORMAT * );
    CLIPFORMAT_UserUnmarshal = ole32.CLIPFORMAT_UserUnmarshal
    CLIPFORMAT_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       CLIPFORMAT_UserFree(     __RPC__in ULONG *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserFree = ole32.CLIPFORMAT_UserFree
    CLIPFORMAT_UserFree.restype = VOID

    # ULONG              HACCEL_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in HACCEL * );
    HACCEL_UserSize = ole32.HACCEL_UserSize
    HACCEL_UserSize.restype = ULONG

    # UCHAR *  HACCEL_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HACCEL * );
    HACCEL_UserMarshal = ole32.HACCEL_UserMarshal
    HACCEL_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  HACCEL_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HACCEL * );
    HACCEL_UserUnmarshal = ole32.HACCEL_UserUnmarshal
    HACCEL_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       HACCEL_UserFree(     __RPC__in ULONG *, __RPC__in HACCEL * );
    HACCEL_UserFree = ole32.HACCEL_UserFree
    HACCEL_UserFree.restype = VOID

    # ULONG              HDC_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in HDC * );
    HDC_UserSize = ole32.HDC_UserSize
    HDC_UserSize.restype = ULONG

    # UCHAR *  HDC_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HDC * );
    HDC_UserMarshal = ole32.HDC_UserMarshal
    HDC_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  HDC_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HDC * );
    HDC_UserUnmarshal = ole32.HDC_UserUnmarshal
    HDC_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       HDC_UserFree(     __RPC__in ULONG *, __RPC__in HDC * );
    HDC_UserFree = ole32.HDC_UserFree
    HDC_UserFree.restype = VOID

    # ULONG              HPALETTE_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in HPALETTE * );
    HPALETTE_UserSize = ole32.HPALETTE_UserSize
    HPALETTE_UserSize.restype = ULONG

    # UCHAR *  HPALETTE_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HPALETTE * );
    HPALETTE_UserMarshal = ole32.HPALETTE_UserMarshal
    HPALETTE_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  HPALETTE_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HPALETTE * );
    HPALETTE_UserUnmarshal = ole32.HPALETTE_UserUnmarshal
    HPALETTE_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       HPALETTE_UserFree(     __RPC__in ULONG *, __RPC__in HPALETTE * );
    HPALETTE_UserFree = ole32.HPALETTE_UserFree
    HPALETTE_UserFree.restype = VOID

    # ULONG              HRGN_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in HRGN * );
    HRGN_UserSize = ole32.HRGN_UserSize
    HRGN_UserSize.restype = ULONG

    # UCHAR *  HRGN_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HRGN * );
    HRGN_UserMarshal = ole32.HRGN_UserMarshal
    HRGN_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  HRGN_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HRGN * );
    HRGN_UserUnmarshal = ole32.HRGN_UserUnmarshal
    HRGN_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       HRGN_UserFree(     __RPC__in ULONG *, __RPC__in HRGN * );
    HRGN_UserFree = ole32.HRGN_UserFree
    HRGN_UserFree.restype = VOID

    # ULONG              HWND_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in HWND * );
    HWND_UserSize = ole32.HWND_UserSize
    HWND_UserSize.restype = ULONG

    # UCHAR *  HWND_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HWND * );
    HWND_UserMarshal = ole32.HWND_UserMarshal
    HWND_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  HWND_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HWND * );
    HWND_UserUnmarshal = ole32.HWND_UserUnmarshal
    HWND_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       HWND_UserFree(     __RPC__in ULONG *, __RPC__in HWND * );
    HWND_UserFree = ole32.HWND_UserFree
    HWND_UserFree.restype = VOID

    # ULONG              VARIANT_UserSize(     __RPC__in ULONG *, ULONG            , __RPC__in VARIANT * );
    VARIANT_UserSize = oleaut32.VARIANT_UserSize
    VARIANT_UserSize.restype = ULONG

    # UCHAR *  VARIANT_UserMarshal(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal = oleaut32.VARIANT_UserMarshal
    VARIANT_UserMarshal.restype = POINTER(UCHAR)

    # UCHAR *  VARIANT_UserUnmarshal(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal = oleaut32.VARIANT_UserUnmarshal
    VARIANT_UserUnmarshal.restype = POINTER(UCHAR)

    # VOID                       VARIANT_UserFree(     __RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree = oleaut32.VARIANT_UserFree
    VARIANT_UserFree.restype = VOID

    # ULONG              BSTR_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in BSTR * );
    BSTR_UserSize64 = oleaut32.BSTR_UserSize64
    BSTR_UserSize64.restype = ULONG

    # UCHAR *  BSTR_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in BSTR * );
    BSTR_UserMarshal64 = oleaut32.BSTR_UserMarshal64
    BSTR_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  BSTR_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out BSTR * );
    BSTR_UserUnmarshal64 = oleaut32.BSTR_UserUnmarshal64
    BSTR_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                      BSTR_UserFree64(     __RPC__in ULONG *, __RPC__in BSTR * );
    BSTR_UserFree64 = oleaut32.BSTR_UserFree64
    BSTR_UserFree64.restype = VOID

    # ULONG              CLIPFORMAT_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserSize64 = ole32.CLIPFORMAT_UserSize64
    CLIPFORMAT_UserSize64.restype = ULONG

    # UCHAR *  CLIPFORMAT_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserMarshal64 = ole32.CLIPFORMAT_UserMarshal64
    CLIPFORMAT_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  CLIPFORMAT_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out CLIPFORMAT * );
    CLIPFORMAT_UserUnmarshal64 = ole32.CLIPFORMAT_UserUnmarshal64
    CLIPFORMAT_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       CLIPFORMAT_UserFree64(     __RPC__in ULONG *, __RPC__in CLIPFORMAT * );
    CLIPFORMAT_UserFree64 = ole32.CLIPFORMAT_UserFree64
    CLIPFORMAT_UserFree64.restype = VOID

    # ULONG              HACCEL_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in HACCEL * );
    HACCEL_UserSize64 = ole32.HACCEL_UserSize64
    HACCEL_UserSize64.restype = ULONG

    # UCHAR *  HACCEL_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HACCEL * );
    HACCEL_UserMarshal64 = ole32.HACCEL_UserMarshal64
    HACCEL_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  HACCEL_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HACCEL * );
    HACCEL_UserUnmarshal64 = ole32.HACCEL_UserUnmarshal64
    HACCEL_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       HACCEL_UserFree64(     __RPC__in ULONG *, __RPC__in HACCEL * );
    HACCEL_UserFree64 = ole32.HACCEL_UserFree64
    HACCEL_UserFree64.restype = VOID

    # ULONG              HDC_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in HDC * );
    HDC_UserSize64 = ole32.HDC_UserSize64
    HDC_UserSize64.restype = ULONG

    # UCHAR *  HDC_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HDC * );
    HDC_UserMarshal64 = ole32.HDC_UserMarshal64
    HDC_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  HDC_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HDC * );
    HDC_UserUnmarshal64 = ole32.HDC_UserUnmarshal64
    HDC_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       HDC_UserFree64(     __RPC__in ULONG *, __RPC__in HDC * );
    HDC_UserFree64 = ole32.HDC_UserFree64
    HDC_UserFree64.restype = VOID

    # ULONG              HPALETTE_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in HPALETTE * );
    HPALETTE_UserSize64 = ole32.HPALETTE_UserSize64
    HPALETTE_UserSize64.restype = ULONG

    # UCHAR *  HPALETTE_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HPALETTE * );
    HPALETTE_UserMarshal64 = ole32.HPALETTE_UserMarshal64
    HPALETTE_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  HPALETTE_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HPALETTE * );
    HPALETTE_UserUnmarshal64 = ole32.HPALETTE_UserUnmarshal64
    HPALETTE_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       HPALETTE_UserFree64(     __RPC__in ULONG *, __RPC__in HPALETTE * );
    HPALETTE_UserFree64 = ole32.HPALETTE_UserFree64
    HPALETTE_UserFree64.restype = VOID

    # ULONG              HRGN_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in HRGN * );
    HRGN_UserSize64 = oleaut32.HRGN_UserSize64
    HRGN_UserSize64.restype = ULONG

    # UCHAR *  HRGN_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HRGN * );
    HRGN_UserMarshal64 = oleaut32.HRGN_UserMarshal64
    HRGN_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  HRGN_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HRGN * );
    HRGN_UserUnmarshal64 = oleaut32.HRGN_UserUnmarshal64
    HRGN_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       HRGN_UserFree64(     __RPC__in ULONG *, __RPC__in HRGN * );
    HRGN_UserFree64 = oleaut32.HRGN_UserFree64
    HRGN_UserFree64.restype = VOID

    # ULONG              HWND_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in HWND * );
    HWND_UserSize64 = ole32.HWND_UserSize64
    HWND_UserSize64.restype = ULONG

    # UCHAR *  HWND_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in HWND * );
    HWND_UserMarshal64 = ole32.HWND_UserMarshal64
    HWND_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  HWND_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out HWND * );
    HWND_UserUnmarshal64 = ole32.HWND_UserUnmarshal64
    HWND_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       HWND_UserFree64(     __RPC__in ULONG *, __RPC__in HWND * );
    HWND_UserFree64 = ole32.HWND_UserFree64
    HWND_UserFree64.restype = VOID

    # ULONG              VARIANT_UserSize64(     __RPC__in ULONG *, ULONG            , __RPC__in VARIANT * );
    VARIANT_UserSize64 = oleaut32.VARIANT_UserSize64
    VARIANT_UserSize64.restype = ULONG

    # UCHAR *  VARIANT_UserMarshal64(  __RPC__in ULONG *, __RPC__inout_xcount(0) UCHAR *, __RPC__in VARIANT * );
    VARIANT_UserMarshal64 = oleaut32.VARIANT_UserMarshal64
    VARIANT_UserMarshal64.restype = POINTER(UCHAR)

    # UCHAR *  VARIANT_UserUnmarshal64(__RPC__in ULONG *, __RPC__in_xcount(0) UCHAR *, __RPC__out VARIANT * );
    VARIANT_UserUnmarshal64 = oleaut32.VARIANT_UserUnmarshal64
    VARIANT_UserUnmarshal64.restype = POINTER(UCHAR)

    # VOID                       VARIANT_UserFree64(     __RPC__in ULONG *, __RPC__in VARIANT * );
    VARIANT_UserFree64 = oleaut32.VARIANT_UserFree64
    VARIANT_UserFree64.restype = VOID

   # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


