# @ohos.accessibility (辅助应用)

本模块提供辅助应用查询能力，包括获取辅助应用列表、获取辅助应用启用状态、获取无障碍字幕配置等。

- 本模块首批接口从 API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { accessibility } from '@kit.AccessibilityKit';
```

#### AbilityState

type AbilityState = 'enable' | 'disable' | 'install'

辅助应用状态类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'enable'表示辅助应用已启用。'disable'辅助应用已禁用。'install'辅助应用已安装。

#### AbilityType

type AbilityType = 'audible' | 'generic' | 'haptic' | 'spoken' | 'visual' | 'all'

无障碍辅助应用类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'audible'表示具有听觉反馈。'generic'表示具有通用反馈。'haptic'表示具有触觉反馈。'spoken'表示具有语音反馈。'visual'表示具有视觉反馈。'all'9+表示以上所有类别。

#### AccessibilityAbilityInfo

辅助应用信息。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### 属性

名称类型只读可选说明idstring是否ability id。namestring是否ability 名。bundleNamestring是否Bundle名称。targetBundleNames9+Array<string>是否关注的目标Bundle名称。abilityTypesArray<[AbilityType](#ZH-CN_TOPIC_0000002529444639__abilitytype)>是否辅助应用类型。capabilitiesArray<[Capability](#ZH-CN_TOPIC_0000002529444639__capability)>是否辅助应用能力列表。descriptionstring是否辅助应用描述。eventTypesArray<[EventType](#ZH-CN_TOPIC_0000002529444639__eventtype)>是否辅助应用关注的无障碍事件列表。needHide12+boolean是否辅助应用是否在已安装的扩展服务列表中被隐藏，true表示隐藏服务，false表示显示服务。label12+string是否扩展应用在扩展服务列表中的名称。

#### Action

type Action = 'accessibilityFocus' | 'clearAccessibilityFocus' | 'focus' | 'clearFocus' | 'clearSelection' |

 'click' | 'longClick' | 'cut' | 'copy' | 'paste' | 'select' | 'setText' | 'delete' |

 'scrollForward' | 'scrollBackward' | 'setSelection' | 'setCursorPosition' | 'home' |

 'back' | 'recentTask' | 'notificationCenter' | 'controlCenter' | 'common'

应用所支持的目标动作，需要配置参数的目标动作已在描述中标明。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'click'表示点击操作。'longClick'表示长按操作。'scrollForward'表示向前滚动操作。'scrollBackward'表示向后滚动操作。'focus'表示获得焦点操作。'clearFocus'表示清除焦点操作。'clearSelection'表示清除选择操作。当前版本暂不支持。'accessibilityFocus'表示获得无障碍焦点操作。'clearAccessibilityFocus'表示清除无障碍焦点操作。'cut'表示剪切操作。'copy'表示复制操作。'paste'表示粘贴操作。'select'表示选择操作。'setText'表示设置文本操作，需配置参数setText。'delete'表示删除操作。当前版本暂不支持。'setSelection'表示选择操作，需配置参数selectTextBegin、selectTextEnd、selectTextInForWard。'common'表示没有特定操作，用于主动聚焦、主动播报等场景。'home'表示返回桌面操作。'back'表示返回上一级操作。'recentTask'表示打开最近任务操作。'notificationCenter'表示打开通知栏操作。'controlCenter'表示打开控制中心操作。'setCursorPosition'表示设置光标位置操作，需配置参数offset。

#### Capability

type Capability = 'retrieve' | 'touchGuide' | 'keyEventObserver' | 'zoom' | 'gesture'

辅助应用能力类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'retrieve'具有检索窗口内容的能力。'touchGuide'具有触摸探索模式的能力。'keyEventObserver'具有过滤按键事件的能力。'zoom'具有控制显示放大的能力，当前版本暂不支持。'gesture'具有执行手势动作的能力。

#### CaptionsFontEdgeType8+

type CaptionsFontEdgeType = 'none' | 'raised' | 'depressed' | 'uniform' | 'dropShadow'

字幕字体边缘类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

类型说明'none'表示无效果。'raised'表示凸起效果。'depressed'表示凹陷效果。'uniform'表示轮廓效果。'dropShadow'表示阴影效果。

#### CaptionsFontFamily8+

type CaptionsFontFamily = 'default' | 'monospacedSerif' | 'serif' | 'monospacedSansSerif' |

 'sansSerif' | 'casual' | 'cursive' | 'smallCapitals'

字幕字体。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

类型说明'default'表示默认字体。'monospacedSerif'表示等宽 Serif 字体。'serif'表示Serif 字体。'monospacedSansSerif'表示等宽 Sans Serif 字体。'sansSerif'表示Sans Serif 字体。'casual'表示非正式字体。'cursive'表示手写字体。'smallCapitals'表示小型大写字母字体。

#### CaptionsStyle8+

字幕风格。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

名称类型只读可选说明fontFamily[CaptionsFontFamily](#ZH-CN_TOPIC_0000002529444639__captionsfontfamily8)否否描述字幕字体。fontScalenumber否否描述字幕字体缩放系数，单位%，参数范围1~200。fontColornumber | string否否

描述字幕字体颜色。

number：HEX 格式颜色，支持 rgb 或 argb。

string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。

例：不透明红色，number: 0xffff0000，string: '#ff0000', '#ff0000ff', '#f00', '#f00f'。

fontEdgeType[CaptionsFontEdgeType](#ZH-CN_TOPIC_0000002529444639__captionsfontedgetype8)否否描述字幕字体边缘。backgroundColornumber | string否否

描述字幕背景颜色。

number：HEX 格式颜色，支持 rgb 或 argb。

string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。

例：不透明红色，number: 0xffff0000，string: '#ff0000', '#ff0000ff', '#f00', '#f00f'。

windowColornumber | string否否

描述字幕窗口颜色。

number：HEX 格式颜色，支持 rgb 或 argb。

string：支持 '#rrggbb', '#rrggbbaa', '#rgb', '#rgba' 格式。

例：不透明红色，number: 0xffff0000，string: '#ff0000', '#ff0000ff', '#f00', '#f00f'。

#### CaptionsManager8+

字幕配置管理，在调用CaptionsManager的方法前，需要先通过 [accessibility.getCaptionsManager() ](#ZH-CN_TOPIC_0000002529444639__accessibilitygetcaptionsmanagerdeprecated)获取 CaptionsManager实例。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

#### 属性

名称类型只读可选说明enabledboolean否否表示是否启用字幕配置。true表示字幕配置开启，false表示字幕配置关闭。style[CaptionsStyle](#ZH-CN_TOPIC_0000002529444639__captionsstyle8)否否表示字幕风格。

#### on('enableChange')(deprecated)

on(type: 'enableChange', callback: Callback<boolean>): void;

监听字幕配置启用状态变化事件，使用callback异步回调。

从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

参数名类型必填说明typestring是监听的事件名，固定为‘enableChange’，即字幕配置启用状态变化事件。callbackCallback<boolean>是回调函数，在启用状态变化时将状态通过此函数进行通知。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

#### on('styleChange')(deprecated)

on(type: 'styleChange', callback: Callback<CaptionsStyle>): void;

监听字幕风格变化事件，使用callback异步回调。

从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

参数名类型必填说明typestring是监听的事件名，固定为‘styleChange’，即字幕风格变化事件。callbackCallback<[CaptionsStyle](#ZH-CN_TOPIC_0000002529444639__captionsstyle8)>是回调函数，在字幕风格变化时通过此函数进行通知。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

#### off('enableChange')(deprecated)

off(type: 'enableChange', callback?: Callback<boolean>): void;

取消监听字幕配置启用状态变化事件，使用callback异步回调。

从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

参数名类型必填说明typestring是取消监听的事件名，固定为‘enableChange’，即字幕配置启用状态变化事件。callbackCallback<boolean>否回调函数，取消指定callback对象的事件响应。需与on('enableChange')的callback一致。缺省时，表示注销所有已注册事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe caption manager enable state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

#### off('styleChange')(deprecated)

off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void;

取消字幕风格变化监听事件，使用callback异步回调。

从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

参数名类型必填说明typestring是取消监听的事件名，固定为‘styleChange’，即字幕风格变化事件。callbackCallback<[CaptionsStyle](#ZH-CN_TOPIC_0000002529444639__captionsstyle8)>否回调函数，取消指定callback对象的事件响应。需与on('styleChange')的callback一致。缺省时，表示注销所有已注册事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(`subscribe caption manager style state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

#### EventInfo

界面变更事件。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### 属性

名称类型只读可选说明type[EventType](#ZH-CN_TOPIC_0000002529444639__eventtype)否否无障碍事件类型，不可缺省。windowUpdateType[WindowUpdateType](#ZH-CN_TOPIC_0000002529444639__windowupdatetype)否是窗口变化类型。bundleNamestring否否目标应用名；不可缺省。componentTypestring否是应与事件源组件类型对应，如：按钮Button类型->'Button'、图片Image类型->'Image'。pageIdnumber否是事件源的页面ID，默认值为0。descriptionstring否是事件描述，根据实际场景设置，无特殊限制。triggerAction[Action](#ZH-CN_TOPIC_0000002529444639__action)否否触发事件的Action，不可缺省。textMoveUnit[TextMoveUnit](#ZH-CN_TOPIC_0000002529444639__textmoveunit)否是文本移动粒度。contentsArray<string>否是内容列表，根据实际场景设置，无特殊限制。lastContentstring否是最新内容，根据实际场景设置，无特殊限制。beginIndexnumber否是画面显示条目的开始序号，默认值为0。currentIndexnumber否是当前条目序号，默认值为0。endIndexnumber否是画面显示条目的结束序号，默认值为0。itemCountnumber否是条目总数，默认值为0。elementId12+number否是组件elementId，默认值为0。textAnnouncedForAccessibility12+string否是主动播报的内容。当应用需要主动播报时，根据实际场景设置播报内容，无特殊限制。textResourceAnnouncedForAccessibility18+Resource否是主动播报的内容支持传入Resource类型，且只能传入string。customId12+string否是主动聚焦的组件ID。

#### constructor

constructor(jsonObject: Object)

构造函数。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明jsonObjectObject是包含 type、bundleName 和 triggerAction 三个字段的 JSON对象，详见示例。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});
```

#### constructor11+

constructor(type: EventType, bundleName: string, triggerAction: Action)

构造函数。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明type[EventType](#ZH-CN_TOPIC_0000002529444639__eventtype)是无障碍事件类型。bundleNamestring是目标应用名。triggerAction[Action](#ZH-CN_TOPIC_0000002529444639__action)是触发事件的 Action。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

let eventInfo = new accessibility.EventInfo('click', 'com.example.MyApplication', 'click');
```

#### EventType

type EventType = 'accessibilityFocus' | 'accessibilityFocusClear' |

'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' |

'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' |

'announceForAccessibility' | 'requestFocusForAccessibilityNotInterrupt' |

'announceForAccessibilityNotInterrupt' | 'scrolling'

无障碍事件类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'accessibilityFocus'表示获得无障碍焦点的事件。'accessibilityFocusClear'表示清除无障碍焦点的事件。'click'表示点击组件的事件。'longClick'表示长按组件的事件。'select'表示选择组件的事件。'hoverEnter'表示悬停进入组件的事件。'hoverExit'表示悬停离开组件的事件。'focus'表示组件获得焦点的事件，当前版本暂不支持。'textUpdate'表示组件文本已更改的事件。'textSelectionUpdate'表示选定文本已更改的事件，当前版本暂不支持。'scroll'表示滚动视图的事件。'requestFocusForAccessibility'表示主动聚焦的事件。'announceForAccessibility'表示主动播报的事件。'requestFocusForAccessibilityNotInterrupt'18+表示主动聚焦不打断的事件。'announceForAccessibilityNotInterrupt'18+表示主动播报不打断的事件。'scrolling'18+表示滚动视图中有item被滚出屏幕的事件。

#### TextMoveUnit

type TextMoveUnit = 'char' | 'word' | 'line' | 'page' | 'paragraph'

文本无障碍导航移动粒度。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'char'表示以字符为移动粒度遍历节点文本。'word'表示以词为移动粒度遍历节点文本。'line'表示以行为移动粒度遍历节点文本。'page'表示以页为移动粒度遍历节点文本。'paragraph'表示以段落为移动粒度遍历节点文本。

#### WindowUpdateType

type WindowUpdateType = 'add' | 'remove' | 'bounds' | 'active' | 'focus'

窗口变化类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'add'表示添加窗口的窗口变化事件，值固定为'add'字符串。'remove'表示一个窗口被删除的窗口变化事件，值固定为'remove'字符串。'bounds'表示窗口边界已更改的窗口变化事件，值固定为'bounds'字符串。'active'表示窗口变为活动或不活动的窗口变化事件，值固定为'active'字符串。'focus'表示窗口焦点发生变化的窗口变化事件，值固定为'focus'字符串。

#### accessibility.getAbilityLists(deprecated)

getAbilityLists(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

查询辅助应用列表，使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。

推荐使用[accessibility.getAccessibilityExtensionList()](#ZH-CN_TOPIC_0000002529444639__accessibilitygetaccessibilityextensionlist9)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明abilityType[AbilityType](#ZH-CN_TOPIC_0000002529444639__abilitytype)是辅助应用的类型。stateType[AbilityState](#ZH-CN_TOPIC_0000002529444639__abilitystate)是辅助应用的状态。

**返回值：**

类型说明Promise<Array<[AccessibilityAbilityInfo](#ZH-CN_TOPIC_0000002529444639__accessibilityabilityinfo)>>Promise对象，返回辅助应用信息列表。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken';
let abilityState: accessibility.AbilityState = 'enable';

accessibility.getAbilityLists(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get accessibility extension list because ${JSON.stringify(err)}`);
});
```

#### accessibility.getAbilityLists(deprecated)

getAbilityLists(abilityType: AbilityType, stateType: AbilityState,callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

查询辅助应用列表，使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。

推荐使用[accessibility.getAccessibilityExtensionList()](#ZH-CN_TOPIC_0000002529444639__accessibilitygetaccessibilityextensionlist9-1)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明abilityType[AbilityType](#ZH-CN_TOPIC_0000002529444639__abilitytype)是辅助应用的类型。stateType[AbilityState](#ZH-CN_TOPIC_0000002529444639__abilitystate)是辅助应用的状态。callbackAsyncCallback<Array<[AccessibilityAbilityInfo](#ZH-CN_TOPIC_0000002529444639__accessibilityabilityinfo)>>是回调函数，返回辅助应用信息列表。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken';
let abilityState: accessibility.AbilityState = 'enable';

accessibility.getAbilityLists(abilityType, abilityState, (err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
  if (err) {
    console.error(`failed to get accessibility extension list because ${JSON.stringify(err)}`);
    return;
  }
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
})
```

#### accessibility.getAccessibilityExtensionList9+

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

查询辅助应用列表，使用Promise异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明abilityType[AbilityType](#ZH-CN_TOPIC_0000002529444639__abilitytype)是辅助应用的类型。stateType[AbilityState](#ZH-CN_TOPIC_0000002529444639__abilitystate)是辅助应用的状态。

**返回值：**

类型说明Promise<Array<[AccessibilityAbilityInfo](#ZH-CN_TOPIC_0000002529444639__accessibilityabilityinfo)>>Promise对象，返回辅助应用信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**参数示例：**

辅助应用类型 \ 辅助应用状态enabledisableinstall**audible**查询已启用的具有听觉反馈的辅助应用查询已禁用的具有听觉反馈的辅助应用查询已安装的具有听觉反馈的辅助应用**generic**查询已启用的具有通用反馈的辅助应用查询已禁用的具有通用反馈的辅助应用查询已安装的具有通用反馈的辅助应用**haptic**查询已启用的具有触觉反馈的辅助应用查询已禁用的具有触觉反馈的辅助应用查询已安装的具有触觉反馈的辅助应用**spoken**查询已启用的具有语音反馈的辅助应用查询已禁用的具有语音反馈的辅助应用查询已安装的具有语音反馈的辅助应用**visual**查询已启用的具有视觉反馈的辅助应用查询已禁用的具有视觉反馈的辅助应用查询已安装的具有视觉反馈的辅助应用**all**查询所有已启用的辅助应用查询所有已禁用的辅助应用查询所有已安装的辅助应用

**查询所有已安装的辅助应用示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装

accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
});

// 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用
// 日志打印结果为：
// [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
// "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
// "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
// "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
// "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
// "announceForAccessibility","announceForAccessibilityNotInterrupt",
// "requestFocusForAccessibilityNotInterrupt","scrolling"],"targetBundleNames":[],"needHide":false}}]
```

**查询所有已启用的具有语音反馈的辅助应用示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型
let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用

accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo[]) => {
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
});
```

#### accessibility.getAccessibilityExtensionList9+

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState, callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

查询辅助应用列表，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明abilityType[AbilityType](#ZH-CN_TOPIC_0000002529444639__abilitytype)是辅助应用的类型。stateType[AbilityState](#ZH-CN_TOPIC_0000002529444639__abilitystate)是辅助应用的状态。callbackAsyncCallback<Array<[AccessibilityAbilityInfo](#ZH-CN_TOPIC_0000002529444639__accessibilityabilityinfo)>>是回调函数，返回辅助应用信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**参数示例：**

辅助应用类型 \ 辅助应用状态enabledisableinstall**audible**查询已启用的具有听觉反馈的辅助应用查询已禁用的具有听觉反馈的辅助应用查询已安装的具有听觉反馈的辅助应用**generic**查询已启用的具有通用反馈的辅助应用查询已禁用的具有通用反馈的辅助应用查询已安装的具有通用反馈的辅助应用**haptic**查询已启用的具有触觉反馈的辅助应用查询已禁用的具有触觉反馈的辅助应用查询已安装的具有触觉反馈的辅助应用**spoken**查询已启用的具有语音反馈的辅助应用查询已禁用的具有语音反馈的辅助应用查询已安装的具有语音反馈的辅助应用**visual**查询已启用的具有视觉反馈的辅助应用查询已禁用的具有视觉反馈的辅助应用查询已安装的具有视觉反馈的辅助应用**all**查询所有已启用的辅助应用查询所有已禁用的辅助应用查询所有已安装的辅助应用

**查询所有已安装的辅助应用示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装

accessibility.getAccessibilityExtensionList(abilityType, abilityState,(err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
  if (err) {
    console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
});

// 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用
// 日志打印结果为：
// [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
// "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
// "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
// "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
// "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
// "announceForAccessibility","announceForAccessibilityNotInterrupt",
// "requestFocusForAccessibilityNotInterrupt","scrolling"],"targetBundleNames":[],"needHide":false}}]
```

**查询所有已启用的具有语音反馈的辅助应用示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型
let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用

accessibility.getAccessibilityExtensionList(abilityType, abilityState,(err: BusinessError, data: accessibility.AccessibilityAbilityInfo[]) => {
  if (err) {
    console.error(`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
});
```

#### accessibility.getAccessibilityExtensionListSync12+

getAccessibilityExtensionListSync(abilityType: AbilityType, stateType: AbilityState): Array<AccessibilityAbilityInfo>

查询当前系统内辅助应用列表，支持按条件查询。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明abilityType[AbilityType](#ZH-CN_TOPIC_0000002529444639__abilitytype)是辅助应用的类型。stateType[AbilityState](#ZH-CN_TOPIC_0000002529444639__abilitystate)是辅助应用的状态。

**返回值：**

类型说明Array<[AccessibilityAbilityInfo](#ZH-CN_TOPIC_0000002529444639__accessibilityabilityinfo)>返回辅助应用信息列表。

**参数示例：**

辅助应用类型 \ 辅助应用状态enabledisableinstall**audible**查询已启用的具有听觉反馈的辅助应用查询已禁用的具有听觉反馈的辅助应用查询已安装的具有听觉反馈的辅助应用**generic**查询已启用的具有通用反馈的辅助应用查询已禁用的具有通用反馈的辅助应用查询已安装的具有通用反馈的辅助应用**haptic**查询已启用的具有触觉反馈的辅助应用查询已禁用的具有触觉反馈的辅助应用查询已安装的具有触觉反馈的辅助应用**spoken**查询已启用的具有语音反馈的辅助应用查询已禁用的具有语音反馈的辅助应用查询已安装的具有语音反馈的辅助应用**visual**查询已启用的具有视觉反馈的辅助应用查询已禁用的具有视觉反馈的辅助应用查询已安装的具有视觉反馈的辅助应用**all**查询所有已启用的辅助应用查询所有已禁用的辅助应用查询所有已安装的辅助应用

**查询所有已安装的辅助应用示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
let abilityState: accessibility.AbilityState = 'install'; // 辅助应用状态为已安装
let data: accessibility.AccessibilityAbilityInfo[];

try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
} catch (error) {
  let err = error as BusinessError;
  console.error(`error code: ${err.code}`);
}

// 例如：系统内安装一个包名为com.example.myaccessibilityapp的辅助应用
// 日志打印结果为：
// [{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
// "bundleName":"com.example.myaccessibilityapp","abilityTypes":[],
// "capabilities":["retrieve","gesture"],"description":"$string:MainAbility_desc",
// "eventTypes":["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
// "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
// "announceForAccessibility","announceForAccessibilityNotInterrupt",
// "requestFocusForAccessibilityNotInterrupt","scrolling"],"targetBundleNames":[],"needHide":false}}]
```

**查询所有已启用的具有语音反馈的辅助应用示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken'; // 辅助应用类型为具有语音反馈类型
let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已启用
let data: accessibility.AccessibilityAbilityInfo[];

try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  console.info(`Succeeded in get accessibility extension list, ${JSON.stringify(data)}`);
} catch (error) {
  let err = error as BusinessError;
  console.error(`error code: ${err.code}`);
}
```

**查询屏幕朗读是否开启示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let status: boolean = accessibility.isOpenAccessibilitySync();
console.info(`accessibilty status = ${status}`);
if (!status) {
  console.info(`screen reader not enable.`); // 屏幕朗读关闭
  return;
}

let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已使能
let data: accessibility.AccessibilityAbilityInfo[];
try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  if(data.length <= 0) {
    console.info(`screen reader not enable.`); // 屏幕朗读关闭
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info(`Succeeded in get accessibility extension, ${JSON.stringify(data[i])}`);
    if (data[i].bundleName == 'com.huawei.hmos.screenreader') {
      console.info(`screen reader is enabled.`); // 屏幕朗读开启
      return;
    }
  }
} catch (error) {
  let err = error as BusinessError;
  console.error(`error code: ${err.code}`);
}
```

#### accessibility.getCaptionsManager(deprecated)

getCaptionsManager(): CaptionsManager

获取无障碍字幕配置管理实例。

从API version 12开始废弃。系统不再开放相关功能。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Hearing

**返回值：**

类型说明[CaptionsManager](#ZH-CN_TOPIC_0000002529444639__captionsmanager8)无障碍字幕配置管理。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

let captionsManager = accessibility.getCaptionsManager();
```

#### accessibility.on('accessibilityStateChange')

on(type: 'accessibilityStateChange', callback: Callback<boolean>): void

监听辅助应用启用状态变化事件，使用callback异步回调。如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](#ZH-CN_TOPIC_0000002529444639__accessibilitygetaccessibilityextensionlistsync12)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明typestring是监听的事件名，固定为‘accessibilityStateChange’，即辅助应用启用状态变化事件。callbackCallback<boolean>是回调函数，在辅助应用启用状态变化时将状态通过此函数进行通知。此状态为全局辅助应用启用状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

// 系统内已安装一个或多个辅助应用时:
// 1. 启用辅助应用场景：第一个辅助应用启用后，回调函数会返回true
// 2. 禁用辅助应用场景：若一个或多个辅助应用已启用，最后一个已启用的辅助应用被禁用时，回调函数会返回false
accessibility.on('accessibilityStateChange', (data: boolean) => {
  console.info(`subscribe accessibility state change, result: ${JSON.stringify(data)}`);
});
```

**监听屏幕朗读是否开启示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onAccessibilityStateChangeListener = (state: boolean) : void => {
  if (!state) {
    console.info(`screen reader not enable.`); // 屏幕朗读关闭
    return;
  }
  let abilityType: accessibility.AbilityType = 'all'; // 辅助应用类型为所有类型
  let abilityState: accessibility.AbilityState = 'enable'; // 辅助应用状态为已使能
  let data: accessibility.AccessibilityAbilityInfo[];
  try {
    data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
    if(data.length <= 0) {
      console.info(`screen reader not enable.`); // 屏幕朗读关闭
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info(`Succeeded in get accessibility extension, ${JSON.stringify(data[i])}`);
      if (data[i].bundleName == 'com.huawei.hmos.screenreader') {
        console.info(`screen reader is enabled.`); // 屏幕朗读开启
        return;
      }
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(`error code: ${err.code}`);
  }
};

accessibility.on('accessibilityStateChange', onAccessibilityStateChangeListener);
```

#### accessibility.on('touchGuideStateChange')

on(type: 'touchGuideStateChange', callback: Callback<boolean>): void

监听触摸浏览功能启用状态变化事件，使用callback异步回调。如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](#ZH-CN_TOPIC_0000002529444639__accessibilitygetaccessibilityextensionlistsync12)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

参数名类型必填说明typestring是监听的事件名，固定为‘touchGuideStateChange’，即触摸浏览启用状态变化事件。callbackCallback<boolean>是回调函数，在触摸浏览启用状态变化时将状态通过此函数进行通知。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

// 系统内已安装一个或多个具备触摸浏览能力的辅助应用（Capability配置中含有'touchGuide'的辅助应用）时：
// 1. 启用触摸浏览辅助应用场景：第一个触摸浏览辅助应用启用后，回调函数会返回true
// 2. 禁用触摸浏览辅助应用场景：若一个或多个触摸浏览辅助应用已启用，最后一个已启用的触摸浏览辅助应用被禁用时，回调函数会返回false
accessibility.on('touchGuideStateChange', (data: boolean) => {
  console.info(`subscribe touch guide state change, result: ${JSON.stringify(data)}`);
});
```

#### accessibility.on('screenReaderStateChange')18+

on(type: 'screenReaderStateChange', callback: Callback<boolean>): void

监听屏幕朗读功能启用状态变化事件，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明typestring是监听的事件名，固定为‘screenReaderStateChange’，即屏幕朗读启用状态变化事件。callbackCallback<boolean>是回调函数，在屏幕朗读启用状态变化时将状态通过此函数进行通知。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

accessibility.on('screenReaderStateChange', (data: boolean) => {
  console.info(`subscribe screen reader state change, result: ${JSON.stringify(data)}`);
});
```

#### accessibility.on('touchModeChange')20+

on(type: 'touchModeChange', callback: Callback<string>): void

监听触摸浏览功能下的单击/双击操作模式变化事件，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明typestring是监听的事件名，固定为‘touchModeChange’，即触摸浏览功能下的单击/双击操作模式变化事件。callbackCallback<string>是回调函数，在触摸浏览功能下的单击/双击操作模式变化时将状态通过此函数进行通知。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (mode: string) => void = this.eventCallback;
  eventCallback(mode: string): void {
    console.info(`current touch mode: ${JSON.stringify(mode)}`);
  }

  aboutToAppear(): void {
    accessibility.on('touchModeChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

#### accessibility.off('accessibilityStateChange')

off(type: 'accessibilityStateChange', callback?: Callback<boolean>): void

取消监听辅助应用启用状态变化事件，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明typestring是取消监听的事件名，固定为‘accessibilityStateChange’，即辅助应用启用状态变化事件。callbackCallback<boolean>否回调函数，取消指定callback对象的事件响应。需与accessibility.on('accessibilityStateChange')的callback一致。缺省时，表示注销所有已注册事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

accessibility.off('accessibilityStateChange', (data: boolean) => {
  console.info(`Unsubscribe accessibility state change, result: ${JSON.stringify(data)}`);
});
```

#### accessibility.off('touchGuideStateChange')

off(type: 'touchGuideStateChange', callback?: Callback<boolean>): void

取消监听触摸浏览启用状态变化事件，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明typestring是取消监听的事件名，固定为‘touchGuideStateChange’，即触摸浏览启用状态变化事件。callbackCallback<boolean>否回调函数，取消指定callback对象的事件响应。需与accessibility.on('touchGuideStateChange')的callback一致。缺省时，表示注销所有已注册事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

accessibility.off('touchGuideStateChange', (data: boolean) => {
  console.info(`Unsubscribe touch guide state change, result: ${JSON.stringify(data)}`);
});
```

#### accessibility.off('screenReaderStateChange')18+

off(type: 'screenReaderStateChange', callback?: Callback<boolean>): void

取消监听屏幕朗读启用状态变化事件，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明typestring是取消监听的事件名，固定为‘screenReaderStateChange’，即屏幕朗读启用状态变化事件。callbackCallback<boolean>否回调函数，取消指定callback对象的事件响应。需与accessibility.on('screenReaderStateChange')的callback一致。缺省时，表示注销所有已注册事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

accessibility.off('screenReaderStateChange', (data: boolean) => {
  console.info(`Unsubscribe screen reader state change, result: ${JSON.stringify(data)}`);
});
```

#### accessibility.off('touchModeChange')20+

off(type: 'touchModeChange', callback?: Callback<string>): void

取消监听触摸浏览功能下的单击/双击操作模式变化事件，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明typestring是取消监听的事件名，固定为‘touchModeChange’，即触摸浏览功能下的单击/双击操作模式变化事件。callbackCallback<string>否回调函数，取消指定callback对象的事件响应。需与[accessibility.on('touchModeChange')](#ZH-CN_TOPIC_0000002529444639__accessibilityontouchmodechange20)的callback一致。缺省时，表示注销所有已注册事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (mode: string) => void = this.eventCallback;
  eventCallback(mode: string): void {
    console.info(`current touch mode: ${JSON.stringify(mode)}`);
  }

  aboutToAppear(): void {
    accessibility.on('touchModeChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('touchModeChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

#### accessibility.isOpenAccessibility(deprecated)

isOpenAccessibility(): Promise<boolean>

判断是否启用了辅助应用，使用Promise异步回调。

从API version 10开始废弃。

推荐使用[accessibility.isOpenAccessibilitySync](#ZH-CN_TOPIC_0000002529444639__accessibilityisopenaccessibilitysync10)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

类型说明Promise<boolean>Promise对象，如果辅助应用已启用，则返回 true；否则返回 false。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenAccessibility().then((data: boolean) => {
  console.info(`success data:isOpenAccessibility : ${JSON.stringify(data)}`)
}).catch((err: BusinessError) => {
  console.error(`failed to  isOpenAccessibility, Code is ${err.code}, message is ${err.message}`);
});
```

#### accessibility.isOpenAccessibility(deprecated)

isOpenAccessibility(callback: AsyncCallback<boolean>): void

判断是否启用了辅助应用，使用callback异步回调。

从API version 10开始废弃。

推荐使用[accessibility.isOpenAccessibilitySync](#ZH-CN_TOPIC_0000002529444639__accessibilityisopenaccessibilitysync10)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数，如果辅助应用已启用，则返回 true；否则返回 false。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenAccessibility((err: BusinessError, data: boolean) => {
  if (err) {
    console.error(`failed to isOpenAccessibility, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`success data:isOpenAccessibility : ${JSON.stringify(data)}`);
});
```

#### accessibility.isOpenAccessibilitySync10+

isOpenAccessibilitySync(): boolean

查询当前系统内是否存在已开启的辅助应用。如需获取系统内辅助应用信息，推荐使用[accessibility.getAccessibilityExtensionListSync](#ZH-CN_TOPIC_0000002529444639__accessibilitygetaccessibilityextensionlistsync12)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

类型说明boolean表示当前系统内是否有辅助应用开启。true表示启用了一个或多个辅助应用，false表示未启用任何辅助应用。当前系统内，屏幕朗读、滚动截屏、手写笔滚动批注和HiCar等功能启动时，此接口会返回true。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1、系统内已安装多个辅助应用，若都没有开启，返回false
// 2、系统内已安装多个辅助应用，若开启任意一个，返回true
let status: boolean = accessibility.isOpenAccessibilitySync();
```

#### accessibility.isOpenTouchGuide(deprecated)

isOpenTouchGuide(): Promise<boolean>

判断触摸浏览模式是否开启，使用Promise异步回调。

从API version 10开始废弃。

推荐使用[accessibility.isOpenTouchGuideSync](#ZH-CN_TOPIC_0000002529444639__accessibilityisopentouchguidesync10)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

类型说明Promise<boolean>Promise对象，如果触摸浏览模式已开启，则返回 true；否则返回 false。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenTouchGuide().then((data: boolean) => {
  console.info(`success data:isOpenTouchGuide : ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to  isOpenTouchGuide, Code is ${err.code}, message is ${err.message}`);
});
```

#### accessibility.isOpenTouchGuide(deprecated)

isOpenTouchGuide(callback: AsyncCallback<boolean>): void

判断触摸浏览模式是否开启，使用callback异步回调。

从API version 10开始废弃。

推荐使用[accessibility.isOpenTouchGuideSync](#ZH-CN_TOPIC_0000002529444639__accessibilityisopentouchguidesync10)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数，如果触摸浏览模式已开启，则返回 true；否则返回 false。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenTouchGuide((err: BusinessError, data: boolean) => {
  if (err) {
    console.error(`failed to isOpenTouchGuide, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`success data:isOpenTouchGuide : ${JSON.stringify(data)}`);
});
```

#### accessibility.isOpenTouchGuideSync10+

isOpenTouchGuideSync(): boolean

是否开启了触摸浏览模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

类型说明boolean表示是否开启了触摸浏览模式。true表示开启了触摸浏览，false表示未开启触摸浏览。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isOpenTouchGuideSync();
```

#### accessibility.isScreenReaderOpenSync18+

isScreenReaderOpenSync(): boolean

是否开启了屏幕朗读模式。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

类型说明boolean表示是否开启了屏幕朗读。true表示开启了屏幕朗读，false表示未开启屏幕朗读。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isScreenReaderOpenSync();
```

#### accessibility.sendEvent(deprecated)

sendEvent(event: EventInfo): Promise<void>

发送无障碍事件，使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。

推荐使用[accessibility.sendAccessibilityEvent()](#ZH-CN_TOPIC_0000002529444639__accessibilitysendaccessibilityevent9)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明event[EventInfo](#ZH-CN_TOPIC_0000002529444639__eventinfo)是无障碍事件对象。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo).then(() => {
  console.info(`Succeeded in send event,eventInfo is ${eventInfo}`);
}).catch((err: BusinessError) => {
  console.error(`failed to sendEvent, Code is ${err.code}, message is ${err.message}`);
});
```

#### accessibility.sendEvent(deprecated)

sendEvent(event: EventInfo, callback: AsyncCallback<void>): void

发送无障碍事件，使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。

推荐使用[accessibility.sendAccessibilityEvent()](#ZH-CN_TOPIC_0000002529444639__accessibilitysendaccessibilityevent9-1)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明event[EventInfo](#ZH-CN_TOPIC_0000002529444639__eventinfo)是辅助事件对象。callbackAsyncCallback<void>是回调函数，如果发送无障碍事件失败，则 AsyncCallback中err有数据返回。

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`failed to sendEvent, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in sendEvent, eventInfo is ${eventInfo}`);
});
```

#### accessibility.sendAccessibilityEvent9+

sendAccessibilityEvent(event: EventInfo): Promise<void>

发送无障碍事件，使用Promise异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明event[EventInfo](#ZH-CN_TOPIC_0000002529444639__eventinfo)是无障碍事件对象。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendAccessibilityEvent(eventInfo).then(() => {
  console.info(`Succeeded in send event,eventInfo is ${eventInfo}`);
}).catch((err: BusinessError) => {
  console.error(`failed to send event , Code is ${err.code}, message is ${err.message}`);
});
```

#### accessibility.sendAccessibilityEvent9+

sendAccessibilityEvent(event: EventInfo, callback: AsyncCallback<void>): void

发送无障碍事件，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明event[EventInfo](#ZH-CN_TOPIC_0000002529444639__eventinfo)是辅助事件对象。callbackAsyncCallback<void>是回调函数，如果发送无障碍事件失败，则 AsyncCallback中err有数据返回。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`failed to send event, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in send event, eventInfo is ${eventInfo}`);
});
```

**主动聚焦示例：**

```ets
@Entry
@Component
struct Index {

  build() {
    Column() {
      // 待聚焦组件添加id属性，id唯一性由使用者保证
      Button('待聚焦组件').id('click')
    }
  }
}
```

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'requestFocusForAccessibility',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'common',
  customId: 'click' // 对应待聚焦组件id属性值
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`failed to send event, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in send event, eventInfo is ${eventInfo}`);
});
```

**主动播报支持Resource示例18+：**

```ets
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'announceForAccessibility',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'common',
  textResourceAnnouncedForAccessibility: $r('app.string.ResourceName'),
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(`failed to send event, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in send event, eventInfo is ${eventInfo}`);
});
```

#### accessibility.getTouchModeSync20+

getTouchModeSync(): string

查询触摸浏览功能下的单击/双击操作模式。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

类型说明string

表示当前操作模式。

- singleTouchMode：表示单击操作模式。

- doubleTouchMode：表示双击操作模式。

- none：表示未开启触摸浏览功能。

```ets
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let touchMode: string = accessibility.getTouchModeSync();
    console.info(`current touch mode: ${JSON.stringify(touchMode)}`);
  }

  build() {
    Column() {
    }
  }
}
```