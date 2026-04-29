# TrustedAuthentication （数字盾服务）

**1019100001 权限校验失败**

错误信息

permission denied.

错误描述

权限校验失败。

可能原因

应用hap未申请数字盾服务AGC权限。

处理步骤

只允许符合使用场景的应用申请该权限。开通数字盾服务，请参考“[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)”。

**1019100002 参数检查失败**

错误信息

argument is invalid.

错误描述

参数检查失败。

可能原因

必选参数没有传入，或者参数类型、规格错误。

处理步骤

请检查必选参数是否没有传入，或者传的参数类型、规格是否错误。

**1019100003 密码认证连续失败次数达到要求的最大次数**

错误信息

The number of consecutive authentication failures exceeds the maximum.

错误描述

密码认证连续失败次数达到数字盾业务要求的最大次数。

可能原因

用户忘记密码导致的连续认证失败 或 攻击者尝试通过密码穷举进行盾密码的暴力破解。

处理步骤

数字盾锁定，开发者可根据业务场景向用户提供对应的数字盾重新激活流程指导。

**1019100004 删除密码失败**

错误信息

delete trusted authentication password failed.

错误描述

内部异常。

可能原因

删除密码执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100005 密码认证失败**

错误信息

trusted authentication verify failed.

错误描述

内部异常。

可能原因

密码认证执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100006 输入文本信息检查失败**

错误信息

secure image process failed.

错误描述

内部异常。

可能原因

设备不支持TUI或TUI服务异常。

处理步骤

请优先确认对应设备是否支持数字盾能力，若支持，则优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100007 不支持的图片格式**

错误信息

the input image format is invalid.

错误描述

输入图片格式不符合要求。

可能原因

输入图片格式不符合要求，数字盾服务相关接口要求可传入的图片格式为RGBA PNG格式图片，且图片长宽约束均在216内。

处理步骤

使用数字盾服务要求的图片格式作为输入。

**1019100008 用户取消操作**

错误信息

The user canceled the operation.

错误描述

用户取消对应业务操作。

可能原因

用户在TUI界面内取消对应操作 或 TUI界面2min内用户无操作自动退出。

处理步骤

非异常场景，用户主动结束对应流程。

**1019100009 备份数据导出失败**

错误信息

Failed to export data.

错误描述

备份数据导出失败。

可能原因

未进行对应数据备份导入 或 导出备份数据时密码认证失败。

处理步骤

确保数据已正确导入且导出过程中用户密码认证通过。

**1019100010 备份数据导入失败**

错误信息

Failed to import data.

错误描述

备份数据导入失败。

可能原因

对应备份数据仅可导入一次，重复导入备份数据时报错。

处理步骤

确保首次导入数据正确，当数字盾服务关闭时，导入数据的生命周期结束。

**1019100011 不合法的TUI认证信息**

错误信息

The text content cannot be displayed.

错误描述

不合法的TUI认证信息。

可能原因

输入的认证信息格式不合法或超过约定长度。

处理步骤

检查输入的TUI认证信息内容是否符合要求。

**1019100012 无效的authID**

错误信息

Invalid authentication ID.

错误描述

无效的authID。

可能原因

在进行对应操作时，传入的密码authID与密码创建时获取的authID不一致。

处理步骤

确认传入的authID是否为密码创建时获取的authID。

**1019100013 创建密码失败**

错误信息

Set trusted authentication password failed.

错误描述

内部异常。

可能原因

密码创建执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100014 修改密码失败**

错误信息

Modify trusted authentication password failed.

错误描述

内部异常。

可能原因

密码修改执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100015 生物认证authToken签发失败**

错误信息

Get biometric authToken failed.

错误描述

内部异常。

可能原因

输入的tuiAuthToken和bioAuthToken未自同一次会话 或 bioAuthToken的ATL等级不为ATL4。

处理步骤

请优先排查可能原因，若均不涉及，通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100016 数字盾服务未使能**

错误信息

The trusted authentication feature is not enabled.

错误描述

数字盾服务未使能。

可能原因

对应类型设备不支持数字盾服务，或该设备上数字盾服务使能失败。

处理步骤

确认对应设备是否支持数字盾服务。

**1019100017 获取剩余认证次数失败**

错误信息

Failed to get the remaining number of authentication attempts.

错误描述

获取数字盾剩余认证次数失败。

可能原因

获取数字盾剩余认证次数执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100018 关闭对应生物特征认证能力失败**

错误信息

Failed to unbind the corresponding biometric data.

错误描述

关闭对应生物特征认证能力失败。

可能原因

关闭对应生物特征认证能力执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1019100019 与绑定的生物特征不匹配**

错误信息

The biometric data for authentication does not match the bound biometric feature.

错误描述

认证的生物特征与绑定的生物特征不匹配。

可能原因

认证的生物特征如指纹，与实际绑定的指位不一致。

处理步骤

提醒用户使用绑定时的生物特征进行认证。

**1019100020 已绑定对应生物特征**

错误信息

The biometric data has already been bound.

错误描述

重复绑定生物特征信息。

可能原因

在已经绑定对应生物特征信息的情况下，重复绑定对应生物特征。

处理步骤

提示用户已绑定对应生物特征。

**1019100021 未绑定对应生物特征**

错误信息

The corresponding biometric data has not been bound.

错误描述

未绑定对应生物特征。

可能原因

使用生物特征进行认证或解绑指定生物特征前，校验发现对应的生物特征暂未绑定。

处理步骤

确认是否已经绑定对应生物特征。