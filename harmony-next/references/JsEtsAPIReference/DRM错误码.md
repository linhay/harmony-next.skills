# DRM错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 24700101 未知错误

**错误信息**

Unknown error.

**错误描述**

未知错误。

**可能原因**

输入参数格式、数据类型错误，导致数据获取、数据转换失败等。

**处理步骤**

获取异常的描述，并检查系统错误日志，根据异常描述及日志中的错误描述处理。

#### 24700103 MediaKeySystem数量达到极限

**错误信息**

Too many MediaKeySystem instances.

**错误描述**

MediaKeySystem实例数量超过上限（64个）。

**可能原因**

无效的MediaKeySystem实例没有及时释放。

**处理步骤**

释放其他不再使用的MediaKeySystem资源。

#### 24700104 MediaKeySession数量达到极限

**错误信息**

Too many MediaKeySession instances.

**错误描述**

MediaKeySession实例数量超过上限（64个）。

**可能原因**

无效的MediaKeySession实例没有及时释放。

**处理步骤**

释放其他不再使用的MediaKeySession资源。

#### 24700201 服务异常

**错误信息**

Service error. For example, the service crashed.

**错误描述**

DRM服务异常。

**可能原因**

1.

底层DRM解决方案插件功能执行错误。

1.

DRM服务挂死等。

**处理步骤**

获取异常的描述，并检查系统错误日志，根据异常描述及日志中的错误描述处理。