# OH_VObject

```ets
typedef struct {...} OH_VObject
```

#### 概述

表示允许的数据字段类型。

**起始版本：** 10

**相关模块：**[RDB](RDB.md)

**所在头文件：**[oh_value_object.h](oh_value_object.h.md)

#### 汇总

#### 成员变量

名称描述int64_t idOH_VObject结构体的唯一标识符。

#### 成员函数

名称描述[int (*putInt64)(OH_VObject *valueObject, int64_t *value, uint32_t count)](#ZH-CN_TOPIC_0000002497444732__putint64)将int64类型的单个参数或者数组转换为OH_VObject类型的值。[int (*putDouble)(OH_VObject *valueObject, double *value, uint32_t count)](#ZH-CN_TOPIC_0000002497444732__putdouble)将double类型的单个参数或者数组转换为OH_VObject类型的值。[int (*putText)(OH_VObject *valueObject, const char *value)](#ZH-CN_TOPIC_0000002497444732__puttext)将char *类型的字符数组转换为OH_VObject类型的值。[int (*putTexts)(OH_VObject *valueObject, const char **value, uint32_t count)](#ZH-CN_TOPIC_0000002497444732__puttexts)将char *类型的字符串数组转换为OH_VObject类型的值。[int (*destroy)(OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497444732__destroy)销毁OH_VObject对象，并回收该对象占用的内存。

#### 成员函数说明

#### putInt64()

```ets
int (*putInt64)(OH_VObject *valueObject, int64_t *value, uint32_t count)
```

**描述**

将int64类型的单个参数或者数组转换为OH_VObject类型的值。

**起始版本：** 10

**参数：**

参数项描述OH_VObject *valueObject表示指向OH_VObject实例的指针。int64_t *value表示指向int64_t类型的单个参数或者数组的指针。uint32_t count如果value是指向单个数值的指针，则count = 1；如果value是指向数组的指针，则count是数组的长度。

**返回：**

类型说明int返回操作是否成功，出错时返回对应的错误码。

#### putDouble()

```ets
int (*putDouble)(OH_VObject *valueObject, double *value, uint32_t count)
```

**描述**

将double类型的单个参数或者数组转换为OH_VObject类型的值。

**起始版本：** 10

**参数：**

参数项描述OH_VObject *valueObject表示指向OH_VObject实例的指针。double *value表示指向double类型的单个参数或者数组的指针。uint32_t count如果value是指向单个数值的指针，则count = 1；如果value是指向数组的指针，则count是数组的长度。

**返回：**

类型说明int返回操作是否成功，出错时返回对应的错误码。

#### putText()

```ets
int (*putText)(OH_VObject *valueObject, const char *value)
```

**描述**

将char *类型的字符数组转换为OH_VObject类型的值。

**起始版本：** 10

**参数：**

参数项描述OH_VObject *valueObject表示指向OH_VObject实例的指针。const char *value表示字符数组参数。

**返回：**

类型说明int返回操作是否成功，出错时返回对应的错误码。

#### putTexts()

```ets
int (*putTexts)(OH_VObject *valueObject, const char **value, uint32_t count)
```

**描述**

将char *类型的字符串数组转换为OH_VObject类型的值。

**起始版本：** 10

**参数：**

参数项描述OH_VObject *valueObject表示指向OH_VObject实例的指针。const char **value表示字符串数组参数。uint32_t count表示字符串数组参数value的长度。

**返回：**

类型说明int返回操作是否成功，出错时返回对应的错误码。

#### destroy()

```ets
int (*destroy)(OH_VObject *valueObject)
```

**描述**

销毁OH_VObject对象，并回收该对象占用的内存。

**起始版本：** 10

**参数：**

参数项描述OH_VObject *valueObject表示指向OH_VObject实例的指针。

**返回：**

类型说明int返回操作是否成功，出错时返回对应的错误码。