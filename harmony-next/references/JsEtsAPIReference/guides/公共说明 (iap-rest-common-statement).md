[]()[]()

# 公共说明

接口协议：HTTPS

响应协议接口数据格式：JSON

协议接口数据字符编码：UTF-8

- 接口支持POST
- 编码：UTF-8
- Post Content Type：application/json;charset=UTF-8、application/x-www-form-urlencoded

  1. 应用内支付的所有服务端接口均要求使用标准的application/json进行访问，使用其他的MIME Type会导致部分场景出现无法预测的调用问题。
  1. 接口响应未来可能会新增字段。

- 认证信息基于请求Header指定，token是JWT格式：

Authorization: Bearer <JWT格式的token>

- 语言信息基于请求Header中Accept-Language指定，取值为标准的Locale

[]()[]()

#### 站点信息

站点

地址

中国

https://iap.cloud.huawei.com

[]()[]()

#### 加密套件

TLS版本

加密套件**（IANA名称）**

TLS 1.3

TLS_AES_128_GCM_SHA256

TLS_AES_256_GCM_SHA384

TLS_CHACHA20_POLY1305_SHA256

TLS 1.2

TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256

[]()[]()

#### 证书校验

如果服务端的证书未经验证或被篡改，客户端连接到的服务端可能不是预期的服务端，会导致中间人攻击、数据泄漏等安全问题。为保障连接安全，开发者服务器在访问IAP服务器时，必须验证IAP服务器提供的证书。验证包含两部分，首先是验证IAP服务器提供证书是否来自值得信任的来源，然后验证IAP服务器是否提供正确的证书。