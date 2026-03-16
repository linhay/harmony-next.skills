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

名称类型只读可选说明sourcestring否否组件模板名。abilitystring否否提供方Ability的bundleName。

#### pluginComponentManager

插件组件管理器。

#### KVObject

type KVObject = { [key: string]: number | string | boolean | [] | KVObject }

以键值对形式存储信息，符合json格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型必填说明[key: string]number | string | boolean | [] | [KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否

键值对形式存储。

number：键值，表示值类型为数字。

 string：键值，表示值类型为字符串，可取空字符串。

 boolean：键值，表示值类型为布尔值。

 []：键值，可取值为[]。

[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)：键值，表示值类型为KVObject。

#### PushParameters

使用PluginManager.Push方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明want[Want](@ohos.application.Want (Want).md)否否组件使用方Ability信息。namestring否否组件名称。data[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否否组件数据。extraData[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否否附加数据。jsonPathstring否是存放模板路径的[external.json](#ZH-CN_TOPIC_0000002497444812__externaljson文件说明)文件的路径。

#### RequestParameters

使用PluginManager.Request方法时需要传递的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明want[Want](@ohos.application.Want (Want).md)否否组件提供方Ability信息。namestring否否请求组件名称。data[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否否组件数据。jsonPathstring否是存放模板路径的[external.json](#ZH-CN_TOPIC_0000002497444812__externaljson文件说明)文件的路径。当jsonPath字段不为空时不触发Request通信。

#### RequestCallbackParameters

PluginManager.Request方法接收到的回调结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明componentTemplate[PluginComponentTemplate](#ZH-CN_TOPIC_0000002497444812__plugincomponenttemplate)否否组件模板。data[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否否组件数据。extraData[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否否附加数据。

#### RequestEventResult

注册Request监听方法后，接收到请求事件时回应请求的数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明templatestring否是组件模板。data[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否是组件数据。extraData[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)否是附加数据。

#### OnPushEventCallback

type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,

 extraData: KVObject) => void

对应Push事件的监听回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明source[Want](@ohos.application.Want (Want).md)是Push请求发送方相关信息。template[PluginComponentTemplate](#ZH-CN_TOPIC_0000002497444812__plugincomponenttemplate)是请求组件模板名称。data[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)是数据。extraData[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)是附加数据。

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

参数名类型必填说明source[Want](@ohos.application.Want (Want).md)是request请求发送方相关信息。namestring是模板名称。data[KVObject](#ZH-CN_TOPIC_0000002497444812__kvobject)是数据。

**返回值：**

类型说明[RequestEventResult](#ZH-CN_TOPIC_0000002497444812__requesteventresult)注册Request监听方法后，接收到请求事件时回应请求的数据类型。

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

参数名类型必填说明param[PushParameters](#ZH-CN_TOPIC_0000002497444812__pushparameters)是组件使用方的详细信息。callbackAsyncCallback<void>是此次接口调用的异步回调。

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

参数名类型必填说明param[RequestParameters](#ZH-CN_TOPIC_0000002497444812__requestparameters)是组件模板的详细请求信息。callbackAsyncCallback<[RequestCallbackParameters](#ZH-CN_TOPIC_0000002497444812__requestcallbackparameters)>是此次请求的异步回调，通过回调接口的参数返回接收请求的数据。

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

参数名类型必填说明eventTypestring是

监听的事件类型， 可选值为："push" 、"request"。

"push”：指组件提供方向使用方主动推送数据。

"request”：指组件使用方向提供方主动请求数据。

callback[OnPushEventCallback](#ZH-CN_TOPIC_0000002497444812__onpusheventcallback) | [OnRequestEventCallback](#ZH-CN_TOPIC_0000002497444812__onrequesteventcallback)是对应监听回调，push事件对应回调类型为[OnPushEventCallback](#ZH-CN_TOPIC_0000002497444812__onpusheventcallback)，request事件对应回调类型为[OnRequestEventCallback](#ZH-CN_TOPIC_0000002497444812__onrequesteventcallback) 。

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