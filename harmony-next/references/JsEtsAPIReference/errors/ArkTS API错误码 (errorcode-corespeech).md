[]()[]()

# ArkTS API错误码

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

[]()[]()

#### 1002200001 创建引擎失败

**错误信息**

Create engine failed.

**错误描述**

创建引擎失败。

**可能原因**

1. 语种不支持。
1. 模式不支持。
1. 资源不存在或初始化超时。

**处理步骤**

1. 调用[listLanguages](../topics/misc/speechRecognizer（语音识别）.md#section813761871119)方法查询支持的语种，确认语种后请重新尝试。
1. 当前仅支持[CreateEngineParams](../topics/misc/speechRecognizer（语音识别）.md#section1638144844811)，确认模式后请重新尝试。
1. 资源不存在及初始化超时时，建议稍后重新尝试。

[]()[]()

#### 1002200002 开始识别失败

**错误信息**

Start listening failed.

**错误描述**

开始识别失败。

**可能原因**

已启动语音识别，重复启动时触发。

**处理步骤**

检测语音识别是否已经启动，不要重复启动。

[]()[]()

#### 1002200003 超过最大音频

**错误信息**

Exceeded the maximum audio length supported.

**错误描述**

超过支持的最大音频长度。

**可能原因**

超过支持的最大音频长度。

**处理步骤**

建议音频长度不要超过60000ms，重新尝试。

[]()[]()

#### 1002200004 结束识别失败

**错误信息**

Finish recognition failed.

**错误描述**

结束识别失败。

**可能原因**

当前没有正在识别的任务。

**处理步骤**

调用[startListening](../topics/misc/speechRecognizer（语音识别）.md#section140216144119)方法先启动语音识别任务，重新尝试。

[]()[]()

#### 1002200005 取消识别失败

**错误信息**

Cancel recognition failed.

**错误描述**

取消识别失败。

**可能原因**

当前没有正在识别的任务。

**处理步骤**

调用[startListening](../topics/misc/speechRecognizer（语音识别）.md#section140216144119)方法先启动语音识别任务，重新尝试。

[]()[]()

#### 1002200006 服务忙碌

**错误信息**

The engine of SpeechRecognition is busy.

**错误描述**

识别服务忙碌。

**可能原因**

引擎正在识别中。

**处理步骤**

调用[isBusy](../topics/misc/speechRecognizer（语音识别）.md#section35361720111113)方法查询服务状态，建议服务空闲时重新尝试。

[]()[]()

#### 1002200007 引擎未初始化

**错误信息**

The engine is not initialized.

**错误描述**

引擎未初始化。

**可能原因**

引擎未初始化。

**处理步骤**

调用[speechRecognizer.createEngine](../topics/misc/speechRecognizer（语音识别）.md#section53411946183318)方法先初始化引擎，重新尝试。

[]()[]()

#### 1002200008 引擎已被销毁

**错误信息**

The engine of SpeechRecognition is being destroyed.

**错误描述**

引擎已被销毁。

**可能原因**

引擎已被销毁。

**处理步骤**

调用[speechRecognizer.createEngine](../topics/misc/speechRecognizer（语音识别）.md#section53411946183318)方法先初始化引擎，重新尝试。

[]()[]()

#### 1002200009 内部服务错误

**错误信息**

Internal Service Error.

**错误描述**

内部服务错误。

**可能原因**

内部服务错误原因导致无法调用引擎功能。

**处理步骤**

根据具体错误信息情况处理。

如果无法解决，建议在线提单，详细步骤请见[在线提单指导](https://developer.huawei.com/consumer/cn/support/feedback/#/)。

[]()[]()

#### 1002200010 语音识别未启动

**错误信息**

Write audio failed because the start listening is failed.

**错误描述**

引擎未启动识别。

**可能原因**

引擎未启动识别。

**处理步骤**

调用[startListening](../topics/misc/speechRecognizer（语音识别）.md#section140216144119)方法先启动语音识别任务，重新尝试。

[]()[]()

#### 1002200011 语音识别异常

**错误信息**

Error in recognition.

**错误描述**

引擎识别中出现异常。

**可能原因**

引擎识别中出现异常。

**处理步骤**

调用[startListening](../topics/misc/speechRecognizer（语音识别）.md#section140216144119)方法重试。

[]()[]()

#### 1002200012 没有获取麦克风权限

**错误信息**

AudioCapturer create failed, please check the permission of MICROPHONE.

**错误描述**

创建[AudioCapturer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiocapturer)失败，请检查麦克风的权限。

**可能原因**

没有获取麦克风权限。

**处理步骤**

检查麦克风权限是否可以获取。

[]()[]()

#### 1002300001 文本长度非法

**错误信息**

The length of text is out of range or empty.

**错误描述**

文本长度非法。

**可能原因**

文本长度为0或超出范围，建议文本不要超过10000字。

**处理步骤**

修改文本，重新尝试。

[]()[]()

#### 1002300002 语言不支持

**错误信息**

The language is not supported.

**错误描述**

语言不支持。

**可能原因**

使用不支持的语言类型。

**处理步骤**

调用[listVoices](../topics/graphics/textToSpeech（文本转语音）.md#section125219451411)接口查询当前支持的语言信息，重新尝试。

[]()[]()

#### 1002300003 音色不支持

**错误信息**

The person is not supported.

**错误描述**

音色不支持。

**可能原因**

使用不支持的音色。

**处理步骤**

调用[listVoices](../topics/graphics/textToSpeech（文本转语音）.md#section125219451411)接口查询当前支持的音色信息，重新尝试。

[]()[]()

#### 1002300005 创建引擎失败

**错误信息**

Create engine failed.

**错误描述**

创建引擎失败。

**可能原因**

1.引擎服务异常。

2.引擎资源加载异常。

**处理步骤**

建议稍后尝试。

[]()[]()

#### 1002300008 下载音色错误

**错误信息**

Failed to download voice.

**错误描述**

文本转语音下载音色接口出错。

**可能原因**

没有网络或因内部服务错误导致的下载异常。

**处理步骤**

运行失败，建议再次尝试。

[]()[]()

#### 1002300009 下载参数错误

**错误信息**

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

**错误描述**

文本转语音下载接口传参错误。

**可能原因**

未按照要求传参。

**处理步骤**

检查输入参数是否符合要求，确保无误后再次尝试。

[]()[]()

#### 1002300010 音色已经下载过

**错误信息**

Voice has already been downloaded.

**错误描述**

文本转语音音色已下载过。

**可能原因**

重复下载已下载过音色。

**处理步骤**

通过查询接口查看哪些音色未下载。