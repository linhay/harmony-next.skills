# @ohos.telephony.data (蜂窝数据)

蜂窝数据提供了移动数据管理能力，包括获取默认移动数据的SIM卡、获取蜂窝数据业务的上下行数据流状态、蜂窝数据业务链路连接状态，以及检查蜂窝数据业务和漫游是否启用等。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { data } from '@kit.TelephonyKit';
```

#### data.getDefaultCellularDataSlotId

getDefaultCellularDataSlotId(callback: AsyncCallback<number>): void

获取默认移动数据的SIM卡，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是

以callback形式异步返回结果。

- 0：卡槽1。

- 1：卡槽2。

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getDefaultCellularDataSlotId((err: BusinessError, contextData: number) => {
    if(err) {
        console.error(`getDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`getDefaultCellularDataSlotId success`);
    }
});
```

#### data.getDefaultCellularDataSlotId

getDefaultCellularDataSlotId(): Promise<number>

获取默认移动数据的SIM卡，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明Promise<number>

以Promise形式返回获取默认移动数据的SIM卡。

- 0：卡槽1。

- 1：卡槽2。

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getDefaultCellularDataSlotId().then((contextData: number) => {
    console.info(`getDefaultCellularDataSlotId success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}`);
});
```

#### data.getDefaultCellularDataSlotIdSync9+

getDefaultCellularDataSlotIdSync(): number

获取默认移动数据的SIM卡。

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明number

获取默认移动数据的SIM卡。

- 0：卡槽1。

- 1：卡槽2。

**示例：**

```ets
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSlotIdSync())
```

#### data.getCellularDataFlowType

getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void

获取蜂窝数据业务的上下行状态，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明callbackAsyncCallback<[DataFlowType](#ZH-CN_TOPIC_0000002529445455__dataflowtype)>是以callback形式异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataFlowType((err: BusinessError, contextData: data.DataFlowType) => {
    if(err) {
        console.error(`getCellularDataFlowType fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`getCellularDataFlowType success`);
    }
});
```

#### data.getCellularDataFlowType

getCellularDataFlowType(): Promise<DataFlowType>

获取蜂窝数据业务的上下行状态，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明Promise<[DataFlowType](#ZH-CN_TOPIC_0000002529445455__dataflowtype)>以Promise形式返回获取蜂窝数据业务的上下行状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataFlowType().then((contextData: data.DataFlowType) => {
    console.info(`getCellularDataFlowType success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`getCellularDataFlowType fail. code: ${err.code}, message: ${err.message}`);
});
```

#### data.getCellularDataState

getCellularDataState(callback: AsyncCallback<DataConnectState>): void

获取蜂窝数据业务的连接状态，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明callbackAsyncCallback<[DataConnectState](#ZH-CN_TOPIC_0000002529445455__dataconnectstate)>是以callback形式异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState((err: BusinessError, contextData: data.DataConnectState) => {
    if(err) {
        console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`getCellularDataState success`);
    }
});
```

#### data.getCellularDataState

getCellularDataState(): Promise<DataConnectState>

获取蜂窝数据业务的连接状态，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明Promise<[DataConnectState](#ZH-CN_TOPIC_0000002529445455__dataconnectstate)>以Promise形式返回获取PS域的连接状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState().then((contextData: data.DataConnectState) => {
    console.info(`getCellularDataState success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}`);
});
```

#### data.isCellularDataEnabled

isCellularDataEnabled(callback: AsyncCallback<boolean>): void

检查蜂窝数据业务是否启用，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是

以callback形式异步返回结果。

true：蜂窝数据业务已启用。

false：蜂窝数据业务已禁用。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档和[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Internal error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataEnabled((err: BusinessError, contextData: boolean) => {
    if(err) {
        console.error(`isCellularDataEnabled fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`isCellularDataEnabled success`);
    }
});
```

#### data.isCellularDataEnabled

isCellularDataEnabled(): Promise<boolean>

检查蜂窝数据业务是否启用，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明Promise<boolean>

以Promise形式返回检查蜂窝数据业务是否启用。

true：蜂窝数据业务已启用。

false：蜂窝数据业务已禁用。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档和[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

错误码ID错误信息201Permission denied.8300002Service connection failed.8300003System internal error.8300999Internal error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataEnabled().then((contextData: boolean) => {
    console.info(`isCellularDataEnabled success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`isCellularDataEnabled fail. code: ${err.code}, message: ${err.message}`);
});
```

#### data.isCellularDataEnabledSync12+

isCellularDataEnabledSync(): boolean

检查蜂窝数据业务是否启用，调用此API返回结果。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明boolean

用来返回检查蜂窝数据业务是否启用。

true：蜂窝数据业务已启用。

false：蜂窝数据业务已禁用。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档和[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

错误码ID错误信息201Permission denied.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Internal error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';

try {
    let isEnabled: boolean = data.isCellularDataEnabledSync();
    console.info(`isCellularDataEnabledSync success : ${isEnabled}`);
} catch (err) {
    console.error(`isCellularDataEnabledSync fail. code: ${err.code}, message: ${err.message}`);
}
```

#### data.isCellularDataRoamingEnabled

isCellularDataRoamingEnabled(slotId: number, callback: AsyncCallback<boolean>): void

检查蜂窝数据业务是否启用漫游，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<boolean>是

以callback形式异步返回结果。

true：蜂窝数据业务已启用漫游。

false：蜂窝数据业务已禁用漫游。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档和[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Internal error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataRoamingEnabled(0, (err: BusinessError, contextData: boolean) => {
    if(err) {
        console.error(`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
    } else {
        console.info(`isCellularDataRoamingEnabled success`);
    }
});
```

#### data.isCellularDataRoamingEnabled

isCellularDataRoamingEnabled(slotId: number): Promise<boolean>

检查蜂窝数据业务是否启用漫游，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<boolean>

以Promise形式返回检查蜂窝数据业务是否启用漫游。

true：蜂窝数据业务已启用漫游。

false：蜂窝数据业务已禁用漫游。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档和[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Internal error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataRoamingEnabled(0).then((contextData: boolean) => {
    console.info(`isCellularDataRoamingEnabled success, contextData: ${contextData}`);
}).catch((err: BusinessError) => {
    console.error(`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}`);
});
```

#### data.isCellularDataRoamingEnabledSync12+

isCellularDataRoamingEnabledSync(slotId: number): boolean

检查蜂窝数据业务是否启用漫游，调用此API返回结果。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明boolean

用来返回检查蜂窝数据业务是否启用漫游。

true：蜂窝数据业务已启用漫游。

false：蜂窝数据业务已禁用漫游。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档和[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Internal error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';

try {
    let isEnabled: boolean = data.isCellularDataRoamingEnabledSync(0);
    console.info(`isCellularDataRoamingEnabledSync success : ${isEnabled}`);
} catch (err) {
    console.error(`isCellularDataRoamingEnabledSync fail. code: ${err.code}, message: ${err.message}`);
}
```

#### data.getDefaultCellularDataSimId10+

getDefaultCellularDataSimId(): number

获取默认移动数据的SIM卡ID。

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明number

获取默认移动数据的SIM卡ID。

与SIM卡绑定，从1开始递增。

**示例：**

```ets
import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSimId());
```

#### data.queryAllApns16+

queryAllApns(): Promise<Array<ApnInfo>>

异步获取默认移动数据的SIM卡的APN（access point name，接入点名称）信息。

**需要权限**：ohos.permission.MANAGE_APN_SETTING（该权限是受限开放权限，仅需要连接移动数据专网进行办公室可以申请该权限，权限介绍参见[权限定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionmanage_apn_setting)）

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明Promise<Array<[ApnInfo](#ZH-CN_TOPIC_0000002529445455__apninfo16)>>Promise对象，返回默认移动数据的SIM卡的APN信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.queryAllApns().then((apnInfos: Array<data.ApnInfo>) => {
    console.info(`queryAllApns success, promise: apnInfos->${JSON.stringify(apnInfos)}`);
}).catch((err: BusinessError) => {
    console.error(`queryAllApns failed. code: ${err.code}, message: ${err.message}`);
});
```

#### data.queryApnIds16+

queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>

异步获取传入的ApnInfo对应的ApnId信息。

**需要权限**：ohos.permission.MANAGE_APN_SETTING（该权限是受限开放权限，仅需要连接移动数据专网进行办公室可以申请该权限，权限介绍参见[权限定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionmanage_apn_setting)）

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明apnInfo[ApnInfo](#ZH-CN_TOPIC_0000002529445455__apninfo16)是要查询的APN参数。

**返回值：**

类型说明Promise<Array<number>>Promise对象，返回传入的ApnInfo对应的ApnId信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let apnInfo: data.ApnInfo;
apnInfo = {
  apnName: "CMNET",
  apn: "cmnet",
  mcc: "460",
  mnc: "07",
};

data.queryApnIds(apnInfo).then((apnIds: Array<number>) => {
    console.info(`queryApnIds success, apnIds: ${apnIds}`);
}).catch((err: BusinessError) => {
    console.error(`queryApnIds failed. code: ${err.code}, message: ${err.message}`);
});
```

#### data.setPreferredApn16+

setPreferredApn(apnId: number): Promise<boolean>

异步设置apnId对应的APN为首选APN。

注意:

如果传入的apnId为无效的apnId，切回运营商默认配置的优选Apn。

**需要权限**：ohos.permission.MANAGE_APN_SETTING（该权限是受限开放权限，仅需要连接移动数据专网进行办公室可以申请该权限，权限介绍参见[权限定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionmanage_apn_setting)）

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

参数名类型必填说明apnIdnumber是要设置的apnId，可以通过[queryApnIds](#ZH-CN_TOPIC_0000002529445455__dataqueryapnids16)查询。

**返回值：**

类型说明Promise<boolean>Promise对象，返回设置的结果，在未插卡时会返回fasle。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let apnId: number = 0; // apnId为通过queryApnIds返回的有效值，setPreferredApn传入无效的apnId会切回运营商默认配置的优选APN。
data.setPreferredApn(apnId).then((result: boolean) => {
    console.info(`setPreferredApn result: ${result}`);
}).catch((err: BusinessError) => {
    console.error(`setPreferredApn failed. code: ${err.code}, message: ${err.message}`);
});
```

#### data.getActiveApnName20+

getActiveApnName(): Promise<string>

异步获取默认移动数据SIM卡对应的处于激活状态的数据业务APN（access point name，接入点名称）name信息，若不处于激活状态，返回为空字符串。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

类型说明Promise<string>Promise对象，返回默认移动数据SIM卡对应的处于激活状态的数据业务APN name信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)说明文档。

错误码ID错误信息201Permission denied.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getActiveApnName().then((apn: string) => {
    console.info(`getActiveApnName success, apn: ${apn}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveApnName failed. code: ${err.code}, message: ${err.message}`);
});
```

#### DataFlowType

描述蜂窝数据流类型。

**系统能力**：SystemCapability.Telephony.CellularData

名称值说明DATA_FLOW_TYPE_NONE0表示没有上行或下行数据。DATA_FLOW_TYPE_DOWN1表示只有下行数据。DATA_FLOW_TYPE_UP2表示只有上行数据。DATA_FLOW_TYPE_UP_DOWN3表示有上下行数据。DATA_FLOW_TYPE_DORMANT4表示没有上下行数据，底层链路处于休眠状态。

#### DataConnectState

描述蜂窝数据链路连接状态。

**系统能力**：SystemCapability.Telephony.CellularData

名称值说明DATA_STATE_UNKNOWN-1表示蜂窝数据链路未知。DATA_STATE_DISCONNECTED0表示蜂窝数据链路断开。DATA_STATE_CONNECTING1表示正在连接蜂窝数据链路。DATA_STATE_CONNECTED2表示蜂窝数据链路已连接。DATA_STATE_SUSPENDED3表示蜂窝数据链路被挂起。

#### ApnInfo16+

APN信息。

**系统能力**：SystemCapability.Telephony.CellularData

名称类型只读可选说明apnNamestring否否APN名称。apnstring否否APN。mccstring否否Sim卡的mcc。mncstring否否Sim卡的mnc。userstring否是用户名。typestring否是APN类型。proxystring否是代理地址。mmsproxystring否是彩信代理。