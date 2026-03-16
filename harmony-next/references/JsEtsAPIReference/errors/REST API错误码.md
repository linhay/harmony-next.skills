# REST API错误码

错误码

描述

处理建议

200

成功

-

400

参数错误

请参考返回信息，检查请求参数是否正确，并且需要确认商户服务器JDK版本需要大于1.8.211。如果检查正确，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

401

鉴权失败

请重新获取Authorization参数并填写在请求头中。

404

路径错误

请检查URL拼写是否正确。

405

权限错误

请检查是否在AGC网站上开启了钱包服务能力，请参见[创建Wallet Kit服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-preparations)。并检查申请的服务号（passTypeIdentifier）对应的卡券类型是否与调用的接口相对应。如果检查正确，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

429

服务不可用

请求接口次数超过调用量限额，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。