# @ohos.app.ability.dialogRequest (dialogRequest模块)

dialogRequest模块用于处理模态弹框的能力，包括获取RequestInfo（用于绑定模态弹框）、获取RequestCallback（用于设置结果）。

模态弹框是指一个系统弹框，该弹框会拦截弹框之下的页面的鼠标、键盘、触屏等事件。销毁该弹框后，才能对页面进行操作。

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则可以使用本模块的接口获取请求方的RequestInfo、RequestCallback并返回请求结果。

#### 导入模块

```ets
import { dialogRequest } from '@kit.AbilityKit';
```

#### dialogRequest.getRequestInfo

getRequestInfo(want: Want): RequestInfo

 该接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则能从Want中获取请求方的RequestInfo。其他场景使用该接口，均无法获取返回值。

从Want中获取请求方的RequestInfo。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是表示发起方请求弹框时传入的want信息。

**返回值：**

类型说明[RequestInfo](#ZH-CN_TOPIC_0000002529444575__requestinfo)请求方RequestInfo，用于绑定模态窗口。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestInfo = dialogRequest.getRequestInfo(want);
    } catch (err) {
      console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
    }
  }
}
```

#### dialogRequest.getRequestCallback

getRequestCallback(want: Want): RequestCallback

从Want中获取请求方的RequestCallback。

 该接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则能从Want中获取请求方的RequestCallback。其他场景使用该接口，均无法获取返回值。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是表示发起方请求弹框时传入的want信息。

**返回值：**

类型说明[RequestCallback](#ZH-CN_TOPIC_0000002529444575__requestcallback)请求方RequestCallback，用于设置返回结果。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestCallback = dialogRequest.getRequestCallback(want);
    } catch(err) {
      console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
    }
  }
}
```

#### WindowRect10+

表示模态弹框的属性。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明leftnumber否否弹框边框的左上角的X坐标。topnumber否否弹框边框的左上角的Y坐标。widthnumber否否弹框的宽度，单位为px。heightnumber否否弹框的高度，单位为px。

#### RequestInfo

表示发起方请求信息，作为窗口绑定模态弹框的入参。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明windowRect10+[WindowRect](#ZH-CN_TOPIC_0000002529444575__windowrect10)否是表示模态弹框的位置属性。

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestInfo = dialogRequest.getRequestInfo(want);
      console.info(`getRequestInfo windowRect=, ${JSON.stringify(requestInfo.windowRect)}` );
    } catch(err) {
      console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
    }
  }
}
```

#### ResultCode

模态弹框请求结果码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称值说明RESULT_OK0表示成功。RESULT_CANCEL1表示失败。

#### RequestResult

模态弹框请求结果，包含结果码ResultCode和请求结果ResultWant。

#### 属性

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明result[ResultCode](#ZH-CN_TOPIC_0000002529444575__resultcode)否否表示结果码。want10+[Want](@ohos.app.ability.Want (Want).md)否是表示Want类型信息，如ability名称，包名等。

#### RequestCallback

用于设置模态弹框请求结果的callback接口。

**模型约束**：此接口仅可在Stage模型下使用。

#### RequestCallback.setRequestResult

setRequestResult(result: RequestResult): void

设置请求结果

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

参数名类型必填说明result[RequestResult](#ZH-CN_TOPIC_0000002529444575__requestresult)是模态弹框请求结果信息。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestCallback = dialogRequest.getRequestCallback(want);
      let myResult: dialogRequest.RequestResult = {
        result : dialogRequest.ResultCode.RESULT_CANCEL,
      };
      requestCallback.setRequestResult(myResult);
    } catch(err) {
      console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
    }
  }
}
```