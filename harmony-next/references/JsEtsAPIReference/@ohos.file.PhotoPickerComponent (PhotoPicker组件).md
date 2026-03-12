# @ohos.file.PhotoPickerComponent (PhotoPicker组件)

应用可以在布局中嵌入PhotoPicker组件，通过此组件，应用无需申请权限，即可实现媒体文件选择功能。在用户选择媒体文件后，应用即可访问用户选中的图片或视频文件。仅包含读权限。

需要注意的是PhotoPickerComponent不能嵌套使用，且不建议在PhotoPickerComponent上覆盖设置了overlay属性的组件，将导致PhotoPickerComponent无法接受手势事件。

应用嵌入组件后，用户可直接在PhotoPicker组件中选择图片或视频文件。

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import {
  PhotoPickerComponent, PickerController, PickerOptions,
  DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, ItemType, ClickType,
  MaxCountType, PhotoBrowserRange, PhotoBrowserUIElement,
  ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback
} from '@ohos.file.PhotoPickerComponent';
```

#### 属性

支持[通用属性](通用属性.md)。

#### PhotoPickerComponent

PhotoPickerComponent({

 pickerOptions?: PickerOptions,

 onSelect?: (uri: string) => void,

 onDeselect?: (uri: string) => void,

 onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean,

 onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean,

 onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean,

 onPickerControllerReady?: () => void,

 onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean,

 onSelectedItemsDeleted?: ItemsDeletedCallback,

 onExceedMaxSelected?: ExceedMaxSelectedCallback,

 onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback,

 onVideoPlayStateChanged?: videoPlayStateChangedCallback,

 pickerController: PickerController

})

应用可以在布局中嵌入PhotoPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的图片或视频文件。

如果当前PhotoPickerComponent组件嵌套在Tabs组件中使用，Tabs组件的左右滑动会与图片选择大图界面的左右滑动切换手势发生冲突。

可在进退大图的回调中设置Tabs组件是否支持滑动来规避，该问题将在后续版本修复。

**装饰器类型**：@Component

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

名称类型必填装饰器类型说明pickerOptions[PickerOptions](#ZH-CN_TOPIC_0000002497605958__pickeroptions)否-

picker配置参数信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onSelect(uri: string) => void否-

用户在Picker组件中勾选图片时产生的回调事件，将图片uri报给应用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onDeselect(uri: string) => void否-

用户在Picker组件中取消勾选图片时产生的回调事件，同时也会将图片uri报给应用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onItemClicked(itemInfo: [ItemInfo](#ZH-CN_TOPIC_0000002497605958__iteminfo), clickType: [ClickType](#ZH-CN_TOPIC_0000002497605958__clicktype)) => boolean否-

用户在picker组件中点击item产生的回调事件。

点击图片（缩略图item）时，返回值为true则勾选此图片，否则不响应勾选，uri不授权；点击相机item，返回值为true则拉起系统相机，否则不拉起相机，由应用自行处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onEnterPhotoBrowser(photoBrowserInfo: [PhotoBrowserInfo](#ZH-CN_TOPIC_0000002497605958__photobrowserinfo)) => boolean否-

点击进入大图时产生的回调事件，将大图相关信息报给应用。不对返回值做特殊处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onExitPhotoBrowser(photoBrowserInfo: [PhotoBrowserInfo](#ZH-CN_TOPIC_0000002497605958__photobrowserinfo)) => boolean否-

退出大图时产生的回调事件，将大图相关信息报给应用。不对返回值做特殊处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onPickerControllerReady() => void否-

当pickerController可用时产生的回调事件。

调用PickerController相关接口需在该回调后才能生效。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onPhotoBrowserChanged(browserItemInfo: [BaseItemInfo](#ZH-CN_TOPIC_0000002497605958__baseiteminfo)) => boolean否-

大图左右滑动时产生的回调事件，将大图相关信息报给应用。仅在多选模式下生效。不对返回值做特殊处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onSelectedItemsDeleted13+[ItemsDeletedCallback](#ZH-CN_TOPIC_0000002497605958__itemsdeletedcallback13)否-

已勾选的图片被删除时产生的回调，并将被删除图片的相关信息回调给应用。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

onExceedMaxSelected13+[ExceedMaxSelectedCallback](#ZH-CN_TOPIC_0000002497605958__exceedmaxselectedcallback13)否-

选择达到最大选择数量（最大图片选择数量或者是最大视频选择数量亦或是总的最大选择数量）之后再次点击勾选时产生的回调。

- 若选择的数量达到了最大图片选择数量且未达到总的最大选择数量则回调的参数exceedMaxCountType为[MaxCountType](#ZH-CN_TOPIC_0000002497605958__maxcounttype).PHOTO_MAX_COUNT。

- 若选择的数量达到了最大视频选择数量且未达到总的最大选择数量则回调的参数exceedMaxCountType为[MaxCountType](#ZH-CN_TOPIC_0000002497605958__maxcounttype).VIDEO_MAX_COUNT。

- 只要选择的数量达到了总的最大选择数量则回调的参数exceedMaxCountType为[MaxCountType](#ZH-CN_TOPIC_0000002497605958__maxcounttype).TOTAL_MAX_COUNT。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

onCurrentAlbumDeleted13+[CurrentAlbumDeletedCallback](#ZH-CN_TOPIC_0000002497605958__currentalbumdeletedcallback13)否-

当前相册被删除时产生的回调。

当前相册是指通过pickerController.[setData](#ZH-CN_TOPIC_0000002497605958__setdata)([DataType](#ZH-CN_TOPIC_0000002497605958__datatype).SET_ALBUM_URI, currentAlbumUri)接口设置给宫格组件的相册，即“currentAlbumUri”。

当前相册被删除后若使用方刷新自己的相册标题栏，使用方可以设置自己的标题栏名称为默认的相册名例如“图片和视频”、“图片”或“视频”，然后通过pickerController.[setData](#ZH-CN_TOPIC_0000002497605958__setdata)([DataType](#ZH-CN_TOPIC_0000002497605958__datatype).SET_ALBUM_URI, '')接口传空串去刷新宫格页为默认相册。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

onVideoPlayStateChanged14+[videoPlayStateChangedCallback](#ZH-CN_TOPIC_0000002497605958__videoplaystatechangedcallback14)否-

大图页视频播放状态改变时回调。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

pickerController[PickerController](#ZH-CN_TOPIC_0000002497605958__pickercontroller)是@ObjectLink

应用可通过PickerController向Picker组件发送数据。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

onMovingPhotoBadgeStateChanged22+[MovingPhotoBadgeStateChangedCallback](#ZH-CN_TOPIC_0000002497605958__movingphotobadgestatechangedcallback22)否-

用户在Picker组件中打开/关闭动态效果时产生的回调。将图片uri和动态照片状态报给应用。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

#### PickerOptions

Picker配置选项，继承自[photoAccessHelper.BaseSelectOptions](Classes (其他).md#ZH-CN_TOPIC_0000002497605950__baseselectoptions)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明checkBoxColorstring否是

勾选框的背景色。格式为8位十六进制颜色代码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

backgroundColorstring否是

picker宫格页面背景色。格式为8位十六进制颜色代码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isRepeatSelectSupportedboolean否是

是否支持单张图片重复选择。true表示支持。默认不支持。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

checkboxTextColorstring否是

勾选框内文本颜色。格式为8位十六进制颜色代码（该能力从API version 19开始支持，API version 19之前系统默认为白色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

photoBrowserBackgroundColorMode[PickerColorMode](#ZH-CN_TOPIC_0000002497605958__pickercolormode)否是

大图背景颜色。包括跟随系统、浅色模式以及深色模式，默认为跟随系统。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

maxSelectedReminderMode[ReminderMode](#ZH-CN_TOPIC_0000002497605958__remindermode)否是

选择数量达到最大时的提示方式。包括弹toast提示、不提示以及蒙层提示，默认为弹toast提示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

orientation[PickerOrientation](#ZH-CN_TOPIC_0000002497605958__pickerorientation)否是

宫格页面滑动预览方向，包括水平和竖直两个方向，默认为竖直方向（该能力从API version 20开始支持，API version 20之前系统默认为竖直方向）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

selectMode[SelectMode](#ZH-CN_TOPIC_0000002497605958__selectmode)否是

选择模式。包括多选和单选，默认为多选。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

maxPhotoSelectNumbernumber否是

图片最大的选择数量。最大值为500，受到最大选择总数的限制。默认为500。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

maxVideoSelectNumbernumber否是

视频最大的选择数量。最大值为500，受到系统中所有媒体文件最大选择总数的限制。默认为500。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isSlidingSelectionSupported13+boolean否是

是否支持滑动多选，true表示支持。默认不支持。重复选择场景不支持滑动多选。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

photoBrowserCheckboxPosition13+[number, number]否是

设置大图页checkbox的位置。第一个参数为X方向偏移量，第二个参数为Y方向偏移量。传参范围0-1，代表距离组件左上角0%-100%的偏移量。默认值为[0, 0]。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

gridMargin14+[Margin](尺寸设置.md#ZH-CN_TOPIC_0000002497444850__margin)否是

设置组件宫格页margin。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

photoBrowserMargin14+[Margin](尺寸设置.md#ZH-CN_TOPIC_0000002497444850__margin)否是

设置组件大图页margin。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

singleLineConfig20+[SingleLineConfig](#ZH-CN_TOPIC_0000002497605958__singlelineconfig20)否是

设置组件宫格页单行显示模式。单行模式下，组件不提供打开大图浏览相关功能。组件不支持大图相关回调，PickerController不支持大图相关的接口，接口调用将无效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

uiComponentColorMode20+[PickerColorMode](#ZH-CN_TOPIC_0000002497605958__pickercolormode)否是

Picker的颜色模式。Picker宫格界面除背景色之外其他组件的深浅色风格，包括搜索框、相机入口、安全使用图库提示组件、推荐气泡等组件，一般与backgroundColor配合使用。默认为PickerColorMode.AUTO，跟随系统深浅色切换。

该属性一般设置PickerColorMode.LIGHT时不与深颜色的backgroundColor搭配；设置PickerColorMode.DARK时不与浅颜色的backgroundColor搭配，否则会出现组件背景或文字无法看清楚的问题。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

gridStartOffset20+number否是

组件宫格缩略图第一行与组件顶部的预留空间。默认值0，单位vp。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

gridEndOffset20+number否是

组件宫格缩略图最后一行与组件底部的预留空间。默认值0，单位vp。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

pickerIndex21+number否是

通过设置唯一序号来区分不同的pickerComponent。默认值为-1，-1时不做区分。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

preselectedInfos21+Array<[PreselectedInfo](#ZH-CN_TOPIC_0000002497605958__preselectedinfo21)>否是

支持在指定pickerIndex的PhotoPickerComponent中回显用户已选择的数据。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

badgeConfig21+[BadgeConfig](#ZH-CN_TOPIC_0000002497605958__badgeconfig21)否是

支持配置特殊角标显示。Picker目前仅支持一种类型的角标，详见[BadgeType](#ZH-CN_TOPIC_0000002497605958__badgetype21)。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

#### ItemsDeletedCallback13+

type ItemsDeletedCallback = (baseItemInfos: Array<BaseItemInfo>) => void

已勾选的图片被删除时产生的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明baseItemInfosArray<[BaseItemInfo](#ZH-CN_TOPIC_0000002497605958__baseiteminfo)>是照片的基本信息。

#### ExceedMaxSelectedCallback13+

type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void

选择达到最大选择数量之后再次点击勾选时的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明exceedMaxCountType[MaxCountType](#ZH-CN_TOPIC_0000002497605958__maxcounttype)是达到最大选择数量的类型。类型包含图片最大选择数量、视频最大选择数量以及总的最大选择数量。

#### CurrentAlbumDeletedCallback13+

type CurrentAlbumDeletedCallback = () => void

当前相册被删除时的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

#### videoPlayStateChangedCallback14+

type videoPlayStateChangedCallback = (state: VideoPlayerState) => void

大图页视频播放状态改变时的回调事件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明state[VideoPlayerState](#ZH-CN_TOPIC_0000002497605958__videoplayerstate14)是视频播放状态。

#### MovingPhotoBadgeStateChangedCallback22+

type MovingPhotoBadgeStateChangedCallback = (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void

用户在Picker组件中打开/关闭动态效果时的回调事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明uristring是动态照片uri。state[photoAccessHelper.MovingPhotoBadgeStateType](Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22)是动态照片状态。

#### PickerController

应用可通过PickerController向picker组件发送数据。

**装饰器类型**：@Observed

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

#### setData

setData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送数据，并通过DataType来区分具体发送什么类型的数据。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明dataType[DataType](#ZH-CN_TOPIC_0000002497605958__datatype)是发送数据的数据类型。dataObject是发送的数据。

#### addData21+

addData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送增加配置数据。通过[DataType](#ZH-CN_TOPIC_0000002497605958__datatype)来区分具体发送的数据类型，该方法仅支持SET_BADGE_CONFIGS类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明dataType[DataType](#ZH-CN_TOPIC_0000002497605958__datatype)是发送增加配置数据的数据类型。dataObject是发送的增加配置数据。

#### deleteData21+

deleteData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送移除配置数据。通过[DataType](#ZH-CN_TOPIC_0000002497605958__datatype)来区分具体发送的数据类型，该方法仅支持SET_BADGE_CONFIGS类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明dataType[DataType](#ZH-CN_TOPIC_0000002497605958__datatype)是发送移除配置数据的数据类型。dataObject是发送的移除配置数据。

#### setMaxSelected

setMaxSelected(maxSelected: MaxSelected): void

应用可通过该接口，实时地设置图片的最大选择数量、视频的最大选择数量以及总的最大选择数量。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明maxSelected[MaxSelected](#ZH-CN_TOPIC_0000002497605958__maxselected)是最大选择数量。

#### setPhotoBrowserItem

setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void

应用可通过该接口,切换picker组件至大图浏览模式浏览图片；当已处于大图浏览模式时，切换浏览的图片。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明uristring是指定大图浏览的图片uri。仅支持指定用户已选择的图片，未选择的图片不生效。photoBrowserRange[PhotoBrowserRange](#ZH-CN_TOPIC_0000002497605958__photobrowserrange)否打开大图浏览模式后，左右滑动切换浏览图片的范围，可配置仅浏览用户选择的或浏览全部图片，视频。默认：PhotoBrowserRange.ALL。浏览全部图片，视频。

#### exitPhotoBrowser13+

exitPhotoBrowser(): void

应用可通过该接口，向picker发送退出大图的通知。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

#### setPhotoBrowserUIElementVisibility13+

setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void

应用可通过该接口，设置大图页大图预览组件外其他UI元素是否可见。不设置则默认可见。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明elementsArray<[PhotoBrowserUIElement](#ZH-CN_TOPIC_0000002497605958__photobrowseruielement13)>是大图页大图预览组件外其他UI元素。isVisibleboolean是是否可见。true表示可见，默认为false。

#### replacePhotoPickerPreview15+

replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void

应用可通过该接口，将photoPicker中用户勾选的图片替换为应用后期编辑修改后的图片。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明originalUristring是原uri，将会被替换掉的uri。newUristring是新uri，即替换后的uri。基于originalUri修改后期望在photoPicker上替换originalUri显示的，暂存在应用沙箱的图片/视频uri。callbackAsyncCallback<void>是调用接口完成替换后的回调。

#### saveTrustedPhotoAssets15+

saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void

应用可通过该接口，保存对应uri列表的文件。使用时，一般结合[replacePhotoPickerPreview](#ZH-CN_TOPIC_0000002497605958__replacephotopickerpreview15)接口使用，将替换显示成功后的应用沙箱图片/视频newUris保存到图库。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明trustedUrisArray<string>是需要保存到图库的应用沙箱图片/视频uri。trustedUris一般来自[replacePhotoPickerPreview](#ZH-CN_TOPIC_0000002497605958__replacephotopickerpreview15)替换显示成功的newUri。callbackAsyncCallback<Array<string>>是返回保存后新生成的媒体库文件对应的uri。configsArray<[photoAccessHelper.PhotoCreationConfig](zh-cn_topic_0000002529285945.html#ZH-CN_TOPIC_0000002529285945__photocreationconfig12)>否

需要保存的文件对应的配置参数。

**注意：**

传入'subtype'选项，配置项不生效，仅支持保存DEFAULT类型图片。

saveMode[SaveMode](#ZH-CN_TOPIC_0000002497605958__savemode15)否图片保存模式。

#### updatePickerOptions22+

updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>

应用通过该接口，更新PhotoPickerComponent的属性。使用Promise异步回调。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

参数名类型必填说明updateConfig[UpdatablePickerConfigs](#ZH-CN_TOPIC_0000002497605958__updatablepickerconfigs22)是支持更新的PhotoPickerComponent属性，为[PickerOptions](#ZH-CN_TOPIC_0000002497605958__pickeroptions)的子集。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

#### BaseItemInfo

图片、视频相关信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明uristring否是

图片、视频的uri。

当[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)为THUMBNAIL时支持，否则为空。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

mimeTypestring否是

图片、视频的mimeType。

当[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)为THUMBNAIL时支持，否则为空。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

widthnumber否是

图片、视频的宽（单位：像素）。

当[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)为THUMBNAIL时支持，否则为空。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

heightnumber否是

图片、视频的高（单位：像素）。

当[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)为THUMBNAIL时支持，否则为空。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

sizenumber否是

图片、视频的大小（单位：字节）。

当[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)为THUMBNAIL时支持，否则为空。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

durationnumber否是

视频的时长（单位：毫秒），图片/动态图片时返回-1。

当[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)为THUMBNAIL时支持，否则为空。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

photoSubType21+[photoAccessHelper.PhotoSubtype](Enums.md#ZH-CN_TOPIC_0000002529445919__photosubtype12)否是

图片类型，包括DEFAULT、MOVING_PHOTO和BRUST。

非特殊类型图片默认为DEFAULT（0）。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

dynamicRangeType21+[photoAccessHelper.DynamicRangeType](Enums.md#ZH-CN_TOPIC_0000002529445919__dynamicrangetype12)否是

媒体文件动态范围模型，包括HDR和SDR。

对于movingPhoto专指封面图片的动态范围类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

orientation21+number否是

图片/视频方向信息。

1.“TOP-left”，图像未旋转。

2.“TOP-right”，镜像水平翻转。

3.“Bottom-right”，图像旋转180°。

4.“Bottom-left”，镜像垂直翻转。

5.“Left-top”，先镜像水平翻转，再顺时针旋转270°。

6.“Right-top”，顺时针旋转90°。

7.“Right-bottom”，先镜像水平翻转，再顺时针旋转90°。

8.“Left-bottom”，顺时针旋转270°。

携带镜像信息的图片无论旋转与否其宽高属性都与原图保持一致，无镜像信息的图片其宽高属性会更新为旋转后的结果。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

movingPhotoBadgeState22+[photoAccessHelper.MovingPhotoBadgeStateType](Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22)否是

动态照片的状态。

当[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)为THUMBNAIL时支持，否则为空。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

VideoMode22+[photoAccessHelper.VideoMode](Enums.md#ZH-CN_TOPIC_0000002529445919__videomode22)否是

视频文件的log模式。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

#### ItemInfo

继承自[BaseItemInfo](#ZH-CN_TOPIC_0000002497605958__baseiteminfo)，增加私有参数itemType。

图片、视频相关信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明itemType[ItemType](#ZH-CN_TOPIC_0000002497605958__itemtype)否是被点击的item类型。包括缩略图item和相机item。

#### PhotoBrowserInfo

大图相关信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明animatorParams[AnimatorParams](#ZH-CN_TOPIC_0000002497605958__animatorparams)否是进入、退出大图界面时的动效参数。

#### AnimatorParams

进退大图动效参数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明durationnumber否是动效时长（单位：毫秒）。curve[Curve](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__curve) | [ICurve](@ohos.curves (插值计算).md#ZH-CN_TOPIC_0000002497604788__icurve9) | string否是动效曲线。

#### MaxSelected

最大选择数量。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明dataMap<[MaxCountType](#ZH-CN_TOPIC_0000002497605958__maxcounttype), number>否是最大选择数量（包含图片的最大选择数量、视频的最大选择数量以及总的最大选择数量）。

#### SingleLineConfig20+

单行显示模式配置项。单行模式下，组件不提供打开大图浏览相关功能。组件不支持大图相关回调，PickerController不支持大图相关的接口，接口调用将无效。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明itemDisplayRatio[ItemDisplayRatio](#ZH-CN_TOPIC_0000002497605958__itemdisplayratio20)否是宫格显示宽高比，支持1:1，原图宽高比两种模式，默认为宽高比1:1显示。itemBorderRadius[Length](zh-cn_topic_0000002497604974.html#ZH-CN_TOPIC_0000002497604974__length) | [BorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9) | [LocalizedBorderRadiuses](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizedborderradiuses12)否是宫格圆角属性。itemGap[Length](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否是宫格间距。

#### BadgeConfig21+

特殊角标配置项。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明badgeType[BadgeType](#ZH-CN_TOPIC_0000002497605958__badgetype21)否是特殊角标的类型。urisArray<string>否是显示角标的资产uri数据。

#### PreselectedInfo21+

预选中的文件以及文件对应的PhotoPickerComponent序号。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明uristring否否选中媒体文件的uri。preselectablePickerIndexnumber否是限制仅在指定序号的PhotoPickerComponent中进行自动选中；默认为-1，即可支持在任意序号的PhotoPickerComponent中自动选中。

#### UpdatablePickerConfigs22+

支持更新的PhotoPickerComponent属性，为[PickerOptions](#ZH-CN_TOPIC_0000002497605958__pickeroptions)的子集。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明mimeType[photoAccessHelper.PhotoViewMIMETypes](Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes)否是

可选择的媒体文件类型。

若无此参数，则默认为图片和视频类型。

mimeTypeFilter[photoAccessHelper.MimeTypeFilter](Classes (其他).md#ZH-CN_TOPIC_0000002497605950__mimetypefilter19)否是

文件类型的过滤配置，支持指定多个类型过滤。

- 当配置mimeTypeFilter参数时，mimeType的配置自动失效。

- 当配置该参数时，仅显示配置过滤类型对应的媒体文件，建议提示用户仅支持选择指定类型的图片/视频。

maxSelectNumbernumber否是

选择媒体文件数量的最大值（单位：个）。

最大可设置为500，若不设置则默认为50。

maxPhotoSelectNumbernumber否是

图片最大的选择数量（单位：个）。

最大值为500，受到最大选择总数的限制。默认为500。

maxVideoSelectNumbernumber否是

视频最大的选择数量（单位：个）。

最大值为500，受到系统中所有媒体文件最大选择总数的限制。默认为500。

selectMode[SelectMode](#ZH-CN_TOPIC_0000002497605958__selectmode)否是

Picker选择模式。

包括多选和单选，默认为多选。

singleSelectionMode[photoAccessHelper.SingleSelectionMode](Enums.md#ZH-CN_TOPIC_0000002529445919__singleselectionmode18)否是单选模式类型。默认为大图预览模式（SingleSelectionMode.BROWSER_MODE）。isRepeatSelectSupportedboolean否是

是否支持单张图片重复选择。

true表示支持，false表示不支持。默认为false。

preselectedUrisArray<string>否是已选择图片的uri数据。checkBoxColorstring否是

勾选框的背景色。

格式为8位十六进制颜色代码。

backgroundColorstring否是

Picker宫格页面背景色。

格式为8位十六进制颜色代码。

checkboxTextColorstring否是

勾选框内文本颜色。

格式为8位十六进制颜色代码。

photoBrowserBackgroundColorMode[PickerColorMode](#ZH-CN_TOPIC_0000002497605958__pickercolormode)否是

大图背景颜色。

包括跟随系统、浅色模式以及深色模式，默认为跟随系统。

uiComponentColorMode[PickerColorMode](#ZH-CN_TOPIC_0000002497605958__pickercolormode)否是

Picker UI组件的颜色模式。

Picker宫格界面除背景色之外其他组件的深浅色风格，包括搜索框、相机入口、安全使用图库提示组件、推荐气泡等组件，一般与backgroundColor配合使用。默认为PickerColorMode.AUTO，跟随系统深浅色切换。

该属性设置为PickerColorMode.LIGHT时，一般不与深颜色的backgroundColor搭配；设置为PickerColorMode.DARK时，不与浅颜色的backgroundColor搭配，避免出现组件背景或文字无法看清楚的问题。

#### DataType

枚举，PickerController向picker组件发送数据的数据类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明SET_SELECTED_URIS1

发送已选择的数据列表，通知picker组件勾选状态刷新，需要传入string数组类型。

例如：应用在自己的页面中删除某张图片后，需要把剩下的已选择的数据列表通过setData接口通知到picker组件，从而触发picker组件勾选框状态刷新正确。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

SET_ALBUM_URI2

发送已选择相册，通知picker组件刷新相册，需要传入string类型。

例如：应用在自己的页面中选择相册后，需要把已选择的相册uri通过setData接口通知到picker组件，从而触发picker组件刷新相册数据。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

SET_SELECTED_INFO21+3

发送已选择的文件uri以及选中的picker序号。当picker序号与参数中的picker序号匹配时，已选择文件支持在当前picker里自动选中。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

SET_BADGE_CONFIGS21+4

发送需要显示角标的配置，类型为[badgeConfig](#ZH-CN_TOPIC_0000002497605958__badgeconfig21)，包含角标的类型和对应文件uri的数据列表。配置后，对应文件会显示配置类型的角标。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

#### ItemType

被点击item的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明THUMBNAIL0图片、视频item（缩略图item）。CAMERA1相机item。

#### ClickType

点击操作的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明SELECTED0选择操作（勾选图片或者点击相机item）。DESELECTED1取消选择操作（取消勾选图片）。

#### PickerOrientation

Picker宫格页面滑动预览的方向。

从API20开始，该能力支持配置；在API12-19，该能力设置不生效，默认为竖直方向。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明VERTICAL0竖直方向。HORIZONTAL1水平方向。

#### SelectMode

选择模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明SINGLE_SELECT0单选模式。MULTI_SELECT1多选模式。

#### PickerColorMode

Picker的颜色模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core。

名称值说明AUTO0跟随系统。LIGHT1浅色模式。DARK2深色模式。

#### ReminderMode

最大选择数量提示方式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明NONE0不提示。TOAST1弹toast提示。MASK2蒙灰提示。

#### MaxCountType

最大选择数量的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明TOTAL_MAX_COUNT0总的最大选择数量。PHOTO_MAX_COUNT1图片的最大选择数量（不能大于总的最大选择数量）。VIDEO_MAX_COUNT2视频的最大选择数量（不能大于总的最大选择数量）。

#### PhotoBrowserRange

打开大图浏览模式后，左右滑动切换浏览图片的范围。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明ALL0全部图片，视频。SELECTED_ONLY1仅用户已选择的图片，视频。

#### PhotoBrowserUIElement13+

大图页大图预览组件外其他UI元素。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明CHECKBOX0大图页勾选框。BACK_BUTTON1大图页返回按钮。

#### SaveMode15+

图片/视频保存模式。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明SAVE_AS0另存为新的图片/视频。OVERWRITE1覆盖原有图片/视频，覆盖后支持在图库中将保存内容回退，还原成原始图片/视频。

#### BadgeType21+

表示特殊角标类型的枚举。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明BADGE_UPLOADED0已上传。

#### VideoPlayerState14+

视频播放状态。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明PLAYING0视频播放中。PAUSED1视频播放暂停。STOPPED2视频播放停止。SEEK_START3开始拖拽进度条。SEEK_FINISH4结束拖拽进度条。

#### ItemDisplayRatio20+

单行布局宫格显示宽高比模式，包括1:1和原图宽高比两种模式。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称值说明SQUARE_RATIO01:1比例显示。ORIGINAL_SIZE_RATIO1原图宽高比显示。

#### 示例

```ets
// xxx.ets
import {
  PhotoPickerComponent,
  PickerController,
  PickerOptions,
  DataType,
  BaseItemInfo,
  ItemInfo,
  PhotoBrowserInfo,
  ItemType,
  ClickType,
  MaxCountType,
  PhotoBrowserRange,
  PhotoBrowserUIElement,
  ItemsDeletedCallback,
  ExceedMaxSelectedCallback,
  CurrentAlbumDeletedCallback,
  videoPlayStateChangedCallback,
  VideoPlayerState
} from '@ohos.file.PhotoPickerComponent';
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PickerDemo {
  pickerOptions: PickerOptions = new PickerOptions();
  @State pickerController: PickerController = new PickerController();
  @State selectUris: string[] = [];
  @State currentUri: string = '';
  @State isBrowserShow: boolean = false;
  private selectedItemsDeletedCallback: ItemsDeletedCallback =
    (baseItemInfos: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(baseItemInfos);
  private exceedMaxSelectedCallback: ExceedMaxSelectedCallback =
    (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType);
  private currentAlbumDeletedCallback: CurrentAlbumDeletedCallback = () => this.onCurrentAlbumDeleted();
  private videoPlayStateChangedCallback: videoPlayStateChangedCallback =
    (state: VideoPlayerState) => this.videoPlayStateChanged(state);
  private thumbnail: PixelMap[] = [];
  private assets: photoAccessHelper.PhotoAsset[] = [];

  aboutToAppear() {
    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
    this.pickerOptions.maxSelectNumber = 5;
    this.pickerOptions.isSearchSupported = false;
    this.pickerOptions.isPhotoTakingSupported = false;
    this.pickerOptions.photoBrowserCheckboxPosition = [0.5, 0.5];
    // 其他属性.....
  }

  private onSelect(uri: string): void {
    // 添加。
    if (uri) {
      this.selectUris.push(uri);
    }
  }

  private onDeselect(uri: string): void {
    // 移除。
    if (uri) {
      this.selectUris = this.selectUris.filter((item: string) => {
        return item != uri;
      })
    }
  }

  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {
      // 点击相机item。
      return true; // 返回true则拉起系统相机，若应用需要自行处理则返回false。
    } else {
      if (clickType === ClickType.SELECTED) {
        // 应用做自己的业务处理（注：非长耗时操作，例如opensync大文件）。
        if (uri) {
          this.selectUris.push(uri);
          this.pickerOptions.preselectedUris = [...this.selectUris];
        }
        return true; // 返回true则勾选，否则不响应勾选。
      } else {
        if (uri) {
          this.selectUris = this.selectUris.filter((item: string) => {
            return item != uri;
          });
          this.pickerOptions.preselectedUris = [...this.selectUris];
        }
      }
      return true;
    }
  }

  private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    // 进入大图的回调。
    this.isBrowserShow = true;
    return true;
  }

  private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    // 退出大图的回调。
    this.isBrowserShow = false;
    return true;
  }

  private onPickerControllerReady(): void {
    // 接收到该回调后，便可通过pickerController相关接口向picker发送数据，在此之前不生效。
    let elements: number[] = [PhotoBrowserUIElement.BACK_BUTTON];
    this.pickerController.setPhotoBrowserUIElementVisibility(elements, false); // 设置大图页不显示返回按钮。
  }

  private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
    // 大图左右滑动的回调。
    this.currentUri = browserItemInfo.uri ?? '';
    return true;
  }

  private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
    // 已勾选图片被删除时的回调。
  }

  private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
    // 超过最大选择数量再次点击时的回调。
  }

  private onCurrentAlbumDeleted(): void {
    // 当前相册被删除时的回调。
  }

  private videoPlayStateChanged(state: VideoPlayerState): void {
    // 当视频播放状态变化时回调。
  }
  build() {
    Flex({
      direction: FlexDirection.Column,
      justifyContent: FlexAlign.Center,
      alignItems: ItemAlign.Center
    }) {
      Column() {
        if (this.isBrowserShow) {
          // 这里模拟应用自己的大图返回按钮。
          Row() {
            Button("退出大图").width('33%').height('8%').onClick(() => {
              this.pickerController.exitPhotoBrowser();
            })
          }.margin({ bottom: 20 })
        }

        PhotoPickerComponent({
          pickerOptions: this.pickerOptions,
          // onSelect: (uri: string): void => this.onSelect(uri),
          // onDeselect: (uri: string): void => this.onDeselect(uri),
          onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo,
            clickType), // 该接口可替代上面两个接口。
          onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
          onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
          onPickerControllerReady: (): void => this.onPickerControllerReady(),
          onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
          onSelectedItemsDeleted: this.selectedItemsDeletedCallback,
          onExceedMaxSelected: this.exceedMaxSelectedCallback,
          onCurrentAlbumDeleted: this.currentAlbumDeletedCallback,
          onVideoPlayStateChanged: this.videoPlayStateChangedCallback,
          pickerController: this.pickerController,
        }).height('60%').width('100%')

        // 这里模拟应用侧底部的选择栏。
        if (this.isBrowserShow) {
          Row() {
            ForEach(this.assets, async (asset: photoAccessHelper.PhotoAsset, index) => {
              if (asset.uri === this.currentUri) {
                Image(this.thumbnail[index])
                  .height('10%')
                  .width('10%')
                  .onClick(() => {
                  })
                  .borderWidth(1)
                  .borderColor('red')
              } else {
                Image(this.thumbnail[index]).height('10%').width('10%').onClick(() => {
                  this.pickerController.setData(DataType.SET_SELECTED_URIS, this.selectUris);
                  this.pickerController.setPhotoBrowserItem(asset.uri, PhotoBrowserRange.ALL);
                })
              }
            }, (uri: string) => JSON.stringify(uri))
          }
        } else {
          Button('预览').width('33%').height('5%').onClick(async () => {
            if (this.selectUris.length > 0) {
              this.thumbnail = [];
              this.assets = [];
              for (let selectUri of this.selectUris) {
                let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
                predicates.equalTo(photoAccessHelper.PhotoKeys.URI, selectUri);
                let fetchOptions: photoAccessHelper.FetchOptions = {
                  fetchColumns: [],
                  predicates: predicates
                };
                let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                let photoHelper = photoAccessHelper.getPhotoAccessHelper(context);
                let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
                  await photoHelper.getAssets(fetchOptions);
                let asset = await fetchResult.getFirstObject()
                this.assets.push(asset);
                this.thumbnail.push(await asset.getThumbnail())
              }
              this.pickerController.setPhotoBrowserItem(this.selectUris[0], PhotoBrowserRange.SELECTED_ONLY);
            }
          })
        }
      }
    }
  }
}
```