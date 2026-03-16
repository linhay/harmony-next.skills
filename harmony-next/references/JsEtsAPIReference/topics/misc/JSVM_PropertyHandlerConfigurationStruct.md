# JSVM_PropertyHandlerConfigurationStruct

```ets
typedef struct {...} JSVM_PropertyHandlerConfigurationStruct
```

#### 概述

当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。

**起始版本：** 12

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](../../capi/headers/jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述[JSVM_Value](JSVM_Value___.md) namedPropertyData命名属性回调使用的数据。[JSVM_Value](JSVM_Value___.md) indexedPropertyData索引属性回调使用的数据。

#### 成员函数

名称描述[JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericnamedpropertygettercallback)通过获取实例对象的命名属性而触发的回调函数。[JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericnamedpropertysettercallback)通过设置实例对象的命名属性而触发的回调函数。[JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericnamedpropertydeletercallback)通过删除实例对象的命名属性而触发的回调函数。[JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericnamedpropertyenumeratorcallback)通过获取对象上的所有命名属性而触发的回调函数。[JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericindexedpropertygettercallback)通过获取实例对象的索引属性而触发的回调函数。[JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericindexedpropertysettercallback)通过设置实例对象的索引属性而触发的回调函数。[JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericindexedpropertydeletercallback)通过删除实例对象的索引属性而触发的回调函数。[JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData)](#ZH-CN_TOPIC_0000002529446133__genericindexedpropertyenumeratorcallback)通过获取对象上的所有索引属性而触发的回调函数。

#### 成员函数说明

#### genericNamedPropertyGetterCallback()

```ets
JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取实例对象的命名属性而触发的回调函数。

#### genericNamedPropertySetterCallback()

```ets
JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过设置实例对象的命名属性而触发的回调函数。

#### genericNamedPropertyDeleterCallback()

```ets
JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过删除实例对象的命名属性而触发的回调函数。

#### genericNamedPropertyEnumeratorCallback()

```ets
JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取对象上的所有命名属性而触发的回调函数。

#### genericIndexedPropertyGetterCallback()

```ets
JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取实例对象的索引属性而触发的回调函数。

#### genericIndexedPropertySetterCallback()

```ets
JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过设置实例对象的索引属性而触发的回调函数。

#### genericIndexedPropertyDeleterCallback()

```ets
JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过删除实例对象的索引属性而触发的回调函数。

#### genericIndexedPropertyEnumeratorCallback()

```ets
JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取对象上的所有索引属性而触发的回调函数。