# @ohos.secureElement (安全单元的通道管理)

本模块主要用于操作及管理安全单元（SecureElement，简称SE），电子设备上可能存在的安全单元有eSE（Embedded SE）和SIM卡。文档中出现的SE服务为SEService实例，参见[createService](#ZH-CN_TOPIC_0000002497605424__omapicreateservice12)。

对于文档中出现以下类型说明：

类型说明Reader此类的实例表示该设备支持的SE，如果支持eSE、SIM和SIM2，则返回3个实例。Session此类的实例表示在某个SE Reader实例上创建连接会话。Channel此类的实例表示在某个Session实例上创建通道，可能为基础通道或逻辑通道。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### **导入模块**

```ets
import { omapi } from '@kit.ConnectivityKit';
```

#### ServiceState

定义不同的SE服务状态值。

**系统能力：** SystemCapability.Communication.SecureElement

名称值说明DISCONNECTED0SE服务状态已断开。CONNECTED1SE服务状态已连接。

#### omapi.newSEService(deprecated)

newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService

建立一个可用于连接到系统中所有可用SE的新连接（服务）。连接过程较为耗时，所以此方法仅提供异步方式进行的。使用callback异步回调。

仅当指定的回调或者当[isConnected](#ZH-CN_TOPIC_0000002497605424__seserviceisconnected)方法返回true时，该返回SEService对象是可用的。

从 API version 10 开始支持，从 API version 12 开始废弃，建议使用[createService](#ZH-CN_TOPIC_0000002497605424__omapicreateservice12)替代。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**typestring是固定填'serviceState' 。callbackCallback<[ServiceState](#ZH-CN_TOPIC_0000002497605424__servicestate)>是返回SE服务状态的回调 。

**返回值：**

**类型****说明**SEServiceSE服务实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.

**示例：**

```ets
import { omapi } from '@kit.ConnectivityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

function secureElementDemo() {
    // 获取 service
    try {
        seService = omapi.newSEService("serviceState", (state) => {
        hilog.info(0x0000, 'testTag', 'se service state = %{public}s', JSON.stringify(state));
        });
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'newSEService error %{public}s', JSON.stringify(error));
    }
    if (seService == undefined || !seService.isConnected()) {
        hilog.error(0x0000, 'testTag', 'secure element service disconnected.');
        return;
    }
}
```

#### omapi.createService12+

createService(): Promise<SEService>;

建立一个可用于连接到系统中所有可用SE的新连接（服务）。连接过程较为耗时，所以此方法仅提供异步方式。使用Promise异步回调。

仅当[isConnected](#ZH-CN_TOPIC_0000002497605424__seserviceisconnected)方法返回true时，该返回SEService对象是可用的。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**Promise<[SEService](#ZH-CN_TOPIC_0000002497605424__seservice)>以Promise形式异步返回可用的SE服务实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { omapi } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

function secureElementDemo() {
    omapi.createService().then((data) => {
        seService = data;
        if (seService == undefined || !seService.isConnected()) {
            hilog.error(0x0000, 'testTag', 'seservice state disconnected');
            return;
        }
        hilog.info(0x0000, 'testTag', 'seservice state connected');
    }).catch((error : BusinessError)=> {
        hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
    });
}
```

#### omapi.on18+

on(type: 'stateChanged', callback: Callback<ServiceState>): void;

注册监听服务状态变化事件。

调用[omapi.newSEService](#ZH-CN_TOPIC_0000002497605424__omapinewseservicedeprecated)或[omapi.createService](#ZH-CN_TOPIC_0000002497605424__omapicreateservice12)创建服务成功后再用on接口注册回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**typestring是订阅监听的事件类型，固定填'stateChanged' 。callbackCallback<[ServiceState](#ZH-CN_TOPIC_0000002497605424__servicestate)>是返回SE服务状态的回调 。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

示例请参见[off](#ZH-CN_TOPIC_0000002497605424__omapioff18)接口的示例。

#### omapi.off18+

off(type: 'stateChanged', callback?: Callback<ServiceState>): void;

取消订阅服务状态更改事件。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**typestring是取消订阅监听的事件类型，固定填'stateChanged' 。callbackCallback<[ServiceState](#ZH-CN_TOPIC_0000002497605424__servicestate)>否返回SE服务状态的回调 。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { omapi } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService: omapi.SEService;
function seStateOnCb(data: omapi.ServiceState) {
    hilog.info(0x0000, 'testTag', 'omapi.on ServiceState: %{public}s', JSON.stringify(data));
}

function seStateOffCb(data: omapi.ServiceState) {
    hilog.info(0x0000, 'testTag', 'omapi.off ServiceState: %{public}s', JSON.stringify(data));

}

function secureElementDemo() {
    try{
        omapi.createService().then((data) => {
            seService = data;
            if (seService == undefined || !seService.isConnected()) {
                hilog.error(0x0000, 'testTag', 'seservice state disconnected');
                return;
            }
            hilog.info(0x0000, 'testTag', 'seservice state connected');
        }).catch((error : BusinessError)=> {
            hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
        });
        omapi.on('stateChanged', seStateOnCb);
    } catch (error) {
        if (error as BusinessError) {
            hilog.error(0x0000, 'testTag', 'omapi on error %{public}s', JSON.stringify(error));
        }
    }
    try{
        omapi.off('stateChanged', seStateOffCb);
    } catch (error) {
        if (error as BusinessError) {
            hilog.error(0x0000, 'testTag', 'omapi off error %{public}s', JSON.stringify(error));
        }
    }
}
```

#### SEService

SEService表示可用于连接到系统中所有可用SE的连接（服务），通过[createService](#ZH-CN_TOPIC_0000002497605424__omapicreateservice12)获取SEService实例。

#### SEService.getReaders

getReaders(): Reader[]

返回可用SE Reader的数组，包含该设备上支持的所有的安全单元。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**[Reader](#ZH-CN_TOPIC_0000002497605424__reader)[]返回可用Reader对象数组。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { omapi } from '@kit.ConnectivityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;
let seReaders : omapi.Reader[];

// 在使用seService之前，需要对seService进行初始化
function secureElementDemo() {
    // 获取readers
    try {
        seReaders = seService.getReaders();
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'getReaders error %{public}s', JSON.stringify(error));
    }
    if (seReaders == undefined || seReaders.length == 0) {
        hilog.error(0x0000, 'testTag', 'no valid reader found.');
        // 释放SeService资源
        seService.shutdown();
        return;
    }
}
```

#### SEService.isConnected

isConnected(): boolean

检查SE服务是否已连接。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**booleantrue: SE服务状态已连接，false: SE服务状态已断开。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { omapi } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

function secureElementDemo() {
    omapi.createService().then((data) => {
        seService = data;
        if (seService == undefined || !seService.isConnected()) {
            hilog.error(0x0000, 'testTag', 'seservice state disconnected');
            return;
        }
        hilog.info(0x0000, 'testTag', 'seservice state connected');
    }).catch((error : BusinessError)=> {
        hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
    });
}
```

#### SEService.shutdown

shutdown(): void

释放该Service分配的所有SE资源。此后[isConnected](#ZH-CN_TOPIC_0000002497605424__seserviceisconnected)将返回false。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { omapi } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

// 在使用seService之前，需要对seService进行初始化

try {
    seService.shutdown();
} catch (error) {
    hilog.error(0x0000, 'testTag', 'shutdown error %{public}s', JSON.stringify(error));
}
```

#### SEService.getVersion

getVersion(): string

返回此实现所基于的Open Mobile API规范的版本号。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**stringOMA版本号（例如，“3.3”表示Open Mobile API规范版本3.3）

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { omapi } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

// 在使用seService之前，需要对seService进行初始化

try {
    let version = seService.getVersion();
    hilog.error(0x0000, 'testTag', 'version %{public}s', JSON.stringify(version));
} catch (error) {
    hilog.error(0x0000, 'testTag', 'getVersion error %{public}s', JSON.stringify(error));
}
```

#### Reader

Reader的实例表示该设备支持的SE，如果支持eSE、SIM和SIM2，则返回3个实例。通过[SEService.getReaders](#ZH-CN_TOPIC_0000002497605424__seservicegetreaders)获取Reader实例。

#### Reader.getName

getName(): string

返回此Reader的名称。如果此读卡器是SIM Reader，则其名称必须为“SIM”。如果此读卡器是SIM2 Reader，则其名称必须为“SIM2”。如果读卡器是eSE，则其名称须为“eSE”。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**string[Reader](#ZH-CN_TOPIC_0000002497605424__reader)名称。

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](../../errors/NFC错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seReaders : omapi.Reader[];

// 在使用seReaders之前，需要对seReaders进行初始化

try {
    let reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
    let name = reader.getName();
    hilog.info(0x0000, 'testTag', 'name %{public}s', JSON.stringify(name));
} catch (error) {
    hilog.error(0x0000, 'testTag', 'getName error %{public}s', JSON.stringify(error));
}
```

#### Reader.isSecureElementPresent

isSecureElementPresent(): boolean

检查当前Reader所对应的安全单元是否可用。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**booleantrue: 安全单元可用， false: 安全单元不可用。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.3300101IllegalStateError, service state exception.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seReaders : omapi.Reader[];

// 在使用seReaders之前，需要对seReaders进行初始化

try {
    let reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
    let isPresent = reader.isSecureElementPresent();
    hilog.info(0x0000, 'testTag', 'isPresent %{public}s', JSON.stringify(isPresent));
} catch (error) {
    hilog.error(0x0000, 'testTag', 'isSecureElementPresent error %{public}s', JSON.stringify(error));
}
```

#### Reader.openSession

 openSession(): Session

在SE Reader实例上创建连接会话，返回Session实例。在一个Reader上可能同时打开多个会话。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**[Session](#ZH-CN_TOPIC_0000002497605424__session)连接会话Session实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.3300101IllegalStateError, service state exception.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seReaders : omapi.Reader[];
let seSession : omapi.Session;

// 在使用seReaders之前，需要对seReaders进行初始化
function secureElementDemo() {
    try {
        let reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
        seSession = reader.openSession();
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'openSession error %{public}s', JSON.stringify(error));
    }
    if (seSession == undefined) {
        hilog.error(0x0000, 'testTag', 'seSession invalid.');
        return;
    }
}
```

#### Reader.closeSessions

 closeSessions(): void

关闭在此Reader上打开的所有Session。所有这些Session打开的所有Channel都将关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.3300101IllegalStateError, service state exception.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seReaders : omapi.Reader[];
let seSession : omapi.Session;
let reader : omapi.Reader;

// 在使用seReaders之前，需要对seReaders进行初始化
function secureElementDemo() {
    try {
        reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
        seSession = reader.openSession();
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'openSession error %{public}s', JSON.stringify(error));
    }
    if (seSession == undefined) {
        hilog.error(0x0000, 'testTag', 'seSession invalid.');
        // 释放SeService资源
        seService.shutdown();
        return;
    }
    try {
        reader.closeSessions();
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'closeSessions error %{public}s', JSON.stringify(error));
    }
}
```

#### Session

Session的实例表示在某个SE Reader实例上创建连接会话。通过[Reader.openSession](#ZH-CN_TOPIC_0000002497605424__readeropensession)获取Session实例。

#### Session.getReader

getReader(): Reader

获取提供此Session的Reader实例。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**[Reader](#ZH-CN_TOPIC_0000002497605424__reader)返回此Session的Reader实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seReaders : omapi.Reader[];
let seSession : omapi.Session;
let reader : omapi.Reader;

// 在使用seReaders之前，需要对seReaders进行初始化
function secureElementDemo() {
    try {
        reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
        seSession = reader.openSession();
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'openSession error %{public}s', JSON.stringify(error));
    }
    if (seSession == undefined) {
        hilog.error(0x0000, 'testTag', 'seSession invalid.');
        return;
    }
    try {
        let sessionReader = seSession.getReader();
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'getReader error %{public}s', JSON.stringify(error));
    }
}
```

#### Session.getATR

getATR(): number[]

获取该SE的ATR。如果该SE的ATR不可用，则应返回空数组。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**number[]返回SE的ATR，SE的ATR不可用时，返回空的数组。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.3300101IllegalStateError, service state exception.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;

// 在使用seSession之前，需要对seSession进行初始化

try {
    let atr = seSession.getATR();
    hilog.info(0x0000, 'testTag', 'atr %{public}s', JSON.stringify(atr));
} catch (error) {
    hilog.error(0x0000, 'testTag', 'getATR error %{public}s', JSON.stringify(error));
}
```

#### Session.close

close(): void

关闭与SE的当前会话连接。这将关闭此Session打开的所有Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.3300101IllegalStateError, service state exception.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;

// 在使用seSession之前，需要对seSession进行初始化

try {
    seSession.close();
} catch (error) {
    hilog.error(0x0000, 'testTag', 'close error %{public}s', JSON.stringify(error));
}
```

#### Session. isClosed

isClosed(): boolean

检查Session是否关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**booleantrue：Session状态已关闭，false：Session是打开的。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;

// 在使用seSession之前，需要对seSession进行初始化

try {
    let isClosed = seSession.isClosed();
    hilog.info(0x0000, 'testTag', 'isClosed %{public}s', JSON.stringify(isClosed));
} catch (error) {
    hilog.error(0x0000, 'testTag', 'isClosed error %{public}s', JSON.stringify(error));
}
```

#### Session.closeChannels

closeChannels(): void

关闭此Session上打开的所有Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.3300101IllegalStateError, service state exception.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;

// 在使用seSession之前，需要对seSession进行初始化

try {
    seSession.closeChannels();
} catch (error) {
    hilog.error(0x0000, 'testTag', 'closeChannels error %{public}s', JSON.stringify(error));
}
```

#### Session.openBasicChannel

openBasicChannel(aid: number[]): Promise<Channel>

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。

**返回值：**

**类型****说明**Promise<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>以Promise形式异步返回可用的基础Channel对象实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
        // 改为在此channel上选择的App的aid
        seSession.openBasicChannel(aidArray).then((data) => {
            seChannel = data;
        }).catch((error : BusinessError)=> {
            hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Session.openBasicChannel

 openBasicChannel(aid: number[], callback: AsyncCallback<Channel>): void

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。callbackAsyncCallback<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>是以callback形式异步返回可用的基础Channel对象实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
        // 改为在此channel上选择的App的aid
        seSession.openBasicChannel(aidArray, (error, data) => {
            if (error) {
                hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
            } else {
                seChannel = data;
            }
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Session.openBasicChannel

openBasicChannel(aid: number[], p2: number): Promise<Channel>

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。p2number是在该Channel上执行的SELECT APDU的P2参数。

**返回值：**

**类型****说明**Promise<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>以Promise形式异步返回可用的基础Channel对象实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
let p2 : number = 0x00;

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
        // 改为在此channel上选择的App的aid
        seSession.openBasicChannel(aidArray, p2).then((data) => {
            seChannel = data;
        }).catch((error : BusinessError)=> {
            hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Session.openBasicChannel

openBasicChannel(aid: number[], p2:number, callback: AsyncCallback<Channel>): void

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。p2number是此Channel上执行SELECT APDU命令的P2参数。callbackAsyncCallback<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>是以callback形式异步返回可用的基础Channel对象实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
let p2 : number = 0x00;

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
        // 改为在此channel上选择的App的aid
        seSession.openBasicChannel(aidArray, p2, (error, data) => {
            if (error) {
                hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
            } else {
                seChannel = data;
            }
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Session.openLogicalChannel

openLogicalChannel(aid: number[]): Promise<Channel>

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。

**返回值：**

**类型****说明**Promise<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>以Promise形式异步返回可用的逻辑Channel对象实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
        // 改为在此channel上选择的App的aid
        seSession.openLogicalChannel(aidArray).then((data) => {
            seChannel = data;
        }).catch((error : BusinessError)=> {
            hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Session.openLogicalChannel

 openLogicalChannel(aid: number[], callback: AsyncCallback<Channel>): void

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。callbackAsyncCallback<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>是以callback形式异步返回可用的逻辑Channel对象实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
        // 改为在此channel上选择的App的aid
        seSession.openLogicalChannel(aidArray, (error, data) => {
            if (error) {
                hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
            } else {
                seChannel = data;
            }
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Session.openLogicalChannel

openLogicalChannel(aid: number[], p2: number): Promise<Channel>

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。p2number是此Channel上执行SELECT APDU命令的P2参数。

**返回值：**

**类型****说明**Promise<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>以Promise形式异步返回可用的逻辑Channel实例对象。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
let p2 : number = 0x00;

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
        // 改为在此channel上选择的App的aid
        seSession.openLogicalChannel(aidArray, p2).then((data) => {
            seChannel = data;
        }).catch((error : BusinessError)=> {
            hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Session.openLogicalChannel

openLogicalChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>):void

打开逻辑通道，参考[ISO 7816-4]协议，返回Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**aidnumber[]是在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。p2number是此Channel上执行SELECT APDU命令的P2参数。callbackAsyncCallback<[Channel](#ZH-CN_TOPIC_0000002497605424__channel)>是以callback形式异步返回可用的逻辑Channel对象实例。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session that has been closed.3300102NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet.3300103SecurityError, the calling application cannot be granted access to this AID or the default applet on this session.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;
let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
let p2 : number = 0x00;

// 在使用seSession之前，需要对seSession进行初始化
function secureElementDemo() {
    try {
    // 改为在此channel上选择的App的aid
        seSession.openLogicalChannel(aidArray, p2, (error, data) => {
            if (error) {
                hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
            } else {
                seChannel = data;
            }
        });
    } catch (exception) {
        hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
    }
    if (seChannel == undefined) {
        hilog.error(0x0000, 'testTag', 'seChannel invalid.');
        return;
    }
}
```

#### Channel

Channel的实例表示在某个Session实例上创建通道，可能为基础通道或逻辑通道。通过[Session.openBasicChannel](#ZH-CN_TOPIC_0000002497605424__sessionopenbasicchannel)或[Session.openLogicalChannel](#ZH-CN_TOPIC_0000002497605424__sessionopenlogicalchannel)获取Channel实例。

#### Channel.getSession

 getSession(): Session

获取打开该Channel的Session对象。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**[Session](#ZH-CN_TOPIC_0000002497605424__session)该Channel绑定的Session 对象。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seSession : omapi.Session;
let seChannel : omapi.Channel;

// 在使用seChannel之前，需要对seChannel进行初始化

try {
    seSession = seChannel.getSession();
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'getSession exception %{public}s', JSON.stringify(exception));
}
```

#### Channel.close

close(): void

关闭Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// 在使用seChannel之前，需要对seChannel进行初始化
try {
    seChannel.close();
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'close exception %{public}s', JSON.stringify(exception));
}
```

#### Channel.isBasicChannel

isBasicChannel(): boolean

检查该Channel是否为基础Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**booleantrue: 该Channel是基础Channel, false：该Channel逻辑Channel 。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// 在使用seChannel之前，需要对seChannel进行初始化
try {
    let isBasic = seChannel.isBasicChannel();
    hilog.info(0x0000, 'testTag', 'isBasic = %{public}s', JSON.stringify(isBasic));
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'isBasicChannel exception %{public}s', JSON.stringify(exception));
}
```

#### Channel.isClosed

isClosed(): boolean

检查该Channel是否已被关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**booleantrue: Channel是关闭的，false: 不是关闭的。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// 在使用seChannel之前，需要对seChannel进行初始化
try {
    let isClosed = seChannel.isClosed();
    hilog.info(0x0000, 'testTag', 'isClosed = %{public}s', JSON.stringify(isClosed));
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'isClosed exception %{public}s', JSON.stringify(exception));
}
```

#### Channel.getSelectResponse

getSelectResponse(): number[]

获取SELECT Applet时的响应数据，包含状态字。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

**类型****说明**number[]SELECT Applet时的响应数据，包含状态字。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// 在使用seChannel之前，需要对seChannel进行初始化
try {
    let response = seChannel.getSelectResponse();
    hilog.info(0x0000, 'testTag', 'response = %{public}s', JSON.stringify(response));
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'getSelectResponse exception %{public}s', JSON.stringify(exception));
}
```

#### Channel.transmit

transmit(command: number[]): Promise<number[]>

向SE发送APDU数据，数据符合ISO/IEC 7816规范。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**commandnumber[]是需要发送到SE的APDU数据。

**返回值：**

**类型****说明**Promise<number[]>以Promise形式异步返回接收到的响应APDU数据，number数组。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session or channel that has been closed.3300103SecurityError, the command is filtered by the security policy.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// 在使用seChannel之前，需要对seChannel进行初始化
let cmdData = [0x01, 0x02, 0x03, 0x04]; // 请更改为正确的data
try {
    seChannel.transmit(cmdData).then((response) => {
        hilog.info(0x0000, 'testTag', 'transmit response = %{public}s.', JSON.stringify(response));
    }).catch((error : BusinessError) => {
        hilog.error(0x0000, 'testTag', 'transmit error = %{public}s.', JSON.stringify(error));
    });
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'transmit exception = %{public}s.', JSON.stringify(exception));
}
```

#### Channel.transmit

transmit(command: number[], callback: AsyncCallback<number[]>): void

向SE发送APDU数据，数据符合ISO/IEC 7816规范。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

**参数名****类型****必填****说明**commandnumber[]是需要发送到SE的APDU数据。callbackAsyncCallback<number[]>是返回接收到的响应APDU数据，number数组。

**错误码：**

错误码的详细介绍请参见[SE错误码](../../errors/SE(secureElement)错误码.md)。

错误码ID错误信息401

The parameter check failed. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameters types.

3. Parameter verification failed.

801Capability not supported.3300101IllegalStateError, an attempt is made to use an SE session or channel that has been closed.3300103SecurityError, the command is filtered by the security policy.3300104IOError, there is a communication problem to the reader or the SE.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { omapi } from '@kit.ConnectivityKit';

let seChannel : omapi.Channel;

// 在使用seChannel之前，需要对seChannel进行初始化
let cmdData = [0x01, 0x02, 0x03, 0x04]; // 请更改为正确的data
try {
    seChannel.transmit(cmdData, (error, response) => {
    if (error) {
        hilog.error(0x0000, 'testTag', 'transmit error %{public}s', JSON.stringify(error));
    } else {
        hilog.info(0x0000, 'testTag', 'transmit response = %{public}s.', JSON.stringify(response));
    }
    });
} catch (exception) {
    hilog.error(0x0000, 'testTag', 'transmit exception %{public}s', JSON.stringify(exception));
}
```