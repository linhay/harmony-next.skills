# oh_bluetooth.h

#### 概述

定义查询蓝牙开关状态的接口。

**引用文件：** <ConnectivityKit/bluetooth/oh_bluetooth.h>

**库：** libbluetooth_ndk.so

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 13

**相关模块：**[Bluetooth](Bluetooth.md)

#### 汇总

#### 枚举

名称typedef关键字描述[Bluetooth_SwitchState](#ZH-CN_TOPIC_0000002529445395__bluetooth_switchstate)Bluetooth_SwitchState定义蓝牙开关状态的枚举值。[Bluetooth_ResultCode](#ZH-CN_TOPIC_0000002529445395__bluetooth_resultcode)Bluetooth_ResultCode定义蓝牙返回值。

#### 函数

名称描述[Bluetooth_ResultCode OH_Bluetooth_GetBluetoothSwitchState(Bluetooth_SwitchState *state)](#ZH-CN_TOPIC_0000002529445395__oh_bluetooth_getbluetoothswitchstate)获取蓝牙开关状态。

#### 枚举类型说明

#### Bluetooth_SwitchState

```ets
enum Bluetooth_SwitchState
```

**描述**

定义蓝牙开关状态的枚举值。

**起始版本：** 13

枚举项描述BLUETOOTH_STATE_OFF = 0表示蓝牙关闭。BLUETOOTH_STATE_TURNING_ON = 1表示蓝牙打开中。BLUETOOTH_STATE_ON = 2表示蓝牙已打开，使用就绪。BLUETOOTH_STATE_TURNING_OFF = 3表示蓝牙关闭中。BLUETOOTH_STATE_BLE_TURNING_ON = 4表示蓝牙LE only模式打开中。BLUETOOTH_STATE_BLE_ON = 5表示蓝牙处于LE only模式。BLUETOOTH_STATE_BLE_TURNING_OFF = 6表示蓝牙LE only模式关闭中。

#### Bluetooth_ResultCode

```ets
enum Bluetooth_ResultCode
```

**描述**

定义蓝牙返回值。

**起始版本：** 13

枚举项描述BLUETOOTH_SUCCESS = 0操作成功。BLUETOOTH_INVALID_PARAM = 401参数错误。可能原因：1. 输入参数为空指针；2. 参数数值超出定义范围。

#### 函数说明

#### OH_Bluetooth_GetBluetoothSwitchState()

```ets
Bluetooth_ResultCode OH_Bluetooth_GetBluetoothSwitchState(Bluetooth_SwitchState *state)
```

**描述**

获取蓝牙开关状态。

**起始版本：** 13

**参数：**

参数项描述[Bluetooth_SwitchState](oh_bluetooth.h.md#ZH-CN_TOPIC_0000002529445395__bluetooth_switchstate) *state- 指向接收蓝牙开关状态的枚举值的指针。需要传入非空指针，否则将返回错误码。详细定义请参考[Bluetooth_SwitchState](oh_bluetooth.h.md#ZH-CN_TOPIC_0000002529445395__bluetooth_switchstate)。

**返回：**

类型说明[Bluetooth_ResultCode](oh_bluetooth.h.md#ZH-CN_TOPIC_0000002529445395__bluetooth_resultcode)

蓝牙开关状态函数返回值。

 详细定义请参考[Bluetooth_ResultCode](oh_bluetooth.h.md#ZH-CN_TOPIC_0000002529445395__bluetooth_resultcode)。

[BLUETOOTH_SUCCESS](oh_bluetooth.h.md#ZH-CN_TOPIC_0000002529445395__bluetooth_resultcode) 成功获取蓝牙开关状态。

[BLUETOOTH_INVALID_PARAM](oh_bluetooth.h.md#ZH-CN_TOPIC_0000002529445395__bluetooth_resultcode) 输入参数为空指针。