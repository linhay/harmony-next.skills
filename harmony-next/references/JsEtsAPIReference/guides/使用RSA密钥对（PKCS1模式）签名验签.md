# 使用RSA密钥对（PKCS1模式）签名验签

本文根据华为开发者官网 `crypto-rsa-sign-sig-verify-pkcs1` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1>
更新时间：2026-04-30 02:41:24

该页说明了 ArkTS 下使用 RSA 密钥对并基于 `PKCS1` 填充模式进行签名与验签的标准流程。

签名侧的核心步骤：
- 通过 `cryptoFramework.createAsyKeyGenerator` 和 `AsyKeyGenerator.generateKeyPair` 生成 RSA 非对称密钥对。
- 通过 `cryptoFramework.createSign` 创建 `RSA1024|PKCS1|SHA256` 等规格的 `Sign` 实例。
- 使用私钥调用 `Sign.init` 初始化，再通过 `Sign.update` 传入待签名数据。
- 调用 `Sign.sign` 生成签名结果。

验签侧的核心步骤：
- 通过 `cryptoFramework.createVerify` 创建与签名参数一致的 `Verify` 实例。
- 使用公钥调用 `Verify.init` 初始化。
- 通过 `Verify.update` 传入待验签数据。
- 调用 `Verify.verify` 校验签名。

补充说明：
- 当前单次 `update` 的数据长度没有限制。
- 数据量较大时可以多次调用 `update`，也可以参考“分段签名验签”的官方配套说明。
