# ArkUI_ContextCallback

```ets
typedef struct {...} ArkUI_ContextCallback
```

#### 概述

事件回调类型。

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](../system-services/ArkUI_NativeModule.md)

**所在头文件：**[native_type.h](../../capi/headers/native_type.h.md)

#### 汇总

#### 成员变量

名称描述void* userData自定义类型。

#### 成员函数

名称描述[void (*callback)(void* userData)](#ZH-CN_TOPIC_0000002497445144__callback)事件回调。

#### 成员函数说明

#### callback()

```ets
void (*callback)(void* userData)
```

**描述：**

事件回调。