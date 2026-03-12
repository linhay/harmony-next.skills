# @ohos.InputMethodExtensionContext (InputMethodExtensionContext)

InputMethodExtensionContext模块是InputMethodExtensionAbility的上下文环境，继承于ExtensionContext，提供InputMethodExtensionAbility具有的能力和接口，包括启动、停止、绑定、解绑Ability。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { InputMethodExtensionContext } from '@kit.IMEKit';
```

#### 使用说明

在使用InputMethodExtensionContext的功能前，需要通过InputMethodExtensionAbility子类实例获取。

```ets
import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    let context: InputMethodExtensionContext = this.context;
  }
}
```

#### InputMethodExtensionContext.destroy

destroy(callback: AsyncCallback<void>): void;

销毁输入法应用。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当销毁输入法应用成功时，err为undefined；否则为错误对象。

**示例：**

```ets
import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    let context: InputMethodExtensionContext = this.context;
  }

  onDestroy() {
    this.context.destroy((err: BusinessError) => {
      if (err) {
        console.error(`Failed to destroy context, err code = ${err.code}`);
        return;
      }
      console.info('Succeeded in destroying context.');
    });
  }
}
```

#### InputMethodExtensionContext.destroy

destroy(): Promise<void>;

销毁输入法应用。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    let context: InputMethodExtensionContext = this.context;
  }

  onDestroy() {
    this.context.destroy().then(() => {
      console.info('Succeed in destroying context.');
    }).catch((err: BusinessError)=>{
      console.error(`Failed to destroy context, err code = ${err.code}`);
    });
  }
}
```

#### InputMethodExtensionContext.startAbility12+

startAbility(want: Want): Promise<void>;

拉起目标应用。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是用于指定目标应用的Want类型信息，包括ability名称、bundle名称等。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[元能力错误码](元能力子系统错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.16000001The specified ability does not exist.16000002Incorrect ability type.16000004Cannot start an invisible component.16000005The specified process does not have the permission.16000006Cross-user operations are not allowed.16000008The crowdtesting application expires.16000009An ability cannot be started or stopped in Wukong mode.16000010The call with the continuation and prepare continuation flag is forbidden.16000011The context does not exist.16000012The application is controlled.16000013The application is controlled by EDM.16000019No matching ability is found.16000050Internal error.16000053The ability is not on the top of the UI.16000055Installation-free timed out.16000061Operation not supported.16200001The caller has been released.16000069The extension cannot start the third party application.16000070The extension cannot start the service.

**示例：**

```ets
import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    const context: InputMethodExtensionContext = this.context;
    const targetWant: Want = {
      bundleName: "com.example.aafwk.test",
      abilityName: "com.example.aafwk.test.TwoAbility"
    };

    context.startAbility(targetWant)
      .then(() => console.info('startAbility success'))
      .catch((err: BusinessError) => {
        console.error(`StartAbility failed. Code: ${err.code}, Message: ${err.message}`);
      });
  }

  onDestroy() {
    this.context.destroy().then(() => {
      console.info('Succeed in destroying context.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to destroy context, err code = ${err.code}`);
    });
  }
}
```