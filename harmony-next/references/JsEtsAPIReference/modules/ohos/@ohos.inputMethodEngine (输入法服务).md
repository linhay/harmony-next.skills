# @ohos.inputMethodEngine (输入法服务)

本模块面向输入法应用（包括系统输入法应用、三方输入法应用），为输入法应用提供能力，包括：创建软键盘窗口、插入/删除字符、选中文本、监听物理键盘按键事件等。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { inputMethodEngine } from '@kit.IMEKit';
```

#### 常量

功能键常量值、编辑框常量值及光标常量值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| ENTER_KEY_TYPE_UNSPECIFIED | number | 0 | 无功能键。 |
| ENTER_KEY_TYPE_GO | number | 2 | “前往”功能键。 |
| ENTER_KEY_TYPE_SEARCH | number | 3 | “搜索”功能键。 |
| ENTER_KEY_TYPE_SEND | number | 4 | “发送”功能键。 |
| ENTER_KEY_TYPE_NEXT | number | 5 | “下一个”功能键。 |
| ENTER_KEY_TYPE_DONE | number | 6 | “回车”功能键。 |
| ENTER_KEY_TYPE_PREVIOUS | number | 7 | “前一个”功能键。 |
| ENTER_KEY_TYPE_NEWLINE12+ | number | 8 | “换行”功能键。 |
| PATTERN_NULL | number | -1 | 无特殊性编辑框。 |
| PATTERN_TEXT | number | 0 | 文本编辑框。 |
| PATTERN_NUMBER | number | 2 | 数字编辑框。 |
| PATTERN_PHONE | number | 3 | 电话号码编辑框。 |
| PATTERN_DATETIME | number | 4 | 日期编辑框。 |
| PATTERN_EMAIL | number | 5 | 邮件编辑框。 |
| PATTERN_URI | number | 6 | 超链接编辑框。 |
| PATTERN_PASSWORD | number | 7 | 密码编辑框。 |
| PATTERN_PASSWORD_NUMBER11+ | number | 8 | 数字密码编辑框。 |
| PATTERN_PASSWORD_SCREEN_LOCK11+ | number | 9 | 锁屏密码编辑框。 |
| PATTERN_USER_NAME20+ | number | 10 | 用户名编辑框。 |
| PATTERN_NEW_PASSWORD20+ | number | 11 | 新密码编辑框。 |
| PATTERN_NUMBER_DECIMAL20+ | number | 12 | 带小数点的数字编辑框。 |
| PATTERN_ONE_TIME_CODE20+ | number | 13 | 验证码编辑框。 |
| OPTION_ASCII | number | 20 | 允许输入ASCII值。 |
| OPTION_NONE | number | 0 | 不指定编辑框输入属性。 |
| OPTION_AUTO_CAP_CHARACTERS | number | 2 | 允许输入字符。 |
| OPTION_AUTO_CAP_SENTENCES | number | 8 | 允许输入句子。 |
| OPTION_AUTO_WORDS | number | 4 | 允许输入单词。 |
| OPTION_MULTI_LINE | number | 1 | 允许输入多行。 |
| OPTION_NO_FULLSCREEN | number | 10 | 半屏样式。 |
| FLAG_SELECTING | number | 2 | 编辑框处于选择状态。 |
| FLAG_SINGLE_LINE | number | 1 | 编辑框为单行。 |
| DISPLAY_MODE_PART | number | 0 | 编辑框显示为半屏。 |
| DISPLAY_MODE_FULL | number | 1 | 编辑框显示为全屏。 |
| CURSOR_UP9+ | number | 1 | 光标上移。 |
| CURSOR_DOWN9+ | number | 2 | 光标下移。 |
| CURSOR_LEFT9+ | number | 3 | 光标左移。 |
| CURSOR_RIGHT9+ | number | 4 | 光标右移。 |
| WINDOW_TYPE_INPUT_METHOD_FLOAT9+ | number | 2105 | 输入法应用窗口风格标识。 |

#### inputMethodEngine.getInputMethodAbility9+

getInputMethodAbility(): InputMethodAbility

获取输入法应用客户端实例[InputMethodAbility](#ZH-CN_TOPIC_0000002553201227__inputmethodability)，仅支持输入法应用调用。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件、创建/销毁输入法面板等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| InputMethodAbility | 输入法应用客户端。 |

**示例：**

```ets
let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```

#### inputMethodEngine.getKeyboardDelegate9+

getKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](#ZH-CN_TOPIC_0000002553201227__keyboarddelegate)。

输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KeyboardDelegate | 客户端编辑事件监听代理。 |

**示例：**

```ets
let KeyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();
```

#### inputMethodEngine.getInputMethodEngine(deprecated)

getInputMethodEngine(): InputMethodEngine

获取输入法应用客户端实例[InputMethodEngine](#ZH-CN_TOPIC_0000002553201227__inputmethodenginedeprecated)。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件等。


从API version 8开始支持，API version 9开始废弃，建议使用[getInputMethodAbility](#ZH-CN_TOPIC_0000002553201227__inputmethodenginegetinputmethodability9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| InputMethodEngine | 输入法应用客户端。 |

**示例：**

```ets
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

#### inputMethodEngine.createKeyboardDelegate(deprecated)

createKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](#ZH-CN_TOPIC_0000002553201227__keyboarddelegate)。输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。


从API version 8开始支持，API version 9开始废弃，建议使用[getKeyboardDelegate](#ZH-CN_TOPIC_0000002553201227__inputmethodenginegetkeyboarddelegate9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KeyboardDelegate | 客户端编辑事件监听代理。 |

**示例：**

```ets
let keyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.createKeyboardDelegate();
```

#### CommandDataType12+

type CommandDataType = number | string | boolean;

表示私有数据类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 类型 | 说明 |
| --- | --- |
| string | 表示值类型为字符串。 |
| number | 表示值类型为数字。 |
| boolean | 表示值类型为布尔值。 |

#### SizeChangeCallback15+

type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void

当输入法面板大小变化时触发的回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | window.Size | 是 | 当前面板大小。 |
| keyboardArea | KeyboardArea | 否 | 当前面板中可作为键盘区域的大小。 |

**InputMethodEngine(deprecated)**


从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility](#ZH-CN_TOPIC_0000002553201227__inputmethodability)替代。

下列API均需使用[getInputMethodEngine](#ZH-CN_TOPIC_0000002553201227__inputmethodenginegetinputmethodenginedeprecated)获取到InputMethodEngine实例后，通过实例调用。

**on('inputStart')(deprecated)**

on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。


从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#on](#ZH-CN_TOPIC_0000002553201227__oninputstart9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) => void | 是 | 回调函数，返回订阅输入法的KeyboardController和TextInputClient实例。 |

**示例：**

```ets
inputMethodEngine.getInputMethodEngine()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let textInputClient: inputMethodEngine.TextInputClient = textClient;
    });
```

**off('inputStart')(deprecated)**

off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

取消订阅输入法绑定成功事件。


从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#off](#ZH-CN_TOPIC_0000002553201227__offinputstart9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getInputMethodEngine()
  .off('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      console.info('delete inputStart notification.');
    });
```

**on('keyboardShow'|'keyboardHide')(deprecated)**

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。


从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#on](#ZH-CN_TOPIC_0000002553201227__onkeyboardshowkeyboardhide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。 -'keyboardShow'表示显示输入法软键盘。 -'keyboardHide'表示隐藏输入法软键盘。 |
callback() => void是回调函数。

**示例：**

```ets
inputMethodEngine.getInputMethodEngine().on('keyboardShow', () => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodEngine.getInputMethodEngine().on('keyboardHide', () => {
  console.info('inputMethodEngine keyboardHide.');
});
```

**off('keyboardShow'|'keyboardHide')(deprecated)**

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。


从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#off](#ZH-CN_TOPIC_0000002553201227__offkeyboardshowkeyboardhide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要取消监听的输入法软键盘事件类型。 -'keyboardShow'表示显示输入法软键盘。 -'keyboardHide'表示隐藏输入法软键盘。 |
callback() => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**示例：**

```ets
inputMethodEngine.getInputMethodEngine().off('keyboardShow');
inputMethodEngine.getInputMethodEngine().off('keyboardHide');
```

#### InputMethodAbility

下列API均需使用[getInputMethodAbility](#ZH-CN_TOPIC_0000002553201227__inputmethodenginegetinputmethodability9)获取到InputMethodAbility实例后，通过实例调用。

#### on('inputStart')9+

on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, inputClient: InputClient) => void | 是 | 回调函数，返回输入法操作相关实例。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
    });
```

#### off('inputStart')9+

off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void

取消订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: KeyboardController, inputClient: InputClient) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('inputStart');
```

#### on('inputStop')9+

on(type: 'inputStop', callback: () => void): void

订阅停止输入法应用事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStop'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().on('inputStop', () => {
  console.info('inputMethodAbility inputStop');
});
```

#### off('inputStop')9+

off(type: 'inputStop', callback: () => void): void

取消订阅停止输入法应用事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'inputStop'。 |
| callback | () => void | 是 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('inputStop', () => {
  console.info('inputMethodAbility delete inputStop notification.');
});
```

#### on('setCallingWindow')9+

on(type: 'setCallingWindow', callback: (wid: number) => void): void

订阅设置调用窗口事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid: number) => void | 是 | 回调函数，返回调用方窗口的Id。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().on('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility setCallingWindow');
});
```

#### off('setCallingWindow')9+

off(type: 'setCallingWindow', callback: (wid:number) => void): void

取消订阅设置调用窗口事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid:number) => void | 是 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility delete setCallingWindow notification.');
});
```

#### on('keyboardShow'|'keyboardHide')9+

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。 - 'keyboardShow'表示显示输入法软键盘。 - 'keyboardHide'表示隐藏输入法软键盘。 |
callback() => void是回调函数。

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
  console.info('InputMethodAbility keyboardShow.');
});
inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
  console.info('InputMethodAbility keyboardHide.');
});
```

#### off('keyboardShow'|'keyboardHide')9+

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。 - 'keyboardShow'表示显示键盘。 - 'keyboardHide'表示隐藏键盘。 |
callback() => void否回调函数。

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
  console.info('InputMethodAbility delete keyboardShow notification.');
});
inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
  console.info('InputMethodAbility delete keyboardHide notification.');
});
```

#### on('setSubtype')9+

on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void

订阅设置输入法子类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: InputMethodSubtype) => void | 是 | 回调函数，返回设置的输入法子类型。 |

**示例：**

```ets
import { InputMethodSubtype } from '@kit.IMEKit';

inputMethodEngine.getInputMethodAbility().on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
  console.info('InputMethodAbility setSubtype.');
});
```

#### off('setSubtype')9+

off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void

取消订阅设置输入法子类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: InputMethodSubtype) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('setSubtype', () => {
  console.info('InputMethodAbility delete setSubtype notification.');
});
```

#### on('securityModeChange')11+

on(type: 'securityModeChange', callback: Callback< SecurityMode>): void

订阅输入法安全模式改变类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | Callback<SecurityMode> | 是 | 回调函数，返回当前输入法应用的安全模式。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility()
  .on('securityModeChange', (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  });
```

#### off('securityModeChange')11+

off(type: 'securityModeChange', callback?: Callback< SecurityMode>): void

取消订阅输入法安全模式改变类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | Callback<SecurityMode> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
let securityChangeCallback: (securityMode: inputMethodEngine.SecurityMode) => void =
  (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  };
let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility.on('securityModeChange', securityChangeCallback);
inputMethodAbility.off('securityModeChange', securityChangeCallback);
```

#### on('privateCommand')12+

on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void;

订阅输入法私有数据事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'privateCommand'。 |
| callback | Callback<Record<string, CommandDataType>> | 是 | 回调函数，返回向输入法应用发送的私有数据。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码]([输入法框架错误码](../../errors/输入法框架错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ets
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i :number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);
```

#### off('privateCommand')12+

off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void

取消订阅输入法私有数据事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'privateCommand'。 |
| callback | Callback<Record<string, CommandDataType>> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ets
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i: number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }

inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);
```

#### on('callingDisplayDidChange')18+

on(type: 'callingDisplayDidChange', callback: Callback<number>): void

订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | Callback<number> | 是 | 回调函数，返回编辑框设置对应窗口屏幕ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |

**示例：**

```ets
let callingDisplayDidChangeCallback: (num: number) => void = (num: number) => {
  console.info(`display id: ${num}`);
}
inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', callingDisplayDidChangeCallback);
```

#### off('callingDisplayDidChange')18+

off(type: 'callingDisplayDidChange', callback?: Callback<number>): void

取消订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | Callback<number> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('callingDisplayDidChange', (num: number) => {
  console.info('InputMethodAbility delete calling display  notification.');
});
```

#### on('discardTypingText')20+

on(type: 'discardTypingText', callback: Callback<void>): void

订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'discardTypingText'。 - 'discardTypingText'：表示订阅编辑框应用发送“清空候选词”事件到输入法。 |
callbackCallback<void>是回调函数。当命令发送成功，err为undefined，否则为错误对象。

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

#### off('discardTypingText')20+

off(type: 'discardTypingText', callback?: Callback<void>): void

取消订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'discardTypingText'。 - 'discardTypingText'：表示取消订阅编辑框应用发送“清空候选词”事件到输入法。 |
callbackCallback<void>否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

#### getSecurityMode11+

getSecurityMode(): SecurityMode

获取输入法应用的当前安全模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SecurityMode | 安全模式。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 12800004 | not an input method application. |

**示例：**

```ets
let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(`getSecurityMode, securityMode is : ${security}`);
```

#### createPanel10+

createPanel(ctx: [BaseContext](../../topics/misc/BaseContext.md), info: PanelInfo, callback: AsyncCallback<Panel>): void

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](@ohos.InputMethodExtensionAbility (InputMethodExtensionAbility).md#ZH-CN_TOPIC_0000002522241256__inputmethodextensionability)类中调用。使用callback异步回调。


单个输入法应用仅允许创建一个[软键盘类型](#ZH-CN_TOPIC_0000002553201227__paneltype10)和一个[状态栏类型](#ZH-CN_TOPIC_0000002553201227__paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa#设置应用子窗口)、[bindContextMenu](菜单控制.md#ZH-CN_TOPIC_0000002522080798__bindcontextmenu8)、[CustomDialog](自定义弹窗 (CustomDialog).md)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](弹出框 (Dialog).md)、[bindMenu](菜单控制.md#ZH-CN_TOPIC_0000002522080798__bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../topics/misc/BaseContext.md) | 是 | 当前输入法应用上下文信息。 |
| info | PanelInfo | 是 | 输入法面板信息。 |
| callback | AsyncCallback<Panel> | 是 | 回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

if (!this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(`Failed to createPanel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      console.info('Succeed in creating panel.');
    })
}
```

#### createPanel10+

createPanel(ctx: [BaseContext](../../topics/misc/BaseContext.md), info: PanelInfo): Promise<Panel>

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](@ohos.InputMethodExtensionAbility (InputMethodExtensionAbility).md#ZH-CN_TOPIC_0000002522241256__inputmethodextensionability)类中调用。使用promise异步回调。


单个输入法应用仅允许创建一个[软键盘类型](#ZH-CN_TOPIC_0000002553201227__paneltype10)和一个[状态栏类型](#ZH-CN_TOPIC_0000002553201227__paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa#设置应用子窗口)、[bindContextMenu](菜单控制.md#ZH-CN_TOPIC_0000002522080798__bindcontextmenu8)、[CustomDialog](自定义弹窗 (CustomDialog).md)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](弹出框 (Dialog).md)、[bindMenu](菜单控制.md#ZH-CN_TOPIC_0000002522080798__bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ctx | [BaseContext](../../topics/misc/BaseContext.md) | 是 | 当前输入法应用上下文信息。 |
| info | PanelInfo | 是 | 输入法面板信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Panel> | 回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

if (this.context) {
  inputMethodEngine.getInputMethodAbility().createPanel(this.context, panelInfo)
    .then((panel: inputMethodEngine.Panel) => {
      console.info('Succeed in creating panel.');
    }).catch((err: BusinessError) => {
    console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
  })
}
```

#### destroyPanel10+

destroyPanel(panel: Panel, callback: AsyncCallback<void>): void

销毁输入法面板。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| panel | Panel | 是 | 要销毁的面板对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法面板销毁成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel, (err: BusinessError) => {
    if (err !== undefined) {
      console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Succeed in destroying panel.');
  })
}
```

#### destroyPanel10+

destroyPanel(panel: Panel): Promise<void>

销毁输入法面板。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| panel | Panel | 是 | 要销毁的面板对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel).then(() => {
    console.info('Succeed in destroying panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
  });
}
```

#### KeyboardDelegate

下列API均需使用[getKeyboardDelegate](#ZH-CN_TOPIC_0000002553201227__inputmethodenginegetkeyboarddelegate9)获取到KeyboardDelegate实例后，通过实例调用。

#### on('keyDown'|'keyUp')

on(type: 'keyDown'|'keyUp', callback: (event: KeyEvent) => boolean): void

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。 - 'keyDown'表示键盘按下。 - 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) => boolean | 是 | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
```

#### off('keyDown'|'keyUp')

off(type: 'keyDown'|'keyUp', callback?: (event: KeyEvent) => boolean): void

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型。 - 'keyDown'表示键盘按下。 - 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) => boolean | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().off('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyUp notification.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyDown notification.');
  return true;
});
```

#### on('keyEvent')10+

on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void

订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: InputKeyEvent) => boolean | 是 | 回调函数，入参为按键事件信息，返回值类型为布尔类型。 - 入参按键事件信息的数据类型为InputKeyEvent。 - 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例：**

```ets
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().on('keyEvent', (keyEvent: KeyEvent) => {
  console.info(`inputMethodEngine keyEvent.action:${ keyEvent.action}`);
  console.info(`inputMethodEngine keyEvent.key.code: ${keyEvent.key.code}`);
  console.info(`inputMethodEngine keyEvent.ctrlKey: ${keyEvent.ctrlKey}`);
  console.info(`inputMethodEngine keyEvent.unicodeChar: ${keyEvent.unicodeChar}`);
  return true;
});
```

#### off('keyEvent')10+

off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void

取消订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: InputKeyEvent) => boolean | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().off('keyEvent', (keyEvent: KeyEvent) => {
  console.info('This is a callback function which will be deregistered.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyEvent');
```

#### on('cursorContextChange')

on(type: 'cursorContextChange', callback: (x: number, y:number, height:number) => void): void

订阅光标变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y: number, height: number) => void | 是 | 回调函数，返回光标信息。 - x为光标上端的x坐标值，y为光标上端的y坐标值，height为光标的高度值。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().on('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('inputMethodEngine cursorContextChange x:' + x);
  console.info('inputMethodEngine cursorContextChange y:' + y);
  console.info('inputMethodEngine cursorContextChange height:' + height);
});
```

#### off('cursorContextChange')

off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void

取消订阅光标变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y:number, height:number) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().off('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('delete cursorContextChange notification.');
});
```

#### on('selectionChange')

on(type: 'selectionChange', callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

订阅文本选择范围变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | 是 | 回调函数，返回文本选择信息。 - oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。 - newBegin为变化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate()
  .on('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('selectionChange oldBegin:' + oldBegin);
    console.info('selectionChange oldEnd:' + oldEnd);
    console.info('selectionChange newBegin:' + newBegin);
    console.info('selectionChange newEnd:' + newEnd);
  });
```

#### off('selectionChange')

off(type: 'selectionChange', callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

取消订阅文本选择范围变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate()
  .off('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('delete selectionChange notification.');
  });
```

#### on('textChange')

on(type: 'textChange', callback: (text: string) => void): void

订阅文本内容变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) => void | 是 | 回调函数，返回订阅的文本内容。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().on('textChange', (text: string) => {
  console.info('inputMethodEngine textChange. text:' + text);
});
```

#### off('textChange')

off(type: 'textChange', callback?: (text: string) => void): void

取消订阅文本内容变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().off('textChange', (text: string) => {
  console.info('delete textChange notification. text:' + text);
});
```

#### on('editorAttributeChanged')10+

on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void

订阅编辑框属性变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: EditorAttribute) => void | 是 | 回调函数，返回变化的编辑框属性。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate()
  .on('editorAttributeChanged', (attr: inputMethodEngine.EditorAttribute) => {
    console.info(`Succeeded in receiving attribute of editor, inputPattern = ${attr.inputPattern}, enterKeyType = ${attr.enterKeyType}`);
  });
```

#### off('editorAttributeChanged')10+

off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void

取消订阅编辑框属性变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 文本变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: EditorAttribute) => void | 否 | 所要取消订阅的回调处理函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');
```

#### Panel10+

下列API均需使用[createPanel](#ZH-CN_TOPIC_0000002553201227__createpanel10)获取到Panel实例后，通过实例调用。

#### setUiContent10+

setUiContent(path: string, callback: AsyncCallback<void>): void

为当前的输入法面板加载具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 具体页面的路径。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

#### setUiContent10+

setUiContent(path: string): Promise<void>

为当前的输入法面板加载具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 具体页面的路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2').then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

#### setUiContent10+

setUiContent(path: string, storage: [LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9), callback: AsyncCallback<void>): void

为当前的输入法面板加载与[LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)相关联的具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)相关联的具体页面的路径。 |
| storage | [LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9) | 是 | 存储单元，为应用程序范围内的可变和不可变状态属性提供存储。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

#### setUiContent10+

setUiContent(path: string, storage: [LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)): Promise<void>

为当前面板加载与[LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)相关联的具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 设置加载页面的路径。 |
| storage | [LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9) | 是 | 存储单元，为应用程序范围内的可变状态属性和非可变状态属性提供存储。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage).then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

#### resize10+

resize(width: number, height: number, callback: AsyncCallback<void>): void

改变当前输入法面板的大小，使用callback异步回调。

面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。

手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。 |
| height | number | 是 | 目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板大小改变成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in changing the panel size.');
});
```

#### resize10+

resize(width: number, height: number): Promise<void>

改变当前输入法面板的大小，使用Promise异步回调。

面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。

手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。 |
| height | number | 是 | 目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000).then(() => {
  console.info('Succeeded in changing the panel size.');
}).catch((err: BusinessError) => {
  console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### moveTo10+

moveTo(x: number, y: number, callback: AsyncCallback<void>): void

移动面板位置，使用callback异步回调。[面板状态](#ZH-CN_TOPIC_0000002553201227__panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。 |
| y | number | 是 | 纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板位置移动成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving the panel.');
});
```

#### moveTo10+

moveTo(x: number, y: number): Promise<void>

移动面板位置，使用promise异步回调。[面板状态](#ZH-CN_TOPIC_0000002553201227__panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。 |
| y | number | 是 | 纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300).then(() => {
  console.info('Succeeded in moving the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### startMoving15+

startMoving(): void

发送移动命令给窗口，不产生实际移动效果（仅在鼠标点击作用才可以移动）。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```ets
panel.startMoving();
```

#### getDisplayId15+

getDisplayId(): Promise<number>

获取当前窗口的所在id，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回窗口的displayId。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.getDisplayId().then((result: number) => {
  console.info('get displayId:' + result);
}).catch((err: BusinessError) => {
  console.error(`Failed to get displayId. Code is ${err.code}, message is ${err.message}`);
});
```

#### show10+

show(callback: AsyncCallback<void>): void

显示当前输入法面板，使用callback异步回调。输入法应用与编辑框绑定成功后可正常调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板显示成功，err为undefined，否则err为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.show((err: BusinessError) => {
  if (err) {
    console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the panel.');
});
```

#### show10+

show(): Promise<void>

显示当前输入法面板，使用promise异步回调。输入法应用与编辑框绑定成功后可正常调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### hide10+

hide(callback: AsyncCallback<void>): void

隐藏当前输入法面板，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板隐藏成功，err为undefined，否则err为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding the panel.');
});
```

#### hide10+

hide(): Promise<void>

隐藏当前输入法面板，使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### adjustPanelRect12+

adjustPanelRect(flag: PanelFlag, rect: PanelRect): void

预设置输入法应用横竖屏大小。接口调用完毕表示adjust请求已提交到输入法框架，不表示执行完毕。


仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。

此接口为同步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。

手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | PanelFlag | 是 | 目标面板状态类型。类型为FLG_FIXED或FLG_FLOATING。 |
| rect | PanelRect | 是 | 目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度。固定态：高度不能超过屏幕高度的70%，宽度不能超过屏幕宽度；悬浮态：高度不能超过屏幕高度，宽度不能超过屏幕宽度。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |

**示例：**

```ets
import { window } from '@kit.ArkUI';

let landscapeRect: window.Rect = {
  left: 100,
  top: 100,
  width: 400,
  height: 400
};

let portraitRect: window.Rect = {
  left: 200,
  top: 200,
  width: 300,
  height: 300
};

let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
let panelRect: inputMethodEngine.PanelRect = {
  landscapeRect: landscapeRect,
  portraitRect: portraitRect
};
panel.adjustPanelRect(panelFlag, panelRect);
```

#### adjustPanelRect15+

adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。


仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。此接口兼容[adjustPanelRect](#ZH-CN_TOPIC_0000002553201227__adjustpanelrect12)的调用方法，若入参rect仅填写属性landscapeRect和portraitRect，则默认调用[adjustPanelRect](#ZH-CN_TOPIC_0000002553201227__adjustpanelrect12)。

此接口为同步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。

手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | PanelFlag | 是 | 目标面板状态类型。类型为FLG_FIXED或FLG_FLOATING。 |
| rect | EnhancedPanelRect | 是 | 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```ets
import { window } from '@kit.ArkUI';

let landscapeRect1: window.Rect = {
  left: 300,
  top: 650,
  width: 2000,
  height: 500
};
let landscapeInputRegion: Array<window.Rect> = [landscapeRect1];

let portraitRect1: window.Rect = {
  left: 0,
  top: 1800,
  width: 1200,
  height: 800
}
let portraitInputRegion: Array<window.Rect> = [portraitRect1];

let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
let panelRect: inputMethodEngine.EnhancedPanelRect = {
  landscapeAvoidY: 650,
  landscapeInputRegion: landscapeInputRegion,
  portraitAvoidY: 1800,
  portraitInputRegion: portraitInputRegion,
  fullScreenMode: true
};
panel.adjustPanelRect(panelFlag, panelRect);
```

#### updateRegion15+

updateRegion(inputRegion: Array<window.Rect>): void

更新当前状态下输入法面板内的热区。

仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。

此接口为同步接口，接口返回仅代表系统侧收到更新热区的请求，不代表已完成热区更新。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputRegion | Array<window.Rect> | 是 | 面板内接收输入事件的区域。 - 数组大小限制为[1, 4]。 - 传入的热区位置是相对于输入法面板窗口左顶点的位置。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let inputRegion: Array<window.Rect> = [{
  left: 300,
  top: 650,
  width: 2000,
  height: 500
}];
panel.updateRegion(inputRegion);
```

#### on('show')10+

on(type: 'show', callback: () => void): void

监听当前面板显示状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的状态类型，固定取值为'show'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ets
panel.on('show', () => {
  console.info('Panel is showing.');
});
```

#### on('hide')10+

on(type: 'hide', callback: () => void): void

监听当前面板隐藏状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的状态类型，固定取值为'hide'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ets
panel.on('hide', () => {
  console.info('Panel is hiding.');
});
```

#### on('sizeChange')12+

on(type: 'sizeChange', callback: SizeChangeCallback): void

监听当前面板大小变化，使用callback异步回调。

仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。

- 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__size7)类型的必选参数。

- 从API version 15起，调用[adjustPanelRect](#ZH-CN_TOPIC_0000002553201227__adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](#ZH-CN_TOPIC_0000002553201227__keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的大小是否产生变化，固定值为'sizeChange'。 |
| callback | SizeChangeCallback | 是 | 回调函数。返回当前软键盘面板的大小，包含宽度和高度值。 |

**示例：**

```ets
import { window } from '@kit.ArkUI';

panel.on('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});

panel.on('sizeChange', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
    `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
});
```

#### off('show')10+

off(type: 'show', callback?: () => void): void

取消监听当前面板的显示状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听当前面板的状态类型，固定取值为'show'。 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
panel.off('show');
```

#### off('hide')10+

off(type: 'hide', callback?: () => void): void

取消监听当前面板的隐藏状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要取消监听的当前面板状态类型，固定取值为'hide'。 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
panel.off('hide');
```

#### off('sizeChange')12+

off(type: 'sizeChange', callback?: SizeChangeCallback): void

取消监听当前面板大小变化，使用callback异步回调。

仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。

- 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__size7)类型的必选参数。

- 从API version 15起，调用[adjustPanelRect](#ZH-CN_TOPIC_0000002553201227__adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](#ZH-CN_TOPIC_0000002553201227__keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听当前面板的大小是否产生变化，固定取值为'sizeChange'。 |
| callback | SizeChangeCallback | 否 | 回调函数。返回当前软键盘面板的大小，包含宽度和高度值。 |

**示例：**

```ets
import { window } from '@kit.ArkUI';

panel.off('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

#### changeFlag10+

changeFlag(flag: PanelFlag): void

将输入法应用的面板状态改变为其他[PanelFlag](#ZH-CN_TOPIC_0000002553201227__panelflag10)形态，仅对[SOFT_KEYBOARD](#ZH-CN_TOPIC_0000002553201227__paneltype10)生效。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | PanelFlag | 是 | 目标面板状态类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
panel.changeFlag(panelFlag);
```

#### setPrivacyMode11+

setPrivacyMode(isPrivacyMode: boolean): void

将输入法应用的面板设置为隐私模式，隐私模式不可被录屏、截屏。

**需要权限：** ohos.permission.PRIVACY_WINDOW

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 是否设置隐私模式。 - 值为true，表示将设置为隐私模式。 - 值为false，表示将设置为非隐私模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permissions check fails. |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ets
let isPrivacyMode: boolean = true;
panel.setPrivacyMode(isPrivacyMode);
```

#### setImmersiveMode15+

setImmersiveMode(mode: ImmersiveMode): void

设置输入法应用的沉浸模式。只能设置不使用沉浸模式(NONE_IMMERSIVE)、浅色沉浸模式(LIGHT_IMMERSIVE)或深色沉浸模式(DARK_IMMERSIVE)。不能设置为沉浸模式(IMMERSIVE)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | ImmersiveMode | 是 | 沉浸模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**示例：**

```ets
panel.setImmersiveMode(inputMethodEngine.ImmersiveMode.LIGHT_IMMERSIVE);
```

#### getImmersiveMode15+

getImmersiveMode(): ImmersiveMode

获取输入法应用的沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ImmersiveMode | 沉浸模式。 |

**示例：**

```ets
let mode: inputMethodEngine.ImmersiveMode = panel.getImmersiveMode();
```

#### setImmersiveEffect20+

setImmersiveEffect(effect: ImmersiveEffect): void

设置输入法应用的沉浸效果。

- 只有在[启用沉浸式模式](#ZH-CN_TOPIC_0000002553201227__setimmersivemode15)时，才能使用渐变模式和流光模式。

- 只有在启用渐变模式时，才能使用流光模式。
- 未启用渐变模式时，渐变高度必须为0px。
- 只有系统应用才能设置流光模式。
- 必须先调用以下任一接口，才能调用当前接口：

  - [adjustPanelRect](#ZH-CN_TOPIC_0000002553201227__adjustpanelrect12)(支持API version 12)

  - [adjustPanelRect](#ZH-CN_TOPIC_0000002553201227__adjustpanelrect15)(支持API version 15)

  - [resize](#ZH-CN_TOPIC_0000002553201227__resize10)(支持API version 10)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | ImmersiveEffect | 是 | 沉浸效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes:1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800020 | invalid immersive effect. 1.The gradient mode and the fluid light mode can only be used when the immersive mode is enabled. 2.The fluid light mode can only be used when the gradient mode is enabled. 3.When the gradient mode is not enabled, the gradient height can only be 0. |
| 12800021 | this operation is allowed only after adjustPanelRect or resize is called. |

**示例：**

```ets
let effect: inputMethodEngine.ImmersiveEffect = {
  gradientHeight: 100,
  gradientMode: inputMethodEngine.GradientMode.LINEAR_GRADIENT
}
panel.setImmersiveEffect(effect);
```

#### setKeepScreenOn20+

setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

设置屏幕常亮。使用Promise异步回调。

- 当键盘拉起时设置常亮生效，键盘关闭则自动失效。
- 规范使用该接口：必要场景（例如：语音输入）下，设置该属性为true；退出必要场景后，重置该属性为false；其他场景下，不使用该接口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isKeepScreenOn | boolean | 是 | 是否设置屏幕常亮。true表示打开屏幕常亮，false表示关闭屏幕常亮。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800013 | window manager service error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

panel.setKeepScreenOn(true).then(() => {
  console.info(`setKeepScreenOn success.`);
}).catch((error: BusinessError) => {
  console.error(`setKeepScreenOn failed, code: ${error.code}, message: ${error.message}`);
})
```

#### getSystemPanelCurrentInsets21+

getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>

获取指定屏幕当前状态（例如：折叠或展开）下，当前输入法键盘状态（例如：悬浮或固定）下输入法软键盘相对系统面板的偏移区域。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 输入法键盘所在屏幕的displayId，可通过getDisplayId获取 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<SystemPanelInsets> | Promise对象。输入法键盘与系统面板的偏移区域。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. Possible causes: 1. Current panel's type is not SOFT_KEYBOARD. 2. Panel's flag is not FLG_FIXED or FLG_FLOATING. |
| 12800022 | invalid displayId. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
let panelConfig: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}
// 以下逻辑需要在输入法InputMethodExtensionAbility中执行，this.context是InputMethodExtensionAbility的上下文
inputMethodAbility.createPanel(this.context, panelConfig).then( (panel: inputMethodEngine.Panel) =>{
  panel.getDisplayId().then((displayId: number) => {
    panel.getSystemPanelCurrentInsets(displayId).then((insets: inputMethodEngine.SystemPanelInsets) => {
      console.info(`getSystemPanelCurrentInsets success, insets is { left: ${insets.left}, right: ${insets.right}, bottom: ${insets.bottom} }`);
    }).catch((error: BusinessError) => {
      console.error(`getSystemPanelCurrentInsets failed, code: ${error.code}, message: ${error.message}`);
    })
  });
})
```

#### setSystemPanelButtonColor22+

setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>

设置当前面板功能键颜色和功能键的背景颜色。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillColor | string|undefined | 是 | 功能键的颜色，取值范围为[#01000000, #FFFFFFFF] 或 [#000000, #FFFFFF]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。 |
| backgroundColor | string|undefined | 是 | 功能键的背景颜色，取值范围为[#01000000, #FFFFFFFF] 或 [#000000, #FFFFFF]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fillColor = "#FFFF00";
  let backgroundColor = "#0000FF";
  this.panel.setSystemPanelButtonColor(fillColor, backgroundColor).then(() => {
    console.info(`setSystemPanelButtonColor success.`);
  }).catch((error: BusinessError) => {
    console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
  })
} catch (err) {
  let error = err as BusinessError;
  console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
}
```

#### KeyboardController

下列API均需使用[on('inputStart')](#ZH-CN_TOPIC_0000002553201227__oninputstart9)获取到KeyboardController实例后，通过实例调用。

#### hide9+

hide(callback: AsyncCallback<void>): void

隐藏输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});
```

#### hide9+

hide(): Promise<void>

隐藏输入法。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
});
```

#### hideKeyboard(deprecated)

hideKeyboard(callback: AsyncCallback<void>): void

隐藏输入法。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[hide](#ZH-CN_TOPIC_0000002553201227__hide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});
```

#### hideKeyboard(deprecated)

hideKeyboard(): Promise<void>

隐藏输入法。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[hide](#ZH-CN_TOPIC_0000002553201227__hide9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.info(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
});
```

#### exitCurrentInputType11+

exitCurrentInputType(callback: AsyncCallback<void>): void

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当退出当前输入类型成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType((err: BusinessError) => {
  if (err) {
    console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info('Succeeded in exiting current input type.');
});
```

#### exitCurrentInputType11+

exitCurrentInputType(): Promise<void>

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType().then(() => {
  console.info('Succeeded in exiting current input type.');
}).catch((err: BusinessError) => {
  console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
});
```

#### SecurityMode11+

输入法的安全模式，如BASIC或FULL。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASIC | 0 | 基础访问模式，基础打字模式，会限制网络访问。 |
| FULL | 1 | 完全访问模式，不做限制，可以访问网络。 |

#### ExtendAction10+

编辑框中文本的扩展编辑操作类型，如剪切、复制等。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECT_ALL | 0 | 全选。 |
| CUT | 3 | 剪切。 |
| COPY | 4 | 复制。 |
| PASTE | 5 | 粘贴。 |

#### Direction10+

光标的移动方向。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CURSOR_UP | 1 | 向上。 |
| CURSOR_DOWN | 2 | 向下。 |
| CURSOR_LEFT | 3 | 向左。 |
| CURSOR_RIGHT | 4 | 向右。 |

#### Range10+

选中的文本范围。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 否 | 选中文本的首字符在编辑框的索引值。 |
| end | number | 否 | 否 | 选中文本的末字符在编辑框的索引值。 |

#### Movement10+

选中文本时，光标移动的方向

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | Direction | 否 | 否 | 选中文本时，光标的移动方向。 |

#### MessageHandler15+

自定义通信对象。


开发者可通过注册此对象来接收已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，接收到自定义通信数据时会触发此对象中[onMessage](#ZH-CN_TOPIC_0000002553201227__onmessage15)回调函数。

此对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#ZH-CN_TOPIC_0000002553201227__onterminated15)回调函数。

若取消注册全局已注册的对象时，会触发被取消对象中[onTerminated](#ZH-CN_TOPIC_0000002553201227__onterminated15)回调函数。

#### onMessage15+

onMessage(msgId: string, msgParam?: ArrayBuffer): void

接收已绑定当前输入法应用的编辑框应用发送的自定义数据回调函数。


当已注册的[MessageHandler](#ZH-CN_TOPIC_0000002553201227__messagehandler15)接收到来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据时，会触发该回调函数。

msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgId | string | 是 | 接收到的自定义通信数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 接收到的自定义通信数据的消息体。 |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      inputClient.recvMessage(messageHandler);
    });
```

#### onTerminated15+

onTerminated(): void

监听对象终止回调函数。


当应用注册新的[MessageHandler](#ZH-CN_TOPIC_0000002553201227__messagehandler15)对象时，会触发上一个已注册[MessageHandler](#ZH-CN_TOPIC_0000002553201227__messagehandler15)对象的[onTerminated](#ZH-CN_TOPIC_0000002553201227__onterminated15)回调函数。

当应用取消注册时，会触发当前已注册[MessageHandler](#ZH-CN_TOPIC_0000002553201227__messagehandler15)对象的[onTerminated](#ZH-CN_TOPIC_0000002553201227__onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例：**

```ets
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      inputClient.recvMessage(messageHandler);
    });
```

#### InputClient9+

下列API均需使用[on('inputStart')](#ZH-CN_TOPIC_0000002553201227__oninputstart9)获取到InputClient实例后，通过实例调用。

#### sendKeyFunction9+

sendKeyFunction(action:number, callback: AsyncCallback<boolean>): void

发送功能键。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。 - 当值为0时，表示无效按键。 - 当值为1时，表示确认键（即回车键）。 |
callbackAsyncCallback<boolean>是回调函数。当功能键发送成功，err为undefined，data为true；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;

inputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

#### sendKeyFunction9+

sendKeyFunction(action: number): Promise<boolean>

发送功能键。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。 当值为0时，表示无效按键； 当值为1时，表示确认键（即回车键）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示功能键发送成功；返回false表示功能键发送失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
inputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
});
```

#### getForward9+

getForward(length:number, callback: AsyncCallback<string>): void

获取光标前固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

#### getForward9+

getForward(length:number): Promise<string>

获取光标前固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标前固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### getForwardSync10+

getForwardSync(length:number): string

获取光标前固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回光标前固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
let length: number = 1;
let text: string = inputClient.getForwardSync(length);
console.info(`Succeeded in getting forward, text: ${text}`);
```

#### getBackward9+

getBackward(length:number, callback: AsyncCallback<string>): void

获取光标后固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

#### getBackward9+

getBackward(length:number): Promise<string>

获取光标后固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标后固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length).then((text: string) => {
  console.info('Succeeded in getting backward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### getBackwardSync10+

getBackwardSync(length:number): string

获取光标后固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回光标后固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
let length: number = 1;
let text: string = inputClient.getBackwardSync(length);
console.info(`Succeeded in getting backward, text: ${text}`);
```

#### deleteForward9+

deleteForward(length:number, callback: AsyncCallback<boolean>): void

删除光标前固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error(`Failed to deleteForward.`);
  }
});
```

#### deleteForward9+

deleteForward(length:number): Promise<boolean>

删除光标前固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete Forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### deleteForwardSync10+

deleteForwardSync(length:number): void

删除光标前固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
let length: number = 1;
inputClient.deleteForwardSync(length);
```

#### deleteBackward9+

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

删除光标后固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error(`Failed to deleteBackward.`);
  }
});
```

#### deleteBackward9+

deleteBackward(length:number): Promise<boolean>

删除光标后固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### deleteBackwardSync10+

deleteBackwardSync(length:number): void

删除光标后固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
let length: number = 1;
inputClient.deleteBackwardSync(length);
```

#### insertText9+

insertText(text:string, callback: AsyncCallback<boolean>): void

插入文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});
```

#### insertText9+

insertText(text:string): Promise<boolean>

插入文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

#### insertTextSync10+

insertTextSync(text: string): void

插入文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
inputClient.insertTextSync('test');
```

#### getEditorAttribute9+

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

获取编辑框属性值。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<EditorAttribute> | 是 | 回调函数。当编辑框属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute((err: BusinessError, editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
});
```

#### getEditorAttribute9+

getEditorAttribute(): Promise<EditorAttribute>

获取编辑框属性值。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<EditorAttribute> | Promise对象，返回编辑框属性值。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

#### getEditorAttributeSync10+

getEditorAttributeSync(): EditorAttribute

获取编辑框属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| EditorAttribute | 编辑框属性对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
let editorAttribute: inputMethodEngine.EditorAttribute = inputClient.getEditorAttributeSync();
console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
```

#### moveCursor9+

moveCursor(direction: number, callback: AsyncCallback<void>): void

移动光标。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 光标移动方向。 - 当值为1时，表示向上。 - 当值为2时，表示向下。 - 当值为3时，表示向左。 - 当值为4时，表示向右。不能小于0。 |
callbackAsyncCallback<void>是回调函数。当光标移动成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving cursor.');
});
```

#### moveCursor9+

moveCursor(direction: number): Promise<void>

移动光标。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 光标移动方向。 - 当值为1时，表示向上。 - 当值为2时，表示向下。 - 当值为3时，表示向左。 - 当值为4时，表示向右。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP).then(() => {
  console.info('Succeeded in moving cursor.');
}).catch((err: BusinessError) => {
  console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
});
```

#### moveCursorSync10+

moveCursorSync(direction: number): void

移动光标。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | number | 是 | 光标移动方向。 - 当值为1时，表示向上。 - 当值为2时，表示向下。 - 当值为3时，表示向左。 - 当值为4时，表示向右。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR_UP);
```

#### selectByRange10+

selectByRange(range: Range, callback: AsyncCallback<void>): void

根据索引范围选中文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | Range | 是 | 选中文本的范围。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by range.');
});
```

#### selectByRange10+

selectByRange(range: Range): Promise<void>

根据索引范围选中文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | Range | 是 | 选中文本的范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range).then(() => {
  console.info('Succeeded in selecting by range.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
});
```

#### selectByRangeSync10+

selectByRangeSync(range: Range): void

根据索引范围选中文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | Range | 是 | 选中文本的范围。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRangeSync(range);
```

#### selectByMovement10+

selectByMovement(movement: Movement, callback: AsyncCallback<void>): void

根据光标移动方向选中文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movement | Movement | 是 | 选中时光标移动的方向。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by movement.');
});
```

#### selectByMovement10+

selectByMovement(movement: Movement): Promise<void>

根据光标移动方向选中文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movement | Movement | 是 | 选中时光标移动的方向。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement).then(() => {
  console.info('Succeeded in selecting by movement.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
});
```

#### selectByMovementSync10+

selectByMovementSync(movement: Movement): void

根据光标移动方向选中文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| movement | Movement | 是 | 选中时光标移动的方向。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ets
let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovementSync(movement);
```

#### getTextIndexAtCursor10+

getTextIndexAtCursor(callback: AsyncCallback<number>): void

获取光标所在处的文本索引。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。当文本索引获取成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor((err: BusinessError, index: number) => {
  if (err) {
    console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
});
```

#### getTextIndexAtCursor10+

getTextIndexAtCursor(): Promise<number>

获取光标所在处的文本索引。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回光标所在处的文本索引。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor().then((index: number) => {
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
});
```

#### getTextIndexAtCursorSync10+

getTextIndexAtCursorSync(): number

获取光标所在处的文本索引。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回光标所在处的文本索引。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
let index: number = inputClient.getTextIndexAtCursorSync();
console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

#### sendExtendAction10+

sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void

发送扩展编辑操作。使用callback异步回调。


输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](@ohos.inputMethod (输入法框架).md#ZH-CN_TOPIC_0000002522241258__onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](#ZH-CN_TOPIC_0000002553201227__extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | ExtendAction | 是 | 要发送的扩展操作。 |
| callback | AsyncCallback<void> | 是 | 回调函数。发送成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in sending extend action.');
});
```

#### sendExtendAction10+

sendExtendAction(action: ExtendAction): Promise<void>

发送扩展编辑操作。使用promise异步回调。


输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](@ohos.inputMethod (输入法框架).md#ZH-CN_TOPIC_0000002522241258__onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](#ZH-CN_TOPIC_0000002553201227__extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | ExtendAction | 是 | 要发送的扩展操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY).then(() => {
  console.info('Succeeded in sending extend action.');
}).catch((err: BusinessError) => {
  console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
});
```

#### sendPrivateCommand12+

sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>

发送私有数据至需要与输入法应用通信的系统其他部分。使用promise异步回调。

- 私有数据通道是系统预置输入法应用与系统特定组件（如文本框、桌面应用等）的通信机制，常用于设备级厂商在特定设备上实现自定义的输入法功能。
- 私有数据规格限制：总大小32KB，数量限制5条。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commandData | Record<string, CommandDataType> | 是 | 私有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodEngine.getInputMethodAbility().on('inputStart', (kbController, textInputClient) => {
  let record: Record<string, inputMethodEngine.CommandDataType> = {
    "valueString1": "abcdefg",
    "valueString2": true,
    "valueString3": 500,
  }
  textInputClient.sendPrivateCommand(record).then(() => {
  }).catch((err: BusinessError) => {
    if (err !== undefined) {
      console.error(`sendPrivateCommand catch error: ${err.code} ${err.message}`);
    }
  });
})
```

#### getCallingWindowInfo12+

getCallingWindowInfo(): Promise<WindowInfo>

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。


本接口仅适用于适配使用[Panel](#ZH-CN_TOPIC_0000002553201227__panel10)作为软键盘窗口的输入法应用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<WindowInfo> | Promise对象，返回拉起输入法的输入框所在应用窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800012 | the input method panel does not exist. |
| 12800013 | window manager service error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getCallingWindowInfo().then((windowInfo: inputMethodEngine.WindowInfo) => {
  console.info(`windowInfo.rect: ${windowInfo.rect.left}, ${windowInfo.rect.top}, ${windowInfo.rect.width}, ${windowInfo.rect.height}`);
  console.info(`windowInfo.status: ${windowInfo.status}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getCallingWindowInfo. Code is ${err.code}, message is ${err.message}`);
});
```

#### setPreviewText12+

setPreviewText(text: string, range: Range): Promise<void>

设置预上屏文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 将被预上屏的文本。 |
| range | Range | 是 | 目标替换的文本范围。 - 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。 - 当start等于end，默认将参数text插入start对应的光标位置。 - 当start不等于end，将参数text替换range对应区域的文本。 - 当start与end为其他含有负数值的组合，按照参数错误返回。 - 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。 - 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewText('test', range).then(() => {
  console.info('Succeeded in setting preview text.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setPreviewText. Code is ${err.code}, message is ${err.message}`);
});
```

#### setPreviewTextSync12+

setPreviewTextSync(text: string, range: Range): void

设置预上屏文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 将被预上屏的文本。 |
| range | Range | 是 | 目标替换的文本范围。 - 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。 - 当start等于end，默认将参数text插入start对应的光标位置。 - 当start不等于end，将参数text替换range对应区域的文本。 - 当start与end为其他含有负数值的组合，按照参数错误返回。 - 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。 - 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```ets
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewTextSync('test', range);
```

#### finishTextPreview12+

finishTextPreview(): Promise<void>

结束预上屏。使用promise异步回调。

若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.finishTextPreview().then(() => {
  console.info('Succeeded in finishing text preview.');
}).catch((err: BusinessError) => {
  console.error(`Failed to finishTextPreview. Code is ${err.code}, message is ${err.message}`);
});
```

#### finishTextPreviewSync12+

finishTextPreviewSync(): void

结束预上屏。

若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```ets
inputClient.finishTextPreviewSync();
```

#### sendMessage15+

sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>

发送自定义通信至已绑定当前输入法应用的编辑框应用。使用Promise异步回调。

该接口需要编辑框与输入法绑定并进入编辑状态，且输入法应用处于完整体验模式时才能调用。

msgId最大限制256B，msgParam最大限制128KB。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgId | string | 是 | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的消息体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800014 | the input method is in basic mode. |
| 12800015 | the other side does not accept the request. |
| 12800016 | input method client is not editable. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputClient.sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send message. Code is ${err.code}, message is ${err.message}`);
});
```

#### recvMessage15+

recvMessage(msgHandler?: MessageHandler): void;

注册或取消注册Messagehandler。


[MessageHandler](#ZH-CN_TOPIC_0000002553201227__messagehandler15)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#ZH-CN_TOPIC_0000002553201227__onterminated15)回调函数。

未填写参数，则取消全局已注册的[MessageHandler](#ZH-CN_TOPIC_0000002553201227__messagehandler15)，并会触发被取消注册对象中[onTerminated](#ZH-CN_TOPIC_0000002553201227__onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgHandler | MessageHandler | 否 | 该对象将通过onMessage接收来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，并通过onTerminated接收终止此对象订阅的消息。 若不填写此参数，则取消全局已注册的MessageHandler对象，同时触发其onTerminated回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```ets
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      inputClient.recvMessage(messageHandler);
    });
```

#### getAttachOptions19+

getAttachOptions(): AttachOptions

获取绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AttachOptions | 返回绑定输入法时的附加选项内容。 |


从API version 20 开始，错误码801 Capability not supported.被移除。

**示例：**

```ets
let attachOptions: inputMethodEngine.AttachOptions = inputClient.getAttachOptions();
console.info(`Succeeded in getting AttachOptions, AttachOptions is ${attachOptions}`);
```

#### on('attachOptionsDidChange')19+

on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | Callback<AttachOptions> | 是 | 回调函数，返回绑定输入法时的附加选项。 |


从API version 20 开始，错误码801 Capability not supported.被移除。

**示例：**

```ets
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

#### off('attachOptionsDidChange')19+

off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void

取消订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | Callback<AttachOptions> | 否 | 取消订阅的回调函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例：**

```ets
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

#### CapitalizeMode20+

枚举，定义了文本首字母大写的不同模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不进行任何首字母大写处理。 |
| SENTENCES | 1 | 每个句子的首字母大写。 |
| WORDS | 2 | 每个单词的首字母大写。 |
| CHARACTERS | 3 | 每个字母都大写。 |

#### EditorAttribute

编辑框属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enterKeyType | number | 是 | 否 | 编辑框的功能属性，详见常量中的功能键定义。 |
| inputPattern | number | 是 | 否 | 编辑框的文本属性，详见常量中的编辑框定义。 |
| isTextPreviewSupported12+ | boolean | 否 | 否 | 编辑框是否支持预上屏。 - 值为true，表示支持。 - 值为false，表示不支持。 |
| bundleName14+ | string | 是 | 是 | 编辑框所属应用包名；该值可能为""，使用该属性时需要考虑为""的场景。 |
| immersiveMode15+ | ImmersiveMode | 是 | 是 | 输入法沉浸模式。 |
| windowId18+ | number | 是 | 是 | 编辑框设置所属窗口ID。 |
| displayId18+ | number | 是 | 是 | 编辑框设置窗口对应的屏幕ID。如果没有设置windowId，取当前焦点窗口屏幕ID。 |
| placeholder20+ | string | 是 | 是 | 编辑框设置的占位符信息。 |
| abilityName20+ | string | 是 | 是 | 编辑框设置的ability名称。 |
| capitalizeMode20+ | CapitalizeMode | 是 | 是 | 编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。 |
| gradientMode20+ | GradientMode | 是 | 是 | 渐变模式。如果没有设置或设置非法值，默认不使用渐变模式。 |
| extraConfig22+ | InputMethodExtraConfig | 是 | 是 | 输入法扩展信息。 |

#### KeyEvent

按键属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | number | 是 | 否 | 按键的键值。键码值说明参考KeyCode。 |
| keyAction | number | 是 | 否 | 按键事件类型。 - 当值为2时，表示按下事件； - 当值为3时，表示抬起事件。 |

#### PanelFlag10+

输入法面板状态类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FLG_FIXED | 0 | 固定态面板类型。 |
| FLG_FLOATING | 1 | 悬浮态面板类型。 |
| FLAG_CANDIDATE15+ | 2 | 候选词态面板类型。 |

#### PanelType10+

输入法面板类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SOFT_KEYBOARD | 0 | 软键盘类型。 |
| STATUS_BAR | 1 | 状态栏类型。 |

#### PanelInfo10+

输入法面板属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | PanelType | 否 | 否 | 面板的类型。 |
| flag | PanelFlag | 否 | 是 | 面板的状态类型。 |

#### PanelRect12+

输入法面板位置大小信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| landscapeRect | window.Rect | 否 | 否 | 横屏状态时输入法面板窗口的位置大小。 |
| portraitRect | window.Rect | 否 | 否 | 竖屏状态时输入法面板窗口的位置大小。 |

#### EnhancedPanelRect15+

增强的输入法面板位置、大小信息，包含自定义避让区域、自定义热区。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| landscapeRect | window.Rect | 否 | 是 | 横屏状态时输入法面板窗口的位置大小。 - 当fullScreenMode不填写或值为false时，此属性为必选。 |
| portraitRect | window.Rect | 否 | 是 | 竖屏状态时，输入法面板窗口的位置大小。 - 当fullScreenMode不填写或值为false时，此属性为必选。 |
| landscapeAvoidY | number | 否 | 是 | 横屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。 - 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。 - 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。 |
| landscapeInputRegion | Array<window.Rect> | 否 | 是 | 横屏状态时，面板接收输入事件的区域。 - 数组大小限制为[1, 4]。默认值为横屏时的面板大小。 - 传入的热区位置是相对于输入法面板窗口左顶点的位置。 |
| portraitAvoidY | number | 否 | 是 | 竖屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。 - 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。 - 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。 |
| portraitInputRegion | Array<window.Rect> | 否 | 是 | 竖屏状态时，面板接收输入事件的区域。 - 数组大小限制为[1, 4]。默认值为竖屏时的面板大小。 - 传入的热区位置是相对于输入法面板窗口左顶点的位置。 |
| fullScreenMode | boolean | 否 | 是 | 是否开启全屏模式。默认值为false。 - 值为true，landscapeRect和portraitRect可不填写。 - 值为false，landscapeRect和portraitRect为必选属性。 |

#### KeyboardArea15+

面板中的键盘区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| top | number | 否 | 否 | 键盘区域的上边界到面板区域上边界的距离，单位为px，该参数为整数。 |
| bottom | number | 否 | 否 | 键盘区域的下边界到面板区域下边界的距离，单位为px，该参数为整数。 |
| left | number | 否 | 否 | 键盘区域的左边界到面板区域左边界的距离，单位为px，该参数为整数。 |
| right | number | 否 | 否 | 键盘区域的右边界到面板区域右边界的距离，单位为px，该参数为整数。 |

#### AttachOptions19+

绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestKeyboardReason | RequestKeyboardReason | 否 | 是 | 该属性由编辑框应用设置，如果没有设置或设置非法值，则默认没有特定的原因触发键盘请求。 |
| isSimpleKeyboardEnabled20+ | boolean | 否 | 是 | 是否使能简单键盘，该属性由编辑框应用设置，true表示使能简单键盘，false表示不使能简单键盘。 如果没有设置或设置非法值，则默认不使能简单键盘。 |

#### WindowInfo12+

窗口信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rect | window.Rect | 否 | 否 | 窗口矩形区域。 |
| status | [window.WindowStatusType](../../types/enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11) | 否 | 否 | 窗口模式类型。 |

#### ImmersiveMode15+

枚举，输入法沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE_IMMERSIVE | 0 | 不使用沉浸模式。 |
| IMMERSIVE | 1 | 沉浸模式，由输入法应用确定沉浸模式类型。 |
| LIGHT_IMMERSIVE | 2 | 浅色沉浸模式。 |
| DARK_IMMERSIVE | 3 | 深色沉浸模式。 |

#### RequestKeyboardReason19+

枚举，请求键盘输入的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示没有特定的原因触发键盘请求。 |
| MOUSE | 1 | 表示键盘请求是由鼠标操作触发的。 |
| TOUCH | 2 | 表示键盘请求是由触摸操作触发的。 |
| OTHER | 20 | 表示键盘请求是由其他原因触发的。 |

#### GradientMode20+

枚举，输入法渐变模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不使用渐变模式。 |
| LINEAR_GRADIENT | 1 | 线性渐变。 |

#### ImmersiveEffect20+

沉浸效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| gradientHeight | number | 否 | 否 | 渐变高度，不能超过屏幕高度的15%。 |
| gradientMode | GradientMode | 否 | 否 | 渐变模式。 |

#### SystemPanelInsets21+

输入法软键盘相对系统面板的偏移区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bottom | number | 是 | 否 | 键盘区域的下边界到系统面板区域下边界的距离，单位为px，该参数为整数。 |
| left | number | 是 | 否 | 键盘区域的左边界到系统面板区域左边界的距离，单位为px，该参数为整数。 |
| right | number | 是 | 否 | 键盘区域的右边界到系统面板区域右边界的距离，单位为px，该参数为整数。 |

#### TextInputClient(deprecated)

下列API示例中都需使用[on('inputStart')](#ZH-CN_TOPIC_0000002553201227__oninputstartdeprecated)回调获取到TextInputClient实例，再通过此实例调用对应方法。


从API version 8开始支持，API version 9开始废弃，建议使用[InputClient](#ZH-CN_TOPIC_0000002553201227__inputclient9)替代。

#### getForward(deprecated)

getForward(length:number, callback: AsyncCallback<string>): void

获取光标前固定长度的文本。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[getForward](#ZH-CN_TOPIC_0000002553201227__getforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

#### getForward(deprecated)

getForward(length:number): Promise<string>

获取光标前固定长度的文本。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[getForward](#ZH-CN_TOPIC_0000002553201227__getforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标前固定长度的文本。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### getBackward(deprecated)

getBackward(length:number, callback: AsyncCallback<string>): void

获取光标后固定长度的文本。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](#ZH-CN_TOPIC_0000002553201227__getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

#### getBackward(deprecated)

getBackward(length:number): Promise<string>

获取光标后固定长度的文本。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](#ZH-CN_TOPIC_0000002553201227__getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回光标后固定长度的文本。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length).then((text: string) => {
  console.info(`'Succeeded in getting backward: ${text}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### deleteForward(deprecated)

deleteForward(length:number, callback: AsyncCallback<boolean>): void

删除光标前固定长度的文本。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](#ZH-CN_TOPIC_0000002553201227__deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to deleteForward.');
  }
});
```

#### deleteForward(deprecated)

deleteForward(length:number): Promise<boolean>

删除光标前固定长度的文本。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](#ZH-CN_TOPIC_0000002553201227__deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### deleteBackward(deprecated)

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

删除光标后固定长度的文本。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](#ZH-CN_TOPIC_0000002553201227__deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
});
```

#### deleteBackward(deprecated)

deleteBackward(length:number): Promise<boolean>

删除光标后固定长度的文本。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](#ZH-CN_TOPIC_0000002553201227__deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### sendKeyFunction(deprecated)

sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void

发送功能键。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](#ZH-CN_TOPIC_0000002553201227__sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。 - 当值为0时，表示无效按键； - 当值为1时，表示确认键（即回车键）。 |
callbackAsyncCallback<boolean>是回调函数。当功能键发送成功，err为undefined，data为true；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

#### sendKeyFunction(deprecated)

sendKeyFunction(action: number): Promise<boolean>

发送功能键。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](#ZH-CN_TOPIC_0000002553201227__sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | number | 是 | 功能键键值。 当值为0时，表示无效按键； 当值为1时，表示确认键（即回车键）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示发送功能键成功；返回false表示发送功能键失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction:. Code is ${err.code}, message is ${err.message}`);
});
```

#### insertText(deprecated)

insertText(text:string, callback: AsyncCallback<boolean>): void

插入文本。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[insertText](#ZH-CN_TOPIC_0000002553201227__inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});
```

#### insertText(deprecated)

insertText(text:string): Promise<boolean>

插入文本。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[insertText](#ZH-CN_TOPIC_0000002553201227__inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

#### getEditorAttribute(deprecated)

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

获取编辑框属性值。使用callback异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](#ZH-CN_TOPIC_0000002553201227__geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<EditorAttribute> | 是 | 回调函数。当编辑框的属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute((err: BusinessError,
  editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}`);
});
```

#### getEditorAttribute(deprecated)

getEditorAttribute(): Promise<EditorAttribute>

获取编辑框属性值。使用promise异步回调。


从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](#ZH-CN_TOPIC_0000002553201227__geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<EditorAttribute> | Promise对象，返回编辑框属性值。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```