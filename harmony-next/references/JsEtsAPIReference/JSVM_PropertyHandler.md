# JSVM_PropertyHandler

```ets
typedef struct {...} JSVM_PropertyHandler
```

#### 概述

包含将class作为函数进行调用时所触发的回调函数的函数指针，以及访问实例对象属性时触发的回调函数的函数指针集。

**起始版本：** 18

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述[JSVM_PropertyHandlerCfg](JSVM_PropertyHandlerConfigurationStruct_.md) propertyHandlerCfg访问实例对象属性触发相应的回调函数。[JSVM_Callback](JSVM_CallbackStruct_.md) callAsFunctionCallback实例对象作为函数调用将触发此回调。