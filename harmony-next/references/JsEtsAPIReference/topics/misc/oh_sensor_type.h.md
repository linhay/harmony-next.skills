# oh_sensor_type.h

**概述**

定义常用传感器属性。

引用文件： <sensors/oh_sensor_type.h>

库： libohsensor.so

系统能力： SystemCapability.Sensors.Sensor

起始版本： 11

相关模块： [Sensor](Sensor.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Sensor_Info | Sensor_Info | 定义传感器信息。 |
| Sensor_Event | Sensor_Event | 定义传感器数据信息。 |
| Sensor_SubscriptionId | Sensor_SubscriptionId | 定义传感器订阅ID，唯一标识传感器。 |
| Sensor_SubscriptionAttribute | Sensor_SubscriptionAttribute | 定义传感器订阅属性。 |
| Sensor_Subscriber | Sensor_Subscriber | 定义传感器订阅者信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Sensor_Type | Sensor_Type | 枚举传感器类型。 |
| Sensor_Result | Sensor_Result | 定义传感器错误码。 |
| Sensor_Accuracy | Sensor_Accuracy | 枚举传感器报告的数据的精度级别。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Sensor_Info **OH_Sensor_CreateInfos(uint32_t count) | - | 用给定的数字创建一个实例数组，请参考Sensor_Info。 |
| int32_t OH_Sensor_DestroyInfos(Sensor_Info **sensors, uint32_t count) | - | 销毁实例数组并回收内存，请参考Sensor_Info。 |
| int32_t OH_SensorInfo_GetName(Sensor_Info* sensor, char *sensorName, uint32_t *length) | - | 获取传感器名称。 |
| int32_t OH_SensorInfo_GetVendorName(Sensor_Info* sensor, char *vendorName, uint32_t *length) | - | 获取传感器的厂商名称。 |
| int32_t OH_SensorInfo_GetType(Sensor_Info* sensor, Sensor_Type *sensorType) | - | 获取传感器类型。 |
| int32_t OH_SensorInfo_GetResolution(Sensor_Info* sensor, float *resolution) | - | 获取传感器分辨率。 |
| int32_t OH_SensorInfo_GetMinSamplingInterval(Sensor_Info* sensor, int64_t *minSamplingInterval) | - | 获取传感器的最小数据上报间隔。 |
| int32_t OH_SensorInfo_GetMaxSamplingInterval(Sensor_Info* sensor, int64_t *maxSamplingInterval) | - | 获取传感器的最大数据上报间隔时间。 |
| int32_t OH_SensorEvent_GetType(Sensor_Event* sensorEvent, Sensor_Type *sensorType) | - | 获取传感器类型。 |
| int32_t OH_SensorEvent_GetTimestamp(Sensor_Event* sensorEvent, int64_t *timestamp) | - | 获取传感器数据的时间戳。 |
| int32_t OH_SensorEvent_GetAccuracy(Sensor_Event* sensorEvent, Sensor_Accuracy *accuracy) | - | 获取传感器数据的精度。 |
| int32_t OH_SensorEvent_GetData(Sensor_Event* sensorEvent, float **data, uint32_t *length) | - | 获取传感器数据。数据的长度和内容依赖于监听的传感器类型，传感器上报的数据格式如下：SENSOR_TYPE_ACCELEROMETER: data[0]、data[1]、data[2]分别表示设备x、y、z轴的加速度分量，单位m/s2。SENSOR_TYPE_GYROSCOPE: data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角速度，单位弧度/s。SENSOR_TYPE_AMBIENT_LIGHT: data[0]表示环境光强度，单位勒克斯；从api版本12开始，将返回两个额外的数据，其中data[1]表示色温，单位为开尔文；data[2]表示红外亮度，单位cd/m2。SENSOR_TYPE_MAGNETIC_FIELD: data[0]、data[1]、data[2]分别表示设备x、y、z轴的地磁分量，单位微特斯拉。SENSOR_TYPE_BAROMETER：data[0]表示气压值，单位hPa。SENSOR_TYPE_HALL: data[0]表示皮套吸合状态，0表示打开，大于0表示吸附。SENSOR_TYPE_PROXIMITY：data[0]表示接近状态，0表示接近，大于0表示远离。SENSOR_TYPE_ORIENTATION:data[0]、data[1]、data[2]分别表示设备绕z、x、y轴的角度，单位度。SENSOR_TYPE_GRAVITY：data[0]、data[1]、data[2]分别表示设备x、y、z轴的重力加速度分量，单位m/s2。SENSOR_TYPE_ROTATION_VECTOR:data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角度，单位度，data[3]表示旋转向量元素。SENSOR_TYPE_PEDOMETER_DETECTION:data[0]表示几步检测状态，1表示检测到了步数变化。SENSOR_TYPE_PEDOMETER:data[0]表示步数。SENSOR_TYPE_HEART_RATE：data[0]表示心率数值。SENSOR_TYPE_LINEAR_ACCELERATION：从api版本13开始支持。data[0]，data[1]，data[2]，表示分别绕设备的x、y、z轴的线性加速度，单位为m/s2。SENSOR_TYPE_GAME_ROTATION_VECTOR：从api版本13支持。data[0]，data[1]和data[2]，表示设备分别围绕x、y、z轴的旋转角度，单位为度。data[3]表示旋转向量。 |
| Sensor_SubscriptionId *OH_Sensor_CreateSubscriptionId(void) | - | 创建一个Sensor_SubscriptionId实例。 |
| int32_t OH_Sensor_DestroySubscriptionId(Sensor_SubscriptionId *id) | - | 销毁Sensor_SubscriptionId实例并回收内存。 |
| int32_t OH_SensorSubscriptionId_GetType(Sensor_SubscriptionId* id, Sensor_Type *sensorType) | - | 获取传感器类型。 |
| int32_t OH_SensorSubscriptionId_SetType(Sensor_SubscriptionId* id, const Sensor_Type sensorType) | - | 设置传感器类型。 |
| Sensor_SubscriptionAttribute *OH_Sensor_CreateSubscriptionAttribute(void) | - | 创建Sensor_SubscriptionAttribute实例。 |
| int32_t OH_Sensor_DestroySubscriptionAttribute(Sensor_SubscriptionAttribute *attribute) | - | 销毁Sensor_SubscriptionAttribute实例并回收内存。 |
| int32_t OH_SensorSubscriptionAttribute_SetSamplingInterval(Sensor_SubscriptionAttribute* attribute, const int64_t samplingInterval) | - | 设置传感器数据报告间隔。 |
| int32_t OH_SensorSubscriptionAttribute_GetSamplingInterval(Sensor_SubscriptionAttribute* attribute, int64_t *samplingInterval) | - | 获取传感器数据报告间隔。 |
| typedef void (*Sensor_EventCallback)(Sensor_Event *event) | Sensor_EventCallback | 定义用于报告传感器数据的回调函数。 |
| Sensor_Subscriber *OH_Sensor_CreateSubscriber(void) | - | 创建一个Sensor_Subscriber实例。 |
| int32_t OH_Sensor_DestroySubscriber(Sensor_Subscriber *subscriber) | - | 销毁Sensor_Subscriber实例并回收内存。 |
| int32_t OH_SensorSubscriber_SetCallback(Sensor_Subscriber* subscriber, const Sensor_EventCallback callback) | - | 设置一个回调函数来报告传感器数据。 |
| int32_t OH_SensorSubscriber_GetCallback(Sensor_Subscriber* subscriber, Sensor_EventCallback *callback) | - | 获取用于报告传感器数据的回调函数。 |

**枚举类型说明**

**Sensor_Type**

```ets
enum Sensor_Type
```

描述

枚举传感器类型。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| SENSOR_TYPE_ACCELEROMETER = 1 | 加速度传感器。 起始版本： 11 |
| SENSOR_TYPE_GYROSCOPE = 2 | 陀螺仪传感器。 起始版本： 11 |
| SENSOR_TYPE_AMBIENT_LIGHT = 5 | 环境光传感器。 起始版本： 11 |
| SENSOR_TYPE_MAGNETIC_FIELD = 6 | 地磁传感器。 起始版本： 11 |
| SENSOR_TYPE_BAROMETER = 8 | 气压传感器。 起始版本： 11 |
| SENSOR_TYPE_HALL = 10 | 霍尔传感器。 起始版本： 11 |
| SENSOR_TYPE_PROXIMITY = 12 | 接近光传感器。 起始版本： 11 |
| SENSOR_TYPE_ORIENTATION = 256 | 方向传感器。 起始版本： 11 |
| SENSOR_TYPE_GRAVITY = 257 | 重力传感器。 起始版本： 11 |
| SENSOR_TYPE_LINEAR_ACCELERATION = 258 | 线性加速度传感器。 起始版本： 13 |
| SENSOR_TYPE_ROTATION_VECTOR = 259 | 旋转矢量传感器。 起始版本： 11 |
| SENSOR_TYPE_GAME_ROTATION_VECTOR = 262 | 游戏旋转矢量传感器。 起始版本： 13 |
| SENSOR_TYPE_PEDOMETER_DETECTION = 265 | 计步器检测传感器。 起始版本： 11 |
| SENSOR_TYPE_PEDOMETER = 266 | 计步器传感器。 起始版本： 11 |
| SENSOR_TYPE_HEART_RATE = 278 | 心率传感器。 起始版本： 11 |

**Sensor_Result**

```ets
enum Sensor_Result
```

描述

定义传感器错误码。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| SENSOR_SUCCESS = 0 | 操作成功。 起始版本： 11 |
| SENSOR_PERMISSION_DENIED = 201 | 权限验证失败。 起始版本： 11 |
| SENSOR_PARAMETER_ERROR = 401 | 参数检查失败。例如，没有传入强制参数，或者传入的参数类型不正确。 起始版本： 11 |
| SENSOR_SERVICE_EXCEPTION = 14500101 | 传感器服务异常。 起始版本： 11 |

**Sensor_Accuracy**

```ets
enum Sensor_Accuracy
```

描述

枚举传感器报告的数据的精度级别。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| SENSOR_ACCURACY_UNRELIABLE = 0 | 传感器数据不可靠。有可能传感器不与设备接触而进行测量。 起始版本： 11 |
| SENSOR_ACCURACY_LOW = 1 | 传感器数据精度较低。数据在使用前必须根据环境进行校准。 起始版本： 11 |
| SENSOR_ACCURACY_MEDIUM = 2 | 传感器数据处于中等精度水平。建议用户在使用前根据实际环境进行数据校准。 起始版本： 11 |
| SENSOR_ACCURACY_HIGH = 3 | 传感器数据具有很高的精度。数据可以直接使用。 起始版本： 11 |

**函数说明**

**OH_Sensor_CreateInfos()**

```ets
Sensor_Info **OH_Sensor_CreateInfos(uint32_t count)
```

描述

用给定的数字创建一个实例数组，请参考[Sensor_Info](Sensor_Info.md)。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| uint32_t count | 要创建的实例的数量，请参考 Sensor_Info。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Sensor_Info ** | 如果操作成功，返回指向Sensor_Info实例数组的双指针；否则返回NULL。 |

**OH_Sensor_DestroyInfos()**

```ets
int32_t OH_Sensor_DestroyInfos(Sensor_Info **sensors, uint32_t count)
```

描述

销毁实例数组并回收内存，请参考[Sensor_Info](Sensor_Info.md)。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info **sensors | 指向Sensor_Info实例数组的双指针。 |
| uint32_t count | 要销毁的Sensor_Info实例的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorInfo_GetName()**

```ets
int32_t OH_SensorInfo_GetName(Sensor_Info* sensor, char *sensorName, uint32_t *length)
```

描述

获取传感器名称。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info* sensor | 指向传感器信息的指针。 |
| char *sensorName | 指向传感器名称的指针。 |
| uint32_t *length | 指向长度的指针，以字节为单位。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorInfo_GetVendorName()**

```ets
int32_t OH_SensorInfo_GetVendorName(Sensor_Info* sensor, char *vendorName, uint32_t *length)
```

描述

获取传感器的厂商名称。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info* sensor | 指向传感器信息的指针。 |
| char *vendorName | 指向供应商名称的指针。 |
| uint32_t *length | 指向长度的指针，以字节为单位。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorInfo_GetType()**

```ets
int32_t OH_SensorInfo_GetType(Sensor_Info* sensor, Sensor_Type *sensorType)
```

描述

获取传感器类型。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info* sensor | 指向传感器信息的指针。 |
| Sensor_Type *sensorType | 指向传感器类型的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorInfo_GetResolution()**

```ets
int32_t OH_SensorInfo_GetResolution(Sensor_Info* sensor, float *resolution)
```

描述

获取传感器分辨率。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info* sensor | 指向传感器信息的指针。 |
| float *resolution | 指向传感器分辨率Sensor_Accuracy的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorInfo_GetMinSamplingInterval()**

```ets
int32_t OH_SensorInfo_GetMinSamplingInterval(Sensor_Info* sensor, int64_t *minSamplingInterval)
```

描述

获取传感器的最小数据上报间隔。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info* sensor | 指向传感器信息的指针。 |
| int64_t *minSamplingInterval | 指向最小数据报告间隔的指针，以纳秒为单位。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorInfo_GetMaxSamplingInterval()**

```ets
int32_t OH_SensorInfo_GetMaxSamplingInterval(Sensor_Info* sensor, int64_t *maxSamplingInterval)
```

描述

获取传感器的最大数据上报间隔时间。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Info* sensor | 指向传感器信息的指针。 |
| int64_t *maxSamplingInterval | 指向最大数据报告间隔的指针，单位为纳秒。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorEvent_GetType()**

```ets
int32_t OH_SensorEvent_GetType(Sensor_Event* sensorEvent, Sensor_Type *sensorType)
```

描述

获取传感器类型。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Event* sensorEvent | 指向传感器数据信息的指针。 |
| Sensor_Type *sensorType | 指向传感器类型的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorEvent_GetTimestamp()**

```ets
int32_t OH_SensorEvent_GetTimestamp(Sensor_Event* sensorEvent, int64_t *timestamp)
```

描述

获取传感器数据的时间戳。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Event* sensorEvent | 指向传感器数据信息的指针。 |
| int64_t *timestamp | 时间戳指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorEvent_GetAccuracy()**

```ets
int32_t OH_SensorEvent_GetAccuracy(Sensor_Event* sensorEvent, Sensor_Accuracy *accuracy)
```

描述

获取传感器数据的精度。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Event* sensorEvent | 指向传感器数据信息的指针。 |
| Sensor_Accuracy *accuracy | 指向精度的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorEvent_GetData()**

```ets
int32_t OH_SensorEvent_GetData(Sensor_Event* sensorEvent, float **data, uint32_t *length)
```

描述

获取传感器数据。数据的长度和内容依赖于监听的传感器类型，传感器上报的数据格式如下：SENSOR_TYPE_ACCELEROMETER: data[0]、data[1]、data[2]分别表示设备x、y、z轴的加速度分量，单位m/s2。SENSOR_TYPE_GYROSCOPE: data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角速度，单位弧度/s。SENSOR_TYPE_AMBIENT_LIGHT: data[0]表示环境光强度，单位勒克斯；从api版本12开始，将返回两个额外的数据，其中data[1]表示色温，单位为开尔文；data[2]表示红外亮度，单位cd/m2。SENSOR_TYPE_MAGNETIC_FIELD: data[0]、data[1]、data[2]分别表示设备x、y、z轴的地磁分量，单位微特斯拉。SENSOR_TYPE_BAROMETER：data[0]表示气压值，单位hPa。SENSOR_TYPE_HALL: data[0]表示皮套吸合状态，0表示打开，大于0表示吸附。SENSOR_TYPE_PROXIMITY：data[0]表示接近状态，0表示接近，大于0表示远离。SENSOR_TYPE_ORIENTATION:data[0]、data[1]、data[2]分别表示设备绕z、x、y轴的角度，单位度。SENSOR_TYPE_GRAVITY：data[0]、data[1]、data[2]分别表示设备x、y、z轴的重力加速度分量，单位m/s2。SENSOR_TYPE_ROTATION_VECTOR:data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角度，单位度，data[3]表示旋转向量元素。SENSOR_TYPE_PEDOMETER_DETECTION:data[0]表示几步检测状态，1表示检测到了步数变化。SENSOR_TYPE_PEDOMETER:data[0]表示步数。SENSOR_TYPE_HEART_RATE：data[0]表示心率数值。SENSOR_TYPE_LINEAR_ACCELERATION：从api版本13开始支持。data[0]，data[1]，data[2]，表示分别绕设备的x、y、z轴的线性加速度，单位为m/s2。SENSOR_TYPE_GAME_ROTATION_VECTOR：从api版本13支持。data[0]，data[1]和data[2]，表示设备分别围绕x、y、z轴的旋转角度，单位为度。data[3]表示旋转向量。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Event* sensorEvent | 传感器数据信息。 |
| float **data | 出参，传感器数据。 |
| uint32_t *length | 出参，数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_Sensor_CreateSubscriptionId()**

```ets
Sensor_SubscriptionId *OH_Sensor_CreateSubscriptionId(void)
```

描述

创建一个[Sensor_SubscriptionId](Sensor_SubscriptionId.md)实例。

起始版本： 11

返回：

| 类型 | 说明 |
| --- | --- |
| Sensor_SubscriptionId * | 如果操作成功，返回指向Sensor_SubscriptionId实例的指针;否则返回NULL。 |

**OH_Sensor_DestroySubscriptionId()**

```ets
int32_t OH_Sensor_DestroySubscriptionId(Sensor_SubscriptionId *id)
```

描述

销毁[Sensor_SubscriptionId](Sensor_SubscriptionId.md)实例并回收内存。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_SubscriptionId *id | 指向Sensor_SubscriptionId实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorSubscriptionId_GetType()**

```ets
int32_t OH_SensorSubscriptionId_GetType(Sensor_SubscriptionId* id, Sensor_Type *sensorType)
```

描述

获取传感器类型。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_SubscriptionId* id | 指向传感器订阅ID的指针。 |
| Sensor_Type *sensorType | 指向传感器类型的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorSubscriptionId_SetType()**

```ets
int32_t OH_SensorSubscriptionId_SetType(Sensor_SubscriptionId* id, const Sensor_Type sensorType)
```

描述

设置传感器类型。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_SubscriptionId* id | 指向传感器订阅ID的指针。 |
| const Sensor_Type sensorType | 要设置的传感器类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_Sensor_CreateSubscriptionAttribute()**

```ets
Sensor_SubscriptionAttribute *OH_Sensor_CreateSubscriptionAttribute(void)
```

描述

创建[Sensor_SubscriptionAttribute](Sensor_SubscriptionAttribute.md)实例。

起始版本： 11

返回：

| 类型 | 说明 |
| --- | --- |
| Sensor_SubscriptionAttribute * | 如果操作成功，返回指向Sensor_SubscriptionAttribute实例的指针；否则返回NULL。 |

**OH_Sensor_DestroySubscriptionAttribute()**

```ets
int32_t OH_Sensor_DestroySubscriptionAttribute(Sensor_SubscriptionAttribute *attribute)
```

描述

销毁[Sensor_SubscriptionAttribute](Sensor_SubscriptionAttribute.md)实例并回收内存。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_SubscriptionAttribute *attribute | 指向Sensor_SubscriptionAttribute实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorSubscriptionAttribute_SetSamplingInterval()**

```ets
int32_t OH_SensorSubscriptionAttribute_SetSamplingInterval(Sensor_SubscriptionAttribute* attribute, const int64_t samplingInterval)
```

描述

设置传感器数据报告间隔。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_SubscriptionAttribute* attribute | 指向传感器订阅属性的指针。 |
| const int64_t samplingInterval | 要设置的数据报告间隔，以纳秒为单位。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorSubscriptionAttribute_GetSamplingInterval()**

```ets
int32_t OH_SensorSubscriptionAttribute_GetSamplingInterval(Sensor_SubscriptionAttribute* attribute, int64_t *samplingInterval)
```

描述

获取传感器数据报告间隔。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_SubscriptionAttribute* attribute | 指向传感器订阅属性的指针。 |
| int64_t *samplingInterval | 指向数据报告间隔的指针，以纳秒为单位。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**Sensor_EventCallback()**

```ets
typedef void (*Sensor_EventCallback)(Sensor_Event *event)
```

描述

定义用于报告传感器数据的回调函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Event* event | 指向传感器数据信息的指针。 |

**OH_Sensor_CreateSubscriber()**

```ets
Sensor_Subscriber *OH_Sensor_CreateSubscriber(void)
```

描述

创建一个[Sensor_Subscriber](Sensor_Subscriber.md)实例。

起始版本： 11

返回：

| 类型 | 说明 |
| --- | --- |
| Sensor_Subscriber * | 如果操作成功，返回指向Sensor_Subscriber实例的指针;否则返回NULL。 |

**OH_Sensor_DestroySubscriber()**

```ets
int32_t OH_Sensor_DestroySubscriber(Sensor_Subscriber *subscriber)
```

描述

销毁[Sensor_Subscriber](Sensor_Subscriber.md)实例并回收内存。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Subscriber *subscriber | 指向Sensor_Subscriber实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorSubscriber_SetCallback()**

```ets
int32_t OH_SensorSubscriber_SetCallback(Sensor_Subscriber* subscriber, const Sensor_EventCallback callback)
```

描述

设置一个回调函数来报告传感器数据。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Subscriber* subscriber | 指向传感器订阅者信息的指针。 |
| const Sensor_EventCallback callback | 设置回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |

**OH_SensorSubscriber_GetCallback()**

```ets
int32_t OH_SensorSubscriber_GetCallback(Sensor_Subscriber* subscriber, Sensor_EventCallback *callback)
```

描述

获取用于报告传感器数据的回调函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Sensor_Subscriber* subscriber | 指向传感器订阅者信息的指针。 |
| Sensor_EventCallback *callback | 指向回调函数的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功返回SENSOR_SUCCESS；否则返回Sensor_Result中定义的错误代码。 |