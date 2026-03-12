# spaceDataTransfer (空间数据传输)

空间数据传输为企业安全管控类[MDM](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit)应用提供下发空间互传策略能力，提供设置审批信息、获取审批信息的能力。

供企业安全管控类MDM应用申请权限后使用。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { fileTransfer } from '@kit.EnterpriseSpaceKit';
```

#### AuditInfo

审批信息。

**系统能力**：SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

auditId

string

否

否

表示在发起审批时由数据库自动生成的审批ID，通常为由9位数字组成的字符串。不能为空字符串。

userId

string

否

否

表示用户ID。

userName

string

否

否

表示用户名称。

time

number

否

否

表示整形转换后的审批时间戳，以ms为单位。

comments

string

否

否

表示审批评论。无位数限制。

status

string

否

否

表示文件审批状态。其中，"1"表示等待审批，"2"表示取消审批，"3"表示拒绝审批，"4"表示同意审批。

#### setAuditInfo

setAuditInfo(transactionNum: string, info: AuditInfo): number

设置审批信息，将审批结果返回给空间互传应用。

**需要权限：**ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT

**系统能力：**SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

transactionNum

string

是

在传输文件时由数据库自动生成的传输编号，通常为由19位数字组成的字符串。不能为空字符串。

info

[AuditInfo](#section14605182931520)

是

表示审批信息。

**返回值：**

类型

说明

number

返回设置审批信息的结果。结果为0代表设置审批信息成功。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

the application does not have permission to call this function.

1020300001

System service exception.

1020300002

Parameter error.

**示例：**

```ets
import { fileTransfer } from '@kit.EnterpriseSpaceKit';

const transactionNum: string = '1111111';
const info: fileTransfer.AuditInfo = {
  auditId: '123456',
  userId: '100',
  userName: 'test',
  time: Date.now(),
  comments: 'Waiting approval',
  status: '1'
};
try {
  const ret: number = fileTransfer.setAuditInfo(transactionNum, info);
  console.info(`Succeeded in setting audit info, number:`, ret);
} catch (err) {
  console.error(`Failed to set audit info. Code: ${err.code}, message: ${err.message}`);
}
```

#### getAuditInfo

getAuditInfo(transactionNum: string): AuditInfo

获取审批信息。

**需要权限：**ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT

**系统能力：**SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

transactionNum

string

是

在传输文件时由数据库自动生成的传输编号，通常为由19位数字组成的字符串。不能为空字符串。

**返回值：**

类型

说明

[AuditInfo](#section14605182931520)

表示审批信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

the application does not have permission to call this function.

1020300001

System service exception.

1020300002

Parameter error.

**示例：**

```ets
import { fileTransfer } from '@kit.EnterpriseSpaceKit';

const transactionNum: string = '1111111';
try {
  const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
  console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
} catch (err) {
  console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
}
```

#### policyPush

policyPush(policyContext: string): void

配置工作空间互传单双通策略。具体而言，分别配置是否允许个人工作空间和企业工作空间向对端空间发送文件。

**需要权限：**ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT or ohos.permission.FILE_TRANSFER_OPERATION

**系统能力：**SystemCapability.EnterpriseSpace.SpaceDataTransfer

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

policyContext

string

是

下发单双通策略的内容。一级节点为**config**，其有5个二级节点，分别为**inEnable**、**incoming_check**、**outEnable**、**outgoing_check**和**checkpoint_config****。**每个节点负责不同的功能，共同构成了完整的策略配置。详细内容参考下表。

- **inEnable**：控制企业空间接收文件的权限。
- **incoming_check**：定义个人空间向企业空间发送文件时的检测规则。参数格式为字符串，内容会在后续详细解释。
- **outEnable **：控制企业空间外发文件的权限。
- **outgoing_check**：定义企业空间向个人空间发送文件时的检测规则。参数格式为字符串，内容会在后续详细解释。
- **checkpoint_config**：配置检测应用的信息，包括应用的包名、组件名、参数、检测函数编码。参数格式为字符串，内容会在后续详细解释。
- **approvalpoint_config**：配置审批点的信息，包括应用的包名和组件名。

**二级节点详细说明**

- **inEnable**：控制企业空间接收文件的权限。其值为“0”时，表示禁止；为“1”时，表示允许。

- **outEnable**：控制企业空间外发文件的权限。其值为“0”时，表示禁止；为“1”时，表示允许。

- **incoming_check**

**参数名称**

**功能描述**

**示例值**

data_list

定义个人空间向企业空间发送文件时的检测规则。

[ { "check_point": "VirusCheck", "check_point_name": "VirusCheck_in", "check_sequence": "Serial", "order": "0", "allow": "VirusCheck.result == 0", "forbidden": "VirusCheck.result == 1" } ]

- **outgoing_check**

**参数名称**

**功能描述**

**示例值**

data_list

定义企业空间向个人空间发送文件时的检测规则。

[ { "check_point": "SecurityCheck", "check_point_name": "SecurityCheck_out", "check_sequence": "Serial", "order": "0", "allow": "SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7", "approval": "SecurityCheck.Result == 10", "forbidden": "SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11" } ]

- **checkpoint_config**

**参数名称**

**功能描述**

**示例值**

data_list

配置检测应用的信息，包括应用的包名、组件名、参数、检测函数编码。

[ { "check_point": "VirusCheck", "check_point_name": "VirusCheck_in", "check_sequence": "Serial", "order": "0", "allow": "VirusCheck.result == 0", "forbidden": "VirusCheck.result == 1" } ]

- **approvalpoint_config**

**参数名称**

**功能描述**

**示例值**

data_list

定义个人空间向企业空间发送文件时的检测规则。

[ { "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts", "ability_name": "TestApprovalAbility" } ]

**三级节点详细说明**

- **incoming_check**下的**data_list**

**参数名称**

**功能描述**

**示例值**

check_point

检测点类型。

"VirusCheck"

check_point_name

检测点名称。

"VirusCheck_in"

check_sequence

检测顺序类型。

"Serial"

order

检测点顺序号。

"0"

allow

放通动作配置，通过表达式配置。

"VirusCheck.result == 0"

forbidden

拦截动作配置，通过表达式配置。

"VirusCheck.result == 1"

- **outgoing_check**下的**data_list**

**参数名称**

**功能描述**

**示例值**

check_point

检测点类型。

"SecurityCheck"

check_point_name

检测点名称。

"SecurityCheck_out"

check_sequence

检测顺序类型。

"Serial"

order

检测点顺序号。

"0"

allow

放通动作配置，通过表达式配置。

"SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7"

approval

审批动作配置，通过表达式配置。

"SecurityCheck.Result == 10"

forbidden

拦截动作配置，通过表达式配置。

"SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11"

- **checkpoint_config**下的**data_list**

**参数名称**

**功能描述**

**示例值**

check_point_name

检测点名称。

"SecurityCheck" 或 "VirusCheck"

bundle_name

包名。

"com.example.enterprisespacekit_samplecode_clientdemo_arkts"

ability_name

组件名。

"TestScanAbility"

func_code

检测函数编码。

"2" 或 "3"

send_param

检测发起的参数配置。暂无实际使用场景，为预留字段。

""

recv_msg

检测响应的参数配置。暂无实际使用场景，为预留字段。

""

type

检测点类型，有病毒检测、资产检测和其他类型，分别为“1”、“2”和“3”。当前只支持病毒检测和资产检测类型。

“1”

- **approvalpoint_config**下的**data_list**

**参数名称**

**功能描述**

**示例值**

bundle_name

包名。

"com.example.enterprisespacekit_samplecode_clientdemo_arkts"

ability_name

组件名。

"TestApprovalAbility"

policyContext内容可参考如下：

```ets
{
  "config": {
    "inEnable": "1",
    "incoming_check": {
      "data_list": [
        {
          "allow": "VirusCheck.result == 0",
          "approval": "",
          "check_point": "VirusCheck",
          "check_point_name": "VirusCheck_in",
          "check_sequence": "Serial",
          "encryption": "",
          "forbidden": "VirusCheck.result == 1",
          "order": "0"
        }
      ]
    },
    "outEnable": "1",
    "outgoing_check": {
      "data_list": [
        {
          "allow": "SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7",
          "approval": "SecurityCheck.Result == 10",
          "check_point": "SecurityCheck",
          "check_point_name": "SecurityCheck_out",
          "check_sequence": "Serial",
          "encryption": "",
          "forbidden": "SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11",
          "order": "0"
        }
      ]
    },
    "checkpoint_config": {
      "data_list": [
        {
          "check_point_name": "SecurityCheck",
          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",
          "ability_name": "TestScanAbility",
          "func_code": "2",
          "send_param": "",
          "recv_msg": "",
          "type": "2"
        },
        {
          "check_point_name": "VirusCheck",
          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",
          "ability_name": "TestScanAbility",
          "func_code": "3",
          "send_param": "",
          "recv_msg": "",
          "type": "1"
        }
      ]
    },
    "approvalpoint_config": {
      "data_list": [
        {
          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",
          "ability_name": "TestApprovalAbility"
        }
      ]
    }
  }
}
```

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

201

the application does not have permission to call this function.

1020300001

System service exception.

1020300002

Parameter error.

**示例：**

```ets
import { fileTransfer } from '@kit.EnterpriseSpaceKit';

const policyContext: string =
  '{\"config\":{\"inEnable\":\"1\",\"incoming_check\":{\"data_list\":[{\"allow\":\"VirusCheck.result == 0\",\"approval\":\"\",\"check_point\":\"VirusCheck\",\"check_point_name\":\"VirusCheck_in\",\"check_sequence\":\"Serial\",\"encryption\":\"\",\"forbidden\":\"VirusCheck.result == 1\",\"order\":\"0\"}]},\"outEnable\":\"0\",\"outgoing_check\":{\"data_list\":[{\"allow\":\"SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7\",\"approval\":\"SecurityCheck.Result == 10\",\"check_point\":\"SecurityCheck\",\"check_point_name\":\"SecurityCheck_out\",\"check_sequence\":\"Serial\",\"encryption\":\"\",\"forbidden\":\"SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11\",\"order\":\"0\"}]},\"checkpoint_config\":{\"data_list\":[{\"check_point_name\":\"SecurityCheck\",\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestScanAbility\",\"func_code\":\"2\",\"send_param\":\"\",\"recv_msg\":\"\",\"type\":\"2\"},{\"check_point_name\":\"VirusCheck\",\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestScanAbility\",\"func_code\":\"3\",\"send_param\":\"\",\"recv_msg\":\"\",\"type\":\"1\"}]},\"approvalpoint_config\":{\"data_list\":[{\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestApprovalAbility\"}]}}}';
try {
  fileTransfer.policyPush(policyContext);
  console.info(`Succeeded in pushing policy`);
} catch (err) {
  console.error(`Failed to push policy. Code: ${err.code}, message: ${err.message}`);
}
```