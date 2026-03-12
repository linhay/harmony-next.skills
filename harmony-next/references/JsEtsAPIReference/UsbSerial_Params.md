# UsbSerial_Params

```ets
typedef struct UsbSerial_Params {...} __attribute__((aligned(8))) UsbSerial_Params
```

#### 概述

定义USB SERIAL DDK使用的USB串口参数.

**起始版本：** 18

**相关模块：**[SerialDdk](USBSerialDdk.md)

**所在头文件：**[usb_serial_types.h](usb_serial_types.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t baudRate波特率。uint8_t nDataBits数据传输位数。uint8_t nStopBits数据停止位数。uint8_t parity校验参数设置。