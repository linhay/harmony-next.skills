# @ohos.distributedDeviceManager (设备管理)

本模块提供分布式设备管理能力。

应用可调用接口实现如下功能：

- 注册和解除注册设备上下线变化监听。
- 发现周边不可信设备。
- 认证和取消认证设备。
- 查询可信设备列表。
- 查询本地设备信息，包括设备名称，设备类型和设备标识等。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
```

#### distributedDeviceManager.createDeviceManager

createDeviceManager(bundleName: string): DeviceManager

创建一个设备管理实例。设备管理实例是分布式设备管理方法的调用入口。用于获取可信设备和本地设备的相关信息。

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明bundleNamestring是指示应用程序的Bundle名称。长度范围1~255字符。

**返回值：**

类型说明[DeviceManager](#ZH-CN_TOPIC_0000002529285429__devicemanager)返回设备管理器对象实例。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
} catch(err) {
  let e: BusinessError = err as BusinessError;
  console.error('createDeviceManager errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### distributedDeviceManager.releaseDeviceManager

releaseDeviceManager(deviceManager: DeviceManager): void

设备管理实例不再使用后，通过该方法释放DeviceManager实例。

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明deviceManager[DeviceManager](#ZH-CN_TOPIC_0000002529285429__devicemanager)是设备管理器对象实例。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  distributedDeviceManager.releaseDeviceManager(dmInstance);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('release device manager errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### DeviceBasicInfo

分布式设备基本信息。

**系统能力**：以下各项对应的系统能力均为SystemCapability.DistributedHardware.DeviceManager

名称类型只读可选说明deviceIdstring否否设备标识符。实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。deviceNamestring否否设备名称。deviceTypestring否否[设备类型](#ZH-CN_TOPIC_0000002529285429__getdevicetype)。networkIdstring否是设备网络标识。

#### DeviceStateChange

表示设备状态。

**系统能力**：以下各项对应的系统能力均为SystemCapability.DistributedHardware.DeviceManager

名称值说明UNKNOWN0设备物理上线，此时状态未知，在状态更改为可用之前，分布式业务无法使用。AVAILABLE1设备可用状态，表示设备间信息已在分布式数据中同步完成，可以运行分布式业务。UNAVAILABLE2设备物理下线，此时状态未知。

#### DeviceManager

设备管理实例，用于获取可信设备和本地设备的相关信息。在调用DeviceManager的方法前，需要先通过createDeviceManager构建一个DeviceManager实例dmInstance。

#### getAvailableDeviceListSync

getAvailableDeviceListSync(): Array<DeviceBasicInfo>

同步获取所有可信设备列表。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

类型说明Array<[DeviceBasicInfo](#ZH-CN_TOPIC_0000002529285429__devicebasicinfo)>返回可信设备列表。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getAvailableDeviceListSync errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### getAvailableDeviceList

getAvailableDeviceList(callback:AsyncCallback<Array<DeviceBasicInfo>>): void

获取所有可信设备列表。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[DeviceBasicInfo](#ZH-CN_TOPIC_0000002529285429__devicebasicinfo)>>是获取所有可信设备列表的回调，返回设备信息。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.getAvailableDeviceList((err: BusinessError, data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
    if (err) {
      console.error('getAvailableDeviceList errCode:' + err.code + ',errMessage:' + err.message);
      return;
    }
    console.info('get available device info: ' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getAvailableDeviceList errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### getAvailableDeviceList

getAvailableDeviceList(): Promise<Array<DeviceBasicInfo>>

获取所有可信设备列表。使用Promise异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

类型说明Promise<Array<[DeviceBasicInfo](#ZH-CN_TOPIC_0000002529285429__devicebasicinfo)>>Promise实例，用于获取异步返回结果。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
dmInstance.getAvailableDeviceList().then((data: Array<distributedDeviceManager.DeviceBasicInfo>) => {
  console.info('get available device info: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('getAvailableDeviceList errCode:' + err.code + ',errMessage:' + err.message);
});
```

#### getLocalDeviceNetworkId

getLocalDeviceNetworkId(): string

获取本地设备网络标识。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

类型说明string返回本地设备网络标识。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceNetworkId: string = dmInstance.getLocalDeviceNetworkId();
  console.info('local device networkId: ' + JSON.stringify(deviceNetworkId));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceNetworkId errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### getLocalDeviceName

getLocalDeviceName(): string

获取本地设备名称。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

类型说明string返回本地设备名称。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceName: string = dmInstance.getLocalDeviceName();
  console.info('local device name: ' + JSON.stringify(deviceName));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### getLocalDeviceType

getLocalDeviceType(): number

获取本地设备类型。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

类型说明number

返回本地设备类型。目前仅支持以下设备类型：

-0: UNKNOWN。

-14: PHONE。

-17: TABLET。

-156: TV。

-131: CAR。

-109: WATCH。

-8: WiFiCamera。

-2562: SMART_DISPLAY。

-2607: 2IN1。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceType: number = dmInstance.getLocalDeviceType();
  console.info('local device type: ' + JSON.stringify(deviceType));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceType errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### getLocalDeviceId

getLocalDeviceId(): string

获取本地设备id，实际值为udid-hash与appid和盐值基于sha256方式进行混淆后的值。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**返回值：**

类型说明string返回本地设备id。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceId: string = dmInstance.getLocalDeviceId();
  console.info('local device id: ' + JSON.stringify(deviceId));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getLocalDeviceId errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### getDeviceName

getDeviceName(networkId: string): string

通过指定设备的网络标识获取该设备名称。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明networkIdstring是设备的网络标识。长度范围1~255字符。

**返回值：**

类型说明string返回指定设备名称。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified networkId is greater than 255.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 设备网络标识，可以从可信设备列表中获取
  let networkId = 'xxxxxxx';
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceName: string = dmInstance.getDeviceName(networkId);
  console.info('device name: ' + JSON.stringify(deviceName));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getDeviceName errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### getDeviceType

getDeviceType(networkId: string): number

通过指定设备的网络标识获取该设备类型。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明networkIdstring是设备的网络标识。长度范围1~255字符。

**返回值：**

类型说明number

返回指定设备类型。目前仅支持以下设备类型：

-0: UNKNOWN。

-14: PHONE。

-17: TABLET。

-156: TV。

-131: CAR。

-109: WATCH。

-8: WiFiCamera。

-2562: SMART_DISPLAY。

-2607: 2IN1。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified networkId is greater than 255.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 设备网络标识，可以从可信设备列表中获取
  let networkId = 'xxxxxxx';
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  let deviceType: number = dmInstance.getDeviceType(networkId);
  console.info('device type: ' + JSON.stringify(deviceType));
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('getDeviceType errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### startDiscovering

startDiscovering(discoverParam: {[key: string]: Object;} , filterOptions?: {[key: string]: Object;} ): void

发现周边设备。发现状态持续两分钟，超过两分钟，会停止发现，最大发现数量99个。wifi场景要求同局域网。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明discoverParam{[key: string]: Object;}是

发现标识。 标识发现的目标类型。

discoverTargetType: 发现目标默认为设备，值为1。

filterOptions{[key: string]: Object;}否

发现设备过滤信息。可选，默认为undefined，发现未上线设备。会携带以下key值：

availableStatus(0-1)：仅发现设备可信，值为0表示设备不可信。

-0：设备离线，客户端需要通过调用bindTarget绑定设备。

-1：设备已在线，客户可以进行连接。

discoverDistance(0-100)：发现距离本地一定距离内的设备，单位为cm。wifi场景不传该参数。

authenticationStatus(0-1)：根据不同的认证状态发现设备：

-0：设备未认证。

-1：设备已认证。

authorizationType(0-2)：根据不同的授权类型发现设备：

-0：根据临时协商的会话密钥认证的设备。

-1：基于同账号密钥进行身份验证的设备。

-2：基于不同账号凭据密钥认证的设备。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed.11600101Failed to execute the function.11600104Discovery unavailable.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface DiscoverParam {
  discoverTargetType: number;
}

interface FilterOptions {
  availableStatus: number;
  discoverDistance: number;
  authenticationStatus: number;
  authorizationType: number;
}

let discoverParam: Record<string, number> = {
  'discoverTargetType': 1
};
let filterOptions: Record<string, number> = {
  'availableStatus': 0
};

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.startDiscovering(discoverParam, filterOptions); // 当有设备发现时，通过discoverSuccess回调通知给应用程序
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('startDiscovering errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### stopDiscovering

stopDiscovering(): void

停止发现周边设备。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.stopDiscovering();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('stopDiscovering errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### bindTarget

bindTarget(deviceId: string, bindParam: {[key: string]: Object;} , callback: AsyncCallback<{deviceId: string;}>): void

认证设备。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明deviceIdstring是设备标识。长度范围1~255字符。bindParam{[key: string]: Object;}是

认证参数。由开发者自行决定传入的键值对。默认会携带以下key值：

bindType 此值是绑定的类型，必填。

-1：PIN码。

targetPkgName 绑定目标的包名。

appName 尝试绑定目标的应用程序名称。

appOperation 应用程序要绑定目标的原因。

customDescription 操作的详细说明。

callbackAsyncCallback<{deviceId: string; }>是认证结果回调。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified deviceId is greater than 255.11600101Failed to execute the function.11600103Authentication unavailable.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  deviceId: string = '';
}

// 认证的设备信息，可以从发现的结果中获取
let deviceId = 'XXXXXXXX';
let bindParam: Record<string, string | number> = {
  'bindType': 1, // 认证类型： 1 - 无账号PIN码认证
  'targetPkgName': 'xxxx',
  'appName': 'xxxx',
  'appOperation': 'xxxx',
  'customDescription': 'xxxx'
};

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.bindTarget(deviceId, bindParam, (err: BusinessError, data: Data) => {
    if (err) {
      console.error('bindTarget errCode:' + err.code + ',errMessage:' + err.message);
      return;
    }
    console.info('bindTarget result:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('bindTarget errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### unbindTarget

unbindTarget(deviceId: string): void

解除认证设备。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明deviceIdstring是设备标识。长度范围1~255字符。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)和[设备管理错误码](设备管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified deviceId is greater than 255.11600101Failed to execute the function.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let deviceId = 'XXXXXXXX';
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.unbindTarget(deviceId);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('unbindTarget errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### on('deviceStateChange')

on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void

注册设备状态回调，以便在设备状态发生变化时根据应用捆绑包名通知应用。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是注册设备状态回调，固定为deviceStateChange。callbackCallback<{ action: [DeviceStateChange](#ZH-CN_TOPIC_0000002529285429__devicestatechange); device: [DeviceBasicInfo](#ZH-CN_TOPIC_0000002529285429__devicebasicinfo); }>是指示要注册的设备状态回调，返回设备状态和设备信息。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  action: distributedDeviceManager.DeviceStateChange = 0;
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('deviceStateChange', (data: Data) => {
    console.info('deviceStateChange on:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceStateChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### off('deviceStateChange')

off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>): void

取消注册设备状态回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是根据应用程序的包名取消注册设备状态回调，固定为deviceStateChange。callbackCallback<{ action: [DeviceStateChange](#ZH-CN_TOPIC_0000002529285429__devicestatechange); device: [DeviceBasicInfo](#ZH-CN_TOPIC_0000002529285429__devicebasicinfo); }>否指示要取消注册的设备状态回调，返回设备状态和设备信息。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  action: distributedDeviceManager.DeviceStateChange = 0;
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('deviceStateChange', (data: Data) => {
    console.info('deviceStateChange' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceStateChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### on('discoverSuccess')

on(type: 'discoverSuccess', callback: Callback<{ device: DeviceBasicInfo; }>): void

注册发现设备成功回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是注册设备发现回调，以便在发现周边设备时通知应用程序，固定为discoverSuccess。callbackCallback<{ device: [DeviceBasicInfo](#ZH-CN_TOPIC_0000002529285429__devicebasicinfo); }>是注册设备发现的回调方法。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('discoverSuccess', (data: Data) => {
    console.info('discoverSuccess:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverSuccess errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### off('discoverSuccess')

off(type: 'discoverSuccess', callback?: Callback<{ device: DeviceBasicInfo; }>): void

取消注册设备发现成功回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是取消注册设备发现回调，固定为discoverSuccess。callbackCallback<{ device: [DeviceBasicInfo](#ZH-CN_TOPIC_0000002529285429__devicebasicinfo); }>否指示要取消注册的设备发现回调，返回设备状态和设备信息。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  device: distributedDeviceManager.DeviceBasicInfo = {
    deviceId: '',
    deviceName: '',
    deviceType: '',
    networkId: ''
  };
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('discoverSuccess', (data: Data) => {
    console.info('discoverSuccess' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverSuccess errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### on('deviceNameChange')

on(type: 'deviceNameChange', callback: Callback<{ deviceName: string; }>): void

注册设备名称变更回调，以便在设备名称改变时通知应用程序。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是注册设备名称改变回调，以便在设备名称改变时通知应用程序，固定为deviceNameChange。callbackCallback<{ deviceName: string;}>是注册设备名称改变的回调方法。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  deviceName: string = '';
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('deviceNameChange', (data: Data) => {
    console.info('deviceNameChange on:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceNameChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### off('deviceNameChange')

off(type: 'deviceNameChange', callback?: Callback<{ deviceName: string; }>): void

取消注册设备名称变更回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是取消注册设备名称改变回调，固定为deviceNameChange。callbackCallback<{ deviceName: string;}>否指示要取消注册设备名称改变的回调方法。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  deviceName: string = '';
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('deviceNameChange', (data: Data) => {
    console.info('deviceNameChange' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('deviceNameChange errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### on('discoverFailure')

on(type: 'discoverFailure', callback: Callback<{ reason: number; }>): void

注册设备发现失败回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是注册设备发现失败回调，以便在发现周边设备失败时通知应用程序，固定为discoverFailure。callbackCallback<{ reason: number; }>是注册设备发现失败的回调方法。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  reason: number = 0;
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('discoverFailure', (data: Data) => {
    console.info('discoverFailure on:' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverFailure errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### off('discoverFailure')

off(type: 'discoverFailure', callback?: Callback<{ reason: number; }>): void

取消注册设备发现失败回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是取消注册设备发现失败回调，固定为discoverFailure。callbackCallback<{ reason: number; }>否指示要取消注册的设备发现失败回调。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

class Data {
  reason: number = 0;
}

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('discoverFailure', (data: Data) => {
    console.info('discoverFailure' + JSON.stringify(data));
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('discoverFailure errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### on('serviceDie')

on(type: 'serviceDie', callback?: Callback<{}>): void

注册设备管理服务死亡回调，以便在服务死亡时通知应用程序。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是注册serviceDie回调，以便在devicemanager服务异常终止时通知应用程序，固定为serviceDie。callbackCallback<{}>否注册serviceDie的回调方法。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.on('serviceDie', () => {
    console.info('serviceDie on');
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('serviceDie errCode:' + e.code + ',errMessage:' + e.message);
}
```

#### off('serviceDie')

off(type: 'serviceDie', callback?: Callback<{}>): void

取消注册设备管理服务死亡回调。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedHardware.DeviceManager

**参数：**

参数名类型必填说明typestring是取消注册serviceDie回调，以便在devicemanager服务异常终止时通知应用程序，固定为serviceDie。callbackCallback<{}>否取消注册serviceDie的回调方法。

**错误码：**

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter type; 3. Parameter verification failed; 4. The size of specified type is greater than 255.

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let dmInstance = distributedDeviceManager.createDeviceManager('ohos.samples.jsHelloWorld');
  dmInstance.off('serviceDie', () => {
    console.info('serviceDie off');
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error('serviceDie errCode:' + e.code + ',errMessage:' + e.message);
}
```