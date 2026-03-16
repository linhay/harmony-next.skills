[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

1001930000

The operation was canceled by the user.

1001930001

Pay failed.

1001930002

The transaction has been processed.

1001930003

Withhold failed.

1001930010

Duplicate request.

1001930011

Network connection error.

1014900000

The operation was canceled by the user.

1014900001

Payment failed.

1014900002

The transaction has been processed.

1014900003

Duplicate request.

1014900004

Network connection error.

1014900005

The payment environment is not ready.

1020100000

The application does not have the required capability.

1020100001

The user did not accept the agreement.

1020100002

The user canceled the operation.

1020100003

The pre-verify ID is invalid.

1020100004

The network is unavailable.

1020100005

System internal error.

1020100006

The camera permission is not granted.

1020100007

The liveness detection failed.

1020100008

The app ID does not match.

1020100009

The user ID does not match.

1022830000

The operation was canceled by the user.

1022830001

Pay failed.

1022830002

The payInfo is invalid. Possible causes: 1.Dataformat is not json string；2.Mandatory parameters are left unspecified.

[]()[]()

#### 1001930000 用户取消操作

**错误信息**

The operation was canceled by the user.

**错误描述**

用户取消支付。

**可能原因**

用户在支付、签约等过程中取消退出。

**处理步骤**

向用户提示，取消相关操作。

[]()[]()

#### 1001930001 支付失败

**错误信息**

Pay failed.

**错误描述**

支付失败。

**可能原因**

1. 传入参数orderStr格式错误，prepayId错误或对应订单不存在。
1. authId、公私钥不匹配，签名错误。

**处理步骤**

1. 请检查orderStr是否为json格式的字符串，orderStr里面的字段类型、值是否正确。
1. 请参见[准备证书](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-certificates-config)、[签名规则](../guides/公共说明 (payment-rest-overview).md#section174821258151218)章节进行检查。

[]()[]()

#### 1001930002 交易已处理

**错误信息**

The transaction has been processed.

**错误描述**

交易已处理。

**可能原因**

1. 使用同一个orderStr同时拉起支付收银台。
1. 已拉起收银台但未完成支付，再次重复拉起收银台支付。

**处理步骤**

1. 确认是否存在重复拉起收银台支付。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1001930003 签约失败

**错误信息**

Withhold failed.

**错误描述**

签约失败。

**可能原因**

1. 传入参数contractStr错误。
1. 预签约号不正确。

**处理步骤**

1. 请检查contractStr是否为json格式的字符串，contractStr里面的字段类型、字段值等是否正确。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1001930010 重复请求

**错误信息**

Duplicate request.

**错误描述**

重复请求。

**可能原因**

调用接口频率太频繁。

**处理步骤**

1. 建议调用接口后不要立马再次调用，添加延时处理机制控制。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1001930011 网络连接异常

**错误信息**

Network connection error.

**错误描述**

网络连接异常。

**可能原因**

用户无网络信号或网络不稳定。

**处理步骤**

应用向用户给出提示，请用户检查网络。

[]()[]()

#### 1014900000 用户取消支付

**错误信息**

The operation was canceled by the user.

**错误描述**

用户取消支付。

**可能原因**

用户在支付过程中取消退出。

**处理步骤**

向用户提示，订单取消。

[]()[]()

#### 1014900001 支付失败

**错误信息**

Payment failed.

**错误描述**

支付失败。

**可能原因**

传入orderInfo参数格式错误。

**处理步骤**

1. 请检查orderInfo参数格式、内容是否正确。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1014900002 交易已处理

**错误信息**

The transaction has been processed.

**错误描述**

交易已处理。

**可能原因**

使用重复的订单号下单。

**处理步骤**

查询交易订单，查看订单状态，使用新订单号去交易。

[]()[]()

#### 1014900003 重复请求

**错误信息**

Duplicate request.

**错误描述**

重复请求。

**可能原因**

短时间发起相同请求。

**处理步骤**

1. 请稍后重试。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1014900004 网络连接异常

**错误信息**

Network connection error.

**错误描述**

网络连接异常。

**可能原因**

用户无网络信号或网络不稳定。

**处理步骤**

应用向用户给出提示，请用户检查网络。

[]()[]()

#### 1014900005 支付环境初始化未完成

**错误信息**

The payment environment is not ready.

**错误描述**

支付环境初始化未完成。

**可能原因**

钱包版本不满足或者未安装，最低版本要求为 1.0.8.305。

**处理步骤**

1. 安装或升级钱包版本。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020100000 应用未开通必要服务

**错误信息**

The application does not have the required capability.

**错误描述**

应用未开通必要服务。

**可能原因**

1. 用户没有在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)开启相关服务。
1. profile文件配置不正确。

**处理步骤**

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，开启服务，具体可参见[开启用户身份验证服务权限开关](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-real-name-preparations#section11591427192013)。
1. 检查profile配置是否正确，参考[申请调试证书和调试Profile文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section081822416419)。

[]()[]()

#### 1020100001 用户未同意

**错误信息**

The user did not accept the agreement.

**错误描述**

用户未同意协议。

**可能原因**

用户首次使用时未同意Payment Kit的用户协议。

**处理步骤**

应用根据需要提示和引导用户同意协议。

[]()[]()

#### 1020100002 用户取消操作

**错误信息**

The user canceled the operation.

**错误描述**

用户取消操作。

**可能原因**

用户在验证、授权等过程中取消退出。

**处理步骤**

向用户提示，取消相关操作。

[]()[]()

#### 1020100003 预验证ID无效

**错误信息**

The pre-verify ID is invalid.

**错误描述**

预验证ID无效。

**可能原因**

传入preVerifyId参数错误，失效等。

**处理步骤**

1. 请检查preVerifyId是否正确。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020100004 网络不可用

**错误信息**

The network is unavailable.

**错误描述**

网络不可用。

**可能原因**

用户无网络信号或网络不稳定。

**处理步骤**

应用向用户给出提示，请用户检查网络。

[]()[]()

#### 1020100005 系统错误

**错误信息**

System internal error.

**错误描述**

系统错误。

**可能原因**

无需开发者感知的内部错误。

**处理步骤**

1. 应用向用户友好提示，引导用户稍后重试，等系统自行修复。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020100006 相机权限未开启

**错误信息**

The camera permission is not granted.

**错误描述**

相机权限未开启。

**可能原因**

应用无开启相机权限。

**处理步骤**

1. 申请开启相机权限。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020100007 活体检测失败

**错误信息**

The liveness detection failed.

**错误描述**

重复请求。

**可能原因**

活体检测环节失败，包括检测失败，检测超时以及其他异常导致的失败。

**处理步骤**

1. 应用向用户友好提示，或稍后重试。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020100008 appID不匹配

**错误信息**

The app ID does not match.

**错误描述**

appId不匹配。

**可能原因**

当前应用的appID和预校验时的clientId不匹配。

**处理步骤**

1. 检查请求预校验接口传递的clientId是否正确。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1020100009 用户ID不匹配

**错误信息**

The user ID does not match.

**错误描述**

用户ID不匹配。

**可能原因**

当前用户的uid和预验证时传递的openId不匹配。

**处理步骤**

1. 检查请求预验证接口传递的openId是否正确。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1022830000 用户取消操作

**错误信息**

The operation was canceled by the user.

**错误描述**

用户取消支付。

**可能原因**

用户在支付等过程中取消退出。

**处理步骤**

向用户提示，取消相关操作。

[]()[]()

#### 1022830001 支付失败

**错误信息**

Pay failed.

**错误描述**

支付失败。

**可能原因**

1. 调用三方支付接口失败。
1. 系统处理异常。

**处理步骤**

1. 请检查payInfo里面的字段类型、值是否正确。明确三方支付接口调用失败具体原因需咨询对应三方支付支撑定位。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1022830002 支付信息无效

**错误信息**

The paylnfo invalid. Possible causes: 1.Dataformat is not json string；2.Mandatory parameters are left unspecified.

**错误描述**

支付信息无效。

**可能原因**

1. 传入参数payInfo格式或内容错误、必选参数未传等。

**处理步骤**

1. 请检查payInfo是否为json格式的字符串，payInfo里面的字段类型、值是否正确。
1. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。