[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1000101101 应用未订阅

**错误信息**

The application has not been registered with the InsightIntent.

**错误描述**

应用未在InsightIntent进行订阅时，系统会产生此错误码。

**可能原因**

应用未在InsightIntent进行订阅（未配置白名单）。

**处理步骤**

参考[开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-access-flow)，进行InsightIntent订阅申请（白名单）。

[]()[]()

#### 1000101102 小艺停止服务

**错误信息**

HUAWEI Assistant has stopped providing services.

**错误描述**

小艺停止服务，共享失败，系统会产生此错误码。

**可能原因**

小艺开关未打开。

**处理步骤**

打开设置-小艺开关。

[]()[]()

#### 1000101104 超过应用共享次数

**错误信息**

The number of sharing times exceeds the limit.

**错误描述**

超过应用共享次数限制，系统会产生此错误码。

**可能原因**

应用共享次数太高。

**处理步骤**

优化业务逻辑，减少共享次数。

[]()[]()

#### 1000101105 超过单次共享数据大小限制

**错误信息**

The size of a single shared data exceeds the limit.

**错误描述**

超过单次共享数据大小限制，系统会产生此错误码。

**可能原因**

单次共享的数据太大。

**处理步骤**

减少单次共享的数据量。

[]()[]()

#### 1000101106 超过所有应用共享总次数限制

**错误信息**

Exceeded the maximum number of sharing times of all applications.

**错误描述**

超过当日所有应用共享总次数限制，系统会产生此错误码。

**可能原因**

系统接收到的共享次数超过当日总上限。

**处理步骤**

延迟共享时间，第2天再进行共享。

[]()[]()

#### 1000101107 过多SID刷新请求

**错误信息**

Too many Service Open ID renew requests.

**错误描述**

超过SID刷新请求限制，系统会产生此错误码。

**可能原因**

SID刷新请求过于频繁。

**处理步骤**

延迟请求时间，第2天再进行刷新请求。或将renew参数设为false获取缓存的SID。

[]()[]()

#### 1000101201 服务异常

**错误信息**

The service is abnormal.

**错误描述**

服务异常时，系统会产生此错误码。

**可能原因**

服务异常。

**处理步骤**

系统异常，建议重启设备重试。