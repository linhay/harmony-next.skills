# DownloadFileButton

下载文件按钮，通过点击该下载按钮，可以获取到当前应用在Download公共目录中所属的存储路径。

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件不支持在Wearable设备上使用。

#### 导入模块

```ets
import { DownloadFileButton } from '@kit.ArkUI';
```

#### 子组件

无

#### 属性

支持[通用属性]([通用属性](../misc/通用属性.md).md)。

#### DownloadFileButton

下载文件按钮组件，默认显示图标和文字。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| contentOptions | DownloadContentOptions | 是 | @State | 创建包含指定元素内容的下载按钮。 |
| styleOptions | DownloadStyleOptions | 是 | @State | 创建包含指定元素样式的下载按钮。 |

#### DownloadContentOptions

下载文件按钮中显示的内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | DownloadIconStyle | 否 | 是 | 设置下载按钮的图标风格。  不传入该参数表示没有图标，icon和text至少存在一个。 |
| text | DownloadDescription | 否 | 是 | 设置下载按钮的文本描述。  不传入该参数表示没有文字描述，icon和text至少存在一个。 |

#### DownloadStyleOptions

下载文件按钮中图标和文字的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconSize | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 是 | 下载控件上图标的尺寸，不支持百分比。  默认值：16vp |
| layoutDirection | DownloadLayoutDirection | 否 | 是 | 下载控件上图标和文字分布的方向。  默认值：DownloadLayoutDirection.HORIZONTAL |
| fontSize | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 是 | 下载控件上文字的尺寸，不支持百分比。  默认值：16fp |
| fontStyle | [FontStyle](枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontstyle) | 否 | 是 | 下载控件上文字的样式。  默认值：FontStyle.Normal |
| fontWeight | number|[FontWeight](枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontweight)|string | 否 | 是 | 下载控件上文字粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Medium |
| fontFamily | string|[Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | 否 | 是 | 下载控件上文字的字体。  默认字体：'HarmonyOS Sans' |
| fontColor | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 是 | 下载控件上文字的颜色。  默认值：#ffffffff |
| iconColor | [Resource](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Color | 否 | 是 | 下载控件上图标的颜色。  默认值：#ffffffff |
| textIconSpace | [Dimension](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10) | 否 | 是 | 下载控件中图标和文字的间距。  默认值：4vp |

#### DownloadIconStyle

下载文件按钮中图标的风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FULL_FILLED | 1 | 下载按钮展示填充样式图标。 |
| LINES | 2 | 下载按钮展示线条样式图标。 |

#### DownloadDescription

下载按钮中文字的内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOWNLOAD | 1 | 下载按钮的文字描述为“下载”。 |
| DOWNLOAD_FILE | 2 | 下载按钮的文字描述为“下载文件”。 |
| SAVE | 3 | 下载按钮的文字描述为“保存”。 |
| SAVE_IMAGE | 4 | 下载按钮的文字描述为“保存图片”。 |
| SAVE_FILE | 5 | 下载按钮的文字描述为“保存文件”。 |
| DOWNLOAD_AND_SHARE | 6 | 下载按钮的文字描述为“下载分享”。 |
| RECEIVE | 7 | 下载按钮的文字描述为“接收”。 |
| CONTINUE_TO_RECEIVE | 8 | 下载按钮的文字描述为“继续接收”。 |

#### DownloadLayoutDirection

下载文件按钮中图标和文字的排列方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HORIZONTAL | 0 | 下载控件上图标和文字分布的方向为水平排列。 |
| VERTICAL | 1 | 下载控件上图标和文字分布的方向为垂直排列。 |

#### 事件

支持[通用事件]([通用事件](../misc/通用事件.md).md)。

#### 示例

```ets
// xxx.ets

import { picker } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { DownloadFileButton, DownloadLayoutDirection, DownloadIconStyle, DownloadDescription } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      DownloadFileButton({
        contentOptions: {
          icon: DownloadIconStyle.FULL_FILLED,
          text: DownloadDescription.DOWNLOAD
        },
        styleOptions: {
          iconSize: '16vp',
          layoutDirection: DownloadLayoutDirection.HORIZONTAL,
          fontSize: '16vp',
          fontStyle: FontStyle.Normal,
          fontWeight: FontWeight.Medium,
          fontFamily: 'HarmonyOS Sans',
          fontColor: '#ffffffff',
          iconColor: '#ffffffff',
          textIconSpace: '4vp'
        }
      })
        .backgroundColor('#007dff')
        .borderStyle(BorderStyle.Dotted)
        .borderWidth(0)
        .borderRadius('24vp')
        .position({ x: 0, y: 0 })
        .markAnchor({ x: 0, y: 0 })
        .offset({ x: 0, y: 0 })
        .constraintSize({})
        .padding({
          top: '12vp',
          bottom: '12vp',
          left: '24vp',
          right: '24vp'
        })
        .onClick(() => {
          this.downloadAction();
        })
    }

  downloadAction() {
    try {
      const document = new picker.DocumentSaveOptions();
      document.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
      new picker.DocumentViewPicker().save(document, (err: BusinessError, result: Array<string>) => {
        if (err) {
          return;
        }
        console.info(`downloadAction result:  ${JSON.stringify(result)}`);
      });
    } catch (e) {
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245364.webp)
