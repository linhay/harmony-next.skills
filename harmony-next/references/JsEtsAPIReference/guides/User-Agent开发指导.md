# User-Agent开发指导

本文根据华为开发者官网 `web-default-useragent` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-default-useragent>
更新时间：2026-04-30 09:02:20

## 默认User-Agent结构
默认User-Agent定义
Mozilla/5.0 ({DeviceType}; {OSName} {OSVersion}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ChromeCompatibleVersion}.0.0.0 Safari/537.36 ArkWeb/{ArkWeb VersionCode} {DeviceCompat} {扩展区}
举例说明
Mozilla/5.0 (Phone; OpenHarmony 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 ArkWeb/4.1.6.1 Mobile
字段说明
字段
含义
DeviceType
当前的设备类型。
取值范围：
- Phone：手机设备
- Tablet：平板设备

## 自定义User-Agent结构
在下面的示例中，通过调用getUserAgent()接口获取当前默认的用户代理（User-Agent）字符串。这一接口提供的默认User-Agent信息为开发者提供了基础，使开发者能够基于这个默认信息进行定制或扩展。
// xxx.ets import { webview } from '@kit.ArkWeb'; import { BusinessError } from '@kit.BasicServicesKit'; @Entry @Component struct WebComponent { controller: webview.WebviewController = new webview.WebviewController(); build() { Column() { Button('getUserAgent') .onClick(() => { try { let userAgent = this.controller.getUserAgent(); console.info("userAgent: " + userAgent); } catch (error) { console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`); } }) Web({ src: 'www.example.com', controller: this.controller }) } } }
以下示例通过setCustomUserAgent()接口设置自定义用户代理，但请注意，此操作会覆盖系统的用户代理。因此，我们建议将扩展字段追加在默认用户代理的末尾，比如三方应用程序的开发场景，可以在系统默认用户代理字符串的末尾追加特定的APP标识，这样既能保留原有用户代理信息，又能增加自定义的应用识别信息。
当Web组件src设置了url时，建议在onControllerAttached回调事件中设置User-Agent，设置方式请参考示例。不建议将User-Agent设置在onLoadIntercept回调事件中，会概率性出现设置失败。若未在onControllerAttached回调事件中设置User-Agent，后续调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。
当Web组件src设置为空字符串时，建议先调用setCustomUserAgent方法设置User-Agent，再通过loadUrl加载具体页面。
// xxx.ets import { webview } from '@kit.ArkWeb'; import { BusinessError } from '@kit.BasicServicesKit'; @Entry @Component struct WebComponent { controller: webview.WebviewController = new webview.WebviewController(); // 三方应用相关信息标识 @State customUserAgent: string = ' DemoApp'; build() { Column() { Web({ src: 'www.example.com', controller: this.controller }) .onControllerAttached(() => { console.info("onControllerAttached"); try { let userAgent = this.controller.getUserAgent() + this.customUserAgent; this.controller.setCustomUserAgent(userAgent); } catch (error) { console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`); } }) } } }
从API version 20开始，可通过setAppCustomUserAgent()接口设置应用级自定义用户代理，或者通过setUserAgentForHosts()对特定网站设置应用级自定义用户代理，覆盖系统的用户代理，应用内所有Web组件生效。
建议在Web组件创建前先调用静态接口getDefaultUserAgent获取默认的用户代理（User-Agent）字符串，然后调用setAppCustomUserAgent，setUserAgentForHosts方法设置User-Agent，再创建指定src的Web组件或通过loadUrl加载具体页面。
// xxx.ets import { webview } from '@kit.ArkWeb'; import { BusinessError } from '@kit.BasicServicesKit'; @Entry @Component struct WebComponent { controller: webview.WebviewController = new webview.WebviewController(); aboutToAppear(): void { try { webview.WebviewController.initializeWebEngine(); let defaultUserAgent = webview.WebviewController.getDefaultUserAgent(); let appUA = defaultUserAgent + " appUA"; webview.WebviewController.setAppCustomUserAgent(appUA); webview.WebviewController.setUserAgentForHosts( appUA, [ "www.example.com", "www.baidu.com" ] ); } catch (error) { console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`); } } build() { Column() { Web({ src: 'www.example.com', controller: this.controller }) } } }
在下面的示例中，通过getCustomUserAgent()接口获取自定义用户代理。
// xxx.ets import { webview } from '@kit.ArkWeb'; import { BusinessError } from '@kit.BasicServicesKit'; @Entry @Component struct WebComponent { controller: webview.WebviewController = new webview.WebviewController(); @State userAgent: string = ''; build() { Column() { Button('getCustomUserAgent') .onClick(() => { try { this.userAgent = this.controller.getCustomUserAgent(); console.info("userAgent: " + this.userAgent); } catch (error) { console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`); } }) Web({ src: 'www.example.com', controller: this.controller }) } } }

## 相关User-Agent接口优先级
接口名称
优先级
说明
setCustomUserAgent
最高
对调用的Web组件生效。
setUserAgentForHosts
低于setCustomUserAgent
对应用中所有Web组件访问指定网站生效。
setAppCustomUserAgent
低于setUserAgentForHosts
对应用中所有Web组件生效。

## 常见问题

## 如何通过User-Agent来识别HarmonyOS操作系统中不同设备
HarmonyOS设备的识别主要通过User-Agent中的系统、系统版本和设备类型三个维度来判断。建议同时检查上述信息，以确保更准确的设备识别。
系统识别
通过User-Agent中的{OSName}字段识别HarmonyOS系统。
const isHarmonyOS = () => /OpenHarmony/i.test(navigator.userAgent);
系统版本识别
通过User-Agent中的{OSName}和{OSVersion}字段识别HarmonyOS NEXT系统及系统版本。格式为：OpenHarmony + 版本号。
// 检测是否是HarmonyOS NEXT系统 const matches = navigator.userAgent.match(/OpenHarmony (\d+\.?\d*)/); matches?.length && Number(matches[1]) >= 5;
设备类型识别
通过deviceType字段来识别不同设备类型。
// 检测是否为手机设备 const isPhone = () => /Phone/i.test(navigator.userAgent); // 检测是否为平板设备 const isTablet = () => /Tablet/i.test(navigator.userAgent); // 检测是否为2in1设备 const is2in1 = () => /PC/i.test(navigator.userAgent);

## 如何模拟HarmonyOS操作系统的User-Agent进行前端调试
在Windows/Mac/Linux等操作系统中，可以通过Chrome/Edge/Firefox等浏览器DevTools提供的User-Agent复写能力，模拟HarmonyOS User-Agent。

## 如何在HarmonyOS中自定义User-Agent以实现H5兼容性
HarmonyOS提供setCustomUserAgent接口以支持User-Agent的自定义设置。为适配移动端H5页面通常依赖的UA标识检测（如Mobile、OpenHarmony等），并确保不覆盖系统默认UA信息，推荐按如下方式操作：首先通过getDefaultUserAgent接口获取系统默认User-Agent字符串，随后将H5兼容所需的自定义标识字段追加至该字符串末尾，最后调用setCustomUserAgent接口设置修改后的完整UA字符串。

## 如何解决H5页面的UA兼容性问题
Q：移动设备上网页呈现电脑版样式或电脑设备上网页呈现移动样式展示
A：网站会针对不同UA展示不同样式页面。需要移动设备UA设置DeviceCompat为"Mobile"，DeviceType为"Phone"，PC设备UA设置DeviceCompat为""，DeviceType为"PC"，平板设备UA设置DeviceCompat为""，DeviceType则为"Tablet"。
Q：部分网页打不开或显示“不支持的浏览器”
A：网页未适配OpenHarmony UA，需要网页对"OpenHarmony"标识作兼容处理。
Q：页面循环跳转
A：应用端对存在跳转关系的两个页面设置了冲突的UA标识‌，导致服务端重定向逻辑陷入死循环。确保应用端在调用setUserAgentForHosts对关联网站设置兼容UA时保持逻辑一致， 避免因UA差异触发网页跳转逻辑循环。
Q：网页提供的下载链接与设备平台不匹配，如OpenHarmony设备上下载安装包为apk等
A：UA 中的“兼容性字段”干扰了服务端识别。为了保障网页兼容性，部分浏览器可能会在用户代理（User-Agent）中增加非OpenHarmony的操作系统名称，如果服务端的解析逻辑顺序不当，可能会忽略掉真正的设备标识。针对这种场景，建议网页将OpenHarmony的处理逻辑放置在其他操作系统处理逻辑之前。

## 示例代码
Web用户代理
