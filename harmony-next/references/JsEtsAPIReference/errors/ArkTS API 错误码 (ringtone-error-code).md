[]()[]()

# ArkTS API 错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 401 参数非法

**错误信息**

Parameter invalid.

**错误描述**

参数错误。

**可能原因**

参数填写不正确。

**处理步骤**

1、参考文档确认数据必填项、取值范围等是否填写正确。

2、尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1011600001 用户取消

**错误信息**

User canceled.

**错误描述**

用户拉起弹框后，未完成铃声设置功能，取消了弹框。

**可能原因**

用户操作原因。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1011600002 文件不存在

**错误信息**

The media file is not found.

**错误描述**

传入的文件路径下不存在文件。

**可能原因**

文件未创建成功就调用了[ringtone.startRingtoneSetting](../topics/misc/ringtone（铃声服务）.md#section5949453189)接口。

**处理步骤**

确保文件路径下传入了对应文件后再重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1011600003 弹出框错误

**错误信息**

Failed to show the dialog box.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1011600004 调用系统接口失败

**错误信息**

Failed to call the system API.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

[]()[]()

#### 1011699999 系统内部错误

**错误信息**

System exception.

**错误描述**

当发生系统内部错误时，将返回该错误码。

**可能原因**

其他未知错误。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。