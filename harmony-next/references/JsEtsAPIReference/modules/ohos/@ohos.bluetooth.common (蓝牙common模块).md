# @ohos.bluetooth.common (蓝牙common模块)

本模块提供了蓝牙公共接口和参数类型。首批接口包括在调用[connection.pairDevice](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002529445383__connectionpairdevice21)时用于指定目标设备的MAC地址与地址类型的相关参数。

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { common } from '@kit.ConnectivityKit';
```

#### BluetoothAddress

描述蓝牙设备地址信息的参数结构，包括地址与地址类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明addressstring否否表示蓝牙设备的地址，例如："XX:XX:XX:XX:XX:XX"。addressType[BluetoothAddressType](#ZH-CN_TOPIC_0000002497445440__bluetoothaddresstype)否否表示地址类型为蓝牙设备的实际MAC地址或虚拟MAC地址。

#### BluetoothAddressType

枚举，蓝牙设备的地址类型。蓝牙设备的实际MAC地址属于用户的隐私信息，在发现设备的过程中，蓝牙子系统会给每个蓝牙外设分配一个虚拟MAC地址，并保存该虚拟MAC地址和外设实际MAC地址的映射关系。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明VIRTUAL1虚拟MAC地址类型。REAL2实际MAC地址类型。