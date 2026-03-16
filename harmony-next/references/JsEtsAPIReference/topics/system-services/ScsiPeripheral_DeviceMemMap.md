# ScsiPeripheral_DeviceMemMap

```ets
typedef struct ScsiPeripheral_DeviceMemMap {...} ScsiPeripheral_DeviceMemMap
```

#### 概述

通过调用OH_ScsiPeripheral_CreateDeviceMemMap创建的设备内存映射。使用该设备内存映射的缓冲区可以提供更好的性能。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](../misc/SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](../../capi/headers/scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t* const address缓冲区地址。const size_t size缓冲区大小。uint32_t offset已使用缓冲区的偏移量。默认值为0，表示没有偏移，缓冲区从指定地址开始。uint32_t bufferLength已使用缓冲区的长度。默认情况下，该值等于缓冲区的大小，表示整个缓冲区都被使用。uint32_t transferredLength传输数据的长度。