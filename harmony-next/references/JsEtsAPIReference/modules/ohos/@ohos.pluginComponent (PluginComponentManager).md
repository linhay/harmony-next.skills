# @ohos.pluginComponent (PluginComponentManager)

用于给插件组件的使用方请求组件与数据，使用方发送组件模板和数据。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { pluginComponentManager } from '@kit.ArkUI';
```

#### PluginComponentTemplate

Plugin组件模板参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| source | string | 否 | 否 | 组件模板名。 |
| ability | string | 否 | 否 | 提供方Ability的bundleName。 |

#### pluginComponentManager

插件组件管理器。

#### KVObject

type KVObject = { [key: string]: number | string | boolean | [] | KVObject }

以键值对形式存储信息，符合json格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [key: string] | number | string | boolean | [] | KVObject | 否 | 键值对形式存储。 number：键值，表示值类型为数字。  string：键值，表示值类型为字符串，可取空字符串。  boolean：键值，表示值类型为布尔值。  []：键值，可取值为[]。 KVObject：键值，表示值类型为KVObject。 |

#### PushParameters

使用PluginManager.Push方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | Want | 否 | 否 | 组件使用方Ability信息。 |
| name | string | 否 | 否 | 组件名称。 |
| data | KVObject | 否 | 否 | 组件数据。 |
| extraData | KVObject | 否 | 否 | 附加数据。 |
| jsonPath | string | 否 | 是 | 存放模板路径的external.json文件的路径。 |

#### RequestParameters

使用PluginManager.Request方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | Want | 否 | 否 | 组件提供方Ability信息。 |
| name | string | 否 | 否 | 请求组件名称。 |
| data | KVObject | 否 | 否 | 组件数据。 |
| jsonPath | string | 否 | 是 | 存放模板路径的external.json文件的路径。当jsonPath字段不为空时不触发Request通信。 |

#### RequestCallbackParameters

PluginManager.Request方法接收到的回调结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| componentTemplate | PluginComponentTemplate | 否 | 否 | 组件模板。 |
| data | KVObject | 否 | 否 | 组件数据。 |
| extraData | KVObject | 否 | 否 | 附加数据。 |

#### RequestEventResult

注册Request监听方法后，接收到请求事件时回应请求的数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| template | string | 否 | 是 | 组件模板。 |
| data | KVObject | 否 | 是 | 组件数据。 |
| extraData | KVObject | 否 | 是 | 附加数据。 |

#### OnPushEventCallback

type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject, extraData: KVObject) => void

对应Push事件的监听回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | Want | 是 | Push请求发送方相关信息。 |
| template | PluginComponentTemplate | 是 | 请求组件模板名称。 |
| data | KVObject | 是 | 数据。 |
| extraData | KVObject | 是 | 附加数据。 |

**示例：**

```ets
import { pluginComponentManager, PluginComponentTemplate } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

function onPushListener(source: Want, template: PluginComponentTemplate, data: pluginComponentManager.KVObject, extraData: pluginComponentManager.KVObject) {
  console.info("onPushListener template.source=" + template.source);
  console.info("onPushListener source=" + JSON.stringify(source));
  console.info("onPushListener template=" + JSON.stringify(template));
  console.info("onPushListener data=" + JSON.stringify(data));
  console.info("onPushListener extraData=" + JSON.stringify(extraData));
}
```

#### OnRequestEventCallback

type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult

对应request事件的监听回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | Want | 是 | request请求发送方相关信息。 |
| name | string | 是 | 模板名称。 |
| data | KVObject | 是 | 数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RequestEventResult | 注册Request监听方法后，接收到请求事件时回应请求的数据类型。 |

**示例：**

```ets
import { pluginComponentManager } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

function onRequestListener(source: Want, name: string, data: pluginComponentManager.KVObject) {
  console.info("onRequestListener");
  console.info("onRequestListener source=" + JSON.stringify(source));
  console.info("onRequestListener name=" + name);
  console.info("onRequestListener data=" + JSON.stringify(data));
  let RtnData: Record<string, string | pluginComponentManager.KVObject> = {
    'template': "ets/pages/plugin.js",
    'data': data,
  }
  return RtnData;
}
```

#### pluginComponentManager.push

push(param: PushParameters , callback: AsyncCallback<void>): void

组件提供方向组件使用方主动发送组件和数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | PushParameters | 是 | 组件使用方的详细信息。 |
| callback | AsyncCallback<void> | 是 | 此次接口调用的异步回调。 |

**示例：**

```ets
import { pluginComponentManager } from '@kit.ArkUI';

pluginComponentManager.push(
  {
    want: {
      bundleName: "com.example.provider",
      abilityName: "com.example.provider.MainAbility",
    },
    name: "plugintemplate",
    data: {
      "key_1": "plugin component test",
      "key_2": 34234,
    },
    extraData: {
      "extra_str": "this is push event",
    },
    jsonPath: "",
  },
  (err) => {
    console.info("push_callback: push ok!");
  }
)
```

#### pluginComponentManager.request

request(param: RequestParameters, callback: AsyncCallback<RequestCallbackParameters>): void

组件使用方向组件提供方主动请求组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | RequestParameters | 是 | 组件模板的详细请求信息。 |
| callback | AsyncCallback<RequestCallbackParameters> | 是 | 此次请求的异步回调，通过回调接口的参数返回接收请求的数据。 |

**示例：**

```ets
import { pluginComponentManager } from '@kit.ArkUI';

pluginComponentManager.request(
  {
    want: {
      bundleName: "com.example.provider",
      abilityName: "com.example.provider.MainAbility",
    },
    name: "plugintemplate",
    data: {
      "key_1": "plugin component test",
      "key_2": 1111111,
    },
    jsonPath: "",
  },
  (err, data) => {
    console.info("request_callback: componentTemplate.ability=" + data.componentTemplate.ability);
    console.info("request_callback: componentTemplate.source=" + data.componentTemplate.source);
    console.info("request_callback: data=" + JSON.stringify(data.data));
    console.info("request_callback: extraData=" + JSON.stringify(data.extraData));
  }
)
```

#### pluginComponentManager.on

on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback ): void

提供方监听"request"类型的事件，给使用方返回通过request接口主动请求的数据；使用方监听"push"类型的事件，接收提供方通过push接口主动推送的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听的事件类型， 可选值为："push" 、"request"。 "push”：指组件提供方向使用方主动推送数据。 "request”：指组件使用方向提供方主动请求数据。 |
| callback | OnPushEventCallback | OnRequestEventCallback | 是 | 对应监听回调，push事件对应回调类型为OnPushEventCallback，request事件对应回调类型为OnRequestEventCallback 。 |

**示例：**

```ets
import { pluginComponentManager, PluginComponentTemplate } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

function onPushListener(source:Want, template:PluginComponentTemplate, data:pluginComponentManager.KVObject, extraData:pluginComponentManager.KVObject) {
  console.info("onPushListener template.source=" + template.source);
  console.info("onPushListener source=" + JSON.stringify(source));
  console.info("onPushListener template=" + JSON.stringify(template));
  console.info("onPushListener data=" + JSON.stringify(data));
  console.info("onPushListener extraData=" + JSON.stringify(extraData));
}
function onRequestListener(source:Want, name:string, data:pluginComponentManager.KVObject) {
  console.info("onRequestListener");
  console.info("onRequestListener source=" + JSON.stringify(source));
  console.info("onRequestListener name=" + name);
  console.info("onRequestListener data=" + JSON.stringify(data));
  let RtnData:Record<string,string|pluginComponentManager.KVObject> = { 'template': "ets/pages/plugin.js", 'data': data };
  return RtnData;
}
pluginComponentManager.on("push", onPushListener);
pluginComponentManager.on("request", onRequestListener);
```

#### external.json文件说明

external.json文件由开发者创建。external.json中以键值对形式存放组件名称以及对应模板路径。以组件名称name作为关键字，对应模板路径作为值。

**示例**

```ets
{
  "PluginProviderExample": "ets/pages/PluginProviderExample.js",
  "plugintemplate2": "ets/pages/plugintemplate2.js"
}
```