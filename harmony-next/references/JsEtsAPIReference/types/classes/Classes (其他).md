# Classes (其他)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### RecommendationOptions11+

图片推荐选项(基于图片数据分析结果，依赖设备适配)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| recommendationType | [RecommendationType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__recommendationtype11) | 否 | 是 | 如果需要根据枚举值推荐相应的图片，则配置此参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| textContextInfo12+ | TextContextInfo | 否 | 是 | 如果需要根据文本信息推荐相应的图片，则配置此参数（如果同时配置了recommendationType，则仅textContextInfo生效）。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### BaseSelectOptions

图库选择选项基类。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| MIMEType | [PhotoViewMIMETypes](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes) | 否 | 是 | 可选择的媒体文件类型，若无此参数，则默认为图片和视频类型。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| maxSelectNumber | number | 否 | 是 | 选择媒体文件数量的最大值（最大可设置的值为500，若不设置则默认为50）。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isPhotoTakingSupported11+ | boolean | 否 | 是 | 是否支持拍照，true表示支持，false表示不支持，默认为true。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isSearchSupported11+ | boolean | 否 | 是 | 是否支持搜索，true表示支持，false表示不支持，默认为true。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| recommendationOptions11+ | RecommendationOptions | 否 | 是 | 图片推荐相关配置参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| preselectedUris11+ | Array<string> | 否 | 是 | 预选择图片的uri数据。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isPreviewForSingleSelectionSupported12+ | boolean | 否 | 是 | 单选模式下是否需要进大图预览，true表示需要，false表示不需要，默认为true。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| singleSelectionMode18+ | [SingleSelectionMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__singleselectionmode18) | 否 | 是 | 单选模式类型。默认为大图预览模式（SingleSelectionMode.BROWSER_MODE）。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| mimeTypeFilter19+ | MimeTypeFilter | 否 | 是 | 文件类型的过滤配置，支持指定多个类型过滤。 当配置mimeTypeFilter参数时，MIMEType的配置自动失效。 配置该参数时，仅显示配置过滤类型对应的媒体文件，建议提示用户仅支持选择指定类型的图片/视频。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| fileSizeFilter19+ | FileSizeFilter | 否 | 是 | 可选择媒体文件大小的过滤配置。 配置该参数时，仅显示配置文件大小范围的媒体文件，建议提示用户仅支持选择指定大小的图片/视频。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| videoDurationFilter19+ | VideoDurationFilter | 否 | 是 | 可选择媒体文件视频时长的过滤配置。 配置该参数时，仅显示配置视频时长范围的媒体文件，建议提示用户仅支持选择指定时长视频。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| combinedMediaTypeFilter20+ | Array<string> | 否 | 是 | 将过滤条件配置为字符串数组，支持多种类型组合。 字符串格式如下：photoType | photoSubType1,photoSubType2, … | mimeType1,mimeType2, …。 - 第1段指定1个photoType，固定为image（图片）或video（视频）。 - 第2段指定1~ N个photoSubType，多个photoSubType之间使用逗号隔开，之间为“或（OR）”的逻辑取并集；N目前支持最大为1；可选的PhotoSubType包括movingPhoto或“*”（忽略）。 - 第3段指定1 N个mimeType，多个mimeType之间使用逗号隔开，之间为“或（OR）”的逻辑取并集；N最大为10，格式类似于MimeTypeFilter。  三段过滤的组合取交集处理。 支持“非”的逻辑。对于需要排除的类型，进行加括号的方式进行标识；一个string最多可使用1个括号。 当应用配置的过滤条件string不满足上述规格时，过滤结果为空。 配置该参数时，仅取数组前三个参数进行处理，MIMEType、mimeTypeFilter参数自动失效。 元服务API： 从API version 20开始支持在元服务中使用。 |
| photoViewMimeTypeFileSizeFilters20+ | Array<PhotoViewMimeTypeFileSizeFilter> | 否 | 是 | 指定媒体文件类型和文件大小进行过滤。 配置该参数时，仅取数组前三个参数进行处理，MIMETypes和fileSizeFilter自动失效。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| isMovingPhotoBadgeShown22+ | boolean | 否 | 是 | 是否在大图浏览模式下展示动态照片图标，true表示展示，false表示不展示，默认为false。 若设置为true，Photoselectresult返回movingPhotoBadgeStates数组，动态照片默认返回状态为MOVING_PHOTO_ENABLED。 注意： 必须同时使用isMovingPhotoBadgeShown和[MovingPhotoBadgeStateType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22)判断照片是否是动态照片。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| assetFilter22+ | Array<OperationItem> | 否 | 是 | 媒体资产过滤器，长度限制为50个，超出取前50个。 注意： 1. 当使用该过滤器时，其他过滤器会失效。 2. 当配置多个条件时，过滤条件前后需要配置英文括号，否则可能和内部过滤项冲突。 模型约束： 此接口仅可在Stage模型下使用。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| autoPlayScenes23+ | Array<AutoPlayScene> | 否 | 是 | 设置动态照片播放模式。长度限制为2个，超出取前2个，多余的会自动忽略。 模型约束： 此接口仅可在Stage模型下使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| globalMovingPhotoState23+ | [MovingPhotoBadgeStateType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22) | 否 | 是 | 设置全局动态照片的效果，当前仅支持MOVING_PHOTO_ENABLED和MOVING_PHOTO_DISABLED。默认为MOVING_PHOTO_ENABLED。 模型约束： 此接口仅可在Stage模型下使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| gridPinchMode23+ | GridPinchMode | 否 | 是 | picker内宫格捏合模式。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

#### PhotoSelectOptions

PhotoSelectOptions extends BaseSelectOptions

图库选择选项子类，继承自[BaseSelectOptions](#ZH-CN_TOPIC_0000002522242084__baseselectoptions)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isEditSupported11+ | boolean | 否 | 是 | 是否支持编辑照片，true表示支持，false表示不支持，默认为true。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isOriginalSupported12+ | boolean | 否 | 是 | 是否显示选择原图按钮，true表示显示，false表示不显示，默认为false。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| subWindowName12+ | string | 否 | 是 | 子窗口名称。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| completeButtonText14+ | [CompleteButtonText](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__completebuttontext14) | 否 | 是 | 完成按钮显示的内容。 完成按钮指在界面右下方，用户点击表示图片选择已完成的按钮。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| contextRecoveryInfo21+ | ContextRecoveryInfo | 否 | 是 | 用于恢复上次退出时PhotoPicker现场的信息。 上次完成选择时photoPicker将返回contextRecoveryInfo给应用，应用可使用返回的contextRecoveryInfo，在下次启动时恢复上次使用picker，最后浏览的宫格界面。 元服务API： 从API version 21开始，该接口支持在元服务中使用。 |
| isDestroyedWithNavigation23+ | boolean | 否 | 是 | 是否支持跟随Navigation销毁，true表示支持，false表示不支持，默认为false。 模型约束： 此接口仅可在Stage模型下使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| maxPhotoSelectNumber23+ | number | 否 | 是 | 支持设置的图片最大的选择数量。单位：个。 受到最大选择总数的限制，最大值为500。默认为500。 模型约束： 此接口仅可在Stage模型下使用。 元服务API：从API version 23开始，该接口支持在元服务中使用。 |
| maxVideoSelectNumber23+ | number | 否 | 是 | 支持设置的视频最大的选择数量。单位：个。 受到系统中所有媒体文件最大选择总数的限制，最大值为500。默认为500。 模型约束： 此接口仅可在Stage模型下使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| isReturnToPhotoBrowserEnabled23+ | boolean | 否 | 是 | 在单选模式下，拍完照是否能自动跳转到大图预览模式，true表示支持，false表示不支持，默认为false。 注意： 该参数配置为true时仅在[SingleSelectionMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__singleselectionmode18)为BROWSER_MODE（大图预览模式）或者BROWSER_AND_SELECT_MODE（兼容模式）并且BaseSelectOptions.isPreviewForSingleSelectionSupported参数为true时生效。 模型约束： 此接口仅可在Stage模型下使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

#### PhotoSelectResult

返回图库选择后的结果集。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| photoUris | Array<string> | 否 | 否 | 返回图库选择后的媒体文件的URI数组。 此URI数组只能通过临时授权的方式调用photoAccessHelper.getAssets接口去使用，具体使用方式请参考媒体文件URI的使用方式。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isOriginalPhoto | boolean | 否 | 否 | 返回图库选择后的媒体文件是否为原图。true表示是原图，false表示不是原图，默认值是false。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| contextRecoveryInfo21+ | ContextRecoveryInfo | 否 | 否 | 当用户完成选择时返回的photoSelectResult将包含退出picker的上下文信息contextRecoveryInfo，支持应用下次启动PhotoPicker时设置给PhotoSelectOptions用于上次退出时现场的恢复。 元服务API： 从API version 21开始，该接口支持在元服务中使用。 |
| movingPhotoBadgeStates22+ | Array<[MovingPhotoBadgeStateType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22)> | 否 | 否 | 返回图库选择的媒体文件动态照片状态数组。 当isMovingPhotoBadgeShown为true时，movingPhotoBadgeStates携带动态照片状态，反之为空。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

**AutoPlayScene23+**

动态照片在不同场景中的播放模式。

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sceneType | SceneType | 否 | 否 | 动态照片播放的场景。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| playMode | PlayMode | 否 | 否 | 是否支持动态照片自动播放。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

#### MimeTypeFilter19+

文件类型的过滤配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mimeTypeArray | Array<string> | 否 | 否 | PhotoPicker可供用户选择媒体文件的过滤类型。数组长度最大为10，因此支持最多十种指定类型。 过滤类型参考MIME类型定义，例如：“image/jpeg”、“video/mp4”等。 |

#### FileSizeFilter19+

可选择媒体文件大小的过滤配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| filterOperator | [FilterOperator](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__filteroperator19) | 否 | 否 | 过滤操作符。 例如：按照大于/小于某个fileSize的方式过滤文件。 |
| fileSize | number | 否 | 否 | 指定进行过滤的文件大小。 单位为字节（Byte）。 |
| extraFileSize | number | 否 | 是 | 针对[FilterOperator](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__filteroperator19).BETWEEN情况下，配置文件大小的上限值。默认值为-1。 单位为字节（Byte）。 |

#### VideoDurationFilter19+

可选择媒体文件视频时长的过滤配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| filterOperator | [FilterOperator](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__filteroperator19) | 否 | 否 | 过滤操作符。 例如：按照大于/小于某个videoDuration的方式过滤可选择的视频。 |
| videoDuration | number | 否 | 否 | 指定过滤视频的时长。 单位为毫秒（ms）。 |
| extraVideoDuration | number | 否 | 是 | 针对[FilterOperator](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__filteroperator19).BETWEEN情况下，配置视频时长的上限值。默认值为-1。 单位为毫秒（ms）。 |

#### RecentPhotoOptions20+

最近图片配置选项。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| period | number | 否 | 是 | 配置最近图片显示的时间范围，单位为秒（s）。配置后，系统将显示距离当前时间点指定时长内的图片。最长可配置时长为1天（86400s）。 当值小于等于0、大于86400或者未配置时，默认按最长时间段（1天）显示最近图片。当配置时间段内无符合的图片或视频时，组件不显示。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |
| MIMEType | photoAccessHelper.[PhotoViewMIMETypes](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes) | 否 | 是 | 最近图片控件显示的文件类型，默认为PhotoViewMIMETypes.IMAGE_VIDEO_TYPE。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |
| photoSource | [PhotoSource](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photosource20) | 否 | 是 | 配置最近图片视频显示内容的来源，比如拍照、截屏等。默认不限制来源。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |

#### RecentPhotoInfo20+

最近图片相关信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dateTaken | number | 否 | 是 | 最近图片/视频的拍摄时间（距1970年1月1日的毫秒数值），单位为毫秒（ms）。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |
| identifier | string | 否 | 是 | 最近图片/视频的名称hash值，用于辅助应用区分最新图片组件将要显示的图片/视频与之前曾显示过的图片/视频是否为同一个。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |

#### PhotoViewMimeTypeFileSizeFilter20+

指定媒体文件类型和文件大小进行过滤。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| photoViewMimeType | [PhotoViewMIMETypes](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes) | 否 | 否 | 指定媒体文件类型，用于文件大小过滤。 |
| sizeFilter | FileSizeFilter | 否 | 否 | 指定文件大小过滤规则。 |

#### ContextRecoveryInfo21+

PhotoPicker退出界面的上下文信息，可以用于下次使用PhotoPicker时恢复上次退出时的现场。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| albumUri | string | 否 | 否 | 用户选择图片后，退出时的相册信息。 albumUri对应媒体库中相册的uri。 - 当上次在所有图片中选择时，albumUri为固定的"allPhotos"字符串。 - 当用户在搜索结果/文本推荐/头像推荐中完成选择退出时，不支持下次恢复现场，此时Picker返回的albumUri为空字符串。 默认值为空字符串。 |
| time | number | 否 | 否 | 用户上次选择图片的宫格界面，左上角首张图片的时间。 - 按拍摄时间排序的相册，返回拍摄时间。 - 按保存时间排序的相册返回保存时间。默认为0。 |
| displayName | string | 否 | 否 | 用户上次选择图片的宫格界面，左上角首张图片的文件名。默认为空字符串。 |
| recommendationType | number | 否 | 否 | 用户上次选择时设置的推荐内容枚举值，参考[RecommendationType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__recommendationtype11)值定义。 上次选择时未设置推荐时，默认为0。 |
| selected[RecommendationType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__recommendationtype11) | number | 否 | 否 | 用户上次选择时选中的推荐内容枚举值，参考RecommendationType值定义。 当上次选择未选中推荐项，选中"全部"时，默认为0。 |
| version | number | 否 | 否 | 现场数据版本号，用于校验现场信息数据与现场恢复能力的匹配度。 版本号必须大于等于1.0。 |
| gridLevel | GridLevel | 否 | 否 | 用户上次退出宫格时的档位。 |

#### OperationItem22+

选择媒体文件的过滤配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| operationType | [OperationType](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__operationtype22) | 否 | 否 | 各类谓词的枚举。 |
| field | [PhotoKeys](../enums/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys) | 否 | 是 | 数据表中的列名。 当前仅支持如下关键字段：URI、PHOTO_TYPE、DISPLAY_NAME、SIZE、DURATION、WIDTH、HEIGHT、ORIENTATION、FAVORITE、TITLE、POSITION、PHOTO_SUBTYPE、DYNAMIC_RANGE_TYPE、COVER_POSITION、BURST_KEY、LCD_SIZE、THM_SIZE、DETAIL_TIME、MEDIA_SUFFIX、OWNER_ALBUM_ID、ASPECT_RATIO 通过select接口配置此参数时，输入非法字段会抛出错误码401；通过PhotoPickerComponent (PhotoPicker组件)配置此参数时，输入非法字段无onPickerControllerReady回调。 非条件谓词如and、or、beginWrap、endWrap等不涉及该字段。 |
| value | Array<[OperationValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605956__operationvaluetype22)> | 否 | 是 | 不同谓词所需匹配的值。 非条件谓词如and、or、beginWrap、endWrap等不涉及该字段。 限制最大长度为10，超出则取前10个值。 |

**RequestReadPermissionResult23+**

包含已授权的uri列表和无效的uri列表。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.FileManagement.PhotoAccessHelper.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authorizedUris | Array<string> | 否 | 否 | 返回已创建并授予保存权限的uri列表。 |
| invalidUris | Array<string> | 否 | 否 | 返回可能被删除、隐藏或重命名的无效uri列表。 |