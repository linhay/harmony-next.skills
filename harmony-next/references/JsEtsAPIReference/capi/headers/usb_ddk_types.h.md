# usb_ddk_types.h

#### 概述

提供USB DDK中的枚举变量、结构体定义与宏定义。

**引用文件：** <usb/usb_ddk_types.h>

**库：** libusb_ndk.z.so

**系统能力：** SystemCapability.Driver.USB.Extension

**起始版本：** 10

**相关模块：**[UsbDDK](../../topics/misc/UsbDDK.md)

#### 汇总

#### 结构体

名称typedef关键字描述[UsbControlRequestSetup](../../topics/misc/UsbControlRequestSetup.md)**attribute**((aligned(8))) UsbControlRequestSetup控制传输setup包，对应USB协议中的Setup Data。[UsbDeviceDescriptor](../../topics/system-services/UsbDeviceDescriptor.md)**attribute**((aligned(8))) UsbDeviceDescriptor标准设备描述符，对应USB协议中Standard Device Descriptor。[UsbConfigDescriptor](../../topics/misc/UsbConfigDescriptor.md)**attribute**((packed)) UsbConfigDescriptor标准配置描述符，对应USB协议中Standard Configuration Descriptor。[UsbInterfaceDescriptor](../../topics/misc/UsbInterfaceDescriptor.md)**attribute**((packed)) UsbInterfaceDescriptor标准接口描述符，对应USB协议中Standard Interface Descriptor。[UsbEndpointDescriptor](../../topics/misc/UsbEndpointDescriptor.md)**attribute**((packed)) UsbEndpointDescriptor标准端点描述符，对应USB协议中Standard Endpoint Descriptor。[UsbDdkEndpointDescriptor](../../topics/misc/UsbDdkEndpointDescriptor.md)UsbDdkEndpointDescriptor端点描述符。[UsbDdkInterfaceDescriptor](../../topics/misc/UsbDdkInterfaceDescriptor.md)UsbDdkInterfaceDescriptor接口描述符。[UsbDdkInterface](../../topics/misc/UsbDdkInterface.md)UsbDdkInterfaceUSB接口，是特定接口下备用设置的集合。[UsbDdkConfigDescriptor](../../topics/misc/UsbDdkConfigDescriptor.md)UsbDdkConfigDescriptor配置描述符。[UsbRequestPipe](../../topics/misc/UsbRequestPipe.md)**attribute**((aligned(8))) UsbRequestPipe请求管道。[UsbDeviceMemMap](../../topics/system-services/UsbDeviceMemMap.md)UsbDeviceMemMap设备内存映射，通过OH_Usb_CreateDeviceMemMap创建设备内存映射，使用内存映射后的缓冲区，获得更好的性能。[Usb_DeviceArray](../../topics/system-services/Usb_DeviceArray.md)Usb_DeviceArray设备ID清单，用于存放OH_Usb_GetDevices接口获取到的设备ID列表和设备数量。

#### 枚举

名称typedef关键字描述[UsbDdkErrCode](#ZH-CN_TOPIC_0000002529445577__usbddkerrcode)UsbDdkErrCodeUSB DDK 错误码定义。

#### 枚举类型说明

#### UsbDdkErrCode

```ets
enum UsbDdkErrCode
```

**描述**

USB DDK 错误码定义。

**起始版本：** 10

枚举项描述USB_DDK_SUCCESS = 0操作成功。USB_DDK_FAILED = -1

操作失败。

**废弃版本：** 16

USB_DDK_NO_PERM = 201

没有权限。

**起始版本：** 14

USB_DDK_INVALID_PARAMETER = 401非法参数，在API version 16之前值为-2。USB_DDK_MEMORY_ERROR = 27400001内存相关的错误，包括：内存不足、内存数据拷贝失败、内存申请失败等，在API version 16之前值为-3。USB_DDK_INVALID_OPERATION = 27400002非法操作，在API version 16之前值为-4。USB_DDK_NULL_PTR = -5

空指针异常。

**废弃版本：** 16

USB_DDK_DEVICE_BUSY = -6

设备忙。

**废弃版本：** 16

USB_DDK_IO_FAILED = 27400003

设备I/O操作失败。

**起始版本：** 14

USB_DDK_TIMEOUT = 27400004传输超时，在API version 16之前值为-7。