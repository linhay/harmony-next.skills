# ohscan.h

#### 概述

声明用于发现和连接扫描仪、从扫描仪扫描图像、获取页面扫描进度和设置扫描图像参数等功能的API

**库：** libohscan.so

**系统能力：** SystemCapability.Print.PrintFramework

**起始版本：** 12

**相关模块：**[OH_Scan](OH_Scan.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Scan_ScannerDevice](Scan_ScannerDevice.md)Scan_ScannerDevice表示扫描仪设备信息[Scan_PictureScanProgress](Scan_PictureScanProgress.md)Scan_PictureScanProgress表示扫描仪扫描图片的进度[Scan_ScannerOptions](Scan_ScannerOptions.md)Scan_ScannerOptions表示一个扫描仪的所有参数选项

#### 枚举

名称typedef关键字描述[Scan_ErrorCode](#ZH-CN_TOPIC_0000002529285525__scan_errorcode)Scan_ErrorCode定义错误码

#### 函数

名称typedef关键字描述[typedef void (*Scan_ScannerDiscoveryCallback)(Scan_ScannerDevice** devices, int32_t deviceCount)](#ZH-CN_TOPIC_0000002529285525__scan_scannerdiscoverycallback)Scan_ScannerDiscoveryCallback扫描仪设备发现回调，通过[OH_Scan_StartScannerDiscovery](zh-cn_topic_0000002529285525.html#ZH-CN_TOPIC_0000002529285525__oh_scan_startscannerdiscovery)注册指针指向的内存将在回调函数结束时释放[int32_t OH_Scan_Init()](#ZH-CN_TOPIC_0000002529285525__oh_scan_init)-此API检查并拉起扫描服务，初始化扫描客户端，并建立与扫描服务的连接[int32_t OH_Scan_StartScannerDiscovery(Scan_ScannerDiscoveryCallback callback)](#ZH-CN_TOPIC_0000002529285525__oh_scan_startscannerdiscovery)-此API开始发现扫描仪，注册回调函数处理发现的扫描仪设备[int32_t OH_Scan_OpenScanner(const char* scannerId)](#ZH-CN_TOPIC_0000002529285525__oh_scan_openscanner)-此API连接到扫描仪设备[int32_t OH_Scan_CloseScanner(const char* scannerId)](#ZH-CN_TOPIC_0000002529285525__oh_scan_closescanner)-此API用于关闭已连接的扫描仪设备[Scan_ScannerOptions* OH_Scan_GetScannerParameter(const char* scannerId, int32_t* errorCode)](#ZH-CN_TOPIC_0000002529285525__oh_scan_getscannerparameter)-此API可用于获取扫描仪可设置的选项列表返回的结构体指针指向的内存会在[OH_Scan_Exit](zh-cn_topic_0000002529285525.html#ZH-CN_TOPIC_0000002529285525__oh_scan_exit)时自动释放，每个型号在内存中只会存储一份副本[int32_t OH_Scan_SetScannerParameter(const char* scannerId, const int32_t option, const char* value)](#ZH-CN_TOPIC_0000002529285525__oh_scan_setscannerparameter)-此API可用于设置扫描仪的某个选项参数传入的选项和值从[OH_Scan_GetScannerParameter](zh-cn_topic_0000002529285525.html#ZH-CN_TOPIC_0000002529285525__oh_scan_getscannerparameter)获取[int32_t OH_Scan_StartScan(const char* scannerId, bool batchMode)](#ZH-CN_TOPIC_0000002529285525__oh_scan_startscan)-此API允许扫描仪开始扫描[int32_t OH_Scan_CancelScan(const char* scannerId)](#ZH-CN_TOPIC_0000002529285525__oh_scan_cancelscan)-此API允许扫描仪取消扫描[int32_t OH_Scan_GetPictureScanProgress(const char* scannerId, Scan_PictureScanProgress* prog)](#ZH-CN_TOPIC_0000002529285525__oh_scan_getpicturescanprogress)-此API可获取扫描仪扫描图片的进度。必须传入非空值，扫描进度将写入指针指向的结构体[int32_t OH_Scan_Exit()](#ZH-CN_TOPIC_0000002529285525__oh_scan_exit)-此API可用于退出扫描服务，释放扫描框架内存，并注销扫描仪发现回调

#### 枚举类型说明

#### Scan_ErrorCode

```ets
enum Scan_ErrorCode
```

**描述**

定义错误码

**起始版本：** 12

枚举项描述SCAN_ERROR_NONE = 0操作成功SCAN_ERROR_NO_PERMISSION = 201权限验证失败SCAN_ERROR_INVALID_PARAMETER = 401参数无效。例如指针为空或字符串为空SCAN_ERROR_GENERIC_FAILURE = 24300101通用内部错误SCAN_ERROR_RPC_FAILURE = 24300102RPC通信错误SCAN_ERROR_SERVER_FAILURE = 24300103服务器错误SCAN_ERROR_UNSUPPORTED = 24300104不支持的操作SCAN_ERROR_CANCELED = 24300105操作已取消SCAN_ERROR_DEVICE_BUSY = 24300106设备繁忙，请稍后重试SCAN_ERROR_INVALID = 24300107数据无效（包括打开时无设备）SCAN_ERROR_JAMMED = 24300108文档进纸器卡纸SCAN_ERROR_NO_DOCS = 24300109文档进纸器缺纸SCAN_ERROR_COVER_OPEN = 24300110扫描仪盖板打开SCAN_ERROR_IO_ERROR = 24300111设备I/O错误SCAN_ERROR_NO_MEMORY = 24300112内存不足

#### 函数说明

#### Scan_ScannerDiscoveryCallback()

```ets
typedef void (*Scan_ScannerDiscoveryCallback)(Scan_ScannerDevice** devices, int32_t deviceCount)
```

**描述**

扫描仪设备发现回调，通过[OH_Scan_StartScannerDiscovery](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__oh_scan_startscannerdiscovery)注册指针指向的内存将在回调函数结束时释放

**起始版本：** 12

**参数：**

参数项描述[Scan_ScannerDevice](Scan_ScannerDevice.md)** devices所有发现的扫描仪设备列表int32_t deviceCount发现的扫描仪数量

#### OH_Scan_Init()

```ets
int32_t OH_Scan_Init()
```

**描述**

此API检查并拉起扫描服务，初始化扫描客户端，并建立与扫描服务的连接

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描服务成功启动

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

#### OH_Scan_StartScannerDiscovery()

```ets
int32_t OH_Scan_StartScannerDiscovery(Scan_ScannerDiscoveryCallback callback)
```

**描述**

此API开始发现扫描仪，注册回调函数处理发现的扫描仪设备

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述[Scan_ScannerDiscoveryCallback](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_scannerdiscoverycallback) callback扫描仪发现事件的[Scan_ScannerDiscoveryCallback](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_scannerdiscoverycallback)回调函数

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示成功开始扫描仪搜索

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

#### OH_Scan_OpenScanner()

```ets
int32_t OH_Scan_OpenScanner(const char* scannerId)
```

**描述**

此API连接到扫描仪设备

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述const char* scannerId用于连接扫描仪的ID

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪成功连接

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

[SCAN_ERROR_DEVICE_BUSY](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪繁忙

[SCAN_ERROR_INVALID_PARAMETER](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示输入参数无效

[SCAN_ERROR_IO_ERROR](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示与设备通信时发生错误

[SCAN_ERROR_NO_MEMORY](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示可用内存不足

#### OH_Scan_CloseScanner()

```ets
int32_t OH_Scan_CloseScanner(const char* scannerId)
```

**描述**

此API用于关闭已连接的扫描仪设备

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述const char* scannerId用于断开扫描仪连接的ID

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪连接成功关闭

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

[SCAN_ERROR_INVALID_PARAMETER](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示输入参数无效

#### OH_Scan_GetScannerParameter()

```ets
Scan_ScannerOptions* OH_Scan_GetScannerParameter(const char* scannerId, int32_t* errorCode)
```

**描述**

此API可用于获取扫描仪可设置的选项列表返回的结构体指针指向的内存会在[OH_Scan_Exit](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__oh_scan_exit)时自动释放，每个型号在内存中只会存储一份副本

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述const char* scannerId用于获取扫描仪参数的IDint32_t* errorCode如果执行成功，errorCode返回[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode)，否则返回特定的错误码，参考[Print_ErrorCode](zh-cn_topic_0000002497445554.html#ZH-CN_TOPIC_0000002497445554__print_errorcode)

**返回：**

类型说明[Scan_ScannerOptions*](Scan_ScannerOptions.md)

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示成功获取扫描仪参数选项

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

[SCAN_ERROR_INVALID_PARAMETER](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示参数无效

#### OH_Scan_SetScannerParameter()

```ets
int32_t OH_Scan_SetScannerParameter(const char* scannerId, const int32_t option, const char* value)
```

**描述**

此API可用于设置扫描仪的某个选项参数传入的选项和值从[OH_Scan_GetScannerParameter](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__oh_scan_getscannerparameter)获取

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述const char* scannerId此ID用于设置特定扫描仪的选项const int32_t option要设置的选项编号。取值范围从0到 optionCount - 1，从[Scan_ScannerOptions](Scan_ScannerOptions.md)获取const char* value要设置的选项值，有效值从ranges获取，从[Scan_ScannerOptions](Scan_ScannerOptions.md)获取

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪参数设置成功

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

[SCAN_ERROR_INVALID_PARAMETER](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示参数无效

#### OH_Scan_StartScan()

```ets
int32_t OH_Scan_StartScan(const char* scannerId, bool batchMode)
```

**描述**

此API允许扫描仪开始扫描

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** code ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述const char* scannerId此ID用于启动指定扫描仪的扫描任务bool batchMode是否以批处理模式启动扫描仪

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪成功启动扫描任务

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

[SCAN_ERROR_JAMMED](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示文档进纸器卡纸

[SCAN_ERROR_NO_DOCS](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示文档进纸器缺纸

[SCAN_ERROR_COVER_OPEN](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪盖板打开

[SCAN_ERROR_IO_ERROR](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示与设备通信时发生错误

[SCAN_ERROR_NO_MEMORY](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示可用内存不足

[SCAN_ERROR_INVALID_PARAMETER](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示输入参数无效

[SCAN_ERROR_DEVICE_BUSY](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示设备繁忙，应稍后重试操作

#### OH_Scan_CancelScan()

```ets
int32_t OH_Scan_CancelScan(const char* scannerId)
```

**描述**

此API允许扫描仪取消扫描

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述const char* scannerId此ID用于取消指定扫描仪的扫描任务

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪成功取消扫描任务

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_INVALID_PARAMETER](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示指针为空或字符串为空

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

#### OH_Scan_GetPictureScanProgress()

```ets
int32_t OH_Scan_GetPictureScanProgress(const char* scannerId, Scan_PictureScanProgress* prog)
```

**描述**

此API可获取扫描仪扫描图片的进度。必须传入非空值，扫描进度将写入指针指向的结构体

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**参数：**

参数项描述const char* scannerId用于查询扫描仪图像扫描进度的ID[Scan_PictureScanProgress](Scan_PictureScanProgress.md)* prog扫描图片的[Scan_PictureScanProgress](Scan_PictureScanProgress.md)，必须为非空值

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪成功查询到扫描图像的进度

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_INVALID_PARAMETER](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示指针为空或字符串为空

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误

[SCAN_ERROR_JAMMED](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示文档进纸器卡纸

[SCAN_ERROR_NO_DOCS](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示文档进纸器缺纸

[SCAN_ERROR_COVER_OPEN](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描仪盖板打开

[SCAN_ERROR_IO_ERROR](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示与扫描仪通信时发生错误

[SCAN_ERROR_NO_MEMORY](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示可用内存不足

[SCAN_ERROR_DEVICE_BUSY](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示设备繁忙，应稍后重试操作

#### OH_Scan_Exit()

```ets
int32_t OH_Scan_Exit()
```

**描述**

此API可用于退出扫描服务，释放扫描框架内存，并注销扫描仪发现回调

**系统能力：** SystemCapability.Print.PrintFramework

**需要权限：** ohos.permission.PRINT

**起始版本：** 12

**返回：**

类型说明int32_t

[SCAN_ERROR_NONE](#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描服务成功退出

[SCAN_ERROR_NO_PERMISSION](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示无权限使用此接口

[SCAN_ERROR_RPC_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示RPC通信错误

[SCAN_ERROR_SERVER_FAILURE](ohscan.h.md#ZH-CN_TOPIC_0000002529285525__scan_errorcode) 表示扫描过程中发生错误