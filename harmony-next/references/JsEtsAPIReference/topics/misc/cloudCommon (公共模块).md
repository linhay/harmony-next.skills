# cloudCommon (公共模块)

本模块提供初始化云开发服务的能力。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { cloudCommon } from '@kit.CloudFoundationKit';
```

**cloudCommon.init**

init(options?: CloudOptions): void

初始化云开发服务。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | CloudOptions | 否 | 设置初始化参数。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

云函数业务免鉴权，开发云函数无需获取用户凭据。开发云存储或云数据库业务则需要获取用户凭据。获取用户凭据有两种方式，以下代码仅以通过AGC认证服务SDK获取为例，更多信息可参考[AuthProvider](#ZH-CN_TOPIC_0000002522242324__authprovider)。

```ets
import { cloudCommon } from '@kit.CloudFoundationKit';
import { request } from '@kit.BasicServicesKit';
import auth from '@hw-agconnect/auth';

let provider = auth.getAuthProvider(); // 在用户登录成功的情况下调用此方法获取authProvider
cloudCommon.init({
  region: cloudCommon.CloudRegion.CHINA,
  authProvider: provider,
  functionOptions: { timeout: 10 * 1000 },
  storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
  databaseOptions: { schema: "schema.json", traceId: "traceId" }
})
```

**CloudOptions**

初始化选项。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| region | CloudRegion | 否 | 是 | 存储地，默认为CHINA。 |
| authProvider | AuthProvider | 否 | 是 | 认证提供方。 |
| functionOptions | FunctionOptions | 否 | 是 | 云函数初始化设置。 |
| storageOptions | StorageOptions | 否 | 是 | 云存储初始化设置。 |
| databaseOptions | DatabaseOptions | 否 | 是 | 云数据库初始化设置。 |

**CloudRegion**

枚举， 存储地类型。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHINA | 0 | 数据存储到中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| GERMANY | 1 | 数据存储到德国区。 |
| RUSSIA | 2 | 数据存储到俄罗斯。 |
| SINGAPORE | 3 | 数据存储到新加坡。 |

**AuthProvider**

认证提供方。开发者可以使用[AGC认证服务SDK](https://developer.huawei.com/consumer/cn/doc/app/agc-help-auth-introduction-0000002271496181)获取AuthProvider，或者使用华为账号服务Access Token接口自定义AuthProvider。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

**getAccessToken**

getAccessToken(isForceRefresh: boolean): Promise<string>

获取用户凭据。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isForceRefresh | boolean | 是 | 是否需要强制刷新返回用户凭据。true表示需要，false表示不需要。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回用户凭据（该用户凭据可使用AGC认证服务SDK或华为账号服务的获取用户级凭证接口生成）。 |

示例：

-

（推荐）方式一：使用AGC认证服务SDK获取AuthProvider（SDK会主动调用getAccessToken方法，无需开发者操作）

  1. 在应用级（一般为entry目录下）“oh-package.json5”文件里面添加认证服务SDK依赖。
```ets
"dependencies": {
  "@hw-agconnect/auth": "^1.0.5"
}
```

  1. 使用手机、邮箱或华为账号进行[登录认证](https://developer.huawei.com/consumer/cn/doc/app/agc-help-auth-login-phone-0000002271416141)。

  1. 认证成功后获取AuthProvider。
```ets
import { cloudCommon } from '@kit.CloudFoundationKit';
import auth from '@hw-agconnect/auth';
import { request } from '@kit.BasicServicesKit';

let authProvider = auth.getAuthProvider();
cloudCommon.init({
  region: cloudCommon.CloudRegion.CHINA,
  authProvider: authProvider,
  functionOptions: { timeout: 10 * 1000 },
  storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
  databaseOptions: { schema: "schema.json", traceId: "traceId" }
})
```

-

方式二：

  1. 使用华为账号服务的[获取用户级凭证](获取用户级凭证.md)接口获取refresh_token，然后基于refresh_token换取access_token自定义AuthProvider。可参考如下示例代码换取：
```ets
import { cloudCommon } from '@kit.CloudFoundationKit';
import { http } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let accessToken = '';

export class MyAuthProvider implements cloudCommon.AuthProvider {
  async getAccessToken(isForceRefresh: boolean): Promise<string> {
    let data =
      "grant_type=refresh_token&client_id=xxxx&client_secret=xxxx&refresh_token=";
    let refreshToken =
      encodeURIComponent('xxxx'); // xxxx为使用华为账号服务获取用户级凭证接口获取的refresh_token
    // access_token过期则强制刷新
    if (isForceRefresh) {
      data = data + refreshToken;
      try {
        let httpRequest = http.createHttp();
        let ohosOptions: http.HttpRequestOptions = {
          method: http.RequestMethod.POST,
          header: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          extraData: data,
        };
        let url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
        let resp = await httpRequest.request(url, ohosOptions);
        accessToken = JSON.parse(resp.result.toString()).access_token;
      } catch (err) {
        hilog.error(0x0000, 'testTag', `Failed to get accessToken, code: ${err.code}, message: ${err.message}`);
      }
    return Promise.resolve(accessToken);
  }
```

  1. 使用自定义的AuthProvider完成初始化。
```ets
import { cloudCommon } from '@kit.CloudFoundationKit';
import { request } from '@kit.BasicServicesKit';
import { MyAuthProvider } from 'xxx'; // xxx为您自定义的AuthProvider文件路径

let authProvider = new MyAuthProvider();
cloudCommon.init({
  region: cloudCommon.CloudRegion.CHINA, // 请填写实际数据处理位置
  authProvider: authProvider,
  functionOptions: { timeout: 10 * 1000 },
  storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
  databaseOptions: { schema: "schema.json", traceId: "traceId" }
})
```

**FunctionOptions**

云函数初始化配置参数。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | 函数请求超时时间，单位毫秒，默认为70*1000毫秒。 取值范围无限制，会转成unsigned long类型。 |

**StorageOptions**

云存储初始化配置参数。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | request.agent.Mode | 否 | 是 | 任务的模式。前端任务在应用切换到后台一段时间后失败/暂停；后台任务不受影响。默认为BACKGROUND。 - BACKGROUND：后台任务。 - FOREGROUND：前端任务。 |
| network | request.agent.Network | 否 | 是 | 使用的网络类型。网络不满足设置条件时，未执行的任务等待执行，执行中的任务失败/暂停。默认为Network.ANY。 - Network.ANY：不限网络类型。 - Network.WIFI：无线网络。 - Network.CELLULAR：蜂窝数据网络。 |

**DatabaseOptions**

云数据库初始化配置参数。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| schema | string | 否 | 是 | 全量数据表结构及权限定义，使用从云端下载的schema.json配置文件，默认读取工程固定目录：rawfile。 |
| traceId | string | 否 | 是 | 用户自定义的traceId，用于跟踪请求操作。 自定义traceId的长度必须大于或等于1个字符，小于或等于32个字符，只能包含以下2种类型： - 字母（a-f） - 数字（0-9） 默认值为空。 |