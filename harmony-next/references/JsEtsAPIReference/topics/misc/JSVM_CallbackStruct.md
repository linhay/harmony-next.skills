# JSVM_CallbackStruct

```ets
typedef struct {...} JSVM_CallbackStruct
```

#### 概述

用户提供的Native回调函数的指针和数据，这些函数通过JSVM-API接口暴露给JavaScript。

**起始版本：** 11

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](../../capi/headers/jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述void* data用户提供的Native回调函数的数据。

#### 成员函数

名称描述[JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env,JSVM_CallbackInfo info)](#ZH-CN_TOPIC_0000002529446129__callback)用户提供的Native回调函数的指针。

#### 成员函数说明

#### callback()

```ets
JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env,JSVM_CallbackInfo info)
```

**描述**

用户提供的Native回调函数的指针。