# @ohos.security.identifySensitiveContent (识别敏感内容)

识别敏感内容功能的实现是通过输入的[扫描策略](#ZH-CN_TOPIC_0000002497445398__policy)来检测指定文件中的敏感信息。

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

参数名类型必填说明filePathstring是识别的文件路径。identifyPoliciesArray<[Policy](#ZH-CN_TOPIC_0000002497445398__policy)>是识别的策略。

**返回值：**

类型说明Promise<Array<[MatchResult](#ZH-CN_TOPIC_0000002497445398__matchresult)>>Promise对象。返回敏感内容识别的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[DLP服务错误码](../../errors/DLP服务错误码.md)。

错误码ID错误信息201permission denied.801Capability not supported.19110001Parameter error.Possible causes:1. Incorrect policy format. 2. Invalid parameter range.19110002Sensitive file content identification timed out.19110003The file is not supported. Possible causes:1. The file path does not exist. 2. The file type is not supported. 3. The file permission is not supported.19110004A system error has occurred.

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

名称类型只读可选说明sensitiveLabelstring否否表示识别策略的标签。最大30字节。keywordsArray<string>否否表示关键字集合。Array最大50，每个元素最大30字节。regexstring否否

表示正则表达式内容。最大512字节。

在输入字符串时，需检查某些特殊字符（如反斜杠 \、双引号 "、换行符等），不会被自动转义，确保字符串的输入效果。

#### MatchResult

显示敏感内容的识别结果。

**系统能力：** SystemCapability.Security.DataLossPrevention

名称类型只读可选说明sensitiveLabelstring是否表示识别策略的标签。matchContentstring是否表示匹配内容。matchNumbernumber是否表示识别内容的总数。