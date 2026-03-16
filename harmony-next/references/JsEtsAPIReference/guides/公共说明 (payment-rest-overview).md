[]()[]()

# 公共说明

[]()[]()

#### HTTPS安全要求

- 所有的API请求必须使用HTTPS。
- 支持的TLS协议版本：1.2 / 1.3。
- 支持的加密套件列表：

```ets
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
TLS_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
```

[]()[]()

#### HTTP方法说明

当前Payment Kit对外接口涉及GET及POST两种HTTP METHOD。

- **GET**：对应于查询场景。适用于从服务器查询资源数据，如查询订单信息、查询签约信息等。
- **POST**：对应于新建/更新资源场景，如预下单、退款请求等。

[]()[]()

#### 数据格式

请求和响应报文统一使用JSON格式。

[]()[]()

#### 字符编码

Payment Kit所有请求默认支持UTF-8编码，如采用其他编码格式的报文可能导致验签失败、字段解析失败等问题。

HTTP METHOD方式为GET的接口请求，请求URL如涉及参数拼接，拼接后完整的请求URL不建议带特殊字符。如有需要，建议对URL中的特殊字符进行编码处理。URL特殊字符参考但不限于：

+, 空格, ?, %, #, &, =

[]()[]()

#### 认证授权

- **认证(Authentication)**：认证操作确认调用者身份，防抵赖和数据篡改。所有对商户开放接口均需要商户在请求头中传递[PayMercAuth](数据模型说明.md#section11744172016145)字段，在开放网关认证通过后方可进行后续流程。
- **授权(Authorization)**：授权确保给定接口仅特定调用者才有权限调用。部分接口仅特定商户申请开通后方可使用。

[]()[]()

#### 签名规则

**签名场景：**商户云侧请求的请求头中参数签名。

**签名算法：**SHA256WithRSA/PSS 或者 SM2。

**开发步骤：**

1. 筛选：排除请求JSON串中sign字段，只保留sign以外的其他字段。
1. 排序拼接：按key值的ASCII码顺序排序，并使用&拼接，列表场景使用符号“=”连接。  具体可参考 [示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供 [Maven依赖（pay-java）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-server-connect#section379431652315)中SignStringUtil.java类的signString方法，排序拼接结果示例如下：

```ets
"allocationType=DELAY_ORDER_ALLOCATION&callbackUrl=https://www.xxxxxx.com/hw/pay/callback&currency=CNY&mercNo=xxxxxx&mercOrderNo=xxxxxx&totalAmount=2&tradeSummary=杂志报刊"
```

1. 签名：调用给定算法对排序后的串完成签名。

**SHA256WithRSA/PSS：**具体可参考[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供[Maven依赖（pay-java）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-server-connect#section379431652315)中RSAUtils.java类的signByRSAWithPSS方法。

**SM2：**具体可参考[Maven依赖（pay-java）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-server-connect#section379431652315)中Sm2Utils.java类中的sign方法。

加签内容参考：

```ets
POST请求：POST https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/preorder/create/app
{
    "appId": "5765880207854262xxx",
    "callbackUrl": "https://www.xxx.com/hw_notify",
    "currency": "CNY",
    "mercNo": "101723200xxx",
    "mercOrderNo": "2405171027547xxx",
    "payload": "shop|h8ahnJA8xxRXVw",
    "totalAmount": 5,
    "tradeSummary": "test",
    "subOrders": [
      {
        "mercNo": "101723200xxx",
        "mercOrderNo": "abcxxx1"
      },
      {
        "mercNo": "101723201xxx",
        "mercOrderNo": "abcxxx2"
      }
    ]
}
加签内容：appId=5765880207854262xxx&callbackUrl=https://www.xxx.com/hw_notify&currency=CNY&mercNo=101723200xxx&mercOrderNo=2405171027547xxx&payload=shop|h8ahnJA8xxRXVw&subOrders=mercNo=101723200xxx&mercOrderNo=abcxxx1,mercNo=101723201xxx&mercOrderNo=abcxxx2&totalAmount=5&tradeSummary=test

GET请求：GET https://petalpay-developer.cloud.huawei.com.cn/api/v2/aggr/transactions/merc-orders/20240507000000041809599950090xxx?mercNo=101540000089&sdkVersion=1.0.0
加签内容：/api/v2/aggr/transactions/merc-orders/20240507000000041809599950090xxx?mercNo=101540000089&sdkVersion=1.0.0
```

字段值设置为null时，字段可不参与签名，设置为空字符时，则必须参与签名。

[]()[]()

#### 常用语言SHA256WithRSA/PSS加签示例代码参考

**go语言**

加签实现示例代码：

```ets
package main
import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"fmt"
	"testing"
)
func signSha256WithRsaPSS(message, privateKeyStr string) (string, error) {
	privateKey, err := getPrivateKey(privateKeyStr)
	if err != nil {
		return "", err
	}
	hasher := sha256.New()
	hasher.Write([]byte(message))
	hashedMessage := hasher.Sum(nil)
	opts := rsa.PSSOptions{
		SaltLength: rsa.PSSSaltLengthEqualsHash,
		Hash:       crypto.SHA256,
	}
	signature, err := rsa.SignPSS(rand.Reader, privateKey, crypto.SHA256, hashedMessage, &opts)
	if err != nil {
		return "", err
	}
	return base64.StdEncoding.EncodeToString(signature), nil
}

func getPrivateKey(privateKeyStr string) (*rsa.PrivateKey, error) {
	decoded, err := base64.StdEncoding.DecodeString(privateKeyStr)
	if err != nil {
		return nil, err
	}
	privateKey, err := x509.ParsePKCS8PrivateKey(decoded)
	if err != nil {
		return nil, err
	}
	rsaPrivateKey, ok := privateKey.(*rsa.PrivateKey)
	if !ok {
		return nil, err
	}
	return rsaPrivateKey, nil
}

func TestRsaSign(t *testing.T) {
	signature, err := signSha256WithRsaPSS("加签排序拼接内容","私钥")
	fmt.Println(signature, err)
}
```

**JavaScript语言**

javascript可通过jsrsasign模块实现，如已[安装node环境](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-certificates-config#li971411417543)，可执行如下命令安装jsrsasign模块。

```ets
npm install jsrsasign
```

加签实现示例代码：

```ets
const jsrsasign = require('jsrsasign');
function signSha256WithRsaPSS(plainData, privateStr) {
  let rsa = new jsrsasign.RSAKey();
  // PEM 格式的私钥
  const priKey = `-----BEGIN PRIVATE KEY-----\n${privateStr}\n-----END PRIVATE KEY-----\n`;
  rsa = jsrsasign.KEYUTIL.getKey(priKey);
  const sig = new jsrsasign.KJUR.crypto.Signature({
    alg: 'SHA256withRSAandMGF1',
  });
  sig.init(rsa);
  sig.updateString(plainData);
  return jsrsasign.hextob64(sig.sign());
}
let signature = signSha256WithRsaPSS("加签排序拼接内容","私钥");
console.info(signature)
```

**python语言**

python可通过cryptography模块实现，可先执行如下命令安装cryptography模块：

```ets
pip install cryptography
```

加签实现示例代码：

```ets
import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

def signSha256WithRsaPSS(private_key_str, message):
    # PEM 格式的私钥
    prikey_content = "-----BEGIN PRIVATE KEY-----\n" + private_key_str +"\n-----END PRIVATE KEY-----\n";
    private_key = load_pem_private_key(data=prikey_content.encode("utf-8"), password=None, backend=default_backend())

    # 使用 RSA-PSS 算法生成签名
    signature = private_key.sign(
        message.encode("utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.DIGEST_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

message = "加签排序拼接内容"
private_key_str = "私钥"
signature = signSha256WithRsaPSS(private_key_str, message)
print(signature)
```

**php语言**

php可通过phpseclib加密库实现，如已安装composer环境，可先通过以下命令导入phpseclib：

```ets
composer require phpseclib/phpseclib
```

phpseclib2加签实现示例代码：

```ets
<?php
require_once 'vendor/autoload.php';
use phpseclib\Crypt\RSA;

function signSha256WithRsaPSS($content, $privateKeyStr) {
    try {
        $privateKey = "-----BEGIN PRIVATE KEY-----\n" . $privateKeyStr ."\n-----END PRIVATE KEY-----";
        $signer = new \phpseclib\Crypt\RSA();
        $signer->loadKey($privateKey, $password = false);
        $signer->setHash('sha256');
        $signer->setSignatureMode(RSA::SIGNATURE_PSS);
        $signer->setMGFHash('sha256');
        $signature = $signer->sign($content);

        $sign = base64_encode($signature);
        return $sign;
    } catch (Exception $e) {
        echo $e->getMessage();
    }
    return null;
}
$data = "加签排序拼接内容";
$privateKeyStr = "私钥";
echo signSha256WithRsaPSS($data, $privateKeyStr)
?>
```

phpseclib3加签实现示例代码：

```ets
<?php
require_once 'vendor/autoload.php';

use phpseclib3\Crypt\PublicKeyLoader;
use phpseclib3\Crypt\RSA;

function signSha256WithRsaPSS($data,$rsa_key){
    $key = "-----BEGIN PRIVATE KEY-----\n" . $rsa_key . "-----END PRIVATE KEY-----";
    $private = PublicKeyLoader::load($key, $password = false);
    $private = $private->withPadding(RSA::SIGNATURE_PSS);
    return base64_encode($private->sign($data));
}

$data = "加签排序拼接内容";
$privateKeyStr = "私钥";
echo signSha256WithRsaPSS($data, $privateKeyStr);
?>
```

**C#语言**

C#可通过BouncyCastle库来实现，如已安装 [.NET SDK](https://dotnet.microsoft.com/download)，可先执行如下命令添加BouncyCastle：

```ets
dotnet add package BouncyCastle
```

加签实现示例代码：

```ets
using System.Text;
using Org.BouncyCastle.OpenSsl;
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Security;
using Org.BouncyCastle.Crypto.Signers;
using Org.BouncyCastle.Crypto.Engines;
using Org.BouncyCastle.Crypto.Digests;
class SignProgram
{
    public static void Main(string[] args)
    {
        string res = RSASign("加签排序拼接内容","私钥");
        Console.WriteLine("result：" + res);
    }
    public static string RSASign(string datastr,string privateStr)
    {
        var priKey = "-----BEGIN PRIVATE KEY-----\n"+ privateStr +"\n-----END PRIVATE KEY-----\n";
        byte[] data = Encoding.UTF8.GetBytes(datastr);
        // 创建PSS签名器
        var signer = new PssSigner(new RsaEngine(), new Sha256Digest());
        AsymmetricKeyParameter rsaPrivateKey = null;
        using (var stringReader = new StringReader(priKey))
        {
            var pemReader = new PemReader(stringReader);
            rsaPrivateKey = pemReader.ReadObject() as AsymmetricKeyParameter;
        }
        signer.Init(true, new ParametersWithRandom(rsaPrivateKey, new SecureRandom()));
        signer.BlockUpdate(data, 0, data.Length);
        byte[] signature = signer.GenerateSignature();
        return Convert.ToBase64String(signature);
    }
}
```

[]()[]()

#### 验签规则

**验签场景****：**商户需要对来自Payment Kit服务器的信息做验签，验证签名信息身份来自Payment Kit服务器。商户服务器对华为支付服务器返回的回调通知请求参数和退款通知请求参数验签。

**验签算法****：**SM2。

**开发步骤：**确认验证签名的公钥证书、确认参与签名字段将待签名字段转换为“key=value”并以符号“&”拼接、使用验签方法验证签名。

1. 获取华为支付公钥，此处公钥证书为[华为支付商户平台](https://petalpay-merchant.cloud.huawei.com/)获取的证书，可参见[下载华为支付证书](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-certificates-config#section377312802116)。
1. 获取参与签名的字段，转换为map并将map的“key-value”排序后以符号“&”拼接。
1. 使用SM2算法进行验签，具体参考[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)引入华为支付提供[Maven依赖（pay-java）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-server-connect)中VerifyTools.java类的verifySign方法。

因业务发展需要，接口字段可能发生变动，建议验签功能实现可扩展——即“先对回调通知的请求体进行验签处理，再转换成业务对象处理”，以确保在字段有变化时也可以正常验签。

[]()[]()

#### 常用语言SM2验签示例代码参考

**JavaScript语言**

javascript可通过sm-crypto模块实现，如已[安装node环境](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-certificates-config#li971411417543)，可执行如下命令安装：

```ets
npm install sm-crypto
```

验签实现示例代码：

```ets
const SmCrypto = require('sm-crypto');
function signSM2Verify(plainData, sign, publicStr) {
  let signHex1 = base64ToHex(sign)
  console.info("plainData: " + plainData)
  console.info("sign: " + sign)
  console.info("sign hex: " + signHex1)
  return SmCrypto.sm2.doVerifySignature(plainData, signHex1, publicStr, {
    hash: true,
    der: true
  })
}
function base64ToHex(base64String) {
  const buffer = Buffer.from(base64String, 'base64');
  return buffer.toString('hex');
}
let signSM2VerifyRes = signSM2Verify(
    "验签排序拼接内容",
    "验签sign",
    "验签公钥"
);
console.info(signSM2VerifyRes)
```

[]()[]()

#### 通知回调接口说明

- 对于回调通知，如果Payment Kit未收到application/json类型响应的数据，或收到应答数据不是{"resultCode":"000000","resultDesc":"Success."} ，Payment Kit会通过一定的周期定期重新发起通知，但不保证通知最终能成功。
- 相同通知可能多次重复发送给商户服务器，商户服务器需要正确实现以应对重复请求，处理建议：

  - 在商户服务器收到通知进行业务处理前先检查对应业务状态，对于未处理过的场景才进行业务处理。已处理的场景则直接返回成功。
  - 在业务处理时，合理设计同步机制防止并发问题。

- 如果在预期时间内未收到Payment Kit的回调请求，请排查提供的callbackUrl网络是否连通。如排除网络连通性问题，请调用同步查询接口确认订单状态。排查建议：

  - 确认callbackUrl为商户系统真实地址，保证url中的域名或IP是外网可以正常访问的。不能填写localhost、127.0.0.1、192.168.x.x、10.xx.xx.xx等。
  - callbackUrl必须为https://开头的完整地址。

- 对于收到的异步回调请求，请务必进行验签处理并在验签通过后进行后续业务流程。否则可能因为信息泄露导致对商户潜在的攻击，造成资金损失。
- 因商户自身系统实现问题导致的业务异常，资金损失，由商户自行承担。
- 如商户对支付回调地址有IP防火墙策略限制，需要对以下网段开通允许名单，后续有变动时会在此处更新。

  - 124.70.118.0/24
  - 139.159.166.0/24

- 商户系统收到回调通知时，需要在**3秒内**返回应答响应，否则华为支付会认为通知失败，会触发重试机制。
- 商户系统收到异步通知并返回{"resultCode":"000000","resultDesc":"Success."}时，服务器异步通知参数callbackId才会失效。同一个异步通知请求的多次重试callbackId是不变的。

**接口约束**

- 请勿将开发者的服务器的IP允许清单设置成用于限制华为的出口IP地址。IP允许清单本身并不能提高安全性且会给业务发展带来约束，在消息层面已有更安全的RSA签名机制条件下，没有存在价值。若开发者不遵守此约定带来的后果将由开发者自行承担。
- 地址必须支持HTTPS协议且具有合法商用证书，否则无法正常接收通知消息。
- 支持的TLS协议版本：1.2 / 1.3。
- 支持的加密套件列表：

```ets
TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
TLS_DHE_DSS_WITH_AES_128_GCM_SHA256
TLS_DHE_DSS_WITH_AES_256_GCM_SHA384
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_AES_128_GCM_SHA256
```