# @ohos.PiPWindow (画中画窗口)

该模块提供画中画基础功能，包括判断当前系统是否支持画中画功能，以及创建画中画控制器用于启动或停止画中画等。适用于视频播放、视频通话或视频会议场景下，以小窗（画中画）模式呈现内容。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

在HarmonyOS 6.0.0之前，支持在Phone、Tablet设备使用画中画功能，其他设备不可用；从HarmonyOS 6.0.0开始，支持在Phone、PC/2in1、Tablet设备使用画中画功能，其他设备不可用。

-

针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](SysCap (系统能力).md#ZH-CN_TOPIC_0000002553202569__caniuse)接口判断当前设备是否支持此syscap及对应接口。

#### 导入模块

```ets
import { PiPWindow } from '@kit.ArkUI';
```

#### PiPWindow.isPiPEnabled

isPiPEnabled(): boolean

判断当前系统是否支持画中画功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前系统是否支持画中画功能。true表示支持，false则表示不支持。 |

**示例：**

```ets
let enable: boolean = PiPWindow.isPiPEnabled();
console.info('isPipEnabled:' + enable);
```

#### PiPWindow.create

create(config: PiPConfiguration): Promise<PiPController>

创建画中画控制器，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | PiPConfiguration | 是 | 创建画中画控制器的参数。该参数不能为空，并且构造该参数的context和componentController不能为空。构造该参数时，如果指定了templateType，需保证templateType是PiPTemplateType类型；如果指定了controlGroups，需保证controlGroups与templateType匹配，详见PiPControlGroup。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PiPController> | Promise对象。返回当前创建的画中画控制器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported.Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';

class Params {
  text: string = '';
  constructor(text: string) {
    this.text = text;
}

// 开发者可以通过@Builder装饰器实现布局构建
@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(20)
      .fontColor(Color.Red)
  }
  .width('100%') // 宽度方向充满画中画窗口
  .height('100%') // 高度方向充满画中画窗口
}

// 开发者可通过继承NodeController实现自定义UI控制器
class TextNodeController extends NodeController {
  private message: string;
  private textNode: BuilderNode<[Params]> | null = null;
  constructor(message: string) {
    super();
    this.message = message;
  }

  // 通过BuilderNode加载自定义布局
  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
    return this.textNode.getFrameNode();
  }

  // 开发者可自定义该方法实现布局更新
  update(message: string) {
    console.info(`update message: ${message}`);
    if (this.textNode !== null) {
      this.textNode.update(new Params(message));
}

@Entry
@Component
struct Index {
    private message: string = 'createPiP';
    private pipController: PiPWindow.PiPController | undefined = undefined;
    private mXComponentController: XComponentController = new XComponentController(); // 开发者应使用该mXComponentController初始化XComponent: XComponent( {id: 'video', type: 'surface', controller: mXComponentController} )，保证XComponent的内容可以被迁移到画中画窗口。
    private nodeController: TextNodeController = new TextNodeController('this is custom UI');
    private navId: string = "page_1"; // 假设当前页面的导航id为page_1，详见PiPConfiguration定义，具体导航名称由开发者自行定义。
    private contentWidth: number = 800; // 假设当前内容宽度800px。
    private contentHeight: number = 600; // 假设当前内容高度600px。
    private pageId: number = this.getUniqueId(); // 获取当前页面Id。
    private para: Record<string, number> = { 'PropA': 47 };
    private localStorage: LocalStorage = new LocalStorage(this.para);
    private res: boolean = this.localStorage.setOrCreate('PropB', 121);
    private defaultWindowSizeType: number = 1; // 指定画中画第一次拉起窗口为小窗口。
    private cornerAdsorptionEnabled: boolean = true;
    private config: PiPWindow.PiPConfiguration = {
        context: this.getUIContext().getHostContext() as Context,
        componentController: this.mXComponentController,
        navigationId: this.navId,
        handleId: this.pageId,
        templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
        contentWidth: this.contentWidth,
        contentHeight: this.contentHeight,
        controlGroups: [PiPWindow.VideoPlayControlGroup.VIDEO_PREVIOUS_NEXT],
        customUIController: this.nodeController, // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
        localStorage: this.localStorage, // 可选，如果需要跟踪主窗实例，可设置此参数。
        defaultWindowSizeType: this.defaultWindowSizeType, // 可选，如果需要配置默认启动窗口档位，可设置此参数。
        cornerAdsorptionEnabled: this.cornerAdsorptionEnabled, // 可选，默认为true，如果不需要画中画窗口四角吸附，可设置此参数为false。
    };

    createPiP() {
        let promise: Promise<PiPWindow.PiPController> = PiPWindow.create(this.config);
        promise.then((data: PiPWindow.PiPController) => {
            this.pipController = data;
            console.info(`Succeeded in creating pip controller. Data:${data}`);
        }).catch((err: BusinessError) => {
            console.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
        });
    }

    //仅用于功能测试，实际开发过程中开发者按功能需求设计组件
    build() {
        RelativeContainer() {
            Button(this.message)
                .onClick(() => {
                    this.createPiP();
                })
        }
```

#### PiPWindow.create12+

create(config: PiPConfiguration, contentNode: [typeNode.XComponent](../../topics/misc/FrameNode.md#ZH-CN_TOPIC_0000002529284787__xcomponent12)): Promise<PiPController>

通过typeNode创建画中画控制器，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | PiPConfiguration | 是 | 创建画中画控制器的参数。该参数不能为空，并且构造该参数的context不能为空。构造该参数时，如果指定了templateType，需保证templateType是PiPTemplateType类型；如果指定了controlGroups，需保证controlGroups与templateType匹配，详见PiPControlGroup。 |
| contentNode | [typeNode.XComponent](../../topics/misc/FrameNode.md#ZH-CN_TOPIC_0000002529284787__xcomponent12) | 是 | 用于渲染画中画窗口中的内容。该参数不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PiPController> | Promise对象。返回当前创建的画中画控制器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported.Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { PiPWindow, typeNode, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
    private message = 'createPiP'
    private pipController: PiPWindow.PiPController | undefined = undefined;
    private xComponentController: XComponentController = new XComponentController();
    private context: UIContext | undefined = this.getUIContext(); // 可传入UIContext或在布局中通过this.getUIContext()为context赋有效值
    private contentWidth: number = 800; // 假设当前内容宽度800px。
    private contentHeight: number = 600; // 假设当前内容高度600px。
    private config: PiPWindow.PiPConfiguration = {
        context: this.getUIContext().getHostContext() as Context,
        componentController: this.xComponentController,
        templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
        contentWidth: this.contentWidth,
        contentHeight: this.contentHeight,
    };
    private options: XComponentOptions = {
        type: XComponentType.SURFACE,
        controller: this.xComponentController
    }
    private xComponent = typeNode.createNode(this.context, 'XComponent', this.options);

    createPiP() {
        let promise: Promise<PiPWindow.PiPController> = PiPWindow.create(this.config, this.xComponent);
        promise.then((data: PiPWindow.PiPController) => {
            this.pipController = data;
            console.info(`Succeeded in creating pip controller. Data:${data}`);
        }).catch((err: BusinessError) => {
            console.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
        });
    }

    //仅用于功能测试，实际开发过程中开发者按功能需求设计组件
    build() {
        RelativeContainer() {
            Button(this.message)
                .onClick(() => {
                    this.createPiP();
                })
        }
```

#### PiPConfiguration

创建画中画控制器时的参数。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [BaseContext](../../topics/misc/BaseContext.md) | 否 | 否 | 表示上下文环境。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| componentController | [XComponentController](../../topics/components/XComponent.md#ZH-CN_TOPIC_0000002529444889__xcomponentcontroller) | 否 | 否 | 表示原始XComponent控制器。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| navigationId | string | 否 | 是 | 当前page导航id，不传值则默认不需要缓存页面。 1、UIAbility使用[Navigation](../../topics/components/Navigation.md)管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面。 2、UIAbility使用Router管理页面时，无需设置navigationId。 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| handleId22+ | number | 否 | 是 | 画中画还原的页面ID，点击"恢复全屏窗口"按钮后，恢复到指定的页面。只适用于UIAbility使用[Navigation](../../topics/components/Navigation.md)管理页面的场景，可以设置为Navigation下的子页面ID。默认为-1，恢复Navigation栈顶页面。推荐使用方法[getUniqueId()](../../topics/components/自定义组件内置方法.md#ZH-CN_TOPIC_0000002497444970__getuniqueid12)获取页面ID。使用Navigation模块内页面路由时，推荐使用系统路由表，否则可能会出现getUniqueId()获取页面ID不对的情况。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| templateType | PiPTemplateType | 否 | 是 | 模板类型，用以区分视频播放、视频通话或视频会议，不传值则默认为视频播放模板。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| contentWidth | number | 否 | 是 | 原始内容宽度，单位为px。用于确定画中画窗口比例。当使用typeNode的方式创建PiPController时，不传值则默认为1920。当不使用typeNode的方式创建PiPController时，不传值则默认为[XComponent](../../topics/components/XComponent.md)组件的宽度。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| contentHeight | number | 否 | 是 | 原始内容高度，单位为px。用于确定画中画窗口比例。当使用typeNode的方式创建PiPController时，不传值则默认为1080。当不使用typeNode的方式创建PiPController时，不传值则默认为[XComponent](../../topics/components/XComponent.md)组件的高度。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| controlGroups12+ | Array<PiPControlGroup> | 否 | 是 | 画中画控制面板的可选控件组列表，应用可以对此进行配置以决定是否显示。应用未配置时，面板显示基础控件（如视频播放控件组的播放/暂停控件）；应用选择配置时，则最多可以选择三个控件。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| customUIController12+ | [NodeController](../../topics/misc/NodeController.md) | 否 | 是 | 用于实现在画中画界面内容上方展示自定义UI功能，不传值则默认不使用自定义UI功能。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| localStorage17+ | LocalStorage | 否 | 是 | 页面级别的UI状态存储单元。多实例下可用来跟踪主窗实例的UI状态存储对象，不传值则无法通过画中画窗口获取主窗的UI状态存储对象。 元服务API： 从API version 17开始，该接口支持在元服务中使用。 |
| defaultWindowSizeType19+ | number | 否 | 是 | 应用第一次拉起画中画的窗口大小。 0：代表不设置大小。按照上次画中画关闭前的大小启动； 1：代表小窗； 2：代表大窗； 不传值则为默认值0。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| cornerAdsorptionEnabled22+ | boolean | 否 | 是 | 是否开启画中画四角吸附功能。当开启画中画四角吸附功能后，屏幕将被划分为四个热区：以屏幕的上下中线和左右中线为界，形成左上、右上、左下、右下四个区域。用户拖动画中画窗口并松手后，系统将根据窗口中心点所处的热区，自动将窗口吸附到对应角落。 true：表示开启画中画四角吸附功能。 false：表示关闭画中画四角吸附功能。 不传值则为默认值true。 设备行为差异： 该接口在Phone、Tablet设备上可正常调用，在其他设备上不生效。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

#### PiPWindowSize15+

画中画窗口大小。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | 窗口宽度，单位为px，该参数应为正整数，不大于屏幕宽。 |
| height | number | 是 | 否 | 窗口高度，单位为px，该参数应为正整数，不大于屏幕高。 |
| scale | number | 是 | 否 | 窗口缩放比，显示大小相对于width和height的缩放比，该参数为浮点数，取值范围大于0.0，小于等于1.0。等于1表示与width和height一样大。 |

#### PiPWindowInfo15+

画中画窗口信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowId | number | 是 | 否 | 画中画窗口ID。 |
| size | PiPWindowSize | 是 | 否 | 画中画窗口大小。 |

#### PiPTemplateType

画中画媒体类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO_PLAY | 0 | 表示将要切换为画中画播放的媒体类型是视频，系统依此加载视频播放模板。 |
| VIDEO_CALL | 1 | 表示将要切换为画中画播放的媒体类型是视频通话，系统依此加载视频通话模板。 |
| VIDEO_MEETING | 2 | 表示将要切换为画中画播放的媒体类型是视频会议，系统依此加载视频会议模板。 |
| VIDEO_LIVE | 3 | 表示将要切换为画中画播放的媒体类型是直播，系统依此加载直播模板。 |

#### PiPState

画中画生命周期状态枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ABOUT_TO_START | 1 | 表示画中画将要启动。 |
| STARTED | 2 | 表示画中画已经启动。 |
| ABOUT_TO_STOP | 3 | 表示画中画将要停止。 |
| STOPPED | 4 | 表示画中画已经停止。 |
| ABOUT_TO_RESTORE | 5 | 表示画中画将从小窗播放恢复到原始播放界面。 |
| ERROR | 6 | 表示画中画生命周期执行过程出现了异常。 |

#### PiPControlGroup12+

type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup | VideoLiveControlGroup

画中画控制面板的可选控件组列表，应用可以配置是否显示可选控件。默认情况下控制面板只显示基础控件（如视频播放控件组的播放/暂停控件）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| VideoPlayControlGroup | 视频播放控件组。 |
| VideoCallControlGroup | 视频通话控件组。 |
| VideoMeetingControlGroup | 视频会议控件组。 |
| VideoLiveControlGroup | 视频直播控件组。 |

#### VideoPlayControlGroup12+

视频播放控件组枚举。仅当[PiPTemplateType](#ZH-CN_TOPIC_0000002553200713__piptemplatetype)为VIDEO_PLAY时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO_PREVIOUS_NEXT | 101 | 视频上一个/下一个控件组。 与视频快进/后退控件组为互斥控件组。如添加视频快进/后退控件组，则不可添加该控件组。 |
| FAST_FORWARD_BACKWARD | 102 | 视频快进/后退控件组。 与视频上一个/下一个控件组为互斥控件组。如添加视频上一个/下一个控件组，则不可添加该控件组。 |

#### VideoCallControlGroup12+

视频通话控件组枚举。仅当[PiPTemplateType](#ZH-CN_TOPIC_0000002553200713__piptemplatetype) 为VIDEO_CALL时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MICROPHONE_SWITCH | 201 | 打开/关闭麦克风控件组。 |
| HANG_UP_BUTTON | 202 | 挂断控件组。 |
| CAMERA_SWITCH | 203 | 打开/关闭摄像头控件组。 |
| MUTE_SWITCH | 204 | 静音控件组。 |

#### VideoMeetingControlGroup12+

视频会议控件组枚举。仅当[PiPTemplateType](#ZH-CN_TOPIC_0000002553200713__piptemplatetype) 为VIDEO_MEETING时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HANG_UP_BUTTON | 301 | 挂断控件组。 |
| CAMERA_SWITCH | 302 | 打开/关闭摄像头控件组。 |
| MUTE_SWITCH | 303 | 静音控件组。 |
| MICROPHONE_SWITCH | 304 | 打开/关闭麦克风控件组。 |

#### VideoLiveControlGroup12+

视频直播控件组枚举。仅当[PiPTemplateType](#ZH-CN_TOPIC_0000002553200713__piptemplatetype) 为VIDEO_LIVE时使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO_PLAY_PAUSE | 401 | 播放/暂停直播控件组。 |
| MUTE_SWITCH | 402 | 静音控件组。 |

#### PiPActionEventType

type PiPActionEventType = PiPVideoActionEvent | PiPCallActionEvent | PiPMeetingActionEvent | PiPLiveActionEvent

画中画控制面板控件动作事件类型，支持以下四种。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| PiPVideoActionEvent | 视频播放控制面板控件事件类型。 |
| PiPCallActionEvent | 视频通话控制面板控件事件类型。 |
| PiPMeetingActionEvent | 视频会议控制面板控件事件类型。 |
| PiPLiveActionEvent | 直播控制面板控件事件类型。 |

#### PiPVideoActionEvent

type PiPVideoActionEvent = 'playbackStateChanged' | 'nextVideo' | 'previousVideo' | 'fastForward' | 'fastBackward'

视频播放控制事件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| 'playbackStateChanged' | 播放状态发生了变化。 |
| 'nextVideo' | 播放下一个视频。 |
| 'previousVideo' | 播放上一个视频。 |
| 'fastForward'12+ | 视频进度快进。从API version 12 开始支持。 |
| 'fastBackward'12+ | 视频进度后退。从API version 12 开始支持。 |

#### PiPCallActionEvent

type PiPCallActionEvent = 'hangUp' | 'micStateChanged' | 'videoStateChanged' | 'voiceStateChanged'

视频通话控制事件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| 'hangUp' | 挂断视频通话。 |
| 'micStateChanged' | 打开或关闭麦克风。 |
| 'videoStateChanged' | 打开或关闭摄像头。 |
| 'voiceStateChanged'12+ | 静音或解除静音。 |

#### PiPMeetingActionEvent

type PiPMeetingActionEvent = 'hangUp' | 'voiceStateChanged' | 'videoStateChanged' | 'micStateChanged'

视频会议控制事件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| 'hangUp' | 挂断视频会议。 |
| 'voiceStateChanged' | 静音或解除静音。 |
| 'videoStateChanged' | 打开或关闭摄像头。 |
| 'micStateChanged'12+ | 打开或关闭麦克风。 |

#### PiPLiveActionEvent

type PiPLiveActionEvent = 'playbackStateChanged' | 'voiceStateChanged'

直播控制事件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| 'playbackStateChanged' | 播放或暂停直播。 |
| 'voiceStateChanged'12+ | 静音或解除静音。 |

#### PiPControlStatus12+

控制面板控件状态枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAY | 1 | 播放。 |
| PAUSE | 0 | 暂停。 |
| OPEN | 1 | 打开。 |
| CLOSE | 0 | 关闭。 |

#### PiPControlType12+

控制面板控件类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO_PLAY_PAUSE | 0 | 播放/暂停控件。 |
| VIDEO_PREVIOUS | 1 | 视频上一个控件。 |
| VIDEO_NEXT | 2 | 视频下一个控件。 |
| FAST_FORWARD | 3 | 视频快进控件 |
| FAST_BACKWARD | 4 | 视频快退控件。 |
| HANG_UP_BUTTON | 5 | 挂断控件。 |
| MICROPHONE_SWITCH | 6 | 打开/关闭麦克风控件。 |
| CAMERA_SWITCH | 7 | 打开/关闭摄像头控件。 |
| MUTE_SWITCH | 8 | 打开/关闭静音控件。 |

#### ControlPanelActionEventCallback12+

type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: number) => void

描述画中画控制面板控件动作事件回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | PiPActionEventType | 是 | 回调画中画控制面板控件动作事件类型。 应用依据控件动作事件做相应处理，如触发'playbackStateChanged'事件时，需要开始或停止视频。 |
statusnumber否表示可切换状态的控件当前的状态，如具备打开和关闭两种状态的麦克风控件组、摄像头控件组和静音控件组，打开为1，关闭为0。其余控件该参数返回默认值-1。

#### ControlEventParam12+

画中画控制面板控件动作回调的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controlType | PiPControlType | 否 | 否 | 回调画中画控制面板控件动作事件类型。应用依据控件类型做相应处理，如视频模板中暂停/播放控件被点击时，需要开始或停止视频。 |
| status | PiPControlStatus | 否 | 是 | 表示可切换状态的控件当前的状态，如具备打开和关闭两种状态的麦克风控件组、摄像头控件组和静音控件组，打开为PiPControlStatus.PLAY，关闭为PiPControlStatus.PAUSE。如不具备开/关和播放/暂停状态的挂断控件默认返回值为-1。 |

#### PiPController

画中画控制器实例。用于启动、停止画中画以及更新回调注册等。

下列API示例中都需先使用[PiPWindow.create()](#ZH-CN_TOPIC_0000002553200713__pipwindowcreate)方法获取到PiPController实例，再通过此实例调用对应方法。

**系统能力：** SystemCapability.Window.SessionManager

#### startPiP

startPiP(): Promise<void>

启动画中画，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码]([窗口错误码](../../errors/窗口错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300012 | The PiP window state is abnormal. |
| 1300013 | Failed to create the PiP window. |
| 1300014 | PiP internal error. |
| 1300015 | Repeated PiP operation. |

**示例：**

```ets
//开发者可根据pipController的定义方式自行实现pipController的调用
let promise : Promise<void> = this.pipController.startPiP();
promise.then(() => {
  console.info(`Succeeded in starting pip.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
});
```

#### stopPiP

stopPiP(): Promise<void>

停止画中画，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300011 | Failed to destroy the PiP window. |
| 1300012 | The PiP window state is abnormal. |
| 1300015 | Repeated PiP operation. |

**示例：**

```ets
let promise : Promise<void> = this.pipController.stopPiP();
promise.then(() => {
  console.info(`Succeeded in stopping pip.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to stop pip. Cause:${err.code}, message:${err.message}`);
});
```

#### setAutoStartEnabled

setAutoStartEnabled(enable: boolean): void

设置是否在返回桌面时自动启动画中画，默认不自动拉起。

在使用xComponent方案实现画中画功能并结合[Navigation](../../topics/components/Navigation.md)进行路由管理时，首次调用setAutoStartEnabled(true)方法，系统会缓存当前应用传入的NavigationId的栈顶信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 如返回桌面时需自动启动画中画，则该参数配置为true，否则为false。若设置中自动启动画中画开关为关闭状态，就算该参数配置为true，应用返回桌面时也不会自动启动画中画窗口。 |

**示例：**

```ets
let enable: boolean = true;
this.pipController.setAutoStartEnabled(enable);
```

#### updateContentSize

updateContentSize(width: number, height: number): void

当媒体源切换时，向画中画控制器更新媒体源尺寸信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 表示媒体内容宽度，必须为大于0的数字，单位为px。用于更新画中画窗口比例。 |
| height | number | 是 | 表示媒体内容高度，必须为大于0的数字，单位为px。用于更新画中画窗口比例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: The PiPController is not created or destroyed. |

**示例：**

```ets
let width: number = 540; // 假设当前内容宽度变为540px。
let height: number = 960; // 假设当前内容高度变为960px。
this.pipController.updateContentSize(width, height);
```

#### updatePiPControlStatus12+

updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void

更新画中画控制面板控件功能状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controlType | PiPControlType | 是 | 表示画中画控制面板控件类型。目前仅支持VIDEO_PLAY_PAUSE、MICROPHONE_SWITCH、CAMERA_SWITCH和MUTE_SWITCH这几种控件类型，传入其他控件类型无效。 |
| status | PiPControlStatus | 是 | 表示画中画控制面板控件状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: The PiPController is not created or destroyed. |

**示例：**

```ets
let controlType: PiPWindow.PiPControlType = PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE; // 视频播放控制面板中播放/暂停控件。
let status: PiPWindow.PiPControlStatus = PiPWindow.PiPControlStatus.PLAY; // 视频播放控制面板中播放/暂停控件为播放状态。
this.pipController.updatePiPControlStatus(controlType, status);
```

#### updateContentNode18+

updateContentNode(contentNode: [typeNode.XComponent](../../topics/misc/FrameNode.md#ZH-CN_TOPIC_0000002529284787__xcomponent12)): Promise<void>

更新画中画节点内容，使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contentNode | [typeNode.XComponent](../../topics/misc/FrameNode.md#ZH-CN_TOPIC_0000002529284787__xcomponent12) | 是 | 用于渲染画中画窗口中的内容。该参数不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed |
| 801 | Capability not supported.Failed to call the API due to limited device capabilities. |
| 1300014 | PiP internal error. |

**示例：**

```ets
import { typeNode, UIContext } from '@kit.ArkUI';

let context: UIContext | undefined = undefined; // 可传入UIContext或在布局中通过this.getUIContext()为context赋有效值

try {
  let contentNode = typeNode.createNode(context, "XComponent");
  this.pipController.updateContentNode(contentNode);
} catch (exception) {
  console.error(`Failed to update content node. Cause: ${exception.code}, message: ${exception.message}`);
}
```

#### setPiPControlEnabled12+

setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void

更新控制面板控件使能状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controlType | PiPControlType | 是 | 表示画中画控制面板控件类型。 |
| enabled | boolean | 是 | 表示画中画控制面板控件使能状态。true表示控件为可使用状态，false则为禁用状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: The PiPController is not created or destroyed. |

**示例：**

```ets
let controlType: PiPWindow.PiPControlType = PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE; // 视频播放控制面板中播放/暂停控件。
let enabled: boolean = false; // 视频播放控制面板中播放/暂停控件为禁用状态。
this.pipController.setPiPControlEnabled(controlType, enabled);
```

#### getPiPWindowInfo15+

getPiPWindowInfo(): Promise<[PiPWindowInfo](#ZH-CN_TOPIC_0000002553200713__pipwindowinfo15)>

获取画中画窗口信息，使用Promise异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PiPWindowInfo> | Promise对象，返回当前画中画窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300014 | PiP internal error. |

**示例：**

```ets
let pipWindowInfo: PiPWindow.PiPWindowInfo | undefined = undefined;
try {
  let promise : Promise<PiPWindow.PiPWindowInfo> = this.pipController.getPiPWindowInfo();
  promise.then((data) => {
    pipWindowInfo = data;
    console.info('Success in get pip window info. Info: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to get pip window info. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get pip window info. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### getPiPSettingSwitch20+

getPiPSettingSwitch(): Promise<boolean>

获取设置中自动启动画中画开关的状态，使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：** 该接口在Phone设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回当前自动启动画中画开关状态，true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300014 | PiP internal error. |

**示例：**

```ets
let pipSwitchStatus: boolean | undefined = undefined;
try {
  let promise : Promise<boolean> = this.pipController.getPiPSettingSwitch();
  promise.then((data) => {
    pipSwitchStatus = data;
    console.info('Succeeded in getting pip switch status. switchStatus: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to get pip switch status. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get pip switch status. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

**isPiPActive23+**

isPiPActive(): Promise<boolean>

获取画中画的隐藏状态。使用Promise异步回调。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Window.SessionManager

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回当前画中画的隐藏状态。true表示前台可见，false表示前台不可见（收入侧边栏）。画中画生命周期不为STARTED时调用本接口总是返回false。 |

错误码：

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300014 | PiP internal error. |

示例：

```ets
let pipActiveStatus: boolean | undefined = undefined;
try {
  let promise : Promise<boolean> | undefined = this.pipController?.isPiPActive();
  promise?.then((data) => {
    pipActiveStatus = data;
    console.info('Succeeded in getting pip active status. activeStatus: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to get pip active status. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to get pip active status. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('stateChange')

on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void

开启画中画生命周期状态的监听，建议在不需要使用时关闭监听，否则可能存在内存泄漏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'stateChange'，即画中画生命周期状态变化事件。 |
| callback | function | 是 | 回调生命周期状态变化事件以及原因。 state：PiPState，表示当前画中画生命周期状态。 reason：string，表示当前生命周期的切换原因。 在HarmonyOS开发套件（基于API 23）配套的系统版本之前，reason始终为“0”，无需关注。 从HarmonyOS开发套件（基于API 23）配套的系统版本开始，reason为当前生命周期的切换原因： "requestStart"：应用调用startPip接口； "autoStart"：应用退后台触发画中画自动启动； "requestDelete"：应用调用stopPip接口； "panelActionDelete"：用户点击画中画窗口的关闭按钮； "dragDelete"：用户将画中画窗口拖入垃圾桶； "panelActionRestore"：用户点击画中画窗口的还原按钮（无还原按钮时可点击画中画窗口）触发还原； "other"：其他原因，如新的画中画窗口拉起导致当前窗口被关闭、应用主窗口被关闭等场景。 |

**示例：**

```ets
this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
  let curState: string = '';
  switch (state) {
    case PiPWindow.PiPState.ABOUT_TO_START:
      curState = 'ABOUT_TO_START';
      break;
    case PiPWindow.PiPState.STARTED:
      curState = 'STARTED';
      break;
    case PiPWindow.PiPState.ABOUT_TO_STOP:
      curState = 'ABOUT_TO_STOP';
      break;
    case PiPWindow.PiPState.STOPPED:
      curState = 'STOPPED';
      break;
    case PiPWindow.PiPState.ABOUT_TO_RESTORE:
      curState = 'ABOUT_TO_RESTORE';
      break;
    case PiPWindow.PiPState.ERROR:
      curState = 'ERROR';
      break;
    default:
      break;
  }
  console.info('stateChange:' + curState + ' reason:' + reason);
});
```

#### off('stateChange')

off(type: 'stateChange'): void

关闭画中画生命周期状态的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'stateChange'，即画中画生命周期状态变化事件。 |

**示例：**

```ets
this.pipController.off('stateChange');
```

#### on('controlPanelActionEvent')

on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void

开启画中画控制面板控件动作事件的监听，建议在不需要使用时关闭监听，否则可能存在内存泄漏。推荐使用[on('controlEvent')](#ZH-CN_TOPIC_0000002553200713__oncontrolevent12)来开启画中画控制面板控件动作事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'controlPanelActionEvent'，即画中画控制面板控件动作事件。 |
| callback | ControlPanelActionEventCallback | 是 | 描述画中画控制面板控件动作事件回调。 |

**示例：**

```ets
this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
  switch (event) {
    case 'playbackStateChanged':
      if (status === 0) {
        //停止视频
      } else if (status === 1) {
        //播放视频
      }
      break;
    case 'nextVideo':
      // 切换到下一个视频
      break;
    case 'previousVideo':
      // 切换到上一个视频
      break;
    case 'fastForward':
      // 视频进度快进
      break;
    case 'fastBackward':
      // 视频进度后退
      break;
    default:
      break;
  }
  console.info('registerActionEventCallback, event:' + event);
});
```

#### on('controlEvent')12+

on(type: 'controlEvent', callback: Callback<ControlEventParam>): void

开启画中画控制面板控件动作事件的监听，建议在不需要使用时关闭监听，否则可能存在内存泄漏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'controlEvent'，即画中画控制面板控件动作事件。 |
| callback | Callback<ControlEventParam> | 是 | 描述画中画控制面板控件动作事件回调。 |

**示例：**

```ets
this.pipController.on('controlEvent', (control) => {
  switch (control.controlType) {
    case PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE:
      if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
        //停止视频
      } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
        //播放视频
      }
      break;
    case PiPWindow.PiPControlType.VIDEO_NEXT:
      // 切换到下一个视频
      break;
    case PiPWindow.PiPControlType.VIDEO_PREVIOUS:
      // 切换到上一个视频
      break;
    case PiPWindow.PiPControlType.FAST_FORWARD:
      // 视频进度快进
      break;
    case PiPWindow.PiPControlType.FAST_BACKWARD:
      // 视频进度后退
      break;
    default:
      break;
  }
  console.info('registerControlEventCallback, controlType:' + control.controlType + ', status' + control.status);
});
```

#### off('controlPanelActionEvent')

off(type: 'controlPanelActionEvent'): void

关闭画中画控制面板控件动作事件的监听。推荐使用[off('controlEvent')](#ZH-CN_TOPIC_0000002553200713__offcontrolevent12)来关闭画中画控制面板控件动作事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'controlPanelActionEvent'，即画中画控制面板控件动作事件。 |

**示例：**

```ets
this.pipController.off('controlPanelActionEvent');
```

#### off('controlEvent')12+

off(type: 'controlEvent', callback?: Callback<ControlEventParam>): void

关闭画中画控制面板控件动作事件的监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'controlEvent'，即画中画控制面板控件动作事件。 |
| callback | Callback<ControlEventParam> | 否 | 描述画中画控制面板控件动作事件回调。如果不传该参数时，解除type为'controlEvent'的所有回调。 |

**示例：**

```ets
this.pipController.off('controlEvent', () => {});
```

#### on('pipWindowSizeChange')15+

on(type: 'pipWindowSizeChange', callback: Callback<PiPWindowSize>): void

开启画中画窗口尺寸变化事件的监听，建议在不需要使用时关闭监听，否则可能存在内存泄漏。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'pipWindowSizeChange'，即画中画窗口尺寸变化事件。 |
| callback | Callback<PiPWindowSize> | 是 | 回调函数。返回当前画中画窗口的尺寸。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: Callback is already registered. |
| 801 | Capability not supported.Failed to call the API due to limited device capabilities. |
| 1300014 | PiP internal error. |

**示例：**

```ets
try {
  this.pipController.on('pipWindowSizeChange', (size: PiPWindow.PiPWindowSize) => {
    console.info('Succeeded in enabling the listener for pip window size changes. size: ' + JSON.stringify(size));
  });
} catch (exception) {
  console.error(`Failed to enable the listener for pip window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### off('pipWindowSizeChange')15+

off(type: 'pipWindowSizeChange', callback?: Callback<PiPWindowSize>): void

关闭画中画窗口尺寸变化事件的监听。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'pipWindowSizeChange'，即画中画窗口尺寸变化事件。 |
| callback | Callback<PiPWindowSize> | 否 | 回调函数。返回当前画中画窗口的尺寸。如果传入参数，则关闭该监听。如果未传入参数，解除type为'pipWindowSizeChange'的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported.Failed to call the API due to limited device capabilities. |

**示例：**

```ets
const callback = (size: PiPWindow.PiPWindowSize) => {
  // ...
}
try {
  // 通过on接口开启监听
  this.pipController.on('pipWindowSizeChange', callback);
} catch (exception) {
  console.error(`Failed to enable the listener for pip window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
}

try {
  // 关闭指定callback的监听
  this.pipController.off('pipWindowSizeChange', callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  this.pipController.off('pipWindowSizeChange');
} catch (exception) {
  console.error(`Failed to disable the listener for pip window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

#### on('activeStatusChange')22+

on(type: 'activeStatusChange', callback: Callback<boolean>): void

开启画中画窗口隐藏状态变化事件的监听，建议在不需要使用时关闭监听，否则可能存在内存泄漏。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'activeStatusChange'，即画中画隐藏状态变化事件。 |
| callback | Callback<boolean> | 是 | 返回当前画中画的隐藏状态。true表示前台可见，false表示前台不可见（收入侧边栏）。 |

**示例：**

```ets
let callback = (activeStatus: boolean) => {
  console.info(`pip window is visible: ${activeStatus}`);
}
this.pipController.on('activeStatusChange', callback);
```

#### off('activeStatusChange')22+

off(type: 'activeStatusChange', callback?: Callback<boolean>): void

关闭画中画窗口隐藏状态变化事件的监听。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'activeStatusChange'，即画中画隐藏状态变化事件。 |
| callback | Callback<boolean> | 否 | 返回当前画中画的隐藏状态。true表示前台可见，false表示前台不可见（收入侧边栏）。如果未传入参数，解除type为'activeStatusChange'的所有回调。 |

**示例：**

```ets
let callback = (activeStatus: boolean) => {
  console.info(`pip window is visible: ${activeStatus}`);
}
this.pipController.off('activeStatusChange', callback);
```