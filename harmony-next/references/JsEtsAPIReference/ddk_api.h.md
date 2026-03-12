# ddk_api.h

#### 概述

声明主机侧访问的Base DDK接口。

**引用文件：** <ddk/ddk_api.h>

**库：** libddk_base.z.so

**系统能力：** SystemCapability.Driver.DDK.Extension

**起始版本：** 12

**相关模块：**[BaseDdk](BaseDdk.md)

#### 汇总

#### 函数

名称描述[DDK_RetCode OH_DDK_CreateAshmem(const uint8_t *name, uint32_t size, DDK_Ashmem **ashmem)](#ZH-CN_TOPIC_0000002497605608__oh_ddk_createashmem)创建共享内存。为了防止资源泄漏，通过调用**OH_DDK_DestroyAshmem**接口来销毁不再需要的共享内存。[DDK_RetCode OH_DDK_MapAshmem(DDK_Ashmem *ashmem, const uint8_t ashmemMapType)](#ZH-CN_TOPIC_0000002497605608__oh_ddk_mapashmem)映射创建的共享内存到用户空间。通过调用**OH_DDK_UnmapAshmem**接口取消映射不需要的共享内存。[DDK_RetCode OH_DDK_UnmapAshmem(DDK_Ashmem *ashmem)](#ZH-CN_TOPIC_0000002497605608__oh_ddk_unmapashmem)取消映射共享内存。[DDK_RetCode OH_DDK_DestroyAshmem(DDK_Ashmem *ashmem)](#ZH-CN_TOPIC_0000002497605608__oh_ddk_destroyashmem)销毁共享内存。

#### 函数说明

#### OH_DDK_CreateAshmem()

```ets
DDK_RetCode OH_DDK_CreateAshmem(const uint8_t *name, uint32_t size, DDK_Ashmem **ashmem)
```

**描述**

创建共享内存。为了防止资源泄漏，通过调用**OH_DDK_DestroyAshmem**接口来销毁不再需要的共享内存。

**起始版本：** 12

**参数：**

参数项描述const uint8_t *name指向要创建的共享内存的指针。uint32_t size共享内存对应的缓冲区大小。[DDK_Ashmem](DDK_Ashmem.md) **ashmem指向创建的共享内存的指针。

**返回：**

类型说明[DDK_RetCode](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode)

[DDK_SUCCESS](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 调用接口成功。

[DDK_INVALID_PARAMETER](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 入参name为空指针，size的大小为0或者入参ashmem是空指针。

[DDK_FAILURE](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 创建共享内存失败或者创建结构体DDK_Ashmem失败。

#### OH_DDK_MapAshmem()

```ets
DDK_RetCode OH_DDK_MapAshmem(DDK_Ashmem *ashmem, const uint8_t ashmemMapType)
```

**描述**

映射创建的共享内存到用户空间。通过调用**OH_DDK_UnmapAshmem**接口取消映射不需要的共享内存。

**起始版本：** 12

**参数：**

参数项描述[DDK_Ashmem](DDK_Ashmem.md) *ashmem要映射的共享内存指针。const uint8_t ashmemMapType共享内存的保护权限值。

**返回：**

类型说明[DDK_RetCode](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode)

[DDK_SUCCESS](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 调用接口成功。

[DDK_NULL_PTR](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 入参ashmem为空指针。

[DDK_FAILURE](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 共享内存的文件描述符无效。

[DDK_INVALID_OPERATION](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 调用接口MapAshmem失败.

#### OH_DDK_UnmapAshmem()

```ets
DDK_RetCode OH_DDK_UnmapAshmem(DDK_Ashmem *ashmem)
```

**描述**

取消映射共享内存。

**起始版本：** 12

**参数：**

参数项描述[DDK_Ashmem](DDK_Ashmem.md) *ashmem要取消映射的共享内存指针。

**返回：**

类型说明[DDK_RetCode](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode)

[DDK_SUCCESS](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 调用接口成功。

[DDK_NULL_PTR](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 入参ashmem为空指针。

[DDK_FAILURE](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 共享内存的文件描述符无效。

#### OH_DDK_DestroyAshmem()

```ets
DDK_RetCode OH_DDK_DestroyAshmem(DDK_Ashmem *ashmem)
```

**描述**

销毁共享内存。

**起始版本：** 12

**参数：**

参数项描述[DDK_Ashmem](DDK_Ashmem.md) *ashmem要销毁的共享内存指针。

**返回：**

类型说明[DDK_RetCode](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode)

[DDK_SUCCESS](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 调用接口成功。

[DDK_NULL_PTR](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 入参ashmem为空指针。

[DDK_FAILURE](ddk_types.h.md#ZH-CN_TOPIC_0000002497445630__ddk_retcode) 共享内存的文件描述符无效。