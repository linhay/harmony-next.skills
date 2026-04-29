# Class (GeolocationPermissions)

Web组件地理位置权限管理对象。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准。

-

目前调用GeolocationPermissions下的方法，都需要先加载Web组件。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

#### 需要权限

访问地理位置时需添加权限：ohos.permission.LOCATION、ohos.permission.APPROXIMATELY_LOCATION、ohos.permission.LOCATION_IN_BACKGROUND，具体权限说明请参考[位置服务](@ohos.geolocation (位置服务).md)。

#### allowGeolocation

static allowGeolocation(origin: string, incognito?: boolean): void

允许指定来源使用地理位置接口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| incognito11+ | boolean | 否 | true表示隐私模式下允许指定来源使用地理位置，false表示正常非隐私模式下允许指定来源使用地理位置。 默认值：false。 传入null或undefined时为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码]([Webview错误码](../../errors/Webview错误码.md).md)、[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('allowGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.allowGeolocation(this.origin);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### deleteGeolocation

static deleteGeolocation(origin: string, incognito?: boolean): void

清除指定来源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| incognito11+ | boolean | 否 | true表示隐私模式下清除指定来源的地理位置权限状态，false表示正常非隐私模式下清除指定来源的地理位置权限状态。 默认值：false。 传入null或undefined时为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('deleteGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.deleteGeolocation(this.origin);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getAccessibleGeolocation

static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void

以回调方式异步获取指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| callback | AsyncCallback<boolean> | 是 | 返回指定源的地理位置权限状态。 获取成功，true表示已授权，false表示拒绝访问。 获取失败，表示不存在指定源的权限状态。 |
| incognito11+ | boolean | 否 | true表示获取隐私模式下以回调方式异步获取指定源的地理位置权限状态，false表示正常非隐私模式下以回调方式异步获取指定源的地理位置权限状态。 默认值：false。 传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('getAccessibleGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
              if (error) {
                console.error(`getAccessibleGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              console.info('getAccessibleGeolocationAsync result: ' + result);
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getAccessibleGeolocation

static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>

以Promise方式异步获取指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| incognito11+ | boolean | 否 | true表示获取隐私模式下以Promise方式异步获取指定源的地理位置权限状态，false表示正常非隐私模式下以Promise方式异步获取指定源的地理位置权限状态。 默认值：false。 传入null或undefined时会抛出异常错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise实例，用于获取指定源的权限状态。 获取成功，true表示已授权，false表示拒绝访问。 获取失败，表示不存在指定源的权限状态。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](Webview错误码.md)、[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('getAccessibleGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getAccessibleGeolocation(this.origin)
              .then(result => {
                console.info('getAccessibleGeolocationPromise result: ' + result);
              }).catch((error: BusinessError) => {
              console.error(`getAccessibleGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}`);
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getStoredGeolocation

static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void

以回调方式异步获取已存储地理位置权限状态的所有源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | 返回已存储地理位置权限状态的所有源信息。 |
| incognito11+ | boolean | 否 | true表示获取隐私模式下以回调方式异步获取已存储地理位置权限状态的所有源信息，false表示正常非隐私模式下以回调方式异步获取已存储地理位置权限状态的所有源信息。 默认值：false。 传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getStoredGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getStoredGeolocation((error, origins) => {
              if (error) {
                console.error(`getStoredGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              let origins_str: string = origins.join();
              console.info('getStoredGeolocationAsync origins: ' + origins_str);
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### getStoredGeolocation

static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>

以Promise方式异步获取已存储地理位置权限状态的所有源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示获取隐私模式下以Promise方式异步获取已存储地理位置权限状态的所有源信息，false表示正常非隐私模式下以Promise方式异步获取已存储地理位置权限状态的所有源信息。 默认值：false。 传入null或undefined时会抛出异常错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise实例，用于获取已存储地理位置权限状态的所有源信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getStoredGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.getStoredGeolocation()
              .then(origins => {
                let origins_str: string = origins.join();
                console.info('getStoredGeolocationPromise origins: ' + origins_str);
              }).catch((error: BusinessError) => {
              console.error(`getStoredGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}`);
            });
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```

#### deleteAllGeolocation

static deleteAllGeolocation(incognito?: boolean): void

清除所有来源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示获取隐私模式下清除所有来源的地理位置权限状态，false表示正常非隐私模式下清除所有来源的地理位置权限状态。 默认值：false。 传入null或undefined时为false。 |

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('deleteAllGeolocation')
        .onClick(() => {
          try {
            webview.GeolocationPermissions.deleteAllGeolocation();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
```