# @ohos.usbManager (USB管理)

本模块主要提供管理USB设备的相关功能，包括主设备上查询USB设备列表、批量数据传输、控制命令传输、权限控制等；从设备上端口管理、功能切换及查询等。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { usbManager } from '@kit.BasicServicesKit';
```

#### 使用说明

凡是参数类型为[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)的接口,都需要执行如下操作：

**在使用接口前：**

1.

调用[usbManager.getDevices](#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)获取设备列表。

1.

调用[usbManager.requestRight](#ZH-CN_TOPIC_0000002497445526__usbmanagerrequestright)获取请求权限。

1.

调用[usbManager.connectDevice](#ZH-CN_TOPIC_0000002497445526__usbmanagerconnectdevice)得到USBDevicePipe作为参数。

**在使用接口后：**

调用[usbManager.closePipe](#ZH-CN_TOPIC_0000002497445526__usbmanagerclosepipe)关闭设备消息控制通道。

#### usbManager.getDevices

getDevices(): Array<Readonly<USBDevice>>

获取接入主设备的USB设备列表。

当USB服务正常运行但无设备接入时，那么将会返回一个空的列表，这是正常情况，表示调用成功但当前没有连接的USB设备。

在USB主机模式未开启、USB服务未正确初始化、USB服务连接失败（如开发者模式关闭）、权限不足或其他系统错误时，接口会返回undefined，注意需要对接口返回值做判空处理。

三方应用没有权限获取serial字段读取设备序列号，需要通过requestRight申请权限后，自行发起控制传输获取。

**系统能力：** SystemCapability.USB.USBManager

**返回值：**

类型说明Array<Readonly<[USBDevice](#ZH-CN_TOPIC_0000002497445526__usbdevice)>>设备信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息801Capability not supported.

**示例：**

```ets
let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
console.info(`devicesList = ${devicesList}`);
/*
devicesList 返回的数据结构,此处提供一个简单的示例，如下
[
  {
    name: "1-1",
    serial: "",
    manufacturerName: "",
    productName: "",
    version: "",
    vendorId: 7531,
    productId: 2,
    clazz: 9,
    subClass: 0,
    protocol: 1,
    devAddress: 1,
    busNum: 1,
    configs: [
      {
        id: 1,
        attributes: 224,
        isRemoteWakeup: true,
        isSelfPowered: true,
        maxPower: 0,
        name: "1-1",
        interfaces: [
          {
            id: 0,
            protocol: 0,
            clazz: 9,
            subClass: 0,
            alternateSetting: 0,
            name: "1-1",
            endpoints: [
              {
                address: 129,
                attributes: 3,
                interval: 12,
                maxPacketSize: 4,
                direction: 128,
                number: 1,
                type: 3,
                interfaceId: 0,
              },
            ],
          },
        ],
      },
    ],
  },
]
*/
```

#### usbManager.connectDevice

connectDevice(device: USBDevice): Readonly<USBDevicePipe>

根据getDevices()返回的设备信息打开USB设备。如果USB服务异常，可能返回undefined，注意需要对接口返回值做判空处理。

1. 需要调用[usbManager.getDevices](#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)获取设备信息以及device;
1. 调用[usbManager.requestRight](#ZH-CN_TOPIC_0000002497445526__usbmanagerrequestright)请求使用该设备的权限。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明device[USBDevice](#ZH-CN_TOPIC_0000002497445526__usbdevice)是USB设备信息，用getDevices获取的busNum和devAddress确定设备，当前其他属性不做处理。

**返回值：**

类型说明Readonly<[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)>指定的传输通道对象。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.14400001Access right denied. Call requestRight to get the USBDevicePipe access right first.

**示例：**

```ets
function connectDevice() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  console.info(`devicepipe = ${devicepipe}`);
}
```

#### usbManager.hasRight

hasRight(deviceName: string): boolean

判断是否有权访问该设备。

如果“使用者”（如各种App或系统）有权访问设备则返回true；无权访问设备则返回false。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明deviceNamestring是设备名称，来自getDevices获取的设备列表。

**返回值：**

类型说明booleantrue表示有访问设备的权限，false表示没有访问设备的权限。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function hasRight(): boolean {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return false;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let right: boolean = usbManager.hasRight(device.name);
  console.info(`${right}`);
  return right;
}
```

#### usbManager.requestRight

requestRight(deviceName: string): Promise<boolean>

请求软件包的临时权限以访问设备。使用Promise异步回调。系统应用默认拥有访问设备权限，无需调用此接口申请。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明deviceNamestring是设备名称，来自getDevices获取的设备列表。

**返回值：**

类型说明Promise<boolean>Promise对象，返回临时权限的申请结果。返回true表示临时权限申请成功；返回false则表示临时权限申请失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function requestRight() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name).then(ret => {
    console.info(`requestRight = ${ret}`);
  });
}
```

#### usbManager.removeRight

removeRight(deviceName: string): boolean

移除软件包访问设备的权限。系统应用默认拥有访问设备权限，调用此接口不会产生影响。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明deviceNamestring是设备名称，来自getDevices获取的设备列表。

**返回值：**

类型说明boolean返回权限移除结果。返回true表示权限移除成功；返回false则表示权限移除失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function removeRight(): boolean {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return false;
  }

  let device: usbManager.USBDevice = devicesList[0];
  if (usbManager.removeRight(device.name)) {
    console.info(`Succeed in removing right`);
    return true;
  }
  return false;
}
```

#### usbManager.claimInterface

claimInterface(pipe: USBDevicePipe, iface: USBInterface, force ?: boolean): number

声明对USB设备某个接口的控制权。

在USB编程中，claim interface是一个常见操作，指的是应用程序请求操作系统将某个USB接口从内核驱动中释放并交由用户空间程序控制。

下面用到的claim通信接口都表示claim interface操作。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定总线号和设备地址，需要调用connectDevice获取。iface[USBInterface](#ZH-CN_TOPIC_0000002497445526__usbinterface)是用于确定需要获取接口的索引，需要调用getDevices获取设备信息并通过id确定唯一接口。forceboolean否可选参数，是否强制获取。默认值为false ，表示不强制获取，用户按需选择。

**返回值：**

类型说明number

claim通信接口成功返回0；claim通信接口失败返回其他错误码如下：

- 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。

- 88080486：服务初始化中，请稍后重试。

- 88080488：无设备访问权限，请先调用requestRight接口申请授权。

- -1：驱动异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function claimInterface() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  let interfaces: usbManager.USBInterface = device.configs[0].interfaces[0];
  let ret: number= usbManager.claimInterface(devicepipe, interfaces);
  console.info(`claimInterface = ${ret}`);
}
```

#### usbManager.releaseInterface

releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number

释放claim过的通信接口。

在调用该接口前需要通过[usbManager.claimInterface](#ZH-CN_TOPIC_0000002497445526__usbmanagerclaiminterface)claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定总线号和设备地址，需要调用connectDevice获取。iface[USBInterface](#ZH-CN_TOPIC_0000002497445526__usbinterface)是用于确定需要释放接口的索引，需要调用getDevices获取设备信息并通过id确定唯一接口。

**返回值：**

类型说明number

释放接口成功返回0；释放接口失败返回其他错误码如下：

- 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。

- 88080486：服务初始化中，请稍后重试。

- 88080488：无设备访问权限，请先调用requestRight接口申请授权。

- -1：驱动异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function releaseInterface() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  let interfaces: usbManager.USBInterface = device.configs[0].interfaces[0];
  let ret: number= usbManager.claimInterface(devicepipe, interfaces);
  ret = usbManager.releaseInterface(devicepipe, interfaces);
  console.info(`releaseInterface = ${ret}`);
}
```

#### usbManager.setConfiguration

setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number

设置设备配置。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定总线号和设备地址，需要调用connectDevice获取。config[USBConfiguration](#ZH-CN_TOPIC_0000002497445526__usbconfiguration)是用于确定需要设置的配置，需要调用getDevices获取设备信息并通过id用于确定唯一设置。

**返回值：**

类型说明number

设置设备配置成功返回0；设置设备配置失败返回其他错误码如下：

- 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。

- 88080486：服务初始化中，请稍后重试。

- 88080488：无设备访问权限，请先调用requestRight接口申请授权。

- -1：驱动异常。

- -17：I/O失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function setConfiguration() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  let config: usbManager.USBConfiguration = device.configs[0];
  let ret: number= usbManager.setConfiguration(devicepipe, config);
  console.info(`setConfiguration = ${ret}`);
}
```

#### usbManager.setInterface

setInterface(pipe: USBDevicePipe, iface: USBInterface): number

设置设备接口。

一个USB接口可能存在多重选择模式，支持动态切换。使用的场景：数据传输时，通过该接口可重新设置端点，使端点与传输类型匹配。

在调用该接口前需要通过[usbManager.claimInterface](#ZH-CN_TOPIC_0000002497445526__usbmanagerclaiminterface)claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定总线号和设备地址，需要调用connectDevice获取。iface[USBInterface](#ZH-CN_TOPIC_0000002497445526__usbinterface)是用于确定需要设置的接口，需要调用getDevices获取设备信息并通过id和alternateSetting确定唯一接口。

**返回值：**

类型说明number

设置设备接口成功返回0；设置设备接口失败返回其他错误码如下：

- 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。

- 88080486：服务初始化中，请稍后重试。

- 88080488：无设备访问权限，请先调用requestRight接口申请授权。

- -1：驱动异常 。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function setInterface() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  let interfaces: usbManager.USBInterface = device.configs[0].interfaces[0];
  let ret: number = usbManager.claimInterface(devicepipe, interfaces);
  ret = usbManager.setInterface(devicepipe, interfaces);
  console.info(`setInterface = ${ret}`);
}
```

#### usbManager.getRawDescriptor

getRawDescriptor(pipe: USBDevicePipe): Uint8Array

获取原始的USB描述符。如果USB服务异常，可能返回undefined，注意需要对接口返回值做判空处理。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定总线号和设备地址，需要调用connectDevice获取。

**返回值：**

类型说明Uint8Array返回获取的原始数据；失败返回undefined。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function getRawDescriptor() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList[0].name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList[0]);
  let ret: Uint8Array = usbManager.getRawDescriptor(devicepipe);
}
```

#### usbManager.getFileDescriptor

getFileDescriptor(pipe: USBDevicePipe): number

获取文件描述符。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定总线号和设备地址，需要调用connectDevice获取。

**返回值：**

类型说明number返回设备对应的文件描述符，失败返回负数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function getFileDescriptor() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList[0].name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList[0]);
  let ret: number = usbManager.getFileDescriptor(devicepipe);
  console.info(`getFileDescriptor = ${ret}`);
  let closeRet: number = usbManager.closePipe(devicepipe);
  console.info(`closePipe = ${closeRet}`);
}
```

#### usbManager.controlTransfer(deprecated)

controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout ?: number): Promise<number>

控制传输。使用Promise异步回调。

从 API version 9开始支持，从API version 12开始废弃。建议使用 [usbControlTransfer](#ZH-CN_TOPIC_0000002497445526__usbmanagerusbcontroltransfer12) 替代。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定设备，需要调用connectDevice获取。controlparam[USBControlParams](#ZH-CN_TOPIC_0000002497445526__usbcontrolparamsdeprecated)是控制传输参数，按需设置参数，参数传参类型请参考USB协议。timeoutnumber否超时时间（单位：ms），可选参数，默认为0不超时，用户按需选择。

**返回值：**

类型说明Promise<number>

Promise对象，获取传输或接收到的数据块大小。失败返回其他错误码如下：

- -1：驱动异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
class PARA {
  request: number = 0
  reqType: usbManager.USBControlRequestType = 0
  target: usbManager.USBRequestTargetType = 0
  value: number = 0
  index: number = 0
  data: Uint8Array = new Uint8Array()
}

let param: PARA = {
  request: 0x06,
  reqType: 0x80,
  target:0,
  value: 0x01 << 8 | 0,
  index: 0,
  data: new Uint8Array(18)
};

function controlTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList[0].name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList[0]);
  usbManager.controlTransfer(devicepipe, param).then((ret: number) => {
  console.info(`controlTransfer = ${ret}`);
  })
}
```

#### usbManager.usbControlTransfer12+

usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout ?: number): Promise<number>

控制传输。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定设备。requestparam[USBDeviceRequestParams](#ZH-CN_TOPIC_0000002497445526__usbdevicerequestparams12)是控制传输参数，按需设置参数，参数传参类型请参考USB协议。timeoutnumber否超时时间（单位：ms），可选参数，默认为0不超时。

**返回值：**

类型说明Promise<number>

Promise对象，获取传输或接收到的数据块大小。失败返回其他错误码如下：

- -1：驱动异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.801Capability not supported.

**示例：**

```ets
class PARA {
  bmRequestType: number = 0
  bRequest: number = 0
  wValue: number = 0
  wIndex: number = 0
  wLength: number = 0
  data: Uint8Array = new Uint8Array()
}

let param: PARA = {
  bmRequestType: 0x80,
  bRequest: 0x06,

  wValue:0x01 << 8 | 0,
  wIndex: 0,
  wLength: 18,
  data: new Uint8Array(18)
};

function usbControlTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList[0].name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList[0]);
  usbManager.usbControlTransfer(devicepipe, param).then((ret: number) => {
  console.info(`usbControlTransfer = ${ret}`);
  })
}
```

#### usbManager.bulkTransfer

bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout ?: number): Promise<number>

批量传输。使用Promise异步回调。

单次批量传输的传输数据总量（包括pipe、endpoint、buffer、timeout）请控制在200KB以下。

在调用接口前需要通过[usbManager.claimInterface](#ZH-CN_TOPIC_0000002497445526__usbmanagerclaiminterface)claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定设备，需要调用connectDevice获取。endpoint[USBEndpoint](#ZH-CN_TOPIC_0000002497445526__usbendpoint)是用于确定传输的端口，需要调用getDevices获取设备信息列表以及endpoint，address用于确定端点地址，direction用于确定端点的方向，interfaceId用于确定所属接口，当前其他属性不做处理。bufferUint8Array是用于写入或读取数据的缓冲区。timeoutnumber否超时时间（单位：ms），可选参数，默认为0不超时，用户按需选择。

**返回值：**

类型说明Promise<number>

Promise对象，获取传输或接收到的数据块大小。失败返回其他错误码如下：

- -1：驱动异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

以下示例代码只是调用bulkTransfer接口的必要流程，实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

```ets
//usbManager.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限。
//把获取到的设备对象作为参数传入usbManager.connectDevice;当usbManager.connectDevice接口成功返回之后；
//才可以调用第三个接口usbManager.claimInterface.当usbManager.claimInterface 调用成功以后,再调用该接口。
function bulkTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);

  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  for (let i = 0; i < device.configs[0].interfaces.length; i++) {
    if (device.configs[0].interfaces[i].endpoints[0].attributes == 2) {
      let endpoint: usbManager.USBEndpoint = device.configs[0].interfaces[i].endpoints[0];
      let interfaces: usbManager.USBInterface = device.configs[0].interfaces[i];
      let ret: number = usbManager.claimInterface(devicepipe, interfaces);
      let buffer =  new Uint8Array(128);
      usbManager.bulkTransfer(devicepipe, endpoint, buffer).then((ret: number) => {
        console.info(`bulkTransfer = ${ret}`);
      });
    }
  }
}
```

#### usbManager.usbSubmitTransfer18+

usbSubmitTransfer(transfer: UsbDataTransferParams): void

提交异步传输请求。

本接口为异步接口，调用后立刻返回，实际读写操作的结果以回调的方式返回。

在调用该接口前需要通过[usbManager.claimInterface](#ZH-CN_TOPIC_0000002497445526__usbmanagerclaiminterface)claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明transfer[UsbDataTransferParams](#ZH-CN_TOPIC_0000002497445526__usbdatatransferparams18)是作为通用USB数据传输接口，客户端需要填充这个对象中的参数，用以发起传输请求。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息801Capability not supported.14400001Access right denied. Call requestRight to get the USBDevicePipe access right first.14400007Resource busy. Possible causes: 1. The transfer has already been submitted. 2. The interface is claimed by another program or driver.14400008No such device (it may have been disconnected).14400009Insufficient memory. Possible causes: 1. Memory allocation failed.14400012Transmission I/O error.

**示例：**

以下示例代码需要放入具体的方法中执行，只是调用usbSubmitTransfer接口的必要流程，实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

```ets
//usbManager.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限。
//把获取到的设备对象作为参数传入usbManager.connectDevice;当usbManager.connectDevice接口成功返回之后；
//才可以调用第三个接口usbManager.claimInterface.当usbManager.claimInterface 调用成功以后,再调用该接口。
function usbSubmitTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }
  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  //获取endpoint端点地址。
  let endpoint = device.configs[0].interfaces[0]?.endpoints.find((value) => {
    return value.direction === 0 && value.type === 2
  })
  //获取设备的第一个id。
  let ret: number = usbManager.claimInterface(devicepipe, device.configs[0].interfaces[0], true);

  let transferParams: usbManager.UsbDataTransferParams = {
    devPipe: devicepipe,
    flags: usbManager.UsbTransferFlags.USB_TRANSFER_SHORT_NOT_OK,
    endpoint: 1,
    type: usbManager.UsbEndpointTransferType.TRANSFER_TYPE_BULK,
    timeout: 2000,
    length: 10,
    callback: () => {},
    userData: new Uint8Array(10),
    buffer: new Uint8Array(10),
    isoPacketCount: 0,
  };
  try {
    transferParams.endpoint=endpoint?.address as number;
    transferParams.callback=(err, callBackData: usbManager.SubmitTransferCallback)=>{
      console.info('callBackData =' +JSON.stringify(callBackData));
    }
    usbManager.usbSubmitTransfer(transferParams);
    console.info('USB transfer request submitted.');
  } catch (error) {
    console.error('USB transfer failed:', error);
  }
}
```

#### usbManager.usbCancelTransfer18+

usbCancelTransfer(transfer: UsbDataTransferParams): void

取消异步传输请求。

该接口的主要作用是主动取消尚未完成的USB数据传输请求（如usbSubmitTransfer提交的传输）。

在调用该接口前需要通过[usbManager.claimInterface](#ZH-CN_TOPIC_0000002497445526__usbmanagerclaiminterface)claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明transfer[UsbDataTransferParams](#ZH-CN_TOPIC_0000002497445526__usbdatatransferparams18)是在取消传输的接口中，只需要填充[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)和[USBEndpoint](#ZH-CN_TOPIC_0000002497445526__usbendpoint)即可。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息801Capability not supported.14400001Access right denied. Call requestRight to get the USBDevicePipe access right first.14400008No such device (it may have been disconnected).14400010

Other USB error. Possible causes:

1.Unrecognized discard error code.

14400011The transfer is not in progress, or is already complete or cancelled.

**示例：**

以下示例代码需要放入具体的方法中执行，只是调用usbCancelTransfer接口的必要流程，实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

```ets
//usbManager.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限。
//把获取到的设备对象作为参数传入usbManager.connectDevice;当usbManager.connectDevice接口成功返回之后；
//才可以调用第三个接口usbManager.claimInterface.当usbManager.claimInterface 调用成功以后,再调用该接口。
function usbCancelTransfer() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }
  let device: usbManager.USBDevice = devicesList[0];
  usbManager.requestRight(device.name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
  //获取endpoint端点地址。
  let endpoint = device.configs[0].interfaces[0]?.endpoints.find((value) => {
    return value.direction === 0 && value.type === 2
  })
  //获取设备的第一个id。
  let ret: number = usbManager.claimInterface(devicepipe, device.configs[0].interfaces[0], true);
  let transferParams: usbManager.UsbDataTransferParams = {
    devPipe: devicepipe,
    flags: usbManager.UsbTransferFlags.USB_TRANSFER_SHORT_NOT_OK,
    endpoint: 1,
    type: usbManager.UsbEndpointTransferType.TRANSFER_TYPE_BULK,
    timeout: 2000,
    length: 10,
    callback: () => {},
    userData: new Uint8Array(10),
    buffer: new Uint8Array(10),
    isoPacketCount: 0,
  };
  try {
    transferParams.endpoint=endpoint?.address as number;
    transferParams.callback=(err, callBackData: usbManager.SubmitTransferCallback)=>{
      console.info('callBackData =' +JSON.stringify(callBackData));
    }
    usbManager.usbSubmitTransfer(transferParams);
    usbManager.usbCancelTransfer(transferParams);
    console.info('USB transfer request submitted.');
  } catch (error) {
    console.error('USB transfer failed:', error);
  }
}
```

#### usbManager.closePipe

closePipe(pipe: USBDevicePipe): number

关闭设备消息控制通道。

1. 需要调用[usbManager.getDevices](#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)获取设备列表；
1. 调用[usbManager.requestRight](#ZH-CN_TOPIC_0000002497445526__usbmanagerrequestright)获取设备请求权限；
1. 调用[usbManager.connectDevice](#ZH-CN_TOPIC_0000002497445526__usbmanagerconnectdevice)得到devicepipe作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定USB设备消息控制通道，需要调用connectDevice获取。

**返回值：**

类型说明number

关闭设备消息控制通道成功返回0；关闭设备消息控制通道失败返回其他错误码如下：

- 22：服务异常。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
function closePipe() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.info(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList[0].name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList[0]);
  let ret: number = usbManager.closePipe(devicepipe);
  console.info(`closePipe = ${ret}`);
}
```

#### usbManager.hasAccessoryRight14+

hasAccessoryRight(accessory: USBAccessory): boolean

检查应用程序是否有权访问USB配件。

需要调用[usbManager.getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明accessory[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)是USB配件，需要通过[getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取。

**返回值：**

类型说明booleantrue表示应用程序有权访问USB配件，false表示应用程序无权访问USB配件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.14400004Service exception. Possible causes: 1. No accessory is plugged in.14400005Database operation exception.14401001The target USBAccessory not matched.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.hasAccessoryRight(accList[0])
  hilog.info(0, 'testTag ui', `hasAccessoryRight success, ret:${flag}`)
} catch (error) {
  hilog.info(0, 'testTag ui', `hasAccessoryRight error ${error.code}, message is ${error.message}`)
}
```

#### usbManager.requestAccessoryRight14+

requestAccessoryRight(accessory: USBAccessory): Promise<boolean>

为指定应用程序申请访问USB配件的访问权限。使用Promise异步回调。

需要调用[usbManager.getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明accessory[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)是USB配件，需要通过[getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取。

**返回值：**

类型说明Promise<boolean>Promise对象，返回应用程序访问配件权限的申请结果。返回true表示权限申请成功；返回false表示权限申请失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.14400004Service exception. Possible causes: 1. No accessory is plugged in.14400005Database operation exception.14401001The target USBAccessory not matched.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.requestAccessoryRight(accList[0])
  hilog.info(0, 'testTag ui', `requestAccessoryRight success, ret:${flag}`)
} catch (error) {
  hilog.info(0, 'testTag ui', `requestAccessoryRight error ${error.code}, message is ${error.message}`)
}
```

#### usbManager.cancelAccessoryRight14+

cancelAccessoryRight(accessory: USBAccessory): void

取消当前应用程序访问USB配件的权限。

需要调用[usbManager.getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明accessory[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)是USB配件，需要通过[getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.14400004Service exception. Possible causes: 1. No accessory is plugged in.14400005Database operation exception.14401001The target USBAccessory not matched.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.requestAccessoryRight(accList[0])
  usbManager.cancelAccessoryRight(accList[0])
  hilog.info(0, 'testTag ui', `cancelAccessoryRight success`)
} catch (error) {
  hilog.info(0, 'testTag ui', `cancelAccessoryRight error ${error.code}, message is ${error.message}`)
}
```

#### usbManager.getAccessoryList14+

getAccessoryList(): Array<Readonly<USBAccessory>>

获取当前已接入主机的USB配件列表。

**系统能力：** SystemCapability.USB.USBManager

**返回值：**

类型说明Array<Readonly<[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)>>只读的USB配件列表。当前仅支持列表中包含1个USB配件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息801Capability not supported.14400004Service exception. Possible causes: 1. No accessory is plugged in.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  hilog.info(0, 'testTag ui', `getAccessoryList success, accList: ${JSON.stringify(accList)}`)
} catch (error) {
  hilog.info(0, 'testTag ui', `getAccessoryList error ${error.code}, message is ${error.message}`)
}
```

#### usbManager.openAccessory14+

openAccessory(accessory: USBAccessory): USBAccessoryHandle

获取配件句柄并打开配件文件描述符。之后可以通过CoreFileKit提供的read/write接口和配件进行通信。

需要调用[usbManager.getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明accessory[USBAccessory](#ZH-CN_TOPIC_0000002497445526__usbaccessory14)是USB配件，需要通过[getAccessoryList](#ZH-CN_TOPIC_0000002497445526__usbmanagergetaccessorylist14)获取。

**返回值：**

类型说明[USBAccessoryHandle](#ZH-CN_TOPIC_0000002497445526__usbaccessoryhandle14)USB配件句柄。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.14400001Access right denied. Call requestRight to get the USBDevicePipe access right first.14400004Service exception. Possible causes: 1. No accessory is plugged in.14401001The target USBAccessory not matched.14401002Failed to open the native accessory node.14401003Cannot reopen the accessory.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo as fs } from '@kit.CoreFileKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.requestAccessoryRight(accList[0])
  let handle = usbManager.openAccessory(accList[0])
  hilog.info(0, 'testTag ui', `openAccessory success`)
  let arrayBuffer = new ArrayBuffer(4096);
  let readLength = fs.readSync(handle.accessoryFd, arrayBuffer, {offset: 0, length: 4096});
  hilog.info(0, 'testTag ui', 'readSync ret: ' + readLength.toString(10));
} catch (error) {
  hilog.info(0, 'testTag ui', `openAccessory error ${error.code}, message is ${error.message}`)
}
```

#### usbManager.closeAccessory14+

closeAccessory(accessoryHandle: USBAccessoryHandle): void

关闭配件文件描述符。

需要调用[usbManager.openAccessory](#ZH-CN_TOPIC_0000002497445526__usbmanageropenaccessory14)获取配件列表，得到[USBAccessoryHandle](#ZH-CN_TOPIC_0000002497445526__usbaccessoryhandle14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明accessoryHandle[USBAccessoryHandle](#ZH-CN_TOPIC_0000002497445526__usbaccessoryhandle14)是USB配件句柄。需要通过[openAccessory](#ZH-CN_TOPIC_0000002497445526__usbmanageropenaccessory14)获取。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.14400004Service exception. Possible causes: 1. No accessory is plugged in.

**示例：**

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
  let flag = usbManager.requestAccessoryRight(accList[0])
  let handle = usbManager.openAccessory(accList[0])
  usbManager.closeAccessory(handle)
  hilog.info(0, 'testTag ui', `closeAccessory success`)
} catch (error) {
  hilog.info(0, 'testTag ui', `closeAccessory error ${error.code}, message is ${error.message}`)
}
```

#### usbManager.resetUsbDevice20+

resetUsbDevice(pipe: USBDevicePipe): boolean

重置USB外设。

本接口调用后会重置此前设置的配置和替换接口，请在调用之前确认相关业务已结束。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

参数名类型必填说明pipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)是用于确定总线号和设备地址，需要调用connectDevice获取。

**返回值：**

类型说明booleantrue表示重置设备成功，false表示重置设备失败。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息801Capability not supported.14400001Access right denied. Call requestRight to get the USBDevicePipe access right first.14400004Service exception. Possible causes: 1. No accessory is plugged in.14400008No such device (it may have been disconnected).14400010

Other USB error. Possible causes:

1.Unrecognized discard error code.

14400013

The USBDevicePipe validity check failed. Possible causes:

1. The input parameters fail the validation check.

2. The call chain used to obtain the input parameters is not reasonable.

**示例：**

```ets
function resetUsbDevice() {
  let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
  if (!devicesList || devicesList.length == 0) {
    console.error(`device list is empty`);
    return;
  }

  usbManager.requestRight(devicesList[0].name);
  let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList[0]);
  try {
    let ret: boolean = usbManager.resetUsbDevice(devicepipe);
    console.info(`resetUsbDevice  = ${ret}`);
  } catch (err) {
    console.error(`resetUsbDevice failed: ` + err);
  }
}
```

#### USBEndpoint

通过USB发送和接收数据的端口。通过[USBInterface](#ZH-CN_TOPIC_0000002497445526__usbinterface)获取。

主机控制器按照Endpoint类型调度。

协议层打包时依赖type决定传输特性。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明addressnumber否否端点地址。attributesnumber否否端点属性。intervalnumber否否端点间隔。maxPacketSizenumber否否端点最大数据包大小。direction[USBRequestDirection](#ZH-CN_TOPIC_0000002497445526__usbrequestdirection)否是端点的方向。numbernumber否是端点号。typenumber否是端点类型。取值见[UsbEndpointTransferType](#ZH-CN_TOPIC_0000002497445526__usbendpointtransfertype18)interfaceIdnumber否是端点所属的接口的唯一标识。

#### USBInterface

一个[USBConfiguration](#ZH-CN_TOPIC_0000002497445526__usbconfiguration)中可以含有多个USBInterface，每个USBInterface提供一个功能。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明idnumber否否接口的唯一标识。protocolnumber否否接口的协议。clazznumber否否设备类型。subClassnumber否否设备子类。alternateSettingnumber否否在同一个接口中的多个描述符中进行切换设置。值的大小表示支持可选模式个数，其中0表示不支持可选模式。namestring否否接口名称。endpointsArray<[USBEndpoint](#ZH-CN_TOPIC_0000002497445526__usbendpoint)>否否当前接口所包含的端点。

#### USBConfiguration

USB配置，一个[USBDevice](#ZH-CN_TOPIC_0000002497445526__usbdevice)中可以含有多个配置。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明idnumber否否配置的唯一标识。attributesnumber否否配置的属性。maxPowernumber否否最大功耗，以毫安为单位。namestring否否配置的名称，可以为空。isRemoteWakeupboolean否否检查当前配置是否支持远程唤醒。true表示支持，false表示不支持。isSelfPoweredboolean否否检查当前配置是否支持独立电源。true表示支持，false表示不支持。interfacesArray <[USBInterface](#ZH-CN_TOPIC_0000002497445526__usbinterface)>否否配置支持的接口属性。

#### USBDevice

USB设备信息。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明busNumnumber否是总线地址。devAddressnumber否是设备地址。serialstring否是序列号。namestring否是设备名字。manufacturerNamestring否是产商信息。productNamestring否是产品信息。versionstring否是版本。vendorIdnumber否是厂商ID。productIdnumber否是产品ID。clazznumber否是设备类。subClassnumber否是设备子类。protocolnumber否是设备协议码。configsArray<[USBConfiguration](#ZH-CN_TOPIC_0000002497445526__usbconfiguration)>否是设备配置描述符信息。

#### USBDevicePipe

USB设备消息传输通道，用于确定设备。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明busNumnumber否否总线地址。devAddressnumber否否设备地址。

#### USBControlParams(deprecated)

控制传输参数。

从 API version 9开始支持，从API version 18开始废弃。建议使用 [USBDeviceRequestParams](#ZH-CN_TOPIC_0000002497445526__usbdevicerequestparams12) 替代。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明requestnumber否否请求类型。target[USBRequestTargetType](#ZH-CN_TOPIC_0000002497445526__usbrequesttargettype)否否请求目标类型。reqType[USBControlRequestType](#ZH-CN_TOPIC_0000002497445526__usbcontrolrequesttype)否否请求控制类型。valuenumber否否请求参数。indexnumber否否请求参数value对应的索引值。dataUint8Array否否用于写入或读取的缓冲区。

#### USBDeviceRequestParams12+

控制传输参数。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明bmRequestTypenumber否否请求控制类型。bRequestnumber否否请求类型。wValuenumber否否请求参数。wIndexnumber否否请求参数value对应的索引值。wLengthnumber否否请求数据的长度。dataUint8Array否否用于写入或读取的缓冲区。

#### USBRequestTargetType

请求目标类型。

**系统能力：** SystemCapability.USB.USBManager

名称值说明USB_REQUEST_TARGET_DEVICE0设备。USB_REQUEST_TARGET_INTERFACE1接口。USB_REQUEST_TARGET_ENDPOINT2端点。USB_REQUEST_TARGET_OTHER3其他。

#### USBControlRequestType

控制请求类型。

**系统能力：** SystemCapability.USB.USBManager

名称值说明USB_REQUEST_TYPE_STANDARD0标准。USB_REQUEST_TYPE_CLASS1类。USB_REQUEST_TYPE_VENDOR2厂商。

#### USBRequestDirection

请求方向。

**系统能力：** SystemCapability.USB.USBManager

名称值说明USB_REQUEST_DIR_TO_DEVICE0写数据，主设备往从设备。USB_REQUEST_DIR_FROM_DEVICE0x80读数据，从设备往主设备。

#### USBAccessory14+

USB配件信息。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明manufacturerstring否否配件的生产厂商。productstring否否配件的产品类型。descriptionstring否否配件的描述。versionstring否否配件的版本。serialNumberstring否否配件的SN号。

#### USBAccessoryHandle14+

USB配件句柄。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明accessoryFdnumber否否配件文件描述符。合法的accessoryFd是正整数。

#### UsbDataTransferParams18+

作为通用USB数据传输接口，客户端需要填充这个对象中的参数，用以发起传输请求。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明devPipe[USBDevicePipe](#ZH-CN_TOPIC_0000002497445526__usbdevicepipe)否否用于确定总线号和设备地址，需要调用connectDevice获取。flags[UsbTransferFlags](#ZH-CN_TOPIC_0000002497445526__usbtransferflags18)否否USB传输标志。endpointnumber否否端点地址，正整数。type[UsbEndpointTransferType](#ZH-CN_TOPIC_0000002497445526__usbendpointtransfertype18)否否传输类型。timeoutnumber否否超时时间，单位为毫秒。lengthnumber否否数据缓冲区的长度，必须是非负数（期望长度），单位为字节。callbackAsyncCallback<[SubmitTransferCallback](#ZH-CN_TOPIC_0000002497445526__submittransfercallback18)>否否传输完成时的回调信息。userDataUint8Array否否用户上下文数据。bufferUint8Array否否用于存储读或者写请求时的数据。isoPacketCountnumber否否实时传输时数据包的数量，仅用于具有实时传输端点的I/O。必须是非负数，单位为个数。

#### UsbTransferFlags18+

USB传输标志。

**系统能力：** SystemCapability.USB.USBManager

名称值说明USB_TRANSFER_SHORT_NOT_OK0将短帧报告为错误。USB_TRANSFER_FREE_BUFFER1自动释放传输缓冲区。USB_TRANSFER_FREE_TRANSFER2完成回调后自动传输。USB_TRANSFER_ADD_ZERO_PACKET3传输将增加一个额外的数据包。

#### UsbEndpointTransferType18+

Usb传输类型。

**系统能力：** SystemCapability.USB.USBManager

名称值说明TRANSFER_TYPE_ISOCHRONOUS0x1实时传输。TRANSFER_TYPE_BULK0x2批量传输。TRANSFER_TYPE_INTERRUPT0x3中断传输。

#### SubmitTransferCallback18+

Usb异步传输回调。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明actualLengthnumber否否读写操作的实际长度值，单位为字节。status[UsbTransferStatus](#ZH-CN_TOPIC_0000002497445526__usbtransferstatus18)否否读写操作完成的状态。isoPacketDescsArray<Readonly<[UsbIsoPacketDescriptor](#ZH-CN_TOPIC_0000002497445526__usbisopacketdescriptor18)>>否否实时传输的分包信息。

#### UsbTransferStatus18+

数据处理完成后通过回调返回的状态码。

**系统能力：** SystemCapability.USB.USBManager

名称值说明TRANSFER_COMPLETED0传输完成。TRANSFER_ERROR1传输失败。TRANSFER_TIMED_OUT2传输超时。TRANSFER_CANCELED3传输已被取消。TRANSFER_STALL4检测到暂停（批量/中断端点）。TRANSFER_NO_DEVICE5设备已断开。TRANSFER_OVERFLOW6设备发送的数据比请求的多。

#### UsbIsoPacketDescriptor18+

实时传输模式回调返回的分包信息。

**系统能力：** SystemCapability.USB.USBManager

名称类型只读可选说明lengthnumber否否读写操作的期望长度值，单位为字节。actualLengthnumber否否读写操作的实际长度值，单位为字节。status[UsbTransferStatus](#ZH-CN_TOPIC_0000002497445526__usbtransferstatus18)否否实时传输分包的状态码。