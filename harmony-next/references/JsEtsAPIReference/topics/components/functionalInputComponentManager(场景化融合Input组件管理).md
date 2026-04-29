# functionalInputComponentManager(场景化融合Input组件管理)

本模块提供[FunctionalInput](FunctionalInput（Input组件）.md)组件的逻辑管理，辅助HarmonyOS应用和元服务通过FunctionalInput组件完成快速拉起选择地区页面，供用户选择地区信息的功能。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**5.1.0(18)

#### 导入模块

```ets
import { functionalInputComponentManager } from '@kit.ScenarioFusionKit';
```

#### InputType

该枚举定义省市区选择器的功能类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECT_DISTRICT | 0 | 默认值为0，省市区选择器类型。 |

#### [FunctionalInput](FunctionalInput（Input组件）.md)Params

该接口定义了[FunctionalInput](FunctionalInput（Input组件）.md)组件的参数，包括省市区选择器的类型，样式，图标等。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputType | InputType | 否 | 否 | Input组件功能场景类型。默认值：SELECT_DISTRICT。 |
| textInputValue | TextInputOptions | 否 | 否 | TextInput组件无输入时的提示文本和文本内容。 |
| inputAttributeModifier | TextInputModifier | 否 | 是 | 设置组件的事件和属性。支持部分通用事件和通用属性，以及部分TextInput的事件和属性。 icon参数为空时，无默认值。icon参数不为空时，默认值为： padding({ top: 8, bottom: 8, left: 16, right: 48, }) 当设备是镜像语言时，默认值为 padding({ top: 8, bottom: 8, left: 48, right: 16, }) 说明： inputAttributeModifier参数失效的事件和属性： 事件：onFocus，onBlur，onClick，onKeyEvent，onKeyPreIme，onSubmit，onEditChange，onCopy，onCut，onPaste，onTextSelectionChange，onSecurityStateChange，onWillInsert，onDidInsert，onWillDelete，onDidDelete。 属性：focusable，tabIndex，defaultFocus，groupDefaultFocus，focusOnTouch，focusBox，type，enterKeyType，caretColor，copyOption，showPasswordIcon，selectedBackgroundColor，caretStyle，caretPosition，passwordIcon，enableKeyboardOnFocus，customKeyboard，passwordRules，selectAll，contentType，showPassword。 |
| icon | Resource | 否 | 是 | 设置组件显示图标，支持symbol和image两种类型。默认不显示图标。 |
| iconImgModifier | ImageModifier | 否 | 是 | 当“icon”设置为image时，可使用该参数进行图标的事件和样式设置。 iconImgModifier .size({ width: 24, height: 24 }) .margin({ start: 8, end: 16, }) |
| iconSymbolModifier | SymbolGlyphModifier | 否 | 是 | 当“icon”设置为symbol时，可使用该参数进行图标的事件和样式设置。 iconSymbolModifier .fontColor([$r('sys.color.ohos_id_color_fourth')]) .margin({ start: 8, end: 16 }) |

#### DistrictSelectResult

该接口定义了选择地区的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputContent | string | 否 | 否 | 返回选择的区域信息。格式为：省、市、区、街道。 |
| districtSelectResult | sceneMap.DistrictSelectResult | 否 | 否 | 返回区划选择的结果。 |

#### 事件

不支持通用事件，仅支持以下事件：

#### [FunctionalInput](FunctionalInput（Input组件）.md)Controller

[FunctionalInput](FunctionalInput（Input组件）.md)组件控制器，用来回调组件内部的点击事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：**5.1.0(18)

#### onSelectDistrict

onSelectDistrict(callback: AsyncCallback<DistrictSelectResult>): [FunctionalInput](FunctionalInput（Input组件）.md)Controller

注册[FunctionalInput](FunctionalInput（Input组件）.md)组件为区域选择的点击事件，使用callback异步回调。

该接口功能依赖Map Kit，参见[selectDistrict](sceneMap（场景化控件）.md#ZH-CN_TOPIC_0000002553202377__selectdistrict)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：**该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<DistrictSelectResult> | 是 | 回调函数。callback返回区划选择请求的结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalInput](FunctionalInput（Input组件）.md)Controller | FunctionalInput组件控制器。 |

**示例：**

```ets
import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { SymbolGlyphModifier, TextInputModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State inputContent: string = '';

  build() {
    Column() {
      Row() {
        Text('所在地区').width(64)
        // 声明FunctionalInput。
        FunctionalInput({
          params: {
            // InputType.SELECT_DISTRICT表示输入类型为省/市/区选择器类型。
            inputType: functionalInputComponentManager.InputType.SELECT_DISTRICT,
            textInputValue: {
              text: this.inputContent,
              placeholder: '省、市、区、街道地址',
            },
            // 调整TextInput样式。
            inputAttributeModifier: new TextInputModifier()
              .fontColor($r('sys.color.ohos_id_color_badge_red'))
              .onChange((value) => {
                if (value !== this.inputContent) {
                  this.inputContent = value;
                }
              }),
            // 将图标设置在末尾。
            icon: $r('sys.symbol.xmark'),
            // 设置符号图标的事件和样式。
            iconSymbolModifier: new SymbolGlyphModifier()
              .onClick(() => {
                this.inputContent = '';
              })
              .fontSize(32),
          },
          // 当InputType为SELECT_DISTRICT时，回调必须为onSelectDistrict。
          controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
            data: functionalInputComponentManager.DistrictSelectResult) => {
            if (err) {
              // 错误日志处理。
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
              return;
            }
            // 成功日志处理。
            hilog.info(0x0000, "testTag", "succeeded in selecting district");
            // 在输入组件中显示所选区域信息。
            this.inputContent = data.inputContent;
          })
          .layoutWeight(1)
      }.height('100%')
    }.width('100%')
  }
```