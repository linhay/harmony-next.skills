# @ohos.security.identifySensitiveContent (识别敏感内容)

识别敏感内容功能的实现是通过输入的[扫描策略](#ZH-CN_TOPIC_0000002553201323__policy)来检测指定文件中的敏感信息。


本模块首批接口从API version 21开始支持。后续版本的新增接口采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { identifySensitiveContent } from '@kit.DataProtectionKit';
```

#### identifySensitiveContent.scanFile

scanFile(filePath: string, identifyPolicies:Array<Policy>): Promise<Array<MatchResult>>

根据设置的策略，识别指定文件中的敏感内容。结果通过Promise方式异步返回。

**需要权限**：ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 识别的文件路径。 |
| identifyPolicies | Array<Policy> | 是 | 识别的策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<MatchResult>> | Promise对象。返回敏感内容识别的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[DLP服务错误码]([DLP服务错误码](../../errors/DLP服务错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 801 | Capability not supported. |
| 19110001 | Parameter error.Possible causes:1. Incorrect policy format. 2. Invalid parameter range. |
| 19110002 | Sensitive file content identification timed out. |
| 19110003 | The file is not supported. Possible causes:1. The file path does not exist. 2. The file type is not supported. 3. The file permission is not supported. |
| 19110004 | A system error has occurred. |

**示例：**

```ets
import { identifySensitiveContent } from '@kit.DataProtectionKit';

let filepath = "file://docs/storage/Users/currentUser/Desktop/test.txt";
let policies: Array<identifySensitiveContent.Policy> = [
  {"sensitiveLabel":"1", "keywords":[], "regex":""}
];
try {
  identifySensitiveContent.scanFile(filepath, policies).then(records => {
    console.info('scanFile finish');
  }).catch((err:Error) => {
    console.error('error message', err.message);
  })
} catch (err) {
  console.error('error message', err.message);
}
```

#### Policy

定义敏感内容识别策略。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensitiveLabel | string | 否 | 否 | 表示识别策略的标签。最大30字节。 |
| keywords | Array<string> | 否 | 否 | 表示关键字集合。Array最大50，每个元素最大30字节。 |
| regex | string | 否 | 否 | 表示正则表达式内容。最大512字节。  在输入字符串时，需检查某些特殊字符（如反斜杠 \、双引号 "、换行符等），不会被自动转义，确保字符串的输入效果。 |

#### MatchResult

显示敏感内容的识别结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensitiveLabel | string | 是 | 否 | 表示识别策略的标签。 |
| matchContent | string | 是 | 否 | 表示匹配内容。 |
| matchNumber | number | 是 | 否 | 表示识别内容的总数。 |