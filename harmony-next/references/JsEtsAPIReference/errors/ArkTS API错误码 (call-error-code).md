[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1007200001 参数无效

**错误信息**

Invalid parameter value.

**错误描述**

参数异常。

**可能原因**

1、参数数量错误，例如必填参数未传递等。

2、通话状态错误，最常见的是上报去电，如果状态不是VOIP_CALL_STATE_DIALING，则上报失败。

3、通话类型错误，目前通话类型只支持语音通话VOIP_CALL_VOICE和视频通话VOIP_CALL_VIDEO两种。

4、callId不匹配，例如，上报通话状态改变、上报音频状态改变时，如果传入的callId在已有的通话中查不到，则上报失败。

5、重复上报，例如，同一路通话，如果上报了两次去电，则上报失败。

**处理步骤**

1、请确认上述参数传递正确。

2、也可以通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1007200002 服务未启动

**错误信息**

Operation failed. Cannot connect to service.

**错误描述**

Call Service Kit未启动。

**可能原因**

调用接口后Call Service Kit服务启动失败。

**处理步骤**

通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1007200003 内部错误

**错误信息**

System internal error.

**错误描述**

Call Service Kit内部错误。

**可能原因**

1、通话数量超限，来电最多允许3路，去电只能有1路，超过会上报失败。

2、与运营商通话冲突，例如有运营商通话存在时，不能发起应用内通话去电。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

[]()[]()

#### 1007200999 未知错误

**错误信息**

Unknown error code.

**错误描述**

Call Service Kit未知错误。

**可能原因**

未知。

**处理步骤**

请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。