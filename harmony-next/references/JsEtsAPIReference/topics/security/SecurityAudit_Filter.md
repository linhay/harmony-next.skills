# SecurityAudit_Filter

#### 概述

提供过滤条件。

**起始版本：** 6.0.0(20)

**相关模块：**[SecurityAudit](SecurityAudit.md)

所在头文件： [security_audit.h](security_audit.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool isInclude | TRUE: 符合条件的事件被返回给客户端。 FALSE: 符合条件的事件不被返回给客户端。 |
| [SecurityAudit_FilterType](SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) type | 过滤器类型。 |
| const char ** value | 事件的过滤器的值。 |
| uint64_t valueCount | 过滤器值的数量。 |

#### 结构体成员变量说明

#### isInclude

```ets
bool SecurityAudit_Filter::isInclude
```

**描述**

TRUE: 符合条件的事件被返回给客户端。 FALSE: 符合条件的事件不被返回给客户端。

#### type

```ets
[SecurityAudit_FilterType](SecurityAudit.md#ZH-CN_TOPIC_0000002482788542__zh-cn_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) SecurityAudit_Filter::type
```

**描述**

过滤器类型。

#### value

```ets
const char** SecurityAudit_Filter::value
```

**描述**

事件的过滤器的值。

#### valueCount

```ets
uint64_t SecurityAudit_Filter::valueCount
```

**描述**

过滤器值的数量。
