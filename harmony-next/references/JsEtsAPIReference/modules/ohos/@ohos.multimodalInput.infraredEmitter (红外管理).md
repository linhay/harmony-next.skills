# @ohos.multimodalInput.infraredEmitter (红外管理)

红外管理模块提供产生特定频率和大小的红外信号，以及查询设备支持的频率范围等功能。

- 本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { infraredEmitter } from '@kit.InputKit';
```

#### infraredEmitter.transmitInfrared

transmitInfrared(infraredFrequency: number, pattern: Array<number>): void

产生特定频率和特定电平大小的红外信号。

**需要权限**：ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

**系统能力**：SystemCapability.MultimodalInput.Input.InfraredEmitter

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| infraredFrequency | number | 是 | 红外频率，单位：Hz。 |
| pattern | Array<number> | 是 | 红外电平信号，单位：μs。电平信号的数量取值范围为[0,1024]。电平信号的取值需大于0。 比如[100,200,300,400]该电平信号数组，其中100us为高电平信号、200us为低电平信号、300us为高电平信号、400us为低电平信号。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed. |

**示例**：

```ets
import { infraredEmitter } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            infraredEmitter.transmitInfrared(38000, [100, 200, 300, 400]);
          } catch (error) {
            console.error(`transmitInfrared failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
```

#### infraredEmitter.getInfraredFrequencies

getInfraredFrequencies(): Array<InfraredFrequency>

查询设备支持的红外信号的频率范围。

**需要权限**：ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

**系统能力**：SystemCapability.MultimodalInput.Input.InfraredEmitter

设备行为差异：该接口在支持红外发射器的Phone和TV设备上返回红外信号的频率范围，在其他不支持红外发射器的设备上返回一组最大和最小频率，且均为0Hz。建议使用[hasIrEmitter](#ZH-CN_TOPIC_0000002553201635__infraredemitterhasiremitter23)接口查询设备是否支持红外发射器。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<InfraredFrequency> | 红外信号的频率范围，包含多组最大和最小频率。 从API version 23开始，当设备不具有红外发射器，返回一组最大和最小频率，且均为0Hz。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例**：

```ets
import { infraredEmitter } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let frequencies = infraredEmitter.getInfraredFrequencies();
            console.info(`frequencies: ${JSON.stringify(frequencies)}`);
          } catch (error) {
            console.error(`Get infrared frequencies failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
```

#### InfraredFrequency

红外信号的频率范围。

**系统能力**：SystemCapability.MultimodalInput.Input.InfraredEmitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| max | number | 否 | 否 | 最大支持频率，单位：Hz。 |
| min | number | 否 | 否 | 最小支持频率，单位：Hz。 |

**infraredEmitter.hasIrEmitter23+**

hasIrEmitter(): Promise<boolean>

查询设备是否配备红外发射器。使用Promise异步回调。

需要权限：ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

系统能力：SystemCapability.MultimodalInput.Input.InfraredEmitter

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 如果设备具有红外发射器，则返回true；否则返回false。 |

错误码：

以下错误码的详细介绍请参见[全局快捷键管理错误码](全局快捷键管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 3800001 | Input service exception. |

示例：

```ets
import { infraredEmitter } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
            infraredEmitter.hasIrEmitter().then((result: boolean) => {
              console.info(`hasIrEmitter: ${JSON.stringify(result)}`);
            }).catch((error: BusinessError)=> {
              console.error(`hasIrEmitter failed: ${JSON.stringify(error)}`);})
        })
    }
```