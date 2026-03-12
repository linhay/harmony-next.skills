# @ohos.mediaquery (媒体查询)

提供根据不同媒体类型定义不同的样式。

-

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

该模块不支持在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](zh-cn_topic_0000002529444749.html)说明。

#### 导入模块

```ets
import { mediaquery } from '@kit.ArkUI';
```

#### mediaquery.matchMediaSync(deprecated)

matchMediaSync(condition: string): MediaQueryListener

设置媒体查询的查询条件，并返回对应的监听句柄。

-

从API version 7开始支持，从API version 18开始废弃，建议使用[matchMediaSync](Class (MediaQuery).md#ZH-CN_TOPIC_0000002497444802__matchmediasync)替代。matchMediaSync需先通过[UIContext](Class (UIContext).md)中的[getMediaQuery](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getmediaquery)方法获取[MediaQuery](Class (MediaQuery).md)对象，然后通过该对象进行调用。

-

从API version 10开始，可以通过使用[UIContext](Class (UIContext).md)中的[getMediaQuery](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getmediaquery)方法获取当前UI上下文关联的[MediaQuery](Class (MediaQuery).md)对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明conditionstring是媒体事件的匹配条件，具体可参考[媒体查询语法规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query#语法规则)。

**返回值：**

类型说明[MediaQueryListener](#ZH-CN_TOPIC_0000002497604790__mediaquerylistener)媒体事件监听句柄，用于注册和去注册监听回调。

**示例：**

```ets
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); //监听横屏事件
```

#### MediaQueryListener

媒体查询的句柄，并包含了申请句柄时的首次查询结果。媒体查询根据设置的条件语句，比如'(width <= 600vp)'，比较系统信息，若首次查询时相关信息未初始化，matches返回false。

继承自[MediaQueryResult](#ZH-CN_TOPIC_0000002497604790__mediaqueryresult)。

**卡片能力：** 从API version 12开始，该类型支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### on('change')

on(type: 'change', callback: Callback<MediaQueryResult>): void

通过句柄向对应的查询条件注册回调，当媒体属性发生变更时会触发该回调。

注册的回调中不允许进一步调用on或off。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是必须填写字符串'change'。callbackCallback<[MediaQueryResult](#ZH-CN_TOPIC_0000002497604790__mediaqueryresult)>是向媒体查询注册的回调。

**示例：**

详见[off示例](#ZH-CN_TOPIC_0000002497604790__offchange)。

#### off('change')

off(type: 'change', callback?: Callback<MediaQueryResult>): void

通过句柄向对应的查询条件取消注册回调，当媒体属性发生变更时不再触发指定的回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是必须填写字符串'change'。callbackCallback<[MediaQueryResult](#ZH-CN_TOPIC_0000002497604790__mediaqueryresult)>否需要取消注册的回调，如果参数缺省则去注册该句柄下所有的回调。

**示例：**

```ets
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); //监听横屏事件
function onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // 注册回调
listener.off('change', onPortrait) // 取消注册回调
```

#### MediaQueryResult

用于执行媒体查询操作。

**卡片能力：** 从API version 12开始，该类型支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

名称类型只读可选说明matchesboolean是否是否符合匹配条件。true表示满足查询条件，false表示不满足查询条件。mediastring是否媒体事件的匹配条件。

#### 示例

推荐通过使用[UIContext](Class (UIContext).md)中的[getMediaQuery](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getmediaquery)方法获取当前UI上下文关联的[MediaQuery](Class (MediaQuery).md)对象。

```ets
import { mediaquery } from '@kit.ArkUI';

@Entry
@Component
struct MediaQueryExample {
  @State color: string = '#DB7093'
  @State text: string = 'Portrait'
  listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)'); //监听横屏事件，mediaquery.matchMediaSync接口已废弃，建议使用this.getUIContext().getMediaQuery().matchMediaSync()来获取

  onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
    if (mediaQueryResult.matches) {
      this.color = '#FFD700'
      this.text = 'Landscape'
    } else {
      this.color = '#DB7093'
      this.text = 'Portrait'
    }
  }

  aboutToAppear() {
    let portraitFunc = (mediaQueryResult: mediaquery.MediaQueryResult): void => this.onPortrait(mediaQueryResult)
    // 绑定回调函数
    this.listener.on('change', portraitFunc);
  }

  aboutToDisappear() {
    // 解绑listener中注册的回调函数
    this.listener.off('change');
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text(this.text).fontSize(24).fontColor(this.color)
    }
    .width('100%').height('100%')
  }
}
```