import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_INC_UIAUTOMATIONCOREAPI = None
__uiautomationclient_h__ = None

class UiaCondition(ctypes.Structure):
    pass





class UiaPropertyCondition(ctypes.Structure):
    pass





class UiaAndOrCondition(ctypes.Structure):
    pass





class UiaNotCondition(ctypes.Structure):
    pass





class UiaCacheRequest(ctypes.Structure):
    pass





class UiaFindParams(ctypes.Structure):
    pass





class UiaEventArgs(ctypes.Structure):
    pass





class UiaPropertyChangedEventArgs(ctypes.Structure):
    pass





class UiaStructureChangedEventArgs(ctypes.Structure):
    pass





class UiaTextEditTextChangedEventArgs(ctypes.Structure):
    pass





class UiaChangesEventArgs(ctypes.Structure):
    pass





class UiaAsyncContentLoadedEventArgs(ctypes.Structure):
    pass





class UiaWindowClosedEventArgs(ctypes.Structure):
    pass







# -------------------------------------------------------------
# UIAutomationCoreAPI.h
# UIAutomation core APIs, types and enums
# Copyright (c) Microsoft Corporation. All rights reserved.
# -------------------------------------------------------------
if not defined(_INC_UIAUTOMATIONCOREAPI):
    _INC_UIAUTOMATIONCOREAPI = VOID
    if defined(__cplusplus):
        pass
    # END IF


    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # ----------------------------------------------------------------
        # General constants and types
        # ----------------------------------------------------------------
        # These are all in FACILITY_ITF
        UIA_E_ELEMENTNOTENABLED = 0x80040200


        UIA_E_ELEMENTNOTAVAILABLE = 0x80040201


        UIA_E_NOCLICKABLEPOINT = 0x80040202


        UIA_E_PROXYASSEMBLYNOTLOADED = 0x80040203

        # Can be thrown by providers to indicate they
        # explicitly don't support a pattern or property
        UIA_E_NOTSUPPORTED = 0x80040204

        # The following are COR error codes, included here as a convenience
        # (equivalent codes are in < corerror.h > )
        # COR_E_INVALIDOPERATION
        UIA_E_INVALIDOPERATION = 0x80131509

        # COR_E_TIMEOUT
        UIA_E_TIMEOUT = 0x80131505

        # The following common managed exceptions are not represented here
        # since they already have standard COM error codes assigned to them
        # by COM Interop:
        # ArgumentException  E_INVALIDARG
        # ArgumentNullException - maps to ArgumentException
        # Other constants
        UiaAppendRuntimeId = 3


        UiaRootObjectId = -25
        HUIANODE = DECLARE_HANDLE()
        HUIAPATTERNOBJECT = DECLARE_HANDLE()
        HUIATEXTRANGE = DECLARE_HANDLE()
        HUIAEVENT = DECLARE_HANDLE()

        if not defined(__uiautomationclient_h__):
            class TreeScope(ENUM):
                TreeScope_None = 0x0
                TreeScope_Element = 0x1
                TreeScope_Children = 0x2
                TreeScope_Descendants = 0x4
                TreeScope_Parent = 0x8
                TreeScope_Ancestors = 0x10
                TreeScope_Subtree = (
                    TreeScope_Element |
                    TreeScope_Children |
                    TreeScope_Descendants
                )

            TreeScope_None = TreeScope.TreeScope_None
            TreeScope_Element = TreeScope.TreeScope_Element
            TreeScope_Children = TreeScope.TreeScope_Children
            TreeScope_Descendants = TreeScope.TreeScope_Descendants
            TreeScope_Parent = TreeScope.TreeScope_Parent
            TreeScope_Ancestors = TreeScope.TreeScope_Ancestors
            TreeScope_Subtree = TreeScope.TreeScope_Subtree
        # END IF


        # ----------------------------------------------------------------
        # Automation Identifier GUIDs
        # ----------------------------------------------------------------
        RuntimeId_Property_GUID = DEFINE_GUID(
            0xA39EEBFA,
            0x7FBA,
            0x4C89,
            0xB4,
            0xD4,
            0xB9,
            0x9E,
            0x2D,
            0xE7,
            0xD1,
            0x60
        )
        BoundingRectangle_Property_GUID = DEFINE_GUID(
            0x7BBFE8B2,
            0x3BFC,
            0x48DD,
            0xB7,
            0x29,
            0xC7,
            0x94,
            0xB8,
            0x46,
            0xE9,
            0xA1
        )
        ProcessId_Property_GUID = DEFINE_GUID(
            0x40499998,
            0x9C31,
            0x4245,
            0xA4,
            0x03,
            0x87,
            0x32,
            0x0E,
            0x59,
            0xEA,
            0xF6
        )
        ControlType_Property_GUID = DEFINE_GUID(
            0xCA774FEA,
            0x28AC,
            0x4BC2,
            0x94,
            0xCA,
            0xAC,
            0xEC,
            0x6D,
            0x6C,
            0x10,
            0xA3
        )
        LocalizedControlType_Property_GUID = DEFINE_GUID(
            0x8763404F,
            0xA1BD,
            0x452A,
            0x89,
            0xC4,
            0x3F,
            0x01,
            0xD3,
            0x83,
            0x38,
            0x06
        )
        Name_Property_GUID = DEFINE_GUID(
            0xC3A6921B,
            0x4A99,
            0x44F1,
            0xBC,
            0xA6,
            0x61,
            0x18,
            0x70,
            0x52,
            0xC4,
            0x31
        )
        AcceleratorKey_Property_GUID = DEFINE_GUID(
            0x514865DF,
            0x2557,
            0x4CB9,
            0xAE,
            0xED,
            0x6C,
            0xED,
            0x08,
            0x4C,
            0xE5,
            0x2C
        )
        AccessKey_Property_GUID = DEFINE_GUID(
            0x06827B12,
            0xA7F9,
            0x4A15,
            0x91,
            0x7C,
            0xFF,
            0xA5,
            0xAD,
            0x3E,
            0xB0,
            0xA7
        )
        HasKeyboardFocus_Property_GUID = DEFINE_GUID(
            0xCF8AFD39,
            0x3F46,
            0x4800,
            0x96,
            0x56,
            0xB2,
            0xBF,
            0x12,
            0x52,
            0x99,
            0x05
        )
        IsKeyboardFocusable_Property_GUID = DEFINE_GUID(
            0xF7B8552A,
            0x0859,
            0x4B37,
            0xB9,
            0xCB,
            0x51,
            0xE7,
            0x20,
            0x92,
            0xF2,
            0x9F
        )
        IsEnabled_Property_GUID = DEFINE_GUID(
            0x2109427F,
            0xDA60,
            0x4FED,
            0xBF,
            0x1B,
            0x26,
            0x4B,
            0xDC,
            0xE6,
            0xEB,
            0x3A
        )
        AutomationId_Property_GUID = DEFINE_GUID(
            0xC82C0500,
            0xB60E,
            0x4310,
            0xA2,
            0x67,
            0x30,
            0x3C,
            0x53,
            0x1F,
            0x8E,
            0xE5
        )
        ClassName_Property_GUID = DEFINE_GUID(
            0x157B7215,
            0x894F,
            0x4B65,
            0x84,
            0xE2,
            0xAA,
            0xC0,
            0xDA,
            0x08,
            0xB1,
            0x6B
        )
        HelpText_Property_GUID = DEFINE_GUID(
            0x08555685,
            0x0977,
            0x45C7,
            0xA7,
            0xA6,
            0xAB,
            0xAF,
            0x56,
            0x84,
            0x12,
            0x1A
        )
        ClickablePoint_Property_GUID = DEFINE_GUID(
            0x0196903B,
            0xB203,
            0x4818,
            0xA9,
            0xF3,
            0xF0,
            0x8E,
            0x67,
            0x5F,
            0x23,
            0x41
        )
        Culture_Property_GUID = DEFINE_GUID(
            0xE2D74F27,
            0x3D79,
            0x4DC2,
            0xB8,
            0x8B,
            0x30,
            0x44,
            0x96,
            0x3A,
            0x8A,
            0xFB
        )
        IsControlElement_Property_GUID = DEFINE_GUID(
            0x95F35085,
            0xABCC,
            0x4AFD,
            0xA5,
            0xF4,
            0xDB,
            0xB4,
            0x6C,
            0x23,
            0x0F,
            0xDB
        )
        IsContentElement_Property_GUID = DEFINE_GUID(
            0x4BDA64A8,
            0xF5D8,
            0x480B,
            0x81,
            0x55,
            0xEF,
            0x2E,
            0x89,
            0xAD,
            0xB6,
            0x72
        )
        LabeledBy_Property_GUID = DEFINE_GUID(
            0xE5B8924B,
            0xFC8A,
            0x4A35,
            0x80,
            0x31,
            0xCF,
            0x78,
            0xAC,
            0x43,
            0xE5,
            0x5E
        )
        IsPassword_Property_GUID = DEFINE_GUID(
            0xE8482EB1,
            0x687C,
            0x497B,
            0xBE,
            0xBC,
            0x03,
            0xBE,
            0x53,
            0xEC,
            0x14,
            0x54
        )
        NewNativeWindowHandle_Property_GUID = DEFINE_GUID(
            0x5196B33B,
            0x380A,
            0x4982,
            0x95,
            0xE1,
            0x91,
            0xF3,
            0xEF,
            0x60,
            0xE0,
            0x24
        )
        ItemType_Property_GUID = DEFINE_GUID(
            0xCDDA434D,
            0x6222,
            0x413B,
            0xA6,
            0x8A,
            0x32,
            0x5D,
            0xD1,
            0xD4,
            0x0F,
            0x39
        )
        IsOffscreen_Property_GUID = DEFINE_GUID(
            0x03C3D160,
            0xDB79,
            0x42DB,
            0xA2,
            0xEF,
            0x1C,
            0x23,
            0x1E,
            0xED,
            0xE5,
            0x07
        )
        Orientation_Property_GUID = DEFINE_GUID(
            0xA01EEE62,
            0x3884,
            0x4415,
            0x88,
            0x7E,
            0x67,
            0x8E,
            0xC2,
            0x1E,
            0x39,
            0xBA
        )
        FrameworkId_Property_GUID = DEFINE_GUID(
            0xDBFD9900,
            0x7E1A,
            0x4F58,
            0xB6,
            0x1B,
            0x70,
            0x63,
            0x12,
            0x0F,
            0x77,
            0x3B
        )
        IsRequiredForForm_Property_GUID = DEFINE_GUID(
            0x4F5F43CF,
            0x59FB,
            0x4BDE,
            0xA2,
            0x70,
            0x60,
            0x2E,
            0x5E,
            0x11,
            0x41,
            0xE9
        )
        ItemStatus_Property_GUID = DEFINE_GUID(
            0x51DE0321,
            0x3973,
            0x43E7,
            0x89,
            0x13,
            0x0B,
            0x08,
            0xE8,
            0x13,
            0xC3,
            0x7F
        )
        AriaRole_Property_GUID = DEFINE_GUID(
            0xDD207B95,
            0xBE4A,
            0x4E0D,
            0xB7,
            0x27,
            0x63,
            0xAC,
            0xE9,
            0x4B,
            0x69,
            0x16
        )
        AriaProperties_Property_GUID = DEFINE_GUID(
            0x4213678C,
            0xE025,
            0x4922,
            0xBE,
            0xB5,
            0xE4,
            0x3B,
            0xA0,
            0x8E,
            0x62,
            0x21
        )
        IsDataValidForForm_Property_GUID = DEFINE_GUID(
            0x445AC684,
            0xC3FC,
            0x4DD9,
            0xAC,
            0xF8,
            0x84,
            0x5A,
            0x57,
            0x92,
            0x96,
            0xBA
        )
        ControllerFor_Property_GUID = DEFINE_GUID(
            0x51124C8A,
            0xA5D2,
            0x4F13,
            0x9B,
            0xE6,
            0x7F,
            0xA8,
            0xBA,
            0x9D,
            0x3A,
            0x90
        )
        DescribedBy_Property_GUID = DEFINE_GUID(
            0x7C5865B8,
            0x9992,
            0x40FD,
            0x8D,
            0xB0,
            0x6B,
            0xF1,
            0xD3,
            0x17,
            0xF9,
            0x98
        )
        FlowsTo_Property_GUID = DEFINE_GUID(
            0xE4F33D20,
            0x559A,
            0x47FB,
            0xA8,
            0x30,
            0xF9,
            0xCB,
            0x4F,
            0xF1,
            0xA7,
            0x0A
        )
        ProviderDescription_Property_GUID = DEFINE_GUID(
            0xDCA5708A,
            0xC16B,
            0x4CD9,
            0xB8,
            0x89,
            0xBE,
            0xB1,
            0x6A,
            0x80,
            0x49,
            0x04
        )
        OptimizeForVisualContent_Property_GUID = DEFINE_GUID(
            0x6A852250,
            0xC75A,
            0x4E5D,
            0xB8,
            0x58,
            0xE3,
            0x81,
            0xB0,
            0xF7,
            0x88,
            0x61
        )
        IsDockPatternAvailable_Property_GUID = DEFINE_GUID(
            0x2600A4C4,
            0x2FF8,
            0x4C96,
            0xAE,
            0x31,
            0x8F,
            0xE6,
            0x19,
            0xA1,
            0x3C,
            0x6C
        )
        IsExpandCollapsePatternAvailable_Property_GUID = DEFINE_GUID(
            0x929D3806,
            0x5287,
            0x4725,
            0xAA,
            0x16,
            0x22,
            0x2A,
            0xFC,
            0x63,
            0xD5,
            0x95
        )
        IsGridItemPatternAvailable_Property_GUID = DEFINE_GUID(
            0x5A43E524,
            0xF9A2,
            0x4B12,
            0x84,
            0xC8,
            0xB4,
            0x8A,
            0x3E,
            0xFE,
            0xDD,
            0x34
        )
        IsGridPatternAvailable_Property_GUID = DEFINE_GUID(
            0x5622C26C,
            0xF0EF,
            0x4F3B,
            0x97,
            0xCB,
            0x71,
            0x4C,
            0x08,
            0x68,
            0x58,
            0x8B
        )
        IsInvokePatternAvailable_Property_GUID = DEFINE_GUID(
            0x4E725738,
            0x8364,
            0x4679,
            0xAA,
            0x6C,
            0xF3,
            0xF4,
            0x19,
            0x31,
            0xF7,
            0x50
        )
        IsMultipleViewPatternAvailable_Property_GUID = DEFINE_GUID(
            0xFF0A31EB,
            0x8E25,
            0x469D,
            0x8D,
            0x6E,
            0xE7,
            0x71,
            0xA2,
            0x7C,
            0x1B,
            0x90
        )
        IsRangeValuePatternAvailable_Property_GUID = DEFINE_GUID(
            0xFDA4244A,
            0xEB4D,
            0x43FF,
            0xB5,
            0xAD,
            0xED,
            0x36,
            0xD3,
            0x73,
            0xEC,
            0x4C
        )
        IsScrollPatternAvailable_Property_GUID = DEFINE_GUID(
            0x3EBB7B4A,
            0x828A,
            0x4B57,
            0x9D,
            0x22,
            0x2F,
            0xEA,
            0x16,
            0x32,
            0xED,
            0x0D
        )
        IsScrollItemPatternAvailable_Property_GUID = DEFINE_GUID(
            0x1CAD1A05,
            0x0927,
            0x4B76,
            0x97,
            0xE1,
            0x0F,
            0xCD,
            0xB2,
            0x09,
            0xB9,
            0x8A
        )
        IsSelectionItemPatternAvailable_Property_GUID = DEFINE_GUID(
            0x8BECD62D,
            0x0BC3,
            0x4109,
            0xBE,
            0xE2,
            0x8E,
            0x67,
            0x15,
            0x29,
            0x0E,
            0x68
        )
        IsSelectionPatternAvailable_Property_GUID = DEFINE_GUID(
            0xF588ACBE,
            0xC769,
            0x4838,
            0x9A,
            0x60,
            0x26,
            0x86,
            0xDC,
            0x11,
            0x88,
            0xC4
        )
        IsTablePatternAvailable_Property_GUID = DEFINE_GUID(
            0xCB83575F,
            0x45C2,
            0x4048,
            0x9C,
            0x76,
            0x15,
            0x97,
            0x15,
            0xA1,
            0x39,
            0xDF
        )
        IsTableItemPatternAvailable_Property_GUID = DEFINE_GUID(
            0xEB36B40D,
            0x8EA4,
            0x489B,
            0xA0,
            0x13,
            0xE6,
            0x0D,
            0x59,
            0x51,
            0xFE,
            0x34
        )
        IsTextPatternAvailable_Property_GUID = DEFINE_GUID(
            0xFBE2D69D,
            0xAFF6,
            0x4A45,
            0x82,
            0xE2,
            0xFC,
            0x92,
            0xA8,
            0x2F,
            0x59,
            0x17
        )
        IsTogglePatternAvailable_Property_GUID = DEFINE_GUID(
            0x78686D53,
            0xFCD0,
            0x4B83,
            0x9B,
            0x78,
            0x58,
            0x32,
            0xCE,
            0x63,
            0xBB,
            0x5B
        )
        IsTransformPatternAvailable_Property_GUID = DEFINE_GUID(
            0xA7F78804,
            0xD68B,
            0x4077,
            0xA5,
            0xC6,
            0x7A,
            0x5E,
            0xA1,
            0xAC,
            0x31,
            0xC5
        )
        IsValuePatternAvailable_Property_GUID = DEFINE_GUID(
            0x0B5020A7,
            0x2119,
            0x473B,
            0xBE,
            0x37,
            0x5C,
            0xEB,
            0x98,
            0xBB,
            0xFB,
            0x22
        )
        IsWindowPatternAvailable_Property_GUID = DEFINE_GUID(
            0xE7A57BB1,
            0x5888,
            0x4155,
            0x98,
            0xDC,
            0xB4,
            0x22,
            0xFD,
            0x57,
            0xF2,
            0xBC
        )
        IsLegacyIAccessiblePatternAvailable_Property_GUID = DEFINE_GUID(
            0xD8EBD0C7,
            0x929A,
            0x4EE7,
            0x8D,
            0x3A,
            0xD3,
            0xD9,
            0x44,
            0x13,
            0x02,
            0x7B
        )
        IsItemContainerPatternAvailable_Property_GUID = DEFINE_GUID(
            0x624B5CA7,
            0xFE40,
            0x4957,
            0xA0,
            0x19,
            0x20,
            0xC4,
            0xCF,
            0x11,
            0x92,
            0x0F
        )
        IsVirtualizedItemPatternAvailable_Property_GUID = DEFINE_GUID(
            0x302CB151,
            0x2AC8,
            0x45D6,
            0x97,
            0x7B,
            0xD2,
            0xB3,
            0xA5,
            0xA5,
            0x3F,
            0x20
        )
        IsSynchronizedInputPatternAvailable_Property_GUID = DEFINE_GUID(
            0x75D69CC5,
            0xD2BF,
            0x4943,
            0x87,
            0x6E,
            0xB4,
            0x5B,
            0x62,
            0xA6,
            0xCC,
            0x66
        )
        IsObjectModelPatternAvailable_Property_GUID = DEFINE_GUID(
            0x6B21D89B,
            0x2841,
            0x412F,
            0x8E,
            0xF2,
            0x15,
            0xCA,
            0x95,
            0x23,
            0x18,
            0xBA
        )
        IsAnnotationPatternAvailable_Property_GUID = DEFINE_GUID(
            0x0B5B3238,
            0x6D5C,
            0x41B6,
            0xBC,
            0xC4,
            0x5E,
            0x80,
            0x7F,
            0x65,
            0x51,
            0xC4
        )
        IsTextPattern2Available_Property_GUID = DEFINE_GUID(
            0x41CF921D,
            0xE3F1,
            0x4B22,
            0x9C,
            0x81,
            0xE1,
            0xC3,
            0xED,
            0x33,
            0x1C,
            0x22
        )
        IsTextEditPatternAvailable_Property_GUID = DEFINE_GUID(
            0x7843425C,
            0x8B32,
            0x484C,
            0x9A,
            0xB5,
            0xE3,
            0x20,
            0x5,
            0x71,
            0xFF,
            0xDA
        )
        IsCustomNavigationPatternAvailable_Property_GUID = DEFINE_GUID(
            0x8F8E80D4,
            0x2351,
            0x48E0,
            0x87,
            0x4A,
            0x54,
            0xAA,
            0x73,
            0x13,
            0x88,
            0x9A
        )
        IsStylesPatternAvailable_Property_GUID = DEFINE_GUID(
            0x27F353D3,
            0x459C,
            0x4B59,
            0xA4,
            0x90,
            0x50,
            0x61,
            0x1D,
            0xAC,
            0xAF,
            0xB5
        )
        IsSpreadsheetPatternAvailable_Property_GUID = DEFINE_GUID(
            0x6FF43732,
            0xE4B4,
            0x4555,
            0x97,
            0xBC,
            0xEC,
            0xDB,
            0xBC,
            0x4D,
            0x18,
            0x88
        )
        IsSpreadsheetItemPatternAvailable_Property_GUID = DEFINE_GUID(
            0x9FE79B2A,
            0x2F94,
            0x43FD,
            0x99,
            0x6B,
            0x54,
            0x9E,
            0x31,
            0x6F,
            0x4A,
            0xCD
        )
        IsTransformPattern2Available_Property_GUID = DEFINE_GUID(
            0x25980B4B,
            0xBE04,
            0x4710,
            0xAB,
            0x4A,
            0xFD,
            0xA3,
            0x1D,
            0xBD,
            0x28,
            0x95
        )
        IsTextChildPatternAvailable_Property_GUID = DEFINE_GUID(
            0x559E65DF,
            0x30FF,
            0x43B5,
            0xB5,
            0xED,
            0x5B,
            0x28,
            0x3B,
            0x80,
            0xC7,
            0xE9
        )
        IsDragPatternAvailable_Property_GUID = DEFINE_GUID(
            0xE997A7B7,
            0x1D39,
            0x4CA7,
            0xBE,
            0xF,
            0x27,
            0x7F,
            0xCF,
            0x56,
            0x5,
            0xCC
        )
        IsDropTargetPatternAvailable_Property_GUID = DEFINE_GUID(
            0x686B62E,
            0x8E19,
            0x4AAF,
            0x87,
            0x3D,
            0x38,
            0x4F,
            0x6D,
            0x3B,
            0x92,
            0xBE
        )
        IsPeripheral_Property_GUID = DEFINE_GUID(
            0xDA758276,
            0x7ED5,
            0x49D4,
            0x8E,
            0x68,
            0xEC,
            0xC9,
            0xA2,
            0xD3,
            0x0,
            0xDD
        )
        PositionInSet_Property_GUID = DEFINE_GUID(
            0x33D1DC54,
            0x641E,
            0x4D76,
            0xA6,
            0xB1,
            0x13,
            0xF3,
            0x41,
            0xC1,
            0xF8,
            0x96
        )
        SizeOfSet_Property_GUID = DEFINE_GUID(
            0x1600D33C,
            0x3B9F,
            0x4369,
            0x94,
            0x31,
            0xAA,
            0x29,
            0x3F,
            0x34,
            0x4C,
            0xF1
        )
        Level_Property_GUID = DEFINE_GUID(
            0x242AC529,
            0xCD36,
            0x400F,
            0xAA,
            0xD9,
            0x78,
            0x76,
            0xEF,
            0x3A,
            0xF6,
            0x27
        )
        AnnotationTypes_Property_GUID = DEFINE_GUID(
            0x64B71F76,
            0x53C4,
            0x4696,
            0xA2,
            0x19,
            0x20,
            0xE9,
            0x40,
            0xC9,
            0xA1,
            0x76
        )
        AnnotationObjects_Property_GUID = DEFINE_GUID(
            0x310910C8,
            0x7C6E,
            0x4F20,
            0xBE,
            0xCD,
            0x4A,
            0xAF,
            0x6D,
            0x19,
            0x11,
            0x56
        )
        LandmarkType_Property_GUID = DEFINE_GUID(
            0x454045F2,
            0x6F61,
            0x49F7,
            0xA4,
            0xF8,
            0xB5,
            0xF0,
            0xCF,
            0x82,
            0xDA,
            0x1E
        )
        LocalizedLandmarkType_Property_GUID = DEFINE_GUID(
            0x7AC81980,
            0xEAFB,
            0x4FB2,
            0xBF,
            0x91,
            0xF4,
            0x85,
            0xBE,
            0xF5,
            0xE8,
            0xE1
        )
        FullDescription_Property_GUID = DEFINE_GUID(
            0x0D4450FF,
            0x6AEF,
            0x4F33,
            0x95,
            0xDD,
            0x7B,
            0xEF,
            0xA7,
            0x2A,
            0x43,
            0x91
        )
        Value_Value_Property_GUID = DEFINE_GUID(
            0xE95F5E64,
            0x269F,
            0x4A85,
            0xBA,
            0x99,
            0x40,
            0x92,
            0xC3,
            0xEA,
            0x29,
            0x86
        )
        Value_IsReadOnly_Property_GUID = DEFINE_GUID(
            0xEB090F30,
            0xE24C,
            0x4799,
            0xA7,
            0x05,
            0x0D,
            0x24,
            0x7B,
            0xC0,
            0x37,
            0xF8
        )
        RangeValue_Value_Property_GUID = DEFINE_GUID(
            0x131F5D98,
            0xC50C,
            0x489D,
            0xAB,
            0xE5,
            0xAE,
            0x22,
            0x08,
            0x98,
            0xC5,
            0xF7
        )
        RangeValue_IsReadOnly_Property_GUID = DEFINE_GUID(
            0x25FA1055,
            0xDEBF,
            0x4373,
            0xA7,
            0x9E,
            0x1F,
            0x1A,
            0x19,
            0x08,
            0xD3,
            0xC4
        )
        RangeValue_Minimum_Property_GUID = DEFINE_GUID(
            0x78CBD3B2,
            0x684D,
            0x4860,
            0xAF,
            0x93,
            0xD1,
            0xF9,
            0x5C,
            0xB0,
            0x22,
            0xFD
        )
        RangeValue_Maximum_Property_GUID = DEFINE_GUID(
            0x19319914,
            0xF979,
            0x4B35,
            0xA1,
            0xA6,
            0xD3,
            0x7E,
            0x05,
            0x43,
            0x34,
            0x73
        )
        RangeValue_LargeChange_Property_GUID = DEFINE_GUID(
            0xA1F96325,
            0x3A3D,
            0x4B44,
            0x8E,
            0x1F,
            0x4A,
            0x46,
            0xD9,
            0x84,
            0x40,
            0x19
        )
        RangeValue_SmallChange_Property_GUID = DEFINE_GUID(
            0x81C2C457,
            0x3941,
            0x4107,
            0x99,
            0x75,
            0x13,
            0x97,
            0x60,
            0xF7,
            0xC0,
            0x72
        )
        Scroll_HorizontalScrollPercent_Property_GUID = DEFINE_GUID(
            0xC7C13C0E,
            0xEB21,
            0x47FF,
            0xAC,
            0xC4,
            0xB5,
            0xA3,
            0x35,
            0x0F,
            0x51,
            0x91
        )
        Scroll_HorizontalViewSize_Property_GUID = DEFINE_GUID(
            0x70C2E5D4,
            0xFCB0,
            0x4713,
            0xA9,
            0xAA,
            0xAF,
            0x92,
            0xFF,
            0x79,
            0xE4,
            0xCD
        )
        Scroll_VerticalScrollPercent_Property_GUID = DEFINE_GUID(
            0x6C8D7099,
            0xB2A8,
            0x4948,
            0xBF,
            0xF7,
            0x3C,
            0xF9,
            0x05,
            0x8B,
            0xFE,
            0xFB
        )
        Scroll_VerticalViewSize_Property_GUID = DEFINE_GUID(
            0xDE6A2E22,
            0xD8C7,
            0x40C5,
            0x83,
            0xBA,
            0xE5,
            0xF6,
            0x81,
            0xD5,
            0x31,
            0x08
        )
        Scroll_HorizontallyScrollable_Property_GUID = DEFINE_GUID(
            0x8B925147,
            0x28CD,
            0x49AE,
            0xBD,
            0x63,
            0xF4,
            0x41,
            0x18,
            0xD2,
            0xE7,
            0x19
        )
        Scroll_VerticallyScrollable_Property_GUID = DEFINE_GUID(
            0x89164798,
            0x0068,
            0x4315,
            0xB8,
            0x9A,
            0x1E,
            0x7C,
            0xFB,
            0xBC,
            0x3D,
            0xFC
        )
        Selection_Selection_Property_GUID = DEFINE_GUID(
            0xAA6DC2A2,
            0x0E2B,
            0x4D38,
            0x96,
            0xD5,
            0x34,
            0xE4,
            0x70,
            0xB8,
            0x18,
            0x53
        )
        Selection_CanSelectMultiple_Property_GUID = DEFINE_GUID(
            0x49D73DA5,
            0xC883,
            0x4500,
            0x88,
            0x3D,
            0x8F,
            0xCF,
            0x8D,
            0xAF,
            0x6C,
            0xBE
        )
        Selection_IsSelectionRequired_Property_GUID = DEFINE_GUID(
            0xB1AE4422,
            0x63FE,
            0x44E7,
            0xA5,
            0xA5,
            0xA7,
            0x38,
            0xC8,
            0x29,
            0xB1,
            0x9A
        )
        Grid_RowCount_Property_GUID = DEFINE_GUID(
            0x2A9505BF,
            0xC2EB,
            0x4FB6,
            0xB3,
            0x56,
            0x82,
            0x45,
            0xAE,
            0x53,
            0x70,
            0x3E
        )
        Grid_ColumnCount_Property_GUID = DEFINE_GUID(
            0xFE96F375,
            0x44AA,
            0x4536,
            0xAC,
            0x7A,
            0x2A,
            0x75,
            0xD7,
            0x1A,
            0x3E,
            0xFC
        )
        GridItem_Row_Property_GUID = DEFINE_GUID(
            0x6223972A,
            0xC945,
            0x4563,
            0x93,
            0x29,
            0xFD,
            0xC9,
            0x74,
            0xAF,
            0x25,
            0x53
        )
        GridItem_Column_Property_GUID = DEFINE_GUID(
            0xC774C15C,
            0x62C0,
            0x4519,
            0x8B,
            0xDC,
            0x47,
            0xBE,
            0x57,
            0x3C,
            0x8A,
            0xD5
        )
        GridItem_RowSpan_Property_GUID = DEFINE_GUID(
            0x4582291C,
            0x466B,
            0x4E93,
            0x8E,
            0x83,
            0x3D,
            0x17,
            0x15,
            0xEC,
            0x0C,
            0x5E
        )
        GridItem_ColumnSpan_Property_GUID = DEFINE_GUID(
            0x583EA3F5,
            0x86D0,
            0x4B08,
            0xA6,
            0xEC,
            0x2C,
            0x54,
            0x63,
            0xFF,
            0xC1,
            0x09
        )
        GridItem_Parent_Property_GUID = DEFINE_GUID(
            0x9D912252,
            0xB97F,
            0x4ECC,
            0x85,
            0x10,
            0xEA,
            0x0E,
            0x33,
            0x42,
            0x7C,
            0x72
        )
        Dock_DockPosition_Property_GUID = DEFINE_GUID(
            0x6D67F02E,
            0xC0B0,
            0x4B10,
            0xB5,
            0xB9,
            0x18,
            0xD6,
            0xEC,
            0xF9,
            0x87,
            0x60
        )
        ExpandCollapse_ExpandCollapseState_Property_GUID = DEFINE_GUID(
            0x275A4C48,
            0x85A7,
            0x4F69,
            0xAB,
            0xA0,
            0xAF,
            0x15,
            0x76,
            0x10,
            0x00,
            0x2B
        )
        MultipleView_CurrentView_Property_GUID = DEFINE_GUID(
            0x7A81A67A,
            0xB94F,
            0x4875,
            0x91,
            0x8B,
            0x65,
            0xC8,
            0xD2,
            0xF9,
            0x98,
            0xE5
        )
        MultipleView_SupportedViews_Property_GUID = DEFINE_GUID(
            0x8D5DB9FD,
            0xCE3C,
            0x4AE7,
            0xB7,
            0x88,
            0x40,
            0x0A,
            0x3C,
            0x64,
            0x55,
            0x47
        )
        Window_CanMaximize_Property_GUID = DEFINE_GUID(
            0x64FFF53F,
            0x635D,
            0x41C1,
            0x95,
            0x0C,
            0xCB,
            0x5A,
            0xDF,
            0xBE,
            0x28,
            0xE3
        )
        Window_CanMinimize_Property_GUID = DEFINE_GUID(
            0xB73B4625,
            0x5988,
            0x4B97,
            0xB4,
            0xC2,
            0xA6,
            0xFE,
            0x6E,
            0x78,
            0xC8,
            0xC6
        )
        Window_WindowVisualState_Property_GUID = DEFINE_GUID(
            0x4AB7905F,
            0xE860,
            0x453E,
            0xA3,
            0x0A,
            0xF6,
            0x43,
            0x1E,
            0x5D,
            0xAA,
            0xD5
        )
        Window_WindowInteractionState_Property_GUID = DEFINE_GUID(
            0x4FED26A4,
            0x0455,
            0x4FA2,
            0xB2,
            0x1C,
            0xC4,
            0xDA,
            0x2D,
            0xB1,
            0xFF,
            0x9C
        )
        Window_IsModal_Property_GUID = DEFINE_GUID(
            0xFF4E6892,
            0x37B9,
            0x4FCA,
            0x85,
            0x32,
            0xFF,
            0xE6,
            0x74,
            0xEC,
            0xFE,
            0xED
        )
        Window_IsTopmost_Property_GUID = DEFINE_GUID(
            0xEF7D85D3,
            0x0937,
            0x4962,
            0x92,
            0x41,
            0xB6,
            0x23,
            0x45,
            0xF2,
            0x40,
            0x41
        )
        SelectionItem_IsSelected_Property_GUID = DEFINE_GUID(
            0xF122835F,
            0xCD5F,
            0x43DF,
            0xB7,
            0x9D,
            0x4B,
            0x84,
            0x9E,
            0x9E,
            0x60,
            0x20
        )
        SelectionItem_SelectionContainer_Property_GUID = DEFINE_GUID(
            0xA4365B6E,
            0x9C1E,
            0x4B63,
            0x8B,
            0x53,
            0xC2,
            0x42,
            0x1D,
            0xD1,
            0xE8,
            0xFB
        )
        Table_RowHeaders_Property_GUID = DEFINE_GUID(
            0xD9E35B87,
            0x6EB8,
            0x4562,
            0xAA,
            0xC6,
            0xA8,
            0xA9,
            0x07,
            0x52,
            0x36,
            0xA8
        )
        Table_ColumnHeaders_Property_GUID = DEFINE_GUID(
            0xAFF1D72B,
            0x968D,
            0x42B1,
            0xB4,
            0x59,
            0x15,
            0x0B,
            0x29,
            0x9D,
            0xA6,
            0x64
        )
        Table_RowOrColumnMajor_Property_GUID = DEFINE_GUID(
            0x83BE75C3,
            0x29FE,
            0x4A30,
            0x85,
            0xE1,
            0x2A,
            0x62,
            0x77,
            0xFD,
            0x10,
            0x6E
        )
        TableItem_RowHeaderItems_Property_GUID = DEFINE_GUID(
            0xB3F853A0,
            0x0574,
            0x4CD8,
            0xBC,
            0xD7,
            0xED,
            0x59,
            0x23,
            0x57,
            0x2D,
            0x97
        )
        TableItem_ColumnHeaderItems_Property_GUID = DEFINE_GUID(
            0x967A56A3,
            0x74B6,
            0x431E,
            0x8D,
            0xE6,
            0x99,
            0xC4,
            0x11,
            0x03,
            0x1C,
            0x58
        )
        Toggle_ToggleState_Property_GUID = DEFINE_GUID(
            0xB23CDC52,
            0x22C2,
            0x4C6C,
            0x9D,
            0xED,
            0xF5,
            0xC4,
            0x22,
            0x47,
            0x9E,
            0xDE
        )
        Transform_CanMove_Property_GUID = DEFINE_GUID(
            0x1B75824D,
            0x208B,
            0x4FDF,
            0xBC,
            0xCD,
            0xF1,
            0xF4,
            0xE5,
            0x74,
            0x1F,
            0x4F
        )
        Transform_CanResize_Property_GUID = DEFINE_GUID(
            0xBB98DCA5,
            0x4C1A,
            0x41D4,
            0xA4,
            0xF6,
            0xEB,
            0xC1,
            0x28,
            0x64,
            0x41,
            0x80
        )
        Transform_CanRotate_Property_GUID = DEFINE_GUID(
            0x10079B48,
            0x3849,
            0x476F,
            0xAC,
            0x96,
            0x44,
            0xA9,
            0x5C,
            0x84,
            0x40,
            0xD9
        )
        LegacyIAccessible_ChildId_Property_GUID = DEFINE_GUID(
            0x9A191B5D,
            0x9EF2,
            0x4787,
            0xA4,
            0x59,
            0xDC,
            0xDE,
            0x88,
            0x5D,
            0xD4,
            0xE8
        )
        LegacyIAccessible_Name_Property_GUID = DEFINE_GUID(
            0xCAEB063D,
            0x40AE,
            0x4869,
            0xAA,
            0x5A,
            0x1B,
            0x8E,
            0x5D,
            0x66,
            0x67,
            0x39
        )
        LegacyIAccessible_Value_Property_GUID = DEFINE_GUID(
            0xB5C5B0B6,
            0x8217,
            0x4A77,
            0x97,
            0xA5,
            0x19,
            0x0A,
            0x85,
            0xED,
            0x01,
            0x56
        )
        LegacyIAccessible_Description_Property_GUID = DEFINE_GUID(
            0x46448418,
            0x7D70,
            0x4EA9,
            0x9D,
            0x27,
            0xB7,
            0xE7,
            0x75,
            0xCF,
            0x2A,
            0xD7
        )
        LegacyIAccessible_Role_Property_GUID = DEFINE_GUID(
            0x6856E59F,
            0xCBAF,
            0x4E31,
            0x93,
            0xE8,
            0xBC,
            0xBF,
            0x6F,
            0x7E,
            0x49,
            0x1C
        )
        LegacyIAccessible_State_Property_GUID = DEFINE_GUID(
            0xDF985854,
            0x2281,
            0x4340,
            0xAB,
            0x9C,
            0xC6,
            0x0E,
            0x2C,
            0x58,
            0x03,
            0xF6
        )
        LegacyIAccessible_Help_Property_GUID = DEFINE_GUID(
            0x94402352,
            0x161C,
            0x4B77,
            0xA9,
            0x8D,
            0xA8,
            0x72,
            0xCC,
            0x33,
            0x94,
            0x7A
        )
        LegacyIAccessible_KeyboardShortcut_Property_GUID = DEFINE_GUID(
            0x8F6909AC,
            0x00B8,
            0x4259,
            0xA4,
            0x1C,
            0x96,
            0x62,
            0x66,
            0xD4,
            0x3A,
            0x8A
        )
        LegacyIAccessible_Selection_Property_GUID = DEFINE_GUID(
            0x8AA8B1E0,
            0x0891,
            0x40CC,
            0x8B,
            0x06,
            0x90,
            0xD7,
            0xD4,
            0x16,
            0x62,
            0x19
        )
        LegacyIAccessible_DefaultAction_Property_GUID = DEFINE_GUID(
            0x3B331729,
            0xEAAD,
            0x4502,
            0xB8,
            0x5F,
            0x92,
            0x61,
            0x56,
            0x22,
            0x91,
            0x3C
        )
        Annotation_AnnotationTypeId_Property_GUID = DEFINE_GUID(
            0x20AE484F,
            0x69EF,
            0x4C48,
            0x8F,
            0x5B,
            0xC4,
            0x93,
            0x8B,
            0x20,
            0x6A,
            0xC7
        )
        Annotation_AnnotationTypeName_Property_GUID = DEFINE_GUID(
            0x9B818892,
            0x5AC9,
            0x4AF9,
            0xAA,
            0x96,
            0xF5,
            0x8A,
            0x77,
            0xB0,
            0x58,
            0xE3
        )
        Annotation_Author_Property_GUID = DEFINE_GUID(
            0x7A528462,
            0x9C5C,
            0x4A03,
            0xA9,
            0x74,
            0x8B,
            0x30,
            0x7A,
            0x99,
            0x37,
            0xF2
        )
        Annotation_DateTime_Property_GUID = DEFINE_GUID(
            0x99B5CA5D,
            0x1ACF,
            0x414B,
            0xA4,
            0xD0,
            0x6B,
            0x35,
            0x0B,
            0x04,
            0x75,
            0x78
        )
        Annotation_Target_Property_GUID = DEFINE_GUID(
            0xB71B302D,
            0x2104,
            0x44AD,
            0x9C,
            0x5C,
            0x09,
            0x2B,
            0x49,
            0x07,
            0xD7,
            0x0F
        )
        Styles_StyleId_Property_GUID = DEFINE_GUID(
            0xDA82852F,
            0x3817,
            0x4233,
            0x82,
            0xAF,
            0x02,
            0x27,
            0x9E,
            0x72,
            0xCC,
            0x77
        )
        Styles_StyleName_Property_GUID = DEFINE_GUID(
            0x1C12B035,
            0x05D1,
            0x4F55,
            0x9E,
            0x8E,
            0x14,
            0x89,
            0xF3,
            0xFF,
            0x55,
            0x0D
        )
        Styles_FillColor_Property_GUID = DEFINE_GUID(
            0x63EFF97A,
            0xA1C5,
            0x4B1D,
            0x84,
            0xEB,
            0xB7,
            0x65,
            0xF2,
            0xED,
            0xD6,
            0x32
        )
        Styles_FillPatternStyle_Property_GUID = DEFINE_GUID(
            0x81CF651F,
            0x482B,
            0x4451,
            0xA3,
            0x0A,
            0xE1,
            0x54,
            0x5E,
            0x55,
            0x4F,
            0xB8
        )
        Styles_Shape_Property_GUID = DEFINE_GUID(
            0xC71A23F8,
            0x778C,
            0x400D,
            0x84,
            0x58,
            0x3B,
            0x54,
            0x3E,
            0x52,
            0x69,
            0x84
        )
        Styles_FillPatternColor_Property_GUID = DEFINE_GUID(
            0x939A59FE,
            0x8FBD,
            0x4E75,
            0xA2,
            0x71,
            0xAC,
            0x45,
            0x95,
            0x19,
            0x51,
            0x63
        )
        Styles_ExtendedProperties_Property_GUID = DEFINE_GUID(
            0xF451CDA0,
            0xBA0A,
            0x4681,
            0xB0,
            0xB0,
            0x0D,
            0xBD,
            0xB5,
            0x3E,
            0x58,
            0xF3
        )
        SpreadsheetItem_Formula_Property_GUID = DEFINE_GUID(
            0xE602E47D,
            0x1B47,
            0x4BEA,
            0x87,
            0xCF,
            0x3B,
            0x0B,
            0x0B,
            0x5C,
            0x15,
            0xB6
        )
        SpreadsheetItem_AnnotationObjects_Property_GUID = DEFINE_GUID(
            0xA3194C38,
            0xC9BC,
            0x4604,
            0x93,
            0x96,
            0xAE,
            0x3F,
            0x9F,
            0x45,
            0x7F,
            0x7B
        )
        SpreadsheetItem_AnnotationTypes_Property_GUID = DEFINE_GUID(
            0xC70C51D0,
            0xD602,
            0x4B45,
            0xAF,
            0xBC,
            0xB4,
            0x71,
            0x2B,
            0x96,
            0xD7,
            0x2B
        )
        Transform2_CanZoom_Property_GUID = DEFINE_GUID(
            0xF357E890,
            0xA756,
            0x4359,
            0x9C,
            0xA6,
            0x86,
            0x70,
            0x2B,
            0xF8,
            0xF3,
            0x81
        )
        LiveSetting_Property_GUID = DEFINE_GUID(
            0xC12BCD8E,
            0x2A8E,
            0x4950,
            0x8A,
            0xE7,
            0x36,
            0x25,
            0x11,
            0x1D,
            0x58,
            0xEB
        )
        Drag_IsGrabbed_Property_GUID = DEFINE_GUID(
            0x45F206F3,
            0x75CC,
            0x4CCA,
            0xA9,
            0xB9,
            0xFC,
            0xDF,
            0xB9,
            0x82,
            0xD8,
            0xA2
        )
        Drag_GrabbedItems_Property_GUID = DEFINE_GUID(
            0x77C1562C,
            0x7B86,
            0x4B21,
            0x9E,
            0xD7,
            0x3C,
            0xEF,
            0xDA,
            0x6F,
            0x4C,
            0x43
        )
        Drag_DropEffect_Property_GUID = DEFINE_GUID(
            0x646F2779,
            0x48D3,
            0x4B23,
            0x89,
            0x2,
            0x4B,
            0xF1,
            0x0,
            0x0,
            0x5D,
            0xF3
        )
        Drag_DropEffects_Property_GUID = DEFINE_GUID(
            0xF5D61156,
            0x7CE6,
            0x49BE,
            0xA8,
            0x36,
            0x92,
            0x69,
            0xDC,
            0xEC,
            0x92,
            0xF
        )
        DropTarget_DropTargetEffect_Property_GUID = DEFINE_GUID(
            0x8BB75975,
            0xA0CA,
            0x4981,
            0xB8,
            0x18,
            0x87,
            0xFC,
            0x66,
            0xE9,
            0x50,
            0x9D
        )
        DropTarget_DropTargetEffects_Property_GUID = DEFINE_GUID(
            0xBC1DD4ED,
            0xCB89,
            0x45F1,
            0xA5,
            0x92,
            0xE0,
            0x3B,
            0x8,
            0xAE,
            0x79,
            0xF
        )
        Transform2_ZoomLevel_Property_GUID = DEFINE_GUID(
            0xEEE29F1A,
            0xF4A2,
            0x4B5B,
            0xAC,
            0x65,
            0x95,
            0xCF,
            0x93,
            0x28,
            0x33,
            0x87
        )
        Transform2_ZoomMinimum_Property_GUID = DEFINE_GUID(
            0x742CCC16,
            0x4AD1,
            0x4E07,
            0x96,
            0xFE,
            0xB1,
            0x22,
            0xC6,
            0xE6,
            0xB2,
            0x2B
        )
        Transform2_ZoomMaximum_Property_GUID = DEFINE_GUID(
            0x42AB6B77,
            0xCEB0,
            0x4ECA,
            0xB8,
            0x2A,
            0x6C,
            0xFA,
            0x5F,
            0xA1,
            0xFC,
            0x08
        )
        FlowsFrom_Property_GUID = DEFINE_GUID(
            0x5C6844F,
            0x19DE,
            0x48F8,
            0x95,
            0xFA,
            0x88,
            0xD,
            0x5B,
            0xF,
            0xD6,
            0x15
        )
        FillColor_Property_GUID = DEFINE_GUID(
            0x6E0EC4D0,
            0xE2A8,
            0x4A56,
            0x9D,
            0xE7,
            0x95,
            0x33,
            0x89,
            0x93,
            0x3B,
            0x39
        )
        OutlineColor_Property_GUID = DEFINE_GUID(
            0xC395D6C0,
            0x4B55,
            0x4762,
            0xA0,
            0x73,
            0xFD,
            0x30,
            0x3A,
            0x63,
            0x4F,
            0x52
        )
        FillType_Property_GUID = DEFINE_GUID(
            0xC6FC74E4,
            0x8CB9,
            0x429C,
            0xA9,
            0xE1,
            0x9B,
            0xC4,
            0xAC,
            0x37,
            0x2B,
            0x62
        )
        VisualEffects_Property_GUID = DEFINE_GUID(
            0xE61A8565,
            0xAAD9,
            0x46D7,
            0x9E,
            0x70,
            0x4E,
            0x8A,
            0x84,
            0x20,
            0xD4,
            0x20
        )
        OutlineThickness_Property_GUID = DEFINE_GUID(
            0x13E67CC7,
            0xDAC2,
            0x4888,
            0xBD,
            0xD3,
            0x37,
            0x5C,
            0x62,
            0xFA,
            0x96,
            0x18
        )
        CenterPoint_Property_GUID = DEFINE_GUID(
            0xCB00C08,
            0x540C,
            0x4EDB,
            0x94,
            0x45,
            0x26,
            0x35,
            0x9E,
            0xA6,
            0x97,
            0x85
        )
        Rotation_Property_GUID = DEFINE_GUID(
            0x767CDC7D,
            0xAEC0,
            0x4110,
            0xAD,
            0x32,
            0x30,
            0xED,
            0xD4,
            0x3,
            0x49,
            0x2E
        )
        Size_Property_GUID = DEFINE_GUID(
            0x2B5F761D,
            0xF885,
            0x4404,
            0x97,
            0x3F,
            0x9B,
            0x1D,
            0x98,
            0xE3,
            0x6D,
            0x8F
        )
        ToolTipOpened_Event_GUID = DEFINE_GUID(
            0x3F4B97FF,
            0x2EDC,
            0x451D,
            0xBC,
            0xA4,
            0x95,
            0xA3,
            0x18,
            0x8D,
            0x5B,
            0x03
        )
        ToolTipClosed_Event_GUID = DEFINE_GUID(
            0x276D71EF,
            0x24A9,
            0x49B6,
            0x8E,
            0x97,
            0xDA,
            0x98,
            0xB4,
            0x01,
            0xBB,
            0xCD
        )
        StructureChanged_Event_GUID = DEFINE_GUID(
            0x59977961,
            0x3EDD,
            0x4B11,
            0xB1,
            0x3B,
            0x67,
            0x6B,
            0x2A,
            0x2A,
            0x6C,
            0xA9
        )
        MenuOpened_Event_GUID = DEFINE_GUID(
            0xEBE2E945,
            0x66CA,
            0x4ED1,
            0x9F,
            0xF8,
            0x2A,
            0xD7,
            0xDF,
            0x0A,
            0x1B,
            0x08
        )
        AutomationPropertyChanged_Event_GUID = DEFINE_GUID(
            0x2527FBA1,
            0x8D7A,
            0x4630,
            0xA4,
            0xCC,
            0xE6,
            0x63,
            0x15,
            0x94,
            0x2F,
            0x52
        )
        AutomationFocusChanged_Event_GUID = DEFINE_GUID(
            0xB68A1F17,
            0xF60D,
            0x41A7,
            0xA3,
            0xCC,
            0xB0,
            0x52,
            0x92,
            0x15,
            0x5F,
            0xE0
        )
        AsyncContentLoaded_Event_GUID = DEFINE_GUID(
            0x5FDEE11C,
            0xD2FA,
            0x4FB9,
            0x90,
            0x4E,
            0x5C,
            0xBE,
            0xE8,
            0x94,
            0xD5,
            0xEF
        )
        MenuClosed_Event_GUID = DEFINE_GUID(
            0x3CF1266E,
            0x1582,
            0x4041,
            0xAC,
            0xD7,
            0x88,
            0xA3,
            0x5A,
            0x96,
            0x52,
            0x97
        )
        LayoutInvalidated_Event_GUID = DEFINE_GUID(
            0xED7D6544,
            0xA6BD,
            0x4595,
            0x9B,
            0xAE,
            0x3D,
            0x28,
            0x94,
            0x6C,
            0xC7,
            0x15
        )
        Invoke_Invoked_Event_GUID = DEFINE_GUID(
            0xDFD699F0,
            0xC915,
            0x49DD,
            0xB4,
            0x22,
            0xDD,
            0xE7,
            0x85,
            0xC3,
            0xD2,
            0x4B
        )
        SelectionItem_ElementAddedToSelectionEvent_Event_GUID = DEFINE_GUID(
            0x3C822DD1,
            0xC407,
            0x4DBA,
            0x91,
            0xDD,
            0x79,
            0xD4,
            0xAE,
            0xD0,
            0xAE,
            0xC6
        )
        SelectionItem_ElementRemovedFromSelectionEvent_Event_GUID = DEFINE_GUID(
            0x097FA8A9,
            0x7079,
            0x41AF,
            0x8B,
            0x9C,
            0x09,
            0x34,
            0xD8,
            0x30,
            0x5E,
            0x5C
        )
        SelectionItem_ElementSelectedEvent_Event_GUID = DEFINE_GUID(
            0xB9C7DBFB,
            0x4EBE,
            0x4532,
            0xAA,
            0xF4,
            0x00,
            0x8C,
            0xF6,
            0x47,
            0x23,
            0x3C
        )
        Selection_InvalidatedEvent_Event_GUID = DEFINE_GUID(
            0xCAC14904,
            0x16B4,
            0x4B53,
            0x8E,
            0x47,
            0x4C,
            0xB1,
            0xDF,
            0x26,
            0x7B,
            0xB7
        )
        Text_TextSelectionChangedEvent_Event_GUID = DEFINE_GUID(
            0x918EDAA1,
            0x71B3,
            0x49AE,
            0x97,
            0x41,
            0x79,
            0xBE,
            0xB8,
            0xD3,
            0x58,
            0xF3
        )
        Text_TextChangedEvent_Event_GUID = DEFINE_GUID(
            0x4A342082,
            0xF483,
            0x48C4,
            0xAC,
            0x11,
            0xA8,
            0x4B,
            0x43,
            0x5E,
            0x2A,
            0x84
        )
        Window_WindowOpened_Event_GUID = DEFINE_GUID(
            0xD3E81D06,
            0xDE45,
            0x4F2F,
            0x96,
            0x33,
            0xDE,
            0x9E,
            0x02,
            0xFB,
            0x65,
            0xAF
        )
        Window_WindowClosed_Event_GUID = DEFINE_GUID(
            0xEDF141F8,
            0xFA67,
            0x4E22,
            0xBB,
            0xF7,
            0x94,
            0x4E,
            0x05,
            0x73,
            0x5E,
            0xE2
        )
        MenuModeStart_Event_GUID = DEFINE_GUID(
            0x18D7C631,
            0x166A,
            0x4AC9,
            0xAE,
            0x3B,
            0xEF,
            0x4B,
            0x54,
            0x20,
            0xE6,
            0x81
        )
        MenuModeEnd_Event_GUID = DEFINE_GUID(
            0x9ECD4C9F,
            0x80DD,
            0x47B8,
            0x82,
            0x67,
            0x5A,
            0xEC,
            0x06,
            0xBB,
            0x2C,
            0xFF
        )
        InputReachedTarget_Event_GUID = DEFINE_GUID(
            0x93ED549A,
            0x0549,
            0x40F0,
            0xBE,
            0xDB,
            0x28,
            0xE4,
            0x4F,
            0x7D,
            0xE2,
            0xA3
        )
        InputReachedOtherElement_Event_GUID = DEFINE_GUID(
            0xED201D8A,
            0x4E6C,
            0x415E,
            0xA8,
            0x74,
            0x24,
            0x60,
            0xC9,
            0xB6,
            0x6B,
            0xA8
        )
        InputDiscarded_Event_GUID = DEFINE_GUID(
            0x7F36C367,
            0x7B18,
            0x417C,
            0x97,
            0xE3,
            0x9D,
            0x58,
            0xDD,
            0xC9,
            0x44,
            0xAB
        )
        SystemAlert_Event_GUID = DEFINE_GUID(
            0xD271545D,
            0x7A3A,
            0x47A7,
            0x84,
            0x74,
            0x81,
            0xD2,
            0x9A,
            0x24,
            0x51,
            0xC9
        )
        LiveRegionChanged_Event_GUID = DEFINE_GUID(
            0x102D5E90,
            0xE6A9,
            0x41B6,
            0xB1,
            0xC5,
            0xA9,
            0xB1,
            0x92,
            0x9D,
            0x95,
            0x10
        )
        HostedFragmentRootsInvalidated_Event_GUID = DEFINE_GUID(
            0xE6BDB03E,
            0x0921,
            0x4EC5,
            0x8D,
            0xCF,
            0xEA,
            0xE8,
            0x77,
            0xB0,
            0x42,
            0x6B
        )
        Drag_DragStart_Event_GUID = DEFINE_GUID(
            0x883A480B,
            0x3AA9,
            0x429D,
            0x95,
            0xE4,
            0xD9,
            0xC8,
            0xD0,
            0x11,
            0xF0,
            0xDD
        )
        Drag_DragCancel_Event_GUID = DEFINE_GUID(
            0xC3EDE6FA,
            0x3451,
            0x4E0F,
            0x9E,
            0x71,
            0xDF,
            0x9C,
            0x28,
            0xA,
            0x46,
            0x57
        )
        Drag_DragComplete_Event_GUID = DEFINE_GUID(
            0x38E96188,
            0xEF1F,
            0x463E,
            0x91,
            0xCA,
            0x3A,
            0x77,
            0x92,
            0xC2,
            0x9C,
            0xAF
        )
        DropTarget_DragEnter_Event_GUID = DEFINE_GUID(
            0xAAD9319B,
            0x32C,
            0x4A88,
            0x96,
            0x1D,
            0x1C,
            0xF5,
            0x79,
            0x58,
            0x1E,
            0x34
        )
        DropTarget_DragLeave_Event_GUID = DEFINE_GUID(
            0xF82EB15,
            0x24A2,
            0x4988,
            0x92,
            0x17,
            0xDE,
            0x16,
            0x2A,
            0xEE,
            0x27,
            0x2B
        )
        DropTarget_Dropped_Event_GUID = DEFINE_GUID(
            0x622CEAD8,
            0x1EDB,
            0x4A3D,
            0xAB,
            0xBC,
            0xBE,
            0x22,
            0x11,
            0xFF,
            0x68,
            0xB5
        )
        Invoke_Pattern_GUID = DEFINE_GUID(
            0xD976C2FC,
            0x66EA,
            0x4A6E,
            0xB2,
            0x8F,
            0xC2,
            0x4C,
            0x75,
            0x46,
            0xAD,
            0x37
        )
        Selection_Pattern_GUID = DEFINE_GUID(
            0x66E3B7E8,
            0xD821,
            0x4D25,
            0x87,
            0x61,
            0x43,
            0x5D,
            0x2C,
            0x8B,
            0x25,
            0x3F
        )
        Value_Pattern_GUID = DEFINE_GUID(
            0x17FAAD9E,
            0xC877,
            0x475B,
            0xB9,
            0x33,
            0x77,
            0x33,
            0x27,
            0x79,
            0xB6,
            0x37
        )
        RangeValue_Pattern_GUID = DEFINE_GUID(
            0x18B00D87,
            0xB1C9,
            0x476A,
            0xBF,
            0xBD,
            0x5F,
            0x0B,
            0xDB,
            0x92,
            0x6F,
            0x63
        )
        Scroll_Pattern_GUID = DEFINE_GUID(
            0x895FA4B4,
            0x759D,
            0x4C50,
            0x8E,
            0x15,
            0x03,
            0x46,
            0x06,
            0x72,
            0x00,
            0x3C
        )
        ExpandCollapse_Pattern_GUID = DEFINE_GUID(
            0xAE05EFA2,
            0xF9D1,
            0x428A,
            0x83,
            0x4C,
            0x53,
            0xA5,
            0xC5,
            0x2F,
            0x9B,
            0x8B
        )
        Grid_Pattern_GUID = DEFINE_GUID(
            0x260A2CCB,
            0x93A8,
            0x4E44,
            0xA4,
            0xC1,
            0x3D,
            0xF3,
            0x97,
            0xF2,
            0xB0,
            0x2B
        )
        GridItem_Pattern_GUID = DEFINE_GUID(
            0xF2D5C877,
            0xA462,
            0x4957,
            0xA2,
            0xA5,
            0x2C,
            0x96,
            0xB3,
            0x03,
            0xBC,
            0x63
        )
        MultipleView_Pattern_GUID = DEFINE_GUID(
            0x547A6AE4,
            0x113F,
            0x47C4,
            0x85,
            0x0F,
            0xDB,
            0x4D,
            0xFA,
            0x46,
            0x6B,
            0x1D
        )
        Window_Pattern_GUID = DEFINE_GUID(
            0x27901735,
            0xC760,
            0x4994,
            0xAD,
            0x11,
            0x59,
            0x19,
            0xE6,
            0x06,
            0xB1,
            0x10
        )
        SelectionItem_Pattern_GUID = DEFINE_GUID(
            0x9BC64EEB,
            0x87C7,
            0x4B28,
            0x94,
            0xBB,
            0x4D,
            0x9F,
            0xA4,
            0x37,
            0xB6,
            0xEF
        )
        Dock_Pattern_GUID = DEFINE_GUID(
            0x9CBAA846,
            0x83C8,
            0x428D,
            0x82,
            0x7F,
            0x7E,
            0x60,
            0x63,
            0xFE,
            0x06,
            0x20
        )
        Table_Pattern_GUID = DEFINE_GUID(
            0xC415218E,
            0xA028,
            0x461E,
            0xAA,
            0x92,
            0x8F,
            0x92,
            0x5C,
            0xF7,
            0x93,
            0x51
        )
        TableItem_Pattern_GUID = DEFINE_GUID(
            0xDF1343BD,
            0x1888,
            0x4A29,
            0xA5,
            0x0C,
            0xB9,
            0x2E,
            0x6D,
            0xE3,
            0x7F,
            0x6F
        )
        Text_Pattern_GUID = DEFINE_GUID(
            0x8615F05D,
            0x7DE5,
            0x44FD,
            0xA6,
            0x79,
            0x2C,
            0xA4,
            0xB4,
            0x60,
            0x33,
            0xA8
        )
        Toggle_Pattern_GUID = DEFINE_GUID(
            0x0B419760,
            0xE2F4,
            0x43FF,
            0x8C,
            0x5F,
            0x94,
            0x57,
            0xC8,
            0x2B,
            0x56,
            0xE9
        )
        Transform_Pattern_GUID = DEFINE_GUID(
            0x24B46FDB,
            0x587E,
            0x49F1,
            0x9C,
            0x4A,
            0xD8,
            0xE9,
            0x8B,
            0x66,
            0x4B,
            0x7B
        )
        ScrollItem_Pattern_GUID = DEFINE_GUID(
            0x4591D005,
            0xA803,
            0x4D5C,
            0xB4,
            0xD5,
            0x8D,
            0x28,
            0x00,
            0xF9,
            0x06,
            0xA7
        )
        LegacyIAccessible_Pattern_GUID = DEFINE_GUID(
            0x54CC0A9F,
            0x3395,
            0x48AF,
            0xBA,
            0x8D,
            0x73,
            0xF8,
            0x56,
            0x90,
            0xF3,
            0xE0
        )
        ItemContainer_Pattern_GUID = DEFINE_GUID(
            0x3D13DA0F,
            0x8B9A,
            0x4A99,
            0x85,
            0xFA,
            0xC5,
            0xC9,
            0xA6,
            0x9F,
            0x1E,
            0xD4
        )
        VirtualizedItem_Pattern_GUID = DEFINE_GUID(
            0xF510173E,
            0x2E71,
            0x45E9,
            0xA6,
            0xE5,
            0x62,
            0xF6,
            0xED,
            0x82,
            0x89,
            0xD5
        )
        SynchronizedInput_Pattern_GUID = DEFINE_GUID(
            0x05C288A6,
            0xC47B,
            0x488B,
            0xB6,
            0x53,
            0x33,
            0x97,
            0x7A,
            0x55,
            0x1B,
            0x8B
        )
        ObjectModel_Pattern_GUID = DEFINE_GUID(
            0x3E04ACFE,
            0x08FC,
            0x47EC,
            0x96,
            0xBC,
            0x35,
            0x3F,
            0xA3,
            0xB3,
            0x4A,
            0xA7
        )
        Annotation_Pattern_GUID = DEFINE_GUID(
            0xF6C72AD7,
            0x356C,
            0x4850,
            0x92,
            0x91,
            0x31,
            0x6F,
            0x60,
            0x8A,
            0x8C,
            0x84
        )
        Text_Pattern2_GUID = DEFINE_GUID(
            0x498479A2,
            0x5B22,
            0x448D,
            0xB6,
            0xE4,
            0x64,
            0x74,
            0x90,
            0x86,
            0x06,
            0x98
        )
        TextEdit_Pattern_GUID = DEFINE_GUID(
            0x69F3FF89,
            0x5AF9,
            0x4C75,
            0x93,
            0x40,
            0xF2,
            0xDE,
            0x29,
            0x2E,
            0x45,
            0x91
        )
        CustomNavigation_Pattern_GUID = DEFINE_GUID(
            0xAFEA938A,
            0x621E,
            0x4054,
            0xBB,
            0x2C,
            0x2F,
            0x46,
            0x11,
            0x4D,
            0xAC,
            0x3F
        )
        Styles_Pattern_GUID = DEFINE_GUID(
            0x1AE62655,
            0xDA72,
            0x4D60,
            0xA1,
            0x53,
            0xE5,
            0xAA,
            0x69,
            0x88,
            0xE3,
            0xBF
        )
        Spreadsheet_Pattern_GUID = DEFINE_GUID(
            0x6A5B24C9,
            0x9D1E,
            0x4B85,
            0x9E,
            0x44,
            0xC0,
            0x2E,
            0x31,
            0x69,
            0xB1,
            0x0B
        )
        SpreadsheetItem_Pattern_GUID = DEFINE_GUID(
            0x32CF83FF,
            0xF1A8,
            0x4A8C,
            0x86,
            0x58,
            0xD4,
            0x7B,
            0xA7,
            0x4E,
            0x20,
            0xBA
        )
        Tranform_Pattern2_GUID = DEFINE_GUID(
            0x8AFCFD07,
            0xA369,
            0x44DE,
            0x98,
            0x8B,
            0x2F,
            0x7F,
            0xF4,
            0x9F,
            0xB8,
            0xA8
        )
        TextChild_Pattern_GUID = DEFINE_GUID(
            0x7533CAB7,
            0x3BFE,
            0x41EF,
            0x9E,
            0x85,
            0xE2,
            0x63,
            0x8C,
            0xBE,
            0x16,
            0x9E
        )
        Drag_Pattern_GUID = DEFINE_GUID(
            0xC0BEE21F,
            0xCCB3,
            0x4FED,
            0x99,
            0x5B,
            0x11,
            0x4F,
            0x6E,
            0x3D,
            0x27,
            0x28
        )
        DropTarget_Pattern_GUID = DEFINE_GUID(
            0xBCBEC56,
            0xBD34,
            0x4B7B,
            0x9F,
            0xD5,
            0x26,
            0x59,
            0x90,
            0x5E,
            0xA3,
            0xDC
        )
        Button_Control_GUID = DEFINE_GUID(
            0x5A78E369,
            0xC6A1,
            0x4F33,
            0xA9,
            0xD7,
            0x79,
            0xF2,
            0x0D,
            0x0C,
            0x78,
            0x8E
        )
        Calendar_Control_GUID = DEFINE_GUID(
            0x8913EB88,
            0x00E5,
            0x46BC,
            0x8E,
            0x4E,
            0x14,
            0xA7,
            0x86,
            0xE1,
            0x65,
            0xA1
        )
        CheckBox_Control_GUID = DEFINE_GUID(
            0xFB50F922,
            0xA3DB,
            0x49C0,
            0x8B,
            0xC3,
            0x06,
            0xDA,
            0xD5,
            0x57,
            0x78,
            0xE2
        )
        ComboBox_Control_GUID = DEFINE_GUID(
            0x54CB426C,
            0x2F33,
            0x4FFF,
            0xAA,
            0xA1,
            0xAE,
            0xF6,
            0x0D,
            0xAC,
            0x5D,
            0xEB
        )
        Edit_Control_GUID = DEFINE_GUID(
            0x6504A5C8,
            0x2C86,
            0x4F87,
            0xAE,
            0x7B,
            0x1A,
            0xBD,
            0xDC,
            0x81,
            0x0C,
            0xF9
        )
        Hyperlink_Control_GUID = DEFINE_GUID(
            0x8A56022C,
            0xB00D,
            0x4D15,
            0x8F,
            0xF0,
            0x5B,
            0x6B,
            0x26,
            0x6E,
            0x5E,
            0x02
        )
        Image_Control_GUID = DEFINE_GUID(
            0x2D3736E4,
            0x6B16,
            0x4C57,
            0xA9,
            0x62,
            0xF9,
            0x32,
            0x60,
            0xA7,
            0x52,
            0x43
        )
        ListItem_Control_GUID = DEFINE_GUID(
            0x7B3717F2,
            0x44D1,
            0x4A58,
            0x98,
            0xA8,
            0xF1,
            0x2A,
            0x9B,
            0x8F,
            0x78,
            0xE2
        )
        List_Control_GUID = DEFINE_GUID(
            0x9B149EE1,
            0x7CCA,
            0x4CFC,
            0x9A,
            0xF1,
            0xCA,
            0xC7,
            0xBD,
            0xDD,
            0x30,
            0x31
        )
        Menu_Control_GUID = DEFINE_GUID(
            0x2E9B1440,
            0x0EA8,
            0x41FD,
            0xB3,
            0x74,
            0xC1,
            0xEA,
            0x6F,
            0x50,
            0x3C,
            0xD1
        )
        MenuBar_Control_GUID = DEFINE_GUID(
            0xCC384250,
            0x0E7B,
            0x4AE8,
            0x95,
            0xAE,
            0xA0,
            0x8F,
            0x26,
            0x1B,
            0x52,
            0xEE
        )
        MenuItem_Control_GUID = DEFINE_GUID(
            0xF45225D3,
            0xD0A0,
            0x49D8,
            0x98,
            0x34,
            0x9A,
            0x00,
            0x0D,
            0x2A,
            0xED,
            0xDC
        )
        ProgressBar_Control_GUID = DEFINE_GUID(
            0x228C9F86,
            0xC36C,
            0x47BB,
            0x9F,
            0xB6,
            0xA5,
            0x83,
            0x4B,
            0xFC,
            0x53,
            0xA4
        )
        RadioButton_Control_GUID = DEFINE_GUID(
            0x3BDB49DB,
            0xFE2C,
            0x4483,
            0xB3,
            0xE1,
            0xE5,
            0x7F,
            0x21,
            0x94,
            0x40,
            0xC6
        )
        ScrollBar_Control_GUID = DEFINE_GUID(
            0xDAF34B36,
            0x5065,
            0x4946,
            0xB2,
            0x2F,
            0x92,
            0x59,
            0x5F,
            0xC0,
            0x75,
            0x1A
        )
        Slider_Control_GUID = DEFINE_GUID(
            0xB033C24B,
            0x3B35,
            0x4CEA,
            0xB6,
            0x09,
            0x76,
            0x36,
            0x82,
            0xFA,
            0x66,
            0x0B
        )
        Spinner_Control_GUID = DEFINE_GUID(
            0x60CC4B38,
            0x3CB1,
            0x4161,
            0xB4,
            0x42,
            0xC6,
            0xB7,
            0x26,
            0xC1,
            0x78,
            0x25
        )
        StatusBar_Control_GUID = DEFINE_GUID(
            0xD45E7D1B,
            0x5873,
            0x475F,
            0x95,
            0xA4,
            0x04,
            0x33,
            0xE1,
            0xF1,
            0xB0,
            0x0A
        )
        Tab_Control_GUID = DEFINE_GUID(
            0x38CD1F2D,
            0x337A,
            0x4BD2,
            0xA5,
            0xE3,
            0xAD,
            0xB4,
            0x69,
            0xE3,
            0x0B,
            0xD3
        )
        TabItem_Control_GUID = DEFINE_GUID(
            0x2C6A634F,
            0x921B,
            0x4E6E,
            0xB2,
            0x6E,
            0x08,
            0xFC,
            0xB0,
            0x79,
            0x8F,
            0x4C
        )
        Text_Control_GUID = DEFINE_GUID(
            0xAE9772DC,
            0xD331,
            0x4F09,
            0xBE,
            0x20,
            0x7E,
            0x6D,
            0xFA,
            0xF0,
            0x7B,
            0x0A
        )
        ToolBar_Control_GUID = DEFINE_GUID(
            0x8F06B751,
            0xE182,
            0x4E98,
            0x88,
            0x93,
            0x22,
            0x84,
            0x54,
            0x3A,
            0x7D,
            0xCE
        )
        ToolTip_Control_GUID = DEFINE_GUID(
            0x05DDC6D1,
            0x2137,
            0x4768,
            0x98,
            0xEA,
            0x73,
            0xF5,
            0x2F,
            0x71,
            0x34,
            0xF3
        )
        Tree_Control_GUID = DEFINE_GUID(
            0x7561349C,
            0xD241,
            0x43F4,
            0x99,
            0x08,
            0xB5,
            0xF0,
            0x91,
            0xBE,
            0xE6,
            0x11
        )
        TreeItem_Control_GUID = DEFINE_GUID(
            0x62C9FEB9,
            0x8FFC,
            0x4878,
            0xA3,
            0xA4,
            0x96,
            0xB0,
            0x30,
            0x31,
            0x5C,
            0x18
        )
        Custom_Control_GUID = DEFINE_GUID(
            0xF29EA0C3,
            0xADB7,
            0x430A,
            0xBA,
            0x90,
            0xE5,
            0x2C,
            0x73,
            0x13,
            0xE6,
            0xED
        )
        Group_Control_GUID = DEFINE_GUID(
            0xAD50AA1C,
            0xE8C8,
            0x4774,
            0xAE,
            0x1B,
            0xDD,
            0x86,
            0xDF,
            0x0B,
            0x3B,
            0xDC
        )
        Thumb_Control_GUID = DEFINE_GUID(
            0x701CA877,
            0xE310,
            0x4DD6,
            0xB6,
            0x44,
            0x79,
            0x7E,
            0x4F,
            0xAE,
            0xA2,
            0x13
        )
        DataGrid_Control_GUID = DEFINE_GUID(
            0x84B783AF,
            0xD103,
            0x4B0A,
            0x84,
            0x15,
            0xE7,
            0x39,
            0x42,
            0x41,
            0x0F,
            0x4B
        )
        DataItem_Control_GUID = DEFINE_GUID(
            0xA0177842,
            0xD94F,
            0x42A5,
            0x81,
            0x4B,
            0x60,
            0x68,
            0xAD,
            0xDC,
            0x8D,
            0xA5
        )
        Document_Control_GUID = DEFINE_GUID(
            0x3CD6BB6F,
            0x6F08,
            0x4562,
            0xB2,
            0x29,
            0xE4,
            0xE2,
            0xFC,
            0x7A,
            0x9E,
            0xB4
        )
        SplitButton_Control_GUID = DEFINE_GUID(
            0x7011F01F,
            0x4ACE,
            0x4901,
            0xB4,
            0x61,
            0x92,
            0x0A,
            0x6F,
            0x1C,
            0xA6,
            0x50
        )
        Window_Control_GUID = DEFINE_GUID(
            0xE13A7242,
            0xF462,
            0x4F4D,
            0xAE,
            0xC1,
            0x53,
            0xB2,
            0x8D,
            0x6C,
            0x32,
            0x90
        )
        Pane_Control_GUID = DEFINE_GUID(
            0x5C2B3F5B,
            0x9182,
            0x42A3,
            0x8D,
            0xEC,
            0x8C,
            0x04,
            0xC1,
            0xEE,
            0x63,
            0x4D
        )
        Header_Control_GUID = DEFINE_GUID(
            0x5B90CBCE,
            0x78FB,
            0x4614,
            0x82,
            0xB6,
            0x55,
            0x4D,
            0x74,
            0x71,
            0x8E,
            0x67
        )
        HeaderItem_Control_GUID = DEFINE_GUID(
            0xE6BC12CB,
            0x7C8E,
            0x49CF,
            0xB1,
            0x68,
            0x4A,
            0x93,
            0xA3,
            0x2B,
            0xEB,
            0xB0
        )
        Table_Control_GUID = DEFINE_GUID(
            0x773BFA0E,
            0x5BC4,
            0x4DEB,
            0x92,
            0x1B,
            0xDE,
            0x7B,
            0x32,
            0x06,
            0x22,
            0x9E
        )
        TitleBar_Control_GUID = DEFINE_GUID(
            0x98AA55BF,
            0x3BB0,
            0x4B65,
            0x83,
            0x6E,
            0x2E,
            0xA3,
            0x0D,
            0xBC,
            0x17,
            0x1F
        )
        Separator_Control_GUID = DEFINE_GUID(
            0x8767EBA3,
            0x2A63,
            0x4AB0,
            0xAC,
            0x8D,
            0xAA,
            0x50,
            0xE2,
            0x3D,
            0xE9,
            0x78
        )
        SemanticZoom_Control_GUID = DEFINE_GUID(
            0x5FD34A43,
            0x061E,
            0x42C8,
            0xB5,
            0x89,
            0x9D,
            0xCC,
            0xF7,
            0x4B,
            0xC4,
            0x3A
        )
        AppBar_Control_GUID = DEFINE_GUID(
            0x6114908D,
            0xCC02,
            0x4D37,
            0x87,
            0x5B,
            0xB5,
            0x30,
            0xC7,
            0x13,
            0x95,
            0x54
        )
        Text_AnimationStyle_Attribute_GUID = DEFINE_GUID(
            0x628209F0,
            0x7C9A,
            0x4D57,
            0xBE,
            0x64,
            0x1F,
            0x18,
            0x36,
            0x57,
            0x1F,
            0xF5
        )
        Text_BackgroundColor_Attribute_GUID = DEFINE_GUID(
            0xFDC49A07,
            0x583D,
            0x4F17,
            0xAD,
            0x27,
            0x77,
            0xFC,
            0x83,
            0x2A,
            0x3C,
            0x0B
        )
        Text_BulletStyle_Attribute_GUID = DEFINE_GUID(
            0xC1097C90,
            0xD5C4,
            0x4237,
            0x97,
            0x81,
            0x3B,
            0xEC,
            0x8B,
            0xA5,
            0x4E,
            0x48
        )
        Text_CapStyle_Attribute_GUID = DEFINE_GUID(
            0xFB059C50,
            0x92CC,
            0x49A5,
            0xBA,
            0x8F,
            0x0A,
            0xA8,
            0x72,
            0xBB,
            0xA2,
            0xF3
        )
        Text_Culture_Attribute_GUID = DEFINE_GUID(
            0xC2025AF9,
            0xA42D,
            0x4CED,
            0xA1,
            0xFB,
            0xC6,
            0x74,
            0x63,
            0x15,
            0x22,
            0x2E
        )
        Text_FontName_Attribute_GUID = DEFINE_GUID(
            0x64E63BA8,
            0xF2E5,
            0x476E,
            0xA4,
            0x77,
            0x17,
            0x34,
            0xFE,
            0xAA,
            0xF7,
            0x26
        )
        Text_FontSize_Attribute_GUID = DEFINE_GUID(
            0xDC5EEEFF,
            0x0506,
            0x4673,
            0x93,
            0xF2,
            0x37,
            0x7E,
            0x4A,
            0x8E,
            0x01,
            0xF1
        )
        Text_FontWeight_Attribute_GUID = DEFINE_GUID(
            0x6FC02359,
            0xB316,
            0x4F5F,
            0xB4,
            0x01,
            0xF1,
            0xCE,
            0x55,
            0x74,
            0x18,
            0x53
        )
        Text_ForegroundColor_Attribute_GUID = DEFINE_GUID(
            0x72D1C95D,
            0x5E60,
            0x471A,
            0x96,
            0xB1,
            0x6C,
            0x1B,
            0x3B,
            0x77,
            0xA4,
            0x36
        )
        Text_HorizontalTextAlignment_Attribute_GUID = DEFINE_GUID(
            0x04EA6161,
            0xFBA3,
            0x477A,
            0x95,
            0x2A,
            0xBB,
            0x32,
            0x6D,
            0x02,
            0x6A,
            0x5B
        )
        Text_IndentationFirstLine_Attribute_GUID = DEFINE_GUID(
            0x206F9AD5,
            0xC1D3,
            0x424A,
            0x81,
            0x82,
            0x6D,
            0xA9,
            0xA7,
            0xF3,
            0xD6,
            0x32
        )
        Text_IndentationLeading_Attribute_GUID = DEFINE_GUID(
            0x5CF66BAC,
            0x2D45,
            0x4A4B,
            0xB6,
            0xC9,
            0xF7,
            0x22,
            0x1D,
            0x28,
            0x15,
            0xB0
        )
        Text_IndentationTrailing_Attribute_GUID = DEFINE_GUID(
            0x97FF6C0F,
            0x1CE4,
            0x408A,
            0xB6,
            0x7B,
            0x94,
            0xD8,
            0x3E,
            0xB6,
            0x9B,
            0xF2
        )
        Text_IsHidden_Attribute_GUID = DEFINE_GUID(
            0x360182FB,
            0xBDD7,
            0x47F6,
            0xAB,
            0x69,
            0x19,
            0xE3,
            0x3F,
            0x8A,
            0x33,
            0x44
        )
        Text_IsItalic_Attribute_GUID = DEFINE_GUID(
            0xFCE12A56,
            0x1336,
            0x4A34,
            0x96,
            0x63,
            0x1B,
            0xAB,
            0x47,
            0x23,
            0x93,
            0x20
        )
        Text_IsReadOnly_Attribute_GUID = DEFINE_GUID(
            0xA738156B,
            0xCA3E,
            0x495E,
            0x95,
            0x14,
            0x83,
            0x3C,
            0x44,
            0x0F,
            0xEB,
            0x11
        )
        Text_IsSubscript_Attribute_GUID = DEFINE_GUID(
            0xF0EAD858,
            0x8F53,
            0x413C,
            0x87,
            0x3F,
            0x1A,
            0x7D,
            0x7F,
            0x5E,
            0x0D,
            0xE4
        )
        Text_IsSuperscript_Attribute_GUID = DEFINE_GUID(
            0xDA706EE4,
            0xB3AA,
            0x4645,
            0xA4,
            0x1F,
            0xCD,
            0x25,
            0x15,
            0x7D,
            0xEA,
            0x76
        )
        Text_MarginBottom_Attribute_GUID = DEFINE_GUID(
            0x7EE593C4,
            0x72B4,
            0x4CAC,
            0x92,
            0x71,
            0x3E,
            0xD2,
            0x4B,
            0x0E,
            0x4D,
            0x42
        )
        Text_MarginLeading_Attribute_GUID = DEFINE_GUID(
            0x9E9242D0,
            0x5ED0,
            0x4900,
            0x8E,
            0x8A,
            0xEE,
            0xCC,
            0x03,
            0x83,
            0x5A,
            0xFC
        )
        Text_MarginTop_Attribute_GUID = DEFINE_GUID(
            0x683D936F,
            0xC9B9,
            0x4A9A,
            0xB3,
            0xD9,
            0xD2,
            0x0D,
            0x33,
            0x31,
            0x1E,
            0x2A
        )
        Text_MarginTrailing_Attribute_GUID = DEFINE_GUID(
            0xAF522F98,
            0x999D,
            0x40AF,
            0xA5,
            0xB2,
            0x01,
            0x69,
            0xD0,
            0x34,
            0x20,
            0x02
        )
        Text_OutlineStyles_Attribute_GUID = DEFINE_GUID(
            0x5B675B27,
            0xDB89,
            0x46FE,
            0x97,
            0x0C,
            0x61,
            0x4D,
            0x52,
            0x3B,
            0xB9,
            0x7D
        )
        Text_OverlineColor_Attribute_GUID = DEFINE_GUID(
            0x83AB383A,
            0xFD43,
            0x40DA,
            0xAB,
            0x3E,
            0xEC,
            0xF8,
            0x16,
            0x5C,
            0xBB,
            0x6D
        )
        Text_OverlineStyle_Attribute_GUID = DEFINE_GUID(
            0x0A234D66,
            0x617E,
            0x427F,
            0x87,
            0x1D,
            0xE1,
            0xFF,
            0x1E,
            0x0C,
            0x21,
            0x3F
        )
        Text_StrikethroughColor_Attribute_GUID = DEFINE_GUID(
            0xBFE15A18,
            0x8C41,
            0x4C5A,
            0x9A,
            0x0B,
            0x04,
            0xAF,
            0x0E,
            0x07,
            0xF4,
            0x87
        )
        Text_StrikethroughStyle_Attribute_GUID = DEFINE_GUID(
            0x72913EF1,
            0xDA00,
            0x4F01,
            0x89,
            0x9C,
            0xAC,
            0x5A,
            0x85,
            0x77,
            0xA3,
            0x07
        )
        Text_Tabs_Attribute_GUID = DEFINE_GUID(
            0x2E68D00B,
            0x92FE,
            0x42D8,
            0x89,
            0x9A,
            0xA7,
            0x84,
            0xAA,
            0x44,
            0x54,
            0xA1
        )
        Text_TextFlowDirections_Attribute_GUID = DEFINE_GUID(
            0x8BDF8739,
            0xF420,
            0x423E,
            0xAF,
            0x77,
            0x20,
            0xA5,
            0xD9,
            0x73,
            0xA9,
            0x07
        )
        Text_UnderlineColor_Attribute_GUID = DEFINE_GUID(
            0xBFA12C73,
            0xFDE2,
            0x4473,
            0xBF,
            0x64,
            0x10,
            0x36,
            0xD6,
            0xAA,
            0x0F,
            0x45
        )
        Text_UnderlineStyle_Attribute_GUID = DEFINE_GUID(
            0x5F3B21C0,
            0xEDE4,
            0x44BD,
            0x9C,
            0x36,
            0x38,
            0x53,
            0x03,
            0x8C,
            0xBF,
            0xEB
        )
        Text_AnnotationTypes_Attribute_GUID = DEFINE_GUID(
            0xAD2EB431,
            0xEE4E,
            0x4BE1,
            0xA7,
            0xBA,
            0x55,
            0x59,
            0x15,
            0x5A,
            0x73,
            0xEF
        )
        Text_AnnotationObjects_Attribute_GUID = DEFINE_GUID(
            0xFF41CF68,
            0xE7AB,
            0x40B9,
            0x8C,
            0x72,
            0x72,
            0xA8,
            0xED,
            0x94,
            0x01,
            0x7D
        )
        Text_StyleName_Attribute_GUID = DEFINE_GUID(
            0x22C9E091,
            0x4D66,
            0x45D8,
            0xA8,
            0x28,
            0x73,
            0x7B,
            0xAB,
            0x4C,
            0x98,
            0xA7
        )
        Text_StyleId_Attribute_GUID = DEFINE_GUID(
            0x14C300DE,
            0xC32B,
            0x449B,
            0xAB,
            0x7C,
            0xB0,
            0xE0,
            0x78,
            0x9A,
            0xEA,
            0x5D
        )
        Text_Link_Attribute_GUID = DEFINE_GUID(
            0xB38EF51D,
            0x9E8D,
            0x4E46,
            0x91,
            0x44,
            0x56,
            0xEB,
            0xE1,
            0x77,
            0x32,
            0x9B
        )
        Text_IsActive_Attribute_GUID = DEFINE_GUID(
            0xF5A4E533,
            0xE1B8,
            0x436B,
            0x93,
            0x5D,
            0xB5,
            0x7A,
            0xA3,
            0xF5,
            0x58,
            0xC4
        )
        Text_SelectionActiveEnd_Attribute_GUID = DEFINE_GUID(
            0x1F668CC3,
            0x9BBF,
            0x416B,
            0xB0,
            0xA2,
            0xF8,
            0x9F,
            0x86,
            0xF6,
            0x61,
            0x2C
        )
        Text_CaretPosition_Attribute_GUID = DEFINE_GUID(
            0xB227B131,
            0x9889,
            0x4752,
            0xA9,
            0x1B,
            0x73,
            0x3E,
            0xFD,
            0xC5,
            0xC5,
            0xA0
        )
        Text_CaretBidiMode_Attribute_GUID = DEFINE_GUID(
            0x929EE7A6,
            0x51D3,
            0x4715,
            0x96,
            0xDC,
            0xB6,
            0x94,
            0xFA,
            0x24,
            0xA1,
            0x68
        )
        Text_BeforeParagraphSpacing_Attribute_GUID = DEFINE_GUID(
            0xBE7B0AB1,
            0xC822,
            0x4A24,
            0x85,
            0xE9,
            0xC8,
            0xF2,
            0x65,
            0xF,
            0xC7,
            0x9C
        )
        Text_AfterParagraphSpacing_Attribute_GUID = DEFINE_GUID(
            0x588CBB38,
            0xE62F,
            0x497C,
            0xB5,
            0xD1,
            0xCC,
            0xDF,
            0xE,
            0xE8,
            0x23,
            0xD8
        )
        Text_LineSpacing_Attribute_GUID = DEFINE_GUID(
            0x63FF70AE,
            0xD943,
            0x4B47,
            0x8A,
            0xB7,
            0xA7,
            0xA0,
            0x33,
            0xD3,
            0x21,
            0x4B
        )
        Text_BeforeSpacing_Attribute_GUID = DEFINE_GUID(
            0xBE7B0AB1,
            0xC822,
            0x4A24,
            0x85,
            0xE9,
            0xC8,
            0xF2,
            0x65,
            0xF,
            0xC7,
            0x9C
        )
        Text_AfterSpacing_Attribute_GUID = DEFINE_GUID(
            0x588CBB38,
            0xE62F,
            0x497C,
            0xB5,
            0xD1,
            0xCC,
            0xDF,
            0xE,
            0xE8,
            0x23,
            0xD8
        )
        Text_SayAsInterpretAs_Attribute_GUID = DEFINE_GUID(
            0xB38AD6AC,
            0xEEE1,
            0x4B6E,
            0x88,
            0xCC,
            0x01,
            0x4C,
            0xEF,
            0xA9,
            0x3F,
            0xCB
        )
        TextEdit_TextChanged_Event_GUID = DEFINE_GUID(
            0x120B0308,
            0xEC22,
            0x4EB8,
            0x9C,
            0x98,
            0x98,
            0x67,
            0xCD,
            0xA1,
            0xB1,
            0x65
        )
        TextEdit_ConversionTargetChanged_Event_GUID = DEFINE_GUID(
            0x3388C183,
            0xED4F,
            0x4C8B,
            0x9B,
            0xAA,
            0x36,
            0x4D,
            0x51,
            0xD8,
            0x84,
            0x7F
        )
        Changes_Event_GUID = DEFINE_GUID(
            0x7DF26714,
            0x614F,
            0x4E05,
            0x94,
            0x88,
            0x71,
            0x6C,
            0x5B,
            0xA1,
            0x94,
            0x36
        )
        Annotation_Custom_GUID = DEFINE_GUID(
            0x9EC82750,
            0x3931,
            0x4952,
            0x85,
            0xBC,
            0x1D,
            0xBF,
            0xF7,
            0x8A,
            0x43,
            0xE3
        )
        Annotation_SpellingError_GUID = DEFINE_GUID(
            0xAE85567E,
            0x9ECE,
            0x423F,
            0x81,
            0xB7,
            0x96,
            0xC4,
            0x3D,
            0x53,
            0xE5,
            0x0E
        )
        Annotation_GrammarError_GUID = DEFINE_GUID(
            0x757A048D,
            0x4518,
            0x41C6,
            0x85,
            0x4C,
            0xDC,
            0x00,
            0x9B,
            0x7C,
            0xFB,
            0x53
        )
        Annotation_Comment_GUID = DEFINE_GUID(
            0xFD2FDA30,
            0x26B3,
            0x4C06,
            0x8B,
            0xC7,
            0x98,
            0xF1,
            0x53,
            0x2E,
            0x46,
            0xFD
        )
        Annotation_FormulaError_GUID = DEFINE_GUID(
            0x95611982,
            0x0CAB,
            0x46D5,
            0xA2,
            0xF0,
            0xE3,
            0x0D,
            0x19,
            0x05,
            0xF8,
            0xBF
        )
        Annotation_TrackChanges_GUID = DEFINE_GUID(
            0x21E6E888,
            0xDC14,
            0x4016,
            0xAC,
            0x27,
            0x19,
            0x05,
            0x53,
            0xC8,
            0xC4,
            0x70
        )
        Annotation_Header_GUID = DEFINE_GUID(
            0x867B409B,
            0xB216,
            0x4472,
            0xA2,
            0x19,
            0x52,
            0x5E,
            0x31,
            0x06,
            0x81,
            0xF8
        )
        Annotation_Footer_GUID = DEFINE_GUID(
            0xCCEAB046,
            0x1833,
            0x47AA,
            0x80,
            0x80,
            0x70,
            0x1E,
            0xD0,
            0xB0,
            0xC8,
            0x32
        )
        Annotation_Highlighted_GUID = DEFINE_GUID(
            0x757C884E,
            0x8083,
            0x4081,
            0x8B,
            0x9C,
            0xE8,
            0x7F,
            0x50,
            0x72,
            0xF0,
            0xE4
        )
        Annotation_Endnote_GUID = DEFINE_GUID(
            0x7565725C,
            0x2D99,
            0x4839,
            0x96,
            0x0D,
            0x33,
            0xD3,
            0xB8,
            0x66,
            0xAB,
            0xA5
        )
        Annotation_Footnote_GUID = DEFINE_GUID(
            0x3DE10E21,
            0x4125,
            0x42DB,
            0x86,
            0x20,
            0xBE,
            0x80,
            0x83,
            0x08,
            0x06,
            0x24
        )
        Annotation_InsertionChange_GUID = DEFINE_GUID(
            0x0DBEB3A6,
            0xDF15,
            0x4164,
            0xA3,
            0xC0,
            0xE2,
            0x1A,
            0x8C,
            0xE9,
            0x31,
            0xC4
        )
        Annotation_DeletionChange_GUID = DEFINE_GUID(
            0xBE3D5B05,
            0x951D,
            0x42E7,
            0x90,
            0x1D,
            0xAD,
            0xC8,
            0xC2,
            0xCF,
            0x34,
            0xD0
        )
        Annotation_MoveChange_GUID = DEFINE_GUID(
            0x9DA587EB,
            0x23E5,
            0x4490,
            0xB3,
            0x85,
            0x1A,
            0x22,
            0xDD,
            0xC8,
            0xB1,
            0x87
        )
        Annotation_FormatChange_GUID = DEFINE_GUID(
            0xEB247345,
            0xD4F1,
            0x41CE,
            0x8E,
            0x52,
            0xF7,
            0x9B,
            0x69,
            0x63,
            0x5E,
            0x48
        )
        Annotation_UnsyncedChange_GUID = DEFINE_GUID(
            0x1851116A,
            0x0E47,
            0x4B30,
            0x8C,
            0xB5,
            0xD7,
            0xDA,
            0xE4,
            0xFB,
            0xCD,
            0x1B
        )
        Annotation_EditingLockedChange_GUID = DEFINE_GUID(
            0xC31F3E1C,
            0x7423,
            0x4DAC,
            0x83,
            0x48,
            0x41,
            0xF0,
            0x99,
            0xFF,
            0x6F,
            0x64
        )
        Annotation_ExternalChange_GUID = DEFINE_GUID(
            0x75A05B31,
            0x5F11,
            0x42FD,
            0x88,
            0x7D,
            0xDF,
            0xA0,
            0x10,
            0xDB,
            0x23,
            0x92
        )
        Annotation_ConflictingChange_GUID = DEFINE_GUID(
            0x98AF8802,
            0x517C,
            0x459F,
            0xAF,
            0x13,
            0x01,
            0x6D,
            0x3F,
            0xAB,
            0x87,
            0x7E
        )
        Annotation_Author_GUID = DEFINE_GUID(
            0xF161D3A7,
            0xF81B,
            0x4128,
            0xB1,
            0x7F,
            0x71,
            0xF6,
            0x90,
            0x91,
            0x45,
            0x20
        )
        Annotation_AdvancedProofingIssue_GUID = DEFINE_GUID(
            0xDAC7B72C,
            0xC0F2,
            0x4B84,
            0xB9,
            0x0D,
            0x5F,
            0xAF,
            0xC0,
            0xF0,
            0xEF,
            0x1C
        )
        Annotation_DataValidationError_GUID = DEFINE_GUID(
            0xC8649FA8,
            0x9775,
            0x437E,
            0xAD,
            0x46,
            0xE7,
            0x09,
            0xD9,
            0x3C,
            0x23,
            0x43
        )
        Annotation_CircularReferenceError_GUID = DEFINE_GUID(
            0x25BD9CF4,
            0x1745,
            0x4659,
            0xBA,
            0x67,
            0x72,
            0x7F,
            0x03,
            0x18,
            0xC6,
            0x16
        )
        Annotation_Mathematics_GUID = DEFINE_GUID(
            0xEAAB634B,
            0x26D0,
            0x40C1,
            0x80,
            0x73,
            0x57,
            0xCA,
            0x1C,
            0x63,
            0x3C,
            0x9B
        )
        Changes_Summary_GUID = DEFINE_GUID(
            0x313D65A6,
            0xE60F,
            0x4D62,
            0x98,
            0x61,
            0x55,
            0xAF,
            0xD7,
            0x28,
            0xD2,
            0x07
        )
        StyleId_Custom_GUID = DEFINE_GUID(
            0xEF2EDD3E,
            0xA999,
            0x4B7C,
            0xA3,
            0x78,
            0x09,
            0xBB,
            0xD5,
            0x2A,
            0x35,
            0x16
        )
        StyleId_Heading1_GUID = DEFINE_GUID(
            0x7F7E8F69,
            0x6866,
            0x4621,
            0x93,
            0x0C,
            0x9A,
            0x5D,
            0x0C,
            0xA5,
            0x96,
            0x1C
        )
        StyleId_Heading2_GUID = DEFINE_GUID(
            0xBAA9B241,
            0x5C69,
            0x469D,
            0x85,
            0xAD,
            0x47,
            0x47,
            0x37,
            0xB5,
            0x2B,
            0x14
        )
        StyleId_Heading3_GUID = DEFINE_GUID(
            0xBF8BE9D2,
            0xD8B8,
            0x4EC5,
            0x8C,
            0x52,
            0x9C,
            0xFB,
            0x0D,
            0x03,
            0x59,
            0x70
        )
        StyleId_Heading4_GUID = DEFINE_GUID(
            0x8436FFC0,
            0x9578,
            0x45FC,
            0x83,
            0xA4,
            0xFF,
            0x40,
            0x05,
            0x33,
            0x15,
            0xDD
        )
        StyleId_Heading5_GUID = DEFINE_GUID(
            0x909F424D,
            0x0DBF,
            0x406E,
            0x97,
            0xBB,
            0x4E,
            0x77,
            0x3D,
            0x97,
            0x98,
            0xF7
        )
        StyleId_Heading6_GUID = DEFINE_GUID(
            0x89D23459,
            0x5D5B,
            0x4824,
            0xA4,
            0x20,
            0x11,
            0xD3,
            0xED,
            0x82,
            0xE4,
            0x0F
        )
        StyleId_Heading7_GUID = DEFINE_GUID(
            0xA3790473,
            0xE9AE,
            0x422D,
            0xB8,
            0xE3,
            0x3B,
            0x67,
            0x5C,
            0x61,
            0x81,
            0xA4
        )
        StyleId_Heading8_GUID = DEFINE_GUID(
            0x2BC14145,
            0xA40C,
            0x4881,
            0x84,
            0xAE,
            0xF2,
            0x23,
            0x56,
            0x85,
            0x38,
            0x0C
        )
        StyleId_Heading9_GUID = DEFINE_GUID(
            0xC70D9133,
            0xBB2A,
            0x43D3,
            0x8A,
            0xC6,
            0x33,
            0x65,
            0x78,
            0x84,
            0xB0,
            0xF0
        )
        StyleId_Title_GUID = DEFINE_GUID(
            0x15D8201A,
            0xFFCF,
            0x481F,
            0xB0,
            0xA1,
            0x30,
            0xB6,
            0x3B,
            0xE9,
            0x8F,
            0x07
        )
        StyleId_Subtitle_GUID = DEFINE_GUID(
            0xB5D9FC17,
            0x5D6F,
            0x4420,
            0xB4,
            0x39,
            0x7C,
            0xB1,
            0x9A,
            0xD4,
            0x34,
            0xE2
        )
        StyleId_Normal_GUID = DEFINE_GUID(
            0xCD14D429,
            0xE45E,
            0x4475,
            0xA1,
            0xC5,
            0x7F,
            0x9E,
            0x6B,
            0xE9,
            0x6E,
            0xBA
        )
        StyleId_Emphasis_GUID = DEFINE_GUID(
            0xCA6E7DBE,
            0x355E,
            0x4820,
            0x95,
            0xA0,
            0x92,
            0x5F,
            0x04,
            0x1D,
            0x34,
            0x70
        )
        StyleId_Quote_GUID = DEFINE_GUID(
            0x5D1C21EA,
            0x8195,
            0x4F6C,
            0x87,
            0xEA,
            0x5D,
            0xAB,
            0xEC,
            0xE6,
            0x4C,
            0x1D
        )
        StyleId_BulletedList_GUID = DEFINE_GUID(
            0x5963ED64,
            0x6426,
            0x4632,
            0x8C,
            0xAF,
            0xA3,
            0x2A,
            0xD4,
            0x02,
            0xD9,
            0x1A
        )
        StyleId_NumberedList_GUID = DEFINE_GUID(
            0x1E96DBD5,
            0x64C3,
            0x43D0,
            0xB1,
            0xEE,
            0xB5,
            0x3B,
            0x06,
            0xE3,
            0xED,
            0xDF
        )
        Notification_Event_GUID = DEFINE_GUID(
            0x72C5A2F7,
            0x9788,
            0x480F,
            0xB8,
            0xEB,
            0x4D,
            0xEE,
            0x00,
            0xF6,
            0x18,
            0x6F
        )
        SID_IsUIAutomationObject = DEFINE_GUID(
            0xB96FDB85,
            0x7204,
            0x4724,
            0x84,
            0x2B,
            0xC7,
            0x05,
            0x9D,
            0xED,
            0xB9,
            0xD0
        )
        SID_ControlElementProvider = DEFINE_GUID(
            0xF4791D68,
            0xE254,
            0x4BA3,
            0x9A,
            0x53,
            0x26,
            0xA5,
            0xC5,
            0x49,
            0x79,
            0x46
        )
        IsSelectionPattern2Available_Property_GUID = DEFINE_GUID(
            0x490806FB,
            0x6E89,
            0x4A47,
            0x83,
            0x19,
            0xD2,
            0x66,
            0xE5,
            0x11,
            0xF0,
            0x21
        )
        Selection2_FirstSelectedItem_Property_GUID = DEFINE_GUID(
            0xCC24EA67,
            0x369C,
            0x4E55,
            0x9F,
            0xF7,
            0x38,
            0xDA,
            0x69,
            0x54,
            0x0C,
            0x29
        )
        Selection2_LastSelectedItem_Property_GUID = DEFINE_GUID(
            0xCF7BDA90,
            0x2D83,
            0x49F8,
            0x86,
            0x0C,
            0x9C,
            0xE3,
            0x94,
            0xCF,
            0x89,
            0xB4
        )
        Selection2_CurrentSelectedItem_Property_GUID = DEFINE_GUID(
            0x34257C26,
            0x83B5,
            0x41A6,
            0x93,
            0x9C,
            0xAE,
            0x84,
            0x1C,
            0x13,
            0x62,
            0x36
        )
        Selection2_ItemCount_Property_GUID = DEFINE_GUID(
            0xBB49EB9F,
            0x456D,
            0x4048,
            0xB5,
            0x91,
            0x9C,
            0x20,
            0x26,
            0xB8,
            0x46,
            0x36
        )
        Selection_Pattern2_GUID = DEFINE_GUID(
            0xFBA25CAB,
            0xAB98,
            0x49F7,
            0xA7,
            0xDC,
            0xFE,
            0x53,
            0x9D,
            0xC1,
            0x5B,
            0xE7
        )
        HeadingLevel_Property_GUID = DEFINE_GUID(
            0x29084272,
            0xAAAF,
            0x4A30,
            0x87,
            0x96,
            0x3C,
            0x12,
            0xF6,
            0x2B,
            0x6B,
            0xBB
        )
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # ----------------------------------------------------------------
        # Error handling
        # ----------------------------------------------------------------
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE

        # BOOL WINAPI UiaGetErrorDescription(BSTR * pDescription);
        UiaGetErrorDescription = uiautomationcore.UiaGetErrorDescription
        UiaGetErrorDescription.restype = BOOL

        # ----------------------------------------------------------------
        # Conditions
        # ----------------------------------------------------------------
        class ConditionType(ENUM):
            ConditionType_True = 0
            ConditionType_False = 1
            ConditionType_Property = 2
            ConditionType_And = 3
            ConditionType_Or = 4
            ConditionType_Not = 5

        ConditionType_True = ConditionType.ConditionType_True
        ConditionType_False = ConditionType.ConditionType_False
        ConditionType_Property = ConditionType.ConditionType_Property
        ConditionType_And = ConditionType.ConditionType_And
        ConditionType_Or = ConditionType.ConditionType_Or
        ConditionType_Not = ConditionType.ConditionType_Not

        if not defined(__uiautomationclient_h__):
            class PropertyConditionFlags(ENUM):
                PropertyConditionFlags_None = 0x00
                PropertyConditionFlags_IgnoreCase = 0x01

            PropertyConditionFlags_None = PropertyConditionFlags.PropertyConditionFlags_None
            PropertyConditionFlags_IgnoreCase = PropertyConditionFlags.PropertyConditionFlags_IgnoreCase
        # END IF


        UiaPropertyCondition._fields_ = [
            ('PropertyId', PROPERTYID),
            ('Value', VARIANT),
            ('Flags', PropertyConditionFlags),
        ]

        UiaAndOrCondition._fields_ = [
            # ptr to array-of-ptrs to conditions
            ('ppConditions', POINTER(POINTER(UiaCondition))),
            ('cConditions', INT),
        ]

        UiaNotCondition._fields_ = [
            ('pCondition', POINTER(UiaCondition)),
        ]

        # ----------------------------------------------------------------
        # Cache request/response
        # ----------------------------------------------------------------
        if not defined(__uiautomationclient_h__):
            class AutomationElementMode(ENUM):
                AutomationElementMode_None = 1
                AutomationElementMode_Full = 2

            AutomationElementMode_None = AutomationElementMode.AutomationElementMode_None
            AutomationElementMode_Full = AutomationElementMode.AutomationElementMode_Full
        # END IF


        UiaCacheRequest._fields_ = [
            ('pViewCondition', POINTER(UiaCondition)),
            ('Scope', TreeScope),
            ('pProperties', POINTER(PROPERTYID)),
            ('cProperties', INT),
            ('pPatterns', POINTER(PATTERNID)),
            ('cPatterns', INT),
            ('automationElementMode', AutomationElementMode),
        ]


        # HRESULT WINAPI UiaHUiaNodeFromVariant(VARIANT * pvar, HUIANODE *phnode);
        UiaHUiaNodeFromVariant = uiautomationcore.UiaHUiaNodeFromVariant
        UiaHUiaNodeFromVariant.restype = HRESULT

        # HRESULT WINAPI UiaHPatternObjectFromVariant(VARIANT * pvar, HUIAPATTERNOBJECT *phobj);
        UiaHPatternObjectFromVariant = (
            uiautomationcore.UiaHPatternObjectFromVariant
        )
        UiaHPatternObjectFromVariant.restype = HRESULT

        # HRESULT WINAPI UiaHTextRangeFromVariant(VARIANT * pvar, HUIATEXTRANGE *phtextrange);
        UiaHTextRangeFromVariant = uiautomationcore.UiaHTextRangeFromVariant
        UiaHTextRangeFromVariant.restype = HRESULT
        # ----------------------------------------------------------------
        # UiaNode methods
        # ----------------------------------------------------------------
        # Used by UiaGetUpdatedCache
        class NormalizeState(ENUM):
            NormalizeState_None = 1
            NormalizeState_View = 2
            NormalizeState_Custom = 3

        NormalizeState_None = NormalizeState.NormalizeState_None
        NormalizeState_View = NormalizeState.NormalizeState_View
        NormalizeState_Custom = NormalizeState.NormalizeState_Custom
        if not defined(__uiautomationclient_h__):
            # Option groups (flags):
            # 1) Traversal order (preorder,
            # postorder): says when nodes should be tested against search
            # conditions (on enter, on leave).
            # 2) Visit order: defines in which order relatives are visited. Relatives include children
            #
            # and siblings. Visit orders are relative to parents. From the
            # child perspective First to
            # Last means 'visit the next sibling from the child' while Last to
            # First means 'visit the
            # previous sibling from the child'.
            class TreeTraversalOptions(ENUM):
                TreeTraversalOptions_Default = 0x0
                TreeTraversalOptions_PostOrder = 0x1
                TreeTraversalOptions_LastToFirstOrder = 0x2

            TreeTraversalOptions_Default = TreeTraversalOptions.TreeTraversalOptions_Default
            TreeTraversalOptions_PostOrder = TreeTraversalOptions.TreeTraversalOptions_PostOrder
            TreeTraversalOptions_LastToFirstOrder = TreeTraversalOptions.TreeTraversalOptions_LastToFirstOrder
        # END IF   __uiautomationclient_h__


        UiaFindParams._fields_ = [
            ('MaxDepth', INT),
            ('FindFirst', BOOL),
            ('ExcludeRoot', BOOL),
            ('pFindCondition', POINTER(UiaCondition)),
        ]


        # BOOL WINAPI UiaNodeRelease(HUIANODE hnode);
        UiaNodeRelease = uiautomationcore.UiaNodeRelease
        UiaNodeRelease.restype = BOOL

        # HRESULT WINAPI UiaGetPropertyValue(HUIANODE hnode, PROPERTYID propertyId, VARIANT * pValue);
        UiaGetPropertyValue = uiautomationcore.UiaGetPropertyValue
        UiaGetPropertyValue.restype = HRESULT

        # HRESULT WINAPI UiaGetPatternProvider(HUIANODE hnode, PATTERNID patternId, HUIAPATTERNOBJECT * phobj);
        UiaGetPatternProvider = uiautomationcore.UiaGetPatternProvider
        UiaGetPatternProvider.restype = HRESULT

        # HRESULT WINAPI UiaGetRuntimeId(HUIANODE hnode, SAFEARRAY ** pruntimeId);
        UiaGetRuntimeId = uiautomationcore.UiaGetRuntimeId
        UiaGetRuntimeId.restype = HRESULT

        # HRESULT WINAPI UiaSetFocus(HUIANODE hnode);
        UiaSetFocus = uiautomationcore.UiaSetFocus
        UiaSetFocus.restype = HRESULT

        # HRESULT WINAPI UiaNavigate(HUIANODE hnode, NavigateDirection direction, UiaCondition * pCondition, UiaCacheRequest * pRequest, SAFEARRAY ** ppRequestedData, BSTR * ppTreeStructure);
        UiaNavigate = uiautomationcore.UiaNavigate
        UiaNavigate.restype = HRESULT

        # HRESULT WINAPI UiaGetUpdatedCache(HUIANODE hnode, UiaCacheRequest * pRequest, NormalizeState normalizeState, UiaCondition * pNormalizeCondition, SAFEARRAY ** ppRequestedData, BSTR * ppTreeStructure);
        UiaGetUpdatedCache = uiautomationcore.UiaGetUpdatedCache
        UiaGetUpdatedCache.restype = HRESULT

        # HRESULT WINAPI UiaFind(HUIANODE hnode, UiaFindParams * pParams, UiaCacheRequest * pRequest, SAFEARRAY ** ppRequestedData, SAFEARRAY ** ppOffsets, SAFEARRAY ** ppTreeStructures);
        UiaFind = uiautomationcore.UiaFind
        UiaFind.restype = HRESULT

        # HRESULT WINAPI UiaNodeFromPoint(DOUBLE x, DOUBLE y, UiaCacheRequest * pRequest, SAFEARRAY ** ppRequestedData, BSTR * ppTreeStructure);
        UiaNodeFromPoint = uiautomationcore.UiaNodeFromPoint
        UiaNodeFromPoint.restype = HRESULT

        # HRESULT WINAPI UiaNodeFromFocus(UiaCacheRequest * pRequest, SAFEARRAY ** ppRequestedData, BSTR * ppTreeStructure);
        UiaNodeFromFocus = uiautomationcore.UiaNodeFromFocus
        UiaNodeFromFocus.restype = HRESULT

        # HRESULT WINAPI UiaNodeFromHandle(HWND hwnd, HUIANODE * phnode);
        UiaNodeFromHandle = uiautomationcore.UiaNodeFromHandle
        UiaNodeFromHandle.restype = HRESULT

        # HRESULT WINAPI UiaNodeFromProvider(IRawElementProviderSimple * pProvider, HUIANODE * phnode);
        UiaNodeFromProvider = uiautomationcore.UiaNodeFromProvider
        UiaNodeFromProvider.restype = HRESULT

        # HRESULT WINAPI UiaGetRootNode(HUIANODE * phnode);
        UiaGetRootNode = uiautomationcore.UiaGetRootNode
        UiaGetRootNode.restype = HRESULT

        if defined(__cplusplus):
            pass
        # END IF


        # ----------------------------------------------------------------
        # Client-side provider support
        # ----------------------------------------------------------------
        class ProviderType(ENUM):
            ProviderType_BaseHwnd = 1
            ProviderType_Proxy = 2
            ProviderType_NonClientArea = 3

        ProviderType_BaseHwnd = ProviderType.ProviderType_BaseHwnd
        ProviderType_Proxy = ProviderType.ProviderType_Proxy
        ProviderType_NonClientArea = ProviderType.ProviderType_NonClientArea

        # SAFEARRAY * WINAPI UiaProviderCallback(HWND hwnd, ProviderType providerType);

        UiaProviderCallback = (
            uiautomationcore.UiaProviderCallback
        )
        UiaProviderCallback.restype = SAFEARRAY

        # VOID WINAPI UiaRegisterProviderCallback(UiaProviderCallback * pCallback);
        UiaRegisterProviderCallback = (
            uiautomationcore.UiaRegisterProviderCallback
        )
        UiaRegisterProviderCallback.restype = VOID
        # ----------------------------------------------------------------
        # Identifier mapping
        # ----------------------------------------------------------------
        class AutomationIdentifierType(ENUM):
            AutomationIdentifierType_Property = 1
            AutomationIdentifierType_Pattern = 2
            AutomationIdentifierType_Event = 3
            AutomationIdentifierType_ControlType = 4
            AutomationIdentifierType_TextAttribute = 5
            AutomationIdentifierType_LandmarkType = 6
            AutomationIdentifierType_Annotation = 7
            AutomationIdentifierType_Changes = 8
            AutomationIdentifierType_Style = 9

        AutomationIdentifierType_Property = AutomationIdentifierType.AutomationIdentifierType_Property
        AutomationIdentifierType_Pattern = AutomationIdentifierType.AutomationIdentifierType_Pattern
        AutomationIdentifierType_Event = AutomationIdentifierType.AutomationIdentifierType_Event
        AutomationIdentifierType_ControlType = AutomationIdentifierType.AutomationIdentifierType_ControlType
        AutomationIdentifierType_TextAttribute = AutomationIdentifierType.AutomationIdentifierType_TextAttribute
        AutomationIdentifierType_LandmarkType = AutomationIdentifierType.AutomationIdentifierType_LandmarkType
        AutomationIdentifierType_Annotation = AutomationIdentifierType.AutomationIdentifierType_Annotation
        AutomationIdentifierType_Changes = AutomationIdentifierType.AutomationIdentifierType_Changes
        AutomationIdentifierType_Style = AutomationIdentifierType.AutomationIdentifierType_Style


        # INT WINAPI UiaLookupId(AutomationIdentifierType type, GUID* pGuid);
        UiaLookupId = uiautomationcore.UiaLookupId
        UiaLookupId.restype = INT
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE


        # HRESULT WINAPI UiaGetReservedNotSupportedValue(IUnknown **punkNotSupportedValue);
        UiaGetReservedNotSupportedValue = (
            uiautomationcore.UiaGetReservedNotSupportedValue
        )
        UiaGetReservedNotSupportedValue.restype = HRESULT

        # HRESULT WINAPI UiaGetReservedMixedAttributeValue(IUnknown **punkMixedAttributeValue);
        UiaGetReservedMixedAttributeValue = (
            uiautomationcore.UiaGetReservedMixedAttributeValue
        )
        UiaGetReservedMixedAttributeValue.restype = HRESULT

        # ----------------------------------------------------------------
        # Event methods
        # ----------------------------------------------------------------
        # Event structs and enums
        class EventArgsType(ENUM):
            EventArgsType_Simple = 1
            EventArgsType_PropertyChanged = 2
            EventArgsType_StructureChanged = 3
            EventArgsType_AsyncContentLoaded = 4
            EventArgsType_WindowClosed = 5
            EventArgsType_TextEditTextChanged = 6
            EventArgsType_Changes = 7
            EventArgsType_Notification = 8

        EventArgsType_Simple = EventArgsType.EventArgsType_Simple
        EventArgsType_PropertyChanged = EventArgsType.EventArgsType_PropertyChanged
        EventArgsType_StructureChanged = EventArgsType.EventArgsType_StructureChanged
        EventArgsType_AsyncContentLoaded = EventArgsType.EventArgsType_AsyncContentLoaded
        EventArgsType_WindowClosed = EventArgsType.EventArgsType_WindowClosed
        EventArgsType_TextEditTextChanged = EventArgsType.EventArgsType_TextEditTextChanged
        EventArgsType_Changes = EventArgsType.EventArgsType_Changes
        EventArgsType_Notification = EventArgsType.EventArgsType_Notification


        class AsyncContentLoadedState(ENUM):
            AsyncContentLoadedState_Beginning = 1
            AsyncContentLoadedState_Progress = 2
            AsyncContentLoadedState_Completed = 3

        AsyncContentLoadedState_Beginning = AsyncContentLoadedState.AsyncContentLoadedState_Beginning
        AsyncContentLoadedState_Progress = AsyncContentLoadedState.AsyncContentLoadedState_Progress
        AsyncContentLoadedState_Completed = AsyncContentLoadedState.AsyncContentLoadedState_Completed

        UiaEventArgs._fields_ = [
            ('Type', EventArgsType),
            ('EventId', INT),
        ]

        UiaPropertyChangedEventArgs._fields_ = [
            ('Type', EventArgsType),
            ('EventId', INT),
            ('PropertyId', PROPERTYID),
            ('OldValue', VARIANT),
            ('NewValue', VARIANT),
        ]

        UiaStructureChangedEventArgs._fields_ = [
            ('Type', EventArgsType),
            ('EventId', INT),
            ('pRuntimeId', POINTER(INT)),
            ('cRuntimeIdLen', INT),
        ]

        UiaTextEditTextChangedEventArgs._fields_ = [
            ('Type', EventArgsType),
            ('EventId', INT),
            ('pTextChange', POINTER(SAFEARRAY)),
        ]

        UiaChangesEventArgs._fields_ = [
            ('Type', EventArgsType),
            ('EventId', INT),
            ('EventIdCount', INT),
            ('pUiaChanges', POINTER(UiaChangeInfo)),
        ]

        UiaAsyncContentLoadedEventArgs._fields_ = [
            ('Type', EventArgsType),
            ('EventId', INT),
            ('PercentComplete', DOUBLE),
        ]

        UiaWindowClosedEventArgs._fields_ = [
            ('Type', EventArgsType),
            ('EventId', INT),
            ('pRuntimeId', POINTER(INT)),
            ('cRuntimeIdLen', INT),
        ]


        # Provider Event APIs
        # HRESULT WINAPI UiaRaiseAutomationPropertyChangedEvent(IRawElementProviderSimple * pProvider, PROPERTYID id, VARIANT oldValue, VARIANT newValue);
        UiaRaiseAutomationPropertyChangedEvent = (
            uiautomationcore.UiaRaiseAutomationPropertyChangedEvent
        )
        UiaRaiseAutomationPropertyChangedEvent.restype = HRESULT

        # HRESULT WINAPI UiaRaiseAutomationEvent(IRawElementProviderSimple * pProvider, EVENTID id);
        UiaRaiseAutomationEvent = uiautomationcore.UiaRaiseAutomationEvent
        UiaRaiseAutomationEvent.restype = HRESULT

        # HRESULT WINAPI UiaRaiseStructureChangedEvent(IRawElementProviderSimple * pProvider, StructureChangeType structureChangeType, INT * pRuntimeId, INT cRuntimeIdLen);
        UiaRaiseStructureChangedEvent = (
            uiautomationcore.UiaRaiseStructureChangedEvent
        )
        UiaRaiseStructureChangedEvent.restype = HRESULT

        # HRESULT WINAPI UiaRaiseAsyncContentLoadedEvent(IRawElementProviderSimple * pProvider, AsyncContentLoadedState asyncContentLoadedState, DOUBLE percentComplete);
        UiaRaiseAsyncContentLoadedEvent = (
            uiautomationcore.UiaRaiseAsyncContentLoadedEvent
        )
        UiaRaiseAsyncContentLoadedEvent.restype = HRESULT
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE


        # HRESULT WINAPI UiaRaiseTextEditTextChangedEvent(IRawElementProviderSimple * pProvider, TextEditChangeType textEditChangeType, SAFEARRAY *pChangedData);
        UiaRaiseTextEditTextChangedEvent = (
            uiautomationcore.UiaRaiseTextEditTextChangedEvent
        )
        UiaRaiseTextEditTextChangedEvent.restype = HRESULT

        # HRESULT WINAPI UiaRaiseChangesEvent(IRawElementProviderSimple * pProvider, INT eventIdCount, struct UiaChangeInfo * pUiaChanges);
        UiaRaiseChangesEvent = uiautomationcore.UiaRaiseChangesEvent
        UiaRaiseChangesEvent.restype = HRESULT

        # HRESULT WINAPI UiaRaiseNotificationEvent(
        # _In_ IRawElementProviderSimple* provider,
        # NotificationKind notificationKind,
        # NotificationProcessing notificationProcessing,
        # _In_opt_ BSTR displayString,
        # _In_ BSTR activityId);
        UiaRaiseNotificationEvent = uiautomationcore.UiaRaiseNotificationEvent
        UiaRaiseNotificationEvent.restype = HRESULT
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE

        # Client Event APIs
        # VOID WINAPI UiaEventCallback(UiaEventArgs * pArgs, SAFEARRAY * pRequestedData, BSTR pTreeStructure);
        UiaAddEvent = uiautomationcore.UiaEventCallback
        UiaAddEvent.restype = VOID

        # HRESULT WINAPI UiaAddEvent(HUIANODE hnode, EVENTID eventId, UiaEventCallback * pCallback, TreeScope scope, PROPERTYID * pProperties, INT cProperties, UiaCacheRequest * pRequest, HUIAEVENT * phEvent);
        UiaAddEvent = uiautomationcore.UiaAddEvent
        UiaAddEvent.restype = HRESULT

        # HRESULT WINAPI UiaRemoveEvent(HUIAEVENT hEvent);
        UiaRemoveEvent = uiautomationcore.UiaRemoveEvent
        UiaRemoveEvent.restype = HRESULT

        # HRESULT WINAPI UiaEventAddWindow(HUIAEVENT hEvent, HWND hwnd);
        UiaEventAddWindow = uiautomationcore.UiaEventAddWindow
        UiaEventAddWindow.restype = HRESULT

        # HRESULT WINAPI UiaEventRemoveWindow(HUIAEVENT hEvent, HWND hwnd);
        UiaEventRemoveWindow = uiautomationcore.UiaEventRemoveWindow
        UiaEventRemoveWindow.restype = HRESULT

        # ----------------------------------------------------------------
        # Pattern methods
        # ----------------------------------------------------------------
        # HRESULT WINAPI DockPattern_SetDockPosition(HUIAPATTERNOBJECT hobj, DockPosition dockPosition);
        DockPattern_SetDockPosition = (
            uiautomationcore.DockPattern_SetDockPosition
        )
        DockPattern_SetDockPosition.restype = HRESULT

        # HRESULT WINAPI ExpandCollapsePattern_Collapse(HUIAPATTERNOBJECT hobj);
        ExpandCollapsePattern_Collapse = (
            uiautomationcore.ExpandCollapsePattern_Collapse
        )
        ExpandCollapsePattern_Collapse.restype = HRESULT

        # HRESULT WINAPI ExpandCollapsePattern_Expand(HUIAPATTERNOBJECT hobj);
        ExpandCollapsePattern_Expand = (
            uiautomationcore.ExpandCollapsePattern_Expand
        )
        ExpandCollapsePattern_Expand.restype = HRESULT

        # HRESULT WINAPI GridPattern_GetItem(HUIAPATTERNOBJECT hobj, INT row, INT column, HUIANODE * pResult);
        GridPattern_GetItem = uiautomationcore.GridPattern_GetItem
        GridPattern_GetItem.restype = HRESULT

        # HRESULT WINAPI InvokePattern_Invoke(HUIAPATTERNOBJECT hobj);
        InvokePattern_Invoke = uiautomationcore.InvokePattern_Invoke
        InvokePattern_Invoke.restype = HRESULT

        # HRESULT WINAPI MultipleViewPattern_GetViewName(HUIAPATTERNOBJECT hobj, INT viewId, BSTR * ppStr);
        MultipleViewPattern_GetViewName = (
            uiautomationcore.MultipleViewPattern_GetViewName
        )
        MultipleViewPattern_GetViewName.restype = HRESULT

        # HRESULT WINAPI MultipleViewPattern_SetCurrentView(HUIAPATTERNOBJECT hobj, INT viewId);
        MultipleViewPattern_SetCurrentView = (
            uiautomationcore.MultipleViewPattern_SetCurrentView
        )
        MultipleViewPattern_SetCurrentView.restype = HRESULT

        # HRESULT WINAPI RangeValuePattern_SetValue(HUIAPATTERNOBJECT hobj, DOUBLE val);
        RangeValuePattern_SetValue = (
            uiautomationcore.RangeValuePattern_SetValue
        )
        RangeValuePattern_SetValue.restype = HRESULT

        # HRESULT WINAPI ScrollItemPattern_ScrollIntoView(HUIAPATTERNOBJECT hobj);
        ScrollItemPattern_ScrollIntoView = (
            uiautomationcore.ScrollItemPattern_ScrollIntoView
        )
        ScrollItemPattern_ScrollIntoView.restype = HRESULT

        # HRESULT WINAPI ScrollPattern_Scroll(HUIAPATTERNOBJECT hobj, ScrollAmount horizontalAmount, ScrollAmount verticalAmount);
        ScrollPattern_Scroll = uiautomationcore.ScrollPattern_Scroll
        ScrollPattern_Scroll.restype = HRESULT

        # HRESULT WINAPI ScrollPattern_SetScrollPercent(HUIAPATTERNOBJECT hobj, DOUBLE horizontalPercent, DOUBLE verticalPercent);
        ScrollPattern_SetScrollPercent = (
            uiautomationcore.ScrollPattern_SetScrollPercent
        )
        ScrollPattern_SetScrollPercent.restype = HRESULT

        # HRESULT WINAPI SelectionItemPattern_AddToSelection(HUIAPATTERNOBJECT hobj);
        SelectionItemPattern_AddToSelection = (
            uiautomationcore.SelectionItemPattern_AddToSelection
        )
        SelectionItemPattern_AddToSelection.restype = HRESULT

        # HRESULT WINAPI SelectionItemPattern_RemoveFromSelection(HUIAPATTERNOBJECT hobj);
        SelectionItemPattern_RemoveFromSelection = (
            uiautomationcore.SelectionItemPattern_RemoveFromSelection
        )
        SelectionItemPattern_RemoveFromSelection.restype = HRESULT

        # HRESULT WINAPI SelectionItemPattern_Select(HUIAPATTERNOBJECT hobj);
        SelectionItemPattern_Select = (
            uiautomationcore.SelectionItemPattern_Select
        )
        SelectionItemPattern_Select.restype = HRESULT

        # HRESULT WINAPI TogglePattern_Toggle(HUIAPATTERNOBJECT hobj);
        TogglePattern_Toggle = uiautomationcore.TogglePattern_Toggle
        TogglePattern_Toggle.restype = HRESULT

        # HRESULT WINAPI TransformPattern_Move(HUIAPATTERNOBJECT hobj, DOUBLE x, DOUBLE y);
        TransformPattern_Move = uiautomationcore.TransformPattern_Move
        TransformPattern_Move.restype = HRESULT

        # HRESULT WINAPI TransformPattern_Resize(HUIAPATTERNOBJECT hobj, DOUBLE width, DOUBLE height);
        TransformPattern_Resize = uiautomationcore.TransformPattern_Resize
        TransformPattern_Resize.restype = HRESULT

        # HRESULT WINAPI TransformPattern_Rotate(HUIAPATTERNOBJECT hobj, DOUBLE degrees);
        TransformPattern_Rotate = uiautomationcore.TransformPattern_Rotate
        TransformPattern_Rotate.restype = HRESULT

        # HRESULT WINAPI ValuePattern_SetValue(HUIAPATTERNOBJECT hobj, LPCWSTR pVal);
        ValuePattern_SetValue = uiautomationcore.ValuePattern_SetValue
        ValuePattern_SetValue.restype = HRESULT

        # HRESULT WINAPI WindowPattern_Close(HUIAPATTERNOBJECT hobj);
        WindowPattern_Close = uiautomationcore.WindowPattern_Close
        WindowPattern_Close.restype = HRESULT

        # HRESULT WINAPI WindowPattern_SetWindowVisualState(HUIAPATTERNOBJECT hobj, WindowVisualState state);
        WindowPattern_SetWindowVisualState = (
            uiautomationcore.WindowPattern_SetWindowVisualState
        )
        WindowPattern_SetWindowVisualState.restype = HRESULT

        # HRESULT WINAPI WindowPattern_WaitForInputIdle(HUIAPATTERNOBJECT hobj, INT milliseconds, BOOL * pResult);
        WindowPattern_WaitForInputIdle = (
            uiautomationcore.WindowPattern_WaitForInputIdle
        )
        WindowPattern_WaitForInputIdle.restype = HRESULT

        # HRESULT WINAPI TextPattern_GetSelection(HUIAPATTERNOBJECT hobj, SAFEARRAY** pRetVal);
        TextPattern_GetSelection = uiautomationcore.TextPattern_GetSelection
        TextPattern_GetSelection.restype = HRESULT

        # HRESULT WINAPI TextPattern_GetVisibleRanges(HUIAPATTERNOBJECT hobj, SAFEARRAY** pRetVal);
        TextPattern_GetVisibleRanges = (
            uiautomationcore.TextPattern_GetVisibleRanges
        )
        TextPattern_GetVisibleRanges.restype = HRESULT

        # HRESULT WINAPI TextPattern_RangeFromChild(HUIAPATTERNOBJECT hobj, HUIANODE hnodeChild, HUIATEXTRANGE* pRetVal);
        TextPattern_RangeFromChild = (
            uiautomationcore.TextPattern_RangeFromChild
        )
        TextPattern_RangeFromChild.restype = HRESULT

        # HRESULT WINAPI TextPattern_RangeFromPoint(HUIAPATTERNOBJECT hobj, UiaPoint point, HUIATEXTRANGE* pRetVal);
        TextPattern_RangeFromPoint = (
            uiautomationcore.TextPattern_RangeFromPoint
        )
        TextPattern_RangeFromPoint.restype = HRESULT

        # HRESULT WINAPI TextPattern_get_DocumentRange(HUIAPATTERNOBJECT hobj, HUIATEXTRANGE* pRetVal);
        TextPattern_get_DocumentRange = (
            uiautomationcore.TextPattern_get_DocumentRange
        )
        TextPattern_get_DocumentRange.restype = HRESULT

        # HRESULT WINAPI TextPattern_get_SupportedTextSelection(HUIAPATTERNOBJECT hobj, SupportedTextSelection* pRetVal);
        TextPattern_get_SupportedTextSelection = (
            uiautomationcore.TextPattern_get_SupportedTextSelection
        )
        TextPattern_get_SupportedTextSelection.restype = HRESULT

        # HRESULT WINAPI TextRange_Clone(HUIATEXTRANGE hobj, HUIATEXTRANGE* pRetVal);
        TextRange_Clone = uiautomationcore.TextRange_Clone
        TextRange_Clone.restype = HRESULT

        # HRESULT WINAPI TextRange_Compare(HUIATEXTRANGE hobj, HUIATEXTRANGE range, BOOL* pRetVal);
        TextRange_Compare = uiautomationcore.TextRange_Compare
        TextRange_Compare.restype = HRESULT

        # HRESULT WINAPI TextRange_CompareEndpoints(HUIATEXTRANGE hobj, TextPatternRangeEndpoint endpoint, HUIATEXTRANGE targetRange, TextPatternRangeEndpoint targetEndpoint, int* pRetVal);
        TextRange_CompareEndpoints = (
            uiautomationcore.TextRange_CompareEndpoints
        )
        TextRange_CompareEndpoints.restype = HRESULT

        # HRESULT WINAPI TextRange_ExpandToEnclosingUnit(HUIATEXTRANGE hobj, TextUnit unit);
        TextRange_ExpandToEnclosingUnit = (
            uiautomationcore.TextRange_ExpandToEnclosingUnit
        )
        TextRange_ExpandToEnclosingUnit.restype = HRESULT

        # HRESULT WINAPI TextRange_GetAttributeValue(HUIATEXTRANGE hobj, TEXTATTRIBUTEID attributeId, VARIANT * pRetVal);
        TextRange_GetAttributeValue = (
            uiautomationcore.TextRange_GetAttributeValue
        )
        TextRange_GetAttributeValue.restype = HRESULT

        # HRESULT WINAPI TextRange_FindAttribute(HUIATEXTRANGE hobj, TEXTATTRIBUTEID attributeId, VARIANT val, BOOL backward, HUIATEXTRANGE * pRetVal);
        TextRange_FindAttribute = uiautomationcore.TextRange_FindAttribute
        TextRange_FindAttribute.restype = HRESULT

        # HRESULT WINAPI TextRange_FindText(HUIATEXTRANGE hobj, BSTR text, BOOL backward, BOOL ignoreCase, HUIATEXTRANGE* pRetVal);
        TextRange_FindText = uiautomationcore.TextRange_FindText
        TextRange_FindText.restype = HRESULT

        # HRESULT WINAPI TextRange_GetBoundingRectangles(HUIATEXTRANGE hobj, SAFEARRAY** pRetVal);
        TextRange_GetBoundingRectangles = (
            uiautomationcore.TextRange_GetBoundingRectangles
        )
        TextRange_GetBoundingRectangles.restype = HRESULT

        # HRESULT WINAPI TextRange_GetEnclosingElement(HUIATEXTRANGE hobj, HUIANODE* pRetVal);
        TextRange_GetEnclosingElement = (
            uiautomationcore.TextRange_GetEnclosingElement
        )
        TextRange_GetEnclosingElement.restype = HRESULT

        # HRESULT WINAPI TextRange_GetText(HUIATEXTRANGE hobj, INT maxLength, BSTR* pRetVal);
        TextRange_GetText = uiautomationcore.TextRange_GetText
        TextRange_GetText.restype = HRESULT

        # HRESULT WINAPI TextRange_Move(HUIATEXTRANGE hobj, TextUnit unit, INT count, int* pRetVal);
        TextRange_Move = uiautomationcore.TextRange_Move
        TextRange_Move.restype = HRESULT

        # HRESULT WINAPI TextRange_MoveEndpointByUnit(HUIATEXTRANGE hobj, TextPatternRangeEndpoint endpoint, TextUnit unit, INT count, int* pRetVal);
        TextRange_MoveEndpointByUnit = (
            uiautomationcore.TextRange_MoveEndpointByUnit
        )
        TextRange_MoveEndpointByUnit.restype = HRESULT

        # HRESULT WINAPI TextRange_MoveEndpointByRange(HUIATEXTRANGE hobj, TextPatternRangeEndpoint endpoint, HUIATEXTRANGE targetRange, TextPatternRangeEndpoint targetEndpoint);
        TextRange_MoveEndpointByRange = (
            uiautomationcore.TextRange_MoveEndpointByRange
        )
        TextRange_MoveEndpointByRange.restype = HRESULT

        # HRESULT WINAPI TextRange_Select(HUIATEXTRANGE hobj);
        TextRange_Select = uiautomationcore.TextRange_Select
        TextRange_Select.restype = HRESULT

        # HRESULT WINAPI TextRange_AddToSelection(HUIATEXTRANGE hobj);
        TextRange_AddToSelection = uiautomationcore.TextRange_AddToSelection
        TextRange_AddToSelection.restype = HRESULT

        # HRESULT WINAPI TextRange_RemoveFromSelection(HUIATEXTRANGE hobj);
        TextRange_RemoveFromSelection = (
            uiautomationcore.TextRange_RemoveFromSelection
        )
        TextRange_RemoveFromSelection.restype = HRESULT

        # HRESULT WINAPI TextRange_ScrollIntoView(HUIATEXTRANGE hobj, BOOL alignToTop);
        TextRange_ScrollIntoView = uiautomationcore.TextRange_ScrollIntoView
        TextRange_ScrollIntoView.restype = HRESULT

        # HRESULT WINAPI TextRange_GetChildren(HUIATEXTRANGE hobj, SAFEARRAY** pRetVal);
        TextRange_GetChildren = uiautomationcore.TextRange_GetChildren
        TextRange_GetChildren.restype = HRESULT

        # HRESULT WINAPI ItemContainerPattern_FindItemByProperty(HUIAPATTERNOBJECT hobj, HUIANODE hnodeStartAfter, PROPERTYID propertyId, VARIANT value, HUIANODE *pFound);
        ItemContainerPattern_FindItemByProperty = (
            uiautomationcore.ItemContainerPattern_FindItemByProperty
        )
        ItemContainerPattern_FindItemByProperty.restype = HRESULT

        # HRESULT WINAPI LegacyIAccessiblePattern_Select(HUIAPATTERNOBJECT hobj, LONG flagsSelect);
        LegacyIAccessiblePattern_Select = (
            uiautomationcore.LegacyIAccessiblePattern_Select
        )
        LegacyIAccessiblePattern_Select.restype = HRESULT

        # HRESULT WINAPI LegacyIAccessiblePattern_DoDefaultAction(HUIAPATTERNOBJECT hobj);
        LegacyIAccessiblePattern_DoDefaultAction = (
            uiautomationcore.LegacyIAccessiblePattern_DoDefaultAction
        )
        LegacyIAccessiblePattern_DoDefaultAction.restype = HRESULT

        # HRESULT WINAPI LegacyIAccessiblePattern_SetValue(HUIAPATTERNOBJECT hobj, LPCWSTR szValue);
        LegacyIAccessiblePattern_SetValue = (
            uiautomationcore.LegacyIAccessiblePattern_SetValue
        )
        LegacyIAccessiblePattern_SetValue.restype = HRESULT

        # HRESULT WINAPI LegacyIAccessiblePattern_GetIAccessible(HUIAPATTERNOBJECT hobj, IAccessible ** pAccessible);
        LegacyIAccessiblePattern_GetIAccessible = (
            uiautomationcore.LegacyIAccessiblePattern_GetIAccessible
        )
        LegacyIAccessiblePattern_GetIAccessible.restype = HRESULT

        # HRESULT WINAPI SynchronizedInputPattern_StartListening(HUIAPATTERNOBJECT hobj, SynchronizedInputType inputType);
        SynchronizedInputPattern_StartListening = (
            uiautomationcore.SynchronizedInputPattern_StartListening
        )
        SynchronizedInputPattern_StartListening.restype = HRESULT

        # HRESULT WINAPI SynchronizedInputPattern_Cancel(HUIAPATTERNOBJECT hobj);
        SynchronizedInputPattern_Cancel = (
            uiautomationcore.SynchronizedInputPattern_Cancel
        )
        SynchronizedInputPattern_Cancel.restype = HRESULT

        # HRESULT WINAPI VirtualizedItemPattern_Realize(HUIAPATTERNOBJECT hobj);
        VirtualizedItemPattern_Realize = (
            uiautomationcore.VirtualizedItemPattern_Realize
        )
        VirtualizedItemPattern_Realize.restype = HRESULT

        # BOOL WINAPI UiaPatternRelease(HUIAPATTERNOBJECT hobj);
        UiaPatternRelease = uiautomationcore.UiaPatternRelease
        UiaPatternRelease.restype = BOOL

        # BOOL WINAPI UiaTextRangeRelease(HUIATEXTRANGE hobj);
        UiaTextRangeRelease = uiautomationcore.UiaTextRangeRelease
        UiaTextRangeRelease.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        # ----------------------------------------------------------------
        # Provider methods
        # ----------------------------------------------------------------
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE


        # LRESULT WINAPI UiaReturnRawElementProvider(HWND hwnd, WPARAM wParam, LPARAM lParam, IRawElementProviderSimple * el);
        UiaReturnRawElementProvider = (
            uiautomationcore.UiaReturnRawElementProvider
        )
        UiaReturnRawElementProvider.restype = LRESULT

        # HRESULT WINAPI UiaHostProviderFromHwnd(HWND hwnd, IRawElementProviderSimple ** ppProvider);
        UiaHostProviderFromHwnd = uiautomationcore.UiaHostProviderFromHwnd
        UiaHostProviderFromHwnd.restype = HRESULT

        # HRESULT WINAPI UiaProviderForNonClient(HWND hwnd, LONG idObject, LONG idChild, IRawElementProviderSimple ** ppProvider);
        UiaProviderForNonClient = uiautomationcore.UiaProviderForNonClient
        UiaProviderForNonClient.restype = HRESULT

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        UIA_IAFP_DEFAULT = 0x0000


        UIA_IAFP_UNWRAP_BRIDGE = 0x0001
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE


        # HRESULT WINAPI UiaIAccessibleFromProvider(
        # _In_ IRawElementProviderSimple * pProvider,
        # _In_ DWORD dwFlags,
        # _Outptr_ IAccessible ** ppAccessible,
        # _Out_ VARIANT* pvarChild);
        UiaIAccessibleFromProvider = (
            uiautomationcore.UiaIAccessibleFromProvider
        )
        UiaIAccessibleFromProvider.restype = HRESULT

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP):
        UIA_PFIA_DEFAULT = 0x0000


        UIA_PFIA_UNWRAP_BRIDGE = 0x0001
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE


        # HRESULT WINAPI UiaProviderFromIAccessible(
        # _In_ IAccessible * pAccessible,
        # LONG idChild,
        # _In_ DWORD dwFlags,
        # _Outptr_ IRawElementProviderSimple ** ppProvider);
        UiaProviderFromIAccessible = (
            uiautomationcore.UiaProviderFromIAccessible
        )
        UiaProviderFromIAccessible.restype = HRESULT

        # ----------------------------------------------------------------
        # Provider Explicit Cleanup methods
        # ----------------------------------------------------------------
        # HRESULT WINAPI UiaDisconnectProvider(IRawElementProviderSimple * pProvider);
        UiaDisconnectProvider = uiautomationcore.UiaDisconnectProvider
        UiaDisconnectProvider.restype = HRESULT
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # ----------------------------------------------------------------
        # Other APIs...
        # ----------------------------------------------------------------
        uiautomationcore = ctypes.windll.UIAUTOMATIONCORE

        # BOOL WINAPI UiaHasServerSideProvider(HWND hwnd);
        UiaHasServerSideProvider = uiautomationcore.UiaHasServerSideProvider
        UiaHasServerSideProvider.restype = BOOL

    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF

# END IF   not _INC_UIAUTOMATIONCOREAPI


