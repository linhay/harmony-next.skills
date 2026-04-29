# ipc_error_code.h

**概述**

提供IPC错误码定义。

引用文件： <IPCKit/ipc_error_code.h>

库： libipc_capi.so

系统能力： SystemCapability.Communication.IPC.Core

起始版本： 12

相关模块： [OHIPCErrorCode](OHIPCErrorCode.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_IPC_ErrorCode | OH_IPC_ErrorCode | IPC消息选项定义。 |

**枚举类型说明**

**OH_IPC_ErrorCode**

```ets
enum OH_IPC_ErrorCode
```

描述：

IPC错误码定义。

起始版本： 12

| 枚举值 | 描述 |
| --- | --- |
| OH_IPC_SUCCESS = 0 | 执行成功。 |
| OH_IPC_ERROR_CODE_BASE = 1901000 | 错误码区间起始值。 |
| OH_IPC_CHECK_PARAM_ERROR = OH_IPC_ERROR_CODE_BASE | 参数错误。 |
| OH_IPC_PARCEL_WRITE_ERROR = OH_IPC_ERROR_CODE_BASE + 1 | 序列化对象写入数据失败。 |
| OH_IPC_PARCEL_READ_ERROR = OH_IPC_ERROR_CODE_BASE + 2 | 序列化对象读取数据失败。 |
| OH_IPC_MEM_ALLOCATOR_ERROR = OH_IPC_ERROR_CODE_BASE + 3 | 内存分配失败。 |
| OH_IPC_CODE_OUT_OF_RANGE = OH_IPC_ERROR_CODE_BASE + 4 | 命令字超出定义范围[0x01,0x00ffffff]。 |
| OH_IPC_DEAD_REMOTE_OBJECT = OH_IPC_ERROR_CODE_BASE + 5 | 远端对象死亡。 |
| OH_IPC_INVALID_USER_ERROR_CODE = OH_IPC_ERROR_CODE_BASE + 6 | 用户自定义错误码超出范围[1900001, 1999999]。 |
| OH_IPC_INNER_ERROR = OH_IPC_ERROR_CODE_BASE + 7 | IPC内部错误。 |
| OH_IPC_ERROR_CODE_MAX = OH_IPC_ERROR_CODE_BASE + 1000 | 错误码区间最大值。 |
| OH_IPC_USER_ERROR_CODE_MIN = 1909000 | 用户自定义错误码最小值。 |
| OH_IPC_USER_ERROR_CODE_MAX = 1909999 | 用户自定义错误码最大值。 |