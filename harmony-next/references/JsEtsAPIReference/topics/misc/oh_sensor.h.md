# oh_sensor.h

**概述**

声明操作传感器的API，包括获取传感器信息和订阅取消订阅传感器数据。

引用文件： <sensors/oh_sensor.h>

库： libohsensor.so

系统能力： SystemCapability.Sensors.Sensor

起始版本： 11

相关模块： [Sensor](Sensor.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| Sensor_Result OH_Sensor_GetInfos(Sensor_Info **infos, uint32_t *count) | 获取设备上所有传感器的信息。 |
| Sensor_Result OH_Sensor_Subscribe(const Sensor_SubscriptionId *id, const Sensor_SubscriptionAttribute *attribute, const Sensor_Subscriber *subscriber) | 订阅传感器数据。系统将以指定的频率向用户报告传感器数据。订阅加速度传感器，需要申请ohos.permission.ACCELEROMETER权限；订阅陀螺仪传感器，需要申请ohos.permission.GYROSCOPE权限；订阅计步器相关传感器时，需要申请ohos.permission.ACTIVITY_MOTION权限；订阅与健康相关的传感器时，比如心率传感器，需要申请ohos.permission.READ_HEALTH_DATA权限，否则订阅失败。订阅其余传感器不需要申请权限。 |
| Sensor_Result OH_Sensor_Unsubscribe(const Sensor_SubscriptionId *id, const Sensor_Subscriber *subscriber) | 取消订阅传感器数据。取消订阅加速度计传感器，需要申请ohos.permission.ACCELEROMETER权限；取消订阅陀螺仪传感器，需要申请ohos.permission.GYROSCOPE权限；取消订阅计步器相关传感器时，需要申请ohos.permission.ACTIVITY_MOTION权限；取消订阅与健康相关的传感器时，需要申请ohos.permission.READ_HEALTH_DATA权限，否则取消订阅失败。取消订阅其余传感器不需要申请权限。 |

**函数说明**

**OH_Sensor_GetInfos()**

```ets
Sensor_Result OH_Sensor_GetInfos(Sensor_Info **infos, uint32_t *count)
```

描述

获取设备上所有传感器的信息。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info **infos | - 双指针指向设备上所有传感器的信息。请参考Sensor_Info。 |
| uint32_t *count | - 指向设备上传感器数量的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Sensor_Result | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。  SENSOR_PARAMETER_ERROR参数检查失败。例如，参数无效；或传入的参数类型不正确。  SENSOR_SERVICE_EXCEPTION传感器服务异常。 |

**OH_Sensor_Subscribe()**

```ets
Sensor_Result OH_Sensor_Subscribe(const Sensor_SubscriptionId *id, const Sensor_SubscriptionAttribute *attribute, const Sensor_Subscriber *subscriber)
```

描述

订阅传感器数据。系统将以指定的频率向用户报告传感器数据。订阅加速度传感器，需要申请ohos.permission.ACCELEROMETER权限；订阅陀螺仪传感器，需要申请ohos.permission.GYROSCOPE权限；订阅计步器相关传感器时，需要申请ohos.permission.ACTIVITY_MOTION权限；订阅与健康相关的传感器时，比如心率传感器，需要申请ohos.permission.READ_HEALTH_DATA权限，否则订阅失败。订阅其余传感器不需要申请权限。

需要权限： ohos.permission.ACCELEROMETER or ohos.permission.GYROSCOPE or

 ohos.permission.ACTIVITY_MOTION or ohos.permission.READ_HEALTH_DATA

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Sensor_SubscriptionId *id | - 指向传感器订阅ID的指针。请参考Sensor_SubscriptionId。 |
| const Sensor_SubscriptionAttribute *attribute | - 指向订阅属性的指针，该属性用于指定数据报告频率。请参考Sensor_SubscriptionAttribute。 |
| const Sensor_Subscriber *subscriber | - 指向订阅者信息的指针，该信息用于指定的回调函数报告传感器数据。请参考Sensor_Subscriber。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Sensor_Result | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。  SENSOR_PERMISSION_DENIED权限验证失败。  SENSOR_PARAMETER_ERROR参数检查失败。例如，参数无效；或传入的参数类型不正确。  SENSOR_SERVICE_EXCEPTION传感器服务异常。 |

**OH_Sensor_Unsubscribe()**

```ets
Sensor_Result OH_Sensor_Unsubscribe(const Sensor_SubscriptionId *id, const Sensor_Subscriber *subscriber)
```

描述

取消订阅传感器数据。取消订阅加速度计传感器，需要申请ohos.permission.ACCELEROMETER权限；取消订阅陀螺仪传感器，需要申请ohos.permission.GYROSCOPE权限；取消订阅计步器相关传感器时，需要申请ohos.permission.ACTIVITY_MOTION权限；取消订阅与健康相关的传感器时，需要申请ohos.permission.READ_HEALTH_DATA权限，否则取消订阅失败。取消订阅其余传感器不需要申请权限。

需要权限： ohos.permission.ACCELEROMETER or ohos.permission.GYROSCOPE or

 ohos.permission.ACTIVITY_MOTION or ohos.permission.READ_HEALTH_DATA

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Sensor_SubscriptionId *id | - 指向传感器订阅ID的指针。请参考Sensor_SubscriptionId。 |
| const Sensor_Subscriber *subscriber | - 指向订阅者信息的指针，该信息用于指定的回调函数报告传感器数据。请参考Sensor_Subscriber。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Sensor_Result | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 SENSOR_PERMISSION_DENIED权限验证失败。 SENSOR_PARAMETER_ERROR参数检查失败。例如，参数无效；或传入的参数类型不正确。 SENSOR_SERVICE_EXCEPTION传感器服务异常。 |