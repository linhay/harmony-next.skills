# @system.mediaquery (媒体查询)

提供根据不同媒体类型定义不同的样式。

- 从API Version 7 开始，该接口不再维护，推荐使用新接口[@ohos.mediaquery](../ohos/@ohos.mediaquery (媒体查询).md)。
- 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import mediaquery from '@system.mediaquery';
```

#### MediaQuery

定义MediaQuery接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### matchMedia

matchMedia(condition: string): MediaQueryList

根据媒体查询条件，创建MediaQueryList对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明conditionstring是用于查询的条件。

**返回值：**

类型说明[MediaQueryList](@system.mediaquery (媒体查询).md#ZH-CN_TOPIC_0000002497604808__mediaquerylist)表示创建MediaQueryList对象的属性，详情见下表说明。

**示例：**

```ets
let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');
```

#### MediaQueryEvent

定义MediaQuery事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明matchesboolean否否匹配结果。true表示满足查询条件，false表示不满足查询条件。

#### MediaQueryList

定义MediaQuery列表信息。

#### 属性

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明mediastring否是序列化媒体查询条件，该参数为只读。matchesboolean否是匹配结果。 true表示满足查询条件，false表示不满足查询条件。onchange(matches: boolean) => void否是匹配结果发生变化时的执行函数。matches表示是否匹配媒体查询条件，true满足查询条件，false不满足查询条件。

#### MediaQueryList.addListener

addListener(callback: (event: MediaQueryEvent) => void): void

给MediaQueryList添加回调函数，回调函数应在onShow生命周期之前添加，即需要在onInit或onReady生命周期里添加。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback(event: MediaQueryEvent) => void是匹配条件发生变化的响应函数。

**示例：**

```ets
import mediaquery, { MediaQueryEvent } from '@system.mediaquery';
let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');

function maxWidthMatch(e: MediaQueryEvent): void {
  if(e.matches){
    // do something
  }
}
mMediaQueryList.addListener(maxWidthMatch);
```

#### MediaQueryList.removeListener

removeListener(callback: (event: MediaQueryEvent) => void): void

移除MediaQueryList中的回调函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback(event: MediaQueryEvent) => void是匹配条件发生变化的响应函数。

**示例：**

```ets
import mediaquery, { MediaQueryEvent } from '@system.mediaquery';
let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');

function maxWidthMatch(e: MediaQueryEvent): void {
  if(e.matches){
    // do something
  }
}
mMediaQueryList.removeListener(maxWidthMatch);
```