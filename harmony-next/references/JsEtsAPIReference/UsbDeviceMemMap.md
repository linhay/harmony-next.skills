# UsbDeviceMemMap

```ets
typedef struct UsbDeviceMemMap {...} UsbDeviceMemMap
```

#### 概述

设备内存映射，通过OH_Usb_CreateDeviceMemMap创建设备内存映射，使用内存映射后的缓冲区，获得更好的性能。

**起始版本：** 10

**相关模块：**[UsbDDK](UsbDDK.md)

**所在头文件：**[usb_ddk_types.h](usb_ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t* const address映射后的缓冲区地址。const size_t size缓冲区大小。uint32_t offset所使用的缓冲区的偏移量，默认为0，表示没有偏移，从{@link address}开始。uint32_t bufferLength所使用的缓冲区的长度，默认等于{@link size}，表示使用全部的缓冲区。uint32_t transferedLength实际传输的数据的长度。