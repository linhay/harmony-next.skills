# 华为账号一键登录（获取手机号和UnionID/OpenID）

本文根据华为开发者官网 `account-phone-unionid-login` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login>
更新时间：2026-04-29 07:35:50

## 概述
华为账号一键登录是基于OAuth 2.0协议标准和OpenID Connect协议标准构建的OAuth 2.0授权登录系统，应用可以通过华为账号一键登录能力快捷地获取华为账号用户的身份标识和手机号，快速建立应用内的用户体系。
优势：
利用系统账号的安全性和便利性，用户无需输入账号名和密码，无需复杂的安全验证，简化登录步骤，提高用户转化率。
提供系统验证过的手机号，关联应用已有用户。
实现Phone、Tablet、PC/2in1、TV设备一致的登录体验。

## 场景介绍
若应用需同时获取手机号和UnionID完成用户登录，Account Kit提供了同时获取手机号和UnionID的华为账号一键登录按钮。应用可以将华为账号一键登录按钮嵌入自有的登录页，使用登录按钮获取手机号和UnionID，实现用户登录。设备登录华为账号（该账号已绑定手机号）后，一键登录获取手机号可不依赖设备插SIM卡。
儿童账号一键登录场景：
用户使用儿童账号进行登录，点击一键登录会触发Account Kit默认提供的家长验密流程（Account Kit提供的验证页，暂不可自定义），家长验密完成后可获取用户的身份标识和手机号。并且TV设备暂不支持儿童账号。
手机号验证机制说明：
Account Kit调用系统能力获取华为账号登录设备上的SIM卡手机号码，与华为账号绑定的手机号进行校验（有网络即可，无需使用SIM卡移动数据）。用户点击一键登录按钮后，结合华为账号使用过程中账号所绑定的手机号短信验证记录，90天内有验证通过的记录，则返回该华为账号绑定的手机号；若90天内没有验证通过的记录，则触发Account Kit默认提供的短信验证流程（Account Kit提供的验证页，暂不可自定义），确保返回的手机号经过验证。

## 约束与限制
应用满足《常见类型移动互联网应用程序必要个人信息范围规定》中使用手机号的必要业务场景。
使用华为账号一键登录功能用户必须同意《华为账号用户认证协议》，当用户点击《华为账号用户认证协议》，系统浅色模式下应用需跳转到如下链接https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN，系统深色模式下跳转到https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN&bgmode=black。
应用在用户同意后获取到手机号，需要根据自身业务场景判断使用的方式，必要时增加其他安全验证手段，比如对二次放号的判断。
华为账号一键登录服务当前仅限中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户可用。
应用服务端获取华为账号绑定号码时，该服务器必须部署在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
华为账号一键登录支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。
仅支持企业开发者使用一键登录，个人开发者请使用华为账号登录或静默登录实现登录。

## 用户体验设计

## 登录页面UX设计规范
一键登录按钮的用户体验和UX设计需符合【华为账号一键登录】按钮规范，用户体验设计图2中的华为标志按钮可参考华为账号登录视觉规范中的样式三。不符合规范的UX设计可能会对应用上架和用户体验带来影响。一键登录按钮的样式设计具体可以参考华为账号登录按钮类型。

## 用户场景设计
用户使用华为账号一键登录能力，注册/登录应用时，可能存在多种场景，应用可参照以下流程，根据自身业务场景进行设计。
将UnionID/OpenID和手机号同时与应用账号建立关联，可以为用户带来更多便利的功能。如：实现静默登录、获取华为账号用户信息、获取华为账号风险等级等。实现免用户操作登录，获得安全快捷的应用登录体验。

## 业务流程

## 用户首次登录应用
若应用未接入过华为账号登录，不存在使用华为账号登录过的应用账号，请参照以下流程接入华为账号一键登录。
图1 华为账号一键登录（用户首次登录应用）流程图
流程说明：
预取号阶段（序号1-4）：
获取匿名手机号需要进行超时处理，应用可根据实际场景设置超时时间，推荐设置5秒保证用户体验。
若华为账号未登录，调用AuthorizationWithHuaweiIDRequest授权请求会返回1001502001 用户未登录华为账号错误码，此时应用需要展示其他登录方式进行应用登录。
展示一键登录页面阶段（序号5）：
获取到的匿名手机号需要展示在页面上并设置好隐私协议，设置登录按钮类型为LoginType.QUICK_LOGIN，展示包含LoginWithHuaweiIDButton组件的一键登录页面。应用可结合实际登录风控场景，通过组件参数传入风险等级标识获取华为账号风险等级，通过华为账号一键登录获取用户风险等级，对恶意账号进行风控，提升应用的安全等级。
点击一键登录关联用户账号阶段（序号6-16）：
用户同意协议后，点击华为账号一键登录按钮，应用可以通过HuaweiIDCredential获取到Authorization Code等数据。
将获取的Authorization Code数据传给应用服务端，应用服务端通过Authorization Code调用/oauth2/v6/quickLogin/getPhoneNumber接口获取用户完整手机号和UnionID、OpenID。
应用通过关联用户手机号和UnionID、OpenID完成用户登录。

## 用户非首次登录应用（可选）
应用接入过华为账号登录，存在使用华为账号登录过的用户账号，即根据UnionID/OpenID判断用户已关联过应用系统数据库，则需要参照以下流程开发。
图2 华为账号一键登录（用户非首次登录应用）流程图
流程说明：
应用调用AuthorizationWithHuaweiIDRequest授权请求获取AuthorizationWithHuaweiIDResponse响应结果中的Authorization Code。
应用服务端通过Authorization Code调用/oauth2/v6/quickLogin/getPhoneNumber接口获取用户相关信息。通过Authorization Code凭证获取用户信息可以有效避免黑客通过数据遍历、身份伪造、重放攻击等手段导致的安全风险。
应用对用户身份标识UnionID/OpenID、业务登录凭证SessionId信息进行认证后，通过UnionID/OpenID判断用户是否已关联应用系统数据库，如已关联，结合风控、安全因素及自身业务场景判断，可展示已关联的账号，由用户选择是否使用华为账号登录应用，或免用户操作，静默登录应用。
用户非首次登录应用流程请参考首次登录应用开发流程中的导入模块及获取匿名手机号，获取AuthorizationWithHuaweiIDResponse响应结果中的Authorization Code。可能存在的异常场景及处理方法，可参考表1 获取匿名手机号错误码处理。
正确获取到Authorization Code，开发者可将Authorization Code传给应用服务端用于获取用户身份标识（UnionID、OpenID），即可查询该用户是否已关联。
1）如已关联，结合风控、安全因素及自身业务场景判断，可展示已关联的账号，由用户选择是否使用华为账号登录应用，或免用户操作，静默登录应用，客户端开发结束。
2）如未关联，则参考首次登录应用开发流程中的展示一键登录页面并获取Authorization Code继续开发。

## 接口说明
华为账号一键登录按钮关键接口如下表所示：
接口名
描述
createAuthorizationWithHuaweiIDRequest(): AuthorizationWithHuaweiIDRequest
获取授权接口，通过AuthorizationWithHuaweiIDRequest传入一键登录的scope：quickLoginAnonymousPhone，即可在授权结果中获取到用户的匿名手机号和Authorization Code。
constructor(context?: common.Context)
创建授权请求Controller。
executeRequest(request: AuthenticationRequest): Promise<AuthenticationResponse>
通过Promise方式执行授权操作。
LoginWithHuaweiIDButton
华为账号Button登录组件。
该组件仅纯文本样式支持华为账号一键登录功能。开发者可以通过调整按钮的大小、圆角等参数以适配HarmonyOS应用登录界面。如果仍然不能满足开发者的诉求，可以使用Style的BUTTON_CUSTOM值定义按钮的文字颜色和背景色。

## 开发前提
在进行代码开发前，请先确认已完成开发准备工作。
若未配置签名和指纹，将报错1001500001 应用指纹证书校验失败。
若未申请“华为账号一键登录”权限，将报错1001502014 应用未申请scopes或permissions权限。
若应用开启了代码混淆，应用工程代码中获取到的quickLoginAnonymousPhone（匿名手机号）属性需要配置混淆白名单防止编译release包时被混淆，否则无法获取到匿名手机号。在调用获取匿名手机号方法工程模块的混淆文件obfuscation-rules.txt中添加：
# 开发者开启属性混淆需要配置quickLoginAnonymousPhone属性白名单防止其被混淆 -enable-property-obfuscation -keep-property-name quickLoginAnonymousPhone

## 客户端开发
开发者可参考下述内容自行开发，也可使用Account Kit为常见的三方开发框架（Flutter、H5、React-Native、uni-app）提供的SampleCode示例工程，用于接入华为账号一键登录能力，具体可参考三方开发框架接入华为账号一键登录进行开发。
