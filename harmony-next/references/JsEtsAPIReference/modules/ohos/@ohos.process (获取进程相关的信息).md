# @ohos.process (获取进程相关的信息)

获取进程相关的信息，提供进程管理的相关功能。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { process } from '@kit.ArkTS';
```

#### 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

名称类型只读可选说明uidnumber是否进程的用户标识。pidnumber是否当前进程的pid。tid8+number是否当前线程的tid。

#### EventListener

type EventListener = (evt: Object) => void

用户存储的事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明evtObject是用户事件。

#### process.isIsolatedProcess8+

isIsolatedProcess(): boolean

检查进程是否已被隔离。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回判断结果。如果进程被隔离则返回true，否则返回false。

**示例：**

```ets
let result = process.isIsolatedProcess();
```

#### process.is64Bit8+

is64Bit(): boolean

检查运行环境是否为64位。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明boolean返回判断结果。如果运行环境是64位则返回true，否则返回false。

**示例：**

```ets
let result = process.is64Bit();
```

#### process.getStartRealtime8+

getStartRealtime(): number

获取系统启动到进程启动的实时时间（以毫秒为单位，不包含系统休眠时间）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回经过的实时时间。单位：毫秒。

**示例：**

```ets
let realtime = process.getStartRealtime();
```

#### process.getPastCpuTime8+

getPastCpuTime(): number

获取进程启动到当前时间的CPU时间（以毫秒为单位）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number返回经过的CPU时间。单位：毫秒。

**示例：**

```ets
let result = process.getPastCpuTime();
```

#### process.abort

abort(): void

该方法会导致进程立即退出并生成一个核心文件，谨慎使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```ets
process.abort();
```

#### process.uptime

uptime(): number

获取当前系统已运行的时间（以秒为单位）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

类型说明number当前系统已运行的时间。单位：秒。

**示例：**

```ets
let time = process.uptime();
```

#### process.kill(deprecated)

kill(signal: number, pid: number): boolean

发送信号到指定进程，结束该进程。

从API version 7开始支持，从API version 9开始废弃，建议使用[kill9+](#ZH-CN_TOPIC_0000002497604752__kill9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明signalnumber是发送的信号。pidnumber是进程的id。

**返回值：**

类型说明boolean信号发送成功返回true，失败返回false。

**示例：**

```ets
let pres = process.pid;
let result = process.kill(28, pres);
```

#### process.exit(deprecated)

exit(code: number): void

终止程序。

请谨慎使用此接口。调用此接口后应用将退出。如果输入参数非0，可能会导致数据丢失或出现异常。

从API version 7开始支持，从API version 9开始废弃，建议使用[exit9+](#ZH-CN_TOPIC_0000002497604752__exit9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明codenumber是进程的退出码。

**示例：**

```ets
process.exit(0);
```

#### process.getUidForName(deprecated)

getUidForName(v: string): number

根据指定的用户名，从系统的用户数据库中获取该用户的uid。

从API version 8开始支持，从API version 9开始废弃，建议使用[getUidForName9+](#ZH-CN_TOPIC_0000002497604752__getuidforname9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明vstring是用户名。

**返回值：**

类型说明number返回用户uid。

**示例：**

```ets
let pres = process.getUidForName("tool");
```

#### process.getThreadPriority(deprecated)

getThreadPriority(v: number): number

根据指定的tid获取线程优先级。

从API version 8开始支持，从API version 9开始废弃，建议使用[getThreadPriority9+](#ZH-CN_TOPIC_0000002497604752__getthreadpriority9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明vnumber是指定的线程tid。

**返回值：**

类型说明number返回线程的优先级。优先级顺序取决于当前操作系统。

**示例：**

```ets
let tid = process.tid;
let pres = process.getThreadPriority(tid);
```

#### process.isAppUid(deprecated)

isAppUid(v: number): boolean

判断uid是否属于应用程序。

从API version 8开始支持，从API version 9开始废弃，建议使用[isAppUid9+](#ZH-CN_TOPIC_0000002497604752__isappuid9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明vnumber是应用程序的uid。

**返回值：**

类型说明boolean返回判断结果。如果是应用程序的uid则返回true，否则返回false。

**示例：**

```ets
let result = process.isAppUid(688);
```

#### process.getSystemConfig(deprecated)

getSystemConfig(name: number): number

获取系统配置信息。

从API version 8开始支持，从API version 9开始废弃，建议使用[getSystemConfig9+](#ZH-CN_TOPIC_0000002497604752__getsystemconfig9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namenumber是指定系统配置参数名。

**返回值：**

类型说明number返回系统配置信息。

**示例：**

```ets
let _SC_ARG_MAX = 0;
let pres = process.getSystemConfig(_SC_ARG_MAX);
```

#### process.getEnvironmentVar(deprecated)

getEnvironmentVar(name: string): string

获取环境变量名对应的值。

从API version 8开始支持，从API version 9开始废弃，建议使用[getEnvironmentVar9+](#ZH-CN_TOPIC_0000002497604752__getenvironmentvar9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是环境变量名。

**返回值：**

类型说明string返回环境变量名对应的值。

**示例：**

```ets
let pres = process.getEnvironmentVar("PATH");
```

#### ProcessManager9+

提供用于新增进程的抛异常接口。

构造ProcessManager对象。

#### isAppUid9+

isAppUid(v: number): boolean

判断uid是否属于当前应用程序。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明vnumber是应用程序的uid。可通过process.uid获取。

**返回值：**

类型说明boolean返回判断结果。如果是应用程序的uid则返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new process.ProcessManager();
// uid通过process.uid获取
let pres = process.uid;
let result = pro.isAppUid(pres);
console.info("result: " + result); // result: true
```

#### getUidForName9+

getUidForName(v: string): number

根据指定的用户名，从系统的用户数据库中获取该用户uid。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明vstring是用户名。

**返回值：**

类型说明number获取用户uid，如果用户不存在则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new process.ProcessManager();
let pres = pro.getUidForName("tool");
```

#### getThreadPriority9+

getThreadPriority(v: number): number

根据指定的tid获取线程优先级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明vnumber是指定的线程tid。

**返回值：**

类型说明number返回线程的优先级。优先级顺序取决于当前操作系统。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new process.ProcessManager();
let tid = process.tid;
let pres = pro.getThreadPriority(tid);
```

#### getSystemConfig9+

getSystemConfig(name: number): number

获取系统配置信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namenumber是指定系统配置参数名。

**返回值：**

类型说明number返回系统配置信息。如果配置不存在，返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new process.ProcessManager();
let _SC_ARG_MAX = 0;
let pres = pro.getSystemConfig(_SC_ARG_MAX);
```

#### getEnvironmentVar9+

getEnvironmentVar(name: string): string

获取环境变量对应的值。

获取环境变量对应的值。如果环境变量不存在，返回undefined。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明namestring是环境变量名。

**返回值：**

类型说明string返回环境变量名对应的值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new process.ProcessManager();
let pres = pro.getEnvironmentVar("PATH");
```

#### exit9+

exit(code: number): void

终止程序。

请谨慎使用此接口，此接口调用后应用会退出，如果入参非0会产生数据丢失或者异常情况。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明codenumber是进程的退出码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new process.ProcessManager();
pro.exit(0);
```

#### kill9+

kill(signal: number, pid: number): boolean

发送signal到指定的进程，结束指定进程（仅支持结束本进程）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

参数名类型必填说明signalnumber是发送特定的信号给目标进程。 取值范围：1 <= signal <= 64。pidnumber是进程的id。

**返回值：**

类型说明boolean信号是否发送成功。如果信号发送成功则返回true，否则返回false。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
let pro = new process.ProcessManager();
let pres = process.pid;
let result = pro.kill(28, pres);
```