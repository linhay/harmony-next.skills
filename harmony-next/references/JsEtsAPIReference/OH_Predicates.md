# OH_Predicates

```ets
typedef struct {...} OH_Predicates
```

#### 概述

表示谓词。

**起始版本：** 10

**相关模块：**[RDB](RDB.md)

**所在头文件：**[oh_predicates.h](oh_predicates.h.md)

#### 成员变量

名称描述int64_t idH_Predicates结构体的唯一标识符。

#### 成员函数

名称描述[OH_Predicates *(*equalTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__equalto)函数指针，配置谓词以匹配数据字段等于指定值的字段。[OH_Predicates *(*notEqualTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__notequalto)

函数指针，配置谓词以匹配数据字段不等于指定值的字段。

该方法等同于SQL语句中的“!=”。

[OH_Predicates *(*beginWrap)(OH_Predicates *predicates)](#ZH-CN_TOPIC_0000002497604710__beginwrap)

函数指针，向谓词添加左括号。

该方法等同于SQL语句中的“(”。

[OH_Predicates *(*endWrap)(OH_Predicates *predicates)](#ZH-CN_TOPIC_0000002497604710__endwrap)

函数指针，向谓词添加右括号。

该方法等同于SQL语句中的“)”。

[OH_Predicates *(*orOperate)(OH_Predicates *predicates)](#ZH-CN_TOPIC_0000002497604710__oroperate)

函数指针，将或条件添加到谓词中。

该方法等同于SQL语句中的“OR”。

[OH_Predicates *(*andOperate)(OH_Predicates *predicates)](#ZH-CN_TOPIC_0000002497604710__andoperate)

函数指针，向谓词添加和条件。

该方法等同于SQL语句中的“AND”。

[OH_Predicates *(*isNull)(OH_Predicates *predicates, const char *field)](#ZH-CN_TOPIC_0000002497604710__isnull)

函数指针，配置谓词以匹配值为null的字段。

该方法等同于SQL语句中的“IS NULL”。

[OH_Predicates *(*isNotNull)(OH_Predicates *predicates, const char *field)](#ZH-CN_TOPIC_0000002497604710__isnotnull)

函数指针，配置谓词以匹配值不为null的指定字段。

该方法等同于SQL语句中的“IS NOT NULL”。

[OH_Predicates *(*like)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__like)

函数指针，配置谓词以匹配数据字段为field且值类似于指定字符串的字段。

该方法等同于SQL语句中的“LIKE”。

[OH_Predicates *(*between)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__between)

函数指针，将谓词配置为匹配数据字段为field且其值在给定范围内的指定字段。

该方法等同于SQL语句中的“BETWEEN”。

[OH_Predicates *(*notBetween)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__notbetween)

函数指针，将谓词配置为匹配数据字段为field且其值超出给定范围内的指定字段。

该方法等同于SQL语句中的“NOT BETWEEN”。

[OH_Predicates *(*greaterThan)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__greaterthan)

函数指针，配置谓词以匹配数据字段为field且值大于指定值valueObject的字段。

该方法等同于SQL语句中的“>”。

[OH_Predicates *(*lessThan)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__lessthan)

函数指针，配置谓词以匹配数据字段为field且值小于指定值valueObject的字段。

该方法等同于SQL语句中的“<”。

[OH_Predicates *(*greaterThanOrEqualTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__greaterthanorequalto)

函数指针，配置谓词以匹配数据字段为field且值大于或等于指定值valueObject的字段。

该方法等同于SQL语句中的“>=”。

[OH_Predicates *(*lessThanOrEqualTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__lessthanorequalto)

函数指针，配置谓词以匹配数据字段为field且值小于或等于指定值valueObject的字段。

该方法等同于SQL语句中的“<=”。

[OH_Predicates *(*orderBy)(OH_Predicates *predicates, const char *field, OH_OrderType type)](#ZH-CN_TOPIC_0000002497604710__orderby)

函数指针，配置谓词以匹配其值按升序或降序排序的列。

该方法等同于SQL语句中的“ORDER BY”。

[OH_Predicates *(*distinct)(OH_Predicates *predicates)](#ZH-CN_TOPIC_0000002497604710__distinct)

函数指针，配置谓词以过滤重复记录并仅保留其中一个。

该方法等同于SQL语句中的“DISTINCT”。

[OH_Predicates *(*limit)(OH_Predicates *predicates, unsigned int value)](#ZH-CN_TOPIC_0000002497604710__limit)

函数指针，设置最大数据记录数的谓词。

该方法等同于SQL语句中的“LIMIT”。

[OH_Predicates *(*offset)(OH_Predicates *predicates, unsigned int rowOffset)](#ZH-CN_TOPIC_0000002497604710__offset)

函数指针，配置谓词以指定返回结果的起始位置。

该方法等同于SQL语句中的“OFFSET”。

[OH_Predicates *(*groupBy)(OH_Predicates *predicates, char const *const *fields, int length)](#ZH-CN_TOPIC_0000002497604710__groupby)

函数指针，配置R谓词按指定列分组查询结果。

该方法等同于SQL语句中的“GROUP BY”。

[OH_Predicates *(*in)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__in)

函数指针，配置谓词以匹配数据字段为field且值在给定范围内的指定字段。

该方法等同于SQL语句中的“IN”。

[OH_Predicates *(*notIn)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)](#ZH-CN_TOPIC_0000002497604710__notin)

函数指针，配置谓词以匹配数据字段为field且值超出给定范围内的指定字段。

该方法等同于SQL语句中的“NOT IN”。

[OH_Predicates *(*clear)(OH_Predicates *predicates)](#ZH-CN_TOPIC_0000002497604710__clear)函数指针，清空谓词。[int (*destroy)(OH_Predicates *predicates)](#ZH-CN_TOPIC_0000002497604710__destroy)销毁OH_Predicates对象，并回收该对象占用的内存。

#### 成员函数说明

#### equalTo()

```ets
OH_Predicates *(*equalTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段等于指定值的字段。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### notEqualTo()

```ets
OH_Predicates *(*notEqualTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段不等于指定值的字段。

该方法等同于SQL语句中的“!=”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### beginWrap()

```ets
OH_Predicates *(*beginWrap)(OH_Predicates *predicates)
```

**描述**

函数指针，向谓词添加左括号。

该方法等同于SQL语句中的“(”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。

**返回：**

类型说明OH_Predicates *返回带有左括号的谓词。

#### endWrap()

```ets
OH_Predicates *(*endWrap)(OH_Predicates *predicates)
```

**描述**

函数指针，向谓词添加右括号。

该方法等同于SQL语句中的“)”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。

**返回：**

类型说明OH_Predicates *返回带有右括号的谓词。

#### orOperate()

```ets
OH_Predicates *(*orOperate)(OH_Predicates *predicates)
```

**描述**

函数指针，将或条件添加到谓词中。

该方法等同于SQL语句中的“OR”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。

**返回：**

类型说明OH_Predicates *返回带有或条件的谓词。

#### andOperate()

```ets
OH_Predicates *(*andOperate)(OH_Predicates *predicates)
```

**描述**

函数指针，向谓词添加和条件。

该方法等同于SQL语句中的“AND”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。

**返回：**

类型说明OH_Predicates *返回带有和条件的谓词。

#### isNull()

```ets
OH_Predicates *(*isNull)(OH_Predicates *predicates, const char *field)
```

**描述**

函数指针，配置谓词以匹配值为null的字段。

该方法等同于SQL语句中的“IS NULL”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### isNotNull()

```ets
OH_Predicates *(*isNotNull)(OH_Predicates *predicates, const char *field)
```

**描述**

函数指针，配置谓词以匹配值不为null的指定字段。

该方法等同于SQL语句中的“IS NOT NULL”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### like()

```ets
OH_Predicates *(*like)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段为field且值类似于指定字符串的字段。

该方法等同于SQL语句中的“LIKE”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### between()

```ets
OH_Predicates *(*between)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，将谓词配置为匹配数据字段为field且其值在给定范围内的指定字段。

该方法等同于SQL语句中的“BETWEEN”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### notBetween()

```ets
OH_Predicates *(*notBetween)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，将谓词配置为匹配数据字段为field且其值超出给定范围内的指定字段。

该方法等同于SQL语句中的“NOT BETWEEN”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### greaterThan()

```ets
OH_Predicates *(*greaterThan)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段为field且值大于指定值valueObject的字段。

该方法等同于SQL语句中的“>”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### lessThan()

```ets
OH_Predicates *(*lessThan)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段为field且值小于指定值valueObject的字段。

该方法等同于SQL语句中的“<”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### greaterThanOrEqualTo()

```ets
OH_Predicates *(*greaterThanOrEqualTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段为field且值大于或等于指定值valueObject的字段。

该方法等同于SQL语句中的“>=”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### lessThanOrEqualTo()

```ets
OH_Predicates *(*lessThanOrEqualTo)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段为field且值小于或等于指定值valueObject的字段。

该方法等同于SQL语句中的“<=”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。OH_VObject *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### orderBy()

```ets
OH_Predicates *(*orderBy)(OH_Predicates *predicates, const char *field, OH_OrderType type)
```

**描述**

函数指针，配置谓词以匹配其值按升序或降序排序的列。

该方法等同于SQL语句中的“ORDER BY”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field数据库表中的列名。[OH_VObject](OH_VObject.md) type表示排序类型[OH_VObject](OH_VObject.md)。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### distinct()

```ets
OH_Predicates *(*distinct)(OH_Predicates *predicates)
```

**描述**

函数指针，配置谓词以过滤重复记录并仅保留其中一个。

该方法等同于SQL语句中的“DISTINCT”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。

**返回：**

类型说明OH_Predicates *返回可用于过滤重复记录的谓词。

#### limit()

```ets
OH_Predicates *(*limit)(OH_Predicates *predicates, unsigned int value)
```

**描述**

函数指针，设置最大数据记录数的谓词。

该方法等同于SQL语句中的“LIMIT”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。unsigned int value表示最大数据记录数。

**返回：**

类型说明OH_Predicates *返回可用于设置最大数据记录数的谓词。

#### offset()

```ets
OH_Predicates *(*offset)(OH_Predicates *predicates, unsigned int rowOffset)
```

**描述**

函数指针，配置谓词以指定返回结果的起始位置。

该方法等同于SQL语句中的“OFFSET”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。unsigned int rowOffset返回结果的起始位置，取值为正整数。

**返回：**

类型说明OH_Predicates *返回具有指定返回结果起始位置的谓词。

#### groupBy()

```ets
OH_Predicates *(*groupBy)(OH_Predicates *predicates, char const *const *fields, int length)
```

**描述**

函数指针，配置R谓词按指定列分组查询结果。

该方法等同于SQL语句中的“GROUP BY”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。char const *const *fields指定分组依赖的列名。int length该参数为输入参数，表示开发者传入的fields数值的长度。

**返回：**

类型说明OH_Predicates *返回分组查询列的谓词。

#### in()

```ets
OH_Predicates *(*in)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段为field且值在给定范围内的指定字段。

该方法等同于SQL语句中的“IN”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field表示数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### notIn()

```ets
OH_Predicates *(*notIn)(OH_Predicates *predicates, const char *field, OH_VObject *valueObject)
```

**描述**

函数指针，配置谓词以匹配数据字段为field且值超出给定范围内的指定字段。

该方法等同于SQL语句中的“NOT IN”。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。const char *field表示数据库表中的列名。[OH_VObject](OH_VObject.md) *valueObject表示指向[OH_VObject](OH_VObject.md)实例的指针，指示要与谓词匹配的值。

**返回：**

类型说明OH_Predicates *返回与指定字段匹配的谓词。

#### clear()

```ets
OH_Predicates *(*clear)(OH_Predicates *predicates)
```

**描述**

函数指针，清空谓词。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。

**返回：**

类型说明OH_Predicates *返回清空后的谓词。

#### destroy()

```ets
int (*destroy)(OH_Predicates *predicates)
```

**描述**

销毁OH_Predicates对象，并回收该对象占用的内存。

**起始版本：** 10

**参数：**

参数项描述OH_Predicates *predicates表示指向OH_Predicates实例的指针。

**返回：**

类型说明int返回操作是否成功，出错时返回对应的错误码。