# 批量转换teamPlayerId

#### 功能介绍

华为开发者联盟上的游戏从一个账号转移到另一个账号进行维护，该游戏资产归属于转入方。

转出方/转入方可以调用此接口，向华为服务器批量提交转让前游戏关联的玩家标识teamPlayerId等信息，批量获取游戏转让后对应的teamPlayerId等信息。

#### 接口约束

- 调用此接口前，请确保转出方/转入方已完成[游戏转移](https://developer.huawei.com/consumer/cn/doc/app/game-center-transferring-0000001194325290)，否则均将无权转换teamPlayerId。
- 单次接口请求最多可以获取1000条teamPlayerId数据。
- 请勿频繁调用此接口，调用的时间间隔请控制在3秒以上。

#### 接口原型

承载协议

HTTPS POST

接口方向

开发者服务器 -> 华为服务器

接口URL

中国站点：https://connect-api.cloud.huawei.com/api/jas/open/players/player-accounts/team-player/convert

 注意：

调用[获取Token](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-References/agcapi-obtain_token-0000001158365043)接口时使用的域名需与本接口域名保持一致，例如本接口使用“connect-api.cloud.huawei.com”，则调用[获取Token](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-References/agcapi-obtain_token-0000001158365043)接口需使用“https://connect-api.cloud.huawei.com/api/jas/open/players/player-accounts/team-player/convert”。

数据格式

请求：Content-Type: application/json

响应：Content-Type: application/json

#### 请求参数

#### Header

参数名称

是否必选

类型

参数说明

client_id

是

String

用于鉴权的客户端ID，获取方法参考[创建API客户端](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agcapi-getstarted-0000001111845114#section103mcpsimp)。

Authorization

是

String

认证信息，格式为“Authorization: Bearer ${access_token}”。access_token为[获取Token](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-References/agcapi-obtain_token-0000001158365043)中获取的access_token。

appId

是

String

游戏APP ID，获取方法参见[查看应用信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-view-app-info-0000002282674569)。

#### Body

请求Body中使用JSON格式携带更相关信息，参数如下表所示。

参数名称

是否必选

类型

参数说明

srcCpId

是

Long

游戏转出方的开发者Developer ID，获取方法参见[查看应用信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-view-app-info-0000002282674569)。

dstCpId

是

Long

游戏转入方的开发者Developer ID，获取方法参见[查看应用信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-view-app-info-0000002282674569)。

teamPlayerIds

是

List<String>

转让前，游戏的玩家标识teamPlayerId列表，列表数量至少1条，至多不超过1000条。

 说明：

建议开发者做好去重工作，确保teamPlayerId列表不要有重复的信息。

#### 请求示例

```ets
POST  HTTP/1.1
Host: connect-api.cloud.huawei.com
Content-Type: application/json
client_id: 41******7168
appId: "*****"
Authorization: Bearer ******
{
    "srcCpId": 4130****71055,
    "dstCpId": 4008****74585,
    "teamPlayerIds":[
        "**********",
        "**********",
        "**********"
    ]
}
```

#### 响应参数

参数名称

是否必选

类型

参数说明

ret

是

[JosRet](#ZH-CN_TOPIC_0000002506511027__zh-cn_topic_0000002273612857_zh-cn_topic_0000002195007290_li266952144619)

包含返回码及描述信息的JSON字符串，格式为{"code":*retcode*, "msg": "*description*"}，retcode为返回码，description为返回码描述信息。

data

是

List<[ConvertTeamPlayerIdItem](#ZH-CN_TOPIC_0000002506511027__zh-cn_topic_0000002273612857_zh-cn_topic_0000002195007290_li14201142814463)>

单次接口请求任务的查询结果。

- JosRet

参数名称

是否必选

类型

参数说明

code

是

int

单次接口请求任务的结果返回码：

  - 0：请求成功。
  - -1：请求失败。
  - 3002：鉴权错误。

msg

否

String

失败时的描述信息。

- ConvertTeamPlayerIdItem

参数名称

是否必选

类型

参数说明

srcCpId

是

Long

游戏转出方的开发者Developer ID。

srcTeamPlayerId

是

String

转让前，游戏的玩家标识teamPlayerId。

dstCpId

是

Long

游戏转入方的开发者Developer ID。

dstTeamPlayerId

是

String

转让后，游戏的玩家标识teamPlayerId。

errCode

是

int

查询单个teamplayerId的结果返回码：

  - 0：成功。
  - -1：失败。

#### 响应示例

```ets
{
    "ret": {
         "code": 0,
         "msg": "string"
    },
    "data": [
        {
            "srcCpId": 4330****71055,
            "srcTeamPlayerId": "******",
            "dstCpId": 4130****71055,
            "dstTeamPlayerId": "*****",
            "errCode": 0
        }
    ]
}
```

#### 调用示例

```ets
“Java”
/**
 * 批量转换teamPlayerId
 *
 * @param domain 请根据您的服务器部署地就近选择对应站点的URL，与获取token时使用的domain保持一致
 * @param client_id 用于鉴权的客户端ID
 * @param token post认证请求的token
 * @param teamPlayerIds 需要查询的teamPlayerId列表
 * @param appId 游戏appId
 */
private static void batchGetOpenIds(String domain, String client_id, String token, List<String> teamPlayerIds, String appId) {
        try {
            // 接口URL，domain请根据您的服务器部署地就近选择对应站点的URL且与获取token时使用的domain保持一致
            HttpPost post = new HttpPost(domain + "/api/jas/open/players/player-accounts/team-player/convert");
            // 构造消息头
            post.setHeader("Authorization", "Bearer " + token);
            post.setHeader("client_id", client_id);
            post.setHeader("appId", appId);
            // 构造消息实体
            JSONObject keyString = new JSONObject();
            keyString.put("srcCpId", srcCpId);
            keyString.put("dstCpId", dstCpId);
            keyString.put("teamPlayerId", teamPlayerIds); // 原主体的teamPlayerId
            StringEntity entity = new StringEntity(keyString.toString(), Charset.forName("UTF-8"));
            entity.setContentEncoding("UTF-8");
            // 发送Json格式的数据请求
            entity.setContentType("application/json");
            post.setEntity(entity);
            CloseableHttpClient httpClient = HttpClients.createDefault();
            HttpResponse response = httpClient.execute(post);
            int statusCode = response.getStatusLine().getStatusCode();
            if (statusCode == HttpStatus.SC_OK) {
                BufferedReader br =
                    new BufferedReader(new InputStreamReader(response.getEntity().getContent(), Consts.UTF_8));
                String result = br.readLine();
                System.out.println(result);
                JSONObject object = JSON.parseObject(result);
            }
            post.releaseConnection();
            httpClient.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
}
```

```ets
“C#”
/**
 * 批量转换teamPlayerId
 *
 * @param domain 请根据您的服务器部署地就近选择对应站点的URL，与获取token时使用的domain保持一致
 * @param clientId 用于鉴权的客户端ID
 * @param token post认证请求的token
 * @param teamPlayerIds 转让前游戏的玩家标识teamPlayerId列表
 * @param appId 游戏appId
 * @Param srcCpId 游戏转出方的开发者Developer ID
 * @Param dstCpId 游戏转入方的开发者Developer ID
 */
static void convertTeamPlayerId(string domain, string clientId, string token, List<string> teamPlayerIds, string appId, long srcCpId, long dstCpId)
{
    try
    {
        // 接口URL，domain请根据您的服务器部署地就近选择对应站点的URL且与获取token时使用的domain保持一致
        var requestUrl = domain + "/api/jas/open/players/player-accounts/team-player/convert";
        HttpWebRequest request = WebRequest.Create(requestUrl) as HttpWebRequest;
        request.Method = "post";
        request.ContentType = "application/json";
        request.Headers.Add("client_id", clientId);
        request.Headers.Add("Authorization", "Bearer " + token);
        request.Headers.Add("appId", appId);
        Dictionary<string, object> dic = new Dictionary<string, object>
        {
            {"srcCpId", srcCpId},
            {"dstCpId", dstCpId},
            {"teamPlayerIds", teamPlayerIds}
        };
        string sendData = JsonConvert.SerializeObject(dic, Formatting.Indented);
        Console.WriteLine(sendData);
        byte[] byteData = Encoding.GetEncoding("utf-8").GetBytes(sendData);
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
    catch (Exception e)
    {
        Console.WriteLine(e.ToString());
    }
}
```

```ets
“PHP”
/**
 * 批量转换teamPlayerId
 *
 * @param string $domain 请根据您的服务器部署地就近选择对应站点的URL，与获取token时使用的domain保持一致
 * @param string $client_id 用于鉴权的客户端ID
 * @param string $token post认证请求的token
 * @param array $teamPlayerIds 转让前游戏的玩家标识teamPlayerId列表
 * @param string $appId 游戏appid
 * @Param long $srcCpId 游戏转出方的开发者Developer ID
 * @Param long $dstCpId 游戏转入方的开发者Developer ID
 * @throws Exception
 */
public function batch_convert_teamPlayerIds(string $domain, string $client_id, string $token, array $teamPlayerIds, string $appId, long $srcCpId, long $dstCpId)
{
    $curl = curl_init();
    $data = array("teamPlayerIds" => $teamPlayerIds, "srcCpId" => $srcCpId, "dstCpId" => $dstCpId);
    curl_setopt_array($curl, array(
        CURLOPT_URL => $domain . '/api/jas/open/players/player-accounts/team-player/convert',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => '',
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_SSL_VERIFYHOST => false,
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS => json_encode($data),
        CURLOPT_HTTPHEADER => array(
            'client_id: ' . $client_id,
            'Authorization: Bearer ' . $token,
            'Content-Type: application/json',
            'appId: ' . $appId
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
```

```ets
“Python”
from getToken import *
class BatchConvertTeamPlayerIdsSolution:
    @staticmethod
    def batch_convert_team_player_ids(domain, client_id, access_token, team_player_id, app_id, src_cp_id, dst_cp_id):
        url = domain + '/api/jas/open/players/player-accounts/team-player/convert'
        data = {"teamPlayerIds": team_player_id, "srcCpId": src_cp_id， "dstCpId": dst_cp_id}
        payload = json.dumps(data)
        headers = {
            'client_id': client_id,
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json',
            'appId': app_id
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
if __name__ == "__main__":
    # 请根据您的服务器部署地就近选择对应站点的URL，这里以中国站点域名为例
    input_domain = 'https://connect-api.cloud.huawei.com'
    # 客户端ID
    input_client_id = 'xxxxxxx'
    # 客户端密钥
    input_client_secret = 'xxxxxxxx'
    # 获取token
    token_function = GetToken()
    input_access_token = token_function.get_token(input_domain, input_client_id, input_client_secret)
    # 游戏appId
    input_app_id = 'xxxxx'
    # 需要转换的teamplayerIds列表，单次最大不要超过1000个，这里以2个为例
    input_player_Ids = ['xxxxxxx', 'xxxxxx']
    # 游戏转出方的开发者Developer ID
    input_src_cp_id = 111111
    # 游戏转入方的开发者Developer ID
    input_dst_cp_id = 222222
    batch_function = BatchGetOpenIdsSolution()
    batch_function.batch_convert_team_player_ids(input_domain, input_client_id, input_access_token, input_player_Ids, input_app_id, input_src_cp_id, input_dst_cp_id)
```