# 转换ID

#### 功能介绍

调用该接口，传入Access Token、appId、gamePlayerId到华为服务器上获取HarmonyOS系统下玩家的playerId、openId、unionId明细信息。

#### 场景描述

通过Access Token、appId、gamePlayerId信息到华为服务器上查询HarmonyOS系统下玩家的playerId、openId、unionId明细信息。

#### 接口原型

承载协议

HTTPS POST

接口方向

开发者服务器->华为游戏服务器

接口URL

https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi

 说明：

请使用TLS 1.2协议或以上版本。

数据格式

请求：Content-Type: application/x-www-form-urlencoded（表单方式）

响应：Content-Type: application/json

#### 请求参数

参数

是否必选

类型

描述

method

是

String

固定传入“external.hms.gs.player.transfer.convertId”。

accessToken

是

String

游戏调用华为账号的[获取用户级凭证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-user-token)接口获取到的Access Token。

appId

是

String

HarmonyOS 5.0及以上游戏的APP ID，获取方法请参见[查看应用信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-view-app-info-0000002282674569)。

gamePlayerId

是

String

HarmonyOS 5.0及以上游戏的玩家标识，通过调用[unionLogin](gamePlayer（基础游戏服务）.md#section157848375136)接口返回。

#### 请求示例

```ets
POST /gameservice/api/gbClientApi HTTP/1.1
Content-Type: application/x-www-form-urlencoded
User-Agent: PostmanRuntime/7.24.0
Accept: */*
Host: jos-open-api.cloud.huawei.com
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 717
// **所有请求参数****值**均需要urlencode编码后再进行拼接
method=external.hms.gs.player.transfer.convertId&accessToken=******&appId=xxxxxxx&gamePlayerId=xxxxxxx
```

#### 响应参数

参数

是否必选

类型

描述

rtnCode

是

int

服务端结果说明。

- 0：获取成功
- -1：获取失败
- 2：accessToken无效
- 3001：参数错误
- 3101：应用ID与鉴权应用不一致

playerId

是

String

HarmonyOS系统下，华为游戏服务器给华为账号封装处理后的对外开放的游戏玩家标识。

openId

是

String

HarmonyOS系统下，由华为账号和应用唯一标识组合加密起来的玩家标识。

unionId

否

String

HarmonyOS系统下，由华为账号和开发者账号组合加密起来的玩家标识。

errMsg

否

String

异常场景下返回错误码的描述。

#### 响应示例

```ets
HTTP/1.1 200 OK
Date: Tue, 19 May 2023 06:28:02 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Content-Encoding: gzip
Server: elb
{
    "playerId": "13423***9864303",
    "openId": "43JIOdok743***980sd9453",
    "unionId": "MDFiaNicx***JHIicHAlnRD",
    "rtnCode": 0
}
```

#### 调用示例

```ets
“Java”
package okhttp.com.post;
import com.alibaba.fastjson.JSONObject;
import okhttp3.*;
import java.io.IOException;

public class ConvertIdTest {
    private static Integer RETURN_CODE_SUCCEED = 0;

    /**
     * 接口本地调测时使用
     */
    public static void main(String[] args) {
        String method = "external.hms.gs.player.transfer.convertId"; // 固定传入
        String accessToken = "xxxxx"; // 请使用游戏客户端调用账号获取到的Access Token
        String appId = "xxxx"; // HarmonyOS 5.0及以上游戏的APP ID
        String gamePlayerId = "xxxxx"; // 通过Access Token到华为服务器上获取到的玩家的gamePlayerId
        convertIdService(method, accessToken,appId, gamePlayerId);
    }

    private static void convertIdService(String method, String accessToken, String appId, String gamePlayerId) {
        OkHttpClient client = new OkHttpClient().newBuilder().build();
        RequestBody mFormBody = new FormBody.Builder().add("method", method)
            .add("accessToken", accessToken)
            .add("appId", appId)
            .add("gamePlayerId", gamePlayerId)
            .build();
        Request request = new Request.Builder().url("https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi")
            .post(mFormBody)
            .build();
        try {
            Response response = client.newCall(request).execute();
            if (response.isSuccessful()) {
                JSONObject object = JSONObject.parseObject(response.body().string());
                if (RETURN_CODE_SUCCEED.equals(object.get("rtnCode"))) {
                    System.out.println("playerId: " + object.get("playerId"));
                    System.out.println("openId: " + object.get("openId"));
                    System.out.println("unionId: " + object.get("unionId"));
                } else {
                    System.out.println("rtnCode: " + object.get("rtnCode"));
                    System.out.println("rtnMsg: " + object.get("errMsg"));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

```ets
“C#”
using System;
using System.IO;
using System.Net;
using System.Text;
using System.Web;
namespace cXdemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // 固定传入“external.hms.gs.player.transfer.convertId”
            string method = "external.hms.gs.player.transfer.convertId";
            // 取自当前玩家的Player对象中获取到的Access Token
            string accessToken = "xxxxx";
	    // HarmonyOS 5.0及以上游戏的APP ID
	    string appId = "xxxx";
	    // 通过Access Token到华为服务器上获取到的玩家的gamePlayerId
	    string gamePlayerId = "xxxxx";
            // 请求接口
            requestgameInfo(method, accessToken, appId, gamePlayerId);
        }
        static void requestgameInfo(string method, string accessToken, string appId, string gamePlayerId)
        {
            var requestUrl = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi";
            HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;
            request.Method = "post";
            request.ContentType = "application/x-www-form-urlencoded";
            StringBuilder data = new StringBuilder();
            data.Append("method=" + HttpUtility.UrlEncode(method));
            data.Append("&accessToken=" + HttpUtility.UrlEncode(accessToken));
			data.Append("&appId=" + HttpUtility.UrlEncode(appId));
			data.Append("&gamePlayerId=" + HttpUtility.UrlEncode(gamePlayerId));
            byte[] byteData = Encoding.UTF8.GetBytes(data.ToString());
            request.ContentLength = byteData.Length;
            Stream postStream = request.GetRequestStream();
            postStream.Write(byteData, 0, byteData.Length);
            postStream.Close();
            WebResponse response = request.GetResponse();
            StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
            string strJson = reader.ReadToEnd();
            Console.WriteLine(strJson);
            reader.Close();
            response.Close();
        }
    }
}
```

```ets
“PHP”
class convert_id
{
    /**
     * 根据AccessToken获取玩家信息
     *
     * @param string $method 固定传入“external.hms.gs.player.transfer.convertId”
     * @param string $accessToken 请使用客户端Player对象中的AccessToken
     * @param string $appId HarmonyOS 5.0及以上游戏的APP ID
     * @param string $gamePlayerId 通过Access Token到华为服务器上获取到的玩家的gamePlayerId
     */
    public function call_https(string $method, string $accessToken, string $appId, string $gamePlayerId): void
    {
        $data = array("method" => $method, "accessToken" => $accessToken, "appId" => $appId, "gamePlayerId" => $gamePlayerId);
        $curl = curl_init();
        curl_setopt_array($curl, array(
            CURLOPT_URL => 'https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_ENCODING => '',
            CURLOPT_MAXREDIRS => 10,
            CURLOPT_TIMEOUT => 0,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_CUSTOMREQUEST => 'POST',
            CURLOPT_SSL_VERIFYHOST => false,
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
            CURLOPT_POSTFIELDS => http_build_query($data),
            CURLOPT_HTTPHEADER => array(
                'Content-Type: application/x-www-form-urlencoded'
            ),
        ));
        $response = curl_exec($curl);
        if (curl_error($curl)) {
            throw new Exception(curl_error($curl));
        }
        curl_close($curl);
        $result = json_decode($response, true);
        var_dump($result);
    }
}
$convert_id = new convert_id();
$method = "external.hms.gs.player.transfer.convertId"; // 固定传入
$accessToken = "xxxxx"; // 请使用客户端Player对象中的AccessToken
$appId = "xxxxx"; // 游戏APP Id
$gamePlayerId = "xxxxx"; // 通过Access Token到华为服务器上获取到的玩家的gamePlayerId
$convert_id->call_https($method, $accessToken, $appId, $gamePlayerId);
```

```ets
“Python”
from typing import Any
import requests
import urllib.parse
class ConvertIdSolution:
    def convert_id(self, method, accessToken, appId, gamePlayerId):
        url = "https://jos-open-api.cloud.huawei.com/gameservice/api/gbClientApi"
        params: dict[str, Any] = {
            'method': method,
            'accessToken': accessToken,
            'appId': appId,
            'gamePlayerId': gamePlayerId
        }
        encodedParams = urllib.parse.urlencode(params)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, headers=headers, data=encodedParams)
        print(response.text)
if __name__ == "__main__":
    # 固定传入“external.hms.gs.player.transfer.convertId”
    input_method = 'external.hms.gs.player.transfer.convertId'
    # 请使用客户端Player对象中的AccessToken
    input_accessToken = 'xxx'
	# HarmonyOS 5.0及以上游戏的APP ID
    input_appId = 'xxx'
	# 通过Access Token到华为服务器上获取到的玩家的gamePlayerId
    input_gamePlayerId = 'xxx'
    function = ConvertIdSolution()
    function.convert_id(input_method, input_accessToken, input_appId, input_gamePlayerId)
```