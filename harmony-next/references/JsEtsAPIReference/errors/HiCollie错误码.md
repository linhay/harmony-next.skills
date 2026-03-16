# HiCollie错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 29800001 系统服务获取失败

**错误信息**

Wrong thread context.The function can not be called from main thread.

**错误描述**

调用接口线程错误。

**可能原因**

无法从主线程调用该接口服务。

**处理步骤**

在非主线程调用该接口服务。

#### 29800002 远程调用失败

**错误信息**

Remote call failed.

**错误描述**

当前接口请求远程服务失败。

**可能原因**

服务未启动或崩溃。

**处理步骤**

建议重试。

#### 29800003 无效的timer名称

**错误信息**

Invalid timer name.

**错误描述**

timer name是无效的。

**可能原因**

传入的字符指针name为nullptr或name指向空字符串。

**处理步骤**

检查传入的name参数，确保其为非空字符指针，且指向非空字符串。

#### 29800004 无效的timeout值

**错误信息**

Invalid timeout value.

**错误描述**

timeout值是无效的。

**可能原因**

传入的timeout的值为0。

**处理步骤**

检查传入的timeout，确保其大于0。

#### 29800005 错误的进程上下文

**错误信息**

Wrong process context.

**错误描述**

进程上下文错误。

**可能原因**

接入函数执行时长检测定时器的进程是appspawn或nativespawn进程。

**处理步骤**

请勿在appspawn和nativespawn进程中接入hicollie检测。

#### 29800006 错误的timer id参数

**错误信息**

Wrong timer id output param.

**错误描述**

错误的任务id值参数。

**可能原因**

- 传入的整型指针id为nullptr；
- 接入函数执行时长检测机制的进程中hicollie插件同时存在任务数达到最大值128。

**处理步骤**

- 检查传入的id参数，确保其为非空整型指针；
- 重试或减少该进程中hicollie检测机制的在其他地方的调用。