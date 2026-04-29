# 通过OpenID或UnionID获取GroupUnionID

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](公共说明.md#ZH-CN_TOPIC_0000002553202251__tls协议及加密套件)。

#### 功能介绍

应用服务端调用华为账号服务的接口，通过用户的OpenID或UnionID获取GroupUnionID信息。

#### 场景描述

不同开发者的应用可通过GroupUnionID关联用户数据，实现数据互通。如果需要实现数据互通的不同开发者应用已具备用户OpenID或UnionID，可以通过该接口批量将用户OpenID或UnionID转换为GroupUnionID。

#### 使用约束

-

- 需确保调用端网络正常。

-

- 仅对企业开发者开放。

-

- 开发者账号必须加入关联主体账号组。具体可通过[创建账号组](https://developer.huawei.com/consumer/cn/doc/start/cag-0000001265390541)创建关联主体账号组，然后在关联主体账号组中[添加账号组成员](https://developer.huawei.com/consumer/cn/doc/start/aai-0000001265430513)。

-

- 仅能获取当前应用的用户OpenID、UnionID对应的GroupUnionID。

#### 接口原型

-

承载协议： HTTPS POST

-

接口方向： 开发者服务器->华为账号服务器

-

接口URL： https://account-api.cloud.huawei.com/oauth2/v6/groupUnionId/batchGet

-

数据格式：

请求消息：Content-Type: application/json;charset=utf-8

响应消息：Content-Type: application/json;charset=utf-8

#### 请求参数

#### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=utf-8。 说明： Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考示例代码。 |
| Authorization | 是 | String | 接口的访问凭证，通过[获取应用级凭证](获取应用级凭证.md)获取的Access Token。 传参格式：Bearer ${Access Token} 样例：Bearer DgEEn******Y+Aj== |

#### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| openIdList | 否 | List<String> | 用户的OpenID列表，每次请求最大支持传100个OpenID。 请求参数unionIdList为空时，此参数必填。 请求参数unionIdList不为空时，此参数不允许填写。 |
| unionIdList | 否 | List<String> | 用户的UnionID列表，每次请求最大支持传100个UnionID。 当请求参数openIdList为空时，此参数必填。 当请求参数openIdList不为空时，此参数不允许填写。 |

#### 请求示例

请通过POST方式调用，示例如下：

```ets
POST /oauth2/v6/groupUnionId/batchGet HTTP/1.1
Host: account-api.cloud.huawei.com
Content-Type: application/json; charset=utf-8
Authorization：Bearer <access_token>

{
  "openIdList": ["<open_id1>","<open_id2>"]
}
```

#### 响应参数

#### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json; charset=utf-8。 |

#### Response Body

调用成功时，响应消息体返回如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| openIdToGroupUnionIdList | 否 | List<OpenIdToGroupUnionIdInfo> | 用户的OpenID转GroupUnionID的列表。当传入openIdList参数时返回。 |
| unionIdToGroupUnionIdList | 否 | List<UnionIdToGroupUnionIdInfo> | 用户的UnionID转GroupUnionID的列表，当传入unionIdList参数时返回。 |


响应参数openIdToGroupUnionIdList和unionIdToGroupUnionIdList列表为去重后的结果，因此响应参数的openIdToGroupUnionIdList数量可能与请求参数的openIdList数量不一致；请求参数unionIdList与响应参数unionIdToGroupUnionIdList同理。

调用失败时，响应消息体返回如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| resultCode | 是 | int | 错误码，详见错误码。 |
| resultDesc | 是 | String | 错误描述信息。 |

#### OpenIdToGroupUnionIdInfo

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| openId | 是 | String | 用户的OpenID，具体格式要求请参考OpenID和UnionID的格式说明。 |
| groupUnionId | 是 | String | GroupUnionID是用户在关联主体账号组内的统一身份标识，使用场景详见不同开发者的应用之间如何实现用户数据互通。 |

#### UnionIdToGroupUnionIdInfo

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| unionId | 是 | String | 用户的UnionID，具体格式要求请参考OpenID和UnionID的格式说明。 |
| groupUnionId | 是 | String | GroupUnionID是用户在关联主体账号组内的统一身份标识，使用场景详见不同开发者的应用之间如何实现用户数据互通。 |

#### 响应示例

#### 请求成功时（入参为openIdList场景）

```ets
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
  "openIdToGroupUnionIdList": [
     { "openId": "AQAxrBzThFv*****lv9tV_4rMCc", "groupUnionId": "AgAsmsA25yiLl*****8Gr-uQyoKU8rSfMEwFJiqOA" },
     { "openId": "AQAxsA2hHN*****lv9U8rSfq2MX", "groupUnionId": "AgAsmWRSUVq2MLl*****8Gr-uQyoKUAxrB1HNqOA" }
  ]
}
```

#### 请求成功时（入参为unionIdList场景）

```ets
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
  "unionIdToGroupUnionIdList": [
     { "unionId": "AAAsbgKRbd*****isROb9mDshln5U", "groupUnionId": "AgAsmsA25yiLl*****8Gr-uQyoKU8rSfMEwFJiqOA" },
     { "unionId": "AAAsbgK2ir*****Gsr-BOmDshln5U", "groupUnionId": "AgAsmWRSUVq2MLl*****8Gr-uQyoKUAxrB1HNqOA" }
  ]
}
```

#### 请求失败时

```ets
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
  "resultCode": 60010003,
  "resultDesc": "Authorization error."
}
```

#### 示例代码

Java示例代码如下，运行前需要进行[示例代码环境配置](公共说明.md#ZH-CN_TOPIC_0000002553202251__示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

```ets
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.apache.http.client.methods.HttpPost;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 通过OpenID或UnionID获取GroupUnionID
 */
@Slf4j
public class GroupUnionIdBatchGetDemo {
    public static void main(String[] args) throws IOException {
        // 通过OpenID或UnionID获取GroupUnionID接口URL
        String url = "https://account-api.cloud.huawei.com/oauth2/v6/groupUnionId/batchGet";
        // 替换为实际获取到的应用级凭证
        String accessToken = "<Access Token>";

        // 通过OpenID或UnionID都可以获取到GroupUnionID，请根据已有的业务场景进行选择
        // 场景一：使用OpenID来获取GroupUnionID场景
        List<String> openIdList = Arrays.asList("<OpenID1>","<OpenID2>");
        JSONObject resultByOpenId = batchGetGroupUnionIdByOpenId(url, accessToken, openIdList);
        // 解析响应结果获取openIdToGroupUnionIdList
        JSONArray openIdToGroupUnionIdList = resultByOpenId.getJSONArray("openIdToGroupUnionIdList");
        // 遍历解析openIdToGroupUnionIdList，openIdToGroupUnionIdList的每个元素，都是一组OpenID和GroupUnionID
        for (Object openIdToGroupUnionId : openIdToGroupUnionIdList) {
            JSONObject openIdToGroupUnionIdJson = (JSONObject) openIdToGroupUnionId;
            // 解析获取openId
            String openId = openIdToGroupUnionIdJson.getString("openId");
            // 解析获取groupUnionId
            String groupUnionId = openIdToGroupUnionIdJson.getString("groupUnionId");
        }

        // 场景二：使用UnionID来获取GroupUnionID场景
        List<String> unionIdList = Arrays.asList("<UnionID1>", "<UnionID2>");
        JSONObject resultByUnionId = batchGetGroupUnionIdByUnionId(url, accessToken, unionIdList);
        // 解析响应结果获取unionIdToGroupUnionIdList
        JSONArray unionIdToGroupUnionIdList = resultByUnionId.getJSONArray("unionIdToGroupUnionIdList");
        // 遍历解析unionIdToGroupUnionIdList，unionIdToGroupUnionIdList的每个元素，都是一组UnionID和GroupUnionID
        for (Object unionIdToGroupUnionId : unionIdToGroupUnionIdList) {
            JSONObject unionIdToGroupUnionIdJson = (JSONObject) unionIdToGroupUnionId;
            // 解析获取unionId
            String unionId = unionIdToGroupUnionIdJson.getString("unionId");
            // 解析获取groupUnionId
            String groupUnionId = unionIdToGroupUnionIdJson.getString("groupUnionId");
    }

    /**
     * 通过UnionID获取GroupUnionID
     * @param url 通过OpenID或UnionID获取GroupUnionID接口URL
     * @param accessToken 应用级凭证
     * @param unionIdList UnionID列表
     * @return JSONObject响应结果
     * @throws IOException 接口调用异常
     */
    private static JSONObject batchGetGroupUnionIdByUnionId(
            String url, String accessToken, List<String> unionIdList) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        Map<String, Object> reqBody = new HashMap<>();
        reqBody.put("unionIdList", unionIdList);
        httpPost.setEntity(CallUtils.wrapJsonEntity(reqBody));
        httpPost.setHeader("Content-Type", "application/json;charset=utf-8");
        httpPost.setHeader("Authorization", "Bearer " + accessToken);
        // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
        return CallUtils.toJsonObject(CallUtils.remoteCallAccountApi(httpPost));
    }

    /**
     * 通过OpenID获取GroupUnionID
     * @param url 通过OpenID或UnionID获取GroupUnionID接口URL
     * @param accessToken 应用级凭证
     * @param openIdList OpenID列表
     * @return JSONObject响应结果
     * @throws IOException 接口调用异常
     */
    private static JSONObject batchGetGroupUnionIdByOpenId(
            String url, String accessToken, List<String> openIdList) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        Map<String, Object> reqBody = new HashMap<>();
        reqBody.put("openIdList", openIdList);
        httpPost.setEntity(CallUtils.wrapJsonEntity(reqBody));
        httpPost.setHeader("Content-Type", "application/json;charset=utf-8");
        httpPost.setHeader("Authorization", "Bearer " + accessToken);
        // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
        return CallUtils.toJsonObject(CallUtils.remoteCallAccountApi(httpPost));
    }
```

#### 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功，实际业务处理结果需要通过Response Body中的resultCode（错误码） 进行判断。 | - |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过在线提单提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过在线提单提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过在线提单提交问题。 |
| 503 | 系统流控。 | 触发系统流控，请稍后重试。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过在线提单提交问题。 |
| 590 | 服务内部错误。 | 请通过在线提单提交问题。 |

| 错误码 | 描述 | 解决方法 |
| --- | --- | --- |
| 60010002 | 参数错误。 | 请按照响应描述中的提示，检查并修改请求参数。 |
| 60010003 | 鉴权头Authorization校验不通过。 | 检查并修改请求参数中Authorization参数。 |
| 60170001 | 开发者账号未加入关联主体账号组。 | 可通过创建账号组创建关联主体账号组，然后在关联主体账号组中添加账号组成员。 |
| 60010001 | 系统内部错误。 | 可重试，若仍无法解决，请通过在线提单提交问题。 |