[]()[]()

# SuperPrivacyMode（超级隐私模式）

本模块提供超级隐私模式相关接口，应用可根据当前的超级隐私模式的状态进行相应业务处理。

**起始版本：**6.0.2(22)

[]()[]()

#### 导入模块

```ets
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
```

[]()[]()

#### SuperPrivacyMode

表示超级隐私模式状态的枚举。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：**6.0.2(22)

名称

值

说明

OFF

0

表示当前超级隐私模式状态为关。

ON_WHEN_FOLDED

1

表示当前超级隐私模式状态为仅折叠保护（展开时超级隐私不生效，折叠时生效）。

ALWAYS_ON

2

表示当前超级隐私模式状态为始终保护。

[]()[]()

#### getSuperPrivacyMode

getSuperPrivacyMode(): Promise<SuperPrivacyMode>

获取当前超级隐私模式状态。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：**6.0.2(22)

**返回值：**

类型

说明

Promise<[SuperPrivacyMode](#section11705111513)>

Promise对象，返回当前的超级隐私模式状态。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SuperPrivacyMode（超级隐私模式） (devicesecurity-arktsapi-errcode-superprivacy).md)**。**

错误码ID

错误信息

1006200002

Internal error.

1006200005

This device is not support SuperPrivacy.

**示例：**

```ets
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

let mode: superPrivacyMode.SuperPrivacyMode = superPrivacyMode.SuperPrivacyMode.OFF;
try {
  mode = await superPrivacyMode.getSuperPrivacyMode();
  hilog.info(DOMAIN, TAG, `Super privacy mode = ${mode}`);
} catch (err) {
  hilog.error(DOMAIN, TAG, `call getSuperPrivacyMode interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
}
```

[]()[]()

#### on('superPrivacyModeChange')

on(type: 'superPrivacyModeChange', callback: Callback<SuperPrivacyMode>): void

订阅超级隐私模式状态变化事件。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：**6.0.2(22)

**参数：**

参数名

类型

必填

说明

type

string

是

输入固定字符串'superPrivacyModeChange'，表示需要订阅'superPrivacyModeChange'。

callback

Callback<[SuperPrivacyMode](#section11705111513)>

是

回调函数，返回调用结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SuperPrivacyMode（超级隐私模式） (devicesecurity-arktsapi-errcode-superprivacy).md)**。**

错误码ID

错误信息

1006200001

General error.

1006200002

Internal error.

1006200005

This device is not support SuperPrivacy.

**示例：**

```ets
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
  hilog.info(DOMAIN, TAG, `super privcy mode changed, mode = ${superPrivacyMode}`);
}

hilog.info(DOMAIN, TAG, 'start register super privacy mode changed listener');
try {
  superPrivacyMode.on('superPrivacyModeChange', superPrivacyChangedCallback);
  hilog.info(DOMAIN, TAG, 'register super privacy mode change listener success');
} catch (err) {
  hilog.error(DOMAIN, TAG, `register super privacy changed listener failed, ${JSON.stringify(err)}`);
}
```

[]()[]()

#### off('superPrivacyModeChange')

off(type: 'superPrivacyModeChange', callback?: Callback<SuperPrivacyMode>): void

取消订阅超级隐私模式状态变化事件。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：**6.0.2(22)

**参数：**

参数名

类型

必填

说明

type

string

是

输入固定字符串'superPrivacyModeChange'，表示需要订阅的事件为'superPrivacyModeChange'。

callback

Callback<[SuperPrivacyMode](#section11705111513)>

否

回调函数，返回调用结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/SuperPrivacyMode（超级隐私模式） (devicesecurity-arktsapi-errcode-superprivacy).md)**。**

错误码ID

错误信息

1006200001

General error.

1006200002

Internal error.

1006200005

This device is not support SuperPrivacy.

**示例：**

```ets
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
  hilog.info(DOMAIN, TAG, `super privcy mode changed, mode = ${superPrivacyMode}`);
}

hilog.info(DOMAIN, TAG, 'start unregister super privacy mode changed listener');
try {
  superPrivacyMode.off('superPrivacyModeChange', superPrivacyChangedCallback);
} catch (err) {
  hilog.error(DOMAIN, TAG, `unregister super privacy changed listener failed, ${JSON.stringify(err)}`);
}
```