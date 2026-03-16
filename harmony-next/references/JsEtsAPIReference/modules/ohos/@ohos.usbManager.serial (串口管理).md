# @ohos.usbManager.serial (串口管理)

本模块主要提供串口管理功能，包括打开和关闭设备的串口、写入和读取数据、设置和获取串口的配置参数、权限管理等。

本模块首批接口从API version 19开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { serialManager } from '@kit.BasicServicesKit';
```

#### serialManager.getPortList

getPortList(): Readonly<SerialPort>[]

查询串口设备清单，包括设备名称和对应的端口号。

**系统能力：** SystemCapability.USB.USBManager.Serial

**返回值：**

类型说明Readonly<[SerialPort](#ZH-CN_TOPIC_0000002529285497__serialport)>[]串口信息列表。

**示例：**

以下示例代码只是调用getPortList接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口设备清单
function getPortList() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;
}
```

#### serialManager.hasSerialRight

hasSerialRight(portId: number): boolean

检查应用程序是否具有访问串口设备的权限。应用退出后再拉起时，需要重新申请授权。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。

**返回值：**

类型说明booleantrue表示已授权，false表示未授权。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14400005Database operation exception.31400001Serial port management exception.31400003PortId does not exist.

**示例：**

以下示例代码只是调用hasSerialRight接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function hasSerialRight() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('portList: ', JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (serialManager.hasSerialRight(portId)) {
    console.info('The serial port is accessible');
  } else {
    console.info('No permission to access the serial port');
  }
}
```

#### serialManager.requestSerialRight

requestSerialRight(portId: number): Promise<boolean>

请求应用程序访问串口设备的权限。应用退出自动移除对串口设备的访问权限，在应用重启后需要重新申请授权。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。

**返回值：**

类型说明Promise<boolean>Promise对象，true表示请求权限成功，false表示请求权限失败。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14400005Database operation exception.31400001Serial port management exception.31400003PortId does not exist.

**示例：**

以下示例代码只是调用requestSerialRight接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function requestSerialRight() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }
}
```

#### serialManager.open

open(portId: number): void

打开串口设备。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400002Access denied. Call requestSerialRight to request user authorization first.31400003PortId does not exist.31400004The serial port device is occupied.

**示例：**

以下示例代码只是调用open接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function open() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }
}
```

#### serialManager.getAttribute

getAttribute(portId: number): Readonly<SerialAttribute>

获取指定串口的配置参数。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。

**返回值：**

类型说明Readonly<[SerialAttribute](#ZH-CN_TOPIC_0000002529285497__serialattribute)>返回串口的配置参数。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400003PortId does not exist.31400005The serial port device is not opened. Call the open API first.

**示例：**

以下示例代码只是调用getAttribute接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function getAttribute() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
    return;
  }

  // 获取串口配置
  try {
    let attribute: serialManager.SerialAttribute = serialManager.getAttribute(portId);
    if (attribute === undefined) {
      console.error('getAttribute usbSerial error, attribute is undefined');
    } else {
      console.info('getAttribute usbSerial success, attribute: ' + JSON.stringify(attribute));
    }
  } catch (error) {
    console.error('getAttribute usbSerial error, ' + JSON.stringify(error));
  }
}
```

#### serialManager.setAttribute

setAttribute(portId: number, attribute: SerialAttribute): void

设置串口的配置参数。如果未调用该方法，使用默认配置参数（波特率：9600bps；据位：8；校验位：0；停止位：1）。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。attribute[SerialAttribute](#ZH-CN_TOPIC_0000002529285497__serialattribute)是串口参数。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400003PortId does not exist.31400005The serial port device is not opened. Call the open API first.

**示例：**

以下示例代码只是调用setAttribute接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function setAttribute() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
    return;
  }

  // 设置串口配置
  try {
    let attribute: serialManager.SerialAttribute = {
      baudRate: serialManager.BaudRates.BAUDRATE_9600,
      dataBits: serialManager.DataBits.DATABIT_8,
      parity: serialManager.Parity.PARITY_NONE,
      stopBits: serialManager.StopBits.STOPBIT_1
    }
    serialManager.setAttribute(portId, attribute);
    console.info('setAttribute usbSerial success, attribute: ' + JSON.stringify(attribute));
  } catch (error) {
    console.error('setAttribute usbSerial error, ' + JSON.stringify(error));
  }
}
```

#### serialManager.read

read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>

从串口设备异步读取数据。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。bufferUint8Array是读取数据的缓冲区。timeoutnumber否超时时间（单位：ms），可选参数，默认为0不超时，用户按需选择。

**返回值：**

类型说明Promise<number>Promise对象，返回读取数据长度。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400003PortId does not exist.31400005The serial port device is not opened. Call the open API first.31400006Data transfer timed out.31400007I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed.

**示例：**

以下示例代码只是调用read接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function read() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // 异步读取
  let readBuffer: Uint8Array = new Uint8Array(64);
  serialManager.read(portId, readBuffer, 2000).then((size: number) => {
    console.info('read usbSerial success, readBuffer: ' + readBuffer.toString());
  }).catch((error: Error) => {
    console.error('read usbSerial error, ' + JSON.stringify(error));
  })
}
```

#### serialManager.readSync

readSync(portId: number, buffer: Uint8Array, timeout?: number): number

从串口设备同步读取数据。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。bufferUint8Array是读取数据的缓冲区。timeoutnumber否超时时间（单位：ms），可选参数，默认为0不超时，用户按需选择。

**返回值：**

类型说明number返回读取数据长度。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400003PortId does not exist.31400005The serial port device is not opened. Call the open API first.31400006Data transfer timed out.31400007I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed.

**示例：**

以下示例代码只是调用readSync接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function readSync() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // 同步读取
  let readSyncBuffer: Uint8Array = new Uint8Array(64);
  try {
    serialManager.readSync(portId, readSyncBuffer, 2000);
    console.info('readSync usbSerial success, readSyncBuffer: ' + readSyncBuffer.toString());
  } catch (error) {
    console.error('readSync usbSerial error, ' + JSON.stringify(error));
  }
}
```

#### serialManager.write

write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>

向串口设备异步写入数据。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。bufferUint8Array是写入数据的缓冲区。timeoutnumber否超时时间（单位：ms），可选参数，默认为0不超时，用户按需选择。

**返回值：**

类型说明Promise<number>Promise对象，返回写入数据长度。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400003PortId does not exist.31400005The serial port device is not opened. Call the open API first.31400006Data transfer timed out.31400007I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed.

**示例：**

以下示例代码只是调用write接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { buffer } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function write() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // 异步写入
  let writeBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
  serialManager.write(portId, writeBuffer, 2000).then((size: number) => {
    console.info('write usbSerial success, writeBuffer: ' + writeBuffer.toString());
  }).catch((error: Error) => {
    console.error('write usbSerial error, ' + JSON.stringify(error));
  })
}
```

#### serialManager.writeSync

writeSync(portId: number, buffer: Uint8Array, timeout?: number): number

向串口设备同步写数据。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。bufferUint8Array是写入目标缓冲区。timeoutnumber否超时时间（单位：ms），可选参数，默认为0不超时，用户按需选择。

**返回值：**

类型说明number返回写入数据长度。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400003PortId does not exist.31400005The serial port device is not opened. Call the open API first.31400006Data transfer timed out.31400007I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed.

**示例：**

以下示例代码只是调用writeSync接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { buffer } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function writeSync() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // 同步写入
  let writeSyncBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
  try {
    serialManager.writeSync(portId, writeSyncBuffer, 2000);
    console.info('writeSync usbSerial success, writeSyncBuffer: ' + writeSyncBuffer.toString());
  } catch (error) {
    console.error('writeSync usbSerial error, ' + JSON.stringify(error));
  }
}
```

#### serialManager.close

close(portId: number): void

关闭串口。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.31400001Serial port management exception.31400003PortId does not exist.31400005The serial port device is not opened. Call the open API first.

**示例：**

以下示例代码只是调用close接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function close() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 打开设备
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
    return;
  }

  // 关闭串口
  try {
    serialManager.close(portId);
    console.info('close usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('close usbSerial error, ' + JSON.stringify(error));
  }
}
```

#### serialManager.cancelSerialRight

cancelSerialRight(portId: number): void

移除应用程序运行时访问串口设备的权限。此接口会调用close关闭已打开的串口。

**系统能力：** SystemCapability.USB.USBManager.Serial

**参数：**

参数名类型必填说明portIdnumber是端口号。

**错误码：**

以下错误码的详细介绍参见[通用错误码](../../errors/通用错误码.md)和[USB服务错误码](../../errors/USB服务错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14400005Database operation exception.31400001Serial port management exception.31400002Access denied. Call requestSerialRight to request user authorization first.31400003PortId does not exist.

**示例：**

以下示例代码只是调用cancelSerialRight接口的必要流程，需要放入具体的方法中执行。实际调用时，设备开发者需要遵循设备相关协议进行调用。

```ets
import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// 获取串口列表
function cancelSerialRight() {
  let portList: serialManager.SerialPort[] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList[0].portId;

  // 检测设备是否可被应用访问
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // 没有访问设备的权限且用户不授权则退出
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // 取消已经授予的权限
  try {
    serialManager.cancelSerialRight(portId);
    console.info('cancelSerialRight success, portId: ', portId);
  } catch (error) {
    console.error('cancelSerialRight error, ', JSON.stringify(error));
  }
}
```

#### SerialAttribute

串口的配置参数。

**系统能力：** SystemCapability.USB.USBManager.Serial

名称类型只读可选说明baudRate[BaudRates](#ZH-CN_TOPIC_0000002529285497__baudrates)否否串口波特率。dataBits[DataBits](#ZH-CN_TOPIC_0000002529285497__databits)否是串口数据位，默认值为8位。parity[Parity](#ZH-CN_TOPIC_0000002529285497__parity)否是串口奇偶校验，默认值为None，无奇偶校验。stopBits[StopBits](#ZH-CN_TOPIC_0000002529285497__stopbits)否是串口停止位，默认值为1位。

#### SerialPort

串口参数。

**系统能力：** SystemCapability.USB.USBManager.Serial

名称类型只读可选说明portIdnumber否否端口号。deviceNamestring否否串口设备名称。

#### BaudRates

表示波特率的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

名称值说明BAUDRATE_5050传输波特率为50。BAUDRATE_7575传输波特率为75。BAUDRATE_110110传输波特率为110。BAUDRATE_134134传输波特率为134。BAUDRATE_150150传输波特率为150。BAUDRATE_200200传输波特率为200。BAUDRATE_300300传输波特率为300。BAUDRATE_600600传输波特率为600。BAUDRATE_12001200传输波特率为1200。BAUDRATE_18001800传输波特率为1800。BAUDRATE_24002400传输波特率为2400。BAUDRATE_48004800传输波特率为4800。BAUDRATE_96009600传输波特率为9600。BAUDRATE_1920019200传输波特率为19200。BAUDRATE_3840038400传输波特率为38400。BAUDRATE_5760057600传输波特率为57600。BAUDRATE_115200115200传输波特率为115200。BAUDRATE_230400230400传输波特率为230400。BAUDRATE_460800460800传输波特率为460800。BAUDRATE_500000500000传输波特率为500000。BAUDRATE_576000576000传输波特率为576000。BAUDRATE_921600921600传输波特率为921600。BAUDRATE_10000001000000传输波特率为1000000。BAUDRATE_11520001152000传输波特率为1152000。BAUDRATE_15000001500000传输波特率为1500000。BAUDRATE_20000002000000传输波特率为2000000。BAUDRATE_25000002500000传输波特率为2500000。BAUDRATE_30000003000000传输波特率为3000000。BAUDRATE_35000003500000传输波特率为3500000。BAUDRATE_40000004000000传输波特率为4000000。

#### DataBits

表示数据位宽的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

名称值说明DATABIT_88报文的有效数据位宽为8比特。DATABIT_77报文的有效数据位宽为7比特。DATABIT_66报文的有效数据位宽为6比特。DATABIT_55报文的有效数据位宽为5比特。

#### Parity

表示校验位的校验方式的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

名称值说明PARITY_NONE0无校验。PARITY_ODD1奇检验。PARITY_EVEN2偶校验。PARITY_MARK3固定为1。PARITY_SPACE4固定为0。

#### StopBits

表示停止位宽的枚举

**系统能力：** SystemCapability.USB.USBManager.Serial

名称值说明STOPBIT_10报文的有效停止位宽为1比特。STOPBIT_21报文的有效停止位宽为2比特。