# @ohos.base (公共回调信息)

本模块定义了HarmonyOS ArkTS接口的公共回调类型，包括接口调用时出现的公共回调和公共错误信息。

-

本模块首批接口从 API version 6 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

从API version 12开始，本模块接口支持在ArkTS卡片中使用。

#### 导入模块

ArkTS示例：

```ets
import { AsyncCallback, BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
```

JS示例：

```ets
import base from '@ohos.base';
```

#### Callback

Callback<T> {

(data: T): void;

}

通用回调函数。

开发者在使用时，可自定义data的类型，回调将返回对应类型的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 接口调用时的公共回调信息。 |

#### ErrorCallback

ErrorCallback<T extends Error = BusinessError> {

(err: T): void;

}

通用回调函数，携带错误参数。

回调返回的信息为[BusinessError](#ZH-CN_TOPIC_0000002553201565__businesserror)类型的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| err | T | 是 | 接口调用失败的公共错误信息。 |

#### AsyncCallback

AsyncCallback<T, E = void> {

(err: BusinessError<E>, data: T): void;

}

通用回调函数，携带错误参数和异步返回值。

错误参数为[BusinessError](#ZH-CN_TOPIC_0000002553201565__businesserror)类型的信息。

异步返回值的类型由开发者自定义，回调将返回对应类型的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| err | BusinessError | 是 | 接口调用失败的公共错误信息。 |
| data | T | 是 | 接口调用时的公共回调信息。 |

#### BusinessError

BusinessError<T = void> extends Error { code: number; data?: T; }

错误参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 接口调用失败返回的错误码信息。 |
| data | T | 否 | 接口调用时的公共回调信息。如果不填，则回调不返回相关信息。 |