# oh_bluetooth.h

**概述**

定义查询蓝牙开关状态的接口。

引用文件： <ConnectivityKit/bluetooth/oh_bluetooth.h>

库： libbluetooth_ndk.so

系统能力： SystemCapability.Communication.Bluetooth.Core

起始版本： 13

相关模块： [Bluetooth](Bluetooth.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Bluetooth_SwitchState | Bluetooth_SwitchState | 定义蓝牙开关状态的枚举值。 |
| Bluetooth_ResultCode | Bluetooth_ResultCode | 定义蓝牙返回值。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Bluetooth_ResultCode OH_Bluetooth_GetBluetoothSwitchState(Bluetooth_SwitchState *state) | 获取蓝牙开关状态。 |

**枚举类型说明**

**Bluetooth_SwitchState**

```ets
enum Bluetooth_SwitchState
```

描述

定义蓝牙开关状态的枚举值。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| BLUETOOTH_STATE_OFF = 0 | 表示蓝牙关闭。 |
| BLUETOOTH_STATE_TURNING_ON = 1 | 表示蓝牙打开中。 |
| BLUETOOTH_STATE_ON = 2 | 表示蓝牙已打开，使用就绪。 |
| BLUETOOTH_STATE_TURNING_OFF = 3 | 表示蓝牙关闭中。 |
| BLUETOOTH_STATE_BLE_TURNING_ON = 4 | 表示蓝牙LE only模式打开中。 |
| BLUETOOTH_STATE_BLE_ON = 5 | 表示蓝牙处于LE only模式。 |
| BLUETOOTH_STATE_BLE_TURNING_OFF = 6 | 表示蓝牙LE only模式关闭中。 |

**Bluetooth_ResultCode**

```ets
enum Bluetooth_ResultCode
```

描述

定义蓝牙返回值。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| BLUETOOTH_SUCCESS = 0 | 操作成功。 |
| BLUETOOTH_INVALID_PARAM = 401 | 参数错误。可能原因：1. 输入参数为空指针；2. 参数数值超出定义范围。 |

**函数说明**

**OH_Bluetooth_GetBluetoothSwitchState()**

```ets
Bluetooth_ResultCode OH_Bluetooth_GetBluetoothSwitchState(Bluetooth_SwitchState *state)
```

描述

获取蓝牙开关状态。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| Bluetooth_SwitchState *state | - 指向接收蓝牙开关状态的枚举值的指针。需要传入非空指针，否则将返回错误码。详细定义请参考Bluetooth_SwitchState。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Bluetooth_ResultCode | 蓝牙开关状态函数返回值。  详细定义请参考Bluetooth_ResultCode。  BLUETOOTH_SUCCESS 成功获取蓝牙开关状态。  BLUETOOTH_INVALID_PARAM 输入参数为空指针。 |