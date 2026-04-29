# SecurityAudit（安全审计）

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

以下仅介绍本模块客户端特有错误码及原因分析，若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

**201 权限校验失败**

错误信息

check permission fail.

错误描述

权限校验失败。

可能原因

应用包未申请ohos.permission.QUERY_AUDIT_EVENT或ohos.permission.kernel.AUTH_AUDIT_EVENT权限。

处理步骤

只允许清单内的企业类应用申请该权限，申请方式请参考：[申请使用企业类应用可用权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-enterprise-apps)。

**401 参数检查失败**

错误信息

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

错误描述

参数检查失败。

可能原因

必选参数没有传入，或者参数类型、规格错误。

处理步骤

请检查必选参数是否没有传入，或者传的参数类型、规格是否错误。

**1012000001 内部异常**

错误信息

Internal error.

错误描述

内部异常。

可能原因

接口执行流程中调用系统其它接口出现异常。

处理步骤

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

**1012000002 客户端总数超限**

错误信息

The number of clients exceeds the global upper limit.

错误描述

客户端总数超限。

可能原因

当前设备申请的审计事件客户端实例超过16个的阈值。

处理步骤

通知类事件应用场景请使用deleteClient接口删除不再使用的客户端实例，并使用newClient接口重新申请审计事件通知类客户端实例；

阻断类事件应用场景请使用deleteAuthClient接口删除不再使用的客户端实例，并使用newAuthClient接口重新申请审计事件阻断类客户端实例。

**1012000003 进程内客户端数量超限**

错误信息

The number of clients exceeds the current process upper limit.

错误描述

进程内客户端数量超限。

可能原因

当前进程申请的审计事件客户端实例超过2个的阈值。

处理步骤

通知类事件应用场景请使用deleteClient接口删除不再使用的客户端实例，并使用newClient接口重新申请审计事件通知类客户端实例；

阻断类事件应用场景请使用deleteAuthClient接口删除不再使用的客户端实例，并使用newAuthClient接口重新申请审计事件阻断类客户端实例。

**1012000004 过滤条件数量超限**

错误信息

The number of filters exceeds the upper limit.

错误描述

过滤条件超限。

可能原因

当前客户端实例所设置的过滤条件值的数量超过256个的阈值。

处理步骤

请根据不同的应用场景，使用客户端实例提供的removeFilter删除不再需要的过滤条件，并使用客户端实例提供addFilter重新设置最新的过滤条件。

**1012000005 事件不支持此过滤条件**

错误信息

The event does not support the filter condition.

错误描述

事件不支持此过滤条件。

可能原因

设置过滤条件的事件id不支持当前过滤条件。

处理步骤

请检查当前事件是否支持所设置过滤条件，如果不支持请更换过滤条件。

**1012000006 查询的进程数量超限**

错误信息

The number of queried processes exceeds the threshold.

错误描述

查询的进程数量超限。

可能原因

当前进程申请查询的进程数量超过16个的阈值。

处理步骤

请减少单次查询的进程数量，再次查询。

**1012000007 找不到对应的阻断事件**

错误信息

The auth event cannot be found.

错误描述

找不到对应的阻断事件。

可能原因

阻断类事件应用场景下，用户订阅的阻断事件的事件发起者已异常退出，或者该事件已经被处理，导致阻断事件已无效。

处理步骤

请检查当前事件是否超时未处理导致发起者退出，或者是已经处理过，请使用未设置阻断策略的事件。