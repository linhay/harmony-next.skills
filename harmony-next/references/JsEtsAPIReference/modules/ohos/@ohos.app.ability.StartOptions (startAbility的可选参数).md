# @ohos.app.ability.StartOptions (startAbility的可选参数)

StartOptions可以作为启动UIAbility接口（例如[startAbility()](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__startability-1)）的入参，用于指定目标UIAbility启动时的选项，包括但不局限于窗口模式、目标UIAbility启动时所在的屏幕等。


-

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { StartOptions } from '@kit.AbilityKit';
```

#### StartOptions

StartOptions用于指定启动目标UIAbility时的选项。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowMode12+ | number | 否 | 是 | 启动UIAbility时的窗口模式，详见WindowMode。 |
| displayId | number | 否 | 是 | 屏幕ID，取值为大于等于-1的整数。 - 取值为-1，表示当前屏幕。 - 取值为0，表示主屏幕。 - 取值为正整数，表示指定ID的屏幕。 说明： 从API version 14开始，默认值是-1，即当前屏幕。 在API version 14之前版本，默认值为0，即主屏幕。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| withAnimation11+ | boolean | 否 | 是 | 启动UIAbility时是否具有动画效果。true表示具有动画效果，false表示不具有动画效果。 约束： 1.该功能仅在2in1和Tablet设备上生效。 2.调用方与目标方必须为同一应用。 |
| windowLeft11+ | number | 否 | 是 | 以指定displayId的屏幕的左顶点为原点，窗口在x轴方向偏移量，单位为px，值为正表示在原点右侧，值为负表示在原点左侧。该参数为整数，非整数将向下取整。当窗口左顶点超出指定displayId的屏幕区域时，限制窗口在指定displayId的屏幕范围内可见。配置该字段时，建议同时配置windowTop。 约束： 该功能仅在自由窗口状态下生效。 |
| windowTop11+ | number | 否 | 是 | 以指定displayId的屏幕的左顶点为原点，窗口在y轴方向偏移量，单位为px，值为正表示在原点下方，值为负表示在原点上方。该参数为整数，非整数将向下取整。当窗口顶部超出指定displayId的屏幕区域时，限制窗口在指定displayId的屏幕范围内可见。配置该字段时，建议同时配置windowLeft。 约束： 该功能仅在自由窗口状态下生效。 |
| windowWidth11+ | number | 否 | 是 | 窗口的宽度，单位为px。 取值范围为[minWindowWidth, maxWindowWidth]，取值范围单位为vp，可参考vp2px换算为对应的px值。 约束： 该功能仅在自由窗口状态下生效。 |
| windowHeight11+ | number | 否 | 是 | 窗口的高度，单位为px。 取值范围为[minWindowHeight, maxWindowHeight]，取值范围单位为vp，可参考vp2px换算为对应的px值。 约束： 该功能仅在自由窗口状态下生效。 |
| processMode12+ | contextConstant.ProcessMode | 否 | 是 | UIAbility启动后的进程模式。 约束： 1.该功能仅在2in1和Tablet设备上生效。 2.仅在[UIAbilityContext.startAbility](../../topics/misc/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-1)中生效。 3.processMode和startupVisibility必须同时设置。 |
| startupVisibility12+ | contextConstant.StartupVisibility | 否 | 是 | UIAbility启动后的可见性。当用户设置目标UIAbility为不可见时，目标UIAbility的窗口不会显示在前台，dock栏也不会有图标，同时目标UIAbility的onForeground生命周期不会被调用。 约束： 1.该功能仅在2in1和Tablet设备上生效。 2.仅在[UIAbilityContext.startAbility](../../topics/misc/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-1)中生效。 3.processMode和startupVisibility必须同时设置。 |
| startWindowIcon14+ | image.PixelMap | 否 | 是 | 启动当前应用的UIAbility时，启动页所显示的图标。如果未配置该字段，则默认采用module.json5文件中startWindowIcon字段的配置。 约束： - 启动其他应用的UIAbility时，该字段不生效。 - 该功能仅在2in1和Tablet设备上生效。 - 仅在[UIAbilityContext.startAbility](../../topics/misc/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-1)中生效。 - 图片数据大小限制为600MB。 |
| startWindowBackgroundColor14+ | string | 否 | 是 | 启动当前应用的UIAbility时，启动页所显示的背景颜色。固定为ARGB格式, 如：#E5FFFFFF。如果未配置该字段，则默认采用module.json5文件中startWindowBackground字段的配置。 约束： - 启动其他应用的UIAbility时，该字段不生效。 - 该功能仅在2in1和Tablet设备上生效。 - 仅在[UIAbilityContext.startAbility](../../topics/misc/UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startability-1)中生效。 |
| supportWindowModes14+ | Array<bundleManager.SupportWindowMode> | 否 | 是 | 启动UIAbility时，指定窗口是否显示最大化/窗口化/分屏按键。如果未配置该字段，则默认采用该UIAbility对应的module.json5配置文件中abilities标签的supportWindowMode字段取值。 - FULL_SCREEN：支持全屏模式。 - FLOATING：支持悬浮窗模式。 - SPLIT：支持分屏模式。通常需要配合FULL_SCREEN或FLOATING一起使用，不建议只配置SPLIT。当仅配置SPLIT时，2in1设备上的窗口默认为悬浮窗模式，支持进入分屏模式；Tablet设备上的窗口默认为全屏模式，支持进入分屏模式。 在自由窗口状态下同时配置FULL_SCREEN和SPLIT时，如果应用的targetAPIVersion小于15，窗口将以悬浮窗模式启动；如果应用的targetAPIVersion大于等于15，窗口将以全屏模式启动。 约束： 仅在2in1和tablet设备上生效。对于tablet设备，还需要在“自由多窗”模式下，该字段方可生效。 |
| minWindowWidth17+ | number | 否 | 是 | 窗口最小的宽度，单位为vp，可以通过getWindowLimitsVP获得当前窗口的尺寸限制。 约束： 该功能仅在自由窗口状态下生效。 |
| minWindowHeight17+ | number | 否 | 是 | 窗口最小的高度，单位为vp，可以通过getWindowLimitsVP获得当前窗口的尺寸限制。 约束： 该功能仅在自由窗口状态下生效。 |
| maxWindowWidth17+ | number | 否 | 是 | 窗口最大的宽度，单位为vp，可以通过getWindowLimitsVP获得当前窗口的尺寸限制。 约束： 该功能仅在自由窗口状态下生效。 |
| maxWindowHeight17+ | number | 否 | 是 | 窗口最大的高度，单位为vp，可以通过getWindowLimitsVP获得当前窗口的尺寸限制。 约束： 该功能仅在自由窗口状态下生效。 |
| completionHandler20+ | CompletionHandler | 否 | 是 | 拉起应用结果的操作类，用于处理拉起应用的结果。 元服务API：从API version 20开始，该接口支持在元服务中使用。 |
| hideStartWindow20+ | boolean | 否 | 是 | 启动当前应用的UIAbility时，控制是否隐藏窗口的启动页，true表示隐藏启动页，false表示不隐藏启动页。启动页介绍和规格详见StartWindow。 约束： 1.该功能仅在2in1设备和自由多窗模式下的Tablet设备上生效。 2.该功能仅在启动当前应用的UIAbility时生效。 |
| windowCreateParams20+ | window.WindowCreateParams | 否 | 是 | 启动UIAbility时的窗口参数。 |

**示例：**

```ets
import { UIAbility, Want, StartOptions, bundleManager, CompletionHandler } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    let completionHandler: CompletionHandler = {
      onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
        console.info(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}`);
      },
      onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
        console.error(`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}`);
      }
    };

    let color = new ArrayBuffer(512 * 512 * 4); // 创建一个ArrayBuffer对象，用于存储图像像素。该对象的大小为（height * width * 4）字节。
    let imagePixelMap: image.PixelMap;
    let windowParam: window.WindowCreateParams = {};
    let bufferArr = new Uint8Array(color);
    for (let i = 0; i < bufferArr.length; i += 4) {
      bufferArr[i] = 255;
      bufferArr[i+1] = 0;
      bufferArr[i+2] = 122;
      bufferArr[i+3] = 255;
    }
    image.createPixelMap(color, {
      editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 512, width: 512 }
    }).then((data) => {
      imagePixelMap = data;
      let options: StartOptions = {
        displayId: 0,
        startWindowIcon: imagePixelMap,
        startWindowBackgroundColor: '#E510FFFF',
        supportWindowModes: [
          bundleManager.SupportWindowMode.FULL_SCREEN,
          bundleManager.SupportWindowMode.SPLIT,
          bundleManager.SupportWindowMode.FLOATING
        ],
        minWindowWidth: 320,
        minWindowHeight: 240,
        maxWindowWidth: 2560,
        maxWindowHeight: 2560,
        completionHandler: completionHandler,
        hideStartWindow: true,
        windowCreateParams: windowParam
      };

      try {
        this.context.startAbility(want, options, (err: BusinessError) => {
          if (err.code) {
            // 处理业务逻辑错误
            console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
            return;
          }
          // 执行正常业务
          console.info('startAbility succeed');
        });
      } catch (err) {
        // 处理入参错误异常
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(`startAbility failed, code is ${code}, message is ${message}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`createPixelMap failed, code is ${err.code}, message is ${err.message}`);
    });
  }
```