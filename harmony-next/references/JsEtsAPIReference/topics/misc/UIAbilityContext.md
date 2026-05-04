# UIAbilityContext

UIAbilityContext是[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)组件的上下文，继承自[Context](Context (Stage模型的上下文基类).md)。各类Context之间的关联与差异详见[应用上下文Context](../../guides/应用上下文Context.md)。

每个UIAbility组件实例化时，系统都会自动创建对应的UIAbilityContext。开发者可以通过UIAbilityContext获取组件信息AbilityInfo、获取应用信息ApplicationInfo、拉起其他UIAbility、连接系统服务、销毁UIAbility等。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 本模块接口仅可在Stage模型下使用。

- 在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的实例。

**导入模块**

```ets
import { common } from '@kit.AbilityKit';
```

**UIAbilityContext**

**属性**

系统能力：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityInfo | AbilityInfo | 否 | 否 | UIAbility的相关信息。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| currentHapModuleInfo | HapModuleInfo | 否 | 否 | 当前UIAbility所属HAP的信息。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| config | Configuration | 否 | 否 | 应用运行时的环境变量，如语言、颜色模式等。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| windowStage12+ | window.WindowStage | 否 | 否 | 当前WindowStage对象。仅支持在主线程调用。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |

**startAbility**

startAbility(want: Want, callback: AsyncCallback<void>): void

启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility的必要信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当接口调用成功，err中code为0，message为空字符串；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP_INSTANCE_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      this.context.startAbility(want, (err: BusinessError) => {
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
```

**startAbility**

startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void

启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility的必要信息。 |
| options | StartOptions | 是 | 启动UIAbility所携带的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当接口调用成功，err中code为0，message为空字符串；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not support. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000067 | The StartOptions check failed. |
| 16000068 | The ability is already running. |
| 16300003 | The target application is not the current application. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP_INSTANCE_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
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
```

**startAbility**

startAbility(want: Want, options?: StartOptions): Promise<void>

启动一个UIAbility。使用Promise异步回调。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility的必要信息。 |
| options | StartOptions | 否 | 启动UIAbility所携带的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not support. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000067 | The StartOptions check failed. |
| 16000068 | The ability is already running. |
| 16300003 | The target application is not the current application. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP_INSTANCE_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbility(want, options)
        .then(() => {
          // 执行正常业务
          console.info('startAbility succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbility failed, code is ${code}, message is ${message}`);
    }
```

**startAbilityForResult**

startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。仅支持在主线程调用。

UIAbility被启动后，有如下情况：

- 正常情况下可以通过调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身，并将结果返回给调用方。

- 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。

- 如果被启动的UIAbility是[单实例模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type#singleton启动模式)，且这个UIAbility被不同应用多次调用该接口启动，当这个UIAbility调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动Ability的必要信息。 |
| callback | AsyncCallback<AbilityResult> | 是 | 回调函数，当接口调用成功，err中code为0，data为被拉起方退出时的结果码和数据；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP_INSTANCE_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      this.context.startAbilityForResult(want, (err: BusinessError, result: common.AbilityResult) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('startAbilityForResult succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbilityForResult failed, code is ${code}, message is ${message}`);
    }
```

**startAbilityForResult**

startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。仅支持在主线程调用。

UIAbility被启动后，有如下情况：

- 正常情况下可以通过调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身，并将结果返回给调用方。

- 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。

- 如果被启动的UIAbility是[单实例模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type#singleton启动模式)，且这个UIAbility被不同应用多次调用该接口启动，当这个UIAbility调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动Ability的必要信息。 |
| options | StartOptions | 是 | 启动Ability所携带的参数。 |
| callback | AsyncCallback<AbilityResult> | 是 | 回调函数，当接口调用成功，err中code为0，data为被拉起方退出时的结果码和数据；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP_INSTANCE_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbilityForResult(want, options, (err: BusinessError, result: common.AbilityResult) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('startAbilityForResult succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbilityForResult failed, code is ${code}, message is ${message}`);
    }
```

**startAbilityForResult**

startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。仅支持在主线程调用。

UIAbility被启动后，有如下情况：

- 正常情况下可以通过调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身，并将结果返回给调用方。

- 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。

- 如果被启动的UIAbility是[单实例模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type#singleton启动模式)，且这个UIAbility被不同应用多次调用该接口启动，当这个UIAbility调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动Ability的必要信息。 |
| options | StartOptions | 否 | 启动Ability所携带的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，包含返回给拉起方的信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP_INSTANCE_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbilityForResult(want, options)
        .then((result: common.AbilityResult) => {
          // 执行正常业务
          console.info('startAbilityForResult succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbilityForResult failed, code is ${code}, message is ${message}`);
    }
```

**terminateSelf**

terminateSelf(callback: AsyncCallback<void>): void

销毁UIAbility自身。使用callback异步回调。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../../guides/module.json5配置文件.md#abilities标签)为true。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当销毁UIAbility自身成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

1.

使用terminateSelf接口停止UIAbility示例代码如下，默认情况下应用会在最近任务列表中保留快照。
```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
      this.context.terminateSelf((err: BusinessError) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('terminateSelf succeed');
      });
    } catch (err) {
      // 捕获同步的参数错误
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`terminateSelf failed, code is ${code}, message is ${message}`);
    }
```

1.

（可选）如果需要在停止UIAbility时，清理任务中心的相关任务（即不保留最近任务列表中的快照），需要在[module.json5](../../guides/module.json5配置文件.md)配置文件中将removeMissionAfterTerminate字段取值配置为true。
```ets
{
  "module": {
    // ...
    "abilities": [
      {
        // ...
        "removeMissionAfterTerminate": true
      }
    ]
  }
```

**terminateSelf**

terminateSelf(): Promise<void>

销毁UIAbility自身。使用Promise异步回调。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../../guides/module.json5配置文件.md#abilities标签)为true。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

1.

使用terminateSelf接口停止UIAbility示例代码如下，默认情况下应用会在最近任务列表中保留快照。
```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
      this.context.terminateSelf()
        .then(() => {
          // 执行正常业务
          console.info('terminateSelf succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 捕获同步的参数错误
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`terminateSelf failed, code is ${code}, message is ${message}`);
    }
```

1.

（可选）如果需要在停止UIAbility时，清理任务中心的相关任务（即不保留最近任务列表中的快照），需要在[module.json5](../../guides/module.json5配置文件.md)配置文件中将removeMissionAfterTerminate字段取值配置为true。
```ets
{
  "module": {
    // ...
    "abilities": [
      {
        // ...
        "removeMissionAfterTerminate": true
      }
    ]
  }
```

**terminateSelfWithResult**

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

销毁UIAbility自身。使用callback异步回调。仅支持在主线程调用。

仅当UIAbility通过[startAbilityForResult](#ZH-CN_TOPIC_0000002553200541__startabilityforresult)接口拉起时，调用terminateSelfWithResult接口销毁UIAbility，才会返回结果给调用方。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../../guides/module.json5配置文件.md#abilities标签)为true。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | AbilityResult | 是 | 返回给startAbilityForResult 接口调用方的相关信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当销毁UIAbility自身成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let resultCode = 100;
    // 返回给接口调用方AbilityResult信息
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };

    try {
      this.context.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('terminateSelfWithResult succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`terminateSelfWithResult failed, code is ${code}, message is ${message}`);
    }
```

**terminateSelfWithResult**

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

销毁UIAbility自身。使用Promise异步回调。仅支持在主线程调用。

仅当UIAbility通过[startAbilityForResult](#ZH-CN_TOPIC_0000002553200541__startabilityforresult)接口拉起时，调用terminateSelfWithResult接口销毁UIAbility，才会返回结果给调用方。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../../guides/module.json5配置文件.md#abilities标签)为true。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | AbilityResult | 是 | 返回给startAbilityForResult 接口调用方的信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let resultCode = 100;
    // 返回给接口调用方AbilityResult信息
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };

    try {
      this.context.terminateSelfWithResult(abilityResult)
        .then(() => {
          // 执行正常业务
          console.info('terminateSelfWithResult succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`terminateSelfWithResult failed, code is ${code}, message is ${message}`);
    }
```

**connectServiceExtensionAbility**

connectServiceExtensionAbility(want: Want, options: ConnectOptions): number

将当前UIAbility连接到一个[ServiceExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 连接ServiceExtensionAbility的Want信息。 |
| options | ConnectOptions | 是 | 回调对象，返回服务连接成功、连接失败、断开的信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，调用方可以通过disconnectServiceExtensionAbility传入该连接id来断开连接。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |

示例：

```ets
import { UIAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'ServiceExtensionAbility'
    };
    let commRemote: rpc.IRemoteObject;
    let options: common.ConnectOptions = {
      onConnect(elementName, remote) {
        commRemote = remote;
        console.info('onConnect...');
      },
      onDisconnect(elementName) {
        console.info('onDisconnect...');
      },
      onFailed(code) {
        console.info('onFailed...');
      }
    };
    let connection: number;

    try {
      connection = this.context.connectServiceExtensionAbility(want, options);
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`connectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**disconnectServiceExtensionAbility**

disconnectServiceExtensionAbility(connection: number): Promise<void>

断开与[ServiceExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。仅支持在主线程调用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识id，即connectServiceExtensionAbility返回的connectionId。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    // connection为connectServiceExtensionAbility中的返回值
    let connection = 1;
    let commRemote: rpc.IRemoteObject | null;

    try {
      this.context.disconnectServiceExtensionAbility(connection).then(() => {
        commRemote = null;
        // 执行正常业务
        console.info('disconnectServiceExtensionAbility succeed');
      }).catch((err: BusinessError) => {
        // 处理业务逻辑错误
        console.error(`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      commRemote = null;
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**disconnectServiceExtensionAbility**

disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void

断开与[ServiceExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用callback异步回调。仅支持在主线程调用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识id，即connectServiceExtensionAbility返回的connectionId。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开与ServiceExtensionAbility的连接成功，err为undefined；否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    // connection为connectServiceExtensionAbility中的返回值
    let connection = 1;
    let commRemote: rpc.IRemoteObject | null;

    try {
      this.context.disconnectServiceExtensionAbility(connection, (err: BusinessError) => {
        commRemote = null;
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('disconnectServiceExtensionAbility succeed');
      });
    } catch (err) {
      commRemote = null;
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**startAbilityByCall**

startAbilityByCall(want: Want): Promise<Caller>

该接口用于获取[Caller](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__caller)通信对象，以便于与[Callee](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__callee)进行通信。如果指定UIAbility未启动，则会将UIAbility启动至前台或后台。使用Promise异步回调。仅支持在主线程调用。

该接口不支持拉起启动模式为[specified模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type#specified启动模式)的UIAbility。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

跨设备场景下，调用方与目标方必须为同一应用。

-

同设备场景下，要求调用方与目标方为不同应用，且调用方具备ohos.permission.ABILITY_BACKGROUND_COMMUNICATION权限（该权限仅系统应用可申请）。

-

此外如果应用需要在后台调用该接口，需要具备ohos.permission.START_ABILITIES_FROM_BACKGROUND（该权限仅系统应用可申请）。更多的组件启动规则详见[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

需要权限：ohos.permission.DISTRIBUTED_DATASYNC

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

API version 10及之前版本，需申请ohos.permission.ABILITY_BACKGROUND_COMMUNICATION（该权限仅系统应用可用）。

-

API version 11开始，仅需申请ohos.permission.DISTRIBUTED_DATASYNC（该权限仅当执行应用间建链操作时由软总线实施权限校验，在应用拉起阶段不做校验）。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 传入需要启动的UIAbility信息，包含abilityName、moduleName、bundleName、deviceId、parameters（可选）。将parameters中的'ohos.aafwk.param.callAbilityToForeground'配置为true可将UIAbility拉起到前台；否则表示将UIAbility拉起到后台。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Caller> | Promise对象，获取要通讯的caller对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed. 2.Sending restart message to system service failed. 3.System service failed to communicate with dependency module. 4.Non-system applications are only allowed to call this interface across devices, not on the current device. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP_INSTANCE_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |

示例：

下面代码展示的是，调用方启动目标方到后台，获取Caller成功后发消息到目标方，然后释放Caller对象。

```ets
import { Caller, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rpc } from '@kit.IPCKit';

const DOMAIN = 0x0000;
const LOG_TAG = 'TEST_TAG';

class TestParcelable implements rpc.Parcelable {
  age: number = 0;
  name: string = '';
  marshalling(dataOut: rpc.MessageSequence): boolean {
    dataOut.writeInt(this.age);
    dataOut.writeString(this.name);
    return true;
  }
  unmarshalling(dataIn: rpc.MessageSequence): boolean {
    this.age = dataIn.readInt();
    this.name = dataIn.readString();
    return true;
  }

export default class EntryAbility extends UIAbility {
  async onForeground() {
    let caller: Caller;
    // 后台启动Ability
    let wantBackground: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
    };

    try {
      caller = await this.context.startAbilityByCall(wantBackground);
      await caller.call('TEST_CALL', new TestParcelable());
      caller.release();
    } catch (err) {
      // 处理入参错误异常
      hilog.error(DOMAIN, LOG_TAG, `startAbilityByCall failed ${err}`);
    }
```

下面代码展示，目标方启动后注册监听，销毁时取消监听。

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rpc } from '@kit.IPCKit';

const DOMAIN = 0x0000;
const LOG_TAG = 'TEST_TAG';

class TestParcelable implements rpc.Parcelable {
  age: number = 0;
  name: string = '';
  marshalling(dataOut: rpc.MessageSequence): boolean {
    dataOut.writeInt(this.age);
    dataOut.writeString(this.name);
    return true;
  }
  unmarshalling(dataIn: rpc.MessageSequence): boolean {
    this.age = dataIn.readInt();
    this.name = dataIn.readString();
    return true;
  }

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, LOG_TAG, '%{public}s', 'Ability onCreate');
    // 注册监听
    this.callee.on('TEST_CALL', (data: rpc.MessageSequence) => {
      let recv = new TestParcelable();
      data.readParcelable(recv);
      recv.age++;
      return recv;
    });
  }

  onDestroy(): void {
    hilog.info(DOMAIN, LOG_TAG, '%{public}s', 'Ability onDestroy');
    // 取消监听
    this.callee.off('TEST_CALL');
  }
```

下面代码展示，调用方启动目标方到前台场景。

```ets
import { Caller, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const LOG_TAG = 'TEST_TAG';

export default class EntryAbility extends UIAbility {
  async onForeground() {
    let caller: Caller;
    // 启动UIAbility到前台，将parameters中的'ohos.aafwk.param.callAbilityToForeground'配置为true
    let wantForeground: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      parameters: {
        'ohos.aafwk.param.callAbilityToForeground': true
      }
    };

    try {
      caller = await this.context.startAbilityByCall(wantForeground);
      caller.release();
    } catch (err) {
      // 处理入参错误异常
      hilog.error(DOMAIN, LOG_TAG, `startAbilityByCall failed ${err}`);
    }
```

**setMissionLabel**

setMissionLabel(label: string, callback: AsyncCallback<void>): void

设置UIAbility在多任务界面中显示的名称。使用callback异步回调。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 任务的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当设置UIAbility在多任务界面中显示的名称成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.setMissionLabel('test', (result: BusinessError) => {
      console.info(`setMissionLabel: ${JSON.stringify(result)}`);
    });
  }
```

**setMissionLabel**

setMissionLabel(label: string): Promise<void>

设置UIAbility在多任务界面中显示的名称。使用Promise异步回调。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 任务的名称。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.setMissionLabel('test').then(() => {
      console.info('success');
    }).catch((err: BusinessError) => {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`setMissionLabel failed, code is ${code}, message is ${message}`);
    });
  }
```

**setMissionContinueState10+**

setMissionContinueState(state: AbilityConstant.ContinueState, callback: AsyncCallback<void>): void

设置UIAbility任务的流转状态。使用callback异步回调。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | AbilityConstant.ContinueState | 是 | 流转状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当设置UIAbility任务的流转状态成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

错误码：

错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result: BusinessError) => {
      console.info(`setMissionContinueState: ${JSON.stringify(result)}`);
    });
  }
```

**setMissionContinueState10+**

setMissionContinueState(state: AbilityConstant.ContinueState): Promise<void>

设置UIAbility任务的流转状态。使用Promise异步回调。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | AbilityConstant.ContinueState | 是 | 流转状态。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE).then(() => {
      console.info('success');
    }).catch((err: BusinessError) => {
      console.error(`setMissionContinueState failed, code is ${err.code}, message is ${err.message}`);
    });
  }
```

**restoreWindowStage**

restoreWindowStage(localStorage: LocalStorage): void

恢复UIAbility中的WindowStage数据。仅支持在主线程调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localStorage | LocalStorage | 是 | 用于恢复window stage的存储数据。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let storage = new LocalStorage();
    this.context.restoreWindowStage(storage);
  }
```

**isTerminating**

isTerminating(): boolean

查询UIAbility是否处于消亡中状态。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否处于消亡中状态。true表示处于消亡中状态，false表示不处于消亡中状态。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let isTerminating: boolean = this.context.isTerminating();
    console.info(`ability state is ${isTerminating}`);
  }
```

**requestDialogService**

requestDialogService(want: Want, result: AsyncCallback<dialogRequest.RequestResult>): void

启动一个支持模态弹框的ServiceExtensionAbility。ServiceExtensionAbility被启动后，应用弹出模态弹框，通过调用[setRequestResult](@ohos.app.ability.dialogRequest (dialogRequest模块).md#ZH-CN_TOPIC_0000002522240558__requestcallbacksetrequestresult)接口返回结果给调用者。使用callback异步回调。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动ServiceExtensionAbility的Want信息。 |
| result | AsyncCallback<dialogRequest.RequestResult> | 是 | 回调函数，当启动一个支持模态弹框的ServiceExtensionAbility成功，err中code为0，data为模态弹框请求结果；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want, dialogRequest } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AuthAccountServiceExtension'
    };

    try {
      this.context.requestDialogService(want, (err: BusinessError, result: dialogRequest.RequestResult) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`requestDialogService failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info(`requestDialogService succeed, result = ${JSON.stringify(result)}`);
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`requestDialogService failed, code is ${code}, message is ${message}`);
    }
```

**requestDialogService**

requestDialogService(want: Want): Promise<dialogRequest.RequestResult>

启动一个支持模态弹框的ServiceExtensionAbility。ServiceExtensionAbility被启动后，应用弹出模态弹框，通过调用[setRequestResult](@ohos.app.ability.dialogRequest (dialogRequest模块).md#ZH-CN_TOPIC_0000002522240558__requestcallbacksetrequestresult)接口返回结果给调用者。使用Promise异步回调。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动ServiceExtensionAbility的Want信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<dialogRequest.RequestResult> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, Want, dialogRequest } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'AuthAccountServiceExtension'
    };

    try {
      this.context.requestDialogService(want)
        .then((result: dialogRequest.RequestResult) => {
          // 执行正常业务
          console.info(`requestDialogService succeed, result = ${JSON.stringify(result)}`);
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`requestDialogService failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`requestDialogService failed, code is ${code}, message is ${message}`);
    }
```

**reportDrawnCompleted10+**

reportDrawnCompleted(callback: AsyncCallback<void>): void

用于通知系统UIAbility对应的窗口内容已经绘制完成。使用callback异步回调。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当通知系统UIAbility对应的窗口内容已经绘制完成的操作成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        return;
      }

      try {
        this.context.reportDrawnCompleted((err) => {
          if (err.code) {
            // 处理业务逻辑错误
            console.error(`reportDrawnCompleted failed, code is ${err.code}, message is ${err.message}`);
            return;
          }
          // 执行正常业务
          console.info('reportDrawnCompleted succeed');
        });
      } catch (err) {
        // 捕获同步的参数错误
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(`reportDrawnCompleted failed, code is ${code}, message is ${message}`);
      }
    });
    console.info("MainAbility onWindowStageCreate");
  }
};
```

**startAbilityByType11+**

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>) : void

通过type隐式启动[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)。使用callback异步回调。仅支持在主线程调用，仅支持处于前台的应用调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 启动的UIExtensionAbility类型，取值详见通过startAbilityByType接口拉起垂类面板。 |
| wantParam | Record<string, Object> | 是 | 表示扩展参数。 |
| abilityStartCallback | AbilityStartCallback | 是 | 回调函数，返回启动失败后的详细错误信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当接口调用成功，err为undefined；否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, common } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let wantParam: Record<string, Object> = {
      'time': '2023-10-23 20:45'
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.info(`code:` + code + `name:` + name + `message:` + message);
      },
      onResult: (abilityResult: common.AbilityResult) => {
        console.info(`resultCode:` + abilityResult.resultCode + `bundleName:` + abilityResult.want?.bundleName);
      }
    };

    this.context.startAbilityByType("photoEditor", wantParam, abilityStartCallback, (err) => {
      if (err) {
        console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
      } else {
        console.info(`success`);
      }
    });
  }
```

**startAbilityByType11+**

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback) : Promise<void>

通过type隐式启动[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)。使用Promise异步回调。仅支持在主线程调用，仅支持处于前台的应用调用。

元服务API：从API version 11开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 启动的UIExtensionAbility类型，取值详见通过startAbilityByType接口拉起垂类面板。 |
| wantParam | Record<string, Object> | 是 | 表示扩展参数。 |
| abilityStartCallback | AbilityStartCallback | 是 | 回调函数，返回启动失败后的详细错误信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let wantParam: Record<string, Object> = {
      'time': '2023-10-23 20:45'
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.info(`code:` + code + `name:` + name + `message:` + message);
      },
      onResult: (abilityResult: common.AbilityResult) => {
        console.info(`resultCode:` + abilityResult.resultCode + `bundleName:` + abilityResult.want?.bundleName);
      }
    };

    this.context.startAbilityByType("photoEditor", wantParam, abilityStartCallback).then(() => {
      console.info(`startAbilityByType success`);
    }).catch((err: BusinessError) => {
      console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
    });
  }
```

**showAbility12+**

showAbility(): Promise<void>

显示当前UIAbility。使用Promise异步回调。仅支持在主线程调用。

调用此接口前要求确保应用已添加至状态栏。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not support. |
| 16000050 | Internal error. |
| 16000067 | The StartOptions check failed. |

示例：

```ets
// Index.ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State showAbility: string = 'showAbility'

  build() {
    Row() {
      Column() {
        Text(this.showAbility)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

            context.showAbility().then(() => {
              console.info(`showAbility success`);
            }).catch((err: BusinessError) => {
              console.error(`showAbility fail, err: ${JSON.stringify(err)}`);
            });
      }
      .width('100%')
    }
    .height('100%')
  }
```

```ets
// EntryAbility.ts
import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
      processMode: contextConstant.ProcessMode.NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM,
      startupVisibility: contextConstant.StartupVisibility.STARTUP_SHOW
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
```

**hideAbility12+**

hideAbility(): Promise<void>

隐藏当前UIAbility。使用Promise异步回调。仅支持在主线程调用。

调用此接口前要求确保应用已添加至状态栏。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not support. |
| 16000050 | Internal error. |
| 16000067 | The StartOptions check failed. |

示例：

```ets
// Index.ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State hideAbility: string = 'hideAbility'

  build() {
    Row() {
      Column() {
        Text(this.hideAbility)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

            context.hideAbility().then(() => {
              console.info(`hideAbility success`);
            }).catch((err: BusinessError) => {
              console.error(`hideAbility fail, err: ${JSON.stringify(err)}`);
            });
      }
      .width('100%')
    }
    .height('100%')
  }
```

```ets
// EntryAbility.ts
import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
      processMode: contextConstant.ProcessMode.NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM,
      startupVisibility: contextConstant.StartupVisibility.STARTUP_HIDE
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
```

**moveAbilityToBackground12+**

moveAbilityToBackground(): Promise<void>

将处于前台的UIAbility移动到后台。使用Promise异步回调。仅支持在主线程调用。

该接口仅支持手机和平板设备。

元服务API：从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：

- 从API version 12开始，该接口仅在Phone、Wearable和TV设备中可正常调用，在其他设备上返回16000061错误码。

- 从API version 13开始，该接口仅在Phone、Tablet、Wearable和TV设备中可正常调用，在其他设备上返回16000061错误码。

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000061 | Operation not supported. |
| 16000065 | The API can be called only when the ability is running in the foreground. |
| 16000066 | An ability cannot switch to the foreground or background in Wukong mode. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State moveAbilityToBackground: string = 'Move To Background'

  build() {
    Row() {
      Column() {
        Text(this.moveAbilityToBackground)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

            context.moveAbilityToBackground().then(() => {
              console.info(`moveAbilityToBackground success.`);
            }).catch((err: BusinessError) => {
              console.info(`moveAbilityToBackground error: ${JSON.stringify(err)}.`);
            });
      }
      .width('100%')
    }
    .height('100%')
  }
```

**openAtomicService12+**

openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>

启动一个独立窗口的元服务。使用Promise异步回调。仅支持在主线程调用。

元服务被启动后，有如下情况：

- 正常情况下元服务可以通过[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身，并且返回结果给调用方。

- 异常情况下比如杀死元服务会返回异常结果给调用方，异常结果的resultCode为-1。

- 如果不同应用多次调用该接口启动同一个元服务，当这个元服务调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方, 其它调用方返回异常结果，异常结果中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的唯一标识，由云端统一分配。 |
| options | AtomicServiceOptions | 否 | 启动元服务所携带的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，包含返回给拉起方的信息。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000002 | Incorrect ability type. |
| 16000003 | The specified ID does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

示例：

```ets
import { UIAbility, common, AtomicServiceOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let appId: string = '6918661953712445909';
    let options: AtomicServiceOptions = {
      displayId: 0
    };

    try {
      this.context.openAtomicService(appId, options)
        .then((result: common.AbilityResult) => {
          // 执行正常业务
          console.info('openAtomicService succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`openAtomicService failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`openAtomicService failed, code is ${code}, message is ${message}`);
    }
```

**openLink12+**

openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>

通过[App Linking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup)或[Deep Linking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup)方式启动UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。仅支持在主线程调用。

通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标UIAbility。目标方必须同时具备以下过滤器特征，才能处理App Linking链接：

- "actions"列表中包含"ohos.want.action.viewData"。

- "entities"列表中包含"entity.system.browsable"。

- "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。

如果希望获取被拉起方终止后的结果，可以设置callback参数，此参数的使用可参照[startAbilityForResult](#ZH-CN_TOPIC_0000002553200541__startabilityforresult)接口。

传入的参数不合法时，如未设置必选参数或link字符串不是标准格式的URL，接口会直接抛出异常。参数校验通过，拉起目标方时出现的错误通过promise返回错误信息。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| link | string | 是 | 指示要打开的标准格式URL。 |
| options | OpenLinkOptions | 否 | 打开URL的选项参数。 |
| callback | AsyncCallback<AbilityResult> | 否 | 回调函数，包含返回给拉起方的信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16200001 | The caller has been released. |
| 16000053 | The ability is not on the top of the UI. |
| 16000136 | The UIAbility is prohibited from launching itself via App Linking. |

示例：

```ets
import { common, OpenLinkOptions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0xeeee;
const TAG: string = '[openLinkDemo]';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("Call StartAbilityForResult")
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let link: string = 'https://www.example.com';
          let openLinkOptions: OpenLinkOptions = {
            appLinkingOnly: true,
            parameters: { demo_key: 'demo_value' }
          };

          try {
            context.openLink(
              link,
              openLinkOptions,
              (err, result) => {
                hilog.error(DOMAIN, TAG, `openLink callback error.code: ${JSON.stringify(err)}`);
                hilog.info(DOMAIN, TAG, `openLink callback result: ${JSON.stringify(result.resultCode)}`);
                hilog.info(DOMAIN, TAG, `openLink callback result data: ${JSON.stringify(result.want)}`);
              }
            ).then(() => {
              hilog.info(DOMAIN, TAG, `open link success.`);
            }).catch((err: BusinessError) => {
              hilog.error(DOMAIN, TAG, `open link failed, errCode ${JSON.stringify(err.code)}`);
            });
          }
          catch (e) {
            hilog.error(DOMAIN, TAG, `exception occured, errCode ${JSON.stringify(e.code)}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

**backToCallerAbilityWithResult12+**

backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>

当通过[startAbilityForResult](#ZH-CN_TOPIC_0000002553200541__startabilityforresult)或[openLink](#ZH-CN_TOPIC_0000002553200541__openlink12)拉起目标方UIAbility，且需要目标方返回结果时，目标方可以通过该接口将结果返回并拉起调用方。与[terminateSelfWithResult](#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)不同的是，本接口在返回时不会销毁当前UIAbility。使用Promise异步回调。

元服务API：从API version 12开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityResult | AbilityResult | 是 | 包含目标方返回给拉起方的结果。 |
| requestCode | string | 是 | 通过startAbilityForResult或openLink拉起目标方Ability且需要目标方返回结果时，系统生成的用于标识本次调用的requestCode。该值可以通过want中的CALLER_REQUEST_CODE字段获取。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000074 | The caller does not exist. |
| 16000075 | BackToCaller is not supported. |

示例：

调用方通过startAbilityForResult接口拉起目标方, 目标方再调用backToCallerAbilityWithResult接口返回到调用方。

```ets
// 调用方
// index.ets
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)

        Button("Call StartAbilityForResult")
          .onClick(() => {
            let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let want: Want = {
              bundleName: 'com.example.demo2',
              abilityName: 'EntryAbility'
            };

            try {
              // 通过startAbilityForResult拉起目标应用
              context.startAbilityForResult(want, (err: BusinessError, result: common.AbilityResult) => {
                if (err.code) {
                  // 处理业务逻辑错误
                  hilog.error(0x0000, 'testTag', `startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
                  this.message = `startAbilityForResult failed: code is ${err.code}, message is ${err.message}`
                  return;
                }
                // 执行正常业务
                hilog.info(0x0000, 'testTag', `startAbilityForResult succeed`);
                hilog.info(0x0000, 'testTag', `AbilityResult is ${JSON.stringify(result)}`);
                this.message = `AbilityResult.resultCode: ${JSON.stringify(result.resultCode)}`
              });
            } catch (err) {
              // 处理入参错误异常
              let code = (err as BusinessError).code;
              let message = (err as BusinessError).message;
              hilog.error(0x0000, 'testTag', `startAbilityForResult failed, code is ${code}, message is ${message}`);
              this.message = `startAbilityForResult failed, code is ${code}, message is ${message}`;
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
```

```ets
// 目标方
// EntryAbility.ets
import { AbilityConstant, common, UIAbility, Want, wantConstant } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 从want中获取调用方的CALLER_REQUEST_CODE，并保存
    let callerRequestCode: string = want?.parameters?.[wantConstant.Params.CALLER_REQUEST_CODE] as string;
    AppStorage.setOrCreate<string>("callerRequestCode", callerRequestCode)
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let callerRequestCode: string = want?.parameters?.[wantConstant.Params.CALLER_REQUEST_CODE] as string;
    AppStorage.setOrCreate<string>("callerRequestCode", callerRequestCode)
  }

  onForeground(): void {
    // 获取保存的CALLER_REQUEST_CODE
    let callerRequestCode: string = AppStorage.get<string>("callerRequestCode") as string;
    hilog.info(0x0000, 'testTag', `callerRequestCode is ${callerRequestCode}`);
    let want: Want = {};
    let resultCode = 100;
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };
    try {
      // 将结果信息返回给调用方
      this.context.backToCallerAbilityWithResult(abilityResult, callerRequestCode)
        .then(() => {
          // 执行正常业务
          hilog.info(0x0000, 'testTag', 'backToCallerAbilityWithResult succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          hilog.error(0x0000, 'testTag', `backToCallerAbilityWithResult failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 捕获同步的参数错误
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(0x0000, 'testTag', `backToCallerAbilityWithResult failed, code is ${code}, message is ${message}`);
    }
```

**setRestoreEnabled14+**

setRestoreEnabled(enabled: boolean): void

设置UIAbility是否启用备份恢复。

元服务API：从API version 14开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 表示是否启用恢复。true表示启用，false表示不启用。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let enabled = true;
    try {
      this.context.setRestoreEnabled(enabled);
    } catch (paramError) {
      let code = (paramError as BusinessError).code;
      let message = (paramError as BusinessError).message;
      console.error(`setRestoreEnabled failed, err code: ${code}, err msg: ${message}`);
    }
```

**startUIServiceExtensionAbility14+**

startUIServiceExtensionAbility(want: Want): Promise<void>

启动一个UIServiceExtensionAbility。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 14开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIServiceExtensionAbility的必要信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

示例：

```ets
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        // 创建启动按钮
        Button('start ability')
          .enabled(true)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let startWant: Want = {
              bundleName: 'com.acts.uiserviceextensionability',
              abilityName: 'UiServiceExtAbility',
            };
            try {
              // 启动UIServiceExtensionAbility
              context.startUIServiceExtensionAbility(startWant).then(() => {
                console.info('startUIServiceExtensionAbility success');
              }).catch((error: BusinessError) => {
                console.info('startUIServiceExtensionAbility error', JSON.stringify(error));
              })
            } catch (err) {
              console.info('startUIServiceExtensionAbility failed', JSON.stringify(err));
            }
          })
      }
```

**connectUIServiceExtensionAbility14+**

connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

连接一个UIServiceExtensionAbility。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 14开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 连接UIServiceExtensionAbility的必要信息。 |
| callback | UIServiceExtensionConnectCallback | 是 | 连接UIServiceExtensionAbility回调。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<UIServiceProxy> | Promise对象，包含connectUIServiceExtensionAbility执行后返回的UIServiceProxy对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 801 | Capability not supported. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000055 | Installation-free timed out. |

示例：

```ets
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[Extension] ';

@Entry
@Component
struct UIServiceExtensionAbility {
  dataCallBack : common.UIServiceExtensionConnectCallback = {
    // 接收数据
    onData: (data: Record<string, Object>) => {
      console.info(`dataCallBack received data`, JSON.stringify(data));
    },
    // 连接断开
    onDisconnect: () => {
      console.info(`dataCallBack onDisconnect`);
    }

  async myConnect() {
    // 获取上下文
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let startWant: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'UiServiceExtAbility'
    };

    try {
      // 连接服务
      context.connectUIServiceExtensionAbility(startWant, this.dataCallBack)
        .then((proxy: common.UIServiceProxy) => {
          console.info(TAG + `try to connectUIServiceExtensionAbility`, JSON.stringify(proxy));
        }).catch((err: Error) => {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.info(TAG + `connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.info(TAG + `connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    };
  }

  build() {
    RelativeContainer() {
      // 创建连接按钮
      Button('connectServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.myConnect()
        });
    }
    .height('100%')
    .width('100%')
  }
```

**disconnectUIServiceExtensionAbility14+**

disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>

断开与UIServiceExtensionAbility的连接。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

元服务API：从API version 14开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | UIServiceProxy | 是 | connectUIServiceExtensionAbility执行返回的Proxy。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[Extension] ';

@Entry
@Component
struct UIServiceExtensionAbility {
  comProxy: common.UIServiceProxy | null = null;

  build() {
    Scroll() {
      Column() {
        // 创建断开连接的按钮
        Button('disconnectUIServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
          .margin({
            top: 5,
            left: 10,
            right: 10,
            bottom: 5
          })
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.myDisconnectUIServiceExtensionAbility()
          });
      }
      .width('100%')
    }
    .height('100%')
  }

  myDisconnectUIServiceExtensionAbility() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    try {
      // 断开UIServiceExtension连接
      context.disconnectUIServiceExtensionAbility(this.comProxy)
        .then(() => {
          console.info(TAG + `disconnectUIServiceExtensionAbility succeed ${this.comProxy}`);
        }).catch((err: Error) => {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.info(TAG + `disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.info(TAG + `disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**setAbilityInstanceInfo15+**

setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>

设置当前UIAbility实例的图标和标签信息。图标与标签信息可在任务中心和快捷栏的界面中显示。使用Promise异步回调。

需要权限： ohos.permission.SET_ABILITY_INSTANCE_INFO

系统能力： SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 新的图标标签。标签长度不超过1024字节，且不可为空字符串。 |
| icon | image.PixelMap | 是 | 新的图标。建议图标大小为512px*512px。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', async (err, data) => {
      if (err.code) {
        console.error(`loadContent failed, code is ${err.code}`);
        return;
      }

      let newLabel: string = 'instance label';
      let color = new ArrayBuffer(512 * 512 * 4); // 创建一个ArrayBuffer对象，用于存储图像像素。该对象的大小为（height * width * 4）字节。
      let bufferArr = new Uint8Array(color);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr[i] = 255;
        bufferArr[i+1] = 0;
        bufferArr[i+2] = 122;
        bufferArr[i+3] = 255;
      }
      let opts: image.InitializationOptions = {
        editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 512, width: 512 }
      };
      let imagePixelMap: image.PixelMap = await image.createPixelMap(color, opts);
      this.context.setAbilityInstanceInfo(newLabel, imagePixelMap)
        .then(() => {
          console.info('setAbilityInstanceInfo success');
        }).catch((err: BusinessError) => {
        console.error(`setAbilityInstanceInfo failed, code is ${err.code}, message is ${err.message}`);
      });
  }
```

**revokeDelegator17+**

revokeDelegator(): Promise<void>

如果Module下首个UIAbility启动时期望重定向到另一个UIAbility，该重定向的UIAbility被称为“DelegatorAbility”。DelegatorAbility的设置详见当前接口示例的步骤1。

当DelegatorAbility完成特定操作时，可以使用该接口回到首个UIAbility。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

当接口调用成功后，DelegatorAbility中的[Window](模块描述.md)方法会失效。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not support. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000065 | The API can be called only when the ability is running in the foreground. |
| 16000084 | Only DelegatorAbility is allowed to call this API, and only once. |
| 16000085 | An error occurred during the interaction between the ability and window. |

示例：

1.

设置DelegatorAbility。

在[module.json5](../../guides/module.json5配置文件.md)配置文件标签中配置abilitySrcEntryDelegator和abilityStageSrcEntryDelegator。当Module下首个UIAbility冷启动时，系统优先启动abilitySrcEntryDelegator指向的UIAbility。

     ![image](public_sys-resources/note_3.0-zh-cn.webp)

  - 当UIAbility是通过[startAbilityByCall](#ZH-CN_TOPIC_0000002553200541__startabilitybycall)启动时，系统会忽略在[module.json5](../../guides/module.json5配置文件.md)配置文件标签中配置的abilitySrcEntryDelegator和abilityStageSrcEntryDelegator。

  - abilityStageSrcEntryDelegator指定的ModuleName不能与当前ModuleName相同。

```ets
{
  "module": {
    // ...
    "abilityStageSrcEntryDelegator": "xxxModuleName",
    "abilitySrcEntryDelegator": "xxxAbilityName",
    // ...
  }
```

1.

取消DelegatorAbility。
```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class DelegatorAbility extends UIAbility {
  onForeground() {
    // DelegatorAbility完成特定操作后，调用revokeDelegator回到首个UIAbility
    this.context.revokeDelegator().then(() => {
      console.info('revokeDelegator success');
    }).catch((err: BusinessError) => {
      console.error(`revokeDelegator failed, code is ${err.code}, message is ${err.message}`);
    });
  }
```

**setColorMode18+**

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

设置UIAbility的深浅色模式。调用该接口前需要保证该UIAbility对应页面已完成加载。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onwindowstagecreate)生命周期中通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法加载页面之后调用。

- 调用该接口后会创建新的资源管理器对象，如果此前有缓存资源管理器，需要进行更新。

- 深浅色模式生效的优先级：UIAbility的深浅色模式 > 应用的深浅色模式（[ApplicationContext.setColorMode](ApplicationContext (应用上下文).md#ZH-CN_TOPIC_0000002553360493__applicationcontextsetcolormode11)）> 系统的深浅色模式。

元服务API：从API version 18开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | 是 | 设置颜色模式，包括: - COLOR_MODE_DARK：深色模式 - COLOR_MODE_LIGHT：浅色模式 - COLOR_MODE_NOT_SET：不设置（跟随系统或应用） |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

示例：

```ets
import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content.');
        return;
      }
      let uiAbilityContext = this.context;
      uiAbilityContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
    });
  }
```

**startAppServiceExtensionAbility20+**

startAppServiceExtensionAbility(want: Want): Promise<void>

启动[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)实例。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口的调用方必须为[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](../../guides/module.json5配置文件.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动AppServiceExtensionAbility的Want信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000200 | The caller is not in the appIdentifierAllowList of the target application. |

示例：

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AppServiceExtensionAbility'
    };

    try {
      this.context.startAppServiceExtensionAbility(want)
        .then(() => {
          // 执行正常业务
          console.info('startAppServiceExtensionAbility succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`startAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**stopAppServiceExtensionAbility20+**

stopAppServiceExtensionAbility(want: Want): Promise<void>

停止[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)实例。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口的调用方必须为[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](../../guides/module.json5配置文件.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 停止AppServiceExtensionAbility的Want信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000200 | The caller is not in the appIdentifierAllowList of the target application. |

示例：

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AppServiceExtensionAbility'
    };

    try {
      this.context.stopAppServiceExtensionAbility(want)
        .then(() => {
          // 执行正常业务
          console.info('stopAppServiceExtensionAbility succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`stopAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`stopAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**connectAppServiceExtensionAbility20+**

connectAppServiceExtensionAbility(want: Want, callback: ConnectOptions): number

将当前UIAbility连接到[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)。通过返回的proxy与AppServiceExtensionAbility进行通信，以使用AppServiceExtensionAbility对外提供的能力。仅支持在主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

如果[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)实例未启动，该接口的调用方必须为AppServiceExtensionAbility所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](../../guides/module.json5配置文件.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 连接AppServiceExtensionAbility的Want信息。 |
| callback | ConnectOptions | 是 | ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，disconnectAppServiceExtensionAbility根据该连接id断开连接。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000201 | The target service has not been started yet. |

示例：

```ets
import { UIAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AppServiceExtensionAbility'
    };
    let commRemote: rpc.IRemoteObject;
    let callback: common.ConnectOptions = {
      onConnect(elementName, remote) {
        commRemote = remote;
        console.info('onConnect...');
      },
      onDisconnect(elementName) {
        console.info('onDisconnect...');
      },
      onFailed(code) {
        console.info('onFailed...');
      }
    };
    let connection: number;

    try {
      connection = this.context.connectAppServiceExtensionAbility(want, callback);
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`connectAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**disconnectAppServiceExtensionAbility20+**

disconnectAppServiceExtensionAbility(connection: number): Promise<void>

断开与[AppServiceExtensionAbility](@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)的连接。仅支持在主线程调用。使用Promise异步回调。

断开连接之后，为了防止使用可能失效的remote对象进行通信，建议将连接成功时返回的remote对象设置为null。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 在connectAppServiceExtensionAbility返回的连接id。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    // connection为connectAppServiceExtensionAbility中的返回值
    let connection = 1;
    let commRemote: rpc.IRemoteObject | null;

    try {
      this.context.disconnectAppServiceExtensionAbility(connection).then(() => {
        commRemote = null;
        // 执行正常业务
        console.info('disconnectAppServiceExtensionAbility succeed');
      }).catch((err: BusinessError) => {
        // 处理业务逻辑错误
        console.error(`disconnectAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      commRemote = null;
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`disconnectAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
    }
```

**setOnNewWantSkipScenarios20+**

setOnNewWantSkipScenarios(scenarios: number): Promise<void>

在特定场景下拉起UIAbility时，如果不需要触发[onNewWant](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onnewwant)生命周期回调，可以通过该接口设置。仅支持在主线程调用。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

该接口通常用于[onCreate](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__oncreate)生命周期回调中。入参取值建议包含所有的[Scenarios](@ohos.app.ability.contextConstant (Context相关常量).md#ZH-CN_TOPIC_0000002553200497__scenarios20)枚举值。详见下方示例代码。

元服务API：从API version 20开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scenarios | number | 是 | 取值范围请参考Scenarios。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. Possible causes: Connection to service failed. |

示例：

```ets
import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let scenarios: number = contextConstant.Scenarios.SCENARIO_MOVE_MISSION_TO_FRONT |
      contextConstant.Scenarios.SCENARIO_SHOW_ABILITY |
      contextConstant.Scenarios.SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT;

    try {
      this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
        // 执行正常业务
        console.info('setOnNewWantSkipScenarios succeed');
      }).catch((err: BusinessError) => {
        // 处理业务逻辑错误
        console.error(`setOnNewWantSkipScenarios failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`setOnNewWantSkipScenarios failed, code is ${code}, message is ${message}`);
    }
```

**startSelfUIAbilityInCurrentProcess22+**

startSelfUIAbilityInCurrentProcess(want: Want, specifiedFlag: string, options?: StartOptions): Promise<void>

在当前进程中启动应用程序自己的UIAbility。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 只能冷启动目标UIAbility，如果目标UIAbility实例已经启动过，则启动失败。

- 通过该接口启动的UIAbility实例，将运行在调用方所在的进程中。其他关于目标UIAbility的进程相关的策略（例如在[module.json5配置文件](../../guides/module.json5配置文件.md)中通过isolationProcess或isolationMode字段来指定进程），均不会生效。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：

- 从API version 23开始，该接口仅在PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

- 从API version 22开始，该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动Ability的必要信息。只支持显式启动，不支持隐式启动。 |
| specifiedFlag | string | 是 | 开发者自定义的UIAbility标识。该标识不能与已启动的UIAbility标识相同，否则将返回错误。 说明： 当通过该接口拉起启动模式为specified的UIAbility时，将不会触发onAcceptWant回调。 |
| options | StartOptions | 否 | 启动Ability所携带的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Connect to system service failed. |
| 16000053 | The ability is not on the top of the UI. |
| 16000122 | The target component is blocked by the system module and does not support startup. |
| 16000123 | Implicit startup is not supported. |
| 16000124 | Starting a remote UIAbility is not supported. |
| 16000130 | The UIAbility not belong to caller. |
| 16000131 | The UIAbility is already exist, can not start again. |

示例：

```ets
import { UIAbility, StartOptions, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let accountId = 100;
    let options: StartOptions = {
      displayId: 0
    };

    let instanceFlag = 'instance1';

    try {
      this.context.startSelfUIAbilityInCurrentProcess(want, instanceFlag, options);
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startSelfUIAbilityInCurrentProcess failed, code is ${code}, message is ${message}`);
    }
```

**restartApp22+**

restartApp(want: Want): Promise<void>

处于获焦状态的UIAbility可以通过该接口，重启当前UIAbility所在的进程，并拉起应用内的指定UIAbility。仅支持主线程调用。使用Promise异步回调。

如果指定UIAbility就是当前UIAbility，则会刷新窗口至初始状态；如果是其他UIAbility，则会跳转并打开新的UIAbility窗口。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

通过该接口重启进程时，不会触发进程中Ability的onDestroy生命周期回调。

在元服务调用本接口成功后的3秒内，再次调用本接口、[restartSelfAtomicService()](@ohos.app.ability.abilityManager (Ability信息管理).md#ZH-CN_TOPIC_0000002553200519__abilitymanagerrestartselfatomicservice20)或[ApplicationContext.restartApp()](ApplicationContext (应用上下文).md#ZH-CN_TOPIC_0000002553360493__applicationcontextrestartapp12)接口中的任一接口，系统将返回错误码16000064。

在应用调用本接口成功后的3秒内，若再次调用本接口或[ApplicationContext.restartApp()](ApplicationContext (应用上下文).md#ZH-CN_TOPIC_0000002553360493__applicationcontextrestartapp12)接口中的任一接口，系统将返回错误码16000064。

元服务API：从API version 22开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在Phone设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | Want类型参数，传入需要启动的UIAbility的信息，校验bundleName、abilityName。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Connect to system server error. |
| 16000063 | The target to restart does not belong to the caller or is not a UIAbility. |
| 16000064 | Restart too frequently. |
| 16000065 | The API can be called only when the ability is focused. |

示例：

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'restartApp with window';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(async () => {
          let want: Want = {
            bundleName: 'com.example.myapplication',
            abilityName: 'EntryAbility'
          };
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          try {
            await context.restartApp(want);
          } catch (err) {
            hilog.error(0x0000, 'testTag', `restart failed: ${err.code}, ${err.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

**setMissionWindowIcon22+**

setMissionWindowIcon(windowIcon: image.PixelMap): Promise<void>

设置当前UIAbility在应用窗口、任务中心应用卡片、快捷栏窗口快照的图标。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

setMissionWindowIcon和[setAbilityInstanceInfo](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__setabilityinstanceinfo15)之间不存在调用优先级关系。当多个接口被依次调用时，后一次调用的接口所设置的图标信息将覆盖之前调用接口所设置的内容，最终生效的图标以最后一次调用的接口为准。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

设备行为差异：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowIcon | image.PixelMap | 是 | 在应用窗口、任务中心应用卡片、快捷栏窗口快照显示的Ability图标。图标必须为正方形，且大小不能超过128M，否则返回401参数错误。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |
| 16000135 | The main window of this ability not exist. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let imagePixelMap: image.PixelMap;
    let color = new ArrayBuffer(1024 * 1024 * 4); // 创建一个ArrayBuffer对象，用于存储图像像素。该对象的大小为（height * width * 4）字节。
    let bufferArr = new Uint8Array(color);
    for (let i = 0; i < bufferArr.length; i += 4) {
      bufferArr[i] = 255;
      bufferArr[i+1] = 0;
      bufferArr[i+2] = 122;
      bufferArr[i+3] = 255;
    }
    image.createPixelMap(color, {
      editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 1024, width: 1024 }
    }).then((data) => {
      imagePixelMap = data;
      this.context.setMissionWindowIcon(imagePixelMap)
        .then(() => {
          console.info('setMissionWindowIcon succeed');
        })
        .catch((err: BusinessError) => {
          console.error(`setMissionWindowIcon failed, code is ${err.code}, message is ${err.message}`);
        });
    }).catch((err: BusinessError) => {
      console.error(`createPixelMap failed, code is ${err.code}, message is ${err.message}`);
    });
  }
```