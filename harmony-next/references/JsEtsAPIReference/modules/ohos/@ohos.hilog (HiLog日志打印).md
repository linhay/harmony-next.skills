# @ohos.hilog (HiLog日志打印)

hilog日志系统，使应用/服务可以按照指定级别、标识和格式字符串输出日志内容，帮助开发者了解应用/服务的运行状态，更好地调试程序。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
```

#### hilog.isLoggable

isLoggable(domain: number, tag: string, level: LogLevel) : boolean

在打印日志前调用该接口，用于检查指定领域标识、日志标识和级别的日志是否可以打印。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。 建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| level | LogLevel | 是 | 日志级别。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果返回true，则该领域标识、日志标识和级别的日志可以打印，否则不能打印。 |

**示例：**

```ets
hilog.isLoggable(0x0001, "testTag", hilog.LogLevel.INFO);
```

#### LogLevel

日志级别。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEBUG | 3 | 详细的流程记录，通过该级别的日志可以更详细地分析业务流程和定位分析问题。 |
| INFO | 4 | 用于记录业务关键流程节点，可以还原业务的主要运行过程； 用于记录可预料的非正常情况信息，如无网络信号、登录失败等。 这些日志都应该由该业务内处于支配地位的模块来记录，避免在多个被调用的模块或低级函数中重复记录。 |
| WARN | 5 | 用于记录较为严重的非预期情况，但是对用户影响不大，应用可以自动恢复或通过简单的操作就可以恢复的问题。 |
| ERROR | 6 | 应用发生了错误，该错误会影响功能的正常运行或用户的正常使用，可以恢复但恢复代价较高，如重置数据等。 |
| FATAL | 7 | 重大致命异常，表明应用即将崩溃，故障无法恢复。 |

#### hilog.debug

debug(domain: number, tag: string, format: string, ...args: any[]) : void

打印DEBUG级别的日志。

DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。 建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。 隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。 |
argsany[]否与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。

**示例：**

输出一条DEBUG信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```ets
hilog.debug(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```ets
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  D     hello World <private>
```

#### hilog.info

info(domain: number, tag: string, format: string, ...args: any[]) : void

打印INFO级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。 建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。 隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。 |
argsany[]否与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。

**示例：**

输出一条INFO信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```ets
hilog.info(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```ets
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     hello World <private>
```

#### hilog.warn

warn(domain: number, tag: string, format: string, ...args: any[]) : void

打印WARN级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。 建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。 隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。 |
argsany[]否与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。

**示例：**

输出一条WARN信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```ets
hilog.warn(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```ets
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  W     hello World <private>
```

#### hilog.error

error(domain: number, tag: string, format: string, ...args: any[]) : void

打印ERROR级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。 建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。 tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。 隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。 |
argsany[]否与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。

**示例：**

输出一条ERROR信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```ets
hilog.error(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```ets
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  E     hello World <private>
```

#### hilog.fatal

fatal(domain: number, tag: string, format: string, ...args: any[]) : void

打印FATAL级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。 建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。 隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。 |
argsany[]否与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。

**示例：**

输出一条FATAL信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```ets
hilog.fatal(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```ets
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  F     hello World <private>
```

#### hilog.setMinLogLevel15+

setMinLogLevel(level: LogLevel): void

设置应用日志打印的最低日志级别，用于拦截低级别日志打印。

如果设置的日志级别低于[全局日志级别](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog#查看和设置日志级别)，设置不生效。

debug版本应用下，此函数不生效。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | LogLevel | 是 | 日志级别。 |

**示例：**

以全局日志级别为INFO下，打印5条不同级别的hilog日志，在打印过程中调用两次setMinLogLevel接口为例：

```ets
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 1);
hilog.setMinLogLevel(hilog.LogLevel.WARN);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 2);
hilog.error(0x0001, 'testTag', 'this is an error level log, id: %{public}d', 3);
hilog.setMinLogLevel(hilog.LogLevel.DEBUG);
hilog.debug(0x0001, "testTag", 'this is a debug level log, id: %{public}d', 4);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 5);
```

由于全局日志起始为INFO，第一条日志可以正常打印。

在设置进程最低可打印日志级别为WARN后，第二条日志不符合该日志级别，第二条日志打印失败，第三条日志可以正常打印。

在设置进程最低日志级别为DEBUG后，但是此时全局日志级别为INFO，所以第四条日志不满足全局日志级别，打印失败，第五条日志可以打印。

最终打印结果如下所示：

```ets
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 1
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  E     this is an error level log, id: 3
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 5
```

#### hilog.setLogLevel21+

setLogLevel(level: LogLevel, prefer: PreferStrategy): void

设置当前应用程序进程的最低日志级别。

可通过prefer参数配置不同的偏好策略。如果选择策略PREFER_CLOSE_LOG，等同于调用setMinLogLevel函数。

debug版本应用下，此函数不生效。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | LogLevel | 是 | 日志级别。 |
| prefer | PreferStrategy | 是 | 偏好策略。 |

#### PreferStrategy21+

偏好策略。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET_LOGLEVEL | 0 | 清除设置, 实际生效的最低日志级别是系统控制的最低级别。 |
| PREFER_CLOSE_LOG | 1 | 实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较大值。 |
| PREFER_OPEN_LOG | 2 | 实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较小值。 |

**示例：**

以全局日志级别为INFO下，打印5条不同级别的hilog日志，在打印过程中调用两次setLogLevel接口为例：

```ets
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 1);
hilog.setLogLevel(hilog.LogLevel.WARN, hilog.PreferStrategy.PREFER_OPEN_LOG);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 2);
hilog.error(0x0001, 'testTag', 'this is an error level log, id: %{public}d', 3);
hilog.setLogLevel(hilog.LogLevel.DEBUG, hilog.PreferStrategy.PREFER_CLOSE_LOG);
hilog.debug(0x0001, "testTag", 'this is a debug level log, id: %{public}d', 4);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 5);
```

由于全局日志起始为INFO，第一条日志可以正常打印。

在设置进程最低日志级别为WARN, 并选择策略PREFER_OPEN_LOG后，实际生效的最低日志级别是全局日志级别INFO，所以第二条和第三条日志均可正常打印。

在设置进程最低日志级别为DEBUG，并选择策略PREFER_CLOSE_LOG后（等同于hilog.setMinLogLevel(hilog.LogLevel.DEBUG)），但是此时全局日志级别为INFO，所以第四条日志不满足全局日志级别，打印失败，第五条日志可以打印。

最终打印结果如下所示：

```ets
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 1
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 2
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  E     this is an error level log, id: 3
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 5
```

#### 参数格式符

上述接口中，日志打印的格式化参数需按照如下格式打印：

%{[private flag]}specifier

| 隐私标识符（private flag） | 说明 |
| --- | --- |
| 无 | 缺省值默认为private，不打印明文参数。 |
| private | 隐私参数类型，不打印明文参数。 |
| public | 明文显示参数。 |

| 格式说明符（specifier） | 说明 | 示例 |
| --- | --- | --- |
| d/i | 支持打印number和bigint类型。 | 123 |
| s | 支持打印string undefined bool 和null类型。 | "123" |
| o/O | 支持打印object、undefined和null类型。 从API version 20开始，支持该能力。 | { 'name': "Jack", 'age': 22 } |

**示例：**

```ets
let testObj: Record<string, string | number> = {
    'name': "Jack",
    'age': 22
}
let isBol = true;
let bigNum = BigInt(1234567890123456789);
hilog.info(0x0001, "jsHilogTest", "print object: %{public}s", JSON.stringify(testObj));
hilog.info(0x0001, "jsHilogTest", "print object: %{public}o", testObj);
hilog.info(0x0001, "jsHilogTest", "private flag: %{private}s %s, print null: %{public}s", "hello", "world", null);
hilog.info(0x0001, "jsHilogTest", "print undefined: %{public}s", undefined);
hilog.info(0x0001, "jsHilogTest", "print number: %{public}d %{public}i", 123, 456);
hilog.info(0x0001, "jsHilogTest", "print bigNum: %{public}d %{public}i", bigNum, bigNum);
hilog.info(0x0001, "jsHilogTest", "print boolean: %{public}s", isBol);
```

**打印结果：**

```ets
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print object: {"name":"Jack","age":22}
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  private flag: <private> <private>, print null: null
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print undefined: undefined
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print number: 123 456
08-09 13:26:29.095  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print bigNum: 1234567890123456768 1234567890123456768
08-09 13:26:29.095  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print boolean: true
```