# Class (VerifyPinHandler)

Web组件返回的pin码认证用户处理功能对象。示例代码参考[onVerifyPin](../../topics/misc/事件.md#ZH-CN_TOPIC_0000002497445228__onverifypin22)。

-

该组件从API version 22开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 22开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### constructor22+

constructor()

VerifyPinHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### confirm22+

confirm(result: PinVerifyResult): void

通知Web组件PIN码认证结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明result[PinVerifyResult](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497605218__pinverifyresult22)是PIN码认证结果。