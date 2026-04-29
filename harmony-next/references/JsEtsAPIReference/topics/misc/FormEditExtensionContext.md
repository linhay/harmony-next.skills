# FormEditExtensionContext

FormEditExtensionContext是[FormEditExtensionAbility](@ohos.app.form.FormEditExtensionAbility  (FormEditExtensionAbility).md)的上下文，继承自[UIExtensionContext](UIExtensionContext.md)。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

**导入模块**

```ets
import { FormEditExtensionAbility } from '@kit.FormKit';
```

**FormEditExtensionContext**

FormEditExtensionContext提供允许访问特定于FormEditExtensionAbility资源的能力。

**startSecondPage**

startSecondPage(want: Want): Promise<[AbilityResult](AbilityResult.md)>

拉起需要被编辑的卡片提供方页面。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Ability.Form

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 第三方应用需要被桌面拉起的编辑页面信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，返回AbilityResult。 |

错误码：

以下错误码的详细介绍请参见[卡片错误码](卡片错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | The application is not a system application. |
| 16500050 | An IPC connection error happened. |
| 16501000 | An internal functional error occurred. |
| 16500100 | Failed to obtain the configuration information. |

示例：

```ets
import { FormEditExtensionAbility } from '@kit.FormKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

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
        console.info(TAG, `startSecondPage result want: ${data.resultCode}`)
      });
    } catch (e) {
      console.error(TAG, `startSecondPage failed, code: ${e.code}, message: ${e.message}`)
      return
    }
```

**startUIAbility23+**

startUIAbility(want: Want): Promise<void>

拉起卡片所属应用的UIAbility。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Ability.Form

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 应用自身UIAbility的ability信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

错误码：

以下错误码的详细介绍请参见[卡片错误码](卡片错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16500050 | An IPC connection error happened. |
| 16500100 | Failed to obtain the configuration information. |
| 16000130 | The target UIAbility does not belong to the caller. |
| 16501014 | The form edit page is not in the foreground. The current operation is not supported. |
| 16000121 | The target component type is not a UIAbility. |

示例：

```ets
import { FormEditExtensionAbility } from '@kit.FormKit'
import { Want, UIExtensionContentSession } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExampleFormEditExtensionAbility'

export default class ExampleFormEditAbility extends FormEditExtensionAbility {
  abilityName: string = 'FormEditSecPageAbility'

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    try {
      this.context.startUIAbility({
        abilityName: 'EntryAbility1',
      }).then(() => {
        console.info(TAG, `startUIAbility success`);
      });
    } catch (e) {
      console.error(TAG, `startUIAbility failed, code: ${e.code}, message: ${e.message}`);
      return
    }
```