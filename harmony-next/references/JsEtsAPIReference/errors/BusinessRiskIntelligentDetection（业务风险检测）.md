# BusinessRiskIntelligentDetection（业务风险检测）

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**1012500001 内部异常**

错误信息

Internal error.

错误描述

内部异常。

可能原因

接口调用超过次数限制或接口执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

**1012500002 设备网络异常**

错误信息

The network is unreachable.

错误描述

设备网络异常。

可能原因

设备未联网。

处理步骤

连接网络后重新发起请求。

**1012500003 访问云端服务器异常**

错误信息

Access cloud server fail.

错误描述

访问云端服务器异常。

可能原因

云侧服务不稳定或异常。

处理步骤

重新发起请求。

**1012500004 权限校验失败**

错误信息

Verify cloud capability fail.

错误描述

权限校验失败。

可能原因

应用hap未开通Device Security服务。

处理步骤

参考[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)在AppGallery Connect开通Device Security服务，开通Device Security服务后重试。

**1012500005 API调用次数超过限制**

错误信息

The interface access frequency exceeds the limit.

错误描述

API调用次数超过限制。

6.0.0(20)及以后版本新增API的调用次数超过限制时，均返回该错误码。

可能原因

应用调用指定API超过当前周期调用限制，参考[服务配额](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-quota)。

处理步骤

在下一个计数周期再次调用API。

**1012500006 API调用超时**

错误信息

Internal timeout.

错误描述

API调用超时。

可能原因

应用调用指定API超时。

处理步骤

重新发起请求。

**1012500007 参数检查失败**

错误信息

Invalid parameters.

错误描述

参数检查失败。

6.0.0(20)版本开始新增该错误码。

可能原因

必选参数没有传入，或者参数类型、参数取值错误。

处理步骤

请检查必选参数是否没有传入，或者传的参数类型、参数取值是否错误。