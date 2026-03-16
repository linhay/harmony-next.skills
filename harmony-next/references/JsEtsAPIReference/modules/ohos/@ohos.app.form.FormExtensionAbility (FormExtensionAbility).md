# @ohos.app.form.FormExtensionAbility (FormExtensionAbility)

FormExtensionAbility为卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

FormExtensionAbility创建后10秒内无操作将会被清理。

如下模块不支持在FormExtensionAbility引用，可能会导致程序异常退出。

- @ohos.ability.particleAbility (ParticleAbility模块)
- @ohos.multimedia.audio (音频管理)
- @ohos.multimedia.camera (相机管理)
- @ohos.multimedia.media (媒体服务)
- @ohos.resourceschedule.backgroundTaskManager (后台任务管理)

#### 导入模块

```ets
import { FormExtensionAbility } from '@kit.FormKit';
```

#### FormExtensionAbility

卡片扩展类。包含卡片提供方接收创建卡片、修改可见性等的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

#### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

名称类型只读可选说明context[FormExtensionContext](../../topics/graphics/FormExtensionContext.md)否否

FormExtensionAbility的上下文环境，继承自[ExtensionContext](../../topics/graphics/ExtensionContext.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

#### FormExtensionAbility.onAddForm

onAddForm(want: Want): formBindingData.FormBindingData

卡片提供方接收创建卡片的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是当前卡片相关的Want类型信息，其中Want中的parameters为自定义取值，取值可以包含[卡片参数枚举](@ohos.app.form.formInfo (formInfo).md#ZH-CN_TOPIC_0000002497445300__formparam)中的一个或多个，如卡片ID、卡片名称、卡片样式等。这些卡片信息必须作为持久数据进行管理，以便后续更新和删除卡片。

**返回值：**

类型说明[formBindingData.FormBindingData](@ohos.app.form.formBindingData (卡片数据绑定类).md#ZH-CN_TOPIC_0000002529445243__formbindingdata)formBindingData.FormBindingData对象，卡片要显示的数据。

**示例：**

```ets
import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };

    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
}
```

#### FormExtensionAbility.onCastToNormalForm

onCastToNormalForm(formId: string): void

卡片提供方收到卡片使用方将临时卡片转常态卡片的通知接口。临时卡片、常态卡片是卡片使用方的概念，其中：临时卡片是短期存在的，在特定事件或用户行为后显示，完成后自动消失。常态卡片是持久存在的，在用户未进行清除或更改的情况下，会一直存在，平时开发的功能卡片属于常态卡片。当前卡片使用方不会使用临时卡片。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是请求转换为常态的卡片标识。

**示例：**

```ets
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onCastToNormalForm(formId: string) {
    // 卡片提供方收到卡片使用方将临时卡片转常态卡片的通知时触发，开发者需根据实际需求做相应的处理
    console.info(`FormExtensionAbility onCastToNormalForm, formId: ${formId}`);
  }
};
```

#### FormExtensionAbility.onUpdateForm

onUpdateForm(formId: string, wantParams?: Record<string, Object>): void

卡片提供方接收携带参数的更新卡片的通知接口。获取最新数据后调用formProvider的[updateForm](@ohos.app.form.formProvider (formProvider).md#ZH-CN_TOPIC_0000002529285271__formproviderupdateform)接口刷新卡片数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是请求更新的卡片ID。wantParams12+Record<string, Object>否更新参数。

**示例：**

```ets
import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onUpdateForm(formId: string, wantParams?: Record<string, Object>) {
    console.info(`FormExtensionAbility onUpdateForm, formId: ${formId},
        wantPara: ${wantParams?.['ohos.extra.param.key.host_bg_inverse_color']}`);
    let param: Record<string, string> = {
      'temperature': '22c',
      'time': '22:00'
    }
    let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
    formProvider.updateForm(formId, obj2).then(() => {
      console.info(`FormExtensionAbility context updateForm`);
    }).catch((error: BusinessError) => {
      console.error(`FormExtensionAbility context updateForm failed, data: ${error}`);
    });
  }
};
```

#### FormExtensionAbility.onChangeFormVisibility

onChangeFormVisibility(newStatus: Record<string, number>): void

卡片提供方接收修改可见性的通知接口。

该接口仅对系统应用生效，且需要将formVisibleNotify配置为true。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明newStatusRecord<string, number>是请求修改的卡片标识和可见状态。

**示例：**

```ets
import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

// ArkTS规范中ets文件无法使用Object.keys和for..in...获取Object的key值，请使用自定义函数getObjKeys代替。
// 使用时请将此函数单独抽离至一个ts文件中并导出，在需要用到的ets文件中导入此函数后使用。
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onChangeFormVisibility(newStatus: Record<string, number>) {
    console.info(`FormExtensionAbility onChangeFormVisibility, newStatus: ${newStatus}`);
    let param: Record<string, string> = {
      'temperature': '22c',
      'time': '22:00'
    }
    let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);

    let keys: string[] = getObjKeys(newStatus);

    for (let i: number = 0; i < keys.length; i++) {
      console.info(`FormExtensionAbility onChangeFormVisibility, key: ${keys[i]}, value= ${newStatus[keys[i]]}`);
      formProvider.updateForm(keys[i], obj2).then(() => {
        console.info(`FormExtensionAbility context updateForm`);
      }).catch((error: BusinessError) => {
        console.error(`Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
      });
    }
  }
};
```

#### FormExtensionAbility.onFormEvent

onFormEvent(formId: string, message: string): void

卡片提供方接收处理卡片事件的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是请求触发事件的卡片标识。messagestring是事件消息。

**示例：**

```ets
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onFormEvent(formId: string, message: string) {
    console.info(`FormExtensionAbility onFormEvent, formId: ${formId}, message: ${message}`);
  }
};
```

#### FormExtensionAbility.onRemoveForm

onRemoveForm(formId: string): void

卡片提供方接收销毁卡片的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是请求销毁的卡片标识。

**示例：**

```ets
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onRemoveForm(formId: string) {
    console.info(`FormExtensionAbility onRemoveForm, formId: ${formId}`);
  }
};
```

#### FormExtensionAbility.onConfigurationUpdate

onConfigurationUpdate(newConfig: Configuration): void

当系统配置项变更时调用，仅当FormExtensionAbility存活时才会触发onConfigurationUpdate回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明newConfig[Configuration](@ohos.app.ability.Configuration (环境变量).md)是表示需要更新的配置信息。

**示例：**

```ets
import { FormExtensionAbility } from '@kit.FormKit';
import { Configuration } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onConfigurationUpdate(newConfig: Configuration) {
    // 仅当前formExtensionAbility存活时更新配置才会触发此生命周期。
    // 需要注意：formExtensionAbility创建后10秒内无操作将会被清理。
    console.info(`onConfigurationUpdate, config: ${JSON.stringify(newConfig)}`);
  }
};
```

#### FormExtensionAbility.onAcquireFormState

onAcquireFormState?(want: Want): formInfo.FormState

卡片提供方接收查询卡片状态通知接口，默认返回卡片初始状态(该方法可以选择性重写)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是want表示获取卡片状态的描述。描述包括Bundle名称、能力名称、模块名称、卡片名称等。

**返回值：**

类型说明[formInfo.FormState](@ohos.app.form.formInfo (formInfo).md#ZH-CN_TOPIC_0000002497445300__formstate)formInfo.FormState枚举，表示卡片当前的状态。

**示例：**

```ets
import { FormExtensionAbility, formInfo } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAcquireFormState(want: Want) {
    console.info(`FormExtensionAbility onAcquireFormState, want: ${want}`);
    return formInfo.FormState.UNKNOWN;
  }
};
```

#### FormExtensionAbility.onStop12+

onStop?(): void

当卡片提供方的卡片进程退出时，触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**示例：**

```ets
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onStop() {
    console.info(`FormExtensionAbility onStop`);
  }
}
```

#### FormExtensionAbility.onFormLocationChanged20+

onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void

当卡片位置发生变化时，触发该回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是发生位置变化的卡片标识。newFormLocation[formInfo.FormLocation](@ohos.app.form.formInfo (formInfo).md#ZH-CN_TOPIC_0000002497445300__formlocation20)是卡片最新位置的枚举值。

**示例：**

```ets
import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    let formData: Record<string, string | Object> = {
      'data': 'addForm'
    };
    return formBindingData.createFormBindingData(formData);
  }
  onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation) {
    console.info("EntryFormAbility onFormLocationChanged current location: " + newFormLocation);
  }
}
```

#### FormExtensionAbility.onSizeChanged20+

onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void

卡片大小变化时，触发回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是卡片标识。newDimension[formInfo.FormDimension](@ohos.app.form.formInfo (formInfo).md#ZH-CN_TOPIC_0000002497445300__formdimension)是卡片尺寸，例如 Dimension_1_2，表示 1 x 2 卡片。newRect[formInfo.Rect](@ohos.app.form.formInfo (formInfo).md#ZH-CN_TOPIC_0000002497445300__rect20)是卡片位置信息，包括卡片左上角顶点的xy坐标和卡片的宽高。

**示例：**

```ets
import { FormExtensionAbility, formInfo } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect) {
    console.info(`FormExtensionAbility onSizeChanged, formId: ${formId}, newDimension: ${newDimension}`);
  }
}
```