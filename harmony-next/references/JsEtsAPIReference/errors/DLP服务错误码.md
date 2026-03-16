# DLP服务错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 19100001 入参错误

**错误信息**

Invalid parameter value.

**错误描述**

非法参数。

**可能原因**

1.

账号长度为空或长度大于1024。

1.

账号类型错误。

1.

aeskey或iv非法。

1.

授权到期时间低于系统时间。

1.

Fd小于0。

1.

tokenid等于0。

1.

包名为空。

1.

appIndex小于0。

1.

userId小于0。

**处理步骤**

请传入正确的参数。

#### 19100006 非DLP沙箱应用

**错误信息**

No permission to call this API, which is available only for DLP sandbox applications.

**错误描述**

调用方不是DLP沙箱应用。

**可能原因**

调用方不是DLP沙箱应用。

**处理步骤**

请确认调用场景后重试。

#### 19100007 DLP沙箱应用不允许调用此接口

**错误信息**

No permission to call this API, which is available only for non-DLP sandbox applications.

**错误描述**

调用方不可以是DLP沙箱应用。

**可能原因**

调用方不可以是DLP沙箱应用。

**处理步骤**

请确认调用场景后重试。

#### 19100011 系统服务工作异常

**错误信息**

The system ability works abnormally.

**错误描述**

系统服务工作异常。

**可能原因**

1.

DLP权限服务无法正常启动。

1.

DLP权限服务的RPC对象无法获取。

1.

DLP权限服务依赖的其他服务无法正常启动。

1.

IPC数据读取写入失败。

1.

服务未初始化。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备尝试。

#### 19100012 内存申请失败

**错误信息**

System memory is insufficient.

**错误描述**

内存申请失败。

**可能原因**

系统内存不足。

**处理步骤**

系统内存不足，请稍后重试，或者重启设备。

#### 19100016 want参数中没有uri

**错误信息**

The uri field is missing in the want parameter.

**错误描述**

want参数中没有uri。

**可能原因**

want参数中没有uri。

**处理步骤**

请传入正确的参数。

#### 19100017 want参数中parameters内没有displayName

**错误信息**

The displayName field is missing in the want parameter.

**错误描述**

want参数中parameters内没有displayName。

**可能原因**

want参数中parameters内没有displayName。

**处理步骤**

请传入正确的参数。

#### 19100018 应用未授权

**错误信息**

The application is not authorized.

**错误描述**

应用未授权。

**可能原因**

应用不在授信应用白名单中。

**处理步骤**

请设置授信应用白名单。

#### 19100021 设置企业应用策略失败

**错误信息**

Failed to set the enterprise policy.

**错误描述**

设置企业应用策略失败。

**可能原因**

输入策略格式异常。

**处理步骤**

请检查策略格式，并进行重试。

#### 19110001 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

1.

策略格式错误。

1.

参数范围错误。

**处理步骤**

请传入正确的参数。

#### 19110002 文件敏感信息识别超时

**错误信息**

Sensitive file content identification timed out.

**错误描述**

文件敏感信息识别超时。

**可能原因**

文件敏感信息识别超时。

**处理步骤**

请等待一段时间后重试。

#### 19110003 文件不支持

**错误信息**

The file is not supported.

**错误描述**

文件不支持。

**可能原因**

1.

文件路径不存在。

1.

文件类型不支持。

1.

文件权限不支持。

**处理步骤**

请确认传入的文件是否正确。

#### 19110004 系统功能运行异常

**错误信息**

A system error has occurred.

**错误描述**

系统功能运行异常。

**可能原因**

1.

服务无法正常启动。

1.

服务依赖的服务无法正常启动。

1.

IPC数据读写识别。

1.

服务未初始化。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备尝试。