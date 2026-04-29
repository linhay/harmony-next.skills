# Class (FileSelectorParam)

Web组件获取文件对象。示例代码参考[onShowFileSelector事件](事件.md#ZH-CN_TOPIC_0000002522081170__onshowfileselector9)。


-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准。

#### constructor9+

constructor()

FileSelectorParam的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getTitle9+

getTitle(): string

获取文件选择器标题。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回文件选择器标题。 |

#### getMode9+

getMode(): [FileSelectorMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__fileselectormode9)

获取文件选择器的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FileSelectorMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__fileselectormode9) | 返回文件选择器的模式。 |

#### getAcceptType9+

getAcceptType(): Array<string>

获取文件过滤类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回文件过滤类型。 |

#### isCapture9+

isCapture(): boolean

获取是否调用多媒体能力。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否调用多媒体能力。 true表示返回调用多媒体能力，false表示返回未调用多媒体能力。 |

#### getMimeTypes18+

getMimeTypes(): Array<string>

获取文件MIME类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回文件MIME类型。 |

**getSuggestedName23+**

getSuggestedName(): string

获取建议选择的文件名。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的suggestedName。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 返回建议文件名。 |

**getDefaultPath23+**

getDefaultPath(): string

获取文件选择器默认起始路径。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的startIn。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 返回默认路径。 当前端startIn设置为公共目录downloads、pictures时，要注意应分别转化为鸿蒙系统下的download和images。 |

**getDescriptions23+**

getDescriptions(): Array<string>

获取各组文件类型的描述。为允许的文件类型类别的可选描述。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的description。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回文件类型的描述数组。 |

**isAcceptAllOptionExcluded23+**

isAcceptAllOptionExcluded(): boolean

获取文件选择器是否支持选项（*/*），即所有文件。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的excludeAcceptAllOption。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否包含一个不应用任何文件类型过滤器的选项。 true表示不包含，false表示包含。 |

**getAcceptableFileTypes23+**

getAcceptableFileTypes(): Array<Array<AcceptableFileType>>

获取文件types信息。对应HTML里[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-file-upload#自定义处理js接口拉起的文件请求)中的types。

系统能力： SystemCapability.Web.Webview.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<Array<AcceptableFileType>> | 返回文件types信息。 |