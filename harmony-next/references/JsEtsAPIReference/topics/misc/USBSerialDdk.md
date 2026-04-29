# USBSerialDDK

#### 概述

提供USB Serial DDK接口，包括枚举类型和USB Serial DDK API使用的数据结构。工业用途及一些老旧设备会使用到串口通信，如：发卡机、身份证读卡器等。通过构建USB Serial DDK，支持外设扩展驱动基于USB Serial DDK开发非标外设扩展驱动。

**系统能力：** SystemCapability.Driver.UsbSerial.Extension

**起始版本：** 18

#### 文件汇总

| 名称 | 描述 |
| --- | --- |
| [usb_serial_api.h](usb_serial_api.h.md) | 声明用于主机侧访问串口设备的USB Serial DDK接口。 |
| [usb_serial_types.h](usb_serial_types.h.md) | 提供USB SERIAL DDK中的枚举变量、结构体定义与宏定义。 |
