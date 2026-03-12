# @ohos.router (页面路由)(不推荐)

本模块提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。

推荐使用[Navigation组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)作为应用路由框架。

-

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

页面路由需要在页面渲染完成之后才能调用，在onInit和onReady生命周期中页面还处于渲染阶段，禁止调用页面路由方法。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](zh-cn_topic_0000002529444749.html)说明。

-

如果使用传入callback形式的[pushUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushurl-1)或[pushNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushnamedroute-1)接口，callback中通过[getLength](Class (Router).md#ZH-CN_TOPIC_0000002497604782__getlength)等接口获取的栈信息为中间态的栈信息，可能与栈操作完全结束后，再通过[getLength](Class (Router).md#ZH-CN_TOPIC_0000002497604782__getlength)等接口获取的栈信息不一致。

#### 导入模块

```ets
import { router } from '@kit.ArkUI';
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions): Promise<void>

跳转到应用内的指定页面。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushurl)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
})
  .then(() => {
    console.error(`pushUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushurl-1)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, (err) => {
  if (err) {
    console.error(`pushUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushUrl success');
})
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>

跳转到应用内的指定页面。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushurl-2)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`pushUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushurl-3)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100002Uri error. The URI of the page to redirect is incorrect or does not exist.100003Page stack error. Too many pages are pushed.

**示例：**

```ets
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`pushUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushUrl success');
})
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replaceurl)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
})
  .then(() => {
    console.error(`replaceUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replaceurl-1)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, (err) => {
  if (err) {
    console.error(`replaceUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceUrl success');
})
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replaceurl-2)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Failed to get the delegate. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1:string;

  constructor(str:string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`replaceUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replaceurl-3)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.200002Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**示例：**

```ets
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`replaceUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceUrl success');
});
```

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions): Promise<void>

跳转到指定的命名路由页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushnamedroute)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
})
  .then(() => {
    console.error(`pushNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

详细示例请参考：[UI开发-页面路由](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushnamedroute-1)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, (err) => {
  if (err) {
    console.error(`pushNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushNamedRoute success');
})
```

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

跳转到指定的命名路由页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushnamedroute-2)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str
    this.data2 = new innerParams(tuple)
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`pushNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[pushNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushnamedroute-3)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是跳转页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.100003Page stack error. Too many pages are pushed.100004Named route error. The named route does not exist.

**示例：**

```ets
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`pushNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushNamedRoute success');
})
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replacenamedroute)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
})
  .then(() => {
    console.error(`replaceNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replacenamedroute-1)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, (err) => {
  if (err) {
    console.error(`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceNamedRoute success');
})
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replacenamedroute-2)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。

**返回值：**

类型说明Promise<void>异常返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Failed to get the delegate. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`replaceNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

从API version 10开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[replaceNamedRoute](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replacenamedroute-3)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[NamedRouterOptions](#ZH-CN_TOPIC_0000002529444757__namedrouteroptions10)是替换页面描述信息。mode[RouterMode](#ZH-CN_TOPIC_0000002529444757__routermode9)是跳转页面使用的模式。callbackAsyncCallback<void>是异常响应回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[页面路由错误码](页面路由错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

该接口返回的以下错误码均为string类型。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001The UI execution context is not found. This error code is thrown only in the standard system.100004Named route error. The named route does not exist.

**示例：**

```ets
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceNamedRoute success');
});
```

#### router.back(deprecated)

back(options?: RouterOptions ): void

返回上一页面或指定的页面，会删除当前页面与指定页面之间的所有页面。

从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[back](Class (Router).md#ZH-CN_TOPIC_0000002497604782__back)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)否返回页面描述信息，其中参数url指路由跳转时会返回到指定url的界面，如果页面栈上没有url页面，则不响应该情况。如果url未设置，则返回上一页，页面不会重新构建，页面栈里面的page不会回收，出栈后会被回收。back是返回接口，url设置为特殊值"/"不生效。如果是用命名路由的方式跳转，传入的url需是命名路由的名称。

**示例：**

```ets
this.getUIContext().getRouter().back({ url: 'pages/detail' });
```

#### router.back(deprecated)

back(index: number, params?: Object): void;

返回指定的页面，会删除当前页面与指定页面之间的所有页面。

从API version 12开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[back](Class (Router).md#ZH-CN_TOPIC_0000002497604782__back12)。

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是跳转目标页面的索引值。 从栈底到栈顶，index从1开始递增。paramsObject否页面返回时携带的参数。

**示例：**

```ets
this.getUIContext().getRouter().back(1);
```

```ets
this.getUIContext().getRouter().back(1, { info: '来自Home页' }); //携带参数返回
```

#### router.clear(deprecated)

clear(): void

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[clear](Class (Router).md#ZH-CN_TOPIC_0000002497604782__clear)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
this.getUIContext().getRouter().clear();
```

#### router.getLength(deprecated)

getLength(): string

获取当前在页面栈内的页面数量。

从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[getLength](Class (Router).md#ZH-CN_TOPIC_0000002497604782__getlength)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明string页面数量，页面栈支持最大数值是32。

**示例：**

```ets
let size = this.getUIContext().getRouter().getLength();
console.info('pages stack size = ' + size);
```

#### router.getState(deprecated)

getState(): RouterState

获取栈顶页面的状态信息。

从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[getState](Class (Router).md#ZH-CN_TOPIC_0000002497604782__getstate)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明[RouterState](#ZH-CN_TOPIC_0000002529444757__routerstate)页面状态信息。

**示例：**

```ets
let page = this.getUIContext().getRouter().getState();
console.info('current index = ' + page.index);
console.info('current name = ' + page.name);
console.info('current path = ' + page.path);
```

#### router.getStateByIndex(deprecated)

getStateByIndex(index: number): RouterState | undefined

通过索引值获取对应页面的状态信息。

从API version 12开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[getStateByIndex](Class (Router).md#ZH-CN_TOPIC_0000002497604782__getstatebyindex12)。

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是表示要获取的页面索引。从栈底到栈顶，index从1开始递增。

**返回值：**

类型说明[RouterState](#ZH-CN_TOPIC_0000002529444757__routerstate) | undefined返回页面状态信息。索引不存在时返回undefined。

**示例：**

```ets
let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info(`params = ${JSON.stringify(options.params)}`);
}
```

#### router.getStateByUrl(deprecated)

getStateByUrl(url: string): Array<RouterState>

通过url获取对应页面的状态信息。

从API version 12开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[getStateByUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__getstatebyurl12)。

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明urlstring是表示要获取对应页面信息的url。

**返回值：**

类型说明Array<[RouterState](#ZH-CN_TOPIC_0000002529444757__routerstate)>页面状态信息。

**示例：**

```ets
let options: Array<router.RouterState> = router.getStateByUrl('pages/index');
for (let i: number = 0; i < options.length; i++) {
  console.info('index = ' + options[i].index);
  console.info('name = ' + options[i].name);
  console.info('path = ' + options[i].path);
  console.info('params = ' + options[i].params);
}
```

#### RouterState

页面状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

名称类型只读可选说明indexnumber否否

表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

namestring否否

表示当前页面的名称，即对应文件名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

pathstring否否

表示当前页面的路径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

params12+Object否否

表示当前页面携带的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### router.showAlertBeforeBackPage(deprecated)

showAlertBeforeBackPage(options: EnableAlertOptions): void

开启页面返回询问对话框。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[showAlertBeforeBackPage](Class (Router).md#ZH-CN_TOPIC_0000002497604782__showalertbeforebackpage)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[EnableAlertOptions](#ZH-CN_TOPIC_0000002529444757__enablealertoptions)是文本弹窗信息描述。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed.100001Internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  this.getUIContext().getRouter().showAlertBeforeBackPage({
    message: 'Message Info'
  });
} catch (err) {
  console.error(`showAlertBeforeBackPage failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
}
```

#### EnableAlertOptions

页面返回询问对话框选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

名称类型只读可选说明messagestring否否询问对话框内容。

#### router.hideAlertBeforeBackPage(deprecated)

hideAlertBeforeBackPage(): void

禁用页面返回询问对话框。

从API version 9开始支持，从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[hideAlertBeforeBackPage](Class (Router).md#ZH-CN_TOPIC_0000002497604782__hidealertbeforebackpage)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
this.getUIContext().getRouter().hideAlertBeforeBackPage();
```

#### router.getParams(deprecated)

getParams(): Object

获取发起跳转的页面往当前页传入的参数。

从API version 18开始废弃，建议使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取[Router](Class (Router).md)实例，再通过此实例调用替代方法[getParams](Class (Router).md#ZH-CN_TOPIC_0000002497604782__getparams)。

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)方法获取当前UI上下文关联的[Router](Class (Router).md)对象。

getParams只获取当前页面的参数，并不会清除页面关联的参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Object发起跳转的页面往当前页传入的参数。

**示例：**

```ets
this.getUIContext().getRouter().getParams();
```

#### RouterOptions

路由跳转选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite。

名称类型只读可选说明urlstring否否

表示目标页面的url，可以用以下两种格式：

- 页面绝对路径，由配置文件中pages列表提供，例如：

- pages/index/index

- pages/detail/detail

- 特殊值，如果url的值是"/"，则跳转到首页，首页默认为页面跳转配置项src数组的第一个数据项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

paramsObject否是

表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。

**说明：**

params参数只能传递可序列化的参数，不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造object类型对象进行传递。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

recoverable14+boolean否是

表示对应的页面是否可恢复，默认为true。当为true时，表示可恢复，当为false时，表示不可恢复。

**说明：**

当应用退到后台，并且在未来的某个时间点，由于系统资源限制等原因被系统杀死，如果某个页面被设置成可恢复，那么该应用再次被拉到前台后系统可以恢复出页面，详细说明请参考[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)。

页面路由栈支持的最大Page数量为32。

#### RouterMode9+

路由跳转模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

名称值说明Standard0

多实例模式，也是默认情况下的跳转模式。

目标页面会被添加到页面栈顶，无论栈中是否存在相同url的页面。

**说明：**

不使用路由跳转模式时，则按照默认的多实例模式进行跳转。

Single1

单实例模式。

如果目标页面的url已经存在于页面栈中，则该url页面移动到栈顶。

如果目标页面的url在页面栈中不存在同url页面，则按照默认的多实例模式进行跳转。

#### NamedRouterOptions10+

命名路由跳转选项。

名称类型只读可选说明namestring否否

表示目标命名路由页面的name。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

paramsObject否是

表示路由跳转时要同时传递到目标页面的数据。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。

**说明：**

params参数不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造object类型对象进行传递。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

recoverable14+boolean否是

表示对应的页面是否可恢复，默认为true。当为true时，表示可恢复，当为false时，表示不可恢复。

**说明：**

当应用退到后台，并且在未来的某个时间点，由于系统资源限制等原因被系统杀死，如果某个页面被设置成可恢复，那么该应用再次被拉到前台后系统可以恢复出页面，详细说明请参考[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

#### 完整示例

#### 基于JS扩展的类Web开发范式

以下代码仅适用于javascript文件，不适用于ArkTS文件

```ets
// 在当前页面中
export default {
  pushPage() {
    router.pushUrl({
      url: 'pages/detail/detail',
      params: {
        data1: 'message'
      }
    });
  }
}
```

```ets
// 在detail页面中
export default {
  onInit() {
    console.info('showData1:' + this.getUIContext().getRouter().getParams()['data1']);
  }
}
```

#### 基于TS扩展的声明式开发范式

直接使用router可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext获取[UIContext](zh-cn_topic_0000002529444749.html)实例，并使用[getRouter](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getrouter)获取绑定实例的router。

```ets
// 通过router.pushUrl跳转至目标页携带params参数
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义传递参数的类
class innerParams {
  array: number[];

  constructor(tuple: number[]) {
    this.array = tuple;
  }
}

class RouterParams {
  text: string;
  data: innerParams;

  constructor(str: string, tuple: number[]) {
    this.text = str;
    this.data = new innerParams(tuple);
  }
}

@Entry
@Component
struct Index {
  async routePage() {
    let options: router.RouterOptions = {
      url: 'pages/second',
      params: new RouterParams('这是第一页的值', [12, 45, 78])
    }
    // 建议使用this.getUIContext().getRouter().pushUrl()
    this.getUIContext().getRouter().pushUrl(options)
      .then(() => {
        console.error(`pushUrl finish`);
      })
      .catch((err: ESObject) => {
        console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
      })
    }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('这是第一页')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

```ets
// 在second页面中接收传递过来的参数
import { router } from '@kit.ArkUI';

class innerParams {
  array: number[];

  constructor(tuple: number[]) {
    this.array = tuple;
  }
}

class RouterParams {
  text: string;
  data: innerParams;

  constructor(str: string, tuple: number[]) {
    this.text = str;
    this.data = new innerParams(tuple);
  }
}

@Entry
@Component
struct Second {
  private content: string = "这是第二页";
  // 建议使用this.getUIContext().getRouter().getParams()
  @State text: string = (this.getUIContext().getRouter().getParams() as RouterParams).text;
  @State data: object = (this.getUIContext().getRouter().getParams() as RouterParams).data;
  @State secondData: string = '';

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text(`${this.content}`)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
      Text(this.text)
        .fontSize(30)
        .onClick(() => {
          this.secondData = (this.data['array'][1]).toString();
        })
        .margin({ top: 20 })
      Text(`第一页传来的数值:${this.secondData}`)
        .fontSize(20)
        .margin({ top: 20 })
        .backgroundColor('red')
    }
    .width('100%')
    .height('100%')
  }
}
```

#### router.push(deprecated)

push(options: RouterOptions): void

跳转到应用内的指定页面。

从API version 8开始支持，从API version 9开始废弃，建议使用[pushUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__pushurl)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是跳转页面描述信息。

**示例：**

```ets
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.push({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
});
```

#### router.replace(deprecated)

replace(options: RouterOptions): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

从API version 8开始支持，从API version 9开始废弃，建议使用[replaceUrl](Class (Router).md#ZH-CN_TOPIC_0000002497604782__replaceurl)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

参数名类型必填说明options[RouterOptions](#ZH-CN_TOPIC_0000002529444757__routeroptions)是替换页面描述信息。

**示例：**

```ets
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replace({
  url: 'pages/detail',
  params: new RouterParams('message')
});
```

#### router.enableAlertBeforeBackPage(deprecated)

enableAlertBeforeBackPage(options: EnableAlertOptions): void

开启页面返回询问对话框。

从API version 8开始支持，从API version 9开始废弃，建议使用[showAlertBeforeBackPage](Class (Router).md#ZH-CN_TOPIC_0000002497604782__showalertbeforebackpage)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[EnableAlertOptions](#ZH-CN_TOPIC_0000002529444757__enablealertoptions)是文本弹窗信息描述。

**示例：**

```ets
router.enableAlertBeforeBackPage({
  message: 'Message Info'
});
```

#### router.disableAlertBeforeBackPage(deprecated)

disableAlertBeforeBackPage(): void

禁用页面返回询问对话框。

从API version 8开始支持，从API version 9开始废弃，建议使用[hideAlertBeforeBackPage](Class (Router).md#ZH-CN_TOPIC_0000002497604782__hidealertbeforebackpage)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
router.disableAlertBeforeBackPage();
```