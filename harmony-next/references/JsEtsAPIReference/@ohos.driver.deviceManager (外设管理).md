# @ohos.driver.deviceManager (外设管理)

本模块主要提供管理外部设备的相关功能，包括查询设备列表、绑定设备和解除绑定设备。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
```

#### deviceManager.queryDevices

queryDevices(busType?: number): Array<Readonly<Device>>

获取接入主设备的外部设备列表。如果没有设备接入，那么将会返回一个空的列表。

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明busTypenumber否设备总线类型，不填则查找所有类型设备。

**返回值：**

类型说明Array<Readonly<[Device](#ZH-CN_TOPIC_0000002497445624__device)>>设备信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.22900001ExternalDeviceManager service exception or busType parameter error.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';

try {
  let devices : Array<deviceManager.Device> = deviceManager.queryDevices(deviceManager.BusType.USB);
  for (let item of devices) {
    let device : deviceManager.USBDevice = item as deviceManager.USBDevice;
    console.info(`Device id is ${device.deviceId}`);
  }
} catch (error) {
  console.error(`Failed to query device. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDriverWithDeviceId19+

bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>

根据queryDevices()返回的设备信息绑定设备。使用Promise异步回调。

需要调用[deviceManager.queryDevices](#ZH-CN_TOPIC_0000002497445624__devicemanagerquerydevices)获取设备信息列表。

**需要权限：** ohos.permission.ACCESS_DDK_DRIVERS

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过queryDevices获得。onDisconnectAsyncCallback<number>是绑定设备断开的回调。

**返回值：**

类型说明Promise<[RemoteDeviceDriver](#ZH-CN_TOPIC_0000002497445624__remotedevicedriver11)>Promise对象，返回RemoteDeviceDriver对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.26300001ExternalDeviceManager service exception.26300002The driver service does not allow any client to bind.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDriverWithDeviceId(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(`bindDriverWithDeviceId success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.unbindDriverWithDeviceId19+

unbindDriverWithDeviceId(deviceId: number): Promise<number>

解除设备绑定。使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS_DDK_DRIVERS

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过[queryDevices](#ZH-CN_TOPIC_0000002497445624__devicemanagerquerydevices)获得。

**返回值：**

类型说明Promise<number>Promise对象，返回设备ID。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.26300001ExternalDeviceManager service exception.26300003There is no binding relationship.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDriverWithDeviceId(12345678).then((data : number) => {
    console.info(`unbindDriverWithDeviceId success, Device_Id is ${data}.`);
  }, (error : BusinessError) => {
    console.error(`unbindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>,

 callback: AsyncCallback<{deviceId: number; remote: rpc.IRemoteObject;}>): void

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices()](#ZH-CN_TOPIC_0000002497445624__devicemanagerquerydevices)获取设备信息以及device。

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#ZH-CN_TOPIC_0000002497445624__devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过queryDevices获得。onDisconnectAsyncCallback<number>是绑定设备断开的回调。callbackAsyncCallback<{deviceId: number; remote: [rpc.IRemoteObject](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__iremoteobject);}>是绑定设备的回调，返回绑定设备的通信对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.22900001ExternalDeviceManager service exception.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

interface DataType {
  deviceId : number;
  remote : rpc.IRemoteObject;
}

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }, (error : BusinessError, data : DataType) => {
    if (error) {
      console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`bindDevice success`);
  });
} catch (error) {
  console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>,

 callback: AsyncCallback<RemoteDeviceDriver>): void

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices()](#ZH-CN_TOPIC_0000002497445624__devicemanagerquerydevices)获取设备信息以及device。

从 API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#ZH-CN_TOPIC_0000002497445624__devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过queryDevices获得。onDisconnectAsyncCallback<number>是绑定设备断开的回调。callbackAsyncCallback<[RemoteDeviceDriver](#ZH-CN_TOPIC_0000002497445624__remotedevicedriver11)>是指示绑定结果，包括设备 ID 和远程对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.22900001ExternalDeviceManager service exception.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }, (error : BusinessError, data : deviceManager.RemoteDeviceDriver) => {
    if (error) {
      console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`bindDeviceDriver success`);
  });
} catch (error) {
  console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{deviceId: number;

 remote: rpc.IRemoteObject;}>;

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices](#ZH-CN_TOPIC_0000002497445624__devicemanagerquerydevices)获取设备信息以及device。

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#ZH-CN_TOPIC_0000002497445624__devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过queryDevices获得。onDisconnectAsyncCallback<number>是绑定设备断开的回调。

**返回值：**

类型说明Promise<{deviceId: number; remote: [rpc.IRemoteObject](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__iremoteobject);}>Promise对象，返回设备ID和IRemoteObject对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.22900001ExternalDeviceManager service exception.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }).then(data => {
    console.info(`bindDevice success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices](#ZH-CN_TOPIC_0000002497445624__devicemanagerquerydevices)获取设备信息以及device。

从 API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#ZH-CN_TOPIC_0000002497445624__devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过queryDevices获得。onDisconnectAsyncCallback<number>是绑定设备断开的回调。

**返回值：**

类型说明Promise<[RemoteDeviceDriver](#ZH-CN_TOPIC_0000002497445624__remotedevicedriver11)>Promise对象，返回RemoteDeviceDriver对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.22900001ExternalDeviceManager service exception.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(`bindDeviceDriver success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number, callback: AsyncCallback<number>): void

解除设备绑定。

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](#ZH-CN_TOPIC_0000002497445624__devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限**：ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过queryDevices获得。callbackAsyncCallback<number>是解绑完成的回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.22900001ExternalDeviceManager service exception.

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDevice(12345678, (error : BusinessError, data : number) => {
    if (error) {
      console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`unbindDevice success`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number): Promise<number>

解除设备绑定。

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](#ZH-CN_TOPIC_0000002497445624__devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限**：ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

参数名类型必填说明deviceIdnumber是设备ID，通过queryDevices获得。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[驱动错误码](驱动错误码.md)。

错误码ID错误信息201The permission check failed.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.22900001ExternalDeviceManager service exception.

**返回值：**

类型说明Promise<number>Promise对象，返回设备ID。

**示例：**

```ets
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDevice(12345678).then((data : number) => {
    console.info(`unbindDevice success, Device_Id is ${data}.`);
  }, (error : BusinessError) => {
    console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### Device

外设信息。

**系统能力：** SystemCapability.Driver.ExternalDevice

名称类型只读可选说明busType[BusType](#ZH-CN_TOPIC_0000002497445624__bustype)否否总线类型。deviceIdnumber否否设备ID。descriptionstring否否设备描述。

#### USBDevice

USB设备信息，继承自[Device](#ZH-CN_TOPIC_0000002497445624__device)。

**系统能力：** SystemCapability.Driver.ExternalDevice

名称类型只读可选说明vendorIdnumber否否USB设备Vendor ID。productIdnumber否否USB设备Product ID。

#### BusType

设备总线类型。

**系统能力：** SystemCapability.Driver.ExternalDevice

名称值说明USB1USB总线类型。

#### RemoteDeviceDriver11+

远程设备驱动。

**系统能力：** SystemCapability.Driver.ExternalDevice

名称类型只读可选说明deviceId11+number否否设备ID。remote11+[rpc.IRemoteObject](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__iremoteobject)否否远程驱动程序对象。