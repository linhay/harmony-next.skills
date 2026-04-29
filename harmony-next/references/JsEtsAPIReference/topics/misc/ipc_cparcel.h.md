# ipc_cparcel.h

**概述**

提供IPC序列化/反序列化C接口。

引用文件： <IPCKit/ipc_cparcel.h>

库： libipc_capi.so

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

相关模块：[OHIPCParcel](OHIPCParcel.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OHIPCParcel | OHIPCParcel | IPC序列化对象。 |
| OHIPCRemoteProxy | OHIPCRemoteProxy | IPC远端代理对象。 |
| OHIPCRemoteStub | OHIPCRemoteStub | IPC远端服务对象。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void* (*OH_IPC_MemAllocator)(int32_t len) | OH_IPC_MemAllocator | 内存分配函数类型。 |
| OHIPCParcel* OH_IPCParcel_Create(void) | - | 创建OHIPCParcel对象，对象可序列化大小不能超过204800字节。 |
| void OH_IPCParcel_Destroy(OHIPCParcel *parcel) | - | 销毁OHIPCParcel对象。 |
| int OH_IPCParcel_GetDataSize(const OHIPCParcel *parcel) | - | 获取OHIPCParcel对象包含的数据的大小。 |
| int OH_IPCParcel_GetWritableBytes(const OHIPCParcel *parcel) | - | 获取OHIPCParcel对象可以写入的字节数。 |
| int OH_IPCParcel_GetReadableBytes(const OHIPCParcel *parcel) | - | 获取OHIPCParcel对象还可以读取的字节数。 |
| int OH_IPCParcel_GetReadPosition(const OHIPCParcel *parcel) | - | 获取OHIPCParcel对象当前读取位置。 |
| int OH_IPCParcel_GetWritePosition(const OHIPCParcel *parcel) | - | 获取OHIPCParcel对象当前写入位置。 |
| int OH_IPCParcel_RewindReadPosition(OHIPCParcel *parcel, uint32_t newReadPos) | - | 重置OHIPCParcel对象读取位置。 |
| int OH_IPCParcel_RewindWritePosition(OHIPCParcel *parcel, uint32_t newWritePos) | - | 重置OHIPCParcel对象写入位置。 |
| int OH_IPCParcel_WriteInt8(OHIPCParcel *parcel, int8_t value) | - | 向OHIPCParcel对象写入一个int8_t值。 |
| int OH_IPCParcel_ReadInt8(const OHIPCParcel *parcel, int8_t *value) | - | 从OHIPCParcel对象中读取一个int8_t值。 |
| int OH_IPCParcel_WriteInt16(OHIPCParcel *parcel, int16_t value) | - | 向OHIPCParcel对象写入一个int16_t值。 |
| int OH_IPCParcel_ReadInt16(const OHIPCParcel *parcel, int16_t *value) | - | 从OHIPCParcel对象中读取一个int16_t值。 |
| int OH_IPCParcel_WriteInt32(OHIPCParcel *parcel, int32_t value) | - | 向OHIPCParcel对象写入一个int32_t值。 |
| int OH_IPCParcel_ReadInt32(const OHIPCParcel *parcel, int32_t *value) | - | 从OHIPCParcel对象中读取一个int32_t值。 |
| int OH_IPCParcel_WriteInt64(OHIPCParcel *parcel, int64_t value) | - | 向OHIPCParcel对象写入一个int64_t值。 |
| int OH_IPCParcel_ReadInt64(const OHIPCParcel *parcel, int64_t *value) | - | 从OHIPCParcel对象中读取一个int64_t值。 |
| int OH_IPCParcel_WriteFloat(OHIPCParcel *parcel, float value) | - | 向OHIPCParcel对象写入一个float值。 |
| int OH_IPCParcel_ReadFloat(const OHIPCParcel *parcel, float *value) | - | 从OHIPCParcel对象中读取一个float值。 |
| int OH_IPCParcel_WriteDouble(OHIPCParcel *parcel, double value) | - | 向OHIPCParcel对象写入一个double值。 |
| int OH_IPCParcel_ReadDouble(const OHIPCParcel *parcel, double *value) | - | 从OHIPCParcel对象中读取一个double值。 |
| int OH_IPCParcel_WriteString(OHIPCParcel *parcel, const char *str) | - | 向OHIPCParcel对象写入字符串，包含字符串结束符。 |
| const char* OH_IPCParcel_ReadString(const OHIPCParcel *parcel) | - | 从OHIPCParcel对象读取字符串，用户可通过strlen获取字符串长度。 |
| int OH_IPCParcel_Writebuffer(OHIPCParcel *parcel, const uint8_t *buffer, int32_t len) | - | 向OHIPCParcel对象写入指定长度的内存信息。 |
| const uint8_t* OH_IPCParcel_ReadBuffer(const OHIPCParcel *parcel, int32_t len) | - | 从OHIPCParcel对象读取指定长度的内存信息。 |
| int OH_IPCParcel_WriteRemoteStub(OHIPCParcel *parcel, const OHIPCRemoteStub *stub) | - | 向OHIPCParcel对象写入OHIPCRemoteStub对象。 |
| OHIPCRemoteStub* OH_IPCParcel_ReadRemoteStub(const OHIPCParcel *parcel) | - | 从OHIPCParcel对象读取OHIPCRemoteStub对象。 |
| int OH_IPCParcel_WriteRemoteProxy(OHIPCParcel *parcel, const OHIPCRemoteProxy *proxy) | - | 向OHIPCParcel对象写入OHIPCRemoteProxy对象。 |
| OHIPCRemoteProxy* OH_IPCParcel_ReadRemoteProxy(const OHIPCParcel *parcel) | - | 从OHIPCParcel对象读取OHIPCRemoteProxy对象。 |
| int OH_IPCParcel_WriteFileDescriptor(OHIPCParcel *parcel, int32_t fd) | - | 向OHIPCParcel对象写入文件描述符。 |
| int OH_IPCParcel_ReadFileDescriptor(const OHIPCParcel *parcel, int32_t *fd) | - | 从OHIPCParcel对象读取文件描述符。 |
| int OH_IPCParcel_Append(OHIPCParcel *parcel, const OHIPCParcel *data) | - | OHIPCParcel对象数据拼接。 |
| int OH_IPCParcel_WriteInterfaceToken(OHIPCParcel *parcel, const char *token) | - | 向OHIPCParcel对象写入接口描述符，用于接口身份校验。 |
| int OH_IPCParcel_ReadInterfaceToken(const OHIPCParcel *parcel, char **token, int32_t *len, OH_IPC_MemAllocator allocator) | - | 从OHIPCParcel对象读取接口描述符信息，用于接口身份校验。 |

**函数说明**

**OH_IPC_MemAllocator()**

```ets
typedef void* (*OH_IPC_MemAllocator)(int32_t len)
```

描述：

内存分配函数类型。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t len | len 申请内存的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| void* | 成功返回分配的内存地址；失败返回NULL。 |

**OH_IPCParcel_Create()**

```ets
OHIPCParcel* OH_IPCParcel_Create(void)
```

描述：

创建OHIPCParcel对象，对象可序列化大小不能超过204800字节。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OHIPCParcel* | 成功返回OHIPCParcel对象指针；失败返回NULL。 |

**OH_IPCParcel_Destroy()**

```ets
void OH_IPCParcel_Destroy(OHIPCParcel *parcel)
```

描述：

销毁OHIPCParcel对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel 需要销毁OHIPCParcel对象的指针。 |

**OH_IPCParcel_GetDataSize()**

```ets
int OH_IPCParcel_GetDataSize(const OHIPCParcel *parcel)
```

描述：

获取OHIPCParcel对象包含的数据的大小。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 描述 |
| --- | --- |
| int | 返回数据大小，参数不合法时返回-1。 |

**OH_IPCParcel_GetWritableBytes()**

```ets
int OH_IPCParcel_GetWritableBytes(const OHIPCParcel *parcel)
```

描述：

获取OHIPCParcel对象可以写入的字节数。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回可写字节数大小，参数不合法时返回-1。 |

**OH_IPCParcel_GetReadableBytes()**

```ets
int OH_IPCParcel_GetReadableBytes(const OHIPCParcel *parcel)
```

描述：

获取OHIPCParcel对象还可以读取的字节数。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回可读字节数大小，参数不合法时返回-1。 |

**OH_IPCParcel_GetReadPosition()**

```ets
int OH_IPCParcel_GetReadPosition(const OHIPCParcel *parcel)
```

描述：

获取OHIPCParcel对象当前读取位置。

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回当前读位置，参数不合法时返回-1。 |

**OH_IPCParcel_GetWritePosition()**

```ets
int OH_IPCParcel_GetWritePosition(const OHIPCParcel *parcel)
```

描述：

获取OHIPCParcel对象当前写入位置。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回当前写入位置，参数不合法时返回-1。 |

**OH_IPCParcel_RewindReadPosition()**

```ets
int OH_IPCParcel_RewindReadPosition(OHIPCParcel *parcel, uint32_t newReadPos)
```

描述：

重置OHIPCParcel对象读取位置。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| uint32_t newReadPos | newReadPos 新的读取位置，范围：[0，当前数据大小]。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR。 |

**OH_IPCParcel_RewindWritePosition()**

```ets
int OH_IPCParcel_RewindWritePosition(OHIPCParcel *parcel, uint32_t newWritePos)
```

描述：

重置OHIPCParcel的写入位置。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| uint32_t newWritePos | newWritePos 新的写入位置，范围：[0, 当前数据大小]。 |

返回：

| 类型 | 描述 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR。 |

**OH_IPCParcel_WriteInt8()**

```ets
int OH_IPCParcel_WriteInt8(OHIPCParcel *parcel, int8_t value)
```

描述：

向OHIPCParcel写入一个int8_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int8_t value | value 要写入的值。 |

返回：

| 返回 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadInt8()**

```ets
int OH_IPCParcel_ReadInt8(const OHIPCParcel *parcel, int8_t *value)
```

描述：

从OHIPCParcel对象中读取int8_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int8_t *value | value 存储读取数据的指针，不能为空。 |

返回：

| 返回 | 描述 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |

**OH_IPCParcel_WriteInt16()**

```ets
int OH_IPCParcel_WriteInt16(OHIPCParcel *parcel, int16_t value)
```

描述：

向OHIPCParcel对象写入int16_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int16_t value | value 要写入的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadInt16()**

```ets
int OH_IPCParcel_ReadInt16(const OHIPCParcel *parcel, int16_t *value)
```

描述：

从OHIPCParcel对象读取int16_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int16_t *value | value 存储读取数据的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |

**OH_IPCParcel_WriteInt32()**

```ets
int OH_IPCParcel_WriteInt32(OHIPCParcel *parcel, int32_t value)
```

描述：

向OHIPCParcel对象写入int32_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int32_t value | value 要写入的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadInt32()**

```ets
int OH_IPCParcel_ReadInt32(const OHIPCParcel *parcel, int32_t *value)
```

描述：

从OHIPCParcel对象读取int32_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int32_t *value | value 存储读取数据的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |

**OH_IPCParcel_WriteInt64()**

```ets
int OH_IPCParcel_WriteInt64(OHIPCParcel *parcel, int64_t value)
```

描述：

向OHIPCParcel对象写入int64_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int64_t value | value 要写入的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadInt64()**

```ets
int OH_IPCParcel_ReadInt64(const OHIPCParcel *parcel, int64_t *value)
```

描述：

从OHIPCParcel对象读取int64_t值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int64_t *value | value 存储读取数据的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |

**OH_IPCParcel_WriteFloat()**

```ets
int OH_IPCParcel_WriteFloat(OHIPCParcel *parcel, float value)
```

描述：

向OHIPCParcel对象写入float值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| float value | value 要写入的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadFloat()**

```ets
int OH_IPCParcel_ReadFloat(const OHIPCParcel *parcel, float *value)
```

描述：

从OHIPCParcel对象读取float值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| float *value | value 存储读取数据的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |

**OH_IPCParcel_WriteDouble()**

```ets
int OH_IPCParcel_WriteDouble(OHIPCParcel *parcel, double value)
```

描述：

向OHIPCParcel对象写入double值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| double value | value 要写入的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadDouble()**

```ets
int OH_IPCParcel_ReadDouble(const OHIPCParcel *parcel, double *value)
```

描述：

从OHIPCParcel对象读取double值。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| double *value | value 存储读取数据的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |

**OH_IPCParcel_WriteString()**

```ets
int OH_IPCParcel_WriteString(OHIPCParcel *parcel, const char *str)
```

描述：

向OHIPCParcel对象写入字符串，包括字符串结束符。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| const char *str | str 写入字符串，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadString()**

```ets
const char* OH_IPCParcel_ReadString(const OHIPCParcel *parcel)
```

描述：

从OHIPCParcel对象读取字符串，用户可通过strlen获取字符串长度。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char* | 成功返回读取字符串地址；参数不合法或读取失败时返回NULL。 |

**OH_IPCParcel_WriteBuffer()**

```ets
int OH_IPCParcel_WriteBuffer(OHIPCParcel *parcel, const uint8_t *buffer, int32_t len)
```

描述：

向OHIPCParcel对象写入指定长度的内存信息。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| const uint8_t *buffer | buffer 写入内存地址信息。 |
| int32_t len | len 写入信息长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadBuffer()**

```ets
const uint8_t* OH_IPCParcel_ReadBuffer(const OHIPCParcel *parcel, int32_t len)
```

描述：

从OHIPCParcel对象读取指定长度内存信息。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int32_t len | len 读取内存的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const uint8_t* | 成功返回读取到的内存地址；参数不合法或len超过parcel可读长度时返回NULL。 |

**OH_IPCParcel_WriteRemoteStub()**

```ets
int OH_IPCParcel_WriteRemoteStub(OHIPCParcel *parcel, const OHIPCRemoteStub *stub)
```

描述：

向OHIPCParcel对象写入OHIPCRemoteStub对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| const OHIPCRemoteStub *stub | stub 需要写入的OHIPCRemoteStub对象指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadRemoteStub()**

```ets
OHIPCRemoteStub* OH_IPCParcel_ReadRemoteStub(const OHIPCParcel *parcel)
```

描述：

从OHIPCParcel对象读取OHIPCRemoteStub对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OHIPCRemoteStub* | 成功返回OHIPCRemoteStub对象指针；失败返回NULL。 |

**OH_IPCParcel_WriteRemoteProxy()**

```ets
int OH_IPCParcel_WriteRemoteProxy(OHIPCParcel *parcel, const OHIPCRemoteProxy *proxy)
```

描述：

向OHIPCParcel对象写入OHIPCRemoteProxy对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| const OHIPCRemoteProxy *proxy | proxy 需要写入的OHIPCRemoteProxy对象指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadRemoteProxy()**

```ets
OHIPCRemoteProxy* OH_IPCParcel_ReadRemoteProxy(const OHIPCParcel *parcel)
```

描述：

从OHIPCParcel对象读取OHIPCRemoteProxy对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OHIPCRemoteProxy* | 成功返回OHIPCRemoteProxy对象指针；失败返回NULL。 |

**OH_IPCParcel_WriteFileDescriptor()**

```ets
int OH_IPCParcel_WriteFileDescriptor(OHIPCParcel *parcel, int32_t fd)
```

描述：

向OHIPCParcel对象写入文件描述符。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int32_t fd | fd 要写入的文件描述符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadFileDescriptor()**

```ets
int OH_IPCParcel_ReadFileDescriptor(const OHIPCParcel *parcel, int32_t *fd)
```

描述：

从OHIPCParcel对象读取文件描述符。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| int32_t *fd | fd 存储读取文件描述符的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |

**OH_IPCParcel_Append()**

```ets
int OH_IPCParcel_Append(OHIPCParcel *parcel, const OHIPCParcel *data)
```

描述：

OHIPCParcel对象数据拼接。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| const OHIPCParcel *data | data 源OHIPCParcel对象的指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  拼接失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_WriteInterfaceToken()**

```ets
int OH_IPCParcel_WriteInterfaceToken(OHIPCParcel *parcel, const char *token)
```

描述：

向OHIPCParcel对象写入接口描述符，用于接口身份校验。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| const char *token | token 需要写入的接口描述符信息，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  写入失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_WRITE_ERROR。 |

**OH_IPCParcel_ReadInterfaceToken()**

```ets
int OH_IPCParcel_ReadInterfaceToken(const OHIPCParcel *parcel, char **token, int32_t *len, OH_IPC_MemAllocator allocator)
```

描述：

从OHIPCParcel对象读取接口描述符信息，用于接口身份校验。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OHIPCParcel *parcel | parcel OHIPCParcel对象的指针，不能为空。 |
| char **token | token 用于存储接口描述符信息的内存地址，该内存由用户提供的分配器进行内存分配，用户使用完后需要主动释放，不能为空。接口返回失败时，用户依然需要判断该内存是否为空，并主动释放，否则会造成内存泄漏。 |
| int32_t *len | len 存储读取接口描述符的长度，包括结束符，不能为空。 |
| OH_IPC_MemAllocator allocator | allocator 用户指定的用来分配token的内存分配器，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；读取失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR。 |