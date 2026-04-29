# Class (Tool)

本模块定义的工具类，仅提供静态的方法，主要完成其他模块和[common2D](@ohos.graphics.common2D (2D图形通用数据类型).md)中定义的数据结构的转换功能等操作。


-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 15开始支持。

-

本模块使用屏幕物理像素单位px。

-

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

#### 导入模块

```ets
import { drawing } from '@kit.ArkGraphics2D';
```

#### makeColorFrom[ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)15+

static makeColorFrom[ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)(resourceColor: [Resource](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)Color): common2D.Color

将[ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)类型的值转换为common2D.Color对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceColor | [ResourceColor](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 是 | ResourceColor格式的颜色值（支持所有的4种输入，示例中提供13个示例输入）。其中第4种类型Resource只接受$r('belonging.type.name')构造方法，需要确保该资源在main/resources/base/element目录下已定义(app支持color、string和integer，sys只支持color)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color | 转换后的common2D.Color颜色对象，若转换失败则返回空指针。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```ets
import { drawing, common2D } from '@kit.ArkGraphics2D';

// Color
let color1: common2D.Color = drawing.Tool.makeColorFromResourceColor(Color.Blue);

// Number
let color2: common2D.Color = drawing.Tool.makeColorFromResourceColor(0xffc0cb);
let color3: common2D.Color = drawing.Tool.makeColorFromResourceColor(0x11ffa500);

// String
let color4: common2D.Color = drawing.Tool.makeColorFromResourceColor('#ff0000');
let color5: common2D.Color = drawing.Tool.makeColorFromResourceColor('#110000ff');
let color6: common2D.Color = drawing.Tool.makeColorFromResourceColor('#00f');
let color7: common2D.Color = drawing.Tool.makeColorFromResourceColor('#100f');
let color8: common2D.Color = drawing.Tool.makeColorFromResourceColor('rgb(255, 100, 255)');
let color9: common2D.Color = drawing.Tool.makeColorFromResourceColor('rgba(255, 100, 255, 0.5)');

// Resource
let color10: common2D.Color = drawing.Tool.makeColorFromResourceColor($r('sys.color.ohos_id_color_secondary'));

// Use color
let brush = new drawing.Brush();
brush.setColor(color1);
```