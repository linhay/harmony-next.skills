# HalfScreenLaunchComponent

半屏嵌入式启动元服务组件，当被拉起方未授权嵌入式运行元服务时，宿主将使用跳出式拉起元服务。


该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

如果需要在该组件中实现一个可嵌入式运行的元服务时，元服务必须继承自[EmbeddableUIAbility](@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件).md)。若不继承自EmbeddableUIAbility，系统无法保证元服务功能正常。

#### 导入模块

```ets
import { HalfScreenLaunchComponent } from '@kit.ArkUI';
```

#### 子组件

无

#### 属性

不支持[通用属性]([通用属性](../misc/通用属性.md).md)

#### HalfScreenLaunchComponent

HalfScreenLaunchComponent({ content: Callback<void>, appId: string, options?: AtomicServiceOptions, onError?: ErrorCallback, onTerminated?: Callback<[TerminationInfo](EmbeddedComponent.md#ZH-CN_TOPIC_0000002497444946__terminationinfo)> })

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| content | Callback<void> | 是 | @BuilderParam | 组件显示内容。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| appId | string | 是 | - | 元服务appId。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| options | AtomicServiceOptions | 否 | - | 拉起元服务参数，默认为空。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| onError | ErrorCallback | 否 | - | 被拉起的元服务扩展在运行过程中发生异常时触发本回调。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| onTerminated | Callback<[TerminationInfo](EmbeddedComponent.md#ZH-CN_TOPIC_0000002497444946__terminationinfo)> | 否 | - | 回调函数，入参用于接收元服务的返回结果，类型为TerminationInfo。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| onReceive20+ | Callback<Record<string, Object>> | 否 | - | 被拉起的嵌入式运行元服务通过Window调用API时，触发本回调。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### 示例

该示例展示如何嵌入式拉起手机充值服务。

```ets
import { HalfScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  appId: string = "576****************"; // 元服务appId。

  build() {
    Column() {
      HalfScreenLaunchComponent({
        appId: this.appId,
        options: {},
        onTerminated:  (info:TerminationInfo)=> {
          console.info('onTerminated info = '+ info.want);
        },
        onError: (err) => {
          console.error(" onError code: " + err.code + ", message: ", err.message);
        },
        onReceive: (data) => {
          console.info("onReceive, data: " + data['ohos.atomicService.window']);
        }
      }) {
        Column() {
          Image($r('app.media.app_icon'))
          Text('拉起手机充值')
        }.width("80vp").height("80vp").margin({bottom:30})
      } // 通过尾随闭包形式传入content。
    }

  }
```
