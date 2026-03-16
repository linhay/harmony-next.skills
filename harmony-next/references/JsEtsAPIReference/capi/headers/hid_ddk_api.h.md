# hid_ddk_api.h

#### 概述

声明主机侧访问输入设备的HID DDK接口。

**引用文件：** <hid/hid_ddk_api.h>

**库：** libhid.z.so

**系统能力：** SystemCapability.Driver.HID.Extension

**起始版本：** 11

**相关模块：**[HidDdk](../../topics/misc/HidDdk.md)

#### 汇总

#### 函数

名称描述[int32_t OH_Hid_CreateDevice(Hid_Device *hidDevice, Hid_EventProperties *hidEventProperties)](#ZH-CN_TOPIC_0000002529285601__oh_hid_createdevice)创建设备。[int32_t OH_Hid_EmitEvent(int32_t deviceId, const Hid_EmitItem items[], uint16_t length)](#ZH-CN_TOPIC_0000002529285601__oh_hid_emitevent)向指定设备发送事件列表。[int32_t OH_Hid_DestroyDevice(int32_t deviceId)](#ZH-CN_TOPIC_0000002529285601__oh_hid_destroydevice)销毁设备。[int32_t OH_Hid_Init(void)](#ZH-CN_TOPIC_0000002529285601__oh_hid_init)初始化HID DDK。[int32_t OH_Hid_Release(void)](#ZH-CN_TOPIC_0000002529285601__oh_hid_release)释放HID DDK。[int32_t OH_Hid_Open(uint64_t deviceId, uint8_t interfaceIndex, Hid_DeviceHandle **dev)](#ZH-CN_TOPIC_0000002529285601__oh_hid_open)打开deviceId和interfaceIndex指定的设备。[int32_t OH_Hid_Close(Hid_DeviceHandle **dev)](#ZH-CN_TOPIC_0000002529285601__oh_hid_close)关闭设备。[int32_t OH_Hid_Write(Hid_DeviceHandle *dev, uint8_t *data, uint32_t length, uint32_t *bytesWritten)](#ZH-CN_TOPIC_0000002529285601__oh_hid_write)向设备写入报告。[int32_t OH_Hid_ReadTimeout(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize, int timeout, uint32_t *bytesRead)](#ZH-CN_TOPIC_0000002529285601__oh_hid_readtimeout)在指定的超时时间内从设备读取报告。[int32_t OH_Hid_Read(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize, uint32_t *bytesRead)](#ZH-CN_TOPIC_0000002529285601__oh_hid_read)从设备读取报告，默认为阻塞模式（阻塞等待直到有数据可读取），可以调用[OH_Hid_SetNonBlocking](hid_ddk_api.h.md#ZH-CN_TOPIC_0000002529285601__oh_hid_setnonblocking)改变模式。[int32_t OH_Hid_SetNonBlocking(Hid_DeviceHandle *dev, int nonBlock)](#ZH-CN_TOPIC_0000002529285601__oh_hid_setnonblocking)设置设备读取模式为非阻塞。[int32_t OH_Hid_GetRawInfo(Hid_DeviceHandle *dev, Hid_RawDevInfo *rawDevInfo)](#ZH-CN_TOPIC_0000002529285601__oh_hid_getrawinfo)获取设备原始信息。[int32_t OH_Hid_GetRawName(Hid_DeviceHandle *dev, char *data, uint32_t bufSize)](#ZH-CN_TOPIC_0000002529285601__oh_hid_getrawname)获取设备原始名称。[int32_t OH_Hid_GetPhysicalAddress(Hid_DeviceHandle *dev, char *data, uint32_t bufSize)](#ZH-CN_TOPIC_0000002529285601__oh_hid_getphysicaladdress)获取设备物理地址。[int32_t OH_Hid_GetRawUniqueId(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize)](#ZH-CN_TOPIC_0000002529285601__oh_hid_getrawuniqueid)获取设备原始唯一标识符。[int32_t OH_Hid_SendReport(Hid_DeviceHandle *dev, Hid_ReportType reportType, const uint8_t *data, uint32_t length)](#ZH-CN_TOPIC_0000002529285601__oh_hid_sendreport)向设备发送报告。[int32_t OH_Hid_GetReport(Hid_DeviceHandle *dev, Hid_ReportType reportType, uint8_t *data, uint32_t bufSize)](#ZH-CN_TOPIC_0000002529285601__oh_hid_getreport)获取设备报告。[int32_t OH_Hid_GetReportDescriptor(Hid_DeviceHandle *dev, uint8_t *buf, uint32_t bufSize, uint32_t *bytesRead)](#ZH-CN_TOPIC_0000002529285601__oh_hid_getreportdescriptor)获取设备报告描述符。

#### 函数说明

#### OH_Hid_CreateDevice()

```ets
int32_t OH_Hid_CreateDevice(Hid_Device *hidDevice, Hid_EventProperties *hidEventProperties)
```

**描述**

创建设备。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 11

**参数：**

参数项描述[Hid_Device](../../topics/system-services/Hid_Device.md) *hidDevice创建设备需要的基本信息，包括设备名、厂商ID、产品ID等。[Hid_EventProperties](../../topics/misc/Hid_EventProperties.md) *hidEventProperties创建的设备关注的事件，包括事件类型、按键事件属性、绝对坐标事件属性、相对坐标事件属性等。

**返回：**

类型说明int32_t

deviceID (一个非负的数字) 调用接口成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 连接hid_ddk服务失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能的原因：1. 入参hidDevice为空指针;

 2. 入参hidEventProperties为空指针; 3. properties的长度超过7; 4. hidEventTypes的长度超过5;

 5. hidKeys的长度超过100; 6. hidAbs的长度超过26; 7.hidRelBits的长度超过13;

 8. hidMiscellaneous的长度超过6。

[HID_DDK_FAILURE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 设备数量达到最大值200。

#### OH_Hid_EmitEvent()

```ets
int32_t OH_Hid_EmitEvent(int32_t deviceId, const Hid_EmitItem items[], uint16_t length)
```

**描述**

向指定设备发送事件列表。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 11

**参数：**

参数项描述int32_t deviceId设备ID。items发送的事件列表，事件包括类型（取值来源事件类型Hid_EventType）、编码（取值来源同步事件编码Hid_SynEvent、键值编码Hid_KeyCode、按钮编码HidBtnCode、绝对坐标编码Hid_AbsAxes、相对坐标编码Hid_RelAxes、其它类型的输入事件编码Hid_MscEvent）、值（根据实际设备输入决定）。uint16_t length发送事件列表长度（一次发送事件个数）。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 调用接口成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 连接hid_ddk服务失败或者调用方不是设备的创建者。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能的原因: 1.设备ID小于0;

 2.入参length长度超过7; 3.入参items为空指针。

[HID_DDK_NULL_PTR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 对应设备的注入为空。

[HID_DDK_FAILURE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 对应设备不存在。

#### OH_Hid_DestroyDevice()

```ets
int32_t OH_Hid_DestroyDevice(int32_t deviceId)
```

**描述**

销毁设备。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 11

**参数：**

参数项描述int32_t deviceId设备ID。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 调用接口成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 连接hid_ddk服务失败或者调用方不是设备的创建者。

[HID_DDK_FAILURE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 对应设备不存在。

#### OH_Hid_Init()

```ets
int32_t OH_Hid_Init(void)
```

**描述**

初始化HID DDK。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 初始化DDK失败。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

#### OH_Hid_Release()

```ets
int32_t OH_Hid_Release(void)
```

**描述**

释放HID DDK。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

#### OH_Hid_Open()

```ets
int32_t OH_Hid_Open(uint64_t deviceId, uint8_t interfaceIndex, Hid_DeviceHandle **dev)
```

**描述**

打开deviceId和interfaceIndex指定的设备。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述uint64_t deviceId操作设备的ID。uint8_t interfaceIndex接口索引，对应HID设备的接口。[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) **dev设备操作句柄。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) dev内存申请失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) dev为空。

[HID_DDK_DEVICE_NOT_FOUND](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 根据deviceId和interfaceIndex找不到设备。

#### OH_Hid_Close()

```ets
int32_t OH_Hid_Close(Hid_DeviceHandle **dev)
```

**描述**

关闭设备。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) **dev设备操作句柄。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) dev为空。

#### OH_Hid_Write()

```ets
int32_t OH_Hid_Write(Hid_DeviceHandle *dev, uint8_t *data, uint32_t length, uint32_t *bytesWritten)
```

**描述**

向设备写入报告。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。uint8_t *data待写入的数据。uint32_t length写入数据的字节长度，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。uint32_t *bytesWritten实际写入的数据字节数。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. length为0；4. length超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)；

 5. bytesWritten为空。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

#### OH_Hid_ReadTimeout()

```ets
int32_t OH_Hid_ReadTimeout(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize, int timeout, uint32_t *bytesRead)
```

**描述**

在指定的超时时间内从设备读取报告。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。uint8_t *data存放读取数据的缓冲区。uint32_t bufSize存放读取数据的缓冲区大小，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。int timeout超时时间（毫秒）或-1表示阻塞等待。uint32_t *bytesRead读取的字节数。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. bufSize为0；4. bufSize超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)；

 5. bytesRead为空。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 内存数据拷贝失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_TIMEOUT](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 读取超时。

#### OH_Hid_Read()

```ets
int32_t OH_Hid_Read(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize, uint32_t *bytesRead)
```

**描述**

从设备读取报告，默认为阻塞模式（阻塞等待直到有数据可读取），可以调用[OH_Hid_SetNonBlocking](hid_ddk_api.h.md#ZH-CN_TOPIC_0000002529285601__oh_hid_setnonblocking)改变模式。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。uint8_t *data存放读取数据的缓冲区。uint32_t bufSize存放读取数据的缓冲区大小，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。uint32_t *bytesRead读取的字节数。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. bufSize为0；4. bufSize超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)；

 5.bytesRead为空。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 内存数据拷贝失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_TIMEOUT](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 读取超时。

#### OH_Hid_SetNonBlocking()

```ets
int32_t OH_Hid_SetNonBlocking(Hid_DeviceHandle *dev, int nonBlock)
```

**描述**

设置设备读取模式为非阻塞。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。int nonBlock

是否启用非阻塞模式读取数据。1: 启用非阻塞模式，调用[OH_Hid_Read](hid_ddk_api.h.md#ZH-CN_TOPIC_0000002529285601__oh_hid_read)接口时，如果设备有可读的数据，读取并返回[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode)，

 如果设备没有数据可读，则返回[HID_DDK_TIMEOUT](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode)。0: 禁用非阻塞模式。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. nonBlock不是1或0。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

#### OH_Hid_GetRawInfo()

```ets
int32_t OH_Hid_GetRawInfo(Hid_DeviceHandle *dev, Hid_RawDevInfo *rawDevInfo)
```

**描述**

获取设备原始信息。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。[Hid_RawDevInfo](../../topics/misc/Hid_RawDevInfo.md) *rawDevInfo设备原始信息，包含供应商ID、产品ID和总线类型。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. rawDevInfo为空。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 不支持此操作。

#### OH_Hid_GetRawName()

```ets
int32_t OH_Hid_GetRawName(Hid_DeviceHandle *dev, char *data, uint32_t bufSize)
```

**描述**

获取设备原始名称。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。char *data存放读取数据的缓冲区。uint32_t bufSize存放读取数据的缓冲区大小，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. bufSize为0；4. bufSize超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 内存数据拷贝失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 不支持此操作。

#### OH_Hid_GetPhysicalAddress()

```ets
int32_t OH_Hid_GetPhysicalAddress(Hid_DeviceHandle *dev, char *data, uint32_t bufSize)
```

**描述**

获取设备物理地址。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。char *data存放读取数据的缓冲区。uint32_t bufSize存放读取数据的缓冲区大小，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. bufSize为0；4. bufSize超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 内存数据拷贝失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 不支持此操作。

#### OH_Hid_GetRawUniqueId()

```ets
int32_t OH_Hid_GetRawUniqueId(Hid_DeviceHandle *dev, uint8_t *data, uint32_t bufSize)
```

**描述**

获取设备原始唯一标识符。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。uint8_t *data存放读取数据的缓冲区。uint32_t bufSize存放读取数据的缓冲区大小，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. bufSize为0；4. bufSize超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 内存数据拷贝失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 不支持此操作。

#### OH_Hid_SendReport()

```ets
int32_t OH_Hid_SendReport(Hid_DeviceHandle *dev, Hid_ReportType reportType, const uint8_t *data, uint32_t length)
```

**描述**

向设备发送报告。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。[Hid_ReportType](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_reporttype) reportType报告类型。const uint8_t *data待发送的数据。uint32_t length发送数据的字节长度，最大不超过 [HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. length为0；4. length超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 不支持此操作。

#### OH_Hid_GetReport()

```ets
int32_t OH_Hid_GetReport(Hid_DeviceHandle *dev, Hid_ReportType reportType, uint8_t *data, uint32_t bufSize)
```

**描述**

获取设备报告。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。[Hid_ReportType](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_reporttype) reportType报告类型。uint8_t *data存放读取数据的缓冲区。uint32_t bufSize存放读取数据的缓冲区大小，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. data为空；3. bufSize为0；4. bufSize超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 内存数据拷贝失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 不支持此操作。

#### OH_Hid_GetReportDescriptor()

```ets
int32_t OH_Hid_GetReportDescriptor(Hid_DeviceHandle *dev, uint8_t *buf, uint32_t bufSize, uint32_t *bytesRead)
```

**描述**

获取设备报告描述符。

**需要权限：** ohos.permission.ACCESS_DDK_HID

**起始版本：** 18

**参数：**

参数项描述[Hid_DeviceHandle](../../topics/system-services/Hid_DeviceHandle.md) *dev设备操作句柄。uint8_t *buf存放描述符的缓冲区。uint32_t bufSize缓冲区的字节大小，最大不超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)。uint32_t *bytesRead读取的字节数。

**返回：**

类型说明int32_t

[HID_DDK_SUCCESS](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 操作成功。

[HID_DDK_NO_PERM](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 权限校验失败。

[HID_DDK_INVALID_PARAMETER](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 参数校验失败。可能原因：1. dev为空；

 2. buf为空；3. bufSize为0；4. bufSize超过[HID_MAX_REPORT_BUFFER_SIZE](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_max_report_buffer_size)；

 5. bytesRead为空。

[HID_DDK_INIT_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) DDK未初始化。

[HID_DDK_SERVICE_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 与DDK服务通信失败。

[HID_DDK_MEMORY_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 内存数据拷贝失败。

[HID_DDK_IO_ERROR](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) I/O操作失败。

[HID_DDK_INVALID_OPERATION](hid_ddk_types.h.md#ZH-CN_TOPIC_0000002529445575__hid_ddkerrcode) 不支持此操作。