# Class (WebKeyboardController)

控制自定义键盘的输入、删除、关闭等操作。示例代码参考[onInterceptKeyboardAttach](../../topics/misc/事件.md#ZH-CN_TOPIC_0000002497445228__oninterceptkeyboardattach12)。

-

该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 12开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### constructor12+

constructor()

WebKeyboardController的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### insertText12+

insertText(text: string): void

Web输入框中插入字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明textstring是向Web输入框插入字符。

#### deleteForward12+

deleteForward(length: number): void

从后往前删除Web输入框中指定长度的字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明lengthnumber是

从后往前删除Web输入框中指定长度的字符。

取值范围：[-2147483648 , 2147483647]，当参数值大于字符长度时，默认删除光标前面所有字符；参数值为负数时，不执行删除操作。

#### deleteBackward12+

deleteBackward(length: number): void

从前往后删除Web输入框中指定长度的字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明lengthnumber是

从前往后删除Web输入框中指定长度的字符。

取值范围：[-2147483648 , 2147483647]，当参数值大于字符长度时，默认删除光标后面所有字符；参数值为负数时，不执行删除操作。

#### sendFunctionKey12+

sendFunctionKey(key: number): void

插入功能按键，目前仅支持Enter键类型，取值见[EnterKeyType](../../modules/ohos/@ohos.inputMethod (输入法框架).md#ZH-CN_TOPIC_0000002529285281__enterkeytype10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明keynumber是向Web输入框传递功能键，目前仅支持Enter键。

#### close12+

close(): void

关闭自定义键盘。

**系统能力：** SystemCapability.Web.Webview.Core