# FormEditExtensionContext

FormEditExtensionContext是[FormEditExtensionAbility](@ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility).md)的上下文，继承自[UIExtensionContext](UIExtensionContext.md)。

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { FormEditExtensionAbility } from '@kit.FormKit';
```

#### FormEditExtensionContext

FormEditExtensionContext提供允许访问特定于FormEditExtensionAbility资源的能力。

#### startSecondPage

startSecondPage(want: Want): Promise<[AbilityResult](AbilityResult.md)>

拉起需要被编辑的卡片提供方页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是第三方应用需要被桌面拉起的编辑页面信息。

**返回值：**

类型说明Promise<[AbilityResult](AbilityResult.md)>Promise对象，返回AbilityResult。

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](卡片错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息202The application is not a system application.16500050An IPC connection error happened.16501000An internal functional error occurred.16500100Failed to obtain the configuration information.

**示例：**

```ets
import { FormEditExtensionAbility } from '@kit.FormKit'
import { Want, UIExtensionContentSession } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExampleFormEditExtensionAbility'

export default class ExampleFormEditAbility extends FormEditExtensionAbility {
  abilityName: string = 'FormEditSecPageAbility'

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    try {
      this.context.startSecondPage({
        bundleName: 'com.example.formEditDemo',
        parameters: {
          "secPageAbilityName": this.abilityName
        }

      }).then(data => {
        console.info(TAG, `startSecondPage result want: ${JSON.stringify(data)}`)
      });
    } catch (e) {
      console.error(TAG, `startSecondPage failed:${e}`)
      return
    }
  }
}
```