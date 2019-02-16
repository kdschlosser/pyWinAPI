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
__uiautomationclient_h__ = None
__IUIAutomationElement_FWD_DEFINED__ = None
__IUIAutomationElementArray_FWD_DEFINED__ = None
__IUIAutomationCondition_FWD_DEFINED__ = None
__IUIAutomationBoolCondition_FWD_DEFINED__ = None
__IUIAutomationPropertyCondition_FWD_DEFINED__ = None
__IUIAutomationAndCondition_FWD_DEFINED__ = None
__IUIAutomationOrCondition_FWD_DEFINED__ = None
__IUIAutomationNotCondition_FWD_DEFINED__ = None
__IUIAutomationCacheRequest_FWD_DEFINED__ = None
__IUIAutomationTreeWalker_FWD_DEFINED__ = None
__IUIAutomationEventHandler_FWD_DEFINED__ = None
__IUIAutomationPropertyChangedEventHandler_FWD_DEFINED__ = None
__IUIAutomationStructureChangedEventHandler_FWD_DEFINED__ = None
__IUIAutomationFocusChangedEventHandler_FWD_DEFINED__ = None
__IUIAutomationTextEditTextChangedEventHandler_FWD_DEFINED__ = None
__IUIAutomationChangesEventHandler_FWD_DEFINED__ = None
__IUIAutomationNotificationEventHandler_FWD_DEFINED__ = None
__IUIAutomationInvokePattern_FWD_DEFINED__ = None
__IUIAutomationDockPattern_FWD_DEFINED__ = None
__IUIAutomationExpandCollapsePattern_FWD_DEFINED__ = None
__IUIAutomationGridPattern_FWD_DEFINED__ = None
__IUIAutomationGridItemPattern_FWD_DEFINED__ = None
__IUIAutomationMultipleViewPattern_FWD_DEFINED__ = None
__IUIAutomationObjectModelPattern_FWD_DEFINED__ = None
__IUIAutomationRangeValuePattern_FWD_DEFINED__ = None
__IUIAutomationScrollPattern_FWD_DEFINED__ = None
__IUIAutomationScrollItemPattern_FWD_DEFINED__ = None
__IUIAutomationSelectionPattern_FWD_DEFINED__ = None
__IUIAutomationSelectionPattern2_FWD_DEFINED__ = None
__IUIAutomationSelectionItemPattern_FWD_DEFINED__ = None
__IUIAutomationSynchronizedInputPattern_FWD_DEFINED__ = None
__IUIAutomationTablePattern_FWD_DEFINED__ = None
__IUIAutomationTableItemPattern_FWD_DEFINED__ = None
__IUIAutomationTogglePattern_FWD_DEFINED__ = None
__IUIAutomationTransformPattern_FWD_DEFINED__ = None
__IUIAutomationValuePattern_FWD_DEFINED__ = None
__IUIAutomationWindowPattern_FWD_DEFINED__ = None
__IUIAutomationTextRange_FWD_DEFINED__ = None
__IUIAutomationTextRange2_FWD_DEFINED__ = None
__IUIAutomationTextRange3_FWD_DEFINED__ = None
__IUIAutomationTextRangeArray_FWD_DEFINED__ = None
__IUIAutomationTextPattern_FWD_DEFINED__ = None
__IUIAutomationTextPattern2_FWD_DEFINED__ = None
__IUIAutomationTextEditPattern_FWD_DEFINED__ = None
__IUIAutomationCustomNavigationPattern_FWD_DEFINED__ = None
__IUIAutomationLegacyIAccessiblePattern_FWD_DEFINED__ = None
__IUIAutomationItemContainerPattern_FWD_DEFINED__ = None
__IUIAutomationVirtualizedItemPattern_FWD_DEFINED__ = None
__IUIAutomationAnnotationPattern_FWD_DEFINED__ = None
__IUIAutomationStylesPattern_FWD_DEFINED__ = None
__IUIAutomationSpreadsheetPattern_FWD_DEFINED__ = None
__IUIAutomationSpreadsheetItemPattern_FWD_DEFINED__ = None
__IUIAutomationTransformPattern2_FWD_DEFINED__ = None
__IUIAutomationTextChildPattern_FWD_DEFINED__ = None
__IUIAutomationDragPattern_FWD_DEFINED__ = None
__IUIAutomationDropTargetPattern_FWD_DEFINED__ = None
__IUIAutomationElement2_FWD_DEFINED__ = None
__IUIAutomationElement3_FWD_DEFINED__ = None
__IUIAutomationElement4_FWD_DEFINED__ = None
__IUIAutomationElement5_FWD_DEFINED__ = None
__IUIAutomationElement6_FWD_DEFINED__ = None
__IUIAutomationElement7_FWD_DEFINED__ = None
__IUIAutomationElement8_FWD_DEFINED__ = None
__IUIAutomationProxyFactory_FWD_DEFINED__ = None
__IUIAutomationProxyFactoryEntry_FWD_DEFINED__ = None
__IUIAutomationProxyFactoryMapping_FWD_DEFINED__ = None
__IUIAutomation_FWD_DEFINED__ = None
__IUIAutomation2_FWD_DEFINED__ = None
__IUIAutomation3_FWD_DEFINED__ = None
__IUIAutomation4_FWD_DEFINED__ = None
__IUIAutomation5_FWD_DEFINED__ = None
__CUIAutomation_FWD_DEFINED__ = None
__CUIAutomation8_FWD_DEFINED__ = None
_INC_UIAUTOMATIONCOREAPI = None
__UIAutomationClient_LIBRARY_DEFINED__ = None
__UIA_PatternIds_MODULE_DEFINED__ = None
__UIA_EventIds_MODULE_DEFINED__ = None
__UIA_PropertyIds_MODULE_DEFINED__ = None
__UIA_TextAttributeIds_MODULE_DEFINED__ = None
__UIA_ControlTypeIds_MODULE_DEFINED__ = None
__UIA_AnnotationTypes_MODULE_DEFINED__ = None
__UIA_StyleIds_MODULE_DEFINED__ = None
__UIA_LandmarkTypeIds_MODULE_DEFINED__ = None
__UIA_HeadingLevelIds_MODULE_DEFINED__ = None
__UIA_ChangeIds_MODULE_DEFINED__ = None
__UIA_MetadataIds_MODULE_DEFINED__ = None
__IUIAutomationElement_INTERFACE_DEFINED__ = None
__IUIAutomationElementArray_INTERFACE_DEFINED__ = None
__IUIAutomationCondition_INTERFACE_DEFINED__ = None
__IUIAutomationBoolCondition_INTERFACE_DEFINED__ = None
__IUIAutomationPropertyCondition_INTERFACE_DEFINED__ = None
__IUIAutomationAndCondition_INTERFACE_DEFINED__ = None
__IUIAutomationOrCondition_INTERFACE_DEFINED__ = None
__IUIAutomationNotCondition_INTERFACE_DEFINED__ = None
__IUIAutomationCacheRequest_INTERFACE_DEFINED__ = None
__IUIAutomationTreeWalker_INTERFACE_DEFINED__ = None
__IUIAutomationEventHandler_INTERFACE_DEFINED__ = None
__IUIAutomationPropertyChangedEventHandler_INTERFACE_DEFINED__ = None
__IUIAutomationStructureChangedEventHandler_INTERFACE_DEFINED__ = None
__IUIAutomationFocusChangedEventHandler_INTERFACE_DEFINED__ = None
__IUIAutomationTextEditTextChangedEventHandler_INTERFACE_DEFINED__ = None
__IUIAutomationChangesEventHandler_INTERFACE_DEFINED__ = None
__IUIAutomationNotificationEventHandler_INTERFACE_DEFINED__ = None
__IUIAutomationInvokePattern_INTERFACE_DEFINED__ = None
__IUIAutomationDockPattern_INTERFACE_DEFINED__ = None
__IUIAutomationExpandCollapsePattern_INTERFACE_DEFINED__ = None
__IUIAutomationGridPattern_INTERFACE_DEFINED__ = None
__IUIAutomationGridItemPattern_INTERFACE_DEFINED__ = None
__IUIAutomationMultipleViewPattern_INTERFACE_DEFINED__ = None
__IUIAutomationObjectModelPattern_INTERFACE_DEFINED__ = None
__IUIAutomationRangeValuePattern_INTERFACE_DEFINED__ = None
__IUIAutomationScrollPattern_INTERFACE_DEFINED__ = None
__IUIAutomationScrollItemPattern_INTERFACE_DEFINED__ = None
__IUIAutomationSelectionPattern_INTERFACE_DEFINED__ = None
__IUIAutomationSelectionPattern2_INTERFACE_DEFINED__ = None
__IUIAutomationSelectionItemPattern_INTERFACE_DEFINED__ = None
__IUIAutomationSynchronizedInputPattern_INTERFACE_DEFINED__ = None
__IUIAutomationTablePattern_INTERFACE_DEFINED__ = None
__IUIAutomationTableItemPattern_INTERFACE_DEFINED__ = None
__IUIAutomationTogglePattern_INTERFACE_DEFINED__ = None
__IUIAutomationTransformPattern_INTERFACE_DEFINED__ = None
__IUIAutomationValuePattern_INTERFACE_DEFINED__ = None
__IUIAutomationWindowPattern_INTERFACE_DEFINED__ = None
__IUIAutomationTextRange_INTERFACE_DEFINED__ = None
__IUIAutomationTextRange2_INTERFACE_DEFINED__ = None
__IUIAutomationTextRange3_INTERFACE_DEFINED__ = None
__IUIAutomationTextRangeArray_INTERFACE_DEFINED__ = None
__IUIAutomationTextPattern_INTERFACE_DEFINED__ = None
__IUIAutomationTextPattern2_INTERFACE_DEFINED__ = None
__IUIAutomationTextEditPattern_INTERFACE_DEFINED__ = None
__IUIAutomationCustomNavigationPattern_INTERFACE_DEFINED__ = None
__IUIAutomationLegacyIAccessiblePattern_INTERFACE_DEFINED__ = None
__IUIAutomationItemContainerPattern_INTERFACE_DEFINED__ = None
__IUIAutomationVirtualizedItemPattern_INTERFACE_DEFINED__ = None
__IUIAutomationAnnotationPattern_INTERFACE_DEFINED__ = None
__IUIAutomationStylesPattern_INTERFACE_DEFINED__ = None
__IUIAutomationSpreadsheetPattern_INTERFACE_DEFINED__ = None
__IUIAutomationSpreadsheetItemPattern_INTERFACE_DEFINED__ = None
__IUIAutomationTransformPattern2_INTERFACE_DEFINED__ = None
__IUIAutomationTextChildPattern_INTERFACE_DEFINED__ = None
__IUIAutomationDragPattern_INTERFACE_DEFINED__ = None
__IUIAutomationDropTargetPattern_INTERFACE_DEFINED__ = None
__IUIAutomationElement2_INTERFACE_DEFINED__ = None
__IUIAutomationElement3_INTERFACE_DEFINED__ = None
__IUIAutomationElement4_INTERFACE_DEFINED__ = None
__IUIAutomationElement5_INTERFACE_DEFINED__ = None
__IUIAutomationElement6_INTERFACE_DEFINED__ = None
__IUIAutomationElement7_INTERFACE_DEFINED__ = None
__IUIAutomationElement8_INTERFACE_DEFINED__ = None
__IUIAutomationProxyFactory_INTERFACE_DEFINED__ = None
__IUIAutomationProxyFactoryEntry_INTERFACE_DEFINED__ = None
__IUIAutomationProxyFactoryMapping_INTERFACE_DEFINED__ = None
__IUIAutomation_INTERFACE_DEFINED__ = None
__IUIAutomation2_INTERFACE_DEFINED__ = None
__IUIAutomation3_INTERFACE_DEFINED__ = None
__IUIAutomation4_INTERFACE_DEFINED__ = None
__IUIAutomation5_INTERFACE_DEFINED__ = None


class ExtendedProperty(ctypes.Structure):
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

if not defined(__uiautomationclient_h__):
    __uiautomationclient_h__ = VOID
    if defined(_MSC_VER) and (_MSC_VER  >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IUIAutomationElement_FWD_DEFINED__):
        __IUIAutomationElement_FWD_DEFINED__ = VOID


        class IUIAutomationElement(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement_FWD_DEFINED__

    if not defined(__IUIAutomationElementArray_FWD_DEFINED__):
        __IUIAutomationElementArray_FWD_DEFINED__ = VOID


        class IUIAutomationElementArray(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElementArray_FWD_DEFINED__

    if not defined(__IUIAutomationCondition_FWD_DEFINED__):
        __IUIAutomationCondition_FWD_DEFINED__ = VOID


        class IUIAutomationCondition(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationCondition_FWD_DEFINED__

    if not defined(__IUIAutomationBoolCondition_FWD_DEFINED__):
        __IUIAutomationBoolCondition_FWD_DEFINED__ = VOID


        class IUIAutomationBoolCondition(IUIAutomationCondition):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationBoolCondition_FWD_DEFINED__

    if not defined(__IUIAutomationPropertyCondition_FWD_DEFINED__):
        __IUIAutomationPropertyCondition_FWD_DEFINED__ = VOID


        class IUIAutomationPropertyCondition(IUIAutomationCondition):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationPropertyCondition_FWD_DEFINED__

    if not defined(__IUIAutomationAndCondition_FWD_DEFINED__):
        __IUIAutomationAndCondition_FWD_DEFINED__ = VOID


        class IUIAutomationAndCondition(IUIAutomationCondition):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationAndCondition_FWD_DEFINED__

    if not defined(__IUIAutomationOrCondition_FWD_DEFINED__):
        __IUIAutomationOrCondition_FWD_DEFINED__ = VOID


        class IUIAutomationOrCondition(IUIAutomationCondition):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationOrCondition_FWD_DEFINED__

    if not defined(__IUIAutomationNotCondition_FWD_DEFINED__):
        __IUIAutomationNotCondition_FWD_DEFINED__ = VOID


        class IUIAutomationNotCondition(IUIAutomationCondition):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationNotCondition_FWD_DEFINED__

    if not defined(__IUIAutomationCacheRequest_FWD_DEFINED__):
        __IUIAutomationCacheRequest_FWD_DEFINED__ = VOID


        class IUIAutomationCacheRequest(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationCacheRequest_FWD_DEFINED__

    if not defined(__IUIAutomationTreeWalker_FWD_DEFINED__):
        __IUIAutomationTreeWalker_FWD_DEFINED__ = VOID


        class IUIAutomationTreeWalker(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTreeWalker_FWD_DEFINED__

    if not defined(__IUIAutomationEventHandler_FWD_DEFINED__):
        __IUIAutomationEventHandler_FWD_DEFINED__ = VOID


        class IUIAutomationEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationEventHandler_FWD_DEFINED__

    if not defined(__IUIAutomationPropertyChangedEventHandler_FWD_DEFINED__):
        __IUIAutomationPropertyChangedEventHandler_FWD_DEFINED__ = VOID


        class IUIAutomationPropertyChangedEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationPropertyChangedEventHandler_FWD_DEFINED__

    if not defined(__IUIAutomationStructureChangedEventHandler_FWD_DEFINED__):
        __IUIAutomationStructureChangedEventHandler_FWD_DEFINED__ = VOID


        class IUIAutomationStructureChangedEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationStructureChangedEventHandler_FWD_DEFINED__

    if not defined(__IUIAutomationFocusChangedEventHandler_FWD_DEFINED__):
        __IUIAutomationFocusChangedEventHandler_FWD_DEFINED__ = VOID


        class IUIAutomationFocusChangedEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationFocusChangedEventHandler_FWD_DEFINED__

    if not defined(__IUIAutomationTextEditTextChangedEventHandler_FWD_DEFINED__):
        __IUIAutomationTextEditTextChangedEventHandler_FWD_DEFINED__ = VOID


        class IUIAutomationTextEditTextChangedEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextEditTextChangedEventHandler_FWD_DEFINED__

    if not defined(__IUIAutomationChangesEventHandler_FWD_DEFINED__):
        __IUIAutomationChangesEventHandler_FWD_DEFINED__ = VOID


        class IUIAutomationChangesEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationChangesEventHandler_FWD_DEFINED__

    if not defined(__IUIAutomationNotificationEventHandler_FWD_DEFINED__):
        __IUIAutomationNotificationEventHandler_FWD_DEFINED__ = VOID


        class IUIAutomationNotificationEventHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationNotificationEventHandler_FWD_DEFINED__

    if not defined(__IUIAutomationInvokePattern_FWD_DEFINED__):
        __IUIAutomationInvokePattern_FWD_DEFINED__ = VOID


        class IUIAutomationInvokePattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationInvokePattern_FWD_DEFINED__

    if not defined(__IUIAutomationDockPattern_FWD_DEFINED__):
        __IUIAutomationDockPattern_FWD_DEFINED__ = VOID


        class IUIAutomationDockPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationDockPattern_FWD_DEFINED__

    if not defined(__IUIAutomationExpandCollapsePattern_FWD_DEFINED__):
        __IUIAutomationExpandCollapsePattern_FWD_DEFINED__ = VOID


        class IUIAutomationExpandCollapsePattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationExpandCollapsePattern_FWD_DEFINED__

    if not defined(__IUIAutomationGridPattern_FWD_DEFINED__):
        __IUIAutomationGridPattern_FWD_DEFINED__ = VOID


        class IUIAutomationGridPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationGridPattern_FWD_DEFINED__

    if not defined(__IUIAutomationGridItemPattern_FWD_DEFINED__):
        __IUIAutomationGridItemPattern_FWD_DEFINED__ = VOID


        class IUIAutomationGridItemPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationGridItemPattern_FWD_DEFINED__

    if not defined(__IUIAutomationMultipleViewPattern_FWD_DEFINED__):
        __IUIAutomationMultipleViewPattern_FWD_DEFINED__ = VOID


        class IUIAutomationMultipleViewPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationMultipleViewPattern_FWD_DEFINED__

    if not defined(__IUIAutomationObjectModelPattern_FWD_DEFINED__):
        __IUIAutomationObjectModelPattern_FWD_DEFINED__ = VOID


        class IUIAutomationObjectModelPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationObjectModelPattern_FWD_DEFINED__

    if not defined(__IUIAutomationRangeValuePattern_FWD_DEFINED__):
        __IUIAutomationRangeValuePattern_FWD_DEFINED__ = VOID


        class IUIAutomationRangeValuePattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationRangeValuePattern_FWD_DEFINED__

    if not defined(__IUIAutomationScrollPattern_FWD_DEFINED__):
        __IUIAutomationScrollPattern_FWD_DEFINED__ = VOID


        class IUIAutomationScrollPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationScrollPattern_FWD_DEFINED__

    if not defined(__IUIAutomationScrollItemPattern_FWD_DEFINED__):
        __IUIAutomationScrollItemPattern_FWD_DEFINED__ = VOID


        class IUIAutomationScrollItemPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationScrollItemPattern_FWD_DEFINED__

    if not defined(__IUIAutomationSelectionPattern_FWD_DEFINED__):
        __IUIAutomationSelectionPattern_FWD_DEFINED__ = VOID


        class IUIAutomationSelectionPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationSelectionPattern_FWD_DEFINED__

    if not defined(__IUIAutomationSelectionPattern2_FWD_DEFINED__):
        __IUIAutomationSelectionPattern2_FWD_DEFINED__ = VOID


        class IUIAutomationSelectionPattern2(IUIAutomationSelectionPattern):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationSelectionPattern2_FWD_DEFINED__

    if not defined(__IUIAutomationSelectionItemPattern_FWD_DEFINED__):
        __IUIAutomationSelectionItemPattern_FWD_DEFINED__ = VOID


        class IUIAutomationSelectionItemPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationSelectionItemPattern_FWD_DEFINED__

    if not defined(__IUIAutomationSynchronizedInputPattern_FWD_DEFINED__):
        __IUIAutomationSynchronizedInputPattern_FWD_DEFINED__ = VOID


        class IUIAutomationSynchronizedInputPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationSynchronizedInputPattern_FWD_DEFINED__

    if not defined(__IUIAutomationTablePattern_FWD_DEFINED__):
        __IUIAutomationTablePattern_FWD_DEFINED__ = VOID


        class IUIAutomationTablePattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTablePattern_FWD_DEFINED__

    if not defined(__IUIAutomationTableItemPattern_FWD_DEFINED__):
        __IUIAutomationTableItemPattern_FWD_DEFINED__ = VOID


        class IUIAutomationTableItemPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTableItemPattern_FWD_DEFINED__

    if not defined(__IUIAutomationTogglePattern_FWD_DEFINED__):
        __IUIAutomationTogglePattern_FWD_DEFINED__ = VOID


        class IUIAutomationTogglePattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTogglePattern_FWD_DEFINED__

    if not defined(__IUIAutomationTransformPattern_FWD_DEFINED__):
        __IUIAutomationTransformPattern_FWD_DEFINED__ = VOID


        class IUIAutomationTransformPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTransformPattern_FWD_DEFINED__

    if not defined(__IUIAutomationValuePattern_FWD_DEFINED__):
        __IUIAutomationValuePattern_FWD_DEFINED__ = VOID


        class IUIAutomationValuePattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationValuePattern_FWD_DEFINED__

    if not defined(__IUIAutomationWindowPattern_FWD_DEFINED__):
        __IUIAutomationWindowPattern_FWD_DEFINED__ = VOID


        class IUIAutomationWindowPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationWindowPattern_FWD_DEFINED__

    if not defined(__IUIAutomationTextRange_FWD_DEFINED__):
        __IUIAutomationTextRange_FWD_DEFINED__ = VOID


        class IUIAutomationTextRange(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextRange_FWD_DEFINED__

    if not defined(__IUIAutomationTextRange2_FWD_DEFINED__):
        __IUIAutomationTextRange2_FWD_DEFINED__ = VOID


        class IUIAutomationTextRange2(IUIAutomationTextRange):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextRange2_FWD_DEFINED__

    if not defined(__IUIAutomationTextRange3_FWD_DEFINED__):
        __IUIAutomationTextRange3_FWD_DEFINED__ = VOID


        class IUIAutomationTextRange3(IUIAutomationTextRange2):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextRange3_FWD_DEFINED__

    if not defined(__IUIAutomationTextRangeArray_FWD_DEFINED__):
        __IUIAutomationTextRangeArray_FWD_DEFINED__ = VOID


        class IUIAutomationTextRangeArray(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextRangeArray_FWD_DEFINED__

    if not defined(__IUIAutomationTextPattern_FWD_DEFINED__):
        __IUIAutomationTextPattern_FWD_DEFINED__ = VOID


        class IUIAutomationTextPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextPattern_FWD_DEFINED__

    if not defined(__IUIAutomationTextPattern2_FWD_DEFINED__):
        __IUIAutomationTextPattern2_FWD_DEFINED__ = VOID


        class IUIAutomationTextPattern2(IUIAutomationTextPattern):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextPattern2_FWD_DEFINED__

    if not defined(__IUIAutomationTextEditPattern_FWD_DEFINED__):
        __IUIAutomationTextEditPattern_FWD_DEFINED__ = VOID


        class IUIAutomationTextEditPattern(IUIAutomationTextPattern):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextEditPattern_FWD_DEFINED__

    if not defined(__IUIAutomationCustomNavigationPattern_FWD_DEFINED__):
        __IUIAutomationCustomNavigationPattern_FWD_DEFINED__ = VOID


        class IUIAutomationCustomNavigationPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationCustomNavigationPattern_FWD_DEFINED__

    if not defined(__IUIAutomationLegacyIAccessiblePattern_FWD_DEFINED__):
        __IUIAutomationLegacyIAccessiblePattern_FWD_DEFINED__ = VOID


        class IUIAutomationLegacyIAccessiblePattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationLegacyIAccessiblePattern_FWD_DEFINED__

    if not defined(__IUIAutomationItemContainerPattern_FWD_DEFINED__):
        __IUIAutomationItemContainerPattern_FWD_DEFINED__ = VOID


        class IUIAutomationItemContainerPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationItemContainerPattern_FWD_DEFINED__

    if not defined(__IUIAutomationVirtualizedItemPattern_FWD_DEFINED__):
        __IUIAutomationVirtualizedItemPattern_FWD_DEFINED__ = VOID


        class IUIAutomationVirtualizedItemPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationVirtualizedItemPattern_FWD_DEFINED__

    if not defined(__IUIAutomationAnnotationPattern_FWD_DEFINED__):
        __IUIAutomationAnnotationPattern_FWD_DEFINED__ = VOID


        class IUIAutomationAnnotationPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationAnnotationPattern_FWD_DEFINED__

    if not defined(__IUIAutomationStylesPattern_FWD_DEFINED__):
        __IUIAutomationStylesPattern_FWD_DEFINED__ = VOID


        class IUIAutomationStylesPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationStylesPattern_FWD_DEFINED__

    if not defined(__IUIAutomationSpreadsheetPattern_FWD_DEFINED__):
        __IUIAutomationSpreadsheetPattern_FWD_DEFINED__ = VOID


        class IUIAutomationSpreadsheetPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationSpreadsheetPattern_FWD_DEFINED__

    if not defined(__IUIAutomationSpreadsheetItemPattern_FWD_DEFINED__):
        __IUIAutomationSpreadsheetItemPattern_FWD_DEFINED__ = VOID


        class IUIAutomationSpreadsheetItemPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationSpreadsheetItemPattern_FWD_DEFINED__

    if not defined(__IUIAutomationTransformPattern2_FWD_DEFINED__):
        __IUIAutomationTransformPattern2_FWD_DEFINED__ = VOID


        class IUIAutomationTransformPattern2(IUIAutomationTransformPattern):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTransformPattern2_FWD_DEFINED__

    if not defined(__IUIAutomationTextChildPattern_FWD_DEFINED__):
        __IUIAutomationTextChildPattern_FWD_DEFINED__ = VOID


        class IUIAutomationTextChildPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationTextChildPattern_FWD_DEFINED__

    if not defined(__IUIAutomationDragPattern_FWD_DEFINED__):
        __IUIAutomationDragPattern_FWD_DEFINED__ = VOID


        class IUIAutomationDragPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationDragPattern_FWD_DEFINED__

    if not defined(__IUIAutomationDropTargetPattern_FWD_DEFINED__):
        __IUIAutomationDropTargetPattern_FWD_DEFINED__ = VOID


        class IUIAutomationDropTargetPattern(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationDropTargetPattern_FWD_DEFINED__

    if not defined(__IUIAutomationElement2_FWD_DEFINED__):
        __IUIAutomationElement2_FWD_DEFINED__ = VOID


        class IUIAutomationElement2(IUIAutomationElement):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement2_FWD_DEFINED__

    if not defined(__IUIAutomationElement3_FWD_DEFINED__):
        __IUIAutomationElement3_FWD_DEFINED__ = VOID


        class IUIAutomationElement3(IUIAutomationElement2):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement3_FWD_DEFINED__

    if not defined(__IUIAutomationElement4_FWD_DEFINED__):
        __IUIAutomationElement4_FWD_DEFINED__ = VOID


        class IUIAutomationElement4(IUIAutomationElement3):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement4_FWD_DEFINED__

    if not defined(__IUIAutomationElement5_FWD_DEFINED__):
        __IUIAutomationElement5_FWD_DEFINED__ = VOID


        class IUIAutomationElement5(IUIAutomationElement4):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement5_FWD_DEFINED__

    if not defined(__IUIAutomationElement6_FWD_DEFINED__):
        __IUIAutomationElement6_FWD_DEFINED__ = VOID


        class IUIAutomationElement6(IUIAutomationElement5):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement6_FWD_DEFINED__

    if not defined(__IUIAutomationElement7_FWD_DEFINED__):
        __IUIAutomationElement7_FWD_DEFINED__ = VOID


        class IUIAutomationElement7(IUIAutomationElement6):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement7_FWD_DEFINED__

    if not defined(__IUIAutomationElement8_FWD_DEFINED__):
        __IUIAutomationElement8_FWD_DEFINED__ = VOID


        class IUIAutomationElement8(IUIAutomationElement7):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationElement8_FWD_DEFINED__

    if not defined(__IUIAutomationProxyFactory_FWD_DEFINED__):
        __IUIAutomationProxyFactory_FWD_DEFINED__ = VOID


        class IUIAutomationProxyFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationProxyFactory_FWD_DEFINED__

    if not defined(__IUIAutomationProxyFactoryEntry_FWD_DEFINED__):
        __IUIAutomationProxyFactoryEntry_FWD_DEFINED__ = VOID


        class IUIAutomationProxyFactoryEntry(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationProxyFactoryEntry_FWD_DEFINED__

    if not defined(__IUIAutomationProxyFactoryMapping_FWD_DEFINED__):
        __IUIAutomationProxyFactoryMapping_FWD_DEFINED__ = VOID


        class IUIAutomationProxyFactoryMapping(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomationProxyFactoryMapping_FWD_DEFINED__

    if not defined(__IUIAutomation_FWD_DEFINED__):
        __IUIAutomation_FWD_DEFINED__ = VOID


        class IUIAutomation(comtypes.IUnknown):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomation_FWD_DEFINED__

    if not defined(__IUIAutomation2_FWD_DEFINED__):
        __IUIAutomation2_FWD_DEFINED__ = VOID


        class IUIAutomation2(IUIAutomation):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomation2_FWD_DEFINED__

    if not defined(__IUIAutomation3_FWD_DEFINED__):
        __IUIAutomation3_FWD_DEFINED__ = VOID


        class IUIAutomation3(IUIAutomation2):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomation3_FWD_DEFINED__

    if not defined(__IUIAutomation4_FWD_DEFINED__):
        __IUIAutomation4_FWD_DEFINED__ = VOID


        class IUIAutomation4(IUIAutomation3):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomation4_FWD_DEFINED__

    if not defined(__IUIAutomation5_FWD_DEFINED__):
        __IUIAutomation5_FWD_DEFINED__ = VOID


        class IUIAutomation5(IUIAutomation4):
            _case_insensitive_ = True
            _iid_ = None
            _idlflags_ = []

    # END IF  __IUIAutomation5_FWD_DEFINED__

    if not defined(__CUIAutomation_FWD_DEFINED__):
        __CUIAutomation_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class CUIAutomation(comtypes.CoClass):
                """
                The Central Class for UIAutomation
                """
                _case_insensitive_ = True
                _idlflags_ = []
                _reg_clsid_ = None
                _reg_typelib_ = ()
                _com_interfaces_ = []

        # END IF  __cplusplus
    # END IF  __CUIAutomation_FWD_DEFINED__

    if not defined(__CUIAutomation8_FWD_DEFINED__):
        __CUIAutomation8_FWD_DEFINED__ = VOID
        if defined(__cplusplus):
            pass
        else:
            class CUIAutomation8(comtypes.CoClass):
                """
                The Central Class for UIAutomation8
                """
                _case_insensitive_ = True
                _idlflags_ = []
                _reg_clsid_ = None
                _reg_typelib_ = ()
                _com_interfaces_ = []

        # END IF  __cplusplus
    # END IF  __CUIAutomation8_FWD_DEFINED__

    # header files for imported files
    from pyWinAPI.um.uiautomationcore_h import * # NOQA

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_uiautomationclient_0000_0000
    # [local]
    # -------------------------------------------------------------
    # UIAutomationClient.H
    # UIAutomation Client interface definitions and related types and enums
    # (Generated from UIAutomationClient.idl)
    # Copyright (c) Microsoft Corporation. All rights reserved.
    # -------------------------------------------------------------
    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(_INC_UIAUTOMATIONCOREAPI):
            class TreeScope(ENUM):
                TreeScope_None = 0
                TreeScope_Element = 0x1
                TreeScope_Children = 0x2
                TreeScope_Descendants = 0x4
                TreeScope_Parent = 0x8
                TreeScope_Ancestors = 0x10
                TreeScope_Subtree = (
                    (TreeScope_Element | TreeScope_Children ) |
                    TreeScope_Descendants
                )


            TreeScope_None = TreeScope.TreeScope_None
            TreeScope_Element = TreeScope.TreeScope_Element
            TreeScope_Children = TreeScope.TreeScope_Children
            TreeScope_Descendants = TreeScope.TreeScope_Descendants
            TreeScope_Parent = TreeScope.TreeScope_Parent
            TreeScope_Ancestors = TreeScope.TreeScope_Ancestors
            TreeScope_Subtree = TreeScope.TreeScope_Subtree


            class PropertyConditionFlags(ENUM):
                PropertyConditionFlags_None = 0
                PropertyConditionFlags_IgnoreCase = 0x1

            PropertyConditionFlags_None = (
                PropertyConditionFlags.PropertyConditionFlags_None
            )
            PropertyConditionFlags_IgnoreCase = (
                PropertyConditionFlags.PropertyConditionFlags_IgnoreCase
            )


            class AutomationElementMode(ENUM):
                AutomationElementMode_None = 0
                AutomationElementMode_Full = AutomationElementMode_None + 1

            AutomationElementMode_None = (
                AutomationElementMode.AutomationElementMode_None
            )
            AutomationElementMode_Full = (
                AutomationElementMode.AutomationElementMode_Full
            )


            class TreeTraversalOptions(ENUM):
                TreeTraversalOptions_Default = 0
                TreeTraversalOptions_PostOrder = 0x1
                TreeTraversalOptions_LastToFirstOrder = 0x2

            TreeTraversalOptions_Default = (
                TreeTraversalOptions.TreeTraversalOptions_Default
            )
            TreeTraversalOptions_PostOrder = (
                TreeTraversalOptions.TreeTraversalOptions_PostOrder
            )
            TreeTraversalOptions_LastToFirstOrder = (
                TreeTraversalOptions.TreeTraversalOptions_LastToFirstOrder
            )
        # END IF

        ExtendedProperty._fields_ = [
            ('PropertyName', BSTR),
            ('PropertyValue', BSTR),
        ]
        UIA_HWND = POINTER(VOID)
        if not defined(__UIAutomationClient_LIBRARY_DEFINED__):
            __UIAutomationClient_LIBRARY_DEFINED__ = VOID

            # library UIAutomationClient
            # [version][lcid][uuid]
            if not defined(__UIA_PatternIds_MODULE_DEFINED__):
                __UIA_PatternIds_MODULE_DEFINED__ = VOID

                # module UIA_PatternIds
                # [dllname]
                UIA_InvokePatternId = 10000
                UIA_SelectionPatternId = 10001
                UIA_ValuePatternId = 10002
                UIA_RangeValuePatternId = 10003
                UIA_ScrollPatternId = 10004
                UIA_ExpandCollapsePatternId = 10005
                UIA_GridPatternId = 10006
                UIA_GridItemPatternId = 10007
                UIA_MultipleViewPatternId = 10008
                UIA_WindowPatternId = 10009
                UIA_SelectionItemPatternId = 10010
                UIA_DockPatternId = 10011
                UIA_TablePatternId = 10012
                UIA_TableItemPatternId = 10013
                UIA_TextPatternId = 10014
                UIA_TogglePatternId = 10015
                UIA_TransformPatternId = 10016
                UIA_ScrollItemPatternId = 10017
                UIA_LegacyIAccessiblePatternId = 10018
                UIA_ItemContainerPatternId = 10019
                UIA_VirtualizedItemPatternId = 10020
                UIA_SynchronizedInputPatternId = 10021
                UIA_ObjectModelPatternId = 10022
                UIA_AnnotationPatternId = 10023
                UIA_TextPattern2Id = 10024
                UIA_StylesPatternId = 10025
                UIA_SpreadsheetPatternId = 10026
                UIA_SpreadsheetItemPatternId = 10027
                UIA_TransformPattern2Id = 10028
                UIA_TextChildPatternId = 10029
                UIA_DragPatternId = 10030
                UIA_DropTargetPatternId = 10031
                UIA_TextEditPatternId = 10032
                UIA_CustomNavigationPatternId = 10033
                UIA_SelectionPattern2Id = 10034
            # END IF  __UIA_PatternIds_MODULE_DEFINED__

            if not defined(__UIA_EventIds_MODULE_DEFINED__):
                __UIA_EventIds_MODULE_DEFINED__ = VOID

                # module UIA_EventIds
                # [dllname]
                UIA_ToolTipOpenedEventId = 20000
                UIA_ToolTipClosedEventId = 20001
                UIA_StructureChangedEventId = 20002
                UIA_MenuOpenedEventId = 20003
                UIA_AutomationPropertyChangedEventId = 20004
                UIA_AutomationFocusChangedEventId = 20005
                UIA_AsyncContentLoadedEventId = 20006
                UIA_MenuClosedEventId = 20007
                UIA_LayoutInvalidatedEventId = 20008
                UIA_Invoke_InvokedEventId = 20009
                UIA_SelectionItem_ElementAddedToSelectionEventId = 20010
                UIA_SelectionItem_ElementRemovedFromSelectionEventId = 20011
                UIA_SelectionItem_ElementSelectedEventId = 20012
                UIA_Selection_InvalidatedEventId = 20013
                UIA_Text_TextSelectionChangedEventId = 20014
                UIA_Text_TextChangedEventId = 20015
                UIA_Window_WindowOpenedEventId = 20016
                UIA_Window_WindowClosedEventId = 20017
                UIA_MenuModeStartEventId = 20018
                UIA_MenuModeEndEventId = 20019
                UIA_InputReachedTargetEventId = 20020
                UIA_InputReachedOtherElementEventId = 20021
                UIA_InputDiscardedEventId = 20022
                UIA_SystemAlertEventId = 20023
                UIA_LiveRegionChangedEventId = 20024
                UIA_HostedFragmentRootsInvalidatedEventId = 20025
                UIA_Drag_DragStartEventId = 20026
                UIA_Drag_DragCancelEventId = 20027
                UIA_Drag_DragCompleteEventId = 20028
                UIA_DropTarDragEnterEventId = 20029
                UIA_DropTarDragLeaveEventId = 20030
                UIA_DropTarDroppedEventId = 20031
                UIA_TextEdit_TextChangedEventId = 20032
                UIA_TextEdit_ConversionTargetChangedEventId = 20033
                UIA_ChangesEventId = 20034
                UIA_NotificationEventId = 20035
            # END IF  __UIA_EventIds_MODULE_DEFINED__

            if not defined(__UIA_PropertyIds_MODULE_DEFINED__):
                __UIA_PropertyIds_MODULE_DEFINED__ = VOID

                # module UIA_PropertyIds
                # [dllname]
                UIA_RuntimeIdPropertyId = 30000
                UIA_BoundingRectanglePropertyId = 30001
                UIA_ProcessIdPropertyId = 30002
                UIA_ControlTypePropertyId = 30003
                UIA_LocalizedControlTypePropertyId = 30004
                UIA_NamePropertyId = 30005
                UIA_AcceleratorKeyPropertyId = 30006
                UIA_AccessKeyPropertyId = 30007
                UIA_HasKeyboardFocusPropertyId = 30008
                UIA_IsKeyboardFocusablePropertyId = 30009
                UIA_IsEnabledPropertyId = 30010
                UIA_AutomationIdPropertyId = 30011
                UIA_ClassNamePropertyId = 30012
                UIA_HelpTextPropertyId = 30013
                UIA_ClickablePointPropertyId = 30014
                UIA_CulturePropertyId = 30015
                UIA_IsControlElementPropertyId = 30016
                UIA_IsContentElementPropertyId = 30017
                UIA_LabeledByPropertyId = 30018
                UIA_IsPasswordPropertyId = 30019
                UIA_NativeWindowHandlePropertyId = 30020
                UIA_ItemTypePropertyId = 30021
                UIA_IsOffscreenPropertyId = 30022
                UIA_OrientationPropertyId = 30023
                UIA_FrameworkIdPropertyId = 30024
                UIA_IsRequiredForFormPropertyId = 30025
                UIA_ItemStatusPropertyId = 30026
                UIA_IsDockPatternAvailablePropertyId = 30027
                UIA_IsExpandCollapsePatternAvailablePropertyId = 30028
                UIA_IsGridItemPatternAvailablePropertyId = 30029
                UIA_IsGridPatternAvailablePropertyId = 30030
                UIA_IsInvokePatternAvailablePropertyId = 30031
                UIA_IsMultipleViewPatternAvailablePropertyId = 30032
                UIA_IsRangeValuePatternAvailablePropertyId = 30033
                UIA_IsScrollPatternAvailablePropertyId = 30034
                UIA_IsScrollItemPatternAvailablePropertyId = 30035
                UIA_IsSelectionItemPatternAvailablePropertyId = 30036
                UIA_IsSelectionPatternAvailablePropertyId = 30037
                UIA_IsTablePatternAvailablePropertyId = 30038
                UIA_IsTableItemPatternAvailablePropertyId = 30039
                UIA_IsTextPatternAvailablePropertyId = 30040
                UIA_IsTogglePatternAvailablePropertyId = 30041
                UIA_IsTransformPatternAvailablePropertyId = 30042
                UIA_IsValuePatternAvailablePropertyId = 30043
                UIA_IsWindowPatternAvailablePropertyId = 30044
                UIA_ValueValuePropertyId = 30045
                UIA_ValueIsReadOnlyPropertyId = 30046
                UIA_RangeValueValuePropertyId = 30047
                UIA_RangeValueIsReadOnlyPropertyId = 30048
                UIA_RangeValueMinimumPropertyId = 30049
                UIA_RangeValueMaximumPropertyId = 30050
                UIA_RangeValueLargeChangePropertyId = 30051
                UIA_RangeValueSmallChangePropertyId = 30052
                UIA_ScrollHorizontalScrollPercentPropertyId = 30053
                UIA_ScrollHorizontalViewSizePropertyId = 30054
                UIA_ScrollVerticalScrollPercentPropertyId = 30055
                UIA_ScrollVerticalViewSizePropertyId = 30056
                UIA_ScrollHorizontallyScrollablePropertyId = 30057
                UIA_ScrollVerticallyScrollablePropertyId = 30058
                UIA_SelectionSelectionPropertyId = 30059
                UIA_SelectionCanSelectMultiplePropertyId = 30060
                UIA_SelectionIsSelectionRequiredPropertyId = 30061
                UIA_GridRowCountPropertyId = 30062
                UIA_GridColumnCountPropertyId = 30063
                UIA_GridItemRowPropertyId = 30064
                UIA_GridItemColumnPropertyId = 30065
                UIA_GridItemRowSpanPropertyId = 30066
                UIA_GridItemColumnSpanPropertyId = 30067
                UIA_GridItemContainingGridPropertyId = 30068
                UIA_DockDockPositionPropertyId = 30069
                UIA_ExpandCollapseExpandCollapseStatePropertyId = 30070
                UIA_MultipleViewCurrentViewPropertyId = 30071
                UIA_MultipleViewSupportedViewsPropertyId = 30072
                UIA_WindowCanMaximizePropertyId = 30073
                UIA_WindowCanMinimizePropertyId = 30074
                UIA_WindowWindowVisualStatePropertyId = 30075
                UIA_WindowWindowInteractionStatePropertyId = 30076
                UIA_WindowIsModalPropertyId = 30077
                UIA_WindowIsTopmostPropertyId = 30078
                UIA_SelectionItemIsSelectedPropertyId = 30079
                UIA_SelectionItemSelectionContainerPropertyId = 30080
                UIA_TableRowHeadersPropertyId = 30081
                UIA_TableColumnHeadersPropertyId = 30082
                UIA_TableRowOrColumnMajorPropertyId = 30083
                UIA_TableItemRowHeaderItemsPropertyId = 30084
                UIA_TableItemColumnHeaderItemsPropertyId = 30085
                UIA_ToggleToggleStatePropertyId = 30086
                UIA_TransformCanMovePropertyId = 30087
                UIA_TransformCanResizePropertyId = 30088
                UIA_TransformCanRotatePropertyId = 30089
                UIA_IsLegacyIAccessiblePatternAvailablePropertyId = 30090
                UIA_LegacyIAccessibleChildIdPropertyId = 30091
                UIA_LegacyIAccessibleNamePropertyId = 30092
                UIA_LegacyIAccessibleValuePropertyId = 30093
                UIA_LegacyIAccessibleDescriptionPropertyId = 30094
                UIA_LegacyIAccessibleRolePropertyId = 30095
                UIA_LegacyIAccessibleStatePropertyId = 30096
                UIA_LegacyIAccessibleHelpPropertyId = 30097
                UIA_LegacyIAccessibleKeyboardShortcutPropertyId = 30098
                UIA_LegacyIAccessibleSelectionPropertyId = 30099
                UIA_LegacyIAccessibleDefaultActionPropertyId = 30100
                UIA_AriaRolePropertyId = 30101
                UIA_AriaPropertiesPropertyId = 30102
                UIA_IsDataValidForFormPropertyId = 30103
                UIA_ControllerForPropertyId = 30104
                UIA_DescribedByPropertyId = 30105
                UIA_FlowsToPropertyId = 30106
                UIA_ProviderDescriptionPropertyId = 30107
                UIA_IsItemContainerPatternAvailablePropertyId = 30108
                UIA_IsVirtualizedItemPatternAvailablePropertyId = 30109
                UIA_IsSynchronizedInputPatternAvailablePropertyId = 30110
                UIA_OptimizeForVisualContentPropertyId = 30111
                UIA_IsObjectModelPatternAvailablePropertyId = 30112
                UIA_AnnotationAnnotationTypeIdPropertyId = 30113
                UIA_AnnotationAnnotationTypeNamePropertyId = 30114
                UIA_AnnotationAuthorPropertyId = 30115
                UIA_AnnotationDateTimePropertyId = 30116
                UIA_AnnotationTargetPropertyId = 30117
                UIA_IsAnnotationPatternAvailablePropertyId = 30118
                UIA_IsTextPattern2AvailablePropertyId = 30119
                UIA_StylesStyleIdPropertyId = 30120
                UIA_StylesStyleNamePropertyId = 30121
                UIA_StylesFillColorPropertyId = 30122
                UIA_StylesFillPatternStylePropertyId = 30123
                UIA_StylesShapePropertyId = 30124
                UIA_StylesFillPatternColorPropertyId = 30125
                UIA_StylesExtendedPropertiesPropertyId = 30126
                UIA_IsStylesPatternAvailablePropertyId = 30127
                UIA_IsSpreadsheetPatternAvailablePropertyId = 30128
                UIA_SpreadsheetItemFormulaPropertyId = 30129
                UIA_SpreadsheetItemAnnotationObjectsPropertyId = 30130
                UIA_SpreadsheetItemAnnotationTypesPropertyId = 30131
                UIA_IsSpreadsheetItemPatternAvailablePropertyId = 30132
                UIA_Transform2CanZoomPropertyId = 30133
                UIA_IsTransformPattern2AvailablePropertyId = 30134
                UIA_LiveSettingPropertyId = 30135
                UIA_IsTextChildPatternAvailablePropertyId = 30136
                UIA_IsDragPatternAvailablePropertyId = 30137
                UIA_DragIsGrabbedPropertyId = 30138
                UIA_DragDropEffectPropertyId = 30139
                UIA_DragDropEffectsPropertyId = 30140
                UIA_IsDropTargetPatternAvailablePropertyId = 30141
                UIA_DropTargetDropTargetEffectPropertyId = 30142
                UIA_DropTargetDropTargetEffectsPropertyId = 30143
                UIA_DragGrabbedItemsPropertyId = 30144
                UIA_Transform2ZoomLevelPropertyId = 30145
                UIA_Transform2ZoomMinimumPropertyId = 30146
                UIA_Transform2ZoomMaximumPropertyId = 30147
                UIA_FlowsFromPropertyId = 30148
                UIA_IsTextEditPatternAvailablePropertyId = 30149
                UIA_IsPeripheralPropertyId = 30150
                UIA_IsCustomNavigationPatternAvailablePropertyId = 30151
                UIA_PositionInSetPropertyId = 30152
                UIA_SizeOfSetPropertyId = 30153
                UIA_LevelPropertyId = 30154
                UIA_AnnotationTypesPropertyId = 30155
                UIA_AnnotationObjectsPropertyId = 30156
                UIA_LandmarkTypePropertyId = 30157
                UIA_LocalizedLandmarkTypePropertyId = 30158
                UIA_FullDescriptionPropertyId = 30159
                UIA_FillColorPropertyId = 30160
                UIA_OutlineColorPropertyId = 30161
                UIA_FillTypePropertyId = 30162
                UIA_VisualEffectsPropertyId = 30163
                UIA_OutlineThicknessPropertyId = 30164
                UIA_CenterPointPropertyId = 30165
                UIA_RotationPropertyId = 30166
                UIA_SizePropertyId = 30167
                UIA_IsSelectionPattern2AvailablePropertyId = 30168
                UIA_Selection2FirstSelectedItemPropertyId = 30169
                UIA_Selection2LastSelectedItemPropertyId = 30170
                UIA_Selection2CurrentSelectedItemPropertyId = 30171
                UIA_Selection2ItemCountPropertyId = 30172
                UIA_HeadingLevelPropertyId = 30173
            # END IF  __UIA_PropertyIds_MODULE_DEFINED__

            if not defined(__UIA_TextAttributeIds_MODULE_DEFINED__):
                __UIA_TextAttributeIds_MODULE_DEFINED__ = VOID

                # module UIA_TextAttributeIds
                # [dllname]
                UIA_AnimationStyleAttributeId = 40000
                UIA_BackgroundColorAttributeId = 40001
                UIA_BulletStyleAttributeId = 40002
                UIA_CapStyleAttributeId = 40003
                UIA_CultureAttributeId = 40004
                UIA_FontNameAttributeId = 40005
                UIA_FontSizeAttributeId = 40006
                UIA_FontWeightAttributeId = 40007
                UIA_ForegroundColorAttributeId = 40008
                UIA_HorizontalTextAlignmentAttributeId = 40009
                UIA_IndentationFirstLineAttributeId = 40010
                UIA_IndentationLeadingAttributeId = 40011
                UIA_IndentationTrailingAttributeId = 40012
                UIA_IsHiddenAttributeId = 40013
                UIA_IsItalicAttributeId = 40014
                UIA_IsReadOnlyAttributeId = 40015
                UIA_IsSubscriptAttributeId = 40016
                UIA_IsSuperscriptAttributeId = 40017
                UIA_MarginBottomAttributeId = 40018
                UIA_MarginLeadingAttributeId = 40019
                UIA_MarginTopAttributeId = 40020
                UIA_MarginTrailingAttributeId = 40021
                UIA_OutlineStylesAttributeId = 40022
                UIA_OverlineColorAttributeId = 40023
                UIA_OverlineStyleAttributeId = 40024
                UIA_StrikethroughColorAttributeId = 40025
                UIA_StrikethroughStyleAttributeId = 40026
                UIA_TabsAttributeId = 40027
                UIA_TextFlowDirectionsAttributeId = 40028
                UIA_UnderlineColorAttributeId = 40029
                UIA_UnderlineStyleAttributeId = 40030
                UIA_AnnotationTypesAttributeId = 40031
                UIA_AnnotationObjectsAttributeId = 40032
                UIA_StyleNameAttributeId = 40033
                UIA_StyleIdAttributeId = 40034
                UIA_LinkAttributeId = 40035
                UIA_IsActiveAttributeId = 40036
                UIA_SelectionActiveEndAttributeId = 40037
                UIA_CaretPositionAttributeId = 40038
                UIA_CaretBidiModeAttributeId = 40039
                UIA_LineSpacingAttributeId = 40040
                UIA_BeforeParagraphSpacingAttributeId = 40041
                UIA_AfterParagraphSpacingAttributeId = 40042
                UIA_SayAsInterpretAsAttributeId = 40043
            # END IF  __UIA_TextAttributeIds_MODULE_DEFINED__

            if not defined(__UIA_ControlTypeIds_MODULE_DEFINED__):
                __UIA_ControlTypeIds_MODULE_DEFINED__ = VOID

                # module UIA_ControlTypeIds
                # [dllname]
                UIA_ButtonControlTypeId = 50000
                UIA_CalendarControlTypeId = 50001
                UIA_CheckBoxControlTypeId = 50002
                UIA_ComboBoxControlTypeId = 50003
                UIA_EditControlTypeId = 50004
                UIA_HyperlinkControlTypeId = 50005
                UIA_ImageControlTypeId = 50006
                UIA_ListItemControlTypeId = 50007
                UIA_ListControlTypeId = 50008
                UIA_MenuControlTypeId = 50009
                UIA_MenuBarControlTypeId = 50010
                UIA_MenuItemControlTypeId = 50011
                UIA_ProgressBarControlTypeId = 50012
                UIA_RadioButtonControlTypeId = 50013
                UIA_ScrollBarControlTypeId = 50014
                UIA_SliderControlTypeId = 50015
                UIA_SpinnerControlTypeId = 50016
                UIA_StatusBarControlTypeId = 50017
                UIA_TabControlTypeId = 50018
                UIA_TabItemControlTypeId = 50019
                UIA_TextControlTypeId = 50020
                UIA_ToolBarControlTypeId = 50021
                UIA_ToolTipControlTypeId = 50022
                UIA_TreeControlTypeId = 50023
                UIA_TreeItemControlTypeId = 50024
                UIA_CustomControlTypeId = 50025
                UIA_GroupControlTypeId = 50026
                UIA_ThumbControlTypeId = 50027
                UIA_DataGridControlTypeId = 50028
                UIA_DataItemControlTypeId = 50029
                UIA_DocumentControlTypeId = 50030
                UIA_SplitButtonControlTypeId = 50031
                UIA_WindowControlTypeId = 50032
                UIA_PaneControlTypeId = 50033
                UIA_HeaderControlTypeId = 50034
                UIA_HeaderItemControlTypeId = 50035
                UIA_TableControlTypeId = 50036
                UIA_TitleBarControlTypeId = 50037
                UIA_SeparatorControlTypeId = 50038
                UIA_SemanticZoomControlTypeId = 50039
                UIA_AppBarControlTypeId = 50040
            # END IF  __UIA_ControlTypeIds_MODULE_DEFINED__

            if not defined(__UIA_AnnotationTypes_MODULE_DEFINED__):
                __UIA_AnnotationTypes_MODULE_DEFINED__ = VOID

                # module UIA_AnnotationTypes
                # [dllname]
                AnnotationType_Unknown = 60000
                AnnotationType_SpellingError = 60001
                AnnotationType_GrammarError = 60002
                AnnotationType_Comment = 60003
                AnnotationType_FormulaError = 60004
                AnnotationType_TrackChanges = 60005
                AnnotationType_Header = 60006
                AnnotationType_Footer = 60007
                AnnotationType_Highlighted = 60008
                AnnotationType_Endnote = 60009
                AnnotationType_Footnote = 60010
                AnnotationType_InsertionChange = 60011
                AnnotationType_DeletionChange = 60012
                AnnotationType_MoveChange = 60013
                AnnotationType_FormatChange = 60014
                AnnotationType_UnsyncedChange = 60015
                AnnotationType_EditingLockedChange = 60016
                AnnotationType_ExternalChange = 60017
                AnnotationType_ConflictingChange = 60018
                AnnotationType_Author = 60019
                AnnotationType_AdvancedProofingIssue = 60020
                AnnotationType_DataValidationError = 60021
                AnnotationType_CircularReferenceError = 60022
                AnnotationType_Mathematics = 60023
            # END IF  __UIA_AnnotationTypes_MODULE_DEFINED__

            if not defined(__UIA_StyleIds_MODULE_DEFINED__):
                __UIA_StyleIds_MODULE_DEFINED__ = VOID

                # module UIA_StyleIds
                # [dllname]
                StyleId_Custom = 70000
                StyleId_Heading1 = 70001
                StyleId_Heading2 = 70002
                StyleId_Heading3 = 70003
                StyleId_Heading4 = 70004
                StyleId_Heading5 = 70005
                StyleId_Heading6 = 70006
                StyleId_Heading7 = 70007
                StyleId_Heading8 = 70008
                StyleId_Heading9 = 70009
                StyleId_Title = 70010
                StyleId_Subtitle = 70011
                StyleId_Normal = 70012
                StyleId_Emphasis = 70013
                StyleId_Quote = 70014
                StyleId_BulletedList = 70015
                StyleId_NumberedList = 70016
            # END IF  __UIA_StyleIds_MODULE_DEFINED__

            if not defined(__UIA_LandmarkTypeIds_MODULE_DEFINED__):
                __UIA_LandmarkTypeIds_MODULE_DEFINED__ = VOID

                # module UIA_LandmarkTypeIds
                # [dllname]
                UIA_CustomLandmarkTypeId = 80000
                UIA_FormLandmarkTypeId = 80001
                UIA_MainLandmarkTypeId = 80002
                UIA_NavigationLandmarkTypeId = 80003
                UIA_SearchLandmarkTypeId = 80004
            # END IF  __UIA_LandmarkTypeIds_MODULE_DEFINED__

            if not defined(__UIA_HeadingLevelIds_MODULE_DEFINED__):
                __UIA_HeadingLevelIds_MODULE_DEFINED__ = VOID

                # module UIA_HeadingLevelIds
                # [dllname]
                HeadingLevel_None = 80050
                HeadingLevel1 = 80051
                HeadingLevel2 = 80052
                HeadingLevel3 = 80053
                HeadingLevel4 = 80054
                HeadingLevel5 = 80055
                HeadingLevel6 = 80056
                HeadingLevel7 = 80057
                HeadingLevel8 = 80058
                HeadingLevel9 = 80059
            # END IF  __UIA_HeadingLevelIds_MODULE_DEFINED__

            if not defined(__UIA_ChangeIds_MODULE_DEFINED__):
                __UIA_ChangeIds_MODULE_DEFINED__ = VOID

                # module UIA_ChangeIds
                UIA_SummaryChangeId = 90000
            # END IF  __UIA_ChangeIds_MODULE_DEFINED__

            if not defined(__UIA_MetadataIds_MODULE_DEFINED__):
                __UIA_MetadataIds_MODULE_DEFINED__ = VOID

                # module UIA_MetadataIds
                # [dllname]
                UIA_SayAsInterpretAsMetadataId = 100000
            # END IF  __UIA_MetadataIds_MODULE_DEFINED__

            if not defined(__IUIAutomationElement_INTERFACE_DEFINED__):
                __IUIAutomationElement_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement = MIDL_INTERFACE(
                        "{D22108AA-8AC5-49A5-837B-37BBB3D7591E}"
                    )
                    IUIAutomationElement._iid_ = IID_IUIAutomationElement

                    IUIAutomationElement._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetFocus')],
                            HRESULT,
                            'SetFocus',
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRuntimeId')],
                            HRESULT,
                            'GetRuntimeId',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER()),
                                'runtimeId'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindFirst')],
                            HRESULT,
                            'FindFirst',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindAll')],
                            HRESULT,
                            'FindAll',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindFirstBuildCache')],
                            HRESULT,
                            'FindFirstBuildCache',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindAllBuildCache')],
                            HRESULT,
                            'FindAllBuildCache',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method BuildUpdatedCache')],
                            HRESULT,
                            'BuildUpdatedCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'updatedElement'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentPropertyValue')],
                            HRESULT,
                            'GetCurrentPropertyValue',
                            (['in'], PROPERTYID, 'propertyId'),
                            (['retval', 'out'], POINTER(VARIANT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentPropertyValueEx')],
                            HRESULT,
                            'GetCurrentPropertyValueEx',
                            (['in'], PROPERTYID, 'propertyId'),
                            (['in'], BOOL, 'ignoreDefaultValue'),
                            (['retval', 'out'], POINTER(VARIANT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedPropertyValue')],
                            HRESULT,
                            'GetCachedPropertyValue',
                            (['in'], PROPERTYID, 'propertyId'),
                            (['retval', 'out'], POINTER(VARIANT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedPropertyValueEx')],
                            HRESULT,
                            'GetCachedPropertyValueEx',
                            (['in'], PROPERTYID, 'propertyId'),
                            (['in'], BOOL, 'ignoreDefaultValue'),
                            (['out', 'retval'], POINTER(VARIANT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentPatternAs')],
                            HRESULT,
                            'GetCurrentPatternAs',
                            (['in'], PATTERNID, 'patternId'),
                            (['in'], REFIID, 'riid'),
                            (
                                ['retval', 'out', 'iid_is'],
                                POINTER(POINTER(VOID)),
                                'patternObject'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedPatternAs')],
                            HRESULT,
                            'GetCachedPatternAs',
                            (['in'], PATTERNID, 'patternId'),
                            (['in'], REFIID, 'riid'),
                            (
                                ['iid_is', 'retval', 'out'],
                                POINTER(POINTER(VOID)),
                                'patternObject'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentPattern')],
                            HRESULT,
                            'GetCurrentPattern',
                            (['in'], PATTERNID, 'patternId'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'patternObject'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedPattern')],
                            HRESULT,
                            'GetCachedPattern',
                            (['in'], PATTERNID, 'patternId'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'patternObject'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedParent')],
                            HRESULT,
                            'GetCachedParent',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'parent'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedChildren')],
                            HRESULT,
                            'GetCachedChildren',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'children'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentProcessId'), 'propget', 'in'],
                            HRESULT,
                            'CurrentProcessId',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentControlType'), 'propget', 'in'],
                            HRESULT,
                            'CurrentControlType',
                            (
                                ['out', 'retval'],
                                POINTER(CONTROLTYPEID),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentLocalizedControlType'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLocalizedControlType',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentName'), 'propget', 'in'],
                            HRESULT,
                            'CurrentName',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAcceleratorKey'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAcceleratorKey',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAccessKey'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAccessKey',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentHasKeyboardFocus'), 'propget', 'in'],
                            HRESULT,
                            'CurrentHasKeyboardFocus',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsKeyboardFocusable'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsKeyboardFocusable',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsEnabled'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsEnabled',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAutomationId'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAutomationId',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentClassName'), 'propget', 'in'],
                            HRESULT,
                            'CurrentClassName',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentHelpText'), 'propget', 'in'],
                            HRESULT,
                            'CurrentHelpText',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCulture'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCulture',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsControlElement'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsControlElement',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsContentElement'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsContentElement',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsPassword'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsPassword',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentNativeWindowHandle'), 'propget', 'in'],
                            HRESULT,
                            'CurrentNativeWindowHandle',
                            (['retval', 'out'], POINTER(UIA_HWND), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentItemType'), 'propget', 'in'],
                            HRESULT,
                            'CurrentItemType',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsOffscreen'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsOffscreen',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentOrientation'), 'propget', 'in'],
                            HRESULT,
                            'CurrentOrientation',
                            (
                                ['retval', 'out'],
                                POINTER(OrientationType),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentFrameworkId'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFrameworkId',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsRequiredForForm'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsRequiredForForm',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentItemStatus'), 'propget', 'in'],
                            HRESULT,
                            'CurrentItemStatus',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentBoundingRectangle'), 'propget', 'in'],
                            HRESULT,
                            'CurrentBoundingRectangle',
                            (['retval', 'out'], POINTER(RECT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentLabeledBy'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLabeledBy',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAriaRole'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAriaRole',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAriaProperties'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAriaProperties',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsDataValidForForm'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsDataValidForForm',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentControllerFor'), 'propget', 'in'],
                            HRESULT,
                            'CurrentControllerFor',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDescribedBy'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDescribedBy',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentFlowsTo'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFlowsTo',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentProviderDescription'), 'propget', 'in'],
                            HRESULT,
                            'CurrentProviderDescription',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedProcessId'), 'propget', 'in'],
                            HRESULT,
                            'CachedProcessId',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedControlType'), 'propget', 'in'],
                            HRESULT,
                            'CachedControlType',
                            (
                                ['out', 'retval'],
                                POINTER(CONTROLTYPEID),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLocalizedControlType'), 'propget', 'in'],
                            HRESULT,
                            'CachedLocalizedControlType',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedName'), 'propget', 'in'],
                            HRESULT,
                            'CachedName',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAcceleratorKey'), 'propget', 'in'],
                            HRESULT,
                            'CachedAcceleratorKey',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAccessKey'), 'propget', 'in'],
                            HRESULT,
                            'CachedAccessKey',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedHasKeyboardFocus'), 'propget', 'in'],
                            HRESULT,
                            'CachedHasKeyboardFocus',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsKeyboardFocusable'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsKeyboardFocusable',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsEnabled'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsEnabled',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAutomationId'), 'propget', 'in'],
                            HRESULT,
                            'CachedAutomationId',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedClassName'), 'propget', 'in'],
                            HRESULT,
                            'CachedClassName',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedHelpText'), 'propget', 'in'],
                            HRESULT,
                            'CachedHelpText',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCulture'), 'propget', 'in'],
                            HRESULT,
                            'CachedCulture',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsControlElement'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsControlElement',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsContentElement'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsContentElement',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsPassword'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsPassword',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedNativeWindowHandle'), 'propget', 'in'],
                            HRESULT,
                            'CachedNativeWindowHandle',
                            (['out', 'retval'], POINTER(UIA_HWND), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedItemType'), 'propget', 'in'],
                            HRESULT,
                            'CachedItemType',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsOffscreen'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsOffscreen',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedOrientation'), 'propget', 'in'],
                            HRESULT,
                            'CachedOrientation',
                            (
                                ['out', 'retval'],
                                POINTER(OrientationType),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFrameworkId'), 'propget', 'in'],
                            HRESULT,
                            'CachedFrameworkId',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsRequiredForForm'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsRequiredForForm',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedItemStatus'), 'propget', 'in'],
                            HRESULT,
                            'CachedItemStatus',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedBoundingRectangle'), 'propget', 'in'],
                            HRESULT,
                            'CachedBoundingRectangle',
                            (['out', 'retval'], POINTER(RECT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLabeledBy'), 'propget', 'in'],
                            HRESULT,
                            'CachedLabeledBy',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAriaRole'), 'propget', 'in'],
                            HRESULT,
                            'CachedAriaRole',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAriaProperties'), 'propget', 'in'],
                            HRESULT,
                            'CachedAriaProperties',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsDataValidForForm'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsDataValidForForm',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedControllerFor'), 'propget', 'in'],
                            HRESULT,
                            'CachedControllerFor',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDescribedBy'), 'propget', 'in'],
                            HRESULT,
                            'CachedDescribedBy',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFlowsTo'), 'propget', 'in'],
                            HRESULT,
                            'CachedFlowsTo',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedProviderDescription'), 'propget', 'in'],
                            HRESULT,
                            'CachedProviderDescription',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetClickablePoint')],
                            HRESULT,
                            'GetClickablePoint',
                            (['out'], POINTER(POINT), 'clickable'),
                            (
                                ['out', 'retval'],
                                POINTER(BOOL),
                                'gotClickable'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElementArray_INTERFACE_DEFINED__):
                __IUIAutomationElementArray_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElementArray
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElementArray = MIDL_INTERFACE(
                        "{14314595-B4BC-4055-95F2-58F2E42C9855}"
                    )
                    IUIAutomationElementArray._iid_ = IID_IUIAutomationElementArray


                    IUIAutomationElementArray._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Length'), 'propget', 'in'],
                            HRESULT,
                            'Length',
                            (['out', 'retval'], POINTER(INT), 'length'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetElement')],
                            HRESULT,
                            'GetElement',
                            (['in'], INT, 'index'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElementArray_INTERFACE_DEFINED__

            if not defined(__IUIAutomationCondition_INTERFACE_DEFINED__):
                __IUIAutomationCondition_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationCondition
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationCondition = MIDL_INTERFACE(
                        "{352FFBA8-0973-437C-A61F-F64CAFD81DF9}"
                    )
                    IUIAutomationCondition._iid_ = IID_IUIAutomationCondition


                    IUIAutomationCondition._methods_ = []


                # END IF  C style interface
            # END IF  __IUIAutomationCondition_INTERFACE_DEFINED__

            if not defined(__IUIAutomationBoolCondition_INTERFACE_DEFINED__):
                __IUIAutomationBoolCondition_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationBoolCondition
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationBoolCondition = MIDL_INTERFACE(
                        "{1B4E1F2E-75EB-4D0B-8952-5A69988E2307}"
                    )
                    IUIAutomationBoolCondition._iid_ = IID_IUIAutomationBoolCondition


                    IUIAutomationBoolCondition._methods_ = [
                        COMMETHOD(
                            [helpstring('Method BooleanValue'), 'propget', 'in'],
                            HRESULT,
                            'BooleanValue',
                            (['out', 'retval'], POINTER(BOOL), 'boolVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationBoolCondition_INTERFACE_DEFINED__

            if not defined(__IUIAutomationPropertyCondition_INTERFACE_DEFINED__):
                __IUIAutomationPropertyCondition_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationPropertyCondition
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationPropertyCondition = MIDL_INTERFACE(
                        "{99EBF2CB-5578-4267-9AD4-AFD6EA77E94B}"
                    )
                    IUIAutomationPropertyCondition._iid_ = IID_IUIAutomationPropertyCondition


                    IUIAutomationPropertyCondition._methods_ = [
                        COMMETHOD(
                            [helpstring('Method PropertyId'), 'propget', 'in'],
                            HRESULT,
                            'PropertyId',
                            (
                                ['retval', 'out'],
                                POINTER(PROPERTYID),
                                'propertyId'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method PropertyValue'), 'propget', 'in'],
                            HRESULT,
                            'PropertyValue',
                            (
                                ['retval', 'out'],
                                POINTER(VARIANT),
                                'propertyValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method PropertyConditionFlags'), 'propget', 'in'],
                            HRESULT,
                            'PropertyConditionFlags',
                            (
                                ['out', 'retval'],
                                POINTER(PropertyConditionFlags),
                                'flags'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationPropertyCondition_INTERFACE_DEFINED__

            if not defined(__IUIAutomationAndCondition_INTERFACE_DEFINED__):
                __IUIAutomationAndCondition_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationAndCondition
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationAndCondition = MIDL_INTERFACE(
                        "{A7D0AF36-B912-45FE-9855-091DDC174AEC}"
                    )
                    IUIAutomationAndCondition._iid_ = IID_IUIAutomationAndCondition


                    IUIAutomationAndCondition._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ChildCount'), 'propget', 'in'],
                            HRESULT,
                            'ChildCount',
                            (['retval', 'out'], POINTER(INT), 'childCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetChildrenAsNativeArray')],
                            HRESULT,
                            'GetChildrenAsNativeArray',
                            (
                                ['out'],
                                POINTER(POINTER(POINTER(IUIAutomationCondition))),
                                'childArray'
                            ),
                            (['out'], POINTER(INT), 'childArrayCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetChildren')],
                            HRESULT,
                            'GetChildren',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER()),
                                'childArray'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationAndCondition_INTERFACE_DEFINED__

            if not defined(__IUIAutomationOrCondition_INTERFACE_DEFINED__):
                __IUIAutomationOrCondition_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationOrCondition
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationOrCondition = MIDL_INTERFACE(
                        "{8753F032-3DB1-47B5-A1FC-6E34A266C712}"
                    )
                    IUIAutomationOrCondition._iid_ = IID_IUIAutomationOrCondition


                    IUIAutomationOrCondition._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ChildCount'), 'propget', 'in'],
                            HRESULT,
                            'ChildCount',
                            (['retval', 'out'], POINTER(INT), 'childCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetChildrenAsNativeArray')],
                            HRESULT,
                            'GetChildrenAsNativeArray',
                            (
                                ['out'],
                                POINTER(POINTER(POINTER(IUIAutomationCondition))),
                                'childArray'
                            ),
                            (['out'], POINTER(INT), 'childArrayCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetChildren')],
                            HRESULT,
                            'GetChildren',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER()),
                                'childArray'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationOrCondition_INTERFACE_DEFINED__

            if not defined(__IUIAutomationNotCondition_INTERFACE_DEFINED__):
                __IUIAutomationNotCondition_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationNotCondition
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationNotCondition = MIDL_INTERFACE(
                        "{F528B657-847B-498C-8896-D52B565407A1}"
                    )
                    IUIAutomationNotCondition._iid_ = IID_IUIAutomationNotCondition


                    IUIAutomationNotCondition._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetChild')],
                            HRESULT,
                            'GetChild',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'condition'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationNotCondition_INTERFACE_DEFINED__

            if not defined(__IUIAutomationCacheRequest_INTERFACE_DEFINED__):
                __IUIAutomationCacheRequest_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationCacheRequest
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationCacheRequest = MIDL_INTERFACE(
                        "{B32A92B5-BC25-4078-9C08-D7EE95C48E03}"
                    )
                    IUIAutomationCacheRequest._iid_ = IID_IUIAutomationCacheRequest


                    IUIAutomationCacheRequest._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddProperty')],
                            HRESULT,
                            'AddProperty',
                            (['in'], PROPERTYID, 'propertyId'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddPattern')],
                            HRESULT,
                            'AddPattern',
                            (['in'], PATTERNID, 'patternId'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Clone')],
                            HRESULT,
                            'Clone',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCacheRequest)),
                                'clonedRequest'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method TreeScope'), 'propget', 'in'],
                            HRESULT,
                            'TreeScope',
                            (['retval', 'out'], POINTER(TreeScope), 'scope'),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_TreeScope'), 'propput', 'in'],
                            HRESULT,
                            'put_TreeScope',
                            (['in'], TreeScope, 'scope'),
                        ),
                        COMMETHOD(
                            [helpstring('Method TreeFilter'), 'propget', 'in'],
                            HRESULT,
                            'TreeFilter',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'filter'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_TreeFilter'), 'propput', 'in'],
                            HRESULT,
                            'put_TreeFilter',
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'filter'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AutomationElementMode'), 'propget', 'in'],
                            HRESULT,
                            'AutomationElementMode',
                            (
                                ['out', 'retval'],
                                POINTER(AutomationElementMode),
                                'mode'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_AutomationElementMode'), 'propput', 'in'],
                            HRESULT,
                            'put_AutomationElementMode',
                            (['in'], AutomationElementMode, 'mode'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationCacheRequest_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTreeWalker_INTERFACE_DEFINED__):
                __IUIAutomationTreeWalker_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTreeWalker
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTreeWalker = MIDL_INTERFACE(
                        "{4042C624-389C-4AFC-A630-9DF854A541FC}"
                    )
                    IUIAutomationTreeWalker._iid_ = IID_IUIAutomationTreeWalker


                    IUIAutomationTreeWalker._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetParentElement')],
                            HRESULT,
                            'GetParentElement',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'parent'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFirstChildElement')],
                            HRESULT,
                            'GetFirstChildElement',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'first'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetLastChildElement')],
                            HRESULT,
                            'GetLastChildElement',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'last'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNextSiblingElement')],
                            HRESULT,
                            'GetNextSiblingElement',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'next'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPreviousSiblingElement')],
                            HRESULT,
                            'GetPreviousSiblingElement',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'previous'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method NormalizeElement')],
                            HRESULT,
                            'NormalizeElement',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'normalized'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetParentElementBuildCache')],
                            HRESULT,
                            'GetParentElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'parent'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFirstChildElementBuildCache')],
                            HRESULT,
                            'GetFirstChildElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'first'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetLastChildElementBuildCache')],
                            HRESULT,
                            'GetLastChildElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'last'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetNextSiblingElementBuildCache')],
                            HRESULT,
                            'GetNextSiblingElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'next'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPreviousSiblingElementBuildCache')],
                            HRESULT,
                            'GetPreviousSiblingElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'previous'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method NormalizeElementBuildCache')],
                            HRESULT,
                            'NormalizeElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'normalized'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Condition'), 'propget', 'in'],
                            HRESULT,
                            'Condition',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'condition'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTreeWalker_INTERFACE_DEFINED__

            if not defined(__IUIAutomationEventHandler_INTERFACE_DEFINED__):
                __IUIAutomationEventHandler_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationEventHandler
                # [oleautomation][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationEventHandler = MIDL_INTERFACE(
                        "{146C3C17-F12E-4E22-8C27-F894B9B79C69}"
                    )
                    IUIAutomationEventHandler._iid_ = IID_IUIAutomationEventHandler


                    IUIAutomationEventHandler._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandleAutomationEvent')],
                            HRESULT,
                            'HandleAutomationEvent',
                            (['in'], POINTER(IUIAutomationElement), 'sender'),
                            (['in'], EVENTID, 'eventId'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationEventHandler_INTERFACE_DEFINED__

            if not defined(__IUIAutomationPropertyChangedEventHandler_INTERFACE_DEFINED__):
                __IUIAutomationPropertyChangedEventHandler_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationPropertyChangedEventHandler
                # [oleautomation][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationPropertyChangedEventHandler = MIDL_INTERFACE(
                        "{40CD37D4-C756-4B0C-8C6F-BDDFEEB13B50}"
                    )
                    IUIAutomationPropertyChangedEventHandler._iid_ = IID_IUIAutomationPropertyChangedEventHandler


                    IUIAutomationPropertyChangedEventHandler._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandlePropertyChangedEvent')],
                            HRESULT,
                            'HandlePropertyChangedEvent',
                            (['in'], POINTER(IUIAutomationElement), 'sender'),
                            (['in'], PROPERTYID, 'propertyId'),
                            (['in'], VARIANT, 'newValue'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationPropertyChangedEventHandler_INTERFACE_DEFINED__

            if not defined(__IUIAutomationStructureChangedEventHandler_INTERFACE_DEFINED__):
                __IUIAutomationStructureChangedEventHandler_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationStructureChangedEventHandler
                # [oleautomation][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationStructureChangedEventHandler = MIDL_INTERFACE(
                        "{E81D1B4E-11C5-42F8-9754-E7036C79F054}"
                    )
                    IUIAutomationStructureChangedEventHandler._iid_ = IID_IUIAutomationStructureChangedEventHandler


                    IUIAutomationStructureChangedEventHandler._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandleStructureChangedEvent')],
                            HRESULT,
                            'HandleStructureChangedEvent',
                            (['in'], POINTER(IUIAutomationElement), 'sender'),
                            (['in'], StructureChangeType, 'changeType'),
                            (['in'], POINTER(), 'runtimeId'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationStructureChangedEventHandler_INTERFACE_DEFINED__

            if not defined(__IUIAutomationFocusChangedEventHandler_INTERFACE_DEFINED__):
                __IUIAutomationFocusChangedEventHandler_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationFocusChangedEventHandler
                # [oleautomation][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationFocusChangedEventHandler = MIDL_INTERFACE(
                        "{C270F6B5-5C69-4290-9745-7A7F97169468}"
                    )
                    IUIAutomationFocusChangedEventHandler._iid_ = IID_IUIAutomationFocusChangedEventHandler


                    IUIAutomationFocusChangedEventHandler._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandleFocusChangedEvent')],
                            HRESULT,
                            'HandleFocusChangedEvent',
                            (['in'], POINTER(IUIAutomationElement), 'sender'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationFocusChangedEventHandler_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextEditTextChangedEventHandler_INTERFACE_DEFINED__):
                __IUIAutomationTextEditTextChangedEventHandler_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextEditTextChangedEventHandler
                # [oleautomation][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextEditTextChangedEventHandler = MIDL_INTERFACE(
                        "{92FAA680-E704-4156-931A-E32D5BB38F3F}"
                    )
                    IUIAutomationTextEditTextChangedEventHandler._iid_ = IID_IUIAutomationTextEditTextChangedEventHandler


                    IUIAutomationTextEditTextChangedEventHandler._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandleTextEditTextChangedEvent')],
                            HRESULT,
                            'HandleTextEditTextChangedEvent',
                            (['in'], POINTER(IUIAutomationElement), 'sender'),
                            (
                                ['in'],
                                TextEditChangeType,
                                'textEditChangeType'
                            ),
                            (['in'], POINTER(), 'eventStrings'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextEditTextChangedEventHandler_INTERFACE_DEFINED__

            if not defined(__IUIAutomationChangesEventHandler_INTERFACE_DEFINED__):
                __IUIAutomationChangesEventHandler_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationChangesEventHandler
                # [oleautomation][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationChangesEventHandler = MIDL_INTERFACE(
                        "{58EDCA55-2C3E-4980-B1B9-56C17F27A2A0}"
                    )
                    IUIAutomationChangesEventHandler._iid_ = IID_IUIAutomationChangesEventHandler


                    IUIAutomationChangesEventHandler._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandleChangesEvent')],
                            HRESULT,
                            'HandleChangesEvent',
                            (['in'], POINTER(IUIAutomationElement), 'sender'),
                            (['in'], POINTER(UiaChangeInfo), 'uiaChanges'),
                            (['in'], INT, 'changesCount'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationChangesEventHandler_INTERFACE_DEFINED__

            if not defined(__IUIAutomationNotificationEventHandler_INTERFACE_DEFINED__):
                __IUIAutomationNotificationEventHandler_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationNotificationEventHandler
                # [oleautomation][unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationNotificationEventHandler = MIDL_INTERFACE(
                        "{C7CB2637-E6C2-4D0C-85DE-4948C02175C7}"
                    )
                    IUIAutomationNotificationEventHandler._iid_ = IID_IUIAutomationNotificationEventHandler


                    IUIAutomationNotificationEventHandler._methods_ = [
                        COMMETHOD(
                            [helpstring('Method HandleNotificationEvent')],
                            HRESULT,
                            'HandleNotificationEvent',
                            (['in'], POINTER(IUIAutomationElement), 'sender'),
                            ([], NotificationKind, 'notificationKind'),
                            (
                                [],
                                NotificationProcessing,
                                'notificationProcessing'
                            ),
                            (['in'], BSTR, 'displayString'),
                            (['in'], BSTR, 'activityId'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationNotificationEventHandler_INTERFACE_DEFINED__

            if not defined(__IUIAutomationInvokePattern_INTERFACE_DEFINED__):
                __IUIAutomationInvokePattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationInvokePattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationInvokePattern = MIDL_INTERFACE(
                        "{FB377FBE-8EA6-46D5-9C73-6499642D3059}"
                    )
                    IUIAutomationInvokePattern._iid_ = IID_IUIAutomationInvokePattern


                    IUIAutomationInvokePattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Invoke')],
                            HRESULT,
                            'Invoke',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationInvokePattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationDockPattern_INTERFACE_DEFINED__):
                __IUIAutomationDockPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationDockPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationDockPattern = MIDL_INTERFACE(
                        "{FDE5EF97-1464-48F6-90BF-43D0948E86EC}"
                    )
                    IUIAutomationDockPattern._iid_ = IID_IUIAutomationDockPattern


                    IUIAutomationDockPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetDockPosition')],
                            HRESULT,
                            'SetDockPosition',
                            (['in'], DockPosition, 'dockPos'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDockPosition'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDockPosition',
                            (
                                ['retval', 'out'],
                                POINTER(DockPosition),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDockPosition'), 'propget', 'in'],
                            HRESULT,
                            'CachedDockPosition',
                            (
                                ['out', 'retval'],
                                POINTER(DockPosition),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationDockPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationExpandCollapsePattern_INTERFACE_DEFINED__):
                __IUIAutomationExpandCollapsePattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationExpandCollapsePattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationExpandCollapsePattern = MIDL_INTERFACE(
                        "{619BE086-1F4E-4EE4-BAFA-210128738730}"
                    )
                    IUIAutomationExpandCollapsePattern._iid_ = IID_IUIAutomationExpandCollapsePattern


                    IUIAutomationExpandCollapsePattern._methods_ = [
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
                            [helpstring('Method CurrentExpandCollapseState'), 'propget', 'in'],
                            HRESULT,
                            'CurrentExpandCollapseState',
                            (
                                ['out', 'retval'],
                                POINTER(ExpandCollapseState),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedExpandCollapseState'), 'propget', 'in'],
                            HRESULT,
                            'CachedExpandCollapseState',
                            (
                                ['retval', 'out'],
                                POINTER(ExpandCollapseState),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationExpandCollapsePattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationGridPattern_INTERFACE_DEFINED__):
                __IUIAutomationGridPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationGridPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationGridPattern = MIDL_INTERFACE(
                        "{414C3CDC-856B-4F5B-8538-3131C6302550}"
                    )
                    IUIAutomationGridPattern._iid_ = IID_IUIAutomationGridPattern


                    IUIAutomationGridPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetItem')],
                            HRESULT,
                            'GetItem',
                            (['in'], INT, 'row'),
                            (['in'], INT, 'column'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentRowCount'), 'propget', 'in'],
                            HRESULT,
                            'CurrentRowCount',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentColumnCount'), 'propget', 'in'],
                            HRESULT,
                            'CurrentColumnCount',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedRowCount'), 'propget', 'in'],
                            HRESULT,
                            'CachedRowCount',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedColumnCount'), 'propget', 'in'],
                            HRESULT,
                            'CachedColumnCount',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationGridPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationGridItemPattern_INTERFACE_DEFINED__):
                __IUIAutomationGridItemPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationGridItemPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationGridItemPattern = MIDL_INTERFACE(
                        "{78F8EF57-66C3-4E09-BD7C-E79B2004894D}"
                    )
                    IUIAutomationGridItemPattern._iid_ = IID_IUIAutomationGridItemPattern


                    IUIAutomationGridItemPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentContainingGrid'), 'propget', 'in'],
                            HRESULT,
                            'CurrentContainingGrid',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentRow'), 'propget', 'in'],
                            HRESULT,
                            'CurrentRow',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentColumn'), 'propget', 'in'],
                            HRESULT,
                            'CurrentColumn',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentRowSpan'), 'propget', 'in'],
                            HRESULT,
                            'CurrentRowSpan',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentColumnSpan'), 'propget', 'in'],
                            HRESULT,
                            'CurrentColumnSpan',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedContainingGrid'), 'propget', 'in'],
                            HRESULT,
                            'CachedContainingGrid',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedRow'), 'propget', 'in'],
                            HRESULT,
                            'CachedRow',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedColumn'), 'propget', 'in'],
                            HRESULT,
                            'CachedColumn',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedRowSpan'), 'propget', 'in'],
                            HRESULT,
                            'CachedRowSpan',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedColumnSpan'), 'propget', 'in'],
                            HRESULT,
                            'CachedColumnSpan',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationGridItemPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationMultipleViewPattern_INTERFACE_DEFINED__):
                __IUIAutomationMultipleViewPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationMultipleViewPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationMultipleViewPattern = MIDL_INTERFACE(
                        "{8D253C91-1DC5-4BB5-B18F-ADE16FA495E8}"
                    )
                    IUIAutomationMultipleViewPattern._iid_ = IID_IUIAutomationMultipleViewPattern


                    IUIAutomationMultipleViewPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetViewName')],
                            HRESULT,
                            'GetViewName',
                            (['in'], INT, 'view'),
                            (['out', 'retval'], POINTER(BSTR), 'name'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetCurrentView')],
                            HRESULT,
                            'SetCurrentView',
                            (['in'], INT, 'view'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCurrentView'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCurrentView',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentSupportedViews')],
                            HRESULT,
                            'GetCurrentSupportedViews',
                            (['out', 'retval'], POINTER(POINTER()), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCurrentView'), 'propget', 'in'],
                            HRESULT,
                            'CachedCurrentView',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedSupportedViews')],
                            HRESULT,
                            'GetCachedSupportedViews',
                            (['out', 'retval'], POINTER(POINTER()), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationMultipleViewPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationObjectModelPattern_INTERFACE_DEFINED__):
                __IUIAutomationObjectModelPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationObjectModelPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationObjectModelPattern = MIDL_INTERFACE(
                        "{71C284B3-C14D-4D14-981E-19751B0D756D}"
                    )
                    IUIAutomationObjectModelPattern._iid_ = IID_IUIAutomationObjectModelPattern


                    IUIAutomationObjectModelPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetUnderlyingObjectModel')],
                            HRESULT,
                            'GetUnderlyingObjectModel',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationObjectModelPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationRangeValuePattern_INTERFACE_DEFINED__):
                __IUIAutomationRangeValuePattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationRangeValuePattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationRangeValuePattern = MIDL_INTERFACE(
                        "{59213F4F-7346-49E5-B120-80555987A148}"
                    )
                    IUIAutomationRangeValuePattern._iid_ = IID_IUIAutomationRangeValuePattern


                    IUIAutomationRangeValuePattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetValue')],
                            HRESULT,
                            'SetValue',
                            (['in'], DOUBLE, 'val'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentValue'), 'propget', 'in'],
                            HRESULT,
                            'CurrentValue',
                            (['out', 'retval'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsReadOnly'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsReadOnly',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentMaximum'), 'propget', 'in'],
                            HRESULT,
                            'CurrentMaximum',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentMinimum'), 'propget', 'in'],
                            HRESULT,
                            'CurrentMinimum',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentLargeChange'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLargeChange',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentSmallChange'), 'propget', 'in'],
                            HRESULT,
                            'CurrentSmallChange',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedValue'), 'propget', 'in'],
                            HRESULT,
                            'CachedValue',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsReadOnly'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsReadOnly',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedMaximum'), 'propget', 'in'],
                            HRESULT,
                            'CachedMaximum',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedMinimum'), 'propget', 'in'],
                            HRESULT,
                            'CachedMinimum',
                            (['out', 'retval'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLargeChange'), 'propget', 'in'],
                            HRESULT,
                            'CachedLargeChange',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedSmallChange'), 'propget', 'in'],
                            HRESULT,
                            'CachedSmallChange',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationRangeValuePattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationScrollPattern_INTERFACE_DEFINED__):
                __IUIAutomationScrollPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationScrollPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationScrollPattern = MIDL_INTERFACE(
                        "{88F4D42A-E881-459D-A77C-73BBBB7E02DC}"
                    )
                    IUIAutomationScrollPattern._iid_ = IID_IUIAutomationScrollPattern


                    IUIAutomationScrollPattern._methods_ = [
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
                            [helpstring('Method CurrentHorizontalScrollPercent'), 'propget', 'in'],
                            HRESULT,
                            'CurrentHorizontalScrollPercent',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentVerticalScrollPercent'), 'propget', 'in'],
                            HRESULT,
                            'CurrentVerticalScrollPercent',
                            (['out', 'retval'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentHorizontalViewSize'), 'propget', 'in'],
                            HRESULT,
                            'CurrentHorizontalViewSize',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentVerticalViewSize'), 'propget', 'in'],
                            HRESULT,
                            'CurrentVerticalViewSize',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentHorizontallyScrollable'), 'propget', 'in'],
                            HRESULT,
                            'CurrentHorizontallyScrollable',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentVerticallyScrollable'), 'propget', 'in'],
                            HRESULT,
                            'CurrentVerticallyScrollable',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedHorizontalScrollPercent'), 'propget', 'in'],
                            HRESULT,
                            'CachedHorizontalScrollPercent',
                            (['out', 'retval'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedVerticalScrollPercent'), 'propget', 'in'],
                            HRESULT,
                            'CachedVerticalScrollPercent',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedHorizontalViewSize'), 'propget', 'in'],
                            HRESULT,
                            'CachedHorizontalViewSize',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedVerticalViewSize'), 'propget', 'in'],
                            HRESULT,
                            'CachedVerticalViewSize',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedHorizontallyScrollable'), 'propget', 'in'],
                            HRESULT,
                            'CachedHorizontallyScrollable',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedVerticallyScrollable'), 'propget', 'in'],
                            HRESULT,
                            'CachedVerticallyScrollable',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationScrollPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationScrollItemPattern_INTERFACE_DEFINED__):
                __IUIAutomationScrollItemPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationScrollItemPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationScrollItemPattern = MIDL_INTERFACE(
                        "{B488300F-D015-4F19-9C29-BB595E3645EF}"
                    )
                    IUIAutomationScrollItemPattern._iid_ = IID_IUIAutomationScrollItemPattern


                    IUIAutomationScrollItemPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ScrollIntoView')],
                            HRESULT,
                            'ScrollIntoView',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationScrollItemPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationSelectionPattern_INTERFACE_DEFINED__):
                __IUIAutomationSelectionPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationSelectionPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationSelectionPattern = MIDL_INTERFACE(
                        "{5ED5202E-B2AC-47A6-B638-4B0BF140D78E}"
                    )
                    IUIAutomationSelectionPattern._iid_ = IID_IUIAutomationSelectionPattern


                    IUIAutomationSelectionPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCurrentSelection')],
                            HRESULT,
                            'GetCurrentSelection',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCanSelectMultiple'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCanSelectMultiple',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsSelectionRequired'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsSelectionRequired',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedSelection')],
                            HRESULT,
                            'GetCachedSelection',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCanSelectMultiple'), 'propget', 'in'],
                            HRESULT,
                            'CachedCanSelectMultiple',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsSelectionRequired'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsSelectionRequired',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationSelectionPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationSelectionPattern2_INTERFACE_DEFINED__):
                __IUIAutomationSelectionPattern2_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationSelectionPattern2
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationSelectionPattern2 = MIDL_INTERFACE(
                        "{0532BFAE-C011-4E32-A343-6D642D798555}"
                    )
                    IUIAutomationSelectionPattern2._iid_ = IID_IUIAutomationSelectionPattern2


                    IUIAutomationSelectionPattern2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentFirstSelectedItem'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFirstSelectedItem',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentLastSelectedItem'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLastSelectedItem',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCurrentSelectedItem'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCurrentSelectedItem',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentItemCount'), 'propget', 'in'],
                            HRESULT,
                            'CurrentItemCount',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFirstSelectedItem'), 'propget', 'in'],
                            HRESULT,
                            'CachedFirstSelectedItem',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLastSelectedItem'), 'propget', 'in'],
                            HRESULT,
                            'CachedLastSelectedItem',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCurrentSelectedItem'), 'propget', 'in'],
                            HRESULT,
                            'CachedCurrentSelectedItem',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedItemCount'), 'propget', 'in'],
                            HRESULT,
                            'CachedItemCount',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationSelectionPattern2_INTERFACE_DEFINED__

            if not defined(__IUIAutomationSelectionItemPattern_INTERFACE_DEFINED__):
                __IUIAutomationSelectionItemPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationSelectionItemPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationSelectionItemPattern = MIDL_INTERFACE(
                        "{A8EFA66A-0FDA-421A-9194-38021F3578EA}"
                    )
                    IUIAutomationSelectionItemPattern._iid_ = IID_IUIAutomationSelectionItemPattern


                    IUIAutomationSelectionItemPattern._methods_ = [
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
                            [helpstring('Method CurrentIsSelected'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsSelected',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentSelectionContainer'), 'propget', 'in'],
                            HRESULT,
                            'CurrentSelectionContainer',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsSelected'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsSelected',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedSelectionContainer'), 'propget', 'in'],
                            HRESULT,
                            'CachedSelectionContainer',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationSelectionItemPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationSynchronizedInputPattern_INTERFACE_DEFINED__):
                __IUIAutomationSynchronizedInputPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationSynchronizedInputPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationSynchronizedInputPattern = MIDL_INTERFACE(
                        "{2233BE0B-AFB7-448B-9FDA-3B378AA5EAE1}"
                    )
                    IUIAutomationSynchronizedInputPattern._iid_ = IID_IUIAutomationSynchronizedInputPattern


                    IUIAutomationSynchronizedInputPattern._methods_ = [
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
            # END IF  __IUIAutomationSynchronizedInputPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTablePattern_INTERFACE_DEFINED__):
                __IUIAutomationTablePattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTablePattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTablePattern = MIDL_INTERFACE(
                        "{620E691C-EA96-4710-A850-754B24CE2417}"
                    )
                    IUIAutomationTablePattern._iid_ = IID_IUIAutomationTablePattern


                    IUIAutomationTablePattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCurrentRowHeaders')],
                            HRESULT,
                            'GetCurrentRowHeaders',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentColumnHeaders')],
                            HRESULT,
                            'GetCurrentColumnHeaders',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentRowOrColumnMajor'), 'propget', 'in'],
                            HRESULT,
                            'CurrentRowOrColumnMajor',
                            (
                                ['out', 'retval'],
                                POINTER(RowOrColumnMajor),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedRowHeaders')],
                            HRESULT,
                            'GetCachedRowHeaders',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedColumnHeaders')],
                            HRESULT,
                            'GetCachedColumnHeaders',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedRowOrColumnMajor'), 'propget', 'in'],
                            HRESULT,
                            'CachedRowOrColumnMajor',
                            (
                                ['out', 'retval'],
                                POINTER(RowOrColumnMajor),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTablePattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTableItemPattern_INTERFACE_DEFINED__):
                __IUIAutomationTableItemPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTableItemPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTableItemPattern = MIDL_INTERFACE(
                        "{0B964EB3-EF2E-4464-9C79-61D61737A27E}"
                    )
                    IUIAutomationTableItemPattern._iid_ = IID_IUIAutomationTableItemPattern


                    IUIAutomationTableItemPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetCurrentRowHeaderItems')],
                            HRESULT,
                            'GetCurrentRowHeaderItems',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentColumnHeaderItems')],
                            HRESULT,
                            'GetCurrentColumnHeaderItems',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedRowHeaderItems')],
                            HRESULT,
                            'GetCachedRowHeaderItems',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedColumnHeaderItems')],
                            HRESULT,
                            'GetCachedColumnHeaderItems',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTableItemPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTogglePattern_INTERFACE_DEFINED__):
                __IUIAutomationTogglePattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTogglePattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTogglePattern = MIDL_INTERFACE(
                        "{94CF8058-9B8D-4AB9-8BFD-4CD0A33C8C70}"
                    )
                    IUIAutomationTogglePattern._iid_ = IID_IUIAutomationTogglePattern


                    IUIAutomationTogglePattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Toggle')],
                            HRESULT,
                            'Toggle',
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentToggleState'), 'propget', 'in'],
                            HRESULT,
                            'CurrentToggleState',
                            (
                                ['retval', 'out'],
                                POINTER(ToggleState),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedToggleState'), 'propget', 'in'],
                            HRESULT,
                            'CachedToggleState',
                            (
                                ['retval', 'out'],
                                POINTER(ToggleState),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTogglePattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTransformPattern_INTERFACE_DEFINED__):
                __IUIAutomationTransformPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTransformPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTransformPattern = MIDL_INTERFACE(
                        "{A9B55844-A55D-4EF0-926D-569C16FF89BB}"
                    )
                    IUIAutomationTransformPattern._iid_ = IID_IUIAutomationTransformPattern


                    IUIAutomationTransformPattern._methods_ = [
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
                            [helpstring('Method CurrentCanMove'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCanMove',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCanResize'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCanResize',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCanRotate'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCanRotate',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCanMove'), 'propget', 'in'],
                            HRESULT,
                            'CachedCanMove',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCanResize'), 'propget', 'in'],
                            HRESULT,
                            'CachedCanResize',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCanRotate'), 'propget', 'in'],
                            HRESULT,
                            'CachedCanRotate',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTransformPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationValuePattern_INTERFACE_DEFINED__):
                __IUIAutomationValuePattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationValuePattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationValuePattern = MIDL_INTERFACE(
                        "{A94CD8B1-0844-4CD6-9D2D-640537AB39E9}"
                    )
                    IUIAutomationValuePattern._iid_ = IID_IUIAutomationValuePattern


                    IUIAutomationValuePattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method SetValue')],
                            HRESULT,
                            'SetValue',
                            (['in'], BSTR, 'val'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentValue'), 'propget', 'in'],
                            HRESULT,
                            'CurrentValue',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsReadOnly'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsReadOnly',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedValue'), 'propget', 'in'],
                            HRESULT,
                            'CachedValue',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsReadOnly'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsReadOnly',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationValuePattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationWindowPattern_INTERFACE_DEFINED__):
                __IUIAutomationWindowPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationWindowPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationWindowPattern = MIDL_INTERFACE(
                        "{0FAEF453-9208-43EF-BBB2-3B485177864F}"
                    )
                    IUIAutomationWindowPattern._iid_ = IID_IUIAutomationWindowPattern


                    IUIAutomationWindowPattern._methods_ = [
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
                            (['out', 'retval'], POINTER(BOOL), 'success'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetWindowVisualState')],
                            HRESULT,
                            'SetWindowVisualState',
                            (['in'], WindowVisualState, 'state'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCanMaximize'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCanMaximize',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCanMinimize'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCanMinimize',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsModal'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsModal',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsTopmost'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsTopmost',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentWindowVisualState'), 'propget', 'in'],
                            HRESULT,
                            'CurrentWindowVisualState',
                            (
                                ['retval', 'out'],
                                POINTER(WindowVisualState),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentWindowInteractionState'), 'propget', 'in'],
                            HRESULT,
                            'CurrentWindowInteractionState',
                            (
                                ['retval', 'out'],
                                POINTER(WindowInteractionState),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCanMaximize'), 'propget', 'in'],
                            HRESULT,
                            'CachedCanMaximize',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCanMinimize'), 'propget', 'in'],
                            HRESULT,
                            'CachedCanMinimize',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsModal'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsModal',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsTopmost'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsTopmost',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedWindowVisualState'), 'propget', 'in'],
                            HRESULT,
                            'CachedWindowVisualState',
                            (
                                ['retval', 'out'],
                                POINTER(WindowVisualState),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedWindowInteractionState'), 'propget', 'in'],
                            HRESULT,
                            'CachedWindowInteractionState',
                            (
                                ['out', 'retval'],
                                POINTER(WindowInteractionState),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationWindowPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextRange_INTERFACE_DEFINED__):
                __IUIAutomationTextRange_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextRange
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextRange = MIDL_INTERFACE(
                        "{A543CC6A-F4AE-494B-8239-C814481187A8}"
                    )
                    IUIAutomationTextRange._iid_ = IID_IUIAutomationTextRange


                    IUIAutomationTextRange._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Clone')],
                            HRESULT,
                            'Clone',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'clonedRange'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method Compare')],
                            HRESULT,
                            'Compare',
                            (
                                ['in'],
                                POINTER(IUIAutomationTextRange),
                                'range'
                            ),
                            (['retval', 'out'], POINTER(BOOL), 'areSame'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CompareEndpoints')],
                            HRESULT,
                            'CompareEndpoints',
                            (['in'], TextPatternRangeEndpoint, 'srcEndPoint'),
                            (
                                ['in'],
                                POINTER(IUIAutomationTextRange),
                                'range'
                            ),
                            (
                                ['in'],
                                TextPatternRangeEndpoint,
                                'targetEndPoint'
                            ),
                            (['out', 'retval'], POINTER(INT), 'compValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ExpandToEnclosingUnit')],
                            HRESULT,
                            'ExpandToEnclosingUnit',
                            (['in'], TextUnit, 'textUnit'),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindAttribute')],
                            HRESULT,
                            'FindAttribute',
                            (['in'], TEXTATTRIBUTEID, 'attr'),
                            (['in'], VARIANT, 'val'),
                            (['in'], BOOL, 'backward'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'found'
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
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAttributeValue')],
                            HRESULT,
                            'GetAttributeValue',
                            (['in'], TEXTATTRIBUTEID, 'attr'),
                            (['retval', 'out'], POINTER(VARIANT), 'value'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetBoundingRectangles')],
                            HRESULT,
                            'GetBoundingRectangles',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER()),
                                'boundingRects'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetEnclosingElement')],
                            HRESULT,
                            'GetEnclosingElement',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'enclosingElement'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetText')],
                            HRESULT,
                            'GetText',
                            (['in'], INT, 'maxLength'),
                            (['retval', 'out'], POINTER(BSTR), 'text'),
                        ),
                        COMMETHOD(
                            [helpstring('Method Move')],
                            HRESULT,
                            'Move',
                            (['in'], TextUnit, 'unit'),
                            (['in'], INT, 'count'),
                            (['out', 'retval'], POINTER(INT), 'moved'),
                        ),
                        COMMETHOD(
                            [helpstring('Method MoveEndpointByUnit')],
                            HRESULT,
                            'MoveEndpointByUnit',
                            (['in'], TextPatternRangeEndpoint, 'endpoint'),
                            (['in'], TextUnit, 'unit'),
                            (['in'], INT, 'count'),
                            (['out', 'retval'], POINTER(INT), 'moved'),
                        ),
                        COMMETHOD(
                            [helpstring('Method MoveEndpointByRange')],
                            HRESULT,
                            'MoveEndpointByRange',
                            (['in'], TextPatternRangeEndpoint, 'srcEndPoint'),
                            (
                                ['in'],
                                POINTER(IUIAutomationTextRange),
                                'range'
                            ),
                            (
                                ['in'],
                                TextPatternRangeEndpoint,
                                'targetEndPoint'
                            ),
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
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'children'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextRange_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextRange2_INTERFACE_DEFINED__):
                __IUIAutomationTextRange2_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextRange2
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextRange2 = MIDL_INTERFACE(
                        "{BB9B40E0-5E04-46BD-9BE0-4B601B9AFAD4}"
                    )
                    IUIAutomationTextRange2._iid_ = IID_IUIAutomationTextRange2


                    IUIAutomationTextRange2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ShowContextMenu')],
                            HRESULT,
                            'ShowContextMenu',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextRange2_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextRange3_INTERFACE_DEFINED__):
                __IUIAutomationTextRange3_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextRange3
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextRange3 = MIDL_INTERFACE(
                        "{6A315D69-5512-4C2E-85F0-53FCE6DD4BC2}"
                    )
                    IUIAutomationTextRange3._iid_ = IID_IUIAutomationTextRange3


                    IUIAutomationTextRange3._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetEnclosingElementBuildCache')],
                            HRESULT,
                            'GetEnclosingElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'enclosingElement'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetChildrenBuildCache')],
                            HRESULT,
                            'GetChildrenBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'children'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetAttributeValues')],
                            HRESULT,
                            'GetAttributeValues',
                            (
                                ['in'],
                                POINTER(TEXTATTRIBUTEID),
                                'attributeIds'
                            ),
                            (['in'], INT, 'attributeIdCount'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER()),
                                'attributeValues'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextRange3_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextRangeArray_INTERFACE_DEFINED__):
                __IUIAutomationTextRangeArray_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextRangeArray
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextRangeArray = MIDL_INTERFACE(
                        "{CE4AE76A-E717-4C98-81EA-47371D028EB6}"
                    )
                    IUIAutomationTextRangeArray._iid_ = IID_IUIAutomationTextRangeArray


                    IUIAutomationTextRangeArray._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Length'), 'propget', 'in'],
                            HRESULT,
                            'Length',
                            (['retval', 'out'], POINTER(INT), 'length'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetElement')],
                            HRESULT,
                            'GetElement',
                            (['in'], INT, 'index'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'element'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextRangeArray_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextPattern_INTERFACE_DEFINED__):
                __IUIAutomationTextPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextPattern = MIDL_INTERFACE(
                        "{32EBA289-3583-42C9-9C59-3B6D9A1E9B6A}"
                    )
                    IUIAutomationTextPattern._iid_ = IID_IUIAutomationTextPattern


                    IUIAutomationTextPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method RangeFromPoint')],
                            HRESULT,
                            'RangeFromPoint',
                            (['in'], POINT, 'pt'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RangeFromChild')],
                            HRESULT,
                            'RangeFromChild',
                            (['in'], POINTER(IUIAutomationElement), 'child'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetSelection')],
                            HRESULT,
                            'GetSelection',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTextRangeArray)),
                                'ranges'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetVisibleRanges')],
                            HRESULT,
                            'GetVisibleRanges',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTextRangeArray)),
                                'ranges'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method DocumentRange'), 'propget', 'in'],
                            HRESULT,
                            'DocumentRange',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SupportedTextSelection'), 'propget', 'in'],
                            HRESULT,
                            'SupportedTextSelection',
                            (
                                ['retval', 'out'],
                                POINTER(SupportedTextSelection),
                                'supportedTextSelection'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextPattern2_INTERFACE_DEFINED__):
                __IUIAutomationTextPattern2_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextPattern2
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextPattern2 = MIDL_INTERFACE(
                        "{506A921A-FCC9-409F-B23B-37EB74106872}"
                    )
                    IUIAutomationTextPattern2._iid_ = IID_IUIAutomationTextPattern2


                    IUIAutomationTextPattern2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method RangeFromAnnotation')],
                            HRESULT,
                            'RangeFromAnnotation',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'annotation'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCaretRange')],
                            HRESULT,
                            'GetCaretRange',
                            (['out'], POINTER(BOOL), 'isActive'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextPattern2_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextEditPattern_INTERFACE_DEFINED__):
                __IUIAutomationTextEditPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextEditPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextEditPattern = MIDL_INTERFACE(
                        "{17E21576-996C-4870-99D9-BFF323380C06}"
                    )
                    IUIAutomationTextEditPattern._iid_ = IID_IUIAutomationTextEditPattern


                    IUIAutomationTextEditPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetActiveComposition')],
                            HRESULT,
                            'GetActiveComposition',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetConversionTarget')],
                            HRESULT,
                            'GetConversionTarget',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextEditPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationCustomNavigationPattern_INTERFACE_DEFINED__):
                __IUIAutomationCustomNavigationPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationCustomNavigationPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationCustomNavigationPattern = MIDL_INTERFACE(
                        "{01EA217A-1766-47ED-A6CC-ACF492854B1F}"
                    )
                    IUIAutomationCustomNavigationPattern._iid_ = IID_IUIAutomationCustomNavigationPattern


                    IUIAutomationCustomNavigationPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Navigate')],
                            HRESULT,
                            'Navigate',
                            (['in'], NavigateDirection, 'direction'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'pRetVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationCustomNavigationPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationLegacyIAccessiblePattern_INTERFACE_DEFINED__):
                __IUIAutomationLegacyIAccessiblePattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationLegacyIAccessiblePattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationLegacyIAccessiblePattern = MIDL_INTERFACE(
                        "{828055AD-355B-4435-86D5-3B51C14A9B1B}"
                    )
                    IUIAutomationLegacyIAccessiblePattern._iid_ = IID_IUIAutomationLegacyIAccessiblePattern


                    IUIAutomationLegacyIAccessiblePattern._methods_ = [
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
                            [helpstring('Method CurrentChildId'), 'propget', 'in'],
                            HRESULT,
                            'CurrentChildId',
                            (['out', 'retval'], POINTER(INT), 'pRetVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentName'), 'propget', 'in'],
                            HRESULT,
                            'CurrentName',
                            (['out', 'retval'], POINTER(BSTR), 'pszName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentValue'), 'propget', 'in'],
                            HRESULT,
                            'CurrentValue',
                            (['retval', 'out'], POINTER(BSTR), 'pszValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDescription'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDescription',
                            (
                                ['out', 'retval'],
                                POINTER(BSTR),
                                'pszDescription'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentRole'), 'propget', 'in'],
                            HRESULT,
                            'CurrentRole',
                            (['out', 'retval'], POINTER(DWORD), 'pdwRole'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentState'), 'propget', 'in'],
                            HRESULT,
                            'CurrentState',
                            (['out', 'retval'], POINTER(DWORD), 'pdwState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentHelp'), 'propget', 'in'],
                            HRESULT,
                            'CurrentHelp',
                            (['retval', 'out'], POINTER(BSTR), 'pszHelp'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentKeyboardShortcut'), 'propget', 'in'],
                            HRESULT,
                            'CurrentKeyboardShortcut',
                            (
                                ['out', 'retval'],
                                POINTER(BSTR),
                                'pszKeyboardShortcut'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentSelection')],
                            HRESULT,
                            'GetCurrentSelection',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'pvarSelectedChildren'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDefaultAction'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDefaultAction',
                            (
                                ['retval', 'out'],
                                POINTER(BSTR),
                                'pszDefaultAction'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedChildId'), 'propget', 'in'],
                            HRESULT,
                            'CachedChildId',
                            (['out', 'retval'], POINTER(INT), 'pRetVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedName'), 'propget', 'in'],
                            HRESULT,
                            'CachedName',
                            (['out', 'retval'], POINTER(BSTR), 'pszName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedValue'), 'propget', 'in'],
                            HRESULT,
                            'CachedValue',
                            (['retval', 'out'], POINTER(BSTR), 'pszValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDescription'), 'propget', 'in'],
                            HRESULT,
                            'CachedDescription',
                            (
                                ['retval', 'out'],
                                POINTER(BSTR),
                                'pszDescription'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedRole'), 'propget', 'in'],
                            HRESULT,
                            'CachedRole',
                            (['retval', 'out'], POINTER(DWORD), 'pdwRole'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedState'), 'propget', 'in'],
                            HRESULT,
                            'CachedState',
                            (['retval', 'out'], POINTER(DWORD), 'pdwState'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedHelp'), 'propget', 'in'],
                            HRESULT,
                            'CachedHelp',
                            (['out', 'retval'], POINTER(BSTR), 'pszHelp'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedKeyboardShortcut'), 'propget', 'in'],
                            HRESULT,
                            'CachedKeyboardShortcut',
                            (
                                ['out', 'retval'],
                                POINTER(BSTR),
                                'pszKeyboardShortcut'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedSelection')],
                            HRESULT,
                            'GetCachedSelection',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'pvarSelectedChildren'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDefaultAction'), 'propget', 'in'],
                            HRESULT,
                            'CachedDefaultAction',
                            (
                                ['retval', 'out'],
                                POINTER(BSTR),
                                'pszDefaultAction'
                            ),
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
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationLegacyIAccessiblePattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationItemContainerPattern_INTERFACE_DEFINED__):
                __IUIAutomationItemContainerPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationItemContainerPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationItemContainerPattern = MIDL_INTERFACE(
                        "{C690FDB2-27A8-423C-812D-429773C9084E}"
                    )
                    IUIAutomationItemContainerPattern._iid_ = IID_IUIAutomationItemContainerPattern


                    IUIAutomationItemContainerPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method FindItemByProperty')],
                            HRESULT,
                            'FindItemByProperty',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'pStartAfter'
                            ),
                            (['in'], PROPERTYID, 'propertyId'),
                            (['in'], VARIANT, 'value'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'pFound'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationItemContainerPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationVirtualizedItemPattern_INTERFACE_DEFINED__):
                __IUIAutomationVirtualizedItemPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationVirtualizedItemPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationVirtualizedItemPattern = MIDL_INTERFACE(
                        "{6BA3D7A6-04CF-4F11-8793-A8D1CDE9969F}"
                    )
                    IUIAutomationVirtualizedItemPattern._iid_ = IID_IUIAutomationVirtualizedItemPattern


                    IUIAutomationVirtualizedItemPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Realize')],
                            HRESULT,
                            'Realize',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationVirtualizedItemPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationAnnotationPattern_INTERFACE_DEFINED__):
                __IUIAutomationAnnotationPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationAnnotationPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationAnnotationPattern = MIDL_INTERFACE(
                        "{9A175B21-339E-41B1-8E8B-623F6B681098}"
                    )
                    IUIAutomationAnnotationPattern._iid_ = IID_IUIAutomationAnnotationPattern


                    IUIAutomationAnnotationPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentAnnotationTypeId'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAnnotationTypeId',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAnnotationTypeName'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAnnotationTypeName',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAuthor'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAuthor',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDateTime'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDateTime',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentTarget'), 'propget', 'in'],
                            HRESULT,
                            'CurrentTarget',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAnnotationTypeId'), 'propget', 'in'],
                            HRESULT,
                            'CachedAnnotationTypeId',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAnnotationTypeName'), 'propget', 'in'],
                            HRESULT,
                            'CachedAnnotationTypeName',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAuthor'), 'propget', 'in'],
                            HRESULT,
                            'CachedAuthor',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDateTime'), 'propget', 'in'],
                            HRESULT,
                            'CachedDateTime',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedTarget'), 'propget', 'in'],
                            HRESULT,
                            'CachedTarget',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationAnnotationPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationStylesPattern_INTERFACE_DEFINED__):
                __IUIAutomationStylesPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationStylesPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationStylesPattern = MIDL_INTERFACE(
                        "{85B5F0A2-BD79-484A-AD2B-388C9838D5FB}"
                    )
                    IUIAutomationStylesPattern._iid_ = IID_IUIAutomationStylesPattern


                    IUIAutomationStylesPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentStyleId'), 'propget', 'in'],
                            HRESULT,
                            'CurrentStyleId',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentStyleName'), 'propget', 'in'],
                            HRESULT,
                            'CurrentStyleName',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentFillColor'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFillColor',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentFillPatternStyle'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFillPatternStyle',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentShape'), 'propget', 'in'],
                            HRESULT,
                            'CurrentShape',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentFillPatternColor'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFillPatternColor',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentExtendedProperties'), 'propget', 'in'],
                            HRESULT,
                            'CurrentExtendedProperties',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentExtendedPropertiesAsArray')],
                            HRESULT,
                            'GetCurrentExtendedPropertiesAsArray',
                            (
                                ['out'],
                                POINTER(POINTER(ExtendedProperty)),
                                'propertyArray'
                            ),
                            (['out'], POINTER(INT), 'propertyCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedStyleId'), 'propget', 'in'],
                            HRESULT,
                            'CachedStyleId',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedStyleName'), 'propget', 'in'],
                            HRESULT,
                            'CachedStyleName',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFillColor'), 'propget', 'in'],
                            HRESULT,
                            'CachedFillColor',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFillPatternStyle'), 'propget', 'in'],
                            HRESULT,
                            'CachedFillPatternStyle',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedShape'), 'propget', 'in'],
                            HRESULT,
                            'CachedShape',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFillPatternColor'), 'propget', 'in'],
                            HRESULT,
                            'CachedFillPatternColor',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedExtendedProperties'), 'propget', 'in'],
                            HRESULT,
                            'CachedExtendedProperties',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedExtendedPropertiesAsArray')],
                            HRESULT,
                            'GetCachedExtendedPropertiesAsArray',
                            (
                                ['out'],
                                POINTER(POINTER(ExtendedProperty)),
                                'propertyArray'
                            ),
                            (['out'], POINTER(INT), 'propertyCount'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationStylesPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationSpreadsheetPattern_INTERFACE_DEFINED__):
                __IUIAutomationSpreadsheetPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationSpreadsheetPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationSpreadsheetPattern = MIDL_INTERFACE(
                        "{7517A7C8-FAAE-4DE9-9F08-29B91E8595C1}"
                    )
                    IUIAutomationSpreadsheetPattern._iid_ = IID_IUIAutomationSpreadsheetPattern


                    IUIAutomationSpreadsheetPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method GetItemByName')],
                            HRESULT,
                            'GetItemByName',
                            (['in'], BSTR, 'name'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationSpreadsheetPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationSpreadsheetItemPattern_INTERFACE_DEFINED__):
                __IUIAutomationSpreadsheetItemPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationSpreadsheetItemPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationSpreadsheetItemPattern = MIDL_INTERFACE(
                        "{7D4FB86C-8D34-40E1-8E83-62C15204E335}"
                    )
                    IUIAutomationSpreadsheetItemPattern._iid_ = IID_IUIAutomationSpreadsheetItemPattern


                    IUIAutomationSpreadsheetItemPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentFormula'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFormula',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentAnnotationObjects')],
                            HRESULT,
                            'GetCurrentAnnotationObjects',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentAnnotationTypes')],
                            HRESULT,
                            'GetCurrentAnnotationTypes',
                            (['out', 'retval'], POINTER(POINTER()), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFormula'), 'propget', 'in'],
                            HRESULT,
                            'CachedFormula',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedAnnotationObjects')],
                            HRESULT,
                            'GetCachedAnnotationObjects',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedAnnotationTypes')],
                            HRESULT,
                            'GetCachedAnnotationTypes',
                            (['out', 'retval'], POINTER(POINTER()), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationSpreadsheetItemPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTransformPattern2_INTERFACE_DEFINED__):
                __IUIAutomationTransformPattern2_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTransformPattern2
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTransformPattern2 = MIDL_INTERFACE(
                        "{6D74D017-6ECB-4381-B38B-3C17A48FF1C2}"
                    )
                    IUIAutomationTransformPattern2._iid_ = IID_IUIAutomationTransformPattern2


                    IUIAutomationTransformPattern2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Zoom')],
                            HRESULT,
                            'Zoom',
                            (['in'], DOUBLE, 'zoomValue'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ZoomByUnit')],
                            HRESULT,
                            'ZoomByUnit',
                            (['in'], ZoomUnit, 'zoomUnit'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentCanZoom'), 'propget', 'in'],
                            HRESULT,
                            'CurrentCanZoom',
                            (['retval', 'out'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedCanZoom'), 'propget', 'in'],
                            HRESULT,
                            'CachedCanZoom',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentZoomLevel'), 'propget', 'in'],
                            HRESULT,
                            'CurrentZoomLevel',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedZoomLevel'), 'propget', 'in'],
                            HRESULT,
                            'CachedZoomLevel',
                            (['out', 'retval'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentZoomMinimum'), 'propget', 'in'],
                            HRESULT,
                            'CurrentZoomMinimum',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedZoomMinimum'), 'propget', 'in'],
                            HRESULT,
                            'CachedZoomMinimum',
                            (['out', 'retval'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentZoomMaximum'), 'propget', 'in'],
                            HRESULT,
                            'CurrentZoomMaximum',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedZoomMaximum'), 'propget', 'in'],
                            HRESULT,
                            'CachedZoomMaximum',
                            (['retval', 'out'], POINTER(DOUBLE), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTransformPattern2_INTERFACE_DEFINED__

            if not defined(__IUIAutomationTextChildPattern_INTERFACE_DEFINED__):
                __IUIAutomationTextChildPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationTextChildPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationTextChildPattern = MIDL_INTERFACE(
                        "{6552B038-AE05-40C8-ABFD-AA08352AAB86}"
                    )
                    IUIAutomationTextChildPattern._iid_ = IID_IUIAutomationTextChildPattern


                    IUIAutomationTextChildPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method TextContainer'), 'propget', 'in'],
                            HRESULT,
                            'TextContainer',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'container'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method TextRange'), 'propget', 'in'],
                            HRESULT,
                            'TextRange',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTextRange)),
                                'range'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationTextChildPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationDragPattern_INTERFACE_DEFINED__):
                __IUIAutomationDragPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationDragPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationDragPattern = MIDL_INTERFACE(
                        "{1DC7B570-1F54-4BAD-BCDA-D36A722FB7BD}"
                    )
                    IUIAutomationDragPattern._iid_ = IID_IUIAutomationDragPattern


                    IUIAutomationDragPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentIsGrabbed'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsGrabbed',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsGrabbed'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsGrabbed',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDropEffect'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDropEffect',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDropEffect'), 'propget', 'in'],
                            HRESULT,
                            'CachedDropEffect',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDropEffects'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDropEffects',
                            (['out', 'retval'], POINTER(POINTER()), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDropEffects'), 'propget', 'in'],
                            HRESULT,
                            'CachedDropEffects',
                            (['out', 'retval'], POINTER(POINTER()), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentGrabbedItems')],
                            HRESULT,
                            'GetCurrentGrabbedItems',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCachedGrabbedItems')],
                            HRESULT,
                            'GetCachedGrabbedItems',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationDragPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationDropTargetPattern_INTERFACE_DEFINED__):
                __IUIAutomationDropTargetPattern_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationDropTargetPattern
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationDropTargetPattern = MIDL_INTERFACE(
                        "{69A095F7-EEE4-430E-A46B-FB73B1AE39A5}"
                    )
                    IUIAutomationDropTargetPattern._iid_ = IID_IUIAutomationDropTargetPattern


                    IUIAutomationDropTargetPattern._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentDropTargetEffect'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDropTargetEffect',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDropTargetEffect'), 'propget', 'in'],
                            HRESULT,
                            'CachedDropTargetEffect',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentDropTargetEffects'), 'propget', 'in'],
                            HRESULT,
                            'CurrentDropTargetEffects',
                            (['retval', 'out'], POINTER(POINTER()), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedDropTargetEffects'), 'propget', 'in'],
                            HRESULT,
                            'CachedDropTargetEffects',
                            (['out', 'retval'], POINTER(POINTER()), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationDropTargetPattern_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElement2_INTERFACE_DEFINED__):
                __IUIAutomationElement2_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement2
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement2 = MIDL_INTERFACE(
                        "{6749C683-F70D-4487-A698-5F79D55290D6}"
                    )
                    IUIAutomationElement2._iid_ = IID_IUIAutomationElement2


                    IUIAutomationElement2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentOptimizeForVisualContent'), 'propget', 'in'],
                            HRESULT,
                            'CurrentOptimizeForVisualContent',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedOptimizeForVisualContent'), 'propget', 'in'],
                            HRESULT,
                            'CachedOptimizeForVisualContent',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentLiveSetting'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLiveSetting',
                            (
                                ['retval', 'out'],
                                POINTER(LiveSetting),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLiveSetting'), 'propget', 'in'],
                            HRESULT,
                            'CachedLiveSetting',
                            (
                                ['out', 'retval'],
                                POINTER(LiveSetting),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentFlowsFrom'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFlowsFrom',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFlowsFrom'), 'propget', 'in'],
                            HRESULT,
                            'CachedFlowsFrom',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement2_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElement3_INTERFACE_DEFINED__):
                __IUIAutomationElement3_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement3
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement3 = MIDL_INTERFACE(
                        "{8471DF34-AEE0-4A01-A7DE-7DB9AF12C296}"
                    )
                    IUIAutomationElement3._iid_ = IID_IUIAutomationElement3


                    IUIAutomationElement3._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ShowContextMenu')],
                            HRESULT,
                            'ShowContextMenu',
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentIsPeripheral'), 'propget', 'in'],
                            HRESULT,
                            'CurrentIsPeripheral',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedIsPeripheral'), 'propget', 'in'],
                            HRESULT,
                            'CachedIsPeripheral',
                            (['out', 'retval'], POINTER(BOOL), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement3_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElement4_INTERFACE_DEFINED__):
                __IUIAutomationElement4_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement4
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement4 = MIDL_INTERFACE(
                        "{3B6E233C-52FB-4063-A4C9-77C075C2A06B}"
                    )
                    IUIAutomationElement4._iid_ = IID_IUIAutomationElement4


                    IUIAutomationElement4._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentPositionInSet'), 'propget', 'in'],
                            HRESULT,
                            'CurrentPositionInSet',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentSizeOfSet'), 'propget', 'in'],
                            HRESULT,
                            'CurrentSizeOfSet',
                            (['retval', 'out'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentLevel'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLevel',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAnnotationTypes'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAnnotationTypes',
                            (['retval', 'out'], POINTER(POINTER()), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentAnnotationObjects'), 'propget', 'in'],
                            HRESULT,
                            'CurrentAnnotationObjects',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedPositionInSet'), 'propget', 'in'],
                            HRESULT,
                            'CachedPositionInSet',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedSizeOfSet'), 'propget', 'in'],
                            HRESULT,
                            'CachedSizeOfSet',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLevel'), 'propget', 'in'],
                            HRESULT,
                            'CachedLevel',
                            (['out', 'retval'], POINTER(INT), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAnnotationTypes'), 'propget', 'in'],
                            HRESULT,
                            'CachedAnnotationTypes',
                            (['retval', 'out'], POINTER(POINTER()), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedAnnotationObjects'), 'propget', 'in'],
                            HRESULT,
                            'CachedAnnotationObjects',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement4_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElement5_INTERFACE_DEFINED__):
                __IUIAutomationElement5_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement5
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement5 = MIDL_INTERFACE(
                        "{98141C1D-0D0E-4175-BBE2-6BFF455842A7}"
                    )
                    IUIAutomationElement5._iid_ = IID_IUIAutomationElement5


                    IUIAutomationElement5._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentLandmarkType'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLandmarkType',
                            (
                                ['out', 'retval'],
                                POINTER(LANDMARKTYPEID),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CurrentLocalizedLandmarkType'), 'propget', 'in'],
                            HRESULT,
                            'CurrentLocalizedLandmarkType',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLandmarkType'), 'propget', 'in'],
                            HRESULT,
                            'CachedLandmarkType',
                            (
                                ['out', 'retval'],
                                POINTER(LANDMARKTYPEID),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedLocalizedLandmarkType'), 'propget', 'in'],
                            HRESULT,
                            'CachedLocalizedLandmarkType',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement5_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElement6_INTERFACE_DEFINED__):
                __IUIAutomationElement6_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement6
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement6 = MIDL_INTERFACE(
                        "{4780D450-8BCA-4977-AFA5-A4A517F555E3}"
                    )
                    IUIAutomationElement6._iid_ = IID_IUIAutomationElement6


                    IUIAutomationElement6._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentFullDescription'), 'propget', 'in'],
                            HRESULT,
                            'CurrentFullDescription',
                            (['out', 'retval'], POINTER(BSTR), 'retVal'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedFullDescription'), 'propget', 'in'],
                            HRESULT,
                            'CachedFullDescription',
                            (['retval', 'out'], POINTER(BSTR), 'retVal'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement6_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElement7_INTERFACE_DEFINED__):
                __IUIAutomationElement7_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement7
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement7 = MIDL_INTERFACE(
                        "{204E8572-CFC3-4C11-B0C8-7DA7420750B7}"
                    )
                    IUIAutomationElement7._iid_ = IID_IUIAutomationElement7


                    IUIAutomationElement7._methods_ = [
                        COMMETHOD(
                            [helpstring('Method FindFirstWithOptions')],
                            HRESULT,
                            'FindFirstWithOptions',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['in'],
                                TreeTraversalOptions,
                                'traversalOptions'
                            ),
                            (['in'], POINTER(IUIAutomationElement), 'root'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindAllWithOptions')],
                            HRESULT,
                            'FindAllWithOptions',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['in'],
                                TreeTraversalOptions,
                                'traversalOptions'
                            ),
                            (['in'], POINTER(IUIAutomationElement), 'root'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindFirstWithOptionsBuildCache')],
                            HRESULT,
                            'FindFirstWithOptionsBuildCache',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                TreeTraversalOptions,
                                'traversalOptions'
                            ),
                            (['in'], POINTER(IUIAutomationElement), 'root'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method FindAllWithOptionsBuildCache')],
                            HRESULT,
                            'FindAllWithOptionsBuildCache',
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                TreeTraversalOptions,
                                'traversalOptions'
                            ),
                            (['in'], POINTER(IUIAutomationElement), 'root'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElementArray)),
                                'found'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetCurrentMetadataValue')],
                            HRESULT,
                            'GetCurrentMetadataValue',
                            (['in'], INT, 'targetId'),
                            (['in'], METADATAID, 'metadataId'),
                            (
                                ['out', 'retval'],
                                POINTER(VARIANT),
                                'returnVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement7_INTERFACE_DEFINED__

            if not defined(__IUIAutomationElement8_INTERFACE_DEFINED__):
                __IUIAutomationElement8_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationElement8
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationElement8 = MIDL_INTERFACE(
                        "{8C60217D-5411-4CDE-BCC0-1CEDA223830C}"
                    )
                    IUIAutomationElement8._iid_ = IID_IUIAutomationElement8


                    IUIAutomationElement8._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CurrentHeadingLevel'), 'propget', 'in'],
                            HRESULT,
                            'CurrentHeadingLevel',
                            (
                                ['out', 'retval'],
                                POINTER(HEADINGLEVELID),
                                'retVal'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CachedHeadingLevel'), 'propget', 'in'],
                            HRESULT,
                            'CachedHeadingLevel',
                            (
                                ['retval', 'out'],
                                POINTER(HEADINGLEVELID),
                                'retVal'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationElement8_INTERFACE_DEFINED__

            if not defined(__IUIAutomationProxyFactory_INTERFACE_DEFINED__):
                __IUIAutomationProxyFactory_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationProxyFactory
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationProxyFactory = MIDL_INTERFACE(
                        "{85B94ECD-849D-42B6-B94D-D6DB23FDF5A4}"
                    )
                    IUIAutomationProxyFactory._iid_ = IID_IUIAutomationProxyFactory


                    IUIAutomationProxyFactory._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CreateProvider')],
                            HRESULT,
                            'CreateProvider',
                            (['in'], UIA_HWND, 'hwnd'),
                            (['in'], LONG, 'idObject'),
                            (['in'], LONG, 'idChild'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IRawElementProviderSimple)),
                                'provider'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ProxyFactoryId'), 'propget', 'in'],
                            HRESULT,
                            'ProxyFactoryId',
                            (['retval', 'out'], POINTER(BSTR), 'factoryId'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationProxyFactory_INTERFACE_DEFINED__

            if not defined(__IUIAutomationProxyFactoryEntry_INTERFACE_DEFINED__):
                __IUIAutomationProxyFactoryEntry_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationProxyFactoryEntry
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationProxyFactoryEntry = MIDL_INTERFACE(
                        "{D50E472E-B64B-490C-BCA1-D30696F9F289}"
                    )
                    IUIAutomationProxyFactoryEntry._iid_ = IID_IUIAutomationProxyFactoryEntry


                    IUIAutomationProxyFactoryEntry._methods_ = [
                        COMMETHOD(
                            [helpstring('Method ProxyFactory'), 'propget', 'in'],
                            HRESULT,
                            'ProxyFactory',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationProxyFactory)),
                                'factory'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ClassName'), 'propget', 'in'],
                            HRESULT,
                            'ClassName',
                            (['retval', 'out'], POINTER(BSTR), 'className'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ImageName'), 'propget', 'in'],
                            HRESULT,
                            'ImageName',
                            (['retval', 'out'], POINTER(BSTR), 'imageName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AllowSubstringMatch'), 'propget', 'in'],
                            HRESULT,
                            'AllowSubstringMatch',
                            (
                                ['retval', 'out'],
                                POINTER(BOOL),
                                'allowSubstringMatch'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CanCheckBaseClass'), 'propget', 'in'],
                            HRESULT,
                            'CanCheckBaseClass',
                            (
                                ['retval', 'out'],
                                POINTER(BOOL),
                                'canCheckBaseClass'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method NeedsAdviseEvents'), 'propget', 'in'],
                            HRESULT,
                            'NeedsAdviseEvents',
                            (
                                ['retval', 'out'],
                                POINTER(BOOL),
                                'adviseEvents'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_ClassName'), 'propput', 'in'],
                            HRESULT,
                            'put_ClassName',
                            (['in'], LPCWSTR, 'className'),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_ImageName'), 'propput', 'in'],
                            HRESULT,
                            'put_ImageName',
                            (['in'], LPCWSTR, 'imageName'),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_AllowSubstringMatch'), 'propput', 'in'],
                            HRESULT,
                            'put_AllowSubstringMatch',
                            (['in'], BOOL, 'allowSubstringMatch'),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_CanCheckBaseClass'), 'propput', 'in'],
                            HRESULT,
                            'put_CanCheckBaseClass',
                            (['in'], BOOL, 'canCheckBaseClass'),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_NeedsAdviseEvents'), 'propput', 'in'],
                            HRESULT,
                            'put_NeedsAdviseEvents',
                            (['in'], BOOL, 'adviseEvents'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetWinEventsForAutomationEvent')],
                            HRESULT,
                            'SetWinEventsForAutomationEvent',
                            (['in'], EVENTID, 'eventId'),
                            (['in'], PROPERTYID, 'propertyId'),
                            (['in'], POINTER(), 'winEvents'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetWinEventsForAutomationEvent')],
                            HRESULT,
                            'GetWinEventsForAutomationEvent',
                            (['in'], EVENTID, 'eventId'),
                            (['in'], PROPERTYID, 'propertyId'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER()),
                                'winEvents'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationProxyFactoryEntry_INTERFACE_DEFINED__

            if not defined(__IUIAutomationProxyFactoryMapping_INTERFACE_DEFINED__):
                __IUIAutomationProxyFactoryMapping_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomationProxyFactoryMapping
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomationProxyFactoryMapping = MIDL_INTERFACE(
                        "{09E31E18-872D-4873-93D1-1E541EC133FD}"
                    )
                    IUIAutomationProxyFactoryMapping._iid_ = IID_IUIAutomationProxyFactoryMapping


                    IUIAutomationProxyFactoryMapping._methods_ = [
                        COMMETHOD(
                            [helpstring('Method Count'), 'propget', 'in'],
                            HRESULT,
                            'Count',
                            (['retval', 'out'], POINTER(UINT), 'count'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetTable')],
                            HRESULT,
                            'GetTable',
                            (['out', 'retval'], POINTER(POINTER()), 'table'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetEntry')],
                            HRESULT,
                            'GetEntry',
                            (['in'], UINT, 'index'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationProxyFactoryEntry)),
                                'entry'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method SetTable')],
                            HRESULT,
                            'SetTable',
                            (['in'], POINTER(), 'factoryList'),
                        ),
                        COMMETHOD(
                            [helpstring('Method InsertEntries')],
                            HRESULT,
                            'InsertEntries',
                            (['in'], UINT, 'before'),
                            (['in'], POINTER(), 'factoryList'),
                        ),
                        COMMETHOD(
                            [helpstring('Method InsertEntry')],
                            HRESULT,
                            'InsertEntry',
                            (['in'], UINT, 'before'),
                            (
                                ['in'],
                                POINTER(IUIAutomationProxyFactoryEntry),
                                'factory'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveEntry')],
                            HRESULT,
                            'RemoveEntry',
                            (['in'], UINT, 'index'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ClearTable')],
                            HRESULT,
                            'ClearTable',
                        ),
                        COMMETHOD(
                            [helpstring('Method RestoreDefaultTable')],
                            HRESULT,
                            'RestoreDefaultTable',
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomationProxyFactoryMapping_INTERFACE_DEFINED__

            if not defined(__IUIAutomation_INTERFACE_DEFINED__):
                __IUIAutomation_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomation
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomation = MIDL_INTERFACE(
                        "{30CBE57D-D9D0-452A-AB13-7AC5AC4825EE}"
                    )
                    IUIAutomation._iid_ = IID_IUIAutomation


                    IUIAutomation._methods_ = [
                        COMMETHOD(
                            [helpstring('Method CompareElements')],
                            HRESULT,
                            'CompareElements',
                            (['in'], POINTER(IUIAutomationElement), 'el1'),
                            (['in'], POINTER(IUIAutomationElement), 'el2'),
                            (['retval', 'out'], POINTER(BOOL), 'areSame'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CompareRuntimeIds')],
                            HRESULT,
                            'CompareRuntimeIds',
                            (['in'], POINTER(), 'runtimeId1'),
                            (['in'], POINTER(), 'runtimeId2'),
                            (['out', 'retval'], POINTER(BOOL), 'areSame'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRootElement')],
                            HRESULT,
                            'GetRootElement',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'root'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ElementFromHandle')],
                            HRESULT,
                            'ElementFromHandle',
                            (['in'], UIA_HWND, 'hwnd'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ElementFromPoint')],
                            HRESULT,
                            'ElementFromPoint',
                            (['in'], POINT, 'pt'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFocusedElement')],
                            HRESULT,
                            'GetFocusedElement',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetRootElementBuildCache')],
                            HRESULT,
                            'GetRootElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'root'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ElementFromHandleBuildCache')],
                            HRESULT,
                            'ElementFromHandleBuildCache',
                            (['in'], UIA_HWND, 'hwnd'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ElementFromPointBuildCache')],
                            HRESULT,
                            'ElementFromPointBuildCache',
                            (['in'], POINT, 'pt'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetFocusedElementBuildCache')],
                            HRESULT,
                            'GetFocusedElementBuildCache',
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateTreeWalker')],
                            HRESULT,
                            'CreateTreeWalker',
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'pCondition'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTreeWalker)),
                                'walker'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ControlViewWalker'), 'propget', 'in'],
                            HRESULT,
                            'ControlViewWalker',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationTreeWalker)),
                                'walker'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ContentViewWalker'), 'propget', 'in'],
                            HRESULT,
                            'ContentViewWalker',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTreeWalker)),
                                'walker'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RawViewWalker'), 'propget', 'in'],
                            HRESULT,
                            'RawViewWalker',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationTreeWalker)),
                                'walker'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RawViewCondition'), 'propget', 'in'],
                            HRESULT,
                            'RawViewCondition',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'condition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ControlViewCondition'), 'propget', 'in'],
                            HRESULT,
                            'ControlViewCondition',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'condition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ContentViewCondition'), 'propget', 'in'],
                            HRESULT,
                            'ContentViewCondition',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'condition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateCacheRequest')],
                            HRESULT,
                            'CreateCacheRequest',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCacheRequest)),
                                'cacheRequest'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateTrueCondition')],
                            HRESULT,
                            'CreateTrueCondition',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateFalseCondition')],
                            HRESULT,
                            'CreateFalseCondition',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreatePropertyCondition')],
                            HRESULT,
                            'CreatePropertyCondition',
                            (['in'], PROPERTYID, 'propertyId'),
                            (['in'], VARIANT, 'value'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreatePropertyConditionEx')],
                            HRESULT,
                            'CreatePropertyConditionEx',
                            (['in'], PROPERTYID, 'propertyId'),
                            (['in'], VARIANT, 'value'),
                            (['in'], PropertyConditionFlags, 'flags'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateAndCondition')],
                            HRESULT,
                            'CreateAndCondition',
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition1'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition2'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateAndConditionFromArray')],
                            HRESULT,
                            'CreateAndConditionFromArray',
                            (['in'], POINTER(), 'conditions'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateAndConditionFromNativeArray')],
                            HRESULT,
                            'CreateAndConditionFromNativeArray',
                            (
                                ['in'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'conditions'
                            ),
                            (['in'], INT, 'conditionCount'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateOrCondition')],
                            HRESULT,
                            'CreateOrCondition',
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition1'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition2'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateOrConditionFromArray')],
                            HRESULT,
                            'CreateOrConditionFromArray',
                            (['in'], POINTER(), 'conditions'),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateOrConditionFromNativeArray')],
                            HRESULT,
                            'CreateOrConditionFromNativeArray',
                            (
                                ['in'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'conditions'
                            ),
                            (['in'], INT, 'conditionCount'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateNotCondition')],
                            HRESULT,
                            'CreateNotCondition',
                            (
                                ['in'],
                                POINTER(IUIAutomationCondition),
                                'condition'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationCondition)),
                                'newCondition'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddAutomationEventHandler')],
                            HRESULT,
                            'AddAutomationEventHandler',
                            (['in'], EVENTID, 'eventId'),
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAutomationEventHandler')],
                            HRESULT,
                            'RemoveAutomationEventHandler',
                            (['in'], EVENTID, 'eventId'),
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddPropertyChangedEventHandlerNativeArray')],
                            HRESULT,
                            'AddPropertyChangedEventHandlerNativeArray',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationPropertyChangedEventHandler),
                                'handler'
                            ),
                            (['in'], POINTER(PROPERTYID), 'propertyArray'),
                            (['in'], INT, 'propertyCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddPropertyChangedEventHandler')],
                            HRESULT,
                            'AddPropertyChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationPropertyChangedEventHandler),
                                'handler'
                            ),
                            (['in'], POINTER(), 'propertyArray'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemovePropertyChangedEventHandler')],
                            HRESULT,
                            'RemovePropertyChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationPropertyChangedEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddStructureChangedEventHandler')],
                            HRESULT,
                            'AddStructureChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationStructureChangedEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveStructureChangedEventHandler')],
                            HRESULT,
                            'RemoveStructureChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationStructureChangedEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method AddFocusChangedEventHandler')],
                            HRESULT,
                            'AddFocusChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationFocusChangedEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveFocusChangedEventHandler')],
                            HRESULT,
                            'RemoveFocusChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationFocusChangedEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveAllEventHandlers')],
                            HRESULT,
                            'RemoveAllEventHandlers',
                        ),
                        COMMETHOD(
                            [helpstring('Method IntNativeArrayToSafeArray')],
                            HRESULT,
                            'IntNativeArrayToSafeArray',
                            (['in'], POINTER(INT), 'array'),
                            (['in'], INT, 'arrayCount'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER()),
                                'safeArray'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method IntSafeArrayToNativeArray')],
                            HRESULT,
                            'IntSafeArrayToNativeArray',
                            (['in'], POINTER(), 'intArray'),
                            (['out'], POINTER(POINTER(INT)), 'array'),
                            (['retval', 'out'], POINTER(INT), 'arrayCount'),
                        ),
                        COMMETHOD(
                            [helpstring('Method RectToVariant')],
                            HRESULT,
                            'RectToVariant',
                            (['in'], RECT, 'rc'),
                            (['retval', 'out'], POINTER(VARIANT), 'var'),
                        ),
                        COMMETHOD(
                            [helpstring('Method VariantToRect')],
                            HRESULT,
                            'VariantToRect',
                            (['in'], VARIANT, 'var'),
                            (['out', 'retval'], POINTER(RECT), 'rc'),
                        ),
                        COMMETHOD(
                            [helpstring('Method SafeArrayToRectNativeArray')],
                            HRESULT,
                            'SafeArrayToRectNativeArray',
                            (['in'], POINTER(), 'rects'),
                            (['out'], POINTER(POINTER(RECT)), 'rectArray'),
                            (
                                ['out', 'retval'],
                                POINTER(INT),
                                'rectArrayCount'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method CreateProxyFactoryEntry')],
                            HRESULT,
                            'CreateProxyFactoryEntry',
                            (
                                ['in'],
                                POINTER(IUIAutomationProxyFactory),
                                'factory'
                            ),
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(IUIAutomationProxyFactoryEntry)),
                                'factoryEntry'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ProxyFactoryMapping'), 'propget', 'in'],
                            HRESULT,
                            'ProxyFactoryMapping',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationProxyFactoryMapping)),
                                'factoryMapping'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPropertyProgrammaticName')],
                            HRESULT,
                            'GetPropertyProgrammaticName',
                            (['in'], PROPERTYID, 'property'),
                            (['retval', 'out'], POINTER(BSTR), 'name'),
                        ),
                        COMMETHOD(
                            [helpstring('Method GetPatternProgrammaticName')],
                            HRESULT,
                            'GetPatternProgrammaticName',
                            (['in'], PATTERNID, 'pattern'),
                            (['retval', 'out'], POINTER(BSTR), 'name'),
                        ),
                        COMMETHOD(
                            [helpstring('Method PollForPotentialSupportedPatterns')],
                            HRESULT,
                            'PollForPotentialSupportedPatterns',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'pElement'
                            ),
                            (['out'], POINTER(POINTER()), 'patternIds'),
                            (['out'], POINTER(POINTER()), 'patternNames'),
                        ),
                        COMMETHOD(
                            [helpstring('Method PollForPotentialSupportedProperties')],
                            HRESULT,
                            'PollForPotentialSupportedProperties',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'pElement'
                            ),
                            (['out'], POINTER(POINTER()), 'propertyIds'),
                            (['out'], POINTER(POINTER()), 'propertyNames'),
                        ),
                        COMMETHOD(
                            [helpstring('Method CheckNotSupported')],
                            HRESULT,
                            'CheckNotSupported',
                            (['in'], VARIANT, 'value'),
                            (
                                ['retval', 'out'],
                                POINTER(BOOL),
                                'isNotSupported'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ReservedNotSupportedValue'), 'propget', 'in'],
                            HRESULT,
                            'ReservedNotSupportedValue',
                            (
                                ['out', 'retval'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'notSupportedValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ReservedMixedAttributeValue'), 'propget', 'in'],
                            HRESULT,
                            'ReservedMixedAttributeValue',
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(comtypes.IUnknown)),
                                'mixedAttributeValue'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ElementFromIAccessible')],
                            HRESULT,
                            'ElementFromIAccessible',
                            (['in'], POINTER(IAccessible), 'accessible'),
                            (['in'], INT, 'childId'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method ElementFromIAccessibleBuildCache')],
                            HRESULT,
                            'ElementFromIAccessibleBuildCache',
                            (['in'], POINTER(IAccessible), 'accessible'),
                            (['in'], INT, 'childId'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(IUIAutomationElement)),
                                'element'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomation_INTERFACE_DEFINED__

            if not defined(__IUIAutomation2_INTERFACE_DEFINED__):
                __IUIAutomation2_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomation2
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomation2 = MIDL_INTERFACE(
                        "{34723AFF-0C9D-49D0-9896-7AB52DF8CD8A}"
                    )
                    IUIAutomation2._iid_ = IID_IUIAutomation2


                    IUIAutomation2._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AutoSetFocus'), 'propget', 'in'],
                            HRESULT,
                            'AutoSetFocus',
                            (
                                ['out', 'retval'],
                                POINTER(BOOL),
                                'autoSetFocus'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_AutoSetFocus'), 'propput', 'in'],
                            HRESULT,
                            'put_AutoSetFocus',
                            (['in'], BOOL, 'autoSetFocus'),
                        ),
                        COMMETHOD(
                            [helpstring('Method ConnectionTimeout'), 'propget', 'in'],
                            HRESULT,
                            'ConnectionTimeout',
                            (['retval', 'out'], POINTER(DWORD), 'timeout'),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_ConnectionTimeout'), 'propput', 'in'],
                            HRESULT,
                            'put_ConnectionTimeout',
                            (['in'], DWORD, 'timeout'),
                        ),
                        COMMETHOD(
                            [helpstring('Method TransactionTimeout'), 'propget', 'in'],
                            HRESULT,
                            'TransactionTimeout',
                            (['retval', 'out'], POINTER(DWORD), 'timeout'),
                        ),
                        COMMETHOD(
                            [helpstring('Method put_TransactionTimeout'), 'propput', 'in'],
                            HRESULT,
                            'put_TransactionTimeout',
                            (['in'], DWORD, 'timeout'),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomation2_INTERFACE_DEFINED__

            if not defined(__IUIAutomation3_INTERFACE_DEFINED__):
                __IUIAutomation3_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomation3
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomation3 = MIDL_INTERFACE(
                        "{73D768DA-9B51-4B89-936E-C209290973E7}"
                    )
                    IUIAutomation3._iid_ = IID_IUIAutomation3


                    IUIAutomation3._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddTextEditTextChangedEventHandler')],
                            HRESULT,
                            'AddTextEditTextChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                TextEditChangeType,
                                'textEditChangeType'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationTextEditTextChangedEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveTextEditTextChangedEventHandler')],
                            HRESULT,
                            'RemoveTextEditTextChangedEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationTextEditTextChangedEventHandler),
                                'handler'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomation3_INTERFACE_DEFINED__

            if not defined(__IUIAutomation4_INTERFACE_DEFINED__):
                __IUIAutomation4_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomation4
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomation4 = MIDL_INTERFACE(
                        "{1189C02A-05F8-4319-8E21-E817E3DB2860}"
                    )
                    IUIAutomation4._iid_ = IID_IUIAutomation4


                    IUIAutomation4._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddChangesEventHandler')],
                            HRESULT,
                            'AddChangesEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (['in'], TreeScope, 'scope'),
                            (['in'], POINTER(INT), 'changeTypes'),
                            (['in'], INT, 'changesCount'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'pCacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationChangesEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveChangesEventHandler')],
                            HRESULT,
                            'RemoveChangesEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationChangesEventHandler),
                                'handler'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomation4_INTERFACE_DEFINED__

            if not defined(__IUIAutomation5_INTERFACE_DEFINED__):
                __IUIAutomation5_INTERFACE_DEFINED__ = VOID

                # interface IUIAutomation5
                # [unique][uuid][object]
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else:
                    IID_IUIAutomation5 = MIDL_INTERFACE(
                        "{25F700C8-D816-4057-A9DC-3CBDEE77E256}"
                    )
                    IUIAutomation5._iid_ = IID_IUIAutomation5


                    IUIAutomation5._methods_ = [
                        COMMETHOD(
                            [helpstring('Method AddNotificationEventHandler')],
                            HRESULT,
                            'AddNotificationEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (['in'], TreeScope, 'scope'),
                            (
                                ['in'],
                                POINTER(IUIAutomationCacheRequest),
                                'cacheRequest'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationNotificationEventHandler),
                                'handler'
                            ),
                        ),
                        COMMETHOD(
                            [helpstring('Method RemoveNotificationEventHandler')],
                            HRESULT,
                            'RemoveNotificationEventHandler',
                            (
                                ['in'],
                                POINTER(IUIAutomationElement),
                                'element'
                            ),
                            (
                                ['in'],
                                POINTER(IUIAutomationNotificationEventHandler),
                                'handler'
                            ),
                        ),
                    ]

                # END IF  C style interface
            # END IF  __IUIAutomation5_INTERFACE_DEFINED__

            if defined(__cplusplus):
                pass
            # END IF


            if defined(__cplusplus):
                pass
            # END IF

            LIBID_UIAutomationClient = UUID(
                '{944dE083-8FB8-45CF-BCB7-C477ACB2F897}'
            )

            CLSID_CUIAutomation = DECLSPEC_UUID(
                "{FF48DBA4-60EF-4201-AA87-54103EEF594E}"
            )

            CUIAutomation._reg_clsid_ = CLSID_CUIAutomation
            CUIAutomation._reg_typelib_ = (LIBID_UIAutomationClient, 1, 0)
            CUIAutomation._com_interfaces_ += [IUIAutomation]

            CLSID_CUIAutomation8 = DECLSPEC_UUID(
                "{E22AD333-B25F-460C-83D0-0581107395C9}"
            )

            CUIAutomation8._reg_clsid_ = CLSID_CUIAutomation8
            CUIAutomation8._reg_typelib_ = (LIBID_UIAutomationClient, 1, 0)
            CUIAutomation8._com_interfaces_ += [
                IUIAutomation2,
                IUIAutomation3,
                IUIAutomation4,
                IUIAutomation5

            ]

        # END IF  __UIAutomationClient_LIBRARY_DEFINED__

        # interface __MIDL_itf_uiautomationclient_0000_0001
        # [local]
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    # Additional Prototypes for ALL interfaces
    # end of Additional Prototypes
    if defined(__cplusplus):
        pass
    # END IF

# END IF


