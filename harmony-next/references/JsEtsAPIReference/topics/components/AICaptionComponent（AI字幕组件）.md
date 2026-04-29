# AICaptionComponent（AI字幕组件）

AI字幕控件使用AI能力将语音实时转化成文本并翻译，提供原文、译文的展示。适用于一些音乐类、视频类等音视频内容App，帮助用户在一些无法直接浏览音频内容或者对音频源语言不熟悉的场景下，通过字幕来高效获取信息。

起始版本： 5.0.0(12)

**导入模块**

```ets
import {
  AICaptionComponent, AudioInfo, AudioData, AICaptionOptions, AICaptionController
} from "@kit.SpeechKit";
```

**AICaptionComponent**

AI字幕组件，可以作为动态组件加载。

装饰器类型： @Component

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

参数：

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| isShown | boolean | 是 | @Link | 字幕显示状态。 true：显示，从5.1.0(18)开始支持自动识别应用音频生成字幕。 false：隐藏。 |
| controller | AICaptionController | 是 | - | 字幕控制器。 |
| options | AICaptionOptions | 是 | - | 字幕初始化参数。 |

**build**

build(): void

用于创建对象[AICaptionComponent](#ZH-CN_TOPIC_0000002553362523__aicaptioncomponent)的构造函数。

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

示例：

```ets
import { AICaptionComponent, AICaptionController, AICaptionOptions } from '@kit.SpeechKit';

@Entry
@Component
struct Index {
  private captionOption?: AICaptionOptions;
  private controller = new AICaptionController();
  @State isShow: boolean = false;

  aboutToAppear(): void {
    this.captionOption = {
      initialOpacity: 1,
      onPrepared: () => {
        // ...
      },
      onError: () => {
        // ...
      }

  build() {
    Column() {
      // 调用AICaptionComponent组件初始化字幕
      AICaptionComponent({
        isShown: this.isShow,
        controller: this.controller,
        options: this.captionOption
      })
    }
```

**AICaptionController**

AI字幕控件的主要功能入口类。

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

示例：

```ets
import { AICaptionComponent, AICaptionOptions, AICaptionController } from '@kit.SpeechKit';

@Entry
@Component
struct Index {
  private options?: AICaptionOptions;
  private controller = new AICaptionController();
  @State isShown: boolean = false;

  aboutToAppear(): void {
    this.options = {
      initialOpacity: 1,
      onPrepared: () => {
        // ...
      },
      onError: () => {
        // ...
      }

  build() {
    Column() {
      // 调用AICaptionComponent组件初始化字幕
      AICaptionComponent({
        isShown: this.isShown,
        controller: this.controller,
        options: this.options
      })
    }
```

**getAudioInfo**

getAudioInfo(): AudioInfo

获取要被识别的音频信息。

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| AudioInfo | 获取当前版本字幕支持的音频信息。 |

示例：

```ets
import { AICaptionController, AudioInfo } from '@kit.SpeechKit';

try {
  let controller = new AICaptionController();
  let audioInfo: AudioInfo = controller.getAudioInfo();
} catch (e) {
  console.error(`GetAudioInfo failed. Code: ${e.code}, message: ${e.message}`);
}
```

**writeAudio**

writeAudio(audioData: AudioData): void

写入音频数据。音频流信息格式从[getAudioInfo](#ZH-CN_TOPIC_0000002553362523__getaudioinfo)方法获取（调用此方法会停止自动获取应用音频生成字幕，以写入的音频流为准）。

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| audioData | AudioData | 是 | 音频数据。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1012900012 | Audio recognition failed. |

示例：

```ets
import { AICaptionController } from '@kit.SpeechKit';
import { AudioData } from '@kit.SpeechKit';

let audioData: AudioData = {
  data: new Uint8Array()
}
try {
  let controller = new AICaptionController();
  controller.writeAudio(audioData)
} catch (e) {
  console.error(`WriteAudio failed. Code: ${e.code}, message: ${e.message}`);
}
```

**AudioInfo**

音频流信息。

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioType | string | 否 | 否 | 音频类型。 当前仅支持 "pcm"编码。 |
| sampleRate | audio.AudioSamplingRate | 否 | 否 | 音频采样率。 当前仅支持16000采样率。 |
| soundChannel | audio.AudioChannel | 否 | 否 | 音频声道。 当前仅支持1个通道。 |
| sampleBit | number | 否 | 否 | 音频采样字节。 当前仅支持16位。 |

**AudioData**

音频数据。

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 音频数据。 当前仅支持音频数据长度为640字节或1280字节。 建议每次发送音频调用间隔为20ms（传输音频长度为640字节）或40ms（传输音频长度为1280字节）。 |

**AICaptionOptions**

字幕初始化选项。

系统能力： SystemCapability.AI.AICaption

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialOpacity | number | 否 | 是 | 字幕精简态下面板背景的不透明度。 - Phone和tablet的取值范围：[0，1]，1表示不透明，0表示完全透明，达到隐藏组件效果，但是在布局中占位，默认值：0。 - 2in1有全透明：0 、半透明：0.5 、不透明：1三个选项，默认值：全透明：0。 |
| onPrepared | Callback<void> | 否 | 否 | 监听控件初始化完成的回调函数。 |
| onError | ErrorCallback | 否 | 否 | 监听控件错误的回调函数。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1012900010 | AI caption service is busy. |
| 1012900011 | AI caption controller initialized failed. |