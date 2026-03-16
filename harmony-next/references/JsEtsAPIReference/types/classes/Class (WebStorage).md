# Class (WebStorage)

通过WebStorage可管理Web SQL数据库接口和HTML5 Web存储接口，每个应用中的所有Web组件共享一个WebStorage。

-

本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

-

目前调用WebStorage下的方法，都需要先加载Web组件。

-

本Class下的接口在ArkWeb内核升级到M132版本后因内核废弃Web SQL，对Web SQL数据库的管理失效。ArkWeb内核版本参考ArkWeb简介[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-overview#约束与限制)。

#### 导入模块

```ets
import { webview } from '@kit.ArkWeb';
```

#### deleteOrigin

static deleteOrigin(origin: string): void

清除指定源所使用的存储。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明originstring是指定源的字符串索引，来自于[getOrigins](#ZH-CN_TOPIC_0000002497605198__getorigins)。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)、[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息17100011Invalid origin.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('deleteOrigin')
        .onClick(() => {
          try {
            webview.WebStorage.deleteOrigin(this.origin);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件。

```ets
 <!-- index.html -->
 <!DOCTYPE html>
 <html>
 <head>
   <meta charset="UTF-8">
   <title>test</title>
   <script type="text/javascript">

       // 打开或创建数据库
       var request = indexedDB.open('myDatabase', 1);

       // 如果数据库版本变化或首次创建时触发
       request.onupgradeneeded = function(event) {
           var db = event.target.result;

           // 创建对象存储（表），设置主键为‘id’
           var objectStore = db.createObjectStore('customers', { keyPath: 'id' });

           // 为‘name’创建索引
           objectStore.createIndex('name', 'name', { unique: false });
       };

       // 打开数据库成功时的回调
       request.onsuccess = function(event) {
           var db = event.target.result;

           const customerData = [
               {id: 1, name: 'John Doe', email: 'john@example.com'},
               {id: 2, name: 'John Doe', email: 'john@example.com'},
           ]

           // 插入数据
           var transaction = db.transaction('customers', 'readwrite');
           var objectStore = transaction.objectStore('customers');

           customerData.forEach((customer) => {
               objectStore.add(customer);
           });

           transaction.oncomplete = function () {
               console.info('Transaction completed: data added');
           }

           transaction.onerror = function (event) {
               console.error("Transaction failed", event);
           }

           // 查询数据
           var queryTransaction = db.transaction(['customers']);
           var queryObjectStore = queryTransaction.objectStore('customers');
           var query = queryObjectStore.get(2);

           query.onsuccess = function (event) {
               console.info('query succ');
               console.info('Customer:', event.target.result);
               console.info('Customer id:', event.target.result.id);
               console.info('Customer name:', event.target.result.name);
               console.info('Customer email:', event.target.result.email);
           };

           queryObjectStore.openCursor().onsuccess = (event) => {
               const cursor = event.target.result;
               if (cursor) {
                   var msg = "<p>查询记录：" + cursor.key + "</p>";
                   document.querySelector("#status").innerHTML += msg;
                   var msg = "<p><b>" + cursor.value.name + "</b></p>";
                   document.querySelector("#status").innerHTML += msg;
                   console.info(`SSN ${cursor.key} 对应的名字是 ${cursor.value.name}`);
                   cursor.continue();
               } else {
                   console.info("没有更多记录了")
               }
           }
       };

       // 错误处理
       request.onerror = function(event) {
           console.error('Database error:', event.target.error);
       };

     </script>
 </head>
 <body>
 <div id="status" name="status">状态信息</div>
 </body>
 </html>
```

#### getOrigins

static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void

以回调方式异步获取当前使用Web SQL数据库和HTML5支持的Web存储API的所有源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[WebStorageOrigin](../interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002529285193__webstorageorigin)>>是以数组方式返回源的信息。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)、[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息17100012Invalid web storage origin.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

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
      Button('getOrigins')
        .onClick(() => {
          try {
            webview.WebStorage.getOrigins((error, origins) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              for (let i = 0; i < origins.length; i++) {
                console.info('origin: ' + origins[i].origin);
                console.info('usage: ' + origins[i].usage);
                console.info('quota: ' + origins[i].quota);
              }
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](#ZH-CN_TOPIC_0000002497605198__deleteorigin)接口下的html文件。

#### getOrigins

static getOrigins(): Promise<Array<WebStorageOrigin>>

以Promise方式异步获取当前使用Web SQL数据库和HTML5支持的Web存储API的所有源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

类型说明Promise<Array<[WebStorageOrigin](../interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002529285193__webstorageorigin)>>Promise实例，用于获取当前所有源的信息。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)、[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息17100012Invalid web storage origin.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

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
      Button('getOrigins')
        .onClick(() => {
          try {
            webview.WebStorage.getOrigins()
              .then(origins => {
                for (let i = 0; i < origins.length; i++) {
                  console.info('origin: ' + origins[i].origin);
                  console.info('usage: ' + origins[i].usage);
                  console.info('quota: ' + origins[i].quota);
                }
              })
              .catch((e: BusinessError) => {
                console.error('error: ' + JSON.stringify(e));
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](#ZH-CN_TOPIC_0000002497605198__deleteorigin)接口下的html文件。

#### getOriginQuota

static getOriginQuota(origin: string, callback: AsyncCallback<number>): void

使用callback回调异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储配额，配额以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明originstring是指定源的字符串索引。callbackAsyncCallback<number>是

指定源的存储配额。

number是long型整数，范围为(-2,147,483,648)~(2,147,483,647)。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)、[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息17100011Invalid origin.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginQuota')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginQuota(this.origin, (error, quota) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              console.info('quota: ' + quota);
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](#ZH-CN_TOPIC_0000002497605198__deleteorigin)接口下的html文件。

#### getOriginQuota

static getOriginQuota(origin: string): Promise<number>

以Promise方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储配额，配额以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明originstring是指定源的字符串索引

**返回值：**

类型说明Promise<number>Promise实例，用于获取指定源的存储配额。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)、[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息17100011Invalid origin.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginQuota')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginQuota(this.origin)
              .then(quota => {
                console.info('quota: ' + quota);
              })
              .catch((e: BusinessError) => {
                console.error('error: ' + JSON.stringify(e));
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](#ZH-CN_TOPIC_0000002497605198__deleteorigin)接口下的html文件。

#### getOriginUsage

static getOriginUsage(origin: string, callback: AsyncCallback<number>): void

以回调方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储量，存储量以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明originstring是指定源的字符串索引callbackAsyncCallback<number>是指定源的存储量。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)、[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息17100011Invalid origin.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginUsage')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginUsage(this.origin, (error, usage) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              console.info('usage: ' + usage);
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](#ZH-CN_TOPIC_0000002497605198__deleteorigin)接口下的html文件。

#### getOriginUsage

static getOriginUsage(origin: string): Promise<number>

以Promise方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储量，存储量以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明originstring是指定源的字符串索引

**返回值：**

类型说明Promise<number>Promise实例，用于获取指定源的存储量。

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](../../errors/Webview错误码.md)、[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息17100011Invalid origin.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginUsage')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginUsage(this.origin)
              .then(usage => {
                console.info('usage: ' + usage);
              }).catch((e: BusinessError) => {
              console.error('error: ' + JSON.stringify(e));
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](#ZH-CN_TOPIC_0000002497605198__deleteorigin)接口下的html文件。

#### deleteAllData

static deleteAllData(incognito?: boolean): void

清除被JavaScript存储API使用的所有存储数据，这包括Web SQL数据库和HTML5支持的Web存储API。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明incognito11+boolean否

true表示删除所有隐私模式下内存中的web数据，false表示删除正常非隐私模式下Web的SQL数据库当前使用的所有存储。

默认值：false。

传入undefined或null时为false。

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
      Button('deleteAllData')
        .onClick(() => {
          try {
            webview.WebStorage.deleteAllData();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](#ZH-CN_TOPIC_0000002497605198__deleteorigin)接口下加载的html文件。