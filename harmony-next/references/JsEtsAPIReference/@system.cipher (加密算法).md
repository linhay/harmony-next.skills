# @system.cipher (加密算法)

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始废弃， 建议使用[@ohos.security.cryptoFramework的Cipher](@ohos.security.cryptoFramework (加解密算法库框架).md#ZH-CN_TOPIC_0000002497445368__cipher)替代。

#### 导入模块

```ets
import cipher from '@system.cipher';
```

#### CipherResponse

调用cipher接口后，返回的内容。

**系统能力**：SystemCapability.Security.Cipher

名称类型只读可选说明textstring否否返回的内容。

#### CipherRsaOptions

调用cipher rsa方法时，传入的参数。

**系统能力**：SystemCapability.Security.Cipher

名称类型必填说明actionstring是

加密类型，可选项有：

1. encrypt 加密；

2. decrypt 解密。

textstring是待加密或解密的文本内容。待加密的文本内容应该是一段普通文本，长度不能超过 keySize / 8 - 66，其中 keySize 是密钥的长度（例如密钥长度为 1024 时，text 不能超过 62 个字节）。待解密的文本内容应该是经过 base64 编码的一段二进制值。base64 编码使用默认风格。keystring是加密的密钥，RSA的密钥。加密时key为公钥，解密时key为私钥。transformationstring否RSA算法的填充项，默认为RSA/None/OAEPWithSHA256AndMGF1Padding。success(data: [CipherResponse](#ZH-CN_TOPIC_0000002529445313__cipherresponse)) => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。complete() => void否接口调用结束的回调函数。

#### CipherAesOptions

调用cipher aes方法时，传入的参数。

**系统能力**：SystemCapability.Security.Cipher

名称类型必填说明actionstring是

加密类型，可选项有：

1. encrypt 加密；

2. decrypt 解密。

textstring是待加密或解密的文本内容。待加密的文本内容应该是一段普通文本。待解密的文本内容应该是经过 base64 编码的一段二进制值。base64 编码使用默认风格。keystring是加密或解密使用到的密钥，经过 base64 编码后生成的字符串。transformationstring否AES算法的加密模式和填充项，默认AES/CBC/PKCS5Padding。ivstring否AES加解密的初始向量，经过base64编码后的字符串，默认值为key值。ivOffsetstring否AES加解密的初始向量偏移，默认值0，仅支持0。ivLenstring否AES加解密的初始向量字节长度，当前为预留字段，默认值16，仅支持16。success(data: [CipherResponse](#ZH-CN_TOPIC_0000002529445313__cipherresponse)) => void否接口调用成功的回调函数。fail(data: string, code: number) => void否接口调用失败的回调函数。complete() => void否接口调用结束的回调函数。

#### cipher.rsa

rsa(options: CipherRsaOptions): void

RSA 算法加解密。

**系统能力：** SystemCapability.Security.Cipher

**参数：**

参数名类型必填说明options[CipherRsaOptions](#ZH-CN_TOPIC_0000002529445313__cipherrsaoptions)是rsa加解密需要设置的参数。

**示例：**

```ets
export default {
  rsa() {
    cipher.rsa({
      //加密。
      action: 'encrypt',
      //待加密的文本内容。
      text: 'hello',
      //base64编码后的加密公钥。
      key:
     'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCx414QSP3RsYWYzf9mkBMiBAXo\n' +
     '6S7Lpva1fKlcuVxjoFC1iMnzD4mC0uiL4k5MNi43J64c7dbqi3qAJjdAtuwQ6NZJ\n' +
     '+Enz0RzmVFh/4yk6lmqRzuEFQqhQqSZzaLq6sq2N2G0Sv2Xl3sLvqAfe2HNm2oBw\n' +
     'jBpApTJ3TeneOo6Z5QIDAQAB',
      success: function(data) {
        console.log(`handling success:${data.text}`);
      },
      fail: function(data, code) {
        console.log(`### cipher.rsa encrypt fail ### ${code}:${data}`);
      },
      complete: function() {
        console.log(`operation complete!`);
      }
      });
      cipher.rsa({
        //解密：
        action: 'decrypt',
        //待解密的内容，是base64编码后的一段二进制值，解密后是文本内容“hello”。
        text:
       'EPeCFPib6ayKbA0M6oSywARvFZ8dFYfjQv3nY8ikZGtS9UHq2sLPvAfpeIzggSiCxqbWeCftP1XQ\n' +
       'Sa+jEpzFlT1qoSTunBbrYzugPTajIJDTg6R1IRsF/J+mmakn0POVPvi4jCo9wqavB324Bx0Wipnc\n' +
       'EU5WO0oBHo5l4x6dTpU=',
         //base64编码后的解密私钥。
         key:
        'MIICXgIBAAKBgQCx414QSP3RsYWYzf9mkBMiBAXo6S7Lpva1fKlcuVxjoFC1iMnz\n' +
        'D4mC0uiL4k5MNi43J64c7dbqi3qAJjdAtuwQ6NZJ+Enz0RzmVFh/4yk6lmqRzuEF\n' +
        'QqhQqSZzaLq6sq2N2G0Sv2Xl3sLvqAfe2HNm2oBwjBpApTJ3TeneOo6Z5QIDAQAB\n' +
        'AoGBAKPNtoRQcklxqo+2wQP0j2m3Qqnib1DggjVEgb/8f/LNYQSI3U2QdROemryU\n' +
        'u3y6N3xacZ359PktTrRKfH5+8ohmHGhIuPAnefp6bLvAFUcl4t1xm74Cow62Kyw3\n' +
        'aSbmuTG98dxPA1sXD0jiprdtsq2wQ9CoKNyY7/d/pKoqxNuBAkEA4GytZ60NCTj9\n' +
        'w24jACFeko5YqCFY/TTLoc4SQvWtFMnimRPclLZhtUIK0P8dib71UFedx+AxklgL\n' +
        'A5gjcfo+2QJBAMrqiwyCh3OQ5DhyRPDwt87x1/jg5fy4hhete2ufSf2FoQCVqO+w\n' +
        'PKoljdXmJeS6rGgzGibstuHLrP3tcIho4+0CQD3ZFWzF/xq0jxKlrpWhnJuNCRfE\n' +
        'oO6e9yNvVA8J/5oEDSOcmqSNIp4+RhbUx8InUxnCG6Ryv5aSFu71pYcKrPkCQQCL\n' +
        'RUGcm3ZGTnslduB0knNF+V2ndwzDUQ7P74UXT+PjurTPhujFYiuxCEd6ORVnEOzG\n' +
        'M9TORIgdH8MjIbWsGnndAkEAw9yURDaorE8IYPLF2IEn09g1uzvWPs3phDb6smVx\n' +
        '8GfqIdUNf+aCG5TZK/kXBF1sqcsi7jXMAf4jBlejVbSVZg==',
         success: function(data) {
           console.log(`handling success:${data.text}`);
         },
         fail: function(data, code) {
           console.log(`### cipher.rsa decrypt fail ### ${code}:${data}`);
         },
         complete: function() {
           console.log(`operation complete!`);
         }
       });
   }
}
```

#### cipher.aes

aes(options: CipherAesOptions): void

AES 算法加解密。

**系统能力：** SystemCapability.Security.Cipher

**参数：**

参数名类型必填说明options[CipherAesOptions](#ZH-CN_TOPIC_0000002529445313__cipheraesoptions)是aes加解密需要设置的参数。

**示例：**

```ets
export default {
  aes() {
    cipher.aes({
      //加密。
      action: 'encrypt',
      //待加密的文本内容。
      text: 'hello',
      //base64编码后的密钥。
      key: 'NDM5Qjk2UjAzMEE0NzVCRjlFMkQwQkVGOFc1NkM1QkQ=',
      transformation: 'AES/CBC/PKCS5Padding',
      ivOffset: '0',
      ivLen: '16',
      success: function(data) {
        console.log(`handling success:${data.text}`);
        },
      fail: function(data, code) {
        console.log(`### cipher.aes encrypt fail ### ${code}:${data}`);
        },
      complete: function() {
        console.log(`operation complete!`);
      }
    });
    cipher.aes({
      //解密：
      action: 'decrypt',
      //待解密的内容，是base64编码后的一段二进制值。
      text: '1o0kf2HXwLxHkSh5W5NhzA==',
       //base64编码后的密钥。
       key: 'NDM5Qjk2UjAzMEE0NzVCRjlFMkQwQkVGOFc1NkM1QkQ=',
       transformation: 'AES/CBC/PKCS5Padding',
       ivOffset: '0',
       ivLen: '16',
       success: function(data) {
         console.log(`handling success:${data.text}`);
        },
       fail: function(data, code) {
         console.log(`### cipher.aes decrypt fail ### ${code}:${data}`);
       },
       complete: function() {
         console.log(`operation complete!`);
        }
     });
  }
}
```