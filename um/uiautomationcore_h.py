import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *

import comtypes

COMMETHOD = comtypees.COMMETHOD
helpstring = comtypees.helpstring


__REQUIRED_RPCNDR_H_VERSION__ = None
__REQUIRED_RPCSAL_H_VERSION__ = None
__RPCNDR_H_VERSION__ = None
__uiautomationcore_h__ = None
__IRawElementProviderSimple_FWD_DEFINED__ = None
__IAccessibleEx_FWD_DEFINED__ = None
__IRawElementProviderSimple2_FWD_DEFINED__ = None
__IRawElementProviderSimple3_FWD_DEFINED__ = None
__IRawElementProviderFragmentRoot_FWD_DEFINED__ = None
__IRawElementProviderFragment_FWD_DEFINED__ = None
__IRawElementProviderAdviseEvents_FWD_DEFINED__ = None
__IRawElementProviderHwndOverride_FWD_DEFINED__ = None
__IProxyProviderWinEventSink_FWD_DEFINED__ = None
__IProxyProviderWinEventHandler_FWD_DEFINED__ = None
__IRawElementProviderWindowlessSite_FWD_DEFINED__ = None
__IAccessibleHostingElementProviders_FWD_DEFINED__ = None
__IRawElementProviderHostingAccessibles_FWD_DEFINED__ = None
__IDockProvider_FWD_DEFINED__ = None
__IExpandCollapseProvider_FWD_DEFINED__ = None
__IGridProvider_FWD_DEFINED__ = None
__IGridItemProvider_FWD_DEFINED__ = None
__IInvokeProvider_FWD_DEFINED__ = None
__IMultipleViewProvider_FWD_DEFINED__ = None
__IRangeValueProvider_FWD_DEFINED__ = None
__IScrollItemProvider_FWD_DEFINED__ = None
__ISelectionProvider_FWD_DEFINED__ = None
__ISelectionProvider2_FWD_DEFINED__ = None
__IScrollProvider_FWD_DEFINED__ = None
__ISelectionItemProvider_FWD_DEFINED__ = None
__ISynchronizedInputProvider_FWD_DEFINED__ = None
__ITableProvider_FWD_DEFINED__ = None
__ITableItemProvider_FWD_DEFINED__ = None
__IToggleProvider_FWD_DEFINED__ = None
__ITransformProvider_FWD_DEFINED__ = None
__IValueProvider_FWD_DEFINED__ = None
__IWindowProvider_FWD_DEFINED__ = None
__ILegacyIAccessibleProvider_FWD_DEFINED__ = None
__IItemContainerProvider_FWD_DEFINED__ = None
__IVirtualizedItemProvider_FWD_DEFINED__ = None
__IObjectModelProvider_FWD_DEFINED__ = None
__IAnnotationProvider_FWD_DEFINED__ = None
__IStylesProvider_FWD_DEFINED__ = None
__ISpreadsheetProvider_FWD_DEFINED__ = None
__ISpreadsheetItemProvider_FWD_DEFINED__ = None
__ITransformProvider2_FWD_DEFINED__ = None
__IDragProvider_FWD_DEFINED__ = None
__IDropTargetProvider_FWD_DEFINED__ = None
__ITextRangeProvider_FWD_DEFINED__ = None
__ITextProvider_FWD_DEFINED__ = None
__ITextProvider2_FWD_DEFINED__ = None
__ITextEditProvider_FWD_DEFINED__ = None
__ITextRangeProvider2_FWD_DEFINED__ = None
__ITextChildProvider_FWD_DEFINED__ = None
__ICustomNavigationProvider_FWD_DEFINED__ = None
__IUIAutomationPatternInstance_FWD_DEFINED__ = None
__IUIAutomationPatternHandler_FWD_DEFINED__ = None
__IUIAutomationRegistrar_FWD_DEFINED__ = None
__CUIAutomationRegistrar_FWD_DEFINED__ = None
__UIA_LIBRARY_DEFINED__ = None
__UIA_OtherConstants_MODULE_DEFINED__ = None
__IRawElementProviderSimple_INTERFACE_DEFINED__ = None
__IAccessibleEx_INTERFACE_DEFINED__ = None
__IRawElementProviderSimple2_INTERFACE_DEFINED__ = None
__IRawElementProviderSimple3_INTERFACE_DEFINED__ = None
__IRawElementProviderFragmentRoot_INTERFACE_DEFINED__ = None
__IRawElementProviderFragment_INTERFACE_DEFINED__ = None
__IRawElementProviderAdviseEvents_INTERFACE_DEFINED__ = None
__IRawElementProviderHwndOverride_INTERFACE_DEFINED__ = None
__IProxyProviderWinEventSink_INTERFACE_DEFINED__ = None
__IProxyProviderWinEventHandler_INTERFACE_DEFINED__ = None
__IRawElementProviderWindowlessSite_INTERFACE_DEFINED__ = None
__IAccessibleHostingElementProviders_INTERFACE_DEFINED__ = None
__IRawElementProviderHostingAccessibles_INTERFACE_DEFINED__ = None
__IDockProvider_INTERFACE_DEFINED__ = None
__IExpandCollapseProvider_INTERFACE_DEFINED__ = None
__IGridProvider_INTERFACE_DEFINED__ = None
__IGridItemProvider_INTERFACE_DEFINED__ = None
__IInvokeProvider_INTERFACE_DEFINED__ = None
__IMultipleViewProvider_INTERFACE_DEFINED__ = None
__IRangeValueProvider_INTERFACE_DEFINED__ = None
__IScrollItemProvider_INTERFACE_DEFINED__ = None
__ISelectionProvider_INTERFACE_DEFINED__ = None
__ISelectionProvider2_INTERFACE_DEFINED__ = None
__IScrollProvider_INTERFACE_DEFINED__ = None
__ISelectionItemProvider_INTERFACE_DEFINED__ = None
__ISynchronizedInputProvider_INTERFACE_DEFINED__ = None
__ITableProvider_INTERFACE_DEFINED__ = None
__ITableItemProvider_INTERFACE_DEFINED__ = None
__IToggleProvider_INTERFACE_DEFINED__ = None
__ITransformProvider_INTERFACE_DEFINED__ = None
__IValueProvider_INTERFACE_DEFINED__ = None
__IWindowProvider_INTERFACE_DEFINED__ = None
__ILegacyIAccessibleProvider_INTERFACE_DEFINED__ = None
__IItemContainerProvider_INTERFACE_DEFINED__ = None
__IVirtualizedItemProvider_INTERFACE_DEFINED__ = None
__IObjectModelProvider_INTERFACE_DEFINED__ = None
__IAnnotationProvider_INTERFACE_DEFINED__ = None
__IStylesProvider_INTERFACE_DEFINED__ = None
__ISpreadsheetProvider_INTERFACE_DEFINED__ = None
__ISpreadsheetItemProvider_INTERFACE_DEFINED__ = None
__ITransformProvider2_INTERFACE_DEFINED__ = None
__IDragProvider_INTERFACE_DEFINED__ = None
__IDropTargetProvider_INTERFACE_DEFINED__ = None
__ITextRangeProvider_INTERFACE_DEFINED__ = None
__ITextProvider_INTERFACE_DEFINED__ = None
__ITextProvider2_INTERFACE_DEFINED__ = None
__ITextEditProvider_INTERFACE_DEFINED__ = None
__ITextRangeProvider2_INTERFACE_DEFINED__ = None
__ITextChildProvider_INTERFACE_DEFINED__ = None
__ICustomNavigationProvider_INTERFACE_DEFINED__ = None
__IUIAutomationPatternInstance_INTERFACE_DEFINED__ = None
__IUIAutomationPatternHandler_INTERFACE_DEFINED__ = None
__IUIAutomationRegistrar_INTERFACE_DEFINED__ = None


class UiaRect(ctypes.Structure):
    pass


class UiaPoint(ctypes.Structure):
    pass


class UiaChangeInfo(ctypes.Structure):
    pass


class UIAutomationParameter(ctypes.Structure):
    pass


class UIAutomationPropertyInfo(ctypes.Structure):
    pass


class UIAutomationEventInfo(ctypes.Structure):
    pass


class UIAutomationMethodInfo(ctypes.Structure):
    pass


class UIAutomationPatternInfo(ctypes.Structure):
    pass


# this ALWAYS GENERATED file contains the definitions for the interfaces
# File created by MIDL compiler version 8.01.0622
# @@MIDL_FILE_HEADING( )
# verify that the < rpcndr.h > version is high enough to compile this file
if not defined(__REQUIRED_RPCNDR_H_VERSION__):
    __REQUIRED_RPCNDR_H_VERSION__ = 475
# END IF


# verify that the < rpcsal.h > version is high enough to compile this file
if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    __REQUIRED_RPCSAL_H_VERSION__ = 100
# END IF


from pyWinAPI.shared.rpc_h import * # NOQA
from pyWinAPI.shared.rpcndr_h import * # NOQA

if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__

if not defined(__uiautomationcore_h__):
    __uiautomationcore_h__ = VOID

    if defined(_MSC_VER) and (_MSC_VER  >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IRawElementProviderSimple_FWD_DEFINED__):
        __IRawElementProviderSimple_FWD_DEFINED__ = VOID


        class IRawElementProviderSimple(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderSimple_FWD_DEFINED__

    if not defined(__IAccessibleEx_FWD_DEFINED__):
        __IAccessibleEx_FWD_DEFINED__ = VOID


        class IAccessibleEx(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAccessibleEx_FWD_DEFINED__

    if not defined(__IRawElementProviderSimple2_FWD_DEFINED__):
        __IRawElementProviderSimple2_FWD_DEFINED__ = VOID


        class IRawElementProviderSimple2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderSimple2_FWD_DEFINED__

    if not defined(__IRawElementProviderSimple3_FWD_DEFINED__):
        __IRawElementProviderSimple3_FWD_DEFINED__ = VOID


        class IRawElementProviderSimple3(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderSimple3_FWD_DEFINED__

    if not defined(__IRawElementProviderFragmentRoot_FWD_DEFINED__):
        __IRawElementProviderFragmentRoot_FWD_DEFINED__ = VOID


        class IRawElementProviderFragmentRoot(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderFragmentRoot_FWD_DEFINED__

    if not defined(__IRawElementProviderFragment_FWD_DEFINED__):
        __IRawElementProviderFragment_FWD_DEFINED__ = VOID


        class IRawElementProviderFragment(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderFragment_FWD_DEFINED__

    if not defined(__IRawElementProviderAdviseEvents_FWD_DEFINED__):
        __IRawElementProviderAdviseEvents_FWD_DEFINED__ = VOID


        class IRawElementProviderAdviseEvents(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderAdviseEvents_FWD_DEFINED__

    if not defined(__IRawElementProviderHwndOverride_FWD_DEFINED__):
        __IRawElementProviderHwndOverride_FWD_DEFINED__ = VOID


        class IRawElementProviderHwndOverride(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderHwndOverride_FWD_DEFINED__

    if not defined(__IProxyProviderWinEventSink_FWD_DEFINED__):
        __IProxyProviderWinEventSink_FWD_DEFINED__ = VOID


        class IProxyProviderWinEventSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProxyProviderWinEventSink_FWD_DEFINED__

    if not defined(__IProxyProviderWinEventHandler_FWD_DEFINED__):
        __IProxyProviderWinEventHandler_FWD_DEFINED__ = VOID


        class IProxyProviderWinEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IProxyProviderWinEventHandler_FWD_DEFINED__

    if not defined(__IRawElementProviderWindowlessSite_FWD_DEFINED__):
        __IRawElementProviderWindowlessSite_FWD_DEFINED__ = VOID


        class IRawElementProviderWindowlessSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderWindowlessSite_FWD_DEFINED__

    if not defined(__IAccessibleHostingElementProviders_FWD_DEFINED__):
        __IAccessibleHostingElementProviders_FWD_DEFINED__ = VOID


        class IAccessibleHostingElementProviders(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAccessibleHostingElementProviders_FWD_DEFINED__

    if not defined(__IRawElementProviderHostingAccessibles_FWD_DEFINED__):
        __IRawElementProviderHostingAccessibles_FWD_DEFINED__ = VOID


        class IRawElementProviderHostingAccessibles(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRawElementProviderHostingAccessibles_FWD_DEFINED__

    if not defined(__IDockProvider_FWD_DEFINED__):
        __IDockProvider_FWD_DEFINED__ = VOID


        class IDockProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDockProvider_FWD_DEFINED__

    if not defined(__IExpandCollapseProvider_FWD_DEFINED__):
        __IExpandCollapseProvider_FWD_DEFINED__ = VOID


        class IExpandCollapseProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IExpandCollapseProvider_FWD_DEFINED__

    if not defined(__IGridProvider_FWD_DEFINED__):
        __IGridProvider_FWD_DEFINED__ = VOID


        class IGridProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IGridProvider_FWD_DEFINED__

    if not defined(__IGridItemProvider_FWD_DEFINED__):
        __IGridItemProvider_FWD_DEFINED__ = VOID


        class IGridItemProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IGridItemProvider_FWD_DEFINED__

    if not defined(__IInvokeProvider_FWD_DEFINED__):
        __IInvokeProvider_FWD_DEFINED__ = VOID


        class IInvokeProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IInvokeProvider_FWD_DEFINED__

    if not defined(__IMultipleViewProvider_FWD_DEFINED__):
        __IMultipleViewProvider_FWD_DEFINED__ = VOID


        class IMultipleViewProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IMultipleViewProvider_FWD_DEFINED__

    if not defined(__IRangeValueProvider_FWD_DEFINED__):
        __IRangeValueProvider_FWD_DEFINED__ = VOID


        class IRangeValueProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IRangeValueProvider_FWD_DEFINED__

    if not defined(__IScrollItemProvider_FWD_DEFINED__):
        __IScrollItemProvider_FWD_DEFINED__ = VOID


        class IScrollItemProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IScrollItemProvider_FWD_DEFINED__

    if not defined(__ISelectionProvider_FWD_DEFINED__):
        __ISelectionProvider_FWD_DEFINED__ = VOID


        class ISelectionProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISelectionProvider_FWD_DEFINED__

    if not defined(__ISelectionProvider2_FWD_DEFINED__):
        __ISelectionProvider2_FWD_DEFINED__ = VOID


        class ISelectionProvider2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISelectionProvider2_FWD_DEFINED__

    if not defined(__IScrollProvider_FWD_DEFINED__):
        __IScrollProvider_FWD_DEFINED__ = VOID


        class IScrollProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IScrollProvider_FWD_DEFINED__

    if not defined(__ISelectionItemProvider_FWD_DEFINED__):
        __ISelectionItemProvider_FWD_DEFINED__ = VOID


        class ISelectionItemProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISelectionItemProvider_FWD_DEFINED__

    if not defined(__ISynchronizedInputProvider_FWD_DEFINED__):
        __ISynchronizedInputProvider_FWD_DEFINED__ = VOID


        class ISynchronizedInputProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISynchronizedInputProvider_FWD_DEFINED__

    if not defined(__ITableProvider_FWD_DEFINED__):
        __ITableProvider_FWD_DEFINED__ = VOID


        class ITableProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITableProvider_FWD_DEFINED__

    if not defined(__ITableItemProvider_FWD_DEFINED__):
        __ITableItemProvider_FWD_DEFINED__ = VOID


        class ITableItemProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITableItemProvider_FWD_DEFINED__

    if not defined(__IToggleProvider_FWD_DEFINED__):
        __IToggleProvider_FWD_DEFINED__ = VOID


        class IToggleProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IToggleProvider_FWD_DEFINED__

    if not defined(__ITransformProvider_FWD_DEFINED__):
        __ITransformProvider_FWD_DEFINED__ = VOID


        class ITransformProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITransformProvider_FWD_DEFINED__

    if not defined(__IValueProvider_FWD_DEFINED__):
        __IValueProvider_FWD_DEFINED__ = VOID


        class IValueProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IValueProvider_FWD_DEFINED__

    if not defined(__IWindowProvider_FWD_DEFINED__):
        __IWindowProvider_FWD_DEFINED__ = VOID


        class IWindowProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IWindowProvider_FWD_DEFINED__

    if not defined(__ILegacyIAccessibleProvider_FWD_DEFINED__):
        __ILegacyIAccessibleProvider_FWD_DEFINED__ = VOID


        class ILegacyIAccessibleProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ILegacyIAccessibleProvider_FWD_DEFINED__

    if not defined(__IItemContainerProvider_FWD_DEFINED__):
        __IItemContainerProvider_FWD_DEFINED__ = VOID


        class IItemContainerProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IItemContainerProvider_FWD_DEFINED__

    if not defined(__IVirtualizedItemProvider_FWD_DEFINED__):
        __IVirtualizedItemProvider_FWD_DEFINED__ = VOID


        class IVirtualizedItemProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IVirtualizedItemProvider_FWD_DEFINED__

    if not defined(__IObjectModelProvider_FWD_DEFINED__):
        __IObjectModelProvider_FWD_DEFINED__ = VOID


        class IObjectModelProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IObjectModelProvider_FWD_DEFINED__

    if not defined(__IAnnotationProvider_FWD_DEFINED__):
        __IAnnotationProvider_FWD_DEFINED__ = VOID


        class IAnnotationProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IAnnotationProvider_FWD_DEFINED__

    if not defined(__IStylesProvider_FWD_DEFINED__):
        __IStylesProvider_FWD_DEFINED__ = VOID


        class IStylesProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IStylesProvider_FWD_DEFINED__

    if not defined(__ISpreadsheetProvider_FWD_DEFINED__):
        __ISpreadsheetProvider_FWD_DEFINED__ = VOID


        class ISpreadsheetProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpreadsheetProvider_FWD_DEFINED__

    if not defined(__ISpreadsheetItemProvider_FWD_DEFINED__):
        __ISpreadsheetItemProvider_FWD_DEFINED__ = VOID


        class ISpreadsheetItemProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ISpreadsheetItemProvider_FWD_DEFINED__

    if not defined(__ITransformProvider2_FWD_DEFINED__):
        __ITransformProvider2_FWD_DEFINED__ = VOID


        class ITransformProvider2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITransformProvider2_FWD_DEFINED__

    if not defined(__IDragProvider_FWD_DEFINED__):
        __IDragProvider_FWD_DEFINED__ = VOID


        class IDragProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDragProvider_FWD_DEFINED__

    if not defined(__IDropTargetProvider_FWD_DEFINED__):
        __IDropTargetProvider_FWD_DEFINED__ = VOID


        class IDropTargetProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IDropTargetProvider_FWD_DEFINED__

    if not defined(__ITextRangeProvider_FWD_DEFINED__):
        __ITextRangeProvider_FWD_DEFINED__ = VOID


        class ITextRangeProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITextRangeProvider_FWD_DEFINED__

    if not defined(__ITextProvider_FWD_DEFINED__):
        __ITextProvider_FWD_DEFINED__ = VOID


        class ITextProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITextProvider_FWD_DEFINED__

    if not defined(__ITextProvider2_FWD_DEFINED__):
        __ITextProvider2_FWD_DEFINED__ = VOID


        class ITextProvider2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITextProvider2_FWD_DEFINED__

    if not defined(__ITextEditProvider_FWD_DEFINED__):
        __ITextEditProvider_FWD_DEFINED__ = VOID


        class ITextEditProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITextEditProvider_FWD_DEFINED__

    if not defined(__ITextRangeProvider2_FWD_DEFINED__):
        __ITextRangeProvider2_FWD_DEFINED__ = VOID


        class ITextRangeProvider2(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITextRangeProvider2_FWD_DEFINED__

    if not defined(__ITextChildProvider_FWD_DEFINED__):
        __ITextChildProvider_FWD_DEFINED__ = VOID


        class ITextChildProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ITextChildProvider_FWD_DEFINED__

    if not defined(__ICustomNavigationProvider_FWD_DEFINED__):
        __ICustomNavigationProvider_FWD_DEFINED__ = VOID


        class ICustomNavigationProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __ICustomNavigationProvider_FWD_DEFINED__

    if not defined(__IUIAutomationPatternInstance_FWD_DEFINED__):
        __IUIAutomationPatternInstance_FWD_DEFINED__ = VOID


        class IUIAutomationPatternInstance(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationPatternInstance_FWD_DEFINED__

    if not defined(__IUIAutomationPatternHandler_FWD_DEFINED__):
        __IUIAutomationPatternHandler_FWD_DEFINED__ = VOID


        class IUIAutomationPatternHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationPatternHandler_FWD_DEFINED__

    if not defined(__IUIAutomationRegistrar_FWD_DEFINED__):
        __IUIAutomationRegistrar_FWD_DEFINED__ = VOID


        class IUIAutomationRegistrar(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationRegistrar_FWD_DEFINED__

    if not defined(__CUIAutomationRegistrar_FWD_DEFINED__):
        __CUIAutomationRegistrar_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:

            class CUIAutomationRegistrar(comtypes.CoClass):
                """
                Class for registering UIAutomation patterns properties and events.
                """
                _case_insensitive_ = True
                _idlflags_ = []
                _reg_clsid_ = None
                _reg_typelib_ = ()
                _com_interfaces_ = []

        # END IF  __cplusplus
    # END IF  __CUIAutomationRegistrar_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.oaidl_h import * # NOQA
    from pyWinAPI.um.oleacc_h import * # NOQA
    if defined(__cplusplus):
        pass
    # END IF


    # interface __MIDL_itf_uiautomationcore_0000_0000
    # [local]
    # -------------------------------------------------------------
    # UIAutomationCore.H
    # UIAutomation interface definitions and related types and enums
    # (Generated from UIAutomationCore.idl)
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # -------------------------------------------------------------
    class NavigateDirection(ENUM):
        NavigateDirection_Parent = 0
        NavigateDirection_NextSibling = 1
        NavigateDirection_PreviousSibling = 2
        NavigateDirection_FirstChild = 3
        NavigateDirection_LastChild = 4

    NavigateDirection_Parent = NavigateDirection.NavigateDirection_Parent
    NavigateDirection_NextSibling = NavigateDirection.NavigateDirection_NextSibling
    NavigateDirection_PreviousSibling = NavigateDirection.NavigateDirection_PreviousSibling
    NavigateDirection_FirstChild = NavigateDirection.NavigateDirection_FirstChild
    NavigateDirection_LastChild = NavigateDirection.NavigateDirection_LastChild


    class ProviderOptions(ENUM):
        ProviderOptions_ClientSideProvider = 0x1
        ProviderOptions_ServerSideProvider = 0x2
        ProviderOptions_NonClientAreaProvider = 0x4
        ProviderOptions_OverrideProvider = 0x8
        ProviderOptions_ProviderOwnsSetFocus = 0x10
        ProviderOptions_UseComThreading = 0x20
        ProviderOptions_RefuseNonClientSupport = 0x40
        ProviderOptions_HasNativeIAccessible = 0x80
        ProviderOptions_UseClientCoordinates = 0x100

    ProviderOptions_ClientSideProvider = ProviderOptions.ProviderOptions_ClientSideProvider
    ProviderOptions_ServerSideProvider = ProviderOptions.ProviderOptions_ServerSideProvider
    ProviderOptions_NonClientAreaProvider = ProviderOptions.ProviderOptions_NonClientAreaProvider
    ProviderOptions_OverrideProvider = ProviderOptions.ProviderOptions_OverrideProvider
    ProviderOptions_ProviderOwnsSetFocus = ProviderOptions.ProviderOptions_ProviderOwnsSetFocus
    ProviderOptions_UseComThreading = ProviderOptions.ProviderOptions_UseComThreading
    ProviderOptions_RefuseNonClientSupport = ProviderOptions.ProviderOptions_RefuseNonClientSupport
    ProviderOptions_HasNativeIAccessible = ProviderOptions.ProviderOptions_HasNativeIAccessible
    ProviderOptions_UseClientCoordinates = ProviderOptions.ProviderOptions_UseClientCoordinates


    class StructureChangeType(ENUM):
        StructureChangeType_ChildAdded = 0
        StructureChangeType_ChildRemoved = StructureChangeType_ChildAdded + 1
        StructureChangeType_ChildrenInvalidated = (
            StructureChangeType_ChildRemoved + 1
        )
        StructureChangeType_ChildrenBulkAdded = (
            StructureChangeType_ChildrenInvalidated + 1
        )
        StructureChangeType_ChildrenBulkRemoved = (
            StructureChangeType_ChildrenBulkAdded + 1
        )
        StructureChangeType_ChildrenReordered = (
            StructureChangeType_ChildrenBulkRemoved + 1
        )

    StructureChangeType_ChildAdded = StructureChangeType.StructureChangeType_ChildAdded
    StructureChangeType_ChildRemoved = StructureChangeType.StructureChangeType_ChildRemoved
    StructureChangeType_ChildrenInvalidated = StructureChangeType.StructureChangeType_ChildrenInvalidated
    StructureChangeType_ChildrenBulkAdded = StructureChangeType.StructureChangeType_ChildrenBulkAdded
    StructureChangeType_ChildrenBulkRemoved = StructureChangeType.StructureChangeType_ChildrenBulkRemoved
    StructureChangeType_ChildrenReordered = StructureChangeType.StructureChangeType_ChildrenReordered


    class TextEditChangeType(ENUM):
        TextEditChangeType_None = 0
        TextEditChangeType_AutoCorrect = 1
        TextEditChangeType_Composition = 2
        TextEditChangeType_CompositionFinalized = 3
        TextEditChangeType_AutoComplete = 4

    TextEditChangeType_None = TextEditChangeType.TextEditChangeType_None
    TextEditChangeType_AutoCorrect = TextEditChangeType.TextEditChangeType_AutoCorrect
    TextEditChangeType_Composition = TextEditChangeType.TextEditChangeType_Composition
    TextEditChangeType_CompositionFinalized = TextEditChangeType.TextEditChangeType_CompositionFinalized
    TextEditChangeType_AutoComplete = TextEditChangeType.TextEditChangeType_AutoComplete


    class OrientationType(ENUM):
        OrientationType_None = 0
        OrientationType_Horizontal = 1
        OrientationType_Vertical = 2

    OrientationType_None = OrientationType.OrientationType_None
    OrientationType_Horizontal = OrientationType.OrientationType_Horizontal
    OrientationType_Vertical = OrientationType.OrientationType_Vertical


    class DockPosition(ENUM):
        DockPosition_Top = 0
        DockPosition_Left = 1
        DockPosition_Bottom = 2
        DockPosition_Right = 3
        DockPosition_Fill = 4
        DockPosition_None = 5

    DockPosition_Top = DockPosition.DockPosition_Top
    DockPosition_Left = DockPosition.DockPosition_Left
    DockPosition_Bottom = DockPosition.DockPosition_Bottom
    DockPosition_Right = DockPosition.DockPosition_Right
    DockPosition_Fill = DockPosition.DockPosition_Fill
    DockPosition_None = DockPosition.DockPosition_None


    class ExpandCollapseState(ENUM):
        ExpandCollapseState_Collapsed = 0
        ExpandCollapseState_Expanded = 1
        ExpandCollapseState_PartiallyExpanded = 2
        ExpandCollapseState_LeafNode = 3

    ExpandCollapseState_Collapsed = ExpandCollapseState.ExpandCollapseState_Collapsed
    ExpandCollapseState_Expanded = ExpandCollapseState.ExpandCollapseState_Expanded
    ExpandCollapseState_PartiallyExpanded = ExpandCollapseState.ExpandCollapseState_PartiallyExpanded
    ExpandCollapseState_LeafNode = ExpandCollapseState.ExpandCollapseState_LeafNode


    class ScrollAmount(ENUM):
        ScrollAmount_LargeDecrement = 0
        ScrollAmount_SmallDecrement = 1
        ScrollAmount_NoAmount = 2
        ScrollAmount_LargeIncrement = 3
        ScrollAmount_SmallIncrement = 4

    ScrollAmount_LargeDecrement = ScrollAmount.ScrollAmount_LargeDecrement
    ScrollAmount_SmallDecrement = ScrollAmount.ScrollAmount_SmallDecrement
    ScrollAmount_NoAmount = ScrollAmount.ScrollAmount_NoAmount
    ScrollAmount_LargeIncrement = ScrollAmount.ScrollAmount_LargeIncrement
    ScrollAmount_SmallIncrement = ScrollAmount.ScrollAmount_SmallIncrement


    class RowOrColumnMajor(ENUM):
        RowOrColumnMajor_RowMajor = 0
        RowOrColumnMajor_ColumnMajor = 1
        RowOrColumnMajor_Indeterminate = 2

    RowOrColumnMajor_RowMajor = RowOrColumnMajor.RowOrColumnMajor_RowMajor
    RowOrColumnMajor_ColumnMajor = RowOrColumnMajor.RowOrColumnMajor_ColumnMajor
    RowOrColumnMajor_Indeterminate = RowOrColumnMajor.RowOrColumnMajor_Indeterminate


    class ToggleState(ENUM):
        ToggleState_Off = 0
        ToggleState_On = 1
        ToggleState_Indeterminate = 2

    ToggleState_Off = ToggleState.ToggleState_Off
    ToggleState_On = ToggleState.ToggleState_On
    ToggleState_Indeterminate = ToggleState.ToggleState_Indeterminate


    class WindowVisualState(ENUM):
        WindowVisualState_Normal = 0
        WindowVisualState_Maximized = 1
        WindowVisualState_Minimized = 2

    WindowVisualState_Normal = WindowVisualState.WindowVisualState_Normal
    WindowVisualState_Maximized = WindowVisualState.WindowVisualState_Maximized
    WindowVisualState_Minimized = WindowVisualState.WindowVisualState_Minimized


    class SynchronizedInputType(ENUM):
        SynchronizedInputType_KeyUp = 0x1
        SynchronizedInputType_KeyDown = 0x2
        SynchronizedInputType_LeftMouseUp = 0x4
        SynchronizedInputType_LeftMouseDown = 0x8
        SynchronizedInputType_RightMouseUp = 0x10
        SynchronizedInputType_RightMouseDown = 0x20

    SynchronizedInputType_KeyUp = SynchronizedInputType.SynchronizedInputType_KeyUp
    SynchronizedInputType_KeyDown = SynchronizedInputType.SynchronizedInputType_KeyDown
    SynchronizedInputType_LeftMouseUp = SynchronizedInputType.SynchronizedInputType_LeftMouseUp
    SynchronizedInputType_LeftMouseDown = SynchronizedInputType.SynchronizedInputType_LeftMouseDown
    SynchronizedInputType_RightMouseUp = SynchronizedInputType.SynchronizedInputType_RightMouseUp
    SynchronizedInputType_RightMouseDown = SynchronizedInputType.SynchronizedInputType_RightMouseDown


    class WindowInteractionState(ENUM):
        WindowInteractionState_Running = 0
        WindowInteractionState_Closing = 1
        WindowInteractionState_ReadyForUserInteraction = 2
        WindowInteractionState_BlockedByModalWindow = 3
        WindowInteractionState_NotResponding = 4

    WindowInteractionState_Running = WindowInteractionState.WindowInteractionState_Running
    WindowInteractionState_Closing = WindowInteractionState.WindowInteractionState_Closing
    WindowInteractionState_ReadyForUserInteraction = WindowInteractionState.WindowInteractionState_ReadyForUserInteraction
    WindowInteractionState_BlockedByModalWindow = WindowInteractionState.WindowInteractionState_BlockedByModalWindow
    WindowInteractionState_NotResponding = WindowInteractionState.WindowInteractionState_NotResponding


    class SayAsInterpretAs(ENUM):
        SayAsInterpretAs_None = 0
        SayAsInterpretAs_Spell = 1
        SayAsInterpretAs_Cardinal = 2
        SayAsInterpretAs_Ordinal = 3
        SayAsInterpretAs_Number = 4
        SayAsInterpretAs_Date = 5
        SayAsInterpretAs_Time = 6
        SayAsInterpretAs_Telephone = 7
        SayAsInterpretAs_Currency = 8
        SayAsInterpretAs_Net = 9
        SayAsInterpretAs_Url = 10
        SayAsInterpretAs_Address = 11
        SayAsInterpretAs_Alphanumeric = 12
        SayAsInterpretAs_Name = 13
        SayAsInterpretAs_Media = 14
        SayAsInterpretAs_Date_MonthDayYear = 15
        SayAsInterpretAs_Date_DayMonthYear = 16
        SayAsInterpretAs_Date_YearMonthDay = 17
        SayAsInterpretAs_Date_YearMonth = 18
        SayAsInterpretAs_Date_MonthYear = 19
        SayAsInterpretAs_Date_DayMonth = 20
        SayAsInterpretAs_Date_MonthDay = 21
        SayAsInterpretAs_Date_Year = 22
        SayAsInterpretAs_Time_HoursMinutesSeconds12 = 23
        SayAsInterpretAs_Time_HoursMinutes12 = 24
        SayAsInterpretAs_Time_HoursMinutesSeconds24 = 25
        SayAsInterpretAs_Time_HoursMinutes24 = 26

    SayAsInterpretAs_None = SayAsInterpretAs.SayAsInterpretAs_None
    SayAsInterpretAs_Spell = SayAsInterpretAs.SayAsInterpretAs_Spell
    SayAsInterpretAs_Cardinal = SayAsInterpretAs.SayAsInterpretAs_Cardinal
    SayAsInterpretAs_Ordinal = SayAsInterpretAs.SayAsInterpretAs_Ordinal
    SayAsInterpretAs_Number = SayAsInterpretAs.SayAsInterpretAs_Number
    SayAsInterpretAs_Date = SayAsInterpretAs.SayAsInterpretAs_Date
    SayAsInterpretAs_Time = SayAsInterpretAs.SayAsInterpretAs_Time
    SayAsInterpretAs_Telephone = SayAsInterpretAs.SayAsInterpretAs_Telephone
    SayAsInterpretAs_Currency = SayAsInterpretAs.SayAsInterpretAs_Currency
    SayAsInterpretAs_Net = SayAsInterpretAs.SayAsInterpretAs_Net
    SayAsInterpretAs_Url = SayAsInterpretAs.SayAsInterpretAs_Url
    SayAsInterpretAs_Address = SayAsInterpretAs.SayAsInterpretAs_Address
    SayAsInterpretAs_Alphanumeric = SayAsInterpretAs.SayAsInterpretAs_Alphanumeric
    SayAsInterpretAs_Name = SayAsInterpretAs.SayAsInterpretAs_Name
    SayAsInterpretAs_Media = SayAsInterpretAs.SayAsInterpretAs_Media
    SayAsInterpretAs_Date_MonthDayYear = SayAsInterpretAs.SayAsInterpretAs_Date_MonthDayYear
    SayAsInterpretAs_Date_DayMonthYear = SayAsInterpretAs.SayAsInterpretAs_Date_DayMonthYear
    SayAsInterpretAs_Date_YearMonthDay = SayAsInterpretAs.SayAsInterpretAs_Date_YearMonthDay
    SayAsInterpretAs_Date_YearMonth = SayAsInterpretAs.SayAsInterpretAs_Date_YearMonth
    SayAsInterpretAs_Date_MonthYear = SayAsInterpretAs.SayAsInterpretAs_Date_MonthYear
    SayAsInterpretAs_Date_DayMonth = SayAsInterpretAs.SayAsInterpretAs_Date_DayMonth
    SayAsInterpretAs_Date_MonthDay = SayAsInterpretAs.SayAsInterpretAs_Date_MonthDay
    SayAsInterpretAs_Date_Year = SayAsInterpretAs.SayAsInterpretAs_Date_Year
    SayAsInterpretAs_Time_HoursMinutesSeconds12 = SayAsInterpretAs.SayAsInterpretAs_Time_HoursMinutesSeconds12
    SayAsInterpretAs_Time_HoursMinutes12 = SayAsInterpretAs.SayAsInterpretAs_Time_HoursMinutes12
    SayAsInterpretAs_Time_HoursMinutesSeconds24 = SayAsInterpretAs.SayAsInterpretAs_Time_HoursMinutesSeconds24
    SayAsInterpretAs_Time_HoursMinutes24 = SayAsInterpretAs.SayAsInterpretAs_Time_HoursMinutes24


    class TextUnit(ENUM):
        TextUnit_Character = 0
        TextUnit_Format = 1
        TextUnit_Word = 2
        TextUnit_Line = 3
        TextUnit_Paragraph = 4
        TextUnit_Page = 5
        TextUnit_Document = 6

    TextUnit_Character = TextUnit.TextUnit_Character
    TextUnit_Format = TextUnit.TextUnit_Format
    TextUnit_Word = TextUnit.TextUnit_Word
    TextUnit_Line = TextUnit.TextUnit_Line
    TextUnit_Paragraph = TextUnit.TextUnit_Paragraph
    TextUnit_Page = TextUnit.TextUnit_Page
    TextUnit_Document = TextUnit.TextUnit_Document


    class TextPatternRangeEndpoint(ENUM):
        TextPatternRangeEndpoint_Start = 0
        TextPatternRangeEndpoint_End = 1

    TextPatternRangeEndpoint_Start = TextPatternRangeEndpoint.TextPatternRangeEndpoint_Start
    TextPatternRangeEndpoint_End = TextPatternRangeEndpoint.TextPatternRangeEndpoint_End


    class SupportedTextSelection(ENUM):
        SupportedTextSelection_None = 0
        SupportedTextSelection_Single = 1
        SupportedTextSelection_Multiple = 2

    SupportedTextSelection_None = SupportedTextSelection.SupportedTextSelection_None
    SupportedTextSelection_Single = SupportedTextSelection.SupportedTextSelection_Single
    SupportedTextSelection_Multiple = SupportedTextSelection.SupportedTextSelection_Multiple


    class LiveSetting(ENUM):
        Off = 0
        Polite = 1
        Assertive = 2

    Off = LiveSetting.Off
    Polite = LiveSetting.Polite
    Assertive = LiveSetting.Assertive


    class ActiveEnd(ENUM):
        ActiveEnd_None = 0
        ActiveEnd_Start = 1
        ActiveEnd_End = 2

    ActiveEnd_None = ActiveEnd.ActiveEnd_None
    ActiveEnd_Start = ActiveEnd.ActiveEnd_Start
    ActiveEnd_End = ActiveEnd.ActiveEnd_End


    class CaretPosition(ENUM):
        CaretPosition_Unknown = 0
        CaretPosition_EndOfLine = 1
        CaretPosition_BeginningOfLine = 2

    CaretPosition_Unknown = CaretPosition.CaretPosition_Unknown
    CaretPosition_EndOfLine = CaretPosition.CaretPosition_EndOfLine
    CaretPosition_BeginningOfLine = CaretPosition.CaretPosition_BeginningOfLine


    class CaretBidiMode(ENUM):
        CaretBidiMode_LTR = 0
        CaretBidiMode_RTL = 1

    CaretBidiMode_LTR = CaretBidiMode.CaretBidiMode_LTR
    CaretBidiMode_RTL = CaretBidiMode.CaretBidiMode_RTL


    class ZoomUnit(ENUM):
        ZoomUnit_NoAmount = 0
        ZoomUnit_LargeDecrement = 1
        ZoomUnit_SmallDecrement = 2
        ZoomUnit_LargeIncrement = 3
        ZoomUnit_SmallIncrement = 4

    ZoomUnit_NoAmount = ZoomUnit.ZoomUnit_NoAmount
    ZoomUnit_LargeDecrement = ZoomUnit.ZoomUnit_LargeDecrement
    ZoomUnit_SmallDecrement = ZoomUnit.ZoomUnit_SmallDecrement
    ZoomUnit_LargeIncrement = ZoomUnit.ZoomUnit_LargeIncrement
    ZoomUnit_SmallIncrement = ZoomUnit.ZoomUnit_SmallIncrement


    class AnimationStyle(ENUM):
        AnimationStyle_None = 0
        AnimationStyle_LasVegasLights = 1
        AnimationStyle_BlinkingBackground = 2
        AnimationStyle_SparkleText = 3
        AnimationStyle_MarchingBlackAnts = 4
        AnimationStyle_MarchingRedAnts = 5
        AnimationStyle_Shimmer = 6
        AnimationStyle_Other = - 1

    AnimationStyle_None = AnimationStyle.AnimationStyle_None
    AnimationStyle_LasVegasLights = AnimationStyle.AnimationStyle_LasVegasLights
    AnimationStyle_BlinkingBackground = AnimationStyle.AnimationStyle_BlinkingBackground
    AnimationStyle_SparkleText = AnimationStyle.AnimationStyle_SparkleText
    AnimationStyle_MarchingBlackAnts = AnimationStyle.AnimationStyle_MarchingBlackAnts
    AnimationStyle_MarchingRedAnts = AnimationStyle.AnimationStyle_MarchingRedAnts
    AnimationStyle_Shimmer = AnimationStyle.AnimationStyle_Shimmer
    AnimationStyle_Other = AnimationStyle.AnimationStyle_Other


    class BulletStyle(ENUM):
        BulletStyle_None = 0
        BulletStyle_HollowRoundBullet = 1
        BulletStyle_FilledRoundBullet = 2
        BulletStyle_HollowSquareBullet = 3
        BulletStyle_FilledSquareBullet = 4
        BulletStyle_DashBullet = 5
        BulletStyle_Other = - 1

    BulletStyle_None = BulletStyle.BulletStyle_None
    BulletStyle_HollowRoundBullet = BulletStyle.BulletStyle_HollowRoundBullet
    BulletStyle_FilledRoundBullet = BulletStyle.BulletStyle_FilledRoundBullet
    BulletStyle_HollowSquareBullet = BulletStyle.BulletStyle_HollowSquareBullet
    BulletStyle_FilledSquareBullet = BulletStyle.BulletStyle_FilledSquareBullet
    BulletStyle_DashBullet = BulletStyle.BulletStyle_DashBullet
    BulletStyle_Other = BulletStyle.BulletStyle_Other


    class CapStyle(ENUM):
        CapStyle_None = 0
        CapStyle_SmallCap = 1
        CapStyle_AllCap = 2
        CapStyle_AllPetiteCaps = 3
        CapStyle_PetiteCaps = 4
        CapStyle_Unicase = 5
        CapStyle_Titling = 6
        CapStyle_Other = - 1

    CapStyle_None = CapStyle.CapStyle_None
    CapStyle_SmallCap = CapStyle.CapStyle_SmallCap
    CapStyle_AllCap = CapStyle.CapStyle_AllCap
    CapStyle_AllPetiteCaps = CapStyle.CapStyle_AllPetiteCaps
    CapStyle_PetiteCaps = CapStyle.CapStyle_PetiteCaps
    CapStyle_Unicase = CapStyle.CapStyle_Unicase
    CapStyle_Titling = CapStyle.CapStyle_Titling
    CapStyle_Other = CapStyle.CapStyle_Other


    class FillType(ENUM):
        FillType_None = 0
        FillType_Color = 1
        FillType_Gradient = 2
        FillType_Picture = 3
        FillType_Pattern = 4

    FillType_None = FillType.FillType_None
    FillType_Color = FillType.FillType_Color
    FillType_Gradient = FillType.FillType_Gradient
    FillType_Picture = FillType.FillType_Picture
    FillType_Pattern = FillType.FillType_Pattern


    class FlowDirections(ENUM):
        FlowDirections_Default = 0
        FlowDirections_RightToLeft = 0x1
        FlowDirections_BottomToTop = 0x2
        FlowDirections_Vertical = 0x4

    FlowDirections_Default = FlowDirections.FlowDirections_Default
    FlowDirections_RightToLeft = FlowDirections.FlowDirections_RightToLeft
    FlowDirections_BottomToTop = FlowDirections.FlowDirections_BottomToTop
    FlowDirections_Vertical = FlowDirections.FlowDirections_Vertical


    class HorizontalTextAlignment(ENUM):
        HorizontalTextAlignment_Left = 0
        HorizontalTextAlignment_Centered = 1
        HorizontalTextAlignment_Right = 2
        HorizontalTextAlignment_Justified = 3

    HorizontalTextAlignment_Left = HorizontalTextAlignment.HorizontalTextAlignment_Left
    HorizontalTextAlignment_Centered = HorizontalTextAlignment.HorizontalTextAlignment_Centered
    HorizontalTextAlignment_Right = HorizontalTextAlignment.HorizontalTextAlignment_Right
    HorizontalTextAlignment_Justified = HorizontalTextAlignment.HorizontalTextAlignment_Justified


    class OutlineStyles(ENUM):
        OutlineStyles_None = 0
        OutlineStyles_Outline = 1
        OutlineStyles_Shadow = 2
        OutlineStyles_Engraved = 4
        OutlineStyles_Embossed = 8

    OutlineStyles_None = OutlineStyles.OutlineStyles_None
    OutlineStyles_Outline = OutlineStyles.OutlineStyles_Outline
    OutlineStyles_Shadow = OutlineStyles.OutlineStyles_Shadow
    OutlineStyles_Engraved = OutlineStyles.OutlineStyles_Engraved
    OutlineStyles_Embossed = OutlineStyles.OutlineStyles_Embossed


    class TextDecorationLineStyle(ENUM):
        TextDecorationLineStyle_None = 0
        TextDecorationLineStyle_Single = 1
        TextDecorationLineStyle_WordsOnly = 2
        TextDecorationLineStyle_Double = 3
        TextDecorationLineStyle_Dot = 4
        TextDecorationLineStyle_Dash = 5
        TextDecorationLineStyle_DashDot = 6
        TextDecorationLineStyle_DashDotDot = 7
        TextDecorationLineStyle_Wavy = 8
        TextDecorationLineStyle_ThickSingle = 9
        TextDecorationLineStyle_DoubleWavy = 11
        TextDecorationLineStyle_ThickWavy = 12
        TextDecorationLineStyle_LongDash = 13
        TextDecorationLineStyle_ThickDash = 14
        TextDecorationLineStyle_ThickDashDot = 15
        TextDecorationLineStyle_ThickDashDotDot = 16
        TextDecorationLineStyle_ThickDot = 17
        TextDecorationLineStyle_ThickLongDash = 18
        TextDecorationLineStyle_Other = - 1

    TextDecorationLineStyle_None = TextDecorationLineStyle.TextDecorationLineStyle_None
    TextDecorationLineStyle_Single = TextDecorationLineStyle.TextDecorationLineStyle_Single
    TextDecorationLineStyle_WordsOnly = TextDecorationLineStyle.TextDecorationLineStyle_WordsOnly
    TextDecorationLineStyle_Double = TextDecorationLineStyle.TextDecorationLineStyle_Double
    TextDecorationLineStyle_Dot = TextDecorationLineStyle.TextDecorationLineStyle_Dot
    TextDecorationLineStyle_Dash = TextDecorationLineStyle.TextDecorationLineStyle_Dash
    TextDecorationLineStyle_DashDot = TextDecorationLineStyle.TextDecorationLineStyle_DashDot
    TextDecorationLineStyle_DashDotDot = TextDecorationLineStyle.TextDecorationLineStyle_DashDotDot
    TextDecorationLineStyle_Wavy = TextDecorationLineStyle.TextDecorationLineStyle_Wavy
    TextDecorationLineStyle_ThickSingle = TextDecorationLineStyle.TextDecorationLineStyle_ThickSingle
    TextDecorationLineStyle_DoubleWavy = TextDecorationLineStyle.TextDecorationLineStyle_DoubleWavy
    TextDecorationLineStyle_ThickWavy = TextDecorationLineStyle.TextDecorationLineStyle_ThickWavy
    TextDecorationLineStyle_LongDash = TextDecorationLineStyle.TextDecorationLineStyle_LongDash
    TextDecorationLineStyle_ThickDash = TextDecorationLineStyle.TextDecorationLineStyle_ThickDash
    TextDecorationLineStyle_ThickDashDot = TextDecorationLineStyle.TextDecorationLineStyle_ThickDashDot
    TextDecorationLineStyle_ThickDashDotDot = TextDecorationLineStyle.TextDecorationLineStyle_ThickDashDotDot
    TextDecorationLineStyle_ThickDot = TextDecorationLineStyle.TextDecorationLineStyle_ThickDot
    TextDecorationLineStyle_ThickLongDash = TextDecorationLineStyle.TextDecorationLineStyle_ThickLongDash
    TextDecorationLineStyle_Other = TextDecorationLineStyle.TextDecorationLineStyle_Other


    class VisualEffects(ENUM):
        VisualEffects_None = 0
        VisualEffects_Shadow = 1 << 0
        VisualEffects_Reflection = 1 << 1
        VisualEffects_Glow = 1 << 2
        VisualEffects_SoftEdges = 1 << 3
        VisualEffects_Bevel = 1 << 4

    VisualEffects_None = VisualEffects.VisualEffects_None
    VisualEffects_Shadow = VisualEffects.VisualEffects_Shadow
    VisualEffects_Reflection = VisualEffects.VisualEffects_Reflection
    VisualEffects_Glow = VisualEffects.VisualEffects_Glow
    VisualEffects_SoftEdges = VisualEffects.VisualEffects_SoftEdges
    VisualEffects_Bevel = VisualEffects.VisualEffects_Bevel


    class NotificationProcessing(ENUM):
        NotificationProcessing_ImportantAll = 0
        NotificationProcessing_ImportantMostRecent = 1
        NotificationProcessing_All = 2
        NotificationProcessing_MostRecent = 3
        NotificationProcessing_CurrentThenMostRecent = 4

    NotificationProcessing_ImportantAll = (
        NotificationProcessing.NotificationProcessing_ImportantAll
    )
    NotificationProcessing_ImportantMostRecent = (
        NotificationProcessing.NotificationProcessing_ImportantMostRecent
    )
    NotificationProcessing_All = (
        NotificationProcessing.NotificationProcessing_All
    )
    NotificationProcessing_MostRecent = (
        NotificationProcessing.NotificationProcessing_MostRecent
    )
    NotificationProcessing_CurrentThenMostRecent = (
        NotificationProcessing.NotificationProcessing_CurrentThenMostRecent
    )


    class NotificationKind(ENUM):
        NotificationKind_ItemAdded = 0
        NotificationKind_ItemRemoved = 1
        NotificationKind_ActionCompleted = 2
        NotificationKind_ActionAborted = 3
        NotificationKind_Other = 4


    NotificationKind_ItemAdded = NotificationKind.NotificationKind_ItemAdded
    NotificationKind_ItemRemoved = (
        NotificationKind.NotificationKind_ItemRemoved
    )
    NotificationKind_ActionCompleted = (
        NotificationKind.NotificationKind_ActionCompleted
    )
    NotificationKind_ActionAborted = (
        NotificationKind.NotificationKind_ActionAborted
    )
    NotificationKind_Other = NotificationKind.NotificationKind_Other

    PROPERTYID = INT
    PATTERNID = INT
    EVENTID = INT
    TEXTATTRIBUTEID = INT
    CONTROLTYPEID = INT
    LANDMARKTYPEID = INT
    METADATAID = INT
    HEADINGLEVELID = INT

    UiaRect._fields_ = [
        ('left', DOUBLE),
        ('top', DOUBLE),
        ('width', DOUBLE),
        ('height', DOUBLE),
    ]

    UiaPoint._fields_ = [
        ('x', DOUBLE),
        ('y', DOUBLE),
    ]

    UiaChangeInfo._fields_ = [
        ('uiaId', INT),
        ('payload', VARIANT),
        ('extraInfo', VARIANT),
    ]
    if not defined(__UIA_LIBRARY_DEFINED__):
        __UIA_LIBRARY_DEFINED__ = VOID

        # library UIA
        # [hidden][version][lcid][uuid]
        class UIAutomationType(ENUM):
            UIAutomationType_Int = 0x1
            UIAutomationType_Bool = 0x2
            UIAutomationType_String = 0x3
            UIAutomationType_Double = 0x4
            UIAutomationType_Point = 0x5
            UIAutomationType_Rect = 0x6
            UIAutomationType_Element = 0x7
            UIAutomationType_Array = 0x10000
            UIAutomationType_Out = 0x20000
            UIAutomationType_IntArray = (
                UIAutomationType_Int |
                UIAutomationType_Array
            )
            UIAutomationType_BoolArray = (
                UIAutomationType_Bool |
                UIAutomationType_Array
            )
            UIAutomationType_StringArray = (
                UIAutomationType_String |
                UIAutomationType_Array
            )
            UIAutomationType_DoubleArray = (
                UIAutomationType_Double |
                UIAutomationType_Array
            )
            UIAutomationType_PointArray = (
                UIAutomationType_Point |
                UIAutomationType_Array
            )
            UIAutomationType_RectArray = (
                UIAutomationType_Rect |
                UIAutomationType_Array
            )
            UIAutomationType_ElementArray = (
                UIAutomationType_Element |
                UIAutomationType_Array
            )
            UIAutomationType_OutInt = (
                UIAutomationType_Int |
                UIAutomationType_Out
            )
            UIAutomationType_OutBool = (
                UIAutomationType_Bool |
                UIAutomationType_Out
            )
            UIAutomationType_OutString = (
                UIAutomationType_String |
                UIAutomationType_Out
            )
            UIAutomationType_OutDouble = (
                UIAutomationType_Double |
                UIAutomationType_Out
            )
            UIAutomationType_OutPoint = (
                UIAutomationType_Point |
                UIAutomationType_Out
            )
            UIAutomationType_OutRect = (
                UIAutomationType_Rect |
                UIAutomationType_Out
            )
            UIAutomationType_OutElement = (
                UIAutomationType_Element |
                UIAutomationType_Out
            )
            UIAutomationType_OutIntArray = (
                (UIAutomationType_Int | UIAutomationType_Array) |
                UIAutomationType_Out
            )
            UIAutomationType_OutBoolArray = (
                (UIAutomationType_Bool | UIAutomationType_Array) |
                UIAutomationType_Out
            )
            UIAutomationType_OutStringArray = (
                (UIAutomationType_String | UIAutomationType_Array) |
                UIAutomationType_Out
            )
            UIAutomationType_OutDoubleArray = (
                (UIAutomationType_Double | UIAutomationType_Array) |
                UIAutomationType_Out
            )
            UIAutomationType_OutPointArray = (
                (UIAutomationType_Point | UIAutomationType_Array) |
                UIAutomationType_Out
            )
            UIAutomationType_OutRectArray = (
                (UIAutomationType_Rect | UIAutomationType_Array) |
                UIAutomationType_Out
            )
            UIAutomationType_OutElementArray = (
                (UIAutomationType_Element | UIAutomationType_Array) |
                UIAutomationType_Out
            )
        UIAutomationType_Int = UIAutomationType.UIAutomationType_Int
        UIAutomationType_Bool = UIAutomationType.UIAutomationType_Bool
        UIAutomationType_String = UIAutomationType.UIAutomationType_String
        UIAutomationType_Double = UIAutomationType.UIAutomationType_Double
        UIAutomationType_Point = UIAutomationType.UIAutomationType_Point
        UIAutomationType_Rect = UIAutomationType.UIAutomationType_Rect
        UIAutomationType_Element = UIAutomationType.UIAutomationType_Element
        UIAutomationType_Array = UIAutomationType.UIAutomationType_Array
        UIAutomationType_Out = UIAutomationType.UIAutomationType_Out
        UIAutomationType_IntArray = UIAutomationType.UIAutomationType_IntArray
        UIAutomationType_BoolArray = (
            UIAutomationType.UIAutomationType_BoolArray
        )
        UIAutomationType_StringArray = (
            UIAutomationType.UIAutomationType_StringArray
        )
        UIAutomationType_DoubleArray = (
            UIAutomationType.UIAutomationType_DoubleArray
        )
        UIAutomationType_PointArray = (
            UIAutomationType.UIAutomationType_PointArray
        )
        UIAutomationType_RectArray = (
            UIAutomationType.UIAutomationType_RectArray
        )
        UIAutomationType_ElementArray = (
            UIAutomationType.UIAutomationType_ElementArray
        )
        UIAutomationType_OutInt = (
            UIAutomationType.UIAutomationType_OutInt
        )
        UIAutomationType_OutBool = UIAutomationType.UIAutomationType_OutBool
        UIAutomationType_OutString = (
            UIAutomationType.UIAutomationType_OutString
        )
        UIAutomationType_OutDouble = (
            UIAutomationType.UIAutomationType_OutDouble
        )
        UIAutomationType_OutPoint = UIAutomationType.UIAutomationType_OutPoint
        UIAutomationType_OutRect = UIAutomationType.UIAutomationType_OutRect
        UIAutomationType_OutElement = (
            UIAutomationType.UIAutomationType_OutElement
        )
        UIAutomationType_OutIntArray = (
            UIAutomationType.UIAutomationType_OutIntArray
        )
        UIAutomationType_OutBoolArray = (
            UIAutomationType.UIAutomationType_OutBoolArray
        )
        UIAutomationType_OutStringArray = (
            UIAutomationType.UIAutomationType_OutStringArray
        )
        UIAutomationType_OutDoubleArray = (
            UIAutomationType.UIAutomationType_OutDoubleArray
        )
        UIAutomationType_OutPointArray = (
            UIAutomationType.UIAutomationType_OutPointArray
        )
        UIAutomationType_OutRectArray = (
            UIAutomationType.UIAutomationType_OutRectArray
        )
        UIAutomationType_OutElementArray = (
            UIAutomationType.UIAutomationType_OutElementArray
        )

        UIAutomationParameter._fields_ = [
            ('UIAutomationType type', enum),
            ('pData', POINTER(VOID)),
        ]
        UIAutomationPropertyInfo._fields_ = [
            ('guid', GUID),
            ('pProgrammaticName', LPCWSTR),
            ('UIAutomationType type', enum),
        ]
        UIAutomationEventInfo._fields_ = [
            ('guid', GUID),
            ('pProgrammaticName', LPCWSTR),
        ]
        UIAutomationMethodInfo._fields_ = [
            ('pProgrammaticName', LPCWSTR),
            ('doSetFocus', BOOL),
            ('cInParameters', UINT),
            ('cOutParameters', UINT),
            # [size_is]
            ('UIAutomationType *pParameterTypes', enum),
            # [size_is]
            ('pParameterNames', POINTER(LPCWSTR)),
        ]
        UIAutomationPatternInfo._fields_ = [
            ('guid', GUID),
            ('pProgrammaticName', LPCWSTR),
            ('providerInterfaceId', GUID),
            ('clientInterfaceId', GUID),
            ('cProperties', UINT),
            # [size_is]
            ('pProperties', POINTER(UIAutomationPropertyInfo)),
            ('cMethods', UINT),
            # [size_is]
            ('pMethods', POINTER(UIAutomationMethodInfo)),
            ('cEvents', UINT),
            # [size_is]
            ('pEvents', POINTER(UIAutomationEventInfo)),
            ('pPatternHandler', POINTER(IUIAutomationPatternHandler)),
        ]
        if not defined(__UIA_OtherConstants_MODULE_DEFINED__):
            __UIA_OtherConstants_MODULE_DEFINED__ = VOID

            # module UIA_OtherConstants
            # [dllname]        # END IF  __UIA_OtherConstants_MODULE_DEFINED__
        if not defined(__IRawElementProviderSimple_INTERFACE_DEFINED__):
            __IRawElementProviderSimple_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderSimple
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderSimple = MIDL_INTERFACE(
                    "{D6DD68D1-86FD-4332-8666-9ABEDEA2D24C}"
                )
                IRawElementProviderSimple._iid_ = IID_IRawElementProviderSimple


                IRawElementProviderSimple._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ProviderOptions'), 'propget', 'in'],
                        HRESULT,
                        'ProviderOptions',
                        (
                            ['out', 'retval'],
                            POINTER(ProviderOptions),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPatternProvider')],
                        HRESULT,
                        'GetPatternProvider',
                        (['in'], PATTERNID, 'patternId'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetPropertyValue')],
                        HRESULT,
                        'GetPropertyValue',
                        (['in'], PROPERTYID, 'propertyId'),
                        (['retval', 'out'], POINTER(VARIANT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method HostRawElementProvider'), 'propget', 'in'],
                        HRESULT,
                        'HostRawElementProvider',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderSimple_INTERFACE_DEFINED__

        if not defined(__IAccessibleEx_INTERFACE_DEFINED__):
            __IAccessibleEx_INTERFACE_DEFINED__ = VOID

            # interface IAccessibleEx
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IAccessibleEx = MIDL_INTERFACE(
                    "{F8B80ADA-2C44-48D0-89BE-5FF23C9CD875}"
                )
                IAccessibleEx._iid_ = IID_IAccessibleEx


                IAccessibleEx._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetObjectForChild')],
                        HRESULT,
                        'GetObjectForChild',
                        (['in'], LONG, 'idChild'),
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IAccessibleEx)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetIAccessiblePair')],
                        HRESULT,
                        'GetIAccessiblePair',
                        (['out'], POINTER(POINTER(IAccessible)), 'ppAcc'),
                        (['out'], POINTER(LONG), 'pidChild'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRuntimeId')],
                        HRESULT,
                        'GetRuntimeId',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ConvertReturnedElement')],
                        HRESULT,
                        'ConvertReturnedElement',
                        (['in'], POINTER(IRawElementProviderSimple), 'pIn'),
                        (
                            ['out'],
                            POINTER(POINTER(IAccessibleEx)),
                            'ppRetValOut'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IAccessibleEx_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderSimple2_INTERFACE_DEFINED__):
            __IRawElementProviderSimple2_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderSimple2
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderSimple2 = MIDL_INTERFACE(
                    "{A0A839A9-8DA1-4A82-806A-8E0D44E79F56}"
                )
                IRawElementProviderSimple2._iid_ = IID_IRawElementProviderSimple2


                IRawElementProviderSimple2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ShowContextMenu')],
                        HRESULT,
                        'ShowContextMenu',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderSimple2_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderSimple3_INTERFACE_DEFINED__):
            __IRawElementProviderSimple3_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderSimple3
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderSimple3 = MIDL_INTERFACE(
                    "{FCF5D820-D7EC-4613-BDF6-42A84CE7DAAF}"
                )
                IRawElementProviderSimple3._iid_ = IID_IRawElementProviderSimple3


                IRawElementProviderSimple3._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetMetadataValue')],
                        HRESULT,
                        'GetMetadataValue',
                        (['in'], INT, 'targetId'),
                        (['in'], METADATAID, 'metadataId'),
                        (['out', 'retval'], POINTER(VARIANT), 'returnVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderSimple3_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderFragmentRoot_INTERFACE_DEFINED__):
            __IRawElementProviderFragmentRoot_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderFragmentRoot
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderFragmentRoot = MIDL_INTERFACE(
                    "{620CE2A5-AB8F-40A9-86CB-DE3C75599B58}"
                )
                IRawElementProviderFragmentRoot._iid_ = IID_IRawElementProviderFragmentRoot


                IRawElementProviderFragmentRoot._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ElementProviderFromPoint')],
                        HRESULT,
                        'ElementProviderFromPoint',
                        (['in'], DOUBLE, 'x'),
                        (['in'], DOUBLE, 'y'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderFragment)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetFocus')],
                        HRESULT,
                        'GetFocus',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderFragment)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderFragmentRoot_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderFragment_INTERFACE_DEFINED__):
            __IRawElementProviderFragment_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderFragment
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderFragment = MIDL_INTERFACE(
                    "{F7063DA8-8359-439C-9297-BBC5299A7D87}"
                )
                IRawElementProviderFragment._iid_ = IID_IRawElementProviderFragment


                IRawElementProviderFragment._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Navigate')],
                        HRESULT,
                        'Navigate',
                        (['in'], NavigateDirection, 'direction'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderFragment)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRuntimeId')],
                        HRESULT,
                        'GetRuntimeId',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method BoundingRectangle')],
                        HRESULT,
                        'BoundingRectangle',
                        (['retval', 'out'], POINTER(UiaRect), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetEmbeddedFragmentRoots')],
                        HRESULT,
                        'GetEmbeddedFragmentRoots',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetFocus')],
                        HRESULT,
                        'SetFocus',
                    ),
                    COMMETHOD(
                        [helpstring('Method FragmentRoot'), 'propget', 'in'],
                        HRESULT,
                        'FragmentRoot',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IRawElementProviderFragmentRoot)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderFragment_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderAdviseEvents_INTERFACE_DEFINED__):
            __IRawElementProviderAdviseEvents_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderAdviseEvents
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderAdviseEvents = MIDL_INTERFACE(
                    "{A407B27B-0F6D-4427-9292-473C7BF93258}"
                )
                IRawElementProviderAdviseEvents._iid_ = IID_IRawElementProviderAdviseEvents


                IRawElementProviderAdviseEvents._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AdviseEventAdded')],
                        HRESULT,
                        'AdviseEventAdded',
                        (['in'], EVENTID, 'eventId'),
                        (['in'], POINTER(), 'propertyIDs'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AdviseEventRemoved')],
                        HRESULT,
                        'AdviseEventRemoved',
                        (['in'], EVENTID, 'eventId'),
                        (['in'], POINTER(), 'propertyIDs'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderAdviseEvents_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderHwndOverride_INTERFACE_DEFINED__):
            __IRawElementProviderHwndOverride_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderHwndOverride
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderHwndOverride = MIDL_INTERFACE(
                    "{1D5DF27C-8947-4425-B8D9-79787BB460B8}"
                )
                IRawElementProviderHwndOverride._iid_ = IID_IRawElementProviderHwndOverride


                IRawElementProviderHwndOverride._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetOverrideProviderForHwnd')],
                        HRESULT,
                        'GetOverrideProviderForHwnd',
                        (['in'], HWND, 'hwnd'),
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderHwndOverride_INTERFACE_DEFINED__

        if not defined(__IProxyProviderWinEventSink_INTERFACE_DEFINED__):
            __IProxyProviderWinEventSink_INTERFACE_DEFINED__ = VOID

            # interface IProxyProviderWinEventSink
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IProxyProviderWinEventSink = MIDL_INTERFACE(
                    "{4FD82B78-A43E-46AC-9803-0A6969C7C183}"
                )
                IProxyProviderWinEventSink._iid_ = IID_IProxyProviderWinEventSink


                IProxyProviderWinEventSink._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AddAutomationPropertyChangedEvent')],
                        HRESULT,
                        'AddAutomationPropertyChangedEvent',
                        (
                            ['in'],
                            POINTER(IRawElementProviderSimple),
                            'pProvider'
                        ),
                        (['in'], PROPERTYID, 'id'),
                        (['in'], VARIANT, 'newValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddAutomationEvent')],
                        HRESULT,
                        'AddAutomationEvent',
                        (
                            ['in'],
                            POINTER(IRawElementProviderSimple),
                            'pProvider'
                        ),
                        (['in'], EVENTID, 'id'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AddStructureChangedEvent')],
                        HRESULT,
                        'AddStructureChangedEvent',
                        (
                            ['in'],
                            POINTER(IRawElementProviderSimple),
                            'pProvider'
                        ),
                        (['in'], StructureChangeType, 'structureChangeType'),
                        (['in'], POINTER(), 'runtimeId'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IProxyProviderWinEventSink_INTERFACE_DEFINED__

        if not defined(__IProxyProviderWinEventHandler_INTERFACE_DEFINED__):
            __IProxyProviderWinEventHandler_INTERFACE_DEFINED__ = VOID

            # interface IProxyProviderWinEventHandler
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IProxyProviderWinEventHandler = MIDL_INTERFACE(
                    "{89592AD4-F4E0-43D5-A3B6-BAD7E111B435}"
                )
                IProxyProviderWinEventHandler._iid_ = IID_IProxyProviderWinEventHandler


                IProxyProviderWinEventHandler._methods_ = [
                    COMMETHOD(
                        [helpstring('Method RespondToWinEvent')],
                        HRESULT,
                        'RespondToWinEvent',
                        (['in'], DWORD, 'idWinEvent'),
                        (['in'], HWND, 'hwnd'),
                        (['in'], LONG, 'idObject'),
                        (['in'], LONG, 'idChild'),
                        (
                            ['in'],
                            POINTER(IProxyProviderWinEventSink),
                            'pSink'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IProxyProviderWinEventHandler_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderWindowlessSite_INTERFACE_DEFINED__):
            __IRawElementProviderWindowlessSite_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderWindowlessSite
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderWindowlessSite = MIDL_INTERFACE(
                    "{0A2A93CC-BFAD-42AC-9B2E-0991FB0D3EA0}"
                )
                IRawElementProviderWindowlessSite._iid_ = IID_IRawElementProviderWindowlessSite


                IRawElementProviderWindowlessSite._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetAdjacentFragment')],
                        HRESULT,
                        'GetAdjacentFragment',
                        (['in'], NavigateDirection, 'direction'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderFragment)),
                            'ppParent'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetRuntimeIdPrefix')],
                        HRESULT,
                        'GetRuntimeIdPrefix',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderWindowlessSite_INTERFACE_DEFINED__

        if not defined(__IAccessibleHostingElementProviders_INTERFACE_DEFINED__):
            __IAccessibleHostingElementProviders_INTERFACE_DEFINED__ = VOID

            # interface IAccessibleHostingElementProviders
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IAccessibleHostingElementProviders = MIDL_INTERFACE(
                    "{33AC331B-943E-4020-B295-DB37784974A3}"
                )
                IAccessibleHostingElementProviders._iid_ = IID_IAccessibleHostingElementProviders


                IAccessibleHostingElementProviders._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetEmbeddedFragmentRoots')],
                        HRESULT,
                        'GetEmbeddedFragmentRoots',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetObjectIdForProvider')],
                        HRESULT,
                        'GetObjectIdForProvider',
                        (
                            ['in'],
                            POINTER(IRawElementProviderSimple),
                            'pProvider'
                        ),
                        (['out'], POINTER(LONG), 'pidObject'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IAccessibleHostingElementProviders_INTERFACE_DEFINED__

        if not defined(__IRawElementProviderHostingAccessibles_INTERFACE_DEFINED__):
            __IRawElementProviderHostingAccessibles_INTERFACE_DEFINED__ = VOID

            # interface IRawElementProviderHostingAccessibles
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRawElementProviderHostingAccessibles = MIDL_INTERFACE(
                    "{24BE0B07-D37D-487A-98CF-A13ED465E9B3}"
                )
                IRawElementProviderHostingAccessibles._iid_ = IID_IRawElementProviderHostingAccessibles


                IRawElementProviderHostingAccessibles._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetEmbeddedAccessibles')],
                        HRESULT,
                        'GetEmbeddedAccessibles',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRawElementProviderHostingAccessibles_INTERFACE_DEFINED__

        if not defined(__IDockProvider_INTERFACE_DEFINED__):
            __IDockProvider_INTERFACE_DEFINED__ = VOID

            # interface IDockProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDockProvider = MIDL_INTERFACE(
                    "{159BC72C-4AD3-485E-9637-D7052EDF0146}"
                )
                IDockProvider._iid_ = IID_IDockProvider


                IDockProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetDockPosition')],
                        HRESULT,
                        'SetDockPosition',
                        (['in'], DockPosition, 'dockPosition'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DockPosition'), 'propget', 'in'],
                        HRESULT,
                        'DockPosition',
                        (['out', 'retval'], POINTER(DockPosition), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDockProvider_INTERFACE_DEFINED__

        if not defined(__IExpandCollapseProvider_INTERFACE_DEFINED__):
            __IExpandCollapseProvider_INTERFACE_DEFINED__ = VOID

            # interface IExpandCollapseProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IExpandCollapseProvider = MIDL_INTERFACE(
                    "{D847D3A5-CAB0-4A98-8C32-ECB45C59AD24}"
                )
                IExpandCollapseProvider._iid_ = IID_IExpandCollapseProvider


                IExpandCollapseProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Expand')],
                        HRESULT,
                        'Expand',
                    ),
                    COMMETHOD(
                        [helpstring('Method Collapse')],
                        HRESULT,
                        'Collapse',
                    ),
                    COMMETHOD(
                        [helpstring('Method ExpandCollapseState'), 'propget', 'in'],
                        HRESULT,
                        'ExpandCollapseState',
                        (
                            ['out', 'retval'],
                            POINTER(ExpandCollapseState),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IExpandCollapseProvider_INTERFACE_DEFINED__

        if not defined(__IGridProvider_INTERFACE_DEFINED__):
            __IGridProvider_INTERFACE_DEFINED__ = VOID

            # interface IGridProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IGridProvider = MIDL_INTERFACE(
                    "{B17D6187-0907-464B-A168-0EF17A1572B1}"
                )
                IGridProvider._iid_ = IID_IGridProvider


                IGridProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetItem')],
                        HRESULT,
                        'GetItem',
                        (['in'], INT, 'row'),
                        (['in'], INT, 'column'),
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method RowCount'), 'propget', 'in'],
                        HRESULT,
                        'RowCount',
                        (['out', 'retval'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ColumnCount'), 'propget', 'in'],
                        HRESULT,
                        'ColumnCount',
                        (['out', 'retval'], POINTER(INT), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IGridProvider_INTERFACE_DEFINED__

        if not defined(__IGridItemProvider_INTERFACE_DEFINED__):
            __IGridItemProvider_INTERFACE_DEFINED__ = VOID

            # interface IGridItemProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IGridItemProvider = MIDL_INTERFACE(
                    "{D02541F1-FB81-4D64-AE32-F520F8A6DBD1}"
                )
                IGridItemProvider._iid_ = IID_IGridItemProvider


                IGridItemProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Row'), 'propget', 'in'],
                        HRESULT,
                        'Row',
                        (['retval', 'out'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Column'), 'propget', 'in'],
                        HRESULT,
                        'Column',
                        (['out', 'retval'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RowSpan'), 'propget', 'in'],
                        HRESULT,
                        'RowSpan',
                        (['retval', 'out'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ColumnSpan'), 'propget', 'in'],
                        HRESULT,
                        'ColumnSpan',
                        (['out', 'retval'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ContainingGrid'), 'propget', 'in'],
                        HRESULT,
                        'ContainingGrid',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IGridItemProvider_INTERFACE_DEFINED__

        if not defined(__IInvokeProvider_INTERFACE_DEFINED__):
            __IInvokeProvider_INTERFACE_DEFINED__ = VOID

            # interface IInvokeProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IInvokeProvider = MIDL_INTERFACE(
                    "{54FCB24B-E18E-47A2-B4D3-ECCBE77599A2}"
                )
                IInvokeProvider._iid_ = IID_IInvokeProvider


                IInvokeProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Invoke')],
                        HRESULT,
                        'Invoke',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IInvokeProvider_INTERFACE_DEFINED__

        if not defined(__IMultipleViewProvider_INTERFACE_DEFINED__):
            __IMultipleViewProvider_INTERFACE_DEFINED__ = VOID

            # interface IMultipleViewProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IMultipleViewProvider = MIDL_INTERFACE(
                    "{6278CAB1-B556-4A1A-B4E0-418ACC523201}"
                )
                IMultipleViewProvider._iid_ = IID_IMultipleViewProvider


                IMultipleViewProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetViewName')],
                        HRESULT,
                        'GetViewName',
                        (['in'], INT, 'viewId'),
                        (['out', 'retval'], POINTER(BSTR), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetCurrentView')],
                        HRESULT,
                        'SetCurrentView',
                        (['in'], INT, 'viewId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CurrentView'), 'propget', 'in'],
                        HRESULT,
                        'CurrentView',
                        (['out', 'retval'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSupportedViews')],
                        HRESULT,
                        'GetSupportedViews',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IMultipleViewProvider_INTERFACE_DEFINED__

        if not defined(__IRangeValueProvider_INTERFACE_DEFINED__):
            __IRangeValueProvider_INTERFACE_DEFINED__ = VOID

            # interface IRangeValueProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IRangeValueProvider = MIDL_INTERFACE(
                    "{36DC7AEF-33E6-4691-AFE1-2BE7274B3D33}"
                )
                IRangeValueProvider._iid_ = IID_IRangeValueProvider


                IRangeValueProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetValue')],
                        HRESULT,
                        'SetValue',
                        (['in'], DOUBLE, 'val'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Value'), 'propget', 'in'],
                        HRESULT,
                        'Value',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsReadOnly'), 'propget', 'in'],
                        HRESULT,
                        'IsReadOnly',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Maximum'), 'propget', 'in'],
                        HRESULT,
                        'Maximum',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Minimum'), 'propget', 'in'],
                        HRESULT,
                        'Minimum',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method LargeChange'), 'propget', 'in'],
                        HRESULT,
                        'LargeChange',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SmallChange'), 'propget', 'in'],
                        HRESULT,
                        'SmallChange',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IRangeValueProvider_INTERFACE_DEFINED__

        if not defined(__IScrollItemProvider_INTERFACE_DEFINED__):
            __IScrollItemProvider_INTERFACE_DEFINED__ = VOID

            # interface IScrollItemProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IScrollItemProvider = MIDL_INTERFACE(
                    "{2360C714-4BF1-4B26-BA65-9B21316127EB}"
                )
                IScrollItemProvider._iid_ = IID_IScrollItemProvider


                IScrollItemProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ScrollIntoView')],
                        HRESULT,
                        'ScrollIntoView',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IScrollItemProvider_INTERFACE_DEFINED__

        if not defined(__ISelectionProvider_INTERFACE_DEFINED__):
            __ISelectionProvider_INTERFACE_DEFINED__ = VOID

            # interface ISelectionProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISelectionProvider = MIDL_INTERFACE(
                    "{FB8B03AF-3BDF-48D4-BD36-1A65793BE168}"
                )
                ISelectionProvider._iid_ = IID_ISelectionProvider


                ISelectionProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSelection')],
                        HRESULT,
                        'GetSelection',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanSelectMultiple'), 'propget', 'in'],
                        HRESULT,
                        'CanSelectMultiple',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsSelectionRequired'), 'propget', 'in'],
                        HRESULT,
                        'IsSelectionRequired',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISelectionProvider_INTERFACE_DEFINED__

        if not defined(__ISelectionProvider2_INTERFACE_DEFINED__):
            __ISelectionProvider2_INTERFACE_DEFINED__ = VOID

            # interface ISelectionProvider2
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISelectionProvider2 = MIDL_INTERFACE(
                    "{14F68475-EE1C-44F6-A869-D239381F0FE7}"
                )
                ISelectionProvider2._iid_ = IID_ISelectionProvider2


                ISelectionProvider2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method FirstSelectedItem'), 'propget', 'in'],
                        HRESULT,
                        'FirstSelectedItem',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'retVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method LastSelectedItem'), 'propget', 'in'],
                        HRESULT,
                        'LastSelectedItem',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'retVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method CurrentSelectedItem'), 'propget', 'in'],
                        HRESULT,
                        'CurrentSelectedItem',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'retVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ItemCount'), 'propget', 'in'],
                        HRESULT,
                        'ItemCount',
                        (['retval', 'out'], POINTER(INT), 'retVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISelectionProvider2_INTERFACE_DEFINED__

        if not defined(__IScrollProvider_INTERFACE_DEFINED__):
            __IScrollProvider_INTERFACE_DEFINED__ = VOID

            # interface IScrollProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IScrollProvider = MIDL_INTERFACE(
                    "{B38B8077-1FC3-42A5-8CAE-D40C2215055A}"
                )
                IScrollProvider._iid_ = IID_IScrollProvider


                IScrollProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Scroll')],
                        HRESULT,
                        'Scroll',
                        (['in'], ScrollAmount, 'horizontalAmount'),
                        (['in'], ScrollAmount, 'verticalAmount'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SetScrollPercent')],
                        HRESULT,
                        'SetScrollPercent',
                        (['in'], DOUBLE, 'horizontalPercent'),
                        (['in'], DOUBLE, 'verticalPercent'),
                    ),
                    COMMETHOD(
                        [helpstring('Method HorizontalScrollPercent'), 'propget', 'in'],
                        HRESULT,
                        'HorizontalScrollPercent',
                        (['retval', 'out'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method VerticalScrollPercent'), 'propget', 'in'],
                        HRESULT,
                        'VerticalScrollPercent',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method HorizontalViewSize'), 'propget', 'in'],
                        HRESULT,
                        'HorizontalViewSize',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method VerticalViewSize'), 'propget', 'in'],
                        HRESULT,
                        'VerticalViewSize',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method HorizontallyScrollable'), 'propget', 'in'],
                        HRESULT,
                        'HorizontallyScrollable',
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method VerticallyScrollable'), 'propget', 'in'],
                        HRESULT,
                        'VerticallyScrollable',
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IScrollProvider_INTERFACE_DEFINED__

        if not defined(__ISelectionItemProvider_INTERFACE_DEFINED__):
            __ISelectionItemProvider_INTERFACE_DEFINED__ = VOID

            # interface ISelectionItemProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISelectionItemProvider = MIDL_INTERFACE(
                    "{2ACAD808-B2D4-452D-A407-91FF1AD167B2}"
                )
                ISelectionItemProvider._iid_ = IID_ISelectionItemProvider


                ISelectionItemProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Select')],
                        HRESULT,
                        'Select',
                    ),
                    COMMETHOD(
                        [helpstring('Method AddToSelection')],
                        HRESULT,
                        'AddToSelection',
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveFromSelection')],
                        HRESULT,
                        'RemoveFromSelection',
                    ),
                    COMMETHOD(
                        [helpstring('Method IsSelected'), 'propget', 'in'],
                        HRESULT,
                        'IsSelected',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method SelectionContainer'), 'propget', 'in'],
                        HRESULT,
                        'SelectionContainer',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISelectionItemProvider_INTERFACE_DEFINED__

        if not defined(__ISynchronizedInputProvider_INTERFACE_DEFINED__):
            __ISynchronizedInputProvider_INTERFACE_DEFINED__ = VOID

            # interface ISynchronizedInputProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISynchronizedInputProvider = MIDL_INTERFACE(
                    "{29DB1A06-02CE-4CF7-9B42-565D4FAB20EE}"
                )
                ISynchronizedInputProvider._iid_ = IID_ISynchronizedInputProvider


                ISynchronizedInputProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method StartListening')],
                        HRESULT,
                        'StartListening',
                        (['in'], SynchronizedInputType, 'inputType'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Cancel')],
                        HRESULT,
                        'Cancel',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISynchronizedInputProvider_INTERFACE_DEFINED__

        if not defined(__ITableProvider_INTERFACE_DEFINED__):
            __ITableProvider_INTERFACE_DEFINED__ = VOID

            # interface ITableProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITableProvider = MIDL_INTERFACE(
                    "{9C860395-97B3-490A-B52A-858CC22AF166}"
                )
                ITableProvider._iid_ = IID_ITableProvider


                ITableProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetRowHeaders')],
                        HRESULT,
                        'GetRowHeaders',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetColumnHeaders')],
                        HRESULT,
                        'GetColumnHeaders',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RowOrColumnMajor'), 'propget', 'in'],
                        HRESULT,
                        'RowOrColumnMajor',
                        (
                            ['retval', 'out'],
                            POINTER(RowOrColumnMajor),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITableProvider_INTERFACE_DEFINED__

        if not defined(__ITableItemProvider_INTERFACE_DEFINED__):
            __ITableItemProvider_INTERFACE_DEFINED__ = VOID

            # interface ITableItemProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITableItemProvider = MIDL_INTERFACE(
                    "{B9734FA6-771F-4D78-9C90-2517999349CD}"
                )
                ITableItemProvider._iid_ = IID_ITableItemProvider


                ITableItemProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetRowHeaderItems')],
                        HRESULT,
                        'GetRowHeaderItems',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetColumnHeaderItems')],
                        HRESULT,
                        'GetColumnHeaderItems',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITableItemProvider_INTERFACE_DEFINED__

        if not defined(__IToggleProvider_INTERFACE_DEFINED__):
            __IToggleProvider_INTERFACE_DEFINED__ = VOID

            # interface IToggleProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IToggleProvider = MIDL_INTERFACE(
                    "{56D00BD0-C4F4-433C-A836-1A52A57E0892}"
                )
                IToggleProvider._iid_ = IID_IToggleProvider


                IToggleProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Toggle')],
                        HRESULT,
                        'Toggle',
                    ),
                    COMMETHOD(
                        [helpstring('Method ToggleState'), 'propget', 'in'],
                        HRESULT,
                        'ToggleState',
                        (['retval', 'out'], POINTER(ToggleState), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IToggleProvider_INTERFACE_DEFINED__

        if not defined(__ITransformProvider_INTERFACE_DEFINED__):
            __ITransformProvider_INTERFACE_DEFINED__ = VOID

            # interface ITransformProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITransformProvider = MIDL_INTERFACE(
                    "{6829DDC4-4F91-4FFA-B86F-BD3E2987CB4C}"
                )
                ITransformProvider._iid_ = IID_ITransformProvider


                ITransformProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Move')],
                        HRESULT,
                        'Move',
                        (['in'], DOUBLE, 'x'),
                        (['in'], DOUBLE, 'y'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Resize')],
                        HRESULT,
                        'Resize',
                        (['in'], DOUBLE, 'width'),
                        (['in'], DOUBLE, 'height'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Rotate')],
                        HRESULT,
                        'Rotate',
                        (['in'], DOUBLE, 'degrees'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanMove'), 'propget', 'in'],
                        HRESULT,
                        'CanMove',
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanResize'), 'propget', 'in'],
                        HRESULT,
                        'CanResize',
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanRotate'), 'propget', 'in'],
                        HRESULT,
                        'CanRotate',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITransformProvider_INTERFACE_DEFINED__

        if not defined(__IValueProvider_INTERFACE_DEFINED__):
            __IValueProvider_INTERFACE_DEFINED__ = VOID

            # interface IValueProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IValueProvider = MIDL_INTERFACE(
                    "{C7935180-6FB3-4201-B174-7DF73ADBF64A}"
                )
                IValueProvider._iid_ = IID_IValueProvider


                IValueProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetValue')],
                        HRESULT,
                        'SetValue',
                        (['in'], LPCWSTR, 'val'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Value'), 'propget', 'in'],
                        HRESULT,
                        'Value',
                        (['retval', 'out'], POINTER(BSTR), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsReadOnly'), 'propget', 'in'],
                        HRESULT,
                        'IsReadOnly',
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IValueProvider_INTERFACE_DEFINED__

        if not defined(__IWindowProvider_INTERFACE_DEFINED__):
            __IWindowProvider_INTERFACE_DEFINED__ = VOID

            # interface IWindowProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IWindowProvider = MIDL_INTERFACE(
                    "{987DF77B-DB06-4D77-8F8A-86A9C3BB90B9}"
                )
                IWindowProvider._iid_ = IID_IWindowProvider


                IWindowProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method SetVisualState')],
                        HRESULT,
                        'SetVisualState',
                        (['in'], WindowVisualState, 'state'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Close')],
                        HRESULT,
                        'Close',
                    ),
                    COMMETHOD(
                        [helpstring('Method WaitForInputIdle')],
                        HRESULT,
                        'WaitForInputIdle',
                        (['in'], INT, 'milliseconds'),
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanMaximize'), 'propget', 'in'],
                        HRESULT,
                        'CanMaximize',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanMinimize'), 'propget', 'in'],
                        HRESULT,
                        'CanMinimize',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsModal'), 'propget', 'in'],
                        HRESULT,
                        'IsModal',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method WindowVisualState'), 'propget', 'in'],
                        HRESULT,
                        'WindowVisualState',
                        (
                            ['out', 'retval'],
                            POINTER(WindowVisualState),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method WindowInteractionState'), 'propget', 'in'],
                        HRESULT,
                        'WindowInteractionState',
                        (
                            ['out', 'retval'],
                            POINTER(WindowInteractionState),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method IsTopmost'), 'propget', 'in'],
                        HRESULT,
                        'IsTopmost',
                        (['out', 'retval'], POINTER(BOOL), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IWindowProvider_INTERFACE_DEFINED__

        if not defined(__ILegacyIAccessibleProvider_INTERFACE_DEFINED__):
            __ILegacyIAccessibleProvider_INTERFACE_DEFINED__ = VOID

            # interface ILegacyIAccessibleProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ILegacyIAccessibleProvider = MIDL_INTERFACE(
                    "{E44C3566-915D-4070-99C6-047BFF5A08F5}"
                )
                ILegacyIAccessibleProvider._iid_ = IID_ILegacyIAccessibleProvider


                ILegacyIAccessibleProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Select')],
                        HRESULT,
                        'Select',
                        ([], LONG, 'flagsSelect'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DoDefaultAction')],
                        HRESULT,
                        'DoDefaultAction',
                    ),
                    COMMETHOD(
                        [helpstring('Method SetValue')],
                        HRESULT,
                        'SetValue',
                        (['in'], LPCWSTR, 'szValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetIAccessible')],
                        HRESULT,
                        'GetIAccessible',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IAccessible)),
                            'ppAccessible'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method ChildId'), 'propget', 'in'],
                        HRESULT,
                        'ChildId',
                        (['retval', 'out'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Name'), 'propget', 'in'],
                        HRESULT,
                        'Name',
                        (['out', 'retval'], POINTER(BSTR), 'pszName'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Value'), 'propget', 'in'],
                        HRESULT,
                        'Value',
                        (['retval', 'out'], POINTER(BSTR), 'pszValue'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Description'), 'propget', 'in'],
                        HRESULT,
                        'Description',
                        (['out', 'retval'], POINTER(BSTR), 'pszDescription'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Role'), 'propget', 'in'],
                        HRESULT,
                        'Role',
                        (['retval', 'out'], POINTER(DWORD), 'pdwRole'),
                    ),
                    COMMETHOD(
                        [helpstring('Method State'), 'propget', 'in'],
                        HRESULT,
                        'State',
                        (['out', 'retval'], POINTER(DWORD), 'pdwState'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Help'), 'propget', 'in'],
                        HRESULT,
                        'Help',
                        (['out', 'retval'], POINTER(BSTR), 'pszHelp'),
                    ),
                    COMMETHOD(
                        [helpstring('Method KeyboardShortcut'), 'propget', 'in'],
                        HRESULT,
                        'KeyboardShortcut',
                        (
                            ['retval', 'out'],
                            POINTER(BSTR),
                            'pszKeyboardShortcut'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetSelection')],
                        HRESULT,
                        'GetSelection',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER()),
                            'pvarSelectedChildren'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method DefaultAction'), 'propget', 'in'],
                        HRESULT,
                        'DefaultAction',
                        (
                            ['retval', 'out'],
                            POINTER(BSTR),
                            'pszDefaultAction'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ILegacyIAccessibleProvider_INTERFACE_DEFINED__

        if not defined(__IItemContainerProvider_INTERFACE_DEFINED__):
            __IItemContainerProvider_INTERFACE_DEFINED__ = VOID

            # interface IItemContainerProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IItemContainerProvider = MIDL_INTERFACE(
                    "{E747770B-39CE-4382-AB30-D8FB3F336F24}"
                )
                IItemContainerProvider._iid_ = IID_IItemContainerProvider


                IItemContainerProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method FindItemByProperty')],
                        HRESULT,
                        'FindItemByProperty',
                        (
                            ['in'],
                            POINTER(IRawElementProviderSimple),
                            'pStartAfter'
                        ),
                        (['in'], PROPERTYID, 'propertyId'),
                        (['in'], VARIANT, 'value'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pFound'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IItemContainerProvider_INTERFACE_DEFINED__

        if not defined(__IVirtualizedItemProvider_INTERFACE_DEFINED__):
            __IVirtualizedItemProvider_INTERFACE_DEFINED__ = VOID

            # interface IVirtualizedItemProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IVirtualizedItemProvider = MIDL_INTERFACE(
                    "{CB98B665-2D35-4FAC-AD35-F3C60D0C0B8B}"
                )
                IVirtualizedItemProvider._iid_ = IID_IVirtualizedItemProvider


                IVirtualizedItemProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Realize')],
                        HRESULT,
                        'Realize',
                    ),
                ]

            # END IF  C style interface
        # END IF  __IVirtualizedItemProvider_INTERFACE_DEFINED__

        if not defined(__IObjectModelProvider_INTERFACE_DEFINED__):
            __IObjectModelProvider_INTERFACE_DEFINED__ = VOID

            # interface IObjectModelProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IObjectModelProvider = MIDL_INTERFACE(
                    "{3AD86EBD-F5EF-483D-BB18-B1042A475D64}"
                )
                IObjectModelProvider._iid_ = IID_IObjectModelProvider


                IObjectModelProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetUnderlyingObjectModel')],
                        HRESULT,
                        'GetUnderlyingObjectModel',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'ppUnknown'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IObjectModelProvider_INTERFACE_DEFINED__

        if not defined(__IAnnotationProvider_INTERFACE_DEFINED__):
            __IAnnotationProvider_INTERFACE_DEFINED__ = VOID

            # interface IAnnotationProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IAnnotationProvider = MIDL_INTERFACE(
                    "{F95C7E80-BD63-4601-9782-445EBFF011FC}"
                )
                IAnnotationProvider._iid_ = IID_IAnnotationProvider


                IAnnotationProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method AnnotationTypeId'), 'propget', 'in'],
                        HRESULT,
                        'AnnotationTypeId',
                        (['out', 'retval'], POINTER(INT), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method AnnotationTypeName'), 'propget', 'in'],
                        HRESULT,
                        'AnnotationTypeName',
                        (['retval', 'out'], POINTER(BSTR), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Author'), 'propget', 'in'],
                        HRESULT,
                        'Author',
                        (['retval', 'out'], POINTER(BSTR), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DateTime'), 'propget', 'in'],
                        HRESULT,
                        'DateTime',
                        (['retval', 'out'], POINTER(BSTR), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Target'), 'propget', 'in'],
                        HRESULT,
                        'Target',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'retVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IAnnotationProvider_INTERFACE_DEFINED__

        if not defined(__IStylesProvider_INTERFACE_DEFINED__):
            __IStylesProvider_INTERFACE_DEFINED__ = VOID

            # interface IStylesProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IStylesProvider = MIDL_INTERFACE(
                    "{19B6B649-F5D7-4A6D-BDCB-129252BE588A}"
                )
                IStylesProvider._iid_ = IID_IStylesProvider


                IStylesProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method StyleId'), 'propget', 'in'],
                        HRESULT,
                        'StyleId',
                        (['retval', 'out'], POINTER(INT), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method StyleName'), 'propget', 'in'],
                        HRESULT,
                        'StyleName',
                        (['retval', 'out'], POINTER(BSTR), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FillColor'), 'propget', 'in'],
                        HRESULT,
                        'FillColor',
                        (['retval', 'out'], POINTER(INT), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FillPatternStyle'), 'propget', 'in'],
                        HRESULT,
                        'FillPatternStyle',
                        (['retval', 'out'], POINTER(BSTR), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Shape'), 'propget', 'in'],
                        HRESULT,
                        'Shape',
                        (['retval', 'out'], POINTER(BSTR), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FillPatternColor'), 'propget', 'in'],
                        HRESULT,
                        'FillPatternColor',
                        (['retval', 'out'], POINTER(INT), 'retVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ExtendedProperties'), 'propget', 'in'],
                        HRESULT,
                        'ExtendedProperties',
                        (['retval', 'out'], POINTER(BSTR), 'retVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IStylesProvider_INTERFACE_DEFINED__

        if not defined(__ISpreadsheetProvider_INTERFACE_DEFINED__):
            __ISpreadsheetProvider_INTERFACE_DEFINED__ = VOID

            # interface ISpreadsheetProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpreadsheetProvider = MIDL_INTERFACE(
                    "{6F6B5D35-5525-4F80-B758-85473832FFC7}"
                )
                ISpreadsheetProvider._iid_ = IID_ISpreadsheetProvider


                ISpreadsheetProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetItemByName')],
                        HRESULT,
                        'GetItemByName',
                        (['in'], LPCWSTR, 'name'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpreadsheetProvider_INTERFACE_DEFINED__

        if not defined(__ISpreadsheetItemProvider_INTERFACE_DEFINED__):
            __ISpreadsheetItemProvider_INTERFACE_DEFINED__ = VOID

            # interface ISpreadsheetItemProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ISpreadsheetItemProvider = MIDL_INTERFACE(
                    "{EAED4660-7B3D-4879-A2E6-365CE603F3D0}"
                )
                ISpreadsheetItemProvider._iid_ = IID_ISpreadsheetItemProvider


                ISpreadsheetItemProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Formula'), 'propget', 'in'],
                        HRESULT,
                        'Formula',
                        (['out', 'retval'], POINTER(BSTR), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAnnotationObjects')],
                        HRESULT,
                        'GetAnnotationObjects',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAnnotationTypes')],
                        HRESULT,
                        'GetAnnotationTypes',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ISpreadsheetItemProvider_INTERFACE_DEFINED__

        if not defined(__ITransformProvider2_INTERFACE_DEFINED__):
            __ITransformProvider2_INTERFACE_DEFINED__ = VOID

            # interface ITransformProvider2
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITransformProvider2 = MIDL_INTERFACE(
                    "{4758742F-7AC2-460C-BC48-09FC09308A93}"
                )
                ITransformProvider2._iid_ = IID_ITransformProvider2


                ITransformProvider2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Zoom')],
                        HRESULT,
                        'Zoom',
                        (['in'], DOUBLE, 'zoom'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CanZoom'), 'propget', 'in'],
                        HRESULT,
                        'CanZoom',
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ZoomLevel'), 'propget', 'in'],
                        HRESULT,
                        'ZoomLevel',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ZoomMinimum'), 'propget', 'in'],
                        HRESULT,
                        'ZoomMinimum',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ZoomMaximum'), 'propget', 'in'],
                        HRESULT,
                        'ZoomMaximum',
                        (['out', 'retval'], POINTER(DOUBLE), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ZoomByUnit')],
                        HRESULT,
                        'ZoomByUnit',
                        (['in'], ZoomUnit, 'zoomUnit'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITransformProvider2_INTERFACE_DEFINED__

        if not defined(__IDragProvider_INTERFACE_DEFINED__):
            __IDragProvider_INTERFACE_DEFINED__ = VOID

            # interface IDragProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDragProvider = MIDL_INTERFACE(
                    "{6AA7BBBB-7FF9-497D-904F-D20B897929D8}"
                )
                IDragProvider._iid_ = IID_IDragProvider


                IDragProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method IsGrabbed'), 'propget', 'in'],
                        HRESULT,
                        'IsGrabbed',
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DropEffect'), 'propget', 'in'],
                        HRESULT,
                        'DropEffect',
                        (['retval', 'out'], POINTER(BSTR), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DropEffects'), 'propget', 'in'],
                        HRESULT,
                        'DropEffects',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetGrabbedItems')],
                        HRESULT,
                        'GetGrabbedItems',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDragProvider_INTERFACE_DEFINED__

        if not defined(__IDropTargetProvider_INTERFACE_DEFINED__):
            __IDropTargetProvider_INTERFACE_DEFINED__ = VOID

            # interface IDropTargetProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IDropTargetProvider = MIDL_INTERFACE(
                    "{BAE82BFD-358A-481C-85A0-D8B4D90A5D61}"
                )
                IDropTargetProvider._iid_ = IID_IDropTargetProvider


                IDropTargetProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method DropTargetEffect'), 'propget', 'in'],
                        HRESULT,
                        'DropTargetEffect',
                        (['retval', 'out'], POINTER(BSTR), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method DropTargetEffects'), 'propget', 'in'],
                        HRESULT,
                        'DropTargetEffects',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IDropTargetProvider_INTERFACE_DEFINED__

        if not defined(__ITextRangeProvider_INTERFACE_DEFINED__):
            __ITextRangeProvider_INTERFACE_DEFINED__ = VOID

            # interface ITextRangeProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITextRangeProvider = MIDL_INTERFACE(
                    "{5347AD7B-C355-46F8-AFF5-909033582F63}"
                )
                ITextRangeProvider._iid_ = IID_ITextRangeProvider


                ITextRangeProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Clone')],
                        HRESULT,
                        'Clone',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Compare')],
                        HRESULT,
                        'Compare',
                        (['in'], POINTER(ITextRangeProvider), 'range'),
                        (['retval', 'out'], POINTER(BOOL), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CompareEndpoints')],
                        HRESULT,
                        'CompareEndpoints',
                        (['in'], TextPatternRangeEndpoint, 'endpoint'),
                        (['in'], POINTER(ITextRangeProvider), 'targetRange'),
                        (['in'], TextPatternRangeEndpoint, 'targetEndpoint'),
                        (['out', 'retval'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method ExpandToEnclosingUnit')],
                        HRESULT,
                        'ExpandToEnclosingUnit',
                        (['in'], TextUnit, 'unit'),
                    ),
                    COMMETHOD(
                        [helpstring('Method FindAttribute')],
                        HRESULT,
                        'FindAttribute',
                        (['in'], TEXTATTRIBUTEID, 'attributeId'),
                        (['in'], VARIANT, 'val'),
                        (['in'], BOOL, 'backward'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method FindText')],
                        HRESULT,
                        'FindText',
                        (['in'], BSTR, 'text'),
                        (['in'], BOOL, 'backward'),
                        (['in'], BOOL, 'ignoreCase'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetAttributeValue')],
                        HRESULT,
                        'GetAttributeValue',
                        (['in'], TEXTATTRIBUTEID, 'attributeId'),
                        (['retval', 'out'], POINTER(VARIANT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetBoundingRectangles')],
                        HRESULT,
                        'GetBoundingRectangles',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetEnclosingElement')],
                        HRESULT,
                        'GetEnclosingElement',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetText')],
                        HRESULT,
                        'GetText',
                        (['in'], INT, 'maxLength'),
                        (['retval', 'out'], POINTER(BSTR), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Move')],
                        HRESULT,
                        'Move',
                        (['in'], TextUnit, 'unit'),
                        (['in'], INT, 'count'),
                        (['retval', 'out'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method MoveEndpointByUnit')],
                        HRESULT,
                        'MoveEndpointByUnit',
                        (['in'], TextPatternRangeEndpoint, 'endpoint'),
                        (['in'], TextUnit, 'unit'),
                        (['in'], INT, 'count'),
                        (['retval', 'out'], POINTER(INT), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method MoveEndpointByRange')],
                        HRESULT,
                        'MoveEndpointByRange',
                        (['in'], TextPatternRangeEndpoint, 'endpoint'),
                        (['in'], POINTER(ITextRangeProvider), 'targetRange'),
                        (['in'], TextPatternRangeEndpoint, 'targetEndpoint'),
                    ),
                    COMMETHOD(
                        [helpstring('Method Select')],
                        HRESULT,
                        'Select',
                    ),
                    COMMETHOD(
                        [helpstring('Method AddToSelection')],
                        HRESULT,
                        'AddToSelection',
                    ),
                    COMMETHOD(
                        [helpstring('Method RemoveFromSelection')],
                        HRESULT,
                        'RemoveFromSelection',
                    ),
                    COMMETHOD(
                        [helpstring('Method ScrollIntoView')],
                        HRESULT,
                        'ScrollIntoView',
                        (['in'], BOOL, 'alignToTop'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetChildren')],
                        HRESULT,
                        'GetChildren',
                        (['out', 'retval'], POINTER(POINTER()), 'pRetVal'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITextRangeProvider_INTERFACE_DEFINED__

        if not defined(__ITextProvider_INTERFACE_DEFINED__):
            __ITextProvider_INTERFACE_DEFINED__ = VOID

            # interface ITextProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITextProvider = MIDL_INTERFACE(
                    "{3589C92C-63F3-4367-99BB-ADA653B77CF2}"
                )
                ITextProvider._iid_ = IID_ITextProvider


                ITextProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetSelection')],
                        HRESULT,
                        'GetSelection',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetVisibleRanges')],
                        HRESULT,
                        'GetVisibleRanges',
                        (['retval', 'out'], POINTER(POINTER()), 'pRetVal'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RangeFromChild')],
                        HRESULT,
                        'RangeFromChild',
                        (
                            ['in'],
                            POINTER(IRawElementProviderSimple),
                            'childElement'
                        ),
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method RangeFromPoint')],
                        HRESULT,
                        'RangeFromPoint',
                        (['in'], UiaPoint, 'point'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method DocumentRange'), 'propget', 'in'],
                        HRESULT,
                        'DocumentRange',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method SupportedTextSelection'), 'propget', 'in'],
                        HRESULT,
                        'SupportedTextSelection',
                        (
                            ['retval', 'out'],
                            POINTER(SupportedTextSelection),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITextProvider_INTERFACE_DEFINED__

        if not defined(__ITextProvider2_INTERFACE_DEFINED__):
            __ITextProvider2_INTERFACE_DEFINED__ = VOID

            # interface ITextProvider2
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITextProvider2 = MIDL_INTERFACE(
                    "{0DC5E6ED-3E16-4BF1-8F9A-A979878BC195}"
                )
                ITextProvider2._iid_ = IID_ITextProvider2


                ITextProvider2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method RangeFromAnnotation')],
                        HRESULT,
                        'RangeFromAnnotation',
                        (
                            ['in'],
                            POINTER(IRawElementProviderSimple),
                            'annotationElement'
                        ),
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetCaretRange')],
                        HRESULT,
                        'GetCaretRange',
                        (['out'], POINTER(BOOL), 'isActive'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITextProvider2_INTERFACE_DEFINED__

        if not defined(__ITextEditProvider_INTERFACE_DEFINED__):
            __ITextEditProvider_INTERFACE_DEFINED__ = VOID

            # interface ITextEditProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITextEditProvider = MIDL_INTERFACE(
                    "{EA3605B4-3A05-400E-B5F9-4E91B40F6176}"
                )
                ITextEditProvider._iid_ = IID_ITextEditProvider


                ITextEditProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetActiveComposition')],
                        HRESULT,
                        'GetActiveComposition',
                        (
                            ['retval', 'out'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method GetConversionTarget')],
                        HRESULT,
                        'GetConversionTarget',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITextEditProvider_INTERFACE_DEFINED__

        if not defined(__ITextRangeProvider2_INTERFACE_DEFINED__):
            __ITextRangeProvider2_INTERFACE_DEFINED__ = VOID

            # interface ITextRangeProvider2
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITextRangeProvider2 = MIDL_INTERFACE(
                    "{9BBCE42C-1921-4F18-89CA-DBA1910A0386}"
                )
                ITextRangeProvider2._iid_ = IID_ITextRangeProvider2


                ITextRangeProvider2._methods_ = [
                    COMMETHOD(
                        [helpstring('Method ShowContextMenu')],
                        HRESULT,
                        'ShowContextMenu',
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITextRangeProvider2_INTERFACE_DEFINED__

        if not defined(__ITextChildProvider_INTERFACE_DEFINED__):
            __ITextChildProvider_INTERFACE_DEFINED__ = VOID

            # interface ITextChildProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ITextChildProvider = MIDL_INTERFACE(
                    "{4C2DE2B9-C88F-4F88-A111-F1D336B7D1A9}"
                )
                ITextChildProvider._iid_ = IID_ITextChildProvider


                ITextChildProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method TextContainer'), 'propget', 'in'],
                        HRESULT,
                        'TextContainer',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method TextRange'), 'propget', 'in'],
                        HRESULT,
                        'TextRange',
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(ITextRangeProvider)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ITextChildProvider_INTERFACE_DEFINED__

        if not defined(__ICustomNavigationProvider_INTERFACE_DEFINED__):
            __ICustomNavigationProvider_INTERFACE_DEFINED__ = VOID

            # interface ICustomNavigationProvider
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_ICustomNavigationProvider = MIDL_INTERFACE(
                    "{2062A28A-8C07-4B94-8E12-7037C622AEB8}"
                )
                ICustomNavigationProvider._iid_ = IID_ICustomNavigationProvider


                ICustomNavigationProvider._methods_ = [
                    COMMETHOD(
                        [helpstring('Method Navigate')],
                        HRESULT,
                        'Navigate',
                        (['in'], NavigateDirection, 'direction'),
                        (
                            ['out', 'retval'],
                            POINTER(POINTER(IRawElementProviderSimple)),
                            'pRetVal'
                        ),
                    ),
                ]

            # END IF  C style interface
        # END IF  __ICustomNavigationProvider_INTERFACE_DEFINED__

        if not defined(__IUIAutomationPatternInstance_INTERFACE_DEFINED__):
            __IUIAutomationPatternInstance_INTERFACE_DEFINED__ = VOID

            # interface IUIAutomationPatternInstance
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IUIAutomationPatternInstance = MIDL_INTERFACE(
                    "{C03A7FE4-9431-409F-BED8-AE7C2299BC8D}"
                )
                IUIAutomationPatternInstance._iid_ = IID_IUIAutomationPatternInstance


                IUIAutomationPatternInstance._methods_ = [
                    COMMETHOD(
                        [helpstring('Method GetProperty'), 'local', 'in'],
                        HRESULT,
                        'GetProperty',
                        (['in'], UINT, 'index'),
                        (['in'], BOOL, 'cached'),
                        (['in'], UIAutomationType, 'type'),
                        (['out'], POINTER(VOID), 'pPtr'),
                    ),
                    COMMETHOD(
                        [helpstring('Method CallMethod'), 'local', 'in'],
                        HRESULT,
                        'CallMethod',
                        (['in'], UINT, 'index'),
                        (['in'], POINTER(UIAutomationParameter), 'pParams'),
                        (['in'], UINT, 'cParams'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IUIAutomationPatternInstance_INTERFACE_DEFINED__

        if not defined(__IUIAutomationPatternHandler_INTERFACE_DEFINED__):
            __IUIAutomationPatternHandler_INTERFACE_DEFINED__ = VOID

            # interface IUIAutomationPatternHandler
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IUIAutomationPatternHandler = MIDL_INTERFACE(
                    "{D97022F3-A947-465E-8B2A-AC4315FA54E8}"
                )
                IUIAutomationPatternHandler._iid_ = IID_IUIAutomationPatternHandler


                IUIAutomationPatternHandler._methods_ = [
                    COMMETHOD(
                        [helpstring('Method CreateClientWrapper')],
                        HRESULT,
                        'CreateClientWrapper',
                        (
                            ['in'],
                            POINTER(IUIAutomationPatternInstance),
                            'pPatternInstance'
                        ),
                        (
                            ['out'],
                            POINTER(POINTER(comtypes.IUnknown)),
                            'pClientWrapper'
                        ),
                    ),
                    COMMETHOD(
                        [helpstring('Method Dispatch'), 'local', 'in'],
                        HRESULT,
                        'Dispatch',
                        (['in'], POINTER(comtypes.IUnknown), 'pTarget'),
                        (['in'], UINT, 'index'),
                        (['in'], POINTER(UIAutomationParameter), 'pParams'),
                        (['in'], UINT, 'cParams'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IUIAutomationPatternHandler_INTERFACE_DEFINED__

        if not defined(__IUIAutomationRegistrar_INTERFACE_DEFINED__):
            __IUIAutomationRegistrar_INTERFACE_DEFINED__ = VOID

            # interface IUIAutomationRegistrar
            # [oleautomation][unique][uuid][object]
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else:
                IID_IUIAutomationRegistrar = MIDL_INTERFACE(
                    "{8609C4EC-4A1A-4D88-A357-5A66E060E1CF}"
                )
                IUIAutomationRegistrar._iid_ = IID_IUIAutomationRegistrar


                IUIAutomationRegistrar._methods_ = [
                    COMMETHOD(
                        [helpstring('Method RegisterProperty')],
                        HRESULT,
                        'RegisterProperty',
                        (
                            ['in'],
                            POINTER(UIAutomationPropertyInfo),
                            'property'
                        ),
                        (['out'], POINTER(PROPERTYID), 'propertyId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RegisterEvent')],
                        HRESULT,
                        'RegisterEvent',
                        (['in'], POINTER(UIAutomationEventInfo), 'event'),
                        (['out'], POINTER(EVENTID), 'eventId'),
                    ),
                    COMMETHOD(
                        [helpstring('Method RegisterPattern')],
                        HRESULT,
                        'RegisterPattern',
                        (['in'], POINTER(UIAutomationPatternInfo), 'pattern'),
                        (['out'], POINTER(PATTERNID), 'pPatternId'),
                        (
                            ['out'],
                            POINTER(PROPERTYID),
                            'pPatternAvailablePropertyId'
                        ),
                        (['in'], UINT, 'propertyIdCount'),
                        (['out'], POINTER(PROPERTYID), 'pPropertyIds'),
                        (['in'], UINT, 'eventIdCount'),
                        (['out'], POINTER(EVENTID), 'pEventIds'),
                    ),
                ]

            # END IF  C style interface
        # END IF  __IUIAutomationRegistrar_INTERFACE_DEFINED__

        if defined(__cplusplus):
            pass
        # END IF

        CLSID_CUIAutomationRegistrar = DECLSPEC_UUID(
            "{6E29FABF-9977-42D1-8D0E-CA7E61AD87E6}"
        )

        LIBID_UIA = UUID(
            "{930299CE-9965-4dEC-B0F4-A54848D4B667}"
        )

        CUIAutomationRegistrar._com_interfaces_ += [IUIAutomationRegistrar]
        CUIAutomationRegistrar._reg_clsid_ = CLSID_CUIAutomationRegistrar
        CUIAutomationRegistrar._reg_typelib_ = (LIBID_UIA, 1, 0)

    # END IF  __UIA_LIBRARY_DEFINED__

    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


