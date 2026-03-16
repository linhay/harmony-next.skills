[]()[]()

# REST API错误码

若问题仍无法解决，请选择[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 公共错误码说明

Payment Kit开放网关会对开发者的应用/元服务接口的非业务类型调用返回错误码。

返回码

结果描述

**错误码**

**错误描述**

解决方案

000000

Success

-

-

不涉及。

100000

权限不足

INSUFFICIENT_PERMISSION

商户权限受限

在商户平台检查并配置该产品权限。

200000

缺少必选参数

MISSING_AUTH_HEADER

缺少鉴权参数

在请求头中构建并传入对应的鉴权信息。

MISSING_TRACER_ID

缺少tracerId参数

检查请求参数，每次请求传入唯一的traceId。

MISSING_HEADER_SIGN

缺少headSign参数

检查请求参数，传入headerSign。

MISSING_CALLER_ID

缺少callerId参数

检查请求参数，传入callerId，对应于商户号。

MISSING_BODY_SIGN

缺少bodySign参数

检查请求参数，传入bodySign。

MISSING_AUTH_ID

缺少authId参数

检查请求参数，传入商户对应的authId。

MISSING_TIME

缺少时间戳参数

检查请求参数，传入当前时间戳信息。

MISS_ACCESS_TOKEN

缺少accessToken参数

检查请求头参数MISS_ACCESS_TOKEN是否正确传递。

MISS_PETAL_PAY_SIGN_KEY_ID

缺失petalpaySignKeyId参数

检查请求头参数petalpaySignKeyId是否正确传递。

MISS_PETAL_PAY_ENC_KEY_ID

缺失petalpayEncKeyId参数

检查请求头参数petalpayEncKeyId是否正确传递。

MISS_DEVELOPER_SIGN_KEY_ID

缺失developerSignKeyId参数

检查请求头参数developerSignKeyId是否正确传递。

200001

非法的参数

INVALID_AUTH_HEADER

鉴权信息无效

检查请求头，传入正确的鉴权信息。

INVALID_TRACER_ID

tracerId参数无效

检查请求参数，传入正确的traceId。

INVALID_AUTH_ID

authId参数无效

检查请求参数，传入正确的authId。

INVALID_TIME

时间戳参数无效

检查请求参数，传入正确的时间戳。

INVALID_SESSION_KEY

sessionKey参数无效

检查请求参数，传入正确的sessionKey。

INVALID_PUB_KEY

商户公钥无效

检查请求参数，确认已生成并上传公钥。

INVALID_DUPLICATE_REQUEST

无效的重复请求

检查请求参数，每次请求需要生成新的traceId。

INVALID_PARAMETER

参数无效

检查请求参数，传入正确的参数。

INVALID_CALLER_ID

callerId参数无效

检查鉴权请求头callerId字段传递是否正确（如类型、特殊字符、长度等）。

INVALID_PAY_DEV_AUTH

invalid payDevAuth header

检查鉴权请求头payDevAuth 是否正确传递。

UNSUPPORTED_PETAL_PAY_ENC_KEY_ID

unsupported PetalPayEncKeyId

检查鉴权参数PetalPayEncKeyId是否正确传递。

检查接口入参敏感字段加密所用公钥是否匹配。

UNSUPPORTED_PETAL_PAY_SIGN_KEY_ID

unsupported PetalPaySignKeyId

检查鉴权参数PetalPaySignKeyId是否正确传递。

UNSUPPORTED_DEVELOPER_SIGN_KEY_ID

unsupported developerSignKeyId

检查鉴权参数developerSignKeyId是否正确传递。

检查请求加签所用公钥是否匹配。

200002

签名错误

INVALID_SIGNATURE

无效签名

检查请求参数，按说明完成签名并传入正确的签名参数。

300000

调用频率受限

CALL_FREQUENCY_LIMITED

API调用次数超限

降低请求并发量。

400000

业务处理失败

对应的错误码和说明见下方具体接口说明。

500000

服务不可用

UNKNOW_ERROR

服务暂不可用，请稍后重试

稍后重试。

[]()[]()

#### 业务错误码

响应的错误码示例，具体请参考业务接口（**resultCode**非400000的错误码请查看[公共错误码说明](#section1187515498410)）

返回码

错误码

错误描述

解决方案

400000

UNKNOW_ERROR

服务暂不可用，请稍后重试

稍后重试。

400000

INVALID_ARGUMENTS

参数不合法

检查请求参数。

400000

PAY_ORDER_NOT_EXIST

支付订单号不存在

检查入参订单号是否正确。

400000

MERC_ORDER_NOT_EXIST

商户订单号不存在

检查入参订单号是否正确。

400000

INVALID_MERCNO

无效商户号

检查入参商户号是否正确。

400000

REJECTED_BY_RISK_CONTROL

风控拒绝

咨询华为支付团队，[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

400000

NO_MATCH_MATCHING_PRODUCT

未匹配到商户产品

检查商户产品是否配置正确。

400000

CHECK_ORDER_STATUS

订单状态异常

请检查是否使用相同订单重复下单。

400000

BANK_CARD_NOT_SUPPORT

银行卡不支持

更换其他银行卡重试。

400000

CHECK_ACCOUNT_STATUS

支付账号异常

请检查支付账号状态。

400000

CHECK_MERC_STATUS

商户状态异常

请检查商户状态是否正常。

400000

MERC_NOT_SUPPORT_REFUND

商户不支持退款

请检查商户是否具有退款权限。

400000

CHECK_AMOUNT_INVALID

金额校验失败

检查传入金额是否合法。

400000

CHECK_ACCOUNT_BALANCE

账户余额不足

查看商户账户余额。

400000

RETRY_TOO_MANY

重试次数超限，请换单重试

换单重新请求。

400000

NOT_SETTLEMENT_DATE

非结算日，账单未生成

请修改入参日期重试。

400000

INVALID_APPID

appId不匹配

检查appId是否正确且已经绑定商户号。

400000

BILL_SWITCH_NOT_TURN_ON

账单开关没有打开

前往“[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)”的“功能设置”中开启相应的账单开关。

400000

INVALID_SUB_MERCNO

权限异常，请求传递的子商户号不是验签商户的子商户

请检查子商户号是否和验签商户正确关联。

400000

ORDER_CONCURRENT_ERROR

订单并发错误

解决方案：

1. 一笔普通收单多次退款，时间间隔要在1分钟以上。

2. 合单多笔子单退款，时间间隔要在1分钟以上。

400000

NOT_SUPPORTED_OPERATION

不支持的操作

请确认操作是否允许，如无法确认可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

400000

RESTRICTED_USER_ACCOUNT

用户账户受限

请确认用户账户状态是否正常。

400000

RESTRICTED_USER_TRANSACTION

用户交易受限

请确认用户状态是否正常。

400000

RESTRICTED_MERCHANT_TRANSACTION

商户交易受限

请检查商户支付账号状态是否正常。

400000

CHECK_CONTRACT_STATUS

签约号无效

1. 请确认是否存在签约关系。
1. 检查签约号输入是否正确。

400000

NOT_IN_VALIDITY_PERIOD

不在有效期内

请检查订单是否已过期，不再支持操作。

400000

PAYMENT_ACCOUNT_NOT_ENABLE

支付账户未开通

请检查是否开通支付账户。

400000

CUST_NOT_EXIST

用户不存在或已销户

请确认操作的华为账号状态是否正常或已销户。

400000

OPERATION_NOT_AUTHORIZED

操作未授权

服务商代特约商户发起退款需要申请授权。

400000

RESTRICTED_TRANSACTION

交易受限

交易存在风险，无法正常交易，请确认。无法确认可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

400000

WITHHOLD_OVER_TIMES

代扣次数超限

请间隔四小时后再重试。

400000

INVALID_PAYMENT_TYPE

用户无有效支付方式

请检查用户是否存在可用支付方式。

400000

CHECK_TRANSACTION_ORDER_STATUS

交易订单状态异常

请检查是否使用相同的商户订单号重复预下单。

400000

NEED_CHANGE_ORDER

请换单重试

更换商户订单号重试。

400000

ORDER_NOT_SUPPORT

订单不支持

确认操作是否正确，

无法确认可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。