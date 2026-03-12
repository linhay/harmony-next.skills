# 通过OpenID获取UnionID

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](公共说明.md#section1329115361128)。

#### 功能介绍

应用服务端向华为账号服务器调用该接口，通过用户的OpenID获取UnionID信息。

#### 场景描述

在开发HarmonyOS应用时，您需要考虑同一用户在非HarmonyOS应用和HarmonyOS应用的用户数据是否互通。如果您之前使用OpenID来关联用户数据，我们建议将用户数据关系切换成UnionID，以确保用户使用HarmonyOS应用后可以继承老版本的用户数据。

#### 使用约束

- 需确保调用端网络正常。
- 仅能获取自身应用的用户OpenID对应的UnionID。

#### 接口原型

**承载协议**

HTTPS POST

**接口方向**

开发者服务器->华为账号服务器

**接口URL**

https://oauth-login.cloud.huawei.com/rest.php?nsp_svc=huawei.oauth2.app.openIdToUnionId

**数据格式**

请求消息：Content-Type: application/x-www-form-urlencoded

响应消息：Content-Type: text/plain;charset=utf-8

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

Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](#section15783195817216)。

#### Request Body

参数

是否必选

参数类型

描述

access_token

是

String

通过[获取应用级凭证](获取应用级凭证.md)获取的Access Token。

open_id

是

String

用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

#### 请求示例

请通过POST方式调用，示例如下：

```ets
POST /rest.php?nsp_svc=huawei.oauth2.app.openIdToUnionId HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

open_id=*<open_id>*&access_token=*<access_token>*
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

取值为：text/plain;charset=utf-8。

#### Response Body

调用成功时，响应消息体返回如下：

**参数**

是否必选

参数类型

描述

union_id

是

String

用户的UnionID，由用户账号和应用开发者账号签名而成。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)。

调用失败时，响应消息体返回如下：

参数

参数位置

参数类型

描述

NSP_STATUS

header

String

错误码，详见本章节[错误码](#section1737691991515)。

error

body

String

错误描述信息。

#### 响应示例

#### 请求成功时

```ets
HTTP/1.1 200 OK
Content-Type: text/plain;charset=utf-8

{"union_id":"AQAxrB1HNA*****n-IfWRSUVq2M7xU"}
```

#### 请求失败时

```ets
HTTP/1.1 200 OK
Content-Type: text/plain;charset=utf-8
**NSP_STATUS: 102**

{
    "error": "invalid session"
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
 * 通过OpenID获取UnionID
 */
@Slf4j
public class OpenIdToUnionIdDemo {
    public static void main(String[] args) throws IOException {
        // 通过OpenID获取UnionID的接口URL
        String url = "https://oauth-login.cloud.huawei.com/rest.php?nsp_svc=huawei.oauth2.app.openIdToUnionId";
        // 替换为您实际获取到的应用级凭证Access Token
        String accessToken = "*<Access Token>*";
        // 替换为您获取到的OpenID
        String openId = "*<OpenID>*";
        JSONObject result = openIdToUnionId(url, accessToken, openId);
        // 解析获取union_id
        String unionId = result.getString("union_id");
    }

    private static JSONObject openIdToUnionId(String url, String accessToken, String openId) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("access_token", accessToken));
        request.add(new BasicNameValuePair("open_id", openId));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // 使用默认异常处理逻辑，自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
        return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
    }
}
```

#### 错误码

HTTP响应码

描述

解决方法

200

仅表示本次接口调用成功，实际业务处理结果需要通过**Response Header**中的**NSP_STATUS**进行判断。

-

400

参数错误。

请根据文档排查请求参数是否符合规范。

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

Response Header中的NSP_STATUS字段，在处理成功时不会返回。

NSP_STATUS

描述

解决方法

6

access_token过期。

请重新获取新的access_token。

102

无效的access_token。

access_token参数无效，可能原因：请求头的Content-Type为application/x-www-form-urlencoded，但实际代码调用时，未对请求body参数进行URLEncode处理，可参考[示例代码](#section15783195817216)组装参数。

500

接口内部错误。

根据返回的错误描述进行处理，若仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

501

服务分发异常。

- 检查请求URL中nsp_svc是否正确
- 若确认请求URL与文档一致，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

1302

接口流控。

业务调用频率过高，单应用调用并发请低于100TPS。

31204

access_token失效。

请重新获取新的access_token。

150028

open_id参数为空或超长。

请检查open_id是否为空或者超过256的字符长度。具体格式要求请参考[OpenID和UnionID的格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9)