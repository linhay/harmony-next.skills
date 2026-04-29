# UsbDeviceMemMap

```ets
typedef struct UsbDeviceMemMap {...} UsbDeviceMemMap
```

**概述**

设备内存映射，通过OH_Usb_CreateDeviceMemMap创建设备内存映射，使用内存映射后的缓冲区，获得更好的性能。

起始版本： 10

相关模块： [UsbDdk](UsbDdk.md)

所在头文件： [usb_ddk_types.h](usb_ddk_types.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint8_t* const address | 映射后的缓冲区地址。 |
| const size_t size | 缓冲区大小。 |
| uint32_t offset | 所使用的缓冲区的偏移量，默认为0，表示没有偏移，从映射后的缓冲区地址address开始。 |
| uint32_t bufferLength | 所使用的缓冲区的长度，默认等于缓冲区大小 size，表示使用全部的缓冲区。 |
| uint32_t transferedLength | 实际传输的数据的长度。 |