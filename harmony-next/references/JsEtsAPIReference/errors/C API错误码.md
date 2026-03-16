# C API错误码

以下仅介绍Game Service Kit特有错误码，通用错误码请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 1010300001 游戏内部通用错误

**错误信息**

System internal error.

**错误描述**

游戏内部通用错误。

**可能原因**

Game Service Kit系统内部错误。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354579010004&keyWord=Game Service Kit)提交问题，华为工程师会及时处理。

#### 1010300002 鉴权失败

**错误信息**

Invalid caller.

**错误描述**

鉴权失败。

**可能原因**

网络连接或传参错误。

**处理步骤**

1. 首次使用设备进行登录时，请确认网络连接正常。
1. 请检查[HMS_GamePerformance_Init](../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1045d9d8f4e7972b44ff95571afca8f9)接口传参是否正确。

#### 1010300003 非法请求

**错误信息**

Invalid request.

**错误描述**

非法请求。

**可能原因**

未初始化或初始化未成功时，调用了其他接口。

**处理步骤**

请先调用[HMS_GamePerformance_Init](../topics/misc/GamePerformance.md#ZH-CN_TOPIC_0000002474311058__ga1045d9d8f4e7972b44ff95571afca8f9)接口，并确保调用成功。

#### 1010300004 参数错误

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

- 必填参数为空。
- 参数校验失败。

**处理步骤**

请检查必选参数是否传入，或者传入参数是否符合要求。