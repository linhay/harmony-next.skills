# Class (Router)

提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 10开始支持。

-

以下API需先使用UIContext中的[getRouter()](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取到Router对象，再通过该对象调用对应方法。

#### pushUrl

pushUrl(options: router.RouterOptions): Promise<void>

跳转到应用内的指定页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushUrl({
        url: 'pages/routerpage2',
        params: {
          data1: 'message',
          data2: {
            data3: [123, 456, 789]
          }
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### pushUrl

pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushUrl({
      url: 'pages/routerpage2',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushUrl success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### pushUrl

pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>

跳转到应用内的指定页面，使用Promise异步回调。与[pushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushUrl({
        url: 'pages/routerpage2',
        params: {
          data1: 'message',
          data2: {
            data3: [123, 456, 789]
          }
        }
      }, rtm.Standard)
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### pushUrl

pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。使用callback异步回调。与[pushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushUrl({
      url: 'pages/routerpage2',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, rtm.Standard, (err) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushUrl success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceUrl

replaceUrl(options: router.RouterOptions): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceUrl({
        url: 'pages/detail',
        params: {
          data1: 'message'
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceUrl

replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceUrl({
      url: 'pages/detail',
      params: {
        data1: 'message'
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceUrl success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceUrl

replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。与[replaceUrl](#ZH-CN_TOPIC_0000002497604782__replaceurl)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Failed to get the delegate. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceUrl({
        url: 'pages/detail',
        params: {
          data1: 'message'
        }
      }, rtm.Standard)
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceUrl

replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。使用callback异步回调。与[replaceUrl](#ZH-CN_TOPIC_0000002497604782__replaceurl-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceUrl({
      url: 'pages/detail',
      params: {
        data1: 'message'
      }
    }, rtm.Standard, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceUrl failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceUrl success');
    });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions): Promise<void>

跳转到指定的命名路由页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushNamedRoute({
        name: 'myPage',
        params: {
          data1: 'message',
          data2: {
            data3: [123, 456, 789]
          }
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushNamedRoute({
      name: 'myPage',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>

跳转到指定的命名路由页面，使用Promise异步回调。与[pushNamedRoute](#ZH-CN_TOPIC_0000002497604782__pushnamedroute)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp{
  Standard:router.RouterMode = router.RouterMode.Standard;
}
let rtm:RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushNamedRoute({
        name: 'myPage',
        params: {
          data1: 'message',
          data2: {
            data3: [123, 456, 789]
          }
        }
      }, rtm.Standard)
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### pushNamedRoute

pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。使用callback异步回调。与[pushNamedRoute](#ZH-CN_TOPIC_0000002497604782__pushnamedroute-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().pushNamedRoute({
      name: 'myPage',
      params: {
        data1: 'message',
        data2: {
          data3: [123, 456, 789]
        }
      }
    }, rtm.Standard, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`pushNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('pushNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401if the number of parameters is less than 1 or the type of the url parameter is not string.100001The UI execution context is not found. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceNamedRoute({
        name: 'myPage',
        params: {
          data1: 'message'
        }
      })
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceNamedRoute({
      name: 'myPage',
      params: {
        data1: 'message'
      }
    }, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。与[replaceNamedRoute](#ZH-CN_TOPIC_0000002497604782__replacenamedroute)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Failed to get the delegate. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceNamedRoute({
        name: 'myPage',
        params: {
          data1: 'message'
        }
      }, rtm.Standard)
      .then(() => {
        console.info('succeeded');
      })
      .catch((error: BusinessError) => {
        console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
      })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### replaceNamedRoute

replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。使用callback异步回调。与[replaceNamedRoute](#ZH-CN_TOPIC_0000002497604782__replacenamedroute-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.NamedRouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。mode[router.RouterMode](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是

router跳转结果回调函数。

当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[页面路由错误码](../../errors/页面路由错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401if the number of parameters is less than 1 or the type of the url parameter is not string.100001The UI execution context is not found. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class RouterTmp {
  Standard: router.RouterMode = router.RouterMode.Standard;
}

let rtm: RouterTmp = new RouterTmp();

@Entry
@Component
struct Index {
  async routePage() {
    this.getUIContext().getRouter().replaceNamedRoute({
      name: 'myPage',
      params: {
        data1: 'message'
      }
    }, rtm.Standard, (err: Error) => {
      if (err) {
        let message = (err as BusinessError).message;
        let code = (err as BusinessError).code;
        console.error(`replaceNamedRoute failed, code is ${code}, message is ${message}`);
        return;
      }
      console.info('replaceNamedRoute success');
    })
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage();
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### back

back(options?: router.RouterOptions ): void

返回上一页面或指定的页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.RouterOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routeroptions)否

返回页面描述信息，其中参数url指路由跳转时返回到指定url的页面，如果页面栈中没有对应url的页面，则不响应该操作；如果栈中存在对应url的页面，则返回至index最大的同名页面。

如果url未设置，则返回上一页，页面不会重新构建，页面栈里面的page不会回收，出栈后会被回收。

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
router.back({url:'pages/detail'});
```

#### back12+

back(index: number, params?: Object): void

返回指定的页面。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是

跳转目标页面的索引值。

 取值范围：[0, +∞)

paramsObject否页面返回时携带的参数。

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
router.back(1);
```

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
router.back(1, {info:'来自Home页'}); //携带参数返回
```

#### clear

clear(): void

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
router.clear();
```

#### getLength

getLength(): string

获取当前在页面栈内的页面数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明string页面数量，页面栈支持最大数值是32。

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
let size = router.getLength();
console.info('pages stack size = ' + size);
```

#### getState

getState(): router.RouterState

获取当前页面的状态信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明router.[RouterState](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routerstate)页面状态信息。

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
let page = router.getState();
if (page != undefined) {
  console.info('current index = ' + page.index);
  console.info('current name = ' + page.name);
  console.info('current path = ' + page.path);
}
```

#### getStateByIndex12+

getStateByIndex(index: number): router.RouterState | undefined

通过索引值获取对应页面的状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是

表示要获取的页面索引。

 取值范围：[0, +∞)

**返回值：**

类型说明router.[RouterState](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routerstate) | undefined返回页面状态信息。索引不存在时返回undefined。

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info('params = ' + options.params);
}
```

#### getStateByUrl12+

getStateByUrl(url: string): Array<router.[RouterState](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routerstate)>

通过url获取当前页面的状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明urlstring是表示要获取对应页面信息的url。

**返回值：**

类型说明Array<router.[RouterState](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routerstate)>页面状态信息。

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
let options:Array<router.RouterState> = router.getStateByUrl('pages/index');
for (let i: number = 0; i < options.length; i++) {
  console.info('index = ' + options[i].index);
  console.info('name = ' + options[i].name);
  console.info('path = ' + options[i].path);
  console.info('params = ' + options[i].params);
}
```

#### showAlertBeforeBackPage

showAlertBeforeBackPage(options: router.EnableAlertOptions): void

开启页面返回询问对话框。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[router.EnableAlertOptions](../../modules/ohos/@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__enablealertoptions)是文本弹窗信息描述。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[接口调用异常错误码](../../errors/接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
try {
  router.showAlertBeforeBackPage({
    message: 'Message Info'
  });
} catch(error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(`showAlertBeforeBackPage failed, code is ${code}, message is ${message}`);
}
```

#### hideAlertBeforeBackPage

hideAlertBeforeBackPage(): void

禁用页面返回询问对话框。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();

let router: Router = uiContext.getRouter();
router.hideAlertBeforeBackPage();
```

#### getParams

getParams(): Object

获取发起跳转的页面往当前页传入的参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Object发起跳转的页面往当前页传入的参数。

**示例：**

完整示例请参考[PushUrl](#ZH-CN_TOPIC_0000002497604782__pushurl)中的示例。

```ets
import { Router , UIContext } from '@kit.ArkUI';
let uiContext: UIContext = this.getUIContext();
let router: Router = uiContext.getRouter();
router.getParams();
```