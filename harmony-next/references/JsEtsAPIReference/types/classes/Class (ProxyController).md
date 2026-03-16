# Class (ProxyController)

此类用于为应用程序设置代理。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 15开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

#### applyProxyOverride15+

static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void

设置应用中所有Web使用的代理配置，与[insertBypassRule](Class (ProxyConfig).md#ZH-CN_TOPIC_0000002497605190__insertbypassrule15)中插入的bypass规则匹配的URL将不会使用代理，而是直接向URL指定的源地址发起请求。代理设置成功后，不保证网络连接后会立即使用新的代理设置，在加载页面之前请等待监听器触发，这个监听器将在UI线程上被调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明proxyConfig[ProxyConfig](Class (ProxyConfig).md)是对代理的配置。callback[OnProxyConfigChangeCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605202__onproxyconfigchangecallback15)是代理设置成功的回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)说明文档。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

完整示例代码参考[removeProxyOverride](Class (ProxyController).md#ZH-CN_TOPIC_0000002529285183__removeproxyoverride15)。

#### removeProxyOverride15+

static removeProxyOverride(callback: OnProxyConfigChangeCallback): void

移除代理配置。移除代理配置后，不保证网络连接后会立即使用新的代理设置，在加载页面之前等待监听器，这个监听器将在UI线程上被调用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明callback[OnProxyConfigChangeCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605202__onproxyconfigchangecallback15)是代理设置成功的回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)说明文档。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  proxyRules: webview.ProxyRule[] = [];

  build() {
    Row() {
      Column() {
        Button("applyProxyOverride").onClick(()=>{
          let proxyConfig:webview.ProxyConfig = new webview.ProxyConfig();
          //优先使用第一个代理配置https://proxy.XXX.com
          //代理失败后会回落到直连服务器insertDirectRule
          try {
            proxyConfig.insertProxyRule("https://proxy.XXX.com", webview.ProxySchemeFilter.MATCH_ALL_SCHEMES);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
          try {
            proxyConfig.insertDirectRule(webview.ProxySchemeFilter.MATCH_HTTP);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
          try {
            proxyConfig.insertBypassRule("*.example.com");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
          proxyConfig.clearImplicitRules();
          proxyConfig.bypassHostnamesWithoutPeriod();
          try {
            proxyConfig.enableReverseBypass(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
          let bypassRules = proxyConfig.getBypassRules();
          for (let i = 0; i < bypassRules.length; i++) {
            console.info("bypassRules: " + bypassRules[i]);
          }
          this.proxyRules = proxyConfig.getProxyRules();
          for (let i = 0; i < this.proxyRules.length; i++) {
            console.info("SchemeFilter: " + this.proxyRules[i].getSchemeFilter());
            console.info("Url: " + this.proxyRules[i].getUrl());
          }
          let isReverseBypassRule = proxyConfig.isReverseBypassEnabled();
          console.info("isReverseBypassRules: " + isReverseBypassRule);
          try {
            webview.ProxyController.applyProxyOverride(proxyConfig, () => {
              console.info("PROXYCONTROLLER proxy changed");
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        Button("loadUrl-https").onClick(()=>{
          this.controller.loadUrl("https://www.example.com")
        })
        Button("loadUrl-http").onClick(()=>{
          this.controller.loadUrl("http://www.example.com")
        })
        Button("removeProxyOverride").onClick(()=>{
          try {
          webview.ProxyController.removeProxyOverride(() => {
            console.info("PROXYCONTROLLER proxy changed");
          });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        Web({ src: 'www.example.com', controller: this.controller})
      }
      .width('100%')
    }
    .height('100%')
  }
}
```