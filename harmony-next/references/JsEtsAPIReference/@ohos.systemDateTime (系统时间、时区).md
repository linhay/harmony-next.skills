# @ohos.systemDateTime (系统时间、时区)

本模块主要由系统时间和系统时区功能组成。开发者可以获取系统时间及系统时区。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { systemDateTime } from '@kit.BasicServicesKit';
```

#### TimeType10+

定义获取时间的枚举类型。

**系统能力**: SystemCapability.MiscServices.Time

名称值说明STARTUP0自系统启动以来经过的毫秒数，包括深度睡眠时间。ACTIVE1自系统启动以来经过的毫秒数，不包括深度睡眠时间。

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getTime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明isNanoboolean是

返回结果是否为纳秒数。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

callbackAsyncCallback<number>是回调函数，返回自Unix纪元以来经过的时间戳。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getTime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数，返回自Unix纪元以来经过的时间戳(ms)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano?: boolean): Promise<number>

获取自Unix纪元以来经过的时间，使用Promise异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getTime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明isNanoboolean否

返回结果是否为纳秒数,默认值为false。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

**返回值：**

类型说明Promise<number>Promise对象，返回自Unix纪元以来经过的时间戳。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime().then((time: number) => {
    console.info(`Succeeded in getting currentTime : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明isNanoboolean是

返回结果是否为纳秒数。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

callbackAsyncCallback<number>是回调函数，返回自系统启动以来经过的时间，但不包括深度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数，返回自系统启动以来经过的时间，但不包括度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明isNanoboolean否

返回结果是否为纳秒数,默认值为false。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

**返回值：**

类型说明Promise<number>Promise对象，返回自系统启动以来经过的时间，但不包括深度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealTime(deprecated)

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明isNanoboolean是

返回结果是否为纳秒数。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

callbackAsyncCallback<number>是回调函数，返回自系统启动以来经过的时间，包括深度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealTime(deprecated)

getRealTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数，返回自系统启动以来经过的时间，包括深度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getRealTime(deprecated)

getRealTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，包括深度睡眠时间，使用Promise异步回调。

从API version 9开始支持，从API Version 12开始废弃，建议使用[systemDateTime.getUptime10+](#ZH-CN_TOPIC_0000002529445483__systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明isNanoboolean否

返回结果是否为纳秒数,默认值为false。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

**返回值：**

类型说明Promise<number>Promise对象，返回自系统启动以来经过的时间，包括深度睡眠时间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime().then((time: number) => {
    console.info(`Succeeded in getting real time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTime10+

getTime(isNanoseconds?: boolean): number

使用同步方式获取自Unix纪元以来到当前系统时间所经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明isNanosecondsboolean否

返回结果是否为纳秒数。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

默认值为false。

**返回值：**

类型说明number自Unix纪元以来到当前系统时间所经过的时间。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getTime(true)
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get time. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getUptime10+

getUptime(timeType: TimeType, isNanoseconds?: boolean): number

使用同步方式获取自系统启动以来经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明timeType[TimeType](#ZH-CN_TOPIC_0000002529445483__timetype10)是获取时间的类型，仅能为STARTUP或者ACTIVE。isNanosecondsboolean否

返回结果是否为纳秒数。

- true：表示返回结果为纳秒数(ns)。

- false：表示返回结果为毫秒数(ms)。

默认值为false。

**返回值：**

类型说明number自系统启动以来经过的时间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401

Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification

 failed.This error code was added due to missing issues.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getUptime(systemDateTime.TimeType.ACTIVE, false);
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get uptime. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getDate(deprecated)

getDate(callback: AsyncCallback<Date>): void

获取当前系统日期，使用callback异步回调。

从API version 9开始支持，从API version 10开始废弃，建议使用[new Date()](https://gitcode.com/HarmonyOS/docs/blob/weekly_20251117/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明callbackAsyncCallback<Date>是回调函数，返回当前系统日期。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.System error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in getting date : ${date}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getDate(deprecated)

getDate(): Promise<Date>

获取当前系统日期，使用Promise异步回调。

从API version 9开始支持，从API version 10开始废弃，建议使用[new Date()](https://gitcode.com/HarmonyOS/docs/blob/weekly_20251117/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

类型说明Promise<Date>Promise对象，返回当前系统日期。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.System error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate().then((date: Date) => {
    console.info(`Succeeded in getting date : ${date}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get date. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTimezone

getTimezone(callback: AsyncCallback<string>): void

获取系统时区，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是回调函数，返回系统时区。具体可见[支持的系统时区](#ZH-CN_TOPIC_0000002529445483__支持的系统时区)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone((error: BusinessError, data: string) => {
    if (error) {
      console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
      return;
    }
    console.info(`Succeeded in get timezone : ${data}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTimezone

getTimezone(): Promise<string>

获取系统时区，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

类型说明Promise<string>Promise对象，返回系统时区。具体可见[支持的系统时区](#ZH-CN_TOPIC_0000002529445483__支持的系统时区)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone().then((data: string) => {
    console.info(`Succeeded in getting timezone: ${data}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### systemDateTime.getTimezoneSync10+

getTimezoneSync(): string

获取系统时区，使用同步方式。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

类型说明string返回系统时区。具体可见[支持的系统时区](#ZH-CN_TOPIC_0000002529445483__支持的系统时区)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timezone: string = systemDateTime.getTimezoneSync();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```

#### 支持的系统时区

支持的系统时区及各时区与0时区相比的偏移量(单位：h)可见下表。

时区偏移量Antarctica/McMurdo12America/Argentina/Buenos_Aires-3Australia/Sydney10America/Noronha-2America/St_Johns-3Africa/Kinshasa1America/Santiago-3Asia/Shanghai8Asia/Nicosia3Europe/Berlin2America/Guayaquil-5Europe/Madrid2Pacific/Pohnpei11America/Godthab-2Asia/Jakarta7Pacific/Tarawa12Asia/Almaty6Pacific/Majuro12Asia/Ulaanbaatar8America/Mexico_City-5Asia/Kuala_Lumpur8Pacific/Auckland12Pacific/Tahiti-10Pacific/Port_Moresby10Asia/Gaza3Europe/Lisbon1Europe/Moscow3Europe/Kiev3Pacific/Wake12America/New_York-4Asia/Tashkent5

#### systemDateTime.getAutoTimeStatus21+

getAutoTimeStatus(): boolean

获取自动设置时间开关状态，使用同步方式。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

类型说明boolean

返回自动设置时间开关状态。

- true：表示自动设置时间开关状态为打开。

- false：表示自动设置时间开关状态为关闭。

**错误码：**

以下错误码的详细介绍请参见[时间时区错误码](时间时区服务错误码.md)和[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息13000001Network connection error or OS error. Possible causes: 1.System memory is insufficient; 2.Calls the underlying system interface failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let status: boolean = systemDateTime.getAutoTimeStatus();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get autotime status. message: ${error.message}, code: ${error.code}`);
}
```