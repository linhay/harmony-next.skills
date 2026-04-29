# crypto framework错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](通用错误码.md)。

#### 17620001 内存操作失败
**错误信息**

Memory operation failed.

**错误描述**

内存操作失败。

**可能原因**

当前系统内存分配失败。

**处理步骤**

1. 检查当前系统功能是否正常。
1. 业务检查数据是否超长，导致系统无法分配内存。

#### 17620002 ArkTS和C之间转换参数失败
**错误信息**

Failed to convert parameters between arkts and c.

**错误描述**

ArkTS和C之间转换参数失败。

**可能原因**

系统出现的不可预料的错误。

**处理步骤**

检查当前系统功能是否正常。

#### 17630001 算法相关的操作错误，调用三方算法库API出错

**错误信息**

Crypto operation error.

**错误描述**

调用三方算法库API出错。

**可能原因**

加解密算法框架与三方算法库交互时，出现错误。

**处理步骤**

检查该接口或相关联接口输入参数的正确性。

AES解密失败可参考[AES解密失败返回17630001](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-decryption-error-faq)。