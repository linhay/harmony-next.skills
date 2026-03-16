[]()[]()

# ArkTS错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1001500001 应用指纹证书校验失败

**错误信息**

Failed to check the fingerprint of the app bundle.

**错误描述**

应用指纹证书校验失败。

**可能原因**

请参见Account Kit常见问题[1001500001 应用指纹证书校验失败的可能原因和解决办法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-1)。

**处理步骤**

请参见Account Kit常见问题[1001500001 应用指纹证书校验失败的可能原因和解决办法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-1)。

[]()[]()

#### 1001500002 重复请求

**错误信息**

This error code is reported when a request is already being processed.

**错误描述**

重复请求。

**可能原因**

用户多次触发请求Account Kit页面。

**处理步骤**

应用无需特殊处理。

[]()[]()

#### 1001500003 不支持该scopes或permissions

**错误信息**

The scopes or permissions are not supported.

**错误描述**

不支持该scopes或者permissions。

**可能原因**

1、已登录的华为账号不支持授权应用请求的数据。

2、在获取实名信息、实名信息校验、人脸核身等场景下，用户登录的账号为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）注册的华为账号，但使用了港澳台通行证进行实名。

3、在实名信息校验、人脸核身等场景下，PC/2in1设备或前置摄像功能异常的设备不支持传入verifyRealName和verifyFace 2个scope进行授权。

4、元服务开发过程中，调[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)接口时传了profile这个scope，且supportAtomicService参数未设置为true。

5、元服务开发过程中，调[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)接口时传了phone这个scope。

6、在实名信息校验、人脸核身场景，登录的华为账号是儿童账号。

7、Wearable、TV设备申请获取不支持的scope。

**处理步骤**

1、更换或注册一个中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为账号重新登录授权，如果在一键登录场景下，应用需展示其他登录方式。

2、在获取实名信息、实名信息校验、人脸核身等场景下，引导用户更换使用中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）身份证实名的华为账号。

3、在实名信息校验、人脸核身等场景下，使用其他前置摄像功能正常的设备授权verifyRealName和verifyFace 2个scope。

4、元服务开发过程中，调[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)接口时传了profile这个scope，并将supportAtomicService参数设置为true。

5、元服务不能直接调用该接口获取手机号，可参考场景化控件[快速验证手机号button](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-getphonenumber)获取。

6、更换或注册一个中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的成人华为账号，重新触发接口。

7、更换其他支持调用该API的设备或改用其他方式获取相关信息。

[]()[]()

#### 1001500004 已登录的华为账号不支持该功能

**错误信息**

The account does not support this function.

**错误描述**

已登录的华为账号不支持该功能。

**可能原因**

1、已登录的华为账号注册地在中国境外、香港特别行政区、澳门特别行政区或中国台湾，不支持调用获取手机号一致性状态接口。

2、儿童账号不支持在TV设备上调用华为账号一键登录接口。

**处理步骤**

1、更换或注册一个注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的账号，重新触发该接口。

2、在TV设备上，登录成人账号调用华为账号一键登录接口。

[]()[]()

#### 1001500005 该功能被限制调用

**错误信息**

This function is restricted from being called.

**错误描述**

功能被限制调用。

**可能原因**

获取手机号一致性接口[getMobileNumberConsistency](../topics/security/authentication (华为账号应用统一认证服务).md#section571965992211)在24h内被调用超过50次。

**处理步骤**

1、应用需要控制手机号一致性接口的调用次数，保证24h内不超过50次。

2、若开发者调测过程中出现该错误码，可通过重启设备恢复。

[]()[]()

#### 1001502001 用户未登录华为账号

**错误信息**

The user has not logged in with HUAWEI ID.

**错误描述**

用户未登录华为账号。

**可能原因**

1、用户事先未登录华为账号。

2、Wearable设备未登录状态调用[LoginWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section42261825935)、[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)等方法进行华为账号登录。

**处理步骤**

1、如需引导用户登录，可调用[LoginWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section42261825935)，将forceLogin参数设置为true拉起登录页面引导用户登录，或引导用户在系统设置中登录华为账号。

2、Wearable设备需要用户前往设置或运动健康APP同步登录华为账号。

[]()[]()

#### 1001502002 应用未授权

**错误信息**

The application is not authorized.

**错误描述**

应用未授权。

**可能原因**

1、调用[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)且forceAuthorization参数设置为false的场景，用户未对应用授权。

2、idValue未按照[getMobileNumberConsistency](../topics/security/authentication (华为账号应用统一认证服务).md#section571965992211)接口中的[ConsistencyRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section168131411512)正确传入或用户已对应用取消授权。

3、idValue未按照[getHuaweiIDState](../topics/security/authentication (华为账号应用统一认证服务).md#section102884586336)接口中的[StateRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section9615740103819)正确传入或用户已对应用取消授权。

**处理步骤**

1、如需引导用户授权，可调用[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)，通过将forceAuthorization参数设置为true（不设置默认为true）拉起用户授权页面引导用户授权。

2、参考[ConsistencyRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section168131411512)中的idValue正确方式获取或重新授权。

3、参考[StateRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section9615740103819)中的idValue正确方式获取或重新授权。

[]()[]()

#### 1001502003 输入参数值无效

**错误信息**

Invalid input parameter value.

**错误描述**

输入参数值无效。

**可能原因**

1、接口传参异常，如调用授权API（[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)）时scope和permission都未传。

2、client_id未配置或配置错误。

3、如果是一键登录场景，则可能是传入的匿名手机号不正确，或是未调用授权API（[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)）获取匿名手机号。

4、未使用手动签名。

5、申请的Profile文件不包含APP ID，需要重新申请Profile文件。

**处理步骤**

1、检查接口参数。

2、检查module type为entry的模块下module.json5中的client_id是否配置或配置的值是否正确，请参考[配置Client ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-client-id)。

3、如果是上述原因3导致，需要传通过授权API（[AuthorizationWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section12940173017165)）获取到的匿名手机号。

4、请使用手动签名方式配置签名，请参考[配置签名和指纹](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints)。

5、请在AppGallery Connect中重新申请Profile文件并重新进行签名。在调试阶段，请参考[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)，完成Profile申请并重新手动签名；在发布阶段，请参考[申请发布Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)，完成Profile申请并重新手动签名。

[]()[]()

#### 1001502005 网络错误

**错误信息**

Network error.

**错误描述**

网络错误。

**可能原因**

设备未联网。

**处理步骤**

检查网络连接。

[]()[]()

#### 1001502009 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

华为账号服务器错误或其他内部错误等。

**处理步骤**

1、重启设备后重试。

2、若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354306240980&keyWord=Account Kit)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1001502012 用户取消授权

**错误信息**

The user canceled the authorization.

**错误描述**

用户取消授权。

**可能原因**

用户取消了授权操作。

**处理步骤**

由于用户主动取消授权，应用无需特殊处理。

[]()[]()

#### 1001502014 应用未申请scopes或permissions权限

**错误信息**

The app does not have the required scopes or permissions.

**错误描述**

应用未申请scopes或permissions权限。

**可能原因**

请参见Account Kit常见问题[1001502014 应用未申请scopes或permissions权限的可能原因和解决方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2)。

**处理步骤**

请参见Account Kit常见问题[1001502014 应用未申请scopes或permissions权限的可能原因和解决方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2)。

[]()[]()

#### 1001600001 网络不可用

**错误信息**

The network is unavailable.

**错误描述**

网络不可用。

**可能原因**

网络未连接或连接不好。

**处理步骤**

检查网络是否连接好。

[]()[]()

#### 1001600002 账号未登录

**错误信息**

The user has not logged in with HUAWEI ID.

**错误描述**

用户未登录华为账号。

**可能原因**

用户未事先登录华为账号。

**处理步骤**

如需引导用户登录，可调用[LoginWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section42261825935)，将forceLogin参数设置为true拉起登录页面引导用户登录，或引导用户在系统设置中登录华为账号。

[]()[]()

#### 1001600003 应用指纹证书校验失败

**错误信息**

Failed to check the fingerprint of the application bundle.

**错误描述**

应用指纹证书校验失败。

**可能原因**

1、client_id配置错误（例如：错配成项目的Client ID）。

2、应用的指纹证书未配置或配置错误。

**处理步骤**

1、检查module type为entry的模块下的module.json5配置文件中的Client ID是否正确，请参考[配置Client ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-client-id)。

2、检查AGC上应用的指纹证书，详情请见[添加公钥指纹](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview#section1726913517284)。

[]()[]()

#### 1001600004 应用未申请对应permissions权限

**错误信息**

The application does not have the required permissions.

**错误描述**

应用未申请对应permissions权限。

**可能原因**

未申请对应接口permissions权限。

**处理步骤**

申请对应权限。

[]()[]()

#### 1001600005 用户取消当前操作

**错误信息**

The user canceled the current operation.

**错误描述**

用户取消当前操作。

**可能原因**

用户取消了当前操作流程。

**处理步骤**

应用无需特殊处理。

[]()[]()

#### 1001600006 当前设备不支持此验证要素

**错误信息**

The requested verification factors are unavailable on the device.

**错误描述**

当前设备不支持此验证要素。

**可能原因**

用户二次验证中未配置验证要素，如手机号、安全手机号、邮箱、安全邮箱。

**处理步骤**

引导用户到系统设置>华为账号中心>个人信息或系统设置>华为账号中心>账号安全对验证要素进行配置。

[]()[]()

#### 1001600007 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

华为账号服务器错误或其他内部错误等。

**处理步骤**

1、重启设备后重试。

2、若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354306240980&keyWord=Account Kit)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1008100001 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

华为账号服务器错误或其他内部错误等。

**处理步骤**

1、重启设备后重试。

2、若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354306240980&keyWord=Account Kit)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1008100002 网络不可用

**错误信息**

The network is unavailable.

**错误描述**

网络不可用。

**可能原因**

网络未连接或连接不好。

**处理步骤**

检查网络是否连接好。

[]()[]()

#### 1008100003 账号未登录

**错误信息**

The user has not signed in with HUAWEI ID.

**错误描述**

用户未登录华为账号。

**可能原因**

用户未事先登录华为账号。

**处理步骤**

如需引导用户登录，可调用[LoginWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section42261825935)，将forceLogin参数设置为true拉起登录页面引导用户登录，或引导用户在系统设置中登录华为账号。

[]()[]()

#### 1008100004 应用指纹证书校验失败

**错误信息**

Failed to check the fingerprint of the app bundle.

**错误描述**

应用指纹证书校验失败。

**可能原因**

1、client_id配置错误（例如：错配成项目的Client ID）。

2、应用的指纹证书未配置或配置错误。

**处理步骤**

1、检查module type为entry的模块下的module.json5配置文件中的Client ID是否正确，详情请见[配置Client ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-client-id)。

2、检查AGC上应用的指纹证书，详情请见[添加公钥指纹](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview#section1726913517284)。

[]()[]()

#### 1008100005 应用未申请对应permissions权限

**错误信息**

The app does not have the required permissions.

**错误描述**

应用未申请对应permissions权限。

**可能原因**

未申请对应接口permissions权限。

**处理步骤**

确认对应接口permissions是否已申请，申请步骤参见[开发前提](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-choose-address-dev#section1061219267293)。

[]()[]()

#### 1008100006 用户未完成操作就退出了收货地址管理服务

**错误信息**

The user quits the shipping address management service without finishing.

**错误描述**

用户未完成操作就退出了收货地址管理服务。

**可能原因**

用户未完成收货地址选择操作，取消或者关闭了收货地址管理服务页面。

**处理步骤**

应用无需特殊处理。

[]()[]()

#### 1008100007 已登录的华为账号不支持收货地址管理服务

**错误信息**

The shipping address management service does not support the HUAWEI ID that is already signed in.

**错误描述**

已登录的华为账号不支持收货地址管理服务。

**可能原因**

已登录的华为账号注册地（如海外账号）不支持收货地址管理服务。

**处理步骤**

引导用户更换或注册一个中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为账号重新登录，或使用其他方式获取收货地址。

[]()[]()

#### 1010060001 用户取消发票服务

**错误信息**

The operation was canceled by the user.

**错误描述**

用户取消了发票服务。

**可能原因**

操作未完成用户就取消了操作。

**处理步骤**

应用无需特殊处理。

[]()[]()

#### 1010060002 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

华为账号服务器错误或其他内部错误等。

**处理步骤**

1、重启设备后重试。

2、若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354306240980&keyWord=Account Kit)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1010060003 应用指纹证书校验失败

**错误信息**

Failed to check the fingerprint of the app bundle.

**错误描述**

应用指纹证书校验失败。

**可能原因**

1、client_id配置错误（例如：错配成项目的Client ID）。

2、应用的指纹证书未配置或配置错误。

**处理步骤**

1、检查module type为entry的模块下的module.json5配置文件中的Client ID是否正确，请参考[配置Client ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-client-id)。

2、检查AGC上应用的指纹证书，详情请见[添加公钥指纹](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview#section1726913517284)。

[]()[]()

#### 1010060004 调用过于频繁

**错误信息**

Too frequent API calls.

**错误描述**

接口访问过频。

**可能原因**

接口访问间隔过短。

**处理步骤**

请控制接口调用频度。

[]()[]()

#### 1010060005 网络连接错误

**错误信息**

Network connection error.

**错误描述**

网络连接错误。

**可能原因**

网络未连接或连接不好。

**处理步骤**

检查网络是否连接好。

[]()[]()

#### 1010060006 账号未登录

**错误信息**

The HUAWEI ID is not signed in.

**错误描述**

用户未登录华为账号。

**可能原因**

用户未事先登录华为账号。

**处理步骤**

如需引导用户登录，可调用[LoginWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section42261825935)，将forceLogin参数设置为true拉起登录页面引导用户登录，或引导用户在系统设置中登录华为账号。

[]()[]()

#### 1010060007 发票抬头已存在

**错误信息**

Failed to create a invoice title because the title already exists.

**错误描述**

创建发票抬头失败，发票抬头已存在。

**可能原因**

发票抬头已存在。

**处理步骤**

应用无需特殊处理。

[]()[]()

#### 1010060008 华为账号不支持发票服务

**错误信息**

The invoice service does not support the logged HUAWEI ID.

**错误描述**

华为账号不支持发票服务。

**可能原因**

账号可能为海外账号。

**处理步骤**

引导用户更换或注册一个中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为账号重新登录，或使用其他方式获取发票抬头。

[]()[]()

#### 1005300001 用户未同意协议

**错误信息**

The user did not accept the agreement.

**错误描述**

用户未同意协议。

**可能原因**

使用华为账号登录组件时，未设置协议状态为ACCEPTED。

**处理步骤**

需要用户手动同意协议。

[]()[]()

#### 1005300002 用户未点击“华为账号一键登录”按钮

**错误信息**

The user did not click the HUAWEI ID login button.

**错误描述**

用户未点击“华为账号一键登录”按钮。

**可能原因**

开发者绕过点击“华为账号一键登录”按钮，直接调用continueLogin接口。

**处理步骤**

仅通过点击“华为账号一键登录”按钮，在拉起的协议弹框上点击同意并登录按钮时才调用continueLogin接口。

[]()[]()

#### 1009900002 未成年人模式未开启

**错误信息**

The minors mode is not enabled.

**错误描述**

未成年人模式未开启。

**可能原因**

未成年人模式未开启就调用验证密码请求。

**处理步骤**

[开启未成年人模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-app-turn-on-minorsprotection)。

[]()[]()

#### 1009900003 用户取消操作

**错误信息**

The user canceled the operation.

**错误描述**

用户取消操作。

**可能原因**

用户主动点击页面关闭按钮

**处理步骤**

处理用户取消的逻辑。

[]()[]()

#### 1009900005 未成年人模式已经开启

**错误信息**

The minors mode is already on.

**错误描述**

未成年人模式已经开启。

**可能原因**

未成年人模式已经开启，重复调用开启未成年人模式接口。

**处理步骤**

调用[getMinorsProtectionInfoSync](../topics/misc/minorsProtection (华为账号未成年人模式).md#section11505356101217)()或[getMinorsProtectionInfo](../topics/misc/minorsProtection (华为账号未成年人模式).md#section82313184131)()判断当前未成年人模式的状态，如果未成年人模式是关闭状态，再调用接口。

[]()[]()

#### 1009900006 未成年人模式已经关闭

**错误信息**

The minors mode is already off.

**错误描述**

未成年人模式已经关闭。

**可能原因**

未成年人模式已经关闭，重复调用关闭未成年人模式接口。

**处理步骤**

调用[getMinorsProtectionInfoSync](../topics/misc/minorsProtection (华为账号未成年人模式).md#section11505356101217)()或[getMinorsProtectionInfo](../topics/misc/minorsProtection (华为账号未成年人模式).md#section82313184131)()判断当前未成年人模式的状态，如果未成年人模式是开启状态，再调用接口，否则无需重复调用。

[]()[]()

#### 1009900007 不支持的账号

**错误信息**

Unsupported HUAWEI ID.

**错误描述**

不支持的账号。

**可能原因**

账号可能为海外账号。

**处理步骤**

登录中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）账号。

[]()[]()

#### 1009900011 服务不可用

**错误信息**

Service not available.

**错误描述**

服务不可用。

**可能原因**

设备进入隐私空间。

**处理步骤**

开发者可提醒用户进入“设置”>“隐私和安全”>“隐私空间”退出隐私空间，或者构建自己的未成年人模式。

[]()[]()

#### 1002500001 网络不可用

**错误信息**

The network is unavailable.

**错误描述**

网络不可用。

**可能原因**

网络未连接或连接不好。

**处理步骤**

检查网络是否连接好。

[]()[]()

#### 1002500002 账号未登录

**错误信息**

The user has not logged in with HUAWEI ID.

**错误描述**

用户未登录华为账号。

**可能原因**

用户未事先登录华为账号。

**处理步骤**

如需引导用户登录，可调用[LoginWithHuaweiIDRequest](../topics/security/authentication (华为账号应用统一认证服务).md#section42261825935)，将forceLogin参数设置为true拉起登录页面引导用户登录，或引导用户在系统设置中登录华为账号。

[]()[]()

#### 1002500003 应用指纹证书校验失败

**错误信息**

Failed to check the fingerprint of the application bundle.

**错误描述**

应用指纹证书校验失败。

**可能原因**

1、client_id配置错误（例如：错配成项目的Client ID）。

2、应用的指纹证书未配置或配置错误。

**处理步骤**

1、检查module type为entry的模块下的module.json5配置文件中的Client ID是否正确，请参考[配置Client ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-client-id)。

2、检查AGC上应用的指纹证书，详情请见[添加公钥指纹](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview#section1726913517284)。

[]()[]()

#### 1002500004 应用未申请对应permissions权限

**错误信息**

The application does not have the required permissions.

**错误描述**

应用未申请对应permissions权限。

**可能原因**

未申请对应接口permissions权限。

**处理步骤**

确认对应接口permissions是否已申请，申请步骤参见对应场景下的开发前提。

[]()[]()

#### 1002500005 用户取消验证

**错误信息**

The user canceled the verification of the HUAWEI ID.

**错误描述**

用户取消验证操作。

**可能原因**

用户取消了验证操作流程。

**处理步骤**

应用无需特殊处理。

[]()[]()

#### 1002500006 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

华为账号服务器错误、调用了当前设备不支持的API或其他内部错误等。

**处理步骤**

1、重启设备后重试。

2、请检查当前设备是否支持调用该API，建议先使用[canIUse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap#判断-api-是否可以使用)判断当前设备是否支持该API，再进行调用。

3、若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354306240980&keyWord=Account Kit)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1002500008 该华为账号不支持实名验证

**错误信息**

Real-name verification is not supported for the HUAWEI ID.

**错误描述**

该华为账号不支持实名验证。

**可能原因**

使用的华为账号注册地为中国境外、香港特别行政区、澳门特别行政区或中国台湾。

**处理步骤**

更换注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）账号再操作。

[]()[]()

#### 1002500009 实名渠道验证失败

**错误信息**

Real-name channel verification failed.

**错误描述**

实名渠道验证失败。

**可能原因**

1、实名认证渠道号传入错误。

2、实名认证渠道验证出错。

**处理步骤**

1、请检查实名认证渠道号是否正确。

2、请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354306240980&keyWord=Account Kit)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1002500011 您的面部与作为身份证明的面部图像不匹配

**错误信息**

Your face does not match your facial image as proof of identity.

**错误描述**

您的面部与作为身份证明的面部图像不匹配。

**可能原因**

您的面部与作为身份证明的面部图像不匹配。

**处理步骤**

引导用户重新验证人脸。

[]()[]()

#### 1002500012 未查询到实名信息

**错误信息**

No real-name information is found for the HUAWEI ID.

**错误描述**

未查询到实名信息。

**可能原因**

账号未实名。

**处理步骤**

引导用户到系统设置>华为账号中心>个人信息>实名认证条目下完成实名认证。

[]()[]()

#### 1002500013 姓名和身份证号码不匹配

**错误信息**

Your name and ID number do not match.

**错误描述**

姓名和身份证号码不匹配。

**可能原因**

1、用户输入有误。

2、用户可能最近变更了户口，或挂失身份证并补发了新卡，但该身份信息尚未与公安部同步。

**处理步骤**

1、重新输入姓名身份证号后重试。

2、如是原因2引起，建议用户隔段时间后再重试。

[]()[]()

#### 1002500014 实名验证尝试次数过多

**错误信息**

Too many real-name verification attempts.

**错误描述**

实名验证尝试次数过多。

**可能原因**

实名验证尝试次数过多。

**处理步骤**

24小时后重试。

[]()[]()

#### 1002500015 参数verificationToken不合法

**错误信息**

The verificationToken parameter is incorrectly set.

**错误描述**

参数verificationToken不合法。

**可能原因**

参数verificationToken不合法。

**处理步骤**

重新获取正确的verificationToken后重试。

[]()[]()

#### 1002500016 此设备不支持此API

**错误信息**

This device does not support this API.

**错误描述**

此设备不支持此API。

**可能原因**

在人脸核身场景下设备前置摄像头不可用。

**处理步骤**

修复该设备的前置摄像故障或更换前置摄像功能正常的设备后重试。