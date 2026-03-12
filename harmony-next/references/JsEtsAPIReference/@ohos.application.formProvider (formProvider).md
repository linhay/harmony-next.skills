# @ohos.application.formProvider (formProvider)

FormProvider模块提供了卡片提供方相关接口的能力，开发者在开发卡片时，可通过该模块提供接口实现更新卡片，设置卡片更新时间，获取卡片信息，请求发布卡片等。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9 开始不再维护，建议使用[formProvider](@ohos.app.form.formProvider (formProvider).md)替代。

#### 导入模块

```ets
import { formProvider } from '@kit.FormKit';
```

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void

设置指定卡片的下一次更新时间，使用callback异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是卡片标识。minutenumber是指定多久之后更新。单位分钟，大于等于5。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
import Base from '@ohos.base';
import formProvider from '@ohos.application.formProvider';

let formId: string = '12400633174999288';
formProvider.setFormNextRefreshTime(formId, 5, (error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formProvider setFormNextRefreshTime, error: ${JSON.stringify(error)}`);
  }
});
```

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number): Promise<void>

设置指定卡片的下一次更新时间，使用Promise异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是卡片标识。minutenumber是指定多久之后更新。单位分钟，大于等于5。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import Base from '@ohos.base';
import formProvider from '@ohos.application.formProvider';

let formId: string = '12400633174999288';
formProvider.setFormNextRefreshTime(formId, 5).then(() => {
  console.info('formProvider setFormNextRefreshTime success');
}).catch((error: Base.BusinessError) => {
  console.error(`formProvider setFormNextRefreshTime, error: ${JSON.stringify(error)}`);
});
```

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData,callback: AsyncCallback<void>): void

更新指定的卡片，使用callback异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是请求更新的卡片标识。formBindingData[formBindingData.FormBindingData](@ohos.application.formBindingData (卡片数据绑定类).md#ZH-CN_TOPIC_0000002529285275__formbindingdata)是用于更新的数据。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
import Base from '@ohos.base';
import formBindingData from '@ohos.application.formBindingData';
import formProvider from '@ohos.application.formProvider';

let formId: string = '12400633174999288';
let param: Record<string, string> = {
  'temperature': '22c',
  'time': '22:00'
}
let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, obj, (error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formProvider updateForm, error: ${JSON.stringify(error)}`);
  }
});
```

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>

更新指定的卡片，使用Promise异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

参数名类型必填说明formIdstring是请求更新的卡片标识。formBindingData[formBindingData.FormBindingData](@ohos.application.formBindingData (卡片数据绑定类).md#ZH-CN_TOPIC_0000002529285275__formbindingdata)是用于更新的数据。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import Base from '@ohos.base';
import formBindingData from '@ohos.application.formBindingData';
import formProvider from '@ohos.application.formProvider';

let formId: string = '12400633174999288';
let param: Record<string, string> = {
  'temperature': '22c',
  'time': '22:00'
}
let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, obj).then(() => {
  console.info('formProvider updateForm success');
}).catch((error: Base.BusinessError) => {
  console.error(`formProvider updateForm, error: ${JSON.stringify(error)}`);
});
```