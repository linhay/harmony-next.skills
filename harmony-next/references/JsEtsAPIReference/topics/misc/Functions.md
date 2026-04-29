# Functions


-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

示例效果请以真机运行为准。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

**webview.once**

once(type: string, callback: Callback<void>): void

订阅一次指定类型Web事件的回调，Web事件的类型目前仅支持"webInited"，在Web引擎初始化完成时触发。

当应用中开始加载第一个Web组件时，Web引擎初始化，且后续再在同一应用中继续加载其他Web组件时不会再触发once接口。当应用销毁最后一个Web组件时，若再加载第一个Web组件，应用重新进入Web引擎初始化流程。

系统能力： SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | Web事件的类型，目前支持："webInited"（Web初始化完成）。 |
| callback | Callback<void> | 是 | 所订阅的回调函数。 |

**[错误码](../../errors/错误码.md)：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| [错误码](../../errors/错误码.md)ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

webview.once("webInited", () => {
  console.info("configCookieSync");
  webview.WebCookieManager.configCookieSync("https://www.example.com", "a=b");
})

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      }
```