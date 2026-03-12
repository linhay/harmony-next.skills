# Interface (Macro)

Macro 继承自 [MacroQuery](Interface (MacroQuery).md)。

提供使能微距能力的接口。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 19开始支持。

#### 导入模块

```ets
import { camera } from '@kit.CameraKit';
```

#### enableMacro19+

enableMacro(enabled: boolean): void

使能当前的微距能力。

使用该接口前，需要先通过[isMacroSupported](Interface (MacroQuery).md#ZH-CN_TOPIC_0000002497605784__ismacrosupported19)接口查询当前设备是否支持微距能力。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

参数名类型必填说明enabledboolean是是否开启微距能力。true表示开启微距能力，false表示关闭微距能力。

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](Camera错误码.md)。

错误码ID错误信息7400102Operation not allowed.7400103Session not config.

**示例：**

```ets
function enableMacro(photoSession: camera.PhotoSession): void {
  let isSupported: boolean = photoSession.isMacroSupported();
  if (isSupported) {
    photoSession.enableMacro(true);
  }
}
```