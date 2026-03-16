[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1000500001 内部错误

[]()[]()

#### 算法异常

**错误信息**

- Internal error. Failed to encode.
- Internal error. Failed to decode.
- Internal error. Failed to decode image.

**错误描述**

算法异常。

**可能原因**

码图生成或图像识码时算法出现错误。

**处理步骤**

尝试重新调用码图生成或图像识码接口。

[]()[]()

#### 码图生成失败

**错误信息**

Internal error. Failed to create pixelMap.

**错误描述**

码图生成失败，创建pixelMap失败。

**可能原因**

系统创建图像逻辑异常。

**处理步骤**

尝试重新调用生成码图接口。

[]()[]()

#### 图片获取失败

**错误信息**

Internal error. Failed to read file.

**错误描述**

读取文件失败。

**可能原因**

开发者传入uri无效。

**处理步骤**

检查传入的uri。

[]()[]()

#### 获取系统context失败

**错误信息**

- Internal error. Get UI content failed.
- Internal error. Get context failed.

**错误描述**

获取系统context失败。

**可能原因**

传入的context错误。

**处理步骤**

排查context入参。

[]()[]()

#### 获取callback失败

**错误信息**

Internal error. Get callback failed.

**错误描述**

获取Callback失败。

**可能原因**

外部传入Callback异常。

**处理步骤**

排查Callback入参。

[]()[]()

#### 接口调用顺序错误

**错误信息**

- Internal error. This interface must be invoked after the customScan.start interface.
- Internal error. This interface cannot be used after the camera session is paused.
- Internal error. ScanOption is null, please call customScan.init first.

**错误描述**

接口调用顺序错误。

**可能原因**

未按开发指南的业务流程调用接口，如未调用customScan.init接口，直接调用customScan.start接口。

**处理步骤**

调整接口调用顺序。例如：先调用customScan.init接口，再调用customScan.start。

[]()[]()

#### 接口调用不被允许

**错误信息**

Internal error. The interface can't be used in promise interface.

**错误描述**

该接口不允许在customScan.start的Promise方式中调用。

**可能原因**

customScan.start的Promise方式中调用了customScan.rescan接口。

**处理步骤**

使用customScan.start的Callback方式再调用customScan.rescan接口。

[]()[]()

#### 分辨率不匹配

**错误信息**

Internal error. The width and height of viewControl do not match the width and height supported by the camera.

**错误描述**

传入的ViewControl宽高比例与相机分辨率不匹配。

**可能原因**

传入的ViewControl宽高比例与相机分辨率不匹配。

**处理步骤**

检查ViewControl的宽高比例。

[]()[]()

#### 相机错误

**错误信息**

- Internal error. CustomScan stop session failed.
- Internal error. Open camera flash failed.
- Internal error. Close camera flash failed.
- Internal error. Camera setZoom failed.
- Internal error. Camera getZoom failed.
- Internal error. Camera setFocusPoint failed.
- Internal error. Reset focus mode failed.
- Internal error. Camera config captureSession failed.
- Internal error. Camera create cameraManager failed.
- Internal error. Camera create camera session failed.
- Internal error. Camera restart camera session failed.
- Internal error. Camera create preview output failed.

**错误描述**

相机错误。

**可能原因**

- 相机流暂停失败。
- 打开闪光灯失败。
- 关闭闪光灯失败。
- 设置变焦比失败。
- 获取变焦比失败。
- 设置变焦点失败。
- 重置对焦模式失败。
- 相机配流失败。
- 相机创建cameraManager失败。
- 相机创建session失败。
- 相机重启失败。
- 相机创建预览流失败。

**处理步骤**

建议尝试重新创建业务。

[]()[]()

#### 1000500002 用户取消扫码

**错误信息**

The user canceled the barcode scanning.

**错误描述**

用户取消扫码。

**可能原因**

用户点击关闭按钮或侧滑取消默认界面扫码。

**处理步骤**

使用[scanBarcode.startScanForResult](../topics/components/scanBarcode (默认界面扫码).md#section829511911349)会返回此错误码，请根据使用场景处理用户取消默认界面扫码后的业务流程。