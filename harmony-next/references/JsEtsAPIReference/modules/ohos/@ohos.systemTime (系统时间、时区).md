# @ohos.systemTime (系统时间、时区)

本模块主要由系统时间和系统时区功能组成。开发者可以设置、获取系统时间及系统时区。

- 从API Version 9 开始，该模块接口不再维护，推荐使用新模块接口[@ohos.systemDateTime (系统时间、时区)](@ohos.systemDateTime (系统时间、时区).md)。
- 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { systemTime } from '@kit.BasicServicesKit';
```

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。 - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
callbackAsyncCallback<number>是回调函数，返回自Unix纪元以来经过的时间。

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime: ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(isNano?: boolean): Promise<number>

获取自Unix纪元以来经过的时间，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。 默认值为false。 - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自Unix纪元以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime().then((time: number) => {
    console.info(`Succeeded in getting currentTime : ${time}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。 - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
callbackAsyncCallback<number>是回调函数，返回自系统启动以来经过的时间，不包括深度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。 - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealTime8+(deprecated)

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。 - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
callbackAsyncCallback<number>是回调函数，返回自系统启动以来经过的时间，包括深度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealTime8+(deprecated)

getRealTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getRealTime8+(deprecated)

getRealTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，包括深度睡眠时间，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。 默认值为false。 - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime().then((time: number) => {
    console.info(`Succeeded in getting real time : ${time}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getDate8+(deprecated)

getDate(callback: AsyncCallback<Date>): void

获取当前系统日期，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Date> | 是 | 回调函数，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting date : ${date}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getDate8+(deprecated)

getDate(): Promise<Date>

获取当前系统日期，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Date> | Promise对象，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate().then((date: Date) => {
    console.info(`Succeeded in getting date : ${date}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getTimezone8+(deprecated)

getTimezone(callback: AsyncCallback<string>): void

获取系统时区，使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTimezone](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegettimezone)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回系统时区。具体可见支持的系统时区 。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone((error: BusinessError, data: string) => {
    if (error) {
      console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting timezone : ${data}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.getTimezone8+(deprecated)

getTimezone(): Promise<string>

获取系统时区，使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTimezone](@ohos.systemDateTime (系统时间、时区).md#ZH-CN_TOPIC_0000002553361527__systemdatetimegettimezone-1)替代。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回系统时区。具体可见支持的系统时区 。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone().then((data: string) => {
    console.info(`Succeeded in getting timezone: ${data}`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTime(deprecated)

setTime(time : number, callback : AsyncCallback<void>) : void

设置系统时间，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 目标时间戳（ms）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25
let time = 1611081385000;
try {
  systemTime.setTime(time, (error: BusinessError) => {
    if (error) {
      console.info(`Failed to setting time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting time`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTime(deprecated)

setTime(time : number) : Promise<void>

设置系统时间，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 目标时间戳（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// time对应的时间为2021-01-20 02:36:25
let time = 1611081385000;
try {
  systemTime.setTime(time).then(() => {
    console.info(`Succeeded in setting time.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to setting time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setDate(deprecated)

setDate(date: Date, callback: AsyncCallback<void>): void

设置系统日期，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date | 是 | 目标日期。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let date = new Date();
try {
  systemTime.setDate(date, (error: BusinessError) => {
    if (error) {
      console.info(`Failed to setting date. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting date.`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setDate(deprecated)

setDate(date: Date): Promise<void>

设置系统日期，使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date | 是 | 目标日期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let date = new Date();
try {
  systemTime.setDate(date).then(() => {
    console.info(`Succeeded in setting date.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to setting date. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTimezone(deprecated)

setTimezone(timezone: string, callback: AsyncCallback<void>): void

设置系统时区，使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET_TIME_ZONE

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timezone | string | 是 | 系统时区。具体可见支持的系统时区 。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai', (error: BusinessError) => {
    if (error) {
      console.info(`Failed to setting timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in setting timezone.`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemTime.setTimezone(deprecated)

setTimezone(timezone: string): Promise<void>

使用Promise异步回调设置系统时区。


从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET_TIME_ZONE

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timezone | string | 是 | 系统时区。具体可见支持的系统时区 。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](时间时区服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai').then(() => {
    console.info(`Succeeded in setting timezone.`);
  }).catch((error: BusinessError) => {
    console.info(`Failed to setting timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### 支持的系统时区

支持的系统时区及各时区与0时区相比的偏移量（单位：h）可见下表。

| 时区 | 偏移量 |
| --- | --- |
| Antarctica/McMurdo | 12 |
| America/Argentina/Buenos_Aires | -3 |
| Australia/Sydney | 10 |
| America/Noronha | -2 |
| America/St_Johns | -3 |
| Africa/Kinshasa | 1 |
| America/Santiago | -3 |
| Asia/Shanghai | 8 |
| Asia/Nicosia | 3 |
| Europe/Berlin | 2 |
| America/Guayaquil | -5 |
| Europe/Madrid | 2 |
| Pacific/Pohnpei | 11 |
| America/Godthab | -2 |
| Asia/Jakarta | 7 |
| Pacific/Tarawa | 12 |
| Asia/Almaty | 6 |
| Pacific/Majuro | 12 |
| Asia/Ulaanbaatar | 8 |
| America/Mexico_City | -5 |
| Asia/Kuala_Lumpur | 8 |
| Pacific/Auckland | 12 |
| Pacific/Tahiti | -10 |
| Pacific/Port_Moresby | 10 |
| Asia/Gaza | 3 |
| Europe/Lisbon | 1 |
| Europe/Moscow | 3 |
| Europe/Kiev | 3 |
| Pacific/Wake | 12 |
| America/New_York | -4 |
| Asia/Tashkent | 5 |