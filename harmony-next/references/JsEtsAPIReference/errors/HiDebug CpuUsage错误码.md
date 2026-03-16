# HiDebug CpuUsage错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 11400104 CpuUsage统计异常

**错误信息**

The status of the system CPU usage is abnormal.

**错误描述**

当前CPU使用率状态异常。

**可能原因**

hiview服务进程未正常启动。

**处理步骤**

检查hiview进程的运行状态，重启hiview服务或系统。