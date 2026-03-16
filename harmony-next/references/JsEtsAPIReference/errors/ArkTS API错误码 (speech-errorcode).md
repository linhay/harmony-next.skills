[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 201 权限校验失败

**错误信息**

Permission denied.

**错误描述**

权限校验失败。

**可能原因**

开发者未配置ohos.permission.KEEP_BACKGROUND_RUNNING的后台运行权限。

**处理步骤**

配置相关权限后再尝试运行。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 401 参数检查失败

**错误信息**

Parameter error.

**错误描述**

参数检查错误。

**可能原因**

参数检查失败，包括必选参数没有传入，参数类型错误。

**处理步骤**

检查是否传入必选参数以及参数类型是否正确。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600011 初始化失败

**错误信息**

Initialize failed.

**错误描述**

TextReader初始化失败。

**可能原因**

1. 可能是TTS引擎侧或播放器侧初始化失败。
1. 部分机型暂不支持。

**处理步骤**

1. 检查是否已初始化，再次调用初始化会出现此错误。
1. 在初始化前设置好windowStage。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600012 未初始化

**错误信息**

The TextReader is not initialized.

**错误描述**

未初始化。

**可能原因**

未初始化TextReader调用起播时触发。

**处理步骤**

需要首先调用[init](../topics/graphics/TextReader（朗读控件）.md#section173751154134515)方法初始化TextReader。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600013 TTS音频合成错误

**错误信息**

Text-to-speech engine error.

**错误描述**

TTS音频合成错误。

**可能原因**

TTS引擎侧合成音频异常。

**处理步骤**

建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600014 播放器错误

**错误信息**

AudioRenderer play error.

**错误描述**

播放器错误。

**可能原因**

AudioRenderer播放器播放异常。

**处理步骤**

检查readInfoList参数的格式以及内容是否正确。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600015 解码错误

**错误信息**

Audio decode error.

**错误描述**

解码错误。

**可能原因**

TTS引擎侧音频解码失败。

**处理步骤**

建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600016 播控中心同步错误

**错误信息**

AVSession error.

**错误描述**

播控中心同步错误。

**可能原因**

AVSession播控中心同步封面图片或播放状态错误。

**处理步骤**

建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600017 其他错误

**错误信息**

Other error.

**错误描述**

其他错误。

**可能原因**

其他原因造成的异常。

**处理步骤**

建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600018 播放前一首失败

**错误信息**

playPrev failed.

**错误描述**

播放前一首失败。

**可能原因**

数据异常等。

**处理步骤**

检查上一首对应的readInfo参数内容是否正确。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600019 播放后一首失败

**错误信息**

playNext failed.

**错误描述**

播放后一首失败。

**可能原因**

数据异常等。

**处理步骤**

检查下一首对应的readInfo参数内容是否正确。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1010600020 释放异常

**错误信息**

Release error.

**错误描述**

TextReader释放失败。

**可能原因**

可能是资源释放异常等原因造成的异常。

**处理步骤**

设置延时后再次调用release接口。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1012900010 AI字幕服务忙

**错误信息**

AI caption service is busy.

**错误描述**

AI字幕服务忙。

**可能原因**

AI字幕服务忙造成的异常。

**处理步骤**

建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1012900011 AI字幕控制器初始化失败

**错误信息**

AI caption controller initialized failed.

**错误描述**

AI字幕控制器初始化失败。

**可能原因**

AI字幕控制器初始化失败造成的异常。

**处理步骤**

排查是否有其他应用正在使用字幕应用。

建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1012900012 音频识别失败

**错误信息**

Audio recognition failed.

**错误描述**

音频识别失败。

**可能原因**

AI字幕音频识别失败造成的异常。

**处理步骤**

1. 检查传入的音频的字节长度是否小于640或者大于1280。
1. 检查AI引擎是否初始化成功。

如果解决不了，建议[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)。