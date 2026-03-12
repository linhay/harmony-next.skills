# textToSpeech（文本转语音）

文本转语音服务提供将文本信息转换为语音并进行播报的能力，便于用户与设备进行互动，实现实时语音交互，文本播报。

目前本服务支持的语种为中文、英文，支持的音色为聆小珊女声音色、英语（美国）劳拉女声音色、凌飞哲男声音色。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';
```

#### textToSpeech.createEngine

createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<TextToSpeechEngine>): void

创建[TextToSpeechEngine](#section185526396124)实例，并初始化引擎。使用callback异步回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

createEngineParams

[CreateEngineParams](#section1638144844811)

是

创建引擎实例的配置项。

callback

[AsyncCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#asynccallback)<[TextToSpeechEngine](#section185526396124)>

是

回调函数。引擎实例的回调。

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

1002300002

The language is not supported.

1002300003

The person is not supported.

1002300005

Create engine failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

// 创建引擎实例相关参数
let ttsEngine: textToSpeech.TextToSpeechEngine;
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
let initParamsInfo: textToSpeech.CreateEngineParams = {
  language: 'zh-CN',
  person: 0,
  online: 1,
  extraParams: extraParam
};
// 调用创建引擎实例接口
textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
  if (!err) {
    console.info('Succeeded in creating engine.');
    // 获得引擎实例
    ttsEngine = textToSpeechEngine;
  } else {
    console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
  }
});

@Entry
@Component
struct Page {

  build() {
  }
}
```

#### textToSpeech.createEngine

createEngine(createEngineParams: CreateEngineParams): Promise<TextToSpeechEngine>

创建[TextToSpeechEngine](#section185526396124)实例，并初始化引擎。使用Promise异步回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

createEngineParams

[CreateEngineParams](#section1638144844811)

是

创建引擎实例的配置项。

**返回值：**

类型

说明

Promise<[TextToSpeechEngine](#section185526396124)>

Promise对象。返回创建的引擎实例。

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

1002300002

The language is not supported.

1002300003

The person is not supported.

1002300005

Create engine failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 创建引擎实例相关参数
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
let initParamsInfo: textToSpeech.CreateEngineParams = {
  language: 'zh-CN',
  person: 0,
  online: 1,
  extraParams: extraParam
};

// 调用createEngine方法
textToSpeech.createEngine(initParamsInfo).then((res: textToSpeech.TextToSpeechEngine) => {
  // 获得引擎实例
  ttsEngine = res;
  console.info(`Succeeded in creating engine.`);
}).catch((err: BusinessError) =>{
  console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
});

@Entry
@Component
struct Page {

  build() {
  }
}
```

#### textToSpeech.listVoices

listVoices(queryParams: VoiceQuery): Promise<VoiceInfo[]>

查询支持的语种音色信息，使用Promise异步回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

queryParams

[VoiceQuery](#section235272615215)

是

查询语种音色信息请求参数。

**返回值：**

类型

说明

Promise<[VoiceInfo](#section85771521101910)[]>

Promise对象，返回查询的结果。

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

// 设置查询相关的参数
let voicesQuery: textToSpeech.VoiceQuery = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  online: 1
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 调用listVoices方法
        textToSpeech.listVoices(voicesQuery).then((res: textToSpeech.VoiceInfo[]) => {
          // 获得目前支持的语种音色等信息
          console.info(`Succeeded in listing voices, result: ${JSON.stringify(res)}.`);
        }).catch((err: BusinessError) =>{
          console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}.`);
        });
      })
  }
}
```

#### textToSpeech.downloadVoice

downloadVoice(downloadParams: VoiceDownload, callback: AsyncCallback<DownloadResponse>): void

下载支持的语种音色。使用callback异步回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**设备行为差异：**该接口在Phone、Tablet设备中可正常调用，在其他设备中调起下载弹窗后点击下载返回1002300008错误码。

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

downloadParams

[VoiceDownload](#section10297014134719)

是

下载语种音色请求参数。

callback

[AsyncCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#asynccallback)<[DownloadResponse](#section037913322072)>

是

回调函数，下载的音色模型及信息。

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

1002300008

Failed to download voice.

1002300009

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1002300010

Voice has already been downloaded.

**示例：**

```ets
import { BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

// 设置下载音色相关参数
let voicesDownload: textToSpeech.VoiceDownload = {
  requestId: '12345678-b', // 请求ID，ID不可重复
  language: 'en-US',
  person: 8,
  style: 'interaction-broadcast'
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick(() => {
        // 调用downloadVoice方法
        textToSpeech.downloadVoice(voicesDownload,
          (error: BusinessError, downloadResponse: textToSpeech.DownloadResponse) => {
            if (error) {
              console.error(`Failed to download voice. code: ${error.code}, message: ${error.message}`);
              return;
            }
            if (!downloadResponse) {
              console.error(`Failed to download voice. downloadResponse is null`);
              return
            }
            let requestId: string = downloadResponse.requestId;

            // 定义函数
            let startCallback: Callback<string> = (info: string) => {
              // 下载开始回调
              console.info(`download voice start, requestId: ${requestId}, info:${info}}`);
            }

            // 定义函数
            let progressCallback: Callback<string> = (schedule: string) => {
              // 下载进度回调
              console.error(`download voice schedule, requestId: ${requestId} scheduleInfo: ${schedule}`);
            }

            // 定义函数
            let completeCallback: Callback<textToSpeech.VoiceInfo> = (voiceInfo: textToSpeech.VoiceInfo) => {
              // 下载完成回调
              console.info(`download voice complete, requestId: ${requestId} voiceInfo: ${JSON.stringify(voiceInfo)}`);
              // 取消下载开始事件回调注册
              downloadResponse.off('start', startCallback);
              // 取消下载进度事件回调注册
              downloadResponse.off('progress',progressCallback);
              // 取消下载完成事件回调注册
              downloadResponse.off('complete',completeCallback);
              // 取消下载取消事件回调注册
              downloadResponse.off('cancel',cancelCallback);
              // 取消下载过程错误事件回调注册
              downloadResponse.off('error',errorCallback);
            }

            // 定义函数
            let cancelCallback: Callback<string> = (cancelInfo: string) => {
              // 用户取消下载回调
              console.error(`download voice cancel, requestId: ${requestId} cancelInfo: ${cancelInfo}`);
            }

            // 定义函数
            let errorCallback: ErrorCallback<BusinessError> = (err: BusinessError) => {
              // 下载过程错误回调
              console.error(`download voice error, requestId: ${requestId} errorCode: ${err.code} errorMessage: ${err.message}`);
            }

            // 注册下载开始事件回调
            downloadResponse.on('start', startCallback);
            // 注册下载进度事件回调
            downloadResponse.on('progress', progressCallback);
            // 注册下载完成事件回调
            downloadResponse.on('complete', completeCallback);
            // 注册下载取消事件回调
            downloadResponse.on('cancel', cancelCallback);
            // 注册下载过程错误事件回调
            downloadResponse.on('error', errorCallback);
          })
      })
  }
}
```

#### TextToSpeechEngine

文本转语音类，用于执行文本转语音过程中的相关操作。在调用TextToSpeechEngine的方法前，需要先通过[createEngine](#section53411946183318)方法创建一个[TextToSpeechEngine](#section185526396124)实例。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

#### listVoices

listVoices(params: VoiceQuery, callback: AsyncCallback<Array<VoiceInfo>>): void

查询支持的语种音色。使用callback异步回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

params

[VoiceQuery](#section235272615215)

是

查询语种音色信息请求参数。

callback

[AsyncCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#asynccallback)<Array<[VoiceInfo](#section85771521101910)>>

是

回调函数，接收返回的查询结果。

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置查询相关参数
let voicesQuery: textToSpeech.VoiceQuery = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  online: 1
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 调用listVoices方法，以callback返回
        ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo[]) => {
          if (!err) {
            // 接收目前支持的语种音色等信息
            console.info(`Succeeded in listing voices, voiceInfo is ${JSON.stringify(voiceInfo)}.`);
          } else {
            console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}.`);
          }
        });
      })
  }
}
```

#### listVoices

listVoices(params: VoiceQuery): Promise<Array<VoiceInfo>>

查询支持的语种音色。使用Promise异步回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

params

[VoiceQuery](#section235272615215)

是

查询语种音色信息请求参数。

**返回值：**

类型

说明

Promise<Array<[VoiceInfo](#section85771521101910)>>

Promise对象，接收返回的查询结果。

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置查询相关的参数
let voicesQuery: textToSpeech.VoiceQuery = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  online: 1
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 调用listVoices方法
        ttsEngine.listVoices(voicesQuery).then((res: textToSpeech.VoiceInfo[]) => {
          // 获得目前支持的语种音色等信息
          console.info(`Succeeded in listing voices, result: ${JSON.stringify(res)}.`);
        }).catch((err: BusinessError) =>{
          console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}.`);
        });
      })
  }
}
```

#### setListener

setListener(listener: SpeakListener): void

设置合成播报回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

listener

[SpeakListener](#section115395631614)

是

合成播报相关事件的回调。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置speak的回调信息
let speakListener: textToSpeech.SpeakListener = {
  // 开始播报回调
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 合成完成及播报完成回调
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 停止播报回调
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 返回音频流
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
  },
  // 错误回调
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 设置回调
        ttsEngine.setListener(speakListener);
      })
  }
}
```

#### speak

speak(text: string, speakParams: SpeakParams): void

合成播报文本。请先调用[setListener](#section143821952181910)方法，否则，无法接收语音的回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

text

string

是

待播报的文本。根据不同场景的实际需求，可主动设置单词发音方式、数字播报策略、指定汉字发音以及在播报时插入静音停顿。具体方式请参考[设置播报策略](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/texttospeech-guide#section137481719163910)。

文本长度不得超过10000字数。

speakParams

[SpeakParams](#section7843122735210)

是

合成播报音频的相关参数。

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

1002300001

The length of text is out of range or empty.

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t" +
  "纸上得来终觉浅，绝知此事要躬行。\n\t\t";

// 合成及播报相关的参数
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 传入文本originalText，调用speak接口
        ttsEngine.speak(originalText, speakParams);
      })
  }
}
```

#### stop

stop(): void

同时停止合成及播报，请先调用[setListener](#section143821952181910)方法，否则无法接收stop的回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t" +
  "纸上得来终觉浅，绝知此事要躬行。\n\t\t";

// 合成及播报相关的参数
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // 传入文本originalText，调用speak接口
          ttsEngine.speak(originalText, speakParams);
        })

      Button()
        .id('Stop')
        .onClick( () => {
          // 调用stop接口
          ttsEngine.stop();
        })
    }
  }
}
```

#### isBusy

isBusy(): boolean

判断引擎当前是否处于合成或播报中。请先调用[setListener](#section143821952181910)方法，否则无法接收isBusy()错误相关的回调。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

服务是否处于合成或播报状态的返回值。

- true：引擎正处于合成或播报状态。
- false：引擎没有处于合成或播报状态。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t" +
  "纸上得来终觉浅，绝知此事要躬行。\n\t\t";

// 合成及播报相关的参数
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // 传入文本originalText，调用speak接口
          ttsEngine.speak(originalText, speakParams);
        })

      Button()
        .id('isBusy')
        .onClick( () => {
          // 调用isBusy接口
          let isBusy = ttsEngine.isBusy();
          console.info(`isBusy: ${isBusy}`);
        })
    }
  }
}
```

#### shutdown

shutdown(): void

关闭引擎，释放引擎资源。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t" +
  "纸上得来终觉浅，绝知此事要躬行。\n\t\t";

// 合成及播报相关的参数
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // 传入文本originalText，调用speak接口
          ttsEngine.speak(originalText, speakParams);
        })

      Button()
        .id('shutdown')
        .onClick( () => {
          // 调用shutdown接口
          ttsEngine.shutdown();
        })
    }
  }
}
```

#### SpeakListener

合成及播报的回调对象，通过此对象可返回合成及播报过程的相关状态，例如开始合成及播报、合成完成、播报完成、停止播报完成等。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

#### onStart

onStart(requestId: string, response: StartResponse): void

播报开始时，回调此接口，返回请求ID、播报相关参数，例如通道数、采样率、采样位数信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

requestId

string

是

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

response

[StartResponse](#section270311282525)

是

播报相关参数。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置speak的回调信息
let speakListener: textToSpeech.SpeakListener = {
  // 开始播报回调
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 合成完成及播报完成回调
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 停止播报回调
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 返回音频流
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
  },
  // 错误回调
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 设置回调
        ttsEngine.setListener(speakListener);
      })
  }
}
```

#### onStop

onStop(requestId: string, response: StopResponse): void

调用stop()方法时，回调此接口，表示stop已完成。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

requestId

string

是

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

response

[StopResponse](#section892952965214)

是

响应停止事件的相关信息。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置speak的回调信息
let speakListener: textToSpeech.SpeakListener = {
  // 开始播报回调
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 合成完成及播报完成回调
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 停止播报回调
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 返回音频流
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
  },
  // 错误回调
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 设置回调
        ttsEngine.setListener(speakListener);
      })
  }
}
```

#### onComplete

onComplete(requestId: string, response: CompleteResponse): void

合成或播报结束后分别回调此接口，返回请求ID，完成播报相关信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

requestId

string

是

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

response

[CompleteResponse](#section26265304523)

是

完成播报相关信息。

onData 可能并未返回完毕，请继续接收 onData 回调。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置speak的回调信息
let speakListener: textToSpeech.SpeakListener = {
  // 开始播报回调
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 合成完成及播报完成回调
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 停止播报回调
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 返回音频流
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
  },
  // 错误回调
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 设置回调
        ttsEngine.setListener(speakListener);
      })
  }
}
```

#### onData

onData?: OnDataCallback

合成播报过程中回调此接口，返回请求ID，音频流信息，音频附加信息如格式、时长等。若需要返回音频流信息，请实现此接口。

因为异步ipc会导致onData音频流顺序小规模错乱，需要调用方在播放前对音频流按照sequence排序。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

onData

[OnDataCallback](#section0818167184314)

否

合成的回调，通过音频的参数返回音频数据。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置speak的回调信息
let speakListener: textToSpeech.SpeakListener = {
  // 开始播报回调
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 合成完成及播报完成回调
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 停止播报回调
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 返回音频流
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
  },
  // 错误回调
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 设置回调
        ttsEngine.setListener(speakListener);
      })
  }
}
```

#### onError

onError(requestId: string, errorCode: number, errorMessage: string): void

合成播报过程中，出现错误时回调，返回请求ID、错误码及错误描述。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

requestId

string

是

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

errorCode

number

是

[错误码](ArkTS API错误码.md)。

errorMessage

string

是

错误信息描述。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// 设置speak的回调信息
let speakListener: textToSpeech.SpeakListener = {
  // 开始播报回调
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 合成完成及播报完成回调
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 停止播报回调
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
  },
  // 返回音频流
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
  },
  // 错误回调
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // 设置回调
        ttsEngine.setListener(speakListener);
      })
  }
}
```

#### OnDataCallback

type OnDataCallback = (requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void

合成的回调，通过音频的参数返回音频数据。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

requestId

string

是

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

audio

ArrayBuffer

是

音频流。

response

[SynthesisResponse](#section8985194614315)

是

返回的音频流相关信息。

#### CreateEngineParams

创建引擎实例的相关参数，用于配置语种、模式、音色和风格等。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

language

string

否

否

语种，当前支持中文、英文。

中文推荐使用“zh-CN”格式，兼容“zh_CN”格式。

英文推荐使用“en-US”格式，兼容“en_US”格式。

online

number

否

否

模式。

0为在线，目前不支持；1为离线，当前仅支持离线模式。

person

number

否

否

音色。

中文：13为聆小珊女声音色（推荐使用13，同时支持0）；21为凌飞哲男声音色（需下载）。

英文：8为英语（美国）劳拉女声音色（需下载）。

extraParams

Record<string, Object>

否

是

- <'style', string> 风格。

可选，不设置时默认为“interaction-broadcast”，当前仅支持“interaction-broadcast”。

interaction-broadcast：广播风格。

- <'locate', string> 区域信息。

可选，不设置时默认为“CN”，当前仅支持“CN”。

CN:中国。

- <'name', string> 引擎名称。

可选，引擎名称，不可以是随机数，不设置时默认为空，当前支持多应用、多实例，同一个设备上所有应用一共最多支持3个实例。

- <'isBackStage', boolean> 是否支持后台播报。

可选，不设置时默认不支持后台播报。设置'isBackStage': true时，TTS支持后台播报。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

// 设置创建引擎参数
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName','isBackStage': true};
let initParamsInfo: textToSpeech.CreateEngineParams = {
  language: 'zh-CN',
  person: 0,
  online: 1,
  extraParams: extraParam
};

@Entry
@Component
struct Page {

  build() {
  }
}
```

#### VoiceQuery

查询音色语种信息的相关参数。例如查询离线模式、中文语种所支持的音色信息，需将online参数设置为1，language参数设置为“zh-CN”。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

requestId

string

否

否

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

online

number

否

否

模式。

0为在线，目前不支持；1为离线，当前仅支持离线。

extraParams

Record<string, Object>

否

是

- <'language', string> 查询的语种。

可选，当前支持“zh-CN”中文，“en-US”英文。不填时查询全量列表。

- <'person', number> 查询的音色。

可选，非空时则language必填。不填时查询全量列表。

中文支持：

13. 聆小珊女声音色（推荐使用13，同时支持0）；

21. 凌飞哲男声音色（需下载）。

英文支持：

8. 英语（美国）劳拉女声音色（需下载）。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

// 设置创建引擎参数
let extraParam: Record<string, Object> = {"language": 'zh-CN', "person": 0};
let voiceQuery: textToSpeech.VoiceQuery= {
  requestId: '12345678', // requestId在同一实例内仅能用一次，请勿重复设置
  online: 1,
  extraParams: extraParam
};

@Entry
@Component
struct Page {

  build() {
  }
}
```

#### VoiceDownload

下载音色时的相关参数，所有参数通过listVoices接口获取。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

名称

类型

只读

可选

说明

requestId

string

否

否

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

language

string

否

否

支持下载的语种，有效范围通过[listVoices（Callback异步回调）](#section813761871119)和[listVoices（Promise异步回调）](#section125219451411)获取。

person

number

否

否

支持下载的音色，有效范围通过[listVoices（Callback异步回调）](#section813761871119)和[listVoices（Promise异步回调）](#section125219451411)获取。

style

string

否

否

支持下载的音色风格，有效范围通过[listVoices（Callback异步回调）](#section813761871119)和[listVoices（Promise异步回调）](#section125219451411)获取。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

// 设置下载音色相关参数
let voicesDownload: textToSpeech.VoiceDownload = {
  requestId: '12345678-b', // 请求ID，ID不可重复
  language: 'en-US',
  person: 8,
  style: 'interaction-broadcast'
};
```

#### DownloadResponse

下载音色语种时的回调对象。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

名称

类型

只读

可选

说明

requestId

string

否

否

请求ID。唯一标识一条请求。

支持英文字符，数字和中文，长度不限制。

#### on('start')

on(type: 'start', callback: Callback<string>): void

音色下载开始时，触发此接口，接收下载开始信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“start”。监听音色下载开始事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<string>

是

callback回调，接收下载开始信息。

**示例：**

```ets
// 定义函数
let startCallback: Callback<string> = (info: string) => {
  // 开始下载回调
  console.info(`download voice start, info:${info}}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载开始事件回调
downloadResponse.on('start', startCallback);
// 取消下载开始事件回调注册
downloadResponse.off('start', startCallback);
```

#### on('progress')

on(type: 'progress', callback: Callback<string>): void

音色下载过程中，触发此接口，接收下载进度信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“progress”。监听音色下载进度事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<string>

是

callback回调，接收下载进度信息。

**示例：**

```ets
// 定义函数
let progressCallback: Callback<string> = (schedule: string) => {
  // 下载进度回调
  console.error(`download voice schedule, scheduleInfo: ${schedule}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载进度事件回调
downloadResponse.on('progress', progressCallback);
// 取消下载进度事件回调注册
downloadResponse.off('progress',progressCallback);
```

#### on('complete')

on(type: 'complete', callback: Callback<VoiceInfo>): void

音色下载完成时，触发此接口，接收下载完成音色信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“complete”。监听音色下载完成事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<[VoiceInfo](#section85771521101910)>

是

callback回调，接收下载完成的音色信息。

**示例：**

```ets
// 定义函数
let completeCallback: Callback<textToSpeech.VoiceInfo> = (voiceInfo: textToSpeech.VoiceInfo) => {
  // 下载完成回调
  console.info(`download voice complete, voiceInfo: ${JSON.stringify(voiceInfo)}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载完成事件回调
downloadResponse.on('complete', completeCallback);
// 取消下载完成事件回调注册
downloadResponse.off('complete',completeCallback);
```

#### on('cancel')

on(type: 'cancel', callback: Callback<string>): void

用户点击进度框上关闭按钮，取消下载时，触发此接口，接收取消下载信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“cancel”。监听用户取消音色下载事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<string>

是

callback回调，接收用户取消下载信息。

点击下载同意弹窗上的“取消”按钮不会触发此回调。

**示例：**

```ets
// 定义函数
let cancelCallback: Callback<string> = (cancelInfo: string) => {
  // 用户取消下载回调
  console.error(`download voice cancel, cancelInfo: ${cancelInfo}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载取消事件回调
downloadResponse.on('cancel', cancelCallback);
// 取消下载取消事件回调注册
downloadResponse.off('cancel',cancelCallback);
```

#### on('error')

on(type: 'error', callback: ErrorCallback<BusinessError>): void

音色下载错误时，触发此接口，接收下载错误信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“error”。监听音色下载出错事件。

callback

[ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback)<[BusinessError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#businesserror)>

是

callback回调，接收下载错误信息。

**示例：**

```ets
// 定义函数
let errorCallback: ErrorCallback<BusinessError> = (err: BusinessError) => {
  // 下载过程错误回调
  console.error(`download voice error, errorCode: ${err.code} errorMessage: ${err.message}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载过程出错事件回调
downloadResponse.on('error', errorCallback);
// 取消下载过程出错事件回调注册
downloadResponse.off('error',errorCallback);
```

#### off('start')

off(type: 'start', callback?: Callback<string>): void

取消监听音色下载开始事件。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“start”。取消监听下载开始事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<string>

否

需要取消注册的回调函数，需与监听时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**示例：**

```ets
// 定义函数
let startCallback: Callback<string> = (info: string) => {
  // 开始下载回调
  console.info(`download voice start, info:${info}}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载开始事件回调
downloadResponse.on('start', startCallback);
// 取消下载开始事件回调注册
downloadResponse.off('start', startCallback);
```

#### off('progress')

off(type: 'progress', callback?: Callback<string>): void

取消监听音色下载过程事件。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“progress”。取消监听下载过程事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<string>

否

需要取消注册的回调函数，需与监听时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**示例：**

```ets
// 定义函数
let progressCallback: Callback<string> = (schedule: string) => {
  // 下载进度回调
  console.error(`download voice schedule, scheduleInfo: ${schedule}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载进度事件回调
downloadResponse.on('progress', progressCallback);
// 取消下载进度事件回调注册
downloadResponse.off('progress',progressCallback);
```

#### off('complete')

off(type: 'complete', callback?: Callback<VoiceInfo>): void

取消监听音色下载完成事件。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“complete”。取消监听下载完成事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<[VoiceInfo](#section85771521101910)>

否

需要取消注册的回调函数，需与监听时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**示例：**

```ets
// 定义函数
let completeCallback: Callback<textToSpeech.VoiceInfo> = (voiceInfo: textToSpeech.VoiceInfo) => {
  // 下载完成回调
  console.info(`download voice complete, voiceInfo: ${JSON.stringify(voiceInfo)}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载完成事件回调
downloadResponse.on('complete', completeCallback);
// 取消下载完成事件回调注册
downloadResponse.off('complete',completeCallback);
```

#### off('cancel')

off(type: 'cancel', callback?: Callback<string>): void

取消监听音色下载取消事件。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“cancel”。取消监听下载取消事件。

callback

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)<string>

否

需要取消注册的回调函数，需与监听时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**示例：**

```ets
// 定义函数
let cancelCallback: Callback<string> = (cancelInfo: string) => {
  // 用户取消下载回调
  console.error(`download voice cancel, cancelInfo: ${cancelInfo}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载取消事件回调
downloadResponse.on('cancel', cancelCallback);
// 取消下载取消事件回调注册
downloadResponse.off('cancel',cancelCallback);
```

#### off('error')

off(type: 'error', callback?: ErrorCallback<BusinessError>): void

取消监听音色下载错误事件。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定字符串“error”。取消监听下载错误事件。

callback

[ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback)<[BusinessError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#businesserror)>

否

需要取消注册的回调函数，需与监听时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**示例：**

```ets
// 定义函数
let errorCallback: ErrorCallback<BusinessError> = (err: BusinessError) => {
  // 下载过程错误回调
  console.error(`download voice error, errorCode: ${err.code} errorMessage: ${err.message}`);
}
// downloadResponse由接口[textToSpeech.downloadVoice](#section376811290229)中获取
// 注册下载过程出错事件回调
downloadResponse.on('error', errorCallback);
// 取消下载过程出错事件回调注册
downloadResponse.off('error',errorCallback);
```

#### SpeakParams

合成播报音频流的相关参数，用于配置语速、音量、音调、合成类型等。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

requestId

string

否

否

合成播报ID，全局不允许重复。

支持英文字符，数字和中文，此字段用于区分不同请求，长度不限制。

extraParams

Record<string, Object>

否

是

- <'speed', number> 语速。

可选，支持范围[0.5-2]，不传参时默认为1，使用一倍语速合成音频流。

- <'volume', number> 音量。

可选，支持范围[0-2]，不传参时默认为1，使用一倍音量合成音频流。

- <'pitch', number> 音调。

可选，支持范围[0.5-2]，不传参时默认为1，使用正常音调合成音频流。

- <'languageContext', string> 语境，播放阿拉伯数字用的语种。

可选，当前支持“zh-CN”中文与“en-US”英文，不传参时默认“zh-CN”。

- <'audioType', string> 音频类型。

可选，当前仅支持“pcm”，不传参时默认为“pcm”（PCM 即脉冲编码调制 (Pulse Code Modulation)）。

- <'playType', number> 合成类型。

可选，不传参时默认为1。

0：仅合成不播报，返回音频流。

1：合成与播报不返回音频流。

- <'soundChannel', number> 播报通道。

可选，参数范围请参考[音频流使用](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#streamusage)来选择适合自己的音频场景，范围之外会播报异常。

不传参时默认为3，语音助手通道。

 说明：

如果使用了通道1或12，设备息屏场景下，会出现播报截断的问题，原因是进入了音频的[低功耗模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/power-saving-for-playback)。

- <'queueMode', number> 播报模式。

可选，不传参时默认为0。

0：排队模式播报。

1：抢占模式播报。

**示例：**

```ets
import { textToSpeech } from '@kit.CoreSpeechKit';

// 设置播报相关参数
let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm", "soundChannel": 3, "playType":1};
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
  extraParams: extraParam
}

@Entry
@Component
struct Page {

  build() {
  }
}
```

#### VoiceInfo

返回查询的相关参数。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

language

string

否

否

支持的语种信息。当前支持中文、英文。

中文推荐使用“zh-CN”格式，兼容“zh_CN”格式。

英文推荐使用“en-US”格式，兼容“en_US”格式。

person

number

否

否

支持的音色信息。

中文：13为聆小珊女声音色（推荐使用13，同时支持0）；21为凌飞哲男声音色（需下载）。

英文：8为英语（美国）劳拉女声音色（需下载）。

style

string

否

否

风格。

- interaction-broadcast：普通话播报。

gender

string

否

否

性别。

- Male：男性。
- Female：女性。

description

string

否

否

语音的描述，角色属性、支持的情感等说明。

status

string

否

是

音色模型状态。

- 'GA'：音色可下载。
- 'INSTALLED'：音色已下载。
- 'EOM'：音色不可用。

**起始版本：**5.1.1(19)

#### StartResponse

返回播放的相关参数。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

audioType

string

否

否

音频类型，当前仅支持“pcm”（PCM 即脉冲编码调制（Pulse Code Modulation））。

sampleRate

number

否

否

音频返回的采样率信息。当前仅支持16000采样率。

sampleBit

number

否

否

音频返回的采样位数。当前仅支持16位。

audioChannel

number

否

否

音频返回的通道数信息。取决于输入通道信息。

compressRate

number

否

否

pcm格式默认为0（PCM 即脉冲编码调制（Pulse Code Modulation））。

#### StopResponse

返回停止播报时的相关参数。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

type

number

否

否

代表结束的类型。

- 0：同时结束合成和播报。
- 1：只结束播报。

message

string

否

否

返回信息说明。

字符长度范围[0, 30]。

#### CompleteResponse

返回完成播报时的相关参数。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

type

number

否

否

代表合成或播报结束。

- 0：合成结束。
- 1：播报结束。

message

string

否

否

返回信息说明。

字符长度范围[0, 30]。

#### SynthesisResponse

返回的音频流相关信息。

**系统能力：**SystemCapability.AI.TextToSpeech

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

sequence

number

否

否

代表返回的音频数据的次序。

从0开始，每次加1。

取值范围[0, 100000]。

audioType

string

否

否

返回的音频数据类型，当前仅支持‘pcm’类型（PCM 即脉冲编码调制 (Pulse Code Modulation)）。