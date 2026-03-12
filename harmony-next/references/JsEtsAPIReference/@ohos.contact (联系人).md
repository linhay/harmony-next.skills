# @ohos.contact (联系人)

本模块提供联系人管理能力，包括添加联系人、删除联系人、更新联系人等。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { contact } from '@kit.ContactsKit';
```

#### contact.addContact10+

addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void

添加联系人。使用callback异步回调。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。callbackAsyncCallback<number>是回调函数。成功返回添加的联系人id；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.addContact(context, {
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to add Contact. Code:${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
  });
```

#### contact.addContact(deprecated)

addContact(contact: Contact, callback: AsyncCallback<number>): void

添加联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[addContact](#ZH-CN_TOPIC_0000002529286075__contactaddcontact10)替代。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。callbackAsyncCallback<number>是回调函数。成功返回添加的联系人id；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.addContact(context, {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxxxx'
  }]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to add Contact. Code:${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
});
```

#### contact.addContact10+

addContact(context: Context, contact: Contact): Promise<number>

添加联系人。使用Promise异步回调。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。

**返回值：**

类型说明Promise<number>Promise对象，返回添加的联系人id。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.addContact(context, {
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  });
  promise.then((data) => {
    console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to add Contact. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.addContact(deprecated)

addContact(contact: Contact): Promise<number>

添加联系人。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[addContact](#ZH-CN_TOPIC_0000002529286075__contactaddcontact10-1)替代。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。

**返回值：**

类型说明Promise<number>Promise对象，返回添加的联系人id。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.addContact({
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxxxx'
  }]
});
promise.then((data) => {
  console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to add Contact. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.deleteContact10+

deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void

删除联系人。使用callback异步回调。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。keystring是联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。callbackAsyncCallback<void>是回调函数。成功返回删除的联系人id；失败返回失败的错误码。

**错误码：**

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

 // 通过selectContacts接口选择联系人。
  contact.selectContacts().then((data) => {
    // 获取context。
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 第二个参数传入选择联系人的key值
    contact.deleteContact(context, data[0].key, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in deleting Contact.');
    });
  }).catch((err: BusinessError) => {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.deleteContact(deprecated)

deleteContact(key: string, callback: AsyncCallback<void>): void

删除联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[deleteContact](#ZH-CN_TOPIC_0000002529286075__contactdeletecontact10)替代。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明keystring是联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。callbackAsyncCallback<void>是回调函数。成功返回删除的联系人id；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // 第一个参数传入选择联系人的key值
  contact.deleteContact(data[0].key, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in deleting Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.deleteContact10+

deleteContact(context: Context, key: string): Promise<void>

删除联系人。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。keystring是联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // 第二个参数传入选择联系人的key值
  let promise = contact.deleteContact(context, data[0].key);
  promise.then(() => {
    console.info(`Succeeded in deleting Contact.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.deleteContact(deprecated)

deleteContact(key: string): Promise<void>

删除联系人。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[deleteContact](#ZH-CN_TOPIC_0000002529286075__contactdeletecontact10-1)替代。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明keystring是联系人的唯一查询键key值，一个联系人对应一个key，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 第一个参数传入选择联系人的key值
  let promise = contact.deleteContact(data[0].key);
  promise.then(() => {
    console.info(`Succeeded in deleting Contact.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.updateContact10+

updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>): void

更新联系人。使用callback异步回调。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。id必填，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。callbackAsyncCallback<void>是回调函数。成功返回更新的联系人id；失败返回失败的错误码。

**错误码：**

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data[0].id,  // 选择联系人的id。
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.updateContact(deprecated)

updateContact(contact: Contact, callback: AsyncCallback<void>): void

更新联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[updateContact](#ZH-CN_TOPIC_0000002529286075__contactupdatecontact10)替代。

**需要权限**：ohos.permission.WRITE_CONTACTS和ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。id必填，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。callbackAsyncCallback<void>是回调函数。成功返回更新的联系人id；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data[0].id,  // 选择联系人的id。
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.updateContact10+

updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void

更新联系人（支持传入联系人的属性列表）。使用callback异步回调。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。id必填，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<void>是回调函数。成功返回更新的联系人id；失败返回失败的错误码。

**错误码：**

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data[0].id,  // 选择联系人的id。
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.updateContact(deprecated)

updateContact(contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void

更新联系人（支持传入联系人的属性列表）。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[updateContact](#ZH-CN_TOPIC_0000002529286075__contactupdatecontact10-1)替代。

**需要权限**：ohos.permission.WRITE_CONTACTS和ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。id必填，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<void>是回调函数。成功返回更新的联系人id；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  contact.updateContact({
    id: data[0].id,  // 选择联系人的id。
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.updateContact10+

updateContact(context: Context, contact: Contact, attrs?: ContactAttributes): Promise<void>

更新联系人（支持传入联系人的属性列表）。使用Promise异步回调。

**需要权限**：ohos.permission.WRITE_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。id必填，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 通过selectContacts接口选择联系人。
  contact.selectContacts().then((data) => {
    // 获取context。
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let promise = contact.updateContact(context, {
      id: data[0].id,  // 选择联系人的id。
      name: {
        fullName: 'xxx'
      },
      phoneNumbers: [{
        phoneNumber: '138xxxxxxxx'
      }]
    }, {
      attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
    });
    promise.then(() => {
      console.info('Succeeded in updating Contact.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.updateContact(deprecated)

updateContact(contact: Contact, attrs?: ContactAttributes): Promise<void>

更新联系人（支持传入联系人的属性列表）。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[updateContact](#ZH-CN_TOPIC_0000002529286075__contactupdatecontact10-2)替代。

**需要权限**：ohos.permission.WRITE_CONTACTS和ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。id必填，可通过[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)接口获取。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  let promise = contact.updateContact({
    id: data[0].id,  // 选择联系人的id。
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  });
  promise.then(() => {
    console.info('Succeeded in updating Contact.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.isLocalContact10+

isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void

判断当前联系人id是否在电话簿中。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。idnumber是联系人对象的id属性，一个联系人对应一个id。callbackAsyncCallback<boolean>是回调函数。成功返回布尔值，true代表联系人id在本地电话簿中，false则代表联系人id不在本地电话簿中；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.isLocalContact(context, /*id*/1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
});
```

#### contact.isLocalContact(deprecated)

isLocalContact(id: number, callback: AsyncCallback<boolean>): void

判断当前联系人id是否在电话簿中。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isLocalContact](#ZH-CN_TOPIC_0000002529286075__contactislocalcontact10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明idnumber是联系人对象的id属性，一个联系人对应一个id。callbackAsyncCallback<boolean>是回调函数。成功返回布尔值，true代表联系人id在本地电话簿中，false则代表联系人id不在本地电话簿中；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.isLocalContact(/*id*/1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
});
```

#### contact.isLocalContact10+

isLocalContact(context: Context, id: number): Promise<boolean>

判断当前联系人id是否在电话簿中。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。idnumber是联系人对象的id属性，一个联系人对应一个id。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示联系人id在本地电话簿中，返回false表示联系人id不在本地电话簿中。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.isLocalContact(context, /*id*/1);
  promise.then((data) => {
    console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.isLocalContact(deprecated)

isLocalContact(id: number): Promise<boolean>

判断当前联系人id是否在电话簿中。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isLocalContact](#ZH-CN_TOPIC_0000002529286075__contactislocalcontact10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明idnumber是联系人对象的id属性，一个联系人对应一个id。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示联系人id在本地电话簿中，返回false表示联系人id不在本地电话簿中。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.isLocalContact(/*id*/1);
promise.then((data) => {
  console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.isMyCard10+

isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>): void

判断是否为“我的名片”。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。idnumber是名片对象的id属性。callbackAsyncCallback<boolean>是回调函数。成功返回是否为“我的名片”的布尔值。true代表的是“我的名片”，false则代表不是；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.isMyCard(context, /*id*/1, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
  });
```

#### contact.isMyCard(deprecated)

isMyCard(id: number, callback: AsyncCallback<boolean>): void

判断是否为“我的名片”。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isMyCard](#ZH-CN_TOPIC_0000002529286075__contactismycard10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明idnumber是名片对象的id属性。callbackAsyncCallback<boolean>是回调函数。成功返回是否为“我的名片”的布尔值。true代表的是“我的名片”，false则代表不是；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.isMyCard(/*id*/1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
});
```

#### contact.isMyCard10+

isMyCard(context: Context, id: number): Promise<boolean>

判断是否为“我的名片”。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。idnumber是名片对象的id属性。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示是“我的名片”，返回false表示不是。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.isMyCard(context, /*id*/1);
  promise.then((data) => {
    console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.isMyCard(deprecated)

isMyCard(id: number): Promise<boolean>

判断是否为“我的名片”。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[isMyCard](#ZH-CN_TOPIC_0000002529286075__contactismycard10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明idnumber是名片对象的id属性。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示是“我的名片”，返回false表示不是。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.isMyCard(/*id*/1);
promise.then((data) => {
  console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryMyCard10+

queryMyCard(context: Context, callback: AsyncCallback<Contact>): void

查询“我的名片”。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回“我的名片”信息；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  });
```

#### contact.queryMyCard(deprecated)

queryMyCard(callback: AsyncCallback<Contact>): void

查询“我的名片”。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryMyCard](#ZH-CN_TOPIC_0000002529286075__contactquerymycard10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回“我的名片”信息；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryMyCard((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
});
```

#### contact.queryMyCard10+

queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回“我的名片”信息；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  });
```

#### contact.queryMyCard(deprecated)

queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryMyCard](#ZH-CN_TOPIC_0000002529286075__contactquerymycard10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回“我的名片”信息；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryMyCard({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
});
```

#### contact.queryMyCard10+

queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>

查询“我的名片”（支持传入联系人的属性列表）。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表。

**返回值：**

类型说明Promise<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>Promise对象。返回“我的名片”联系人对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.queryMyCard(context, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  });
  promise.then((data) => {
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.queryMyCard(deprecated)

queryMyCard(attrs?: ContactAttributes): Promise<Contact>

查询“我的名片”（支持传入联系人的属性列表）。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryMyCard](#ZH-CN_TOPIC_0000002529286075__contactquerymycard10-2)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表。

**返回值：**

类型说明Promise<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>Promise对象。返回“我的名片”联系人对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryMyCard({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.selectContact(deprecated)

selectContact(callback: AsyncCallback<Array<Contact>>): void

调用选择联系人接口，打开选择联系人UI界面。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10)替代。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回选择的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.selectContact((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to select Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in selecting Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.selectContact(deprecated)

selectContact(): Promise<Array<Contact>>

调用选择联系人接口，打开选择联系人UI界面。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[selectContacts](#ZH-CN_TOPIC_0000002529286075__contactselectcontacts10-1)替代。

**系统能力**：SystemCapability.Applications.Contacts

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回选择的联系人数组对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.selectContact();
promise.then((data) => {
  console.info(`Succeeded in selecting Contact. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contact. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.selectContacts10+

selectContacts(callback: AsyncCallback<Array<Contact>>): void

调用选择联系人接口，打开选择联系人UI界面。使用callback异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回选择的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.selectContacts((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.selectContacts10+

selectContacts(): Promise<Array<Contact>>

调用选择联系人接口，打开选择联系人UI界面。使用Promise异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回选择的联系人数组对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.selectContacts();
promise.then((data) => {
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.selectContacts10+

selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void

调用选择联系人接口，打开选择联系人UI界面（选择联系人时支持传入筛选条件）。使用callback异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明options[ContactSelectionOptions](#ZH-CN_TOPIC_0000002529286075__contactselectionoptions10)是选择联系人时的筛选条件。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回选择的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.selectContacts({
  isMultiSelect:false
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.selectContacts10+

selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>

调用选择联系人接口，打开选择联系人UI界面（选择联系人时支持传入筛选条件）。使用Promise异步回调。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明options[ContactSelectionOptions](#ZH-CN_TOPIC_0000002529286075__contactselectionoptions10)是选择联系人时的筛选条件。

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回选择的联系人数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.selectContacts({isMultiSelect:false});
promise.then((data) => {
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContact10+

queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void

根据key查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。keystring是联系人的key值，一个联系人对应一个key。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContact(deprecated)

queryContact(key: string, callback: AsyncCallback<Contact>): void

根据key查询联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明keystring是联系人的key值，一个联系人对应一个key。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContact10+

queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void

根据key和holder查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。keystring是联系人的key值，一个联系人对应一个key。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContact(deprecated)

queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void

根据key和holder查询联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明keystring是联系人的key值，一个联系人对应一个key。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContact10+

queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key和attrs查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。keystring是联系人的key值，一个联系人对应一个key。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContact(deprecated)

queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key和attrs查询联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-2)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明keystring是联系人的key值，一个联系人对应一个key。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContact10+

queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key、holder和attrs查询联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。keystring是联系人的key值，一个联系人对应一个key。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // 获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryContact(context, 'xxx', {
    holderId: 1,
    bundleName: "",
    displayName: ""
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
  });
```

#### contact.queryContact(deprecated)

queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void

根据key、holder和attrs查询联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明keystring是联系人的key值，一个联系人对应一个key。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>是回调函数。成功返回查询的联系人对象；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContact('xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContact10+

queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>

根据key、holder和attrs查询联系人。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。keystring是联系人的key值，一个联系人对应一个key。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>Promise对象。返回查询到的联系人对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContact(context, 'xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContact(deprecated)

queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>

根据key、holder和attrs查询联系人。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-4)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明keystring是联系人的key值，一个联系人对应一个key。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>Promise对象。返回查询到的联系人对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryContact('xxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContacts10+

queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void

查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts(deprecated)

queryContacts(callback: AsyncCallback<Array<Contact>>): void

查询所有联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](#ZH-CN_TOPIC_0000002529286075__contactquerycontacts10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts10+

queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据holder查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts(deprecated)

queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据holder查询所有联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](#ZH-CN_TOPIC_0000002529286075__contactquerycontacts10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts({
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts10+

queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据attrs查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts(deprecated)

queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据attrs查询所有联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](#ZH-CN_TOPIC_0000002529286075__contactquerycontacts10-2)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts10+

queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据holder和attrs查询所有联系人。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContacts(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts(deprecated)

queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据holder和attrs查询所有联系人。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](#ZH-CN_TOPIC_0000002529286075__contactquerycontacts10-3)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContacts({
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContacts10+

queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据holder和attrs查询所有联系人。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回查询到的联系人数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContacts(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contacts. data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContacts(deprecated)

queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据holder和attrs查询所有联系人。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContacts](#ZH-CN_TOPIC_0000002529286075__contactquerycontacts10-4)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回查询到的联系人数组对象。

**示例：**

```ets
  import { BusinessError } from '@kit.BasicServicesKit';

  let promise = contact.queryContacts({
    holderId: 1,
    bundleName: "",
    displayName: ""
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  });
  promise.then((data) => {
    console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void

根据电话号码查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。phoneNumberstring是联系人的电话号码。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void

根据电话号码查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyphonenumber10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明phoneNumberstring是联系人的电话号码。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。phoneNumberstring是联系人的电话号码。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyphonenumber10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明phoneNumberstring是联系人的电话号码。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。phoneNumberstring是联系人的电话号码。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyphonenumber10-2)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明phoneNumberstring是联系人的电话号码。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。phoneNumberstring是联系人的电话号码。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据电话号码、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyphonenumber10-3)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明phoneNumberstring是联系人的电话号码。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByPhoneNumber10+

queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据电话号码、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。phoneNumberstring是联系人的电话号码。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回查询到的联系人数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsByPhoneNumber(context, '138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContactsByPhoneNumber(deprecated)

queryContactsByPhoneNumber(phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据电话号码、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByPhoneNumber](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyphonenumber10-4)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明phoneNumberstring是联系人的电话号码。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回查询到的联系人数组对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryContactsByPhoneNumber('138xxxxxxxx', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contacts By PhoneNumber. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Contacts By PhoneNumber. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, callback: AsyncCallback<Array<Contact>>): void

根据email查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。emailstring是联系人的邮箱地址。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, callback: AsyncCallback<Array<Contact>>): void

根据email查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyemail10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明emailstring是联系人的邮箱地址。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据email和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。emailstring是联系人的邮箱地址。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void

根据email和holder查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyemail10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明emailstring是联系人的邮箱地址。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。emailstring是联系人的邮箱地址。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', {
  attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyemail10-2)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明emailstring是联系人的邮箱地址。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', {
  attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。emailstring是联系人的邮箱地址。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContactsByEmail(context, 'xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void

根据email、holder和attrs查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyemail10-3)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明emailstring是联系人的邮箱地址。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)是联系人的属性列表。callbackAsyncCallback<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>是回调函数。成功返回查询到的联系人对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryContactsByEmail('xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
});
```

#### contact.queryContactsByEmail10+

queryContactsByEmail(context: Context, email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据email、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。emailstring是联系人的邮箱地址。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回查询到的联系人数组对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsByEmail(context, 'xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContactsByEmail(deprecated)

queryContactsByEmail(email: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>

根据email、holder和attrs查询联系人。使用Promise异步回调。该接口仅返回联系人信息中的id、key、Emails属性。如果要查询联系人的所有信息，建议使用[queryContact](#ZH-CN_TOPIC_0000002529286075__contactquerycontact10-3)接口，根据该接口返回的属性key查询。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryContactsByEmail](#ZH-CN_TOPIC_0000002529286075__contactquerycontactsbyemail10-4)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明emailstring是联系人的邮箱地址。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。attrs[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否联系人的属性列表，不传默认查询所有联系人属性。

**返回值：**

类型说明Promise<Array<[Contact](#ZH-CN_TOPIC_0000002529286075__contact)>>Promise对象。返回查询到的联系人数组对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryContactsByEmail('xxx@email.com', {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, {
  attributes: [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contacts By Email. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Contacts By Email. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryGroups10+

queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void

查询联系人的所有群组。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。callbackAsyncCallback<Array<[Group](#ZH-CN_TOPIC_0000002529286075__group)>>是回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。

**错误码：**

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryGroups(context, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```

#### contact.queryGroups(deprecated)

queryGroups(callback: AsyncCallback<Array<Group>>): void

查询联系人的所有群组。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryGroups](#ZH-CN_TOPIC_0000002529286075__contactquerygroups10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[Group](#ZH-CN_TOPIC_0000002529286075__group)>>是回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryGroups((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups.. data->${JSON.stringify(data)}`);
});
```

#### contact.queryGroups10+

queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void

根据holder查询联系人的所有群组。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Group](#ZH-CN_TOPIC_0000002529286075__group)>>是回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryGroups(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```

#### contact.queryGroups(deprecated)

queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void

根据holder查询联系人的所有群组。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryGroups](#ZH-CN_TOPIC_0000002529286075__contactquerygroups10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<Array<[Group](#ZH-CN_TOPIC_0000002529286075__group)>>是回调函数。成功返回查询到的群组对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryGroups({
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```

#### contact.queryGroups10+

queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>

根据holder查询联系人的所有群组。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人群组。

**返回值：**

类型说明Promise<Array<[Group](#ZH-CN_TOPIC_0000002529286075__group)>>Promise对象。返回查询到的群组对象数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryGroups(context, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryGroups(deprecated)

queryGroups(holder?: Holder): Promise<Array<Group>>

根据holder查询联系人的所有群组。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryGroups](#ZH-CN_TOPIC_0000002529286075__contactquerygroups10-2)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人群组。

**返回值：**

类型说明Promise<Array<[Group](#ZH-CN_TOPIC_0000002529286075__group)>>Promise对象。返回查询到的群组对象数组。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryGroups({
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryHolders10+

queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void

查询所有创建联系人的应用信息。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。callbackAsyncCallback<Array<[Holder](#ZH-CN_TOPIC_0000002529286075__holder)>>是回调函数。成功返回查询到的创建联系人应用信息的对象数组；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryHolders(context, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
});
```

#### contact.queryHolders(deprecated)

queryHolders(callback: AsyncCallback<Array<Holder>>): void

查询所有创建联系人的应用信息。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryHolders](#ZH-CN_TOPIC_0000002529286075__contactqueryholders10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[Holder](#ZH-CN_TOPIC_0000002529286075__holder)>>是回调函数。成功返回查询到的创建联系人应用信息的对象数组；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryHolders((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
});
```

#### contact.queryHolders10+

queryHolders(context: Context): Promise<Array<Holder>>

查询所有创建联系人的应用信息。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

**返回值：**

类型说明Promise<Array<[Holder](#ZH-CN_TOPIC_0000002529286075__holder)>>Promise对象。返回查询到的创建联系人应用信息的对象数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: Mandatory parameters are left unspecified.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryHolders(context);
promise.then((data) => {
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryHolders(deprecated)

queryHolders(): Promise<Array<Holder>>

查询所有创建联系人的应用信息。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryHolders](#ZH-CN_TOPIC_0000002529286075__contactqueryholders10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**返回值：**

类型说明Promise<Array<[Holder](#ZH-CN_TOPIC_0000002529286075__holder)>>Promise对象。返回查询到的创建联系人应用信息的对象数组。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryHolders();
promise.then((data) => {
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryKey10+

queryKey(context: Context, id: number, callback: AsyncCallback<string>): void

根据联系人的id查询联系人的key。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。idnumber是联系人对象的id属性。callbackAsyncCallback<string>是回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryKey(context, /*id*/1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

#### contact.queryKey(deprecated)

queryKey(id: number, callback: AsyncCallback<string>): void

根据联系人的id查询联系人的key。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryKey](#ZH-CN_TOPIC_0000002529286075__contactquerykey10)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明idnumber是联系人对象的id属性。callbackAsyncCallback<string>是回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryKey(/*id*/1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

#### contact.queryKey10+

queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void

根据联系人的id和holder查询联系人的key。使用callback异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。idnumber是联系人对象的id属性。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<string>是回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryKey(context, /*id*/1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

#### contact.queryKey(deprecated)

queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void

根据联系人的id和holder查询联系人的key。使用callback异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryKey](#ZH-CN_TOPIC_0000002529286075__contactquerykey10-1)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明idnumber是联系人对象的id属性。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)是创建联系人的应用信息。callbackAsyncCallback<string>是回调函数。成功返回查询到的联系人对应的key；失败返回失败的错误码。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryKey(/*id*/1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

#### contact.queryKey10+

queryKey(context: Context, id: number, holder?: Holder): Promise<string>

根据联系人的id和holder查询联系人的key。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。idnumber是联系人对象的id属性。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。

**返回值：**

类型说明Promise<string>Promise对象。返回查询到的联系人对应的key。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryKey(context, /*id*/1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryKey(deprecated)

queryKey(id: number, holder?: Holder): Promise<string>

根据联系人的id和holder查询联系人的key。使用Promise异步回调。

从API version 7 开始支持，从API version 10 开始废弃，建议使用[queryKey](#ZH-CN_TOPIC_0000002529286075__contactquerykey10-2)替代。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明idnumber是联系人对象的id属性。holder[Holder](#ZH-CN_TOPIC_0000002529286075__holder)否创建联系人的应用信息，不传默认不使用该条件过滤联系人。

**返回值：**

类型说明Promise<string>Promise对象。返回查询到的联系人对应的key。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryKey(/*id*/1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.queryContactsCount22+

queryContactsCount(context: Context): Promise<int>

查询所有联系人的数量。使用Promise异步回调。

**需要权限**：ohos.permission.READ_CONTACTS

**系统能力**：SystemCapability.Applications.ContactsData

**参数：**

参数名类型必填说明context[Context](Context (Stage模型的上下文基类).md)是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

**返回值：**

类型说明Promise<int>Promise对象。返回查询到的联系人数量。

**示例：**

```ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 获取context。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsCount(context);
promise.then((data) => {
  console.info(`Succeeded in querying ContactsCount. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query ContactsCount. Code: ${err.code}, message: ${err.message}`);
});
```

#### contact.addContactViaUI15+

addContactViaUI(context: Context, contact: Contact): Promise<number>

调用新建联系人接口，打开新建联系人UI界面，新建完成。使用Promise异步回调。

**元服务API**: 从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。

**返回值：**

类型说明Promise<number>Promise对象。返回添加的联系人id。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[Contacts错误码](Contacts错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Mandatory parameters are left unspecified.801The specified SystemCapability name was not found.16700001General error.16700102Failed to set value to contacts data.16700103User cancel.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 获取context。
let contactInfo: contact.Contact = {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxx'
  }]
}
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.addContactViaUI(context, contactInfo);
promise.then((data) => {
    console.info(`Succeeded in add Contact via UI.data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to add Contact via UI. Code: ${err.code}, message: ${err.message}`);
  });
```

#### contact.saveToExistingContactViaUI15+

saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>

调用保存至已有联系人接口，选择联系人UI界面并完成编辑。使用Promise异步回调。

**元服务API**: 从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明contextContext是应用上下文Context，Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。contact[Contact](#ZH-CN_TOPIC_0000002529286075__contact)是联系人信息。

**返回值：**

类型说明Promise<number>Promise对象。返回添加的联系人id。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[Contacts错误码](Contacts错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: Mandatory parameters are left unspecified.801The specified SystemCapability name was not found.16700001General error.16700101Failed to get value to contacts data.16700102Failed to set value to contacts data.16700103User cancel.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 获取context。
let contactInfo: contact.Contact = {
  id: 1,
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxx'
  }]
}
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.saveToExistingContactViaUI(context, contactInfo);
promise.then((data) => {
    console.info(`Succeeded in save to existing Contact via UI.data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to save to existing Contact via UI. Code: ${err.code}, message: ${err.message}`);
  });
```

#### ContactSelectionOptions10+

选择联系人条件。

**系统能力**：SystemCapability.Applications.Contacts

名称类型只读可选说明isMultiSelect10+boolean否是是否为多选，true:多选，false:单选。默认值为false。**元服务API**：从API version 11 开始，该接口支持在元服务中使用。maxSelectable15+number否是联系人选择数量上限。默认值为10000。**元服务API**：从API version 15 开始，该接口支持在元服务中使用。isDisplayedByName15+boolean否是是否按联系人姓名维度展示，true:按联系人姓名维度展示，false:按联系人号码维度展示。默认值为false。**元服务API**：从API version 15 开始，该接口支持在元服务中使用。filter15+[ContactSelectionFilter](#ZH-CN_TOPIC_0000002529286075__contactselectionfilter15)否是联系人查询过滤器。**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

#### ContactSelectionFilter15+

联系人查询过滤器。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

名称类型只读可选说明filterClause[FilterClause](#ZH-CN_TOPIC_0000002529286075__filterclause15)否否过滤条件。filterType[FilterType](#ZH-CN_TOPIC_0000002529286075__filtertype15)否否过滤类型。

#### FilterType15+

枚举，联系人过滤类型。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称值说明SHOW_FILTER0

仅展示符合过滤条件的联系人。

**系统能力**：SystemCapability.Applications.Contacts

DEFAULT_SELECT1

默认勾选符合过滤条件的联系人。

**系统能力**：SystemCapability.Applications.Contacts

SHOW_FILTER_AND_DEFAULT_SELECT2

默认勾选仅展示符合过滤条件的联系人。

**系统能力**：SystemCapability.Applications.Contacts

#### FilterClause15+

联系人过滤条件。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

名称类型只读可选说明idArray<[FilterOptions](#ZH-CN_TOPIC_0000002529286075__filteroptions15)>否是联系人id。nameArray<[FilterOptions](#ZH-CN_TOPIC_0000002529286075__filteroptions15)>否是联系人姓名。dataItem[DataFilter](#ZH-CN_TOPIC_0000002529286075__datafilter15)否是联系人数据过滤项。focusModeListArray<[FilterOptions](#ZH-CN_TOPIC_0000002529286075__filteroptions15)>否是专注模式。

#### FilterOptions15+

联系人过滤参数。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

名称类型只读可选说明filterCondition[FilterCondition](#ZH-CN_TOPIC_0000002529286075__filtercondition15)否否过滤条件。valuestring | ValueType[]否是过滤值，默认为undefined。

#### FilterCondition15+

枚举，过滤条件。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称值说明IS_NOT_NULL0

对应字段不为空。

**系统能力**：SystemCapability.Applications.Contacts

EQUAL_TO1

对应字段等于某值。

**系统能力**：SystemCapability.Applications.Contacts

NOT_EQUAL_TO2

对应字段不等于某值。

**系统能力**：SystemCapability.Applications.Contacts

IN3

对应字段值在某数组中。

**系统能力**：SystemCapability.Applications.Contacts

NOT_IN4

对应字段值不在某数组中。

**系统能力**：SystemCapability.Applications.Contacts

CONTAINS5

对应字段值包含某值

**系统能力**：SystemCapability.Applications.Contacts。

#### DataFilter15+

联系人数据过滤项。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

名称类型只读可选说明field[DataField](#ZH-CN_TOPIC_0000002529286075__datafield15)否否联系人数据字段。optionsArray<[FilterOptions](#ZH-CN_TOPIC_0000002529286075__filteroptions15)>否否过滤参数。

#### DataField15+

枚举，联系人数据字段。

**元服务API**：从API version 15 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称值说明EMAIL0

联系人邮箱。

**系统能力**：SystemCapability.Applications.Contacts。

PHONE1

联系人电话。

**系统能力**：SystemCapability.Applications.Contacts。

ORGANIZATION2

联系人单位。

**系统能力**：SystemCapability.Applications.Contacts。

#### Contact

联系人对象类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明INVALID_CONTACT_IDnumber-1默认联系人的id。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明idnumber是是联系人的id，由系统自动生成。keystring是是联系人的key，由系统自动生成。contactAttributes[ContactAttributes](#ZH-CN_TOPIC_0000002529286075__contactattributes)否是联系人的属性列表。emails[Email](#ZH-CN_TOPIC_0000002529286075__email)[]否是联系人的邮箱地址列表。events[Event](#ZH-CN_TOPIC_0000002529286075__event)[]否是联系人的生日、周年纪念等重要日期列表。groups[Group](#ZH-CN_TOPIC_0000002529286075__group)[]否是联系人的群组列表。imAddresses[ImAddress](#ZH-CN_TOPIC_0000002529286075__imaddress)[]否是联系人的即时消息地址列表。phoneNumbers[PhoneNumber](#ZH-CN_TOPIC_0000002529286075__phonenumber)[]否是联系人的电话号码列表。portrait[Portrait](#ZH-CN_TOPIC_0000002529286075__portrait)否是联系人的头像。postalAddresses[PostalAddress](#ZH-CN_TOPIC_0000002529286075__postaladdress)[]否是联系人的邮政地址列表。relations[Relation](#ZH-CN_TOPIC_0000002529286075__relation)[]否是联系人的关系列表。sipAddresses[SipAddress](#ZH-CN_TOPIC_0000002529286075__sipaddress)[]否是联系人的会话发起协议(SIP)地址列表。websites[Website](#ZH-CN_TOPIC_0000002529286075__website)[]否是联系人的网站列表。name[Name](#ZH-CN_TOPIC_0000002529286075__name)否是联系人的姓名。nickName[NickName](#ZH-CN_TOPIC_0000002529286075__nickname)否是联系人的昵称。note[Note](#ZH-CN_TOPIC_0000002529286075__note)否是联系人的备注。organization[Organization](#ZH-CN_TOPIC_0000002529286075__organization)否是联系人的组织信息。

**对象创建示例：**

使用JSON格式创建联系人数据。

```ets
let myContact: contact.Contact = {
    phoneNumbers: [{
        phoneNumber: "138xxxxxxxx"
    }],
    name: {
        fullName: "fullName",
        namePrefix: "namePrefix"
    },
    nickName: {
        nickName: "nickName"
    }
};
```

#### ContactAttributes

联系人属性列表，一般作为入参用来标识希望查询的联系人属性。

当传入为null时，默认查询全部属性。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明attributes[Attribute](#ZH-CN_TOPIC_0000002529286075__attribute)[]否否联系人属性列表。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let contactAttributes: contact.ContactAttributes = {
    attributes: [
        contact.Attribute.ATTR_EMAIL,
        contact.Attribute.ATTR_NAME,
        contact.Attribute.ATTR_PHONE
    ]
};
```

#### Attribute

枚举，联系人属性列表。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称值说明ATTR_CONTACT_EVENT0联系人的生日、周年纪念等重要日期。ATTR_EMAIL1联系人的邮箱地址。ATTR_GROUP_MEMBERSHIP2联系人的群组。ATTR_IM3联系人的即时消息地址。ATTR_NAME4联系人的姓名。ATTR_NICKNAME5联系人的昵称。ATTR_NOTE6联系人的备注。ATTR_ORGANIZATION7联系人的组织信息。ATTR_PHONE8联系人的电话号码。ATTR_PORTRAIT9联系人的头像。ATTR_POSTAL_ADDRESS10联系人的邮政地址。ATTR_RELATION11联系人的关系。ATTR_SIP_ADDRESS12联系人的会话发起协议(SIP)地址。ATTR_WEBSITE13联系人的网站。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let attributes = [contact.Attribute.ATTR_EMAIL, contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE];
```

#### Email

联系人的邮箱。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明CUSTOM_LABELnumber0自定义邮箱类型。EMAIL_HOMEnumber1家庭邮箱类型。EMAIL_WORKnumber2工作邮箱类型。EMAIL_OTHERnumber3其它邮箱类型。INVALID_LABEL_IDnumber-1无效邮箱类型。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明emailstring否否邮箱地址。labelNamestring否是邮箱的类型名称。displayNamestring否是邮箱的显示名称。labelIdnumber否是邮箱的类型。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let email: contact.Email = {
    email: "xxx@email.com",
    displayName: "displayName"
}
```

或使用new一个Email对象的方式创建数据。

```ets
let email = new contact.Email();
email.email = "xxx@email.com";
```

#### Holder

创建联系人的应用信息类。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明bundleNamestring是否Bundle名称，值为com.ohos.contacts。displayNamestring是是应用名称。holderIdnumber否是应用Id。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let holder: contact.Holder = {
  bundleName: "com.ohos.contacts",
  displayName: "displayName",
  holderId: 1
};
```

#### Event

联系人事件类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明CUSTOM_LABELnumber0自定义事件类型。EVENT_ANNIVERSARYnumber1周年纪念事件类型。EVENT_OTHERnumber2其它事件类型。EVENT_BIRTHDAYnumber3生日事件类型。INVALID_LABEL_IDnumber-1无效事件类型。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明eventDatestring否否事件的日期。labelNamestring否是事件类型名称。labelIdnumber否是事件类型。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let event: contact.Event = {
    eventDate: "2000-01-01"
};
```

或使用new一个Event对象的方式创建数据。

```ets
let event = new contact.Event();
event.eventDate = "2000-01-01";
```

#### Group

联系人的群组类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明groupIdnumber否是联系人群组的Id。titlestring否否联系人群组的名称。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let group: contact.Group = {
    groupId: 1,
    title: "title"
};
```

#### ImAddress

联系人的即时消息地址。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明CUSTOM_LABELnumber-1自定义即时消息类型。IM_AIMnumber0AIM即时消息类型。IM_MSNnumber1MSN即时消息类型。IM_YAHOOnumber2YAHOO即时消息类型。IM_SKYPEnumber3SKYPE即时消息类型。IM_QQnumber4QQ即时消息类型。IM_ICQnumber6ICQ即时消息类型。IM_JABBERnumber7JABBER即时消息类型。INVALID_LABEL_IDnumber-2无效的即时消息类型。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明imAddressstring否否即时消息地址。labelNamestring否是即时消息类型名称。labelIdnumber否是即时消息类型。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let imAddress: contact.ImAddress = {
    imAddress: "imAddress",
    labelName: "labelName"
};
```

或使用new一个ImAddress对象的方式创建数据。

```ets
let imAddress = new contact.ImAddress();
imAddress.imAddress = "imAddress";
```

#### Name

联系人的名字类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明familyNamestring否是联系人的家庭姓名。familyNamePhoneticstring否是联系人的家庭姓名拼音。fullNamestring否否联系人的全名。givenNamestring否是联系人的名称(firstName)。givenNamePhoneticstring否是联系人的名称拼音。middleNamestring否是联系人的中间名。middleNamePhoneticstring否是联系人的中间名拼音。namePrefixstring否是联系人的姓名前缀。nameSuffixstring否是联系人的姓名后缀。hasName22+boolean否是联系人信息中是否包含姓名。true表示包含，false表示不包含。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let name: contact.Name = {
    familyName: "familyName",
    fullName: "fullName"
};
```

#### NickName

联系人的昵称类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明nickNamestring否否联系人的昵称。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let nickName: contact.NickName = {
    nickName: "nickName"
};
```

#### Note

联系人的备注类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明noteContentstring否否联系人的备注内容。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let note: contact.Note = {
    noteContent: "noteContent"
};
```

#### Organization

联系人的组织类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明namestring否否单位名称。titlestring否是职位名称。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let organization: contact.Organization = {
    name: "name",
    title: "title"
};
```

#### PhoneNumber

联系人电话号码类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明CUSTOM_LABELnumber0自定义电话类型。NUM_HOMEnumber1家庭电话类型。NUM_MOBILEnumber2移动电话类型。NUM_WORKnumber3工作电话类型。NUM_FAX_WORKnumber4工作传真电话类型。NUM_FAX_HOMEnumber5家庭传真电话类型。NUM_PAGERnumber6寻呼机电话类型。NUM_OTHERnumber7其它电话类型。NUM_CALLBACKnumber8回呼电话类型。NUM_CARnumber9车机电话类型。NUM_COMPANY_MAINnumber10公司电话类型。NUM_ISDNnumber11综合业务数字网(ISDN)电话类型。NUM_MAINnumber12主电话类型。NUM_OTHER_FAXnumber13其它传真类型。NUM_RADIOnumber14无线电话类型。NUM_TELEXnumber15电传电话类型。NUM_TTY_TDDnumber16电传打字机(TTY)或测试驱动开发(TDD)电话类型。NUM_WORK_MOBILEnumber17工作移动电话类型。NUM_WORK_PAGERnumber18工作寻呼机电话类型。NUM_ASSISTANTnumber19助理电话类型。NUM_MMSnumber20彩信电话类型。INVALID_LABEL_IDnumber-1无效电话类型。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明labelNamestring否是电话号码类型名称。phoneNumberstring否否电话号码。labelIdnumber否是电话号码类型。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let phoneNumber: contact.PhoneNumber = {
    phoneNumber: "138xxxxxxxx",
    labelId: contact.PhoneNumber.NUM_HOME
};
```

或使用new一个PhoneNumber对象的方式创建数据。

```ets
let phoneNumber = new contact.PhoneNumber();
phoneNumber.phoneNumber = "138xxxxxxxx";
```

#### Portrait

联系人的头像类。

从API version 22开始，支持通过uri和[PixelMap](Interface (PixelMap).md)格式设置联系人头像资源(暂不支持通过[addContactViaUI](#ZH-CN_TOPIC_0000002529286075__contactaddcontactviaui15)、[saveToExistingContactViaUI](#ZH-CN_TOPIC_0000002529286075__contactsavetoexistingcontactviaui15)接口设置)。

uri为可访问的联系人头像文件地址，[PixelMap](Interface (PixelMap).md)为通过联系人头像资源生成的[PixelMap](Interface (PixelMap).md)对象。

读取联系人头像资源仅支持uri格式，该格式仅支持以[fs.open](@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsopen)方式打开，无法直接在Image组件内显示，需读取后转换为[PixelMap](Interface (PixelMap).md)格式显示。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明uristring否否uri格式联系人头像。photo22+[image.PixelMap](Interface (PixelMap).md)否是pixelMap格式的联系人头像。

**对象创建示例：**

使用JSON格式创建数据。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function SetPortraitUri(uri: string) {
  let portrait: contact.Portrait = {
    uri: uri
  };
}

async function SetPortraitPixelMap(photo: image.PixelMap) {
  let portrait: contact.Portrait = {
    uri: "",
    photo: photo
  };
}
```

#### PostalAddress

联系人的邮政地址类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明CUSTOM_LABELnumber0自定义邮政地址类型。ADDR_HOMEnumber1家庭地址类型。ADDR_WORKnumber2工作地址类型。ADDR_OTHERnumber3其它地址类型。INVALID_LABEL_IDnumber-1无效地址类型。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明citystring否是联系人所在的城市。countrystring否是联系人所在的国家。labelNamestring否是邮政地址类型名称。neighborhoodstring否是联系人的邻居。poboxstring否是联系人的邮箱。postalAddressstring否否联系人的邮政地址。postcodestring否是联系人所在区域的邮政编码。regionstring否是联系人所在的区域。streetstring否是联系人所在的街道。labelIdnumber否是邮政地址类型。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let postalAddress: contact.PostalAddress = {
    city: "city",
    postalAddress: "postalAddress"
};
```

或使用new一个PostalAddress对象的方式创建数据。

```ets
let postalAddress = new contact.PostalAddress();
postalAddress.city = "city";
postalAddress.postalAddress = "postalAddress";
```

#### Relation

联系人的关系类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明CUSTOM_LABELnumber0自定义关系类型。RELATION_ASSISTANTnumber1助手关系类型。RELATION_BROTHERnumber2兄弟关系类型。RELATION_CHILDnumber3子女关系类型。RELATION_DOMESTIC_PARTNERnumber4同居同伴关系类型。RELATION_FATHERnumber5父亲关系类型。RELATION_FRIENDnumber6朋友关系类型。RELATION_MANAGERnumber7管理者关系类型。RELATION_MOTHERnumber8母亲关系类型。RELATION_PARENTnumber9父母关系类型。RELATION_PARTNERnumber10合作伙伴关系类型。RELATION_REFERRED_BYnumber11推荐人关系类型。RELATION_RELATIVEnumber12亲属关系类型。RELATION_SISTERnumber13姐妹关系类型。RELATION_SPOUSEnumber14配偶关系类型。INVALID_LABEL_IDnumber-1无效的关系类型。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明labelNamestring否是关系类型名称。relationNamestring否否关系名称。labelIdnumber否是关系类型。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let relation: contact.Relation = {
    relationName: "relationName",
    labelId: contact.Relation.RELATION_ASSISTANT
};
```

或使用new一个Relation对象的方式创建数据。

```ets
let relation = new contact.Relation();
relation.relationName = "relationName";
relation.labelId = contact.Relation.RELATION_ASSISTANT;
```

#### SipAddress

联系人的会话发起协议(SIP)地址类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

#### 常量

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型值说明CUSTOM_LABELnumber0自定义会话发起协议(SIP)地址类型。SIP_HOMEnumber1家庭会话发起协议(SIP)地址类型。SIP_WORKnumber2工作会话发起协议(SIP)地址类型。SIP_OTHERnumber3其它会话发起协议(SIP)地址类型。INVALID_LABEL_IDnumber-1无效会话发起协议(SIP)地址类型。

#### 属性

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明labelNamestring否是会话发起协议(SIP)地址类型名称。sipAddressstring否否会话发起协议(SIP)地址。labelIdnumber否是会话发起协议(SIP)地址类型。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let sipAddress: contact.SipAddress = {
    sipAddress: "sipAddress"
};
```

或使用new一个SipAddress对象的方式创建数据。

```ets
let sipAddress = new contact.SipAddress();
sipAddress.sipAddress = "sipAddress";
```

#### Website

联系人的网站信息类。

**元服务API**：从API version 11 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.ContactsData

名称类型只读可选说明websitestring否否联系人的网站信息。

**对象创建示例：**

使用JSON格式创建数据。

```ets
let website: contact.Website = {
    website: "website"
};
```