# Class (AdsBlockManager)

通过AdsBlockManager可以向Web组件中设置自定义的广告过滤配置、关闭特定网站的广告过滤功能，其中每个应用中的所有Web组件都共享一个AdsBlockManager实例。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 12开始支持。

-

示例效果请以真机运行为准。

-

静态方法必须在用户界面（UI）线程上使用。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

#### setAdsBlockRules12+

static setAdsBlockRules(rulesFile: string, replace: boolean): void

向Web组件中设置自定义的符合通用easylist语法规则的广告过滤配置文件。

此接口设置的广告过滤规则，内部解析成功后会持久化存储，应用重启后不需要重复设置。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rulesFile | string | 是 | 指定了符合 easylist 通用语法的规则文件路径，应用需要有此文件的读权限。 |
| replace | boolean | 是 | true表示强制替换掉内置的默认规则，false表示设置的自定义规则将与内置规则共同工作。 |

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { picker, fileUri } from '@kit.CoreFileKit';

// 演示点击按钮，通过filepicker打开一个easylist规则文件并设置到Web组件中
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Flex() {
        Button({ type: ButtonType.Capsule }) {
          Text("setAdsBlockRules")
        }
        .onClick(() => {
          try {
            let documentSelectionOptions: ESObject = new picker.DocumentSelectOptions();
            let documentPicker: ESObject = new picker.DocumentViewPicker();
            documentPicker.select(documentSelectionOptions).then((documentSelectResult: ESObject) => {
              if (documentSelectResult && documentSelectResult.length > 0) {
                let fileRealPath = new fileUri.FileUri(documentSelectResult[0]);
                console.info('DocumentViewPicker.select successfully, uri: ' + fileRealPath);
                webview.AdsBlockManager.setAdsBlockRules(fileRealPath.path, true);
              }
            })
          } catch (err) {
            console.error('DocumentViewPicker.select failed with err:' + err);
          }
        })
      }
```

#### addAdsBlockDisallowedList12+

static addAdsBlockDisallowedList(domainSuffixes: Array<string>): void

向AdsBlockManager的DisallowedList中添加一组域名。广告过滤功能开启时，将禁用这些网站的广告过滤功能。

此接口设置的域名不会持久化，应用重启需要重新设置。

广告过滤特性会使用后缀匹配的方式判断domainSuffix和当前站点的url是否能匹配，例如，当前Web组件打开的网站是[https://www.example.com，设置的DisallowList中有'example.com'或者'www.example.com'，后缀匹配成功，此网站将禁用广告过滤，访问'https://m.example.com'也将禁用广告过滤。](https://www.example.com，设置的DisallowList中有'example.com'%E6%88%96%E8%80%85'www.example.com'%EF%BC%8C%E5%90%8E%E7%BC%80%E5%8C%B9%E9%85%8D%E6%88%90%E5%8A%9F%EF%BC%8C%E6%AD%A4%E7%BD%91%E7%AB%99%E5%B0%86%E7%A6%81%E7%94%A8%E5%B9%BF%E5%91%8A%E8%BF%87%E6%BB%A4%EF%BC%8C%E8%AE%BF%E9%97%AE'https://m.example.com'%E4%B9%9F%E5%B0%86%E7%A6%81%E7%94%A8%E5%B9%BF%E5%91%8A%E8%BF%87%E6%BB%A4%E3%80%82)

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 演示通过一个按钮的点击向Web组件设置广告过滤的域名策略
@Entry
@Component
struct WebComponent {
  main_url: string = 'https://www.example.com';
  text_input_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();
  @State input_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
            .id("input_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input_text);
          })

          Button({type: ButtonType.Capsule}) { Text("addAdsBlockDisallowedList") }
          .onClick(() => {
            let arrDomainSuffixes = new Array<string>();
            arrDomainSuffixes.push('example.com');
            arrDomainSuffixes.push('abcdefg.cn');
            webview.AdsBlockManager.addAdsBlockDisallowedList(arrDomainSuffixes);
          })
        }
      Web({ src: this.main_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true);
        })
}
```

#### removeAdsBlockDisallowedList12+

static removeAdsBlockDisallowedList(domainSuffixes: Array<string>): void

从AdsBlockManager的DisallowedList中删除一组域名。

AdsBlockManager的DisallowedList不会持久化，应用重启需要重新设置。删除不存在的条目不会触发异常。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 演示通过一个按钮的点击从AdsBlockManager的DisallowedList中删除域名元素
@Entry
@Component
struct WebComponent {
  main_url: string = 'https://www.example.com';
  text_input_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();
  @State input_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
            .id("input_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input_text);
          })

          Button({type: ButtonType.Capsule}) { Text("removeAdsBlockDisallowedList") }
          .onClick(() => {
            let arrDomainSuffixes = new Array<string>();
            arrDomainSuffixes.push('example.com');
            arrDomainSuffixes.push('abcdefg.cn');
            webview.AdsBlockManager.removeAdsBlockDisallowedList(arrDomainSuffixes);
          })
        }
      Web({ src: this.main_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true);
        })
}
```

#### clearAdsBlockDisallowedList12+

static clearAdsBlockDisallowedList(): void

清空AdsBlockManager的DisallowedList。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  main_url: string = 'https://www.example.com';
  text_input_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();
  @State input_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
            .id("input_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input_text);
          })

          Button({type: ButtonType.Capsule}) { Text("clearAdsBlockDisallowedList") }
          .onClick(() => {
            webview.AdsBlockManager.clearAdsBlockDisallowedList();
          })
        }
      Web({ src: this.main_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true);
        })
}
```

#### addAdsBlockAllowedList12+

static addAdsBlockAllowedList(domainSuffixes: Array<string>): void

向AdsBlockManager的AllowedList中添加一组域名，主要用于重新开启DisallowList中的部分网站的广告过滤。

此接口设置的域名不会持久化，应用重启需要重新设置。

AllowedList的优先级比DisAllowList高，例如，DisallowList中配置了['example.com']，禁用了所有example.com域名下的网页，此时如果需要开启'news.example.com'下的广告过滤，可以使用addAdsBlockAllowedList(['news.example.com'])。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 演示通过一个按钮的点击向Web组件设置广告过滤的域名策略
@Entry
@Component
struct WebComponent {
  main_url: string = 'https://www.example.com';
  text_input_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();
  @State input_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
            .id("input_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input_text);
          })

          Button({type: ButtonType.Capsule}) { Text("addAdsBlockAllowedList") }
          .onClick(() => {
            let arrDisallowDomainSuffixes = new Array<string>();
            arrDisallowDomainSuffixes.push('example.com');
            webview.AdsBlockManager.addAdsBlockDisallowedList(arrDisallowDomainSuffixes);

            let arrAllowedDomainSuffixes = new Array<string>();
            arrAllowedDomainSuffixes.push('news.example.com');
            webview.AdsBlockManager.addAdsBlockAllowedList(arrAllowedDomainSuffixes);
          })
        }
      Web({ src: this.main_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true)
        })
}
```

#### removeAdsBlockAllowedList12+

static removeAdsBlockAllowedList(domainSuffixes: Array<string>): void

从AdsBlockManager的AllowedList中删除一组域名。

AdsBlockManager的AllowedList不会持久化，应用重启需要重新设置。删除不存在的条目不会触发异常。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 演示通过一个按钮的点击从AdsBlockManager的DisallowedList中删除域名元素
@Entry
@Component
struct WebComponent {
  main_url: string = 'https://www.example.com';
  text_input_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();
  @State input_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
            .id("input_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input_text);
          })

          Button({type: ButtonType.Capsule}) { Text("removeAdsBlockAllowedList") }
          .onClick(() => {
            let arrDomainSuffixes = new Array<string>();
            arrDomainSuffixes.push('example.com');
            arrDomainSuffixes.push('abcdefg.cn');
            webview.AdsBlockManager.removeAdsBlockAllowedList(arrDomainSuffixes);
          })
        }
      Web({ src: this.main_url, controller: this.controller })
        .onControllerAttached(()=>{
          this.controller.enableAdsBlock(true);
        })
}
```

#### clearAdsBlockAllowedList12+

static clearAdsBlockAllowedList(): void

清空AdsBlockManager的AllowedList。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  main_url: string = 'https://www.example.com';
  text_input_controller: TextInputController = new TextInputController();
  controller: webview.WebviewController = new webview.WebviewController();
  @State input_text: string = 'https://www.example.com';

  build() {
    Column() {
      Row() {
        Flex() {
          TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
            .id("input_url")
            .height(40)
            .margin(5)
            .borderColor(Color.Blue)
            .onChange((value: string) => {
              this.input_text = value;
            })

          Button({type: ButtonType.Capsule}) { Text("Go") }
          .onClick(() => {
            this.controller.loadUrl(this.input_text);
          })

          Button({type: ButtonType.Capsule}) { Text("clearAdsBlockAllowedList") }
          .onClick(() => {
            webview.AdsBlockManager.clearAdsBlockAllowedList();
          })
        }
      Web({ src: this.main_url, controller: this.controller })
      .onControllerAttached(()=>{
        this.controller.enableAdsBlock(true);
      })
    }
```