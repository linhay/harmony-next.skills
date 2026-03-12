# JSVM_PropertyDescriptor

```ets
typedef struct {...} JSVM_PropertyDescriptor
```

#### 概述

属性描述符。

**起始版本：** 11

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述const char* utf8name描述属性键值的可选字符串，UTF-8编码。必须为属性提供utf8name或name之一。[JSVM_Value](JSVM_Value___.md) name可选的JSVM_Value，指向用作属性键的JavaScript字符串或符号。必须为属性提供utf8name或name之一。[JSVM_Callback](JSVM_CallbackStruct_.md) method设置此项使属性描述符对象的value属性成为method表示的JavaScript函数。[JSVM_Callback](JSVM_CallbackStruct_.md) getter执行对属性的获取访问时调用的函数。[JSVM_Callback](JSVM_CallbackStruct_.md) setter执行属性的设置访问时调用的函数。[JSVM_Value](JSVM_Value___.md) value如果属性是数据属性，则通过属性的get访问检索到的值。[JSVM_PropertyAttributes](jsvm_types.h.md#ZH-CN_TOPIC_0000002497446184__jsvm_propertyattributes) attributes与特定属性关联的属性。