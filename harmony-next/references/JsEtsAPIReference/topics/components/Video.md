# Video

用于播放视频文件并控制其播放状态的组件。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

Video组件只提供简单的视频播放功能，无法支撑复杂的视频播控场景。复杂开发场景推荐使用[AVPlayer](Interface (AVPlayer).md)播控API和[XComponent](XComponent.md)组件开发。

Video组件在使用expandSafeArea扩展安全区域时，组件视频显示内容区域不支持扩展。

**权限列表**

使用网络视频时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../../guides/声明权限.md)。

**子组件**

不支持子组件。

**接口**

**Video**

Video(value: VideoOptions)

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | VideoOptions | 是 | 视频信息。 |

**VideoOptions对象说明**

定义Video的具体配置参数。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | string | Resource | 否 | 是 | 视频的数据源，支持本地视频和网络视频。 Resource格式可以跨包/跨模块访问资源文件，常用于访问本地视频。 - 仅支持rawfile文件下的资源，即通过$rawfile引用视频文件。 string格式可用于加载网络视频和本地视频，常用于加载网络视频。 - 支持网络视频地址。 - 支持file://路径前缀的字符串，即应用沙箱URI：file://<bundleName>/<sandboxPath>。用于读取应用沙箱路径内的资源。需要保证目录包路径下的文件有可读权限。 默认值：空字符串 异常值：按默认值处理。 说明： 视频支持的格式是：mp4、mkv、TS。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| currentProgressRate | number | string | PlaybackSpeed8+ | 否 | 是 | 视频播放倍速。 说明： number格式取值仅支持：0.75，1.0，1.25，1.75，2.0。从API version 22开始，新增支持取值0.5，1.5，3，0.25和0.125。 string格式支持number格式取值的字符串形式："0.75"，"1.0"，"1.25"，"1.75"，"2.0"。从API version 22开始，新增支持取值"0.5"，"1.5"，"3"，"0.25"和"0.125"。 除此之外的取值，比如"abc"或"1.5+1.5"会按照异常值处理。 默认值：1.0 | PlaybackSpeed.Speed_Forward_1_00_X 异常值：按默认值处理。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| previewUri | string | PixelMap | Resource | 否 | 是 | 视频未播放时的预览图片路径，默认不显示图片。 string格式可用于加载本地图片和网络图片， - 支持网络图片地址。 - 支持相对路径引用本地图片，例如：previewUri: “common/test.jpg”。当使用相对路径引用本地图片时，不支持跨包/跨模块调用。 - 支持file://路径前缀的字符串，即应用沙箱URI：file://<bundleName>/<sandboxPath>。用于读取应用沙箱路径内的资源。需要保证目录包路径下的文件有可读权限。 Resource格式可以跨包/跨模块访问资源文件。 - 支持rawfile文件下的资源，即通过$rawfile引用图片。 - 支持通过$r引用系统资源或者应用资源中的图片。 默认值：空字符串 异常值：按默认值处理。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| controller | VideoController | 否 | 是 | 设置视频控制器，可以控制视频的播放状态。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| imageAIOptions12+ | ImageAIOptions | 否 | 是 | 设置图像AI分析选项，可配置分析类型或绑定一个分析控制器。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| posterOptions18+ | PosterOptions | 否 | 是 | 设置视频播放的首帧送显选项，可以控制视频是否支持首帧送显。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

**PlaybackSpeed8+枚举说明**

视频播放倍速选项。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Speed_Forward_0_75_X | 0.75 | 0.75倍速播放。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Speed_Forward_1_00_X | 1 | 1倍速播放。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Speed_Forward_1_25_X | 1.25 | 1.25倍速播放。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Speed_Forward_1_75_X | 1.75 | 1.75倍速播放。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| Speed_Forward_2_00_X | 2 | 2倍速播放。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| SPEED_FORWARD_0_50_X22+ | 0.5 | 0.5倍速播放。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED_FORWARD_1_50_X22+ | 1.5 | 1.5倍速播放。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED_FORWARD_3_00_X22+ | 3 | 3倍速播放。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED_FORWARD_0_25_X22+ | 0.25 | 0.25倍速播放。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED_FORWARD_0_125_X22+ | 0.125 | 0.125倍速播放。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

**muted**

muted(value: boolean)

设置视频是否静音，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 视频是否静音。 true：开启静音；false：关闭静音。 默认值：false |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

Video组件在未设置静音的情况下，启播瞬间会抢占音频焦点。若用户想设置静音播放不抢占其他音频焦点，应保证静音设置在开始播放视频之前。

**autoPlay**

autoPlay(value: boolean)

设置视频是否自动播放，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否自动播放。 true：开启自动播放；false：关闭自动播放。 默认值：false |

**controls**

controls(value: boolean)

设置控制视频播放的控制栏是否显示，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 控制视频播放的控制栏是否显示。 true：控制栏显示；false：控制栏不显示。 默认值：true |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

Video组件自带的控制器无法自定义。若有其他需求，可隐藏自带控制器并自定义控制器的样式或功能。参考[视频播放](https://gitcode.com/harmonyos_samples/video-play)。

**objectFit**

objectFit(value: ImageFit)

设置视频的填充模式，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ImageFit | 是 | 视频填充模式。 默认值：Cover 约束：不支持ImageFit类型中的枚举值MATRIX，若设置，则作用效果与Cover一致。 异常值：若设置异常值undefined、null，或不在ImageFit枚举范围内的值，作用效果均与Cover一致。 |

**loop**

loop(value: boolean)

设置是否单个视频循环播放，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否单个视频循环播放。 true：开启循环播放；false：关闭循环播放。 默认值：false |

**enableAnalyzer12+**

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

使能后，视频播放暂停时自动进入分析状态，开始分析当前画面帧，视频继续播放后自动退出分析状态。

不能和[overlay](浮层.md)属性同时使用，两者同时设置时[overlay](浮层.md)中[CustomBuilder](基础类型定义.md#ZH-CN_TOPIC_0000002553360849__custombuilder8)属性将失效。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用AI分析功能。 true：开启AI分析功能；false：关闭AI分析功能。 默认值：false |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

当前仅在使用自定义控制栏([controls](#ZH-CN_TOPIC_0000002553200815__controls)属性设置为false)时支持该功能。

该特性依赖设备能力。

**analyzerConfig12+**

analyzerConfig(config: ImageAnalyzerConfig)

设置AI分析识别类型，包括主体识别、文字识别和对象查找等功能，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | ImageAnalyzerConfig | 是 | 设置AI分析识别类型。 |

**enableShortcutKey15+**

enableShortcutKey(enabled: boolean)

设置组件支持快捷键响应，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

目前支持在组件获焦后响应空格键播放/暂停、上下方向键调整视频音量、左右方向键快进/快退。

元服务API： 从API version 15开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用快捷键响应。 true：开启快捷键响应；false：关闭快捷键响应。 默认值：false |

**事件**

除支持[通用事件](通用事件.md)外，还支持以下事件：

**onStart**

onStart(event: VoidCallback)

播放时触发该事件，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | 是 | 视频播放的回调函数。 |

**onPause**

onPause(event: VoidCallback)

暂停时触发该事件，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | 是 | 视频暂停的回调函数。 |

**onFinish**

onFinish(event: VoidCallback)

播放结束时触发该事件，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | 是 | 视频播放结束的回调函数。 |

**onError**

onError(event: VoidCallback | ErrorCallback)

播放失败时触发该事件，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)中调用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | ErrorCallback20+ | 是 | 视频播放失败时的回调函数。其中ErrorCallback类型入参的回调函数用于接收异常信息，回调返回的错误码详细介绍请参见Video组件错误码和媒体错误码。 |

**onStop12+**

onStop(event: Callback<void>)

播放停止时触发该事件(当stop()方法被调用后触发)，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<void> | 是 | 视频播放停止时的回调函数。 |

**onPrepared**

onPrepared(callback: Callback<PreparedInfo>)

视频准备完成时触发该事件，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<PreparedInfo> | 是 | 视频准备完成时的回调函数。 |

**onSeeking**

onSeeking(callback: Callback<PlaybackInfo>)

操作进度条过程时上报时间信息，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<PlaybackInfo> | 是 | 操作进度条过程时的回调函数。 |

**onSeeked**

onSeeked(callback: Callback<PlaybackInfo>)

操作进度条完成后，上报播放时间信息，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<PlaybackInfo> | 是 | 操作进度条完成后的回调函数。 |

**onUpdate**

onUpdate(callback: Callback<PlaybackInfo>)

播放进度变化时触发该事件，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<PlaybackInfo> | 是 | 播放进度变化时的回调函数。 |

**onFullscreenChange**

onFullscreenChange(callback: Callback<FullscreenInfo>)

在全屏播放与非全屏播放状态之间切换时触发该事件，支持[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002522240800__attributemodifier)动态设置属性方法。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<FullscreenInfo> | 是 | 在全屏播放与非全屏播放状态之间切换时的回调函数。 |

**FullscreenInfo18+对象说明**

用于描述当前视频是否进入全屏播放状态。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fullscreen10+ | boolean | 否 | 否 | 当前视频是否进入全屏播放状态。 true：进入全屏播放状态；false：未进入全屏播放状态。 默认值：false 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**PreparedInfo18+对象说明**

用于描述当前视频的时长。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration10+ | number | 否 | 否 | 当前视频的时长。 单位：秒 取值范围：[0,+∞) 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**PlaybackInfo18+对象说明**

用于描述当前视频播放的进度。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

元服务API： 从API version 18开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| time10+ | number | 否 | 否 | 当前视频播放的进度。 单位：秒 取值范围：[0,+∞) 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

**PosterOptions18+对象说明**

用于描述当前视频是否配置首帧送显。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showFirstFrame | boolean | 否 | 是 | 当前视频是否配置首帧送显，当开启首帧送显时，VideoOptions对象中的previewUri字段不生效。 true：开启首帧送显；false：关闭首帧送显。 默认值：false 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| contentTransitionEffect21+ | ContentTransitionEffect | 否 | 是 | 当前视频的预览图内容变化时的转场动效。配置showFirstFrame为true（即配置开启首帧送显时），或未配置有效的VideoOptions对象的previewUri时，该字段不生效。 默认值：ContentTransitionEffect.IDENTITY 设置为undefined或null时，取值为ContentTransitionEffect.IDENTITY。 元服务API： 从API version 21开始，该接口支持在元服务中使用。 |

**VideoController**

一个VideoController对象可以控制一个或多个Video。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**导入对象**

```ets
let controller: VideoController = new VideoController();
```

**constructor**

constructor()

VideoController的构造函数。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**start**

start()

开始播放。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**pause**

pause()

暂停播放，显示当前帧，再次播放时从当前位置继续播放。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**stop**

stop()

停止播放，显示当前帧，再次播放时从头开始播放。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**reset12+**

reset(): void

Video组件重置AVPlayer。显示当前帧，再次播放时从头开始播放。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**setCurrentTime**

setCurrentTime(value: number)

指定视频播放的进度位置。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

若用户需要从视频内的某一时间点开始播放，应关闭自动播放，在视频准备完成后先跳转再播放。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 视频播放进度位置。 取值范围：[0, duration] 当设置value大于duration时，进度跳转至最后；当设置value小于0时，不会进行进度跳转。 单位：秒 从API version 8开始，支持设置视频的跳转模式，详见setCurrentTime8+。 |

**requestFullscreen**

requestFullscreen(value: boolean)

请求全屏播放。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否全屏（填充满应用窗口）播放。 true：请求全屏播放；false：不请求全屏播放。 默认值：false |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

Video组件自带的全屏功能仅将视频内容设为全屏，显示默认控制器，无法显示自定义标题或控制器。如需其他功能，用户需自行实现全屏功能。

**exitFullscreen**

exitFullscreen()

退出全屏播放。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**setCurrentTime8+**

setCurrentTime(value: number, seekMode: SeekMode)

指定视频播放的进度位置，并指定跳转模式。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 视频播放进度位置。 取值范围：[0, duration] 当设置value大于duration时，进度跳转至最后；当设置value小于0时，不会进行进度跳转。 单位：秒 |
| seekMode | SeekMode | 是 | 跳转模式。 |

**SeekMode8+枚举说明**

视频跳转模式选项。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| PreviousKeyframe | 跳转到前一个最近的关键帧。 |
| NextKeyframe | 跳转到后一个最近的关键帧。 |
| ClosestKeyframe | 跳转到最近的关键帧。 |
| Accurate | 精准跳转，不论是否为关键帧。 |

**示例**

**示例1（视频播放基础用法）**

基础用法包括：控制栏、预览图、自动播放、播放速度、响应快捷键（从API version 15开始，支持通过[enableShortcutKey](#ZH-CN_TOPIC_0000002553200815__enableshortcutkey15)设置组件开启快捷键响应）、控制器（开始播放、暂停播放、停止播放、重置AVPlayer、跳转等）、首帧送显（从API version 18开始，支持通过[posterOptions](#ZH-CN_TOPIC_0000002553200815__posteroptions18对象说明)设置视频播放的首帧送显选项。从API version 21开始，posterOptions支持通过[PosterOptions](#ZH-CN_TOPIC_0000002553200815__posteroptions18对象说明)的contentTransitionEffect参数来设置当前视频的预览图内容变化时的转场动效。）以及一些状态回调方法。

```ets
// xxx.ets
@Entry
@Component
struct VideoCreateComponent {
  // $rawfile('video1.mp4')、$r('app.media.poster1')需要分别替换为开发者所需的视频、图片资源文件。
  @State videoSrc: Resource = $rawfile('video1.mp4');
  @State previewUri: Resource = $r('app.media.poster1');
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  @State isAutoPlay: boolean = false;
  @State showControls: boolean = true;
  @State isShortcutKeyEnabled: boolean = false;
  @State showFirstFrame: boolean = false;
  controller: VideoController = new VideoController();

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri, // 设置预览图。
        currentProgressRate: this.curRate, // 设置播放速度。
        controller: this.controller,
        posterOptions: { showFirstFrame: this.showFirstFrame, contentTransitionEffect: ContentTransitionEffect.OPACITY } // 关闭首帧送显, 设置预览图淡入淡出动效。
      })
        .width('100%')
        .height(600)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .enableShortcutKey(this.isShortcutKeyEnabled)
        .onStart(() => {
          console.info('onStart');
        })
        .onPause(() => {
          console.info('onPause');
        })
        .onFinish(() => {
          console.info('onFinish');
        })
        .onError(() => {
          console.info('onError');
        })
        .onStop(() => {
          console.info('onStop');
        })
        .onPrepared((e?: DurationObject) => {
          if (e != undefined) {
            console.info('onPrepared is ' + e.duration);
          }
        })
        .onSeeking((e?: TimeObject) => {
          if (e != undefined) {
            console.info('onSeeking is ' + e.time);
          }
        })
        .onSeeked((e?: TimeObject) => {
          if (e != undefined) {
            console.info('onSeeked is ' + e.time);
          }
        })
        .onUpdate((e?: TimeObject) => {
          if (e != undefined) {
            console.info('onUpdate is ' + e.time);
          }
        })
        .onFullscreenChange((e?: FullscreenObject) => {
          if (e != undefined) {
            console.info('onFullscreenChange is ' + e.fullscreen);
          }
        })

      Row() {
        // $rawfile('video2.mp4')、$r('app.media.poster2')需要分别替换为开发者所需的视频、图片资源文件。
        Button('src').onClick(() => {
          this.videoSrc = $rawfile('video2.mp4'); // 切换视频源。
        }).margin(5)
        Button('previewUri').onClick(() => {
          this.previewUri = $r('app.media.poster2'); // 切换视频预览海报。
        }).margin(5)
        Button('controls').onClick(() => {
          this.showControls = !this.showControls; // 切换是否显示视频控制栏。
        }).margin(5)
      }

      Row() {
        Button('start').onClick(() => {
          this.controller.start(); // 开始播放。
        }).margin(2)
        Button('pause').onClick(() => {
          this.controller.pause(); // 暂停播放。
        }).margin(2)
        Button('stop').onClick(() => {
          this.controller.stop(); // 结束播放。
        }).margin(2)
        Button('reset').onClick(() => {
          this.controller.reset(); // 重置AVPlayer。
        }).margin(2)
        Button('setTime').onClick(() => {
          this.controller.setCurrentTime(10, SeekMode.Accurate); // 精准跳转到视频的10s位置。
        }).margin(2)
      }

      Row() {
        Button('rate 0.75').onClick(() => {
          this.curRate = PlaybackSpeed.Speed_Forward_0_75_X; // 0.75倍速播放。
        }).margin(5)
        Button('rate 1').onClick(() => {
          this.curRate = PlaybackSpeed.Speed_Forward_1_00_X; // 原倍速播放。
        }).margin(5)
        Button('rate 2').onClick(() => {
          this.curRate = PlaybackSpeed.Speed_Forward_2_00_X; // 2倍速播放。
        }).margin(5)
      }

interface DurationObject {
  duration: number;
}

interface TimeObject {
  time: number;
}

interface FullscreenObject {
  fullscreen: boolean;
}
```

**示例2（图像分析功能）**

通过enableAnalyzer属性开启图像AI分析。

```ets
// xxx.ets
@Entry
@Component
struct ImageAnalyzerExample {
  // $rawfile('video1.mp4')、$r('app.media.poster1')需要分别替换为开发者所需的视频、图片资源文件
  @State videoSrc: Resource = $rawfile('video1.mp4');
  @State previewUri: Resource = $r('app.media.poster1');
  controller: VideoController = new VideoController();
  config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  }
  private aiController: ImageAnalyzerController = new ImageAnalyzerController();
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller,
        imageAIOptions: this.options // 设置图像AI分析选项
      })
        .width('100%')
        .height(600)
        .controls(false)
        .enableAnalyzer(true)
        .analyzerConfig(this.config)
        .onStart(() => {
          console.info('onStart');
        })
        .onPause(() => {
          console.info('onPause');
        })

      Row() {
        Button('start').onClick(() => {
          this.controller.start(); // 开始播放
        }).margin(5)
        Button('pause').onClick(() => {
          this.controller.pause(); // 暂停播放
        }).margin(5)
        Button('getTypes').onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes();
        }).margin(5)
      }
```

**示例3（播放拖入的视频）**

以下示例展示了如何使Video组件能够播放拖入的视频。

```ets
// xxx.ets
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  // $rawfile('video1.mp4')需要替换为开发者所需的视频资源文件
  @State videoSrc: Resource | string = $rawfile('video1.mp4');
  private controller: VideoController = new VideoController();

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        controller: this.controller
      })
        .width('100%')
        .height(600)
        .onPrepared(() => {
          // 在onPrepared回调中执行controller的start方法，确保视频源更换后直接开始播放。
          this.controller.start();
        })
        .onDrop((e: DragEvent) => {
          // 外部视频拖入应用Video组件范围，松手后触发通过onDrop注册的回调。
          // 在DragEvent中会包含拖入的视频源信息，取出后赋值给状态变量videoSrc即可改变Video的视频源。
          let record = e.getData().getRecords()[0];
          if (record.getType() == uniformTypeDescriptor.UniformDataType.VIDEO) {
            let videoInfo = record as unifiedDataChannel.Video;
            this.videoSrc = videoInfo.videoUri;
          }
        })
    }
```

**示例4（视频填充模式）**

通过objectFit属性设置视频填充模式。

```ets
// xxx.ets
@Entry
@Component
struct VideoObject {
  // $rawfile('rabbit.mp4')、$r('app.media.tree')需要分别替换为开发者所需的视频、图片资源文件
  @State videoSrc: Resource = $rawfile('rabbit.mp4');
  @State previewUri: Resource = $r('app.media.tree');
  @State showControls: boolean = true;
  controller: VideoController = new VideoController();

  build() {
    Column() {
      Text('ImageFit.Contain').fontSize(12)
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller
      })
        .width(350)
        .height(230)
        .controls(this.showControls)
        .objectFit(ImageFit.Contain) // 设置视频填充模式为ImageFit.Contain
        .margin(5)

      Text('ImageFit.Fill').fontSize(12)
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller
      })
        .width(350)
        .height(230)
        .controls(this.showControls)
        .objectFit(ImageFit.Fill) // 设置视频填充模式为ImageFit.Fill
        .margin(5)

      Text('ImageFit.START').fontSize(12)
      Video({
        src: this.videoSrc,
        previewUri: this.previewUri,
        controller: this.controller
      })
        .width(350)
        .height(230)
        .controls(this.showControls)
        .objectFit(ImageFit.START) // 设置视频填充模式为ImageFit.START
        .margin(5)
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002553365033.webp)

**示例5（onError事件上报错误码）**

从API version 20开始，支持通过[onError](#ZH-CN_TOPIC_0000002553200815__onerror)获取错误信息，该示例以传入不存在的视频资源路径为例。

```ets
// xxx.ets
@Entry
@Component
struct VideoErrorComponent {
  @State videoSrc: string = 'video.mp4'; // 传入不存在的视频资源路径。
  @State isAutoPlay: boolean = false;
  @State showControls: boolean = true;
  @State showFirstFrame: boolean = false;
  controller: VideoController = new VideoController();
  @State errorMessage: string = '';

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        controller: this.controller,
      })
        .width(200)
        .height(120)
        .margin(5)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .onError((err) => {
          // 通过onError事件获取错误码，code为错误码，message为错误信息。
          console.error(`code is ${err.code}, message is ${err.message}`);
          this.errorMessage = `code is ${err.code}, message is ${err.message}`;
        })
      // 传入不存在的视频资源路径，预期："code is 103602, message is Not a valid source"。
      Text(this.errorMessage)
    }
    .width('100%')
    .height('100%')
    .backgroundColor('rgb(213,213,213)')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245110.webp)

**示例6（使用attributeModifier动态设置Video组件的属性及方法）**

以下示例展示了如何使用attributeModifier动态设置Video组件的enableAnalyzer、analyzerConfig属性和onStart、onPause、onFinish、onError、onStop、onPrepared、onSeeking、onSeeked、onUpdate、onFullscreenChange方法。

```ets
// xxx.ets
class MyVideoModifier implements AttributeModifier<VideoAttribute> {
  applyNormalAttribute(instance: VideoAttribute): void {
    // 设置开启组件AI分析功能，长按触发AI识别功能
    instance.enableAnalyzer(true);
    let config: ImageAnalyzerConfig = {
      types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
    }
    instance.analyzerConfig(config);
    instance.onStart(() => {
      console.info('video: onStart');
    })
    instance.onPause(() => {
      console.info('video: onPause');
    })
    instance.onFinish(() => {
      console.info('video: onFinish');
    })
    instance.onError((err) => {
      console.error('video: onError is code = ' + err.code + ', message = ' + err.message);
    })
    instance.onStop(() => {
      console.info('video: onStop');
    })
    instance.onPrepared((e?: DurationObject) => {
      if (e != undefined) {
        console.info('video: onPrepared is ' + e.duration);
      }
    })
    instance.onSeeking((e?: TimeObject) => {
      if (e != undefined) {
        console.info('video: onSeeking is ' + e.time);
      }
    })
    instance.onSeeked((e?: TimeObject) => {
      if (e != undefined) {
        console.info('video: onSeeked is ' + e.time);
      }
    })
    instance.onUpdate((e?: TimeObject) => {
      if (e != undefined) {
        console.info('video: onUpdate is ' + e.time);
      }
    })
    instance.onFullscreenChange((e?: FullscreenObject) => {
      if (e != undefined) {
        console.info('video: onFullscreenChange is ' + e.fullscreen);
      }
    })
  }

@Entry
@Component
struct VideoModifierDemo {
  // $rawfile('video.mp4')需要替换为开发者所需的视频资源文件
  @State videoSrc: Resource = $rawfile('video.mp4');
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  @State isAutoPlay: boolean = false;
  @State showControls: boolean = false;
  controller: VideoController = new VideoController();
  @State modifier: MyVideoModifier = new MyVideoModifier();

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        currentProgressRate: this.curRate, //设置播放速度
        controller: this.controller
      })
        .width(300)
        .height(180)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .attributeModifier(this.modifier)
      Row() {
        Button('start').onClick(() => {
          this.controller.start(); // 开始播放
        }).margin(2)
        Button('pause').onClick(() => {
          this.controller.pause(); // 暂停播放
        }).margin(2)
        Button('stop').onClick(() => {
          this.controller.stop(); // 结束播放
        }).margin(2)
        Button('reset').onClick(() => {
          this.controller.reset(); // 重置AVPlayer
        }).margin(2)
      }

      Row() {
        Button('Fullscreen').onClick(() => {
          this.controller.requestFullscreen(true); // 全屏
        }).margin(2)
        Button('showControls').onClick(() => {
          this.showControls = !this.showControls; // 显示控制栏
        }).margin(2)
      }

interface DurationObject {
  duration: number;
}

interface TimeObject {
  time: number;
}

interface FullscreenObject {
  fullscreen: boolean;
}
```

![image](public_sys-resources/zh-cn_image_0000002553205071.webp)