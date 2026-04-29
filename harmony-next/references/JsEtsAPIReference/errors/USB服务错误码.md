# USB服务错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 14400001 连接USB设备被拒绝

**错误信息**

Access right denied. Call requestRight to get the USBDevicePipe access right first.

**错误描述**

当调用USB模块部分接口时，如果没有相关权限，会报此错误码。

**可能原因**

没有获取到设备的使用权限。

**处理步骤**

调用requestRight方法申请设备的使用权限。

#### 14400004 服务异常

**错误信息**

Service exception. Possible causes: No accessory is plugged in.

**错误描述**

服务异常。

**可能原因：**

没有配件插入。

**处理步骤**

插入配件。

#### 14400005 数据库操作异常

**错误信息**

Database operation exception.

**错误描述**

数据库操作异常。

**处理步骤**

尝试重新调用接口。

#### 14401001 目标USB配件未匹配

**错误信息**

The target USBAccessory not matched.

**错误描述**

目标USB配件未匹配。

**处理步骤**

通过getAccessoryList获得配件列表，使用匹配的USBAccessory重新操作。

#### 14401002 打开配件节点失败

**错误信息**

Failed to open the native accessory node.

**错误描述**

打开配件节点失败。

**处理步骤**

尝试重新调用接口。

#### 14401003 不能重复打开配件

**错误信息**

Cannot reopen the accessory.

**错误描述**

不能重复打开配件。

**处理步骤**

配件已被打开，继续执行后续开发操作。

#### 14400007 资源繁忙

**错误信息**

Resource busy. Possible causes: 1. The transfer has already been submitted. 2. The interface is claimed by another program or driver.

**错误描述**

资源被占用。

**可能原因**

1.

传输任务已提交。

1.

该接口已被另一个程序或驱动程序占用。

**处理步骤**

检查[usbManager.claimInterface](@ohos.usbManager (USB管理).md#ZH-CN_TOPIC_0000002553201555__usbmanagerclaiminterface)接口是否调用成功。

#### 14400008 没有设备(连接已断开)

**错误信息**

No such device (it may have been disconnected).

**错误描述**

未识别到正确设备信息。

**处理步骤**

检查设备类型是否正确，检查设备是否已成功连接。

#### 14400009 内存不足

**错误信息**

Insufficient memory. Possible causes: 1. Memory allocation failed.

**错误描述**

内存申请时无内存可用，单次传输，数据大小最大为1KB。

**可能原因**

内存占用率过高，没有足够的空间分配给当前任务。

**处理步骤**

及时清理内存。

#### 14400010 无法识别的错误

**错误信息**

Other USB error. Possible causes:Unrecognized discard error code.

**错误描述**

系统无法识别的错误。

**处理步骤**

查阅设备相关资料，尝试重新操作。

#### 14400011 未找到正在进行的传输

**错误信息**

The transfer is not in progress, or is already complete or cancelled.

**错误描述**

此次传输已被取消或已经传输完成。

**处理步骤**

重新发起新的传输请求。

#### 14400012 I/O错误

**错误信息**

Transmission I/O error.

**错误描述**

I/O通道异常，实际读/写操作失败。

**处理步骤**

尝试重新操作。

#### 14400013 参数合法性检查失败

**错误信息**

The USBDevicePipe validity check failed. Possible causes: 1. The input parameters fail the validation check. 2. The call chain used to obtain the input parameters is not reasonable.

**错误描述**

参数合法性检查失败。

**可能原因**

1.

输入参数合法性检查失败。

1.

入参获取调用链不合理。

**处理步骤**

采用合理的调用链获取入参。

#### 31400001 串口服务异常

**错误信息**

Serial port management exception.

**错误描述**

串口服务异常。

**可能原因**

程序出现异常导致进程退出。

**处理步骤**

检查是否连接设备，重新通过串口列表获取端口号。

#### 31400002 没有串口设备访问权限

**错误信息**

Access denied. Call requestSerialRight to request user authorization first.

**错误描述**

没有串口设备访问权限，先调用 requestSerialRight。

**可能原因**

没有申请串口设备访问权限。

**处理步骤**

调用requestSerialRight 申请访问权限。

#### 31400003 端口号不存在

**错误信息**

PortId does not exist.

**错误描述**

端口号不存在。

**可能原因**

设备连接异常导致原有端口号失效。

**处理步骤**

插拔设备，再次尝试打开。

#### 31400004 端口正在被其他应用程序使用

**错误信息**

The serial port device is occupied.

**错误描述**

串口设备已被占用。

**可能原因**

重复打开串口设备。

**处理步骤**

插拔设备，再次尝试打开。

#### 31400005 设备未打开

**错误信息**

The serial port device is not opened. Call the open API first.

**错误描述**

串口设备未打开，请先调用Open接口打开设备。

**可能原因**

使用未打开的设备。

**处理步骤**

请先调用Open接口打开设备，再进行后续操作。

#### 31400006 传输超时

**错误信息**

Data transfer timed out.

**错误描述**

数据传输超时。

**可能原因**

对端未发送数据。

**处理步骤**

请检查对端设备是否发起数据传输。

#### 31400007 IO异常

**错误信息**

IO exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed.

**错误描述**

IO异常。

**可能原因**

1.

传输任务被异常取消。

1.

用户接收的单次传输数据量超过了设置的缓冲区大小。

**处理步骤**

设置符合传输场景要求的缓冲区大小后，重新启动传输任务。