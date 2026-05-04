# 使用RSA密钥对分段签名验签（PKCS1模式）

本文根据华为开发者官网 `crypto-rsa-sign-sig-verify-pkcs1-by-segment` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment>
更新时间：2026-04-30 02:41:24

该页是“使用 RSA 密钥对（PKCS1 模式）签名验签”的分段版本，适合待处理数据较大、需要多次 `update` 输入数据的场景。

签名与验签流程的核心差异在于：
- 创建 `Sign` / `Verify` 实例并完成 `init` 后，不是一次性传入完整数据。
- 开发者可以多次调用 `update`，按顺序持续写入多个数据分段。
- 最终再调用 `sign` 或 `verify` 完成签名结果生成或验签校验。

其余密钥生成、算法规格选择、实例初始化方式，与非分段版 `PKCS1` 签名验签流程保持一致。
