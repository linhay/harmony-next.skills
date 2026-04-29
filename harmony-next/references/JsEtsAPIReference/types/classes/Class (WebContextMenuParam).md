# Class (WebContextMenuParam)

实现长按页面元素或鼠标右键弹出来的菜单信息。示例代码参考[onContextMenuShow事件](事件.md#ZH-CN_TOPIC_0000002522081170__oncontextmenushow9)。


-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准。

#### constructor9+

constructor()

WebContextMenuParam的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### x9+

x(): number

弹出菜单的x坐标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。 单位：vp。 |

#### y9+

y(): number

弹出菜单的y坐标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。 单位：vp。 |

#### getLinkUrl9+

getLinkUrl(): string

获取经过安全检查的url链接地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回经过安全检查的url链接。 |

#### getUnfilteredLinkUrl9+

getUnfilteredLinkUrl(): string

获取原始url链接地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回原始的url链接。 |

#### getSourceUrl9+

getSourceUrl(): string

获取sourceUrl链接。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 如果选中的元素有src属性，返回src的url。返回url的最大上限为2M，超出上限时返回空字符串。 |

#### existsImageContents9+

existsImageContents(): boolean

是否存在图像内容。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 长按位置中有图片返回true，否则返回false。 |

#### getMediaType9+

getMediaType(): [ContextMenuMediaType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenumediatype9)

获取网页元素媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuMediaType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenumediatype9) | 网页元素媒体类型。 |

#### getSelectionText9+

getSelectionText(): string

获取选中文本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 菜单上下文选中文本内容，不存在则返回空。 |

#### getSourceType9+

getSourceType(): [ContextMenuSourceType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenusourcetype9)

获取菜单事件来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuSourceType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenusourcetype9) | 菜单事件来源。 |

#### getInputFieldType9+

getInputFieldType(): [ContextMenuInputFieldType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenuinputfieldtype9)

获取网页元素输入框类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuInputFieldType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenuinputfieldtype9) | 输入框类型。 |

#### isEditable9+

isEditable(): boolean

获取网页元素是否可编辑标识。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 网页元素可编辑返回true，不可编辑返回false。 |

#### getEditStateFlags9+

getEditStateFlags(): number

获取网页元素可编辑标识。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 网页元素可编辑标识，参照[ContextMenuEditStateFlags](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenueditstateflags9)。 |

#### getPreviewWidth13+

getPreviewWidth(): number

获取预览图的宽。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 预览图的宽。 单位：vp。 |

#### getPreviewHeight13+

getPreviewHeight(): number

获取预览图的高。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 预览图的高。 单位：vp。 |

#### get[ContextMenuMediaType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenumediatype9)22+

get[ContextMenuMediaType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenumediatype9)(): ContextMenuDataMediaType

在上报上下文菜单事件时，获取用户点击的网页元素类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuDataMediaType](../enums/Enums.md#ZH-CN_TOPIC_0000002497605218__contextmenudatamediatype22) | 网页元素媒体类型。 |