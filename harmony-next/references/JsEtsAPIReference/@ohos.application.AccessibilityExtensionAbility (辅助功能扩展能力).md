# @ohos.application.AccessibilityExtensionAbility (辅助功能扩展能力)

AccessibilityExtensionAbility基于ExtensionAbility框架，提供辅助功能业务的能力。

- 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';
```

#### AccessibilityExtensionAbility

AccessibilityExtensionAbility基于ExtensionAbility框架，提供辅助功能业务的能力。

#### 属性

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

名称类型只读可选说明context[AccessibilityExtensionContext](AccessibilityExtensionContext (辅助功能扩展上下文).md)否否表示辅助扩展能力上下文。

#### AccessibilityEvent

辅助事件信息。

#### 属性

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

名称类型只读可选说明eventType[accessibility.EventType](@ohos.accessibility (辅助应用).md#ZH-CN_TOPIC_0000002529444639__eventtype) | [accessibility.WindowUpdateType](@ohos.accessibility (辅助应用).md#ZH-CN_TOPIC_0000002529444639__windowupdatetype) | [TouchGuideType](#ZH-CN_TOPIC_0000002529284667__touchguidetype) | [GestureType](#ZH-CN_TOPIC_0000002529284667__gesturetype) | [PageUpdateType](#ZH-CN_TOPIC_0000002529284667__pageupdatetype)否否

具体事件类型。

EventType：无障碍事件类型；

WindowUpdateType：窗口变化类型；

TouchGuideType：触摸浏览事件类型；

GestureType：手势事件类型；

PageUpdateType：页面刷新类型。

target[AccessibilityElement](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__accessibilityelement9)否是发生事件的目标组件。timeStampnumber否是事件时间戳，单位是毫秒。默认值为0。elementId12+number否是主动聚焦的组件ID。默认值为0。textAnnouncedForAccessibility12+string否是主动播报的内容。当应用需要主动播报时根据实际场景设置播报内容，无特殊限制。extraInfo20+string否是针对TextArea、TextInput、SearchField、RichEdit组件，当文本内容有新增或删除时，携带的文本内容。根据实际场景设置，无特殊限制。

#### AccessibilityElement10+

type AccessibilityElement = _AccessibilityElement

表示无障碍节点元素，请参考[AccessibilityElement](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__accessibilityelement9)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明_AccessibilityElement表示无障碍节点元素，请参考[AccessibilityElement](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__accessibilityelement9)。

**示例：**

```ets
import { AccessibilityElement } from '@kit.AccessibilityKit';

let accessibilityElement: AccessibilityElement;
```

#### ElementAttributeValues10+

type ElementAttributeValues = _ElementAttributeValues

表示节点元素具备的属性名称及属性值类型信息，请参考[ElementAttributeValues](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__elementattributevalues)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明_ElementAttributeValues表示节点元素具备的属性名称及属性值类型信息，请参考[ElementAttributeValues](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__elementattributevalues)。

**示例：**

```ets
import { ElementAttributeValues } from '@kit.AccessibilityKit';

let elementAttributeValues: ElementAttributeValues;
```

#### FocusDirection10+

type FocusDirection = _FocusDirection

表示查询下一焦点元素的方向，请参考[FocusDirection](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__focusdirection)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明_FocusDirection表示查询下一焦点元素的方向，请参考[FocusDirection](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__focusdirection)。

**示例：**

```ets
import { FocusDirection } from '@kit.AccessibilityKit';

let focusDirection: FocusDirection;
```

#### ElementAttributeKeys10+

type ElementAttributeKeys = keyof ElementAttributeValues

表示[ElementAttributeValues](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__elementattributevalues)的属性名称。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明keyof [ElementAttributeValues](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__elementattributevalues)表示[ElementAttributeValues](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__elementattributevalues)中所有属性名组成的联合类型。

**示例：**

```ets
import { ElementAttributeKeys } from '@kit.AccessibilityKit';

let elementAttributeKeys: ElementAttributeKeys;
```

#### FocusType10+

type FocusType = _FocusType

表示查询焦点元素的类型，请参考[FocusType](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__focustype)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明_FocusType表示查询焦点元素的类型，请参考[FocusType](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__focustype)。

**示例：**

```ets
import { FocusType } from '@kit.AccessibilityKit';

let focusType: FocusType;
```

#### WindowType 10+

type WindowType = _WindowType

表示窗口的类型，请参考[WindowType](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__windowtype)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明_WindowType表示窗口的类型，请参考[WindowType](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__windowtype)。

**示例：**

```ets
import { WindowType } from '@kit.AccessibilityKit';

let windowType: WindowType;
```

#### Rect10+

type Rect = _Rect

表示矩形区域，请参考[Rect](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__rect)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明_Rect表示矩形区域，请参考[Rect](AccessibilityExtensionContext (辅助功能扩展上下文).md#ZH-CN_TOPIC_0000002529444641__rect)。

**示例：**

```ets
import { Rect } from '@kit.AccessibilityKit';

let rect: Rect;
```

#### AccessibilityExtensionContext10+

type AccessibilityExtensionContext = _AccessibilityExtensionContext.default

表示辅助功能扩展的上下文环境，请参考[AccessibilityExtensionContext](AccessibilityExtensionContext (辅助功能扩展上下文).md)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明_AccessibilityExtensionContext.default表示辅助功能扩展的上下文环境，请参考[AccessibilityExtensionContext](AccessibilityExtensionContext (辅助功能扩展上下文).md)。

**示例：**

```ets
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class EntryAbility extends AccessibilityExtensionAbility {
  onConnect(): void {
    let axContext = this.context;
  }
}
```

#### GestureType

type GestureType = 'left' | 'leftThenRight' | 'leftThenUp' | 'leftThenDown' | 'right' | 'rightThenLeft' | 'rightThenUp' | 'rightThenDown' | 'up' | 'upThenLeft' | 'upThenRight' | 'upThenDown' | 'down' | 'downThenLeft' | 'downThenRight' | 'downThenUp' | 'twoFingerSingleTap' | 'twoFingerDoubleTap' | 'twoFingerDoubleTapAndHold' | 'twoFingerTripleTap' | 'twoFingerTripleTapAndHold' | 'threeFingerSingleTap' | 'threeFingerDoubleTap' | 'threeFingerDoubleTapAndHold' | 'threeFingerTripleTap' | 'threeFingerTripleTapAndHold' | 'fourFingerSingleTap' | 'fourFingerDoubleTap' | 'fourFingerDoubleTapAndHold' | 'fourFingerTripleTap' | 'fourFingerTripleTapAndHold' | 'threeFingerSwipeUp' | 'threeFingerSwipeDown' | 'threeFingerSwipeLeft' | 'threeFingerSwipeRight' | 'fourFingerSwipeUp' | 'fourFingerSwipeDown' | 'fourFingerSwipeLeft' | 'fourFingerSwipeRight'

手势事件类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'left'表示向左的手势。'leftThenRight'表示先向左再向右的手势。'leftThenUp'表示先向左再向上的手势。'leftThenDown'表示先向左再向下的手势。'right'表示向右的手势。'rightThenLeft'表示先向右再向左的手势。'rightThenUp'表示先向右再向上的手势。'rightThenDown'表示先向右再向下的手势。'up'表示向上的手势。'upThenLeft'表示先向上再向左的手势。'upThenRight'表示先向上再向右的手势。'upThenDown'表示先向上再向下的手势。'down'表示向下的手势。'downThenLeft'表示先向下再向左的手势。'downThenRight'表示先向下再向右的手势。'downThenUp'表示先向下再向上的手势。'twoFingerSingleTap'11+表示双指单击的手势。'twoFingerDoubleTap'11+表示双指双击的手势。'twoFingerDoubleTapAndHold'11+表示双指双击长按的手势。'twoFingerTripleTap'11+表示双指三击的手势。'twoFingerTripleTapAndHold'11+表示双指三击长按的手势。'threeFingerSingleTap'11+表示三指单击的手势。'threeFingerDoubleTap'11+表示三指双击的手势。'threeFingerDoubleTapAndHold'11+表示三指双击长按的手势。'threeFingerTripleTap'11+表示三指三击的手势。'threeFingerTripleTapAndHold'11+表示三指三击长按的手势。'fourFingerSingleTap'11+表示四指单击的手势。'fourFingerDoubleTap'11+表示四指双击的手势。'fourFingerDoubleTapAndHold'11+表示四指双击长按的手势。'fourFingerTripleTap'11+表示四指三击的手势。'fourFingerTripleTapAndHold'11+表示四指三击长按的手势。'threeFingerSwipeUp'11+表示三指向上滑动的手势。'threeFingerSwipeDown'11+表示三指向下滑动的手势。'threeFingerSwipeLeft'11+表示三指向左滑动的手势。'threeFingerSwipeRight'11+表示三指向右滑动的手势。'fourFingerSwipeUp'11+表示四指向上滑动的手势。'fourFingerSwipeDown'11+表示四指向下滑动的手势。'fourFingerSwipeLeft'11+表示四指向左滑动的手势。'fourFingerSwipeRight'11+表示四指向右滑动的手势。

#### PageUpdateType

type PageUpdateType = 'pageContentUpdate' | 'pageStateUpdate'

页面刷新类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'pageContentUpdate'表示页面内容刷新。'pageStateUpdate'表示页面状态刷新。

#### TouchGuideType

type TouchGuideType = 'touchBegin' | 'touchEnd'

触摸浏览事件类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

类型说明'touchBegin'表示触摸浏览时开始触摸。'touchEnd'表示触摸浏览时结束触摸。

#### AccessibilityExtensionAbility.onConnect(deprecated)

onConnect(): void;

用户启用AccessibilityExtensionAbility时，系统服务完成连接后，回调此接口，可以该方法中执行初始化业务逻辑操作。该方法可以选择性重写。

从API version 12开始废弃。替代接口仅面向系统应用开放。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**示例：**

```ets
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onConnect(): void {
    console.info('AxExtensionAbility onConnect');
  }
}
```

#### AccessibilityExtensionAbility.onDisconnect(deprecated)

onDisconnect(): void;

用户停用AccessibilityExtensionAbility时，系统服务完成断开连接后，回调此接口，可以该方法中执行资源回收退出业务逻辑操作。该方法可以选择性重写。

从API version 12开始废弃。替代接口仅面向系统应用开放。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**示例：**

```ets
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onDisconnect(): void {
    console.info('AxExtensionAbility onDisconnect');
  }
}
```

#### AccessibilityExtensionAbility.onAccessibilityEvent(deprecated)

onAccessibilityEvent(event: AccessibilityEvent): void;

在关注的应用及事件类型对应的事件发生时回调此接口，可以在该方法中根据事件信息进行业务逻辑处理。一般情况下需要重写该方法完成业务。

从API version 12开始废弃。替代接口仅面向系统应用开放。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明event[AccessibilityEvent](#ZH-CN_TOPIC_0000002529284667__accessibilityevent)是无障碍事件。无返回值。

**示例：**

```ets
import { AccessibilityExtensionAbility, AccessibilityEvent } from '@kit.AccessibilityKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onAccessibilityEvent(event: AccessibilityEvent): void {
    console.info('AxExtensionAbility onAccessibilityEvent');
    if (event.eventType === 'click') {
      console.info('AxExtensionAbility onAccessibilityEvent: click');
    }
  }
}
```

#### AccessibilityExtensionAbility.onKeyEvent(deprecated)

onKeyEvent(keyEvent: KeyEvent): boolean;

在物理按键按下时回调此方法，可以在该方法中根据业务判断是否对事件进行拦截。

从API version 12开始废弃。替代接口仅面向系统应用开放。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

参数名类型必填说明keyEvent[KeyEvent](@ohos.multimodalInput.keyEvent (按键输入事件).md#ZH-CN_TOPIC_0000002529445533__keyevent)是按键事件回调函数。返回true表示拦截此按键。

**返回值：**

类型说明boolean

返回true表示此事件被消费，不会继续传递。

返回false表示此事件未被消费，会继续传递。

**示例：**

```ets
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';
import { KeyEvent } from '@kit.InputKit';

class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
  onKeyEvent(keyEvent: KeyEvent): boolean {
    console.info('AxExtensionAbility onKeyEvent');
    if (keyEvent.key.code === 16) {
      console.info('AxExtensionAbility onKeyEvent: intercept 16');
      return true;
    }
    return false;
  }
}
```