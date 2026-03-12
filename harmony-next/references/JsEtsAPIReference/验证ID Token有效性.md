# 验证ID Token有效性

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](公共说明.md#section1329115361128)。

#### 功能介绍

应用服务端向华为账号服务器，调用该接口验证ID Token的有效性，并解析ID Token中的信息，只用于调试目的。

#### 场景描述

- 第三方应用通过ID Token方式进行华为账号登录授权，要解析出用户的ID Token，需要先对ID Token的有效性进行验证，如果本地验证失败，可调用此接口向华为服务器发送验证请求进行调试，验证ID Token的有效性。
- 如果ID Token是直接调用[获取用户级凭证](获取用户级凭证.md)的接口获取的，则不需要验证ID Token的有效性。

#### 使用约束

- 需确保调用端网络正常。
- 由于调用此接口耗时，并且易受网络状况的影响，所以该接口只能用于调试目的。在商用环境需采用本地验证的方式，详见[解析与验证](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-12#section6924154019588)。

#### 接口原型

**承载协议**

HTTPS POST

**接口方向**

开发者服务器->华为账号服务器

**接口URL**

https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo

数据格式

请求消息：Content-Type: application/x-www-form-urlencoded

响应消息：Content-Type: application/json

#### 请求参数

#### Request Header

参数

是否必选

参数类型

描述

Content-Type

是

String

取值为：application/x-www-form-urlencoded。

 说明：

Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](#section1635104211466)。

#### Request Body

**参数**

是否必选

**参数类型**

描述

id_token

是

String

应用获取到的ID Token。

#### 请求示例

请通过POST方式调用，示例如下：

```ets
POST /oauth2/v3/tokeninfo HTTP/1.1
Host:oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

id_token=*<id_token>*
```

#### 响应参数

#### Response Header

参数

是否必选

参数类型

描述

Content-Type

是

String

取值为：application/json。

#### Response Body

调用成功时，响应消息体返回如下：

参数

是否必选

参数类型

描述

typ

是

String

ID Token的格式，固定“JWT”。

alg

是

String

ID Token的签名算法。

- PS256
- RS256

kid

是

String

验证签名所用公私密钥对的id，长度最大256。

调用失败时，响应消息体返回如下：

参数

参数类型

描述

error

int

业务响应主错误码，详见[错误码](#section1186915200438)。

sub_error

int

业务响应子错误码，详见[错误码](#section1186915200438)。

error_description

String

错误描述信息。

#### ID Token字段解析

其中部分字段与生成id_token的scope有关，如下为各scope对应字段说明：

scope包含权限项openid时，解析的字段映射表如下：

参数

是否必选

参数类型

描述

iss

是

String

固定值：https://accounts.huawei.com。

sub

是

String

用户的UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

aud

是

String

接收ID Token的Client ID。

exp

是

Long

ID Token的过期时间戳(10位)。

iat

是

Long

ID Token的生成时间戳(10位)。

at_hash

是

String

Access Token的哈希值。

azp

是

String

生成ID Token的Client ID。

openid

是

String

用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

nonce

否

String

防重放攻击随机值。详情请参考[LoginWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#section42261825935)或[AuthorizationWithHuaweiIDRequest](authentication (华为账号应用统一认证服务).md#section12940173017165)的nonce字段说明。

scope包含权限项profile时，解析的字段映射表如下：

**参数**

是否必选

参数类型

描述

picture

否

String

用户头像图片链接。

display_name

否

String

华为账号对应的昵称，没有昵称则取匿名化的邮箱或手机号。

nickname

否

String

华为账号对应的昵称。

scope包含权限项quickLoginAnonymousPhone时，解析的字段映射表如下：

**参数**

是否必选

参数类型

描述

anonymized_login_mobile_number

否

String

匿名化的华为账号绑定手机号码，详见[华为账号一键登录（获取手机号和UnionID/OpenID）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login)。

scope包含权限项email时，解析的字段映射表如下：

参数

是否必选

参数类型

描述

email_verified

否

Boolean

用户邮箱是否已验证。

- true：是
- false：否

由于Email不是华为账号的必填项，响应中可能没有这个属性。

email

否

String

用户邮箱地址，由于Email不是华为账号的必填项，响应中可能没有这个属性。

#### 响应示例

#### 请求成功时

```ets
HTTP/1.1 200 OK
Content-Type: application/json

{
	"at_hash": "Dx5WUwU*****L-SKuAvWUg",
	"sub": "AQAxrB1HNA*****n-IfWRSUVq2M7xU",
	"kid": "6a2880c5d6a88c*****88eb680e05197d5bebd*****7b71757fc1b9530809ca",
	"iss": "https://accounts.huawei.com",
	"typ": "JWT",
	"display_name": "Jack",
	"nickname": "Jack",
	"aud": "30*****33",
	"azp": "30*****33",
	"exp": 1563823909,
	"iat": 1563820309,
	"alg": "PS256",
	"nonce": "default",
	"openid": "AQAxrBzThFv*****lv9tV_4rMCc"
}
```

#### 请求失败时

```ets
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
	"sub_error": 14004,
	"error_description": "jwk not found error",
	"error": 1400
}
```

#### 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](公共说明.md#section444143185314)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```ets
import com.alibaba.fastjson2.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.message.BasicNameValuePair;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * 验证ID Token有效性
 */
@Slf4j
public class IDTokenAPIDemo {
    public static void main(String[] args) throws IOException {
        // 验证ID Token有效性的接口URL
        String url = "https://oauth-login.cloud.huawei.com/oauth2/v3/tokeninfo";
        // 替换为您获取到的ID Token
        String idToken = "*<ID Token>*";
        JSONObject result = getDetailByIDToken(url, idToken);
        // 解析获取kid
        String kid = result.getString("kid");
        // 解析获取typ
        String typ = result.getString("typ");
        // 解析获取alg
        String alg = result.getString("alg");
        // 解析获取iss
        String iss = result.getString("iss");
        // 解析获取sub
        String sub = result.getString("sub");
        // 解析获取aud
        String aud = result.getString("aud");
        // 解析获取exp
        Long exp = result.getLong("exp");
        // 解析获取iat
        Long iat = result.getLong("iat");
        // 解析获取at_hash
        String atHash = result.getString("at_hash");
        // 解析获取azp
        String azp = result.getString("azp");
        // 解析获取openid
        String openid = result.getString("openid");
        // 解析获取nonce
        String nonce = result.getString("nonce");
    }

    private static JSONObject getDetailByIDToken(String url, String idToken) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("id_token", idToken));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        return CallUtils.toJsonObject(CallUtils.remoteCallOAuth(httpPost));
    }
}
```

#### 错误码

HTTP响应码

描述

解决方法

200

成功。

-

400

参数错误。

请根据**业务响应主错误码**以及**业务响应子错误码**进一步排查问题。

403

无权限访问。

通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

404

找不到服务。

请检查请求URI是否正确。

405

不支持的http请求method。

请检查http请求method是否与接口说明一致。

500

服务内部错误。

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

502

请求连接异常，常见于网络状况不稳定。

建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

503

系统流控。

触发系统流控，请稍后重试。

504

请求连接超时，常见于网络状况不稳定。

建议稍后重试，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

590

服务内部错误。

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

业务响应主错误码

业务响应子错误码

描述

解决方法

1203

100305

id_token的header解析失败。

id_token格式错误或者伪造的id_token。

- 检查id_token值是否JWT格式。
- 检查是否为华为账号返回的原始值。

100306

id_token的payload解析失败。

id_token格式错误或者伪造的id_token。

- 检查id_token值是否JWT格式。
- 检查是否为华为账号返回的原始值。

150021

id_token解析失败。

id_token格式错误或者伪造的id_token。

- 检查id_token值是否JWT格式。
- 检查是否为华为账号返回的原始值。

150023

id_token的signature解析失败。

id_token格式错误或者伪造的id_token。

- 检查id_token值是否JWT格式。
- 检查是否为华为账号返回的原始值。

500

系统内部错误。

系统内部处理错误，建议业务打印错误码信息，并请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

1400

14004

无法通过其kid找到对应的JWT公钥相关信息。

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

1500

15003

无效的id_token。

id_token格式错误或者伪造的id_token。

- 检查id_token值是否JWT格式。
- 检查是否为华为账号返回的原始值。

15004

id_token验证失败。

检查验证时使用的公钥、算法是否正确。

15005

id_token的issuer验证失败。

请排查id_token是否被篡改。

15006

id_token已过期。

请重新获取新的id_token。

15007

id_token为空。

请按照接口参数的要求，传入正确的id_token参数。

15008

id_token格式不正确。

检查id_token的格式是否满足正则：^[0-9a-zA-Z_\-\.]+$。