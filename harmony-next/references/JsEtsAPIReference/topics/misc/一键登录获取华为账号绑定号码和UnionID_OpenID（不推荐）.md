# 一键登录获取华为账号绑定号码和UnionID/OpenID（不推荐）

为了更安全的网络访问，请务必使用TLS1.2协议及规定内的加密套件。若使用协议是TLS1.0、TLS1.1或规定外的加密套件，可能无法正常访问华为账号服务。

关于TLS1.2协议及规定内加密套件的信息，可以点击这里进行详细了解：[TLS协议及加密套件](公共说明.md#ZH-CN_TOPIC_0000002553202251__tls协议及加密套件)。


为优化开发者体验，Account Kit推荐使用[一键登录获取华为账号绑定号码和UnionID/OpenID](一键登录获取华为账号绑定号码和UnionID_OpenID.md)新接口进行应用服务端开发，可以减少[获取用户级凭证](获取用户级凭证.md)接口调用，接入更简单，整体时延更低。

#### 功能介绍

[华为账号一键登录（获取手机号和UnionID/OpenID）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login)场景，应用服务端向华为账号服务器调用该接口获取UnionID，OpenID，华为账号绑定的手机号码及其相关信息。该服务仅对中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户提供。

#### 场景描述

应用已经通过授权码（Authorization Code）获取到Access Token后，获取UnionID，OpenID，华为账号绑定的手机号码及其相关信息。

#### 使用约束

-

- 需确保调用端网络正常。

-

- 华为账号一键登录服务仅对中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户提供；且应用服务端获取华为账号绑定号码时，该服务器必须部署在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

-

应用使用华为账号一键登录功能之前，需要完成quickLoginMobilePhone（华为账号一键登录）的scope权限申请，详见[开发前提](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login#开发前提)。


应用未申请quickLoginMobilePhone（华为账号一键登录）的scope权限，或获取Authorization Code时不携带quickLoginMobilePhone（华为账号一键登录）scope，调用成功后响应中将不包含华为账号绑定号码。

#### 接口原型

-

承载协议：HTTPS POST

-

接口方向：开发者服务器->华为账号服务器

-

接口URL：https://account.cloud.huawei.com/rest.php?nsp_svc=GOpen.User.getInfo

-

数据格式：

请求消息：Content-Type: application/x-www-form-urlencoded

响应消息：Content-Type: application/json;charset=utf-8

#### 请求参数

#### Request Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/x-www-form-urlencoded。 说明： Request Body传参，请务必遵循此请求头格式，否则可能导致请求失败，具体传参方式可参考[示例代码](获取华为账号用户信息-获取头像昵称.md#section1888515151299)。 |

#### Request Body

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| access_token | 是 | String | 通过[获取用户级凭证](获取用户级凭证.md)获取的Access Token。获取凭证时Authorization Code需包含quickLoginMobilePhone scope的授权。 |

#### 请求示例

请通过POST方式调用，示例如下：

```ets
POST /rest.php?nsp_svc=GOpen.User.getInfo HTTP/1.1
Host: account.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

access_token=<Access Token>
```

#### 响应参数

#### Response Header

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| Content-Type | 是 | String | 取值为：application/json;charset=utf-8。 |

#### Response Body

调用成功时，响应消息返回如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| openID | 是 | String | 用户OpenID。具体格式要求请参考OpenID和UnionID的格式说明。 |
| unionID | 是 | String | 用户UnionID。具体格式要求请参考OpenID和UnionID的格式说明。 |
| loginMobileNumber | 否 | String | 华为账号绑定号码，使用该手机号完成一键登录的功能，详见华为账号一键登录（获取手机号和UnionID/OpenID）。 以下场景loginMobileNumber不返回: - 用户未绑定手机号 - 应用未申请quickLoginMobilePhone的scope权限 - 获取Authorization Code时不携带quickLoginMobilePhone scope - 应用服务器部署在中国境外、香港特别行政区、澳门特别行政区或中国台湾 |
| loginMobileValid | 否 | int | 通过一键登录功能获取的华为账号绑定号码的实时有效性。 当不返回 loginMobileNumber时，也不进行返回。 若发起一键登录时LoginPanelParams的verifyPhoneNumber参数值传递为true，表示华为代为验证手机号有效性，开发者无需关注此返回值； 若verifyPhoneNumber参数值传递为false, 需要根据返回的状态值进行处理。 0：在过去90天内，无法证明当前手机号码可以触达用户， 需要进行验证 1：在过去90天内，当前手机号码被证明可以触达用户，可以直接使用 |
| purePhoneNumber | 否 | String | 不带国家码的手机号，此处为loginMobileNumber去除国际冠码与国际电话区号的形式。 当不返回 loginMobileNumber时，也不进行返回。 |
| phoneCountryCode | 否 | String | purePhoneNumber的国际冠码(00)+国际电话区号。 当不返回 loginMobileNumber时，也不进行返回。 |
| warning | 否 | String | 应用服务器部署在中国境外、香港特别行政区、澳门特别行政区或中国台湾时, 不返回华为账号绑定的手机号码，而返回此字段进行提示说明。 |


如字段无特殊说明，华为账号服务器返回的手机号码格式如下：

-

- 当账号注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）且绑定手机号为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）手机号码时，省略国际冠码与国际电话区号，直接返回手机号码，如: 11136000008。

-

- 其它情况则遵循格式：国际冠码(统一使用00) + 国际电话区号 + 手机号码，如：0085261234567 (香港特别行政区)、 0079871234560 (俄罗斯)。

调用失败时，响应消息返回如下：

| 参数 | 参数位置 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| NSP_STATUS | header | String | 错误码，详见本章节错误码。 |
| error | body | String | 错误描述信息。 |

#### 响应示例

#### 请求成功时

```ets
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "openID": "MDFAMTAxMDA1MTg1QGFlMzM0OWIyOGY0*****MDRiaNTI5ODAxYTA3MDh*****A4ZTZmNTA2ZTE4ZT*****lmNGVmN2E1ZjY1OTg4NWRiaN2QxMzQy*****TU0YWQ3",
    "unionID": "MDF9pBd6xxxxA8iaG4ZNPTw*****3fyXzG9WgUcmY8XibBvQ",
    // 华为账号绑定号码，使用该手机号完成一键登录的功能(返回数据实际为明文)
    "loginMobileNumber": "191******08",
    // 通过一键登录功能获取的华为账号绑定号码的实时有效性, 0表示需要进一步验证有效性， 1表示可以直接使用
    "loginMobileValid": 1,
    // 不带国际冠码与国际电话区号的手机号码(返回数据实际为明文)
    "purePhoneNumber": "191******08",
    "phoneCountryCode": "0086"
}
```

#### 请求失败时

```ets
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8
NSP_STATUS: 6

{
    "error": "session timeout"
}
```

#### 从中国境外、香港特别行政区、澳门特别行政区或中国台湾服务器请求时

```ets
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "openID": "MDFAMTAxMDA1MTg1QGFlMzM0OWIyOGY0*****MDRiaNTI5ODAxYTA3MDh*****A4ZTZmNTA2ZTE4ZT*****lmNGVmN2E1ZjY1OTg4NWRiaN2QxMzQy*****TU0YWQ3",
    "warning": "xxx site doesn't support quick login, see the guide for details"
}
```

#### [示例代码](获取华为账号用户信息-获取头像昵称.md#section1888515151299)

Java示例代码如下，运行前需要进行[示例代码环境配置](公共说明.md#ZH-CN_TOPIC_0000002553202251__示例代码环境配置)（请将此示例代码与工具类CallUtils放于同一路径下，如不在同一路径，请手动添加import）

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
 * 一键登录获取华为账号绑定号码和UnionID/OpenID
 */
@Slf4j
public class GetMobileByQuickLoginDemo {
    public static void main(String[] args) throws IOException {
        // 一键登录获取华为账号绑定号码和UnionID/OpenID的接口URL
        String url = "https://account.cloud.huawei.com/rest.php?nsp_svc=GOpen.User.getInfo";
        // 替换为实际获取到的用户级凭证Access Token
        String accessToken = "<Access Token>";
        JSONObject result = getQuickLoginMobile(url, accessToken);
        // 解析获取openID
        String openID = result.getString("openID");
        // 解析获取unionID
        String unionID = result.getString("unionID");
        // 解析获取loginMobileNumber
        String loginMobileNumber = result.getString("loginMobileNumber");
        // 解析获取loginMobileValid
        Integer loginMobileValid = result.getInteger("loginMobileValid");
        // 解析获取purePhoneNumber
        String purePhoneNumber = result.getString("purePhoneNumber");
        // 解析获取phoneCountryCode
        String phoneCountryCode = result.getString("phoneCountryCode");
        // 解析获取warning
        String warning = result.getString("warning");
    }

    private static JSONObject getQuickLoginMobile(String url, String accessToken) throws IOException {
        HttpPost httpPost = new HttpPost(url);
        List<NameValuePair> request = new ArrayList<>();
        request.add(new BasicNameValuePair("access_token", accessToken));
        httpPost.setHeader("Content-Type", "application/x-www-form-urlencoded");
        httpPost.setEntity(new UrlEncodedFormEntity(request));
        // 如需要自定义异常处理请使用api CallUtils#remoteCall(HttpUriRequest, BiFunction<CloseableHttpResponse,String,E>)
        return CallUtils.toJsonObject(CallUtils.remoteCall(httpPost));
    }
```

#### 错误码

| HTTP响应码 | 描述 | 解决方法 |
| --- | --- | --- |
| 200 | 仅表示本次接口调用成功（接口调用成功不等于业务处理成功，如Response Header中返回了NSP_STATUS字段，说明业务处理报错，需要判断报错原因）。 | - |
| 400 | 参数错误。 | 请根据文档排查请求参数是否符合规范。 |
| 403 | 无权限访问。 | 通常是调用方网络安全策略阻止了访问，请检查网络环境配置。若仍无法解决，请通过在线提单提交问题。 |
| 404 | 找不到服务。 | 请检查请求URI是否正确。 |
| 405 | 不支持的http请求method。 | 请检查http请求method是否与接口说明一致。 |
| 500 | 服务内部错误。 | 请通过在线提单提交问题。 |
| 502 | 请求连接异常，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过在线提单提交问题。 |
| 504 | 请求连接超时，常见于网络状况不稳定。 | 建议稍后重试，若仍无法解决，请通过在线提单提交问题。 |
| 590 | 服务内部错误。 | 请通过在线提单提交问题。 |


Response Header中的NSP_STATUS字段，在处理成功时不会返回。

| NSP_STATUS | 描述 | 解决方法 |
| --- | --- | --- |
| 6 | 会话失效，session timeout。 可能原因: - access_token无效或已过期 - access_token格式不正确 - 其他内部原因 | - 请检查传参是否正确，如无问题请尝试重新获取。 - 未对access_token进行URLEncode处理，可参考[示例代码](获取华为账号用户信息-获取头像昵称.md#section1888515151299)组装参数。 - 根据返回的错误描述进行处理，若仍无法解决，请通过在线提单提交问题。 |
| 403 | 访问无权限。 | 请前往AppGallery Connect（简称AGC）为应用申请开放权限，详见申请账号权限。 |
| 500 | 接口内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过在线提单提交问题。 |
| 503 | 触发系统流控。 | 请稍后重试。 |
| 70001402 | 系统鉴权错误。 | 鉴权系统异常，若重试无法解决，请通过在线提单提交问题。 |
| 70020002 | 内部网络错误。 | 内部网络错误，若重试无法解决，请通过在线提单提交问题。 |
| 70001401 | 系统内部错误。 | 根据返回的错误描述进行处理，若仍无法解决，请通过在线提单提交问题。 |