# FunctionalButton（Button组件）

本模块提供FunctionalButton组件，为开发者提供场景化开发能力，包括：快速验证手机号、实时验证手机号、选择头像、打开授权设置页、打开App、选择收货地址、选择发票抬头、打开地图选点、实名信息校验、人脸核身、实况窗订阅、权限设置、服务动态授权码、元服务分享、反馈与投诉和获取手机号和风险等级。

FunctionalButton需要配合[functionalButtonComponentManager](functionalButtonComponentManager(场景化融合Button组件管理).md)一起使用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
```

#### FunctionalButton

场景化Button组件。

本模块提供FunctionalButton场景化Button组件，HarmonyOS应用和元服务通过集成Button组件完成相应功能。

Button组件需要[functionalButtonComponentManager](functionalButtonComponentManager(场景化融合Button组件管理).md)配合一起使用，完成相应功能。

**装饰器类型：**@Component

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| params | functionalButtonComponentManager.FunctionalButtonParams | 是 | @Prop | FunctionalButton组件参数。 |
| controller | functionalButtonComponentManager.FunctionalButtonController | 是 | - | FunctionalButton组件控制器，用来接收组件的点击事件。 |

#### build

build(): void

用于创建FunctionalButton对象的构造函数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**4.1.0(11)

**示例：**

```ets
import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // 声明FunctionalButton。
        FunctionalButton({
          params: {
            // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
            openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
            label: '快速验证手机号',
            // 调整按钮样式。
            styleOption: {
              bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
              size: functionalButtonComponentManager.SizeType.DEFAULT,
              plain: false,
              disabled:false,
              loading: false,
              hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
              hoverStartTime: 0,
              hoverStayTime: 0,
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onGetPhoneNumber((err, data) => {
              if (err) {
                // 错误日志处理。
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // 成功日志处理。
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // 获取授权码。
              let authorizationCode = data.code;
            })
      }.width('100%')
    }.height('100%')
  }
```