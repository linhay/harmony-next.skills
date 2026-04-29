# HandWrite_HistoricalPoint

#### 概述

定义历史触摸点信息的结构体。

**系统能力：**SystemCapability.Stylus.HandWrite

**起始版本：**6.0.0(20)

**相关模块：**[HandWrite](HandWrite.md)

**所在头文件：**[native_handwrite_api.h](../../topics/misc/[native_handwrite_api.h](native_handwrite_api.h.md).md)

#### 汇总

#### 成员变量

名称

描述

float [x](#section20387061661)

历史触摸点的X坐标，相对于被触摸元素左边缘，单位：像素。

float [y](#section72219335715)

历史触摸点的Y坐标，相对于被触摸元素上边缘，单位：像素。

int64_t [timeStamp](#section12061557279)

当前历史触摸点的时间戳，单位：ns。

float [force](#section3181185590)

当前历史触摸点的压力值。

#### 结构体成员变量说明

#### x

```ets
float HandWrite_HistoricalPoint::x
```

**描述**

历史触摸点的X坐标，相对于被触摸元素左边缘。

#### y

```ets
float HandWrite_HistoricalPoint::y
```

**描述**

历史触摸点的Y坐标，相对于被触摸元素上边缘。

#### timeStamp

```ets
int64_t HandWrite_HistoricalPoint::timeStamp
```

**描述**

当前历史触摸点的时间戳，单位为ns。

#### force

```ets
float HandWrite_HistoricalPoint::force
```

**描述**

当前历史触摸点的压力值。
