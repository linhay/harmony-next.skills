# commonEventSubscriber

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### CommonEventSubscriber

表示公共事件的订阅者。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

#### 使用说明

在使用CommonEventSubscriber的功能前，需要通过commonEventManager.createSubscriber获取subscriber对象。

```ets
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
let subscriber: commonEventManager.CommonEventSubscriber;
// 订阅者信息
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    events: ['event']
};
// 创建订阅者
subscriber = commonEventManager.createSubscriberSync(subscribeInfo);
```

#### getCode

getCode(callback: AsyncCallback<number>): void

获取有序公共事件传递的数据（number类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。返回有序公共事件传递的数据（number类型）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.getCode((err: BusinessError, code: number) => {
  if (err) {
    console.error(`Failed to get code. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
});
```

#### getCode

getCode(): Promise<number>

获取有序公共事件传递的数据（number类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<number>Promise对象。返回有序公共事件传递的数据（number类型）。

**示例：**

```ets
subscriber.getCode().then((code: number) => {
  console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get code. Code is ${err.code}, message is ${err.message}`);
});
```

#### getCodeSync10+

getCodeSync(): number

获取有序公共事件传递的数据（number类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明number表示有序公共事件传递的数据（number类型）。

**示例：**

```ets
let code: number = subscriber.getCodeSync();
console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
```

#### setCode

setCode(code: number, callback: AsyncCallback<void>): void

设置有序公共事件传递的数据（number类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明codenumber是有序公共事件传递的数据（number类型）。callbackAsyncCallback<void>是回调函数。当设置有序公共事件传递的数据（number类型）成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.setCode(1, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting code.`);
});
```

#### setCode

setCode(code: number): Promise<void>

设置有序公共事件传递的数据（number类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明codenumber是有序公共事件传递的数据（number类型）。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.setCode(1).then(() => {
  console.info(`Succeeded in setting code.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
});
```

#### setCodeSync10+

setCodeSync(code: number): void

设置有序公共事件传递的数据（number类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明codenumber是有序公共事件传递的数据（number类型）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
try {
  subscriber.setCodeSync(1);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
}
```

#### getData

getData(callback: AsyncCallback<string>): void

获取有序公共事件传递的数据（string类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是回调函数。返回有序公共事件传递的数据（string类型）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
// 获取有序公共事件传递的数据（string类型）回调
subscriber.getData((err: BusinessError, data: string) => {
  if (err) {
    console.error(`Failed to get data. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting data, data is ${JSON.stringify(data)}`);
});
```

#### getData

getData(): Promise<string>

获取有序公共事件传递的数据（string类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<string>Promise对象。返回有序公共事件传递的数据（string类型）。

**示例：**

```ets
subscriber.getData().then((data: string) => {
  console.info(`Succeeded in getting data, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get data. Code is ${err.code}, message is ${err.message}`);
});
```

#### getDataSync10+

getDataSync(): string

获取有序公共事件传递的数据（string类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明string有序公共事件传递的数据（string类型）。

**示例：**

```ets
let data: string = subscriber.getDataSync();
console.info(`Succeeded in getting data, data is ${data}`);
```

#### setData

setData(data: string, callback: AsyncCallback<void>): void

设置有序公共事件传递的数据（string类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明datastring是有序公共事件传递的数据（string类型）。callbackAsyncCallback<void>是回调函数。当设置有序公共事件传递的数据（string类型）成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.setData('publish_data_changed', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting data.`);
});
```

#### setData

setData(data: string): Promise<void>

设置有序公共事件传递的数据（string类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明datastring是有序公共事件传递的数据（string类型）。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.setData('publish_data_changed').then(() => {
  console.info(`Succeeded in setting data.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
});
```

#### setDataSync10+

setDataSync(data: string): void

设置有序公共事件传递的数据（string类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明datastring是有序公共事件传递的数据（string类型）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
try {
  subscriber.setDataSync('publish_data_changed');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
}
```

#### setCodeAndData

setCodeAndData(code: number, data: string, callback:AsyncCallback<void>): void

设置有序公共事件数据。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明codenumber是有序公共事件传递的数据（number类型）。datastring是有序公共事件传递的数据（string类型）。callbackAsyncCallback<void>是回调函数。当设置有序公共事件传递的数据成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.setCodeAndData(1, 'publish_data_changed', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting code and data.`);
});
```

#### setCodeAndData

setCodeAndData(code: number, data: string): Promise<void>

设置有序公共事件传递的数据。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明codenumber是有序公共事件传递的数据（number类型）。datastring是有序公共事件传递的数据（string类型）。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.setCodeAndData(1, 'publish_data_changed').then(() => {
  console.info(`Succeeded in setting code and data.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
});
```

#### setCodeAndDataSync10+

setCodeAndDataSync(code: number, data: string): void

设置有序公共事件传递的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明codenumber是有序公共事件传递的数据（number类型）。datastring是有序公共事件传递的数据（string类型）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
try {
  subscriber.setCodeAndDataSync(1, 'publish_data_changed');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
}
```

#### isOrderedCommonEvent

isOrderedCommonEvent(callback: AsyncCallback<boolean>): void

查询当前公共事件是否为有序公共事件。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示有序公共事件；返回false表示无序公共事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.isOrderedCommonEvent((err: BusinessError, isOrdered:boolean) => {
  if (err) {
    console.error(`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`isOrderedCommonEvent ${JSON.stringify(isOrdered)}`);
});
```

#### isOrderedCommonEvent

isOrderedCommonEvent(): Promise<boolean>

查询当前公共事件是否为有序公共事件。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示有序公共事件；返回false表示无序公共事件。

**示例：**

```ets
subscriber.isOrderedCommonEvent().then((isOrdered:boolean) => {
  console.info(`isOrderedCommonEvent ${JSON.stringify(isOrdered)}`);
}).catch((err: BusinessError) => {
  console.error(`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}`);
});
```

#### isOrderedCommonEventSync10+

isOrderedCommonEventSync(): boolean

查询当前公共事件是否为有序公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明boolean返回true表示有序公共事件；返回false表示无序公共事件。

**示例：**

```ets
let isOrdered: boolean = subscriber.isOrderedCommonEventSync();
console.info(`isOrderedCommonEventSync ${JSON.stringify(isOrdered)}`);
```

#### isStickyCommonEvent

isStickyCommonEvent(callback: AsyncCallback<boolean>): void

检查当前公共事件是否为一个粘性事件。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示是粘性公共事件；返回false表示不是粘性公共事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.isStickyCommonEvent((err: BusinessError, isSticky:boolean) => {
  if (err) {
    console.error(`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`isStickyCommonEvent ${JSON.stringify(isSticky)}`);
});
```

#### isStickyCommonEvent

isStickyCommonEvent(): Promise<boolean>

检查当前公共事件是否为一个粘性事件。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示是粘性公共事件；返回false表示不是粘性公共事件。

**示例：**

```ets
subscriber.isStickyCommonEvent().then((isSticky:boolean) => {
  console.info(`isStickyCommonEvent ${JSON.stringify(isSticky)}`);
}).catch((err: BusinessError) => {
  console.error(`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}`);
});
```

#### isStickyCommonEventSync10+

isStickyCommonEventSync(): boolean

检查当前公共事件是否为一个粘性事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明boolean返回true表示是粘性公共事件；返回false表示不是粘性公共事件。

**示例：**

```ets
let isSticky: boolean = subscriber.isStickyCommonEventSync();
console.info(`isStickyCommonEventSync ${JSON.stringify(isSticky)}`);
```

#### abortCommonEvent

abortCommonEvent(callback: AsyncCallback<void>): void

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](#ZH-CN_TOPIC_0000002529285505__finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当添加有序公共事件中止状态成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.abortCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to abort common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in aborting common event.`);
});
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in finishing common event.`);
});
```

#### abortCommonEvent

abortCommonEvent(): Promise<void>

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](#ZH-CN_TOPIC_0000002529285505__finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
subscriber.abortCommonEvent().then(() => {
  console.info(`Succeeded in aborting common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to abort common event. Code is ${err.code}, message is ${err.message}`);
});
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```

#### abortCommonEventSync10+

abortCommonEventSync(): void

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](#ZH-CN_TOPIC_0000002529285505__finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**系统能力：** SystemCapability.Notification.CommonEvent

**示例：**

```ets
subscriber.abortCommonEventSync();
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```

#### clearAbortCommonEvent

clearAbortCommonEvent(callback: AsyncCallback<void>): void

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](#ZH-CN_TOPIC_0000002529285505__finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当清理有序公共事件中止状态成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.clearAbortCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in clearing abort common event.`);
});
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in finishing common event.`);
});
```

#### clearAbortCommonEvent

clearAbortCommonEvent(): Promise<void>

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](#ZH-CN_TOPIC_0000002529285505__finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
subscriber.clearAbortCommonEvent().then(() => {
  console.info(`Succeeded in clearing abort common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}`);
});
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```

#### clearAbortCommonEventSync10+

clearAbortCommonEventSync(): void

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](#ZH-CN_TOPIC_0000002529285505__finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。

**系统能力：** SystemCapability.Notification.CommonEvent

**示例：**

```ets
subscriber.clearAbortCommonEventSync();
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```

#### getAbortCommonEvent

getAbortCommonEvent(callback: AsyncCallback<boolean>): void

获取当前有序公共事件是否处于中止状态。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.getAbortCommonEvent((err: BusinessError, abortEvent: boolean) => {
  if (err) {
    console.error(`Failed to get abort common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
});
```

#### getAbortCommonEvent

getAbortCommonEvent(): Promise<boolean>

获取当前有序公共事件是否处于中止状态。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。

**示例：**

```ets
subscriber.getAbortCommonEvent().then((abortEvent: boolean) => {
  console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get abort common event. Code is ${err.code}, message is ${err.message}`);
});
```

#### getAbortCommonEventSync10+

getAbortCommonEventSync(): boolean

获取当前有序公共事件是否处于中止状态。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明boolean返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。

**示例：**

```ets
let abortEvent: boolean = subscriber.getAbortCommonEventSync();
console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
```

#### getSubscribeInfo

getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void

获取订阅者的订阅信息。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<[CommonEventSubscribeInfo](CommonEventSubscribeInfo.md)>是回调函数。返回订阅者的订阅信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.getSubscribeInfo((err: BusinessError, subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
  if (err) {
    console.error(`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}`);
});
```

#### getSubscribeInfo

getSubscribeInfo(): Promise<CommonEventSubscribeInfo>

获取订阅者的订阅信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<[CommonEventSubscribeInfo](CommonEventSubscribeInfo.md)>Promise对象。返回订阅者的订阅信息。

**示例：**

```ets
subscriber.getSubscribeInfo().then((subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
  console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}`);
});
```

#### getSubscribeInfoSync10+

getSubscribeInfoSync(): CommonEventSubscribeInfo

获取订阅者的订阅信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明[CommonEventSubscribeInfo](CommonEventSubscribeInfo.md)表示订阅者的订阅信息。

**示例：**

```ets
let subscribeInfo = subscriber.getSubscribeInfoSync();
console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}`);
```

#### finishCommonEvent9+

finishCommonEvent(callback: AsyncCallback<void>): void

用于订阅者结束对当前有序公共事件的处理。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当订阅者结束当前有序公共事件成功时，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**示例：**

```ets
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in finishing common event.`);
});
```

#### finishCommonEvent9+

finishCommonEvent(): Promise<void>

用于订阅者结束对当前有序公共事件的处理。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
subscriber.finishCommonEvent().then(() => {
  console.info(`Succeeded in finishing common event.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
});
```