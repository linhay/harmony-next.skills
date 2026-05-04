# UIExtensionContext

UIExtensionContext是[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)的上下文环境，继承自[ExtensionContext](ExtensionContext.md)，提供[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)的相关配置信息以及操作[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)的方法，如启动[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)等。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 本模块接口仅可在Stage模型下使用。

- 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

**导入模块**

```ets
import { common } from '@kit.AbilityKit';
```

**UIExtensionContext**

**startAbility**

startAbility(want: Want, callback: AsyncCallback<void>): void

启动一个UIAbility。使用callback异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动UIAbility成功时，err为undefined，否则为错误对象。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {

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

启动一个UIAbility。使用callback异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | StartOptions | 是 | 启动UIAbility所携带的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动UIAbility成功时，err为undefined，否则为错误对象。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

启动一个UIAbility。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | StartOptions | 否 | 启动UIAbility所携带的额外参数。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
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

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止并且返回结果给调用方。

- 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。

- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| callback | AsyncCallback<AbilityResult> | 是 | 回调函数，包含返回给拉起方的信息。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
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

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止并且返回结果给调用方。

- 异常情况下比如杀死UIAbility会返回异常信息给调用方，异常信息中resultCode为-1。

- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方，其它调用方返回异常信息, 异常信息中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | StartOptions | 是 | 启动UIAbility所携带的额外参数。 |
| callback | AsyncCallback<AbilityResult> | 是 | 回调函数，包含返回给拉起方的信息。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
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

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止并且返回结果给调用方。

- 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。

- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | StartOptions | 否 | 启动UIAbility所携带的额外参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，返回被拉起的UIAbility退出时的返回结果。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
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

**connectServiceExtensionAbility**

connectServiceExtensionAbility(want: Want, options: ConnectOptions): number

将当前UIExtensionAbility连接到一个ServiceExtensionAbility，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。

ServiceExtensionAbility是一类特殊的[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 连接ServiceExtensionAbility的Want信息，包括Ability名称，Bundle名称等。 |
| options | ConnectOptions | 是 | ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，客户端可以通过disconnectServiceExtensionAbility传入该连接id来断开连接。 |

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
| 16000070 | The extension cannot start the service. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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
        console.error(`onFailed, err code: ${code}.`);
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

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。

ServiceExtensionAbility是一类特殊的[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识Id，即connectServiceExtensionAbility返回的connectionId。 |

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
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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
      })
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

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用callback异步回调。

ServiceExtensionAbility是一类特殊的[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识Id，即connectServiceExtensionAbility返回的connectionId。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开与ServiceExtensionAbility的连接成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

**terminateSelf12+**

terminateSelf(callback: AsyncCallback<void>): void

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用callback异步回调。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。UIExtensionAbility停止成功时，err为undefined，否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

**terminateSelf12+**

terminateSelf(): Promise<void>

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用Promise异步回调。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

**terminateSelfWithResult12+**

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用callback异步回调。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | AbilityResult | 是 | 返回给UIExtensionAbility拉起方的信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。UIExtensionAbility停止成功时，err为undefined，否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

**terminateSelfWithResult12+**

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用Promise异步回调。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | AbilityResult | 是 | 返回给UIExtensionAbility拉起方的信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

错误码：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

**reportDrawnCompleted12+**

reportDrawnCompleted(callback: AsyncCallback<void>): void

用于应用通知系统UIExtensionAbility对应的窗口内容已绘制完成。系统会根据开发者调用的时机进行资源分配优化等，以优化应用启动及显示时间。使用callback异步回调。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当打点成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[testTag] ShareExtAbility';

export default class ShareExtAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
    let data: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(data);
    session.loadContent('pages/extension', storage);
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
```

**openAtomicService12+**

openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>

打开一个独立窗口的元服务，并返回结果。使用Promise异步回调。

分为以下几种情况：

- 正常情况下可通过调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止并且返回结果给调用方。

- 异常情况下比如杀死元服务会返回异常信息给调用方，异常信息中resultCode为-1。

- 如果不同应用多次调用该接口启动同一个元服务，当这个元服务调用[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002553200541__terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息，异常信息中resultCode为-1。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的唯一标识，由云端统一分配。 |
| options | AtomicServiceOptions | 否 | 启动元服务所携带的参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象。返回给拉起方的信息。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16200001 | The caller has been released. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, common, AtomicServiceOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let appId: string = '6918661953712445909';
    let options: AtomicServiceOptions = {
      displayId: 0,
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

通过App Linking或Deep Linking方式启动UIAbility。使用Promise异步回调。

通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标UIAbility。目标方必须具备以下过滤器特征，才能处理App Linking链接：

- "actions"列表中包含"ohos.want.action.viewData"。

- "entities"列表中包含"entity.system.browsable"。

- "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。

如果希望获取被拉起方终止后的结果，可以设置callback参数，此参数的使用可参照[startAbilityForResult](#ZH-CN_TOPIC_0000002522080578__startabilityforresult)接口。

传入的参数不合法时，如未设置必选参数或link字符串不是标准格式的URL，接口会直接抛出异常。参数校验通过，拉起目标方时出现的错误通过promise返回错误信息。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

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
| Promise<void> | 无返回结果的Promise对象。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16200001 | The caller has been released. |
| 16000053 | The ability is not on the top of the UI. |
| 16000136 | The UIAbility is prohibited from launching itself via App Linking. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, Want, UIExtensionContentSession, OpenLinkOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onCreate() {
    console.info(`UIExtAbility onCreate`);
  }

  onForeground() {
    console.info(`UIExtAbility onForeground`);
  }

  onBackground() {
    console.info(`UIExtAbility onBackground`);
  }

  onDestroy() {
    console.info(`UIExtAbility onDestroy`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(`UIExtAbility onSessionCreate`);
    console.info(`UIExtAbility onSessionCreate, want: ${JSON.stringify(want)}`);
    let record: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(record);
    session.loadContent('pages/UIExtensionIndex', storage);

    let link: string = 'https://www.example.com';
    let openLinkOptions: OpenLinkOptions = {
      appLinkingOnly: true
    };
    try {
      this.context.openLink(
        link,
        openLinkOptions,
        (err, result) => {
          if (err) {
            console.error(`openLink callback failed, err code: ${err.code}, err msg: ${err.message}.`);
            return;
          }
          console.info(`openLink success, result code: ${result.resultCode} result data: ${result.want}.`);
        }
      ).then(() => {
        console.info(`open link success.`);
      }).catch((err: BusinessError) => {
        console.error(`open link failed, err code: ${err.code}, err msg: ${err.message}.`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(`openLink failed, err code: ${code}, err msg: ${msg}.`);
    }

  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(`UIExtAbility onSessionDestroy`);
  }
```

**startUIServiceExtensionAbility14+**

startUIServiceExtensionAbility(want: Want): Promise<void>

启动一个UIServiceExtensionAbility。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 启动UIServiceExtensionAbility的Want。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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
            let context = this.getUIContext().getHostContext() as common.UIExtensionContext;
            let startWant: Want = {
              bundleName: 'com.acts.uiserviceextensionability',
              abilityName: 'UiServiceExtAbility',
            };
            try {
              // 启动UIServiceExtensionAbility
              context.startUIServiceExtensionAbility(startWant).then(() => {
                console.info(`startUIServiceExtensionAbility success.`);
              }).catch((error: BusinessError) => {
                console.error(`startUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.`);
              })
            } catch (err) {
              let code = (err as BusinessError).code;
              let msg = (err as BusinessError).message;
              console.error(`startUIServiceExtensionAbility failed, err code: ${code}, err msg: ${msg}.`);
            }
          })
      }
```

**connectUIServiceExtensionAbility14+**

connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

连接到一个UIServiceExtensionAbility。使用Promise异步回调。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件启动规则详见：[组件启动规则（Stage模型）](../../guides/组件启动规则（Stage模型）.md)。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 用于连接的Want信息。 |
| callback | UIServiceExtensionConnectCallback | 是 | 连接UIServiceExtensionAbility回调。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<UIServiceProxy> | Promise对象，连接UIServiceExtensionAbility成功时，返回UIServiceProxy对象，借助该对象可以往UIServiceExtensionAbility发送数据。 |

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
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000055 | Installation-free timed out. |

示例：

```ets
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page_UIServiceExtensionAbility {
  @State uiServiceProxy: common.UIServiceProxy | null = null;

  build() {
    Column() {
      Row() {
        // ...
      }.onClick(() => {
        const context = this.getUIContext().getHostContext() as common.UIExtensionContext;
        const want: Want = {
          deviceId: '',
          bundleName: 'com.example.myapplication',
          abilityName: ''
        };
        // 定义回调
        const callback: common.UIServiceExtensionConnectCallback = {
          onData: (data: Record<string, Object>): void => {
            console.info(`onData, data: ${JSON.stringify(data)}.`);
          },
          onDisconnect: (): void => {
            console.info(`onDisconnect`);
          }
        };
        // 连接UIServiceExtensionAbility
        context.connectUIServiceExtensionAbility(want, callback).then((uiServiceProxy: common.UIServiceProxy) => {
          this.uiServiceProxy = uiServiceProxy;
          console.info(`connectUIServiceExtensionAbility success`);
        }).catch((error: BusinessError) => {
          console.error(`connectUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.`);
        })
    }
```

**disconnectUIServiceExtensionAbility14+**

disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>

断开UIServiceExtensionAbility。使用Promise异步回调。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | UIServiceProxy | 是 | connectUIServiceExtensionAbility返回的Proxy。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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

@Entry
@Component
struct Page_UIServiceExtensionAbility {
  @State uiServiceProxy: common.UIServiceProxy | null = null;

  build() {
    Column() {
      Row() {
        // ...
      }.onClick(() => {
        const context = this.getUIContext().getHostContext() as common.UIExtensionContext;
        // this.uiServiceProxy是连接时保存的proxy对象
        context.disconnectUIServiceExtensionAbility(this.uiServiceProxy).then(() => {
          console.info(`disconnectUIServiceExtensionAbility success.`);
        }).catch((error: BusinessError) => {
          console.info(`disconnectUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.`);
        })
    }
```

**setColorMode18+**

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

设置UIExtensionAbility的深浅色模式。调用该接口前需要保证该UIExtensionContext对应页面已完成加载。仅支持主线程调用。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 调用该接口后会创建新的资源管理器对象，如果此前有缓存资源管理器，需要进行更新。

- 深浅色模式生效的优先级：UIExtensionAbility的深浅色模式 > 应用的深浅色模式（[ApplicationContext.setColorMode](ApplicationContext (应用上下文).md#ZH-CN_TOPIC_0000002553360493__applicationcontextsetcolormode11)）> 系统的深浅色模式。

系统能力：SystemCapability.Ability.AbilityRuntime.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | 是 | 设置颜色模式，包括： - COLOR_MODE_DARK：深色模式 - COLOR_MODE_LIGHT：浅色模式 - COLOR_MODE_NOT_SET：不设置（跟随系统或应用） |

错误码：

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

示例：

```ets
// UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { ShareExtensionAbility, ConfigurationConstant } from '@kit.AbilityKit';

export default class MyAbility extends ShareExtensionAbility {
  onForeground() {
    let uiExtensionContext = this.context;
    uiExtensionContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
  }
```