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
  ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, SingleLineConfig,
    BadgeConfig, PreselectedInfo, SaveMode, BadgeType, VideoPlayerState, ItemDisplayRatio
} from '@kit.MediaLibraryKit';
```

#### 属性

支持[通用属性]([通用属性](../../topics/misc/通用属性.md).md)。

#### PhotoPickerComponent

PhotoPickerComponent({ pickerOptions?: PickerOptions, onSelect?: (uri: string) => void, onDeselect?: (uri: string) => void, onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean, onItemClickedNotify?: ItemClickedNotifyCallback, onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean, onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean, onPickerControllerReady?: () => void, onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean, onSelectedItemsDeleted?: ItemsDeletedCallback, onExceedMaxSelected?: ExceedMaxSelectedCallback, onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback, onVideoPlayStateChanged?: videoPlayStateChangedCallback, pickerController: PickerController })

应用可以在布局中嵌入PhotoPickerComponent组件，通过此组件，应用无需申请权限，即可访问公共目录中的图片或视频文件。

如果当前PhotoPickerComponent组件嵌套在Tabs组件中使用，Tabs组件的左右滑动会与图片选择大图界面的左右滑动切换手势发生冲突。

可在进退大图的回调中设置Tabs组件是否支持滑动来规避，该问题将在后续版本修复。

**装饰器类型**：@Component

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| pickerOptions | PickerOptions | 否 | - | picker配置参数信息。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onSelect | (uri: string) => void | 否 | - | 用户在Picker组件中勾选图片时产生的回调事件，将图片uri报给应用。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onDeselect | (uri: string) => void | 否 | - | 用户在Picker组件中取消勾选图片时产生的回调事件，同时也会将图片uri报给应用。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onItemClicked | (itemInfo: ItemInfo, clickType: ClickType) => boolean | 否 | - | 用户在picker组件中点击宫格产生的回调事件。 点击图片（缩略图宫格）时，返回值为true则勾选此图片，否则不响应勾选，URI不授权；点击相机宫格，返回值为true则拉起系统相机，否则不拉起相机，由应用自行处理。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onItemClickedNotify23+ | ItemClickedNotifyCallback | 否 | - | 用户在picker组件中点击宫格产生的回调事件。 应用可执行自身是否选中逻辑，需要配合addData方法一同使用，通过ADD_ITEM_CLICK_RESULT进行选中或不选中。若未设置选中结果，在2秒或PhotoPicker被关闭时取消授权。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| onPinchGridSwitched23+ | (gridLevel: GridLevel) => void | 否 | - | 宫格捏合时产生的回调事件。仅在gridPinchModeType配置为FULL_FUNCTION_GRID下会被触发。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| onEnterPhotoBrowser | (photoBrowserInfo: PhotoBrowserInfo) => boolean | 否 | - | 点击进入大图时产生的回调事件，将大图相关信息报给应用。不对返回值做特殊处理。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onExitPhotoBrowser | (photoBrowserInfo: PhotoBrowserInfo) => boolean | 否 | - | 退出大图时产生的回调事件，将大图相关信息报给应用。不对返回值做特殊处理。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onPickerControllerReady | () => void | 否 | - | 当pickerController可用时产生的回调事件。 调用PickerController相关接口需在该回调后才能生效。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onPhotoBrowserChanged | (browserItemInfo: BaseItemInfo) => boolean | 否 | - | 大图左右滑动时产生的回调事件，将大图相关信息报给应用。仅在多选模式下生效。不对返回值做特殊处理。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onSelectedItemsDeleted13+ | ItemsDeletedCallback | 否 | - | 已勾选的图片被删除时产生的回调，并将被删除图片的相关信息回调给应用。 元服务API：从API version 13开始，该接口支持在元服务中使用。 |
| onExceedMaxSelected13+ | ExceedMaxSelectedCallback | 否 | - | 选择达到最大选择数量（最大图片选择数量或者是最大视频选择数量亦或是总的最大选择数量）之后再次点击勾选时产生的回调。 - 若选择的数量达到了最大图片选择数量且未达到总的最大选择数量则回调的参数exceedMaxCountType为MaxCountType.PHOTO_MAX_COUNT。 - 若选择的数量达到了最大视频选择数量且未达到总的最大选择数量则回调的参数exceedMaxCountType为MaxCountType.VIDEO_MAX_COUNT。 - 只要选择的数量达到了总的最大选择数量则回调的参数exceedMaxCountType为MaxCountType.TOTAL_MAX_COUNT。 元服务API：从API version 13开始，该接口支持在元服务中使用。 |
| onCurrentAlbumDeleted13+ | CurrentAlbumDeletedCallback | 否 | - | 当前相册被删除时产生的回调。 当前相册是指通过pickerController.setData(DataType.SET_ALBUM_URI, currentAlbumUri)接口设置给宫格组件的相册，即“currentAlbumUri”。 当前相册被删除后若使用方刷新自己的相册标题栏，使用方可以设置自己的标题栏名称为默认的相册名例如“图片和视频”、“图片”或“视频”，然后通过pickerController.setData(DataType.SET_ALBUM_URI, '')接口传空串去刷新宫格页为默认相册。 元服务API：从API version 13开始，该接口支持在元服务中使用。 |
| onVideoPlayStateChanged14+ | videoPlayStateChangedCallback | 否 | - | 大图页视频播放状态改变时回调。 元服务API：从API version 14开始，该接口支持在元服务中使用。 |
| pickerController | PickerController | 是 | @ObjectLink | 应用可通过PickerController向Picker组件发送数据。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| onMovingPhotoBadgeStateChanged22+ | MovingPhotoBadgeStateChangedCallback | 否 | - | 用户在Picker组件中打开/关闭动态效果时产生的回调。将图片uri和动态照片状态报给应用。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| onScrollStopAtStart23+ | ScrollStopAtStartCallback | 否 | - | 用户在Picker组件滑动停止、处于宫格内容起始位置时的回调。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| onScrollStopAtEnd23+ | ScrollStopAtEndCallback | 否 | - | 用户在Picker组件滑动停止、处于宫格内容结束位置时的回调。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| onPhotoBrowserChangeStart23+ | PhotoBrowserChangeStartCallback | 否 | - | 宫格试图进入到大图视图、大图浏览切换时产生的回调。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| onError23+ | ErrorCallback | 否 | - | 使用PhotoPickerComponent组件发生错误时产生的回调。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |

#### PickerOptions

Picker配置选项，继承自[photoAccessHelper.BaseSelectOptions](Classes (其他).md#ZH-CN_TOPIC_0000002522242084__baseselectoptions)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| checkBoxColor | string | 否 | 是 | 勾选框的背景色。格式为8位十六进制颜色代码。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor | string | 否 | 是 | picker宫格页面背景色。格式为8位十六进制颜色代码。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| isRepeatSelectSupported | boolean | 否 | 是 | 是否支持单张图片重复选择。true表示支持。默认不支持。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| checkboxTextColor | string | 否 | 是 | 勾选框内文本颜色。格式为8位十六进制颜色代码（该能力从API version 19开始支持，API version 19之前系统默认为白色）。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| photoBrowserBackgroundColorMode | PickerColorMode | 否 | 是 | 大图背景颜色。包括跟随系统、浅色模式以及深色模式，默认为跟随系统。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| maxSelectedReminderMode | ReminderMode | 否 | 是 | 选择数量达到最大时的提示方式。包括弹toast提示、不提示以及蒙层提示，默认为弹toast提示。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| orientation | PickerOrientation | 否 | 是 | 宫格页面滑动预览方向，包括水平和竖直两个方向，默认为竖直方向（该能力从API version 20开始支持，API version 20之前系统默认为竖直方向）。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| selectMode | SelectMode | 否 | 是 | 选择模式。包括多选和单选，默认为多选。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| maxPhotoSelectNumber | number | 否 | 是 | 图片最大的选择数量。最大值为500，受到最大选择总数的限制。默认为500。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| maxVideoSelectNumber | number | 否 | 是 | 视频最大的选择数量。最大值为500，受到系统中所有媒体文件最大选择总数的限制。默认为500。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| isSlidingSelectionSupported13+ | boolean | 否 | 是 | 是否支持滑动多选，true表示支持。默认不支持。重复选择场景不支持滑动多选。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| photoBrowserCheckboxPosition13+ | [number, number] | 否 | 是 | 设置大图页checkbox的位置。第一个参数为X方向偏移量，第二个参数为Y方向偏移量。传参范围0-1，代表距离组件左上角0%-100%的偏移量。默认值为[0, 0]。 元服务API： 从API version 13开始，该接口支持在元服务中使用。 |
| grid[Margin](../../topics/components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__margin)14+ | Margin | 否 | 是 | 设置组件宫格页margin。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| photoBrowser[Margin](../../topics/components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__margin)14+ | Margin | 否 | 是 | 设置组件大图页margin。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| singleLineConfig20+ | SingleLineConfig | 否 | 是 | 设置组件宫格页单行显示模式。单行模式下，组件不提供打开大图浏览相关功能。组件不支持大图相关回调，PickerController不支持大图相关的接口，接口调用将无效。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| uiComponentColorMode20+ | PickerColorMode | 否 | 是 | Picker的颜色模式。Picker宫格界面除背景色之外其他组件的深浅色风格，包括搜索框、相机入口、安全使用图库提示组件、推荐气泡等组件，一般与backgroundColor配合使用。默认为PickerColorMode.AUTO，跟随系统深浅色切换。 该属性一般设置PickerColorMode.LIGHT时不与深颜色的backgroundColor搭配；设置PickerColorMode.DARK时不与浅颜色的backgroundColor搭配，否则会出现组件背景或文字无法看清楚的问题。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| gridStartOffset20+ | number | 否 | 是 | 组件宫格缩略图第一行与组件顶部的预留空间。默认值0，单位vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| gridEndOffset20+ | number | 否 | 是 | 组件宫格缩略图最后一行与组件底部的预留空间。默认值0，单位vp。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| pickerIndex21+ | number | 否 | 是 | 通过设置唯一序号来区分不同的pickerComponent。默认值为-1，-1时不做区分。 元服务API： 从API version 21开始，该接口支持在元服务中使用。 |
| preselectedInfos21+ | Array<PreselectedInfo> | 否 | 是 | 支持在指定pickerIndex的PhotoPickerComponent中回显用户已选择的数据。 元服务API： 从API version 21开始，该接口支持在元服务中使用。 |
| badgeConfig21+ | BadgeConfig | 否 | 是 | 支持配置特殊角标显示。Picker目前仅支持一种类型的角标，详见BadgeType。 元服务API： 从API version 21开始，该接口支持在元服务中使用。 |
| isSlidingSupported23+ | boolean | 否 | 是 | 是否屏蔽PhotoPickerComponent的滚动。true表示不屏蔽滚动事件，响应用户滚动。false表示屏蔽滚动事件，不响应用户滚动。 默认为true。 模型约束：此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| edgeEffect23+ | EdgeEffect | 否 | 是 | Picker宫格页滑动到边缘处的滑动效果。 默认为EdgeEffect.Spring。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| appAlbumFilters23+ | Array<string> | 否 | 是 | 仅显示与指定bundle name对应的相册内容。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |

#### ItemsDeletedCallback13+

type ItemsDeletedCallback = (baseItemInfos: Array<BaseItemInfo>) => void

已勾选的图片被删除时产生的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| baseItemInfos | Array<BaseItemInfo> | 是 | 照片的基本信息。 |

#### ExceedMaxSelectedCallback13+

type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void

选择达到最大选择数量之后再次点击勾选时的回调事件。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exceedMaxCountType | MaxCountType | 是 | 达到最大选择数量的类型。类型包含图片最大选择数量、视频最大选择数量以及总的最大选择数量。 |

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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | VideoPlayerState | 是 | 视频播放状态。 |

#### MovingPhotoBadgeStateChangedCallback22+

type MovingPhotoBadgeStateChangedCallback = (uri: string, state: [photoAccessHelper.MovingPhotoBadgeStateType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22)) => void

用户在Picker组件中打开/关闭动态效果时的回调事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 动态照片uri。 |
| state | [photoAccessHelper.MovingPhotoBadgeStateType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22) | 是 | 动态照片状态。 |

**ScrollStopAtStartCallback23+**

type ScrollStopAtStartCallback = () => void

表示用户滑动picker宫格页，当滚动停止并处于宫格内容开始位置时的回调事件类型。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

**ItemClickedNotifyCallback23+**

type ItemClickedNotifyCallback = (itemInfo: ItemInfo, clickType: ClickType) => void

用户在picker组件中点击宫格产生的回调事件。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemInfo | ItemInfo | 是 | 被点击的宫格类型。包括缩略图宫格和相机宫格。 |
| clickType | ClickType | 是 | 点击操作的类型。 |

**ScrollStopAtEndCallback23+**

type ScrollStopAtEndCallback = () => void

表示用户滑动picker宫格页，当滚动停止并处于宫格内容结束位置时的回调事件类型。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

**PhotoBrowserChangeStartCallback23+**

type PhotoBrowserChangeStartCallback = (targetPhotoInfo: BaseItemInfo) => void

用户在Picker组件中打开/关闭动态效果时的回调事件。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetPhotoInfo | baseItemInfo | 是 | 照片的基本信息。 |

**ErrorCallback23+**

type ErrorCallback = (pickerError: PickerError) => void

PhotoPickerComponent产生错误时的回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pickerError | PickerError | 是 | 产生的错误的基本信息。 |

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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | DataType | 是 | 发送数据的数据类型。 |
| data | Object | 是 | 发送的数据。 |

#### addData21+

addData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送增加配置数据。通过[DataType](#ZH-CN_TOPIC_0000002522242092__datatype)来区分具体发送的数据类型，该方法仅支持SET_BADGE_CONFIGS类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | DataType | 是 | 发送增加配置数据的数据类型。 |
| data | Object | 是 | 发送的增加配置数据。 |

#### deleteData21+

deleteData(dataType: DataType, data: Object): void

应用可通过该接口向picker组件发送移除配置数据。通过[DataType](#ZH-CN_TOPIC_0000002522242092__datatype)来区分具体发送的数据类型，该方法仅支持SET_BADGE_CONFIGS类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataType | DataType | 是 | 发送移除配置数据的数据类型。 |
| data | Object | 是 | 发送的移除配置数据。 |

#### setMaxSelected

setMaxSelected(maxSelected: MaxSelected): void

应用可通过该接口，实时地设置图片的最大选择数量、视频的最大选择数量以及总的最大选择数量。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxSelected | MaxSelected | 是 | 最大选择数量。 |

#### setPhotoBrowserItem

setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void

应用可通过该接口,切换picker组件至大图浏览模式浏览图片；当已处于大图浏览模式时，切换浏览的图片。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 指定大图浏览的图片uri。仅支持指定用户已选择的图片，未选择的图片不生效。 |
| photoBrowserRange | PhotoBrowserRange | 否 | 打开大图浏览模式后，左右滑动切换浏览图片的范围，可配置仅浏览用户选择的或浏览全部图片，视频。默认：PhotoBrowserRange.ALL。浏览全部图片，视频。 |

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

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Array<PhotoBrowserUIElement> | 是 | 大图页大图预览组件外其他UI元素。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，默认为false。 |

#### replacePhotoPickerPreview15+

replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void

应用可通过该接口，将photoPicker中用户勾选的图片替换为应用后期编辑修改后的图片。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalUri | string | 是 | 原uri，将会被替换掉的uri。 |
| newUri | string | 是 | 新uri，即替换后的uri。基于originalUri修改后期望在photoPicker上替换originalUri显示的，暂存在应用沙箱的图片/视频uri。 |
| callback | AsyncCallback<void> | 是 | 调用接口完成替换后的回调。 |

#### saveTrustedPhotoAssets15+

saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void

应用可通过该接口，保存对应uri列表的文件。使用时，一般结合[replacePhotoPickerPreview](#ZH-CN_TOPIC_0000002522242092__replacephotopickerpreview15)接口使用，将替换显示成功后的应用沙箱图片/视频newUris保存到图库。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| trustedUris | Array<string> | 是 | 需要保存到图库的应用沙箱图片/视频uri。trustedUris一般来自replacePhotoPickerPreview替换显示成功的newUri。 |
| callback | AsyncCallback<Array<string>> | 是 | 返回保存后新生成的媒体库文件对应的uri。 |
| configs | Array<photoAccessHelper.PhotoCreationConfig> | 否 | 需要保存的文件对应的配置参数。 注意： 传入'subtype'选项，配置项不生效，仅支持保存DEFAULT类型图片。 |
| saveMode | SaveMode | 否 | 图片保存模式。 |

#### updatePickerOptions22+

updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>

应用通过该接口，更新PhotoPickerComponent的属性。使用Promise异步回调。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| updateConfig | UpdatablePickerConfigs | 是 | 支持更新的PhotoPickerComponent属性，为PickerOptions的子集。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**saveTrustedPhotoAssetsEx23+**

saveTrustedPhotoAssetsEx(trustedUris: Array<string>,settings?: Array<photoAccessHelper.CreationSetting>, saveMode?: SaveMode): Promise<Array<string>>

应用可通过该接口保存对应URI列表中的文件。使用Promise异步回调。


此接口通常与[replacePhotoPickerPreview](#ZH-CN_TOPIC_0000002522242092__replacephotopickerpreview15)接口结合使用，以保存替换显示成功后的应用沙箱图片或视频newUris到图库。

模型约束：此接口仅可在Stage模型下使用。

元服务API：从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| trustedUris | Array<string> | 是 | 需要保存到图库的应用沙箱图片或视频URI。 trustedUris一般来自replacePhotoPickerPreview替换显示成功后的应用沙箱图片或视频newUri。 |
| settings | Array<photoAccessHelper.CreationSetting> | 否 | 需要保存的文件对应的配置参数。 |
| saveMode | SaveMode | 否 | 图片或视频的保存模式。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回保存后新生成的媒体库文件对应的URI。 |

**setMovingPhotoState23+**

setMovingPhotoState(movingPhotoState: [photoAccessHelper.MovingPhotoBadgeStateType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22)): Promise<void>

应用通过该接口，设置大图浏览下当前动态照片的效果。使用Promise异步回调。

仅在大图浏览下设置生效，不支持设置NOT_MOVING_PHOTO。

模型约束： 此接口仅可在Stage模型下使用。

元服务API：从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movingPhotoState | [photoAccessHelper.MovingPhotoBadgeStateType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22) | 是 | 设置当前大图动态照片的状态。 |

错误码：

接口抛出错误码的详细介绍请参见[媒体库错误码](媒体库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 23800151 | Scene parameters validate failed, possible causes: 1. An invalid enumeration value was passed. Only MOVING_PHOTO_ENABLE and MOVING_PHOTO_DISABLE are supported for configuration |
| 23800202 | Invalid call context. Possible causes: 1. The API is called outside the photo browsing scenario. 2. The API is called when isMovingPhotoBadgeShown is already set to true. |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

#### BaseItemInfo

图片、视频相关信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 是 | 图片、视频的uri。 当ItemType为THUMBNAIL时支持，否则为空。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| mimeType | string | 否 | 是 | 图片、视频的mimeType。 当ItemType为THUMBNAIL时支持，否则为空。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| width | number | 否 | 是 | 图片、视频的宽（单位：像素）。 当ItemType为THUMBNAIL时支持，否则为空。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| height | number | 否 | 是 | 图片、视频的高（单位：像素）。 当ItemType为THUMBNAIL时支持，否则为空。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| size | number | 否 | 是 | 图片、视频的大小（单位：字节）。 当ItemType为THUMBNAIL时支持，否则为空。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| duration | number | 否 | 是 | 视频的时长（单位：毫秒），图片/动态图片时返回-1。 当ItemType为THUMBNAIL时支持，否则为空。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| photoSubType21+ | [photoAccessHelper.PhotoSubtype](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photosubtype12) | 否 | 是 | 图片类型，包括DEFAULT、MOVING_PHOTO和BRUST。 非特殊类型图片默认为DEFAULT（0）。 元服务API：从API version 21开始，该接口支持在元服务中使用。 |
| dynamicRangeType21+ | [photoAccessHelper.DynamicRangeType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__dynamicrangetype12) | 否 | 是 | 媒体文件动态范围模型，包括HDR和SDR。 对于movingPhoto专指封面图片的动态范围类型。 元服务API：从API version 21开始，该接口支持在元服务中使用。 |
| orientation21+ | number | 否 | 是 | 图片/视频方向信息。 1.“TOP-left”，图像未旋转。 2.“TOP-right”，镜像水平翻转。 3.“Bottom-right”，图像旋转180°。 4.“Bottom-left”，镜像垂直翻转。 5.“Left-top”，先镜像水平翻转，再顺时针旋转270°。 6.“Right-top”，顺时针旋转90°。 7.“Right-bottom”，先镜像水平翻转，再顺时针旋转90°。 8.“Left-bottom”，顺时针旋转270°。 携带镜像信息的图片无论旋转与否其宽高属性都与原图保持一致，无镜像信息的图片其宽高属性会更新为旋转后的结果。 元服务API：从API version 21开始，该接口支持在元服务中使用。 |
| movingPhotoBadgeState22+ | [photoAccessHelper.MovingPhotoBadgeStateType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22) | 否 | 是 | 动态照片的状态。 当ItemType为THUMBNAIL时支持，否则为空。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| videoMode22+ | [photoAccessHelper.VideoMode](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__videomode22) | 否 | 是 | 视频文件的log模式。  元服务API：从API version 22开始，该接口支持在元服务中使用。 |

#### ItemInfo

继承自[BaseItemInfo](#ZH-CN_TOPIC_0000002522242092__baseiteminfo)，增加私有参数itemType。

图片、视频相关信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemType | ItemType | 否 | 是 | 被点击的item类型。包括缩略图item和相机item。 |

#### PhotoBrowserInfo

大图相关信息。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| animatorParams | AnimatorParams | 否 | 是 | 进入、退出大图界面时的动效参数。 |

#### AnimatorParams

进退大图动效参数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 动效时长（单位：毫秒）。 |
| curve | Curve | ICurve | string | 否 | 是 | 动效曲线。 |

#### MaxSelected

最大选择数量。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Map<MaxCountType, number> | 否 | 是 | 最大选择数量（包含图片的最大选择数量、视频的最大选择数量以及总的最大选择数量）。 |

#### SingleLineConfig20+

单行显示模式配置项。单行模式下，组件不提供打开大图浏览相关功能。组件不支持大图相关回调，PickerController不支持大图相关的接口，接口调用将无效。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemDisplayRatio | ItemDisplayRatio | 否 | 是 | 宫格显示宽高比，支持1:1，原图宽高比两种模式，默认为宽高比1:1显示。 |
| itemBorderRadius | [Length](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | [BorderRadiuses](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__borderradiuses9) | [LocalizedBorderRadiuses](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__localizedborderradiuses12) | 否 | 是 | 宫格圆角属性。 |
| itemGap | [Length](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length) | 否 | 是 | 宫格间距。 |

#### BadgeConfig21+

特殊角标配置项。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| badgeType | BadgeType | 否 | 是 | 特殊角标的类型。 |
| uris | Array<string> | 否 | 是 | 显示角标的资产uri数据。 |

**ClickResult23+**

设置指定URI的资产是否被选中。

模型约束：此接口仅可在Stage模型下使用。

元服务API：从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 媒体文件资产的URI。 |
| isSelected | boolean | 否 | 否 | 设置指定的媒体文件资产是否被选中，true表示选中，false表示不选中。 |

#### PreselectedInfo21+

预选中的文件以及文件对应的PhotoPickerComponent序号。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 选中媒体文件的uri。 |
| preselectablePickerIndex | number | 否 | 是 | 限制仅在指定序号的PhotoPickerComponent中进行自动选中；默认为-1，即可支持在任意序号的PhotoPickerComponent中自动选中。 |

#### UpdatablePickerConfigs22+

支持更新的PhotoPickerComponent属性，为[PickerOptions](#ZH-CN_TOPIC_0000002522242092__pickeroptions)的子集。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mimeType | [photoAccessHelper.PhotoViewMIMETypes](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes) | 否 | 是 | 可选择的媒体文件类型。 若无此参数，则默认为图片和视频类型。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| mimeTypeFilter | photoAccessHelper.MimeTypeFilter | 否 | 是 | 文件类型的过滤配置，支持指定多个类型过滤。 - 当配置mimeTypeFilter参数时，mimeType的配置自动失效。 - 当配置该参数时，仅显示配置过滤类型对应的媒体文件，建议提示用户仅支持选择指定类型的图片/视频。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| maxSelectNumber | number | 否 | 是 | 选择媒体文件数量的最大值（单位：个）。 最大可设置为500，若不设置则默认为50。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| maxPhotoSelectNumber | number | 否 | 是 | 图片最大的选择数量（单位：个）。 最大值为500，受到最大选择总数的限制。默认为500。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| maxVideoSelectNumber | number | 否 | 是 | 视频最大的选择数量（单位：个）。 最大值为500，受到系统中所有媒体文件最大选择总数的限制。默认为500。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| selectMode | SelectMode | 否 | 是 | Picker选择模式。 包括多选和单选，默认为多选。  元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| singleSelectionMode | [photoAccessHelper.SingleSelectionMode](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529445919__singleselectionmode18) | 否 | 是 | 单选模式类型。默认为大图预览模式（SingleSelectionMode.BROWSER_MODE）。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| isRepeatSelectSupported | boolean | 否 | 是 | 是否支持单张图片重复选择。 true表示支持，false表示不支持。默认为false。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| preselectedUris | Array<string> | 否 | 是 | 已选择图片的uri数据。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| checkBoxColor | string | 否 | 是 | 勾选框的背景色。 格式为8位十六进制颜色代码。  元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| backgroundColor | string | 否 | 是 | Picker宫格页面背景色。 格式为8位十六进制颜色代码。  元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| checkboxTextColor | string | 否 | 是 | 勾选框内文本颜色。 格式为8位十六进制颜色代码。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| photoBrowserBackgroundColorMode | PickerColorMode | 否 | 是 | 大图背景颜色。 包括跟随系统、浅色模式以及深色模式，默认为跟随系统。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| uiComponentColorMode | PickerColorMode | 否 | 是 | Picker UI组件的颜色模式。 Picker宫格界面除背景色之外其他组件的深浅色风格，包括搜索框、相机入口、安全使用图库提示组件、推荐气泡等组件，一般与backgroundColor配合使用。默认为PickerColorMode.AUTO，跟随系统深浅色切换。 该属性设置为PickerColorMode.LIGHT时，一般不与深颜色的backgroundColor搭配；设置为PickerColorMode.DARK时，不与浅颜色的backgroundColor搭配，避免出现组件背景或文字无法看清楚的问题。 元服务API：从API version 22开始，该接口支持在元服务中使用。 |
| isSlidingSupported23+ | boolean | 否 | 是 | 是否屏蔽PhotoPickerComponent的滚动。true表示不屏蔽滚动事件，响应用户滚动。false表示屏蔽滚动事件，不响应用户滚动。 默认为true。 模型约束：此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| edgeEffect23+ | EdgeEffect | 否 | 是 | Picker宫格页滑动到边缘处的滑动效果。 默认为EdgeEffect.Spring。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| appAlbumFilters23+ | Array<string> | 否 | 是 | 仅显示与指定bundle name对应的相册内容。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| autoPlayScenes23+ | Array<AutoPlayScene> | 否 | 是 | 设置动态照片播放模式。长度限制为2个，超出取前2个，多余的会自动忽略。 模型约束： 此接口仅可在Stage模型下使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

**PickerError23+**

使用PhotoPickerComponent组件发生错误时返回的错误的接口名称、错误码和错误描述。

模型约束： 此接口仅可在Stage模型下使用。

元服务API：从API version 23开始，该接口支持在元服务中使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| functionName | string | 否 | 否 | 产生错误的接口名称。 |
| errorCode | number | 否 | 否 | 错误码。 |
| message | string | 否 | 否 | 接口返回的具体错误描述信息。 |

#### DataType

枚举，PickerController向picker组件发送数据的数据类型。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SET_SELECTED_URIS | 1 | 发送已选择的数据列表，通知picker组件勾选状态刷新，需要传入string数组类型。 例如：应用在自己的页面中删除某张图片后，需要把剩下的已选择的数据列表通过setData接口通知到picker组件，从而触发picker组件勾选框状态刷新正确。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| SET_ALBUM_URI | 2 | 发送已选择相册，通知picker组件刷新相册，需要传入string类型。 例如：应用在自己的页面中选择相册后，需要把已选择的相册uri通过setData接口通知到picker组件，从而触发picker组件刷新相册数据。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| SET_SELECTED_INFO21+ | 3 | 发送已选择的文件uri以及选中的picker序号。当picker序号与参数中的picker序号匹配时，已选择文件支持在当前picker里自动选中。 元服务API：从API version 21开始，该接口支持在元服务中使用。 |
| SET_BADGE_CONFIGS21+ | 4 | 发送需要显示角标的配置，类型为badgeConfig，包含角标的类型和对应文件uri的数据列表。配置后，对应文件会显示配置类型的角标。 元服务API：从API version 21开始，该接口支持在元服务中使用。 |
| SET_ITEM_CLICK_RESULT23+ | 5 | 发送点击后的结果，类型为ClickResult。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |

#### ItemType

被点击item的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| THUMBNAIL | 0 | 图片、视频item（缩略图item）。 |
| CAMERA | 1 | 相机item。 |

#### ClickType

点击操作的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECTED | 0 | 选择操作（勾选图片或者点击相机item）。 |
| DESELECTED | 1 | 取消选择操作（取消勾选图片）。 |

#### PickerOrientation

Picker宫格页面滑动预览的方向。

从API20开始，该能力支持配置；在API12-19，该能力设置不生效，默认为竖直方向。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VERTICAL | 0 | 竖直方向。 |
| HORIZONTAL | 1 | 水平方向。 |

#### SelectMode

选择模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLE_SELECT | 0 | 单选模式。 |
| MULTI_SELECT | 1 | 多选模式。 |

#### PickerColorMode

Picker的颜色模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 跟随系统。 |
| LIGHT | 1 | 浅色模式。 |
| DARK | 2 | 深色模式。 |

#### ReminderMode

最大选择数量提示方式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不提示。 |
| TOAST | 1 | 弹toast提示。 |
| MASK | 2 | 蒙灰提示。 |

#### MaxCountType

最大选择数量的类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOTAL_MAX_COUNT | 0 | 总的最大选择数量。 |
| PHOTO_MAX_COUNT | 1 | 图片的最大选择数量（不能大于总的最大选择数量）。 |
| VIDEO_MAX_COUNT | 2 | 视频的最大选择数量（不能大于总的最大选择数量）。 |

#### PhotoBrowserRange

打开大图浏览模式后，左右滑动切换浏览图片的范围。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 全部图片，视频。 |
| SELECTED_ONLY | 1 | 仅用户已选择的图片，视频。 |

#### PhotoBrowserUIElement13+

大图页大图预览组件外其他UI元素。

**元服务API**：从API version 13开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHECKBOX | 0 | 大图页勾选框。 |
| BACK_BUTTON | 1 | 大图页返回按钮。 |

#### SaveMode15+

图片/视频保存模式。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAVE_AS | 0 | 另存为新的图片/视频。 |
| OVERWRITE | 1 | 覆盖原有图片/视频，覆盖后支持在图库中将保存内容回退，还原成原始图片/视频。 |

#### BadgeType21+

表示特殊角标类型的枚举。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BADGE_UPLOADED | 0 | 已上传。 |

#### VideoPlayerState14+

视频播放状态。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAYING | 0 | 视频播放中。 |
| PAUSED | 1 | 视频播放暂停。 |
| STOPPED | 2 | 视频播放停止。 |
| SEEK_START | 3 | 开始拖拽进度条。 |
| SEEK_FINISH | 4 | 结束拖拽进度条。 |

#### ItemDisplayRatio20+

单行布局宫格显示宽高比模式，包括1:1和原图宽高比两种模式。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SQUARE_RATIO | 0 | 1:1比例显示。 |
| ORIGINAL_SIZE_RATIO | 1 | 原图宽高比显示。 |

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
  VideoPlayerState,
  photoAccessHelper
} from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';
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

  private onDeselect(uri: string): void {
    // 移除。
    if (uri) {
      this.selectUris = this.selectUris.filter((item: string) => {
        return item != uri;
      })
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
      return true;
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
```