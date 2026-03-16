# native_handwrite_api.h

#### 概述

声明用于对外提供手写能力。

**库：**libhandwrite_ndk.z.so

**系统能力****：**SystemCapability.Stylus.Handwrite

**起始版本：**6.0.0(20)

**相关模块：**[HandWrite](../../topics/misc/HandWrite.md)

#### 汇总

#### 结构体

名称

描述

struct [HandWrite_HistoricalPoint](../../topics/misc/HandWrite_HistoricalPoint.md)

定义历史触摸点信息的结构体。

#### 枚举

名称

描述

enum [HandWrite_ErrCode](../../topics/misc/HandWrite.md#section2871102614149) {

E_NO_ERROR = 0,

E_PARAMS = 401,

E_INNER_ERROR = 1010400001

}

定义手写错误码。

#### 函数

名称

函数

int32_t [HMS_HandWrite_GetPredictPoint](../../topics/misc/HandWrite.md#section3513132112183)(const [HandWrite_HistoricalPoint](../../topics/misc/HandWrite_HistoricalPoint.md) *event, int32_t size, float *predictPointX, float *predictPointY)

此接口用于获取预测点。