# 日历选择器弹窗 (CalendarPickerDialog)

点击日期弹出日历选择器弹窗，可在弹窗内选择日期。

-

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](Class (UIContext).md)说明。

-

本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。

#### CalendarPickerDialog

#### show

static show(options?: CalendarDialogOptions): void

定义日历选择器弹窗。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | CalendarDialogOptions | 否 | 配置日历选择器弹窗参数。 |

#### CalendarDialogOptions对象说明

日历选择器弹窗选项。

继承自[CalendarOptions](CalendarPicker.md#ZH-CN_TOPIC_0000002553360761__calendaroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onAccept | [Callback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12)<Date> | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。 回调函数的参数表示选中的日期值。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onCancel | Void[Callback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12) | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onChange | [Callback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12)<Date> | 否 | 是 | 选择弹窗中日期使当前选中项改变时触发该回调。 回调函数的参数表示选中的日期值。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor) | 否 | 是 | 弹窗背板颜色。 默认值：Color.Transparent 说明： 当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| background[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)11+ | BlurStyle | 否 | 是 | 弹窗背板模糊材质。 默认值：BlurStyle.COMPONENT_ULTRA_THICK 说明： 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| background[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)Options19+ | [BackgroundBlurStyleOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](背景设置.md#ZH-CN_TOPIC_0000002529444791__backgroundeffectoptions11) | 否 | 是 | 背景效果参数。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。 说明： acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](选择器（Picker）公共接口.md#ZH-CN_TOPIC_0000002529444857__pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。 说明： acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | Void[Callback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12) | 否 | 是 | 弹窗弹出后的事件回调。 说明： 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。 4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | Void[Callback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12) | 否 | 是 | 弹窗消失后的事件回调。 说明： 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | Void[Callback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12) | 否 | 是 | 弹窗显示动效前的事件回调。 说明： 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | Void[Callback](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__callback12) | 否 | 是 | 弹窗退出动效前的事件回调。 说明： 1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。 2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowoptions对象说明) | [ShadowStyle](图像效果.md#ZH-CN_TOPIC_0000002497444856__shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。 当设备为2in1时，默认场景下，获焦时阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦时为ShadowStyle.OUTER_FLOATING_SM。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。 - true：响应悬停态。 - false：不响应悬停态。 默认值：false 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](半模态转场.md#ZH-CN_TOPIC_0000002497604850__hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。 默认值：HoverModeAreaType.BOTTOM_SCREEN 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| markToday19+ | boolean | 否 | 是 | 设置日历选择器弹窗中系统当前日期是否保持高亮显示。 - true：系统当前日期在日历选择器弹窗内保持高亮显示。 - false：系统当前日期在日历选择器弹窗内不保持高亮显示。 默认值：false 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |


在应用窗口缩小过程中，弹窗的宽度会被不断压缩，当缩小到一定程度时会导致其内容无法完整显示，保证CalendarPickerDialog内容能够完整显示的最小窗口宽度为386vp。

#### 示例

#### 示例1（设置弹窗背板）

该示例通过[CalendarDialogOptions](#ZH-CN_TOPIC_0000002522240884__calendardialogoptions对象说明)的backgroundColor、backgroundBlurStyle、shadow设置日历选择器弹窗背板。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-03-24');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            backgroundColor: Color.Gray,
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER_FLOATING_SM,
            onAccept: (value) => {
              // 点击弹窗中的“确定”按钮时触发该回调，value表示选中的日期值。
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            },
            onCancel: () => {
              // 点击弹窗中的“取消”按钮时触发该回调。
              console.info('calendar onCancel');
            },
            onChange: (value) => {
              // 选择弹窗中日期使当前选中项改变时触发该回调，value表示选中的日期值。
              console.info('calendar onChange:' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('calendar onDidAppear');
            },
            onDidDisappear: () => {
              console.info('calendar onDidDisappear');
            },
            onWillAppear: () => {
              console.info('calendar onWillAppear');
            },
            onWillDisappear: () => {
              console.info('calendar onWillDisappear');
            }
          });
        })
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205273.webp)

#### 示例2（自定义按钮样式）

从API version 12开始，该示例通过配置[CalendarDialogOptions](#ZH-CN_TOPIC_0000002522240884__calendardialogoptions对象说明)的acceptButtonStyle、cancelButtonStyle实现自定义日历选择器弹窗按钮样式。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date();

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            acceptButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: 'rgb(81, 81, 216)',
              fontSize: '26fp',
              fontWeight: FontWeight.Bolder,
              fontStyle: FontStyle.Normal,
              fontFamily: 'sans-serif',
              backgroundColor: '#A6ACAF',
              borderRadius: 20
            },
            cancelButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: Color.Blue,
              fontSize: '16fp',
              fontWeight: FontWeight.Normal,
              fontStyle: FontStyle.Italic,
              fontFamily: 'sans-serif',
              backgroundColor: '#50182431',
              borderRadius: 10
            },
            onAccept: (value) => {
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            }
          });
        })
    }.width('100%')
  }
```

#### 示例3（悬停态弹窗）

从API version 14开始，该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-04-23');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            onAccept: (value) => {
              console.info('calendar onAccept:' + JSON.stringify(value));
            },
            onCancel: () => {
              console.info('calendar onCancel');
            },
            onChange: (value) => {
              console.info('calendar onChange:' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('calendar onDidAppear');
            },
            onDidDisappear: () => {
              console.info('calendar onDidDisappear');
            },
            onWillAppear: () => {
              console.info('calendar onWillAppear');
            },
            onWillDisappear: () => {
              console.info('calendar onWillDisappear');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP_SCREEN,
          });
        })
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553365235.webp)

#### 示例4（设置日期选中态底板样式）

从API version 10开始，该示例通过[CalendarOptions](CalendarPicker.md#ZH-CN_TOPIC_0000002553360761__calendaroptions对象说明)的hintRadius设置日期选中态底板样式。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-04-23');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            hintRadius: 1,
            onAccept: (value) => {
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            }
          });
        })
    }.width('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245312.webp)

#### 示例5（设置开始日期和结束日期）

从API version 18开始，该示例通过[CalendarOptions](CalendarPicker.md#ZH-CN_TOPIC_0000002553360761__calendaroptions对象说明)的start和end设置日历选择器弹窗的开始日期和结束日期。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-01-01');
  private startDate: Date = new Date('2024-01-10');
  private endDate: Date = new Date('2025-01-10');

  build() {
    Column() {
      Text('月历日期选择器').fontSize(30)
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            start: this.startDate,
            end: this.endDate,
            selected: this.selectedDate,
          });
        })
    }.width('100%').margin({ top: 350 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205275.webp)

#### 示例6（设置系统当前日期在日历选择器弹窗内保持高亮显示，并设置禁用日期区间）

从API version 19开始，该示例通过配置[CalendarDialogOptions](#ZH-CN_TOPIC_0000002522240884__calendardialogoptions对象说明)的markToday，使系统当前日期在日历选择器弹窗内保持高亮显示，并通过配置[CalendarOptions](CalendarPicker.md#ZH-CN_TOPIC_0000002553360761__calendaroptions对象说明)的disabledDateRange设置禁用的日期区间。

```ets
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private disabledDateRange: DateRange[] = [
    { start: new Date('2025-01-01'), end: new Date('2025-01-02') },
    { start: new Date('2025-01-09'), end: new Date('2025-01-10') },
    { start: new Date('2025-01-15'), end: new Date('2025-01-16') },
    { start: new Date('2025-01-19'), end: new Date('2025-01-19') },
    { start: new Date('2025-01-22'), end: new Date('2025-01-25') }
  ];

  build() {
    Column() {
      Button("Show CalendarPicker Dialog")
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({ markToday: true, disabledDateRange: this.disabledDateRange });
        })
    }.width('100%').margin({ top: 350 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085320.webp)

#### 示例7（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](#ZH-CN_TOPIC_0000002522240884__calendardialogoptions对象说明)，实现自定义背景模糊效果。

```ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-08-05');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('Show CalendarPicker Dialog')
          .margin(20)
          .onClick(() => {
            CalendarPickerDialog.show({
              selected: this.selectedDate,
              hintRadius: 1,
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: [20, 20] },
              },
            });
          })
      }.width('100%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002553365237.webp)

#### 示例8（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](#ZH-CN_TOPIC_0000002522240884__calendardialogoptions对象说明)，实现自定义背景效果。

```ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-08-05');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('Show CalendarPicker Dialog')
          .margin(20)
          .onClick(() => {
            CalendarPickerDialog.show({
              selected: this.selectedDate,
              hintRadius: 1,
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundEffect: {
                radius: 60,
                saturation: 0,
                brightness: 1,
                color: Color.White,
                blurOptions: { grayscale: [20, 20] }
              },
            });
          })
      }.width('100%')
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245314.webp)