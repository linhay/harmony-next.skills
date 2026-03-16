[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1019000001 内部错误

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

系统服务错误或其它内部错误。

**处理步骤**

1、重启设备后重试。

2、若重启后仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000002 用户未授权

**错误信息**

The user has not authorized the application to access this interface.

**错误描述**

用户未授权应用程序访问此接口。

**可能原因**

用户拒绝了权限申请。

**处理步骤**

1、请确认用户同意权限申请。

2、若用户操作正常，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000003 用户取消

**错误信息**

The user canceled the operation.

**错误描述**

用户取消了操作。

**可能原因**

用户取消了拉起应用列表picker页的操作。

**处理步骤**

1、请确认用户没有取消操作。

2、若用户操作正常，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000004 策略数量超限

**错误信息**

The number of strategies exceeds the upper limit.

**错误描述**

策略数量超过上限。

**可能原因**

添加管控策略太多，使其数量超过50条限制。

**处理步骤**

1、减少管控策略数量。

2、若策略数量正常，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000005 策略名称重复

**错误信息**

The strategy name is already existed.

**错误描述**

策略名称已存在。

**可能原因**

添加的策略名称已经存在。

**处理步骤**

1、先使用[策略查询接口（queryGuardStrategies）](../topics/system-services/GuardService（屏幕时间守护服务）.md#section1812105318579)获取应用名下有哪些策略。

2、将本次调用使用的策略名称更换成不重复的策略名称。

3、若策略名称正常，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000006 策略不存在

**错误信息**

Nonexistent strategy.

**错误描述**

没有对应名称的策略。

**可能原因**

试图修改、删除、启用、停止不存在的策略。

**处理步骤**

1、确认要修改的策略是否存在。

2、若策略存在，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000007 策略重复执行

**错误信息**

The strategy is already being executed.

**错误描述**

该策略已在执行中。

**可能原因**

试图启动的管控策略已在执行中。

**处理步骤**

1、确认策略是否已经在执行中。

2、若策略不在执行，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000008 策略未执行

**错误信息**

This strategy has not been started yet.

**错误描述**

该策略尚未开始执行。

**可能原因**

试图停止的管控策略已不在执行中。

**处理步骤**

1、确认策略是否已经停止。

2、若策略仍在执行，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1019000009 参数检查失败

**错误信息**

Parameter error. Possible causes:1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**错误描述**

1、必填参数为空。

2、参数类型不正确。

3、参数校验失败。无论是同步还是异步接口，此类异常大部分都通过同步的方式抛出。

**可能原因**

1、必选参数没有传入。

2、参数类型错误 (Type Error)。

3、参数数量错误 (Argument Count Error)。

4、空参数错误 (Null Argument Error)。

5、参数格式错误 (Format Error)。

6、参数值范围错误 (Value Range Error)。

**处理步骤**

1、请检查必选参数是否传入，或者传入的参数类型是否错误。对于参数校验失败，阅读参数规格约束，按照可能原因进行排查。

2、若参数正常，可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。