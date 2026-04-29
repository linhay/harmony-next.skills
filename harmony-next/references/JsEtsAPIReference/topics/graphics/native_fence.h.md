# native_fence.h

**概述**

定义获取和使用NativeFence的相关函数。

引用文件： <native_fence/native_fence.h>

库： libnative_fence.so

起始版本： 20

系统能力： SystemCapability.Graphic.Graphic2D.NativeWindow

相关模块： [NativeFence](NativeFence.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| bool OH_NativeFence_IsValid(int fenceFd) | 检查fenceFd是否有效。 |
| bool OH_NativeFence_Wait(int fenceFd, uint32_t timeout) | 阻塞传入的fenceFd。最大阻塞时间由超时参数决定。传入的fenceFd需要用户自己关闭。 |
| bool OH_NativeFence_WaitForever(int fenceFd) | 永久阻塞传入的fenceFd。传入的fenceFd需要用户自己关闭。 |
| void OH_NativeFence_Close(int fenceFd) | 关闭fenceFd。 |

**函数说明**

**OH_NativeFence_IsValid()**

```ets
bool OH_NativeFence_IsValid(int fenceFd)
```

描述

检查fenceFd是否有效。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示fenceFd有效，返回false表示该值是一个负整数。 |

**OH_NativeFence_Wait()**

```ets
bool OH_NativeFence_Wait(int fenceFd, uint32_t timeout)
```

描述

阻塞传入的fenceFd。最大阻塞时间由超时参数决定。传入的fenceFd需要用户自己关闭。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。 |
| uint32_t timeout | 表示等待时间。单位为毫秒，-1表示永久等待，0表示接口立即返回。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示对应的fenceFd有信号触发； 在以下情况会返回false： 1.传入的fenceFd为负整数。 2.在指定的超时时间内无信号触发。 3.调用底层poll接口失败。 4.超时时间设置为0。 5.接口中复制文件描述符执行失败。 |

**OH_NativeFence_WaitForever()**

```ets
bool OH_NativeFence_WaitForever(int fenceFd)
```

描述

永久阻塞传入的fenceFd。传入的fenceFd需要用户自己关闭。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示对应的fenceFd有信号触发； 在以下情况会返回false： 1.传入的fenceFd为负整数。 2.在指定的超时时间内无信号触发，永久等待。 3.接口中复制文件描述符执行失败。 |

**OH_NativeFence_Close()**

```ets
void OH_NativeFence_Close(int fenceFd)
```

描述

关闭fenceFd。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| int fenceFd | 表示一个文件描述符，用于定时同步。该值是一个非负整数。 |