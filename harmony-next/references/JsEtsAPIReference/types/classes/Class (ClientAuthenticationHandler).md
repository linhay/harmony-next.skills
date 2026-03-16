# Class (ClientAuthenticationHandler)

Web组件返回的SSL客户端证书请求事件的处理对象。示例代码参考[onClientAuthenticationRequest事件](../../topics/misc/事件.md#ZH-CN_TOPIC_0000002497445228__onclientauthenticationrequest9)。

-

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本Class首批接口从API version 9开始支持。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### constructor9+

constructor()

ClientAuthenticationHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### confirm9+

confirm(priKeyFile : string, certChainFile : string): void

通知Web组件使用指定的私钥和客户端证书链。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明priKeyFilestring是存放私钥文件的完整路径。certChainFilestring是存放证书链文件的完整路径。

#### confirm10+

confirm(authUri : string): void

通知Web组件使用指定的凭据(从证书管理模块获得)。

需要配置权限：ohos.permission.ACCESS_CERT_MANAGER。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明authUristring是凭据的关键值。

支持的证书签名算法以及秘钥长度详见下表。

签名算法秘钥长度SSL_SIGN_RSA_PKCS1_SHA2561024（API version 18后开始支持）、2048、3072、4096SSL_SIGN_RSA_PKCS1_SHA3841024（API version 18后开始支持）、2048、3072、4096SSL_SIGN_RSA_PKCS1_SHA5121024（API version 18后开始支持）、2048、3072、4096SSL_SIGN_RSA_PSS_SHA2561024（API version 18后开始支持）、2048、3072、4096SSL_SIGN_RSA_PSS_SHA3841024（API version 18后开始支持）、2048、3072、4096SSL_SIGN_RSA_PSS_SHA5121024（API version 18后开始支持）、2048、3072、4096SSL_SIGN_ECDSA_SECP256R1_SHA256256SSL_SIGN_ECDSA_SECP384R1_SHA384384SSL_SIGN_ECDSA_SECP521R1_SHA512521

#### confirm22+

confirm(identity: string, credentialTypeOrCertChainFile: CredentialType | string): void

通知Web组件使用从证书管理模块获取的指定凭据和凭据类型。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

参数名类型必填说明identitystring是用于识别凭据的唯一标识值。credentialTypeOrCertChainFile[CredentialType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497605218__credentialtype22) | string是类型为[CredentialType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497605218__credentialtype22)时，代表凭据类型；类型为string时，表示证书链文件路径。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息801Capability not supported.

#### cancel9+

cancel(): void

通知Web组件取消相同host和port服务器发送的客户端证书请求事件。同时，相同host和port服务器的请求，不重复上报该事件。

**系统能力：** SystemCapability.Web.Webview.Core

#### ignore9+

ignore(): void

通知Web组件忽略本次请求。

**系统能力：** SystemCapability.Web.Webview.Core