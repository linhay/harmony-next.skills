# Classes (其他)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### RecommendationOptions11+

图片推荐选项(基于图片数据分析结果，依赖设备适配)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明recommendationType[RecommendationType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__recommendationtype11)否是

如果需要根据枚举值推荐相应的图片，则配置此参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

textContextInfo12+[TextContextInfo](../interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002529285945__textcontextinfo12)否是

如果需要根据文本信息推荐相应的图片，则配置此参数（如果同时配置了recommendationType，则仅textContextInfo生效）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### BaseSelectOptions

图库选择选项基类。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明MIMEType[PhotoViewMIMETypes](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes)否是

可选择的媒体文件类型，若无此参数，则默认为图片和视频类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

maxSelectNumbernumber否是

选择媒体文件数量的最大值（最大可设置的值为500，若不设置则默认为50）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

isPhotoTakingSupported11+boolean否是

是否支持拍照，true表示支持，false表示不支持，默认为true。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

isSearchSupported11+boolean否是

是否支持搜索，true表示支持，false表示不支持，默认为true。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

recommendationOptions11+[RecommendationOptions](#ZH-CN_TOPIC_0000002497605950__recommendationoptions11)否是

图片推荐相关配置参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

preselectedUris11+Array<string>否是

预选择图片的uri数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

isPreviewForSingleSelectionSupported12+boolean否是

单选模式下是否需要进大图预览，true表示需要，false表示不需要，默认为true。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

singleSelectionMode18+[SingleSelectionMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__singleselectionmode18)否是

单选模式类型。默认为大图预览模式（SingleSelectionMode.BROWSER_MODE）。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

mimeTypeFilter19+[MimeTypeFilter](#ZH-CN_TOPIC_0000002497605950__mimetypefilter19)否是

文件类型的过滤配置，支持指定多个类型过滤。

当配置mimeTypeFilter参数时，MIMEType的配置自动失效。

配置该参数时，仅显示配置过滤类型对应的媒体文件，建议提示用户仅支持选择指定类型的图片/视频。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

fileSizeFilter19+[FileSizeFilter](#ZH-CN_TOPIC_0000002497605950__filesizefilter19)否是

可选择媒体文件大小的过滤配置。

配置该参数时，仅显示配置文件大小范围的媒体文件，建议提示用户仅支持选择指定大小的图片/视频。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

videoDurationFilter19+[VideoDurationFilter](#ZH-CN_TOPIC_0000002497605950__videodurationfilter19)否是

可选择媒体文件视频时长的过滤配置。

配置该参数时，仅显示配置视频时长范围的媒体文件，建议提示用户仅支持选择指定时长视频。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

combinedMediaTypeFilter20+Array<string>否是

将过滤条件配置为字符串数组，支持多种类型组合。

字符串格式如下：photoType | photoSubType1,photoSubType2, … | mimeType1,mimeType2, …。

- 第1段指定1个photoType，固定为image（图片）或video（视频）。

- 第2段指定1~

N个photoSubType，多个photoSubType之间使用逗号隔开，之间为“或（OR）”的逻辑取并集；N目前支持最大为1；可选的PhotoSubType包括movingPhoto或“*”（忽略）。

- 第3段指定1

 N个mimeType，多个mimeType之间使用逗号隔开，之间为“或（OR）”的逻辑取并集；N最大为10，格式类似于[MimeTypeFilter](#ZH-CN_TOPIC_0000002497605950__mimetypefilter19)。

三段过滤的组合取交集处理。

支持“非”的逻辑。对于需要排除的类型，进行加括号的方式进行标识；一个string最多可使用1个括号。

当应用配置的过滤条件string不满足上述规格时，过滤结果为空。

配置该参数时，仅取数组前三个参数进行处理，MIMEType、mimeTypeFilter参数自动失效。

**元服务API：** 从API version 20开始支持在元服务中使用。

photoViewMimeTypeFileSizeFilters20+Array<[PhotoViewMimeTypeFileSizeFilter](#ZH-CN_TOPIC_0000002497605950__photoviewmimetypefilesizefilter20)>否是

指定媒体文件类型和文件大小进行过滤。

配置该参数时，仅取数组前三个参数进行处理，MIMETypes和fileSizeFilter自动失效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

isMovingPhotoBadgeShown22+boolean否是

是否在大图浏览模式下展示动态照片图标，true表示展示，false表示不展示，默认为false。

若设置为true，[Photoselectresult](#ZH-CN_TOPIC_0000002497605950__photoselectresult)返回movingPhotoBadgeStates数组，动态照片默认返回状态为MOVING_PHOTO_ENABLED。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

assetFilter22+Array<[OperationItem](#ZH-CN_TOPIC_0000002497605950__operationitem22)>否是

媒体资产过滤器，长度限制为50个，超出取前50个。

**注意：**

1. 当使用该过滤器时，其他过滤器会失效。

2. 当配置多个条件时，过滤条件前后需要配置英文括号，否则可能和内部过滤项冲突。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

#### PhotoSelectOptions

PhotoSelectOptions extends BaseSelectOptions

图库选择选项子类，继承自[BaseSelectOptions](#ZH-CN_TOPIC_0000002497605950__baseselectoptions)。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明isEditSupported11+boolean否是

是否支持编辑照片，true表示支持，false表示不支持，默认为true。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

isOriginalSupported12+boolean否是

是否显示选择原图按钮，true表示显示，false表示不显示，默认为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

subWindowName12+string否是

子窗口名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

completeButtonText14+[CompleteButtonText](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__completebuttontext14)否是

完成按钮显示的内容。

完成按钮指在界面右下方，用户点击表示图片选择已完成的按钮。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

contextRecoveryInfo21+[ContextRecoveryInfo](#ZH-CN_TOPIC_0000002497605950__contextrecoveryinfo21)否是

用于恢复上次退出时PhotoPicker现场的信息。

上次完成选择时photoPicker将返回contextRecoveryInfo给应用，应用可使用返回的contextRecoveryInfo，在下次启动时恢复上次使用picker，最后浏览的宫格界面。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

#### PhotoSelectResult

返回图库选择后的结果集。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明photoUrisArray<string>否否

返回图库选择后的媒体文件的uri数组，此uri数组只能通过临时授权的方式调用[photoAccessHelper.getAssets接口](../interfaces/Interface (PhotoAccessHelper).md#ZH-CN_TOPIC_0000002529445917__getassets)去使用，具体使用方式参见用户文件uri介绍中的[媒体文件uri的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

isOriginalPhotoboolean否否

返回图库选择后的媒体文件是否为原图。true表示是原图，false表示不是原图，默认值是false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

contextRecoveryInfo21+[ContextRecoveryInfo](#ZH-CN_TOPIC_0000002497605950__contextrecoveryinfo21)否否

当用户完成选择时返回的photoSelectResult将包含退出picker的上下文信息contextRecoveryInfo，支持应用下次启动PhotoPicker时设置给PhotoSelectOptions用于上次退出时现场的恢复。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

movingPhotoBadgeStates22+Array<[MovingPhotoBadgeStateType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__movingphotobadgestatetype22)>否否

返回图库选择的媒体文件动态照片状态数组。

当isMovingPhotoBadgeShown为true时，movingPhotoBadgeStates携带动态照片状态，反之为空。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

#### MimeTypeFilter19+

文件类型的过滤配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明mimeTypeArrayArray<string>否否

PhotoPicker可供用户选择媒体文件的过滤类型。最多支持指定十种媒体文件类型。

过滤类型参考MIME类型定义，例如：“image/jpeg”、“video/mp4”等。

#### FileSizeFilter19+

可选择媒体文件大小的过滤配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明filterOperator[FilterOperator](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__filteroperator19)否否

过滤操作符。

例如：按照大于/小于某个fileSize的方式过滤文件。

fileSizenumber否否

指定进行过滤的文件大小。

单位为字节（Byte）。

extraFileSizenumber否是

针对FilterOperator.BETWEEN情况下，配置文件大小的上限值。默认值为-1。

单位为字节（Byte）。

#### VideoDurationFilter19+

可选择媒体文件视频时长的过滤配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明filterOperator[FilterOperator](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__filteroperator19)否否

过滤操作符。

例如：按照大于/小于某个videoDuration的方式过滤可选择的视频。

videoDurationnumber否否

指定过滤视频的时长。

单位为毫秒（ms）。

extraVideoDurationnumber否是

针对FilterOperator.BETWEEN情况下，配置视频时长的上限值。默认值为-1。

单位为毫秒（ms）。

#### RecentPhotoOptions20+

最近图片配置选项。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明periodnumber否是

配置最近图片显示的时间范围，单位为秒（s）。配置后，系统将显示距离当前时间点指定时长内的图片。最长可配置时长为1天（86400s）。

当值小于等于0、大于86400或者未配置时，默认按最长时间段（1天）显示最近图片。当配置时间段内无符合的图片或视频时，组件不显示。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

MIMEType[photoAccessHelper.PhotoViewMIMETypes](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes)否是

最近图片控件显示的文件类型，默认为PhotoViewMIMETypes.IMAGE_VIDEO_TYPE。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

photoSource[PhotoSource](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photosource20)否是

配置最近图片视频显示内容的来源，比如拍照、截屏等。默认不限制来源。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

#### RecentPhotoInfo20+

最近图片相关信息。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明dateTakennumber否是

最近图片/视频的拍摄时间（距1970年1月1日的毫秒数值），单位为毫秒（ms）。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

identifierstring否是

最近图片/视频的名称hash值，用于辅助应用区分最新图片组件将要显示的图片/视频与之前曾显示过的图片/视频是否为同一个。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

#### PhotoViewMimeTypeFileSizeFilter20+

指定媒体文件类型和文件大小进行过滤。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明photoViewMimeType[PhotoViewMIMETypes](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photoviewmimetypes)否否指定媒体文件类型，用于文件大小过滤。sizeFilter[FileSizeFilter](#ZH-CN_TOPIC_0000002497605950__filesizefilter19)否否指定文件大小过滤规则。

#### ContextRecoveryInfo21+

PhotoPicker退出界面的上下文信息，可以用于下次使用PhotoPicker时恢复上次退出时的现场。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明albumUristring否否

用户选择图片后，退出时的相册信息。

albumUri对应媒体库中相册的uri。

- 当上次在所有图片中选择时，albumUri为固定的"allPhotos"字符串。

- 当用户在搜索结果/文本推荐/头像推荐中完成选择退出时，不支持下次恢复现场，此时Picker返回的albumUri为空字符串。

默认值为空字符串。

timenumber否否

用户上次选择图片的宫格界面，左上角首张图片的时间。

- 按拍摄时间排序的相册，返回拍摄时间。

- 按保存时间排序的相册返回保存时间。默认为0。

displayNamestring否否用户上次选择图片的宫格界面，左上角首张图片的文件名。默认为空字符串。recommendationTypenumber否否

用户上次选择时设置的推荐内容枚举值，参考[RecommendationType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__recommendationtype11)值定义。

上次选择时未设置推荐时，默认为0。

selectedRecommendationTypenumber否否

用户上次选择时选中的推荐内容枚举值，参考[RecommendationType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__recommendationtype11)值定义。

当上次选择未选中推荐项，选中"全部"时，默认为0。

versionnumber否否

现场数据版本号，用于校验现场信息数据与现场恢复能力的匹配度。

版本号必须大于等于1.0。

#### OperationItem22+

选择媒体文件的过滤配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

名称类型只读可选说明operationType[OperationType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__operationtype22)否否各类谓词的枚举。field[PhotoKeys](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445919__photokeys)否是

数据表中的列名。

当前仅支持如下关键字段：URI、PHOTO_TYPE、DISPLAY_NAME、SIZE、DURATION、WIDTH、HEIGHT、ORIENTATION、FAVORITE、TITLE、POSITION、PHOTO_SUBTYPE、DYNAMIC_RANGE_TYPE、COVER_POSITION、BURST_KEY、LCD_SIZE、THM_SIZE、DETAIL_TIME、MEDIA_SUFFIX、OWNER_ALBUM_ID、ASPECT_RATIO

通过[select](Class (PhotoViewPicker).md#ZH-CN_TOPIC_0000002529445913__select)接口配置此参数时，输入非法字段会抛出错误码401；通过[PhotoPickerComponent (PhotoPicker组件)](../../modules/ohos/@ohos.file.PhotoPickerComponent (PhotoPicker组件).md)配置此参数时，输入非法字段无onPickerControllerReady回调。

非条件谓词如and、or、beginWrap、endWrap等不涉及该字段。

valueArray<[OperationValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605956__operationvaluetype22)>否是

不同谓词所需匹配的值。

非条件谓词如and、or、beginWrap、endWrap等不涉及该字段。

限制最大长度为10，超出则取前10个值。