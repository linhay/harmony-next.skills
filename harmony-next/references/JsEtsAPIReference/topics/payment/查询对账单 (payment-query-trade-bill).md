[]()[]()

# 查询对账单

[]()[]()

#### 功能介绍

开发者可以通过该接口完成对账单离线表单文件的下载。

1. 无论是否产生交易，每日自动生成账单。如果查询日期超限或未生成，则不返回文件下载信息。其他情况会返回。
1. 账单下载后，建议遍历附件目录以获取“.csv”后缀的文件进行解析。
1. 解析表单内容时，需考虑表单更新，如新增列等场景。

[]()[]()

#### 使用场景

为方便开发者快速完成交易对账，可通过该接口获取华为支付商户对账单离线文件下载链接。

[]()[]()

#### 接口原型

承载协议

HTTPS GET

接口方向

开发者服务器 -> 华为支付服务器

接口URL

https://petalpay-developer.cloud.huawei.com.cn/api/v1/bill/trade-bill/downloadInfo?billDate=xxxxxx

数据格式

请求消息：Content-Type: application/json

响应消息：Content-Type: application/json

[]()[]()

#### 请求参数

**Request Header**

参数

是否必选

参数类型

描述

Content-Type

是

String

取值为：application/json; charset=UTF-8

PayMercAuth

是

String

取值为：[PayMercAuth](../../guides/数据模型说明.md#section11744172016145)的JSON字符串

**Request Query**

参数

是否必选

参数类型

描述

billDate

是

String

账单日期。只能查询九十日内的，需精确到某一天，格式：yyyyMMdd（如20210101）。

不支持下载当日账单，只能下载前一日24点前的账单数据，当日数据一般于次日 9 点后生成，特殊情况（如系统异常等）可能延迟。

[]()[]()

#### 请求示例

```ets
GET /v1/bill/trade-bill/downloadInfo?billDate=20221010 HTTP/1.1
Content-Type: application/json;charset=UTF-8
PayMercAuth: {"callerId":"10132120***","traceId":"202305151520201971407","time":1684135220018,"authId":"120291744647139***","headerSign":"qnZUnn7I+tI1********************U2A14dsRr1bZxIhSA+85LSmZd3YkzZwJlmZpgXA0oHptyUM=","bodySign":"lpFEmBEE4Ds5SgmW5oKq7VXVmVZg8YRwK1LZe/9L6I/yJ/fr1Pe1RaX++nlAeptIWOi5R/8i********************wmJKQzK9GM2xCp60RM="}
```

[]()[]()

#### 响应参数

**Response Header**

参数

是否必选

参数类型

描述

Content-Type

是

String

取值为：application/json; charset=UTF-8

**Response Body**

参数

是否必选

参数类型

描述

resultCode

是

String

结果码，“000000”表示成功，其他表示失败。

resultDesc

是

String

结果描述。

subCode

否

String

业务错误码。

subDesc

否

String

业务错误描述信息。

sign

是

String

签名值。用于开发者对响应报文进行防篡改验证。

billDownloadParam

否

[BillDownloadParam](../../guides/数据模型说明.md#section580851813465)

账单下载请求信息。有生成账单数据时返回。

[]()[]()

#### 响应示例

```ets
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
{
  "sign": "MEUCIGnmUY8Yg34Ma5NBwqYz********************zruzPoKn+cRVu/W3HH+8WGGJsV3TA=",
  "resultCode": "000000",
  "resultDesc": "Success",
  "billDownloadParam": {
    "headers": {
      "Authorization": "AWS4-HMAC-SHA256 Credential=BJIIJMUMOQKXDCODXVCG/2022110********************z-client-request-id;x-amz-content-sha256;x-amz-date, Signature=e7275216278aebc548f413f899eb2f4d82011ed479087f0055c702fa6addc8e5",
      "x-amz-content-sha256": "UNSIGNED-PAYLOAD",
      "x-amz-client-request-id": "20210863286224479792",
      "x-amz-date": "20221103T005326Z",
      "connection": "close",
      "Host": "petalpay-merchant-test-001.obs.cn-north-4.myhuaweicloud.cn",
      "user-agent": "Apache-HttpAsyncClient/4.1.2 (Java/1.8.0_272)",
      "Content-Type": "application/octet-stream"
    },
    "method": "GET",
    "downloadUrl": "https://petalpay-merchant-test-001.obs.cn-north-4.myhuaweicloud.cn/xxxxxx.zip"
  }
}
```

[]()[]()

#### 错误码

**resultCode**非400000的错误码请查看[公共错误码说明](../../errors/REST API错误码 (payment-error-code-rest).md#section1187515498410)。

返回码

错误码

**错误描述**

**解决方案**

400000

INVALID_ARGUMENTS

参数不合法

请检查请求参数。

400000

BILL_SWITCH_NOT_TURN_ON

账单开关没有打开

请检查并[打开账单开关](查询对账单 (payment-partner-agent-query-trade-bill).md#section199441211417)。

400000

UNKNOWN_ERROR

服务暂不可用，请稍后重试

稍后重试。

[]()[]()

#### 下载文件示例

```ets
RestTemplate restTemplate = new RestTemplate(new HttpComponentsClientHttpRequestFactory(HttpClients.createSystem()));
HttpHeaders headers = new HttpHeaders();
// billResponse为请求账单接口响应的对象
billResponse.getBillDownloadParam().getHeaders().forEach(headers::add);
HttpEntity<?> httpEntity = new HttpEntity<>(headers);
ResponseEntity<byte[]> responseEntity = restTemplate.exchange(billResponse.getBillDownloadParam().getDownloadUrl(), HttpMethod.GET, httpEntity, byte[].class, new Object[0]);
if (responseEntity.getStatusCode() == HttpStatus.OK) {
    // "./对账单2022xxxx.zip" 路径可自定义
    Files.write(Paths.get("./对账单2022xxxx.zip"), responseEntity.getBody());
}
```

[]()[]()

#### 对账单文件说明

**字段名**

**是否必填**

**描述**

**示例值**

商户名称

否

发起该笔交易下单的华为支付商户主体名称。

测试******商户

商户号

是

发起该笔交易下单的华为支付商户号。

1015******89

交易创建时间

是

指该笔交易的创建时间，格式为yyyy-MM-dd HH:mm:ss。

2022-08-25 10:29:19

交易完成时间

是

指该笔交易的支付成功时间，格式为yyyy-MM-dd HH:mm:ss。

2022-08-25 10:29:19

系统交易订单号

是

华为支付为该笔订单分配的订单号。

122082320******0000007764421

商户订单号

是

商户传入的该笔订单的商户订单号，对应下单接口里的mercOrderNo字段。

Pec4ae35b3ec0476de8e825bce******

交易状态

是

标识该笔交易的状态：

- 成功
- 失败

成功

交易类型

是

该笔订单类型，包括但不限于（后续可能新增）：

- 收单：通过华为支付收款的订单
- 退款：给用户退款的订单
- 代付：付款至指定银行账户的订单
- 商户充值：将银行资金充值至商户账户的订单
- 商户提现：将商户账户资金提现至银行的订单
- 分账：收款资金分账给合作方的订单
- 分账回收入金：分账后从合作方分账回收的订单
- 分账回收出金：分账后被合作方分账回收的订单
- 商户收单：通过华为支付收款的订单
- B2C转账：转账给用户支付账户的订单

收单

产品实例编号

否

指该笔订单使用的交易产品编号。

8478701144******88

产品名称

否

指该笔订单使用的交易产品名称。

借记卡快捷支付

银行名称

否

指该笔订单发生交易的银行。

工商银行

卡类型

否

指该笔订单发生交易的银行卡类型：

- 借记卡
- 贷记卡

借记卡

交易币种

是

指该笔订单的交易币种。

- CNY（人民币，默认值）

CNY

交易金额(元)

是

该笔订单的实际支付金额，最多保留到小数点后2位。

0.06

订单金额(元)

是

该笔订单的总金额，包括用户支付金额、优惠金额，最多保留到小数点后2位。

0.06

优惠金额(元)

否

指该笔订单在用户支付时的减免金额，最多保留到小数点后2位。

0

手续费金额(元)

是

该笔订单产生的交易手续费，最多保留小数点后2位。

0.01

合作方商户号

否

指分账订单的发起方商户号。

1015******89

合作方商户名称

否

指分账订单的发起方商户名称。

xyz

原系统交易订单号

否

退款或者分账原华为支付系统订单号。

124042317******0740873494880

原商户订单号

否

退款或者分账原商户订单号。

czl00120******554112

商户预留信息

否

预下单时的商户预留信息。

payload test

AppID

否

应用ID。

如果商户交易未配置AppID校验，则该字段信息为空。

5765880******8652727

用户标识

否

商户AppID生成的对应的openid。

如果商户交易未配置AppID校验，则该字段信息为空。

2248554******3012454