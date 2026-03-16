# ArkWeb_ProxyObjectWithResult

```ets
typedef struct {...} ArkWeb_ProxyObjectWithResult
```

#### 概述

注入的Proxy对象通用结构体。

**起始版本：** 18

**相关模块：**[Web](web.md)

**所在头文件：**[arkweb_type.h](../../capi/headers/arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述const char* objName注入的对象名。const [ArkWeb_ProxyMethodWithResult](ArkWeb_ProxyMethodWithResult.md)* methodList注入的对象携带的方法结构体数组。size_t size方法结构体数组的长度。