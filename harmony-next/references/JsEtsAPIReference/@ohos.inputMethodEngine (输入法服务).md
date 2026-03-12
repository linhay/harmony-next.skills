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

名称类型值说明ENTER_KEY_TYPE_UNSPECIFIEDnumber0无功能键。ENTER_KEY_TYPE_GOnumber2“前往”功能键。ENTER_KEY_TYPE_SEARCHnumber3“搜索”功能键。ENTER_KEY_TYPE_SENDnumber4“发送”功能键。ENTER_KEY_TYPE_NEXTnumber5“下一个”功能键。ENTER_KEY_TYPE_DONEnumber6“回车”功能键。ENTER_KEY_TYPE_PREVIOUSnumber7“前一个”功能键。ENTER_KEY_TYPE_NEWLINE12+number8“换行”功能键。PATTERN_NULLnumber-1无特殊性编辑框。PATTERN_TEXTnumber0文本编辑框。PATTERN_NUMBERnumber2数字编辑框。PATTERN_PHONEnumber3电话号码编辑框。PATTERN_DATETIMEnumber4日期编辑框。PATTERN_EMAILnumber5邮件编辑框。PATTERN_URInumber6超链接编辑框。PATTERN_PASSWORDnumber7密码编辑框。PATTERN_PASSWORD_NUMBER11+number8数字密码编辑框。PATTERN_PASSWORD_SCREEN_LOCK11+number9锁屏密码编辑框。PATTERN_USER_NAME20+number10用户名编辑框。PATTERN_NEW_PASSWORD20+number11新密码编辑框。PATTERN_NUMBER_DECIMAL20+number12带小数点的数字编辑框。PATTERN_ONE_TIME_CODE20+number13验证码编辑框。OPTION_ASCIInumber20允许输入ASCII值。OPTION_NONEnumber0不指定编辑框输入属性。OPTION_AUTO_CAP_CHARACTERSnumber2允许输入字符。OPTION_AUTO_CAP_SENTENCESnumber8允许输入句子。OPTION_AUTO_WORDSnumber4允许输入单词。OPTION_MULTI_LINEnumber1允许输入多行。OPTION_NO_FULLSCREENnumber10半屏样式。FLAG_SELECTINGnumber2编辑框处于选择状态。FLAG_SINGLE_LINEnumber1编辑框为单行。DISPLAY_MODE_PARTnumber0编辑框显示为半屏。DISPLAY_MODE_FULLnumber1编辑框显示为全屏。CURSOR_UP9+number1光标上移。CURSOR_DOWN9+number2光标下移。CURSOR_LEFT9+number3光标左移。CURSOR_RIGHT9+number4光标右移。WINDOW_TYPE_INPUT_METHOD_FLOAT9+number2105输入法应用窗口风格标识。

#### inputMethodEngine.getInputMethodAbility9+

getInputMethodAbility(): InputMethodAbility

获取输入法应用客户端实例[InputMethodAbility](#ZH-CN_TOPIC_0000002529445255__inputmethodability)，仅支持输入法应用调用。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件、创建/销毁输入法面板等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明[InputMethodAbility](#ZH-CN_TOPIC_0000002529445255__inputmethodability)输入法应用客户端。

**示例：**

```ets
let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```

#### inputMethodEngine.getKeyboardDelegate9+

getKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](#ZH-CN_TOPIC_0000002529445255__keyboarddelegate)。

输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明[KeyboardDelegate](#ZH-CN_TOPIC_0000002529445255__keyboarddelegate)客户端编辑事件监听代理。

**示例：**

```ets
let KeyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();
```

#### inputMethodEngine.getInputMethodEngine(deprecated)

getInputMethodEngine(): InputMethodEngine

获取输入法应用客户端实例[InputMethodEngine](#ZH-CN_TOPIC_0000002529445255__inputmethodengine)。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件等。

从API version 8开始支持，API version 9开始废弃，建议使用[getInputMethodAbility()](#ZH-CN_TOPIC_0000002529445255__inputmethodenginegetinputmethodability9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明[InputMethodEngine](#ZH-CN_TOPIC_0000002529445255__inputmethodengine)输入法应用客户端。

**示例：**

```ets
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

#### inputMethodEngine.createKeyboardDelegate(deprecated)

createKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](#ZH-CN_TOPIC_0000002529445255__keyboarddelegate)。输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

从API version 8开始支持，API version 9开始废弃，建议使用[getKeyboardDelegate()](#ZH-CN_TOPIC_0000002529445255__inputmethodenginegetkeyboarddelegate9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明[KeyboardDelegate](#ZH-CN_TOPIC_0000002529445255__keyboarddelegate)客户端编辑事件监听代理。

**示例：**

```ets
let keyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.createKeyboardDelegate();
```

#### CommandDataType12+

type CommandDataType = number | string | boolean;

表示私有数据类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

类型说明string表示值类型为字符串。number表示值类型为数字。boolean表示值类型为布尔值。

#### SizeChangeCallback15+

type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void

当输入法面板大小变化时触发的回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明size[window.Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__size7)是当前面板大小。keyboardArea[KeyboardArea](#ZH-CN_TOPIC_0000002529445255__keyboardarea15)否当前面板中可作为键盘区域的大小。

#### InputMethodEngine

下列API均需使用[getInputMethodEngine](#ZH-CN_TOPIC_0000002529445255__inputmethodenginegetinputmethodenginedeprecated)获取到InputMethodEngine实例后，通过实例调用。

#### on('inputStart')

on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是设置监听类型，固定取值为'inputStart'。callback(kbController: [KeyboardController](#ZH-CN_TOPIC_0000002529445255__keyboardcontroller), textInputClient: [TextInputClient](#ZH-CN_TOPIC_0000002529445255__textinputclientdeprecated)) => void是回调函数，返回订阅输入法的KeyboardController和TextInputClient实例。

**示例：**

```ets
inputMethodEngine.getInputMethodEngine()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let textInputClient: inputMethodEngine.TextInputClient = textClient;
    });
```

#### off('inputStart')

off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

取消订阅输入法绑定成功事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是设置监听类型，固定取值为'inputStart'。callback(kbController: [KeyboardController](#ZH-CN_TOPIC_0000002529445255__keyboardcontroller), textInputClient: [TextInputClient](#ZH-CN_TOPIC_0000002529445255__textinputclientdeprecated)) => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**示例：**

```ets
inputMethodEngine.getInputMethodEngine()
  .off('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      console.info('delete inputStart notification.');
    });
```

#### on('keyboardShow'|'keyboardHide')

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是

设置监听类型。

-'keyboardShow'表示显示输入法软键盘。

-'keyboardHide'表示隐藏输入法软键盘。

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

#### off('keyboardShow'|'keyboardHide')

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是

要取消监听的输入法软键盘事件类型。

-'keyboardShow'表示显示输入法软键盘。

-'keyboardHide'表示隐藏输入法软键盘。

callback() => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**示例：**

```ets
inputMethodEngine.getInputMethodEngine().off('keyboardShow');
inputMethodEngine.getInputMethodEngine().off('keyboardHide');
```

#### InputMethodAbility

下列API均需使用[getInputMethodAbility](#ZH-CN_TOPIC_0000002529445255__inputmethodenginegetinputmethodability9)获取到InputMethodAbility实例后，通过实例调用。

#### on('inputStart')9+

on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是设置监听类型，固定取值为'inputStart'。callback(kbController: [KeyboardController](#ZH-CN_TOPIC_0000002529445255__keyboardcontroller), inputClient: [InputClient](#ZH-CN_TOPIC_0000002529445255__inputclient9)) => void是回调函数，返回输入法操作相关实例。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'inputStart'。callback(kbController: [KeyboardController](#ZH-CN_TOPIC_0000002529445255__keyboardcontroller), inputClient: [InputClient](#ZH-CN_TOPIC_0000002529445255__inputclient9)) => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**示例：**

```ets
inputMethodEngine.getInputMethodAbility().off('inputStart');
```

#### on('inputStop')9+

on(type: 'inputStop', callback: () => void): void

订阅停止输入法应用事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是设置监听类型，固定取值为'inputStop'。callback() => void是回调函数。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'inputStop'。callback() => void是取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'setCallingWindow'。callback(wid: number) => void是回调函数，返回调用方窗口的Id。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'setCallingWindow'。callback(wid:number) => void是取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是

设置监听类型。

- 'keyboardShow'表示显示输入法软键盘。

- 'keyboardHide'表示隐藏输入法软键盘。

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

参数名类型必填说明typestring是

设置监听类型。

- 'keyboardShow'表示显示键盘。

- 'keyboardHide'表示隐藏键盘。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'setSubtype'。callback(inputMethodSubtype: [InputMethodSubtype](@ohos.InputMethodSubtype (输入法子类型).md)) => void是回调函数，返回设置的输入法子类型。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'setSubtype'。callback(inputMethodSubtype: [InputMethodSubtype](@ohos.InputMethodSubtype (输入法子类型).md)) => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'securityModeChange'。callbackCallback<[SecurityMode](#ZH-CN_TOPIC_0000002529445255__securitymode11)>是回调函数，返回当前输入法应用的安全模式。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'securityModeChange'。callbackCallback<[SecurityMode](#ZH-CN_TOPIC_0000002529445255__securitymode11)>否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'privateCommand'。callbackCallback<Record<string, [CommandDataType](#ZH-CN_TOPIC_0000002529445255__commanddatatype12)>>是回调函数，返回向输入法应用发送的私有数据。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800010not the preconfigured default input method.

**示例：**

```ets
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i :number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }
inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);
```

#### off('privateCommand')12+

off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void

取消订阅输入法私有数据事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是设置监听类型，固定取值为'privateCommand'。callbackCallback<Record<string, [CommandDataType](#ZH-CN_TOPIC_0000002529445255__commanddatatype12)>>否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800010not the preconfigured default input method.

**示例：**

```ets
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i: number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }

inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);
```

#### on('callingDisplayDidChange')18+

on(type: 'callingDisplayDidChange', callback: Callback<number>): void

订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是设置监听类型，固定取值为'callingDisplayDidChange'。callbackCallback<number>是回调函数，返回编辑框设置对应窗口屏幕ID。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息801capability not supported.

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

参数名类型必填说明typestring是设置监听类型，固定取值为'callingDisplayDidChange'。callbackCallback<number>否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是

设置监听类型，固定取值为'discardTypingText'。

- 'discardTypingText'：表示订阅编辑框应用发送“清空候选词”事件到输入法。

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

参数名类型必填说明typestring是

设置监听类型，固定取值为'discardTypingText'。

- 'discardTypingText'：表示取消订阅编辑框应用发送“清空候选词”事件到输入法。

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

类型说明[SecurityMode](#ZH-CN_TOPIC_0000002529445255__securitymode11)安全模式。

**错误码：**

错误码ID错误信息12800004not an input method application.

**示例：**

```ets
let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(`getSecurityMode, securityMode is : ${security}`);
```

#### createPanel10+

createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](@ohos.InputMethodExtensionAbility (InputMethodExtensionAbility).md#ZH-CN_TOPIC_0000002529285279__inputmethodextensionability)类中调用。使用callback异步回调。

单个输入法应用仅允许创建一个[软键盘类型](#ZH-CN_TOPIC_0000002529445255__paneltype10)和一个[状态栏类型](#ZH-CN_TOPIC_0000002529445255__paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa#设置应用子窗口)、[bindContextMenu](zh-cn_topic_0000002497604848.html#ZH-CN_TOPIC_0000002497604848__bindcontextmenu8)、[CustomDialog](自定义弹窗 (CustomDialog).md)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](弹出框 (Dialog).md)、[bindMenu](菜单控制.md#ZH-CN_TOPIC_0000002497604848__bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明ctx[BaseContext](BaseContext.md)是当前输入法应用上下文信息。info[PanelInfo](#ZH-CN_TOPIC_0000002529445255__panelinfo10)是输入法面板信息。callbackAsyncCallback<[Panel](#ZH-CN_TOPIC_0000002529445255__panel10)>是回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。

**错误码：**

错误码ID错误信息401parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.12800004not an input method application.

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

createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](@ohos.InputMethodExtensionAbility (InputMethodExtensionAbility).md#ZH-CN_TOPIC_0000002529285279__inputmethodextensionability)类中调用。使用promise异步回调。

单个输入法应用仅允许创建一个[软键盘类型](#ZH-CN_TOPIC_0000002529445255__paneltype10)和一个[状态栏类型](#ZH-CN_TOPIC_0000002529445255__paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa#设置应用子窗口)、[bindContextMenu](zh-cn_topic_0000002497604848.html#ZH-CN_TOPIC_0000002497604848__bindcontextmenu8)、[CustomDialog](自定义弹窗 (CustomDialog).md)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](弹出框 (Dialog).md)、[bindMenu](菜单控制.md#ZH-CN_TOPIC_0000002497604848__bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明ctx[BaseContext](BaseContext.md)是当前输入法应用上下文信息。info[PanelInfo](#ZH-CN_TOPIC_0000002529445255__panelinfo10)是输入法面板信息。

**返回值：**

类型说明Promise<[Panel](#ZH-CN_TOPIC_0000002529445255__panel10)>回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。

**错误码：**

错误码ID错误信息401parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.12800004not an input method application.

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

参数名类型必填说明panel[Panel](#ZH-CN_TOPIC_0000002529445255__panel10)是要销毁的面板对象。callbackAsyncCallback<void>是回调函数。当输入法面板销毁成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

参数名类型必填说明panel[Panel](#ZH-CN_TOPIC_0000002529445255__panel10)是要销毁的面板对象。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

下列API均需使用[getKeyboardDelegate](#ZH-CN_TOPIC_0000002529445255__inputmethodenginegetkeyboarddelegate9)获取到KeyboardDelegate实例后，通过实例调用。

#### on('keyDown'|'keyUp')

on(type: 'keyDown'|'keyUp', callback: (event: KeyEvent) => boolean): void

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是

设置监听类型。

- 'keyDown'表示键盘按下。

- 'keyUp'表示键盘抬起。

callback(event: [KeyEvent](#ZH-CN_TOPIC_0000002529445255__keyevent)) => boolean是回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。

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

参数名类型必填说明typestring是

设置监听类型。

- 'keyDown'表示键盘按下。

- 'keyUp'表示键盘抬起。

callback(event: [KeyEvent](#ZH-CN_TOPIC_0000002529445255__keyevent)) => boolean否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'keyEvent'。callback(event: [InputKeyEvent](@ohos.multimodalInput.keyEvent (按键输入事件).md#ZH-CN_TOPIC_0000002529445533__keyevent)) => boolean是

回调函数，入参为按键事件信息，返回值类型为布尔类型。

- 入参按键事件信息的数据类型为[InputKeyEvent](@ohos.multimodalInput.keyEvent (按键输入事件).md#ZH-CN_TOPIC_0000002529445533__keyevent)。

- 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。

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

参数名类型必填说明typestring是设置监听类型，固定取值为'keyEvent'。callbackfunction否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是光标变化事件，固定取值为'cursorContextChange'。callback(x: number, y: number, height: number) => void是

回调函数，返回光标信息。

- x为光标上端的x坐标值，y为光标上端的y坐标值，height为光标的高度值。

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

参数名类型必填说明typestring是光标变化事件，固定取值为'cursorContextChange'。callback(x: number, y:number, height:number) => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是文本选择变化事件，固定取值为'selectionChange'。callback(oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void是

回调函数，返回文本选择信息。

- oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。

- newBegin为变化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。

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

参数名类型必填说明typestring是文本选择变化事件，固定取值为'selectionChange'。callback(oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是文本变化事件，固定取值为'textChange'。callback(text: string) => void是回调函数，返回订阅的文本内容。

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

参数名类型必填说明typestring是文本变化事件，固定取值为'textChange'。callback(text: string) => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

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

参数名类型必填说明typestring是文本变化事件，固定取值为'editorAttributeChanged'。callback(attr: [EditorAttribute](#ZH-CN_TOPIC_0000002529445255__editorattribute)) => void是回调函数，返回变化的编辑框属性。

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

参数名类型必填说明typestring是文本变化事件，固定取值为'editorAttributeChanged'。callback(attr: [EditorAttribute](#ZH-CN_TOPIC_0000002529445255__editorattribute)) => void否所要取消订阅的回调处理函数。参数不填写时，默认取消订阅type对应的所有回调事件。

**示例：**

```ets
inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');
```

#### Panel10+

下列API均需使用[createPanel](#ZH-CN_TOPIC_0000002529445255__createpanel10)获取到Panel实例后，通过实例调用。

#### setUiContent10+

setUiContent(path: string, callback: AsyncCallback<void>): void

为当前的输入法面板加载具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明pathstring是具体页面的路径。callbackAsyncCallback<void>是回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

参数名类型必填说明pathstring是具体页面的路径。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

为当前的输入法面板加载与LocalStorage相关联的具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明pathstring是LocalStorage相关联的具体页面的路径。storage[LocalStorage](应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)是存储单元，为应用程序范围内的可变和不可变状态属性提供存储。callbackAsyncCallback<void>是回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

setUiContent(path: string, storage: LocalStorage): Promise<void>

为当前面板加载与LocalStorage相关联的具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明pathstring是设置加载页面的路径。storage[LocalStorage](应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)是存储单元，为应用程序范围内的可变状态属性和非可变状态属性提供存储。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明widthnumber是目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。heightnumber是目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。callbackAsyncCallback<void>是回调函数。当面板大小改变成功，err为undefined，否则err为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明widthnumber是目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。heightnumber是目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

移动面板位置，使用callback异步回调。[面板状态](#ZH-CN_TOPIC_0000002529445255__panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明xnumber是横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。ynumber是纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。callbackAsyncCallback<void>是回调函数。当面板位置移动成功，err为undefined，否则err为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

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

移动面板位置，使用promise异步回调。[面板状态](#ZH-CN_TOPIC_0000002529445255__panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明xnumber是横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。ynumber是纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

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

错误码ID错误信息801capability not supported.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800013window manager service error.12800017invalid panel type or panel flag.

**示例：**

```ets
panel.startMoving();
```

#### getDisplayId15+

getDisplayId(): Promise<number>

获取当前窗口的所在id，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明Promise<number>Promise对象。返回窗口的displayId。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800013window manager service error.

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

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当面板显示成功，err为undefined，否则err为错误对象。

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

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当面板隐藏成功，err为undefined，否则err为错误对象。

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

类型说明Promise<void>无返回结果的Promise对象。

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

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明flag[PanelFlag](#ZH-CN_TOPIC_0000002529445255__panelflag10)是目标面板状态类型。类型为FLG_FIXED或FLG_FLOATING。rect[PanelRect](#ZH-CN_TOPIC_0000002529445255__panelrect12)是目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度。固定态：高度不能超过屏幕高度的70%，宽度不能超过屏幕宽度；悬浮态：高度不能超过屏幕高度，宽度不能超过屏幕宽度。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800013window manager service error.

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

仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。此接口兼容[adjustPanelRect](#ZH-CN_TOPIC_0000002529445255__adjustpanelrect12)的调用方法，若入参rect仅填写属性landscapeRect和portraitRect，则默认调用[adjustPanelRect](#ZH-CN_TOPIC_0000002529445255__adjustpanelrect12)。

此接口为同步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明flag[PanelFlag](#ZH-CN_TOPIC_0000002529445255__panelflag10)是目标面板状态类型。类型为FLG_FIXED或FLG_FLOATING。rect[EnhancedPanelRect](#ZH-CN_TOPIC_0000002529445255__enhancedpanelrect15)是目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800013window manager service error.12800017invalid panel type or panel flag.

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

参数名类型必填说明inputRegionArray<[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)>是

面板内接收输入事件的区域。

- 数组大小限制为[1, 4]。

- 传入的热区位置是相对于输入法面板窗口左顶点的位置。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800013window manager service error.12800017invalid panel type or panel flag.

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

参数名类型必填说明typestring是监听当前面板的状态类型，固定取值为'show'。callback() => void是回调函数。

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

参数名类型必填说明typestring是监听当前面板的状态类型，固定取值为'hide'。callback() => void是回调函数。

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

- 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__size7)类型的必选参数。
- 从API version 15起，调用[adjustPanelRect](#ZH-CN_TOPIC_0000002529445255__adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](#ZH-CN_TOPIC_0000002529445255__keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是监听当前面板的大小是否产生变化，固定值为'sizeChange'。callback[SizeChangeCallback](#ZH-CN_TOPIC_0000002529445255__sizechangecallback15)是回调函数。返回当前软键盘面板的大小，包含宽度和高度值。

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

参数名类型必填说明typestring是取消监听当前面板的状态类型，固定取值为'show'。callback() => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
panel.off('show');
```

#### off('hide')10+

off(type: 'hide', callback?: () => void): void

取消监听当前面板的隐藏状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是要取消监听的当前面板状态类型，固定取值为'hide'。callback() => void否取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
panel.off('hide');
```

#### off('sizeChange')12+

off(type: 'sizeChange', callback?: SizeChangeCallback): void

取消监听当前面板大小变化，使用callback异步回调。

仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。

- 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__size7)类型的必选参数。
- 从API version 15起，调用[adjustPanelRect](#ZH-CN_TOPIC_0000002529445255__adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](#ZH-CN_TOPIC_0000002529445255__keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明typestring是监听当前面板的大小是否产生变化，固定取值为'sizeChange'。callback[SizeChangeCallback](#ZH-CN_TOPIC_0000002529445255__sizechangecallback15)否回调函数。返回当前软键盘面板的大小，包含宽度和高度值。

**示例：**

```ets
import { window } from '@kit.ArkUI';

panel.off('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

#### changeFlag10+

changeFlag(flag: PanelFlag): void

将输入法应用的面板状态改变为其他[PanelFlag](#ZH-CN_TOPIC_0000002529445255__panelflag10)形态，仅对[SOFT_KEYBOARD](#ZH-CN_TOPIC_0000002529445255__paneltype10)生效。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明flag[PanelFlag](#ZH-CN_TOPIC_0000002529445255__panelflag10)是目标面板状态类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

参数名类型必填说明isPrivacyModeboolean是

是否设置隐私模式。

- 值为true，表示将设置为隐私模式。

- 值为false，表示将设置为非隐私模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201permissions check fails.401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

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

参数名类型必填说明mode[ImmersiveMode](#ZH-CN_TOPIC_0000002529445255__immersivemode15)是沉浸模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800013window manager service error.

**示例：**

```ets
panel.setImmersiveMode(inputMethodEngine.ImmersiveMode.LIGHT_IMMERSIVE);
```

#### getImmersiveMode15+

getImmersiveMode(): ImmersiveMode

获取输入法应用的沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明[ImmersiveMode](#ZH-CN_TOPIC_0000002529445255__immersivemode15)沉浸模式。

**示例：**

```ets
let mode: inputMethodEngine.ImmersiveMode = panel.getImmersiveMode();
```

#### setImmersiveEffect20+

setImmersiveEffect(effect: ImmersiveEffect): void

设置输入法应用的沉浸效果。

- 只有在[启用沉浸式模式](#ZH-CN_TOPIC_0000002529445255__setimmersivemode15)时，才能使用渐变模式和流光模式。
- 只有在启用渐变模式时，才能使用流光模式。
- 未启用渐变模式时，渐变高度必须为0px。
- 只有系统应用才能设置流光模式。
- 必须先调用以下任一接口，才能调用当前接口：

  - [adjustPanelRect](#ZH-CN_TOPIC_0000002529445255__adjustpanelrect12)(支持API version 12)
  - [adjustPanelRect](#ZH-CN_TOPIC_0000002529445255__adjustpanelrect15)(支持API version 15)
  - [resize](#ZH-CN_TOPIC_0000002529445255__resize10)(支持API version 10)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明effect[ImmersiveEffect](#ZH-CN_TOPIC_0000002529445255__immersiveeffect20)是沉浸效果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息801capability not supported.12800002input method engine error. Possible causes:1.input method panel not created. 2.the input method application does not subscribe to related events.12800013window manager service error.12800020invalid immersive effect. 1.The gradient mode and the fluid light mode can only be used when the immersive mode is enabled. 2.The fluid light mode can only be used when the gradient mode is enabled. 3.When the gradient mode is not enabled, the gradient height can only be 0.12800021this operation is allowed only after adjustPanelRect or resize is called.

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

参数名类型必填说明isKeepScreenOnboolean是是否设置屏幕常亮。true表示打开屏幕常亮，false表示关闭屏幕常亮。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800013window manager service error.

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

参数名类型必填说明displayIdnumber是输入法键盘所在屏幕的displayId，可通过[getDisplayId](#ZH-CN_TOPIC_0000002529445255__getdisplayid15)获取

**返回值：**

类型说明Promise<[SystemPanelInsets](#ZH-CN_TOPIC_0000002529445255__systempanelinsets21)>Promise对象。输入法键盘与系统面板的偏移区域。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800013window manager service error.12800017invalid panel type or panel flag. Possible causes: 1. Current panel's type is not SOFT_KEYBOARD. 2. Panel's flag is not FLG_FIXED or FLG_FLOATING.12800022invalid displayId.

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

参数名类型必填说明fillColorstring|undefined是功能键的颜色，取值范围为[#01000000, #FFFFFFFF] 或 [#000000, #FFFFFF]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。backgroundColorstring|undefined是功能键的背景颜色，取值范围为[#01000000, #FFFFFFFF] 或 [#000000, #FFFFFF]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果。

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

下列API均需使用[on('inputStart')](#ZH-CN_TOPIC_0000002529445255__oninputstart9)获取到KeyboardController实例后，通过实例调用。

#### hide9+

hide(callback: AsyncCallback<void>): void

隐藏输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

从API version 8开始支持，API version 9开始废弃，建议使用[hide](#ZH-CN_TOPIC_0000002529445255__hide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。

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

从API version 8开始支持，API version 9开始废弃，建议使用[hide](#ZH-CN_TOPIC_0000002529445255__hide9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

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

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当退出当前输入类型成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800008input method manager service error. Possible cause: a system error, such as null pointer, IPC exception.12800010not the preconfigured default input method.

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

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800008input method manager service error. Possible cause: a system error, such as null pointer, IPC exception.12800010not the preconfigured default input method.

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

名称值说明BASIC0基础访问模式，基础打字模式，会限制网络访问。FULL1完全访问模式，不做限制，可以访问网络。

#### ExtendAction10+

编辑框中文本的扩展编辑操作类型，如剪切、复制等。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

名称值说明SELECT_ALL0全选。CUT3剪切。COPY4复制。PASTE5粘贴。

#### Direction10+

光标的移动方向。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

名称值说明CURSOR_UP1向上。CURSOR_DOWN2向下。CURSOR_LEFT3向左。CURSOR_RIGHT4向右。

#### Range10+

选中的文本范围。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明startnumber否否选中文本的首字符在编辑框的索引值。endnumber否否选中文本的末字符在编辑框的索引值。

#### Movement10+

选中文本时，光标移动的方向

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明direction[Direction](#ZH-CN_TOPIC_0000002529445255__direction10)否否选中文本时，光标的移动方向。

#### MessageHandler15+

自定义通信对象。

开发者可通过注册此对象来接收已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，接收到自定义通信数据时会触发此对象中[onMessage](#ZH-CN_TOPIC_0000002529445255__onmessage15)回调函数。

此对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)回调函数。

若取消注册全局已注册的对象时，会触发被取消对象中[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)回调函数。

#### onMessage15+

onMessage(msgId: string, msgParam?: ArrayBuffer): void

接收已绑定当前输入法应用的编辑框应用发送的自定义数据回调函数。

当已注册的[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)接收到来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据时，会触发该回调函数。

msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明msgIdstring是接收到的自定义通信数据的标识符。msgParamArrayBuffer否接收到的自定义通信数据的消息体。

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
      }
      inputClient.recvMessage(messageHandler);
    });
```

#### onTerminated15+

onTerminated(): void

监听对象终止回调函数。

当应用注册新的[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)对象时，会触发上一个已注册[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)对象的[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)回调函数。

当应用取消注册时，会触发当前已注册[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)对象的[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)回调函数。

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
      }
      inputClient.recvMessage(messageHandler);
    });
```

#### InputClient9+

下列API均需使用[on('inputStart')](#ZH-CN_TOPIC_0000002529445255__oninputstart9)获取到InputClient实例后，通过实例调用。

#### sendKeyFunction9+

sendKeyFunction(action:number, callback: AsyncCallback<boolean>): void

发送功能键。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明actionnumber是

功能键键值。

- 当值为0时，表示无效按键。

- 当值为1时，表示确认键（即回车键）。

callbackAsyncCallback<boolean>是回调函数。当功能键发送成功，err为undefined，data为true；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明actionnumber是

功能键键值。

当值为0时，表示无效按键；

当值为1时，表示确认键（即回车键）。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示功能键发送成功；返回false表示功能键发送失败。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<string>是回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0

**返回值：**

类型说明Promise<string>Promise对象，返回光标前固定长度的文本。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明string返回光标前固定长度的文本。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<string>是回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明Promise<string>Promise对象，返回光标后固定长度的文本。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明string返回光标后固定长度的文本。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<boolean>是回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<boolean>是回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明textstring是文本内容。callbackAsyncCallback<boolean>是回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明textstring是文本。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明textstring是文本内容。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800002input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

**示例：**

```ets
inputClient.insertTextSync('test');
```

#### getEditorAttribute9+

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

获取编辑框属性值。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明callbackAsyncCallback<[EditorAttribute](#ZH-CN_TOPIC_0000002529445255__editorattribute)>是回调函数。当编辑框属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

类型说明Promise<[EditorAttribute](#ZH-CN_TOPIC_0000002529445255__editorattribute)>Promise对象，返回编辑框属性值。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

类型说明[EditorAttribute](#ZH-CN_TOPIC_0000002529445255__editorattribute)编辑框属性对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明directionnumber是

光标移动方向。

- 当值为1时，表示向上。

- 当值为2时，表示向下。

- 当值为3时，表示向左。

- 当值为4时，表示向右。不能小于0。

callbackAsyncCallback<void>是回调函数。当光标移动成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明directionnumber是

光标移动方向。

- 当值为1时，表示向上。

- 当值为2时，表示向下。

- 当值为3时，表示向左。

- 当值为4时，表示向右。不能小于0。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明directionnumber是

光标移动方向。

- 当值为1时，表示向上。

- 当值为2时，表示向下。

- 当值为3时，表示向左。

- 当值为4时，表示向右。不能小于0。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

**示例：**

```ets
inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR_UP);
```

#### selectByRange10+

selectByRange(range: Range, callback: AsyncCallback<void>): void

根据索引范围选中文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明range[Range](#ZH-CN_TOPIC_0000002529445255__range10)是选中文本的范围。callbackAsyncCallback<void>是回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明range[Range](#ZH-CN_TOPIC_0000002529445255__range10)是选中文本的范围。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明range[Range](#ZH-CN_TOPIC_0000002529445255__range10)是选中文本的范围。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明movement[Movement](#ZH-CN_TOPIC_0000002529445255__movement10)是选中时光标移动的方向。callbackAsyncCallback<void>是回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明movement[Movement](#ZH-CN_TOPIC_0000002529445255__movement10)是选中时光标移动的方向。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明movement[Movement](#ZH-CN_TOPIC_0000002529445255__movement10)是选中时光标移动的方向。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.

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

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当文本索引获取成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

类型说明Promise<number>Promise对象，返回光标所在处的文本索引。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

类型说明number返回光标所在处的文本索引。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

**示例：**

```ets
let index: number = inputClient.getTextIndexAtCursorSync();
console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

#### sendExtendAction10+

sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void

发送扩展编辑操作。使用callback异步回调。

输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](@ohos.inputMethod (输入法框架).md#ZH-CN_TOPIC_0000002529285281__onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](#ZH-CN_TOPIC_0000002529445255__extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明action[ExtendAction](#ZH-CN_TOPIC_0000002529445255__extendaction10)是要发送的扩展操作。callbackAsyncCallback<void>是回调函数。发送成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](@ohos.inputMethod (输入法框架).md#ZH-CN_TOPIC_0000002529285281__onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](#ZH-CN_TOPIC_0000002529445255__extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明action[ExtendAction](#ZH-CN_TOPIC_0000002529445255__extendaction10)是要发送的扩展操作。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800006input method controller error. Possible cause: create InputMethodController object failed.

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

参数名类型必填说明commandDataRecord<string, [CommandDataType](#ZH-CN_TOPIC_0000002529445255__commanddatatype12)>是私有数据。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800010not the preconfigured default input method.

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

本接口仅适用于适配使用[Panel](#ZH-CN_TOPIC_0000002529445255__panel10)作为软键盘窗口的输入法应用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明Promise<[WindowInfo](#ZH-CN_TOPIC_0000002529445255__windowinfo12)>Promise对象，返回拉起输入法的输入框所在应用窗口信息。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800012the input method panel does not exist.12800013window manager service error.

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

参数名类型必填说明textstring是将被预上屏的文本。range[Range](#ZH-CN_TOPIC_0000002529445255__range10)是

目标替换的文本范围。

- 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。

- 当start等于end，默认将参数text插入start对应的光标位置。

- 当start不等于end，将参数text替换range对应区域的文本。

- 当start与end为其他含有负数值的组合，按照参数错误返回。

- 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。

- 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800011text preview not supported.

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

参数名类型必填说明textstring是将被预上屏的文本。range[Range](#ZH-CN_TOPIC_0000002529445255__range10)是

目标替换的文本范围。

- 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。

- 当start等于end，默认将参数text插入start对应的光标位置。

- 当start不等于end，将参数text替换range对应区域的文本。

- 当start与end为其他含有负数值的组合，按照参数错误返回。

- 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。

- 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800011text preview not supported.

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

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)。

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800011text preview not supported.

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

错误码ID错误信息12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800011text preview not supported.

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

参数名类型必填说明msgIdstring是需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的标识符。msgParamArrayBuffer否需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的消息体。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length.12800003input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons.12800009input method client detached.12800014the input method is in basic mode.12800015the other side does not accept the request.12800016input method client is not editable.

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

[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)回调函数。

未填写参数，则取消全局已注册的[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)，并会触发被取消注册对象中[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明msgHandler[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)否

该对象将通过[onMessage](#ZH-CN_TOPIC_0000002529445255__onmessage15)接收来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，并通过[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)接收终止此对象订阅的消息。

若不填写此参数，则取消全局已注册的[MessageHandler](#ZH-CN_TOPIC_0000002529445255__messagehandler15)对象，同时触发其[onTerminated](#ZH-CN_TOPIC_0000002529445255__onterminated15)回调函数。

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](输入法框架错误码.md)，[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401parameter error. Possible causes: 1. Incorrect parameter types.

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
      }
      inputClient.recvMessage(messageHandler);
    });
```

#### getAttachOptions19+

getAttachOptions(): AttachOptions

获取绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明[AttachOptions](#ZH-CN_TOPIC_0000002529445255__attachoptions19)返回绑定输入法时的附加选项内容。

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

参数名类型必填说明typestring是绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。callbackCallback<[AttachOptions](#ZH-CN_TOPIC_0000002529445255__attachoptions19)>是回调函数，返回绑定输入法时的附加选项。

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

参数名类型必填说明typestring是绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。callbackCallback<[AttachOptions](#ZH-CN_TOPIC_0000002529445255__attachoptions19)>否取消订阅的回调函数。参数不填写时，默认取消订阅type对应的所有回调事件。

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

名称值说明NONE0不进行任何首字母大写处理。SENTENCES1每个句子的首字母大写。WORDS2每个单词的首字母大写。CHARACTERS3每个字母都大写。

#### EditorAttribute

编辑框属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明enterKeyTypenumber是否编辑框的功能属性，详见[常量中的功能键定义](#ZH-CN_TOPIC_0000002529445255__常量)。inputPatternnumber是否编辑框的文本属性，详见[常量中的编辑框定义](#ZH-CN_TOPIC_0000002529445255__常量)。isTextPreviewSupported12+boolean否否

编辑框是否支持预上屏。

- 值为true，表示支持。

- 值为false，表示不支持。

bundleName14+string是是编辑框所属应用包名；该值可能为""，使用该属性时需要考虑为""的场景。immersiveMode15+[ImmersiveMode](#ZH-CN_TOPIC_0000002529445255__immersivemode15)是是输入法沉浸模式。windowId18+number是是编辑框设置所属窗口ID。displayId18+number是是编辑框设置窗口对应的屏幕ID。如果没有设置windowId，取当前焦点窗口屏幕ID。placeholder20+string是是编辑框设置的占位符信息。abilityName20+string是是编辑框设置的ability名称。capitalizeMode20+[CapitalizeMode](#ZH-CN_TOPIC_0000002529445255__capitalizemode20)是是编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。gradientMode20+[GradientMode](#ZH-CN_TOPIC_0000002529445255__gradientmode20)是是渐变模式。如果没有设置或设置非法值，默认不使用渐变模式。extraConfig22+[InputMethodExtraConfig](zh-cn_topic_0000002497445312.html#ZH-CN_TOPIC_0000002497445312__inputmethodextraconfig)是是输入法扩展信息。

#### KeyEvent

按键属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明keyCodenumber是否按键的键值。键码值说明参考[KeyCode](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)。keyActionnumber是否

按键事件类型。

- 当值为2时，表示按下事件；

- 当值为3时，表示抬起事件。

#### PanelFlag10+

输入法面板状态类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称值说明FLG_FIXED0固定态面板类型。FLG_FLOATING1悬浮态面板类型。FLAG_CANDIDATE15+2候选词态面板类型。

#### PanelType10+

输入法面板类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称值说明SOFT_KEYBOARD0软键盘类型。STATUS_BAR1状态栏类型。

#### PanelInfo10+

输入法面板属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明type[PanelType](#ZH-CN_TOPIC_0000002529445255__paneltype10)否否面板的类型。flag[PanelFlag](#ZH-CN_TOPIC_0000002529445255__panelflag10)否是面板的状态类型。

#### PanelRect12+

输入法面板位置大小信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明landscapeRect[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)否否横屏状态时输入法面板窗口的位置大小。portraitRect[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)否否竖屏状态时输入法面板窗口的位置大小。

#### EnhancedPanelRect15+

增强的输入法面板位置、大小信息，包含自定义避让区域、自定义热区。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明landscapeRect[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)否是

横屏状态时输入法面板窗口的位置大小。

- 当fullScreenMode不填写或值为false时，此属性为必选。

portraitRect[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)否是

竖屏状态时，输入法面板窗口的位置大小。

- 当fullScreenMode不填写或值为false时，此属性为必选。

landscapeAvoidYnumber否是

横屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。

- 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。

- 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。

landscapeInputRegionArray<[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)>否是

横屏状态时，面板接收输入事件的区域。

- 数组大小限制为[1, 4]。默认值为横屏时的面板大小。

- 传入的热区位置是相对于输入法面板窗口左顶点的位置。

portraitAvoidYnumber否是

竖屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。

- 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。

- 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。

portraitInputRegionArray<[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)>否是

竖屏状态时，面板接收输入事件的区域。

- 数组大小限制为[1, 4]。默认值为竖屏时的面板大小。

- 传入的热区位置是相对于输入法面板窗口左顶点的位置。

fullScreenModeboolean否是

是否开启全屏模式。默认值为false。

- 值为true，landscapeRect和portraitRect可不填写。

- 值为false，landscapeRect和portraitRect为必选属性。

#### KeyboardArea15+

面板中的键盘区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明topnumber否否键盘区域的上边界到面板区域上边界的距离，单位为px，该参数为整数。bottomnumber否否键盘区域的下边界到面板区域下边界的距离，单位为px，该参数为整数。leftnumber否否键盘区域的左边界到面板区域左边界的距离，单位为px，该参数为整数。rightnumber否否键盘区域的右边界到面板区域右边界的距离，单位为px，该参数为整数。

#### AttachOptions19+

绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明requestKeyboardReason[RequestKeyboardReason](#ZH-CN_TOPIC_0000002529445255__requestkeyboardreason19)否是该属性由编辑框应用设置，如果没有设置或设置非法值，则默认没有特定的原因触发键盘请求。isSimpleKeyboardEnabled20+boolean否是

是否使能简单键盘，该属性由编辑框应用设置，true表示使能简单键盘，false表示不使能简单键盘。

如果没有设置或设置非法值，则默认不使能简单键盘。

#### WindowInfo12+

窗口信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明rect[window.Rect](Interfaces (其他).md#ZH-CN_TOPIC_0000002529284795__rect7)否否窗口矩形区域。status[window.WindowStatusType](Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)否否窗口模式类型。

#### ImmersiveMode15+

枚举，输入法沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称值说明NONE_IMMERSIVE0不使用沉浸模式。IMMERSIVE1沉浸模式，由输入法应用确定沉浸模式类型。LIGHT_IMMERSIVE2浅色沉浸模式。DARK_IMMERSIVE3深色沉浸模式。

#### RequestKeyboardReason19+

枚举，请求键盘输入的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称值说明NONE0表示没有特定的原因触发键盘请求。MOUSE1表示键盘请求是由鼠标操作触发的。TOUCH2表示键盘请求是由触摸操作触发的。OTHER20表示键盘请求是由其他原因触发的。

#### GradientMode20+

枚举，输入法渐变模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称值说明NONE0不使用渐变模式。LINEAR_GRADIENT1线性渐变。

#### ImmersiveEffect20+

沉浸效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明gradientHeightnumber否否渐变高度，不能超过屏幕高度的15%。gradientMode[GradientMode](#ZH-CN_TOPIC_0000002529445255__gradientmode20)否否渐变模式。

#### SystemPanelInsets21+

输入法软键盘相对系统面板的偏移区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明bottomnumber是否键盘区域的下边界到系统面板区域下边界的距离，单位为px，该参数为整数。leftnumber是否键盘区域的左边界到系统面板区域左边界的距离，单位为px，该参数为整数。rightnumber是否键盘区域的右边界到系统面板区域右边界的距离，单位为px，该参数为整数。

#### TextInputClient(deprecated)

下列API示例中都需使用[on('inputStart')](#ZH-CN_TOPIC_0000002529445255__oninputstart)回调获取到TextInputClient实例，再通过此实例调用对应方法。

从API version 8开始支持，API version 9开始废弃，建议使用[InputClient](#ZH-CN_TOPIC_0000002529445255__inputclient9)替代。

#### getForward(deprecated)

getForward(length:number, callback: AsyncCallback<string>): void

获取光标前固定长度的文本。使用callback异步回调。

从API version 8开始支持，API version 9开始废弃，建议使用[getForward](#ZH-CN_TOPIC_0000002529445255__getforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<string>是回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。

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

从API version 8开始支持，API version 9开始废弃，建议使用[getForward](#ZH-CN_TOPIC_0000002529445255__getforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明Promise<string>Promise对象，返回光标前固定长度的文本。

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

从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](#ZH-CN_TOPIC_0000002529445255__getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<string>是回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。

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

从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](#ZH-CN_TOPIC_0000002529445255__getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明Promise<string>Promise对象，返回光标后固定长度的文本。

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

从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](#ZH-CN_TOPIC_0000002529445255__deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<boolean>是回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。

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

从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](#ZH-CN_TOPIC_0000002529445255__deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。

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

从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](#ZH-CN_TOPIC_0000002529445255__deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。callbackAsyncCallback<boolean>是回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。

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

从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](#ZH-CN_TOPIC_0000002529445255__deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明lengthnumber是文本长度。不能小于0。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。

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

从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](#ZH-CN_TOPIC_0000002529445255__sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明actionnumber是

功能键键值。

- 当值为0时，表示无效按键；

- 当值为1时，表示确认键（即回车键）。

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

从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](#ZH-CN_TOPIC_0000002529445255__sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明actionnumber是

功能键键值。

当值为0时，表示无效按键；

当值为1时，表示确认键（即回车键）。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示发送功能键成功；返回false表示发送功能键失败。

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

从API version 8开始支持，API version 9开始废弃，建议使用[insertText](#ZH-CN_TOPIC_0000002529445255__inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明textstring是文本。callbackAsyncCallback<boolean>是回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。

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

从API version 8开始支持，API version 9开始废弃，建议使用[insertText](#ZH-CN_TOPIC_0000002529445255__inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明textstring是文本。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。

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

从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](#ZH-CN_TOPIC_0000002529445255__geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

参数名类型必填说明callbackAsyncCallback<[EditorAttribute](#ZH-CN_TOPIC_0000002529445255__editorattribute)>是回调函数。当编辑框的属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。

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

从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](#ZH-CN_TOPIC_0000002529445255__geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

类型说明Promise<[EditorAttribute](#ZH-CN_TOPIC_0000002529445255__editorattribute)>Promise对象，返回编辑框属性值。

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