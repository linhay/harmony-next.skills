# @system.bluetooth (蓝牙)

-

从API Version 7 开始，该接口不再维护，推荐使用[@ohos.bluetooth.ble](../ohos/@ohos.bluetooth.ble (蓝牙ble模块).md)等相关profile接口。

-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import bluetooth from '@system.bluetooth';
```

#### bluetooth.startBLEScan(OBJECT)

开始搜寻附近的低功耗蓝牙外围设备。此操作比较耗费系统资源，请在搜索并连接到设备后调用[bluetooth.stopBLEScan](#ZH-CN_TOPIC_0000002529445401__bluetoothstopblescanobject)方法停止搜索。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

**表1** StartBLEScanOptions

名称类型必填说明intervalnumber否上报设备的间隔，单位毫秒，默认值为0。0表示找到新设备立即上报，其他数值根据传入的间隔上报。successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

**示例：**

```ets
bluetooth.startBLEScan({
  interval:0,
  success() {
    console.log('call bluetooth.startBLEScan success.');
  },
  fail(code, data) {
    console.log('call bluetooth.startBLEScan failed, code:' + code + ', data:' + data);
  },
  complete() {
    console.log('call bluetooth.startBLEScan complete.');
  }
});
```

#### bluetooth.stopBLEScan(OBJECT)

停止搜寻附近的低功耗蓝牙外围设备。与[bluetooth.startBLEScan(OBJECT)](#ZH-CN_TOPIC_0000002529445401__bluetoothstartblescanobject)接口配套使用。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

**表2** StopBLEScanOptions

名称类型必填说明successFunction否接口调用成功的回调函数。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

**示例：**

```ets
bluetooth.stopBLEScan({
  success() {
    console.log('call bluetooth.stopBLEScan success.');
  },
  fail(data, code) {
    console.log('call bluetooth.stopBLEScan fail, code:' + code + ', data:' + data);
  },
  complete() {
    console.log('call bluetooth.stopBLEScan complete.');
  }
});
```

#### bluetooth.subscribeBLEFound(OBJECT)

订阅寻找到新设备。再次调用时，会覆盖前一次调用效果，即仅最后一次调用生效。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

**表3** SubscribeBLEFoundOptions

名称类型必填说明successFunction是寻找到新设备上报时调用的回调函数。failFunction否接口调用失败的回调函数。

**表4** success返回值

参数名类型说明devicesArray<BluetoothDevice>新搜索到的设备列表。

**表5** BluetoothDevice

参数名类型说明addrTypestring

设备地址类型，可能值有：

- public: 公共地址

- random: 随机地址

addrstring设备MAC地址。rssinumber设备蓝牙的信号强弱指标。txpowerstring广播数据中的txpower字段。datahex string广播数据（包含广播数据和扫描响应数据），十六进制字符串。

**示例：**

```ets
bluetooth.subscribeBLEFound({
  success(data) {
    console.log('call bluetooth.subscribeBLEFound success, data: ${data}.');
  },
  fail(data, code) {
    console.log('call bluetooth.startBLEScan failed, code:' + code + ', data:' + data);
  }
});
```

#### bluetooth.unsubscribeBLEFound()

解除订阅寻找到新设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**示例：**

```ets
bluetooth.unsubscribeBLEFound();
```

#### 常见错误码

错误码说明1100是否处于已连接状态。1101当前蓝牙适配器不可用。1102没有找到指定设备。1103连接失败。1104没有找到指定服务。1105没有找到指定特征值。1106当前连接已断开。1107当前特征值不支持此操作。1108其余所有系统上报的异常。1109系统版本不支持 BLE。