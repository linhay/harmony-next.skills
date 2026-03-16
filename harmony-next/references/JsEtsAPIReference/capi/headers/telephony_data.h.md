# telephony_data.h

#### 概述

为电话蜂窝数据定义C接口。

**引用文件：** <telephony/core_service/telephony_radio.h>

**库：** libtelephony_data.so

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 13

**相关模块：**[Telephony](../../topics/misc/Telephony.md)

#### 汇总

#### 函数

名称描述[int32_t OH_Telephony_GetDefaultCellularDataSlotId(void)](#ZH-CN_TOPIC_0000002497445516__oh_telephony_getdefaultcellulardataslotid)获取默认移动数据的SIM卡接口。

#### 函数说明

#### OH_Telephony_GetDefaultCellularDataSlotId()

```ets
int32_t OH_Telephony_GetDefaultCellularDataSlotId(void)
```

**描述**

获取默认移动数据的SIM卡接口。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 13

**返回：**

类型说明int32_t默认移动数据的SIM卡接口 (0 表示卡槽1, 1 表示卡槽2)。