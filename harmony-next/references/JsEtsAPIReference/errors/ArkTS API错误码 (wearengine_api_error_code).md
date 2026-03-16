[]()[]()

# ArkTS API错误码

[]()[]()

#### 401 参数错误

**错误信息**

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**错误描述**

参数错误。

**可能原因**

必选参数没有传入，或者参数类型错误。

**处理步骤**

1. 请检查必选参数是否没有传入，或者传的参数类型是否错误。
1. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 801 该设备不支持此API

**错误信息**

Capability not supported.

**错误描述**

该设备不支持此API，通常用于在设备已支持该SysCap时，针对其少量的API的支持处理。

**可能原因**

该设备不支持此API。

**处理步骤**

请检查设备是否支持使用的API。

[]()[]()

#### 1008500001 网络错误

**错误信息**

Network error. The network is unavailable.

**错误描述**

网络错误。

**可能原因**

网络未连接。

**处理步骤**

1. 检查网络配置。
1. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1008500002 无绑定设备

**错误信息**

No device is bound.

**错误描述**

无绑定设备。

**可能原因**

当前没有穿戴设备与手机连接。

**处理步骤**

1. 检查设备是否已正确连接手机。
1. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1008500003 设备未连接

**错误信息**

Device disconnected.

**错误描述**

设备未连接。

**可能原因**

1. 手机同设备侧蓝牙断开。
1. 运动健康APP与设备侧断联。

**处理步骤**

1. 检查设备侧与手机侧的蓝牙是否打开。
1. 检查运动健康APP中是否已绑定并连接设备。
1. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1008500004 应用未申请Wear Engine服务

**错误信息**

App has not applied for the Wear Engine service.

**错误描述**

手机侧应用未申请Wear Engine服务。

**可能原因**

开发者未在开发者联盟申请WearEngine服务。

**处理步骤**

1. 登录开发者联盟[申请接入Wear Engine服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_apply)。
1. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1008500005 用户未授权

**错误信息**

The HUAWEI ID is not authorized.

**错误描述**

用户华为账号鉴权失败。

**可能原因**

接口所需权限用户尚未授权。

**处理步骤**

参考[请求用户授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request_user_authorization)，确认用户已授权相关权限。

[]()[]()

#### 1008500006 用户未同意隐私授权

**错误信息**

User privacy is not agreed.

**错误描述**

用户未同意运动健康隐私授权。

**可能原因**

用户从未打开过运动健康App。

**处理步骤**

引导用户启动运动健康App，进行隐私授权。

[]()[]()

#### 1008500007 穿戴设备侧能力不支持

**错误信息**

The device capability is not supported.

**错误描述**

穿戴设备不支持对应的能力。

**可能原因**

穿戴设备侧不支持完成当前接口成功调用所需的能力。

**处理步骤**

核查设备能力集。

[]()[]()

#### 1008500008 账号未登录

**错误信息**

Account error. The user has not logged in with HUAWEI ID.

**错误描述**

账号未登录。

**可能原因**

账号未登录。

**处理步骤**

登录华为账号后再重新调用接口。

[]()[]()

#### 1008500009 账号异常

**错误信息**

Account error. Failed to obtain account information with HUAWEI ID.

**错误描述**

账号异常。

**可能原因**

使用的华为账号注册地非中国境内（不包含中国香港、中国澳门、中国台湾）。

**处理步骤**

更换注册地为中国境内（不包含中国香港、中国澳门、中国台湾）账号再操作。

[]()[]()

#### 1008500010 无效设备ID

**错误信息**

Device ID is invalid.

**错误描述**

无效设备ID。

**可能原因**

1. 传入了错误的设备ID。
1. 传入了过期的设备ID。

**处理步骤**

调用[getConnectedDevices](../topics/media/wearEngine(穿戴设备能力开放).md#section1828213119411)接口重新获取设备ID。

[]()[]()

#### 1008500011 无效文件

**错误信息**

File is invalid.

**错误描述**

无效文件。

**可能原因**

传入的文件为无效文件。

**处理步骤**

1. 检查文件路径是否合法。
1. 检查文件是否存在。

[]()[]()

#### 1008500012 回调函数过多

**错误信息**

Too many callbacks of the same type.

**错误描述**

回调函数过多。

**可能原因**

在同一个type上注册了过多的回调函数。

**处理步骤**

及时关闭已经不再使用的监听事件。

[]()[]()

#### 1008509999 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

WearEngine发生了未知的错误。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。