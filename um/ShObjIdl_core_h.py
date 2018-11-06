import comtypes
__cplusplus = None
CINTERFACE = 1


def defined(value):
    return value is not None


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
    __REQUIRED_RPCNDR_H_VERSION__ = 500
# END IF

# verify that the <rpcsal.h> version is high enough to compile this file

if not defined(__REQUIRED_RPCSAL_H_VERSION__):
    __REQUIRED_RPCSAL_H_VERSION__ = 100
# END IF

if not defined(__RPCNDR_H_VERSION__):
    pass
# END IF  __RPCNDR_H_VERSION__
if not defined(COM_NO_WINDOWS_H):
    pass
# END IF  COM_NO_WINDOWS_H
if not defined(__shobjidl_core_h__):
    __shobjidl_core_h__ = 1

    if defined(_MSC_VER) and (_MSC_VER >= 1020):
        pass
    # END IF

    # Forward Declarations
    if not defined(__IContextMenu_FWD_DEFINED__):
        __IContextMenu_FWD_DEFINED__ = 1
        IID_IContextMenu = MIDL_INTERFACE(
            "{000214E4-0000-0000-C000-000000000046)//IID_ICONTEXTMEN}"
        )
        
        
        class IContextMenu(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IContextMenu


    # END IF  __IContextMenu_FWD_DEFINED__

    if not defined(__IContextMenu2_FWD_DEFINED__):
        __IContextMenu2_FWD_DEFINED__ = 1
        IID_IContextMenu2 = MIDL_INTERFACE(
            "{000214F4-0000-0000-C000-000000000046)//IID_ICONTEXTMENU}"
        )
        
        
        class IContextMenu2(IContextMenu):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IContextMenu2


    # END IF  __IContextMenu2_FWD_DEFINED__

    if not defined(__IContextMenu3_FWD_DEFINED__):
        __IContextMenu3_FWD_DEFINED__ = 1
        IID_IContextMenu3 = MIDL_INTERFACE(
            "{BCFCE0A0-EC17-11D0-8D10-00A0C90F2719)//IID_ICONTEXTMENU}"
        )
        
        
        class IContextMenu3(IContextMenu2):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IContextMenu3


    # END IF  __IContextMenu3_FWD_DEFINED__

    if not defined(__IExecuteCommand_FWD_DEFINED__):
        __IExecuteCommand_FWD_DEFINED__ = 1
        IID_IExecuteCommand = MIDL_INTERFACE(
            "{7F9185B0-CB92-43C5-80A9-92277A4F7B54}"
        )
        
        
        class IExecuteCommand(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExecuteCommand


    # END IF  __IExecuteCommand_FWD_DEFINED__

    if not defined(__IPersistFolder_FWD_DEFINED__):
        __IPersistFolder_FWD_DEFINED__ = 1
        IID_IPersistFolder = MIDL_INTERFACE(
            "{000214EA-0000-0000-C000-000000000046)//IID_IPERSISTFOLDE}"
        )
        
        
        class IPersistFolder(IPersist):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPersistFolder


    # END IF  __IPersistFolder_FWD_DEFINED__

    if not defined(__IRunnableTask_FWD_DEFINED__):
        __IRunnableTask_FWD_DEFINED__ = 1
        IID_IRunnableTask = MIDL_INTERFACE(
            "{85788D00-6807-11D0-B810-00C04FD706EC)//IID_IRUNNABLETAS}"
        )
        
        
        class IRunnableTask(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IRunnableTask


    # END IF  __IRunnableTask_FWD_DEFINED__

    if not defined(__IShellTaskScheduler_FWD_DEFINED__):
        __IShellTaskScheduler_FWD_DEFINED__ = 1
        IID_IShellTaskScheduler = MIDL_INTERFACE(
            "{6CCB7BE0-6807-11D0-B810-00C04FD706EC}"
        )
        
        
        class IShellTaskScheduler(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellTaskScheduler


    # END IF  __IShellTaskScheduler_FWD_DEFINED__

    if not defined(__IPersistFolder2_FWD_DEFINED__):
        __IPersistFolder2_FWD_DEFINED__ = 1
        IID_IPersistFolder2 = MIDL_INTERFACE(
            "{1AC3D9F0-175C-11D1-95BE-00609797EA4F)//IID_IPERSISTFOLDER}"
        )
        
        
        class IPersistFolder2(IPersistFolder):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPersistFolder2


    # END IF  __IPersistFolder2_FWD_DEFINED__

    if not defined(__IPersistFolder3_FWD_DEFINED__):
        __IPersistFolder3_FWD_DEFINED__ = 1
        IID_IPersistFolder3 = MIDL_INTERFACE(
            "{CEF04FDF-FE72-11D2-87A5-00C04F6837CF)//IID_IPERSISTFOLDER}"
        )
        
        
        class IPersistFolder3(IPersistFolder2):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPersistFolder3


    # END IF  __IPersistFolder3_FWD_DEFINED__

    if not defined(__IPersistIDList_FWD_DEFINED__):
        __IPersistIDList_FWD_DEFINED__ = 1
        IID_IPersistIDList = MIDL_INTERFACE(
            "{1079ACFC-29BD-11D3-8E0D-00C04F6837D5)//IID_IPERSISTIDLIS}"
        )
        
        
        class IPersistIDList(IPersist):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPersistIDList


    # END IF  __IPersistIDList_FWD_DEFINED__

    if not defined(__IEnumIDList_FWD_DEFINED__):
        __IEnumIDList_FWD_DEFINED__ = 1
        IID_IEnumIDList = MIDL_INTERFACE(
            "{000214F2-0000-0000-C000-000000000046}"
        )
        
        
        class IEnumIDList(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumIDList


    # END IF  __IEnumIDList_FWD_DEFINED__

    if not defined(__IEnumFullIDList_FWD_DEFINED__):
        __IEnumFullIDList_FWD_DEFINED__ = 1
        IID_IEnumFullIDList = MIDL_INTERFACE(
            "{D0191542-7954-4908-BC06-B2360BBE45BA}"
        )
        
        
        class IEnumFullIDList(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumFullIDList


    # END IF  __IEnumFullIDList_FWD_DEFINED__

    if not defined(__IFileSyncMergeHandler_FWD_DEFINED__):
        __IFileSyncMergeHandler_FWD_DEFINED__ = 1
        IID_IFileSyncMergeHandler = MIDL_INTERFACE(
            "{D97B5AAC-C792-433C-975D-35C4EADC7A9D}"
        )
        
        
        class IFileSyncMergeHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileSyncMergeHandler


    # END IF  __IFileSyncMergeHandler_FWD_DEFINED__

    if not defined(__IObjectWithFolderEnumMode_FWD_DEFINED__):
        __IObjectWithFolderEnumMode_FWD_DEFINED__ = 1
        IID_IObjectWithFolderEnumMode = MIDL_INTERFACE(
            "{6A9D9026-0E6E-464C-B000-42ECC07DE673}"
        )
        
        
        class IObjectWithFolderEnumMode(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IObjectWithFolderEnumMode


    # END IF  __IObjectWithFolderEnumMode_FWD_DEFINED__

    if not defined(__IParseAndCreateItem_FWD_DEFINED__):
        __IParseAndCreateItem_FWD_DEFINED__ = 1
        IID_IParseAndCreateItem = MIDL_INTERFACE(
            "{67EFED0E-E827-4408-B493-78F3982B685C}"
        )
        
        
        class IParseAndCreateItem(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IParseAndCreateItem


    # END IF  __IParseAndCreateItem_FWD_DEFINED__

    if not defined(__IShellFolder_FWD_DEFINED__):
        __IShellFolder_FWD_DEFINED__ = 1
        IID_IShellFolder = MIDL_INTERFACE(
            "{000214E6-0000-0000-C000-000000000046}"
        )
        
        
        class IShellFolder(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellFolder


    # END IF  __IShellFolder_FWD_DEFINED__

    if not defined(__IEnumExtraSearch_FWD_DEFINED__):
        __IEnumExtraSearch_FWD_DEFINED__ = 1
        IID_IEnumExtraSearch = MIDL_INTERFACE(
            "{0E700BE1-9DB6-11D1-A1CE-00C04FD75D13}"
        )
        
        
        class IEnumExtraSearch(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumExtraSearch


    # END IF  __IEnumExtraSearch_FWD_DEFINED__

    if not defined(__IShellFolder2_FWD_DEFINED__):
        __IShellFolder2_FWD_DEFINED__ = 1
        IID_IShellFolder2 = MIDL_INTERFACE(
            "{93F2F68C-1D1B-11D3-A30E-00C04F79ABD1}"
        )
        
        
        class IShellFolder2(IShellFolder):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellFolder2


    # END IF  __IShellFolder2_FWD_DEFINED__

    if not defined(__IShellView_FWD_DEFINED__):
        __IShellView_FWD_DEFINED__ = 1
        IID_IShellView = MIDL_INTERFACE(
            "{000214E3-0000-0000-C000-000000000046}"
        )
        
        
        class IShellView(IOleWindow):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellView


    # END IF  __IShellView_FWD_DEFINED__

    if not defined(__IShellView2_FWD_DEFINED__):
        __IShellView2_FWD_DEFINED__ = 1
        IID_IShellView2 = MIDL_INTERFACE(
            "{88E39E80-3578-11CF-AE69-08002B2E1262}"
        )
        
        
        class IShellView2(IShellView):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellView2


    # END IF  __IShellView2_FWD_DEFINED__

    if not defined(__IFolderView_FWD_DEFINED__):
        __IFolderView_FWD_DEFINED__ = 1
        IID_IFolderView = MIDL_INTERFACE(
            "{CDE725B0-CCC9-4519-917E-325D72FAB4CE}"
        )
        
        
        class IFolderView(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFolderView


    # END IF  __IFolderView_FWD_DEFINED__

    if not defined(__IFolderView2_FWD_DEFINED__):
        __IFolderView2_FWD_DEFINED__ = 1
        IID_IFolderView2 = MIDL_INTERFACE(
            "{1AF3A467-214F-4298-908E-06B03E0B39F9}"
        )
        
        
        class IFolderView2(IFolderView):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFolderView2


    # END IF  __IFolderView2_FWD_DEFINED__

    if not defined(__IFolderViewSettings_FWD_DEFINED__):
        __IFolderViewSettings_FWD_DEFINED__ = 1
        IID_IFolderViewSettings = MIDL_INTERFACE(
            "{AE8C987D-8797-4ED3-BE72-2A47DD938DB0}"
        )
        
        
        class IFolderViewSettings(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFolderViewSettings


    # END IF  __IFolderViewSettings_FWD_DEFINED__

    if not defined(__IPreviewHandlerVisuals_FWD_DEFINED__):
        __IPreviewHandlerVisuals_FWD_DEFINED__ = 1
        IID_IPreviewHandlerVisuals = MIDL_INTERFACE(
            "{196BF9A5-B346-4EF0-AA1E-5DCDB76768B1}"
        )
        
        
        class IPreviewHandlerVisuals(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPreviewHandlerVisuals


    # END IF  __IPreviewHandlerVisuals_FWD_DEFINED__

    if not defined(__ICommDlgBrowser_FWD_DEFINED__):
        __ICommDlgBrowser_FWD_DEFINED__ = 1
        IID_ICommDlgBrowser = MIDL_INTERFACE(
            "{000214F1-0000-0000-C000-000000000046}"
        )
        
        
        class ICommDlgBrowser(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICommDlgBrowser


    # END IF  __ICommDlgBrowser_FWD_DEFINED__

    if not defined(__ICommDlgBrowser2_FWD_DEFINED__):
        __ICommDlgBrowser2_FWD_DEFINED__ = 1
        IID_ICommDlgBrowser2 = MIDL_INTERFACE(
            "{10339516-2894-11D2-9039-00C04F8EEB3E}"
        )
        
        
        class ICommDlgBrowser2(ICommDlgBrowser):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICommDlgBrowser2


    # END IF  __ICommDlgBrowser2_FWD_DEFINED__

    if not defined(__IColumnManager_FWD_DEFINED__):
        __IColumnManager_FWD_DEFINED__ = 1
        IID_IColumnManager = MIDL_INTERFACE(
            "{D8EC27BB-3F3B-4042-B10A-4ACFD924D453}"
        )
        
        
        class IColumnManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IColumnManager


    # END IF  __IColumnManager_FWD_DEFINED__

    if not defined(__IFolderFilterSite_FWD_DEFINED__):
        __IFolderFilterSite_FWD_DEFINED__ = 1
        IID_IFolderFilterSite = MIDL_INTERFACE(
            "{C0A651F5-B48B-11D2-B5ED-006097C686F6)//IID_IFOLDERFILTERSIT}"
        )
        
        
        class IFolderFilterSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFolderFilterSite


    # END IF  __IFolderFilterSite_FWD_DEFINED__

    if not defined(__IFolderFilter_FWD_DEFINED__):
        __IFolderFilter_FWD_DEFINED__ = 1
        IID_IFolderFilter = MIDL_INTERFACE(
            "{9CC22886-DC8E-11D2-B1D0-00C04F8EEB3E)//IID_IFOLDERFILTE}"
        )
        
        
        class IFolderFilter(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFolderFilter


    # END IF  __IFolderFilter_FWD_DEFINED__

    if not defined(__IInputObjectSite_FWD_DEFINED__):
        __IInputObjectSite_FWD_DEFINED__ = 1
        IID_IInputObjectSite = MIDL_INTERFACE(
            "{F1DB8392-7331-11D0-8C99-00A0C92DBFE8}"
        )
        
        
        class IInputObjectSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInputObjectSite


    # END IF  __IInputObjectSite_FWD_DEFINED__

    if not defined(__IInputObject_FWD_DEFINED__):
        __IInputObject_FWD_DEFINED__ = 1
        IID_IInputObject = MIDL_INTERFACE(
            "{68284FAA-6A48-11D0-8C78-00C04FD918B4}"
        )
        
        
        class IInputObject(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInputObject


    # END IF  __IInputObject_FWD_DEFINED__

    if not defined(__IInputObject2_FWD_DEFINED__):
        __IInputObject2_FWD_DEFINED__ = 1
        IID_IInputObject2 = MIDL_INTERFACE(
            "{6915C085-510B-44CD-94AF-28DFA56CF92B}"
        )
        
        
        class IInputObject2(IInputObject):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInputObject2


    # END IF  __IInputObject2_FWD_DEFINED__

    if not defined(__IShellIcon_FWD_DEFINED__):
        __IShellIcon_FWD_DEFINED__ = 1
        IID_IShellIcon = MIDL_INTERFACE(
            "{000214E5-0000-0000-C000-000000000046)//IID_ISHELLICO}"
        )
        
        
        class IShellIcon(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellIcon


    # END IF  __IShellIcon_FWD_DEFINED__

    if not defined(__IShellBrowser_FWD_DEFINED__):
        __IShellBrowser_FWD_DEFINED__ = 1
        IID_IShellBrowser = MIDL_INTERFACE(
            "{000214E2-0000-0000-C000-000000000046}"
        )
        
        
        class IShellBrowser(IOleWindow):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellBrowser


    # END IF  __IShellBrowser_FWD_DEFINED__

    if not defined(__IProfferService_FWD_DEFINED__):
        __IProfferService_FWD_DEFINED__ = 1
        IID_IProfferService = MIDL_INTERFACE(
            "{CB728B20-F786-11CE-92AD-00AA00A74CD0)//IID_IPROFFERSERVIC}"
        )
        
        
        class IProfferService(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IProfferService


    # END IF  __IProfferService_FWD_DEFINED__

    if not defined(__IShellItem_FWD_DEFINED__):
        __IShellItem_FWD_DEFINED__ = 1
        IID_IShellItem = MIDL_INTERFACE(
            "{43826D1E-E718-42EE-BC55-A1E261C37BFE}"
        )
        
        
        class IShellItem(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellItem


    # END IF  __IShellItem_FWD_DEFINED__

    if not defined(__IShellItem2_FWD_DEFINED__):
        __IShellItem2_FWD_DEFINED__ = 1
        IID_IShellItem2 = MIDL_INTERFACE(
            "{7E9FB0D3-919F-4307-AB2E-9B1860310C93}"
        )
        
        
        class IShellItem2(IShellItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellItem2


    # END IF  __IShellItem2_FWD_DEFINED__

    if not defined(__IShellItemImageFactory_FWD_DEFINED__):
        __IShellItemImageFactory_FWD_DEFINED__ = 1
        IID_IShellItemImageFactory = MIDL_INTERFACE(
            "{BCC18B79-BA16-442F-80C4-8A59C30C463B}"
        )
        
        
        class IShellItemImageFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellItemImageFactory


    # END IF  __IShellItemImageFactory_FWD_DEFINED__

    if not defined(__IEnumShellItems_FWD_DEFINED__):
        __IEnumShellItems_FWD_DEFINED__ = 1
        IID_IEnumShellItems = MIDL_INTERFACE(
            "{70629033-E363-4A28-A567-0DB78006E6D7}"
        )
        
        
        class IEnumShellItems(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumShellItems


    # END IF  __IEnumShellItems_FWD_DEFINED__

    if not defined(__ITransferAdviseSink_FWD_DEFINED__):
        __ITransferAdviseSink_FWD_DEFINED__ = 1
        IID_ITransferAdviseSink = MIDL_INTERFACE(
            "{D594D0D8-8DA7-457B-B3B4-CE5DBAAC0B88}"
        )
        
        
        class ITransferAdviseSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITransferAdviseSink


    # END IF  __ITransferAdviseSink_FWD_DEFINED__

    if not defined(__ITransferSource_FWD_DEFINED__):
        __ITransferSource_FWD_DEFINED__ = 1
        IID_ITransferSource = MIDL_INTERFACE(
            "{00ADB003-BDE9-45C6-8E29-D09F9353E108}"
        )
        
        
        class ITransferSource(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITransferSource


    # END IF  __ITransferSource_FWD_DEFINED__

    if not defined(__IEnumResources_FWD_DEFINED__):
        __IEnumResources_FWD_DEFINED__ = 1
        IID_IEnumResources = MIDL_INTERFACE(
            "{2DD81FE3-A83C-4DA9-A330-47249D345BA1}"
        )
        
        
        class IEnumResources(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumResources


    # END IF  __IEnumResources_FWD_DEFINED__

    if not defined(__IShellItemResources_FWD_DEFINED__):
        __IShellItemResources_FWD_DEFINED__ = 1
        IID_IShellItemResources = MIDL_INTERFACE(
            "{FF5693BE-2CE0-4D48-B5C5-40817D1ACDB9}"
        )
        
        
        class IShellItemResources(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellItemResources


    # END IF  __IShellItemResources_FWD_DEFINED__

    if not defined(__ITransferDestination_FWD_DEFINED__):
        __ITransferDestination_FWD_DEFINED__ = 1
        IID_ITransferDestination = MIDL_INTERFACE(
            "{48ADDD32-3CA5-4124-ABE3-B5A72531B207}"
        )
        
        
        class ITransferDestination(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITransferDestination


    # END IF  __ITransferDestination_FWD_DEFINED__

    if not defined(__IFileOperationProgressSink_FWD_DEFINED__):
        __IFileOperationProgressSink_FWD_DEFINED__ = 1
        IID_IFileOperationProgressSink = MIDL_INTERFACE(
            "{04B0F1A7-9490-44BC-96E1-4296A31252E2}"
        )
        
        
        class IFileOperationProgressSink(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileOperationProgressSink


    # END IF  __IFileOperationProgressSink_FWD_DEFINED__

    if not defined(__IShellItemArray_FWD_DEFINED__):
        __IShellItemArray_FWD_DEFINED__ = 1
        IID_IShellItemArray = MIDL_INTERFACE(
            "{B63EA76D-1F85-456F-A19C-48159EFA858B}"
        )
        
        
        class IShellItemArray(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellItemArray


    # END IF  __IShellItemArray_FWD_DEFINED__

    if not defined(__IInitializeWithItem_FWD_DEFINED__):
        __IInitializeWithItem_FWD_DEFINED__ = 1
        IID_IInitializeWithItem = MIDL_INTERFACE(
            "{7F73BE3F-FB79-493C-A6C7-7EE14E245841}"
        )
        
        
        class IInitializeWithItem(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInitializeWithItem


    # END IF  __IInitializeWithItem_FWD_DEFINED__

    if not defined(__IObjectWithSelection_FWD_DEFINED__):
        __IObjectWithSelection_FWD_DEFINED__ = 1
        IID_IObjectWithSelection = MIDL_INTERFACE(
            "{1C9CD5BB-98E9-4491-A60F-31AACC72B83C}"
        )
        
        
        class IObjectWithSelection(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IObjectWithSelection


    # END IF  __IObjectWithSelection_FWD_DEFINED__

    if not defined(__IObjectWithBackReferences_FWD_DEFINED__):
        __IObjectWithBackReferences_FWD_DEFINED__ = 1
        IID_IObjectWithBackReferences = MIDL_INTERFACE(
            "{321A6A6A-D61F-4BF3-97AE-14BE2986BB36}"
        )
        
        
        class IObjectWithBackReferences(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IObjectWithBackReferences


    # END IF  __IObjectWithBackReferences_FWD_DEFINED__

    if not defined(__IPropertyUI_FWD_DEFINED__):
        __IPropertyUI_FWD_DEFINED__ = 1
        IID_IPropertyUI = MIDL_INTERFACE(
            "{757A7D9F-919A-4118-99D7-DBB208C8CC66}"
        )
        
        
        class IPropertyUI(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPropertyUI


    # END IF  __IPropertyUI_FWD_DEFINED__

    if not defined(__ICategoryProvider_FWD_DEFINED__):
        __ICategoryProvider_FWD_DEFINED__ = 1
        IID_ICategoryProvider = MIDL_INTERFACE(
            "{9AF64809-5864-4C26-A720-C1F78C086EE3}"
        )
        
        
        class ICategoryProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICategoryProvider


    # END IF  __ICategoryProvider_FWD_DEFINED__

    if not defined(__ICategorizer_FWD_DEFINED__):
        __ICategorizer_FWD_DEFINED__ = 1
        IID_ICategorizer = MIDL_INTERFACE(
            "{A3B14589-9174-49A8-89A3-06A1AE2B9BA7}"
        )
        
        
        class ICategorizer(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICategorizer


    # END IF  __ICategorizer_FWD_DEFINED__

    if not defined(__IDropTargetHelper_FWD_DEFINED__):
        __IDropTargetHelper_FWD_DEFINED__ = 1
        IID_IDropTargetHelper = MIDL_INTERFACE(
            "{4657278B-411B-11D2-839A-00C04FD918D0}"
        )
        
        
        class IDropTargetHelper(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDropTargetHelper


    # END IF  __IDropTargetHelper_FWD_DEFINED__

    if not defined(__IDragSourceHelper_FWD_DEFINED__):
        __IDragSourceHelper_FWD_DEFINED__ = 1
        IID_IDragSourceHelper = MIDL_INTERFACE(
            "{DE5BF786-477A-11D2-839D-00C04FD918D0}"
        )
        
        
        class IDragSourceHelper(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDragSourceHelper


    # END IF  __IDragSourceHelper_FWD_DEFINED__

    if not defined(__IShellLinkA_FWD_DEFINED__):
        __IShellLinkA_FWD_DEFINED__ = 1
        IID_IShellLinkA = MIDL_INTERFACE(
            "{000214EE-0000-0000-C000-000000000046}"
        )
        
        
        class IShellLinkA(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellLinkA


    # END IF  __IShellLinkA_FWD_DEFINED__

    if not defined(__IShellLinkW_FWD_DEFINED__):
        __IShellLinkW_FWD_DEFINED__ = 1
        IID_IShellLinkW = MIDL_INTERFACE(
            "{000214F9-0000-0000-C000-000000000046}"
        )
        
        
        class IShellLinkW(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellLinkW


    # END IF  __IShellLinkW_FWD_DEFINED__

    if not defined(__IShellLinkDataList_FWD_DEFINED__):
        __IShellLinkDataList_FWD_DEFINED__ = 1
        IID_IShellLinkDataList = MIDL_INTERFACE(
            "{45E2B4AE-B1C3-11D0-B92F-00A0C90312E1}"
        )
        
        
        class IShellLinkDataList(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = ['#ifdef BUILD_SPLIT_AS_IE', '#endif']
            _iid_ = IID_IShellLinkDataList


    # END IF  __IShellLinkDataList_FWD_DEFINED__

    if not defined(__IResolveShellLink_FWD_DEFINED__):
        __IResolveShellLink_FWD_DEFINED__ = 1
        IID_IResolveShellLink = MIDL_INTERFACE(
            "{5CD52983-9449-11D2-963A-00C04F79ADF0}"
        )
        
        
        class IResolveShellLink(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IResolveShellLink


    # END IF  __IResolveShellLink_FWD_DEFINED__

    if not defined(__IActionProgressDialog_FWD_DEFINED__):
        __IActionProgressDialog_FWD_DEFINED__ = 1
        IID_IActionProgressDialog = MIDL_INTERFACE(
            "{49FF1172-EADC-446D-9285-156453A6431C}"
        )
        
        
        class IActionProgressDialog(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IActionProgressDialog


    # END IF  __IActionProgressDialog_FWD_DEFINED__

    if not defined(__IActionProgress_FWD_DEFINED__):
        __IActionProgress_FWD_DEFINED__ = 1
        IID_IActionProgress = MIDL_INTERFACE(
            "{49FF1173-EADC-446D-9285-156453A6431C}"
        )
        
        
        class IActionProgress(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IActionProgress


    # END IF  __IActionProgress_FWD_DEFINED__

    if not defined(__IShellExtInit_FWD_DEFINED__):
        __IShellExtInit_FWD_DEFINED__ = 1
        IID_IShellExtInit = MIDL_INTERFACE(
            "{000214E8-0000-0000-C000-000000000046}"
        )
        
        
        class IShellExtInit(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellExtInit


    # END IF  __IShellExtInit_FWD_DEFINED__

    if not defined(__IShellPropSheetExt_FWD_DEFINED__):
        __IShellPropSheetExt_FWD_DEFINED__ = 1
        IID_IShellPropSheetExt = MIDL_INTERFACE(
            "{000214E9-0000-0000-C000-000000000046}"
        )
        
        
        class IShellPropSheetExt(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellPropSheetExt


    # END IF  __IShellPropSheetExt_FWD_DEFINED__

    if not defined(__IRemoteComputer_FWD_DEFINED__):
        __IRemoteComputer_FWD_DEFINED__ = 1
        IID_IRemoteComputer = MIDL_INTERFACE(
            "{000214FE-0000-0000-C000-000000000046}"
        )
        
        
        class IRemoteComputer(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IRemoteComputer


    # END IF  __IRemoteComputer_FWD_DEFINED__

    if not defined(__IQueryContinue_FWD_DEFINED__):
        __IQueryContinue_FWD_DEFINED__ = 1
        IID_IQueryContinue = MIDL_INTERFACE(
            "{7307055C-B24A-486B-9F25-163E597A28A9}"
        )
        
        
        class IQueryContinue(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IQueryContinue


    # END IF  __IQueryContinue_FWD_DEFINED__

    if not defined(__IObjectWithCancelEvent_FWD_DEFINED__):
        __IObjectWithCancelEvent_FWD_DEFINED__ = 1
        IID_IObjectWithCancelEvent = MIDL_INTERFACE(
            "{F279B885-0AE9-4B85-AC06-DDECF9408941}"
        )
        
        
        class IObjectWithCancelEvent(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IObjectWithCancelEvent


    # END IF  __IObjectWithCancelEvent_FWD_DEFINED__

    if not defined(__IUserNotification_FWD_DEFINED__):
        __IUserNotification_FWD_DEFINED__ = 1
        IID_IUserNotification = MIDL_INTERFACE(
            "{BA9711BA-5893-4787-A7E1-41277151550B}"
        )
        
        
        class IUserNotification(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IUserNotification


    # END IF  __IUserNotification_FWD_DEFINED__

    if not defined(__IItemNameLimits_FWD_DEFINED__):
        __IItemNameLimits_FWD_DEFINED__ = 1
        IID_IItemNameLimits = MIDL_INTERFACE(
            "{1DF0D7F1-B267-4D28-8B10-12E23202A5C4}"
        )
        
        
        class IItemNameLimits(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IItemNameLimits


    # END IF  __IItemNameLimits_FWD_DEFINED__

    if not defined(__ISearchFolderItemFactory_FWD_DEFINED__):
        __ISearchFolderItemFactory_FWD_DEFINED__ = 1
        IID_ISearchFolderItemFactory = MIDL_INTERFACE(
            "{A0FFBC28-5482-4366-BE27-3E81E78E06C2}"
        )
        
        
        class ISearchFolderItemFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ISearchFolderItemFactory


    # END IF  __ISearchFolderItemFactory_FWD_DEFINED__

    if not defined(__IExtractImage_FWD_DEFINED__):
        __IExtractImage_FWD_DEFINED__ = 1
        IID_IExtractImage = MIDL_INTERFACE(
            "{BB2E617C-0920-11D1-9A0B-00C04FC2D6C1}"
        )
        
        
        class IExtractImage(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExtractImage


    # END IF  __IExtractImage_FWD_DEFINED__

    if not defined(__IExtractImage2_FWD_DEFINED__):
        __IExtractImage2_FWD_DEFINED__ = 1
        IID_IExtractImage2 = MIDL_INTERFACE(
            "{953BB1EE-93B4-11D1-98A3-00C04FB687DA}"
        )
        
        
        class IExtractImage2(IExtractImage):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExtractImage2


    # END IF  __IExtractImage2_FWD_DEFINED__

    if not defined(__IThumbnailHandlerFactory_FWD_DEFINED__):
        __IThumbnailHandlerFactory_FWD_DEFINED__ = 1
        IID_IThumbnailHandlerFactory = MIDL_INTERFACE(
            "{E35B4B2E-00DA-4BC1-9F13-38BC11F5D417}"
        )
        
        
        class IThumbnailHandlerFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IThumbnailHandlerFactory


    # END IF  __IThumbnailHandlerFactory_FWD_DEFINED__

    if not defined(__IParentAndItem_FWD_DEFINED__):
        __IParentAndItem_FWD_DEFINED__ = 1
        IID_IParentAndItem = MIDL_INTERFACE(
            "{B3A4B685-B685-4805-99D9-5DEAD2873236)//IID_IPARENTANDITE}"
        )
        
        
        class IParentAndItem(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IParentAndItem


    # END IF  __IParentAndItem_FWD_DEFINED__

    if not defined(__IDockingWindow_FWD_DEFINED__):
        __IDockingWindow_FWD_DEFINED__ = 1
        IID_IDockingWindow = MIDL_INTERFACE(
            "{012DD920-7B26-11D0-8CA9-00A0C92DBFE8}"
        )
        
        
        class IDockingWindow(IOleWindow):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDockingWindow


    # END IF  __IDockingWindow_FWD_DEFINED__

    if not defined(__IDeskBand_FWD_DEFINED__):
        __IDeskBand_FWD_DEFINED__ = 1
        IID_IDeskBand = MIDL_INTERFACE(
            "{EB0FE172-1A3A-11D0-89B3-00A0C90A90AC}"
        )
        
        
        class IDeskBand(IDockingWindow):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDeskBand


    # END IF  __IDeskBand_FWD_DEFINED__

    if not defined(__IDeskBandInfo_FWD_DEFINED__):
        __IDeskBandInfo_FWD_DEFINED__ = 1
        IID_IDeskBandInfo = MIDL_INTERFACE(
            "{77E425FC-CBF9-4307-BA6A-BB5727745661}"
        )
        
        
        class IDeskBandInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDeskBandInfo


    # END IF  __IDeskBandInfo_FWD_DEFINED__

    if not defined(__ITaskbarList_FWD_DEFINED__):
        __ITaskbarList_FWD_DEFINED__ = 1
        IID_ITaskbarList = MIDL_INTERFACE(
            "{56FDF342-FD6D-11D0-958A-006097C9A090}"
        )
        
        
        class ITaskbarList(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITaskbarList


    # END IF  __ITaskbarList_FWD_DEFINED__

    if not defined(__ITaskbarList2_FWD_DEFINED__):
        __ITaskbarList2_FWD_DEFINED__ = 1
        IID_ITaskbarList2 = MIDL_INTERFACE(
            "{602D4995-B13A-429B-A66E-1935E44F4317}"
        )
        
        
        class ITaskbarList2(ITaskbarList):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITaskbarList2


    # END IF  __ITaskbarList2_FWD_DEFINED__

    if not defined(__ITaskbarList3_FWD_DEFINED__):
        __ITaskbarList3_FWD_DEFINED__ = 1
        IID_ITaskbarList3 = MIDL_INTERFACE(
            "{EA1AFB91-9E28-4B86-90E9-9E9F8A5EEFAF}"
        )
        
        
        class ITaskbarList3(ITaskbarList2):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITaskbarList3


    # END IF  __ITaskbarList3_FWD_DEFINED__

    if not defined(__ITaskbarList4_FWD_DEFINED__):
        __ITaskbarList4_FWD_DEFINED__ = 1
        IID_ITaskbarList4 = MIDL_INTERFACE(
            "{C43DC798-95D1-4BEA-9030-BB99E2983A1A}"
        )
        
        
        class ITaskbarList4(ITaskbarList3):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITaskbarList4


    # END IF  __ITaskbarList4_FWD_DEFINED__

    if not defined(__IExplorerBrowserEvents_FWD_DEFINED__):
        __IExplorerBrowserEvents_FWD_DEFINED__ = 1
        IID_IExplorerBrowserEvents = MIDL_INTERFACE(
            "{361BBDC7-E6EE-4E13-BE58-58E2240C810F)//IID_IEXPLORERBROWSEREVENT}"
        )
        
        
        class IExplorerBrowserEvents(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExplorerBrowserEvents


    # END IF  __IExplorerBrowserEvents_FWD_DEFINED__

    if not defined(__IExplorerBrowser_FWD_DEFINED__):
        __IExplorerBrowser_FWD_DEFINED__ = 1
        IID_IExplorerBrowser = MIDL_INTERFACE(
            "{DFD3B6B5-C10C-4BE9-85F6-A66969F402F6}"
        )
        
        
        class IExplorerBrowser(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExplorerBrowser


    # END IF  __IExplorerBrowser_FWD_DEFINED__

    if not defined(__IEnumObjects_FWD_DEFINED__):
        __IEnumObjects_FWD_DEFINED__ = 1
        IID_IEnumObjects = MIDL_INTERFACE(
            "{2C1C7E2E-2D0E-4059-831E-1E6F82335C2E}"
        )
        
        
        class IEnumObjects(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumObjects


    # END IF  __IEnumObjects_FWD_DEFINED__

    if not defined(__IOperationsProgressDialog_FWD_DEFINED__):
        __IOperationsProgressDialog_FWD_DEFINED__ = 1
        IID_IOperationsProgressDialog = MIDL_INTERFACE(
            "{0C9FB851-E5C9-43EB-A370-F0677B13874C}"
        )
        
        
        class IOperationsProgressDialog(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IOperationsProgressDialog


    # END IF  __IOperationsProgressDialog_FWD_DEFINED__

    if not defined(__IIOCancelInformation_FWD_DEFINED__):
        __IIOCancelInformation_FWD_DEFINED__ = 1
        IID_IIOCancelInformation = MIDL_INTERFACE(
            "{F5B0BF81-8CB5-4B1B-9449-1A159E0C733C}"
        )
        
        
        class IIOCancelInformation(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IIOCancelInformation


    # END IF  __IIOCancelInformation_FWD_DEFINED__

    if not defined(__IFileOperation_FWD_DEFINED__):
        __IFileOperation_FWD_DEFINED__ = 1
        IID_IFileOperation = MIDL_INTERFACE(
            "{947AAB5F-0A5C-4C13-B4D6-4BF7836FC9F8}"
        )
        
        
        class IFileOperation(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileOperation


    # END IF  __IFileOperation_FWD_DEFINED__

    if not defined(__IFileOperation2_FWD_DEFINED__):
        __IFileOperation2_FWD_DEFINED__ = 1
        IID_IFileOperation2 = MIDL_INTERFACE(
            "{CD8F23C1-8F61-4916-909D-55BDD0918753}"
        )
        
        
        class IFileOperation2(IFileOperation):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileOperation2


    # END IF  __IFileOperation2_FWD_DEFINED__

    if not defined(__IObjectProvider_FWD_DEFINED__):
        __IObjectProvider_FWD_DEFINED__ = 1
        IID_IObjectProvider = MIDL_INTERFACE(
            "{A6087428-3BE3-4D73-B308-7C04A540BF1A}"
        )
        
        
        class IObjectProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IObjectProvider


    # END IF  __IObjectProvider_FWD_DEFINED__

    if not defined(__INamespaceWalkCB_FWD_DEFINED__):
        __INamespaceWalkCB_FWD_DEFINED__ = 1
        IID_INamespaceWalkCB = MIDL_INTERFACE(
            "{D92995F8-CF5E-4A76-BF59-EAD39EA2B97E}"
        )
        
        
        class INamespaceWalkCB(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_INamespaceWalkCB


    # END IF  __INamespaceWalkCB_FWD_DEFINED__

    if not defined(__INamespaceWalkCB2_FWD_DEFINED__):
        __INamespaceWalkCB2_FWD_DEFINED__ = 1
        IID_INamespaceWalkCB2 = MIDL_INTERFACE(
            "{7AC7492B-C38E-438A-87DB-68737844FF70}"
        )
        
        
        class INamespaceWalkCB2(INamespaceWalkCB):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_INamespaceWalkCB2


    # END IF  __INamespaceWalkCB2_FWD_DEFINED__

    if not defined(__INamespaceWalk_FWD_DEFINED__):
        __INamespaceWalk_FWD_DEFINED__ = 1
        IID_INamespaceWalk = MIDL_INTERFACE(
            "{57CED8A7-3F4A-432C-9350-30F24483F74F}"
        )
        
        
        class INamespaceWalk(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_INamespaceWalk


    # END IF  __INamespaceWalk_FWD_DEFINED__

    if not defined(__IBandSite_FWD_DEFINED__):
        __IBandSite_FWD_DEFINED__ = 1
        IID_IBandSite = MIDL_INTERFACE(
            "{4CF504B0-DE96-11D0-8B3F-00A0C911E8E5}"
        )
        
        
        class IBandSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IBandSite


    # END IF  __IBandSite_FWD_DEFINED__

    if not defined(__IModalWindow_FWD_DEFINED__):
        __IModalWindow_FWD_DEFINED__ = 1
        IID_IModalWindow = MIDL_INTERFACE(
            "{B4DB1657-70D7-485E-8E3E-6FCB5A5C1802}"
        )
        
        
        class IModalWindow(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IModalWindow


    # END IF  __IModalWindow_FWD_DEFINED__

    if not defined(__IContextMenuSite_FWD_DEFINED__):
        __IContextMenuSite_FWD_DEFINED__ = 1
        IID_IContextMenuSite = MIDL_INTERFACE(
            "{0811AEBE-0B87-4C54-9E72-548CF649016B}"
        )
        
        
        class IContextMenuSite(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IContextMenuSite


    # END IF  __IContextMenuSite_FWD_DEFINED__

    if not defined(__IMenuBand_FWD_DEFINED__):
        __IMenuBand_FWD_DEFINED__ = 1
        IID_IMenuBand = MIDL_INTERFACE(
            "{568804CD-CBD7-11D0-9816-00C04FD91972}"
        )
        
        
        class IMenuBand(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IMenuBand


    # END IF  __IMenuBand_FWD_DEFINED__

    if not defined(__IRegTreeItem_FWD_DEFINED__):
        __IRegTreeItem_FWD_DEFINED__ = 1
        IID_IRegTreeItem = MIDL_INTERFACE(
            "{A9521922-0812-4D44-9EC3-7FD38C726F3D}"
        )
        
        
        class IRegTreeItem(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IRegTreeItem


    # END IF  __IRegTreeItem_FWD_DEFINED__

    if not defined(__IDeskBar_FWD_DEFINED__):
        __IDeskBar_FWD_DEFINED__ = 1
        IID_IDeskBar = MIDL_INTERFACE(
            "{EB0FE173-1A3A-11D0-89B3-00A0C90A90AC}"
        )
        
        
        class IDeskBar(IOleWindow):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDeskBar


    # END IF  __IDeskBar_FWD_DEFINED__

    if not defined(__IMenuPopup_FWD_DEFINED__):
        __IMenuPopup_FWD_DEFINED__ = 1
        IID_IMenuPopup = MIDL_INTERFACE(
            "{D1E7AFEB-6A2E-11D0-8C78-00C04FD918B4}"
        )
        
        
        class IMenuPopup(IDeskBar):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IMenuPopup


    # END IF  __IMenuPopup_FWD_DEFINED__

    if not defined(__IFileIsInUse_FWD_DEFINED__):
        __IFileIsInUse_FWD_DEFINED__ = 1
        IID_IFileIsInUse = MIDL_INTERFACE(
            "{64A1CBF0-3A1A-4461-9158-376969693950}"
        )
        
        
        class IFileIsInUse(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileIsInUse


    # END IF  __IFileIsInUse_FWD_DEFINED__

    if not defined(__IFileDialogEvents_FWD_DEFINED__):
        __IFileDialogEvents_FWD_DEFINED__ = 1
        IID_IFileDialogEvents = MIDL_INTERFACE(
            "{973510DB-7D7F-452B-8975-74A85828D354}"
        )
        
        
        class IFileDialogEvents(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileDialogEvents


    # END IF  __IFileDialogEvents_FWD_DEFINED__

    if not defined(__IFileDialog_FWD_DEFINED__):
        __IFileDialog_FWD_DEFINED__ = 1
        IID_IFileDialog = MIDL_INTERFACE(
            "{42F85136-DB7E-439C-85F1-E4075D135FC8}"
        )
        
        
        class IFileDialog(IModalWindow):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileDialog


    # END IF  __IFileDialog_FWD_DEFINED__

    if not defined(__IFileSaveDialog_FWD_DEFINED__):
        __IFileSaveDialog_FWD_DEFINED__ = 1
        IID_IFileSaveDialog = MIDL_INTERFACE(
            "{84BCCD23-5FDE-4CDB-AEA4-AF64B83D78AB}"
        )
        
        
        class IFileSaveDialog(IFileDialog):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileSaveDialog


    # END IF  __IFileSaveDialog_FWD_DEFINED__

    if not defined(__IFileOpenDialog_FWD_DEFINED__):
        __IFileOpenDialog_FWD_DEFINED__ = 1
        IID_IFileOpenDialog = MIDL_INTERFACE(
            "{D57C7288-D4AD-4768-BE02-9D969532D960}"
        )
        
        
        class IFileOpenDialog(IFileDialog):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileOpenDialog


    # END IF  __IFileOpenDialog_FWD_DEFINED__

    if not defined(__IFileDialogCustomize_FWD_DEFINED__):
        __IFileDialogCustomize_FWD_DEFINED__ = 1
        IID_IFileDialogCustomize = MIDL_INTERFACE(
            "{E6FDD21A-163F-4975-9C8C-A69F1BA37034}"
        )
        
        
        class IFileDialogCustomize(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileDialogCustomize


    # END IF  __IFileDialogCustomize_FWD_DEFINED__

    if not defined(__IApplicationAssociationRegistration_FWD_DEFINED__):
        __IApplicationAssociationRegistration_FWD_DEFINED__ = 1
        IID_IApplicationAssociationRegistration = MIDL_INTERFACE(
            "{4E530B0A-E611-4C77-A3AC-9031D022281B}"
        )
        
        
        class IApplicationAssociationRegistration(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IApplicationAssociationRegistration


    # END IF  __IApplicationAssociationRegistration_FWD_DEFINED__

    if not defined(__IDelegateFolder_FWD_DEFINED__):
        __IDelegateFolder_FWD_DEFINED__ = 1
        IID_IDelegateFolder = MIDL_INTERFACE(
            "{ADD8BA80-002B-11D0-8F0F-00C04FD7D062}"
        )
        
        
        class IDelegateFolder(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDelegateFolder


    # END IF  __IDelegateFolder_FWD_DEFINED__

    if not defined(__IBrowserFrameOptions_FWD_DEFINED__):
        __IBrowserFrameOptions_FWD_DEFINED__ = 1
        IID_IBrowserFrameOptions = MIDL_INTERFACE(
            "{10DF43C8-1DBE-11D3-8B34-006097DF5BD4}"
        )
        
        
        class IBrowserFrameOptions(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IBrowserFrameOptions


    # END IF  __IBrowserFrameOptions_FWD_DEFINED__

    if not defined(__INewWindowManager_FWD_DEFINED__):
        __INewWindowManager_FWD_DEFINED__ = 1
        IID_INewWindowManager = MIDL_INTERFACE(
            "{D2BC4C84-3F72-4A52-A604-7BCBF3982CBB}"
        )
        
        
        class INewWindowManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_INewWindowManager


    # END IF  __INewWindowManager_FWD_DEFINED__

    if not defined(__IAttachmentExecute_FWD_DEFINED__):
        __IAttachmentExecute_FWD_DEFINED__ = 1
        IID_IAttachmentExecute = MIDL_INTERFACE(
            "{73DB1241-1E85-4581-8E4F-A81E1D0F8C57)//IID_IATTACHMENTEXECUT}"
        )
        
        
        class IAttachmentExecute(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IAttachmentExecute


    # END IF  __IAttachmentExecute_FWD_DEFINED__

    if not defined(__IShellMenuCallback_FWD_DEFINED__):
        __IShellMenuCallback_FWD_DEFINED__ = 1
        IID_IShellMenuCallback = MIDL_INTERFACE(
            "{4CA300A1-9B8D-11D1-8B22-00C04FD918D0}"
        )
        
        
        class IShellMenuCallback(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellMenuCallback


    # END IF  __IShellMenuCallback_FWD_DEFINED__

    if not defined(__IShellMenu_FWD_DEFINED__):
        __IShellMenu_FWD_DEFINED__ = 1
        IID_IShellMenu = MIDL_INTERFACE(
            "{EE1F7637-E138-11D1-8379-00C04FD918D0}"
        )
        
        
        class IShellMenu(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellMenu


    # END IF  __IShellMenu_FWD_DEFINED__

    if not defined(__IKnownFolder_FWD_DEFINED__):
        __IKnownFolder_FWD_DEFINED__ = 1
        IID_IKnownFolder = MIDL_INTERFACE(
            "{3AA7AF7E-9B36-420C-A8E3-F77D4674A488}"
        )
        
        
        class IKnownFolder(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IKnownFolder


    # END IF  __IKnownFolder_FWD_DEFINED__

    if not defined(__IKnownFolderManager_FWD_DEFINED__):
        __IKnownFolderManager_FWD_DEFINED__ = 1
        IID_IKnownFolderManager = MIDL_INTERFACE(
            "{8BE2D872-86AA-4D47-B776-32CCA40C7018}"
        )
        
        
        class IKnownFolderManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IKnownFolderManager


    # END IF  __IKnownFolderManager_FWD_DEFINED__

    if not defined(__ISharingConfigurationManager_FWD_DEFINED__):
        __ISharingConfigurationManager_FWD_DEFINED__ = 1
        IID_ISharingConfigurationManager = MIDL_INTERFACE(
            "{B4CD448A-9C86-4466-9201-2E62105B87AE}"
        )
        
        
        class ISharingConfigurationManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ISharingConfigurationManager


    # END IF  __ISharingConfigurationManager_FWD_DEFINED__

    if not defined(__IRelatedItem_FWD_DEFINED__):
        __IRelatedItem_FWD_DEFINED__ = 1
        IID_IRelatedItem = MIDL_INTERFACE(
            "{A73CE67A-8AB1-44F1-8D43-D2FCBF6B1CD0}"
        )
        
        
        class IRelatedItem(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IRelatedItem


    # END IF  __IRelatedItem_FWD_DEFINED__

    if not defined(__IIdentityName_FWD_DEFINED__):
        __IIdentityName_FWD_DEFINED__ = 1
        IID_IIdentityName = MIDL_INTERFACE(
            "{7D903FCA-D6F9-4810-8332-946C0177E247}"
        )
        
        
        class IIdentityName(IRelatedItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IIdentityName


    # END IF  __IIdentityName_FWD_DEFINED__

    if not defined(__IDelegateItem_FWD_DEFINED__):
        __IDelegateItem_FWD_DEFINED__ = 1
        IID_IDelegateItem = MIDL_INTERFACE(
            "{3C5A1C94-C951-4CB7-BB6D-3B93F30CCE93}"
        )
        
        
        class IDelegateItem(IRelatedItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDelegateItem


    # END IF  __IDelegateItem_FWD_DEFINED__

    if not defined(__ICurrentItem_FWD_DEFINED__):
        __ICurrentItem_FWD_DEFINED__ = 1
        IID_ICurrentItem = MIDL_INTERFACE(
            "{240A7174-D653-4A1D-A6D3-D4943CFBFE3D}"
        )
        
        
        class ICurrentItem(IRelatedItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICurrentItem


    # END IF  __ICurrentItem_FWD_DEFINED__

    if not defined(__ITransferMediumItem_FWD_DEFINED__):
        __ITransferMediumItem_FWD_DEFINED__ = 1
        IID_ITransferMediumItem = MIDL_INTERFACE(
            "{77F295D5-2D6F-4E19-B8AE-322F3E721AB5}"
        )
        
        
        class ITransferMediumItem(IRelatedItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ITransferMediumItem


    # END IF  __ITransferMediumItem_FWD_DEFINED__

    if not defined(__IDisplayItem_FWD_DEFINED__):
        __IDisplayItem_FWD_DEFINED__ = 1
        IID_IDisplayItem = MIDL_INTERFACE(
            "{C6FD5997-9F6B-4888-8703-94E80E8CDE3F}"
        )
        
        
        class IDisplayItem(IRelatedItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDisplayItem


    # END IF  __IDisplayItem_FWD_DEFINED__

    if not defined(__IViewStateIdentityItem_FWD_DEFINED__):
        __IViewStateIdentityItem_FWD_DEFINED__ = 1
        IID_IViewStateIdentityItem = MIDL_INTERFACE(
            "{9D264146-A94F-4195-9F9F-3BB12CE0C955}"
        )
        
        
        class IViewStateIdentityItem(IRelatedItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IViewStateIdentityItem


    # END IF  __IViewStateIdentityItem_FWD_DEFINED__

    if not defined(__IPreviewItem_FWD_DEFINED__):
        __IPreviewItem_FWD_DEFINED__ = 1
        IID_IPreviewItem = MIDL_INTERFACE(
            "{36149969-0A8F-49C8-8B00-4AECB20222FB}"
        )
        
        
        class IPreviewItem(IRelatedItem):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPreviewItem


    # END IF  __IPreviewItem_FWD_DEFINED__

    if not defined(__IDestinationStreamFactory_FWD_DEFINED__):
        __IDestinationStreamFactory_FWD_DEFINED__ = 1
        IID_IDestinationStreamFactory = MIDL_INTERFACE(
            "{8A87781B-39A7-4A1F-AAB3-A39B9C34A7D9}"
        )
        
        
        class IDestinationStreamFactory(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDestinationStreamFactory


    # END IF  __IDestinationStreamFactory_FWD_DEFINED__

    if not defined(__ICreateProcessInputs_FWD_DEFINED__):
        __ICreateProcessInputs_FWD_DEFINED__ = 1
        IID_ICreateProcessInputs = MIDL_INTERFACE(
            "{F6EF6140-E26F-4D82-BAC4-E9BA5FD239A8}"
        )
        
        
        class ICreateProcessInputs(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICreateProcessInputs


    # END IF  __ICreateProcessInputs_FWD_DEFINED__

    if not defined(__ICreatingProcess_FWD_DEFINED__):
        __ICreatingProcess_FWD_DEFINED__ = 1
        IID_ICreatingProcess = MIDL_INTERFACE(
            "{None        }"
        )
        
        
        class ICreatingProcess(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICreatingProcess


    # END IF  __ICreatingProcess_FWD_DEFINED__

    if not defined(__INewMenuClient_FWD_DEFINED__):
        __INewMenuClient_FWD_DEFINED__ = 1
        IID_INewMenuClient = MIDL_INTERFACE(
            "{DCB07FDC-3BB5-451C-90BE-966644FED7B0}"
        )
        
        
        class INewMenuClient(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_INewMenuClient


    # END IF  __INewMenuClient_FWD_DEFINED__

    if not defined(__IInitializeWithBindCtx_FWD_DEFINED__):
        __IInitializeWithBindCtx_FWD_DEFINED__ = 1
        IID_IInitializeWithBindCtx = MIDL_INTERFACE(
            "{71C0D2BC-726D-45CC-A6C0-2E31C1DB2159}"
        )
        
        
        class IInitializeWithBindCtx(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInitializeWithBindCtx


    # END IF  __IInitializeWithBindCtx_FWD_DEFINED__

    if not defined(__IShellItemFilter_FWD_DEFINED__):
        __IShellItemFilter_FWD_DEFINED__ = 1
        IID_IShellItemFilter = MIDL_INTERFACE(
            "{2659B475-EEB8-48B7-8F07-B378810F48CF}"
        )
        
        
        class IShellItemFilter(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellItemFilter


    # END IF  __IShellItemFilter_FWD_DEFINED__

    if not defined(__INameSpaceTreeControl_FWD_DEFINED__):
        __INameSpaceTreeControl_FWD_DEFINED__ = 1
        IID_INameSpaceTreeControl = MIDL_INTERFACE(
            "{028212A3-B627-47E9-8856-C14265554E4F}"
        )
        
        
        class INameSpaceTreeControl(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_INameSpaceTreeControl


    # END IF  __INameSpaceTreeControl_FWD_DEFINED__

    if not defined(__INameSpaceTreeControlFolderCapabilities_FWD_DEFINED__):
        __INameSpaceTreeControlFolderCapabilities_FWD_DEFINED__ = 1
        IID_INameSpaceTreeControlFolderCapabilities = MIDL_INTERFACE(
            "{E9701183-E6B3-4FF2-8568-813615FEC7BE}"
        )
        
        
        class INameSpaceTreeControlFolderCapabilities(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_INameSpaceTreeControlFolderCapabilities


    # END IF  __INameSpaceTreeControlFolderCapabilities_FWD_DEFINED__

    if not defined(__IPreviewHandler_FWD_DEFINED__):
        __IPreviewHandler_FWD_DEFINED__ = 1
        IID_IPreviewHandler = MIDL_INTERFACE(
            "{8895B1C6-B41F-4C1C-A562-0D564250836F}"
        )
        
        
        class IPreviewHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPreviewHandler


    # END IF  __IPreviewHandler_FWD_DEFINED__

    if not defined(__IPreviewHandlerFrame_FWD_DEFINED__):
        __IPreviewHandlerFrame_FWD_DEFINED__ = 1
        IID_IPreviewHandlerFrame = MIDL_INTERFACE(
            "{FEC87AAF-35F9-447A-ADB7-20234491401A}"
        )
        
        
        class IPreviewHandlerFrame(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPreviewHandlerFrame


    # END IF  __IPreviewHandlerFrame_FWD_DEFINED__

    if not defined(__IExplorerPaneVisibility_FWD_DEFINED__):
        __IExplorerPaneVisibility_FWD_DEFINED__ = 1
        IID_IExplorerPaneVisibility = MIDL_INTERFACE(
            "{E07010EC-BC17-44C0-97B0-46C7C95B9EDC}"
        )
        
        
        class IExplorerPaneVisibility(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExplorerPaneVisibility


    # END IF  __IExplorerPaneVisibility_FWD_DEFINED__

    if not defined(__IContextMenuCB_FWD_DEFINED__):
        __IContextMenuCB_FWD_DEFINED__ = 1
        IID_IContextMenuCB = MIDL_INTERFACE(
            "{3409E930-5A39-11D1-83FA-00A0C90DC849}"
        )
        
        
        class IContextMenuCB(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IContextMenuCB


    # END IF  __IContextMenuCB_FWD_DEFINED__

    if not defined(__IDefaultExtractIconInit_FWD_DEFINED__):
        __IDefaultExtractIconInit_FWD_DEFINED__ = 1
        IID_IDefaultExtractIconInit = MIDL_INTERFACE(
            "{41DED17D-D6B3-4261-997D-88C60E4B1D58}"
        )
        
        
        class IDefaultExtractIconInit(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDefaultExtractIconInit


    # END IF  __IDefaultExtractIconInit_FWD_DEFINED__

    if not defined(__IExplorerCommand_FWD_DEFINED__):
        __IExplorerCommand_FWD_DEFINED__ = 1
        IID_IExplorerCommand = MIDL_INTERFACE(
            "{A08CE4D0-FA25-44AB-B57C-C7B1C323E0B9}"
        )
        
        
        class IExplorerCommand(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExplorerCommand


    # END IF  __IExplorerCommand_FWD_DEFINED__

    if not defined(__IExplorerCommandState_FWD_DEFINED__):
        __IExplorerCommandState_FWD_DEFINED__ = 1
        IID_IExplorerCommandState = MIDL_INTERFACE(
            "{BDDACB60-7657-47AE-8445-D23E1ACF82AE}"
        )
        
        
        class IExplorerCommandState(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExplorerCommandState


    # END IF  __IExplorerCommandState_FWD_DEFINED__

    if not defined(__IInitializeCommand_FWD_DEFINED__):
        __IInitializeCommand_FWD_DEFINED__ = 1
        IID_IInitializeCommand = MIDL_INTERFACE(
            "{85075ACF-231F-40EA-9610-D26B7B58F638}"
        )
        
        
        class IInitializeCommand(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInitializeCommand


    # END IF  __IInitializeCommand_FWD_DEFINED__

    if not defined(__IEnumExplorerCommand_FWD_DEFINED__):
        __IEnumExplorerCommand_FWD_DEFINED__ = 1
        IID_IEnumExplorerCommand = MIDL_INTERFACE(
            "{A88826F8-186F-4987-AADE-EA0CEF8FBFE8}"
        )
        
        
        class IEnumExplorerCommand(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumExplorerCommand


    # END IF  __IEnumExplorerCommand_FWD_DEFINED__

    if not defined(__IExplorerCommandProvider_FWD_DEFINED__):
        __IExplorerCommandProvider_FWD_DEFINED__ = 1
        IID_IExplorerCommandProvider = MIDL_INTERFACE(
            "{64961751-0835-43C0-8FFE-D57686530E64}"
        )
        
        
        class IExplorerCommandProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExplorerCommandProvider


    # END IF  __IExplorerCommandProvider_FWD_DEFINED__

    if not defined(__IOpenControlPanel_FWD_DEFINED__):
        __IOpenControlPanel_FWD_DEFINED__ = 1
        IID_IOpenControlPanel = MIDL_INTERFACE(
            "{D11AD862-66DE-4DF4-BF6C-1F5621996AF1}"
        )
        
        
        class IOpenControlPanel(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IOpenControlPanel


    # END IF  __IOpenControlPanel_FWD_DEFINED__

    if not defined(__IFileSystemBindData_FWD_DEFINED__):
        __IFileSystemBindData_FWD_DEFINED__ = 1
        IID_IFileSystemBindData = MIDL_INTERFACE(
            "{01E18D10-4D8B-11D2-855D-006008059367}"
        )
        
        
        class IFileSystemBindData(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileSystemBindData


    # END IF  __IFileSystemBindData_FWD_DEFINED__

    if not defined(__IFileSystemBindData2_FWD_DEFINED__):
        __IFileSystemBindData2_FWD_DEFINED__ = 1
        IID_IFileSystemBindData2 = MIDL_INTERFACE(
            "{3ACF075F-71DB-4AFA-81F0-3FC4FDF2A5B8}"
        )
        
        
        class IFileSystemBindData2(IFileSystemBindData):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFileSystemBindData2


    # END IF  __IFileSystemBindData2_FWD_DEFINED__

    if not defined(__ICustomDestinationList_FWD_DEFINED__):
        __ICustomDestinationList_FWD_DEFINED__ = 1
        IID_ICustomDestinationList = MIDL_INTERFACE(
            "{6332DEBF-87B5-4670-90C0-5E57B408A49E}"
        )
        
        
        class ICustomDestinationList(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ICustomDestinationList


    # END IF  __ICustomDestinationList_FWD_DEFINED__

    if not defined(__IApplicationDestinations_FWD_DEFINED__):
        __IApplicationDestinations_FWD_DEFINED__ = 1
        IID_IApplicationDestinations = MIDL_INTERFACE(
            "{12337D35-94C6-48A0-BCE7-6A9C69D4D600}"
        )
        
        
        class IApplicationDestinations(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IApplicationDestinations


    # END IF  __IApplicationDestinations_FWD_DEFINED__

    if not defined(__IApplicationDocumentLists_FWD_DEFINED__):
        __IApplicationDocumentLists_FWD_DEFINED__ = 1
        IID_IApplicationDocumentLists = MIDL_INTERFACE(
            "{3C594F9F-9F30-47A1-979A-C9E83D3D0A06}"
        )
        
        
        class IApplicationDocumentLists(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IApplicationDocumentLists


    # END IF  __IApplicationDocumentLists_FWD_DEFINED__

    if not defined(__IObjectWithAppUserModelID_FWD_DEFINED__):
        __IObjectWithAppUserModelID_FWD_DEFINED__ = 1
        IID_IObjectWithAppUserModelID = MIDL_INTERFACE(
            "{36DB0196-9665-46D1-9BA7-D3709EECF9ED}"
        )
        
        
        class IObjectWithAppUserModelID(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IObjectWithAppUserModelID


    # END IF  __IObjectWithAppUserModelID_FWD_DEFINED__

    if not defined(__IObjectWithProgID_FWD_DEFINED__):
        __IObjectWithProgID_FWD_DEFINED__ = 1
        IID_IObjectWithProgID = MIDL_INTERFACE(
            "{71E806FB-8DEE-46FC-BF8C-7748A8A1AE13}"
        )
        
        
        class IObjectWithProgID(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IObjectWithProgID


    # END IF  __IObjectWithProgID_FWD_DEFINED__

    if not defined(__IUpdateIDList_FWD_DEFINED__):
        __IUpdateIDList_FWD_DEFINED__ = 1
        IID_IUpdateIDList = MIDL_INTERFACE(
            "{6589B6D2-5F8D-4B9E-B7E0-23CDD9717D8C}"
        )
        
        
        class IUpdateIDList(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IUpdateIDList


    # END IF  __IUpdateIDList_FWD_DEFINED__

    if not defined(__IDesktopWallpaper_FWD_DEFINED__):
        __IDesktopWallpaper_FWD_DEFINED__ = 1
        IID_IDesktopWallpaper = MIDL_INTERFACE(
            "{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}"
        )
        
        
        class IDesktopWallpaper(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDesktopWallpaper


    # END IF  __IDesktopWallpaper_FWD_DEFINED__

    if not defined(__IHomeGroup_FWD_DEFINED__):
        __IHomeGroup_FWD_DEFINED__ = 1
        IID_IHomeGroup = MIDL_INTERFACE(
            "{7A3BD1D9-35A9-4FB3-A467-F48CAC35E2D0}"
        )
        
        
        class IHomeGroup(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IHomeGroup


    # END IF  __IHomeGroup_FWD_DEFINED__

    if not defined(__IInitializeWithPropertyStore_FWD_DEFINED__):
        __IInitializeWithPropertyStore_FWD_DEFINED__ = 1
        IID_IInitializeWithPropertyStore = MIDL_INTERFACE(
            "{C3E12EB5-7D8D-44F8-B6DD-0E77B34D6DE4}"
        )
        
        
        class IInitializeWithPropertyStore(comtypes.IUnknown):
            """        
    Initialize With IPropertyStore
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInitializeWithPropertyStore


    # END IF  __IInitializeWithPropertyStore_FWD_DEFINED__

    if not defined(__IOpenSearchSource_FWD_DEFINED__):
        __IOpenSearchSource_FWD_DEFINED__ = 1
        IID_IOpenSearchSource = MIDL_INTERFACE(
            "{F0EE7333-E6FC-479B-9F25-A860C234A38E}"
        )
        
        
        class IOpenSearchSource(comtypes.IUnknown):
            """        
    OpenSearch Data Source API
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IOpenSearchSource


    # END IF  __IOpenSearchSource_FWD_DEFINED__

    if not defined(__IShellLibrary_FWD_DEFINED__):
        __IShellLibrary_FWD_DEFINED__ = 1
        IID_IShellLibrary = MIDL_INTERFACE(
            "{11A66EFA-382E-451A-9234-1E0E12EF3085}"
        )
        
        
        class IShellLibrary(comtypes.IUnknown):
            """        
    Shell Library API
            """
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellLibrary


    # END IF  __IShellLibrary_FWD_DEFINED__

    if not defined(__IDefaultFolderMenuInitialize_FWD_DEFINED__):
        __IDefaultFolderMenuInitialize_FWD_DEFINED__ = 1
        IID_IDefaultFolderMenuInitialize = MIDL_INTERFACE(
            "{7690AA79-F8FC-4615-A327-36F7D18F5D91}"
        )
        
        
        class IDefaultFolderMenuInitialize(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDefaultFolderMenuInitialize


    # END IF  __IDefaultFolderMenuInitialize_FWD_DEFINED__

    if not defined(__IApplicationActivationManager_FWD_DEFINED__):
        __IApplicationActivationManager_FWD_DEFINED__ = 1
        IID_IApplicationActivationManager = MIDL_INTERFACE(
            "{2E941141-7F97-4756-BA1D-9DECDE894A3D}"
        )
        
        
        class IApplicationActivationManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IApplicationActivationManager


    # END IF  __IApplicationActivationManager_FWD_DEFINED__

    if not defined(__DesktopWallpaper_FWD_DEFINED__):
        __DesktopWallpaper_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __DesktopWallpaper_FWD_DEFINED__
    if not defined(__ShellDesktop_FWD_DEFINED__):
        __ShellDesktop_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ShellDesktop_FWD_DEFINED__
    if not defined(__ShellFSFolder_FWD_DEFINED__):
        __ShellFSFolder_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ShellFSFolder_FWD_DEFINED__
    if not defined(__NetworkPlaces_FWD_DEFINED__):
        __NetworkPlaces_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __NetworkPlaces_FWD_DEFINED__
    if not defined(__ShellLink_FWD_DEFINED__):
        __ShellLink_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ShellLink_FWD_DEFINED__
    if not defined(__DriveSizeCategorizer_FWD_DEFINED__):
        __DriveSizeCategorizer_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __DriveSizeCategorizer_FWD_DEFINED__
    if not defined(__DriveTypeCategorizer_FWD_DEFINED__):
        __DriveTypeCategorizer_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __DriveTypeCategorizer_FWD_DEFINED__
    if not defined(__FreeSpaceCategorizer_FWD_DEFINED__):
        __FreeSpaceCategorizer_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __FreeSpaceCategorizer_FWD_DEFINED__
    if not defined(__SizeCategorizer_FWD_DEFINED__):
        __SizeCategorizer_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __SizeCategorizer_FWD_DEFINED__
    if not defined(__PropertiesUI_FWD_DEFINED__):
        __PropertiesUI_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __PropertiesUI_FWD_DEFINED__
    if not defined(__UserNotification_FWD_DEFINED__):
        __UserNotification_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __UserNotification_FWD_DEFINED__
    if not defined(__TaskbarList_FWD_DEFINED__):
        __TaskbarList_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __TaskbarList_FWD_DEFINED__
    if not defined(__ShellItem_FWD_DEFINED__):
        __ShellItem_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ShellItem_FWD_DEFINED__
    if not defined(__NamespaceWalker_FWD_DEFINED__):
        __NamespaceWalker_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __NamespaceWalker_FWD_DEFINED__
    if not defined(__FileOperation_FWD_DEFINED__):
        __FileOperation_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __FileOperation_FWD_DEFINED__
    if not defined(__FileOpenDialog_FWD_DEFINED__):
        __FileOpenDialog_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __FileOpenDialog_FWD_DEFINED__
    if not defined(__FileSaveDialog_FWD_DEFINED__):
        __FileSaveDialog_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __FileSaveDialog_FWD_DEFINED__
    if not defined(__KnownFolderManager_FWD_DEFINED__):
        __KnownFolderManager_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __KnownFolderManager_FWD_DEFINED__
    if not defined(__SharingConfigurationManager_FWD_DEFINED__):
        __SharingConfigurationManager_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __SharingConfigurationManager_FWD_DEFINED__
    if not defined(__NetworkConnections_FWD_DEFINED__):
        __NetworkConnections_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __NetworkConnections_FWD_DEFINED__
    if not defined(__ScheduledTasks_FWD_DEFINED__):
        __ScheduledTasks_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ScheduledTasks_FWD_DEFINED__
    if not defined(__ApplicationAssociationRegistration_FWD_DEFINED__):
        __ApplicationAssociationRegistration_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ApplicationAssociationRegistration_FWD_DEFINED__
    if not defined(__SearchFolderItemFactory_FWD_DEFINED__):
        __SearchFolderItemFactory_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __SearchFolderItemFactory_FWD_DEFINED__
    if not defined(__OpenControlPanel_FWD_DEFINED__):
        __OpenControlPanel_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __OpenControlPanel_FWD_DEFINED__
    if not defined(__MailRecipient_FWD_DEFINED__):
        __MailRecipient_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __MailRecipient_FWD_DEFINED__
    if not defined(__NetworkExplorerFolder_FWD_DEFINED__):
        __NetworkExplorerFolder_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __NetworkExplorerFolder_FWD_DEFINED__
    if not defined(__DestinationList_FWD_DEFINED__):
        __DestinationList_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __DestinationList_FWD_DEFINED__
    if not defined(__ApplicationDestinations_FWD_DEFINED__):
        __ApplicationDestinations_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ApplicationDestinations_FWD_DEFINED__
    if not defined(__ApplicationDocumentLists_FWD_DEFINED__):
        __ApplicationDocumentLists_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ApplicationDocumentLists_FWD_DEFINED__
    if not defined(__HomeGroup_FWD_DEFINED__):
        __HomeGroup_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __HomeGroup_FWD_DEFINED__
    if not defined(__ShellLibrary_FWD_DEFINED__):
        __ShellLibrary_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ShellLibrary_FWD_DEFINED__
    if not defined(__AppStartupLink_FWD_DEFINED__):
        __AppStartupLink_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __AppStartupLink_FWD_DEFINED__
    if not defined(__EnumerableObjectCollection_FWD_DEFINED__):
        __EnumerableObjectCollection_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __EnumerableObjectCollection_FWD_DEFINED__
    if not defined(__FrameworkInputPane_FWD_DEFINED__):
        __FrameworkInputPane_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __FrameworkInputPane_FWD_DEFINED__
    if not defined(__DefFolderMenu_FWD_DEFINED__):
        __DefFolderMenu_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __DefFolderMenu_FWD_DEFINED__
    if not defined(__AppVisibility_FWD_DEFINED__):
        __AppVisibility_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __AppVisibility_FWD_DEFINED__
    if not defined(__AppShellVerbHandler_FWD_DEFINED__):
        __AppShellVerbHandler_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __AppShellVerbHandler_FWD_DEFINED__
    if not defined(__ExecuteUnknown_FWD_DEFINED__):
        __ExecuteUnknown_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ExecuteUnknown_FWD_DEFINED__
    if not defined(__PackageDebugSettings_FWD_DEFINED__):
        __PackageDebugSettings_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __PackageDebugSettings_FWD_DEFINED__
    if not defined(__SuspensionDependencyManager_FWD_DEFINED__):
        __SuspensionDependencyManager_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __SuspensionDependencyManager_FWD_DEFINED__
    if not defined(__ApplicationActivationManager_FWD_DEFINED__):
        __ApplicationActivationManager_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ApplicationActivationManager_FWD_DEFINED__
    if not defined(__ApplicationDesignModeSettings_FWD_DEFINED__):
        __ApplicationDesignModeSettings_FWD_DEFINED__ = 1

        if defined(__cplusplus):
            pass
    else:
        # END IF  __cplusplus
    # END IF  __ApplicationDesignModeSettings_FWD_DEFINED__
    if not defined(__IAssocHandlerInvoker_FWD_DEFINED__):
        __IAssocHandlerInvoker_FWD_DEFINED__ = 1
        IID_IAssocHandlerInvoker = MIDL_INTERFACE(
            "{92218CAB-ECAA-4335-8133-807FD234C2EE}"
        )
        
        
        class IAssocHandlerInvoker(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IAssocHandlerInvoker


    # END IF  __IAssocHandlerInvoker_FWD_DEFINED__

    if not defined(__IAssocHandler_FWD_DEFINED__):
        __IAssocHandler_FWD_DEFINED__ = 1
        IID_IAssocHandler = MIDL_INTERFACE(
            "{F04061AC-1659-4A3F-A954-775AA57FC083}"
        )
        
        
        class IAssocHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IAssocHandler


    # END IF  __IAssocHandler_FWD_DEFINED__

    if not defined(__IEnumAssocHandlers_FWD_DEFINED__):
        __IEnumAssocHandlers_FWD_DEFINED__ = 1
        IID_IEnumAssocHandlers = MIDL_INTERFACE(
            "{973810AE-9599-4B88-9E4D-6EE98C9552DA}"
        )
        
        
        class IEnumAssocHandlers(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IEnumAssocHandlers


    # END IF  __IEnumAssocHandlers_FWD_DEFINED__

    if not defined(__IDataObjectProvider_FWD_DEFINED__):
        __IDataObjectProvider_FWD_DEFINED__ = 1
        IID_IDataObjectProvider = MIDL_INTERFACE(
            "{3D25F6D6-4B2A-433C-9184-7C33AD35D001}"
        )
        
        
        class IDataObjectProvider(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDataObjectProvider


    # END IF  __IDataObjectProvider_FWD_DEFINED__

    if not defined(__IDataTransferManagerInterop_FWD_DEFINED__):
        __IDataTransferManagerInterop_FWD_DEFINED__ = 1
        IID_IDataTransferManagerInterop = MIDL_INTERFACE(
            "{3A3DCD6C-3EAB-43DC-BCDE-45671CE800C8}"
        )
        
        
        class IDataTransferManagerInterop(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IDataTransferManagerInterop


    # END IF  __IDataTransferManagerInterop_FWD_DEFINED__

    if not defined(__IFrameworkInputPaneHandler_FWD_DEFINED__):
        __IFrameworkInputPaneHandler_FWD_DEFINED__ = 1
        IID_IFrameworkInputPaneHandler = MIDL_INTERFACE(
            "{226C537B-1E76-4D9E-A760-33DB29922F18}"
        )
        
        
        class IFrameworkInputPaneHandler(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFrameworkInputPaneHandler


    # END IF  __IFrameworkInputPaneHandler_FWD_DEFINED__

    if not defined(__IFrameworkInputPane_FWD_DEFINED__):
        __IFrameworkInputPane_FWD_DEFINED__ = 1
        IID_IFrameworkInputPane = MIDL_INTERFACE(
            "{5752238B-24F0-495A-82F1-2FD593056796}"
        )
        
        
        class IFrameworkInputPane(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IFrameworkInputPane


    # END IF  __IFrameworkInputPane_FWD_DEFINED__

    if not defined(__IAppVisibilityEvents_FWD_DEFINED__):
        __IAppVisibilityEvents_FWD_DEFINED__ = 1
        IID_IAppVisibilityEvents = MIDL_INTERFACE(
            "{6584CE6B-7D82-49C2-89C9-C6BC02BA8C38}"
        )
        
        
        class IAppVisibilityEvents(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IAppVisibilityEvents


    # END IF  __IAppVisibilityEvents_FWD_DEFINED__

    if not defined(__IAppVisibility_FWD_DEFINED__):
        __IAppVisibility_FWD_DEFINED__ = 1
        IID_IAppVisibility = MIDL_INTERFACE(
            "{2246EA2D-CAEA-4444-A3C4-6DE827E44313}"
        )
        
        
        class IAppVisibility(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IAppVisibility


    # END IF  __IAppVisibility_FWD_DEFINED__

    if not defined(__IPackageExecutionStateChangeNotification_FWD_DEFINED__):
        __IPackageExecutionStateChangeNotification_FWD_DEFINED__ = 1
        IID_IPackageExecutionStateChangeNotification = MIDL_INTERFACE(
            "{1BB12A62-2AD8-432B-8CCF-0C2C52AFCD5B}"
        )
        
        
        class IPackageExecutionStateChangeNotification(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPackageExecutionStateChangeNotification


    # END IF  __IPackageExecutionStateChangeNotification_FWD_DEFINED__

    if not defined(__IPackageDebugSettings_FWD_DEFINED__):
        __IPackageDebugSettings_FWD_DEFINED__ = 1
        IID_IPackageDebugSettings = MIDL_INTERFACE(
            "{F27C3930-8029-4AD1-94E3-3DBA417810C1}"
        )
        
        
        class IPackageDebugSettings(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPackageDebugSettings


    # END IF  __IPackageDebugSettings_FWD_DEFINED__

    if not defined(__IPackageDebugSettings2_FWD_DEFINED__):
        __IPackageDebugSettings2_FWD_DEFINED__ = 1
        IID_IPackageDebugSettings2 = MIDL_INTERFACE(
            "{6E3194BB-AB82-4D22-93F5-FABDA40E7B16}"
        )
        
        
        class IPackageDebugSettings2(IPackageDebugSettings):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IPackageDebugSettings2


    # END IF  __IPackageDebugSettings2_FWD_DEFINED__

    if not defined(__ISuspensionDependencyManager_FWD_DEFINED__):
        __ISuspensionDependencyManager_FWD_DEFINED__ = 1
        IID_ISuspensionDependencyManager = MIDL_INTERFACE(
            "{52B83A42-2543-416A-81D9-C0DE7969C8B3}"
        )
        
        
        class ISuspensionDependencyManager(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ISuspensionDependencyManager


    # END IF  __ISuspensionDependencyManager_FWD_DEFINED__

    if not defined(__IExecuteCommandApplicationHostEnvironment_FWD_DEFINED__):
        __IExecuteCommandApplicationHostEnvironment_FWD_DEFINED__ = 1
        IID_IExecuteCommandApplicationHostEnvironment = MIDL_INTERFACE(
            "{18B21AA9-E184-4FF0-9F5E-F882D03771B3}"
        )
        
        
        class IExecuteCommandApplicationHostEnvironment(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExecuteCommandApplicationHostEnvironment


    # END IF  __IExecuteCommandApplicationHostEnvironment_FWD_DEFINED__

    if not defined(__IExecuteCommandHost_FWD_DEFINED__):
        __IExecuteCommandHost_FWD_DEFINED__ = 1
        IID_IExecuteCommandHost = MIDL_INTERFACE(
            "{4B6832A2-5F04-4C9D-B89D-727A15D103E7}"
        )
        
        
        class IExecuteCommandHost(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IExecuteCommandHost


    # END IF  __IExecuteCommandHost_FWD_DEFINED__

    if not defined(__IApplicationDesignModeSettings_FWD_DEFINED__):
        __IApplicationDesignModeSettings_FWD_DEFINED__ = 1
        IID_IApplicationDesignModeSettings = MIDL_INTERFACE(
            "{2A3DEE9A-E31D-46D6-8508-BCC597DB3557}"
        )
        
        
        class IApplicationDesignModeSettings(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IApplicationDesignModeSettings


    # END IF  __IApplicationDesignModeSettings_FWD_DEFINED__

    if not defined(__IApplicationDesignModeSettings2_FWD_DEFINED__):
        __IApplicationDesignModeSettings2_FWD_DEFINED__ = 1
        IID_IApplicationDesignModeSettings2 = MIDL_INTERFACE(
            "{490514E1-675A-4D6E-A58D-E54901B4CA2F}"
        )
        
        
        class IApplicationDesignModeSettings2(IApplicationDesignModeSettings):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IApplicationDesignModeSettings2


    # END IF  __IApplicationDesignModeSettings2_FWD_DEFINED__

    if not defined(__ILaunchTargetMonitor_FWD_DEFINED__):
        __ILaunchTargetMonitor_FWD_DEFINED__ = 1
        IID_ILaunchTargetMonitor = MIDL_INTERFACE(
            "{266FBC7E-490D-46ED-A96B-2274DB252003}"
        )
        
        
        class ILaunchTargetMonitor(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ILaunchTargetMonitor


    # END IF  __ILaunchTargetMonitor_FWD_DEFINED__

    if not defined(__ILaunchSourceViewSizePreference_FWD_DEFINED__):
        __ILaunchSourceViewSizePreference_FWD_DEFINED__ = 1
        IID_ILaunchSourceViewSizePreference = MIDL_INTERFACE(
            "{E5AA01F7-1FB8-4830-8720-4E6734CBD5F3}"
        )
        
        
        class ILaunchSourceViewSizePreference(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ILaunchSourceViewSizePreference


    # END IF  __ILaunchSourceViewSizePreference_FWD_DEFINED__

    if not defined(__ILaunchTargetViewSizePreference_FWD_DEFINED__):
        __ILaunchTargetViewSizePreference_FWD_DEFINED__ = 1
        IID_ILaunchTargetViewSizePreference = MIDL_INTERFACE(
            "{2F0666C6-12F7-4360-B511-A394A0553725}"
        )
        
        
        class ILaunchTargetViewSizePreference(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ILaunchTargetViewSizePreference


    # END IF  __ILaunchTargetViewSizePreference_FWD_DEFINED__

    if not defined(__ILaunchSourceAppUserModelId_FWD_DEFINED__):
        __ILaunchSourceAppUserModelId_FWD_DEFINED__ = 1
        IID_ILaunchSourceAppUserModelId = MIDL_INTERFACE(
            "{989191AC-28FF-4CF0-9584-E0D078BC2396}"
        )
        
        
        class ILaunchSourceAppUserModelId(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_ILaunchSourceAppUserModelId


    # END IF  __ILaunchSourceAppUserModelId_FWD_DEFINED__

    if not defined(__IInitializeWithWindow_FWD_DEFINED__):
        __IInitializeWithWindow_FWD_DEFINED__ = 1
        IID_IInitializeWithWindow = MIDL_INTERFACE(
            "{3E68D4BD-7135-4D10-8018-9FB6D9F33FA1}"
        )
        
        
        class IInitializeWithWindow(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IInitializeWithWindow


    # END IF  __IInitializeWithWindow_FWD_DEFINED__

    if not defined(__IHandlerInfo_FWD_DEFINED__):
        __IHandlerInfo_FWD_DEFINED__ = 1
        IID_IHandlerInfo = MIDL_INTERFACE(
            "{997706EF-F880-453B-8118-39E1A2D2655A}"
        )
        
        
        class IHandlerInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IHandlerInfo


    # END IF  __IHandlerInfo_FWD_DEFINED__

    if not defined(__IHandlerActivationHost_FWD_DEFINED__):
        __IHandlerActivationHost_FWD_DEFINED__ = 1
        IID_IHandlerActivationHost = MIDL_INTERFACE(
            "{35094A87-8BB1-4237-96C6-C417EEBDB078}"
        )
        
        
        class IHandlerActivationHost(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IHandlerActivationHost


    # END IF  __IHandlerActivationHost_FWD_DEFINED__

    if not defined(__IAppActivationUIInfo_FWD_DEFINED__):
        __IAppActivationUIInfo_FWD_DEFINED__ = 1
        IID_IAppActivationUIInfo = MIDL_INTERFACE(
            "{ABAD189D-9FA3-4278-B3CA-8CA448A88DCB}"
        )
        
        
        class IAppActivationUIInfo(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IAppActivationUIInfo


    # END IF  __IAppActivationUIInfo_FWD_DEFINED__

    if not defined(__IContactManagerInterop_FWD_DEFINED__):
        __IContactManagerInterop_FWD_DEFINED__ = 1
        IID_IContactManagerInterop = MIDL_INTERFACE(
            "{99EACBA7-E073-43B6-A896-55AFE48A0833}"
        )
        
        
        class IContactManagerInterop(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IContactManagerInterop


    # END IF  __IContactManagerInterop_FWD_DEFINED__

    if not defined(__IShellIconOverlayIdentifier_FWD_DEFINED__):
        __IShellIconOverlayIdentifier_FWD_DEFINED__ = 1
        IID_IShellIconOverlayIdentifier = MIDL_INTERFACE(
            "{0C6C4200-C589-11D0-999A-00C04FD655E1}"
        )
        
        
        class IShellIconOverlayIdentifier(comtypes.IUnknown):
            _case_insensitive_ = True
            _idlflags_ = []
            _iid_ = IID_IShellIconOverlayIdentifier


    # END IF  __IShellIconOverlayIdentifier_FWD_DEFINED__

    # header files for imported files

    if defined(__cplusplus):
        pass
    # END IF

    # interface __MIDL_itf_shobjidl_core_0000_0000

    # [local]
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        if not defined(SHSTDAPI):
            if defined(_SHELL32_):
                SHSTDAPI = STDAPI
                

def SHSTDAPI_(type):
    return STDAPI_type
        else:
                SHSTDAPI = EXTERN_C DECLSPEC_IMPORT HRESULT STDAPICALLTYPE
                

def SHSTDAPI_(type):
    return EXTERN_C DECLSPEC_IMPORT type STDAPICALLTYPE
            # END IF
        # END IF   SHSTDAPI

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =

        # IContextMenu interface

        # [OverView]

        # The shell uses the IContextMenu interface in following three cases.

        # case - 1: The shell is loading context menu extensions.

        # When the user clicks the right mouse button on an item within the
        # shell's

        # name space (i.g., file, directory, server, work - group, etc.), it
        # creates

        # the default context menu for its type, then loads context menu
        # extensions

        # that are registered for that type (and its base type) so that they
        # can

        # add extra menu items. Those context menu extensions are registered at

        # HKCR\{ProgID}\shellex\ContextMenuHandlers.

        # case - 2: The shell is retrieving a context menu of sub - folders in
        # extended

        # name - space.

        # When the explorer's name space is extended by name space extensions,

        # the shell calls their IShellFolder::GetUIObjectOf to get the
        # IContextMenu

        # objects when it creates context menus for folders under those
        # extended

        # name spaces.

        # case - 3: The shell is loading non - default drag and drop handler
        # for directories.

        # When the user performed a non - default drag and drop onto one of
        # file

        # system folders (i.e., directories), it loads shell extensions that
        # are

        # registered at HKCR\{ProgID}\DragDropHandlers.

        # [Member functions]

        # IContextMenu::QueryContextMenu

        # This member function may insert one or more menuitems to the
        # specified

        # menu (hmenu) at the specified location
        # (indexMenu which is never be - 1).

        # The IDs of those menuitem must be in the specified range
        # (idCmdFirst and

        # idCmdLast). It returns the maximum menuitem ID offset (uSHORT) in the

        # 'code' field (low word) of the scode.

        # The uFlags specify the context. It may have one or more of following

        # flags.

        # CMF_DEFAULTONLY: This flag is passed if the user is invoking the
        # default

        # action (typically by DOUBLE - clicking, case 1 and 2 only). Context
        # menu

        # extensions (case 1) should not add any menu items, and returns S_OK.

        # CMF_VERBSONLY: The explorer passes this flag if it is constructing

        # a context menu for a SHORT - cut object (case 1 and case 2 only). If
        # this

        # flag is passed, it should not add any menu - items that is not
        # appropriate

        # from a SHORT - cut.

        # A good example is the Delete menuitem, which confuses the user

        # because it is not clear whether it deletes the link source item or
        # the

        # link itself.

        # CMF_EXPLORER: The explorer passes this flag if it has the left -
        # side pane

        # (case 1 and 2 only). Context menu extensions should ignore this flag.

        # High word (16 - bit) are reserved for context specific communications

        # and the rest of flags (13 - bit) are reserved by the system.

        # IContextMenu::InvokeCommand

        # This member is called when the user has selected one of menuitems
        # that

        # are inserted by previous QueryContextMenu member. In this case, the

        # LOWORD(lpici - >lpVerb) contains the menuitem ID offset
        # (menuitem ID -

        # idCmdFirst).

        # This member function may also be called programmatically. In such a
        # case,

        # lpici - >lpVerb specifies the canonical name of the command to be
        # invoked,

        # which is typically retrieved by GetCommandString member previously.

        # Parameters in lpci:

        # cbSize - - Specifies the size of this structure
        # (ctypes.sizeof(*lpci))

        # hwnd - - Specifies the owner window for any message/dialog box.

        # fMask - - Specifies whether or not dwHotkey/hIcon paramter is valid.

        # lpVerb - - Specifies the command to be invoked.

        # lpParameters - - Parameters (optional)

        # lpDirectory - - Working directory (optional)

        # nShow - - Specifies the flag to be passed to ShowWindow (SW_*).

        # dwHotKey - - Hot key to be asINT to the app after invoked (optional).

        # hIcon - - Specifies the icon (optional).

        # hMonitor - - Specifies the default monitor (optional).

        # IContextMenu::GetCommandString

        # This member function is called by the explorer either to get the

        # canonical (language independent) command name (uFlags == GCS_VERB) or

        # the help text ((uFlags & GCS_HELPTEXT) != 0) for the specified
        # command.

        # The retrieved canonical string may be passed to its InvokeCommand

        # member function to invoke a command programmatically. The explorer

        # displays the help texts in its status bar; therefore, the length of

        # the help text should be reasonably SHORT (<40 CHARacters).

        # Parameters:

        # idCmd - - Specifies menuitem ID offset (from idCmdFirst)

        # uFlags - - Either GCS_VERB or GCS_HELPTEXT

        # pwReserved - - Reserved
        # (must pass NULL when calling, must ignore when called)

        # pszName - - Specifies the string buffer.

        # cchMax - - Specifies the size of the string buffer.

        # == == == == == == == == == == == == == == == == == == == == == == ==
        # == == == == == == == == == == == == == == =

        # QueryContextMenu uFlags
        CMF_NORMAL = 0x00000000
        CMF_DEFAULTONLY = 0x00000001
        CMF_VERBSONLY = 0x00000002
        CMF_EXPLORE = 0x00000004
        CMF_NOVERBS = 0x00000008
        CMF_CANRENAME = 0x00000010
        CMF_NODEFAULT = 0x00000020

        if (NTDDI_VERSION < NTDDI_VISTA):
            CMF_INCLUDESTATIC = 0x00000040
        # END IF

        if (NTDDI_VERSION >= NTDDI_VISTA):
            CMF_ITEMMENU = 0x00000080
        # END IF
        CMF_EXTENDEDVERBS = 0x00000100

        if (NTDDI_VERSION >= NTDDI_VISTA):
            CMF_DISABLEDVERBS = 0x00000200
        # END IF
        CMF_ASYNCVERBSTATE = 0x00000400
        CMF_OPTIMIZEFORINVOKE = 0x00000800
        CMF_SYNCCASCADEMENU = 0x00001000
        CMF_DONOTPICKDEFAULT = 0x00002000
        CMF_RESERVED = 0xFFFF0000

        # GetCommandString uFlags
        GCS_VERBA = 0x00000000
        GCS_HELPTEXTA = 0x00000001
        GCS_VALIDATEA = 0x00000002
        GCS_VERBW = 0x00000004
        GCS_HELPTEXTW = 0x00000005
        GCS_VALIDATEW = 0x00000006
        GCS_VERBICONW = 0x00000014
        GCS_UNICODE = 0x00000004

        if defined(UNICODE):
            GCS_VERB = GCS_VERBW
            GCS_HELPTEXT = GCS_HELPTEXTW
            GCS_VALIDATE = GCS_VALIDATEW
    else:
            # GCS_VERB = GCS_VERBA
            # GCS_HELPTEXT = GCS_HELPTEXTA
            # GCS_VALIDATE = GCS_VALIDATEA
        # END IF
        CMDSTR_NEWFOLDERA = "NewFolder"
        CMDSTR_VIEWLISTA = "ViewList"
        CMDSTR_VIEWDETAILSA = "ViewDetails"
        CMDSTR_NEWFOLDERW = "NewFolder"
        CMDSTR_VIEWLISTW = "ViewList"
        CMDSTR_VIEWDETAILSW = "ViewDetails"

        if defined(UNICODE):
            CMDSTR_NEWFOLDER = CMDSTR_NEWFOLDERW
            CMDSTR_VIEWLIST = CMDSTR_VIEWLISTW
            CMDSTR_VIEWDETAILS = CMDSTR_VIEWDETAILSW
    else:
            # CMDSTR_NEWFOLDER = CMDSTR_NEWFOLDERA
            # CMDSTR_VIEWLIST = CMDSTR_VIEWLISTA
            # CMDSTR_VIEWDETAILS = CMDSTR_VIEWDETAILSA
        # END IF
        CMIC_MASK_HOTKEY = SEE_MASK_HOTKEY
        CMIC_MASK_ICON = SEE_MASK_ICON
        CMIC_MASK_FLAG_NO_UI = SEE_MASK_FLAG_NO_UI
        CMIC_MASK_UNICODE = SEE_MASK_UNICODE
        CMIC_MASK_NO_CONSOLE = SEE_MASK_NO_CONSOLE

        if (NTDDI_VERSION < NTDDI_VISTA):
            CMIC_MASK_HASLINKNAME = SEE_MASK_HASLINKNAME
            CMIC_MASK_HASTITLE = SEE_MASK_HASTITLE
        # END IF   NTDDI_VISTA
        CMIC_MASK_FLAG_SEP_VDM = SEE_MASK_FLAG_SEPVDM
        CMIC_MASK_ASYNCOK = SEE_MASK_ASYNCOK

        if (NTDDI_VERSION >= NTDDI_VISTA):
            CMIC_MASK_NOASYNC = SEE_MASK_NOASYNC
        # END IF
        CMIC_MASK_SHIFT_DOWN = 0x10000000
        CMIC_MASK_CONTROL_DOWN = 0x40000000
        CMIC_MASK_FLAG_LOG_USAGE = SEE_MASK_FLAG_LOG_USAGE
        CMIC_MASK_NOZONECHECKS = SEE_MASK_NOZONECHECKS
        CMIC_MASK_PTINVOKE = 0x20000000

        if not defined(HMONITOR_DECLARED) and not defined(HMONITOR) and (WINVER < 0x0500):
            HMONITOR_DECLARED = 1
        # END IF
        class _CMINVOKECOMMANDINFO(ctypes.Structure):
            pass
        _CMINVOKECOMMANDINFO._fields_ = [
            ('cbSize', DWORD),
            ('fMask', DWORD),
            ('hwnd', HWND),
            ('lpVerb', LPCSTR),
            ('lpParameters', LPCSTR),
            ('lpDirectory', LPCSTR),
            ('nShow', INT),
            ('dwHotKey', DWORD),
            ('hIcon', HANDLE),
        ]


        CMINVOKECOMMANDINFO = _CMINVOKECOMMANDINFO


        class _CMINVOKECOMMANDINFOEX(ctypes.Structure):
            pass
        _CMINVOKECOMMANDINFOEX._fields_ = [
            ('cbSize', DWORD),
            ('fMask', DWORD),
            ('hwnd', HWND),
            ('lpVerb', LPCSTR),
            ('lpParameters', LPCSTR),
            ('lpDirectory', LPCSTR),
            ('nShow', INT),
            ('dwHotKey', DWORD),
            ('hIcon', HANDLE),
            ('lpTitle', LPCSTR),
            ('lpVerbW', LPCWSTR),
            ('lpParametersW', LPCWSTR),
            ('lpDirectoryW', LPCWSTR),
            ('lpTitleW', LPCWSTR),
            ('ptInvoke', POINT),
        ]


        CMINVOKECOMMANDINFOEX = _CMINVOKECOMMANDINFOEX



        if not defined(__IContextMenu_INTERFACE_DEFINED__):
            __IContextMenu_INTERFACE_DEFINED__ = 1

            # interface IContextMenu

            # [object][unique][uuid][local]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]

                # [annotation][in]
            else: # C style interface
                IContextMenu._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'QueryContextMenu',
                        ([annotation('_In_'), 'in'], HMENU, 'hmenu'),
                        ([], UINT, 'indexMenu'),
                        ([], UINT, 'idCmdFirst'),
                        ([], UINT, 'idCmdLast'),
                        ([], UINT, 'uFlags'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'InvokeCommand',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(CMINVOKECOMMANDINFO),
                           'pici'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCommandString',
                        ([annotation('_In_'), 'in'], UINT_PTR, 'idCmd'),
                        ([], UINT, 'uType'),
                        (
                            [annotation('_Reserved_'), 'in'],
                            POINTER(UINT),
                           ' pReserved'
                        ),
                        (
                            ['out', annotation('_Out_writes_bytes_((uType & GCS_UNICODE) ? (cchMax * ctypes.sizeof(WCHAR)) : cchMax) _When_(not (uType & (GCS_VALIDATEA | GCS_VALIDATEW)), _Null_terminated_))],
                            POINTER(CHAR),
                           'pszName'
                        ),
                        ([], UINT, 'cchMax'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IContextMenu_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0001

        # [local]
        if not defined(__IContextMenu2_INTERFACE_DEFINED__):
            __IContextMenu2_INTERFACE_DEFINED__ = 1

            # interface IContextMenu2

            # [object][unique][uuid][local]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            else: # C style interface
                IContextMenu2._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'HandleMenuMsg',
                        ([annotation('_In_'), 'in'], UINT, 'uMsg'),
                        ([], WPARAM, 'wParam'),
                        ([], LPARAM, 'lParam'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IContextMenu2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0002

        # [local]
        if not defined(__IContextMenu3_INTERFACE_DEFINED__):
            __IContextMenu3_INTERFACE_DEFINED__ = 1

            # interface IContextMenu3

            # [object][unique][uuid][local]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]
            else: # C style interface
                IContextMenu3._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'HandleMenuMsg2',
                        ([annotation('_In_'), 'in'], UINT, 'uMsg'),
                        ([], WPARAM, 'wParam'),
                        ([], LPARAM, 'lParam'),
                        (
                            ['out', annotation('_Out_opt_')],
                            POINTER(LRESULT),
                           'plResult'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IContextMenu3_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0003

        # [local]
        if not defined(__IExecuteCommand_INTERFACE_DEFINED__):
            __IExecuteCommand_INTERFACE_DEFINED__ = 1

            # interface IExecuteCommand

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IExecuteCommand._methods_ = [
                    # key state values MK_CONTROL & MK_SHIFT
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetKeyState',
                        (['in'], DWORD, 'grfKeyState'),
                    ),

                    # for context menu invokes this comes from
                    # CMINVOKECOMMANDINFO.lpParameters                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetParameters',
                        (['in'], LPCWSTR, 'pszParameters'),
                    ),

                    # default Position = center of default monitor                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetPosition',
                        (['in'], POINT, 'pt'),
                    ),

                    # default = SW_NORMAL                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetShowWindow',
                        (['in'], INT, 'nShow'),
                    ),

                    # default = FALSE                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetNoShowUI',
                        (['in'], BOOL, 'fNoShowUI'),
                    ),

                    # default Directory = GetCurrentDirectory()                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetDirectory',
                        (['in'], LPCWSTR, 'pszDirectory'),
                    ),

                    # this is where the work happensnot                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Execute',
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IExecuteCommand_INTERFACE_DEFINED__
        if not defined(__IPersistFolder_INTERFACE_DEFINED__):
            __IPersistFolder_INTERFACE_DEFINED__ = 1

            # interface IPersistFolder

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IPersistFolder._methods_ = [

                    # IShellFolder::BindToObject when it is initializing a
                    # shell folder object.")
                    # called when the explorer is initializing a shell folder
                    # object.
                    # pidl - - Specifies the absolute location of the folder                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], PCIDLIST_ABSOLUTE, 'pidl'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IPersistFolder_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0005

        # [local]
        IRTIR_TASK_NOT_RUNNING = 0
        IRTIR_TASK_RUNNING = 1
        IRTIR_TASK_SUSPENDED = 2
        IRTIR_TASK_PENDING = 3
        IRTIR_TASK_FINISHED = 4

        if not defined(__IRunnableTask_INTERFACE_DEFINED__):
            __IRunnableTask_INTERFACE_DEFINED__ = 1

            # interface IRunnableTask

            # [local][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]
            else: # C style interface
                IRunnableTask._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Run',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Kill',
                        ([annotation('_In_'), 'in'], BOOL, 'bWait'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Suspend',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Resume',
                    ),
                
                    COMMETHOD(
                        [],
                        ULONG,
                        'IsRunning',
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IRunnableTask_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0006

        # [local]
        TOID_NULL = GUID_NULL
        ITSAT_DEFAULT_LPARAM = (DWORD_PTR) - 1
        ITSAT_DEFAULT_PRIORITY = 0x10000000
        ITSAT_MAX_PRIORITY = 0x7FFFFFFF
        ITSAT_MIN_PRIORITY = 0x00000000
        ITSSFLAG_COMPLETE_ON_DESTROY = 0x0000
        ITSSFLAG_KILL_ON_DESTROY = 0x0001
        ITSSFLAG_FLAGS_MASK = 0x0003
        ITSS_THREAD_DESTROY_DEFAULT_TIMEOUT = 10*1000
        ITSS_THREAD_TERMINATE_TIMEOUT = INFINITE
        ITSS_THREAD_TIMEOUT_NO_CHANGE = INFINITE - 1

        if not defined(__IShellTaskScheduler_INTERFACE_DEFINED__):
            __IShellTaskScheduler_INTERFACE_DEFINED__ = 1

            # interface IShellTaskScheduler

            # [local][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            else: # C style interface
                IShellTaskScheduler._methods_ = [

                    # Adds Tasks to the scheduler's background queue. The
                    # TASKOWNERID allow particular types
                    # of tasks to be grouped so that they can be counted or
                    # removed. The lParam allows the task
                    # to be associated with a particular item
                    # (for example an item in a listview). Thus, all
                    # tasks owned by a particular item can be accessed by
                    # passing a non default value for this
                    # parameter (i.e. to RemoveTasks()).
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'AddTask',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IRunnableTask),
                           'prt'
                        ),
                        ([], REFTASKOWNERID, 'rtoid'),
                        ([], DWORD_PTR, 'lParam'),
                        ([], DWORD, 'dwPriority'),
                    ),

                    # Removes tasks from the scheduler's queue. These can be
                    # sepcified in terms of their TASKOWNERID
                    # or their LPARAM, or both, or neither
                    # (TOID_NULL and ITSAT_DEFAULT_LPARAM results in all tasks being
                    # 
                    # removed). If a task that matches is currently running and ITaskScheduler::Status() has been
                    # 
                    # passeed ITSSFLAG_KILL_ON_DESTROY then the scheduler will
                    # attempt to kill the current task. The
                    # fWaitIfRunning parameter is then passed to
                    # IRunnableTask::Kill().
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveTasks',
                        ([annotation('_In_'), 'in'], REFTASKOWNERID, 'rtoid'),
                        ([], DWORD_PTR, 'lParam'),
                        ([], BOOL, 'bWaitIfRunning'),
                    ),

                    # returns the count of tasks in the queue depending upon
                    # the TASKOWNERID and the LPARAM passed.
                    # pass TOID_NULL to count all tasks in the queue                
                    COMMETHOD(
                        [],
                        UINT,
                        'CountTasks',
                        ([annotation('_In_'), 'in'], REFTASKOWNERID, 'rtoid'),
                    ),

                    # This sets the ReleaseStatus for the current task and the
                    # background thread timeout. When
                    # ITaskScheduler::RemoveTasks() is called and there is a
                    # task currently running that matches
                    # ITSSFLAG_COMPLETE_ON_DESTROY will cause TRUE to be
                    # passed to the task's IRunnableTask::Kill().
                    # The dwThreadTimeout parameter if not set to the default
                    # will cause the background thread to
                    # die if no new tasks have been added to the queue in the
                    # timeout period. The Thread will be
                    # recreated when the next new task is added.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Status',
                        (
                            [annotation('_In_'), 'in'],
                            DWORD,
                           'dwReleaseStatus'
                        ),
                        ([], DWORD, 'dwThreadTimeout'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IShellTaskScheduler_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0007

        # [local]
        SID_ShellTaskScheduler = IID_IShellTaskScheduler

        if not defined(__IPersistFolder2_INTERFACE_DEFINED__):
            __IPersistFolder2_INTERFACE_DEFINED__ = 1

            # interface IPersistFolder2

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IPersistFolder2._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCurFolder',
                        (['out'], POINTER(PIDLIST_ABSOLUTE), 'ppidl'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IPersistFolder2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0008

        # [local]
        CSIDL_FLAG_PFTI_TRACKTARGET = CSIDL_FLAG_DONT_VERIFY
        class _PERSIST_FOLDER_TARGET_INFO(ctypes.Structure):
            pass
        _PERSIST_FOLDER_TARGET_INFO._fields_ = [
            ('pidlTargetFolder', PIDLIST_ABSOLUTE),
            ('szTargetParsingName', WCHAR * 260),
            ('szNetworkProvider', WCHAR * 260),
            ('dwAttributes', DWORD),
            ('csidl', INT),
        ]


        PERSIST_FOLDER_TARGET_INFO = _PERSIST_FOLDER_TARGET_INFO



        if not defined(__IPersistFolder3_INTERFACE_DEFINED__):
            __IPersistFolder3_INTERFACE_DEFINED__ = 1

            # interface IPersistFolder3

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IPersistFolder3._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'InitializeEx',
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        (['in'], PCIDLIST_ABSOLUTE, 'pidlRoot'),
                        ([], POINTER(PERSIST_FOLDER_TARGET_INFO), 'ppfti'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFolderTargetInfo',
                        (
                            ['out'],
                            POINTER(PERSIST_FOLDER_TARGET_INFO),
                           'ppfti'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IPersistFolder3_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0009

        # [local]
        if (NTDDI_VERSION >= NTDDI_WINXP) or (_WIN32_IE >= _WIN32_IE_IE70):
            if not defined(__IPersistIDList_INTERFACE_DEFINED__):
                __IPersistIDList_INTERFACE_DEFINED__ = 1

                # interface IPersistIDList

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IPersistIDList._methods_ = [
                        # sets or gets a fully qualifed idlist for an object
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetIDList',
                            (['in'], PCIDLIST_ABSOLUTE, 'pidl'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetIDList',
                            (['out'], POINTER(PIDLIST_ABSOLUTE), 'ppidl'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IPersistIDList_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0010

            # [local]
        # END IF   NTDDI_WINXP or  (_WIN32_IE >= _WIN32_IE_IE70)
        if not defined(__IEnumIDList_INTERFACE_DEFINED__):
            __IEnumIDList_INTERFACE_DEFINED__ = 1

            # interface IEnumIDList

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][length_is][size_is][out]

                # [annotation][out]
            else: # C style interface
                IEnumIDList._methods_ = [
                    #
                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'Next',
                        ([annotation('_In_'), 'in'], ULONG, 'celt'),
                        (
                            ['out', annotation('_Out_writes_to_(celt, *pceltFetched)), 'in', 'out'],
                            POINTER(PITEMID_CHILD),
                           'rgelt'
                        ),
                        (
                            ['out', annotation('_Out_opt_ _Deref_out_range_(0, celt))],
                            POINTER(ULONG),
                           'pceltFetched'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoteNext',
                        (['in'], ULONG, 'celt'),
                        (
                            ['out', 'in', 'out'],
                            POINTER(PITEMID_CHILD),
                           'rgelt'
                        ),
                        (['out'], POINTER(ULONG), 'pceltFetched'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'celt'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Reset',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Clone',
                        (['out'], POINTER(POINTER(IEnumIDList)), 'ppenum'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][length_is][size_is][out]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IEnumIDList_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0011

        # [local]
        if not defined(__IEnumFullIDList_INTERFACE_DEFINED__):
            __IEnumFullIDList_INTERFACE_DEFINED__ = 1

            # interface IEnumFullIDList

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][length_is][size_is][out]

                # [annotation][out]
            else: # C style interface
                IEnumFullIDList._methods_ = [
                    #
                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'Next',
                        ([annotation('_In_'), 'in'], ULONG, 'celt'),
                        (
                            ['out', annotation('_Out_writes_to_(celt, *pceltFetched)), 'in', 'out'],
                            POINTER(PIDLIST_ABSOLUTE),
                           'rgelt'
                        ),
                        (
                            ['out', annotation('_Out_opt_ _Deref_out_range_(0, celt))],
                            POINTER(ULONG),
                           'pceltFetched'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoteNext',
                        (['in'], ULONG, 'celt'),
                        (
                            ['out', 'in', 'out'],
                            POINTER(PIDLIST_ABSOLUTE),
                           'rgelt'
                        ),
                        (['out'], POINTER(ULONG), 'pceltFetched'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'celt'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Reset',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumFullIDList)),
                           'ppenum'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][length_is][size_is][out]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IEnumFullIDList_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0012

        # [local]

        # [v1_enum]
        class _SHGDNF(ENUM):
            SHGDN_NORMAL = 0
            SHGDN_INFOLDER = 0x1
            SHGDN_FOREDITING = 0x1000
            SHGDN_FORADDRESSBAR = 0x4000
            SHGDN_FORPARSING = 0x8000


        SHGDN_NORMAL = _SHGDNF.SHGDN_NORMAL
        SHGDN_INFOLDER = _SHGDNF.SHGDN_INFOLDER
        SHGDN_FOREDITING = _SHGDNF.SHGDN_FOREDITING
        SHGDN_FORADDRESSBAR = _SHGDNF.SHGDN_FORADDRESSBAR
        SHGDN_FORPARSING = _SHGDNF.SHGDN_FORPARSING

        # [v1_enum]
        class _SHCONTF(ENUM):
            SHCONTF_CHECKING_FOR_CHILDREN = 0x10
            SHCONTF_FOLDERS = 0x20
            SHCONTF_NONFOLDERS = 0x40
            SHCONTF_INCLUDEHIDDEN = 0x80
            SHCONTF_INIT_ON_FIRST_NEXT = 0x100
            SHCONTF_NETPRINTERSRCH = 0x200
            SHCONTF_SHAREABLE = 0x400
            SHCONTF_STORAGE = 0x800
            SHCONTF_NAVIGATION_ENUM = 0x1000
            SHCONTF_FASTITEMS = 0x2000
            SHCONTF_FLATLIST = 0x4000
            SHCONTF_ENABLE_ASYNC = 0x8000
            SHCONTF_INCLUDESUPERHIDDEN = 0x10000


        SHCONTF_CHECKING_FOR_CHILDREN = _SHCONTF.SHCONTF_CHECKING_FOR_CHILDREN
        SHCONTF_FOLDERS = _SHCONTF.SHCONTF_FOLDERS
        SHCONTF_NONFOLDERS = _SHCONTF.SHCONTF_NONFOLDERS
        SHCONTF_INCLUDEHIDDEN = _SHCONTF.SHCONTF_INCLUDEHIDDEN
        SHCONTF_INIT_ON_FIRST_NEXT = _SHCONTF.SHCONTF_INIT_ON_FIRST_NEXT
        SHCONTF_NETPRINTERSRCH = _SHCONTF.SHCONTF_NETPRINTERSRCH
        SHCONTF_SHAREABLE = _SHCONTF.SHCONTF_SHAREABLE
        SHCONTF_STORAGE = _SHCONTF.SHCONTF_STORAGE
        SHCONTF_NAVIGATION_ENUM = _SHCONTF.SHCONTF_NAVIGATION_ENUM
        SHCONTF_FASTITEMS = _SHCONTF.SHCONTF_FASTITEMS
        SHCONTF_FLATLIST = _SHCONTF.SHCONTF_FLATLIST
        SHCONTF_ENABLE_ASYNC = _SHCONTF.SHCONTF_ENABLE_ASYNC
        SHCONTF_INCLUDESUPERHIDDEN = _SHCONTF.SHCONTF_INCLUDESUPERHIDDEN
        SHCIDS_ALLFIELDS = 0x80000000
        SHCIDS_CANONICALONLY = 0x10000000
        SHCIDS_BITMASK = 0xFFFF0000
        SHCIDS_COLUMNMASK = 0x0000FFFF
        SFGAO_CANCOPY = DROPEFFECT_COPY
        SFGAO_CANMOVE = DROPEFFECT_MOVE
        SFGAO_CANLINK = DROPEFFECT_LINK
        SFGAO_STORAGE = 0x00000008
        SFGAO_CANRENAME = 0x00000010
        SFGAO_CANDELETE = 0x00000020
        SFGAO_HASPROPSHEET = 0x00000040
        SFGAO_DROPTARGET = 0x00000100
        SFGAO_CAPABILITYMASK = 0x00000177
        SFGAO_PLACEHOLDER = 0x00000800
        SFGAO_SYSTEM = 0x00001000
        SFGAO_ENCRYPTED = 0x00002000
        SFGAO_ISSLOW = 0x00004000
        SFGAO_GHOSTED = 0x00008000
        SFGAO_LINK = 0x00010000
        SFGAO_SHARE = 0x00020000
        SFGAO_READONLY = 0x00040000
        SFGAO_HIDDEN = 0x00080000
        SFGAO_DISPLAYATTRMASK = 0x000FC000
        SFGAO_FILESYSANCESTOR = 0x10000000
        SFGAO_FOLDER = 0x20000000
        SFGAO_FILESYSTEM = 0x40000000
        SFGAO_HASSUBFOLDER = 0x80000000
        SFGAO_CONTENTSMASK = 0x80000000
        SFGAO_VALIDATE = 0x01000000
        SFGAO_REMOVABLE = 0x02000000
        SFGAO_COMPRESSED = 0x04000000
        SFGAO_BROWSABLE = 0x08000000
        SFGAO_NONENUMERATED = 0x00100000
        SFGAO_NEWCONTENT = 0x00200000
        SFGAO_CANMONIKER = 0x00400000
        SFGAO_HASSTORAGE = 0x00400000
        SFGAO_STREAM = 0x00400000
        SFGAO_STORAGEANCESTOR = 0x00800000
        SFGAO_STORAGECAPMASK = 0x70C50008
        SFGAO_PKEYSFGAOMASK = 0x81044000


        class SYNC_TRANSFER_STATUS(ENUM):
            STS_NONE = 0
            STS_NEEDSUPLOAD = 0x1
            STS_NEEDSDOWNLOAD = 0x2
            STS_TRANSFERRING = 0x4
            STS_PAUSED = 0x8
            STS_HASERROR = 0x10
            STS_FETCHING_METADATA = 0x20
            STS_USER_REQUESTED_REFRESH = 0x40
            STS_HASWARNING = 0x80
            STS_EXCLUDED = 0x100
            STS_INCOMPLETE = 0x200


        STS_NONE = SYNC_TRANSFER_STATUS.STS_NONE
        STS_NEEDSUPLOAD = SYNC_TRANSFER_STATUS.STS_NEEDSUPLOAD
        STS_NEEDSDOWNLOAD = SYNC_TRANSFER_STATUS.STS_NEEDSDOWNLOAD
        STS_TRANSFERRING = SYNC_TRANSFER_STATUS.STS_TRANSFERRING
        STS_PAUSED = SYNC_TRANSFER_STATUS.STS_PAUSED
        STS_HASERROR = SYNC_TRANSFER_STATUS.STS_HASERROR
        STS_FETCHING_METADATA = SYNC_TRANSFER_STATUS.STS_FETCHING_METADATA
        STS_USER_REQUESTED_REFRESH = SYNC_TRANSFER_STATUS.STS_USER_REQUESTED_REFRESH
        STS_HASWARNING = SYNC_TRANSFER_STATUS.STS_HASWARNING
        STS_EXCLUDED = SYNC_TRANSFER_STATUS.STS_EXCLUDED
        STS_INCOMPLETE = SYNC_TRANSFER_STATUS.STS_INCOMPLETE
        class STORAGE_PROVIDER_FILE_FLAGS(ENUM):
            SPFF_NONE = 0
            SPFF_DOWNLOAD_BY_DEFAULT = 0x1
            SPFF_CREATED_ON_THIS_DEVICE = 0x2


        SPFF_NONE = STORAGE_PROVIDER_FILE_FLAGS.SPFF_NONE
        SPFF_DOWNLOAD_BY_DEFAULT = STORAGE_PROVIDER_FILE_FLAGS.SPFF_DOWNLOAD_BY_DEFAULT
        SPFF_CREATED_ON_THIS_DEVICE = STORAGE_PROVIDER_FILE_FLAGS.SPFF_CREATED_ON_THIS_DEVICE
        class PLACEHOLDER_STATES(ENUM):
            PS_NONE = 0
            PS_MARKED_FOR_OFFLINE_AVAILABILITY = 0x1
            PS_FULL_PRIMARY_STREAM_AVAILABLE = 0x2
            PS_CREATE_FILE_ACCESSIBLE = 0x4
            PS_CLOUDFILE_PLACEHOLDER = 0x8
            #~#~#~ PS_DEFAULT    = ( ( PS_MARKED_FOR_OFFLINE_AVAILABILITY | PS_FULL_PRIMARY_STREAM_AVAILABLE )  | PS_CREATE_FILE_ACCESSIBLE )
            #~#~#~ PS_ALL    = ( ( ( PS_MARKED_FOR_OFFLINE_AVAILABILITY | PS_FULL_PRIMARY_STREAM_AVAILABLE )  | PS_CREATE_FILE_ACCESSIBLE )  | PS_CLOUDFILE_PLACEHOLDER )


        PS_NONE = PLACEHOLDER_STATES.PS_NONE
        PS_MARKED_FOR_OFFLINE_AVAILABILITY = PLACEHOLDER_STATES.PS_MARKED_FOR_OFFLINE_AVAILABILITY
        PS_FULL_PRIMARY_STREAM_AVAILABLE = PLACEHOLDER_STATES.PS_FULL_PRIMARY_STREAM_AVAILABLE
        PS_CREATE_FILE_ACCESSIBLE = PLACEHOLDER_STATES.PS_CREATE_FILE_ACCESSIBLE
        PS_CLOUDFILE_PLACEHOLDER = PLACEHOLDER_STATES.PS_CLOUDFILE_PLACEHOLDER
        CONFLICT_RESOLUTION_CLSID_KEY = "ConflictResolutionCLSID"


        class MERGE_UPDATE_STATUS(ENUM):
            MUS_COMPLETE = 0
            #~#~#~ MUS_USERINPUTNEEDED    = ( MUS_COMPLETE + 1 )
            #~#~#~ MUS_FAILED    = ( MUS_USERINPUTNEEDED + 1 )


        MUS_COMPLETE = MERGE_UPDATE_STATUS.MUS_COMPLETE
        if not defined(__IFileSyncMergeHandler_INTERFACE_DEFINED__):
            __IFileSyncMergeHandler_INTERFACE_DEFINED__ = 1

            # interface IFileSyncMergeHandler

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IFileSyncMergeHandler._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Merge',
                        (['in'], LPCWSTR, 'localFilePath'),
                        ([], LPCWSTR, 'serverFilePath'),
                        (
                            ['retval', 'out'],
                            POINTER(MERGE_UPDATE_STATUS),
                           'updateStatus'
                        ),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ShowResolveConflictUIAsync',
                        (['in'], LPCWSTR, 'localFilePath'),
                        ([], HMONITOR, 'monitorToDisplayOn'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IFileSyncMergeHandler_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0013

        # [local]
        STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE = "Force Folder Shortcut Resolve"
        STR_AVOID_DRIVE_RESTRICTION_POLICY = "AVOID Drive Restriction Policy"
        STR_AVOID_DRIVE_RESTRICTION_POLICY = "AVOID Drive Restriction Policy"
        STR_SKIP_BINDING_CLSID = "Skip Binding CLSID"
        STR_PARSE_PREFER_FOLDER_BROWSING = "Parse Prefer Folder Browsing"
        STR_DONT_PARSE_RELATIVE = "Don't Parse Relative"
        STR_PARSE_TRANSLATE_ALIASES = "Parse Translate Aliases"
        STR_PARSE_SKIP_NET_CACHE = "Skip Net Resource Cache"
        STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS = (
    "Parse Shell Protocol To File Objects"
)

        if (_WIN32_IE >= 0x0700):
            STR_TRACK_CLSID = "Track the CLSID"
            STR_INTERNAL_NAVIGATE = "Internal Navigation"
            STR_PARSE_PROPERTYSTORE = "DelegateNamedProperties"
            STR_NO_VALIDATE_FILENAME_CHARS = "NoValidateFilenameChars"
            STR_BIND_DELEGATE_CREATE_OBJECT = "Delegate Object Creation"
            STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS = (
    "Allow binding to Internet shell folder handlers and negate STR_PARSE_PREFER_WEB_BROWSING"
)
            STR_PARSE_PREFER_WEB_BROWSING = "Do not bind to Internet shell folder handlers"
            STR_PARSE_SHOW_NET_DIAGNOSTICS_UI = "Show network diagnostics UI"
            STR_PARSE_DONT_REQUIRE_VALIDATED_URLS = "Do not require validated URLs"
            STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE = "Validate URL"
        # END IF   _WIN32_IE >= 0x0700

        if (NTDDI_VERSION >= NTDDI_WIN8):
            BIND_INTERRUPTABLE = 0xFFFFFFFF
        # END IF   NTDDI_WIN8

        if (NTDDI_VERSION >= NTDDI_WIN7):
            STR_BIND_FOLDERS_READ_ONLY = "Folders As Read Only"
            STR_BIND_FOLDER_ENUM_MODE = "Folder Enum Mode"


            class FOLDER_ENUM_MODE(ENUM):
                FEM_VIEWRESULT = 0
                FEM_NAVIGATION = 1


            FEM_VIEWRESULT = FOLDER_ENUM_MODE.FEM_VIEWRESULT
            FEM_NAVIGATION = FOLDER_ENUM_MODE.FEM_NAVIGATION
            if not defined(__IObjectWithFolderEnumMode_INTERFACE_DEFINED__):
                __IObjectWithFolderEnumMode_INTERFACE_DEFINED__ = 1

                # interface IObjectWithFolderEnumMode

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IObjectWithFolderEnumMode._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetMode',
                            (['in'], FOLDER_ENUM_MODE, 'feMode'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetMode',
                            (['out'], POINTER(FOLDER_ENUM_MODE), 'pfeMode'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IObjectWithFolderEnumMode_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0014

            # [local]
            STR_PARSE_WITH_EXPLICIT_PROGID = "ExplicitProgid"
            STR_PARSE_WITH_EXPLICIT_ASSOCAPP = "ExplicitAssociationApp"
            STR_PARSE_EXPLICIT_ASSOCIATION_SUCCESSFUL = "ExplicitAssociationSuccessful"
            STR_PARSE_AND_CREATE_ITEM = "ParseAndCreateItem"
            STR_PROPERTYBAG_PARAM = "SHBindCtxPropertyBag"
            STR_ENUM_ITEMS_FLAGS = "SHCONTF"

            if not defined(__IParseAndCreateItem_INTERFACE_DEFINED__):
                __IParseAndCreateItem_INTERFACE_DEFINED__ = 1

                # interface IParseAndCreateItem

                # [local][unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IParseAndCreateItem._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetItem',
                            (['in'], POINTER(IShellItem), 'psi'),
                        ),

                        # Returns IShellItem                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetItem',
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IParseAndCreateItem_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0015

            # [local]
            STR_ITEM_CACHE_CONTEXT = "ItemCacheContext"
        # END IF   NTDDI_VERSION >= NTDDI_WIN7

        if not defined(__IShellFolder_INTERFACE_DEFINED__):
            __IShellFolder_INTERFACE_DEFINED__ = 1

            # interface IShellFolder

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][unique][out][in]

                # [annotation][unique][out][in]

                # [annotation][unique][in]

                # [annotation][in]

                # [annotation][string][in]

                # [annotation][in]

                # [annotation][out]
            else: # C style interface
                IShellFolder._methods_ = [

                    # annotation is allowed on local interface and local
                    # methods only                
                    COMMETHOD(
                        [],
                        midl_pragma,
                        'warning',
                        (
                            [],
                            disable: * i,
                           '2495)  HRESULT ParseDisplayName('
                        ),
                        ([], unique], 'HWND hwnd'),
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        (['in'], LPWSTR, 'pszDisplayName'),
                        (
                            [annotation('_Reserved_'), 'unique', 'out', 'in'],
                            POINTER(ULONG),
                           'pchEaten'
                        ),
                        (['out'], POINTER(PIDLIST_RELATIVE), 'ppidl'),
                        (
                            ['out', 'unique', 'in'],
                            POINTER(ULONG),
                           'pdwAttributes'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        midl_pragma,
                        'warning',
                        ([], default: * i, '2495)  HRESULT EnumObjects('),
                        ([], unique], 'HWND hwnd'),
                        (['in'], SHCONTF, 'grfFlags'),
                        (
                            ['out'],
                            POINTER(POINTER(IEnumIDList)),
                           'ppenumIDList'
                        ),
                    ),

                    # returns an instance of a sub - folder which is specified
                    # by the IDList (pidl).
                    # IShellFolder or derived interfaces
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'BindToObject',
                        (['in'], PCUIDLIST_RELATIVE, 'pidl'),
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # produces the same result as BindToObject()
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'BindToStorage',
                        (['in'], PCUIDLIST_RELATIVE, 'pidl'),
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # compares two IDLists and returns the result. The shell
                    # explorer always passes 0 as lParam, which indicates
                    # 'sort by name'.
                    # It should return 0 (as CODE of the scode), if two id
                    # indicates the
                    # same object; negative value if pidl1 should be placed
                    # before pidl2;
                    # positive value if pidl2 should be placed before pidl1.
                    # use the macro ResultFromShort() to extract the result
                    # comparison
                    # it deals with the casting and type conversion issues for
                    # you
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CompareIDs',
                        (['in'], LPARAM, 'lParam'),
                        ([], PCUIDLIST_RELATIVE, 'pidl1'),
                        ([], PCUIDLIST_RELATIVE, 'pidl2'),
                    ),

                    # creates a view object of the folder itself. The view
                    # object is a difference instance from the shell folder
                    # object.
                    # 'hwndOwner' can be used as the owner window of its
                    # dialog box or
                    # menu during the lifetime of the view object.
                    # This member function should always create a new
                    # instance which has only one reference count. The
                    # explorer may create
                    # more than one instances of view object from one shell
                    # folder object
                    # and treat them as separate instances.
                    # returns IShellView derived interface
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CreateViewObject',
                        (['unique', 'in'], HWND, 'hwndOwner'),
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # returns the attributes of specified objects in that
                    # folder. 'cidl' and 'apidl' specifies objects. 'apidl'
                    # contains only
                    # simple IDLists. The explorer initializes *prgfInOut with
                    # a set of
                    # flags to be evaluated. The shell folder may optimize the
                    # operation
                    # by not returning unspecified flags.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetAttributesOf',
                        (['in'], UINT, 'cidl'),
                        (['unique', 'in'], PCUITEMID_CHILD_ARRAY, 'apidl'),
                        (['out', 'in'], POINTER(SFGAOF), ' rgfInOut'),
                    ),

                    # annotation is allowed on local interface and local
                    # methods only creates a UI object to be used for
                    # specified objects. The shell explorer passes either
                    # IID_IDataObject (for transfer operation) or
                    # IID_IContextMenu (for context menu operation) as riid
                    # and many other interfaces                
                    COMMETHOD(
                        [],
                        midl_pragma,
                        'warning',
                        (
                            [],
                            disable: * i,
                           '2495)      HRESULT GetUIObjectOf('
                        ),
                        ([], unique], 'HWND hwndOwner'),
                        (['in'], UINT, 'cidl'),
                        (['unique', 'in'], PCUITEMID_CHILD_ARRAY, 'apidl'),
                        ([], REFIID, 'riid'),
                        (
                            [annotation('_Reserved_'), 'unique', 'out', 'in'],
                            POINTER(UINT),
                           ' rgfReserved'
                        ),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # returns the display name of the specified object. If the
                    # ID contains the display name
                    # (in the locale CHARacter set), it returns the offset to
                    # the name. Otherwise, it returns a pointer to the display
                    # name string (UNICODE), which is allocated by the task
                    # allocator, or fills in a buffer. use the helper APIS
                    # StrRetToStr() or StrRetToBuf() to deal with the
                    # different forms of the STRRET structure                
                    COMMETHOD(
                        [],
                        midl_pragma,
                        'warning',
                        (
                            [],
                            default: * i,
                           '2495)         HRESULT GetDisplayNameOf('
                        ),
                        ([], unique], 'PCUITEMID_CHILD pidl'),
                        (['in'], SHGDNF, 'uFlags'),
                        (['out'], POINTER(STRRET), 'pName'),
                    ),

                    # sets the display name of the specified object.
                    # If it changes the ID as well, it returns the new ID
                    # which is
                    # alocated by the task allocator.
                    #                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'SetNameOf',
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            HWND,
                           'hwnd'
                        ),
                        ([annotation('_In_'), 'in'], PCUITEMID_CHILD, 'pidl'),
                        ([annotation('_In_'), , 'in'], LPCWSTR, 'pszName'),
                        ([], SHGDNF, 'uFlags'),
                        (
                            ['out', annotation('_Outptr_opt_')],
                            POINTER(PITEMID_CHILD),
                           'ppidlOut'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoteSetNameOf',
                        (['unique', 'in'], HWND, 'hwnd'),
                        (['in'], PCUITEMID_CHILD, 'pidl'),
                        (['in'], LPCWSTR, 'pszName'),
                        ([], SHGDNF, 'uFlags'),
                        (['out'], POINTER(PITEMID_CHILD), 'ppidlOut'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][unique][out][in]

                # [annotation][unique][out][in]

                # [annotation][unique][in]

                # [annotation][in]

                # [annotation][string][in]

                # [annotation][in]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IShellFolder_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0016

        # [local]
        class EXTRASEARCH(ctypes.Structure):
            pass
        EXTRASEARCH._fields_ = [
            ('guidSearch', GUID),
            ('wszFriendlyName', WCHAR * 80),
            ('wszUrl', WCHAR * 2084),
        ]


        LPEXTRASEARCH = POINTER(EXTRASEARCH)


        if not defined(__IEnumExtraSearch_INTERFACE_DEFINED__):
            __IEnumExtraSearch_INTERFACE_DEFINED__ = 1

            # interface IEnumExtraSearch

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IEnumExtraSearch._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'celt'),
                        (['out', 'in', 'out'], POINTER(EXTRASEARCH), 'rgelt'),
                        (['out'], POINTER(ULONG), 'pceltFetched'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'celt'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Reset',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumExtraSearch)),
                           'ppenum'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IEnumExtraSearch_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0017

        # [local]
        if not defined(__IShellFolder2_INTERFACE_DEFINED__):
            __IShellFolder2_INTERFACE_DEFINED__ = 1

            # interface IShellFolder2

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellFolder2._methods_ = [

                    # Returns the guid of the search that is to be invoked
                    # when user clicks on the search toolbar button                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDefaultSearchGUID',
                        (['out'], POINTER(GUID), 'pguid'),
                    ),

                    # gives an enumerator of the searches to be added to the
                    # search menu                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnumSearches',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumExtraSearch)),
                           'ppenum'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDefaultColumn',
                        (['in'], DWORD, 'dwRes'),
                        (['out'], POINTER(ULONG), 'pSort'),
                        ([], POINTER(ULONG), 'pDisplay'),
                    ),

                    # return SHCOLSTATE_ values
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDefaultColumnState',
                        (['in'], UINT, 'iColumn'),
                        (['out'], POINTER(SHCOLSTATEF), 'pcsFlags'),
                    ),

                    # PCUITEMID_CHILD should have been annotated as [in].
                    # Changing the annotation will break compatibility, but
                    # GetDetailsEx should never be called with a null pidl.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDetailsEx',
                        (['unique', 'in'], PCUITEMID_CHILD, 'pidl'),
                        (['in'], POINTER(SHCOLUMNID), 'pscid'),
                        (['out'], POINTER(VARIANT), 'pv'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDetailsOf',
                        (['unique', 'in'], PCUITEMID_CHILD, 'pidl'),
                        (['in'], UINT, 'iColumn'),
                        (['out'], POINTER(SHELLDETAILS), 'psd'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'MapColumnToSCID',
                        (['in'], UINT, 'iColumn'),
                        (['out'], POINTER(SHCOLUMNID), 'pscid'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][unique][out][in]

                # [annotation][unique][out][in]

                # [annotation][unique][in]

                # [annotation][in]

                # [annotation][string][in]

                # [annotation][in]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IShellFolder2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0018

        # [local]
        class FOLDERFLAGS(ENUM):
            FWF_NONE = 0
            FWF_AUTOARRANGE = 0x1
            FWF_ABBREVIATEDNAMES = 0x2
            FWF_SNAPTOGRID = 0x4
            FWF_OWNERDATA = 0x8
            FWF_BESTFITWINDOW = 0x10
            FWF_DESKTOP = 0x20
            FWF_SINGLESEL = 0x40
            FWF_NOSUBFOLDERS = 0x80
            FWF_TRANSPARENT = 0x100
            FWF_NOCLIENTEDGE = 0x200
            FWF_NOSCROLL = 0x400
            FWF_ALIGNLEFT = 0x800
            FWF_NOICONS = 0x1000
            FWF_SHOWSELALWAYS = 0x2000
            FWF_NOVISIBLE = 0x4000
            FWF_SINGLECLICKACTIVATE = 0x8000
            FWF_NOWEBVIEW = 0x10000
            FWF_HIDEFILENAMES = 0x20000
            FWF_CHECKSELECT = 0x40000
            FWF_NOENUMREFRESH = 0x80000
            FWF_NOGROUPING = 0x100000
            FWF_FULLROWSELECT = 0x200000
            FWF_NOFILTERS = 0x400000
            FWF_NOCOLUMNHEADER = 0x800000
            FWF_NOHEADERINALLVIEWS = 0x1000000
            FWF_EXTENDEDTILES = 0x2000000
            FWF_TRICHECKSELECT = 0x4000000
            FWF_AUTOCHECKSELECT = 0x8000000
            FWF_NOBROWSERVIEWSTATE = 0x10000000
            FWF_SUBSETGROUPS = 0x20000000
            FWF_USESEARCHFOLDER = 0x40000000
            FWF_ALLOWRTLREADING = 0x80000000


        FWF_NONE = FOLDERFLAGS.FWF_NONE
        FWF_AUTOARRANGE = FOLDERFLAGS.FWF_AUTOARRANGE
        FWF_ABBREVIATEDNAMES = FOLDERFLAGS.FWF_ABBREVIATEDNAMES
        FWF_SNAPTOGRID = FOLDERFLAGS.FWF_SNAPTOGRID
        FWF_OWNERDATA = FOLDERFLAGS.FWF_OWNERDATA
        FWF_BESTFITWINDOW = FOLDERFLAGS.FWF_BESTFITWINDOW
        FWF_DESKTOP = FOLDERFLAGS.FWF_DESKTOP
        FWF_SINGLESEL = FOLDERFLAGS.FWF_SINGLESEL
        FWF_NOSUBFOLDERS = FOLDERFLAGS.FWF_NOSUBFOLDERS
        FWF_TRANSPARENT = FOLDERFLAGS.FWF_TRANSPARENT
        FWF_NOCLIENTEDGE = FOLDERFLAGS.FWF_NOCLIENTEDGE
        FWF_NOSCROLL = FOLDERFLAGS.FWF_NOSCROLL
        FWF_ALIGNLEFT = FOLDERFLAGS.FWF_ALIGNLEFT
        FWF_NOICONS = FOLDERFLAGS.FWF_NOICONS
        FWF_SHOWSELALWAYS = FOLDERFLAGS.FWF_SHOWSELALWAYS
        FWF_NOVISIBLE = FOLDERFLAGS.FWF_NOVISIBLE
        FWF_SINGLECLICKACTIVATE = FOLDERFLAGS.FWF_SINGLECLICKACTIVATE
        FWF_NOWEBVIEW = FOLDERFLAGS.FWF_NOWEBVIEW
        FWF_HIDEFILENAMES = FOLDERFLAGS.FWF_HIDEFILENAMES
        FWF_CHECKSELECT = FOLDERFLAGS.FWF_CHECKSELECT
        FWF_NOENUMREFRESH = FOLDERFLAGS.FWF_NOENUMREFRESH
        FWF_NOGROUPING = FOLDERFLAGS.FWF_NOGROUPING
        FWF_FULLROWSELECT = FOLDERFLAGS.FWF_FULLROWSELECT
        FWF_NOFILTERS = FOLDERFLAGS.FWF_NOFILTERS
        FWF_NOCOLUMNHEADER = FOLDERFLAGS.FWF_NOCOLUMNHEADER
        FWF_NOHEADERINALLVIEWS = FOLDERFLAGS.FWF_NOHEADERINALLVIEWS
        FWF_EXTENDEDTILES = FOLDERFLAGS.FWF_EXTENDEDTILES
        FWF_TRICHECKSELECT = FOLDERFLAGS.FWF_TRICHECKSELECT
        FWF_AUTOCHECKSELECT = FOLDERFLAGS.FWF_AUTOCHECKSELECT
        FWF_NOBROWSERVIEWSTATE = FOLDERFLAGS.FWF_NOBROWSERVIEWSTATE
        FWF_SUBSETGROUPS = FOLDERFLAGS.FWF_SUBSETGROUPS
        FWF_USESEARCHFOLDER = FOLDERFLAGS.FWF_USESEARCHFOLDER
        FWF_ALLOWRTLREADING = FOLDERFLAGS.FWF_ALLOWRTLREADING
        class FOLDERVIEWMODE(ENUM):
            FVM_AUTO = - 1
            FVM_FIRST = 1
            FVM_ICON = 1
            FVM_SMALLICON = 2
            FVM_LIST = 3
            FVM_DETAILS = 4
            FVM_THUMBNAIL = 5
            FVM_TILE = 6
            FVM_THUMBSTRIP = 7
            FVM_CONTENT = 8
            FVM_LAST = 8


        FVM_AUTO = FOLDERVIEWMODE.FVM_AUTO
        FVM_FIRST = FOLDERVIEWMODE.FVM_FIRST
        FVM_ICON = FOLDERVIEWMODE.FVM_ICON
        FVM_SMALLICON = FOLDERVIEWMODE.FVM_SMALLICON
        FVM_LIST = FOLDERVIEWMODE.FVM_LIST
        FVM_DETAILS = FOLDERVIEWMODE.FVM_DETAILS
        FVM_THUMBNAIL = FOLDERVIEWMODE.FVM_THUMBNAIL
        FVM_TILE = FOLDERVIEWMODE.FVM_TILE
        FVM_THUMBSTRIP = FOLDERVIEWMODE.FVM_THUMBSTRIP
        FVM_CONTENT = FOLDERVIEWMODE.FVM_CONTENT
        FVM_LAST = FOLDERVIEWMODE.FVM_LAST
        if (NTDDI_VERSION >= NTDDI_VISTA):
            class FOLDERLOGICALVIEWMODE(ENUM):
                FLVM_UNSPECIFIED = - 1
                FLVM_FIRST = 1
                FLVM_DETAILS = 1
                FLVM_TILES = 2
                FLVM_ICONS = 3
                FLVM_LIST = 4
                FLVM_CONTENT = 5
                FLVM_LAST = 5


            FLVM_UNSPECIFIED = FOLDERLOGICALVIEWMODE.FLVM_UNSPECIFIED
            FLVM_FIRST = FOLDERLOGICALVIEWMODE.FLVM_FIRST
            FLVM_DETAILS = FOLDERLOGICALVIEWMODE.FLVM_DETAILS
            FLVM_TILES = FOLDERLOGICALVIEWMODE.FLVM_TILES
            FLVM_ICONS = FOLDERLOGICALVIEWMODE.FLVM_ICONS
            FLVM_LIST = FOLDERLOGICALVIEWMODE.FLVM_LIST
            FLVM_CONTENT = FOLDERLOGICALVIEWMODE.FLVM_CONTENT
            FLVM_LAST = FOLDERLOGICALVIEWMODE.FLVM_LAST
        # END IF   NTDDI_VISTA
        class FOLDERSETTINGS(ctypes.Structure):
            pass
        FOLDERSETTINGS._fields_ = [
            ('ViewMode', UINT),
            ('fFlags', UINT),
        ]


        class _SVSIF(ENUM):
            SVSI_DESELECT = 0
            SVSI_SELECT = 0x1
            SVSI_EDIT = 0x3
            SVSI_DESELECTOTHERS = 0x4
            SVSI_ENSUREVISIBLE = 0x8
            SVSI_FOCUSED = 0x10
            SVSI_TRANSLATEPT = 0x20
            SVSI_SELECTIONMARK = 0x40
            SVSI_POSITIONITEM = 0x80
            SVSI_CHECK = 0x100
            SVSI_CHECK2 = 0x200
            SVSI_KEYBOARDSELECT = 0x401
            SVSI_NOTAKEFOCUS = 0x40000000


        SVSI_DESELECT = _SVSIF.SVSI_DESELECT
        SVSI_SELECT = _SVSIF.SVSI_SELECT
        SVSI_EDIT = _SVSIF.SVSI_EDIT
        SVSI_DESELECTOTHERS = _SVSIF.SVSI_DESELECTOTHERS
        SVSI_ENSUREVISIBLE = _SVSIF.SVSI_ENSUREVISIBLE
        SVSI_FOCUSED = _SVSIF.SVSI_FOCUSED
        SVSI_TRANSLATEPT = _SVSIF.SVSI_TRANSLATEPT
        SVSI_SELECTIONMARK = _SVSIF.SVSI_SELECTIONMARK
        SVSI_POSITIONITEM = _SVSIF.SVSI_POSITIONITEM
        SVSI_CHECK = _SVSIF.SVSI_CHECK
        SVSI_CHECK2 = _SVSIF.SVSI_CHECK2
        SVSI_KEYBOARDSELECT = _SVSIF.SVSI_KEYBOARDSELECT
        SVSI_NOTAKEFOCUS = _SVSIF.SVSI_NOTAKEFOCUS
        SVSI_NOSTATECHANGE = (UINT)0x80000000


        class _SVGIO(ENUM):
            SVGIO_BACKGROUND = 0
            SVGIO_SELECTION = 0x1
            SVGIO_ALLVIEW = 0x2
            SVGIO_CHECKED = 0x3
            SVGIO_TYPE_MASK = 0xF
            SVGIO_FLAG_VIEWORDER = 0x80000000


        SVGIO_BACKGROUND = _SVGIO.SVGIO_BACKGROUND
        SVGIO_SELECTION = _SVGIO.SVGIO_SELECTION
        SVGIO_ALLVIEW = _SVGIO.SVGIO_ALLVIEW
        SVGIO_CHECKED = _SVGIO.SVGIO_CHECKED
        SVGIO_TYPE_MASK = _SVGIO.SVGIO_TYPE_MASK
        SVGIO_FLAG_VIEWORDER = _SVGIO.SVGIO_FLAG_VIEWORDER
        class SVUIA_STATUS(ENUM):
            SVUIA_DEACTIVATE = 0
            SVUIA_ACTIVATE_NOFOCUS = 1
            SVUIA_ACTIVATE_FOCUS = 2
            SVUIA_INPLACEACTIVATE = 3


        SVUIA_DEACTIVATE = SVUIA_STATUS.SVUIA_DEACTIVATE
        SVUIA_ACTIVATE_NOFOCUS = SVUIA_STATUS.SVUIA_ACTIVATE_NOFOCUS
        SVUIA_ACTIVATE_FOCUS = SVUIA_STATUS.SVUIA_ACTIVATE_FOCUS
        SVUIA_INPLACEACTIVATE = SVUIA_STATUS.SVUIA_INPLACEACTIVATE
        if defined(_FIX_ENABLEMODELESS_CONFLICT):
            EnableModeless = EnableModelessSV
        # END IF

        if defined(_NEVER_):
            pass
    else: # not _NEVER_
            pass
        # END IF  _NEVER_
        if not defined(__IShellView_INTERFACE_DEFINED__):
            __IShellView_INTERFACE_DEFINED__ = 1

            # interface IShellView

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            else: # C style interface
                IShellView._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TranslateAccelerator',
                        (['in'], POINTER(MSG), 'pmsg'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnableModeless',
                        (['in'], BOOL, 'fEnable'),
                    ),

                    # SVUIA_STATUS                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'UIActivate',
                        (['in'], UINT, 'uState'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Refresh',
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CreateViewWindow',
                        (
                            ['unique', 'in'],
                            POINTER(IShellView),
                           'psvPrevious'
                        ),
                        (['in'], LPCFOLDERSETTINGS, 'pfs'),
                        ([], POINTER(IShellBrowser), 'psb'),
                        ([], POINTER(RECT), 'prcView'),
                        (['out'], POINTER(HWND), 'phWnd'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'DestroyViewWindow',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCurrentInfo',
                        (['out'], LPFOLDERSETTINGS, 'pfs'),
                    ),

                    #                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'AddPropertySheetPages',
                        ([annotation('_In_'), 'in'], DWORD, 'dwReserved'),
                        ([], LPFNSVADDPROPSHEETPAGE, 'pfn'),
                        ([], LPARAM, 'lparam'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SaveViewState',
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SelectItem',
                        (['unique', 'in'], PCUITEMID_CHILD, 'pidlItem'),
                        (['in'], SVSIF, 'uFlags'),
                    ),

                    # SVGIO                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetItemObject',
                        (['in'], UINT, 'uItem'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IShellView_INTERFACE_DEFINED__
        if not defined(__IShellView2_INTERFACE_DEFINED__):
            __IShellView2_INTERFACE_DEFINED__ = 1

            # interface IShellView2

            # [unique][object][uuid]
            SV2GV_CURRENTVIEW = (UINT) - 1
            SV2GV_DEFAULTVIEW = (UINT) - 2
            class _SV2CVW2_PARAMS(ctypes.Structure):
                pass
            _SV2CVW2_PARAMS._fields_ = [
                ('cbSize', DWORD),
                ('psvPrev', POINTER(IShellView)),
                ('pfs', LPCFOLDERSETTINGS),
                ('psbOwner', POINTER(IShellBrowser)),
                ('prcView', POINTER(RECT)),
                ('pvid', POINTER(SHELLVIEWID)),
                ('hwndView', HWND),
            ]


            SV2CVW2_PARAMS = _SV2CVW2_PARAMS


            LPSV2CVW2_PARAMS = POINTER(_SV2CVW2_PARAMS)



            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellView2._methods_ = [

                    # NOTE if the cbSize param is ever
                    # updated,") then there will have to be custom [wire_marshal]") implementation to support it")
                    # 
                    # Return to byte packing
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CreateViewWindow2',
                        (['in'], LPSV2CVW2_PARAMS, 'lpParams'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'HandleRename',
                        (['unique', 'in'], PCUITEMID_CHILD, 'pidlNew'),
                    ),

                    # SVSIF                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SelectAndPositionItem',
                        (['unique', 'in'], PCUITEMID_CHILD, 'pidlItem'),
                        (['in'], UINT, 'uFlags'),
                        ([], POINTER(POINT), 'ppt'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IShellView2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0020

        # [local]
        if defined(_FIX_ENABLEMODELESS_CONFLICT):
            pass
        # END IF
        if not defined(__IFolderView_INTERFACE_DEFINED__):
            __IFolderView_INTERFACE_DEFINED__ = 1

            # interface IFolderView

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IFolderView._methods_ = [
                    # FOLDERVIEWMODE
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCurrentViewMode',
                        (['out'], POINTER(UINT), 'pViewMode'),
                    ),

                    # FOLDERVIEWMODE                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetCurrentViewMode',
                        (['in'], UINT, 'ViewMode'),
                    ),

                    # the folder for the view, returns IShellFolder and
                    # related interfaces
                    # also supports IShellItemArray that returns an array with
                    # a single item for the folder
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFolder',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Item',
                        (['in'], INT, 'iItemIndex'),
                        (['out'], POINTER(PITEMID_CHILD), 'ppidl'),
                    ),

                    # get the count of items for selection, total, etc
                    # SVGIO                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ItemCount',
                        (['in'], UINT, 'uFlags'),
                        (['out'], POINTER(INT), 'pcItems'),
                    ),

                    # get the items in the view in the form of
                    # IShellItemArray, IDataObject, etc
                    # SVGIO                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Items',
                        (['in'], UINT, 'uFlags'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetSelectionMarkedItem',
                        (['out'], POINTER(INT), 'piItem'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFocusedItem',
                        (['out'], POINTER(INT), 'piItem'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetItemPosition',
                        (['in'], PCUITEMID_CHILD, 'pidl'),
                        (['out'], POINTER(POINT), 'ppt'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetSpacing',
                        (['out', 'unique', 'in'], POINTER(POINT), 'ppt'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDefaultSpacing',
                        (['out'], POINTER(POINT), 'ppt'),
                    ),

                    # returns S_OK if AutoArrange is on, S_FALSE if off                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetAutoArrange',
                    ),

                    # like IShellView::SelectItem() by index, SVSI_ flags
                    # SVSIF                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SelectItem',
                        (['in'], INT, 'iItem'),
                        ([], DWORD, 'dwFlags'),
                    ),

                    # SVSIF                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SelectAndPositionItems',
                        (['in'], UINT, 'cidl'),
                        (['in'], PCUITEMID_CHILD_ARRAY, 'apidl'),
                        (
                            ['unique', 'disable_consistency_check', 'in'],
                            POINTER(POINT),
                           'apt'
                        ),
                        ([], DWORD, 'dwFlags'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IFolderView_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0021

        # [local]
        SID_SFolderView = IID_IFolderView

        if (NTDDI_VERSION >= NTDDI_VISTA) or (_WIN32_IE >= _WIN32_IE_IE70):
            if not defined(NO_SHOBJIDL_SORTDIRECTION):

                # [v1_enum]
                class tagSORTDIRECTION(ENUM):
                    SORT_DESCENDING = - 1
                    SORT_ASCENDING = 1


                SORT_DESCENDING = tagSORTDIRECTION.SORT_DESCENDING
                SORT_ASCENDING = tagSORTDIRECTION.SORT_ASCENDING
            # END IF   NO_SHOBJIDL_SORTDIRECTION
            class SORTCOLUMN(ctypes.Structure):
                pass
            SORTCOLUMN._fields_ = [
                ('propkey', PROPERTYKEY),
                ('direction', SORTDIRECTION),
            ]


            class FVTEXTTYPE(ENUM):
                FVST_EMPTYTEXT = 0


            FVST_EMPTYTEXT = FVTEXTTYPE.FVST_EMPTYTEXT
            if defined(__cplusplus):
                DEPRECATED_HRESULT = HRESULT DECLSPEC_DEPRECATED
            # END IF

            if not defined(__IFolderView2_INTERFACE_DEFINED__):
                __IFolderView2_INTERFACE_DEFINED__ = 1

                # interface IFolderView2

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][out]

                    # [annotation][out]
                else: # C style interface
                    IFolderView2._methods_ = [

                        # Sets the group by property and starts a grouping
                        # operation
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetGroupBy',
                            (['in'], REFPROPERTYKEY, 'key'),
                            ([], BOOL, 'fAscending'),
                        ),

                        #                    
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'GetGroupBy',
                            (
                                ['out', annotation('_Out_')],
                                POINTER(PROPERTYKEY),
                               'pkey'
                            ),
                            (
                                [annotation('_Out_opt_'), 'out'],
                                POINTER(BOOL),
                               'pfAscending'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteGetGroupBy',
                            (['out'], POINTER(PROPERTYKEY), 'pkey'),
                            ([], POINTER(BOOL), 'pfAscending'),
                        ),

                        # Setting and Getting per item view properties is not
                        # possible for Libraries or Search results views.
                        # Consider using existing item properties instead.
                        #                    
                        COMMETHOD(
                            [],
                            DEPRECATED_HRESULT,
                            'SetViewProperty',
                            (['in'], PCUITEMID_CHILD, 'pidl'),
                            ([], REFPROPERTYKEY, 'propkey'),
                            ([], REFPROPVARIANT, 'propvar'),
                        ),

                        # Setting and Getting per item view properties is not
                        # possible for Libraries or Search results views.
                        # Consider using existing item properties instead.
                        #                    
                        COMMETHOD(
                            [],
                            DEPRECATED_HRESULT,
                            'GetViewProperty',
                            (['in'], PCUITEMID_CHILD, 'pidl'),
                            ([], REFPROPERTYKEY, 'propkey'),
                            (['out'], POINTER(PROPVARIANT), 'ppropvar'),
                        ),

                        # Setting per item Tile view properties is not
                        # possible for Libraries or Search results views.
                        # Consider setting property lists for your item types
                        # instead (see PKEY_PropList_TileInfo)
                        #                    
                        COMMETHOD(
                            [],
                            DEPRECATED_HRESULT,
                            'SetTileViewProperties',
                            (['in'], PCUITEMID_CHILD, 'pidl'),
                            (['in'], LPCWSTR, 'pszPropList'),
                        ),

                        # Setting per item Extended Tile view properties is
                        # not possible for Libraries or Search results views.
                        # Consider setting property lists for your item types
                        # instead (see PKEY_PropList_ExtendedTileInfo)
                        #                    
                        COMMETHOD(
                            [],
                            DEPRECATED_HRESULT,
                            'SetExtendedTileViewProperties',
                            (['in'], PCUITEMID_CHILD, 'pidl'),
                            (['in'], LPCWSTR, 'pszPropList'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetText',
                            (['in'], FVTEXTTYPE, 'iType'),
                            ([], LPCWSTR, 'pwszText'),
                        ),

                        # FOLDERFLAGS FOLDERFLAGS                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetCurrentFolderFlags',
                            (['in'], DWORD, 'dwMask'),
                            ([], DWORD, 'dwFlags'),
                        ),

                        # FOLDERFLAGS                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetCurrentFolderFlags',
                            (['out'], POINTER(DWORD), 'pdwFlags'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSortColumnCount',
                            (['out'], POINTER(INT), 'pcColumns'),
                        ),

                        # Sets the sort by property and starts a sort operation
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSortColumns',
                            (['in'], POINTER(SORTCOLUMN), 'rgSortColumns'),
                            (['in'], INT, 'cColumns'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSortColumns',
                            (['out'], POINTER(SORTCOLUMN), 'rgSortColumns'),
                            (['in'], INT, 'cColumns'),
                        ),

                        # return IShellItem for an item based on its index
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetItem',
                            (['in'], INT, 'iItem'),
                            ([], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetVisibleItem',
                            (['in'], INT, 'iStart'),
                            ([], BOOL, 'fPrevious'),
                            (['out'], POINTER(INT), 'piItem'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSelectedItem',
                            (['in'], INT, 'iStart'),
                            (['out'], POINTER(INT), 'piItem'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSelection',
                            (['in'], BOOL, 'fNoneImpliesFolder'),
                            (
                                ['out'],
                                POINTER(POINTER(IShellItemArray)),
                               'ppsia'
                            ),
                        ),

                        # Gets the selection state including check state. Same
                        # as the flags for IFolderView::SelectAndPositionItems
                        # SVSIF                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSelectionState',
                            (['in'], PCUITEMID_CHILD, 'pidl'),
                            (['out'], POINTER(DWORD), 'pdwFlags'),
                        ),

                        # If pszVerb is NULL, then the default verb is invoked.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'InvokeVerbOnSelection',
                            (['unique', , 'in'], LPCSTR, 'pszVerb'),
                        ),

                        # Sets default icon size if iImageSize == - 1
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetViewModeAndIconSize',
                            (['in'], FOLDERVIEWMODE, 'uViewMode'),
                            ([], INT, 'iImageSize'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetViewModeAndIconSize',
                            (['out'], POINTER(FOLDERVIEWMODE), 'puViewMode'),
                            ([], POINTER(INT), 'piImageSize'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetGroupSubsetCount',
                            (['in'], UINT, 'cVisibleRows'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetGroupSubsetCount',
                            (['out'], POINTER(UINT), 'pcVisibleRows'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetRedraw',
                            (['in'], BOOL, 'fRedrawOn'),
                        ),

                        # S_OK means this view sourced the current drag drop
                        # or cut/paste operation (used by drop target objects)                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'IsMoveInSameFolder',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DoRename',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][out]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __IFolderView2_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0022

            # [local]
            if (NTDDI_VERSION >= NTDDI_VISTA):
                if not defined(__IFolderViewSettings_INTERFACE_DEFINED__):
                    __IFolderViewSettings_INTERFACE_DEFINED__ = 1

                    # interface IFolderViewSettings

                    # [object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        IFolderViewSettings._methods_ = [

                            # GetColumnPropertyList - returns
                            # IPropertyDescriptionList. Ordered list of
                            # columns that must correspond to column enumerated
                            # via ISF::GetDetailsOf. Any column from
                            # ISF::GetDetailsOf not included in this list will
                            # be marked SHCOLSTATE_SECONDARYUI
                            # (or maintain SHCOLSTATE_HIDDEN)
                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetColumnPropertyList',
                                (['in'], REFIID, 'riid'),
                                (['out'], POINTER(POINTER(VOID)), 'ppv'),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetGroupByProperty',
                                (['out'], POINTER(PROPERTYKEY), 'pkey'),
                                ([], POINTER(BOOL), 'pfGroupAscending'),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetViewMode',
                                (
                                    ['out'],
                                    POINTER(FOLDERLOGICALVIEWMODE),
                                   'plvm'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetIconSize',
                                (['out'], POINTER(UINT), 'puIconSize'),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetFolderFlags',
                                (
                                    ['out'],
                                    POINTER(FOLDERFLAGS),
                                   'pfolderMask'
                                ),
                                ([], POINTER(FOLDERFLAGS), 'pfolderFlags'),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetSortColumns',
                                (
                                    ['out', 'in', 'out'],
                                    POINTER(SORTCOLUMN),
                                   'rgSortColumns'
                                ),
                                (['in'], UINT, 'cColumnsIn'),
                                (['out'], POINTER(UINT), 'pcColumnsOut'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetGroupSubsetCount',
                                (['out'], POINTER(UINT), 'pcVisibleRows'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __IFolderViewSettings_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0023

                # [local]
            # END IF   NTDDI_VISTA
        # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
        if (_WIN32_IE >= _WIN32_IE_IE70):
            if not defined(__IPreviewHandlerVisuals_INTERFACE_DEFINED__):
                __IPreviewHandlerVisuals_INTERFACE_DEFINED__ = 1

                # interface IPreviewHandlerVisuals

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IPreviewHandlerVisuals._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetBackgroundColor',
                            (['in'], COLORREF, 'color'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFont',
                            (['in'], POINTER(LOGFONTW), 'plf'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetTextColor',
                            (['in'], COLORREF, 'color'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IPreviewHandlerVisuals_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0024

            # [local]
        # END IF   _WIN32_IE_IE70
        CDBOSC_SETFOCUS = 0x00000000
        CDBOSC_KILLFOCUS = 0x00000001
        CDBOSC_SELCHANGE = 0x00000002
        CDBOSC_RENAME = 0x00000003
        CDBOSC_STATECHANGE = 0x00000004

        if not defined(__ICommDlgBrowser_INTERFACE_DEFINED__):
            __ICommDlgBrowser_INTERFACE_DEFINED__ = 1

            # interface ICommDlgBrowser

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                ICommDlgBrowser._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'OnDefaultCommand',
                        (['in'], POINTER(IShellView), 'ppshv'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'OnStateChange',
                        (['in'], POINTER(IShellView), 'ppshv'),
                        ([], ULONG, 'uChange'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'IncludeObject',
                        (['unique', 'in'], POINTER(IShellView), 'ppshv'),
                        (['in'], PCUITEMID_CHILD, 'pidl'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ICommDlgBrowser_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0025

        # [local]
        SID_SExplorerBrowserFrame = IID_ICommDlgBrowser

        if (NTDDI_VERSION >= NTDDI_WIN2K):
            CDB2N_CONTEXTMENU_DONE = 0x00000001
            CDB2N_CONTEXTMENU_START = 0x00000002
            CDB2GVF_SHOWALLFILES = 0x00000001

            if (NTDDI_VERSION >= NTDDI_VISTA):
                CDB2GVF_ISFILESAVE = 0x00000002
                CDB2GVF_ALLOWPREVIEWPANE = 0x00000004
                CDB2GVF_NOSELECTVERB = 0x00000008
                CDB2GVF_NOINCLUDEITEM = 0x00000010
                CDB2GVF_ISFOLDERPICKER = 0x00000020
                CDB2GVF_ADDSHIELD = 0x00000040
            # END IF   NTDDI_VISTA

            if not defined(__ICommDlgBrowser2_INTERFACE_DEFINED__):
                __ICommDlgBrowser2_INTERFACE_DEFINED__ = 1

                # interface ICommDlgBrowser2

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    ICommDlgBrowser2._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Notify',
                            (['in'], POINTER(IShellView), 'ppshv'),
                            ([], DWORD, 'dwNotifyType'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetDefaultMenuText',
                            (['in'], POINTER(IShellView), 'ppshv'),
                            (['out', ], LPWSTR, 'pszText'),
                            ([], INT, 'cchMax'),
                        ),

                        # returns CDB2GVF_XXX values to control the behavior
                        # of the view when in common dialog mode                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetViewFlags',
                            (['out'], POINTER(DWORD), 'pdwFlags'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __ICommDlgBrowser2_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0026

            # [local]
        # END IF   NTDDI_WIN2K
        if (_WIN32_IE >= _WIN32_IE_IE70):
            class CM_MASK(ENUM):
                CM_MASK_WIDTH = 0x1
                CM_MASK_DEFAULTWIDTH = 0x2
                CM_MASK_IDEALWIDTH = 0x4
                CM_MASK_NAME = 0x8
                CM_MASK_STATE = 0x10


            CM_MASK_WIDTH = CM_MASK.CM_MASK_WIDTH
            CM_MASK_DEFAULTWIDTH = CM_MASK.CM_MASK_DEFAULTWIDTH
            CM_MASK_IDEALWIDTH = CM_MASK.CM_MASK_IDEALWIDTH
            CM_MASK_NAME = CM_MASK.CM_MASK_NAME
            CM_MASK_STATE = CM_MASK.CM_MASK_STATE
            class CM_STATE(ENUM):
                CM_STATE_NONE = 0
                CM_STATE_VISIBLE = 0x1
                CM_STATE_FIXEDWIDTH = 0x2
                CM_STATE_NOSORTBYFOLDERNESS = 0x4
                CM_STATE_ALWAYSVISIBLE = 0x8


            CM_STATE_NONE = CM_STATE.CM_STATE_NONE
            CM_STATE_VISIBLE = CM_STATE.CM_STATE_VISIBLE
            CM_STATE_FIXEDWIDTH = CM_STATE.CM_STATE_FIXEDWIDTH
            CM_STATE_NOSORTBYFOLDERNESS = CM_STATE.CM_STATE_NOSORTBYFOLDERNESS
            CM_STATE_ALWAYSVISIBLE = CM_STATE.CM_STATE_ALWAYSVISIBLE
            class CM_ENUM_FLAGS(ENUM):
                CM_ENUM_ALL = 0x1
                CM_ENUM_VISIBLE = 0x2


            CM_ENUM_ALL = CM_ENUM_FLAGS.CM_ENUM_ALL
            CM_ENUM_VISIBLE = CM_ENUM_FLAGS.CM_ENUM_VISIBLE
            class CM_SET_WIDTH_VALUE(ENUM):
                CM_WIDTH_USEDEFAULT = - 1
                CM_WIDTH_AUTOSIZE = - 2


            CM_WIDTH_USEDEFAULT = CM_SET_WIDTH_VALUE.CM_WIDTH_USEDEFAULT
            CM_WIDTH_AUTOSIZE = CM_SET_WIDTH_VALUE.CM_WIDTH_AUTOSIZE
            class CM_COLUMNINFO(ctypes.Structure):
                pass
            CM_COLUMNINFO._fields_ = [
                ('cbSize', DWORD),
                ('dwMask', DWORD),
                ('dwState', DWORD),
                ('uWidth', UINT),
                ('uDefaultWidth', UINT),
                ('uIdealWidth', UINT),
                ('wszName', WCHAR * 80),
            ]


            if not defined(__IColumnManager_INTERFACE_DEFINED__):
                __IColumnManager_INTERFACE_DEFINED__ = 1

                # interface IColumnManager

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IColumnManager._methods_ = [

                        # NOTE: These methods only accept physical pixel
                        # values.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetColumnInfo',
                            (['in'], REFPROPERTYKEY, 'propkey'),
                            ([], POINTER(CM_COLUMNINFO), 'pcmci'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetColumnInfo',
                            (['in'], REFPROPERTYKEY, 'propkey'),
                            (['out', 'in'], POINTER(CM_COLUMNINFO), 'pcmci'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetColumnCount',
                            (['in'], CM_ENUM_FLAGS, 'dwFlags'),
                            (['out'], POINTER(UINT), 'puCount'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetColumns',
                            (['in'], CM_ENUM_FLAGS, 'dwFlags'),
                            (['out'], POINTER(PROPERTYKEY), 'rgkeyOrder'),
                            ([], UINT, 'cColumns'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetColumns',
                            (['in'], POINTER(PROPERTYKEY), 'rgkeyOrder'),
                            (['in'], UINT, 'cVisible'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IColumnManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0027

            # [local]
        # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
        if not defined(__IFolderFilterSite_INTERFACE_DEFINED__):
            __IFolderFilterSite_INTERFACE_DEFINED__ = 1

            # interface IFolderFilterSite

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IFolderFilterSite._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetFilter',
                        (['in'], POINTER(IUnknown), 'punk'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IFolderFilterSite_INTERFACE_DEFINED__
        if not defined(__IFolderFilter_INTERFACE_DEFINED__):
            __IFolderFilter_INTERFACE_DEFINED__ = 1

            # interface IFolderFilter

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IFolderFilter._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ShouldShow',
                        (['in'], POINTER(IShellFolder), 'psf'),
                        (['unique', 'in'], PCIDLIST_ABSOLUTE, 'pidlFolder'),
                        ([], PCUITEMID_CHILD, 'pidlItem'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetEnumFlags',
                        (['in'], POINTER(IShellFolder), 'psf'),
                        ([], PCIDLIST_ABSOLUTE, 'pidlFolder'),
                        (['out'], POINTER(HWND), 'phwnd'),
                        (['out', 'in'], POINTER(DWORD), 'pgrfFlags'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IFolderFilter_INTERFACE_DEFINED__
        if not defined(__IInputObjectSite_INTERFACE_DEFINED__):
            __IInputObjectSite_INTERFACE_DEFINED__ = 1

            # interface IInputObjectSite

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IInputObjectSite._methods_ = [
                    # Object (punkObj) is getting or losing the focus.
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'OnFocusChangeIS',
                        (['unique', 'in'], POINTER(IUnknown), 'punkObj'),
                        (['in'], BOOL, 'fSetFocus'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IInputObjectSite_INTERFACE_DEFINED__
        if not defined(__IInputObject_INTERFACE_DEFINED__):
            __IInputObject_INTERFACE_DEFINED__ = 1

            # interface IInputObject

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IInputObject._methods_ = [

                    # Activates or deactivates the object. lpMsg may be NULL.
                    # Returns
                    # S_OK if the activation succeeded.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'UIActivateIO',
                        (['in'], BOOL, 'fActivate'),
                        (['unique', 'in'], POINTER(MSG), 'pMsg'),
                    ),

                    # Returns S_OK if the object has the focus, S_FALSE if not.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'HasFocusIO',
                    ),

                    # Allow the object to process the message. Returns S_OK if
                    # the
                    # message was processed (eaten).                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TranslateAcceleratorIO',
                        (['in'], POINTER(MSG), 'pMsg'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IInputObject_INTERFACE_DEFINED__
        if not defined(__IInputObject2_INTERFACE_DEFINED__):
            __IInputObject2_INTERFACE_DEFINED__ = 1

            # interface IInputObject2

            # [local][unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]
            else: # C style interface
                IInputObject2._methods_ = [

                    # Called to handle global accelerators, so that input
                    # objects can
                    # respond to keyboard even when they are not UI active.
                    # Note that pMsg is not const, to allow implementors to
                    # forward to the
                    # Win32 TranslateAccelerator without having to cast away
                    # const - ness.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TranslateAcceleratorGlobal',
                        ([annotation('_In_'), 'in'], POINTER(MSG), 'pMsg'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IInputObject2_INTERFACE_DEFINED__
        if not defined(__IShellIcon_INTERFACE_DEFINED__):
            __IShellIcon_INTERFACE_DEFINED__ = 1

            # interface IShellIcon

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellIcon._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIconOf',
                        (['in'], PCUITEMID_CHILD, 'pidl'),
                        ([], UINT, 'flags'),
                        (['out'], POINTER(INT), 'pIconIndex'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IShellIcon_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0033

        # [local]
        SBSP_DEFBROWSER = 0x0000
        SBSP_SAMEBROWSER = 0x0001
        SBSP_NEWBROWSER = 0x0002
        SBSP_DEFMODE = 0x0000
        SBSP_OPENMODE = 0x0010
        SBSP_EXPLOREMODE = 0x0020
        SBSP_HELPMODE = 0x0040
        SBSP_NOTRANSFERHIST = 0x0080
        SBSP_ABSOLUTE = 0x0000
        SBSP_RELATIVE = 0x1000
        SBSP_PARENT = 0x2000
        SBSP_NAVIGATEBACK = 0x4000
        SBSP_NAVIGATEFORWARD = 0x8000
        SBSP_ALLOW_AUTONAVIGATE = 0x00010000

        if (NTDDI_VERSION >= NTDDI_VISTA):
            SBSP_KEEPSAMETEMPLATE = 0x00020000
            SBSP_KEEPWORDWHEELTEXT = 0x00040000
            SBSP_ACTIVATE_NOFOCUS = 0x00080000
            SBSP_CREATENOHISTORY = 0x00100000
            SBSP_PLAYNOSOUND = 0x00200000
        # END IF   (NTDDI_VERSION >= NTDDI_VISTA)

        if (_WIN32_IE >= _WIN32_IE_IE60SP2):
            SBSP_CALLERUNTRUSTED = 0x00800000
            SBSP_TRUSTFIRSTDOWNLOAD = 0x01000000
            SBSP_UNTRUSTEDFORDOWNLOAD = 0x02000000
        # END IF   _WIN32_IE_IE60SP2
        SBSP_NOAUTOSELECT = 0x04000000
        SBSP_WRITENOHISTORY = 0x08000000

        if (_WIN32_IE >= _WIN32_IE_IE60SP2):
            SBSP_TRUSTEDFORACTIVEX = 0x10000000
        # END IF   _WIN32_IE_IE60SP2

        if (_WIN32_IE >= _WIN32_IE_IE70):
            SBSP_FEEDNAVIGATION = 0x20000000
        # END IF   _WIN32_IE_IE70
        SBSP_REDIRECT = 0x40000000
        SBSP_INITIATEDBYHLINKFRAME = 0x80000000
        FCW_STATUS = 0x0001
        FCW_TOOLBAR = 0x0002
        FCW_TREE = 0x0003
        FCW_INTERNETBAR = 0x0006
        FCW_PROGRESS = 0x0008

        if (_WIN32_IE >= 0x0700):
            pass
        # END IF
        FCT_MERGE = 0x0001
        FCT_CONFIGABLE = 0x0002
        FCT_ADDTOEND = 0x0004

        if defined(_NEVER_):
            pass
    else: # not _NEVER_
            pass
        # END IF  _NEVER_
        if not defined(__IShellBrowser_INTERFACE_DEFINED__):
            __IShellBrowser_INTERFACE_DEFINED__ = 1

            # interface IShellBrowser

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            else: # C style interface
                IShellBrowser._methods_ = [
                    # same as IOleInPlaceFrame

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'InsertMenusSB',
                        (['in'], HMENU, 'hmenuShared'),
                        (['out', 'in'], LPOLEMENUGROUPWIDTHS, 'lpMenuWidths'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetMenuSB',
                        (['unique', 'in'], HMENU, 'hmenuShared'),
                        ([], HOLEMENU, 'holemenuRes'),
                        ([], HWND, 'hwndActiveObject'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveMenusSB',
                        (['in'], HMENU, 'hmenuShared'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetStatusTextSB',
                        (['unique', 'in'], LPCWSTR, 'pszStatusText'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnableModelessSB',
                        (['in'], BOOL, 'fEnable'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TranslateAcceleratorSB',
                        (['in'], POINTER(MSG), 'pmsg'),
                        ([], WORD, 'wID'),
                    ),

                    # IShellBrowser
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'BrowseObject',
                        (['unique', 'in'], PCUIDLIST_RELATIVE, 'pidl'),
                        (['in'], UINT, 'wFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetViewStateStream',
                        (['in'], DWORD, 'grfMode'),
                        (['out'], POINTER(POINTER(IStream)), 'ppStrm'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetControlWindow',
                        (['in'], UINT, 'id'),
                        (['out'], POINTER(HWND), ' phwnd'),
                    ),

                    #                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'SendControlMsg',
                        ([annotation('_In_'), 'in'], UINT, 'id'),
                        ([], UINT, 'uMsg'),
                        ([], WPARAM, 'wParam'),
                        ([], LPARAM, 'lParam'),
                        (
                            ['out', annotation('_Out_opt_')],
                            POINTER(LRESULT),
                           'pret'
                        ),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'QueryActiveShellView',
                        (['out'], POINTER(POINTER(IShellView)), 'ppshv'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'OnViewWindowActive',
                        (['in'], POINTER(IShellView), 'pshv'),
                    ),

                    #                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'SetToolbarItems',
                        (
                            [annotation('_In_reads_opt_(nButtons)), 'in'],
                            LPTBBUTTONSB,
                           'lpButtons'
                        ),
                        ([annotation('_In_'), 'in'], UINT, 'nButtons'),
                        ([], UINT, 'uFlags'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IShellBrowser_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0034

        # [local]
        if not defined(__IProfferService_INTERFACE_DEFINED__):
            __IProfferService_INTERFACE_DEFINED__ = 1

            # interface IProfferService

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IProfferService._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ProfferService',
                        (['in'], REFGUID, 'guidService'),
                        ([], POINTER(IServiceProvider), 'psp'),
                        (['out'], POINTER(DWORD), 'pdwCookie'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RevokeService',
                        (['in'], DWORD, 'dwCookie'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IProfferService_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0035

        # [local]
        SID_SProfferService = IID_IProfferService
        STR_DONT_RESOLVE_LINK = "Don't Resolve Link"
        STR_GET_ASYNC_HANDLER = "GetAsyncHandler"

        if not defined(__IShellItem_INTERFACE_DEFINED__):
            __IShellItem_INTERFACE_DEFINED__ = 1

            # interface IShellItem

            # [unique][object][uuid]


            class _SIGDN(ENUM):
                SIGDN_NORMALDISPLAY = 0
                #~#~#~ SIGDN_PARENTRELATIVEPARSING    = ( INT  )0x80018001
                #~#~#~ SIGDN_DESKTOPABSOLUTEPARSING    = ( INT  )0x80028000
                #~#~#~ SIGDN_PARENTRELATIVEEDITING    = ( INT  )0x80031001
                #~#~#~ SIGDN_DESKTOPABSOLUTEEDITING    = ( INT  )0x8004c000
                #~#~#~ SIGDN_FILESYSPATH    = ( INT  )0x80058000
                #~#~#~ SIGDN_URL    = ( INT  )0x80068000
                #~#~#~ SIGDN_PARENTRELATIVEFORADDRESSBAR    = ( INT  )0x8007c001
                #~#~#~ SIGDN_PARENTRELATIVE    = ( INT  )0x80080001
                #~#~#~ SIGDN_PARENTRELATIVEFORUI    = ( INT  )0x80094001


            SIGDN = _SIGDN
            SIGDN_NORMALDISPLAY = _SIGDN.SIGDN_NORMALDISPLAY

            # [v1_enum]
            class _SICHINTF(ENUM):
                SICHINT_DISPLAY = 0
                #~#~#~ SICHINT_ALLFIELDS    = ( INT  )0x80000000
                SICHINT_CANONICAL = 0x10000000
                SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL = 0x20000000


            SICHINT_DISPLAY = _SICHINTF.SICHINT_DISPLAY
            SICHINT_CANONICAL = _SICHINTF.SICHINT_CANONICAL
            SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL = _SICHINTF.SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL
            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][string][out]
            else: # C style interface
                IShellItem._methods_ = [

                    # lower word (& with 0xFFFF) SHGDN_NORMAL SHGDN_INFOLDER |
                    # SHGDN_FORPARSING SHGDN_FORPARSING SHGDN_INFOLDER |
                    # SHGDN_FOREDITING SHGDN_FORPARSING | SHGDN_FORADDRESSBAR
                    # SHGDN_FORPARSING | SHGDN_FORADDRESSBAR SHGDN_INFOLDER
                    # SHGDN_INFOLDER | SHGDN_FORADDRESSBAR
                    # SICHINT_DISPLAY  iOrder based on display in a folder view
                    # SICHINT_ALLFIELDS  exact instance compare
                    # SICHINT_CANONICAL  iOrder based on canonical name
                    # (better performance)
                    #
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'BindToHandler',
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        (['in'], REFGUID, 'bhid'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetParent',
                        (['out'], POINTER(POINTER(IShellItem)), 'ppsi'),
                    ),

                    # allow the annotation here, it is safe and useful                
                    COMMETHOD(
                        [],
                        midl_pragma,
                        'warning',
                        (
                            [],
                            disable: * in] SIGDN sigdnNam,
                           '2495 ) HRESULT GetDisplayName('
                        ),
                        (
                            [annotation('_Outptr_result_nullonfailure_'), 'out', ],
                            POINTER(LPWSTR),
                           'ppszName'
                        ),
                    ),

                    # annotation() only allowed on local methods/interfaces                
                    COMMETHOD(
                        [],
                        midl_pragma,
                        'warning',
                        (
                            [],
                            default: * in] SFGAOF sfgaoMas,
                           '2495 )  HRESULT GetAttributes('
                        ),
                        (['out'], POINTER(SFGAOF), 'psfgaoAttribs'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Compare',
                        (['in'], POINTER(IShellItem), 'psi'),
                        ([], SICHINTF, 'hint'),
                        (['out'], POINTER(INT), 'piOrder'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][string][out]
            # END IF  C style interface
        # END IF  __IShellItem_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0036

        # [local]
        if (_WIN32_IE >= _WIN32_IE_IE70):

            # CLSID_ShellItem create and init helper APIs. produce IShellItem
            # derived interfaces from these different expressions of an item
        # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
        if (NTDDI_VERSION >= NTDDI_VISTA):

            # get the IDList expression from an object, works with objects
            # that support IPersistIDlist or IPersistIDlist like
            # CLSID_ShellItem and most shell folders

            # similar to SHGetIDListFromObject but returns an IShellItem -
            # based object
            # (preferred for performance if the IDList is already bound to a folder)
            # 

            # these APIs return object that support IPropertyStore or related
            # interfaces
        # END IF   (NTDDI_VERSION >= NTDDI_VISTA)
        if (NTDDI_VERSION >= NTDDI_WIN7):
            class DATAOBJ_GET_ITEM_FLAGS(ENUM):
                DOGIF_DEFAULT = 0
                DOGIF_TRAVERSE_LINK = 0x1
                DOGIF_NO_HDROP = 0x2
                DOGIF_NO_URL = 0x4
                DOGIF_ONLY_IF_ONE = 0x8


            DOGIF_DEFAULT = DATAOBJ_GET_ITEM_FLAGS.DOGIF_DEFAULT
            DOGIF_TRAVERSE_LINK = DATAOBJ_GET_ITEM_FLAGS.DOGIF_TRAVERSE_LINK
            DOGIF_NO_HDROP = DATAOBJ_GET_ITEM_FLAGS.DOGIF_NO_HDROP
            DOGIF_NO_URL = DATAOBJ_GET_ITEM_FLAGS.DOGIF_NO_URL
            DOGIF_ONLY_IF_ONE = DATAOBJ_GET_ITEM_FLAGS.DOGIF_ONLY_IF_ONE
        # END IF   (NTDDI_VERSION >= NTDDI_WIN7)
        STR_GPS_HANDLERPROPERTIESONLY = "GPS_HANDLERPROPERTIESONLY"
        STR_GPS_FASTPROPERTIESONLY = "GPS_FASTPROPERTIESONLY"
        STR_GPS_OPENSLOWITEM = "GPS_OPENSLOWITEM"
        STR_GPS_DELAYCREATION = "GPS_DELAYCREATION"
        STR_GPS_BESTEFFORT = "GPS_BESTEFFORT"
        STR_GPS_NO_OPLOCK = "GPS_NO_OPLOCK"

        if not defined(__IShellItem2_INTERFACE_DEFINED__):
            __IShellItem2_INTERFACE_DEFINED__ = 1

            # interface IShellItem2

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellItem2._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPropertyStore',
                        (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # factory for low - rights creation of type ICreateObject                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPropertyStoreWithCreateObject',
                        (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
                        ([], POINTER(IUnknown), 'punkCreateObject'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPropertyStoreForKeys',
                        (['in'], POINTER(PROPERTYKEY), 'rgKeys'),
                        (['in'], UINT, 'cKeys'),
                        ([], GETPROPERTYSTOREFLAGS, 'flags'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPropertyDescriptionList',
                        (['in'], REFPROPERTYKEY, 'keyType'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # Ensures any cached information in this item is up to
                    # date, or returns
                    # __HRESULT_FROM_WIN32(ERROR_FILE_NOT_FOUND) if the item
                    # does not exist.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Update',
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetProperty',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(PROPVARIANT), 'ppropvar'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCLSID',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(CLSID), 'pclsid'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFileTime',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(FILETIME), 'pft'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetInt32',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(INT), 'pi'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetString',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out', ], POINTER(LPWSTR), 'ppsz'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetUInt32',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(ULONG), 'pui'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetUInt64',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(ULONGLONG), 'pull'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetBool',
                        (['in'], REFPROPERTYKEY, 'key'),
                        (['out'], POINTER(BOOL), 'pf'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][string][out]
            # END IF  C style interface
        # END IF  __IShellItem2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0037

        # [local]

        # [v1_enum]
        class _SIIGBF(ENUM):
            SIIGBF_RESIZETOFIT = 0
            SIIGBF_BIGGERSIZEOK = 0x1
            SIIGBF_MEMORYONLY = 0x2
            SIIGBF_ICONONLY = 0x4
            SIIGBF_THUMBNAILONLY = 0x8
            SIIGBF_INCACHEONLY = 0x10
            SIIGBF_CROPTOSQUARE = 0x20
            SIIGBF_WIDETHUMBNAILS = 0x40
            SIIGBF_ICONBACKGROUND = 0x80
            SIIGBF_SCALEUP = 0x100


        SIIGBF_RESIZETOFIT = _SIIGBF.SIIGBF_RESIZETOFIT
        SIIGBF_BIGGERSIZEOK = _SIIGBF.SIIGBF_BIGGERSIZEOK
        SIIGBF_MEMORYONLY = _SIIGBF.SIIGBF_MEMORYONLY
        SIIGBF_ICONONLY = _SIIGBF.SIIGBF_ICONONLY
        SIIGBF_THUMBNAILONLY = _SIIGBF.SIIGBF_THUMBNAILONLY
        SIIGBF_INCACHEONLY = _SIIGBF.SIIGBF_INCACHEONLY
        SIIGBF_CROPTOSQUARE = _SIIGBF.SIIGBF_CROPTOSQUARE
        SIIGBF_WIDETHUMBNAILS = _SIIGBF.SIIGBF_WIDETHUMBNAILS
        SIIGBF_ICONBACKGROUND = _SIIGBF.SIIGBF_ICONBACKGROUND
        SIIGBF_SCALEUP = _SIIGBF.SIIGBF_SCALEUP
        if not defined(__IShellItemImageFactory_INTERFACE_DEFINED__):
            __IShellItemImageFactory_INTERFACE_DEFINED__ = 1

            # interface IShellItemImageFactory

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellItemImageFactory._methods_ = [

                    # bitmap returned is a DIB; color format is RGB24, RGB32
                    # or PARGB32
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetImage',
                        (['in'], SIZE, 'size'),
                        ([], SIIGBF, 'flags'),
                        (['out'], POINTER(HBITMAP), 'phbm'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IShellItemImageFactory_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0038

        # [local]
        if (NTDDI_VERSION >= NTDDI_WINXP):
            if not defined(__IEnumShellItems_INTERFACE_DEFINED__):
                __IEnumShellItems_INTERFACE_DEFINED__ = 1

                # interface IEnumShellItems

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][length_is][size_is][out]

                    # [annotation][out]
                else: # C style interface
                    IEnumShellItems._methods_ = [
                        #
                    
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'Next',
                            ([annotation('_In_'), 'in'], ULONG, 'celt'),
                            (
                                ['out', annotation('_Out_writes_to_(celt, *pceltFetched)), 'in', 'out'],
                                POINTER(POINTER(IShellItem)),
                               'rgelt'
                            ),
                            (
                                ['out', annotation('_Out_opt_ _Deref_out_range_(0, celt))],
                                POINTER(ULONG),
                               'pceltFetched'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteNext',
                            (['in'], ULONG, 'celt'),
                            (
                                ['out', 'in', 'out'],
                                POINTER(POINTER(IShellItem)),
                               'rgelt'
                            ),
                            (['out'], POINTER(ULONG), 'pceltFetched'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Skip',
                            (['in'], ULONG, 'celt'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Reset',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Clone',
                            (
                                ['out'],
                                POINTER(POINTER(IEnumShellItems)),
                               'ppenum'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][length_is][size_is][out]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __IEnumShellItems_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0039

            # [local]
            class STGOP(ENUM):
                STGOP_MOVE = 1
                STGOP_COPY = 2
                STGOP_SYNC = 3
                STGOP_REMOVE = 5
                STGOP_RENAME = 6
                STGOP_APPLYPROPERTIES = 8
                STGOP_NEW = 10


            STGOP_MOVE = STGOP.STGOP_MOVE
            STGOP_COPY = STGOP.STGOP_COPY
            STGOP_SYNC = STGOP.STGOP_SYNC
            STGOP_REMOVE = STGOP.STGOP_REMOVE
            STGOP_RENAME = STGOP.STGOP_RENAME
            STGOP_APPLYPROPERTIES = STGOP.STGOP_APPLYPROPERTIES
            STGOP_NEW = STGOP.STGOP_NEW
        # END IF   NTDDI_WINXP

        # [v1_enum]
        class _TRANSFER_SOURCE_FLAGS(ENUM):
            TSF_NORMAL = 0
            TSF_FAIL_EXIST = 0
            TSF_RENAME_EXIST = 0x1
            TSF_OVERWRITE_EXIST = 0x2
            TSF_ALLOW_DECRYPTION = 0x4
            TSF_NO_SECURITY = 0x8
            TSF_COPY_CREATION_TIME = 0x10
            TSF_COPY_WRITE_TIME = 0x20
            TSF_USE_FULL_ACCESS = 0x40
            TSF_DELETE_RECYCLE_IF_POSSIBLE = 0x80
            TSF_COPY_HARD_LINK = 0x100
            TSF_COPY_LOCALIZED_NAME = 0x200
            TSF_MOVE_AS_COPY_DELETE = 0x400
            TSF_SUSPEND_SHELLEVENTS = 0x800


        TSF_NORMAL = _TRANSFER_SOURCE_FLAGS.TSF_NORMAL
        TSF_FAIL_EXIST = _TRANSFER_SOURCE_FLAGS.TSF_FAIL_EXIST
        TSF_RENAME_EXIST = _TRANSFER_SOURCE_FLAGS.TSF_RENAME_EXIST
        TSF_OVERWRITE_EXIST = _TRANSFER_SOURCE_FLAGS.TSF_OVERWRITE_EXIST
        TSF_ALLOW_DECRYPTION = _TRANSFER_SOURCE_FLAGS.TSF_ALLOW_DECRYPTION
        TSF_NO_SECURITY = _TRANSFER_SOURCE_FLAGS.TSF_NO_SECURITY
        TSF_COPY_CREATION_TIME = _TRANSFER_SOURCE_FLAGS.TSF_COPY_CREATION_TIME
        TSF_COPY_WRITE_TIME = _TRANSFER_SOURCE_FLAGS.TSF_COPY_WRITE_TIME
        TSF_USE_FULL_ACCESS = _TRANSFER_SOURCE_FLAGS.TSF_USE_FULL_ACCESS
        TSF_DELETE_RECYCLE_IF_POSSIBLE = _TRANSFER_SOURCE_FLAGS.TSF_DELETE_RECYCLE_IF_POSSIBLE
        TSF_COPY_HARD_LINK = _TRANSFER_SOURCE_FLAGS.TSF_COPY_HARD_LINK
        TSF_COPY_LOCALIZED_NAME = _TRANSFER_SOURCE_FLAGS.TSF_COPY_LOCALIZED_NAME
        TSF_MOVE_AS_COPY_DELETE = _TRANSFER_SOURCE_FLAGS.TSF_MOVE_AS_COPY_DELETE
        TSF_SUSPEND_SHELLEVENTS = _TRANSFER_SOURCE_FLAGS.TSF_SUSPEND_SHELLEVENTS
        if (_WIN32_IE >= _WIN32_IE_IE70):
            if not defined(__ITransferAdviseSink_INTERFACE_DEFINED__):
                __ITransferAdviseSink_INTERFACE_DEFINED__ = 1

                # interface ITransferAdviseSink

                # [object][uuid]

                # [v1_enum]


                class _TRANSFER_ADVISE_STATE(ENUM):
                    TS_NONE = 0
                    TS_PERFORMING = 0x1
                    TS_PREPARING = 0x2
                    TS_INDETERMINATE = 0x4


                TS_NONE = _TRANSFER_ADVISE_STATE.TS_NONE
                TS_PERFORMING = _TRANSFER_ADVISE_STATE.TS_PERFORMING
                TS_PREPARING = _TRANSFER_ADVISE_STATE.TS_PREPARING
                TS_INDETERMINATE = _TRANSFER_ADVISE_STATE.TS_INDETERMINATE
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    ITransferAdviseSink._methods_ = [

                        # Transfer is being performed Preparing to perform
                        # transfer - calculating space needed, etc. The length
                        # of the transfer is indeterminate
                        # UpdateProgress
                        # Updates the sink as to current progress of an
                        # operation.
                        # Implementers of this function should return an error
                        # code when the operation needs to terminate early
                        # (e.g. the user clicked on the cancel button).
                        # If all parameters are 0, UpdateProgress should not
                        # change any of its progress data but should can still
                        # return an error code
                        # to halt the operation.
                        # If all the total parameters are 0 but some of the
                        # current parameters are non - zero, UpdateProgress
                        # should update it's current progress but shouldn't
                        # change
                        # it's total progress.
                        # Callers should regularly query for a cancel request
                        # by calling this function with all parameters set to
                        # 0 even if no measurable progress occured.
                        # Parameters:
                        # ullSizeTotal, nFilesTotal, nFoldersTotal
                        # Total size in bytes, number of files and number of
                        # folders. This includes what has been processed and
                        # what will be processed.
                        # Setting all three to 0 indicates that the totals
                        # have not changed since the last call to
                        # UpdateProgress.
                        # ullSizeCurrent, nFilesCurrent, nFoldersCurrent
                        # Number of bytes, files and folders processed since
                        # the start of the operation.
                        # Setting all six parameters to zero indicates that
                        # progress has not changed since the last call to
                        # UpdateProgress.
                        # Return values:
                        # COPYENGINE_E_USER_CANCELLED
                        # The user has cancelled the operation and the caller
                        # should halt execution of the operation as soon as
                        # possible.
                        # Any other error:
                        # The caller should halt execution of the operation as
                        # soon as possible.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UpdateProgress',
                            (['in'], ULONGLONG, 'ullSizeCurrent'),
                            ([], ULONGLONG, 'ullSizeTotal'),
                            ([], INT, 'nFilesCurrent'),
                            ([], INT, 'nFilesTotal'),
                            ([], INT, 'nFoldersCurrent'),
                            ([], INT, 'nFoldersTotal'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UpdateTransferState',
                            (['in'], TRANSFER_ADVISE_STATE, 'ts'),
                        ),

                        # ConfirmOverwrite
                        # Parameters:
                        # psiSource
                        # Source IShellItem.
                        # psiDestParent
                        # Destination's parent folder's IShellItem.
                        # pszName
                        # Pointer to wide - string containing the name of the
                        # item. If NULL,
                        # the name is the same as the psiSource's.
                        # Return Values from Confirmations
                        # COPYENGINE_S_USER_IGNORED
                        # Continue operation
                        # COPYENGINE_E_USER_CANCELLED
                        # is a user - interaction cancel. The user clicked
                        # "Cancel" somewhere.
                        # Any other HRESULT should be passed up.
                        # Confirm that the operation is ok to actually
                        # overwrite an existing item
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ConfirmOverwrite',
                            (['in'], POINTER(IShellItem), 'psiSource'),
                            ([], POINTER(IShellItem), 'psiDestParent'),
                            (['in'], LPCWSTR, 'pszName'),
                        ),

                        # Confirm that the operation is ok to lose encryption
                        # (disclosure)                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ConfirmEncryptionLoss',
                            (['in'], POINTER(IShellItem), 'psiSource'),
                        ),

                        # Parameters:
                        # psi
                        # The IShellItem that is reporting the failure.
                        # pszItem
                        # If NULL, the "psi"'s display name will be used.
                        # If not NULL, this should be a pointer to a string
                        # that is the
                        # name of the item.
                        # hrError
                        # The error that is being reported.
                        # pszRename
                        # A buffer that the caller passes if it wants to be
                        # able to
                        # retry the operation with a new destination name. If
                        # this
                        # parameter is NULL, no option to rename will be
                        # available.
                        # cchRename
                        # Size of the buffer pointed to be pszRename.
                        # Return Values:
                        # COPYENGINE_S_USER_RETRY
                        # The handler should retry the file operation.
                        # COPYENGINE_S_USER_IGNORED
                        # The handler should skip creating the item and return
                        # this code
                        # back to the copy engine.
                        # COPYENGINE_E_USERCANCELLED
                        # The user clicked "Cancel" somewhere. The entire copy
                        # job is
                        # being aborted. The handler should return this code
                        # back to the
                        # copy engine.
                        # Any other HRESULT should be passed up. If failure
                        # not handled,
                        # the return value should be the same as hrError.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'FileFailure',
                            (['in'], POINTER(IShellItem), 'psi'),
                            (['unique', 'in'], LPCWSTR, 'pszItem'),
                            ([], HRESULT, 'hrError'),
                            (['out', 'unique', 'in'], LPWSTR, 'pszRename'),
                            ([], ULONG, 'cchRename'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SubStreamFailure',
                            (['in'], POINTER(IShellItem), 'psi'),
                            (['in'], LPCWSTR, 'pszStreamName'),
                            ([], HRESULT, 'hrError'),
                        ),

                        # (pkey == NULL) indicates loss of all properties                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PropertyFailure',
                            (['in'], POINTER(IShellItem), 'psi'),
                            (['unique', 'in'], POINTER(PROPERTYKEY), 'pkey'),
                            ([], HRESULT, 'hrError'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __ITransferAdviseSink_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0040

            # [local]
        # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
        if (NTDDI_VERSION >= NTDDI_VISTA):
            if not defined(__ITransferSource_INTERFACE_DEFINED__):
                __ITransferSource_INTERFACE_DEFINED__ = 1

                # interface ITransferSource

                # [local][unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][unique][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][out]

                    # [annotation][in]

                    # [annotation][in]
                else: # C style interface
                    ITransferSource._methods_ = [
                        # Description:

                        # Do an advise before calling anything so the handler
                        # can callback for
                        # any errors that might occur. If not set, the handler
                        # should consider
                        # it an indication that no feedback is available and
                        # to do the "default"
                        # operation.
                        # Parameters:
                        # psink
                        # ITransferAdviseSink interface to be used for status
                        # and
                        # failures.
                        # pdwCookie
                        # Pointer to a returned token that uniquely identifies
                        # this
                        # connection. The caller uses this token later to
                        # delete the
                        # connection by passing it to the Unadvise method. If
                        # the
                        # connection was not successfully established, this
                        # value is zero.
                        # Return Values:
                        # S_OK
                        # Interface successfully associated.
                        # E_UNEXPECTED
                        # The handler can only handle one sink interface.
                        # other HRESULTs indicate a failure.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Advise',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(ITransferAdviseSink),
                               'psink'
                            ),
                            (
                                ['out', annotation('_Out_')],
                                POINTER(DWORD),
                               'pdwCookie'
                            ),
                        ),

                        # Description:
                        # Terminates an advisory connection previously
                        # established through
                        # Advise method. The dwCookie parameter identifies the
                        # connection
                        # to terminate
                        # Parameters:
                        # dwCookie
                        # Connection token previously returned from Advise.
                        # Return Values:
                        # S_OK
                        # The connection was successfully terminated.
                        # CONNECT_E_NOCONNECTION
                        # The value in dwCookie does not represent a valid
                        # connection.
                        # other HRESULTs indicate a failure.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Unadvise',
                            ([annotation('_In_'), 'in'], DWORD, 'dwCookie'),
                        ),

                        # Description:
                        # Set properties that should be applied to an item
                        # Parameters:
                        # pproparray
                        # Contains a list of changes
                        # Return Values:
                        # S_OK
                        # Properties set successfully
                        # other HRESULTs indicate a failure.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetProperties',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IPropertyChangeArray),
                               'pproparray'
                            ),
                        ),

                        # Open the item for copying, returning an object that
                        # can be enumerated
                        # for resources (IShellItemResources).
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OpenItem',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psi'
                            ),
                            ([], TRANSFER_SOURCE_FLAGS, 'flags'),
                            ([], REFIID, 'riid'),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(VOID)),
                               'ppv'
                            ),
                        ),

                        # Move the item within the volume/namespace, returning
                        # the shell item
                        # in its new location.
                        # returns:
                        # FAILED() codes with special meaning for
                        # HRESULT_FROM_WIN32(ERROR_NOT_SAME_DEVICE) - > caller
                        # should convert move into a copy/delete
                        # E_NOINTERFACE - > caller should convert move into a
                        # copy/delete
                        # in the case of moving a folder
                        # HRESULT_FROM_WIN32(ERROR_FILE_EXISTS) or
                        # HRESULT_FROM_WIN32(ERROR_ALREADY_EXISTS)
                        # indicates
                        # to convert to a copy/delete the destination item
                        # must support ITransferDestination
                        # SUCCEEDED() code with special meaning for
                        # S_OK - move succeeded, *ppsiNew contains the new
                        # item that is the target of the move
                        # COPYENGINE_S_USER_IGNORED - > *ppsiNew is NULL, the
                        # destination item already exists and
                        # has not been overwritten. caller should complete the
                        # "move" by deleting the
                        # /   source item
                        # COPYENGINE_S_MERGE - > *ppsiNew is NULL, the
                        # destination folder already exists
                        # and the user has chosen to proceed merging the
                        # folder, the caller should complete
                        # the "move" of the folder by deleting the source
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'MoveItem',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psi'
                            ),
                            ([], POINTER(IShellItem), 'psiParentDst'),
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszNameDst'
                            ),
                            (['in'], TRANSFER_SOURCE_FLAGS, 'flags'),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(IShellItem)),
                               'ppsiNew'
                            ),
                        ),

                        # Recycle the item into the provided recycle location,
                        # returning the new
                        # recycled item in that location.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RecycleItem',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiSource'
                            ),
                            ([], POINTER(IShellItem), 'psiParentDest'),
                            ([], TRANSFER_SOURCE_FLAGS, 'flags'),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(IShellItem)),
                               'ppsiNewDest'
                            ),
                        ),

                        # Removed the item (without recycle support)
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoveItem',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiSource'
                            ),
                            ([], TRANSFER_SOURCE_FLAGS, 'flags'),
                        ),

                        # Change the name of an item, returing the shell item
                        # in its new location
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RenameItem',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiSource'
                            ),
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszNewName'
                            ),
                            ([], TRANSFER_SOURCE_FLAGS, 'flags'),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(IShellItem)),
                               'ppsiNewDest'
                            ),
                        ),

                        # not used or supported, return E_NOTIMPL
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'LinkItem',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiSource'
                            ),
                            ([], POINTER(IShellItem), 'psiParentDest'),
                            (
                                ['unique', , annotation('_In_opt_'), 'in'],
                                LPCWSTR,
                               'pszNewName'
                            ),
                            ([], TRANSFER_SOURCE_FLAGS, 'flags'),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(IShellItem)),
                               'ppsiNewDest'
                            ),
                        ),

                        # Apply a set of property changes to an item, return
                        # the modified shell item.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ApplyPropertiesToItem',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiSource'
                            ),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(IShellItem)),
                               'ppsiNew'
                            ),
                        ),

                        # Return the default name, if different from the items
                        # parsing name.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetDefaultDestinationName',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiSource'
                            ),
                            ([], POINTER(IShellItem), 'psiParentDest'),
                            (
                                [annotation('_Outptr_'), 'out', ],
                                POINTER(LPWSTR),
                               'ppszDestinationName'
                            ),
                        ),

                        # Description:
                        # These are called after a destination folder item has
                        # been created.
                        # EnterFolder() will be called before the children
                        # objects will be
                        # created.
                        # Expected the order of operations to be:
                        # DoCopyItem( psiParentSource, psiParentFolderDest, pszChildName )
                        # 
                        # {
                        # psiParentSource -
                        # >BindToHandler( ..., & ptsParentFolderSource)
                        # ptsParentSource - >Advise( psink, & dwCookie )
                        # ptsParentSource -
                        # >CopyItem( psiParentFolderDest, pszChildName, 0, & psiFolderDest )
                        # 
                        # if ( psiParentSource.HasChildren() )
                        # {
                        # ptsParentSource - >EnterFolder( psiFolderDest )
                        # for each child in psiParentSource
                        # {
                        # psiParentSource - >"GetChild"( & psiChildSource ); <
                        # - - a little more complicated
                        # DoCopyItem( psiChildSource , psiFolderDest )
                        # }
                        # ptsParentSource - >LeaveFolder( psiFolderDest )
                        # }
                        # ptsParentSource - >Unadvise( dwCookie )
                        # }
                        # Parameters:
                        # psiChildFolderDest
                        # IShellItem of the folder being entered.
                        # Return Values:
                        # S_OK
                        # Operation successful.
                        # other HRESULTs indicate failure.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnterFolder',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiChildFolderDest'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'LeaveFolder',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IShellItem),
                               'psiChildFolderDest'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][unique][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][out]

                    # [annotation][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __ITransferSource_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0041

            # [local]
        # END IF   NTDDI_VISTA
        class SHELL_ITEM_RESOURCE(ctypes.Structure):
            pass
        SHELL_ITEM_RESOURCE._fields_ = [
            ('guidType', GUID),
            ('szName', WCHAR * 260),
        ]


        if not defined(__IEnumResources_INTERFACE_DEFINED__):
            __IEnumResources_INTERFACE_DEFINED__ = 1

            # interface IEnumResources

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IEnumResources._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Next',
                        (['in'], ULONG, 'celt'),
                        (
                            ['out', 'in', 'out'],
                            POINTER(SHELL_ITEM_RESOURCE),
                           'psir'
                        ),
                        (['out'], POINTER(ULONG), 'pceltFetched'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'celt'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Reset',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumResources)),
                           'ppenumr'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IEnumResources_INTERFACE_DEFINED__
        if not defined(__IShellItemResources_INTERFACE_DEFINED__):
            __IShellItemResources_INTERFACE_DEFINED__ = 1

            # interface IShellItemResources

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellItemResources._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetAttributes',
                        (['out'], POINTER(DWORD), 'pdwAttributes'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetSize',
                        (['out'], POINTER(ULONGLONG), 'pullSize'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetTimes',
                        (['out'], POINTER(FILETIME), 'pftCreation'),
                        ([], POINTER(FILETIME), 'pftWrite'),
                        ([], POINTER(FILETIME), 'pftAccess'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetTimes',
                        (['unique', 'in'], POINTER(FILETIME), 'pftCreation'),
                        ([], POINTER(FILETIME), 'pftWrite'),
                        ([], POINTER(FILETIME), 'pftAccess'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetResourceDescription',
                        (['in'], POINTER(SHELL_ITEM_RESOURCE), 'pcsir'),
                        (['out'], POINTER(LPWSTR), 'ppszDescription'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnumResources',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumResources)),
                           'ppenumr'
                        ),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SupportsResource',
                        (['in'], POINTER(SHELL_ITEM_RESOURCE), 'pcsir'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'OpenResource',
                        (['in'], POINTER(SHELL_ITEM_RESOURCE), 'pcsir'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CreateResource',
                        (['in'], POINTER(SHELL_ITEM_RESOURCE), 'pcsir'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'MarkForDelete',
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IShellItemResources_INTERFACE_DEFINED__
        if not defined(__ITransferDestination_INTERFACE_DEFINED__):
            __ITransferDestination_INTERFACE_DEFINED__ = 1

            # interface ITransferDestination

            # [local][unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][out]

                # [annotation][string][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][iid_is][out]
            else: # C style interface
                ITransferDestination._methods_ = [
                    # *** 1: advise ***

                    # Do an advise before calling anything so the object can
                    # callback for
                    # any errors that might occur. If not set, the object
                    # should consider
                    # it an indication that no feedback is available and to do
                    # the "default"
                    # for the operation.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Advise',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(ITransferAdviseSink),
                           ' psink'
                        ),
                        (
                            ['out', annotation('_Out_')],
                            POINTER(DWORD),
                           ' pdwCookie'
                        ),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Unadvise',
                        (['in'], DWORD, 'dwCookie'),
                    ),

                    # returns:
                    # SUCCEEDED() code with special meaning for
                    # S_OK - move succeeded, *ppvItem and *ppvResources
                    # contains the new item and resources object
                    # that should be copied to
                    # COPYENGINE_S_USER_IGNORED - > *ppvItem and *ppvResources
                    # are NULL, the destination item already exists and
                    # has not been overwritten. if the caller is implemeting
                    # "move" as copy/delete it should complete
                    # the "move" by deleting the source item
                    # FILE_ATTRIBUTE_XXX values, most important being
                    # FILE_ATTRIBUTE_DIRECTORY indicating that a folder should
                    # be created the size of the item being copied or zero if
                    # unknow ppvItem should be an IShellItem or derived
                    # interface ppvResources should be an IShellItemResources
                    # or derived interface                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CreateItem',
                        ([annotation('_In_'), , 'in'], LPCWSTR, 'pszName'),
                        ([annotation('_In_'), 'in'], DWORD, 'dwAttributes'),
                        ([], ULONGLONG, 'ullSize'),
                        ([], TRANSFER_SOURCE_FLAGS, 'flags'),
                        ([], REFIID, 'riidItem'),
                        (
                            ['out', annotation('_Outptr_')],
                            POINTER(POINTER(VOID)),
                           'ppvItem'
                        ),
                        ([], REFIID, 'riidResources'),
                        (
                            ['out', annotation('_Outptr_')],
                            POINTER(POINTER(VOID)),
                           'ppvResources'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][out]

                # [annotation][string][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ITransferDestination_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0044

        # [local]
        if (_WIN32_IE >= _WIN32_IE_IE70):
            if not defined(__IFileOperationProgressSink_INTERFACE_DEFINED__):
                __IFileOperationProgressSink_INTERFACE_DEFINED__ = 1

                # interface IFileOperationProgressSink

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFileOperationProgressSink._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'StartOperations',
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'FinishOperations',
                            (['in'], HRESULT, 'hrResult'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PreRenameItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                            (['unique', 'in'], LPCWSTR, 'pszNewName'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PostRenameItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                            (['in'], LPCWSTR, 'pszNewName'),
                            ([], HRESULT, 'hrRename'),
                            ([], POINTER(IShellItem), 'psiNewlyCreated'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PreMoveItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                            ([], POINTER(IShellItem), 'psiDestinationFolder'),
                            (['unique', , 'in'], LPCWSTR, 'pszNewName'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PostMoveItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                            ([], POINTER(IShellItem), 'psiDestinationFolder'),
                            (['unique', , 'in'], LPCWSTR, 'pszNewName'),
                            ([], HRESULT, 'hrMove'),
                            ([], POINTER(IShellItem), 'psiNewlyCreated'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PreCopyItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                            ([], POINTER(IShellItem), 'psiDestinationFolder'),
                            (['unique', 'in'], LPCWSTR, 'pszNewName'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PostCopyItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                            ([], POINTER(IShellItem), 'psiDestinationFolder'),
                            (['unique', 'in'], LPCWSTR, 'pszNewName'),
                            ([], HRESULT, 'hrCopy'),
                            ([], POINTER(IShellItem), 'psiNewlyCreated'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PreDeleteItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PostDeleteItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiItem'),
                            ([], HRESULT, 'hrDelete'),
                            ([], POINTER(IShellItem), 'psiNewlyCreated'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PreNewItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiDestinationFolder'),
                            (['unique', 'in'], LPCWSTR, 'pszNewName'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PostNewItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], POINTER(IShellItem), 'psiDestinationFolder'),
                            (['unique', 'in'], LPCWSTR, 'pszNewName'),
                            ([], LPCWSTR, 'pszTemplateName'),
                            ([], DWORD, 'dwFileAttributes'),
                            ([], HRESULT, 'hrNew'),
                            ([], POINTER(IShellItem), 'psiNewItem'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UpdateProgress',
                            (['in'], UINT, 'iWorkTotal'),
                            ([], UINT, 'iWorkSoFar'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ResetTimer',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'PauseTimer',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ResumeTimer',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IFileOperationProgressSink_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0045

            # [local]
        # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
        if not defined(__IShellItemArray_INTERFACE_DEFINED__):
            __IShellItemArray_INTERFACE_DEFINED__ = 1

            # interface IShellItemArray

            # [unique][object][uuid]


            class SIATTRIBFLAGS(ENUM):
                SIATTRIBFLAGS_AND = 0x1
                SIATTRIBFLAGS_OR = 0x2
                SIATTRIBFLAGS_APPCOMPAT = 0x3
                SIATTRIBFLAGS_MASK = 0x3
                SIATTRIBFLAGS_ALLITEMS = 0x4000


            SIATTRIBFLAGS_AND = SIATTRIBFLAGS.SIATTRIBFLAGS_AND
            SIATTRIBFLAGS_OR = SIATTRIBFLAGS.SIATTRIBFLAGS_OR
            SIATTRIBFLAGS_APPCOMPAT = SIATTRIBFLAGS.SIATTRIBFLAGS_APPCOMPAT
            SIATTRIBFLAGS_MASK = SIATTRIBFLAGS.SIATTRIBFLAGS_MASK
            SIATTRIBFLAGS_ALLITEMS = SIATTRIBFLAGS.SIATTRIBFLAGS_ALLITEMS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellItemArray._methods_ = [

                    # if multiple items and the attirbutes together. if
                    # multiple items or the attributes together. Call
                    # GetAttributes directly on the ShellFolder for multiple
                    # attributes for the AND/OR/APPCOMPAT value normally only
                    # the first few items are used to compute the attributes,
                    # pass this to force all of them doing all will result in
                    # poor performance for large arrays so use this carefuly
                    # some bits are flags, others are not bhid values
                    # supported for the handler type are defined in shlguid.h
                    # BHID_DataObject - IDataObject, only works for flat data
                    # objects or item arrays produced directly using
                    # SHCreateShellItemArrayFromDataObject()
                    # BHID_AssociationArray - IQueryAssociations from the
                    # first item in the array BHID_SFUIObject - only works for
                    # flat (items in the same folder) item array                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPropertyStore',
                        (['in'], GETPROPERTYSTOREFLAGS, 'flags'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPropertyDescriptionList',
                        (['in'], REFPROPERTYKEY, 'keyType'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # get the attributes for the items using different methods
                    # defined by SIATTRIBFLAGS                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetAttributes',
                        (['in'], SIATTRIBFLAGS, 'AttribFlags'),
                        ([], SFGAOF, 'sfgaoMask'),
                        (['out'], POINTER(SFGAOF), 'psfgaoAttribs'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCount',
                        (['out'], POINTER(DWORD), 'pdwNumItems'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetItemAt',
                        (['in'], DWORD, 'dwIndex'),
                        (['out'], POINTER(POINTER(IShellItem)), 'ppsi'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnumItems',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumShellItems)),
                           'ppenumShellItems'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IShellItemArray_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0046

        # [local]
        if (_WIN32_IE >= _WIN32_IE_IE70):
            pass
        # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
        if not defined(__IInitializeWithItem_INTERFACE_DEFINED__):
            __IInitializeWithItem_INTERFACE_DEFINED__ = 1

            # interface IInitializeWithItem

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IInitializeWithItem._methods_ = [

                    # grfMode is STGM_ values indicating read/readwrite and
                    # sharing modes                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], POINTER(IShellItem), 'psi'),
                        ([], DWORD, 'grfMode'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IInitializeWithItem_INTERFACE_DEFINED__
        if not defined(__IObjectWithSelection_INTERFACE_DEFINED__):
            __IObjectWithSelection_INTERFACE_DEFINED__ = 1

            # interface IObjectWithSelection

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IObjectWithSelection._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetSelection',
                        (['in'], POINTER(IShellItemArray), 'psia'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetSelection',
                        (['in'], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IObjectWithSelection_INTERFACE_DEFINED__
        if not defined(__IObjectWithBackReferences_INTERFACE_DEFINED__):
            __IObjectWithBackReferences_INTERFACE_DEFINED__ = 1

            # interface IObjectWithBackReferences

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IObjectWithBackReferences._methods_ = [

                    # This method is used for all tasks associated with
                    # freeing/releasing back references held
                    # by an object, and may prepare an object for reuse                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveBackReferences',
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IObjectWithBackReferences_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0049

        # [local]

        # [v1_enum]
        class _PROPERTYUI_NAME_FLAGS(ENUM):
            PUIFNF_DEFAULT = 0
            PUIFNF_MNEMONIC = 0x1


        PUIFNF_DEFAULT = _PROPERTYUI_NAME_FLAGS.PUIFNF_DEFAULT
        PUIFNF_MNEMONIC = _PROPERTYUI_NAME_FLAGS.PUIFNF_MNEMONIC

        # [v1_enum]
        class _PROPERTYUI_FLAGS(ENUM):
            PUIF_DEFAULT = 0
            PUIF_RIGHTALIGN = 0x1
            PUIF_NOLABELININFOTIP = 0x2


        PUIF_DEFAULT = _PROPERTYUI_FLAGS.PUIF_DEFAULT
        PUIF_RIGHTALIGN = _PROPERTYUI_FLAGS.PUIF_RIGHTALIGN
        PUIF_NOLABELININFOTIP = _PROPERTYUI_FLAGS.PUIF_NOLABELININFOTIP

        # [v1_enum]
        class _PROPERTYUI_FORMAT_FLAGS(ENUM):
            PUIFFDF_DEFAULT = 0
            PUIFFDF_RIGHTTOLEFT = 0x1
            PUIFFDF_SHORTFORMAT = 0x2
            PUIFFDF_NOTIME = 0x4
            PUIFFDF_FRIENDLYDATE = 0x8


        PUIFFDF_DEFAULT = _PROPERTYUI_FORMAT_FLAGS.PUIFFDF_DEFAULT
        PUIFFDF_RIGHTTOLEFT = _PROPERTYUI_FORMAT_FLAGS.PUIFFDF_RIGHTTOLEFT
        PUIFFDF_SHORTFORMAT = _PROPERTYUI_FORMAT_FLAGS.PUIFFDF_SHORTFORMAT
        PUIFFDF_NOTIME = _PROPERTYUI_FORMAT_FLAGS.PUIFFDF_NOTIME
        PUIFFDF_FRIENDLYDATE = _PROPERTYUI_FORMAT_FLAGS.PUIFFDF_FRIENDLYDATE
        if not defined(__IPropertyUI_INTERFACE_DEFINED__):
            __IPropertyUI_INTERFACE_DEFINED__ = 1

            # interface IPropertyUI

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IPropertyUI._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ParsePropertyName',
                        (['in'], LPCWSTR, 'pszName'),
                        (['out'], POINTER(FMTID), 'pfmtid'),
                        ([], POINTER(PROPID), 'ppid'),
                        (['out', 'in'], POINTER(ULONG), 'pchEaten'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCannonicalName',
                        (['in'], REFFMTID, 'fmtid'),
                        ([], PROPID, 'pid'),
                        (['out', ], LPWSTR, 'pwszText'),
                        ([], DWORD, 'cchText'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDisplayName',
                        (['in'], REFFMTID, 'fmtid'),
                        ([], PROPID, 'pid'),
                        ([], PROPERTYUI_NAME_FLAGS, 'flags'),
                        (['out'], LPWSTR, 'pwszText'),
                        ([], DWORD, 'cchText'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPropertyDescription',
                        (['in'], REFFMTID, 'fmtid'),
                        ([], PROPID, 'pid'),
                        (['out'], LPWSTR, 'pwszText'),
                        ([], DWORD, 'cchText'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDefaultWidth',
                        (['in'], REFFMTID, 'fmtid'),
                        ([], PROPID, 'pid'),
                        (['out'], POINTER(ULONG), 'pcxChars'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFlags',
                        (['in'], REFFMTID, 'fmtid'),
                        ([], PROPID, 'pid'),
                        (['out'], POINTER(PROPERTYUI_FLAGS), 'pflags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'FormatForDisplay',
                        (['in'], REFFMTID, 'fmtid'),
                        ([], PROPID, 'pid'),
                        ([], POINTER(PROPVARIANT), 'ppropvar'),
                        ([], PROPERTYUI_FORMAT_FLAGS, 'puiff'),
                        (['out'], LPWSTR, 'pwszText'),
                        ([], DWORD, 'cchText'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetHelpInfo',
                        (['in'], REFFMTID, 'fmtid'),
                        ([], PROPID, 'pid'),
                        (['out'], LPWSTR, 'pwszHelpFile'),
                        ([], DWORD, 'cch'),
                        (['out'], POINTER(UINT), 'puHelpID'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IPropertyUI_INTERFACE_DEFINED__
        if not defined(__ICategoryProvider_INTERFACE_DEFINED__):
            __ICategoryProvider_INTERFACE_DEFINED__ = 1

            # interface ICategoryProvider

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                ICategoryProvider._methods_ = [

                    # Returns S_OK if the view should display this column in
                    # category selection UI, or S_FALSE to remove it.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CanCategorizeOnSCID',
                        (['in'], POINTER(SHCOLUMNID), 'pscid'),
                    ),

                    # Returns either a GUID to create in CreateCategory, or a
                    # SHCOLUNNID that is used by the default categorizer.
                    # Return S_FALSE if you do not support a default group.
                    # GUID_NULL returned in pguid indicates to the client to
                    # use pscid as the default category.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDefaultCategory',
                        (['out'], POINTER(GUID), 'pguid'),
                        ([], POINTER(SHCOLUMNID), 'pscid'),
                    ),

                    # Returns either a GUID that represents the categoizer to
                    # use for the specified SHCOLUMNID.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCategoryForSCID',
                        (['in'], POINTER(SHCOLUMNID), 'pscid'),
                        (['out'], POINTER(GUID), 'pguid'),
                    ),

                    # Returns an IEnumGUID that has a list of GUIDs that
                    # represent categories.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnumCategories',
                        (['out'], POINTER(POINTER(IEnumGUID)), 'penum'),
                    ),

                    # Returns the name of the given category.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCategoryName',
                        (['in'], POINTER(GUID), 'pguid'),
                        (['out'], LPWSTR, 'pszName'),
                        ([], UINT, 'cch'),
                    ),

                    # Creates the category.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CreateCategory',
                        (['in'], POINTER(GUID), 'pguid'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ICategoryProvider_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0051

        # [local]
        class CATEGORYINFO_FLAGS(ENUM):
            CATINFO_NORMAL = 0
            CATINFO_COLLAPSED = 0x1
            CATINFO_HIDDEN = 0x2
            CATINFO_EXPANDED = 0x4
            CATINFO_NOHEADER = 0x8
            CATINFO_NOTCOLLAPSIBLE = 0x10
            CATINFO_NOHEADERCOUNT = 0x20
            CATINFO_SUBSETTED = 0x40
            CATINFO_SEPARATE_IMAGES = 0x80
            CATINFO_SHOWEMPTY = 0x100


        CATINFO_NORMAL = CATEGORYINFO_FLAGS.CATINFO_NORMAL
        CATINFO_COLLAPSED = CATEGORYINFO_FLAGS.CATINFO_COLLAPSED
        CATINFO_HIDDEN = CATEGORYINFO_FLAGS.CATINFO_HIDDEN
        CATINFO_EXPANDED = CATEGORYINFO_FLAGS.CATINFO_EXPANDED
        CATINFO_NOHEADER = CATEGORYINFO_FLAGS.CATINFO_NOHEADER
        CATINFO_NOTCOLLAPSIBLE = CATEGORYINFO_FLAGS.CATINFO_NOTCOLLAPSIBLE
        CATINFO_NOHEADERCOUNT = CATEGORYINFO_FLAGS.CATINFO_NOHEADERCOUNT
        CATINFO_SUBSETTED = CATEGORYINFO_FLAGS.CATINFO_SUBSETTED
        CATINFO_SEPARATE_IMAGES = CATEGORYINFO_FLAGS.CATINFO_SEPARATE_IMAGES
        CATINFO_SHOWEMPTY = CATEGORYINFO_FLAGS.CATINFO_SHOWEMPTY
        class CATSORT_FLAGS(ENUM):
            CATSORT_DEFAULT = 0
            CATSORT_NAME = 0x1


        CATSORT_DEFAULT = CATSORT_FLAGS.CATSORT_DEFAULT
        CATSORT_NAME = CATSORT_FLAGS.CATSORT_NAME
        class CATEGORY_INFO(ctypes.Structure):
            pass
        CATEGORY_INFO._fields_ = [
            ('cif', CATEGORYINFO_FLAGS),
            ('wszName', WCHAR * 260),
        ]


        if not defined(__ICategorizer_INTERFACE_DEFINED__):
            __ICategorizer_INTERFACE_DEFINED__ = 1

            # interface ICategorizer

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                ICategorizer._methods_ = [

                    # Returns the description of this category that will be
                    # displayed in the UI
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDescription',
                        (['out'], LPWSTR, 'pszDesc'),
                        (['in'], UINT, 'cch'),
                    ),

                    # Returns a list of categories associated with a list of
                    # ID Lists. NOTE: - 1 is an invalid Category ID, and they
                    # cannot be persisted
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCategory',
                        (['in'], UINT, 'cidl'),
                        (['in'], PCUITEMID_CHILD_ARRAY, 'apidl'),
                        (['out'], POINTER(DWORD), 'rgCategoryIds'),
                    ),

                    # Returns information about the category, such as default
                    # display and the text to display in the UI
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCategoryInfo',
                        (['in'], DWORD, 'dwCategoryId'),
                        (['out'], POINTER(CATEGORY_INFO), 'pci'),
                    ),

                    # Returns HRESULTFromShort. - 1, 0, 1 indicate the
                    # comparison of the IDs. Used for sorting categories in
                    # the UI
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CompareCategory',
                        (['in'], CATSORT_FLAGS, 'csfFlags'),
                        ([], DWORD, 'dwCategoryId1'),
                        ([], DWORD, 'dwCategoryId2'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ICategorizer_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0052

        # [local]
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            class SHDRAGIMAGE(ctypes.Structure):
                pass
            SHDRAGIMAGE._fields_ = [
                ('sizeDragImage', SIZE),
                ('ptOffset', POINT),
                ('hbmpDragImage', HBITMAP),
                ('crColorKey', COLORREF),
            ]


            LPSHDRAGIMAGE = POINTER(SHDRAGIMAGE)


            DI_GETDRAGIMAGE = TEXT("ShellGetDragImage")

            if not defined(__IDropTargetHelper_INTERFACE_DEFINED__):
                __IDropTargetHelper_INTERFACE_DEFINED__ = 1

                # interface IDropTargetHelper

                # [object][unique][local][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                else: # C style interface
                    IDropTargetHelper._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DragEnter',
                            ([annotation('_In_'), 'in'], HWND, 'hwndTarget'),
                            ([], POINTER(IDataObject), 'pDataObject'),
                            ([], POINTER(POINT), 'ppt'),
                            ([], DWORD, 'dwEffect'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DragLeave',
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DragOver',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(POINT),
                               'ppt'
                            ),
                            ([], DWORD, 'dwEffect'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Drop',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IDataObject),
                               'pDataObject'
                            ),
                            ([], POINTER(POINT), 'ppt'),
                            ([], DWORD, 'dwEffect'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Show',
                            ([annotation('_In_'), 'in'], BOOL, 'fShow'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IDropTargetHelper_INTERFACE_DEFINED__
            if not defined(__IDragSourceHelper_INTERFACE_DEFINED__):
                __IDragSourceHelper_INTERFACE_DEFINED__ = 1

                # interface IDragSourceHelper

                # [object][unique][local][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]
                else: # C style interface
                    IDragSourceHelper._methods_ = [
                        # IDragSourceHelper

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'InitializeFromBitmap',
                            (
                                [annotation('_In_'), 'in'],
                                LPSHDRAGIMAGE,
                               'pshdi'
                            ),
                            ([], POINTER(IDataObject), 'pDataObject'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'InitializeFromWindow',
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                HWND,
                               'hwnd'
                            ),
                            ([], POINTER(POINT), 'ppt'),
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IDataObject),
                               'pDataObject'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IDragSourceHelper_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0054

            # [local]
        # END IF   NTDDI_WIN2K
        if defined(UNICODE):
            IShellLink = IShellLinkW
    else:
            # IShellLink = IShellLinkA
        # END IF


        class SLR_FLAGS(ENUM):
            SLR_NONE = 0
            SLR_NO_UI = 0x1
            SLR_ANY_MATCH = 0x2
            SLR_UPDATE = 0x4
            SLR_NOUPDATE = 0x8
            SLR_NOSEARCH = 0x10
            SLR_NOTRACK = 0x20
            SLR_NOLINKINFO = 0x40
            SLR_INVOKE_MSI = 0x80
            SLR_NO_UI_WITH_MSG_PUMP = 0x101
            SLR_OFFER_DELETE_WITHOUT_FILE = 0x200
            SLR_KNOWNFOLDER = 0x400
            SLR_MACHINE_IN_LOCAL_TARGET = 0x800
            SLR_UPDATE_MACHINE_AND_SID = 0x1000
            SLR_NO_OBJECT_ID = 0x2000


        SLR_NONE = SLR_FLAGS.SLR_NONE
        SLR_NO_UI = SLR_FLAGS.SLR_NO_UI
        SLR_ANY_MATCH = SLR_FLAGS.SLR_ANY_MATCH
        SLR_UPDATE = SLR_FLAGS.SLR_UPDATE
        SLR_NOUPDATE = SLR_FLAGS.SLR_NOUPDATE
        SLR_NOSEARCH = SLR_FLAGS.SLR_NOSEARCH
        SLR_NOTRACK = SLR_FLAGS.SLR_NOTRACK
        SLR_NOLINKINFO = SLR_FLAGS.SLR_NOLINKINFO
        SLR_INVOKE_MSI = SLR_FLAGS.SLR_INVOKE_MSI
        SLR_NO_UI_WITH_MSG_PUMP = SLR_FLAGS.SLR_NO_UI_WITH_MSG_PUMP
        SLR_OFFER_DELETE_WITHOUT_FILE = SLR_FLAGS.SLR_OFFER_DELETE_WITHOUT_FILE
        SLR_KNOWNFOLDER = SLR_FLAGS.SLR_KNOWNFOLDER
        SLR_MACHINE_IN_LOCAL_TARGET = SLR_FLAGS.SLR_MACHINE_IN_LOCAL_TARGET
        SLR_UPDATE_MACHINE_AND_SID = SLR_FLAGS.SLR_UPDATE_MACHINE_AND_SID
        SLR_NO_OBJECT_ID = SLR_FLAGS.SLR_NO_OBJECT_ID
        class SLGP_FLAGS(ENUM):
            SLGP_SHORTPATH = 0x1
            SLGP_UNCPRIORITY = 0x2
            SLGP_RAWPATH = 0x4
            SLGP_RELATIVEPRIORITY = 0x8


        SLGP_SHORTPATH = SLGP_FLAGS.SLGP_SHORTPATH
        SLGP_UNCPRIORITY = SLGP_FLAGS.SLGP_UNCPRIORITY
        SLGP_RAWPATH = SLGP_FLAGS.SLGP_RAWPATH
        SLGP_RELATIVEPRIORITY = SLGP_FLAGS.SLGP_RELATIVEPRIORITY
        if not defined(__IShellLinkA_INTERFACE_DEFINED__):
            __IShellLinkA_INTERFACE_DEFINED__ = 1

            # interface IShellLinkA

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellLinkA._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPath',
                        (['out', ], LPSTR, 'pszFile'),
                        (['in'], INT, 'cch'),
                        (
                            ['out', 'unique', 'in'],
                            POINTER(WIN32_FIND_DATAA),
                           'pfd'
                        ),
                        ([], DWORD, 'fFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIDList',
                        (['out'], POINTER(PIDLIST_ABSOLUTE), ' ppidl'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetIDList',
                        (['in'], PCIDLIST_ABSOLUTE, 'pidl'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDescription',
                        (['out', ], LPSTR, 'pszName'),
                        (['in'], INT, 'cch'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetDescription',
                        (['in'], LPCSTR, 'pszName'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetWorkingDirectory',
                        (['out', ], LPSTR, 'pszDir'),
                        (['in'], INT, 'cch'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetWorkingDirectory',
                        (['in'], LPCSTR, 'pszDir'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetArguments',
                        (['out'], LPSTR, 'pszArgs'),
                        (['in'], INT, 'cch'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetArguments',
                        (['in'], LPCSTR, 'pszArgs'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetHotkey',
                        (['out'], POINTER(WORD), 'pwHotkey'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetHotkey',
                        (['in'], WORD, 'wHotkey'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetShowCmd',
                        (['out'], POINTER(INT), 'piShowCmd'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetShowCmd',
                        (['in'], INT, 'iShowCmd'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIconLocation',
                        (['out', ], LPSTR, 'pszIconPath'),
                        (['in'], INT, 'cch'),
                        (['out'], POINTER(INT), 'piIcon'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetIconLocation',
                        (['in'], LPCSTR, 'pszIconPath'),
                        (['in'], INT, 'iIcon'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetRelativePath',
                        (['in'], LPCSTR, 'pszPathRel'),
                        (['in'], DWORD, 'dwReserved'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Resolve',
                        (['unique', 'in'], HWND, 'hwnd'),
                        (['in'], DWORD, 'fFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetPath',
                        (['in'], LPCSTR, 'pszFile'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IShellLinkA_INTERFACE_DEFINED__
        if not defined(__IShellLinkW_INTERFACE_DEFINED__):
            __IShellLinkW_INTERFACE_DEFINED__ = 1

            # interface IShellLinkW

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellLinkW._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPath',
                        (['out', ], LPWSTR, 'pszFile'),
                        (['in'], INT, 'cch'),
                        (
                            ['out', 'unique', 'in'],
                            POINTER(WIN32_FIND_DATAW),
                           'pfd'
                        ),
                        ([], DWORD, 'fFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIDList',
                        (['out'], POINTER(PIDLIST_ABSOLUTE), ' ppidl'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetIDList',
                        (['unique', 'in'], PCIDLIST_ABSOLUTE, 'pidl'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDescription',
                        (['out', ], LPWSTR, 'pszName'),
                        ([], INT, 'cch'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetDescription',
                        (['in'], LPCWSTR, 'pszName'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetWorkingDirectory',
                        (['out'], LPWSTR, 'pszDir'),
                        ([], INT, 'cch'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetWorkingDirectory',
                        (['in'], LPCWSTR, 'pszDir'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetArguments',
                        (['out'], LPWSTR, 'pszArgs'),
                        (['in'], INT, 'cch'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetArguments',
                        (['in'], LPCWSTR, 'pszArgs'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetHotkey',
                        (['out'], POINTER(WORD), 'pwHotkey'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetHotkey',
                        (['in'], WORD, 'wHotkey'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetShowCmd',
                        (['out'], POINTER(INT), 'piShowCmd'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetShowCmd',
                        (['in'], INT, 'iShowCmd'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIconLocation',
                        (['out'], LPWSTR, 'pszIconPath'),
                        (['in'], INT, 'cch'),
                        (['out'], POINTER(INT), 'piIcon'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetIconLocation',
                        (['in'], LPCWSTR, 'pszIconPath'),
                        (['in'], INT, 'iIcon'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetRelativePath',
                        (['in'], LPCWSTR, 'pszPathRel'),
                        (['in'], DWORD, 'dwReserved'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Resolve',
                        (['unique', 'in'], HWND, 'hwnd'),
                        (['in'], DWORD, 'fFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetPath',
                        (['in'], LPCWSTR, 'pszFile'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IShellLinkW_INTERFACE_DEFINED__
        if not defined(__IShellLinkDataList_INTERFACE_DEFINED__):
            __IShellLinkDataList_INTERFACE_DEFINED__ = 1

            # interface IShellLinkDataList

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]
            else: # C style interface
                IShellLinkDataList._methods_ = [
                    #
                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'AddDataBlock',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(VOID),
                           ' pDataBlock'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'CopyDataBlock',
                        ([annotation('_In_'), 'in'], DWORD, 'dwSig'),
                        (
                            ['out', annotation('_Outptr_')],
                            POINTER(POINTER(VOID)),
                           'ppDataBlock'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveDataBlock',
                        (['in'], DWORD, 'dwSig'),
                    ),

                    # flags are SLDF_ values as defined in shlobj.h
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFlags',
                        (['out'], POINTER(DWORD), 'pdwFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetFlags',
                        (['in'], DWORD, 'dwFlags'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IShellLinkDataList_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0057

        # [local]
        if (NTDDI_VERSION >= NTDDI_WIN2K):
            if not defined(__IResolveShellLink_INTERFACE_DEFINED__):
                __IResolveShellLink_INTERFACE_DEFINED__ = 1

                # interface IResolveShellLink

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IResolveShellLink._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ResolveShellLink',
                            (['in'], POINTER(IUnknown), 'punkLink'),
                            (['unique', 'in'], HWND, 'hwnd'),
                            ([], DWORD, 'fFlags'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IResolveShellLink_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0058

            # [local]
        # END IF   NTDDI_WIN2K
        if not defined(__IActionProgressDialog_INTERFACE_DEFINED__):
            __IActionProgressDialog_INTERFACE_DEFINED__ = 1

            # interface IActionProgressDialog

            # [unique][uuid][object]

            # [v1_enum]


            class _SPINITF(ENUM):
                SPINITF_NORMAL = 0
                SPINITF_MODAL = 0x1
                SPINITF_NOMINIMIZE = 0x8


            SPINITF_NORMAL = _SPINITF.SPINITF_NORMAL
            SPINITF_MODAL = _SPINITF.SPINITF_MODAL
            SPINITF_NOMINIMIZE = _SPINITF.SPINITF_NOMINIMIZE
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IActionProgressDialog._methods_ = [

                    # default normal progress behavior call punkSite -
                    # >EnableModeless() or EnableWindow() Do not have a
                    # minimize button in the caption bar.
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], SPINITF, 'flags'),
                        (['unique', , 'in'], LPCWSTR, 'pszTitle'),
                        ([], LPCWSTR, 'pszCancel'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Stop',
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IActionProgressDialog_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0059

        # [local]
        ARCONTENT_AUTORUNINF = 0x00000002
        ARCONTENT_AUDIOCD = 0x00000004
        ARCONTENT_DVDMOVIE = 0x00000008
        ARCONTENT_BLANKCD = 0x00000010
        ARCONTENT_BLANKDVD = 0x00000020
        ARCONTENT_UNKNOWNCONTENT = 0x00000040
        ARCONTENT_AUTOPLAYPIX = 0x00000080
        ARCONTENT_AUTOPLAYMUSIC = 0x00000100
        ARCONTENT_AUTOPLAYVIDEO = 0x00000200

        if (NTDDI_VERSION >= NTDDI_VISTA):
            ARCONTENT_VCD = 0x00000400
            ARCONTENT_SVCD = 0x00000800
            ARCONTENT_DVDAUDIO = 0x00001000
            ARCONTENT_BLANKBD = 0x00002000
            ARCONTENT_BLURAY = 0x00004000
            ARCONTENT_CAMERASTORAGE = 0x00008000
            ARCONTENT_CUSTOMEVENT = 0x00010000
            ARCONTENT_NONE = 0x00000000
            ARCONTENT_MASK = 0x0001FFFE
            ARCONTENT_PHASE_UNKNOWN = 0x00000000
            ARCONTENT_PHASE_PRESNIFF = 0x10000000
            ARCONTENT_PHASE_SNIFFING = 0x20000000
            ARCONTENT_PHASE_FINAL = 0x40000000
            ARCONTENT_PHASE_MASK = 0x70000000
        # END IF   NTDDI_VISTA

        if not defined(__IActionProgress_INTERFACE_DEFINED__):
            __IActionProgress_INTERFACE_DEFINED__ = 1

            # interface IActionProgress

            # [unique][uuid][object]

            # [v1_enum]


            class _SPBEGINF(ENUM):
                SPBEGINF_NORMAL = 0
                SPBEGINF_AUTOTIME = 0x2
                SPBEGINF_NOPROGRESSBAR = 0x10
                SPBEGINF_MARQUEEPROGRESS = 0x20
                SPBEGINF_NOCANCELBUTTON = 0x40


            SPBEGINF_NORMAL = _SPBEGINF.SPBEGINF_NORMAL
            SPBEGINF_AUTOTIME = _SPBEGINF.SPBEGINF_AUTOTIME
            SPBEGINF_NOPROGRESSBAR = _SPBEGINF.SPBEGINF_NOPROGRESSBAR
            SPBEGINF_MARQUEEPROGRESS = _SPBEGINF.SPBEGINF_MARQUEEPROGRESS
            SPBEGINF_NOCANCELBUTTON = _SPBEGINF.SPBEGINF_NOCANCELBUTTON
            class _SPACTION(ENUM):
                SPACTION_NONE = 0
                #~#~#~ SPACTION_MOVING    = ( SPACTION_NONE + 1 )
                #~#~#~ SPACTION_COPYING    = ( SPACTION_MOVING + 1 )
                #~#~#~ SPACTION_RECYCLING    = ( SPACTION_COPYING + 1 )
                #~#~#~ SPACTION_APPLYINGATTRIBS    = ( SPACTION_RECYCLING + 1 )
                #~#~#~ SPACTION_DOWNLOADING    = ( SPACTION_APPLYINGATTRIBS + 1 )
                #~#~#~ SPACTION_SEARCHING_INTERNET    = ( SPACTION_DOWNLOADING + 1 )
                #~#~#~ SPACTION_CALCULATING    = ( SPACTION_SEARCHING_INTERNET + 1 )
                #~#~#~ SPACTION_UPLOADING    = ( SPACTION_CALCULATING + 1 )
                #~#~#~ SPACTION_SEARCHING_FILES    = ( SPACTION_UPLOADING + 1 )
                #~#~#~ SPACTION_DELETING    = ( SPACTION_SEARCHING_FILES + 1 )
                #~#~#~ SPACTION_RENAMING    = ( SPACTION_DELETING + 1 )
                #~#~#~ SPACTION_FORMATTING    = ( SPACTION_RENAMING + 1 )
                #~#~#~ SPACTION_COPY_MOVING    = ( SPACTION_FORMATTING + 1 )


            SPACTION = _SPACTION
            SPACTION_NONE = _SPACTION.SPACTION_NONE
            class _SPTEXT(ENUM):
                SPTEXT_ACTIONDESCRIPTION = 1
                #~#~#~ SPTEXT_ACTIONDETAIL    = ( SPTEXT_ACTIONDESCRIPTION + 1 )


            SPTEXT = _SPTEXT
            SPTEXT_ACTIONDESCRIPTION = _SPTEXT.SPTEXT_ACTIONDESCRIPTION
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IActionProgress._methods_ = [

                    # default normal progress behavior automatically updates
                    # the "time remaining" text Don't display the progress bar
                    # (SetProgress() wont be called) use marquee progress
                    # (comctl32 v6 required) no cancel button
                    # Vista or higher Vista or higher Vista or higher Move as
                    # copy - delete, Windows 7 or higher
                    #
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Begin',
                        (['in'], SPACTION, 'action'),
                        ([], SPBEGINF, 'flags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'UpdateProgress',
                        (['in'], ULONGLONG, 'ulCompleted'),
                        ([], ULONGLONG, 'ulTotal'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'UpdateText',
                        (['in'], SPTEXT, 'sptext'),
                        (['in'], LPCWSTR, 'pszText'),
                        ([], BOOL, 'fMayCompact'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'QueryCancel',
                        (['out'], POINTER(BOOL), ' pfCancelled'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ResetCancel',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'End',
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IActionProgress_INTERFACE_DEFINED__
        if not defined(__IShellExtInit_INTERFACE_DEFINED__):
            __IShellExtInit_INTERFACE_DEFINED__ = 1

            # interface IShellExtInit

            # [unique][local][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][unique][in]
            else: # C style interface
                IShellExtInit._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            PCIDLIST_ABSOLUTE,
                           'pidlFolder'
                        ),
                        ([], POINTER(IDataObject), 'pdtobj'),
                        ([], HKEY, 'hkeyProgID'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][unique][in]
            # END IF  C style interface
        # END IF  __IShellExtInit_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0061

        # [local]
        if not defined(__IShellPropSheetExt_INTERFACE_DEFINED__):
            __IShellPropSheetExt_INTERFACE_DEFINED__ = 1

            # interface IShellPropSheetExt

            # [unique][local][object][uuid]

            # [v1_enum]


            class _EXPPS(ENUM):
                EXPPS_FILETYPES = 0x1


            EXPPS_FILETYPES = _EXPPS.EXPPS_FILETYPES
            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            else: # C style interface
                IShellPropSheetExt._methods_ = [
                    #

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'AddPages',
                        (
                            [annotation('_In_'), 'in'],
                            LPFNSVADDPROPSHEETPAGE,
                           'pfnAddPage'
                        ),
                        ([], LPARAM, 'lParam'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ReplacePage',
                        ([annotation('_In_'), 'in'], EXPPS, 'uPageID'),
                        ([], LPFNSVADDPROPSHEETPAGE, 'pfnReplaceWith'),
                        ([], LPARAM, 'lParam'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IShellPropSheetExt_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0062

        # [local]
        if not defined(__IRemoteComputer_INTERFACE_DEFINED__):
            __IRemoteComputer_INTERFACE_DEFINED__ = 1

            # interface IRemoteComputer

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IRemoteComputer._methods_ = [
                    # function is called when the explorer is initializing or

                    # enumerating the name space extension. If failure is
                    # returned during
                    # enumeration, the extension won't appear for this
                    # computer. Otherwise,
                    # the extension will appear, and should target the given
                    # machine.
                    # pszMachine  Specifies the name of the machine to target.
                    # (\\server)
                    # bEnumerationg test to see if this object should be
                    # enumerated
                    # on this server
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], LPCWSTR, 'pszMachine'),
                        (['in'], BOOL, 'bEnumerating'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IRemoteComputer_INTERFACE_DEFINED__
        if not defined(__IQueryContinue_INTERFACE_DEFINED__):
            __IQueryContinue_INTERFACE_DEFINED__ = 1

            # interface IQueryContinue

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IQueryContinue._methods_ = [
                    # S_OK - > Continue, S_FALSE - > Cancel
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'QueryContinue',
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IQueryContinue_INTERFACE_DEFINED__
        if not defined(__IObjectWithCancelEvent_INTERFACE_DEFINED__):
            __IObjectWithCancelEvent_INTERFACE_DEFINED__ = 1

            # interface IObjectWithCancelEvent

            # [unique][local][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][out]
            else: # C style interface
                IObjectWithCancelEvent._methods_ = [

                    # Call this function to retrieve an event that will be
                    # signaled when
                    # the callee cancels the operation it's performing.
                    # The caller is responsible for closing the returned
                    # handle.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCancelEvent',
                        (
                            ['out', annotation('_Out_')],
                            POINTER(HANDLE),
                           'phEvent'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IObjectWithCancelEvent_INTERFACE_DEFINED__
        if not defined(__IUserNotification_INTERFACE_DEFINED__):
            __IUserNotification_INTERFACE_DEFINED__ = 1

            # interface IUserNotification

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IUserNotification._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetBalloonInfo',
                        (['unique', , 'in'], LPCWSTR, 'pszTitle'),
                        ([], LPCWSTR, 'pszText'),
                        (['in'], DWORD, 'dwInfoFlags'),
                    ),

                    # times in msec                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetBalloonRetry',
                        (['in'], DWORD, 'dwShowTime'),
                        ([], DWORD, 'dwInterval'),
                        ([], UINT, 'cRetryCount'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetIconInfo',
                        (['unique', 'in'], HICON, 'hIcon'),
                        (['unique', 'in'], LPCWSTR, 'pszToolTip'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Show',
                        (['unique', 'in'], POINTER(IQueryContinue), 'pqc'),
                        (['in'], DWORD, 'dwContinuePollInterval'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'PlaySound',
                        (['in'], LPCWSTR, 'pszSoundName'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IUserNotification_INTERFACE_DEFINED__
        if not defined(__IItemNameLimits_INTERFACE_DEFINED__):
            __IItemNameLimits_INTERFACE_DEFINED__ = 1

            # interface IItemNameLimits

            # [object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IItemNameLimits._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetValidCharacters',
                        (['out'], POINTER(LPWSTR), 'ppwszValidChars'),
                        ([], POINTER(LPWSTR), 'ppwszInvalidChars'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetMaxLength',
                        (['in'], LPCWSTR, 'pszName'),
                        (['out'], POINTER(INT), 'piMaxNameLen'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IItemNameLimits_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0067

        # [local]
        if (NTDDI_VERSION >= NTDDI_VISTA):
            if not defined(__ISearchFolderItemFactory_INTERFACE_DEFINED__):
                __ISearchFolderItemFactory_INTERFACE_DEFINED__ = 1

                # interface ISearchFolderItemFactory

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    ISearchFolderItemFactory._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetDisplayName',
                            (['in'], LPCWSTR, 'pszDisplayName'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFolderTypeID',
                            (['in'], FOLDERTYPEID, 'ftid'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFolderLogicalViewMode',
                            (['in'], FOLDERLOGICALVIEWMODE, 'flvm'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetIconSize',
                            (['in'], INT, 'iIconSize'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetVisibleColumns',
                            (['in'], UINT, 'cVisibleColumns'),
                            (['in'], POINTER(PROPERTYKEY), 'rgKey'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSortColumns',
                            (['in'], UINT, 'cSortColumns'),
                            (['in'], POINTER(SORTCOLUMN), 'rgSortColumns'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetGroupColumn',
                            (['in'], REFPROPERTYKEY, 'keyGroup'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetStacks',
                            (['in'], UINT, 'cStackKeys'),
                            (['in'], POINTER(PROPERTYKEY), 'rgStackKeys'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetScope',
                            (['in'], POINTER(IShellItemArray), 'psiaScope'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetCondition',
                            (['in'], POINTER(ICondition), 'pCondition'),
                        ),

                        # returns IShellItem, navigate to this                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetShellItem',
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetIDList',
                            (['out'], POINTER(PIDLIST_ABSOLUTE), 'ppidl'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __ISearchFolderItemFactory_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0068

            # [local]
        # END IF   NTDDI_VISTA
        IEI_PRIORITY_MAX = ITSAT_MAX_PRIORITY
        IEI_PRIORITY_MIN = ITSAT_MIN_PRIORITY
        IEIT_PRIORITY_NORMAL = ITSAT_DEFAULT_PRIORITY
        IEIFLAG_ASYNC = 0x0001
        IEIFLAG_CACHE = 0x0002
        IEIFLAG_ASPECT = 0x0004
        IEIFLAG_OFFLINE = 0x0008
        IEIFLAG_GLEAM = 0x0010
        IEIFLAG_SCREEN = 0x0020
        IEIFLAG_ORIGSIZE = 0x0040
        IEIFLAG_NOSTAMP = 0x0080
        IEIFLAG_NOBORDER = 0x0100
        IEIFLAG_QUALITY = 0x0200
        IEIFLAG_REFRESH = 0x0400

        if not defined(__IExtractImage_INTERFACE_DEFINED__):
            __IExtractImage_INTERFACE_DEFINED__ = 1

            # interface IExtractImage

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IExtractImage._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetLocation',
                        (['out', ], LPWSTR, 'pszPathBuffer'),
                        (['in'], DWORD, 'cch'),
                        (
                            ['out', 'unique', 'in'],
                            POINTER(DWORD),
                           'pdwPriority'
                        ),
                        ([], POINTER(SIZE), ' prgSize'),
                        ([], DWORD, 'dwRecClrDepth'),
                        (['out', 'in'], POINTER(DWORD), 'pdwFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Extract',
                        (['out'], POINTER(HBITMAP), 'phBmpThumbnail'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IExtractImage_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0069

        # [local]
        if not defined(__IExtractImage2_INTERFACE_DEFINED__):
            __IExtractImage2_INTERFACE_DEFINED__ = 1

            # interface IExtractImage2

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IExtractImage2._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDateStamp',
                        (['out'], POINTER(FILETIME), 'pDateStamp'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IExtractImage2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0070

        # [local]
        if not defined(__IThumbnailHandlerFactory_INTERFACE_DEFINED__):
            __IThumbnailHandlerFactory_INTERFACE_DEFINED__ = 1

            # interface IThumbnailHandlerFactory

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IThumbnailHandlerFactory._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetThumbnailHandler',
                        (['in'], PCUITEMID_CHILD, 'pidlChild'),
                        (['unique', 'in'], POINTER(IBindCtx), 'pbc'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IThumbnailHandlerFactory_INTERFACE_DEFINED__
        if not defined(__IParentAndItem_INTERFACE_DEFINED__):
            __IParentAndItem_INTERFACE_DEFINED__ = 1

            # interface IParentAndItem

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][out]

                # [annotation][out]

                # [annotation][out]
            else: # C style interface
                IParentAndItem._methods_ = [
                    # 2 ways to init

                    # pidlParent == NULL
                    # psf is folder, pidlChild is child relative to psf
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetParentAndItem',
                        (['unique', 'in'], PCIDLIST_ABSOLUTE, 'pidlParent'),
                        ([], POINTER(IShellFolder), 'psf'),
                        (['in'], PCUITEMID_CHILD, 'pidlChild'),
                    ),

                    # all params optional
                    # ppidlParent gets full pidl to parent of item
                    # ppsf gets parent folder for item
                    # ppidlChild gets item relitve to psf
                    #                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'GetParentAndItem',
                        (
                            [annotation('_Outptr_opt_'), 'out'],
                            POINTER(PIDLIST_ABSOLUTE),
                           'ppidlParent'
                        ),
                        ([], POINTER(POINTER(IShellFolder)), 'ppsf'),
                        ([], POINTER(PITEMID_CHILD), 'ppidlChild'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoteGetParentAndItem',
                        (['out'], POINTER(PIDLIST_ABSOLUTE), 'ppidlParent'),
                        ([], POINTER(POINTER(IShellFolder)), 'ppsf'),
                        ([], POINTER(PITEMID_CHILD), 'ppidlChild'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][out]

                # [annotation][out]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IParentAndItem_INTERFACE_DEFINED__
        if not defined(__IDockingWindow_INTERFACE_DEFINED__):
            __IDockingWindow_INTERFACE_DEFINED__ = 1

            # interface IDockingWindow

            # [object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IDockingWindow._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ShowDW',
                        (['in'], BOOL, 'fShow'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CloseDW',
                        (['in'], DWORD, 'dwReserved'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ResizeBorderDW',
                        (['unique', 'in'], LPCRECT, 'prcBorder'),
                        ([], POINTER(IUnknown), 'punkToolbarSite'),
                        (['in'], BOOL, 'fReserved'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IDockingWindow_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0073

        # [local]
        DBIM_MINSIZE = 0x0001
        DBIM_MAXSIZE = 0x0002
        DBIM_INTEGRAL = 0x0004
        DBIM_ACTUAL = 0x0008
        DBIM_TITLE = 0x0010
        DBIM_MODEFLAGS = 0x0020
        DBIM_BKCOLOR = 0x0040
        class DESKBANDINFO(ctypes.Structure):
            pass
        DESKBANDINFO._fields_ = [
            ('dwMask', DWORD),
            ('ptMinSize', POINTL),
            ('ptMaxSize', POINTL),
            ('ptIntegral', POINTL),
            ('ptActual', POINTL),
            ('wszTitle', WCHAR * 256),
            ('dwModeFlags', DWORD),
            ('crBkgnd', COLORREF),
        ]


        DBIMF_NORMAL = 0x0000
        DBIMF_FIXED = 0x0001
        DBIMF_FIXEDBMP = 0x0004
        DBIMF_VARIABLEHEIGHT = 0x0008
        DBIMF_UNDELETEABLE = 0x0010
        DBIMF_DEBOSSED = 0x0020
        DBIMF_BKCOLOR = 0x0040
        DBIMF_USECHEVRON = 0x0080
        DBIMF_BREAK = 0x0100
        DBIMF_ADDTOFRONT = 0x0200
        DBIMF_TOPALIGN = 0x0400

        if (NTDDI_VERSION >= NTDDI_VISTA):
            DBIMF_NOGRIPPER = 0x0800
            DBIMF_ALWAYSGRIPPER = 0x1000
            DBIMF_NOMARGINS = 0x2000
        # END IF   NTDDI_VISTA
        DBIF_VIEWMODE_NORMAL = 0x0000
        DBIF_VIEWMODE_VERTICAL = 0x0001
        DBIF_VIEWMODE_FLOATING = 0x0002
        DBIF_VIEWMODE_TRANSPARENT = 0x0004


        class tagDESKBANDCID(ENUM):
            DBID_BANDINFOCHANGED = 0
            DBID_SHOWONLY = 1
            DBID_MAXIMIZEBAND = 2
            DBID_PUSHCHEVRON = 3
            DBID_DELAYINIT = 4
            DBID_FINISHINIT = 5
            DBID_SETWINDOWTHEME = 6
            DBID_PERMITAUTOHIDE = 7


        DBID_BANDINFOCHANGED = tagDESKBANDCID.DBID_BANDINFOCHANGED
        DBID_SHOWONLY = tagDESKBANDCID.DBID_SHOWONLY
        DBID_MAXIMIZEBAND = tagDESKBANDCID.DBID_MAXIMIZEBAND
        DBID_PUSHCHEVRON = tagDESKBANDCID.DBID_PUSHCHEVRON
        DBID_DELAYINIT = tagDESKBANDCID.DBID_DELAYINIT
        DBID_FINISHINIT = tagDESKBANDCID.DBID_FINISHINIT
        DBID_SETWINDOWTHEME = tagDESKBANDCID.DBID_SETWINDOWTHEME
        DBID_PERMITAUTOHIDE = tagDESKBANDCID.DBID_PERMITAUTOHIDE
        DBPC_SELECTFIRST =  - 1
        DBPC_SELECTLAST =  - 2
        CGID_DeskBand = IID_IDeskBand

        if not defined(__IDeskBand_INTERFACE_DEFINED__):
            __IDeskBand_INTERFACE_DEFINED__ = 1

            # interface IDeskBand

            # [object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IDeskBand._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetBandInfo',
                        (['in'], DWORD, 'dwBandID'),
                        ([], DWORD, 'dwViewMode'),
                        (['out', 'in'], POINTER(DESKBANDINFO), 'pdbi'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IDeskBand_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0074

        # [local]
        if (NTDDI_VERSION >= NTDDI_VISTA):
            if not defined(__IDeskBandInfo_INTERFACE_DEFINED__):
                __IDeskBandInfo_INTERFACE_DEFINED__ = 1

                # interface IDeskBandInfo

                # [object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IDeskBandInfo._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetDefaultBandWidth',
                            (['in'], DWORD, 'dwBandID'),
                            ([], DWORD, 'dwViewMode'),
                            (['out'], POINTER(INT), 'pnWidth'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IDeskBandInfo_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0075

            # [local]
        # END IF   NTDDI_VISTA
        if not defined(__ITaskbarList_INTERFACE_DEFINED__):
            __ITaskbarList_INTERFACE_DEFINED__ = 1

            # interface ITaskbarList

            # [object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                ITaskbarList._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'HrInit',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'AddTab',
                        (['in'], HWND, 'hwnd'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'DeleteTab',
                        (['in'], HWND, 'hwnd'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ActivateTab',
                        (['in'], HWND, 'hwnd'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetActiveAlt',
                        (['in'], HWND, 'hwnd'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ITaskbarList_INTERFACE_DEFINED__
        if not defined(__ITaskbarList2_INTERFACE_DEFINED__):
            __ITaskbarList2_INTERFACE_DEFINED__ = 1

            # interface ITaskbarList2

            # [object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                ITaskbarList2._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'MarkFullscreenWindow',
                        (['in'], HWND, 'hwnd'),
                        ([], BOOL, 'fFullscreen'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ITaskbarList2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0077

        # [local]
        if defined(MIDL_PASS):
            pass
        # END IF
        class THUMBBUTTONFLAGS(ENUM):
            THBF_ENABLED = 0
            THBF_DISABLED = 0x1
            THBF_DISMISSONCLICK = 0x2
            THBF_NOBACKGROUND = 0x4
            THBF_HIDDEN = 0x8
            THBF_NONINTERACTIVE = 0x10


        THBF_ENABLED = THUMBBUTTONFLAGS.THBF_ENABLED
        THBF_DISABLED = THUMBBUTTONFLAGS.THBF_DISABLED
        THBF_DISMISSONCLICK = THUMBBUTTONFLAGS.THBF_DISMISSONCLICK
        THBF_NOBACKGROUND = THUMBBUTTONFLAGS.THBF_NOBACKGROUND
        THBF_HIDDEN = THUMBBUTTONFLAGS.THBF_HIDDEN
        THBF_NONINTERACTIVE = THUMBBUTTONFLAGS.THBF_NONINTERACTIVE
        class THUMBBUTTONMASK(ENUM):
            THB_BITMAP = 0x1
            THB_ICON = 0x2
            THB_TOOLTIP = 0x4
            THB_FLAGS = 0x8


        THB_BITMAP = THUMBBUTTONMASK.THB_BITMAP
        THB_ICON = THUMBBUTTONMASK.THB_ICON
        THB_TOOLTIP = THUMBBUTTONMASK.THB_TOOLTIP
        THB_FLAGS = THUMBBUTTONMASK.THB_FLAGS
        class THUMBBUTTON(ctypes.Structure):
            pass
        THUMBBUTTON._fields_ = [
            ('dwMask', THUMBBUTTONMASK),
            ('iId', UINT),
            ('iBitmap', UINT),
            ('hIcon', HICON),
            ('szTip', WCHAR * 260),
            ('dwFlags', THUMBBUTTONFLAGS),
        ]


        LPTHUMBBUTTON = POINTER(THUMBBUTTON)


        THBN_CLICKED = 0x1800

        if not defined(__ITaskbarList3_INTERFACE_DEFINED__):
            __ITaskbarList3_INTERFACE_DEFINED__ = 1

            # interface ITaskbarList3

            # [object][uuid]


            class TBPFLAG(ENUM):
                TBPF_NOPROGRESS = 0
                TBPF_INDETERMINATE = 0x1
                TBPF_NORMAL = 0x2
                TBPF_ERROR = 0x4
                TBPF_PAUSED = 0x8


            TBPF_NOPROGRESS = TBPFLAG.TBPF_NOPROGRESS
            TBPF_INDETERMINATE = TBPFLAG.TBPF_INDETERMINATE
            TBPF_NORMAL = TBPFLAG.TBPF_NORMAL
            TBPF_ERROR = TBPFLAG.TBPF_ERROR
            TBPF_PAUSED = TBPFLAG.TBPF_PAUSED
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                ITaskbarList3._methods_ = [
                    # Flags for Setting Taskbar Progress state

                    #
                    #
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetProgressState',
                        (['in'], HWND, 'hwnd'),
                        ([], TBPFLAG, 'tbpFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RegisterTab',
                        (['in'], HWND, 'hwndTab'),
                        ([], HWND, 'hwndMDI'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'UnregisterTab',
                        (['in'], HWND, 'hwndTab'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetTabOrder',
                        (['in'], HWND, 'hwndTab'),
                        ([], HWND, 'hwndInsertBefore'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetTabActive',
                        (['in'], HWND, 'hwndTab'),
                        ([], HWND, 'hwndMDI'),
                        ([], DWORD, 'dwReserved'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ThumbBarAddButtons',
                        (['in'], HWND, 'hwnd'),
                        ([], UINT, 'cButtons'),
                        (['in'], LPTHUMBBUTTON, 'pButton'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ThumbBarUpdateButtons',
                        (['in'], HWND, 'hwnd'),
                        ([], UINT, 'cButtons'),
                        (['in'], LPTHUMBBUTTON, 'pButton'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ThumbBarSetImageList',
                        (['in'], HWND, 'hwnd'),
                        ([], HIMAGELIST, 'himl'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetOverlayIcon',
                        (['in'], HWND, 'hwnd'),
                        ([], HICON, 'hIcon'),
                        (['unique', , 'in'], LPCWSTR, 'pszDescription'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetThumbnailTooltip',
                        (['in'], HWND, 'hwnd'),
                        (['unique', , 'in'], LPCWSTR, 'pszTip'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetThumbnailClip',
                        (['in'], HWND, 'hwnd'),
                        ([], POINTER(RECT), 'prcClip'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ITaskbarList3_INTERFACE_DEFINED__
        if not defined(__ITaskbarList4_INTERFACE_DEFINED__):
            __ITaskbarList4_INTERFACE_DEFINED__ = 1

            # interface ITaskbarList4

            # [object][uuid]


            class STPFLAG(ENUM):
                STPF_NONE = 0
                STPF_USEAPPTHUMBNAILALWAYS = 0x1
                STPF_USEAPPTHUMBNAILWHENACTIVE = 0x2
                STPF_USEAPPPEEKALWAYS = 0x4
                STPF_USEAPPPEEKWHENACTIVE = 0x8


            STPF_NONE = STPFLAG.STPF_NONE
            STPF_USEAPPTHUMBNAILALWAYS = STPFLAG.STPF_USEAPPTHUMBNAILALWAYS
            STPF_USEAPPTHUMBNAILWHENACTIVE = STPFLAG.STPF_USEAPPTHUMBNAILWHENACTIVE
            STPF_USEAPPPEEKALWAYS = STPFLAG.STPF_USEAPPPEEKALWAYS
            STPF_USEAPPPEEKWHENACTIVE = STPFLAG.STPF_USEAPPPEEKWHENACTIVE
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                ITaskbarList4._methods_ = [
                    # Flags for Setting Tab Properties

                    #
                    #
                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __ITaskbarList4_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0079

        # [local]
        if (NTDDI_VERSION >= NTDDI_WINXP) or (_WIN32_IE >= _WIN32_IE_IE70):
            if (_WIN32_IE >= _WIN32_IE_IE70):
                if not defined(__IExplorerBrowserEvents_INTERFACE_DEFINED__):
                    __IExplorerBrowserEvents_INTERFACE_DEFINED__ = 1

                    # interface IExplorerBrowserEvents

                    # [object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        IExplorerBrowserEvents._methods_ = [

                            # Returning failure from this will cancel the
                            # navigation.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'OnNavigationPending',
                                (['in'], PCIDLIST_ABSOLUTE, 'pidlFolder'),
                            ),

                            # Called once the view window has been created. Do
                            # any last minute modifcations
                            # to the view here before it is shown
                            # (set view modes, folder flags, etc...)                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'OnViewCreated',
                                (['in'], POINTER(IShellView), 'psv'),
                            ),

                            # Called once the navigation has succeeded
                            # (after OnViewCreated).                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'OnNavigationComplete',
                                (['in'], PCIDLIST_ABSOLUTE, 'pidlFolder'),
                            ),

                            # Called if a navigation failed, despite the call
                            # to IShellBrowser::BrowseObject succeeding.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'OnNavigationFailed',
                                (['in'], PCIDLIST_ABSOLUTE, 'pidlFolder'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __IExplorerBrowserEvents_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0080

                # [local]
                class EXPLORER_BROWSER_OPTIONS(ENUM):
                    EBO_NONE = 0
                    EBO_NAVIGATEONCE = 0x1
                    EBO_SHOWFRAMES = 0x2
                    EBO_ALWAYSNAVIGATE = 0x4
                    EBO_NOTRAVELLOG = 0x8
                    EBO_NOWRAPPERWINDOW = 0x10
                    EBO_HTMLSHAREPOINTVIEW = 0x20
                    EBO_NOBORDER = 0x40
                    EBO_NOPERSISTVIEWSTATE = 0x80


                EBO_NONE = EXPLORER_BROWSER_OPTIONS.EBO_NONE
                EBO_NAVIGATEONCE = EXPLORER_BROWSER_OPTIONS.EBO_NAVIGATEONCE
                EBO_SHOWFRAMES = EXPLORER_BROWSER_OPTIONS.EBO_SHOWFRAMES
                EBO_ALWAYSNAVIGATE = EXPLORER_BROWSER_OPTIONS.EBO_ALWAYSNAVIGATE
                EBO_NOTRAVELLOG = EXPLORER_BROWSER_OPTIONS.EBO_NOTRAVELLOG
                EBO_NOWRAPPERWINDOW = EXPLORER_BROWSER_OPTIONS.EBO_NOWRAPPERWINDOW
                EBO_HTMLSHAREPOINTVIEW = EXPLORER_BROWSER_OPTIONS.EBO_HTMLSHAREPOINTVIEW
                EBO_NOBORDER = EXPLORER_BROWSER_OPTIONS.EBO_NOBORDER
                EBO_NOPERSISTVIEWSTATE = EXPLORER_BROWSER_OPTIONS.EBO_NOPERSISTVIEWSTATE
                class EXPLORER_BROWSER_FILL_FLAGS(ENUM):
                    EBF_NONE = 0
                    EBF_SELECTFROMDATAOBJECT = 0x100
                    EBF_NODROPTARGET = 0x200


                EBF_NONE = EXPLORER_BROWSER_FILL_FLAGS.EBF_NONE
                EBF_SELECTFROMDATAOBJECT = EXPLORER_BROWSER_FILL_FLAGS.EBF_SELECTFROMDATAOBJECT
                EBF_NODROPTARGET = EXPLORER_BROWSER_FILL_FLAGS.EBF_NODROPTARGET
                if not defined(__IExplorerBrowser_INTERFACE_DEFINED__):
                    __IExplorerBrowser_INTERFACE_DEFINED__ = 1

                    # interface IExplorerBrowser

                    # [object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):

                        # [annotation][in]

                        # [annotation][in]

                        # [annotation][unique][in]

                        # [annotation][unique][out][in]

                        # [annotation][in]
                    else: # C style interface
                        IExplorerBrowser._methods_ = [
                            # to clean up this object you must call ::Destroy.

                            #                        
                            COMMETHOD(
                                ['local'],
                                HRESULT,
                                'Initialize',
                                (
                                    [annotation('_In_'), 'in'],
                                    HWND,
                                   'hwndParent'
                                ),
                                ([], POINTER(RECT), 'prc'),
                                (
                                    ['unique', annotation('_In_opt_'), 'in'],
                                    POINTER(FOLDERSETTINGS),
                                   'pfs'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Destroy',
                            ),

                            # relative to hwndParent                        
                            COMMETHOD(
                                ['local'],
                                HRESULT,
                                'SetRect',
                                (
                                    ['unique', 'out', annotation('_Inout_opt_'), 'in'],
                                    POINTER(HDWP),
                                   'phdwp'
                                ),
                                (
                                    [annotation('_In_'), 'in'],
                                    RECT,
                                   'rcBrowser'
                                ),
                            ),

                            # Property bag for view state persistence                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetPropertyBag',
                                (['in'], LPCWSTR, 'pszPropertyBag'),
                            ),

                            # Displayed when view is empty                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetEmptyText',
                                (['in'], LPCWSTR, 'pszEmptyText'),
                            ),

                            # Sets how view displays / operates                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetFolderSettings',
                                (['in'], POINTER(FOLDERSETTINGS), 'pfs'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Advise',
                                (
                                    ['in'],
                                    POINTER(IExplorerBrowserEvents),
                                   'psbe'
                                ),
                                (['out'], POINTER(DWORD), 'pdwCookie'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Unadvise',
                                (['in'], DWORD, 'dwCookie'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetOptions',
                                (['in'], EXPLORER_BROWSER_OPTIONS, 'dwFlag'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetOptions',
                                (
                                    ['out'],
                                    POINTER(EXPLORER_BROWSER_OPTIONS),
                                   'pdwFlag'
                                ),
                            ),

                            # navigate the browser to a particular location
                            # uFlags contains SBSP_ flag values                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'BrowseToIDList',
                                (['in'], PCUIDLIST_RELATIVE, 'pidl'),
                                ([], UINT, 'uFlags'),
                            ),

                            # punk is a shell item (IShellItem) or any object
                            # that can produce an IDList
                            # using SHGetIDListFromObject()
                            # uFlags contains SBSP_ flag values                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'BrowseToObject',
                                (['in'], POINTER(IUnknown), 'punk'),
                                ([], UINT, 'uFlags'),
                            ),

                            # populate from a given data source
                            # punk can be an IDataObject or anything that can
                            # be used with INamespaceWalk                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'FillFromObject',
                                (['unique', 'in'], POINTER(IUnknown), 'punk'),
                                (
                                    ['in'],
                                    EXPLORER_BROWSER_FILL_FLAGS,
                                   'dwFlags'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'RemoveAll',
                            ),

                            # return the current view object on IShellView or
                            # IFolderView or related interface                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetCurrentView',
                                (['in'], REFIID, 'riid'),
                                (['out'], POINTER(POINTER(VOID)), 'ppv'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]

                        # [annotation][in]

                        # [annotation][in]

                        # [annotation][unique][in]

                        # [annotation][unique][out][in]

                        # [annotation][in]
                    # END IF  C style interface
                # END IF  __IExplorerBrowser_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0081

                # [local]
            # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
            if (_WIN32_IE >= _WIN32_IE_IE70):
                if not defined(__IEnumObjects_INTERFACE_DEFINED__):
                    __IEnumObjects_INTERFACE_DEFINED__ = 1

                    # interface IEnumObjects

                    # [unique][object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):

                        # [annotation][in]

                        # [annotation][in]

                        # [annotation][iid_is][length_is][size_is][out]

                        # [annotation][out]
                    else: # C style interface
                        IEnumObjects._methods_ = [
                            #
                        
                            COMMETHOD(
                                ['local'],
                                HRESULT,
                                'Next',
                                ([annotation('_In_'), 'in'], ULONG, 'celt'),
                                ([], REFIID, 'riid'),
                                (
                                    ['out', annotation('_Out_writes_to_(celt, *pceltFetched)), 'in', 'out'],
                                    POINTER(POINTER(VOID)),
                                   'rgelt'
                                ),
                                (
                                    ['out', annotation('_Out_opt_ _Deref_out_range_(0, celt))],
                                    POINTER(ULONG),
                                   'pceltFetched'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'RemoteNext',
                                (['in'], ULONG, 'celt'),
                                ([], REFIID, 'riid'),
                                (
                                    ['out', 'in', 'out'],
                                    POINTER(POINTER(VOID)),
                                   'rgelt'
                                ),
                                (['out'], POINTER(ULONG), 'pceltFetched'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Skip',
                                (['in'], ULONG, 'celt'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Reset',
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Clone',
                                (
                                    ['out'],
                                    POINTER(POINTER(IEnumObjects)),
                                   'ppenum'
                                ),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]

                        # [annotation][in]

                        # [annotation][in]

                        # [annotation][iid_is][length_is][size_is][out]

                        # [annotation][out]
                    # END IF  C style interface
                # END IF  __IEnumObjects_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0082

                # [local]

                # [v1_enum]
                class _OPPROGDLGF(ENUM):
                    OPPROGDLG_DEFAULT = 0
                    OPPROGDLG_ENABLEPAUSE = 0x80
                    OPPROGDLG_ALLOWUNDO = 0x100
                    OPPROGDLG_DONTDISPLAYSOURCEPATH = 0x200
                    OPPROGDLG_DONTDISPLAYDESTPATH = 0x400
                    OPPROGDLG_NOMULTIDAYESTIMATES = 0x800
                    OPPROGDLG_DONTDISPLAYLOCATIONS = 0x1000


                OPPROGDLG_DEFAULT = _OPPROGDLGF.OPPROGDLG_DEFAULT
                OPPROGDLG_ENABLEPAUSE = _OPPROGDLGF.OPPROGDLG_ENABLEPAUSE
                OPPROGDLG_ALLOWUNDO = _OPPROGDLGF.OPPROGDLG_ALLOWUNDO
                OPPROGDLG_DONTDISPLAYSOURCEPATH = _OPPROGDLGF.OPPROGDLG_DONTDISPLAYSOURCEPATH
                OPPROGDLG_DONTDISPLAYDESTPATH = _OPPROGDLGF.OPPROGDLG_DONTDISPLAYDESTPATH
                OPPROGDLG_NOMULTIDAYESTIMATES = _OPPROGDLGF.OPPROGDLG_NOMULTIDAYESTIMATES
                OPPROGDLG_DONTDISPLAYLOCATIONS = _OPPROGDLGF.OPPROGDLG_DONTDISPLAYLOCATIONS
                if not defined(__IOperationsProgressDialog_INTERFACE_DEFINED__):
                    __IOperationsProgressDialog_INTERFACE_DEFINED__ = 1

                    # interface IOperationsProgressDialog

                    # [unique][object][uuid]

                    # [v1_enum]


                    class _PDMODE(ENUM):
                        PDM_DEFAULT = 0
                        PDM_RUN = 0x1
                        PDM_PREFLIGHT = 0x2
                        PDM_UNDOING = 0x4
                        PDM_ERRORSBLOCKING = 0x8
                        PDM_INDETERMINATE = 0x10


                    PDM_DEFAULT = _PDMODE.PDM_DEFAULT
                    PDM_RUN = _PDMODE.PDM_RUN
                    PDM_PREFLIGHT = _PDMODE.PDM_PREFLIGHT
                    PDM_UNDOING = _PDMODE.PDM_UNDOING
                    PDM_ERRORSBLOCKING = _PDMODE.PDM_ERRORSBLOCKING
                    PDM_INDETERMINATE = _PDMODE.PDM_INDETERMINATE
                    class PDOPSTATUS(ENUM):
                        PDOPS_RUNNING = 1
                        PDOPS_PAUSED = 2
                        PDOPS_CANCELLED = 3
                        PDOPS_STOPPED = 4
                        PDOPS_ERRORS = 5


                    PDOPS_RUNNING = PDOPSTATUS.PDOPS_RUNNING
                    PDOPS_PAUSED = PDOPSTATUS.PDOPS_PAUSED
                    PDOPS_CANCELLED = PDOPSTATUS.PDOPS_CANCELLED
                    PDOPS_STOPPED = PDOPSTATUS.PDOPS_STOPPED
                    PDOPS_ERRORS = PDOPSTATUS.PDOPS_ERRORS
                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        IOperationsProgressDialog._methods_ = [

                            # Operation is running Pre - flight mode,
                            # calculating operation time, etc Operation is
                            # rolling back, undo has been selected Only errors
                            # remain, error dialogs are blocking progress from
                            # completing The length of the operation is
                            # indeterminate, don't show a timer, progressbar
                            # is in marquee mode
                            # Operation is running, no user intervention
                            # Operation has been paused by the user Operation
                            # has been cancelled by the user - now go undo
                            # Operation has been stopped by the user -
                            # terminate completely Operation has gone as far
                            # as it can without throwing error dialogs                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'StartProgressDialog',
                                (['unique', 'in'], HWND, 'hwndOwner'),
                                (['in'], OPPROGDLGF, 'flags'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'StopProgressDialog',
                            ),

                            # Sets which operation is occuring, and whether we
                            # are in pre - flight or undo mode - sets
                            # animations, text, etc.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetOperation',
                                (['in'], SPACTION, 'action'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetMode',
                                (['in'], PDMODE, 'mode'),
                            ),

                            # Progress (in points) we are currently at
                            # Progress (in points) to go to timer Progress
                            # (in bytes) we are currently at Progress
                            # (in bytes) total Progress (in of items) we are
                            # currently at Progress (in of items) total                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'UpdateProgress',
                                (['in'], ULONGLONG, 'ullPointsCurrent'),
                                ([], ULONGLONG, 'ullPointsTotal'),
                                ([], ULONGLONG, 'ullSizeCurrent'),
                                ([], ULONGLONG, 'ullSizeTotal'),
                                ([], ULONGLONG, 'ullItemsCurrent'),
                                ([], ULONGLONG, 'ullItemsTotal'),
                            ),

                            # Used to generate display for
                            # "from <item (path)> to <item (path)>", etc.
                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'UpdateLocations',
                                (
                                    ['unique', 'in'],
                                    POINTER(IShellItem),
                                   'psiSource'
                                ),
                                ([], POINTER(IShellItem), 'psiTarget'),
                                ([], POINTER(IShellItem), 'psiItem'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'ResetTimer',
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'PauseTimer',
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'ResumeTimer',
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetMilliseconds',
                                (['out'], POINTER(ULONGLONG), 'pullElapsed'),
                                ([], POINTER(ULONGLONG), 'pullRemaining'),
                            ),

                            # Returns running/paused/cancelled, etc.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetOperationStatus',
                                (['out'], POINTER(PDOPSTATUS), 'popstatus'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __IOperationsProgressDialog_INTERFACE_DEFINED__
                if not defined(__IIOCancelInformation_INTERFACE_DEFINED__):
                    __IIOCancelInformation_INTERFACE_DEFINED__ = 1

                    # interface IIOCancelInformation

                    # [local][unique][object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):

                        # [annotation][out]

                        # [annotation][out]
                    else: # C style interface
                        IIOCancelInformation._methods_ = [

                            # When the progress UI is cancled by the user,
                            # dwThreadID will have
                            # 1) any pending or future IO requests canceled using CancelSynchronousIo()
                            # 
                            # 2) uMsgCancel will be posted to the thread to tell it to
                            # 
                            # exit a wait that it might be in waiting for
                            # async IO to complete                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetCancelInformation',
                                (['in'], DWORD, 'dwThreadID'),
                                ([], UINT, 'uMsgCancel'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetCancelInformation',
                                (
                                    ['out', annotation('_Out_opt_')],
                                    POINTER(DWORD),
                                   'pdwThreadID'
                                ),
                                ([], POINTER(UINT), 'puMsgCancel'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]

                        # [annotation][out]

                        # [annotation][out]
                    # END IF  C style interface
                # END IF  __IIOCancelInformation_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0084

                # [local]
                FOFX_NOSKIPJUNCTIONS = 0x00010000
                FOFX_PREFERHARDLINK = 0x00020000
                FOFX_SHOWELEVATIONPROMPT = 0x00040000
                FOFX_RECYCLEONDELETE = 0x00080000
                FOFX_EARLYFAILURE = 0x00100000
                FOFX_PRESERVEFILEEXTENSIONS = 0x00200000
                FOFX_KEEPNEWERFILE = 0x00400000
                FOFX_NOCOPYHOOKS = 0x00800000
                FOFX_NOMINIMIZEBOX = 0x01000000
                FOFX_MOVEACLSACROSSVOLUMES = 0x02000000
                FOFX_DONTDISPLAYSOURCEPATH = 0x04000000
                FOFX_DONTDISPLAYDESTPATH = 0x08000000
                FOFX_REQUIREELEVATION = 0x10000000
                FOFX_ADDUNDORECORD = 0x20000000
                FOFX_COPYASDOWNLOAD = 0x40000000
                FOFX_DONTDISPLAYLOCATIONS = 0x80000000

                if not defined(__IFileOperation_INTERFACE_DEFINED__):
                    __IFileOperation_INTERFACE_DEFINED__ = 1

                    # interface IFileOperation

                    # [unique][object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        IFileOperation._methods_ = [
                            # 1) (Optional) Set up your event sink.
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Advise',
                                (
                                    ['in'],
                                    POINTER(IFileOperationProgressSink),
                                   'pfops'
                                ),
                                (['out'], POINTER(DWORD), 'pdwCookie'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'Unadvise',
                                (['in'], DWORD, 'dwCookie'),
                            ),

                            # 2) Set operation state
                            # FOF_ flags (defined in shellapi.h) and FOFX_
                            # flags are passed here
                            # if not specified the default flags are
                            # FOF_ALLOWUNDO | FOF_NOCONFIRMMKDIR                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetOperationFlags',
                                (['in'], DWORD, 'dwOperationFlags'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetProgressMessage',
                                (['in'], LPCWSTR, 'pszMessage'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetProgressDialog',
                                (
                                    ['in'],
                                    POINTER(IOperationsProgressDialog),
                                   'popd'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetProperties',
                                (
                                    ['in'],
                                    POINTER(IPropertyChangeArray),
                                   'pproparray'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetOwnerWindow',
                                (['in'], HWND, 'hwndOwner'),
                            ),

                            # 3) Specify operations to take on given items.
                            # FooItem takes an IShellItem*.
                            # FooItems takes an IShellItem*, an
                            # IEnumShellItems* or an IDataObject*.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'ApplyPropertiesToItem',
                                (['in'], POINTER(IShellItem), 'psiItem'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'ApplyPropertiesToItems',
                                (['in'], POINTER(IUnknown), 'punkItems'),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'RenameItem',
                                (['in'], POINTER(IShellItem), 'psiItem'),
                                (['in'], LPCWSTR, 'pszNewName'),
                                (
                                    ['unique', 'in'],
                                    POINTER(IFileOperationProgressSink),
                                   'pfopsItem'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'RenameItems',
                                (['in'], POINTER(IUnknown), 'pUnkItems'),
                                (['in'], LPCWSTR, 'pszNewName'),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'MoveItem',
                                (['in'], POINTER(IShellItem), 'psiItem'),
                                (
                                    [],
                                    POINTER(IShellItem),
                                   'psiDestinationFolder'
                                ),
                                (['unique', 'in'], LPCWSTR, 'pszNewName'),
                                (
                                    ['unique', 'in'],
                                    POINTER(IFileOperationProgressSink),
                                   'pfopsItem'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'MoveItems',
                                (['in'], POINTER(IUnknown), 'punkItems'),
                                (
                                    [],
                                    POINTER(IShellItem),
                                   'psiDestinationFolder'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'CopyItem',
                                (['in'], POINTER(IShellItem), 'psiItem'),
                                (
                                    [],
                                    POINTER(IShellItem),
                                   'psiDestinationFolder'
                                ),
                                (['unique', , 'in'], LPCWSTR, 'pszCopyName'),
                                (
                                    ['unique', 'in'],
                                    POINTER(IFileOperationProgressSink),
                                   'pfopsItem'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'CopyItems',
                                (['in'], POINTER(IUnknown), 'punkItems'),
                                (
                                    [],
                                    POINTER(IShellItem),
                                   'psiDestinationFolder'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'DeleteItem',
                                (['in'], POINTER(IShellItem), 'psiItem'),
                                (
                                    ['unique', 'in'],
                                    POINTER(IFileOperationProgressSink),
                                   'pfopsItem'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'DeleteItems',
                                (['in'], POINTER(IUnknown), 'punkItems'),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'NewItem',
                                (
                                    ['in'],
                                    POINTER(IShellItem),
                                   'psiDestinationFolder'
                                ),
                                ([], DWORD, 'dwFileAttributes'),
                                (['in'], LPCWSTR, 'pszName'),
                                (
                                    ['unique', 'in'],
                                    LPCWSTR,
                                   'pszTemplateName'
                                ),
                                (
                                    ['unique', 'in'],
                                    POINTER(IFileOperationProgressSink),
                                   'pfopsItem'
                                ),
                            ),

                            # 4) Perform operations.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'PerformOperations',
                            ),

                            # 5) Were any operations aborted?                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetAnyOperationsAborted',
                                (
                                    ['out'],
                                    POINTER(BOOL),
                                   'pfAnyOperationsAborted'
                                ),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __IFileOperation_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0085

                # [local]
                if (NTDDI_VERSION >= NTDDI_WIN10_RS4):
                    class FILE_OPERATION_FLAGS2(ENUM):
                        FOF2_NONE = 0
                        FOF2_MERGEFOLDERSONCOLLISION = 0x1


                    FOF2_NONE = FILE_OPERATION_FLAGS2.FOF2_NONE
                    FOF2_MERGEFOLDERSONCOLLISION = FILE_OPERATION_FLAGS2.FOF2_MERGEFOLDERSONCOLLISION
                    if not defined(__IFileOperation2_INTERFACE_DEFINED__):
                        __IFileOperation2_INTERFACE_DEFINED__ = 1

                        # interface IFileOperation2

                        # [unique][object][uuid]

                        if defined(__cplusplus) and not defined(CINTERFACE):
                            pass
                        else: # C style interface
                            IFileOperation2._methods_ = [
                            
                                COMMETHOD(
                                    [],
                                    HRESULT,
                                    'SetOperationFlags2',
                                    (
                                        ['in'],
                                        FILE_OPERATION_FLAGS2,
                                       'operationFlags2'
                                    ),
                                ),

                                #                            ]


                            # [annotation][iid_is][out]
                        # END IF  C style interface
                    # END IF  __IFileOperation2_INTERFACE_DEFINED__

                    # interface __MIDL_itf_shobjidl_core_0000_0086

                    # [local]
                # END IF   (NTDDI_VERSION >= NTDDI_WIN10_RS4)
                if not defined(__IObjectProvider_INTERFACE_DEFINED__):
                    __IObjectProvider_INTERFACE_DEFINED__ = 1

                    # interface IObjectProvider

                    # [unique][object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        IObjectProvider._methods_ = [

                            # IObjectProvider is similar to IServiceProvider
                            # except that it
                            # does not imply that unhandled/unknown requests
                            # should be forwarded,
                            # as IServiceProvider does. the object being
                            # queired for is identified
                            # by guidObject, usually named as OID_XXX                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'QueryObject',
                                (['in'], REFGUID, 'guidObject'),
                                ([], REFIID, 'riid'),
                                (['out'], POINTER(POINTER(VOID)), 'ppvOut'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __IObjectProvider_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0087

                # [local]
            # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
            if not defined(__INamespaceWalkCB_INTERFACE_DEFINED__):
                __INamespaceWalkCB_INTERFACE_DEFINED__ = 1

                # interface INamespaceWalkCB

                # [object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    INamespaceWalkCB._methods_ = [

                        # called for every non folder item found in the
                        # folder. these items are reported
                        # before any of the folders are returned via
                        # EnterFolder(). this is a bredth first
                        # walk of the name space                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'FoundItem',
                            (['in'], POINTER(IShellFolder), 'psf'),
                            ([], PCUITEMID_CHILD, 'pidl'),
                        ),

                        # this is called for ever sub folder found below the
                        # punkToWalk input
                        # it is not called for any folders specified directly
                        # in the input
                        # for every folder this is called after all of the
                        # items in the folder have
                        # been reported via FoundItem()
                        # return:
                        # S_OK to continue recursing
                        # S_FALSE to skip this folder but continue
                        # FAILED() (HRESULT_FROM_WIN32(ERROR_CANCELLED)) to
                        # stop the whole walk                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnterFolder',
                            (['in'], POINTER(IShellFolder), 'psf'),
                            ([], PCUITEMID_CHILD, 'pidl'),
                        ),

                        # matches the EnterFolder() calls, but since folders
                        # can nest this
                        # other folders may be entered and left before the
                        # matching call is made                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'LeaveFolder',
                            (['in'], POINTER(IShellFolder), 'psf'),
                            ([], PCUITEMID_CHILD, 'pidl'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'InitializeProgressDialog',
                            (['out', ], POINTER(LPWSTR), 'ppszTitle'),
                            ([], POINTER(LPWSTR), 'ppszCancel'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __INamespaceWalkCB_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0088

            # [local]
            if (_WIN32_IE >= _WIN32_IE_IE70):
                if not defined(__INamespaceWalkCB2_INTERFACE_DEFINED__):
                    __INamespaceWalkCB2_INTERFACE_DEFINED__ = 1

                    # interface INamespaceWalkCB2

                    # [object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        INamespaceWalkCB2._methods_ = [
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'WalkComplete',
                                (['in'], HRESULT, 'hr'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __INamespaceWalkCB2_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0089

                # [local]
            # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
            if not defined(__INamespaceWalk_INTERFACE_DEFINED__):
                __INamespaceWalk_INTERFACE_DEFINED__ = 1

                # interface INamespaceWalk

                # [object][uuid]


                class NAMESPACEWALKFLAG(ENUM):
                    NSWF_DEFAULT = 0
                    NSWF_NONE_IMPLIES_ALL = 0x1
                    NSWF_ONE_IMPLIES_ALL = 0x2
                    NSWF_DONT_TRAVERSE_LINKS = 0x4
                    NSWF_DONT_ACCUMULATE_RESULT = 0x8
                    NSWF_TRAVERSE_STREAM_JUNCTIONS = 0x10
                    NSWF_FILESYSTEM_ONLY = 0x20
                    NSWF_SHOW_PROGRESS = 0x40
                    NSWF_FLAG_VIEWORDER = 0x80
                    NSWF_IGNORE_AUTOPLAY_HIDA = 0x100
                    NSWF_ASYNC = 0x200
                    NSWF_DONT_RESOLVE_LINKS = 0x400
                    NSWF_ACCUMULATE_FOLDERS = 0x800
                    NSWF_DONT_SORT = 0x1000
                    NSWF_USE_TRANSFER_MEDIUM = 0x2000
                    NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS = 0x4000
                    NSWF_ANY_IMPLIES_ALL = 0x8000


                NSWF_DEFAULT = NAMESPACEWALKFLAG.NSWF_DEFAULT
                NSWF_NONE_IMPLIES_ALL = NAMESPACEWALKFLAG.NSWF_NONE_IMPLIES_ALL
                NSWF_ONE_IMPLIES_ALL = NAMESPACEWALKFLAG.NSWF_ONE_IMPLIES_ALL
                NSWF_DONT_TRAVERSE_LINKS = NAMESPACEWALKFLAG.NSWF_DONT_TRAVERSE_LINKS
                NSWF_DONT_ACCUMULATE_RESULT = NAMESPACEWALKFLAG.NSWF_DONT_ACCUMULATE_RESULT
                NSWF_TRAVERSE_STREAM_JUNCTIONS = NAMESPACEWALKFLAG.NSWF_TRAVERSE_STREAM_JUNCTIONS
                NSWF_FILESYSTEM_ONLY = NAMESPACEWALKFLAG.NSWF_FILESYSTEM_ONLY
                NSWF_SHOW_PROGRESS = NAMESPACEWALKFLAG.NSWF_SHOW_PROGRESS
                NSWF_FLAG_VIEWORDER = NAMESPACEWALKFLAG.NSWF_FLAG_VIEWORDER
                NSWF_IGNORE_AUTOPLAY_HIDA = NAMESPACEWALKFLAG.NSWF_IGNORE_AUTOPLAY_HIDA
                NSWF_ASYNC = NAMESPACEWALKFLAG.NSWF_ASYNC
                NSWF_DONT_RESOLVE_LINKS = NAMESPACEWALKFLAG.NSWF_DONT_RESOLVE_LINKS
                NSWF_ACCUMULATE_FOLDERS = NAMESPACEWALKFLAG.NSWF_ACCUMULATE_FOLDERS
                NSWF_DONT_SORT = NAMESPACEWALKFLAG.NSWF_DONT_SORT
                NSWF_USE_TRANSFER_MEDIUM = NAMESPACEWALKFLAG.NSWF_USE_TRANSFER_MEDIUM
                NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS = NAMESPACEWALKFLAG.NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS
                NSWF_ANY_IMPLIES_ALL = NAMESPACEWALKFLAG.NSWF_ANY_IMPLIES_ALL
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    INamespaceWalk._methods_ = [

                        # don't traverse the targets of link items
                        # (items with SFGAO_LINK) don't store the results of
                        # the walk, GetIDArrayResult() will fail if called for
                        # items with both SFGAO_FOLDER and SFGAO_STREAM
                        # discovered via the walk
                        # (as opposed to those passed as the input) for
                        # example .zip, .search - ms and .library - ms files
                        # traverse through them and find the items they
                        # reference. this will result in
                        # EnterFolder()/LeaveFolder() callbacks instead of
                        # FoundItem() only return file system items
                        # (SFGAO_FILESYSTEM) display the progress dialog while
                        # walking order the items based on the view order that
                        # might be different from the default sort run the
                        # walk on a background thread aVOID the expense of
                        # resolving links, means link targets might not be up
                        # to date Don't maintain sort order of items Use
                        # SHCONTF_STORAGE in enumerations for passed to the
                        # walk (as opposed to those discovered by walking),
                        # for do not traverse them, instead treat them as
                        # items. this will result in FoundItem() callbacks
                        # instead of EnterFolder()/LeaveFolder() For
                        # selections > 0
                        # punkToWalk can be  a punkSite that
                        # QueryService(SID_SFolderView, IFolderView) can
                        # discover IShellFolder IDataObject IParentAndItem
                        # (thus supports CLSID_ShellItem/IShellItem)
                        # IEnumFullIDList IShellItem IShellItemArray
                        # NAMESPACEWALKFLAG
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetIDArrayResult',
                            (['out'], POINTER(UINT), 'pcItems'),
                            (
                                ['out'],
                                POINTER(POINTER(PIDLIST_ABSOLUTE)),
                               'prgpidl'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __INamespaceWalk_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0090

            # [local]
        # END IF   NTDDI_WINXP or (_WIN32_IE >= _WIN32_IE_IE70)
        if defined(STRICT_TYPED_ITEMIDS) and defined(__cplusplus):
            pass
    else: #   defined(STRICT_TYPED_ITEMIDS) and defined(__cplusplus)
            FreeIDListArrayFull = FreeIDListArray
            FreeIDListArrayChild = FreeIDListArray
        # END IF    defined(STRICT_TYPED_ITEMIDS) and defined(__cplusplus)
        class tagBANDSITEINFO(ctypes.Structure):
            pass
        tagBANDSITEINFO._fields_ = [
            ('dwMask', DWORD),
            ('dwState', DWORD),
            ('dwStyle', DWORD),
        ]


        BANDSITEINFO = tagBANDSITEINFO




        class tagBANDSITECID(ENUM):
            BSID_BANDADDED = 0
            #~#~#~ BSID_BANDREMOVED    = ( BSID_BANDADDED + 1 )


        BSID_BANDADDED = tagBANDSITECID.BSID_BANDADDED
        BSIM_STATE = 0x00000001
        BSIM_STYLE = 0x00000002
        BSSF_VISIBLE = 0x00000001
        BSSF_NOTITLE = 0x00000002
        BSSF_UNDELETEABLE = 0x00001000
        BSIS_AUTOGRIPPER = 0x00000000
        BSIS_NOGRIPPER = 0x00000001
        BSIS_ALWAYSGRIPPER = 0x00000002
        BSIS_LEFTALIGN = 0x00000004
        BSIS_SINGLECLICK = 0x00000008
        BSIS_NOCONTEXTMENU = 0x00000010
        BSIS_NODROPTARGET = 0x00000020
        BSIS_NOCAPTION = 0x00000040
        BSIS_PREFERNOLINEBREAK = 0x00000080
        BSIS_LOCKED = 0x00000100

        if (_WIN32_IE >= _WIN32_IE_IE70):
            BSIS_PRESERVEORDERDURINGLAYOUT = 0x00000200
            BSIS_FIXEDORDER = 0x00000400
        # END IF   _WIN32_IE_IE70
        SID_SBandSite = IID_IBandSite
        CGID_BandSite = IID_IBandSite

        if not defined(__IBandSite_INTERFACE_DEFINED__):
            __IBandSite_INTERFACE_DEFINED__ = 1

            # interface IBandSite

            # [uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][out]

                # [annotation][out]

                # [annotation][size_is][string][out]

                # [annotation][in]
            else: # C style interface
                IBandSite._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'AddBand',
                        (['in'], POINTER(IUnknown), 'punk'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnumBands',
                        (['in'], UINT, 'uBand'),
                        (['out'], POINTER(DWORD), 'pdwBandID'),
                    ),

                    #                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'QueryBand',
                        ([annotation('_In_'), 'in'], DWORD, 'dwBandID'),
                        (
                            [annotation('_Outptr_opt_'), 'out'],
                            POINTER(POINTER(IDeskBand)),
                           'ppstb'
                        ),
                        (
                            ['out', annotation('_Out_opt_')],
                            POINTER(DWORD),
                           'pdwState'
                        ),
                        (
                            [annotation('_Out_writes_opt_(cchName)), , 'out'],
                            LPWSTR,
                           'pszName'
                        ),
                        ([], INT, 'cchName'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoteQueryBand',
                        (['in'], DWORD, 'dwBandID'),
                        (['out'], POINTER(POINTER(IDeskBand)), 'ppstb'),
                        ([], POINTER(DWORD), 'pdwState'),
                        (['out'], LPWSTR, 'pszName'),
                        ([], INT, 'cchName'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetBandState',
                        (['in'], DWORD, 'dwBandID'),
                        ([], DWORD, 'dwMask'),
                        ([], DWORD, 'dwState'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveBand',
                        (['in'], DWORD, 'dwBandID'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetBandObject',
                        (['in'], DWORD, 'dwBandID'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetBandSiteInfo',
                        (['in'], POINTER(BANDSITEINFO), 'pbsinfo'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetBandSiteInfo',
                        (['out', 'in'], POINTER(BANDSITEINFO), 'pbsinfo'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][out]

                # [annotation][out]

                # [annotation][size_is][string][out]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IBandSite_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0091

        # [local]
        if (NTDDI_VERSION >= NTDDI_WINXP):
            if not defined(__IModalWindow_INTERFACE_DEFINED__):
                __IModalWindow_INTERFACE_DEFINED__ = 1

                # interface IModalWindow

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][unique][in]
                else: # C style interface
                    IModalWindow._methods_ = [
                    
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'Show',
                            (
                                [annotation('_In_opt_'), 'unique', 'in'],
                                HWND,
                               'hwndOwner'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteShow',
                            (['unique', 'in'], HWND, 'hwndOwner'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]
                # END IF  C style interface
            # END IF  __IModalWindow_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0092

            # [local]
        # END IF   NTDDI_WINXP
        if not defined(__IContextMenuSite_INTERFACE_DEFINED__):
            __IContextMenuSite_INTERFACE_DEFINED__ = 1

            # interface IContextMenuSite

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IContextMenuSite._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'DoContextMenuPopup',
                        (['in'], POINTER(IUnknown), 'punkContextMenu'),
                        ([], UINT, 'fFlags'),
                        ([], POINT, 'pt'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IContextMenuSite_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0093

        # [local]
        if (NTDDI_VERSION >= NTDDI_WINXP) or (_WIN32_IE >= _WIN32_IE_IE70):
            if (NTDDI_VERSION >= NTDDI_WINXP):
                if not defined(__IMenuBand_INTERFACE_DEFINED__):
                    __IMenuBand_INTERFACE_DEFINED__ = 1

                    # interface IMenuBand

                    # [local][unique][object][uuid]


                    class tagMENUBANDHANDLERCID(ENUM):
                        MBHANDCID_PIDLSELECT = 0


                    MBHANDCID_PIDLSELECT = tagMENUBANDHANDLERCID.MBHANDCID_PIDLSELECT
                    if defined(__cplusplus) and not defined(CINTERFACE):

                        # [annotation][in]

                        # [annotation][out][in]

                        # [annotation][out]
                    else: # C style interface
                        IMenuBand._methods_ = [

                            # CmdIDs for the IOleCommandTarget Group:
                            # CGID_MenuBandHandler (defined in shguidp.h)
                            # A PIDL from a menuband was selected                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'IsMenuMessage',
                                (
                                    [annotation('_In_'), 'in'],
                                    POINTER(MSG),
                                   'pmsg'
                                ),
                            ),

                            #                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'TranslateMenuMessage',
                                (
                                    ['out', annotation('_Inout_'), 'in'],
                                    POINTER(MSG),
                                   'pmsg'
                                ),
                                (
                                    [annotation('_Out_'), 'out'],
                                    POINTER(LRESULT),
                                   'plRet'
                                ),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]

                        # [annotation][in]

                        # [annotation][out][in]

                        # [annotation][out]
                    # END IF  C style interface
                # END IF  __IMenuBand_INTERFACE_DEFINED__
                if not defined(__IRegTreeItem_INTERFACE_DEFINED__):
                    __IRegTreeItem_INTERFACE_DEFINED__ = 1

                    # interface IRegTreeItem

                    # [object][local][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):

                        # [annotation][out]

                        # [annotation][in]
                    else: # C style interface
                        IRegTreeItem._methods_ = [
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetCheckState',
                                (
                                    [annotation('_Out_'), 'out'],
                                    POINTER(BOOL),
                                   'pbCheck'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetCheckState',
                                ([annotation('_In_'), 'in'], BOOL, 'bCheck'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]

                        # [annotation][out]

                        # [annotation][in]
                    # END IF  C style interface
                # END IF  __IRegTreeItem_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0095

                # [local]
            # END IF   NTDDI_WINXP
        # END IF   NTDDI_WINXP) or (_WIN32_IE >= _WIN32_IE_IE70)
        if (_WIN32_IE >= _WIN32_IE_IE60):
            if not defined(__IDeskBar_INTERFACE_DEFINED__):
                __IDeskBar_INTERFACE_DEFINED__ = 1

                # interface IDeskBar

                # [local][unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][unique][in]

                    # [annotation][out]

                    # [annotation][in]
                else: # C style interface
                    IDeskBar._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetClient',
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                POINTER(IUnknown),
                               'punkClient'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetClient',
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(IUnknown)),
                               'ppunkClient'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnPosRectChangeDB',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(RECT),
                               'prc'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]

                    # [annotation][out]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IDeskBar_INTERFACE_DEFINED__
            if not defined(__IMenuPopup_INTERFACE_DEFINED__):
                __IMenuPopup_INTERFACE_DEFINED__ = 1

                # interface IMenuPopup

                # [local][unique][object][uuid]


                class tagMENUPOPUPSELECT(ENUM):
                    MPOS_EXECUTE = 0
                    #~#~#~ MPOS_FULLCANCEL    = ( MPOS_EXECUTE + 1 )
                    #~#~#~ MPOS_CANCELLEVEL    = ( MPOS_FULLCANCEL + 1 )
                    #~#~#~ MPOS_SELECTLEFT    = ( MPOS_CANCELLEVEL + 1 )
                    #~#~#~ MPOS_SELECTRIGHT    = ( MPOS_SELECTLEFT + 1 )
                    #~#~#~ MPOS_CHILDTRACKING    = ( MPOS_SELECTRIGHT + 1 )


                MPOS_EXECUTE = tagMENUPOPUPSELECT.MPOS_EXECUTE
                class tagMENUPOPUPPOPUPFLAGS(ENUM):
                    MPPF_SETFOCUS = 0x1
                    MPPF_INITIALSELECT = 0x2
                    MPPF_NOANIMATE = 0x4
                    MPPF_KEYBOARD = 0x10
                    MPPF_REPOSITION = 0x20
                    MPPF_FORCEZORDER = 0x40
                    MPPF_FINALSELECT = 0x80
                    MPPF_TOP = 0x20000000
                    MPPF_LEFT = 0x40000000
                    MPPF_RIGHT = 0x60000000
                    #~#~#~ MPPF_BOTTOM    = ( INT  )0x80000000
                    #~#~#~ MPPF_POS_MASK    = ( INT  )0xe0000000
                    MPPF_ALIGN_LEFT = 0x2000000
                    MPPF_ALIGN_RIGHT = 0x4000000


                MPPF_SETFOCUS = tagMENUPOPUPPOPUPFLAGS.MPPF_SETFOCUS
                MPPF_INITIALSELECT = tagMENUPOPUPPOPUPFLAGS.MPPF_INITIALSELECT
                MPPF_NOANIMATE = tagMENUPOPUPPOPUPFLAGS.MPPF_NOANIMATE
                MPPF_KEYBOARD = tagMENUPOPUPPOPUPFLAGS.MPPF_KEYBOARD
                MPPF_REPOSITION = tagMENUPOPUPPOPUPFLAGS.MPPF_REPOSITION
                MPPF_FORCEZORDER = tagMENUPOPUPPOPUPFLAGS.MPPF_FORCEZORDER
                MPPF_FINALSELECT = tagMENUPOPUPPOPUPFLAGS.MPPF_FINALSELECT
                MPPF_TOP = tagMENUPOPUPPOPUPFLAGS.MPPF_TOP
                MPPF_LEFT = tagMENUPOPUPPOPUPFLAGS.MPPF_LEFT
                MPPF_RIGHT = tagMENUPOPUPPOPUPFLAGS.MPPF_RIGHT
                MPPF_ALIGN_LEFT = tagMENUPOPUPPOPUPFLAGS.MPPF_ALIGN_LEFT
                MPPF_ALIGN_RIGHT = tagMENUPOPUPPOPUPFLAGS.MPPF_ALIGN_RIGHT
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                else: # C style interface
                    IMenuPopup._methods_ = [
                        # Type values for IMenuPopup::OnSelect

                        # Execute the selected menu item Cancel the entire
                        # menu Cancel the current cascaded menu select one to
                        # the left of the cur selection select one to the
                        # right of the cur selection the child got a tracking
                        # select (mouse moved over)
                        # Flags for IMenuPopup::Popup
                        # Menu can take the focus Select the first item Do not
                        # animate this show The menu is activated by keyboard
                        # Resposition the displayed bar. internal: Tells
                        # menubar to ignore Submenu positions Select the last
                        # item Popup menu up from point Popup menu left from
                        # point Popup menu right from point Popup menu below
                        # point Menu Position Mask Default alignment Popup
                        # menu aligned to right of exclude rect
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Popup',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(POINTL),
                               'ppt'
                            ),
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                POINTER(RECTL),
                               'prcExclude'
                            ),
                            ([], MP_POPUPFLAGS, 'dwFlags'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnSelect',
                            (
                                [annotation('_In_'), 'in'],
                                DWORD,
                               'dwSelectType'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSubMenu',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IMenuPopup),
                               'pmp'
                            ),
                            ([], BOOL, 'fSet'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IMenuPopup_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0097

            # [local]
        # END IF   _WIN32_IE_IE60
        if (NTDDI_VERSION >= NTDDI_VISTA):
            class FILE_USAGE_TYPE(ENUM):
                FUT_PLAYING = 0
                #~#~#~ FUT_EDITING    = ( FUT_PLAYING + 1 )
                #~#~#~ FUT_GENERIC    = ( FUT_EDITING + 1 )


            FUT_PLAYING = FILE_USAGE_TYPE.FUT_PLAYING
            OF_CAP_CANSWITCHTO = 0x0001
            OF_CAP_CANCLOSE = 0x0002

            if not defined(__IFileIsInUse_INTERFACE_DEFINED__):
                __IFileIsInUse_INTERFACE_DEFINED__ = 1

                # interface IFileIsInUse

                # [object][unique][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFileIsInUse._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetAppName',
                            (['out'], POINTER(LPWSTR), 'ppszName'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetUsage',
                            (['out'], POINTER(FILE_USAGE_TYPE), 'pfut'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetCapabilities',
                            (['out'], POINTER(DWORD), 'pdwCapFlags'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSwitchToHWND',
                            (['out'], POINTER(HWND), 'phwnd'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'CloseFile',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IFileIsInUse_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0098

            # [local]
            class FDE_OVERWRITE_RESPONSE(ENUM):
                FDEOR_DEFAULT = 0
                FDEOR_ACCEPT = 1
                FDEOR_REFUSE = 2


            FDEOR_DEFAULT = FDE_OVERWRITE_RESPONSE.FDEOR_DEFAULT
            FDEOR_ACCEPT = FDE_OVERWRITE_RESPONSE.FDEOR_ACCEPT
            FDEOR_REFUSE = FDE_OVERWRITE_RESPONSE.FDEOR_REFUSE
            class FDE_SHAREVIOLATION_RESPONSE(ENUM):
                FDESVR_DEFAULT = 0
                FDESVR_ACCEPT = 1
                FDESVR_REFUSE = 2


            FDESVR_DEFAULT = FDE_SHAREVIOLATION_RESPONSE.FDESVR_DEFAULT
            FDESVR_ACCEPT = FDE_SHAREVIOLATION_RESPONSE.FDESVR_ACCEPT
            FDESVR_REFUSE = FDE_SHAREVIOLATION_RESPONSE.FDESVR_REFUSE
            class FDAP(ENUM):
                FDAP_BOTTOM = 0
                FDAP_TOP = 1


            FDAP_BOTTOM = FDAP.FDAP_BOTTOM
            FDAP_TOP = FDAP.FDAP_TOP
            if not defined(__IFileDialogEvents_INTERFACE_DEFINED__):
                __IFileDialogEvents_INTERFACE_DEFINED__ = 1

                # interface IFileDialogEvents

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFileDialogEvents._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnFileOk',
                            (['in'], POINTER(IFileDialog), 'pfd'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnFolderChanging',
                            (['in'], POINTER(IFileDialog), 'pfd'),
                            ([], POINTER(IShellItem), 'psiFolder'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnFolderChange',
                            (['in'], POINTER(IFileDialog), 'pfd'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnSelectionChange',
                            (['in'], POINTER(IFileDialog), 'pfd'),
                        ),

                        # Note: FOS_SHAREAWARE must be set in
                        # IFileDialog::SetOptions in order for this method to
                        # be called.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnShareViolation',
                            (['in'], POINTER(IFileDialog), 'pfd'),
                            ([], POINTER(IShellItem), 'psi'),
                            (
                                ['out'],
                                POINTER(FDE_SHAREVIOLATION_RESPONSE),
                               'pResponse'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnTypeChange',
                            (['in'], POINTER(IFileDialog), 'pfd'),
                        ),

                        # Note: FOS_OVERWRITEPROMPT must be set in
                        # IFileDialog::SetOptions in order for this method to
                        # be called.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnOverwrite',
                            (['in'], POINTER(IFileDialog), 'pfd'),
                            ([], POINTER(IShellItem), 'psi'),
                            (
                                ['out'],
                                POINTER(FDE_OVERWRITE_RESPONSE),
                               'pResponse'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IFileDialogEvents_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0099

            # [local]
            if not defined(__IFileDialog_INTERFACE_DEFINED__):
                __IFileDialog_INTERFACE_DEFINED__ = 1

                # interface IFileDialog

                # [unique][object][uuid]

                # [v1_enum]


                class _FILEOPENDIALOGOPTIONS(ENUM):
                    FOS_OVERWRITEPROMPT = 0x2
                    FOS_STRICTFILETYPES = 0x4
                    FOS_NOCHANGEDIR = 0x8
                    FOS_PICKFOLDERS = 0x20
                    FOS_FORCEFILESYSTEM = 0x40
                    FOS_ALLNONSTORAGEITEMS = 0x80
                    FOS_NOVALIDATE = 0x100
                    FOS_ALLOWMULTISELECT = 0x200
                    FOS_PATHMUSTEXIST = 0x800
                    FOS_FILEMUSTEXIST = 0x1000
                    FOS_CREATEPROMPT = 0x2000
                    FOS_SHAREAWARE = 0x4000
                    FOS_NOREADONLYRETURN = 0x8000
                    FOS_NOTESTFILECREATE = 0x10000
                    FOS_HIDEMRUPLACES = 0x20000
                    FOS_HIDEPINNEDPLACES = 0x40000
                    FOS_NODEREFERENCELINKS = 0x100000
                    FOS_OKBUTTONNEEDSINTERACTION = 0x200000
                    FOS_DONTADDTORECENT = 0x2000000
                    FOS_FORCESHOWHIDDEN = 0x10000000
                    FOS_DEFAULTNOMINIMODE = 0x20000000
                    FOS_FORCEPREVIEWPANEON = 0x40000000
                    FOS_SUPPORTSTREAMABLEITEMS = 0x80000000


                FOS_OVERWRITEPROMPT = _FILEOPENDIALOGOPTIONS.FOS_OVERWRITEPROMPT
                FOS_STRICTFILETYPES = _FILEOPENDIALOGOPTIONS.FOS_STRICTFILETYPES
                FOS_NOCHANGEDIR = _FILEOPENDIALOGOPTIONS.FOS_NOCHANGEDIR
                FOS_PICKFOLDERS = _FILEOPENDIALOGOPTIONS.FOS_PICKFOLDERS
                FOS_FORCEFILESYSTEM = _FILEOPENDIALOGOPTIONS.FOS_FORCEFILESYSTEM
                FOS_ALLNONSTORAGEITEMS = _FILEOPENDIALOGOPTIONS.FOS_ALLNONSTORAGEITEMS
                FOS_NOVALIDATE = _FILEOPENDIALOGOPTIONS.FOS_NOVALIDATE
                FOS_ALLOWMULTISELECT = _FILEOPENDIALOGOPTIONS.FOS_ALLOWMULTISELECT
                FOS_PATHMUSTEXIST = _FILEOPENDIALOGOPTIONS.FOS_PATHMUSTEXIST
                FOS_FILEMUSTEXIST = _FILEOPENDIALOGOPTIONS.FOS_FILEMUSTEXIST
                FOS_CREATEPROMPT = _FILEOPENDIALOGOPTIONS.FOS_CREATEPROMPT
                FOS_SHAREAWARE = _FILEOPENDIALOGOPTIONS.FOS_SHAREAWARE
                FOS_NOREADONLYRETURN = _FILEOPENDIALOGOPTIONS.FOS_NOREADONLYRETURN
                FOS_NOTESTFILECREATE = _FILEOPENDIALOGOPTIONS.FOS_NOTESTFILECREATE
                FOS_HIDEMRUPLACES = _FILEOPENDIALOGOPTIONS.FOS_HIDEMRUPLACES
                FOS_HIDEPINNEDPLACES = _FILEOPENDIALOGOPTIONS.FOS_HIDEPINNEDPLACES
                FOS_NODEREFERENCELINKS = _FILEOPENDIALOGOPTIONS.FOS_NODEREFERENCELINKS
                FOS_OKBUTTONNEEDSINTERACTION = _FILEOPENDIALOGOPTIONS.FOS_OKBUTTONNEEDSINTERACTION
                FOS_DONTADDTORECENT = _FILEOPENDIALOGOPTIONS.FOS_DONTADDTORECENT
                FOS_FORCESHOWHIDDEN = _FILEOPENDIALOGOPTIONS.FOS_FORCESHOWHIDDEN
                FOS_DEFAULTNOMINIMODE = _FILEOPENDIALOGOPTIONS.FOS_DEFAULTNOMINIMODE
                FOS_FORCEPREVIEWPANEON = _FILEOPENDIALOGOPTIONS.FOS_FORCEPREVIEWPANEON
                FOS_SUPPORTSTREAMABLEITEMS = _FILEOPENDIALOGOPTIONS.FOS_SUPPORTSTREAMABLEITEMS
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFileDialog._methods_ = [

                        # (on by default in the save dialog) In the save
                        # dialog, only allow the user to choose a file that
                        # has one of the file extensions provided in
                        # SetFileTypes. Don't change the current working
                        # directory Invoke the open dialog in folder picking
                        # mode. Ensure that items returned are filesystem
                        # items. Allow choosing items that have no storage.
                        # (on by default)
                        # (on by default in the open dialog and folder picker)
                        # (on by default in the save dialog) AVOID testing the
                        # creation of the chosen file in the save dialog
                        # (specifying this flag will circumvent some useful error handling, such as access denied) (not used in Win7) Don't display the standard namespace locations in the navigation pane. (generally used aLONG with AddPlace) Don't treat SHORTcuts as their target files. Only enable the OK button if the user has done something in the view. Don't add the chosen file to the recent documents list (SHAddToRecentDocs) Show all files including system and hidden files. (not used in Win7) Indicates the caller will use BHID_Stream to open contents, no need to download the file
                        # 
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFileTypes',
                            (['in'], UINT, 'cFileTypes'),
                            (
                                ['in'],
                                POINTER(COMDLG_FILTERSPEC),
                               'rgFilterSpec'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFileTypeIndex',
                            (['in'], UINT, 'iFileType'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFileTypeIndex',
                            (['out'], POINTER(UINT), 'piFileType'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Advise',
                            (['in'], POINTER(IFileDialogEvents), 'pfde'),
                            (['out'], POINTER(DWORD), 'pdwCookie'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Unadvise',
                            (['in'], DWORD, 'dwCookie'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetOptions',
                            (['in'], FILEOPENDIALOGOPTIONS, 'fos'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetOptions',
                            (['out'], POINTER(FILEOPENDIALOGOPTIONS), 'pfos'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetDefaultFolder',
                            (['in'], POINTER(IShellItem), 'psi'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFolder',
                            (['in'], POINTER(IShellItem), 'psi'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFolder',
                            (['out'], POINTER(POINTER(IShellItem)), 'ppsi'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetCurrentSelection',
                            (['out'], POINTER(POINTER(IShellItem)), 'ppsi'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFileName',
                            (['in'], LPCWSTR, 'pszName'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFileName',
                            (['out'], POINTER(LPWSTR), 'pszName'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetTitle',
                            (['in'], LPCWSTR, 'pszTitle'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetOkButtonLabel',
                            (['in'], LPCWSTR, 'pszText'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFileNameLabel',
                            (['in'], LPCWSTR, 'pszLabel'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetResult',
                            (['out'], POINTER(POINTER(IShellItem)), 'ppsi'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddPlace',
                            (['in'], POINTER(IShellItem), 'psi'),
                            ([], FDAP, 'fdap'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetDefaultExtension',
                            (['in'], LPCWSTR, 'pszDefaultExtension'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Close',
                            (['in'], HRESULT, 'hr'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetClientGuid',
                            (['in'], REFGUID, 'guid'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ClearClientData',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFilter',
                            (['in'], POINTER(IShellItemFilter), 'pFilter'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]
                # END IF  C style interface
            # END IF  __IFileDialog_INTERFACE_DEFINED__
            if not defined(__IFileSaveDialog_INTERFACE_DEFINED__):
                __IFileSaveDialog_INTERFACE_DEFINED__ = 1

                # interface IFileSaveDialog

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFileSaveDialog._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSaveAsItem',
                            (['in'], POINTER(IShellItem), 'psi'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetProperties',
                            (['in'], POINTER(IPropertyStore), 'pStore'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetCollectedProperties',
                            (
                                ['in'],
                                POINTER(IPropertyDescriptionList),
                               'pList'
                            ),
                            ([], BOOL, 'fAppendDefault'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetProperties',
                            (
                                ['out'],
                                POINTER(POINTER(IPropertyStore)),
                               'ppStore'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ApplyProperties',
                            (['in'], POINTER(IShellItem), 'psi'),
                            ([], POINTER(IPropertyStore), 'pStore'),
                            (['unique', 'in'], HWND, 'hwnd'),
                            (
                                [],
                                POINTER(IFileOperationProgressSink),
                               'pSink'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]
                # END IF  C style interface
            # END IF  __IFileSaveDialog_INTERFACE_DEFINED__
            if not defined(__IFileOpenDialog_INTERFACE_DEFINED__):
                __IFileOpenDialog_INTERFACE_DEFINED__ = 1

                # interface IFileOpenDialog

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFileOpenDialog._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetResults',
                            (
                                ['out'],
                                POINTER(POINTER(IShellItemArray)),
                               'ppenum'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSelectedItems',
                            (
                                ['out'],
                                POINTER(POINTER(IShellItemArray)),
                               'ppsai'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]
                # END IF  C style interface
            # END IF  __IFileOpenDialog_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0102

            # [local]
            class CDCONTROLSTATEF(ENUM):
                CDCS_INACTIVE = 0
                CDCS_ENABLED = 0x1
                CDCS_VISIBLE = 0x2
                CDCS_ENABLEDVISIBLE = 0x3


            CDCS_INACTIVE = CDCONTROLSTATEF.CDCS_INACTIVE
            CDCS_ENABLED = CDCONTROLSTATEF.CDCS_ENABLED
            CDCS_VISIBLE = CDCONTROLSTATEF.CDCS_VISIBLE
            CDCS_ENABLEDVISIBLE = CDCONTROLSTATEF.CDCS_ENABLEDVISIBLE
            if not defined(__IFileDialogCustomize_INTERFACE_DEFINED__):
                __IFileDialogCustomize_INTERFACE_DEFINED__ = 1

                # interface IFileDialogCustomize

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFileDialogCustomize._methods_ = [

                        # Methods for adding or enabling controls. All of
                        # these can have their
                        # enabled/visible state set, however the default is
                        # for them to be enabled and visible,
                        # so this parameter has been left off these methods.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnableOpenDropDown',
                            (['in'], DWORD, 'dwIDCtl'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddMenu',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszLabel'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddPushButton',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszLabel'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddComboBox',
                            (['in'], DWORD, 'dwIDCtl'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddRadioButtonList',
                            (['in'], DWORD, 'dwIDCtl'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddCheckButton',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszLabel'),
                            ([], BOOL, 'bChecked'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddEditBox',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszText'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddSeparator',
                            (['in'], DWORD, 'dwIDCtl'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddText',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszText'),
                        ),

                        # Getting/setting attributes on controls on the fly
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetControlLabel',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszLabel'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetControlState',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['out'], POINTER(CDCONTROLSTATEF), 'pdwState'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetControlState',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], CDCONTROLSTATEF, 'dwState'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetEditBoxText',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['out', ], POINTER(POINTER(WCHAR)), 'ppszText'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetEditBoxText',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszText'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetCheckButtonState',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['out'], POINTER(BOOL), 'pbChecked'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetCheckButtonState',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], BOOL, 'bChecked'),
                        ),

                        # Method for adding items to "container controls"
                        # (radiogroup, combobox, opendropdown, toolsmenu)
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddControlItem',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], DWORD, 'dwIDItem'),
                            ([], LPCWSTR, 'pszLabel'),
                        ),

                        # Methods for removing items in the
                        # "container controls"
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoveControlItem',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], DWORD, 'dwIDItem'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoveAllControlItems',
                            (['in'], DWORD, 'dwIDCtl'),
                        ),

                        # Getting/setting attributes on control items on the
                        # fly
                        # Items are considered immutable once created, except
                        # for their state:
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetControlItemState',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], DWORD, 'dwIDItem'),
                            (['out'], POINTER(CDCONTROLSTATEF), 'pdwState'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetControlItemState',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], DWORD, 'dwIDItem'),
                            ([], CDCONTROLSTATEF, 'dwState'),
                        ),

                        # Methods for some "container controls": OpenDropDown,
                        # combobox, radiobuttongroup.
                        # These methods don't apply to the tools menu.
                        # These methods can be called after the dialog has
                        # closed, to determine the users final choice.
                        # For comboboxes and radiobuttongroups, these methods
                        # may also be called while the
                        # dialog is showing
                        # (which makes no sense for the OpenDropDown).
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSelectedControlItem',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['out'], POINTER(DWORD), 'pdwIDItem'),
                        ),

                        # Not valid for OpenDropDown                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSelectedControlItem',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], DWORD, 'dwIDItem'),
                        ),

                        # Controls can be grouped by wrapping their adds in
                        # StartVisualGroup/EndVisualGroup
                        # Groups have control IDs, and can be disabled/hidden,
                        # just like other controls.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'StartVisualGroup',
                            (['in'], DWORD, 'dwIDCtl'),
                            (['in'], LPCWSTR, 'pszLabel'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EndVisualGroup',
                        ),

                        # One control may be marked as appearing prominently
                        # in the UI                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'MakeProminent',
                            (['in'], DWORD, 'dwIDCtl'),
                        ),

                        # Set the text of a control item
                        # (RadioButton, or item in an OpenDropDown or Menu)
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetControlItemText',
                            (['in'], DWORD, 'dwIDCtl'),
                            ([], DWORD, 'dwIDItem'),
                            (['in'], LPCWSTR, 'pszLabel'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IFileDialogCustomize_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0103

            # [local]
            class ASSOCIATIONLEVEL(ENUM):
                AL_MACHINE = 0
                #~#~#~ AL_EFFECTIVE    = ( AL_MACHINE + 1 )
                #~#~#~ AL_USER    = ( AL_EFFECTIVE + 1 )


            AL_MACHINE = ASSOCIATIONLEVEL.AL_MACHINE
            class ASSOCIATIONTYPE(ENUM):
                AT_FILEEXTENSION = 0
                #~#~#~ AT_URLPROTOCOL    = ( AT_FILEEXTENSION + 1 )
                #~#~#~ AT_STARTMENUCLIENT    = ( AT_URLPROTOCOL + 1 )
                #~#~#~ AT_MIMETYPE    = ( AT_STARTMENUCLIENT + 1 )


            AT_FILEEXTENSION = ASSOCIATIONTYPE.AT_FILEEXTENSION
            if not defined(__IApplicationAssociationRegistration_INTERFACE_DEFINED__):
                __IApplicationAssociationRegistration_INTERFACE_DEFINED__ = 1

                # interface IApplicationAssociationRegistration

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IApplicationAssociationRegistration._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'QueryCurrentDefault',
                            (['in'], LPCWSTR, 'pszQuery'),
                            (['in'], ASSOCIATIONTYPE, 'atQueryType'),
                            ([], ASSOCIATIONLEVEL, 'alQueryLevel'),
                            (['out', ], POINTER(LPWSTR), 'ppszAssociation'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'QueryAppIsDefault',
                            (['in'], LPCWSTR, 'pszQuery'),
                            (['in'], ASSOCIATIONTYPE, 'atQueryType'),
                            ([], ASSOCIATIONLEVEL, 'alQueryLevel'),
                            ([], LPCWSTR, 'pszAppRegistryName'),
                            (['out'], POINTER(BOOL), 'pfDefault'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'QueryAppIsDefaultAll',
                            (['in'], ASSOCIATIONLEVEL, 'alQueryLevel'),
                            (['in'], LPCWSTR, 'pszAppRegistryName'),
                            (['out'], POINTER(BOOL), 'pfDefault'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetAppAsDefault',
                            (['in'], LPCWSTR, 'pszAppRegistryName'),
                            ([], LPCWSTR, 'pszSet'),
                            (['in'], ASSOCIATIONTYPE, 'atSetType'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetAppAsDefaultAll',
                            (['in'], LPCWSTR, 'pszAppRegistryName'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ClearUserAssociations',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IApplicationAssociationRegistration_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0104

            # [local]
        # END IF   NTDDI_VISTA
        class DELEGATEITEMID(ctypes.Structure):
            pass
        DELEGATEITEMID._fields_ = [
            ('cbSize', WORD),
            ('wOuter', WORD),
            ('cbInner', WORD),
            ('rgb', BYTE * 1),
        ]


        if not defined(__IDelegateFolder_INTERFACE_DEFINED__):
            __IDelegateFolder_INTERFACE_DEFINED__ = 1

            # interface IDelegateFolder

            # [unique][local][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]
            else: # C style interface
                IDelegateFolder._methods_ = [

                    # use to give the delegate folder the IMalloc interface
                    # that it
                    # needs to use to alloc and free item IDs.
                    # These IDs are in the form of DELEGATEITEMIDs
                    # and it is the delegates job to pack its data into the
                    # pidl
                    # in the delegate format                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetItemAlloc',
                        (
                            [annotation('_In_'), 'in'],
                            POINTER(IMalloc),
                           'pmalloc'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IDelegateFolder_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0105

        # [local]
        if (_WIN32_IE >= _WIN32_IE_IE60):

            # INTERFACE: IBrowserFrameOptions

            # This interface was implemented so a browser or host can ask a
            # ShellView/ShelNameSpace what

            # kind of 'Behavior' is appropriate for that view.

            # IBrowserFrameOptions::GetBrowserOptions()

            # dwMask is the logical OR of bits to look for. pdwOptions is not
            # optional and

            # it's return value will always equal or will be a subset of
            # dwMask.

            # If the function succeeds, the return value must be S_OK and
            # pdwOptions needs to be filled in.

            # If the function fails, pdwOptions needs to be filled in with
            # BFO_NONE.
            if not defined(__IBrowserFrameOptions_INTERFACE_DEFINED__):
                __IBrowserFrameOptions_INTERFACE_DEFINED__ = 1

                # interface IBrowserFrameOptions

                # [local][object][uuid]

                # [v1_enum]


                class _BROWSERFRAMEOPTIONS(ENUM):
                    BFO_NONE = 0
                    BFO_BROWSER_PERSIST_SETTINGS = 0x1
                    BFO_RENAME_FOLDER_OPTIONS_TOINTERNET = 0x2
                    BFO_BOTH_OPTIONS = 0x4
                    BIF_PREFER_INTERNET_SHORTCUT = 0x8
                    BFO_BROWSE_NO_IN_NEW_PROCESS = 0x10
                    BFO_ENABLE_HYPERLINK_TRACKING = 0x20
                    BFO_USE_IE_OFFLINE_SUPPORT = 0x40
                    BFO_SUBSTITUE_INTERNET_START_PAGE = 0x80
                    BFO_USE_IE_LOGOBANDING = 0x100
                    BFO_ADD_IE_TOCAPTIONBAR = 0x200
                    BFO_USE_DIALUP_REF = 0x400
                    BFO_USE_IE_TOOLBAR = 0x800
                    BFO_NO_PARENT_FOLDER_SUPPORT = 0x1000
                    BFO_NO_REOPEN_NEXT_RESTART = 0x2000
                    BFO_GO_HOME_PAGE = 0x4000
                    BFO_PREFER_IEPROCESS = 0x8000
                    BFO_SHOW_NAVIGATION_CANCELLED = 0x10000
                    BFO_USE_IE_STATUSBAR = 0x20000
                    #~#~#~ BFO_QUERY_ALL    = ( INT  )0xffffffff


                BFO_NONE = _BROWSERFRAMEOPTIONS.BFO_NONE
                BFO_BROWSER_PERSIST_SETTINGS = _BROWSERFRAMEOPTIONS.BFO_BROWSER_PERSIST_SETTINGS
                BFO_RENAME_FOLDER_OPTIONS_TOINTERNET = _BROWSERFRAMEOPTIONS.BFO_RENAME_FOLDER_OPTIONS_TOINTERNET
                BFO_BOTH_OPTIONS = _BROWSERFRAMEOPTIONS.BFO_BOTH_OPTIONS
                BIF_PREFER_INTERNET_SHORTCUT = _BROWSERFRAMEOPTIONS.BIF_PREFER_INTERNET_SHORTCUT
                BFO_BROWSE_NO_IN_NEW_PROCESS = _BROWSERFRAMEOPTIONS.BFO_BROWSE_NO_IN_NEW_PROCESS
                BFO_ENABLE_HYPERLINK_TRACKING = _BROWSERFRAMEOPTIONS.BFO_ENABLE_HYPERLINK_TRACKING
                BFO_USE_IE_OFFLINE_SUPPORT = _BROWSERFRAMEOPTIONS.BFO_USE_IE_OFFLINE_SUPPORT
                BFO_SUBSTITUE_INTERNET_START_PAGE = _BROWSERFRAMEOPTIONS.BFO_SUBSTITUE_INTERNET_START_PAGE
                BFO_USE_IE_LOGOBANDING = _BROWSERFRAMEOPTIONS.BFO_USE_IE_LOGOBANDING
                BFO_ADD_IE_TOCAPTIONBAR = _BROWSERFRAMEOPTIONS.BFO_ADD_IE_TOCAPTIONBAR
                BFO_USE_DIALUP_REF = _BROWSERFRAMEOPTIONS.BFO_USE_DIALUP_REF
                BFO_USE_IE_TOOLBAR = _BROWSERFRAMEOPTIONS.BFO_USE_IE_TOOLBAR
                BFO_NO_PARENT_FOLDER_SUPPORT = _BROWSERFRAMEOPTIONS.BFO_NO_PARENT_FOLDER_SUPPORT
                BFO_NO_REOPEN_NEXT_RESTART = _BROWSERFRAMEOPTIONS.BFO_NO_REOPEN_NEXT_RESTART
                BFO_GO_HOME_PAGE = _BROWSERFRAMEOPTIONS.BFO_GO_HOME_PAGE
                BFO_PREFER_IEPROCESS = _BROWSERFRAMEOPTIONS.BFO_PREFER_IEPROCESS
                BFO_SHOW_NAVIGATION_CANCELLED = _BROWSERFRAMEOPTIONS.BFO_SHOW_NAVIGATION_CANCELLED
                BFO_USE_IE_STATUSBAR = _BROWSERFRAMEOPTIONS.BFO_USE_IE_STATUSBAR
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][out]
                else: # C style interface
                    IBrowserFrameOptions._methods_ = [

                        # Do nothing. Does this item want the browser stream?
                        # (Same window position as IE browser windows?) Rename
                        # "Folder Options" to "Internet Options" in the Tools
                        # or View menu? Keep both "Folder Options" and
                        # "Internet Options" in the Tools or View menu? NSE
                        # would prefer a .url SHORTcut over a .lnk SHORTcut
                        # Specify this flag if you don't want the
                        # "Browse in New Process" via invoking a SHORTcut.
                        # Does this NSE want it's display name tracked to
                        # determine when hyperlinks should be tagged as
                        # previously used? Use "Internet Explorer"'s offline
                        # support? Does this NSE want to use the Start Page
                        # support? Use the Brand block in the Toolbar.
                        # (Spinning globe or whatever it is this year) Should
                        # " - Internet Explorer" be appended to display name
                        # in the Captionbar Should the DialUp ref count get a
                        # ref while the browse is navigated to this location?
                        # This will also enable the ICW and Software update.
                        # Should the IE toolbar be used? Can you NOT navigate
                        # to a parent folder? Used for Backspace button to
                        # parent folder or the View.GoTo.ParentFolder feature.
                        # Browser windows are NOT reopened the next time the
                        # shell boots if the windows were left open on the
                        # previous logoff. Does this NSE want the same
                        # feature? Add "Home Page" to menu (Go). prefers to
                        # use IEXPLORE.EXE over EXPLORER.EXE If navigation is
                        # aborted, show the "Action Cancelled" HTML page. Use
                        # the persisted IE status bar settings Return all
                        # values set.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFrameOptions',
                            (
                                [annotation('_In_'), 'in'],
                                BROWSERFRAMEOPTIONS,
                               'dwMask'
                            ),
                            (
                                ['out', annotation('_Out_')],
                                POINTER(BROWSERFRAMEOPTIONS),
                               ' pdwOptions'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __IBrowserFrameOptions_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0106

            # [local]
        # END IF   _WIN32_IE_IE60
        if (_WIN32_IE >= _WIN32_IE_IE60SP2):
            class NWMF(ENUM):
                NWMF_UNLOADING = 0x1
                NWMF_USERINITED = 0x2
                NWMF_FIRST = 0x4
                NWMF_OVERRIDEKEY = 0x8
                NWMF_SHOWHELP = 0x10
                NWMF_HTMLDIALOG = 0x20
                NWMF_FROMDIALOGCHILD = 0x40
                NWMF_USERREQUESTED = 0x80
                NWMF_USERALLOWED = 0x100
                NWMF_FORCEWINDOW = 0x10000
                NWMF_FORCETAB = 0x20000
                NWMF_SUGGESTWINDOW = 0x40000
                NWMF_SUGGESTTAB = 0x80000
                NWMF_INACTIVETAB = 0x100000


            NWMF_UNLOADING = NWMF.NWMF_UNLOADING
            NWMF_USERINITED = NWMF.NWMF_USERINITED
            NWMF_FIRST = NWMF.NWMF_FIRST
            NWMF_OVERRIDEKEY = NWMF.NWMF_OVERRIDEKEY
            NWMF_SHOWHELP = NWMF.NWMF_SHOWHELP
            NWMF_HTMLDIALOG = NWMF.NWMF_HTMLDIALOG
            NWMF_FROMDIALOGCHILD = NWMF.NWMF_FROMDIALOGCHILD
            NWMF_USERREQUESTED = NWMF.NWMF_USERREQUESTED
            NWMF_USERALLOWED = NWMF.NWMF_USERALLOWED
            NWMF_FORCEWINDOW = NWMF.NWMF_FORCEWINDOW
            NWMF_FORCETAB = NWMF.NWMF_FORCETAB
            NWMF_SUGGESTWINDOW = NWMF.NWMF_SUGGESTWINDOW
            NWMF_SUGGESTTAB = NWMF.NWMF_SUGGESTTAB
            NWMF_INACTIVETAB = NWMF.NWMF_INACTIVETAB
            SID_SNewWindowManager = IID_INewWindowManager

            if not defined(__INewWindowManager_INTERFACE_DEFINED__):
                __INewWindowManager_INTERFACE_DEFINED__ = 1

                # interface INewWindowManager

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    INewWindowManager._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EvaluateNewWindow',
                            (['in'], LPCWSTR, 'pszUrl'),
                            ([], LPCWSTR, 'pszName'),
                            ([], LPCWSTR, 'pszUrlContext'),
                            ([], LPCWSTR, 'pszFeatures'),
                            (['in'], BOOL, 'fReplace'),
                            ([], DWORD, 'dwFlags'),
                            ([], DWORD, 'dwUserActionTime'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __INewWindowManager_INTERFACE_DEFINED__
            if not defined(__IAttachmentExecute_INTERFACE_DEFINED__):
                __IAttachmentExecute_INTERFACE_DEFINED__ = 1

                # interface IAttachmentExecute

                # [unique][local][uuid][object]


                class ATTACHMENT_PROMPT(ENUM):
                    ATTACHMENT_PROMPT_NONE = 0
                    ATTACHMENT_PROMPT_SAVE = 0x1
                    ATTACHMENT_PROMPT_EXEC = 0x2
                    ATTACHMENT_PROMPT_EXEC_OR_SAVE = 0x3


                ATTACHMENT_PROMPT_NONE = ATTACHMENT_PROMPT.ATTACHMENT_PROMPT_NONE
                ATTACHMENT_PROMPT_SAVE = ATTACHMENT_PROMPT.ATTACHMENT_PROMPT_SAVE
                ATTACHMENT_PROMPT_EXEC = ATTACHMENT_PROMPT.ATTACHMENT_PROMPT_EXEC
                ATTACHMENT_PROMPT_EXEC_OR_SAVE = ATTACHMENT_PROMPT.ATTACHMENT_PROMPT_EXEC_OR_SAVE
                class ATTACHMENT_ACTION(ENUM):
                    ATTACHMENT_ACTION_CANCEL = 0
                    ATTACHMENT_ACTION_SAVE = 0x1
                    ATTACHMENT_ACTION_EXEC = 0x2


                ATTACHMENT_ACTION_CANCEL = ATTACHMENT_ACTION.ATTACHMENT_ACTION_CANCEL
                ATTACHMENT_ACTION_SAVE = ATTACHMENT_ACTION.ATTACHMENT_ACTION_SAVE
                ATTACHMENT_ACTION_EXEC = ATTACHMENT_ACTION.ATTACHMENT_ACTION_EXEC
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][out]

                    # [annotation][in]
                else: # C style interface
                    IAttachmentExecute._methods_ = [
                        #

                        #
                        # IAttachmentExecute - COM object deINT to help client
                        # applications
                        # safely manage saving and opening attachments for
                        # users.
                        # clients are assumed to have some policy/settings
                        # already
                        # to determine the support and behavior for
                        # attachments.
                        # this API assumes that the client is interactive with
                        # the user
                        # ClientTitle - (optional) caller specific title for
                        # the prompt
                        # if unset, the prompts come with a default title of
                        # "File Download"                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetClientTitle',
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszTitle'
                            ),
                        ),

                        # ClientGuid - (optional) for storing user specific
                        # settings
                        # someprompts are allowed to be aVOIDed in the future
                        # if the user
                        # chooses. that choice is stored on per - client basis
                        # indexed by the ClientGuid
                        # Specific Example: In the User Trust Prompt there is
                        # a check box that is checked
                        # by default, but may be unchecked by the user. this
                        # option is stored under the ClientGuid
                        # based on the file type.
                        # ClearClientState() will reset any user options
                        # stored on the clients behalf.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetClientGuid',
                            ([annotation('_In_'), 'in'], REFGUID, 'guid'),
                        ),

                        # EVIDENCE properties
                        # LocalPath - (REQUIRED) path that would be passed to
                        # ShellExecute()
                        # if FileName was already used for the Check() and
                        # Prompt() calls,
                        # and the LocalPath points to a different handler than
                        # predicted,
                        # previous trust may be revoked, and the Policy and
                        # User trust re - verified.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetLocalPath',
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszLocalPath'
                            ),
                        ),

                        # FileName - (optional) proposed name (not path) to be
                        # used to construct LocalPath
                        # optionally use this if the caller wants to perform
                        # Check() before copying
                        # the file to the LocalPath.
                        # (eg, Check() proposed download)                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetFileName',
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszFileName'
                            ),
                        ),

                        # Source - (optional) alternate identity path or URL
                        # for a file transfer
                        # used as the primary Zone determinant. if this is
                        # NULL default to the Restricted Zone.
                        # may also be used in the Prompt() UI for the "From"
                        # field
                        # may also be sent to handlers that can process URLs                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSource',
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszSource'
                            ),
                        ),

                        # Referrer - (optional) Zone determinant for container
                        # or link types
                        # only used for Zone/Policy
                        # container formats like ZIP and OLE packager use the
                        # Referrer to
                        # indicate indirect inheritance and aVOID Zone
                        # elevation.
                        # Shortcuts can also use it to limit elevation based
                        # on parameters                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetReferrer',
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszReferrer'
                            ),
                        ),

                        # CheckPolicy() - examines available evidence and
                        # checks the resultant policy
                        # * requires FileName or LocalPath
                        # Returns S_OK for enable
                        # S_FALSE for prompt
                        # FAILURE for disable                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'CheckPolicy',
                        ),

                        # Prompt() - application can force UI at an earlier
                        # point,
                        # even before the file has been copied to disk
                        # * requires FileName or LocalPath
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Prompt',
                            ([annotation('_In_'), 'in'], HWND, 'hwnd'),
                            ([], ATTACHMENT_PROMPT, 'prompt'),
                            (
                                [annotation('_Out_'), 'out'],
                                POINTER(ATTACHMENT_ACTION),
                               'paction'
                            ),
                        ),

                        # Save() - should always be called if LocalPath is in
                        # not in a temp dir
                        # * requires valid LocalPath
                        # * called after the file has been copied to LocalPath
                        # * may run virus scanners or other trust services to
                        # validate the file.
                        # these services may delete or alter the file
                        # * may attach evidence to the LocalPath                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Save',
                        ),

                        # Execute() - will call Prompt() if necessary, with
                        # the EXEC action
                        # * requires valid LocalPath
                        # * called after the file has been copied to LocalPath
                        # * may run virus scanners or other trust services to
                        # validate the file.
                        # these services may delete or alter the file
                        # * may attach evidence to the LocalPath
                        # phProcess - if non - NULL Execute() will be
                        # synchronous and return an HPROCESS if available
                        # if null Execute() will be async, implies that you
                        # have a message pump and a LONG lived window
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Execute',
                            ([annotation('_In_'), 'in'], HWND, 'hwnd'),
                            (
                                [annotation('_In_opt_'), 'in'],
                                LPCWSTR,
                               'pszVerb'
                            ),
                            (
                                [annotation('_Out_opt_'), 'out'],
                                POINTER(HANDLE),
                               'phProcess'
                            ),
                        ),

                        # SaveWithUI() - superset of Save() that can show
                        # modal error UI, but still does not call Prompt()
                        # * requires valid LocalPath
                        # * called after the file has been copied to LocalPath
                        # * may run virus scanners or other trust services to
                        # validate the file.
                        # these services may delete or alter the file
                        # * may attach evidence to the LocalPath                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SaveWithUI',
                            ([annotation('_In_'), 'in'], HWND, 'hwnd'),
                        ),

                        # ClearClientState() - removes any state that is
                        # stored based on the ClientGuid
                        # * requires SetClientGuid() to be called first                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ClearClientState',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][out]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IAttachmentExecute_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0108

            # [local]
        # END IF   _WIN32_IE_IE60SP2
        if (_WIN32_IE >= _WIN32_IE_IE60):
            class tagSMDATA(ctypes.Structure):
                pass
            tagSMDATA._fields_ = [
                ('dwMask', DWORD),
                ('dwFlags', DWORD),
                ('hmenu', HMENU),
                ('hwnd', HWND),
                ('uId', UINT),
                ('uIdParent', UINT),
                ('uIdAncestor', UINT),
                ('punk', POINTER(comtypes.IUnknown)),
                ('pidlFolder', PIDLIST_ABSOLUTE),
                ('pidlItem', PUITEMID_CHILD),
                ('psf', POINTER(IShellFolder)),
                ('pvUserData', POINTER(VOID)),
            ]


            SMDATA = tagSMDATA


            LPSMDATA = POINTER(tagSMDATA)



            # Mask
            SMDM_SHELLFOLDER = 0x00000001
            SMDM_HMENU = 0x00000002
            SMDM_TOOLBAR = 0x00000004

            # Flags (bitmask)
            class tagSMINFO(ctypes.Structure):
                pass
            tagSMINFO._fields_ = [
                ('dwMask', DWORD),
                ('dwType', DWORD),
                ('dwFlags', DWORD),
                ('iIcon', INT),
            ]


            SMINFO = tagSMINFO


            PSMINFO = POINTER(tagSMINFO)


            class SHCSCHANGENOTIFYSTRUCT(ctypes.Structure):
                pass
            SHCSCHANGENOTIFYSTRUCT._fields_ = [
                ('lEvent', LONG),
                ('pidl1', PCIDLIST_ABSOLUTE),
                ('pidl2', PCIDLIST_ABSOLUTE),
            ]


            SMCSHCHANGENOTIFYSTRUCT = SHCSCHANGENOTIFYSTRUCT


            PSMCSHCHANGENOTIFYSTRUCT = POINTER(SHCSCHANGENOTIFYSTRUCT)




            class tagSMINFOMASK(ENUM):
                SMIM_TYPE = 0x1
                SMIM_FLAGS = 0x2
                SMIM_ICON = 0x4


            SMIM_TYPE = tagSMINFOMASK.SMIM_TYPE
            SMIM_FLAGS = tagSMINFOMASK.SMIM_FLAGS
            SMIM_ICON = tagSMINFOMASK.SMIM_ICON
            class tagSMINFOTYPE(ENUM):
                SMIT_SEPARATOR = 0x1
                SMIT_STRING = 0x2


            SMIT_SEPARATOR = tagSMINFOTYPE.SMIT_SEPARATOR
            SMIT_STRING = tagSMINFOTYPE.SMIT_STRING
            class tagSMINFOFLAGS(ENUM):
                SMIF_ICON = 0x1
                SMIF_ACCELERATOR = 0x2
                SMIF_DROPTARGET = 0x4
                SMIF_SUBMENU = 0x8
                SMIF_CHECKED = 0x20
                SMIF_DROPCASCADE = 0x40
                SMIF_HIDDEN = 0x80
                SMIF_DISABLED = 0x100
                SMIF_TRACKPOPUP = 0x200
                SMIF_DEMOTED = 0x400
                SMIF_ALTSTATE = 0x800
                SMIF_DRAGNDROP = 0x1000
                SMIF_NEW = 0x2000


            SMIF_ICON = tagSMINFOFLAGS.SMIF_ICON
            SMIF_ACCELERATOR = tagSMINFOFLAGS.SMIF_ACCELERATOR
            SMIF_DROPTARGET = tagSMINFOFLAGS.SMIF_DROPTARGET
            SMIF_SUBMENU = tagSMINFOFLAGS.SMIF_SUBMENU
            SMIF_CHECKED = tagSMINFOFLAGS.SMIF_CHECKED
            SMIF_DROPCASCADE = tagSMINFOFLAGS.SMIF_DROPCASCADE
            SMIF_HIDDEN = tagSMINFOFLAGS.SMIF_HIDDEN
            SMIF_DISABLED = tagSMINFOFLAGS.SMIF_DISABLED
            SMIF_TRACKPOPUP = tagSMINFOFLAGS.SMIF_TRACKPOPUP
            SMIF_DEMOTED = tagSMINFOFLAGS.SMIF_DEMOTED
            SMIF_ALTSTATE = tagSMINFOFLAGS.SMIF_ALTSTATE
            SMIF_DRAGNDROP = tagSMINFOFLAGS.SMIF_DRAGNDROP
            SMIF_NEW = tagSMINFOFLAGS.SMIF_NEW
            SMC_INITMENU = 0x00000001
            SMC_CREATE = 0x00000002
            SMC_EXITMENU = 0x00000003
            SMC_GETINFO = 0x00000005
            SMC_GETSFINFO = 0x00000006
            SMC_GETOBJECT = 0x00000007
            SMC_GETSFOBJECT = 0x00000008
            SMC_SFEXEC = 0x00000009
            SMC_SFSELECTITEM = 0x0000000A
            SMC_REFRESH = 0x00000010
            SMC_DEMOTE = 0x00000011
            SMC_PROMOTE = 0x00000012
            SMC_DEFAULTICON = 0x00000016
            SMC_NEWITEM = 0x00000017
            SMC_CHEVRONEXPAND = 0x00000019
            SMC_DISPLAYCHEVRONTIP = 0x0000002A
            SMC_SETSFOBJECT = 0x0000002D
            SMC_SHCHANGENOTIFY = 0x0000002E
            SMC_CHEVRONGETTIP = 0x0000002F
            SMC_SFDDRESTRICTED = 0x00000030

            if (_WIN32_IE >= _WIN32_IE_IE70):
                SMC_SFEXEC_MIDDLE = 0x00000031
                SMC_GETAUTOEXPANDSTATE = 0x00000041
                SMC_AUTOEXPANDCHANGE = 0x00000042
                SMC_GETCONTEXTMENUMODIFIER = 0x00000043
                SMC_GETBKCONTEXTMENU = 0x00000044
                SMC_OPEN = 0x00000045

                # Flags for return value from SMC_GETAUTOEXPANDSTATE and
                # SMC_AUTOEXPANDCHANGE:
                SMAE_EXPANDED = 0x00000001
                SMAE_CONTRACTED = 0x00000002

                # SMAE_EXPANDED and SMAE_CONTRACTED are mutually exclusive
                SMAE_USER = 0x00000004

                # of user choice
                SMAE_VALID = 0x00000007
            # END IF   _WIN32_IE_IE70

            if not defined(__IShellMenuCallback_INTERFACE_DEFINED__):
                __IShellMenuCallback_INTERFACE_DEFINED__ = 1

                # interface IShellMenuCallback

                # [local][unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][out][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                else: # C style interface
                    IShellMenuCallback._methods_ = [

                        # psmd is [in,out] because SMC_MAPACCELERATOR returns
                        # a value in uId
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'CallbackSM',
                            (
                                [annotation('_Inout_'), 'out', 'in'],
                                LPSMDATA,
                               'psmd'
                            ),
                            ([annotation('_In_'), 'in'], UINT, 'uMsg'),
                            ([], WPARAM, 'wParam'),
                            ([], LPARAM, 'lParam'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][out][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IShellMenuCallback_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0109

            # [local]
            SMINIT_DEFAULT = 0x00000000
            SMINIT_RESTRICT_DRAGDROP = 0x00000002
            SMINIT_TOPLEVEL = 0x00000004
            SMINIT_CACHED = 0x00000010

            if (_WIN32_IE >= _WIN32_IE_IE70):
                SMINIT_AUTOEXPAND = 0x00000100
                SMINIT_AUTOTOOLTIP = 0x00000200
                SMINIT_DROPONCONTAINER = 0x00000400
            # END IF   _WIN32_IE_IE70
            SMINIT_VERTICAL = 0x10000000
            SMINIT_HORIZONTAL = 0x20000000
            ANCESTORDEFAULT = (UINT) - 1
            SMSET_TOP = 0x10000000
            SMSET_BOTTOM = 0x20000000
            SMSET_DONTOWN = 0x00000001
            SMINV_REFRESH = 0x00000001
            SMINV_ID = 0x00000008

            if not defined(__IShellMenu_INTERFACE_DEFINED__):
                __IShellMenu_INTERFACE_DEFINED__ = 1

                # interface IShellMenu

                # [local][unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][iid_is][out]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]
                else: # C style interface
                    IShellMenu._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Initialize',
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                POINTER(IShellMenuCallback),
                               'psmc'
                            ),
                            ([annotation('_In_'), 'in'], UINT, 'uId'),
                            ([], UINT, 'uIdAncestor'),
                            ([], DWORD, 'dwFlags'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetMenuInfo',
                            (
                                ['out', annotation('_Outptr_opt_')],
                                POINTER(POINTER(IShellMenuCallback)),
                               'ppsmc'
                            ),
                            (
                                ['out', annotation('_Out_opt_')],
                                POINTER(UINT),
                               'puId'
                            ),
                            ([], POINTER(UINT), 'puIdAncestor'),
                            ([], POINTER(DWORD), 'pdwFlags'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetShellFolder',
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                POINTER(IShellFolder),
                               'psf'
                            ),
                            ([], PCIDLIST_ABSOLUTE, 'pidlFolder'),
                            ([], HKEY, 'hKey'),
                            ([annotation('_In_'), 'in'], DWORD, 'dwFlags'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetShellFolder',
                            (
                                ['out', annotation('_Out_')],
                                POINTER(DWORD),
                               'pdwFlags'
                            ),
                            (
                                ['out', annotation('_Outptr_')],
                                POINTER(PIDLIST_ABSOLUTE),
                               'ppidl'
                            ),
                            (['in'], REFIID, 'riid'),
                            (
                                ['out', annotation('_Outptr_')],
                                POINTER(POINTER(VOID)),
                               'ppv'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetMenu',
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                HMENU,
                               'hmenu'
                            ),
                            ([], HWND, 'hwnd'),
                            ([annotation('_In_'), 'in'], DWORD, 'dwFlags'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetMenu',
                            (
                                ['out', annotation('_Out_opt_')],
                                POINTER(HMENU),
                               'phmenu'
                            ),
                            ([], POINTER(HWND), 'phwnd'),
                            ([], POINTER(DWORD), 'pdwFlags'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'InvalidateItem',
                            (
                                [annotation('_In_opt_'), 'in'],
                                LPSMDATA,
                               'psmd'
                            ),
                            ([annotation('_In_'), 'in'], DWORD, 'dwFlags'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetState',
                            (['out', annotation('_Out_')], LPSMDATA, 'psmd'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetMenuToolbar',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IUnknown),
                               'punk'
                            ),
                            ([], DWORD, 'dwFlags'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][iid_is][out]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IShellMenu_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0110

            # [local]
        # END IF   _WIN32_IE_IE60
        if (NTDDI_VERSION >= NTDDI_VISTA):
            class KF_CATEGORY(ENUM):
                KF_CATEGORY_VIRTUAL = 1
                KF_CATEGORY_FIXED = 2
                KF_CATEGORY_COMMON = 3
                KF_CATEGORY_PERUSER = 4


            KF_CATEGORY_VIRTUAL = KF_CATEGORY.KF_CATEGORY_VIRTUAL
            KF_CATEGORY_FIXED = KF_CATEGORY.KF_CATEGORY_FIXED
            KF_CATEGORY_COMMON = KF_CATEGORY.KF_CATEGORY_COMMON
            KF_CATEGORY_PERUSER = KF_CATEGORY.KF_CATEGORY_PERUSER

            # [v1_enum]
            class _KF_DEFINITION_FLAGS(ENUM):
                KFDF_LOCAL_REDIRECT_ONLY = 0x2
                KFDF_ROAMABLE = 0x4
                KFDF_PRECREATE = 0x8
                KFDF_STREAM = 0x10
                KFDF_PUBLISHEXPANDEDPATH = 0x20
                KFDF_NO_REDIRECT_UI = 0x40


            KFDF_LOCAL_REDIRECT_ONLY = _KF_DEFINITION_FLAGS.KFDF_LOCAL_REDIRECT_ONLY
            KFDF_ROAMABLE = _KF_DEFINITION_FLAGS.KFDF_ROAMABLE
            KFDF_PRECREATE = _KF_DEFINITION_FLAGS.KFDF_PRECREATE
            KFDF_STREAM = _KF_DEFINITION_FLAGS.KFDF_STREAM
            KFDF_PUBLISHEXPANDEDPATH = _KF_DEFINITION_FLAGS.KFDF_PUBLISHEXPANDEDPATH
            KFDF_NO_REDIRECT_UI = _KF_DEFINITION_FLAGS.KFDF_NO_REDIRECT_UI

            # [v1_enum]
            class _KF_REDIRECT_FLAGS(ENUM):
                KF_REDIRECT_USER_EXCLUSIVE = 0x1
                KF_REDIRECT_COPY_SOURCE_DACL = 0x2
                KF_REDIRECT_OWNER_USER = 0x4
                KF_REDIRECT_SET_OWNER_EXPLICIT = 0x8
                KF_REDIRECT_CHECK_ONLY = 0x10
                KF_REDIRECT_WITH_UI = 0x20
                KF_REDIRECT_UNPIN = 0x40
                KF_REDIRECT_PIN = 0x80
                KF_REDIRECT_COPY_CONTENTS = 0x200
                KF_REDIRECT_DEL_SOURCE_CONTENTS = 0x400
                KF_REDIRECT_EXCLUDE_ALL_KNOWN_SUBFOLDERS = 0x800


            KF_REDIRECT_USER_EXCLUSIVE = _KF_REDIRECT_FLAGS.KF_REDIRECT_USER_EXCLUSIVE
            KF_REDIRECT_COPY_SOURCE_DACL = _KF_REDIRECT_FLAGS.KF_REDIRECT_COPY_SOURCE_DACL
            KF_REDIRECT_OWNER_USER = _KF_REDIRECT_FLAGS.KF_REDIRECT_OWNER_USER
            KF_REDIRECT_SET_OWNER_EXPLICIT = _KF_REDIRECT_FLAGS.KF_REDIRECT_SET_OWNER_EXPLICIT
            KF_REDIRECT_CHECK_ONLY = _KF_REDIRECT_FLAGS.KF_REDIRECT_CHECK_ONLY
            KF_REDIRECT_WITH_UI = _KF_REDIRECT_FLAGS.KF_REDIRECT_WITH_UI
            KF_REDIRECT_UNPIN = _KF_REDIRECT_FLAGS.KF_REDIRECT_UNPIN
            KF_REDIRECT_PIN = _KF_REDIRECT_FLAGS.KF_REDIRECT_PIN
            KF_REDIRECT_COPY_CONTENTS = _KF_REDIRECT_FLAGS.KF_REDIRECT_COPY_CONTENTS
            KF_REDIRECT_DEL_SOURCE_CONTENTS = _KF_REDIRECT_FLAGS.KF_REDIRECT_DEL_SOURCE_CONTENTS
            KF_REDIRECT_EXCLUDE_ALL_KNOWN_SUBFOLDERS = _KF_REDIRECT_FLAGS.KF_REDIRECT_EXCLUDE_ALL_KNOWN_SUBFOLDERS

            # [v1_enum]
            class _KF_REDIRECTION_CAPABILITIES(ENUM):
                KF_REDIRECTION_CAPABILITIES_ALLOW_ALL = 0xFF
                KF_REDIRECTION_CAPABILITIES_REDIRECTABLE = 0x1
                KF_REDIRECTION_CAPABILITIES_DENY_ALL = 0xFFF00
                KF_REDIRECTION_CAPABILITIES_DENY_POLICY_REDIRECTED = 0x100
                KF_REDIRECTION_CAPABILITIES_DENY_POLICY = 0x200
                KF_REDIRECTION_CAPABILITIES_DENY_PERMISSIONS = 0x400


            KF_REDIRECTION_CAPABILITIES_ALLOW_ALL = _KF_REDIRECTION_CAPABILITIES.KF_REDIRECTION_CAPABILITIES_ALLOW_ALL
            KF_REDIRECTION_CAPABILITIES_REDIRECTABLE = _KF_REDIRECTION_CAPABILITIES.KF_REDIRECTION_CAPABILITIES_REDIRECTABLE
            KF_REDIRECTION_CAPABILITIES_DENY_ALL = _KF_REDIRECTION_CAPABILITIES.KF_REDIRECTION_CAPABILITIES_DENY_ALL
            KF_REDIRECTION_CAPABILITIES_DENY_POLICY_REDIRECTED = _KF_REDIRECTION_CAPABILITIES.KF_REDIRECTION_CAPABILITIES_DENY_POLICY_REDIRECTED
            KF_REDIRECTION_CAPABILITIES_DENY_POLICY = _KF_REDIRECTION_CAPABILITIES.KF_REDIRECTION_CAPABILITIES_DENY_POLICY
            KF_REDIRECTION_CAPABILITIES_DENY_PERMISSIONS = _KF_REDIRECTION_CAPABILITIES.KF_REDIRECTION_CAPABILITIES_DENY_PERMISSIONS
            class KNOWNFOLDER_DEFINITION(ctypes.Structure):
                pass
            KNOWNFOLDER_DEFINITION._fields_ = [
                ('category', KF_CATEGORY),
                ('pszName', LPWSTR),
                ('pszDescription', LPWSTR),
                ('fidParent', KNOWNFOLDERID),
                ('pszRelativePath', LPWSTR),
                ('pszParsingName', LPWSTR),
                ('pszTooltip', LPWSTR),
                ('pszLocalizedName', LPWSTR),
                ('pszIcon', LPWSTR),
                ('pszSecurity', LPWSTR),
                ('dwAttributes', DWORD),
                ('kfdFlags', KF_DEFINITION_FLAGS),
                ('ftidType', FOLDERTYPEID),
            ]


            if not defined(__IKnownFolder_INTERFACE_DEFINED__):
                __IKnownFolder_INTERFACE_DEFINED__ = 1

                # interface IKnownFolder

                # [ref][version][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IKnownFolder._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetId',
                            (['out'], POINTER(KNOWNFOLDERID), 'pkfid'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetCategory',
                            (['out'], POINTER(KF_CATEGORY), 'pCategory'),
                        ),

                        # get the ShellItem (IShellItem or derived interface)
                        # for this known folder
                        # KNOWN_FOLDER_FLAG                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetShellItem',
                            (['in'], DWORD, 'dwFlags'),
                            ([], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),

                        # KNOWN_FOLDER_FLAG                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetPath',
                            (['in'], DWORD, 'dwFlags'),
                            (['out', ], POINTER(LPWSTR), 'ppszPath'),
                        ),

                        # KNOWN_FOLDER_FLAG                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetPath',
                            (['in'], DWORD, 'dwFlags'),
                            (['in'], LPCWSTR, 'pszPath'),
                        ),

                        # KNOWN_FOLDER_FLAG                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetIDList',
                            (['in'], DWORD, 'dwFlags'),
                            (['out'], POINTER(PIDLIST_ABSOLUTE), 'ppidl'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFolderType',
                            (['out'], POINTER(FOLDERTYPEID), 'pftid'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetRedirectionCapabilities',
                            (
                                ['out'],
                                POINTER(KF_REDIRECTION_CAPABILITIES),
                               ' pCapabilities'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFolderDefinition',
                            (
                                ['out'],
                                POINTER(KNOWNFOLDER_DEFINITION),
                               'pKFD'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IKnownFolder_INTERFACE_DEFINED__
            if not defined(__IKnownFolderManager_INTERFACE_DEFINED__):
                __IKnownFolderManager_INTERFACE_DEFINED__ = 1

                # interface IKnownFolderManager

                # [ref][version][object][uuid]


                class FFFP_MODE(ENUM):
                    FFFP_EXACTMATCH = 0
                    #~#~#~ FFFP_NEARESTPARENTMATCH    = ( FFFP_EXACTMATCH + 1 )


                FFFP_EXACTMATCH = FFFP_MODE.FFFP_EXACTMATCH
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][string][unique][in]

                    # [annotation][in]

                    # [annotation][unique][size_is][in]

                    # [annotation][string][out]
                else: # C style interface
                    IKnownFolderManager._methods_ = [
                        #

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'FolderIdFromCsidl',
                            (['in'], INT, 'nCsidl'),
                            (['out'], POINTER(KNOWNFOLDERID), 'pfid'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'FolderIdToCsidl',
                            (['in'], REFKNOWNFOLDERID, 'rfid'),
                            (['out'], POINTER(INT), 'pnCsidl'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFolderIds',
                            (
                                ['out'],
                                POINTER(POINTER(KNOWNFOLDERID)),
                               ' ppKFId'
                            ),
                            (['out', 'in'], POINTER(UINT), 'pCount'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFolder',
                            (['in'], REFKNOWNFOLDERID, 'rfid'),
                            (['out'], POINTER(POINTER(IKnownFolder)), 'ppkf'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetFolderByName',
                            (['in'], LPCWSTR, 'pszCanonicalName'),
                            (['out'], POINTER(POINTER(IKnownFolder)), 'ppkf'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RegisterFolder',
                            (['in'], REFKNOWNFOLDERID, 'rfid'),
                            ([], POINTER(KNOWNFOLDER_DEFINITION), 'pKFD'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UnregisterFolder',
                            (['in'], REFKNOWNFOLDERID, 'rfid'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'FindFolderFromPath',
                            (['in'], LPCWSTR, 'pszPath'),
                            (['in'], FFFP_MODE, 'mode'),
                            (['out'], POINTER(POINTER(IKnownFolder)), 'ppkf'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'FindFolderFromIDList',
                            (['in'], PCIDLIST_ABSOLUTE, 'pidl'),
                            (['out'], POINTER(POINTER(IKnownFolder)), 'ppkf'),
                        ),

                        #                    
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'Redirect',
                            (
                                [annotation('_In_'), 'in'],
                                REFKNOWNFOLDERID,
                               'rfid'
                            ),
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                HWND,
                               'hwnd'
                            ),
                            ([], KF_REDIRECT_FLAGS, 'flags'),
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                LPCWSTR,
                               'pszTargetPath'
                            ),
                            ([], UINT, 'cFolders'),
                            (
                                ['unique', annotation('_In_reads_opt_(cFolders)), 'in'],
                                POINTER(KNOWNFOLDERID),
                               'pExclusion'
                            ),
                            (
                                ['out', , annotation('_Outptr_opt_result_maybenull_')],
                                POINTER(LPWSTR),
                               'ppszError'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoteRedirect',
                            (['in'], REFKNOWNFOLDERID, 'rfid'),
                            (['unique', 'in'], HWND, 'hwnd'),
                            ([], KF_REDIRECT_FLAGS, 'flags'),
                            (['unique', 'in'], LPCWSTR, 'pszTargetPath'),
                            ([], UINT, 'cFolders'),
                            (['unique', 'in'], POINTER(GUID), 'pExclusion'),
                            (['out', ], POINTER(LPWSTR), 'ppszError'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][string][unique][in]

                    # [annotation][in]

                    # [annotation][unique][size_is][in]

                    # [annotation][string][out]
                # END IF  C style interface
            # END IF  __IKnownFolderManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0112

            # [local]
            class SHARE_ROLE(ENUM):
                SHARE_ROLE_INVALID = - 1
                SHARE_ROLE_READER = 0
                SHARE_ROLE_CONTRIBUTOR = 1
                SHARE_ROLE_CO_OWNER = 2
                SHARE_ROLE_OWNER = 3
                SHARE_ROLE_CUSTOM = 4
                SHARE_ROLE_MIXED = 5


            SHARE_ROLE_INVALID = SHARE_ROLE.SHARE_ROLE_INVALID
            SHARE_ROLE_READER = SHARE_ROLE.SHARE_ROLE_READER
            SHARE_ROLE_CONTRIBUTOR = SHARE_ROLE.SHARE_ROLE_CONTRIBUTOR
            SHARE_ROLE_CO_OWNER = SHARE_ROLE.SHARE_ROLE_CO_OWNER
            SHARE_ROLE_OWNER = SHARE_ROLE.SHARE_ROLE_OWNER
            SHARE_ROLE_CUSTOM = SHARE_ROLE.SHARE_ROLE_CUSTOM
            SHARE_ROLE_MIXED = SHARE_ROLE.SHARE_ROLE_MIXED
            class DEF_SHARE_ID(ENUM):
                DEFSHAREID_USERS = 1
                DEFSHAREID_PUBLIC = 2


            DEFSHAREID_USERS = DEF_SHARE_ID.DEFSHAREID_USERS
            DEFSHAREID_PUBLIC = DEF_SHARE_ID.DEFSHAREID_PUBLIC
            if not defined(__ISharingConfigurationManager_INTERFACE_DEFINED__):
                __ISharingConfigurationManager_INTERFACE_DEFINED__ = 1

                # interface ISharingConfigurationManager

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    ISharingConfigurationManager._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'CreateShare',
                            (['in'], DEF_SHARE_ID, 'dsid'),
                            ([], SHARE_ROLE, 'role'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DeleteShare',
                            (['in'], DEF_SHARE_ID, 'dsid'),
                        ),

                        # returns S_OK if the share exists, S_FALSE otherwise                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ShareExists',
                            (['in'], DEF_SHARE_ID, 'dsid'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSharePermissions',
                            (['in'], DEF_SHARE_ID, 'dsid'),
                            (['out'], POINTER(SHARE_ROLE), 'pRole'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SharePrinters',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'StopSharingPrinters',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ArePrintersShared',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __ISharingConfigurationManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0113

            # [local]
        # END IF   NTDDI_VISTA
        if (NTDDI_VERSION >= NTDDI_VISTA):
            if not defined(__IRelatedItem_INTERFACE_DEFINED__):
                __IRelatedItem_INTERFACE_DEFINED__ = 1

                # interface IRelatedItem

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IRelatedItem._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetItemIDList',
                            (['out'], POINTER(PIDLIST_ABSOLUTE), 'ppidl'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetItem',
                            (['out'], POINTER(POINTER(IShellItem)), 'ppsi'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IRelatedItem_INTERFACE_DEFINED__
            if not defined(__IIdentityName_INTERFACE_DEFINED__):
                __IIdentityName_INTERFACE_DEFINED__ = 1

                # interface IIdentityName

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IIdentityName._methods_ = [
                        #
                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IIdentityName_INTERFACE_DEFINED__
            if not defined(__IDelegateItem_INTERFACE_DEFINED__):
                __IDelegateItem_INTERFACE_DEFINED__ = 1

                # interface IDelegateItem

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IDelegateItem._methods_ = [
                        #
                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IDelegateItem_INTERFACE_DEFINED__
            if not defined(__ICurrentItem_INTERFACE_DEFINED__):
                __ICurrentItem_INTERFACE_DEFINED__ = 1

                # interface ICurrentItem

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    ICurrentItem._methods_ = [
                        #
                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __ICurrentItem_INTERFACE_DEFINED__
            if not defined(__ITransferMediumItem_INTERFACE_DEFINED__):
                __ITransferMediumItem_INTERFACE_DEFINED__ = 1

                # interface ITransferMediumItem

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    ITransferMediumItem._methods_ = [
                        #
                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __ITransferMediumItem_INTERFACE_DEFINED__
            if not defined(__IDisplayItem_INTERFACE_DEFINED__):
                __IDisplayItem_INTERFACE_DEFINED__ = 1

                # interface IDisplayItem

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IDisplayItem._methods_ = [
                        #
                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IDisplayItem_INTERFACE_DEFINED__
            if not defined(__IViewStateIdentityItem_INTERFACE_DEFINED__):
                __IViewStateIdentityItem_INTERFACE_DEFINED__ = 1

                # interface IViewStateIdentityItem

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IViewStateIdentityItem._methods_ = [
                        #
                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IViewStateIdentityItem_INTERFACE_DEFINED__
            if not defined(__IPreviewItem_INTERFACE_DEFINED__):
                __IPreviewItem_INTERFACE_DEFINED__ = 1

                # interface IPreviewItem

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IPreviewItem._methods_ = [
                        #
                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IPreviewItem_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0121

            # [local]
        # END IF   NTDDI_VISTA
        if not defined(__IDestinationStreamFactory_INTERFACE_DEFINED__):
            __IDestinationStreamFactory_INTERFACE_DEFINED__ = 1

            # interface IDestinationStreamFactory

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IDestinationStreamFactory._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDestinationStream',
                        (['out'], POINTER(POINTER(IStream)), 'ppstm'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IDestinationStreamFactory_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0122

        # [local]
        if (NTDDI_VERSION >= NTDDI_VISTA):
            if not defined(__ICreateProcessInputs_INTERFACE_DEFINED__):
                __ICreateProcessInputs_INTERFACE_DEFINED__ = 1

                # interface ICreateProcessInputs

                # [local][unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][string][in]
                else: # C style interface
                    ICreateProcessInputs._methods_ = [
                        # CreateProcess() dwCreationFlags parameter
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetCreateFlags',
                            (
                                ['out', annotation('_Out_')],
                                POINTER(DWORD),
                               'pdwCreationFlags'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetCreateFlags',
                            (
                                [annotation('_In_'), 'in'],
                                DWORD,
                               'dwCreationFlags'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddCreateFlags',
                            (
                                [annotation('_In_'), 'in'],
                                DWORD,
                               'dwCreationFlags'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetHotKey',
                            ([annotation('_In_'), 'in'], WORD, 'wHotKey'),
                        ),

                        # STARTUPINFO.dwFlags                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddStartupFlags',
                            (
                                [annotation('_In_'), 'in'],
                                DWORD,
                               'dwStartupInfoFlags'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetTitle',
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszTitle'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetEnvironmentVariable',
                            ([annotation('_In_'), 'in'], LPCWSTR, 'pszName'),
                            ([], LPCWSTR, 'pszValue'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][string][in]

                    # [annotation][string][in]

                    # [annotation][string][in]
                # END IF  C style interface
            # END IF  __ICreateProcessInputs_INTERFACE_DEFINED__
            if not defined(__ICreatingProcess_INTERFACE_DEFINED__):
                __ICreatingProcess_INTERFACE_DEFINED__ = 1

                # interface ICreatingProcess

                # [object][local][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]
                else: # C style interface
                    ICreatingProcess._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnCreating',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(ICreateProcessInputs),
                               'pcpi'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __ICreatingProcess_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0124

            # [local]
            SID_ExecuteCreatingProcess = __uuidof(ICreatingProcess)
        # END IF   NTDDI_VISTA

        # [v1_enum]


        class _NMCII_FLAGS(ENUM):
            NMCII_NONE = 0
            NMCII_ITEMS = 0x1
            NMCII_FOLDERS = 0x2


        NMCII_NONE = _NMCII_FLAGS.NMCII_NONE
        NMCII_ITEMS = _NMCII_FLAGS.NMCII_ITEMS
        NMCII_FOLDERS = _NMCII_FLAGS.NMCII_FOLDERS

        # [v1_enum]
        class _NMCSAEI_FLAGS(ENUM):
            NMCSAEI_SELECT = 0
            NMCSAEI_EDIT = 0x1


        NMCSAEI_SELECT = _NMCSAEI_FLAGS.NMCSAEI_SELECT
        NMCSAEI_EDIT = _NMCSAEI_FLAGS.NMCSAEI_EDIT
        if not defined(__INewMenuClient_INTERFACE_DEFINED__):
            __INewMenuClient_INTERFACE_DEFINED__ = 1

            # interface INewMenuClient

            # [object][unique][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                INewMenuClient._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'IncludeItems',
                        (['out'], POINTER(NMCII_FLAGS), 'pflags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SelectAndEditItem',
                        (['in'], PCIDLIST_ABSOLUTE, 'pidlItem'),
                        ([], NMCSAEI_FLAGS, 'flags'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __INewMenuClient_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0125

        # [local]
        SID_SNewMenuClient = IID_INewMenuClient

        if (_WIN32_IE >= _WIN32_IE_IE70):
            if not defined(__IInitializeWithBindCtx_INTERFACE_DEFINED__):
                __IInitializeWithBindCtx_INTERFACE_DEFINED__ = 1

                # interface IInitializeWithBindCtx

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IInitializeWithBindCtx._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Initialize',
                            (['in'], POINTER(IBindCtx), 'pbc'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IInitializeWithBindCtx_INTERFACE_DEFINED__
            if not defined(__IShellItemFilter_INTERFACE_DEFINED__):
                __IShellItemFilter_INTERFACE_DEFINED__ = 1

                # interface IShellItemFilter

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IShellItemFilter._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'IncludeItem',
                            (['in'], POINTER(IShellItem), 'psi'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetEnumFlagsForItem',
                            (['in'], POINTER(IShellItem), 'psi'),
                            (['out'], POINTER(SHCONTF), 'pgrfFlags'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IShellItemFilter_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0127

            # [local]
        # END IF   (_WIN32_IE >= _WIN32_IE_IE70)
        if not defined(__INameSpaceTreeControl_INTERFACE_DEFINED__):
            __INameSpaceTreeControl_INTERFACE_DEFINED__ = 1

            # interface INameSpaceTreeControl

            # [uuid][object]

            # [v1_enum]


            class _NSTCSTYLE(ENUM):
                NSTCS_HASEXPANDOS = 0x1
                NSTCS_HASLINES = 0x2
                NSTCS_SINGLECLICKEXPAND = 0x4
                NSTCS_FULLROWSELECT = 0x8
                NSTCS_SPRINGEXPAND = 0x10
                NSTCS_HORIZONTALSCROLL = 0x20
                NSTCS_ROOTHASEXPANDO = 0x40
                NSTCS_SHOWSELECTIONALWAYS = 0x80
                NSTCS_NOINFOTIP = 0x200
                NSTCS_EVENHEIGHT = 0x400
                NSTCS_NOREPLACEOPEN = 0x800
                NSTCS_DISABLEDRAGDROP = 0x1000
                NSTCS_NOORDERSTREAM = 0x2000
                NSTCS_RICHTOOLTIP = 0x4000
                NSTCS_BORDER = 0x8000
                NSTCS_NOEDITLABELS = 0x10000
                NSTCS_TABSTOP = 0x20000
                NSTCS_FAVORITESMODE = 0x80000
                NSTCS_AUTOHSCROLL = 0x100000
                NSTCS_FADEINOUTEXPANDOS = 0x200000
                NSTCS_EMPTYTEXT = 0x400000
                NSTCS_CHECKBOXES = 0x800000
                NSTCS_PARTIALCHECKBOXES = 0x1000000
                NSTCS_EXCLUSIONCHECKBOXES = 0x2000000
                NSTCS_DIMMEDCHECKBOXES = 0x4000000
                NSTCS_NOINDENTCHECKS = 0x8000000
                NSTCS_ALLOWJUNCTIONS = 0x10000000
                NSTCS_SHOWTABSBUTTON = 0x20000000
                NSTCS_SHOWDELETEBUTTON = 0x40000000
                #~#~#~ NSTCS_SHOWREFRESHBUTTON    = ( INT  )0x80000000


            NSTCS_HASEXPANDOS = _NSTCSTYLE.NSTCS_HASEXPANDOS
            NSTCS_HASLINES = _NSTCSTYLE.NSTCS_HASLINES
            NSTCS_SINGLECLICKEXPAND = _NSTCSTYLE.NSTCS_SINGLECLICKEXPAND
            NSTCS_FULLROWSELECT = _NSTCSTYLE.NSTCS_FULLROWSELECT
            NSTCS_SPRINGEXPAND = _NSTCSTYLE.NSTCS_SPRINGEXPAND
            NSTCS_HORIZONTALSCROLL = _NSTCSTYLE.NSTCS_HORIZONTALSCROLL
            NSTCS_ROOTHASEXPANDO = _NSTCSTYLE.NSTCS_ROOTHASEXPANDO
            NSTCS_SHOWSELECTIONALWAYS = _NSTCSTYLE.NSTCS_SHOWSELECTIONALWAYS
            NSTCS_NOINFOTIP = _NSTCSTYLE.NSTCS_NOINFOTIP
            NSTCS_EVENHEIGHT = _NSTCSTYLE.NSTCS_EVENHEIGHT
            NSTCS_NOREPLACEOPEN = _NSTCSTYLE.NSTCS_NOREPLACEOPEN
            NSTCS_DISABLEDRAGDROP = _NSTCSTYLE.NSTCS_DISABLEDRAGDROP
            NSTCS_NOORDERSTREAM = _NSTCSTYLE.NSTCS_NOORDERSTREAM
            NSTCS_RICHTOOLTIP = _NSTCSTYLE.NSTCS_RICHTOOLTIP
            NSTCS_BORDER = _NSTCSTYLE.NSTCS_BORDER
            NSTCS_NOEDITLABELS = _NSTCSTYLE.NSTCS_NOEDITLABELS
            NSTCS_TABSTOP = _NSTCSTYLE.NSTCS_TABSTOP
            NSTCS_FAVORITESMODE = _NSTCSTYLE.NSTCS_FAVORITESMODE
            NSTCS_AUTOHSCROLL = _NSTCSTYLE.NSTCS_AUTOHSCROLL
            NSTCS_FADEINOUTEXPANDOS = _NSTCSTYLE.NSTCS_FADEINOUTEXPANDOS
            NSTCS_EMPTYTEXT = _NSTCSTYLE.NSTCS_EMPTYTEXT
            NSTCS_CHECKBOXES = _NSTCSTYLE.NSTCS_CHECKBOXES
            NSTCS_PARTIALCHECKBOXES = _NSTCSTYLE.NSTCS_PARTIALCHECKBOXES
            NSTCS_EXCLUSIONCHECKBOXES = _NSTCSTYLE.NSTCS_EXCLUSIONCHECKBOXES
            NSTCS_DIMMEDCHECKBOXES = _NSTCSTYLE.NSTCS_DIMMEDCHECKBOXES
            NSTCS_NOINDENTCHECKS = _NSTCSTYLE.NSTCS_NOINDENTCHECKS
            NSTCS_ALLOWJUNCTIONS = _NSTCSTYLE.NSTCS_ALLOWJUNCTIONS
            NSTCS_SHOWTABSBUTTON = _NSTCSTYLE.NSTCS_SHOWTABSBUTTON
            NSTCS_SHOWDELETEBUTTON = _NSTCSTYLE.NSTCS_SHOWDELETEBUTTON

            # [v1_enum]
            class _NSTCROOTSTYLE(ENUM):
                NSTCRS_VISIBLE = 0
                NSTCRS_HIDDEN = 0x1
                NSTCRS_EXPANDED = 0x2


            NSTCRS_VISIBLE = _NSTCROOTSTYLE.NSTCRS_VISIBLE
            NSTCRS_HIDDEN = _NSTCROOTSTYLE.NSTCRS_HIDDEN
            NSTCRS_EXPANDED = _NSTCROOTSTYLE.NSTCRS_EXPANDED

            # [v1_enum]
            class _NSTCITEMSTATE(ENUM):
                NSTCIS_NONE = 0
                NSTCIS_SELECTED = 0x1
                NSTCIS_EXPANDED = 0x2
                NSTCIS_BOLD = 0x4
                NSTCIS_DISABLED = 0x8
                NSTCIS_SELECTEDNOEXPAND = 0x10


            NSTCIS_NONE = _NSTCITEMSTATE.NSTCIS_NONE
            NSTCIS_SELECTED = _NSTCITEMSTATE.NSTCIS_SELECTED
            NSTCIS_EXPANDED = _NSTCITEMSTATE.NSTCIS_EXPANDED
            NSTCIS_BOLD = _NSTCITEMSTATE.NSTCIS_BOLD
            NSTCIS_DISABLED = _NSTCITEMSTATE.NSTCIS_DISABLED
            NSTCIS_SELECTEDNOEXPAND = _NSTCITEMSTATE.NSTCIS_SELECTEDNOEXPAND
            class NSTCGNI(ENUM):
                NSTCGNI_NEXT = 0
                NSTCGNI_NEXTVISIBLE = 1
                NSTCGNI_PREV = 2
                NSTCGNI_PREVVISIBLE = 3
                NSTCGNI_PARENT = 4
                NSTCGNI_CHILD = 5
                NSTCGNI_FIRSTVISIBLE = 6
                NSTCGNI_LASTVISIBLE = 7


            NSTCGNI_NEXT = NSTCGNI.NSTCGNI_NEXT
            NSTCGNI_NEXTVISIBLE = NSTCGNI.NSTCGNI_NEXTVISIBLE
            NSTCGNI_PREV = NSTCGNI.NSTCGNI_PREV
            NSTCGNI_PREVVISIBLE = NSTCGNI.NSTCGNI_PREVVISIBLE
            NSTCGNI_PARENT = NSTCGNI.NSTCGNI_PARENT
            NSTCGNI_CHILD = NSTCGNI.NSTCGNI_CHILD
            NSTCGNI_FIRSTVISIBLE = NSTCGNI.NSTCGNI_FIRSTVISIBLE
            NSTCGNI_LASTVISIBLE = NSTCGNI.NSTCGNI_LASTVISIBLE
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                INameSpaceTreeControl._methods_ = [
                    # temporary  insert empty text when folder is empty

                    #
                    #
                    #
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], HWND, 'hwndParent'),
                        (['unique', 'in'], POINTER(RECT), 'prc'),
                        ([], NSTCSTYLE, 'nsctsFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TreeAdvise',
                        (['in'], POINTER(IUnknown), 'punk'),
                        (['out'], POINTER(DWORD), 'pdwCookie'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TreeUnadvise',
                        (['in'], DWORD, 'dwCookie'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'AppendRoot',
                        (['in'], POINTER(IShellItem), 'psiRoot'),
                        ([], SHCONTF, 'grfEnumFlags'),
                        ([], NSTCROOTSTYLE, 'grfRootStyle'),
                        (['unique', 'in'], POINTER(IShellItemFilter), 'pif'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'InsertRoot',
                        (['in'], INT, 'iIndex'),
                        ([], POINTER(IShellItem), 'psiRoot'),
                        ([], SHCONTF, 'grfEnumFlags'),
                        ([], NSTCROOTSTYLE, 'grfRootStyle'),
                        (['unique', 'in'], POINTER(IShellItemFilter), 'pif'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveRoot',
                        (['in'], POINTER(IShellItem), 'psiRoot'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveAllRoots',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetRootItems',
                        (
                            ['out'],
                            POINTER(POINTER(IShellItemArray)),
                           'ppsiaRootItems'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetItemState',
                        (['in'], POINTER(IShellItem), 'psi'),
                        ([], NSTCITEMSTATE, 'nstcisMask'),
                        ([], NSTCITEMSTATE, 'nstcisFlags'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetItemState',
                        (['in'], POINTER(IShellItem), 'psi'),
                        ([], NSTCITEMSTATE, 'nstcisMask'),
                        (['out'], POINTER(NSTCITEMSTATE), 'pnstcisFlags'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetSelectedItems',
                        (
                            ['out'],
                            POINTER(POINTER(IShellItemArray)),
                           'psiaItems'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetItemCustomState',
                        (['in'], POINTER(IShellItem), 'psi'),
                        (['out'], POINTER(INT), 'piStateNumber'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetItemCustomState',
                        (['in'], POINTER(IShellItem), 'psi'),
                        ([], INT, 'iStateNumber'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnsureItemVisible',
                        (['in'], POINTER(IShellItem), 'psi'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetTheme',
                        (['in'], LPCWSTR, 'pszTheme'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetNextItem',
                        (['unique', 'in'], POINTER(IShellItem), 'psi'),
                        (['in'], NSTCGNI, 'nstcgi'),
                        (['out'], POINTER(POINTER(IShellItem)), 'ppsiNext'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'HitTest',
                        (['in'], POINTER(POINT), 'ppt'),
                        (['out'], POINTER(POINTER(IShellItem)), 'ppsiOut'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetItemRect',
                        (['in'], POINTER(IShellItem), 'psi'),
                        (['out'], POINTER(RECT), 'prect'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'CollapseAll',
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __INameSpaceTreeControl_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0128

        # [local]
        SID_SNavigationPane = IID_INameSpaceTreeControl

        if (NTDDI_VERSION >= NTDDI_VISTA):
            if not defined(__INameSpaceTreeControlFolderCapabilities_INTERFACE_DEFINED__):
                __INameSpaceTreeControlFolderCapabilities_INTERFACE_DEFINED__ = 1

                # interface INameSpaceTreeControlFolderCapabilities

                # [local][uuid][object]


                class NSTCFOLDERCAPABILITIES(ENUM):
                    NSTCFC_NONE = 0
                    NSTCFC_PINNEDITEMFILTERING = 0x1
                    NSTCFC_DELAY_REGISTER_NOTIFY = 0x2


                NSTCFC_NONE = NSTCFOLDERCAPABILITIES.NSTCFC_NONE
                NSTCFC_PINNEDITEMFILTERING = NSTCFOLDERCAPABILITIES.NSTCFC_PINNEDITEMFILTERING
                NSTCFC_DELAY_REGISTER_NOTIFY = NSTCFOLDERCAPABILITIES.NSTCFC_DELAY_REGISTER_NOTIFY
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][out]
                else: # C style interface
                    INameSpaceTreeControlFolderCapabilities._methods_ = [

                        # Supports filtering based on
                        # PKEY_IsPinnedToNameSpaceTree Delays registration for
                        # change notifications until expanded in navigation
                        # pane
                        #
                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __INameSpaceTreeControlFolderCapabilities_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0129

            # [local]
        # END IF   NTDDI_VISTA
        E_PREVIEWHANDLER_DRM_FAIL = _HRESULT_TYPEDEF_(0x86420001)
        E_PREVIEWHANDLER_NOAUTH = _HRESULT_TYPEDEF_(0x86420002)
        E_PREVIEWHANDLER_NOTFOUND = _HRESULT_TYPEDEF_(0x86420003)
        E_PREVIEWHANDLER_CORRUPT = _HRESULT_TYPEDEF_(0x86420004)

        if not defined(__IPreviewHandler_INTERFACE_DEFINED__):
            __IPreviewHandler_INTERFACE_DEFINED__ = 1

            # interface IPreviewHandler

            # [uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IPreviewHandler._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetWindow',
                        (['in'], HWND, 'hwnd'),
                        ([], POINTER(RECT), 'prc'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetRect',
                        (['in'], POINTER(RECT), 'prc'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'DoPreview',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Unload',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetFocus',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'QueryFocus',
                        (['out'], POINTER(HWND), 'phwnd'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TranslateAccelerator',
                        (['in'], POINTER(MSG), 'pmsg'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IPreviewHandler_INTERFACE_DEFINED__
        if not defined(__IPreviewHandlerFrame_INTERFACE_DEFINED__):
            __IPreviewHandlerFrame_INTERFACE_DEFINED__ = 1

            # interface IPreviewHandlerFrame

            # [unique][uuid][object]
            class PREVIEWHANDLERFRAMEINFO(ctypes.Structure):
                pass
            PREVIEWHANDLERFRAMEINFO._fields_ = [
                ('haccel', HACCEL),
                ('cAccelEntries', UINT),
            ]



            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IPreviewHandlerFrame._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetWindowContext',
                        (['out'], POINTER(PREVIEWHANDLERFRAMEINFO), 'pinfo'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'TranslateAccelerator',
                        (['in'], POINTER(MSG), 'pmsg'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IPreviewHandlerFrame_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0131

        # [local]
            if 0:
                pass
            # END IF   0
        if (NTDDI_VERSION >= NTDDI_VISTA):
            if defined(__cplusplus):
                REFEXPLORERPANE = EXPLORERPANE  &
        else: #  not __cplusplus
                REFEXPLORERPANE = EXPLORERPANE * __MIDL_CONST
            # END IF   __cplusplus

            if not defined(__IExplorerPaneVisibility_INTERFACE_DEFINED__):
                __IExplorerPaneVisibility_INTERFACE_DEFINED__ = 1

                # interface IExplorerPaneVisibility

                # [unique][local][uuid][object]

                # [v1_enum]


                class _EXPLORERPANESTATE(ENUM):
                    EPS_DONTCARE = 0
                    EPS_DEFAULT_ON = 0x1
                    EPS_DEFAULT_OFF = 0x2
                    EPS_STATEMASK = 0xFFFF
                    EPS_INITIALSTATE = 0x10000
                    EPS_FORCE = 0x20000


                EPS_DONTCARE = _EXPLORERPANESTATE.EPS_DONTCARE
                EPS_DEFAULT_ON = _EXPLORERPANESTATE.EPS_DEFAULT_ON
                EPS_DEFAULT_OFF = _EXPLORERPANESTATE.EPS_DEFAULT_OFF
                EPS_STATEMASK = _EXPLORERPANESTATE.EPS_STATEMASK
                EPS_INITIALSTATE = _EXPLORERPANESTATE.EPS_INITIALSTATE
                EPS_FORCE = _EXPLORERPANESTATE.EPS_FORCE
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][out]
                else: # C style interface
                    IExplorerPaneVisibility._methods_ = [

                        # ordinals don't impact the pane at all set its
                        # default state to "on", however user - modified
                        # persisted state is respected. " "
                        # " "off". flags not all ExplorerPanes will necessarily respect these flags ignore persisted state from the user, but user can still modify the state. user can't modify the state (i.e. hide affordances for show/hide). implies EPS_INITIALSTATE.
                        # 
                        # each pane has its own semantic, for example the
                        # NavPane is opt - out, so EPS_DONTCARE means you'll
                        # typically have the
                        # NavPane displayed, clients who want it to never show
                        # will pass EPS_DEFAULT_OFF | EPS_FORCE.
                        # QueryPane is opt - in, so it will only show for
                        # clients who pass EPS_DEFAULT_ON. however its default
                        # persisted state
                        # is "off" so if you want to force it on you have to
                        # pass EPS_DEFAULT_ON | EPS_INITIALSTATE.
                        # IExplorerPaneVisibility client can provide default
                        # states by returning EXPLORERPANESTATE here,
                        # failure of GetPaneState corresponds to EPS_DONTCARE.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetPaneState',
                            (
                                [annotation('_In_'), 'in'],
                                REFEXPLORERPANE,
                               'ep'
                            ),
                            (
                                ['out', annotation('_Out_')],
                                POINTER(EXPLORERPANESTATE),
                               'peps'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __IExplorerPaneVisibility_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0132

            # [local]
            SID_ExplorerPaneVisibility = IID_IExplorerPaneVisibility

            if not defined(__IContextMenuCB_INTERFACE_DEFINED__):
                __IContextMenuCB_INTERFACE_DEFINED__ = 1

                # interface IContextMenuCB

                # [local][unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                else: # C style interface
                    IContextMenuCB._methods_ = [
                        # uMsg is one of DFM_XXX values

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'CallBack',
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                POINTER(IShellFolder),
                               'psf'
                            ),
                            ([], HWND, 'hwndOwner'),
                            ([], POINTER(IDataObject), 'pdtobj'),
                            ([annotation('_In_'), 'in'], UINT, 'uMsg'),
                            ([], WPARAM, 'wParam'),
                            ([], LPARAM, 'lParam'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IContextMenuCB_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0133

            # [local]
        # END IF   NTDDI_VISTA
        if not defined(__IDefaultExtractIconInit_INTERFACE_DEFINED__):
            __IDefaultExtractIconInit_INTERFACE_DEFINED__ = 1

            # interface IDefaultExtractIconInit

            # [unique][local][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]
            else: # C style interface
                IDefaultExtractIconInit._methods_ = [
                    # set IExtractIcon GIL_XXX flags
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetFlags',
                        ([annotation('_In_'), 'in'], UINT, 'uFlags'),
                    ),

                    # set the registry key to load "DefaultIcon" value from                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetKey',
                        ([annotation('_In_'), 'in'], HKEY, 'hkey'),
                    ),

                    # set the various forms of icons, if pszFile is NULL iIcon
                    # is SHSTOCKICONID (SIID_) value
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetNormalIcon',
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            LPCWSTR,
                           'pszFile'
                        ),
                        ([annotation('_In_'), 'in'], INT, 'iIcon'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetOpenIcon',
                        (
                            ['unique', , annotation('_In_opt_'), 'in'],
                            LPCWSTR,
                           'pszFile'
                        ),
                        ([annotation('_In_'), 'in'], INT, 'iIcon'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetShortcutIcon',
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            LPCWSTR,
                           'pszFile'
                        ),
                        ([annotation('_In_'), 'in'], INT, 'iIcon'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetDefaultIcon',
                        (
                            [annotation('_In_opt_'), 'unique', , 'in'],
                            LPCWSTR,
                           'pszFile'
                        ),
                        ([annotation('_In_'), 'in'], INT, 'iIcon'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]

                # [annotation][string][unique][in]

                # [annotation][in]
            # END IF  C style interface
        # END IF  __IDefaultExtractIconInit_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0134

        # [local]
        if not defined(__IExplorerCommand_INTERFACE_DEFINED__):
            __IExplorerCommand_INTERFACE_DEFINED__ = 1

            # interface IExplorerCommand

            # [object][unique][uuid]

            # [v1_enum]


            class _EXPCMDSTATE(ENUM):
                ECS_ENABLED = 0
                ECS_DISABLED = 0x1
                ECS_HIDDEN = 0x2
                ECS_CHECKBOX = 0x4
                ECS_CHECKED = 0x8
                ECS_RADIOCHECK = 0x10


            ECS_ENABLED = _EXPCMDSTATE.ECS_ENABLED
            ECS_DISABLED = _EXPCMDSTATE.ECS_DISABLED
            ECS_HIDDEN = _EXPCMDSTATE.ECS_HIDDEN
            ECS_CHECKBOX = _EXPCMDSTATE.ECS_CHECKBOX
            ECS_CHECKED = _EXPCMDSTATE.ECS_CHECKED
            ECS_RADIOCHECK = _EXPCMDSTATE.ECS_RADIOCHECK

            # [v1_enum]
            class _EXPCMDFLAGS(ENUM):
                ECF_DEFAULT = 0
                ECF_HASSUBCOMMANDS = 0x1
                ECF_HASSPLITBUTTON = 0x2
                ECF_HIDELABEL = 0x4
                ECF_ISSEPARATOR = 0x8
                ECF_HASLUASHIELD = 0x10
                ECF_SEPARATORBEFORE = 0x20
                ECF_SEPARATORAFTER = 0x40
                ECF_ISDROPDOWN = 0x80
                ECF_TOGGLEABLE = 0x100
                ECF_AUTOMENUICONS = 0x200


            ECF_DEFAULT = _EXPCMDFLAGS.ECF_DEFAULT
            ECF_HASSUBCOMMANDS = _EXPCMDFLAGS.ECF_HASSUBCOMMANDS
            ECF_HASSPLITBUTTON = _EXPCMDFLAGS.ECF_HASSPLITBUTTON
            ECF_HIDELABEL = _EXPCMDFLAGS.ECF_HIDELABEL
            ECF_ISSEPARATOR = _EXPCMDFLAGS.ECF_ISSEPARATOR
            ECF_HASLUASHIELD = _EXPCMDFLAGS.ECF_HASLUASHIELD
            ECF_SEPARATORBEFORE = _EXPCMDFLAGS.ECF_SEPARATORBEFORE
            ECF_SEPARATORAFTER = _EXPCMDFLAGS.ECF_SEPARATORAFTER
            ECF_ISDROPDOWN = _EXPCMDFLAGS.ECF_ISDROPDOWN
            ECF_TOGGLEABLE = _EXPCMDFLAGS.ECF_TOGGLEABLE
            ECF_AUTOMENUICONS = _EXPCMDFLAGS.ECF_AUTOMENUICONS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IExplorerCommand._methods_ = [
                    #

                    # New for NTDDI_WIN8 New for NTDDI_WIN8                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetTitle',
                        (
                            ['unique', 'in'],
                            POINTER(IShellItemArray),
                           'psiItemArray'
                        ),
                        (['out'], POINTER(LPWSTR), 'ppszName'),
                    ),

                    # fill in ppszIcon with an icon resource strings format,
                    # for example "shell32, - 123"                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIcon',
                        (
                            ['unique', 'in'],
                            POINTER(IShellItemArray),
                           'psiItemArray'
                        ),
                        (['out', ], POINTER(LPWSTR), 'ppszIcon'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetToolTip',
                        (
                            ['unique', 'in'],
                            POINTER(IShellItemArray),
                           'psiItemArray'
                        ),
                        (['out', ], POINTER(LPWSTR), 'ppszInfotip'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCanonicalName',
                        (['out'], POINTER(GUID), 'pguidCommandName'),
                    ),

                    # Compute the visibility state of the verb here
                    # When "fOkToBeSlow" is FALSE this method must return
                    # quickly, in this case you can
                    # return E_PENDING and this object will be recreated on a
                    # background thread and called with
                    # fOkToBeSlow == TRUE where you can do expensive work.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetState',
                        (
                            ['unique', 'in'],
                            POINTER(IShellItemArray),
                           'psiItemArray'
                        ),
                        (['in'], BOOL, 'fOkToBeSlow'),
                        (['out'], POINTER(EXPCMDSTATE), 'pCmdState'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Invoke',
                        (
                            ['unique', 'in'],
                            POINTER(IShellItemArray),
                           'psiItemArray'
                        ),
                        ([], POINTER(IBindCtx), 'pbc'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFlags',
                        (['out'], POINTER(EXPCMDFLAGS), 'pFlags'),
                    ),

                    # If GetFlags() returned ECF_HASSUBCOMMANDS this will be
                    # used to discover the sub commands.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'EnumSubCommands',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumExplorerCommand)),
                           'ppEnum'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IExplorerCommand_INTERFACE_DEFINED__
        if not defined(__IExplorerCommandState_INTERFACE_DEFINED__):
            __IExplorerCommandState_INTERFACE_DEFINED__ = 1

            # interface IExplorerCommandState

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IExplorerCommandState._methods_ = [
                    # Compute the visibility state of the verb here

                    # When "fOkToBeSlow" is FALSE this method must return
                    # quickly, in this case you can
                    # return E_PENDING and this object will be recreated on a
                    # background thread and called with
                    # fOkToBeSlow == TRUE where you can do expensive work.
                    # this method has the same semantics as
                    # IExplorerCommand::GetState()                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetState',
                        (['in'], POINTER(IShellItemArray), 'psiItemArray'),
                        ([], BOOL, 'fOkToBeSlow'),
                        (['out'], POINTER(EXPCMDSTATE), 'pCmdState'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IExplorerCommandState_INTERFACE_DEFINED__
        if not defined(__IInitializeCommand_INTERFACE_DEFINED__):
            __IInitializeCommand_INTERFACE_DEFINED__ = 1

            # interface IInitializeCommand

            # [unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IInitializeCommand._methods_ = [

                    # pszCommandName - This parameter is the verb that this
                    # handler instance is
                    # being created for. If the same handler is used for
                    # different verbs this lets the
                    # handler have different behavior for different verbs.
                    # ppb - This parameter provides access to values stored in
                    # the registry under the verb.
                    # These values can be used to control the behavior of the
                    # verb handler for
                    # different verb isntances.
                    # Another property bag can be used to share state between
                    # handler instances. This can be
                    # accessed by implementing IObjectWithSite and then
                    # querying the site for SID_CommandsPropertyBag.                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], LPCWSTR, 'pszCommandName'),
                        (['in'], POINTER(IPropertyBag), 'ppb'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IInitializeCommand_INTERFACE_DEFINED__
        if not defined(__IEnumExplorerCommand_INTERFACE_DEFINED__):
            __IEnumExplorerCommand_INTERFACE_DEFINED__ = 1

            # interface IEnumExplorerCommand

            # [unique][object][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][in]

                # [annotation][length_is][size_is][out]

                # [annotation][out]
            else: # C style interface
                IEnumExplorerCommand._methods_ = [
                    #
                
                    COMMETHOD(
                        ['local'],
                        HRESULT,
                        'Next',
                        ([annotation('_In_'), 'in'], ULONG, 'celt'),
                        (
                            ['out', annotation('_Out_writes_to_(celt, *pceltFetched)), 'in', 'out'],
                            POINTER(POINTER(IExplorerCommand)),
                           'pUICommand'
                        ),
                        (
                            ['out', annotation('_Out_opt_ _Deref_out_range_(0, celt))],
                            POINTER(ULONG),
                           'pceltFetched'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoteNext',
                        (['in'], ULONG, 'celt'),
                        (
                            ['out', 'in', 'out'],
                            POINTER(POINTER(IExplorerCommand)),
                           'pUICommand'
                        ),
                        (['out'], POINTER(ULONG), 'pceltFetched'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Skip',
                        (['in'], ULONG, 'celt'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Reset',
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Clone',
                        (
                            ['out'],
                            POINTER(POINTER(IEnumExplorerCommand)),
                           'ppenum'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][in]

                # [annotation][length_is][size_is][out]

                # [annotation][out]
            # END IF  C style interface
        # END IF  __IEnumExplorerCommand_INTERFACE_DEFINED__
        if not defined(__IExplorerCommandProvider_INTERFACE_DEFINED__):
            __IExplorerCommandProvider_INTERFACE_DEFINED__ = 1

            # interface IExplorerCommandProvider

            # [object][unique][uuid]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IExplorerCommandProvider._methods_ = [
                    # IEnumExplorerCommand

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCommands',
                        (['in'], POINTER(IUnknown), 'punkSite'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # IExplorerCommand
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCommand',
                        (['in'], REFGUID, 'rguidCommandId'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IExplorerCommandProvider_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0139

        # [local]
        class CPVIEW(ENUM):
            CPVIEW_CLASSIC = 0
            CPVIEW_ALLITEMS = CPVIEW_CLASSIC
            CPVIEW_CATEGORY = 1
            CPVIEW_HOME = CPVIEW_CATEGORY


        CPVIEW_CLASSIC = CPVIEW.CPVIEW_CLASSIC
        CPVIEW_ALLITEMS = CPVIEW.CPVIEW_ALLITEMS
        CPVIEW_CATEGORY = CPVIEW.CPVIEW_CATEGORY
        CPVIEW_HOME = CPVIEW.CPVIEW_HOME
        if not defined(__IOpenControlPanel_INTERFACE_DEFINED__):
            __IOpenControlPanel_INTERFACE_DEFINED__ = 1

            # interface IOpenControlPanel

            # [uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IOpenControlPanel._methods_ = [
                    #
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Open',
                        (['unique', , 'in'], LPCWSTR, 'pszName'),
                        ([], LPCWSTR, 'pszPage'),
                        (['unique', 'in'], POINTER(IUnknown), 'punkSite'),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetPath',
                        (['unique', , 'in'], LPCWSTR, 'pszName'),
                        (['out'], LPWSTR, 'pszPath'),
                        (['in'], UINT, 'cchPath'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetCurrentView',
                        (['out'], POINTER(CPVIEW), 'pView'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IOpenControlPanel_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0140

        # [local]
        STR_FILE_SYS_BIND_DATA = "File System Bind Data"
        STR_FILE_SYS_BIND_DATA_WIN7_FORMAT = "Win7FileSystemIdList"

        if not defined(__IFileSystemBindData_INTERFACE_DEFINED__):
            __IFileSystemBindData_INTERFACE_DEFINED__ = 1

            # interface IFileSystemBindData

            # [local][unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IFileSystemBindData._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetFindData',
                        (['in'], POINTER(WIN32_FIND_DATAW), 'pfd'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFindData',
                        (['out'], POINTER(WIN32_FIND_DATAW), 'pfd'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IFileSystemBindData_INTERFACE_DEFINED__
        if not defined(__IFileSystemBindData2_INTERFACE_DEFINED__):
            __IFileSystemBindData2_INTERFACE_DEFINED__ = 1

            # interface IFileSystemBindData2

            # [local][unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IFileSystemBindData2._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetFileID',
                        (['in'], LARGE_INTEGER, 'liFileID'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFileID',
                        (['out'], POINTER(LARGE_INTEGER), 'pliFileID'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetJunctionCLSID',
                        (['in'], REFCLSID, 'clsid'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetJunctionCLSID',
                        (['out'], POINTER(CLSID), 'pclsid'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IFileSystemBindData2_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0142

        # [local]
        if (NTDDI_VERSION >= NTDDI_WIN7):
            if not defined(__ICustomDestinationList_INTERFACE_DEFINED__):
                __ICustomDestinationList_INTERFACE_DEFINED__ = 1

                # interface ICustomDestinationList

                # [unique][object][uuid]


                class KNOWNDESTCATEGORY(ENUM):
                    KDC_FREQUENT = 1
                    #~#~#~ KDC_RECENT    = ( KDC_FREQUENT + 1 )


                KDC_FREQUENT = KNOWNDESTCATEGORY.KDC_FREQUENT
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    ICustomDestinationList._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetAppID',
                            (['in'], LPCWSTR, 'pszAppID'),
                        ),

                        # Retrieve IObjectArray of IShellItems or IShellLinks
                        # that represent removed destinations
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'BeginList',
                            (['out'], POINTER(UINT), 'pcMinSlots'),
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AppendCategory',
                            (['in'], LPCWSTR, 'pszCategory'),
                            (['in'], POINTER(IObjectArray), 'poa'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AppendKnownCategory',
                            (['in'], KNOWNDESTCATEGORY, 'category'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AddUserTasks',
                            (['in'], POINTER(IObjectArray), 'poa'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'CommitList',
                        ),

                        # Retrieve IObjectCollection of IShellItems
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetRemovedDestinations',
                            (['in'], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DeleteList',
                            (['unique', 'in'], LPCWSTR, 'pszAppID'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AbortList',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __ICustomDestinationList_INTERFACE_DEFINED__
            if not defined(__IApplicationDestinations_INTERFACE_DEFINED__):
                __IApplicationDestinations_INTERFACE_DEFINED__ = 1

                # interface IApplicationDestinations

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IApplicationDestinations._methods_ = [

                        # Set the App User Model ID for the application
                        # removing destinations from its list. If an AppID is
                        # not provided
                        # via this method, the system will use a heuristically
                        # determined ID. This method must be called before
                        # RemoveDestination or RemoveAllDestinations.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetAppID',
                            (['in'], LPCWSTR, 'pszAppID'),
                        ),

                        # Remove an IShellItem or an IShellLink from the
                        # automatic destination list                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoveDestination',
                            (['in'], POINTER(IUnknown), 'punk'),
                        ),

                        # Clear the frequent and recent destination lists for
                        # this application.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RemoveAllDestinations',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IApplicationDestinations_INTERFACE_DEFINED__
            if not defined(__IApplicationDocumentLists_INTERFACE_DEFINED__):
                __IApplicationDocumentLists_INTERFACE_DEFINED__ = 1

                # interface IApplicationDocumentLists

                # [unique][object][uuid]


                class APPDOCLISTTYPE(ENUM):
                    ADLT_RECENT = 0
                    #~#~#~ ADLT_FREQUENT    = ( ADLT_RECENT + 1 )


                ADLT_RECENT = APPDOCLISTTYPE.ADLT_RECENT
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IApplicationDocumentLists._methods_ = [

                        # The recently used documents list The frequently used
                        # documents list
                        # Set the App User Model ID for the application
                        # retrieving this list. If an AppID is not provided
                        # via this method,
                        # the system will use a heuristically determined ID.
                        # This method must be called before GetList.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetAppID',
                            (['in'], LPCWSTR, 'pszAppID'),
                        ),

                        # Retrieve an IEnumObjects or IObjectArray for
                        # IShellItems and/or IShellLinks.
                        # Items may appear in both the frequent and recent
                        # lists.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetList',
                            (['in'], APPDOCLISTTYPE, 'listtype'),
                            ([], UINT, 'cItemsDesired'),
                            ([], REFIID, 'riid'),
                            (['out'], POINTER(POINTER(VOID)), 'ppv'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IApplicationDocumentLists_INTERFACE_DEFINED__
            if not defined(__IObjectWithAppUserModelID_INTERFACE_DEFINED__):
                __IObjectWithAppUserModelID_INTERFACE_DEFINED__ = 1

                # interface IObjectWithAppUserModelID

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IObjectWithAppUserModelID._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetAppID',
                            (['in'], LPCWSTR, 'pszAppID'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetAppID',
                            (['out'], POINTER(LPWSTR), 'ppszAppID'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IObjectWithAppUserModelID_INTERFACE_DEFINED__
            if not defined(__IObjectWithProgID_INTERFACE_DEFINED__):
                __IObjectWithProgID_INTERFACE_DEFINED__ = 1

                # interface IObjectWithProgID

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IObjectWithProgID._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetProgID',
                            (['in'], LPCWSTR, 'pszProgID'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetProgID',
                            (['out'], POINTER(LPWSTR), 'ppszProgID'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IObjectWithProgID_INTERFACE_DEFINED__
            if not defined(__IUpdateIDList_INTERFACE_DEFINED__):
                __IUpdateIDList_INTERFACE_DEFINED__ = 1

                # interface IUpdateIDList

                # [object][unique][local][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][out]
                else: # C style interface
                    IUpdateIDList._methods_ = [

                        # Implemented by an IShellFolder implementation, this
                        # method updates the provided child IDList based on the
                        # parameters specified by the provided IBindCtx. If
                        # pbc is NULL, or does not contain any parameters that
                        # apply to the current Shell Folder, pidlIn should
                        # simply be cloned into ppidlOut.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Update',
                            (
                                ['unique', annotation('_In_opt_'), 'in'],
                                POINTER(IBindCtx),
                               'pbc'
                            ),
                            (
                                [annotation('_In_'), 'in'],
                                PCUITEMID_CHILD,
                               'pidlIn'
                            ),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(PITEMID_CHILD),
                               'ppidlOut'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][unique][in]

                    # [annotation][in]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __IUpdateIDList_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0148

            # [local]
        # END IF   NTDDI_WIN7
        if (NTDDI_VERSION >= NTDDI_WIN8):
            if not defined(__IDesktopWallpaper_INTERFACE_DEFINED__):
                __IDesktopWallpaper_INTERFACE_DEFINED__ = 1

                # interface IDesktopWallpaper

                # [object][uuid]


                class DESKTOP_SLIDESHOW_OPTIONS(ENUM):
                    DSO_SHUFFLEIMAGES = 0x1


                DSO_SHUFFLEIMAGES = DESKTOP_SLIDESHOW_OPTIONS.DSO_SHUFFLEIMAGES
                class DESKTOP_SLIDESHOW_STATE(ENUM):
                    DSS_ENABLED = 0x1
                    DSS_SLIDESHOW = 0x2
                    DSS_DISABLED_BY_REMOTE_SESSION = 0x4


                DSS_ENABLED = DESKTOP_SLIDESHOW_STATE.DSS_ENABLED
                DSS_SLIDESHOW = DESKTOP_SLIDESHOW_STATE.DSS_SLIDESHOW
                DSS_DISABLED_BY_REMOTE_SESSION = DESKTOP_SLIDESHOW_STATE.DSS_DISABLED_BY_REMOTE_SESSION
                class DESKTOP_SLIDESHOW_DIRECTION(ENUM):
                    DSD_FORWARD = 0
                    DSD_BACKWARD = 1


                DSD_FORWARD = DESKTOP_SLIDESHOW_DIRECTION.DSD_FORWARD
                DSD_BACKWARD = DESKTOP_SLIDESHOW_DIRECTION.DSD_BACKWARD
                class DESKTOP_WALLPAPER_POSITION(ENUM):
                    DWPOS_CENTER = 0
                    DWPOS_TILE = 1
                    DWPOS_STRETCH = 2
                    DWPOS_FIT = 3
                    DWPOS_FILL = 4
                    DWPOS_SPAN = 5


                DWPOS_CENTER = DESKTOP_WALLPAPER_POSITION.DWPOS_CENTER
                DWPOS_TILE = DESKTOP_WALLPAPER_POSITION.DWPOS_TILE
                DWPOS_STRETCH = DESKTOP_WALLPAPER_POSITION.DWPOS_STRETCH
                DWPOS_FIT = DESKTOP_WALLPAPER_POSITION.DWPOS_FIT
                DWPOS_FILL = DESKTOP_WALLPAPER_POSITION.DWPOS_FILL
                DWPOS_SPAN = DESKTOP_WALLPAPER_POSITION.DWPOS_SPAN
                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IDesktopWallpaper._methods_ = [

                        # This enumeration is used to set and get slideshow
                        # options.
                        # When set, indicates that the order in which images
                        # in the slideshow are displayed can be randomized.
                        # This enumeration is used by GetStatus to indicate
                        # the current status of the slideshow. Slideshows are
                        # enabled. This is normally true, unless the Enable
                        # method is used. A slideshow is currently configured
                        # (e.g., using SetSlideshow). A remote session has
                        # temporarily disabled the slideshow
                        # This enumeration is used by the AdvanceSlideshow
                        # method to indicate whether to advance the slideshow
                        # forward or backward. Advance slideshow forward.
                        # Advance slideshow backward.
                        # This enumeration indicates the wallpaper position
                        # for all monitors.
                        # (This includes when slideshows are running.)
                        # The wallpaper position specifies how the image that
                        # is asINT to a monitor should be displayed.
                        # Center the image, do not stretch
                        # (WPSTYLE_CENTER in IActiveDesktop). Tile the image
                        # across all monitors
                        # (WPSTYLE_TILE in IActiveDesktop). Stretch the image
                        # to exactly fit on the monitor
                        # (WPSTYLE_STRETCH in IActiveDesktop). Stretch the
                        # image to exactly the height or width of the monitor
                        # without changing its aspect ratio or cropping
                        # (WPSTYLE_KEEPASPECT in IActiveDesktop). This often
                        # results in letterbox bars on the sides or top/bottom
                        # of the image. Like DWPOS_FIT, but stretches the
                        # image until it completely fills the screen, allowing
                        # cropping to aVOID letterbox bars
                        # (WPSTYLE_CROPTOFIT in IActiveDesktop). Spans a
                        # single image (new, no IActiveDesktop equivalent).
                        # These methods allow the wallpaper to be set and get
                        # for each monitor. The first parameter indicates the
                        # monitor by its
                        # identifier (obtained with GetMonitorDevicePathAt)
                        # and the second a path to the wallpaper. If NULL is
                        # passed as the monitor
                        # identifier to SetWallpaper, then that wallpaper will
                        # be set for all monitors. Passing NULL as the monitor
                        # identifier to
                        # GetWallpaper will return S_OK and a valid wallpaper
                        # path if all monitors are displaying the same image,
                        # or S_FALSE and an
                        # empty string if they are not
                        # (i.e., there are multiple static images on each monitor or a slideshow is running). An empty
                        # 
                        # wallpaper string indicates no image, or a monitor
                        # that is displaying the system color for the
                        # background.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetWallpaper',
                            (['unique', 'in'], LPCWSTR, 'monitorID'),
                            (['in'], LPCWSTR, 'wallpaper'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetWallpaper',
                            (['unique', 'in'], LPCWSTR, 'monitorID'),
                            (['out'], POINTER(LPWSTR), 'wallpaper'),
                        ),

                        # These methods allow the monitor count and a unique
                        # identifier for each monitor to be obtained.
                        # This includes monitors that are currently detached
                        # but have an image asINT to them; such a monitor
                        # would display its asINT image when it is reattached.
                        # Use GetMonitorRECT to distinguish between
                        # attached and detached monitors.
                        # Note that these methods wrap existing CCD library
                        # functionality.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetMonitorDevicePathAt',
                            (['in'], UINT, 'monitorIndex'),
                            (['out', ], POINTER(LPWSTR), 'monitorID'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetMonitorDevicePathCount',
                            (['out'], POINTER(UINT), 'count'),
                        ),

                        # This method allows the display rectangle of the
                        # specified monitor to be obtained, in screen
                        # coordinates. If the monitor
                        # is not currently attached, it will return S_FALSE
                        # and an empty RECT. Checking for S_FALSE is a valid
                        # way to determine
                        # which monitors are currently attached to the system.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetMonitorRECT',
                            (['in'], LPCWSTR, 'monitorID'),
                            (['out'], POINTER(RECT), 'displayRect'),
                        ),

                        # These are callthroughs to
                        # SetSysColor(COLOR_BACKGROUND) and
                        # GetSysColor(COLOR_BACKGROUND).
                        # This is the color that is visible on the desktop
                        # when no image is currently displayed or when the
                        # Enable method is used to disable the background. The
                        # color will also be visible when the wallpaper does
                        # not
                        # fill the entire monitor
                        # (e.g., often when the wallpaper position is Fit or Center).
                        #                     
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetBackgroundColor',
                            (['in'], COLORREF, 'color'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetBackgroundColor',
                            (['out'], POINTER(COLORREF), 'color'),
                        ),

                        # These methods allow the wallpaper position to be set
                        # and get, as indicated by the
                        # DESKTOP_WALLPAPER_POSITION enumeration.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetPosition',
                            (['in'], DESKTOP_WALLPAPER_POSITION, 'position'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetPosition',
                            (
                                ['out'],
                                POINTER(DESKTOP_WALLPAPER_POSITION),
                               'position'
                            ),
                        ),

                        # These methods are used to set and get the items that
                        # will be displayed in a slideshow. When setting the
                        # slideshow,
                        # the IShellItemArray can specify either a set of
                        # items that are all part of the same container or a
                        # single item that
                        # is itself a container; any other IShellItemArray
                        # will cause SetSlideshow to fail.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSlideshow',
                            (['in'], POINTER(IShellItemArray), 'items'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSlideshow',
                            (
                                ['out'],
                                POINTER(POINTER(IShellItemArray)),
                               'items'
                            ),
                        ),

                        # These methods are used to set and get the slideshow
                        # options that are part of the
                        # DESKTOP_SLIDESHOW_OPTIONS
                        # enumeration, as well as the slideshow "tick"
                        # (the interval between slideshow background image transitions), in milliseconds.
                        #                     
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetSlideshowOptions',
                            (['in'], DESKTOP_SLIDESHOW_OPTIONS, 'options'),
                            ([], UINT, 'slideshowTick'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetSlideshowOptions',
                            (
                                ['out'],
                                POINTER(DESKTOP_SLIDESHOW_OPTIONS),
                               'options'
                            ),
                            ([], POINTER(UINT), 'slideshowTick'),
                        ),

                        # Call this method to advance the slideshow. The first
                        # parameter indicates the monitor to change; when
                        # NULL, it advances the
                        # monitor that would be expected to change on the next
                        # tick of the slideshow. The second parameter uses the
                        # DESKTOP_SLIDESHOW_DIRECTION enumeration to indicate
                        # whether to advance the slideshow forward or backward.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AdvanceSlideshow',
                            (['unique', 'in'], LPCWSTR, 'monitorID'),
                            (
                                ['in'],
                                DESKTOP_SLIDESHOW_DIRECTION,
                               'direction'
                            ),
                        ),

                        # This method returns the current status of the
                        # slideshow, as indicated by the
                        # DESKTOP_SLIDESHOW_STATE enumeration.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetStatus',
                            (
                                ['out'],
                                POINTER(DESKTOP_SLIDESHOW_STATE),
                               'state'
                            ),
                        ),

                        # This method allows the desktop background to be
                        # enabled or disabled, depending on the
                        # value of the argument. This is primarily intended
                        # for situations such as terminal server
                        # where it may be desirable to disable the background
                        # for performance reasons.
                        # Note that a call to SetWallpaper or SetSlideshow
                        # will re - enable the background even if it
                        # is disabled by this method.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Enable',
                            (['in'], BOOL, 'enable'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IDesktopWallpaper_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0149

            # [local]
        # END IF   NTDDI_WIN8
        HOMEGROUP_SECURITY_GROUP_MULTI = "HUG"
        HOMEGROUP_SECURITY_GROUP = "HomeUsers"

        if not defined(__IHomeGroup_INTERFACE_DEFINED__):
            __IHomeGroup_INTERFACE_DEFINED__ = 1

            # interface IHomeGroup

            # [local][object][uuid]


            class HOMEGROUPSHARINGCHOICES(ENUM):
                HGSC_NONE = 0
                HGSC_MUSICLIBRARY = 0x1
                HGSC_PICTURESLIBRARY = 0x2
                HGSC_VIDEOSLIBRARY = 0x4
                HGSC_DOCUMENTSLIBRARY = 0x8
                HGSC_PRINTERS = 0x10


            HGSC_NONE = HOMEGROUPSHARINGCHOICES.HGSC_NONE
            HGSC_MUSICLIBRARY = HOMEGROUPSHARINGCHOICES.HGSC_MUSICLIBRARY
            HGSC_PICTURESLIBRARY = HOMEGROUPSHARINGCHOICES.HGSC_PICTURESLIBRARY
            HGSC_VIDEOSLIBRARY = HOMEGROUPSHARINGCHOICES.HGSC_VIDEOSLIBRARY
            HGSC_DOCUMENTSLIBRARY = HOMEGROUPSHARINGCHOICES.HGSC_DOCUMENTSLIBRARY
            HGSC_PRINTERS = HOMEGROUPSHARINGCHOICES.HGSC_PRINTERS
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IHomeGroup._methods_ = [
                    #

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ShowSharingWizard',
                        (['in'], HWND, 'owner'),
                        (
                            ['out'],
                            POINTER(HOMEGROUPSHARINGCHOICES),
                           'sharingchoices'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IHomeGroup_INTERFACE_DEFINED__
        if not defined(__IInitializeWithPropertyStore_INTERFACE_DEFINED__):
            __IInitializeWithPropertyStore_INTERFACE_DEFINED__ = 1

            # interface IInitializeWithPropertyStore

            # [unique][object][uuid][helpstring]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IInitializeWithPropertyStore._methods_ = [
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], POINTER(IPropertyStore), 'pps'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IInitializeWithPropertyStore_INTERFACE_DEFINED__
        if not defined(__IOpenSearchSource_INTERFACE_DEFINED__):
            __IOpenSearchSource_INTERFACE_DEFINED__ = 1

            # interface IOpenSearchSource

            # [unique][object][uuid][helpstring]

            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IOpenSearchSource._methods_ = [
                    # return IStream
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetResults',
                        (['in'], HWND, 'hwnd'),
                        ([], LPCWSTR, 'pszQuery'),
                        ([], DWORD, 'dwStartIndex'),
                        ([], DWORD, 'dwCount'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IOpenSearchSource_INTERFACE_DEFINED__
        if not defined(__IShellLibrary_INTERFACE_DEFINED__):
            __IShellLibrary_INTERFACE_DEFINED__ = 1

            # interface IShellLibrary

            # [unique][object][uuid][helpstring]


            class LIBRARYFOLDERFILTER(ENUM):
                LFF_FORCEFILESYSTEM = 1
                LFF_STORAGEITEMS = 2
                LFF_ALLITEMS = 3


            LFF_FORCEFILESYSTEM = LIBRARYFOLDERFILTER.LFF_FORCEFILESYSTEM
            LFF_STORAGEITEMS = LIBRARYFOLDERFILTER.LFF_STORAGEITEMS
            LFF_ALLITEMS = LIBRARYFOLDERFILTER.LFF_ALLITEMS
            class LIBRARYOPTIONFLAGS(ENUM):
                LOF_DEFAULT = 0
                LOF_PINNEDTONAVPANE = 0x1
                LOF_MASK_ALL = 0x1


            LOF_DEFAULT = LIBRARYOPTIONFLAGS.LOF_DEFAULT
            LOF_PINNEDTONAVPANE = LIBRARYOPTIONFLAGS.LOF_PINNEDTONAVPANE
            LOF_MASK_ALL = LIBRARYOPTIONFLAGS.LOF_MASK_ALL
            class DEFAULTSAVEFOLDERTYPE(ENUM):
                DSFT_DETECT = 1
                #~#~#~ DSFT_PRIVATE    = ( DSFT_DETECT + 1 )
                #~#~#~ DSFT_PUBLIC    = ( DSFT_PRIVATE + 1 )


            DSFT_DETECT = DEFAULTSAVEFOLDERTYPE.DSFT_DETECT
            class LIBRARYSAVEFLAGS(ENUM):
                LSF_FAILIFTHERE = 0
                LSF_OVERRIDEEXISTING = 0x1
                LSF_MAKEUNIQUENAME = 0x2


            LSF_FAILIFTHERE = LIBRARYSAVEFLAGS.LSF_FAILIFTHERE
            LSF_OVERRIDEEXISTING = LIBRARYSAVEFLAGS.LSF_OVERRIDEEXISTING
            LSF_MAKEUNIQUENAME = LIBRARYSAVEFLAGS.LSF_MAKEUNIQUENAME
            if defined(__cplusplus) and not defined(CINTERFACE):
                pass
            else: # C style interface
                IShellLibrary._methods_ = [

                    # Return only file system items. Return any items that can
                    # be bound to an IStorage. (default) Return all items.
                    # Specifies that this library is pinned to the navigation
                    # pane.
                    # Specifies the save folder for the current user depending
                    # on whether or not they are the owner of the library
                    # Specifies the private save folder for the owner of the
                    # library Specifies the public save folder for non -
                    # owners of the library
                    # if a library with the same name exists fail to save will
                    # override existing library with the same name if there or
                    # create a new one if not if a library with the same name
                    # exists create a unique name by adding a number in
                    # parenthesis
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'LoadLibraryFromKnownFolder',
                        (['in'], REFKNOWNFOLDERID, 'kfidLibrary'),
                        ([], DWORD, 'grfMode'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'AddFolder',
                        (['in'], POINTER(IShellItem), 'psiLocation'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'RemoveFolder',
                        (['in'], POINTER(IShellItem), 'psiLocation'),
                    ),

                    # may return S_FALSE if some folders were omitted due to
                    # errors during enumeration
                    # returns IShellItemArray                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFolders',
                        (['in'], LIBRARYFOLDERFILTER, 'lff'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # returns S_FALSE if no resolution was necessary; resolved
                    # folder will not be saved until Save[InKnownFolder] or
                    # Commit is called
                    # returns IShellItem                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'ResolveFolder',
                        (['in'], POINTER(IShellItem), 'psiFolderToResolve'),
                        ([], DWORD, 'dwTimeout'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),

                    # returns IShellItem                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetDefaultSaveFolder',
                        (['in'], DEFAULTSAVEFOLDERTYPE, 'dsft'),
                        ([], REFIID, 'riid'),
                        (['out'], POINTER(POINTER(VOID)), 'ppv'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetDefaultSaveFolder',
                        (['in'], DEFAULTSAVEFOLDERTYPE, 'dsft'),
                        ([], POINTER(IShellItem), 'psi'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetOptions',
                        (['out'], POINTER(LIBRARYOPTIONFLAGS), 'plofOptions'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetOptions',
                        (['in'], LIBRARYOPTIONFLAGS, 'lofMask'),
                        ([], LIBRARYOPTIONFLAGS, 'lofOptions'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetFolderType',
                        (['out'], POINTER(FOLDERTYPEID), 'pftid'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetFolderType',
                        (['in'], REFFOLDERTYPEID, 'ftid'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetIcon',
                        (['out'], POINTER(LPWSTR), 'ppszIcon'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetIcon',
                        (['in'], LPCWSTR, 'pszIcon'),
                    ),
                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Commit',
                    ),

                    # name without an extension                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Save',
                        (['in'], POINTER(IShellItem), 'psiFolderToSaveIn'),
                        (['in'], LPCWSTR, 'pszLibraryName'),
                        ([], LIBRARYSAVEFLAGS, 'lsf'),
                        (
                            ['out'],
                            POINTER(POINTER(IShellItem)),
                           'ppsiSavedTo'
                        ),
                    ),

                    # name without an extension                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SaveInKnownFolder',
                        (['in'], REFKNOWNFOLDERID, 'kfidToSaveIn'),
                        (['in'], LPCWSTR, 'pszLibraryName'),
                        ([], LIBRARYSAVEFLAGS, 'lsf'),
                        (
                            ['out'],
                            POINTER(POINTER(IShellItem)),
                           'ppsiSavedTo'
                        ),
                    ),

                    #                ]


                # [annotation][iid_is][out]
            # END IF  C style interface
        # END IF  __IShellLibrary_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0153

        # [local]
        class DEFAULT_FOLDER_MENU_RESTRICTIONS(ENUM):
            DFMR_DEFAULT = 0
            DFMR_NO_STATIC_VERBS = 0x8
            DFMR_STATIC_VERBS_ONLY = 0x10
            DFMR_NO_RESOURCE_VERBS = 0x20
            DFMR_OPTIN_HANDLERS_ONLY = 0x40
            DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY = 0x80
            DFMR_USE_SPECIFIED_HANDLERS = 0x100
            DFMR_USE_SPECIFIED_VERBS = 0x200
            DFMR_NO_ASYNC_VERBS = 0x400
            DFMR_NO_NATIVECPU_VERBS = 0x800


        DFMR_DEFAULT = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_DEFAULT
        DFMR_NO_STATIC_VERBS = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_NO_STATIC_VERBS
        DFMR_STATIC_VERBS_ONLY = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_STATIC_VERBS_ONLY
        DFMR_NO_RESOURCE_VERBS = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_NO_RESOURCE_VERBS
        DFMR_OPTIN_HANDLERS_ONLY = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_OPTIN_HANDLERS_ONLY
        DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY
        DFMR_USE_SPECIFIED_HANDLERS = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_USE_SPECIFIED_HANDLERS
        DFMR_USE_SPECIFIED_VERBS = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_USE_SPECIFIED_VERBS
        DFMR_NO_ASYNC_VERBS = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_NO_ASYNC_VERBS
        DFMR_NO_NATIVECPU_VERBS = DEFAULT_FOLDER_MENU_RESTRICTIONS.DFMR_NO_NATIVECPU_VERBS
        if not defined(__IDefaultFolderMenuInitialize_INTERFACE_DEFINED__):
            __IDefaultFolderMenuInitialize_INTERFACE_DEFINED__ = 1

            # interface IDefaultFolderMenuInitialize

            # [local][unique][uuid][object]

            if defined(__cplusplus) and not defined(CINTERFACE):

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][size_is][unique][in]
            else: # C style interface
                IDefaultFolderMenuInitialize._methods_ = [

                    # Set context menu info
                    # (equivalent to struct DEFCONTEXTMENU).
                    # Do not use this method to reinitialize a context menu.
                    # Use IShellExtInit::Initialize instead.
                    # Optional: callback object Optional: IDList to folder of
                    # the items, computed from psf if NULL Optional: folder of
                    # the items Count of items in apidl Items operating on,
                    # used to get IDataObject and IAssociationArray Optional:
                    # IQueryAssociations, specifies where to load extensions
                    # from, computed from apidl if NULL Count of items in
                    # aKeys, may be zero Optional: specifies where to load
                    # extensions from                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'Initialize',
                        (['in'], HWND, 'hwnd'),
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            POINTER(IContextMenuCB),
                           'pcmcb'
                        ),
                        ([], PCIDLIST_ABSOLUTE, 'pidlFolder'),
                        ([], POINTER(IShellFolder), 'psf'),
                        ([], UINT, 'cidl'),
                        (['unique', 'in'], PCUITEMID_CHILD_ARRAY, 'apidl'),
                        ([], POINTER(IUnknown), 'punkAssociation'),
                        ([], UINT, 'cKeys'),
                        (
                            ['unique', annotation('_In_opt_'), 'in'],
                            POINTER(HKEY),
                           'aKeys'
                        ),
                    ),

                    # Control behavior of menu
                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetMenuRestrictions',
                        (
                            ['in'],
                            DEFAULT_FOLDER_MENU_RESTRICTIONS,
                           'dfmrValues'
                        ),
                    ),

                    #                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'GetMenuRestrictions',
                        (
                            ['in'],
                            DEFAULT_FOLDER_MENU_RESTRICTIONS,
                           'dfmrMask'
                        ),
                        (
                            ['out'],
                            POINTER(DEFAULT_FOLDER_MENU_RESTRICTIONS),
                           'pdfmrValues'
                        ),
                    ),

                    # Specify the handler to be used                
                    COMMETHOD(
                        [],
                        HRESULT,
                        'SetHandlerClsid',
                        (['in'], REFCLSID, 'rclsid'),
                    ),

                    #                ]


                # [annotation][iid_is][out]

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][unique][in]

                # [annotation][size_is][unique][in]
            # END IF  C style interface
        # END IF  __IDefaultFolderMenuInitialize_INTERFACE_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0154

        # [local]
        if (NTDDI_VERSION >= NTDDI_WIN8):
            class ACTIVATEOPTIONS(ENUM):
                AO_NONE = 0
                AO_DESIGNMODE = 0x1
                AO_NOERRORUI = 0x2
                AO_NOSPLASHSCREEN = 0x4
                AO_PRELAUNCH = 0x2000000


            AO_NONE = ACTIVATEOPTIONS.AO_NONE
            AO_DESIGNMODE = ACTIVATEOPTIONS.AO_DESIGNMODE
            AO_NOERRORUI = ACTIVATEOPTIONS.AO_NOERRORUI
            AO_NOSPLASHSCREEN = ACTIVATEOPTIONS.AO_NOSPLASHSCREEN
            AO_PRELAUNCH = ACTIVATEOPTIONS.AO_PRELAUNCH
            if not defined(__IApplicationActivationManager_INTERFACE_DEFINED__):
                __IApplicationActivationManager_INTERFACE_DEFINED__ = 1

                # interface IApplicationActivationManager

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IApplicationActivationManager._methods_ = [

                        # Activates the specified immersive application for
                        # the "Launch" contract, passing the provided arguments
                        # string into the application. Callers can obtain the
                        # process Id of the application instance fulfilling
                        # this contract.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ActivateApplication',
                            (['in'], LPCWSTR, 'appUserModelId'),
                            (['unique', 'in'], LPCWSTR, 'arguments'),
                            ([], ACTIVATEOPTIONS, 'options'),
                            (['out'], POINTER(DWORD), 'processId'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ActivateForFile',
                            (['in'], LPCWSTR, 'appUserModelId'),
                            ([], POINTER(IShellItemArray), 'itemArray'),
                            (['unique', 'in'], LPCWSTR, 'verb'),
                            (['out'], POINTER(DWORD), 'processId'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ActivateForProtocol',
                            (['in'], LPCWSTR, 'appUserModelId'),
                            ([], POINTER(IShellItemArray), 'itemArray'),
                            (['out'], POINTER(DWORD), 'processId'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IApplicationActivationManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0155

            # [local]
        # END IF   NTDDI_WIN8
        if not defined(__ShellCoreObjects_LIBRARY_DEFINED__):
            __ShellCoreObjects_LIBRARY_DEFINED__ = 1

            # library ShellCoreObjects

            # [version][lcid][uuid]

            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
            if defined(__cplusplus):
                pass
            # END IF
        # END IF  __ShellCoreObjects_LIBRARY_DEFINED__

        # interface __MIDL_itf_shobjidl_core_0000_0156

        # [local]
        if (NTDDI_VERSION >= NTDDI_VISTA):
            pass
        # END IF   NTDDI_VISTA
        if (NTDDI_VERSION >= NTDDI_WIN7):
            if (_WIN32_IE >= _WIN32_IE_IE70):
                class LIBRARYMANAGEDIALOGOPTIONS(ENUM):
                    LMD_DEFAULT = 0
                    LMD_ALLOWUNINDEXABLENETWORKLOCATIONS = 0x1


                LMD_DEFAULT = LIBRARYMANAGEDIALOGOPTIONS.LMD_DEFAULT
                LMD_ALLOWUNINDEXABLENETWORKLOCATIONS = LIBRARYMANAGEDIALOGOPTIONS.LMD_ALLOWUNINDEXABLENETWORKLOCATIONS
                if defined(__cplusplus) and not defined(CINTERFACE):

                    # These functions properly initialize their _Outptr_
                    # parameters to NULL, and only return NULL

                    # on failure, but /analyze can't presently distinguish the
                    # failure case from the success case, and

                    # throws warning C6387 anyway. Thus, the warning is
                    # disabled to aVOID generating noise for code

                    # that includes shobjidl.h and compiles with /analyze.
                # END IF   __cplusplus and not CINTERFACE
            # END IF   _WIN32_IE >= _WIN32_IE_IE70
        # END IF   NTDDI_WIN7
        if (NTDDI_VERSION >= NTDDI_VISTA):
            if not defined(__IAssocHandlerInvoker_INTERFACE_DEFINED__):
                __IAssocHandlerInvoker_INTERFACE_DEFINED__ = 1

                # interface IAssocHandlerInvoker

                # [local][unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IAssocHandlerInvoker._methods_ = [

                        # Returns S_OK if selection is supported, S_FALSE if
                        # not.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SupportsSelection',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Invoke',
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IAssocHandlerInvoker_INTERFACE_DEFINED__
            if not defined(__IAssocHandler_INTERFACE_DEFINED__):
                __IAssocHandler_INTERFACE_DEFINED__ = 1

                # interface IAssocHandler

                # [local][unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][out][string]

                    # [annotation][out][string]

                    # [annotation][out][string]

                    # [annotation][out]

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]
                else: # C style interface
                    IAssocHandler._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetName',
                            (
                                [annotation('_Outptr_'), , 'out'],
                                POINTER(LPWSTR),
                               'ppsz'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetUIName',
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(LPWSTR),
                               'ppsz'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetIconLocation',
                            (
                                ['out', annotation('_Outptr_')],
                                POINTER(LPWSTR),
                               'ppszPath'
                            ),
                            (
                                [annotation('_Out_'), 'out'],
                                POINTER(INT),
                               'pIndex'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'IsRecommended',
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'MakeDefault',
                            (
                                [annotation('_In_'), , 'in'],
                                LPCWSTR,
                               'pszDescription'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Invoke',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IDataObject),
                               'pdo'
                            ),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'CreateInvoker',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IDataObject),
                               'pdo'
                            ),
                            (
                                [annotation('_Outptr_'), 'out'],
                                POINTER(POINTER(IAssocHandlerInvoker)),
                               'ppInvoker'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][out][string]

                    # [annotation][out][string]

                    # [annotation][out][string]

                    # [annotation][out]

                    # [annotation][string][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __IAssocHandler_INTERFACE_DEFINED__
            if not defined(__IEnumAssocHandlers_INTERFACE_DEFINED__):
                __IEnumAssocHandlers_INTERFACE_DEFINED__ = 1

                # interface IEnumAssocHandlers

                # [local][unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][length_is][size_is][out]

                    # [annotation][out]
                else: # C style interface
                    IEnumAssocHandlers._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Next',
                            ([annotation('_In_'), 'in'], ULONG, 'celt'),
                            (
                                ['out', annotation('_Out_writes_to_(celt, *pceltFetched)), 'in', 'out'],
                                POINTER(POINTER(IAssocHandler)),
                               'rgelt'
                            ),
                            (
                                ['out', annotation('_Out_opt_ _Deref_out_range_(0,celt))],
                                POINTER(ULONG),
                               'pceltFetched'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][length_is][size_is][out]

                    # [annotation][out]
                # END IF  C style interface
            # END IF  __IEnumAssocHandlers_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0159

            # [local]
            class ASSOC_FILTER(ENUM):
                ASSOC_FILTER_NONE = 0
                ASSOC_FILTER_RECOMMENDED = 0x1


        # END IF   NTDDI_VISTA
        if (NTDDI_VERSION >= NTDDI_WIN7):
            pass
        # END IF   NTDDI_WIN7
        if (NTDDI_VERSION >= NTDDI_WIN8):
            if not defined(__IDataObjectProvider_INTERFACE_DEFINED__):
                __IDataObjectProvider_INTERFACE_DEFINED__ = 1

                # interface IDataObjectProvider

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]
                else: # C style interface
                    IDataObjectProvider._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetDataObject',
                            (
                                ['out'],
                                POINTER(POINTER(IDataObject)),
                               'dataObject'
                            ),
                        ),
                    
                        COMMETHOD(
                            ['local'],
                            HRESULT,
                            'SetDataObject',
                            (
                                [annotation('_In_'), 'in'],
                                POINTER(IDataObject),
                               'dataObject'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IDataObjectProvider_INTERFACE_DEFINED__
            if not defined(__IDataTransferManagerInterop_INTERFACE_DEFINED__):
                __IDataTransferManagerInterop_INTERFACE_DEFINED__ = 1

                # interface IDataTransferManagerInterop

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IDataTransferManagerInterop._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetForWindow',
                            (['in'], HWND, 'appWindow'),
                            ([], REFIID, 'riid'),
                            (
                                ['retval', 'out'],
                                POINTER(POINTER(VOID)),
                               'dataTransferManager'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ShowShareUIForWindow',
                            (['in'], HWND, 'appWindow'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IDataTransferManagerInterop_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0161

            # [local]
        # END IF   NTDDI_WIN8
        if (NTDDI_VERSION >= NTDDI_WIN8):
            if not defined(__IFrameworkInputPaneHandler_INTERFACE_DEFINED__):
                __IFrameworkInputPaneHandler_INTERFACE_DEFINED__ = 1

                # interface IFrameworkInputPaneHandler

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFrameworkInputPaneHandler._methods_ = [

                        # This method is called right before the Input Pane is
                        # going to show
                        # prcInputPaneScreenLocation - The screen location of
                        # the Input Pane in screen pixels
                        # fEnsureFocusedElementInView - If true, the framework
                        # implementor should attempt to keep
                        # the currently focused element
                        # (text box, for example) in view and unobscured by
                        # the RECT
                        # specified in prcInputPaneScreenLocation                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Showing',
                            (
                                ['in'],
                                POINTER(RECT),
                               'prcInputPaneScreenLocation'
                            ),
                            ([], BOOL, 'fEnsureFocusedElementInView'),
                        ),

                        # This is called right before the Input Pane is going
                        # to hide
                        # fEnsureFocusedElementInView - If true, the framework
                        # implementor should attempt to keep
                        # the currently focused element
                        # (text box, for example) in view. One thing
                        # that a framework could do is move the focused
                        # element back
                        # to its original location (pre - Showing())                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Hiding',
                            (['in'], BOOL, 'fEnsureFocusedElementInView'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IFrameworkInputPaneHandler_INTERFACE_DEFINED__
            if not defined(__IFrameworkInputPane_INTERFACE_DEFINED__):
                __IFrameworkInputPane_INTERFACE_DEFINED__ = 1

                # interface IFrameworkInputPane

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IFrameworkInputPane._methods_ = [

                        # This allows application frameworks to get callbacks
                        # on their handler
                        # whenever an event triggers the Input Pane to show
                        # for the passed in ICoreWindow.
                        # pWindow - This identifies the window for which the
                        # caller is interested in listening to Input Pane
                        # events.
                        # Even though this is an IUnknown, it must be a
                        # pointer to an object that implements IWindow.
                        # pHandler - The handler that will recieve callbacks
                        # for Input Pane Events
                        # pdwCookie - A returned cookie that the application
                        # framework can later use to unregister
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Advise',
                            (['in'], POINTER(IUnknown), 'pWindow'),
                            (
                                [],
                                POINTER(IFrameworkInputPaneHandler),
                               'pHandler'
                            ),
                            (['out'], POINTER(DWORD), 'pdwCookie'),
                        ),

                        # This is an alternative signature to Advise directly
                        # using an HWND as opposed to an ICoreWindow.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AdviseWithHWND',
                            (['in'], HWND, 'hwnd'),
                            (
                                [],
                                POINTER(IFrameworkInputPaneHandler),
                               'pHandler'
                            ),
                            (['out'], POINTER(DWORD), 'pdwCookie'),
                        ),

                        # This takes in an identifier returned from Advise(),
                        # and unregisters the handler
                        # so that it will no LONGer recieve notifications
                        # dwCookie - The registration cookie returned from a
                        # previous Advise() call                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Unadvise',
                            (['in'], DWORD, 'dwCookie'),
                        ),

                        # This gets the current location of the Input Pane in
                        # screen coordinates
                        # If the Input Pane is not visible this will be an
                        # empty rectangle.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Location',
                            (
                                ['out'],
                                POINTER(RECT),
                               'prcInputPaneScreenLocation'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IFrameworkInputPane_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0163

            # [local]
            if not defined(PROP_CONTRACT_DELEGATE):
                PROP_CONTRACT_DELEGATE = "ContractDelegate"
            # END IF   PROP_CONTRACT_DELEGATE

            # For applications that use modern APIs and use a child or owned
            # window

            # that run on different threads this API must be used to indicate
            # which

            # window is the current main window. Call this API when those
            # windows change their state.
        # END IF   NTDDI_WIN8

        if (NTDDI_VERSION >= NTDDI_WIN8):
            class MONITOR_APP_VISIBILITY(ENUM):
                MAV_UNKNOWN = 0
                MAV_NO_APP_VISIBLE = 1
                MAV_APP_VISIBLE = 2


            MAV_UNKNOWN = MONITOR_APP_VISIBILITY.MAV_UNKNOWN
            MAV_NO_APP_VISIBLE = MONITOR_APP_VISIBILITY.MAV_NO_APP_VISIBLE
            MAV_APP_VISIBLE = MONITOR_APP_VISIBILITY.MAV_APP_VISIBLE
            if not defined(__IAppVisibilityEvents_INTERFACE_DEFINED__):
                __IAppVisibilityEvents_INTERFACE_DEFINED__ = 1

                # interface IAppVisibilityEvents

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IAppVisibilityEvents._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'AppVisibilityOnMonitorChanged',
                            (['in'], HMONITOR, 'hMonitor'),
                            ([], MONITOR_APP_VISIBILITY, 'previousMode'),
                            ([], MONITOR_APP_VISIBILITY, 'currentMode'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'LauncherVisibilityChange',
                            (['in'], BOOL, 'currentVisibleState'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IAppVisibilityEvents_INTERFACE_DEFINED__
            if not defined(__IAppVisibility_INTERFACE_DEFINED__):
                __IAppVisibility_INTERFACE_DEFINED__ = 1

                # interface IAppVisibility

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IAppVisibility._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetAppVisibilityOnMonitor',
                            (['in'], HMONITOR, 'hMonitor'),
                            (
                                ['out'],
                                POINTER(MONITOR_APP_VISIBILITY),
                               'pMode'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'IsLauncherVisible',
                            (['out'], POINTER(BOOL), 'pfVisible'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Advise',
                            (['out'], POINTER(DWORD), 'pdwCookie'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Unadvise',
                            (['in'], DWORD, 'dwCookie'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IAppVisibility_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0165

            # [local]
            if defined(MIDL_PASS):
                pass
            # END IF
            class PACKAGE_EXECUTION_STATE(ENUM):
                PES_UNKNOWN = 0
                PES_RUNNING = 1
                PES_SUSPENDING = 2
                PES_SUSPENDED = 3
                PES_TERMINATED = 4


            PES_UNKNOWN = PACKAGE_EXECUTION_STATE.PES_UNKNOWN
            PES_RUNNING = PACKAGE_EXECUTION_STATE.PES_RUNNING
            PES_SUSPENDING = PACKAGE_EXECUTION_STATE.PES_SUSPENDING
            PES_SUSPENDED = PACKAGE_EXECUTION_STATE.PES_SUSPENDED
            PES_TERMINATED = PACKAGE_EXECUTION_STATE.PES_TERMINATED
            if not defined(__IPackageExecutionStateChangeNotification_INTERFACE_DEFINED__):
                __IPackageExecutionStateChangeNotification_INTERFACE_DEFINED__ = 1

                # interface IPackageExecutionStateChangeNotification

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IPackageExecutionStateChangeNotification._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'OnStateChanged',
                            (['in'], LPCWSTR, 'pszPackageFullName'),
                            (['in'], PACKAGE_EXECUTION_STATE, 'pesNewState'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IPackageExecutionStateChangeNotification_INTERFACE_DEFINED__
            if not defined(__IPackageDebugSettings_INTERFACE_DEFINED__):
                __IPackageDebugSettings_INTERFACE_DEFINED__ = 1

                # interface IPackageDebugSettings

                # [uuid][local][object]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]
                else: # C style interface
                    IPackageDebugSettings._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnableDebugging',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                            (
                                [annotation('_In_opt_'), 'in'],
                                LPCWSTR,
                               'debuggerCommandLine'
                            ),
                            ([], PZZWSTR, 'environment'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'DisableDebugging',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Suspend',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Resume',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'TerminateAllProcesses',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetTargetSessionId',
                            ([annotation('_In_'), 'in'], ULONG, 'sessionId'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnumerateBackgroundTasks',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                            (
                                ['out', annotation('_Out_')],
                                POINTER(ULONG),
                               'taskCount'
                            ),
                            (
                                ['out', annotation('_Outptr_result_buffer_(*taskCount))],
                                POINTER(LPCGUID),
                               'taskIds'
                            ),
                            ([], POINTER(POINTER(LPCWSTR)), 'taskNames'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ActivateBackgroundTask',
                            ([annotation('_In_'), 'in'], LPCGUID, 'taskId'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'StartServicing',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'StopServicing',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'StartSessionRedirection',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                            ([], ULONG, 'sessionId'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'StopSessionRedirection',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetPackageExecutionState',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                            (
                                [annotation('_Out_'), 'out'],
                                POINTER(PACKAGE_EXECUTION_STATE),
                               'packageExecutionState'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RegisterForPackageStateChanges',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                            (
                                [],
                                POINTER(IPackageExecutionStateChangeNotification),
                               'pPackageExecutionStateChangeNotification'
                            ),
                            (
                                [annotation('_Out_'), 'out'],
                                POINTER(DWORD),
                               'pdwCookie'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UnregisterForPackageStateChanges',
                            ([annotation('_In_'), 'in'], DWORD, 'dwCookie'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __IPackageDebugSettings_INTERFACE_DEFINED__
            if not defined(__IPackageDebugSettings2_INTERFACE_DEFINED__):
                __IPackageDebugSettings2_INTERFACE_DEFINED__ = 1

                # interface IPackageDebugSettings2

                # [uuid][local][object]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][size_is][size_is][out]
                else: # C style interface
                    IPackageDebugSettings2._methods_ = [
                        #
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'EnumerateApps',
                            (
                                [annotation('_In_'), 'in'],
                                LPCWSTR,
                               'packageFullName'
                            ),
                            (
                                ['out', annotation('_Out_')],
                                POINTER(ULONG),
                               'appCount'
                            ),
                            (
                                [annotation('_Outptr_result_buffer_(*appCount)), 'out'],
                                POINTER(POINTER(LPWSTR)),
                               'appUserModelIds'
                            ),
                            ([], POINTER(POINTER(LPWSTR)), 'appDisplayNames'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][out]

                    # [annotation][size_is][size_is][out]

                    # [annotation][size_is][size_is][out]
                # END IF  C style interface
            # END IF  __IPackageDebugSettings2_INTERFACE_DEFINED__
            if not defined(__ISuspensionDependencyManager_INTERFACE_DEFINED__):
                __ISuspensionDependencyManager_INTERFACE_DEFINED__ = 1

                # interface ISuspensionDependencyManager

                # [uuid][local][object]

                if defined(__cplusplus) and not defined(CINTERFACE):

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                else: # C style interface
                    ISuspensionDependencyManager._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'RegisterAsChild',
                            (
                                [annotation('_In_'), 'in'],
                                HANDLE,
                               'processHandle'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GroupChildWithParent',
                            (
                                [annotation('_In_'), 'in'],
                                HANDLE,
                               'childProcessHandle'
                            ),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'UngroupChildFromParent',
                            (
                                [annotation('_In_'), 'in'],
                                HANDLE,
                               'childProcessHandle'
                            ),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]

                    # [annotation][in]

                    # [annotation][in]

                    # [annotation][in]
                # END IF  C style interface
            # END IF  __ISuspensionDependencyManager_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0169

            # [local]
            class AHE_TYPE(ENUM):
                AHE_DESKTOP = 0
                AHE_IMMERSIVE = 1


            AHE_DESKTOP = AHE_TYPE.AHE_DESKTOP
            AHE_IMMERSIVE = AHE_TYPE.AHE_IMMERSIVE
            if not defined(__IExecuteCommandApplicationHostEnvironment_INTERFACE_DEFINED__):
                __IExecuteCommandApplicationHostEnvironment_INTERFACE_DEFINED__ = 1

                # interface IExecuteCommandApplicationHostEnvironment

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IExecuteCommandApplicationHostEnvironment._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetValue',
                            (['out'], POINTER(AHE_TYPE), 'pahe'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IExecuteCommandApplicationHostEnvironment_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0170

            # [local]
            class EC_HOST_UI_MODE(ENUM):
                ECHUIM_DESKTOP = 0
                #~#~#~ ECHUIM_IMMERSIVE    = ( ECHUIM_DESKTOP + 1 )
                #~#~#~ ECHUIM_SYSTEM_LAUNCHER    = ( ECHUIM_IMMERSIVE + 1 )


            ECHUIM_DESKTOP = EC_HOST_UI_MODE.ECHUIM_DESKTOP
            if not defined(__IExecuteCommandHost_INTERFACE_DEFINED__):
                __IExecuteCommandHost_INTERFACE_DEFINED__ = 1

                # interface IExecuteCommandHost

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IExecuteCommandHost._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetUIMode',
                            (['out'], POINTER(EC_HOST_UI_MODE), 'pUIMode'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IExecuteCommandHost_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0171

            # [local]
            SID_ExecuteCommandHost = IID_IExecuteCommandHost


            class APPLICATION_VIEW_STATE(ENUM):
                AVS_FULLSCREEN_LANDSCAPE = 0
                #~#~#~ AVS_FILLED    = ( AVS_FULLSCREEN_LANDSCAPE + 1 )
                #~#~#~ AVS_SNAPPED    = ( AVS_FILLED + 1 )
                #~#~#~ AVS_FULLSCREEN_PORTRAIT    = ( AVS_SNAPPED + 1 )


            AVS_FULLSCREEN_LANDSCAPE = APPLICATION_VIEW_STATE.AVS_FULLSCREEN_LANDSCAPE
            class EDGE_GESTURE_KIND(ENUM):
                EGK_TOUCH = 0
                #~#~#~ EGK_KEYBOARD    = ( EGK_TOUCH + 1 )
                #~#~#~ EGK_MOUSE    = ( EGK_KEYBOARD + 1 )


            EGK_TOUCH = EDGE_GESTURE_KIND.EGK_TOUCH
            if not defined(__IApplicationDesignModeSettings_INTERFACE_DEFINED__):
                __IApplicationDesignModeSettings_INTERFACE_DEFINED__ = 1

                # interface IApplicationDesignModeSettings

                # [uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IApplicationDesignModeSettings._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetNativeDisplaySize',
                            (['in'], SIZE, 'nativeDisplaySizePixels'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetScaleFactor',
                            (['in'], DEVICE_SCALE_FACTOR, 'scaleFactor'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'SetApplicationViewState',
                            (['in'], APPLICATION_VIEW_STATE, 'viewState'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ComputeApplicationSize',
                            (['out'], POINTER(SIZE), 'applicationSizePixels'),
                        ),

                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'IsApplicationViewStateSupported',
                            (['in'], APPLICATION_VIEW_STATE, 'viewState'),
                            ([], SIZE, 'nativeDisplaySizePixels'),
                            ([], DEVICE_SCALE_FACTOR, 'scaleFactor'),
                            (['out'], POINTER(BOOL), 'supported'),
                        ),
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'TriggerEdgeGesture',
                            (['in'], EDGE_GESTURE_KIND, 'edgeGestureKind'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IApplicationDesignModeSettings_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0172

            # [local]
            class NATIVE_DISPLAY_ORIENTATION(ENUM):
                NDO_LANDSCAPE = 0
                #~#~#~ NDO_PORTRAIT    = ( NDO_LANDSCAPE + 1 )


            NDO_LANDSCAPE = NATIVE_DISPLAY_ORIENTATION.NDO_LANDSCAPE
            class APPLICATION_VIEW_ORIENTATION(ENUM):
                AVO_LANDSCAPE = 0
                #~#~#~ AVO_PORTRAIT    = ( AVO_LANDSCAPE + 1 )


            AVO_LANDSCAPE = APPLICATION_VIEW_ORIENTATION.AVO_LANDSCAPE
            class ADJACENT_DISPLAY_EDGES(ENUM):
                ADE_NONE = 0
                ADE_LEFT = 0x1
                ADE_RIGHT = 0x2


            ADE_NONE = ADJACENT_DISPLAY_EDGES.ADE_NONE
            ADE_LEFT = ADJACENT_DISPLAY_EDGES.ADE_LEFT
            ADE_RIGHT = ADJACENT_DISPLAY_EDGES.ADE_RIGHT
            if (NTDDI_VERSION >= NTDDI_WINBLUE):
                class APPLICATION_VIEW_MIN_WIDTH(ENUM):
                    AVMW_DEFAULT = 0
                    AVMW_320 = 1
                    AVMW_500 = 2


                AVMW_DEFAULT = APPLICATION_VIEW_MIN_WIDTH.AVMW_DEFAULT
                AVMW_320 = APPLICATION_VIEW_MIN_WIDTH.AVMW_320
                AVMW_500 = APPLICATION_VIEW_MIN_WIDTH.AVMW_500
                if not defined(__IApplicationDesignModeSettings2_INTERFACE_DEFINED__):
                    __IApplicationDesignModeSettings2_INTERFACE_DEFINED__ = 1

                    # interface IApplicationDesignModeSettings2

                    # [uuid][object]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        IApplicationDesignModeSettings2._methods_ = [
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetNativeDisplayOrientation',
                                (
                                    ['in'],
                                    NATIVE_DISPLAY_ORIENTATION,
                                   'nativeDisplayOrientation'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetApplicationViewOrientation',
                                (
                                    ['in'],
                                    APPLICATION_VIEW_ORIENTATION,
                                   'viewOrientation'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetAdjacentDisplayEdges',
                                (
                                    ['in'],
                                    ADJACENT_DISPLAY_EDGES,
                                   'adjacentDisplayEdges'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetIsOnLockScreen',
                                (['in'], BOOL, 'isOnLockScreen'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'SetApplicationViewMinWidth',
                                (
                                    ['in'],
                                    APPLICATION_VIEW_MIN_WIDTH,
                                   'viewMinWidth'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetApplicationSizeBounds',
                                (
                                    ['out'],
                                    POINTER(SIZE),
                                   'minApplicationSizePixels'
                                ),
                                (
                                    [],
                                    POINTER(SIZE),
                                   'maxApplicationSizePixels'
                                ),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetApplicationViewOrientation',
                                (['in'], SIZE, 'applicationSizePixels'),
                                (
                                    ['out'],
                                    POINTER(APPLICATION_VIEW_ORIENTATION),
                                   'viewOrientation'
                                ),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __IApplicationDesignModeSettings2_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0173

                # [local]
                STR_TAB_REUSE_IDENTIFIER = "Tab Reuse Identifier"
                STR_REFERRER_IDENTIFIER = "Referrer Identifier"

                if not defined(__ILaunchTargetMonitor_INTERFACE_DEFINED__):
                    __ILaunchTargetMonitor_INTERFACE_DEFINED__ = 1

                    # interface ILaunchTargetMonitor

                    # [uuid][object]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        ILaunchTargetMonitor._methods_ = [
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetMonitor',
                                (['out'], POINTER(HMONITOR), 'monitor'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __ILaunchTargetMonitor_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0174

                # [local]
                SID_LaunchTargetMonitor = (
    __uuidof((struct __declspec(uuid("8D547FA1 - CC45 - 40C8 - B7C1 - D48C183F13F3")) LaunchTargetMonitor*)0)
)


                class APPLICATION_VIEW_SIZE_PREFERENCE(ENUM):
                    AVSP_DEFAULT = 0
                    AVSP_USE_LESS = 1
                    AVSP_USE_HALF = 2
                    AVSP_USE_MORE = 3
                    AVSP_USE_MINIMUM = 4
                    AVSP_USE_NONE = 5
                    AVSP_CUSTOM = 6


                AVSP_DEFAULT = APPLICATION_VIEW_SIZE_PREFERENCE.AVSP_DEFAULT
                AVSP_USE_LESS = APPLICATION_VIEW_SIZE_PREFERENCE.AVSP_USE_LESS
                AVSP_USE_HALF = APPLICATION_VIEW_SIZE_PREFERENCE.AVSP_USE_HALF
                AVSP_USE_MORE = APPLICATION_VIEW_SIZE_PREFERENCE.AVSP_USE_MORE
                AVSP_USE_MINIMUM = APPLICATION_VIEW_SIZE_PREFERENCE.AVSP_USE_MINIMUM
                AVSP_USE_NONE = APPLICATION_VIEW_SIZE_PREFERENCE.AVSP_USE_NONE
                AVSP_CUSTOM = APPLICATION_VIEW_SIZE_PREFERENCE.AVSP_CUSTOM
                if not defined(__ILaunchSourceViewSizePreference_INTERFACE_DEFINED__):
                    __ILaunchSourceViewSizePreference_INTERFACE_DEFINED__ = 1

                    # interface ILaunchSourceViewSizePreference

                    # [uuid][object]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        ILaunchSourceViewSizePreference._methods_ = [
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetSourceViewToPosition',
                                (['out'], POINTER(HWND), 'hwnd'),
                            ),
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetSourceViewSizePreference',
                                (
                                    ['out'],
                                    POINTER(APPLICATION_VIEW_SIZE_PREFERENCE),
                                   'sourceSizeAfterLaunch'
                                ),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __ILaunchSourceViewSizePreference_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0175

                # [local]
                if not defined(__ILaunchTargetViewSizePreference_INTERFACE_DEFINED__):
                    __ILaunchTargetViewSizePreference_INTERFACE_DEFINED__ = 1

                    # interface ILaunchTargetViewSizePreference

                    # [uuid][object]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        ILaunchTargetViewSizePreference._methods_ = [
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetTargetViewSizePreference',
                                (
                                    ['out'],
                                    POINTER(APPLICATION_VIEW_SIZE_PREFERENCE),
                                   'targetSizeOnLaunch'
                                ),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __ILaunchTargetViewSizePreference_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0176

                # [local]
                if not defined(__ILaunchSourceAppUserModelId_INTERFACE_DEFINED__):
                    __ILaunchSourceAppUserModelId_INTERFACE_DEFINED__ = 1

                    # interface ILaunchSourceAppUserModelId

                    # [uuid][object]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        ILaunchSourceAppUserModelId._methods_ = [
                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetAppUserModelId',
                                (['out', ], POINTER(LPWSTR), 'launchingApp'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __ILaunchSourceAppUserModelId_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0177

                # [local]
            # END IF   NTDDI_WINBLUE
            if not defined(__IInitializeWithWindow_INTERFACE_DEFINED__):
                __IInitializeWithWindow_INTERFACE_DEFINED__ = 1

                # interface IInitializeWithWindow

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IInitializeWithWindow._methods_ = [
                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'Initialize',
                            (['in'], HWND, 'hwnd'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IInitializeWithWindow_INTERFACE_DEFINED__
            if not defined(__IHandlerInfo_INTERFACE_DEFINED__):
                __IHandlerInfo_INTERFACE_DEFINED__ = 1

                # interface IHandlerInfo

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IHandlerInfo._methods_ = [

                        # Return the application display name suitable for
                        # display in UI. If not available this will
                        # return the file name of the application .exe.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetApplicationDisplayName',
                            (['out'], POINTER(LPWSTR), 'value'),
                        ),

                        # Return the application publisher suitable for
                        # display in UI. If not available this will fail.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetApplicationPublisher',
                            (['out'], POINTER(LPWSTR), 'value'),
                        ),

                        # Return the application icon suitable for display in
                        # UI. If not available this will fail.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'GetApplicationIconReference',
                            (['out'], POINTER(LPWSTR), 'value'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IHandlerInfo_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0179

            # [local]
            SID_HandlerInfo = IID_IHandlerInfo

            if not defined(__IHandlerActivationHost_INTERFACE_DEFINED__):
                __IHandlerActivationHost_INTERFACE_DEFINED__ = 1

                # interface IHandlerActivationHost

                # [unique][object][uuid]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IHandlerActivationHost._methods_ = [

                        # Implementations of these methods return S_OK to
                        # enable the activation of the handler,
                        # or an error code to cancel it. If the user canceled
                        # the operation
                        # HRESULT_FROM_WIN32(ERROR_CANCELLED) should be
                        # returned. EXECUTE_E_LAUNCH_APPLICATION
                        # can be returned to indicate that this verb
                        # implementation should be skipped and the next
                        # one tried (if there is one). Generally these error
                        # codes will propagate out of the sub system
                        # activating the handlers.
                        # handlerInfo implements IHandlerInfo2
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'BeforeCoCreateInstance',
                            (['in'], REFCLSID, 'clsidHandler'),
                            (
                                [],
                                POINTER(IShellItemArray),
                               'itemsBeingActivated'
                            ),
                            ([], POINTER(IHandlerInfo), 'handlerInfo'),
                        ),

                        # The applicationPath will normally be a fully
                        # qualified path to an application .exe
                        # but it can also be a .dll in the case of
                        # rundll32.exe based handlers.
                        #                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'BeforeCreateProcess',
                            (['in'], LPCWSTR, 'applicationPath'),
                            ([], LPCWSTR, 'commandLine'),
                            ([], POINTER(IHandlerInfo), 'handlerInfo'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IHandlerActivationHost_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0180

            # [local]
            SID_SHandlerActivationHost = IID_IHandlerActivationHost

            if (NTDDI_VERSION >= NTDDI_WIN10):
                if not defined(__IAppActivationUIInfo_INTERFACE_DEFINED__):
                    __IAppActivationUIInfo_INTERFACE_DEFINED__ = 1

                    # interface IAppActivationUIInfo

                    # [unique][object][uuid]

                    if defined(__cplusplus) and not defined(CINTERFACE):
                        pass
                    else: # C style interface
                        IAppActivationUIInfo._methods_ = [

                            # These methods will fail with E_NOT_SET if the
                            # values are not available.
                            # The monitor that originated the activation. UI
                            # generated should go on the same monitor.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetMonitor',
                                (['out'], POINTER(HMONITOR), 'value'),
                            ),

                            # Point in screen coordinates where the click or
                            # touch that originated the activation.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetInvokePoint',
                                (['out'], POINTER(POINT), 'value'),
                            ),

                            # ShowWindow() values, SW_NORMAL,
                            # SW_SHOWMINIMIZED, etc.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetShowCommand',
                                (['out'], POINTER(int), 'value'),
                            ),

                            # Indicates if UI should be displayed or not.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetShowUI',
                                (['out'], POINTER(BOOL), 'value'),
                            ),

                            # State of shift and control keys at activation
                            # time: MK_SHIFT, MK_CONTROL.                        
                            COMMETHOD(
                                [],
                                HRESULT,
                                'GetKeyState',
                                (['out'], POINTER(DWORD), 'value'),
                            ),

                            #                        ]


                        # [annotation][iid_is][out]
                    # END IF  C style interface
                # END IF  __IAppActivationUIInfo_INTERFACE_DEFINED__

                # interface __MIDL_itf_shobjidl_core_0000_0181

                # [local]
                SID_AppActivationUIInfo = IID_IAppActivationUIInfo
            # END IF   NTDDI_WIN10
        # END IF   NTDDI_WIN8

        if (NTDDI_VERSION >= NTDDI_WINBLUE):
            class FLYOUT_PLACEMENT(ENUM):
                FP_DEFAULT = 0
                #~#~#~ FP_ABOVE    = ( FP_DEFAULT + 1 )
                #~#~#~ FP_BELOW    = ( FP_ABOVE + 1 )
                #~#~#~ FP_LEFT    = ( FP_BELOW + 1 )
                #~#~#~ FP_RIGHT    = ( FP_LEFT + 1 )


            FP_DEFAULT = FLYOUT_PLACEMENT.FP_DEFAULT
            if not defined(__IContactManagerInterop_INTERFACE_DEFINED__):
                __IContactManagerInterop_INTERFACE_DEFINED__ = 1

                # interface IContactManagerInterop

                # [unique][uuid][object]

                if defined(__cplusplus) and not defined(CINTERFACE):
                    pass
                else: # C style interface
                    IContactManagerInterop._methods_ = [

                        # Default browser will use this method to launch
                        # contact card from its tab window, specified
                        # by the appWindow parameter.
                        # Must be a
                        # Windows::ApplicationModel::Contacts::IContact
                        # object. Use IUnknown here because classic COM IDL
                        # cannot use WinRT types.                    
                        COMMETHOD(
                            [],
                            HRESULT,
                            'ShowContactCardForWindow',
                            (['in'], HWND, 'appWindow'),
                            ([], POINTER(IUnknown), 'contact'),
                            ([], POINTER(RECT), 'selection'),
                            ([], FLYOUT_PLACEMENT, 'preferredPlacement'),
                        ),

                        #                    ]


                    # [annotation][iid_is][out]
                # END IF  C style interface
            # END IF  __IContactManagerInterop_INTERFACE_DEFINED__

            # interface __MIDL_itf_shobjidl_core_0000_0182

            # [local]
        # END IF   NTDDI_WINBLUE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
    if not defined(__IShellIconOverlayIdentifier_INTERFACE_DEFINED__):
        __IShellIconOverlayIdentifier_INTERFACE_DEFINED__ = 1

        # interface IShellIconOverlayIdentifier

        # [object][unique][uuid]

        if defined(__cplusplus) and not defined(CINTERFACE):
            pass
        else: # C style interface
            IShellIconOverlayIdentifier._methods_ = [
                #
            
                COMMETHOD(
                    [],
                    HRESULT,
                    'IsMemberOf',
                    (['in'], LPCWSTR, 'pwszPath'),
                    (['in'], DWORD, 'dwAttrib'),
                ),

                #            
                COMMETHOD(
                    [],
                    HRESULT,
                    'GetOverlayInfo',
                    (['out', ], LPWSTR, 'pwszIconFile'),
                    (['in'], INT, 'cchMax'),
                    (['out'], POINTER(INT), 'pIndex'),
                    ([], POINTER(DWORD), 'pdwFlags'),
                ),

                #            
                COMMETHOD(
                    [],
                    HRESULT,
                    'GetPriority',
                    (['out'], POINTER(INT), 'pPriority'),
                ),

                #            ]


            # [annotation][iid_is][out]
        # END IF  C style interface
    # END IF  __IShellIconOverlayIdentifier_INTERFACE_DEFINED__

    # interface __MIDL_itf_shobjidl_core_0000_0183

    # [local]
    ISIOI_ICONFILE = 0x00000001
    ISIOI_ICONINDEX = 0x00000002

    # Additional Prototypes for ALL interfaces

    # [annotation][in]

    # [annotation][length_is][size_is][out]

    # [annotation][out]

    # [annotation][in]

    # [annotation][length_is][size_is][out]

    # [annotation][out]

    # [annotation][unique][in]

    # [annotation][in]

    # [annotation][string][in]

    # [annotation][in]

    # [annotation][out]

    # [annotation][out]

    # [annotation][out]

    # [annotation][in]

    # [annotation][length_is][size_is][out]

    # [annotation][out]

    # [annotation][out]

    # [annotation][out]

    # [annotation][out]

    # [annotation][in]

    # [annotation][in]

    # [annotation][iid_is][length_is][size_is][out]

    # [annotation][out]

    # [annotation][in]

    # [annotation][out]

    # [annotation][out]

    # [annotation][size_is][string][out]

    # [annotation][in]

    # [annotation][unique][in]

    # [annotation][in]

    # [annotation][unique][in]

    # [annotation][in]

    # [annotation][string][unique][in]

    # [annotation][in]

    # [annotation][unique][size_is][in]

    # [annotation][string][out]

    # [annotation][in]

    # [annotation][length_is][size_is][out]

    # [annotation][out]

    # end of Additional Prototypes

    if defined(__cplusplus):
        pass
    # END IF
# END IF
