[]()[]()

# FIDO

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1005900003 用户取消操作

**错误信息**

User cancels.

**错误描述**

用户取消时，系统会产生此错误码。

**可能原因**

用户验证生物特征时点击关闭按钮。

**处理步骤**

重新发起认证。

[]()[]()

#### 1005900005 没有可用认证器

**错误信息**

No authenticator matching the authenticator policy specified is available.

**错误描述**

无可用的认证器时，系统会产生此错误码。

**可能原因**

1. checkPolicy：服务端有用户数据，客户端没有，比如开启FIDO认证后清除用户数据等操作。

2. processUAFOperation：

开启：已经开启FIDO认证的用户再次开启。

认证：未开启FIDO认证的用户做认证。

**处理步骤**

1. checkPolicy：重新开启FIDO认证。

2. processUAFOperation：

开启：已经开启，无需重复开启，直接做认证。

认证：用户在未开启状态，先开启再做认证，参见：[FIDO免密身份认证](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-fido#section2960852143012)。

[]()[]()

#### 1005900006 协议错误

**错误信息**

A violation of the UAF protocol occurred.

**错误描述**

UAF协议发生错误时，系统会产生此错误码。

**可能原因**

报文格式或数据有误。

**处理步骤**

检查传入报文是否有误，传入正确的报文。

[]()[]()

#### 1005900007 facet id不匹配

**错误信息**

No Facet_ID is registered.

**错误描述**

facet id不匹配，系统会产生此错误码。

**可能原因**

客户端计算的facet id与FIDO服务端配置的不一致（facet id为应用打包时签名证书的签名值，提前获取后配置在FIDO服务端）。

**处理步骤**

检查服务端配置的facet id是否正确。HarmonyOS的facet id格式为：ohos:app-id:<应用签名值>。

应用签名值通过[getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself) 接口获取，[BundleFlag](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundleflag)设置为GET_BUNDLE_INFO_WITH_SIGNATURE_INFO，获取其中的signatureInfo的appId字段，并且将appId去除前面的包名前缀以及末尾全部“=”。

例：

1. 通过[getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)接口获取的appId：

“com.huawei.hmos.test_6ea5b1b7d51b857cb46d570eb79f7b1c8936a18c5f9bd6b9592ccc75e3406863==”。

2. 去除前面的包名前缀以及末尾全部“=”得到签名值：

“6ea5b1b7d51b857cb4d50e79f7b1c8936a18c5f9bd6b9592ccc75e3406863”。

3. 拼接“ohos:app-id:”前缀后得到facet id：

“ohos:app-id:6ea5b1b7d51b857cb46d570eb79f7b1c8936a18c5f9bd6b9592ccc75e3406863”。

[]()[]()

#### 1005900009 拒绝本次请求

**错误信息**

The authenticator denies access to the generated request.

**错误描述**

认证器拒绝请求时，系统会产生此错误码。

**可能原因**

认证时数据库中读取的KeyHandle解密后得到的KHAccessToken与动态计算的KHAccessToken不匹配。

**处理步骤**

关闭当前FIDO指纹/人脸认证，重新开启。

[]()[]()

#### 1005900014 用户未录入生物特征信息

**错误信息**

The user does not record biometric features or the authentication module is abnormal.

**错误描述**

用户未注册生物特征或认证模块异常时，系统会产生此错误码。

**可能原因**

用户未注册生物特征。

**处理步骤**

1. 检查移动端设备是否注册生物特征信息。
1. 在设置里录入生物特征信息。

[]()[]()

#### 1005900015 系统中断

**错误信息**

System Interruption.

**错误描述**

系统发生中断时，系统会产生此错误码。

**可能原因**

运行环境异常。

**处理步骤**

重启移动端设备。

[]()[]()

#### 1005900016 未知错误

**错误信息**

Unknown error.

**错误描述**

发生未知错误时，系统会产生此错误码。

**可能原因**

FIDO服务未知异常。

**处理步骤**

1. 重试。
1. 重启设备，重试。

[]()[]()

#### 1005900017 切换到自定义认证方式

**错误信息**

Switched to the custom authentication process.

**错误描述**

在调用时传入了其他认证方式按钮文本，用户认证失败后取消认证，系统会返回此错误码。

**可能原因**

用户认证失败后取消认证。

**处理步骤**

重新发起UAF认证或者拉起自定义认证方式。