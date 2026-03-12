# stylusInteraction (手写笔交互功能)

手写笔交互功能入口类，当前包含手写笔笔身轻捏事件和手写笔笔身双击事件。

**系统能力：**SystemCapability.Stylus.StylusService

**起始版本：**5.1.1(19)

#### 导入模块

```ets
import { stylusInteraction } from '@kit.Penkit';
```

#### stylusInteraction.on('squeeze')

on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void

监听手写笔笔身轻捏事件。

**系统能力：**SystemCapability.Stylus.StylusService

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"squeeze"字符串，表示手写笔笔身轻捏事件。

receiver

Callback<[SqueezeEvent](#section10272152161111)>

是

回调函数，返回手写笔笔身轻捏事件的详细信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`got squeeze event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### stylusInteraction.off('squeeze')

off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void

取消监听手写笔笔身轻捏事件。

**系统能力：**SystemCapability.Stylus.StylusService

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"squeeze"字符串，表示手写笔笔身轻捏事件。

receiver

Callback<[SqueezeEvent](#section10272152161111)>

否

需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的轻捏事件。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`off squeeze event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### stylusInteraction.on('doubleTap')

on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void

监听手写笔笔身双击事件。

**系统能力：**SystemCapability.Stylus.StylusService

**起始版本：**5.1.1(19)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"doubleTap"字符串，表示手写笔笔身双击事件。

receiver

Callback<[DoubleTapEvent](#section4950173171415)>

是

回调函数，返回手写笔笔身双击事件的详细信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`got doubleTap event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### stylusInteraction.off('doubleTap')

off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void

取消监听手写笔笔身双击事件。

**系统能力：**SystemCapability.Stylus.StylusService

**起始版本：**5.1.1(19)

**参数：****：**

参数名

类型

必填

说明

type

string

是

固定填写"doubleTap"字符串，表示手写笔笔身双击事件。

receiver

Callback<[DoubleTapEvent](#section4950173171415)>

否

需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的双击事件。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`off doubleTap event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### SqueezeEvent

手写笔笔身轻捏事件信息。

**系统能力：**SystemCapability.Stylus.StylusService

**起始版本：**5.1.1(19)

**参数：**

名称

**类型**

只读

可选

**说明**

timestamp

number

否

否

时间戳，自系统启动以来经过的时间，单位：ms。

#### DoubleTapEvent

手写笔笔身双击事件信息。

**系统能力：**SystemCapability.Stylus.StylusService

**起始版本：**5.1.1(19)

**参数：**

名称

**类型**

只读

可选

**说明**

timestamp

number

否

否

时间戳，自系统启动以来经过的时间，单位：ms。