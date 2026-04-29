# ipc_cremote_object.h

**概述**

提供远端对象创建、销毁、数据发送、远端对象死亡状态监听等功能的C接口。

引用文件： <IPCKit/ipc_cremote_object.h>

库： libipc_capi.so

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

相关模块： [OHIPCRemoteObject](OHIPCRemoteObject.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_IPC_MessageOption | - | IPC消息选项定义。 |
| OHIPCDeathRecipient | OHIPCDeathRecipient | 死亡通知对象。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_IPC_RequestMode | OH_IPC_RequestMode | IPC请求模式定义。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef int (*OH_OnRemoteRequestCallback)(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData) | OH_OnRemoteRequestCallback | Stub端用于处理远端数据请求的回调函数。 |
| typedef void (*OH_OnRemoteDestroyCallback)(void *userData) | OH_OnRemoteDestroyCallback | 用于监听对象销毁的回调函数。 |
| OHIPCRemoteStub* OH_IPCRemoteStub_Create(const char *descriptor, OH_OnRemoteRequestCallback requestCallback, OH_OnRemoteDestroyCallback destroyCallback, void *userData) | - | 创建OHIPCRemoteStub对象。 |
| void OH_IPCRemoteStub_Destroy(OHIPCRemoteStub *stub) | - | 销毁OHIPCRemoteStub对象。 |
| void OH_IPCRemoteProxy_Destroy(OHIPCRemoteProxy *proxy) | - | 销毁OHIPCRemoteProxy对象。 |
| int OH_IPCRemoteProxy_SendRequest(const OHIPCRemoteProxy *proxy, uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, const OH_IPC_MessageOption *option) | - | IPC消息发送函数。 |
| int OH_IPCRemoteProxy_GetInterfaceDescriptor(OHIPCRemoteProxy *proxy, char **descriptor, int32_t *len, OH_IPC_MemAllocator allocator) | - | 从Stub端获取接口描述符。 |
| typedef void (*OH_OnDeathRecipientCallback)(void *userData) | OH_OnDeathRecipientCallback | 远端OHIPCRemoteStub对象死亡通知的回调函数类型。 |
| typedef void (*OH_OnDeathRecipientDestroyCallback)(void *userData) | OH_OnDeathRecipientDestroyCallback | OH_OnDeathRecipient对象销毁回调函数类型。 |
| OHIPCDeathRecipient* OH_IPCDeathRecipient_Create(OH_OnDeathRecipientCallback deathRecipientCallback, OH_OnDeathRecipientDestroyCallback destroyCallback, void *userData) | - | 创建OHIPCDeathRecipient对象。 |
| void OH_IPCDeathRecipient_Destroy(OHIPCDeathRecipient *recipient) | - | 销毁OHIPCDeathRecipient对象。 |
| int OH_IPCRemoteProxy_AddDeathRecipient(OHIPCRemoteProxy *proxy, OHIPCDeathRecipient *recipient) | - | 向OHIPCRemoteProxy对象添加死亡监听，用于接收远端OHIPCRemoteStub对象死亡的回调通知。 |
| int OH_IPCRemoteProxy_RemoveDeathRecipient(OHIPCRemoteProxy *proxy, OHIPCDeathRecipient *recipient) | - | 移除向OHIPCRemoteProxy对象已经添加的死亡监听。 |
| int OH_IPCRemoteProxy_IsRemoteDead(const OHIPCRemoteProxy *proxy) | - | 判断OHIPCRemoteProxy对象对应的远端OHIPCRemoteStub对象是否死亡。 |

**枚举类型说明**

**OH_IPC_RequestMode**

```ets
enum OH_IPC_RequestMode
```

描述：

IPC请求模式定义。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| OH_IPC_REQUEST_MODE_SYNC = 0 | 同步请求模式。 |
| OH_IPC_REQUEST_MODE_ASYNC = 1 | 异步请求模式。 |

**函数说明**

**OH_OnRemoteRequestCallback()**

```ets
typedef int(*OH_OnRemoteRequestCallback)(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData)
```

描述：

Stub端用于处理远端数据请求的回调函数。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| uint32_t code | code 用户自定义通讯命令字，范围：[0x01, 0x00ffffff]。 |
| const OHIPCParcel *data | data 请求数据对象指针，不会为空，函数内不允许释放。 |
| OHIPCParcel *reply | reply 回应数据对象指针，不会为空，函数内不允许释放。如果函数返回错误，该值不允许写入数据。 |
| void *userData | userData 用户私有数据，可以为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  否则返回用户自定义错误码或系统错误码，自定义错误码范围：[1909001, 1909999]；  如果用户自定义错误码超出范围，将返回OH_IPC_ErrorCode#OH_IPC_INVALID_USER_ERROR_CODE。 |

**OH_OnRemoteDestroyCallback()**

```ets
typedef void(*OH_OnRemoteDestroyCallback)(void *userData)
```

描述：

用于监听对象销毁的回调函数。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| void *userData | userData 用户私有数据，可以为空。 |

**OH_IPCRemoteStub_Create()**

```ets
OHIPCRemoteStub* OH_IPCRemoteStub_Create(const char *descriptor, OH_OnRemoteRequestCallback requestCallback, OH_OnRemoteDestroyCallback destroyCallback, void *userData)
```

描述：

创建OHIPCRemoteStub对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| const char *descriptor | descriptor OHIPCRemoteStub对象描述符，不能为空。 |
| OH_OnRemoteRequestCallback requestCallback | requestCallback 数据请求处理函数，不能为空。 |
| OH_OnRemoteDestroyCallback destroyCallback | destroyCallback对象销毁回调函数，可以为空。 |
| void *userData | userData用户私有数据，可以为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OHIPCRemoteStub* | 成功返回OHIPCRemoteStub对象指针，否则返回NULL。 |

**OH_IPCRemoteStub_Destroy()**

```ets
void OH_IPCRemoteStub_Destroy(OHIPCRemoteStub *stub)
```

描述：

销毁OHIPCRemoteStub对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| OHIPCRemoteStub *stub | stub 要销毁的OHIPCRemoteStub对象指针。 |

**OH_IPCRemoteProxy_Destroy()**

```ets
void OH_IPCRemoteProxy_Destroy(OHIPCRemoteProxy *proxy)
```

描述：

销毁OHIPCRemoteProxy对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| OHIPCRemoteProxy *proxy | proxy 要销毁的OHIPCRemoteProxy对象指针。 |

**OH_IPCRemoteProxy_SendRequest()**

```ets
int OH_IPCRemoteProxy_SendRequest(const OHIPCRemoteProxy *proxy, uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, const OH_IPC_MessageOption *option)
```

描述：

IPC消息发送函数。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| const OHIPCRemoteProxy *proxy | proxy OHIPCRemoteProxy对象指针，不能为空。 |
| uint32_t code | code 用户定义的IPC命令字，范围：[0x01, 0x00ffffff]。 |
| const OHIPCParcel *data | data 请求数据对象指针，不能为空。 |
| OHIPCParcel *reply | reply 回应数据对象指针，同步请求时，不能为空；异步请求时，可以为空。 |
| const OH_IPC_MessageOption *option | option消息选项指针，可以为空，为空时按同步处理。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 发送成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数不合法时返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  远端OHIPCRemoteStub对象死亡返回OH_IPC_ErrorCode#OH_IPC_DEAD_REMOTE_OBJECT；  code超出范围返回OH_IPC_ErrorCode#OH_IPC_CODE_OUT_OF_RANGE；  其它返回OH_IPC_ErrorCode#OH_IPC_INNER_ERROR或用户自定义错误码。 |

**OH_IPCRemoteProxy_GetInterfaceDescriptor()**

```ets
int OH_IPCRemoteProxy_GetInterfaceDescriptor(OHIPCRemoteProxy *proxy, char **descriptor, int32_t *len, OH_IPC_MemAllocator allocator)
```

描述：

从Stub端获取接口描述符。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| OHIPCRemoteProxy *proxy | proxy OHIPCRemoteProxy对象指针，不能为空。 |
| char **descriptor | descriptor 用于存储描述符的内存地址，该内存由用户提供的分配器进行内存分配，用户使用完后需要主动释放，不能为空。 接口返回失败时，用户依然需要判断该内存是否为空，并主动释放，否则会造成内存泄漏。 |
| int32_t *len | len 写入descriptor的数据长度，包含结束符，不能为空。 |
| OH_IPC_MemAllocator allocator | allocator 用户指定的用来分配descriptor的内存分配器，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 发送成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数错误返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  远端OHIPCRemoteStub对象死亡返回OH_IPC_ErrorCode#OH_IPC_DEAD_REMOTE_OBJECT；  内存分配失败返回OH_IPC_ErrorCode#OH_IPC_MEM_ALLOCATOR_ERROR；  序列化读失败返回OH_IPC_ErrorCode#OH_IPC_PARCEL_READ_ERROR或用户自定义错误码。 |

**OH_OnDeathRecipientCallback()**

```ets
typedef void (*OH_OnDeathRecipientCallback)(void *userData)
```

描述：

远端OHIPCRemoteStub对象死亡通知的回调函数类型。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| void *userData | userData 用户私有数据指针，可以为空。 |

**OH_OnDeathRecipientDestroyCallback()**

```ets
typedef void (*OH_OnDeathRecipientDestroyCallback)(void *userData)
```

描述：

OHIPCDeathRecipient对象销毁回调函数类型。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| void *userData | userData 用户私有数据指针，可以为空。 |

**OH_IPCDeathRecipient_Create()**

```ets
OHIPCDeathRecipient* OH_IPCDeathRecipient_Create(OH_OnDeathRecipientCallback deathRecipientCallback, OH_OnDeathRecipientDestroyCallback destroyCallback, void *userData)
```

描述：

创建远端OHIPCRemoteStub对象死亡通知对象OHIPCDeathRecipient。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| OH_OnDeathRecipientCallback deathRecipientCallback | deathRecipientCallback 远端OHIPCRemoteStub对象死亡通知的回调处理函数，不能为空。 |
| OH_OnDeathRecipientDestroyCallback destroyCallback | destroyCallback 对象销毁回调处理函数，可以为空。 |
| void *userData | userData 用户私有数据指针，可以为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OHIPCDeathRecipient* | 成功返回OHIPCDeathRecipient对象指针；否则返回NULL。 |

**OH_IPCDeathRecipient_Destroy()**

```ets
void OH_IPCDeathRecipient_Destroy(OHIPCDeathRecipient *recipient)
```

描述：

销毁OHIPCDeathRecipient对象。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| OHIPCDeathRecipient *recipient | recipient 要销毁的OHIPCDeathRecipient对象指针。 |

**OH_IPCRemoteProxy_AddDeathRecipient()**

```ets
int OH_IPCRemoteProxy_AddDeathRecipient(OHIPCRemoteProxy *proxy, OHIPCDeathRecipient *recipient)
```

描述：

向OHIPCRemoteProxy对象添加死亡监听，用于接收远端OHIPCRemoteStub对象死亡的回调通知。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| OHIPCRemoteProxy *proxy | proxy 需要添加死亡通知的OHIPCRemoteProxy对象指针，不能为空。 |
| OHIPCDeathRecipient *recipient | recipient 用于接收远程对象死亡通知的死亡对象指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数错误返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  其它返回OH_IPC_ErrorCode#OH_IPC_INNER_ERROR。 |

**OH_IPCRemoteProxy_RemoveDeathRecipient()**

```ets
int OH_IPCRemoteProxy_RemoveDeathRecipient(OHIPCRemoteProxy *proxy, OHIPCDeathRecipient *recipient)
```

描述：

移除向OHIPCRemoteProxy对象已经添加的死亡监听。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| OHIPCRemoteProxy *proxy | proxy 需要移除死亡通知的OHIPCRemoteProxy对象指针，不能为空。 |
| OHIPCDeathRecipient *recipient | recipient用于接收远程对象死亡通知的死亡对象指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 成功返回OH_IPC_ErrorCode#OH_IPC_SUCCESS；  参数错误返回OH_IPC_ErrorCode#OH_IPC_CHECK_PARAM_ERROR；  其它返回OH_IPC_ErrorCode#OH_IPC_INNER_ERROR。 |

**OH_IPCRemoteProxy_IsRemoteDead()**

```ets
int OH_IPCRemoteProxy_IsRemoteDead(const OHIPCRemoteProxy *proxy)
```

描述：

判断OHIPCRemoteProxy对象对应的远端OHIPCRemoteStub对象是否死亡。

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

参数:

| 参数项 | 描述 |
| --- | --- |
| const OHIPCRemoteProxy *proxy | proxy 需要判断远端是否死亡的OHIPCRemoteProxy对象指针，不能为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 远端OHIPCRemoteStub对象死亡返回1；否则，返回0。参数非法时，说明其远端OHIPCRemoteStub对象不存在，返回1。 |